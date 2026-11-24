from __future__ import annotations

def build_volume_032_workbook() -> dict:
    return {'workbook_id': 'wb-032-payment-processing-and-atm-arbitrage',
 'volume_id': 'vol-032-payment-processing-and-atm-arbitrage',
 'title': 'ISO Payment Processing & ATM Arbitrage — Practitioner Testimony Operator Workbook',
 'subtitle': 'Field Worksheets for Card Processing Economics, Interchange Optimization, Fee Pass-Through '
             'Compliance, and Residual Protection',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Merchant Economics, Pricing Models, and Statement Diagnosis',
                 'purpose': 'Turn a single merchant statement into a verified picture of fees, card costs, '
                            'processor markup, and agent residual. This worksheet anchors every later '
                            'decision in the fee-splitting mechanics of card acceptance, the Durbin debit '
                            'cap, and the effective rate that lets any pricing model be compared.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Gather at least the most recent full monthly statement and confirm '
                                  'total card volume, total fees, and the pricing model printed on it.',
                                  'Work the fields in order, because the gross profit and split math in '
                                  'the early fields feed the markup and conversion decisions later.',
                                  'Calculate the effective rate before forming any opinion about the '
                                  'pricing model; it is the only undisputed yardstick for comparing '
                                  'providers.',
                                  'Pull the average ticket and card-present versus card-not-present mix '
                                  'before quoting, since small tickets and keyed volume change the '
                                  'economics.',
                                  'Record every past-due gateway balance and coding issue as an action '
                                  'item with a date, not a note to revisit later.'],
                 'fields': [{'name': 'merchant_profile_volume',
                             'type': 'text',
                             'prompt': "Record the merchant's business type, monthly card volume, and "
                                       'current all-in fee percentage, then calculate total monthly fees '
                                       'the way Mario frames the cafe example so every later field in this '
                                       'worksheet starts from one verified dollar figure.',
                             'example': 'Cafe processing $20,000 per month at 2.80% all-in pays $560 in '
                                        'monthly fees. Card costs at 1.40% take $280, leaving $280 gross '
                                        'profit to split between agent and partner. Mario uses exactly '
                                        'this baseline to show how one ordinary storefront becomes '
                                        'recurring income [Residual Builders — lubvPaxm55o @ 00:04:25]. '
                                        'Volume confirmed from the last three statements before any split '
                                        'math.'},
                            {'name': 'residual_split_projection',
                             'type': 'textarea',
                             'prompt': 'Apply your agreed split to the gross profit from the previous '
                                       'field and project the monthly, annual, and ten-year residual. Note '
                                       'who receives the remaining share and whether the split percentage '
                                       'is written into your signed agreement.',
                             'example': 'At an 80/20 split, 80% of the $280 gross profit pays $224 per '
                                        'month, $2,688 per year, and $26,880 across ten years, while the '
                                        'ISO or processor partner keeps the 20% balance [Residual Builders '
                                        '— lubvPaxm55o @ 00:04:25]. One cafe at this size equals a steady '
                                        'monthly payment that compounds as more accounts board.'},
                            {'name': 'iso_vs_direct_role',
                             'type': 'textarea',
                             'prompt': 'Describe which role you will play in the payment chain: agent '
                                       'selling through an ISO, or a party moving funds directly. List '
                                       'which functions the ISO supplies, such as terminals, onboarding, '
                                       'and support, so your sales focus stays clear.',
                             'example': 'Role chosen: agent under an ISO. Joe Wagner says that unless you '
                                        'want responsibility for moving the money and following strict '
                                        'regulations, selling through an ISO is how to succeed [Joe Wagner '
                                        '| Merchant Services & Passive Income — 6dCPtuCCcvw @ 00:01:01]. '
                                        'The ISO handles terminals, onboarding, and merchant support, so '
                                        'my week goes to selling, not settlement.'},
                            {'name': 'pricing_model_audit',
                             'type': 'text',
                             'prompt': "Identify the merchant's current pricing model as flat-rate, "
                                       'tiered, interchange-plus, or subscription, and state the processor '
                                       'markup over interchange. If tiered or flat on a debit-heavy '
                                       'account, note the conversion target and the markup you will quote.',
                             'example': 'Current model: tiered, with no fee review in years, which Joe '
                                        'Wagner says almost always means overpaying and a prime switch '
                                        'target [Joe Wagner | Merchant Services & Passive Income — '
                                        'XXH81AbZQcg @ 00:01:11]. Conversion target: interchange plus '
                                        '0.25%, the rate Shepherd boards every new client on so Durbin '
                                        'cost drops pass through automatically [durbinamendment — '
                                        '_5A2a4Vu7A8 @ 00:09:27].'},
                            {'name': 'average_ticket_durbin_check',
                             'type': 'text',
                             'prompt': "Pull the merchant's average ticket before discussing debit costs. "
                                       'State whether it sits under $10, where the 22-cent regulated '
                                       'per-item fee raises costs, or around $30 and above, where the '
                                       'Durbin cap actually saves the merchant money.',
                             'example': 'Average ticket: $8.40 at a coffee counter, below the $10 line '
                                        'where the 22-cent per-item fee raises costs [Transaction Expert — '
                                        'cL-wn0WX_PA @ 00:02:41]. The regulated cap is 0.05% plus 21 cents '
                                        'plus one cent for fraud protection, applying only to issuers with '
                                        '$10 billion or more in assets [All Things Money — F87ku5Df-mA @ '
                                        '00:01:01].'},
                            {'name': 'debit_cap_exposure',
                             'type': 'textarea',
                             'prompt': 'Assess how the proposed Fed cut to the debit cap changes your '
                                       'pitch to debit-heavy merchants. Note the current and proposed cap '
                                       'figures, and record whether the processor contract would pass any '
                                       'savings through without your intervention.',
                             'example': 'Kevin Von Holten flags a proposed cut from 21 cents to 14.4 '
                                        'cents, a 31% revenue hit for banks already over $10 billion '
                                        '[Cornerstone Advisors — FwB1KshUr5A @ 00:01:15]. Merchant sits on '
                                        'a flat-rate contract, and a processor holding flat rate will not '
                                        'hand over the windfall on its own [durbinamendment — _5A2a4Vu7A8 '
                                        '@ 00:10:36]. Conversion required.'},
                            {'name': 'effective_rate_calc',
                             'type': 'text',
                             'prompt': 'Calculate the interchange effective rate by dividing total '
                                       'interchange by total volume, then the markup effective rate by '
                                       'subtracting interchange from total fees and dividing by volume. '
                                       'Flag any interchange-plus statement that omits a total interchange '
                                       'figure.',
                             'example': 'Interchange divided by volume lands at 1.7%, inside the 1.6% to '
                                        '1.8% band CCSalesPro calls about right [CCSalesPro — 2Sn4XMqpW4I '
                                        '@ 00:01:46]. Total fees minus interchange leaves a 0.9% markup on '
                                        '$30,000 monthly volume, above the roughly 0.7% threshold that '
                                        'signals a savings opportunity at this size [CCSalesPro — '
                                        '2Sn4XMqpW4I @ 00:06:40].'},
                            {'name': 'tier_card_mix',
                             'type': 'textarea',
                             'prompt': 'For tiered statements, record the share of transactions landing in '
                                       'qualified, mid-qualified, and non-qualified buckets before '
                                       'comparing any rates. Note whether the merchant is a physical '
                                       'location and whether the qualified share meets the expected '
                                       'storefront benchmark.',
                             'example': 'Physical retail store showing only 41% qualified, with the rest '
                                        'piled into mid- and non-qualified buckets. CCSalesPro expects 60 '
                                        'to 70% qualified for a storefront, with the remainder split '
                                        'fairly evenly [CCSalesPro — RxgrRsVThx4 @ 00:02:54]. The buckets '
                                        "are stacked against this merchant, matching Merchant Maverick's "
                                        'view that tiered is the least transparent model [Merchant '
                                        'Maverick — h72ua8pD9cU @ 00:16:08].'},
                            {'name': 'coding_and_entry_mode',
                             'type': 'text',
                             'prompt': "Verify the merchant's SIC or MCC code and confirm how much volume "
                                       'is card-present versus card-not-present. Record the rate band each '
                                       'channel should fall into and any keyed or virtual-terminal volume '
                                       'pricing higher than it should.',
                             'example': 'MCC verified against the business type; miscoding would mean '
                                        'paying higher rates than the merchant qualifies for [BancardSales '
                                        '— nLfsn6tUZh4 @ 00:06:37]. Split: 85% card-present, expected near '
                                        '1.25% to 2%; 15% keyed through a virtual terminal, expected near '
                                        '2% to 3.5% because of bank risk [BancardSales — nLfsn6tUZh4 @ '
                                        '00:04:44].'},
                            {'name': 'gateway_and_opening_plan',
                             'type': 'textarea',
                             'prompt': 'Record any past-due gateway balances tied to the account and your '
                                       'plan to clear them, then write the opening line you will use, '
                                       'including a free cost analysis offer that gives you a reason to '
                                       'request the statement.',
                             'example': 'One merchant is past due on gateway billing; resolving it this '
                                        'week, since NMI moves past-due accounts to delinquent and debits '
                                        'uncollected fees from the affiliate account after 6 months [NMI — '
                                        'WxBDVPgeUYI @ 00:01:43]. Opening: free cost analysis, because '
                                        'anyone without one in 12 months may be funding a Durbin windfall '
                                        '[Transaction Expert — cL-wn0WX_PA @ 00:04:53].'}],
                 'completion_gate': "Worksheet 1 is complete when the merchant's effective rate, markup "
                                    'effective rate, average ticket, and pricing model are recorded; the '
                                    'projected agent residual is written out monthly and annually; any '
                                    'flat-rate or tiered debit-heavy account has an interchange-plus '
                                    'conversion target; and no past-due gateway balance remains '
                                    'unresolved.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Interchange Optimization and Cash Discount Program Design',
                 'purpose': 'Find the savings hidden inside interchange itself and decide whether a cash '
                            'discount or dual pricing program fits the merchant. The fields walk through '
                            'commercial card mix, downgrades, Visa CEDP status, honest line-item data, '
                            'average-ticket modeling, point-of-sale capability, and the words used to '
                            'present and close the program.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Confirm the share of business, corporate, purchasing, and government '
                                  'cards before promising any Level 2 or Level 3 savings.',
                                  'Force daily auto-batching and confirm CEDP verified status before '
                                  'modeling optimization savings on paper.',
                                  'Reject any setup that relies on auto-filled or randomized line-item '
                                  'data, regardless of the savings it appears to produce.',
                                  'Model the average ticket and card mix before choosing between a '
                                  'percentage service fee and a per-item fee.',
                                  'Rehearse the presentation script aloud and stop explaining once the '
                                  'application is being filled out.'],
                 'fields': [{'name': 'interchange_share_baseline',
                             'type': 'text',
                             'prompt': "Estimate how much of the merchant's total card fees is interchange "
                                       'rather than processor markup, and state where the realistic '
                                       'savings pool sits. Use this split to decide whether to lead with '
                                       'markup reduction or interchange optimization.',
                             'example': 'Sean Jones puts interchange at 75 to 90 percent of card fees, '
                                        'spread across more than 400 rates [Sean Jones Revolution Payments '
                                        '— vVvGM8Rlor8 @ 00:00:15]. On this B2B distributor, interchange '
                                        'is about 84% of fees, so the lead is optimization, matching '
                                        "Jeremy Layton's view that interchange drives 80 to 90 percent of "
                                        'delivered savings.'},
                            {'name': 'commercial_card_mix',
                             'type': 'textarea',
                             'prompt': 'List the share of volume on business, corporate, purchasing, and '
                                       'government cards, since only those benefit from enhanced data. '
                                       'Note any cards carrying personal liability and the portion of B2B '
                                       'transactions expected not to qualify at all.',
                             'example': 'Commercial card volume is 62% of sales, mostly purchasing and '
                                        'corporate cards from contractors. CCSalesPro warns thirty percent '
                                        'of B2B transactions do not qualify and cards carrying personal '
                                        'liability are excluded [CCSalesPro — tG2nIK3Th4Q @ 00:10:18], so '
                                        'the model assumes only about 43% of total volume earns the lower '
                                        'rate after those exclusions.'},
                            {'name': 'downgrade_and_batch_review',
                             'type': 'textarea',
                             'prompt': 'Scan the statement for standard and EIRF downgrades and record the '
                                       "account's batching schedule. If batching is not daily, document "
                                       'the downgrade cost and the change you will force before modeling '
                                       'any optimization savings for the merchant.',
                             'example': 'Auto shop batching weekly to dodge a 25-cent batch fee. '
                                        'CCSalesPro documented that this habit downgraded 80% of a similar '
                                        "shop's tickets and cost about $1,000 a month [CCSalesPro — "
                                        'mqEQN-xgAAk @ 00:04:03]. Daily auto-batching gets switched on '
                                        'first, and savings get modeled only after a clean month of '
                                        'statements without EIRF hits.'},
                            {'name': 'cedp_status',
                             'type': 'text',
                             'prompt': "Confirm the merchant's Visa CEDP verification status and whether "
                                       'the gateway still sends Level 2-only data on Visa commercial '
                                       'cards. Record the participation fee exposure and whether Product 3 '
                                       'rates can be quoted on this account.',
                             'example': 'Status: not yet verified, so no Level 3 rate regardless of what '
                                        'gets sent [PayTrace — 5z1bCzU6Luw @ 00:26:40]. The gateway still '
                                        'pushes Level 2-only data on Visa commercial cards, which can '
                                        'trigger the 0.05% participation fee with no rate benefit '
                                        '[TouchSuite — mFDxx7C-_EA @ 00:00:40]. Level 2-only submissions '
                                        'shut off pending verification.'},
                            {'name': 'line_item_integrity',
                             'type': 'textarea',
                             'prompt': 'Describe how real line-item data will reach the gateway for each '
                                       'enhanced-data transaction. State whether any auto-filled or '
                                       'randomized data is currently being inserted, and record the fix '
                                       'you will require before quoting Level 3 savings.',
                             'example': 'Current gateway inserts generic placeholder line items on every '
                                        'invoice. Jeremy Layton reports gateways inserting fake data and '
                                        'warns of big problems when they get caught [CCSalesPro — '
                                        'KlaksrooZhw @ 00:22:09]. Fix required: invoices pass real product '
                                        "descriptions, quantities, and amounts from the merchant's billing "
                                        'system before any Level 3 savings appear in the proposal.'},
                            {'name': 'savings_case_math',
                             'type': 'textarea',
                             'prompt': "Build the savings case in the merchant's own terms. Show the "
                                       'spread between current Visa commercial rates and enhanced-data '
                                       'rates, then translate the integration effort into payroll cost '
                                       'against annual savings so the decision reads as simple arithmetic.',
                             'example': 'Visa commercial cards drop from 2.5 to 3 percent down to 1.75 '
                                        'percent with full data, a 75 to 120 basis point spread [PayTrace '
                                        '— 5z1bCzU6Luw @ 00:20:53]. Integration pitch: three weeks of '
                                        'developer time, about $8,000 in payroll, against $70,000 a year '
                                        'in savings [CCSalesPro — tG2nIK3Th4Q @ 00:18:33].'},
                            {'name': 'cash_discount_fit',
                             'type': 'text',
                             'prompt': "Record the merchant's average ticket and decide whether a "
                                       'percentage service fee or a per-item fee fits the program. Note '
                                       'whether the ticket falls inside the residual sweet spot or low '
                                       'enough that fixed debit costs push the fee underwater.',
                             'example': 'Average ticket $6 at a bagel shop, far below the $25 to $70 sweet '
                                        'spot [CCSalesPro — AnhJYbY3ptw @ 00:01:30]. Signature debit runs '
                                        'about 30 to 32 cents all-in, roughly 6.4% on a $5 sale '
                                        '[CCSalesPro — AnhJYbY3ptw @ 00:02:07], so the program uses a '
                                        '59-cent per-item fee instead of a 3.99% service fee.'},
                            {'name': 'pos_capability_and_display',
                             'type': 'textarea',
                             'prompt': "Confirm the merchant's point of sale can actually pass the fee to "
                                       'customers and display the card price correctly. Record the POS '
                                       'brand, how cash and card prices appear at checkout, and any setup '
                                       'that would amount to a disguised surcharge.',
                             'example': 'Merchant runs Square, which cannot pass the fee, leaving about '
                                        '$900 a month in fees on $30,000 in sales [Chad The POS Guy — '
                                        'pNxf7ZuEt5w @ 00:00:48]. Migration required. On the new system '
                                        'the credit price is displayed, because posting only the cash '
                                        'price and charging more at checkout is just another surcharge '
                                        '[FTx POS — YyYXmSsR5as @ 00:01:56].'},
                            {'name': 'price_presentation_script',
                             'type': 'textarea',
                             'prompt': 'Write the exact words you will use to present the program, '
                                       'including the everyday comparison you will open with, one worked '
                                       'register example, and the annualized savings figure. Keep the '
                                       'script short enough to deliver without inviting extra rebuttals.',
                             'example': 'Open with the gas pump: cash price, card price, customer chooses. '
                                        'Register example: a $17.66 cash cheeseburger rings $18.37 on card '
                                        '[PaymentCloud — xRGCXR9kPug @ 00:01:13]. Close on annual figures: '
                                        'saving $500 a month becomes six thousand dollars a year [Joe '
                                        'Wagner | Merchant Services & Passive Income — KRZuPsngOLw @ '
                                        '00:01:14], then ask business or vacation.'},
                            {'name': 'trial_and_close_plan',
                             'type': 'text',
                             'prompt': 'Record the trial period you will offer, the residual you expect '
                                       'after any per-item adjustments, and how you will behave once the '
                                       'application is being filled out. Note any card-mix adjustments '
                                       'needed for high-ticket corporate card merchants.',
                             'example': 'Trial: 60 days with a switch back to traditional processing if '
                                        'the program fails [Scott Shaw — hdPpKRl1Bhk @ 00:03:03]. On a '
                                        'compliant surcharge program, adding a signature-debit per-item '
                                        'fee lifts the residual from about $40 to $82 [CCSalesPro — '
                                        'AKvayIEwefA @ 00:22:59]. Once the application starts, explaining '
                                        'stops, since one extra detail triggers ten more rebuttals.'}],
                 'completion_gate': 'Worksheet 2 is complete when commercial card share and qualification '
                                    'exclusions are documented, daily batching and CEDP verified status '
                                    'are confirmed, line-item data is real, the cash discount fee '
                                    'structure matches the average ticket, the point of sale is confirmed '
                                    'able to pass the fee with the credit price displayed, and a written '
                                    'script with annualized savings is ready.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Fee Pass-Through Compliance and Residual Agreement Protection',
                 'purpose': 'Keep every fee pass-through program legally clean and every residual '
                            'contractually yours. The fields cover choosing among surcharging, cash '
                            'discounting, and dual pricing, testing debit blocks, auditing price displays, '
                            'calculating offset rates, defusing fine exposure, projecting the residual '
                            'book, and locking down agreement language before the first merchant signs.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Choose the pass-through method from how prices are actually posted, not '
                                  'from the program name the processor uses.',
                                  'Test the debit block on live hardware with both PIN and credit entry '
                                  'before the program goes live.',
                                  "Walk the merchant's premises, menus, website, and quotes in person to "
                                  'confirm every price exists twice.',
                                  'Project residuals with conservative per-account figures and add a '
                                  'client buffer for cancels and shortfalls.',
                                  'Get vesting, residual ownership, and termination terms in writing '
                                  'before boarding a single merchant under any agreement.'],
                 'fields': [{'name': 'pass_through_method',
                             'type': 'text',
                             'prompt': 'Identify which of the three legal fee-offset methods fits this '
                                       'specific merchant: surcharging, cash discounting, or dual pricing. '
                                       'Base the choice on how prices are actually posted, card-present '
                                       "versus card-not-present mix, and the merchant's debit share.",
                             'example': 'Storefront with heavy debit volume, so dual pricing ranks first; '
                                        'Global Legal Law Firm notes almost every business has a problem '
                                        'otherwise because the surcharge does not cover the spread and '
                                        'cannot touch debit [Global Legal Law Firm — rj9tjHr1nNo @ '
                                        '00:10:39]. A 100% card-not-present seller would more likely lean '
                                        'toward surcharging [CCSalesPro — gBwNpKmRuWY @ 00:23:56].'},
                            {'name': 'surcharge_rule_checklist',
                             'type': 'textarea',
                             'prompt': 'If surcharging, document each requirement: credit-only '
                                       'application, the percentage cap, notice given to the acquirer, '
                                       'door and till signage, and a separate receipt line. Record the '
                                       'date each item was completed and who confirmed it.',
                             'example': 'Surcharge set at 3%, capped at cost of acceptance and never above '
                                        '3% under Visa, credit only, with debit and prepaid excluded even '
                                        'when debit runs as credit [POS Nexus — m1nRWuyd4rI @ 00:00:36]. '
                                        'Acquirer notified 30 days ahead, signage posted at the door and '
                                        'till, and the receipt shows the surcharge on its own line.'},
                            {'name': 'debit_block_test',
                             'type': 'text',
                             'prompt': 'Test whether the terminal or POS software stops the surcharge on '
                                       'every debit card, whether the customer enters a PIN or the card is '
                                       'run as credit. Record the test cards used, the outcome, and any '
                                       'configuration change required.',
                             'example': 'Ran a debit card with PIN and again as credit; the second attempt '
                                        'fired the surcharge. Reprogrammed the terminal so the fee never '
                                        'applies to debit, because Ryan Anthony is clear that a debit card '
                                        'is a debit card no matter how it is run [Ryan Anthony — '
                                        'KsqD8Ch93YI @ 00:07:07]. Retest passed on both entry methods.'},
                            {'name': 'dual_price_display_audit',
                             'type': 'textarea',
                             'prompt': 'Audit every place a price appears, including shelf labels, menus, '
                                       'the website, and quotes, and confirm the POS stores two real '
                                       'prices. Flag any non-cash adjustment fee that is added and then '
                                       'discounted back off for cash payments.',
                             'example': 'Menus and website showed one price while the POS added a '
                                        'percentage at the till; every price must exist twice, with two '
                                        'real prices stored [POS Nexus — ZAtYPaS2xkA @ 00:01:04]. The old '
                                        'non-cash adjustment fee was removed, since the brands treat it as '
                                        'a surcharge under the 3% cap and debit ban [Ryan Anthony — '
                                        'KsqD8Ch93YI @ 00:12:13].'},
                            {'name': 'statement_offset_rate',
                             'type': 'text',
                             'prompt': 'Calculate the statement rate the processor must charge so a dual '
                                       'pricing card price nets the merchant zero. Show volume before and '
                                       'after the card price, the extra revenue amount, and the resulting '
                                       'offset percentage on the statement.',
                             'example': 'Card price set at 3.99% on $100,000 in card sales lifts volume to '
                                        '$103,990. Fees also run on the extra $3,990, so 3,990 divided by '
                                        '103,990 gives roughly 3.84%, the rate that nets the merchant zero '
                                        '[CCSalesPro — ZRmKamGyTPc @ 00:03:07]. Quoting 3.99% on the '
                                        'statement would leave the merchant slightly out of pocket.'},
                            {'name': 'competitor_statement_check',
                             'type': 'textarea',
                             'prompt': "When a competitor's dual pricing statement shows almost no fees, "
                                       'document where the real cost is hiding. Record any batch pull, '
                                       'consumer credit line, or daily discount matching a flat rate above '
                                       '3% before you quote against it.',
                             'example': 'Competitor statement showed near-zero monthly fees, but each '
                                        'daily deposit carried a discount matching a flat rate above 3%, '
                                        'exactly the pattern CCSalesPro tells agents to hunt for before '
                                        'quoting [CCSalesPro — ZRmKamGyTPc @ 00:04:04]. Effective rate '
                                        'calculated as total card fees divided by card sales came to 3.6%, '
                                        'which became the real comparison number [POS Nexus — ZAtYPaS2xkA '
                                        '@ 00:02:07].'},
                            {'name': 'fine_exposure_plan',
                             'type': 'textarea',
                             'prompt': 'List every legacy program element that could draw a fine, the fine '
                                       'amounts at stake, and the deadline to fix each one. Note what you '
                                       'will personally fund, such as menu reprints, to get the merchant '
                                       'compliant before secret shoppers arrive.',
                             'example': 'Restaurant on a legacy cash discount program faces a $1,000 first '
                                        'fine, plus $5,000 more if not fixed within 30 to 45 days [Ryan '
                                        'Anthony — KsqD8Ch93YI @ 00:11:14]. I am paying for the menu '
                                        'redesign and reprint myself so the merchant becomes compliant '
                                        'fast, because secret shoppers are still handing down fines '
                                        '[Global Legal Law Firm — rj9tjHr1nNo @ 00:10:55].'},
                            {'name': 'residual_projection',
                             'type': 'textarea',
                             'prompt': 'Project your residual book using a realistic per-account figure '
                                       'and your actual split. Show how many new accounts per month you '
                                       'expect, the delay before residuals arrive, and the merchant count '
                                       'needed to hit your monthly income target with a buffer.',
                             'example': "Shepard's average is about $30 per account monthly, roughly two "
                                        'months behind the sale, so 10 sales add about $300 [CCSalesPro — '
                                        'VNId5AUIElE @ 00:05:54]. For a $10,000 target at $400 per client, '
                                        'the math gives 35 merchants, plus a 15-client buffer for cancels, '
                                        'landing on 50 [Residual Builders — 4z4EyZ1Rkbk @ 00:05:05].'},
                            {'name': 'split_vs_schedule_a',
                             'type': 'textarea',
                             'prompt': 'Compare competing processor offers by projected residual per month '
                                       "rather than headline split. Record each processor's split, upfront "
                                       'bonus, and whether it shared its Schedule A, then note any offer '
                                       'where a large split hides inflated costs.',
                             'example': 'Processor A offered an 80% split with an upfront bonus but raised '
                                        'Schedule A costs, so it pays a big piece of a smaller pie '
                                        '[CCSalesPro — ruAqtp4NcPA @ 00:04:41]. Processor B shared its '
                                        'Schedule A at roughly the 50% industry-average split [CCSalesPro '
                                        '— ruAqtp4NcPA @ 00:03:50] and projected more residual per month '
                                        'across three merchant sizes.'},
                            {'name': 'agreement_protection_terms',
                             'type': 'textarea',
                             'prompt': 'Before signing a single merchant, record the exact agreement '
                                       'language on vesting, residual rights after you stop selling, and '
                                       'what happens on sale or termination of the company. Note how the '
                                       'processor handles rate increases and support contact.',
                             'example': 'Joe Wagner lost an entire book after 3.5 years over one sentence '
                                        'in a clause [Joe Wagner | Merchant Services & Passive Income — '
                                        'Em1hM53SuTA @ 00:04:20]. Vesting and post-termination residual '
                                        'rights are now confirmed in writing. The processor commits to no '
                                        'six-month rate and fee increases, and support keeps me as the '
                                        "merchants' primary point of trust."}],
                 'completion_gate': 'Worksheet 3 is complete when the pass-through method is chosen and '
                                    'documented, surcharge rules or dual price displays are verified, '
                                    'debit blocking passes retest, the statement offset rate is '
                                    'calculated, all fine exposures have dated fixes, competing processors '
                                    'are compared on Schedule A residual, and vesting and residual rights '
                                    'are confirmed in writing.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Portfolio Asset Audit and ISO Ladder Plan',
                 'purpose': 'Turn signed merchants into a durable, sellable residual asset. Lock down '
                            'ownership language, drive activations, and test support. Model attrition and '
                            'buyout value, then choose the right rung on the ISO ladder before scaling '
                            'past what your back office can handle.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull your current ISO or agent agreement, Schedule A, and latest '
                                  'residual report before filling in any field.',
                                  'Complete the ownership field first; if the residual is not yours in '
                                  'writing, pause all new boarding until it is.',
                                  'Count only merchants that are approved, boarded, and processing live '
                                  'transactions when tallying your book.',
                                  'Price any buyout on the upfront check alone, and obtain an independent '
                                  'outside bid before responding to your ISO.',
                                  'Revisit the registration and scaling fields each quarter as your '
                                  'monthly MID count and support load change.'],
                 'fields': [{'name': 'residual_ownership_clause',
                             'type': 'textarea',
                             'prompt': 'Quote the exact sentence in your ISO or agent agreement that '
                                       'states who owns the residual, whether the book leaves with you, '
                                       'and what happens on termination or sale. Note any wording you '
                                       'could not confirm in writing before boarding merchants.',
                             'example': 'My draft says residuals survive termination, but the '
                                        'sale-of-company language is blank. Joe Wagner lost residuals for '
                                        'four years with the wrong ISO [Joe Wagner | Merchant Services & '
                                        'Passive Income — 6fKRmYMx0m8 @ 00:04:00], and CCSalesPro says '
                                        'most agreements deny agents the asset [CCSalesPro — RMbvSJJrPMQ @ '
                                        '00:01:43], so no merchant gets signed until that blank is '
                                        'filled.'},
                            {'name': 'activation_tracker',
                             'type': 'textarea',
                             'prompt': 'List every merchant signed in the last 90 days and mark whether '
                                       'each is approved, boarded, and running live transactions. Flag any '
                                       'free terminal sitting unactivated and record the date you called '
                                       'the owner to plug it in.',
                             'example': 'Twelve deals signed, eleven active, one terminal still boxed at a '
                                        'cafe; I called the owner Tuesday to plug it in. Wagner says '
                                        'activations are the most important part [Joe Wagner | Merchant '
                                        'Services & Passive Income — j2tVhd1OiOw @ 00:00:00], and Finance '
                                        'Blueprint counts a merchant only after its first live transaction '
                                        '[Finance Blueprint — _wQk1Avcku8 @ 00:08:59].'},
                            {'name': 'support_line_test',
                             'type': 'textarea',
                             'prompt': "Call the ISO's support line yourself before committing. Record who "
                                       'merchants actually reach, the support hours, the training offered, '
                                       'and the escalation path, then note whether support keeps you as '
                                       "the merchant's primary point of trust and never reprices your "
                                       'merchants.',
                             'example': 'Rang the line at 7 p.m.: a live rep answered, offered agent '
                                        'training, and named a tier-two escalation contact. Wagner warns '
                                        'weak support turns five signed accounts into three lost [Joe '
                                        'Wagner | Merchant Services & Passive Income — rStTwQf0M98 @ '
                                        '00:03:42], and Electronic Money Company flags support that '
                                        'reprices merchants through the 1-800 line [Electronic Money '
                                        'Company — HAEcBxhwNkI @ 00:03:03].'},
                            {'name': 'attrition_and_pricing_model',
                             'type': 'textarea',
                             'prompt': 'Enter your active account count, the basis points you price above '
                                       'cost, and your split. Then project annual attrition at the '
                                       'industry rate and estimate how your pricing choice changes what '
                                       'the book would fetch at buyout.',
                             'example': 'Two hundred accounts on a 50 percent split. At 5 basis points the '
                                        'book pays about $600 a month and buys out near $5,000; at 15 '
                                        'basis points the buyout climbs to about $30,000 [CCSalesPro — '
                                        'iouhW_rMFI0 @ 00:02:48]. At 23 to 24 percent attrition '
                                        '[CCSalesPro — iouhW_rMFI0 @ 00:02:16], I lose roughly 47 accounts '
                                        'a year.'},
                            {'name': 'buyout_offer_review',
                             'type': 'textarea',
                             'prompt': 'Break down any residual buyout offer into the upfront multiple and '
                                       'each earn-out or holdback. Record whether you obtained an '
                                       'independent third-party bid, whether the ISO holds right of first '
                                       'refusal, and whether the upfront check alone satisfies you.',
                             'example': 'My ISO offered 20X on $2,000 a month, split 12X upfront plus two '
                                        '4X earn-outs. Nine times out of ten those earn-outs never pay '
                                        '[CCSalesPro — Aqf6gQvEgnw @ 00:01:43], so I am valuing only the '
                                        '$24,000 upfront, taking an extra week, and requesting an outside '
                                        'bid since the ISO may match it [CCSalesPro — qaQA_RMy-_c @ '
                                        '00:01:57].'},
                            {'name': 'retention_positioning',
                             'type': 'textarea',
                             'prompt': 'Describe how you will position yourself beyond rates when '
                                       'prospecting. Name the merchant pain you lead with, such as unhappy '
                                       'support or software fit, and explain how that positioning keeps '
                                       'accounts active long enough to compound the book.',
                             'example': 'Wagner says if rates is all you are selling you are already way '
                                        'behind [Joe Wagner | Merchant Services & Passive Income — '
                                        '3FBYq-eEJOk @ 00:00:00]. I open with service: many owners are '
                                        'unhappy with Clover support [Electronic Money Company — '
                                        '4LJj9o_IDnQ @ 00:02:03], so I promise a direct line to me and a '
                                        'same-day fix.'},
                            {'name': 'referral_channel',
                             'type': 'text',
                             'prompt': 'Identify one software company or vertical partner whose merchants '
                                       'you could refer into your book. State the revenue cut you would '
                                       'offer, and list the qualification tells you will use to screen B2B '
                                       'prospects that partner sends.',
                             'example': 'A local invoicing software vendor; I will offer a revenue cut for '
                                        'referrals, the move Nathan made after a restart [Residual Income '
                                        'for Beginners — GNbDvrGPlnM @ 00:26:26]. Each referred prospect '
                                        'gets screened on three tells: uses a CRM, sends invoices, or runs '
                                        'complex workflows or Stripe [DepositFix — 4idRDNmCnvE @ '
                                        '00:01:05].'},
                            {'name': 'entity_and_branding_setup',
                             'type': 'text',
                             'prompt': 'Record the legal entity that signs your agent agreement, and list '
                                       'which branded items come bundled into the residual split: '
                                       'statements, applications, dashboards, and support. Note any '
                                       'per-seat or per-agent fees the partner charges instead before you '
                                       'sign.',
                             'example': 'The agreement is signed by my LLC, not me personally, from day '
                                        'one [CCSalesPro — KFKUpD0sDxk @ 00:02:25]. Branded statements, '
                                        'applications and dashboards are included in the split; support is '
                                        'masked under my brand, which Shaw Merchant Group offers through '
                                        'its call centers [Scott Shaw — wOJ4s_5GRDY @ 00:02:20]. No '
                                        'per-seat fees.'},
                            {'name': 'registration_decision',
                             'type': 'textarea',
                             'prompt': 'Decide whether to stay an agent, join a branded partner program, '
                                       'or register your own ISO. Compare registration cost and time '
                                       'against expected sales lift, and record the per-authorization buy '
                                       'cost and upfront bonuses each partner program advertises.',
                             'example': 'Registration runs about six months and $30,000 to $40,000 with no '
                                        'real sales lift [CCSalesPro — KFKUpD0sDxk @ 00:04:55], so I am '
                                        'staying under a partner. North American Bancard quotes 1.2 cents '
                                        'per authorization at zero basis points, Shaw 1.5 cents, with up '
                                        'to $10,000 upfront per merchant [Scott Shaw — tjdQFiCG9xo @ '
                                        '00:00:18].'},
                            {'name': 'scaling_infrastructure',
                             'type': 'textarea',
                             'prompt': 'Estimate your monthly MID target for the next year and state who '
                                       'owns underwriting, technical support, and customer service at that '
                                       'pace. Record your retained margin per $100 sale and your '
                                       'telemarketing appointment close rate assumptions.',
                             'example': 'Target is 40 MIDs a month, so support stays outsourced; past 100 '
                                        'a month I must bring underwriting, tech and service in-house '
                                        '[Merchant Service Slayers — pHeumyF-Dw4 @ 00:05:00]. I plan on '
                                        '22.4 cents retained per $100 sale after a 30% residual [Finance '
                                        'Blueprint — _wQk1Avcku8 @ 00:06:22] and a 5-10% new-agent close '
                                        'rate.'}],
                 'completion_gate': 'Complete when the agreement confirms in writing that you own the '
                                    'residual and the book leaves with you, every signed merchant is '
                                    'activated or has a dated follow-up call, the support line has been '
                                    'tested personally, and any buyout offer has an independent '
                                    'third-party bid on file.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'High-Risk Defense and ATM Unit Economics Ledger',
                 'purpose': 'Keep high-risk merchants under card network thresholds with routed processing '
                            'and pre-dispute alerts. Then apply the same discipline to ATM unit economics: '
                            'realistic withdrawals, every fee in the waterfall, an all-in startup budget, '
                            'and bank access for vault cash.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ["Gather last month's chargeback, fraud report, and dispute counts "
                                  'alongside card-not-present sales volume.',
                                  'Never split one business across accounts to mask a ratio; Visa can fine '
                                  '$25,000 per merchant, per month.',
                                  'Model ATM revenue from counted foot traffic and realistic withdrawals, '
                                  'never from the sales pitch.',
                                  'Order no hardware until a signed location contract is in hand and vault '
                                  'cash has an ATM-friendly bank.',
                                  'Recalculate the threshold position and the per-machine waterfall every '
                                  'month and log what changed.'],
                 'fields': [{'name': 'risk_classification',
                             'type': 'textarea',
                             'prompt': "Describe the merchant's vertical, any prior account closures, and "
                                       "whether its products appear on the processor's restricted "
                                       'businesses list. Record the reserve percentage and release window '
                                       'the acquiring bank proposes, and how you disclosed past issues '
                                       'honestly.',
                             'example': 'Supplement brand, closed once by a prior provider; we disclosed '
                                        'it plainly rather than tweaking the business description '
                                        '[PaymentProcessorCom — q9nKd4oVwnw @ 00:01:50]. I spent five '
                                        'minutes on the restricted list first [Funnelish — -G2UpQAf8L0 @ '
                                        '00:03:22]. The bank wants a reserve released in about 3 to 6 '
                                        'months if all goes well [PaymentCloud — XwCDjPAfKtY @ 00:03:17].'},
                            {'name': 'network_threshold_monitor',
                             'type': 'textarea',
                             'prompt': "Record last month's card-not-present sales, fraud reports, "
                                       "disputes, and chargebacks. Calculate the merchant's position "
                                       'against Visa and Mastercard monitoring thresholds, and note how '
                                       'many reports or chargebacks remain before either program would '
                                       'flag the account in the coming month.',
                             'example': "Visa's VAMP flag hits at 1.5% with at least 1,500 fraud reports "
                                        'and disputes; Mastercard starts at 100 chargebacks and 1.5% of '
                                        'prior-month transactions [High-Risk Merchant Accounts | Adaptiv '
                                        'Payments — NdTgGwtE_N4 @ 00:00:51]. We logged 62 chargebacks on '
                                        "9,000 transactions, 0.69%, leaving 38 before Mastercard's count "
                                        'trips. Visa tightening toward 0.5% stays on watch.'},
                            {'name': 'pre_shipment_fraud_rule',
                             'type': 'textarea',
                             'prompt': 'Write the rule that stops suspect orders before shipment rather '
                                       'than refunding them afterward. Specify the signals that hold an '
                                       'order, who reviews it, and how fast, so that issuer fraud reports '
                                       'never reach the network ratio.',
                             'example': 'Any order our review queue flags as suspect is held unshipped, '
                                        'and a manager clears it within four hours. Once a bank logs a '
                                        "fraud report it counts toward Visa's ratio even if we refund "
                                        'later [High-Risk Merchant Accounts | Adaptiv Payments — '
                                        'NdTgGwtE_N4 @ 00:02:37], so a refund is never treated as the '
                                        'fix.'},
                            {'name': 'routing_stack',
                             'type': 'textarea',
                             'prompt': 'Map the multi-processor routing stack: the default processor, '
                                       'where high-risk SKUs route, where declines retry, and the backup '
                                       'merchant account. Confirm the gateway and merchant account are not '
                                       'bundled with one provider that could shut everything down.',
                             'example': 'Stripe is the default, high-risk SKUs route to Authorize.net, and '
                                        'declines retry on NMI. Because Stripe and PayPal bundle gateway '
                                        'and merchant account, one decision can shut everything at once '
                                        '[Funnelish — -G2UpQAf8L0 @ 00:01:18]. The backup rule is live '
                                        'before we scale, since a 10X volume jump overnight gets noticed '
                                        '[Funnelish — -G2UpQAf8L0 @ 00:06:03].'},
                            {'name': 'alert_enrollment',
                             'type': 'textarea',
                             'prompt': 'List each pre-dispute alert service you will enroll in, its '
                                       'expected go-live time, and its per-alert price. Note any overlap '
                                       'that could produce double alerts and double fees on the same '
                                       'dispute, and how you will handle duplicates.',
                             'example': 'Ethoca at $29 per alert, RDR and CDRN at $15 each, paying only '
                                        'for alerts received [Chargeback — sH9CslJpDeA @ 00:01:33]. CDRN '
                                        'and Ethoca can be live in under 24 hours [Scott E. Adams | '
                                        'Chargeback Expert — gROmfVmEsYs @ 00:02:13]. Banks tied to both '
                                        'vendors can trigger double fees [Chargeflow — sBnXe7LYFO8 @ '
                                        '00:06:18], so overlapping alerts get reviewed weekly.'},
                            {'name': 'rdr_reconciliation',
                             'type': 'textarea',
                             'prompt': 'Describe how you reconcile every RDR case against processor '
                                       'chargeback reports each month. Name who checks for the missing M '
                                       'flag downstream, and how Verifi Inform descriptor data feeds your '
                                       'Compelling Evidence 3.0 and Order Insight responses.',
                             'example': 'Every Friday the ops lead matches RDR resolutions to the '
                                        'processor report, because downstream ISOs and gateways often miss '
                                        'the M flag and log a chargeback [Scott E. Adams | Chargeback '
                                        'Expert — 5mi35dvcRrA @ 00:04:08]. Verifi Inform pulls exact '
                                        'descriptors per transaction and serves as our Compelling Evidence '
                                        '3.0 feedback loop [Scott E. Adams | Chargeback Expert — '
                                        'gJ_2exzq6FA @ 00:03:19].'},
                            {'name': 'atm_revenue_waterfall',
                             'type': 'textarea',
                             'prompt': 'Build the per-machine monthly waterfall: expected withdrawals, '
                                       'surcharge, gross, network or processing fees, location share, and '
                                       'back-end or connectivity costs. Show the operating surplus and '
                                       'what share of gross disappears before it reaches you. Use '
                                       'realistic transaction counts, not pitch numbers.',
                             'example': '200 withdrawals at $3.50 gross $700; minus $100 network fees, '
                                        '$140 location share and $90 back-end leaves a $370 surplus '
                                        '[MASTER FINANCE TV — pxfdlwdIz2E @ 00:01:28]. Nearly half of '
                                        'gross vanishes, and 100 transactions at $5 is $500 gross, not '
                                        '$500 of profit [Future Investor — l2IVnP9Bnwk @ 00:04:15].'},
                            {'name': 'startup_budget',
                             'type': 'textarea',
                             'prompt': 'Itemize the all-in startup cost for one machine: hardware, vault '
                                       'cash, installation, entity formation, bank and strap fees, '
                                       'scouting gas, and a cash reserve. Compare your total against the '
                                       'three-thousand-dollar sales pitch and explain the gap.',
                             'example': "My itemized total lands at $6,900, inside Juan Jeronimo's $5,500 "
                                        'to $8,500 all-in range [Juan Jeronimo — 2iQEC3gV3oo @ 00:00:42]. '
                                        'Philip Webb warns that students budgeting on the $3,000 pitch '
                                        'underestimate working capital by up to 300% once formation, strap '
                                        'fees, scouting gas and extra vault cash hit [Philip Webb — '
                                        'nAL1HBqHAl8 @ 00:01:31].'},
                            {'name': 'site_traffic_count',
                             'type': 'textarea',
                             'prompt': 'Record two weeks of foot-traffic counts at the candidate site, '
                                       'then project monthly ATM users at four to eight percent of '
                                       'traffic. State whether the venue clears the volume band where '
                                       'machines net money or falls into the bleeding zone.',
                             'example': 'Counted 3,600 visitors over two weeks, about 7,200 a month '
                                        '[CAPITAL COACH — R1wscXZLkbw @ 00:12:27]. At 4% to 8% usage that '
                                        'projects 288 to 576 withdrawals [The Business Guy | Asset '
                                        'Protection Planners — gaNeKJoK-74 @ 00:11:20], comfortably above '
                                        'the sub-100 venues that bleed and within reach of the $280 to '
                                        '$570 net band.'},
                            {'name': 'vault_cash_banking',
                             'type': 'textarea',
                             'prompt': 'Name the ATM-friendly bank holding your vault cash, confirm the '
                                       'entity name avoids the word ATM, and describe how you separate '
                                       'surcharge funds from bulk cash. Note any machine running empty '
                                       'between refills before adding locations.',
                             'example': 'Vault cash sits at an ATM-friendly bank, never a retail checking '
                                        'account [Lines & Gains — -6VRYcYBnSA @ 00:07:45]. The LLC name '
                                        "leaves out 'ATM' because major banks treat ATMs as high-risk "
                                        '[Juan Jeronimo — eSIQwH_sArI @ 00:02:16]. Two accounts: one for '
                                        'surcharge, one for bulk cash [Juan Jeronimo — eSIQwH_sArI @ '
                                        '00:08:32]. No machine ran empty last month.'}],
                 'completion_gate': 'Complete when the merchant sits below every Visa and Mastercard '
                                    'monitoring threshold with alerts live and reconciled, a backup '
                                    'account and routing rule are active, and each ATM site shows two '
                                    'weeks of traffic counts, a positive operating surplus, an itemized '
                                    'all-in budget, and vault cash held at an ATM-friendly bank.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'ATM Placement, Agreements, Hardware, and Vault Control',
                 'purpose': 'Lock in high-traffic, cash-dependent ATM placements on enforceable '
                            'agreements, and set surcharges that hold up against competitors. Buy and '
                            'install hardware that meets the security floor, and control vault cash so no '
                            'vaulter, location, or breach clause can drain the route.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Scout competitor surcharges nearby and meet the true decision maker '
                                  'face to face before discussing terms.',
                                  'Fix your minimum take per transaction in writing before every location '
                                  'negotiation begins.',
                                  'No signed location agreement, no machine, with no handshake exceptions '
                                  'for any owner.',
                                  'Clear every used machine with your processor before any payment changes '
                                  'hands with the seller.',
                                  'Reconcile vaulted machines against settlement deposits daily and '
                                  'monthly, logging every variance found.'],
                 'fields': [{'name': 'location_prospect_profile',
                             'type': 'textarea',
                             'prompt': 'Profile the target location: business type, cash dependency, foot '
                                       'traffic, and any existing machine on site. Record the real '
                                       "decision maker's name, confirm you met them face to face, and note "
                                       'whether an incumbent box is out of service.',
                             'example': 'Cash-only barbershop with steady walk-ins; I met the owner in '
                                        'person, not a relative relaying messages, since a go-between '
                                        'forces a full restart [Philip Webb — cH26OWh_YDI @ 00:01:40]. The '
                                        'incumbent machine wears an out-of-service sticker, which Otsuji '
                                        'used as the main selling point for a swap [Chad Otsuji ATM '
                                        'Business — pxCV1SkPnK4 @ 00:04:09].'},
                            {'name': 'surcharge_setting',
                             'type': 'text',
                             'prompt': 'Set the surcharge for this location after scouting competitor fees '
                                       'nearby. State the national norm you anchor to, any event or venue '
                                       'premium you apply, and whether you leave room to negotiate if the '
                                       'owner later wants a share.',
                             'example': 'Competitors two blocks away charge $3, matching the national norm '
                                        'Webb reports [Philip Webb — r5NRe-C_aM0 @ 00:08:06]. The owner '
                                        'says they need no money, so I price at $2.50 to keep negotiating '
                                        'room if they want something later [Philip Webb — r5NRe-C_aM0 @ '
                                        '00:02:59]. Weekend events nearby could justify $4.50.'},
                            {'name': 'split_negotiation',
                             'type': 'textarea',
                             'prompt': 'Write down your minimum take per transaction before the meeting, '
                                       "the owner's opening ask, and the final split you agreed. Explain "
                                       'how you defended your floor and whether you offered volume tiers '
                                       'instead of a flat percentage.',
                             'example': 'Floor set at $2 on a $3 surcharge. The owner asked for 50/50; I '
                                        'countered the way Otsuji did, one dollar to the owner and two to '
                                        'me, roughly 33 and 66 percent [Chad Otsuji ATM Business — '
                                        'pxCV1SkPnK4 @ 00:05:22]. Holding at $2 kept the deal profitable '
                                        '[Chad Otsuji ATM Business — pxCV1SkPnK4 @ 00:04:46].'},
                            {'name': 'agreement_clauses',
                             'type': 'textarea',
                             'prompt': 'List the clauses in your signed location agreement: term length, '
                                       'auto-renewal, surcharge-raise rights with notice, breach payout '
                                       'formula, cancellation fee, and any buyout opt-out. Confirm the '
                                       'machine is not installed until the owner has verified the '
                                       'agreement.',
                             'example': 'Five-year auto-renewing term, no trial period, and surcharge '
                                        'raises allowed with notice. The breach clause bills remaining '
                                        'surcharge: 100 transactions at $2 with 24 months left is $4,800 '
                                        'plus a $100 cancellation fee [Philip Webb — 9QGfLH_pm0o @ '
                                        '00:01:35]. I removed a $5,000 buyout opt-out after Webb called '
                                        'that a significant risk [Philip Webb — kbluVa_rgsM @ 00:06:33].'},
                            {'name': 'signing_language_and_raises',
                             'type': 'textarea',
                             'prompt': 'Script the words you use to close the agreement and the notice you '
                                       'will print on monthly statements before any surcharge raise. '
                                       'Estimate how many owners in your route will push back and what '
                                       'share of the raise you would offer them.',
                             'example': 'I never say sign or contract; I ask the owner to verify the '
                                        'agreement [Philip Webb — OHndNgTdq3Y @ 00:01:17]. Statements '
                                        'carry a 30 to 60 day raise notice, and Webb sees about five '
                                        'pushbacks per 100 machines [Philip Webb — FhOgcbeefS0 @ '
                                        '00:01:47]. An owner wanting a slice moves from 50 cents to 55 on '
                                        'a fresh five-year agreement.'},
                            {'name': 'hardware_purchase_check',
                             'type': 'textarea',
                             'prompt': 'For any machine you plan to buy, record the brand, model number, '
                                       'manufacture date, software version, EMV and TLS 1.2 support, and '
                                       'whether the seller holds both passwords and the combo. Note your '
                                       "processor's sign-off before payment.",
                             'example': 'Used Genmega unit: seller supplied model number, manufacture date '
                                        'and software version, plus both passwords and the combo, and my '
                                        'processor cleared it before I paid [ATMDepot - Make Money with '
                                        'ATM Machines — ETBd5FI2JHY @ 00:02:28]. I passed on a Hyosung lot '
                                        "after Otsuji's warning that those machines are prone to "
                                        'jackpotting [Chad Otsuji ATM Business — 6zaxeyp07Zg @ 00:02:41].'},
                            {'name': 'install_and_programming',
                             'type': 'textarea',
                             'prompt': 'Document delivery and setup: the tip indicator reading at '
                                       'delivery, transport orientation, hole caps installed, clock set to '
                                       'current time, languages enabled, and confirmation the surcharge '
                                       'setting is enabled so customers are actually charged before the '
                                       'first transaction.',
                             'example': 'Tip indicator showed metallic silver, and the unit rode back-down '
                                        'with the front facing the sky [ATM Connect — ujDLOkqXvfg @ '
                                        '00:00:13]. Black caps are on every hole to keep rodents off the '
                                        'wires [ATM Connect — ujDLOkqXvfg @ 00:04:47]. Clock set, Spanish '
                                        'enabled [Rocket ATM — gS2sjD2NYOU @ 00:12:21], and surcharge '
                                        'confirmed enabled [Rocket ATM — gS2sjD2NYOU @ 00:04:02].'},
                            {'name': 'vaulter_agreement',
                             'type': 'textarea',
                             'prompt': 'Summarize the signed vaulter agreement: per-transaction pay, '
                                       'minimum fill level, refill threshold, service response time, '
                                       'penalties for missed fills, and the lead clause assigning any new '
                                       'locations the vaulter hears about to you. Attach the signed copy.',
                             'example': "Vaulter earns 95 cents per transaction, inside Webb's 70 cents to "
                                        '$1.25 standard [Philip Webb — 6k0qIHsvs0M @ 00:05:06]. Fill '
                                        'level, refill threshold, response time and penalties are written '
                                        'in before they touch the machine [Philip Webb — 6k0qIHsvs0M @ '
                                        '00:04:05], and any lead from my merchant is mine, paid as a '
                                        'referral fee [Philip Webb — 6k0qIHsvs0M @ 00:06:54].'},
                            {'name': 'cash_reconciliation',
                             'type': 'textarea',
                             'prompt': 'Describe your daily and monthly reconciliation of every vaulted '
                                       'machine against settlement deposits. Record weekly vault-cash '
                                       'needs per busy location, total cash committed across the route, '
                                       'and the months to return on that parked capital. Flag any variance '
                                       'immediately.',
                             'example': 'Each morning I match dispensed totals to settlement deposits, '
                                        'because a vault casher can move money with a click of a mouse '
                                        '[Philip Webb — zHPWp60QbG4 @ 00:06:39]. Busy locations need '
                                        '$4,200 to $6,200 a week, $16,000 minimum across three [ATM '
                                        "Connect — kXEFZM-F90k @ 00:10:13]; Zaback's five self-loaded "
                                        'machines tied up $112,500 for almost two years [Austin Zaback — '
                                        'gvvB3u1AMMI @ 00:12:05].'},
                            {'name': 'cash_vertical_and_card_alternative',
                             'type': 'textarea',
                             'prompt': 'For a dispensary or other cash-heavy placement, record the '
                                       'surcharge split, who loads the cash, and your background-check '
                                       'status. Then compare any high-risk card account offered as an '
                                       'alternative, listing rate, per-authorization fee, chargeback fee, '
                                       'and rolling reserve terms.',
                             'example': 'Dispensary split is 50/50 since I load cash, at the bottom of the '
                                        '60 percent to 50/50 range Webb hears [Philip Webb — ZN0dj7u6nmo @ '
                                        '00:03:11]. Background check cleared [ATMDepot - Make Money with '
                                        'ATM Machines — Cb9qwLOH7y0 @ 00:02:08]. Durango lists 1.95% to '
                                        '4.95% plus 15 to 25 cents, $15 to $25 chargebacks, 5 to 10% '
                                        'reserve [Megalith — lnoavHYKfcI @ 00:01:28].'}],
                 'completion_gate': 'Complete when every placement has a verified written agreement with '
                                    'breach and raise clauses, a surcharge set against scouted '
                                    'competitors, processor-cleared EMV and TLS 1.2 hardware with the '
                                    'surcharge enabled, a signed vaulter agreement containing a lead '
                                    'clause, and daily reconciliation against settlement deposits running '
                                    'without unexplained variances.'}]}
