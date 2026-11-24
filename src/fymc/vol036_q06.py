from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'neocloud-economics-multi-cloud-gpu-brokerage',
 'question_prompt': 'How do neoclouds make money, and how do teams broker and schedule GPU jobs across '
                    'multiple clouds and clusters?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Neocloud Economics and Multi-Cloud GPU Brokerage',
 'subtitle': 'Single-H100 neocloud unit economics, CoreWeave, Nebius, Crusoe, Lambda, and Fluidstack, '
             'GPUaaS, startups leaving AWS and Azure for bare metal, debt-financed buildouts from the '
             'telecom bust, SkyPilot as an intercloud broker at Meta scale, unscheduled-GPU diagnosis, '
             'gang scheduling and preemption, spot-checkpoint math, CoreWeave SUNK, Modelplane, and '
             'multi-node fine-tuning on Nebius',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Neocloud operators and multi-cloud brokers converge on one law: idle or stalled '
                      'GPUs bleed money, so utilization, scheduling and portability decide who survives. '
                      'Caleb Writes Code models a $25K H100 rented at $2.30/hr returning a 28% CAGR only '
                      'at full utilization, with broad stocks winning below roughly 55%. Neoclouds list '
                      'GPUs at roughly half to two-thirds of hyperscaler prices and up to 30-50% cheaper '
                      "on contract, while SkyPilot's broker finds up to 3x on-demand and 9x spot price "
                      'spreads across zones. Street mechanics center on queues with priority preemption, '
                      'checkpointed spot runs saved near a 34-minute interval, and one YAML spec that '
                      'fails over across clouds. Disagreement persists over provider picks, Slurm versus '
                      'Kubernetes, and whether neocloud debt echoes the telecom bust, where a NY-LA '
                      'circuit collapsed from $1.8M to under $150K a year.',
 'key_metrics': [{'label': 'Neocloud Break-Even Utilization',
                  'metric': 'Neocloud Break-Even Utilization',
                  'value': 'At or below ~55% utilization, broad stocks beat the neocloud',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'H100 bought for $25K plus $5K opex, rented at $2.30/hr for about 4 years, '
                             'returns a 28% CAGR only at 100% utilization',
                  'source': 'Caleb Writes Code ([9u2hCf8FlW0 @ 00:01:22])'},
                 {'label': 'Cross-Cloud GPU Price Spread',
                  'metric': 'Cross-Cloud GPU Price Spread',
                  'value': 'Up to 3x on-demand and up to 9x spot',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Price differences measured across zones by the SkyPilot intercloud broker '
                             "team at NSDI '23",
                  'source': 'USENIX ([3Edw88b1bRg @ 00:07:21])'},
                 {'label': 'Scheduler Utilization Gap',
                  'metric': 'Scheduler Utilization Gap',
                  'value': '~45% default Kubernetes vs ~85% workload-aware, worth ~$150k per day',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Modeled on a 10,000-GPU fleet costing about $400M across 1,250 hosts in 32 '
                             'racks',
                  'source': 'Codemia ([a_zou7QahAo @ 00:04:38])'},
                 {'label': 'Optimal Spot Checkpoint Interval',
                  'metric': 'Optimal Spot Checkpoint Interval',
                  'value': '~34 minutes (square root of 2 x MTBI x save cost)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': '2,000-run simulation of a 100h job with 8h interruptions, 6-minute restarts, '
                             '72s saves and a 70% spot discount',
                  'source': 'The Code Notebook ([IZtzUfhm8LU @ 00:10:20])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every operator in this chapter starts from the same brutal arithmetic: a '
                              'GPU only earns while it is busy. Caleb Writes Code prices a single H100 at '
                              '$25K plus $5K opex, gives it roughly 4 years of useful life, and shows that '
                              'renting it at $2.30/hr yields about $55 a day, near $20K a year and about '
                              '$80K over four years, which works out to a 28% CAGR only at 100% '
                              'utilization; at or below roughly 55% utilization, broad stocks beat the '
                              'neocloud outright [9u2hCf8FlW0 @ 00:01:22]. The gpuMaster frames the same '
                              'pain from the renter side: stalled GPUs still bill, and large-scale GPU '
                              "workloads are 'far less forgiving' [_tV0Elv_jIk @ 00:01:29]. Codemia puts a "
                              'dollar figure on scheduler quality for a 10,000-GPU fleet: default '
                              'Kubernetes lands near 45% utilization, a workload-aware design reaches '
                              'about 85%, and that gap is worth roughly $150k per day [a_zou7QahAo @ '
                              '00:04:38]. The Code Notebook compresses the whole consensus into one line, '
                              "'The cheapest GPU is one that is switched off,' backed by a scale-to-zero "
                              'simulation that cut 24 GPU-hours to 4.04, an 83% reduction, at a cost of '
                              '3.9 cold starts per day lasting 60 seconds each [IZtzUfhm8LU @ 00:12:17].',
                              'The second point of agreement is that neoclouds win on price and workload '
                              'fit, not on breadth of services. Cloud Computing Insider defines a neocloud '
                              'as an AI-first, GPU-centric provider and argues that hyperscalers were '
                              'built for all IT, while neoclouds were built for the compute, networking '
                              'and storage patterns modern AI needs, and hyperscalers charge more for AI '
                              'because they run it less efficiently [mAgWtefgeP8 @ 00:01:02]. Romil '
                              'Bhardwaj of SkyPilot, speaking at TMLS, lists the neocloud edge as instant '
                              'self-serve capacity, 3.2TB/s InfiniBand, top SemiAnalysis ClusterMAX tiers, '
                              'and pricing up to 30 to 50% cheaper depending on contract length, while '
                              'warning that the long tail of neoclouds runs 2 to 3x cheaper but less '
                              'reliable [_oWJ0t-RW7o @ 00:06:30]. The Code Notebook, working from vendor '
                              'figures dated October 2026, pegs neocloud GPU list prices at roughly '
                              'one-half to two-thirds of big-cloud rates [IZtzUfhm8LU @ 00:05:29]. Caleb '
                              'Writes Code, whose own model assumes a market rate of $1 to $5 per hour '
                              'across CoreWeave, Runpod, Vultr and Thunder Compute, adds the hard '
                              'corollary: neoclouds are heavily commoditized, customers typically look for '
                              'the cheapest pricing, and any operator who charges a premium watches '
                              'utilization fall [9u2hCf8FlW0 @ 00:01:37].',
                              'The third consensus is that no serious buyer stays on one provider. '
                              'Zhanghao Wu and Kevin Mingtarja of SkyPilot open their '
                              'frontier-capabilities talk by pointing to Meta signing multi-billion-dollar '
                              'deals with CoreWeave and Nebius and give three reasons to run '
                              'multi-provider: capacity, cost, and no single point of failure [uwLkrJb5pEA '
                              "@ 00:01:47]. Romil Bhardwaj, presenting at CNCF, traces OpenAI's move from "
                              'Microsoft exclusivity to Oracle, CoreWeave and GCP [-czZES1U_Us @ '
                              "00:00:49]. The USENIX NSDI '23 SkyPilot team makes the economic case for "
                              'brokerage: silos reduce availability and leverage, a single-cloud business '
                              'is more vulnerable to large-scale outages, and it has lower negotiation '
                              "leverage to get a better deal because 'choice is power' [3Edw88b1bRg @ "
                              '00:01:22]. Their broker example routes SGX workloads to Azure, TPU training '
                              'to GCP and Inferentia inference to AWS. Cloud Computing Insider expects the '
                              'end state to be a hybrid, heterogeneous mix, telling buyers that a '
                              'best-of-breed play is going to be complex and heterogeneous, and that if '
                              'they shortlist two providers it is probably Nebius and CoreWeave, while '
                              'disclaiming any single-provider recommendation [mAgWtefgeP8 @ 00:13:14]. '
                              'The prerequisite all of them share is a portability layer that lets '
                              'workloads move when prices, quotas or availability shift.'],
               'table': {'caption': 'Where neocloud operators, brokers and buyers agree on the core '
                                    'economics',
                         'headers': ['Consensus Point',
                                     'What The Practitioner Reported',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Utilization decides whether neocloud rentals pay',
                                   '$25K H100 at $2.30/hr earns about $55/day and 28% CAGR at 100% '
                                   'utilization',
                                   'At or below roughly 55% utilization, broad stocks beat the GPU rental '
                                   'business',
                                   'Caleb Writes Code ([9u2hCf8FlW0 @ 00:00:50])'],
                                  ['Stalled GPUs keep billing the renter regardless',
                                   'Large-scale GPU workloads are far less forgiving and stalled GPUs '
                                   'still bill',
                                   "Saying 'we need more GPUs' is incomplete without topology and "
                                   'throughput analysis',
                                   'The gpuMaster ([_tV0Elv_jIk @ 00:01:29])'],
                                  ['Neoclouds undercut hyperscalers on GPU pricing',
                                   'Neoclouds run up to 30-50% cheaper depending on the contract length '
                                   'signed',
                                   'Benchmark your own workload during a roughly week-long POC before '
                                   'signing anything',
                                   'Toronto Machine Learning Society (TMLS) ([_oWJ0t-RW7o @ 00:06:30])'],
                                  ['Scheduler quality converts directly into daily cash',
                                   'Default Kubernetes near 45% utilization versus about 85% with '
                                   'workload-aware design',
                                   'On a 10,000-GPU fleet that utilization gap is worth roughly $150k per '
                                   'day',
                                   'Codemia ([a_zou7QahAo @ 00:04:38])'],
                                  ['Multi-provider sourcing is now the default posture',
                                   'Capacity, cost and no single point of failure drive multi-provider '
                                   'strategy',
                                   "Meta's multi-billion-dollar CoreWeave and Nebius deals signal the "
                                   'market shift underway',
                                   'SkyPilot ([uwLkrJb5pEA @ 00:01:47])'],
                                  ['Single-cloud silos destroy buyer negotiating leverage',
                                   'Lock-in reduces availability, raises outage exposure and lowers '
                                   'negotiation leverage overall',
                                   'Use credible alternative providers to win better deals because choice '
                                   'is power',
                                   'USENIX ([3Edw88b1bRg @ 00:01:22])'],
                                  ['AI platforms will end up hybrid and heterogeneous',
                                   'Best-of-breed plays are complex; Nebius and CoreWeave lead a '
                                   'two-provider shortlist',
                                   'Judge platform readiness against twelve months out, as usage can scale '
                                   'toward millions',
                                   'Cloud Computing Insider ([mAgWtefgeP8 @ 00:13:14])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['On the supply side, the build math gets heavier fast. Caleb Writes Code '
                              'notes that a GPT-3-class model needs more than 350GB of VRAM, so a serious '
                              'customer needs at least 8 H100s, which puts the minimum rentable unit at '
                              '$250K: $200K for cards and $50K opex; eBay cards are risky, and supplier '
                              'relationships act as the moat [9u2hCf8FlW0 @ 00:03:59]. Scaling is '
                              'non-linear: efficiency drops to 77% at 8 GPUs under model parallelism and '
                              '74% at 512 per an NVIDIA paper, fragmented nodes create bottlenecks, and '
                              'scheduling turns into Tetris. CUDA and ROCm workloads are not '
                              'interchangeable, so a mixed fleet carries heterogeneity risk. On financing, '
                              'Caleb Writes Code points out that resale value stays near purchase price, '
                              'which enables asset-backed loans, while contracts trade a discount for '
                              'flexibility [9u2hCf8FlW0 @ 00:13:55]. Codemia sizes a 10,000-GPU fleet at '
                              'about $400M across 1,250 hosts in 32 racks, with cards renting at $20 to '
                              '$40 per hour [a_zou7QahAo @ 00:03:35]. Reliability becomes a sales weapon: '
                              "Deok Filho of CoreWeave cites Meta's figure of roughly 8 hours between "
                              'interruptions per 1,000 GPUs and claims CoreWeave runs 70 to 80 hours for '
                              'an equivalent job size [vdP0fhqpYZs @ 00:06:03].',
                              'On the buy side, The Code Notebook lays out the pricing ladder: flex start '
                              'runs about half price, commitments go down to about 45%, and spot goes down '
                              'to about 9% [IZtzUfhm8LU @ 00:06:06]. The commitment rule is simple: '
                              'utilization must exceed 1 minus the discount. With $10 on-demand, a $4.50 '
                              'commit costs $5 per used hour at 90% busy but $45 per used hour at 10% '
                              "busy, hence 'Never commit to your peak.' Spot carries a different tax: AWS "
                              'gives 2 minutes of warning and Azure gives 30 seconds. In a 2,000-run '
                              'simulation of a 100-hour job with interruptions every 8 hours, 6-minute '
                              'restarts, 72-second saves and a 70% discount, never saving produced '
                              '2,203,564 hours, saving every 30 minutes finished in 109 hours at a cost of '
                              '32.6 against 100 on-demand, and saving every 30 seconds took 345 hours at '
                              '103.5. The optimal save interval, the square root of 2 times MTBI times '
                              'save cost, lands near 34 minutes [IZtzUfhm8LU @ 00:10:20]. The USENIX '
                              'SkyPilot team measured the spread that makes brokering pay: up to 3x on '
                              'on-demand pricing and up to 9x on spot across zones [3Edw88b1bRg @ '
                              "00:07:21]. Codemia's scheduler polls for spot reclaim every 5 seconds "
                              'against the 2-minute warning [a_zou7QahAo @ 00:29:02].',
                              'The brokerage layer itself is mostly scheduling and provisioning plumbing. '
                              "SkyPilot's Zhanghao Wu and Kevin Mingtarja run `sky launch --gpus B200` for "
                              'a dev box, bump `num_nodes 16` to scale out, and use `sky jobs launch` so a '
                              'GPU failure, node maintenance, quota reclamation or spot preemption is '
                              'recovered hands-free; in their demo the optimizer picked the cheapest '
                              'option, an already-provisioned CoreWeave H100 node [uwLkrJb5pEA @ '
                              '00:08:31]. At Meta FAIR, Lucca Bertoncini found a 10-step setup lost about '
                              '90% of users by step 2 and 98% by the end, and 2FA on every cluster drove '
                              'adoption to 0%, so the team shipped a single binary that writes the '
                              'configuration and holds SSH/ET tunnels in tmux with 2FA done once, across '
                              'clusters of roughly 20K GPUs each [Pas2NE76220 @ 00:05:54]. Seung Jin Yang '
                              'of SkyPilot replaces spreadsheets and node taints with a real queue, '
                              'priority preemption backed by checkpoints, Slack alerts on preemption, and '
                              "quota borrowing that lets a team grab 256 GPUs idling in another team's "
                              'queue [tb-Yg8PNXT4 @ 00:05:02]. Alex from Nebius shows SkyPilot task '
                              'definitions running 3 to 4x shorter than the Kubernetes equivalent, driving '
                              'a 2-node, 16-H100 Llama 3.1 fine-tune with TorchTune [QLSYI5Ali8Y @ '
                              '00:02:24].'],
               'table': {'caption': 'Exact numbers, formulas and commands practitioners run in neocloud '
                                    'brokerage',
                         'headers': ['Mechanic',
                                     'Exact Numbers Or Command',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Single H100 rental unit economics baseline',
                                   '$25K card plus $5K opex, $2.30/hr, about $80K over 4 years',
                                   'Reach full utilization for 28% CAGR; at or below 55%, stocks win',
                                   'Caleb Writes Code ([9u2hCf8FlW0 @ 00:00:50])'],
                                  ['Commitment break-even rule for reserved GPUs',
                                   'Utilization must exceed 1 minus the discount on list price',
                                   'A $4.50 commit on $10 on-demand costs $45 per used hour at 10% busy',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:07:33])'],
                                  ['Checkpoint interval for interrupted spot training runs',
                                   'Square root of 2 times MTBI times save cost, about 34 minutes',
                                   'Saving every 30 minutes cost 32.6 versus 100 on-demand in simulation',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:10:20])'],
                                  ['Managed job recovery across clouds and neoclouds',
                                   'sky jobs launch with automatic node-failure and preemption recovery '
                                   'built in',
                                   'Avoid 3 a.m. pages when GPUs fail, nodes drain or spot is reclaimed',
                                   'SkyPilot ([uwLkrJb5pEA @ 00:08:31])'],
                                  ['Gang placement scoring for multi-node training jobs',
                                   'Bandwidth 40%, compactness 25%, rack penalty 25%, fragmentation 10%, '
                                   'under 100ms',
                                   'Pair with an etcd 60s lease and two-phase commit to place gangs',
                                   'Codemia ([a_zou7QahAo @ 00:13:52])'],
                                  ['Quota floors and burst allowances between teams',
                                   'Reserved floor of 400 cards plus a burst allowance of 600 cards',
                                   'Enforce dominant-resource fairness across teams sharing the same GPU '
                                   'fleet',
                                   'Codemia ([a_zou7QahAo @ 00:20:40])'],
                                  ['MIG slicing to lift idle card utilization',
                                   'Up to 7 slices per card, taking utilization from 8% to over 60%',
                                   'Carve lightly used cards into slices instead of leaving whole GPUs '
                                   'idle',
                                   'Codemia ([a_zou7QahAo @ 00:32:20])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What The Brokers Do Before Spending A Dollar',
                           'body': 'The operators who win on GPU arbitrage test before they sign, request '
                                   'capabilities instead of clusters, and price work rather than sticker '
                                   'hours.',
                           'items': ['Run your own end-to-end workload in a roughly week-long POC before '
                                     'signing, and use multicloud optionality as negotiating leverage '
                                     '[Toronto Machine Learning Society (TMLS) — _oWJ0t-RW7o @ 00:07:47].',
                                     'Never build a plan around a chip that is only announced, and always '
                                     'test your own workload before you sign anything [The Code Notebook — '
                                     'IZtzUfhm8LU @ 00:04:26].',
                                     'Request intent, not hardware: a `network_tier: best` field gets '
                                     'translated to EFA or GPUDirect per cloud, with raw pod specs kept as '
                                     'an escape hatch [CNCF [Cloud Native Computing Foundation] — '
                                     '-czZES1U_Us @ 00:12:15].',
                                     'Declare requirements, not clusters: the deployment asked for 8 GPUs '
                                     'with at least 140GB VRAM on vLLM, never named the cluster, and '
                                     'placed 2 replicas across AWS and CoreWeave [Modelplane — Wq9Ov_jlxlM '
                                     '@ 00:03:54].']},
               'sop_steps': [{'step': 1,
                              'title': 'Model Utilization Break-Even',
                              'action': 'Price the card, opex and hourly rate, then compute returns at '
                                        'realistic utilization rather than full occupancy.',
                              'detail': 'Use the baseline of a $25K H100 plus $5K opex rented at $2.30/hr, '
                                        'which returns a 28% CAGR at 100% utilization while broad stocks '
                                        'win at or below roughly 55% [Caleb Writes Code — 9u2hCf8FlW0 @ '
                                        '00:01:22].'},
                             {'step': 2,
                              'title': 'Benchmark Shortlisted Neoclouds',
                              'action': 'Run your own workload on each candidate provider before '
                                        'committing any contract.',
                              'detail': 'Run a roughly week-long POC to confirm end-to-end performance, '
                                        'since neoclouds can be 30-50% cheaper depending on contract '
                                        'length and multicloud gives negotiating leverage [Toronto Machine '
                                        'Learning Society (TMLS) — _oWJ0t-RW7o @ 00:07:47].'},
                             {'step': 3,
                              'title': 'Size Commitments Below Peak',
                              'action': 'Commit only the capacity you will keep busier than the break-even '
                                        'line.',
                              'detail': 'Commit only when utilization will exceed 1 minus the discount; a '
                                        '$4.50 commit on $10 on-demand costs $5 per used hour at 90% busy '
                                        'and $45 at 10% busy, so never commit to your peak [The Code '
                                        'Notebook — IZtzUfhm8LU @ 00:07:52].'},
                             {'step': 4,
                              'title': 'Launch Through A Broker With Checkpointed Recovery',
                              'action': 'Define the job once in YAML, launch as a managed job, and mount '
                                        'checkpoints to durable storage.',
                              'detail': 'Launch with `sky jobs launch`, mount checkpoints (the demo used '
                                        'S3 at /checkpoints), and let SkyPilot recover from GPU failure, '
                                        'node maintenance, quota reclamation or spot preemption hands-free '
                                        '[SkyPilot — uwLkrJb5pEA @ 00:08:31].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["The first split is whether to own GPUs or arbitrage other people's "
                              'capacity. Caleb Writes Code runs the owner math cold: a $25,000 H100 plus '
                              '$5,000 opex, a four-year life, and $2.30 per hour yielding roughly $55 a '
                              "day, about $20,000 a year and $80,000 over the card's life, a 28% CAGR only "
                              'at 100% utilization [9u2hCf8FlW0 @ 00:00:50]. Drop to roughly 55% '
                              'utilization and broad stocks beat the neocloud, and because the market is '
                              'commoditized, any premium price simply bleeds utilization [9u2hCf8FlW0 @ '
                              '00:01:22]. Romil Bhardwaj attacks from the buyer side: the long tail of '
                              'neoclouds runs two to three times cheaper but is less reliable, and '
                              'neoclouds can land 30 to 50% cheaper depending on how long a contract you '
                              'sign [_oWJ0t-RW7o @ 00:06:30]. Cloud Computing Insider frames the same gap '
                              'structurally, arguing hyperscalers charge more for AI because they were '
                              'built for all IT and are less efficient at it [mAgWtefgeP8 @ 00:01:49]. The '
                              'owner needs full racks and steady renters; the broker profits when that '
                              "owner's margin collapses under competition. Both camps agree price is the "
                              'battlefield, but they sit on opposite sides of the same spread, and an '
                              'operator has to decide which side of that spread pays the bills before '
                              'buying a single card.',
                              'The second fight is concentration versus brokerage. Cloud Computing Insider '
                              'will name names, saying if you look at two providers it is probably Nebius '
                              'and CoreWeave, with CoreWeave as the gold standard, yet the same speaker '
                              'refuses to back a single provider and warns that a best-of-breed play will '
                              "be complex and heterogeneous [mAgWtefgeP8 @ 00:13:14]. CoreWeave's Deok "
                              'Filho pushes concentration hard: Meta reports about eight hours between '
                              'interruptions per 1,000 GPUs, CoreWeave claims 70 to 80 hours for an '
                              "equivalent job size, and the pitch closes with 'It just will run better on "
                              "us' [vdP0fhqpYZs @ 00:06:03]. The Sky Computing team at USENIX argues the "
                              'opposite, that silos cut availability and negotiation leverage because '
                              'choice is power, and that clouds will never commoditize themselves through '
                              'standardization, so a broker must sit on top [3Edw88b1bRg @ 00:01:22]. '
                              'Modelplane adds a sharper twist: the multi-cloud layer is too important to '
                              'be proprietary, and clusters should be treated as one fleet where a '
                              'deployment never names the cluster at all [Wq9Ov_jlxlM @ 00:02:46]. '
                              'Single-vendor depth buys reliability numbers and integrated tooling; '
                              "brokerage buys leverage and failover. Neither camp disputes the other's "
                              'data, only which risk an operator should eat.',
                              'The third split is how to buy time on the iron. Caleb Writes Code treats '
                              'contracts as a plain trade of discount for flexibility [9u2hCf8FlW0 @ '
                              "00:11:30]. The Code Notebook maps the buyer's full ladder: flex start at "
                              'about half price, commitments down to about 45%, spot down to about 9%, and '
                              'a hard rule that a commitment only wins when utilization exceeds one minus '
                              "the discount, summed up as 'Never commit to your peak' [IZtzUfhm8LU @ "
                              '00:07:52]. The USENIX SkyPilot team bets on the spread instead, measuring '
                              'up to three times difference in on-demand pricing and up to nine times in '
                              'spot pricing across zones, then routing jobs with an ILP solver that '
                              'minimizes total cost or time [3Edw88b1bRg @ 00:07:21]. Underneath the '
                              'pricing sits a cluster-manager argument. Romil Bhardwaj says Slurm hits '
                              'isolation and serving limits, Kubernetes brings a steep learning curve with '
                              'no SSH and no gang scheduling, and raw VMs dump key management and manual '
                              'orchestration on the team, so the recommendation is managed Kubernetes plus '
                              'VMs [_oWJ0t-RW7o @ 00:11:41]. CoreWeave answers by running Slurm on '
                              'Kubernetes through SUNK, while Meta FAIR still flags schedulers stacked on '
                              'schedulers as an open problem. Each answer reshapes how much of the '
                              'discount actually reaches the bottom line.'],
               'table': {'caption': 'Side-by-side playbooks where neocloud and brokerage practitioners '
                                    'split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Own GPUs versus rent the price spread',
                                   'Buy an H100 at $25K, earning 28% CAGR only at 100% utilization',
                                   'Rent neocloud capacity 30 to 50% cheaper depending on contract length',
                                   'Caleb Writes Code ([9u2hCf8FlW0 @ 00:00:50]); Toronto Machine Learning '
                                   'Society (TMLS) ([_oWJ0t-RW7o @ 00:06:30])'],
                                  ['Single best provider versus a heterogeneous provider mix',
                                   'Shortlist Nebius and CoreWeave as the two strongest picks',
                                   'Expect a complex, heterogeneous best-of-breed stack across many '
                                   'providers',
                                   'Cloud Computing Insider ([mAgWtefgeP8 @ 00:12:47])'],
                                  ['Vendor reliability depth versus brokered cross-cloud failover',
                                   'CoreWeave claims 70 to 80 hours between interruptions per 1,000 GPUs',
                                   'Broker across clouds because choice is power in every negotiation',
                                   'SkyPilot ([vdP0fhqpYZs @ 00:06:03]); USENIX ([3Edw88b1bRg @ '
                                   '00:01:22])'],
                                  ['Committed reservations versus chasing spot price spreads',
                                   'Commit only when utilization exceeds one minus the discount offered',
                                   'Chase up to nine times spot spreads across zones with ILP',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:07:33]); USENIX ([3Edw88b1bRg @ '
                                   '00:07:21])'],
                                  ['Slurm versus Kubernetes as the cluster control plane',
                                   'Run Slurm on Kubernetes through SUNK with backfill and priority '
                                   'scheduling',
                                   'Managed Kubernetes plus VMs because Slurm limits isolation and serving',
                                   'SkyPilot ([vdP0fhqpYZs @ 00:01:56]); Toronto Machine Learning Society '
                                   '(TMLS) ([_oWJ0t-RW7o @ 00:11:41])'],
                                  ['Proprietary integrated stack versus an open fleet layer',
                                   'Use the vendor-integrated stack that claims jobs run better there',
                                   'Keep the multi-cloud layer open, Apache-licensed and built on '
                                   'Crossplane',
                                   'SkyPilot ([vdP0fhqpYZs @ 00:15:59]); Modelplane ([Wq9Ov_jlxlM @ '
                                   '00:02:46])'],
                                  ['Which cost metric should drive GPU procurement decisions',
                                   'Market rate cards from $1 to $5 per GPU-hour set pricing',
                                   'Track cost per training run, per token and per request instead',
                                   'Caleb Writes Code ([9u2hCf8FlW0 @ 00:00:32]); The gpuMaster '
                                   '([_tV0Elv_jIk @ 00:07:32])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is cheap spot capacity run without discipline. The '
                              'Code Notebook simulated a 100-hour job with interruptions every eight '
                              'hours, a six-minute restart, 72 seconds per save, 2,000 runs, and a 70% '
                              'discount: never saving stretched the job to 2,203,564 hours, saving every '
                              '30 minutes finished in 109 hours at a cost of 32.6 against 100 on-demand, '
                              'and saving every 30 seconds ballooned to 345 hours at 103.5 [IZtzUfhm8LU @ '
                              '00:09:58]. Their verdict is that spot without checkpoints is not cheap, '
                              'saving too often costs more than not using spot at all, and the optimal '
                              'interval is the square root of two times mean time between interruptions '
                              'times save cost, about 34 minutes [IZtzUfhm8LU @ 00:10:20]. The same '
                              'speaker notes the warning windows are brutal: AWS gives two minutes and '
                              "Azure gives 30 seconds. Codemia's scheduler design polls the two-minute "
                              'reclaim notice every five seconds and tells operators to give each job a '
                              'random offset so checkpoint timers do not line up, because correlated '
                              "failures are where these systems break [a_zou7QahAo @ 00:31:58]. SkyPilot's "
                              'managed jobs layer pitches hands-free recovery from GPU failure, node '
                              'maintenance, quota reclamation, and spot preemption so nobody gets paged at '
                              '3:00 a.m. [uwLkrJb5pEA @ 00:08:31].',
                              "The second trap is paying for GPUs that are not doing work. The gpuMaster's "
                              'core warning is that stalled GPUs still bill, and that large-scale GPU '
                              'workloads are far less forgiving [_tV0Elv_jIk @ 00:01:29]. Caleb Writes '
                              'Code measured the scaling tax: efficiency drops to 77% at eight GPUs under '
                              'model parallelism and 74% at 512, and fragmented nodes turn scheduling into '
                              'Tetris [9u2hCf8FlW0 @ 00:05:04]. Seung Jin Yang of SkyPilot debugged the '
                              'failures researchers actually hit when they ask why their job is not '
                              'scheduled: fragmentation, rogue taints left by agents, a request for 128 '
                              'CPUs on nodes with only about 126.32 allocatable that shows up as blocked, '
                              'and quota oversubscription where 12 GPUs are promised against 8, which, in '
                              'their words, can happen in practice [tb-Yg8PNXT4 @ 00:13:27]. Codemia '
                              'prices the gap: default Kubernetes gets about 45% utilization, a '
                              'workload-aware design about 85%, a spread worth roughly $150,000 per day on '
                              'a 10,000-GPU fleet [a_zou7QahAo @ 00:04:38]. The same speaker caps '
                              'defragmentation at 5% per hour, because the cure has to stay cheaper than '
                              'the disease. Every one of these leaks lands as billed GPU hours with zero '
                              'training progress behind them.',
                              'The third trap is the balance sheet. Tulipnomics walks through the telecom '
                              'bust as a template: Lucent promised $6.7 billion in customer credit by '
                              'September 2000, with Nortel and Cisco running similar programs, summed up '
                              "as the seller lending the buyer the money to buy the seller's own products "
                              '[71yv5MpdX1s @ 00:02:24]. When capacity flooded in, a New York to Los '
                              'Angeles circuit fell from $1.8 million a year to under $150,000, telecom '
                              'made up over half of 2002 bond defaults with 21 cents of recovery, and the '
                              "same channel now counts roughly $36 billion of CoreWeave debt plus Moody's "
                              'tally of $1.2 trillion in lease commitments, $820 billion not yet started '
                              '[71yv5MpdX1s @ 00:09:54]. theCUBE flags the operator-level exposure: a 2024 '
                              'net loss of $863.4 million, NVIDIA dependence, and over 60% of revenue from '
                              'Microsoft, with the warning that sustaining profitability is going to be '
                              'another challenge [VjfoLNKgo3A @ 00:03:51]. Caleb Writes Code offers the '
                              'counterweight, noting that GPU resale value stays near purchase price, '
                              "which enables asset-backed loans [9u2hCf8FlW0 @ 00:13:55]. Tulipnomics' own "
                              'coda cuts both ways: the cable was never the problem, but new owners bought '
                              'the networks for a fraction of what they cost to build, and the banks lost '
                              'money on the fiber.'],
               'table': {'caption': 'Firsthand failure modes with the numbers practitioners measured',
                         'headers': ['Failure Mode',
                                     'Firsthand Number',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Running spot capacity with no checkpoints at all',
                                   'A 100-hour job stretched to 2,203,564 hours in simulation',
                                   'Save roughly every 34 minutes to cut cost to 32.6',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:09:12])'],
                                  ['Over-checkpointing spot jobs far too frequently',
                                   'Saving every 30 seconds took 345 hours at cost 103.5',
                                   'Saving too often costs more than skipping spot entirely',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:10:20])'],
                                  ['Signing a reservation sized to peak demand',
                                   'A $4.50 commit costs $45 per used hour at 10% busy',
                                   'Commit only when utilization exceeds one minus the discount',
                                   'The Code Notebook ([IZtzUfhm8LU @ 00:07:07])'],
                                  ['Owned cards sitting at low rental utilization',
                                   'At or below roughly 55% utilization, broad stocks beat the neocloud',
                                   'Model returns at real utilization, never at full 100% occupancy',
                                   'Caleb Writes Code ([9u2hCf8FlW0 @ 00:01:22])'],
                                  ['Scheduler blind spots blocking researcher jobs silently',
                                   'Requesting 128 CPUs against about 126.32 allocatable shows as blocked',
                                   'Audit allocatable resources, rogue taints and quota oversubscription '
                                   'first',
                                   'SkyPilot ([tb-Yg8PNXT4 @ 00:11:00])'],
                                  ['Leaving default Kubernetes scheduling on a large fleet',
                                   'About 45% utilization versus about 85% with workload-aware design',
                                   'That gap is worth roughly $150,000 per day on 10,000 GPUs',
                                   'Codemia ([a_zou7QahAo @ 00:04:38])'],
                                  ['Painful multi-step onboarding to shared GPU clusters',
                                   'A ten-step setup lost about 98% of users by the end',
                                   'Ship one binary that writes config and holds tunnels open',
                                   'SkyPilot ([Pas2NE76220 @ 00:04:51])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Before Scaling GPU Spend',
                           'body': 'Every item below maps to a loss or bottleneck a practitioner measured '
                                   'or debugged firsthand. Do not add nodes, sign commits, or flip jobs to '
                                   'spot until each one is checked.',
                           'items': ['Checkpoint interval set near the square-root optimum, about 34 '
                                     'minutes in the simulation, before any spot job runs [The Code '
                                     'Notebook — IZtzUfhm8LU @ 00:10:20].',
                                     'Commitment sized below peak and signed only where utilization clears '
                                     'one minus the discount [The Code Notebook — IZtzUfhm8LU @ 00:07:52].',
                                     'Own workload benchmarked end to end in a roughly week-long POC '
                                     'before any contract is signed [Toronto Machine Learning Society '
                                     '(TMLS) — _oWJ0t-RW7o @ 00:07:47].',
                                     'Provider interruption rate per 1,000 GPUs confirmed against the '
                                     'reported benchmarks of about 8 hours at Meta and 70 to 80 hours at '
                                     'CoreWeave [SkyPilot — vdP0fhqpYZs @ 00:06:03].']}}],
 'pull_quote': '"Spot without checkpoints is not cheap." — The Code Notebook (IZtzUfhm8LU @ 00:09:35).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Test your own workload before you sign anything, and never build a plan around a '
                      'chip that is only announced [The Code Notebook — IZtzUfhm8LU @ 00:04:26].',
                      'Run a roughly week-long POC on each candidate neocloud and use the multicloud '
                      'option as negotiating leverage on price [Toronto Machine Learning Society (TMLS) — '
                      '_oWJ0t-RW7o @ 00:07:33].',
                      'Spin up a dev box with sky launch --gpus B200, scale out with num_nodes 16, and '
                      'move long runs to sky jobs launch for automatic node-failure recovery [SkyPilot — '
                      'uwLkrJb5pEA @ 00:05:36].',
                      'Replace spreadsheets and node taints with an actual queuing setup using priority '
                      'preemption, checkpoints, and real-time Slack alerts on preemption [SkyPilot — '
                      'tb-Yg8PNXT4 @ 00:04:12].',
                      'Mount S3 checkpoints at /checkpoints and cache the container image on NFS so '
                      'preempted Slurm jobs resume fast [SkyPilot — uwLkrJb5pEA @ 00:19:36].',
                      'Scale inference to zero when idle; the simulation dropped 24 GPU-hours to 4.04, an '
                      '83% cut, at 3.9 cold starts per day of 60 seconds each [The Code Notebook — '
                      'IZtzUfhm8LU @ 00:12:59].'],
 'statutory_citations': [{'title': 'Caleb Writes Code — The Economics of Neoclouds [00:01:22]',
                          'url': 'https://www.youtube.com/watch?v=9u2hCf8FlW0&t=82s',
                          'relevance': 'Primary practitioner testimony on H100 unit economics and the '
                                       'utilization break-even for neocloud owners.'},
                         {'title': 'The Code Notebook — Why Cheap Spot GPUs End Up Costing MORE (The '
                                   'Checkpoint Mistake) [00:09:35]',
                          'url': 'https://www.youtube.com/watch?v=IZtzUfhm8LU&t=575s',
                          'relevance': 'Primary practitioner testimony on spot checkpoint economics and '
                                       'commitment break-even math.'},
                         {'title': "USENIX — NSDI '23 - SkyPilot: An Intercloud Broker for Sky Computing "
                                   '[00:07:21]',
                          'url': 'https://www.youtube.com/watch?v=3Edw88b1bRg&t=441s',
                          'relevance': 'Primary practitioner testimony on cross-cloud price spreads and '
                                       'intercloud brokerage architecture.'},
                         {'title': 'Tulipnomics — The Telecom Bust: The Debt That Built the Internet '
                                   '[00:02:24]',
                          'url': 'https://www.youtube.com/watch?v=71yv5MpdX1s&t=144s',
                          'relevance': 'Primary practitioner testimony on vendor financing, capacity '
                                       'gluts, and AI infrastructure debt parallels.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '9u2hCf8FlW0',
                       'title': 'The Economics of Neoclouds',
                       'channel': 'Caleb Writes Code',
                       'author': 'Caleb Writes Code',
                       'text': 'So, right off the bat, you realize that utilization is a key metric to '
                               'consider when you run Neo clouds.',
                       'tip': 'So, right off the bat, you realize that utilization is a key metric to '
                              'consider when you run Neo clouds.',
                       'timestamp': 82,
                       'timestamp_seconds': 82,
                       'timestamp_label': '[00:01:22]',
                       'url': 'https://www.youtube.com/watch?v=9u2hCf8FlW0&t=82s',
                       'markdown': '[00:01:22](https://www.youtube.com/watch?v=9u2hCf8FlW0&t=82s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mAgWtefgeP8',
                       'title': 'Top 5 NeoClouds Explained: CoreWeave, Nebius, Crusoe, Lambda, Fluidstack',
                       'channel': 'Cloud Computing Insider',
                       'author': 'Cloud Computing Insider',
                       'text': 'So, consider the fact that your best of breed play is going to be complex '
                               "and it's going to be heterogeneous.",
                       'tip': 'So, consider the fact that your best of breed play is going to be complex '
                              "and it's going to be heterogeneous.",
                       'timestamp': 794,
                       'timestamp_seconds': 794,
                       'timestamp_label': '[00:13:14]',
                       'url': 'https://www.youtube.com/watch?v=mAgWtefgeP8&t=794s',
                       'markdown': '[00:13:14](https://www.youtube.com/watch?v=mAgWtefgeP8&t=794s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VjfoLNKgo3A',
                       'title': 'Ep. 36 GPUaaS Explained: Why CoreWeave and Others Are Fueling the Next '
                                'Cloud Revolution | AI Insight',
                       'channel': 'SiliconANGLE theCUBE',
                       'author': 'SiliconANGLE theCUBE',
                       'text': 'Sustaining profitability is going to be another challenge for them.',
                       'tip': 'Sustaining profitability is going to be another challenge for them.',
                       'timestamp': 231,
                       'timestamp_seconds': 231,
                       'timestamp_label': '[00:03:51]',
                       'url': 'https://www.youtube.com/watch?v=VjfoLNKgo3A&t=231s',
                       'markdown': '[00:03:51](https://www.youtube.com/watch?v=VjfoLNKgo3A&t=231s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '71yv5MpdX1s',
                       'title': 'The Telecom Bust: The Debt That Built the Internet',
                       'channel': 'Tulipnomics',
                       'author': 'Tulipnomics',
                       'text': "The seller lends the buyer the money to buy the seller's own products.",
                       'tip': "The seller lends the buyer the money to buy the seller's own products.",
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=71yv5MpdX1s&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=71yv5MpdX1s&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_tV0Elv_jIk',
                       'title': 'Bare-Metal GPU Clouds vs Hyperscalers: Why startups are fleeing AWS and '
                                'Azure?',
                       'channel': 'The gpuMaster',
                       'author': 'The gpuMaster',
                       'text': "So saying, 'We need more GPUs,' is incomplete.",
                       'tip': "So saying, 'We need more GPUs,' is incomplete.",
                       'timestamp': 287,
                       'timestamp_seconds': 287,
                       'timestamp_label': '[00:04:47]',
                       'url': 'https://www.youtube.com/watch?v=_tV0Elv_jIk&t=287s',
                       'markdown': '[00:04:47](https://www.youtube.com/watch?v=_tV0Elv_jIk&t=287s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Pas2NE76220',
                       'title': 'SkyPilot at 100k+ GPU Scale at Meta AI (FAIR) - Lucca Bertoncini (Meta)',
                       'channel': 'SkyPilot',
                       'author': 'SkyPilot',
                       'text': 'Uh so yeah 10 steps like you lost like 98% of the users.',
                       'tip': 'Uh so yeah 10 steps like you lost like 98% of the users.',
                       'timestamp': 291,
                       'timestamp_seconds': 291,
                       'timestamp_label': '[00:04:51]',
                       'url': 'https://www.youtube.com/watch?v=Pas2NE76220&t=291s',
                       'markdown': '[00:04:51](https://www.youtube.com/watch?v=Pas2NE76220&t=291s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tb-Yg8PNXT4',
                       'title': 'Why are my GPUs not getting scheduled - Seung Jin Yang (SkyPilot)',
                       'channel': 'SkyPilot',
                       'author': 'SkyPilot',
                       'text': 'This is what we in the industry call fragmentation.',
                       'tip': 'This is what we in the industry call fragmentation.',
                       'timestamp': 540,
                       'timestamp_seconds': 540,
                       'timestamp_label': '[00:09:00]',
                       'url': 'https://www.youtube.com/watch?v=tb-Yg8PNXT4&t=540s',
                       'markdown': '[00:09:00](https://www.youtube.com/watch?v=tb-Yg8PNXT4&t=540s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_oWJ0t-RW7o',
                       'title': 'Building Multi-Cloud GenAI Platforms Without the Pain | Romil Bhardwaj, '
                                'SkyPilot',
                       'channel': 'Toronto Machine Learning Society (TMLS)',
                       'author': 'Toronto Machine Learning Society (TMLS)',
                       'text': 'Whereas Neoclouds can be up to like 30 to 50% cheaper depending on how uh '
                               "long of a contract you're signing.",
                       'tip': 'Whereas Neoclouds can be up to like 30 to 50% cheaper depending on how uh '
                              "long of a contract you're signing.",
                       'timestamp': 390,
                       'timestamp_seconds': 390,
                       'timestamp_label': '[00:06:30]',
                       'url': 'https://www.youtube.com/watch?v=_oWJ0t-RW7o&t=390s',
                       'markdown': '[00:06:30](https://www.youtube.com/watch?v=_oWJ0t-RW7o&t=390s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IZtzUfhm8LU',
                       'title': 'Why Cheap Spot GPUs End Up Costing MORE (The Checkpoint Mistake)',
                       'channel': 'The Code Notebook',
                       'author': 'The Code Notebook',
                       'text': 'Spot without checkpoints is not cheap.',
                       'tip': 'Spot without checkpoints is not cheap.',
                       'timestamp': 575,
                       'timestamp_seconds': 575,
                       'timestamp_label': '[00:09:35]',
                       'url': 'https://www.youtube.com/watch?v=IZtzUfhm8LU&t=575s',
                       'markdown': '[00:09:35](https://www.youtube.com/watch?v=IZtzUfhm8LU&t=575s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3Edw88b1bRg',
                       'title': "NSDI '23 - SkyPilot: An Intercloud Broker for Sky Computing",
                       'channel': 'USENIX',
                       'author': 'USENIX',
                       'text': "And we see that there's a up to three times difference for on-demand "
                               'pricing and up to nine times difference for spot pricing.',
                       'tip': "And we see that there's a up to three times difference for on-demand "
                              'pricing and up to nine times difference for spot pricing.',
                       'timestamp': 441,
                       'timestamp_seconds': 441,
                       'timestamp_label': '[00:07:21]',
                       'url': 'https://www.youtube.com/watch?v=3Edw88b1bRg&t=441s',
                       'markdown': '[00:07:21](https://www.youtube.com/watch?v=3Edw88b1bRg&t=441s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uwLkrJb5pEA',
                       'title': 'SkyPilot: Your AI Infra, Frontier Capabilities - Zhanghao Wu, Kevin '
                                'Mingtarja (SkyPilot)',
                       'channel': 'SkyPilot',
                       'author': 'SkyPilot',
                       'text': 'For example, a GPU failure, a node maintenance, or quota reclamation, spot '
                               'preemption, SkyPilot handles the whole recovery with your hands free.',
                       'tip': 'For example, a GPU failure, a node maintenance, or quota reclamation, spot '
                              'preemption, SkyPilot handles the whole recovery with your hands free.',
                       'timestamp': 511,
                       'timestamp_seconds': 511,
                       'timestamp_label': '[00:08:31]',
                       'url': 'https://www.youtube.com/watch?v=uwLkrJb5pEA&t=511s',
                       'markdown': '[00:08:31](https://www.youtube.com/watch?v=uwLkrJb5pEA&t=511s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a_zou7QahAo',
                       'title': 'GPU Cluster Scheduler System Design | Gang Scheduling, Topology, '
                                'Preemption',
                       'channel': 'Codemia',
                       'author': 'Codemia',
                       'text': 'Correlated failures are where these systems break.',
                       'tip': 'Correlated failures are where these systems break.',
                       'timestamp': 1918,
                       'timestamp_seconds': 1918,
                       'timestamp_label': '[00:31:58]',
                       'url': 'https://www.youtube.com/watch?v=a_zou7QahAo&t=1918s',
                       'markdown': '[00:31:58](https://www.youtube.com/watch?v=a_zou7QahAo&t=1918s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vdP0fhqpYZs',
                       'title': 'Training At Scale With Confidence (SkyPilot Integration w/ CoreWeave '
                                'SUNK) - Deok Filho (CoreWeave)',
                       'channel': 'SkyPilot',
                       'author': 'SkyPilot',
                       'text': 'We have addressed them and our number is around 70 to 80 hours for a '
                               'equivalent job size, 1,000 GPUs.',
                       'tip': 'We have addressed them and our number is around 70 to 80 hours for a '
                              'equivalent job size, 1,000 GPUs.',
                       'timestamp': 363,
                       'timestamp_seconds': 363,
                       'timestamp_label': '[00:06:03]',
                       'url': 'https://www.youtube.com/watch?v=vdP0fhqpYZs&t=363s',
                       'markdown': '[00:06:03](https://www.youtube.com/watch?v=vdP0fhqpYZs&t=363s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-czZES1U_Us',
                       'title': 'Building Multi-cloud AI Platforms on Kubernetes Without the Pain - Romil '
                                'Bhardwaj, SkyPilot',
                       'channel': 'CNCF [Cloud Native Computing Foundation]',
                       'author': 'CNCF [Cloud Native Computing Foundation]',
                       'text': "And there's like no fleet-wide view.",
                       'tip': "And there's like no fleet-wide view.",
                       'timestamp': 791,
                       'timestamp_seconds': 791,
                       'timestamp_label': '[00:13:11]',
                       'url': 'https://www.youtube.com/watch?v=-czZES1U_Us&t=791s',
                       'markdown': '[00:13:11](https://www.youtube.com/watch?v=-czZES1U_Us&t=791s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Wq9Ov_jlxlM',
                       'title': 'Run One AI Model Across Multiple Clouds and GPUs (Modelplane)',
                       'channel': 'Modelplane',
                       'author': 'Modelplane',
                       'text': 'And the economics are changing every single day.',
                       'tip': 'And the economics are changing every single day.',
                       'timestamp': 108,
                       'timestamp_seconds': 108,
                       'timestamp_label': '[00:01:48]',
                       'url': 'https://www.youtube.com/watch?v=Wq9Ov_jlxlM&t=108s',
                       'markdown': '[00:01:48](https://www.youtube.com/watch?v=Wq9Ov_jlxlM&t=108s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QLSYI5Ali8Y',
                       'title': 'Video tutorial: SkyPilot and Kubernetes for multi-node LLM fine-tuning',
                       'channel': 'Nebius',
                       'author': 'Nebius',
                       'text': 'For this demo, I provisioned a fairly small cluster with only two GPU '
                               'nodes.',
                       'tip': 'For this demo, I provisioned a fairly small cluster with only two GPU '
                              'nodes.',
                       'timestamp': 251,
                       'timestamp_seconds': 251,
                       'timestamp_label': '[00:04:11]',
                       'url': 'https://www.youtube.com/watch?v=QLSYI5Ali8Y&t=251s',
                       'markdown': '[00:04:11](https://www.youtube.com/watch?v=QLSYI5Ali8Y&t=251s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IZtzUfhm8LU',
                       'title': 'Why Cheap Spot GPUs End Up Costing MORE (The Checkpoint Mistake)',
                       'channel': 'The Code Notebook',
                       'author': 'The Code Notebook',
                       'text': 'Never commit to your peak.',
                       'tip': 'Never commit to your peak.',
                       'timestamp': 472,
                       'timestamp_seconds': 472,
                       'timestamp_label': '[00:07:52]',
                       'url': 'https://www.youtube.com/watch?v=IZtzUfhm8LU&t=472s',
                       'markdown': '[00:07:52](https://www.youtube.com/watch?v=IZtzUfhm8LU&t=472s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a_zou7QahAo',
                       'title': 'GPU Cluster Scheduler System Design | Gang Scheduling, Topology, '
                                'Preemption',
                       'channel': 'Codemia',
                       'author': 'Codemia',
                       'text': 'The cure has to stay cheaper than the disease.',
                       'tip': 'The cure has to stay cheaper than the disease.',
                       'timestamp': 1424,
                       'timestamp_seconds': 1424,
                       'timestamp_label': '[00:23:44]',
                       'url': 'https://www.youtube.com/watch?v=a_zou7QahAo&t=1424s',
                       'markdown': '[00:23:44](https://www.youtube.com/watch?v=a_zou7QahAo&t=1424s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
