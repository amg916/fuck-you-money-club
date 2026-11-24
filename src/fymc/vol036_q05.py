from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'finops-and-repatriation-controlling-cloud-and-ai-compute-spend',
 'question_prompt': 'How do teams control cloud and AI spend, and when does bare metal or owning hardware '
                    'beat hyperscaler bills?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'FinOps and Repatriation: Controlling Cloud and AI Compute Spend',
 'subtitle': "AWS FinOps basics, CapEx vs OpEx and rightsizing, RI and savings-plan benchmarking, Amazon's "
             'internal cost lessons, FinOps+ at re:Invent, building a FinOps agent, agentic AI FinOps on '
             'Azure, AI budgets under tokenmaxxing, AI subscriptions vs owning an H100, $500 Epyc servers, '
             'and the $200 box vs $4,000 cloud bill',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from AWS, Vantage, ProsperOps, Kion and the FinOps Foundation '
                      'converge on one sequence: hourly resource-level visibility, engineer ownership, '
                      'policy-driven automation, then commitment and model-routing discipline. ProsperOps '
                      'benchmarks average Effective Savings Rate at 10.5% against a 98th percentile near '
                      '40.5%, and its automation engine posts a 47% blended discount at over 98% coverage. '
                      'Intellipaat pegs on-demand at two or three times committed rates. AI tokens now '
                      'dominate the agenda: GenAI tops budget-overrun causes, FinOps X attendees spend 80% '
                      'of their time on AI, and Vantage streams invocation logs because AWS billing lags '
                      'seven to eight hours. The split comes on autonomy versus oversight and on '
                      'repatriation: Nick Gioftsos champions a $200 box over a $4,000 cloud bill, while '
                      'Caleb Writes Code finds a $200 subscription beats owning an H100.',
 'key_metrics': [{'label': 'Average Effective Savings Rate on AWS Compute',
                  'metric': 'Average Effective Savings Rate on AWS Compute',
                  'value': '10.5% average; 75th percentile in the low 20s; 98th percentile about 40.5%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'ProsperOps benchmark across more than 1,400 data points with up to $2M per '
                             'month in compute spend, measuring outcome-based savings from RIs and Savings '
                             'Plans.',
                  'source': 'ProsperOps, a Flexera company ([KW_LS_stgvc @ 00:03:35])'},
                 {'label': 'On-Demand Premium Over Long-Term Commitment',
                  'metric': 'On-Demand Premium Over Long-Term Commitment',
                  'value': 'Two or three times more expensive',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Intellipaat's comparison of on-demand pricing against long-term commitment "
                             'rates, used to argue that a central team should own rate negotiation.',
                  'source': 'Intellipaat ([7_L1_3-4kg8 @ 00:22:10])'},
                 {'label': 'Share of FinOps Time Spent on AI Spend',
                  'metric': 'Share of FinOps Time Spent on AI Spend',
                  'value': '80% of time',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'FinOps X attendees reporting how much of their working time now goes to AI '
                             'spend, alongside GenAI ranking as the top cause of budget overruns greater '
                             'than 10%.',
                  'source': 'Vantage ([N1u_6ENlZV4 @ 00:16:54])'},
                 {'label': 'Self-Hosted DGX H100 Break-Even',
                  'metric': 'Self-Hosted DGX H100 Break-Even',
                  'value': 'About $400K total cost of ownership; 28 users to break even',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Caleb Writes Code's math for hosting a frontier model on a $285K-300K DGX "
                             'H100 versus paying $200 per month per subscription seat.',
                  'source': 'Caleb Writes Code ([SmYNK0kqaDI @ 00:05:08])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator who spoke on this starts in the same place: you cannot cut '
                              'what you cannot see. AWS With A Beer frames FinOps as a financial guard '
                              'rail that forces engineering, finance and leadership into one room, and '
                              'names lack of visibility, zombie instances, tangled pricing on data '
                              'transfer and reserved instances, and organizational silos as the core leaks '
                              '[6qqv9Ss3MaE @ 00:01:50]. Intellipaat pushes ownership down to the people '
                              'launching the servers: finance experts will not fully understand ECS or '
                              'Lambda versus EC2 choices, so developers must justify spend against '
                              'business value and own the bill [7_L1_3-4kg8 @ 00:07:24]. Nathan Perry of '
                              'the AWS OPTICS team describes how Amazon itself moved from monthly, '
                              'account-level data to hourly, ARN-level grain using CUR and Data Exports, '
                              'then democratized Cost Explorer to every team rather than hoarding it '
                              'inside a central group [tPYmvdc5oE0 @ 00:02:17]. Rem at Vantage lays out '
                              'the same sequence for AI spend: visibility, then allocation, then value '
                              'measurement, then budgets and guardrails, in that order [1-lJfz3oQ2w @ '
                              '00:08:02]. The shared lesson is blunt. Get granular data into the hands of '
                              'whoever controls the resource, attach a business owner to every dollar, and '
                              'only then start cutting.',
                              'Rate optimization is the second point of agreement, and the numbers are '
                              'loud. Intellipaat puts on-demand pricing at two or three times the cost of '
                              'long-term commitment and argues a central team should own rate negotiation '
                              "so engineers never touch it [7_L1_3-4kg8 @ 00:22:10]. ProsperOps' Erik "
                              'Carlin pitches the logical extreme: software that buys and manages Reserved '
                              'Instances and Savings Plans autonomously across more than $1B in annual '
                              'compute, stating flatly that the platform does not provide recommendations, '
                              'it acts [_ScBbR2FfCA @ 00:00:23]. Tatum Tummins of Kion makes the '
                              'governance case for the same instinct, warning that a human review cycle of '
                              '30 to 60 days simply lets waste pile up while the ticket waits; the line is '
                              'that policy becomes automation and automation becomes guardrails '
                              "[NE8Ua2YVa6Q @ 00:06:12]. Nathan Perry keeps Amazon's automation policy- "
                              'and threshold-triggered but logs every action and preserves human '
                              'oversight, calling that balance crucial to building trust and driving '
                              'adoption [tPYmvdc5oE0 @ 00:13:10]. The consensus position: commit to '
                              'discounted rates centrally, encode waste definitions, snapshot retention, '
                              'lights-off schedules and tagging rules as policy, and let machines execute '
                              'faster than a monthly review meeting ever could, while keeping an audit '
                              'trail humans can read.',
                              'The third shared conviction is that AI tokens have become the budget line '
                              'that breaks plans. Jean of 451/S&P reports that GenAI was the top cause of '
                              'budget overruns greater than 10%, and that FinOps X attendees now say 80% '
                              "of their time goes to AI spend [N1u_6ENlZV4 @ 00:15:23]. Vantage's Ben adds "
                              'that tracked spend across roughly 30 AI providers has tripled year-to-date, '
                              'with customers commonly running 1,500 to 2,500 employees on Claude. In the '
                              'Tokenmaxxing session, the Vantage team warns that leaderboards treating '
                              'token burn as productivity are not sustainable because tokens cost money, '
                              'and pushes cost per developer, cost per customer and cost per Linear ticket '
                              'as the real yardsticks [1-lJfz3oQ2w @ 00:05:23]. Adam Richter of the AWS '
                              'optics team reframes the job itself: FinOps is shifting from reading '
                              'dashboards to asking whether ten large GPU instances are each idling at 10% '
                              "when one at 100% would do [JqwiGt78aOI @ 00:07:58]. Intellipaat's unit math "
                              'shows why per-unit thinking wins: a Lambda refactor lifts spend from $1,000 '
                              'to $1,300 while users double from 1,000 to 2,000, pushing cost per customer '
                              'below $1 [7_L1_3-4kg8 @ 00:35:30].'],
               'table': {'caption': 'Where practitioners agree on the baseline FinOps operating model',
                         'headers': ['Consensus Point',
                                     'What Practitioners Actually Do',
                                     'Why It Matters To The Bill',
                                     'Expert Source'],
                         'rows': [['Visibility comes before any cutting',
                                   'Run Cost Explorer as a financial Fitbit, AWS Budgets with custom '
                                   'alerts, and Trusted Advisor for idle resources',
                                   'Zombie instances, complex pricing and organizational silos drive '
                                   'uncontrolled cloud growth when nobody is watching',
                                   'AWS With A Beer ([6qqv9Ss3MaE @ 00:03:00])'],
                                  ['Fine-grained cost data for every team',
                                   'Move from monthly account grain to hourly ARN grain using CUR and Data '
                                   'Exports, then open Cost Explorer to all',
                                   'Teams can only fix spend they can trace back to the specific resources '
                                   'they launched',
                                   'AWS Events ([tPYmvdc5oE0 @ 00:02:17])'],
                                  ['Engineers own their own cloud spend',
                                   'Developers justify every EC2 launch against business value instead of '
                                   'deferring cost questions to finance',
                                   'Finance staff cannot judge ECS, Lambda or EC2 architecture trade-offs '
                                   'on their own',
                                   'Intellipaat ([7_L1_3-4kg8 @ 00:07:24])'],
                                  ['Governance runs as automated policy',
                                   'Encode orphan definitions, snapshot retention, lights-off for dev and '
                                   'sandbox, and tag key-value pairs as policy',
                                   'Human reviews lasting 30 to 60 days let waste keep accruing while '
                                   'approvals sit in queue',
                                   'AWS Events ([NE8Ua2YVa6Q @ 00:05:06])'],
                                  ['Commitment buying is centralized and automated',
                                   'Automate RIs and Savings Plans and score results with Effective '
                                   'Savings Rate net of the vendor fee',
                                   'ESR turns discount instruments into one outcome-based ROI number '
                                   'leadership can track',
                                   'ProsperOps, a Flexera company ([_ScBbR2FfCA @ 00:00:56])'],
                                  ['AI spend needs a multi-KPI scorecard',
                                   'Track model mix, cache ratio, cost per developer, cost per customer '
                                   'and cost per Linear ticket together',
                                   'Single KPIs get gamed through smaller PRs or prompt reuse that '
                                   'inflates cache-hit ratios',
                                   'Vantage ([1-lJfz3oQ2w @ 00:16:23])'],
                                  ['Spend is framed against business outcomes',
                                   'Attribute spend to revenue, such as $100K of cloud spend tied to $1M '
                                   'of revenue generated',
                                   'Business-aligned mechanisms are one of the three core lessons from '
                                   "Amazon's internal FinOps program",
                                   'AWS Events ([tPYmvdc5oE0 @ 00:16:27])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["On commitments, ProsperOps publishes the scoreboard. Erik Carlin's example "
                              'customer console shows 1,306 automated actions averaging more than 45 per '
                              'day, near-perfect utilization, a 47% blended discount and over 98% '
                              'coverage, with savings reported as incremental lifetime dollars net of the '
                              'ProsperOps charge and allocated back by account, resource type or region '
                              'through Intelligent Showback [_ScBbR2FfCA @ 00:01:08]. The ProsperOps '
                              'benchmark across more than 1,400 data points, up to $2M per month in '
                              'compute, sets the grading curve: average Effective Savings Rate is 10.5%, '
                              'the 75th percentile sits in the low 20s and the 98th percentile hits about '
                              '40.5% [KW_LS_stgvc @ 00:03:35]. The same benchmark flags a savings-loss '
                              'zone, mostly at smaller customers holding unused commitments, because it is '
                              "actually possible with these instruments to lose money. Intellipaat's term "
                              'rule is the street version: never buy a three-year plan for an application '
                              'expected to last two, since one more year is completely wasted [7_L1_3-4kg8 '
                              '@ 00:15:36]. On Azure, the FinOps Foundation demo overlays existing '
                              'reservations and savings plans before acting on Advisor rightsizing, '
                              'because shrinking a VM can leave an existing RI underutilized [b7TiwS4_Ytw '
                              '@ 00:17:51].',
                              "Token spend gets its own toolkit. Vantage's demo wires OpenAI, Anthropic "
                              'and Cursor billing into one view, drills from token usage into uncached '
                              'input, cache writes, cache reads and output, then sets per-user budgets '
                              'with anomaly alerts; joining application logs to Anthropic costs splits out '
                              'agents that share a single API key [1-lJfz3oQ2w @ 00:24:06]. Ben at Vantage '
                              'recommends Bedrock request metadata combined with virtual tags for '
                              'attribution, and flags the billing-latency gap: AWS billing lags seven to '
                              'eight hours while an engineer can blow up token usage inside an hour, so '
                              'invocation logs should stream straight to the cost platform [N1u_6ENlZV4 @ '
                              "00:39:12]. Adam Richter's routing playbook uses Bedrock intelligent prompt "
                              'routing, Opus to plan and Sonnet or Haiku to write code, with backoffs or '
                              'sequential calls to dodge API throttling; input tokens run roughly four '
                              'times cheaper than output, but input balloons over multi-turn chats '
                              "[JqwiGt78aOI @ 00:18:04]. Hande Adiguzel treats the agent's context window "
                              'as a budget to optimize rather than a limit, warning that handing an agent '
                              'too many tools makes it slower, more expensive and likely to pick the wrong '
                              'tool [b7TiwS4_Ytw @ 00:23:47].',
                              'Repatriation math is where the street gets specific. Caleb Writes Code runs '
                              'the H100 numbers: a $200 monthly subscription over six years totals '
                              '$14,400, buying an H100 costs about $30,000, and renting one from a '
                              'neocloud at about $2.20 per hour for eight hours a day runs about $38,544 '
                              'with weekends or $27,456 on weekdays only [SmYNK0kqaDI @ 00:01:20]. Sharing '
                              'one card among four users shifts part of the math, since four subscriptions '
                              'cost $57,600 while the H100 plus roughly $3,700 of electricity at $0.20 per '
                              'kWh totals about $33,700, but Kimi K2 Thinking needs at least 14 H100s at '
                              'full precision and a DGX H100 lands near $400K total cost of ownership, or '
                              '28 users to break even [SmYNK0kqaDI @ 00:05:08]. Craft Computing shows the '
                              'cheap end: a Quanta T22HF two-node Epyc chassis with rails for $500, at a '
                              'time when a single H11SSL board alone has climbed to $300 to $400 '
                              '[JoqFD69bWLw @ 00:05:40]. Nick Gioftsos contrasts a $200 box against a '
                              "client's $4,000 cloud bill for the same workload, and specs a roughly 15 W "
                              'lab built on a Proxmox mini PC, a separate NAS, and a VLAN-segmented router '
                              'and switch [rGnDq9evKng @ 00:00:00].'],
               'table': {'caption': 'Exact mechanics, settings and unit economics taught by the '
                                    'practitioners',
                         'headers': ['Mechanic Or Tool',
                                     'Exact Numbers Or Settings',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Effective Savings Rate benchmark curve',
                                   'Average 10.5%, 75th percentile in the low 20s, 98th percentile about '
                                   '40.5%',
                                   'Grade commitment performance against more than 1,400 peer data points '
                                   'up to $2M monthly',
                                   'ProsperOps, a Flexera company ([KW_LS_stgvc @ 00:03:35])'],
                                  ['Autonomous RI and Savings Plan engine',
                                   '1,306 actions, 45-plus per day, 47% blended discount, over 98% '
                                   'coverage',
                                   'Let software adjust commitments daily instead of waiting on periodic '
                                   'human purchase reviews',
                                   'ProsperOps, a Flexera company ([_ScBbR2FfCA @ 00:01:08])'],
                                  ['Azure tiered forecast-based budgets',
                                   '50% and 75% thresholds on actual or forecasted cost, scoped by '
                                   'subscription, app, then tags',
                                   'Forecast-based alerts fire earlier and offset the latency in Azure '
                                   'cost data',
                                   'FinOps Foundation ([b7TiwS4_Ytw @ 00:11:19])'],
                                  ['AI-written Cloud Custodian cleanup policy',
                                   'Snapshot unattached EBS volumes older than 7 days, then delete the '
                                   'volumes',
                                   'Turn written waste definitions into enforced cleanup without filing '
                                   'manual tickets',
                                   'AWS Events ([NE8Ua2YVa6Q @ 00:09:25])'],
                                  ['AI-assisted monthly budget updates',
                                   'Cut from 45 to 60 minutes down to under 5 minutes across 50 to 100 '
                                   'cost centers',
                                   'In-app prompts replace spreadsheet grind for owners maintaining many '
                                   'cost center budgets',
                                   'AWS Events ([NE8Ua2YVa6Q @ 00:08:34])'],
                                  ['Rightsizing lift-and-shift servers',
                                   '32 cores and 256 GB provisioned, 4 vCPU and 16 GB used at peak, 87% '
                                   'wasted',
                                   'Monitor, identify, downsize, re-evaluate using Compute Optimizer and '
                                   'CloudWatch before and after migration',
                                   'CloudExpert Solutions ([dpje7Qql0SU @ 00:09:37])'],
                                  ['Owning versus renting H100 capacity',
                                   '$30,000 per card, about $2.20 per hour rented, DGX near $400K total '
                                   'cost of ownership',
                                   'Compare against $200 monthly subscriptions over six years before '
                                   'buying any GPU hardware',
                                   'Caleb Writes Code ([SmYNK0kqaDI @ 00:01:03])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Shortcuts operators pulled straight from their own demos',
                           'body': 'Small configuration moves the speakers used to keep automation, agents '
                                   'and token budgets from biting back.',
                           'items': ['Instance Scheduler is tag-based, so warn developers who work '
                                     'weekends before lights-off schedules shut their boxes down [AWS '
                                     'Events — JqwiGt78aOI @ 00:14:19].',
                                     'Start every FinOps agent read-only or human-in-the-loop, and confirm '
                                     '.gitignore hides access keys before the repo leaves the machine [AWS '
                                     'Events — JqwiGt78aOI @ 00:19:37].',
                                     'Prompt compactors can raise output tokens, so measure the full bill '
                                     'before declaring a compression win [Vantage — 1-lJfz3oQ2w @ '
                                     '00:30:15].',
                                     'If a user cannot view cost in the Azure portal, neither can their '
                                     'agent, so sort cost-read permissions before enabling the ARM MCP '
                                     'Server cost toolsets via headers [FinOps Foundation — b7TiwS4_Ytw @ '
                                     '00:26:56].']},
               'sop_steps': [{'step': 1,
                              'title': 'Drop to hourly, resource-level cost data',
                              'action': 'Enable CUR and Data Exports at hourly ARN grain and open Cost '
                                        'Explorer to every engineering team.',
                              'detail': 'Amazon moved off monthly account-level data, democratized Cost '
                                        'Explorer, and layered in tagging, Compute Optimizer, Cost '
                                        'Optimization Hub and Organizations [AWS Events — tPYmvdc5oE0 @ '
                                        '00:02:17].'},
                             {'step': 2,
                              'title': 'Set tiered, forecast-driven budgets',
                              'action': 'Build budgets by subscription or billing account, then app, then '
                                        'tags, with 50% and 75% thresholds on forecasted cost.',
                              'detail': 'Forecast-based budgets are more proactive and offset cost-data '
                                        'latency compared with alerts on actual spend [FinOps Foundation — '
                                        'b7TiwS4_Ytw @ 00:11:19].'},
                             {'step': 3,
                              'title': 'Automate commitments and score them with ESR',
                              'action': 'Hand RI and Savings Plan management to automation and track '
                                        'Effective Savings Rate against the peer curve.',
                              'detail': 'Average ESR is 10.5%, the 75th percentile sits in the low 20s and '
                                        'the 98th percentile reaches about 40.5%, while unused commitments '
                                        'can push smaller accounts into a savings-loss zone [ProsperOps, a '
                                        'Flexera company — KW_LS_stgvc @ 00:03:35].'},
                             {'step': 4,
                              'title': 'Instrument tokens in near real time',
                              'action': 'Stream model invocation logs into the cost platform, tag Bedrock '
                                        'requests, and set per-user budgets with anomaly alerts.',
                              'detail': 'AWS billing lags seven to eight hours while an engineer can blow '
                                        'up token usage within an hour, so invocation logs plus Bedrock '
                                        'request metadata and virtual tags close the gap [Vantage — '
                                        'N1u_6ENlZV4 @ 00:39:12].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The build-versus-buy fight is the sharpest split in the room. Jean of '
                              '451/S&P, speaking on Vantage, tracks a repeating arc: shops start with a '
                              'first-party tool, try to roll their own, then end up buying a capable '
                              'third-party platform [N1u_6ENlZV4 @ 00:06:38]. Nathan Perry of the AWS '
                              'OPTICS team, after 11 years inside Amazon, goes further and labels the '
                              "early custom-build confidence 'Dunning Kruger', a lesson the Amazon team "
                              'paid to learn [tPYmvdc5oE0 @ 00:19:27]. Adam Richter, also on the optics '
                              'team, does not ban building. Richter wires up a live FinOps agent on camera '
                              'with Kiro CLI, Strands and the Billing and Cost Management MCP, but warns '
                              'that the moment you build, you own support and security yourself '
                              '[JqwiGt78aOI @ 00:09:22]. ProsperOps takes the opposite pole from every '
                              'dashboard vendor: Erik Carlin states flatly that the platform does not '
                              'provide recommendations, it acts, with ProsperBot buying and reshaping RIs '
                              'and Savings Plans autonomously across more than $1B in annual compute '
                              '[_ScBbR2FfCA @ 00:00:23]. The operator choice is three-way: buy visibility, '
                              'build an agent you will maintain forever, or hand the commitment portfolio '
                              'to an autonomous engine and judge it purely on incremental savings net of '
                              'its own charge.',
                              'How fast automation should fire is the second fault line. Tatum Tummins of '
                              'Kion, who spent 7.5 years running FinOps in healthcare, argues that a human '
                              'review cycle of 30 to 60 days simply lets waste accrue in the meantime, and '
                              'pushes policy straight into automated guardrails: orphan definitions, '
                              'snapshot retention, lights-off for dev and sandbox, and enforced tag '
                              "key-value pairs [NE8Ua2YVa6Q @ 00:06:12]. Nathan Perry runs Amazon's own "
                              'estate with a counterweight, keeping policy- and threshold-triggered '
                              'automation paired with human oversight and logging every single action, '
                              'calling that balance crucial to building trust and driving adoption '
                              '[tPYmvdc5oE0 @ 00:13:10]. Adam Richter sits even further toward caution for '
                              'agents, preferring to start read-only or human-in-the-loop before granting '
                              'any write access [JqwiGt78aOI @ 00:19:37]. The Microsoft team of Vikram '
                              'Desai and Hande Adiguzel lands on a hybrid: the GitHub Copilot CLI agent '
                              'pulls Advisor usage and rate recommendations, overlays existing RIs and '
                              'savings plans, then ships the change as a Terraform pull request for human '
                              "approval [b7TiwS4_Ytw @ 00:20:35]. Kion's fast lane looks like an "
                              'AI-written Cloud Custodian policy that snapshots unattached EBS volumes '
                              'older than 7 days and then deletes them; the Microsoft lane routes every '
                              'change through a reviewer first.',
                              'The repatriation debate splits cleanly between cloud economics and owned '
                              'iron. CloudExpert Solutions frames CapEx as the losing bet: $2M on servers '
                              'over five years, traffic drops by year three, the hardware is outdated by '
                              'year five, and you carry the full risk, while OpEx scales from 10 to 50 to '
                              "5 servers with 'zero waste' [dpje7Qql0SU @ 00:02:47]. Nick Gioftsos, a "
                              'systems and cloud engineer working in Azure and Microsoft 365, opens with '
                              "the counter-punch: a $200 box doing the same workload as a client's $4,000 "
                              'cloud bill, with the team sitting idle for three hours during a regional '
                              'hiccup, and a warning that cloud-only engineers are building careers on '
                              'rented land [rGnDq9evKng @ 00:00:00]. Caleb Writes Code runs the GPU '
                              'version of the same math and lands on the rental side: $200 a month in '
                              'subscriptions for six years totals $14,400 against roughly $30,000 for one '
                              "H100, so 'the math doesn't really work in our favor' for owning "
                              '[SmYNK0kqaDI @ 00:01:03]. Hostrunway pitches the middle path: dedicated '
                              'bare metal with H100, H200 and B300 GPUs, no hypervisor, no noisy '
                              'neighbors, billed month-to-month with no lock-in [Auj5NAlVFVk @ 00:02:13]. '
                              "Even Gioftsos concedes the cloud isn't going away."],
               'table': {'caption': 'Competing playbooks named practitioners run for cloud and AI compute '
                                    'spend',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Cost tooling: build in-house or buy a platform',
                                   'Start with first-party tools, attempt an in-house build, then buy a '
                                   'capable third-party tool',
                                   'Build on native AWS Billing and Cost Management and treat custom-build '
                                   'confidence as Dunning Kruger',
                                   'Vantage ([N1u_6ENlZV4 @ 00:06:38]); AWS Events ([tPYmvdc5oE0 @ '
                                   '00:19:27])'],
                                  ['Who executes commitment purchases and adjustments',
                                   'ProsperBot autonomously buys and reshapes RIs and Savings Plans with '
                                   'no recommendations step',
                                   'Trusted Advisor and Compute Optimizer surface rightsizing and RI '
                                   'recommendations for humans to act on',
                                   'ProsperOps, a Flexera company ([_ScBbR2FfCA @ 00:00:23]); AWS With A '
                                   'Beer ([6qqv9Ss3MaE @ 00:03:00])'],
                                  ['How fast governance automation should fire',
                                   'Policy becomes automation and guardrails, skipping 30 to 60 day human '
                                   'review lag',
                                   'Policy and threshold-triggered automation paired with human oversight '
                                   'and every action logged',
                                   'AWS Events ([NE8Ua2YVa6Q @ 00:06:12]); AWS Events ([tPYmvdc5oE0 @ '
                                   '00:13:10])'],
                                  ['How much write access a FinOps agent gets',
                                   'Start the agent read-only or human-in-the-loop before any autonomous '
                                   'action',
                                   'Agent drafts the optimization as a Terraform pull request for human '
                                   'approval',
                                   'AWS Events ([JqwiGt78aOI @ 00:19:37]); FinOps Foundation ([b7TiwS4_Ytw '
                                   '@ 00:20:35])'],
                                  ['Owning infrastructure versus paying for cloud usage',
                                   'OpEx cloud: pay for 10, then 50, then 5 servers with zero waste',
                                   "A $200 owned box replacing a client's $4,000 cloud bill for the same "
                                   'workload',
                                   'CloudExpert Solutions ([dpje7Qql0SU @ 00:04:13]); Nick Gioftsos '
                                   '([rGnDq9evKng @ 00:00:00])'],
                                  ['Single-user AI compute: subscribe, rent, or buy',
                                   'A $200 monthly subscription totals $14,400 over six full years',
                                   'Buy an H100 near $30,000 or rent a neocloud H100 at $2.20 per hour',
                                   'Caleb Writes Code ([SmYNK0kqaDI @ 00:01:03])'],
                                  ['How to route expensive models across the organization',
                                   'Blunt routing that makes certain models off-limits to certain '
                                   'departments entirely',
                                   'Bedrock intelligent prompt routing: Opus plans the work, Sonnet or '
                                   'Haiku writes the code',
                                   'Vantage ([N1u_6ENlZV4 @ 00:27:24]); AWS Events ([JqwiGt78aOI @ '
                                   '00:15:14])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Commitments are where operators bleed fastest. ProsperOps built a benchmark '
                              'of more than 1,400 data points covering up to $2M a month in compute spend, '
                              'and it maps a savings-loss zone where unused commitments turn into a net '
                              "loss: 'it's actually possible with these instruments to lose money', with "
                              'that zone dominated by smaller customers [KW_LS_stgvc @ 00:01:58]. Right '
                              'above it sits a no-savings zone where commitments go unused at spend levels '
                              'up to roughly $250K to $500K a month, and the average Effective Savings '
                              'Rate across the whole set is only 10.5%, against the low 20s at the 75th '
                              'percentile and about 40.5% at the 98th [KW_LS_stgvc @ 00:03:35]. '
                              "Intellipaat's instructor gives the simplest version of the trap: buy a "
                              "three-year plan for an app predicted to live two years and 'one more year "
                              "would be completely wasted' [7_L1_3-4kg8 @ 00:15:36]. The Microsoft demo "
                              'exposes the collision between rate and usage optimization: right-sizing a '
                              'VM can leave an existing reservation underutilized, which is why the '
                              'Copilot agent overlays current RIs and savings plans on top of Advisor '
                              'recommendations before proposing any change [b7TiwS4_Ytw @ 00:17:51]. Rate '
                              'wins and usage wins fight each other unless one workflow sees both at the '
                              'same time.',
                              'AI spend breaks the old monthly-close rhythm. Ben of Vantage and Jean of '
                              '451/S&P both flag the latency gap: AWS billing lags 7 to 8 hours, while an '
                              'engineer can blow up token usage inside an hour, so the fix is streaming '
                              'invocation logs straight into the cost platform, and both agree there is '
                              'still room for improvement [N1u_6ENlZV4 @ 00:39:12]. Tokenmaxxing creates '
                              "its own perverse incentives: Vantage's session on AI budgets warns that "
                              'smaller PRs drive tokens-per-PR down without improving cost-per-feature, '
                              'and prompt reuse inflates cache-hit ratios, so any single KPI gets gamed '
                              'and teams must track many of them [1-lJfz3oQ2w @ 00:14:57]. The same '
                              'session reports that prompt compactors can raise output tokens, the '
                              'opposite of what an operator buys them for [1-lJfz3oQ2w @ 00:30:15]. Adam '
                              'Richter adds the math behind that trap: input tokens run about four times '
                              'cheaper than output, but input balloons as multi-turn chats carry history '
                              'forward, and the consensus-plus-judge agent pattern that cuts hallucination '
                              "costs more to run [JqwiGt78aOI @ 00:18:04]. Vantage's rule is to decide the "
                              'over-budget action, downgrade the model or stop usage, before the spike '
                              'hits, while protecting end users in application AI.',
                              'Repatriating to owned hardware trades the cloud bill for a new set of '
                              'failure points. Craft Computing bought two AMD Epyc nodes in a Quanta T22HF '
                              'chassis for $500 including rails, then hit a wall: one proprietary U.2 '
                              'power cable, zero vendor documentation for a 2018 server, no POST after '
                              'about 20 minutes, and a BMC that appears cloud-connected to Quanta, '
                              'requiring a license and active subscription to manage your own local '
                              "hardware [JoqFD69bWLw @ 00:15:33]. Quanta's answer was that it does not "
                              'recommend CPUs not designed for the platform and cannot provide relevant '
                              'documentation, leaving the fix to crowdsourcing [JoqFD69bWLw @ 00:19:39]. '
                              'Caleb Writes Code finds the GPU version of the same trap: Kimi K2 Thinking '
                              'needs at least 14 H100s at full precision, a DGX H100 runs $285K to $300K, '
                              'about $400K total cost of ownership, and needs 28 users to break even '
                              '[SmYNK0kqaDI @ 00:05:08]. Even then, the 140 GB left for KV cache yields '
                              'roughly 80,000 tokens, about 2,850 per person. Nick Gioftsos names the '
                              'cloud-side trap as the virtual taximeter: fear of a $400 bill drives a '
                              'terraform destroy after 45 minutes, so day-90 problems like a full /var, '
                              'expired certificates and memory leaks never surface [rGnDq9evKng @ '
                              '00:03:58].'],
               'table': {'caption': 'Firsthand traps and the economics check each practitioner applied',
                         'headers': ['Trap', 'Firsthand Evidence', 'Economics Check', 'Expert Source'],
                         'rows': [['Unused commitments sitting idle on the bill',
                                   'Savings-loss zone concentrated among smaller customers in a '
                                   '1,400-point benchmark',
                                   'Track ESR: average 10.5% versus about 40.5% at the 98th percentile',
                                   'ProsperOps, a Flexera company ([KW_LS_stgvc @ 00:01:58])'],
                                  ["Commitment term longer than the workload's life",
                                   'Three-year plan bought for an application predicted to last two years',
                                   'One full year of the commitment is completely wasted',
                                   'Intellipaat ([7_L1_3-4kg8 @ 00:15:36])'],
                                  ['Slow human review of waste policies',
                                   'Waste keeps accruing during 30 to 60 day review cycles',
                                   'Convert written policy into automated guardrails that produce outcomes',
                                   'AWS Events ([NE8Ua2YVa6Q @ 00:06:12])'],
                                  ['Billing latency on fast-moving AI token spend',
                                   'AWS billing lags 7 to 8 hours while one engineer can blow up tokens '
                                   'within an hour',
                                   'Stream invocation logs directly into the cost platform for near '
                                   'real-time alerts',
                                   'Vantage ([N1u_6ENlZV4 @ 00:39:12])'],
                                  ['Lift-and-shift migration carrying oversized servers',
                                   '32 cores and 256 GB provisioned while peak use is 4 vCPU and 16 GB',
                                   '87% of spend wasted; monitor, identify, downsize, then re-evaluate '
                                   'continuously',
                                   'CloudExpert Solutions ([dpje7Qql0SU @ 00:09:37])'],
                                  ['Cheap proprietary used servers with locked management',
                                   'Cloud-connected BMC needing a Quanta subscription, no documentation, '
                                   'one proprietary U.2 cable',
                                   '$500 bought two Epyc nodes that still would not POST',
                                   'Craft Computing ([JoqFD69bWLw @ 00:15:33])'],
                                  ['Self-hosting a frontier model on owned GPUs',
                                   'Kimi K2 Thinking needs at least 14 H100s at full precision',
                                   'DGX H100 at about $400K TCO needs 28 users just to break even',
                                   'Caleb Writes Code ([SmYNK0kqaDI @ 00:05:08])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Ship Checks Before Committing, Automating, or Repatriating',
                           'body': 'Every item below is a trap a named practitioner hit or measured '
                                   'firsthand. Clear all four before signing a commitment, granting an '
                                   'agent write access, or racking owned hardware.',
                           'items': ["Never buy a commitment term longer than the workload's predicted "
                                     'life; a three-year plan on a two-year app wastes a full year '
                                     '[Intellipaat — 7_L1_3-4kg8 @ 00:15:36].',
                                     'Overlay existing RIs and savings plans before right-sizing, or the '
                                     'downsized VM leaves the reservation underutilized [FinOps Foundation '
                                     '— b7TiwS4_Ytw @ 00:17:51].',
                                     'Start any FinOps agent read-only or human-in-the-loop, and confirm '
                                     '.gitignore hides access keys before code leaves the box [AWS Events '
                                     '— JqwiGt78aOI @ 00:19:37].',
                                     'Before buying used servers, verify the BMC is not locked behind a '
                                     'vendor cloud license and that documentation exists for the platform '
                                     '[Craft Computing — JoqFD69bWLw @ 00:15:33].']}}],
 'pull_quote': '"It\'s actually possible with these instruments to lose money." — attributed to '
               'ProsperOps, a Flexera company (KW_LS_stgvc @ 00:01:58).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Move cost data from monthly/account grain to hourly/ARN grain using CUR and Data '
                      'Exports, and open Cost Explorer to every team [AWS Events — tPYmvdc5oE0 @ '
                      '00:02:17].',
                      'Adopt Effective Savings Rate as the outcome KPI for commitments and benchmark it '
                      'against the 10.5% average and the 40.5% top tier [ProsperOps, a Flexera company — '
                      'KW_LS_stgvc @ 00:00:39].',
                      'Build tiered budgets from subscription to app to tags with 50% and 75% thresholds '
                      'on forecasted cost to offset data latency [FinOps Foundation — b7TiwS4_Ytw @ '
                      '00:11:19].',
                      'Integrate OpenAI, Anthropic and Cursor spend, drill into uncached input, cache '
                      'writes/reads and output, and set per-user budgets with anomaly alerts [Vantage — '
                      '1-lJfz3oQ2w @ 00:19:43].',
                      'Route models by task with Bedrock intelligent prompt routing, using Opus to plan '
                      'and Sonnet or Haiku to code [AWS Events — JqwiGt78aOI @ 00:15:14].',
                      'Codify waste policy as automation, such as a Cloud Custodian policy that snapshots '
                      'unattached EBS volumes older than 7 days and then deletes them [AWS Events — '
                      'NE8Ua2YVa6Q @ 00:09:25].'],
 'statutory_citations': [{'title': 'ProsperOps, a Flexera company — Benchmarking AWS Cloud Financial '
                                   'Management [00:01:58]',
                          'url': 'https://www.youtube.com/watch?v=KW_LS_stgvc&t=118s',
                          'relevance': 'Primary practitioner testimony on commitment savings-loss zones '
                                       'and ESR percentile benchmarks.'},
                         {'title': "AWS Events — AWS re:Invent 2025 - Amazon's finops: Cloud cost lessons "
                                   'from a global e-commerce giant (AMZ308) [00:13:10]',
                          'url': 'https://www.youtube.com/watch?v=tPYmvdc5oE0&t=790s',
                          'relevance': 'Primary practitioner testimony on balancing automation with human '
                                       'oversight inside Amazon.'},
                         {'title': 'Vantage — The State of Cloud & AI Cost Management in 2026 | FinOps '
                                   'Summer Camp Session 1 [00:39:12]',
                          'url': 'https://www.youtube.com/watch?v=N1u_6ENlZV4&t=2352s',
                          'relevance': 'Primary practitioner testimony on billing latency versus near '
                                       'real-time AI token spend.'},
                         {'title': 'Caleb Writes Code — AI Subscription vs H100 [00:01:03]',
                          'url': 'https://www.youtube.com/watch?v=SmYNK0kqaDI&t=63s',
                          'relevance': 'Primary practitioner testimony on owning versus renting versus '
                                       'subscribing to GPU compute.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '6qqv9Ss3MaE',
                       'title': 'AWS FinOps Explained in 5 Minutes',
                       'channel': 'AWS With A Beer',
                       'author': 'AWS With A Beer',
                       'text': 'FinOps is a financial guard rail where engineering, finance and leadership '
                               'work together.',
                       'tip': 'FinOps is a financial guard rail where engineering, finance and leadership '
                              'work together.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=6qqv9Ss3MaE&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=6qqv9Ss3MaE&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'N1u_6ENlZV4',
                       'title': 'The State of Cloud & AI Cost Management in 2026 | FinOps Summer Camp '
                                'Session 1',
                       'channel': 'Vantage',
                       'author': 'Vantage',
                       'text': 'And so these are big businesses that are growing and as a result they have '
                               'a big impact on costs.',
                       'tip': 'And so these are big businesses that are growing and as a result they have '
                              'a big impact on costs.',
                       'timestamp': 1408,
                       'timestamp_seconds': 1408,
                       'timestamp_label': '[00:23:28]',
                       'url': 'https://www.youtube.com/watch?v=N1u_6ENlZV4&t=1408s',
                       'markdown': '[00:23:28](https://www.youtube.com/watch?v=N1u_6ENlZV4&t=1408s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_ScBbR2FfCA',
                       'title': 'FinOps X - 3-min Vendor Pitch - ProsperOps with Erik Carlin',
                       'channel': 'ProsperOps, a Flexera company',
                       'author': 'ProsperOps, a Flexera company',
                       'text': "Our platform doesn't provide recommendations.",
                       'tip': "Our platform doesn't provide recommendations.",
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=_ScBbR2FfCA&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=_ScBbR2FfCA&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NE8Ua2YVa6Q',
                       'title': 'AWS re:Invent 2025 - FinOps+: A New Era of Accelerating Value (COP211)',
                       'channel': 'AWS Events',
                       'author': 'AWS Events',
                       'text': 'Policy becomes automation and automation becomes guardrails.',
                       'tip': 'Policy becomes automation and automation becomes guardrails.',
                       'timestamp': 285,
                       'timestamp_seconds': 285,
                       'timestamp_label': '[00:04:45]',
                       'url': 'https://www.youtube.com/watch?v=NE8Ua2YVa6Q&t=285s',
                       'markdown': '[00:04:45](https://www.youtube.com/watch?v=NE8Ua2YVa6Q&t=285s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1-lJfz3oQ2w',
                       'title': 'Managing AI Budgets in the Age of Tokenmaxxing | FinOps Summer Camp '
                                'Session 3',
                       'channel': 'Vantage',
                       'author': 'Vantage',
                       'text': 'In reality this is not really a sustainable practice because obviously '
                               'tokens cost money.',
                       'tip': 'In reality this is not really a sustainable practice because obviously '
                              'tokens cost money.',
                       'timestamp': 323,
                       'timestamp_seconds': 323,
                       'timestamp_label': '[00:05:23]',
                       'url': 'https://www.youtube.com/watch?v=1-lJfz3oQ2w&t=323s',
                       'markdown': '[00:05:23](https://www.youtube.com/watch?v=1-lJfz3oQ2w&t=323s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KW_LS_stgvc',
                       'title': 'Benchmarking AWS Cloud Financial Management',
                       'channel': 'ProsperOps, a Flexera company',
                       'author': 'ProsperOps, a Flexera company',
                       'text': "It's actually possible with these instruments to lose money.",
                       'tip': "It's actually possible with these instruments to lose money.",
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=KW_LS_stgvc&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=KW_LS_stgvc&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wKXTR8j4jbY',
                       'title': 'AWS reInvent 2025:  FinOps A New Era of Accelerating Value',
                       'channel': 'Kion',
                       'author': 'Kion',
                       'text': 'When that happens, you start to have guardrails and those guardrails '
                               'produce outcomes.',
                       'tip': 'When that happens, you start to have guardrails and those guardrails '
                              'produce outcomes.',
                       'timestamp': 345,
                       'timestamp_seconds': 345,
                       'timestamp_label': '[00:05:45]',
                       'url': 'https://www.youtube.com/watch?v=wKXTR8j4jbY&t=345s',
                       'markdown': '[00:05:45](https://www.youtube.com/watch?v=wKXTR8j4jbY&t=345s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tPYmvdc5oE0',
                       'title': "AWS re:Invent 2025 - Amazon's finops: Cloud cost lessons from a global "
                                'e-commerce giant (AMZ308)',
                       'channel': 'AWS Events',
                       'author': 'AWS Events',
                       'text': "This balance between automation and oversight is super important, and it's "
                               'crucial to building trust and driving adoption.',
                       'tip': "This balance between automation and oversight is super important, and it's "
                              'crucial to building trust and driving adoption.',
                       'timestamp': 790,
                       'timestamp_seconds': 790,
                       'timestamp_label': '[00:13:10]',
                       'url': 'https://www.youtube.com/watch?v=tPYmvdc5oE0&t=790s',
                       'markdown': '[00:13:10](https://www.youtube.com/watch?v=tPYmvdc5oE0&t=790s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7_L1_3-4kg8',
                       'title': 'AWS Finops Tutorial | AWS FinOps | Cloud Finops | Intellipaat',
                       'channel': 'Intellipaat',
                       'author': 'Intellipaat',
                       'text': 'Do not buy a three-year plan for an application predicted to last two '
                               'years, because one more year would be completely wasted.',
                       'tip': 'Do not buy a three-year plan for an application predicted to last two '
                              'years, because one more year would be completely wasted.',
                       'timestamp': 936,
                       'timestamp_seconds': 936,
                       'timestamp_label': '[00:15:36]',
                       'url': 'https://www.youtube.com/watch?v=7_L1_3-4kg8&t=936s',
                       'markdown': '[00:15:36](https://www.youtube.com/watch?v=7_L1_3-4kg8&t=936s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JqwiGt78aOI',
                       'title': 'Build a FinOps Agent I The Keys to AWS Optimization | S16 E6',
                       'channel': 'AWS Events',
                       'author': 'AWS Events',
                       'text': 'From my perspective, I prefer initially like read only or human in the '
                               'loop.',
                       'tip': 'From my perspective, I prefer initially like read only or human in the '
                              'loop.',
                       'timestamp': 1177,
                       'timestamp_seconds': 1177,
                       'timestamp_label': '[00:19:37]',
                       'url': 'https://www.youtube.com/watch?v=JqwiGt78aOI&t=1177s',
                       'markdown': '[00:19:37](https://www.youtube.com/watch?v=JqwiGt78aOI&t=1177s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dpje7Qql0SU',
                       'title': 'Cloud FinOps Explained | CapEx vs OpEx, Cost Savings & Rightsizing | AWS '
                                'CLF-C02 [2026]',
                       'channel': 'CloudExpert Solutions',
                       'author': 'CloudExpert Solutions',
                       'text': 'They are wasting 87% of what they pay for.',
                       'tip': 'They are wasting 87% of what they pay for.',
                       'timestamp': 598,
                       'timestamp_seconds': 598,
                       'timestamp_label': '[00:09:58]',
                       'url': 'https://www.youtube.com/watch?v=dpje7Qql0SU&t=598s',
                       'markdown': '[00:09:58](https://www.youtube.com/watch?v=dpje7Qql0SU&t=598s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b7TiwS4_Ytw',
                       'title': 'AI for FinOps on Azure: Smarter Cloud Operations with Agentic AI',
                       'channel': 'FinOps Foundation',
                       'author': 'FinOps Foundation',
                       'text': "There's one principle we kept in mind when we were building the server, "
                               "which is treat your agent's context window as a budget you need to "
                               'optimize, rather than a limit you cannot exceed.',
                       'tip': "There's one principle we kept in mind when we were building the server, "
                              "which is treat your agent's context window as a budget you need to "
                              'optimize, rather than a limit you cannot exceed.',
                       'timestamp': 1406,
                       'timestamp_seconds': 1406,
                       'timestamp_label': '[00:23:26]',
                       'url': 'https://www.youtube.com/watch?v=b7TiwS4_Ytw&t=1406s',
                       'markdown': '[00:23:26](https://www.youtube.com/watch?v=b7TiwS4_Ytw&t=1406s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JoqFD69bWLw',
                       'title': 'TWO AMD Epyc Servers for $500!',
                       'channel': 'Craft Computing',
                       'author': 'Craft Computing',
                       'text': 'The BMC appears to be cloud connected directly to Quanta, so you have to '
                               'have a license and an active subscription with Quanta to access the BMC on '
                               'your own local hardware.',
                       'tip': 'The BMC appears to be cloud connected directly to Quanta, so you have to '
                              'have a license and an active subscription with Quanta to access the BMC on '
                              'your own local hardware.',
                       'timestamp': 933,
                       'timestamp_seconds': 933,
                       'timestamp_label': '[00:15:33]',
                       'url': 'https://www.youtube.com/watch?v=JoqFD69bWLw&t=933s',
                       'markdown': '[00:15:33](https://www.youtube.com/watch?v=JoqFD69bWLw&t=933s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rGnDq9evKng',
                       'title': 'The Cloud Was a Lie (Why Senior Engineers Are Going Back to Bare Metal)',
                       'channel': 'Nick Gioftsos',
                       'author': 'Nick Gioftsos',
                       'text': 'If you only know how to build in the cloud, you are building your career '
                               'on rented land.',
                       'tip': 'If you only know how to build in the cloud, you are building your career on '
                              'rented land.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=rGnDq9evKng&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=rGnDq9evKng&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Auj5NAlVFVk',
                       'title': 'Bare-Metal, Cloud & AI GPU Servers Built for Scale | Hostrunway',
                       'channel': 'Hostrunway',
                       'author': 'Hostrunway',
                       'text': 'No hypervisor, no noisy neighbors.',
                       'tip': 'No hypervisor, no noisy neighbors.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=Auj5NAlVFVk&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=Auj5NAlVFVk&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SmYNK0kqaDI',
                       'title': 'AI Subscription vs H100',
                       'channel': 'Caleb Writes Code',
                       'author': 'Caleb Writes Code',
                       'text': "So yeah, right up front, the math doesn't really work in our favor because "
                               "you're much better off using $200 a month subscription for 6 years "
                               'instead.',
                       'tip': "So yeah, right up front, the math doesn't really work in our favor because "
                              "you're much better off using $200 a month subscription for 6 years instead.",
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=SmYNK0kqaDI&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=SmYNK0kqaDI&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SmYNK0kqaDI',
                       'title': 'AI Subscription vs H100',
                       'channel': 'Caleb Writes Code',
                       'author': 'Caleb Writes Code',
                       'text': 'Broadly speaking my hot take is that companies that charge by the API '
                               "pricing probably bakes their unit cost into their pricing so they don't "
                               'lose money.',
                       'tip': 'Broadly speaking my hot take is that companies that charge by the API '
                              "pricing probably bakes their unit cost into their pricing so they don't "
                              'lose money.',
                       'timestamp': 509,
                       'timestamp_seconds': 509,
                       'timestamp_label': '[00:08:29]',
                       'url': 'https://www.youtube.com/watch?v=SmYNK0kqaDI&t=509s',
                       'markdown': '[00:08:29](https://www.youtube.com/watch?v=SmYNK0kqaDI&t=509s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
