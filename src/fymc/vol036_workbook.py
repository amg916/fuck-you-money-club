from __future__ import annotations

def build_volume_036_workbook() -> dict:
    return {'workbook_id': 'wb-036-gpu-compute-and-telecom-capacity-arbitrage',
 'volume_id': 'vol-036-gpu-compute-and-telecom-capacity-arbitrage',
 'title': 'GPU Compute & Telecom Capacity Arbitrage — Practitioner Testimony Operator Workbook',
 'subtitle': 'A field workbook for converting mining rigs into rental income, pricing data-center silicon '
             'by memory, renting and vetting marketplace GPUs, choosing between colocation and warehouse '
             'power, disciplining cloud and AI token spend, and underwriting neocloud capacity before a '
             'single contract is signed',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Rental Rig Economics and Data-Center Silicon Valuation',
                 'purpose': 'Turn existing or planned GPUs into a rental fleet with honest fee, power, and '
                            'payback math, then value data-center cards and servers by memory capacity, '
                            'bandwidth, and irreversible risk rather than by headline teraflops or vendor '
                            'spec sheets.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Write down your actual electricity rate and every card you hold before '
                                  'filling any field, because every later number depends on revenue minus '
                                  'power.',
                                  'Subtract each marketplace fee and the daily power cost line by line, '
                                  'and never record a gross rental rate as income.',
                                  'Run every burn-in and intake check on real hardware and paste the '
                                  'measured wattage, duration, and interrupt counts rather than estimates.',
                                  'For data-center silicon, record whether each spec figure is dense, '
                                  'sparse, or still projected, and note which inference framework produced '
                                  'each benchmark.',
                                  'Mark any irreversible action, such as a fuse write, in a separate line '
                                  'and list which cards you can afford to lose before approving it.'],
                 'fields': [{'name': 'rental_vs_mining_thesis',
                             'type': 'textarea',
                             'prompt': 'State whether your existing or planned GPUs will mine, rent, or do '
                                       'both. Record your residential or commercial power rate, the cards '
                                       'you hold, and the specific revenue reason you believe renting VRAM '
                                       'beats hashing for your situation today.',
                             'example': 'Rent, not mine. Red Panda Mining states GPU mining is dead and '
                                        'not profitable at any residential electric rate [Red Panda Mining '
                                        '— mfQE_CptyLA @ 00:04:26]. Our six 3090s sit on residential '
                                        'power, so all six move to rental listings. Mining stays off '
                                        'unless revenue minus power leaves a cushion [Crypto Miners Rigs — '
                                        '1q_WZwOjByQ @ 00:07:22].'},
                            {'name': 'marketplace_fee_stack',
                             'type': 'text',
                             'prompt': 'List each rental marketplace you will host on and its cut of '
                                       'revenue. Then write the daily net per card after fees and power, '
                                       'showing every subtraction so you can see which platform actually '
                                       'pays the most.',
                             'example': 'Vast about 25%, SimplePod 20%, Salad 10% plus 40 cents. One 4090 '
                                        'on Salad: 18 cents an hour is $4.32 a day, fees bring it to '
                                        '$3.88, and $0.96 of power leaves $2.92 net [Modern Mining — '
                                        'WJnsgbZsg0U @ 00:37:51]. Glover still calls 25% cheap since the '
                                        'marketplace handles marketing, sales and support [Alec Glover — '
                                        'iuLuDflfEE4 @ 00:15:34].'},
                            {'name': 'card_tier_selection',
                             'type': 'textarea',
                             'prompt': 'Decide between high-end cards and budget or 30-series cards for '
                                       'your rental fleet. Name the marketplace demand signal you are '
                                       'following, the power draw per card you expect, and the reason the '
                                       'tier fits your capital and electricity limits.',
                             'example': 'Budget tier first. SimplePod wants 30-series cards rather than '
                                        'more 4090s or 5090s, and 3090s and 3060s rent consistently at low '
                                        'power draw [Red Panda Mining — mfQE_CptyLA @ 00:08:39]. '
                                        'BearMarketMiner argues high-end is definitely the way to go '
                                        '[BearMarketMiner — egH5hKD913Y @ 00:06:44], so two 4090s stay as '
                                        'a test pair while the 3090 block carries base income.'},
                            {'name': 'used_card_intake_check',
                             'type': 'text',
                             'prompt': 'Describe the intake procedure for every used GPU you buy. Include '
                                       'where you price-check it, how you test it before money changes '
                                       'hands, and the cabling standard you apply before the card ever '
                                       'goes onto a rental listing.',
                             'example': 'Every used card is tested in person before payment and '
                                        'price-checked on gpudeals.net to dodge used-card scams. On '
                                        'install, the 12V cable is seated fully and a 14-gauge power cable '
                                        'is run [Modern Mining — WJnsgbZsg0U @ 00:14:04]. Any card failing '
                                        'the in-person test is refused on the spot, regardless of how '
                                        'attractive the asking price looked online.'},
                            {'name': 'power_and_cpu_tuning',
                             'type': 'textarea',
                             'prompt': 'Record the steady-state load target for your PSUs, PDUs, and rack '
                                       'circuits, plus any CPU clock pinning or GPU power limit you apply. '
                                       'Note the floor you will never cross on platforms that degrade rigs '
                                       'for aggressive power limiting.',
                             'example': 'All power infrastructure sized to sit at a consistent 80% load '
                                        '[Alec Glover — CgsDEFaGLJ0 @ 00:27:22]. The 7950X host is pinned '
                                        'at 1600 MHz, which cut system draw from 600 W to 318 W in '
                                        "BearMarketMiner's run, and GPU power limits never go below 90% on "
                                        'Salad or the rig gets degraded [BearMarketMiner — egH5hKD913Y @ '
                                        '00:21:18].'},
                            {'name': 'burn_in_and_stability_log',
                             'type': 'textarea',
                             'prompt': 'Document your burn-in protocol for each new server: the stress '
                                       'tool, the duration, the throttling symptom you watch for, and the '
                                       'riser troubleshooting sequence you follow if Windows System '
                                       'interrupts climb during mining or rental workloads.',
                             'example': 'C-Payne stress tool runs 48 hours to a week, watching for '
                                        'throttling such as a 4090 dropping from 450 W to 230 W [Alec '
                                        'Glover — CgsDEFaGLJ0 @ 00:46:26]. If System interrupts climb, '
                                        'reseat risers, rerun, then replace one riser at a time even when '
                                        'BIOS shows every port green [Crypto LLC — nHwXk9HCuYI @ '
                                        '00:02:46].'},
                            {'name': 'build_vs_buy_chassis',
                             'type': 'text',
                             'prompt': 'Decide whether you will hand-build open-frame rigs, buy '
                                       'purpose-built chassis, or buy OEM systems with a warranty. Record '
                                       'the per-chassis cost you are budgeting and how you will negotiate '
                                       'OEM quotes against each other before signing.',
                             'example': 'Chassis from day one. Glover tells anyone seeking scale to just '
                                        'go for the chassis immediately [Alec Glover — CgsDEFaGLJ0 @ '
                                        '00:04:55], budgeting $1,500 to $2,000 each. For OEM systems, play '
                                        'vendors against each other: Glover cites Dell at $1M against '
                                        'Supermicro at $750K, with OEM margins near 10% and sometimes 8% '
                                        '[Alec Glover — CgsDEFaGLJ0 @ 00:54:07].'},
                            {'name': 'memory_first_valuation',
                             'type': 'textarea',
                             'prompt': 'Price each data-center GPU option by memory capacity and bandwidth '
                                       'rather than headline teraflops. Note whether spec-sheet figures '
                                       'are dense or sparse, whether any numbers are still projected, and '
                                       'which workload constraint drives your choice of generation.',
                             'example': 'H100 carries 80 GB of HBM3 at 3.35 TB/s [Hitesh C. — fKrvPg4P6KY '
                                        '@ 00:00:28]. Sparse figures are exactly double dense, and the '
                                        'B200 set is still projected, so H200 is chosen when KV cache '
                                        'limits batch size and Blackwell only for FP4 or faster NVLink '
                                        '[Hitesh C. — fKrvPg4P6KY @ 00:03:01]. Under autoregression, H100 '
                                        'compute sits idle up to 80% of the time.'},
                            {'name': 'payback_and_benchmark_check',
                             'type': 'textarea',
                             'prompt': 'Calculate payback on any 8-GPU server against rental pricing, then '
                                       'state your realistic enterprise break-even window. Record which '
                                       'inference framework your benchmark used and whether you will '
                                       'retest on a second framework before committing capital.',
                             'example': 'A ~$250K 8-GPU box against $30/GPU-hr ($240/hr) pays back in '
                                        'about 1,000 hours, roughly 6 weeks flat out, tempered to a '
                                        '12-to-18-month enterprise break-even [SysTelligence — 2tGJAc9AgQI '
                                        '@ 00:11:58]. Ollama showed an H100 at 36.6 tok/s and an H200 with '
                                        'effectively no gain, so vLLM retest comes first [Gimel12 — '
                                        'gD-lTOjHc04 @ 00:03:51].'},
                            {'name': 'irreversible_mod_and_hardening',
                             'type': 'textarea',
                             'prompt': 'Before modding or deploying any data-center card or server, record '
                                       'which actions are irreversible, which cards you can afford to '
                                       'brick, and the network isolation, encryption, and thermal limits '
                                       'applied before the first paying workload lands.',
                             'example': 'No fuse writes on cards we cannot afford to brick; fuse writes '
                                        'are permanent and one card stayed stuck at 64 GB [LOCKBREAK — '
                                        'k-M24u2WcZw @ 00:08:13]. IPMI sits on its own out-of-band VLAN, '
                                        'InfiniBand stays off the management switch, secure boot and NVMe '
                                        'encryption are on, and GPUs hold under 83°C [SysTelligence — '
                                        '2tGJAc9AgQI @ 00:05:17].'}],
                 'completion_gate': 'Worksheet 1 is complete only when every card has a net daily figure '
                                    'after marketplace fees and power, every server has passed a logged '
                                    '48-hour stress run without throttling, all power infrastructure is '
                                    'sized to an 80% steady load, and no irreversible modification is '
                                    'approved on a card you cannot afford to brick.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Marketplace GPU Rental and Colocation Power Planning',
                 'purpose': 'Price rented GPU work by the job instead of the hour, vet marketplace hosts '
                            'in the first minutes, control dud, interruption, and storage leakage, and '
                            'decide where owned hardware lives by comparing provisioned colocation power '
                            'against metered warehouse power and every hidden quote line.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Define one real job, with its deadline and data size, before comparing '
                                  'any rental prices, so totals replace hourly sticker rates.',
                                  'Set a minimum reliability score and a host-vetting checklist first, and '
                                  'only then sort candidate machines by price.',
                                  'Log every pod you launch, including duds and interrupted spot runs, so '
                                  'your dud and interruption rates come from your own records.',
                                  'Break every colocation quote into space, power, cross-connects, and '
                                  'remote hands, and note whether power is billed on provisioned or '
                                  'metered draw.',
                                  'Walk the physical environment for humidity, air quality, and phase '
                                  'balance before any GPU is powered on in a new space.'],
                 'fields': [{'name': 'price_the_job',
                             'type': 'textarea',
                             'prompt': 'Define the job you are pricing, not the hourly rate. Record total '
                                       'price, expected duration, reliability requirement, and data costs '
                                       'for each candidate GPU, and explain why a faster card might finish '
                                       'cheaper under per-second billing.',
                             'example': 'Fine-tuning job priced on four numbers: total price, reliability, '
                                        'duration, and data costs. GPU Battle names pricing the hour '
                                        'instead of the job as mistake number four, since per-second '
                                        'billing lets a faster card cost less per job [GPU Battle — '
                                        'WhTJ6B-YCmw @ 00:04:46]. A minimum reliability score is set '
                                        'before sorting by price [HostingCompared with Natalie — '
                                        'cEAhnKuawL8 @ 00:00:40].'},
                            {'name': 'platform_split_ratio',
                             'type': 'text',
                             'prompt': 'State the ratio of work you will route to RunPod versus Vast.ai, '
                                       'and justify it with the hidden costs, egress charges, spend caps, '
                                       'and predictability differences you expect between a fixed-rate '
                                       'platform and an open host marketplace.',
                             'example': "Roughly 70% RunPod and 30% Vast, matching GPU Battle's split. "
                                        'Vast adds 30 to 60% hidden uplift plus $5 to $50 in bandwidth, '
                                        'while RunPod charges zero egress, holds a fixed $0.34 4090 rate, '
                                        'and defaults to an $80-per-hour spend cap. RunPod is the hour you '
                                        'need not babysit [Bryan Software — Ez2jsa33jFY @ 00:08:59].'},
                            {'name': 'first_minute_host_vetting',
                             'type': 'textarea',
                             'prompt': 'Write the checklist you run in the first two minutes on any rented '
                                       'machine. Name each measurement, the threshold that triggers '
                                       'destruction, and how many hosts you launch in parallel because a '
                                       'single marketplace host cannot be trusted.',
                             'example': 'Check power limit, CPU, and download speed in the first two '
                                        'minutes and destroy the machine if anything is off [GPU Battle — '
                                        'dWC3n2Bn3r8 @ 00:05:34]. Confirm the GPU is not underclocked by '
                                        '65 to 70%. Launch three Vast hosts, because one can never be '
                                        'trusted [GPU Battle — 156XFkwFpwY @ 00:02:32]. Duds cost pennies; '
                                        'slow hosts cost real money.'},
                            {'name': 'dud_and_interruption_budget',
                             'type': 'text',
                             'prompt': 'Estimate the share of pods you expect never to run and the share '
                                       'of spot or interruptible attempts you expect to lose. Record which '
                                       'workloads are restartable enough for interruptible capacity and '
                                       'which must stay on-demand.',
                             'example': 'Budget a 16% dud rate on Vast (47 of 291 pods never ran) against '
                                        'about 7% on RunPod (14 of 200); all 47 Vast duds cost about one '
                                        'dollar [GPU Battle — kvP__Lh53oM @ 00:00:17]. About half of 17 '
                                        'spot attempts were kicked off early, so only checkpointed batch '
                                        'jobs go interruptible; client deliverables stay on-demand.'},
                            {'name': 'vram_fit_decision',
                             'type': 'textarea',
                             'prompt': 'Record the VRAM your model actually needs and whether it fits on a '
                                       'single card. If you plan multiple GPUs, name the splitting method '
                                       'you will use, and explain why a second card genuinely helps this '
                                       'particular workload.',
                             'example': 'The chat model fits on one 48 GB card, the boring and safer '
                                        'choice; with no named splitting method, a second card is not '
                                        'assumed to help [HostingCompared with Natalie — b0fXfKwASvI @ '
                                        '00:01:20]. Most jobs never need more than 48 GB, and a 3090 or '
                                        '4090 is cheaper for chat, images and voice [GPU Battle — '
                                        'ymI6ZvqQNjQ @ 00:03:32].'},
                            {'name': 'teardown_and_storage_hygiene',
                             'type': 'textarea',
                             'prompt': 'Describe your end-of-session teardown. Specify whether you stop or '
                                       'terminate pods, where persistent files live, how you find orphaned '
                                       'volumes, and what stopped storage would cost per month if it were '
                                       'left sitting unnoticed for weeks.',
                             'example': 'Back up, terminate the pod or destroy the instance, then open '
                                        'storage and delete orphaned network or Vast volumes '
                                        '[HostingCompared with Natalie — OQpEhkeZZp4 @ 00:01:19]. Stopping '
                                        'releases the GPU but RunPod volume disk keeps billing at 20 cents '
                                        'per GB-month, so 100 GB stopped costs $20 a month '
                                        '[HostingCompared with Natalie — OQpEhkeZZp4 @ 00:00:19].'},
                            {'name': 'colo_vs_warehouse_power',
                             'type': 'textarea',
                             'prompt': 'Compare colocation against a DIY warehouse for your fleet. Record '
                                       'the per-kW-month price under each model, whether you are billed on '
                                       'provisioned or metered power, and the actual utilization your GPUs '
                                       'draw against each provisioned circuit.',
                             'example': 'Colo floor of $150+ per kW-month against $50 or less DIY [Alec '
                                        'Glover — TZp1yBea0o4 @ 00:01:49]. Colo bills the whole '
                                        'provisioned 6 kW circuit while GPUs use only 20% to 30%, so '
                                        'metered power wins [Alec Glover — TZp1yBea0o4 @ 00:01:30]. Glover '
                                        'ran 1,000 GPUs for about $25,000 a month, though underspending on '
                                        'the build choked growth.'},
                            {'name': 'colo_quote_line_items',
                             'type': 'text',
                             'prompt': 'Break every colocation quote into its separate cost lines. Count '
                                       'cross-connects, remote hands hourly rates, space, and power per '
                                       'server, and total the upfront and monthly charges before you sign '
                                       'anything with the facility operator.',
                             'example': 'Four cross-connects at $500 to $1,500 install plus $100 to $300 '
                                        'monthly each mean $2,000 to $6,000 upfront alone [IPTP Networks — '
                                        '3EnjHW-36GI @ 00:02:34]. Remote hands run $150 to $350 an hour. '
                                        'Each GPU server draws 5 to 15 kW against under 0.5 kW standard, '
                                        'making power the largest line [IPTP Networks — 3EnjHW-36GI @ '
                                        '00:01:36].'},
                            {'name': 'environmental_controls',
                             'type': 'textarea',
                             'prompt': 'Record how you will control humidity, air quality, and phase '
                                       'balance wherever your GPUs live. Note the sensors you install at '
                                       'the GPU intake, the humidity floor you refuse to cross, and how '
                                       'each rack is balanced electrically.',
                             'example': 'Humidity is read the day non-data-center air conditioning starts; '
                                        'at 5% a static shock can destroy a ton of hardware [Alec Glover — '
                                        'TZp1yBea0o4 @ 00:09:43]. Wet, dirty intake air corroded old '
                                        'mining gear within 3 years. Switched PDUs track temperature and '
                                        'humidity at GPU intake, and every rack balances across all three '
                                        'phases [Cakka | Cybersecurity — psGPevLhvpI @ 00:05:22].'},
                            {'name': 'remote_ops_readiness',
                             'type': 'textarea',
                             'prompt': 'Describe how you will service hardware you cannot reach quickly. '
                                       'List your standardization rules, the documentation you keep on '
                                       'serial numbers and disk positions, the spares you stock, and what '
                                       'the facility parts room or staff will cover.',
                             'example': 'All servers are identical, with serial numbers and disk positions '
                                        'documented so parts get ordered before the drive [Techno Tim — '
                                        'zbkqRPIUYAo @ 00:02:20]. The facility stocks common drive sizes, '
                                        'since an 800 GB versus 960 GB mismatch can ruin a day, plus DAC '
                                        'cables and spare PDUs, with staff on site 24x7 [Lawrence Systems '
                                        '— gsN_CJJDy_o @ 00:24:30].'}],
                 'completion_gate': 'Worksheet 2 is complete only when every rental is priced as a total '
                                    'job cost with a reliability floor, a two-minute host-vetting '
                                    'checklist and teardown routine are written down, no orphaned volume '
                                    'remains billing, and every colocation quote shows provisioned versus '
                                    'metered power plus all cross-connect and remote hands charges.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'FinOps Discipline, Repatriation, and Neocloud Underwriting',
                 'purpose': 'Establish visibility and ownership of compute and AI token spend, benchmark '
                            'commitments without overbuying, decide when owning hardware beats paying '
                            'cloud or subscription fees, and underwrite neocloud and multi-cloud GPU '
                            'capacity on utilization, checkpointing, and portability before signing any '
                            'contract.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Pull hourly, resource-level cost data and assign an owner to every line '
                                  'before evaluating any commitment or repatriation option.',
                                  'Benchmark your Effective Savings Rate and on-demand premium against '
                                  'published practitioner figures, and size commitments below peak demand.',
                                  'Start every automation or FinOps agent read-only or human-in-the-loop, '
                                  'and confirm credentials are protected before any code leaves the '
                                  'machine.',
                                  'Model ownership and neocloud returns at your realistic utilization, not '
                                  'at 100%, and state the utilization floor where the investment fails.',
                                  'Run your own end-to-end workload in a proof of concept and record '
                                  'provider interruption benchmarks before signing any GPU contract.'],
                 'fields': [{'name': 'spend_visibility_baseline',
                             'type': 'textarea',
                             'prompt': 'Describe how you see compute and AI token spend today: the '
                                       'granularity, the billing lag, and who owns each line. Note any '
                                       'spend you cannot attribute to an engineer or team, and how quickly '
                                       'invocation costs reach you.',
                             'example': 'Hourly resource-level visibility with engineer ownership is the '
                                        'first step. AWS billing lags seven to eight hours, so invocation '
                                        'logs are streamed for token spend. FinOps X attendees spend 80% '
                                        'of their time on AI, and GenAI tops budget-overrun causes '
                                        '[Vantage — N1u_6ENlZV4 @ 00:16:54]. Tokens cost money, so '
                                        'unlimited use is not sustainable [Vantage — 1-lJfz3oQ2w @ '
                                        '00:05:23].'},
                            {'name': 'commitment_benchmark',
                             'type': 'text',
                             'prompt': 'Record your current Effective Savings Rate on committed compute '
                                       'and compare it to published benchmarks. Note the on-demand premium '
                                       'you are paying, the share of spend covered by commitments, and '
                                       'whether any commitment could actually lose money.',
                             'example': 'Our ESR is checked against the ProsperOps benchmark: 10.5% '
                                        'average, low 20s at the 75th percentile, about 40.5% at the 98th '
                                        '[ProsperOps, a Flexera company — KW_LS_stgvc @ 00:03:35]. '
                                        'On-demand runs two or three times committed rates [Intellipaat — '
                                        '7_L1_3-4kg8 @ 00:22:10]. These instruments can lose money, so '
                                        'coverage is sized below peak.'},
                            {'name': 'commitment_term_and_rightsizing',
                             'type': 'textarea',
                             'prompt': 'For every commitment you hold or plan, record its term against the '
                                       "workload's predicted life. Then describe the order in which you "
                                       'overlay existing reservations and savings plans before any '
                                       'rightsizing action shrinks the underlying virtual machines.',
                             'example': 'The inference app has a two-year predicted life, so no three-year '
                                        'plan; a three-year term on a two-year app wastes a full year '
                                        '[Intellipaat — 7_L1_3-4kg8 @ 00:15:36]. Existing RIs and savings '
                                        'plans are overlaid before right-sizing, or the downsized VM '
                                        'leaves the reservation underutilized [FinOps Foundation — '
                                        'b7TiwS4_Ytw @ 00:17:51].'},
                            {'name': 'automation_guardrails',
                             'type': 'textarea',
                             'prompt': 'Describe the guardrails you will automate and the oversight you '
                                       'will keep. Note whether any FinOps agent starts read-only or '
                                       'human-in-the-loop, how credentials are protected, and which '
                                       'scheduling policies could surprise developers working odd hours.',
                             'example': 'The FinOps agent starts read-only, and .gitignore is confirmed to '
                                        'hide access keys before code leaves the box [AWS Events — '
                                        'JqwiGt78aOI @ 00:19:37]. Instance Scheduler is tag-based, so '
                                        'weekend developers are warned before lights-off schedules shut '
                                        'their boxes down [AWS Events — JqwiGt78aOI @ 00:14:19]. Policy '
                                        'becomes automation and automation becomes guardrails.'},
                            {'name': 'token_cost_controls',
                             'type': 'text',
                             'prompt': 'List the techniques you use to cut AI token spend, such as '
                                       'compression, routing, or permissions. For each, record how you '
                                       'will measure the full bill afterward, so a local saving does not '
                                       'hide a larger cost elsewhere.',
                             'example': 'Prompt compactors can raise output tokens, so the full bill is '
                                        'measured before claiming a compression win [Vantage — 1-lJfz3oQ2w '
                                        '@ 00:30:15]. On Azure, cost-read permissions are sorted before '
                                        'enabling the ARM MCP Server cost toolsets, because a user who '
                                        'cannot view cost has an agent that cannot either [FinOps '
                                        'Foundation — b7TiwS4_Ytw @ 00:26:56].'},
                            {'name': 'repatriation_decision',
                             'type': 'textarea',
                             'prompt': 'Decide whether to keep paying cloud or subscription fees or to own '
                                       'hardware. Record the seat count or monthly bill that justifies '
                                       'ownership, the total cost of owning, and the BMC and documentation '
                                       'checks for any used servers.',
                             'example': 'A DGX H100 costs about $400K total to own and needs 28 '
                                        'subscription seats at $200 a month to break even [Caleb Writes '
                                        'Code — SmYNK0kqaDI @ 00:05:08]. With nine seats, subscriptions '
                                        'win. Any used server is checked so its BMC is not locked behind a '
                                        'vendor cloud license and documentation exists [Craft Computing — '
                                        'JoqFD69bWLw @ 00:15:33].'},
                            {'name': 'neocloud_utilization_breakeven',
                             'type': 'textarea',
                             'prompt': 'Model the return on owning or leasing neocloud-class GPUs at your '
                                       'realistic utilization. Record purchase price, operating cost, '
                                       'rental rate, and expected years of service, then state the '
                                       'utilization level below which the investment fails.',
                             'example': 'An H100 bought for $25K plus $5K opex, rented at $2.30/hr for '
                                        'about four years, returns a 28% CAGR only at 100% utilization; at '
                                        'or below roughly 55%, broad stocks win [Caleb Writes Code — '
                                        '9u2hCf8FlW0 @ 00:01:22]. Our projected 60% clears that line '
                                        'narrowly, so contracted demand must be signed first.'},
                            {'name': 'multicloud_price_spread',
                             'type': 'text',
                             'prompt': 'Record the price spread you observe for the same GPU across clouds '
                                       'and zones, both on-demand and spot. Note how you will declare '
                                       'requirements instead of naming clusters, so a broker can fail over '
                                       'without rewriting deployment specs.',
                             'example': "SkyPilot's broker measured up to 3x on-demand and 9x spot spreads "
                                        'across zones [USENIX — 3Edw88b1bRg @ 00:07:21]. Deployments '
                                        'declare requirements only: 8 GPUs with at least 140GB VRAM on '
                                        'vLLM, no cluster named, with 2 replicas placed across AWS and '
                                        'CoreWeave [Modelplane — Wq9Ov_jlxlM @ 00:03:54]. One YAML spec '
                                        'handles failover across clouds.'},
                            {'name': 'spot_checkpoint_and_scheduling',
                             'type': 'textarea',
                             'prompt': 'Set the checkpoint interval for every spot job and describe the '
                                       'scheduler that keeps GPUs busy. Record mean time between '
                                       'interruptions, save cost, restart cost, and the utilization '
                                       'difference between default and workload-aware scheduling on your '
                                       'fleet.',
                             'example': 'Checkpoint near the square root of 2 x MTBI x save cost, about 34 '
                                        'minutes for a 100h job with 8h interruptions, 6-minute restarts '
                                        'and 72s saves [The Code Notebook — IZtzUfhm8LU @ 00:10:20]. '
                                        'Default Kubernetes holds about 45% utilization versus 85% '
                                        'workload-aware, worth about $150k per day on 10,000 GPUs [Codemia '
                                        '— a_zou7QahAo @ 00:04:38].'},
                            {'name': 'contract_and_provider_gate',
                             'type': 'textarea',
                             'prompt': 'Before signing any neocloud or GPU contract, record your '
                                       'proof-of-concept plan, commitment sizing rule, and provider '
                                       'interruption benchmarks. Note any chip that is only announced, and '
                                       'how multicloud optionality will be used as negotiating leverage.',
                             'example': 'Our own workload runs end to end in a roughly week-long POC, with '
                                        'multicloud optionality as leverage [Toronto Machine Learning '
                                        'Society (TMLS) — _oWJ0t-RW7o @ 00:07:47]. Commitment is sized '
                                        'below peak and signed only where utilization clears one minus the '
                                        'discount [The Code Notebook — IZtzUfhm8LU @ 00:07:52]. '
                                        'Interruption benchmarks: about 8 hours at Meta, 70 to 80 at '
                                        'CoreWeave.'}],
                 'completion_gate': 'Worksheet 3 is complete only when every spend line has an owner, no '
                                    'commitment term outlives its workload, every FinOps agent starts '
                                    'read-only, the utilization floor for any owned or neocloud GPU is '
                                    'stated, spot jobs carry a calculated checkpoint interval, and a '
                                    'week-long proof of concept precedes every signed contract.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Multi-Tenant GPU Sharing and Inference Engine Tuning',
                 'purpose': 'Turn each shared GPU node into a metered, isolated, multi-tenant asset, then '
                            'pull the most tokens per GPU out of it. You choose a sharing layer by '
                            'workload, enforce memory at runtime, align fractional requests with engine '
                            'memory settings, and pick an inference engine from your prefix-sharing '
                            'profile and real request sizes.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Inventory every GPU node pool by card model and VRAM before you choose '
                                  'a sharing layer, because time-slicing, MIG, MPS and Ray fractions each '
                                  'trade throughput, latency and isolation differently.',
                                  'For every fractional tenant, write down how memory is enforced at '
                                  'runtime rather than only annotated at placement, and name the '
                                  'CUDA-level limit that stops one leaky workload from killing its '
                                  'neighbor.',
                                  'Change MIG layouts only on drained nodes, and canary any GPU operator '
                                  'upgrade on one node with metrics re-verified before it reaches the rest '
                                  'of the fleet.',
                                  'Choose your inference engine from measured traffic: estimate '
                                  'shared-prefix token share, confirm the largest real request fits every '
                                  'length limit, and keep the KV pool fraction below the maximum.',
                                  'Benchmark with model, tokenizer, quantization, lengths and concurrency '
                                  'pinned, record median and p99, and price the engineering headcount '
                                  'against the GPU bill before adopting a more complex engine.'],
                 'fields': [{'name': 'sharing_strategy_choice',
                             'type': 'textarea',
                             'prompt': 'Name the GPU sharing layer you will deploy on each node pool '
                                       '(time-slicing, MIG, MPS, or Ray fractions) and state whether your '
                                       'tenants need throughput or low latency, since the measured split '
                                       'between MIG and time sharing turns on that choice.',
                             'example': 'Inference pool: MIG on the A100 nodes for the speech service '
                                        'because throughput matters most; Emmanuel Corels measured 0.76 '
                                        'rising to 1.0 requests/s per GPU at 50 users under MIG [Emmanuel '
                                        'Corels Academy — sRtvITK_o8I @ 00:03:35]. Latency-sensitive chat '
                                        'stays on time sharing, which kept mean speech latency lower in '
                                        'the same test, and dev notebooks get time-slice replicas.'},
                            {'name': 'time_slice_replica_plan',
                             'type': 'text',
                             'prompt': 'Record the time-slicing replica count for each GPU model, the node '
                                       'label that sets the profile, and how you will verify that the GPU '
                                       'operator reconciled the advertised count after you edit the label '
                                       'on a live node.',
                             'example': 'A10 nodes run time-slice profile six by default and flip to ten '
                                        'for batch evenings. Editing the nvidia.com label triggered the '
                                        'NVIDIA GPU operator, and 10 replicas became 6 in a few seconds '
                                        '[Rafay Systems — n-O8p7y9Z5A @ 00:02:13]. After each edit we '
                                        'describe the node and confirm the allocatable nvidia.com/gpu '
                                        'count matches the profile before scheduling tenants.'},
                            {'name': 'memory_isolation_control',
                             'type': 'textarea',
                             'prompt': 'Describe how GPU memory is enforced at runtime for every '
                                       'fractional tenant, not merely annotated at placement, including '
                                       'the CUDA-level limit you apply and the tool you trust for real '
                                       'per-pod usage instead of raw nvidia-smi output.',
                             'example': 'KAI placement alone leaves noisy neighbors possible [CNCF — '
                                        'Vw7DTM1SV60 @ 00:10:30], so every fraction is wrapped by '
                                        'HAMi-core, which converted a 0.35 GPU fraction into an 8,061 MB '
                                        'CUDA_DEVICE_MEMORY_LIMIT [CNCF — Vw7DTM1SV60 @ 00:14:00]. We '
                                        'ignore nvidia-smi on time-sliced L4 cards, where it showed 13 GB '
                                        'while the pod really used 4 GB.'},
                            {'name': 'mig_layout_change_procedure',
                             'type': 'textarea',
                             'prompt': 'List the MIG profiles you will carve on each A100 or similar card, '
                                       'the drain procedure you follow before any layout change, and how '
                                       'inference nodes and training nodes differ in their partition sizes '
                                       'and fault isolation needs.',
                             'example': 'Inference VMs receive 1G.5GB, 2G.10GB and 3G.20GB profiles, each '
                                        'vGPU partition attached to one VM [SUSE — 4q3LHacRheg @ '
                                        '00:00:48]. Layouts change only on drained nodes, because changing '
                                        'the layout while work is running is a named trap [Core Concept '
                                        'Learning — 56JbSXiXhhE @ 00:02:19]. Training nodes stay '
                                        'unpartitioned so large jobs keep full memory.'},
                            {'name': 'ray_vllm_fraction_alignment',
                             'type': 'text',
                             'prompt': 'State the Ray fractional GPU request for each vLLM replica and the '
                                       'matching gpu memory utilization value, and explain how you prevent '
                                       'PyTorch and vLLM from each grabbing the whole VRAM when replicas '
                                       'share a single device.',
                             'example': 'Each replica requests 0.25 GPU in Ray and sets vLLM GPU memory '
                                        'utilization to 0.25 as well. A fractional resource request in Ray '
                                        'is useless on its own [The Code Architect — TwICQ_zP8Ys @ '
                                        '00:06:22], and a 0.25 request alone can still saturate 100 '
                                        'percent of the device [The Code Architect — TwICQ_zP8Ys @ '
                                        '00:07:14].'},
                            {'name': 'preemption_checkpoint_and_upgrade',
                             'type': 'textarea',
                             'prompt': 'Explain where preemptible tenant jobs write checkpoints before '
                                       'they can be reclaimed, and how you canary GPU operator upgrades so '
                                       'that DCGM metrics feeding billing and quotas are re-verified '
                                       'before the upgrade reaches every node in the fleet.',
                             'example': 'Low-priority training checkpoints to a PVC every epoch, so a '
                                        'reclaimed pod resumes at the next epoch instead of restarting '
                                        'from zero [Christian Kniep — K9yY6_2255Y @ 00:02:24]. Operator '
                                        'upgrades go to one canary node first and we re-verify every '
                                        'dashboard, because operator updates very often change or break '
                                        'metrics [CNCF — zrGFmLHI7hg @ 00:10:03].'},
                            {'name': 'engine_selection_by_prefix_share',
                             'type': 'textarea',
                             'prompt': 'Estimate the share of tokens that repeat across requests in your '
                                       'traffic, such as shared system prompts, and use that share to '
                                       'choose between vLLM and SGLang, noting the threshold where you '
                                       'expect the engine choice to matter.',
                             'example': 'Our agent traffic shares roughly 70% of tokens through a fixed '
                                        'system prompt, so it moves to SGLang: below 20% shared tokens the '
                                        'engines are equal, above 40% SGLang wins, and above 70% expect '
                                        'two times or more throughput [Neural AI Flair — 18AkpuX3vkY @ '
                                        '00:06:19]. Independent chat requests stay on vLLM as the stable '
                                        'option.'},
                            {'name': 'memory_limits_and_kv_pool',
                             'type': 'textarea',
                             'prompt': 'Record your max-model-len, max-num-batched-tokens, max-num-seqs '
                                       'and KV pool fraction settings, and confirm the single largest real '
                                       'request in production fits within both length limits with headroom '
                                       'left for VRAM drift between restarts, and explain how you tested '
                                       'it.',
                             'example': 'Our largest request is an 18K visual plus 12K text prompt at 30K '
                                        'tokens, which exceeded both max-model-len and '
                                        'max-num-batched-tokens until we raised them [Lukasz Gawenda — '
                                        "ycEQJIyZ2sU @ 00:07:20]. SGLang's KV pool sits below the maximum "
                                        'because 0.9 yielded only 166K tokens and VRAM use varies between '
                                        'restarts [Lukasz Gawenda — RlsxXB5q-cA @ 00:32:34].'},
                            {'name': 'quantization_and_benchmark_protocol',
                             'type': 'textarea',
                             'prompt': 'Choose the weight precision you will serve (BF16, FP8 or 4-bit), '
                                       'describe the pinned benchmark protocol you will run before and '
                                       'after the change, and name the accuracy check that confirms '
                                       'quantization did not damage answers.',
                             'example': 'Moving a 27B model on an H100 from BF16 to FP8 to 4-bit took '
                                        'weights from 54 GB to 27 GB to 14 GB and decode from about 60 to '
                                        '120 to 240 tok/s [AI WITH Rithesh — lasG5MsR-gE @ 00:11:12]. Runs '
                                        'pin model, tokenizer and concurrency, warm up, clear the prefix '
                                        'cache, and record median and p99 [Tensor Garage — Ym3TP9rlzCk @ '
                                        '00:00:49].'},
                            {'name': 'headcount_and_observability',
                             'type': 'textarea',
                             'prompt': 'Compare the engineering headcount a complex inference engine '
                                       'demands against the monthly GPU bill it saves, and describe the '
                                       'Prometheus and Grafana views that will show throughput and latency '
                                       'as concurrent user counts climb after launch.',
                             'example': 'Before adopting a more complex engine we priced staff, because '
                                        'one ML Ops salary can exceed the entire GPU spend [Uplatz — '
                                        'jp2pwEpUg-Q @ 00:05:50]. We stay on vLLM with Prometheus and '
                                        'Grafana wired onto the server so throughput and latency stay '
                                        'visible as users climb [KodeKloud — qdPkA5mxLhg @ 00:13:06], and '
                                        'we re-run both engines after any CUDA change.'}],
                 'completion_gate': 'Do not onboard a paying tenant until every fractional workload has a '
                                    'runtime CUDA memory limit, MIG changes are restricted to drained '
                                    'nodes, the largest real request fits both max-model-len and '
                                    'max-num-batched-tokens, and a pinned benchmark with median and p99 is '
                                    'on file.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Token Routing, Cheap Self-Hosting, and Voice-AI Telephony',
                 'purpose': 'Decide when to rent tokens through a gateway and when to own the serving '
                            'stack, then wire the telephony layer that voice agents ride on. You set spend '
                            'bands, gateway budgets and routing modes, test cheap hardware honestly, and '
                            'choose SIP trunks and CPaaS carriers without leaving an exposed trunk open to '
                            'toll fraud.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Place your monthly inference spend in a rent-versus-own band first, and '
                                  'price any managed gateway commission per month and per year against the '
                                  'staff time a self-hosted proxy would demand.',
                                  'Lock the gateway with a strong master key before enabling auto-routing, '
                                  'and assume one request will overshoot every key budget so the hard line '
                                  'sits below the true limit.',
                                  'Measure launch-to-ready time, time to first token and tokens per '
                                  'second, cold versus warm, before paying for faster storage, more RAM or '
                                  'another node in a local cluster.',
                                  'Size SIP capacity in concurrent call paths and minutes, compare retail '
                                  'stackable trunks with wholesale minimums, and verify any vendor latency '
                                  'claim with your own test calls.',
                                  'Close every toll-fraud path before a trunk carries traffic: no unused '
                                  'international patterns, zero wildcards, ports 5060 and 5061 restricted '
                                  'to known IPs, and admin access only through VPN.'],
                 'fields': [{'name': 'rent_vs_own_spend_band',
                             'type': 'text',
                             'prompt': 'Enter your current monthly third-party inference spend and place '
                                       'it in a rent-versus-own band, stating whether you stay on APIs, '
                                       'treat the middle range as a judgment call, or begin a self-hosting '
                                       'plan this quarter.',
                             'example': 'Current spend is about £40k a month, inside the £10k to £100k '
                                        'judgment-call band; Daniel keeps teams on third-party APIs under '
                                        '£10k and treats over £100k a month as a strong push to self-host '
                                        '[Data Science Festival — WiA5Hm6IpZs @ 00:13:47]. We stay rented, '
                                        'review quarterly, and start a self-hosting pilot if spend crosses '
                                        '£100k.'},
                            {'name': 'gateway_commission_math',
                             'type': 'textarea',
                             'prompt': 'Calculate what a managed gateway commission costs you per month '
                                       'and per year at your current usage, then compare it with the staff '
                                       'time needed to run a self-hosted LiteLLM proxy, including '
                                       'database, caching and patching duties.',
                             'example': "At 100,000 a month of usage, OpenRouter's 5% commission is 5,000 "
                                        'a month or 60,000 a year [Jono Finds — XZPNjgJ4E0c @ 00:02:24]. '
                                        'Self-hosting LiteLLM removes that cut, but with the open-source '
                                        'option you manage the database, caching and patching and own the '
                                        'attack surface [Mariselle Hartwell — pa2rbXDnUYM @ 00:01:57]. We '
                                        'budget one part-time operator.'},
                            {'name': 'virtual_key_budget_controls',
                             'type': 'textarea',
                             'prompt': 'Define the LiteLLM virtual keys, budgets, rate limits and fallback '
                                       'chains for each team, and describe how you absorb the single '
                                       'request that overshoots a budget line before the proxy starts '
                                       'returning budget exceeded errors to callers.',
                             'example': 'The support team key carries a $500 budget with a Slack alert. '
                                        'Ready Tensor watched the request that crossed $500 still succeed, '
                                        'and only the next one returned a 400 budget exceeded error [Ready '
                                        'Tensor — 9t-W51EHgzY @ 00:12:43], so we set the key at $450 to '
                                        'absorb one oversized call before the hard line.'},
                            {'name': 'routing_mode_selection',
                             'type': 'textarea',
                             'prompt': 'For each model you call through a gateway, choose the routing mode '
                                       '(default, cheapest, or fastest) and justify it with measured '
                                       'median latency and the price multiple you accept for speed on '
                                       'user-facing paths versus batch paths.',
                             'example': 'On GPT-OSS 120B the default took 1.87 seconds, cheapest Venice '
                                        '3.89 seconds, and fastest Cerebras 1.34 seconds at 5.6 times the '
                                        'cost [Prompt Engineer 48 — FpNPRj38T6s @ 00:03:34]. Batch jobs '
                                        'use :cheapest there. On Qwen 3.8 27B we pay about 20 percent more '
                                        'for :fastest, which cut median latency from 8.99s to 1.83s.'},
                            {'name': 'auto_router_hardening',
                             'type': 'text',
                             'prompt': 'Describe how you lock down the gateway before enabling automatic '
                                       'model routing, including the master key, parameter handling, and '
                                       'the rules or classifier that decide which requests are sent to the '
                                       'more complex and expensive models.',
                             'example': 'The Auto Router runs with drop_params enabled and a strong master '
                                        'key [LiteLLM AI Gateway — blSVb26UQYg @ 00:03:44]. Routing runs a '
                                        'heuristic first, then keyword rules like security review or '
                                        'incident going to complex, then an LLM classifier using the last '
                                        '3 turns with heuristic fallback [LiteLLM AI Gateway — blSVb26UQYg '
                                        '@ 00:02:25]. We log every routed decision.'},
                            {'name': 'cheap_hardware_self_host_test',
                             'type': 'textarea',
                             'prompt': 'If you plan to self-host on free or low-cost hardware, record '
                                       'launch-to-ready time, time to first token and tokens per second, '
                                       'cold versus warm, and note any network timeout that long prefill '
                                       'could trip before a response.',
                             'example': 'Two free Kaggle T4s ran a ~180B MoE at 28.5-33.2 tok/s at Q2 '
                                        '[Bruno Vega — KVXaHQu32Rw @ 00:07:53]. The first boot took '
                                        '1,097s, 840s of it downloading 68GB, so weights are cached to a '
                                        'private dataset. Agent harnesses send 8 to 30K tokens up front, '
                                        "near Cloudflare's 100-second cut [Bruno Vega — KVXaHQu32Rw @ "
                                        '00:12:40].'},
                            {'name': 'cluster_and_confidential_controls',
                             'type': 'textarea',
                             'prompt': 'If you link several local machines or offer confidential inference '
                                       'to tenants, describe how RPC nodes are kept off open networks, '
                                       'when adding a node stops helping, and how serving images are '
                                       'attested before weights are released.',
                             'example': 'The llama.cpp RPC backend is fragile and insecure, so laptop '
                                        'nodes sit on an isolated segment [Cian Mag — kgSARM9iGF4 @ '
                                        '00:08:36], and we stopped at three because a fourth machine is '
                                        'another one the cluster has to wait for. Every new confidential '
                                        'serving image is attested before weights release, with rollback '
                                        'on failure [Duality Technologies — nXTWdWFiGvM @ 00:04:03].'},
                            {'name': 'sip_trunk_and_carrier_tier',
                             'type': 'textarea',
                             'prompt': 'Size your SIP trunk capacity in concurrent call paths and monthly '
                                       'minutes, then decide whether you buy retail stackable trunks or '
                                       'meet a wholesale carrier minimum commitment, showing the '
                                       'per-minute rate and monthly floor for each option.',
                             'example': 'We need five concurrent calls and about 15,000 minutes, so five '
                                        'SIPStation trunks at 3,000 minutes each, one bi-directional '
                                        'concurrent call per trunk [Sangoma — dTsrqOzzrOk @ 00:02:13]. '
                                        'VoIP Innovations wholesale carries a $250 monthly minimum service '
                                        'commitment plus volume-based plans [Sangoma — dTsrqOzzrOk @ '
                                        '00:25:51], which we revisit once resale volume clears that '
                                        'floor.'},
                            {'name': 'cpaas_voice_agent_carrier',
                             'type': 'textarea',
                             'prompt': 'Choose the CPaaS carrier behind your voice agents and messaging, '
                                       'comparing per-unit SMS and voice pricing, region pinning, and '
                                       'turn-gap latency, and describe the test calls you will run before '
                                       'trusting any vendor latency benchmark on production routes.',
                             'example': 'Plivo lists $0.007 per SMS and $0.01 per voice minute [Amir '
                                        'Tutorial — _2POs6qxMdo @ 00:01:48], while Telnyx markets sub-200 '
                                        'millisecond round trips, which Tim says to take with a grain of '
                                        'salt [Voice AI with Tim — kYOdE4uxQXQ @ 00:05:42]. We place 100 '
                                        'test calls per carrier and pin Twilio numbers to Australia for '
                                        'Sydney callers.'},
                            {'name': 'sip_fraud_lockdown',
                             'type': 'textarea',
                             'prompt': 'Document the toll-fraud controls on every trunk and PBX: dial plan '
                                       'patterns, wildcard usage, which IP addresses may reach ports 5060 '
                                       'and 5061, how admins reach the PBX, and whether the SIP host has a '
                                       'static public IP.',
                             'example': 'The dial plan holds no international patterns and zero wildcards, '
                                        'since attackers throw random numbers to see which completes '
                                        '[Mitel Academy — ijPHb8SEENo @ 00:10:37]. Ports 5060 and 5061 '
                                        "accept only the provider's IP and known remote users, with admin "
                                        'over VPN [Mitel Academy — ijPHb8SEENo @ 00:13:08]. The SIP VM '
                                        'holds a static public IP before trunks point at it.'}],
                 'completion_gate': 'Do not route production traffic until your spend band is recorded, '
                                    'every gateway key has a budget set below its true limit, routing '
                                    'modes are justified with measured latency, 100 test calls per carrier '
                                    'are logged, and the dial plan and SIP ports pass the toll-fraud '
                                    'lockdown.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'A2P 10DLC Registration and Carrier Compliance',
                 'purpose': 'Get business SMS registered, vetted and delivered, then keep a voice resale '
                            'operation legal and profitable. You match brand identity to tax records, '
                            'write a call to action reviewers accept, budget vetting attempts, plan '
                            'throughput tiers, confirm attestation and Robocall Mitigation Database status '
                            'yourself, and model whether thin resale margins survive compliance costs.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ["Match the brand's legal name and EIN exactly to the tax filing and "
                                  'confirm a DUNS number is on file before paying any registration fee.',
                                  'Open the public opt-in link in an incognito tab before every '
                                  'resubmission, and confirm the SMS checkbox is unchecked and separate '
                                  'from the terms box.',
                                  'Budget registration, external vetting and per-attempt campaign vetting '
                                  'fees, and plan throughput against default carrier tiers, asking your '
                                  'platform whether each limit is a carrier or internal cap.',
                                  'Call an attestation checker from your own trunk, buy DIDs from the '
                                  'carrier that signs your calls, and confirm your Robocall Mitigation '
                                  'Database listing personally instead of trusting an upstream carrier or '
                                  'adviser.',
                                  'Model resale margin, USF pass-through and state filings before launch, '
                                  'set daily spend and per-minute caps on termination, and run the '
                                  'switching test before signing any IoT or eSIM connectivity deal.'],
                 'fields': [{'name': 'brand_identity_match',
                             'type': 'text',
                             'prompt': "Enter the brand's legal name, EIN and DUNS number exactly as they "
                                       'appear on tax filings, and record when you compared each one '
                                       'against IRS records before submitting the brand to TCR for '
                                       'verification and approval.',
                             'example': 'Legal name and EIN were copied from the tax filing, and a DUNS '
                                        'number was confirmed on file. RingLogix saw a one-month '
                                        'verification stall clear the same day once the legal name and EIN '
                                        'matched exactly [RingLogix — gmCqaG2hBKQ @ 00:38:26]. The $4 '
                                        'brand registration fee [TwilioDevs — KWvbRToRnGg @ 00:13:45] was '
                                        'paid only after this check.'},
                            {'name': 'opt_in_call_to_action',
                             'type': 'textarea',
                             'prompt': 'Write the exact call to action reviewers will see, describing '
                                       'where the opt-in form lives, how a screenshot or public link '
                                       'proves it exists, and how the SMS consent checkbox is kept '
                                       'unchecked and separate from the terms box.',
                             'example': 'Customers opt in on the website form with name, phone, consent '
                                        'and submit; a screenshot sits in a Google Drive link pasted into '
                                        "the call to action, the fix that ended Paradigm Escape's "
                                        'rejections [Paradigm Escape — wpj7_7cz4Kk @ 00:01:10]. The SMS '
                                        'checkbox starts unchecked and separate from the terms box '
                                        '[TwilioDevs — 7pXYEARPIwU @ 00:00:33].'},
                            {'name': 'message_samples',
                             'type': 'textarea',
                             'prompt': 'Draft the campaign message samples from the messages you will '
                                       'actually send, showing the brand name in every sample, square '
                                       'brackets around dynamic data, and the opt-out language that tells '
                                       'recipients how to stop further messages.',
                             'example': "Sample one: '[First name], your Northline Clinic appointment is "
                                        "[date] at [time]. Reply STOP to opt out.' Every sample is written "
                                        'from live templates, names the brand, and wraps dynamic data in '
                                        'square brackets [TwilioDevs — KWvbRToRnGg @ 00:15:45]. We also '
                                        'confirm every STOP gets a reply before scaling [Telecom '
                                        'Application Development Summit — SRizDef5BbE @ 00:15:53].'},
                            {'name': 'vetting_and_fee_budget',
                             'type': 'textarea',
                             'prompt': 'Budget every registration and vetting fee you expect to pay, '
                                       'including brand registration, external vetting, and per-attempt '
                                       'campaign vetting charges, and state how many rejected '
                                       'resubmissions your budget and launch timeline can absorb before '
                                       'you go live.',
                             'example': 'Brand registration is $4, external vetting a $40 one-time fee '
                                        '[Telgorithm — dgkKW0cbz1E @ 00:23:54], and DCA vetting $15 per '
                                        'attempt, or $45 after three rejections [Telgorithm — dgkKW0cbz1E '
                                        '@ 00:28:46]. We budget for three attempts, while noting a Midwest '
                                        'MSP needed about 15 resubmissions after repeated call-to-action '
                                        'rejections [Paradigm Escape — wpj7_7cz4Kk @ 00:03:14].'},
                            {'name': 'throughput_tier_plan',
                             'type': 'textarea',
                             'prompt': 'Record your expected daily segments and messages per minute '
                                       'against the default carrier tiers and the tier unlocked by a high '
                                       'vetting score, and ask your platform whether any limit you see is '
                                       'a carrier limit or an internal one.',
                             'example': 'Default tiers sit near 2,000 segments a day on T-Mobile and 75 '
                                        'TPM on AT&T; a vetting score of 80-100 unlocks 4,500 TPM and '
                                        '200,000 a day [Telgorithm — dgkKW0cbz1E @ 00:24:25]. Our platform '
                                        'capped us at 60 messages per minute, so we asked whether that was '
                                        'the carrier or internal limit [Signal House — sVsWkczKncU @ '
                                        '00:04:08].'},
                            {'name': 'send_caps_and_spend_controls',
                             'type': 'text',
                             'prompt': 'Describe the daily send ceiling you enforce per brand, the spend '
                                       'caps set on the messaging account, and the alert that fires before '
                                       'a send would exceed the carrier cap and silently drop messages to '
                                       'customers.',
                             'example': 'Our queue stops at 1,900 messages a day per brand, because on a '
                                        '2,000 T-Mobile cap the 2,001st message drops [Telgorithm — '
                                        'dgkKW0cbz1E @ 00:53:48]. Spend caps are set before scaling, since '
                                        'escalated spam reviews start at $500 [Telecom Application '
                                        'Development Summit — SRizDef5BbE @ 00:15:53]. An alert fires at '
                                        '1,800 sends so the overflow moves to the next day.'},
                            {'name': 'stir_shaken_attestation',
                             'type': 'textarea',
                             'prompt': 'Record the STIR/SHAKEN attestation level your outbound calls '
                                       'receive, which carrier sold each DID, how forwarded calls are '
                                       'signed, and the result of calling an attestation checker from your '
                                       'own trunk before you resell voice service.',
                             'example': 'We call the checker number 920-66-1392 from our trunk and fix '
                                        'anything other than A [Crosstalk Solutions — ycGPHG_ANrE @ '
                                        '00:04:31]. DIDs are bought from the signing carrier, since '
                                        'third-party DIDs drop to B [Sangoma — 3XJ9OkK8aFw @ 00:07:34]. '
                                        'Follow-me forwarding signs B today, and C signings drive most '
                                        'T-Mobile spam flags.'},
                            {'name': 'rmd_and_regulatory_filings',
                             'type': 'textarea',
                             'prompt': 'List every regulatory filing your voice operation needs, including '
                                       'the Robocall Mitigation Database listing, FCC Form 499 and state '
                                       'filings, and record how you personally confirmed each listing '
                                       'rather than trusting an upstream carrier or adviser.',
                             'example': 'Our Robocall Mitigation Database listing was checked directly, '
                                        'because providers must refuse traffic from anyone not listed as '
                                        'of May 28th 2024 [ZCorum — ZLzeR3N0mpc @ 00:05:20]. Chris trusted '
                                        'both their upstream carrier and lawyer, and both were wrong '
                                        '[Crosstalk Solutions — ycGPHG_ANrE @ 00:20:06]. State filings and '
                                        'billing are modeled before launch, not after.'},
                            {'name': 'resale_margin_and_usf',
                             'type': 'textarea',
                             'prompt': 'Model your voice resale margin after registration, tax engine, '
                                       'billing, token and certificate costs, and show how USF '
                                       'pass-through line items affect the customer bill, so you know '
                                       'whether thin margins survive the compliance load every month.',
                             'example': 'Crosstalk reached only 15 to 20 percent monthly margin once its '
                                        'SIP side business turned a profit [Crosstalk Solutions — '
                                        'ycGPHG_ANrE @ 00:07:43], and the iconectiv token and certificate '
                                        'each cost thousands a year. USF pass-through runs four to five '
                                        'dollars a bill with the factor at 25 to 33 percent [The '
                                        'Federalist Society — EL34vsXYuGQ @ 00:03:00].'},
                            {'name': 'termination_caps_and_lock_in',
                             'type': 'textarea',
                             'prompt': 'Set daily spend and per-minute caps on outbound termination, and '
                                       'for any IoT or eSIM connectivity deal, answer the switching test '
                                       'of who you can move to today and what it would cost before signing '
                                       'any contract.',
                             'example': "Outbound termination runs on Sangoma's A-Z service with daily "
                                        'spend and per-minute caps [Sangoma — 3XJ9OkK8aFw @ 00:21:59], '
                                        'backed by a fraud score between zero and 100. Before the IoT deal '
                                        'we asked who we could switch to today and how much it would cost, '
                                        'because if you cannot switch you are locked by technology [IoT '
                                        '(eSIM) Studio — GZtF-I2M1ZE @ 00:02:51].'}],
                 'completion_gate': 'Do not send business SMS or resell voice until the brand identity '
                                    'matches tax records, the opt-in link passes an incognito check, daily '
                                    'sends sit under the carrier cap, attestation returns A from your own '
                                    'trunk, and your Robocall Mitigation Database listing is personally '
                                    'confirmed.'}]}
