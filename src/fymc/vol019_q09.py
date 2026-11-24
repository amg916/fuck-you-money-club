from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'saas-renewal-management',
 'question_prompt': 'How are SaaS renewals tracked, forecast, and negotiated, and where do buyers '
                    'overspend?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'SaaS Renewal Management',
 'subtitle': 'Notice-deadline tracking and free renewal trackers, renewal tools such as Zylo, Flexera, and '
             'Vanuko, hidden renewal traps, data accuracy over discounts, renewal forecasting and churn '
             'reporting, AI-era renewals, and license vs. consultant cost optimization',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators from MetrixData 360, Zylo, Venduris, Vektorindex, Vistack, and SPK and '
                      'Associates agree that SaaS renewals are lost on data and dates, not discounts. '
                      'MetrixData 360 shows a 15% discount masking $1.3 million in overpayment on 3,200 '
                      'inactive Microsoft seats. It also reports that buyers enter renewals at 50 to 60% '
                      'data confidence while vendors sit at 95%. The working mechanics: track the notice '
                      'deadline (renewal date minus notice period), start 120 days out, pull usage at 90, '
                      'benchmark at 60, and send notice or sign at 30. Reported levers include multi-year '
                      'price locks, a Salesforce 9% price cap cut to 3%, 24-to-36-month terms for another '
                      '5 to 10%, and roughly 20% for reference programs. The main split is over '
                      'auto-renewal. One Zylo speaker lets well-priced, fully used apps roll, while '
                      "Vistack and Zylo's negotiator strip the clauses out entirely.",
 'key_metrics': [{'label': 'Buyer vs Vendor Data Confidence at Renewal',
                  'metric': 'Buyer vs Vendor Data Confidence at Renewal',
                  'value': '50-60% buyer data confidence vs 95% vendor confidence',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'MetrixData 360 assessed client data quality going into renewals and found '
                             'most organizations at 50 to 60% confidence. Vendors such as Microsoft and '
                             'SAP build their proposals on data they are 95% confident in.',
                  'source': 'MetrixData 360 ([ViSmcebdPlM @ 00:14:17])'},
                 {'label': 'Overpayment Hidden Behind a 15% Discount',
                  'metric': 'Overpayment Hidden Behind a 15% Discount',
                  'value': '$1.3 million per year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A client held 10,000 E3 seats but needed only 6,800. The 15% discount saved '
                             'about $570,000, while 3,200 inactive licenses cost roughly $1.9 million.',
                  'source': 'MetrixData 360 ([ViSmcebdPlM @ 00:13:36])'},
                 {'label': 'Average SaaS Renewals per Organization per Year',
                  'metric': 'Average SaaS Renewals per Organization per Year',
                  'value': '204 renewals',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Zylo data on its customer base. The same speaker reports that 44% of '
                             'licenses go wasted every month.',
                  'source': 'Zylo ([Os3h9DFeKBU @ 00:00:58])'},
                 {'label': 'Salesforce Annual Price Cap Negotiated Down',
                  'metric': 'Salesforce Annual Price Cap Negotiated Down',
                  'value': '9% cap cut to 3%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Salesforce inserted a 9% yearly price cap into agreements. Zylo's senior "
                             'SaaS services manager negotiated it down to 3% on a live renewal.',
                  'source': 'Zylo ([8wZiGBXdOBo @ 00:23:30])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus - Renewals Are Won on Data, Dates, and '
                          'Owners',
               'paragraphs': ['Every operator here lands on the same verdict: the discount line is the '
                              'least important number on a renewal. Mike of MetrixData 360 walks through a '
                              'client holding 10,000 Microsoft E3 seats that only needed 6,800. '
                              'Procurement banked a 15% discount worth about $570,000 a year, while 3,200 '
                              'inactive contractor, blocked, and stale accounts kept costing roughly $1.9 '
                              'million. The so-called win overpaid by $1.3 million [ViSmcebdPlM @ '
                              '00:13:22]. Venduris makes the same point at smaller scale. The gap between '
                              'paid seats and seats used in the last ninety days is the strongest '
                              'negotiating point you hold, and it does not depend on the vendor agreeing '
                              'with you [saQOnMvtxrQ @ 00:02:04]. Sarah Kraft at SPK and Associates names '
                              'the root failure: treating renewals as an admin task rather than a '
                              'financial decision. That habit means renewing the same licenses year after '
                              'year, with forgotten marketplace apps and over-tiered Microsoft 365 '
                              "editions riding along [Y8SGLxkUJd8 @ 00:02:59]. Zylo's Ben Pimpinger runs "
                              'the same math through a Zoom renewal scenario. Once usage data surfaced 229 '
                              'inactive licenses and 50 downgrade candidates, the buyer covered planned '
                              'new hires without buying a single extra seat [Os3h9DFeKBU @ 00:04:58]. '
                              'Right-size first, haggle second.',
                              'The second point of agreement: the date that costs money is not the renewal '
                              'date. Venduris puts it bluntly. The notice deadline often lands ninety days '
                              "earlier, and missing it means the contract renews on the vendor's terms "
                              '[0W4a6u1-zMQ @ 00:00:00]. Vektorindex splits each renewal into three dates: '
                              'the payment trigger, the notice date, and the decision deadline. It then '
                              'shows what timing does to a $48,000 renewal. Discovered a week before '
                              'payment, the only available action is paying. Discovered 120 days out, '
                              'right-sizing, negotiating, consolidating, and exiting all stay open, '
                              'because a late renewal is a signature, not a negotiation [lR3RrM_hqMg @ '
                              "00:05:54]. Zylo's milestone playbook sends the first stakeholder alert at "
                              '120 days and uses it to read auto-renewal terms and notification periods. '
                              'It starts even earlier for complex core platforms like Salesforce and '
                              'Microsoft [Cm2h-fPMxJ8 @ 00:01:46]. Filippo, founder of Vistack, adds that '
                              'most SaaS contracts carry auto-renewal clauses with 90, 60, or 30 day '
                              'windows. Once the window closes, the contract can legally roll and cannot '
                              'be cancelled for another set period [0I4GdLiHF5Y @ 00:00:53]. For these '
                              'operators, a renewal that surfaces inside its notice window is a forced '
                              'payment rather than a deal.',
                              'Third, renewals slip because nobody owns them and nothing lives in one '
                              'place. Venduris names three causes: contracts scattered across inboxes and '
                              'drives, a signer who has moved on so nobody owns the date, and a tracker '
                              'that holds the renewal date instead of the notice deadline [0W4a6u1-zMQ @ '
                              '00:00:20]. Vektorindex counts up to five distinct roles on every '
                              'subscription: vendor, purchaser, technical owner, budget owner, and '
                              'business owner. A record with none of them is an orphan, meaning software '
                              'with access, credentials, and data that nobody is accountable for. That is '
                              'how zombie subscriptions keep billing after a project ends or a contractor '
                              "leaves [lR3RrM_hqMg @ 00:06:32]. Zylo's Wendy scenario shows the manual "
                              'version. A procurement lead working off a fifteen-row spreadsheet spends '
                              'time hunting down the Zoom app owner and never gets a defensible seat '
                              "count. The lead then renews at the vendor's quoted price and adds users "
                              'just to avoid a per-license increase [Os3h9DFeKBU @ 00:02:53]. Stitchflow '
                              'built its free tracker because IT admins rarely have a single source of '
                              'truth for renewal dates, and spreadsheets lead to missed deadlines and '
                              'unattended auto-renewals [7vly2W7M-Ew @ 00:00:01]. The shared fix is one '
                              'central inventory and one named owner per contract, confirmed again before '
                              'every cycle.'],
               'table': {'caption': 'Where SaaS renewal operators agree: the baseline rules before any '
                                    'pricing conversation',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Operator Move',
                                     'Expert Source'],
                         'rows': [['Right-size seats before chasing any discount',
                                   'A 15% discount saved about $570,000 while 3,200 inactive E3 seats cost '
                                   'nearly $1.9 million',
                                   'Strip inactive, blocked, and stale accounts before opening any pricing '
                                   'talks',
                                   'MetrixData 360 ([ViSmcebdPlM @ 00:13:22])'],
                                  ['The notice deadline is the real decision date',
                                   'The notice deadline often falls ninety days before renewal, and '
                                   'missing it locks in vendor terms',
                                   'Track a notice-deadline column and treat it as the true due date',
                                   'Venduris ([0W4a6u1-zMQ @ 00:00:00])'],
                                  ['A late renewal is a signature, not a deal',
                                   'A $48,000 renewal found one week out leaves payment as the only '
                                   'remaining option',
                                   'Open every material renewal at least 120 days before the payment date',
                                   'Vektorindex ([lR3RrM_hqMg @ 00:05:54])'],
                                  ['The gap between paid and active seats is the strongest lever',
                                   'Compare seats you pay for against people who actually used the tool in '
                                   'ninety days',
                                   'Export usage and present the gap as plain fact the vendor cannot '
                                   'dispute',
                                   'Venduris ([saQOnMvtxrQ @ 00:02:04])'],
                                  ['A centralized inventory prevents missed renewals and overbuying',
                                   'Without central inventory, teams miss renewals, buy too many licenses, '
                                   'or forget to cancel apps',
                                   'Hold contract, usage, and benchmarking data together in one system of '
                                   'record',
                                   'Zylo ([Cm2h-fPMxJ8 @ 00:01:11])'],
                                  ['Every subscription needs a verified named owner',
                                   'Orphaned subscriptions keep billing with live credentials after '
                                   'projects end or contractors leave',
                                   'Assign one named owner per contract and re-ask them on a schedule',
                                   'Vektorindex ([lR3RrM_hqMg @ 00:06:51])'],
                                  ['A renewal is a financial decision, not admin paperwork',
                                   'Companies renew forgotten marketplace apps and over-tiered Microsoft '
                                   '365 editions without checking usage',
                                   'Review what you own and actually use before the renewal quote arrives',
                                   'SPK and Associates ([Y8SGLxkUJd8 @ 00:02:59])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Venduris gives the cleanest build. Use one row per contract with ten '
                              'columns: vendor, owner, annual cost, renewal date, notice period, notice '
                              'deadline, auto-renewal, status, decision, and source document. Pull every '
                              'date from the latest signed order form or amendment, never from an invoice '
                              'or memory [0W4a6u1-zMQ @ 00:00:41]. The core formula is renewal date minus '
                              "notice period. A CRM renewing March 1 on 90 days' notice must be decided by "
                              'December 1, and a contract without auto-renewal uses its end date as the '
                              'decision date. Add a countdown (deadline minus today) and four statuses: '
                              'Missed once passed, Act now under 30 days, Prepare under 90, and On track '
                              'beyond that. Then color-code and sort by deadline so the next decision '
                              'always sits on top [0W4a6u1-zMQ @ 00:01:26]. Each calendar reminder gets a '
                              'job. At 90 days, pull usage and confirm the owner. At 60, decide to renew, '
                              'reduce, renegotiate, or exit. At 30, send notice or sign. A 30-minute '
                              'monthly review backs this up and ends with one number for leadership '
                              "[0W4a6u1-zMQ @ 00:02:09]. Stitchflow's free tool speeds up intake by using "
                              'AI to parse an uploaded contract and autofill renewal dates, cost, and '
                              'license counts. It then sends email reminders and syncs to your calendar '
                              '[7vly2W7M-Ew @ 00:00:17].',
                              'MetrixData 360 treats the data layer as non-negotiable. That means 95% '
                              'inventory coverage across active devices, plus 95% coverage of the '
                              'attributes that drive license math: processors, cores, host-to-guest VM '
                              'relationships, active-passive and clustering status, user and consumption '
                              'data, and current entitlements [ViSmcebdPlM @ 00:19:48]. That data feeds an '
                              'optimized license position, the fewest and lowest-cost licenses that keep '
                              'you compliant. It also flips the negotiation. Without it, you negotiate '
                              "down from the vendor's number; with it, the vendor negotiates up from yours "
                              '[ViSmcebdPlM @ 00:22:21]. For one client, a $7.5 million Microsoft proposal '
                              'backed by a 100-slide vendor deck landed at $5 million. Cross-departmental '
                              'interviews surfaced $2 million in optimization: $500,000 from overlicensed '
                              'SQL Server and $1.5 million from M365 profiling and right-sizing '
                              "[ViSmcebdPlM @ 00:31:30]. Flexera's version runs on connectors. Feed "
                              'discovery from the browser extension, agent API, CASB, and SSO. Add '
                              'Microsoft 365, Entra, and Salesforce connectors with tenant ID, client ID, '
                              'client secret, and domain, then load cost per unit plus purchase, start, '
                              'and end dates. From there, filter subscriptions expiring in the next 60 '
                              'days and export CSV into Power BI for departmental chargeback. The renewal '
                              'then opens on data rather than estimates [2ns7Rlmm4GA @ 00:03:12].',
                              'With a defensible count in hand, the levers come out, and Tori Kagan '
                              'Kikendall of Zylo says to pull several at once. Multi-year terms lock price '
                              'against the 5 to 20% yearly hikes vendors keep pushing, and cap language is '
                              'negotiable. Salesforce recently inserted a 9% annual price cap, which '
                              'Kikendall cut to 3% on a live renewal [8wZiGBXdOBo @ 00:23:30]. Reference '
                              'and case-study programs can be as simple as lending a logo or writing a few '
                              'comments on how the team uses the tool, and they often carry around 20% off '
                              "[8wZiGBXdOBo @ 00:26:31]. Filippo of Vistack works the vendor's calendar. "
                              "Salesforce's fiscal year closes December 31, so year-end renewals pull "
                              'bigger discounts from stressed reps who want to go on holiday and ask their '
                              'managers for deeper cuts. Stretching a 12-month term to 24 or 36 months can '
                              "lock in another 5 to 10% [0I4GdLiHF5Y @ 00:01:46]. Zylo's Ben Pimpinger "
                              'anchors on benchmarks. In the Zoom scenario, benchmarking data on SKU cost '
                              'and overlapping internal apps produced a 10% cost reduction from the '
                              'average price, plus a downgrade and a lower license count [Os3h9DFeKBU @ '
                              '00:05:15]. Kikendall also treats quarter-end and year-end signing as a '
                              'separate lever, one that only exists if the renewal opened early. Pricing '
                              'comes last, after usage has already shrunk the base.'],
               'table': {'caption': 'Renewal mechanics, settings, and numbers operators actually run',
                         'headers': ['Mechanic',
                                     'Exact Numbers or Settings',
                                     'How Operators Run It',
                                     'Expert Source'],
                         'rows': [['Notice deadline formula in the tracker',
                                   "Renewal date minus notice period; a March 1 renewal on 90 days' notice "
                                   'is due December 1',
                                   'Fill the formula down every row; contracts without auto-renewal use '
                                   'their end date',
                                   'Venduris ([0W4a6u1-zMQ @ 00:01:04])'],
                                  ['Countdown status bands',
                                   'Missed, Act now under 30 days, Prepare under 90 days, On track beyond '
                                   'that',
                                   'Color-code, sort by deadline, and keep the next decision on top',
                                   'Venduris ([0W4a6u1-zMQ @ 00:01:26])'],
                                  ['Spreadsheet breaking point',
                                   'Spreadsheets break past roughly 30 contracts, several owners, or a '
                                   'need for usage data beside renewals',
                                   'Move to a renewal platform as soon as any of those thresholds is hit',
                                   'Venduris ([0W4a6u1-zMQ @ 00:02:33])'],
                                  ['Above-the-line renewal triage',
                                   'A $75,000 spend threshold is the suggested starting cutoff for deep '
                                   'renewal work',
                                   'Build full strategy above the line; let well-priced, fully used apps '
                                   'auto-renew',
                                   'Zylo ([Os3h9DFeKBU @ 00:06:06])'],
                                  ['Price cap language in the agreement',
                                   "Salesforce's 9% annual cap was negotiated down to 3% on a live renewal",
                                   'Redline cap language at signature, because those terms persist for '
                                   'many years',
                                   'Zylo ([8wZiGBXdOBo @ 00:23:30])'],
                                  ['Contract term extension',
                                   'Moving from 12 months to 24 or 36 months can lock another 5 to 10% '
                                   'discount',
                                   'Use only for vendors the business is certain to keep long term',
                                   'Vistack ([0I4GdLiHF5Y @ 00:03:49])'],
                                  ['Flat unit price on shrinking quantity',
                                   'Dropping from 50 units to 40 units at the same $50 unit price counts '
                                   'as a win',
                                   'Push for a flat unit price whenever a first-time usage analysis cuts '
                                   'quantities',
                                   'Zylo ([8wZiGBXdOBo @ 00:25:49])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Street-Level Leverage Plays from the Renewal Desk',
                           'body': 'Four moves operators use to shift leverage before and during the '
                                   'renewal conversation.',
                           'items': ['Strip auto-renewal so nothing triggers from the vendor side and the '
                                     'vendor rep has to chase you. If your contract owner leaves without a '
                                     'handover, the vendor must flag the renewal instead of letting it '
                                     'silently roll [Vistack — 0I4GdLiHF5Y @ 00:05:54]',
                                     'Turn annual-upfront payment into a discount pretext. Tell the vendor '
                                     'you are losing margin you could earn by keeping that cash in the '
                                     'bank, and demand 5 to 10% off, or negotiate six-month payment terms '
                                     'instead [Vistack — 0I4GdLiHF5Y @ 00:04:20]',
                                     'Bring leadership in as the bad cop on big-vendor deals. Telling SAP '
                                     'that the big boss says no pulled prices down another 15% [Zylo — '
                                     '8wZiGBXdOBo @ 00:39:01]',
                                     'Audit contractors and so-called decommissioned servers before the '
                                     'count is set. Servers still active on the network are licensable, '
                                     'and contractors who do not act as full-time employees can be '
                                     'licensed differently [MetrixData 360 — ViSmcebdPlM @ 00:16:52]']},
               'sop_steps': [{'step': 1,
                              'title': 'Day 120: Alert Stakeholders and Set Strategy',
                              'action': 'Send the first renewal alert to procurement, business, '
                                        'application, and IT owners, and decide whether to keep, expand, '
                                        'contract, or cancel.',
                              'detail': 'Use the alert to review auto-renewal terms and notification '
                                        'periods so options and deadlines are known. Start earlier than '
                                        '120 days for complex core platforms like Salesforce and Microsoft '
                                        '[Zylo — Cm2h-fPMxJ8 @ 00:01:46]'},
                             {'step': 2,
                              'title': 'Day 90: Pull Usage and Reclaim Seats',
                              'action': 'Review utilization data and run an IT workflow to identify and '
                                        'reclaim underused or unused licenses.',
                              'detail': 'Use the new usage baseline to set the license quantity, then '
                                        'request the renewal order form at that number. Review '
                                        'consolidation and rationalization options at the same time [Zylo '
                                        '— Cm2h-fPMxJ8 @ 00:02:44]'},
                             {'step': 3,
                              'title': 'Day 60: Benchmark and Decide',
                              'action': 'Benchmark the quoted price, then pick one path: renew, reduce, '
                                        'renegotiate, or exit.',
                              'detail': 'If pricing is above benchmark, bring that to the table. If the '
                                        'deal is already good, ask for add-ons such as a sandbox or '
                                        'support credits [Zylo — Cm2h-fPMxJ8 @ 00:03:33]. The 60-day '
                                        'reminder is the decision point [Venduris — 0W4a6u1-zMQ @ '
                                        '00:02:09]'},
                             {'step': 4,
                              'title': 'Day 30 and Close: Send Notice or Sign, Then Log the Win',
                              'action': 'Send notice or sign before the deadline, load the final agreement '
                                        'into the system of record, and track the savings.',
                              'detail': 'After the deadline, the contract renews as-is [Venduris — '
                                        '0W4a6u1-zMQ @ 00:02:09]. Keeping the contract record current '
                                        'makes the next cycle run smoothly, and reporting cumulative '
                                        "savings shows the program's value to executives [Zylo — "
                                        'Cm2h-fPMxJ8 @ 00:04:20]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Auto-renewal is the sharpest split on the renewal desk. Tori Kagan '
                              'Kikendall of Zylo treats the clause as a deal-breaker: review the terms '
                              'before signature, redline every auto-renew clause, and tell the supplier '
                              'those terms are non-negotiable; if the paper is already signed, wire alerts '
                              'that fire 90 and 30 days out so the clause never catches you [8wZiGBXdOBo @ '
                              '00:07:48]. Filippo at Vistack lands in the same camp for a different '
                              'reason, arguing that a contract with no auto-renewal hands you leverage '
                              "because nothing can be triggered from the vendor's side, and it forces the "
                              'rep to chase you when your own contract owner has left without a handover '
                              '[0I4GdLiHF5Y @ 00:05:54]. Ben Pimpinger, also at Zylo, breaks ranks: '
                              'auto-renewals are not always a bad thing, and if you already hold a good '
                              'price with active usage on every license, do not spend time on it and let '
                              'it auto-renew, while noting there are still lots of savings sitting in mid '
                              'and short tail spend [Os3h9DFeKBU @ 00:06:48]. Venduris draws the hard line '
                              'both camps respect: after the notice deadline the contract renews as is, so '
                              'the renew, reduce, renegotiate or exit decision has to land at the 60-day '
                              'reminder, with notice sent or paper signed by 30 [0W4a6u1-zMQ @ 00:02:09].',
                              'The second fault line is whether price benchmarking is the main weapon or '
                              "the last one. Zylo's milestone model makes the benchmark the 60-day "
                              'centerpiece: if your price sits above benchmark, bring that to the '
                              'negotiation table to secure a lower cost, and if you already have a pretty '
                              'good deal, stop haggling over price and ask for add-ons like a sandbox '
                              'account or support credits [Cm2h-fPMxJ8 @ 00:03:50]. Mike at MetrixData 360 '
                              'flips the order entirely, saying a benchmark on discount is probably the '
                              'last thing you should be doing, because the structure of the deal is so '
                              'much more important than the discount, and a negotiated discount keeps '
                              'getting mistaken for a strong outcome [ViSmcebdPlM @ 00:11:05]. Multi-year '
                              "terms split the room the same way. Zylo's Kikendall says sign multi-year to "
                              'lock the price, push back on any built-in percentage increase, and attack '
                              "Salesforce's new 9% annual price cap, which was negotiated down to 3% on "
                              'one recent renewal [8wZiGBXdOBo @ 00:23:09]. UpperEdge counters that vendor '
                              'caps arrive chained to a flat-or-rising spend profile three to five years '
                              'out, so the protection vanishes the moment you try to shrink; the fix is '
                              "making 'no restriction on the spend profile' issue 1B every time you push "
                              'for capped percentages or flat pricing [x34vxEJV40A @ 00:01:11].',
                              'Practitioners also split on when a spreadsheet stops being good enough to '
                              'run renewals and on how early the clock should start ticking. Venduris says '
                              'a spreadsheet works until you pass 30 contracts, several owners, or need '
                              'usage data sitting next to each renewal, and that is the point where '
                              'Venduris takes over, reading the contracts and calculating every notice '
                              'deadline [0W4a6u1-zMQ @ 00:02:33]. Vektorindex defends the spreadsheet as a '
                              'fine audit tool for a small estate, then names the breaking point: multiple '
                              'files, conflicting versions, stale renewal dates, missing owners and no '
                              'history of who changed what, at which point it stops being a control system '
                              'and becomes a place where control goes to decay [lR3RrM_hqMg @ 00:09:22]. '
                              "Zylo's Ben Pimpinger is blunter, calling a spreadsheet the bare minimum and "
                              'telling anyone comfortable with missed renewals, ill-informed decisions and '
                              'money left on the table that it is to each their own [Os3h9DFeKBU @ '
                              "00:07:19]. On lead time, Zylo's renewal milestones open at 120 days with an "
                              'alert to procurement, business application owners and IT owners, but push '
                              'that first step further out for core platforms like Salesforce and '
                              'Microsoft because they are much more complex and take more time to prepare '
                              '[Cm2h-fPMxJ8 @ 00:02:27].'],
               'table': {'caption': 'Competing renewal playbooks side by side, as argued by the '
                                    'practitioners.',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Auto-renew clauses in SaaS agreements',
                                   'Redline every auto-renew clause before signature and declare those '
                                   'terms non-negotiable with the supplier',
                                   'Let it auto-renew when the price is already good and every license '
                                   'shows active usage',
                                   'Zylo | The Leader in Enterprise SaaS Management ([8wZiGBXdOBo @ '
                                   '00:07:48]); Zylo | The Leader in Enterprise SaaS Management '
                                   '([Os3h9DFeKBU @ 00:06:48])'],
                                  ['Role of price benchmarking in the renewal',
                                   'Run the benchmark at 60 days and bring above-benchmark pricing '
                                   'straight to the negotiation table',
                                   'Treat discount benchmarking as the last step; fix deal structure and '
                                   'license counts first',
                                   'Zylo | The Leader in Enterprise SaaS Management ([Cm2h-fPMxJ8 @ '
                                   '00:03:50]); MetrixData 360 ([ViSmcebdPlM @ 00:11:05])'],
                                  ['Multi-year terms and renewal price caps',
                                   'Sign multi-year to lock price and negotiate the Salesforce 9% annual '
                                   'cap down to 3%',
                                   'Strip the flat-or-rising spend-profile restriction vendors attach '
                                   'before trusting any capped percentage',
                                   'Zylo | The Leader in Enterprise SaaS Management ([8wZiGBXdOBo @ '
                                   '00:23:09]); UpperEdge, LLC ([x34vxEJV40A @ 00:01:11])'],
                                  ['Bundles versus buying products piecemeal',
                                   'Evaluate the Atlassian Teamwork Collection instead of buying Jira and '
                                   'Confluence piecemeal for growth',
                                   'Question whether the extra E7 products are needed versus negotiating '
                                   'E5 plus Copilot alone',
                                   'SPK and Associates ([Y8SGLxkUJd8 @ 00:05:23]); MetrixData 360 '
                                   '([ViSmcebdPlM @ 00:12:28])'],
                                  ['Renewal tracking system of record',
                                   'A spreadsheet works for a small estate until you pass roughly 30 '
                                   'contracts',
                                   'A spreadsheet is the bare minimum; run a SaaS management platform with '
                                   'a renewal calendar',
                                   'Venduris ([0W4a6u1-zMQ @ 00:02:33]); Zylo | The Leader in Enterprise '
                                   'SaaS Management ([Os3h9DFeKBU @ 00:07:19])'],
                                  ['How early to open the renewal',
                                   'Standard 120-day alert, pushed further out for complex core platforms '
                                   'like Salesforce and Microsoft',
                                   'Get at enterprise agreements 120 days before, maybe even six or nine '
                                   'months out',
                                   'Zylo | The Leader in Enterprise SaaS Management ([Cm2h-fPMxJ8 @ '
                                   '00:02:27]); MetrixData 360 ([ViSmcebdPlM @ 00:43:21])'],
                                  ['How to read SaaS waste statistics',
                                   'Zylo data shows 44% of licenses wasted every month, equating to $17 '
                                   'million yearly',
                                   'Waste stats from tool sellers are directional; an unused seat is '
                                   'potential optimization, not confirmed waste',
                                   'Zylo | The Leader in Enterprise SaaS Management ([Os3h9DFeKBU @ '
                                   '00:00:38]); Vektorindex ([lR3RrM_hqMg @ 00:03:49])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure on record is winning the discount and losing the '
                              'deal. Mike at MetrixData 360 walked through a customer holding 10,000 '
                              'Microsoft E3 licenses that needed only 6,800; procurement banked a 15% '
                              'discount worth about $570,000 a year, while 3,200 inactive contractor, '
                              'blocked and stale accounts kept costing almost $2 million, so the company '
                              'paid roughly $1.3 million more than necessary and still called it a win '
                              "[ViSmcebdPlM @ 00:13:36]. Zylo's Ben Pimpinger shows the single-app "
                              'version: a procurement lead working off a spreadsheet of 15 upcoming '
                              'renewals received a Zoom price-increase email that would be waived for a '
                              "higher license count, had no data points to leverage, and renewed at Zoom's "
                              'price while adding users [Os3h9DFeKBU @ 00:02:53]. Rerun with a SaaS '
                              'management platform, the same renewal surfaced 229 inactive licenses and 50 '
                              'downgrade candidates, leaving room for incoming hires without buying a '
                              'single extra Zoom seat [Os3h9DFeKBU @ 00:04:58]. Venduris shows the '
                              'small-scale bleed: a contract renewing in February after its notice window '
                              'closed in December over the holidays, landing a new invoice fourteen '
                              'percent higher for forty seats while only twenty people actually used the '
                              'tool [saQOnMvtxrQ @ 00:00:17].',
                              'Missed clocks are the second trap. Venduris names three reasons renewals '
                              'slip: contracts are scattered across inboxes and drives, the person who '
                              'signed has moved on so nobody owns the date, and the tracker holds the '
                              'renewal date instead of the notice deadline that often sits ninety days '
                              'earlier [0W4a6u1-zMQ @ 00:00:20]. Vistack has watched vendors stay quiet '
                              "when a client's contract owner leaves without a handover; nobody from the "
                              'client side reaches out, the contract auto-renews, and the business is '
                              'locked into another 12-month term with a vendor it probably does not need '
                              '[0I4GdLiHF5Y @ 00:06:25]. Vektorindex prices the timing penalty in dollars: '
                              'a $48,000 renewal discovered a week before payment leaves no time to check '
                              'usage, gather evidence, compare alternatives or get approvals, so the only '
                              'available action is paying, whereas 120 days out every option exists, from '
                              'right-sizing and negotiating to consolidation and exit [lR3RrM_hqMg @ '
                              '00:05:54]. The same practitioner traces zombie subscriptions to projects '
                              'that ended, contractors who left and teams that restructured, where no '
                              'process owns the cancellation and the invoice simply keeps arriving; the '
                              'fix is offboarding that covers software, not just laptops [lR3RrM_hqMg @ '
                              '00:06:51].',
                              'Economics checks fail quietly inside the paper itself. UpperEdge says '
                              'renewal caps that look solid usually carry conditions: keep spend flat or '
                              'rising, keep the same products and volumes in the go-forward portfolio, and '
                              'leave percentage-of-net success plans like Premier or Signature unstated in '
                              'the order form; if those conditions remain, the cap is not going to be what '
                              'you think, and your vendor likely knows it [x34vxEJV40A @ 00:04:46]. '
                              'MetrixData 360 found an SAP proposal stuffed with millions in AI licensing '
                              'the client could not use for the first two years; once the over-buying was '
                              'modeled against the commercials, the client was not getting any discount at '
                              'all and was actually overpaying by 10% [ViSmcebdPlM @ 00:36:07]. Cloud '
                              'Trailz flags the budget hole on platforms like Salesforce: the license buys '
                              'access only, the consultant who bends the platform to your process is doing '
                              'real back-end work, and when consulting was never in the budget, the whole '
                              'thing starts to go awry [wMMt_gTxRls @ 00:01:12]. Vektorindex adds '
                              'arithmetic discipline: $99 a month is not $99 a year, so keep monthly '
                              'recurring, annualized, total contract value and one-time charges as four '
                              'separate numbers, or reports misstate commitments in both directions at '
                              'once [lR3RrM_hqMg @ 00:08:43].'],
               'table': {'caption': 'Firsthand renewal failures and the economics check each one exposes.',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Discount negotiated on a bloated seat count',
                                   'Customer took 15% off 10,000 E3 licenses when only 6,800 were needed',
                                   'Discount saved about $570,000 yearly while idle seats cost almost $2 '
                                   'million',
                                   'MetrixData 360 ([ViSmcebdPlM @ 00:13:36])'],
                                  ['Decommissioned servers left live on the network',
                                   'Servers called decommissioned a year earlier were still active in '
                                   'Active Directory',
                                   'Active on the network means licensable, whether or not anyone uses '
                                   'them',
                                   'MetrixData 360 ([ViSmcebdPlM @ 00:16:40])'],
                                  ['Notice window closed over the holidays',
                                   'Contract renewed in February after the December notice window passed '
                                   'unnoticed',
                                   'Invoice came in fourteen percent higher for forty seats with twenty '
                                   'users',
                                   'Venduris ([saQOnMvtxrQ @ 00:00:17])'],
                                  ['Renewal discovered a week before payment',
                                   'A $48,000 renewal surfaced too late to check usage or compare '
                                   'alternatives',
                                   'The only available action was paying; at 120 days every option existed',
                                   'Vektorindex ([lR3RrM_hqMg @ 00:05:54])'],
                                  ['Price cap tied to product lock-in',
                                   'Cap required keeping the same products and volumes in the go-forward '
                                   'portfolio',
                                   'Buyer must keep products or editions it no longer needs to retain the '
                                   'cap',
                                   'UpperEdge, LLC ([x34vxEJV40A @ 00:03:22])'],
                                  ['Forgotten marketplace apps renewed by default',
                                   'Apps bought for one project or team were never reviewed again',
                                   'Renewals treated as an admin task renew licenses nobody checked for '
                                   'usage',
                                   'SPK and Associates ([Y8SGLxkUJd8 @ 00:03:14])'],
                                  ['Downgrade pushed through without usage logic',
                                   'Customer worried about pricing wanted to downgrade ahead of the '
                                   'renewal',
                                   'Usage logic showed the downgrade would trigger overage charges or lost '
                                   'functionality',
                                   '10K ([wI9SWTi8f3E @ 00:01:31])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Signature Renewal Gate',
                           'body': 'Run these four checks on every renewal before any order form gets '
                                   'signed; each one maps to a loss a practitioner has already eaten.',
                           'items': ['Strip inactive, blocked, stale and contractor accounts from the '
                                     'count before negotiating, because even a 0% discount on the right '
                                     'quantity beats a big discount on the wrong one [MetrixData 360 — '
                                     'ViSmcebdPlM @ 00:19:14].',
                                     'Pull every date from the latest signed order form or amendment, '
                                     'never an invoice or memory, and log the notice deadline as renewal '
                                     'date minus notice period [Venduris — 0W4a6u1-zMQ @ 00:00:41].',
                                     'Read every cap for spend-profile, product-lock, changed-metric and '
                                     'renamed-product conditions before counting on the capped percentage '
                                     '[UpperEdge, LLC — x34vxEJV40A @ 00:03:42].',
                                     "Attach usage logs plus an owner's confirmation before anyone touches "
                                     'seat counts, since an unused seat may be a hire starting Monday or a '
                                     'contractual minimum [Vektorindex — lR3RrM_hqMg @ 00:03:49].']}}],
 'pull_quote': '"Instead of paying more to feel safe, we paid less because we were certain." — client '
               'debrief on a $7.5 million Microsoft proposal cut to a $5 million controlled renewal, '
               'relayed by MetrixData 360 (ViSmcebdPlM @ 00:32:06).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Build one row per contract with ten columns (vendor, owner, annual cost, renewal '
                      'date, notice period, notice deadline, auto-renewal, status, decision, source '
                      'document) and compute the notice deadline as renewal date minus notice period '
                      '[Venduris — 0W4a6u1-zMQ @ 00:00:41].',
                      'Before every renewal, compare paid seats with people who used the tool in the last '
                      'ninety days and flag inactive users, underused premium-tier users and duplicate '
                      'workspaces [Venduris — saQOnMvtxrQ @ 00:01:48].',
                      'At 90 days, partner with IT to run a reclaim workflow on underutilized licenses, '
                      'then request the renewal order form on the new usage baseline [Zylo | The Leader in '
                      'Enterprise SaaS Management — Cm2h-fPMxJ8 @ 00:03:03].',
                      'Build an optimized license position from validated data so the vendor negotiates up '
                      'from your number instead of you negotiating down from theirs [MetrixData 360 — '
                      'ViSmcebdPlM @ 00:22:21].',
                      "Time the signature to the supplier's quarter-end or year-end and sign early to "
                      'capture the bigger discount reps chase at period close [Zylo | The Leader in '
                      'Enterprise SaaS Management — 8wZiGBXdOBo @ 00:24:10].',
                      'Offer your logo, a review or a case study in exchange for price, a concession that '
                      'can come with around 20% off [Zylo | The Leader in Enterprise SaaS Management — '
                      '8wZiGBXdOBo @ 00:26:51].'],
 'statutory_citations': [{'title': 'MetrixData 360 — The Renewal Illusion: Why Software Vendor Discounts '
                                   'Matter Less Than Data Accuracy [00:13:01]',
                          'url': 'https://www.youtube.com/watch?v=ViSmcebdPlM&t=781s',
                          'relevance': 'Primary practitioner testimony on the 10,000 versus 6,800 E3 seat '
                                       'case where a 15% discount masked a $1.3 million overpayment.'},
                         {'title': 'UpperEdge, LLC — The Hidden Traps in SaaS Renewals: What Vendors Don’t '
                                   'Want You to Know [00:01:11]',
                          'url': 'https://www.youtube.com/watch?v=x34vxEJV40A&t=71s',
                          'relevance': 'Primary practitioner testimony on spend-profile and product '
                                       'lock-in conditions vendors attach to renewal price caps.'},
                         {'title': 'Venduris — How to Track SaaS Renewals (Free Tracker + Notice Deadline '
                                   'Formula) [00:01:04]',
                          'url': 'https://www.youtube.com/watch?v=0W4a6u1-zMQ&t=64s',
                          'relevance': 'Primary practitioner testimony on the notice deadline formula and '
                                       'the 90/60/30-day reminder cadence.'},
                         {'title': 'Zylo | The Leader in Enterprise SaaS Management — 4 Secrets to SaaS '
                                   'Subscription Renewals [00:07:48]',
                          'url': 'https://www.youtube.com/watch?v=8wZiGBXdOBo&t=468s',
                          'relevance': 'Primary practitioner testimony on redlining auto-renew clauses and '
                                       'negotiating Salesforce price caps from 9% to 3%.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ViSmcebdPlM',
                       'title': 'The Renewal Illusion: Why Software Vendor Discounts Matter Less Than Data '
                                'Accuracy',
                       'channel': 'MetrixData 360',
                       'author': 'MetrixData 360',
                       'text': "Without it you negotiate down from the vendor's number, whereas with this "
                               'the vendor is negotiating up from your number.',
                       'tip': "Without it you negotiate down from the vendor's number, whereas with this "
                              'the vendor is negotiating up from your number.',
                       'timestamp': 1341,
                       'timestamp_seconds': 1341,
                       'timestamp_label': '[00:22:21]',
                       'url': 'https://www.youtube.com/watch?v=ViSmcebdPlM&t=1341s',
                       'markdown': '[00:22:21](https://www.youtube.com/watch?v=ViSmcebdPlM&t=1341s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y8SGLxkUJd8',
                       'title': 'Strategies for Optimizing Software License Costs',
                       'channel': 'SPK and Associates',
                       'author': 'SPK and Associates',
                       'text': 'One of the biggest problems companies make is that they treat software '
                               'renewals as an admin task and not really a financial decision.',
                       'tip': 'One of the biggest problems companies make is that they treat software '
                              'renewals as an admin task and not really a financial decision.',
                       'timestamp': 179,
                       'timestamp_seconds': 179,
                       'timestamp_label': '[00:02:59]',
                       'url': 'https://www.youtube.com/watch?v=Y8SGLxkUJd8&t=179s',
                       'markdown': '[00:02:59](https://www.youtube.com/watch?v=Y8SGLxkUJd8&t=179s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wMMt_gTxRls',
                       'title': 'Salesforce License Cost Vs Consultant Cost: Why Consultants Often Cost '
                                'More Than Licenses',
                       'channel': 'Cloud Trailz',
                       'author': 'Cloud Trailz',
                       'text': 'The license cost is the access, the subscription; consultant cost is for '
                               'someone to come in and do the work to customize it.',
                       'tip': 'The license cost is the access, the subscription; consultant cost is for '
                              'someone to come in and do the work to customize it.',
                       'timestamp': 96,
                       'timestamp_seconds': 96,
                       'timestamp_label': '[00:01:36]',
                       'url': 'https://www.youtube.com/watch?v=wMMt_gTxRls&t=96s',
                       'markdown': '[00:01:36](https://www.youtube.com/watch?v=wMMt_gTxRls&t=96s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x34vxEJV40A',
                       'title': 'The Hidden Traps in SaaS Renewals: What Vendors Don’t Want You to Know',
                       'channel': 'UpperEdge, LLC',
                       'author': 'UpperEdge, LLC',
                       'text': 'When you give me a percentage, I need to have assurances that I can go up '
                               'and down.',
                       'tip': 'When you give me a percentage, I need to have assurances that I can go up '
                              'and down.',
                       'timestamp': 135,
                       'timestamp_seconds': 135,
                       'timestamp_label': '[00:02:15]',
                       'url': 'https://www.youtube.com/watch?v=x34vxEJV40A&t=135s',
                       'markdown': '[00:02:15](https://www.youtube.com/watch?v=x34vxEJV40A&t=135s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2ns7Rlmm4GA',
                       'title': 'SaaS Renewal Management | How to Manage Renewals with SaaS‑Only Vendors | '
                                'Flexera',
                       'channel': 'Flexera | ITAM, FinOps & SaaS Management',
                       'author': 'Flexera | ITAM, FinOps & SaaS Management',
                       'text': 'You can use this data to charge back accurately and go into your next '
                               'vendor renewal with a place of data rather than estimations.',
                       'tip': 'You can use this data to charge back accurately and go into your next '
                              'vendor renewal with a place of data rather than estimations.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=2ns7Rlmm4GA&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=2ns7Rlmm4GA&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0W4a6u1-zMQ',
                       'title': 'How to Track SaaS Renewals (Free Tracker + Notice Deadline Formula)',
                       'channel': 'Venduris',
                       'author': 'Venduris',
                       'text': "A CRM renewing on March 1st, with 90 days' notice, has to be decided by "
                               'December 1st.',
                       'tip': "A CRM renewing on March 1st, with 90 days' notice, has to be decided by "
                              'December 1st.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=0W4a6u1-zMQ&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=0W4a6u1-zMQ&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7vly2W7M-Ew',
                       'title': 'Renewal Tracker - A free tool to organize SaaS contracts, track renewals '
                                '& get auto-reminders',
                       'channel': 'Stitchflow',
                       'author': 'Stitchflow',
                       'text': "It's painful to rely on spreadsheets as it's messy, leading to more grunt "
                               'work, missed deadlines and sometimes unattended auto renewals too.',
                       'tip': "It's painful to rely on spreadsheets as it's messy, leading to more grunt "
                              'work, missed deadlines and sometimes unattended auto renewals too.',
                       'timestamp': 17,
                       'timestamp_seconds': 17,
                       'timestamp_label': '[00:00:17]',
                       'url': 'https://www.youtube.com/watch?v=7vly2W7M-Ew&t=17s',
                       'markdown': '[00:00:17](https://www.youtube.com/watch?v=7vly2W7M-Ew&t=17s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wMnj47JPiwE',
                       'title': 'Using Vanuko for Managing SaaS Software Renewals',
                       'channel': 'Vanuko',
                       'author': 'Vanuko',
                       'text': "Once a quotation has been emailed, the icon turns green and that renewal's "
                               'quoted price is protected.',
                       'tip': "Once a quotation has been emailed, the icon turns green and that renewal's "
                              'quoted price is protected.',
                       'timestamp': 437,
                       'timestamp_seconds': 437,
                       'timestamp_label': '[00:07:17]',
                       'url': 'https://www.youtube.com/watch?v=wMnj47JPiwE&t=437s',
                       'markdown': '[00:07:17](https://www.youtube.com/watch?v=wMnj47JPiwE&t=437s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Os3h9DFeKBU',
                       'title': 'What’s an Effective Strategy to Manage My SaaS Renewals?',
                       'channel': 'Zylo | The Leader in Enterprise SaaS Management',
                       'author': 'Zylo | The Leader in Enterprise SaaS Management',
                       'text': "If you're already getting a good price and have active usage of all of "
                               "your licenses, don't spend time on it and let it auto renew.",
                       'tip': "If you're already getting a good price and have active usage of all of your "
                              "licenses, don't spend time on it and let it auto renew.",
                       'timestamp': 408,
                       'timestamp_seconds': 408,
                       'timestamp_label': '[00:06:48]',
                       'url': 'https://www.youtube.com/watch?v=Os3h9DFeKBU&t=408s',
                       'markdown': '[00:06:48](https://www.youtube.com/watch?v=Os3h9DFeKBU&t=408s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lR3RrM_hqMg',
                       'title': "Is Your SaaS Spend Out of Control? Here's How To Fix It",
                       'channel': 'Vektorindex',
                       'author': 'Vektorindex',
                       'text': 'Rightsize, negotiate, consolidate, even exit. Timing is not '
                               'administration. Timing is leverage.',
                       'tip': 'Rightsize, negotiate, consolidate, even exit. Timing is not administration. '
                              'Timing is leverage.',
                       'timestamp': 373,
                       'timestamp_seconds': 373,
                       'timestamp_label': '[00:06:13]',
                       'url': 'https://www.youtube.com/watch?v=lR3RrM_hqMg&t=373s',
                       'markdown': '[00:06:13](https://www.youtube.com/watch?v=lR3RrM_hqMg&t=373s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0I4GdLiHF5Y',
                       'title': 'Best Strategies to Renew SaaS Contracts',
                       'channel': 'Vistack',
                       'author': 'Vistack',
                       'text': 'Knowing that the fiscal year of Salesforce ends on December 31st gives me '
                               'more power to negotiate my renewal at the end of the year.',
                       'tip': 'Knowing that the fiscal year of Salesforce ends on December 31st gives me '
                              'more power to negotiate my renewal at the end of the year.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=0I4GdLiHF5Y&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=0I4GdLiHF5Y&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OjPZFAoutfA',
                       'title': 'SAAS RENEWALS Report and How to Analyze it',
                       'channel': 'CSM Practice',
                       'author': 'CSM Practice',
                       'text': 'Having the CSM constantly update what is expected to come in brought the '
                               'renewal forecast to an accuracy level of a two percent gap against the '
                               'actual numbers.',
                       'tip': 'Having the CSM constantly update what is expected to come in brought the '
                              'renewal forecast to an accuracy level of a two percent gap against the '
                              'actual numbers.',
                       'timestamp': 466,
                       'timestamp_seconds': 466,
                       'timestamp_label': '[00:07:46]',
                       'url': 'https://www.youtube.com/watch?v=OjPZFAoutfA&t=466s',
                       'markdown': '[00:07:46](https://www.youtube.com/watch?v=OjPZFAoutfA&t=466s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cm2h-fPMxJ8',
                       'title': 'SaaS Renewal Management, Explained',
                       'channel': 'Zylo | The Leader in Enterprise SaaS Management',
                       'author': 'Zylo | The Leader in Enterprise SaaS Management',
                       'text': "If you're already getting a pretty good deal it may not be worth haggling "
                               'over price, but you could consider asking for add-ons like a sandbox '
                               'account or support credits.',
                       'tip': "If you're already getting a pretty good deal it may not be worth haggling "
                              'over price, but you could consider asking for add-ons like a sandbox '
                              'account or support credits.',
                       'timestamp': 245,
                       'timestamp_seconds': 245,
                       'timestamp_label': '[00:04:05]',
                       'url': 'https://www.youtube.com/watch?v=Cm2h-fPMxJ8&t=245s',
                       'markdown': '[00:04:05](https://www.youtube.com/watch?v=Cm2h-fPMxJ8&t=245s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'saQOnMvtxrQ',
                       'title': 'SaaS Contract Management, License Management & Renewal Management '
                                '(Explained)',
                       'channel': 'Venduris',
                       'author': 'Venduris',
                       'text': 'The gap between paid seats and active seats is your strongest negotiating '
                               "point, and it doesn't depend on the vendor agreeing with you.",
                       'tip': 'The gap between paid seats and active seats is your strongest negotiating '
                              "point, and it doesn't depend on the vendor agreeing with you.",
                       'timestamp': 108,
                       'timestamp_seconds': 108,
                       'timestamp_label': '[00:01:48]',
                       'url': 'https://www.youtube.com/watch?v=saQOnMvtxrQ&t=108s',
                       'markdown': '[00:01:48](https://www.youtube.com/watch?v=saQOnMvtxrQ&t=108s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wI9SWTi8f3E',
                       'title': 'The AI Era Is Reshaping SaaS Renewals. Is Your Business Ready?',
                       'channel': '10K',
                       'author': '10K',
                       'text': 'In this case, the logic will determine a downgrade will actually result in '
                               'overage charges or lost functionality.',
                       'tip': 'In this case, the logic will determine a downgrade will actually result in '
                              'overage charges or lost functionality.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=wI9SWTi8f3E&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=wI9SWTi8f3E&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8wZiGBXdOBo',
                       'title': '4 Secrets to SaaS Subscription Renewals',
                       'channel': 'Zylo | The Leader in Enterprise SaaS Management',
                       'author': 'Zylo | The Leader in Enterprise SaaS Management',
                       'text': 'Salesforce just put in a price cap of 9% every year in their agreements; '
                               "that's something you can negotiate lower, and I just negotiated one of "
                               'those and got a 3% price cap.',
                       'tip': 'Salesforce just put in a price cap of 9% every year in their agreements; '
                              "that's something you can negotiate lower, and I just negotiated one of "
                              'those and got a 3% price cap.',
                       'timestamp': 1389,
                       'timestamp_seconds': 1389,
                       'timestamp_label': '[00:23:09]',
                       'url': 'https://www.youtube.com/watch?v=8wZiGBXdOBo&t=1389s',
                       'markdown': '[00:23:09](https://www.youtube.com/watch?v=8wZiGBXdOBo&t=1389s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
