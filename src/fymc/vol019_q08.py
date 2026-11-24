from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'q08-revenue-recognition-resold-software',
 'question_prompt': 'How must software revenue be recognized under ASC 606, including principal-vs-agent '
                    'calls for resellers?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Revenue Recognition for Resold Software',
 'subtitle': 'Principal vs. agent gross/net reporting, the five-step model, SaaS and usage-based revenue, '
             'side letters and enforceability failures, IFRS 15 cases, NetSuite Advanced Revenue '
             'Management, and how renewals and multi-year contracts affect ARR and retention',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one test for resold software: control before transfer '
                      'decides whether the deal books gross as principal or net as agent, and cash never '
                      "equals revenue. Jobank CPA's ECC case shows a $500,000 GPU resale collapsing to a "
                      '$75,000 commission once custody disappears, while credit risk and flash title prove '
                      'nothing. The SaaS CFO, Concierge CPA, and Ledger & Logic all route upfront cash to '
                      'deferred revenue and recognize ratably. Accounting and Auditing Hub reallocates a '
                      '$600,000 bundle on $700,000 of standalone value, burying the setup fee in SaaS. '
                      "Mechanics run through NetSuite ARM carve-outs, RSM's revenue rules, and Ordway's "
                      'unified billing-revenue platform. The fights: ratable versus consumption '
                      'recognition for usage commits, with Angela Louu and Devon Coombs warning that '
                      'overage estimates, breakage, and SSP swings defy every revenue system they pitched.',
 'key_metrics': [{'label': 'Gross-to-Net Collapse on Resold Element',
                  'metric': 'Gross-to-Net Collapse on Resold Element',
                  'value': '$500,000 gross shrinks to $75,000 (15% net commission)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "ECC's third-party GPU resale books gross with upfront inventory risk and "
                             'physical custody; if the vendor bills the customer directly and ECC never '
                             'takes custody, it flips to agent and keeps only the commission.',
                  'source': 'Jobank CPA ([KjWijHo8iMI @ 00:06:58])'},
                 {'label': 'Revenue Lost to Weak Contract Management',
                  'metric': 'Revenue Lost to Weak Contract Management',
                  'value': '9.2% of annual revenue',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Average leakage cited from messy mid-cycle upgrades, downgrades, and '
                             'prorations handled through manual calculations and poor data tracking.',
                  'source': 'Ledger & Logic ([lYs19gfynCE @ 00:03:51])'},
                 {'label': 'Side-Letter Revenue Wipeout',
                  'metric': 'Side-Letter Revenue Wipeout',
                  'value': '$900,000 TCV deal recognized at $0 for the quarter; $75,000 catch-up on April '
                           '1',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A sales VP email promising a 100% refund if latency exceeded 200 '
                             'milliseconds in Q1 forced $300,000 of upfront cash into a refund liability '
                             'until the right lapsed.',
                  'source': 'Jobank CPA ([WeV8GbQwaPE @ 00:05:30])'},
                 {'label': 'Typical Overage Estimate in Ratable Consumption Models',
                  'metric': 'Typical Overage Estimate in Ratable Consumption Models',
                  'value': '30% overage tacked on and smoothed ratably',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Companies taking committed usage ratably estimate a typical 30% overage they '
                             'have not invoiced yet and spread it over the term, which guarantees they are '
                             'wrong a lot.',
                  'source': 'Ambition, Aligned with Devon Coombs ([B4Ckh2wjlgc @ 00:03:39])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every operator who touched the reseller question lands on the same pivot: '
                              'control, not invoicing, decides whether a resold deal hits the top line '
                              'gross or net. Jobank CPA frames it as two outcomes - a principal books the '
                              'full gross billing to the customer, while an agent books only gross billing '
                              'minus vendor cost, the retained commission [KjWijHo8iMI @ 00:01:00]. The '
                              'test is whether the reseller controls the specified good or service before '
                              'it reaches the end customer; if the obligation is only to arrange for '
                              'another party to provide it, the reseller is the agent [KjWijHo8iMI @ '
                              '00:01:31]. The 12th & Norwegian hosts reach the same split with a '
                              'food-delivery analogy: a platform that sets price and takes ownership '
                              'before delivery is probably principal, while one handling logistics at the '
                              "restaurant's price is probably agent, and the agent typically books only "
                              'its commission or fee [Q0XhS1B8mWE @ 00:16:35]. Juliet at Concierge CPA '
                              'pushes the same discipline from the software side, warning that ASC 606 is '
                              'not looking at the word software but at how control transfers, so a '
                              'perpetual license lands at a point in time while ongoing access lands over '
                              'time [I8dBdXuT7cA @ 00:14:41]. Look past the label, trace control, and '
                              'price the deal accordingly.',
                              'The second point of total agreement: cash in the bank is not revenue. Ben '
                              'Murray of The SaaS CFO walks a $12,000 one-year invoice through the books - '
                              'debit accounts receivable, credit deferred revenue - and names the classic '
                              'mistake of crediting the full $12,000 to the P&L in one month instead of '
                              "pulling it in ratably [p4KgISWaH6s @ 00:04:43]. The SaaS CFO's three-year, "
                              '$36,000 example recognizes $1,000 a month starting April 1, leaving $11,000 '
                              'then $10,000 of deferred revenue as each month closes [p4KgISWaH6s @ '
                              '00:06:57]. Concierge CPA runs the same play at bigger size: Big Tech '
                              'collects $120,000 on January 1, recognizes zero that day, credits deferred '
                              'revenue as a contract liability, and earns $10,000 per month as access is '
                              'delivered; if performance runs ahead of billing, the entry flips to a '
                              'contract asset instead [I8dBdXuT7cA @ 00:13:04]. Ledger & Logic calls '
                              'confusing the two the fastest way to fail an audit, because the customer '
                              'who hands over $12,000 upfront is still owed 12 months of software access, '
                              'which is why the balance is a liability rather than a win [lYs19gfynCE @ '
                              '00:01:01]. For a reseller, that means booking, invoicing, cash receipt, and '
                              'recognition run as four separate events, never one.',
                              'Nobody trusts the price printed on the invoice. Suresh Perryami of '
                              'Accounting and Auditing Hub lists it as trap number two - never blindly '
                              'trust the sales invoice, always reallocate total contract value on '
                              'standalone selling prices - alongside never booking an administrative setup '
                              'fee upfront even when it is billed and non-refundable [-5y55BOFAKA @ '
                              '00:05:33]. CFO AI calls this the heart of the matter in NetSuite: when '
                              'items sell in one bundle, the price on each sales-order line may not '
                              'reflect standalone value, so total cash must be spread across every piece '
                              'on fair value [MAsF2w47iew @ 00:01:24]. Ledger & Logic warns that randomly '
                              'parking a bundle discount on whatever product feels convenient, without '
                              'documented SSP, invites massive audit risk [lYs19gfynCE @ 00:03:05]. Dan '
                              'Colbach at Ordway gives the field version: software sold with '
                              'implementation and maintenance thrown in at 100% discount still carries '
                              "three obligations, so the seller must pull each one's fair value out of the "
                              '$12K total and run it on its own schedule - software and maintenance over '
                              '12 months, implementation over four [vPpXI4fjA1A @ 00:10:52]. The operating '
                              'rule for any resold bundle is the same five steps every time: contract, '
                              'obligations, price, allocation, recognition, with no step skipped.'],
               'table': {'caption': 'Where the practitioners agree on resold and bundled software revenue',
                         'headers': ['Consensus Point',
                                     'Operator Translation For Resold Software',
                                     'Expert Source'],
                         'rows': [['Control before transfer decides gross versus net revenue on resold '
                                   'SaaS',
                                   'Principal books full gross billing; agent books only billing minus '
                                   'vendor cost as commission',
                                   'Jobank CPA ([KjWijHo8iMI @ 00:01:17])'],
                                  ['Agents recognize only their commission or fee, never the full sale',
                                   'A platform that sets price and takes ownership first is probably the '
                                   'principal',
                                   '12th & Norwegian ([Q0XhS1B8mWE @ 00:16:35])'],
                                  ['Invoicing or cash receipt never equals revenue recognition on '
                                   'subscriptions',
                                   'Credit deferred revenue on the invoice, then recognize ratably in each '
                                   'month of term',
                                   'The SaaS CFO ([p4KgISWaH6s @ 00:08:12])'],
                                  ['Revenue follows performance, not cash, under the five-step ASC 606 '
                                   'model',
                                   'Big Tech collects $120,000 upfront, recognizes zero on day one, then '
                                   '$10,000 monthly',
                                   'Accounting: Concierge CPA ([I8dBdXuT7cA @ 00:11:38])'],
                                  ['Invoice line prices must be reallocated on standalone selling prices '
                                   'every time',
                                   'Bundled discount forces reallocation; the setup fee gets absorbed into '
                                   'SaaS over three years',
                                   'Accounting and Auditing Hub ([-5y55BOFAKA @ 00:05:48])'],
                                  ['Distinct promises must be separated before any price allocation '
                                   'happens',
                                   'Software recognized ratably over twelve months while a one-time '
                                   'training fee books at completion',
                                   'Ledger & Logic ([lYs19gfynCE @ 00:02:36])'],
                                  ['Spreadsheets break under revenue scrutiny, so systematize before '
                                   'audits and fundraising',
                                   'One fat-fingered cell can corrupt schedules, raise audit fees, and '
                                   'trigger a significant deficiency',
                                   'Ordway ([vPpXI4fjA1A @ 00:08:00])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Jobank CPA gives resellers a three-question tree: are you integrating the '
                              'third-party SaaS into a distinct combined solution; do you control the '
                              'underlying hosted software before transfer; or is your primary promise just '
                              'arranging for the vendor to provide it? Yes on either of the first two '
                              'means principal, yes on the third means agent [KjWijHo8iMI @ 00:05:13]. '
                              'Define the unit of account - bare access to a vendor-hosted platform, a '
                              'combined SaaS-plus-implementation output, or merely an ordering and billing '
                              'service - then weigh three indicators: a vendor that hosts and maintains '
                              'the platform is principal even if you handle basic tech support; buying '
                              'capacity only after securing an order leans agent, while committing to pay '
                              'regardless of an end user leans principal; price discretion shows market '
                              'power but does not alone prove control [KjWijHo8iMI @ 00:02:39]. Two myths '
                              'die here: issuing the invoice and eating customer default proves nothing '
                              'because credit risk was removed as a primary indicator, and flash title is '
                              'a magic trick auditors will not buy [KjWijHo8iMI @ 00:03:43]. The 12th & '
                              'Norwegian hosts weight the same levers - who sets the price and who takes '
                              "ownership before delivery [Q0XhS1B8mWE @ 00:16:20]. Jobank's ECC case "
                              'prices the stakes: $500,000 gross with custody, $75,000 net commission '
                              'without it.',
                              "Suresh Perryami's Cloud Nova case is the cleanest worked allocation. A "
                              'non-cancellable three-year deal invoices $50,000 setup, $70,000 data '
                              'migration, $360,000 cloud ERP access, and $120,000 premium support - '
                              '$600,000 paid on day one. Migration is distinct because a third-party '
                              'consultant could do it; the setup fee is just server provisioning and '
                              'passwords, so it folds into the SaaS obligation; premium support with '
                              'dedicated account managers is distinct. A $20,000-per-year refund if uptime '
                              'drops below 99.9% is variable consideration, but 99.99% historical uptime '
                              'constrains it to zero, so price stays $600,000 [-5y55BOFAKA @ 00:02:15]. '
                              'Standalone prices - migration $100,000, SaaS plus setup $450,000, support '
                              '$150,000, $700,000 total - drive the split, and the $50,000 setup fee '
                              'disappears into SaaS spread over the term [-5y55BOFAKA @ 00:02:51]. '
                              'Migration finishes March 31 and books $85,800; SaaS allocated at $385,800 '
                              'earns $96,450 over nine months; the year-one entry debits deferred revenue '
                              '$128,550, leaving $385,650 split into current and non-current [-5y55BOFAKA '
                              '@ 00:04:35]. CFO AI shows the same redistribution inside NetSuite: on a '
                              '$12,000 deal the system carves $800 out of the license and carves it into '
                              'maintenance, and total revenue stays $12,000, a zero-sum game [MAsF2w47iew '
                              '@ 00:03:28].',
                              "Once the math is right, practitioners push it into a system. CFO AI's "
                              'NetSuite ARM setup has three moves: switch the feature on - a one-way '
                              'street, permanent once enabled - define revenue rules, and configure items, '
                              'the bedrock of the whole build; an approved sale then spawns a non-posting '
                              'revenue arrangement, actual plans that post to the ledger, and forecast '
                              'plans for reporting. At month end, generate revenue journal entries first '
                              'and only then run the deferred revenue reclassification, reconciling on the '
                              "deferred revenue waterfall [MAsF2w47iew @ 00:04:55]. RSM's demo lists the "
                              'common rules - percent complete, ratable, milestone, one-time event - and '
                              'flags the end date change impact: update all periods for one cumulative '
                              'catch-up in the current period, or update remaining periods only to spread '
                              'unrecognized revenue forward [Qxj-ooX7WrE @ 00:04:41]. For resellers, RSM '
                              'uses NetSuite dimensions to sell the same item through a channel and '
                              'directly to end users while keeping one simplified item catalog '
                              "[Qxj-ooX7WrE @ 00:11:10]. Ordway's Dan Colbach, a former PwC auditor, "
                              'explains the urgency: one fat-fingered cell or corrupted formula in a '
                              'revenue spreadsheet compounds into wider testing, rising audit fees, a '
                              'possible significant deficiency, a restatement, or a missed financing round '
                              '[vPpXI4fjA1A @ 00:08:20].'],
               'table': {'caption': 'Worked numbers and system settings the practitioners actually ran',
                         'headers': ['Mechanic', 'Exact Number, Setting, Or Rule', 'Expert Source'],
                         'rows': [['ECC hybrid bundle element B resale of third-party server maker GPUs',
                                   '$500,000 gross as principal versus $75,000 at a 15% net commission as '
                                   'agent',
                                   'Jobank CPA ([KjWijHo8iMI @ 00:06:58])'],
                                  ['Cloud Nova bundled three-year contract allocated on relative '
                                   'standalone selling prices',
                                   '$600,000 paid against $700,000 standalone value; data migration books '
                                   '$85,800 at completion',
                                   'Accounting and Auditing Hub ([-5y55BOFAKA @ 00:03:10])'],
                                  ['SLA uptime penalty treated as variable consideration and then '
                                   'constrained',
                                   '$20,000 yearly refund below 99.9% uptime; 99.99% history constrains '
                                   'the penalty to zero',
                                   'Accounting and Auditing Hub ([-5y55BOFAKA @ 00:02:33])'],
                                  ['NetSuite ARM carve-out and carve-in redistribution across bundled '
                                   'sales order lines',
                                   '$800 carved out of the license into maintenance; $12,000 total revenue '
                                   'stays unchanged',
                                   'CFO AI ([MAsF2w47iew @ 00:03:28])'],
                                  ['Side-letter latency refund email attached to a three-year enterprise '
                                   'deal',
                                   '$300,000 upfront cash credited to refund liability; $75,000 cumulative '
                                   'catch-up on April 1',
                                   'Jobank CPA ([WeV8GbQwaPE @ 00:05:30])'],
                                  ['Consumption commit recognized ratably with estimated overage smoothing '
                                   'over the term',
                                   '$100K paid for 120K in credits; a typical 30% overage estimated and '
                                   'smoothed ratably',
                                   'Ambition, Aligned with Devon Coombs ([B4Ckh2wjlgc @ 00:03:39])'],
                                  ['Weak contract management on mid-cycle upgrades, downgrades, and manual '
                                   'prorations',
                                   'Average leakage of 9.2% of annual revenue through calculation errors '
                                   'and poor tracking',
                                   'Ledger & Logic ([lYs19gfynCE @ 00:03:51])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Lock the deal desk before the auditor opens the contract',
                           'body': 'The sharpest operators stop revenue problems upstream - at the order '
                                   'form, the side email, and the item configuration - instead of fixing '
                                   'them at quarter close.',
                           'items': ['Wire a hard-stop controller review into Salesforce CPQ or your '
                                     'RevOps platform for any non-standard discount, performance '
                                     'guarantee, or cancellation clause before the deal goes out for '
                                     'signature [Jobank CPA — WeV8GbQwaPE @ 00:06:15]',
                                     'Run quarterly or annual side letter confirmations with top '
                                     'enterprise customers so a rogue Slack message or late-night AE email '
                                     'cannot rewrite the master services agreement [Jobank CPA — '
                                     'WeV8GbQwaPE @ 00:06:29]',
                                     'Use NetSuite dimensions to run channel and direct-to-end-user sales '
                                     'off one item with one-to-many fair value calculations instead of '
                                     'bloating the item catalog [RSM US LLP — Qxj-ooX7WrE @ 00:11:10]',
                                     "Generate the month's revenue journal entries first and only then run "
                                     'the deferred revenue reclassification, then reconcile against the '
                                     'deferred revenue waterfall report [CFO AI — MAsF2w47iew @ '
                                     '00:04:55]']},
               'sop_steps': [{'step': 1,
                              'title': 'Define the unit of account',
                              'action': 'Decide whether the promise is bare SaaS access, a combined '
                                        'SaaS-plus-implementation output, or merely an ordering and '
                                        'billing service.',
                              'detail': "Hosted SaaS runs on the original owner's infrastructure, not the "
                                        "reseller's, so this definition drives everything downstream "
                                        '[Jobank CPA — KjWijHo8iMI @ 00:02:04]'},
                             {'step': 2,
                              'title': 'Run the 1-2-3 control test',
                              'action': 'Ask integration, control before transfer, and arrange-only in '
                                        'order; weigh fulfillment, inventory risk, and price discretion; '
                                        'ignore credit risk and flash title.',
                              'detail': 'Integration or control means principal and gross; arrange-only '
                                        'means agent and net commission [Jobank CPA — KjWijHo8iMI @ '
                                        '00:05:13]'},
                             {'step': 3,
                              'title': 'Reallocate on standalone selling prices',
                              'action': 'Ignore invoice line prices, fold non-distinct setup fees into '
                                        'SaaS, assess SLA penalties as variable consideration, then '
                                        'allocate total price on relative SSP.',
                              'detail': 'Cloud Nova allocates $600,000 against $700,000 of standalone '
                                        'value and constrains a $20,000 SLA refund to zero on 99.99% '
                                        'uptime history [Accounting and Auditing Hub — -5y55BOFAKA @ '
                                        '00:02:51]'},
                             {'step': 4,
                              'title': 'Book the cash correctly and automate the schedule',
                              'action': 'Credit upfront cash to deferred revenue, or to refund liability '
                                        'if any refund right exists, then load the arrangement into a '
                                        'revenue sub-ledger such as NetSuite ARM.',
                              'detail': 'Cash under an open 100% refund right sits in refund liability '
                                        'until the right lapses [Jobank CPA — WeV8GbQwaPE @ 00:05:09]; '
                                        'month-end runs revenue entries before the deferred revenue '
                                        'reclass [CFO AI — MAsF2w47iew @ 00:04:55]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split on resold software is what actually proves you are the '
                              'principal. 12th & Norwegian frames it with a food-delivery platform: set '
                              'the price and take ownership before delivery and you are probably the '
                              'principal, but if the restaurant sets the price and you only run logistics, '
                              'you are the agent booking a commission [Q0XhS1B8mWE @ 00:16:20]. Jobank CPA '
                              'refuses to let pricing power carry that much weight, warning that freedom '
                              'to set the end price shows market power but does not definitively prove '
                              'control of the underlying SaaS [KjWijHo8iMI @ 00:03:10]. Jobank goes '
                              "further on the reseller's favorite argument: issuing the invoice and eating "
                              'customer defaults is a billing mechanic, because ASC 606 intentionally '
                              'removed credit risk as a primary indicator, and flash title held for a '
                              'split second is a magic trick auditors will not fall for [KjWijHo8iMI @ '
                              '00:03:43]. The stakes are spelled out in the ECC case: upfront inventory '
                              'risk of $400,000, physical custody in its own data centers, and end-price '
                              'control earn $500,000 gross, while a vendor-bills-direct version collapses '
                              'Element B to a 15% net commission of $75,000 [KjWijHo8iMI @ 00:06:58]. '
                              'Operators packaging third-party SaaS with light implementation should '
                              'expect principal treatment only on their own services.',
                              'On usage-priced deals the split is between straight-line and burn-down. '
                              'Angela Louu of Ambition, Aligned lays out the two camps: take a $100,000 '
                              'commitment for 120k in credits ratably and estimate overages as variable '
                              'consideration, or recognize revenue as credits are actually consumed, and '
                              'reports that more than 50% of companies started ratable but more and more '
                              'are flipping to consumption, especially infrastructure players [B4Ckh2wjlgc '
                              '@ 00:04:31]. The ratable camp books a typical 30% overage it has not '
                              'invoiced and smooths it, which Louu calls the ultra-technical loophole that '
                              'keeps producing cumulative catch-ups and portfolio approaches [B4Ckh2wjlgc '
                              '@ 00:03:39]. Co-host Devon Coombs, a former Google Cloud controller, leans '
                              'consumption when overages are planned but concedes that with ten or a '
                              'thousand consumption obligations the SSP allocation needs day-one estimates '
                              'no revenue system could operationalize, so ratable usually wins as the '
                              'lesser evil, provided the business structures packages correctly '
                              '[B4Ckh2wjlgc @ 00:39:37]. Louu adds that consumption is not estimate-free, '
                              'because breakage forecasting ends up looking a lot like variable '
                              'consideration. Accounting Academy shows why timing labels mislead: a '
                              'satellite builder recognizes at a point in time when there is no '
                              'enforceable right to payment, flipping to over time only when both criteria '
                              'are met [rm7beKRTRko @ 00:03:10].',
                              "The tooling camps split three ways. Ordway's Dan Colbach, a former PwC "
                              'auditor and four-year NetSuite veteran, argues billing and revenue must '
                              'live on one platform built together, because modules bolted on years apart '
                              'do not always talk and a contract change has to flow seamlessly into '
                              'revenue [vPpXI4fjA1A @ 00:12:52]. Ledger & Logic prefers a dedicated '
                              'revenue sub-ledger inside the billing platform that crunches prorations and '
                              'allocation logic and feeds only summarized data to the ERP, which stays the '
                              'pristine source of truth [lYs19gfynCE @ 00:06:22]. RSM US and CFO AI take '
                              'the ERP-native route, building the logic inside NetSuite Advanced Revenue '
                              'Management, where a sales order spawns a non-posting revenue arrangement, '
                              'fair value price lists drive carve-outs and carve-ins, and RSM points out '
                              'that legacy revenue recognition classic needed bundle installs, '
                              'customization, and scripting to allocate by fair value [Qxj-ooX7WrE @ '
                              '00:16:17]. Devon Coombs of Ambition, Aligned punctures all three for usage '
                              'models: after pitching every major revenue operations system, the answer '
                              'was that it cannot be systematized and needs conventions or manual '
                              'recognition [B4Ckh2wjlgc @ 00:39:22]. 12th & Norwegian lands in the same '
                              'place on basic subscriptions, calling manual tracking a complete nightmare '
                              'and pointing to purpose-built SaaS revenue software.'],
               'table': {'caption': 'Side-by-side playbooks where practitioners split on resold and '
                                    'bundled software',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Reseller gross versus net revenue call',
                                   'Set the end price and take ownership before delivery, then book the '
                                   'full sale as principal',
                                   'Price discretion shows market power but does not definitively prove '
                                   'control of hosted SaaS',
                                   '12th & Norwegian ([Q0XhS1B8mWE @ 00:16:20]); Jobank CPA ([KjWijHo8iMI '
                                   '@ 00:03:10])'],
                                  ['Committed usage and credit deals',
                                   'Ratable stand-ready recognition with an estimated 30% overage smoothed '
                                   'as variable consideration',
                                   'Burn down credits as actually consumed and estimate breakage on unused '
                                   'balances',
                                   'Ambition, Aligned with Devon Coombs ([B4Ckh2wjlgc @ 00:03:39]); '
                                   'Ambition, Aligned with Devon Coombs ([B4Ckh2wjlgc @ 00:36:08])'],
                                  ['Mid-term contract modification true-ups',
                                   'A downgrade triggers a cumulative catch-up recalculated as of the '
                                   'modification date',
                                   'Minor term extensions or price tweaks just adjust the existing '
                                   'recognition pattern going forward',
                                   'Ledger & Logic ([lYs19gfynCE @ 00:05:23]); 12th & Norwegian '
                                   '([Q0XhS1B8mWE @ 00:17:29])'],
                                  ['End date extension inside NetSuite ARM',
                                   'Update all periods with one cumulative catch-up booked in the current '
                                   'period',
                                   'Update remaining periods only, spreading unrecognized revenue over the '
                                   'months left',
                                   'RSM US LLP ([Qxj-ooX7WrE @ 00:04:41]); RSM US LLP ([Qxj-ooX7WrE @ '
                                   '00:05:12])'],
                                  ['Monthly subscription revenue timing trigger',
                                   'Recognize one hundred dollars per month when the customer pays for the '
                                   'subscription',
                                   'Revenue follows performance, not cash, so upfront payments sit in '
                                   'deferred revenue first',
                                   'Accounting Journal Entries ([SgRytNI-ALo @ 00:02:01]); Accounting: '
                                   'Concierge CPA ([I8dBdXuT7cA @ 00:03:18])'],
                                  ['Onboarding, setup, and implementation fees',
                                   'A provisioning-only setup fee is not distinct and gets absorbed into '
                                   'the SaaS allocation over 36 months',
                                   'Bundled implementation running four months gets its own SSP slice and '
                                   'recognition schedule',
                                   'Accounting and Auditing Hub ([-5y55BOFAKA @ 00:03:28]); Ordway '
                                   '([vPpXI4fjA1A @ 00:10:52])'],
                                  ['Where the revenue engine should live',
                                   'One platform where billing and revenue were built together so contract '
                                   'changes flow straight through',
                                   'A billing-side revenue sub-ledger that feeds only clean summarized '
                                   'entries into the ERP',
                                   'Ordway ([vPpXI4fjA1A @ 00:12:36]); Ledger & Logic ([lYs19gfynCE @ '
                                   '00:06:22])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Jobank CPA's CloudScale AI teardown is the cleanest blow-up story. Sales "
                              'signs a three-year, $900,000 TCV deal at the December 31 buzzer, books a '
                              '$300,000 ARR boost, and three months later the big four auditors put '
                              'recognized GAAP revenue for the quarter at exactly $0 [WeV8GbQwaPE @ '
                              '00:00:54]. Two things killed it. A clause letting the customer walk '
                              'penalty-free after year one shrank the accounting term from three years to '
                              'one, and then a VP of sales email promised a 100% refund if AI CPU latency '
                              'topped 200 milliseconds in Q1, which overrides the master services '
                              'agreement and makes the contract term effectively day-to-day [WeV8GbQwaPE @ '
                              '00:03:36]. The cash cannot even sit in deferred revenue: the $300,000 lands '
                              'as a refund liability on January 1 and only moves to deferred revenue on '
                              'April 1 if the refund right lapses, followed by a $75,000 cumulative '
                              'catch-up [WeV8GbQwaPE @ 00:05:30]. Accounting: Concierge CPA reduces step '
                              'one to the same blunt test: is this a real enforceable arrangement and do '
                              'we actually expect to get paid, because if not there may be no contract at '
                              'all [I8dBdXuT7cA @ 00:04:03]. Until April 1, Jobank warns, working-capital '
                              'metrics look incredibly weak to any investor scrutinizing the books.',
                              'The most common self-inflicted wound is booking the invoice as revenue. Ben '
                              'Murray of The SaaS CFO calls out companies that debit receivables and '
                              'credit revenue for the full $12,000 annual subscription in one month '
                              'instead of deferring it and pulling it in ratably [p4KgISWaH6s @ 00:05:05]. '
                              "Concierge CPA's Big Tech example drives the same point: $120,000 wired on "
                              'January 1 is zero revenue that day and $10,000 a month thereafter, because '
                              'revenue follows performance, not cash. Suresh Perryami of Accounting and '
                              'Auditing Hub lists three traps from a $600,000 Cloud Nova contract: never '
                              'recognize a non-refundable $50,000 setup fee on day one, never trust '
                              'invoice prices over standalone selling prices, and always treat a '
                              '$20,000-a-year uptime SLA refund as variable consideration that must be '
                              'formally assessed before locking the transaction price [-5y55BOFAKA @ '
                              '00:05:48]. Cloud Nova only constrained that penalty to zero because '
                              'historical data proved 99.99% uptime against a 99.9% threshold [-5y55BOFAKA '
                              '@ 00:02:33]. The mnainstitute.com analysts show how outsiders catch '
                              'aggressive booking: receivables outgrowing revenue, end-of-quarter spikes '
                              'tied to channel stuffing, and a widening gap between reported revenue and '
                              'unearned revenue, with a 30% receivables jump against 15% revenue growth '
                              'forcing a human call on contract structure versus collections [7IqQXBLa14Y '
                              '@ 00:05:58].',
                              'Spreadsheet-run revenue is where the economics bleed. Ledger & Logic puts '
                              'weak contract management around mid-cycle adjustments at an average 9.2% of '
                              'annual revenue, and calls manual downgrade catch-ups across hundreds of '
                              'customers practically impossible without critical errors [lYs19gfynCE @ '
                              '00:03:51]. Dan Colbach of Ordway, recalling audit days, says one '
                              'fat-fingered cell or corrupted formula compounds into expanded testing, '
                              'rising audit fees, a possible significant deficiency, restatements, or a '
                              'blown financing, and Steve Kyer adds that a failed audit can push a raise '
                              'back six months or longer [vPpXI4fjA1A @ 00:08:36]. The Ambition, Aligned '
                              'hosts flag the slow-motion version: smoothing variable consideration into '
                              'the future feels clean until five years later, when contracts modified '
                              'every nine months have stacked up millions of dollars in deferred balances '
                              'that nobody left on the team can explain [B4Ckh2wjlgc @ 00:27:32]. Coombs '
                              'has also watched $10 million-plus design efforts to fix this that were '
                              'never auditable and never got executed [B4Ckh2wjlgc @ 00:42:36]. Inside '
                              'NetSuite, CFO AI flags that switching ARM on is a one-way street and that '
                              'revenue journal entries must run before the deferred revenue '
                              'reclassification, the exact order that keeps the financials accurate every '
                              'single time.'],
               'table': {'caption': 'Firsthand traps and the economics they hit',
                         'headers': ['Failure Mode', 'Reported Damage', 'Economics Check', 'Expert Source'],
                         'rows': [['Side email refund promise from sales',
                                   'A $900,000 TCV deal booked as a $300,000 ARR boost shows $0 GAAP '
                                   'revenue for the quarter',
                                   'Hold the cash in refund liability until the Q1 latency refund right '
                                   'lapses on April 1',
                                   'Jobank CPA ([WeV8GbQwaPE @ 00:01:10])'],
                                  ['Reseller assumes principal status by default',
                                   'Element B shrinks from $500,000 gross to a 15% net commission of '
                                   '$75,000',
                                   'Test custody, upfront inventory risk, and who hosts the software '
                                   'before booking gross',
                                   'Jobank CPA ([KjWijHo8iMI @ 00:06:58])'],
                                  ['Annual invoice credited straight to revenue',
                                   'The full $12,000 one-year subscription lands in a single month on the '
                                   'P&L',
                                   'Credit deferred revenue, then release $1,000 per month as the service '
                                   'is delivered',
                                   'The SaaS CFO ([p4KgISWaH6s @ 00:05:05])'],
                                  ['Manual handling of mid-cycle modifications',
                                   'Weak contract management costs companies an average 9.2% of annual '
                                   'revenue',
                                   'Route downgrades, prorations, and catch-ups through an automated '
                                   'revenue sub-ledger',
                                   'Ledger & Logic ([lYs19gfynCE @ 00:03:51])'],
                                  ['Spreadsheet revenue schedules under audit',
                                   'Fat-fingered cells drive extra testing, higher audit fees, and a '
                                   'possible significant deficiency',
                                   'Systematize before a financing round so a failed audit does not delay '
                                   'it six months',
                                   'Ordway ([vPpXI4fjA1A @ 00:08:36])'],
                                  ['Monthly retention masking multi-year renewal risk',
                                   'Diligence asks why the May 2023 renewal rate hit 65% against 95% gross '
                                   'revenue retention',
                                   'Track renewal rate on dollar and count basis in each customer '
                                   'anniversary month',
                                   'The SaaS CFO ([G9iKRE0cqZU @ 00:02:54])'],
                                  ['Usage estimates that no system can operationalize',
                                   '$10 million-plus design efforts that were never auditable and never '
                                   'got executed',
                                   'Check whether frequent overages mean the performance obligations were '
                                   'misidentified',
                                   'Ambition, Aligned with Devon Coombs ([B4Ckh2wjlgc @ 00:42:36])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Booking Gate for Resold and Bundled Software',
                           'body': 'Clear every gate before a reseller or bundled deal touches the top '
                                   'line or the ARR deck.',
                           'items': ['Run the three-step control test (integration into a combined '
                                     'solution, control of the hosted software before transfer, or a pure '
                                     'arrange-for-the-vendor promise) before booking gross; vendor-billed '
                                     'direct deals drop to net commission [Jobank CPA — KjWijHo8iMI @ '
                                     '00:05:13].',
                                     'Force a hard-stop controller review in Salesforce CPQ or RevOps '
                                     'tooling for any non-standard discount, performance guarantee, or '
                                     'cancellation clause, and collect side letter confirmations from top '
                                     'enterprise customers [Jobank CPA — WeV8GbQwaPE @ 00:06:15].',
                                     'Reallocate every bundle on standalone selling price instead of '
                                     'invoice prices and fold non-distinct setup fees into the '
                                     'subscription allocation [Accounting and Auditing Hub — -5y55BOFAKA @ '
                                     '00:05:48].',
                                     'At month end, generate revenue journal entries first and only then '
                                     'run the deferred revenue reclassification, reconciling on the '
                                     'deferred revenue waterfall [CFO AI — MAsF2w47iew @ 00:04:55].']}}],
 'pull_quote': "'If an auditor pulled your biggest SaaS reseller contract today, would your topline "
               "revenue survive the control test?' — Jobank CPA (KjWijHo8iMI @ 00:07:14).",
 'diagram_id': 'diag-04',
 'action_checklist': ['Map each resold SKU to its unit of account (hosted SaaS access, a combined solution '
                      'with your own implementation, or an ordering and billing service) before running '
                      'the control test [Jobank CPA — KjWijHo8iMI @ 00:02:04].',
                      'Invoice annual deals into deferred revenue and release one-twelfth at each '
                      'month-end close, keeping booking, invoicing, cash receipt, and recognition as '
                      'separate events [The SaaS CFO — p4KgISWaH6s @ 00:08:12].',
                      'Hold any cash subject to a refund right in refund liability, reclassify it to '
                      'deferred revenue only after the right lapses, then post the cumulative catch-up '
                      '[Jobank CPA — WeV8GbQwaPE @ 00:05:09].',
                      'Classify every mid-term change as a new separate contract, a prospective '
                      'adjustment, or a cumulative catch-up by asking whether distinct goods are added at '
                      'standalone selling price [Ledger & Logic — lYs19gfynCE @ 00:04:24].',
                      'Configure items, revenue rules, and fair value price lists in NetSuite ARM so each '
                      'approved sales order spawns a revenue arrangement with actual and forecast plans '
                      '[RSM US LLP — Qxj-ooX7WrE @ 00:08:35].',
                      'Report renewal rate by dollars and count in each anniversary month alongside gross '
                      'and net revenue retention, and log a renewal as a booking only on net expansion '
                      '[The SaaS CFO — G9iKRE0cqZU @ 00:02:28].'],
 'statutory_citations': [{'title': 'Jobank CPA — Episode 16 ASC 606 Principal vs Agent Explained: Gross vs '
                                   'Net Revenue Rules [00:03:43]',
                          'url': 'https://www.youtube.com/watch?v=KjWijHo8iMI&t=223s',
                          'relevance': 'Primary practitioner testimony on principal-versus-agent control '
                                       'tests, the credit risk and flash title myths, and gross-versus-net '
                                       'revenue for SaaS resellers.'},
                         {'title': 'Jobank CPA — ASC 606 Revenue Recognition Edge Cases: Side Letters & '
                                   'Contract Enforceability (SaaS Accounting) [00:03:36]',
                          'url': 'https://www.youtube.com/watch?v=WeV8GbQwaPE&t=216s',
                          'relevance': 'Primary practitioner testimony on side letters, refund '
                                       'liabilities, and how a sales email wiped a $900,000 deal to $0 '
                                       'quarterly GAAP revenue.'},
                         {'title': 'Ambition, Aligned with Devon Coombs — Consumption Based Revenue '
                                   'Recognition: ASC 606 & Usage-Based Pricing (SaaS & Cloud Accounting) '
                                   '[00:04:31]',
                          'url': 'https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=271s',
                          'relevance': 'Primary practitioner testimony on ratable versus consumption '
                                       'recognition, overage estimates, breakage, and system limits for '
                                       'usage-based deals.'},
                         {'title': 'Accounting and Auditing Hub — SaaS Revenue Recognition Explained: IFRS '
                                   '15 & ASC 606 Case Study [00:05:33]',
                          'url': 'https://www.youtube.com/watch?v=-5y55BOFAKA&t=333s',
                          'relevance': 'Primary practitioner testimony on setup fee, stated price, and SLA '
                                       'variable consideration traps in a multi-element SaaS contract.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'KjWijHo8iMI',
                       'title': 'Episode 16 ASC 606 Principal vs Agent Explained: Gross vs Net Revenue '
                                'Rules',
                       'channel': 'Jobank CPA',
                       'author': 'Jobank CPA',
                       'text': 'The absolute biggest trap to avoid is assuming credit risk equals control; '
                               'ASC 606 intentionally removed credit risk as a primary indicator.',
                       'tip': 'The absolute biggest trap to avoid is assuming credit risk equals control; '
                              'ASC 606 intentionally removed credit risk as a primary indicator.',
                       'timestamp': 223,
                       'timestamp_seconds': 223,
                       'timestamp_label': '[00:03:43]',
                       'url': 'https://www.youtube.com/watch?v=KjWijHo8iMI&t=223s',
                       'markdown': '[00:03:43](https://www.youtube.com/watch?v=KjWijHo8iMI&t=223s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'p4KgISWaH6s',
                       'title': 'What is SaaS Revenue Recognition?',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': 'Companies without proper revenue recognition are debiting accounts '
                               "receivable and crediting revenue on their P&L, so they're taking the "
                               'entire twelve thousand as revenue in one month.',
                       'tip': 'Companies without proper revenue recognition are debiting accounts '
                              "receivable and crediting revenue on their P&L, so they're taking the entire "
                              'twelve thousand as revenue in one month.',
                       'timestamp': 305,
                       'timestamp_seconds': 305,
                       'timestamp_label': '[00:05:05]',
                       'url': 'https://www.youtube.com/watch?v=p4KgISWaH6s&t=305s',
                       'markdown': '[00:05:05](https://www.youtube.com/watch?v=p4KgISWaH6s&t=305s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SgRytNI-ALo',
                       'title': 'ASC 606 Simplified: Understanding Revenue Recognition in 3 Minutes',
                       'channel': 'Accounting Journal Entries',
                       'author': 'Accounting Journal Entries',
                       'text': 'A company provides a subscription service to customers for one hundred '
                               'dollars per month, and under ASC 606 the company would recognize revenue '
                               'of one hundred dollars per month when the customer pays for the '
                               'subscription.',
                       'tip': 'A company provides a subscription service to customers for one hundred '
                              'dollars per month, and under ASC 606 the company would recognize revenue of '
                              'one hundred dollars per month when the customer pays for the subscription.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=SgRytNI-ALo&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=SgRytNI-ALo&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lYs19gfynCE',
                       'title': 'ASC 606 Masterclass: Automating SaaS Revenue Recognition',
                       'channel': 'Ledger & Logic',
                       'author': 'Ledger & Logic',
                       'text': 'Weak contract management, especially around these messy mid-cycle '
                               'adjustments, costs companies an average of 9.2% of their annual revenue.',
                       'tip': 'Weak contract management, especially around these messy mid-cycle '
                              'adjustments, costs companies an average of 9.2% of their annual revenue.',
                       'timestamp': 231,
                       'timestamp_seconds': 231,
                       'timestamp_label': '[00:03:51]',
                       'url': 'https://www.youtube.com/watch?v=lYs19gfynCE&t=231s',
                       'markdown': '[00:03:51](https://www.youtube.com/watch?v=lYs19gfynCE&t=231s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I8dBdXuT7cA',
                       'title': "ASC 606 Revenue Recognition in Plain English: A CPA's Walkthrough of the "
                                '5-Step Model',
                       'channel': 'Accounting: Concierge CPA',
                       'author': 'Accounting: Concierge CPA',
                       'text': 'Big Tech had $120,000 in the bank on January 1st, and revenue on January '
                               '1st was zero, because revenue follows performance, not cash.',
                       'tip': 'Big Tech had $120,000 in the bank on January 1st, and revenue on January '
                              '1st was zero, because revenue follows performance, not cash.',
                       'timestamp': 739,
                       'timestamp_seconds': 739,
                       'timestamp_label': '[00:12:19]',
                       'url': 'https://www.youtube.com/watch?v=I8dBdXuT7cA&t=739s',
                       'markdown': '[00:12:19](https://www.youtube.com/watch?v=I8dBdXuT7cA&t=739s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7IqQXBLa14Y',
                       'title': 'Revenue Recognition ASC 606 & IFRS 15 — 5-Step Quality Test with AI ⭐ '
                                'mnainstitute.com',
                       'channel': '[mnainstitute.com] M&A Certification & Courses',
                       'author': '[mnainstitute.com] M&A Certification & Courses',
                       'text': 'The first is accounts receivable growing significantly faster than '
                               'revenue, which can indicate that sales are being recorded before customers '
                               'have actually committed to paying.',
                       'tip': 'The first is accounts receivable growing significantly faster than revenue, '
                              'which can indicate that sales are being recorded before customers have '
                              'actually committed to paying.',
                       'timestamp': 256,
                       'timestamp_seconds': 256,
                       'timestamp_label': '[00:04:16]',
                       'url': 'https://www.youtube.com/watch?v=7IqQXBLa14Y&t=256s',
                       'markdown': '[00:04:16](https://www.youtube.com/watch?v=7IqQXBLa14Y&t=256s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vPpXI4fjA1A',
                       'title': 'Revenue Recognition for SaaS Contracts under ASC 606',
                       'channel': 'Ordway',
                       'author': 'Ordway',
                       'text': 'One fat fingered number within one cell can corrupt it, one misplaced or '
                               'corrupted formula can destroy the whole thing, and with auditors the risk '
                               'of fraud is always very high in revenue.',
                       'tip': 'One fat fingered number within one cell can corrupt it, one misplaced or '
                              'corrupted formula can destroy the whole thing, and with auditors the risk '
                              'of fraud is always very high in revenue.',
                       'timestamp': 480,
                       'timestamp_seconds': 480,
                       'timestamp_label': '[00:08:00]',
                       'url': 'https://www.youtube.com/watch?v=vPpXI4fjA1A&t=480s',
                       'markdown': '[00:08:00](https://www.youtube.com/watch?v=vPpXI4fjA1A&t=480s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q0XhS1B8mWE',
                       'title': 'ASC 606 SaaS Basics - Revenue Recognition Podcast',
                       'channel': '12th & Norwegian',
                       'author': '12th & Norwegian',
                       'text': "If the platform sets the price and they're taking ownership of the food "
                               "before it's delivered, they're probably the principal.",
                       'tip': "If the platform sets the price and they're taking ownership of the food "
                              "before it's delivered, they're probably the principal.",
                       'timestamp': 980,
                       'timestamp_seconds': 980,
                       'timestamp_label': '[00:16:20]',
                       'url': 'https://www.youtube.com/watch?v=Q0XhS1B8mWE&t=980s',
                       'markdown': '[00:16:20](https://www.youtube.com/watch?v=Q0XhS1B8mWE&t=980s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WeV8GbQwaPE',
                       'title': 'ASC 606 Revenue Recognition Edge Cases: Side Letters & Contract '
                                'Enforceability (SaaS Accounting)',
                       'channel': 'Jobank CPA',
                       'author': 'Jobank CPA',
                       'text': 'Because of that one casual sales email granting a 100% refund, all of that '
                               'cash must be classified as a refund liability.',
                       'tip': 'Because of that one casual sales email granting a 100% refund, all of that '
                              'cash must be classified as a refund liability.',
                       'timestamp': 291,
                       'timestamp_seconds': 291,
                       'timestamp_label': '[00:04:51]',
                       'url': 'https://www.youtube.com/watch?v=WeV8GbQwaPE&t=291s',
                       'markdown': '[00:04:51](https://www.youtube.com/watch?v=WeV8GbQwaPE&t=291s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XcyrOPFaa6o',
                       'title': 'Does Expansion MRR or ARR Include Renewals? | SaaS Metrics School | '
                                'Renewals',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': "A renewal is a booking when we have net expansion: they're paying us "
                               '10,000 a year, we renew them at 13,000, and that net 3K expansion is an '
                               'expansion booking.',
                       'tip': "A renewal is a booking when we have net expansion: they're paying us 10,000 "
                              'a year, we renew them at 13,000, and that net 3K expansion is an expansion '
                              'booking.',
                       'timestamp': 32,
                       'timestamp_seconds': 32,
                       'timestamp_label': '[00:00:32]',
                       'url': 'https://www.youtube.com/watch?v=XcyrOPFaa6o&t=32s',
                       'markdown': '[00:00:32](https://www.youtube.com/watch?v=XcyrOPFaa6o&t=32s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G9iKRE0cqZU',
                       'title': 'How Do We Track Retention When We Offer Multi-year Contracts | SaaS '
                                'Metrics School | Retention',
                       'channel': 'The SaaS CFO',
                       'author': 'The SaaS CFO',
                       'text': 'In due diligence they look at a number and say, in May 2023 why was your '
                               'renewal rate 65% when gross revenue retention annually is 95%.',
                       'tip': 'In due diligence they look at a number and say, in May 2023 why was your '
                              'renewal rate 65% when gross revenue retention annually is 95%.',
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=G9iKRE0cqZU&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=G9iKRE0cqZU&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-5y55BOFAKA',
                       'title': 'SaaS Revenue Recognition Explained: IFRS 15 & ASC 606 Case Study',
                       'channel': 'Accounting and Auditing Hub',
                       'author': 'Accounting and Auditing Hub',
                       'text': 'Trap number one, the setup fee: never recognize administrative onboarding '
                               'fees upfront on day one, even if they are heavily billed and '
                               'non-refundable.',
                       'tip': 'Trap number one, the setup fee: never recognize administrative onboarding '
                              'fees upfront on day one, even if they are heavily billed and '
                              'non-refundable.',
                       'timestamp': 333,
                       'timestamp_seconds': 333,
                       'timestamp_label': '[00:05:33]',
                       'url': 'https://www.youtube.com/watch?v=-5y55BOFAKA&t=333s',
                       'markdown': '[00:05:33](https://www.youtube.com/watch?v=-5y55BOFAKA&t=333s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rm7beKRTRko',
                       'title': 'ASC 606: Revenue Recognition - Step 5 Recognize Revenue',
                       'channel': 'Accounting Academy',
                       'author': 'Accounting Academy',
                       'text': 'The correct answer is point in time due to the lack of an enforceable '
                               'right of payment.',
                       'tip': 'The correct answer is point in time due to the lack of an enforceable right '
                              'of payment.',
                       'timestamp': 190,
                       'timestamp_seconds': 190,
                       'timestamp_label': '[00:03:10]',
                       'url': 'https://www.youtube.com/watch?v=rm7beKRTRko&t=190s',
                       'markdown': '[00:03:10](https://www.youtube.com/watch?v=rm7beKRTRko&t=190s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MAsF2w47iew',
                       'title': 'NetSuite Advanced Revenue Management ASC 606 ARM',
                       'channel': 'CFO AI',
                       'author': 'CFO AI',
                       'text': 'First, you run the process that generates all the revenue journal entries '
                               'for the month, then, and only then, do you run the deferred revenue '
                               'reclassification.',
                       'tip': 'First, you run the process that generates all the revenue journal entries '
                              'for the month, then, and only then, do you run the deferred revenue '
                              'reclassification.',
                       'timestamp': 295,
                       'timestamp_seconds': 295,
                       'timestamp_label': '[00:04:55]',
                       'url': 'https://www.youtube.com/watch?v=MAsF2w47iew&t=295s',
                       'markdown': '[00:04:55](https://www.youtube.com/watch?v=MAsF2w47iew&t=295s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MAsF2w47iew',
                       'title': 'NetSuite Advanced Revenue Management ASC 606 ARM',
                       'channel': 'CFO AI',
                       'author': 'CFO AI',
                       'text': 'First, you have to switch the feature on, and this is a one-way street; '
                               "once it's on, it's on for good.",
                       'tip': 'First, you have to switch the feature on, and this is a one-way street; '
                              "once it's on, it's on for good.",
                       'timestamp': 115,
                       'timestamp_seconds': 115,
                       'timestamp_label': '[00:01:55]',
                       'url': 'https://www.youtube.com/watch?v=MAsF2w47iew&t=115s',
                       'markdown': '[00:01:55](https://www.youtube.com/watch?v=MAsF2w47iew&t=115s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Qxj-ooX7WrE',
                       'title': 'NetSuite Advanced Revenue Management (ARM) demo | ASC 606 overview for '
                                'NetSuite users',
                       'channel': 'RSM US LLP',
                       'author': 'RSM US LLP',
                       'text': "If you've started to recognize revenue and you find out that you need to "
                               'extend your revenue recognition terms, you can update all periods with one '
                               'cumulative catch-up or update the remaining periods only.',
                       'tip': "If you've started to recognize revenue and you find out that you need to "
                              'extend your revenue recognition terms, you can update all periods with one '
                              'cumulative catch-up or update the remaining periods only.',
                       'timestamp': 281,
                       'timestamp_seconds': 281,
                       'timestamp_label': '[00:04:41]',
                       'url': 'https://www.youtube.com/watch?v=Qxj-ooX7WrE&t=281s',
                       'markdown': '[00:04:41](https://www.youtube.com/watch?v=Qxj-ooX7WrE&t=281s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B4Ckh2wjlgc',
                       'title': 'Consumption Based Revenue Recognition: ASC 606 & Usage-Based Pricing '
                                '(SaaS & Cloud Accounting)',
                       'channel': 'Ambition, Aligned with Devon Coombs',
                       'author': 'Ambition, Aligned with Devon Coombs',
                       'text': "I've gone and pitched to every single major revenue operation system and "
                               'said, is there a way to solve this, and they say no.',
                       'tip': "I've gone and pitched to every single major revenue operation system and "
                              'said, is there a way to solve this, and they say no.',
                       'timestamp': 2362,
                       'timestamp_seconds': 2362,
                       'timestamp_label': '[00:39:22]',
                       'url': 'https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=2362s',
                       'markdown': '[00:39:22](https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=2362s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B4Ckh2wjlgc',
                       'title': 'Consumption Based Revenue Recognition: ASC 606 & Usage-Based Pricing '
                                '(SaaS & Cloud Accounting)',
                       'channel': 'Ambition, Aligned with Devon Coombs',
                       'author': 'Ambition, Aligned with Devon Coombs',
                       'text': "More than 50% of companies were doing it ratably before, and I've been "
                               'seeing more and more companies flip over to a consumption type model.',
                       'tip': "More than 50% of companies were doing it ratably before, and I've been "
                              'seeing more and more companies flip over to a consumption type model.',
                       'timestamp': 271,
                       'timestamp_seconds': 271,
                       'timestamp_label': '[00:04:31]',
                       'url': 'https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=271s',
                       'markdown': '[00:04:31](https://www.youtube.com/watch?v=B4Ckh2wjlgc&t=271s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
