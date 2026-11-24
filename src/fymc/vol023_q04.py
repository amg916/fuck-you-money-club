from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'wi-nri-calculations-working-the-numbers',
 'question_prompt': 'How do I calculate working interest and net revenue interest for owners, co-tenants '
                    'and operators, including in pooled units?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Working the Numbers: WI and NRI Calculations',
 'subtitle': 'Three-step NRI calculation, gross working interest, operator NRI after royalties and '
             'overrides, AAPL study-guide situations with NPRIs, pooled-unit acreage problems, and '
             'undivided co-tenant interests with different royalties',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Landmen and mineral owners working these numbers agree on one spine: before a lease '
                      'the mineral owner holds 100% working interest and 100% net revenue interest; after '
                      'the lease the lessee takes 100% of the WI and the lessor keeps only the royalty '
                      'fraction. From there every division-order decimal is built by multiplication: '
                      'royalty times mineral interest times tract acres over unit acres. Matt Sands turns '
                      '16 net acres in a 1,280-acre DSU at a 15% royalty into .001875 and a roughly $937 '
                      'three-month check estimate. Alyce Hoge and the Land Training drills show 1/8 '
                      'leaving the operator 0.875 and 3/16 leaving 0.8125, with overrides and NPRIs carved '
                      "out further. UHD's instructor insists on a lease-level check-and-balance, while "
                      'Land Training leans on Excel fill-down and summing back to the tract share.',
 'key_metrics': [{'label': 'Owner NRI in Bakken DSU example',
                  'metric': 'Owner NRI in Bakken DSU example',
                  'value': '.001875 (0.1875% of oil and gas sold)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': '16 net mineral acres divided by a 1,280-acre drilling spacing unit, '
                             'multiplied by a 15% lease royalty; this decimal must match the division '
                             'order.',
                  'source': 'Matt Sands ([Yy7az5T7_vs @ 00:12:22])'},
                 {'label': 'Estimated three-month oil royalty',
                  'metric': 'Estimated three-month oil royalty',
                  'value': 'About $937',
                  'confidence': 'attributed_practitioner_claim',
                  'context': '10,000 barrels in the first three months, based on averaging nearby Bakken '
                             'wells, at $50 per barrel times the .001875 NRI.',
                  'source': 'Matt Sands ([Yy7az5T7_vs @ 00:15:38])'},
                 {'label': 'Going-rate well cost carried by the lessee',
                  'metric': 'Going-rate well cost carried by the lessee',
                  'value': 'About $6 million per well',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Hoge's justification for the grand bargain: the oil company pays for a dry "
                             'hole, the royalty owner pays nothing.',
                  'source': 'Land Training www.landtraining.net ([eZU5hvGcngg @ 00:05:34])'},
                 {'label': 'Sunrise lease-level take and unit NRI',
                  'metric': 'Sunrise lease-level take and unit NRI',
                  'value': '82.5 cents per dollar; 0.20625 unit NRI',
                  'confidence': 'attributed_practitioner_claim',
                  'context': '100% WI lease burdened by a 12.5% royalty and 5% geologist override, then '
                             'pooled as 80 acres into a 320-acre unit.',
                  'source': 'UHD Continuing and Professional Education ([oHKF06pFkh0 @ 00:05:22])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ["The cleanest consensus across the Land Training sessions and Alyce Hoge's "
                              'lease breakdown is the grand bargain. Before any oil and gas lease, the '
                              'mineral owner holds 100% of the working interest and 100% of the net '
                              'revenue interest, meaning they pay every drilling bill and keep every '
                              'barrel, while the oil company owns 0% of both. Sign the lease and the '
                              'lessor hands 100% of the working interest to the lessee, keeping only a '
                              'royalty fraction in return [eZU5hvGcngg @ 00:03:47]. The Land Training '
                              'instructor runs the same trade through the Harry Truman fact pattern: '
                              'Hiroshima Drilling leases all 160 acres for a 1/8 royalty, leaving Truman '
                              'with 0% working interest and a 0.125 net revenue interest, while the '
                              'company holds 100% working interest and a 0.875 net revenue interest '
                              '[PjGnR-YfLy4 @ 00:07:07]. Why would an owner accept that split? Every '
                              'speaker answers with risk. Hoge prices a well at about $6 million and '
                              "stresses that a dry hole is the company's loss alone; the royalty owner "
                              'pays nothing [eZU5hvGcngg @ 00:05:34]. A second Land Training walkthrough '
                              'puts the cost at a million dollars and up, climbing with every rework, and '
                              'calls drilling cost prohibitive for most landowners [yWZaJ-ItXKQ @ '
                              '00:02:51]. The lessor trades cost exposure for a clean, cost-free slice of '
                              'production.',
                              'The second point of agreement is that pooling shrinks the royalty by '
                              'acreage, and everyone uses the same multiplication. The Land Training '
                              'instructor explains that state conservation agencies, the Texas Railroad '
                              "Commission, Louisiana's Department of Conservation and the Oklahoma "
                              'Corporation Commission, cap wells per acreage, so owners without a wellbore '
                              'on their tract still share production in proportion to the acres they '
                              'contribute [WPeA0rs7SLA @ 00:04:17]. The formula: royalty interest times '
                              'tract acres divided by unit acres. Hoge runs a lessor with 160 acres in a '
                              '640-acre gas unit at 3/16 and lands on 0.046875, warning that these '
                              'decimals usually run out to eight decimal places [eZU5hvGcngg @ 00:13:51]. '
                              "Matt Sands, coming at it from the mineral owner's chair, builds the "
                              'identical equation from three inputs that take under five minutes once '
                              'gathered: net mineral acres, drilling spacing unit size and lease royalty '
                              'rate [Yy7az5T7_vs @ 00:01:35]. Another Land Training walkthrough lands on '
                              '1/32, or 0.03125, for 160 of 640 acres at 1/8 [yWZaJ-ItXKQ @ 00:09:51]. '
                              'Practitioners also agree on where the numbers live: working interest on the '
                              'joint interest billing deck, net revenue interest on the division order pay '
                              "sheet. If the operator's decimal disagrees with the owner's math, the owner "
                              'digs in.',
                              "Third, the operator's net revenue interest is always gross working interest "
                              "minus burdens, and overrides come off the company's side, never the "
                              "lessor's. The UHD instructor calls net revenue interest the most important "
                              'number an oil company has, the take-home pay after deductions, and lays out '
                              'the order: calculate gross working interest first, calculate every burden '
                              'second, then subtract [oHKF06pFkh0 @ 00:00:36]. The Land Training '
                              "instructor applies it to Adam's 1/8 lease with a 3% override assigned to "
                              'the geologist: the override is carved out of the working interest, so the '
                              "company's 0.875 drops to 0.845 and the geologist holds a 0.03 decimal that "
                              'pays nothing if the well is dry [B5fBIyi1-hw @ 00:04:40]. Non-participating '
                              'royalties hit the other side of the ledger. When Alpha conveys 2.5% of the '
                              'oil and gas produced and saved to Bravo and then leases to Charlie at 1/8, '
                              "Alpha's 12.5% shrinks to 10%, Bravo keeps 2.5%, and Charlie still holds "
                              "87.5% [JVbDAxk_YTU @ 00:04:49]. The instructor flags 'produced and saved' "
                              'as the buzzwords that separate a royalty conveyance from a mineral '
                              'conveyance, and notes that nobody takes a lease from the NPRI holder '
                              '[HkEK5QVZAJ0 @ 00:01:14]. Whoever granted the burden absorbs it: the lessee '
                              'for the override, the mineral owner for the NPRI.'],
               'table': {'caption': 'Where the practitioners line up on WI and NRI fundamentals',
                         'headers': ['Consensus Point',
                                     'Practitioner Position',
                                     'Operator Use',
                                     'Expert Source'],
                         'rows': [['Pre-lease ownership split between mineral owner and company',
                                   'Mineral owner holds 100% WI and 100% NRI; the company holds zero of '
                                   'both',
                                   'Treat any unleased owner as paying every drilling bill on their own',
                                   'Land Training www.landtraining.net ([eZU5hvGcngg @ 00:02:41])'],
                                  ['Post-lease grand bargain transfers the full working interest to lessee',
                                   'Lessor keeps 0% WI plus royalty; lessee takes 100% WI and 0.875 NRI at '
                                   '1/8',
                                   'Start every operator NRI from 100% minus the stated lease royalty '
                                   'fraction',
                                   'Land Training www.landtraining.net ([PjGnR-YfLy4 @ 00:07:07])'],
                                  ["Royalty size directly cuts the operator's net revenue interest",
                                   '1/8 leaves 0.875, 3/16 leaves 0.8125, and 1/4 leaves 0.75 to the '
                                   'company',
                                   'Hoge says operators typically want at least a 78% NRI for the venture '
                                   'to pay',
                                   'Land Training www.landtraining.net ([eZU5hvGcngg @ 00:07:46])'],
                                  ['Pooled unit formula for a single mineral owner in a unit',
                                   'Royalty interest times tract acres divided by unit acres equals the '
                                   "owner's NRI",
                                   "Farmer Brown's 160 acres in a 640-acre unit at 1/8 yields 0.03125",
                                   'Land Training www.landtraining.net ([WPeA0rs7SLA @ 00:08:13])'],
                                  ['Operator NRI equals gross working interest minus every listed burden',
                                   'Calculate gross first, list every burden second, then subtract down to '
                                   'the net',
                                   'Sunrise keeps 82.5 cents per lease dollar after a 12.5% royalty and 5% '
                                   'override',
                                   'UHD Continuing and Professional Education ([oHKF06pFkh0 @ 00:05:22])'],
                                  ["Division order decimal must match the owner's own independent math",
                                   "Sands says the decimal on the division order is the owner's net "
                                   'revenue interest',
                                   'If numbers differ, recheck inputs, then challenge the operator who '
                                   'sent the order',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:12:07])'],
                                  ['Working interest and net revenue interest live on different decks',
                                   'WI appears on the joint interest billing deck; NRI on the division '
                                   'order pay sheet',
                                   'Pull the JIB deck for cost shares and the pay deck for revenue shares',
                                   'Land Training www.landtraining.net ([PjGnR-YfLy4 @ 00:08:35])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Matt Sands teaches the owner-side workflow as three inputs and one '
                              'equation. Net mineral acres come from the legal description: gross acres '
                              'times decimal ownership, so a 1/40 interest, 2.5%, in a 640-acre section '
                              'yields 16 net mineral acres; if the decimal is unknown, a landman or '
                              "lawyer's title search running the chain of transfers in county records "
                              'supplies it [Yy7az5T7_vs @ 00:06:19]. Drilling spacing unit size comes off '
                              "the state oil and gas commission's map; in North Dakota, Sands uses the "
                              "Industrial Commission's GIS map server, turns on the spacing-unit layer, "
                              'finds the section and reads a 1,280-acre, two-section DSU for a horizontal '
                              'Bakken well. The royalty rate sits on page one of the lease, in the clause '
                              "delivering the lessor's share free of cost into the tanks or pipeline, here "
                              '15%, pulled from the county clerk and recorder if the owner has no copy '
                              '[Yy7az5T7_vs @ 00:10:11]. Then 16 divided by 1,280 times 0.15 equals '
                              '.001875, the decimal that must match the division order [Yy7az5T7_vs @ '
                              '00:12:22]. Alyce Hoge confirms operators build the same figure, net acres '
                              'over unit acres times the royalty fraction, which is how those crazy '
                              'eight-place decimals appear on the pay deck [eZU5hvGcngg @ 00:12:21].',
                              'Once ownership splits, the formula gains a factor. The Land Training '
                              "instructor's spacing-unit formula for co-tenants is royalty interest times "
                              'mineral interest times tract acres divided by unit acres, and they keep '
                              'mineral interest as its own term so errors stay traceable [wUqopw4hh2o @ '
                              '00:04:21]. The lease itself only shows 160 acres; the actual mineral '
                              "interest comes from the lease purchase report built off the landman's chain "
                              'of title, so assuming 100% from the lease face is wrong. In the Brady heirs '
                              'problem, four children each hold 25% undivided in 160 acres inside a '
                              '320-acre unit: Greg at 1/4 royalty nets 0.03125, Peter at 3/16 nets '
                              '0.0234375, and Bobby and Cindy at 1/8 net 0.015625 each. The instructor '
                              'builds it in Excel, typing the formula once with an equals sign, then '
                              'dragging the fill handle when the skinny plus sign appears to populate '
                              'every row [wUqopw4hh2o @ 00:10:21]. The single-owner drills stay fast: '
                              "Franklin Roosevelt's 20 acres in an 80-acre unit at 3/16 come to 0.046875 "
                              "[kw0rYmoBLXU @ 00:01:34], while Budro's 160 acres in a 160-acre unit keep "
                              'the full 0.1875 because the tract fills the unit. Ten Marcellus acres at '
                              '1/5 in an 80-acre unit work out to 0.20 times 10 over 80, or 0.025 '
                              '[kC2dYFP0U0g @ 00:01:04].',
                              "Burdens get the same discipline. The UHD instructor's Sunrise Oil and Gas "
                              "example: 100% gross working interest in Homer Murray's 80-acre lease, 12.5% "
                              'royalty, 5% override to the geologist, so Sunrise pockets 82.5 cents on '
                              'every dollar [oHKF06pFkh0 @ 00:05:22]. Pool the 80 acres into a 320-acre '
                              "unit and Sunrise's unit gross becomes 0.25, Homer's unit royalty 0.03125, "
                              "the override 0.0125, because it is tied to Homer's acres, leaving a 0.20625 "
                              'net. The check: 0.825 times 0.25 must equal 0.20625, and it does '
                              "[oHKF06pFkh0 @ 00:09:36]. The UHD instructor's caution: if Sunrise brings "
                              'five leases with different burdens, run the check lease by lease, never '
                              'commingled, or the totals will not reconcile. Always run it, the instructor '
                              'says, even when you think you aced the math. Land Training checks the '
                              'co-tenant split the same way, summing royalty and lessee shares back to '
                              "each owner's mineral interest times the unit factor, as with Greg's 0.5 "
                              'times 0.25 equaling 0.125 [n2pg2-Q06P8 @ 00:10:23]. On paper, the landman '
                              "writes the full fraction, 1/8, 3/16 or 1/6, into each co-tenant's lease, "
                              'never the reduced decimal; the proportionate reduction clause then lets the '
                              "division order drop Greg's 1/8 to 0.0625 based on what Greg actually owns "
                              '[PNLVi6Ee0KM @ 00:09:16].'],
               'table': {'caption': 'Worked numbers the practitioners ran on camera',
                         'headers': ['Scenario',
                                     'Inputs Stated',
                                     'Calculation and Result',
                                     'Expert Source'],
                         'rows': [['Bakken owner holding a single section inside a two-section DSU',
                                   '16 net mineral acres, 1,280-acre DSU, and a 15% lease royalty rate',
                                   '16 / 1,280 x 0.15 = .001875 decimal expected on the division order',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:12:22])'],
                                  ['Three-month royalty check estimate for a new Bakken well',
                                   '10,000 barrels in the first three months at a $50 Bakken price',
                                   '10,000 x $50 x .001875 = about $937 in oil royalty only',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:15:38])'],
                                  ['Operator NRI after a 1/8 royalty and a geologist override',
                                   "Adam's 1/8 lease plus a 3% override assigned to the geologist",
                                   '0.875 minus 0.03 leaves a 0.845 operator net revenue interest',
                                   'Land Training www.landtraining.net ([B5fBIyi1-hw @ 00:05:00])'],
                                  ["NPRI carved out of the mineral owner's lease royalty share",
                                   'Alpha conveys 2.5% produced and saved, then leases to Charlie at 1/8',
                                   'Alpha 10% NRI, Bravo 2.5% NPRI, Charlie as lessee 87.5% NRI',
                                   'Land Training www.landtraining.net ([JVbDAxk_YTU @ 00:04:49])'],
                                  ['Pooled unit carrying both a lease royalty and a tied override',
                                   'Sunrise 80 acres pooled into a 320-acre unit, 12.5% royalty, 5% ORRI',
                                   '0.25 minus 0.03125 minus 0.0125 equals 0.20625; check 0.825 x 0.25',
                                   'UHD Continuing and Professional Education ([oHKF06pFkh0 @ 00:07:43])'],
                                  ['Co-tenants holding different royalties inside one spacing unit',
                                   'Four heirs at 25% each in 160 acres within a 320-acre unit',
                                   'Greg 0.03125, Peter 0.0234375, Bobby and Cindy 0.015625 each',
                                   'Land Training www.landtraining.net ([wUqopw4hh2o @ 00:10:21])'],
                                  ['Small tract pooled into a Marcellus drilling and spacing unit',
                                   '10 acres leased at a 1/5 royalty inside an 80-acre unit',
                                   '0.20 x 10 / 80 = 0.025 net revenue interest for the owner',
                                   'Land Training www.landtraining.net ([kC2dYFP0U0g @ 00:01:04])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Shortcuts and tells the practitioners lean on',
                           'body': 'Small habits that keep a division-order decimal honest before anyone '
                                   'signs or cashes a check.',
                           'items': ["Watch for 'produced and saved' in any conveyance: it signals a "
                                     'royalty, not minerals, so the grantee is an NPRI holder and the '
                                     "mineral owner's NRI shrinks once a lease is signed [Land Training "
                                     'www.landtraining.net — JVbDAxk_YTU @ 00:01:03].',
                                     'Do not answer 9.5% when no lease exists yet: David simply owns 100% '
                                     "of the minerals subject to Charlie's 3% NPRI until a lease royalty "
                                     'is set [Land Training www.landtraining.net — HkEK5QVZAJ0 @ '
                                     '00:04:30].',
                                     'Expect the realized price to trail the benchmark: Sands cites WTI at '
                                     '$60 while Bakken barrels bring $50 because of the price differential '
                                     'for transport and processing, and state production data can lag a '
                                     'couple of months [Matt Sands — Yy7az5T7_vs @ 00:16:47].',
                                     'Keep mineral interest as its own column in Excel instead of folding '
                                     'it into the acres, so a bad input is visible and traceable when the '
                                     'decimal looks off [Land Training www.landtraining.net — wUqopw4hh2o '
                                     '@ 00:04:43].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pin down net mineral acres and true mineral interest',
                              'action': 'Multiply gross tract acres by the decimal ownership from the '
                                        'legal description or title work.',
                              'detail': 'Sands gets 16 net mineral acres from 2.5% of 640 acres and falls '
                                        "back on a landman's title search when the decimal is unknown "
                                        '[Matt Sands — Yy7az5T7_vs @ 00:06:19]; lease administration '
                                        'confirms the actual mineral interest on the lease purchase '
                                        'report, not the lease face [Land Training www.landtraining.net — '
                                        'wUqopw4hh2o @ 00:02:40].'},
                             {'step': 2,
                              'title': 'Pull unit size and the lease royalty rate',
                              'action': 'Read the DSU from the state commission GIS layer and the royalty '
                                        'from page one of the lease.',
                              'detail': 'Sands turns on the spacing-unit layer on the North Dakota map '
                                        'server, reads a 1,280-acre DSU, and takes the 15% royalty from '
                                        'the delivery clause, pulling the lease from the county clerk and '
                                        'recorder if needed [Matt Sands — Yy7az5T7_vs @ 00:10:11].'},
                             {'step': 3,
                              'title': 'Run the formula, then subtract operator burdens',
                              'action': 'Multiply royalty x mineral interest x tract acres / unit acres; '
                                        'for the lessee, subtract every burden from gross WI.',
                              'detail': 'The co-tenant formula stacks royalty, mineral interest and '
                                        'tract-over-unit acres [Land Training www.landtraining.net — '
                                        "wUqopw4hh2o @ 00:00:42]; the operator's 0.875 less a 0.03 "
                                        'override leaves 0.845 [Land Training www.landtraining.net — '
                                        'B5fBIyi1-hw @ 00:05:21].'},
                             {'step': 4,
                              'title': 'Check, reconcile and challenge',
                              'action': 'Run a check-and-balance per lease, compare to the division order, '
                                        'and challenge mismatches.',
                              'detail': 'UHD checks 0.825 x 0.25 against the 0.20625 net and runs each '
                                        'lease separately when burdens differ [UHD Continuing and '
                                        'Professional Education — oHKF06pFkh0 @ 00:10:00]; Sands goes back '
                                        'to the operator who sent the division order when a verified '
                                        'calculation does not match [Matt Sands — Yy7az5T7_vs @ '
                                        '00:12:07].'}]},
              {'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Matt Sands and the Land Training instructors reach the same decimal through '
                              'different keystrokes, and the order matters when you hunt for an error. '
                              'Sands front-loads the ownership fraction: multiply gross acreage by your '
                              'decimal interest to get net mineral acres, so 2.5% of a 640-acre section '
                              'yields 16 NMA, then divide by the 1280-acre DSU and multiply by the 15% '
                              'royalty to land on .001875 [Yy7az5T7_vs @ 00:06:19]. The Land Training '
                              'co-tenant playbook refuses to pre-blend: royalty interest times mineral '
                              'interest times tract acres divided by unit acres. The instructor explains '
                              "that keeping the mineral interest as its own factor 'helps you know if "
                              "there's a mistake where you can go back and look at it' [wUqopw4hh2o @ "
                              '00:04:43]. For a 100% owner, the pooled-unit drills strip the formula down '
                              'to royalty times tract acres over unit acres. Problem 2 shows that a '
                              "160-acre tract in a 160-acre spacing unit leaves Boudreaux's 3/16 royalty "
                              'untouched at .1875 [VPrc0ax0-_o @ 00:01:26]. The operator takeaway is a '
                              "split by use case. Sands's collapsed NMA method is faster for a single "
                              'mineral owner reading one division order. The separated-factor method '
                              'scales better when four heirs, three royalty rates, and one spacing unit '
                              'all hit the same pay deck and you need to isolate which input broke the '
                              'number.',
                              'Sands pitches self-service. With net mineral acres, DSU size, and royalty '
                              "rate in hand, the math 'should take you less than five minutes,' and the "
                              "county clerk and recorder website is 'worth giving it a shot yourself "
                              "first' before paying a landman to pull the lease [Yy7az5T7_vs @ 00:09:40]. "
                              'Sands flips that advice for bigger positions. When multiple horizontal '
                              'wells are being drilled, Sands recommends a petroleum engineer for reserves '
                              "and a proper production forecast, plus a landman, because you 'could "
                              "actually own more or less' than you think [Yy7az5T7_vs @ 00:18:14]. The "
                              'Land Training instructor routes the grind into Excel instead. After '
                              "fumbling a hand calculation on Bobby's interest, the instructor says 'this "
                              "is why we want to use a spreadsheet,' builds royalty, mineral, tract, and "
                              "unit columns, and drags the formula down to fill every heir's row "
                              '[wUqopw4hh2o @ 00:08:19]. The UHD instructor adds a verification layer that '
                              "the other two playbooks do not mandate: 'always do a check and a balance "
                              "even if it feels cumbersome.' The check multiplies the lease-level take of "
                              '82.5 cents on the dollar by the unit gross working interest of 0.25 and '
                              'confirms it matches the gross-minus-burdens figure of .20625 [oHKF06pFkh0 @ '
                              '00:08:28]. That gives an operator three playbooks at three cost levels: '
                              'free solo math, spreadsheet automation, or hired professionals.',
                              'The practitioners also split on whose pocket a burden comes out of, and the '
                              'answer changes every decimal downstream. An overriding royalty rides on the '
                              'operator. In Situation #3, the oil company assigns a 3% override to its '
                              "geologist, and that override is 'carved out of the working interest.' The "
                              "company's 0.875 drops to a 0.845 net revenue interest, while Adam's .125 "
                              'royalty stays whole [B5fBIyi1-hw @ 00:02:56]. A non-participating royalty '
                              'rides on the mineral owner instead. In Situation #4, Alpha conveys 2.5% of '
                              'the oil and gas produced and saved to Bravo, then leases to Charlie at 1/8. '
                              "Alpha's 12.5% shrinks to a 10% net revenue interest, while Charlie the "
                              'lessee keeps the full 87.5% [JVbDAxk_YTU @ 00:03:42]. On the company side, '
                              'the royalty fraction itself is the lever, and Alyce Hoge walks it down the '
                              'board. A 1/8 royalty leaves the operator 87.5%, 3/16 leaves 81.25%, and a '
                              "quarter royalty leaves 75%, because the company's net revenue interest "
                              "'decreases the higher the royalty goes' [eZU5hvGcngg @ 00:10:32]. Read the "
                              'conveyance language before touching a calculator. Situation #4 teaches that '
                              "'produced and saved' signals a royalty conveyance rather than minerals, and "
                              "that one phrase decides which party's decimal absorbs the hit [JVbDAxk_YTU "
                              '@ 00:01:03].'],
               'table': {'caption': 'Side-by-side playbooks practitioners run on WI and NRI math',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Order of operations in the NRI formula',
                                   'Sands multiplies gross acres by decimal interest first, then divides '
                                   'NMA by DSU and multiplies by royalty',
                                   'Land Training keeps royalty, mineral interest, tract acres, and unit '
                                   'acres as separate factors to trace mistakes',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:06:19]); Land Training '
                                   'www.landtraining.net ([wUqopw4hh2o @ 00:04:43])'],
                                  ['Drilling cost that justifies the grand bargain',
                                   'Alyce Hoge puts the going rate at roughly $6 million per well, with '
                                   'the dry-hole risk carried by the company',
                                   'Companion lecture says a well can cost a million dollars and up '
                                   'easily, rising with every rework',
                                   'Land Training www.landtraining.net ([eZU5hvGcngg @ 00:05:34]); Land '
                                   'Training www.landtraining.net ([yWZaJ-ItXKQ @ 00:02:51])'],
                                  ['Who digs up the lease and title inputs',
                                   'Sands says try the county clerk and recorder website yourself before '
                                   'paying anyone',
                                   'For significant acreage with multiple horizontal wells, Sands hires a '
                                   'landman and a petroleum engineer forecast',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:09:40]); Matt Sands ([Yy7az5T7_vs @ '
                                   '00:18:14])'],
                                  ['Hand math versus spreadsheet execution',
                                   'Whiteboard multiplication for single-owner pooled problems such as '
                                   '0.1875 times 0.25 equals 0.046875',
                                   'Excel columns with the formula dragged down across every co-tenant row '
                                   'in the unit',
                                   'Land Training www.landtraining.net ([kw0rYmoBLXU @ 00:01:34]); Land '
                                   'Training www.landtraining.net ([wUqopw4hh2o @ 00:10:21])'],
                                  ['How to verify the final net figure',
                                   'UHD multiplies the lease-level take of 82.5 cents by unit gross '
                                   'working interest of 0.25',
                                   'Unit co-tenant lesson sums royalty and lessee shares against mineral '
                                   'interest times the unit factor',
                                   'UHD Continuing and Professional Education ([oHKF06pFkh0 @ 00:09:12]); '
                                   'Land Training www.landtraining.net ([n2pg2-Q06P8 @ 00:10:23])'],
                                  ['Who absorbs a carved-out burden',
                                   'Override is carved out of working interest, so the operator falls from '
                                   '0.875 to 0.845',
                                   'NPRI is paid out of lessor royalty, so Alpha drops from 12.5% to a 10% '
                                   'NRI',
                                   'Land Training www.landtraining.net ([B5fBIyi1-hw @ 00:02:56]); Land '
                                   'Training www.landtraining.net ([JVbDAxk_YTU @ 00:03:42])'],
                                  ['Which decimal belongs on which document',
                                   'Operator writes 1/8 in the lease and reduces it to 0.0625 on the '
                                   'division order',
                                   'Owner recomputes the decimal independently and challenges the operator '
                                   'when the division order mismatches',
                                   'Land Training www.landtraining.net ([PNLVi6Ee0KM @ 00:09:16]); Matt '
                                   'Sands ([Yy7az5T7_vs @ 00:12:22])']]}},
              {'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first failure mode is feeding the formula a bad input. The Land '
                              'Training instructor warns that a lease reading 160 acres never states the '
                              "lessor's fractional ownership. In the instructor's words, 'if you look at "
                              'just the lease and it says 160 Acres you might assume that Greg owns 100, '
                              "that would be incorrect,' so lease administration has to pull the lease "
                              'purchase report [wUqopw4hh2o @ 00:02:40]. Sands flags a timing trap on '
                              "production data. State commission sites update monthly and 'may lag a "
                              "couple of months,' so a May lookup may only surface February or March "
                              'volumes, and a brand-new well may not show at all [Yy7az5T7_vs @ 00:13:41]. '
                              'Price is the next leak. Sands notes that Bakken barrels can clear at 50 '
                              'dollars when WTI prints 60, because of a price differential tied to '
                              'transport and processing costs, and that operator hedging blurs the average '
                              'price on the check stub further [Yy7az5T7_vs @ 00:16:47]. The AAPL '
                              'study-guide trap is premature math. In Situation #5, a 1/8 lease minus '
                              "Charlie's 3% NPRI would net David 9.5%, but no lease exists yet. The "
                              "instructor says 'don't be thinking the answer to this is 9.5%,' because the "
                              'correct answer is 100% minerals subject to the 3% NPRI [HkEK5QVZAJ0 @ '
                              '00:04:30]. Each of these errors produces a clean-looking decimal that is '
                              'simply wrong.',
                              'The second failure mode is fat-fingering decimals, and the instructors '
                              "commit it live on camera. While checking the four Brady heirs' "
                              'joint-ownership total, the Land Training instructor stalls '
                              "mid-multiplication with 'oh I did that wrong sorry.' It takes a third pass "
                              'before 0.03125 times four reconciles back to the original 1/8 royalty '
                              '[pjP04Ns4pww @ 00:06:07]. In Pooled Unit Problem 4, a one-fifth royalty on '
                              '10 acres inside an 80-acre Marcellus drilling and spacing unit correctly '
                              "computes to 0.025. It then gets restated aloud as 'a 0.25 is the net "
                              "revenue interest,' a tenfold slip that would wreck a pay deck if it reached "
                              'a division order [kC2dYFP0U0g @ 00:01:26]. In the unit co-tenant lesson, '
                              "the calculator returns 014063 for Peter's royalty share in the 640-acre "
                              'unit, and the whiteboard receives 01463, a dropped zero that silently '
                              'shifts the figure [n2pg2-Q06P8 @ 00:06:59]. Alyce Hoge explains why slips '
                              "like these hide so well. Division order decimals 'usually go out to eight "
                              "decimal places,' which is how owners end up staring at 'crazy decimals' "
                              'they cannot eyeball [eZU5hvGcngg @ 00:13:51]. The practitioner fix is '
                              'structural: separate factor columns, Excel formulas copied down the sheet, '
                              'and a closing sum that must reconcile.',
                              'The third failure mode is running a check that cannot catch the error. The '
                              "UHD instructor's paycheck analogy is blunt: if the payroll person botches a "
                              "deduction, take-home pay is wrong. Likewise, 'if we make a mistake anywhere "
                              "before we get to the net it will affect the net revenue interest' "
                              '[oHKF06pFkh0 @ 00:04:15]. The same instructor caps the method with a '
                              'warning. When an operator brings five leases with different burdens into '
                              "one unit, 'you can't co-mingle them.' The check has to run lease by lease, "
                              'or it will not return the gross-minus-burdens figure [oHKF06pFkh0 @ '
                              '00:10:21]. The unit co-tenant lesson supplies a per-owner reconciliation. '
                              "Greg's royalty share plus the lessee's share must sum to 0.125, which "
                              'equals his 0.5 mineral interest times the 0.25 unit factor, and the same '
                              'test holds for Peter and Bobby [n2pg2-Q06P8 @ 00:10:23]. On the paper side, '
                              'the Land Training instructor warns lease drafters not to write 0.0625 into '
                              'a lease for a 50% owner. Write 1/8 instead and let the proportionate '
                              'reduction clause cut the royalty on the division order, because that clause '
                              'is what gives the operator the right to reduce it [PNLVi6Ee0KM @ 00:09:16]. '
                              'Skip the clause logic, and the lease and the pay deck stop agreeing.'],
               'table': {'caption': 'Firsthand traps, what broke, and the fix practitioners teach',
                         'headers': ['Trap', 'What Went Wrong', 'Fix Taught', 'Expert Source'],
                         'rows': [['Treating lease acreage as ownership',
                                   'Lease shows 160 acres and the reader assumes Greg owns 100% when he '
                                   'owns 25%',
                                   'Pull the lease purchase report to get the actual mineral interest '
                                   'before calculating',
                                   'Land Training www.landtraining.net ([wUqopw4hh2o @ 00:02:40])'],
                                  ['Estimating checks from stale production data',
                                   'State commission sites update monthly and may lag a couple of months '
                                   'behind',
                                   'Average initial production across a large sample of similar nearby '
                                   'wells in the same formation',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:13:41])'],
                                  ['Plugging posted WTI into the royalty estimate',
                                   'Bakken crude can realize 50 dollars when WTI sits at 60 because of the '
                                   'differential',
                                   'Expect the deduct, plus hedged and spot-sold volumes averaged on the '
                                   'check stub',
                                   'Matt Sands ([Yy7az5T7_vs @ 00:16:47])'],
                                  ['Calculating an NRI before any lease exists',
                                   'Answering 9.5% for David when only a 3% NPRI burden and no lease exist',
                                   'State 100% minerals subject to the 3% non-participating royalty '
                                   'interest to Charlie',
                                   'Land Training www.landtraining.net ([HkEK5QVZAJ0 @ 00:04:30])'],
                                  ['Shifting the decimal one place',
                                   'A one-fifth royalty on 10 of 80 acres computed as 0.025, then spoken '
                                   'as 0.25',
                                   'Rerun royalty times tract acres divided by unit acres and confirm the '
                                   'magnitude',
                                   'Land Training www.landtraining.net ([kC2dYFP0U0g @ 00:01:26])'],
                                  ["Misreading the lessee's seven-eighths",
                                   'Seven-eighths written as 0.08 75 before being corrected on the board',
                                   'Confirm the royalty decimal plus the lessee decimal totals 100 percent',
                                   'Land Training www.landtraining.net ([yWZaJ-ItXKQ @ 00:04:47])'],
                                  ['Commingling multiple leases in one check',
                                   'Five leases with different burdens will not reconcile to gross minus '
                                   'burdens',
                                   'Run the check and balance on each lease separately before combining '
                                   'results',
                                   'UHD Continuing and Professional Education ([oHKF06pFkh0 @ '
                                   '00:10:21])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do not release a decimal to the pay deck until these four clear',
                           'body': 'Every gate below comes from a mistake or warning a practitioner '
                                   'reported while working live WI and NRI numbers.',
                           'items': ['Recompute every division order decimal from NMA, DSU acres, and '
                                     'royalty rate, and challenge the operator if your number does not '
                                     'match [Matt Sands — Yy7az5T7_vs @ 00:12:22].',
                                     'Never take mineral interest from the face of the lease; confirm it '
                                     'on the lease purchase report [Land Training www.landtraining.net — '
                                     'wUqopw4hh2o @ 00:02:40].',
                                     'Run the check and balance lease by lease when an operator brings '
                                     'multiple leases with different burdens into a unit [UHD Continuing '
                                     'and Professional Education — oHKF06pFkh0 @ 00:10:21].',
                                     'Write the full royalty fraction in the lease and let the '
                                     'proportionate reduction clause produce the reduced decimal on the '
                                     'division order [Land Training www.landtraining.net — PNLVi6Ee0KM @ '
                                     '00:09:16].']}}],
 'pull_quote': 'Always do a check and a balance even if it feels cumbersome, even if it feels like you '
               'hardly ever make a mistake. Attributed to UHD Continuing and Professional Education '
               '(oHKF06pFkh0 @ 00:08:28).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Multiply gross tract acreage by your decimal interest to get net mineral acres, and '
                      'order a title search if the decimal is unknown [Matt Sands — Yy7az5T7_vs @ '
                      '00:06:19].',
                      'Pull the drilling spacing unit size from the state oil and gas commission GIS map '
                      'by turning on the DSU layer for your section [Matt Sands — Yy7az5T7_vs @ 00:07:46].',
                      'Read the royalty clause on the first page of the lease and convert fractions like '
                      '1/8 or 1/5 to decimals [Matt Sands — Yy7az5T7_vs @ 00:10:11].',
                      'Build an Excel sheet with royalty, mineral interest, tract acres, and unit acres '
                      'columns, then drag the formula down every owner row [Land Training '
                      'www.landtraining.net — wUqopw4hh2o @ 00:10:21].',
                      "Subtract any override from the operator's 0.875 before reporting its NRI, as in "
                      '0.875 minus 0.03 equals 0.845 [Land Training www.landtraining.net — B5fBIyi1-hw @ '
                      '00:05:00].',
                      'Estimate the royalty check as barrels times price times NRI, as in 10,000 barrels '
                      'times 50 dollars times .001875 equals about 937 dollars, and dig deeper if the '
                      'actual check differs significantly [Matt Sands — Yy7az5T7_vs @ 00:15:38].'],
 'statutory_citations': [{'title': 'Matt Sands — MRP 3: How to Calculate your Net Revenue Interest in 3 '
                                   'Simple Steps [00:11:24]',
                          'url': 'https://www.youtube.com/watch?v=Yy7az5T7_vs&t=684s',
                          'relevance': 'Primary practitioner testimony on the NMA divided by DSU times '
                                       'royalty method and division order verification.'},
                         {'title': 'UHD Continuing and Professional Education — Calculating the Oil '
                                   "Company's Net Revenue Interest [00:08:28]",
                          'url': 'https://www.youtube.com/watch?v=oHKF06pFkh0&t=508s',
                          'relevance': 'Primary practitioner testimony on gross minus burdens and the '
                                       'lease-level check and balance.'},
                         {'title': 'Land Training www.landtraining.net — Calculating WI and NRI in an Oil '
                                   '& Gas Lease by Alyce Hoge [00:12:00]',
                          'url': 'https://www.youtube.com/watch?v=eZU5hvGcngg&t=720s',
                          'relevance': 'Primary practitioner testimony on the grand bargain and how '
                                       'pooled-unit division order decimals are built.'},
                         {'title': 'Land Training www.landtraining.net — VII NRI Co Tenants Different RI '
                                   'in a Spacing Unit Prob 1 [00:00:42]',
                          'url': 'https://www.youtube.com/watch?v=wUqopw4hh2o&t=42s',
                          'relevance': 'Primary practitioner testimony on the royalty times mineral '
                                       'interest times tract over unit formula for co-tenants.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Yy7az5T7_vs',
                       'title': 'MRP 3: How to Calculate your Net Revenue Interest in 3 Simple Steps',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': "If you're sure or fairly certain that you're using the right information, "
                               "that's where you go back to the operator who sent you the division order "
                               "and then you can challenge that interest to make sure that it's correct.",
                       'tip': "If you're sure or fairly certain that you're using the right information, "
                              "that's where you go back to the operator who sent you the division order "
                              "and then you can challenge that interest to make sure that it's correct.",
                       'timestamp': 742,
                       'timestamp_seconds': 742,
                       'timestamp_label': '[00:12:22]',
                       'url': 'https://www.youtube.com/watch?v=Yy7az5T7_vs&t=742s',
                       'markdown': '[00:12:22](https://www.youtube.com/watch?v=Yy7az5T7_vs&t=742s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Yy7az5T7_vs',
                       'title': 'MRP 3: How to Calculate your Net Revenue Interest in 3 Simple Steps',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'The first step is we take the net mineral acres that we own and divide '
                               'that by the size of our drilling spacing unit acres.',
                       'tip': 'The first step is we take the net mineral acres that we own and divide that '
                              'by the size of our drilling spacing unit acres.',
                       'timestamp': 684,
                       'timestamp_seconds': 684,
                       'timestamp_label': '[00:11:24]',
                       'url': 'https://www.youtube.com/watch?v=Yy7az5T7_vs&t=684s',
                       'markdown': '[00:11:24](https://www.youtube.com/watch?v=Yy7az5T7_vs&t=684s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eZU5hvGcngg',
                       'title': 'Calculating WI and NRI in an Oil & Gas Lease by Alyce Hoge',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'The lower we can make this royalty payment the higher the net revenue '
                               'interest is going to be for the oil and gas company.',
                       'tip': 'The lower we can make this royalty payment the higher the net revenue '
                              'interest is going to be for the oil and gas company.',
                       'timestamp': 466,
                       'timestamp_seconds': 466,
                       'timestamp_label': '[00:07:46]',
                       'url': 'https://www.youtube.com/watch?v=eZU5hvGcngg&t=466s',
                       'markdown': '[00:07:46](https://www.youtube.com/watch?v=eZU5hvGcngg&t=466s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PjGnR-YfLy4',
                       'title': 'III  GWI & NRI in an Oil & Gas Lease   One Owner Example 1',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "Some people say think about this being the jib deck, it's who is paying "
                               "the bills, so it's called a joint interest billing deck.",
                       'tip': "Some people say think about this being the jib deck, it's who is paying the "
                              "bills, so it's called a joint interest billing deck.",
                       'timestamp': 515,
                       'timestamp_seconds': 515,
                       'timestamp_label': '[00:08:35]',
                       'url': 'https://www.youtube.com/watch?v=PjGnR-YfLy4&t=515s',
                       'markdown': '[00:08:35](https://www.youtube.com/watch?v=PjGnR-YfLy4&t=515s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oHKF06pFkh0',
                       'title': 'Calculating the Oil Company’s Net Revenue Interest',
                       'channel': 'UHD Continuing and Professional Education',
                       'author': 'UHD Continuing and Professional Education',
                       'text': "Here's my advice: always do a check and a balance even if it feels "
                               'cumbersome.',
                       'tip': "Here's my advice: always do a check and a balance even if it feels "
                              'cumbersome.',
                       'timestamp': 508,
                       'timestamp_seconds': 508,
                       'timestamp_label': '[00:08:28]',
                       'url': 'https://www.youtube.com/watch?v=oHKF06pFkh0&t=508s',
                       'markdown': '[00:08:28](https://www.youtube.com/watch?v=oHKF06pFkh0&t=508s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oHKF06pFkh0',
                       'title': 'Calculating the Oil Company’s Net Revenue Interest',
                       'channel': 'UHD Continuing and Professional Education',
                       'author': 'UHD Continuing and Professional Education',
                       'text': "You're going to have to calculate or do the check and a balance on each of "
                               "the leases separately from one another; in other words, you can't "
                               'co-mingle them.',
                       'tip': "You're going to have to calculate or do the check and a balance on each of "
                              "the leases separately from one another; in other words, you can't co-mingle "
                              'them.',
                       'timestamp': 621,
                       'timestamp_seconds': 621,
                       'timestamp_label': '[00:10:21]',
                       'url': 'https://www.youtube.com/watch?v=oHKF06pFkh0&t=621s',
                       'markdown': '[00:10:21](https://www.youtube.com/watch?v=oHKF06pFkh0&t=621s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HkEK5QVZAJ0',
                       'title': 'Situation #5 WI & NRI Calculations p  70 AAPL  Study Guide',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "There's no lease currently, so don't be thinking the answer to this is "
                               '9.5%.',
                       'tip': "There's no lease currently, so don't be thinking the answer to this is "
                              '9.5%.',
                       'timestamp': 270,
                       'timestamp_seconds': 270,
                       'timestamp_label': '[00:04:30]',
                       'url': 'https://www.youtube.com/watch?v=HkEK5QVZAJ0&t=270s',
                       'markdown': '[00:04:30](https://www.youtube.com/watch?v=HkEK5QVZAJ0&t=270s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yWZaJ-ItXKQ',
                       'title': 'Working Interest & Net Revenue Interests in Oil & Gas Lease Calculations',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "We're going to basically take their net acres divided by the unit acres "
                               "times the royalty interest and that's going to give us the lessor's net "
                               'revenue interest.',
                       'tip': "We're going to basically take their net acres divided by the unit acres "
                              "times the royalty interest and that's going to give us the lessor's net "
                              'revenue interest.',
                       'timestamp': 614,
                       'timestamp_seconds': 614,
                       'timestamp_label': '[00:10:14]',
                       'url': 'https://www.youtube.com/watch?v=yWZaJ-ItXKQ&t=614s',
                       'markdown': '[00:10:14](https://www.youtube.com/watch?v=yWZaJ-ItXKQ&t=614s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JVbDAxk_YTU',
                       'title': 'Situation #4 WI & NRI Calculations p  70 AAPL Study Guide',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'When we see the words produced and saved, that is an indication that we '
                               'are not selling minerals but we are selling a royalty interest.',
                       'tip': 'When we see the words produced and saved, that is an indication that we are '
                              'not selling minerals but we are selling a royalty interest.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=JVbDAxk_YTU&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=JVbDAxk_YTU&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pjP04Ns4pww',
                       'title': 'V NRI Joint Ownership Undivided Interests   Same RI Problem 1',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'All you have to remember is that we have to reduce that royalty by their '
                               'actual percentage of interest.',
                       'tip': 'All you have to remember is that we have to reduce that royalty by their '
                              'actual percentage of interest.',
                       'timestamp': 192,
                       'timestamp_seconds': 192,
                       'timestamp_label': '[00:03:12]',
                       'url': 'https://www.youtube.com/watch?v=pjP04Ns4pww&t=192s',
                       'markdown': '[00:03:12](https://www.youtube.com/watch?v=pjP04Ns4pww&t=192s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WPeA0rs7SLA',
                       'title': 'IV NRI Calculations of Mineral Owner Pooled Unit Problem 1',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "The well doesn't have to be on your property in order for you to get a "
                               'share of it, but your share is going to be reduced by the number of acres '
                               "that's actually in the unit.",
                       'tip': "The well doesn't have to be on your property in order for you to get a "
                              'share of it, but your share is going to be reduced by the number of acres '
                              "that's actually in the unit.",
                       'timestamp': 274,
                       'timestamp_seconds': 274,
                       'timestamp_label': '[00:04:34]',
                       'url': 'https://www.youtube.com/watch?v=WPeA0rs7SLA&t=274s',
                       'markdown': '[00:04:34](https://www.youtube.com/watch?v=WPeA0rs7SLA&t=274s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wUqopw4hh2o',
                       'title': 'VII NRI Co Tenants Different RI in a Spacing Unit Prob 1',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'If you look at just the lease and it says 160 acres you might assume that '
                               'Greg owns 100, that would be incorrect; you still have to look at this '
                               'lease purchase report.',
                       'tip': 'If you look at just the lease and it says 160 acres you might assume that '
                              'Greg owns 100, that would be incorrect; you still have to look at this '
                              'lease purchase report.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=wUqopw4hh2o&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=wUqopw4hh2o&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B5fBIyi1-hw',
                       'title': 'Situation #3 WI & NRI Calculations AAPL Study Guide PG 70',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'The working interest owner, typically the oil and gas company, is going to '
                               "be the one that pays the geologist; it doesn't come from the royalty "
                               "owners or the mineral owner's property.",
                       'tip': 'The working interest owner, typically the oil and gas company, is going to '
                              "be the one that pays the geologist; it doesn't come from the royalty owners "
                              "or the mineral owner's property.",
                       'timestamp': 176,
                       'timestamp_seconds': 176,
                       'timestamp_label': '[00:02:56]',
                       'url': 'https://www.youtube.com/watch?v=B5fBIyi1-hw&t=176s',
                       'markdown': '[00:02:56](https://www.youtube.com/watch?v=B5fBIyi1-hw&t=176s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'n2pg2-Q06P8',
                       'title': 'Unit:  Calculating Undivided Interests with Different Royalties in a Unit',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "If you have a logical mind, you're going to be able to do this kind of "
                               'work, so just take your time and think it through.',
                       'tip': "If you have a logical mind, you're going to be able to do this kind of "
                              'work, so just take your time and think it through.',
                       'timestamp': 693,
                       'timestamp_seconds': 693,
                       'timestamp_label': '[00:11:33]',
                       'url': 'https://www.youtube.com/watch?v=n2pg2-Q06P8&t=693s',
                       'markdown': '[00:11:33](https://www.youtube.com/watch?v=n2pg2-Q06P8&t=693s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PNLVi6Ee0KM',
                       'title': 'Calculating Undivided Interest - Different Royalties.avi',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'The proportionate reduction clause says that we can reduce the royalty '
                               'rate based on what they actually own in the fee simple estate.',
                       'tip': 'The proportionate reduction clause says that we can reduce the royalty rate '
                              'based on what they actually own in the fee simple estate.',
                       'timestamp': 601,
                       'timestamp_seconds': 601,
                       'timestamp_label': '[00:10:01]',
                       'url': 'https://www.youtube.com/watch?v=PNLVi6Ee0KM&t=601s',
                       'markdown': '[00:10:01](https://www.youtube.com/watch?v=PNLVi6Ee0KM&t=601s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kC2dYFP0U0g',
                       'title': 'IV NRI Calculations of Mineral Owner Pooled Unit Problem 4',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': 'All we did was we took the royalty times the tract acres divided by the '
                               'unit acres to get that net revenue interest.',
                       'tip': 'All we did was we took the royalty times the tract acres divided by the '
                              'unit acres to get that net revenue interest.',
                       'timestamp': 86,
                       'timestamp_seconds': 86,
                       'timestamp_label': '[00:01:26]',
                       'url': 'https://www.youtube.com/watch?v=kC2dYFP0U0g&t=86s',
                       'markdown': '[00:01:26](https://www.youtube.com/watch?v=kC2dYFP0U0g&t=86s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kw0rYmoBLXU',
                       'title': 'IV NRI Calculations of Mineral Owner Pooled Unit Problem 3',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "I've now taken out lease tract acres and it's just tract acres, which is "
                               "how you're usually going to see it.",
                       'tip': "I've now taken out lease tract acres and it's just tract acres, which is "
                              "how you're usually going to see it.",
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=kw0rYmoBLXU&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=kw0rYmoBLXU&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VPrc0ax0-_o',
                       'title': 'IV NRI Calculations of Mineral Owner Pooled Unit Problem 2',
                       'channel': 'Land Training www.landtraining.net',
                       'author': 'Land Training www.landtraining.net',
                       'text': "This mineral owner's net revenue interest is not going to be reduced at "
                               "all, so he's going to be able to keep that 1875 net revenue interest.",
                       'tip': "This mineral owner's net revenue interest is not going to be reduced at "
                              "all, so he's going to be able to keep that 1875 net revenue interest.",
                       'timestamp': 86,
                       'timestamp_seconds': 86,
                       'timestamp_label': '[00:01:26]',
                       'url': 'https://www.youtube.com/watch?v=VPrc0ax0-_o&t=86s',
                       'markdown': '[00:01:26](https://www.youtube.com/watch?v=VPrc0ax0-_o&t=86s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
