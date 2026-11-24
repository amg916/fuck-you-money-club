from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'add-backs-cash-flow-net-working-capital',
 'question_prompt': 'Which EBITDA and SDE add-backs hold up, and how is net working capital defined and '
                    'calculated for a deal?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Add-Backs, Cash Flow, and Calculating Net Working Capital',
 'subtitle': 'Qualifying vs. rejected EBITDA add-backs, common SDE add-backs, the three-question add-back '
             "test, QoE adjustments, why 'EBITDA is an opinion, cash flow is a fact', defining working "
             'capital for the peg, calculating NWC, financial-diligence working capital analysis, the '
             'indirect-method sign logic, and common working-capital issues',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from growthink, The Finance Lab, Transact Capital, A Simple Model and '
                      'John Colley converge on one operating truth: adjusted EBITDA sets the price, but '
                      'working capital and cash conversion decide what the buyer actually gets. growthink '
                      'shows $250,000 of accepted add-backs worth about $1.5 million at six times, with '
                      "the burden of proof on the seller. The Finance Lab's three-question test caps "
                      'credible add-backs near 15 to 20 percent of reported EBITDA and sizes owner pay '
                      'against a replacement salary. Transact Capital adjusts $1.8 million of reported '
                      'working capital to $1.85 million, sets a $1.6 million twelve-month target, and '
                      "books a $143,000 closing excess. Colley's bridge turns $20.7 million of EBITDA into "
                      '$8.1 million of free cash flow. Fault lines run through owner-salary add-backs, '
                      'debt-like liabilities, deferred revenue and lookback periods.',
 'key_metrics': [{'label': 'Enterprise value of accepted add-backs at 6x',
                  'metric': 'Enterprise value of accepted add-backs at 6x',
                  'value': '$250,000 of add-backs = roughly $1.5 million of enterprise value',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Jeff Jones on an LOI valued at six times trailing-twelve-month EBITDA when '
                             'the seller gets full credit for the adjustments',
                  'source': 'growthink ([UfQ-Ho_j61s @ 00:03:52])'},
                 {'label': 'Add-back structural warning threshold',
                  'metric': 'Add-back structural warning threshold',
                  'value': '15% to 20% of reported EBITDA',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A business reporting $5 million of EBITDA with $1.5 million of add-backs '
                             'needs a full forensic review before the numbers can be relied on',
                  'source': 'The Finance Lab ([hIU9zSg4cQg @ 00:00:59])'},
                 {'label': 'Healthy free cash flow conversion for industrials',
                  'metric': 'Healthy free cash flow conversion for industrials',
                  'value': '60% to 80% (Summit case: 39%)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Free cash flow divided by EBITDA; below 50% demands an explanation, and '
                             'Summit converted $20.7 million of normalized EBITDA into $8.1 million of '
                             'free cash flow',
                  'source': 'John Colley | The Investment Banking Practitioner ([ha9dRzcYak4 @ 00:03:17])'},
                 {'label': 'Working capital excess delivered at closing',
                  'metric': 'Working capital excess delivered at closing',
                  'value': '$143,000 excess lifts a $20 million price to $20.14 million',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Estimated closing working capital of $1.75 million against a roughly $1.6 '
                             'million twelve-month target, adjusted dollar for dollar',
                  'source': 'Transact Capital ([YAk3dxgnsBU @ 00:11:52])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner on this beat treats adjusted EBITDA as the number that '
                              'actually gets priced, so every add-back is real money. Jeff Jones of '
                              'growthink frames it in dollars: at six times trailing-twelve-month EBITDA '
                              'in an LOI, $250,000 of accepted add-backs equals roughly $1.5 million of '
                              'enterprise value, which is why sellers fight for full credit and buyers '
                              'stay skeptical [UfQ-Ho_j61s @ 00:03:52]. Elliott Holland walks the same '
                              "chain from the buyer's chair: start with EBITDA as reported, review every "
                              'adjustment for things the owner ran through the business that a new owner '
                              'will not pay for, then land on the final adjusted EBITDA you will be paying '
                              'a multiple of [XDVFloSBuko @ 00:00:18]. The Finance Lab calls the adjusted '
                              'EBITDA schedule the place where deals are made and lost and where sellers '
                              'are most creative, with every line an argument that a cost did not really '
                              'happen, will not recur, or leaves with the owner [hIU9zSg4cQg @ 00:00:00]. '
                              'The shared rule underneath: the burden of proof sits with the seller, and '
                              'adjustments do not fly without clear, consistent documentation tracked over '
                              'time, because buyers come in naturally skeptical and a trend backed by '
                              'records is what gets everyone comfortable [UfQ-Ho_j61s @ 00:09:04].',
                              "The categories line up across shops. growthink's Antonio lists the standard "
                              'accepted buckets: one-time items such as legal settlements, advisory fees '
                              'tied to an initiative, plant relocation and transaction financing costs; '
                              'owner discretionary spend where family expenses flow through the company '
                              'for tax mitigation; owner compensation only to the extent it runs above '
                              'market rate; related-party rent normalized plus or minus to market; and, on '
                              'services deals, equity taken as compensation [UfQ-Ho_j61s @ 00:10:45]. '
                              'Edspira sorts quality of earnings work into three groups: non-recurring or '
                              'non-operational adjustments like asset impairments, disposal gains or '
                              'losses, lease termination fees and severance; pro forma adjustments that '
                              'push recent rent, salary or raw-material increases into historical EBITDA; '
                              'and accounting adjustments that convert cash-basis books to accrual or '
                              'reverse improperly capitalized expenses and misrecognized revenue '
                              "[j5A0VGOV88E @ 00:00:14]. ProjectionHub's Adam runs four buckets in its "
                              'free SDE calculator template: owner compensation, personal expenses such as '
                              'a $10,000-a-year personal vehicle billed through the business, non-cash '
                              'depreciation and amortization, and one-time costs like a $25,000 move '
                              '[OiLlMiZv9ZQ @ 00:01:47]. Kirk Michie adds the direction check most owners '
                              'miss: owner economics such as self-owned buildings rented below or above '
                              'market and blended personal trips must be recalibrated, and a few of those '
                              'adjustments push EBITDA down, not up [BHyx6-mgFe8 @ 00:00:55].',
                              'On the balance sheet side, the consensus is that deals close cash-free and '
                              'debt-free with a normalized level of working capital left behind. Ross '
                              'Harris of Transact Capital says that is how 90 to 95 percent of deals work: '
                              'the seller keeps the cash, pays off debts two or three days before closing, '
                              'and leaves the buyer a fair level of working capital, and the seller does '
                              'not get to choose how much gas the car needs because a process sets it '
                              '[YAk3dxgnsBU @ 00:00:31]. Kirk Michie reduces deal-math working capital to '
                              'accounts receivable plus inventory minus accounts payable, including taxes '
                              'payable in a pass-through LLC or S corp, and warns the peg draws lots and '
                              'lots of post-purchase disputes [QqemANnN2ZM @ 00:00:43]. Morse frames the '
                              "buyer's motive as refusing to buy a business with the cupboards bare, with "
                              'buyer and seller negotiating a target equal to the cash and working capital '
                              'needed for a month or two of operations so the buyer does not have to '
                              'inject cash after closing [0V-By_uyuhM @ 00:00:20]. A Simple Model draws '
                              'the line between accounting and deal definitions: cash is excluded, not '
                              'every current account is included, and accrued taxes, litigation accounts, '
                              'lines of credit, notes payable and current debt are common carve-outs '
                              '[DbHq5BHo_XA @ 00:01:16].'],
               'table': {'caption': 'Where the practitioners agree on add-backs and working capital',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Adjusted EBITDA is the number buyers actually price',
                                   'Accepted add-backs flow through the LOI multiple into enterprise value',
                                   'At six times TTM, $250,000 of credited add-backs is worth about $1.5 '
                                   'million',
                                   'growthink ([UfQ-Ho_j61s @ 00:03:52])'],
                                  ['Burden of proof sits squarely with the seller',
                                   'Adjustments do not fly without clear, consistent, tracked '
                                   'documentation over time',
                                   'Track add-backs monthly so the trend is already evidenced at exit',
                                   'growthink ([UfQ-Ho_j61s @ 00:09:04])'],
                                  ['Owner economics must be recalibrated before buyers see numbers',
                                   'Related-party rent and blended personal trips get adjusted either up '
                                   'or down',
                                   'Expect a few adjustments to lower EBITDA, not only raise it',
                                   'Kirk Michie ([BHyx6-mgFe8 @ 00:01:16])'],
                                  ['Every add-back is an argument the seller must win',
                                   'Costs either did not happen, will not recur, or leave with the owner',
                                   'Rebuild the schedule yourself and treat the seller version as a '
                                   'starting point',
                                   'The Finance Lab ([hIU9zSg4cQg @ 00:00:00])'],
                                  ['Quality of earnings adjustments fall into three families',
                                   'Non-recurring, pro forma normalizing, and accounting corrections like '
                                   'cash-to-accrual conversion',
                                   'Push recent rent, salary, and raw-material increases into historical '
                                   'EBITDA',
                                   'Edspira ([j5A0VGOV88E @ 00:00:31])'],
                                  ['Deals close cash-free and debt-free with normalized working capital',
                                   'Seller keeps cash, pays off debt, and leaves a fair working capital '
                                   'level',
                                   'Roughly 90 to 95 percent of deals follow this exact process',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:00:31])'],
                                  ['Working capital peg protects buyers from an empty tank',
                                   'Buyer should not need to fund payroll or payables right after closing',
                                   'Never agree to the peg formula in an LOI without understanding it',
                                   'Kirk Michie ([QqemANnN2ZM @ 00:03:07])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Add-back vetting runs on a three-question test from The Finance Lab: was it '
                              'truly non-recurring, would a new owner actually save it, and is the amount '
                              'reasonable. On the first question, ask for the invoice behind any legal '
                              'add-back, because one litigation settlement passes while a pattern of '
                              'recurring disputes fails; on the second, a seller paying themselves '
                              '$900,000 against a $350,000 replacement CEO supports a $550,000 add-back '
                              'only if you will really hire at that salary and the owner was doing one '
                              "person's job [hIU9zSg4cQg @ 00:00:38]. The reasonableness bar is hard: "
                              'add-backs above 15 to 20 percent of reported EBITDA are a structural '
                              'warning, and $1.5 million of add-backs on $5 million of EBITDA means the '
                              'books need a full forensic review [hIU9zSg4cQg @ 00:00:59]. ProjectionHub '
                              'runs the same math smaller: a $100,000 owner salary against a $75,000 '
                              'replacement hire nets a $25,000 add-back, settled by negotiation '
                              '[OiLlMiZv9ZQ @ 00:02:09]. Elliott Holland measures total adjustments as a '
                              'percentage of adjusted EBITDA on a trailing-twelve-month basis, then strips '
                              "out the seller's salary: two-thirds looks large, but once the $1 million "
                              'salary is pulled, the remaining $300,000 is not significant against $1.8 '
                              "million [XDVFloSBuko @ 00:00:36]. The Finance Lab's closing instruction is "
                              "to rebuild the adjusted EBITDA schedule from scratch, treating the seller's "
                              'version as a starting point, never a conclusion.',
                              "Transact Capital's working capital build is the cleanest worked example. "
                              'Run the internal balance sheet: $7.5 million of current assets minus $5.7 '
                              'million of current liabilities gives $1.8 million of reported working '
                              'capital; zero out cash and the line of credit and definitional working '
                              'capital drops to $1.3 million [YAk3dxgnsBU @ 00:04:04]. Then strip tax '
                              'items and debt-like liabilities: the deferred tax asset generally always '
                              'goes, credit card payables are almost always debt-like unless the card '
                              'replaces the payables account, commissions payable go debt-like about 80 '
                              'percent of the time, and vacation PTO is a 50-50 fight, landing adjusted '
                              'working capital at $1.85 million. Run that same formula monthly; the '
                              'six-month average is $1.575 million and the twelve-month average $1.607 '
                              'million, and the twelve-month average is most common for stable businesses '
                              '[YAk3dxgnsBU @ 00:09:42]. A Simple Model shows a balance-level carve-out: '
                              'excluding receivables aged over 90 days cuts $10 million of AR to $8.3 '
                              'million because the buyer should not pay for cash it may never collect '
                              "[DbHq5BHo_XA @ 00:02:38]. CandiMentor's distributor case nets $18 million "
                              'receivables plus $12 million inventory minus $14 million payables and $4 '
                              'million accruals to a $12 million target; a $14.4 million closing balance '
                              'hands the seller a potential $2.4 million adjustment [siH_wi11PX8 @ '
                              '00:04:31].',
                              'The true-up follows a fixed sequence. A Simple Model lays it out: agree a '
                              'target, close with part of the price parked in a working capital escrow, '
                              'give the buyer 60 to 120 days to deliver a closing statement, then give the '
                              'seller roughly 30 days to object in writing with reasonable detail; signing '
                              'the working capital calculation agreement releases escrow, with excess paid '
                              'to the seller and shortfall released to the buyer [C-seCQXqtM4 @ 00:01:47]. '
                              'MCM Capital says the items that most often drive the adjustment start with '
                              'accruals, such as earned-but-unpaid bonuses when closing near year-end, and '
                              'inventory, which MCM always suggests settling with a physical count at '
                              'close, especially in manufacturing [almKwAlo5T4 @ 00:00:34]. John Colley '
                              "then bridges adjusted earnings to cash: Summit's $20.7 million of "
                              'normalized EBITDA loses $6.2 million to maintenance CapEx, $1.8 million to '
                              'working capital, $2.8 million to cash taxes, $1.2 million to interest and '
                              '$0.6 million to other items, leaving $8.1 million of free cash flow, a 39 '
                              'percent conversion against a healthy 60 to 80 percent for industrials '
                              "[ha9dRzcYak4 @ 00:06:43]. Colley's punchline: the $180 million headline at "
                              '8.7 times normalized EBITDA is really 22 times free cash flow, so debt '
                              'paydown will be slow.'],
               'table': {'caption': 'Street mechanics: the exact numbers and rules operators run',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Run It',
                                     'Expert Source'],
                         'rows': [['Owner compensation add-back sizing against replacement cost',
                                   '$900,000 owner pay minus $350,000 replacement CEO equals $550,000 '
                                   'add-back',
                                   'Credit it only if you will actually hire at that salary',
                                   'The Finance Lab ([hIU9zSg4cQg @ 00:00:38])'],
                                  ['Add-back reasonableness ceiling on reported EBITDA',
                                   'Add-backs above 15 to 20 percent of reported EBITDA flag trouble',
                                   'At $1.5 million on $5 million, order a full forensic review',
                                   'The Finance Lab ([hIU9zSg4cQg @ 00:00:59])'],
                                  ['Definitional working capital after cash and debt removal',
                                   '$7.5 million assets minus $5.7 million liabilities, then cash and '
                                   'credit line zeroed to $1.3 million',
                                   'Run the internal QuickBooks balance sheet, then zero cash and debt '
                                   'lines',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:04:04])'],
                                  ['Debt-like liability classification odds in negotiation',
                                   'Commissions payable debt-like 80 percent of the time; vacation PTO is '
                                   '50-50',
                                   'Credit cards stay in only if they replace the payables account',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:06:40])'],
                                  ['Working capital target lookback period selection',
                                   'Six-month average $1.575 million versus twelve-month average $1.607 '
                                   'million',
                                   'Use the twelve-month monthly average for stable businesses, most '
                                   'common in deals',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:09:42])'],
                                  ['Aged receivables carve-out from the peg calculation',
                                   'Excluding AR over 90 days cuts $10 million down to $8.3 million',
                                   'Let the seller chase old balances instead of paying for them',
                                   'A Simple Model ([DbHq5BHo_XA @ 00:02:38])'],
                                  ['EBITDA to free cash flow conversion bridge',
                                   '$20.7 million normalized EBITDA converts to $8.1 million free cash '
                                   'flow, 39 percent',
                                   'Subtract maintenance CapEx, working capital change, cash taxes, and '
                                   'cash interest',
                                   'John Colley | The Investment Banking Practitioner ([ha9dRzcYak4 @ '
                                   '00:06:43])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the pros protect add-back credit and the working capital number',
                           'body': 'These are the moves practitioners use to keep add-backs from getting '
                                   'haircut in quality of earnings and to keep the working capital peg '
                                   'from turning into a post-close fight.',
                           'items': ['Run personal pass-through expenses on one credit card and track '
                                     'add-backs monthly so they can be brought back cleanly at transaction '
                                     'time [growthink — UfQ-Ho_j61s @ 00:14:50]',
                                     'Build your own adjusted EBITDA schedule from scratch and use the '
                                     "seller's schedule only as a starting point, never a conclusion [The "
                                     'Finance Lab — hIU9zSg4cQg @ 00:01:19]',
                                     'Split maintenance from growth CapEx with one test: if all CapEx '
                                     'stopped, what breaks within 12 months; demand a three-year breakdown '
                                     'by asset category [John Colley | The Investment Banking Practitioner '
                                     '— ha9dRzcYak4 @ 00:03:57]',
                                     'Lock the working capital target lookback period at the LOI stage '
                                     'even though the full formula cannot be agreed until diligence is '
                                     'done [Transact Capital — YAk3dxgnsBU @ 00:12:57]']},
               'sop_steps': [{'step': 1,
                              'title': 'Itemize adjusted EBITDA in the model',
                              'action': 'Bake an itemized adjusted EBITDA line into the annual financial '
                                        'model, historical and forecast.',
                              'detail': 'Show reported EBITDA, each adjustment, and normalized adjusted '
                                        'EBITDA so strategic and financial buyers can verify it quickly '
                                        'and give full credit [growthink — UfQ-Ho_j61s @ 00:35:59]'},
                             {'step': 2,
                              'title': 'Run every add-back through the three-question test',
                              'action': 'Test each line for non-recurrence, real cost savings to a new '
                                        'owner, and reasonable size.',
                              'detail': 'Pull the invoice on legal add-backs, size owner pay against a '
                                        'replacement salary, and flag totals above 15 to 20 percent of '
                                        'reported EBITDA [The Finance Lab — hIU9zSg4cQg @ 00:00:20]'},
                             {'step': 3,
                              'title': 'Map the ledger and set the working capital target',
                              'action': 'Strip cash, debt, tax items and agreed debt-like liabilities, '
                                        'then average adjusted monthly working capital.',
                              'detail': 'Apply the locked formula to prior months and take a 3, 6 or 12 '
                                        'month average, with 12 months most common for stable businesses '
                                        '[Transact Capital — YAk3dxgnsBU @ 00:09:24]'},
                             {'step': 4,
                              'title': 'Bridge EBITDA to free cash flow before pricing',
                              'action': 'Subtract maintenance CapEx, working capital change, cash taxes '
                                        'and cash interest from normalized EBITDA.',
                              'detail': 'Compute the conversion ratio and implied free cash flow multiple; '
                                        'below 60 percent, find exactly where the cash goes [John Colley | '
                                        'The Investment Banking Practitioner — ha9dRzcYak4 @ 00:02:57]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on add-backs is where the alarm bell should ring. The '
                              'Finance Lab draws a hard line: add-backs above 15 to 20% of reported EBITDA '
                              'are a structural warning signal, and a business reporting $5 million of '
                              'EBITDA with $1.5 million in add-backs is telling you the financials sit so '
                              'far from economic reality that nothing can be relied on without a full '
                              "forensic review [hIU9zSg4cQg @ 00:00:59]. growthink's Antonio runs a far "
                              'looser tolerance, saying add-backs at 30%, 40%, 50% or more of adjusted '
                              'EBITDA do not mean automatic rejection, only that the buyer leans in harder '
                              'and starts asking whether those numbers will hold through quality of '
                              'earnings or whether the offer is wasted diligence money [UfQ-Ho_j61s @ '
                              '00:22:00]. Elliott Holland splits the difference by decomposing the ratio '
                              'instead of reacting to it: adjustments running two-thirds of adjusted '
                              'EBITDA look ugly until you pull out the $1 million seller salary, at which '
                              'point the remaining $300,000 is not significant against $1.8 million '
                              '[XDVFloSBuko @ 00:00:58]. The operator playbook that falls out of this is '
                              'simple: screen the headline ratio Finance Lab-style, strip owner '
                              'compensation the Holland way, then test whatever remains before deciding '
                              'whether the deal deserves forensic money or a polite pass.',
                              'Owner compensation is the add-back everyone fights over, and practitioners '
                              'price it in at least three different ways. ProjectionHub warns that sellers '
                              'routinely add back the full salary, say $100,000, when the buyer must hire '
                              'a $75,000 replacement to do the same job, so only $25,000 belongs in SDE, '
                              'and even that figure is a negotiation between buyer and seller [OiLlMiZv9ZQ '
                              '@ 00:02:26]. The Finance Lab runs identical math at middle-market scale, '
                              '$900,000 of owner pay against a $350,000 replacement CEO for a $550,000 '
                              'add-back, but attaches two conditions: the buyer must actually plan to hire '
                              'at that salary, and the owner must genuinely have been doing the work of '
                              'one person [hIU9zSg4cQg @ 00:00:38]. growthink goes further in multi-owner '
                              'shops, carving out compensation entirely when a retiring owner will not be '
                              'replaced post-close, while flagging that owner pay is not an add-back per '
                              'se, only the above-market slice is [UfQ-Ho_j61s @ 00:12:11]. Edspira pushes '
                              'the opposite direction, insisting pro forma adjustments also cut EBITDA '
                              'when rent, salaries, or raw materials have recently risen, because '
                              'historical statements are backward looking [j5A0VGOV88E @ 00:00:49]. '
                              'Sellers chasing the full-salary add-back should expect buyers armed with '
                              'the replacement-cost test, and buyers should expect sellers to argue '
                              'redundancy.',
                              'On net working capital, the definitional fights are where practitioners '
                              'openly contradict each other, and taxes are the cleanest example. Kirk '
                              "Michie's deal-math formula is receivables plus inventory minus payables, "
                              'explicitly including taxes payable in a pass-through LLC or S corp '
                              "[QqemANnN2ZM @ 00:00:43]. Transact Capital's Ross Harris takes the opposite "
                              "line: anything tax related is the seller's responsibility, is not assumed "
                              'by the buyer at closing, and gets removed from the calculation [YAk3dxgnsBU '
                              '@ 00:04:35]. Break Into Finance refuses both absolutes, arguing that '
                              'regular current tax obligations cycling in and out can be argued as working '
                              'capital, while a large unpaid income tax liability is probably a net debt '
                              'item, and the outcome depends on how the negotiation goes [S31vo0Umk5M @ '
                              '00:38:12]. Deferred revenue splits the room the same way. MCM Capital '
                              'frames customer prepayments as a loan from your customer, more often than '
                              'not treated as debt rather than working capital, yet admits they have seen '
                              'it go both ways in the final contract definitions [almKwAlo5T4 @ 00:02:08]. '
                              'The operator read is blunt: each of these lines is a direct price lever on '
                              'both sides of the table, and whoever writes the inclusion schedule controls '
                              'the size of the closing check.'],
               'table': {'caption': 'Contested add-back and working capital calls, side by side, as '
                                    'practitioners actually play them',
                         'headers': ['Contested Issue', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Where the add-back ratio alarm should ring',
                                   'Add-backs above 15 to 20% of reported EBITDA trigger a full forensic '
                                   'review',
                                   'Add-backs at 30, 40, 50% or more draw extra scrutiny, not automatic '
                                   'rejection',
                                   'The Finance Lab ([hIU9zSg4cQg @ 00:00:59]); growthink ([UfQ-Ho_j61s @ '
                                   '00:22:00])'],
                                  ['How much owner compensation gets added back',
                                   'Add back only pay above replacement cost, e.g. $25,000 of a $100,000 '
                                   'salary',
                                   'Carve out the full owner salary when a retiring owner is not replaced',
                                   'ProjectionHub ([OiLlMiZv9ZQ @ 00:02:41]); growthink ([UfQ-Ho_j61s @ '
                                   '00:12:31])'],
                                  ['Whether taxes payable sit inside the peg',
                                   'Include taxes payable for a pass-through LLC or S corp in deal math',
                                   'Strip every tax-related line because taxes stay with the seller at '
                                   'close',
                                   'Kirk Michie ([QqemANnN2ZM @ 00:00:43]); Transact Capital ([YAk3dxgnsBU '
                                   '@ 00:04:35])'],
                                  ['How to classify deferred revenue and customer deposits',
                                   'Treat upfront customer cash as a customer loan usually classified as '
                                   'debt',
                                   'Keep recurring deferred revenue, like subscriptions, inside working '
                                   'capital as normal trading',
                                   'MCM Capital ([almKwAlo5T4 @ 00:02:08]); Break Into Finance '
                                   '([S31vo0Umk5M @ 00:41:52])'],
                                  ['How long the target lookback period should run',
                                   'Twelve-month average of adjusted NWC is most common for stable '
                                   'businesses',
                                   'Cover at least two annual cycles, ideally three to four years monthly',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:09:42]); Break Into Finance '
                                   '([S31vo0Umk5M @ 01:01:08])'],
                                  ['Whether credit cards and PTO count as debt',
                                   'Credit cards are almost always debt-like; vacation and PTO is a 50/50 '
                                   'fight',
                                   'Seller argues card balances recur, get paid monthly, and crystallize '
                                   'to cash',
                                   'Transact Capital ([YAk3dxgnsBU @ 00:06:54]); Break Into Finance '
                                   '([S31vo0Umk5M @ 00:34:27])'],
                                  ['Which number the headline price really anchors on',
                                   'Enterprise value pegged on adjusted EBITDA multiples, with add-backs '
                                   'credited at the multiple',
                                   'Price the implied free cash flow multiple; $180 million at 8.7x EBITDA '
                                   'is 22x FCF',
                                   'growthink ([UfQ-Ho_j61s @ 00:02:54]); John Colley | The Investment '
                                   'Banking Practitioner ([ha9dRzcYak4 @ 00:07:26])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive add-back failure is the last-mile retrade. growthink '
                              'reports that the majority of the time, once the quality of earnings report '
                              'lands with the buyer, there is pushback and an attempted haircut to '
                              'add-backs or EBITDA, and that is exactly when deals blow up [UfQ-Ho_j61s @ '
                              '00:18:34]. The trap usually starts with categories sellers assume are '
                              'one-time. In one growthink case, bad debts appeared on the P&L every single '
                              'year, which already proved they were not non-recurring and would struggle '
                              'to survive as add-backs [UfQ-Ho_j61s @ 00:33:07]. The Finance Lab applies '
                              'the same logic to legal fees: one litigation settlement is legitimate, a '
                              'pattern of recurring legal disputes is not, and the buyer should demand to '
                              'see the invoice before crediting a dollar [hIU9zSg4cQg @ 00:00:20]. The '
                              'economics are brutal in both directions. At six times trailing EBITDA, '
                              '$250,000 of accepted adjustments is worth $1.5 million of enterprise value '
                              'if the seller gets full credit [UfQ-Ho_j61s @ 00:03:52]. That multiplier '
                              'cuts both ways: every line a buyer strikes during diligence comes off the '
                              'price at six times its face value, so a seller defending a weak add-back is '
                              'defending value that was never really there.',
                              'Working capital is where signed deals go to die after the handshake. Kirk '
                              'Michie says nondisclosure agreements almost never trigger lawsuits, but net '
                              'working capital pegs and formulas generate lots and lots of post-purchase '
                              'disputes, and the letter of intent is a ceiling that only gets worse '
                              "afterward [QqemANnN2ZM @ 00:03:07]. Transact Capital's Ross Harris has "
                              'watched deals die over working capital when sellers did not understand the '
                              'process, with closings turning contentious and deal threatening '
                              '[YAk3dxgnsBU @ 00:12:43]. The post-close clock is unforgiving. A Simple '
                              'Model lays out the timeline: the buyer gets 60 to 120 days to deliver a '
                              'closing statement, the seller gets roughly 30 days to review it, and any '
                              'disagreement must be delivered in writing with reasonable detail before '
                              'that window expires, while escrowed funds stay frozen until both sides sign '
                              '[C-seCQXqtM4 @ 00:02:18]. Break Into Finance flags the gaming risk built '
                              'into the mechanism itself: a seller who understands cyclicality can let the '
                              'peg get set off a trough month and then close in a known peak month like '
                              'January to harvest a big purchase price uplift [S31vo0Umk5M @ 00:24:20]. '
                              'Sellers who sleep through the review window and buyers who accept a '
                              'trough-based peg both eat the loss.',
                              'The final economics check is whether the cash actually shows up. John '
                              'Colley has seen companies report $20 million of EBITDA yet generate only $8 '
                              'million of free cash flow, with $12 million vanishing into working capital, '
                              'maintenance CapEx, and customer deposits that never materialized '
                              '[ha9dRzcYak4 @ 00:00:25]. His Summit Services walkthrough turns $20.7 '
                              'million of normalized EBITDA into $8.1 million of free cash flow, a 39% '
                              'conversion ratio against the 60 to 80% a healthy industrial services '
                              'business should post, and he calls that result poor without hedging '
                              '[ha9dRzcYak4 @ 00:06:43]. Day one is its own trap. Break Into Finance walks '
                              'through a target with two cash outflows in the first week, a payroll run '
                              'and a supplier run, before the first customer collection lands, and advises '
                              'PE buyers without a treasury function to make the vendor leave enough cash '
                              'or stand up a revolver immediately [S31vo0Umk5M @ 00:57:05]. MCM Capital '
                              'adds the inventory landmine: they always push for a physical inventory at '
                              'close, especially for manufacturers, because gaps between the books and the '
                              'warehouse that were never trued up surface right when the adjustment gets '
                              'calculated [almKwAlo5T4 @ 00:00:34]. Every one of these gaps is cash '
                              'somebody funds after closing.'],
               'table': {'caption': 'Firsthand traps, what they cost, and the countermove practitioners '
                                    'use',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics / Countermove',
                                     'Expert Source'],
                         'rows': [['Quality of earnings haircut triggers a last-mile retrade',
                                   'Buyer pushes back post-QoE and haircuts add-backs, which is when deals '
                                   'blow up',
                                   'Run an informal pre-market QoE so the adjusted EBITDA survives buyer '
                                   'diligence',
                                   'growthink ([UfQ-Ho_j61s @ 00:18:34])'],
                                  ['Recurring costs dressed up as one-time add-backs',
                                   'Bad debts showed up every year, proving they were not non-recurring',
                                   'Only claim items tied to a genuine one-time event, with explanation '
                                   'attached',
                                   'growthink ([UfQ-Ho_j61s @ 00:33:07])'],
                                  ['Pricing a deal on EBITDA that never converts',
                                   "Summit's $20.7 million normalized EBITDA produced only $8.1 million of "
                                   'free cash flow',
                                   'Investigate any conversion ratio below 60% before accepting the '
                                   'headline multiple',
                                   'John Colley | The Investment Banking Practitioner ([ha9dRzcYak4 @ '
                                   '00:06:43])'],
                                  ['Agreeing to a working capital peg in the LOI blind',
                                   'Net working capital formulas drive lots and lots of post-purchase '
                                   'disputes',
                                   'Treat the LOI as a ceiling and nail the formula down up front',
                                   'Kirk Michie ([QqemANnN2ZM @ 00:03:07])'],
                                  ['Paying full value for stale receivables inside the peg',
                                   'Excluding receivables over 90 days cut $10 million of AR to $8.3 '
                                   'million',
                                   'Let the seller chase the aged balances instead of buying the '
                                   'collection risk',
                                   'A Simple Model ([DbHq5BHo_XA @ 00:02:38])'],
                                  ['Modeling the working capital baseline off a trough month',
                                   'Straight-line assumption from a January trough left buyers injecting '
                                   'cash later',
                                   'Map working capital monthly and set aside funds for the seasonal peak',
                                   'Break Into Finance ([S31vo0Umk5M @ 00:19:44])'],
                                  ['Reading a payables increase as a cash drain',
                                   'Students subtract a $3,000 payables increase because more debt means '
                                   'less cash',
                                   'Add operating payable increases; they postpone cash payments under the '
                                   'indirect method',
                                   'Accounting Rescue with Lisa ([t0rj9LcHTgw @ 00:05:16])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before You Sign',
                           'body': 'Each gate comes straight from a loss, dispute, or retrade the '
                                   'practitioners watched happen. Clear all four before the purchase '
                                   'agreement locks the numbers.',
                           'items': ['Do not agree to a net working capital peg in the letter of intent '
                                     'until you understand exactly what the formula means, because the LOI '
                                     'is a ceiling that only gets worse [Kirk Michie — QqemANnN2ZM @ '
                                     '00:03:07].',
                                     'Strike any add-back that fails the three-question test: truly '
                                     'non-recurring, actually saved by a new owner, and reasonable in '
                                     'size, and demand the invoice behind every legal fee [The Finance Lab '
                                     '— hIU9zSg4cQg @ 00:00:20].',
                                     'Build the EBITDA-to-free-cash-flow bridge and, if conversion lands '
                                     'below 60%, find exactly where the cash is going and whether that is '
                                     'fixable [John Colley | The Investment Banking Practitioner — '
                                     'ha9dRzcYak4 @ 00:08:30].',
                                     'Map day-one cash obligations against collection dates and make the '
                                     'vendor leave enough cash or put a revolver or overdraft in place '
                                     'immediately [Break Into Finance — S31vo0Umk5M @ 00:57:05].']}}],
 'pull_quote': "EBITDA is an opinion. Cash flow is a fact. If you're pricing a deal on EBITDA, but the "
               "cash isn't there, you're buying a mirage. — John Colley | The Investment Banking "
               'Practitioner (ha9dRzcYak4 @ 00:00:01).',
 'diagram_id': 'diag-05',
 'action_checklist': ["Rebuild the adjusted EBITDA schedule from scratch, using the seller's schedule as a "
                      'starting point rather than a conclusion, and run every line through the '
                      'three-question test [The Finance Lab — hIU9zSg4cQg @ 00:01:37].',
                      'Track add-backs monthly inside the operating model and run personal pass-through '
                      'expenses on one credit card so every item is clean, tracked, and evidenced at '
                      'transaction time [growthink — UfQ-Ho_j61s @ 00:14:50].',
                      'Rerun the adjusted net working capital calculation for each historical month and '
                      'set the target off the 12-month average, the most common choice for stable '
                      'businesses [Transact Capital — YAk3dxgnsBU @ 00:09:42].',
                      'Negotiate exclusions for receivables aged 90 days or more and obsolete inventory so '
                      'the peg only pays for balances that will actually convert to cash [A Simple Model — '
                      'DbHq5BHo_XA @ 00:02:07].',
                      'Take a physical inventory at close, especially in manufacturing, and reconcile '
                      'book-to-warehouse differences well before the adjustment mechanism is triggered '
                      '[MCM Capital — almKwAlo5T4 @ 00:00:34].',
                      'Separate maintenance CapEx from growth CapEx by asking what breaks within 12 months '
                      'if all CapEx stops, and request a three-year breakdown by asset category [John '
                      'Colley | The Investment Banking Practitioner — ha9dRzcYak4 @ 00:03:38].'],
 'statutory_citations': [{'title': 'John Colley | The Investment Banking Practitioner — EBITDA Is an '
                                   'Opinion. Cash Flow Is a Fact. (M&A Practitioner Walkthrough) '
                                   '[00:06:43]',
                          'url': 'https://www.youtube.com/watch?v=ha9dRzcYak4&t=403s',
                          'relevance': 'Primary practitioner testimony on the EBITDA-to-free-cash-flow '
                                       'bridge and the 39% Summit Services conversion ratio.'},
                         {'title': 'Transact Capital — Investment Banking - How To Calculate Net Working '
                                   'Capital for an M&A Transaction - Transact Capital [00:06:23]',
                          'url': 'https://www.youtube.com/watch?v=YAk3dxgnsBU&t=383s',
                          'relevance': 'Primary practitioner testimony on definitional and debt-like '
                                       'working capital adjustments, target lookbacks, and closing '
                                       'true-ups.'},
                         {'title': 'growthink — Qualifying EBITDA Add-Backs - Separating Fact From Fiction '
                                   '| Masterclass [00:18:34]',
                          'url': 'https://www.youtube.com/watch?v=UfQ-Ho_j61s&t=1114s',
                          'relevance': 'Primary practitioner testimony on add-back credibility, quality of '
                                       'earnings haircuts, and retrade risk.'},
                         {'title': 'Break Into Finance — Net Working Capital Adjustment - M&A Transactions '
                                   '(#5) [00:34:10]',
                          'url': 'https://www.youtube.com/watch?v=S31vo0Umk5M&t=2050s',
                          'relevance': 'Primary practitioner testimony on grey-area working capital items, '
                                       'seasonality gaming, and day-one funding needs.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'UfQ-Ho_j61s',
                       'title': 'Qualifying EBITDA Add-Backs - Separating Fact From Fiction | Masterclass',
                       'channel': 'growthink',
                       'author': 'growthink',
                       'text': 'Normally we need to expect there will be some kind of haircut at the end '
                               'of that process the buyer will try to apply to the deal for add-backs or '
                               'adjustments or EBITDA, which obviously impacts your valuation and '
                               'potential deal.',
                       'tip': 'Normally we need to expect there will be some kind of haircut at the end of '
                              'that process the buyer will try to apply to the deal for add-backs or '
                              'adjustments or EBITDA, which obviously impacts your valuation and potential '
                              'deal.',
                       'timestamp': 1114,
                       'timestamp_seconds': 1114,
                       'timestamp_label': '[00:18:34]',
                       'url': 'https://www.youtube.com/watch?v=UfQ-Ho_j61s&t=1114s',
                       'markdown': '[00:18:34](https://www.youtube.com/watch?v=UfQ-Ho_j61s&t=1114s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BHyx6-mgFe8',
                       'title': 'Add Backs for Adjusted EBITDA',
                       'channel': 'Kirk Michie',
                       'author': 'Kirk Michie',
                       'text': 'You own your own building and you charge yourself below market rent or you '
                               'charge yourself above market rent so that your earnings are lower and your '
                               'taxes are lower.',
                       'tip': 'You own your own building and you charge yourself below market rent or you '
                              'charge yourself above market rent so that your earnings are lower and your '
                              'taxes are lower.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=BHyx6-mgFe8&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=BHyx6-mgFe8&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C-seCQXqtM4',
                       'title': 'Working Capital Adjustment Process',
                       'channel': 'A Simple Model',
                       'author': 'A Simple Model',
                       'text': 'The buyer will have somewhere between 60 and 120 days after the closing '
                               "date to deliver a closing statement which details the buyer's calculation "
                               'of working capital.',
                       'tip': 'The buyer will have somewhere between 60 and 120 days after the closing '
                              "date to deliver a closing statement which details the buyer's calculation "
                              'of working capital.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=C-seCQXqtM4&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=C-seCQXqtM4&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0V-By_uyuhM',
                       'title': 'Working Capital Adjustment: Common Issues in M&A Transactions',
                       'channel': 'Morse',
                       'author': 'Morse',
                       'text': 'In all likelihood there are disputes post closing where a buyer alleges '
                               'that an inadequate amount of working capital was in fact delivered at '
                               'closing.',
                       'tip': 'In all likelihood there are disputes post closing where a buyer alleges '
                              'that an inadequate amount of working capital was in fact delivered at '
                              'closing.',
                       'timestamp': 98,
                       'timestamp_seconds': 98,
                       'timestamp_label': '[00:01:38]',
                       'url': 'https://www.youtube.com/watch?v=0V-By_uyuhM&t=98s',
                       'markdown': '[00:01:38](https://www.youtube.com/watch?v=0V-By_uyuhM&t=98s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'almKwAlo5T4',
                       'title': 'Most Common Working Capital Adjustments',
                       'channel': 'MCM Capital',
                       'author': 'MCM Capital',
                       'text': "That's really something that's more often than not thought of as debt, not "
                               'working capital.',
                       'tip': "That's really something that's more often than not thought of as debt, not "
                              'working capital.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=almKwAlo5T4&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=almKwAlo5T4&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QqemANnN2ZM',
                       'title': 'Net Working Capital Peg for Business Owners',
                       'channel': 'Kirk Michie',
                       'author': 'Kirk Michie',
                       'text': 'Remember, that letter of intent is a ceiling. It only gets worse after '
                               'that.',
                       'tip': 'Remember, that letter of intent is a ceiling. It only gets worse after '
                              'that.',
                       'timestamp': 187,
                       'timestamp_seconds': 187,
                       'timestamp_label': '[00:03:07]',
                       'url': 'https://www.youtube.com/watch?v=QqemANnN2ZM&t=187s',
                       'markdown': '[00:03:07](https://www.youtube.com/watch?v=QqemANnN2ZM&t=187s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S31vo0Umk5M',
                       'title': 'Net Working Capital Adjustment - M&A Transactions (#5)',
                       'channel': 'Break Into Finance',
                       'author': 'Break Into Finance',
                       'text': "One party will argue that that is net debt and that's probably going to be "
                               'the buyer because they want to reduce the purchase price.',
                       'tip': "One party will argue that that is net debt and that's probably going to be "
                              'the buyer because they want to reduce the purchase price.',
                       'timestamp': 2050,
                       'timestamp_seconds': 2050,
                       'timestamp_label': '[00:34:10]',
                       'url': 'https://www.youtube.com/watch?v=S31vo0Umk5M&t=2050s',
                       'markdown': '[00:34:10](https://www.youtube.com/watch?v=S31vo0Umk5M&t=2050s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'S31vo0Umk5M',
                       'title': 'Net Working Capital Adjustment - M&A Transactions (#5)',
                       'channel': 'Break Into Finance',
                       'author': 'Break Into Finance',
                       'text': "I know that I'm going to settle in January and get a big uplift on the "
                               'purchase price.',
                       'tip': "I know that I'm going to settle in January and get a big uplift on the "
                              'purchase price.',
                       'timestamp': 1474,
                       'timestamp_seconds': 1474,
                       'timestamp_label': '[00:24:34]',
                       'url': 'https://www.youtube.com/watch?v=S31vo0Umk5M&t=1474s',
                       'markdown': '[00:24:34](https://www.youtube.com/watch?v=S31vo0Umk5M&t=1474s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'siH_wi11PX8',
                       'title': 'Financial Due Diligence Working Capital Analysis: Practical Case Study',
                       'channel': 'CandiMentor',
                       'author': 'CandiMentor',
                       'text': 'Compared with the $12 million target, the seller is delivering $2.4 '
                               'million more than normal, creating a potential purchase price adjustment '
                               "in the seller's favor.",
                       'tip': 'Compared with the $12 million target, the seller is delivering $2.4 million '
                              'more than normal, creating a potential purchase price adjustment in the '
                              "seller's favor.",
                       'timestamp': 292,
                       'timestamp_seconds': 292,
                       'timestamp_label': '[00:04:52]',
                       'url': 'https://www.youtube.com/watch?v=siH_wi11PX8&t=292s',
                       'markdown': '[00:04:52](https://www.youtube.com/watch?v=siH_wi11PX8&t=292s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 't0rj9LcHTgw',
                       'title': 'Working Capital Adjustments in the Indirect Method (Add or Subtract?)',
                       'channel': 'Accounting Rescue with Lisa',
                       'author': 'Accounting Rescue with Lisa',
                       'text': 'A student subtracts the $3,000 because more debt means less cash, right? '
                               'But, that is not correct.',
                       'tip': 'A student subtracts the $3,000 because more debt means less cash, right? '
                              'But, that is not correct.',
                       'timestamp': 316,
                       'timestamp_seconds': 316,
                       'timestamp_label': '[00:05:16]',
                       'url': 'https://www.youtube.com/watch?v=t0rj9LcHTgw&t=316s',
                       'markdown': '[00:05:16](https://www.youtube.com/watch?v=t0rj9LcHTgw&t=316s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OiLlMiZv9ZQ',
                       'title': 'What are Common EBITDA Add Backs When Calculating SDE',
                       'channel': 'ProjectionHub',
                       'author': 'ProjectionHub',
                       'text': 'You as the buyer might need to hire someone in their position to do the '
                               'job that the current owner is doing; maybe you need to pay them $75,000 to '
                               'be able to do that job.',
                       'tip': 'You as the buyer might need to hire someone in their position to do the job '
                              'that the current owner is doing; maybe you need to pay them $75,000 to be '
                              'able to do that job.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=OiLlMiZv9ZQ&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=OiLlMiZv9ZQ&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ha9dRzcYak4',
                       'title': 'EBITDA Is an Opinion. Cash Flow Is a Fact. (M&A Practitioner Walkthrough)',
                       'channel': 'John Colley | The Investment Banking Practitioner',
                       'author': 'John Colley | The Investment Banking Practitioner',
                       'text': 'EBITDA is an opinion. Cash flow is a fact.',
                       'tip': 'EBITDA is an opinion. Cash flow is a fact.',
                       'timestamp': 1,
                       'timestamp_seconds': 1,
                       'timestamp_label': '[00:00:01]',
                       'url': 'https://www.youtube.com/watch?v=ha9dRzcYak4&t=1s',
                       'markdown': '[00:00:01](https://www.youtube.com/watch?v=ha9dRzcYak4&t=1s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YAk3dxgnsBU',
                       'title': 'Investment Banking - How To Calculate Net Working Capital for an M&A '
                                'Transaction - Transact Capital',
                       'channel': 'Transact Capital',
                       'author': 'Transact Capital',
                       'text': "We've seen deals die over net working capital; if sellers are not familiar "
                               'with how it works, closing can become contentious and deal threatening.',
                       'tip': "We've seen deals die over net working capital; if sellers are not familiar "
                              'with how it works, closing can become contentious and deal threatening.',
                       'timestamp': 763,
                       'timestamp_seconds': 763,
                       'timestamp_label': '[00:12:43]',
                       'url': 'https://www.youtube.com/watch?v=YAk3dxgnsBU&t=763s',
                       'markdown': '[00:12:43](https://www.youtube.com/watch?v=YAk3dxgnsBU&t=763s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'j5A0VGOV88E',
                       'title': 'Quality of Earnings Adjustments',
                       'channel': 'Edspira',
                       'author': 'Edspira',
                       'text': "If the company's a small firm it's possible they use cash basis "
                               "accounting, in which case the seller's EBITDA could be adjusted so it's "
                               'consistent with accrual accounting.',
                       'tip': "If the company's a small firm it's possible they use cash basis accounting, "
                              "in which case the seller's EBITDA could be adjusted so it's consistent with "
                              'accrual accounting.',
                       'timestamp': 65,
                       'timestamp_seconds': 65,
                       'timestamp_label': '[00:01:05]',
                       'url': 'https://www.youtube.com/watch?v=j5A0VGOV88E&t=65s',
                       'markdown': '[00:01:05](https://www.youtube.com/watch?v=j5A0VGOV88E&t=65s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XDVFloSBuko',
                       'title': 'QoE 101 Video 2: EBITDA & Adjustments   1st Place To Look',
                       'channel': 'Elliott Holland',
                       'author': 'Elliott Holland',
                       'text': 'You want to look at total adjustments as a percentage of the adjusted '
                               "EBITDA, and you're likely going to want to look at that in the trailing 12 "
                               'month period.',
                       'tip': 'You want to look at total adjustments as a percentage of the adjusted '
                              "EBITDA, and you're likely going to want to look at that in the trailing 12 "
                              'month period.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=XDVFloSBuko&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=XDVFloSBuko&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hIU9zSg4cQg',
                       'title': 'PE - 1 - Video 5 - How to Analyze Adjusted EBITDA Add-Backs in M&A Deals '
                                '(3-Question Test)',
                       'channel': 'The Finance Lab',
                       'author': 'The Finance Lab',
                       'text': 'Add backs that exceed 15 to 20% of reported EBITDA are a structural '
                               'warning signal.',
                       'tip': 'Add backs that exceed 15 to 20% of reported EBITDA are a structural warning '
                              'signal.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=hIU9zSg4cQg&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=hIU9zSg4cQg&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DbHq5BHo_XA',
                       'title': 'The Definition of Working Capital in the Working Capital Peg',
                       'channel': 'A Simple Model',
                       'author': 'A Simple Model',
                       'text': 'A buyer may want to omit all accounts receivable balances aged 90 days or '
                               'more to avoid the risk that those customers do not end up paying.',
                       'tip': 'A buyer may want to omit all accounts receivable balances aged 90 days or '
                              'more to avoid the risk that those customers do not end up paying.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=DbHq5BHo_XA&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=DbHq5BHo_XA&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
