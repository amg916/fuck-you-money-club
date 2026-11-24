from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'sales-tax-nexus-compliance-automation',
 'question_prompt': 'Where do I owe sales tax as an online seller, and which software should I use to '
                    'calculate, collect, and file it?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Sales Tax Nexus and Compliance Automation',
 'subtitle': 'Economic nexus after Wayfair, marketplace facilitator rules, duties vs. taxes, Avalara vs. '
             'TaxJar vs. Taxify vs. TaxCloud vs. Numeral comparisons, the AvaTax and TaxJar demos, the SAP '
             'Commerce Cloud integration, and US obligations for Canadian sellers',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree that sales tax is now a growth-triggered liability: since the '
                      '2018 Wayfair ruling, most states key economic nexus to $100,000 in sales or 200 '
                      'transactions, and FBA or 3PL inventory creates physical presence on its own. The '
                      'working cycle is nexus, register, calculate, handle exemptions, then file and '
                      'remit, and Avalara and LedgerGurus both insist you never collect before '
                      'registering. Amazon, Walmart, and Etsy collect as marketplace facilitators; Shopify '
                      'does not. Street numbers run from TaxJar at about $20 a month with AutoFile near '
                      '$30 to $35 per filing up to Avalara engines at $10k to $30k plus $40 to $50 per '
                      "return. The fights are over tooling: Avalara's 10-out-of-10 engine versus its "
                      "price, TaxJar's March 2026 repricing and backfiling gaps, and Numeral, Taxify, and "
                      'TaxCloud pitched as leaner challengers.',
 'key_metrics': [{'label': 'Common Economic Nexus Threshold',
                  'metric': 'Common Economic Nexus Threshold',
                  'value': '$100,000 in sales or 200 transactions',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Most states use this bar since June 2018, while California, New York, and '
                             'Texas set higher thresholds.',
                  'source': 'Cherry Bekaert ([rUvJ4UwGqiA @ 00:01:00])'},
                 {'label': 'Rate and Rule Permutations',
                  'metric': 'Rate and Rule Permutations',
                  'value': '13,000 permutations changing monthly',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Avalara's webinar presenters cite 13,000 rate, rule, and boundary "
                             'permutations that change every month, with ZIP 30024 spanning three '
                             'counties.',
                  'source': 'Avalara ([EtT3YoVfP0c @ 00:38:55])'},
                 {'label': 'TaxJar AutoFile Cost Per Filing',
                  'metric': 'TaxJar AutoFile Cost Per Filing',
                  'value': 'About $30 to $35 per filing',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Arthur Glinkin prices TaxJar subscriptions from about $20 a month and calls '
                             'AutoFile at roughly $30 to $35 per filing worth it.',
                  'source': 'Arthur Glinkin ([1Cr_iHc8p4s @ 00:07:44])'},
                 {'label': 'Avalara Engine and Filing Cost',
                  'metric': 'Avalara Engine and Filing Cost',
                  'value': '$10k to $30k engine plus $40 to $50 per return',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'LedgerGurus quotes the Avalara engine at $10k to $30k and filing at $40 to '
                             '$50 per return, fitting businesses over $5M or on Shopify Plus.',
                  'source': 'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:13:07])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every operator starts from the same map: nexus is the switch that turns '
                              'sales tax on, and it now flips two ways. Cherry Bekaert lists the physical '
                              'triggers as employees, 1099 workers, sales reps, offices, and inventory '
                              'sitting in Amazon or 3PL warehouses, then stacks economic nexus on top '
                              'since June 2018, with most states keyed to $100,000 in sales or 200 '
                              'transactions while California, New York, and Texas run higher bars, and '
                              'what counts toward the bar shifts between retail and wholesale, marketplace '
                              'and direct, taxable and non-taxable sales [rUvJ4UwGqiA @ 00:01:00]. '
                              "Avalara's webinar presenters hammer the FBA angle hardest: parking "
                              'inventory in a fulfillment center creates presence in that state whether or '
                              'not you meant to sell there [EtT3YoVfP0c @ 00:17:05]. Arthur Glinkin adds '
                              'the street nuance that physical triggers are not always obvious; California '
                              'told them a passive partner does not create nexus, so their standing move '
                              'is to phone the state department of revenue and get the answer straight '
                              'from the source [1Cr_iHc8p4s @ 00:04:05]. LedgerGurus and Avalara close the '
                              'loop on timing: liability begins only from the moment the threshold is '
                              'crossed, which makes the crossing date the single most important number an '
                              'operator tracks [pqXEldKeguY @ 00:30:16].',
                              "The second point of agreement is who actually holds the bag. Avalara's Tax "
                              '101 explainer states that Amazon, Walmart, and Etsy must collect under '
                              "marketplace facilitator laws, meaning a major marketplace 'is already "
                              "taking care of sales tax for you,' while Shopify is not a facilitator and "
                              'leaves the seller fully responsible [QiT660QtcXA @ 00:01:18]. Arthur '
                              'Glinkin runs the same split with Amazon, eBay, and Etsy and adds the '
                              'operator payoff: those facilitated sales are excluded from threshold '
                              "counts, so a seller's own storefront volume is what drives the math "
                              '[1Cr_iHc8p4s @ 00:06:00]. Ryan McKenzie strips away the small-seller '
                              "comfort zone entirely, warning that 'the size of your business does not "
                              "grant you anything' and that the state will collect every last penny, with "
                              'the brand owner on the hook to organize, file, and pay [jmsERJHMp_0 @ '
                              "00:01:27]. Avalara's webinar team frames it as tax 'triggered by growth, "
                              "not intent,' pointing to a sweat-suit brand that scaled to $10M a month and "
                              'an M&A deal in which $1,000,000 was withheld from the sale price '
                              '[EtT3YoVfP0c @ 00:32:53]. The consensus is blunt: volume, not paperwork, '
                              'decides when a seller is exposed, and the exposure follows the business all '
                              'the way into its exit.',
                              "Process consensus is just as tight. Avalara's webinar lays out five steps "
                              'in strict order: figure out where you owe, register, calculate, track, then '
                              'file and remit, with the flat warning to never collect before registering '
                              '[EtT3YoVfP0c @ 00:15:15]. The LedgerGurus session with Avalara repeats the '
                              'sequence as nexus, register, calculate, exemptions, file and remit, and '
                              "lands the same rule: 'please don't collect unless you're registered' "
                              '[pqXEldKeguY @ 00:31:09]. Nobody argues for doing it by hand. Sal of SAL '
                              "Accounting CPA says Shopify Tax 'does half the work,' covering more than "
                              '11,000 jurisdictions and free for the first $100,000 in sales but never '
                              'filing or paying, and tells sellers not to fall back to manual work because '
                              "of penalties [HbiniE5ODzI @ 00:02:41]. Avalara's SAP Commerce Cloud demo "
                              'shows why: two buyers in the same zip code with identical carts pay '
                              'different tax because one sits inside a special City Improvement District '
                              'that zip-code calculation would most certainly have overlooked, while '
                              'AvaTax validates the address and pushes the rate to the cart in '
                              'milliseconds [A7FAFArV6JM @ 00:00:39]. The baseline prerequisite every '
                              'speaker assumes is an automated engine plus a filing layer, wired in before '
                              'the first taxable order ships.'],
               'table': {'caption': 'Where the practitioners line up on nexus, responsibility, and process',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Physical nexus triggers from people and stored inventory',
                                   'Employees, 1099 workers, reps, offices, and Amazon or 3PL inventory '
                                   'all create presence',
                                   'Audit every warehouse, contractor, and office location before assuming '
                                   'you owe nothing',
                                   'Cherry Bekaert ([rUvJ4UwGqiA @ 00:00:24])'],
                                  ['Economic nexus thresholds since the 2018 Wayfair ruling',
                                   'Thresholds commonly run $100K in sales or 200 transactions over twelve '
                                   'months',
                                   'Track rolling twelve-month sales and order counts separately for every '
                                   'single state',
                                   'LedgerGurus: Ecommerce Accounting Experts ([pqXEldKeguY @ 00:10:12])'],
                                  ['Marketplace facilitators collect on their own platform sales',
                                   'Amazon, eBay, and Etsy collect and remit; those sales are excluded '
                                   'from thresholds',
                                   'Your own storefront volume, not marketplace volume, drives your '
                                   'threshold math',
                                   'Arthur Glinkin ([1Cr_iHc8p4s @ 00:06:00])'],
                                  ['Shopify is not a marketplace facilitator for its merchants',
                                   'Shopify leaves the seller fully responsible for collecting, filing, '
                                   'and paying the tax',
                                   'Pair Shopify checkout with a separate filing tool or an accountant '
                                   'every period',
                                   'Avalara ([QiT660QtcXA @ 00:01:18])'],
                                  ['Register with the state before collecting a single cent',
                                   'Never collect before registering; officers face personal liability and '
                                   'unjust enrichment exposure',
                                   'Lock in each state permit first, then switch on collection in the cart',
                                   'Avalara ([EtT3YoVfP0c @ 00:19:36])'],
                                  ['Tax exposure is triggered by growth rather than intent',
                                   'Small sellers are not safe; the state will collect every last penny '
                                   'owed',
                                   'Monitor nexus as revenue scales instead of assuming size buys you a '
                                   'pass',
                                   'Ryan McKenzie ([jmsERJHMp_0 @ 00:01:27])'],
                                  ['Zip-code rates miss special districts inside one zip code',
                                   'Two buyers in one zip pay different tax when one sits in an '
                                   'improvement district',
                                   'Use address-level calculation rather than a single flat zip-code rate '
                                   'table',
                                   'Avalara ([A7FAFArV6JM @ 00:00:39])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['TaxJar is the default entry point, and the numbers are specific. Arthur '
                              "Glinkin pegs subscriptions at about $20 a month, 'super affordable,' with "
                              'AutoFile at roughly $30 to $35 per filing that they call worth it, and they '
                              'treat the Detailed Sales Tax Analysis report as the source of truth over '
                              'QuickBooks Online [1Cr_iHc8p4s @ 00:07:44]. The plan tier matters: Starter '
                              'only flags nexus once a threshold is hit, while Professional shows progress '
                              "such as '95%' so a seller sees the crossing coming [1Cr_iHc8p4s @ "
                              "00:08:25]. TaxJar's own 2026 demo shows the tracker alerting at 75% and "
                              "100% of each state's order or revenue threshold, rolling 100 Connecticut "
                              'Shopify orders together with eBay or Etsy sales, and auto-marking Amazon '
                              'sales into New York as marketplace-exempt [M_AJmScLLXE @ 00:02:43]. Sales '
                              'Tax at Scale puts the 2026 price shock on the table: roughly a 100% or '
                              'larger jump in March 2026, with 25,000 transactions moving from $12k to '
                              '$25k a year and AutoFile rising from $35 to $55 per filing, legacy pricing '
                              'holding until October 1, 2026, plus Starter at $39 for 200 orders and '
                              'Professional at $99, scaling to $1,199 at 2,500 orders [5Dtw2cworM0 @ '
                              '00:02:49].',
                              'Avalara is the heavyweight, and the operators price it that way. '
                              'LedgerGurus rates its engine 10 out of 10 for calculation, with rooftop '
                              'accuracy and 700-plus connections, but quotes $10k to $30k for the engine '
                              'plus $40 to $50 per return and fits it to businesses over $5M or on Shopify '
                              "Plus [-DhtTN5_Rh4 @ 00:13:07]. The same firm's 2020 breakdown adds GPS "
                              'accuracy down to the house number, an exclusive Shopify partnership with '
                              'AvaTax running about $300 a month there, a hard approval window where '
                              'returns not approved by the 10th are auto-approved on the 11th, and '
                              'mandatory product code mapping, exemption certificates, and every location '
                              'loaded up front [1L7s6llWlRo @ 00:08:32]. Sales Tax at Scale fills in the '
                              'per-unit math: about $403 per registration location, filings at $42 to $54 '
                              'per return per Reddit users, setup fees on top, and free filing in 24 '
                              "states through Avalara's SST CSP status if you ask about enrollment "
                              "[5Dtw2cworM0 @ 00:01:35]. Avalara's own AvaTax demo reduces the engine to "
                              "three questions: nexus, customer, item; any 'no' returns $0, and the same "
                              'engine also calculates VAT, GST, customs duties, and tariffs across '
                              '1,200-plus partner integrations [RRnAKNi_DBU @ 00:02:08].',
                              'The challenger stack is where the cheaper street plays live. Sal of SAL '
                              'Accounting CPA names Numeral their favorite because it auto-registers, '
                              'files, and pays, and their clients have never missed a deadline, even '
                              'though it is newer with fewer tutorials [HbiniE5ODzI @ 00:05:15]. Ryan '
                              'McKenzie ranks software as the easiest of four options and points to '
                              "Numeral's claim of 'less than five minutes monthly,' with site monitoring, "
                              'registration in nexus states, remittance, and no long-term contracts, '
                              "versus a big tax agency they used that was great but 'considerably more' "
                              'expensive and prone to human error [jmsERJHMp_0 @ 00:02:40]. LedgerGurus '
                              'says Taxify runs for over 50% of their clients as the middle ground: '
                              'mid-$40s a month, $27 per filing, flexible adjustments, phone support, and '
                              "a 12th-of-the-month approval deadline against TaxJar's 6th and Avalara's "
                              '10th [1L7s6llWlRo @ 00:19:30]. Sales Tax at Scale backs TaxCloud for '
                              'businesses over $1M, at $39 down to $20 per return, SST CSP status in 24 '
                              'states, US-based support, VDAs, and backfiling, though limited to the US '
                              'and Canada, which the channel picks over both Avalara and TaxJar '
                              '[5Dtw2cworM0 @ 00:06:26]. Every challenger pitch is aimed at the same pain: '
                              'Avalara-level filing coverage without Avalara-level invoices.'],
               'table': {'caption': 'Stated pricing and mechanics for the sales tax tool stack',
                         'headers': ['Tool or Tier',
                                     'Stated Pricing',
                                     'Key Mechanic or Limit',
                                     'Expert Source'],
                         'rows': [['TaxJar subscription with AutoFile enrolled state by state',
                                   'About $20 per month to start, AutoFile roughly $30 to $35 per filing',
                                   'Starter flags nexus only at threshold; Professional shows progress '
                                   'like 95%',
                                   'Arthur Glinkin ([1Cr_iHc8p4s @ 00:07:21])'],
                                  ['TaxJar after the March 2026 repricing of its plans',
                                   '25,000 transactions moved from $12k to $25k yearly; AutoFile $35 to '
                                   '$55',
                                   'Legacy pricing holds until October 1, 2026; support cut and moved '
                                   'offshore',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:02:49])'],
                                  ['Avalara AvaTax engine plus its returns filing service',
                                   'Engine runs $10k to $30k; filing about $40 to $50 per return',
                                   'Rated 10 out of 10 for calculation; fits sellers above $5M or Shopify '
                                   'Plus',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:13:07])'],
                                  ['Avalara registration and per-return filing fee structure',
                                   'About $403 per registration location and $42 to $54 per return',
                                   'SST CSP status gives free filing in 24 states if you ask about '
                                   'enrollment',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:01:35])'],
                                  ['Taxify, now part of Sovos, as the middle-ground option',
                                   'Starts at $34 with $27 per return and backfilings at the same rate',
                                   'Phone support, editable data, and an approval deadline on the 12th',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:23:31])'],
                                  ['TaxCloud for businesses already above $1M in sales',
                                   'Per-return pricing stated as $39 down to $20 per filed return',
                                   'SST CSP in 24 states, US-based support, VDAs, and backfiling included',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:06:26])'],
                                  ['Shopify Tax built directly into the Shopify checkout',
                                   'Free for the first $100,000 in sales across 11,000-plus jurisdictions',
                                   'Calculates only; it never files or pays, so never run it alone',
                                   'SAL Accounting CPA ([HbiniE5ODzI @ 00:02:07])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the operators actually do inside the tools',
                           'body': 'Four moves practitioners use to cut cost, catch errors, and keep '
                                   'filings clean.',
                           'items': ['Run the TaxJar Detailed Sales Tax Analysis report as the source of '
                                     'truth, and when it disagrees with QuickBooks Online, trust TaxJar '
                                     '[Arthur Glinkin — 1Cr_iHc8p4s @ 00:09:04].',
                                     'If you run TaxJar, use it as both engine and filer because its '
                                     'returns cannot be adjusted, and always send the full street address '
                                     '[LedgerGurus: Ecommerce Accounting Experts — 1L7s6llWlRo @ '
                                     '00:14:42].',
                                     'Texas is one of the only states that accepts voluntary prepayments, '
                                     'which earn a 1.25% discount [Avalara — EtT3YoVfP0c @ 00:49:10].',
                                     'When negotiating with Avalara, ask directly about SST CSP '
                                     'enrollment, which unlocks free filing in 24 states [Sales Tax at '
                                     'Scale — 5Dtw2cworM0 @ 00:01:35].']},
               'sop_steps': [{'step': 1,
                              'title': 'Map nexus across every channel',
                              'action': 'Connect carts, marketplaces, and ERP, set physical nexus in the '
                                        'business profile, and watch the 75% and 100% threshold alerts.',
                              'detail': "TaxJar's setup flow connects carts, marketplaces, and ERP, sets "
                                        'physical nexus through the business profile, and tracks each '
                                        "state's order or revenue threshold [TaxJar — M_AJmScLLXE @ "
                                        '00:00:52]. Include employees, 1099 workers, reps, offices, and '
                                        'Amazon or 3PL inventory as physical triggers [Cherry Bekaert — '
                                        'rUvJ4UwGqiA @ 00:00:24].'},
                             {'step': 2,
                              'title': 'Register before you collect',
                              'action': 'Get an EIN, apply for each state permit through the department of '
                                        'revenue, and only then switch on collection.',
                              'detail': 'Registration runs through the state department of revenue after '
                                        'obtaining an EIN, is mostly free, and Wisconsin and South '
                                        'Carolina can charge $30 to $50 [Tyler — SgxDnkPR36U @ 00:02:32]. '
                                        'Never collect before registering [Avalara — EtT3YoVfP0c @ '
                                        '00:19:36].'},
                             {'step': 3,
                              'title': 'Wire the calculation engine',
                              'action': 'Turn on automatic rate calculation, set exemptions, and use '
                                        'address-level accuracy rather than zip-code tables.',
                              'detail': 'In Shopify, set the address under Settings > General, enable '
                                        'automatic calculation under Settings > Taxes, and handle '
                                        'exemptions with a collection plus a tax override [Tyler — '
                                        "SgxDnkPR36U @ 00:06:00]. Avalara's engine calculates at rooftop "
                                        'level and earns a 10 out of 10 for calculation [LedgerGurus: '
                                        'Ecommerce Accounting Experts — -DhtTN5_Rh4 @ 00:09:08].'},
                             {'step': 4,
                              'title': 'Automate filing and approve on time',
                              'action': 'Enroll states in AutoFile with a US bank account, approve returns '
                                        "before each tool's deadline, and archive every return.",
                              'detail': 'AutoFile needs a subscription, a US bank account, and sometimes '
                                        'state e-file credentials; the state pulls funds via ACH and '
                                        'returns are archived as an audit trail [TaxJar — M_AJmScLLXE @ '
                                        '00:04:29]. Approval deadlines run the 12th for Taxify, the 6th '
                                        'for TaxJar, and the 10th for Avalara [LedgerGurus: Ecommerce '
                                        'Accounting Experts — 1L7s6llWlRo @ 00:19:30].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['No single winning stack emerges among these operators. Sales Tax at Scale '
                              'pushes TaxCloud for businesses over $1M, pitching $39 down to $20 per '
                              'return, SST CSP status in 24 states, US-based support, VDAs and backfiling, '
                              'with the catch that it covers only the US and Canada [5Dtw2cworM0 @ '
                              '00:06:08]. SAL Accounting CPA picks Numeral instead because it '
                              'auto-registers, files and pays, and reports that their clients have never '
                              'missed a deadline even though the platform is newer with fewer tutorials '
                              '[HbiniE5ODzI @ 00:05:15]. The split verdict there is Numeral for small '
                              'sellers, TaxJar for medium multi-state sellers, Avalara for multi-country '
                              'operations, and never Shopify Tax alone [HbiniE5ODzI @ 00:10:52]. '
                              'LedgerGurus rates the Avalara engine 10 out of 10 for calculation and slots '
                              'it for businesses over $5M or on Shopify Plus [-DhtTN5_Rh4 @ 00:14:13], '
                              'while Acuity Ecommerce Accounting goes the opposite direction, flagging '
                              'that AvaTax lacks cart connectors and TrustFile drops Amazon registry '
                              "addresses before concluding 'don't even really consider it' [8zfPSv7hAWM @ "
                              '00:07:28]. The working read: the engine LedgerGurus scores perfect is the '
                              'one Acuity tells sellers to skip, so the choice tracks revenue band, '
                              'channel mix, and multi-country exposure rather than brand reputation.',
                              'TaxJar is where the numbers collide hardest. LedgerGurus prices TaxJar '
                              'backfilings at $300 to $500 per return and notes no local home-rule filing '
                              '[-DhtTN5_Rh4 @ 00:18:40], yet the 2020 LedgerGurus breakdown lists '
                              'backfiling as unsupported alongside Colorado home-rule, Louisiana parishes, '
                              'Missouri remote sellers and Michigan use tax, pricing the plan at $19.99 '
                              'per month and about $25 per filing [1L7s6llWlRo @ 00:14:42]. Arthur Glinkin '
                              'says subscriptions start around $20 per month, with AutoFile at roughly $30 '
                              "to $35 per filing that is 'worth it,' and leans on the Professional plan "
                              'because it shows progress toward a threshold instead of only flagging nexus '
                              'once it is hit [1Cr_iHc8p4s @ 00:07:44]. Sales Tax at Scale paints a '
                              'harsher 2026 picture: a March increase of roughly 100% or more, with 25k '
                              'transactions jumping from $12k to $25k per year and AutoFile moving from '
                              '$35 to $55 per filing, legacy pricing holding until October 1, 2026, plus '
                              'support cut and moved offshore [5Dtw2cworM0 @ 00:02:49]. Phone support only '
                              'arrives at the Professional tier, per the same breakdown. Budget against '
                              'the newest written quote, not the cheapest figure in a review.',
                              'Operators also split on how much accuracy is worth paying for. In the '
                              'LedgerGurus Sales Tax 101 session, the Avalara presenters say they dropped '
                              'zip-code rate files because those were only about 80% accurate [pqXEldKeguY '
                              '@ 00:12:00], claim 80 to 90 tax researchers behind a 100% accuracy '
                              "guarantee, yet concede Shopify's zip-based engine is 'really close' "
                              "[pqXEldKeguY @ 00:52:46]. SAL Accounting CPA treats Shopify Tax as 'half "
                              "the work,' free for the first $100,000 in sales but never filing or paying "
                              '[HbiniE5ODzI @ 00:02:41], while Tyler walks sellers through enabling '
                              "Shopify's automatic rate calculation under Settings and exporting the tax "
                              'filing report to an accountant [SgxDnkPR36U @ 00:08:29]. On who does the '
                              'work, Ryan McKenzie ranks four routes from easiest to hardest: software '
                              "such as Numeral at 'less than five minutes monthly,' a big tax agency that "
                              "worked but was 'considerably more' expensive and prone to human error, an "
                              "internal team that is wrong for 98% of sellers, and DIY, the 'least "
                              "intelligent' option where you will 'probably mess something up' "
                              '[jmsERJHMp_0 @ 00:02:24]. The split comes down to footprint: zip-close is '
                              'tolerable in simple states, while special districts reward rooftop '
                              'engines.'],
               'table': {'caption': 'Side-by-side playbooks where named operators take opposing positions',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which platform to run for a growing US seller',
                                   'TaxCloud for businesses over $1M, $39 down to $20 per return, SST CSP '
                                   'in 24 states',
                                   'Numeral for small sellers because it auto-registers, files and pays '
                                   'with no missed deadlines',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:06:08]); SAL Accounting CPA '
                                   '([HbiniE5ODzI @ 00:05:15])'],
                                  ['Whether Avalara belongs in the stack at all',
                                   'Engine rated 10 out of 10 with rooftop calculation, fit for over $5M '
                                   'or Shopify Plus',
                                   'AvaTax lacks cart connectors and TrustFile drops Amazon registry '
                                   'addresses, so skip it',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:14:13]); '
                                   'Acuity Ecommerce Accounting ([8zfPSv7hAWM @ 00:07:28])'],
                                  ['Whether TaxJar can file historical periods for you',
                                   'TaxJar backfilings are available at $300 to $500 per return',
                                   'TaxJar remits calculated amounts and cannot backfile historical '
                                   'returns at all',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:18:40]); '
                                   'Acuity Ecommerce Accounting ([8zfPSv7hAWM @ 00:08:32])'],
                                  ['What a TaxJar AutoFile return actually costs per filing',
                                   'Roughly $30 to $35 per filing, which Arthur Glinkin calls worth it',
                                   'About $25 per filing in 2020, versus $35 rising to $55 after March '
                                   '2026',
                                   'Arthur Glinkin ([1Cr_iHc8p4s @ 00:07:44]); LedgerGurus: Ecommerce '
                                   'Accounting Experts ([1L7s6llWlRo @ 00:14:42]); Sales Tax at Scale '
                                   '([5Dtw2cworM0 @ 00:02:49])'],
                                  ['Who should own filing and remittance work day to day',
                                   'Software like Numeral at less than five minutes monthly with no '
                                   'long-term contracts',
                                   'Big tax agency that works but costs considerably more and invites '
                                   'human error',
                                   'Ryan McKenzie ([jmsERJHMp_0 @ 00:02:24])'],
                                  ['Zip-code rates versus rooftop address-level calculation',
                                   "Shopify's zip-based engine is really close and free for the first "
                                   '$100,000',
                                   'Zip files only about 80% accurate; same-zip buyers in an improvement '
                                   'district pay differently',
                                   'LedgerGurus: Ecommerce Accounting Experts ([pqXEldKeguY @ 00:52:46]); '
                                   'Avalara ([A7FAFArV6JM @ 00:00:39])'],
                                  ['How many Avalara integrations exist for connecting carts',
                                   '700+ integrations including SAP, Oracle and NetSuite connections',
                                   '1,200+ partner integrations claimed in the AvaTax product demo',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:00:37]); Avalara ([RRnAKNi_DBU @ '
                                   '00:02:48])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive traps sit between collecting and remitting. Avalara's "
                              'growing-sellers webinar warns never to collect before registering, because '
                              "officers are personally liable, with exposure framed as jail and 'unjust "
                              "enrichment' [EtT3YoVfP0c @ 00:22:52]; the LedgerGurus Sales Tax 101 session "
                              "repeats it bluntly: 'So please don't collect unless you're registered' "
                              '[pqXEldKeguY @ 00:31:09]. LedgerGurus then flags a TaxJar-specific leak: it '
                              'remits what it calculates rather than what you actually collected, which '
                              'produces either illegal retention of tax or overpayment out of your own '
                              "margin [-DhtTN5_Rh4 @ 00:17:26]. Tyler's Shopify walkthrough shows how "
                              "confusion creeps in, stating remittance goes 'to the IRS' when every other "
                              'operator routes it to the state department of revenue, and confirming '
                              'Shopify does not remit at all, so the filing report must be exported to an '
                              'accountant [SgxDnkPR36U @ 00:04:15]. The fix pattern is consistent: get the '
                              'permit first, reconcile collected tax against filed tax every period, and '
                              "treat Shopify's collection toggle as the start of liability, not the end of "
                              'the job. Registration itself is mostly free, though Wisconsin and South '
                              'Carolina can charge $30 to $50.',
                              'Calendar and data-hygiene failures are the next layer. LedgerGurus says '
                              "Avalara must be approved by the 11th at 5 PM ET or it auto-files, TaxJar's "
                              "approval deadline is the 5th and Taxify's the 12th, with the tools setting "
                              'deadlines one to two weeks ahead of the states [-DhtTN5_Rh4 @ 00:12:28]; '
                              'the 2020 LedgerGurus breakdown instead lists Avalara at the 10th and TaxJar '
                              'at the 6th, and requires product code mapping, exemption certificates and '
                              'every location loaded up front [1L7s6llWlRo @ 00:08:32]. LedgerGurus calls '
                              "Avalara setup long and 'garbage in, garbage out,' and warns Taxify has no "
                              'exemption-certificate tracking plus a broken Shopify connection that forces '
                              'manual imports [-DhtTN5_Rh4 @ 00:25:17]. Certificates also die on their '
                              'own: Florida resale certificates expire December 31st every year, Louisiana '
                              'does not exempt nonprofits, and a certificate issued to an old company name '
                              'was disallowed [EtT3YoVfP0c @ 00:46:28]. The same Avalara webinar has '
                              'sellers audit payroll and warehouses a couple of times a year, because tax '
                              "is 'triggered by growth, not intent' [EtT3YoVfP0c @ 00:32:53]. The Sales "
                              'Tax 101 session adds that you need one certificate per state per customer, '
                              'with shared SST and MTC forms available [pqXEldKeguY @ 00:39:42].',
                              'Economics checks separate survivable mistakes from fatal ones. Sales Tax at '
                              'Scale reports one customer hit with a 2,000% Avalara price increase and '
                              'another paying $30k on TaxCloud versus $150k on Avalara, with Reddit users '
                              'dropping from $100k to $150k a year down to $25k to $30k after switching '
                              "[5Dtw2cworM0 @ 00:08:07]. Avalara's growing-sellers webinar describes one "
                              'M&A deal where $1,000,000 was withheld from the sale price, Florida '
                              'penalties running 10% per month up to 50%, and Texas voluntary prepayment '
                              'earning a 1.25% discount [EtT3YoVfP0c @ 00:34:38]. The LedgerGurus Sales '
                              'Tax 101 webinar recounts The Mattress Queen being shut down after a '
                              'Washington audit, and lays out the VDA escape hatch: Texas lookback is '
                              'unlimited, but a VDA caps it at 5 years, penalties are waived and interest '
                              "usually is not [pqXEldKeguY @ 00:26:07]. Cherry Bekaert's remedy sequence "
                              'matches: get a permit, then file prior-period returns or a VDA for large '
                              'liabilities [rUvJ4UwGqiA @ 00:02:09]. Liability begins only from the moment '
                              'you cross the threshold, so the first spreadsheet to build is the date each '
                              'state was crossed, then price backfiling against a VDA before a state finds '
                              'you first.'],
               'table': {'caption': 'Firsthand traps, what broke, and the countermove operators reported',
                         'headers': ['Trap', 'What Went Wrong', 'Cost or Countermove', 'Expert Source'],
                         'rows': [['Collecting sales tax before the state permit is issued',
                                   'Officers become personally liable, with jail and unjust enrichment '
                                   'exposure described',
                                   'Register in each nexus state first, then switch collection on',
                                   'Avalara ([EtT3YoVfP0c @ 00:19:36])'],
                                  ['TaxJar remitting calculated tax instead of collected tax',
                                   'Filed amounts drift from collected amounts, causing illegal retention '
                                   'or overpayment',
                                   'Reconcile collected versus filed tax every period before approving '
                                   'returns',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:17:26])'],
                                  ['Missing the monthly return approval cutoff inside the filing tool',
                                   'Avalara auto-files if returns are not approved by the 11th at 5 PM ET',
                                   'Calendar the 5th for TaxJar, 11th for Avalara, 12th for Taxify',
                                   'LedgerGurus: Ecommerce Accounting Experts ([-DhtTN5_Rh4 @ 00:12:28])'],
                                  ['Expired or mismatched customer exemption certificates on file',
                                   'Florida certificates expire December 31st; an old-company-name '
                                   'certificate was disallowed',
                                   'Renew annually and match the legal entity name on every certificate',
                                   'Avalara ([EtT3YoVfP0c @ 00:46:28])'],
                                  ['Quoting international buyers without a full landed cost build',
                                   'Miss one duty, tax, fee or add-on and the quote can fall apart',
                                   'Lock the HTS code first, then stack transport, insurance, duties and '
                                   'fees',
                                   'Shipping Solutions ([IrCCfr1mSvg @ 00:03:05])'],
                                  ['Vendor price shocks on renewal of the tax platform contract',
                                   'One customer saw a 2,000% Avalara increase; TaxJar rose roughly 100% '
                                   'in 2026',
                                   'Get written renewal quotes and benchmark TaxCloud at $30k versus $150k '
                                   'Avalara',
                                   'Sales Tax at Scale ([5Dtw2cworM0 @ 00:08:07])'],
                                  ['Ignoring a state audit until enforcement shuts the business down',
                                   'The Mattress Queen was shut down after a Washington sales tax audit',
                                   'Use a VDA to cap Texas lookback at 5 years and waive penalties',
                                   'LedgerGurus: Ecommerce Accounting Experts ([pqXEldKeguY @ '
                                   '00:22:56])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Checks Before Scaling Into New States',
                           'body': 'Every item below comes from a trap a named operator watched burn '
                                   'sellers; clear all four before turning on collection in a new state or '
                                   'renewing a tax platform contract.',
                           'items': ['Do not enable collection in any state until the permit is issued, '
                                     'because collecting unregistered creates personal officer liability '
                                     '[Avalara — EtT3YoVfP0c @ 00:19:36].',
                                     'Confirm Amazon, Walmart and Etsy sales are treated as '
                                     'marketplace-collected, and remember Shopify is not a facilitator so '
                                     'you still own that tax [Avalara — QiT660QtcXA @ 00:01:18].',
                                     'Approve returns before the platform cutoff, since Avalara auto-files '
                                     "after the 11th at 5 PM ET and TaxJar's deadline is the 5th "
                                     '[LedgerGurus: Ecommerce Accounting Experts — -DhtTN5_Rh4 @ '
                                     '00:12:28].',
                                     'Map every employee, 1099 worker, rep, office and Amazon or 3PL '
                                     'inventory location, because each creates physical nexus [Cherry '
                                     'Bekaert — rUvJ4UwGqiA @ 00:00:24].']}}],
 'pull_quote': '"The size of your business does not grant you anything." — Ryan McKenzie (jmsERJHMp_0 @ '
               '00:01:27).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Audit physical nexus by listing employees, 1099 workers, reps, offices and '
                      'inventory sitting in Amazon or 3PL warehouses [Cherry Bekaert — rUvJ4UwGqiA @ '
                      '00:00:24].',
                      'Turn on a nexus tracker that alerts at 75% and 100% of each state threshold and '
                      'combines Shopify, eBay and Etsy orders [TaxJar — M_AJmScLLXE @ 00:02:43].',
                      'Register with the state department of revenue before collecting a single dollar in '
                      'that state [LedgerGurus: Ecommerce Accounting Experts — pqXEldKeguY @ 00:31:09].',
                      'Treat the TaxJar detailed sales tax analysis report as the source of truth when it '
                      'disagrees with QuickBooks Online [Arthur Glinkin — 1Cr_iHc8p4s @ 00:09:04].',
                      'Enroll AutoFile with a US bank account and any required state e-file credentials, '
                      'then archive every filed return as an audit trail [TaxJar — M_AJmScLLXE @ '
                      '00:04:29].',
                      'For past exposure, get the permit and either file prior-period returns or run a VDA '
                      'when the liability is large [Cherry Bekaert — rUvJ4UwGqiA @ 00:02:09].'],
 'statutory_citations': [{'title': 'LedgerGurus: Ecommerce Accounting Experts — Avalara? TaxJar? Taxify? '
                                   'BEST SALES TAX APP for Ecommerce [00:17:26]',
                          'url': 'https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=1046s',
                          'relevance': 'Primary practitioner testimony on TaxJar remitting calculated '
                                       'rather than collected tax, approval cutoffs and backfiling costs.'},
                         {'title': 'Avalara — Webinar: Ecommerce Sales Tax Basics for Growing Sellers '
                                   '[00:19:36]',
                          'url': 'https://www.youtube.com/watch?v=EtT3YoVfP0c&t=1176s',
                          'relevance': 'Primary practitioner testimony on never collecting before '
                                       'registering, officer liability, certificate failures and penalty '
                                       'economics.'},
                         {'title': 'Sales Tax at Scale — Avalara? TaxJar? TaxCloud? The Honest Comparison '
                                   'for Ecommerce [00:08:07]',
                          'url': 'https://www.youtube.com/watch?v=5Dtw2cworM0&t=487s',
                          'relevance': 'Primary practitioner testimony on platform price shocks, 2026 '
                                       'TaxJar repricing and TaxCloud versus Avalara spend.'},
                         {'title': 'LedgerGurus: Ecommerce Accounting Experts — Sales Tax 101 with Avalara '
                                   '[00:26:07]',
                          'url': 'https://www.youtube.com/watch?v=pqXEldKeguY&t=1567s',
                          'relevance': 'Primary practitioner testimony on voluntary disclosure lookback '
                                       'caps, penalty waivers and audit enforcement.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'IrCCfr1mSvg',
                       'title': 'Duties, Tariffs and Taxes: Understanding the Costs of International Trade',
                       'channel': 'Shipping Solutions',
                       'author': 'Shipping Solutions',
                       'text': 'Even if your product qualifies for duty-free treatment under a free trade '
                               'agreement, VAT or GST may still apply at import.',
                       'tip': 'Even if your product qualifies for duty-free treatment under a free trade '
                              'agreement, VAT or GST may still apply at import.',
                       'timestamp': 56,
                       'timestamp_seconds': 56,
                       'timestamp_label': '[00:00:56]',
                       'url': 'https://www.youtube.com/watch?v=IrCCfr1mSvg&t=56s',
                       'markdown': '[00:00:56](https://www.youtube.com/watch?v=IrCCfr1mSvg&t=56s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EtT3YoVfP0c',
                       'title': 'Webinar: Ecommerce Sales Tax Basics for Growing Sellers',
                       'channel': 'Avalara',
                       'author': 'Avalara',
                       'text': 'The state of Texas is one of the only states in the country that you can '
                               'voluntarily make prepayments.',
                       'tip': 'The state of Texas is one of the only states in the country that you can '
                              'voluntarily make prepayments.',
                       'timestamp': 2950,
                       'timestamp_seconds': 2950,
                       'timestamp_label': '[00:49:10]',
                       'url': 'https://www.youtube.com/watch?v=EtT3YoVfP0c&t=2950s',
                       'markdown': '[00:49:10](https://www.youtube.com/watch?v=EtT3YoVfP0c&t=2950s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5Dtw2cworM0',
                       'title': 'Avalara? TaxJar? TaxCloud? The Honest Comparison for Ecommerce',
                       'channel': 'Sales Tax at Scale',
                       'author': 'Sales Tax at Scale',
                       'text': 'Neither Avalara nor TaxJar offers hands on audit defense.',
                       'tip': 'Neither Avalara nor TaxJar offers hands on audit defense.',
                       'timestamp': 347,
                       'timestamp_seconds': 347,
                       'timestamp_label': '[00:05:47]',
                       'url': 'https://www.youtube.com/watch?v=5Dtw2cworM0&t=347s',
                       'markdown': '[00:05:47](https://www.youtube.com/watch?v=5Dtw2cworM0&t=347s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HbiniE5ODzI',
                       'title': 'Numeral vs TaxJar vs Avalara - Best US Sales Tax Platform for Canadians',
                       'channel': 'SAL Accounting CPA',
                       'author': 'SAL Accounting CPA',
                       'text': 'So Shopify tax does half the work for you.',
                       'tip': 'So Shopify tax does half the work for you.',
                       'timestamp': 161,
                       'timestamp_seconds': 161,
                       'timestamp_label': '[00:02:41]',
                       'url': 'https://www.youtube.com/watch?v=HbiniE5ODzI&t=161s',
                       'markdown': '[00:02:41](https://www.youtube.com/watch?v=HbiniE5ODzI&t=161s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-DhtTN5_Rh4',
                       'title': 'Avalara? TaxJar? Taxify? BEST SALES TAX APP for Ecommerce',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': 'So 10 out of 10 for calculation.',
                       'tip': 'So 10 out of 10 for calculation.',
                       'timestamp': 622,
                       'timestamp_seconds': 622,
                       'timestamp_label': '[00:10:22]',
                       'url': 'https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=622s',
                       'markdown': '[00:10:22](https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=622s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-DhtTN5_Rh4',
                       'title': 'Avalara? TaxJar? Taxify? BEST SALES TAX APP for Ecommerce',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': 'TaxJar remits what it calculates, not what you collected, which leads to '
                               'illegal retention of tax or overpayment.',
                       'tip': 'TaxJar remits what it calculates, not what you collected, which leads to '
                              'illegal retention of tax or overpayment.',
                       'timestamp': 1046,
                       'timestamp_seconds': 1046,
                       'timestamp_label': '[00:17:26]',
                       'url': 'https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=1046s',
                       'markdown': '[00:17:26](https://www.youtube.com/watch?v=-DhtTN5_Rh4&t=1046s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rUvJ4UwGqiA',
                       'title': 'Sales & Use Tax: eCommerce Nexus',
                       'channel': 'Cherry Bekaert',
                       'author': 'Cherry Bekaert',
                       'text': 'Since June 2018, most states use a threshold of $100,000 in sales or 200 '
                               'transactions, while California, New York and Texas set higher thresholds.',
                       'tip': 'Since June 2018, most states use a threshold of $100,000 in sales or 200 '
                              'transactions, while California, New York and Texas set higher thresholds.',
                       'timestamp': 60,
                       'timestamp_seconds': 60,
                       'timestamp_label': '[00:01:00]',
                       'url': 'https://www.youtube.com/watch?v=rUvJ4UwGqiA&t=60s',
                       'markdown': '[00:01:00](https://www.youtube.com/watch?v=rUvJ4UwGqiA&t=60s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QiT660QtcXA',
                       'title': 'Tax 101: Does my online marketplace collect sales tax for me?',
                       'channel': 'Avalara',
                       'author': 'Avalara',
                       'text': 'That means a major marketplace like Amazon is already taking care of sales '
                               'tax for you.',
                       'tip': 'That means a major marketplace like Amazon is already taking care of sales '
                              'tax for you.',
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=QiT660QtcXA&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=QiT660QtcXA&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RRnAKNi_DBU',
                       'title': 'Avalara AvaTax Demo',
                       'channel': 'Avalara',
                       'author': 'Avalara',
                       'text': 'If the answer to any of the nexus, customer or item questions is no, the '
                               'tax returned is zero dollars.',
                       'tip': 'If the answer to any of the nexus, customer or item questions is no, the '
                              'tax returned is zero dollars.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=RRnAKNi_DBU&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=RRnAKNi_DBU&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8zfPSv7hAWM',
                       'title': 'Avalara TaxJar Taxify | Sales Tax Solutions for Ecommerce Sellers',
                       'channel': 'Acuity Ecommerce Accounting',
                       'author': 'Acuity Ecommerce Accounting',
                       'text': "Don't even really consider it.",
                       'tip': "Don't even really consider it.",
                       'timestamp': 448,
                       'timestamp_seconds': 448,
                       'timestamp_label': '[00:07:28]',
                       'url': 'https://www.youtube.com/watch?v=8zfPSv7hAWM&t=448s',
                       'markdown': '[00:07:28](https://www.youtube.com/watch?v=8zfPSv7hAWM&t=448s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1Cr_iHc8p4s',
                       'title': 'Ecommerce Sales Tax MADE EASY (TaxJar Setup)',
                       'channel': 'Arthur Glinkin',
                       'author': 'Arthur Glinkin',
                       'text': 'So, last time I checked, the Tax Jar subscriptions start at about $20 per '
                               'month, which is super affordable.',
                       'tip': 'So, last time I checked, the Tax Jar subscriptions start at about $20 per '
                              'month, which is super affordable.',
                       'timestamp': 441,
                       'timestamp_seconds': 441,
                       'timestamp_label': '[00:07:21]',
                       'url': 'https://www.youtube.com/watch?v=1Cr_iHc8p4s&t=441s',
                       'markdown': '[00:07:21](https://www.youtube.com/watch?v=1Cr_iHc8p4s&t=441s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SgxDnkPR36U',
                       'title': 'Online Sales Tax: A Guide to Economic Nexus & Ecommerce',
                       'channel': 'Tyler',
                       'author': 'Tyler',
                       'text': 'Shopify does not remit the tax for you, so use the tax filing report and '
                               'export it to your accountant.',
                       'tip': 'Shopify does not remit the tax for you, so use the tax filing report and '
                              'export it to your accountant.',
                       'timestamp': 509,
                       'timestamp_seconds': 509,
                       'timestamp_label': '[00:08:29]',
                       'url': 'https://www.youtube.com/watch?v=SgxDnkPR36U&t=509s',
                       'markdown': '[00:08:29](https://www.youtube.com/watch?v=SgxDnkPR36U&t=509s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jmsERJHMp_0',
                       'title': "Don't Get Crushed by Ecom Sales Tax! Learn the Wayfair Secret to Survival",
                       'channel': 'Ryan McKenzie',
                       'author': 'Ryan McKenzie',
                       'text': 'The size of your business does not grant you anything.',
                       'tip': 'The size of your business does not grant you anything.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=jmsERJHMp_0&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=jmsERJHMp_0&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1L7s6llWlRo',
                       'title': '2020 Sales Tax Apps for Online Sellers | Avalara, Taxjar, and Taxify',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': 'For simple needs go with TaxJar or Taxify, for moderate needs Taxify, and '
                               'for robust needs Avalara.',
                       'tip': 'For simple needs go with TaxJar or Taxify, for moderate needs Taxify, and '
                              'for robust needs Avalara.',
                       'timestamp': 1417,
                       'timestamp_seconds': 1417,
                       'timestamp_label': '[00:23:37]',
                       'url': 'https://www.youtube.com/watch?v=1L7s6llWlRo&t=1417s',
                       'markdown': '[00:23:37](https://www.youtube.com/watch?v=1L7s6llWlRo&t=1417s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A7FAFArV6JM',
                       'title': 'SAP Commerce Cloud + Avalara',
                       'channel': 'Avalara',
                       'author': 'Avalara',
                       'text': 'Two buyers in the same zip code with the same cart pay different tax, '
                               'because one sits in a City Improvement District that most certainly would '
                               'have been overlooked.',
                       'tip': 'Two buyers in the same zip code with the same cart pay different tax, '
                              'because one sits in a City Improvement District that most certainly would '
                              'have been overlooked.',
                       'timestamp': 39,
                       'timestamp_seconds': 39,
                       'timestamp_label': '[00:00:39]',
                       'url': 'https://www.youtube.com/watch?v=A7FAFArV6JM&t=39s',
                       'markdown': '[00:00:39](https://www.youtube.com/watch?v=A7FAFArV6JM&t=39s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M_AJmScLLXE',
                       'title': 'TaxJar demo: How to automate sales tax compliance in 2026',
                       'channel': 'TaxJar',
                       'author': 'TaxJar',
                       'text': 'We track nexus based on your number of orders or revenue based on each '
                               "state's economic nexus thresholds.",
                       'tip': 'We track nexus based on your number of orders or revenue based on each '
                              "state's economic nexus thresholds.",
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=M_AJmScLLXE&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=M_AJmScLLXE&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pqXEldKeguY',
                       'title': 'Sales Tax 101 with Avalara',
                       'channel': 'LedgerGurus: Ecommerce Accounting Experts',
                       'author': 'LedgerGurus: Ecommerce Accounting Experts',
                       'text': "So please don't collect unless you're registered.",
                       'tip': "So please don't collect unless you're registered.",
                       'timestamp': 1869,
                       'timestamp_seconds': 1869,
                       'timestamp_label': '[00:31:09]',
                       'url': 'https://www.youtube.com/watch?v=pqXEldKeguY&t=1869s',
                       'markdown': '[00:31:09](https://www.youtube.com/watch?v=pqXEldKeguY&t=1869s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
