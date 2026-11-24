from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'dscr-loans-commercial-real-estate-underwriting-metrics',
 'question_prompt': 'How do lenders use DSCR and related metrics to size investor real estate loans, and '
                    'how do investors use DSCR loans?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'DSCR Loans and Commercial Real Estate Underwriting Metrics',
 'subtitle': 'Calculating DSCR Correctly, Typical 1.25x Minimums, LTV, Debt Yield and the Loan Constant, '
             'DSCR Loans for Rentals and 5+ Unit or Commercial Property, Interest-Only Options, and BRRRR '
             'with Hard Money and DSCR Refinances',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Brokers and lenders across the field agree that DSCR is the gatekeeper metric: '
                      'divide what the property earns by what the debt costs, and if the answer clears the '
                      "lender's bar, personal income, W-2s and tax returns stop mattering. Small-balance "
                      'DSCR lenders like Ryan Marks, Andrew Russell and Brandon Turner qualify on gross '
                      'market rent against full PITI, with a 1.0 floor at SEI Mortgage and a 1.2 target at '
                      "Turner's shop, while commercial underwriters such as Trevor Calton, Tactica RES and "
                      'Chalkboard Real Estate size loans off NOI at 1.2 to 1.25x. Once a deal crosses five '
                      'units, Marks reports 680 credit, 25% down and six months reserves. The sharpest '
                      'split is debt yield: Academy For Commercial Lending argues it, not DSCR, separated '
                      'CMBS loans that refinanced cleanly (13.3% to 14.4%) from sub-10% failures.',
 'key_metrics': [{'label': 'Five-Plus Unit DSCR Entry Box',
                  'metric': 'Five-Plus Unit DSCR Entry Box',
                  'value': '680 credit score, 25% minimum down, 6 months PITI reserves, 1.0 DSCR',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ryan Marks lists the qualifying checklist once a building crosses from four '
                             'units into technically commercial five-plus territory, versus a 600 credit '
                             'floor and often zero reserves on one-to-four.',
                  'source': 'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:02:05])'},
                 {'label': 'Rent Gap Between Approval and Rejection',
                  'metric': 'Rent Gap Between Approval and Rejection',
                  'value': '$11 per unit ($1,211 vs $1,200 a side; 1.19 vs 1.2 DSCR)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Brandon Turner's duplex example at $2,400 total rent against a $2,017 "
                             'payment on a $240,000 loan at 6.5% falls one hundredth short of a 1.2 '
                             'target.',
                  'source': 'Brandon Turner | Real Estate Investor ([-W2ThDxeu-o @ 00:09:19])'},
                 {'label': 'Debt Yield at Maturity: Paid vs Unpaid CMBS',
                  'metric': 'Debt Yield at Maturity: Paid vs Unpaid CMBS',
                  'value': '13.3% to 14.4% paid on schedule; sub-10% failed to pay off',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Academy For Commercial Lending reports that across 2024 and 2025 CMBS '
                             'maturities, debt yield rather than DSCR separated loans that refinanced '
                             'cleanly from those that stalled.',
                  'source': 'Academy For Commercial Lending ([NHfs2vBPCys @ 00:03:06])'},
                 {'label': 'Maximum Debt Service From NOI at 1.25x',
                  'metric': 'Maximum Debt Service From NOI at 1.25x',
                  'value': '$100,000 NOI / 1.25 = $80,000 annual ($6,667 monthly) maximum debt service',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Trevor Calton shows how the coverage minimum caps the payment, which then '
                             'caps loan size at $1,112,000 at 6%, $1 million at 7%, and $943,000 on a '
                             '25-year amortization.',
                  'source': 'Real Estate Finance Academy with Trevor Calton ([2cFIwSgUOQM @ 00:01:38])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['The core mechanic every speaker repeats is that the building, not the '
                              'borrower, carries the file. Ryan Marks at SEI Mortgage tells investors they '
                              'still need no job once they move past four units, because the property is '
                              'the income and there is no debt-to-income test whatsoever [OOFsomPO_Mc @ '
                              '00:04:12]. Brandon Turner says it more bluntly: personal income counts for '
                              'zero, tax returns showing big depreciation and cost-segregation losses are '
                              'great at tax time and terrible at bank time, and the DSCR loan removes that '
                              'bottleneck so each new deal makes the next one easier instead of piling '
                              'onto a debt-to-income ratio [-W2ThDxeu-o @ 00:05:36]. Andrew Russell '
                              'watched a Brooklyn client get capped by a conventional lender after a '
                              'fourth property and told to find a co-signer, then pivot to DSCR with one '
                              'month of bank statements and go from four doors to well over ten '
                              '[SExreBEJY5Q @ 00:01:11]. Eli the DSCR Pro frames traditional banks as a '
                              'trap for five-to-twenty-unit and mixed-use buildings, citing tax-return '
                              'demands, committee review and moving targets that change the ratio or the '
                              'down payment at the finish line [6P1p0e_NBxs @ 00:00:17]. The lender '
                              "underwrites the asset; the operator's personal paperwork stays in the "
                              'drawer.',
                              'On the formula itself the field converges, with one split in the inputs. '
                              'Small-balance DSCR desks divide gross rent by full PITI: Devin Peterson of '
                              'ProAlpha Capital runs $2,000 of monthly rent over $1,500 of principal, '
                              'interest, taxes and insurance for a 1.333 ratio and tells investors that '
                              "approval rests on the property's rental income, not their personal DTI "
                              '[L9TrjfKxYdY @ 00:01:34]. Commercial underwriters divide NOI by debt '
                              'service and build in a cushion. Trevor Calton says the ratio usually sits '
                              'right around 1.25, sometimes 1.2 or 1.3, depending on the market, the '
                              'timing and the product type, which works out to roughly 0.25 over the debt '
                              "payment [2cFIwSgUOQM @ 00:00:02]. J Scott, speaking on Mauricio Rauld's "
                              "channel, frames the lender's ask as cash left after expenses of at least "
                              '1.2 times the mortgage, so a $100,000 monthly mortgage needs $120,000 left '
                              'over [52mBD7-QKAw @ 00:01:06]. REtipster lays out the full ladder: 1.0 is '
                              'break-even, most asset-based lenders want 1.2 or higher, and 1.5 or above '
                              'is perceived as really good and may earn better rates [7sx67OQUmsM @ '
                              '00:02:38]. Every one of them treats the threshold as lender-specific, so '
                              "the broker's first job is knowing which desk uses which denominator before "
                              'quoting a client.',
                              'Crossing from four units to five is where the consensus shifts the box. '
                              'Ryan Marks warns that the moment a building adds that fifth unit it is '
                              "technically commercial financing, and SEI's five-plus DSCR program then "
                              'demands roughly a 680 credit score instead of the 600 floor on one-to-four, '
                              'a 25% minimum down payment, six months of PITI in reserves where '
                              'one-to-four often needs none, and higher rates and fees [OOFsomPO_Mc @ '
                              '00:02:05]. Beau Eckstein confirms the product exists, typically for five to '
                              'twenty units, but says it is not as aggressive on loan-to-value as '
                              'one-to-four, and once a deal reaches a couple million dollars Eckstein '
                              'would look at bank, credit union, bridge or Fannie Mae and Freddie Mac '
                              'agency debt before defaulting to DSCR [rzgxx8EB7NI @ 00:00:54]. Eli the '
                              'DSCR Pro defines the same commercial lane as five to twenty residential '
                              'units or mixed-use with stores below and apartments above [6P1p0e_NBxs @ '
                              '00:01:50]. What does not change, per Marks, is the qualifying logic: 100% '
                              'of fair market rent or existing leases, an interest-only option, no job '
                              'requirement and up to 6% seller concessions carry straight over from the '
                              'small-residential product [OOFsomPO_Mc @ 00:03:41]. The practical read for '
                              'a broker is that the debt-coverage engine is identical while the cash '
                              'requirements and pricing step up.'],
               'table': {'caption': 'Where DSCR practitioners agree: qualifying logic, thresholds and the '
                                    'five-unit shift',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Property income fully replaces personal income verification',
                                   'No job needed, no DTI test, the property itself is the qualifying '
                                   'income',
                                   'Self-employed and loss-reporting investors qualify on rent coverage '
                                   'alone',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:04:12])'],
                                  ['Aggressive tax write-offs sink conventional bank approvals',
                                   'Depreciation, cost segregation and bonus depreciation make returns '
                                   'show big losses',
                                   'Route heavy write-off clients straight into DSCR programs before bank '
                                   'review',
                                   'Brandon Turner | Real Estate Investor ([-W2ThDxeu-o @ 00:05:36])'],
                                  ['Commercial lenders size loans with a cushion above 1.0',
                                   'Ratio usually sits around 1.25, sometimes 1.2 or 1.3 by market',
                                   "Quote clients the lender's floor, never the bare break-even ratio",
                                   'Real Estate Finance Academy with Trevor Calton ([2cFIwSgUOQM @ '
                                   '00:00:02])'],
                                  ['Break-even sits at 1.0 and 1.5 reads as strong',
                                   'Below 1.0 operates at a loss; 1.5 or higher may earn better rates',
                                   'Push clients toward 1.5 coverage when chasing pricing improvements on '
                                   'the loan',
                                   'REtipster ([7sx67OQUmsM @ 00:02:38])'],
                                  ['Five units and above is technically commercial financing territory',
                                   'Roughly 680 credit, 25% down, six months reserves, higher rates and '
                                   'fees',
                                   "Reprice the client's total cash needs before writing any five-plus "
                                   'offer',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:02:05])'],
                                  ['Lowering loan-to-value mechanically raises the coverage ratio',
                                   'Dropping from 70% to 65% LTV lifted coverage from 1.11 to 1.20',
                                   "Cut leverage first whenever the ratio comes back short of the lender's "
                                   'minimum',
                                   'Tactica RES ([ZgYmvPS5gJY @ 00:02:48])'],
                                  ['Lender LTV offers are an output of coverage, not tightening',
                                   'Higher rates push offers to 55% to 65%; true cash cows still get 75%',
                                   "Model the coverage at today's rate before promising a client any "
                                   'leverage figure',
                                   'Mauricio Rauld ([52mBD7-QKAw @ 00:02:36])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Lenders size from the ratio backward, and the instructors who teach it show '
                              'the arithmetic. Trevor Calton takes $100,000 of NOI, divides by a 1.25 '
                              'minimum and lands on $80,000 of maximum annual debt service, or $6,667 a '
                              'month; at 6% on a 30-year amortization that caps the loan near $1,112,000, '
                              'at 7% it falls to $1 million, and shortening amortization to 25 years drops '
                              'it again to $943,000 [2cFIwSgUOQM @ 00:04:47]. Chalkboard Real Estate runs '
                              'a four-unit with a two-car garage: $4,200 gross, $2,200 of expenses, $2,000 '
                              'NOI against a $2,319 payment on a $360,000 loan at 6% over 25 years, a 0.86 '
                              'ratio and a $319 monthly deficit; at a 1.2 bank minimum the payment caps at '
                              '$1,666 and the loan near $258,000, solved by trial on the bankrate.com '
                              'calculator [F8RMxGMNHtM @ 00:03:29]. Tactica RES shows the same lever on a '
                              '$7.5 million acquisition: 70% LTV at 7.25% over 30 years produced a '
                              '$429,999 annual payment and a 1.11 ratio, so the LTV came down to 65%, the '
                              'payment to $399,000 and the ratio to 1.20 [ZgYmvPS5gJY @ 00:02:48]. In '
                              'every case the NOI is fixed and the loan amount is the variable that bends.',
                              'On the small-commercial DSCR side the math runs on rent and PITI, and the '
                              "worked deals are specific. Ryan Marks priced a client's $800,000 six-unit, "
                              'partially vacant: 25% down for a $600,000 loan at 7.125% with a one-year '
                              'prepayment penalty, property tax at 1.25% or $833 a month, insurance around '
                              '$200, for a $5,325 PITI the rents must meet; vacant units were credited at '
                              'the middle of three appraisal rent comps, so comps of $1,000, $1,250 and '
                              '$1,500 produce $1,250, and the six-month reserve tally came to about '
                              '$31,950 [OOFsomPO_Mc @ 00:07:05]. Switching that client to interest-only '
                              'cut the payment to a $4,550 IOTI and freed $679 a month while rents '
                              'stabilized [OOFsomPO_Mc @ 00:10:03]. Brandon Turner walks a duplex renting '
                              '$1,200 a side against a $2,017 payment on a $240,000 loan at 6.5%, a 1.19 '
                              'ratio that misses a 1.2 target, then lists three levers: roughly $2,700 '
                              'more down, buying the rate to 6.25% for a 1.21, or pushing rent to $1,211 a '
                              'side, an $11-per-unit gap between approval and rejection [-W2ThDxeu-o @ '
                              "00:09:19]. Andrew Russell's Brooklyn files worked the same way, two units "
                              'at $2,500 covering a $5,000 payment and four at $2,200 covering $8,800 '
                              '[SExreBEJY5Q @ 00:11:53].',
                              'The program terms brokers quote vary by desk, and the numbers are worth '
                              'memorizing. Eli the DSCR Pro offers 30-year fixed paper on '
                              'five-to-twenty-unit and mixed-use buildings at up to 80% LTV on purchases, '
                              'a 1.0 ratio, no-ratio loans when the borrower only takes 60% to 65% LTV, up '
                              'to 6% seller concessions, gift funds and a four-week target close, with a '
                              'five-year step-down prepayment instead of yield maintenance [6P1p0e_NBxs @ '
                              '00:04:29]. Jeff Trevarthen quotes loans up to $2 million, purchases with as '
                              'little as 15% down, 20% to 25% equity on refinances, reserves as low as '
                              'three months, credit down to 640, no cap on the number of financed '
                              'properties, and approvals on non-warrantable condos and short-term rentals '
                              '[O49frBQ6oe0 @ 00:03:52]. Hard Money Mike pairs the product with BRRRR: a '
                              'hard money loan that wraps purchase and rehab with the investor all in at '
                              'about 75%, then a rate-and-term DSCR refinance at 75% to 80% of the new '
                              'appraised value, since cash-out typically costs five to ten points of LTV '
                              "[HYtATwfeE50 @ 00:04:38]. Andrew Russell's repeat Brooklyn buyer typically "
                              'put 25% down to lock best-case pricing, with market rent of every unit '
                              'covering the full payment each time [SExreBEJY5Q @ 00:02:56].'],
               'table': {'caption': 'DSCR street mechanics: sizing math, structure levers and fallback '
                                    'options with exact numbers',
                         'headers': ['Mechanic',
                                     'Exact Numbers Taught',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Back-solving the maximum loan from fixed NOI',
                                   '$100,000 NOI / 1.25 = $80,000 debt service, $6,667 monthly, $1,112,000 '
                                   'loan at 6%',
                                   'Cap the payment first, then let rate and amortization set loan size',
                                   'Real Estate Finance Academy with Trevor Calton ([2cFIwSgUOQM @ '
                                   '00:01:38])'],
                                  ['Five-plus PITI coverage test on a partially vacant building',
                                   '$800,000 six-unit, $600,000 loan at 7.125%, $5,325 PITI the rents must '
                                   'meet',
                                   'Use middle rent comp for vacant units plus 100% of existing leases',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:07:05])'],
                                  ['Interest-only payment while stabilizing below-market rents',
                                   'IO available up to 10 years; $4,550 IOTI freed $679 monthly cash flow',
                                   'Bridge to stabilized rents, then refinance into a competitive 30-year '
                                   'fixed',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:10:03])'],
                                  ['Debt yield hurdle layered on top of the DSCR requirement',
                                   '9.82% debt yield failed a 10.5% requirement; 60% LTV reached 10.64%',
                                   "Cut LTV until both coverage and debt yield clear the lender's bar",
                                   'Tactica RES ([ZgYmvPS5gJY @ 00:05:06])'],
                                  ['Loan constant compared against the project cap rate',
                                   '8.19% constant over 6.38% cap rate dragged cash-on-cash return to '
                                   '3.68%',
                                   'Negotiate purchase price down until leverage turns positive again',
                                   'Tactica RES ([ZgYmvPS5gJY @ 00:06:47])'],
                                  ['Prepayment penalty term traded against rate and points',
                                   'Five-year penalty at 7%; shorter four-to-zero year windows raise rate '
                                   'or closing costs',
                                   "Match penalty length to the client's realistic sale or refinance "
                                   'horizon',
                                   'I Am Andrew Russell ([SExreBEJY5Q @ 00:13:36])'],
                                  ['Fallback when market rent falls short of the payment',
                                   'Extra 5% down or 7.5% rate; no-rent-check loans at 25% to 30% down '
                                   'near 8.5% to 9.25%',
                                   'Keep short-coverage deals alive by trading down payment or rate for '
                                   'approval',
                                   'I Am Andrew Russell ([SExreBEJY5Q @ 00:15:28])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the closers do before the appraisal lands',
                           'body': 'The operators who close DSCR deals cleanly front-load the rent number, '
                                   'the reserve proof, the concession structure and the debt yield check '
                                   'before the file ever reaches underwriting.',
                           'items': ['Pull your own rent comps before going under contract and run the '
                                     'DSCR twice, once at your rent and once at market rent, because the '
                                     "lender uses the appraiser's rent schedule, not your lease or pro "
                                     'forma [Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                     '00:15:28].',
                                     'Reserves do not have to move: 401k, brokerage, business checking, '
                                     'personal checking and savings all count toward the six-month '
                                     'requirement, but tell the lender the asset type up front since not '
                                     'every account is credited at 100% of balance [SEI Mortgage - Ryan '
                                     'Marks — OOFsomPO_Mc @ 00:07:48].',
                                     'Underwrite debt yield alongside DSCR from day one and know the bar '
                                     'moves by asset class: multifamily often 8% to 9%, special purpose '
                                     'and owner-occupied 11% to 13% or more [Academy For Commercial '
                                     'Lending — NHfs2vBPCys @ 00:05:22].',
                                     'Structure up to 6% seller concessions into the offer before going '
                                     'under contract so they can cover closing costs or buy down the rate '
                                     'on both one-to-four and five-plus DSCR loans [SEI Mortgage - Ryan '
                                     'Marks — OOFsomPO_Mc @ 00:05:14].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the rent number the lender will actually use',
                              'action': 'Pull market rent comps and identify existing leases before '
                                        'signing the contract.',
                              'detail': 'Vacant units are credited at the middle of three appraisal rent '
                                        'comps, so $1,000, $1,250 and $1,500 comps produce $1,250, added '
                                        'to 100% of existing leases [SEI Mortgage - Ryan Marks — '
                                        "OOFsomPO_Mc @ 00:05:45]; stress the same deal at the appraiser's "
                                        'likely number because that rent schedule drives the ratio '
                                        '[Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                        '00:14:14].'},
                             {'step': 2,
                              'title': 'Build full PITI and compute the ratio',
                              'action': 'Add principal, interest, taxes and insurance, then divide rent by '
                                        'that total.',
                              'detail': 'Divide monthly rent by PITI the way underwriters do, for example '
                                        '$2,000 over $1,500 for a 1.333 ratio [ProAlpha Capital — '
                                        'L9TrjfKxYdY @ 00:01:19]; include HOA in the payment where it '
                                        'applies [Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                        '00:06:50].'},
                             {'step': 3,
                              'title': 'Back-solve the loan if coverage comes up short',
                              'action': "Divide NOI by the lender's minimum ratio to find the maximum "
                                        'payment, then solve for loan size.',
                              'detail': 'Take $2,000 NOI divided by 1.2 to get a $1,666 maximum payment, '
                                        'then plug 6% and 25 years into a loan calculator until the '
                                        'payment matches, landing near $258,000 [Chalkboard Real Estate — '
                                        "F8RMxGMNHtM @ 00:03:29]; alternatively pull Turner's levers of "
                                        'more down, a rate buydown or an $11 rent bump [Brandon Turner | '
                                        'Real Estate Investor — -W2ThDxeu-o @ 00:08:48].'},
                             {'step': 4,
                              'title': 'Match prepayment and payment structure to the exit',
                              'action': 'Choose the penalty window and interest-only option based on the '
                                        'planned hold.',
                              'detail': 'Take the longer penalty and better pricing for a long-term hold, '
                                        'and pay up for a shorter window if a BRRRR or quick flip is '
                                        'possible [Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                        '00:13:47]; use interest-only for up to 10 years while '
                                        'stabilizing, remembering the loan reamortizes over the remaining '
                                        '20 years in year 11 [SEI Mortgage - Ryan Marks — OOFsomPO_Mc @ '
                                        '00:09:34].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The coverage floor is the first place the desks split. Ryan Marks of SEI '
                              'Mortgage qualifies five-plus-unit buildings on DSCR as long as the property '
                              'is doing a one or greater against PITI, counting 100% of fair market rent '
                              'or 100% of existing leases in place [OOFsomPO_Mc @ 00:03:27]. Jeff '
                              'Trevarthen also screens for 1.0, but says some lenders still allow a 0.80 '
                              'ratio in markets where cash flow keeps improving, and he runs the program '
                              'from one-to-four units up to five-to-eight [O49frBQ6oe0 @ 00:01:25]. '
                              'Brandon Turner raises the bar: the number you are generally shooting for is '
                              '1.2, sometimes 1.25, meaning the property brings in 20% more income than '
                              'goes out on the debt, and his own sample duplex at 1.19 fails by one '
                              'hundredth [-W2ThDxeu-o @ 00:08:18]. Trevor Calton treats 1.25 as the sizing '
                              'default, sometimes 1.2 and sometimes 1.3, depending on industry, market, '
                              'market timing and product type, with lenders adjusting it for competitive '
                              'reasons [2cFIwSgUOQM @ 00:00:02]. The split is structural: rent-over-PITI '
                              'desks clear loans near 1.0, while NOI-over-debt-service desks demand '
                              'roughly a 0.20 to 0.25 cushion before they size anything, so the same '
                              'building can pass one lender and fail the next one down the street.',
                              'Leverage and the no-ratio escape hatch split the commercial DSCR shops wide '
                              'open. Eli the DSCR Pro quotes up to 80% LTV on five-to-20-unit and '
                              'mixed-use purchases, and says that if the borrower is only at 60 or 65% '
                              'LTV, the property typically does not have to cash flow at one at all, '
                              'because the equity protects the lender and a no ratio loan is on the table '
                              '[6P1p0e_NBxs @ 00:04:29]. Ryan Marks says the opposite for five-plus: 25% '
                              'down is the minimum, the deal still has to debt cover, and you cannot do a '
                              'no ratio or just keep increasing your down payment the way the one-to-four '
                              'space allows [OOFsomPO_Mc @ 00:03:27]. Andrew Russell sits between them on '
                              'two-to-four-unit deals: when market rent falls short of the payment, some '
                              'lenders skip the rent check entirely at 25 or 30% down, but the rate climbs '
                              'from roughly 7% to 8.5 or even 9.25 [SExreBEJY5Q @ 00:15:58]. Mauricio '
                              "Rauld, with J Scott, frames today's 55 to 65% LTV outcomes as rate math "
                              'rather than tightening: lenders use the same metrics they always have and '
                              'will still lend 75% on a cash cow that covers 1.2 [52mBD7-QKAw @ 00:02:36].',
                              'Pricing and exit structure draw the sharpest contrasts. Andrew Russell says '
                              'DSCR rates run pretty much in line with two teachers buying a one-family '
                              'home with 30% down, and calls the prepayment penalty a small financial '
                              'penalty where nothing bad happens [SExreBEJY5Q @ 00:03:48]. Brandon Turner '
                              'agrees DSCR prices at or frequently below conventional on an '
                              'apples-to-apples rental comparison, but treats the penalty as real money: '
                              '3% on a $240,000 loan is $7,200, and anything he plans to sell or refi '
                              'inside a year or two goes to hard money instead [-W2ThDxeu-o @ 00:13:00]. '
                              'Hard Money Mike runs that exact sequence, buying with a hard money loan '
                              'that wraps purchase and rehab at 75% all-in, then refinancing into DSCR at '
                              '75 to 80% of appraised value on a rate and term, because a cash-out always '
                              'costs five or ten percent less loan to value [HYtATwfeE50 @ 00:04:23]. Beau '
                              'Eckstein questions running DSCR at all on bigger buildings: once a deal '
                              'reaches the couple-million-dollar range he would look at bank, credit '
                              'union, bridge, or Fannie Mae and Freddie Mac agency debt first, keeping '
                              'DSCR for small multi of 5 to 15 units [rzgxx8EB7NI @ 00:00:54].'],
               'table': {'caption': 'Side-by-side commercial DSCR playbooks where practitioners split on '
                                    'terms and tactics',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Minimum coverage ratio needed to clear the loan',
                                   '1.0 or greater on rent over PITI, with 0.80 allowed by some lenders',
                                   '1.2 to 1.25 on NOI over debt service, moved by market and product type',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:03:27]); Real Estate '
                                   'Finance Academy with Trevor Calton ([2cFIwSgUOQM @ 00:00:02])'],
                                  ['No-ratio loans on five-plus-unit commercial buildings',
                                   'At 60 to 65% LTV the property need not cash flow at one',
                                   'Five-plus must still debt cover; no ratio and extra down are off the '
                                   'table',
                                   'Eli the DSCR Pro ([6P1p0e_NBxs @ 00:04:29]); SEI Mortgage - Ryan Marks '
                                   '([OOFsomPO_Mc @ 00:03:27])'],
                                  ['Purchase leverage and credit on commercial DSCR deals',
                                   'Up to 80% LTV on five-to-20-unit and mixed-use purchases with gift '
                                   'funds allowed',
                                   '25% down minimum and 680 credit for five-plus, versus 600 on '
                                   'one-to-four',
                                   'Eli the DSCR Pro ([6P1p0e_NBxs @ 00:04:10]); SEI Mortgage - Ryan Marks '
                                   '([OOFsomPO_Mc @ 00:02:05])'],
                                  ['Reserves required to close the DSCR loan',
                                   'As little as three months reserves with 15% down on purchases',
                                   'Six months PITI reserves, provable from 401k, brokerage or checking '
                                   'balances',
                                   'Jeff Trevarthen ([O49frBQ6oe0 @ 00:03:52]); SEI Mortgage - Ryan Marks '
                                   '([OOFsomPO_Mc @ 00:08:05])'],
                                  ['How heavily to weigh the prepayment penalty',
                                   'Small penalty where nothing bad happens; shorter windows cost rate or '
                                   'closing costs',
                                   '3% on $240,000 is $7,200, so short holds belong in hard money',
                                   'I Am Andrew Russell ([SExreBEJY5Q @ 00:04:16]); Brandon Turner | Real '
                                   'Estate Investor ([-W2ThDxeu-o @ 00:13:00])'],
                                  ['Which rent number drives the coverage calculation',
                                   'Middle of three appraisal rent comps plus 100% of existing leases in '
                                   'place',
                                   "Appraiser's form 1007 market rent, not your lease or your pro forma",
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:06:00]); Brandon Turner | '
                                   'Real Estate Investor ([-W2ThDxeu-o @ 00:14:14])'],
                                  ['Whether DSCR and LTV alone are enough to screen a deal',
                                   'LTV and DSCR are the primary metrics lenders use in most cases',
                                   'Underwrite debt yield alongside DSCR; 8-9% multifamily, 11-13% special '
                                   'purpose',
                                   'Beyond Lenders ([tlI9IYK5Dxg @ 00:00:20]); Academy For Commercial '
                                   'Lending ([NHfs2vBPCys @ 00:05:22])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Brandon Turner's most expensive trap is the thin margin. His duplex at "
                              '$2,400 of rent against a $2,017 payment lands at 1.19 and gets rejected; '
                              'the fixes are about $2,700 more down, a buy-down from 6.5 to 6.25, or '
                              '$1,211 a side instead of $1,200, an $11 difference per unit between '
                              'approval and rejection [-W2ThDxeu-o @ 00:09:19]. The same deal can die on '
                              "day 18 when the appraiser's rent schedule comes back at $1,100, dropping "
                              'coverage to 1.09 with earnest money exposed if there is no financing '
                              'contingency; long-term tenants paying above market and renovated units '
                              'compared against unrenovated comps get hit hardest [-W2ThDxeu-o @ '
                              '00:14:45]. Ryan Marks shows how the lender builds that number on a '
                              'six-unit: three appraisal rent comps at $1,000, $1,250 and $1,500, with the '
                              'middle $1,250 used for vacant units plus 100% of the existing leases '
                              '[OOFsomPO_Mc @ 00:06:00]. Chalkboard Real Estate shows the deeper version '
                              'of the miss: a four-plex with $2,000 of monthly NOI against $2,319 of '
                              'principal and interest runs 0.86, a $319 monthly deficit, and at a 1.2 '
                              'minimum the most the bank lends is about $258,000 instead of the $360,000 '
                              'requested [F8RMxGMNHtM @ 00:03:10].',
                              'Rate resets quietly shrink loans that looked fine on paper. Trevor Calton '
                              'caps monthly debt service at $6,667 on $100,000 of NOI at a 1.25 minimum; '
                              'at 6% over 30 years that supports $1,112,000, at 7% it drops to $1 million, '
                              'and at 7% over 25 years it falls to $943,000 [2cFIwSgUOQM @ 00:04:47]. '
                              'Mauricio Rauld describes the same squeeze: a $100,000 monthly mortgage at '
                              '4% becomes $150,000 at seven or eight percent, so the $120,000 left over no '
                              'longer clears 1.2 and the lender cuts proceeds [52mBD7-QKAw @ 00:02:00]. '
                              'Academy For Commercial Lending calls this the trap of the 2016 vintage: a '
                              '3.75% coupon cleared a comfortable 1.35x DSCR while carrying a debt yield '
                              'well under 10%, and Trepp data shows loans that paid off on schedule '
                              'carried 13.3% to 14.4% debt yields while the ones that stalled sat below '
                              '10% [NHfs2vBPCys @ 00:05:00]. Tactica RES ran it live on a $7.5 million '
                              'purchase: 70% LTV at 7.25% produced only 1.11, backing off to 65% hit 1.20, '
                              'but debt yield sat at 9.82% against a 10.5% requirement until LTV dropped '
                              'to 60% for 10.64% [ZgYmvPS5gJY @ 00:05:06].',
                              "Structure traps finish the list. Ryan Marks' six-unit client took the "
                              'interest-only option to free $679 a month while stabilizing rents, but if '
                              'no principal is paid through the 10-year IO window, year 11 effectively '
                              'turns the loan into a 20-year payoff, so the refinance exit has to be '
                              'planned up front [OOFsomPO_Mc @ 00:09:34]. Brandon Turner warns the penalty '
                              'applies to any payoff, not just a sale: buy at 7.5%, rates drop, refinance '
                              '14 months later and the penalty eats most of what you made; he also treats '
                              '1.2 coverage as buffer, never profit, when vacancy, repairs, capex and '
                              'management can take 35 to 40% of rent on an older building [-W2ThDxeu-o @ '
                              '00:13:16]. Tactica RES flags negative leverage: an 8.19% loan constant '
                              'above a 6.38% cap rate dragged cash-on-cash to 3.68%, and only cutting the '
                              'price $2 million to $5.5 million pushed the cap rate to 8.71% and made '
                              'leverage positive [ZgYmvPS5gJY @ 00:07:43]. Eli the DSCR Pro reports '
                              'traditional banks killing five-to-20-unit deals with moving targets on '
                              'ratio and down payment late in the process, then locking borrowers in with '
                              'yield maintenance or defeasance that can run tens of thousands of dollars '
                              '[6P1p0e_NBxs @ 00:05:04].'],
               'table': {'caption': 'Firsthand DSCR failure modes with the numbers practitioners actually '
                                    'hit',
                         'headers': ['Trap', 'Firsthand Numbers', 'Operator Fix', 'Expert Source'],
                         'rows': [['Coverage misses the lender minimum by one hundredth',
                                   '$2,400 rent over a $2,017 payment equals 1.19 against a 1.2 bar',
                                   'Add about $2,700 down, buy the rate to 6.25, or get $1,211 a side',
                                   'Brandon Turner | Real Estate Investor ([-W2ThDxeu-o @ 00:09:19])'],
                                  ['Appraisal rent schedule cuts the deal on day 18',
                                   'Appraiser writes $1,100 market rent, coverage falls to 1.09, earnest '
                                   'money exposed',
                                   'Pull rent comps before contract and run DSCR at both rents',
                                   'Brandon Turner | Real Estate Investor ([-W2ThDxeu-o @ 00:14:45])'],
                                  ['Rate increase shrinks the maximum loan amount',
                                   'A $6,667 payment cap supports $1,112,000 at 6% but $1 million at 7%',
                                   'Model the loan at higher rates and shorter amortization before '
                                   'committing',
                                   'Real Estate Finance Academy with Trevor Calton ([2cFIwSgUOQM @ '
                                   '00:04:47])'],
                                  ['Healthy DSCR hiding a weak debt yield at refinance',
                                   'A 3.75% coupon cleared 1.35x DSCR with debt yield under 10%',
                                   'Run debt yield from the start; clean payoffs carried 13.3-14.4% debt '
                                   'yields',
                                   'Academy For Commercial Lending ([NHfs2vBPCys @ 00:04:37])'],
                                  ['Negative leverage dragging returns on a financed purchase',
                                   '8.19% loan constant over a 6.38% cap rate cut cash-on-cash to 3.68%',
                                   'Pay less; a $5.5 million price lifted the cap rate to 8.71%',
                                   'Tactica RES ([ZgYmvPS5gJY @ 00:07:09])'],
                                  ['Interest-only period compressing the remaining amortization term',
                                   'Ten years with no principal turns year 11 into an effective 20-year '
                                   'payoff',
                                   'Plan the refinance exit up front; IO freed $679 of monthly cash flow',
                                   'SEI Mortgage - Ryan Marks ([OOFsomPO_Mc @ 00:09:34])'],
                                  ['Conventional pre-approval wall after the fourth rental property',
                                   'Brooklyn investor was denied, limited, and asked to find a co-signer',
                                   'Pivot to DSCR on market rent with one month of bank statements',
                                   'I Am Andrew Russell ([SExreBEJY5Q @ 00:01:11])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before a DSCR file goes under contract',
                           'body': 'Every one of these checks comes from a deal a practitioner watched '
                                   'fail, shrink, or get repriced. Clear all four before earnest money '
                                   'goes out.',
                           'items': ['Run DSCR twice, once at your rent and once at market rent; if it '
                                     'only works at your higher number you have a hope of a deal, not a '
                                     'deal [Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                     '00:15:28].',
                                     'Underwrite the deal, not just the loan: set aside about 3% vacancy, '
                                     '5-10% repairs, 5-10% capex and 10% management, because a 1.2 '
                                     'approval leaves only 20% of buffer [Brandon Turner | Real Estate '
                                     'Investor — -W2ThDxeu-o @ 00:11:42].',
                                     'Check debt yield against the lender requirement next to DSCR; a deal '
                                     'that cleared 1.20 at 65% LTV still needed 60% LTV to reach 10.64% '
                                     'against a 10.5% bar [Tactica RES — ZgYmvPS5gJY @ 00:05:06].',
                                     'Back into the maximum loan before offering: $2,000 NOI divided by a '
                                     '1.2 minimum caps principal and interest at $1,666, which supports '
                                     'only about $258,000 [Chalkboard Real Estate — F8RMxGMNHtM @ '
                                     '00:03:29].']}}],
 'pull_quote': '"The lender is underwriting the loan. You still have to underwrite the deal." — Brandon '
               'Turner | Real Estate Investor (-W2ThDxeu-o @ 00:12:15).',
 'diagram_id': 'diag-06',
 'action_checklist': ['Pull your own rent comps before going under contract and run DSCR at both your rent '
                      "and market rent, because the lender uses the appraiser's number [Brandon Turner | "
                      'Real Estate Investor — -W2ThDxeu-o @ 00:15:28].',
                      'Size the maximum loan by dividing NOI by the lender minimum DSCR, then plug the '
                      'capped payment into a loan calculator like bankrate.com until the payment matches '
                      '[Chalkboard Real Estate — F8RMxGMNHtM @ 00:03:47].',
                      'Ask the loan officer whether there is a prepayment penalty and what the rate '
                      'pricing or closing cost is for less than five years [I Am Andrew Russell — '
                      'SExreBEJY5Q @ 00:14:44].',
                      'Document six months of PITI reserves for five-plus units from liquid accounts such '
                      'as 401k, brokerage or checking, and tell the lender the asset types up front [SEI '
                      'Mortgage - Ryan Marks — OOFsomPO_Mc @ 00:08:18].',
                      'Structure up to 6% seller concessions before going under contract so they can cover '
                      'closing costs or buy down the rate [SEI Mortgage - Ryan Marks — OOFsomPO_Mc @ '
                      '00:05:14].',
                      'Calculate debt yield and the loan constant against the cap rate, and pay less for '
                      'the asset when the loan constant exceeds the cap rate [Tactica RES — ZgYmvPS5gJY @ '
                      '00:07:43].'],
 'statutory_citations': [{'title': 'Brandon Turner | Real Estate Investor — DSCR Loans Explained for 2026: '
                                   'Mortgages for Rental Investors [00:14:14]',
                          'url': 'https://www.youtube.com/watch?v=-W2ThDxeu-o&t=854s',
                          'relevance': 'Primary practitioner testimony on appraiser rent schedules '
                                       'overriding borrower leases in the DSCR calculation.'},
                         {'title': 'Academy For Commercial Lending — Debt Yield vs. DSCR: The Metric Every '
                                   'Commercial Mortgage Broker Needs to Understand [00:03:28]',
                          'url': 'https://www.youtube.com/watch?v=NHfs2vBPCys&t=208s',
                          'relevance': 'Primary practitioner testimony on debt yield, not DSCR, separating '
                                       'loans that refinanced cleanly from those that stalled.'},
                         {'title': 'SEI Mortgage - Ryan Marks — 6 Unit DSCR Loans for Commercial Property: '
                                   'THIS Catches Investors Off Guard [00:03:27]',
                          'url': 'https://www.youtube.com/watch?v=OOFsomPO_Mc&t=207s',
                          'relevance': 'Primary practitioner testimony on five-plus-unit DSCR '
                                       'qualification and the loss of no-ratio flexibility.'},
                         {'title': 'Tactica RES — The Relationship Between LTV, DSCR, Debt Yield & the '
                                   'Loan Constant [00:04:45]',
                          'url': 'https://www.youtube.com/watch?v=ZgYmvPS5gJY&t=285s',
                          'relevance': 'Primary practitioner testimony on adjusting LTV to satisfy both '
                                       'DSCR and debt yield requirements.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'OOFsomPO_Mc',
                       'title': '6 Unit DSCR Loans for Commercial Property: THIS Catches Investors Off '
                                'Guard',
                       'channel': 'SEI Mortgage - Ryan Marks',
                       'author': 'SEI Mortgage - Ryan Marks',
                       'text': 'This type of loan product does require a higher credit score on average of '
                               'a 680 or above to utilize this financing where the DSCR one to four, we go '
                               'as low as a 600 credit score.',
                       'tip': 'This type of loan product does require a higher credit score on average of '
                              'a 680 or above to utilize this financing where the DSCR one to four, we go '
                              'as low as a 600 credit score.',
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=OOFsomPO_Mc&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=OOFsomPO_Mc&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6P1p0e_NBxs',
                       'title': 'DSCR Loan For Commercial Property',
                       'channel': 'Eli the DSCR Pro',
                       'author': 'Eli the DSCR Pro',
                       'text': "If you have a lot of equity, let's say you are only borrowing 60 or 65% "
                               'LTV, we typically do not require the property to cash flow at one.',
                       'tip': "If you have a lot of equity, let's say you are only borrowing 60 or 65% "
                              'LTV, we typically do not require the property to cash flow at one.',
                       'timestamp': 269,
                       'timestamp_seconds': 269,
                       'timestamp_label': '[00:04:29]',
                       'url': 'https://www.youtube.com/watch?v=6P1p0e_NBxs&t=269s',
                       'markdown': '[00:04:29](https://www.youtube.com/watch?v=6P1p0e_NBxs&t=269s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rzgxx8EB7NI',
                       'title': 'What is a good DSCR for commercial real estate?',
                       'channel': 'Beau Eckstein, Business Ownership Coach',
                       'author': 'Beau Eckstein, Business Ownership Coach',
                       'text': 'Can you go Fannie Mae or Freddie Mac for agency debt, so DSCR for small '
                               'multi 5 to 15 units may play a factor.',
                       'tip': 'Can you go Fannie Mae or Freddie Mac for agency debt, so DSCR for small '
                              'multi 5 to 15 units may play a factor.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=rzgxx8EB7NI&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=rzgxx8EB7NI&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NHfs2vBPCys',
                       'title': 'Debt Yield vs. DSCR: The Metric Every Commercial Mortgage Broker Needs to '
                                'Understand',
                       'channel': 'Academy For Commercial Lending',
                       'author': 'Academy For Commercial Lending',
                       'text': "Loans that didn't were sitting at sub-10% debt yields. DSCR wasn't the "
                               'variable separating those two groups. Debt yield was.',
                       'tip': "Loans that didn't were sitting at sub-10% debt yields. DSCR wasn't the "
                              'variable separating those two groups. Debt yield was.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=NHfs2vBPCys&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=NHfs2vBPCys&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SExreBEJY5Q',
                       'title': 'This is Why 99% of Investors Don’t Use DSCR Loans!',
                       'channel': 'I Am Andrew Russell',
                       'author': 'I Am Andrew Russell',
                       'text': 'There are actually some lenders who you can get away with putting 25 or '
                               '30% down and have no market rent checked.',
                       'tip': 'There are actually some lenders who you can get away with putting 25 or 30% '
                              'down and have no market rent checked.',
                       'timestamp': 958,
                       'timestamp_seconds': 958,
                       'timestamp_label': '[00:15:58]',
                       'url': 'https://www.youtube.com/watch?v=SExreBEJY5Q&t=958s',
                       'markdown': '[00:15:58](https://www.youtube.com/watch?v=SExreBEJY5Q&t=958s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'O49frBQ6oe0',
                       'title': 'DSCR Loans Explained for 2023 -- Mortgages for Investors.',
                       'channel': 'Jeff Trevarthen',
                       'author': 'Jeff Trevarthen',
                       'text': 'In some instances a 0.80 DSCR ratio, so debt service coverage ratio 0.8, '
                               'is still allowable for some investors to be able to help you get a loan on '
                               'a property.',
                       'tip': 'In some instances a 0.80 DSCR ratio, so debt service coverage ratio 0.8, is '
                              'still allowable for some investors to be able to help you get a loan on a '
                              'property.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=O49frBQ6oe0&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=O49frBQ6oe0&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HYtATwfeE50',
                       'title': 'BRRRR: How to Succeed Using DSCR and Hard Money Loans',
                       'channel': 'Hard Money Mike',
                       'author': 'Hard Money Mike',
                       'text': "Cash out refinance always always cost you a little bit more because it's "
                               'going to be five or ten percent less than the loan to value.',
                       'tip': "Cash out refinance always always cost you a little bit more because it's "
                              'going to be five or ten percent less than the loan to value.',
                       'timestamp': 263,
                       'timestamp_seconds': 263,
                       'timestamp_label': '[00:04:23]',
                       'url': 'https://www.youtube.com/watch?v=HYtATwfeE50&t=263s',
                       'markdown': '[00:04:23](https://www.youtube.com/watch?v=HYtATwfeE50&t=263s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2cFIwSgUOQM',
                       'title': 'DSCR Demystified: How Lenders Really Use It to Size Your Loan | Debt '
                                'Service Coverage Ratio',
                       'channel': 'Real Estate Finance Academy with Trevor Calton',
                       'author': 'Real Estate Finance Academy with Trevor Calton',
                       'text': 'If interest rates rise, then the loan amount would have to go down, in '
                               'order for us to stay within the minimum required debt service coverage '
                               'ratio.',
                       'tip': 'If interest rates rise, then the loan amount would have to go down, in '
                              'order for us to stay within the minimum required debt service coverage '
                              'ratio.',
                       'timestamp': 158,
                       'timestamp_seconds': 158,
                       'timestamp_label': '[00:02:38]',
                       'url': 'https://www.youtube.com/watch?v=2cFIwSgUOQM&t=158s',
                       'markdown': '[00:02:38](https://www.youtube.com/watch?v=2cFIwSgUOQM&t=158s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-W2ThDxeu-o',
                       'title': 'DSCR Loans Explained for 2026: Mortgages for Rental Investors',
                       'channel': 'Brandon Turner | Real Estate Investor',
                       'author': 'Brandon Turner | Real Estate Investor',
                       'text': "Your lender does not use your rent estimate. They use the appraiser's rent "
                               'estimate.',
                       'tip': "Your lender does not use your rent estimate. They use the appraiser's rent "
                              'estimate.',
                       'timestamp': 840,
                       'timestamp_seconds': 840,
                       'timestamp_label': '[00:14:00]',
                       'url': 'https://www.youtube.com/watch?v=-W2ThDxeu-o&t=840s',
                       'markdown': '[00:14:00](https://www.youtube.com/watch?v=-W2ThDxeu-o&t=840s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L9TrjfKxYdY',
                       'title': 'DSCR Loans Explained in 2 Minutes',
                       'channel': 'ProAlpha Capital',
                       'author': 'ProAlpha Capital',
                       'text': 'The only thing that the underwriters are going to calculate on a file that '
                               'is a DSCR loan is the rent divided by the debt service.',
                       'tip': 'The only thing that the underwriters are going to calculate on a file that '
                              'is a DSCR loan is the rent divided by the debt service.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=L9TrjfKxYdY&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=L9TrjfKxYdY&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '52mBD7-QKAw',
                       'title': 'Debt Service Coverage Ratio (DSCR) | Lender Preferred Metric (w J Scott)',
                       'channel': 'Mauricio Rauld',
                       'author': 'Mauricio Rauld',
                       'text': "The reality is the lenders aren't tightening up; the lenders use the same "
                               "computations, the same metrics as they've always used.",
                       'tip': "The reality is the lenders aren't tightening up; the lenders use the same "
                              "computations, the same metrics as they've always used.",
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=52mBD7-QKAw&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=52mBD7-QKAw&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3AB1K3GHp4w',
                       'title': 'What is Debt Service Coverage Ratio (DSCR) and How to Use It',
                       'channel': 'Succeed REI',
                       'author': 'Succeed REI',
                       'text': 'You really never want your DSCR to be lower than 1.0.',
                       'tip': 'You really never want your DSCR to be lower than 1.0.',
                       'timestamp': 248,
                       'timestamp_seconds': 248,
                       'timestamp_label': '[00:04:08]',
                       'url': 'https://www.youtube.com/watch?v=3AB1K3GHp4w&t=248s',
                       'markdown': '[00:04:08](https://www.youtube.com/watch?v=3AB1K3GHp4w&t=248s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZgYmvPS5gJY',
                       'title': 'The Relationship Between LTV, DSCR, Debt Yield & the Loan Constant',
                       'channel': 'Tactica RES',
                       'author': 'Tactica RES',
                       'text': 'When the loan constant is greater than the cap rate, leverage is negative '
                               'and financing is actually hurting our return on cash invested.',
                       'tip': 'When the loan constant is greater than the cap rate, leverage is negative '
                              'and financing is actually hurting our return on cash invested.',
                       'timestamp': 407,
                       'timestamp_seconds': 407,
                       'timestamp_label': '[00:06:47]',
                       'url': 'https://www.youtube.com/watch?v=ZgYmvPS5gJY&t=407s',
                       'markdown': '[00:06:47](https://www.youtube.com/watch?v=ZgYmvPS5gJY&t=407s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F8RMxGMNHtM',
                       'title': 'How to CORRECTLY Calculate the Debt Service Coverage Ratio (DSCR)',
                       'channel': 'Chalkboard Real Estate',
                       'author': 'Chalkboard Real Estate',
                       'text': "Assuming these numbers are correct, there is zero chance you're getting a "
                               'loan for $360,000 from a bank on this property.',
                       'tip': "Assuming these numbers are correct, there is zero chance you're getting a "
                              'loan for $360,000 from a bank on this property.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=F8RMxGMNHtM&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=F8RMxGMNHtM&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tlI9IYK5Dxg',
                       'title': 'You Must Understand LTV and DSCR',
                       'channel': 'Beyond Lenders',
                       'author': 'Beyond Lenders',
                       'text': "The LTV for your deal will need to be less than the lender's maximum LTV "
                               "and the DSCR for your deal will need to be greater than the lender's "
                               'minimum DSCR.',
                       'tip': "The LTV for your deal will need to be less than the lender's maximum LTV "
                              "and the DSCR for your deal will need to be greater than the lender's "
                              'minimum DSCR.',
                       'timestamp': 226,
                       'timestamp_seconds': 226,
                       'timestamp_label': '[00:03:46]',
                       'url': 'https://www.youtube.com/watch?v=tlI9IYK5Dxg&t=226s',
                       'markdown': '[00:03:46](https://www.youtube.com/watch?v=tlI9IYK5Dxg&t=226s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7sx67OQUmsM',
                       'title': 'Debt Service Coverage Ratio (DSCR) Explained',
                       'channel': 'REtipster',
                       'author': 'REtipster',
                       'text': 'A business or investment opportunity with a DSCR of 1.5 or higher is '
                               'normally perceived as really good and may have a case for obtaining better '
                               'rates on their loan.',
                       'tip': 'A business or investment opportunity with a DSCR of 1.5 or higher is '
                              'normally perceived as really good and may have a case for obtaining better '
                              'rates on their loan.',
                       'timestamp': 158,
                       'timestamp_seconds': 158,
                       'timestamp_label': '[00:02:38]',
                       'url': 'https://www.youtube.com/watch?v=7sx67OQUmsM&t=158s',
                       'markdown': '[00:02:38](https://www.youtube.com/watch?v=7sx67OQUmsM&t=158s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
