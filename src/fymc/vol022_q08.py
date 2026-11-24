from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'recalls-removals-and-the-maude-database',
 'question_prompt': 'How do recalls, corrections, and adverse-event reports work, and how can buyers '
                    "research a device's safety history?",
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Recalls, Removals, and the MAUDE Database',
 'subtitle': '21 CFR 806 corrections and removals, recall guidance and litigation, recall vs. warning '
             'letter vs. safety communication, recall prevention, complaint handling and Form 3500A, '
             'searching MAUDE and openFDA, reporting quality, and software/usability recall examples',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one operating rule: a recall is a removal or correction '
                      'of violative product, and under Part 806 the risk-to-health actions get reported '
                      'within 10 working days of the decision to act, not the customer letter. Ex-FDA '
                      'veteran Steve Needelman puts voluntary recalls at 99.999% and favors filing 80% of '
                      'the facts on time over 100% late, while Tim Phillips warns against quiet recalls '
                      'disguised as technical bulletins. On the data side, Abby Smart, Ibrahim Alawad and '
                      "Christina Bernstein all hit MAUDE's 500-record cap; Smart and Alawad split date "
                      'ranges, merge Excel exports and keyword-search narratives. Disagreements center on '
                      'data quality and close-out targets: Health Watch USA finds 96.6% of reports come '
                      'from manufacturers and 0.49% directly from physicians, Jeff Kasof says most firms '
                      'check 100% of customers, and Needelman calls 25% retrieval acceptable.',
 'key_metrics': [{'label': 'MAUDE Single-Search Output Cap',
                  'metric': 'MAUDE Single-Search Output Cap',
                  'value': '500 reports per search',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Abby Smart states the database only returns 500 reports for a single search '
                             'and splits queries into consecutive date ranges to get past it.',
                  'source': 'Ofstead Insights ([a-scTl1C2PA @ 00:08:44])'},
                 {'label': 'Part 806 Reporting Deadline',
                  'metric': 'Part 806 Reporting Deadline',
                  'value': '10 working days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Amanda Johnston states risk-to-health corrections and removals are reported '
                             'to FDA within 10 working days under Part 806.',
                  'source': 'Gardner Law ([aYQu_0ujhyU @ 00:12:43])'},
                 {'label': 'Manufacturer Share of MAUDE Reports',
                  'metric': 'Manufacturer Share of MAUDE Reports',
                  'value': '96.6%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Analysis of roughly 7.5M MAUDE events from 1997 to 2018 using custom '
                             'software; the speaker suggests warranty claims and lawsuits may drive the '
                             'volume.',
                  'source': 'Health Watch USA ([yKomHc_DWtw @ 00:05:20])'},
                 {'label': 'Expected Recall Product Return',
                  'metric': 'Expected Recall Product Return',
                  'value': 'About 30%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Steve Needelman tells firms to expect about 30% product return and to make '
                             'three good-faith attempts to reach each customer.',
                  'source': 'Medmarc ([nJblY5CRIVY @ 00:39:10])'}],
 'sections': [{'number': 1,
               'title': 'The Practitioner Consensus: What Counts as a Recall and Where the Evidence Lives',
               'paragraphs': ['Every practitioner who works the recall side starts from the same '
                              'definition. Amanda Johnston of Gardner Law frames a recall as the removal '
                              'or correction of violative product, explicitly excluding market withdrawals '
                              'and stock recovery [aYQu_0ujhyU @ 00:07:25]. Aaron Snyder compresses Part '
                              "806 into five words, 'report field actions to fda,' and states that all "
                              'Class 1 and Class 2 recalls must be reported within 10 days of initiating '
                              'the recall [8Pgfw2y5xe0 @ 00:01:52]. Steve Needelman, 34 years at FDA '
                              'before joining King & Spalding, sharpens the trigger: the 10 business days '
                              'run from the decision to act, not from the date the customer letter goes '
                              'out [nJblY5CRIVY @ 00:04:43]. Jeff Kasof repeats the number flatly: the '
                              'deadline for issuing the report is 10 working days [1kYC2rBfPPA @ '
                              '00:41:45]. The classes line up the same way across speakers: Class 1 is '
                              'highest risk, Class 2 moderate, Class 3 lowest, and FDA, not the firm, '
                              'assigns the final class, although a company can propose one through its '
                              'health hazard evaluation. Johnston adds that reportability is decided on '
                              'the risk-to-health definition rather than the class definitions, and that '
                              'unreported corrections and removals still require kept records. For anyone '
                              'moving used equipment, that vocabulary is the filter for reading every '
                              'recall entry attached to a unit.',
                              'The second point of agreement is that almost nothing here is forced, and '
                              "that hiding a recall is the expensive move. Needelman says FDA's mandatory "
                              'recall authority has existed since 1990 and been used fewer than 10 times, '
                              "putting voluntary recalls at '99.999%' [nJblY5CRIVY @ 00:05:39]; Johnston "
                              "lands in the 'high 90%' range. Treomark warns against misreading that word: "
                              "'voluntary' describes how a recall began, not how severe it is, and not "
                              'every unit is physically returned [GoXd4_jxKBg @ 00:00:16]. Tim Phillips, '
                              'who spent 12 years as an FDA investigator and 20 as a compliance officer, '
                              "is blunt that recalls cannot be disguised as a 'technical bulletin' and "
                              'that there are no quiet recalls [aYQu_0ujhyU @ 00:34:48]. Needelman backs '
                              'that with a Medrad warning letter as his silent-recall example and a bulb '
                              'hypothetical: failures at 22 to 23 months are not a recall, failures at 8 '
                              'to 9 months are, and a depleted backup battery is a recall [nJblY5CRIVY @ '
                              '00:51:13]. David Graham, a litigator with 35-plus years, explains why it '
                              'matters downstream: a recall makes information public, and an opaque one '
                              "turns a 'bad device case' into a 'bad company case.' Graham's working "
                              'assumption is that every document goes public eventually.',
                              'On the data side, the consensus is that MAUDE is free, public, and badly '
                              'limited, and that operators should use it anyway. Abby Smart, an '
                              'epidemiologist at Ofstead Insights, dates the database to 1991 and notes it '
                              'is searchable for 10 years of reports [a-scTl1C2PA @ 00:01:12]; Dr. Ibrahim '
                              'Alawad gives the same 1991 start and 10-year window, and Dr. Hashem '
                              'stresses that no hospital data is needed because the database is free and '
                              'public. Three speakers independently hit the same wall when pulling large '
                              'device histories: output is capped at 500 records per search. Alawad says '
                              "flatly 'It only gives you back' 500 records [a_T4LqfP6zE @ 00:25:33], and "
                              'Christina Bernstein adds that roughly 500 records arrive every two weeks, '
                              'so the cap bites fast [xbxXTRwdVRs @ 00:22:47]. Gene Parunak reports '
                              "'pushback' that not every event reaches MAUDE, and that exemptions, "
                              'variances and alternative reporting are excluded [0dpHnJj93Ns @ 00:00:25]. '
                              'Smart also lists underreporting, late-arriving reports, redactions, and '
                              "FDA's own statement that MAUDE cannot assess prevalence. Bernstein's rule "
                              'closes the loop: a record is not causation, so public data has to be '
                              'cross-checked against manufacturer claims, patient records and FDA findings '
                              'before anyone builds a decision on it.'],
               'table': {'caption': 'Where the recall and MAUDE practitioners agree',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operational Detail',
                                     'Expert Source'],
                         'rows': [['Part 806 reporting clock starts at the decision',
                                   'Class 1 and 2 corrections and removals reported within 10 business '
                                   'days of the decision to act',
                                   'Date the recall decision itself, never the date the customer letter '
                                   'was mailed',
                                   'Medmarc ([nJblY5CRIVY @ 00:04:43])'],
                                  ['A recall means removal or correction of violative product',
                                   'Market withdrawals and stock recovery sit entirely outside the recall '
                                   'definition',
                                   'Decide reportability on the risk-to-health definition, never on the '
                                   'class definitions',
                                   'Gardner Law ([aYQu_0ujhyU @ 00:07:25])'],
                                  ['Voluntary recalls dominate the entire device market',
                                   'Mandatory recall authority exists since 1990 but used fewer than 10 '
                                   'times',
                                   'Stay transparent with the district recall coordinator throughout the '
                                   'whole recall',
                                   'Medmarc ([nJblY5CRIVY @ 00:05:39])'],
                                  ['Quiet or disguised recalls are never acceptable',
                                   'Recalls cannot be relabeled as a technical bulletin or run quietly',
                                   'Software fixes for risk-to-health bugs likely count as corrections as '
                                   'well',
                                   'Gardner Law ([aYQu_0ujhyU @ 00:34:48])'],
                                  ['MAUDE output is capped for every single search',
                                   'Advanced search returns at most 500 reports for any one query',
                                   'Split into consecutive date ranges, then merge the exported Excel '
                                   'files afterward',
                                   'Ofstead Insights ([a-scTl1C2PA @ 00:08:44])'],
                                  ['A MAUDE record does not establish causation',
                                   'Duplicate narratives exist because clinical sites and manufacturers '
                                   'each file separate reports',
                                   'Cross-check against manufacturer claims, patient records and FDA '
                                   'findings before concluding',
                                   'Expert Institute ([xbxXTRwdVRs @ 00:15:00])'],
                                  ['Complete records are what auditors check first',
                                   'Missing signatures, missing approvals, ignored field issues and absent '
                                   'procedures are warning signs',
                                   'Know how many field actions happened in three years and how many were '
                                   'reported',
                                   'Quality Systems Explained ([8Pgfw2y5xe0 @ 00:02:29])']]}},
              {'number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers: Searching MAUDE and Running the Recall',
               'paragraphs': ['The search workflow is consistent across three teachers. Smart skips simple '
                              'search because it returns irrelevant hits and misses inexact terms, warning '
                              "that MAUDE 'doesn't work like Google.' Smart starts with product class, "
                              'then layers manufacturer, model or brand, widens the default one-month date '
                              'range, and deliberately leaves the event-type filter off because '
                              'malfunction reports may describe injuries [a-scTl1C2PA @ 00:02:55]. Results '
                              'get exported to Excel; Smart reads the event description first, then the '
                              "manufacturer narrative. Smart's worked example, a robotic surgical system "
                              'from October 2018 to October 2020, returned almost 300 reports, which were '
                              "scanned by 'device problem,' then 'event text,' using Find & Select "
                              '[a-scTl1C2PA @ 00:06:59]. Alawad ran the same play on the da Vinci Xi: 293 '
                              "records, then Ctrl+F for 'broken cable' produced 2 hits, one of them a "
                              'death [a_T4LqfP6zE @ 00:21:38]. Ann McLain shows the faster general route: '
                              'product-problem dropdown, product class, and event type; a battery issue '
                              'plus malfunction for the first month of the year returned 332 records, '
                              'sortable by manufacturer, brand or date [OS2unSk68KQ @ 00:01:52]. For a '
                              'known product, McLain goes to the device classification database, pulls the '
                              'product code, and opens the Total Product Lifecycle report, which lists '
                              'every recorded device problem in one view.',
                              'When a search breaks, the fixes are mechanical. Zero results means widening '
                              'dates, dropping brand, including all event types, trying manufacturer-name '
                              "variants and checking spelling; Alawad's example of name variants is Rosh "
                              'versus Rocher [a_T4LqfP6zE @ 00:24:33]. Too many results means splitting '
                              'the window: Smart cuts the query into consecutive date ranges and merges '
                              'them [a-scTl1C2PA @ 00:08:44], and Alawad used the same split-and-merge to '
                              'pull about 1,000 bronchoscope records over 2 years. Empty narratives are '
                              'sometimes filled in later, and gaps get backfilled from the IFU, '
                              'manufacturer site, YouTube, journals and newsletters. Bernstein runs '
                              "openFDA instead of the web form: querying the brand 'Pelace' took about 10 "
                              'seconds and returned 656 injuries, 13 malfunctions and 2 other events, and '
                              'the same query URL accepts any brand name substituted in [xbxXTRwdVRs @ '
                              '00:09:28]. Because CRB carries about 20 mesh brand names, Bernstein queries '
                              "the exact product, finds codes by searching 'FDA product code, manufacturer "
                              "name, brand name,' and treats the TPLC report as the recall history. The "
                              'read is comparative: if one manufacturer has all the recalls, suspect that '
                              'manufacturer; if all of them do, suspect the product type. Parunak adds '
                              'that bulk voluntary-report zips go back to June 1993 [0dpHnJj93Ns @ '
                              '00:00:45].',
                              'On execution, the numbers are tight. Phillips lays out a timeline: issue '
                              'identified on Day 0, health hazard evaluation on Days 1 to 3, the recall '
                              'decision on Day 5 starting the 806 clock, strategy and notifications on '
                              'Days 6 and 7, and Day 15 as the latest compliant report [aYQu_0ujhyU @ '
                              "00:21:52]. David Pudwell's checklist for the FDA package covers product "
                              'name, catalog numbers, lot, serial and UDI, quantities, a consignee list, '
                              'and notices to both ship-to and bill-to; notices should be directed rather '
                              'than indiscriminate so customers are not desensitized [sNeRd4nIrG8 @ '
                              '00:14:34]. Needelman insists on certified mail or verifiable receipt rather '
                              'than email or phone, separates units sold from units used, expects about '
                              '30% product return, and requires three good-faith attempts [nJblY5CRIVY @ '
                              '00:39:10]. Pudwell wants monthly status reports carrying root cause and '
                              'CAPA each time, while Kasof recommends status reports every two to four '
                              'weeks and notes most firms run effectiveness checks on 100% of customers '
                              '[1kYC2rBfPPA @ 00:46:51]. Kasof numbers each report by registration number, '
                              'date, sequence and type, and sends customer letters by mail merge. '
                              "Needelman's rule on completeness settles the tension: 80% of the "
                              "information on time beats 100% late, and a report full of 'to be "
                              "determined' entries has no value."],
               'table': {'caption': 'Exact search settings, recall numbers and cadences taught by the '
                                    'practitioners',
                         'headers': ['Mechanic',
                                     'Exact Number or Setting',
                                     'How Practitioners Run It',
                                     'Expert Source'],
                         'rows': [['MAUDE single-search output cap on advanced search',
                                   '500 reports returned for any single search query',
                                   'Split consecutive date ranges, export each range to Excel, then merge',
                                   'Ofstead Insights ([a-scTl1C2PA @ 00:08:44])'],
                                  ['Robotic surgical system keyword sweep through narratives',
                                   "293 records, 2 'broken cable' hits, one of them a death",
                                   'Export the results, then Ctrl+F the narratives for failure keywords',
                                   'Dr. Hashem Abu Serhan ([a_T4LqfP6zE @ 00:21:38])'],
                                  ['openFDA brand-name query run against a mesh product',
                                   'About 10 seconds; 656 injuries, 13 malfunctions, 2 other events',
                                   'Substitute the exact brand name into the same openFDA query URL',
                                   'Expert Institute ([xbxXTRwdVRs @ 00:09:28])'],
                                  ['General product-problem search across all manufacturers',
                                   '332 records for battery issue plus malfunction in one month',
                                   'Product problem dropdown, product class, event type, then sort results',
                                   'Koven Technology Canada ([OS2unSk68KQ @ 00:01:52])'],
                                  ['Recall timeline from issue identification to FDA report',
                                   'Day 5 recall decision starts clock; Day 15 latest compliant report',
                                   'Health hazard evaluation Days 1 to 3, strategy and notifications Days '
                                   '6 to 7',
                                   'Gardner Law ([aYQu_0ujhyU @ 00:21:52])'],
                                  ['Product return expectation during an active recall',
                                   'About 30% product return expected from the field',
                                   'Three good-faith attempts using certified mail or verifiable receipt',
                                   'Medmarc ([nJblY5CRIVY @ 00:39:10])'],
                                  ['Status report cadence and effectiveness check depth',
                                   'Status reports every two to four weeks; checks on 100% of customers',
                                   'Number each report by registration number, date, sequence and type',
                                   'GlobalCompliance Panel ([1kYC2rBfPPA @ 00:46:51])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Search and Recall Moves the Practitioners Actually Use',
                           'body': 'These are the small settings and habits that separate a usable MAUDE '
                                   'pull or a clean recall file from a pile of noise [Ofstead Insights — '
                                   'a-scTl1C2PA @ 00:03:32].',
                           'items': ['Leave the event-type filter off: malfunction reports may describe '
                                     'injuries, so filtering by event type hides real harm [Ofstead '
                                     'Insights — a-scTl1C2PA @ 00:03:32].',
                                     'Collect every keyword and brand variant before searching; Alawad '
                                     "found 'fericim map' listed under 'Vabismo' [Dr. Hashem Abu Serhan — "
                                     'a_T4LqfP6zE @ 00:20:33].',
                                     'Match lot, serial, model and dates against the recall itself, and '
                                     'work from the current agency page rather than screenshots [Treomark '
                                     '— GoXd4_jxKBg @ 00:00:33].',
                                     'Get the letter and strategy in front of FDA before launch; Phillips '
                                     "says review has no guaranteed time but expect 'hours... a day or "
                                     "two' [Gardner Law — aYQu_0ujhyU @ 00:27:01]."]},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the FDA product code',
                              'action': 'Look up the device in the Device Classification database and '
                                        'record its product code before touching MAUDE.',
                              'detail': 'McLain uses the device classification database to find the '
                                        'product code and then opens the TPLC product code report [Koven '
                                        'Technology Canada — OS2unSk68KQ @ 00:02:12]; Bernstein finds '
                                        "codes by searching 'FDA product code, manufacturer name, brand "
                                        "name,' with LWJ for a hip implant as the example [Expert "
                                        'Institute — xbxXTRwdVRs @ 00:19:34].'},
                             {'step': 2,
                              'title': 'Run an advanced MAUDE search wide',
                              'action': 'Start with product class, add manufacturer, model or brand, widen '
                                        'the date range past the one-month default, and include all event '
                                        'types.',
                              'detail': 'Smart skips simple search, starts with product class, widens the '
                                        'default last-month window, and keeps all event types because '
                                        'malfunctions may describe injuries [Ofstead Insights — '
                                        'a-scTl1C2PA @ 00:02:55].'},
                             {'step': 3,
                              'title': 'Beat the 500-record cap and sweep the narratives',
                              'action': 'Split large pulls into consecutive date ranges, export each to '
                                        'Excel, merge, then keyword-search device problem and event text '
                                        'fields.',
                              'detail': 'Alawad splits date ranges and merges the Excel files, pulling '
                                        'about 1,000 bronchoscope records over 2 years, then uses Ctrl+F '
                                        'on the narratives [Dr. Hashem Abu Serhan — a_T4LqfP6zE @ '
                                        '00:25:33].'},
                             {'step': 4,
                              'title': 'Read the recall history comparatively',
                              'action': 'Treat the TPLC report as the recall history and compare recall '
                                        'counts across every manufacturer of the same product type.',
                              'detail': "Bernstein's rule: if one manufacturer has all the recalls, "
                                        'suspect that manufacturer; if all of them do, suspect the product '
                                        'type, and never treat a single record as causation [Expert '
                                        'Institute — xbxXTRwdVRs @ 00:21:28].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The 806 clock is the first place the experts split, and the split is over '
                              'what starts it. Aaron Snyder of Quality Systems Explained gives the '
                              'shorthand: every Class 1 and Class 2 recall goes to FDA within 10 days of '
                              'initiating the recall [8Pgfw2y5xe0 @ 00:01:52]. Steve Needelman, who spent '
                              '34 years at FDA before joining King & Spalding, moves the trigger upstream: '
                              '10 business days from the decision to act, not from the day the customer '
                              'letter goes out [nJblY5CRIVY @ 00:04:43]. Tim Phillips, 12 years an FDA '
                              'investigator and 20 a compliance officer, runs it as a calendar: issue '
                              'found on Day 0, health hazard evaluation on Days 1 to 3, the recall '
                              'decision on Day 5 starting the clock, strategy and notifications on Days 6 '
                              'and 7, and Day 15 as the latest compliant report [aYQu_0ujhyU @ 00:21:52]. '
                              'Amanda Johnston, the Gardner Law partner on the same panel, breaks from the '
                              'class-based shorthand entirely: decide reportability with the '
                              'risk-to-health definition, not the class definitions; FDA assigns the class '
                              'itself, and a company only proposes one through its HHE [aYQu_0ujhyU @ '
                              '00:17:54]. Operators who count from letter dates, or who wait for a class '
                              'before deciding whether to report, are working off the softer version of '
                              'the rule.',
                              'Everyone who pulls MAUDE hits the same wall, then climbs it differently. '
                              'Abby Smart, the Ofstead epidemiologist, says the database returns only 500 '
                              'reports per search, so they split the window into consecutive date ranges '
                              'and merge the exports [a-scTl1C2PA @ 00:08:44]. Dr. Ibrahim Alawad runs the '
                              'identical split-and-merge in Excel and pulled roughly 1,000 bronchoscope '
                              'records over two years that way [a_T4LqfP6zE @ 00:25:33]. Christina '
                              'Bernstein, the ASQ-certified auditor working as an expert witness, skips '
                              'the spreadsheet grind: MAUDE returns 500 records at a time while roughly '
                              '500 new ones land every two weeks, so they hit the openFDA query URL, swap '
                              'in a brand name, and had 656 injuries, 13 malfunctions and 2 other events '
                              'for the Pelace mesh brand in about 10 seconds, after warning that one maker '
                              'sells about 20 mesh brand names, so the exact product must be queried '
                              '[xbxXTRwdVRs @ 00:09:28]. The second split is filtering. Ann McLain filters '
                              'on event type up front, and a battery problem plus malfunction plus one '
                              'month returned 332 records [OS2unSk68KQ @ 00:01:52]. Smart refuses the '
                              'event-type filter, because reports filed as malfunctions can describe '
                              "injuries. For a reseller screening a model before buying, McLain's narrow "
                              "pull is faster, while Smart's wider net catches injury stories buried in "
                              'malfunction filings.',
                              'Recall execution draws the sharpest numeric splits. Jeff Kasof, the '
                              'endoscopy quality director with 13 earlier years running regulatory '
                              'affairs, says most firms run effectiveness checks against 100% of customers '
                              '[1kYC2rBfPPA @ 00:50:28]. Needelman sets a far lower bar for product '
                              'actually coming home: expect about 30% return, make three good-faith '
                              'attempts, and in Q&A they called 25% retrieval potentially acceptable '
                              '[nJblY5CRIVY @ 00:39:10]. Cadence splits too. David Pudwell of Mr. '
                              "Regulatory, walking through FDA's March 2020 guidance, runs status reports "
                              'monthly and repeats root cause and CAPA in every one [sNeRd4nIrG8 @ '
                              '00:23:00], while Kasof recommends every two to four weeks and notes FDA may '
                              'or may not specify it [1kYC2rBfPPA @ 00:46:51]. The delivery channel is '
                              'contested as well. Needelman wants certified mail or verifiable receipt and '
                              'rejects email or phone; Pudwell builds a phone script into the strategy and '
                              'only bars website posting as the sole means; Kasof generates customer '
                              'letters by mail merge. On publicity, Kasof treats a press release as '
                              'required for Class I and optional for Classes II and III, while Needelman '
                              'says Class I usually needs one and FDA will issue its own if yours is '
                              'unacceptable.'],
               'table': {'caption': 'Side-by-side playbooks where the recall and MAUDE practitioners split',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['What starts the 806 clock and how days count',
                                   'Snyder: all Class 1 and Class 2 recalls reported within 10 days of '
                                   'initiating the recall',
                                   'Needelman: 10 business days from the decision to act, not from the '
                                   'customer letter',
                                   'Quality Systems Explained ([8Pgfw2y5xe0 @ 00:01:52]); Medmarc '
                                   '([nJblY5CRIVY @ 00:04:43])'],
                                  ['Beating the 500-record MAUDE output cap on big pulls',
                                   'Smart and Alawad: split into consecutive date ranges, export each to '
                                   'Excel, merge the files',
                                   'Bernstein: substitute the brand into the openFDA query URL; one mesh '
                                   'brand returned 656 injuries in about 10 seconds',
                                   'Ofstead Insights ([a-scTl1C2PA @ 00:08:44]); Expert Institute '
                                   '([xbxXTRwdVRs @ 00:09:28])'],
                                  ['Using the event-type filter inside a MAUDE search',
                                   'McLain: filter on event type; battery issue plus malfunction plus one '
                                   'month returned 332 records',
                                   'Smart: skip the event-type filter entirely because malfunction reports '
                                   'may describe injuries',
                                   'Koven Technology Canada ([OS2unSk68KQ @ 00:01:52]); Ofstead Insights '
                                   '([a-scTl1C2PA @ 00:03:32])'],
                                  ['Effectiveness check depth and acceptable product return rate',
                                   'Kasof: most firms run effectiveness checks against 100% of their '
                                   'customers',
                                   'Needelman: expect about 30% return, make three good-faith attempts, '
                                   '25% retrieval can be acceptable',
                                   'GlobalCompliance Panel ([1kYC2rBfPPA @ 00:50:28]); Medmarc '
                                   '([nJblY5CRIVY @ 00:39:10])'],
                                  ['Status report cadence while a recall stays open',
                                   'Pudwell: monthly status reports that repeat root cause and CAPA every '
                                   'single time',
                                   'Kasof: every two to four weeks or so, whether or not FDA specifies it',
                                   'Mr. Regulatory ([sNeRd4nIrG8 @ 00:23:36]); GlobalCompliance Panel '
                                   '([1kYC2rBfPPA @ 00:46:51])'],
                                  ['How long to keep recall and reporting files on hand',
                                   'Kasof: keep recall or correction records three years beyond expected '
                                   'device life, even after discontinuing',
                                   'Alawad: keep all adverse event reporting records for 2 years',
                                   'GlobalCompliance Panel ([1kYC2rBfPPA @ 00:42:57]); Dr. Hashem Abu '
                                   'Serhan ([a_T4LqfP6zE @ 00:32:07])'],
                                  ['Labeling a fast-tap shutdown bug as usability or software',
                                   'Human Factors Engineering: both, because a UI interaction triggers a '
                                   'software design flaw fixed by update',
                                   'Phillips: software fixes for risk-to-health bugs likely count as '
                                   'corrections under 806',
                                   'Human Factors Engineering ([NXLRmBcAe9U @ 00:02:03]); Gardner Law '
                                   '([aYQu_0ujhyU @ 01:01:33])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive mistake the FDA veterans describe is timing, and the '
                              'second is disguise. Phillips says a late 806 report invites a 483 or a '
                              'warning letter scaled to how late it was, and a firm that hoped nobody '
                              'would notice is still exposed when an investigator finds it months later '
                              '[aYQu_0ujhyU @ 00:22:33]. They also flag the camouflage moves FDA sees '
                              'through: a recall dressed up as a technical bulletin, or a quiet recall '
                              '[aYQu_0ujhyU @ 00:34:48]. Needelman draws the silent-recall line with a '
                              'bulb hypothetical: lamps failing at 22 to 23 months are not a recall, lamps '
                              'failing at 8 to 9 months are, and a depleted backup battery is a recall '
                              'too; they cite a Medrad warning letter as the live example [nJblY5CRIVY @ '
                              '00:51:13]. Their fix for the clock is blunt: 80% of the information on time '
                              'beats 100% late, amend later, and promptly reporting in those 10 days is '
                              'critical [nJblY5CRIVY @ 00:52:35]. The trap on the other side is an 806 '
                              'report stuffed with placeholder entries, which they say has no value at '
                              'all. Phillips adds that vague recall letters raise red flags, and that '
                              'asking FDA what you should do is not a plan.',
                              'MAUDE punishes anyone who reads it at face value. The Health Watch USA '
                              'pharmacology researcher ran roughly 7.5 million events from 1997 to 2018 '
                              'through custom software and found manufacturers filed 96.6% of reports, '
                              'possibly driven by warranty claims and lawsuits, while physicians filed '
                              'directly only 0.49% and facilities 1.3% despite mandatory reporting '
                              '[yKomHc_DWtw @ 00:05:20]. The same study hit Johnson & Johnson logged under '
                              'multiple name variants, common duplicates, and a cobalt toxicity pull of '
                              '14,714 records where only 4% listed lab levels [yKomHc_DWtw @ 00:07:05]. '
                              'Smart warns that narratives can be empty and get filled in later, that '
                              'reports arrive late and underreported, and that FDA itself says MAUDE '
                              'cannot assess prevalence [a-scTl1C2PA @ 00:09:23]. Bernstein adds that '
                              'clinical sites and manufacturers each file narratives on the same problem, '
                              'very ill patients confound causation, and a record is not causation until '
                              'it is cross-checked against manufacturer claims, patient records and FDA '
                              "findings [xbxXTRwdVRs @ 00:30:15]. Alawad's zero-result fix is to widen "
                              'dates, drop brand and event type, and try every manufacturer name variant, '
                              'as with Rosh versus Rocher. Gene Parunak still calls a cursory keyword look '
                              'at similar devices well worth your time.',
                              'The economics bite hardest where records and contracts are thin. Pudwell '
                              'calls a recall without distribution records a rough spot, wants both '
                              'ship-to and bill-to consignees notified, and warns that indiscriminate '
                              'notices desensitize customers [sNeRd4nIrG8 @ 00:10:55]. Needelman closes '
                              'two escape hatches: if one unit of a 100-unit lot ships, the action is no '
                              'longer a stock recovery, and an expired warranty is no excuse, so set an '
                              'end-of-life date and resist that temptation [nJblY5CRIVY @ 00:14:26]. They '
                              'also describe recall fatigue, the same device recalled for 6 to 12 reasons '
                              'inside 6 to 9 months, and push sales staff into the field for visits. David '
                              'Graham, the 35-year litigator, says an opaque recall turns a bad device '
                              'case into a bad company case, so assume every document goes public and line '
                              'up a communication plan or PR firm, supply-chain indemnification and cost '
                              'analysis, contracts and recall insurance [aYQu_0ujhyU @ 00:45:18]. The '
                              'early-warning cost is real: Alawad found Ethicon stapler reports sitting in '
                              'MAUDE 2 years before a recall that covered 92,000 US devices [a_T4LqfP6zE @ '
                              "00:43:24]. Usually, as Alawad puts it, you're not the only one experiencing "
                              'something.'],
               'table': {'caption': 'Firsthand traps, exposure, and economics checks reported by the '
                                    'practitioners',
                         'headers': ['Trap',
                                     'What Was Reported',
                                     'Economics or Exposure Check',
                                     'Expert Source'],
                         'rows': [['Filing the 806 report late or misdating the clock',
                                   'Late reporting draws a 483 or warning letter scaled by lateness; '
                                   'discovery months later still exposes the firm',
                                   'Day 15 is the latest compliant report when the recall decision lands '
                                   'on Day 5',
                                   'Gardner Law ([aYQu_0ujhyU @ 00:22:33])'],
                                  ['Running a recall as a technical bulletin or silent fix',
                                   'Phillips rejects technical-bulletin recalls and quiet recalls; '
                                   'Needelman cites a Medrad warning letter',
                                   'Bulb failures at 8 to 9 months are a recall; a depleted backup battery '
                                   'is a recall',
                                   'Gardner Law ([aYQu_0ujhyU @ 00:34:48]); Medmarc ([nJblY5CRIVY @ '
                                   '00:51:13])'],
                                  ['MDR and recall decisions that contradict each other on file',
                                   'FDA is citing inconsistent MDR and recall decisions in 483s, according '
                                   'to Needelman',
                                   'File the 806 even when an MDR was already filed for the same event',
                                   'Medmarc ([nJblY5CRIVY @ 01:13:57])'],
                                  ['Reading MAUDE counts as prevalence or proof of causation',
                                   'Manufacturers file 96.6% of reports, physicians 0.49% directly, and '
                                   'duplicate records are common',
                                   'Cross-check every record against manufacturer claims, patient records '
                                   'and FDA findings before relying on it',
                                   'Health Watch USA ([yKomHc_DWtw @ 00:05:20]); Expert Institute '
                                   '([xbxXTRwdVRs @ 00:30:15])'],
                                  ['Treating a terminated recall or close-out letter as clearance',
                                   'A terminated recall does not erase the problem or create approval; a '
                                   'close-out is not blanket approval',
                                   'Match lot, serial, model and dates against the current agency page, '
                                   'not screenshots',
                                   'Treomark ([GoXd4_jxKBg @ 00:01:49])'],
                                  ['Untrained front-desk staff letting complaints slip past',
                                   'Missed feedback risks seizure or injunction and, anecdotally, ISO or '
                                   'CE revocation',
                                   'Train receptionists and anyone else who could possibly receive a '
                                   'complaint',
                                   'GlobalCompliance Panel ([1kYC2rBfPPA @ 00:05:02])'],
                                  ['Spending prevention money on the wrong recall cause',
                                   '1,059 recalls in 2024; the top 8 causes drive 80% and training people '
                                   'better is cheaper',
                                   "Don't spend $100k on a $10 problem; run a Pareto on bugs before buying "
                                   'tools',
                                   'Medical Device Academy ([GPC9Ci11MuI @ 00:21:52])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Operator Gate: Four Checks Before Calling a Recall Handled',
                           'body': 'Each gate below comes straight from a practitioner who watched firms '
                                   'get burned on it. Clear all four before treating a recall, a '
                                   'correction, or a MAUDE pull as settled.',
                           'items': ['Start the 806 clock at the recall decision, not the customer letter, '
                                     "and land the report by Day 15 on Phillips' calendar [Gardner Law — "
                                     'aYQu_0ujhyU @ 00:21:52].',
                                     'Never push a risk-to-health fix out as a technical bulletin or quiet '
                                     'software update; Phillips says software fixes for risk-to-health '
                                     'bugs likely count as corrections [Gardner Law — aYQu_0ujhyU @ '
                                     '01:01:33].',
                                     'Do not expect closure until root cause is documented; Needelman says '
                                     'FDA will not close a recall without one [Medmarc — nJblY5CRIVY @ '
                                     '00:33:13].',
                                     'Before trusting any MAUDE count, work around the 500-record cap and '
                                     'treat each record as a lead, not causation [Expert Institute — '
                                     'xbxXTRwdVRs @ 00:22:47].']}}],
 'pull_quote': 'Please do not ever expect FDA to become a part of your system to help you detect and '
               'assess. — Tim Phillips, attributed to Gardner Law (aYQu_0ujhyU @ 00:34:10).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Run the health hazard evaluation on Days 1 to 3 and treat the Day 5 recall decision '
                      'as the start of the 806 clock [Gardner Law — aYQu_0ujhyU @ 00:20:43].',
                      'Provide the reason, test results, complaints and MDRs to FDA up front to avoid '
                      'back-and-forth [Mr. Regulatory — sNeRd4nIrG8 @ 00:09:02].',
                      'Search MAUDE through advanced search, start with product class, widen the default '
                      'one-month date range, and export to Excel [Ofstead Insights — a-scTl1C2PA @ '
                      '00:02:23].',
                      'Pull the TPLC report by product code as the recall history; if one manufacturer has '
                      'all the recalls, suspect that manufacturer [Expert Institute — xbxXTRwdVRs @ '
                      '00:21:28].',
                      'Send recall notices by certified mail or verifiable receipt, not email or phone, '
                      'and make three good-faith attempts [Medmarc — nJblY5CRIVY @ 00:27:53].',
                      'Document every non-reporting decision and have the justification reviewed by an '
                      'external consultant [GlobalCompliance Panel — 1kYC2rBfPPA @ 00:44:59].'],
 'statutory_citations': [{'title': 'Gardner Law — Medical Device Recalls Unpacked: FDA Compliance and '
                                   'Litigation Insights [00:20:43]',
                          'url': 'https://www.youtube.com/watch?v=aYQu_0ujhyU&t=1243s',
                          'relevance': 'Primary practitioner testimony on the HHE-to-decision recall '
                                       'timeline and when the 806 clock starts.'},
                         {'title': 'Medmarc — Medical Device Recalls and Part 806: The Importance of '
                                   'Getting It Right [00:04:43]',
                          'url': 'https://www.youtube.com/watch?v=nJblY5CRIVY&t=283s',
                          'relevance': 'Primary practitioner testimony on the 10-business-day reporting '
                                       'window measured from the decision to act.'},
                         {'title': 'GlobalCompliance Panel — Recalls, Removals, and Market Corrections in '
                                   'Compliance with FDA and ISO Requirements [00:41:45]',
                          'url': 'https://www.youtube.com/watch?v=1kYC2rBfPPA&t=2505s',
                          'relevance': 'Primary practitioner testimony on the 10-working-day report '
                                       'deadline and report content.'},
                         {'title': 'Ofstead Insights — Searching the FDA MAUDE database [00:08:44]',
                          'url': 'https://www.youtube.com/watch?v=a-scTl1C2PA&t=524s',
                          'relevance': 'Primary practitioner testimony on the 500-report MAUDE cap and the '
                                       'date-split workaround.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '8Pgfw2y5xe0',
                       'title': 'Corrections and Removals 21 CFR 806 & ISO 13485 § 8.3.3 (Executive Series '
                                '#55)',
                       'channel': 'Quality Systems Explained',
                       'author': 'Quality Systems Explained',
                       'text': 'All class 1 and class 2 recalls must be reported to the FDA within 10 days '
                               'of initiating the recall.',
                       'tip': 'All class 1 and class 2 recalls must be reported to the FDA within 10 days '
                              'of initiating the recall.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=8Pgfw2y5xe0&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=8Pgfw2y5xe0&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OS2unSk68KQ',
                       'title': "FDA's MAUDE database: A medical device expert's insight",
                       'channel': 'Koven Technology Canada',
                       'author': 'Koven Technology Canada',
                       'text': 'A search on a battery issue, the malfunction event type, and the first '
                               'month of the year returned 332 records.',
                       'tip': 'A search on a battery issue, the malfunction event type, and the first '
                              'month of the year returned 332 records.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=OS2unSk68KQ&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=OS2unSk68KQ&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a-scTl1C2PA',
                       'title': 'Searching the FDA MAUDE database',
                       'channel': 'Ofstead Insights',
                       'author': 'Ofstead Insights',
                       'text': 'The MAUDE database only allows 500 reports to be returned for a single '
                               'search.',
                       'tip': 'The MAUDE database only allows 500 reports to be returned for a single '
                              'search.',
                       'timestamp': 524,
                       'timestamp_seconds': 524,
                       'timestamp_label': '[00:08:44]',
                       'url': 'https://www.youtube.com/watch?v=a-scTl1C2PA&t=524s',
                       'markdown': '[00:08:44](https://www.youtube.com/watch?v=a-scTl1C2PA&t=524s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aYQu_0ujhyU',
                       'title': 'Medical Device Recalls Unpacked: FDA Compliance and Litigation Insights',
                       'channel': 'Gardner Law',
                       'author': 'Gardner Law',
                       'text': 'Please do not ever expect FDA to become a part of your system to help you '
                               'detect and assess.',
                       'tip': 'Please do not ever expect FDA to become a part of your system to help you '
                              'detect and assess.',
                       'timestamp': 2050,
                       'timestamp_seconds': 2050,
                       'timestamp_label': '[00:34:10]',
                       'url': 'https://www.youtube.com/watch?v=aYQu_0ujhyU&t=2050s',
                       'markdown': '[00:34:10](https://www.youtube.com/watch?v=aYQu_0ujhyU&t=2050s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0dpHnJj93Ns',
                       'title': "Who's Maude Anyway? Two FDA Databases Get Updates",
                       'channel': 'in2being',
                       'author': 'in2being',
                       'text': 'MAUDE is a publicly accessible database, openFDA, publicly accessible.',
                       'tip': 'MAUDE is a publicly accessible database, openFDA, publicly accessible.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=0dpHnJj93Ns&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=0dpHnJj93Ns&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sNeRd4nIrG8',
                       'title': 'EPISODE 2: Product Recalls, Including Removals and Corrections',
                       'channel': 'Mr. Regulatory',
                       'author': 'Mr. Regulatory',
                       'text': 'Provide the reason, test results, complaints and MDRs up front to avoid '
                               'back-and-forth with FDA.',
                       'tip': 'Provide the reason, test results, complaints and MDRs up front to avoid '
                              'back-and-forth with FDA.',
                       'timestamp': 542,
                       'timestamp_seconds': 542,
                       'timestamp_label': '[00:09:02]',
                       'url': 'https://www.youtube.com/watch?v=sNeRd4nIrG8&t=542s',
                       'markdown': '[00:09:02](https://www.youtube.com/watch?v=sNeRd4nIrG8&t=542s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GoXd4_jxKBg',
                       'title': 'FDA Recall vs Warning Letter vs Safety Communication: Know the Difference',
                       'channel': 'Treomark',
                       'author': 'Treomark',
                       'text': 'The letter is not itself a product recall.',
                       'tip': 'The letter is not itself a product recall.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=GoXd4_jxKBg&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=GoXd4_jxKBg&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4_qtgUz46GU',
                       'title': 'FDA Recall Update: Food and Medicine Nov 9. 2026',
                       'channel': 'FDA RECALLS',
                       'author': 'FDA RECALLS',
                       'text': 'This recall is being issued because the product may contain thallium, a '
                               'toxic heavy metal.',
                       'tip': 'This recall is being issued because the product may contain thallium, a '
                              'toxic heavy metal.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=4_qtgUz46GU&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=4_qtgUz46GU&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-6DRTqlDCP0',
                       'title': 'Medical Device Complaint Handling Process | MAUDE Database & FDA 3500A '
                                'Walkthrough',
                       'channel': 'REGSTALK',
                       'author': 'REGSTALK',
                       'text': 'So wherever you identify any issues you have to report it.',
                       'tip': 'So wherever you identify any issues you have to report it.',
                       'timestamp': 1634,
                       'timestamp_seconds': 1634,
                       'timestamp_label': '[00:27:14]',
                       'url': 'https://www.youtube.com/watch?v=-6DRTqlDCP0&t=1634s',
                       'markdown': '[00:27:14](https://www.youtube.com/watch?v=-6DRTqlDCP0&t=1634s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yKomHc_DWtw',
                       'title': 'The FDA MAUDE Database.  Who is reporting and how good are the reports.',
                       'channel': 'Health Watch USA',
                       'author': 'Health Watch USA',
                       'text': 'Health care professionals are not required to report harm or fatalities to '
                               'the FDA.',
                       'tip': 'Health care professionals are not required to report harm or fatalities to '
                              'the FDA.',
                       'timestamp': 577,
                       'timestamp_seconds': 577,
                       'timestamp_label': '[00:09:37]',
                       'url': 'https://www.youtube.com/watch?v=yKomHc_DWtw&t=577s',
                       'markdown': '[00:09:37](https://www.youtube.com/watch?v=yKomHc_DWtw&t=577s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1kYC2rBfPPA',
                       'title': 'Recalls, Removals, and Market Corrections in Compliance with FDA and ISO '
                                'Requirements',
                       'channel': 'GlobalCompliance Panel',
                       'author': 'GlobalCompliance Panel',
                       'text': 'The deadline for issuing the report is 10 working days.',
                       'tip': 'The deadline for issuing the report is 10 working days.',
                       'timestamp': 2505,
                       'timestamp_seconds': 2505,
                       'timestamp_label': '[00:41:45]',
                       'url': 'https://www.youtube.com/watch?v=1kYC2rBfPPA&t=2505s',
                       'markdown': '[00:41:45](https://www.youtube.com/watch?v=1kYC2rBfPPA&t=2505s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nJblY5CRIVY',
                       'title': 'Medical Device Recalls and Part 806: The Importance of Getting It Right',
                       'channel': 'Medmarc',
                       'author': 'Medmarc',
                       'text': 'Promptly reporting in those 10 days is critical.',
                       'tip': 'Promptly reporting in those 10 days is critical.',
                       'timestamp': 3155,
                       'timestamp_seconds': 3155,
                       'timestamp_label': '[00:52:35]',
                       'url': 'https://www.youtube.com/watch?v=nJblY5CRIVY&t=3155s',
                       'markdown': '[00:52:35](https://www.youtube.com/watch?v=nJblY5CRIVY&t=3155s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nJblY5CRIVY',
                       'title': 'Medical Device Recalls and Part 806: The Importance of Getting It Right',
                       'channel': 'Medmarc',
                       'author': 'Medmarc',
                       'text': "It's important that you document, document, document all your decisions "
                               "and your basis for not reporting or for determining it's a class three "
                               'recall.',
                       'tip': "It's important that you document, document, document all your decisions and "
                              "your basis for not reporting or for determining it's a class three recall.",
                       'timestamp': 3340,
                       'timestamp_seconds': 3340,
                       'timestamp_label': '[00:55:40]',
                       'url': 'https://www.youtube.com/watch?v=nJblY5CRIVY&t=3340s',
                       'markdown': '[00:55:40](https://www.youtube.com/watch?v=nJblY5CRIVY&t=3340s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GPC9Ci11MuI',
                       'title': '8 Surprising Ways to Prevent Device Recalls!',
                       'channel': 'Medical Device Academy',
                       'author': 'Medical Device Academy',
                       'text': 'Training people better is cheaper.',
                       'tip': 'Training people better is cheaper.',
                       'timestamp': 638,
                       'timestamp_seconds': 638,
                       'timestamp_label': '[00:10:38]',
                       'url': 'https://www.youtube.com/watch?v=GPC9Ci11MuI&t=638s',
                       'markdown': '[00:10:38](https://www.youtube.com/watch?v=GPC9Ci11MuI&t=638s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a_T4LqfP6zE',
                       'title': 'A Step-by-Step Guide to the Manufacturer and User Facility Device '
                                'Experience (MAUDE) Database',
                       'channel': 'Dr. Hashem Abu Serhan',
                       'author': 'Dr. Hashem Abu Serhan',
                       'text': "Usually you're not the only one experiencing something.",
                       'tip': "Usually you're not the only one experiencing something.",
                       'timestamp': 1989,
                       'timestamp_seconds': 1989,
                       'timestamp_label': '[00:33:09]',
                       'url': 'https://www.youtube.com/watch?v=a_T4LqfP6zE&t=1989s',
                       'markdown': '[00:33:09](https://www.youtube.com/watch?v=a_T4LqfP6zE&t=1989s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NXLRmBcAe9U',
                       'title': 'Critical FDA Recall: A Usability Issue… or a Software Bug? #fdarecall '
                                '#usability #software',
                       'channel': 'Human Factors Engineering',
                       'author': 'Human Factors Engineering',
                       'text': 'The underlying issue, on the other hand, is a software design flaw that '
                               "can't properly accommodate real world user behavior.",
                       'tip': 'The underlying issue, on the other hand, is a software design flaw that '
                              "can't properly accommodate real world user behavior.",
                       'timestamp': 123,
                       'timestamp_seconds': 123,
                       'timestamp_label': '[00:02:03]',
                       'url': 'https://www.youtube.com/watch?v=NXLRmBcAe9U&t=123s',
                       'markdown': '[00:02:03](https://www.youtube.com/watch?v=NXLRmBcAe9U&t=123s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xbxXTRwdVRs',
                       'title': 'Best Practices for Using Open FDA Data in Medical Device Cases',
                       'channel': 'Expert Institute',
                       'author': 'Expert Institute',
                       'text': 'It will only return 500 records at a time.',
                       'tip': 'It will only return 500 records at a time.',
                       'timestamp': 1367,
                       'timestamp_seconds': 1367,
                       'timestamp_label': '[00:22:47]',
                       'url': 'https://www.youtube.com/watch?v=xbxXTRwdVRs&t=1367s',
                       'markdown': '[00:22:47](https://www.youtube.com/watch?v=xbxXTRwdVRs&t=1367s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
