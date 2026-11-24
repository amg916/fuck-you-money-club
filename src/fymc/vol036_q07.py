from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'multi-tenant-gpu-sharing-kubernetes',
 'question_prompt': 'How do I slice and share GPUs safely across multiple tenants on Kubernetes so '
                    "expensive capacity isn't idle?",
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Multi-Tenant GPU Sharing on Kubernetes',
 'subtitle': 'NVIDIA GPU Operator deployment, time-slicing replicas, MIG spatial partitioning and '
             'MIG-backed vGPU, MPS and Ray sharing, memory-safe dynamic time-slicing, vCluster, Open '
             'WebUI, OpenShift AI with KAI, Run:ai team sharing, HAMi vendor-neutral observability, DRA '
             'sharing-strategy benchmarks, and transparent GPU pod checkpointing',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators sharing GPUs on Kubernetes converge on one stack: the NVIDIA GPU operator '
                      'for drivers, device plugin and DCGM, then a sharing layer chosen by workload. Time '
                      'slicing advertises phantom replicas (Rafay flips an A10 between 2, 6 and 10 via a '
                      'node label; vCluster runs 4 replicas on an RTX 5070 Ti) but gives no memory '
                      'isolation, and Kubex watched a leaky classifier OOM-kill a neighbor LLM on a 24 GB '
                      'L4. MIG carves an A100 into up to seven 1g.5gb slices with fault isolation, at the '
                      'cost of static sizing. MPS, benchmarked by Klues and Chen, roughly doubles '
                      'light-load utilization and, capped at 10% for low-priority work, holds '
                      'near-dedicated performance. The split is throughput versus latency: Emmanuel Corels '
                      'measured A100 throughput rising from 0.76 to 1.0 requests/s under MIG while time '
                      'sharing kept mean latency lower.',
 'key_metrics': [{'label': 'Time-Slice Replica Resize Speed',
                  'metric': 'Time-Slice Replica Resize Speed',
                  'value': '10 replicas reduced to 6 in a few seconds after a node label edit',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Editing the nvidia.com label on an A10 node to time-slice profile six '
                             'triggered the NVIDIA GPU operator to reconcile the advertised GPU count',
                  'source': 'Rafay Systems ([n-O8p7y9Z5A @ 00:02:13])'},
                 {'label': 'HAMi-core Memory Cap Conversion',
                  'metric': 'HAMi-core Memory Cap Conversion',
                  'value': '0.35 GPU fraction converted to an 8,061 MB CUDA_DEVICE_MEMORY_LIMIT',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'HAMi-core intercepts CUDA calls via LD_PRELOAD so that only the leaky '
                             'classifier OOMs instead of the neighboring LLM',
                  'source': 'CNCF ([Vw7DTM1SV60 @ 00:14:00])'},
                 {'label': 'MIG Throughput at 50 Users on A100',
                  'metric': 'MIG Throughput at 50 Users on A100',
                  'value': '0.76 to 1.0 requests/s per GPU',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Same jobs run shared and then on separate MIG instances while ramping '
                             'concurrency; mean speech latency was still lower with time sharing',
                  'source': 'Emmanuel Corels Academy ([sRtvITK_o8I @ 00:03:35])'},
                 {'label': 'Quota Plus MIG Utilization Gain',
                  'metric': 'Quota Plus MIG Utilization Gain',
                  'value': 'Overall GPU utilization roughly doubles',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'After one month of Run:ai quotas, over-quota borrowing, MIG on inference '
                             'nodes and notebook coaching across three teams',
                  'source': 'Core Concept Learning ([56JbSXiXhhE @ 00:01:58])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner who actually ships shared GPUs starts from the same '
                              'foundation: the NVIDIA GPU operator. Techi Nik frames its job bluntly — it '
                              'detects GPU nodes, installs the NVIDIA drivers, manages GPU resources, and '
                              'skips any node without a card, so mixed clusters stay clean [f-FKoMHqRoI @ '
                              '00:00:35]. Saiyam of vCluster lists the full payload the operator drops '
                              'onto each GPU node: CUDA drivers, the container runtime, the device plugin, '
                              'metrics, and GPU feature discovery [sXpJ4vSc-cM @ 00:31:46]. That discovery '
                              "layer is what surfaces sharing to the Kubernetes scheduler. On Rafay's MKS "
                              'cluster, the operator stamps nvidia.com labels onto the GPU node reporting '
                              'GPU present true, an NVIDIA A10, a physical count of 1, and a time-slicing '
                              'strategy with 10 replicas, so a single card shows up to the scheduler as '
                              'ten [n-O8p7y9Z5A @ 00:00:44]. Jitesh Powankar calls enablement '
                              'straightforward: install the operator, configure node policies, and once '
                              'configured Kubernetes automatically discovers the new slices and reports '
                              'them like CPU or memory [Ul1dZowvKvE @ 00:03:58]. The operator consensus is '
                              'that nobody hand-rolls drivers and device plugins per node; the operator '
                              'owns that layer, and every sharing strategy — time slicing, MIG, or '
                              'fractional scheduling — is expressed as a label, a config, or an annotation '
                              'that the operator and scheduler reconcile.',
                              'The business case is idle silicon. Jitesh Powankar puts numbers on it: a '
                              'pod that requests a whole card may use only 20 to 30 percent, leaving 70 '
                              'percent idle while other pods queue — like booking a whole 50-seat bus for '
                              'one passenger [Ul1dZowvKvE @ 00:00:34]. The Code Architect drills into the '
                              'hardware reason: a light task occupies about 10 percent of the streaming '
                              'multiprocessors and the other 90 percent sit idle, because separate CUDA '
                              'contexts cannot run concurrently, and an H100 is far more than a '
                              '256M-parameter model needs [TwICQ_zP8Ys @ 00:02:40]. Saiyam states the '
                              'default outcome without a sharing layer: one pod takes the entire GPU, and '
                              'no one else can use it until it releases it [sXpJ4vSc-cM @ 00:34:26]. The '
                              'DevOps & AI Toolkit host hit that wall live on GKE: after llama 2 grabbed '
                              'the single GPU with a limit of nvidia.com/gpu equal to 1, the second model '
                              'sat Pending with no available GPUs, and buying another node only makes '
                              'sense when the first is at full capacity — otherwise it is a waste of money '
                              '[zuRKdveFuZ4 @ 00:08:47]. The shared conclusion: the default '
                              'one-pod-one-card model burns budget, and the arbitrage is packing multiple '
                              'tenants onto hardware you already pay for.',
                              'There is also broad agreement that no single mechanism wins; the mechanism '
                              'has to match the workload. Kevin Klues frames it as space versus time '
                              'partitioning, a fundamental inherent trade-off: MIG delivers full fault '
                              'isolation and memory-bandwidth QoS but fixed partition sizes, while MPS '
                              'offers flexible sizes with limited isolation that does not suit '
                              'multi-tenancy [nOgxv_R13Dg @ 00:05:00]. Emmanuel Corels Academy describes '
                              "the same split from the tenant's seat: time sharing lends idle capacity to "
                              'other jobs but jobs compete when both are busy, whereas MIG gives isolated '
                              'slices with no borrowing, so reserved capacity can sit idle [sRtvITK_o8I @ '
                              '00:00:52]. The Code Architect compresses it into a rule: time slicing for '
                              'bursty heterogeneous workloads, MPS for trusted and predictable ones, MIG '
                              'for absolute isolation [TwICQ_zP8Ys @ 00:08:03]. Core Concept Learning '
                              'shows what that looks like across three teams on Run:ai: inference GPUs '
                              'split into up to seven MIG instances, notebooks on Run:ai fractional GPUs, '
                              'and large training kept on full GPUs, with the exam-grade advice to match '
                              "the mechanism to the workload and each team's guarantee [56JbSXiXhhE @ "
                              '00:01:37]. Hardware gates the menu: The Code Architect notes MIG requires '
                              'Ampere or newer, and Emmanuel Corels Academy flags the L4 as lacking MIG '
                              'entirely.'],
               'table': {'caption': 'Where the practitioners line up on GPU sharing fundamentals',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reported',
                                     'Why It Matters for Operators',
                                     'Expert Source'],
                         'rows': [['GPU operator is the mandatory base layer for sharing',
                                   'Detects GPU nodes, installs NVIDIA drivers, manages GPU resources, and '
                                   'skips non-GPU nodes',
                                   'Every sharing strategy is reconciled by the operator rather than '
                                   'configured by hand per node',
                                   'Techi Nik ([f-FKoMHqRoI @ 00:00:35])'],
                                  ['Whole-card requests waste most of the purchased GPU',
                                   'A pod requesting a full card may use only 20-30 percent, leaving 70 '
                                   'percent idle',
                                   'Idle capacity is exactly the margin that a sharing layer recovers for '
                                   'other tenants',
                                   'Jitesh Powankar ([Ul1dZowvKvE @ 00:00:34])'],
                                  ['Light tasks strand most of the streaming multiprocessors',
                                   'A light task occupies about 10 percent of SMs while the other 90 '
                                   'percent sit idle',
                                   'Separate CUDA contexts cannot run concurrently without a deliberate '
                                   'sharing mechanism in place',
                                   'The Code Architect ([TwICQ_zP8Ys @ 00:02:40])'],
                                  ['Space versus time partitioning is an inherent trade-off',
                                   'MIG gives fault isolation and memory-bandwidth QoS with fixed sizes; '
                                   'MPS is flexible but weakly isolated',
                                   'Choose isolation or flexibility deliberately for each tenant and each '
                                   'workload class',
                                   'CNCF ([nOgxv_R13Dg @ 00:05:00])'],
                                  ['Time slicing provides zero memory isolation between tenants',
                                   'Context-switch overhead and jitter, with absolutely no memory '
                                   'isolation between the processes',
                                   'Untrusted or leaky tenants sharing time slices can crash their '
                                   'neighbors with OOM errors',
                                   'The Code Architect ([TwICQ_zP8Ys @ 00:03:47])'],
                                  ['MIG slices behave as hard walls with guaranteed QoS',
                                   'Time slicing works like a revolving door while MIG builds hard '
                                   'physical walls',
                                   'Use MIG where tenants need guaranteed capacity rather than '
                                   'opportunistic borrowing of idle cycles',
                                   'Jitesh Powankar ([Ul1dZowvKvE @ 00:03:05])'],
                                  ['Quotas, borrowing and MIG together lift cluster utilization',
                                   'Guaranteed project quotas, over-quota borrowing and MIG roughly '
                                   'doubled overall GPU utilization',
                                   'Fair-share policy, not slicing alone, is what keeps idle cards busy '
                                   'across contested teams',
                                   'Core Concept Learning ([56JbSXiXhhE @ 00:01:58])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Time slicing is a config-and-label game. Rafay's cluster runs a GPU "
                              'blueprint (V2) mapped to an NVIDIA GPU operator add-on carrying time-slice '
                              "configs for 2, 6 and 10 replicas; the engineer edits the node's nvidia.com "
                              'label to profile six, saves it, and the operator reconciles 10 replicas '
                              'down to 6 in a few seconds, then flips back to 10 when more applications '
                              'need to land [n-O8p7y9Z5A @ 00:02:13]. The vCluster step-by-step runs the '
                              'host side with GPU operator 25.3.0 and 4 replicas: create the time-slicing '
                              'config, patch it, then describe the node to confirm 1 GPU advertising 4 '
                              'replicas; inside each tenant vCluster with nodes enabled, reinstall the '
                              'operator with the toolkit and driver disabled, reapply and re-patch, and '
                              'expect a node refresh before 4 replicas appear [KzJvhbdgvl8 @ 00:01:27]. On '
                              'GKE, Saiyam simply sets time-sharing with max shared clients per GPU at '
                              'five on a single Tesla T4 and notes GKE automatically handles the operator '
                              'install [sXpJ4vSc-cM @ 00:44:18]. Under the hood, Kevin Klues explains the '
                              'device-plugin model: nvidia.com/gpu, GFD labels, a per-node replicas config '
                              'such as 3, and a .shared suffix on the advertised resource [nOgxv_R13Dg @ '
                              '00:09:27]. Skip the replicas, the vCluster demo warns, and pods fail to '
                              'schedule.',
                              "MIG is spatial and declarative. Rafay's upstream cluster shows a single "
                              'A100 labeled MIG capable true; the blueprint layers an add-on setting the '
                              'MIG single strategy, and because every partition is the same size the '
                              'operator slices to the maximum the card supports — seven GPUs reported as '
                              'GPU 0 through 6 [YoZoDn_Fvq0 @ 00:01:58]. A five-replica test app scheduled '
                              'against all-1g.5gb nodes comes up with identical GPU UUIDs but distinct MIG '
                              'UUIDs, which is the verification check. The DevOps & AI Toolkit host '
                              'recreated a GKE node pool with partition 1g.5gb, which means one compute '
                              'unit — 1/7 of the streaming multiprocessors — and 5 GB of memory, letting '
                              'up to seven pods share one GPU so the stuck second model finally ran, while '
                              'warning that sizing is dark magic best settled in the documentation, not by '
                              'intuition [zuRKdveFuZ4 @ 00:10:19]. SUSE pushes MIG into VMs on Harvester '
                              '170: a MIG configurations CRD is auto-created by querying the driver, three '
                              'profiles (1G.5GB, 2G.10GB, 3G.20GB) are defined, and each vGPU partition '
                              'attaches to a VM [4q3LHacRheg @ 00:00:48]. Emmanuel Corels Academy lists '
                              'the raw commands, nvidia-smi -l and nvidia-smi mig -l gip, and warns '
                              'workloads need both GPU and compute instances, with some models requiring a '
                              'reset [sRtvITK_o8I @ 00:01:38].',
                              'Fractional sharing with real memory enforcement is where the numbers get '
                              "precise. Saiyam's KAI pattern is to annotate gpu-fraction 0.5 while keeping "
                              'the resource limit at 1 [sXpJ4vSc-cM @ 00:38:38]. Julien Semaan of Kubex '
                              'runs three workloads with gpu-fraction annotations of 0.35, 0.20 and 0.35 '
                              'plus a reservation pod, but stresses KAI controls placement only; the fix '
                              'is HAMi-core, which intercepts CUDA calls via LD_PRELOAD and converts a '
                              '0.35 fraction into an 8,061 MB CUDA_DEVICE_MEMORY_LIMIT, after which only '
                              'the leaky classifier OOMs instead of the LLM beside it [Vw7DTM1SV60 @ '
                              '00:14:00]. The Code Architect applies the same discipline to Ray: a 0.25 '
                              "GPU request only sets CUDA_VISIBLE_DEVICES, so vLLM's GPU memory "
                              'utilization must be tuned to match the Ray placement fraction [TwICQ_zP8Ys '
                              "@ 00:07:14]. Yuan Chen's benchmarks put MPS limits in hard figures: under "
                              'heavy inference load, capping a low-priority job at 10 percent gives the '
                              'high-priority job near-dedicated performance, and on GPU burn, where one '
                              'job consumes about 23 to 24 GB and time slicing let job 1 take roughly 10 '
                              "times job 2's memory, MPS with 50 percent limits fixed the imbalance, while "
                              'the MPS daemon itself costs about 20 MB [nOgxv_R13Dg @ 00:20:02].'],
               'table': {'caption': 'Exact commands, settings and numbers practitioners used to share GPUs',
                         'headers': ['Mechanism or Tool',
                                     'Exact Command, Setting or Number',
                                     'Operator Use',
                                     'Expert Source'],
                         'rows': [['GPU operator Helm install with custom values file',
                                   'helm install gpu-operator nvidia/gpu-operator -n gpu-operator '
                                   '--create-namespace --wait -f values.yml',
                                   'Base install setting the NVIDIA runtime as default with runtime class '
                                   'nvidia',
                                   'Techi Nik ([f-FKoMHqRoI @ 00:03:20])'],
                                  ['Time-slice profile switch through a node label edit',
                                   'Edit the nvidia.com label to profile six and 10 replicas become 6 '
                                   'within seconds',
                                   'Resize tenant density on a live node without redeploying the operator',
                                   'Rafay Systems ([n-O8p7y9Z5A @ 00:02:13])'],
                                  ['MIG single strategy applied on an A100 node',
                                   'All-1g.5gb layout yields seven GPUs reported to Kubernetes as GPU 0 '
                                   'through 6',
                                   'Verify isolation by checking identical GPU UUIDs and distinct MIG '
                                   'UUIDs per pod',
                                   'Rafay Systems ([YoZoDn_Fvq0 @ 00:01:58])'],
                                  ['KAI fractional GPU annotation on tenant pods',
                                   'Annotate gpu-fraction 0.5 while keeping the nvidia.com/gpu limit set '
                                   'at 1',
                                   'Pack multiple tenant pods onto one card at the placement level',
                                   'vCluster ([sXpJ4vSc-cM @ 00:38:38])'],
                                  ['HAMi-core runtime memory cap through CUDA interception',
                                   'A 0.35 fraction converted to an 8,061 MB CUDA_DEVICE_MEMORY_LIMIT via '
                                   'LD_PRELOAD',
                                   'Confine an OOM to the leaky pod instead of crashing its neighbors',
                                   'CNCF ([Vw7DTM1SV60 @ 00:14:00])'],
                                  ['MPS resource limits for prioritized co-located jobs',
                                   'Low-priority job capped at 10 percent; 50 percent caps fix the GPU '
                                   'burn memory imbalance',
                                   'Benchmark limits empirically because no standard method for setting '
                                   'them exists yet',
                                   'CNCF ([nOgxv_R13Dg @ 00:20:02])'],
                                  ['MIG manager layout driven by a node label',
                                   'GPU Operator MIG manager applies a named configuration set through a '
                                   'node label',
                                   'Split inference GPUs into up to seven isolated instances with '
                                   'dedicated memory',
                                   'Core Concept Learning ([56JbSXiXhhE @ 00:01:37])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Settings that separate working shared clusters from OOM cascades',
                           'body': 'Four field-tested adjustments the practitioners applied once the basic '
                                   'operator install was running.',
                           'items': ["Match vLLM's GPU memory utilization to the Ray placement fraction, "
                                     'because a 0.25 GPU request on its own can still saturate 100 percent '
                                     'of the device and let PyTorch and vLLM each grab the whole VRAM [The '
                                     'Code Architect — TwICQ_zP8Ys @ 00:07:14].',
                                     'Do not trust nvidia-smi on time-sliced cards: on a 24 GB L4 with 5 '
                                     "replicas it showed 13 GB while the pod's real usage was 4 GB [CNCF — "
                                     'Vw7DTM1SV60 @ 00:04:56].',
                                     'Inside each tenant vCluster, reinstall the GPU operator with the '
                                     'toolkit and driver disabled, reapply and re-patch time slicing, and '
                                     'refresh the node if the 4 replicas do not show [vCluster — '
                                     'KzJvhbdgvl8 @ 00:02:09].',
                                     'Set NVIDIA_DRIVER_CAPABILITIES to compute and utility when the model '
                                     'does not use video, keep the nvidia.com/gpu limit explicit, and add '
                                     "a toleration keyed nvidia.com/gpu to clear the GPU node's NoSchedule "
                                     'taint [DevOps & AI Toolkit — zuRKdveFuZ4 @ 00:07:02].']},
               'sop_steps': [{'step': 1,
                              'title': 'Install and verify the GPU operator',
                              'action': 'Add the nvidia Helm repo, install gpu-operator with a values.yml '
                                        'setting the containerd template, socket path and nvidia runtime '
                                        'class, then run a test pod.',
                              'detail': 'Run helm repo add nvidia and helm repo update, install into the '
                                        'gpu-operator namespace with --create-namespace --wait, confirm '
                                        'the driver daemonset, device plugin, DCGM exporter and toolkit '
                                        'pods come up after a couple more minutes, then kubectl exec a GPU '
                                        'count 1 TensorFlow pod and run nvidia-smi [Techi Nik — '
                                        'f-FKoMHqRoI @ 00:04:27].'},
                             {'step': 2,
                              'title': 'Apply the sharing profile by label',
                              'action': 'Pick time-slice replicas or a MIG layout and drive it through the '
                                        'node label that the operator watches.',
                              'detail': "For time slicing, edit the node's nvidia.com label to a blueprint "
                                        'profile such as six or ten and let the operator reconcile the '
                                        "advertised GPU count in seconds; for MIG, let the GPU Operator's "
                                        'MIG manager apply a named configuration set through a node label '
                                        '[Rafay Systems — n-O8p7y9Z5A @ 00:01:29].'},
                             {'step': 3,
                              'title': 'Enforce per-tenant memory at runtime',
                              'action': 'Pair fractional placement with a runtime memory cap so one tenant '
                                        'cannot OOM the card.',
                              'detail': 'Annotate pods with KAI gpu-fraction values such as 0.35 and 0.20 '
                                        'for placement, then inject HAMi-core so the 0.35 fraction becomes '
                                        'an 8,061 MB CUDA_DEVICE_MEMORY_LIMIT via LD_PRELOAD and only the '
                                        'misbehaving pod OOMs [CNCF — Vw7DTM1SV60 @ 00:14:00].'},
                             {'step': 4,
                              'title': 'Benchmark shared versus isolated and rebalance',
                              'action': 'Run identical jobs shared and on separate instances, ramp '
                                        'concurrency, and adjust layouts on a fixed cadence.',
                              'detail': 'Give each job a distinct CUDA_VISIBLE_DEVICES, measure latency '
                                        'and throughput while ramping users, and remember nvidia-smi does '
                                        'not attribute utilization per instance, which is how an A100 at '
                                        '50 users showed 0.76 versus 1.0 requests/s per GPU [Emmanuel '
                                        'Corels Academy — sRtvITK_o8I @ 00:02:25].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is the classic one, time slicing versus MIG, and the '
                              'practitioners do not land in the same place. Emmanuel Corels Academy ran '
                              'the same jobs shared and then on separate MIG instances on an A100, with a '
                              'distinct CUDA_VISIBLE_DEVICES per job, and at 50 users throughput moved '
                              'from 0.76 to 1.0 requests per second per GPU, yet mean speech latency came '
                              'in lower with time sharing [sRtvITK_o8I @ 00:03:35]. So the answer depends '
                              'on whether a tenant is buying throughput or responsiveness. Julien Semaan '
                              'of Kubex concedes in Q&A that MIG is usually faster but static, and his '
                              'entire build targets making time slicing memory-safe rather than abandoning '
                              'it [Vw7DTM1SV60 @ 00:20:40]. Kevin Klues frames it as a fundamental '
                              'inherent trade-off: MIG buys full fault isolation and memory-bandwidth QoS '
                              'but locks you into fixed partition sizes, while time partitioning gives '
                              'flexibility that you pay for in contention [nOgxv_R13Dg @ 00:05:00]. The '
                              'Code Architect settles the fight by workload class instead of ideology: '
                              'time slicing for bursty heterogeneous workloads, MPS for trusted and '
                              'predictable ones, and MIG only when you need absolute isolation '
                              '[TwICQ_zP8Ys @ 00:08:03]. The operator read is that no single sharing mode '
                              'wins every tenant mix, so each tenant gets placed and priced by the load '
                              'profile it actually runs, not by whichever mode the platform team installed '
                              'first.',
                              'Fractional GPUs split the field a second time, over whether a fraction is a '
                              'promise or an enforced wall. Saiyam and Mike Peterson at vCluster demo the '
                              'KAI approach: annotate the pod with gpu-fraction 0.5 while keeping the '
                              'limit at 1 [sXpJ4vSc-cM @ 00:38:38]. Semaan warns that this controls '
                              'placement only; KAI does not enforce the fraction at runtime, so noisy '
                              'neighbors remain possible, and his fix layers HAMi-core underneath, '
                              'intercepting CUDA calls through LD_PRELOAD so a 0.35 fraction becomes an '
                              '8,061 MB CUDA_DEVICE_MEMORY_LIMIT [Vw7DTM1SV60 @ 00:10:30]. The Code '
                              'Architect hits the same wall from the Ray side: a 0.25 GPU request can '
                              'still saturate the whole device because Ray only sets CUDA_VISIBLE_DEVICES, '
                              "so the fix lives in the application, tuning vLLM's GPU memory utilization "
                              "to match the Ray placement fraction [TwICQ_zP8Ys @ 00:06:22]. Yuan Chen's "
                              'benchmarks push a third playbook, MPS with explicit limits: capping a '
                              'low-priority job at 10% gave the other job near-dedicated performance under '
                              'heavy load, where plain time slicing pinned the GPU at 100% and degraded '
                              "badly [nOgxv_R13Dg @ 00:20:45]. Semaan's own talk counters that MPS adds a "
                              'daemon that becomes another point of failure. The real choice is where '
                              "enforcement lives: in the CUDA interception layer, in each application's "
                              'memory config, or in an extra daemon on every GPU node.',
                              "The tenancy wrapper is the third fault line. vCluster's Saiyam and Mike "
                              "Peterson argue namespaces provide weak isolation, you can't do CRDs, and "
                              '3,000 secrets in one namespace load etcd for everyone, so each tenant gets '
                              'its own virtual cluster, with the host either syncing node information in '
                              'or exposing only a runtime class [sXpJ4vSc-cM @ 00:41:50]. Core Concept '
                              "Learning's Run:ai playbook stays in one shared cluster and runs it like a "
                              'quota market: departments and projects hold guaranteed GPU quotas, research '
                              "borrows analytics' idle GPUs overnight, and preemption claws the quota back "
                              "when the owner returns [56JbSXiXhhE @ 00:00:56]. Luca Berton's OpenShift AI "
                              'build for a French avionics customer is governance-heavy: tenants arrive '
                              'through PR-based templates covering RBAC, network policies and quotas, '
                              'while KAI caps, priority classes and preemption keep interactive work above '
                              'training [nABVTFBmV2M @ 00:13:02]. SUSE moves the boundary down to the '
                              'virtual machine, carving MIG-backed vGPUs in Harvester into 1G.5GB, 2G.10GB '
                              'and 3G.20GB profiles and attaching each partition to its own VM, with both '
                              'VMs seeing the GPU [4q3LHacRheg @ 00:00:48]. Each camp trades operational '
                              'weight for a harder boundary: borrowing is light and fast, PR-gated '
                              'templates leave an audit trail, and VM-attached partitions give the hardest '
                              'line of the four. The operator picks the wrapper first, then picks the '
                              'slicing mode that runs underneath it.'],
               'table': {'caption': 'Competing GPU-sharing playbooks, side by side as the practitioners '
                                    'ran them',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Time slicing versus MIG for multi-user inference serving',
                                   'Time sharing delivered lower mean speech latency at 50 users on an '
                                   'A100',
                                   'Separate MIG instances moved throughput from 0.76 to 1.0 requests per '
                                   'second per GPU',
                                   'Emmanuel Corels Academy ([sRtvITK_o8I @ 00:03:35])'],
                                  ['MIG raw speed versus flexible time-sliced fractions in production',
                                   'MIG is usually faster but its partition sizes stay static and rigid',
                                   'Memory-safe time slicing with HAMi-core keeps flexible fractions on a '
                                   '24 GB L4',
                                   'CNCF ([Vw7DTM1SV60 @ 00:20:40])'],
                                  ['Where a fractional GPU request is actually enforced at runtime',
                                   'KAI gpu-fraction annotation with the limit kept at 1 controls '
                                   'placement only',
                                   'HAMi-core LD_PRELOAD turns a 0.35 fraction into an 8,061 MB '
                                   'CUDA_DEVICE_MEMORY_LIMIT',
                                   'CNCF ([Vw7DTM1SV60 @ 00:10:30])'],
                                  ['Co-locating jobs on one GPU under heavy inference load',
                                   'Plain time slicing pins the GPU at 100 percent and degrades badly',
                                   'MPS capping the low-priority job at 10 percent gives near-dedicated '
                                   'performance',
                                   'CNCF ([nOgxv_R13Dg @ 00:20:45])'],
                                  ['Whether the MPS daemon is worth running on shared nodes',
                                   'Benchmark team measured the MPS daemon at about 20 MB with a slower '
                                   'start',
                                   'Kubex treats the MPS daemon as another point of failure and avoids it',
                                   'CNCF ([nOgxv_R13Dg @ 00:19:44]); CNCF ([Vw7DTM1SV60 @ 00:08:06])'],
                                  ['Which tenancy wrapper sits around the shared GPU fleet',
                                   'vCluster virtual clusters because namespaces give weak isolation and '
                                   'no CRDs',
                                   'Run:ai departments with guaranteed quotas and over-quota borrowing '
                                   'reclaimed by preemption',
                                   'vCluster ([sXpJ4vSc-cM @ 00:41:50]); Core Concept Learning '
                                   '([56JbSXiXhhE @ 00:00:56])'],
                                  ['How many time-slice replicas to advertise per physical GPU',
                                   'More slices suit light chat usage spread across many tenant users',
                                   'Fewer, faster slices suit heavy code-completion use, with usage '
                                   'monitored continuously',
                                   'vCluster ([sXpJ4vSc-cM @ 00:56:01])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Memory is where shared GPUs die first. Julien Semaan's Kubex demo put 5 "
                              'time-slice replicas on a 24 GB L4, and nvidia-smi showed 13 GB for a pod '
                              'whose real usage was 4 GB, so the standard tool misreported who was '
                              'actually eating the card [Vw7DTM1SV60 @ 00:04:56]. Then a leaky classifier '
                              'on the same GPU pushed LLM A into OOM, killing the well-behaved tenant '
                              'instead of the offender. The Code Architect traces the same failure to '
                              'layer misalignment: when hardware, driver and orchestration layers '
                              "disagree, the result is OOM errors and node crashes, and Ray's fractional "
                              'request only sets CUDA_VISIBLE_DEVICES, letting PyTorch and vLLM each grab '
                              "the whole VRAM [TwICQ_zP8Ys @ 00:01:14]. Yuan Chen's GPU-burn benchmark "
                              'quantified the imbalance: under plain time slicing, job 1 took about ten '
                              "times job 2's memory, and only MPS with 50% limits evened it out "
                              "[nOgxv_R13Dg @ 00:23:49]. Dynamia.ai's HAMi talk adds the utilization cost: "
                              'without memory isolation, OOM crashes tanked utilization, and reserved '
                              'memory, 5 GB in their example, is not the same thing as consumed memory, so '
                              'unused reservations and noisy neighbors both have to be watched '
                              '[zrGFmLHI7hg @ 00:09:22]. The economics check is blunt: an unenforced '
                              'fraction is an outage waiting for the noisiest neighbor on the card, and it '
                              'takes down the paying tenant first.',
                              'The second trap is capacity that exists on paper but never schedules. '
                              'Jitesh Powankar frames the baseline waste: a pod requesting a whole card '
                              'may use only 20 to 30 percent, leaving 70 percent idle while other pods '
                              'queue, like booking a whole 50-seat bus for one passenger [Ul1dZowvKvE @ '
                              '00:00:34]. DevOps & AI Toolkit hit it live on GKE: after llama 2 took the '
                              'single GPU, the second model sat Pending with no available GPUs, and adding '
                              'another node before the first was at full capacity would have been a waste '
                              'of money; recreating the pool with 1g.5gb partitions let up to seven pods '
                              "share the card [zuRKdveFuZ4 @ 00:08:47]. vCluster's host-cluster "
                              'walkthrough showed the inverse problem: without time-slicing replicas '
                              'advertised, pods simply fail to schedule, so the replica count has to be '
                              'confirmed on the node before tenants arrive [KzJvhbdgvl8 @ 00:04:26]. Gang '
                              'scheduling is the costliest version: with 8 pods and 4 GPUs, the default '
                              'scheduler places 4 and leaves 4 pending, so the job never starts while 4 '
                              'GPUs are still consumed [sXpJ4vSc-cM @ 00:37:13]. DevOps & AI Toolkit also '
                              'flags the quieter blocker: GPU nodes carry a NoSchedule taint, so a pod '
                              'without the nvidia.com/gpu toleration never lands on the hardware you are '
                              'paying for.',
                              'The third failure class is drift, and it hits the teams that are already '
                              'winning. Saiyam warns that deleting the GPU operator leaves drivers on the '
                              'node, and a reinstall then produces a version mismatch that just breaks '
                              "[sXpJ4vSc-cM @ 00:01:22]. Luca Berton's air-gapped H200 build lost time to "
                              'a ConnectX versus Intel RDMA kernel collision that blocked SR-IOV until the '
                              "Intel driver was blacklisted, and the team's upgrade path now runs through "
                              'a compatibility matrix in Git, a 48-hour canary pool and Argo CD rollback '
                              '[nABVTFBmV2M @ 00:11:34]. Dynamia.ai reports that NVIDIA GPU operator '
                              'updates very often change or break metrics, so metric pipelines have to be '
                              're-verified after every operator bump [zrGFmLHI7hg @ 00:10:03]. Core '
                              'Concept Learning names the policy traps directly: static per-team GPUs, a '
                              'whole GPU for every notebook, changing the MIG layout while work is '
                              'running, and preemption without checkpointing [56JbSXiXhhE @ 00:02:19]. The '
                              'payoff for avoiding them is real, with overall GPU utilization roughly '
                              'doubling after a month of quota rebalancing, a MIG relayout on two drained '
                              "nodes and coaching for idle-notebook users. Christian Kniep's checkpoint "
                              'operator closes the preemption gap by restoring a PyTorch job at epoch 4 '
                              'after the pod is deleted, for jobs carrying the checkpoint labels.'],
               'table': {'caption': 'Firsthand failures on shared GPUs and the check each practitioner '
                                    'applied',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics or Operational Check',
                                     'Expert Source'],
                         'rows': [['Phantom memory readings under time slicing on an L4',
                                   "nvidia-smi showed 13 GB while the pod's real usage was only 4 GB",
                                   'Never size tenant fractions off nvidia-smi totals on time-sliced cards',
                                   'CNCF ([Vw7DTM1SV60 @ 00:04:56])'],
                                  ['Leaky neighbor pushing a healthy model into OOM',
                                   'A leaky classifier on the shared L4 caused LLM A to hit OOM',
                                   'Enforce per-pod CUDA memory limits so only the offending classifier '
                                   'dies',
                                   'CNCF ([Vw7DTM1SV60 @ 00:05:31])'],
                                  ['Fake fractional request on a Ray-managed GPU device',
                                   'A 0.25 GPU request saturated the device and cascaded into OOM',
                                   'Match vLLM GPU memory utilization to the Ray placement fraction every '
                                   'time',
                                   'The Code Architect ([TwICQ_zP8Ys @ 00:05:31])'],
                                  ['No time-slicing replicas configured on the GPU node',
                                   'Pods failed to schedule until the replica count was advertised by the '
                                   'node',
                                   'Describe the node and confirm replicas before onboarding any tenant '
                                   'workload',
                                   'vCluster ([KzJvhbdgvl8 @ 00:04:26])'],
                                  ['Partial gang placement on a default Kubernetes scheduler',
                                   'An 8-pod job on 4 GPUs placed 4 pods and left 4 pending',
                                   'Evaluate Kueue, Volcano or KAI so idle reserved GPUs stop burning '
                                   'money',
                                   'vCluster ([sXpJ4vSc-cM @ 00:37:13])'],
                                  ['GPU operator reinstall leaving stale drivers behind on nodes',
                                   'Deleting the operator left drivers, and reinstalling caused a breaking '
                                   'version mismatch',
                                   'Keep a compatibility matrix in Git and run a 48-hour canary pool',
                                   'vCluster ([sXpJ4vSc-cM @ 00:01:22]); CNCF ([nABVTFBmV2M @ 00:14:48])'],
                                  ['Blind per-instance utilization on partitioned MIG GPUs',
                                   'NVIDIA SMI does not attribute utilization per MIG instance during '
                                   'tests',
                                   'Measure latency and throughput per job while ramping concurrency step '
                                   'by step',
                                   'Emmanuel Corels Academy ([sRtvITK_o8I @ 00:03:12])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do not open a shared GPU to a second tenant until these four checks '
                                    'pass',
                           'body': 'Every item below comes from a practitioner who lost a model, a job or '
                                   'a dashboard to it. Clear all four before advertising slices, fractions '
                                   'or borrowing to another team.',
                           'items': ['Memory is enforced at runtime, not only annotated: KAI placement '
                                     'alone leaves noisy neighbors possible, so wrap fractions in a '
                                     'CUDA-level memory limit [CNCF — Vw7DTM1SV60 @ 00:10:30].',
                                     'MIG layouts are only changed on drained nodes; changing the layout '
                                     'while work is running is a named trap [Core Concept Learning — '
                                     '56JbSXiXhhE @ 00:02:19].',
                                     'Preemptible jobs checkpoint to a PVC first, so a reclaimed pod '
                                     'resumes at the next epoch instead of restarting from zero [Christian '
                                     'Kniep — K9yY6_2255Y @ 00:02:24].',
                                     'GPU operator upgrades are canaried with metrics re-verified, because '
                                     'operator updates very often change or break metrics [CNCF — '
                                     'zrGFmLHI7hg @ 00:10:03].']}}],
 'pull_quote': '"When we do time slicing on Kubernetes, we\'re basically tricking the scheduler into '
               'thinking there are more GPUs available for scheduling than there are physically." Julien '
               'Semaan, Kubex, attributed to CNCF [Cloud Native Computing Foundation] (Vw7DTM1SV60 @ '
               '00:06:57).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Install the GPU operator with helm install gpu-operator nvidia/gpu-operator -n '
                      'gpu-operator --create-namespace --wait -f values.yml, with the Nvidia runtime set '
                      'as default, then confirm the driver, device plugin, DCGM exporter and toolkit pods '
                      '[Techi Nik — f-FKoMHqRoI @ 00:03:20].',
                      'Drive time-slice replica counts from a node label backed by blueprint profiles for '
                      '2, 6 and 10 replicas, and confirm the advertised GPU count flips within seconds '
                      '[Rafay Systems — n-O8p7y9Z5A @ 00:02:13].',
                      'For MIG single strategy on an A100, deploy a test app and verify all pods share one '
                      'GPU UUID with distinct MIG UUIDs before onboarding tenants [Rafay Systems — '
                      'YoZoDn_Fvq0 @ 00:02:55].',
                      'Back every fractional request with HAMi-core so the fraction converts into a hard '
                      'CUDA_DEVICE_MEMORY_LIMIT and only the leaking workload OOMs [CNCF — Vw7DTM1SV60 @ '
                      '00:14:00].',
                      'Set guaranteed project quotas, allow over-quota borrowing of idle GPUs, and require '
                      'regular checkpointing so preempted work resumes cleanly [Core Concept Learning — '
                      '56JbSXiXhhE @ 00:00:56].',
                      'Track per-slice memory and compute in Prometheus and Grafana with alerts, then '
                      'rebalance slice counts as usage shifts between light and heavy tenants [Jitesh '
                      'Powankar — Ul1dZowvKvE @ 00:04:15].'],
 'statutory_citations': [{'title': 'CNCF [Cloud Native Computing Foundation] — Fixing GPU Time-Slicing on '
                                   'Kubernetes: Dynamic, Memory-Safe Sharing for AI... Julien Semaan, '
                                   'Kubex [00:10:30]',
                          'url': 'https://www.youtube.com/watch?v=Vw7DTM1SV60&t=630s',
                          'relevance': 'Primary practitioner testimony on why scheduler-level GPU '
                                       'fractions fail without runtime memory enforcement.'},
                         {'title': 'CNCF [Cloud Native Computing Foundation] — Which GPU Sharing Strategy '
                                   'Is Right for You? A Comprehensive Benchmark Study Us... K. Klues, Y. '
                                   'Chen [00:20:45]',
                          'url': 'https://www.youtube.com/watch?v=nOgxv_R13Dg&t=1245s',
                          'relevance': 'Primary practitioner testimony on benchmarked time slicing, MPS '
                                       'and MIG behavior under light and heavy load.'},
                         {'title': 'Core Concept Learning — NCP-AIO Scenario 03/5: Sharing GPUs Across '
                                   'Teams with Run:ai and MIG [00:02:19]',
                          'url': 'https://www.youtube.com/watch?v=56JbSXiXhhE&t=139s',
                          'relevance': 'Primary practitioner testimony on quota, borrowing, MIG layout and '
                                       'preemption traps across teams.'},
                         {'title': 'CNCF [Cloud Native Computing Foundation] — Lessons Learned '
                                   'Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA KAI '
                                   '(G/H2... Luca Berton [00:14:48]',
                          'url': 'https://www.youtube.com/watch?v=nABVTFBmV2M&t=888s',
                          'relevance': 'Primary practitioner testimony on driver drift, upgrade canaries '
                                       'and GitOps rollback for multi-tenant GPU fleets.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'n-O8p7y9Z5A',
                       'title': 'NVIDIA GPU Time Slicing: Create Multiple GPU Replicas on Kubernetes | '
                                'Rafay',
                       'channel': 'Rafay Systems',
                       'author': 'Rafay Systems',
                       'text': 'Saving the label triggers the Nvidia GPU operator to apply the change, and '
                               '10 becomes 6 in a few seconds.',
                       'tip': 'Saving the label triggers the Nvidia GPU operator to apply the change, and '
                              '10 becomes 6 in a few seconds.',
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=n-O8p7y9Z5A&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=n-O8p7y9Z5A&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f-FKoMHqRoI',
                       'title': 'How to deploy NVIDIA GPU Operator Deployment on Kubernetes',
                       'channel': 'Techi Nik',
                       'author': 'Techi Nik',
                       'text': 'Run helm install gpu-operator nvidia/gpu-operator in the gpu-operator '
                               'namespace with create-namespace, wait, and the values.yml file.',
                       'tip': 'Run helm install gpu-operator nvidia/gpu-operator in the gpu-operator '
                              'namespace with create-namespace, wait, and the values.yml file.',
                       'timestamp': 200,
                       'timestamp_seconds': 200,
                       'timestamp_label': '[00:03:20]',
                       'url': 'https://www.youtube.com/watch?v=f-FKoMHqRoI&t=200s',
                       'markdown': '[00:03:20](https://www.youtube.com/watch?v=f-FKoMHqRoI&t=200s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TwICQ_zP8Ys',
                       'title': 'Stop Wasting GPUs: How to Share Hardware with Ray, MPS, and Time-Slicing',
                       'channel': 'The Code Architect',
                       'author': 'The Code Architect',
                       'text': 'A fractional resource request in Ray is useless on its own.',
                       'tip': 'A fractional resource request in Ray is useless on its own.',
                       'timestamp': 382,
                       'timestamp_seconds': 382,
                       'timestamp_label': '[00:06:22]',
                       'url': 'https://www.youtube.com/watch?v=TwICQ_zP8Ys&t=382s',
                       'markdown': '[00:06:22](https://www.youtube.com/watch?v=TwICQ_zP8Ys&t=382s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4q3LHacRheg',
                       'title': 'SUSE Virtualization NVIDIA MIG vGPU Multi-Tenancy on Kubernetes',
                       'channel': 'SUSE',
                       'author': 'SUSE',
                       'text': 'Three MIG profiles are created, 1G.5GB, 2G.10GB and 3G.20GB, and each vGPU '
                               'partition is attached to a VM.',
                       'tip': 'Three MIG profiles are created, 1G.5GB, 2G.10GB and 3G.20GB, and each vGPU '
                              'partition is attached to a VM.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=4q3LHacRheg&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=4q3LHacRheg&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KzJvhbdgvl8',
                       'title': 'GPU Timeslicing + Open WebUI on Kubernetes with vCluster – Step‑by‑Step '
                                'Guide',
                       'channel': 'vCluster',
                       'author': 'vCluster',
                       'text': 'Without the time-slicing replicas in place, the pods fail to schedule.',
                       'tip': 'Without the time-slicing replicas in place, the pods fail to schedule.',
                       'timestamp': 266,
                       'timestamp_seconds': 266,
                       'timestamp_label': '[00:04:26]',
                       'url': 'https://www.youtube.com/watch?v=KzJvhbdgvl8&t=266s',
                       'markdown': '[00:04:26](https://www.youtube.com/watch?v=KzJvhbdgvl8&t=266s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sRtvITK_o8I',
                       'title': 'One GPU, Several AI Users: MIG vs Time-Slicing Explained',
                       'channel': 'Emmanuel Corels Academy',
                       'author': 'Emmanuel Corels Academy',
                       'text': "MIG separates assigned GPU resources, but doesn't control access to your "
                               'application, its data, or its network.',
                       'tip': "MIG separates assigned GPU resources, but doesn't control access to your "
                              'application, its data, or its network.',
                       'timestamp': 238,
                       'timestamp_seconds': 238,
                       'timestamp_label': '[00:03:58]',
                       'url': 'https://www.youtube.com/watch?v=sRtvITK_o8I&t=238s',
                       'markdown': '[00:03:58](https://www.youtube.com/watch?v=sRtvITK_o8I&t=238s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nABVTFBmV2M',
                       'title': 'Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with '
                                'NVIDIA KAI (G/H2... Luca Berton',
                       'channel': 'CNCF [Cloud Native Computing Foundation]',
                       'author': 'CNCF [Cloud Native Computing Foundation]',
                       'text': 'The hard part is sharing them safely, fairly, and efficiently across '
                               'teams.',
                       'tip': 'The hard part is sharing them safely, fairly, and efficiently across teams.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=nABVTFBmV2M&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=nABVTFBmV2M&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Vw7DTM1SV60',
                       'title': 'Fixing GPU Time-Slicing on Kubernetes: Dynamic, Memory-Safe Sharing for '
                                'AI... Julien Semaan, Kubex',
                       'channel': 'CNCF [Cloud Native Computing Foundation]',
                       'author': 'CNCF [Cloud Native Computing Foundation]',
                       'text': "Kai doesn't enforce it on runtime, so noisy neighbors remain possible.",
                       'tip': "Kai doesn't enforce it on runtime, so noisy neighbors remain possible.",
                       'timestamp': 630,
                       'timestamp_seconds': 630,
                       'timestamp_label': '[00:10:30]',
                       'url': 'https://www.youtube.com/watch?v=Vw7DTM1SV60&t=630s',
                       'markdown': '[00:10:30](https://www.youtube.com/watch?v=Vw7DTM1SV60&t=630s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sXpJ4vSc-cM',
                       'title': 'Multi-Tenancy Fundamentals: Why GPU Sharing is Harder in Kubernetes',
                       'channel': 'vCluster',
                       'author': 'vCluster',
                       'text': "Without that, you're just going to have one pod take the entire GPU, and "
                               'no one else can use it until it releases it.',
                       'tip': "Without that, you're just going to have one pod take the entire GPU, and no "
                              'one else can use it until it releases it.',
                       'timestamp': 2066,
                       'timestamp_seconds': 2066,
                       'timestamp_label': '[00:34:26]',
                       'url': 'https://www.youtube.com/watch?v=sXpJ4vSc-cM&t=2066s',
                       'markdown': '[00:34:26](https://www.youtube.com/watch?v=sXpJ4vSc-cM&t=2066s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YoZoDn_Fvq0',
                       'title': 'NVIDIA MIG: Spatial GPU Partitioning for Multi-Tenant Workloads | Rafay',
                       'channel': 'Rafay Systems',
                       'author': 'Rafay Systems',
                       'text': 'You look at the UUID for the GPU, all of them are identical, but the MIG '
                               'ID is different.',
                       'tip': 'You look at the UUID for the GPU, all of them are identical, but the MIG ID '
                              'is different.',
                       'timestamp': 175,
                       'timestamp_seconds': 175,
                       'timestamp_label': '[00:02:55]',
                       'url': 'https://www.youtube.com/watch?v=YoZoDn_Fvq0&t=175s',
                       'markdown': '[00:02:55](https://www.youtube.com/watch?v=YoZoDn_Fvq0&t=175s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ul1dZowvKvE',
                       'title': 'GPU Resource Slice Explained with Pizza Analogy | NVIDIA MIG & GPU '
                                'Slicing Made Easy',
                       'channel': 'Jitesh Powankar',
                       'author': 'Jitesh Powankar',
                       'text': "It's like booking a whole 50-seat bus for just one passenger.",
                       'tip': "It's like booking a whole 50-seat bus for just one passenger.",
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=Ul1dZowvKvE&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=Ul1dZowvKvE&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zrGFmLHI7hg',
                       'title': 'Vendor-Neutral GPU Observability for Kubernetes - Reza Jelveh, Dynamia.ai',
                       'channel': 'CNCF [Cloud Native Computing Foundation]',
                       'author': 'CNCF [Cloud Native Computing Foundation]',
                       'text': 'A thing that happens very often is that when Nvidia updates their GPU '
                               'operator the metrics change or like stuff breaks.',
                       'tip': 'A thing that happens very often is that when Nvidia updates their GPU '
                              'operator the metrics change or like stuff breaks.',
                       'timestamp': 603,
                       'timestamp_seconds': 603,
                       'timestamp_label': '[00:10:03]',
                       'url': 'https://www.youtube.com/watch?v=zrGFmLHI7hg&t=603s',
                       'markdown': '[00:10:03](https://www.youtube.com/watch?v=zrGFmLHI7hg&t=603s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nOgxv_R13Dg',
                       'title': 'Which GPU Sharing Strategy Is Right for You? A Comprehensive Benchmark '
                                'Study Us... K. Klues, Y. Chen',
                       'channel': 'CNCF [Cloud Native Computing Foundation]',
                       'author': 'CNCF [Cloud Native Computing Foundation]',
                       'text': 'We should consider use this MPS with the proper resource limits and can '
                               'provide much better resource isolation.',
                       'tip': 'We should consider use this MPS with the proper resource limits and can '
                              'provide much better resource isolation.',
                       'timestamp': 1511,
                       'timestamp_seconds': 1511,
                       'timestamp_label': '[00:25:11]',
                       'url': 'https://www.youtube.com/watch?v=nOgxv_R13Dg&t=1511s',
                       'markdown': '[00:25:11](https://www.youtube.com/watch?v=nOgxv_R13Dg&t=1511s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zuRKdveFuZ4',
                       'title': 'GPUs in Kubernetes for AI Workloads',
                       'channel': 'DevOps & AI Toolkit',
                       'author': 'DevOps & AI Toolkit',
                       'text': 'MIG partitioning is dark magic, so consult the documentation instead of '
                               'relying on intuition.',
                       'tip': 'MIG partitioning is dark magic, so consult the documentation instead of '
                              'relying on intuition.',
                       'timestamp': 661,
                       'timestamp_seconds': 661,
                       'timestamp_label': '[00:11:01]',
                       'url': 'https://www.youtube.com/watch?v=zuRKdveFuZ4&t=661s',
                       'markdown': '[00:11:01](https://www.youtube.com/watch?v=zuRKdveFuZ4&t=661s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K9yY6_2255Y',
                       'title': 'Checkpoint K8s pods transparently (plain CPU or GPU accelerated)',
                       'channel': 'Christian Kniep',
                       'author': 'Christian Kniep',
                       'text': 'The checkpoint is restored into the rescheduled pod and training resumes '
                               'from epoch 4.',
                       'tip': 'The checkpoint is restored into the rescheduled pod and training resumes '
                              'from epoch 4.',
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=K9yY6_2255Y&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=K9yY6_2255Y&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '56JbSXiXhhE',
                       'title': 'NCP-AIO Scenario 03/5: Sharing GPUs Across Teams with Run:ai and MIG',
                       'channel': 'Core Concept Learning',
                       'author': 'Core Concept Learning',
                       'text': 'Sharing policy is never finished.',
                       'tip': 'Sharing policy is never finished.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=56JbSXiXhhE&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=56JbSXiXhhE&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '56JbSXiXhhE',
                       'title': 'NCP-AIO Scenario 03/5: Sharing GPUs Across Teams with Run:ai and MIG',
                       'channel': 'Core Concept Learning',
                       'author': 'Core Concept Learning',
                       'text': "Using other teams' idle GPUs is over quota borrowing, reclaimed by "
                               'preemption.',
                       'tip': "Using other teams' idle GPUs is over quota borrowing, reclaimed by "
                              'preemption.',
                       'timestamp': 178,
                       'timestamp_seconds': 178,
                       'timestamp_label': '[00:02:58]',
                       'url': 'https://www.youtube.com/watch?v=56JbSXiXhhE&t=178s',
                       'markdown': '[00:02:58](https://www.youtube.com/watch?v=56JbSXiXhhE&t=178s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
