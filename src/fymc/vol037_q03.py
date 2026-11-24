from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'distributor-marketplaces-msp-margin-engine',
 'question_prompt': 'How do MSPs and resellers use cloud distributors such as Pax8 and Ingram Micro to '
                    'build a profitable recurring-revenue software resale business, and where do VARs '
                    'still add value?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Distributor Marketplaces and the MSP Margin Engine: Pax8, Ingram Micro, and the VAR Model',
 'subtitle': 'Pax8 as a cloud distributor and marketplace demo, MSP integrations, portfolio-based margin '
             'analysis, go-to-market design, packaging security add-ons into services, cybersecurity '
             'attach-rate sales, Ingram Micro reseller transformations with Cisco and IBM/AWS, and the '
             'debate over whether value-added resellers earn their margin',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Distributor practitioners converge on one engine: the MSP buys Microsoft and '
                      'third-party cloud through a marketplace like Pax8 or Ingram Micro, then earns its '
                      "real margin on wrapped services, not on the licence. Pax8's co-founder cites IDC's "
                      '$4.14 of services attached per $1 of Microsoft cloud, while the Pax8 profitability '
                      'playbook demands at least 30% margin on security, RMM and non-Microsoft licensing '
                      'and 60% on managed support. Street mechanics centre on reconciling the M365 tenant, '
                      'billing engine and PSA, where one US client recovered $130,000 a year, plus '
                      'per-client delta analysis from MSP CFO. Security bundles sold opt-out with a signed '
                      'waiver push MDR adoption past 90%. Disagreement runs on whether VARs earn their '
                      'slice: TC2 calls resale low margin and demands markup transparency, while a Tech '
                      'Field Day panel splits on whether resellers are useless or time-saving brokers.',
 'key_metrics': [{'label': 'Services Attached Per $1 of Microsoft Cloud',
                  'metric': 'Services Attached Per $1 of Microsoft Cloud',
                  'value': '$4.14 of services per $1 of Microsoft cloud sold',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Pax8 co-founder citing IDC on what successful MSPs attach to every Microsoft '
                             'cloud dollar they resell.',
                  'source': 'Cloud Software Association ([phXe8eJoVeo @ 00:13:15])'},
                 {'label': 'Margin Floor on Security, RMM and Non-Microsoft Licensing',
                  'metric': 'Margin Floor on Security, RMM and Non-Microsoft Licensing',
                  'value': 'At least 30% margin, not markup',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Pax8 profitability playbook for MSPs; best-in-class firms also clear at '
                             'least 60% margin on managed support services.',
                  'source': 'Pax8 ([KcmWalqZBzk @ 00:01:54])'},
                 {'label': 'Annual Savings From Tenant, Billing and PSA Reconciliation',
                  'metric': 'Annual Savings From Tenant, Billing and PSA Reconciliation',
                  'value': '$130,000 per year for one US client',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Pax8 demo team on closing gaps between the M365 tenant, the Xero billing '
                             'engine and the PSA, gaps that run into tens of thousands.',
                  'source': 'Tubblog - The Hub for MSPs ([NVSw5ZYgQzw @ 00:14:03])'},
                 {'label': 'Opt-Out MDR and SOC Campaign Adoption Rate',
                  'metric': 'Opt-Out MDR and SOC Campaign Adoption Rate',
                  'value': 'Over 90% opt-in adoption',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Blackpoint Europe reporting adoption when customers must sign a waiver to '
                             'decline MDR and SOC coverage.',
                  'source': 'Magic Chats ([fM8cQVJ3oh8 @ 00:08:39])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The baseline every distributor-side operator repeats is that software '
                              'reaches small and mid-market buyers through the channel, not around it. The '
                              'Pax8 co-founder learned this at MX Logic, which sold direct, entered the '
                              'channel badly and only grew once it added channel partners; they now '
                              'dismiss the beliefs that all customers will buy direct, that marketplaces '
                              'will replace the channel, and that distribution is dead [phXe8eJoVeo @ '
                              "00:04:02]. TC2's Joe Schmidt and Ben Fox put it bluntly from the "
                              'procurement side: a company buying Cisco network equipment very rarely buys '
                              'direct from Cisco, because OEMs sell through channel partners and VARs are '
                              "close to unavoidable [6YNd6Xcyekw @ 00:01:16]. Ingram Micro's IBM alliance "
                              'conversation extends the same logic to hyperscaler marketplaces, where IBM '
                              'software such as HashiCorp and Apptio now transacts through AWS Marketplace '
                              'via Ingram, and deals close about 27% quicker and land larger because '
                              'customers themselves are pushing marketplace buying [ZoUkvQ-5m3c @ '
                              '00:02:21]. Bob Park frames the vendor side of the same funnel: one phone '
                              'call to set up an account with a distributor such as Ingram Micro or Tech '
                              'Data gives a manufacturer access to thousands of resellers, which beats '
                              'funding a cold-calling squad that needs capital and resources before any '
                              'revenue arrives [z-ZzUEITMGM @ 00:04:12].',
                              'Practitioners also agree on where the money actually sits: the licence is '
                              "the entry ticket, and the service wrapped around it is the margin. Pax8's "
                              'profitability playbook tells MSPs to hold at least 30% margin, not markup, '
                              'on security, RMM and non-Microsoft licensing, and says best-in-class firms '
                              'clear at least 60% margin on managed support services [KcmWalqZBzk @ '
                              '00:01:54]. Because Microsoft 365 margins are capped and lower, the same '
                              'playbook folds M365 support cost into the services line rather than hoping '
                              'the licence pays for it [KcmWalqZBzk @ 00:02:35]. The Pax8 co-founder backs '
                              "this with IDC's finding that successful MSPs attach $4.14 of services for "
                              'every $1 of Microsoft cloud sold, and adds that MSPs with more than half '
                              'their revenue from cloud see 2x revenue, 1.8x growth and 1.5x profit '
                              '[phXe8eJoVeo @ 00:13:15]. Dan Harris Mills of Highlander Computing '
                              'Solutions lived the shift: before Azure their firm was a commoditized '
                              "box-shifter, and after building the Azure go-to-market with Ingram Micro's "
                              'pre-sales technical resources and marketing, customers started treating '
                              'them as an advisor, a jump that began with the CSP move Highlander had put '
                              'off for a long time [bGmD7XlTNZI @ 00:02:02].',
                              'The third point of agreement is that a distributor earns its slot by '
                              'carrying operational load the MSP cannot staff itself. The Pax8 co-founder '
                              'lists what they had to build: a partner console with a multi-customer view, '
                              'monthly billing with proration and co-termination instead of anniversary '
                              'billing, and provisioning, billing and consumption APIs wired into '
                              'ConnectWise, Autotask and Kaseya, while warning that the real challenge is '
                              'quote-to-cash, not just selling [phXe8eJoVeo @ 00:28:13]. Phylip Morgan '
                              'demos the result as a self-serve portal to provision, bill, manage and '
                              'analyse, and calls instant provisioning a tagline that holds up in '
                              'practice, roughly two minutes from click to the Office portal [NVSw5ZYgQzw '
                              "@ 00:23:50]. Nick Heddy, Pax8's CRO and employee number eight, sells the "
                              'human layer as wingman support: 24x7 US-based L2 and L3 support with no '
                              'finger pointing, and Heddy tells doubters to check Reddit for raw partner '
                              'feedback [hsCUDuKzpaw @ 00:06:16]. Ingram Micro pitches the same backbone '
                              'alongside Cisco, reframing itself from traditional distributor to platform '
                              'company through Xvantage and running a CARE program built to cut churn and '
                              'raise lifetime value in recurring models, backed by a free Advanced '
                              'Solutions Integration Lab for demos and attack simulations [ADZwWSQGFFI @ '
                              '00:04:33].'],
               'table': {'caption': 'Where distributor, MSP and VAR practitioners line up on the channel '
                                    'margin engine',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Channel beats direct for SMB software vendors',
                                   'MX Logic sold direct, entered the channel badly, and only grew after '
                                   'adding channel partners',
                                   'Route vendor products through distributors and MSPs instead of around '
                                   'them',
                                   'Cloud Software Association ([phXe8eJoVeo @ 00:04:02])'],
                                  ['Licence margin is thin and Microsoft is capped',
                                   'Hold at least 30% margin, not markup, on security, RMM and '
                                   'non-Microsoft licensing',
                                   'Fold capped Microsoft 365 support costs into the managed services '
                                   'price',
                                   'Pax8 ([KcmWalqZBzk @ 00:01:54])'],
                                  ['Services attach drives the real MSP economics',
                                   'Successful MSPs attach $4.14 of services per $1 of Microsoft cloud '
                                   'sold',
                                   'Treat every licence sale as the entry point for attached services '
                                   'revenue',
                                   'Cloud Software Association ([phXe8eJoVeo @ 00:13:15])'],
                                  ['Marketplace buying accelerates enterprise deal velocity',
                                   'IBM deals through AWS Marketplace via Ingram close about 27% quicker '
                                   'and run larger',
                                   'Bring opportunities early so Ingram, IBM and AWS reps join the calls',
                                   'Ingram Micro Canada ([ZoUkvQ-5m3c @ 00:02:21])'],
                                  ['Cloud moves turn box-shifters into trusted advisors',
                                   'Highlander went from commoditized box-shifter to advisor after Azure '
                                   'with Ingram support',
                                   'Lean on distributor pre-sales technical resources and marketing to '
                                   'launch Azure',
                                   'Ingram Micro Cloud UK ([bGmD7XlTNZI @ 00:02:02])'],
                                  ['Distributor support substitutes for in-house specialist headcount',
                                   'Pax8 wingman offers 24x7 US-based L2 and L3 support with no finger '
                                   'pointing',
                                   'Escalate vendor issues to distributor support instead of staffing '
                                   'every specialty',
                                   'Channel Talk ([hsCUDuKzpaw @ 00:06:16])'],
                                  ['VARs are nearly unavoidable in hardware procurement',
                                   'Buying Cisco network equipment direct from Cisco is very unusual for '
                                   'companies',
                                   'Build VAR selection and markup control into every hardware purchase '
                                   'cycle',
                                   'Staying Connected ([6YNd6Xcyekw @ 00:01:16])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The core mechanic Pax8's demo team teaches is reconciling the holy trinity: "
                              'the Microsoft 365 tenant, the billing engine such as Xero, and the PSA. '
                              'Left unsynced, gaps between those three systems run into the tens of '
                              'thousands, and one US client saved $130,000 a year once they were closed '
                              '[NVSw5ZYgQzw @ 00:14:03]. Setup is quick: the PSA integration takes 10 to '
                              '15 minutes using an API user with a public and private key, with formal '
                              'integrations for ConnectWise, Autotask, Syncro, Tigerpaw and RepairShopr '
                              'plus open APIs; the operator then binds each company and product one-to-one '
                              'and exports products with MSRP pre-populated [NVSw5ZYgQzw @ 00:16:35]. '
                              'Billing sync is one-way, pushing quantity changes and recurring additions, '
                              'with two-way sync reserved for Pax8 Pro. Ordering supports future effective '
                              'dates, $0 line items for bundles and auto-proration, a seat change from 10 '
                              'to 11 took about 30 seconds on screen, and Pax8 can generate PDF invoices '
                              'for Xero batch import [NVSw5ZYgQzw @ 01:00:32]. The Pax8 co-founder lists '
                              'the plumbing that matters more than the catalogue: monthly billing with '
                              'proration and co-termination, plus provisioning, billing and consumption '
                              'APIs, are what MSPs need to get through quote-to-cash [phXe8eJoVeo @ '
                              '00:21:57].',
                              "Larry Cobran of MSP CFO supplies the per-client math. Cobran's portfolio "
                              'method treats clients like stores: five stores averaging 18% move to 20% '
                              'just by lifting the one 6% outlier to 16%, and outliers hide across '
                              'clients, agreements, engineers and ticket types. The delta compares the '
                              'labor portion of an agreement against shadow billable value: a $3,000 labor '
                              'portion against 20 hours at $200, or $4,000, is a negative delta meaning '
                              'the client is overserved or underpriced [TxvzhnvDnxA @ 00:07:18]. One real '
                              '2024 client was only $21,000 off in aggregate, yet the bottom five clients '
                              'made up 12.3% of managed-service revenue. The data only works if techs log '
                              '100% of hours against at least an eight-hour day, for example 6.7 hours of '
                              'client work plus 1.3 hours admin, and never mark agreement-covered work as '
                              'non-billable [TxvzhnvDnxA @ 00:16:57]. Root cause then runs through revenue '
                              'per endpoint, billable per hour, hours per ticket and tickets per endpoint, '
                              'against an agreement-efficiency target of 1.2 to 1.3 where the example sat '
                              "at 0.75 [TxvzhnvDnxA @ 00:18:22]. Pax8's profitability playbook closes the "
                              'loop: inspect margins consistently through PSA and MSP CFO dashboards and '
                              'raise rates gradually on unprofitable clients [KcmWalqZBzk @ 00:01:18].',
                              'The packaging mechanic that turns a thin licence into a service is the '
                              "opt-out bundle. Josh, who worked Pax8's go-to-market team before joining "
                              'Usecure, found UK MSPs already owned the tools but bolted them on as a '
                              'two-quid-a-month add-on with no service wrap; the fix is good, better, best '
                              'tiers, with a waiver for any client who declines the recommended tier '
                              '[oQIMe7F_kaw @ 00:05:23]. Sham of Blackpoint Europe runs the same play for '
                              'MDR and SOC: the customer must sign a waiver to decline, and opt-in '
                              "adoption runs over 90%; Blackpoint's account management team builds the "
                              'waiver and pre-renewal conversations, and fence-sitters get a 180-day '
                              'historical scan showing prior compromise such as wire-fraud prerequisites '
                              '[fM8cQVJ3oh8 @ 00:08:39]. Pax8 arms the upsell with data: Pax8 Pro uses '
                              'Microsoft APIs to flag clients buying a la carte instead of the M365 '
                              'Business Premium bundle, idle resource groups and unused E5 security '
                              'features, then generates SOW templates to pull through professional '
                              'services [hsCUDuKzpaw @ 00:03:10]. The white-label MCAT report runs in one '
                              'to two minutes, self-deletes after 30 days, and in the demo surfaced a '
                              '241-a-month saving framed to the client as two grand over 12 months '
                              '[NVSw5ZYgQzw @ 00:57:26].'],
               'table': {'caption': 'Street-level settings, benchmarks and pricing mechanics practitioners '
                                    'run',
                         'headers': ['Mechanic',
                                     'Exact Number or Setting',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['PSA integration setup with API keys',
                                   '10 to 15 minutes using an API user with public and private key',
                                   'Bind each company and product one-to-one before the first billing sync',
                                   'Tubblog - The Hub for MSPs ([NVSw5ZYgQzw @ 00:16:35])'],
                                  ['Margin floor on the non-Microsoft stack',
                                   'At least 30% margin, not markup, on security, RMM and licensing',
                                   'Reprice any tool falling under the floor after inspecting per-client '
                                   'profitability',
                                   'Pax8 ([KcmWalqZBzk @ 00:01:54])'],
                                  ['Managed support services margin benchmark',
                                   'At least 60% margin for best-in-class managed support services',
                                   'Inspect margins consistently through PSA and MSP CFO dashboards',
                                   'Pax8 ([KcmWalqZBzk @ 00:02:14])'],
                                  ['Client delta against shadow billable value',
                                   '$3,000 labor portion versus $4,000 shadow billable at 20 hours times '
                                   '$200',
                                   'Flag overserved or underpriced clients and route revenue issues to '
                                   'account management',
                                   'Pax8 ([TxvzhnvDnxA @ 00:07:18])'],
                                  ['Agreement efficiency target per client',
                                   'Target 1.2 to 1.3 against an example client sitting at 0.75',
                                   'Deconstruct revenue per endpoint, hours per ticket and tickets per '
                                   'endpoint',
                                   'Pax8 ([TxvzhnvDnxA @ 00:18:22])'],
                                  ['Opt-out MDR and SOC security campaign',
                                   'Opt-in adoption over 90% when declining requires a signed waiver',
                                   'Default every client into MDR and make refusal a written decision',
                                   'Magic Chats ([fM8cQVJ3oh8 @ 00:08:39])'],
                                  ['VAR resale markup mechanics on OEM discount',
                                   'OEM 60% discount reduced to 58% instead of a cost-plus markup',
                                   'Demand transparent pricing because 1% markup differs from 1% discount '
                                   'cut',
                                   'Staying Connected ([6YNd6Xcyekw @ 00:03:54])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Margin Leaks Operators Plug Before Chasing New Logos',
                           'body': 'These are the small operational moves practitioners use to make '
                                   'distributor data, cloud spend and AI tooling pay off inside existing '
                                   'accounts.',
                           'items': ['Never mark agreement-covered work as non-billable, and log 100% of '
                                     'hours against at least an eight-hour day so the delta report '
                                     'reflects real client cost [Pax8 — TxvzhnvDnxA @ 00:17:30].',
                                     'Fix the client before firing them: the law-firm case had normal '
                                     'revenue per endpoint but high ticket counts, solved with '
                                     'lunch-and-learns instead of a price increase [Pax8 — TxvzhnvDnxA @ '
                                     '00:25:05].',
                                     'Give committed AWS spend a home in IBM products like Maximo and '
                                     'Apptio when customer projects ebb, and push Q4 deals where AWS '
                                     'credits a percentage of deal size to the customer [Ingram Micro '
                                     'Canada — ZoUkvQ-5m3c @ 00:03:30].',
                                     'Generate an MCP token under Settings then Integrations, and run a '
                                     'read-only query for renewals in the next 30 days to surface a '
                                     'Defender upsell recommendation [Pax8 — P960HFmyakQ @ 00:10:42].']},
               'sop_steps': [{'step': 1,
                              'title': 'Wire the Holy Trinity',
                              'action': 'Connect the PSA to Pax8 and bind every company and product before '
                                        'billing.',
                              'detail': 'Create an API user with a public and private key, connect '
                                        'ConnectWise, Autotask, Syncro, Tigerpaw or RepairShopr in 10 to '
                                        '15 minutes, bind companies and products one-to-one, export '
                                        'products with MSRP pre-populated, and reconcile tenant, Xero and '
                                        'PSA [Tubblog - The Hub for MSPs — NVSw5ZYgQzw @ 00:15:04].'},
                             {'step': 2,
                              'title': 'Set Margin Floors by Product Line',
                              'action': 'Price the stack to margin, not markup, and absorb Microsoft 365 '
                                        'support into services.',
                              'detail': 'Know your goods, tools and people costs, hold at least 30% margin '
                                        'on security, RMM and non-Microsoft licensing, target at least 60% '
                                        'on managed support, and fold capped M365 support cost into the '
                                        'services price [Pax8 — KcmWalqZBzk @ 00:01:54].'},
                             {'step': 3,
                              'title': 'Run the Client Delta Report',
                              'action': 'Pull the top and bottom five clients and compare delta across '
                                        '3-month windows.',
                              'detail': 'Use the free MSP CFO insights report to rank clients by delta, '
                                        'compare 3-month windows, then route operations issues to '
                                        'operations and revenue issues to account management [Pax8 — '
                                        'TxvzhnvDnxA @ 00:15:30].'},
                             {'step': 4,
                              'title': 'Package Security as an Opt-Out Bundle',
                              'action': 'Default clients into MDR and SOC inside good, better, best tiers '
                                        'with a decline waiver.',
                              'detail': 'Require a signed waiver to decline MDR and SOC coverage, build '
                                        'the waiver into pre-renewal conversations, and use a 180-day '
                                        'historical scan to move fence-sitters [Magic Chats — fM8cQVJ3oh8 '
                                        '@ 00:08:22].'}]},
              {'heading': '3. Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split is whether the middleman earns its cut at all. Tech Field '
                              "Day Plus opened its roundtable on the premise that 'resellers are useless,' "
                              'with critics favoring a direct sales model and faulting the account manager '
                              "who takes 'a thin slice off the top' [oB21xupXerM @ 00:01:14]. The VAR-side "
                              "panelists concede that 'some resellers are useless' when the buyer only "
                              'wants a box. They then counter with the insurance-broker play: a VAR tracks '
                              'discount programs and incentives that a customer buying every three to four '
                              'years cannot follow, and earns its keep when the customer is unfamiliar '
                              'with the technology [oB21xupXerM @ 00:05:14]. The Pax8 co-founder speaking '
                              'to the Cloud Software Association attacks the direct thesis from the vendor '
                              'side. The co-founder disputes that all customers will buy direct, that '
                              'marketplaces will replace the channel, or that distribution is dead, and '
                              'warns that MX Logic sold direct, entered the channel badly, and only grew '
                              "once it added the channel [phXe8eJoVeo @ 00:04:02]. TC2's Joe Schmidt and "
                              'Ben Fox treat the question as settled by structure rather than ideology. '
                              'OEMs sell through channel partners and buying Cisco equipment direct is '
                              "'very unusual,' so the live choice is between resale specialists such as "
                              'SHI and WWT and carriers or systems integrators that offer resale as a '
                              'complement [6YNd6Xcyekw @ 00:01:46].',
                              "Stack architecture splits the Pax8 camp itself. The co-founder's lesson "
                              'list calls for a partner management console with a multi-customer view, so '
                              'the MSP runs every customer from one place [phXe8eJoVeo @ 00:21:02]. Phylip '
                              "Morgan, demoing for Tubblog, rejects that framing outright: 'single pane of "
                              "glass is anathema.' Morgan's reasoning is that an MSP carries five roles "
                              '(sales and marketing, operations, finance, technical, and the CEO), and '
                              'each one needs its own dashboard [NVSw5ZYgQzw @ 00:07:15]. On vendor count, '
                              'Nick Heddy describes the typical MSP as running four to five vendors with '
                              'Microsoft as the core. Heddy pitches Pax8 Stacks to surface cross-sell gaps '
                              'across names like SentinelOne, Proofpoint, Azure migrations, and '
                              'RingCentral [hsCUDuKzpaw @ 00:04:45]. Josh, who worked mostly with SMB MSPs '
                              'on the Pax8 go-to-market team before joining usecure, pulls the opposite '
                              "direction. In Josh's view, tool sprawl and inherited tooling are the "
                              'problem, so the answer is to consolidate and build the stack around the '
                              'human, starting at the bottom with email security, M365 or Google Workspace '
                              'backup, web filtering, VPN, and ITDR [oQIMe7F_kaw @ 00:07:41]. The contrast '
                              'for an operator is expansion driven by marketplace gap analysis versus '
                              'consolidation driven by the people delivering the service. Both playbooks '
                              "come out of the same distributor's orbit, and both are taught to the same "
                              'partner base.',
                              'Fixing an underpriced book of clients produces two different playbooks. The '
                              'Pax8 profitability brief says to inspect per-client profitability and raise '
                              'rates gradually on unprofitable existing clients. It also says to hold at '
                              'least 30% margin, not markup, on security, RMM, and non-Microsoft licensing '
                              '[KcmWalqZBzk @ 00:01:18]. Larry Cobran of MSP CFO pushes price to the back '
                              "of the line: 'firing a client is like your 10th decision,' so start with "
                              "fixing the client. In Cobran's law-firm case, revenue per endpoint was "
                              'normal but ticket counts ran high, and the fix was lunch-and-learns rather '
                              'than a price increase [TxvzhnvDnxA @ 00:26:05]. Security packaging splits '
                              "the same way. Josh at usecure found UK MSPs bolting tools on as a 'two quid "
                              "a month' add-on. Josh's motion names 'fear selling' and lands on good, "
                              'better, best three-tier packaging, with a waiver for clients who decline '
                              'the recommended tier [oQIMe7F_kaw @ 00:05:23]. Sham at Blackpoint goes '
                              'further with an opt-out campaign: the customer must sign a waiver to '
                              'decline MDR and SOC, and Sham reports the opt-in adoption rate at over 90% '
                              '[fM8cQVJ3oh8 @ 00:08:39]. Tiered choice keeps a cheaper rung on the table. '
                              'Opt-out removes the decision entirely unless the client signs away cover in '
                              'writing.'],
               'table': {'caption': 'Side-by-side playbooks where Q3 practitioners split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Buy direct from the vendor or through a VAR',
                                   'Critics favor direct sales and fewer middlemen, calling the account '
                                   "manager's cut a thin slice off the top",
                                   'MX Logic sold direct, entered the channel badly, and only grew after '
                                   'adding channel partners',
                                   'Tech Field Day Plus ([oB21xupXerM @ 00:01:14]); Cloud Software '
                                   'Association ([phXe8eJoVeo @ 00:04:02])'],
                                  ['How MSP operators should view their portfolio data',
                                   'Build one partner management console with a multi-customer view across '
                                   'every tenant',
                                   'Single pane of glass is anathema; give five MSP roles their own '
                                   'separate dashboards',
                                   'Cloud Software Association ([phXe8eJoVeo @ 00:21:02]); Tubblog - The '
                                   'Hub for MSPs ([NVSw5ZYgQzw @ 00:07:15])'],
                                  ['What to do with unprofitable or underpriced clients',
                                   'Inspect per-client profitability, then raise rates gradually on '
                                   'unprofitable existing clients',
                                   'Firing is the 10th decision; fix the client first, as lunch-and-learns '
                                   'did for a law firm',
                                   'Pax8 ([KcmWalqZBzk @ 00:01:18]); Pax8 / MSP CFO ([TxvzhnvDnxA @ '
                                   '00:26:05])'],
                                  ['How to package security services for SMB customers',
                                   'Good, better, best three tiers with a waiver when the client declines '
                                   'the recommendation',
                                   'Opt-out MDR and SOC campaign where declining requires a signed waiver, '
                                   'with over 90% opt-in',
                                   'usecure ([oQIMe7F_kaw @ 00:05:23]); Magic Chats ([fM8cQVJ3oh8 @ '
                                   '00:08:39])'],
                                  ['How VARs and distributors build their resale margin',
                                   'VAR takes a percentage markup on net cost, or trims the OEM discount '
                                   'from 60% to 58%',
                                   'Manufacturer sells into distribution at a standard 30 to 40% discount '
                                   'off end-user value',
                                   'Staying Connected ([6YNd6Xcyekw @ 00:04:10]); bobvalueadded '
                                   '([z-ZzUEITMGM @ 00:06:11])'],
                                  ['Whether the VAR account manager adds real value',
                                   'Account managers drink and play golf while customers pay for the '
                                   'relationship overhead',
                                   'The same account managers maximize vendor discounts, and the value-add '
                                   "is saving the buyer's time",
                                   'Tech Field Day Plus ([oB21xupXerM @ 00:09:11]); Tech Field Day Plus '
                                   '([oB21xupXerM @ 00:08:55])'],
                                  ['Whether to prioritize creativity or consistency in go-to-market',
                                   'Amanda says consistency over creativity sounds crazy at first, and '
                                   'Scott still values creativity',
                                   'Four out of five employees should describe the same approach before '
                                   'you scale it',
                                   'Pax8 ([_98wIAhek0M @ 00:17:12]); Pax8 ([_98wIAhek0M @ 00:16:57])']]}},
              {'heading': '4. Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures are timing failures. The Pax8 co-founder warns '
                              'that MX Logic sold direct, entered the channel badly, and only grew after '
                              'adding it. The fix is the 18 month rule: commit long-term, because '
                              "unassisted 'Bluebirds' only start landing around the eighth assisted deal "
                              '[phXe8eJoVeo @ 00:18:08]. The same talk flags an internal sabotage loop in '
                              'which reps earned more by avoiding channel margin, which is why channel '
                              'sales need positive comp. It closes on the warning that the real challenge '
                              'is quote-to-cash, not just selling [phXe8eJoVeo @ 00:28:13]. Dan Harris '
                              "Mills of Highlander Computing Solutions admits the firm 'put off for a long "
                              "time' the CSP move Microsoft wanted. Highlander then leaned on Ingram Micro "
                              'Cloud for pre-planning, customer conversations, pre-sales technical '
                              'resources, and Azure marketing. Only after that did it stop being a '
                              "'commoditized' box-shifter and start being treated by customers as an "
                              'advisor [bGmD7XlTNZI @ 00:01:16]. Bob Park describes the capital trap on '
                              'the manufacturer side of the VAR model: a cold-calling squad needs capital '
                              "and resources before any revenue arrives. Park's phase one is a single "
                              'phone call to open an account with a distributor such as Ingram Micro or '
                              'Tech Data, which gives access to thousands of VARs [z-ZzUEITMGM @ '
                              '00:03:49]. In each case, months pass before the channel pays back.',
                              'Margin leaks quietly through billing and time data. Phylip Morgan describes '
                              'the holy trinity of the M365 tenant, the Xero billing engine, and the PSA '
                              "drifting apart. Reconciliation gaps reach '10s of 1000s,' and one US client "
                              'saved $130,000 a year once the three were synced [NVSw5ZYgQzw @ 00:14:03]. '
                              "Larry Cobran's MSP CFO data shows how an aggregate number hides the damage. "
                              'A real 2024 client was only $21K off overall, yet its bottom five clients '
                              "were 12.3% of managed-service revenue [TxvzhnvDnxA @ 00:09:33]. Cobran's "
                              'warning on the input side is blunt: do not mark agreement-covered work as '
                              'non-billable, and log 100% of hours on at least an 8-hour day. The '
                              'shadow-billable delta depends on that data, and in the worked example '
                              'agreement efficiency sat at 0.75 against a 1.2 to 1.3 target [TxvzhnvDnxA @ '
                              '00:17:30]. The Pax8 profitability brief adds the structural squeeze: '
                              'Microsoft 365 margins are capped and lower. That means M365 support costs '
                              'have to be folded into services pricing, then inspected consistently '
                              'through the PSA and MSP CFO dashboards [KcmWalqZBzk @ 00:02:35]. An MSP '
                              'that skips any of these checks prices from a blended average that masks its '
                              'worst accounts.',
                              'Commercial traps sit in the fine print and the comp plan. Josh at usecure '
                              "saw UK MSPs who held the right tools but pushed them as a 'two quid a "
                              "month' add-on with no service wrap. Their problem was getting those tools "
                              'into their customers in a form the client understood [oQIMe7F_kaw @ '
                              '00:04:03]. On hardware and software resale, TC2 warns that VAR resale is '
                              'good for revenue but a low-margin business. A quote should carry only '
                              'shipping and sales tax; import duties, customs, broker, FX-hedging, '
                              'logistics, and management fees are the padding to strike out [6YNd6Xcyekw @ '
                              '00:05:38]. The same pair found that logistics and tax variance can exceed '
                              'markup variance. Their answer is multiple quotes per transaction, itemised '
                              "'taxes,' and direct OEM relationships kept alive for price negotiation "
                              '[6YNd6Xcyekw @ 00:08:02]. The Tech Field Day panel explains why VAR reps '
                              'push the wrong box. Compensation is tied to quarterly numbers, publicly '
                              'traded VARs face investor scrutiny every 90 days, and a missed number means '
                              "a 'pink slip.' That pressure is how a customer ends up pitched a "
                              'four-spatial-stream mGig flagship access point it never needed [oB21xupXerM '
                              "@ 00:12:33]. The panel's remedy is to escalate to the rep's boss, and it "
                              'notes that VARs can fire customers too.'],
               'table': {'caption': 'Firsthand traps and the economics check each practitioner applies',
                         'headers': ['Trap', 'What Practitioners Saw', 'Economics Check', 'Expert Source'],
                         'rows': [['Treating the most efficient clients as safe revenue',
                                   'Cobran reports the highest efficiency clients churn more often than '
                                   'the average client',
                                   'Review the top five clients alongside the bottom five in the free '
                                   'insights report',
                                   'Pax8 ([TxvzhnvDnxA @ 00:11:06])'],
                                  ['Marking agreement-covered work as non-billable in the PSA',
                                   'The value delta breaks when covered hours are hidden or days are '
                                   'under-logged',
                                   'Log 100% of hours on an 8-hour day, such as 6.7h client work plus 1.3h '
                                   'admin',
                                   'Pax8 ([TxvzhnvDnxA @ 00:17:30])'],
                                  ['Assuming your PSA already connects to MSP CFO',
                                   'Cobran lists ConnectWise and Autotask, then says right now only '
                                   'Autotask can connect',
                                   'Confirm the live connector during the one-hour real demo before '
                                   'committing',
                                   'Pax8 ([TxvzhnvDnxA @ 00:28:54])'],
                                  ['Letting the M365 tenant, Xero, and PSA drift apart',
                                   'Gaps reached tens of thousands, and one US client saved $130,000 a '
                                   'year after syncing',
                                   'Bind companies and products one-to-one, and note that billing sync is '
                                   'one-way',
                                   'Tubblog - The Hub for MSPs ([NVSw5ZYgQzw @ 00:14:03])'],
                                  ['Chasing too many vendors, offers, and ideas at once',
                                   'Convoluted messaging, a randomized pipeline, and burned-out delivery '
                                   'teams followed',
                                   'Pick one solution focus for 90 days and measure reach, frequency, and '
                                   'yield',
                                   'Pax8 ([_98wIAhek0M @ 00:07:13])'],
                                  ['Leaving MFA gaps unflagged in customer tenants',
                                   'One demo tenant sat at 33% MFA adoption, while 2021 breach cost hit '
                                   '8,460 pounds',
                                   'Run the gap analysis widget for MFA, inactive users, global admin, and '
                                   'legacy auth',
                                   'Tubblog - The Hub for MSPs ([NVSw5ZYgQzw @ 00:48:09])'],
                                  ['Delaying the Microsoft CSP move for years',
                                   'Highlander put the move off for a long time and stayed a commoditized '
                                   'box-shifter',
                                   'Use distributor pre-planning, pre-sales technical help, and marketing '
                                   'for the Azure push',
                                   'Ingram Micro Cloud UK ([bGmD7XlTNZI @ 00:01:16])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before any offer, price, tool, or VAR order goes live',
                           'body': 'Each gate comes straight from a failure a practitioner hit or watched '
                                   'partners hit. Do not move to the next step until every gate below is '
                                   'cleared.',
                           'items': ['Answer yes to all three questions (where do we create value, where '
                                     'and how do we make money, and do we have the execution muscle to '
                                     'support this) or do not launch the offer [Pax8 — _98wIAhek0M @ '
                                     '00:08:58].',
                                     'Confirm at least 30% margin, not markup, on security, RMM, and '
                                     'non-Microsoft licensing before quoting [Pax8 — KcmWalqZBzk @ '
                                     '00:01:54].',
                                     'Check the integration and run proper comparisons before writing off '
                                     'or switching a tool [usecure — oQIMe7F_kaw @ 00:11:57].',
                                     'Strike every VAR fee except shipping and sales tax, and require '
                                     'itemised taxes on each quote [Staying Connected — 6YNd6Xcyekw @ '
                                     '00:05:38].']}}],
 'pull_quote': "'But I always say firing a client is like your 10th decision. Start with fixing the "
               "client.' — Larry Cobran of MSP CFO, Pax8 (TxvzhnvDnxA @ 00:26:05).",
 'diagram_id': 'diag-03',
 'action_checklist': ['Pick one solution focus for the next 90 days, standardize the message across teams, '
                      'and run the same motion repeatedly [Pax8 — _98wIAhek0M @ 00:25:09].',
                      'Pull the free top and bottom five insights report and compare 3-month delta windows '
                      'to find overserved or underpriced clients [Pax8 — TxvzhnvDnxA @ 00:15:30].',
                      'Connect the PSA to Pax8 with an API user and public/private key in 5 to 10 minutes, '
                      'then bind companies and products one-to-one [Tubblog - The Hub for MSPs — '
                      'NVSw5ZYgQzw @ 00:16:35].',
                      'Launch an opt-out MDR and SOC campaign in which the customer must sign a waiver to '
                      'decline cover [Magic Chats — fM8cQVJ3oh8 @ 00:08:22].',
                      'Build an OEM by country matrix for VAR bidders to complete, and get multiple quotes '
                      'per transaction [Staying Connected — 6YNd6Xcyekw @ 00:07:04].',
                      'Bring IBM opportunities to Ingram, IBM, and AWS reps even at an early stage so they '
                      'can join calls on AWS Marketplace deals [Ingram Micro Canada — ZoUkvQ-5m3c @ '
                      '00:06:11].'],
 'statutory_citations': [{'title': 'Pax8 — From Data to Dollars: Using the Portfolio Approach to Improve '
                                   'Margins in Your MSP | Pax8 [00:26:05]',
                          'url': 'https://www.youtube.com/watch?v=TxvzhnvDnxA&t=1565s',
                          'relevance': 'Primary practitioner testimony on fixing underpriced clients '
                                       'before firing them, and on portfolio margin outliers.'},
                         {'title': 'Tubblog - The Hub for MSPs — Pax8 Demo and Product Tour | MSP Cloud '
                                   'Services Marketplace [00:14:03]',
                          'url': 'https://www.youtube.com/watch?v=NVSw5ZYgQzw&t=843s',
                          'relevance': 'Primary practitioner testimony on reconciling the M365 tenant, '
                                       'Xero, and PSA, and the $130,000 a year recovered for one client.'},
                         {'title': 'Tech Field Day Plus — VARs are Useless – The On-Premise IT Roundtable '
                                   '[00:01:14]',
                          'url': 'https://www.youtube.com/watch?v=oB21xupXerM&t=74s',
                          'relevance': 'Primary practitioner testimony on the direct-versus-VAR debate and '
                                       'on VAR comp pressure.'},
                         {'title': 'Staying Connected — Get the Most Value from Value Added Resellers '
                                   '[00:05:38]',
                          'url': 'https://www.youtube.com/watch?v=6YNd6Xcyekw&t=338s',
                          'relevance': 'Primary practitioner testimony on VAR markup models, hidden fees, '
                                       'and quote transparency.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'phXe8eJoVeo',
                       'title': 'Pax8  - A Cloud Distributor that MSPs Actually Use',
                       'channel': 'Cloud Software Association',
                       'author': 'Cloud Software Association',
                       'text': 'The challenge is quote-to-cash, not just selling.',
                       'tip': 'The challenge is quote-to-cash, not just selling.',
                       'timestamp': 1693,
                       'timestamp_seconds': 1693,
                       'timestamp_label': '[00:28:13]',
                       'url': 'https://www.youtube.com/watch?v=phXe8eJoVeo&t=1693s',
                       'markdown': '[00:28:13](https://www.youtube.com/watch?v=phXe8eJoVeo&t=1693s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KcmWalqZBzk',
                       'title': 'Building a Profitable MSP | Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': "Make sure you're getting at least 30% margin, not markup, on those "
                               'products.',
                       'tip': "Make sure you're getting at least 30% margin, not markup, on those "
                              'products.',
                       'timestamp': 114,
                       'timestamp_seconds': 114,
                       'timestamp_label': '[00:01:54]',
                       'url': 'https://www.youtube.com/watch?v=KcmWalqZBzk&t=114s',
                       'markdown': '[00:01:54](https://www.youtube.com/watch?v=KcmWalqZBzk&t=114s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KcmWalqZBzk',
                       'title': 'Building a Profitable MSP | Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': 'Best-in-class companies are getting at least 60% margin on their managed '
                               'support services.',
                       'tip': 'Best-in-class companies are getting at least 60% margin on their managed '
                              'support services.',
                       'timestamp': 134,
                       'timestamp_seconds': 134,
                       'timestamp_label': '[00:02:14]',
                       'url': 'https://www.youtube.com/watch?v=KcmWalqZBzk&t=134s',
                       'markdown': '[00:02:14](https://www.youtube.com/watch?v=KcmWalqZBzk&t=134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hsCUDuKzpaw',
                       'title': 'Nick Heddy - Getting to know Pax8, a Microsoft Indirect Provider.',
                       'channel': 'Channel Talk',
                       'author': 'Channel Talk',
                       'text': 'Wingman support is 24x7 US-based L2 and L3 support with no finger '
                               'pointing.',
                       'tip': 'Wingman support is 24x7 US-based L2 and L3 support with no finger pointing.',
                       'timestamp': 376,
                       'timestamp_seconds': 376,
                       'timestamp_label': '[00:06:16]',
                       'url': 'https://www.youtube.com/watch?v=hsCUDuKzpaw&t=376s',
                       'markdown': '[00:06:16](https://www.youtube.com/watch?v=hsCUDuKzpaw&t=376s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bGmD7XlTNZI',
                       'title': 'How an IT reseller transformed their business with Ingram Micro Cloud',
                       'channel': 'Ingram Micro Cloud UK',
                       'author': 'Ingram Micro Cloud UK',
                       'text': 'Before Azure we were a commoditized box-shifter, and now customers treat '
                               'us as an advisor.',
                       'tip': 'Before Azure we were a commoditized box-shifter, and now customers treat us '
                              'as an advisor.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=bGmD7XlTNZI&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=bGmD7XlTNZI&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZoUkvQ-5m3c',
                       'title': 'IBM + AWS + Ingram Micro: Your Shortcut to Smarter Reseller Success',
                       'channel': 'Ingram Micro Canada',
                       'author': 'Ingram Micro Canada',
                       'text': "I think it's about 27% quicker.",
                       'tip': "I think it's about 27% quicker.",
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=ZoUkvQ-5m3c&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=ZoUkvQ-5m3c&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ADZwWSQGFFI',
                       'title': 'How Ingram Micro and Cisco help partners grow together',
                       'channel': 'Ingram Micro USA',
                       'author': 'Ingram Micro USA',
                       'text': 'The CARE program reduces churn and raises lifetime value in recurring '
                               'models.',
                       'tip': 'The CARE program reduces churn and raises lifetime value in recurring '
                              'models.',
                       'timestamp': 273,
                       'timestamp_seconds': 273,
                       'timestamp_label': '[00:04:33]',
                       'url': 'https://www.youtube.com/watch?v=ADZwWSQGFFI&t=273s',
                       'markdown': '[00:04:33](https://www.youtube.com/watch?v=ADZwWSQGFFI&t=273s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TxvzhnvDnxA',
                       'title': 'From Data to Dollars: Using the Portfolio Approach to Improve Margins in '
                                'Your MSP | Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': 'The highest efficiency clients churn more often than your average client.',
                       'tip': 'The highest efficiency clients churn more often than your average client.',
                       'timestamp': 666,
                       'timestamp_seconds': 666,
                       'timestamp_label': '[00:11:06]',
                       'url': 'https://www.youtube.com/watch?v=TxvzhnvDnxA&t=666s',
                       'markdown': '[00:11:06](https://www.youtube.com/watch?v=TxvzhnvDnxA&t=666s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TxvzhnvDnxA',
                       'title': 'From Data to Dollars: Using the Portfolio Approach to Improve Margins in '
                                'Your MSP | Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': 'But I always say firing a client is like your 10th decision.',
                       'tip': 'But I always say firing a client is like your 10th decision.',
                       'timestamp': 1565,
                       'timestamp_seconds': 1565,
                       'timestamp_label': '[00:26:05]',
                       'url': 'https://www.youtube.com/watch?v=TxvzhnvDnxA&t=1565s',
                       'markdown': '[00:26:05](https://www.youtube.com/watch?v=TxvzhnvDnxA&t=1565s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'P960HFmyakQ',
                       'title': 'Building the Next-Gen MSP Stack: How Pax8 Is Simplifying MSP Integrations '
                                '| Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': 'The MCP server is a secure bridge for Claude, Copilot and Cursor.',
                       'tip': 'The MCP server is a secure bridge for Claude, Copilot and Cursor.',
                       'timestamp': 495,
                       'timestamp_seconds': 495,
                       'timestamp_label': '[00:08:15]',
                       'url': 'https://www.youtube.com/watch?v=P960HFmyakQ&t=495s',
                       'markdown': '[00:08:15](https://www.youtube.com/watch?v=P960HFmyakQ&t=495s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_98wIAhek0M',
                       'title': 'How MSPs Can Turn Strategy into Real Business Results | Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': "So more often than not, you're not going to scale by doing more things.",
                       'tip': "So more often than not, you're not going to scale by doing more things.",
                       'timestamp': 493,
                       'timestamp_seconds': 493,
                       'timestamp_label': '[00:08:13]',
                       'url': 'https://www.youtube.com/watch?v=_98wIAhek0M&t=493s',
                       'markdown': '[00:08:13](https://www.youtube.com/watch?v=_98wIAhek0M&t=493s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7HqXWzAK1WM',
                       'title': 'Your MSP Questions, Answered: Stack, Security, Coaching & Community | '
                                'Pax8',
                       'channel': 'Pax8',
                       'author': 'Pax8',
                       'text': 'The reality is is that technicians start businesses in the middle of an '
                               'entrepreneurial seizure.',
                       'tip': 'The reality is is that technicians start businesses in the middle of an '
                              'entrepreneurial seizure.',
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=7HqXWzAK1WM&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=7HqXWzAK1WM&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NVSw5ZYgQzw',
                       'title': 'Pax8 Demo and Product Tour | MSP Cloud Services Marketplace',
                       'channel': 'Tubblog - The Hub for MSPs',
                       'author': 'Tubblog - The Hub for MSPs',
                       'text': "So instant provisioning is definitely one of our taglines that you'll "
                               'hear, in real world practice truly, from you know, click to portal dot '
                               "office, we're talking two minutes.",
                       'tip': "So instant provisioning is definitely one of our taglines that you'll hear, "
                              'in real world practice truly, from you know, click to portal dot office, '
                              "we're talking two minutes.",
                       'timestamp': 1430,
                       'timestamp_seconds': 1430,
                       'timestamp_label': '[00:23:50]',
                       'url': 'https://www.youtube.com/watch?v=NVSw5ZYgQzw&t=1430s',
                       'markdown': '[00:23:50](https://www.youtube.com/watch?v=NVSw5ZYgQzw&t=1430s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oQIMe7F_kaw',
                       'title': 'From £2 Add-On to a Service Clients Understand: Lessons From Pax8',
                       'channel': 'usecure',
                       'author': 'usecure',
                       'text': 'I would have a look at the integration before you write something off.',
                       'tip': 'I would have a look at the integration before you write something off.',
                       'timestamp': 717,
                       'timestamp_seconds': 717,
                       'timestamp_label': '[00:11:57]',
                       'url': 'https://www.youtube.com/watch?v=oQIMe7F_kaw&t=717s',
                       'markdown': '[00:11:57](https://www.youtube.com/watch?v=oQIMe7F_kaw&t=717s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fM8cQVJ3oh8',
                       'title': '90%+ Customer Adoption? The Cybersecurity Sales Strategy MSPs Should Know '
                                '| Blackpoint at Pax8 EMEA',
                       'channel': 'Magic Chats',
                       'author': 'Magic Chats',
                       'text': "What's really, really interesting with the opt-out campaign, Magic, is "
                               'that the adoption rate for opting in is over 90%.',
                       'tip': "What's really, really interesting with the opt-out campaign, Magic, is that "
                              'the adoption rate for opting in is over 90%.',
                       'timestamp': 519,
                       'timestamp_seconds': 519,
                       'timestamp_label': '[00:08:39]',
                       'url': 'https://www.youtube.com/watch?v=fM8cQVJ3oh8&t=519s',
                       'markdown': '[00:08:39](https://www.youtube.com/watch?v=fM8cQVJ3oh8&t=519s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6YNd6Xcyekw',
                       'title': 'Get the Most Value from Value Added Resellers',
                       'channel': 'Staying Connected',
                       'author': 'Staying Connected',
                       'text': 'VAR services tend to be good for revenue but it is a low margin business.',
                       'tip': 'VAR services tend to be good for revenue but it is a low margin business.',
                       'timestamp': 185,
                       'timestamp_seconds': 185,
                       'timestamp_label': '[00:03:05]',
                       'url': 'https://www.youtube.com/watch?v=6YNd6Xcyekw&t=185s',
                       'markdown': '[00:03:05](https://www.youtube.com/watch?v=6YNd6Xcyekw&t=185s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oB21xupXerM',
                       'title': 'VARs are Useless – The On-Premise IT Roundtable',
                       'channel': 'Tech Field Day Plus',
                       'author': 'Tech Field Day Plus',
                       'text': 'The value-added is saving my time.',
                       'tip': 'The value-added is saving my time.',
                       'timestamp': 535,
                       'timestamp_seconds': 535,
                       'timestamp_label': '[00:08:55]',
                       'url': 'https://www.youtube.com/watch?v=oB21xupXerM&t=535s',
                       'markdown': '[00:08:55](https://www.youtube.com/watch?v=oB21xupXerM&t=535s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z-ZzUEITMGM',
                       'title': 'Reseller - VAR  Value Added  Reseller Part 1',
                       'channel': 'bobvalueadded',
                       'author': 'bobvalueadded',
                       'text': 'The standard is a 30 to 40% discount.',
                       'tip': 'The standard is a 30 to 40% discount.',
                       'timestamp': 371,
                       'timestamp_seconds': 371,
                       'timestamp_label': '[00:06:11]',
                       'url': 'https://www.youtube.com/watch?v=z-ZzUEITMGM&t=371s',
                       'markdown': '[00:06:11](https://www.youtube.com/watch?v=z-ZzUEITMGM&t=371s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
