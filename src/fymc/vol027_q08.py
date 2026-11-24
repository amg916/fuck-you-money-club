from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'quality-of-earnings-financial-due-diligence',
 'question_prompt': 'What is a quality of earnings report, how is it read, and why do lenders and buyers '
                    'rely on it?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Quality of Earnings and Financial Due Diligence',
 'subtitle': 'QoE vs. reported EBITDA, a step-by-step QoE analysis and databook walkthrough, reading a QoE '
             'as a practitioner, how lenders read QoE reports and why banks reject seller EBITDA, QoE '
             'cost, financial due diligence fundamentals, common seller and inventory mistakes, and the '
             'diligence failures that kill deals',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': "Practitioners from Acquira's TreeWalk QoE desk, John Colley, Elliott Holland, "
                      'CandiMentor, and lender-focused QoE shops agree that the purchase price is a '
                      'multiple of EBITDA, so the QoE exists to prove which earnings are real, recurring, '
                      'and transferable. Every add-back needs an invoice, payroll record, or genuine '
                      'one-time event, and a cost recurring three years running gets rejected. Street '
                      'mechanics start with proof of cash tied to bank statements and tax returns, run a '
                      'three-column bridge from reported to normalized EBITDA, and set a debt-free, '
                      "cash-free working capital peg from monthly data. Colley's Summit case shows a $2.3 "
                      'million gap becoming $23 million at 10x; TreeWalk reports roughly half of QoEs come '
                      'back clean and 20 to 25% kill the deal. Practitioners split on cost and scope, from '
                      '$12,000 fixed-fee reports to $500,000 Big Four engagements.',
 'key_metrics': [{'label': 'QoE Outcome Split Across 50+ Deals',
                  'metric': 'QoE Outcome Split Across 50+ Deals',
                  'value': '45-50% clean; 20-25% deal-killers; ~20% gray-area renegotiation',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "The TreeWalk Consulting QoE lead's breakdown of last year's 50-plus "
                             'transactions: about half came back clean, 20 to 25% surfaced major mistakes '
                             'that stopped the deal, and the rest carried downward EBITDA pressure '
                             'requiring earnouts, seller notes, or repricing.',
                  'source': 'Acquira ([g_fy5eeJpHE @ 00:27:49])'},
                 {'label': 'Small-Business QoE Fixed-Fee Pricing Tiers',
                  'metric': 'Small-Business QoE Fixed-Fee Pricing Tiers',
                  'value': '$12,000-$15,000 (<$2.5M revenue); $14,000-$20,000/$23,000 (<$10M EV); $25,000+ '
                           '(>$10M EV)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Midwest CPA's budgeting guide, with simple single-location businesses at the "
                             'bottom tier and custom scopes above $10 million enterprise value, always '
                             'billed as a fixed fee.',
                  'source': 'Chris Barrett, CPA ([36OTOiIXSrk @ 00:01:31])'},
                 {'label': 'Summit Normalization Gap And Price Swing',
                  'metric': 'Summit Normalization Gap And Price Swing',
                  'value': '$18.5M reported to $16.2M normalized; $2.3M gap = $23M at 10x',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Colley's Summit Industrial Services case: a trimmed founder salary add-back, "
                             'rejected recurring consulting fees, and a missed below-market related-party '
                             'lease reset.',
                  'source': 'John Colley | The Investment Banking Practitioner ([zQE4R-z6Yww @ 00:03:17])'},
                 {'label': 'Lender Minimum Debt Service Coverage',
                  'metric': 'Lender Minimum Debt Service Coverage',
                  'value': 'At least 1.25x',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Adjusted cash flow divided by annual debt payments is the key number lenders '
                             'pull from the QoE before approving acquisition debt.',
                  'source': 'QoE and Financial Modeling Practice ([SBILxsNgW-o @ 00:01:02])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner who prices deals lands on the same arithmetic: the '
                              'purchase price is a multiple of EBITDA or SDE, so the earnings figure '
                              "itself is the asset being bought. Edspira frames the buyer's goal as "
                              'learning how much of earnings is cash versus non-cash, recurring versus '
                              'non-recurring, and the product of aggressive accounting, because valuation '
                              'is often expressed as a multiple of adjusted EBITDA [itIweMi_DyU @ '
                              '00:00:28]. Elliott Holland is blunter: sellers lie about EBITDA, and a CIM '
                              'showing $1 million at a 4x multiple implies $4 million of value when the '
                              'real figure could be $800,000, $1.2 million, $500,000, or even zero '
                              '[KJPGQ94h_GY @ 00:00:19]. Holland adds that once sellers know they are '
                              'exiting at three to five times EBITDA, even the most honorable people hide '
                              'things between data sets the buyer has no time to reconcile while chasing '
                              'lenders and equity [KJPGQ94h_GY @ 00:01:09]. John Colley, drawing on 30 '
                              'years across SG Cowen, Wasserstein, and Houlihan Lokey, calls the QoE the '
                              'single most consequential document in M&A diligence because it answers '
                              'whether the claimed EBITDA is real, targeting normalized maintainable '
                              'EBITDA under new ownership [zQE4R-z6Yww @ 00:01:57]. Steve Roscioli lists '
                              'the review scope: revenue, add-backs, expenses, accounting practices, '
                              'customer concentration, working capital, and performance trends over time '
                              '[RXawmeZf9sU @ 00:00:17].',
                              "The second consensus point is that no add-back survives on the seller's "
                              'say-so. The QoE and Financial Modeling Practice channel says lenders walk '
                              'through every add-back, and each one needs an invoice, a payroll record, or '
                              'a clear one-time event; an add-back without documentation is usually thrown '
                              'out [SBILxsNgW-o @ 00:00:00]. Their companion breakdown makes it concrete: '
                              'a seller claiming $1.2 million of EBITDA after adding back a boat, a '
                              'nephew, and a one-time lawsuit watches the lender toss anything without '
                              'paper overboard, boat included, because banks lend on proof, not on says '
                              '[yP7oBq_gKbw @ 00:00:23]. CandiMentor insists the label one-time is not '
                              'enough: a non-recurring item may be removed only when there is a credible '
                              'reason it will not come back, and repeated one-time costs reveal normal '
                              'operations rather than genuine exceptions [QVDTq7Qd6-A @ 00:02:25]. John '
                              'Colley converts this into five red flags: recurring items dressed up as '
                              'one-time, above-market owner compensation add-backs that ignore replacement '
                              'cost, missing negative adjustments such as below-market related-party rent, '
                              'aggressive revenue normalization that assumes a departed customer returns, '
                              'and understated run-rate costs from deferred maintenance or running lean '
                              'for the sale process [zQE4R-z6Yww @ 00:03:34]. Every practitioner here '
                              "treats the add-back schedule as the seller's burden to prove.",
                              'Consensus also holds that clean EBITDA can still produce a bad deal when '
                              'cash, working capital, debt-like items, or customer dependency are misread. '
                              'Corporate Finance Institute describes a CFO bragging about $50 million of '
                              'EBITDA while diligence finds only $10 million converting to usable cash, '
                              'usually from aging receivables or inventory built ahead of growth '
                              '[FvywvHEpXKU @ 00:04:18]. The same team calls customer concentration the '
                              'first red flag: if 40% of revenue comes from one customer, valuation has to '
                              'plummet [FvywvHEpXKU @ 00:03:48]. The FE International guest on Jon '
                              "Stoddard's channel contrasts two $10 million businesses: one client on a "
                              'non-transferable rolling annual agreement versus 100 clients paying '
                              '$100,000 on three-year, auto-extending, assignable contracts, the latter '
                              'worth significantly more [Yr06Fv79PU0 @ 00:04:32]. Figuring Out with Rahul '
                              'lays out the working capital safeguard: set a target from historical data, '
                              'measure actual NWC at close, and cut the price dollar for dollar on any '
                              'shortfall [xgCInPpZDiQ @ 00:05:05]. CandiMentor stretches net debt beyond '
                              'the bank loan to leases, accrued interest, seller obligations, and unfunded '
                              'commitments, asking whether the buyer will effectively fund them after '
                              'closing [a5aX7QK8vKA @ 00:02:37]. Each speaker treats these checks as part '
                              'of the same earnings question, not a separate exercise.'],
               'table': {'caption': 'Where QoE Practitioners Agree: Core Principles And Their Deal '
                                    'Consequences',
                         'headers': ['Consensus Principle',
                                     'What The Practitioner States',
                                     'Deal Consequence',
                                     'Expert Source'],
                         'rows': [['Adjusted EBITDA is the number that drives the purchase price',
                                   "Valuation is often expressed as a multiple of the seller's adjusted "
                                   'EBITDA figure',
                                   'A significant discrepancy lets the buyer renegotiate price or walk '
                                   'away entirely',
                                   'Edspira ([itIweMi_DyU @ 00:01:16])'],
                                  ['Sellers inflate claimed earnings when a sale multiple is in sight',
                                   'Even honorable sellers lie about EBITDA when exiting at three to five '
                                   'times',
                                   'A $1 million CIM EBITDA could really be $500,000 or even zero',
                                   'Elliott Holland ([KJPGQ94h_GY @ 00:01:09])'],
                                  ['Every add-back must be backed by documentary evidence before credit',
                                   'An invoice, payroll record, or clear one-time event must support each '
                                   'add-back',
                                   'Undocumented add-backs are usually thrown out by the lender reviewing '
                                   'the deal',
                                   'QoE and Financial Modeling Practice ([SBILxsNgW-o @ 00:00:22])'],
                                  ['The recurrence test kills disguised one-time costs in the bridge',
                                   'A non-recurring cost appearing three years running is not actually '
                                   'non-recurring',
                                   'Rejected add-backs reduce normalized EBITDA and move the purchase '
                                   'price directly',
                                   'John Colley | The Investment Banking Practitioner ([zQE4R-z6Yww @ '
                                   '00:03:51])'],
                                  ['Owner personal spending running through the business must be stripped '
                                   'out',
                                   'Sports tickets, vacations, home repairs, second homes, and boats show '
                                   'up in the books',
                                   'Non-business costs are isolated so true business earnings become '
                                   'visible to the buyer',
                                   'XPX - Exit Planning Exchange ([gRV7segOzzo @ 00:01:48])'],
                                  ['Earnings must convert into cash, not just accounting profit on paper',
                                   'Strong EBITDA can hide cash trapped in inventory or unpaid customer '
                                   'invoices',
                                   'Lenders focus on cash conversion and repayment capacity under real '
                                   'pressure',
                                   'CandiMentor ([QVDTq7Qd6-A @ 00:04:34])'],
                                  ['Revenue durability and transferability determine what earnings are '
                                   'actually worth',
                                   'One non-assignable client is far riskier than 100 clients on '
                                   'three-year contracts',
                                   'Two businesses with identical $10 million earnings receive very '
                                   'different valuations',
                                   'Jon Stoddard ([Yr06Fv79PU0 @ 00:05:07])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The TreeWalk Consulting QoE lead presenting on Acquira, whose midsize CPA '
                              'firm of about 65 people ran roughly 50 to 55 transactions last year with '
                              '85% in the lower mid-market, says proof of cash is the first step on every '
                              'engagement [g_fy5eeJpHE @ 00:01:29]. Mechanically, revenue net of AR '
                              'movement and expenses net of AP and capex movement are tied to what '
                              'actually hits and leaves the bank statements; about 85% of the time it '
                              'works out because owners watch cash closely, and the businesses where it '
                              'does not are red flags to run from [g_fy5eeJpHE @ 00:05:30]. The lender '
                              'version is a three-way tie: bank deposits to the P&L, the P&L to the tax '
                              'returns, and if the three sources disagree the lender wants to know why '
                              '[SBILxsNgW-o @ 00:00:43]. Elliott Holland explains why the tie-out cannot '
                              'be skipped in small companies: in 16 years they have seen cash-ish and '
                              'accrual-ish books, never straight either one, so interpreting revenue '
                              'recognition is a core QoE task [KJPGQ94h_GY @ 00:00:54]. Chris Barrett of '
                              'Midwest CPA prices the work off that complexity: percent-completion, '
                              'revenue recognition, inventory and project tracking, multiple locations, '
                              'carve-outs, and overall size all add hours to the engagement [36OTOiIXSrk @ '
                              '00:00:13].',
                              "John Colley's three-column framework runs reported EBITDA, adjusted EBITDA "
                              'after genuinely non-recurring items, and normalized EBITDA after '
                              'normalization and pro forma adjustments [zQE4R-z6Yww @ 00:04:50]. On the '
                              'Summit Industrial Services case, $18.5 million of reported EBITDA accepts a '
                              '$1.8 million litigation add-back as legitimate, cuts a $900,000 founder '
                              'salary add-back to $500,000 because the replacement costs $400,000, rejects '
                              "$600,000 of 'one-time' consulting in its third straight year, and adds a "
                              'missed $350,000 hit from a family-trust warehouse lease 30% below market, '
                              'landing at $16.2 million [zQE4R-z6Yww @ 00:05:30]. At 10x, that $2.3 '
                              'million gap is a $23 million price swing [zQE4R-z6Yww @ 00:03:17]. Figuring '
                              'Out with Rahul runs the same math: $10 million reported normalizes to $7.5 '
                              'million, a 25% drop, and at 5x the price falls from $50 million to $37.5 '
                              'million [xgCInPpZDiQ @ 00:06:06]. Verified Metrics builds the bridge in a '
                              'databook: management adjustments picked from a drop-down of account names, '
                              'a separate diligence-adjustments block for items like IPO share listing and '
                              'legal fees, and annual plus LTM columns [EzOFN-69wBU @ 00:01:24]. '
                              'CandiMentor adds the bridge check that the same benefit is never counted '
                              'twice [QVDTq7Qd6-A @ 00:04:34].',
                              'Working capital is where the TreeWalk lead says deals die, ranking the peg '
                              'a top-two or top-three killer [g_fy5eeJpHE @ 00:16:31]. Their M&A '
                              'definition is debt-free, cash-free: strip lines of credit, deferred '
                              'revenue, bank indebtedness, and other debt-like items from current '
                              'liabilities and remove cash from current assets. On an $8.7 million deal, '
                              "closer to $10 million with earnouts, a seller's tax accountant netted the "
                              'line of credit and produced roughly $300,000, while the QoE produced $2.1 '
                              'million because city contracts paid in six months, $2.5 million sat in AR, '
                              'and 10% retainage was withheld [g_fy5eeJpHE @ 00:18:16]. They insist '
                              'monthly P&Ls and monthly adjustments matter more than any other tab, since '
                              'bonus payouts, PTO, and large vendor payments around the closing date '
                              'belong in net debt or the peg [g_fy5eeJpHE @ 00:29:14]. Verified Metrics '
                              'shows the manual override: delete the formula and key in only the partial '
                              'amount of accrued employee expenses to exclude, then read the three-month '
                              'average NWC against longer averages [EzOFN-69wBU @ 00:02:41]. Lenders then '
                              'test whether the peg leaves enough cash at closing and whether adjusted '
                              'cash flow covers annual debt payments at least 1.25 times [yP7oBq_gKbw @ '
                              '00:01:03].'],
               'table': {'caption': 'QoE Street Mechanics: Procedures, Tools, And The Numbers '
                                    'Practitioners Report',
                         'headers': ['Mechanic Or Tool',
                                     'Exact Execution',
                                     'Numbers Reported',
                                     'Expert Source'],
                         'rows': [['Proof of cash run as the first procedure on every engagement',
                                   'Tie revenue net of AR and expenses net of AP and capex to bank '
                                   'statements',
                                   'Works out about 85% of the time; failures are red flags to run from',
                                   'Acquira ([g_fy5eeJpHE @ 00:05:45])'],
                                  ['Lender three-way reconciliation of bank deposits, P&L, and tax returns',
                                   'Bank deposits tie to the P&L and the P&L ties to filed tax returns',
                                   'Any disagreement among the three sources triggers a lender demand for '
                                   'explanation',
                                   'QoE and Financial Modeling Practice ([SBILxsNgW-o @ 00:00:43])'],
                                  ['Three-column EBITDA bridge from reported through adjusted to '
                                   'normalized earnings',
                                   'Remove genuine one-time items, then apply normalization and pro forma '
                                   'adjustments',
                                   'Summit moves from $18.5 million to $16.2 million, a $23 million swing '
                                   'at 10x',
                                   'John Colley | The Investment Banking Practitioner ([zQE4R-z6Yww @ '
                                   '00:06:13])'],
                                  ['Excel databook with drop-down management and diligence adjustment '
                                   'blocks',
                                   'Select account names from the drop-down so actual financials '
                                   'auto-populate each period',
                                   'Annual figures plus last-twelve-month columns, with LTM ending June '
                                   '2024 in the case',
                                   'Verified Metrics ([EzOFN-69wBU @ 00:00:34])'],
                                  ['Expected count of EBITDA adjustments on a typical small acquisition '
                                   'deal',
                                   'Each adjustment carries written commentary explaining why it hits the '
                                   'bridge',
                                   'Average around 8 to 9, lowest about 3, highest seen in the mid-20s',
                                   'Acquira ([g_fy5eeJpHE @ 00:15:31])'],
                                  ['Fixed-fee QoE pricing tiers scaled to revenue and enterprise value',
                                   'Price set by industry complexity, number of locations or entities, and '
                                   'size',
                                   '$12,000-$15,000 small; $14,000-$23,000 under $10 million EV; $25,000+ '
                                   'above',
                                   'Chris Barrett, CPA ([36OTOiIXSrk @ 00:01:31])'],
                                  ['Debt service coverage test lenders run on the finished QoE numbers',
                                   'Divide adjusted cash flow by the annual debt payments on the '
                                   'acquisition',
                                   'Most lenders want coverage of at least 1.25 times before funding',
                                   'QoE and Financial Modeling Practice ([yP7oBq_gKbw @ 00:01:03])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Moves The Pros Use To Lock The Numbers Down',
                           'body': 'These are the small procedural habits practitioners say separate a '
                                   'defensible QoE from a closing-table fight.',
                           'items': ['After any working capital meeting, send the seller a written email '
                                     'with the number in bold stating exactly how much stays in the '
                                     'business; one seller agreed to $750,000 in a presentation, then '
                                     'insisted two days before closing they were only leaving $150,000 '
                                     '[Acquira — g_fy5eeJpHE @ 00:38:03]',
                                     'Net every owner compensation add-back against the replacement hire: '
                                     'a $500,000 owner salary with a $350,000 replacement CEO is a '
                                     '$150,000 add-back, not $500,000 [John Colley | The Investment '
                                     'Banking Practitioner — zQE4R-z6Yww @ 00:03:51]',
                                     'Leave account names in the databook exactly as they appear in the '
                                     'source financials; renaming them breaks the auto-populated outputs '
                                     '[Verified Metrics — EzOFN-69wBU @ 00:01:09]',
                                     'Insist on a fixed-fee QoE engagement so quick clarifying calls with '
                                     'the provider never generate surprise bills mid-diligence [Chris '
                                     'Barrett, CPA — 36OTOiIXSrk @ 00:02:52]']},
               'sop_steps': [{'step': 1,
                              'title': 'Define The QoE Scope And Budget',
                              'action': 'Agree in writing what the provider means by quality of earnings '
                                        'before work starts, and budget by deal size and complexity.',
                              'detail': 'There is no standard definition: one buyer gets a one-hour tax '
                                        'accountant review, another a $150,000 three-month Big Four '
                                        'report, so clarify scope right after signing the LOI [Acquira — '
                                        'g_fy5eeJpHE @ 00:07:59]; budget $12,000 to $25,000-plus by '
                                        'revenue, enterprise value, and complexity [Chris Barrett, CPA — '
                                        '36OTOiIXSrk @ 00:01:31].'},
                             {'step': 2,
                              'title': 'Run Proof Of Cash And The Three-Way Tie',
                              'action': 'Reconcile bank activity to the presented financials and the '
                                        'financials to tax returns before touching adjustments.',
                              'detail': 'Tie revenue net of AR movement and expenses net of AP and capex '
                                        'movement to bank statements [Acquira — g_fy5eeJpHE @ 00:05:30]; '
                                        'confirm bank deposits, P&L, and tax returns tell one story or '
                                        'demand an explanation [QoE and Financial Modeling Practice — '
                                        'SBILxsNgW-o @ 00:00:43].'},
                             {'step': 3,
                              'title': 'Build And Interrogate The EBITDA Bridge',
                              'action': 'Walk reported to adjusted to normalized EBITDA, challenging every '
                                        'add-back for evidence and recurrence.',
                              'detail': 'Use the three-column framework and reject any one-time cost seen '
                                        'three years running [John Colley | The Investment Banking '
                                        'Practitioner — zQE4R-z6Yww @ 00:04:50]; throw out any add-back '
                                        'lacking an invoice, payroll record, or truly one-time event [QoE '
                                        'and Financial Modeling Practice — yP7oBq_gKbw @ 00:00:23].'},
                             {'step': 4,
                              'title': 'Set The Debt-Free, Cash-Free Working Capital Peg',
                              'action': 'Strip debt-like items and cash, set the peg from historical '
                                        'monthly data, and size the closing adjustment.',
                              'detail': 'Remove lines of credit, deferred revenue, bank indebtedness, and '
                                        'cash before calculating NWC [Acquira — g_fy5eeJpHE @ 00:18:16]; '
                                        'measure actual NWC at close against the target and reduce price '
                                        'dollar for dollar on any shortfall [Figuring Out with Rahul — '
                                        'xgCInPpZDiQ @ 00:05:05].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['There is no agreed product called a quality of earnings, and practitioners '
                              "split hard on how much of one a buyer should pay for. Acquira's QoE lead "
                              'says there is no unique and standard definition: they have watched a local '
                              'tax accountant spend one hour on the books and call it a QoE, while Big '
                              'Four reports they saw at Deloitte cost $150,000 and took three months '
                              '[g_fy5eeJpHE @ 00:07:27] [g_fy5eeJpHE @ 00:07:44]. Chris Barrett, CPA '
                              'prices the small-deal version as a fixed fee: $12,000 to $15,000 for a '
                              'simple, single-location business under $2.5 million in revenue, roughly '
                              '$14,000 to $23,000 up to $10 million enterprise value, and $25,000-plus on '
                              'a custom scope above that [36OTOiIXSrk @ 00:01:31]. Barrett refuses to sell '
                              'a light option because a skipped step can leave a buyer owning a business '
                              'they regret [36OTOiIXSrk @ 00:02:23]. Jon Stoddard runs the opposite model '
                              'from the sell side, building the QoE in-house with ex-PwC, KPMG and '
                              "Deloitte staff, and calls one buyer's half-million-dollar Big Four QoE on a "
                              '$3 million deal overkill [Yr06Fv79PU0 @ 00:00:49] [Yr06Fv79PU0 @ 00:07:23]. '
                              'Steve Roscioli says QoE is more common in larger or complex deals because '
                              'of the expense, while Acquira insists small deals are where buyers want it '
                              'most [RXawmeZf9sU @ 00:01:13] [g_fy5eeJpHE @ 00:00:50].',
                              'The practitioners also disagree on what kind of animal a QoE is and why the '
                              'numbers are wrong in the first place. Elliott Holland calls it an '
                              'audit-like tool you run because sellers lie about EBITDA, and argues that '
                              'when owners know they are selling at three to five times EBITDA, even the '
                              'most honorable people will hide things between data sets a buyer has no '
                              'time to reconcile [KJPGQ94h_GY @ 00:00:00] [KJPGQ94h_GY @ 00:01:09]. Jon '
                              'Stoddard reads the same gap differently: sellers often get numbers wrong '
                              'without malice, and even their accountants can be wrong, so having an '
                              'accountant does not make the numbers accurate [Yr06Fv79PU0 @ 00:01:09]. '
                              'Edspira lands in between, noting that seller management simply has the '
                              'incentive to make the company look as good as possible, and compares the '
                              'QoE to having a mechanic inspect a used car [itIweMi_DyU @ 00:01:46]. On '
                              'method, Figuring Out with Rahul rejects the audit comparison outright: an '
                              'audit is the referee checking that past plays followed the rules, while a '
                              'QoE is the scout reading game tape to forecast future cash flow '
                              "[xgCInPpZDiQ @ 00:01:22]. Holland's own close is blunt: you cannot overpay "
                              'for an asset, so the QoE exists to validate the EBITDA the multiple sits on '
                              '[KJPGQ94h_GY @ 00:01:43].',
                              'Even add-backs everyone agrees exist get sized differently depending on who '
                              'is across the table. John Colley refuses to add back the full owner salary: '
                              'if the owner takes $500,000 and a replacement CEO costs $350,000, the real '
                              'add-back is $150,000, and on the Summit case a $900,000 founder add-back '
                              'shrinks to $500,000 against a $400,000 replacement [zQE4R-z6Yww @ 00:03:51] '
                              '[zQE4R-z6Yww @ 00:05:30]. Acquira treats post-close costs as negotiation '
                              'rather than math: a buyer whose insurance rises argues a $1 million EBITDA '
                              'business is really $900,000, the seller says that is not their problem, and '
                              'the gap gets bridged with earnout or more forgivable seller note instead of '
                              'a straight cut [g_fy5eeJpHE @ 00:26:42] [g_fy5eeJpHE @ 00:27:34]. Only '
                              'flat-out errors, like a $400,000 add-back that never belonged, get pushed '
                              'as a full purchase-price adjustment [g_fy5eeJpHE @ 00:26:01]. CandiMentor '
                              'splits the audience: a buyer cares about sustainable earnings and future '
                              'value, while a lender focuses on cash conversion, downside protection and '
                              'repayment under pressure [QVDTq7Qd6-A @ 00:05:47]. QoE and Financial '
                              'Modeling Practice shows what that lens means in practice: an add-back '
                              'without an invoice, payroll record or clear one-time event is usually '
                              'thrown out, and most lenders want debt service coverage of at least 1.25 '
                              'times [SBILxsNgW-o @ 00:00:22] [SBILxsNgW-o @ 00:01:02].'],
               'table': {'caption': 'Alternative QoE Playbooks Practitioners Run Side by Side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Who builds the QoE and what it costs',
                                   'Buyer hires a fixed-fee CPA: $12,000 to $15,000 small, $25,000-plus '
                                   'above $10 million',
                                   'Sell-side broker builds it in-house; half-million Big Four QoE on $3 '
                                   'million deal called overkill',
                                   'Chris Barrett, CPA ([36OTOiIXSrk @ 00:01:31]) vs Jon Stoddard '
                                   '([Yr06Fv79PU0 @ 00:07:23])'],
                                  ['Whether a QoE is basically an audit',
                                   'Audit-like outsourced accounting tool that validates the EBITDA the '
                                   'multiple gets applied to',
                                   'Scout reading game tape to forecast future cash flow, not a referee '
                                   'checking rules',
                                   'Elliott Holland ([KJPGQ94h_GY @ 00:01:28]) vs Figuring Out with Rahul '
                                   '([xgCInPpZDiQ @ 00:01:22])'],
                                  ["Why the seller's EBITDA comes in wrong",
                                   'Sellers lie about EBITDA; even honorable people hide things between '
                                   'data sets',
                                   'Often not malicious; sellers and even their accountants simply get the '
                                   'numbers wrong',
                                   'Elliott Holland ([KJPGQ94h_GY @ 00:01:09]) vs Jon Stoddard '
                                   '([Yr06Fv79PU0 @ 00:01:09])'],
                                  ['Whose lens decides which adjustments survive',
                                   'Buyer prices sustainable earnings and future value creation off '
                                   'adjusted EBITDA',
                                   'Lender throws out undocumented add-backs and wants debt service '
                                   'coverage of at least 1.25 times',
                                   'CandiMentor ([QVDTq7Qd6-A @ 00:05:47]) vs QoE and Financial Modeling '
                                   'Practice ([SBILxsNgW-o @ 00:01:02])'],
                                  ['How to close the gap after EBITDA drops',
                                   'Flat-out seller error like a $400,000 bogus add-back becomes a full '
                                   'price cut',
                                   'Gray-area costs like higher insurance get bridged with earnout or '
                                   'forgivable seller note',
                                   'Acquira ([g_fy5eeJpHE @ 00:26:01]); Acquira ([g_fy5eeJpHE @ '
                                   '00:27:34])'],
                                  ['Buy-side versus sell-side diligence posture',
                                   'Buy side acts as professional skeptic actively hunting for reasons to '
                                   'pay less',
                                   'Seller runs the same playbook first; an existing sell-side QoE makes '
                                   'buyer pushback harder',
                                   'Corporate Finance Institute ([FvywvHEpXKU @ 00:06:34]) vs Acquira '
                                   '([g_fy5eeJpHE @ 00:43:14])'],
                                  ['Choosing targets to reduce QoE error risk',
                                   'Recurring Shopify, WooCommerce or SaaS revenue tied to third-party '
                                   'platforms reads cleanest',
                                   'Never buy a poor-fit business just to cut error risk; let QoE experts '
                                   'handle complexity',
                                   'Acquira ([g_fy5eeJpHE @ 00:44:42]); Acquira ([g_fy5eeJpHE @ '
                                   '00:44:56])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures come from add-backs and revenue that collapse '
                              "under the first real tie-out. Acquira's team watched an e-commerce seller "
                              'book a $125,000 purchase order as revenue and receivable before invoicing; '
                              'on a deal with about $425,000 of EBITDA the error ran over 20 percent, and '
                              'the deal died on the spot [g_fy5eeJpHE @ 00:33:13] [g_fy5eeJpHE @ '
                              '00:33:42]. On a $3.2 million EBITDA deal in November 2025, the seller added '
                              'back roughly $500,000 of family payroll that the tax accountant had already '
                              'reclassified to distributions at year end, double counting it; the deal '
                              'went into renegotiation with trust and months lost [g_fy5eeJpHE @ '
                              '00:34:53]. Construction is the repeat offender: the team estimates about 75 '
                              'percent of work-in-progress businesses record WIP wrong, and revenue '
                              'recognition is a main reason EBITDA comes back 10, 20 or 30 percent lower '
                              "[g_fy5eeJpHE @ 00:03:44] [g_fy5eeJpHE @ 00:13:36]. John Colley's Summit "
                              "case shows the subtler version: a $600,000 'one-time' consulting fee in its "
                              'third consecutive year, plus a missed $350,000 hit from a warehouse leased '
                              "from the founder's family trust at 30 percent below market, help shrink "
                              '$18.5 million reported EBITDA to $16.2 million [zQE4R-z6Yww @ 00:05:50] '
                              "[zQE4R-z6Yww @ 00:06:13]. CandiMentor's rule: a 'one-time' cost that shows "
                              'up every year is normal operations [QVDTq7Qd6-A @ 00:06:06].',
                              'Working capital is where deals die late. Acquira ranks the net working '
                              'capital peg among the top two or three deal killers and has lived it: a '
                              "seller's tax accountant netted a line of credit against current assets and "
                              'got roughly $300,000, while a debt-free, cash-free calculation that '
                              'stripped lines of credit, deferred revenue and cash produced $2.1 million '
                              'on an $8.7 million deal [g_fy5eeJpHE @ 00:17:41]. Another seller refused to '
                              'leave any working capital when the buyer needed about $550,000, and the '
                              'deal died; a third agreed to a $750,000 peg in a presentation, then said '
                              'two days before closing they had only ever meant $150,000 [g_fy5eeJpHE @ '
                              '00:35:55] [g_fy5eeJpHE @ 00:37:01]. The fix now is a bolded follow-up email '
                              'spelling out what stays in the business [g_fy5eeJpHE @ 00:37:48]. Figuring '
                              'Out with Rahul describes the protection: set an NWC target from history, '
                              'measure the actual figure at close, and cut the price dollar for dollar on '
                              'any shortfall [xgCInPpZDiQ @ 00:05:05]. Miss the peg and the buyer funds '
                              'payroll and operations out of pocket after close [g_fy5eeJpHE @ 00:20:43]. '
                              'Verified Metrics adds the timing check: a company running consistently '
                              'negative working capital, with a recent three-month average worse than '
                              'longer-term averages, may be leaning on short-term financing to fund '
                              'operations [EzOFN-69wBU @ 00:03:47] [EzOFN-69wBU @ 00:04:03].',
                              'Acquira says roughly half of its 50-plus QoEs last year came back clean, 20 '
                              'to 25 percent surfaced deal-killing mistakes, and the rest needed retrades '
                              'or creative repricing; a small deal averages eight or nine EBITDA '
                              'adjustments, from a low of three to the mid-twenties [g_fy5eeJpHE @ '
                              '00:27:49] [g_fy5eeJpHE @ 00:15:31]. Proof of cash is the first screen: '
                              'Acquira finds it ties about 85 percent of the time, and the businesses that '
                              'miss are ones to run from [g_fy5eeJpHE @ 00:06:00]. The XPX panel agrees '
                              'inventory always ends up on the list and funky revenue accounting always '
                              'brings a cutoff problem; one sell-side software client still carried '
                              'material revenue adjustments after two separate recognition studies '
                              '[gRV7segOzzo @ 00:00:21] [gRV7segOzzo @ 00:01:25]. At scale the same miss '
                              'is catastrophic: Corporate Finance Institute recounts HP paying $11 billion '
                              'for Autonomy, missing channel stuffing and invented sales, and writing down '
                              "$8.8 billion, while Microsoft's Nokia deal ended in a $7.6 billion "
                              'write-off after diligence validated the past but not the market shift '
                              '[FvywvHEpXKU @ 00:09:06] [FvywvHEpXKU @ 00:10:23]. Lenders have their own '
                              'tripwires: QoE and Financial Modeling Practice lists unexplained deposits, '
                              'shrinking margins, personal expenses in the books, and numbers that change '
                              'every version as the signals that make a lender run for the woods '
                              '[yP7oBq_gKbw @ 00:01:23].'],
               'table': {'caption': 'Firsthand Deal Failures and Their Price Tags',
                         'headers': ['Failure Mode',
                                     'What Actually Happened',
                                     'Economic Damage or Fix',
                                     'Expert Source'],
                         'rows': [['Revenue booked on a purchase order',
                                   '$125,000 PO booked as revenue and receivable, still not invoiced six '
                                   'months later',
                                   'Over 20 percent of roughly $425,000 EBITDA erased; deal died on the '
                                   'spot',
                                   'Acquira ([g_fy5eeJpHE @ 00:33:13])'],
                                  ['Double-counted family payroll add-back',
                                   'Seller added back family payroll the tax accountant already moved to '
                                   'distributions',
                                   '$500,000 gap on $3.2 million EBITDA forced renegotiation and months of '
                                   'lost trust',
                                   'Acquira ([g_fy5eeJpHE @ 00:34:53])'],
                                  ['Inventory expensed the day it arrived',
                                   'Seller expensed all inventory through the P&L to cut taxes, holding '
                                   'nothing on the balance sheet',
                                   'COGS overstated and EBITDA understated on a roughly $6 million EBITDA '
                                   'business; margins rebuilt from history',
                                   'Acquira ([g_fy5eeJpHE @ 00:14:14])'],
                                  ['Seller pockets prepaid deferred revenue',
                                   'Med spa seller wanted to keep about $750,000 of prepaid subscriptions, '
                                   'leaving only 10 percent',
                                   'Buyer services those customers post close; take cash retained or walk '
                                   'into trouble',
                                   'Acquira ([g_fy5eeJpHE @ 00:38:51])'],
                                  ['Franchise carve-out with hidden cash needs',
                                   'Franchisor claimed no working capital need across six carved-out '
                                   'locations',
                                   'Security deposits plus first, last and advance rent tied up over '
                                   '$100,000',
                                   'Acquira ([g_fy5eeJpHE @ 00:22:11])'],
                                  ['Below-market related-party lease missed',
                                   "Warehouse leased from the founder's family trust at 30 percent below "
                                   'market, absent from the QoE',
                                   '$350,000 EBITDA hit once rent resets; part of a $2.3 million '
                                   'normalized gap',
                                   'John Colley | The Investment Banking Practitioner ([zQE4R-z6Yww @ '
                                   '00:05:50])'],
                                  ['Starved maintenance and cut costs pre-sale',
                                   'Seller cheaped out on maintenance capex or cut marketing and headcount '
                                   'to lift EBITDA',
                                   'Buyer inherits a hidden equipment bill and the savings disappear after '
                                   'the transaction',
                                   'Figuring Out with Rahul ([xgCInPpZDiQ @ 00:05:35]); CandiMentor '
                                   '([QVDTq7Qd6-A @ 00:03:56])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'OPERATOR GATE: Clear These Four Traps Before Closing',
                           'body': 'Each check below comes from a deal that died, repriced or nearly blew '
                                   'up at the closing table.',
                           'items': ['Run proof of cash first: tie bank deposits and disbursements to the '
                                     'P&L and the P&L to tax returns; businesses where cash does not match '
                                     'are ones to run from [Acquira — g_fy5eeJpHE @ 00:06:16].',
                                     'Put the working capital peg and what it means in a bolded written '
                                     'email to the seller well before closing week; a verbal yes on '
                                     '$750,000 turned into $150,000 two days out [Acquira — g_fy5eeJpHE @ '
                                     '00:37:48].',
                                     'Strike every add-back that lacks an invoice, payroll record or truly '
                                     'one-time event; the lender tosses it overboard anyway, boat included '
                                     '[QoE and Financial Modeling Practice — yP7oBq_gKbw @ 00:00:23].',
                                     'Reclassify any non-recurring cost that has appeared three years '
                                     'running as recurring before it reaches the multiple [John Colley | '
                                     'The Investment Banking Practitioner — zQE4R-z6Yww @ 00:03:34].']}}],
 'pull_quote': '"The quality of earnings report isn\'t an accounting document. It\'s a pricing document. '
               'Every adjustment you accept or challenge directly moves the purchase price." — John Colley '
               '| The Investment Banking Practitioner (zQE4R-z6Yww @ 00:06:50).',
 'diagram_id': 'diag-04',
 'action_checklist': ["Before signing the engagement, confirm in writing exactly what the provider's "
                      'quality of earnings covers, since a one-hour tax-accountant review and a '
                      'three-month $150,000 Big Four report share the same name [Acquira — g_fy5eeJpHE @ '
                      '00:07:44].',
                      'Budget the QoE as a fixed fee by size: $12,000 to $15,000 under $2.5 million '
                      'revenue, about $14,000 to $23,000 up to $10 million enterprise value, and '
                      '$25,000-plus above that [Chris Barrett, CPA — 36OTOiIXSrk @ 00:01:31].',
                      'Build the EBITDA bridge in three columns, reported, adjusted for genuinely '
                      'non-recurring items, and normalized, then price off the third column [John Colley | '
                      'The Investment Banking Practitioner — zQE4R-z6Yww @ 00:04:31].',
                      'Pull monthly P&Ls and monthly adjustments, then hunt for bonuses, PTO payouts and '
                      'large vendor payments landing right after close and push them into net debt or the '
                      'peg [Acquira — g_fy5eeJpHE @ 00:29:42].',
                      'Calculate working capital debt-free and cash-free by stripping lines of credit, '
                      'deferred revenue, bank indebtedness and cash before agreeing to any peg [Acquira — '
                      'g_fy5eeJpHE @ 00:18:16].',
                      "Run the lender's math on the surviving numbers: adjusted cash flow divided by "
                      'annual debt payments must clear at least 1.25 times [QoE and Financial Modeling '
                      'Practice — yP7oBq_gKbw @ 00:01:03].'],
 'statutory_citations': [{'title': 'Acquira — Quality of Earnings Explained: Financial Due Diligence '
                                   'Mistakes That Kill Deals [00:33:13]',
                          'url': 'https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1993s',
                          'relevance': 'Primary practitioner testimony on firsthand deal-killing QoE war '
                                       'stories covering purchase-order revenue, double-counted add-backs, '
                                       'working capital pegs and deferred revenue.'},
                         {'title': 'John Colley | The Investment Banking Practitioner — How to Read a '
                                   "Quality of Earnings Report (M&A Practitioner's Method) [00:05:50]",
                          'url': 'https://www.youtube.com/watch?v=zQE4R-z6Yww&t=350s',
                          'relevance': 'Primary practitioner testimony on missed negative adjustments and '
                                       'the $2.3 million normalized EBITDA gap in the Summit case.'},
                         {'title': 'QoE and Financial Modeling Practice — How Lenders Read a Quality of '
                                   'Earnings (QoE) Report | SBA Loans & Due Diligence [00:01:02]',
                          'url': 'https://www.youtube.com/watch?v=SBILxsNgW-o&t=62s',
                          'relevance': 'Primary practitioner testimony on lender debt service coverage '
                                       'thresholds and red flags in a QoE report.'},
                         {'title': 'Chris Barrett, CPA — How Much Does a Quality of Earnings (QoE) '
                                   'Analysis Cost? [00:01:31]',
                          'url': 'https://www.youtube.com/watch?v=36OTOiIXSrk&t=91s',
                          'relevance': 'Primary practitioner testimony on fixed-fee QoE pricing tiers for '
                                       'small business acquisitions.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'EzOFN-69wBU',
                       'title': 'Quality of Earnings Databook - A Case Walkthrough',
                       'channel': 'Verified Metrics',
                       'author': 'Verified Metrics',
                       'text': 'In the next example, we will show you how to make manual adjustments, '
                               'which is useful when we only want to exclude a partial amount of an '
                               'account.',
                       'tip': 'In the next example, we will show you how to make manual adjustments, which '
                              'is useful when we only want to exclude a partial amount of an account.',
                       'timestamp': 161,
                       'timestamp_seconds': 161,
                       'timestamp_label': '[00:02:41]',
                       'url': 'https://www.youtube.com/watch?v=EzOFN-69wBU&t=161s',
                       'markdown': '[00:02:41](https://www.youtube.com/watch?v=EzOFN-69wBU&t=161s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a5aX7QK8vKA',
                       'title': 'Financial Due Diligence: Quality of Earnings Analysis Step-by-Step',
                       'channel': 'CandiMentor',
                       'author': 'CandiMentor',
                       'text': 'Analysts also look for the reverse problem: costs that management left '
                               'out, even though the buyer will continue paying them.',
                       'tip': 'Analysts also look for the reverse problem: costs that management left out, '
                              'even though the buyer will continue paying them.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=a5aX7QK8vKA&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=a5aX7QK8vKA&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3hIMMSUc5gQ',
                       'title': 'Quality of Earnings (QoE) Explained | Financial Due Diligence Interview '
                                'Questions',
                       'channel': 'CandiMentor',
                       'author': 'CandiMentor',
                       'text': 'Certain indicators suggest poor earnings quality, including significant '
                               'deviations between cash flow and net income, frequent changes in '
                               'accounting policies, and large amounts of non-recurring items.',
                       'tip': 'Certain indicators suggest poor earnings quality, including significant '
                              'deviations between cash flow and net income, frequent changes in accounting '
                              'policies, and large amounts of non-recurring items.',
                       'timestamp': 114,
                       'timestamp_seconds': 114,
                       'timestamp_label': '[00:01:54]',
                       'url': 'https://www.youtube.com/watch?v=3hIMMSUc5gQ&t=114s',
                       'markdown': '[00:01:54](https://www.youtube.com/watch?v=3hIMMSUc5gQ&t=114s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'itIweMi_DyU',
                       'title': 'Quality of Earnings Report',
                       'channel': 'Edspira',
                       'author': 'Edspira',
                       'text': 'If the quality of earnings report finds a significant discrepancy between '
                               'the EBITDA reported by the seller and the adjusted EBITDA, the buyer might '
                               'choose to renegotiate the price or, worst case scenario, just walk away '
                               'from the deal.',
                       'tip': 'If the quality of earnings report finds a significant discrepancy between '
                              'the EBITDA reported by the seller and the adjusted EBITDA, the buyer might '
                              'choose to renegotiate the price or, worst case scenario, just walk away '
                              'from the deal.',
                       'timestamp': 76,
                       'timestamp_seconds': 76,
                       'timestamp_label': '[00:01:16]',
                       'url': 'https://www.youtube.com/watch?v=itIweMi_DyU&t=76s',
                       'markdown': '[00:01:16](https://www.youtube.com/watch?v=itIweMi_DyU&t=76s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QVDTq7Qd6-A',
                       'title': 'Quality of Earnings (QoE) vs EBITDA | Key Differences Explained',
                       'channel': 'CandiMentor',
                       'author': 'CandiMentor',
                       'text': 'Repeated one-time costs are especially revealing because something that '
                               'happens every year is probably part of normal operations rather than a '
                               'genuine exception.',
                       'tip': 'Repeated one-time costs are especially revealing because something that '
                              'happens every year is probably part of normal operations rather than a '
                              'genuine exception.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=QVDTq7Qd6-A&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=QVDTq7Qd6-A&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KJPGQ94h_GY',
                       'title': 'Quality of Earnings Explained',
                       'channel': 'Elliott Holland',
                       'author': 'Elliott Holland',
                       'text': "When sellers know that they're selling for three or five times EBITDA, "
                               'even the most honorable people will lie and hide things in between data '
                               "sets that you don't have time to reconcile and validate.",
                       'tip': "When sellers know that they're selling for three or five times EBITDA, even "
                              'the most honorable people will lie and hide things in between data sets '
                              "that you don't have time to reconcile and validate.",
                       'timestamp': 69,
                       'timestamp_seconds': 69,
                       'timestamp_label': '[00:01:09]',
                       'url': 'https://www.youtube.com/watch?v=KJPGQ94h_GY&t=69s',
                       'markdown': '[00:01:09](https://www.youtube.com/watch?v=KJPGQ94h_GY&t=69s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g_fy5eeJpHE',
                       'title': 'Quality of Earnings Explained: Financial Due Diligence Mistakes That Kill '
                                'Deals',
                       'channel': 'Acquira',
                       'author': 'Acquira',
                       'text': 'The seller received a PO from a large customer and recorded $125,000 of '
                               'revenue and $125,000 of accounts receivable before they had even invoiced '
                               'it.',
                       'tip': 'The seller received a PO from a large customer and recorded $125,000 of '
                              'revenue and $125,000 of accounts receivable before they had even invoiced '
                              'it.',
                       'timestamp': 1993,
                       'timestamp_seconds': 1993,
                       'timestamp_label': '[00:33:13]',
                       'url': 'https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1993s',
                       'markdown': '[00:33:13](https://www.youtube.com/watch?v=g_fy5eeJpHE&t=1993s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g_fy5eeJpHE',
                       'title': 'Quality of Earnings Explained: Financial Due Diligence Mistakes That Kill '
                                'Deals',
                       'channel': 'Acquira',
                       'author': 'Acquira',
                       'text': 'Now, anytime we do a working capital meeting with a seller, I send a huge '
                               'email and bold out what this means: you leave this much in the business.',
                       'tip': 'Now, anytime we do a working capital meeting with a seller, I send a huge '
                              'email and bold out what this means: you leave this much in the business.',
                       'timestamp': 2268,
                       'timestamp_seconds': 2268,
                       'timestamp_label': '[00:37:48]',
                       'url': 'https://www.youtube.com/watch?v=g_fy5eeJpHE&t=2268s',
                       'markdown': '[00:37:48](https://www.youtube.com/watch?v=g_fy5eeJpHE&t=2268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Yr06Fv79PU0',
                       'title': 'Due Diligence,  Quality of Earnings and Why Deals Fail',
                       'channel': 'Jon Stoddard',
                       'author': 'Jon Stoddard',
                       'text': 'They spent half a million dollars, which relative to the size of the deal '
                               'is a good level of diligence, but to me is overkill for a deal that size.',
                       'tip': 'They spent half a million dollars, which relative to the size of the deal '
                              'is a good level of diligence, but to me is overkill for a deal that size.',
                       'timestamp': 443,
                       'timestamp_seconds': 443,
                       'timestamp_label': '[00:07:23]',
                       'url': 'https://www.youtube.com/watch?v=Yr06Fv79PU0&t=443s',
                       'markdown': '[00:07:23](https://www.youtube.com/watch?v=Yr06Fv79PU0&t=443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FvywvHEpXKU',
                       'title': 'Corporate Finance Explained | Financial Due Diligence',
                       'channel': 'Corporate Finance Institute',
                       'author': 'Corporate Finance Institute',
                       'text': 'The due diligence team missed massive accounting irregularities, '
                               'specifically how Autonomy was manipulating revenue by stuffing the channel '
                               'and using complex vendor deals to basically invent sales.',
                       'tip': 'The due diligence team missed massive accounting irregularities, '
                              'specifically how Autonomy was manipulating revenue by stuffing the channel '
                              'and using complex vendor deals to basically invent sales.',
                       'timestamp': 546,
                       'timestamp_seconds': 546,
                       'timestamp_label': '[00:09:06]',
                       'url': 'https://www.youtube.com/watch?v=FvywvHEpXKU&t=546s',
                       'markdown': '[00:09:06](https://www.youtube.com/watch?v=FvywvHEpXKU&t=546s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xgCInPpZDiQ',
                       'title': 'Quality of Earnings Analysis in Mergers and Acquisitions || CFA',
                       'channel': 'Figuring Out with Rahul',
                       'author': 'Figuring Out with Rahul',
                       'text': 'On the day the deal closes, we measure the actual NWC being delivered, and '
                               "if there's a shortfall, the purchase price gets reduced dollar for dollar.",
                       'tip': 'On the day the deal closes, we measure the actual NWC being delivered, and '
                              "if there's a shortfall, the purchase price gets reduced dollar for dollar.",
                       'timestamp': 305,
                       'timestamp_seconds': 305,
                       'timestamp_label': '[00:05:05]',
                       'url': 'https://www.youtube.com/watch?v=xgCInPpZDiQ&t=305s',
                       'markdown': '[00:05:05](https://www.youtube.com/watch?v=xgCInPpZDiQ&t=305s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zQE4R-z6Yww',
                       'title': "How to Read a Quality of Earnings Report (M&A Practitioner's Method)",
                       'channel': 'John Colley | The Investment Banking Practitioner',
                       'author': 'John Colley | The Investment Banking Practitioner',
                       'text': "Summit's warehouse leases with the founder's family trust at 30% below "
                               'market; post close, that rent resets to market, and that $350,000 hit to '
                               'EBITDA is not in the quality of earnings.',
                       'tip': "Summit's warehouse leases with the founder's family trust at 30% below "
                              'market; post close, that rent resets to market, and that $350,000 hit to '
                              'EBITDA is not in the quality of earnings.',
                       'timestamp': 350,
                       'timestamp_seconds': 350,
                       'timestamp_label': '[00:05:50]',
                       'url': 'https://www.youtube.com/watch?v=zQE4R-z6Yww&t=350s',
                       'markdown': '[00:05:50](https://www.youtube.com/watch?v=zQE4R-z6Yww&t=350s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gRV7segOzzo',
                       'title': 'Behind the Numbers: Quality of Earnings in a Transaction',
                       'channel': 'XPX - Exit Planning Exchange',
                       'author': 'XPX - Exit Planning Exchange',
                       'text': 'Others are fairly heavily burdened with all types of costs, sports tickets '
                               'and vacations and repairs to homes and second homes and boats, running '
                               'through a business.',
                       'tip': 'Others are fairly heavily burdened with all types of costs, sports tickets '
                              'and vacations and repairs to homes and second homes and boats, running '
                              'through a business.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=gRV7segOzzo&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=gRV7segOzzo&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '36OTOiIXSrk',
                       'title': 'How Much Does a Quality of Earnings (QoE) Analysis Cost?',
                       'channel': 'Chris Barrett, CPA',
                       'author': 'Chris Barrett, CPA',
                       'text': "If you're buying a business that's under 2.5 million in revenue, is a "
                               "relatively simple industry, and isn't multilocation, you're generally "
                               'going to be somewhere between $12,000 and $15,000 for a quality of '
                               'earnings analysis.',
                       'tip': "If you're buying a business that's under 2.5 million in revenue, is a "
                              "relatively simple industry, and isn't multilocation, you're generally going "
                              'to be somewhere between $12,000 and $15,000 for a quality of earnings '
                              'analysis.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=36OTOiIXSrk&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=36OTOiIXSrk&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SBILxsNgW-o',
                       'title': 'How Lenders Read a Quality of Earnings (QoE) Report | SBA Loans & Due '
                                'Diligence',
                       'channel': 'QoE and Financial Modeling Practice',
                       'author': 'QoE and Financial Modeling Practice',
                       'text': 'Each add back needs support, an invoice, a payroll record, or a clear '
                               'one-time event, and an add back without documentation is usually thrown '
                               'out.',
                       'tip': 'Each add back needs support, an invoice, a payroll record, or a clear '
                              'one-time event, and an add back without documentation is usually thrown '
                              'out.',
                       'timestamp': 22,
                       'timestamp_seconds': 22,
                       'timestamp_label': '[00:00:22]',
                       'url': 'https://www.youtube.com/watch?v=SBILxsNgW-o&t=22s',
                       'markdown': '[00:00:22](https://www.youtube.com/watch?v=SBILxsNgW-o&t=22s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RXawmeZf9sU',
                       'title': 'What Is a Quality of Earnings Report (QoE)?',
                       'channel': 'Steve Roscioli',
                       'author': 'Steve Roscioli',
                       'text': "The review may find that a possible add-back isn't supported, that recent "
                               'revenue includes a one-time project, or that the business will need more '
                               'working capital than expected after it closes.',
                       'tip': "The review may find that a possible add-back isn't supported, that recent "
                              'revenue includes a one-time project, or that the business will need more '
                              'working capital than expected after it closes.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=RXawmeZf9sU&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=RXawmeZf9sU&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yP7oBq_gKbw',
                       'title': 'Why Banks Reject Your EBITDA: How Lenders Read a Quality of Earnings '
                                '(QoE) Report',
                       'channel': 'QoE and Financial Modeling Practice',
                       'author': 'QoE and Financial Modeling Practice',
                       'text': "Banks don't lend on says, they lend on proof, and a quality of earnings "
                               'report is where the proof lives.',
                       'tip': "Banks don't lend on says, they lend on proof, and a quality of earnings "
                              'report is where the proof lives.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=yP7oBq_gKbw&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=yP7oBq_gKbw&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
