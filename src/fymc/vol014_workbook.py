from __future__ import annotations

def build_volume_014_workbook() -> dict:
    return {'workbook_id': 'wb-014-specialty-finance-brokerage',
 'volume_id': 'vol-014-specialty-finance-brokerage',
 'title': 'Specialty Finance Brokerage — Practitioner Testimony Operator Workbook',
 'subtitle': 'Deal Economics, Brokerage Launch Mechanics, Licensing and Lender Positioning, Equipment '
             'Brokerage, Asset-Backed and Contractor Products, and Factoring Worksheets for the Specialty '
             'Finance Broker Who Gets Paid Only When the Deal Funds',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Deal Economics and Brokerage Launch Scorecard',
                 'purpose': 'Turn every incoming file into a priced, qualified, lender-matched opportunity '
                            'before any heavy lifting begins. This worksheet forces the commission math, '
                            'the point-pricing score, the packaging deposit, the lender appetite check, '
                            'and the launch basics onto one page so weak files get cut early and fundable '
                            'files move fast.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete one copy of this worksheet for every new borrower file before '
                                  'you quote points or promise a timeline.',
                                  'Work the fields in order, because lender fit and commission math decide '
                                  'whether the remaining fields are worth your time.',
                                  "Use real figures from the borrower's bank statements, rent roll, P&L, "
                                  'and balance sheet rather than the story told on the first call.',
                                  'Remember that the broker typically gets paid only when the deal '
                                  'actually funds, so every field should move the file toward a funded '
                                  'close.',
                                  'If the file is small, messy, and the borrower keeps talking your fee '
                                  'down, record the walk-away decision and move to the next qualified '
                                  'file.'],
                 'fields': [{'name': 'lender_fit_mandate',
                             'type': 'textarea',
                             'prompt': 'Describe the specific borrower file you are working right now and '
                                       'name the one, two, or three lenders whose credit box genuinely '
                                       'fits it. Explain why each lender fits, and state which lenders you '
                                       'deliberately excluded and the reason for each exclusion.',
                             'example': 'A $2 million stabilized retail refinance fits a regional bank and '
                                        'one debt fund only, so the file goes to the bank first and '
                                        "nowhere else. Most clients are 'a best fit for just one or two or "
                                        "three different lenders' [Commercial Loan Broker Institute — "
                                        '-HZRdtDpSRo @ 00:02:24]. The hard-money shop and the SBA desk '
                                        'were excluded because neither matches stabilized retail.'},
                            {'name': 'commission_math',
                             'type': 'text',
                             'prompt': 'Calculate your expected commission on the current file by '
                                       'multiplying the funded loan amount by the points you plan to '
                                       'quote. Show the arithmetic, list the product type, and compare the '
                                       'result against the typical one to six point range practitioners '
                                       'report.',
                             'example': 'Funded amount of $2,000,000 times 1.5 points equals $30,000 on '
                                        'one deal, against roughly $4,000 on a $400,000 residential loan '
                                        'at about 1% [Commercial Loan Broker Institute — v3GnrXphwvM @ '
                                        '00:04:10]. Product: commercial real estate refinance. Most '
                                        'products pay 1% to 6%, with certain cases reaching 15% '
                                        '[Commercial Loan Broker Institute — 3V8HTzwHS90 @ 00:03:38], so '
                                        '1.5 points sits low but fair.'},
                            {'name': 'stacked_revenue_streams',
                             'type': 'textarea',
                             'prompt': 'List every pay stream available on this client beyond front-end '
                                       'points, including packaging deposits, back-end yield spread, '
                                       'correspondent premiums, factoring residuals, and repeat financing '
                                       'events. Estimate a dollar figure for each stream and note when it '
                                       'would actually be paid.',
                             'example': 'A trucking client takes a factor line paying a residual of 10% to '
                                        '15% of monthly factor fees whenever they pull on it, potentially '
                                        'month after month for 5 years [Commercial Loan Broker Institute — '
                                        '3V8HTzwHS90 @ 00:07:38]. Their second location can pay four times '
                                        'through real estate, equipment, fixtures, and working capital '
                                        '[Commercial Loan Broker Institute — 7OHPVFeEmD4 @ 00:10:37].'},
                            {'name': 'point_pricing_score',
                             'type': 'textarea',
                             'prompt': 'Score the file on deal size, deal type, borrower constraints, '
                                       'complexity, and time pressure before you quote any points. Write '
                                       'the score for each factor, the resulting point quote, and whether '
                                       'the per-deal dollar figure justifies your time on it.',
                             'example': 'Deal size $400,000, bridge purchase, borrower with two late tax '
                                        'filings, needs funding in 21 days: high hair, high urgency, so 3 '
                                        'points, or $12,000. That clears the $5,000 to $10,000 per-deal '
                                        'target and fits the goal of 2 to 5 closed deals a month [John '
                                        'Neufer — uqs40-CCDSc @ 00:10:38]. Small and messy with constant '
                                        'pushback would mean walking away.'},
                            {'name': 'hair_clause_script',
                             'type': 'textarea',
                             'prompt': 'Write the exact words you will use at the start of the engagement '
                                       'to tell the borrower that complexity or messiness discovered later '
                                       'adds points at closing. Include your walk-away line if the '
                                       'borrower refuses to accept that condition.',
                             'example': "'My quote is 2 points on a clean file. If this deal turns complex "
                                        "or messy, more points get added at the end.' Walk-away line: 'If "
                                        "that does not work, I am not the right fit.' Neufer sets this "
                                        'hair clause up front and walks if they refuse [John Neufer — '
                                        'uqs40-CCDSc @ 00:04:38]. No point cuts for promised future '
                                        'business either.'},
                            {'name': 'packaging_deposit_terms',
                             'type': 'text',
                             'prompt': 'Set the packaging deposit you will collect before doing the heavy '
                                       'lifting on this file. State the dollar amount, the refund clause '
                                       'and its time window, and how you will interpret a borrower who '
                                       'refuses to put any money down.',
                             'example': 'Deposit: $250, fully refundable if no LOI is issued within 45 '
                                        'days. Collected before underwriting the rent roll or building the '
                                        'package. A borrower who will not put down $200 with a full refund '
                                        'guarantee is not serious [Commercial Loan Broker Institute — '
                                        '7OHPVFeEmD4 @ 00:06:48], so that refusal moves the file out of '
                                        'the active pipeline and frees the week.'},
                            {'name': 'bank_appetite_call_log',
                             'type': 'textarea',
                             'prompt': 'Log your Monday or Tuesday calls to bank commercial managers '
                                       'asking where the money is going this week. Record each contact, '
                                       'the asset types they are filling or avoiding, and how many '
                                       'commercial manager lunches you booked for the week.',
                             'example': 'Monday: called four commercial managers. One says the multifamily '
                                        'bucket is full this quarter; another wants owner-occupied '
                                        'industrial. Portfolios fill up by asset type, so appetite gets '
                                        'confirmed before submission [CFM (Commercial Financing Mastery) — '
                                        'cqOh0arlXGU @ 00:04:41]. Booked three lunches toward the '
                                        'three-to-five weekly target; Truong reports at least one deal a '
                                        'month from a single TD contact.'},
                            {'name': 'centers_of_influence',
                             'type': 'textarea',
                             'prompt': 'Name the centers of influence you will cultivate for steady deal '
                                       'flow, such as commercial real estate brokers, CPAs, attorneys, and '
                                       'hard-money lenders. For each, write the follow-up cadence and the '
                                       'response window you commit to keeping for every referral.',
                             'example': 'Two CPAs, one real estate attorney, one hard-money lender, and '
                                        'three CRE brokers, each touched every two weeks. Every borrower '
                                        'and referral gets an answer within 24 to 48 hours, because '
                                        "'there's no excuse not to' [Commercial Capital Training Group, "
                                        "LLC — UBxQzlMJT7k @ 00:22:52]. Shafran's reminder stays on the "
                                        'desk: the money is in the followup, not the initial contact.'},
                            {'name': 'underwriting_self_check',
                             'type': 'textarea',
                             'prompt': 'Run LTV, DSCR, and debt yield yourself before any lender sees the '
                                       "file, and confirm the prospect's story matches the bank statements "
                                       "and balance sheet. Record each ratio, the lender's test, and any "
                                       'gap you must solve before packaging.',
                             'example': 'LTV 65%, DSCR 1.28, debt yield 10% against an 11% lender test. '
                                        'Rapp shows that one-point miss opening a gap above $300,000 [Bill '
                                        'Rapp, CCIM - Director - Commloan — TlDScaCI3fE @ 00:06:00], so '
                                        'the loan gets resized or more equity comes in. Bank statements '
                                        'reconcile with the stated revenue, so the story checks out before '
                                        'packaging.'},
                            {'name': 'package_scrub_and_launch',
                             'type': 'textarea',
                             'prompt': 'Scrub the package before submission for credit reports older than '
                                       '60 days, inactive LLCs, missing pages, and asset gaps. Also '
                                       'confirm your launch basics: corporate identity, professional email '
                                       'domain, firm name, and E&O coverage for commercial and unsecured '
                                       'files.',
                             'example': 'Credit report pulled 72 days ago: re-pulled. LLC status: '
                                        'reinstated before submission [AD Mortgage — -j6-Ev4L24c @ '
                                        "00:49:12]. Firm name carries 'advisor' and all financial requests "
                                        'go from a company domain, never Gmail or Yahoo [Commercial '
                                        'Capital Training Group, LLC — nxxklr3VSSo @ 00:29:27]. E&O policy '
                                        'topped up because most policies do not cover unsecured or '
                                        'commercial property financing out of a residential shop.'}],
                 'completion_gate': 'Do not submit the file until one or two well-matched lenders are '
                                    'named, the commission math clears your per-deal target, the hair '
                                    'clause has been stated aloud, a packaging deposit is collected, '
                                    'lender appetite was confirmed this week, and the package scrub shows '
                                    'no stale credit, inactive entities, or missing pages.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Compliance Positioning and Equipment Brokerage Build Sheet',
                 'purpose': 'Protect the brokerage from licensing, securities, and paper-quality traps '
                            'while building the lender trust and vendor channels that drive equipment deal '
                            'flow. This worksheet pairs state-by-state compliance checks with lender '
                            'network growth, the thirty-second deal summary, resale and lien tests, dealer '
                            'outreach, lead economics, and a lender-ready day-one package.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start with the licensing and securities fields, because a compliance '
                                  'failure can erase the fee and create judgment exposure far larger than '
                                  'the deal.',
                                  "Call the borrower's state department directly and write down what you "
                                  'were told, with names and dates, rather than relying on memory.',
                                  'Treat lender trust as your primary asset: build the network first, then '
                                  'present every deal with reconciled numbers a lender can grasp in '
                                  'seconds.',
                                  'For equipment files, test every listed asset for resale value and '
                                  'existing UCC filings before you spend time packaging the request.',
                                  'Never write or say anything that sounds like a promised approval, a '
                                  'specific rate, or a guaranteed funding result to a client or vendor.'],
                 'fields': [{'name': 'state_licensing_check',
                             'type': 'textarea',
                             'prompt': "Identify the borrower's state and confirm by calling the state "
                                       'department whether it licenses or registers commercial financing. '
                                       'Record who you spoke with, the requirement they described, any '
                                       'deadlines, and whether you will broker directly or refer out.',
                             'example': 'Borrower is in Texas, and most people treat borrower location as '
                                        'controlling [Jonathan Mills Patrick — gfK-oOi-TuI @ 00:04:44]. '
                                        'Sales-based financing registration runs through NMLS by December '
                                        '31, 2026, with rules due by September 1, 2026 [Texas Office of '
                                        'Consumer Credit Commissioner — rhDEWGC8KqM @ 00:06:28]. Decision: '
                                        'calendar the registration and confirm which products in the '
                                        'pipeline count as sales-based financing.'},
                            {'name': 'licensed_associate_play',
                             'type': 'textarea',
                             'prompt': 'If the deal sits in a licensing state where you hold no license, '
                                       'name the licensed local associate you will partner with. Describe '
                                       'how the referral will be handed off, the referral fee you expect, '
                                       'and how the client relationship stays intact.',
                             'example': 'A California borrower needs a commercial loan, and the state bill '
                                        'would require a $500 to $1,000 license plus $25,000 net worth by '
                                        'July 2028 [Funder Intel — jCWdtQmKTiU @ 00:00:34]. The deal goes '
                                        'to a licensed local associate for a referral fee instead of '
                                        'brokering it directly, the same associate play Patrick runs '
                                        '[Jonathan Mills Patrick — gfK-oOi-TuI @ 00:05:56].'},
                            {'name': 'securities_line',
                             'type': 'textarea',
                             'prompt': 'Determine whether anything you are being asked to place is '
                                       "actually a security, such as interests in someone else's "
                                       'syndication. Write your decision, your fee position, and the '
                                       'structure you will use if you still want to bring money in.',
                             'example': 'A sponsor offers a fee for raising $1 million into their '
                                        "syndication. That is selling someone else's security, and a "
                                        '$25,000 fee can become a $1 million rescission judgment '
                                        '[Trowbridge Law Group — 8p8VFFvdliQ @ 00:07:22]. Decision: no fee '
                                        'taken. Alternative: form our own syndication and have it invest '
                                        'as a single investor [Trowbridge Law Group — 8p8VFFvdliQ @ '
                                        '00:10:09].'},
                            {'name': 'paper_and_due_diligence',
                             'type': 'textarea',
                             'prompt': 'Review the funding paper and borrower identity documentation for '
                                       'compliance traps. Note any confession of judgment or pre-default '
                                       'power of attorney in California paper, and list each individual '
                                       'owning 25 percent or more of the borrowing entity for the '
                                       'beneficial ownership file.',
                             'example': 'California funder agreement contained a confession of judgment '
                                        'clause, so it was flagged and stripped before the client signed '
                                        '[Funder Intel — jCWdtQmKTiU @ 00:00:50]. Ownership list: two '
                                        'members at 40% each and one at 20%. Only the two 40% members fall '
                                        'under the ownership prong covering each individual with 25 '
                                        'percent or more [Compliance Connection — gnx32nNbVfU @ '
                                        '00:05:01].'},
                            {'name': 'lender_network_build',
                             'type': 'textarea',
                             'prompt': 'Inventory your current lender network and set the growth plan that '
                                       'keeps it fresh. Record how many lenders you have by product, the '
                                       'two new lenders you will add this month, and which screens each '
                                       'new lender uses.',
                             'example': 'Current bench: 14 lenders across CRE, equipment, and factoring. '
                                        'Target growth is 15 to 20 percent new lenders per year, about 2 '
                                        'per month [Commercial Loan Broker Institute — tgEHrpyZE9U @ '
                                        '00:11:45]. This month: one equipment lender and one bridge '
                                        'lender. Network comes first, because most new brokers wrongly '
                                        'think their number one job is finding clients.'},
                            {'name': 'thirty_second_summary',
                             'type': 'textarea',
                             'prompt': 'Write the deal summary a lender should understand in under thirty '
                                       'seconds, with reconciled numbers only. Then write your follow-up '
                                       'plan, including how you will read lender silence and which backup '
                                       'lenders are lined up if no answer comes.',
                             'example': "'$1.2 million purchase of an owner-occupied warehouse, 1.31 DSCR, "
                                        "70% LTV, borrower with 11 years in business.' The lender should "
                                        'get it in under 30 seconds [Commercial Loan Broker Institute — '
                                        '4ELMBLT7mvs @ 00:03:19]. If no reply in a week, that silence '
                                        "'isn't confusion, it's a decision' [Commercial Loan Broker "
                                        'Institute — 4ELMBLT7mvs @ 00:06:17], and the two backups get '
                                        'called.'},
                            {'name': 'equipment_resale_test',
                             'type': 'textarea',
                             'prompt': 'Run the resale and lien test on every asset in the equipment '
                                       'request. List each unit with its age, VIN or serial status, '
                                       'vendor, and whether a UCC filing already exists, then state '
                                       'whether the lender could resell it.',
                             'example': 'Two recent-model dump trucks with VINs from a dealer pass, '
                                        'because the lender can resell every listed asset [ION Capital - '
                                        'Loan Broker University — 2BqGahVBgUs @ 00:02:16]. An older loader '
                                        'already carries a UCC filing from a prior lender, so it is '
                                        'dropped; lenders will not take second position on an asset [ION '
                                        'Capital - Loan Broker University — wt92Utt7o6I @ 00:04:07].'},
                            {'name': 'vendor_outreach_plan',
                             'type': 'textarea',
                             'prompt': 'Map your vendor and dealer outreach for the next month. Name the '
                                       'equipment categories, the opening question you will ask, the '
                                       'channels you will use instead of mass cold calling, and the '
                                       'payment tool you will give each dealer.',
                             'example': "Target: construction equipment dealers. Opener: 'do you use "
                                        "financing to sell more equipment,' run through LinkedIn plus "
                                        'automation instead of 300 cold calls [Credit Suite — L2-ax8GoKVw '
                                        '@ 00:12:09]. Each dealer gets a payment calculator so reps sell '
                                        "'$800/month, 100% tax deductible' rather than sticker price "
                                        '[Credit Suite — L2-ax8GoKVw @ 00:15:20]. One rep can lead to '
                                        'whole teams.'},
                            {'name': 'lead_source_economics',
                             'type': 'textarea',
                             'prompt': 'Compare your lead sources by cost and yield. For dealer referrals, '
                                       'exclusive bought leads, and shared bought leads, record the cost '
                                       'per lead, the expected close rate, the average points, and the '
                                       'follow-up cadence you will run for twelve months.',
                             'example': 'Exclusive leads cost $50 each with a 30-lead minimum, or $1,500 a '
                                        'month [Leads For Locals — Oq4y-D6sylo @ 00:21:25], against a 3-5% '
                                        "close rate. Shared leads at $40-80 are 'a treadmill' [Equipment "
                                        'Finance Academy — dc0_7D431kI @ 00:01:23]. Dealer flow funds 4-5 '
                                        'of 10 weekly applications. Unclosed leads get a call every 60 '
                                        'days for 12 months.'},
                            {'name': 'day_one_package_and_promises',
                             'type': 'textarea',
                             'prompt': 'Assemble the lender-ready equipment package before the first '
                                       'submission and audit your client and vendor language. List each '
                                       'required item and its status, and write down any phrase you used '
                                       'that could sound like a promised approval, rate, or result.',
                             'example': 'Package: legal name, owner info, time in business, equipment '
                                        'description, vendor, exact cost, and signed credit authorization, '
                                        'all complete on day one [Equipment Finance Academy — dc0_7D431kI '
                                        "@ 00:03:50]. Language audit: 'you are basically approved' was "
                                        "replaced with 'I will match you to the right lender,' because a "
                                        'broker should never promise approval, rate, or funding [Equipment '
                                        'Finance Academy — nN3wD1zIjqM @ 00:06:29].'}],
                 'completion_gate': "Do not broker or submit until the borrower's state requirement is "
                                    'confirmed by phone, no security is being sold for a fee, problem '
                                    'clauses are stripped, two new lenders are added this month, every '
                                    'equipment asset passes the resale and lien test, and the day-one '
                                    'package is complete with no promised outcomes in writing.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Asset-Backed, Contractor, and Factoring Deal Structuring Sheet',
                 'purpose': 'Structure equipment, purchase order, surety, and receivables deals so the '
                            'asset or the account debtor carries the credit and the client can actually '
                            'afford the payment. This worksheet stress-tests cash flow, screens credit, '
                            'verifies vendors and invoices, audits the aging report, interrogates factor '
                            'terms, recomputes net proceeds, and maps residual income.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Run the weak-demand cash flow case before anything else, because '
                                  'borrowing capacity is not the same as investment opportunity.',
                                  'For equipment files, verify the vendor and invoice price yourself and '
                                  'take over all vendor communication to speed closing and earn referrals.',
                                  'For receivables files, underwrite the account debtors, separate fast '
                                  'payers from slow payers, and factor only the invoices that need it.',
                                  'Quote factoring cost per invoice batch in dollars, never annualized, '
                                  'and compare it side by side with the bank line using real days to '
                                  'collect.',
                                  'Record every residual and referral commission at placement so the '
                                  'income from each factoring client is tracked for the life of the deal.'],
                 'fields': [{'name': 'cash_flow_stress_test',
                             'type': 'textarea',
                             'prompt': 'Run the weak-demand case on the equipment request. Record the '
                                       'proposed monthly payment, the expected incremental operating cash '
                                       'the machine produces, the downside cash figure, the monthly '
                                       'shortfall, and whether you will restructure the term or walk away '
                                       'from the file.',
                             'example': "Payment $1,500 a month. If weak demand cuts the machine's "
                                        'incremental cash to $900, the business faces a $600 monthly '
                                        'shortfall out of reserves [BizMoney Explained — Q4yDbzFte3g @ '
                                        '00:13:05]. Decision: stretch the term to bring the payment under '
                                        'the downside figure. Borrowing capacity is not the same as '
                                        'investment opportunity, so unnecessary units come off the '
                                        'request.'},
                            {'name': 'credit_profile_screen',
                             'type': 'textarea',
                             'prompt': "Screen the applicant's credit profile against small-ticket "
                                       'equipment standards. Record the personal score, revolving '
                                       'utilization, payment history, collections, comparable past debt as '
                                       'a percentage of the request, and whether the purchase is from a '
                                       'real vendor or an auction house.',
                             'example': 'Startup owner: 724 score, 38% utilization, no collections, prior '
                                        'auto and equipment debt about 65% of the $140,000 request, buying '
                                        "from a real dealer. That fits ROK's startup ceiling of up to "
                                        '$150,000 with 700-plus credit and comparable debt at 60 to 70 '
                                        'percent [ROK Financial — EelcRfosnt8 @ 00:19:21]. An '
                                        'auction-house purchase would have been screened out.'},
                            {'name': 'product_fit_selection',
                             'type': 'textarea',
                             'prompt': 'Choose the right equipment product for this client: '
                                       'application-only lease, full-documentation loan, sale-leaseback, '
                                       'or split across multiple lenders. Explain the deciding factors, '
                                       'including ticket size, credit score, existing free-and-clear '
                                       'equipment, and how much one lender will cover on its own.',
                             'example': 'Client needs $120,000 for a new machine with a 640 score, so an '
                                        'application-only lease fits; Camberato cites about $100,000 to '
                                        '$150,000 at 620 or higher [Joe Camberato — H6xXORaU7Jo @ '
                                        '00:03:29]. Their paid-off excavator could support a '
                                        'sale-leaseback for working capital. A roughly $700,000 truck '
                                        'invoice would be split across three lenders, as ROK does.'},
                            {'name': 'vendor_and_invoice_verification',
                             'type': 'textarea',
                             'prompt': 'Verify the seller and the invoice before submission. Record the '
                                       "vendor's legal name, how you confirmed the business is real, how "
                                       "the invoice price compares to the asset's value, and who on your "
                                       'desk will handle all vendor communication.',
                             'example': "Vendor confirmed through a call to the dealership's main line, "
                                        "and the invoice price matches the asset's value, so 100% "
                                        'financing is possible if credit qualifies [ROK Financial — '
                                        'EelcRfosnt8 @ 00:39:03]. A friend-down-the-street invoice would '
                                        'be caught every time [The Banking Podcast — bvVqx_kVIj8 @ '
                                        '00:08:28]. Our desk handles title adjustments and GPS units '
                                        'directly.'},
                            {'name': 'po_and_surety_costing',
                             'type': 'textarea',
                             'prompt': 'For manufacturers or contractors, cost out purchase order funding '
                                       "or surety bonding before the bid. Record the PO lender's monthly "
                                       'rate and billing increments, the bond premium percentage, and '
                                       'where the premium will be built into the bid or change order.',
                             'example': 'PO money runs 1 to 3 percent per month while outstanding, billed '
                                        'in 5, 15, or 30 day increments [Joe Camberato — PB-h1pXLzhg @ '
                                        "00:03:34]. The contractor's performance bond starts at 3 percent "
                                        'of the bid with no completed-project portfolio yet, and that '
                                        'premium is baked into the bid [Surety Bonds Direct — ttoT3V6duzU '
                                        '@ 00:03:47]. Indemnity exposure explained before signing.'},
                            {'name': 'aging_report_audit',
                             'type': 'textarea',
                             'prompt': "Audit the client's accounts receivable aging report before any "
                                       'invoice is offered to a factor. Separate pristine commercial '
                                       'customers from habitual late payers, note days to pay for each, '
                                       'and decide which customers stay on the bank line.',
                             'example': 'Aging review: six customers pay inside 30 days and two run past '
                                        '45 [Trifecta Business Group — lkbt0MYbQeI @ 00:00:18]. The fast '
                                        'payers stay on the bank line, and only the two slow customers get '
                                        "factored, following Johnson's split [Ian Johnson — Lu16E6BvvDE @ "
                                        "00:06:03]. The factor underwrites those account debtors' credit, "
                                        "not the client's own rating."},
                            {'name': 'factor_term_interrogation',
                             'type': 'textarea',
                             'prompt': 'Interrogate every factoring proposal before the client signs. '
                                       'Record answers on notified versus non-notified, all-or-none versus '
                                       'spot, recourse versus non-recourse, personal guarantee, '
                                       'per-invoice and maintenance fees, contract length, and the exact '
                                       'cost to exit the agreement early. Note any origination or annual '
                                       'fee.',
                             'example': 'Proposal A: notified, spot factoring, recourse, personal '
                                        'guarantee required, no per-invoice fee, 12-month contract with an '
                                        'exit cost to be confirmed in writing [Joe Camberato — qWXtw52gtTw '
                                        '@ 00:03:15]. Origination and annual fees were asked about '
                                        'directly before signing [Joe Camberato — qWXtw52gtTw @ 00:02:48]. '
                                        'Proposal B was dropped because it would not disclose the exit '
                                        'cost.'},
                            {'name': 'net_proceeds_math',
                             'type': 'textarea',
                             'prompt': "Recompute the client's net proceeds on a sample invoice batch. "
                                       'Show face value, the advance rate, the fee on gross receivables, '
                                       'interest on the amount actually advanced for the days outstanding, '
                                       'and the final dollars the client keeps.',
                             'example': 'Batch face value $100,000 at an 80 percent advance puts $80,000 '
                                        'in the account on day one. Net proceeds equal face value minus '
                                        'the fee on gross receivables minus interest on the amount '
                                        'actually advanced for the days outstanding [LetsLearn Global — '
                                        'qEKcL_abQ9c @ 00:13:58]. A 3 percent first-30-day discount costs '
                                        '$3,000, quoted per batch, never annualized.'},
                            {'name': 'bank_vs_factoring_comparison',
                             'type': 'textarea',
                             'prompt': 'Build the bank-versus-factoring comparison using the real interest '
                                       'rate and the actual days to collect. Show the added factoring cost '
                                       "in dollars, note the current prime rate beside the factor's "
                                       'effective rate, and state your recommendation to the client.',
                             'example': "Johnson's worksheet runs the real bank rate and actual days to "
                                        'collect so the added factoring cost shows up in dollars [Ian '
                                        'Johnson — Lu16E6BvvDE @ 00:00:34]. Prime sits next to the '
                                        "factor's effective rate on the same page [Ian Johnson — "
                                        'Lu16E6BvvDE @ 00:02:55]. Recommendation: factor only slow payers, '
                                        'since the facility can grow as the client wins customers.'},
                            {'name': 'factoring_referral_income',
                             'type': 'textarea',
                             'prompt': 'Map the referral income from every factoring client you place or '
                                       'hand off. Record the program used, the commission structure, '
                                       'whether it pays for the life of the deal, the projected monthly '
                                       'residual, and your hard-to-place fallback partner.',
                             'example': 'A CPA referral placed with Universal Funding pays 20% commission '
                                        'for the life of the deal by monthly check [Universal Funding '
                                        'Corporation — 3PlJmybrzHs @ 00:01:26]. A trucking prospect no '
                                        'direct factor would take goes to Factor Finders, which places it '
                                        'with a partner and splits commissions fifty-fifty [Factor Finders '
                                        '— 8C1D2A4YVvQ @ 00:01:50].'}],
                 'completion_gate': 'Do not submit until the weak-demand case shows the payment is '
                                    'survivable, the credit screen and vendor verification are clean, PO '
                                    'or surety costs are built into the bid, the aging report is split by '
                                    'payer quality, every factor term including exit cost is answered, and '
                                    'net proceeds and residual income are written in dollars.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Borrowing Base, Supply Chain, and SBA Fit Worksheet',
                 'purpose': 'Convert trapped receivables and inventory into a defensible borrowing base, '
                            'test cheaper supply chain and trade credit alternatives, then triage '
                            'owner-user and acquisition requests into the right SBA 7(a) or 504 structure '
                            'before any package reaches a lender.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ["Work from the client's current aging report and inventory listing, not "
                                  'from summaries or verbal estimates.',
                                  'Strip past-due receivables and concentration excess before applying any '
                                  'advance rate, because lenders underwrite to liquidation rather than '
                                  'face value.',
                                  'Check vendor terms and buyer-led supply chain programs before '
                                  'recommending a borrowing base facility or inventory line.',
                                  'For SBA requests, confirm 51% owner occupancy, filed tax returns, and '
                                  'debt service coverage before choosing between 7(a) and 504.',
                                  'Complete every field with dollar figures and dates so the finished file '
                                  "can land in the lender's A bucket."],
                 'fields': [{'name': 'aging_report_scrub',
                             'type': 'textarea',
                             'prompt': "List every receivable on the client's current aging report, then "
                                       'strike anything more than 30 days past due. Record the gross AR '
                                       'total, the dollar amount removed as past-due ineligibles, and the '
                                       'percentage of the pool that disappeared before any concentration '
                                       'cap applies.',
                             'example': "Gross AR from the distributor's aging report is $700,000. "
                                        'Invoices more than 30 days past due total about $63,000, roughly '
                                        '9% of the pool, matching the cut Evan Wagner saw in his sample '
                                        'borrowing base [Naturally New York — oobK7A-p9-U @ 00:33:19]. '
                                        'Those invoices are flagged ineligible now, so the lender never '
                                        'finds them first.'},
                            {'name': 'concentration_cap',
                             'type': 'text',
                             'prompt': 'Identify any single customer whose balance exceeds 25% of '
                                       'remaining eligible receivables. Write the customer name or code, '
                                       'the excess dollar amount stripped by the concentration threshold, '
                                       'and the resulting net eligible AR figure you will carry forward '
                                       'into the advance calculation.',
                             'example': 'Customer code D-114 carries a balance well above 25% of the '
                                        'remaining pool. Most lenders cap one account at 25%, so roughly '
                                        "$77,000 of excess is stripped, about the 11% slice Wagner's cap "
                                        'removed [Naturally New York — oobK7A-p9-U @ 00:33:42]. Net '
                                        'eligible AR now stands near $560,000 for the advance '
                                        'calculation.'},
                            {'name': 'receivables_advance',
                             'type': 'text',
                             'prompt': "Apply the lender's receivables advance rate to net eligible AR and "
                                       "record the resulting availability. Note whether the end customer's "
                                       'certainty of payment supports the higher advance tier, and state '
                                       'the rate you will pitch with one sentence of justification.',
                             'example': 'At 85 cents on the dollar, the advance Wagner applied when 586 of '
                                        'net eligible AR produced 498 [Naturally New York — oobK7A-p9-U @ '
                                        '00:39:00], $560,000 yields $476,000 of availability. The end '
                                        'customers are large, reliable payers, and certainty of payment is '
                                        'what moves an advance toward 90% rather than 70-80% [FinanceKid — '
                                        'u5hujmtiiaY @ 00:08:59].'},
                            {'name': 'inventory_component',
                             'type': 'textarea',
                             'prompt': 'Describe the finished-goods inventory the client wants included in '
                                       "the base. Record the lender's lesser-of test using cost advance "
                                       'and NOLV, then explain whether inventory financing should wait as '
                                       'a last resort given its fees, pricing, warehousing, and audit '
                                       'burden.',
                             'example': "Finished goods carry $300,000 at cost. Under SG Credit Partners' "
                                        'sample, availability is the lesser of 65 cents or 85% of NOLV '
                                        '[Naturally New York — oobK7A-p9-U @ 00:39:00]. Even so, we hold '
                                        'inventory back because double fees, Prime+4-6% pricing, '
                                        'warehousing costs, and 3-6 month audits make it a last resort '
                                        '[FinanceKid — u5hujmtiiaY @ 00:16:25].'},
                            {'name': 'liquidity_runway',
                             'type': 'text',
                             'prompt': "Add excess availability to cash on hand and divide by the client's "
                                       'average monthly historical burn. Record the months of runway, then '
                                       'state whether the file clears a 12-month cushion or sits in the '
                                       'tough-call zone near three months.',
                             'example': 'Excess availability of $180,000 plus $120,000 cash equals '
                                        '$300,000 against a $22,000 monthly burn, about 13.6 months of '
                                        'runway. That clears the at-least-12-months test Wagner applies, '
                                        'where three months would be a tough call [Naturally New York — '
                                        'oobK7A-p9-U @ 00:48:23]. The file moves forward without a request '
                                        'for an additional equity cushion.'},
                            {'name': 'scf_and_trade_credit',
                             'type': 'textarea',
                             'prompt': 'Before sizing debt, check whether vendor terms or a buyer-led '
                                       'supply chain finance program could fund the gap more cheaply. '
                                       "Record the supplier's current borrowing rate, the buyer's rate "
                                       'available through the program, and the arbitrage you will present.',
                             'example': 'First question: can the client stretch payables? Walton calls '
                                        'trade credit often the cheapest capital when available '
                                        '[Commercial Loan Broker Institute — 4fxpQTB_spA @ 00:06:12]. '
                                        "Second, the client's largest buyer runs a supply chain program, "
                                        "so this supplier could fund at the buyer's 2% instead of its 12% "
                                        'bank loan, which Vanijja likens to co-signing [Vanijja | Trade '
                                        'Insights — RcVypdN4SHs @ 00:04:08].'},
                            {'name': 'sba_owner_user_triage',
                             'type': 'textarea',
                             'prompt': 'For any owner-user real estate request, capture only the three '
                                       'triage items: use of proceeds with amount, the business website, '
                                       'and the property address. Then record the payment estimate per '
                                       "million borrowed and compare it against the client's current rent.",
                             'example': 'Use of proceeds: buy the occupied building for $2 million. '
                                        "Website and address confirm an operating owner-user; Rosenthal's "
                                        'three items call lender fit in about three minutes [My SBA Loan '
                                        'Pro Podcast — XKIBsDDkBUI @ 00:30:41]. At roughly $6,000 per '
                                        'month per million, payment lands near $12,000 versus $11,500 '
                                        'current rent [My SBA Loan Pro Podcast — XKIBsDDkBUI @ 00:32:41].'},
                            {'name': 'program_selection_7a_vs_504',
                             'type': 'textarea',
                             'prompt': 'Compare 7(a) and 504 structures for this request. Record occupancy '
                                       'percentage, down payment, rate type, and whether the plan involves '
                                       'value-add work or heavy working capital, then name the program you '
                                       'will recommend and the reason in one sentence.',
                             'example': 'The client occupies 70% of the building, above the 51% owner-user '
                                        'floor [CDC Small Business Finance — C-omBBP27hg @ 00:00:06]. No '
                                        'value-add or large working-capital need exists, so the 504 fits: '
                                        'a 50% bank first, 40% debenture, and 10% down, blending the 6.2 '
                                        'debenture with prime-plus-one senior debt into the sevens [Beau '
                                        'Eckstein, Business Ownership Coach — aBEJBn_bUA0 @ 00:01:28].'},
                            {'name': 'acquisition_tax_return_check',
                             'type': 'textarea',
                             'prompt': "For a business acquisition, confirm the seller's returns were "
                                       'actually filed, that cash revenue appears on them, and that the '
                                       'latest returns arrive by June 30. Record debt service coverage on '
                                       'the most recent return and year-to-date figures.',
                             'example': 'Seller filed all three years; transcripts should match because '
                                        'underwriting reconciles returns to IRS transcripts [Commercial '
                                        'Loan Broker Institute — 8-4I4VOIIqg @ 00:38:11]. The current '
                                        'return is promised by June 30, not an October extension '
                                        '[Commercial Loan Broker Institute — CvS7BttXuu0 @ 00:15:04]. '
                                        'Coverage is 1.31x on the latest return and 1.28x year-to-date, '
                                        "above Trillant's 1.25x standard."},
                            {'name': 'working_capital_and_package_status',
                             'type': 'textarea',
                             'prompt': 'Record the net working capital figure both parties agreed to at '
                                       'LOI, any real estate buildout bid with a 10% contingency, and the '
                                       'package completeness status that determines whether the file lands '
                                       "in the lender's A, B, or C bucket.",
                             'example': 'Net working capital was narrowed to $150,000 at LOI instead of '
                                        'leaving a 500,000 versus 100,000 gap for closing [Commercial Loan '
                                        'Broker Institute — 8-4I4VOIIqg @ 00:39:20]. The $200,000 buildout '
                                        'bid becomes $220,000 with contingency [SBA University — '
                                        'py_IPiHezcw @ 00:03:50]. The package is complete, aiming for the '
                                        'A bucket of a lender seeing seven or eight deals daily.'}],
                 'completion_gate': 'Do not submit until net eligible AR, availability, runway of at least '
                                    '12 months, the 7(a) or 504 recommendation, filed-return confirmation, '
                                    'and a complete package are all recorded with figures.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'MCA Restructuring and Working Capital Offer Worksheet',
                 'purpose': 'Map every merchant cash advance position from the original contracts, stop '
                            'the stacking spiral, climb the takeout ladder from refinance to attorney-led '
                            'restructure, and screen new revenue-based or working capital offers against '
                            'hard refusal thresholds before a client signs.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ["Pull original MCA agreements, bank statements, and the owner's license "
                                  "from the client's own records without alerting any funder.",
                                  'Instruct any client holding more than three advances to take no new '
                                  'positions while the plan is built.',
                                  'Route any lawsuit, confession of judgment, or active UCC enforcement to '
                                  'an attorney before discussing settlement options.',
                                  'Quote every alternative offer in total payback and real term, never '
                                  'only the daily payment or factor rate.',
                                  'Tie any new funding to a documented 13-week cash map and one qualifying '
                                  'purpose.'],
                 'fields': [{'name': 'mca_debt_schedule',
                             'type': 'textarea',
                             'prompt': 'Build the written debt schedule from the original funder contracts '
                                       "pulled from the client's own records, never from broker summaries. "
                                       'List every position, remaining balance, daily or weekly pull, '
                                       'factor rate, and true payback for each advance.',
                             'example': 'Position one: $80,000 remaining, $1,100 daily, 1.35 factor. '
                                        'Position two: $45,000 remaining, $650 daily, 1.42 factor. '
                                        'Position three: $30,000 remaining, $2,400 weekly. All three '
                                        "positions came from the client's signed contracts, as Siegel "
                                        'insists [Zach Siegel — w-ETPb-Trek @ 00:03:56], and no funder was '
                                        'asked for copies [Zeus Commercial Capital | Business & RE Loans — '
                                        'OccRWwWbI2M @ 00:02:10].'},
                            {'name': 'stacking_load',
                             'type': 'text',
                             'prompt': 'Total all daily-equivalent MCA withdrawals and divide by average '
                                       'daily card receipts or deposits. Record the percentage, flag the '
                                       'file if it reaches the 30 to 40 percent collapse zone, and note '
                                       'whether the client has agreed to stop stacking.',
                             'example': 'Daily pulls total about $2,230 ($1,100 plus $650 plus $480 '
                                        'weekly-equivalent) against $6,500 in average daily receipts, or '
                                        "34%. That sits inside Wadley's thirty-to-forty percent zone where "
                                        'rent and payroll stop getting covered [Gap Funding | 100% Real '
                                        'Estate Financing — OWlnOeMGBkg @ 00:01:35]. The owner signed off '
                                        'on no new advances [Zach Siegel — w-ETPb-Trek @ 00:03:16].'},
                            {'name': 'ucc_lien_audit',
                             'type': 'textarea',
                             'prompt': 'Pull every UCC-1 filed against the business and compare the debtor '
                                       'name on each filing to the exact legal entity name. Record any '
                                       'typo, any DBA used in place of the legal entity, and whether the '
                                       'contract was framed as a sale.',
                             'example': "Funder two filed under the trade name 'Riverside Grill' rather "
                                        'than the legal entity, and Berkshire notes a DBA in place of the '
                                        'legal entity can invalidate the lien [Berkshire Financial '
                                        'Services LLC — V8S0sywozwU @ 00:00:31]. All three agreements are '
                                        'framed as receivable purchases, so we flag whether a security '
                                        'interest was even permitted [Berkshire Financial Services LLC — '
                                        'V8S0sywozwU @ 00:00:47].'},
                            {'name': 'legal_escalation',
                             'type': 'text',
                             'prompt': 'Note whether any funder has an active UCC enforcement action, '
                                       'confession of judgment, or lawsuit pending against the client. If '
                                       'any exists, record the attorney referral and date, because '
                                       'non-attorney relief companies should not handle those matters.',
                             'example': 'Funder one filed a lawsuit last week after two missed debits. The '
                                        'file was referred to a restructuring attorney the same day, '
                                        'following the rule that any UCC enforcement, confession of '
                                        'judgment, or lawsuit goes to counsel rather than a non-attorney '
                                        'relief company [Gap Funding | 100% Real Estate Financing — '
                                        'OccRWwWbI2M @ 00:02:53]. Settlement-company talks are paused.'},
                            {'name': 'takeout_ladder',
                             'type': 'textarea',
                             'prompt': 'Place the client on the takeout ladder: conventional or SBA '
                                       'refinance first, asset-backed takeout second, attorney-led '
                                       'restructure last. Record credit, coverage, whether the proposed '
                                       'payment improves monthly cash flow by 10 percent, and the current '
                                       'lender stance on MCA payoffs.',
                             'example': 'Hookima says SBA refinancing needs a 10 percent monthly cash flow '
                                        'improvement, which MCA files usually clear [ProjectionHub — '
                                        '_V39MGbzjw0 @ 00:00:21]. But The Approved Guy reports new SBA '
                                        'rules disqualify 7(a) MCA refinances [The Approved Guy — '
                                        'spCn3Rbs4XY @ 00:00:00]. With that split unresolved and '
                                        'free-and-clear trucks on the balance sheet, we test an '
                                        'asset-backed takeout next.'},
                            {'name': 'restructure_vs_settlement',
                             'type': 'textarea',
                             'prompt': 'If the file lands on the bottom rung, compare an attorney-led '
                                       'restructure against a debt settlement company. Record expected '
                                       'monthly payment relief, fee structure, likely payoff range, and '
                                       'whether the proposal lowers total cost or simply reschedules the '
                                       'pain.',
                             'example': 'Attorney route: Boore cites 50 to 80 percent monthly savings '
                                        'ending in a zero-balance letter [The Approved Guy — dDwHOnFlzaA @ '
                                        '00:01:28]. Settlement route: 15 to 30 percent fees with payoffs '
                                        'landing at 40 to 65 percent of balance [Gap Funding | 100% Real '
                                        'Estate Financing — OWlnOeMGBkg @ 00:05:18]. We demand total '
                                        'payback and real term before choosing.'},
                            {'name': 'revenue_based_sizing',
                             'type': 'text',
                             'prompt': 'Average the last three to six months of deposits and size any '
                                       'revenue-based advance against that figure. Record the average, the '
                                       'advance range, the quoted factor rate, origination percentage, and '
                                       'holdback, and confirm the file meets the qualification floor.',
                             'example': 'Separate unstacked file: six-month average deposits are $60,000, '
                                        "so Camberato's 100-150% sizing points to $60,000 to $90,000 [Joe "
                                        'Camberato — U1zLsMRu1ig @ 00:01:22]. Quote: 1.10 factor plus 2% '
                                        'origination, 6% holdback. The owner has a 610 score, 3 years in '
                                        "business, and full statements, clearing Shvarts's 550, six-month, "
                                        '$20,000 floor [Unbankable with Alex Shvarts — MNdDLiTLoNY @ '
                                        '00:07:16].'},
                            {'name': 'offer_red_flag_screen',
                             'type': 'textarea',
                             'prompt': 'Screen every alternative offer for red flags before the client '
                                       'signs. Record the factor rate, origination as a percentage of the '
                                       'advance, prepayment incentive terms, and debit frequency, and '
                                       'reject any first funding that crosses the refusal thresholds.',
                             'example': 'Offer B came in at a 1.499 factor with 12% origination on a first '
                                        "funding, so it is refused: Siegel's line is 1.499 or origination "
                                        'above 10% [Zach Siegel — Yq5OojmQIac @ 00:01:47]. Offer A '
                                        'forgives 15% of remaining fees on early payoff; Offer C has no '
                                        'prepayment incentive at all, an instant red flag [Zach Siegel — '
                                        'Yq5OojmQIac @ 00:02:26].'},
                            {'name': 'bank_account_readiness',
                             'type': 'text',
                             'prompt': 'Before connecting any bank account through Plaid, count the '
                                       "client's negative-balance days per month and calculate the average "
                                       'daily balance. Record both figures and the cleanup steps needed to '
                                       'reach four or fewer negative days and a $3,000 balance.',
                             'example': 'Last month showed six negative days and a $2,100 average daily '
                                        'balance, so the Plaid connection waits. The owner will keep a '
                                        'larger cash cushion in the account until negative days drop to '
                                        'four or fewer and the average daily balance reaches $3,000 '
                                        '[Business Credit — L3n2zgxag4E @ 00:06:10]. Recheck scheduled '
                                        'after thirty days.'},
                            {'name': 'thirteen_week_purpose',
                             'type': 'textarea',
                             'prompt': 'Map 13 weeks of cash in and cash out, then state which qualifying '
                                       'purpose the money serves: bridging to higher revenue, easing '
                                       'seasonality, fulfilling a contract, or fixing operations. Attach '
                                       'the one-page brief covering need, timing, repayment, and downside '
                                       'plan.',
                             'example': 'The 13-week map shows a $70,000 trough in weeks five through nine '
                                        'while a municipal contract ramps up, so the purpose is contract '
                                        'fulfillment [Brian M. Hazel Quotes — e3NbWehFdJs @ 00:01:17]. The '
                                        'one-page brief covers need, why now, repayment from contract '
                                        'receivables, and a downside plan that draws a revolving line only '
                                        'as jobs start [Brian M. Hazel Quotes — e3NbWehFdJs @ 00:03:01].'}],
                 'completion_gate': 'Do not present any takeout, restructure, or new advance until the '
                                    'debt schedule, stacking percentage, UCC audit, legal escalation '
                                    'status, and red-flag screen are complete and reconciled to the funder '
                                    'contracts.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'DSCR, Capital Stack, and Specialty Credit Worksheet',
                 'purpose': 'Size investment property and commercial real estate loans with DSCR, debt '
                            'yield, and back-solved maximum loan math, then structure the capital stack, '
                            'bridge exit, transferable tax credit purchase, or litigation funding request '
                            'so each layer is priced and documented.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ["Use market rent from your own comps alongside the client's rent, "
                                  "because the lender relies on the appraiser's rent schedule.",
                                  'Run DSCR and debt yield side by side and check the bar for this '
                                  'specific asset class.',
                                  'Back into maximum loan size before the client makes an offer or goes '
                                  'under contract.',
                                  'Layer the cheapest senior money first and add expensive risk capital '
                                  'only where a documented gap remains.',
                                  'Record every credit support, exit plan, and funder approach with dates '
                                  'and the supporting practitioner figure.'],
                 'fields': [{'name': 'dscr_two_rent_test',
                             'type': 'text',
                             'prompt': "Calculate DSCR twice: once using the client's actual or projected "
                                       'rent and once using market rent from your own comps. Record both '
                                       'ratios against full PITI and state whether the deal works at '
                                       'market rent or only at the higher number.',
                             'example': 'Duplex payment is $2,017 on a $240,000 loan at 6.5%. Client rent '
                                        'of $2,500 gives 1.24; market comps at $2,400 give 1.19, one '
                                        'hundredth below a 1.2 target, the same $11-per-side gap Turner '
                                        'describes [Brandon Turner | Real Estate Investor — -W2ThDxeu-o @ '
                                        "00:09:19]. Working only at the client's number means hope, not a "
                                        'deal.'},
                            {'name': 'operating_reserves',
                             'type': 'textarea',
                             'prompt': 'Underwrite the deal and not just the loan. Record monthly '
                                       'set-asides for vacancy, repairs, capital expenditures, and '
                                       'management as dollar amounts, then show how much buffer remains '
                                       'between rent and debt service once those reserves come out.',
                             'example': 'On $2,500 rent: 3% vacancy is $75, 5% repairs is $125, 5% capex '
                                        'is $125, and 10% management is $250, totaling $575. Against the '
                                        '$2,017 payment, the $483 gross buffer is consumed and a $92 '
                                        "monthly gap appears, confirming Turner's warning that a 1.2 "
                                        'approval leaves little room [Brandon Turner | Real Estate '
                                        'Investor — -W2ThDxeu-o @ 00:11:42].'},
                            {'name': 'max_loan_backsolve',
                             'type': 'textarea',
                             'prompt': 'Back into the maximum loan before any offer goes out. Divide NOI '
                                       "by the lender's minimum coverage to find allowable annual debt "
                                       'service, convert to monthly, then record the loan amount that '
                                       'payment supports at the quoted rate and amortization.',
                             'example': 'NOI of $100,000 divided by 1.25 caps annual debt service at '
                                        '$80,000, or $6,667 monthly. Calton shows that payment supports '
                                        '$1,112,000 at 6%, $1 million at 7%, and $943,000 on a 25-year '
                                        'amortization [Real Estate Finance Academy with Trevor Calton — '
                                        '2cFIwSgUOQM @ 00:01:38]. If rates rise, the loan amount shrinks '
                                        'to stay within coverage.'},
                            {'name': 'debt_yield_check',
                             'type': 'text',
                             'prompt': 'Compute debt yield for the proposed loan and compare it to the '
                                       "lender's stated bar for this asset class. Record the result next "
                                       'to DSCR, and if it falls short, the lower LTV needed to clear the '
                                       'requirement.',
                             'example': "Tactica's case cleared 1.20 DSCR at 65% LTV yet still had to drop "
                                        'to 60% LTV to reach a 10.64% debt yield against a 10.5% bar '
                                        '[Tactica RES — ZgYmvPS5gJY @ 00:05:06]. Our owner-occupied file '
                                        'faces a bar often at 11% to 13% or more [Academy For Commercial '
                                        'Lending — NHfs2vBPCys @ 00:05:22], so LTV is resized now.'},
                            {'name': 'five_plus_unit_box',
                             'type': 'textarea',
                             'prompt': 'If the property has five or more units, confirm the borrower fits '
                                       'the commercial DSCR entry box. Record credit score, down payment '
                                       'percentage, months of PITI reserves, and which accounts supply '
                                       'those reserves, noting any asset type credited below full balance.',
                             'example': 'Eight-unit building: borrower shows a 702 score and 25% down, '
                                        "meeting Marks's 680, 25%, six-month, 1.0 DSCR box [SEI Mortgage - "
                                        'Ryan Marks — OOFsomPO_Mc @ 00:02:05]. Six months of PITI comes '
                                        'from a 401k plus business checking; the lender was told the 401k '
                                        'up front since not every account counts at 100% [SEI Mortgage - '
                                        'Ryan Marks — OOFsomPO_Mc @ 00:07:48].'},
                            {'name': 'coverage_levers',
                             'type': 'textarea',
                             'prompt': "When DSCR lands just under the lender's floor, list the structural "
                                       'levers you will test, such as a longer term, interest-only '
                                       'payments, seller concessions, or a larger down payment, and record '
                                       'the revised ratio each lever produces.',
                             'example': "The rental sits at 0.98, so Glazer's 40-year term and an "
                                        'interest-only option are both tested [AD Mortgage — -j6-Ev4L24c @ '
                                        '01:09:49]. Up to 6% seller concessions go into the offer to buy '
                                        'down the rate [SEI Mortgage - Ryan Marks — OOFsomPO_Mc @ '
                                        '00:05:14]. At 60-65% LTV, some lenders do not require 1.0 '
                                        'coverage [Eli the DSCR Pro — 6P1p0e_NBxs @ 00:04:29].'},
                            {'name': 'capital_stack_layers',
                             'type': 'textarea',
                             'prompt': 'Lay out the full capital stack from cheapest senior money to the '
                                       "most expensive risk capital. Record each layer's share of total "
                                       'cost and its all-in price, and explain why any mezzanine or '
                                       'preferred equity is needed only where a gap remains.',
                             'example': "Senior bridge debt at 70% LTV prices inside Boucher's 7-12% range "
                                        'with 1% to 3-4% origination [Jeremiah Boucher — KFtBrowO6pc @ '
                                        '00:02:08]. Mezzanine and preferred equity, which run 15-20% '
                                        'all-in, enter only to fill a 10% gap; sponsor equity covers 20%. '
                                        'The cheapest money sits first, and expensive capital is rented '
                                        'sparingly.'},
                            {'name': 'bridge_exit_plan',
                             'type': 'textarea',
                             'prompt': 'Before any bridge loan is signed, map the exit and confirm an '
                                       'attorney has redlined the default provisions. Record whether the '
                                       'lender will fund capex, the interest reserve requested, the '
                                       'expected closing window, and the permanent takeout you will '
                                       'pursue.',
                             'example': 'Exit is a DSCR refinance once renovated units lease at market. '
                                        "Counsel redlined default provisions before signing, per Boucher's "
                                        'rule [Jeremiah Boucher — KFtBrowO6pc @ 00:07:15]. The lender '
                                        'agreed to fund capex and a 12-month interest reserve, keeping '
                                        'sponsor liquidity intact [Jeremiah Boucher — KFtBrowO6pc @ '
                                        '00:09:36]. Expected close is about 30 days.'},
                            {'name': 'tax_credit_pricing',
                             'type': 'textarea',
                             'prompt': 'For a transferable clean energy credit, record the pricing tier '
                                       'you expect, the credit support in place such as insurance, parent '
                                       'guarantees, or Big-4 memos, and the prevailing wage and '
                                       'apprenticeship verification completed before paying above the '
                                       'risk-taker tier.',
                             'example': 'Seller offers insurance, a parent guarantee, and a Big-4 memo, '
                                        'supporting a price near 92 cents versus roughly 85 cents '
                                        'unwrapped and 80 cents for risk-takers [Tax Alpha Insider — '
                                        'TQ86awlkdKw @ 00:16:11]. Prevailing wage was checked against '
                                        'Davis-Bacon on sam.gov with apprenticeship records before bidding '
                                        'above 80 cents [Tax Alpha Insider — TQ86awlkdKw @ 00:19:34].'},
                            {'name': 'litigation_funding_fit',
                             'type': 'textarea',
                             'prompt': 'If a client seeks commercial litigation funding, record realistic '
                                       'case value against the requested commitment, the target multiple, '
                                       'the weaknesses you will surface up front, and the short list of '
                                       'targeted funders you will approach under NDA.',
                             'example': 'Requested commitment is $500,000 against realistic case value '
                                        'near $5 million, meeting the roughly 10x ratio funders want, with '
                                        'a 2-4x target return. Statera accepts only 3-5% of cases [The '
                                        'National Law Review — cBxujqoCcbY @ 00:38:00], so three targeted '
                                        'funders receive an NDA, budget, timeline, and case outline, '
                                        'weaknesses included [The National Law Review — cBxujqoCcbY @ '
                                        '00:44:50].'}],
                 'completion_gate': 'Do not release the file until DSCR at market rent, debt yield against '
                                    'the asset-class bar, maximum loan, the full capital stack, and any '
                                    'bridge exit or credit verification are documented with figures.'}]}
