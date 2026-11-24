from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'saas-pricing-architecture-seats-usage-ai-credits-renewal-uplifts',
 'question_prompt': 'How do SaaS vendors structure pricing models and metrics, and how is the shift from '
                    'per-seat to usage and AI pricing changing what buyers pay?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'SaaS Pricing Architecture: Seats, Usage, AI Credits, and Renewal Uplifts',
 'subtitle': 'Pricing structure and packaging, pricing-metric viability, common SaaS pricing models, B2B '
             'pricing strategies and validation, good-pricing signals, hybrid seat/usage pricing in the AI '
             'era, Atlassian Rovo credits, Zendesk/HubSpot token pricing, enterprise pushback on AI '
             'pricing, benchmarking, automated renewal price uplifts, and subscription billing',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the seat is no longer the whole price; it survives as a base '
                      'fee wrapped in credits, metered overage, and contractual uplifts. Hybrid models are '
                      'gaining share, with one Growth Unhinged cut showing hybrid rising from 27% to 41% '
                      'and posting 105% net revenue retention, while AI drags classical 85% to 95% gross '
                      'margins toward roughly 50%. The heaviest users drive losses: a P90 user can cost '
                      'five times a P50 user, and unlimited AI let about 5% of heavy users bleed an '
                      'image-generation company. Street mechanics include fixed or maximum renewal uplifts '
                      'enforced in quoting software, 3% to 7% escalators that open at seven, 60% gross '
                      'margin targets at P50, 90-day repricing, and price-last validation decks. '
                      'Disagreement centers on repricing cadence, whether outcome pricing works, and '
                      'whether hybrids simply revive shelfware risk.',
 'key_metrics': [{'label': 'Hybrid pricing net revenue retention',
                  'metric': 'Hybrid pricing net revenue retention',
                  'value': '105% (vs 102% subscription, 100% outcome, 99% consumption)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Net revenue retention compared across pricing models; hybrid leads, pure '
                             'consumption trails',
                  'source': 'The Innovation Attorney ([ubYfOw6FSPA @ 00:09:42])'},
                 {'label': 'AI-era gross margin compression',
                  'metric': 'AI-era gross margin compression',
                  'value': '85% to 95% classical SaaS gross margin falls to about 50% with AI',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Variable inference cost erodes the near-zero marginal cost that classical '
                             'SaaS margins were built on',
                  'source': 'Champion Leadership ([jOL79tUtq3o @ 00:06:14])'},
                 {'label': 'Post-2020 startups on usage or outcome pricing',
                  'metric': 'Post-2020 startups on usage or outcome pricing',
                  'value': '56%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Share of companies founded after 2020 using usage or outcome pricing, from '
                             '160 coded startups',
                  'source': 'Andrew Garberson ([l1Q6q8yDjTQ @ 00:01:21])'},
                 {'label': 'Contract price escalator range',
                  'metric': 'Contract price escalator range',
                  'value': '3% to 7% per year (Salesforce runs 7%)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Annual uplift founders are told to bake into contracts; uplift outweighs '
                             'churn by a multiple',
                  'source': 'Champion Leadership ([jOL79tUtq3o @ 00:29:27])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus: The Seat Survives Only as a Base Fee',
               'paragraphs': ['The loudest agreement in the field is that per-seat pricing has lost its '
                              'job as the whole price but kept its job as the floor. Soft Learn Hub puts '
                              'it bluntly: what is ending is the seat as the whole price, and the seat '
                              'survives as a base fee, backed by a Stripe survey of 200 leaders in which '
                              'seats as the main model drop from 16% to 11% by 2027 [oDjXoRkYaA0 @ '
                              '00:00:51]. The Innovation Attorney lands on the same shift with Growth '
                              'Unhinged data: seat-based pricing fell from 21% to 15% while hybrid jumped '
                              'from 27% to 41%, a mix where the seat survives inside the bundle rather '
                              'than disappearing [ubYfOw6FSPA @ 00:10:35]. Andrew Garberson coded 160 '
                              'startups, reviewed 20 CRM leaders, and found 56% of companies founded after '
                              '2020 running usage or outcome pricing, with Lightfield on credits and Attio '
                              'stacking seats plus credits [l1Q6q8yDjTQ @ 00:01:21]. Roland Umlauft of '
                              'Ultimate CFO names the engine behind the move: an efficiency paradox in '
                              'which better AI means fewer seats sold, layered on AI compute that is '
                              'variable instead of near-zero, which has pushed seat pricing down and usage '
                              'components into contracts over the last 12 to 24 months [xmq83cmzth4 @ '
                              '00:02:28].',
                              'The second point of consensus is that the heaviest users are where margin '
                              'bleeds out, and unlimited AI is the fastest way to find them. Roee Hartuv '
                              'on Champion Leadership anchors the math: classical SaaS was built on 85% to '
                              '95% gross margin, and AI drags that toward roughly 50% [jOL79tUtq3o @ '
                              "00:06:14]. Hartuv's cautionary case is an image-generation company that "
                              'granted unlimited AI and then bled money from roughly 5% of heavy users '
                              '[jOL79tUtq3o @ 00:08:45]. The Innovation Attorney quantifies the same tail '
                              'with a worked unit model: at $0.035 per action, the P50 user costs $4.20 a '
                              'month while the P90 user costs $21.00, a 5:1 spread against a $29 price '
                              'point, and the trigger rule is to move to usage or hybrid once inference '
                              'cost per customer varies by more than roughly 3:1 [ubYfOw6FSPA @ 00:11:51]. '
                              'Andrew Garberson turns the tail into a dashboard item: track margin on the '
                              'top 10% of accounts and split expansion revenue out so you can see whether '
                              'the unit is actually working [l1Q6q8yDjTQ @ 00:06:08]. Three operators, '
                              'three lenses on the same distribution, one verdict: price the tail '
                              'deliberately, cap it, or meter it, because a flat seat fee lets a small '
                              'cohort of power users eat the margin everyone else generates.',
                              'The third agreement concerns the metric itself and the order in which a '
                              'buyer sees it. Willingness to Pay insists a metric must be non-arbitrary '
                              'and countable by a computer, invoiceable against an account in a timely '
                              'way, and auditable down to showing a customer 1M API calls if challenged; '
                              'the drill is to generate 50 to 100 candidate metrics and kill every one '
                              'that fails [rTGrwbYBlXg @ 00:07:31]. Andrew Garberson runs the same filter '
                              'from the buyer side: does the customer already count this unit, the way Fin '
                              'counts resolutions, Gorgias counts tickets and Ashby counts headcount, and '
                              'can you say it in one sentence, a test that vague 50-credit bundles fail '
                              '[l1Q6q8yDjTQ @ 00:01:56]. On sequencing, Willingness to Pay wants the '
                              'customer nodding through value proposition, packaging, features and metric '
                              'logic before any price appears, so friction lands only at the price point, '
                              'one friction point instead of four [tNlpy7MZ8Vk @ 00:01:02]. The longer '
                              'validation training makes that order mandatory, with packaging shown only '
                              "as $/$$/$$$ placeholders and the line 'assume the price is fair' used to "
                              'isolate reaction to the model itself, because if buyers hate the model it '
                              'does not matter whether the percentage is 1, 2 or 10 [Ieuyh9RZzvM @ '
                              '00:18:26].'],
               'table': {'caption': 'Where the practitioners converge on seats, hybrids, heavy users, and '
                                    'metric discipline',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['The seat survives only as a base fee',
                                   'Seats as the main model fall from 16% to 11% by 2027 across 200 '
                                   'surveyed leaders',
                                   'Keep a seat floor and layer credits or metered overage on top of it',
                                   'Soft Learn Hub ([oDjXoRkYaA0 @ 00:00:51])'],
                                  ['Hybrid models are taking share from pure seats',
                                   'Seat-based fell from 21% to 15% while hybrid rose from 27% to 41%',
                                   'Default new AI packaging to a base seat with allotment plus overage',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:10:35])'],
                                  ['Newer companies have already moved past per-seat pricing',
                                   '56% of companies founded after 2020 use usage or outcome pricing '
                                   'models',
                                   'Benchmark your unit against Lightfield credits and Attio seats plus '
                                   'credits',
                                   'Andrew Garberson ([l1Q6q8yDjTQ @ 00:01:21])'],
                                  ['AI compresses the classical SaaS gross margin profile',
                                   'Classical SaaS ran 85% to 95% gross margin; AI pulls it near 50%',
                                   'Track unit economics per individual user, not just per product line',
                                   'Champion Leadership ([jOL79tUtq3o @ 00:06:14])'],
                                  ['The heavy-user tail drives the losses on flat pricing',
                                   'At $0.035 per action, P90 costs $21.00 monthly versus $4.20 for P50',
                                   'Move to usage or hybrid once per-customer cost spread passes roughly '
                                   '3:1',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:11:51])'],
                                  ['The pricing metric must be countable and auditable',
                                   'Non-arbitrary, counted by a computer, invoiceable, and provable down '
                                   'to 1M API calls',
                                   'Generate 50 to 100 candidate metrics and drop every one that fails',
                                   'Willingness to Pay ([rTGrwbYBlXg @ 00:07:31])'],
                                  ['Price is shown last in every validation conversation',
                                   'Buyer nods through value, packaging, features and metric; friction '
                                   'lands at price',
                                   'Build the five-slide deck with actual prices on the final slide only',
                                   'Willingness to Pay ([tNlpy7MZ8Vk @ 00:01:02])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers: Uplifts, Credit Wallets, and Margin '
                        'Floors',
               'paragraphs': ['Renewal uplifts are the cheapest revenue on the table and the easiest to '
                              "lose. MonetizeNow's workflow launches the quote from the Salesforce "
                              'opportunity, opens a Renewal Uplift section, and sets a percentage as '
                              'either fixed or maximum, the maximum acting as a ceiling for negotiation or '
                              "CPI; in the demo a 5% uplift is saved and the quote prints 'renewal price "
                              "includes a fixed 5% increase' [x0K0bAATQIA @ 00:00:41]. At renewal the "
                              "operator picks end-of-term or early 'rip and replace,' accepting the "
                              'renewal locks out further amendments, and an account-specific rate carries '
                              'the price from $100 to $105 per user per month automatically [x0K0bAATQIA @ '
                              '00:03:06]. Roee Hartuv supplies the negotiating posture: Salesforce runs a '
                              '7% annual escalator, founders should bake 3% to 7% into contracts, and the '
                              "opening number matters because, in Hartuv's words, start at seven and then "
                              'procurement will take you down to four [jOL79tUtq3o @ 00:31:08]. IWI '
                              "Consulting Group's David Apple covers the back office: keep one "
                              'subscription system of record synced natively with Salesforce and CPQ, so '
                              'new sale, upsell and renewal sit in one place and post straight into the '
                              'native general ledger [s-VGS7d821o @ 00:01:05].',
                              'AI credits and hybrid meters are where the pricing architecture gets '
                              'mechanical. The Innovation Attorney lists the stack required before '
                              'shipping any of it: metering, a rating engine, a credit wallet, and '
                              'invoicing with dunning, with Orb and Metronome named as the vendors '
                              '[ubYfOw6FSPA @ 00:07:13]. The reference build is Salesforce Agentforce '
                              'running three models: $2.00 per conversation from October 2024, '
                              '$0.10-per-action Flex Credits from May 2025, and $125 per user per month '
                              'AELA seats, with all three live simultaneously, so one buyer can be metered '
                              'per conversation, per action and per seat inside the same vendor '
                              'relationship [ubYfOw6FSPA @ 00:08:34]. Soft Learn Hub tracks the '
                              'seat-plus-credit pattern spreading: from December 3 Atlassian bills Rovo '
                              'overage at 1 cent per credit with overage on by default, Jira Premium '
                              'includes 70 credits per user per month, and Monday.com requires an AI '
                              'credit bundle [oDjXoRkYaA0 @ 00:01:08]. Willingness to Pay reframes the '
                              'wallet itself: credit-based systems are essentially usage-based pricing '
                              'paid up front, expiry and churn rules have to be defined before launch, and '
                              'training credits can roll over, 100 plus 20 for a balance of 120 '
                              '[BGb6-WKMNN4 @ 00:08:54].',
                              'Validation and margin control close the loop. The Innovation Attorney sets '
                              'the margin bar at no less than 60% gross margin at P50 users, inside a 50% '
                              'to 70% band, and runs repricing on a roughly 90-day cycle rather than '
                              'treating the price as a one-time launch decision [ubYfOw6FSPA @ 00:21:13]. '
                              'Willingness to Pay runs pilots as a 100-day sequence: 10 days of '
                              'integrations, a 60-day trial, and a 30-day KPI workshop with an opt-out, '
                              'with the customer signing the full subscription on day one, for example EUR '
                              '10 per employee, and the pitch going to the real buyer rather than a 20K '
                              'gatekeeper; otherwise, the training warns, the pilot is just internal '
                              'marketing [BGb6-WKMNN4 @ 00:02:02]. In validation interviews, the same '
                              "channel's rule after showing the price point is to shut up and wait while "
                              'the customer self-calculates and reaches for a comparator, pre-calculating '
                              'only when the math is hard; budget or rival software as the comparator '
                              'signals friction, while savings signals you are in business [Ieuyh9RZzvM @ '
                              '00:12:49]. The sample is small by design: 5 to 10 interviews per fence, not '
                              '50, run by salespeople as narration practice, and the channel says it has '
                              'never seen a product with green lights at every step fail a sales test '
                              '[Ieuyh9RZzvM @ 00:19:35].'],
               'table': {'caption': 'Street mechanics: exact settings, price points, and execution details',
                         'headers': ['Mechanic',
                                     'Exact Numbers & Settings',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['Renewal uplift configured at quote time',
                                   'Fixed or maximum percentage; the demo saves a fixed 5% uplift',
                                   'Set it inside the quote launched from the Salesforce opportunity',
                                   'MonetizeNow ([x0K0bAATQIA @ 00:00:41])'],
                                  ['Uplift carried forward into the renewal',
                                   '$100 moves to $105 per user per month via account-specific rate',
                                   'Accepting the renewal blocks further amendments, so finalize terms '
                                   'first',
                                   'MonetizeNow ([x0K0bAATQIA @ 00:03:06])'],
                                  ['Escalator anchoring against procurement teams',
                                   'Salesforce runs 7% yearly; bake 3% to 7% into every contract',
                                   'Open at seven so procurement negotiates you down to four',
                                   'Champion Leadership ([jOL79tUtq3o @ 00:31:08])'],
                                  ['Concurrent multi-meter AI agent pricing',
                                   '$2.00 per conversation, $0.10 per action Flex Credits, $125 per user '
                                   'AELA',
                                   'Salesforce Agentforce runs all three pricing models at the same time',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:08:34])'],
                                  ['Base fee with included premium request allotment',
                                   'Copilot charges $10 base, 300 premium requests, then $0.04 each',
                                   'Include an allotment in the base and meter every request beyond it',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:19:39])'],
                                  ['Credit overage switched on by default',
                                   'Atlassian Rovo overage billed at 1 cent per credit from December 3',
                                   'Overage runs on by default unless the buyer actively turns it off',
                                   'Soft Learn Hub ([oDjXoRkYaA0 @ 00:00:00])'],
                                  ['Flat fee that raises the revenue floor',
                                   '$1,000 flat plus $10 per user lifts the minimum deal value',
                                   'Add a usage metric only once ACV clears a couple thousand euros',
                                   'Willingness to Pay ([BGb6-WKMNN4 @ 00:06:12])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the Money Hides in Uplifts, Fees, and Meters',
                           'body': 'The operators who extract the most from SaaS pricing treat the renewal '
                                   'clause, the fee lines, and the overage meter as negotiable surfaces in '
                                   'their own right, not as fine print.',
                           'items': ['Use the maximum uplift setting as a ceiling for negotiation or CPI '
                                     'instead of a fixed rate when the buyer is expected to haggle at '
                                     'renewal [MonetizeNow — x0K0bAATQIA @ 00:00:21].',
                                     'Open escalator talks at seven percent; procurement will take you '
                                     'down to four, so the high anchor is what protects the uplift '
                                     '[Champion Leadership — jOL79tUtq3o @ 00:31:08].',
                                     'Infrastructure fees moved one insurtech from roughly 60M to 100M DKK '
                                     'ARR across 30 customers, a 60 raise with no churn [Willingness to '
                                     'Pay — BGb6-WKMNN4 @ 00:28:52].',
                                     'On the buying side, find every meter, set alerts at 80% and 100%, '
                                     'and negotiate rollover, locked overage pricing, and a contractual '
                                     'cap [Soft Learn Hub — oDjXoRkYaA0 @ 00:02:18].']},
               'sop_steps': [{'step': 1,
                              'title': 'Map every meter and cap it',
                              'action': 'Inventory all seat, credit, and overage meters on the account and '
                                        'set spend caps with alerts.',
                              'detail': 'Find every meter, set caps with alerts at 80% and 100%, track '
                                        'cost per outcome by dividing the AI bill by tickets resolved or '
                                        'tasks done, and negotiate rollover plus locked overage pricing '
                                        '[Soft Learn Hub — oDjXoRkYaA0 @ 00:02:18].'},
                             {'step': 2,
                              'title': 'Model the P50 versus P90 cost spread',
                              'action': 'Price cost per action against the median and heavy user before '
                                        'setting the seat price.',
                              'detail': 'At $0.035 per action a P50 user costs $4.20 monthly and a P90 '
                                        'user $21.00, a 5:1 spread against a $29 price; move to usage or '
                                        'hybrid once spread passes roughly 3:1 [The Innovation Attorney — '
                                        'ubYfOw6FSPA @ 00:11:51].'},
                             {'step': 3,
                              'title': 'Lock the renewal uplift into the quote',
                              'action': 'Configure a fixed or maximum uplift percentage at quote time so '
                                        'renewals price automatically.',
                              'detail': 'In the Renewal Uplift section choose fixed or maximum, save the '
                                        'percentage such as 5%, and let the account-specific rate carry '
                                        '$100 to $105 per user per month so the uplift is never missed '
                                        '[MonetizeNow — x0K0bAATQIA @ 00:00:21].'},
                             {'step': 4,
                              'title': 'Validate with a price-last deck and silence',
                              'action': 'Run 5 to 10 interviews per fence, showing prices last, then stop '
                                        'talking.',
                              'detail': 'After the price slide, shut up and wait while the customer '
                                        'self-calculates and picks a comparator; budget or rival software '
                                        'means friction, savings means you are in business [Willingness to '
                                        'Pay — Ieuyh9RZzvM @ 00:12:49].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over the billing unit itself. The Innovation Attorney '
                              'sets a hard trigger: move to usage or hybrid pricing once inference cost '
                              'per customer varies by more than roughly 3:1, then decide on P90 margin, '
                              'deal size and forecastability [ubYfOw6FSPA @ 00:00:17]. Their scoreboard '
                              'has hybrid winning net revenue retention at 105% against subscription at '
                              '102%, outcome at 100% and consumption at 99%, so the model with the most '
                              'flexible meter is not the one that keeps customers best [ubYfOw6FSPA @ '
                              "00:09:42]. Roland Umlauft of Ultimate CFO argues from the buyer's chair: "
                              'enterprise finance teams treat 40% month-over-month invoice swings as a '
                              'nightmare and are demanding predictability even at the expense of the '
                              'theoretical efficiency gains from usage-based pricing [xmq83cmzth4 @ '
                              '00:04:52]. Soft Learn Hub lands between the camps with the cleanest '
                              'framing: what is ending is the seat as the whole price, and the seat '
                              'survives as a base fee sitting under credits, per-resolution charges or '
                              'multi-year enterprise flat fees [oDjXoRkYaA0 @ 00:02:53]. The operator read '
                              'is to treat seat versus usage as a false binary: pick a seat floor buyers '
                              'can budget for, then meter the variable cost on top so heavy users fund '
                              'their own compute.',
                              'Outcome pricing is where the practitioners openly contradict each other. '
                              'The Innovation Attorney logs Salesforce Agentforce running three models at '
                              'once: $2.00 per conversation from October 2024, $0.10-per-action Flex '
                              'Credits from May 2025, and $125 per user per month AELA seats [ubYfOw6FSPA '
                              '@ 00:08:34]. Roee Hartuv on Champion Leadership tells it differently, '
                              'saying Salesforce tried outcome pricing, it did not work, and it is now '
                              'back to usage, because outcomes are hard to measure, with ChatGPT recipes '
                              'versus Excel work as the example [jOL79tUtq3o @ 00:10:27]. Umlauft reports '
                              "the move as Agentforce shifting from consumption-only to a buyer's choice "
                              'of consumption, flex credits or per-user [xmq83cmzth4 @ 00:05:52]. '
                              'Meanwhile outcome prices keep compressing in the market: HubSpot charges 50 '
                              'cents per resolution with escalations free and Intercom charges 99 cents '
                              '[oDjXoRkYaA0 @ 00:01:25]. The credit unit splits the room too. Willingness '
                              'to Pay calls credits usage-based pricing paid up front, workable if expiry '
                              'and churn rules are defined, while Hartuv warns against made-up token units '
                              'and Garberson fails credit bundles like 50 credits on the one-sentence '
                              "test. Hartuv's fallback is a plain hybrid of a base fee plus credits, "
                              'emails or API calls.',
                              'Cadence and positioning split the field as well. The Innovation Attorney '
                              'reprices roughly every 90 days against a target of at least 60% gross '
                              'margin at P50 users [ubYfOw6FSPA @ 00:22:19], while Hartuv reviews pricing '
                              'per product version or per sales cycle and insists somebody must own it '
                              '[jOL79tUtq3o @ 00:28:03]. On price level, Ulrik of Willingness to Pay runs '
                              'two opposite plays: shrink the market by halving price, turning a $1B '
                              'market into $0.5B but winning around 30% of it, or go premium, where a '
                              'price of 20 with triple CAC and triple delivery still leaves 7 in profit '
                              'versus 5 at a price of 10 [cdQzCVUJybY @ 00:04:53]. The non-negotiable is '
                              "the closing line: whatever you do, don't try to just be in the middle "
                              '[cdQzCVUJybY @ 00:11:59]. The same channel also pushes back on '
                              'recurring-revenue purism, telling founders not to get too married to the '
                              'idea, because money is money and start, ad-hoc and exit fees can sit beside '
                              "the subscription. Rob Walling's survey shows where independent founders "
                              'actually sit: about 47% monthly and 36% annual, with metered at 6.6% and '
                              'revenue share near 2.3%. Pick an extreme on price, then choose the review '
                              'cadence your margin volatility demands.'],
               'table': {'caption': 'Side-by-side playbooks where practitioners split on units, cadence '
                                    'and price level',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Primary billing unit for AI-heavy products',
                                   'Move to usage or hybrid once inference cost per customer varies more '
                                   'than about 3:1',
                                   'Copilots stay seat-based while automation moves to usage or outcome '
                                   'pricing',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:00:17]); Ultimate CFO '
                                   '([xmq83cmzth4 @ 00:07:42])'],
                                  ['Salesforce Agentforce pricing history and current state',
                                   'Three models at once: $2.00 per conversation, $0.10 Flex Credits, $125 '
                                   'AELA seats',
                                   'Outcome pricing did not work and Salesforce is now back to usage',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:08:34]); Champion '
                                   'Leadership ([jOL79tUtq3o @ 00:10:27])'],
                                  ['Credits as the metered unit inside a hybrid',
                                   'Credits are usage-based pricing paid up front, with expiry and churn '
                                   'rules defined',
                                   'Ambiguous bundles like 50 credits fail the one-sentence explanation '
                                   'test',
                                   'Willingness to Pay ([BGb6-WKMNN4 @ 00:08:54]); Andrew Garberson '
                                   '([l1Q6q8yDjTQ @ 00:04:43])'],
                                  ['How often to revisit the price book',
                                   'Reprice roughly every 90 days against at least 60% gross margin at P50',
                                   'Review at each product version or each sales cycle, with a named owner',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:22:19]); Champion '
                                   'Leadership ([jOL79tUtq3o @ 00:28:03])'],
                                  ['Price level and market positioning strategy',
                                   'Shrink the market: halve price, turn $1B into $0.5B, win about 30%',
                                   'Go premium: price 20 with 3x CAC and 3x delivery still leaves 7 profit',
                                   'Willingness to Pay ([cdQzCVUJybY @ 00:01:48]); Willingness to Pay '
                                   '([cdQzCVUJybY @ 00:04:53])'],
                                  ['Validation sample size before a sales test',
                                   'Interview 5 to 10 customers per fence, not 50, in 30-45 minute '
                                   'sessions',
                                   'Pilot AI features with 5 to 20 customers under a fair-use cap',
                                   'Willingness to Pay ([Ieuyh9RZzvM @ 00:19:35]); Champion Leadership '
                                   '([jOL79tUtq3o @ 00:18:01])'],
                                  ['Recurring subscription versus transactional fee revenue mix',
                                   'Monthly about 47% and annual about 36% of independent SaaS, annual '
                                   'often 12 for 10',
                                   "Don't get too married to recurring revenue; start, ad-hoc and exit "
                                   'fees count',
                                   'Rob Walling ([lC6Gpn0ugFI @ 00:01:21]); Willingness to Pay '
                                   '([BGb6-WKMNN4 @ 00:01:43])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive mistake on record is handing out unlimited AI. Hartuv '
                              'describes an image-generation company that bled money after granting '
                              'unlimited usage, with roughly 5% of heavy users driving the losses, against '
                              'a backdrop where classical SaaS gross margin of 85% to 95% falls to about '
                              '50% once AI compute enters the stack [jOL79tUtq3o @ 00:08:45]. The '
                              'Innovation Attorney quantifies the same tail: at $0.035 per action, a P50 '
                              'user costs $4.20 a month and a P90 user $21.00, a 5:1 spread sitting under '
                              'a $29 price [ubYfOw6FSPA @ 00:11:51]. Flip the meter onto the customer and '
                              'the blowups move to their side: a Cursor $7,000 annual plan consumed in one '
                              'day, and Replit charging $1,000 a week against a usual $180 to $200 '
                              '[ubYfOw6FSPA @ 00:15:39]. Umlauft adds that actual costs exceed vendor '
                              'estimates by 30% to 50%, and buyers are pushing back [xmq83cmzth4 @ '
                              "00:04:03]. Garberson's fix is to watch the top 10% of accounts by margin "
                              'and split expansion revenue so you can see whether the unit is working. '
                              "Hartuv's launch discipline is a fair-use policy to cap losses, then a pilot "
                              'with 5 to 20 customers before measuring value and cost.',
                              'Renewal uplifts leak quietly. MonetizeNow calls enforcement the tricky part '
                              'under manual ops and says uplifts that are not automated simply get missed, '
                              'which is revenue leakage [x0K0bAATQIA @ 00:03:28]. Their fix stores the '
                              'uplift as a fixed or maximum percentage on the quote, so a $100 per user '
                              'per month seat rolls to $105 automatically through an account-specific '
                              'rate, and accepting the renewal blocks further amendments. Hartuv argues '
                              'that uplift outweighs churn by a multiple, points to Salesforce at 7% a '
                              'year, and coaches founders to bake 3% to 7% into contracts, with the blunt '
                              'negotiating line: start at seven and then procurement will take you down to '
                              'four [jOL79tUtq3o @ 00:31:08]. The price-cut trap runs the other way. '
                              "Ulrik's warning is Rackspace, whose roughly 33% cut was simply matched by "
                              'AWS [cdQzCVUJybY @ 00:07:15]. On the fee side, Willingness to Pay reports '
                              'the upside of getting fairness right: an insurtech went from roughly 60M to '
                              'roughly 100M DKK ARR on 30 customers by adding infrastructure fees, summed '
                              'up as raising prices 60 with no churn [BGb6-WKMNN4 @ 00:29:59]. Uplift and '
                              'fee lines only stick when they are written into the quote and the contract.',
                              'Packaging and metric errors kill deals before price is ever discussed. '
                              'Willingness to Pay saw the Lifegen density trap firsthand: 1M cases at a '
                              '€20 average, but 700K of them were zero-value, which invites sorting of '
                              'volume worth 1.4M [BGb6-WKMNN4 @ 00:47:11]. The same channel reports a '
                              'recruitment client whose cost-per-recruiter job-to-be-done was rejected '
                              'because recruiters wanted volume throughput, and warns that when buyers '
                              'hate the model it does not matter whether the percentage is one, two or 10% '
                              '[Ieuyh9RZzvM @ 00:10:41]. Hartuv caught a Claude-built pricing table '
                              'proposing an $89-a-month tier, about $1K a year, against a $12K ACV, which '
                              'would cannibalize revenue [jOL79tUtq3o @ 00:34:50]. Umlauft flags the '
                              'hybrid trap: credit caps and fair-use thresholds bring shelfware risk back, '
                              'and without process redesign AI software becomes the most expensive '
                              'shelfware enterprises have ever purchased [xmq83cmzth4 @ 00:07:22]. On the '
                              'reporting side, The SaaS CFO warns that aggregate benchmarks pooling '
                              'million-dollar and $10-a-month products mislead, and that an enterprise '
                              'business cannot be benchmarked against a self-service one. Segment by ACV '
                              'first, then compare against top, median and bottom quartiles of companies '
                              'with a similar profile, using data sets like BenchmarkIt.'],
               'table': {'caption': 'Firsthand failure modes with the economics check practitioners '
                                    'attached to each',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Unlimited AI granted to every single user',
                                   'An image-generation company bled money from roughly 5% heavy users',
                                   'AI drags 85-95% classical SaaS gross margin toward about 50%',
                                   'Champion Leadership ([jOL79tUtq3o @ 00:08:45])'],
                                  ['Flat price sitting over a wide cost tail',
                                   'At $0.035 per action, P50 costs $4.20 and P90 costs $21.00 monthly',
                                   'A 5:1 spread under a $29 price; hold 60% margin at P50',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:11:51])'],
                                  ['Bill shock on uncapped customer usage plans',
                                   'Cursor $7,000 annual plan used in one day; Replit billed $1,000 weekly',
                                   'Usual Replit spend had been $180 to $200 per week',
                                   'The Innovation Attorney ([ubYfOw6FSPA @ 00:15:39])'],
                                  ['Renewal uplifts enforced by manual operations teams',
                                   'Uplifts get missed at renewal, which means quiet revenue leakage',
                                   'Automate a fixed 5% so $100 becomes $105 per user per month',
                                   'MonetizeNow ([x0K0bAATQIA @ 00:03:28])'],
                                  ['Low-density metric carrying large zero-value volume',
                                   'Lifegen had 1M cases at a €20 average but 700K were zero-value',
                                   'Zero-value cases invite sorting of volume worth 1.4M',
                                   'Willingness to Pay ([BGb6-WKMNN4 @ 00:47:11])'],
                                  ['Price cut used as a competitive weapon',
                                   'Rackspace cut price by about 33% and AWS simply matched it',
                                   "Whatever you do, don't try to just be in the middle",
                                   'Willingness to Pay ([cdQzCVUJybY @ 00:07:15])'],
                                  ['Usage invoices swinging beyond buyer budget tolerance',
                                   'Actual costs exceed vendor estimates by 30% to 50% in practice',
                                   '40% month-over-month swings are a nightmare for enterprise finance',
                                   'Ultimate CFO ([xmq83cmzth4 @ 00:04:03])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Close the Leaks Before the New Price Ships',
                           'body': 'Four gates to clear before launching a seat, usage or credit '
                                   'architecture, each pulled from a loss or blowup a practitioner '
                                   'reported.',
                           'items': ['Cap AI losses with a fair-use policy and pilot with 5 to 20 '
                                     'customers before opening usage to the full base [Champion Leadership '
                                     '— jOL79tUtq3o @ 00:18:01].',
                                     'Store the renewal uplift as a fixed or maximum percentage on the '
                                     'quote so it is never missed at renewal [MonetizeNow — x0K0bAATQIA @ '
                                     '00:00:21].',
                                     'Model P50 and P90 cost per user against the price point and hold at '
                                     'least 60% gross margin at P50 users [The Innovation Attorney — '
                                     'ubYfOw6FSPA @ 00:21:13].',
                                     'Expect buyers to demand caps with alerts at 80% and 100%, rollover, '
                                     'locked overage pricing and a contractual cap, and price that in '
                                     '[Soft Learn Hub — oDjXoRkYaA0 @ 00:02:18].']}}],
 'pull_quote': '“Start at seven and then procurement will take you down to four.” — Champion Leadership '
               '(jOL79tUtq3o @ 00:31:08).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Generate 50 to 100 candidate pricing metrics and drop every one that is not '
                      'measurable, invoiceable and auditable [Willingness to Pay — rTGrwbYBlXg @ '
                      '00:07:31].',
                      'Run the validation deck in strict sequence with price last, then stop talking and '
                      'let the customer self-calculate and pick a comparator [Willingness to Pay — '
                      'Ieuyh9RZzvM @ 00:12:49].',
                      'Bake a 3% to 7% annual escalator into contracts and open at seven so procurement '
                      'lands at four [Champion Leadership — jOL79tUtq3o @ 00:29:27].',
                      'Configure the renewal uplift as a fixed or maximum percentage in the quote so the '
                      'increase carries forward automatically [MonetizeNow — x0K0bAATQIA @ 00:00:21].',
                      'Build the hybrid as a base seat with an allotment plus metered overage, backed by '
                      'metering, a rating engine, a credit wallet and invoicing and dunning [The '
                      'Innovation Attorney — ubYfOw6FSPA @ 00:09:09].',
                      'Benchmark only against companies in the same ACV segment and read results by top, '
                      'median and bottom quartile [The SaaS CFO — FvNIaRG9sxI @ 00:01:37].'],
 'statutory_citations': [{'title': 'The Innovation Attorney — Seat Pricing or Token Pricing: What Zendesk '
                                   'and HubSpot Chose [00:00:17]',
                          'url': 'https://www.youtube.com/watch?v=ubYfOw6FSPA&t=17s',
                          'relevance': 'Primary practitioner testimony on the 3:1 inference-cost trigger '
                                       'for moving from seats to usage or hybrid pricing.'},
                         {'title': "Champion Leadership — The Founder's Guide to SaaS Pricing in the AI "
                                   'Era: Seat-Based, Usage-Based, or Hybrid? | Roee Hartuv [00:29:27]',
                          'url': 'https://www.youtube.com/watch?v=jOL79tUtq3o&t=1767s',
                          'relevance': 'Primary practitioner testimony on contract price escalators of 3% '
                                       'to 7% and AI margin compression.'},
                         {'title': 'Willingness to Pay — SaaS Pricing Architecture (Full Training) '
                                   '[00:11:05]',
                          'url': 'https://www.youtube.com/watch?v=BGb6-WKMNN4&t=665s',
                          'relevance': 'Primary practitioner testimony on the four metric criteria, credit '
                                       'design, fairness tests and wallet structuring.'},
                         {'title': 'Ultimate CFO — Why Enterprise Buyers Hate AI Pricing Models - The AI '
                                   'vs. SaaS Pricing War [00:04:52]',
                          'url': 'https://www.youtube.com/watch?v=xmq83cmzth4&t=292s',
                          'relevance': 'Primary practitioner testimony on enterprise buyer pushback '
                                       'against unpredictable usage-based AI invoices.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'x0K0bAATQIA',
                       'title': 'SaaS Renewal Price Uplifts: Automate Price Increases | MonetizeNow',
                       'channel': 'MonetizeNow',
                       'author': 'MonetizeNow',
                       'text': "Now it's $105, a 5% increase applied automatically.",
                       'tip': "Now it's $105, a 5% increase applied automatically.",
                       'timestamp': 186,
                       'timestamp_seconds': 186,
                       'timestamp_label': '[00:03:06]',
                       'url': 'https://www.youtube.com/watch?v=x0K0bAATQIA&t=186s',
                       'markdown': '[00:03:06](https://www.youtube.com/watch?v=x0K0bAATQIA&t=186s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ubYfOw6FSPA',
                       'title': 'Seat Pricing or Token Pricing: What Zendesk and HubSpot Chose',
                       'channel': 'The Innovation Attorney',
                       'author': 'The Innovation Attorney',
                       'text': 'Growth is not retention and a company evaluating its own pricing choice '
                               'needs both figures rather than either alone.',
                       'tip': 'Growth is not retention and a company evaluating its own pricing choice '
                              'needs both figures rather than either alone.',
                       'timestamp': 616,
                       'timestamp_seconds': 616,
                       'timestamp_label': '[00:10:16]',
                       'url': 'https://www.youtube.com/watch?v=ubYfOw6FSPA&t=616s',
                       'markdown': '[00:10:16](https://www.youtube.com/watch?v=ubYfOw6FSPA&t=616s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 's-VGS7d821o',
                       'title': 'Sage Intacct Subscription Billing | SaaS Revenue & Reporting',
                       'channel': 'IWI Consulting Group',
                       'author': 'IWI Consulting Group',
                       'text': 'It all posts into the native general ledger as part of the solution.',
                       'tip': 'It all posts into the native general ledger as part of the solution.',
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=s-VGS7d821o&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=s-VGS7d821o&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KGmwDKTR6fQ',
                       'title': 'How to Get Your SaaS Pricing Structure Right',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'Validate the new pricing internally with finance, customer success, sales '
                               'and product, and externally with customers.',
                       'tip': 'Validate the new pricing internally with finance, customer success, sales '
                              'and product, and externally with customers.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=KGmwDKTR6fQ&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=KGmwDKTR6fQ&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rTGrwbYBlXg',
                       'title': 'SaaS Pricing Metrics Explained: Operational Viability',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'The pricing metric must be non-arbitrary, something a computer can count.',
                       'tip': 'The pricing metric must be non-arbitrary, something a computer can count.',
                       'timestamp': 170,
                       'timestamp_seconds': 170,
                       'timestamp_label': '[00:02:50]',
                       'url': 'https://www.youtube.com/watch?v=rTGrwbYBlXg&t=170s',
                       'markdown': '[00:02:50](https://www.youtube.com/watch?v=rTGrwbYBlXg&t=170s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lC6Gpn0ugFI',
                       'title': 'SaaS Pricing Models Explained in 5 Minutes',
                       'channel': 'Rob Walling',
                       'author': 'Rob Walling',
                       'text': 'Annual plans are often priced as 12 for 10 or 15 to 20 percent off, which '
                               'brings cash in up front.',
                       'tip': 'Annual plans are often priced as 12 for 10 or 15 to 20 percent off, which '
                              'brings cash in up front.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=lC6Gpn0ugFI&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=lC6Gpn0ugFI&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cdQzCVUJybY',
                       'title': 'Pricing for B2B SaaS',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': "And whatever you do, don't try to just be in the middle.",
                       'tip': "And whatever you do, don't try to just be in the middle.",
                       'timestamp': 719,
                       'timestamp_seconds': 719,
                       'timestamp_label': '[00:11:59]',
                       'url': 'https://www.youtube.com/watch?v=cdQzCVUJybY&t=719s',
                       'markdown': '[00:11:59](https://www.youtube.com/watch?v=cdQzCVUJybY&t=719s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tNlpy7MZ8Vk',
                       'title': 'What Good SaaS Pricing Looks Like: Bechmarks, Signals and Metrics',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'Good pricing leaves one friction point instead of four, with the friction '
                               'arriving only at the price point.',
                       'tip': 'Good pricing leaves one friction point instead of four, with the friction '
                              'arriving only at the price point.',
                       'timestamp': 62,
                       'timestamp_seconds': 62,
                       'timestamp_label': '[00:01:02]',
                       'url': 'https://www.youtube.com/watch?v=tNlpy7MZ8Vk&t=62s',
                       'markdown': '[00:01:02](https://www.youtube.com/watch?v=tNlpy7MZ8Vk&t=62s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jOL79tUtq3o',
                       'title': "The Founder's Guide to SaaS Pricing in the AI Era: Seat-Based, "
                                'Usage-Based, or Hybrid? | Roee Hartuv',
                       'channel': 'Champion Leadership',
                       'author': 'Champion Leadership',
                       'text': 'Start at seven and then procurement will take you down to four.',
                       'tip': 'Start at seven and then procurement will take you down to four.',
                       'timestamp': 1868,
                       'timestamp_seconds': 1868,
                       'timestamp_label': '[00:31:08]',
                       'url': 'https://www.youtube.com/watch?v=jOL79tUtq3o&t=1868s',
                       'markdown': '[00:31:08](https://www.youtube.com/watch?v=jOL79tUtq3o&t=1868s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jOL79tUtq3o',
                       'title': "The Founder's Guide to SaaS Pricing in the AI Era: Seat-Based, "
                                'Usage-Based, or Hybrid? | Roee Hartuv',
                       'channel': 'Champion Leadership',
                       'author': 'Champion Leadership',
                       'text': 'Classical SaaS was built on 85% to 95% gross margin.',
                       'tip': 'Classical SaaS was built on 85% to 95% gross margin.',
                       'timestamp': 114,
                       'timestamp_seconds': 114,
                       'timestamp_label': '[00:01:54]',
                       'url': 'https://www.youtube.com/watch?v=jOL79tUtq3o&t=114s',
                       'markdown': '[00:01:54](https://www.youtube.com/watch?v=jOL79tUtq3o&t=114s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l1Q6q8yDjTQ',
                       'title': 'SaaS Pricing Strategy: Why Most New Startups Moved Beyond Per-Seat',
                       'channel': 'Andrew Garberson',
                       'author': 'Andrew Garberson',
                       'text': 'The first price that a startup picks is almost always wrong.',
                       'tip': 'The first price that a startup picks is almost always wrong.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=l1Q6q8yDjTQ&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=l1Q6q8yDjTQ&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ieuyh9RZzvM',
                       'title': 'Validating Pricing Models in B2B SaaS',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'Show the pricing, then you shut up and you wait.',
                       'tip': 'Show the pricing, then you shut up and you wait.',
                       'timestamp': 769,
                       'timestamp_seconds': 769,
                       'timestamp_label': '[00:12:49]',
                       'url': 'https://www.youtube.com/watch?v=Ieuyh9RZzvM&t=769s',
                       'markdown': '[00:12:49](https://www.youtube.com/watch?v=Ieuyh9RZzvM&t=769s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BGb6-WKMNN4',
                       'title': 'SaaS Pricing Architecture (Full Training)',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'Credit based systems are essentially usage-based pricing paid up front.',
                       'tip': 'Credit based systems are essentially usage-based pricing paid up front.',
                       'timestamp': 534,
                       'timestamp_seconds': 534,
                       'timestamp_label': '[00:08:54]',
                       'url': 'https://www.youtube.com/watch?v=BGb6-WKMNN4&t=534s',
                       'markdown': '[00:08:54](https://www.youtube.com/watch?v=BGb6-WKMNN4&t=534s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BGb6-WKMNN4',
                       'title': 'SaaS Pricing Architecture (Full Training)',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': "It's a concept that I call wallet structuring where you try to break your "
                               'pricing into components that speak to different parties in the '
                               'organization.',
                       'tip': "It's a concept that I call wallet structuring where you try to break your "
                              'pricing into components that speak to different parties in the '
                              'organization.',
                       'timestamp': 2098,
                       'timestamp_seconds': 2098,
                       'timestamp_label': '[00:34:58]',
                       'url': 'https://www.youtube.com/watch?v=BGb6-WKMNN4&t=2098s',
                       'markdown': '[00:34:58](https://www.youtube.com/watch?v=BGb6-WKMNN4&t=2098s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FvNIaRG9sxI',
                       'title': 'How to Benchmark Your SaaS Business | SaaS Metrics School | '
                                'BenchMarkIt.ai | SaaS Business',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': "We can't benchmark an enterprise business against a self-service business "
                               'and vice versa.',
                       'tip': "We can't benchmark an enterprise business against a self-service business "
                              'and vice versa.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=FvNIaRG9sxI&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=FvNIaRG9sxI&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xmq83cmzth4',
                       'title': 'Why Enterprise Buyers Hate AI Pricing Models - The AI vs. SaaS Pricing '
                                'War',
                       'channel': 'Ultimate CFO',
                       'author': 'Ultimate CFO',
                       'text': 'Without that work, AI software is going to become the most expensive '
                               'shelfware that enterprises have ever purchased.',
                       'tip': 'Without that work, AI software is going to become the most expensive '
                              'shelfware that enterprises have ever purchased.',
                       'timestamp': 442,
                       'timestamp_seconds': 442,
                       'timestamp_label': '[00:07:22]',
                       'url': 'https://www.youtube.com/watch?v=xmq83cmzth4&t=442s',
                       'markdown': '[00:07:22](https://www.youtube.com/watch?v=xmq83cmzth4&t=442s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oDjXoRkYaA0',
                       'title': 'Per Seat Pricing Is Ending? 3 SaaS Pricing Models Replacing It (Atlassian '
                                'Rovo, Dec 3)',
                       'channel': 'Soft Learn Hub',
                       'author': 'Soft Learn Hub',
                       'text': "What's ending is the seat as the whole price.",
                       'tip': "What's ending is the seat as the whole price.",
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=oDjXoRkYaA0&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=oDjXoRkYaA0&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ydyjI39LlNw',
                       'title': '8 SaaS pricing models explained in under 3 minutes',
                       'channel': 'Binary Stream Software',
                       'author': 'Binary Stream Software',
                       'text': 'Pay as you go pricing allows customers to pay only for what they use.',
                       'tip': 'Pay as you go pricing allows customers to pay only for what they use.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=ydyjI39LlNw&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=ydyjI39LlNw&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
