from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'decline-curves-well-performance-mineral-valuation',
 'question_prompt': 'Why do royalty checks decline, and how do decline curves, type curves and well '
                    'performance drive mineral value?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Decline Curves, Well Performance and Mineral Valuation',
 'subtitle': 'Life of a well, decline curve analysis in Danomics and Citrine, economic rate with oil and '
             'gas streams, type curves, shale performance drivers, Haynesville top wells, drilling costs, '
             'negative gas prices, royalty economics, and how activity drives mineral value',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree that modern shale wells front-load their value. Steven Hatcher '
                      'says 70-80% of volume comes in the first two years, Mr. Business models a 60-70% '
                      'first-year decline, and Troy Eckard warns that the first royalty check bundles one '
                      'to five months of production. The street toolkit is Arps-style decline curve '
                      'analysis: hyperbolic fits with b capped near 1.3, exponential tails around 8%, '
                      'flowback excluded, and economic limits solved where revenue equals operating cost. '
                      'TopDogEngineer used that method to reach 140.3 bbl/month. Valuation layers price '
                      "and development timing on the curve, from Matt Sands's 50-70x three-month-royalty "
                      'multiple up to full NPV10 builds. Disagreements center on three questions: whether '
                      'to fit an average type curve or each well, whether type curves are useful for PDP, '
                      'and how far auction comps can be trusted.',
 'key_metrics': [{'label': 'Shale two-year recovery share',
                  'metric': 'Shale two-year recovery share',
                  'value': '70-80% of total well volume within the first two years of production',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Hatcher's rule of thumb for shale wells. He uses it to explain why mineral "
                             'value peaks in the months right after first production.',
                  'source': 'Steven Hatcher | Minerals Guy ([CiR-w5lHfvI @ 00:11:46])'},
                 {'label': 'Producing royalty valuation multiple',
                  'metric': 'Producing royalty valuation multiple',
                  'value': '50-70x the average of the last 3 months of royalty, up to 100x in hot areas',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sands's quick rule of thumb for valuing mature producing mineral assets "
                             'before a full engineering valuation is run.',
                  'source': 'Matt Sands ([86mQK92f7Bg @ 00:29:36])'},
                 {'label': 'DIY decline fit constraints',
                  'metric': 'DIY decline fit constraints',
                  'value': 'b-factor below 1.3 with an 8% terminal decline',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sands's settings for a one-month Well Database DIY forecast exported to "
                             'Excel. He calls 8% a good conservative number for most wells.',
                  'source': 'Matt Sands ([VYytHJ0lMVw @ 00:38:39])'},
                 {'label': 'Economic limit rate',
                  'metric': 'Economic limit rate',
                  'value': '140.3 bbl/month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Breakeven oil rate from a Solver run on q*Poil + q*GOR*Pgas - OpEx = 0, '
                             'using a net gas price of about $2.067/Mcf. Below this rate the well loses '
                             'money.',
                  'source': 'TopDogEngineer ([4mzbNb16NQc @ 00:08:25])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner who talks about well performance describes the same '
                              'shape: the money arrives early and the curve bends hard. Troy Eckard '
                              'contrasts the shale era with vintage wells that started near 400 bbl/day '
                              'and bled down to 25-50 bbl/day by roughly year 14. Modern high-IP wells let '
                              'the operator target payback inside 36 months and then fund wells #2-5 on '
                              'the same pad [nn1juJ3_-WA @ 00:05:58]. Steven Hatcher gives the rule of '
                              'thumb that a shale well recovers 70 to 80 percent of its total volume '
                              'within the first two years of production [CiR-w5lHfvI @ 00:11:46]. The '
                              'Crude Files puts a number on a single Midland well: it peaks around 730 '
                              "bbl/d and drops more than 70% inside year one. The channel's summary is "
                              "'the money is spent at the start, the oil comes fast, and then slows' "
                              '[R-AasPj-Y5E @ 00:14:43]. Mr. Business pegs first-year decline at 60-70%, '
                              'followed by several percent per year, and calls horizontal shale wells '
                              "'especially dramatic' [hIerB5MQ52U @ 00:11:25]. The consequence for the "
                              'owner is the first-check trap. Eckard warns that the first check covers one '
                              'to five months of production and lands about six months after start. The '
                              'next check covers a single month, so it can look like a third or a sixth of '
                              'the first.',
                              'The second point of agreement is that decline curve analysis is a '
                              "forecasting method, not a guess. Matt Sands says the process works 'no "
                              "matter what type of well' and applies to roughly 95% of wells. The "
                              'exceptions are enhanced recovery such as waterflood or CO2, pipeline '
                              'curtailment, and flat water-drive production [VYytHJ0lMVw @ 00:06:59]. He '
                              'traces the method from Arps in 1945 to Fetkovich in the 1980s. The working '
                              'shape is a two-part fit: hyperbolic early, then an exponential tail at '
                              '8-15% per year, read on a semi-log scale. Francis Ramos II insists on a '
                              'diagnostic check before any exponential math. Rate versus cumulative '
                              'production should plot as a straight line, and rate versus time on a '
                              'semi-log plot should be a straight line with a similar slope. A plain '
                              "linear rate-time chart 'doesn't really tell you' whether the decline is "
                              'exponential [u3kTgNXLIGI @ 00:02:28]. Once the decline is confirmed, he '
                              "says you can estimate cumulative production 'without even drilling the "
                              "well.' Mergers & Inquisitions defines the type curve as initial production "
                              'plus its decline. In its model, that curve drives the revenue, expense, and '
                              'capex estimates for each well, and the wells are then aggregated with '
                              'OFFSET [2tJpxiIqFSM @ 00:01:00]. All three treat the decline curve as the '
                              'foundation for every number that follows.',
                              'On valuation, the consensus is that a decline curve is worthless until '
                              "price and timing are layered on top. Steven Hatcher compresses it to 'high "
                              "prices plus High activity equals high value.' He argues that undeveloped "
                              'minerals carry zero value until development is in sight, and that value '
                              'peaks in the months after first production [CiR-w5lHfvI @ 00:00:48]. In his '
                              'valuation episode, Matt Sands lays out the income, or engineering, '
                              'approach: pick analog wells, adjust for one- or two-mile laterals, build a '
                              'type curve, apply spacing and timing, and compute NPV [86mQK92f7Bg @ '
                              '00:15:30]. In a later episode he adds that value scales roughly linearly '
                              'with price. Moving the price deck from $60 to $80 lifts value about 1.3x, '
                              'and dropping from $80 to $60 leaves about 75% [VYytHJ0lMVw @ 00:33:18]. Mr. '
                              'Business warns that a $2,000 check from a six-month-old well overstates '
                              'future income. That is why professionals run decline curve analysis and '
                              'PV10 and apply a discount to undrilled locations [8gaFGCKNpnk @ 00:12:28]. '
                              'Without the curve, the number on the check tells an owner little about '
                              'future income. With the curve, a price deck, and a development timeline, it '
                              'becomes a defensible valuation.'],
               'table': {'caption': 'Where the practitioners agree on decline and value',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Shale production is heavily front-loaded',
                                   'A shale well recovers 70 to 80 percent of its total volume within the '
                                   'first two years',
                                   'Peak mineral value sits in the months right after first production '
                                   'starts',
                                   'Steven Hatcher | Minerals Guy ([CiR-w5lHfvI @ 00:11:46])'],
                                  ['First-year decline is brutal',
                                   'A Midland well peaks near 730 bbl/d, then falls more than 70% inside '
                                   'year one',
                                   'Never annualize early production rates when judging an offer or a '
                                   'budget',
                                   'The Crude Files ([R-AasPj-Y5E @ 00:14:27])'],
                                  ['The first royalty check is inflated',
                                   'The first check covers one to five months and arrives about six months '
                                   'after start',
                                   'Expect the next single-month check to be roughly a third or a sixth as '
                                   'large',
                                   'Eckard Enterprises | Oil & Gas Investing ([nn1juJ3_-WA @ 00:07:50])'],
                                  ['Decline curve analysis applies to most wells',
                                   'It fits roughly 95% of wells; the exceptions are waterflood, CO2, '
                                   'curtailment, and water drive',
                                   'Flag enhanced-recovery and curtailed wells before trusting any fitted '
                                   'curve',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:06:59])'],
                                  ['Confirm exponential decline before using the exponential equations',
                                   'Rate versus cumulative production must plot as a straight line before '
                                   'the exponential decline equations apply',
                                   'Run both diagnostic plots, because a linear rate-time chart alone does '
                                   'not show whether decline is exponential',
                                   'Francis Ramos II ([u3kTgNXLIGI @ 00:02:28])'],
                                  ['A royalty is a depleting asset',
                                   'More than 45% of a five-year royalty total arrived in year one alone',
                                   'Treat royalty income as a depleting asset rather than as a steady '
                                   'salary',
                                   'Mr. Business ([hIerB5MQ52U @ 00:10:06])'],
                                  ['Price plus activity sets value',
                                   'Undeveloped minerals carry zero value until line of sight to '
                                   'development appears',
                                   'Track permits and rigs within two to three miles to gauge development '
                                   'timing',
                                   'Steven Hatcher | Minerals Guy ([CiR-w5lHfvI @ 00:09:31])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The fitting work is done in software, within set constraints. Matt Sands '
                              'describes the two levers: initial decline sets the steepness, and the '
                              'b-factor sets the bend, usually between 0 and 2. A b of 1 is harmonic '
                              'decline, and a b of 0 is exponential [VYytHJ0lMVw @ 00:19:57]. For a DIY '
                              'run he points to Well Database on a one-month subscription. He caps b below '
                              '1.3 and sets an 8% terminal decline, then exports to Excel and multiplies '
                              "by the owner's decimal interest. He calls 8% 'a good conservative number "
                              "for most wells.' Danomics applies a similar constraint set in its Flows "
                              'tool: Di left open, b bounded at 0-1.3, and a qi factor of 2x the maximum '
                              "observed rate. On the 1.3 bound, the presenter adds, 'I'm not saying that "
                              "is the correct value.' The tool declines roughly 4,000 wells in seconds and "
                              'exports qi, Di, and b to CSV [gleafhkBQWg @ 00:03:45]. The choice of start '
                              'method matters. Max is the default, First decline handles capacity-limited, '
                              'choked gas wells, and Best fit suits late-time PDP packages. KAPPA '
                              "Engineering's CITRINE excludes early flowback before fitting and weights "
                              'rate against cumulative production in the regression objective. It then '
                              'compares hyperbolic, Duong, and power-law exponential fits side by side to '
                              'bracket an EUR range and exports the results in an Aries-compatible format '
                              '[tPB4O0ryZww @ 00:03:47].',
                              'Where the curve ends is an economics question, not a geology one. '
                              'TopDogEngineer defines breakeven as oil rate times oil price, plus oil rate '
                              'times GOR times gas price, minus operating cost, equals zero. He derives '
                              'GOR from the derivative of cumulative gas with respect to cumulative oil, '
                              'substitutes the Arps cumulative equation, and solves with Excel Solver '
                              '[4mzbNb16NQc @ 00:03:24]. He starts from a $3.35 gas price, multiplies it '
                              'by a 7/8 NRI, and subtracts severance and ad valorem taxes, for a net of '
                              'about $2.067 per Mcf. The run lands on an economic rate of 140.3 bbl/month; '
                              "below that rate, in his words, 'we're losing money' [4mzbNb16NQc @ "
                              '00:08:25]. Mergers & Inquisitions builds the forward model in Excel. Inputs '
                              'are a 10 MMcfe/d IP, a 60% initial decline, and a hyperbolic formula with a '
                              'log-based D factor. Decline is set to MAX(formula, terminal) so it never '
                              'drops below 5%. Production is set to MIN(prior production times one minus '
                              'decline, EUR minus cumulative), for a total of 14.25 Bcfe [2tJpxiIqFSM @ '
                              '00:06:44]. With $4.7M of D&C capex, his version produced a 113% IRR and a '
                              "$15M NPV10. The company's own figures were 124% and $6.3M, and he "
                              'attributes the gap to a different curve shape [2tJpxiIqFSM @ 00:15:17]. A '
                              'different bend gives a very different answer.',
                              'The royalty-side arithmetic is just as mechanical. Mr. Business walks '
                              'through a check. Ten net mineral acres in a 640-acre unit is 1.5625%; at a '
                              '20% royalty, that gives a 0.3125% NRI. Ninety thousand barrels at $70 '
                              'grosses $6.3M, so the owner receives about $19,700, or roughly $18,500 '
                              'after an assumed 5-6% in combined taxes [8gaFGCKNpnk @ 00:07:11]. Applying '
                              'his decline of 90k, 48k, 35k, 28k, and 24k barrels, five years total about '
                              '$49k gross, with more than 40% of it in year one. Matt Sands gives a '
                              'shortcut for mature producing assets: average the last three months of '
                              'royalty and multiply by 50-70x, or up to 100x in hot areas. He prices a '
                              'full engineering valuation at 2-4 hours of work, about $400-800 '
                              '[86mQK92f7Bg @ 00:29:36]. In his example, a $10-15k per acre offer on 5 '
                              'acres might really be worth $20-30k per acre. ComboCurve screened the '
                              'Haynesville down to 2,022 wells that passed its vintage, lateral, proppant, '
                              'and production filters. The medians were a b of 0.94, a Di of 59, payout in '
                              '19 months at flat $70/$3.25, an NPV10 of $5.8 million, and an IRR of 52% '
                              "[k4f-XlIpXZU @ 00:19:20]. Those medians are benchmarks a buyer's offer can "
                              'be measured against before anyone signs.'],
               'table': {'caption': 'Street numbers and tool settings for decline and valuation work',
                         'headers': ['Lever or Tool',
                                     'Setting or Number',
                                     'How It Is Used',
                                     'Expert Source'],
                         'rows': [['Well Database DIY forecast',
                                   'b below 1.3, 8% terminal decline, one-month subscription',
                                   'Export the forecast to Excel and multiply it by your decimal interest',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:38:39])'],
                                  ['Danomics Flows constraints',
                                   'b bounded at 0-1.3, Di left open, qi factor of 2x the max rate',
                                   'Auto-declines about 4,000 wells in seconds and exports qi, Di, and b '
                                   'to CSV',
                                   'Danomics ([gleafhkBQWg @ 00:03:45])'],
                                  ['KAPPA CITRINE model set',
                                   'Hyperbolic, Duong, power-law exponential, stretched exponential, '
                                   'logistic growth, SRV bounded',
                                   'Compare the model fits side by side to set a defensible EUR range',
                                   'KAPPA Engineering ([tPB4O0ryZww @ 00:01:30])'],
                                  ['Economic rate solve in Excel',
                                   'Net gas of $2.067/Mcf after the 7/8 NRI and taxes, giving 140.3 '
                                   'bbl/month',
                                   'Stop producing below this rate because the well is losing money',
                                   'TopDogEngineer ([4mzbNb16NQc @ 00:08:25])'],
                                  ['Excel type-curve build',
                                   '10 MMcfe/d IP, 60% initial decline, 5% terminal floor, 14.25 Bcfe '
                                   'total',
                                   'Drives revenue, LOE, and capex; this build produced a 113% IRR and a '
                                   '$15M NPV10',
                                   'Mergers & Inquisitions / Breaking Into Wall Street ([2tJpxiIqFSM @ '
                                   '00:06:44])'],
                                  ['Producing royalty multiple',
                                   'Average of the last three months of royalty times 50-70x, up to 100x '
                                   'in hot areas',
                                   'Quick sanity check on buyer offers for mature producing mineral assets',
                                   'Matt Sands ([86mQK92f7Bg @ 00:29:36])'],
                                  ['Haynesville well benchmark',
                                   'Median b of 0.94, Di of 59, 19-month payout, NPV10 of $5.8M, IRR of '
                                   '52%',
                                   'Benchmark drawn from 2,022 wells that passed the vintage, lateral, and '
                                   'production filters',
                                   'ComboCurve ([k4f-XlIpXZU @ 00:19:20])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Clean the Fit Before You Trust Any Number',
                           'body': 'The curve is only as good as the data window and constraints behind '
                                   'it. These are the settings and checks the practitioners apply before a '
                                   'forecast reaches a valuation.',
                           'items': ['Use the First decline start method for capacity-limited, choked gas '
                                     'wells instead of the default Max start [Danomics — gleafhkBQWg @ '
                                     '00:03:04]',
                                     'Move the start-time marker to exclude early flowback data before '
                                     'running any hyperbolic regression [KAPPA Engineering — tPB4O0ryZww @ '
                                     '00:01:54]',
                                     'Wait for 18-24 months of unrestricted production data before relying '
                                     "on a well's own fitted curve [Matt Sands — VYytHJ0lMVw @ 00:35:19]",
                                     'Confirm that rate versus cumulative production plots linear before '
                                     'applying exponential decline equations to the well [Francis Ramos II '
                                     '— u3kTgNXLIGI @ 00:02:28]']},
               'sop_steps': [{'step': 1,
                              'title': 'Classify and locate the minerals',
                              'action': 'Sort the interest into producing or non-producing, then pull '
                                        'wells and permits by legal description.',
                              'detail': 'Sands makes this step one: check the state oil and gas commission '
                                        'map for permits and wells on your legal description before any '
                                        'valuation work [Matt Sands — 86mQK92f7Bg @ 00:08:33]'},
                             {'step': 2,
                              'title': 'Fit a constrained decline curve',
                              'action': 'Fit a hyperbolic curve with b below 1.3 and an 8% terminal '
                                        'decline, then export the forecast to Excel.',
                              'detail': 'Use a one-month Well Database subscription, export to Excel, and '
                                        'multiply the forecast by your decimal interest to get owner '
                                        'volumes [Matt Sands — VYytHJ0lMVw @ 00:38:39]'},
                             {'step': 3,
                              'title': 'Solve the economic limit',
                              'action': 'Set revenue net of NRI and taxes minus operating cost equal to '
                                        'zero and solve for the cutoff rate.',
                              'detail': 'Excel Solver landed on 140.3 bbl/month for this example; '
                                        'production below that rate loses money and should stop '
                                        '[TopDogEngineer — 4mzbNb16NQc @ 00:08:25]'},
                             {'step': 4,
                              'title': 'Price the forecast and sanity-check',
                              'action': 'Run the forecast against a price deck, then cross-check the '
                                        'result with the 50-70x three-month royalty multiple.',
                              'detail': 'Choose the NYMEX 10-year strip, a bank deck, the SEC 12-month '
                                        'average, or a flat $60, knowing value moves roughly linearly with '
                                        'price [Matt Sands — VYytHJ0lMVw @ 00:32:06]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Troy W. Eckard of Eckard Enterprises frames steep shale decline as a gift. '
                              'Wells that once crawled along at 50 to 100 BOE per day now open at high '
                              'rates, and operators target payback inside 36 months. Eckard tells owners '
                              'it is not a negative that wells decline but a positive that they start so '
                              'high, with wells predicted to last 50 to 75 years after the hyperbolic '
                              'leveling-off [nn1juJ3_-WA @ 00:10:01]. Mr. Business runs the same numbers '
                              'colder. In their five-year example, more than 45% of total royalty income '
                              'lands in year one and first-year decline runs 60 to 70%, so the operating '
                              'rule is that a royalty is not a salary but a depleting asset [hIerB5MQ52U @ '
                              '00:12:19]. Steven Hatcher splits the difference for sellers. Peak value '
                              'sits in the months right after first production, because a shale well '
                              'recovers 70 to 80% of its volume in its first two years, while a '
                              'pre-production sale trades a lower price for dumping development risk on '
                              'the buyer [CiR-w5lHfvI @ 00:11:46]. Matt Sands lands on the opposite side '
                              'of the sell trigger: hold unless the cash is needed now, and when it is, '
                              'carve out an NPRI or sell any slice from 1% to 100% rather than the whole '
                              'estate [86mQK92f7Bg @ 00:31:06].',
                              'With no Zillow for minerals and most sale prices undisclosed, Justin '
                              "Williams, the West Texas inheritor on Matt Sands' show, calls the market "
                              "approach the preferred method. Pull arm's-length comps from auction sites "
                              'like EnergyNet and normalize everything to price per net mineral acre, the '
                              'mineral version of price per square foot [86mQK92f7Bg @ 00:13:00]. Sands '
                              'pushes back hard. Auction fever makes bidders overpay or underpay, a '
                              'credible comp set needs 50-plus transactions inside about six months in one '
                              'tight area, and geology and 3D seismic can swing prices between neighboring '
                              'townships, so auction data gets taken with a grain of salt [86mQK92f7Bg @ '
                              '00:13:25]. The rival playbook is the income or engineering approach: pick '
                              'analog wells, adjust them for one- or two-mile laterals, build a type '
                              'curve, layer in spacing and timing, then compute NPV. Sands puts that at a '
                              'two-to-four-hour job that runs about $400 to $800 [86mQK92f7Bg @ 00:15:30]. '
                              'Mr. Business sides with the engineering camp for producing royalty. '
                              'Professionals value with decline curve analysis and PV10, undrilled '
                              'locations get discounted, stripper wells can be shut in or plugged, and a '
                              '$2,000 check from a six-month-old well overstates future income '
                              '[8gaFGCKNpnk @ 00:12:28].',
                              'On curve mechanics, Matt Sands flags an open split in type-curve building. '
                              'One camp fits a single curve to the averaged production of analog wells '
                              'from the last ten years, normalized for lateral length and time. The other '
                              'fits every well individually and then averages the results [VYytHJ0lMVw @ '
                              '00:28:42]. Danomics runs the per-well style at scale, auto-declining about '
                              '4,000 wells in seconds with b capped at 1.3 and qi capped at twice the '
                              'maximum observed rate, while openly refusing to call 1.3 the correct value '
                              '[gleafhkBQWg @ 00:04:04]. KAPPA Engineering refuses to bet on a single '
                              'equation. It excludes early flowback, weights rate against cumulative '
                              'production in the regression objective, then stacks hyperbolic, Duong and '
                              'power-law exponential fits on the same well and compares them to bracket a '
                              'range of EURs [tPB4O0ryZww @ 00:03:47]. Ryan Hassen of whitson attacks the '
                              'premise that analogs transfer cleanly. Across more than 100,000 wells, '
                              "lateral length behaves close to 'a shale is a shale,' but frac fluid "
                              'intensity, water cut and spacing are special snowflakes. Eagle Ford shows '
                              'the tightest depletion contour and the Delaware Third Bone Spring Sand the '
                              'widest [qdJuFyTh5yU @ 00:02:33].'],
               'table': {'caption': 'Competing playbooks for reading decline, fitting curves and pricing '
                                    'minerals',
                         'headers': ['Fault Line', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How owners should read steep first-year decline',
                                   'Eckard calls high starting rates a positive, not a negative',
                                   'Mr. Business treats a royalty as a depleting asset, not a salary',
                                   'Eckard Enterprises | Oil & Gas Investing ([nn1juJ3_-WA @ 00:10:01]); '
                                   'Mr. Business ([hIerB5MQ52U @ 00:12:19])'],
                                  ['How to price minerals without public sale data',
                                   'Justin Williams prefers EnergyNet comps normalized per net mineral '
                                   'acre',
                                   'Matt Sands wants 50-plus comps in six months, or an engineered NPV',
                                   'Matt Sands ([86mQK92f7Bg @ 00:13:25])'],
                                  ['Fitting a type curve across many analog wells',
                                   'Fit one curve to the averaged, normalized analog production',
                                   'Fit every well individually first, then average the fitted results',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:28:42])'],
                                  ['Choosing the b-factor and terminal decline in forecasts',
                                   'Danomics caps b at 1.3 but refuses to call it correct',
                                   'Sands runs DIY curves with b under 1.3 and 8% terminal decline',
                                   'Danomics ([gleafhkBQWg @ 00:04:04]); Matt Sands ([VYytHJ0lMVw @ '
                                   '00:38:39])'],
                                  ['Selecting one decline model versus a model range',
                                   'Danomics auto-declines about 4,000 wells with one constrained setup in '
                                   'seconds',
                                   'KAPPA stacks hyperbolic, Duong and power-law exponential fits to '
                                   'bracket EUR',
                                   'Danomics ([gleafhkBQWg @ 00:04:45]); KAPPA Engineering ([tPB4O0ryZww @ '
                                   '00:03:47])'],
                                  ['Price deck used to value future production',
                                   'Sands lists NYMEX strip, bank deck, SEC average or flat $60',
                                   'ComboCurve runs flat $70 oil and $3.25 gas for 19-month payout',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:32:06]); ComboCurve ([k4f-XlIpXZU @ '
                                   '00:18:56])'],
                                  ['Accounting method applied to the same well costs',
                                   'Successful efforts expenses G&G and dry holes, booking a $1.3M loss',
                                   'Full cost capitalizes them, booking a $110K profit on identical '
                                   'activity',
                                   'Duahbed Consult ([bZGu6nyMvTA @ 00:07:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap is the paycheck itself. Troy W. Eckard warns that the first '
                              'royalty check arrives about six months after production starts and bundles '
                              'one to five months of volume. The next check covers a single month, so it '
                              "can come in at a third or a sixth of the first. Eckard's instruction is not "
                              'to be alarmed but grateful for revenue captured fast [nn1juJ3_-WA @ '
                              '00:08:21]. Mr. Business hammers a second gap: real checks are always lower '
                              'than the headline math. Regional differentials pull a $70 WTI print down to '
                              "a realized $66 to $68, and post-production costs, 'cost-free' lease "
                              'language fights and severance taxes chew on the rest [hIerB5MQ52U @ '
                              '00:11:07]. On gas, the same channel says deductions hinge on exact lease '
                              "wording such as 'free of costs,' 'market value at the well' or 'proceeds "
                              "received,' plus state law [8gaFGCKNpnk @ 00:15:08]. Then the buyers circle. "
                              'Matt Sands states flatly that buyers will offer less than value, and pairs '
                              'that with a data rule: 18 to 24 months of unrestricted production before '
                              'trusting any curve, since curtailment, waterfloods and CO2 projects sit '
                              'outside the standard fit [VYytHJ0lMVw @ 00:34:47].',
                              'Model risk shows up in the inputs before it shows up in the checks. Ryan '
                              'Hassen found that one apparent wellbore-azimuth anomaly was just a wrong '
                              'EPSG code, and warns that if a GOR map is garbage, no machine-learned '
                              'relationship can save the forecast. The 100,000-well dataset also carries '
                              'selection bias, because it covers only shales that worked [qdJuFyTh5yU @ '
                              '00:12:19]. Mergers & Inquisitions built a hyperbolic type curve in Excel '
                              'from a 10 MMcfe/d IP, a 60% initial decline and a 5% terminal floor. It '
                              "landed at a 113% IRR and $15 million NPV10, against Silver Bow's published "
                              '124% and $6.3 million, a gap the instructor pins on curve shape '
                              '[2tJpxiIqFSM @ 00:15:17]. Worse, issuers like Range Resources disclose EUR '
                              'and D&C cost but no equation. That forces a goal-seeked 4 to 5% decline '
                              'over roughly 25 years against a reserve life near 20, which the instructor '
                              'calls a very common issue [2tJpxiIqFSM @ 00:18:02]. Francis Ramos II adds a '
                              'diagnostic check before any exponential math. Rate versus cumulative must '
                              'plot linear, and semi-log rate versus time must run as a straight line, '
                              'while a plain linear rate-versus-time chart does not reveal whether decline '
                              'is exponential [u3kTgNXLIGI @ 00:02:47].',
                              'Every forecast ends at an economic wall. TopDogEngineer solves for it '
                              'directly, setting oil revenue plus GOR-linked gas revenue minus operating '
                              'cost to zero. In their Excel case the economic rate lands at 140.3 bbl per '
                              'month; below it the well is losing money, and drilling and completion cost '
                              'is pushed out to the NPV step [4mzbNb16NQc @ 00:08:49]. The Crude Files '
                              'notes that about three in four US wells already produce under 15 bbl per '
                              'day. Plugging and abandonment costs run from tens of thousands upward, and '
                              'orphan wells often land on taxpayers and states [R-AasPj-Y5E @ 00:13:06]. '
                              'Price can drag the wall forward. The Crude Files sets a Dallas Fed '
                              'breakeven near $65 against 2025 oil in the low-to-mid $60s. ComboCurve '
                              "reports core Haynesville gas not even at break-even, with JP Morgan's "
                              'roughly $3.50 core breakeven against about $3 gas [k4f-XlIpXZU @ 00:05:53]. '
                              'Permian Resources shows the defensive play. With Waha falling to negative '
                              '$9.52, it choked back about 20% of gas by curtailing high-GOR wells and '
                              'used already-paid firm transport to realize a positive $0.38 per Mcf, an '
                              'estimated $75 million uplift [Kwv0e2yhRmA @ 00:08:47].'],
               'table': {'caption': 'Firsthand traps and the economics checks practitioners use to catch '
                                    'them',
                         'headers': ['Trap',
                                     'What Practitioners Reported',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['First royalty check overstates normal monthly income',
                                   'First check bundles one to five months of production volume',
                                   'Expect the next single-month check near a third or sixth',
                                   'Eckard Enterprises | Oil & Gas Investing ([nn1juJ3_-WA @ 00:07:50])'],
                                  ['Valuing a young well off its latest check',
                                   'A $2,000 check from a six-month-old well overstates future income',
                                   'Professionals run decline curve analysis and PV10 before pricing '
                                   'royalty',
                                   'Mr. Business ([8gaFGCKNpnk @ 00:12:28])'],
                                  ['Fitting curves to curtailed or short production history',
                                   'Curtailment, waterflood and CO2 projects break the standard decline '
                                   'fit',
                                   'Require 18 to 24 months of unrestricted data before forecasting',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:35:19])'],
                                  ['Trusting a type curve as a single-well forecast',
                                   'Type curves land 50/50 above or below actual well results',
                                   'Not every well follows the type curve you come up with',
                                   'Matt Sands ([VYytHJ0lMVw @ 00:37:04])'],
                                  ['Producing past the economic rate on the tail',
                                   'Below 140.3 bbl per month the example well loses money',
                                   'Solve revenue minus operating cost equals zero, then stop producing',
                                   'TopDogEngineer ([4mzbNb16NQc @ 00:08:49])'],
                                  ['Drilling cost outrunning the realized commodity price',
                                   'Dallas Fed breakeven near $65 versus 2025 oil in low-to-mid $60s',
                                   'Operator quality alone moves well cost roughly $2 million each',
                                   'The Crude Files ([R-AasPj-Y5E @ 00:11:04]); The Crude Files '
                                   '([R-AasPj-Y5E @ 00:08:39])'],
                                  ['Selling the entire mineral estate to a lowball buyer',
                                   'Selling 100% of right, title and interest means no going back',
                                   'Sell an NPRI or a partial interest and keep the rest',
                                   'Matt Sands ([86mQK92f7Bg @ 00:31:23])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Pricing, Budgeting or Selling a Royalty',
                           'body': 'Every gate below comes from a trap practitioners hit or watched owners '
                                   'hit: inflated first checks, curves fit to bad data, garbage inputs, '
                                   'and irreversible sales.',
                           'items': ['Do not budget off the first check: it covers one to five months of '
                                     'production, and the next single-month check can run a third or a '
                                     'sixth of it [Eckard Enterprises | Oil & Gas Investing — nn1juJ3_-WA '
                                     '@ 00:08:21].',
                                     'No forecast without 18 to 24 months of unrestricted production; '
                                     'curtailed, waterflooded or CO2 wells break standard decline curve '
                                     'analysis [Matt Sands — VYytHJ0lMVw @ 00:35:19].',
                                     'Audit the inputs before the model: a wrong EPSG code faked an '
                                     'azimuth signal, and a garbage GOR map wrecks any forecast [Whitson '
                                     'Academy — qdJuFyTh5yU @ 00:12:19].',
                                     'Before any sale, pay for your own deed review, because buyer-drafted '
                                     'deeds can sweep in suspense or escheated funds, and a 100% sale is a '
                                     'done deal [Matt Sands — 86mQK92f7Bg @ 00:27:15].']}}],
 'pull_quote': '"The smart way to think about a royalty is not as a salary, it\'s as a depleting asset." — '
               'Mr. Business (hIerB5MQ52U @ 00:12:19).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Pull permits and wells by legal description from the state oil and gas commission '
                      'map, and classify the minerals as producing or non-producing [Matt Sands — '
                      '86mQK92f7Bg @ 00:09:22].',
                      'Compute decimal interest as net mineral acres over unit acres times royalty rate; '
                      '10 NMA in a 640-acre unit at 20% gives 0.3125% [Mr. Business — 8gaFGCKNpnk @ '
                      '00:07:11].',
                      'Fit a two-part curve on a semi-log plot: hyperbolic first, then exponential '
                      'terminal decline at 8% to 15% per year [Matt Sands — VYytHJ0lMVw @ 00:21:29].',
                      'Export Well Database production to Excel, keep b under 1.3, set 8% terminal '
                      'decline, and multiply by your decimal interest [Matt Sands — VYytHJ0lMVw @ '
                      '00:39:28].',
                      'Solve for the economic rate where oil revenue plus gas revenue minus operating cost '
                      'equals zero, using Excel Solver or any root finder [TopDogEngineer — 4mzbNb16NQc @ '
                      '00:03:24].',
                      'Cross-check mature producing assets by averaging the last three months of royalty '
                      'and multiplying by 50 to 70, up to 100 in hot areas [Matt Sands — 86mQK92f7Bg @ '
                      '00:29:36].'],
 'statutory_citations': [{'title': 'Matt Sands — MRP 293:  Why Your Royalty Checks Keep Dropping (And How '
                                   "to Predict What's Next) [00:05:16]",
                          'url': 'https://www.youtube.com/watch?v=VYytHJ0lMVw&t=316s',
                          'relevance': 'Primary practitioner testimony on decline curve analysis, b-factor '
                                       'and terminal decline settings, type-curve disputes, and price '
                                       'decks for royalty forecasting.'},
                         {'title': 'Matt Sands — MRP 4: How Mineral Rights are Valued [00:15:30]',
                          'url': 'https://www.youtube.com/watch?v=86mQK92f7Bg&t=930s',
                          'relevance': 'Primary practitioner testimony on market comps versus income '
                                       'valuation, the 50 to 70 times rule of thumb, and deed traps in '
                                       'mineral sales.'},
                         {'title': 'Mr. Business — The Economics of Owning an Oil Well Royalty Interest '
                                   '[00:08:37]',
                          'url': 'https://www.youtube.com/watch?v=hIerB5MQ52U&t=517s',
                          'relevance': 'Primary practitioner testimony on five-year royalty decline math, '
                                       'price sensitivity, and deductions that cut real checks below '
                                       'headline numbers.'},
                         {'title': 'Eckard Enterprises | Oil & Gas Investing — What the Decline Curve '
                                   'Means for Mineral Investments with Troy W. Eckard - Mineral Royalties '
                                   '101 [00:07:50]',
                          'url': 'https://www.youtube.com/watch?v=nn1juJ3_-WA&t=470s',
                          'relevance': 'Primary practitioner testimony on shale decline shape, 36-month '
                                       'operator payback, and first-check timing for mineral owners.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'nn1juJ3_-WA',
                       'title': 'What the Decline Curve Means for Mineral Investments with Troy W. Eckard '
                                '- Mineral Royalties 101',
                       'channel': 'Eckard Enterprises | Oil & Gas Investing',
                       'author': 'Eckard Enterprises | Oil & Gas Investing',
                       'text': "It's not a negative that your wells are declining, it's a positive that "
                               "they're starting with such a high rate.",
                       'tip': "It's not a negative that your wells are declining, it's a positive that "
                              "they're starting with such a high rate.",
                       'timestamp': 601,
                       'timestamp_seconds': 601,
                       'timestamp_label': '[00:10:01]',
                       'url': 'https://www.youtube.com/watch?v=nn1juJ3_-WA&t=601s',
                       'markdown': '[00:10:01](https://www.youtube.com/watch?v=nn1juJ3_-WA&t=601s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4mzbNb16NQc',
                       'title': 'Decline Curve Analysis: Economic Rate Oil + Gas',
                       'channel': 'TopDogEngineer',
                       'author': 'TopDogEngineer',
                       'text': "When the oil rate gets down to here on our decline curve, we're not making "
                               "any money, we're losing money.",
                       'tip': "When the oil rate gets down to here on our decline curve, we're not making "
                              "any money, we're losing money.",
                       'timestamp': 529,
                       'timestamp_seconds': 529,
                       'timestamp_label': '[00:08:49]',
                       'url': 'https://www.youtube.com/watch?v=4mzbNb16NQc&t=529s',
                       'markdown': '[00:08:49](https://www.youtube.com/watch?v=4mzbNb16NQc&t=529s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Kwv0e2yhRmA',
                       'title': 'Permian Resources (PR): How They Beat Negative Gas Prices',
                       'channel': 'The Byte-Size Brief',
                       'author': 'The Byte-Size Brief',
                       'text': 'They choked back roughly 20% of their total natural gas production.',
                       'tip': 'They choked back roughly 20% of their total natural gas production.',
                       'timestamp': 527,
                       'timestamp_seconds': 527,
                       'timestamp_label': '[00:08:47]',
                       'url': 'https://www.youtube.com/watch?v=Kwv0e2yhRmA&t=527s',
                       'markdown': '[00:08:47](https://www.youtube.com/watch?v=Kwv0e2yhRmA&t=527s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qdJuFyTh5yU',
                       'title': 'Quantifying Shale Performance Drivers Across 100,000 Wells | Ryan Hassen, '
                                'whitson | whitCon 2026',
                       'channel': 'Whitson Academy',
                       'author': 'Whitson Academy',
                       'text': "So, if your GOR map is totally garbage, it doesn't matter if all these "
                               'relationships are great.',
                       'tip': "So, if your GOR map is totally garbage, it doesn't matter if all these "
                              'relationships are great.',
                       'timestamp': 739,
                       'timestamp_seconds': 739,
                       'timestamp_label': '[00:12:19]',
                       'url': 'https://www.youtube.com/watch?v=qdJuFyTh5yU&t=739s',
                       'markdown': '[00:12:19](https://www.youtube.com/watch?v=qdJuFyTh5yU&t=739s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hIerB5MQ52U',
                       'title': 'The Economics of Owning an Oil Well Royalty Interest',
                       'channel': 'Mr. Business',
                       'author': 'Mr. Business',
                       'text': "The smart way to think about a royalty is not as a salary, it's as a "
                               'depleting asset.',
                       'tip': "The smart way to think about a royalty is not as a salary, it's as a "
                              'depleting asset.',
                       'timestamp': 739,
                       'timestamp_seconds': 739,
                       'timestamp_label': '[00:12:19]',
                       'url': 'https://www.youtube.com/watch?v=hIerB5MQ52U&t=739s',
                       'markdown': '[00:12:19](https://www.youtube.com/watch?v=hIerB5MQ52U&t=739s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CiR-w5lHfvI',
                       'title': 'How are Mineral Rights Valued? | How Oil and Gas Activity Impacts the '
                                'Value of Your Mineral Rights',
                       'channel': 'Steven Hatcher | Minerals Guy',
                       'author': 'Steven Hatcher | Minerals Guy',
                       'text': 'A good rule of thumb for a shale well is that it will recover 70 to 80 '
                               'percent of its total volume within the first two years of production.',
                       'tip': 'A good rule of thumb for a shale well is that it will recover 70 to 80 '
                              'percent of its total volume within the first two years of production.',
                       'timestamp': 706,
                       'timestamp_seconds': 706,
                       'timestamp_label': '[00:11:46]',
                       'url': 'https://www.youtube.com/watch?v=CiR-w5lHfvI&t=706s',
                       'markdown': '[00:11:46](https://www.youtube.com/watch?v=CiR-w5lHfvI&t=706s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VYytHJ0lMVw',
                       'title': 'MRP 293:  Why Your Royalty Checks Keep Dropping (And How to Predict '
                                "What's Next)",
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': "It doesn't mean that every well is going to follow that type curve that "
                               'you come up with.',
                       'tip': "It doesn't mean that every well is going to follow that type curve that you "
                              'come up with.',
                       'timestamp': 2209,
                       'timestamp_seconds': 2209,
                       'timestamp_label': '[00:36:49]',
                       'url': 'https://www.youtube.com/watch?v=VYytHJ0lMVw&t=2209s',
                       'markdown': '[00:36:49](https://www.youtube.com/watch?v=VYytHJ0lMVw&t=2209s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bZGu6nyMvTA',
                       'title': 'Oil and Gas Accounting 102: Practical Case Study | Income Statement & '
                                'Balance Sheet',
                       'channel': 'Duahbed Consult',
                       'author': 'Duahbed Consult',
                       'text': 'Production cost fifty thousand.',
                       'tip': 'Production cost fifty thousand.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=bZGu6nyMvTA&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=bZGu6nyMvTA&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gleafhkBQWg',
                       'title': 'Decline Curve Analysis with Danomics Flows',
                       'channel': 'Danomics',
                       'author': 'Danomics',
                       'text': "I'm just putting it at 1.3, I'm not saying that is the correct value.",
                       'tip': "I'm just putting it at 1.3, I'm not saying that is the correct value.",
                       'timestamp': 244,
                       'timestamp_seconds': 244,
                       'timestamp_label': '[00:04:04]',
                       'url': 'https://www.youtube.com/watch?v=gleafhkBQWg&t=244s',
                       'markdown': '[00:04:04](https://www.youtube.com/watch?v=gleafhkBQWg&t=244s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tPB4O0ryZww',
                       'title': 'CITRINE - WORKFLOW- Decline Curve Analysis',
                       'channel': 'KAPPA Engineering',
                       'author': 'KAPPA Engineering',
                       'text': 'This way DCA models can be compared and used for making decisions on '
                               'possible range of EURs.',
                       'tip': 'This way DCA models can be compared and used for making decisions on '
                              'possible range of EURs.',
                       'timestamp': 227,
                       'timestamp_seconds': 227,
                       'timestamp_label': '[00:03:47]',
                       'url': 'https://www.youtube.com/watch?v=tPB4O0ryZww&t=227s',
                       'markdown': '[00:03:47](https://www.youtube.com/watch?v=tPB4O0ryZww&t=227s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k4f-XlIpXZU',
                       'title': 'Breaking Down the Haynesville Shale’s Top Wells',
                       'channel': 'ComboCurve',
                       'author': 'ComboCurve',
                       'text': "Gas isn't even currently at break-even for the core.",
                       'tip': "Gas isn't even currently at break-even for the core.",
                       'timestamp': 353,
                       'timestamp_seconds': 353,
                       'timestamp_label': '[00:05:53]',
                       'url': 'https://www.youtube.com/watch?v=k4f-XlIpXZU&t=353s',
                       'markdown': '[00:05:53](https://www.youtube.com/watch?v=k4f-XlIpXZU&t=353s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R-AasPj-Y5E',
                       'title': 'THE COST OF DRILLING AN OIL WELL | 8 Million and NO GUARANTEES',
                       'channel': 'The Crude Files',
                       'author': 'The Crude Files',
                       'text': 'A gap of roughly $2 million per well, just from how well the company has '
                               'run.',
                       'tip': 'A gap of roughly $2 million per well, just from how well the company has '
                              'run.',
                       'timestamp': 519,
                       'timestamp_seconds': 519,
                       'timestamp_label': '[00:08:39]',
                       'url': 'https://www.youtube.com/watch?v=R-AasPj-Y5E&t=519s',
                       'markdown': '[00:08:39](https://www.youtube.com/watch?v=R-AasPj-Y5E&t=519s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '86mQK92f7Bg',
                       'title': 'MRP 4: How Mineral Rights are Valued',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'So if you were to sell all 100 percent of all your right, title and '
                               "interest to any mineral rights you own, it's a done deal, there's no going "
                               'back.',
                       'tip': 'So if you were to sell all 100 percent of all your right, title and '
                              "interest to any mineral rights you own, it's a done deal, there's no going "
                              'back.',
                       'timestamp': 1883,
                       'timestamp_seconds': 1883,
                       'timestamp_label': '[00:31:23]',
                       'url': 'https://www.youtube.com/watch?v=86mQK92f7Bg&t=1883s',
                       'markdown': '[00:31:23](https://www.youtube.com/watch?v=86mQK92f7Bg&t=1883s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u3kTgNXLIGI',
                       'title': 'Life of a Well and Decline Curve Analysis',
                       'channel': 'Francis Ramos II',
                       'author': 'Francis Ramos II',
                       'text': 'Just because you know that little relationship is linear, you know for a '
                               'fact that the well is exponentially declining.',
                       'tip': 'Just because you know that little relationship is linear, you know for a '
                              'fact that the well is exponentially declining.',
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=u3kTgNXLIGI&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=u3kTgNXLIGI&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2tJpxiIqFSM',
                       'title': 'Type Curves in Oil & Gas Modeling: Modeling Master Key or Academic '
                                'Curiosity?',
                       'channel': 'Mergers & Inquisitions / Breaking Into Wall Street',
                       'author': 'Mergers & Inquisitions / Breaking Into Wall Street',
                       'text': 'The terminal decline is just the minimum decline rate the well will '
                               'eventually reach.',
                       'tip': 'The terminal decline is just the minimum decline rate the well will '
                              'eventually reach.',
                       'timestamp': 328,
                       'timestamp_seconds': 328,
                       'timestamp_label': '[00:05:28]',
                       'url': 'https://www.youtube.com/watch?v=2tJpxiIqFSM&t=328s',
                       'markdown': '[00:05:28](https://www.youtube.com/watch?v=2tJpxiIqFSM&t=328s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8gaFGCKNpnk',
                       'title': 'How Oil Well Royalties Work: Income, Decline Curves, Taxes & Risks',
                       'channel': 'Mr. Business',
                       'author': 'Mr. Business',
                       'text': 'If something sounds too good to be true, it probably is.',
                       'tip': 'If something sounds too good to be true, it probably is.',
                       'timestamp': 1134,
                       'timestamp_seconds': 1134,
                       'timestamp_label': '[00:18:54]',
                       'url': 'https://www.youtube.com/watch?v=8gaFGCKNpnk&t=1134s',
                       'markdown': '[00:18:54](https://www.youtube.com/watch?v=8gaFGCKNpnk&t=1134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VYytHJ0lMVw',
                       'title': 'MRP 293:  Why Your Royalty Checks Keep Dropping (And How to Predict '
                                "What's Next)",
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': "I think that's a good conservative number for most wells.",
                       'tip': "I think that's a good conservative number for most wells.",
                       'timestamp': 2319,
                       'timestamp_seconds': 2319,
                       'timestamp_label': '[00:38:39]',
                       'url': 'https://www.youtube.com/watch?v=VYytHJ0lMVw&t=2319s',
                       'markdown': '[00:38:39](https://www.youtube.com/watch?v=VYytHJ0lMVw&t=2319s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '86mQK92f7Bg',
                       'title': 'MRP 4: How Mineral Rights are Valued',
                       'channel': 'Matt Sands',
                       'author': 'Matt Sands',
                       'text': 'So you got to really take some of that data with a grain of salt.',
                       'tip': 'So you got to really take some of that data with a grain of salt.',
                       'timestamp': 820,
                       'timestamp_seconds': 820,
                       'timestamp_label': '[00:13:40]',
                       'url': 'https://www.youtube.com/watch?v=86mQK92f7Bg&t=820s',
                       'markdown': '[00:13:40](https://www.youtube.com/watch?v=86mQK92f7Bg&t=820s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
