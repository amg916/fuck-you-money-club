from __future__ import annotations

def build_volume_041_workbook() -> dict:
    return {'workbook_id': 'wb-041-buying-group-card-float-and-rebate-arbitrage',
 'volume_id': 'vol-041-buying-group-card-float-and-rebate-arbitrage',
 'title': 'Buying Group, Commercial Card-Float & Rebate Arbitrage — Practitioner Testimony Operator '
          'Workbook',
 'subtitle': 'Buying-group reimbursement spreads, promo gift card exits, interest-free card float, limit '
             'growth timing, Amex financial review defense, and Capital One Spark charge-card economics, '
             'worked through operator worksheets',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Buying Group Order Survival & Gift Card Exit Ledger',
                 'purpose': 'Lock down the cash ceiling, platform choice, order mechanics, and exit routes '
                            'before a single buying-group order or promo gift card goes on a card, so '
                            'every swipe has a reimbursement, a buyer, or a repayment path already '
                            'committed.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Fill in the float ceiling first; every later field must fit inside the '
                                  'cash actually sitting in checking today.',
                                  'Log every order in a spreadsheet with exact SKU, color, model, payout '
                                  'price, order size, and ship-to address as posted by the group.',
                                  'Run all math with the practitioner spreads in view: 2-5 percent per '
                                  'deal, rarely 10, with points and minimum spend as the real prize.',
                                  'Treat every Discord DM, unverified address, and buyer without an agreed '
                                  'rate as a stop signal, not a negotiation.',
                                  'Complete the liquidation and tax fields even if you never plan to '
                                  'liquidate, so the cost and reporting exposure are known in advance.'],
                 'fields': [{'name': 'float_ceiling_vs_bank_balance',
                             'type': 'text',
                             'prompt': 'Write the exact dollar amount currently sitting in your checking '
                                       'account, then set the maximum total you will float across all open '
                                       'buying-group orders awaiting reimbursement. State how many days of '
                                       'pending payouts that ceiling must survive without touching other '
                                       'funds.',
                             'example': 'Checking balance is $14,000, so the float ceiling is $12,000, '
                                        'leaving a cushion for pending charges. Julie recalls an attendee '
                                        "who said 'I lost $60,000' after floating beyond cash on hand "
                                        '[Geobreeze Travel — zay5oOKCEls @ 00:18:11]. The ceiling must '
                                        'also absorb the 5-7 days that pending charges can take before '
                                        'failed orders clear.'},
                            {'name': 'group_and_platform_selection',
                             'type': 'textarea',
                             'prompt': 'Name the buying group you will start with and justify it against '
                                       'at least one alternative. Record its payout method, payout speed, '
                                       'how deals are posted, and any secrecy or communication concerns '
                                       'practitioners raised about that group before committing money.',
                             'example': 'Starting with BFMR, the consensus beginner pick for fast, simple '
                                        'payouts; the group sends an ACH transfer back as soon as it '
                                        'receives the package [Czech It Out: Money Hacks — HNO_8rnhPeE @ '
                                        "00:00:54]. Mitch distrusts BFMR's secrecy, so deal terms get "
                                        "screenshotted. Eunice's alternative, gift-card groups with fixed "
                                        'payout dates, stays on the backup list.'},
                            {'name': 'reserve_before_research_log',
                             'type': 'text',
                             'prompt': 'Describe your rule for committing to a deal before researching it, '
                                       'given that reservations hold only a short window. List which '
                                       'details you will verify inside that window: exact SKU, color, '
                                       'model, payout price, and the posted ship-to address.',
                             'example': 'Reserve first, because reservations hold only a 12 to 24 hour '
                                        'window [Lets Get To The Points — mEjNm8zKoQs @ 00:35:32]. Inside '
                                        'that window, match the exact SKU, since a wrong color or model '
                                        'means no reimbursement, and log the payout price in a spreadsheet '
                                        'because payout prices can change. Release the reservation if the '
                                        'retail price no longer fits.'},
                            {'name': 'spread_versus_points_math',
                             'type': 'textarea',
                             'prompt': 'Estimate the profit spread on your next three deals and the card '
                                       'rewards each will earn. Show whether the trade still works at '
                                       'break-even, and project annual points from your expected volume '
                                       'using a stated earning multiplier on your primary card.',
                             'example': 'Spread on buying-group deals usually runs 2-5 percent and rarely '
                                        '10 [Frequent Miler — nMlQUH3s8qY @ 00:38:29], so the real prize '
                                        'is points and minimum spend. At about $250,000 a year on a 4x '
                                        'card, volume yields roughly 1M points. Czech It Out reported '
                                        '$1,800 in July on about $70,000 processed, which sets a realistic '
                                        'first-month benchmark.'},
                            {'name': 'order_size_and_checkout_method',
                             'type': 'text',
                             'prompt': 'Set your maximum single-order size and the checkout method you '
                                       'will use for each retailer. Note whether you will route payment '
                                       "through a wallet service, where the card's billing address points, "
                                       'and how you will split any larger purchase.',
                             'example': 'Orders stay between $500 and $1,000 after a $2,000 Target order '
                                        'was cited as an oversized-order flag [John Muscarello — '
                                        'ThO9ard-k8E @ 00:03:24]. Checkout runs through PayPal, Apple Pay '
                                        "or Shop Pay to mask billing, and the card's billing address is "
                                        'set to the prep center. A $1,800 restock gets split into two '
                                        'separate orders.'},
                            {'name': 'ship_to_verification_and_alerts',
                             'type': 'text',
                             'prompt': 'Record where you receive deal alerts and how you confirm every '
                                       'shipping address before checkout. Name the official channel where '
                                       'addresses are posted, and write the rule you will follow when '
                                       'someone claiming to be an admin sends a direct message.',
                             'example': "Alerts come from Max Out Deals' Discord, which carries the "
                                        'timeliest posts [Geobreeze Travel — zay5oOKCEls @ 00:20:49]. '
                                        'Shipping goes only to addresses posted by the group itself. Any '
                                        "DM from an 'admin' gets ignored and reported, because "
                                        'impersonators redirected about $20k of goods. Before each '
                                        'checkout, the address is compared character by character against '
                                        'the posted listing.'},
                            {'name': 'failed_order_and_returns_rule',
                             'type': 'text',
                             'prompt': 'Write your protocol for a declined or cancelled order and for '
                                       'inventory that never sells. State how long you will wait before '
                                       'retrying, what you will do with stuck pending charges, and why '
                                       'returns are off the table for this account.',
                             'example': 'No resubmits while pending charges sit for 5-7 days, and no '
                                        'returns of unsold items, because returns are a red flag [John '
                                        'Muscarello — rpJHRiGfebQ @ 00:11:25]. For in-store pickup, the '
                                        'cart is loaded in-aisle and paid with a card not linked to the '
                                        'store account, since Target tracks it. Failed orders get logged, '
                                        'not retried the same day.'},
                            {'name': 'gift_card_buyer_lock',
                             'type': 'textarea',
                             'prompt': 'Before buying any promotion-sourced gift cards, name the buyer, '
                                       'the agreed buy rate as a percentage of face value, and the card '
                                       'offer generating your margin. Show the margin calculation and the '
                                       'format, physical or electronic, that actually triggers the offer.',
                             'example': 'QCGC buys $100 Walmart gift cards at 91.5% of face against the '
                                        'Amex spend $100, get 25% back offer, a 16.5% margin [Geobreeze '
                                        'Travel — QTa7eNv00k4 @ 00:21:49]. Cards are bought physically '
                                        'in-store, since e-gift cards processed through CashStar will not '
                                        'trigger the offer. No card is purchased until the buyer confirms '
                                        'that rate in writing.'},
                            {'name': 'liquidation_route_cost_and_test',
                             'type': 'textarea',
                             'prompt': 'If you plan to convert card credit to cash, list each route you '
                                       'are considering with its fee, payout timeline, and net cost after '
                                       'card rewards. Describe the small test transfer you will run first '
                                       'and which bank receives the funds.',
                             'example': 'Liquidators charge 5% to 6% over 5-10 business days, per Alex '
                                        'Barajas, while invoice and PayPal routes run about 2-3%. A 6% fee '
                                        'minus 2% card rewards nets about 4% [Naam Wynn — AsYTdszcmx8 @ '
                                        '00:10:07]. A $100 test goes first and must land before thousands '
                                        'move, and cash never deposits into the bank it was pulled from.'},
                            {'name': 'tax_reporting_1099k',
                             'type': 'textarea',
                             'prompt': 'Total your expected gross sales across payment processors and '
                                       'third-party networks for the year. Compare that figure against the '
                                       'reporting threshold, name the EIN or SSN the forms will be issued '
                                       'under, and state how sales will appear on your return.',
                             'example': 'Expected network sales of $38,000 clear the $5,000 Form 1099-K '
                                        'threshold cited for calendar year 2024 [James Baker CPA — '
                                        'w7-zxRnNOSo @ 00:00:58]. Sales get reported at or above the '
                                        '1099-K total under the matching EIN to avoid an audit flag, and a '
                                        'return gets filed reporting those sales even if there is no tax '
                                        'to pay.'}],
                 'completion_gate': 'All ten fields are filled with your own numbers; the float ceiling is '
                                    'at or below your checking balance; the ship-to rule names the '
                                    'official posting channel; a buyer and agreed rate are recorded for '
                                    'any gift card plan; and a $100 test transfer is scheduled before any '
                                    'liquidation route carries real volume.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Interest-Free Float Stack & Limit Growth Planner',
                 'purpose': 'Map every card, intro window, and issuer rule into one calendar so the float '
                            'stays interest-free, charge cards clear inside their cycle, and limit '
                            'increases are requested on schedule with clean repayment history instead of '
                            'guesswork.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Start with the pay-in-full rule; nothing else on this worksheet applies '
                                  'to a card that is accruing interest.',
                                  'Use exact dates for every 0% expiry, charge card statement close, and '
                                  'next eligible limit increase request.',
                                  'Count banks, not cards, when confirming rotation depth, and record any '
                                  'limit cut as it happens.',
                                  'Confirm pull type by phone or by reading the request page before every '
                                  'limit increase or reallocation.',
                                  'Revisit the cycling and exposure fields before any new application, '
                                  "since a single new line shifts every issuer's math."],
                 'fields': [{'name': 'issuer_economics_and_pay_in_full_rule',
                             'type': 'textarea',
                             'prompt': 'Explain in your own words how issuers earn money from your swipes '
                                       'and who funds the rewards you collect. Then write the single '
                                       'pay-in-full rule you will follow, including what happens to any '
                                       'rewards strategy the month interest appears.',
                             'example': 'Issuers already profit on 2 to 3% swipe fees, and about $15 '
                                        'billion a year moves from revolvers to pay-in-full cardholders '
                                        '[Mogulnomics — nzZ8nwy2xSY @ 00:03:29]. The rule: never pay '
                                        'interest to chase rewards, because a 2% cashback card cannot beat '
                                        'a 22% interest rate. Any month with interest pauses every rewards '
                                        'play until balances clear.'},
                            {'name': 'credit_stack_inventory',
                             'type': 'textarea',
                             'prompt': 'Inventory every card in your stack by type: 0% intro cards, charge '
                                       'cards, and regular revolving cards. For each, record the limit, '
                                       'the intro expiry date if any, and the issuer, then total the stack '
                                       'and the share at 0%.',
                             'example': "Joey's benchmark stack totals $277,000, with almost $142,000 at "
                                        '0% expiring June 2027, roughly $100,000 in charge cards, and '
                                        'about $36,000 in regular cards [Joey | Amazon FBA — tKw8SljNcPE @ '
                                        '00:10:37]. A smaller operator logs three 0% cards, one charge '
                                        'card, and two regular cards, totaling them the same way to see '
                                        'what share actually floats interest-free.'},
                            {'name': 'intro_expiry_map',
                             'type': 'textarea',
                             'prompt': 'Map every 0% intro expiry date on a calendar and identify where '
                                       'each expiring balance will land. Note the spacing between intros, '
                                       'the next window you plan to open, and the balance transfer fee you '
                                       'would accept as a fallback.',
                             'example': 'Intros get spaced about six months apart so every expiring '
                                        'balance has a fresh 0% card to land on [Joey | Amazon FBA — '
                                        'tKw8SljNcPE @ 00:08:19]. Elan offers the longest window at 18 '
                                        'months, versus Chase at 12 and Bank of America at 7. The fallback '
                                        'is an Elan balance transfer at around a 3% fee before the intro '
                                        'rate dies.'},
                            {'name': 'charge_card_clearance_test',
                             'type': 'text',
                             'prompt': 'Calculate how many days your cash conversion cycle takes from '
                                       'purchase to cash in hand. Compare that number against the roughly '
                                       '30-day charge card statement cycle and decide how much of your '
                                       'stack can safely sit on charge cards.',
                             'example': 'A charge-card-heavy stack only works when cash conversion can '
                                        'clear the full statement balance inside roughly 30 days [Joey | '
                                        'Amazon FBA — tKw8SljNcPE @ 00:02:52]. Inventory here turns in '
                                        'about 45 days, so charge cards carry only spend that converts '
                                        'faster, such as reimbursed buying-group orders, while slower '
                                        'inventory sits on 0% cards instead.'},
                            {'name': 'bank_rotation_and_application_sequence',
                             'type': 'textarea',
                             'prompt': 'List the banks currently in your rotation and confirm at least '
                                       'three before scaling. Write your application sequence for the next '
                                       'six months, including relationship seasoning periods, application '
                                       'timing, and the order for issuers that share underwriting '
                                       'visibility.',
                             'example': 'Rotation covers Amex, Chase, and Elan after Amex cut one card to '
                                        "a third and halved a charge line. Following McColl's playbook, "
                                        'bank relationships season 30 to 60 days and Amex applications go '
                                        'in after 7:00 p.m. Eastern. Elan comes first, then Elan balances '
                                        'stay low before applying at US Bank, because shared underwriters '
                                        'see them [Jack McColl — c5MGulNCfZ8 @ 00:09:44].'},
                            {'name': 'velocity_banking_cash_flow_check',
                             'type': 'text',
                             'prompt': 'If you are considering velocity banking, record your monthly '
                                       'income, monthly expenses, and the surplus between them. Show one '
                                       "cycle's interest calculation on the residual balance and state "
                                       'whether positive cash flow exists to make the method work at all.',
                             'example': 'Maria pushes $3,500 onto a $4,000 card on day one, then charges '
                                        '$3,200 of living expenses back on through the month, paying about '
                                        '$7.87 on a $500 residual at 19% APR over 30 days [Stephen Smith — '
                                        'bYSi0VFWtpg @ 00:07:22]. The method works only if income exceeds '
                                        'expenses, even by $100 a month.'},
                            {'name': 'income_update_and_primary_spender_plan',
                             'type': 'textarea',
                             'prompt': 'Record the household income currently on file with each issuer and '
                                       'the date you will update it. Name the target card that will serve '
                                       'as primary spender for about three months, and describe how you '
                                       'will pay it down before requesting.',
                             'example': 'Household income gets updated first, following Naam Wynn, Colin '
                                        'Matthew and Bella Sloan Enterprises. The Navy Federal card then '
                                        'runs as primary spender for three months with every statement '
                                        'paid on time, because heavy usage means nothing without timely '
                                        'payments [Stephen Smith — RY2Q9yq3v3E @ 00:04:25]. The balance '
                                        'drops to near zero before the request goes in.'},
                            {'name': 'issuer_specific_increase_calendar',
                             'type': 'textarea',
                             'prompt': 'For each issuer you hold, write the earliest date you can request '
                                       'a limit increase and the spacing you will use afterward. Include '
                                       'the ask size you plan, either a large multiple or a smaller '
                                       'percentage step, and justify your choice.',
                             'example': 'Amex at day 60 then every 90 days, Discover every 30 days, and '
                                        'Navy Federal at 190 to 195 days rather than 181. Cal Barton '
                                        'climbed Navy Federal from $10K in January 2020 to $66K in '
                                        'February 2024 in roughly $8K steps [Cal Barton — D6bPd67bgps @ '
                                        '00:07:26], so asks here run as 25-50% steps.'},
                            {'name': 'pull_type_confirmation_script',
                             'type': 'text',
                             'prompt': 'Write the short phone script you will use to confirm whether a '
                                       'limit increase request triggers a soft or hard pull. List the '
                                       'exact page phrases that will make you back out of an online '
                                       'request before submitting anything.',
                             'example': 'Script: ask which pull applies before submitting, because 30 '
                                        'seconds of asking saves you an inquiry [Bella Sloan Enterprises — '
                                        '2sUP7XrGRgM @ 00:07:12]. Online, back out if the page says '
                                        "'credit check', 'review your credit report', 'detailed credit "
                                        "evaluation', or 'consent to obtain your credit report'. After any "
                                        'denial, read the adverse-action reason before planning the next '
                                        'ask.'},
                            {'name': 'cycling_limits_and_exposure_caps',
                             'type': 'textarea',
                             'prompt': 'Set your monthly credit cycling ceiling for each issuer and the '
                                       "maximum charge as a share of the line. Record each issuer's "
                                       'approximate exposure cap against your income and note any limit '
                                       'you would lower to make room for a new card.',
                             'example': 'Cycling stays at one to three times per month with each charge '
                                        'under 70% of the line [Colin Matthew — gTpUtrhQsnM @ 00:12:28], '
                                        'and Capital One gets the least, since it cares most about '
                                        'cycling. Exposure caps run about 50% of income at Chase and 35% '
                                        'at Amex; cutting a Sapphire from $25K to $10K opened room for a '
                                        '$30K Ink.'}],
                 'completion_gate': 'Every card appears in the stack inventory with limit and expiry; each '
                                    '0% expiry has a named landing card or transfer fallback; at least '
                                    'three banks are in rotation; the charge-card share matches a cash '
                                    'conversion cycle near 30 days; and each issuer has a dated limit '
                                    'increase request with confirmed pull type.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Amex Review Defense & Capital One Spark Deployment',
                 'purpose': 'Build the documentation, spend curve, and points-exit plan that let an '
                            'operator survive an Amex financial review, then decide whether Spark Cash '
                            'Plus or Venture X Business earns its fee and personal-credit footprint in the '
                            'stack.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Pull six months of statements before starting; the velocity baseline '
                                  'and trigger audit depend on actual numbers, not memory.',
                                  'Assemble the documentation kit now, while there is no 14-day clock '
                                  'running.',
                                  'Treat Membership Rewards as exposed value until transferred to the '
                                  'redemption it is meant for.',
                                  'Run the Spark break-even with real projected business spend: inventory, '
                                  'software, ads, and other unavoidable costs.',
                                  'Write the exit strategy before the first Spark swipe, assuming the full '
                                  'statement must clear every month.'],
                 'fields': [{'name': 'spend_velocity_baseline',
                             'type': 'textarea',
                             'prompt': 'Calculate your average monthly Amex spend over the past six months '
                                       'and identify the largest single-month jump. Write the ramp '
                                       'schedule you will follow for any planned increase, and note when '
                                       'you will call ahead before a large purchase.',
                             'example': 'High-velocity spending sat behind 65% of financial reviews across '
                                        '20 data points [Cal Barton — 0pnnp262mLg @ 00:12:07], and spend '
                                        'above the six-month average raises a flag. Current average is '
                                        '$4,000, so the ramp runs 5K, then 10K, then 15K across months, '
                                        'with a call to Amex before any massive purchase rather than after '
                                        'the decline.'},
                            {'name': 'review_trigger_audit',
                             'type': 'textarea',
                             'prompt': 'Audit your recent activity against the known review triggers: '
                                       'returned payments, repeated spending power checks, limit cycling, '
                                       'cash-like purchases, large transfers to others, and stated income '
                                       'you cannot prove. Mark each as clean, at risk, or active.',
                             'example': 'Spending power gets checked once this week, below the '
                                        'more-than-three-times-a-day pattern people claim can trigger a '
                                        'review [CardRight — RqEu9gdaauI @ 00:00:58]. No PayPal, Cash App, '
                                        'Square or Venmo transfers run through Amex; family money moves '
                                        'through Amex Send and Split. Stated income matches tax returns. '
                                        'Gift card purchases are marked at risk and paused.'},
                            {'name': 'income_documentation_kit',
                             'type': 'textarea',
                             'prompt': 'Assemble the documents you could submit within the review window: '
                                       'recent bank statements, pay stubs, and tax returns or transcripts. '
                                       'Record where each file lives, how quickly you can produce it, and '
                                       'whether it supports the income you reported.',
                             'example': 'The Amex letter allows 14 days from its date before additional '
                                        'credit actions, up to cancellation [RJ Financial — vfXgcEGNVuM @ '
                                        '00:04:13]. Two-thirds of reviewed cases asked for two months of '
                                        'bank statements or two pay stubs, so both sit in one folder. Last '
                                        "year's tax return is ready too, since refusing it practically "
                                        'guarantees a shutdown.'},
                            {'name': 'same_day_response_protocol',
                             'type': 'text',
                             'prompt': 'Write the step-by-step protocol you will follow the day a '
                                       'financial review notice arrives. Include which phone number you '
                                       'will dial, what you will send, how you will handle numbers that '
                                       'look unfavorable, and when you will request goodwill.',
                             'example': 'Call the same day using the number on the back of the card, not '
                                        'the one in the voicemail, which protects against spoofing [Colin '
                                        'Matthew — xZwOSYlOyVc @ 00:03:29]. Send exactly what is asked and '
                                        'submit even if the numbers are off. After weeks frozen on a card '
                                        'with an $800 or $900 fee, request a goodwill credit.'},
                            {'name': 'points_exposure_and_exit',
                             'type': 'textarea',
                             'prompt': 'Record your current Membership Rewards balance and the redemptions '
                                       'you actually plan to make. Describe when you will transfer points '
                                       'out ahead of any possible shutdown, and how much you are willing '
                                       'to leave exposed if accounts close suddenly.',
                             'example': 'One cardholder lost all nine cards and only kept value because '
                                        '580,000 points were moved out in time [Cal Barton — sVToTQaS_Dw @ '
                                        '00:04:50]. When Amex shuts accounts down, it takes all the '
                                        'points. With 210,000 points on hand, the planned redemptions '
                                        'transfer out now, leaving no more than 30,000 exposed while any '
                                        'review remains possible.'},
                            {'name': 'payment_bank_switch_checklist',
                             'type': 'text',
                             'prompt': 'If you are changing the bank account that pays your cards, list '
                                       'each verification step before the switch. Include routing and '
                                       'account numbers, available balance, confirmation the payment '
                                       'cleared at both banks, and the autopays still tied to the old '
                                       'account.',
                             'example': 'Routing number, account number and available balance get verified '
                                        'before the first payment from the new bank [Cal Barton — '
                                        '3dq0zRBwn8E @ 00:10:02]. The payment is confirmed cleared at both '
                                        'banks, since returned payments are a review trigger. The old '
                                        'account stays open until every autopay, including three card '
                                        'autopays and the phone bill, has moved.'},
                            {'name': 'spark_break_even_math',
                             'type': 'textarea',
                             'prompt': 'Estimate your annual business spend that would run through Spark '
                                       'Cash Plus and calculate the break-even against its annual fee. '
                                       'Compare the net result against a no-fee flat-rate card and note '
                                       'whether you reach the fee refund threshold.',
                             'example': 'Break-even is $7,500 a year to cover the $150 fee, and about '
                                        '$30,000 a year to beat no-fee 1.5% cards, where both net $450 '
                                        '[Ask Sebby Business — x9-GMvg8lPA @ 00:02:10]. Projected spend of '
                                        '$90,000 nets $1,650 after the fee; the fee only refunds once '
                                        'yearly spend reaches $150,000. Inventory, software, and ad spend '
                                        'all route through the card.'},
                            {'name': 'personal_reporting_and_524_check',
                             'type': 'textarea',
                             'prompt': 'Before applying for a Spark product, count your Chase 5/24 slots '
                                       'and list any planned stacking applications. Note how personal '
                                       'credit reporting and the bureau pulls involved would affect those '
                                       'plans and your utilization if a balance reports before payment.',
                             'example': 'Spark pulls all three personal bureaus and its personal reporting '
                                        'adds the card to the 5/24 tally [Just Money Ish — Zu5102EGxLc @ '
                                        '00:03:20]. At 3/24 with an Ink planned, Spark waits. HowToCredit '
                                        'warns a $5,000 charge on a $10,000 line reads as 50% utilization '
                                        'even with the minimum paid, so balances get paid before the '
                                        'statement reports.'},
                            {'name': 'spark_ramp_and_exit_plan',
                             'type': 'textarea',
                             'prompt': 'Describe how you will ramp spend on a new no-preset-limit Spark '
                                       'card over its first two months. Write the exit strategy for the '
                                       'capital you deploy, including how each statement gets cleared and '
                                       'what happens if revenue stalls.',
                             'example': 'Spend ramps over the first month or two instead of dropping 50k '
                                        'in month one, since Capital One scrutinizes early activity '
                                        'against a limit it does not disclose [Ask Sebby Business — '
                                        'x9-GMvg8lPA @ 00:01:34]. The $100,000 TikTok-live case failed '
                                        'without pressure-testing or an exit and sat at roughly 20% '
                                        'interest. Every statement clears from existing revenue.'},
                            {'name': 'miles_conversion_and_banker_relationship',
                             'type': 'textarea',
                             'prompt': 'Decide whether your Spark rewards stay as cash or convert into '
                                       'Capital One miles for partner transfers. Record the redemption you '
                                       'are targeting, its cash value, and how you will use an assigned '
                                       'banker or card controls to protect the account.',
                             'example': 'The two-card setup turned $1,320 of Spark cash back into 132,000 '
                                        'miles, moved as 130,000 Singapore miles for an ~$8,500 JFK to '
                                        'Singapore saver seat [Ask Sebby Business — x9-GMvg8lPA @ '
                                        "00:06:34]. Ryan Maya keeps the banker's cell number for problems "
                                        'and new lines. Single-use virtual cards and per-employee limits '
                                        'keep low spenders carrying less risk.'}],
                 'completion_gate': 'The velocity baseline and ramp schedule are written; every review '
                                    'trigger is marked clean, at risk, or active; the documentation kit '
                                    'can be produced within 14 days; points exposure has a stated ceiling; '
                                    'the Spark break-even and 5/24 count are calculated; and a written '
                                    'exit plan covers every dollar of planned Spark spend.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Net-60 Float & Chase Ink Stack Planner',
                 'purpose': 'Turn the Amex Plum into a deliberate float instrument and build the Chase Ink '
                            'entry rung without wasting a bonus. Every dollar gets one mode, either '
                            'early-pay discount or full 60-day float, every large charge is confirmed '
                            'before it is swiped, and every Ink application clears the 24-month card count '
                            'first.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull your last three statements and mark each statement close date '
                                  'before planning any Plum purchase.',
                                  'Assign every planned Plum dollar to exactly one mode, early-pay '
                                  'discount or full 60-day float, and never mix them.',
                                  'Only buy what cash on hand already covers, because interest after day '
                                  '60 can wipe out the entire trade.',
                                  'Count every card opened in the last 24 months, including '
                                  'authorized-user accounts, before touching a Chase Ink application.',
                                  'Log every office-store gift card purchase the same day, with PIN, '
                                  'balance check, photos, and a non-round total.'],
                 'fields': [{'name': 'plum_float_window_map',
                             'type': 'text',
                             'prompt': 'Map the Plum float window against your statement calendar. Record '
                                       'the statement close date, the purchase date you will target, the '
                                       '60-day payment deadline, and the total days of zero-interest float '
                                       'you expect before any interest begins to accrue on inventory.',
                             'example': 'Statement closes on the 3rd; Q4 inventory is bought that same '
                                        'day, so the charge rides a full cycle plus 60 days. Stephen Smith '
                                        'reads this as roughly 90 days of 0% on inventory [Stephen Smith — '
                                        'zOrHXaEEgxk @ 00:10:51]. Deadline logged on the shared calendar '
                                        'with a reminder set ten days earlier to confirm cash is staged.'},
                            {'name': 'plum_mode_per_dollar',
                             'type': 'textarea',
                             'prompt': 'For each planned Plum charge, choose one mode: pay within 10 days '
                                       'for the 1.5 percent discount, or float the full 60 days. Write the '
                                       'dollar amount assigned to each mode and the reason float beats the '
                                       'discount for that purchase.',
                             'example': '$20,000 of supplier invoices paid early inside the 10-day window '
                                        'to capture 1.5 percent, about $300; $8,000 of Q4 inventory '
                                        'floated the full 60 days because sell-through cash arrives in '
                                        'week seven. Jake Broe equates skipping the discount to roughly an '
                                        '18 percent APR on top of the 250 dollar fee [Jake Broe — '
                                        'UdDb_X5YHDI @ 00:06:47].'},
                            {'name': 'plum_fee_breakeven',
                             'type': 'text',
                             'prompt': 'Calculate your Plum fee breakeven. Enter projected annual '
                                       'early-paid spend, multiply by 1.5 percent, subtract the 250 dollar '
                                       'fee charged from year two, and state whether your realistic volume '
                                       'clears the breakeven line with margin to spare for the coming '
                                       'year.',
                             'example': 'Projected early-paid spend is $48,000, returning $720 at 1.5 '
                                        'percent; minus the $250 fee nets $470. Daniel Shepherd puts '
                                        'breakeven at a little over $16,600 of early-paid spend [Daniel '
                                        'Shepherd — a0APMJagyzA @ 00:02:54], so this volume clears it '
                                        'nearly three times over. Year one fee is waived, so the '
                                        'first-year net is the full $720.'},
                            {'name': 'plum_vs_blue_business_cash',
                             'type': 'textarea',
                             'prompt': 'Compare the always-paid-early Plum against the no-fee Blue '
                                       'Business Cash at your actual annual spend. Show the cash returned '
                                       'by each card net of fees and note the spend level where the Plum '
                                       'finally catches up. Include employee card spend in totals.',
                             'example': 'At $90,000 a year, the Blue Business Cash pays 2% on $50,000 '
                                        '($1,000) plus 1% on $40,000 ($400), totaling $1,400. The Plum '
                                        'pays $1,350 minus $250, netting $1,100. Jake Broe finds both '
                                        'cards return $2,000 only at $150,000 [Jake Broe — UdDb_X5YHDI @ '
                                        '00:11:55], so the Blue Business Cash stays primary below that.'},
                            {'name': 'large_ticket_capacity_check',
                             'type': 'text',
                             'prompt': 'Before any large charge on a no-preset-limit card, record the '
                                       'purchase amount, the date you called the issuer, the '
                                       "representative's confirmation, and a fallback card ready in case "
                                       'the transaction is still declined or flagged for review at '
                                       'checkout.',
                             'example': 'A $14,000 equipment order is planned for the 12th. Called Amex on '
                                        'the 10th and the representative noted the charge for '
                                        "pre-authorization, following Jake Broe's practice of calling "
                                        'ahead on a charge card [Jake Broe — UdDb_X5YHDI @ 00:04:37]. '
                                        'Because purchasing capacity can vary and transactions may still '
                                        'be declined, the Ink Premier sits ready as backup.'},
                            {'name': 'amex_slot_inventory',
                             'type': 'textarea',
                             'prompt': 'List every Amex card you hold across personal and business '
                                       'profiles, tagging each as credit or charge. Count remaining '
                                       'credit-card and charge-card slots and confirm the Plum or any new '
                                       'no-preset-limit card lands in an open slot before you submit the '
                                       'application.',
                             'example': 'Held: Blue Business Plus, Blue Business Cash, and personal Blue '
                                        'Cash Preferred, so three credit-card slots used and one '
                                        'remaining; zero charge cards. Under the rule of four credit cards '
                                        'and up to ten charge cards, the Plum sits in a charge-card slot '
                                        '[u2 credit consulting — UYH3UwJ9oOM @ 00:03:53]. Existing '
                                        'relationship should support a soft-pull-only approval.'},
                            {'name': 'five_24_count',
                             'type': 'text',
                             'prompt': 'Count every card opened in the last 24 months from any issuer, '
                                       'including authorized-user accounts and personally reporting '
                                       'business cards. Enter the total, the date the oldest account falls '
                                       'off, and whether you sit under five before any Chase Ink '
                                       'application.',
                             'example': 'Four accounts in 24 months: two personal cards, one '
                                        'authorized-user card, and a Spark Cash Plus that reports '
                                        'personally and counts toward the tally. The oldest falls off in '
                                        'March, so an Ink application stays possible now while under five '
                                        '[Just Money Ish — 04bDgAQcsYs @ 00:02:03]. Any additional '
                                        'personal card waits until after the Ink approval.'},
                            {'name': 'ink_bonus_card_choice',
                             'type': 'textarea',
                             'prompt': 'Decide whether the Ink Cash or Ink Unlimited earns your welcome '
                                       'bonus, since only one pays. Record the current offer, required '
                                       "spend and window, your planned spend sources, and why that card's "
                                       'earning structure fits your business better than the other.',
                             'example': 'Choosing the Ink Cash for the 100,000-point offer on $8,000 in 4 '
                                        'months, because phone, internet and office-supply spend fills the '
                                        '5x bucket. Chase pays the welcome bonus on only one of the two '
                                        'cards [Miles with Mary - Points & Miles Travel — z45WdojPWE8 @ '
                                        '00:07:21]. Spend sources: quarterly software renewals, phone '
                                        'autopay, and a planned printer purchase.'},
                            {'name': 'ink_cash_5x_plan',
                             'type': 'textarea',
                             'prompt': 'Plan your Ink Cash 5x spend against the $25,000 annual cap. List '
                                       'monthly phone and internet bills, office-supply store purchases, '
                                       'and any fee-free gift cards, then project the points earned toward '
                                       'the 125,000-point ceiling for the year and note the remaining gap.',
                             'example': 'Phone and internet autopay run $310 a month, about $3,720 a year. '
                                        'Office-store purchases add $1,200 in one month for 6,000 points, '
                                        'matching the Staples or Office Depot result [Leen on Travel — '
                                        'zK3uQ4upb_4 @ 00:00:43]. Adding printer and supply purchases, '
                                        'projected total is $9,000 at 5x, or 45,000 points, leaving '
                                        '$16,000 of cap for later quarters.'},
                            {'name': 'gift_card_hygiene_log',
                             'type': 'textarea',
                             'prompt': 'Log every office-store gift card purchase with date, store, card '
                                       'amount, PIN set, balance verified, and receipt photographed. '
                                       'Confirm the order total does not end in 000 and the gift card mall '
                                       'address was typed fully into the browser bar every single time.',
                             'example': 'March 6, Staples: two $200 Visa gift cards plus a pack of gum, '
                                        'bringing the total to $401.89 so it never ends in 000 [Leen on '
                                        'Travel — zK3uQ4upb_4 @ 00:01:15]. PINs set, balances verified, '
                                        'both sides photographed, receipt saved, since a past claim '
                                        'replacement took about six weeks. Address typed fully, not '
                                        'clicked.'}],
                 'completion_gate': 'Do not place a single Plum or Ink charge until every planned dollar '
                                    'has one assigned mode, the 60-day deadline is calendared with cash '
                                    'already on hand, large tickets are pre-cleared with the issuer, and '
                                    'the 24-month card count sits under five.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Business Gold Bonus Engine & Portal Stack Ledger',
                 'purpose': 'Capture the largest available Business Gold offer, land the minimum spend on '
                            'real expenses, route 4x categories correctly, and layer portal cashback, '
                            'card-linked offers, and card earn on one checkout with tracking evidence '
                            'saved for every order.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Check the offer through a private window, VPN browser, and the '
                                  'pre-approval tool before accepting anything below the top figure.',
                                  'Schedule big real expenses into the three-month window so minimum spend '
                                  'lands naturally without a tax payment crossing the line.',
                                  'Confirm the merchant type qualifies for 4x before routing spend, and '
                                  'verify each credit is live before counting it.',
                                  'Set the Rakuten payout currency before each quarterly date and confirm '
                                  'your status before choosing Bilt.',
                                  'Disable ad blockers, use only portal-listed codes, and screenshot every '
                                  'confirmation page before closing the browser tab.'],
                 'fields': [{'name': 'bg_offer_hunt',
                             'type': 'text',
                             'prompt': 'Record the Business Gold offer you will accept. Note the figure '
                                       'shown publicly, the figure surfaced through private browsing, VPN '
                                       'browsers, or the pre-approval tool, and whether the offer carries '
                                       'lifetime language that blocks a second bonus on this product '
                                       'later.',
                             'example': 'The public offer showed 100,000 points. Loading a referral link '
                                        "in Opera's private browser with the built-in VPN surfaced 200,000 "
                                        '[Phillip Pak — Ye64oVq2FgU @ 00:00:39], and the pre-approval tool '
                                        'confirmed the targeted amount before applying. Terms show no '
                                        "lifetime language. Following Phillip Pak's rule, nothing under "
                                        '200,000 gets accepted on this card.'},
                            {'name': 'bg_minimum_spend_timing',
                             'type': 'textarea',
                             'prompt': 'Map how the $15,000 minimum spend in three months will land '
                                       'naturally. List each large expense, its expected date and amount, '
                                       'and confirm that a tax payment is never the purchase that crosses '
                                       'the threshold. If spend is low, record the expense you will wait '
                                       'for.',
                             'example': 'Application waits until the roof repair is quoted, so the $15,000 '
                                        'lands naturally [The Rewards Master — qjuRrg-ROGg @ 00:02:50]. '
                                        'Month one: $9,200 roof repair. Month two: $4,100 software and '
                                        'advertising. Month three: $1,900 supplies push spend past the '
                                        'threshold. The quarterly tax payment posts in month two, never as '
                                        'the crossing purchase.'},
                            {'name': 'tax_payment_net_return',
                             'type': 'text',
                             'prompt': 'If you route a tax payment toward the bonus, record the bill '
                                       'amount, the processing fee percentage, the bonus return '
                                       'percentage, and the net return after fees, so the real yield is '
                                       'visible before you pay. Note which processor you will use.',
                             'example': 'A $7,000 estimated tax bill goes on the Business Gold toward the '
                                        'bonus. The bonus return works out to 30 percent, minus a 3 '
                                        'percent processing fee, for a 27 percent net return [Spencer '
                                        'Johnson — Fk75okyk2W4 @ 00:07:28]. Processing fee of $210 is '
                                        'logged as a cost, and the payment is scheduled mid-window.'},
                            {'name': 'four_x_category_routing',
                             'type': 'textarea',
                             'prompt': 'Identify the top two Business Gold categories your spend will hit '
                                       'each cycle. Confirm merchant types qualify, noting gas exclusions '
                                       'at supermarkets, superstores and warehouse clubs, and track '
                                       'cumulative 4x spend against the $150,000 calendar-year cap, '
                                       'including all employee card spend.',
                             'example': 'Top two categories are software and advertising. Website hosting '
                                        'moved off the Blue Business Plus at 2x after Points with Phillip '
                                        'described the same mistake [Points with Phillip — nZSZ4gP-QwI @ '
                                        '00:02:04]. Fuel at a warehouse club is excluded, so it goes '
                                        'elsewhere. Year-to-date 4x spend sits at $41,000 against the '
                                        '$150,000 cap.'},
                            {'name': 'monthly_credit_harvest',
                             'type': 'text',
                             'prompt': 'Plan how the $20 monthly credit will be captured without opening '
                                       'new subscriptions. Name the merchant, the exact purchase, and the '
                                       'method, then calculate the effective annual fee after twelve '
                                       'months of successful credit capture. Confirm the credit is live on '
                                       'the account first.',
                             'example': 'Each month a $20 Amazon gift card is bought on Staples.com, not '
                                        'Office Depot.com, which runs through a third party [Leen on '
                                        'Travel — TvJBiMpMRhw @ 00:01:33]. Twelve months of $20 equals '
                                        '$240, bringing the $375 fee down to $135. Credit confirmed live '
                                        'on the account dashboard before the first purchase was counted.'},
                            {'name': 'keep_or_cancel_test',
                             'type': 'textarea',
                             'prompt': 'Decide whether the Business Gold earns its keep after year one. '
                                       'Compare annual 4x points earned on real spend against what the '
                                       'Blue Business Plus would earn on the same spend, then net the '
                                       'effective fee. Record the keep or cancel verdict and date.',
                             'example': 'Real 4x spend runs $12,000 a year, earning 48,000 points versus '
                                        '24,000 on the Blue Business Plus at 2x. The extra 24,000 points '
                                        'must beat a $135 effective fee. Daniel Shepherd warns the card '
                                        'loses when 4x spend is low, so look at actual spending [Daniel '
                                        'Shepherd — 9mXtEwhakHo @ 00:15:00]. Verdict: keep, reviewed every '
                                        'renewal.'},
                            {'name': 'rakuten_payout_currency',
                             'type': 'text',
                             'prompt': 'Record your Rakuten payout currency before each quarterly payout '
                                       'date in February, May, August and November. Note whether you hold '
                                       'an MR-earning card, the conversion rate you will receive, and your '
                                       'Bilt status if routing there. Each payout is cash or points, not '
                                       'both.',
                             'example': 'Payout set to Amex Membership Rewards at $1 equals 100 points, '
                                        'confirmed because the Blue Business Plus earns MR [Points Rookie '
                                        '— lfbv6SuAgRE @ 00:05:10]. Bilt was rejected for now: without '
                                        'Silver status the account converts at 2:1, a 50% cut. Currency is '
                                        'rechecked one week before each payout date, next on February 15.'},
                            {'name': 'four_layer_stack_build',
                             'type': 'textarea',
                             'prompt': 'Build one checkout stack layer by layer: sale price or '
                                       'Rakuten-listed code, portal cashback rate, card-linked offer, and '
                                       'card earn rate. Show the dollar value of each layer and the final '
                                       'net cost of the order and the percentage saved.',
                             'example': 'A $200 Nike order: 15% code drops it to $170, Rakuten 10% returns '
                                        '$17, a 5% card offer returns $8.50, and 2% card cashback layers '
                                        'on top, netting $141.10, nearly 30% saved [Everyday Money Heroes '
                                        '— HbZGYalSsyc @ 00:19:01]. Only the code Rakuten displays was '
                                        'used, so the multiplier stayed valid and the confirmation was '
                                        'screenshotted.'},
                            {'name': 'tracking_evidence_log',
                             'type': 'textarea',
                             'prompt': 'For every portal purchase, record the date, merchant, order total, '
                                       'expected cashback, browser setup used, and screenshot location. '
                                       'Note whether ad blockers were disabled, and log the claim filing '
                                       'date if the purchase failed to track within the posting window.',
                             'example': 'October 3, tire shop order of $1,054, expected cashback logged. '
                                        'Ad blocker disabled and a private window used, confirmation '
                                        'screenshotted to the receipts folder [Money with Andrey — '
                                        'E-FSl936NIg @ 00:07:05]. Nothing tracked after the posting '
                                        'period, so a claim was filed with the screenshot, since '
                                        'non-tracking is the most common complaint.'},
                            {'name': 'portal_focus_and_bank_offers',
                             'type': 'textarea',
                             'prompt': 'Choose the one to three portals you will concentrate funds in and '
                                       'list the high-yield offer types you will chase, such as '
                                       'subscription and bank-bonus offers. Record expected quarterly '
                                       'points and offers you will deliberately skip because they earn '
                                       'nothing.',
                             'example': 'Portals limited to Rakuten plus Capital One Shopping in a '
                                        "separate browser, following KaungFi's advice to focus on one or "
                                        'two, maybe three at most [KaungFi — R-TCKAPsObw @ 00:07:54]. '
                                        'Priority goes to 80-100% cashback subscriptions and bank offers, '
                                        'which made up 58% of roughly 405k points in one two-player setup. '
                                        'Newegg gift cards are skipped, since they earn nothing.'}],
                 'completion_gate': 'Do not apply or check out until the accepted offer is the top figure '
                                    'found, minimum spend maps to real expenses with no tax payment '
                                    'crossing the line, every 4x merchant and credit is verified, and each '
                                    'portal order has a saved screenshot.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Shopping Offers, Transfer Hurdles & Wallet Fee Math',
                 'purpose': 'Harvest Capital One Shopping targeted offers and the referral bonus without '
                            'tracking failures, move points only when a priced award clears the hurdle '
                            'rate, and build a pay-in-full wallet whose premium fees are justified by '
                            'credits that replace real spending.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Screenshot every targeted offer with amount, expiration, and current '
                                  'date before activating it, and file requests after 30 days.',
                                  'Run competing shopping extensions in separate browsers and complete a '
                                  'small test purchase before any large order.',
                                  'Price each award in partner miles and in bank-portal points, then '
                                  'transfer only when the hurdle rate clears.',
                                  'Count only premium card credits that replace spending you already make, '
                                  'and subtract the full annual fee.',
                                  'Calendar every 0% expiry and issuer rule change, and confirm the full '
                                  'balance is cleared before each window closes.'],
                 'fields': [{'name': 'cos_referral_bonus_checklist',
                             'type': 'text',
                             'prompt': 'Track the Capital One Shopping $80 referral bonus requirements. '
                                       'Record the referral link used, install date, confirmation the '
                                       'device never had the extension, the qualifying purchase amount and '
                                       'date, and the expected posting window for the credit. Keep the '
                                       'extension installed throughout.',
                             'example': 'Signed up through a referral link and installed within seven days '
                                        'on a laptop that never had the extension; $12 spent at a '
                                        'qualifying store within 30 days and the extension stays installed '
                                        "[Eli — L5V4-qjpKSw @ 00:01:59]. Nate Bind's $80 posted roughly 90 "
                                        'days after a $1 purchase, so the calendar reminder sits at day '
                                        '95.'},
                            {'name': 'targeted_offer_hunt',
                             'type': 'textarea',
                             'prompt': 'Describe your routine for surfacing targeted Capital One Shopping '
                                       'offers. Note merchants browsed inside the portal, logout and '
                                       "return timing, marketing email settings, and each offer's amount, "
                                       'spend requirement, and expiration, with screenshots and the '
                                       'current date captured before activating anything.',
                             'example': 'Browsed GNC, Vitamin Shop and Lucky Vitamin protein listings '
                                        'inside the portal, logged out, and returned two to three days '
                                        'later to a $45 back on $75 offer [Michael Martinez — CDTjD80PdZk '
                                        '@ 00:09:30]. Marketing emails switched on, since emailed offers '
                                        'run higher. Screenshot shows amount, expiration and current date '
                                        'before activation.'},
                            {'name': 'extension_conflict_and_test',
                             'type': 'text',
                             'prompt': 'Record how you prevent extension conflicts and confirm tracking. '
                                       'Note which browser runs Capital One Shopping, which runs Rakuten, '
                                       'whether ad blockers are removed, and the small test purchase '
                                       'completed before any large order at that store. Never edit orders '
                                       'after checkout.',
                             'example': 'Capital One Shopping runs in Chrome with no other extensions; '
                                        'Rakuten runs in a separate browser so the two never void each '
                                        'other [Michael Martinez — CDTjD80PdZk @ 00:12:44]. A $14 test '
                                        'order at the target store tracked before the $600 order went '
                                        'through. Orders are never tweaked after checkout, since edits '
                                        'risk the transaction not counting.'},
                            {'name': 'offer_terms_and_payout_plan',
                             'type': 'textarea',
                             'prompt': "Read every targeted offer's terms for excluded items before "
                                       'purchasing, and plan how gift-card-only payouts will be used. '
                                       'Record exclusions found, the reward request deadline at 30 days, '
                                       'and the gift card you intend to redeem toward with expected payout '
                                       'timing.',
                             'example': 'Electronics offer terms exclude Apple products, so the order was '
                                        'built around other brands [Twin Finances — OxMh5dpHvJk @ '
                                        '00:03:13]. Reward request goes in at day 31 with screenshots if '
                                        'nothing posts. Because payouts come only as gift cards after one '
                                        'to three months, the balance is building toward a large Marriott '
                                        'gift card for a hotel stay.'},
                            {'name': 'transfer_hurdle_calc',
                             'type': 'text',
                             'prompt': 'Before transferring any points, price the award in partner miles '
                                       'and in bank-portal points. Divide the all-in cash price by points '
                                       'required to get cents per point and compare against your personal '
                                       'hurdle rate, remembering transfers are irreversible.',
                             'example': 'Christmas Eve at the Grand Hyatt Vail costs 35,000 points against '
                                        'a $773 all-in cash price. Dividing $773 by 35,000 gives 2.2 cents '
                                        'per point, clearing a 2-cent hurdle rate [AskSebby — Uvyem-_QFhI '
                                        '@ 00:09:00]. Bank-portal price checked first and came in far '
                                        'higher, so the transfer is approved only once award space is '
                                        'confirmed.'},
                            {'name': 'transfer_bonus_watch',
                             'type': 'textarea',
                             'prompt': 'List active or expected transfer bonuses for your points '
                                       'currencies. For each, record the partner, bonus percentage, end '
                                       'date, baseline cents-per-point value, boosted value after the '
                                       'bonus, and whether an actual redemption exists to justify moving '
                                       'points before the deadline passes.',
                             'example': 'Chase to IHG at an 80 percent bonus, ending December 3, lifts an '
                                        'average IHG valuation from 0.6 cents to 1.08 cents per Chase '
                                        'point [Ben Hedges — 3sY2v2Stv7c @ 00:01:36]. A two-night stay is '
                                        'priced and matched to the boosted rate. ANA award space is '
                                        'monitored through seats.aero alerts before any airline transfer.'},
                            {'name': 'catch_all_wallet_architecture',
                             'type': 'textarea',
                             'prompt': 'Design your wallet around one 2x or 2 percent catch-all card '
                                       'wrapped by category specialists. Name each card, the spend it '
                                       'captures, its earn rate, and your estimated blended return across '
                                       'total annual spend on a pay-in-full basis.',
                             'example': 'Catch-all is the Blue Business Plus at 2x for uncategorized '
                                        'spend, with Business Gold handling software and advertising, Ink '
                                        'Cash covering phone and internet, and Blue Cash Preferred taking '
                                        'groceries. Rob Berger shows a three-card system landing close to '
                                        '3 percent on average [Rob Berger — 4pWev9D_0yQ @ 00:08:01]. Every '
                                        'statement is paid in full.'},
                            {'name': 'premium_fee_credit_capture',
                             'type': 'textarea',
                             'prompt': 'Run the premium card fee test. List each annual credit, the dollar '
                                       'amount you will actually use, and whether it replaces spending you '
                                       'already make, then subtract the annual fee to show your true net '
                                       'value for the year.',
                             'example': 'Gold credits listed total $524 against a $325 fee. Using every '
                                        'credit nets +$199, but capturing only dining and Uber lands at '
                                        "-$85 [Leo's Travel Hacks — 4uIEMf5mkHg @ 00:08:15]. Only credits "
                                        'replacing existing spend are counted, which pushed a light '
                                        'Platinum user to -$715 against the $895 fee [Card & Capital — '
                                        '-JFBxMqq458 @ 00:07:27]. Verdict: Gold kept, Platinum declined.'},
                            {'name': 'zero_apr_float_exit',
                             'type': 'textarea',
                             'prompt': 'Map every 0% APR window you will use for float. Record the card, '
                                       'balance, intro expiry date, where idle cash is parked and at what '
                                       'yield, any tax set-aside, and the date the full balance will be '
                                       'cleared.',
                             'example': 'Blue Business Plus 0% window holds $12,282.88 of spend, with '
                                        'matching cash parked at 4.5% APY. The targeted 25k MR offer plus '
                                        'interest produced $926.66 profit, or $861.34 after a 15% tax '
                                        'set-aside [Fat Stacks Academy — 9JkcZCA1q_M @ 00:10:31]. Full '
                                        'payoff is scheduled one month before expiry, since an 18 to 25 '
                                        'percent APR wipes out rewards.'},
                            {'name': 'rule_change_and_grocery_crossover',
                             'type': 'textarea',
                             'prompt': 'Record issuer rule changes and spend crossovers that alter your '
                                       'wallet. Note the Platinum hotel credit two-night minimum, your '
                                       'monthly supermarket spend against the Blue Cash Preferred '
                                       'crossover, and the adjustments you will make before each change '
                                       'takes effect.',
                             'example': 'If held, Platinum hotel credit plans are rebuilt around the '
                                        'two-night minimum confirmed for January 1, 2027 [Ben Hedges — '
                                        '1K72JHTnPlw @ 00:03:14], so two-night stays are booked together. '
                                        'Supermarket spend averages $410 a month, above the roughly $264 '
                                        'crossover where the $95 Blue Cash Preferred at 6% overtakes the '
                                        'no-fee Blue Cash Everyday. Preferred stays.'}],
                 'completion_gate': 'Do not activate an offer, transfer a point, or renew a premium card '
                                    'until screenshots are saved, the award clears your hurdle rate in '
                                    'both pricing views, credits are counted only against existing spend, '
                                    'and every 0% balance has a dated payoff.'}]}
