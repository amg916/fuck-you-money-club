from __future__ import annotations

def build_volume_037_workbook() -> dict:
    return {'workbook_id': 'wb-037-saas-discount-and-gpo-arbitrage',
 'volume_id': 'vol-037-saas-discount-and-gpo-arbitrage',
 'title': 'SaaS Discount Brokerage & GPO Arbitrage — Practitioner Testimony Operator Workbook',
 'subtitle': 'A field workbook for brokering Microsoft, Adobe, Google Workspace, and UCaaS licenses '
             'through distributor marketplaces, harvesting partner incentives, and protecting margin on '
             'every seat you resell or buy.',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Microsoft Channel Entry and Incentive Harvest Worksheet',
                 'purpose': 'Build a verified Microsoft resale foundation, from Partner Center '
                            'registration through indirect provider selection, NCE term discipline, and '
                            'Microsoft Commerce Incentives enrollment, so a thin 8-15% license margin is '
                            'backed by service revenue and stacked back-end incentives paid as 60% rebate '
                            'and 40% co-op.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete fields in order, because provider choice, incentive '
                                  'eligibility, and CPOR claims all depend on a verified Partner Center '
                                  'account and a linked MPN ID.',
                                  'Pull live numbers from Partner Center, your distributor marketplace, '
                                  'and your earnings reports rather than estimating from memory or old '
                                  'quotes.',
                                  'Record every date that triggers a hard deadline, including NCE 7-day '
                                  'windows, CPOR 12-month start limits, and the April 2026 MFA cutoff for '
                                  'automation.',
                                  'After any enrollment or association change, wait two to three days and '
                                  'then validate the status before treating the item as complete.',
                                  'Book skilling well before quarter end so capability points and '
                                  'designation status refresh in time for the next monthly score update.'],
                 'fields': [{'name': 'partner_center_foundation',
                             'type': 'text',
                             'prompt': 'Record the domain email, primary Entra tenant, and business '
                                       'verification status you used to register Partner Center, then note '
                                       'your AI Cloud Partner Program enrollment date and the MPN ID you '
                                       'will link to an indirect provider for resale.',
                             'example': 'Registered Partner Center under a domain email on our primary '
                                        'Entra tenant, cleared business verification, joined the free AI '
                                        'Cloud Partner Program, and linked our MPN ID to Pax8, since '
                                        'direct bill demands $1,000,000 per year, up from roughly '
                                        '$300,000, and Pax8 APAC expects two-thirds of direct partners to '
                                        'move indirect [Pax8 APAC — Xywyds1IfvM @ 00:04:31].'},
                            {'name': 'provider_model_selection',
                             'type': 'textarea',
                             'prompt': 'Compare CSP Direct, Indirect Provider, and Indirect Reseller for '
                                       'your firm, naming which layer owns first-line support, the '
                                       'indirect provider you chose, and the marketplace, provisioning, '
                                       'and in-house ticket closure evidence that justified the choice '
                                       'over alternatives.',
                             'example': 'Chose Indirect Reseller under Pax8 after scoring marketplace '
                                        'strength, instant provisioning, and tickets closed in-house '
                                        'rather than escalated [Pax8 APAC — Xywyds1IfvM @ 00:09:05]. '
                                        'Support ownership is logged in the customer contract because the '
                                        'indirect reseller is not responsible for support; support falls '
                                        'back to the provider [Spyglass MTG — yNBOfW1MoPs @ 00:00:50].'},
                            {'name': 'license_margin_math',
                             'type': 'textarea',
                             'prompt': 'Show the per-seat margin math for one core Microsoft license, '
                                       'including MSRP, your cost, the resulting percentage, and the '
                                       'managed service you will bundle around it so the account earns on '
                                       'the service layer rather than the software alone.',
                             'example': 'Seat cost $18 against $20 MSRP, inside the 8-15% license margin '
                                        'band, so we wrap onboarding, security baselining and helpdesk '
                                        'into one per-user fee, because the partner earns the margin on '
                                        'the service layer, not the software [m365 Show | M365, Azure '
                                        'Cloud, Power Platform & AI — LGgw20GtaDQ @ 00:04:18].'},
                            {'name': 'nce_term_and_window',
                             'type': 'textarea',
                             'prompt': 'List each NCE subscription with chosen term (monthly, annual paid '
                                       'monthly, annual, or triennial), the resulting premium or saving, '
                                       'the order date, and the exact date its 7-day adjustment window '
                                       'closes, plus who signs off on seat counts.',
                             'example': 'Twenty seats moved from monthly to annual because monthly terms '
                                        'carry a 20% premium, a $100 seat becoming $120, while annual paid '
                                        'monthly adds only 5% and triennial saves 12-18% [m365 Show | '
                                        'M365, Azure Cloud, Power Platform & AI — LGgw20GtaDQ @ 00:04:45]. '
                                        'The operations lead signed off seat counts on day two.'},
                            {'name': 'incentive_stack',
                             'type': 'textarea',
                             'prompt': 'Map your target incentive stack for M365, Azure, and Dynamics, '
                                       'listing core, Tier 1, Tier 2, PSTN, and customer-add rates you '
                                       'expect to qualify for, and confirm Microsoft Commerce Incentives '
                                       'enrollment is separate from your benefits package or designation.',
                             'example': 'M365 stack: core 3.75%, Tier 1 5%, Tier 2 7%, PSTN 20% and '
                                        'customer-add 15% for 12 months, up to 25.75%; Azure to 26%, '
                                        'Dynamics to 34.75% [Inside Microsoft AI Cloud Partner Program — '
                                        'jz1cE7UYBO4 @ 00:15:48]. MCI enrollment filed separately because '
                                        'a benefits package or designation alone starts nothing.'},
                            {'name': 'mci_eligibility_check',
                             'type': 'textarea',
                             'prompt': 'Document MCI eligibility per location ID: trailing 12-month '
                                       'revenue against the $25K floor, the designation, specialization, '
                                       'or capability points you hold, enrollment status color, Incentives '
                                       'Admin role holder, and every payout profile created for co-op, '
                                       'fee, indirect, and rebate.',
                             'example': 'Location ID clears the $25K trailing 12-month floor and holds 25 '
                                        'capability points, with scores refreshing only monthly [Pax8 — '
                                        'tsL0gg_Jy9U @ 00:11:07]. Status is green in every enrollment row, '
                                        'Incentives Admin assigned, payout profiles built for co-op, fee, '
                                        'indirect and rebate before forecasting cash [Inside Microsoft AI '
                                        'Cloud Partner Program — jcYTmMdEGPo @ 00:21:04].'},
                            {'name': 'fy27_incentive_shift',
                             'type': 'textarea',
                             'prompt': 'Explain how the FY27 removal of core incentives for Modern Work '
                                       'and Business Apps changes your plan, naming which Tier 2 strategic '
                                       'SKUs, growth accelerator targets, and tiered Azure growth bands '
                                       'you will now chase instead, and why.',
                             'example': 'Core incentive no longer carries the plan, so we push Tier 2 '
                                        'strategic SKUs at 7% and target the CSP growth accelerator, which '
                                        'rises to 12.5% from 7.5% [Pax8 — 1RKZdigqOf4 @ 00:12:20]. '
                                        'Forecasts avoid double counting because growth margin already '
                                        'includes base margin and is not stacked on top [Pax8 — '
                                        'tsL0gg_Jy9U @ 00:07:16].'},
                            {'name': 'cpor_claims',
                             'type': 'textarea',
                             'prompt': 'List each Claiming Partner of Record association you will submit, '
                                       'with customer domain match, workload start date within 12 months, '
                                       'original two-to-three sentence workload description, and the '
                                       'Modern Work deployment points you expect versus the CSP '
                                       'equivalent.',
                             'example': 'Domain matched, start date inside 12 months, description written '
                                        'originally, never copied, then pasted from a draft because '
                                        'comments do not autosave [Inside Microsoft AI Cloud Partner '
                                        'Program — uHFljjNXztI @ 00:26:54]. Expected 5 deployment points '
                                        'versus 2.5 for CSP, with usage growth at 0.06 versus 0.015 '
                                        '[Inside Microsoft AI Cloud Partner Program — uHFljjNXztI @ '
                                        '00:04:19].'},
                            {'name': 'copilot_trial_conversion',
                             'type': 'text',
                             'prompt': 'Describe how you configure Copilot trials at checkout so trial '
                                       'seats roll into paid subscriptions, including seat count, '
                                       'conversion setting, the follow-up date, and the governance '
                                       'controls each deployed agent needs before going live with the '
                                       'customer.',
                             'example': 'Copilot in 30 trial set to convert to subscription after trial at '
                                        'checkout, so all 25 seats roll straight into paid seats [Pax8 — '
                                        '1RKZdigqOf4 @ 00:37:13]. Each agent gets a named owner, '
                                        'least-privilege access, a registry entry and a credit limit, '
                                        'because an agent nobody owns is a liability with a login '
                                        '[Microsoft Events — z4JbWkKJagI @ 00:30:34].'},
                            {'name': 'support_and_operations_hygiene',
                             'type': 'textarea',
                             'prompt': 'Record your escalation and hygiene routines: what you send '
                                       'Microsoft on API failures, how you pull portal diagnostics, how '
                                       'long you wait before filing billing disputes, MFA readiness for '
                                       'automation, and the order of steps before removing a customer.',
                             'example': 'API tickets carry request and response logs plus the '
                                        'MS-CorrelationID, with a SPOCK file pulled by Ctrl+Alt+D for '
                                        'portal faults [Microsoft Helps — 9Q30FhN41LI @ 00:35:20]. Billing '
                                        'gaps get a 24-hour recheck before filing [m365 Show | M365, Azure '
                                        'Cloud, Power Platform & AI — uiVjifpxK38 @ 00:13:33]. Customer '
                                        'removal starts by suspending subscriptions and cancelling '
                                        'reservations.'}],
                 'completion_gate': 'Do not forecast incentive cash or quote a Microsoft deal until MCI '
                                    'enrollment is green, the Incentives Admin role is assigned, payout '
                                    'profiles exist for co-op, fee, indirect and rebate, NCE seat counts '
                                    'are locked inside the 7-day window, and every API automation is '
                                    'MFA-ready ahead of the April 2026 cutoff.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Marketplace Margin Engine and Adobe VIP Marketplace Migration Worksheet',
                 'purpose': 'Turn distributor marketplace purchasing into a margin engine by testing offer '
                            'viability, enforcing margin floors, reconciling tenant, billing and PSA data, '
                            'and moving Adobe customers from classic VIP to VIP Marketplace without '
                            'duplicate consoles or wrong-quantity renewals.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Score each offer against the three launch questions before touching '
                                  'pricing, and treat a single no answer as a stop.',
                                  'Calculate margin on sell price, never markup on cost, and flag any line '
                                  'that falls below the 30% or 60% floors.',
                                  'Reconcile tenant, billing engine, and PSA counts monthly and log every '
                                  'recovered dollar against the client it came from.',
                                  'Check every Adobe anniversary date before scheduling a transfer, and '
                                  'keep customers inside the 30-day renewal window on the old VIP route.',
                                  'Lock Adobe downsizes and auto-renewal changes at least two days before '
                                  'the anniversary and record the locking date in the field.'],
                 'fields': [{'name': 'offer_viability_three_questions',
                             'type': 'textarea',
                             'prompt': 'Answer the three launch questions for your next marketplace offer: '
                                       'where you create value, where and how you make money, and whether '
                                       'you have the execution muscle to support it, giving a plain yes or '
                                       'no with evidence for each.',
                             'example': 'Managed security bundle: value is created in onboarding and '
                                        'monitoring, money is made on the wrapped service rather than the '
                                        'licence, and execution muscle exists through a staffed helpdesk. '
                                        'All three answered yes, so the offer launches [Pax8 — _98wIAhek0M '
                                        '@ 00:08:58]. Benchmark: $4.14 of services per $1 of Microsoft '
                                        'cloud [Cloud Software Association — phXe8eJoVeo @ 00:13:15].'},
                            {'name': 'margin_floor_check',
                             'type': 'textarea',
                             'prompt': 'For every product line you resell, record cost, sell price, and '
                                       'true margin rather than markup, then flag any security, RMM, or '
                                       'non-Microsoft licensing line below the floor and any managed '
                                       'support service below the best-in-class threshold.',
                             'example': 'RMM line repriced because markup looked healthy but margin sat '
                                        'under the floor; the rule is at least 30% margin, not markup, on '
                                        'security, RMM and non-Microsoft licensing [Pax8 — KcmWalqZBzk @ '
                                        '00:01:54]. Managed support is held to the best-in-class marker of '
                                        'at least 60% margin on managed support services [Pax8 — '
                                        'KcmWalqZBzk @ 00:02:14].'},
                            {'name': 'tenant_billing_psa_reconciliation',
                             'type': 'textarea',
                             'prompt': 'Reconcile license counts across the M365 tenant, your billing '
                                       'engine, and your PSA for each client, listing every mismatch '
                                       'found, its monthly value, the system of record you corrected, and '
                                       'the date the next invoice confirmed the fix.',
                             'example': 'Monthly three-way check compares tenant seats, the Xero billing '
                                        'engine and PSA agreements, the same gap-closing routine that '
                                        'recovered $130,000 a year for one US client [Tubblog - The Hub '
                                        'for MSPs — NVSw5ZYgQzw @ 00:14:03]. The framing for leadership: '
                                        'the challenge is quote-to-cash, not just selling [Cloud Software '
                                        'Association — phXe8eJoVeo @ 00:28:13].'},
                            {'name': 'client_delta_analysis',
                             'type': 'textarea',
                             'prompt': 'Run a per-client delta analysis comparing revenue per endpoint '
                                       'against logged service cost, noting hours logging rules, ticket '
                                       'volume outliers, and whether the fix for each unprofitable client '
                                       'is training, process change, or a price increase.',
                             'example': 'Agreement-covered work is never marked non-billable and 100% of '
                                        'hours are logged against at least an eight-hour day [Pax8 — '
                                        'TxvzhnvDnxA @ 00:17:30]. A law-firm client showed normal revenue '
                                        'per endpoint but high ticket counts, so lunch-and-learns replaced '
                                        'a price increase [Pax8 — TxvzhnvDnxA @ 00:25:05], remembering '
                                        'that the highest efficiency clients churn more often than '
                                        'average.'},
                            {'name': 'security_attach_campaign',
                             'type': 'textarea',
                             'prompt': 'Design your security attach campaign: which MDR or SOC bundle is '
                                       'included by default, how the opt-out waiver works, the target '
                                       'adoption rate, and how you will track declines against renewal '
                                       'conversations and upsell recommendations for every managed client.',
                             'example': 'MDR and SOC coverage ships inside every managed bundle and '
                                        'customers must sign a waiver to decline, the opt-out structure '
                                        'that produced over 90% adoption [Magic Chats — fM8cQVJ3oh8 @ '
                                        '00:08:39]. A read-only MCP query, using a token from Settings '
                                        'then Integrations, lists renewals in the next 30 days for '
                                        'Defender upsells [Pax8 — P960HFmyakQ @ 00:10:42].'},
                            {'name': 'var_fee_transparency',
                             'type': 'textarea',
                             'prompt': 'When buying through a value-added reseller, list every fee line on '
                                       'the quote, mark which survive the rule that strikes everything '
                                       'except shipping and sales tax, confirm taxes are itemised, and '
                                       'record what time-saving brokerage value justifies any remaining '
                                       'reseller margin.',
                             'example': 'Quote reduced to licence, shipping and sales tax after striking '
                                        'every other VAR fee and requiring itemised taxes on each quote '
                                        '[Staying Connected — 6YNd6Xcyekw @ 00:05:38]. Remaining margin is '
                                        'accepted only where the reseller acts as an advisor, the shift '
                                        'one partner described as moving beyond being a commoditized '
                                        'box-shifter [Ingram Micro Cloud UK — bGmD7XlTNZI @ 00:02:02].'},
                            {'name': 'vipmp_transfer_plan',
                             'type': 'textarea',
                             'prompt': 'For each Adobe customer still on classic VIP, record the agreement '
                                       'number, anniversary date, whether it falls inside the 30-day '
                                       'renewal window, who enters the transfer, and confirmation that no '
                                       'new order was placed before the inbound transfer ran.',
                             'example': 'Design agency on classic VIP sits 12 days from its anniversary, '
                                        'so it renews on the old route and migration is parked until the '
                                        'window closes [TD SYNNEX Spain — 824bcq4wI-Q @ 00:21:40]. New '
                                        'orders stay blocked, since a fresh order would generate another '
                                        'console and another VIP plan instead of migrating it [TD SYNNEX '
                                        'Spain — 824bcq4wI-Q @ 00:18:14].'},
                            {'name': 'admin_and_volume_level',
                             'type': 'text',
                             'prompt': 'Record the single VIP Marketplace owner email for each account, '
                                       'confirm it sits on a corporate domain rather than a blacklisted '
                                       "private provider, and note the price level the customer's seat "
                                       'count places them in on the volume ladder.',
                             'example': 'Owner email rejected at onboarding because it ended in Gmail; '
                                        'only one admin email is allowed and private domains sit on '
                                        "Adobe's blacklist [AppXite — GDHnAQ3r53A @ 00:05:08]. With 14 "
                                        'seats the customer lands at the 10-49 level, above Level 1 up to '
                                        '9 units, with Levels 3 and 4 currently priced alike [TD SYNNEX '
                                        'Spain — 824bcq4wI-Q @ 00:09:09].'},
                            {'name': 'renewal_change_lock',
                             'type': 'textarea',
                             'prompt': 'List every downsize, increase, and auto-renewal change for '
                                       'upcoming Adobe anniversaries, with the date each change is locked '
                                       'and who approved it, the buffer kept against time-zone drift, and '
                                       'how you handle the 14-day return window for new licences.',
                             'example': 'Downsize from 10 to 6 seats locked three days before the '
                                        'anniversary, beating the two-day rule so time-zone drift cannot '
                                        'renew the wrong quantity [SoftwareOne Platform — sNCywL0bfVI @ '
                                        '00:01:11]. New licences are confirmed with users inside 14 days, '
                                        'because after the 15th day a VIPMP licence cannot be returned [TD '
                                        'SYNNEX Spain — 824bcq4wI-Q @ 00:17:35].'},
                            {'name': 'auto_renewal_bulk_and_escalation',
                             'type': 'textarea',
                             'prompt': 'Identify set-and-forget Adobe accounts for auto-renewal, the bulk '
                                       'configuration order you will use per agreement, scheduled renewal '
                                       'increases staged in advance with their effective dates, and the '
                                       'designated technical relationship manager who alone may escalate '
                                       'issues to Adobe technical support.',
                             'example': 'A customer renewing the same seats since 2016 and every '
                                        'single-unit customer move to auto-renewal [TD SYNNEX Spain — '
                                        '824bcq4wI-Q @ 00:23:03], flipped in one configuration order '
                                        'because they share an agreement [SoftwareOne Platform — '
                                        'nnAd6F22fiw @ 00:00:18]. A staged jump from 2 to 10 licences was '
                                        'overwritten in the history tab to five extra [AppXite — '
                                        'GDHnAQ3r53A @ 00:10:18].'}],
                 'completion_gate': 'The worksheet is complete when every offer has three documented yes '
                                    'answers, every resold line clears its margin floor, reconciliation '
                                    'gaps are closed and confirmed by the next invoice, and every classic '
                                    'VIP customer has a transfer date, a corporate-domain owner email, and '
                                    'renewal quantities locked at least two days before the anniversary.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Adobe and Workspace Discount Arbitrage and UCaaS Brokerage Worksheet',
                 'purpose': 'Treat list price as a negotiable anchor across Adobe, Google Workspace, Zoom, '
                            'and RingCentral by matching plans to real usage, pricing exit costs, '
                            'verifying seat legitimacy, and brokering UCaaS and contact center deals where '
                            'the provider, not the customer, pays the representation fee.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Start with the buyer type, since consumer, small business, student, and '
                                  'enterprise buyers face different Adobe discounts and renewal uplifts.',
                                  'Price exit costs and cancellation-screen offers before recommending any '
                                  'Adobe plan change or renewal.',
                                  'Get Google to confirm the license type behind any cheap Workspace seats '
                                  'before buying or reselling them.',
                                  'Use the four-line switch test on every platform migration and show the '
                                  'year-one difference even when it is unfavorable.',
                                  'For UCaaS deals, confirm the CRM integration path, exit terms, and real '
                                  'support tier before presenting street pricing.'],
                 'fields': [{'name': 'adobe_plan_fit',
                             'type': 'textarea',
                             'prompt': 'For each Adobe seat or client, record the current plan and monthly '
                                       'price, actual feature use, the cheaper plan or single app that '
                                       'would cover it, and whether a free alternative closes the gap for '
                                       "that user's workload entirely.",
                             'example': 'Illustrator-only freelancer moved off Creative Cloud Pro, which '
                                        'runs $69.99 a month after the intro deal, about $840 a year [Tech '
                                        'Meets East — xCgcup4z6CI @ 00:02:28]. Users who skip heavy AI '
                                        'features drop to Creative Cloud Standard at $54.99 a month, '
                                        'noting that increases were deferred, not cancelled [Tech Meets '
                                        'East — IIVbCmH7kHA @ 00:24:24].'},
                            {'name': 'adobe_exit_cost',
                             'type': 'textarea',
                             'prompt': 'Price the exit on every Adobe annual-paid-monthly plan before '
                                       'signing or renewing: remaining payments, the early cancellation '
                                       'share owed, where the fee is disclosed, and whether any retention '
                                       'offer at the cancellation screen restarts a new commitment.',
                             'example': 'Eight payments remain, and half of every remaining payment is '
                                        'owed on early cancellation, a fee reportedly buried in fine print '
                                        'or behind hover icons [Tech Meets East — ZnXsR4iADwM @ 00:02:30]. '
                                        'Free months at the cancellation screen were declined because '
                                        'accepting can start a brand new one-year commitment [Tech Meets '
                                        'East — ZnXsR4iADwM @ 00:07:28].'},
                            {'name': 'adobe_discount_stack',
                             'type': 'textarea',
                             'prompt': 'List every Adobe discount route you can legitimately apply for '
                                       'each buyer type, such as introductory, regional, student, or '
                                       'annual prepaid pricing, with verification method, expiry, and the '
                                       'enterprise renewal uplift you expect where discounts do not apply.',
                             'example': 'Student buyers verify through school email at the account step, '
                                        'skipping manual document checks [Daniel Studios — 4XzZib-kFMg @ '
                                        '00:03:09], with Black Friday peaking at 77% off the first year '
                                        '[Daniel Studios — lyQ4gisVObM @ 00:00:12]. Enterprise renewals '
                                        'are budgeted for 8 to 12% increases on multi-year agreements '
                                        '[Tech Meets East — ZnXsR4iADwM @ 00:17:28].'},
                            {'name': 'workspace_reseller_terms',
                             'type': 'textarea',
                             'prompt': 'Document your Google Workspace reseller arrangement: wholesale '
                                       'versus retail pricing, off-book discounts available above your '
                                       'seat thresholds, split-billing eligibility for mixing premium and '
                                       'light licenses, and the professional email address used for '
                                       'partner enrollment and its approval date.',
                             'example': 'Our 24-user client now qualifies for split licensing, mixing '
                                        'premium and light seats, because the floor dropped to 20 users '
                                        'from more than 100 [itGenius 🤓 Biz Tech Experts — aAQpTV4Ybnk @ '
                                        '00:02:25]. Partner enrollment used a domain address, since it '
                                        'cannot be a standard personal address ending in gmail.com [HowTo '
                                        'With Glen — o7bsmkpf6kA @ 00:01:04].'},
                            {'name': 'workspace_seat_legitimacy',
                             'type': 'textarea',
                             'prompt': 'Before buying or reselling any discounted Workspace seats, record '
                                       'the seat price, the license type Google confirms for the domain, '
                                       'whether it rides a nonprofit, education, legacy, or official '
                                       'partner panel, and the callback reference from Google support.',
                             'example': 'A vendor offered seats under $2, the price typical of nonprofit '
                                        'panels procured at as low as $0 and holding 500-plus seats '
                                        "[InboxKit — 0Vk8NzIt_RM @ 00:00:29]. We filed Google's form under "
                                        'the suspended administrator option, requested a phone callback, '
                                        'and asked which license type the domain runs on before any '
                                        'purchase [InboxKit — 0Vk8NzIt_RM @ 00:01:51].'},
                            {'name': 'switch_decision_four_lines',
                             'type': 'textarea',
                             'prompt': 'Before recommending any platform switch, fill the four decision '
                                       'lines: current bill, replacement cost including anything retained, '
                                       'one-time transition cost, and the first date old commitments can '
                                       'end, then state the year-one net difference for the client '
                                       'honestly.',
                             'example': 'M365-to-Workspace move scored on four lines: current bill, '
                                        'replacement including retained licences, one-time transition '
                                        'cost, and first exit date for old commitments [Rook Technology '
                                        'Consulting — -uYS0eABgbk @ 00:02:10]. The cheaper-looking switch '
                                        'can still cost $2,800 more in year one, so the client stays put '
                                        'until old commitments can end.'},
                            {'name': 'ucaas_broker_pricing',
                             'type': 'textarea',
                             'prompt': 'For each UCaaS deal, record list price per user, the brokered '
                                       'street price you negotiated, idle DID and toll-free minute rates, '
                                       'and confirmation that the provider rather than the customer pays '
                                       'your representation fee on the account.',
                             'example': 'Zoom Phone Unlimited brokered below $10 per user, sometimes $8 to '
                                        '$9, against a $15 list [AeroCom Inc — viRtp8k9GAo @ 00:03:12]. '
                                        'Idle DIDs pushed from the $5 list toward $1 and high-volume '
                                        'toll-free from 3.7 cents to 1.5 to 2 cents per inbound minute '
                                        '[AeroCom Inc — viRtp8k9GAo @ 00:08:22], with the provider paying '
                                        'our fee.'},
                            {'name': 'spiff_and_channel_programs',
                             'type': 'textarea',
                             'prompt': 'List the vendor incentives active on your pipeline, including '
                                       'SPIFF multiples, residual changes, and end dates, plus which '
                                       'stalled deals you will pivot into those products and how Channel '
                                       'Harmony or similar conflict rules affect who owns each '
                                       'opportunity.',
                             'example': 'A UC deal stuck on complex analytics requirements pivots to '
                                        'RingCX, where RingCentral is paying a 15x SPIFF plus increased '
                                        'residuals through year-end [Telarus — 8ge4I4KL5kQ @ 00:10:59]. '
                                        'Zoom pipeline is tracked as its own practice, since the channel '
                                        'TAM is sized at $200 billion plus by decade end [UC Today News — '
                                        'dqTXnYdAKdQ @ 00:10:09].'},
                            {'name': 'contact_center_upsell',
                             'type': 'textarea',
                             'prompt': 'Decide whether each queue-heavy customer needs a full contact '
                                       'center license or a lighter add-on, recording supervisor and agent '
                                       'counts, the analytics they actually require, per-seat pricing for '
                                       'each option, and the integration proof demanded from bundled '
                                       'vendors.',
                             'example': 'A support team needing queue times and real-time analytics gets '
                                        'the Customer Engagement Pack at $20 per supervisor per month '
                                        'instead of $100-plus per agent [AeroCom Inc — auYElw4sYi8 @ '
                                        '00:13:34]. On a NICE plus RingCentral bid we demanded proof of '
                                        'integrated workflows, consistent administration, data sharing and '
                                        'implementation ownership [CX without the BS — DKzL7oMyWis @ '
                                        '00:06:51].'},
                            {'name': 'ucaas_contract_risk',
                             'type': 'text',
                             'prompt': 'Record the contract risks for each UCaaS recommendation: '
                                       'early-exit terms against expected headcount volatility, the '
                                       'support tier the customer will actually receive and its cost, and '
                                       'the CRM integration path confirmed before pricing was presented to '
                                       'the decision maker.',
                             'example': 'Seasonal headcount flagged because Zoom rarely releases customers '
                                        'early and is not month-to-month [AeroCom Inc — auYElw4sYi8 @ '
                                        '00:24:32]. Support tier checked, since chat needs over $10 a '
                                        'month and phone over $200 [LONDON FILM — ZHjObNVm5_Y @ 00:02:11]. '
                                        'A deal lost on CRM gaps reopens with a free 14-day, five-user '
                                        'trial [WeAreVoxFlo — Zbk_QOoXQ_M @ 00:02:08].'}],
                 'completion_gate': 'Do not present a recommendation until each Adobe client has a '
                                    'plan-fit and exit-cost entry, every discounted Workspace seat has a '
                                    'Google-confirmed license type, every switch has all four decision '
                                    'lines filled, and every UCaaS proposal shows street versus list '
                                    'pricing, the fee source, exit terms, the real support tier, and a '
                                    'confirmed CRM integration path.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'GPO Leverage and Contingency Audit Ledger',
                 'purpose': 'Capture how pooled buying power, supplier-paid admin fees, commitment '
                            'compliance, and contingency telecom audits turn into verified savings, so '
                            'every GPO contract and expense recovery is documented, tracked to the '
                            'invoice, and defensible before it goes live.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Pull 12 months of general ledger data for every category you plan to '
                                  'route through a GPO or a contingency auditor before filling any field.',
                                  'Confirm how each GPO and audit partner is paid, whether admin fee, '
                                  'participation fee, shared savings, retainer, or hourly, before '
                                  'comparing savings claims.',
                                  'Record compliance targets and carve-outs inside the contract itself, '
                                  'never in side emails or verbal agreements with account executives.',
                                  'Treat every disconnect, rate change, and refund as open until the next '
                                  'invoice confirms it billed correctly.',
                                  'Cite the practitioner source for each benchmark you rely on so '
                                  'reviewers can trace every savings assumption back to its origin.'],
                 'fields': [{'name': 'gpo_fee_model',
                             'type': 'text',
                             'prompt': 'Record exactly how your chosen GPO gets paid: vendor '
                                       'administrative fees, member participation fees, or both, and '
                                       'whether each fee is a percentage or an annual flat rate. Note who '
                                       'ultimately funds the savings you are being promised and why.',
                             'example': 'Our food-service GPO is Una, which runs free membership with no '
                                        'commitments or exclusivities and funds itself from a small slice '
                                        'of the supplier admin fee [Una — wRrnU1fw7P0 @ 00:00:47]. Fee '
                                        'model logged as vendor-paid percentage only, no member '
                                        'participation charge, confirmed against the fee-structure '
                                        'checklist [Educationleaves — Nx4UI5uowcw @ 00:01:25].'},
                            {'name': 'admin_fee_exposure',
                             'type': 'textarea',
                             'prompt': 'Estimate the supplier-paid administrative fee flowing to the GPO '
                                       'on your category spend, using the 1.5 to 3 percent of sales range. '
                                       'Then decide whether that fee stream makes the middleman the real '
                                       'winner on any contract you are evaluating.',
                             'example': 'On $2,000,000 of annual med-device purchases, the manufacturer '
                                        'admin fee runs $30,000 to $60,000, which Eric Bricker likens to a '
                                        'commission [AHealthcareZ - Healthcare Finance Explained — '
                                        'N0B0bUjLrUE @ 00:01:24]. Flagged against PBM-affiliated GPOs '
                                        'pocketing $7.6 billion in 2022 fees [PBM Insider — uyVsmq0w3FM @ '
                                        '00:01:24]; decision: request fee disclosure before signing.'},
                            {'name': 'commitment_compliance_plan',
                             'type': 'textarea',
                             'prompt': 'Choose between a binding letter of commitment and a flexible '
                                       'letter of participation for each category. State the committed '
                                       'compliance level, 70, 80, or 90 percent, and describe the Power BI '
                                       'or Tableau tracker that will monitor it against rebate thresholds.',
                             'example': 'Surgical gloves signed on a letter of commitment at 80 percent; '
                                        'we will run the category at 81 percent rather than hover near 78 '
                                        'or 79 without a carve-out [Healthcare Supply Chain Hub: Angelique '
                                        'W. Beslic — K2Slgt-y1wo @ 00:21:44]. A Power BI tracker checks '
                                        'compliance and rebate status before go-live [Healthcare Supply '
                                        'Chain Hub: Angelique W. Beslic — K2Slgt-y1wo @ 00:26:28].'},
                            {'name': 'carve_out_justification',
                             'type': 'textarea',
                             'prompt': 'List every product excluded from a committed contract and attach '
                                       'the written clinical justification that supports it. Explain where '
                                       'the justification lives inside the contract and how the 10 to 20 '
                                       'percent uncommitted sandbox will be used for innovation.',
                             'example': 'Carve-out: one specialty catheter line, documented by our '
                                        'clinical committee in an enhanced addendum to the GPO contract '
                                        '[Healthcare Supply Chain Hub: Angelique W. Beslic — K2Slgt-y1wo @ '
                                        '00:23:09]. The remaining 10 to 20 percent wiggle room above 80 to '
                                        '90 percent compliance is reserved as a sandbox for trialing new '
                                        'suppliers [Healthcare Supply Chain Hub: Angelique W. Beslic — '
                                        'K2Slgt-y1wo @ 00:03:39].'},
                            {'name': 'tail_spend_handoff',
                             'type': 'textarea',
                             'prompt': 'Separate tail spend and non-strategic categories you will hand to '
                                       'the GPO from strategic spend you will negotiate yourself. Name the '
                                       'search tool or team you will use to connect contracts and '
                                       'suppliers you are not yet linked to.',
                             'example': 'Handed to the GPO: janitorial supplies, office consumables and '
                                        'break-room food, the small categories that quietly add up, while '
                                        'our team keeps strategic spend the GPO typically cannot help with '
                                        '[Una — pKhFVbBzkz4 @ 00:02:32]. Ran the Opus search, found two '
                                        'unconnected cooperative contracts, and pinged the OMNIA team to '
                                        'connect them [OMNIA Partners — fdEV8yBr5eM @ 00:02:47].'},
                            {'name': 'day_one_expectations',
                             'type': 'text',
                             'prompt': 'Write the expectations you will put on the table at the first '
                                       'onboarding call: volume, locations, SKUs, and terms. Include the '
                                       'savings range you expect to see and how member-specific numbers '
                                       'will be confirmed during onboarding.',
                             'example': 'Day-one sheet lists 12 locations, 340 SKUs, weekly delivery '
                                        'volume and net-30 terms, because unmet or undiscussed '
                                        'expectations cause the most frustration [Una — N9511Ln5CfE @ '
                                        '00:07:27]. Target food savings set at 18 to 22 percent with '
                                        'long-term price protection, member-specific numbers to be '
                                        'confirmed on the onboarding call [Una — vXeviFgIR1I @ 00:00:24].'},
                            {'name': 'contingency_fee_terms',
                             'type': 'textarea',
                             'prompt': 'Define the contingency or shared-savings agreement with your '
                                       'cost-reduction partner: fee model, upfront cost, whether incumbent '
                                       'vendors stay in place, and how many vendors are attacked first. '
                                       'Compare the expected reduction against running the audit '
                                       'internally.',
                             'example': 'Engagement is pure shared savings with nothing to start, so no '
                                        'budget line is needed [Expense Consulting — o2wyRpIYL0w @ '
                                        '00:01:34]. Scope opens on three to five vendors rather than all '
                                        '100 [ExpenseSavvy — 2RDXap2GiBE @ 00:03:32]. Outsourcing chosen '
                                        'because typical reductions run 15 to 40 percent versus 3 to 5 '
                                        'percent internally [singlesourcetelecom — GcLqzAGpP2s @ '
                                        '00:02:19].'},
                            {'name': 'telecom_go_behind_audit',
                             'type': 'textarea',
                             'prompt': 'Identify accounts previously audited by other firms and schedule a '
                                       'go-behind audit focused on data accounts. Also list over-collected '
                                       'sales tax claims, back-billing refunds, and forward savings you '
                                       'will pursue on auto-paid invoices nobody reads.',
                             'example': 'Data accounts already audited twice go to a go-behind audit, the '
                                        'same move that pulled a $165,000 credit on one account [Auditel, '
                                        'Inc. Telecom Expense Management — YAHf-FXxBCM @ 00:01:19]. Vendor '
                                        'sales tax is checked for over-collection and refunded to us '
                                        '[kconole2011 — meAxKn8Td5k @ 00:01:52], keeping incumbent vendors '
                                        'in place while the price drops.'},
                            {'name': 'disconnect_order_tracking',
                             'type': 'textarea',
                             'prompt': 'Log every disconnect and rate-change order placed with a carrier, '
                                       'including closed sites and leftover equipment. Record the invoice '
                                       'that confirms each change, because providers place orders '
                                       'incorrectly or not at all while the account keeps billing.',
                             'example': 'Closed satellite office: switch shutdown emailed to the carrier, '
                                        'but it was never shut off, the pattern brightfin cleaned up for '
                                        'roughly $56,000 [brightfin — lxObl7Zpr2A @ 00:03:06]. A '
                                        'still-activated modem was found charging after devices were '
                                        'ported [Ancy Alphonse — RV9K4EXWxJs @ 00:04:19]. Each disconnect '
                                        'stays open until the next invoice confirms it [Auditel, Inc. '
                                        'Telecom Expense Management — F00NVfaC6Tk @ 00:01:33].'},
                            {'name': 'ucaas_license_reclaim',
                             'type': 'textarea',
                             'prompt': 'Map every Zoom, Teams, and similar collaboration license to HR '
                                       'master data so departed employees are flagged at off-boarding. '
                                       'Identify license stacking across overlapping products and decide '
                                       'where deliberate redundancy is justified for staff running '
                                       'customer demos.',
                             'example': "HR master data now feeds the license register, so leavers' active "
                                        'seats are flagged and reclaimed at off-boarding [UC Today News — '
                                        'bQwapQbcKSk @ 00:14:25]. Heavy users holding two or three similar '
                                        'meeting products get trimmed to one, except sales staff, who keep '
                                        'a backup tool for customer demos by written policy [UC Today News '
                                        '— bQwapQbcKSk @ 00:12:20].'}],
                 'completion_gate': 'Do not sign a GPO commitment or contingency engagement until the fee '
                                    'model is confirmed, a Power BI or Tableau compliance tracker is live, '
                                    'every carve-out has written clinical justification, and each '
                                    'disconnect order shows on a corrected invoice.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'SaaS Estate Audit and Renewal Defense Planner',
                 'purpose': 'Build the money-first, identity-second view of the SaaS estate, rightsize '
                            'idle and shadow licenses, and enter every renewal with usage data, a '
                            'calendared notice deadline, and contract language that caps increases and '
                            'protects downscaling rights.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Start with spend data from ERP, invoices, and expense reports, then '
                                  'layer identity data from SSO, Entra ID, Okta, and the HRIS.',
                                  'Work renewals backward from the notice deadline, opening each '
                                  'negotiation 60 to 90 days before the renewal date at minimum.',
                                  'Keep your own monthly assignment records for Adobe and Microsoft so '
                                  'vendor assessments can be challenged with evidence.',
                                  'Get every concession, price lock, and seat-flexibility promise in '
                                  'writing; verbal assurances from account managers do not count.',
                                  'Transfer owned documents and workspaces before reclaiming any seat, and '
                                  'log each reclaimed license into a shared pool.'],
                 'fields': [{'name': 'spend_baseline',
                             'type': 'textarea',
                             'prompt': 'Assemble twelve months of ERP, invoice, and expense data to build '
                                       'the money-first SaaS baseline. Record the vendor count leadership '
                                       'estimated before the audit and the count the audit actually found, '
                                       'then note the multiple between them.',
                             'example': 'Leadership guessed 55 vendors; the 12-month ERP, invoice and '
                                        'Concur pull found 160, inside the two-to-four-times underestimate '
                                        'band [SaaS Procurement Insider — udHdwtjP7yM @ 00:00:00]. The '
                                        'transaction CSV was uploaded to AI for categorization, cutting a '
                                        'two-day job to two hours [SaaS Procurement Insider — udHdwtjP7yM '
                                        '@ 00:01:50], with free trials auto-renewing on cards flagged '
                                        'separately.'},
                            {'name': 'identity_join',
                             'type': 'textarea',
                             'prompt': 'Join the spend baseline to identity sources such as SSO, Entra ID, '
                                       'Okta, and the HRIS. Describe the quarterly cross-match that '
                                       'catches leavers and role-changers still holding paid seats, and '
                                       'name the owner who runs it.',
                             'example': 'Entra ID and Okta login data joined to the HRIS roster; every '
                                        'quarter the IT asset lead cross-matches app user lists to catch '
                                        'leavers and role-changers holding paid seats [SaaS Procurement '
                                        'Insider — udHdwtjP7yM @ 00:07:57]. Default birthright licenses '
                                        'are listed explicitly in each review because they go unflagged '
                                        'and quietly add up [YouAttest — NCcXkxFkX8k @ 00:05:05].'},
                            {'name': 'cost_per_active_user_triage',
                             'type': 'textarea',
                             'prompt': 'Calculate cost per active user for each tool and sort it into '
                                       'three bands: cancel tools under 20 percent utilization, right-size '
                                       'the middle band 90 days before renewal, and negotiate the rest. '
                                       'Record the band and next action.',
                             'example': 'Diagramming tool at 14 percent active use goes to cancel; the '
                                        'project tracker at 52 percent is right-sized in a review held 60 '
                                        'to 90 days before renewal [NinjaOne IT Tech Tips — ORh7DquM3lY @ '
                                        '00:01:07]. Benchmark context: 44 percent of licenses sit idle in '
                                        'any 30-day window [SAP Concur — ARjBgExQ3oQ @ 00:09:33].'},
                            {'name': 'shadow_it_discovery',
                             'type': 'textarea',
                             'prompt': 'Estimate the share of actual SaaS spend sitting in shadow IT, from '
                                       'employee-expensed apps, departmental buys, and free trials '
                                       'auto-renewing on a credit card. Note which login sources or '
                                       'browser signals reveal them and which tools carry cyber risk '
                                       'needing review.',
                             'example': 'Azure AD and Google Workspace login monitoring plus browser '
                                        'extensions surfaced shadow IT at 22 percent of real spend, inside '
                                        'the 15 to 30 percent band [SaaS Procurement Insider — udHdwtjP7yM '
                                        '@ 00:03:10]. We assume roughly 40 percent of the team is already '
                                        'using these tools [IronEdge Group — nsIixe4EZI0 @ 00:40:04], so '
                                        'those apps join the cyber-risk review first.'},
                            {'name': 'reclaim_workflow',
                             'type': 'textarea',
                             'prompt': 'Design the seat reclaim workflow: inactivity threshold, manager '
                                       'confirmation campaign, document and workspace transfer, automated '
                                       'deactivation, and redeployment to a shared pool. Name the platform '
                                       'or form tool that sends messages and deactivates users through '
                                       'APIs.',
                             'example': 'Reclaim starts at 90 days of inactivity, and owned documents and '
                                        'workspaces transfer before any seat is pulled [Zylo | The Leader '
                                        'in Enterprise SaaS Management — ftGGihhAn3g @ 00:02:37]. An '
                                        'Airtable form handles messaging, collects responses and '
                                        'deactivates users through the APIs [Optimize Information Systems '
                                        '— tex2cNz4vcc @ 00:04:21]; freed seats land in a shared pool for '
                                        'redeployment.'},
                            {'name': 'assignment_records_and_shelf_check',
                             'type': 'textarea',
                             'prompt': 'Before cutting any Adobe or Microsoft seats, document your own '
                                       'month-to-month assignment records. Also mine help desk tickets for '
                                       'repeated purchases of the same tool and check idle licenses on the '
                                       'shelf before approving any new request.',
                             'example': 'Monthly assignment logs are kept because Adobe once assessed a '
                                        'client at 250 seats against 200 in use [MetrixData 360 — '
                                        'lB5ThkY4hMA @ 00:16:32]. Ticket mining found mind-mapping '
                                        'software bought 150 times in 60 days, fixed with a volume '
                                        'agreement and 90-day reclaim [MetrixData 360 — lB5ThkY4hMA @ '
                                        '00:26:16]; a pending Kofax request receives an idle Adobe license '
                                        'instead.'},
                            {'name': 'vendor_usage_data_demand',
                             'type': 'textarea',
                             'prompt': 'List the usage data you will demand from each vendor in writing '
                                       'before renewal: user list, last login, 90-day login count, and '
                                       "session duration. Record each vendor's response and treat any "
                                       'refusal as a negotiation signal worth noting.',
                             'example': 'Written request sent to the CRM vendor for user list, last login, '
                                        '90-day login count and session duration; the vendor declined, '
                                        'logged as a signal [SaaS Procurement Insider — udHdwtjP7yM @ '
                                        '00:06:44], since vendors know SSO access arms buyers to negotiate '
                                        '[SaaS Procurement Insider — udHdwtjP7yM @ 00:07:20]. Comparable '
                                        'case: 40 seats renewed at 19,200 euros with only 12 actual '
                                        'users.'},
                            {'name': 'notice_deadline_calendar',
                             'type': 'text',
                             'prompt': 'Calendar the contractual notice deadline for each auto-renewing '
                                       'contract, not the renewal date. Count the notice period literally, '
                                       'name an owner and a backup for the reminder, and record the '
                                       'address where written notice must be delivered.',
                             'example': 'Renewal on December 31 with a 60-day notice clause means notice '
                                        'by November 1, while a two-month clause means October 31 [fynk — '
                                        'QLqtDhk3PoI @ 00:02:19]. Reminder routes to the finance owner and '
                                        'an IT backup [fynk — QLqtDhk3PoI @ 00:02:44]. Notice goes to the '
                                        'contract address with delivery proof, because a friendly chat may '
                                        'not count [fynk — QLqtDhk3PoI @ 00:04:10].'},
                            {'name': 'price_cap_language',
                             'type': 'textarea',
                             'prompt': 'Write the renewal price cap you will demand, targeting 3 to 5 '
                                       'percent. Define what the percentage applies to, whether the cap '
                                       'multiplies across term length, and any volume, spend, or term '
                                       'conditions attached to it.',
                             'example': 'Supplier paper allowed 5 to 25 percent increases; we countered '
                                        'with a 4 percent cap [Tropic — FESALIJcxS0 @ 00:02:00]. Redline '
                                        'specifies 4 percent of last-year net spend, not CPI plus four '
                                        '[Marcus Harris Software & Tech Attorney — PQUXMXjSfjw @ '
                                        '00:04:17], and states that added users come at existing pricing '
                                        'without renegotiation [Heather Meeker — RDxElFsVuWs @ 00:10:00].'},
                            {'name': 'negotiation_sequence',
                             'type': 'textarea',
                             'prompt': 'Lay out the negotiation sequence for your largest renewal: kickoff '
                                       'date, who attends discovery calls, year-one price target, '
                                       'multi-year concessions sought, and exit terms. Flag any '
                                       'acceleration clause and any downscaling rights you need written '
                                       'into the contract.',
                             'example': 'Kickoff set 75 days out with the CFO kept off discovery calls '
                                        '[Tropic — veu6EUBTdBE @ 00:02:57]. Year-one price gets negotiated '
                                        'before multi-year is offered for concessions [Tropic — '
                                        "veu6EUBTdBE @ 00:04:24]. The exit clause's acceleration of "
                                        'remaining fees is struck [Marcus Harris Software & Tech Attorney '
                                        '— xY5Bk1dd768 @ 00:06:35], and downscaling rights are written in '
                                        '[Redress Compliance — -1Sqw4pgdxY @ 00:01:57].'}],
                 'completion_gate': 'The worksheet is complete when every tool carries a '
                                    'cost-per-active-user band, every auto-renewing contract has a '
                                    'calendared notice deadline with owner and backup, vendor usage data '
                                    'is requested in writing, and the price cap definition is redlined.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'SaaS Sales Engine and Pricing Architecture Blueprint',
                 'purpose': 'Translate cold-call volume, procurement-proof business cases, and quota math '
                            'into a repeatable selling motion, then design seat, credit, and uplift '
                            'pricing that protects gross margin from heavy AI users and survives '
                            'enterprise buyer pushback at renewal.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Measure dials, conversations, and meetings per block before judging any '
                                  'opener or script, and retire openers that book nothing.',
                                  'Keep price as the final issue with procurement and bring the champion '
                                  'into every pricing conversation.',
                                  'Pair every concession with something received in return and log it in '
                                  'the concession ledger the same day.',
                                  'Model P50 and P90 cost per user before publishing any AI credit '
                                  'allowance or usage tier.',
                                  'Store renewal uplift terms on the quote itself so no renewal ships at '
                                  "the prior year's price by accident."],
                 'fields': [{'name': 'cold_call_cadence',
                             'type': 'textarea',
                             'prompt': 'Set the weekly cold-call cadence: dial hours per day, calls per '
                                       'hour, total weekly dials, and the meeting target those dials '
                                       'should produce. Write the permission opener you will use and the '
                                       'meeting, not the product, you are selling.',
                             'example': 'One hour a day at 40 calls an hour gives 200 dials a week and at '
                                        'least two meetings [Sell Better — aW8jAYnvqyI @ 00:00:13]. Opener '
                                        "ends with permission check: I'm not looking to sign you guys up, "
                                        'is that fair [Sales Scripter — u9D8WbQixac @ 00:09:27]. Close by '
                                        'asking for calendars, booking today or tomorrow, triple confirm '
                                        '[Sell Better — m2z1tgfv8Kc @ 00:13:34].'},
                            {'name': 'opener_test_log',
                             'type': 'textarea',
                             'prompt': 'Log each opener by dial block: dials made, conversations reached, '
                                       'and meetings booked. Retire any opener whose block books nothing, '
                                       'and record your success rate against the average cold-call '
                                       'benchmark and the talk ratio you held.',
                             'example': 'Opener A ran 400 dials and booked zero, so it is retired, the '
                                        "lesson from Armand's 800 dials over four weeks with no meetings "
                                        '[Sell Better — aW8jAYnvqyI @ 00:08:01]. Opener B hit 2.1 percent '
                                        'against the 1.48 percent average, with a 55/45 talk ratio [Sell '
                                        'Better — m2z1tgfv8Kc @ 00:00:03]; a calendar hold follows each '
                                        'booking.'},
                            {'name': 'procurement_business_case',
                             'type': 'textarea',
                             'prompt': 'Build the business case you will walk procurement through: the '
                                       'champion in the room, the measurable return, and the spend '
                                       'requested. Keep price as the final issue and record how believable '
                                       'the executive sponsor rates the numbers.',
                             'example': 'Model follows the Gong case: 80 new AEs ramping one month faster '
                                        'at $40k ARR each equals $3.2M against $385k spend [Caliber '
                                        '(Formerly pclub.io) — lmaQjDuWaSY @ 00:03:57]. After walking '
                                        "procurement through the CRO's numbers, we asked how believable "
                                        "they were; 'very believable' moved a $200k budget to a $385k "
                                        'signature [Caliber (Formerly pclub.io) — lmaQjDuWaSY @ '
                                        '00:03:36].'},
                            {'name': 'concession_ledger',
                             'type': 'textarea',
                             'prompt': 'Keep a concession ledger for the deal: each give, what you '
                                       'received in return, and when it was offered. Confirm cash is the '
                                       'last objection before conceding quarterly billing, net 60 or 90 '
                                       'terms, or delayed payments.',
                             'example': 'Give: quarterly billing. Get: a two-year term and a case study. '
                                        'Offered only after the buyer confirmed cash was the last blocker, '
                                        'following the rule do not offer that until you know it is the '
                                        'last thing [Caliber (Formerly pclub.io) — lmaQjDuWaSY @ '
                                        '00:08:39]. Every give is paired, because dragons only get '
                                        'hungrier when fed [Caliber (Formerly pclub.io) — B5SsF-kHahw @ '
                                        '00:09:19].'},
                            {'name': 'quota_ote_model',
                             'type': 'text',
                             'prompt': 'Set quota as a multiple of on-target earnings for each rep and '
                                       'record the attainment assumption behind the headcount plan. State '
                                       'the SDR-to-AE ratio for your segment and the correction you will '
                                       'make if it overspends.',
                             'example': "A $200K OTE rep carries about $1M quota at 5x, against Bridge's "
                                        '4.6x median [SaasRise — 3enRkyZlcQk @ 00:00:36]. The plan does '
                                        'not assume 80 percent attainment with doubled reps, since 91 '
                                        'percent of companies missed quota [The SaaS CFO — uBngVWkX0K4 @ '
                                        '00:27:09]. Mid-market SDR bench cut from 2.5:1 to 2:1 '
                                        '[GrowthSpree - AI Native B2B Marketing Agency — 2dLvgvK0qCY @ '
                                        '00:02:07].'},
                            {'name': 'renewal_automation',
                             'type': 'textarea',
                             'prompt': 'Describe the CRM automation that surfaces every renewal before it '
                                       'lapses: trigger object, days-before-expiry threshold, agreement '
                                       'repository search, and who receives the task. Include how call '
                                       'notes are captured automatically into the customer record and '
                                       'which integration handles it.',
                             'example': 'HubSpot workflow fires on the contract object when the renewal '
                                        'date is less than 30 days away [HubSpot Data Analytics by '
                                        'MergeYourData — ahHk4naTV0s @ 00:00:46]. Each Monday the account '
                                        'manager opens the Docusign Agreements tab, sorts by expiration '
                                        'and pulls MSAs expiring in 90 days [Docusign — HlJxNYkv7AY @ '
                                        '00:00:24]. RingCentral call notes sync through Zapier.'},
                            {'name': 'pricing_metric',
                             'type': 'textarea',
                             'prompt': 'Name the pricing metric for your offer and test it: is it '
                                       'non-arbitrary, can a computer count it, and does it leave friction '
                                       'only at the price point. Record which internal teams and customers '
                                       'validated the metric before launch.',
                             'example': 'Metric chosen: active workflows per month, countable by the '
                                        'billing system and non-arbitrary [Willingness to Pay — '
                                        'rTGrwbYBlXg @ 00:02:50]. The checkout flow leaves one friction '
                                        'point at the price instead of four [Willingness to Pay — '
                                        'tNlpy7MZ8Vk @ 00:01:02]. Validated internally with finance, '
                                        'customer success, sales and product, then externally with '
                                        'customers [Willingness to Pay — KGmwDKTR6fQ @ 00:00:59].'},
                            {'name': 'hybrid_margin_model',
                             'type': 'textarea',
                             'prompt': 'Model the hybrid structure: base seat fee, included credits, and '
                                       'metered overage. Calculate P50 and P90 cost per user against the '
                                       'price point, confirm at least 60 percent gross margin at P50, and '
                                       'note retention alongside growth.',
                             'example': 'Seat at $40 with 500 AI credits; P50 user costs $14, a 65 percent '
                                        'margin, while P90 costs five times that, so overage applies past '
                                        'the credit pool [The Innovation Attorney — ubYfOw6FSPA @ '
                                        '00:21:13]. Hybrid chosen for its 105 percent net revenue '
                                        'retention versus 102 for subscription [The Innovation Attorney — '
                                        'ubYfOw6FSPA @ 00:09:42].'},
                            {'name': 'renewal_uplift',
                             'type': 'textarea',
                             'prompt': 'Specify the renewal uplift stored on each quote, fixed or maximum, '
                                       'and the opening escalator you will anchor with. Explain how the '
                                       'uplift is applied automatically at renewal and where CPI replaces '
                                       'a fixed rate for buyers expected to haggle.',
                             'example': 'Escalator talks open at seven percent, expecting procurement to '
                                        'land near four [Champion Leadership — jOL79tUtq3o @ 00:31:08]. '
                                        'Standard quotes store a fixed 5 percent uplift, so a $100 line '
                                        'becomes $105 automatically [MonetizeNow — x0K0bAATQIA @ '
                                        '00:03:06]; enterprise quotes use a maximum uplift as the '
                                        'negotiation ceiling instead [MonetizeNow — x0K0bAATQIA @ '
                                        '00:00:21].'},
                            {'name': 'ai_usage_guardrails',
                             'type': 'textarea',
                             'prompt': 'Set guardrails for AI usage: fair-use policy, pilot cohort size '
                                       'before full rollout, and the meters buyers will watch. Price in '
                                       'the alerts, rollover, locked overage pricing, and contractual caps '
                                       'enterprise buyers are likely to demand at signature.',
                             'example': 'Fair-use policy caps heavy users, avoiding the unlimited plan '
                                        'where about 5 percent of users bled an image-generation company; '
                                        'usage opens to a 12-customer pilot first [Champion Leadership — '
                                        'jOL79tUtq3o @ 00:18:01]. Contract template already offers alerts '
                                        'at 80 and 100 percent, rollover, locked overage pricing and a '
                                        'hard cap [Soft Learn Hub — oDjXoRkYaA0 @ 00:02:18].'}],
                 'completion_gate': 'Release the plan only when openers have dial-block results, quota is '
                                    'set as an OTE multiple with realistic attainment, P50 gross margin '
                                    'clears 60 percent, uplift terms sit on every quote, and an AI '
                                    'fair-use policy is piloted.'}]}
