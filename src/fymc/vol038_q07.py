from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'cost-segregation-fundamentals-and-payoff-analysis',
 'question_prompt': 'What is a cost segregation study, when does it pay off, and when is it a bad idea?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Cost Segregation Fundamentals and Payoff Analysis',
 'subtitle': 'Reclassifying building components into shorter lives, $350K and $750K benefit estimates, '
             'short-term rental and real-estate-professional use cases, a real study walkthrough, referral '
             'processes, and cases where cost seg backfires',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'CPAs, tax attorneys and engineering-led study shops agree cost segregation is a '
                      "timing weapon: carve 25-40% of a building's basis into 5-, 7- and 15-year buckets "
                      'and, with 100% bonus restored, write it off in year one. Engineered Tax Services '
                      'turns a $2.5M depreciable basis from $64K of straight-line into $794K in year one; '
                      'CostSegRx shows $25,921 saved on a $750K commercial buy at 24%. Studies run $500 '
                      'DIY to $15K, averaging $3-6K, with the free benefit analysis back in 1-2 days and '
                      "final reports inside about six weeks. Land value is, per CSA Partners' Chris "
                      'Streit, the easiest thing for the IRS to deny. The fault lines: whether the loss is '
                      'usable outside REPS or the short-term-rental loophole, what rate recapture hits at, '
                      'whether 2026 bonus sits at 100% or 20%, and whether small deals beat the fee.',
 'key_metrics': [{'label': 'Typical Reclassification Range on Good Candidates',
                  'metric': 'Typical Reclassification Range on Good Candidates',
                  'value': '25-40% of basis',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Chris Streit of CSA Partners on the share of a good candidate property that '
                             'moves into accelerated classes; mobile home parks run a little over 80% and '
                             'warehouses 12-15%.',
                  'source': 'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ 00:15:54])'},
                 {'label': 'Year-One Write-Off With Bonus on a $2.5M Basis',
                  'metric': 'Year-One Write-Off With Bonus on a $2.5M Basis',
                  'value': '$794K year one vs $64K straight-line',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A $3M building with $2.5M left after land; $172K accelerated without bonus, '
                             'and a December close still books about $770K because bonus is not prorated.',
                  'source': 'Engineered Tax Services ([qEFJIGNNOkw @ 00:12:13])'},
                 {'label': 'Cost of a Study',
                  'metric': 'Cost of a Study',
                  'value': '$500 DIY up to $15K; average $3-6K',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Mark Perlberg's range for study pricing, against historical pricing of "
                             '$20-25K and $100K-plus on large projects reported by Engineered Tax '
                             'Services.',
                  'source': 'Mark Perlberg, CPA ([3bjz5YCldWA @ 00:21:12])'},
                 {'label': 'Audit Frequency on Cost Segregation Studies',
                  'metric': 'Audit Frequency on Cost Segregation Studies',
                  'value': 'About 4-5 audits per ~5,000 studies a year (1 in 1,000)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Chris Streit's firm volume versus audits it defends each year; land value, "
                             'missing site visits and missing cost methodology are the red flags.',
                  'source': 'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ '
                            '00:18:44])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every operator here runs the same engine: a study pulls components out of '
                              'the long-life building bucket and drops them into short-life buckets that '
                              'can be written off fast. Toby Mathis sets the baseline, with residential '
                              'treated as 1250 property over 27.5 years and commercial stretched over 39 '
                              'years [3G2c1STMThk @ 00:00:25]. Karlton Dennis shows the drag in raw '
                              'numbers: $1M of residential building throws off only $36,363.63 a year, and '
                              'the same $1M on a 39-year schedule yields $25,641; his field test for '
                              "splitting structural from non-structural components is to 'flip a house "
                              "upside down' [NOA2tGOp9G8 @ 00:06:08]. Mark Perlberg puts fridges, TVs, "
                              'linens and cabinetry in the 5-year bucket, driveways and pools in 15-year, '
                              'and stresses that bonus depreciation only reaches assets with lives under '
                              '20 years [3bjz5YCldWA @ 00:06:07]. Brendan Hall of Hall CPA confirms the '
                              'allocation runs across 5-, 7-, 15- and 27.5-year classes and that 100% '
                              'bonus lands on the short-life pieces when the study is done in the first '
                              'year of ownership, generally 20-30% of the purchase price [6eVkkFsis9g @ '
                              '00:02:01]. Nothing new is deducted; the same basis is simply pulled forward '
                              'out of the back decades and into the early years when cash matters most.',
                              'The reclassification band is remarkably tight across shops that compete '
                              'hard for the same investor clients. Engineered Tax Services reports about '
                              '30% of basis, with a 25-40% range, on multifamily, commercial and '
                              'hospitality deals pushed through its pipeline of 75,000-plus studies '
                              '[qEFJIGNNOkw @ 00:18:41]. Chris Streit, CEO of the cost-seg-only shop CSA '
                              "Partners, quotes the identical 25-40% for good candidates on Toby Mathis's "
                              'channel and walks a $500K duplex down to a $400K basis, roughly 30% '
                              'accelerated, a $120K deduction worth about $50K in tax at a 37% bracket '
                              '[beMOZDrXOJ8 @ 00:15:54]. Karlton Dennis lands in the same 25-40% '
                              'non-structural window and runs it to the end: with 100% bonus, a $1M '
                              'purchase produces roughly a negative $400K loss on paper [NOA2tGOp9G8 @ '
                              '00:07:39]. Mark Perlberg, after seeing hundreds of studies, compresses it '
                              'to a ballpark operators can do in their heads: 25% of purchase price for a '
                              'long-term rental and 30% for a short-term rental, with year-one write-offs '
                              'that can reach 50% [3bjz5YCldWA @ 00:17:47]. That convergence is the core '
                              'screening tool. Before paying anyone, multiply the depreciable basis by '
                              '25-30%, apply your marginal bracket, and see whether the resulting cash '
                              "number moves the needle at all on this year's return.",
                              'The prerequisite every serious practitioner hammers is not the property; it '
                              "is the owner's tax status. Streit's two-part test on Toby Mathis's channel "
                              'is simple: you need an income-producing property, and then your status '
                              'decides the reach, because a real estate professional can offset all income '
                              'while everyone else offsets only rental or passive income [beMOZDrXOJ8 @ '
                              '00:10:13]. Mark Perlberg spells out the REP bar as 750 hours, 50% of '
                              'working time, 5% ownership, plus material participation at the 100- or '
                              '500-hour marks, and names the short-term-rental loophole, an average stay '
                              'of 7 days or less, as the side door [3bjz5YCldWA @ 00:09:37]. Brendan Hall '
                              'gives the non-REP math: a $25K passive allowance below $100K of MAGI, '
                              'phased out above $150K, with suspended losses carried forward, while REPs '
                              'who materially participate are unlimited [6eVkkFsis9g @ 00:02:33]. The LYFE '
                              'Accounting CPA, who runs studies through a virtual cost-seg vendor, shows '
                              "what happens when that gate is skipped: one client is sitting on 'hundreds "
                              "of thousands' in passive losses that cannot be used [w16nUKkydYc @ "
                              '00:07:57]. Consensus verdict: confirm exactly where the loss will land, '
                              'against W-2, business or passive income, before ordering the study, or the '
                              'deduction just parks on the return as a carryforward.'],
               'table': {'caption': 'Where the practitioners line up on cost segregation fundamentals',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Reclassification band for standard income property deals',
                                   'About 30% of basis, 25-40% range, on multifamily, commercial and '
                                   'hospitality',
                                   'Screen every deal at 25-30% of basis before ordering anything',
                                   'Engineered Tax Services ([qEFJIGNNOkw @ 00:18:41])'],
                                  ['Quick rule of thumb by rental type',
                                   'Ballpark 25% of purchase price for long-term rentals and 30% for '
                                   'short-term',
                                   'Use the rental type to set a fast first-year write-off estimate',
                                   'Mark Perlberg, CPA ([3bjz5YCldWA @ 00:17:47])'],
                                  ['Bonus reach is limited to short-life assets',
                                   '100% bonus covers lives under 20 years when the study is done in year '
                                   'one',
                                   'Order the study in the first year of ownership to capture full bonus',
                                   'Hall CPA | Tax Smart Real Estate Investors ([6eVkkFsis9g @ 00:02:01])'],
                                  ['Owner tax status decides whether the loss is usable',
                                   'A REP offsets all income; everyone else offsets only rental or passive '
                                   'income',
                                   'Confirm REP or passive position before paying any study fee at all',
                                   'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ '
                                   '00:10:13])'],
                                  ['Short-term rental route as the alternative pathway',
                                   'STR requires 100 hours and an average guest stay of 7 days or less',
                                   'Dennis buys in October, runs it short-term, then converts to long-term '
                                   'in January',
                                   'Karlton Dennis ([NOA2tGOp9G8 @ 00:10:17])'],
                                  ['Passive allowance ceiling for non-REP owners',
                                   '$25K allowance below $100K MAGI, phased out above $150K, suspended '
                                   'losses carry forward',
                                   'High earners without REP status should expect the loss to sit '
                                   'suspended',
                                   'Hall CPA | Tax Smart Real Estate Investors ([6eVkkFsis9g @ 00:02:33])'],
                                  ['Large deals are the default use case',
                                   'Morris says cost seg is almost always prescribed on large deals, with '
                                   'REP NOLs carrying forward',
                                   'Bigger basis clears the study fee with plenty of room to spare',
                                   'Advise RE ([8ZzVeQLb80E @ 00:05:40])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The worked numbers line up across shops. Engineered Tax Services runs a $3M '
                              'building with $2.5M left after land: $64K a year straight-line, $172K '
                              'accelerated without bonus, and $794K in year one with bonus, and because '
                              'bonus is not prorated, a December close still books about $770K against '
                              "roughly $6K of straight-line [qEFJIGNNOkw @ 00:13:12]. CostSegRx's $750K "
                              'commercial file backs land out at 20%, or $150,000, straight from county '
                              'tax records, adds $75,000 of improvements for a $675,000 basis, and lands '
                              '$101,250 accelerated, $108,003 of first-year depreciation and $25,921 of '
                              'savings at a 24% rate [IFbN2m1Gw3Y @ 00:01:44]. Its $350K Sarasota rental '
                              'placed in service 7/15/2026 uses 25% land for a $262,500 basis, then '
                              '$46,200 accelerated, $49,806 first-year and $11,953 saved at 24% '
                              '[Ha5KYCa_Yjk @ 00:01:20]. Karlton Dennis opens his own 2023 duplex study at '
                              '80% bonus: $404,990 cost, $29,295 land, $375,695 basis, split into $83K of '
                              '5-year, $24K of 15-year and $266K of 27.5-year, which put $93,505 of '
                              'year-one depreciation on his return [NOA2tGOp9G8 @ 00:13:45]. Each file '
                              'shows the same shape: a fat first year, then thinner trailing depreciation, '
                              'which CostSegRx quantifies at $14,711 with the study versus $17,307 without '
                              'on the commercial deal and $7,865 versus $9,545 on the rental.',
                              'Execution is a short, mostly manual pipeline. Engineered Tax Services times '
                              "it: a benefit analysis that takes 1-2 days and is 'not automated,' a site "
                              'visit within 2-3 weeks, and a final report in no more than about 6 weeks '
                              '[qEFJIGNNOkw @ 00:21:39]. In its real-estate-pro webinar the same firm '
                              'quotes the benefit analysis at about 24 hours and no cost, prices an '
                              "in-person visit at 'a couple hundred bucks,' and calls a virtual visit 'not "
                              "ideal' if the study ever lands in audit; its calculator defaults to 20% "
                              'land, 23% to 5-year and 5% to 15-year, turning a $5M property into $1.1M of '
                              'bonus and then about $104K a year [sXpa52KOvog @ 00:29:02]. Pricing is down '
                              'hard from the era when studies ran $20-25K and large projects $100K-plus. '
                              "Mark Perlberg puts today's range at $500 DIY up to $15K, averaging $3-6K "
                              '[3bjz5YCldWA @ 00:21:12]. Peter Harris budgets $4-5K for a 10-unit and '
                              'about $20K for a 100-unit, and his own math shows why scale wins: the fee '
                              'roughly quadruples while the reclassified basis jumps from $300K to $2.1M, '
                              'about sevenfold, which on his 100-unit deal split across 10 investors hands '
                              'each $210K of write-off in year one [lJFBf789ODI @ 00:12:14].',
                              'The defense file is built before the IRS ever asks. Chris Streit puts land '
                              "value at the top of the red-flag list because 'it is the easiest thing for "
                              "the IRS to deny'; examiners pull the county appraisal district number, and "
                              "flat 80/20, 15% or 10% land splits have been 'lost in less than three "
                              "minutes' [beMOZDrXOJ8 @ 00:21:41]. His next two flags are no site visit and "
                              "no cost methodology such as RSMeans, and he warns that 'there are firms "
                              "right now who can give you a report in 30 minutes with no site visit'; his "
                              'own shop handles 70% of visits remotely but live [beMOZDrXOJ8 @ 00:23:34]. '
                              'Engineered Tax Services pushes land value back to the CPA, notes a '
                              'California property can be 80% land, and says the IRS audits land value '
                              'more often [qEFJIGNNOkw @ 00:52:48]. Stefan Morris of Advise RE starts '
                              'every analysis with the land-building allocation and treats it as a '
                              'facts-and-circumstances call [8ZzVeQLb80E @ 00:00:26]. Audit odds are low '
                              "but not zero: Streit's firm runs about 5,000 studies a year and sees "
                              'roughly 4-5 audits, about 1 in 1,000, and Engineered Tax Services says 99% '
                              'of IDRs close once the study is sent and covers clients through appeals.'],
               'table': {'caption': 'Deal-level numbers practitioners ran on camera',
                         'headers': ['Deal / Scenario',
                                     'Inputs Stated',
                                     'Reported Output',
                                     'Expert Source'],
                         'rows': [['$3M commercial building walked through the webinar',
                                   '$3M price with $2.5M depreciable after backing out land',
                                   '$64K straight-line, $172K accelerated without bonus, $794K year one '
                                   'with bonus',
                                   'Engineered Tax Services ([qEFJIGNNOkw @ 00:12:13])'],
                                  ['$750K commercial property for tax year 2026',
                                   '20% land per county tax records, $75K improvements, $675K total basis',
                                   '$101,250 accelerated, $108,003 first-year, $25,921 saved at a 24% rate',
                                   'CostSegRx ([IFbN2m1Gw3Y @ 00:01:44])'],
                                  ['$350K Sarasota residential rental on Freewater Lane',
                                   '25% land, $262,500 basis, in service 7/15/2026, 100% bonus',
                                   '$46,200 accelerated, $49,806 first-year, $11,953 saved at 24% '
                                   'effective',
                                   'CostSegRx ([Ha5KYCa_Yjk @ 00:00:37])'],
                                  ["Karlton Dennis's own 2023 duplex study at 80% bonus",
                                   '$404,990 cost, $29,295 land, $375,695 depreciable basis',
                                   '$83K 5-year, $24K 15-year, $93,505 of year-one depreciation received',
                                   'Karlton Dennis ([NOA2tGOp9G8 @ 00:13:45])'],
                                  ['Self-storage outlier deal with leverage',
                                   '$1.35M price, 25% down ($337K), 8% interest, 10% cap rate',
                                   '$1.08M year-one depreciation produced a $421K refund on $32K yearly '
                                   'cash flow',
                                   'Engineered Tax Services ([qEFJIGNNOkw @ 00:16:40])'],
                                  ['10-unit apartment building example from Peter Harris',
                                   '$1M price, 20% land, about 30% land improvements plus personal '
                                   'property',
                                   'About $29K/yr straight-line versus $300K pulled into year one with '
                                   'bonus',
                                   'Commercial Property Advisors ([lJFBf789ODI @ 00:05:57])'],
                                  ['Yield by asset class from a cost-seg-only firm',
                                   'Mobile home parks, warehouses, log cabins and high-rise condos '
                                   'compared',
                                   'Mobile home park a little over 80%, warehouses 12-15%, cabins and '
                                   'condos weak',
                                   'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ '
                                   '00:17:33])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the Study Shops Do That Retail Investors Miss',
                           'body': 'Four moves the study firms and their CPAs use to squeeze more out of '
                                   'the same building and the same calendar.',
                           'items': ['Run the free benefit analysis before spending a dollar: Engineered '
                                     'Tax Services turns it around in about 24 hours at no cost '
                                     '[Engineered Tax Services — sXpa52KOvog @ 00:25:23].',
                                     'Close in December without fear: bonus is not prorated, so a '
                                     'late-year buy still books about $770K on a $2.5M basis versus about '
                                     '$6K straight-line [Engineered Tax Services — qEFJIGNNOkw @ '
                                     '00:13:12].',
                                     'Missed the filing window? Streit applies the study to the open year '
                                     'through the September/October extension with no amendment and calls '
                                     "it 'not a red flag' [Toby Mathis Esq | Tax Planning & Asset "
                                     'Protection — beMOZDrXOJ8 @ 00:12:33].',
                                     'Work the insurance angle: Engineered Tax Services reports 20-23% '
                                     'premium savings per property, citing seven car washes and gas '
                                     'stations in one week [Engineered Tax Services — sXpa52KOvog @ '
                                     '00:22:19].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pin the land number to the county record',
                              'action': 'Back land out using the county tax record or appraisal district '
                                        'figure, never a flat percentage split.',
                              'detail': "CostSegRx backs land out at 20% 'per the county tax records' on "
                                        'its $750K file [CostSegRx — IFbN2m1Gw3Y @ 00:00:00], and Streit '
                                        'says the IRS uses the county appraisal district while flat 80/20, '
                                        "15% or 10% splits were 'lost in less than three minutes' [Toby "
                                        'Mathis Esq | Tax Planning & Asset Protection — beMOZDrXOJ8 @ '
                                        '00:21:41].'},
                             {'step': 2,
                              'title': 'Run the calculator and the benefit analysis',
                              'action': 'Get a free estimate and a human-built benefit analysis before '
                                        'committing to the full study fee.',
                              'detail': "Streit's free calculator runs in a few seconds, but the land "
                                        'value behind it takes 4-6 hours [Toby Mathis Esq | Tax Planning & '
                                        'Asset Protection — beMOZDrXOJ8 @ 00:28:06]; Engineered Tax '
                                        "Services says its benefit analysis takes 1-2 days and is 'not "
                                        "automated' [Engineered Tax Services — qEFJIGNNOkw @ 00:20:51]."},
                             {'step': 3,
                              'title': 'Book the engineer site visit with a cost methodology',
                              'action': 'Insist on an engineer site visit and a named cost methodology '
                                        'such as RSMeans in the report.',
                              'detail': 'AirDNA lays the process out as document review, engineer site '
                                        'visit, then depreciation schedules [AirDNA — nj5gSNmRQuU @ '
                                        '00:01:12]; Streit lists no site visit and no cost methodology '
                                        'such as RSMeans as audit red flags [Toby Mathis Esq | Tax '
                                        'Planning & Asset Protection — beMOZDrXOJ8 @ 00:23:34].'},
                             {'step': 4,
                              'title': 'Load the revised fixed asset schedule and model trailing years',
                              'action': 'Hand the CPA the revised schedule and check year-one against the '
                                        'lower trailing depreciation that follows.',
                              'detail': "CostSegRx's revised schedule breaks out building, distributive "
                                        'trades and services, land improvements and land, then pulls '
                                        'forward bonus [CostSegRx — IFbN2m1Gw3Y @ 00:00:42], and shows '
                                        'trailing depreciation of $14,711 with the study versus $17,307 '
                                        'without [CostSegRx — IFbN2m1Gw3Y @ 00:02:07].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Recapture is the fault line that splits the bench. Karlton Dennis waves it '
                              'off, saying they "aren\'t worried" because an IRC 1031 exchange rolls the '
                              'gain forward [NOA2tGOp9G8 @ 00:16:02]. Peter Harris of Commercial Property '
                              'Advisors lands in a similar camp, pricing recapture at 25 to 30 percent but '
                              'framing the whole maneuver as a "zero interest loan" that funds '
                              'wealth-building while the property inflates [lJFBf789ODI @ 00:13:26]. '
                              'Stefan Morris at Advise RE is blunter about what the study actually is: '
                              'deferral, not permanent savings, with the benefit coming back at the 25 '
                              'percent Section 1250 rate, so flipping fails while buy, hold and 1031 works '
                              '[8ZzVeQLb80E @ 00:04:57]. Clint Coons puts hard numbers on an early exit: '
                              '$100,000 recaptured at 32 percent is $32,000, plus $50,000 of straight-line '
                              'at 25 percent is another $12,500, for $42,500 handed back, and he warns '
                              'that Section 1245 property complicates the 1031 escape hatch Dennis leans '
                              'on [fV7tusLGp3E @ 00:09:03]. Even the stated rate splits them: Morris says '
                              '25 percent, Coons splits ordinary and 25 percent, and Harris quotes a 25 to '
                              '30 percent band. Operators should model the exit price and hold period '
                              'before ordering the study, not after the refund lands.',
                              'The second split is the bonus rate itself, and operators pricing a 2026 '
                              'deal get contradictory instructions. CostSegRx runs its $350,000 Sarasota '
                              'rental at "100% for tax year 2026," producing $46,200 of accelerated '
                              'depreciation and $49,806 in year one [Ha5KYCa_Yjk @ 00:00:37]. Clint Coons '
                              'says 100 percent bonus is now permanent for property placed in service '
                              'after January 19, 2025, with 2018 to 2025 property riding a declining '
                              'schedule [fV7tusLGp3E @ 00:02:06]. BizCpas, by contrast, lays out a '
                              'schedule of 100 percent in 2022, stepping down 20 points a year to just 20 '
                              'percent in 2026, and builds its $700,000 home example on that phase-down '
                              '[mKOnV6RitlA @ 00:06:04]. Engineered Tax Services threads the needle with a '
                              'date test: property purchased, or construction started, before January 2025 '
                              'still falls under the phase-down rules, and their presenter adds that not '
                              'everything qualifies for 100 percent bonus [qEFJIGNNOkw @ 00:22:13]. The '
                              'playbook difference is real money. A study modeled at 20 percent bonus '
                              'front-loads a fraction of what the same study modeled at 100 percent does, '
                              'so the acquisition date, the placed-in-service date and the construction '
                              'start date have to be pinned down before anyone quotes a first-year number '
                              'to a client or a syndication investor.',
                              'Practitioners also split on how much study an operator actually needs to '
                              'buy. Brendan Hall of Hall CPA teaches a DIY "mini" study, pricing movable '
                              'items by make and model on eBay, while conceding the "results won\'t be '
                              'near as good" as an engineered report [6eVkkFsis9g @ 00:03:20]. Toby Mathis '
                              'tells viewers to "calculate, calculate, and calculate," notes that software '
                              'studies run about $1,000 but carry uncertain audit durability, and relays '
                              'Jeff Webb\'s dissent that a study is "a waste of time and money" if you '
                              'plan to sell, yet valuable if you hold [3G2c1STMThk @ 00:02:02]. On the '
                              'site visit, Chris Streit of CSA Partners lists a missing visit as a red '
                              "flag but says 70 percent of his firm's visits are now remote or live "
                              '[beMOZDrXOJ8 @ 00:22:34]. Engineered Tax Services pushes the other way, '
                              'saying an in-person visit is worth "a couple hundred bucks" and a virtual '
                              'one is "not ideal" once an examiner shows up, after a free benefit analysis '
                              'turned around in about 24 hours [sXpa52KOvog @ 00:25:23]. The practical '
                              'read: cheap or virtual work trims the fee but shifts risk to the audit '
                              'file, and the hold-versus-sell question decides whether any version is '
                              'worth commissioning.'],
               'table': {'caption': 'Contested Cost Segregation Calls: Side-by-Side Practitioner Playbooks',
                         'headers': ['Contested Question', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How worried should an owner be about depreciation recapture at sale',
                                   'Dennis says they "aren\'t worried" because an IRC 1031 exchange rolls '
                                   'the gain forward',
                                   'Morris calls the study pure deferral; flipping fails while buy, hold '
                                   'and 1031 works',
                                   'Karlton Dennis ([NOA2tGOp9G8 @ 00:16:02]); Advise RE ([8ZzVeQLb80E @ '
                                   '00:04:57])'],
                                  ['What bonus depreciation rate applies to property placed in service '
                                   'during 2026',
                                   'CostSegRx models its $350,000 Sarasota rental at 100 percent bonus for '
                                   'tax year 2026',
                                   'BizCpas states a schedule stepping down 20 points per year to 20 '
                                   'percent in 2026',
                                   'CostSegRx ([Ha5KYCa_Yjk @ 00:00:37]); BizCpas Accountants & Advisors '
                                   '([mKOnV6RitlA @ 00:06:04])'],
                                  ['What rate recaptured depreciation is actually taxed at on exit',
                                   "Perlberg says recapture is taxed at the owner's marginal rate on the "
                                   'sale',
                                   'Harris quotes 25 to 30 percent and treats it as a "zero interest loan"',
                                   'Mark Perlberg, CPA ([3bjz5YCldWA @ 00:22:05]); Commercial Property '
                                   'Advisors ([lJFBf789ODI @ 00:13:26])'],
                                  ['Whether the engineer site visit must be physically in person',
                                   'CSA Partners runs about 70 percent of its site visits remote or live',
                                   'Engineered Tax Services says in person is worth "a couple hundred '
                                   'bucks" and virtual is "not ideal"',
                                   'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ '
                                   '00:22:34]); Engineered Tax Services ([sXpa52KOvog @ 00:25:23])'],
                                  ['How much study depth and fee an operator should pay for',
                                   'Hall teaches a DIY mini study pricing movable items by make and model '
                                   'on eBay',
                                   'Perlberg prices studies from $500 DIY up to $15,000, averaging $3,000 '
                                   'to $6,000',
                                   'Hall CPA | Tax Smart Real Estate Investors ([6eVkkFsis9g @ 00:03:20]); '
                                   'Mark Perlberg, CPA ([3bjz5YCldWA @ 00:21:12])'],
                                  ['Whether a planned sale kills the case for ordering a study',
                                   'Jeff Webb calls a study "a waste of time and money" if you plan to '
                                   'sell',
                                   'Morris says large deals "almost always" get a study, with REP losses '
                                   'carrying forward',
                                   'Toby Mathis Esq | Tax Planning & Asset Protection ([3G2c1STMThk @ '
                                   '00:02:36]); Advise RE ([8ZzVeQLb80E @ 00:05:40])'],
                                  ['Who should actually prepare the cost segregation study for the owner',
                                   'Dennis says a CPA, EA or CTEC plus a licensed engineer is "required by '
                                   'law"',
                                   'Harris says use a specialist firm, not your regular accountant, to '
                                   'avoid aggressive penalties',
                                   'Karlton Dennis ([NOA2tGOp9G8 @ 00:01:58]); Commercial Property '
                                   'Advisors ([lJFBf789ODI @ 00:14:01])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common way a study backfires is a loss with nowhere to land. Clint '
                              'Coons walks through Marcus: $300,000 of W-2 income, a $100,000 study-driven '
                              'loss against $45,000 of rent, leaving a $55,000 loss suspended under '
                              'Section 469. His verdict is flat: "He saved nothing" [fV7tusLGp3E @ '
                              '00:04:59]. LYFE Accounting reports the same trap at scale, describing a '
                              'client now sitting on "hundreds of thousands" of passive losses that sit '
                              'unusable, because passive losses only offset passive income unless the '
                              'owner qualifies as a real estate professional [w16nUKkydYc @ 00:07:57]. '
                              'Brendan Hall spells out the ceiling for non-professionals: a $25,000 '
                              'passive allowance below $100,000 of MAGI, phased out above $150,000, with '
                              'suspended losses carrying forward, while real estate professionals who '
                              'materially participate are unlimited [6eVkkFsis9g @ 00:02:33]. Chris Streit '
                              'builds his whole intake on this, running a two-part test of whether the '
                              'buyer owns income-producing property and whether their tax status lets the '
                              'loss offset all income or only rental and passive income [beMOZDrXOJ8 @ '
                              '00:10:13]. The economics check is simple: before paying a fee, map exactly '
                              'which income the year-one loss will hit, whether through 750-hour '
                              'professional status, the short-term-rental route, or other passive income '
                              'already on the return.',
                              'The second failure mode is buying a study that cannot beat its own fee. '
                              'Stefan Morris runs a Santa Monica purchase at $1 million with $800,000 of '
                              'land: 25 percent of the $200,000 building yields $50,000 of bonus, roughly '
                              '$13,000 to $14,000 of tax impact against a $5,000 to $6,000 study, which he '
                              'calls "not that interesting" [8ZzVeQLb80E @ 00:02:41]. Engineered Tax '
                              'Services flags the same geography problem, noting a California property can '
                              'run 80 percent land, and they push the land number back to the CPA '
                              '[qEFJIGNNOkw @ 00:23:12]. Clint Coons describes Ryan, buying at $180,000 '
                              'with $90,000 of land, who is "barely going to beat the fee" [fV7tusLGp3E @ '
                              '00:10:56]. Bracket is the other half of the math: Coons prices a $10,000 '
                              'deduction at $3,700 for a 37 percent filer but only $1,200 at 12 percent, '
                              'and tells Lisa, who has a business sale coming, to time the study to the '
                              'income arc rather than burn it in a low year [fV7tusLGp3E @ 00:05:56]. '
                              "Morris's counterexample in the High Desert, a $200,000 to $300,000 "
                              'deduction, clears a $5,000 fee easily, which is why the land-to-building '
                              'allocation is the first line of every analysis.',
                              'Audit exposure clusters in a few predictable spots. Chris Streit says land '
                              'value "is the easiest thing for the IRS to deny," because the examiner '
                              'reaches for the county appraisal district, and flat 80/20, 15 percent or 10 '
                              'percent land splits have "lost in less than three minutes" [beMOZDrXOJ8 @ '
                              '00:21:41]. His other red flags are no site visit and no cost methodology '
                              'such as RSMeans, and he warns that some firms now deliver a report in 30 '
                              'minutes without a visit; Toby Mathis adds that cheap reports tend to '
                              '"sandbag" the percentages [beMOZDrXOJ8 @ 00:24:52]. Streit\'s firm runs '
                              'about 5,000 studies a year and sees roughly four or five audits, about one '
                              'in 1,000. Engineered Tax Services claims 99 percent of IDRs close once the '
                              'study is sent, with support through appeals and hourly billing if it goes '
                              'to tax court [qEFJIGNNOkw @ 00:51:34]. The deepest trap is strategic rather '
                              'than technical. Clint Coons says he never does a deal only on the tax side, '
                              'and closes with a three-question filter: can you use the loss this year, '
                              'how long will you hold, and does the deal work without the tax benefit, '
                              '"otherwise you got a bad deal wrapped up in a costume" [fV7tusLGp3E @ '
                              '00:14:49].'],
               'table': {'caption': 'Firsthand Cost Segregation Failure Modes and the Numbers Behind Them',
                         'headers': ['Failure Mode',
                                     'What Happened / Numbers',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Study loss has no income to offset this year',
                                   'Marcus: $300,000 W-2, $100,000 loss, $45,000 rent, $55,000 suspended; '
                                   '"He saved nothing"',
                                   'Confirm REP status, short-term-rental route, or existing passive '
                                   'income before ordering',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([fV7tusLGp3E @ '
                                   '00:04:59])'],
                                  ['Passive losses pile up and sit unusable for years',
                                   'One client holds "hundreds of thousands" in passive losses that cannot '
                                   'offset other income',
                                   'Passive losses only offset passive income unless the owner qualifies '
                                   'as a REPS',
                                   'LYFE Accounting ([w16nUKkydYc @ 00:07:57])'],
                                  ['Study fee eats most of the tax benefit',
                                   'Santa Monica: $800,000 land on $1 million, $13,000 to $14,000 impact '
                                   'versus $5,000 to $6,000 fee',
                                   'Run the land and building allocation first; land-heavy deals are "not '
                                   'that interesting"',
                                   'Advise RE ([8ZzVeQLb80E @ 00:02:41]); Clint Coons Esq. | Real Estate '
                                   'Asset Protection ([fV7tusLGp3E @ 00:10:56])'],
                                  ['Selling early triggers recapture on accelerated depreciation',
                                   '$100,000 at 32 percent plus $50,000 at 25 percent equals $42,500 owed '
                                   'back',
                                   'Fix the hold period or 1031 plan before the study, since 1245 '
                                   'complicates exchanges',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([fV7tusLGp3E @ '
                                   '00:09:03])'],
                                  ['Flat land percentage gets denied under IRS examination',
                                   'Flat 80/20, 15 percent, or 10 percent land splits "lost in less than '
                                   'three minutes"',
                                   'Anchor land to the county appraisal district figure the IRS itself '
                                   'uses',
                                   'Toby Mathis Esq | Tax Planning & Asset Protection ([beMOZDrXOJ8 @ '
                                   '00:21:41])'],
                                  ['Deduction burned in a low tax bracket year',
                                   'A $10,000 deduction is worth $3,700 at 37 percent versus only $1,200 '
                                   'at 12 percent',
                                   'Time the study to the income arc, such as a coming business sale',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([fV7tusLGp3E @ '
                                   '00:05:56])'],
                                  ['Aggressive or misclassified components create penalty and compliance '
                                   'exposure',
                                   'AirDNA warns misclassification creates compliance issues; Harris flags '
                                   'penalties if too aggressive',
                                   'Use a cost segregation specialist rather than a generalist accountant '
                                   'for the report',
                                   'AirDNA ([nj5gSNmRQuU @ 00:04:25]); Commercial Property Advisors '
                                   '([lJFBf789ODI @ 00:14:01])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before Paying for a Study',
                           'body': 'Practitioners who watched studies backfire run every deal through the '
                                   'same four checks: usable income, defensible land value, fee coverage, '
                                   'and the exit.',
                           'items': ["Map the year-one loss to income you can actually offset; Marcus's "
                                     '$55,000 loss was suspended and "He saved nothing" [Clint Coons Esq. '
                                     '| Real Estate Asset Protection — fV7tusLGp3E @ 00:04:59].',
                                     'Pull land value from the county appraisal district; flat 80/20, 15 '
                                     'percent, or 10 percent splits "lost in less than three minutes" '
                                     '[Toby Mathis Esq | Tax Planning & Asset Protection — beMOZDrXOJ8 @ '
                                     '00:21:41].',
                                     'Kill the study if tax impact barely clears the fee, as with $13,000 '
                                     'to $14,000 of impact against a $5,000 to $6,000 study in Santa '
                                     'Monica [Advise RE — 8ZzVeQLb80E @ 00:02:41].',
                                     'Model the exit first: an early sale handed back $42,500 in recapture '
                                     'on $150,000 of depreciation [Clint Coons Esq. | Real Estate Asset '
                                     'Protection — fV7tusLGp3E @ 00:09:03].']}}],
 'pull_quote': '"I never do a deal only based upon the tax side of it. Otherwise you got a bad deal '
               'wrapped up in a costume." Clint Coons Esq. | Real Estate Asset Protection (fV7tusLGp3E @ '
               '00:14:49).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Start every analysis with the land and building allocation, because it depends on '
                      'facts and circumstances and drives whether the study pays [Advise RE — 8ZzVeQLb80E '
                      '@ 00:00:26].',
                      'Back land out per the county tax records before calculating basis, as on the '
                      '$750,000 commercial example with 20 percent land [CostSegRx — IFbN2m1Gw3Y @ '
                      '00:00:00].',
                      'Confirm tax status first: 750 hours and 50 percent of work time for REP, or a '
                      'seven-day-or-less average stay for the short-term-rental route [Mark Perlberg, CPA '
                      '— 3bjz5YCldWA @ 00:09:37].',
                      'Order the free benefit analysis, then insist on a site visit and documented cost '
                      'methodology so the report holds under audit [Engineered Tax Services — sXpa52KOvog '
                      '@ 00:25:23].',
                      'Apply the study to the open year through the extension in September or October with '
                      'no amendment, which Streit says is "not a red flag" [Toby Mathis Esq | Tax Planning '
                      '& Asset Protection — beMOZDrXOJ8 @ 00:12:33].',
                      'Plan the exit by identifying removed assets, which carry no recapture, and lining '
                      'up a 1031 or "slow 1031" [Engineered Tax Services — sXpa52KOvog @ 00:16:56].'],
 'statutory_citations': [{'title': 'Clint Coons Esq. | Real Estate Asset Protection — Why Cost Segregation '
                                   'Can Be A BAD Idea [00:04:59]',
                          'url': 'https://www.youtube.com/watch?v=fV7tusLGp3E&t=299s',
                          'relevance': 'Primary practitioner testimony on suspended passive losses, '
                                       'early-sale recapture, fee-versus-benefit and the three-question '
                                       'filter.'},
                         {'title': 'Toby Mathis Esq | Tax Planning & Asset Protection — How To Do A Cost '
                                   'Segregation Study: When It Saves You Money And When It Doesn’t '
                                   '[00:21:41]',
                          'url': 'https://www.youtube.com/watch?v=beMOZDrXOJ8&t=1301s',
                          'relevance': 'Primary practitioner testimony on land value audit losses, site '
                                       'visit red flags, cost methodology and audit frequency.'},
                         {'title': 'Advise RE — When a Cost Segregation Study Is Actually Worth It 💡 '
                                   '[00:02:41]',
                          'url': 'https://www.youtube.com/watch?v=8ZzVeQLb80E&t=161s',
                          'relevance': 'Primary practitioner testimony on land-heavy deals failing to beat '
                                       'the study fee and cost segregation as deferral.'},
                         {'title': 'Engineered Tax Services — Webinar: Cost Segregation Deep Dive & '
                                   'Referral Process - August 27 [00:22:13]',
                          'url': 'https://www.youtube.com/watch?v=qEFJIGNNOkw&t=1333s',
                          'relevance': 'Primary practitioner testimony on bonus phase-down dates, land '
                                       'value pushed to the CPA and IDR audit outcomes.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'IFbN2m1Gw3Y',
                       'title': 'Cost Segregation Example: $750K Commercial Property Tax Savings (2026)',
                       'channel': 'CostSegRx',
                       'author': 'CostSegRx',
                       'text': 'At a 24% tax rate, the savings come to $25,921 dollar-for-dollar.',
                       'tip': 'At a 24% tax rate, the savings come to $25,921 dollar-for-dollar.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=IFbN2m1Gw3Y&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=IFbN2m1Gw3Y&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qEFJIGNNOkw',
                       'title': 'Webinar: Cost Segregation Deep Dive & Referral Process - August 27',
                       'channel': 'Engineered Tax Services',
                       'author': 'Engineered Tax Services',
                       'text': 'Um, so just be aware that not everything qualifies for 100% bonus.',
                       'tip': 'Um, so just be aware that not everything qualifies for 100% bonus.',
                       'timestamp': 1375,
                       'timestamp_seconds': 1375,
                       'timestamp_label': '[00:22:55]',
                       'url': 'https://www.youtube.com/watch?v=qEFJIGNNOkw&t=1375s',
                       'markdown': '[00:22:55](https://www.youtube.com/watch?v=qEFJIGNNOkw&t=1375s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sXpa52KOvog',
                       'title': 'Webinar: Cost Segregation for Real Estate Professionals',
                       'channel': 'Engineered Tax Services',
                       'author': 'Engineered Tax Services',
                       'text': 'So we can help mitigate that by identifying all the different assets and '
                               "what gets removed, because there's no recapture on assets that are removed "
                               'from the property.',
                       'tip': 'So we can help mitigate that by identifying all the different assets and '
                              "what gets removed, because there's no recapture on assets that are removed "
                              'from the property.',
                       'timestamp': 1016,
                       'timestamp_seconds': 1016,
                       'timestamp_label': '[00:16:56]',
                       'url': 'https://www.youtube.com/watch?v=sXpa52KOvog&t=1016s',
                       'markdown': '[00:16:56](https://www.youtube.com/watch?v=sXpa52KOvog&t=1016s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'w16nUKkydYc',
                       'title': 'CPA Explains The #1 Real Estate Tax Deduction: Cost Segregation Explained',
                       'channel': 'LYFE Accounting',
                       'author': 'LYFE Accounting',
                       'text': 'Over the last 20 years, bonus depreciation has fluctuated from 30% to '
                               '100%.',
                       'tip': 'Over the last 20 years, bonus depreciation has fluctuated from 30% to 100%.',
                       'timestamp': 320,
                       'timestamp_seconds': 320,
                       'timestamp_label': '[00:05:20]',
                       'url': 'https://www.youtube.com/watch?v=w16nUKkydYc&t=320s',
                       'markdown': '[00:05:20](https://www.youtube.com/watch?v=w16nUKkydYc&t=320s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3G2c1STMThk',
                       'title': 'Cost Segregation Study - Bonus Accelerated Depreciation (BIG Tax Cuts Job '
                                'Act CHANGES)',
                       'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'text': 'In the Tax Cuts and Jobs Act, they gave us bonus depreciation.',
                       'tip': 'In the Tax Cuts and Jobs Act, they gave us bonus depreciation.',
                       'timestamp': 67,
                       'timestamp_seconds': 67,
                       'timestamp_label': '[00:01:07]',
                       'url': 'https://www.youtube.com/watch?v=3G2c1STMThk&t=67s',
                       'markdown': '[00:01:07](https://www.youtube.com/watch?v=3G2c1STMThk&t=67s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dCExXUUA6zA',
                       'title': 'Real Estate Cost Segregation Example',
                       'channel': 'C2 Realty Group',
                       'author': 'C2 Realty Group',
                       'text': 'With $2,000 a month in rent less expenses, cost segregation turns $13,120 '
                               'of taxable income into a loss of about $9,308 that a real estate '
                               'professional can apply to other income.',
                       'tip': 'With $2,000 a month in rent less expenses, cost segregation turns $13,120 '
                              'of taxable income into a loss of about $9,308 that a real estate '
                              'professional can apply to other income.',
                       'timestamp': 111,
                       'timestamp_seconds': 111,
                       'timestamp_label': '[00:01:51]',
                       'url': 'https://www.youtube.com/watch?v=dCExXUUA6zA&t=111s',
                       'markdown': '[00:01:51](https://www.youtube.com/watch?v=dCExXUUA6zA&t=111s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NOA2tGOp9G8',
                       'title': 'Inside My Real Cost Segregation Study (What Actually Happened)',
                       'channel': 'Karlton Dennis',
                       'author': 'Karlton Dennis',
                       'text': 'By choosing to do a cost segregation study on this property, I received '
                               '93,505 dollars in year one depreciation.',
                       'tip': 'By choosing to do a cost segregation study on this property, I received '
                              '93,505 dollars in year one depreciation.',
                       'timestamp': 825,
                       'timestamp_seconds': 825,
                       'timestamp_label': '[00:13:45]',
                       'url': 'https://www.youtube.com/watch?v=NOA2tGOp9G8&t=825s',
                       'markdown': '[00:13:45](https://www.youtube.com/watch?v=NOA2tGOp9G8&t=825s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nj5gSNmRQuU',
                       'title': 'Cost Segregation for Airbnb Hosts: The Tax Strategy That Saves Thousands',
                       'channel': 'AirDNA',
                       'author': 'AirDNA',
                       'text': "To do this right, you'll want to work with a tax adviser who specializes "
                               'in cost segregation.',
                       'tip': "To do this right, you'll want to work with a tax adviser who specializes in "
                              'cost segregation.',
                       'timestamp': 265,
                       'timestamp_seconds': 265,
                       'timestamp_label': '[00:04:25]',
                       'url': 'https://www.youtube.com/watch?v=nj5gSNmRQuU&t=265s',
                       'markdown': '[00:04:25](https://www.youtube.com/watch?v=nj5gSNmRQuU&t=265s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'beMOZDrXOJ8',
                       'title': 'How To Do A Cost Segregation Study: When It Saves You Money And When It '
                                'Doesn’t',
                       'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'text': 'There are firms right now who can give you a report in 30 minutes with no '
                               'site visit.',
                       'tip': 'There are firms right now who can give you a report in 30 minutes with no '
                              'site visit.',
                       'timestamp': 1385,
                       'timestamp_seconds': 1385,
                       'timestamp_label': '[00:23:05]',
                       'url': 'https://www.youtube.com/watch?v=beMOZDrXOJ8&t=1385s',
                       'markdown': '[00:23:05](https://www.youtube.com/watch?v=beMOZDrXOJ8&t=1385s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'beMOZDrXOJ8',
                       'title': 'How To Do A Cost Segregation Study: When It Saves You Money And When It '
                                'Doesn’t',
                       'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
                       'text': 'It is the easiest thing for the IRS to deny.',
                       'tip': 'It is the easiest thing for the IRS to deny.',
                       'timestamp': 1274,
                       'timestamp_seconds': 1274,
                       'timestamp_label': '[00:21:14]',
                       'url': 'https://www.youtube.com/watch?v=beMOZDrXOJ8&t=1274s',
                       'markdown': '[00:21:14](https://www.youtube.com/watch?v=beMOZDrXOJ8&t=1274s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3bjz5YCldWA',
                       'title': 'What is Cost Segregation, and When do I do a Cost Segregation Study?',
                       'channel': 'Mark Perlberg, CPA',
                       'author': 'Mark Perlberg, CPA',
                       'text': "Your best rule of thumb that we've seen after seeing hundreds of cost "
                               "segregation studies is if it's a long-term rental, we ballpark 25% of the "
                               'purchase price.',
                       'tip': "Your best rule of thumb that we've seen after seeing hundreds of cost "
                              "segregation studies is if it's a long-term rental, we ballpark 25% of the "
                              'purchase price.',
                       'timestamp': 1067,
                       'timestamp_seconds': 1067,
                       'timestamp_label': '[00:17:47]',
                       'url': 'https://www.youtube.com/watch?v=3bjz5YCldWA&t=1067s',
                       'markdown': '[00:17:47](https://www.youtube.com/watch?v=3bjz5YCldWA&t=1067s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6eVkkFsis9g',
                       'title': 'Cost Segregation Studies Explained',
                       'channel': 'Hall CPA | Tax Smart Real Estate Investors',
                       'author': 'Hall CPA | Tax Smart Real Estate Investors',
                       'text': 'You can do a mini study yourself by pricing movable items by make and '
                               "model on eBay, but the results won't be near as good.",
                       'tip': 'You can do a mini study yourself by pricing movable items by make and model '
                              "on eBay, but the results won't be near as good.",
                       'timestamp': 200,
                       'timestamp_seconds': 200,
                       'timestamp_label': '[00:03:20]',
                       'url': 'https://www.youtube.com/watch?v=6eVkkFsis9g&t=200s',
                       'markdown': '[00:03:20](https://www.youtube.com/watch?v=6eVkkFsis9g&t=200s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fV7tusLGp3E',
                       'title': 'Why Cost Segregation Can Be A BAD Idea',
                       'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'author': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'text': 'Otherwise you got a bad deal wrapped up in a costume.',
                       'tip': 'Otherwise you got a bad deal wrapped up in a costume.',
                       'timestamp': 889,
                       'timestamp_seconds': 889,
                       'timestamp_label': '[00:14:49]',
                       'url': 'https://www.youtube.com/watch?v=fV7tusLGp3E&t=889s',
                       'markdown': '[00:14:49](https://www.youtube.com/watch?v=fV7tusLGp3E&t=889s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fV7tusLGp3E',
                       'title': 'Why Cost Segregation Can Be A BAD Idea',
                       'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'author': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'text': 'I never do a deal only based upon the tax side of it.',
                       'tip': 'I never do a deal only based upon the tax side of it.',
                       'timestamp': 857,
                       'timestamp_seconds': 857,
                       'timestamp_label': '[00:14:17]',
                       'url': 'https://www.youtube.com/watch?v=fV7tusLGp3E&t=857s',
                       'markdown': '[00:14:17](https://www.youtube.com/watch?v=fV7tusLGp3E&t=857s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ha5KYCa_Yjk',
                       'title': 'Cost Segregation Example: $350K Rental Property Tax Savings (2026)',
                       'channel': 'CostSegRx',
                       'author': 'CostSegRx',
                       'text': 'Below that, you can see the bonus rate is at 100% for tax year 2026 and '
                               'our estimated accelerated depreciation is $46,200.',
                       'tip': 'Below that, you can see the bonus rate is at 100% for tax year 2026 and our '
                              'estimated accelerated depreciation is $46,200.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=Ha5KYCa_Yjk&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=Ha5KYCa_Yjk&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8ZzVeQLb80E',
                       'title': 'When a Cost Segregation Study Is Actually Worth It 💡',
                       'channel': 'Advise RE',
                       'author': 'Advise RE',
                       'text': 'It is a tax deferral strategy.',
                       'tip': 'It is a tax deferral strategy.',
                       'timestamp': 254,
                       'timestamp_seconds': 254,
                       'timestamp_label': '[00:04:14]',
                       'url': 'https://www.youtube.com/watch?v=8ZzVeQLb80E&t=254s',
                       'markdown': '[00:04:14](https://www.youtube.com/watch?v=8ZzVeQLb80E&t=254s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lJFBf789ODI',
                       'title': 'Cost Segregation Made Simple',
                       'channel': 'Commercial Property Advisors',
                       'author': 'Commercial Property Advisors',
                       'text': 'Recapture comes back at 25 to 30 percent, but I look at it as a zero '
                               'interest loan.',
                       'tip': 'Recapture comes back at 25 to 30 percent, but I look at it as a zero '
                              'interest loan.',
                       'timestamp': 806,
                       'timestamp_seconds': 806,
                       'timestamp_label': '[00:13:26]',
                       'url': 'https://www.youtube.com/watch?v=lJFBf789ODI&t=806s',
                       'markdown': '[00:13:26](https://www.youtube.com/watch?v=lJFBf789ODI&t=806s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mKOnV6RitlA',
                       'title': 'Cost Segregation Analysis Explained: How Real Estate Investors Save '
                                '$45,000+ in Taxes Legally',
                       'channel': 'BizCpas Accountants & Advisors',
                       'author': 'BizCpas Accountants & Advisors',
                       'text': 'With the study, year one depreciation totals about $86,000, roughly four '
                               'times the standard amount, for $31,853 in first-year savings.',
                       'tip': 'With the study, year one depreciation totals about $86,000, roughly four '
                              'times the standard amount, for $31,853 in first-year savings.',
                       'timestamp': 254,
                       'timestamp_seconds': 254,
                       'timestamp_label': '[00:04:14]',
                       'url': 'https://www.youtube.com/watch?v=mKOnV6RitlA&t=254s',
                       'markdown': '[00:04:14](https://www.youtube.com/watch?v=mKOnV6RitlA&t=254s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
