from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'saas-license-audits-shadow-it-rightsizing',
 'question_prompt': 'How do I uncover SaaS sprawl, shadow IT, and unused licenses, then rightsize seats '
                    'before money is wasted?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'SaaS License Audits, Shadow IT, and Rightsizing',
 'subtitle': 'Vendor-count license audits, Airtable audit automation, Zylo, Flexera, and CloudEagle SaaS '
             'management, shadow IT discovery and cyber-risk assessment, recurring SaaS review cycles, '
             'third-party vendor risk audits, hidden SaaS waste, shelfware, ServiceNow SAM contract '
             'tracking, and identity-based license rightsizing',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree that leadership underestimates its SaaS estate by two to four '
                      'times, that shadow IT makes up 15 to 30% of real spend, and that roughly a third of '
                      'spend is waste, with Zylo measuring 44% of licenses idle in any 30-day window. The '
                      'street build order is money first (12 months of ERP, invoice and Concur data), '
                      'identity second (SSO, Entra ID, Okta, HRIS), then cost per active user and a '
                      'three-band triage that cancels sub-20% tools, right-sizes the middle 90 days before '
                      'renewal and negotiates the rest. Reclaim runs on Airtable forms, YouAttest manager '
                      'campaigns, Flexera E5-to-E1 downgrades and help desk ticket mining that saved a '
                      'MetrixData 360 client over $250K a year. The split: platform vendors sell '
                      'automation, while Mike Austin insists tools do not equal transformation and '
                      'Adobe-style assignment history can bite back.',
 'key_metrics': [{'label': 'Vendor Count Underestimate',
                  'metric': 'Vendor Count Underestimate',
                  'value': '2-4x the 40-70 vendors leaders estimate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Leaders guess 40 to 70 SaaS vendors; a proper audit finds two to four times '
                             'more, driven by shadow IT, departmental buys and free trials auto-renewing '
                             'on a credit card.',
                  'source': 'SaaS Procurement Insider ([udHdwtjP7yM @ 00:00:00])'},
                 {'label': 'Licenses Wasted per 30-Day Period',
                  'metric': 'Licenses Wasted per 30-Day Period',
                  'value': '44%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Zylo SaaS Management Index figure presented with SAP Concur, alongside '
                             'average annual software spend of about $50M and 37% of apps bought by '
                             'employees and expensed.',
                  'source': 'SAP Concur ([ARjBgExQ3oQ @ 00:09:33])'},
                 {'label': 'Shadow IT Share of Actual Spend',
                  'metric': 'Shadow IT Share of Actual Spend',
                  'value': '15-30%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Shadow IT detected by SaaS management platforms monitoring Azure AD and '
                             'Google Workspace logins plus browser extensions; first-90-day savings cover '
                             'platform cost many times over.',
                  'source': 'SaaS Procurement Insider ([udHdwtjP7yM @ 00:03:10])'},
                 {'label': 'Help Desk Ticket Reclaim Savings',
                  'metric': 'Help Desk Ticket Reclaim Savings',
                  'value': 'Over $250K per year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Mind-mapping software bought 150 times in 60 days inside an estate of 1,500 '
                             'licenses with 750 unused for over six months; fixed with a volume agreement, '
                             '90-day reclaim and shared pool.',
                  'source': 'MetrixData 360 ([lB5ThkY4hMA @ 00:26:16])'}],
 'sections': [{'number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ["Every operator who has opened up a client's books reports the same blind "
                              'spot: leadership undercounts its SaaS footprint by a wide margin. SaaS '
                              'Procurement Insider says leaders guess 40 to 70 vendors and a proper audit '
                              'lands two to four times higher, driven by shadow IT, departmental buys, and '
                              'free trials quietly auto-renewing on a credit card [udHdwtjP7yM @ '
                              '00:00:00]. Zylo co-founder Ben, presenting with SAP Concur, gives the '
                              'enterprise version: a financial services firm estimated $100M in spend and '
                              'discovery surfaced $300M, while a high-growth tech company that believed it '
                              'ran 70 apps actually had 223, with 118 arriving through expense reports '
                              "[ARjBgExQ3oQ @ 00:16:23]. Zylo's index adds that 37% of apps are bought by "
                              'employees and expensed, and IT now buys only about 18% of software, so the '
                              'purchase trail sits with finance, business units and individual staff '
                              'rather than one owner [ARjBgExQ3oQ @ 00:10:21]. Mike Austin of MetrixData '
                              '360 frames the same gap as an ownership failure: shadow IT thrives where '
                              "nobody owns the category, illustrated by a manager approving a tool at '20 "
                              "bucks a month' [lB5ThkY4hMA @ 00:34:04]. The baseline prerequisite is an "
                              'honest master list of who pays for what, built before anyone argues about '
                              'which tool to buy.',
                              'The consensus build order starts with money, then identity. SaaS '
                              'Procurement Insider pulls every vendor payment from the last 12 months out '
                              'of the ERP and invoices, starting from the SaaS cost category, then '
                              'cross-references the SSO directory, calling authentication data a '
                              "'goldmine'; invoices plus SSO get an operator 80% of the way [udHdwtjP7yM @ "
                              '00:03:50]. CloudEagle teaches the identical sequence for smaller shops: '
                              'start from accounting records, cross-check the IT admin list, and capture '
                              "app, owner, license count and renewal date [M0ICfl_2HyY @ 00:01:48]. Zylo's "
                              "'follow the money' pillar runs across Concur and the ERP with AI "
                              'normalization, and the Concur integration pulls a full year of history, '
                              'scans every expense category because miscategorization is common, and '
                              'tracks spend down to the individual employee [ARjBgExQ3oQ @ 00:22:55]. '
                              "NinjaOne's review-cycle playbook then layers identity on top, integrating "
                              'the SaaS management platform with Entra ID or Okta and tracking four '
                              'metrics: inventory by department, active versus dormant users, allocation '
                              'versus utilization, and security posture covering MFA, SSO and access '
                              'controls [ORh7DquM3lY @ 00:01:31]. Across all four, the master list is the '
                              'asset: vendor, annual cost, cost center, renewal date and contract owner '
                              'are the fields that later drive every cut and every negotiation.',
                              'On the size of the prize, practitioners converge on roughly a third of '
                              "spend. Mike Austin says Gartner's 30% SaaS waste figure is 'conservative,' "
                              'that he routinely finds 30 to 40% waste in Microsoft 365, and that on a '
                              "$10M SaaS budget that means $3M burned [lB5ThkY4hMA @ 00:15:17]. Zylo's "
                              'SaaS Management Index puts license waste at 44% in any 30-day period, '
                              'against average annual software spend of about $50M, making software the '
                              'second-largest operating expense after people [ARjBgExQ3oQ @ 00:09:33]. '
                              'SaaS Procurement Insider expects a first audit to surface 15 to 30% of '
                              'spend to eliminate or right-size, and opens the right-size conversation '
                              'with the vendor 90 days before renewal [udHdwtjP7yM @ 00:15:33]. NinjaOne '
                              'sets the same clock, holding reviews 60 to 90 days ahead of major renewals '
                              'so there is time to optimize, with quarterly cycles for high-change '
                              'environments, semi-annual for stable clients, and an annual baseline before '
                              'renewals, M&A, layoffs or audits [ORh7DquM3lY @ 00:01:07]. The shared logic '
                              "is blunt: auto-renewal at last year's count is where the money leaks, so "
                              'the audit has to finish while there is still leverage to cut seats, '
                              'downgrade tiers, or walk away entirely.'],
               'table': {'caption': 'Where the practitioners agree before a single license is touched',
                         'headers': ['Consensus Point',
                                     'What Operators Agree On',
                                     'Anchor Number or Signal',
                                     'Expert Source'],
                         'rows': [['Leadership undercounts the real SaaS vendor footprint',
                                   'Shadow IT, departmental buys and auto-renewing free trials inflate the '
                                   'true count',
                                   'Leaders guess 40 to 70 vendors; audits find 2 to 4 times more',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:00:00])'],
                                  ['Follow the money through expense and ERP data first',
                                   'Concur and ERP spend discovery with AI normalization exposes hidden '
                                   'enterprise outlay',
                                   'Financial services firm estimated $100M; Zylo discovery found $300M',
                                   'SAP Concur ([ARjBgExQ3oQ @ 00:16:23])'],
                                  ['Shadow IT is a material share of total spend',
                                   'SaaS management platforms watch Azure AD, Google Workspace logins and '
                                   'browser extensions',
                                   'Shadow IT runs 15 to 30% of actual SaaS spend',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:03:10])'],
                                  ['Waste is larger than the analyst headline number',
                                   "Gartner's 30% SaaS waste estimate is called conservative in live "
                                   'client estates',
                                   '30 to 40% Microsoft 365 waste found on a routine basis',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:06:44])'],
                                  ['Reviews must land well before the renewal date',
                                   'Quarterly for high-change clients, semi-annual for stable ones, annual '
                                   'baseline otherwise',
                                   'Reviews held 60 to 90 days before every major renewal',
                                   'NinjaOne IT Tech Tips ([ORh7DquM3lY @ 00:01:07])'],
                                  ['Inventory starts in accounting, then the IT admin list',
                                   'Cross-check accounting records against admin lists for every '
                                   'subscription found',
                                   'App, owner, license count and renewal date as the minimum record',
                                   'CloudEagle ([M0ICfl_2HyY @ 00:01:48])'],
                                  ['Approved-app lists are always incomplete in practice',
                                   'Browser-based discovery flags newly connected apps that never passed '
                                   'security review',
                                   '160 newly connected apps found; 17 approved, 4 not approved',
                                   'AppOmni ([EEuTZMr-lgI @ 00:00:39])']]}},
              {'number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['SaaS Procurement Insider runs the sharpest usage math. Last login gets '
                              "tracked, but login frequency is 'most important' and most audits miss it: a "
                              'user logging in three times a year belongs on a restricted tier, and an '
                              'average session of 90 seconds signals view-only use [udHdwtjP7yM @ '
                              '00:05:06]. The killer number is cost per active user, annual cost divided '
                              'by users with at least four logins in 90 days; in the worked example, a '
                              '$30,000 contract becomes $1,071 per active user, with 122 people never '
                              'touching it [udHdwtjP7yM @ 00:09:37]. Triage follows in three bands: below '
                              '20% usage gets a 30-day justification window and is otherwise cancelled, 20 '
                              'to 70% gets right-sized with the vendor 90 days out, and above 70% gets '
                              "negotiated for escalation clauses and a flat renewal. CloudEagle's cut line "
                              "is blunter: 'cancel any tools with zero logins in the last quarter,' and "
                              'when only 2 of 20 licenses are live, trim the rest [M0ICfl_2HyY @ '
                              '00:03:15]. Zylo calibrates the threshold at 90 days of inactivity, shorter '
                              'for daily-use apps, insists on validating the data source and the logic '
                              "that defines 'active,' and decides up front whether users get a choice or "
                              'seats are reclaimed automatically [ftGGihhAn3g @ 00:02:37].',
                              'For the reclaim itself, the operators push automation hard. Chris of '
                              'Optimize Information Systems faced an Asana renewal on Friday with 600 '
                              "licenses allowed and 802 in use, 801 of them real, and says 'I never do "
                              "this manually anymore' [tex2cNz4vcc @ 00:01:56]. His Airtable build pulls "
                              'user lists through integrations, scopes the audit to three months unused, '
                              "messages each user by email or Slack with a yes-or-no 'need continued "
                              "access?' form plus justification, lets Airtable's native AI judge each "
                              'answer against admin-supplied valid reasons, auto-confirms the keepers, '
                              'flags weak answers for admin review, and deactivates denials through the '
                              "app's API [tex2cNz4vcc @ 00:04:21]. YouAttest takes the manager route: "
                              'Craig, a senior director of technology and cyber security at a '
                              "pharmaceutical company, ran a 'Jira licenses' campaign that auto-delegates "
                              'to managers by email to certify or revoke, fed automatically from Okta, '
                              'Azure AD or JumpCloud or from a CSV for siloed apps, and reusing his '
                              "access-review tool for licenses cost 'not a cent more' [NCcXkxFkX8k @ "
                              '00:03:27]. Flexera wires discovery into Microsoft by opening App '
                              'registrations in the Azure portal, adding Microsoft Graph permissions, '
                              'recording tenant ID, client ID and client secret, and configuring the Entra '
                              'ID connector the same way [PNMNLFBOp7E @ 00:01:31].',
                              'The biggest single wins come from tier surgery and procurement plumbing. '
                              "Flexera's rightsizing view shows 4,454 users with no activity in Apps for "
                              'Enterprise who could drop from E5 to E1, non-Power BI users who could move '
                              'from E5 to E3, and users holding both E3 and E5, priced at negotiated cost '
                              'rather than MSRP across an E5 bundle of 39 apps [PNMNLFBOp7E @ 00:03:47]. '
                              'Mike Austin mined help desk tickets and found mind-mapping software bought '
                              '150 times in 60 days inside an estate of 1,500 licenses, 750 of them unused '
                              'for over six months; the fix was a commercial volume agreement instead of '
                              'web pricing, reclaim after 90 days of non-use with a five-day email '
                              'warning, and a shared pool for reclaimed seats, worth over $250K a year '
                              '[lB5ThkY4hMA @ 00:26:16]. SaaS Procurement Insider demands user lists, last '
                              'login, 90-day login counts and session duration from the vendor in writing, '
                              'treats refusal as a signal, writes usage-data rights into the contract, and '
                              'asks for SSO at no extra cost framed as security and compliance '
                              '[udHdwtjP7yM @ 00:06:24]. Provision Networks brings usage data to the table '
                              'too, citing downtime or that 40% never adopted premium features '
                              '[Q3VZHAsymcg @ 00:03:56].'],
               'table': {'caption': 'Street mechanics, triggers and the numbers practitioners actually '
                                    'reported',
                         'headers': ['Mechanic',
                                     'Exact Setup or Trigger',
                                     'Reported Number',
                                     'Expert Source'],
                         'rows': [['Cost per active user calculation on every contract',
                                   'Divide annual cost by users with at least four logins in 90 days',
                                   '$30,000 contract becomes $1,071 per active user; 122 never used it',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:09:37])'],
                                  ['Three-band usage triage before each renewal',
                                   'Eliminate after 30-day justification, right-size 90 days out, '
                                   'negotiate flat renewal',
                                   'Below 20% eliminate, 20 to 70% right-size, above 70% negotiate',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:09:58])'],
                                  ['Airtable automated reclaim with AI-judged justification forms',
                                   'Pull user lists, scope three months unused, message users, deactivate '
                                   'via API',
                                   'Asana: 600 licenses allowed against 802 in use, renewal due Friday',
                                   'Optimize Information Systems ([tex2cNz4vcc @ 00:00:31])'],
                                  ['Help desk ticket mining into a shared license pool',
                                   'Volume agreement replaces web price; reclaim after 90 idle days, '
                                   'five-day warning',
                                   '1,500 licenses, 750 unused six months; over $250K saved yearly',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:26:16])'],
                                  ['Microsoft 365 tier downgrades through Entra ID and Graph connectors',
                                   'Target unassigned subscriptions and inactive users, priced at '
                                   'negotiated cost not MSRP',
                                   '4,454 inactive Apps for Enterprise users could move E5 to E1',
                                   'Flexera | ITAM, FinOps & SaaS Management ([PNMNLFBOp7E @ 00:03:47])'],
                                  ['Manual audit versus paid platform break-even point',
                                   'Spreadsheets work under 500 employees; platforms like Nudge charge per '
                                   'active user',
                                   'Nudge at $5 per active user monthly; payback in a quarter above $2M '
                                   'spend',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:12:36])'],
                                  ['Manager-delegated license certification campaigns via identity '
                                   'provider',
                                   'Okta, Azure AD or JumpCloud feed, or CSV upload for siloed apps',
                                   'Reusing the existing access-review tool for licenses cost not a cent '
                                   'more',
                                   'YouAttest ([NCcXkxFkX8k @ 00:02:16])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Shortcuts the operators use to find seats nobody else finds',
                           'body': 'These are the small moves practitioners use to compress audit time, '
                                   'catch hidden seats, and stop new spend before it lands.',
                           'items': ['Upload the 12-month transaction CSV to AI for categorization; a job '
                                     'that takes two days drops to two hours [SaaS Procurement Insider — '
                                     'udHdwtjP7yM @ 00:01:50]',
                                     'Cross-match app user lists against HRIS every quarter to catch '
                                     'leavers and role-changers still holding paid seats [SaaS Procurement '
                                     'Insider — udHdwtjP7yM @ 00:07:57]',
                                     "Hunt default 'birthright' licenses explicitly; they go unflagged in "
                                     'reviews and quietly add up [YouAttest — NCcXkxFkX8k @ 00:05:05]',
                                     'Before approving a new tool request, check the shelf: a Kofax '
                                     'request stuck in a 4 to 20 week approval should have been offered an '
                                     'idle Adobe license instead [MetrixData 360 — lB5ThkY4hMA @ '
                                     '00:30:57]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the money-first master list',
                              'action': 'Pull 12 months of vendor payments and expense data into one list.',
                              'detail': 'Start from the SaaS cost category in the ERP and invoices, '
                                        'recording vendor, annual cost, cost center, renewal date and '
                                        'contract owner [SaaS Procurement Insider — udHdwtjP7yM @ '
                                        '00:01:30]; scan every Concur expense category because '
                                        'miscategorization is common [SAP Concur — ARjBgExQ3oQ @ '
                                        '00:22:55].'},
                             {'step': 2,
                              'title': 'Overlay identity and usage data',
                              'action': 'Connect SSO and the identity provider to measure real usage per '
                                        'seat.',
                              'detail': 'Integrate the SMP with Entra ID or Okta and track active versus '
                                        'dormant users and allocation versus utilization [NinjaOne IT Tech '
                                        'Tips — ORh7DquM3lY @ 00:01:31]; log last login, login frequency '
                                        'and average session duration, where 90-second sessions mean '
                                        'view-only use [SaaS Procurement Insider — udHdwtjP7yM @ '
                                        '00:05:45].'},
                             {'step': 3,
                              'title': 'Score and triage every app',
                              'action': 'Compute cost per active user and sort into eliminate, right-size '
                                        'or negotiate.',
                              'detail': 'Below 20% usage gets a 30-day justification window, 20 to 70% is '
                                        'right-sized with the vendor 90 days out, above 70% is negotiated '
                                        'for a flat renewal [SaaS Procurement Insider — udHdwtjP7yM @ '
                                        '00:09:58]; cancel tools with zero logins in the last quarter '
                                        'outright [CloudEagle — M0ICfl_2HyY @ 00:03:15].'},
                             {'step': 4,
                              'title': 'Run the automated reclaim',
                              'action': 'Message dormant users, collect justifications, deactivate and '
                                        'pool the seats.',
                              'detail': 'Airtable sends yes-or-no access forms, AI judges each '
                                        'justification, weak answers go to admin review, and denials are '
                                        'deactivated via API [Optimize Information Systems — tex2cNz4vcc @ '
                                        '00:02:20]; reclaimed seats go to a shared pool after 90 days of '
                                        'non-use and a five-day email warning [MetrixData 360 — '
                                        'lB5ThkY4hMA @ 00:26:16].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether an audit needs a platform at all. SaaS '
                              'Procurement Insider draws a hard line: a manual audit built from invoices '
                              'plus SSO data works under 500 employees, while above $2M in SaaS spend a '
                              'platform pays for itself inside a quarter, with Nudge priced at $5 per '
                              'active user per month [udHdwtjP7yM @ 00:13:16]. Chris at Optimize '
                              'Information Systems never runs license audits manually anymore, wiring '
                              'Airtable into the stack so it pulls user lists, messages every inactive '
                              'user, and deactivates through the API [tex2cNz4vcc @ 00:01:56]. Provision '
                              'Networks calls manual audits basically extinct in modern IT operations, '
                              'pointing to platforms that connect through SSO and APIs and scan expense '
                              'data for shadow IT [Q3VZHAsymcg @ 00:02:15]. Mike Austin of MetrixData 360 '
                              "pushes hard the other way: you don't need another tool, because tools do "
                              'not equal transformation, inventories do not show usage, and the biggest '
                              'win came from mining the help desk tickets a client already had '
                              '[lB5ThkY4hMA @ 00:21:23]. The operator read is that the tool debate is '
                              "really a spend-and-headcount threshold question, and Austin's flywheel of "
                              'intelligence plus ownership plus leverage means a platform bought without '
                              'an owner does not move the number by itself.',
                              'Practitioners agree dormant seats must come back, but they split on the '
                              'trigger and on who makes the final call. Zylo starts at a 90-day inactivity '
                              'threshold, shorter for daily-use apps, and forces a choice between offering '
                              'users the option to keep a seat or reclaiming automatically, with owned '
                              'documents and workspaces transferred first [ftGGihhAn3g @ 00:02:37]. '
                              'CloudEagle is blunter: cancel any tool with zero logins in the last '
                              'quarter, then walk into renewal with the trimmed count, as in the case '
                              'where only 2 of 20 licenses were in use [M0ICfl_2HyY @ 00:03:15]. The '
                              'judgment layer differs even more. Optimize Information Systems sends every '
                              'inactive user a yes-or-no continued-access form with a justification box, '
                              "lets Airtable's native AI grade each answer against admin-supplied valid "
                              'reasons, and escalates only insufficient responses for admin review and '
                              'further follow-ups [tex2cNz4vcc @ 00:02:33]. YouAttest puts humans back in '
                              'the loop, auto-delegating a campaign such as Jira licenses to managers by '
                              'email so each manager certifies or revokes every seat, at no extra cost for '
                              'teams already running access reviews on the platform [NCcXkxFkX8k @ '
                              '00:03:27]. The trade is speed against accountability: AI triage clears a '
                              '2-day renewal window, while manager certification produces a defensible '
                              'sign-off trail.',
                              'Low usage does not mean the same thing to every practitioner. SaaS '
                              'Procurement Insider runs a hard triage: below 20% usage the app gets a '
                              '30-day justification window and is otherwise cancelled, 20% to 70% gets '
                              'right-sized by approaching the vendor 90 days out, and above 70% goes to '
                              'negotiation for escalation clauses and a flat renewal [udHdwtjP7yM @ '
                              '00:09:58]. Provision Networks warns that flat usage often signals a '
                              'training gap, not a bad tool, so the usage number alone does not settle '
                              'whether to cut [Q3VZHAsymcg @ 00:01:12]. On shadow IT the split is cut '
                              'versus redirect. Rob Voit at IronEdge Group says full elimination is '
                              'unlikely and tells teams to ask vendors where data resides, who can access '
                              'it, and how fast they must disclose a breach, while the panel pushes '
                              'sanctioned alternatives such as an internal FTP server or Iron AI '
                              '[nsIixe4EZI0 @ 00:48:04]. Mike Austin of MetrixData 360 makes the same '
                              'redirect argument on cost: a Kofax request facing a 4-to-20-week approval '
                              'should have been offered the Adobe license already sitting on the shelf '
                              '[lB5ThkY4hMA @ 00:30:57]. Elimination wins on dead seats; redirection wins '
                              'when a real need is driving the rogue purchase in the first place.'],
               'table': {'caption': 'Competing playbooks on tooling, reclaim triggers, usage triage, '
                                    'cadence, and review ownership',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Buy a SaaS management platform or audit manually',
                                   'Manual invoices plus SSO works under 500 employees; a platform pays '
                                   'back in a quarter above $2M spend',
                                   'Never audit manually anymore; Airtable pulls user lists, messages '
                                   'users, and deactivates through the API',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:11:57]); Optimize '
                                   'Information Systems ([tex2cNz4vcc @ 00:01:56])'],
                                  ['Whether any new tooling is needed at all',
                                   "You don't need another tool; mine existing help desk tickets for "
                                   'repeat software purchases',
                                   'Manual audits are basically extinct; platforms connect through SSO, '
                                   'APIs, and expense data scans',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:21:23]); Provision Networks '
                                   '([Q3VZHAsymcg @ 00:02:15])'],
                                  ['Inactivity threshold that triggers license reclamation',
                                   'Start at 90 days, shorter for daily-use apps, and transfer owned '
                                   'documents and workspaces first',
                                   'Cancel any tool with zero logins in the last quarter before the '
                                   'renewal conversation starts',
                                   'Zylo ([ftGGihhAn3g @ 00:02:37]); CloudEagle ([M0ICfl_2HyY @ '
                                   '00:03:15])'],
                                  ['Who judges whether a dormant user keeps the seat',
                                   'Airtable native AI grades user justifications; only insufficient '
                                   'answers reach admin review',
                                   'Managers receive auto-delegated email campaigns and certify or revoke '
                                   'each individual license',
                                   'Optimize Information Systems ([tex2cNz4vcc @ 00:02:33]); YouAttest '
                                   '([NCcXkxFkX8k @ 00:03:27])'],
                                  ['How to read low or flat usage numbers',
                                   'Below 20% usage gets a 30-day justification window, otherwise the app '
                                   'is cancelled outright',
                                   'Flat usage often signals a training gap rather than a bad tool that '
                                   'needs cutting',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:09:58]); Provision '
                                   'Networks ([Q3VZHAsymcg @ 00:01:12])'],
                                  ['Review cadence across the whole SaaS portfolio',
                                   'Annual audit, 90-day pre-renewal review, quarterly top-10 check, '
                                   'offboarding trigger, top-20 renewal calendar',
                                   'Quarterly for high-change environments aligned to QBRs, semi-annual '
                                   'for stable clients, annual baseline',
                                   'SaaS Procurement Insider ([udHdwtjP7yM @ 00:13:36]); NinjaOne IT Tech '
                                   'Tips ([ORh7DquM3lY @ 00:00:45])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is cutting seats while the vendor still holds the '
                              'only usage records. Mike Austin of MetrixData 360 watched a client cut 30% '
                              'of its Adobe licenses, only for Adobe to use assignment history to demand '
                              'more: the client was assessed at 250 licenses against 200 actually in use, '
                              'because Adobe contracts require month-to-month usage records, which Austin '
                              'calls an unofficial audit [lB5ThkY4hMA @ 00:16:32]. Bad information also '
                              'comes from the sell side; one client was told by both its Microsoft rep and '
                              'its reseller that it could not reduce licenses at the anniversary, and '
                              'Austin says it can [lB5ThkY4hMA @ 00:18:14]. Flexera puts the downside in '
                              'numbers: two-thirds of enterprises expect an audit within 12 months, and '
                              '25% of audited organizations pay over $1,000,000 in true-ups [XMooFDnRJEE @ '
                              '00:00:00]. ITAM Now shows how the paperwork itself bites inside ServiceNow '
                              'SAM: entitlements must be imported with manufacturer part numbers rather '
                              'than reseller numbers from CDW, SHI, SoftwareOne or SoftChoice, and the '
                              'import failed until an agreement type was set, with an enterprise agreement '
                              'allowing overage until true-up [JLEo4uQ_STM @ 00:05:01]. Clean entitlement '
                              'and assignment records, kept in-house, are the only real defense when the '
                              'vendor runs its own recount.',
                              'The second failure is trusting license data that cannot see real usage. '
                              "MetrixData 360's Mike Austin says Snow's SaaS connector cannot judge "
                              'whether a user needs E5 or F5, Adobe Pro versus Reader needs telemetry, and '
                              "inventories alone never show usage [lB5ThkY4hMA @ 00:19:23]. Flexera's "
                              'rightsizing demo shows what the telemetry surfaces once connected: 4,454 '
                              'users with no activity in Apps for Enterprise who could drop from E5 to E1, '
                              'non-Power BI users who could move from E5 to E3, and users holding both E3 '
                              'and E5 at once, with savings priced at actual negotiated cost rather than '
                              'MSRP [PNMNLFBOp7E @ 00:03:47]. YouAttest flags the quieter leak: default '
                              'birthright licenses handed out automatically go unflagged and add up over '
                              'time [NCcXkxFkX8k @ 00:05:05]. SaaS Procurement Insider adds that the data '
                              "itself is gated; SSO sits behind the vendor's top tier because vendors know "
                              'SSO access gives buyers the data to negotiate against them, so the play is '
                              'to ask for SSO at no extra cost framed as security and compliance, and to '
                              'treat any refusal to hand over user lists, last login, 90-day login counts '
                              'and session duration as a signal [udHdwtjP7yM @ 00:07:20]. Session length '
                              'matters too: 90-second averages mean view-only use.',
                              'Shadow IT failures land as breach costs and legal exposure, not just wasted '
                              "seats. IronEdge Group's panel cites IBM's 2025 Cost of a Data Breach "
                              'figures: unsanctioned shadow AI adds an average of $670,000 per breach '
                              'against a stated US average breach cost of about $3.3M [nsIixe4EZI0 @ '
                              '00:09:02]. The same panel warns that Copilot indexes SharePoint, so without '
                              'correct permissions and sensitivity labels payroll data can surface to '
                              'ordinary users [nsIixe4EZI0 @ 00:16:16]. The Tech Compliance Blueprint says '
                              'over 60% of all breaches originate through third-party SaaS vendors while '
                              'the enterprise stays legally accountable, and passive questionnaires are '
                              'unenforceable without contract terms: right to audit, MFA and encryption '
                              'warranties, 24-to-48-hour incident notice, and standalone cyber insurance '
                              'for Tier 1 vendors [WiNczR6ugRY @ 00:01:32]. Mike Austin of MetrixData 360 '
                              'traces the cost side to ownership: shadow IT thrives without an owner, one '
                              'manager waved through a tool at 20 bucks a month, and help desk tickets '
                              'showed mind-mapping software bought 150 times in 60 days [lB5ThkY4hMA @ '
                              '00:34:04]. Small approvals priced at $5 or $20 a month, often never '
                              'purchased at all because free trials let tools spread, are exactly how '
                              'waste and attack surface compound together inside the business, one card '
                              'swipe at a time.'],
               'table': {'caption': 'Firsthand traps with the economics check and counter-move each '
                                    'practitioner applied',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check / Counter-Move',
                                     'Expert Source'],
                         'rows': [['Vendor recount after cutting Adobe licenses',
                                   'Client cut 30% of seats; Adobe used assignment history to assess 250 '
                                   'against 200 in use',
                                   'Keep month-to-month usage records yourself because Adobe contracts '
                                   'require them anyway',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:16:32])'],
                                  ['Rep and reseller misinformation at the contract anniversary',
                                   'Microsoft rep and reseller told a client licenses could not be reduced '
                                   'at anniversary',
                                   'Austin says the client can reduce licenses at the anniversary, so push '
                                   'back in writing',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:18:14])'],
                                  ['True-up shock from an unmanaged software license audit',
                                   '25% of audited organizations end up paying over $1,000,000 in true-ups',
                                   'Two-thirds of enterprises expect an audit within 12 months, so '
                                   'normalize the inventory early',
                                   'Flexera | ITAM, FinOps & SaaS Management ([XMooFDnRJEE @ 00:00:00])'],
                                  ['Entitlement import failure inside ServiceNow SAM records',
                                   'The import failed until an agreement type was set on the contract '
                                   'record',
                                   'Use manufacturer part numbers, not reseller numbers, and always '
                                   'download a fresh import template',
                                   'ITAM Now ([JLEo4uQ_STM @ 00:05:01])'],
                                  ['Bundle overspend hidden inside Microsoft E5 licensing tiers',
                                   '4,454 users showed no Apps for Enterprise activity; some users held '
                                   'both E3 and E5',
                                   'Move inactive users from E5 to E1 and price savings at negotiated '
                                   'cost, not MSRP',
                                   'Flexera | ITAM, FinOps & SaaS Management ([PNMNLFBOp7E @ 00:03:47])'],
                                  ['Birthright licenses silently accumulating across the user base',
                                   'Default birthright licenses go unflagged during reviews and keep '
                                   'adding up over time',
                                   'Run manager certification campaigns through Okta, Azure AD, JumpCloud, '
                                   'or a CSV upload',
                                   'YouAttest ([NCcXkxFkX8k @ 00:05:05])'],
                                  ['Auto-renewal carrying bundled modules nobody actually uses',
                                   'A Fortune 100 client was carrying $1.4M of unused ServiceNow modules '
                                   'before cleanup',
                                   'Tie negotiations to performance, refuse bundles, and stop auto-renewal '
                                   'before the date hits',
                                   'MetrixData 360 ([lB5ThkY4hMA @ 00:37:40])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before any seat is cut or any renewal is signed',
                           'body': 'Every item below comes from a loss, a reversal, or a blind spot a '
                                   'practitioner hit firsthand. Clear all four before the reclaim script '
                                   'runs or the renewal paperwork moves.',
                           'items': ['Hold your own month-to-month assignment records before cutting Adobe '
                                     'or Microsoft seats; Adobe assessed one client at 250 against 200 in '
                                     'use [MetrixData 360 — lB5ThkY4hMA @ 00:16:32].',
                                     'Demand the user list, last login, 90-day login count and session '
                                     'duration in writing before renewal, and read a refusal as a signal '
                                     '[SaaS Procurement Insider — udHdwtjP7yM @ 00:06:44].',
                                     'Transfer owned documents and workspaces before reclaiming any seat, '
                                     'starting from a 90-day inactivity threshold [Zylo | The Leader in '
                                     'Enterprise SaaS Management — ftGGihhAn3g @ 00:02:37].',
                                     'Lock Tier 1 vendors into right to audit, MFA and encryption '
                                     'warranties, 24-48 hour incident notice and standalone cyber '
                                     'insurance, because questionnaires alone are unenforceable [The Tech '
                                     'Compliance Blueprint — WiNczR6ugRY @ 00:01:32].']}}],
 'pull_quote': '"Vendors know that SSO access gives you the data to negotiate against them." Attributed to '
               'SaaS Procurement Insider (udHdwtjP7yM @ 00:07:20).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Pull every vendor payment from the last 12 months starting from the finance SaaS '
                      'cost category, AI-categorize the transaction CSV, and build a master list of '
                      'vendor, annual cost, cost center, renewal date and contract owner [SaaS Procurement '
                      'Insider — udHdwtjP7yM @ 00:01:13].',
                      'Calculate cost per active user as annual cost divided by users with 4 or more '
                      'logins in 90 days, the math that turned $30,000 into $1,071 per active user [SaaS '
                      'Procurement Insider — udHdwtjP7yM @ 00:09:37].',
                      'Cross-match the HRIS against app user lists every quarter to catch leavers and '
                      'role-changers still holding seats [SaaS Procurement Insider — udHdwtjP7yM @ '
                      '00:07:57].',
                      'Mine help desk tickets for repeat purchases, move to a commercial volume agreement, '
                      'reclaim after 90 days of non-use with a 5-day email warning, and send reclaimed '
                      'seats to a shared pool, the play that saved over $250K a year [MetrixData 360 — '
                      'lB5ThkY4hMA @ 00:26:16].',
                      'Ask your Concur client success executive for a spend analysis that follows the '
                      'money across expense and ERP data [SAP Concur — ARjBgExQ3oQ @ 00:24:34].',
                      'Keep a decision log of app, decision, justification and follow-ups to create an '
                      'audit trail, and automate PSA/RMM reminders for the next cycle [NinjaOne IT Tech '
                      'Tips — ORh7DquM3lY @ 00:03:33].'],
 'statutory_citations': [{'title': 'SaaS Procurement Insider — The SaaS Licence Audit: You are Paying for '
                                   'More Than You Think. [00:09:58]',
                          'url': 'https://www.youtube.com/watch?v=udHdwtjP7yM&t=598s',
                          'relevance': 'Primary practitioner testimony on the eliminate, right-size and '
                                       'negotiate usage triage and the cost-per-active-user calculation.'},
                         {'title': 'MetrixData 360 — Shadow IT & SaaS Sprawl: Controlling the Hidden '
                                   'Software Costs Draining Your Budget [00:26:16]',
                          'url': 'https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1576s',
                          'relevance': 'Primary practitioner testimony on the help desk ticket reclaim '
                                       'tactic, Adobe assignment-history recounts, and tooling limits.'},
                         {'title': 'IronEdge Group — Shadow IT and SaaS Sprawl: Managing Hidden Cyber '
                                   'Risks [00:09:02]',
                          'url': 'https://www.youtube.com/watch?v=nsIixe4EZI0&t=542s',
                          'relevance': 'Primary practitioner testimony on shadow AI breach costs, Copilot '
                                       'permission exposure, and sanctioned alternatives.'},
                         {'title': 'Flexera | ITAM, FinOps & SaaS Management — SaaS Licence Rightsizing | '
                                   'How to Rightsize SaaS Licences, Subscriptions, and Features | Flexera '
                                   '[00:03:47]',
                          'url': 'https://www.youtube.com/watch?v=PNMNLFBOp7E&t=227s',
                          'relevance': 'Primary practitioner testimony on E5 to E1 and E3 rightsizing and '
                                       'pricing savings at negotiated cost rather than MSRP.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'udHdwtjP7yM',
                       'title': 'The SaaS Licence Audit: You are Paying for More Than You Think.',
                       'channel': 'SaaS Procurement Insider',
                       'author': 'SaaS Procurement Insider',
                       'text': 'Vendors know that SSO access gives you the data to negotiate against them.',
                       'tip': 'Vendors know that SSO access gives you the data to negotiate against them.',
                       'timestamp': 440,
                       'timestamp_seconds': 440,
                       'timestamp_label': '[00:07:20]',
                       'url': 'https://www.youtube.com/watch?v=udHdwtjP7yM&t=440s',
                       'markdown': '[00:07:20](https://www.youtube.com/watch?v=udHdwtjP7yM&t=440s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tex2cNz4vcc',
                       'title': 'How to Automate SaaS License Audits Using Airtable',
                       'channel': 'Optimize Information Systems',
                       'author': 'Optimize Information Systems',
                       'text': 'Airtable handles all the messaging, it collects all the responses, it '
                               'automatically deactivates users using the APIs.',
                       'tip': 'Airtable handles all the messaging, it collects all the responses, it '
                              'automatically deactivates users using the APIs.',
                       'timestamp': 261,
                       'timestamp_seconds': 261,
                       'timestamp_label': '[00:04:21]',
                       'url': 'https://www.youtube.com/watch?v=tex2cNz4vcc&t=261s',
                       'markdown': '[00:04:21](https://www.youtube.com/watch?v=tex2cNz4vcc&t=261s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ARjBgExQ3oQ',
                       'title': 'Zylo Overview: Saas Optimization',
                       'channel': 'SAP Concur',
                       'author': 'SAP Concur',
                       'text': "So there was a gap of $200 million that they didn't even know existed.",
                       'tip': "So there was a gap of $200 million that they didn't even know existed.",
                       'timestamp': 997,
                       'timestamp_seconds': 997,
                       'timestamp_label': '[00:16:37]',
                       'url': 'https://www.youtube.com/watch?v=ARjBgExQ3oQ&t=997s',
                       'markdown': '[00:16:37](https://www.youtube.com/watch?v=ARjBgExQ3oQ&t=997s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lB5ThkY4hMA',
                       'title': 'Shadow IT & SaaS Sprawl: Controlling the Hidden Software Costs Draining '
                                'Your Budget',
                       'channel': 'MetrixData 360',
                       'author': 'MetrixData 360',
                       'text': "So, the thing is you don't need another tool.",
                       'tip': "So, the thing is you don't need another tool.",
                       'timestamp': 1283,
                       'timestamp_seconds': 1283,
                       'timestamp_label': '[00:21:23]',
                       'url': 'https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1283s',
                       'markdown': '[00:21:23](https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1283s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lB5ThkY4hMA',
                       'title': 'Shadow IT & SaaS Sprawl: Controlling the Hidden Software Costs Draining '
                                'Your Budget',
                       'channel': 'MetrixData 360',
                       'author': 'MetrixData 360',
                       'text': "And it's in your own help desk tickets.",
                       'tip': "And it's in your own help desk tickets.",
                       'timestamp': 1576,
                       'timestamp_seconds': 1576,
                       'timestamp_label': '[00:26:16]',
                       'url': 'https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1576s',
                       'markdown': '[00:26:16](https://www.youtube.com/watch?v=lB5ThkY4hMA&t=1576s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ORh7DquM3lY',
                       'title': 'How to Build Recurring SaaS Review Cycles',
                       'channel': 'NinjaOne IT Tech Tips',
                       'author': 'NinjaOne IT Tech Tips',
                       'text': 'Reviews should occur 60-90 days before major renewals to allow time for '
                               'optimization.',
                       'tip': 'Reviews should occur 60-90 days before major renewals to allow time for '
                              'optimization.',
                       'timestamp': 67,
                       'timestamp_seconds': 67,
                       'timestamp_label': '[00:01:07]',
                       'url': 'https://www.youtube.com/watch?v=ORh7DquM3lY&t=67s',
                       'markdown': '[00:01:07](https://www.youtube.com/watch?v=ORh7DquM3lY&t=67s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WiNczR6ugRY',
                       'title': 'Vendor Risk Management: Auditing Your SaaS Vendors for Cyber Liability',
                       'channel': 'The Tech Compliance Blueprint',
                       'author': 'The Tech Compliance Blueprint',
                       'text': 'Not all software vendors pose equal risk to your organization.',
                       'tip': 'Not all software vendors pose equal risk to your organization.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=WiNczR6ugRY&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=WiNczR6ugRY&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nsIixe4EZI0',
                       'title': 'Shadow IT and SaaS Sprawl: Managing Hidden Cyber Risks',
                       'channel': 'IronEdge Group',
                       'author': 'IronEdge Group',
                       'text': "I'd say it's a pretty safe number to say 40% of your team is already using "
                               'this stuff.',
                       'tip': "I'd say it's a pretty safe number to say 40% of your team is already using "
                              'this stuff.',
                       'timestamp': 2404,
                       'timestamp_seconds': 2404,
                       'timestamp_label': '[00:40:04]',
                       'url': 'https://www.youtube.com/watch?v=nsIixe4EZI0&t=2404s',
                       'markdown': '[00:40:04](https://www.youtube.com/watch?v=nsIixe4EZI0&t=2404s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nsIixe4EZI0',
                       'title': 'Shadow IT and SaaS Sprawl: Managing Hidden Cyber Risks',
                       'channel': 'IronEdge Group',
                       'author': 'IronEdge Group',
                       'text': 'And then misconfiguration is fuel, and not knowing about it is a slow '
                               'burn, and then you got a big breach.',
                       'tip': 'And then misconfiguration is fuel, and not knowing about it is a slow burn, '
                              'and then you got a big breach.',
                       'timestamp': 1716,
                       'timestamp_seconds': 1716,
                       'timestamp_label': '[00:28:36]',
                       'url': 'https://www.youtube.com/watch?v=nsIixe4EZI0&t=1716s',
                       'markdown': '[00:28:36](https://www.youtube.com/watch?v=nsIixe4EZI0&t=1716s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EEuTZMr-lgI',
                       'title': 'Shadow IT SaaS Usage: Discover and Assess Your Risk',
                       'channel': 'AppOmni',
                       'author': 'AppOmni',
                       'text': 'Most security teams maintain a list of approved apps, but that list is '
                               'often incomplete.',
                       'tip': 'Most security teams maintain a list of approved apps, but that list is '
                              'often incomplete.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=EEuTZMr-lgI&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=EEuTZMr-lgI&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M0ICfl_2HyY',
                       'title': 'How to Run a SaaS Audit and Cut Unused Tools Before Renewal',
                       'channel': 'CloudEagle',
                       'author': 'CloudEagle',
                       'text': 'First, cancel any tools with zero logins in the last quarter.',
                       'tip': 'First, cancel any tools with zero logins in the last quarter.',
                       'timestamp': 195,
                       'timestamp_seconds': 195,
                       'timestamp_label': '[00:03:15]',
                       'url': 'https://www.youtube.com/watch?v=M0ICfl_2HyY&t=195s',
                       'markdown': '[00:03:15](https://www.youtube.com/watch?v=M0ICfl_2HyY&t=195s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XMooFDnRJEE',
                       'title': 'Saving with Software License Optimization | Flexera',
                       'channel': 'Flexera | ITAM, FinOps & SaaS Management',
                       'author': 'Flexera | ITAM, FinOps & SaaS Management',
                       'text': 'Running in 3 to 6 weeks, full payback in 6 to 12 months, and savings of up '
                               'to 30% of the software budget.',
                       'tip': 'Running in 3 to 6 weeks, full payback in 6 to 12 months, and savings of up '
                              'to 30% of the software budget.',
                       'timestamp': 147,
                       'timestamp_seconds': 147,
                       'timestamp_label': '[00:02:27]',
                       'url': 'https://www.youtube.com/watch?v=XMooFDnRJEE&t=147s',
                       'markdown': '[00:02:27](https://www.youtube.com/watch?v=XMooFDnRJEE&t=147s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q3VZHAsymcg',
                       'title': '**The Hidden IT Tax: 5 Surprising Ways Your SaaS Stack Is Wasting Money**',
                       'channel': 'Provision Networks',
                       'author': 'Provision Networks',
                       'text': 'Manual audits are basically extinct in modern IT operations.',
                       'tip': 'Manual audits are basically extinct in modern IT operations.',
                       'timestamp': 135,
                       'timestamp_seconds': 135,
                       'timestamp_label': '[00:02:15]',
                       'url': 'https://www.youtube.com/watch?v=Q3VZHAsymcg&t=135s',
                       'markdown': '[00:02:15](https://www.youtube.com/watch?v=Q3VZHAsymcg&t=135s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PNMNLFBOp7E',
                       'title': 'SaaS Licence Rightsizing | How to Rightsize SaaS Licences, Subscriptions, '
                                'and Features | Flexera',
                       'channel': 'Flexera | ITAM, FinOps & SaaS Management',
                       'author': 'Flexera | ITAM, FinOps & SaaS Management',
                       'text': 'Do note that we do not use MSRP for these prices.',
                       'tip': 'Do note that we do not use MSRP for these prices.',
                       'timestamp': 209,
                       'timestamp_seconds': 209,
                       'timestamp_label': '[00:03:29]',
                       'url': 'https://www.youtube.com/watch?v=PNMNLFBOp7E&t=209s',
                       'markdown': '[00:03:29](https://www.youtube.com/watch?v=PNMNLFBOp7E&t=209s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8klvxfhjzF4',
                       'title': "How to Stop Renewing SaaS Licenses at Last Year's Count",
                       'channel': 'CloudEagle',
                       'author': 'CloudEagle',
                       'text': 'One audit might save a company tens of thousands.',
                       'tip': 'One audit might save a company tens of thousands.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=8klvxfhjzF4&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=8klvxfhjzF4&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ftGGihhAn3g',
                       'title': 'SaaS License Management, Explained',
                       'channel': 'Zylo | The Leader in Enterprise SaaS Management',
                       'author': 'Zylo | The Leader in Enterprise SaaS Management',
                       'text': 'Start with a 90-day inactivity threshold, shorter for daily-use apps, and '
                               'transfer owned documents and workspaces first.',
                       'tip': 'Start with a 90-day inactivity threshold, shorter for daily-use apps, and '
                              'transfer owned documents and workspaces first.',
                       'timestamp': 157,
                       'timestamp_seconds': 157,
                       'timestamp_label': '[00:02:37]',
                       'url': 'https://www.youtube.com/watch?v=ftGGihhAn3g&t=157s',
                       'markdown': '[00:02:37](https://www.youtube.com/watch?v=ftGGihhAn3g&t=157s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JLEo4uQ_STM',
                       'title': 'ServiceNow SAM: Software License and Contract Renewal',
                       'channel': 'ITAM Now',
                       'author': 'ITAM Now',
                       'text': 'Import entitlements using manufacturer part numbers, not reseller numbers.',
                       'tip': 'Import entitlements using manufacturer part numbers, not reseller numbers.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=JLEo4uQ_STM&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=JLEo4uQ_STM&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NCcXkxFkX8k',
                       'title': 'Rightsizing your SAAS licenses w/ YouAttest',
                       'channel': 'YouAttest',
                       'author': 'YouAttest',
                       'text': 'Default birthright licenses go unflagged and add up.',
                       'tip': 'Default birthright licenses go unflagged and add up.',
                       'timestamp': 305,
                       'timestamp_seconds': 305,
                       'timestamp_label': '[00:05:05]',
                       'url': 'https://www.youtube.com/watch?v=NCcXkxFkX8k&t=305s',
                       'markdown': '[00:05:05](https://www.youtube.com/watch?v=NCcXkxFkX8k&t=305s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
