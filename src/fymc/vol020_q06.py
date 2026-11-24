from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'pricing-intelligence-and-cost-buildup',
 'question_prompt': 'How do I find what the government paid before, read demand data, and build a '
                    'defensible price?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Pricing Intelligence and Cost Buildup',
 'subtitle': 'Past award prices from FPDS and USASpending.gov, award history for recompetes, finding WOSB '
             'set-asides in FPDS, DLA DIBBS demand, direct and indirect costs (fringe, overhead, G&A, wrap '
             'rates), FAR 31 cost support, FAR 12/15 pricing, and FAR 15 negotiation',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one rule: never price a federal bid blind. Kizzy Parks, '
                      'Fox Wade, FedAccess and Neil McDonnell pull incumbent award values out of FPDS, '
                      'USAspending, GSA eLibrary and direct POC emails, then work backwards from term '
                      "length and evaluation criteria. Solvability's cost team builds the other half of "
                      'the number: fringe near 30%, G&A at an 8-15% norm, a client-site wrap rate near 1.5 '
                      'versus the Reagan-era 2.0 multiplier, and a 5-10% fee. FAR-side speakers add the '
                      'hard lines: certified cost or pricing data above $2M, allocable and supportable '
                      'costs, and unallowables kept out of every pool. Tension remains over how low to go: '
                      'Parks priced so low a contracting office asked if it was an error and won, Bobby '
                      'Butler breaks even on the first 1-12 DLA awards, while Solvability warns underbid '
                      'fringe loses money.',
 'key_metrics': [{'label': 'Client-Site Wrap Rate',
                  'metric': 'Client-Site Wrap Rate',
                  'value': 'About 1.5 ($50/hr pay becomes about $75/hr bill); competitors may target 1.45',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Built from 30% fringe, 3% overhead, 8% G&A and 7% fee for staff placed at a '
                             'government site, replacing the 2.0 multiplier the speaker says dates to the '
                             'Reagan years',
                  'source': 'Solvability ([lOumu-Dk0Jw @ 00:40:51])'},
                 {'label': 'Competitive G&A Band',
                  'metric': 'Competitive G&A Band',
                  'value': '8-15% norm; 60% G&A is out of the game',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "The speaker's benchmark for a G&A rate that can still win price-driven "
                             'federal competitions',
                  'source': 'Solvability ([lOumu-Dk0Jw @ 00:03:35])'},
                 {'label': 'Recompete Pipeline Multiple',
                  'metric': 'Recompete Pipeline Multiple',
                  'value': '$25-100M in opportunities for every $5M of revenue targeted',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Pipeline sizing rule for recompetes pulled from FPDS, with 2027 revenue to '
                             'be won in 2026',
                  'source': 'Neil McDonnell ([17foq325L5w @ 00:10:33])'},
                 {'label': 'Recovered Incumbent Base Award',
                  'metric': 'Recovered Incumbent Base Award',
                  'value': '$1,686,566.88 over three years',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Total recovered from modification 0 of a DHS NAICS 541611 incumbent contract '
                             'after sorting FPDS by date signed; the latest action alone showed 348k',
                  'source': 'Fox Wade ([Z2ZeI5rayvk @ 00:02:50])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every pricing practitioner in this lineup starts from the same premise: the '
                              'last price the government paid is public, and bidding without it is how '
                              'owners burn money. Fox Wade admits their early pricing was off by $4-5M and '
                              'once by $15M, and their answer is to pull what the government already paid '
                              'out of free public data before touching a bid number [Z2ZeI5rayvk @ '
                              '00:00:37]. FedAccess opens with an owner who spent heavily chasing a '
                              'contract that turned out to be worth only a couple hundred thousand '
                              'dollars, not millions, then walks the fix through SAM.gov and FPDS step by '
                              'step [GrYP5KyxBho @ 00:01:29]. Kizzy Parks makes it a standing habit: on '
                              'every sources sought, RFI, RFQ or solicitation, email the POC and ask '
                              'whether there is an incumbent, its name, its contract number and its '
                              'contract value [L0SM3XAM3IE @ 00:00:24]. Neil McDonnell frames FPDS as '
                              "roughly 80% of where a contractor's activity should live, covering what "
                              'they estimate is ninety-plus percent of awards and excluding only '
                              'classified buys and purchases at or under $10,000 [17foq325L5w @ 00:04:57]. '
                              'The shared logic is that pricing intelligence and pipeline intelligence '
                              'come out of the same records, so the operator who mines award history wins '
                              'twice: once on target selection and again on the number written into the '
                              'bid, before a single labor rate is built.',
                              'The second point of agreement is that the price paid is only a reference '
                              'until the evaluation criteria tell you how to use it. Kizzy Parks puts it '
                              'bluntly: knowing the price is great, but the evaluation criteria always '
                              'rule; on a lowest-cost award with a $500K prior, come in around that or '
                              'lower, while technical-led awards turn the old price into a rough guide '
                              '[L0SM3XAM3IE @ 00:02:44]. Carrie, the Colorado government contracts lawyer '
                              'with 25 years in the field, draws the same line in FAR Part 15 terms: LPTA '
                              'makes technical pass/fail with no trade-off, while best value must still '
                              'evaluate price and generally past performance [Tj7x3UDuOSE @ 00:12:51]. On '
                              "the cost side, Solvability's Jenny says price must be as low as reasonable "
                              'or you are just going to lose, and even a best-value buyer needs a reason '
                              'to pay more [lOumu-Dk0Jw @ 00:02:09]. Ellen Beebe, after 33 years in '
                              'estimating and pricing, splits the market in two: commercial items under '
                              "Part 12 are priced to what the market will bear against competitors' "
                              'similar items, while Part 15 sole-source proposals over $2M demand '
                              'certified cost or pricing data backed by a bill of materials consolidated '
                              'across every line item [SpRIyXgvkg0 @ 00:01:06]. Every speaker treats the '
                              'final number as a function of the evaluation method and the buying vehicle, '
                              'never of what the contractor would like to charge.',
                              'The baseline prerequisite the cost-side speakers share is a '
                              'books-and-records system that can defend the number after award. '
                              "Solvability's Johnny Clark, a fractional GovCon CFO, tells contractors to "
                              "book the way they bill, pointing to DCAA's SF 1408 checklist, and to run "
                              'GAAP accrual books with a monthly close by the 15th to 20th, direct and '
                              'indirect costs separated, and interest expense booked as unallowable '
                              '[EBQwejU6UUQ @ 00:05:37]. GovSuccess reduces FAR 31.201-2 to five '
                              'conditions that all have to pass: reasonableness, allocability, accounting '
                              'standards, contract terms and cost-principle limits, warning that clearing '
                              'one does not settle the rest and that an indirect-cost pool never makes an '
                              'unallowable expense disappear [i7_rrrRpotk @ 00:01:10]. That lines up with '
                              "Jenny's unallowable list: interest, alcohol, entertainment, first-class "
                              'airfare, lobbying, gifts, contributions and advertising [lOumu-Dk0Jw @ '
                              '00:09:52]. Carrie adds that certified cost or pricing data must be facts, '
                              'must include all sub quotes, and must disclose profit or fee plus overhead '
                              "and G&A, including the parent company's, with no exemption for small "
                              'businesses [Tj7x3UDuOSE @ 00:17:35]. The consensus is that intelligence '
                              'gets you to a competitive number, but only clean timekeeping, a segregated '
                              'chart of accounts and documented allocations let you keep the money once an '
                              'auditor or contracting officer starts asking questions.'],
               'table': {'caption': 'Where the pricing practitioners agree before any number goes on a bid',
                         'headers': ['Consensus Point',
                                     'Practitioner Practice',
                                     'Operator Payoff',
                                     'Expert Source'],
                         'rows': [['Prior award prices are free public data',
                                   'Pull what the government paid from FPDS before pricing, then team with '
                                   'the incumbent if not ready to prime',
                                   'Avoids the $4-5M and $15M misses the speaker made early on',
                                   'Fox Wade ([Z2ZeI5rayvk @ 00:00:37])'],
                                  ['Always ask the POC for incumbent data',
                                   'Email asking for incumbent name, contract number and contract value on '
                                   'every sources sought, RFI, RFQ or solicitation',
                                   'Gets the baseline price straight from the buyer when no attachment '
                                   'already lists it',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:00:24])'],
                                  ['Evaluation criteria always rule the price',
                                   'Match or undercut the prior value on lowest-cost awards; use it only '
                                   'as a guide on technical-led awards',
                                   'Stops operators from overpricing LPTA work or underselling technical '
                                   'trade-offs',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:02:44])'],
                                  ['LPTA and best value price differently',
                                   'Treat LPTA technical as pass/fail with no trade-off; expect price plus '
                                   'past performance in best value',
                                   'Tells you whether the cheapest acceptable offer or the strongest value '
                                   'story wins',
                                   'How To Sell To & Win Federal Government Contracts ([Tj7x3UDuOSE @ '
                                   '00:12:51])'],
                                  ['Indirect rates must stay competitive',
                                   'Keep G&A inside an 8-15% norm because a 60% rate means you will never '
                                   'succeed',
                                   'Keeps the wrapped bill rate inside the range that actually wins awards',
                                   'Solvability ([lOumu-Dk0Jw @ 00:03:35])'],
                                  ['Books must support the bill',
                                   'Book the way you bill using GAAP accrual, monthly close, and separated '
                                   'direct and indirect costs',
                                   'Positions the firm to pass the pre-award survey when a cost-type award '
                                   'lands',
                                   'Solvability ([EBQwejU6UUQ @ 00:05:37])'],
                                  ['Every claimed cost must pass five tests',
                                   'Check reasonableness, allocability, accounting standards, contract '
                                   'terms and cost-principle limits before billing',
                                   'Prevents shared invoices or unallowables from contaminating proposals '
                                   'and reimbursement requests',
                                   'Win Government Contracts with GovSuccess ([i7_rrrRpotk @ '
                                   '00:01:10])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Fox Wade's extraction routine is the cleanest on record: copy the incumbent "
                              'contract number into FPDS, sort by date signed, ignore the latest '
                              'modification (theirs showed 348k), and scroll down to modification 0 for '
                              'the base award, which revealed an August 2020 award running Sep 28 to Sep '
                              '27 2023, not a set-aside, not a BPA, totaling $1,686,566.88 over three '
                              'years [Z2ZeI5rayvk @ 00:02:50]. FedAccess runs the same date-signed sort on '
                              'a Seeley Lake janitorial recompete with a base year plus four options and '
                              "lands on $47,352.42 for 3/10/2020 to 9/30/2024, plus the incumbent's "
                              'contact details and the number of bids received [GrYP5KyxBho @ 00:03:56]. '
                              'Neil McDonnell insists on field-specific search rather than bare keywords, '
                              'which USAspending cannot match, then targets 100 to 200 results with a '
                              'ceiling of 500, sorts by action obligation or date signed, and exports CSV '
                              'against a roughly 5,000-row limit, never PDF because there is no value in '
                              'it [0cGdQvymmvY @ 00:25:43]. In the WOSB walkthrough they read a $146K '
                              'action as probably around $1M total and a $2M action as possibly $10M, and '
                              'they ignore anything under $1M when hunting [YR_aPfXedtA @ 00:15:26]. The '
                              'repeatable mechanic is always the same: find the base action, rebuild the '
                              'term and total, and only then decide where your number lands against the '
                              'incumbent.',
                              'For labor rates, Kizzy Parks calls GSA eLibrary their number one intel tip: '
                              'it shows which schedules an incumbent or competitor holds, such as a JV on '
                              'STARS III and two firms on MAS, along with posted rates like 63.52 for '
                              'specialists and labor category descriptions you can borrow to craft your '
                              'own [L0SM3XAM3IE @ 00:13:57]. On buy.gsa.gov a contract-number search '
                              'failed, but a Project Manager II lookup averaged 143 with a 103 to 183 '
                              "range, and the floor of 60 tied to a bachelor's degree and six years of "
                              'experience, so a candidate with ten years justifies a higher rate '
                              '[L0SM3XAM3IE @ 00:11:49]. SamSearch works USAspending the same way, '
                              'keyword-searching award descriptions such as website development to surface '
                              "historical values, then filtering by the incumbent's ID to see everything "
                              "that firm has been paid [NiWdxgnr3xo @ 00:12:51]. Eric Coffie's bulk "
                              'version filters FY2019 and FY2018 plus a state, downloads the file, and '
                              'builds an Excel pivot table to sort the fields into a usable rate and award '
                              'picture [Hr_U9z1xK2g @ 00:00:59]. Stacked together, these four pulls give '
                              'an operator a defensible labor-rate band, a list of who is charging what, '
                              'and the exact category language buyers already accept, all before a single '
                              'proposal page gets drafted or a wrap rate is applied.',
                              "Solvability's Jenny builds the burden in FOG order, fringe then overhead "
                              'then G&A, with fringe equal to payroll costs over productive labor, '
                              'overhead equal to overhead costs over direct labor, and G&A equal to '
                              'corporate costs over total cost input [lOumu-Dk0Jw @ 00:31:40]. Fringe runs '
                              'about 30%: payroll taxes near 10% (bid 5% and you lose money), leave of 200 '
                              'out of 2,080 hours, and traps like 88 holiday hours instead of 80 or 56 '
                              'hours of SCA/EO sick leave. The old 2.0 multiplier, $50 to $100, dates to '
                              'the Reagan years; at a client site, 30% fringe, 3% overhead, 8% G&A and 7% '
                              'fee lands near 1.5, so $50 becomes about $75, and competitors may target '
                              '1.45 [lOumu-Dk0Jw @ 00:40:51]. Run it backwards and a $75 bill rate caps '
                              'pay at about $48. Johnny Clark adds that a strong growth forecast can drop '
                              "G&A, so you don't need to bid 40% G&A [EBQwejU6UUQ @ 00:00:35]. On the "
                              'product side, Bobby Butler prices landed cost: a $10 flashlight in 2025 can '
                              'cost $13 in 2026 once tariffs, logistics, packaging and shipping are added, '
                              'so $10 plus 15% is the wrong math [6Fz712e3oWc @ 00:24:31]. Fee stays '
                              "modest across the board, with Jenny calling 5-10% good and noting you won't "
                              'see 12-15%.'],
               'table': {'caption': 'Street-level pricing tools, exact steps and the numbers practitioners '
                                    'pulled',
                         'headers': ['Tool or Mechanic',
                                     'Exact Steps Taught',
                                     'Number Reported',
                                     'Expert Source'],
                         'rows': [['FPDS base award reconstruction',
                                   'Paste incumbent contract number, sort by date signed, scroll to '
                                   'modification 0',
                                   '$1,686,566.88 base over three years versus a 348k latest action',
                                   'Fox Wade ([Z2ZeI5rayvk @ 00:02:50])'],
                                  ['FPDS recompete price check',
                                   'Sort by date signed and read incumbent contact details and bid count',
                                   '$47,352.42 for the 3/10/2020 to 9/30/2024 janitorial contract',
                                   'FedAccess ([GrYP5KyxBho @ 00:03:56])'],
                                  ['FPDS export discipline',
                                   'Narrow by field, sort by action obligation or date signed, export CSV '
                                   'only',
                                   'Target 100-200 results, 500 maximum, roughly 5,000-row CSV limit',
                                   'Neil McDonnell ([0cGdQvymmvY @ 00:25:43])'],
                                  ['FPDS description rate leaks',
                                   'Read the description field on prior awards for embedded labor rates',
                                   '274 IT strategic capital planner, 139 program admin, 192 project '
                                   'control',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:07:21])'],
                                  ['buy.gsa.gov labor category benchmark',
                                   'Search the category instead of the contract number and read the range',
                                   'Project Manager II average 143, range 103-183, floor of 60',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:11:49])'],
                                  ['Excel wrap rate calculator',
                                   'Apply fringe, overhead, G&A and fee in order, then back-solve '
                                   'affordable pay',
                                   'A $75 bill rate means paying no more than about $48',
                                   'Solvability ([lOumu-Dk0Jw @ 00:42:07])'],
                                  ['Landed cost on DLA product quotes',
                                   'Add tariffs, logistics, packaging and shipping before applying any '
                                   'margin',
                                   'A $10 flashlight in 2025 may cost $13 in 2026',
                                   'myContractScout ([6Fz712e3oWc @ 00:24:31])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Pricing Intel Shortcuts the Practitioners Actually Use',
                           'body': 'Four small habits that separate operators who price from data from '
                                   'operators who price from hope.',
                           'items': ['Share and save FPDS searches by URL: the query lives in the URL, so '
                                     'copy it and send it to a teammate instead of rebuilding filters '
                                     '[Neil McDonnell — 17foq325L5w @ 00:25:07]',
                                     'Never guess a withheld value: Kizzy Parks assumed an Army award was '
                                     'at least $250K and it came in around $35K, so ask the POC for '
                                     'incumbent, contract number and value every time [Kizzy Parks — '
                                     'L0SM3XAM3IE @ 00:05:28]',
                                     'Pull the old solicitation alongside the award: in SAM.gov use exact '
                                     'phrase with Status set to Inactive, because scope can grow from 2 '
                                     'people to 10 [FedAccess — GrYP5KyxBho @ 00:05:33]',
                                     'When a cost is gray-area, put it in overhead rather than G&A, or '
                                     "your G&A rate goes through the roof and you won't win any business "
                                     '[Solvability — lOumu-Dk0Jw @ 00:27:28]']},
               'sop_steps': [{'step': 1,
                              'title': 'Extract incumbent identity and value',
                              'action': 'Email the POC on every sources sought, RFI, RFQ or solicitation '
                                        'asking for incumbent name, contract number and contract value.',
                              'detail': 'Skip the email only when an attachment already names the '
                                        'incumbent and value, then work backwards to the term behind the '
                                        'number (1, 2.5, 3 or 5 years) [Kizzy Parks — L0SM3XAM3IE @ '
                                        '00:00:24]'},
                             {'step': 2,
                              'title': 'Rebuild the base award in FPDS',
                              'action': 'Paste the incumbent contract number into FPDS, sort by date '
                                        'signed, and open modification 0.',
                              'detail': 'Read award date, start and end dates, set-aside and BPA status, '
                                        "and total value; Fox Wade's base award showed $1,686,566.88 over "
                                        'three years while the latest action showed only 348k [Fox Wade — '
                                        'Z2ZeI5rayvk @ 00:02:50]'},
                             {'step': 3,
                              'title': 'Benchmark labor rates',
                              'action': "Search the labor category on buy.gsa.gov and the incumbent's "
                                        'schedules on GSA eLibrary.',
                              'detail': 'Record the average, range and floor (Project Manager II averaged '
                                        "143 across 103-183, floor of 60 at six years' experience) and "
                                        "adjust for your candidates' experience [Kizzy Parks — L0SM3XAM3IE "
                                        '@ 00:11:49]'},
                             {'step': 4,
                              'title': 'Wrap and back-solve the rate',
                              'action': 'Apply fringe, overhead, G&A and fee in FOG order in an Excel wrap '
                                        'calculator, then run it backwards from the target bill rate.',
                              'detail': 'At a client site expect roughly a 1.5 wrap; a $75 bill rate means '
                                        "you can't pay more than about $48, so set pay from the "
                                        'competitive bill rate rather than the reverse [Solvability — '
                                        'lOumu-Dk0Jw @ 00:42:07]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["The sharpest split is over how hard to cut price. Solvability's Jenny "
                              'compares indirect rates to taxes, using a downtown Atlanta dealer analogy, '
                              'and says price must be as low as reasonable "or else you\'re just going to '
                              'lose," while conceding that best value still needs a reason to pay more '
                              '[lOumu-Dk0Jw @ 00:02:09]. Kizzy Parks refuses to let the number drive the '
                              'bid by itself: "the evaluation criteria always rules." A $500K lowest-cost '
                              'prior award means coming in at or under that figure, while a technically '
                              'weighted buy only uses price as a rough guide [L0SM3XAM3IE @ 00:02:44]. On '
                              'an Air Force exercise physiologist LPTA, they priced so low that '
                              'contracting asked whether they had made an error, and they still won '
                              'because they knew the profit they could keep. Carrie, a 25-year government '
                              'contracts lawyer, pushes back on the race to zero: "Profit is good." Fee '
                              'caps only bite on cost-plus-fixed-fee deals, at 15% for R&D and 10% '
                              'otherwise, and sole-source awards simply get negotiated harder [Tj7x3UDuOSE '
                              '@ 00:35:22]. Bobby Butler of myContractScout runs a third line on DLA buys. '
                              'Break even or take a thin margin on the first one to twelve awards purely '
                              'to build CPARS history, then price for profit [6Fz712e3oWc @ 00:17:49].',
                              'Practitioners also split on which rates belong in the bid. Johnny Clark, a '
                              'fractional GovCon CFO at Solvability, tells operators to price on forecast: '
                              'if growth will dilute corporate cost, you "don\'t need to bid 40% G&A" '
                              'today [EBQwejU6UUQ @ 00:00:35]. Jenny sets rates per calendar year and '
                              'acknowledges they fall as the company scales, yet assumes flat rates across '
                              'three-to-five-year forecasts [lOumu-Dk0Jw @ 00:29:37]. Jenny also retires '
                              'the old rule of thumb. A 2.0 multiplier that turns $50 of pay into a $100 '
                              'bill rate dates to "the Reagan years." A client-site staffing shop should '
                              'run about 1.5, built from 30% fringe, 3% overhead, 8% G&A and 7% fee, and '
                              'competitors may target 1.45 [lOumu-Dk0Jw @ 00:40:51]. The pricing method '
                              'itself forks by FAR part. Ellen Beebe, with 33 years in estimating, says '
                              'Part 15 sole-source proposals over $2M demand certified cost or pricing '
                              'data, including a bill of materials consolidated across every line item. '
                              'Part 12 commercial items are priced to what the market will bear, off '
                              "competitors' similar items [SpRIyXgvkg0 @ 00:01:06]. Carrie adds that "
                              'certification is prohibited below the $250,000 SAT and required above $2M '
                              'and on modifications above $750K. Adequate competition and commercial items '
                              'are exempt [Tj7x3UDuOSE @ 00:20:51].',
                              'The intel stack is contested too. Neil McDonnell calls FPDS "80% of your '
                              'activity, or it should be," and builds two-year recompete pipelines almost '
                              'entirely from it, sizing $25-100M in opportunities to land $5M in revenue '
                              '[17foq325L5w @ 00:11:22]. SamSearch counters that USAspending is free, '
                              'easier than SAM, and covers $6.8T a year, making it the place to pull '
                              'historical award values by keyword and incumbent ID [NiWdxgnr3xo @ '
                              '00:12:51]. Kizzy Parks prefers FPDS but leaned on paid GovWin for the Air '
                              'Force pricing, distrusts SAM archives, and cross-checks GovTribe trials. '
                              'They call GSA eLibrary rate sheets their "number one tip" for intel '
                              '[L0SM3XAM3IE @ 00:13:57]. Kizzy also works the small end of the market. '
                              'GovWin showed Catholic youth coordinator awards running from about $17K to '
                              '$40-50K, and a 20-50% profit on those still pays well. Bobby Butler rejects '
                              'paid lead feeds outright. A $3,000-a-month list resold to 25 to 100 '
                              'companies triggers a race to the bottom, and switching to the free DLA No '
                              'Bid List saves $36,000 a year [6Fz712e3oWc @ 00:04:15]. Everyone here mines '
                              'federal award data, but they split on which database leads, which dollar '
                              'floor matters, and whether a paid layer earns its fee.'],
               'table': {'caption': 'Competing pricing-intelligence playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How aggressively to cut price on a lowest-cost buy',
                                   'Price as low as reasonable or else you lose; G&A norm runs 8-15%',
                                   'Let evaluation criteria rule; price only guides technically weighted '
                                   'awards',
                                   'Solvability ([lOumu-Dk0Jw @ 00:02:09]); Kizzy Parks ([L0SM3XAM3IE @ '
                                   '00:02:44])'],
                                  ['Whether profit should be squeezed hard to win the award',
                                   'Profit is good; caps apply only to CPFF at 15% R&D and 10% otherwise',
                                   'Break even or take a small profit on the first 1-12 DLA awards to '
                                   'build CPARS',
                                   'How To Sell To & Win Federal Government Contracts ([Tj7x3UDuOSE @ '
                                   '00:35:22]); myContractScout ([6Fz712e3oWc @ 00:17:49])'],
                                  ['Which indirect rates actually go into the bid',
                                   'Price on forecast growth, so you do not need to bid 40% G&A today',
                                   'Set rates per calendar year and assume flat rates for 3-5 year '
                                   'forecasts',
                                   'Solvability ([EBQwejU6UUQ @ 00:00:35]); Solvability ([lOumu-Dk0Jw @ '
                                   '00:29:37])'],
                                  ['How the price itself gets justified to the buyer',
                                   'Part 15 sole source over $2M needs certified cost or pricing data and '
                                   'a consolidated BOM',
                                   'Part 12 commercial items priced to what the market will bear, proven '
                                   'by invoices to the buying command',
                                   'US Federal Contractor Registration ([SpRIyXgvkg0 @ 00:00:43]); US '
                                   'Federal Contractor Registration ([SpRIyXgvkg0 @ 00:01:48])'],
                                  ['Which database anchors pricing and recompete research',
                                   'FPDS is 80% of activity and allows field-specific search unlike '
                                   'USAspending',
                                   'USAspending is free, easier than SAM, and the best place to find '
                                   'winners',
                                   'Neil McDonnell ([0cGdQvymmvY @ 00:17:49]); SamSearch - AI for '
                                   'Government Contracting ([NiWdxgnr3xo @ 00:16:07])'],
                                  ['Which dollar floor is worth researching at all',
                                   'Ignore anything under $1M when building a recompete search',
                                   'Small awards of roughly $17K to $50K still pay well at 20-50% profit',
                                   'Neil McDonnell ([YR_aPfXedtA @ 00:05:37]); Kizzy Parks ([L0SM3XAM3IE @ '
                                   '00:17:11])'],
                                  ['Whether paid intel beats free public award data',
                                   'Paid GovWin surfaced the incumbent and pricing behind the Air Force '
                                   'win',
                                   'Paid $3,000-a-month lead lists resold to 25-100 firms cause a race to '
                                   'the bottom',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:03:00]); myContractScout ([6Fz712e3oWc '
                                   '@ 00:04:15])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest misses start with misread award data. Fox Wade admits their '
                              'early pricing was off by $4-5M, and once by $15M. The fix was to pull the '
                              "incumbent's FPDS record, sort by date signed, and scroll to modification 0 "
                              'for the base award [Z2ZeI5rayvk @ 00:00:37]. That step matters because the '
                              'latest action showed only $348K while the base award totaled $1,686,566.88 '
                              'over three years [Z2ZeI5rayvk @ 00:02:50]. FedAccess opens with an owner '
                              'who spent heavily chasing a contract worth only "a couple hundred '
                              'thousand." They also warn that scope can jump from 2 people to 10, so the '
                              'old solicitation must be pulled before trusting the $47,352.42 price '
                              '[GrYP5KyxBho @ 00:05:33]. Kizzy Parks got burned when the Army withheld the '
                              'value: they assumed at least $250K, and the award came in around $35K '
                              '[L0SM3XAM3IE @ 00:05:28]. Neil McDonnell flags the opposite trap. '
                              'Completion dates mislead because of option years, and a $146K obligation is '
                              'probably about $1M total, while $2M could be $10M [YR_aPfXedtA @ 00:15:26]. '
                              "Kizzy's counter is to work backwards on term every time, because a $2M "
                              'value means something very different over one, three, or five years.',
                              'On the buildup side, Jenny warns that payroll taxes alone run about 10%. '
                              'Bidding 5% fringe means "you\'re going to lose money cuz you haven\'t '
                              'covered everything," and a 60% G&A puts a firm out of the game against an '
                              '8-15% norm [lOumu-Dk0Jw @ 00:13:16]. Their own worked example uses $10M '
                              'revenue with 30% fringe, 38.35% overhead, 10% G&A and 8% profit, and they '
                              'flag those rates as too high to win [lOumu-Dk0Jw @ 00:35:09]. Johnny '
                              "Clark's DCAA fail test is a single $300,000 wages line. Labor distribution "
                              'must tie to gross payroll, timesheet changes need an audit trail, and a '
                              'bill for 170 PM hours must trace back to daily time recording [EBQwejU6UUQ '
                              '@ 00:17:14]. GovSuccess shows the allocation trap with a $2,000 shared '
                              'test-equipment invoice across four projects. Dumping it on one job is '
                              'wrong, equal splits are not automatic, and one-quarter usage points to a '
                              '$500 allocation to investigate [i7_rrrRpotk @ 00:02:29]. They add that "an '
                              'indirect-cost pool does not make an unallowable expense disappear." Bobby '
                              "Butler's landed-cost lesson closes the loop. A $10 flashlight in 2025 can "
                              'cost $13 in 2026 after tariffs, logistics, packaging and shipping, so "$10 '
                              '+ 15%" is the wrong math [6Fz712e3oWc @ 00:24:31].',
                              'Execution traps hit after the number is set. Bobby Butler watched an '
                              'awardee fail to meet the delivery date and names the repeat mistakes: not '
                              'verifying the item is still open, ignoring delivery dates, bidding without '
                              'a supplier, omitting freight and tariffs, and skipping FOB and inspection '
                              'clauses [6Fz712e3oWc @ 00:25:46]. The No Bid List is a 10-20K item snapshot '
                              'with some lines already awarded or cancelled, and quoting 10 cents instead '
                              'of $10 still obligates you if the award is made [6Fz712e3oWc @ 00:30:01]. '
                              'Carrie lays out the Part 15 tripwires: "late is late," an accepted late '
                              'proposal stays protestable, and a withdrawn proposal cannot be resubmitted '
                              '[Tj7x3UDuOSE @ 00:22:09]. Defective pricing brings price adjustments, fees, '
                              'interest, penalties, CPARS damage, and possible criminal or civil exposure '
                              '[Tj7x3UDuOSE @ 00:50:04]. Neil McDonnell adds a research bottleneck. FPDS '
                              'holds summary data only, with no PWS or scope documents, so the work '
                              'statement has to come from SAM, the CO, or FOIA [0cGdQvymmvY @ 00:10:10]. '
                              'Johnny Clark warns that CPAs are "general practitioners," so the books '
                              'behind a cost buildup need a GovCon specialist rather than a generalist '
                              '[EBQwejU6UUQ @ 00:31:06].'],
               'table': {'caption': 'Practitioner-reported pricing failures and the economics check behind '
                                    'each',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Bidding off the latest modification instead of the base award',
                                   'Early pricing ran off by $4-5M, and once by a full $15M',
                                   'Scroll to modification 0; the base award totaled $1,686,566.88 over '
                                   'three years',
                                   'Fox Wade ([Z2ZeI5rayvk @ 00:02:50])'],
                                  ['Guessing the contract value when the agency withholds it',
                                   'Assumed an Army requirement was worth at least $250K',
                                   'Award came in around $35K; email the POC for incumbent value every '
                                   'time',
                                   'Kizzy Parks ([L0SM3XAM3IE @ 00:05:28])'],
                                  ['Underbidding fringe and payroll burden on labor proposals',
                                   'Bidding 5% when payroll taxes alone run about 10%',
                                   'Fringe runs about 30%, and leave alone is 200 of 2,080 hours',
                                   'Solvability ([lOumu-Dk0Jw @ 00:13:16])'],
                                  ['Keeping a single salary-and-wages line in the books',
                                   'One $300,000 wages line is the classic DCAA fail test',
                                   'Labor distribution must tie to gross payroll with a timesheet audit '
                                   'trail',
                                   'Solvability ([EBQwejU6UUQ @ 00:17:14])'],
                                  ['Dumping a shared cost entirely onto one job',
                                   'A $2,000 test-equipment invoice was shared across four projects',
                                   'One-quarter usage suggests a $500 allocation to investigate, not an '
                                   'equal split',
                                   'Win Government Contracts with GovSuccess ([i7_rrrRpotk @ 00:02:29])'],
                                  ['Quoting item cost plus markup and nothing else',
                                   'A $10 flashlight priced as $10 plus 15% on a DLA quote',
                                   'Landed cost reaches $13 after tariffs, logistics, packaging and '
                                   'shipping',
                                   'myContractScout ([6Fz712e3oWc @ 00:24:31])'],
                                  ['Fat-fingering a unit price on a DLA RFQ',
                                   'Quoting 10 cents instead of $10 on a line item',
                                   'You are still obligated to perform at that price if the award is made',
                                   'myContractScout ([6Fz712e3oWc @ 00:30:01])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Bid Pricing Gate',
                           'body': 'Clear all four checks before any number leaves the building.',
                           'items': ['Pull modification 0 and the old solicitation before pricing a '
                                     'recompete, because the latest action and changed scope both distort '
                                     'the number [Fox Wade — Z2ZeI5rayvk @ 00:02:50].',
                                     'Email the POC for incumbent name, contract number and contract value '
                                     'on every sources sought, RFI, RFQ or solicitation, and never assume '
                                     'a withheld value [Kizzy Parks — L0SM3XAM3IE @ 00:00:43].',
                                     'Run the wrap calculator before bidding: a $75 bill rate caps pay at '
                                     'about $48, and G&A near 60% is out of the game [Solvability — '
                                     'lOumu-Dk0Jw @ 00:42:07].',
                                     'Verify the solicitation is still open, lock the supplier, and price '
                                     'freight, tariffs and FOB terms before quoting DLA [myContractScout — '
                                     '6Fz712e3oWc @ 00:19:22].']}}],
 'pull_quote': '"While it\'s great to know the price, the evaluation criteria always rules." — attributed '
               'to Kizzy Parks (L0SM3XAM3IE @ 00:02:44).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Email the POC on every sources sought, RFI, RFQ or solicitation asking whether '
                      'there is an incumbent, plus its name, contract number and contract value [Kizzy '
                      'Parks — L0SM3XAM3IE @ 00:00:24].',
                      'Paste the incumbent contract number into FPDS, sort by date signed, and scroll to '
                      'modification 0 to read the base award value, term and set-aside status [Fox Wade — '
                      'Z2ZeI5rayvk @ 00:02:50].',
                      'Filter USAspending by fiscal year and state, download the results, and build an '
                      'Excel pivot table to sort award fields [Eric Coffie — Hr_U9z1xK2g @ 00:00:59].',
                      'Pull incumbent and competitor schedules, labor rates and labor category '
                      'descriptions from GSA eLibrary to calibrate your own rates [Kizzy Parks — '
                      'L0SM3XAM3IE @ 00:13:57].',
                      'Build rates in FOG order (fringe, overhead, G&A) and push gray-area costs into '
                      'overhead instead of G&A to keep the G&A rate competitive [Solvability — lOumu-Dk0Jw '
                      '@ 00:27:28].',
                      'Keep a five-field cost-support sheet and have the numbers, the operational benefit '
                      'and the contract terms each explained by their owners, resolving disagreements '
                      'before proposal or billing [Win Government Contracts with GovSuccess — i7_rrrRpotk '
                      '@ 00:03:47].'],
 'statutory_citations': [{'title': 'Solvability — Direct & Indirect Costs in Federal Contracting: Fringe, '
                                   'Overhead, G&A and Wrap Rates [00:40:51]',
                          'url': 'https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=2451s',
                          'relevance': 'Primary practitioner testimony on wrap-rate multipliers, '
                                       'indirect-rate buildup and rates too high to win.'},
                         {'title': 'Kizzy Parks — How To Find Price Paid For Past Contracts | Learn About '
                                   'Pricing in Gov Con [00:02:44]',
                          'url': 'https://www.youtube.com/watch?v=L0SM3XAM3IE&t=164s',
                          'relevance': 'Primary practitioner testimony on reading past prices against '
                                       'evaluation criteria and the Army withheld-value miss.'},
                         {'title': 'How To Sell To & Win Federal Government Contracts — 2024:  FAR Part 15 '
                                   '- Contracting by Negotiation [00:20:51]',
                          'url': 'https://www.youtube.com/watch?v=Tj7x3UDuOSE&t=1251s',
                          'relevance': 'Primary practitioner testimony on certified cost or pricing data '
                                       'thresholds, profit caps and defective pricing exposure.'},
                         {'title': 'Fox Wade — How to find what the government paid on previously awarded '
                                   'contracts! #govcon #governmentcontracting [00:02:50]',
                          'url': 'https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=170s',
                          'relevance': 'Primary practitioner testimony on pulling the modification 0 base '
                                       'award after multimillion-dollar pricing misses.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'i7_rrrRpotk',
                       'title': 'FAR Part 31 (Simplified) | Support the Cost Before You Claim It',
                       'channel': 'Win Government Contracts with GovSuccess',
                       'author': 'Win Government Contracts with GovSuccess',
                       'text': 'Under FAR 31.201-3, spending the money does not create a presumption that '
                               'the amount is reasonable.',
                       'tip': 'Under FAR 31.201-3, spending the money does not create a presumption that '
                              'the amount is reasonable.',
                       'timestamp': 90,
                       'timestamp_seconds': 90,
                       'timestamp_label': '[00:01:30]',
                       'url': 'https://www.youtube.com/watch?v=i7_rrrRpotk&t=90s',
                       'markdown': '[00:01:30](https://www.youtube.com/watch?v=i7_rrrRpotk&t=90s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EBQwejU6UUQ',
                       'title': 'GovCon Accounting Explained: How to Price, Bill and Win Contracts',
                       'channel': 'Solvability',
                       'author': 'Solvability',
                       'text': 'The idea is to enter the time once and everything after it agrees.',
                       'tip': 'The idea is to enter the time once and everything after it agrees.',
                       'timestamp': 1768,
                       'timestamp_seconds': 1768,
                       'timestamp_label': '[00:29:28]',
                       'url': 'https://www.youtube.com/watch?v=EBQwejU6UUQ&t=1768s',
                       'markdown': '[00:29:28](https://www.youtube.com/watch?v=EBQwejU6UUQ&t=1768s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GrYP5KyxBho',
                       'title': 'How to Find Past Prices for Better Gov Contract Bids (Using Free '
                                'Resources)',
                       'channel': 'FedAccess',
                       'author': 'FedAccess',
                       'text': 'Every solicitation includes an email address where you can submit '
                               'questions directly to the government.',
                       'tip': 'Every solicitation includes an email address where you can submit questions '
                              'directly to the government.',
                       'timestamp': 471,
                       'timestamp_seconds': 471,
                       'timestamp_label': '[00:07:51]',
                       'url': 'https://www.youtube.com/watch?v=GrYP5KyxBho&t=471s',
                       'markdown': '[00:07:51](https://www.youtube.com/watch?v=GrYP5KyxBho&t=471s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Hr_U9z1xK2g',
                       'title': 'How to get AWARD Data from USA Spending?',
                       'channel': 'Eric Coffie',
                       'author': 'Eric Coffie',
                       'text': 'Pull the award data into Excel, build a pivot table, and sort the fields.',
                       'tip': 'Pull the award data into Excel, build a pivot table, and sort the fields.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=Hr_U9z1xK2g&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=Hr_U9z1xK2g&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z2ZeI5rayvk',
                       'title': 'How to find what the government paid on previously awarded contracts! '
                                '#govcon #governmentcontracting',
                       'channel': 'Fox Wade',
                       'author': 'Fox Wade',
                       'text': "It's free public data, and if you're not ready to prime, contact the "
                               'incumbent to team.',
                       'tip': "It's free public data, and if you're not ready to prime, contact the "
                              'incumbent to team.',
                       'timestamp': 332,
                       'timestamp_seconds': 332,
                       'timestamp_label': '[00:05:32]',
                       'url': 'https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=332s',
                       'markdown': '[00:05:32](https://www.youtube.com/watch?v=Z2ZeI5rayvk&t=332s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eEBn_eN0py8',
                       'title': 'FedBiz Find | Government Contracting | Award History & New Opportunities',
                       'channel': 'FedBiz Access',
                       'author': 'FedBiz Access',
                       'text': 'Approximately 90% of service contracts expire within two to three years '
                               'but are renewable, with about 245,000 renewing annually.',
                       'tip': 'Approximately 90% of service contracts expire within two to three years but '
                              'are renewable, with about 245,000 renewing annually.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=eEBn_eN0py8&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=eEBn_eN0py8&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g-mx_oRCj0k',
                       'title': 'Searching Federal Procurement Data System (FPDS) for Government Contracts',
                       'channel': 'Neil McDonnell',
                       'author': 'Neil McDonnell',
                       'text': 'If you ever want to share this with somebody, just copy the URL, send it '
                               'to them because the query is in the URL.',
                       'tip': 'If you ever want to share this with somebody, just copy the URL, send it to '
                              'them because the query is in the URL.',
                       'timestamp': 1684,
                       'timestamp_seconds': 1684,
                       'timestamp_label': '[00:28:04]',
                       'url': 'https://www.youtube.com/watch?v=g-mx_oRCj0k&t=1684s',
                       'markdown': '[00:28:04](https://www.youtube.com/watch?v=g-mx_oRCj0k&t=1684s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0cGdQvymmvY',
                       'title': 'Introduction to the Federal Procurement Data System (FPDS) - Part 1',
                       'channel': 'Neil McDonnell',
                       'author': 'Neil McDonnell',
                       'text': "Don't ever do PDF because there's no value in PDF.",
                       'tip': "Don't ever do PDF because there's no value in PDF.",
                       'timestamp': 1702,
                       'timestamp_seconds': 1702,
                       'timestamp_label': '[00:28:22]',
                       'url': 'https://www.youtube.com/watch?v=0cGdQvymmvY&t=1702s',
                       'markdown': '[00:28:22](https://www.youtube.com/watch?v=0cGdQvymmvY&t=1702s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L0SM3XAM3IE',
                       'title': 'How To Find Price Paid For Past Contracts | Learn About Pricing in Gov '
                                'Con',
                       'channel': 'Kizzy Parks',
                       'author': 'Kizzy Parks',
                       'text': "While it's great to know the price, the evaluation criteria always rules.",
                       'tip': "While it's great to know the price, the evaluation criteria always rules.",
                       'timestamp': 164,
                       'timestamp_seconds': 164,
                       'timestamp_label': '[00:02:44]',
                       'url': 'https://www.youtube.com/watch?v=L0SM3XAM3IE&t=164s',
                       'markdown': '[00:02:44](https://www.youtube.com/watch?v=L0SM3XAM3IE&t=164s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L0SM3XAM3IE',
                       'title': 'How To Find Price Paid For Past Contracts | Learn About Pricing in Gov '
                                'Con',
                       'channel': 'Kizzy Parks',
                       'author': 'Kizzy Parks',
                       'text': "If you're not willing to play the game with the evaluation criteria, then "
                               "don't bid, don't bid at all.",
                       'tip': "If you're not willing to play the game with the evaluation criteria, then "
                              "don't bid, don't bid at all.",
                       'timestamp': 774,
                       'timestamp_seconds': 774,
                       'timestamp_label': '[00:12:54]',
                       'url': 'https://www.youtube.com/watch?v=L0SM3XAM3IE&t=774s',
                       'markdown': '[00:12:54](https://www.youtube.com/watch?v=L0SM3XAM3IE&t=774s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '17foq325L5w',
                       'title': 'Searching Federal Procurement Data System (FPDS) for Government Contracts',
                       'channel': 'Neil McDonnell',
                       'author': 'Neil McDonnell',
                       'text': 'FPDS is 80% of your activity, or it should be.',
                       'tip': 'FPDS is 80% of your activity, or it should be.',
                       'timestamp': 682,
                       'timestamp_seconds': 682,
                       'timestamp_label': '[00:11:22]',
                       'url': 'https://www.youtube.com/watch?v=17foq325L5w&t=682s',
                       'markdown': '[00:11:22](https://www.youtube.com/watch?v=17foq325L5w&t=682s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NiWdxgnr3xo',
                       'title': 'Government Contractor’s Guide to USASpending.gov [2025 Tutorial]',
                       'channel': 'SamSearch - AI for Government Contracting',
                       'author': 'SamSearch - AI for Government Contracting',
                       'text': 'The key to having a successful government contracting business is being '
                               'datadriven and following the money.',
                       'tip': 'The key to having a successful government contracting business is being '
                              'datadriven and following the money.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=NiWdxgnr3xo&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=NiWdxgnr3xo&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YR_aPfXedtA',
                       'title': 'How to Find WOSB Set Asides Using FPDS | Government Contracting',
                       'channel': 'Neil McDonnell',
                       'author': 'Neil McDonnell',
                       'text': "When I'm doing searches, I could care less about anything below a million "
                               'dollars at the moment.',
                       'tip': "When I'm doing searches, I could care less about anything below a million "
                              'dollars at the moment.',
                       'timestamp': 337,
                       'timestamp_seconds': 337,
                       'timestamp_label': '[00:05:37]',
                       'url': 'https://www.youtube.com/watch?v=YR_aPfXedtA&t=337s',
                       'markdown': '[00:05:37](https://www.youtube.com/watch?v=YR_aPfXedtA&t=337s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SpRIyXgvkg0',
                       'title': 'Breakdown of FAR Part 12 & 15 | Selling Commercial Items or '
                                'Non-Commercial Items to the Government',
                       'channel': 'US Federal Contractor Registration',
                       'author': 'US Federal Contractor Registration',
                       'text': "For commercial items, it's a different story, it is really what the market "
                               'will bear.',
                       'tip': "For commercial items, it's a different story, it is really what the market "
                              'will bear.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=SpRIyXgvkg0&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=SpRIyXgvkg0&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Tj7x3UDuOSE',
                       'title': '2024:  FAR Part 15 - Contracting by Negotiation',
                       'channel': 'How To Sell To & Win Federal Government Contracts',
                       'author': 'How To Sell To & Win Federal Government Contracts',
                       'text': 'You must submit on time; late is late.',
                       'tip': 'You must submit on time; late is late.',
                       'timestamp': 1329,
                       'timestamp_seconds': 1329,
                       'timestamp_label': '[00:22:09]',
                       'url': 'https://www.youtube.com/watch?v=Tj7x3UDuOSE&t=1329s',
                       'markdown': '[00:22:09](https://www.youtube.com/watch?v=Tj7x3UDuOSE&t=1329s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lOumu-Dk0Jw',
                       'title': 'Direct & Indirect Costs in Federal Contracting: Fringe, Overhead, G&A and '
                                'Wrap Rates',
                       'channel': 'Solvability',
                       'author': 'Solvability',
                       'text': "So, if it's 60%, you're never going to succeed in government contracting "
                               'because your costs are too high.',
                       'tip': "So, if it's 60%, you're never going to succeed in government contracting "
                              'because your costs are too high.',
                       'timestamp': 215,
                       'timestamp_seconds': 215,
                       'timestamp_label': '[00:03:35]',
                       'url': 'https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=215s',
                       'markdown': '[00:03:35](https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=215s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lOumu-Dk0Jw',
                       'title': 'Direct & Indirect Costs in Federal Contracting: Fringe, Overhead, G&A and '
                                'Wrap Rates',
                       'channel': 'Solvability',
                       'author': 'Solvability',
                       'text': 'Mathematically, if you have a choice, you want to put something in '
                               "overhead instead of G&A or your G&A rate's going to go through the roof "
                               "and you won't win any business.",
                       'tip': 'Mathematically, if you have a choice, you want to put something in overhead '
                              "instead of G&A or your G&A rate's going to go through the roof and you "
                              "won't win any business.",
                       'timestamp': 1648,
                       'timestamp_seconds': 1648,
                       'timestamp_label': '[00:27:28]',
                       'url': 'https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=1648s',
                       'markdown': '[00:27:28](https://www.youtube.com/watch?v=lOumu-Dk0Jw&t=1648s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6Fz712e3oWc',
                       'title': 'Government Contracting: Demand in DLA DIBBS',
                       'channel': 'myContractScout',
                       'author': 'myContractScout',
                       'text': 'So make sure you count all the costs, not just the cost of the item and '
                               'your profit margin.',
                       'tip': 'So make sure you count all the costs, not just the cost of the item and '
                              'your profit margin.',
                       'timestamp': 1526,
                       'timestamp_seconds': 1526,
                       'timestamp_label': '[00:25:26]',
                       'url': 'https://www.youtube.com/watch?v=6Fz712e3oWc&t=1526s',
                       'markdown': '[00:25:26](https://www.youtube.com/watch?v=6Fz712e3oWc&t=1526s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
