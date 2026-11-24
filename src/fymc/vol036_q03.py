from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'renting-gpus-on-marketplaces-runpod-vs-vast-ai',
 'question_prompt': 'How do I rent the cheapest reliable GPU on RunPod, Vast.ai, and other clouds without '
                    'getting burned by hidden costs and failed pods?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Renting GPUs on Marketplaces: RunPod vs Vast.ai in the Field',
 'subtitle': 'Cheapest GPU per job, $2.69 vs $12.29 H100 price spreads, measured H200 rentals, RTX 4090 '
             'pre-rental checks, multi-GPU VRAM traps, 47 of 291 Vast pods that never ran, storage billing '
             'on stopped pods, total-job cost traps, and Isaac Sim WebRTC setup',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners split marketplace GPU rental along one line: Vast.ai wins the '
                      'sticker, RunPod wins the invoice you can predict. GPU Battle found Vast cheaper on '
                      '17 of 24 shared cards with 55 of 62 tracked GPUs listed, yet 47 of 291 Vast pods '
                      'never ran and one 4090 host delivered half speed. Bryan Software tallied 30 to 60% '
                      "hidden uplift plus $5 to $50 in bandwidth on Vast against RunPod's zero egress, "
                      'fixed $0.34 4090 rate, and $80-per-hour default spend cap. HostingCompared with '
                      'Natalie prices jobs on four numbers: total price, reliability, duration, and data '
                      'costs, warning that stopped storage keeps billing. The street mechanics are '
                      'consistent: price the job not the hour, vet every host in the first minute, destroy '
                      'rather than stop. The split is ratio, not winner: GPU Battle runs roughly 70% '
                      'RunPod, 30% Vast.',
 'key_metrics': [{'label': 'Vast.ai dud pod rate versus RunPod',
                  'metric': 'Vast.ai dud pod rate versus RunPod',
                  'value': '16% on Vast (47 of 291 pods never ran) versus about 7% on RunPod (14 of 200)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'GPU Battle logged every rental while benchmarking; all 47 Vast duds together '
                             'cost about one dollar, so duds are cheap but slow hosts are not.',
                  'source': 'GPU Battle ([kvP__Lh53oM @ 00:00:17])'},
                 {'label': 'Vast.ai hidden cost uplift over the base fee',
                  'metric': 'Vast.ai hidden cost uplift over the base fee',
                  'value': '30 to 60% on top of the base fee, plus $5 to $50 in bandwidth and egress',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Bryan Software compared rate cards line by line; Vast's marketplace runs "
                             'from 2 cents to $6.25 per hour by host while RunPod charges zero for egress.',
                  'source': 'Bryan Software ([Ez2jsa33jFY @ 00:01:06])'},
                 {'label': 'Same H100 SXM 80 GB price spread across clouds',
                  'metric': 'Same H100 SXM 80 GB price spread across clouds',
                  'value': '4.57x, from $2.69 to $12.29 per hour',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Data Receipts compared on-demand list prices inside a single H100 SKU; the '
                             'cheapest row is a marketplace tier and most of the gap is InfiniBand '
                             'interconnect.',
                  'source': 'Data Receipts ([ewu0un1Iy8g @ 00:01:34])'},
                 {'label': 'RunPod stopped volume disk storage rate',
                  'metric': 'RunPod stopped volume disk storage rate',
                  'value': '20 cents per GB-month stopped versus 10 cents running; 100 GB stopped is $20 a '
                           'month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'HostingCompared with Natalie walked the stop versus terminate buttons: stop '
                             'releases the GPU but the volume disk keeps billing, and network volumes '
                             'survive termination.',
                  'source': 'HostingCompared with Natalie ([OQpEhkeZZp4 @ 00:00:19])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus: Vast Wins the Sticker, RunPod Wins the Predictable '
                          'Bill',
               'paragraphs': ['Every operator who has spent real money on both platforms describes the '
                              'same structural split. Bryan Software frames it before running five '
                              'head-to-head tests: RunPod is a managed GPU cloud with fixed rates and '
                              'compliance coverage, while Vast.ai is a marketplace where independent hosts '
                              'set the price [Ez2jsa33jFY @ 00:00:15]. GPU Battle, who checks both price '
                              'lists every day for a tracker covering 62 cards, found Vast listing 55 of '
                              "them against RunPod's 31, and where both carried the same card, Vast came "
                              'in cheaper 17 out of 24 times, with the RTX 3090 at 14 cents versus 22 '
                              'cents, the RTX 5090 at 45 cents versus 69 cents, and the RTX 5080 at 22 '
                              'cents versus 39 cents [156XFkwFpwY @ 00:01:16]. The same operator calls '
                              'Vast the cheapest and also the most expensive provider, because it is the '
                              'only one where bandwidth pricing shifts with each host, which makes it the '
                              'pick for cheap low-VRAM consumer cards while RunPod stays the best '
                              'all-rounder for medium to high workloads [SqfQZYYMPj4 @ 00:01:30]. TWiz '
                              'reaches the same verdict from the usability side: RunPod for a '
                              'user-friendly interface and straightforward pricing, Vast for extensive '
                              'customization and potentially lower costs, paid for with a steeper learning '
                              'curve on the marketplace model [_UBOzLyl2b0 @ 00:02:05].',
                              'The second point of agreement is that the Vast discount is a host lottery, '
                              "and RunPod does not lose every price fight. GPU Battle's plot twist was "
                              'RunPod winning on several big cards, with the H100 at $2.69 against $3.59 '
                              'on Vast, the RTX 4090 at 34 cents against 40 cents, and the A6000 at 33 '
                              'cents against 40 cents, then watching one Vast 4090 host run at half speed '
                              'because it was underclocked [156XFkwFpwY @ 00:01:37]. Across 291 Vast '
                              'rentals the channel logged 47 pods that never ran a single test, a 16% dud '
                              'rate against 14 out of 200, about 7%, on RunPod, while noting the duds '
                              'together cost only a dollar [kvP__Lh53oM @ 00:00:17]. The West Reviews '
                              "relays the same pattern from developers: one Reddit user found Vast's cheap "
                              'GPUs attractive but saw machines fail mid-job and require restarts, while '
                              'another found RunPod more stable with more predictable performance and '
                              'fewer unexpected shutdowns [ZNRLXhDdbW4 @ 00:00:39]. HostingCompared with '
                              'Natalie turns this into an order of operations: set a reliability minimum '
                              'before sorting by price, because if one retry ruins the deadline the lowest '
                              'row becomes the most expensive decision, and even a 99.78% host score is '
                              'useful history, not magic [cEAhnKuawL8 @ 00:00:40].',
                              'The third consensus is about what the bill actually measures, and every '
                              'speaker says the hourly rate alone lies. Bryan Software notes both '
                              'platforms bill per second, so a 16-minute job at $1.99 per hour costs 53 '
                              'cents rather than the full $1.99, a mechanic identical on both sides '
                              '[Ez2jsa33jFY @ 00:01:25]. GPU Battle flags pricing the hour instead of the '
                              'job as a core mistake, since per-second billing means a faster card can be '
                              'cheaper per job, and in their earlier LLM token testing the RTX 3090 rather '
                              'than the H100 came out cheapest per million tokens [WhTJ6B-YCmw @ '
                              '00:04:46]. HostingCompared with Natalie insists on writing down four '
                              'numbers before launch, productive compute, paid idle time, storage lifetime '
                              'and expected transfer, and points out that if setup takes five minutes but '
                              'the GPU sits idle for two hours, setup was never the expensive part '
                              '[_VqIjD7qiIg @ 00:01:43]. The same channel hammers the exit discipline '
                              'everyone repeats: stop on RunPod releases the GPU but the volume disk keeps '
                              'billing at 20 cents per gigabyte per month, so 100 gigabytes is $20 a '
                              'month, a separate network volume survives even termination, and on Vast '
                              'stopping halts compute while storage keeps billing as long as the machine '
                              'is online [OQpEhkeZZp4 @ 00:00:19].'],
               'table': {'caption': 'Where the practitioners agree on RunPod versus Vast.ai',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Vast.ai carries the widest catalogue of rentable cards',
                                   "Vast listed 55 of 62 tracked cards versus RunPod's 31 in daily checks",
                                   'Go to Vast when hunting a consumer or legacy card RunPod does not '
                                   'stock',
                                   'GPU Battle ([156XFkwFpwY @ 00:00:36])'],
                                  ['Vast usually wins the sticker price on shared cards',
                                   'Vast cheaper 17 of 24 times, with the RTX 3090 at 14 cents versus 22 '
                                   'cents',
                                   'Check both price lists daily because RunPod still wins some big cards',
                                   'GPU Battle ([156XFkwFpwY @ 00:01:16])'],
                                  ['RunPod is the managed, predictable all-rounder for heavier work',
                                   'Fixed host rates, zero egress, a default $80 per hour spend cap, final '
                                   'scoreboard 4 to 1',
                                   'Default production-adjacent and deadline-bound jobs to RunPod pods or '
                                   'serverless endpoints',
                                   'Bryan Software ([Ez2jsa33jFY @ 00:06:13])'],
                                  ['Marketplace hosts vary wildly in quality and uptime',
                                   '47 of 291 Vast pods never ran, 16% versus about 7% on RunPod',
                                   'Budget for duds and keep jobs restartable before chasing marketplace '
                                   'floor prices',
                                   'GPU Battle ([kvP__Lh53oM @ 00:00:17])'],
                                  ['The reliability floor comes before any price sorting',
                                   'One captured Vast host showed 99.78% reliability and a nine-month '
                                   'maximum duration',
                                   'Set minimum reliability and duration filters first, then sort the '
                                   'remaining offers by price',
                                   'HostingCompared with Natalie ([cEAhnKuawL8 @ 00:00:40])'],
                                  ['Stopped is not deleted on either platform',
                                   'RunPod stopped volume disk bills 20 cents per gigabyte-month; Vast '
                                   'storage continues while stopped',
                                   'Back up, then terminate or destroy, and delete every leftover volume',
                                   'HostingCompared with Natalie ([OQpEhkeZZp4 @ 00:00:19])'],
                                  ['Both marketplaces undercut the big clouds by a wide margin',
                                   'Isaac Sim on RunPod and Vast ran roughly 10x cheaper than $5 to $6 '
                                   'hourly AWS-class instances',
                                   'Run regular simulation sessions on marketplace clouds instead of '
                                   'paying big-cloud hourly rates',
                                   'hrithik verma ([CkxWiz2Qzi8 @ 00:35:07])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers: Vetting Scripts, Whole-Job Math, and '
                          'Storage Discipline',
               'paragraphs': ['GPU Battle runs rentals through an AI coding agent in Visual Studio Code '
                              'holding the provider API keys, and the street mechanic is a written '
                              'instruction set the agent must follow, starting with confirming CPU specs '
                              'and current RAM before any job lands [WhTJ6B-YCmw @ 00:04:15]. The first '
                              'trap is power-capped cards that listings never disclose: a 5090 throttled '
                              'to 450 watts out of 575, a 4090 at 420 watts, a 3090 at 250 watts against '
                              '315, plus cheap 3060s sitting behind retired mining rigs on 2016-era CPUs '
                              'where a host hands over 16 of 64 cores and the job loads forever, then '
                              'fails to compile [dWC3n2Bn3r8 @ 00:02:25]. The fix is the search prompt '
                              'itself: search by quality, not price, reliability 99% plus, 16 plus CPU '
                              'cores, 800 plus megabytes per second, data center host preferred, price the '
                              'whole job, check power limit, CPU and download speed in the first two '
                              'minutes, destroy the machine if anything is off, always destroy, never '
                              'stop, and keep the API key in a local folder instead of pasting it into '
                              "chat [dWC3n2Bn3r8 @ 00:05:11]. The same channel's one-minute check caught a "
                              '4090 drawing 350 watts against a stock 450, and a listing promising about 3 '
                              'gigabits down that pulled only 14 megabytes a second from Hugging Face '
                              '[kvP__Lh53oM @ 00:00:53].',
                              'The unit economics only work when the whole job is priced line by line. '
                              'HostingCompared with Natalie models a 36-hour run with four paid idle '
                              'hours, 100 gigabytes kept seven days and 50 gigabytes downloaded: RunPod '
                              'compute at the public 74-cent 4090 rate is $29.60 and the full job lands '
                              'around $33.71 with no transfer fee, while the Vast compute floor at a '
                              "28.6-cent host is $11.44, so Vast still wins only if that host's disk and "
                              'transfer extras stay below roughly $22 [cEAhnKuawL8 @ 00:01:40]. Bryan '
                              'Software puts the marketplace range at 2 cents to $6.25 per hour depending '
                              'on host, with hidden costs adding 30 to 60% to the base fee and bandwidth '
                              "and egress tacking on another $5 to $50, against RunPod's zero egress "
                              '[Ez2jsa33jFY @ 00:01:06]. GPU Battle shows how fast those line items bite: '
                              'on one Vast 4090, 6 cents of a 17-cent bill was the download charge, and '
                              'one bad host running ten times slower wipes out the whole discount '
                              '[kvP__Lh53oM @ 00:01:44]. That is why the channel says a 53-cent host can '
                              'beat a 47-cent host, because slow startup on weak CPUs and thin RAM is '
                              'still billed on the same clock [dWC3n2Bn3r8 @ 00:04:28].',
                              'Setup time is the hidden meter, and the speakers attack it with storage '
                              'choices. GPU Battle warns that downloading a 50 GB model on a GPU pod bills '
                              'GPU hours the whole time, so the model goes on a network volume and gets '
                              'downloaded once [WhTJ6B-YCmw @ 00:03:59]. hrithik verma, running Isaac Sim '
                              'from a public Docker template with an 80 GB disk, measured instance builds '
                              'of 15 to 20 minutes plus another long wait for the first Isaac Sim load on '
                              'both platforms, even though data center hosts booted noticeably faster, and '
                              'recommends volume mounts or storing the instance for a week of work instead '
                              'of reloading every session [CkxWiz2Qzi8 @ 00:33:04]. On spec selection, '
                              'HostingCompared with Natalie tells renters of multi-GPU offers to check GPU '
                              'type and count on RunPod, and on Vast the GPU count, per-GPU memory, total '
                              'listed memory, PCIe or NVLink bandwidth and total hourly cost, because two '
                              '24 GB cards only act like one 48 GB pool when the exact framework supports '
                              'model or tensor parallelism [b0fXfKwASvI @ 00:01:37]. Data Receipts applies '
                              'the same discipline at the H100 tier: compare inside one SKU only, since '
                              'the SXM 80 GB, PCIe 80 GB and NVL 94 GB all get sold as an H100 '
                              '[ewu0un1Iy8g @ 00:00:49].'],
               'table': {'caption': 'Street numbers and mechanics reported from live RunPod and Vast.ai '
                                    'rentals',
                         'headers': ['Mechanic or Number',
                                     'Exact Figure Reported',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['RunPod community versus secure cloud on the RTX 4090',
                                   '34 cents community versus 74 cents secure per hour for the same GPU',
                                   'Confirm which RunPod tier a listing is before comparing it against '
                                   'Vast',
                                   'GPU Battle ([WhTJ6B-YCmw @ 00:02:43])'],
                                  ['RunPod fixed rate card that does not swing by host',
                                   'H100 at $2.89 per hour and RTX 4090 at $0.34 per hour',
                                   'Use it as the predictable benchmark against volatile marketplace '
                                   'auction pricing',
                                   'Bryan Software ([Ez2jsa33jFY @ 00:05:51])'],
                                  ['Vast spot interruptible pods bid from the rental menu',
                                   '8 of 17 spot pods kicked off before finishing, about half',
                                   'Use spot only for quick tests or jobs that restart cleanly',
                                   'GPU Battle ([kvP__Lh53oM @ 00:01:13])'],
                                  ['Same-card host spread on the Vast marketplace',
                                   'Three RTX 5070 Ti hosts ran 38 cents apart; listed disk speeds 180 '
                                   'MB/s to 30,000',
                                   'Benchmark several hosts on the same card before trusting any single '
                                   'one',
                                   'GPU Battle ([kvP__Lh53oM @ 00:00:36])'],
                                  ['Off-peak marketplace pricing on cheap consumer cards',
                                   'Five-cent-class listings appear, cheaper when US and European users '
                                   'are asleep',
                                   'Schedule cheap-card sessions off-peak and expect higher marketplace '
                                   'rates at peak',
                                   'hrithik verma ([CkxWiz2Qzi8 @ 00:19:44])'],
                                  ['Same H100 SXM silicon priced across different clouds',
                                   '$1,964 versus $8,972 a month on one GPU, a $7,008 gap',
                                   'Skip InfiniBand cluster pricing when fine-tuning stays on a single '
                                   'node',
                                   'Data Receipts ([ewu0un1Iy8g @ 00:01:57])'],
                                  ['Keeping a stopped Vast instance saved between sessions',
                                   'About $43 a month to hold a stopped Isaac Sim instance',
                                   'Keep the instance only for multi-day work, otherwise destroy it '
                                   'outright',
                                   'hrithik verma ([CkxWiz2Qzi8 @ 00:27:51])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Field Tricks From Operators Who Rent Every Day',
                           'body': 'These are the small moves the speakers credit with turning the Vast '
                                   'floor price into real savings and keeping RunPod bills flat.',
                           'items': ['Test fast and bail: duds cost pennies while slow hosts cost real '
                                     'money, so check every Vast host in the first minute and delete it if '
                                     'the numbers are off [GPU Battle — kvP__Lh53oM @ 00:02:02].',
                                     'Give the AI agent an explicit underclock check, telling it to '
                                     'confirm the GPU is not underclocked by 65 to 70% before the workload '
                                     'starts [GPU Battle — WhTJ6B-YCmw @ 00:04:31].',
                                     'On Vast, add a private Tailscale auth key to the template so UDP '
                                     'ports work for WebRTC streaming, since possibly blocked UDP ports '
                                     'otherwise break the client connection [hrithik verma — CkxWiz2Qzi8 @ '
                                     '00:15:18].',
                                     'If the model fits on one 48 GB card, that is usually the boring and '
                                     'safer choice; if you cannot name the splitting method, do not assume '
                                     'a second card helps [HostingCompared with Natalie — b0fXfKwASvI @ '
                                     '00:01:20].']},
               'sop_steps': [{'step': 1,
                              'title': 'Shortlist by quality, not price',
                              'action': 'Filter offers on reliability, CPU cores, download speed, and host '
                                        'type before sorting by price.',
                              'detail': 'Search with reliability 99% plus, 16 plus CPU cores, 800 plus '
                                        'megabytes per second, and data center hosts preferred, then sort '
                                        'what survives [GPU Battle — dWC3n2Bn3r8 @ 00:05:11].'},
                             {'step': 2,
                              'title': 'Price the whole job in four lines',
                              'action': 'Multiply compute, idle time, storage, and transfer separately for '
                                        'the exact offer you can rent now.',
                              'detail': 'Use productive hours, idle hours, storage kept per day, and '
                                        'gigabytes transferred, and compare a minimum and maximum when any '
                                        'fee is unknown [HostingCompared with Natalie — _VqIjD7qiIg @ '
                                        '00:02:24].'},
                             {'step': 3,
                              'title': 'Vet the host in the first two minutes',
                              'action': 'Check power limit, CPU, and download speed immediately after '
                                        'launch, and move on if the host stalls.',
                              'detail': 'Destroy the machine if anything is off and jump to the next host '
                                        'rather than paying for a throttled card [GPU Battle — dWC3n2Bn3r8 '
                                        '@ 00:05:34].'},
                             {'step': 4,
                              'title': 'Run the exit check',
                              'action': 'Back up or sync, terminate the RunPod pod or destroy the Vast '
                                        'instance, then clear leftover volumes.',
                              'detail': 'Open storage and delete any RunPod network volume or Vast volume '
                                        'you no longer need, because those live beyond compute and bill '
                                        'separately [HostingCompared with Natalie — OQpEhkeZZp4 @ '
                                        '00:01:19].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split is over which platform deserves to be the default. GPU '
                              'Battle, who rents across both every day, refuses to crown a winner and '
                              'lands on a 70/30 mix: 70% of jobs go to RunPod for consistency, templates '
                              'like PyTorch and ComfyUI, and serverless in one account, while 30% go to '
                              'Vast for consumer cards RunPod does not stock, benchmarking experiments, '
                              'and deal sniping on oddities like a Titan RTX [156XFkwFpwY @ 00:06:11]. In '
                              "a later video the same operator softens that into a pure 'either or' call, "
                              'picking whichever platform posts the better deal that day and noting the '
                              'RTX 4090 was actually cheaper on RunPod [WhTJ6B-YCmw @ 00:07:07]. Bryan '
                              'Software is far less diplomatic: across five decision tests the scoreboard '
                              'closed RunPod 4, Vast.ai 1, with Vast winning only the raw hourly price '
                              'test while RunPod took reliability, infrastructure stability, pricing '
                              'predictability, and container customization [Ez2jsa33jFY @ 00:08:01]. '
                              'Meanwhile GPU Battle also calls Vast the ultimate value pack for consumer '
                              'GPUs and budget H100s, provided the agent renting on your API key is told '
                              "how to dodge the marketplace's traps [dWC3n2Bn3r8 @ 00:02:04]. The operator "
                              'takeaway is that the headline verdict depends entirely on whether you score '
                              'sticker price or total predictability.',
                              'Practitioners also disagree on whether Vast is actually cheaper once the '
                              "full bill lands. GPU Battle's own tracking found Vast cheaper 17 out of 24 "
                              'times where both platforms carry the card, with the RTX 3090 at 14 cents '
                              'versus 22 cents and the RTX 5090 at 45 cents versus 69 cents, but RunPod '
                              "won on the big boys, posting the H100 at 2.69 against Vast's 3.59 and the "
                              'A6000 at 33 cents against 40 cents [156XFkwFpwY @ 00:01:16]. '
                              "HostingCompared with Natalie frames it differently: RunPod's public RTX "
                              '4090 pod rate of 74 cents an hour looks terrible beside a dated Vast host '
                              'at 28.6 cents, yet that Vast card explicitly says plus bandwidth, so the '
                              'cheap number is a starting line, not the invoice [cEAhnKuawL8 @ 00:00:19]. '
                              "Bryan Software puts a number on the gap, claiming Vast's hidden costs add "
                              '30 to 60% to the base fee before bandwidth and egress tack on another $5 to '
                              '$50, while RunPod charges zero for egress [Ez2jsa33jFY @ 00:01:06]. Data '
                              'Receipts pushes the argument up-market, showing the same H100 SXM ranging '
                              'from 2.69 to 12.29 an hour, and arguing most of that 4.57x spread is '
                              'InfiniBand interconnect that a single-node fine-tune will never touch '
                              '[ewu0un1Iy8g @ 00:02:21].',
                              'The sharpest playbook clash is over who Vast is for. GPU Battle slots Vast '
                              'into small AI workloads on cheap, low-VRAM consumer cards where you will '
                              'not burn bandwidth, RunPod into medium-to-high workloads, and Modal into '
                              'the really large B300 projects with 200 GB models [SqfQZYYMPj4 @ 00:03:20]. '
                              "TWiz flips part of that logic, pitching RunPod's simplicity to small "
                              "startups while arguing Vast's customization and marketplace model can lead "
                              'to significant cost savings for larger projects and research teams with '
                              'specific GPU requirements [_UBOzLyl2b0 @ 00:01:47]. hrithik verma, running '
                              'Isaac Sim in the cloud, judges the platforms on plumbing rather than price: '
                              'Vast gives you a full Ubuntu VM and UDP ports for WebRTC streaming through '
                              'Tailscale, while RunPod offers neither, so streams feel less stable, '
                              'although both still land about 10x cheaper than the $5 to $6 an hour cited '
                              'for AWS-style instances [CkxWiz2Qzi8 @ 00:35:07]. The West Reviews relays a '
                              "split of developer reports: one user liked Vast's cheap GPUs but hit "
                              'machines failing mid job, while another found RunPod more stable with fewer '
                              'unexpected shutdowns [ZNRLXhDdbW4 @ 00:00:39]. Pick the platform by '
                              'workload size, network needs, and how much restarting you can stomach.'],
               'table': {'caption': 'Side-by-side playbooks where RunPod and Vast.ai practitioners split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Default platform for most AI workloads',
                                   'Run roughly 70% of jobs on RunPod for consistency, templates, and '
                                   'serverless',
                                   'Send roughly 30% to Vast for missing consumer cards, experiments, and '
                                   'deal sniping',
                                   'GPU Battle ([156XFkwFpwY @ 00:06:11])'],
                                  ['Overall cost verdict across five decision tests',
                                   'Vast wins only raw hourly price with a 2 cent marketplace floor',
                                   'RunPod wins reliability, stability, predictability, and containers for '
                                   'a 4 to 1 score',
                                   'Bryan Software ([Ez2jsa33jFY @ 00:08:01])'],
                                  ['Which platform is cheaper on shared cards',
                                   'Vast cheaper 17 of 24 shared cards, like the 3090 at 14 cents',
                                   'RunPod cheaper on H100 at 2.69 versus 3.59 and 4090 at 34 versus 40 '
                                   'cents',
                                   'GPU Battle ([156XFkwFpwY @ 00:01:37])'],
                                  ['Who the marketplace model actually suits best',
                                   'Vast for small low-VRAM consumer workloads, Modal for huge B300 '
                                   'projects',
                                   'Vast for research teams wanting customization and savings on larger '
                                   'projects',
                                   'GPU Battle ([SqfQZYYMPj4 @ 00:03:20]); TWiz ([_UBOzLyl2b0 @ '
                                   '00:01:47])'],
                                  ['Streaming a simulation desktop from the cloud',
                                   'RunPod template over TCP VNC, workable for small scenes but less '
                                   'stable',
                                   'Vast with full Ubuntu VM, UDP ports, Tailscale, and a WebRTC streaming '
                                   'client',
                                   'hrithik verma ([CkxWiz2Qzi8 @ 00:13:12])'],
                                  ['Paying for premium H100 cluster interconnect',
                                   'Single-node fine-tuning skips the InfiniBand cluster node and its 76% '
                                   'premium',
                                   'Training across 64 nodes means the cheap marketplace row is simply not '
                                   'an option',
                                   'Data Receipts ([ewu0un1Iy8g @ 00:03:03])'],
                                  ['Splitting one model across two rented GPUs',
                                   'One 48-gig card when the model fits is the boring and safer choice',
                                   'Two 24-gig cards only when the stack supports model or tensor '
                                   'parallelism and interconnect is adequate',
                                   'HostingCompared with Natalie ([b0fXfKwASvI @ 00:01:20])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure mode is trusting a single marketplace host. GPU '
                              'Battle rented 291 Vast pods and 47 never ran a single test, a 16% dud rate '
                              'against 14 out of 200, about 7%, on RunPod; the duds were cheap, costing a '
                              'dollar combined, so the fix was simply delete and grab another [kvP__Lh53oM '
                              '@ 00:00:17]. The real damage came from hosts that did run but ran slow: the '
                              'same operator rented a 4090 that drew 350 watts when a stock 4090 is 450, '
                              'and listing disk speeds ranged from about 180 megabytes a second to over '
                              '30,000 [kvP__Lh53oM @ 00:00:53]. Old machines behind cheap cards are the '
                              'second trap, with 3060s often sitting on retired mining rigs with 2016-era '
                              'CPUs where the host hands over 16 of 64 cores, so jobs load forever and '
                              'then fail to compile [dWC3n2Bn3r8 @ 00:03:06]. Newer cards are not immune: '
                              'every 5060 GPU Battle tried to rent came back underclocked, saddled with a '
                              'crappy CPU, or short on RAM, making it useless for testing [WhTJ6B-YCmw @ '
                              '00:07:40]. The economics check is blunt: duds cost pennies, slow hosts cost '
                              'real money, and one bad host can wipe out the whole discount.',
                              'Interruptible capacity is where cheap turns into lost work. GPU Battle bid '
                              'on Vast spot pods 17 times and eight got kicked off before they finished, '
                              'about half, which the operator rates great for a quick test and terrible '
                              'for anything you cannot restart [kvP__Lh53oM @ 00:01:13]. Bryan Software '
                              'describes the nightmare version: a training run spins up, runs 40 minutes, '
                              'the host drops, and you lose both the compute time and the checkpoint, with '
                              "Vast's provisioning score at 3.6 out of five and no platform-wide "
                              'contractual SLA [Ez2jsa33jFY @ 00:02:38]. Worse, the same operator flags '
                              "that Vast's interruptible tier bills the license cost even on interrupted "
                              'hours, so the 10 to 30% interruption loss is a charge already paid, not a '
                              'refund, and an unsaved checkpoint means paying for compute you cannot '
                              'recover [Ez2jsa33jFY @ 00:09:16]. HostingCompared with Natalie adds the '
                              'duration trap: always add setup time, idle time, and a safety buffer to the '
                              "offer's maximum rental window, because a cheap offer that expires before "
                              'the checkpoint finishes is just a very affordable way to fail, and if one '
                              'retry ruins the deadline, the lowest row may become the most expensive '
                              'decision [cEAhnKuawL8 @ 00:01:02]. The rule that falls out: spot is for '
                              'restartable work only, and anything with a deadline needs a host that can '
                              'finish.',
                              'The quietest bleed is the bill that keeps running after the work stops. '
                              'HostingCompared with Natalie spells out that stopping a RunPod pod releases '
                              'the GPU but the volume disk keeps billing at the stopped rate of 20 cents '
                              'per gigabyte per month, so 100 gigabytes is $20 a month, while on Vast '
                              'storage keeps billing while the machine is online until you destroy the '
                              'instance and delete any separate volume [OQpEhkeZZp4 @ 00:00:19]. Stopping '
                              'also does not hold your hardware: hrithik verma tried restarting a stopped '
                              'instance and was told it was CPU only because the GPU could not be started, '
                              'so each fresh relaunch means waiting through Docker layers and Isaac Sim '
                              'loading again while the meter runs [CkxWiz2Qzi8 @ 00:04:29]. GPU Battle '
                              'found bandwidth eating 6 cents of a 17 cent Vast 4090 bill on the download '
                              'alone [kvP__Lh53oM @ 00:01:44], and warns that downloading a 50 GB model on '
                              'a GPU pod bills GPU hours the whole time, while an AI agent left '
                              'unsupervised may park a pod on standby instead of terminating it and drain '
                              'credits [WhTJ6B-YCmw @ 00:03:59]. Price the exit, the download, and the '
                              'idle storage before you price the hour.'],
               'table': {'caption': 'Firsthand traps and the economics check each one demands',
                         'headers': ['Trap', 'What Practitioners Hit', 'Economics Check', 'Expert Source'],
                         'rows': [['Dud pods that never run a test',
                                   '47 of 291 Vast pods never ran, 16% versus about 7% on RunPod',
                                   'Duds cost a dollar combined, so delete fast and grab another host',
                                   'GPU Battle ([kvP__Lh53oM @ 00:00:17])'],
                                  ['Same card name, different host speed',
                                   'Same RTX 5070 Ti on three Vast hosts did 2.2 versus 3.05 clips a '
                                   'minute',
                                   'Benchmark three hosts because one 4090 host ran at half speed',
                                   'GPU Battle ([kvP__Lh53oM @ 00:00:36]); GPU Battle ([156XFkwFpwY @ '
                                   '00:02:32])'],
                                  ['Power-capped cards hidden behind normal listings',
                                   '5090 capped at 450 of 575 watts and 3090 at 250 of 315 watts',
                                   'Have the renting agent check the power limit before the real job',
                                   'GPU Battle ([dWC3n2Bn3r8 @ 00:02:25])'],
                                  ['Spot and interruptible tier losses',
                                   'Eight of 17 spot pods were kicked off before finishing their work',
                                   'Interrupted hours still bill license cost, so unsaved checkpoints are '
                                   'sunk compute',
                                   'GPU Battle ([kvP__Lh53oM @ 00:01:13]); Bryan Software ([Ez2jsa33jFY @ '
                                   '00:09:16])'],
                                  ['Stopped pod treated as a deleted pod',
                                   'RunPod stopped volume disk bills 20 cents per gigabyte-month, 100 GB '
                                   'is $20 monthly',
                                   'Back up, terminate or destroy, then delete leftover network or Vast '
                                   'volumes',
                                   'HostingCompared with Natalie ([OQpEhkeZZp4 @ 00:01:19])'],
                                  ['Parking a stored Vast instance for later',
                                   'A stored Isaac Sim instance on Vast showed about $43 for one month',
                                   'Keep it only if skipping repeated 15 to 20 minute rebuilds is worth '
                                   'that',
                                   'hrithik verma ([CkxWiz2Qzi8 @ 00:27:51])'],
                                  ['Treating aggregate VRAM as one big card',
                                   'A 40-gig model can crash on two 24-gig GPUs under data parallel',
                                   'Name the splitting method or assume the second card will not help',
                                   'HostingCompared with Natalie ([b0fXfKwASvI @ 00:00:00])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do Not Launch The Real Job Until The Host Passes',
                           'body': 'Every practitioner who lost money on marketplace GPUs lost it on hosts '
                                   'that looked fine on the listing. Clear these four checks before '
                                   'committing a long run or walking away from a pod.',
                           'items': ['In the first two minutes, check the power limit, CPU, and download '
                                     'speed, and destroy the machine if anything is off [GPU Battle — '
                                     'dWC3n2Bn3r8 @ 00:05:34].',
                                     'Set a minimum reliability score before sorting by price, because if '
                                     'one retry ruins the deadline the lowest row becomes the most '
                                     'expensive decision [HostingCompared with Natalie — cEAhnKuawL8 @ '
                                     '00:00:40].',
                                     'Route spot and interruptible pods only to restartable work, since '
                                     'about half of 17 spot attempts were kicked off before finishing [GPU '
                                     'Battle — kvP__Lh53oM @ 00:01:13].',
                                     'Before leaving, back up, terminate the pod or destroy the instance, '
                                     'then open storage and delete orphaned network or Vast volumes '
                                     '[HostingCompared with Natalie — OQpEhkeZZp4 @ 00:01:19].']}}],
 'pull_quote': "RunPod is the hour you don't have to baby sit, and vast.ai is the hour that costs less if "
               'nothing goes wrong. — Bryan Software (Ez2jsa33jFY @ 00:08:59)',
 'diagram_id': 'diag-03',
 'action_checklist': ['Before launch, write down productive compute, paid idle time, storage lifetime, and '
                      'expected transfer to price the whole job, not the hourly rate [HostingCompared with '
                      'Natalie — _VqIjD7qiIg @ 00:00:00].',
                      'Prompt your renting agent to search by quality, not price: 99% plus reliability, 16 '
                      'plus CPU cores, 800 plus megabytes per second, data center host preferred [GPU '
                      'Battle — dWC3n2Bn3r8 @ 00:05:11].',
                      'Never trust one Vast host; run the same job on three hosts before committing real '
                      'work [GPU Battle — 156XFkwFpwY @ 00:02:32].',
                      'Keep models on a network volume so you download once instead of billing GPU hours '
                      'on every 50 GB pull [GPU Battle — WhTJ6B-YCmw @ 00:03:59].',
                      'Match the card to the job: a 3080 Ti, 3090, or 4090 for chat, images, voice, and '
                      '3D, saving H100s and B200s for big video models [GPU Battle — ymI6ZvqQNjQ @ '
                      '00:03:32].',
                      'When an offer leaves a fee unknown, price a minimum and maximum range instead of '
                      'faking a precise total [HostingCompared with Natalie — _VqIjD7qiIg @ 00:02:44].'],
 'statutory_citations': [{'title': 'Bryan Software — RunPod vs Vast.ai: Which Is Cheapest For GPUs? '
                                   '[00:08:01]',
                          'url': 'https://www.youtube.com/watch?v=Ez2jsa33jFY&t=481s',
                          'relevance': 'Primary practitioner testimony on the five-test RunPod versus '
                                       'Vast.ai scoreboard, hidden cost uplift, and interruptible '
                                       'billing.'},
                         {'title': 'GPU Battle — Vast.ai Review (47 of 291 Pods Never Ran, and What It '
                                   'Cost Me) [00:00:17]',
                          'url': 'https://www.youtube.com/watch?v=kvP__Lh53oM&t=17s',
                          'relevance': 'Primary practitioner testimony on dud rates, host speed variance, '
                                       'spot interruptions, and bandwidth charges on Vast.ai.'},
                         {'title': 'GPU Battle — RunPod vs Vast.ai: Which Cloud GPU Should You Use? '
                                   '[00:06:11]',
                          'url': 'https://www.youtube.com/watch?v=156XFkwFpwY&t=371s',
                          'relevance': 'Primary practitioner testimony on the 70/30 RunPod and Vast split '
                                       'and card-by-card price comparisons.'},
                         {'title': 'HostingCompared with Natalie — RunPod vs Vast.ai: STOPPED GPU, STILL '
                                   'PAYING? Storage Costs Explained [00:00:19]',
                          'url': 'https://www.youtube.com/watch?v=OQpEhkeZZp4&t=19s',
                          'relevance': 'Primary practitioner testimony on stop versus terminate storage '
                                       'billing on both platforms.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'ymI6ZvqQNjQ',
                       'title': 'The Cheapest Cloud GPU for Every AI Job',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': "Most of the time you don't need a GPU with more than 48 GB of VRAM, and "
                               'for chat, images, voice, and 3D, a 3080 Ti, a 3090, or 4090 is cheaper for '
                               'the job.',
                       'tip': "Most of the time you don't need a GPU with more than 48 GB of VRAM, and for "
                              'chat, images, voice, and 3D, a 3080 Ti, a 3090, or 4090 is cheaper for the '
                              'job.',
                       'timestamp': 212,
                       'timestamp_seconds': 212,
                       'timestamp_label': '[00:03:32]',
                       'url': 'https://www.youtube.com/watch?v=ymI6ZvqQNjQ&t=212s',
                       'markdown': '[00:03:32](https://www.youtube.com/watch?v=ymI6ZvqQNjQ&t=212s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SqfQZYYMPj4',
                       'title': 'Mistakes People Make Renting Cloud GPUs (RunPod, Vast.ai, Modal)',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': 'Vast AI is the cheapest, but also the most expensive because the bandwidth '
                               'bill of Vast AI is the only one where the pricing adjusts depending on the '
                               'provider.',
                       'tip': 'Vast AI is the cheapest, but also the most expensive because the bandwidth '
                              'bill of Vast AI is the only one where the pricing adjusts depending on the '
                              'provider.',
                       'timestamp': 65,
                       'timestamp_seconds': 65,
                       'timestamp_label': '[00:01:05]',
                       'url': 'https://www.youtube.com/watch?v=SqfQZYYMPj4&t=65s',
                       'markdown': '[00:01:05](https://www.youtube.com/watch?v=SqfQZYYMPj4&t=65s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '156XFkwFpwY',
                       'title': 'RunPod vs Vast.ai: Which Cloud GPU Should You Use?',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': 'You can never trust one Vast host. You need to run on multiple. So, '
                               'usually I go for three.',
                       'tip': 'You can never trust one Vast host. You need to run on multiple. So, usually '
                              'I go for three.',
                       'timestamp': 152,
                       'timestamp_seconds': 152,
                       'timestamp_label': '[00:02:32]',
                       'url': 'https://www.youtube.com/watch?v=156XFkwFpwY&t=152s',
                       'markdown': '[00:02:32](https://www.youtube.com/watch?v=156XFkwFpwY&t=152s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WhTJ6B-YCmw',
                       'title': "Don't Rent on RunPod Until You Watch This (2026)",
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': 'You want to tell the AI if it starts a container up, terminate it, keep '
                               'your files on network storage or delete network files, terminate pod.',
                       'tip': 'You want to tell the AI if it starts a container up, terminate it, keep '
                              'your files on network storage or delete network files, terminate pod.',
                       'timestamp': 222,
                       'timestamp_seconds': 222,
                       'timestamp_label': '[00:03:42]',
                       'url': 'https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=222s',
                       'markdown': '[00:03:42](https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=222s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WhTJ6B-YCmw',
                       'title': "Don't Rent on RunPod Until You Watch This (2026)",
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': 'Mistake number four, pricing the hour, not the job. Per second billing '
                               'means a faster card can be cheaper per job.',
                       'tip': 'Mistake number four, pricing the hour, not the job. Per second billing '
                              'means a faster card can be cheaper per job.',
                       'timestamp': 286,
                       'timestamp_seconds': 286,
                       'timestamp_label': '[00:04:46]',
                       'url': 'https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=286s',
                       'markdown': '[00:04:46](https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=286s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_UBOzLyl2b0',
                       'title': 'RunPod vs Vast.ai Which GPU Cloud Is Better',
                       'channel': 'TWiz',
                       'author': 'TWiz',
                       'text': "If you're looking for extensive customization and potentially lower costs "
                               'or a marketplace model, Vast.ai may suit you better.',
                       'tip': "If you're looking for extensive customization and potentially lower costs "
                              'or a marketplace model, Vast.ai may suit you better.',
                       'timestamp': 141,
                       'timestamp_seconds': 141,
                       'timestamp_label': '[00:02:21]',
                       'url': 'https://www.youtube.com/watch?v=_UBOzLyl2b0&t=141s',
                       'markdown': '[00:02:21](https://www.youtube.com/watch?v=_UBOzLyl2b0&t=141s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ez2jsa33jFY',
                       'title': 'RunPod vs Vast.ai: Which Is Cheapest For GPUs?',
                       'channel': 'Bryan Software',
                       'author': 'Bryan Software',
                       'text': "RunPod is the hour you don't have to baby sit, and vast.ai is the hour "
                               'that costs less if nothing goes wrong.',
                       'tip': "RunPod is the hour you don't have to baby sit, and vast.ai is the hour that "
                              'costs less if nothing goes wrong.',
                       'timestamp': 539,
                       'timestamp_seconds': 539,
                       'timestamp_label': '[00:08:59]',
                       'url': 'https://www.youtube.com/watch?v=Ez2jsa33jFY&t=539s',
                       'markdown': '[00:08:59](https://www.youtube.com/watch?v=Ez2jsa33jFY&t=539s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ez2jsa33jFY',
                       'title': 'RunPod vs Vast.ai: Which Is Cheapest For GPUs?',
                       'channel': 'Bryan Software',
                       'author': 'Bryan Software',
                       'text': "Vast.ai's interruptible tier bills you for the license cost even on "
                               'interrupted hours, so that 10 to 30% interruption loss is a charge you '
                               'already paid, not a refund.',
                       'tip': "Vast.ai's interruptible tier bills you for the license cost even on "
                              'interrupted hours, so that 10 to 30% interruption loss is a charge you '
                              'already paid, not a refund.',
                       'timestamp': 556,
                       'timestamp_seconds': 556,
                       'timestamp_label': '[00:09:16]',
                       'url': 'https://www.youtube.com/watch?v=Ez2jsa33jFY&t=556s',
                       'markdown': '[00:09:16](https://www.youtube.com/watch?v=Ez2jsa33jFY&t=556s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cEAhnKuawL8',
                       'title': 'RunPod vs Vast.ai RTX 4090: 4 Checks Before You Rent',
                       'channel': 'HostingCompared with Natalie',
                       'author': 'HostingCompared with Natalie',
                       'text': 'Set your minimum before sorting by price. If one retry ruins the deadline, '
                               'the lowest row may become the most expensive decision.',
                       'tip': 'Set your minimum before sorting by price. If one retry ruins the deadline, '
                              'the lowest row may become the most expensive decision.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=cEAhnKuawL8&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=cEAhnKuawL8&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CkxWiz2Qzi8',
                       'title': 'Cheap Cloud GPU for Isaac Sim | RunPod & Vast.ai | WebRTC + VM Setup',
                       'channel': 'hrithik verma',
                       'author': 'hrithik verma',
                       'text': 'Vast AI benefit is that you got VM with it. But in RunPod you do not get '
                               'VM as well as you do not have UDP port.',
                       'tip': 'Vast AI benefit is that you got VM with it. But in RunPod you do not get VM '
                              'as well as you do not have UDP port.',
                       'timestamp': 2107,
                       'timestamp_seconds': 2107,
                       'timestamp_label': '[00:35:07]',
                       'url': 'https://www.youtube.com/watch?v=CkxWiz2Qzi8&t=2107s',
                       'markdown': '[00:35:07](https://www.youtube.com/watch?v=CkxWiz2Qzi8&t=2107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dWC3n2Bn3r8',
                       'title': 'Vast.ai Is the Cheapest Cloud GPU (If You Avoid These Mistakes)',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': 'Search by quality, not price, reliability, 99% plus, 16 plus CPU cores, '
                               '800 plus megabytes per second, data center host preferred.',
                       'tip': 'Search by quality, not price, reliability, 99% plus, 16 plus CPU cores, 800 '
                              'plus megabytes per second, data center host preferred.',
                       'timestamp': 311,
                       'timestamp_seconds': 311,
                       'timestamp_label': '[00:05:11]',
                       'url': 'https://www.youtube.com/watch?v=dWC3n2Bn3r8&t=311s',
                       'markdown': '[00:05:11](https://www.youtube.com/watch?v=dWC3n2Bn3r8&t=311s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b0fXfKwASvI',
                       'title': '2x24GB GPUs Are NOT One 48GB GPU: RunPod vs Vast.ai',
                       'channel': 'HostingCompared with Natalie',
                       'author': 'HostingCompared with Natalie',
                       'text': 'If your model fits on one 48-gig card, that is usually the boring and '
                               'safer choice.',
                       'tip': 'If your model fits on one 48-gig card, that is usually the boring and safer '
                              'choice.',
                       'timestamp': 80,
                       'timestamp_seconds': 80,
                       'timestamp_label': '[00:01:20]',
                       'url': 'https://www.youtube.com/watch?v=b0fXfKwASvI&t=80s',
                       'markdown': '[00:01:20](https://www.youtube.com/watch?v=b0fXfKwASvI&t=80s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '__tHG-ndEu8',
                       'title': 'NVIDIA H200 for AI: What It Actually Delivers (Measured)',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': "It's that VRAM boost. If you don't need the VRAM, go with the H100. It's "
                               'like half the price.',
                       'tip': "It's that VRAM boost. If you don't need the VRAM, go with the H100. It's "
                              'like half the price.',
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=__tHG-ndEu8&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=__tHG-ndEu8&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ewu0un1Iy8g',
                       'title': 'Cheapest GPU cloud: the same H100, $2.69 or $12.29',
                       'channel': 'Data Receipts',
                       'author': 'Data Receipts',
                       'text': 'If you are fine tuning on one node, you are paying for an interconnect you '
                               'will never touch.',
                       'tip': 'If you are fine tuning on one node, you are paying for an interconnect you '
                              'will never touch.',
                       'timestamp': 163,
                       'timestamp_seconds': 163,
                       'timestamp_label': '[00:02:43]',
                       'url': 'https://www.youtube.com/watch?v=ewu0un1Iy8g&t=163s',
                       'markdown': '[00:02:43](https://www.youtube.com/watch?v=ewu0un1Iy8g&t=163s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kvP__Lh53oM',
                       'title': 'Vast.ai Review (47 of 291 Pods Never Ran, and What It Cost Me)',
                       'channel': 'GPU Battle',
                       'author': 'GPU Battle',
                       'text': "My own site's worst story is a host that ran 10 times slower than it "
                               'should and Vast charges for bandwidth.',
                       'tip': "My own site's worst story is a host that ran 10 times slower than it should "
                              'and Vast charges for bandwidth.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=kvP__Lh53oM&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=kvP__Lh53oM&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_VqIjD7qiIg',
                       'title': 'RunPod vs Vast.ai: The Hidden GPU Cost Trap (RTX 4090)',
                       'channel': 'HostingCompared with Natalie',
                       'author': 'HostingCompared with Natalie',
                       'text': 'If an offer leaves one number unknown, do not fake precision. Compare a '
                               'minimum and a maximum instead.',
                       'tip': 'If an offer leaves one number unknown, do not fake precision. Compare a '
                              'minimum and a maximum instead.',
                       'timestamp': 164,
                       'timestamp_seconds': 164,
                       'timestamp_label': '[00:02:44]',
                       'url': 'https://www.youtube.com/watch?v=_VqIjD7qiIg&t=164s',
                       'markdown': '[00:02:44](https://www.youtube.com/watch?v=_VqIjD7qiIg&t=164s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OQpEhkeZZp4',
                       'title': 'RunPod vs Vast.ai: STOPPED GPU, STILL PAYING? Storage Costs Explained',
                       'channel': 'HostingCompared with Natalie',
                       'author': 'HostingCompared with Natalie',
                       'text': 'Last step, open storage and delete any RunPod network volume or Vast '
                               'volume you no longer need. Those live beyond compute and bill separately.',
                       'tip': 'Last step, open storage and delete any RunPod network volume or Vast volume '
                              'you no longer need. Those live beyond compute and bill separately.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=OQpEhkeZZp4&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=OQpEhkeZZp4&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZNRLXhDdbW4',
                       'title': 'Vast.ai vs RunPod: Which GPU Cloud Is Cheaper & Faster? (2026)',
                       'channel': 'The West Reviews',
                       'author': 'The West Reviews',
                       'text': "One Reddit user said Vast.ai's cheap GPUs made it attractive, but "
                               'reliability was inconsistent with machines sometimes failing mid job and '
                               'requiring restarts.',
                       'tip': "One Reddit user said Vast.ai's cheap GPUs made it attractive, but "
                              'reliability was inconsistent with machines sometimes failing mid job and '
                              'requiring restarts.',
                       'timestamp': 39,
                       'timestamp_seconds': 39,
                       'timestamp_label': '[00:00:39]',
                       'url': 'https://www.youtube.com/watch?v=ZNRLXhDdbW4&t=39s',
                       'markdown': '[00:00:39](https://www.youtube.com/watch?v=ZNRLXhDdbW4&t=39s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
