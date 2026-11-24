from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'crm-revenue-attribution-ai-assisted-sales',
 'question_prompt': 'How do we configure the revenue system, evaluate attribution claims, and use AI '
                    'assistance without allowing inaccurate account information to undermine sales?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'CRM, Revenue Attribution, and AI-Assisted Sales',
 'subtitle': 'HubSpot setup and lifecycle stages, Salesforce comparisons and migration considerations, '
             'multi-touch attribution implementations and limitations, attribution software, AI CRM, n8n '
             'outreach, and account-to-proposal fact checking',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators building CRM-driven attribution converge on one rule: pick a model, stay '
                      'consistent, and stop hiding inside blended CAC. Chris Walker ran last touch on a '
                      'nine-day cycle; Milton Anthony of SalesLabX anchors Salesforce on even '
                      'distribution, matches the 180-day influence window to the real cycle, and automates '
                      'campaign membership through hidden UTM campaign-ID fields and Flows. Sarah '
                      'Lane-Hawn rebuilt multi-touch inside HubSpot Pro with seven workflows, 80-some '
                      'fields and 12 baseline channels so board numbers total 100 percent. GrowthSpree '
                      'claims platform data misses 60 to 85 percent of revenue against an 84-day average '
                      'cycle, while Passetto argues attribution itself is part of the problem and should '
                      'be a directional input beneath revenue visibility. CRM pricing, free-tier setup '
                      'mechanics and the AI call-back layer round out the stack, with practitioners split '
                      'on build versus buy and model trust.',
 'key_metrics': [{'label': 'Average B2B Sales Cycle Versus Click Window',
                  'metric': 'Average B2B Sales Cycle Versus Click Window',
                  'value': '84 days; a 30-day click window captures only 5-15% of revenue',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'GrowthSpree argues platform data misses 60-85% of revenue because '
                             'ad-platform windows are far shorter than the B2B buying cycle, and the dark '
                             'funnel is 70% of the journey.',
                  'source': 'GrowthSpree - AI Native B2B Marketing Agency ([fdPFLXFJlwo @ 00:00:18])'},
                 {'label': 'Target Closed-Won Share of Pipeline',
                  'metric': 'Target Closed-Won Share of Pipeline',
                  'value': 'About 30% (51% or 70-80% signals opportunities opened too late)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Milton Anthony uses the closed-won share of pipeline as a health check on '
                             'opportunity-creation discipline inside Salesforce.',
                  'source': 'SalesLabX ([JkmlKUCHcmA @ 00:21:55])'},
                 {'label': 'Goldilocks HubSpot Pro Model Scope',
                  'metric': 'Goldilocks HubSpot Pro Model Scope',
                  'value': '12 baseline channels (26 in one custom build); 7 workflows and 80-some fields',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sarah Lane-Hawn's multi-touch model built for HubSpot Pro, accruing data "
                             'forward with manual backfill, so revenue rolls up to 100%.',
                  'source': 'Value-First ([NZUqq5BtQuU @ 00:14:17])'},
                 {'label': 'Last-Touch Sales Cycle at PatientPop',
                  'metric': 'Last-Touch Sales Cycle at PatientPop',
                  'value': 'About nine days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Chris Walker chose last-touch attribution because the hyper-fast cycle made '
                             'the final interaction a workable proxy for channel efficiency.',
                  'source': 'Chris Walker ([wkcuqfylydw @ 00:01:29])'}],
 'sections': [{'title': 'The Practitioner Consensus: Pick a Model, Discipline the CRM, Treat Credit as '
                        'Directional',
               'paragraphs': ["Chris Walker's PatientPop story sets the baseline every operator here keeps "
                              'returning to: before you obsess over sophistication, stop hiding inside '
                              'blended CAC. Early PatientPop pulled leads from SDR-qualified inbound, '
                              'white paper downloads, channel-partner inbounds and outbound calls, yet '
                              'leadership only saw one blended number and could not tell which channel was '
                              "efficient [wkcuqfylydw @ 00:00:37]. Walker's fix was blunt: they picked "
                              'last touch, stayed consistent, and accepted that a better method might '
                              'exist, because a nine-day sales cycle made the last interaction a fair '
                              'proxy [wkcuqfylydw @ 00:01:29]. That single rule let them split inbound, '
                              'partner, reseller, outbound and self-generated deals and finally compare '
                              'efficiency. Walker even flagged that last touch may not suit every '
                              'business, but the discipline of one rule is what exposed the efficient '
                              'channels. Milton Anthony of SalesLabX lands in the same place from the '
                              'enterprise side, where cycles run past 90 days: turn on every Salesforce '
                              'model, but anchor on even distribution first and only then chase outliers, '
                              'because data-driven is a black box and primary campaign source is myopic '
                              '[JkmlKUCHcmA @ 00:40:31]. Sarah Lane-Hawn adds the board-level reason '
                              'consistency matters: directors want non-squishy numbers that total 100 '
                              'percent, and channel-level influenced revenue that double counts never adds '
                              'up to the real total [NZUqq5BtQuU @ 00:10:58]. Consistency beats cleverness '
                              'across all three.',
                              'The second point of agreement is harsher: attribution software lies by '
                              'omission, so treat it as a directional input, never the scoreboard. '
                              'Passetto opens by telling revenue leaders they are measuring 2026 buyers '
                              'with an early-2000s system, and that switching models flips the answer '
                              'while half the interactions that matter stay untrackable [IYxZQrk554A @ '
                              "00:01:51]. Their 'attribution mirage' is the operator's nightmare: "
                              'podcasts, Slack groups, conferences, LinkedIn and LLM mentions vanish, the '
                              'final organic search gets the credit, and companies then cut the very '
                              'content that drove the deal [IYxZQrk554A @ 00:06:14]. GrowthSpree '
                              'quantifies the blind spot: platform data misses 60 to 85 percent of '
                              'revenue, because a 30-day click window measured against an 84-day average '
                              'B2B cycle captures only 5 to 15 percent, and the dark funnel is 70 percent '
                              'of the journey [fdPFLXFJlwo @ 00:00:18]. Anthony backs the window logic '
                              'inside Salesforce, warning that the default 180-day influence window must '
                              'be matched to your real cycle and that Pardot UTM fields default to first '
                              'touch, so a year-old cookie can steal credit [JkmlKUCHcmA @ 00:37:43]. The '
                              'Value-First host closes the loop: if 90 percent of revenue reads as organic '
                              'while you are spending on events, something is missing [NZUqq5BtQuU @ '
                              '00:30:29].',
                              'Every practitioner agrees the model is worthless without a disciplined CRM '
                              "underneath it. Anthony's three failure points are unconverted leads, "
                              'opportunities without contact roles, and undisciplined opportunity '
                              'creation, and his rule is that marketing must automate campaign membership '
                              'because reps with no economic incentive will never add campaigns by hand '
                              '[JkmlKUCHcmA @ 00:18:25]. Cole Furrh supplies the shared vocabulary that '
                              'makes the data usable: subscriber for newsletter and free-trial forms, lead '
                              'for demo or sales-contact forms, MQL when marketing qualifies, SQL once '
                              'sales deems the lead qualified, and opportunity as the first stage carrying '
                              'a deal value you can optimize ads against [WOpqbZNyqNE @ 00:02:40]. Anthony '
                              'wants those same definitions signed on a one-pager covering MQL, lead, SAL, '
                              'SQL and opportunity, so nobody argues stages mid-quarter [JkmlKUCHcmA @ '
                              '00:24:35]. Envy makes the production-floor case: a CRM is worth nothing '
                              'without the calendar, inbox, phone and call-recording data auto-logged from '
                              'the people actually selling [CTPuSNDPU9Y @ 00:02:35]. Biz Stack School '
                              'applies the same discipline at the smallest scale, only adding a custom '
                              'field if it drives a report, filter or decision, and warning that a deal '
                              'without a next step quietly dies [9qyxUfkZ05c @ 00:13:30]. Skip that '
                              'groundwork and the dashboards simply reflect the mess.'],
               'table': {'caption': 'Where the operators agree: the baseline rules for CRM-driven revenue '
                                    'attribution',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Pick one attribution model and stay consistent with it',
                                   'PatientPop chose last touch on a nine-day cycle and compared every '
                                   'channel',
                                   'Blended CAC hid which inbound, partner and outbound channels were '
                                   'efficient',
                                   'Chris Walker ([wkcuqfylydw @ 00:01:29])'],
                                  ['Start Salesforce attribution with even distribution across all '
                                   'campaigns',
                                   'Turn on every model, anchor on the even split, then examine outliers',
                                   'Data-driven is a black box and primary campaign source is myopic',
                                   'SalesLabX ([JkmlKUCHcmA @ 00:40:31])'],
                                  ['Board-facing revenue numbers must total exactly one hundred percent',
                                   'Build true revenue attribution that rolls up without any double '
                                   'counting',
                                   'Channel-level influenced revenue never adds up to the actual revenue '
                                   'total',
                                   'Value-First ([NZUqq5BtQuU @ 00:10:58])'],
                                  ['Treat attribution as a directional input, never the primary KPI',
                                   'Look for patterns across many signals instead of fighting over '
                                   'sourcing',
                                   'Who-sourced-this-deal fights spark turf wars between SDRs, marketing '
                                   'and partners',
                                   'Passetto ([IYxZQrk554A @ 00:14:06])'],
                                  ['Match lookback windows to the real length of the B2B cycle',
                                   'Use 60 to 180 day windows and optimize campaigns to cost per SQL',
                                   'A 30-day window against an 84-day cycle captures only 5-15 percent',
                                   'GrowthSpree - AI Native B2B Marketing Agency ([fdPFLXFJlwo @ '
                                   '00:04:16])'],
                                  ['Define lifecycle stages as escalating levels of buyer intent',
                                   'Map subscriber, lead, MQL, SQL, opportunity and customer to clear form '
                                   'triggers',
                                   'Opportunity is the first stage with a value to optimize ads against',
                                   'Cole Furrh | B2B SaaS PPC Pro ([WOpqbZNyqNE @ 00:01:50])'],
                                  ['Choose the CRM based on admin capacity before anything else',
                                   'HubSpot for no-admin inbound teams, Salesforce for heavy customization '
                                   'or 50-plus reps',
                                   "Salesforce's flexibility is a liability without someone on staff to "
                                   'own it',
                                   'VerifiedShortlist ([aGsk3Ma7_PA @ 00:04:10])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers: Wiring Credit Into Salesforce and '
                        'HubSpot',
               'paragraphs': ["Anthony's Salesforce build is the most complete wiring diagram any of these "
                              'operators shared. Multi-touch only starts once the record lives in '
                              'Salesforce, and campaigns earn credit when the lead converts to an '
                              'opportunity, because that is where revenue sits [JkmlKUCHcmA @ 00:12:16]. '
                              'Every marketing activity needs a completion action that drops people into a '
                              'campaign, including page actions on a waitlist page and custom redirects '
                              'for case studies; conference kiosk forms he calls an attribution black '
                              'hole. To automate membership, he appends the Salesforce campaign ID to '
                              "UTMs, captures it in a hidden 'SF campaign' form field, and fires a Flow "
                              'that creates the campaign member [JkmlKUCHcmA @ 00:56:16]. Contact-role '
                              'gaps get a scheduled Monday exception report grouped by rep, and a second '
                              'Flow auto-adds same-domain contacts who were campaign members within a 30- '
                              "or 60-day window under an 'automatic addition' role [JkmlKUCHcmA @ "
                              '00:32:14]. His health check: if 51 percent or 70 to 80 percent of pipeline '
                              'is closed-won, opportunities are being opened too late; he targets roughly '
                              '30 percent and refuses auto-created opportunities as technical debt. For '
                              'reporting, he builds the customizable campaign influence report into a '
                              'dashboard with one component per model [JkmlKUCHcmA @ 00:41:46], and Chris '
                              "Walker's channel split shows why the separation pays off [wkcuqfylydw @ "
                              '00:01:43].',
                              "On HubSpot Pro, Sarah Lane-Hawn built a 'Goldilocks' model out of "
                              'frustration with big attribution vendors that left integration gaps and '
                              'double counting [NZUqq5BtQuU @ 00:08:29]. The baseline tracks 12 channels, '
                              'one custom build stretched to 26, and the whole engine runs on seven '
                              'workflows and 80-some fields, mostly custom calculations, accruing data '
                              'forward with manual backfill [NZUqq5BtQuU @ 00:31:28]. Before building, '
                              'they force four decisions: ABM across every contact at the account or '
                              'primary decision-maker only, which channels count, full lifecycle versus '
                              'pre-opportunity-creation view, and build versus buy, with the pitch that '
                              'buying a model once beats a $30,000-a-year cycle. Their sample board '
                              'narrative shows how the output gets used: paid search drove 23 percent of '
                              'revenue on 50 percent of budget, explained by a three-month lag and '
                              'revisited in six months [NZUqq5BtQuU @ 00:18:31]. Enterprise-tier HubSpot '
                              'users can lean on native tools instead; Business Solution notes HubSpot '
                              'offers contact-create, deal-create and revenue attribution with linear, '
                              'U-shaped and W-shaped models, but full multi-touch requires higher tiers '
                              "and quality depends on clean data [gKpbSCZMPqM @ 00:13:22]. Cole Furrh's "
                              'stage map then turns the CRM into ad fuel: once an opportunity carries a '
                              'deal value, campaigns can start optimizing toward conversion value, which '
                              'he calls pipeline [WOpqbZNyqNE @ 00:02:40].',
                              'The stack numbers are concrete. VerifiedShortlist prices HubSpot at free '
                              'for up to two users, Starter $20, Pro $100 plus $1,500 onboarding and '
                              'Enterprise $150 plus $3,500, against Salesforce at Starter $25, Pro $100, '
                              'Enterprise $175, Unlimited $350 and Agentforce 1 $550, with a 30-day trial '
                              "and no free tier [aGsk3Ma7_PA @ 00:02:28]. HubSpot's CPQ add-on runs about "
                              '$84 per seat per month, cross-object reporting is weak, and time to value '
                              'is days to weeks versus weeks to months for Salesforce [aGsk3Ma7_PA @ '
                              '00:03:52]. Biz Stack School shows the free-tier build end to end: email as '
                              "the unique dedupe key, a 'lead source' property on import, CSV stage names "
                              "matched exactly, contacts set to 'update existing only,' and a result of 20 "
                              'deals, 20 associations and 0 errors [9qyxUfkZ05c @ 00:16:51]. The fictional '
                              "roofer's products run from a $199 inspection to a $14,500 full replacement, "
                              'and every logged call gets a follow-up task defaulting to three business '
                              'days. The AI layer bolts on last: Shashank Sharma of Xpedify, on Instantly, '
                              'says the top workflow is a two-minute AI call-back that qualifies the lead '
                              'and updates the CRM, strongest in education, real estate and healthcare, '
                              'but callers drop at 5 to 10 seconds once they detect AI [FOr5YL0hYJE @ '
                              '00:16:44].'],
               'table': {'caption': 'Street pricing and unit economics quoted by the operators for the '
                                    'attribution and CRM stack',
                         'headers': ['Tool or Plan',
                                     'Price or Number Quoted',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['HubSpot Free CRM and Starter tier for small teams',
                                   'Free for up to two users, Starter at $20 per seat',
                                   'No-admin inbound teams going live in days to weeks',
                                   'VerifiedShortlist ([aGsk3Ma7_PA @ 00:01:14])'],
                                  ['Salesforce Enterprise, Unlimited and Agentforce 1 editions',
                                   'Enterprise $175, Unlimited $350, Agentforce 1 $550, no free tier',
                                   'Complex customization or sales floors with more than 50 reps',
                                   'VerifiedShortlist ([aGsk3Ma7_PA @ 00:02:11])'],
                                  ['GrowthSpree attribution agency retainer, self-ranked number one',
                                   '$3,000 per month flat, versus $5-12k at Obility',
                                   'Offline CRM conversion sync and multi-touch for B2B SaaS',
                                   'GrowthSpree - AI Native B2B Marketing Agency ([fdPFLXFJlwo @ '
                                   '00:01:15])'],
                                  ['Thought Metric pixel plus post-purchase survey attribution',
                                   'From $99 per month with a 14-day free trial',
                                   'Blends pixel data with survey ground truth across several models',
                                   'Business Solution ([gKpbSCZMPqM @ 00:04:40])'],
                                  ['ClickMagic link tracking with split tests and bot filtering',
                                   'Pricing plans start at $79 per month, 14-day trial',
                                   'Split testing traffic and filtering bots before crediting conversions',
                                   'Business Solution ([gKpbSCZMPqM @ 00:13:05])'],
                                  ['Xpedify AI CRM first-quarter paid acquisition economics',
                                   '$100 in spend returned $150-200, MRR to CAC above 1',
                                   'Profitability needs six to nine months of customer retention',
                                   'Instantly ([FOr5YL0hYJE @ 00:26:02])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Wiring Moves the Operators Actually Run',
                           'body': 'Small plumbing choices decide whether credit lands on the right '
                                   'campaign or disappears into a black hole.',
                           'items': ['Append the Salesforce campaign ID to every UTM, capture it in a '
                                     "hidden 'SF campaign' form field, and let a Flow create the campaign "
                                     'member so no rep ever touches it [SalesLabX — JkmlKUCHcmA @ '
                                     '00:56:16]',
                                     'Schedule a Monday exception report of opportunities with no contact '
                                     'roles, grouped by rep, and question any $60k-$100k deal carrying a '
                                     'single contact [SalesLabX — JkmlKUCHcmA @ 00:28:18]',
                                     'Audit workflows that auto-move non-deal contacts such as an IT '
                                     'signup to Customer, because they fire false customer conversions in '
                                     'branded and retargeting campaigns [Cole Furrh | B2B SaaS PPC Pro — '
                                     'WOpqbZNyqNE @ 00:03:29]',
                                     'Keep AI outreach emails to 4-7 sentences and test the n8n agent on '
                                     '5-10 leads before switching on full automation [AI Automation '
                                     'Official — bQPaiBg-cWs @ 00:01:20]']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock Stage Definitions',
                              'action': 'Get sales and marketing to sign a one-page definition of MQL, '
                                        'lead, SAL, SQL and opportunity.',
                              'detail': 'Anthony uses a signed one-pager plus monthly KPIs on opportunity '
                                        'creation to stop late opportunities [SalesLabX — JkmlKUCHcmA @ '
                                        '00:24:35]; map each stage to a level of intent, with opportunity '
                                        'as the first stage carrying value [Cole Furrh | B2B SaaS PPC Pro '
                                        '— WOpqbZNyqNE @ 00:01:50].'},
                             {'step': 2,
                              'title': 'Automate Campaign Capture',
                              'action': 'Give every marketing activity a completion action that adds '
                                        'people to a campaign without manual entry.',
                              'detail': 'Use page actions, custom redirects and the hidden SF campaign '
                                        'field feeding a Flow, and stop running any activity until you '
                                        'know how to track it [SalesLabX — JkmlKUCHcmA @ 00:18:25].'},
                             {'step': 3,
                              'title': 'Set Model and Window',
                              'action': 'Turn on all models, anchor on even distribution, and match the '
                                        'lookback window to your real cycle.',
                              'detail': 'Use 60-180 day windows, optimize to cost per SQL and sync CRM '
                                        'data weekly [GrowthSpree - AI Native B2B Marketing Agency — '
                                        'fdPFLXFJlwo @ 00:04:16]; replace the default 180-day influence '
                                        'window if your cycle differs [SalesLabX — JkmlKUCHcmA @ '
                                        '00:37:43].'},
                             {'step': 4,
                              'title': 'Run the Weekly Dashboard Routine',
                              'action': 'Build one dashboard component per model plus deals by stage, and '
                                        'review it every Monday.',
                              'detail': 'Use the customizable campaign influence report for per-model '
                                        'components [SalesLabX — JkmlKUCHcmA @ 00:41:46] and a 10-minute '
                                        'Monday routine on deals by stage and status [Biz Stack School — '
                                        '9qyxUfkZ05c @ 00:35:07].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over which attribution model deserves trust. Chris '
                              'Walker ran early PatientPop on plain last touch because the sales cycle was '
                              'about nine days, and the rule was to pick one model and stay consistent '
                              'rather than chase sophistication, while admitting the team was never super '
                              'confident a better method existed [wkcuqfylydw @ 00:01:29]. Milton Anthony '
                              'of SalesLabX runs the opposite playbook inside Salesforce for cycles past '
                              '90 days: turn every model on, rank primary campaign source dead last as '
                              'myopic, distrust data-driven as a black box, and start from even '
                              'distribution before digging into outliers [JkmlKUCHcmA @ 00:36:46] '
                              '[JkmlKUCHcmA @ 00:40:31]. Sarah Lane-Hawn on Value-First rejects both '
                              'off-the-shelf extremes for HubSpot Pro shops, building a Goldilocks model '
                              'that tracks 12 baseline channels, rolls revenue up to exactly 100 percent, '
                              'and hands the board non-squishy numbers, because channel-level influenced '
                              'revenue never adds up to the total [NZUqq5BtQuU @ 00:10:58]. The operator '
                              'read is simple. Short cycles tolerate a single-touch rule as long as it is '
                              'applied consistently. Long, multi-contact cycles push toward even '
                              'distribution or a custom split that totals cleanly, and the model has to be '
                              'locked before anyone argues about what the output says.',
                              'Practitioners also split on how much weight attribution should carry at '
                              'all. Passetto opens with the hard truth that attribution is more part of '
                              'the problem than the solution, argues that 2026 buyers are being measured '
                              'with an early-2000s system, and demotes attribution to an ancillary, '
                              'directional input rather than the primary KPI [IYxZQrk554A @ 00:00:17]. The '
                              'replacement is revenue visibility: stage progression, bottlenecks, SDR '
                              'follow-up speed and cohorted data that finance can use, which Passetto '
                              'describes as hard to implement but easy to interpret, the exact reverse of '
                              'attribution. Value-First still calls multi-touch absolutely required '
                              'because boards want clean snapshots, yet the host warns against building '
                              'attribution to prove the value of marketing and frames the output as a '
                              'snapshot for board conversations rather than the full picture [NZUqq5BtQuU '
                              '@ 00:22:59]. Chris Walker sits in the pragmatic middle: the payoff of a '
                              'consistent model was simply separating inbound, channel partner, reseller, '
                              'outbound and self-generated deals so channel efficiency could be compared '
                              'at all [wkcuqfylydw @ 00:01:43]. The working playbook blends the camps: use '
                              'attribution to rank channels directionally, then run the stress test '
                              'Passetto closes on, which asks whether you could confidently place an extra '
                              '$1M of budget on what the numbers show [IYxZQrk554A @ 00:17:10].',
                              'Platform choice divides along admin capacity and how much autonomy to hand '
                              "the machines. VerifiedShortlist's rule of thumb is HubSpot when there is no "
                              'admin and the motion is inbound-led, Salesforce for complex customization '
                              "or more than 50 reps, with the blunt warning that Salesforce's flexibility "
                              'is a liability without someone to own it [aGsk3Ma7_PA @ 00:04:10]. Shashank '
                              'Sharma of Xpedify, appearing on Instantly, takes a third path entirely: an '
                              'automation builder with a CRM built in that fills gaps in HubSpot, Zoho and '
                              'Salesforce, using Claude MCP chat to build workflows and dashboards, with '
                              'AI call-backs inside 2 minutes as the top workflow [FOr5YL0hYJE @ '
                              '00:11:32]. On AI sellers, the Outreach CEO interviewed by Chris Bussing '
                              'frames agents as hires with pre-built skills that augment people rather '
                              'than replace them, pointing to 1.5 billion euros of SAP pipeline and 100 '
                              'percent adoption [EQhwdsXidcQ @ 00:01:51]. Ambilio keeps the human firmly '
                              'on the hook instead: every research pin carries a source and date, unknowns '
                              'become discovery questions, and the agent can never make promises on '
                              'discounts or dates [oWWC4Sj-SjA @ 00:06:57]. The practical split is '
                              'augmentation at scale versus tight human sign-off on anything '
                              'customer-facing, and teams pick a side before buying seats.'],
               'table': {'caption': 'Competing Attribution, CRM and AI-Agent Playbooks Side by Side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which attribution model to run day to day',
                                   'Pick last touch once and apply it consistently on a nine-day sales '
                                   'cycle',
                                   'Turn every model on, start with even distribution, then examine the '
                                   'outliers',
                                   'Chris Walker ([wkcuqfylydw @ 00:01:29]); SalesLabX ([JkmlKUCHcmA @ '
                                   '00:40:31])'],
                                  ['How much weight attribution carries in budget decisions',
                                   'Multi-touch is absolutely required because boards want non-squishy '
                                   'numbers totaling 100 percent',
                                   'Attribution is an ancillary directional input while revenue visibility '
                                   'becomes the primary lens',
                                   'Value-First ([NZUqq5BtQuU @ 00:10:58]); Passetto ([IYxZQrk554A @ '
                                   '00:14:06])'],
                                  ['How long the attribution or influence window should be',
                                   'Match the influence window to your sales cycle instead of the 180-day '
                                   'default',
                                   'Use 60 to 180 day windows, optimize to cost per SQL, and sync CRM '
                                   'weekly',
                                   'SalesLabX ([JkmlKUCHcmA @ 00:37:43]); GrowthSpree - AI Native B2B '
                                   'Marketing Agency ([fdPFLXFJlwo @ 00:04:16])'],
                                  ['Build the model, buy software, or hire an agency',
                                   'Buy a HubSpot Pro model once instead of paying into a $30,000 a year '
                                   'cycle',
                                   'Agencies run from $3,000 per month flat up to $15-50k; software starts '
                                   'at $79 or $99 monthly',
                                   'Value-First ([NZUqq5BtQuU @ 00:29:08]); GrowthSpree - AI Native B2B '
                                   'Marketing Agency ([fdPFLXFJlwo @ 00:01:15]); Business Solution '
                                   '([gKpbSCZMPqM @ 00:13:05])'],
                                  ['HubSpot versus Salesforce for a growing sales team',
                                   'HubSpot when there is no admin and an inbound-led motion; live in '
                                   'under four to five weeks',
                                   'Salesforce for complex customization or more than 50 reps, with weeks '
                                   'to months to value',
                                   'VerifiedShortlist ([aGsk3Ma7_PA @ 00:00:00]); Envy - B2B Marketing & '
                                   'RevOps Agency ([CTPuSNDPU9Y @ 00:01:11])'],
                                  ['Where the CRM sits relative to automation tooling',
                                   'Run a mainstream CRM and auto-log calendar, inbox, phone and call '
                                   'transcripts into it',
                                   'Use an automation builder with a CRM built in, driven through Claude '
                                   'MCP chat',
                                   'Envy - B2B Marketing & RevOps Agency ([CTPuSNDPU9Y @ 00:02:17]); '
                                   'Instantly ([FOr5YL0hYJE @ 00:11:32])'],
                                  ['How much autonomy AI sales agents receive',
                                   'Hire agents with pre-built skills to augment reps; SAP reached 100 '
                                   'percent adoption',
                                   'Agent cannot promise discounts or dates, and AI deal scores are '
                                   'prompts, not promises',
                                   'Chris Bussing ([EQhwdsXidcQ @ 00:03:27]); Ambilio ([oWWC4Sj-SjA @ '
                                   '00:06:57]); AI for Every Job ([jorQjadBVYw @ 00:05:40])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive failure is believing the dashboard. Passetto's case is a "
                              '$250M ARR cybersecurity company that poured millions into paid-search free '
                              'trials and got horrible win rates, low-value deals and negligible pipeline; '
                              'the same attribution mirage hides podcasts, Slack, conferences, LinkedIn '
                              'and LLM mentions, hands all the credit to the final organic search, and '
                              'pushes companies to cut content in downturns [IYxZQrk554A @ 00:04:32]. '
                              'GrowthSpree puts numbers on the blind spot: platform data misses 60 to 85 '
                              'percent of revenue, and a 30-day click window against an 84-day average B2B '
                              'sales cycle captures only 5 to 15 percent of it [fdPFLXFJlwo @ 00:00:18]. '
                              'Inside Salesforce, SalesLabX finds Pardot UTM fields are first-touch by '
                              'default, so a cookie from a year earlier walks off with the credit, while '
                              'blank UTM fields are not automatically errors because ad spend has been '
                              'seen lifting organic traffic [JkmlKUCHcmA @ 00:09:31]. Value-First supplies '
                              'the sanity check for the inverse distortion: if 90 percent of revenue shows '
                              'as organic while real money is going into events, something is missing from '
                              'the model [NZUqq5BtQuU @ 00:30:29]. Every one of these traps looks like '
                              'clean data until someone asks where the deals actually came from.',
                              'Record hygiene is where pipelines quietly break. SalesLabX names three '
                              'failure points: leads never converted, opportunities without contact roles, '
                              'and undisciplined opportunity creation, where 51 percent or 70 to 80 '
                              'percent of pipeline showing closed-won means opportunities are opened too '
                              'late against a target of about 30 percent [JkmlKUCHcmA @ 00:21:55]. The '
                              'same firm finds that reps with no economic incentive simply will not add '
                              'campaign members, so campaign membership has to be automated, and kiosk '
                              'forms at conferences turn into an attribution black hole [JkmlKUCHcmA @ '
                              '00:03:21]. Cole Furrh flags a HubSpot-specific trap: workflows that '
                              'auto-move non-deal contacts, such as an IT signup, to the Customer stage '
                              'fire false customer conversions, worst in branded and retargeting campaigns '
                              "[WOpqbZNyqNE @ 00:03:29]. Biz Stack School's beginner build exposes the "
                              'import-level traps: CSV stage names that do not match exactly are the '
                              'number one reason deal imports fail, custom fields should exist only if '
                              'they feed a report, filter or decision, and a deal without a next step '
                              'quietly dies [9qyxUfkZ05c @ 00:16:29]. The pattern across all four warnings '
                              'is that bad attribution usually starts life as bad data entry, not as a bad '
                              'model.',
                              'AI tooling and startup economics produce their own firsthand reversals. '
                              'Shashank Sharma reports that voice AI callers drop off at 5 to 10 seconds '
                              'once they detect a bot, with value only arriving on calls that run past 20 '
                              'to 30 seconds; the first 100 customers came from Meta ads testing 7 to 8 '
                              'propositions but retention was low, the team shrank from 70 people to 33, '
                              'and adopting MCP too late lost clients [FOr5YL0hYJE @ 00:19:44] '
                              '[FOr5YL0hYJE @ 00:30:36]. The economics check is blunt: first-quarter MRR '
                              'to CAC above 1, with $100 of spend returning $150 to $200, yet '
                              "profitability still needs 6 to 9 months of retention. Ambilio's near-miss "
                              'shows what an unchecked agent costs in a proposal: a plan sized at 14 sites '
                              'instead of 11 would have gone out 27 percent overpriced, and agent errors '
                              'fall into four types, stale, overstated, wrong entity and unsupported '
                              '[oWWC4Sj-SjA @ 00:04:11]. VerifiedShortlist adds the buying-side trap: '
                              'under-resourcing the rollout is the top regret after picking a CRM, and '
                              'over-buying for a 60-rep future burns seat budget [aGsk3Ma7_PA @ 00:03:52]. '
                              'The remedy every one of these operators repeats is a human check before '
                              'anything reaches a customer or a forecast.'],
               'table': {'caption': 'Firsthand Failure Modes and the Economics Behind Them',
                         'headers': ['Failure Mode',
                                     'What Happened',
                                     'Economics Check or Fix',
                                     'Expert Source'],
                         'rows': [['Blended CAC hiding which channels actually work',
                                   'Team only looked at blended CAC and could not tell which channels were '
                                   'efficient',
                                   'Split inbound, partner, reseller, outbound and self-generated deals, '
                                   'then compare channel efficiency',
                                   'Chris Walker ([wkcuqfylydw @ 00:02:01])'],
                                  ['Paid-search free trials credited by last-click attribution',
                                   'A $250M ARR cybersecurity firm spent millions on paid-search free '
                                   'trials',
                                   'Horrible win rates, low-value deals, negligible pipeline; ask whether '
                                   'you would place another $1M',
                                   'Passetto ([IYxZQrk554A @ 00:04:32])'],
                                  ['Click window far shorter than the real sales cycle',
                                   'A 30-day click window against an 84-day cycle captures only 5 to 15 '
                                   'percent',
                                   'Move to 60 to 180 day windows and optimize campaigns to cost per SQL',
                                   'GrowthSpree - AI Native B2B Marketing Agency ([fdPFLXFJlwo @ '
                                   '00:00:18])'],
                                  ['Opportunities created too late in the funnel',
                                   '51 percent or 70 to 80 percent of pipeline already closed-won at '
                                   'creation',
                                   'Target about 30 percent with a signed one-pager defining MQL through '
                                   'opportunity',
                                   'SalesLabX ([JkmlKUCHcmA @ 00:21:55])'],
                                  ['False customer conversions feeding ad platforms',
                                   'Workflows auto-move IT signups and other non-deal contacts to the '
                                   'Customer stage',
                                   'Audit lifecycle workflows, especially those touching branded and '
                                   'retargeting campaigns',
                                   'Cole Furrh | B2B SaaS PPC Pro ([WOpqbZNyqNE @ 00:03:29])'],
                                  ['AI research agent mis-sizing a customer proposal',
                                   'Proposal plan sized at 14 sites instead of the real 11',
                                   'Would have shipped 27 percent overpriced; quote the exact source line '
                                   'for every claim',
                                   'Ambilio ([oWWC4Sj-SjA @ 00:04:11])'],
                                  ['Voice AI callers hanging up early on call-backs',
                                   'Callers drop at 5 to 10 seconds once they detect they are talking to '
                                   'AI',
                                   'Value only arrives past 20 to 30 seconds; MRR to CAC above 1 still '
                                   'needs 6-9 months retention',
                                   'Instantly ([FOr5YL0hYJE @ 00:19:44])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Trusting the Pipeline Number',
                           'body': 'Run these checks before any attribution report or AI-drafted proposal '
                                   'reaches a board, a budget meeting or a customer.',
                           'items': ['Run a Monday exception report of opportunities with no contact '
                                     'roles, grouped by rep, and challenge any $60k-$100k deal carrying a '
                                     'single contact [SalesLabX — JkmlKUCHcmA @ 00:28:18].',
                                     'If 90 percent of revenue shows as organic while you are spending on '
                                     'events, find the missing channel before presenting the numbers '
                                     '[Value-First — NZUqq5BtQuU @ 00:30:29].',
                                     'Audit every HubSpot workflow that sets lifecycle stage to Customer '
                                     'so non-deal signups never fire as customer conversions [Cole Furrh | '
                                     'B2B SaaS PPC Pro — WOpqbZNyqNE @ 00:03:29].',
                                     'No agent-drafted proposal ships until site counts, entities and '
                                     'dates are checked against a quoted source line, and the agent never '
                                     'promises discounts or dates [Ambilio — oWWC4Sj-SjA @ 00:06:57].']}}],
 'pull_quote': '"The hard truth is that attribution is more part of the problem than the actual solution." '
               '— Passetto (IYxZQrk554A @ 00:00:17)',
 'diagram_id': 'diag-06',
 'action_checklist': ['Pick one attribution model and stay consistent; on a nine-day sales cycle, last '
                      'touch was enough to separate channels [Chris Walker — wkcuqfylydw @ 00:01:12].',
                      'Add the Salesforce campaign ID to UTMs, capture it in a hidden SF campaign form '
                      'field, and let a Flow create the campaign member [SalesLabX — JkmlKUCHcmA @ '
                      '00:56:16].',
                      'Set the campaign influence window to match your actual sales cycle instead of '
                      'leaving the 180-day default [SalesLabX — JkmlKUCHcmA @ 00:37:43].',
                      'Before building, decide ABM or primary decision-maker only, which channels, full '
                      'lifecycle or pre-opportunity, then build versus buy [Value-First — NZUqq5BtQuU @ '
                      '00:37:01].',
                      'Start optimizing campaigns for conversion value at the Opportunity stage, the first '
                      'lifecycle stage carrying a deal value [Cole Furrh | B2B SaaS PPC Pro — WOpqbZNyqNE '
                      '@ 00:02:40].',
                      'Keep AI outreach emails to 4 to 7 sentences and test on 5 to 10 leads before '
                      'automating the send [AI Automation Official — bQPaiBg-cWs @ 00:01:20].'],
 'statutory_citations': [{'title': 'Passetto — Attribution for SaaS Marketing: What Actually Works (And '
                                   "What Doesn't) [00:00:17]",
                          'url': 'https://www.youtube.com/watch?v=IYxZQrk554A&t=17s',
                          'relevance': 'Primary practitioner testimony on attribution as a directional '
                                       'input versus revenue visibility.'},
                         {'title': 'SalesLabX — SalesLabX Webinar: Salesforce Multi Touch Attribution '
                                   '[00:21:55]',
                          'url': 'https://www.youtube.com/watch?v=JkmlKUCHcmA&t=1315s',
                          'relevance': 'Primary practitioner testimony on unconverted leads, missing '
                                       'contact roles and late opportunity creation.'},
                         {'title': "Value-First — Let's Build Multi-Touch Attribution in HubSpot with "
                                   'Sarah Lane-Hawn [00:10:58]',
                          'url': 'https://www.youtube.com/watch?v=NZUqq5BtQuU&t=658s',
                          'relevance': 'Primary practitioner testimony on board-ready multi-touch models '
                                       'that total 100 percent.'},
                         {'title': 'Ambilio — AI Agents in Sales: From Account Research to Proposal (and '
                                   'the One Check That Saves the Deal) [00:04:11]',
                          'url': 'https://www.youtube.com/watch?v=oWWC4Sj-SjA&t=251s',
                          'relevance': 'Primary practitioner testimony on AI agent proposal errors and the '
                                       'source-check habit.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'wkcuqfylydw',
                       'title': 'How to Measure Multi-Touch Attribution Across Sales and Marketing Teams',
                       'channel': 'Chris Walker',
                       'author': 'Chris Walker',
                       'text': 'We chose last touch attribution so whatever happened last before the '
                               'customer made the purchase, our sales cycle is about nine days so hyper '
                               'fast.',
                       'tip': 'We chose last touch attribution so whatever happened last before the '
                              'customer made the purchase, our sales cycle is about nine days so hyper '
                              'fast.',
                       'timestamp': 89,
                       'timestamp_seconds': 89,
                       'timestamp_label': '[00:01:29]',
                       'url': 'https://www.youtube.com/watch?v=wkcuqfylydw&t=89s',
                       'markdown': '[00:01:29](https://www.youtube.com/watch?v=wkcuqfylydw&t=89s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JkmlKUCHcmA',
                       'title': 'SalesLabX Webinar: Salesforce Multi Touch Attribution',
                       'channel': 'SalesLabX',
                       'author': 'SalesLabX',
                       'text': "This is marketing's responsibility, and this should be automated; don't "
                               'depend on anyone adding campaign members or anybody to campaigns manually.',
                       'tip': "This is marketing's responsibility, and this should be automated; don't "
                              'depend on anyone adding campaign members or anybody to campaigns manually.',
                       'timestamp': 1105,
                       'timestamp_seconds': 1105,
                       'timestamp_label': '[00:18:25]',
                       'url': 'https://www.youtube.com/watch?v=JkmlKUCHcmA&t=1105s',
                       'markdown': '[00:18:25](https://www.youtube.com/watch?v=JkmlKUCHcmA&t=1105s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NZUqq5BtQuU',
                       'title': "Let's Build Multi-Touch Attribution in HubSpot with Sarah Lane-Hawn",
                       'channel': 'Value-First',
                       'author': 'Value-First',
                       'text': 'The number one thing to give to your board is non-squishy numbers; we need '
                               'something that totals 100 percent.',
                       'tip': 'The number one thing to give to your board is non-squishy numbers; we need '
                              'something that totals 100 percent.',
                       'timestamp': 658,
                       'timestamp_seconds': 658,
                       'timestamp_label': '[00:10:58]',
                       'url': 'https://www.youtube.com/watch?v=NZUqq5BtQuU&t=658s',
                       'markdown': '[00:10:58](https://www.youtube.com/watch?v=NZUqq5BtQuU&t=658s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IYxZQrk554A',
                       'title': "Attribution for SaaS Marketing: What Actually Works (And What Doesn't)",
                       'channel': 'Passetto',
                       'author': 'Passetto',
                       'text': 'The hard truth is that attribution is more part of the problem than the '
                               'actual solution.',
                       'tip': 'The hard truth is that attribution is more part of the problem than the '
                              'actual solution.',
                       'timestamp': 17,
                       'timestamp_seconds': 17,
                       'timestamp_label': '[00:00:17]',
                       'url': 'https://www.youtube.com/watch?v=IYxZQrk554A&t=17s',
                       'markdown': '[00:00:17](https://www.youtube.com/watch?v=IYxZQrk554A&t=17s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fdPFLXFJlwo',
                       'title': '6 Best Revenue Attribution Agencies for B2B SaaS in 2026',
                       'channel': 'GrowthSpree - AI Native B2B Marketing Agency',
                       'author': 'GrowthSpree - AI Native B2B Marketing Agency',
                       'text': 'The average B2B sales cycle is 84 days.',
                       'tip': 'The average B2B sales cycle is 84 days.',
                       'timestamp': 18,
                       'timestamp_seconds': 18,
                       'timestamp_label': '[00:00:18]',
                       'url': 'https://www.youtube.com/watch?v=fdPFLXFJlwo&t=18s',
                       'markdown': '[00:00:18](https://www.youtube.com/watch?v=fdPFLXFJlwo&t=18s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gKpbSCZMPqM',
                       'title': '9 Best Marketing Attribution Software for 2027 (Full Demo & Comparison)',
                       'channel': 'Business Solution',
                       'author': 'Business Solution',
                       'text': 'Pricing plans start at $79 per month.',
                       'tip': 'Pricing plans start at $79 per month.',
                       'timestamp': 785,
                       'timestamp_seconds': 785,
                       'timestamp_label': '[00:13:05]',
                       'url': 'https://www.youtube.com/watch?v=gKpbSCZMPqM&t=785s',
                       'markdown': '[00:13:05](https://www.youtube.com/watch?v=gKpbSCZMPqM&t=785s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WOpqbZNyqNE',
                       'title': 'Defining different HubSpot lifecycle stages + how to use them in ad '
                                'campaigns',
                       'channel': 'Cole Furrh | B2B SaaS PPC Pro',
                       'author': 'Cole Furrh | B2B SaaS PPC Pro',
                       'text': 'The important thing to note for marketing and conversion optimization '
                               'purposes about opportunity is this is the first stage where you have a '
                               'value associated with the lead.',
                       'tip': 'The important thing to note for marketing and conversion optimization '
                              'purposes about opportunity is this is the first stage where you have a '
                              'value associated with the lead.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=WOpqbZNyqNE&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=WOpqbZNyqNE&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9qyxUfkZ05c',
                       'title': 'HubSpot CRM Tutorial for Beginners (2026) – Full Free Setup',
                       'channel': 'Biz Stack School',
                       'author': 'Biz Stack School',
                       'text': 'This is the number one reason deal imports fail.',
                       'tip': 'This is the number one reason deal imports fail.',
                       'timestamp': 989,
                       'timestamp_seconds': 989,
                       'timestamp_label': '[00:16:29]',
                       'url': 'https://www.youtube.com/watch?v=9qyxUfkZ05c&t=989s',
                       'markdown': '[00:16:29](https://www.youtube.com/watch?v=9qyxUfkZ05c&t=989s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9qyxUfkZ05c',
                       'title': 'HubSpot CRM Tutorial for Beginners (2026) – Full Free Setup',
                       'channel': 'Biz Stack School',
                       'author': 'Biz Stack School',
                       'text': 'A deal without a next step is a deal that quietly dies.',
                       'tip': 'A deal without a next step is a deal that quietly dies.',
                       'timestamp': 1492,
                       'timestamp_seconds': 1492,
                       'timestamp_label': '[00:24:52]',
                       'url': 'https://www.youtube.com/watch?v=9qyxUfkZ05c&t=1492s',
                       'markdown': '[00:24:52](https://www.youtube.com/watch?v=9qyxUfkZ05c&t=1492s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aGsk3Ma7_PA',
                       'title': 'HubSpot vs Salesforce 2027: Which CRM for SaaS Startups?',
                       'channel': 'VerifiedShortlist',
                       'author': 'VerifiedShortlist',
                       'text': "Salesforce's flexibility is a liability without someone to own it.",
                       'tip': "Salesforce's flexibility is a liability without someone to own it.",
                       'timestamp': 250,
                       'timestamp_seconds': 250,
                       'timestamp_label': '[00:04:10]',
                       'url': 'https://www.youtube.com/watch?v=aGsk3Ma7_PA&t=250s',
                       'markdown': '[00:04:10](https://www.youtube.com/watch?v=aGsk3Ma7_PA&t=250s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yVBDmC1qx5E',
                       'title': 'HubSpot Review—Best CRM Software for Enterprises in 2026!',
                       'channel': 'CRM Central',
                       'author': 'CRM Central',
                       'text': 'Forecasting is weighted by engagement rather than a flat 50 percent stage '
                               'probability.',
                       'tip': 'Forecasting is weighted by engagement rather than a flat 50 percent stage '
                              'probability.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=yVBDmC1qx5E&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=yVBDmC1qx5E&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CTPuSNDPU9Y',
                       'title': 'Why More Companies Are Leaving Salesforce for HubSpot CRM, And Why You '
                                'Should Too 🤔 Marketing Envy',
                       'channel': 'Envy - B2B Marketing & RevOps Agency',
                       'author': 'Envy - B2B Marketing & RevOps Agency',
                       'text': 'A CRM is worth nothing without the data coming in from the production '
                               'floor.',
                       'tip': 'A CRM is worth nothing without the data coming in from the production '
                              'floor.',
                       'timestamp': 155,
                       'timestamp_seconds': 155,
                       'timestamp_label': '[00:02:35]',
                       'url': 'https://www.youtube.com/watch?v=CTPuSNDPU9Y&t=155s',
                       'markdown': '[00:02:35](https://www.youtube.com/watch?v=CTPuSNDPU9Y&t=155s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FOr5YL0hYJE',
                       'title': 'The AI CRM Killing Salesforce & HubSpot',
                       'channel': 'Instantly',
                       'author': 'Instantly',
                       'text': 'Drop-offs happen at 5 to 10 seconds once callers detect AI, and calls '
                               'lasting more than 20 to 30 seconds are where the value comes from.',
                       'tip': 'Drop-offs happen at 5 to 10 seconds once callers detect AI, and calls '
                              'lasting more than 20 to 30 seconds are where the value comes from.',
                       'timestamp': 1184,
                       'timestamp_seconds': 1184,
                       'timestamp_label': '[00:19:44]',
                       'url': 'https://www.youtube.com/watch?v=FOr5YL0hYJE&t=1184s',
                       'markdown': '[00:19:44](https://www.youtube.com/watch?v=FOr5YL0hYJE&t=1184s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EQhwdsXidcQ',
                       'title': '$4.4B Outreach CEO: The Future of Sales Is AI Agents',
                       'channel': 'Chris Bussing',
                       'author': 'Chris Bussing',
                       'text': 'Hire agents with pre-built skills to augment your people, not replace '
                               'them.',
                       'tip': 'Hire agents with pre-built skills to augment your people, not replace them.',
                       'timestamp': 111,
                       'timestamp_seconds': 111,
                       'timestamp_label': '[00:01:51]',
                       'url': 'https://www.youtube.com/watch?v=EQhwdsXidcQ&t=111s',
                       'markdown': '[00:01:51](https://www.youtube.com/watch?v=EQhwdsXidcQ&t=111s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oWWC4Sj-SjA',
                       'title': 'AI Agents in Sales: From Account Research to Proposal (and the One Check '
                                'That Saves the Deal)',
                       'channel': 'Ambilio',
                       'author': 'Ambilio',
                       'text': 'A question shows you did your homework.',
                       'tip': 'A question shows you did your homework.',
                       'timestamp': 379,
                       'timestamp_seconds': 379,
                       'timestamp_label': '[00:06:19]',
                       'url': 'https://www.youtube.com/watch?v=oWWC4Sj-SjA&t=379s',
                       'markdown': '[00:06:19](https://www.youtube.com/watch?v=oWWC4Sj-SjA&t=379s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bQPaiBg-cWs',
                       'title': 'How to Build an Email Outreach AI Agent in n8n',
                       'channel': 'AI Automation Official',
                       'author': 'AI Automation Official',
                       'text': 'Good outreach emails are short.',
                       'tip': 'Good outreach emails are short.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=bQPaiBg-cWs&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=bQPaiBg-cWs&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jorQjadBVYw',
                       'title': 'AI for Salespeople in 2026: Account Research, Outreach, Discovery Calls '
                                'and Forecasts',
                       'channel': 'AI for Every Job',
                       'author': 'AI for Every Job',
                       'text': 'An AI score is an estimate, only as good as the data behind it.',
                       'tip': 'An AI score is an estimate, only as good as the data behind it.',
                       'timestamp': 340,
                       'timestamp_seconds': 340,
                       'timestamp_label': '[00:05:40]',
                       'url': 'https://www.youtube.com/watch?v=jorQjadBVYw&t=340s',
                       'markdown': '[00:05:40](https://www.youtube.com/watch?v=jorQjadBVYw&t=340s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
