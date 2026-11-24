from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'surcharging-compliance-legal-ways-to-pass-on-card-fees',
 'question_prompt': 'When is it legal to surcharge or charge a card fee, and how do you set up compliant '
                    'surcharging, zero-fee, and card-not-present programs?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Surcharging Compliance and the Legal Ways to Pass On Card Fees',
 'subtitle': 'The three legal fee-offset methods; compliant surcharging and dual pricing in 2026; whether '
             'zero-fee processing is legal; debit surcharge rules; the Visa/Mastercard settlement; '
             "card-not-present programs; consumer pushback; and Australia's surcharge ban and its backlash",
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Payments operators agree there are three legal ways to pass card fees to buyers: '
                      'surcharging, cash discounting, and dual pricing. They also agree that the posted '
                      'price, not the program name, decides which rules apply. Surcharging is boxed in: '
                      "credit only, never debit, a 3% cap under Visa, thirty days' notice, door and till "
                      "signage, and a separate receipt line. That ceiling is why Global Legal Law Firm's "
                      'James Huber and Ryan Anthony both rank dual pricing first. The street math: a 3.99% '
                      'card price on $100,000 needs roughly a 3.84% statement rate to net the merchant '
                      'zero, cash discount runs at a 4% going rate, and fines for sloppy programs start at '
                      '$1,000. Practitioners split on cap levels, on whether customers walk away, and on '
                      "whether Australia's surcharge ban simply moves the cost into higher shelf prices.",
 'key_metrics': [{'label': 'Visa Credit Surcharge Ceiling',
                  'metric': 'Visa Credit Surcharge Ceiling',
                  'value': 'Capped at cost of acceptance and never more than 3%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Visa's surcharge rules apply to credit cards only. Debit and prepaid are "
                             'excluded even when debit runs as credit. Merchants must give the acquirer 30 '
                             "days' notice.",
                  'source': 'POS Nexus ([m1nRWuyd4rI @ 00:00:36])'},
                 {'label': 'Dual Pricing Statement Offset Rate',
                  'metric': 'Dual Pricing Statement Offset Rate',
                  'value': '3.99% card price on $100,000 requires about 3.84% charged',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Volume rises to $103,990. Fees also run on the extra $3,990, so 3,990 '
                             'divided by 103,990 gives roughly 3.84% to net the merchant zero.',
                  'source': 'CCSalesPro ([ZRmKamGyTPc @ 00:03:07])'},
                 {'label': 'Non-Compliant Cash Discount Fine Ladder',
                  'metric': 'Non-Compliant Cash Discount Fine Ladder',
                  'value': '$1,000 first fine, plus $5,000 if not fixed in about 30 to 45 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ryan Anthony says he has personally seen merchants on legacy cash discount '
                             'programs fined. He has heard of $25,000 fines per incident.',
                  'source': 'Ryan Anthony ([KsqD8Ch93YI @ 00:11:14])'},
                 {'label': 'Surcharge Purchase Cancellation Rate',
                  'metric': 'Surcharge Purchase Cancellation Rate',
                  'value': '32% of surcharging businesses see customers cancel occasionally or frequently',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A 2026 JD Power study cited by NBC found more than one-third of small '
                             'businesses surcharge credit card payments.',
                  'source': 'TODAY ([ahGJLcVvtj0 @ 00:01:42])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator working this lane starts with the same map: there are three '
                              'legal ways to push card cost onto the buyer. Ginger Gay of Electronic Money '
                              'Company names them as surcharging, cash discounting, and dual pricing '
                              '[HlgVERn_rhY @ 00:00:00]. Ryan Anthony groups the same three under a single '
                              "'pass through' bucket. He contrasts that bucket with traditional pricing, "
                              'where the merchant eats the fee and a $100 sale at 3% deposits $97 '
                              "[KsqD8Ch93YI @ 00:05:01]. POS Nexus strips the marketing off 'zero-fee' "
                              'processing: interchange and network fees are still paid on every card sale, '
                              'and the cost mostly moves from merchant to customer [ZAtYPaS2xkA @ '
                              "00:00:22]. The second point of agreement is that the program's name means "
                              'nothing. What you post decides which rules apply. POS Nexus says that if '
                              'you post the cash price and add a card fee at the till, it is a surcharge '
                              'whatever you call it. Ryan Anthony makes the same call on a $10 menu item '
                              'that rings up at $10.40 on card. Visa and Mastercard read that as an '
                              'in-effect surcharge, subject to the 3% cap and the debit ban [KsqD8Ch93YI @ '
                              '00:10:42]. Every program that survives a secret shopper starts from one '
                              'question: which price does the shopper see first?',
                              'On surcharging itself, the rulebook practitioners recite is nearly '
                              "word-for-word identical across channels. POS Nexus walks through Visa's "
                              'version. Credit cards only, with debit and prepaid off-limits even when '
                              'debit runs as credit. The fee is capped at your cost of accepting that card '
                              "and never above 3%. The acquirer gets thirty days' notice, there is a sign "
                              'at the door and another at the till, and the surcharge appears as its own '
                              'receipt line [m1nRWuyd4rI @ 00:00:36]. Nuvei repeats the same pillars: '
                              'disclosure at the point of sale and on the receipt, a cap tied to the cost '
                              'of acceptance, and an exemption for debit and prepaid cards [bBQUixWA9qA @ '
                              '00:01:18]. Merchant Maverick adds the online version, which puts the notice '
                              'on the checkout page, and tells merchants to program the payment gateway to '
                              'record surcharges accurately. It also notes that Visa and Mastercard allow '
                              'brand-level or product-level surcharges, but not both [CTTa8diTsTU @ '
                              "00:02:07]. WKYC's Stephanie Haney draws the hard line under the card rules. "
                              'The network caps are contract terms merchants accept in order to take the '
                              'cards, not law. Federal law, however, makes surcharges illegal on debit, '
                              'including debit processed without a PIN [AGTRnXUImOw @ 00:00:51]. That '
                              'debit wall is the shared reason surcharging alone rarely recovers the full '
                              'fee.',
                              'The strongest consensus is that dual pricing is where both the merchant and '
                              'the ISO actually get paid. James Huber of Global Legal Law Firm puts it '
                              'bluntly to guest Clark Cramer. The 3% surcharge does not cover the '
                              "merchant's fees and leaves a thin margin for the sales organization, so "
                              'dual pricing is the only way to make money as an ISO while covering the '
                              'cost of card acceptance. Cramer answers that this is exactly right '
                              '[rj9tjHr1nNo @ 00:08:07]. Ryan Anthony ranks the three programs and puts '
                              'dual pricing first because it is completely compliant and tells the '
                              'consumer the deal up front. Cash discount comes second and surcharging last '
                              '[KsqD8Ch93YI @ 00:15:12]. James Shepherd of CCSalesPro says the card brands '
                              'have specifically pointed to a cash price and a card price as compliant. He '
                              'adds that card-not-present invoices make this cleaner, because the customer '
                              'sees both prices on the payment page [gBwNpKmRuWY @ 00:42:48]. POS Nexus '
                              'sets the bar for doing it right. Every price exists twice: on shelf labels, '
                              'menus, the website, and quotes. The POS stores two real prices instead of '
                              'adding a percentage at the till, and the receipt shows which price the '
                              'customer paid [ZAtYPaS2xkA @ 00:01:04]. Across these voices the rule is '
                              'consistent: the higher price is the posted price, and the cash or ACH price '
                              'is the visible discount.'],
               'table': {'caption': 'What Practitioners Agree On for Each Fee Pass-Through Path',
                         'headers': ['Program or Rule',
                                     'What Gets Posted or Charged',
                                     'Point Practitioners Agree On',
                                     'Expert Source'],
                         'rows': [['Surcharge on credit card transactions only',
                                   'Normal price is posted and a fee is added at checkout for credit',
                                   'Capped at your cost of acceptance and never above three percent under '
                                   'Visa rules',
                                   'POS Nexus ([m1nRWuyd4rI @ 00:00:36])'],
                                  ['Debit card exclusion, whether PIN or signature',
                                   'Any card that pulls funds directly out of a checking account',
                                   'No surcharge on debit, and terminal or POS software must block the fee '
                                   'automatically',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:07:07])'],
                                  ['Cash discount program with higher posted prices',
                                   'All prices are raised and posted high, then cash gets money off',
                                   'Going rate is four percent, with no limit on the cash discount or on '
                                   'price increases',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:09:41])'],
                                  ['Dual pricing with two real prices everywhere',
                                   'Cash and card prices are both shown on labels, menus, website, and '
                                   'quotes',
                                   'POS stores two real prices and the receipt shows exactly which price '
                                   'was paid',
                                   'POS Nexus ([ZAtYPaS2xkA @ 00:01:04])'],
                                  ['Surcharge disclosure at the door, till, and checkout',
                                   'Notice at the entrance, near the point of sale, and on online checkout '
                                   'pages',
                                   'The surcharge amount must be listed on the receipt as a separate line '
                                   'item',
                                   'Merchant Maverick ([CTTa8diTsTU @ 00:02:07])'],
                                  ['Convenience fee for a non-standard payment channel',
                                   'Percentage or flat fee for paying online or by phone instead of mail',
                                   'Ohio law allows convenience fees regardless of which type of card the '
                                   'customer uses',
                                   'WKYC Channel 3 ([AGTRnXUImOw @ 00:01:10])'],
                                  ['Zero-fee processing as a marketing label',
                                   'The name processors use for shifting card processing cost onto the '
                                   'customer',
                                   'Interchange and network fees are still paid on every sale, and the '
                                   'cost simply moves',
                                   'POS Nexus ([ZAtYPaS2xkA @ 00:00:22])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The base math is simple. Ryan Anthony runs a $100 sale at 3%. On '
                              'traditional pricing the merchant deposits $97. On a pass-through program '
                              'the customer pays $103 and the merchant deposits the full $100 [KsqD8Ch93YI '
                              "@ 00:02:39]. James Shepherd shows why the processor's statement rate never "
                              'matches the shelf markup. A merchant doing $100,000 a month adds a 3.99% '
                              'card price, so volume becomes $103,990. To collect the $3,990 and leave the '
                              'merchant owing nothing, the processor charges roughly 3.84%, because fees '
                              'now run on the extra $3,990 as well [ZRmKamGyTPc @ 00:03:07]. Shepherd also '
                              "lists the statement tells that give away a competitor's dual pricing deal. "
                              'The first is a high flat rate above 3% with no per-item cost. The second is '
                              "money pulled out of the batch at settlement, shown as a separate 'consumer "
                              "credit' style line. The third is a daily discount that matches the flat "
                              'rate. The sneakiest version is a minimalist statement on a $30,000 month '
                              'showing only a $20 monthly fee and an $8.95 PCI fee, for $28.95 total. '
                              'Shepherd says to assume the merchant is paying far more and the processor '
                              "simply chose not to print the offset [ZRmKamGyTPc @ 00:05:30]. Ginger Gay's "
                              'cash discount receipt shows the same structure at the counter: a total, a '
                              'fee notation line, then the grand total [HlgVERn_rhY @ 00:01:46].',
                              'On the hardware side, Clark Cramer of National E-Payments built Due Price, '
                              'a digital label gun for retail shelves. The operator keys in the item price '
                              'and the percentage, 3% or 4%. The gun then prints one label carrying both '
                              "the cash price and the card price. That solves Huber's complaint that "
                              'gas-station-style posting falls apart inside a store, where prices change '
                              "every day [rj9tjHr1nNo @ 00:08:47]. For East Coast restaurants, Cramer's "
                              'shop goes further and pays for the menu reprint itself so the merchant '
                              'becomes compliant, because secret shoppers are still out handing down fines '
                              '[rj9tjHr1nNo @ 00:11:14]. Ryan Anthony says his programs raise every price '
                              'by the 4% going rate and then adjust each new price to land on a round '
                              'number the merchant chooses. He pegs the recovered money at $2,000 to '
                              '$5,000 a month for merchants processing between $20,000 and $200,000 a '
                              "month [KsqD8Ch93YI @ 00:15:44]. Ginger Gay's dual pricing terminals print a "
                              'receipt with both the cash and non-cash totals, so the customer can switch '
                              'to cash right at the terminal. Her company also runs a white-label POS that '
                              'builds dual pricing into the whole system [HlgVERn_rhY @ 00:03:27]. Every '
                              'one of these tools exists to keep the posted price and the charged price '
                              'identical, because that gap is where the fines land.',
                              "Card-not-present is where Shepherd and payroc's James Derby say these "
                              'programs sell easiest. Online, dual pricing runs as an ACH price versus a '
                              'card price. The customer clicks the invoice link or hosted payment page and '
                              'picks one. Derby says agents treat ACH as the necessary component for true '
                              'compliant dual pricing, because nobody can hand over cash through a virtual '
                              'terminal [gBwNpKmRuWY @ 00:27:15]. He says payroc approved a lighter ACH '
                              'tier that skips the three months of bank statements, limited to roughly '
                              '$2,000 a day and $500 per transaction. He claims merchants on the program '
                              'save up to about 90 to 95% of their total card acceptance bill [gBwNpKmRuWY '
                              '@ 00:40:33]. For surcharging high-ticket B2B and service merchants, Derby '
                              'calls the pass-through an art form. With a 3.5% all-in cost, the merchant '
                              'passes 2% to the cardholder and eats 1.5%, dropping from 2.85% to a point '
                              "and a half. Payroc's technology also identifies the card as it is entered "
                              'and tells the cardholder whether the surcharge applies [gBwNpKmRuWY @ '
                              '00:24:51]. Ginger Gay adds a separate lever for those same buyers. '
                              'Terminals that autofill Level 2 data, such as purchase order number, tax '
                              'amount, and product description, average 8% savings on B2B and government '
                              'cards, with no extra steps for staff [MTRmzsfsHTs @ 00:02:27].'],
               'table': {'caption': 'Street Numbers and Settings Operators Use to Run Fee Pass-Through '
                                    'Programs',
                         'headers': ['Mechanic',
                                     'Exact Number or Setting',
                                     'How Operators Run It',
                                     'Expert Source'],
                         'rows': [['Pass-through deposit math on a single sale',
                                   '$100 sale at 3%: customer pays $103 and merchant deposits $100',
                                   'Compare against traditional pricing, where the same sale deposits only '
                                   '$97',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:02:39])'],
                                  ['Statement offset rate on dual pricing volume',
                                   '3.99% card price on $100,000 needs roughly 3.84% charged on statement',
                                   'Divide 3,990 by 103,990 so fees on the added volume net to zero',
                                   'CCSalesPro ([ZRmKamGyTPc @ 00:03:07])'],
                                  ['Minimalist competitor statement on a dual pricing account',
                                   '$20 monthly plus $8.95 PCI equals $28.95 shown on $30,000 volume',
                                   'Assume the merchant is paying far more and build the proposal '
                                   'accordingly',
                                   'CCSalesPro ([ZRmKamGyTPc @ 00:05:30])'],
                                  ['Retail shelf labeling with the Due Price label gun',
                                   'Key in the item price plus 3% or 4% for automatic calculation',
                                   'Prints a single label carrying both the cash price and the card price',
                                   'Global Legal Law Firm ([rj9tjHr1nNo @ 00:08:47])'],
                                  ['Lightweight ACH tier for card-not-present dual pricing',
                                   'Up to about $2,000 a day and $500 per transaction',
                                   'Skips three months of bank statements so agents can board merchants '
                                   'quickly',
                                   'CCSalesPro ([gBwNpKmRuWY @ 00:40:33])'],
                                  ['Partial surcharge split for high-ticket merchants',
                                   '3.5% all-in cost: pass 2% to the cardholder and absorb 1.5%',
                                   'Takes a merchant from 2.85% effective down to roughly a point and a '
                                   'half',
                                   'CCSalesPro ([gBwNpKmRuWY @ 00:24:51])'],
                                  ['Small brewery surcharge sized to its average tab',
                                   'About $29 average tab carries an 87 cent credit card surcharge',
                                   'Signage posted up front so every customer knows the actual bill in '
                                   'advance',
                                   'TODAY ([ahGJLcVvtj0 @ 00:02:13])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How Field Operators Close and Protect Pass-Through Deals',
                           'body': 'Tactics practitioners use to win the objection, read the competition, '
                                   'and keep the merchant clear of secret-shopper fines.',
                           'items': ['Open with the fuel-station question: ask the owner whether a cash '
                                     'price and a card price at the pump is dishonest. Once they say no '
                                     'and explain it is about avoiding processing fees, they have defended '
                                     'dual pricing before you pitch it [CCSalesPro — gBwNpKmRuWY @ '
                                     '00:38:58]',
                                     'For restaurants, offer to pay for the menu redesign and reprint '
                                     'yourself so the merchant gets compliant fast, because secret '
                                     'shoppers are still out handing down fines [Global Legal Law Firm — '
                                     'rj9tjHr1nNo @ 00:10:55]',
                                     "When a competitor's dual pricing statement shows almost no fees, "
                                     "look for the batch pull, the 'consumer credit' line, or a daily "
                                     'discount matching a flat rate above 3% before quoting [CCSalesPro — '
                                     'ZRmKamGyTPc @ 00:04:04]',
                                     'Program the terminal or POS so the surcharge never fires on a debit '
                                     'card, PIN or signature, because a debit card is a debit card no '
                                     'matter how it is run [Ryan Anthony — KsqD8Ch93YI @ 00:07:07]']},
               'sop_steps': [{'step': 1,
                              'title': 'Measure the Real Cost First',
                              'action': "Calculate the merchant's effective rate before choosing any "
                                        'program.',
                              'detail': 'Divide total card fees by card sales. If the effective rate is '
                                        'lower than the owner thinks, passing the cost on may not be worth '
                                        'it at all [POS Nexus — ZAtYPaS2xkA @ 00:02:07]'},
                             {'step': 2,
                              'title': 'Match the Program to the Card Mix',
                              'action': 'Pick surcharge, cash discount, or dual pricing based on '
                                        'credit-versus-debit volume and cash handling.',
                              'detail': 'Surcharging recovers a lot for mostly-credit merchants but does '
                                        'little for mostly-debit ones. Venues with no cash handling should '
                                        'stay on traditional pricing [Ryan Anthony — KsqD8Ch93YI @ '
                                        '00:16:00]'},
                             {'step': 3,
                              'title': 'Load Two Real Prices Everywhere',
                              'action': 'Post both prices on shelf labels, menus, website, and quotes, and '
                                        'store both in the POS.',
                              'detail': 'Use a label gun that prints the cash and card price on one label, '
                                        'and make sure the POS holds two real prices instead of adding a '
                                        'percentage at the till [Global Legal Law Firm — rj9tjHr1nNo @ '
                                        '00:08:47]'},
                             {'step': 4,
                              'title': 'Notify, Sign, and Itemize',
                              'action': "If surcharging, give 30 days' notice, post signs at the door and "
                                        'till, and itemize on the receipt.',
                              'detail': 'Limit the surcharge to credit only, capped at cost and never '
                                        'above 3%, and confirm the terminal can surcharge credit only and '
                                        'itemize it [POS Nexus — m1nRWuyd4rI @ 00:00:36]'}]},
              {'id': 'section_3',
               'heading': '3. Where Practitioners Disagree & Alternative Playbooks',
               'title': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The practitioners who teach the surcharge cap disagree about where it sits. '
                              'Ryan Anthony of Champion Payments tells merchants flatly that you cannot do '
                              '4%. He says Visa capped surcharging at 3% because the brand does not want '
                              'shoppers to think Visa is more expensive to use [KsqD8Ch93YI @ 00:06:30]. '
                              'Merchant Maverick reads the card rules differently. It tells viewers the '
                              'surcharge can never exceed the fee on the credit card transaction and is '
                              'capped at 4%, or 2% for merchants operating in Colorado [CTTa8diTsTU @ '
                              "00:01:51]. WKYC's legal segment lands between the two. It reports that Visa "
                              'and Mastercard cap surcharges at 3 or 4% of the sale, then stresses that '
                              'those card-company limits are rules businesses agree to in order to take '
                              'the cards, not the law [AGTRnXUImOw @ 00:00:34]. The cash-discount side has '
                              'the same split. Ginger Gay of Electronic Money Company says the '
                              'cash-discount fee is typically 4% and calls that the maximum you can add on '
                              '[HlgVERn_rhY @ 00:01:23]. Anthony argues the opposite: your prices are your '
                              'prices, your discounts are your discounts, and 4% is only the going rate, '
                              'with no limit on how far a merchant raises shelf prices or discounts cash. '
                              'The lowest ceiling anyone states on camera for a surcharge is 3%, capped at '
                              'actual cost.',
                              'The practitioners also split on which pass-through program to run. On the '
                              'Global Legal Law Firm podcast, the hosts argue that a 3% surcharge does not '
                              "even cover the merchant's fees and leaves the sales organization a thin "
                              'margin. In their view, dual pricing is the only way to make money as an ISO '
                              'while the merchant covers the full cost of card acceptance, and guest Clark '
                              'Cramer of National E-Payments answers that it is exactly right [rj9tjHr1nNo '
                              '@ 00:08:07]. Ryan Anthony ranks the three programs: dual pricing first '
                              'because it is completely compliant and tells the customer the deal up '
                              'front, cash discount second, and surcharging last [KsqD8Ch93YI @ 00:15:00]. '
                              'Payroc product specialist James Derby, appearing with CCSalesPro host James '
                              'Shepherd, argues the other way for card-not-present shops. He says a '
                              'merchant that is 100% card not present will more than likely lean toward a '
                              'surcharge model, because the cardholder chooses debit, prepaid, or credit '
                              'at the moment of the transaction [gBwNpKmRuWY @ 00:23:56]. Derby also '
                              'teaches a partial pass-through for high tickets. On a $2,000 average '
                              'ticket, the merchant passes 2% to the cardholder and absorbs the remaining '
                              '1.5% of a 3.5% all-in rate. That takes a merchant who was paying 2.85% down '
                              'to a point and a half, which Derby calls an art form, not a science '
                              '[gBwNpKmRuWY @ 00:24:51].',
                              'The practitioners do not agree on how hard customers push back. Clark '
                              'Cramer of National E-Payments says merchants will not switch until a '
                              'neighbor on their block goes first. Once programs are live, he says, '
                              'cardholders do complain because they believe the merchant pockets the 3% or '
                              '5% difference as profit [rj9tjHr1nNo @ 00:14:28]. SwipeNow Payments reports '
                              'a different experience. The manager of a restaurant running a 3% non-cash '
                              'fee said the fee had not turned off any customers, that cash payers '
                              'appreciate the discount, and that more nearby businesses are starting to '
                              "adopt the program [9ldQhQgiuEY @ 00:02:13]. TODAY's consumer desk cites a "
                              '2026 JD Power study: more than one-third of small businesses surcharge '
                              'credit cards, and 32% of those say customers occasionally or frequently '
                              'cancel a purchase when the charge appears. Its guest adds that consumers '
                              'tend not to be angry about fees disclosed at the very beginning '
                              '[ahGJLcVvtj0 @ 00:01:42]. In Australia, the ban flips the argument '
                              'entirely. Sydney bakery owner Sina Cleg tells ABC News the new rule is not '
                              'a ban on card surcharges, only a ban on passing them on. She says roughly '
                              '1.6% now comes straight out of small-business profit, an annual hit as high '
                              "as her bakery's rent [mlRKCgDApCY @ 00:00:28]."],
               'table': {'caption': 'Where pass-through practitioners disagree on caps, programs, '
                                    'legality, and customer reaction',
                         'headers': ['Point of Disagreement', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Surcharge ceiling on credit card transactions',
                                   'Ryan Anthony says you cannot do 4%, because Visa capped surcharging at '
                                   '3% to protect its brand',
                                   'Merchant Maverick says the surcharge is capped at 4%, drops to 2% in '
                                   'Colorado, and can never exceed the transaction fee',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:06:30]); Merchant Maverick '
                                   '([CTTa8diTsTU @ 00:01:51])'],
                                  ['Ceiling on a cash discount program',
                                   'Ginger Gay says the cash-discount fee is typically 4% and that 4% is '
                                   'the maximum you can add on',
                                   'Ryan Anthony says there is no limit on raising prices or discounting '
                                   'cash and that 4% is only the going rate',
                                   'Electronic Money Company ([HlgVERn_rhY @ 00:01:23]); Ryan Anthony '
                                   '([KsqD8Ch93YI @ 00:09:41])'],
                                  ['Best program to put a merchant on',
                                   'Ryan Anthony ranks dual pricing first, cash discount second, and '
                                   'compliant surcharging last',
                                   "Payroc's James Derby says merchants that are 100% card not present "
                                   'will more than likely lean toward a surcharge model',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:15:00]); CCSalesPro ([gBwNpKmRuWY @ '
                                   '00:23:56])'],
                                  ['Passing on the fee versus cutting the cost',
                                   'POS Nexus says to skip the fee, because a cash discount or a lower '
                                   'processing markup may be the simpler fix',
                                   'Merchant Maverick says to switch to a different provider and choose '
                                   'interchange-plus pricing if processing fees are prohibitively high',
                                   'POS Nexus ([m1nRWuyd4rI @ 00:02:30]); Merchant Maverick ([CTTa8diTsTU '
                                   '@ 00:03:24])'],
                                  ['Cutting cost on B2B and government cards',
                                   'Ginger Gay says Level 2 data enrichment autofills order number, tax '
                                   'amount, and product description, saving an average of 8% on B2B and '
                                   'B2G cards',
                                   'James Derby says to run a statement analysis first to see whether '
                                   'level two savings wash out what the reward pay surcharge would save',
                                   'Electronic Money Company ([MTRmzsfsHTs @ 00:02:27]); CCSalesPro '
                                   '([gBwNpKmRuWY @ 00:29:07])'],
                                  ['Which US states block surcharging',
                                   'Merchant Maverick lists bans in Connecticut, Massachusetts, and Puerto '
                                   'Rico, and says anti-surcharge laws in eight other states are '
                                   'unenforceable',
                                   "POS Nexus says Visa's guidance lists Connecticut, Maine, "
                                   'Massachusetts, and Oklahoma among states that prohibit or limit '
                                   'surcharging',
                                   'Merchant Maverick ([CTTa8diTsTU @ 00:00:51]); POS Nexus ([m1nRWuyd4rI '
                                   '@ 00:00:53])'],
                                  ['Customer backlash once the fee is live',
                                   'A restaurant manager told SwipeNow that its 3% credit card fee has not '
                                   'turned off any customers',
                                   'TODAY cites a 2026 JD Power study in which 32% of surcharging '
                                   'businesses say customers occasionally or frequently cancel purchases',
                                   'SwipeNow Payments ([9ldQhQgiuEY @ 00:02:13]); TODAY ([ahGJLcVvtj0 @ '
                                   '00:01:42])']]}},
              {'id': 'section_4',
               'heading': '4. Firsthand Failure Modes, Traps & Economics Checks',
               'title': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Enforcement is real but uneven, and the operators who have seen it are '
                              'specific about the cost. Ryan Anthony warns that Visa and Mastercard run '
                              'secret shoppers. He calls it rare but says it happens, and the shoppers '
                              'photograph receipts, menus, and invoices to check whether a pass-through '
                              'program is compliant [KsqD8Ch93YI @ 00:01:00]. He says he has personally '
                              'seen merchants fined. The first fine is $1,000, another $5,000 is added if '
                              'the problem is not fixed within roughly 30 or 45 days, and the fines keep '
                              'climbing from there. He has also heard secondhand of $25,000 fines per '
                              'incident [KsqD8Ch93YI @ 00:11:14]. On the Global Legal Law Firm podcast, '
                              'the hosts confirm that secret shoppers are still out there issuing fines, '
                              'though they hear of it less and less [rj9tjHr1nNo @ 00:11:14]. The firm '
                              'also describes a legal dead end. It tried to sue Visa over the fines as '
                              'unfair and anti-competitive, and the suit did not work. Visa says it is not '
                              'fining the ISO; it is fining the bank. The bank passes the fine to the '
                              'processor, the processor passes it to the merchant, and the bank, which is '
                              'making money on the arrangement, will never sue [rj9tjHr1nNo @ 00:12:09]. '
                              'Under that chain, every penalty ends up with the merchant, and agents need '
                              'to explain that before signing anyone onto a program.',
                              'Most failed programs are surcharges under a different label. Anthony says '
                              'the old non-cash adjustment fee is a no-no. Adding the adjustment and then '
                              'discounting it back off for cash payers is what the card brands call an '
                              'effective surcharge, which puts the merchant back under the debit ban and '
                              'the 3% cap [KsqD8Ch93YI @ 00:12:13]. POS Nexus lists where dual pricing '
                              'programs go wrong: only some prices get updated, the gap is a round 4% '
                              'instead of the actual cost, and nobody told the staff. It adds that posting '
                              'the cash price and adding a card fee at the till is a surcharge, whatever '
                              'the merchant calls it [ZAtYPaS2xkA @ 00:01:24]. James Huber, who litigates '
                              'these issues for Global Legal Law Firm, flags California restaurants that '
                              'put an inflation, service, or health-benefits fee of 4% to 7% at the bottom '
                              'of the menu. He says the restaurant carve-out does not cover a customer who '
                              'never saw the fee, so the right approach is two prices on every menu line '
                              '[rj9tjHr1nNo @ 00:10:19]. Debit cards are the other common trap. WKYC '
                              'reports that federal law makes surcharges illegal on debit transactions, '
                              'even when the debit card is processed like a credit card without a PIN '
                              '[AGTRnXUImOw @ 00:00:51]. Any terminal that cannot tell the card types '
                              'apart is a liability for the merchant.',
                              'The economics checks are where agents and merchants get misled. '
                              "CCSalesPro's James Shepherd walks through the offset math. A merchant doing "
                              '$100,000 a month that adds a 3.99% card price grows to $103,990 in volume. '
                              'To net out the $3,990, the processor bills roughly 3.84%, not 3.99%, '
                              'because the fees now also apply to the added volume [ZRmKamGyTPc @ '
                              '00:03:07]. He warns that some processors hide the trade-off entirely. Their '
                              'minimalist statements show a $20 monthly fee, an $8.95 PCI fee, and $28.95 '
                              'in total fees on $30,000 a month, while the merchant is actually paying far '
                              'more, and any proposal must account for the offset that does not appear on '
                              'the statement [ZRmKamGyTPc @ 00:05:30]. Card mix decides whether a '
                              'surcharge is worth running. Anthony says a merchant that takes mostly '
                              'credit recoups a lot of its fees, but a debit-heavy shop gets some help, '
                              'not a lot [KsqD8Ch93YI @ 00:16:00]. Australia shows what happens once '
                              'pass-through is banned. Sina Cleg says she cannot charge $5.58 for a '
                              'coffee, so businesses round prices up past their actual cost. As a result, '
                              'consumers pay more than they did under the old surcharge, and cash payers '
                              'now carry the card cost too [mlRKCgDApCY @ 00:01:02].'],
               'table': {'caption': 'Firsthand traps, losses, and bottlenecks reported by practitioners',
                         'headers': ['Trap',
                                     'What Practitioners Saw Firsthand',
                                     'Reported Cost or Fix',
                                     'Expert Source'],
                         'rows': [['Card-brand secret shopper fines',
                                   'Ryan Anthony has personally seen merchants fined after shoppers '
                                   'photographed receipts, menus, and invoices',
                                   '$1,000 first fine, $5,000 more if not fixed within 30 to 45 days, and '
                                   'reports of $25,000 per incident',
                                   'Ryan Anthony ([KsqD8Ch93YI @ 00:11:14])'],
                                  ['Non-compliant zero-fee setups',
                                   'SwipeNow sees many businesses running zero-fee programs that do not '
                                   'follow card brand guidelines',
                                   'Those merchants risk having their merchant accounts turned off '
                                   'entirely by the processor',
                                   'SwipeNow Payments ([9ldQhQgiuEY @ 00:03:27])'],
                                  ['Hidden dual pricing statements',
                                   'James Shepherd sees statements showing only $28.95 in total fees on '
                                   '$30,000 of monthly volume',
                                   'The merchant is actually paying far more, so assume the hidden offset '
                                   'exists when building any proposal',
                                   'CCSalesPro ([ZRmKamGyTPc @ 00:05:30])'],
                                  ['Offset math miscalculation',
                                   'A 3.99% card price lifts $100,000 of monthly volume to $103,990 of '
                                   'processed volume',
                                   'The processor must bill roughly 3.84%, not 3.99%, for the $3,990 to '
                                   'offset cleanly',
                                   'CCSalesPro ([ZRmKamGyTPc @ 00:03:07])'],
                                  ['ACH limits in card-not-present dual pricing',
                                   'Agents report that ACH funding time and transaction-size limits are '
                                   'the biggest disappointment when selling service businesses',
                                   "Payroc's simplified ACH tier allows up to $2,000 a day and $500 per "
                                   'transaction without three months of bank statements',
                                   'CCSalesPro ([gBwNpKmRuWY @ 00:40:33])'],
                                  ['Cash share is too small to carry a cash discount',
                                   "Sina Cleg's Sydney bakery went from 40% cash customers to only about 7 "
                                   'or 8%',
                                   'She will slightly raise prices and offer a cash discount because the '
                                   'cost cannot be absorbed',
                                   'ABC News (Australia) ([mlRKCgDApCY @ 00:01:50])'],
                                  ['Merchants dropping credit cards entirely after a ban',
                                   "Australia's tax office said it would refuse all credit card payments "
                                   'rather than absorb the processing cost',
                                   "Macquarie's DEFT rent system also blocked credit cards, leaving "
                                   'renters and businesses without the option',
                                   'News24 ([AE1F8LcgZ98 @ 00:00:34])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Pitfalls Practitioners Say to Fix Before Turning On Any '
                                    'Pass-Through Program',
                           'body': 'Practitioners report that each of these mistakes has led to card-brand '
                                   'fines, frozen accounts, or programs that do not actually offset the '
                                   "merchant's fees.",
                           'items': ['Make sure the terminal or POS software stops any surcharge on a '
                                     'debit card, whether the customer enters a PIN or the card is run as '
                                     'credit; a debit card is a debit card [Ryan Anthony — KsqD8Ch93YI @ '
                                     '00:07:07].',
                                     'Make every price exist twice — on shelf labels, menus, the website, '
                                     'and even quotes — and make sure the POS stores two real prices '
                                     'rather than adding a percentage at the till [POS Nexus — ZAtYPaS2xkA '
                                     '@ 00:01:04].',
                                     'Remove any non-cash adjustment fee that gets added and then '
                                     'discounted back off for cash, because the card brands treat it as an '
                                     'effective surcharge subject to the 3% cap and the debit ban [Ryan '
                                     'Anthony — KsqD8Ch93YI @ 00:12:13].',
                                     "Calculate the merchant's effective rate (total card fees divided by "
                                     'card sales) first; if it is lower than expected, passing the cost on '
                                     'may not be worth it [POS Nexus — ZAtYPaS2xkA @ 00:02:07].']}}],
 'pull_quote': '"If you post the cash price and add a card fee at the till, it\'s a surcharge, whatever '
               'it\'s called." — POS Nexus (ZAtYPaS2xkA @ 00:01:24).',
 'diagram_id': 'diag-05',
 'action_checklist': ["Calculate the merchant's effective rate (total card fees divided by card sales) "
                      "before adding any card fee, and check the state's rules [POS Nexus — m1nRWuyd4rI @ "
                      '00:02:30].',
                      'If surcharging, apply it to credit only, keep it at or under cost and 3%, give the '
                      "acquirer 30 days' notice, post signs at the door and the till, and show the fee as "
                      'its own line on the receipt [POS Nexus — m1nRWuyd4rI @ 00:00:36].',
                      'For retail dual pricing, use a label gun that calculates the 3% or 4% difference '
                      'and prints the cash price and the card price on one label [Global Legal Law Firm — '
                      'rj9tjHr1nNo @ 00:08:47].',
                      'For restaurant merchants, offer to redo and pay for the menus so that every item '
                      'shows two prices and the restaurant becomes compliant [Global Legal Law Firm — '
                      'rj9tjHr1nNo @ 00:10:55].',
                      'For card-not-present merchants, send invoices that link to a hosted payment page '
                      'showing an ACH price and a card price, so the customer chooses how to pay '
                      '[CCSalesPro — gBwNpKmRuWY @ 00:27:03].',
                      "To open the dual pricing conversation, ask the owner whether a gas station's "
                      'separate cash and card prices are dishonest, then ask why the station does it '
                      '[CCSalesPro — gBwNpKmRuWY @ 00:39:11].'],
 'statutory_citations': [{'title': 'Ryan Anthony — How to Legally Offset Credit Card Processing Fees '
                                   '[00:11:14]',
                          'url': 'https://www.youtube.com/watch?v=KsqD8Ch93YI&t=674s',
                          'relevance': 'Primary practitioner testimony on card-brand fines from $1,000 to '
                                       '$25,000, the non-cash adjustment trap, and the dual pricing, cash '
                                       'discount, and surcharge ranking.'},
                         {'title': 'POS Nexus — Can You Charge a Credit Card Fee? Surcharge Rules + the '
                                   'Visa/Mastercard Settlement [00:00:36]',
                          'url': 'https://www.youtube.com/watch?v=m1nRWuyd4rI&t=36s',
                          'relevance': 'Primary practitioner testimony on credit-only surcharging, the cap '
                                       'at cost or 3%, 30-day acquirer notice, signage, receipt '
                                       'itemization, and the pending settlement.'},
                         {'title': 'Global Legal Law Firm — Dual Pricing Done Right: 2026 Practical Guide '
                                   'To Cash Discount And Surcharging Compliance | PEP106 [00:10:19]',
                          'url': 'https://www.youtube.com/watch?v=rj9tjHr1nNo&t=619s',
                          'relevance': 'Primary practitioner testimony on California restaurant '
                                       'service-fee exposure, two-price menus, secret shopper fines, and '
                                       'the failed attempt to sue Visa.'},
                         {'title': 'CCSalesPro — Selling Card Not Present Merchants on Dual Pricing and '
                                   'Surcharging [00:42:48]',
                          'url': 'https://www.youtube.com/watch?v=gBwNpKmRuWY&t=2568s',
                          'relevance': 'Primary practitioner testimony on card-not-present dual pricing '
                                       'with ACH and card prices on the hosted payment page, and on why '
                                       'ACH is required for compliance.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'rj9tjHr1nNo',
                       'title': 'Dual Pricing Done Right: 2026 Practical Guide To Cash Discount And '
                                'Surcharging Compliance | PEP106',
                       'channel': 'Global Legal Law Firm',
                       'author': 'Global Legal Law Firm',
                       'text': "I think almost every business has a problem unless you're doing the dual "
                               "pricing, because the surcharge doesn't cover the spread and you can't do "
                               'it on a debit card.',
                       'tip': "I think almost every business has a problem unless you're doing the dual "
                              "pricing, because the surcharge doesn't cover the spread and you can't do it "
                              'on a debit card.',
                       'timestamp': 639,
                       'timestamp_seconds': 639,
                       'timestamp_label': '[00:10:39]',
                       'url': 'https://www.youtube.com/watch?v=rj9tjHr1nNo&t=639s',
                       'markdown': '[00:10:39](https://www.youtube.com/watch?v=rj9tjHr1nNo&t=639s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HlgVERn_rhY',
                       'title': 'Eliminate Your Merchant Services Fees with Dual Pricing! #dualpricing '
                                '#merchantservices',
                       'channel': 'Electronic Money Company',
                       'author': 'Electronic Money Company',
                       'text': 'Cash discounting means you post a sign that says all your prices are cash '
                               'prices, and if you pay with another tender like a credit card then there '
                               "is a fee added on, and typically the fee is 4%, that's the maximum you can "
                               'add on.',
                       'tip': 'Cash discounting means you post a sign that says all your prices are cash '
                              'prices, and if you pay with another tender like a credit card then there is '
                              "a fee added on, and typically the fee is 4%, that's the maximum you can add "
                              'on.',
                       'timestamp': 83,
                       'timestamp_seconds': 83,
                       'timestamp_label': '[00:01:23]',
                       'url': 'https://www.youtube.com/watch?v=HlgVERn_rhY&t=83s',
                       'markdown': '[00:01:23](https://www.youtube.com/watch?v=HlgVERn_rhY&t=83s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZRmKamGyTPc',
                       'title': 'What is Dual Pricing? | Payment Insights',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': "If you actually take 3,990 divided by 103,990, you're not going to get "
                               "3.99%, you're going to get like 3.84%.",
                       'tip': "If you actually take 3,990 divided by 103,990, you're not going to get "
                              "3.99%, you're going to get like 3.84%.",
                       'timestamp': 187,
                       'timestamp_seconds': 187,
                       'timestamp_label': '[00:03:07]',
                       'url': 'https://www.youtube.com/watch?v=ZRmKamGyTPc&t=187s',
                       'markdown': '[00:03:07](https://www.youtube.com/watch?v=ZRmKamGyTPc&t=187s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MTRmzsfsHTs',
                       'title': 'Saving Money on Credit Card Processing Fees | Merchant Services | Credit '
                                'Card Terminal',
                       'channel': 'Electronic Money Company',
                       'author': 'Electronic Money Company',
                       'text': "Savings on B2B and B2G cards averages 8%, that's just shy of 1% on these "
                               'types of transactions.',
                       'tip': "Savings on B2B and B2G cards averages 8%, that's just shy of 1% on these "
                              'types of transactions.',
                       'timestamp': 147,
                       'timestamp_seconds': 147,
                       'timestamp_label': '[00:02:27]',
                       'url': 'https://www.youtube.com/watch?v=MTRmzsfsHTs&t=147s',
                       'markdown': '[00:02:27](https://www.youtube.com/watch?v=MTRmzsfsHTs&t=147s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KsqD8Ch93YI',
                       'title': 'How to Legally Offset Credit Card Processing Fees',
                       'channel': 'Ryan Anthony',
                       'author': 'Ryan Anthony',
                       'text': "First fine is $1,000, and if they don't rectify it within the 30 or 45 "
                               'days, they add $5,000 on top of that and then it just goes up from there.',
                       'tip': "First fine is $1,000, and if they don't rectify it within the 30 or 45 "
                              'days, they add $5,000 on top of that and then it just goes up from there.',
                       'timestamp': 674,
                       'timestamp_seconds': 674,
                       'timestamp_label': '[00:11:14]',
                       'url': 'https://www.youtube.com/watch?v=KsqD8Ch93YI&t=674s',
                       'markdown': '[00:11:14](https://www.youtube.com/watch?v=KsqD8Ch93YI&t=674s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KsqD8Ch93YI',
                       'title': 'How to Legally Offset Credit Card Processing Fees',
                       'channel': 'Ryan Anthony',
                       'author': 'Ryan Anthony',
                       'text': 'You cannot do what we call a non-cash adjustment fee, because you add a '
                               'non-cash adjustment and then you just discount it off if they pay cash.',
                       'tip': 'You cannot do what we call a non-cash adjustment fee, because you add a '
                              'non-cash adjustment and then you just discount it off if they pay cash.',
                       'timestamp': 733,
                       'timestamp_seconds': 733,
                       'timestamp_label': '[00:12:13]',
                       'url': 'https://www.youtube.com/watch?v=KsqD8Ch93YI&t=733s',
                       'markdown': '[00:12:13](https://www.youtube.com/watch?v=KsqD8Ch93YI&t=733s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gBwNpKmRuWY',
                       'title': 'Selling Card Not Present Merchants on Dual Pricing and Surcharging',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': "If you're 100% card not present, you are more than likely going to lean "
                               'toward a surcharge type model.',
                       'tip': "If you're 100% card not present, you are more than likely going to lean "
                              'toward a surcharge type model.',
                       'timestamp': 1436,
                       'timestamp_seconds': 1436,
                       'timestamp_label': '[00:23:56]',
                       'url': 'https://www.youtube.com/watch?v=gBwNpKmRuWY&t=1436s',
                       'markdown': '[00:23:56](https://www.youtube.com/watch?v=gBwNpKmRuWY&t=1436s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gBwNpKmRuWY',
                       'title': 'Selling Card Not Present Merchants on Dual Pricing and Surcharging',
                       'channel': 'CCSalesPro',
                       'author': 'CCSalesPro',
                       'text': 'There are some smaller thresholds with that, up to say two thousand '
                               'dollars a day, up to five hundred dollars per transaction.',
                       'tip': 'There are some smaller thresholds with that, up to say two thousand dollars '
                              'a day, up to five hundred dollars per transaction.',
                       'timestamp': 2433,
                       'timestamp_seconds': 2433,
                       'timestamp_label': '[00:40:33]',
                       'url': 'https://www.youtube.com/watch?v=gBwNpKmRuWY&t=2433s',
                       'markdown': '[00:40:33](https://www.youtube.com/watch?v=gBwNpKmRuWY&t=2433s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZAtYPaS2xkA',
                       'title': 'Dual Pricing vs Cash Discount: Is "Zero-Fee" Processing Legal?',
                       'channel': 'POS Nexus',
                       'author': 'POS Nexus',
                       'text': "If you post the cash price and add a card fee at the till, it's a "
                               "surcharge, whatever it's called.",
                       'tip': "If you post the cash price and add a card fee at the till, it's a "
                              "surcharge, whatever it's called.",
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=ZAtYPaS2xkA&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=ZAtYPaS2xkA&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9ldQhQgiuEY',
                       'title': 'ZERO Fee Processing: No Fee Credit Card Processing | What You Need To '
                                'Know',
                       'channel': 'SwipeNow Payments',
                       'author': 'SwipeNow Payments',
                       'text': "There's a lot of businesses out there that are not following the "
                               'guidelines and they risk having their merchant accounts turned off.',
                       'tip': "There's a lot of businesses out there that are not following the guidelines "
                              'and they risk having their merchant accounts turned off.',
                       'timestamp': 207,
                       'timestamp_seconds': 207,
                       'timestamp_label': '[00:03:27]',
                       'url': 'https://www.youtube.com/watch?v=9ldQhQgiuEY&t=207s',
                       'markdown': '[00:03:27](https://www.youtube.com/watch?v=9ldQhQgiuEY&t=207s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'm1nRWuyd4rI',
                       'title': 'Can You Charge a Credit Card Fee? Surcharge Rules + the Visa/Mastercard '
                                'Settlement',
                       'channel': 'POS Nexus',
                       'author': 'POS Nexus',
                       'text': 'Before you add any card fee, run this checklist: know your real cost '
                               'first, your effective rate, total fees divided by card sales.',
                       'tip': 'Before you add any card fee, run this checklist: know your real cost first, '
                              'your effective rate, total fees divided by card sales.',
                       'timestamp': 150,
                       'timestamp_seconds': 150,
                       'timestamp_label': '[00:02:30]',
                       'url': 'https://www.youtube.com/watch?v=m1nRWuyd4rI&t=150s',
                       'markdown': '[00:02:30](https://www.youtube.com/watch?v=m1nRWuyd4rI&t=150s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ahGJLcVvtj0',
                       'title': 'How to Avoid Credit Card Surcharges and Convenience Fees',
                       'channel': 'TODAY',
                       'author': 'TODAY',
                       'text': 'A 2026 study from JD Power found more than one-third of small businesses '
                               'include surcharges for credit card payments, and 32% of places that '
                               'surcharge say customers occasionally or frequently cancel a purchase when '
                               'the charge appears.',
                       'tip': 'A 2026 study from JD Power found more than one-third of small businesses '
                              'include surcharges for credit card payments, and 32% of places that '
                              'surcharge say customers occasionally or frequently cancel a purchase when '
                              'the charge appears.',
                       'timestamp': 102,
                       'timestamp_seconds': 102,
                       'timestamp_label': '[00:01:42]',
                       'url': 'https://www.youtube.com/watch?v=ahGJLcVvtj0&t=102s',
                       'markdown': '[00:01:42](https://www.youtube.com/watch?v=ahGJLcVvtj0&t=102s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CTTa8diTsTU',
                       'title': 'Credit Card Surcharging: What You Need to Know',
                       'channel': 'Merchant Maverick',
                       'author': 'Merchant Maverick',
                       'text': 'Currently, you are not allowed to add a surcharge if you operate in '
                               'Connecticut, Massachusetts, or the territory of Puerto Rico.',
                       'tip': 'Currently, you are not allowed to add a surcharge if you operate in '
                              'Connecticut, Massachusetts, or the territory of Puerto Rico.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=CTTa8diTsTU&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=CTTa8diTsTU&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bBQUixWA9qA',
                       'title': 'What is surcharging? Credit card surcharge rules explained',
                       'channel': 'Nuvei',
                       'author': 'Nuvei',
                       'text': 'The surcharge cannot exceed the cost of accepting the credit card, and '
                               'debit cards and prepaid cards cannot be surcharged.',
                       'tip': 'The surcharge cannot exceed the cost of accepting the credit card, and '
                              'debit cards and prepaid cards cannot be surcharged.',
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=bBQUixWA9qA&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=bBQUixWA9qA&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'COwQpax5fxU',
                       'title': 'Ban on debit and credit card surcharges | The Business | ABC NEWS',
                       'channel': 'ABC News (Australia)',
                       'author': 'ABC News (Australia)',
                       'text': 'This probably is going to change the name, and that cost will appear in '
                               'some other form from the financial institutions.',
                       'tip': 'This probably is going to change the name, and that cost will appear in '
                              'some other form from the financial institutions.',
                       'timestamp': 180,
                       'timestamp_seconds': 180,
                       'timestamp_label': '[00:03:00]',
                       'url': 'https://www.youtube.com/watch?v=COwQpax5fxU&t=180s',
                       'markdown': '[00:03:00](https://www.youtube.com/watch?v=COwQpax5fxU&t=180s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mlRKCgDApCY',
                       'title': 'Businesses may be forced to increase prices as card surcharge ban begins '
                                '| ABC NEWS',
                       'channel': 'ABC News (Australia)',
                       'author': 'ABC News (Australia)',
                       'text': "It's not actually a ban on credit card surcharges, it's just a ban on "
                               "passing them on, so that's another about 1.6% that's coming straight out "
                               "of a small business's profit.",
                       'tip': "It's not actually a ban on credit card surcharges, it's just a ban on "
                              "passing them on, so that's another about 1.6% that's coming straight out of "
                              "a small business's profit.",
                       'timestamp': 28,
                       'timestamp_seconds': 28,
                       'timestamp_label': '[00:00:28]',
                       'url': 'https://www.youtube.com/watch?v=mlRKCgDApCY&t=28s',
                       'markdown': '[00:00:28](https://www.youtube.com/watch?v=mlRKCgDApCY&t=28s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AE1F8LcgZ98',
                       'title': '‘Unintended consequences’: Labor’s credit card surcharge ban sparks '
                                'backlash',
                       'channel': 'News24',
                       'author': 'News24',
                       'text': 'The tax office announced that rather than absorb the cost itself, it would '
                               'instead refuse all credit card payments from November 30.',
                       'tip': 'The tax office announced that rather than absorb the cost itself, it would '
                              'instead refuse all credit card payments from November 30.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=AE1F8LcgZ98&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=AE1F8LcgZ98&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AGTRnXUImOw',
                       'title': 'Are surcharges and convenience charges legal on debit card transactions?',
                       'channel': 'WKYC Channel 3',
                       'author': 'WKYC Channel 3',
                       'text': 'Federal law makes surcharge fees illegal on debit card transactions, even '
                               'if the debit card payment is being processed like a credit card '
                               'transaction without requiring you to enter your PIN.',
                       'tip': 'Federal law makes surcharge fees illegal on debit card transactions, even '
                              'if the debit card payment is being processed like a credit card transaction '
                              'without requiring you to enter your PIN.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=AGTRnXUImOw&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=AGTRnXUImOw&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
