from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'hts-classification-getting-the-code-right',
 'question_prompt': 'How do I classify goods correctly under the HTSUS so I pay the right duty and avoid '
                    'costly errors?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'HTS Classification: Getting the Code Right Before It Costs You',
 'subtitle': 'HS/HTSUS structure, GRI-based step-by-step classification, calculating duties from HTS '
             "codes, recent CBP rulings, catching classification mistakes, why supplier codes can't be "
             'trusted, and CBP Ruling HQ 350722 on AI classification tools',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one rule: customs classifies by material, function, '
                      'construction, and use, never by product name, and the importer of record owns the '
                      'code and the penalty exposure no matter who supplied it. The mechanics are '
                      'concrete: duty is set at the 8th digit, the last two are statistical, GRIs are '
                      'applied in order with legal notes read first, and at least three candidate headings '
                      "are logged with reasons for elimination. Supplyia's worked umbrella math lands "
                      '$697.14 duty on 5,000 units at $2, while Shipping Solutions shows a 0% base line '
                      'carrying eight possible Chapter 99 overlays. The friction points: Supplyia treats '
                      'Google and supplier codes as starting leads, while Star USA calls CROSS-first '
                      "research a fool's errand and vendor codes no excuse, and KYG Trade flags CBP "
                      'treating 10-digit AI output as licensed customs business.',
 'key_metrics': [{'label': 'Duty-Setting Digit Position',
                  'metric': 'Duty-Setting Digit Position',
                  'value': '8th digit of a 10-digit HTSUS code',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Form 7501 carries all 10 digits, but the duty rate is set at the 8th digit; '
                             'the last two are statistical.',
                  'source': 'Star USA, Inc. ([-v_-OQnVlxE @ 01:01:37])'},
                 {'label': 'Worked Umbrella Duty Total',
                  'metric': 'Worked Umbrella Duty Total',
                  'value': '$697.14 on 5,000 umbrellas at $2 each',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Total duty calculated in a live lookup walkthrough, including MPF and HMF.',
                  'source': 'Supplyia Sourcing ([ff_P7M6LKEo @ 00:14:41])'},
                 {'label': 'Merchandise Processing Fee Range',
                  'metric': 'Merchandise Processing Fee Range',
                  'value': '.3464%, minimum about $26, maximum $508',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'MPF stated as applying to both air and ocean shipments on top of base duty.',
                  'source': 'Supplyia Sourcing ([ff_P7M6LKEo @ 00:04:24])'},
                 {'label': 'One-Detail Duty Swing',
                  'metric': 'One-Detail Duty Swing',
                  'value': 'About 2.9% vs 7.2%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A single-wall stainless steel bottle versus a vacuum-insulated flask, '
                             'showing how one construction detail moves the rate.',
                  'source': 'USA Customs Clearance ([MfmhZLeMz2w @ 00:02:33])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every practitioner who touched the question lands in the same place: '
                              'customs does not classify a product by what you call it. USA Customs '
                              'Clearance says customs looks at material, function, manufacture, complete '
                              'or unfinished state, packaging, and intended use rather than the product '
                              'name, and that one small detail can flip the code [MfmhZLeMz2w @ 00:01:04]. '
                              'The Procurement Lens is blunter, saying customs ignores marketing '
                              'descriptions and brand names, so the first job is locking down an accurate '
                              'product description because a material difference changes both the code and '
                              'the duty [4IEk0Lxmf1c @ 00:04:30]. Straightforward ITC lists the facts that '
                              'actually move the needle as materials, construction, function, design, '
                              'components, principal use, and presentation, and warns that small factual '
                              'differences can change classification [CcVyqKoA9dY @ 00:00:52]. Joe Harper '
                              'of Star USA builds the whole workflow on that foundation: know the product '
                              'through composition, function, use, drawings, bill of materials, and '
                              'in-house experts before listing a single candidate heading, then read the '
                              'notes and only then apply the GRIs [HbhpILTp9v0 @ 00:41:08]. The operator '
                              'takeaway is that the spec sheet comes before the search bar, and anyone '
                              'classifying from a product title is guessing.',
                              'The second point of agreement is that the code is not a label, it is the '
                              'switchboard for every cost and control on the entry. USA Customs Clearance '
                              'ties it to agency requirements, special programs, quotas, and AD/CVD, and '
                              'warns that underpaying creates larger problems later than overpaying does '
                              '[MfmhZLeMz2w @ 00:02:50]. Steve Fodor, a broker for more than 30 years, '
                              'puts the liability squarely on the importer of record, with civil and '
                              'criminal exposure, and calls misclassification the most frequent import '
                              'error [Exy48YwwPtk @ 00:05:14]. Michael D. Eastston of Star USA states it '
                              'in one line, importers are responsible for classifying their goods, and '
                              'frames the duty rate as a result of the classification rather than the '
                              'starting point [-v_-OQnVlxE @ 00:40:34]. Joe Harper closes the escape hatch '
                              'everyone reaches for: customs does not care if the vendor gave you the '
                              'wrong HTS, it cares that you use the right one [HbhpILTp9v0 @ 00:56:12]. '
                              'Put together, the consensus is that there is no one to hide behind. The '
                              'broker, the supplier, and the software vendor all hand you a number, but '
                              'the importer owns the number, the duty math attached to it, and the penalty '
                              'exposure when an audit lands.',
                              'Third, the practitioners agree on what does not work as a method. '
                              'Straightforward ITC opens with the supplier-provided code and answers '
                              'whether you can use it with "not necessarily," then lists the pitfalls: '
                              "relying on the supplier's code, reusing stale codes, picking by keyword "
                              'search, and assuming lookalike products classify the same [CcVyqKoA9dY @ '
                              '00:00:00]. The Procurement Lens flags the same traps, adding generic codes '
                              'chosen because they are easy to find and ignoring tariff updates '
                              '[4IEk0Lxmf1c @ 00:03:44]. What does work is the legal sequence: Eastston '
                              'says apply the GRIs in order and read section and chapter notes first '
                              '[-v_-OQnVlxE @ 00:26:14]. Cole International adds the endgame: understand '
                              'the HS notes, then have a licensed broker or customs attorney request a '
                              'binding ruling before importing, which the firm calls "the definitive '
                              'assessment" [x-SDVKIzJdI @ 00:02:26]. Nobody in this group treats a '
                              'search-engine hit or a supplier invoice as an answer; at best they are '
                              "leads to be tested against the schedule's own legal text. The baseline "
                              'prerequisites are therefore a full product fact file, the GRIs and legal '
                              'notes applied in order, a current tariff version, and a ruling in hand '
                              'whenever the heading is genuinely in doubt.'],
               'table': {'caption': 'Where the practitioners agree: the baseline rules of HTS '
                                    'classification',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Classify on product facts, never on product names',
                                   'Customs weighs material, function, manufacture, finished state, '
                                   'packaging, and intended use',
                                   'Build the full spec sheet before opening any tariff search tool',
                                   'USA Customs Clearance ([MfmhZLeMz2w @ 00:01:04])'],
                                  ['Marketing copy and brand names carry zero classification weight',
                                   'Customs ignores marketing descriptions; a material difference changes '
                                   'both code and duty',
                                   'Lock down an accurate technical product description as step one',
                                   'The Procurement Lens ([4IEk0Lxmf1c @ 00:04:30])'],
                                  ['The importer of record carries the legal liability for the code',
                                   'Civil and criminal exposure; misclassification is the most frequent '
                                   'import error',
                                   'Ownership of the code cannot be outsourced to a broker or supplier',
                                   'Steve Fodor ([Exy48YwwPtk @ 00:05:14])'],
                                  ['Vendor-supplied codes are never a valid defense when customs reviews',
                                   'Customs does not care if the vendor gave you the wrong HTS',
                                   'Verify every supplier code independently before it reaches an entry',
                                   'Star USA, Inc. ([HbhpILTp9v0 @ 00:56:12])'],
                                  ['Keyword search and stale codes are recognized classification traps',
                                   'Supplier codes, reused stale codes, keyword picks, and lookalike '
                                   'assumptions all fail',
                                   'Re-run the classification whenever product facts or tariff versions '
                                   'change',
                                   'Straightforward ITC ([CcVyqKoA9dY @ 00:00:52])'],
                                  ['GRIs and legal notes govern the analysis in strict order',
                                   'Apply the GRIs in order and read section and chapter notes first',
                                   'Treat legal notes as binding text that overrides loose word matching',
                                   'Star USA, Inc. ([-v_-OQnVlxE @ 00:26:14])'],
                                  ['Binding rulings settle genuinely uncertain classifications before '
                                   'goods ship',
                                   'A professionally requested binding ruling is the definitive assessment '
                                   'before importing',
                                   'Request rulings for new products where materials or function are '
                                   'borderline',
                                   'Cole International ([x-SDVKIzJdI @ 00:02:26])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Start with the anatomy, because that is where duty actually lives. USA '
                              'Customs Clearance describes the code as an address: the first six digits '
                              'are international, the US adds more, and most products use 10 digits '
                              "[MfmhZLeMz2w @ 00:02:03]. Steve Fodor walks a men's polyester woven shirt "
                              'through it at 6205.30.2030, reading digits five through eight as the '
                              'subheading and treating the last two as statistical with no duty impact '
                              '[Exy48YwwPtk @ 00:28:23]. Joe Harper of Star USA puts the same point in '
                              'operator terms: the 8th digit is the tariff item that carries the duty '
                              'rate, while the 10th digit is statistical [HbhpILTp9v0 @ 00:14:13]. Michael '
                              'D. Eastston confirms how that plays out on paper, with Form 7501 carrying '
                              'all 10 digits but duty set at the 8th [-v_-OQnVlxE @ 01:01:37]. The '
                              'practical consequence is a two-stage check. The first eight digits decide '
                              'what you pay, so that is where the hardest research belongs, and a wrong '
                              'call there flows straight into the duty bill. The last two digits still '
                              'have to be right because the entry carries the full code, but an error '
                              'there will not change the rate you are assessed on the line.',
                              'For the lookup itself, Supplyia Sourcing runs an umbrella through a '
                              'four-source funnel, using Google, the supplier, the freight forwarder, or '
                              'the ITC database to find chapter and heading, then matching descriptions on '
                              'material, construction, performance, and function; a travel umbrella at '
                              '66032030 comes back free while a garden umbrella sits at 6.5% [ff_P7M6LKEo '
                              '@ 00:10:43]. The same walkthrough stacks the fees: MPF at .3464% on air and '
                              'ocean with a minimum of about $26 and a maximum of $508, plus HMF at 0.125% '
                              'on ocean only, and the worked result of 5,000 umbrellas at $2 lands at a '
                              'total duty of $697.14 including MPF and HMF [ff_P7M6LKEo @ 00:14:41]. '
                              'Shipping Solutions shows why the base rate misleads: a semiconductor line '
                              'shows a default 0%, but eight Chapter 99 tariffs may apply depending on '
                              'source, material, and destination [_I3v11oKRLA @ 00:02:09]. On the '
                              'China-to-US pull, that tool flagged Section 122 at 10% additional for all '
                              'countries and Section 301 at 50% on China, with 9903.91.02 declared on top '
                              'of the base code [_I3v11oKRLA @ 00:03:45]. The operator rule: never quote a '
                              'landed cost off the default rate alone; stack the Chapter 99 overlays and '
                              'the port fees first.',
                              'Research discipline is where the senior brokers spend their airtime. Jo '
                              "Harper's method is to consider at least three headings and document the "
                              'reasoning, keeping a log of the headings considered, why each was '
                              'eliminated, and the details that drove the final pick [ygZWIWKWe4w @ '
                              '00:48:03]. Eastston adds a version-control step: record the HTSUS revision '
                              'number used for each analysis, so the file shows which schedule the call '
                              "was made against [-v_-OQnVlxE @ 00:39:58]. Harper's earlier webinar adds "
                              'program controls: defined roles, sales-team escalation, periodic audits, '
                              'vendor HTS checks, a central database, and involvement in engineering, '
                              'along with a flat warning not to take the first CROSS hit [BwGDeEGn1Wg @ '
                              '00:57:31]. Steve Fodor backs the paper trail from the liability side, '
                              'telling importers to document everything, audit their classifications, and '
                              "get rulings [Exy48YwwPtk @ 00:37:10]. Fodor's framing is that the importer "
                              'of record cannot simply hand the job to a broker; reasonable care means the '
                              "importer's own file has to show the work. The working system is a central "
                              'product database, a written heading-elimination log, the tariff revision '
                              'stamped on every file, periodic audits, and a ruling wherever the call is '
                              'close. When customs asks why, that log is the answer.'],
               'table': {'caption': 'Street numbers and tools operators run on every classification',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Rule Stated',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Merchandise Processing Fee (MPF) on formal entries',
                                   '.3464% on air and ocean, minimum about $26, maximum $508',
                                   'Add to every landed-cost model alongside the base duty rate',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:04:24])'],
                                  ['Harbor Maintenance Fee (HMF) on ocean freight',
                                   '0.125% applied to ocean shipments only, never to air',
                                   'Layer onto ocean entries and leave off air shipment calculations',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:04:45])'],
                                  ['De minimis threshold on commercial invoice value',
                                   'A $500 sample paid no duty; invoices over $800 pay duty',
                                   'Check invoice value before assuming a shipment clears duty free',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:03:41])'],
                                  ['Chapter 99 overlay check on a 0% base line',
                                   'Default 0% semiconductor line showed eight possible Chapter 99 tariffs',
                                   'Run the import-controls lookup by origin before quoting any rate',
                                   'Shipping Solutions ([_I3v11oKRLA @ 00:02:09])'],
                                  ['Section 301 and Section 122 stacking from China',
                                   'Section 301 at 50% on China via 9903.91.02; Section 122 adds 10%',
                                   'Declare the Chapter 99 number in addition to the base code',
                                   'Shipping Solutions ([_I3v11oKRLA @ 00:03:45])'],
                                  ['Duty-bearing digit versus statistical digits on the entry',
                                   'Duty is set at the 8th digit; Form 7501 carries all 10',
                                   'Concentrate the hardest research on the first eight digits',
                                   'Star USA, Inc. ([-v_-OQnVlxE @ 01:01:37])'],
                                  ['One construction detail swinging the duty rate',
                                   'Single-wall stainless bottle about 2.9% versus vacuum-insulated flask '
                                   '7.2%',
                                   'Confirm construction details on the spec sheet before locking the code',
                                   'USA Customs Clearance ([MfmhZLeMz2w @ 00:02:33])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Reading the Schedule Like a Broker',
                           'body': 'The schedule punishes sloppy reading. These are the page-level habits '
                                   'the veteran brokers use to avoid landing in the wrong line.',
                           'items': ['Hold a ruler to the page: indentation shows the hierarchy, and you '
                                     'never classify straight from the alphabetical index [Steve Fodor — '
                                     'Exy48YwwPtk @ 00:13:24]',
                                     'Treat a semicolon in the tariff text as a full stop, and read the '
                                     'legal notes as mandatory text that must be followed [Star USA, Inc. '
                                     '— HbhpILTp9v0 @ 00:24:50]',
                                     'USITC search uses British wording such as "seat" and "anorak", so a '
                                     'keyword like "chair" can miss the right line entirely [Star USA, '
                                     'Inc. — HbhpILTp9v0 @ 00:11:19]',
                                     'A "slash and underscore" after the rate on the lookup means added '
                                     'tariffs apply, so run the tariff check before trusting the base '
                                     'number [Supplyia Sourcing — ff_P7M6LKEo @ 00:11:47]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the Product Fact File',
                              'action': 'Assemble composition, function, use, drawings, bill of materials, '
                                        'and expert input before any search.',
                              'detail': "Harper's workflow opens with knowing the product through "
                                        'composition, function, use, drawings, BOM, and experts, then '
                                        'listing candidate headings [Star USA, Inc. — HbhpILTp9v0 @ '
                                        '00:41:08]'},
                             {'step': 2,
                              'title': 'List and Eliminate Candidate Headings',
                              'action': 'Consider at least three headings, read section and chapter notes, '
                                        'and apply the GRIs in order.',
                              'detail': 'Consider at least three headings and document the reasoning for '
                                        'each elimination [Star USA, Inc. — ygZWIWKWe4w @ 00:46:16]'},
                             {'step': 3,
                              'title': 'Stack the Real Duty Bill',
                              'action': 'Pull the base rate, run the Chapter 99 overlay check by origin, '
                                        'then add MPF and HMF.',
                              'detail': 'A 0% default line can carry eight Chapter 99 tariffs depending on '
                                        'source, material, and destination [Shipping Solutions — '
                                        '_I3v11oKRLA @ 00:02:09]; MPF and HMF fold into the total, as in '
                                        'the $697.14 umbrella result [Supplyia Sourcing — ff_P7M6LKEo @ '
                                        '00:14:41]'},
                             {'step': 4,
                              'title': 'Lock and Document the Call',
                              'action': 'Record the HTSUS revision used, file the heading log, and request '
                                        'a ruling where the call is close.',
                              'detail': 'Record the HTSUS revision number used for each analysis so the '
                                        'file shows which schedule the decision was made against [Star '
                                        'USA, Inc. — -v_-OQnVlxE @ 00:39:58]'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is where the hunt for a code begins. Supplyia Sourcing '
                              'runs a fast street playbook: pull the chapter and heading from Google, the '
                              'supplier, the freight forwarder, or the ITC database, then validate inside '
                              'the ITC search, exactly how they landed an umbrella in 6601 and confirmed '
                              'it [ff_P7M6LKEo @ 00:08:49] [ff_P7M6LKEo @ 00:09:37]. They pitch the whole '
                              'lookup at about 10 minutes. Michael D. Eastston of Star USA rejects that '
                              "foundation outright: a competitor's code is no excuse, and starting a "
                              "novice inside CROSS is a 'fool's errand' because HQ rulings outrank NY "
                              'rulings [-v_-OQnVlxE @ 00:08:45] [-v_-OQnVlxE @ 00:35:37]. Straightforward '
                              'ITC sides with Eastston, warning that a code handed over by the supplier is '
                              "'not necessarily' usable and listing reliance on the supplier's code, "
                              'keyword-search picking, and assuming lookalike products classify the same '
                              'as the core pitfalls [CcVyqKoA9dY @ 00:00:00] [CcVyqKoA9dY @ 00:00:52]. Joe '
                              'Harper of Star USA supplies the alternative playbook: know the product '
                              'through composition, function, use, drawings, BOM, and outside experts, '
                              'list candidate headings, read the notes, then apply the GRIs [HbhpILTp9v0 @ '
                              "00:41:08]. Harper's bottom line on vendor codes is blunt: 'Customs doesn't "
                              'care if the vendor gave you the wrong HTS, they care that you use the right '
                              "HTS' [HbhpILTp9v0 @ 00:56:12].",
                              'The second fault line is who actually owns the classification. Cole '
                              'International tells importers to put a licensed customs broker or customs '
                              'attorney on the product and have that professional request a binding '
                              "ruling, 'the definitive assessment,' before the goods move [x-SDVKIzJdI @ "
                              '00:01:47] [x-SDVKIzJdI @ 00:02:26]. Steve Fodor, a broker for over 30 '
                              "years, pushes back from inside the trade: don't just hand everything to a "
                              "broker, read CBP's 18-page Reasonable Care checklist, and remember that the "
                              'importer of record carries civil and criminal exposure while broker '
                              'liability is limited to the entry fee, often $100 or less [Exy48YwwPtk @ '
                              '00:08:30] [Exy48YwwPtk @ 00:35:38]. Eastston goes further, reporting that '
                              'brokers are exiting classification work, that importers are responsible for '
                              'classifying their goods, and that reasonable care is measured by procedure, '
                              'not result [-v_-OQnVlxE @ 00:40:53] [-v_-OQnVlxE @ 00:37:54]. The KYG Trade '
                              'panel adds a counterintuitive staffing call: importers do not need a '
                              'licensed broker on staff, and putting one there may actually raise their '
                              'reasonable-care bar [myOI9hprs0c @ 00:19:22]. The live choice is between '
                              "Cole's model, where a Canada/US broker handles everything from initial "
                              'assessment through the ruling, and the Fodor-Eastston model, where the '
                              'importer builds and documents its own procedure, audits its '
                              'classifications, and uses the broker as one input rather than the owner of '
                              'the answer.',
                              'Automated classification is the newest fight. The KYG Trade panel reads CBP '
                              'ruling HQ 350722 as drawing a digit line: 6-digit output is acceptable, but '
                              'CBP presumes 10-digit output is customs business that requires a license, '
                              'and filing CF 5106 counts too [myOI9hprs0c @ 00:12:00]. Richard Wartman of '
                              "Grunfeld Desiderio dissents on tone, saying CBP 'went a little overboard' "
                              "on 'bad facts' involving a non-US, unlicensed platform, while the same "
                              "panel flags that ChatGPT and Gemini are 'at least today violating this "
                              "ruling' [myOI9hprs0c @ 00:12:47] [myOI9hprs0c @ 00:18:19]. ImageSearch for "
                              'HS classification takes the hard line, calling prediction of 10-digit codes '
                              "'strictly forbidden without a broker license,' arguing that hedging "
                              'language attached to tool output fails under HQ H290535 because the '
                              "10-digit code determines duty, and pitching the ruling as a 'global "
                              "blueprint' [Z20K9hWki3Q @ 00:01:27] [Z20K9hWki3Q @ 00:02:56]. Their lawful "
                              "alternative is the 'mere conduit' exemption: a neutral pipeline connecting "
                              'importers to brokers, with POAs executed directly and confidentiality kept '
                              'under 19 CFR 111.24. Eastston stays pragmatic: customs requires a human '
                              'classifier, and AI is a tool rather than a substitute [-v_-OQnVlxE @ '
                              "00:36:14]. Harper's verdict lands in the same place: 'It's a tool it's not "
                              "the answer' [HbhpILTp9v0 @ 00:58:19]."],
               'table': {'caption': 'Side-by-Side Playbooks Where Practitioners Split',
                         'headers': ['Fault Line',
                                     'Playbook A (As Argued)',
                                     'Playbook B (As Argued)',
                                     'Expert Source'],
                         'rows': [['Where to source the first candidate code',
                                   'Pull a starting code from Google, supplier, forwarder, or ITC '
                                   'database, then validate it',
                                   'Supplier and competitor codes are no excuse; start from tariff '
                                   'language, notes, and GRIs',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:08:49]); Straightforward ITC '
                                   '([CcVyqKoA9dY @ 00:00:35])'],
                                  ['Broker as owner of the classification answer',
                                   'Hand it to a licensed broker or customs attorney who also requests the '
                                   'ruling',
                                   'Never hand everything over; broker liability stops at the entry fee, '
                                   'often $100 or less',
                                   'Cole International ([x-SDVKIzJdI @ 00:01:47]); Steve Fodor '
                                   '([Exy48YwwPtk @ 00:35:38])'],
                                  ['Software predicting full 10-digit codes for importers',
                                   'CBP went a little overboard on bad facts in HQ 350722',
                                   'Predicting 10-digit codes is strictly forbidden without a broker '
                                   'license, full stop',
                                   'KYG Trade ([myOI9hprs0c @ 00:12:47]); ImageSearch for HS '
                                   'classification ([Z20K9hWki3Q @ 00:01:27])'],
                                  ['Number of chapters in the US tariff schedule',
                                   'Fodor counts 22 sections and 98 chapters in the US schedule',
                                   'Jo Harper counts 99 chapters; Joe Harper counts 21 sections and 97 '
                                   'chapters',
                                   'Steve Fodor ([Exy48YwwPtk @ 00:24:04]); Star USA, Inc. ([ygZWIWKWe4w @ '
                                   '00:09:19]); Star USA, Inc. ([HbhpILTp9v0 @ 00:06:28])'],
                                  ['Countries stuck paying the Column 2 rate',
                                   'Only Cuba and North Korea, paying 20% in the 2021 example',
                                   'Cuba, North Korea, Russia, and Belarus all sit in Column 2 now',
                                   'Star USA, Inc. ([BwGDeEGn1Wg @ 00:23:49]); Star USA, Inc. '
                                   '([ygZWIWKWe4w @ 00:25:18])'],
                                  ['Which code goes on outbound export paperwork',
                                   'Importers who also export can use HTS codes in both directions',
                                   'Exports run on Schedule B, with 6 digits on commercial documents',
                                   'Shipping Solutions ([zDnjfsml-j4 @ 00:03:24]); Star USA, Inc. '
                                   '([HbhpILTp9v0 @ 00:59:20])'],
                                  ['Reacting when two authorities disagree on code',
                                   'Assume any change triggers review; change only for a foreign customs '
                                   'ruling',
                                   'Importer facing conflicting US and Korean rulings used dual codes '
                                   'instead',
                                   'Star USA, Inc. ([-v_-OQnVlxE @ 01:15:09]); Star USA, Inc. '
                                   '([HbhpILTp9v0 @ 00:44:11])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first money trap is a product detail nobody flagged. USA Customs '
                              'Clearance shows a single-wall stainless steel bottle at about 2.9% duty '
                              'while a vacuum-insulated flask lands at 7.2%, and warns that underpaying '
                              'creates larger problems later than overpaying does [MfmhZLeMz2w @ 00:02:33] '
                              '[MfmhZLeMz2w @ 00:03:07]. Supplyia Sourcing hit the same cliff with '
                              'umbrellas: a travel umbrella under 66032030 came up free, a garden umbrella '
                              'at 6.5%, and a slash-and-underscore after the rate signals added tariffs '
                              'stacked on top [ff_P7M6LKEo @ 00:11:25] [ff_P7M6LKEo @ 00:11:47]. Shipping '
                              'Solutions demonstrated how a 0% base rate misleads: the semiconductor code '
                              'showed a default duty of 0%, yet eight Chapter 99 tariffs could apply '
                              'depending on source, material, and destination, including a Section 122 10% '
                              'additional duty for all countries and Section 301 at 50% on China, declared '
                              'as 9903.91.02 on top of the base code [_I3v11oKRLA @ 00:01:24] [_I3v11oKRLA '
                              '@ 00:03:45]. Even that demo drifted: the code chosen was 8541430010, but '
                              'the code entered into the import-controls lookup was 8541.43.0080, and a '
                              "Section 201 duty surfaced only if the item counted as a 'module.' The check "
                              'Shipping Solutions models is pulling every Chapter 99 line and every Import '
                              'Controls flag, including the Xinjiang prohibition, before quoting a landed '
                              'cost.',
                              'Enforcement traps hit importers who outsourced the paperwork. Supplyia '
                              'Sourcing warns that on DDP terms suppliers may deliberately declare a lower '
                              'invoice value, yet the importer of record stays legally responsible, and '
                              "once audited 'you will still pay all the duty plus you will have to pay the "
                              "fine' [ff_P7M6LKEo @ 00:02:34] [ff_P7M6LKEo @ 00:14:20]. Eastston reports "
                              "CBP dropping 'facilitation' for 'enforcement,' a DOJ trade fraud task force "
                              "operating on 'zero trust,' and False Claims Act reach where 'knowingly' "
                              'covers deliberate ignorance, willful blindness, and reckless disregard '
                              '[-v_-OQnVlxE @ 00:08:10]. On DDP undervaluation specifically, DOJ targets '
                              'the beneficiaries, and prior disclosure covers five years of civil '
                              'penalties but not DOJ fraud [-v_-OQnVlxE @ 00:53:26] [-v_-OQnVlxE @ '
                              '00:50:53]. Steve Fodor calls misclassification the most frequent import '
                              'error, notes CBP uses classification to target high-risk shipments, and '
                              'warns that ignoring a binding ruling carries penalties [Exy48YwwPtk @ '
                              '00:05:55] [Exy48YwwPtk @ 00:32:50]. Clark-Esposito Law Firm lists the '
                              'downstream damage: underpayment or overpayment, fines, even seizure of the '
                              'goods, lost preferences, and added scrutiny [8Lpn0Ae59QU @ 00:01:16]. '
                              'Eastston plays reclassification defensively, assuming any change will '
                              'trigger review and expecting a CBP28 request to follow.',
                              'Search tools fail in specific, repeatable ways. Jo Harper found that a '
                              "'chair' is listed as 'seats,' so plain-English searches miss [ygZWIWKWe4w @ "
                              '00:26:57], and in a separate session Harper flagged British wording such as '
                              "'seat' and 'anorak' inside USITC search [HbhpILTp9v0 @ 00:11:19]. The 2021 "
                              'Star USA webinar adds that ad blockers can break HTS website search and '
                              'that the first CROSS hit should never be taken as the answer [BwGDeEGn1Wg @ '
                              '00:19:33] [BwGDeEGn1Wg @ 01:00:17]. The same session logged about 30 HTS '
                              'updates in a year against a historical two or three, driven by Section 301 '
                              'and 232 actions, which is why Eastston records the HTSUS revision number '
                              'used for every analysis [BwGDeEGn1Wg @ 00:06:30] [-v_-OQnVlxE @ 00:39:58]. '
                              'Eastston names the three biggest problems at importers as no conversations, '
                              'no documented method, and no reviews, and notes that ACE lacks part '
                              'numbers, so ACE reports have to be paired with broker reports that carry '
                              "them [-v_-OQnVlxE @ 01:04:29] [-v_-OQnVlxE @ 01:08:54]. Eastston's poll "
                              'found 69% of attendees saying they had adequate measures. Post-summary '
                              'corrections belong inside roughly a year, a file with none looks '
                              'suspicious, and Eastston recommends quarterly reviews, especially lately.'],
               'table': {'caption': 'Failure Modes With Real Dollars and Penalties Attached',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw Go Wrong',
                                     'Economics Or Penalty Check',
                                     'Expert Source'],
                         'rows': [['DDP supplier undervalues the commercial invoice',
                                   'Supplier declares a lower invoice value on purpose under DDP terms',
                                   'Audit brings all the duty plus a fine; DOJ targets the beneficiaries',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:02:34]); Star USA, Inc. '
                                   '([-v_-OQnVlxE @ 00:53:26])'],
                                  ['Forgetting processing fees in landed cost math',
                                   'MPF runs .3464% on air and ocean; HMF 0.125% ocean only',
                                   '5,000 umbrellas at $2 produced $697.14 total duty including MPF and '
                                   'HMF',
                                   'Supplyia Sourcing ([ff_P7M6LKEo @ 00:14:41])'],
                                  ['Assuming the HTS number defines anti-dumping scope',
                                   'AD scope turns on what the item is, not on the number',
                                   'Check what the item physically is against scope, not just its HTS',
                                   'Star USA, Inc. ([BwGDeEGn1Wg @ 00:10:29])'],
                                  ['Claiming an actual-use provision without the proof',
                                   'Actual-use classifications require proof of the use after entry',
                                   'Proof must be shown within 3 years under 19 CFR 10.131-10.139',
                                   'Star USA, Inc. ([BwGDeEGn1Wg @ 00:52:11])'],
                                  ['Letting an AI platform prepare or file entries',
                                   'Non-US unlicensed platform ran POAs, AI classification, OCR '
                                   'population, and CF 5106',
                                   'CBP held platforms may transmit information but not prepare or file '
                                   'documents',
                                   'KYG Trade ([myOI9hprs0c @ 00:09:35]); ImageSearch for HS '
                                   'classification ([Z20K9hWki3Q @ 00:00:34])'],
                                  ['Misclassification consequences that reach beyond the duty bill',
                                   'Wrong code triggers fines, seizure, lost preferences, and more '
                                   'scrutiny',
                                   'Underpayment or overpayment of duties both cost money either way',
                                   'Clark-Esposito Law Firm P.C. ([8Lpn0Ae59QU @ 00:01:16])'],
                                  ['Leaving IEEPA refund money sitting uncollected at CBP',
                                   '$166B potential refunds across 53M entries and 330,000 importers',
                                   'Set up ACE with ACH refund, which requires a US bank account',
                                   'KYG Trade ([myOI9hprs0c @ 00:36:26]); KYG Trade ([myOI9hprs0c @ '
                                   '00:46:57])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Any Code Touches an Entry',
                           'body': 'Each check traces to a loss, reversal, or enforcement action '
                                   'practitioners reported firsthand. Clear all four before the 10-digit '
                                   'code goes onto Form 7501, where duty is set at the 8th digit.',
                           'items': ['Re-derive every supplier or vendor code from the tariff language, '
                                     'notes, and GRIs, because customs only cares that you use the right '
                                     'HTS [Star USA, Inc. — HbhpILTp9v0 @ 00:56:12].',
                                     'On DDP shipments, verify the declared invoice value yourself, '
                                     'because the importer of record pays all the duty plus the fine after '
                                     'audit [Supplyia Sourcing — ff_P7M6LKEo @ 00:14:20].',
                                     'Pull every Chapter 99 line before trusting a 0% base rate, including '
                                     'Section 122, 301, and 201 exposure [Shipping Solutions — _I3v11oKRLA '
                                     '@ 00:03:45].',
                                     'Log the headings considered, why each was eliminated, and the '
                                     'details that decided the final heading [Star USA, Inc. — ygZWIWKWe4w '
                                     '@ 00:48:03].']}}],
 'pull_quote': '"Customs doesn\'t care if the vendor gave you the wrong HTS, they care that you use the '
               'right HTS." Star USA, Inc. (HbhpILTp9v0 @ 00:56:12).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Lock down an accurate product description covering material, construction, '
                      'function, and intended use before searching any code [The Procurement Lens — '
                      '4IEk0Lxmf1c @ 00:04:30].',
                      'Consider at least three candidate headings and keep a written log of why each was '
                      'eliminated [Star USA, Inc. — ygZWIWKWe4w @ 00:46:16].',
                      'Apply the GRIs in order, read section and chapter notes first, and follow the '
                      'indents instead of matching words [Star USA, Inc. — -v_-OQnVlxE @ 00:26:14].',
                      'Check every Chapter 99 tariff that may stack on the base rate by source, material, '
                      'and destination [Shipping Solutions — _I3v11oKRLA @ 00:02:09].',
                      'Request a CBP binding ruling whenever a classification is uncertain, before the '
                      'goods ship [Clark-Esposito Law Firm P.C. — 8Lpn0Ae59QU @ 00:01:52].',
                      'Run quarterly reviews pairing ACE reports with broker reports that carry part '
                      'numbers [Star USA, Inc. — -v_-OQnVlxE @ 00:51:45].'],
 'statutory_citations': [{'title': 'Star USA, Inc. — HTS Classification: Catching Mistakes Before They '
                                   'Become Costly [00:08:10]',
                          'url': 'https://www.youtube.com/watch?v=-v_-OQnVlxE&t=490s',
                          'relevance': 'Primary practitioner testimony on False Claims Act reach, DOJ '
                                       'targeting, and classification process failures.'},
                         {'title': 'KYG Trade — CBP Ruling HQ 350722 & Guardrails for AI in Trade '
                                   'Compliance [00:12:00]',
                          'url': 'https://www.youtube.com/watch?v=myOI9hprs0c&t=720s',
                          'relevance': 'Primary practitioner testimony on the 6-digit versus 10-digit line '
                                       'for AI classification platforms.'},
                         {'title': 'Steve Fodor — HTS Classification The Most Important Step 062016 '
                                   '[00:35:38]',
                          'url': 'https://www.youtube.com/watch?v=Exy48YwwPtk&t=2138s',
                          'relevance': 'Primary practitioner testimony on importer liability versus broker '
                                       'liability capped at the entry fee.'},
                         {'title': 'Supplyia Sourcing — HTS code lookup:  How to Calculate Duties & '
                                   'Tariffs for U.S Imports? [00:02:34]',
                          'url': 'https://www.youtube.com/watch?v=ff_P7M6LKEo&t=154s',
                          'relevance': 'Primary practitioner testimony on DDP undervaluation exposure for '
                                       'the importer of record.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'MfmhZLeMz2w',
                       'title': 'HTS Codes Explained',
                       'channel': 'USA Customs Clearance',
                       'author': 'USA Customs Clearance',
                       'text': 'A single-wall stainless steel bottle is about 2.9% duty, while a '
                               'vacuum-insulated flask is 7.2%.',
                       'tip': 'A single-wall stainless steel bottle is about 2.9% duty, while a '
                              'vacuum-insulated flask is 7.2%.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=MfmhZLeMz2w&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=MfmhZLeMz2w&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4IEk0Lxmf1c',
                       'title': 'HS Code Explained | How Customs Classify Goods Made Simple',
                       'channel': 'The Procurement Lens',
                       'author': 'The Procurement Lens',
                       'text': 'One digit can blow up your profit margins.',
                       'tip': 'One digit can blow up your profit margins.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=4IEk0Lxmf1c&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=4IEk0Lxmf1c&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x-SDVKIzJdI',
                       'title': 'Tariff Classification - A Step by Step Guide',
                       'channel': 'Cole International',
                       'author': 'Cole International',
                       'text': 'Before importing, have a professional request a binding ruling, which is '
                               'the definitive assessment.',
                       'tip': 'Before importing, have a professional request a binding ruling, which is '
                              'the definitive assessment.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=x-SDVKIzJdI&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=x-SDVKIzJdI&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Exy48YwwPtk',
                       'title': 'HTS Classification The Most Important Step 062016',
                       'channel': 'Steve Fodor',
                       'author': 'Steve Fodor',
                       'text': 'Broker liability is limited to the entry fee, often $100 or less.',
                       'tip': 'Broker liability is limited to the entry fee, often $100 or less.',
                       'timestamp': 2138,
                       'timestamp_seconds': 2138,
                       'timestamp_label': '[00:35:38]',
                       'url': 'https://www.youtube.com/watch?v=Exy48YwwPtk&t=2138s',
                       'markdown': '[00:35:38](https://www.youtube.com/watch?v=Exy48YwwPtk&t=2138s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ygZWIWKWe4w',
                       'title': 'HTS Classification',
                       'channel': 'Star USA, Inc.',
                       'author': 'Star USA, Inc.',
                       'text': 'But always keep a log of the headings you considered, why you eliminated '
                               'them and the details that made you select the heading that you did.',
                       'tip': 'But always keep a log of the headings you considered, why you eliminated '
                              'them and the details that made you select the heading that you did.',
                       'timestamp': 2883,
                       'timestamp_seconds': 2883,
                       'timestamp_label': '[00:48:03]',
                       'url': 'https://www.youtube.com/watch?v=ygZWIWKWe4w&t=2883s',
                       'markdown': '[00:48:03](https://www.youtube.com/watch?v=ygZWIWKWe4w&t=2883s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BwGDeEGn1Wg',
                       'title': 'HTSUS Classification Webinar',
                       'channel': 'Star USA, Inc.',
                       'author': 'Star USA, Inc.',
                       'text': "Don't take the first CROSS hit.",
                       'tip': "Don't take the first CROSS hit.",
                       'timestamp': 3617,
                       'timestamp_seconds': 3617,
                       'timestamp_label': '[01:00:17]',
                       'url': 'https://www.youtube.com/watch?v=BwGDeEGn1Wg&t=3617s',
                       'markdown': '[01:00:17](https://www.youtube.com/watch?v=BwGDeEGn1Wg&t=3617s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ff_P7M6LKEo',
                       'title': 'HTS code lookup:  How to Calculate Duties & Tariffs for U.S Imports?',
                       'channel': 'Supplyia Sourcing',
                       'author': 'Supplyia Sourcing',
                       'text': "If you are the importer of the record, you're still legally responsible "
                               'for whatever the amount you should pay.',
                       'tip': "If you are the importer of the record, you're still legally responsible for "
                              'whatever the amount you should pay.',
                       'timestamp': 154,
                       'timestamp_seconds': 154,
                       'timestamp_label': '[00:02:34]',
                       'url': 'https://www.youtube.com/watch?v=ff_P7M6LKEo&t=154s',
                       'markdown': '[00:02:34](https://www.youtube.com/watch?v=ff_P7M6LKEo&t=154s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B4gRBWbdUqo',
                       'title': 'Product Classification Under HTSUS Part 1',
                       'channel': 'Law Office of Yuri Starikov, LLC',
                       'author': 'Law Office of Yuri Starikov, LLC',
                       'text': "If you're wrong it's okay you can always go back see that's the strategy.",
                       'tip': "If you're wrong it's okay you can always go back see that's the strategy.",
                       'timestamp': 1167,
                       'timestamp_seconds': 1167,
                       'timestamp_label': '[00:19:27]',
                       'url': 'https://www.youtube.com/watch?v=B4gRBWbdUqo&t=1167s',
                       'markdown': '[00:19:27](https://www.youtube.com/watch?v=B4gRBWbdUqo&t=1167s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_I3v11oKRLA',
                       'title': 'How to Calculate U.S. Import Tariffs (HTS Codes & Duties Explained)',
                       'channel': 'Shipping Solutions',
                       'author': 'Shipping Solutions',
                       'text': 'There are 8 additional Chapter 99 tariffs that may apply to my product '
                               "depending on the source and material composition of my goods and where I'm "
                               'shipping to.',
                       'tip': 'There are 8 additional Chapter 99 tariffs that may apply to my product '
                              "depending on the source and material composition of my goods and where I'm "
                              'shipping to.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=_I3v11oKRLA&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=_I3v11oKRLA&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-v_-OQnVlxE',
                       'title': 'HTS Classification: Catching Mistakes Before They Become Costly',
                       'channel': 'Star USA, Inc.',
                       'author': 'Star USA, Inc.',
                       'text': 'There is only one correct classification for any given import.',
                       'tip': 'There is only one correct classification for any given import.',
                       'timestamp': 1416,
                       'timestamp_seconds': 1416,
                       'timestamp_label': '[00:23:36]',
                       'url': 'https://www.youtube.com/watch?v=-v_-OQnVlxE&t=1416s',
                       'markdown': '[00:23:36](https://www.youtube.com/watch?v=-v_-OQnVlxE&t=1416s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-v_-OQnVlxE',
                       'title': 'HTS Classification: Catching Mistakes Before They Become Costly',
                       'channel': 'Star USA, Inc.',
                       'author': 'Star USA, Inc.',
                       'text': 'I always assume that a change will trigger review.',
                       'tip': 'I always assume that a change will trigger review.',
                       'timestamp': 4276,
                       'timestamp_seconds': 4276,
                       'timestamp_label': '[01:11:16]',
                       'url': 'https://www.youtube.com/watch?v=-v_-OQnVlxE&t=4276s',
                       'markdown': '[01:11:16](https://www.youtube.com/watch?v=-v_-OQnVlxE&t=4276s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'myOI9hprs0c',
                       'title': 'CBP Ruling HQ 350722 & Guardrails for AI in Trade Compliance',
                       'channel': 'KYG Trade',
                       'author': 'KYG Trade',
                       'text': 'There still has to be human intervention.',
                       'tip': 'There still has to be human intervention.',
                       'timestamp': 1332,
                       'timestamp_seconds': 1332,
                       'timestamp_label': '[00:22:12]',
                       'url': 'https://www.youtube.com/watch?v=myOI9hprs0c&t=1332s',
                       'markdown': '[00:22:12](https://www.youtube.com/watch?v=myOI9hprs0c&t=1332s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'myOI9hprs0c',
                       'title': 'CBP Ruling HQ 350722 & Guardrails for AI in Trade Compliance',
                       'channel': 'KYG Trade',
                       'author': 'KYG Trade',
                       'text': "We're charging a flat fee to do it because the important thing is to get "
                               'into court.',
                       'tip': "We're charging a flat fee to do it because the important thing is to get "
                              'into court.',
                       'timestamp': 2713,
                       'timestamp_seconds': 2713,
                       'timestamp_label': '[00:45:13]',
                       'url': 'https://www.youtube.com/watch?v=myOI9hprs0c&t=2713s',
                       'markdown': '[00:45:13](https://www.youtube.com/watch?v=myOI9hprs0c&t=2713s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z20K9hWki3Q',
                       'title': 'The US CBP declaring an AI-based HS classification tool illegal.',
                       'channel': 'ImageSearch for HS classification',
                       'author': 'ImageSearch for HS classification',
                       'text': 'General six digit HS codes are completely fine.',
                       'tip': 'General six digit HS codes are completely fine.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=Z20K9hWki3Q&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=Z20K9hWki3Q&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zDnjfsml-j4',
                       'title': 'How to Use the Harmonized Tariff Schedule of the United States',
                       'channel': 'Shipping Solutions',
                       'author': 'Shipping Solutions',
                       'text': 'The HTS is a 10-digit code designed so that each article falls into only '
                               'one category.',
                       'tip': 'The HTS is a 10-digit code designed so that each article falls into only '
                              'one category.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=zDnjfsml-j4&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=zDnjfsml-j4&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8Lpn0Ae59QU',
                       'title': 'Tariffs & Classification Explained: Stay Compliant & Avoid Penalties',
                       'channel': 'Clark-Esposito Law Firm P.C.',
                       'author': 'Clark-Esposito Law Firm P.C.',
                       'text': 'Incorrect classification can lead to underpayment or overpayment of '
                               'duties, fines, or even seizure of your goods.',
                       'tip': 'Incorrect classification can lead to underpayment or overpayment of duties, '
                              'fines, or even seizure of your goods.',
                       'timestamp': 76,
                       'timestamp_seconds': 76,
                       'timestamp_label': '[00:01:16]',
                       'url': 'https://www.youtube.com/watch?v=8Lpn0Ae59QU&t=76s',
                       'markdown': '[00:01:16](https://www.youtube.com/watch?v=8Lpn0Ae59QU&t=76s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CcVyqKoA9dY',
                       'title': 'What Is an HTS Code? | U.S. Tariff Classification Explained',
                       'channel': 'Straightforward ITC',
                       'author': 'Straightforward ITC',
                       'text': 'You do not classify a product simply by searching for the description that '
                               'sounds closest.',
                       'tip': 'You do not classify a product simply by searching for the description that '
                              'sounds closest.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=CcVyqKoA9dY&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=CcVyqKoA9dY&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HbhpILTp9v0',
                       'title': 'HTSUS Classification',
                       'channel': 'Star USA, Inc.',
                       'author': 'Star USA, Inc.',
                       'text': "Customs doesn't care if the vendor gave you the wrong HTS, they care that "
                               'you use the right HTS.',
                       'tip': "Customs doesn't care if the vendor gave you the wrong HTS, they care that "
                              'you use the right HTS.',
                       'timestamp': 3372,
                       'timestamp_seconds': 3372,
                       'timestamp_label': '[00:56:12]',
                       'url': 'https://www.youtube.com/watch?v=HbhpILTp9v0&t=3372s',
                       'markdown': '[00:56:12](https://www.youtube.com/watch?v=HbhpILTp9v0&t=3372s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
