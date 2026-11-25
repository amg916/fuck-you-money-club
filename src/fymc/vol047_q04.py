from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'vol047-q04-interconnection-queues-ferc-order-2023-cluster-reform',
 'question_prompt': 'How does the generator interconnection queue work, why is it backlogged, and how are '
                    'FERC Order 2023 cluster reforms changing it?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Interconnection Queues and FERC Order 2023 Cluster Reform',
 'subtitle': 'Queue mechanics and attrition, FERC 2023 cluster studies and network upgrades, TVA, SPP and '
             'CAISO IPE 5.0 process changes, deposits and withdrawal costs, post-SGIA studies, empirical '
             'queue analysis, and AI and automation in queue reform',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the interconnection queue is a request process, not a '
                      'construction schedule: Stats in Motion counts 14 GW withdrawn per 1 GW connected in '
                      '2025, and Andy Knows It puts historical withdrawal at 78%. FERC Order 2023 swapped '
                      'serial first-come queuing for first-ready-first-served clusters, firm deadlines, '
                      'site control and impact-based cost allocation, which Keentel Engineering reduces to '
                      "'cost follows impact, not MW.' Street mechanics are cash-heavy: TVA deposits scale "
                      'to $300K plus readiness money, withdrawal penalties climb to 20% after the LGIA, '
                      'and ISO-NE allocations ran from $0 to $2,700/kW. Dirt to Data and GridState warn '
                      'that AI campuses now face generator-style studies on the load side. Disagreement '
                      'centers on automation: SPP and MISO tout 50% time savings and under-a-day costing, '
                      "while PJM calls AI roughly '80% right' and not ready for prime time.",
 'key_metrics': [{'label': 'Withdrawn-to-Connected Ratio (2025)',
                  'metric': 'Withdrawn-to-Connected Ratio (2025)',
                  'value': '14 GW withdrawn for every 1 GW connected',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Stats in Motion reading of LBNL data: the queue shrank about 10% through '
                             'dropouts, not completions, and the storage queue fell 16%.',
                  'source': 'Stats in Motion ([Z2FdaH10ZCY @ 00:00:15])'},
                 {'label': 'ISO-NE Transitional Cluster Allocation Range',
                  'metric': 'ISO-NE Transitional Cluster Allocation Range',
                  'value': '$0 to $541M per project, or $0 to $2,700/kW',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Keentel Engineering breakdown of a 23-project, 4,826.5 MW cluster carrying '
                             '$3.21B in total upgrade cost.',
                  'source': 'Keentel Engineering ([TM7qt8CCWxk @ 00:05:05])'},
                 {'label': 'PJM Interconnection Cost Tail',
                  'metric': 'PJM Interconnection Cost Tail',
                  'value': 'About $50/kW median, about $400/kW at the 90th percentile',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sarah Johnson's hand-collected PJM dataset of about 4,000 requests and 7,000 "
                             'studies, against roughly $1,500/kW to install.',
                  'source': 'Environmental Defense Fund ([M62wgLYBKBw @ 00:28:33])'},
                 {'label': 'TVA Readiness Deposit, 200 MW-Plus Tier',
                  'metric': 'TVA Readiness Deposit, 200 MW-Plus Tier',
                  'value': '$925K (stated as 2x the $300K study deposit)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'TVA LGIP effective November 1, 2024 for projects over 20 MW, alongside a '
                             '$25K nonrefundable fee and 100% site control.',
                  'source': 'Keentel Engineering ([gGBYCEdn18o @ 00:01:09])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus — Readiness, Impact and the Queue as an '
                          'Asset',
               'paragraphs': ['Every practitioner who touches the numbers lands in the same place: a '
                              'megawatt in the queue is a proposal, not a plant. Blueprint States frames '
                              'the queue as a request process that starts studies and proves nothing about '
                              'financing, construction, or operation, and warns that even a signed '
                              'agreement does not mean commercial operation [v2cs7ZXTQH0 @ 00:01:04]. Andy '
                              'Knows It puts the attrition at 78% of capacity that entered from 2000 to '
                              "2018 eventually withdrawing, and calls the 2,000-plus gigawatt line 'part "
                              "pipeline and part graveyard' [QxDqhnba2Jg @ 00:04:12]. Stats in Motion "
                              'reads the latest shrinkage the same way: in 2025, 14 GW withdrew for every '
                              '1 GW that connected, and of projects entering from 2000 to 2020 only 13% '
                              'were built while 75% withdrew, which the narrator calls the first report '
                              "card on Order 2023 [Z2FdaH10ZCY @ 00:00:48]. Sarah Johnson's PJM work for "
                              'Environmental Defense Fund adds the split by fuel: about 85% of renewables '
                              'never operate versus 68% of fossil, and a survey of roughly 40 developers '
                              'ranked interconnection as the number one barrier [M62wgLYBKBw @ 00:16:15]. '
                              "Blueprint States closes the loop plainly: 'a megawatt in the queue is not a "
                              "megawatt on the grid.'",
                              'On the reform itself, the FERC side and the engineering side describe the '
                              "same machine. Karen Herzfeld of Chairman Phillips' office laid out three "
                              'buckets — first-ready-first-served clusters, speed, and technology — with '
                              'costs allocated by proportional impact, site control at 90% on entry and '
                              '100% by facility study, and the old reasonable-efforts standard replaced by '
                              'firm deadlines with appealable penalties [-BTpIv2G5-0 @ 00:06:32]. Keentel '
                              'Engineering compresses that into one rule: cost follows impact, not '
                              "megawatts, and the real financial risk 'may be many electrical miles away "
                              "from the point of interconnection' [TM7qt8CCWxk @ 00:03:31]. Their TVA "
                              "breakdown shows the competitive dynamic has 'shifted from speed to "
                              "readiness,' with 100% site control required, substation upgrades split per "
                              'capita and system upgrades by proportional impact, and the blunt warning '
                              "that 'your costs are coupled to your neighbors' [gGBYCEdn18o @ 00:04:44]. "
                              'Andy Knows It explains why the serial model broke: the generator that '
                              'triggers an upgrade pays for it, restudy dependencies made '
                              "first-come-first-served 'completely unworkable,' and near-free entry let "
                              "developers file on land they didn't control just to hold position "
                              '[QxDqhnba2Jg @ 00:03:24]. Consensus therefore sits on readiness, controlled '
                              'land, and impact-based allocation as the baseline price of admission, with '
                              'deadlines that no longer bend.',
                              'For data-center land, Dirt to Data draws the line every investor needs: '
                              'seeing the grid is not the same as having the right to use it, and AI '
                              'campuses requesting hundreds of megawatts now raise generator-like '
                              'questions on the load side [264d0wu5W4k @ 00:02:34]. Their example is 300 '
                              'acres sitting near a line that can still be blocked by queued generators '
                              'and other large loads, which is why queue position itself becomes the asset '
                              "— 'your land hasn't changed' — and why power in 2033 against a 2028 need "
                              'simply means no project [264d0wu5W4k @ 00:04:48]. GridState lands in the '
                              "same spot, noting that AI data centers approaching gigawatt scale are 'the "
                              "equivalent of adding an entirely new city to the grid' and face the same "
                              'capacity, cost, and timing questions as generators, while interdependent '
                              "projects mean 'a single project withdrawal can force studies to be rerun' "
                              "[ObxvY1JRruo @ 00:05:23]. Keentel's CAISO IPE 5.0 briefing confirms the "
                              'door is opening: the non-LSE affidavit no longer needs to cite '
                              "sustainability, only the project's value to the organization, which opens "
                              'the path for data centers and industrial operators while keeping the '
                              '25-point award and one-project-per-cluster limit [VdwOf6TKl6U @ 00:01:01]. '
                              "Dirt to Data's investor checklist makes the final point: 'notice that "
                              "acreage isn't on that list.'"],
               'table': {'caption': 'Where the practitioners agree on queue reality and Order 2023 '
                                    'baseline mechanics',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Queue megawatts are proposals, not plants',
                                   'A request only starts connection studies and is not proof of '
                                   'financing, construction, or operation',
                                   'Treat queued capacity near a target site as unbuilt until it reaches '
                                   'commercial operation',
                                   'Blueprint States ([v2cs7ZXTQH0 @ 00:00:18])'],
                                  ['Attrition dwarfs completions in the current queue',
                                   'In 2025, 14 GW were withdrawn for every 1 GW connected, and storage '
                                   'fell 16%',
                                   'Read queue shrinkage as dropouts clearing out, not as projects '
                                   'actually getting built',
                                   'Stats in Motion ([Z2FdaH10ZCY @ 00:00:15])'],
                                  ['Cost follows electrical impact rather than nameplate megawatts',
                                   'Location, topology, the POI, and other cluster projects all drive the '
                                   'allocated upgrade bill',
                                   'Expect financial risk to sit many electrical miles away from the '
                                   'chosen POI',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:05:24])'],
                                  ['Readiness now beats speed in cluster entry',
                                   'TVA requires 100% site control and a 45-day window with flat position '
                                   'inside a cluster',
                                   'Arrive with land and cash locked, because missing the window means '
                                   'waiting a year',
                                   'Keentel Engineering ([gGBYCEdn18o @ 00:00:52])'],
                                  ['Deadlines are firm and carry appealable penalties under the order',
                                   'Reasonable-efforts standard was replaced by firm transmission provider '
                                   'deadlines with appealable penalties',
                                   'Build schedules around fixed study dates rather than open-ended '
                                   'provider best efforts',
                                   'WIRES ([-BTpIv2G5-0 @ 00:08:40])'],
                                  ['Large AI loads now queue like generators do',
                                   'Campuses requesting hundreds of megawatts raise overload, upgrade, '
                                   'protection, cost, and timing questions',
                                   'Underwrite data-center land on queue position and timing, not acreage '
                                   'near a line',
                                   'Dirt to Data ([264d0wu5W4k @ 00:02:34])'],
                                  ['Cost estimates strongly predict who walks away',
                                   'Costs above $100/kW make withdrawal 22 percentage points, about 49%, '
                                   'more likely in PJM',
                                   'Track cost estimate movement between studies as the leading indicator '
                                   'of cluster dropouts',
                                   'Environmental Defense Fund ([M62wgLYBKBw @ 00:33:36])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The cash ladder is where Order 2023 bites. Keentel's TVA walkthrough lists "
                              'a $25K nonrefundable fee, study deposits of $150K under 75 MW, $200K for 75 '
                              'to 199 MW and $300K at 200 MW and up, a readiness deposit at 2x the study '
                              'deposit with $925K stated for the 200 MW-plus tier, and a schedule running '
                              'from a January 15 window through a 60-day engagement, 150-day study, '
                              '150-day restudy and 180-day facilities study [gGBYCEdn18o @ 00:01:09]. '
                              'Withdrawal penalties climb from 2x deposit to the greater of 2x or 5%, then '
                              '2x or 10%, and 20% after the LGIA, with off-ramps for no material effect, a '
                              'restudy cost jump above 25%, or a facilities-study jump above 100% '
                              '[gGBYCEdn18o @ 00:03:16]. Keentel adds that queue position is transferable '
                              "and 'any POI change is always a material modification.' On ISO-NE's "
                              'transitional cluster, the same engineers priced exposure for a 200 MW '
                              'project carrying $178M of allocation at $8.9M at 5%, $17.88M at 10% and '
                              '$35.6M at 20% [TM7qt8CCWxk @ 00:09:17]. Matthew Crosby of Cypress Creek '
                              'told the WIRES panel milestone payments step to 5% then 10%, while MISO '
                              'uses 10% then 20%, and pushed site control that covers the gen-tie all the '
                              'way to the POI [-BTpIv2G5-0 @ 00:44:50].',
                              "Keentel's DFAX worked example is the core screening math every POI "
                              'shortlist should run. A 240 MVA line carrying 200 MVA of base flow takes '
                              'impacts of 50, 30 and 5 MVA from projects A, B and C, pushing it to 285 MVA '
                              'or 118%; a $40M upgrade split by megawatts lands at $17.8M, $13.3M and '
                              '$8.9M, but split by impact it becomes $23.5M, $14.1M and $2.4M [TM7qt8CCWxk '
                              '@ 00:15:28]. In the ISO-NE cluster of 23 projects and 4,826.5 MW, total '
                              'cost hit $3.21B with system upgrades at $2.54B or 79%, substation $581M or '
                              '18%, and interconnection facilities just $75.5M, while 115 kV averaged '
                              'about $831/kW against roughly $453/kW at 345 kV [TM7qt8CCWxk @ 00:07:36]. '
                              "Sarah Johnson's PJM data puts the median cost near $50/kW and the 90th "
                              'percentile near $400/kW against roughly $1,500/kW to install, with 13% of '
                              'estimates shifting more than $100/kW between studies [M62wgLYBKBw @ '
                              '00:32:27]. Casey Cathey frames the same allocation as a highway where the '
                              'last car pays for the new lane, with typical surviving costs around $7M '
                              'versus the $200 to $400M figures [6zj9DYoE8-U @ 00:09:59].',
                              "Speed now comes from software and staffing. At the ESIG workshop, SPP's "
                              'Swerzik credited the GridUnity-built SIMS with about 50% time savings and '
                              "SUGAR 2 with automating phase 1 at roughly 8x speed, while MISO's Westfall "
                              "reported Pearl Street 'has no AI,' matched 99% of constraints in "
                              'benchmarking, and produces upgrades plus costs in under a day before '
                              "transmission owners adjust about 20% [nFQOwcyPbbE @ 00:29:50]. PJM's "
                              'Velock, by contrast, doubled staff and issued about 200 agreements in one '
                              'day. Casey Cathey told Nebraska Wind and Solar that Hitachi/Nvidia GPUs run '
                              '80% faster and cut model solves from about a year to two months, with the '
                              'SPP queue dashboard updated twice weekly [6zj9DYoE8-U @ 00:27:38]. In '
                              "ERCOT, Keentel warns a signed SGIA is a 'false summit': the QSA cycle runs "
                              'quarterly, so a missed prerequisite or failed model quality test slips '
                              'synchronization a full quarter and costs millions in revenue; PSCAD EMT is '
                              'mandatory for all IBRs, as-built models must match exact inverter firmware '
                              "and PPC settings, and vendor data lockdown is the 'single biggest schedule "
                              "risk' [YabOCr0t9pI @ 00:00:58]. Their fix is a single unified study package "
                              'that satisfies both ERCOT and the TSP [YabOCr0t9pI @ 00:03:00].'],
               'table': {'caption': 'Street-level numbers, deposits, tools and timelines practitioners '
                                    'quoted',
                         'headers': ['Mechanic',
                                     'Number or Specification',
                                     'Where It Applies',
                                     'Expert Source'],
                         'rows': [['TVA study deposit tiers by project size',
                                   '$150K under 75 MW, $200K for 75 to 199 MW, $300K at 200 MW-plus',
                                   'TVA LGIP clusters for projects over 20 MW from November 2024',
                                   'Keentel Engineering ([gGBYCEdn18o @ 00:01:09])'],
                                  ['TVA withdrawal penalty ladder through each study phase',
                                   '2x deposit, then max of 2x or 5%, max of 2x or 10%, 20% post-LGIA',
                                   'Escalates as projects advance from study through executed LGIA',
                                   'Keentel Engineering ([gGBYCEdn18o @ 00:03:16])'],
                                  ['DFAX impact-based split of a shared upgrade',
                                   '$40M upgrade becomes $23.5M, $14.1M and $2.4M by impact instead of MW',
                                   'Overloaded 240 MVA line pushed to 285 MVA, or 118%, by three projects',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:15:28])'],
                                  ['Voltage level cost gap in the ISO-NE cluster',
                                   '115 kV averaged about $831/kW versus roughly $453/kW at 345 kV',
                                   'ISO-NE transitional cluster totaling 4,826.5 MW and $3.21B in upgrades',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:07:36])'],
                                  ['SPP SIMS and SUGAR 2 automation gains',
                                   'About 50% time savings from SIMS, roughly 8x speed on phase 1',
                                   'SPP cluster studies, including the 12-month DISIS-2024 study timeframe',
                                   'Energy Systems Integration Group ([nFQOwcyPbbE @ 00:07:20])'],
                                  ['MISO automated upgrade and cost production with Pearl Street',
                                   'Upgrades plus costs in under a day; transmission owners adjust about '
                                   '20%',
                                   'MISO queue capped at 50% of load after 171 GW 2022 cycle',
                                   'Energy Systems Integration Group ([nFQOwcyPbbE @ 00:29:50])'],
                                  ['CAISO full-allocation cap for large load-serving entities',
                                   'Lesser of 50% of forecasted RA load share or 500 MW; energy-only '
                                   'uncapped',
                                   'CAISO IPE 5.0, effective for Cluster 16 opening October 1, 2026',
                                   'Keentel Engineering ([VdwOf6TKl6U @ 00:01:56])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the engineers and developers actually work a cluster',
                           'body': 'Tactics practitioners teach for surviving cluster studies, controlling '
                                   'allocated cost, and jumping the wait.',
                           'items': ['Screen POIs with DFAX before filing, test multiple project sizes, '
                                     'have PSSE and PSCAD models ready, shadow the study, and rebut '
                                     'results you can disprove [Keentel Engineering — TM7qt8CCWxk @ '
                                     '00:19:45]',
                                     'For arbitrage-focused BESS, consider the ERIS downgrade option to '
                                     'shed deliverability-driven upgrade exposure [Keentel Engineering — '
                                     'TM7qt8CCWxk @ 00:13:03]',
                                     'Buy old solar farms for their existing grid position and add '
                                     'batteries to skip waits of more than 5 years, but model the voltage '
                                     'profile and protection settings before buying [Stats in Motion — '
                                     'Z2FdaH10ZCY @ 00:01:07]',
                                     'Frontload POI design and lock site control covering the gen-tie all '
                                     'the way to the POI before entering the cluster [WIRES — -BTpIv2G5-0 '
                                     '@ 01:05:27]']},
               'sop_steps': [{'step': 1,
                              'title': 'Understand the node',
                              'action': 'Run DFAX screening on every candidate POI and test multiple sizes '
                                        'before committing a deposit.',
                              'detail': "Keentel's first rule is 'First, understand the node,' because the "
                                        'cluster neighbors and electrical topology set your allocated '
                                        'bill, not your megawatts [Keentel Engineering — TM7qt8CCWxk @ '
                                        '00:19:29]'},
                             {'step': 2,
                              'title': 'Lock site control and the cash ladder',
                              'action': 'Secure 100% site control and fund study plus readiness deposits '
                                        'before the window opens.',
                              'detail': 'TVA requires 100% site control with a $25K fee and study deposits '
                                        'up to $300K; the window opens January 15 and missing it means '
                                        'waiting a year [Keentel Engineering — gGBYCEdn18o @ 00:01:29]'},
                             {'step': 3,
                              'title': 'Freeze vendor data and build as-built models',
                              'action': 'Lock inverter firmware and PPC settings, then submit PSSE and '
                                        'PSCAD EMT models whose MQT curves overlay.',
                              'detail': 'ERCOT enforces strict as-built lockdowns, PSCAD EMT is mandatory '
                                        'for IBRs, and vendor data lockdown is the single biggest schedule '
                                        'risk [Keentel Engineering — YabOCr0t9pI @ 00:05:06]'},
                             {'step': 4,
                              'title': 'Shadow the study and watch the off-ramps',
                              'action': 'Track restudy and facilities-study cost moves against the '
                                        'withdrawal thresholds at each phase.',
                              'detail': 'TVA off-ramps trigger on a restudy cost increase over 25% or a '
                                        "facilities-study increase over 100%, 'your protection against "
                                        "economics the studies quietly destroy' [Keentel Engineering — "
                                        'gGBYCEdn18o @ 00:03:52]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["Automation splits the grid operators into two camps. MISO's Westfall runs "
                              'Pearl Street, a tool that “has no AI,” and reports benchmarking with 99% of '
                              'constraints matching, plus upgrades and costs produced in under a day '
                              '[nFQOwcyPbbE @ 00:25:02]. The catch is that transmission owners still '
                              'adjust roughly 20% of those outputs, summed up in the line “Well, that '
                              "ain't going to work.” PJM's Velock pushes back harder, framing AI as "
                              'possibly “80% right” and “not ready for prime time yet” [nFQOwcyPbbE @ '
                              "00:46:21]. PJM's alternative playbook was brute force: staff doubled, about "
                              '200 agreements went out in a single day, the backlog was cut 63%, and the '
                              'backlog clears by April. SPP sits between the two camps. It pairs '
                              "GridUnity's SIMS, which delivered about 50% time savings, with SUGAR 2 "
                              'automating phase 1 at roughly 8x speed, and Casey Cathey adds that Hitachi '
                              'and Nvidia GPUs run 80% faster, dropping model solves from about a year to '
                              "two months [6zj9DYoE8-U @ 00:27:38]. Cypress Creek's Matthew Crosby argues "
                              'the unlock sits upstream: a technical conference on study criteria so '
                              'automation has consistent rules to run against [-BTpIv2G5-0 @ 00:26:19]. '
                              'Automated screens move fast, but transmission owners still rewrite roughly '
                              'one in five results.',
                              'The second fault line is who gets into the queue and who pays once inside. '
                              "Cypress Creek's Matthew Crosby opposed any term-sheet or IRP precondition "
                              'for entering the queue while backing DFAX impact-based cost allocation '
                              '[-BTpIv2G5-0 @ 00:45:40]. Keentel Engineering shows why the method moves '
                              'real money: on a $40M upgrade, splitting by MW charges three projects '
                              '$17.8M, $13.3M and $8.9M, while splitting by impact charges $23.5M, $14.1M '
                              'and $2.4M [TM7qt8CCWxk @ 00:15:28]. As Keentel puts it, cost follows '
                              'impact, not MW. Andy Knows It argues reform left the core economics intact, '
                              "because Order 2023 “didn't change who pays,” and RMI found PJM's first "
                              'reformed cluster of 2018-2020 applicants still carried long timelines and '
                              'high costs [QxDqhnba2Jg @ 00:08:43]. On gating, Sarah Johnson of UW '
                              'Madison, presenting for the Environmental Defense Fund, ran '
                              'counterfactuals: a $900k per-generator entry fee adds about 7 GW, mostly '
                              'non-renewable, while per-MW fees and later-study fees are weaker '
                              '[M62wgLYBKBw @ 00:48:51]. Reprioritization adds about 8 GW total and 1.5 GW '
                              'of renewables, mostly by removing small projects, and weighting renewables '
                              '3x yields 4.1 GW, of which 2.7 GW is renewable. Johnson also found raising '
                              'fees still left many entrants, because wait times are so long there is a '
                              'lot of true uncertainty.',
                              'Service type and shortcut strategies draw the sharpest contrasts. Karen '
                              "Herzfeld, from FERC Chairman Phillips' office, called connect-and-manage "
                              'worth exploring while conceding it is unclear how it works with capacity '
                              "markets [-BTpIv2G5-0 @ 00:38:00]. SPP's Casey Cathey countered on the same "
                              'WIRES panel that connect-and-manage ignores stability, subsynchronous and '
                              'EMT limits [-BTpIv2G5-0 @ 00:51:06]. Herzfeld noted alternative '
                              'technologies must be evaluated but need not be deployed, and Cathey called '
                              'the alternative-technology cost estimates burdensome. Cathey also warned '
                              'that ERIS-based affected-system studies reduce interregional transmission, '
                              'while Keentel Engineering pitches the ERIS downgrade as a deliberate option '
                              "for arbitrage-focused BESS [TM7qt8CCWxk @ 00:13:03]. LBNL's Gorman adds "
                              'that ERIS and NRIS timelines diverged around 2018-2019 and the low-cost '
                              'ERIS share has fallen since about 2014, while Southern Company sees little '
                              'meaning in the distinction. The most aggressive playbook comes from Stats '
                              'in Motion: buy old solar farms for their grid position and add batteries to '
                              'skip waits of more than five years [Z2FdaH10ZCY @ 00:01:07]. The same '
                              'channel predicts PJM, as FERC ordered, will require full studies for '
                              'retrofits. Before reform, Andy Knows It reports, entry was nearly free and '
                              "developers filed on land they didn't control just to hold queue position; "
                              'Order 2023 answered with site control, which Herzfeld put at 90% at entry '
                              'and 100% by facility study.'],
               'table': {'caption': 'Contested queue playbooks: where named practitioners split on '
                                    'automation, gating, cost allocation and shortcuts',
                         'headers': ['Contested Question',
                                     'Camp A Playbook',
                                     'Camp B Playbook',
                                     'Expert Source'],
                         'rows': [['Should AI and automation produce binding interconnection study results '
                                   'today?',
                                   'MISO Pearl Street matched 99% of constraints and produced upgrades '
                                   'plus costs in under a day',
                                   "PJM's Velock calls AI possibly 80% right and not ready for prime time "
                                   'yet',
                                   'Energy Systems Integration Group ([nFQOwcyPbbE @ 00:25:02]); Energy '
                                   'Systems Integration Group ([nFQOwcyPbbE @ 00:46:21])'],
                                  ['How should a shared network upgrade cost be split across a cluster?',
                                   'Split by MW, a $40M upgrade charges three projects $17.8M, $13.3M and '
                                   '$8.9M',
                                   'Split by DFAX impact, the same upgrade charges $23.5M, $14.1M and '
                                   '$2.4M',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:15:28])'],
                                  ['Should queue entry require a term sheet or IRP precondition at all?',
                                   'Crosby of Cypress Creek opposed any term-sheet or IRP gate for '
                                   'entering the queue',
                                   'FERC dropped non-financial readiness requirements and kept site '
                                   'control at 90% then 100%',
                                   'WIRES ([-BTpIv2G5-0 @ 00:21:08]); WIRES ([-BTpIv2G5-0 @ 00:07:36])'],
                                  ['Is connect-and-manage a workable shortcut for faster grid '
                                   'interconnection?',
                                   'Herzfeld calls it worth exploring but unclear alongside existing '
                                   'capacity market designs',
                                   'Cathey says connect-and-manage ignores stability, subsynchronous and '
                                   'EMT limits on the system',
                                   'WIRES ([-BTpIv2G5-0 @ 00:38:00]); WIRES ([-BTpIv2G5-0 @ 00:51:06])'],
                                  ['Which entry gate adds the most total capacity to the queue?',
                                   'A $900k per-generator entry fee adds about 7 GW, mostly non-renewable '
                                   'capacity',
                                   'Per-MW and later-study fees are weaker; reprioritization adds about 8 '
                                   'GW mostly removing small projects',
                                   'Environmental Defense Fund ([M62wgLYBKBw @ 00:48:51])'],
                                  ['How should a readiness-based cluster handle requests that are not '
                                   'ready?',
                                   'CAISO scores readiness, policy fit and transmission; IPE 5.0 affidavit '
                                   'only attests organizational value',
                                   "SPP CPP moves requests that aren't ready into the next cycle with no "
                                   'restudies',
                                   'Andy Knows It ([QxDqhnba2Jg @ 00:12:43]); Keentel Engineering '
                                   '([VdwOf6TKl6U @ 00:01:01]); Nebraska Wind and Solar ([6zj9DYoE8-U @ '
                                   '00:42:34])'],
                                  ['Will federal planning reform clear the transmission bottleneck behind '
                                   'the queue?',
                                   'Order 1920 adds a 20-year planning horizon updated every 5 years with '
                                   'GETs and reconductoring',
                                   'Andy Knows It says Order 1920 requires long planning but does not help '
                                   'projects today',
                                   'Decarbonize! ([DgivMHf303Y @ 00:05:09]); Andy Knows It ([QxDqhnba2Jg @ '
                                   '00:11:51])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap is treating a signed agreement as the finish line. Keentel '
                              'Engineering calls the ERCOT SGIA a “false summit” and warns “The reality is '
                              'far harsher.” The QSA runs quarterly, so a missed prerequisite or failed '
                              'model quality test slips synchronization by a full quarter, costing '
                              '“millions of dollars” in revenue [YabOCr0t9pI @ 00:00:58]. The engineering '
                              'gauntlet answers to two masters: ERCOT checks macro stability in PSSE v36, '
                              'TSAT and PSCAD, while TSPs such as Oncor, CenterPoint, ETT, LCRA, CPS and '
                              'Austin Energy each apply their own relay, harmonic, inrush and RTU/ICCP '
                              'rules. PSCAD EMT is mandatory for all IBRs, and if MQT curves fail to '
                              'overlay across all models, the submittal is rejected [YabOCr0t9pI @ '
                              '00:05:25]. Keentel flags vendor data lockdown as the “single biggest '
                              'schedule risk,” and as-built models must reflect exact inverter firmware '
                              'and PPC settings. On the cluster side, the same firm warns of a “hardware '
                              'penalty” from generic models, because “These upgrades can be extremely '
                              'expensive” [TM7qt8CCWxk @ 00:17:28]. Blueprint States lays out the full '
                              'path, from request to cluster studies to allocated upgrades to an '
                              'agreement, and stresses that an agreement still does not mean commercial '
                              'operation [v2cs7ZXTQH0 @ 00:01:18].',
                              'Study results can wreck a pro forma overnight. In the ISO-NE transitional '
                              'cluster, 23 projects totaling 4,826.5 MW drew $3.21B in upgrades, with '
                              'allocations ranging from $0 to $541M, or $0 to $2,700/kW [TM7qt8CCWxk @ '
                              '00:05:05]. Upgrades of up to 93 months meant more than seven years of '
                              'delay. Keentel prices the exit on a 200 MW project with $178M allocated at '
                              '$8.9M at 5%, $17.88M at 10% and $35.6M at 20% [TM7qt8CCWxk @ 00:09:17]. '
                              "Sarah Johnson's PJM data shows the volatility underneath: a median cost of "
                              'about $50/kW, a 90th percentile of about $400/kW, 13% of estimates shifting '
                              'by more than $100/kW between studies, and costs above $100/kW making '
                              'withdrawal 22 percentage points more likely [M62wgLYBKBw @ 00:33:36]. Andy '
                              'Knows It cites Berkeley and RMI work showing developers walk away once '
                              'interconnection exceeds 10% of capex. GridState describes the cascade: “A '
                              'single project withdrawal can force studies to be rerun,” and “Suddenly, a '
                              'project that looked profitable no longer works financially” [ObxvY1JRruo @ '
                              "00:04:22]. TVA's counter is a set of off-ramps for no material effect, a "
                              'more than 25% cost increase in restudy, or a more than 100% increase in the '
                              'facilities study, which Keentel calls “your protection against economics '
                              'the studies quietly destroy.”',
                              'The remaining traps are physical and calendar-driven. Stats in Motion warns '
                              'that the grid-position retrofit play carries hidden engineering: batteries '
                              'are bidirectional, change fault-current behavior so relays may be '
                              'miscalibrated, and push transformers sized for solar into thermal stress, '
                              'so a 40 MW site could be curtailed to 20 MW [Z2FdaH10ZCY @ 00:02:49]. Its '
                              'fix is to model the voltage profile and protection settings before buying. '
                              'Dirt to Data frames the calendar trap bluntly: power in 2033 against a 2028 '
                              'need means no project, because “Queue and timing are inseparable” '
                              '[264d0wu5W4k @ 00:04:48]. The same channel stresses that 300 acres near a '
                              'line can still be blocked by queued generators and other large loads, and '
                              'that acreage does not appear on the investor question list. Study '
                              'throughput compounds the delay. Crosby reported only about 1% of PJM '
                              'facility studies on time and a simple line tap that took four to five '
                              'years, while Cathey said consultants are turning away work [-BTpIv2G5-0 @ '
                              "00:59:40]. Johnson's PJM data puts facility studies at a 16-month median "
                              'against a 6-month official timeline, with a 90th percentile of 35 months, '
                              'and documents the downstream damage: land options expire and PPAs slip '
                              '[M62wgLYBKBw @ 00:26:14]. Johnson also puts renewables that never operate '
                              'at about 85%, versus 68% of fossil.'],
               'table': {'caption': 'Firsthand failure modes, reported damage and the operator check each '
                                    'practitioner teaches',
                         'headers': ['Failure Mode',
                                     'Reported Damage Or Number',
                                     'Operator Check',
                                     'Expert Source'],
                         'rows': [['Treating a signed ERCOT SGIA as clearance to energize the plant',
                                   'A missed prerequisite slips sync a full quarter, costing millions of '
                                   'dollars in revenue',
                                   'Lock vendor data and pass MQT overlays before the quarterly QSA window '
                                   'closes',
                                   'Keentel Engineering ([YabOCr0t9pI @ 00:00:58])'],
                                  ['Submitting generic equipment models into the cluster study instead of '
                                   'real hardware',
                                   'A hardware penalty triggers upgrades that can be extremely expensive '
                                   'for the project',
                                   'Have PSSE and PSCAD models ready with actual equipment data before the '
                                   'study runs',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:17:28]); Keentel Engineering '
                                   '([TM7qt8CCWxk @ 00:19:45])'],
                                  ['Withdrawing late after a large network upgrade allocation lands on the '
                                   'project',
                                   'A 200 MW project with $178M allocated faces $8.9M, $17.88M or $35.6M '
                                   'exits',
                                   'Track TVA-style off-ramps at more than 25% restudy or 100% facilities '
                                   'study increases',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:09:17]); Keentel Engineering '
                                   '([gGBYCEdn18o @ 00:03:52])'],
                                  ['Filing at a low-voltage POI without screening the surrounding '
                                   'electrical topology first',
                                   '115 kV averaged about $831/kW versus about $453/kW at 345 kV in ISO-NE',
                                   'Screen POIs with DFAX and test multiple project sizes before filing '
                                   'the request',
                                   'Keentel Engineering ([TM7qt8CCWxk @ 00:07:36]); Keentel Engineering '
                                   '([TM7qt8CCWxk @ 00:19:45])'],
                                  ['Bolting batteries onto an acquired solar POI without new protection '
                                   'engineering',
                                   'Relays miscalibrated, solar-sized transformers thermally stressed, a '
                                   '40 MW site curtailed to 20 MW',
                                   'Model the voltage profile and protection settings before buying the '
                                   'existing site',
                                   'Stats in Motion ([Z2FdaH10ZCY @ 00:02:49]); Stats in Motion '
                                   '([Z2FdaH10ZCY @ 00:03:21])'],
                                  ['Securing a queue position whose power date misses the load need date',
                                   'Power arriving in 2033 against a 2028 need means there is no project',
                                   'Underwrite queue position and timing together as one inseparable '
                                   'diligence question',
                                   'Dirt to Data ([264d0wu5W4k @ 00:04:48])'],
                                  ['Reading a shrinking queue headline as proof that reform is working',
                                   'In 2025, 14 GW withdrew for every 1 GW connected; battery applications '
                                   'dropped 32%',
                                   'Track withdrawals and completions separately instead of trusting '
                                   'headline queue totals',
                                   'Stats in Motion ([Z2FdaH10ZCY @ 00:00:15]); Andy Knows It '
                                   '([QxDqhnba2Jg @ 00:07:17])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Checks Before Posting the Next Deposit',
                           'body': 'Each check below comes straight from losses, slips and curtailments '
                                   'the practitioners reported. Fail any one and the deal does not advance '
                                   'to the next milestone payment.',
                           'items': ['Do not book revenue at SGIA signing: a failed model quality test or '
                                     'missed prerequisite slips sync a full quarterly QSA cycle and costs '
                                     'millions of dollars [Keentel Engineering — YabOCr0t9pI @ 00:00:58].',
                                     'Price the withdrawal ladder before posting: on 200 MW with $178M '
                                     'allocated, exits run $8.9M at 5%, $17.88M at 10% and $35.6M at 20% '
                                     '[Keentel Engineering — TM7qt8CCWxk @ 00:09:17].',
                                     'Flag any estimate above $100/kW as a kill risk: it makes withdrawal '
                                     '22 percentage points more likely, and 13% of estimates move more '
                                     'than $100/kW between studies [Environmental Defense Fund — '
                                     'M62wgLYBKBw @ 00:33:36].',
                                     'Never buy a solar POI for a battery retrofit without modeling fault '
                                     'current, relays and transformer thermal limits; a 40 MW site could '
                                     'be curtailed to 20 MW [Stats in Motion — Z2FdaH10ZCY @ '
                                     '00:02:49].']}}],
 'pull_quote': '“Your costs are coupled to your neighbors.” — Keentel Engineering (gGBYCEdn18o @ '
               '00:04:44).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Start with the node: screen candidate POIs with DFAX before filing, because cost '
                      'follows impact, not MW [Keentel Engineering — TM7qt8CCWxk @ 00:19:29].',
                      'Line up 100% site control and posting cash before a TVA window: $25K nonrefundable '
                      'fee, $150K/$200K/$300K study deposit by size, and a readiness deposit of 2x the '
                      'study deposit [Keentel Engineering — gGBYCEdn18o @ 00:01:09].',
                      'Build one unified study package that satisfies both ERCOT stability reviews and the '
                      "TSP's local protection, harmonic and inrush rules [Keentel Engineering — "
                      'YabOCr0t9pI @ 00:03:00].',
                      'Test multiple project sizes, keep PSSE and PSCAD models ready, shadow the utility '
                      'study, and rebut results that do not match [Keentel Engineering — TM7qt8CCWxk @ '
                      '00:19:45].',
                      'Monitor the SPP queue dashboard, which is updated twice weekly, to track cluster '
                      'volume and position shifts [Nebraska Wind and Solar — 6zj9DYoE8-U @ 00:17:24].',
                      'Frontload POI design and make site control cover the gen-tie all the way to the POI '
                      '[WIRES — -BTpIv2G5-0 @ 01:05:27].'],
 'statutory_citations': [{'title': 'Keentel Engineering — FERC Order 2023 Cluster Interconnection Studies '
                                   '| Costs, POI & Network Upgrades [00:09:17]',
                          'url': 'https://www.youtube.com/watch?v=TM7qt8CCWxk&t=557s',
                          'relevance': 'Primary practitioner testimony on withdrawal penalty exposure for '
                                       'a 200 MW project with $178M of allocated upgrades.'},
                         {'title': 'WIRES — WIRES 2023 Fall Meeting Panel 1 – FERC Order 2023 [00:06:55]',
                          'url': 'https://www.youtube.com/watch?v=-BTpIv2G5-0&t=415s',
                          'relevance': 'Primary practitioner testimony on Order 2023 site control '
                                       'thresholds of 90% at entry and 100% by facility study.'},
                         {'title': 'Keentel Engineering — TVA Interconnection Queue Reform Explained | New '
                                   'Cluster Process, Deposits & Costs [00:03:16]',
                          'url': 'https://www.youtube.com/watch?v=gGBYCEdn18o&t=196s',
                          'relevance': 'Primary practitioner testimony on the TVA withdrawal penalty '
                                       'ladder and cost-increase off-ramps.'},
                         {'title': 'Environmental Defense Fund — An Empirical Analysis of the '
                                   'Interconnection Queue - January 2024 [00:33:36]',
                          'url': 'https://www.youtube.com/watch?v=M62wgLYBKBw&t=2016s',
                          'relevance': 'Primary practitioner testimony on costs above $100/kW raising '
                                       'withdrawal probability by 22 percentage points.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'YabOCr0t9pI',
                       'title': 'Post-SGIA Interconnection Studies in ERCOT | From SGIA to Grid '
                                'Synchronization | Keentel Engineering',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'But it is not the finish line.',
                       'tip': 'But it is not the finish line.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=YabOCr0t9pI&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=YabOCr0t9pI&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nFQOwcyPbbE',
                       'title': '2025 Fall Workshop: Session 3B: Modernizing Interconnection Queue: AI, '
                                'Automation, & Process Reform',
                       'channel': 'Energy Systems Integration Group',
                       'author': 'Energy Systems Integration Group',
                       'text': "That's not ready for prime time yet.",
                       'tip': "That's not ready for prime time yet.",
                       'timestamp': 2800,
                       'timestamp_seconds': 2800,
                       'timestamp_label': '[00:46:40]',
                       'url': 'https://www.youtube.com/watch?v=nFQOwcyPbbE&t=2800s',
                       'markdown': '[00:46:40](https://www.youtube.com/watch?v=nFQOwcyPbbE&t=2800s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '264d0wu5W4k',
                       'title': 'What Is an Interconnection Queue',
                       'channel': 'Dirt to Data',
                       'author': 'Dirt to Data',
                       'text': 'Queue and timing are inseparable.',
                       'tip': 'Queue and timing are inseparable.',
                       'timestamp': 288,
                       'timestamp_seconds': 288,
                       'timestamp_label': '[00:04:48]',
                       'url': 'https://www.youtube.com/watch?v=264d0wu5W4k&t=288s',
                       'markdown': '[00:04:48](https://www.youtube.com/watch?v=264d0wu5W4k&t=288s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TM7qt8CCWxk',
                       'title': 'FERC Order 2023 Cluster Interconnection Studies | Costs, POI & Network '
                                'Upgrades',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': "Location matters, electrical topology matters, the project's point of "
                               'interconnection matters, and critically, the other projects in the cluster '
                               'matter.',
                       'tip': "Location matters, electrical topology matters, the project's point of "
                              'interconnection matters, and critically, the other projects in the cluster '
                              'matter.',
                       'timestamp': 324,
                       'timestamp_seconds': 324,
                       'timestamp_label': '[00:05:24]',
                       'url': 'https://www.youtube.com/watch?v=TM7qt8CCWxk&t=324s',
                       'markdown': '[00:05:24](https://www.youtube.com/watch?v=TM7qt8CCWxk&t=324s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TM7qt8CCWxk',
                       'title': 'FERC Order 2023 Cluster Interconnection Studies | Costs, POI & Network '
                                'Upgrades',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'The real financial risk may be many electrical miles away from the point '
                               'of interconnection.',
                       'tip': 'The real financial risk may be many electrical miles away from the point of '
                              'interconnection.',
                       'timestamp': 440,
                       'timestamp_seconds': 440,
                       'timestamp_label': '[00:07:20]',
                       'url': 'https://www.youtube.com/watch?v=TM7qt8CCWxk&t=440s',
                       'markdown': '[00:07:20](https://www.youtube.com/watch?v=TM7qt8CCWxk&t=440s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gGBYCEdn18o',
                       'title': 'TVA Interconnection Queue Reform Explained | New Cluster Process, '
                                'Deposits & Costs',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'The competitive dynamic has shifted from speed to readiness.',
                       'tip': 'The competitive dynamic has shifted from speed to readiness.',
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=gGBYCEdn18o&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=gGBYCEdn18o&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gGBYCEdn18o',
                       'title': 'TVA Interconnection Queue Reform Explained | New Cluster Process, '
                                'Deposits & Costs',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Your costs are coupled to your neighbors.',
                       'tip': 'Your costs are coupled to your neighbors.',
                       'timestamp': 284,
                       'timestamp_seconds': 284,
                       'timestamp_label': '[00:04:44]',
                       'url': 'https://www.youtube.com/watch?v=gGBYCEdn18o&t=284s',
                       'markdown': '[00:04:44](https://www.youtube.com/watch?v=gGBYCEdn18o&t=284s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-BTpIv2G5-0',
                       'title': 'WIRES 2023 Fall Meeting Panel 1 – FERC Order 2023',
                       'channel': 'WIRES',
                       'author': 'WIRES',
                       'text': 'Only about 1% of PJM facility studies were completed on time.',
                       'tip': 'Only about 1% of PJM facility studies were completed on time.',
                       'timestamp': 1370,
                       'timestamp_seconds': 1370,
                       'timestamp_label': '[00:22:50]',
                       'url': 'https://www.youtube.com/watch?v=-BTpIv2G5-0&t=1370s',
                       'markdown': '[00:22:50](https://www.youtube.com/watch?v=-BTpIv2G5-0&t=1370s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-BTpIv2G5-0',
                       'title': 'WIRES 2023 Fall Meeting Panel 1 – FERC Order 2023',
                       'channel': 'WIRES',
                       'author': 'WIRES',
                       'text': 'Connect-and-manage ignores stability, subsynchronous, and EMT limits.',
                       'tip': 'Connect-and-manage ignores stability, subsynchronous, and EMT limits.',
                       'timestamp': 3066,
                       'timestamp_seconds': 3066,
                       'timestamp_label': '[00:51:06]',
                       'url': 'https://www.youtube.com/watch?v=-BTpIv2G5-0&t=3066s',
                       'markdown': '[00:51:06](https://www.youtube.com/watch?v=-BTpIv2G5-0&t=3066s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z2FdaH10ZCY',
                       'title': "The Interconnection Queue Shrank. That's Not Good News",
                       'channel': 'Stats in Motion',
                       'author': 'Stats in Motion',
                       'text': 'That reading is wrong.',
                       'tip': 'That reading is wrong.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=Z2FdaH10ZCY&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=Z2FdaH10ZCY&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DgivMHf303Y',
                       'title': 'Why We’re Totally FERC’d: Plan for the Grid We Need or Sit in the Cold '
                                'and Dark',
                       'channel': 'Decarbonize!',
                       'author': 'Decarbonize!',
                       'text': 'FERC cannot build or force transmission; it only writes the rules.',
                       'tip': 'FERC cannot build or force transmission; it only writes the rules.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=DgivMHf303Y&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=DgivMHf303Y&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6zj9DYoE8-U',
                       'title': 'SPP Generation Interconnection Queue Process and Current Backlog',
                       'channel': 'Nebraska Wind and Solar',
                       'author': 'Nebraska Wind and Solar',
                       'text': 'So, 34 gigawatts we have processed.',
                       'tip': 'So, 34 gigawatts we have processed.',
                       'timestamp': 1243,
                       'timestamp_seconds': 1243,
                       'timestamp_label': '[00:20:43]',
                       'url': 'https://www.youtube.com/watch?v=6zj9DYoE8-U&t=1243s',
                       'markdown': '[00:20:43](https://www.youtube.com/watch?v=6zj9DYoE8-U&t=1243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6zj9DYoE8-U',
                       'title': 'SPP Generation Interconnection Queue Process and Current Backlog',
                       'channel': 'Nebraska Wind and Solar',
                       'author': 'Nebraska Wind and Solar',
                       'text': "It's a 500-page tariff change.",
                       'tip': "It's a 500-page tariff change.",
                       'timestamp': 2573,
                       'timestamp_seconds': 2573,
                       'timestamp_label': '[00:42:53]',
                       'url': 'https://www.youtube.com/watch?v=6zj9DYoE8-U&t=2573s',
                       'markdown': '[00:42:53](https://www.youtube.com/watch?v=6zj9DYoE8-U&t=2573s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VdwOf6TKl6U',
                       'title': 'CAISO IPE 5.0 Explained | Cluster 16 Interconnection Changes | Solar & '
                                'BESS Developers Guide',
                       'channel': 'Keentel Engineering',
                       'author': 'Keentel Engineering',
                       'text': 'Projects failing CVC will be withdrawn from the queue entirely, no longer '
                               'converted to energy only.',
                       'tip': 'Projects failing CVC will be withdrawn from the queue entirely, no longer '
                              'converted to energy only.',
                       'timestamp': 233,
                       'timestamp_seconds': 233,
                       'timestamp_label': '[00:03:53]',
                       'url': 'https://www.youtube.com/watch?v=VdwOf6TKl6U&t=233s',
                       'markdown': '[00:03:53](https://www.youtube.com/watch?v=VdwOf6TKl6U&t=233s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QxDqhnba2Jg',
                       'title': 'Interconnection Queue Explained: The $3.5 Billion Waiting List',
                       'channel': 'Andy Knows It',
                       'author': 'Andy Knows It',
                       'text': '78% of that capacity eventually withdrew.',
                       'tip': '78% of that capacity eventually withdrew.',
                       'timestamp': 252,
                       'timestamp_seconds': 252,
                       'timestamp_label': '[00:04:12]',
                       'url': 'https://www.youtube.com/watch?v=QxDqhnba2Jg&t=252s',
                       'markdown': '[00:04:12](https://www.youtube.com/watch?v=QxDqhnba2Jg&t=252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ObxvY1JRruo',
                       'title': "Why New Power Projects Can't Connect to the Grid",
                       'channel': 'GridState',
                       'author': 'GridState',
                       'text': 'A single project withdrawal can force studies to be rerun.',
                       'tip': 'A single project withdrawal can force studies to be rerun.',
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=ObxvY1JRruo&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=ObxvY1JRruo&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M62wgLYBKBw',
                       'title': 'An Empirical Analysis of the Interconnection Queue - January 2024',
                       'channel': 'Environmental Defense Fund',
                       'author': 'Environmental Defense Fund',
                       'text': 'We see that costs are very predictive of withdrawal.',
                       'tip': 'We see that costs are very predictive of withdrawal.',
                       'timestamp': 1999,
                       'timestamp_seconds': 1999,
                       'timestamp_label': '[00:33:19]',
                       'url': 'https://www.youtube.com/watch?v=M62wgLYBKBw&t=1999s',
                       'markdown': '[00:33:19](https://www.youtube.com/watch?v=M62wgLYBKBw&t=1999s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v2cs7ZXTQH0',
                       'title': "Why the Grid Queue Isn't a Construction Schedule",
                       'channel': 'Blueprint States',
                       'author': 'Blueprint States',
                       'text': 'The queue is not a construction schedule.',
                       'tip': 'The queue is not a construction schedule.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=v2cs7ZXTQH0&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=v2cs7ZXTQH0&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
