from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'inference-engines-max-tokens-per-gpu',
 'question_prompt': 'Which inference engine and settings squeeze the most tokens per GPU dollar out of the '
                    'hardware I have?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Inference Engines: Getting Maximum Tokens per GPU',
 'subtitle': 'vLLM PagedAttention and its three memory settings, SGLang RadixAttention, TGI, KV cache and '
             "FlashAttention, continuous batching, quantization, memory bandwidth vs FLOPS, a token's "
             'journey through vLLM and SGLang, Crusoe managed inference, and llama.cpp vs vLLM vs SGLang '
             'benchmarks on one GPU',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators tuning inference engines agree that decode is memory-bound: every token '
                      'streams every weight, so tokens per GPU come from packing more concurrent sequences '
                      'behind each weight read. PagedAttention and continuous batching are the baseline; '
                      'KodeKloud lifted KV utilization from about 20% to roughly 95% with 16-token pages, '
                      'and DataMListic credits continuous batching with an order of magnitude in '
                      'throughput. The street mechanics are a handful of knobs: max-model-len, '
                      'max-num-batched-tokens, max-num-seqs, KV pool fraction, FP8 or 4-bit quantization, '
                      'and chunked prefill budgets that trade time to first token against inter-token '
                      'latency. The split is engine choice: vLLM for independent requests, dense models, '
                      'and very large clusters; SGLang once shared-prefix tokens pass 40%, with 2 times or '
                      'more throughput above 70%. Benchmarks conflict, with Lukasz Gawenda measuring vLLM '
                      'ahead on TTFT and end-to-end latency while SGLang won TPOT.',
 'key_metrics': [{'label': 'PagedAttention KV Utilization Lift',
                  'metric': 'PagedAttention KV Utilization Lift',
                  'value': 'About 20% to about 95% utilization; 4 to 5 times more users',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Hands-on vLLM lab where a 512-token reservation wasted roughly 80% of KV '
                             'memory until page size 16 was applied',
                  'source': 'KodeKloud ([qdPkA5mxLhg @ 00:08:00])'},
                 {'label': 'Continuous Batching Throughput Gain',
                  'metric': 'Continuous Batching Throughput Gain',
                  'value': 'An order of magnitude in throughput',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Static batching kept the GPU busy barely more than half the time; continuous '
                             'batching kept it essentially full',
                  'source': 'DataMListic ([X8CwAqYxH1E @ 00:03:23])'},
                 {'label': 'SGLang Shared-Token Throughput Threshold',
                  'metric': 'SGLang Shared-Token Throughput Threshold',
                  'value': 'Above 70% shared tokens: 2 times or more throughput',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Below 20% shared tokens the engines are equal; above 40% SGLang wins; above '
                             '70% it doubles throughput on the same hardware',
                  'source': 'Neural AI Flair ([18AkpuX3vkY @ 00:06:19])'},
                 {'label': 'Quantization Decode Throughput Ladder',
                  'metric': 'Quantization Decode Throughput Ladder',
                  'value': '54 GB to 27 GB to 14 GB; about 60 to 120 to 240 tok/s',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A 27B model moved from BF16 to FP8 to 4-bit on an H100, with single-user '
                             'decode scaling as bytes per token fell',
                  'source': 'AI WITH Rithesh ([lasG5MsR-gE @ 00:11:12])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus',
               'paragraphs': ['Every operator here starts from the same physics: decode is starved by '
                              'memory, not math. DataMListic lays it out bluntly: each generated token '
                              'requires reading every weight, so a 70B model streams roughly 140 GB per '
                              'token while the compute units mostly sit and wait, and batching four '
                              'requests means one weight load yields four tokens: “Same cost, four times '
                              'the throughput” [X8CwAqYxH1E @ 00:00:41]. AI WITH Rithesh puts hard numbers '
                              'on an H100: 80 GB of HBM at 3.35 TB/s against 989 TFLOPS works out to about '
                              '295 ops per byte, and on a 27B model the compute takes 55 microseconds '
                              'versus 16 ms of memory reads, capping single-user decode near 60 tok/s: '
                              '“The memory side takes almost 300 times longer” [lasG5MsR-gE @ 00:07:36]. '
                              'Micro Learning frames the same split as two phases, with prefill '
                              'compute-bound and decode memory-bound [zkMCHA5uzIo @ 00:01:18]. Serverside '
                              'Acquisitions takes it to the hardware-spend level, claiming $400B went into '
                              'chips that sit 85% idle because each token hauls every parameter through '
                              'the chip, the math finishes in under a microsecond, and the $40,000 '
                              'accelerator then idles [BFMPHZZBGlg @ 00:00:00]. The operator takeaway is '
                              'unanimous: tokens per GPU is won by keeping weights streaming to as many '
                              'concurrent sequences as possible.',
                              'The second point of agreement is that legacy serving burns most of its KV '
                              'memory, and paging fixes it. KodeKloud states traditional systems waste 60 '
                              'to 80% of KV memory, and in their lab a 512-token reservation hit only '
                              'about 20% utilization before PagedAttention with page size 16 pushed it to '
                              'roughly 95%, supporting 4 to 5 times more users [qdPkA5mxLhg @ 00:08:00]. '
                              'Neural AI Flair gives the arithmetic: 4K tokens eat more than 1 GB per '
                              'request on an A100-80GB, generating 300 of a possible 2,000 tokens wastes '
                              '84%, and 16-token pages cut fragmentation below 4% [18AkpuX3vkY @ '
                              '00:01:19]. On scheduling, DataMListic shows static batching leaving 14 of '
                              '32 slots producing nothing, keeping the GPU busy “barely more than half the '
                              'time,” while continuous batching evicts finished rows each step, keeps the '
                              'card “essentially full,” and is worth “an order of magnitude in throughput” '
                              '[X8CwAqYxH1E @ 00:03:23]. Uplatz adds the cost of ignoring this: static '
                              'batching reserves for the worst case, so a GPU can throw out-of-memory '
                              'errors while functionally idle, and Ollama, with no continuous batching, is '
                              'prototype-only [jp2pwEpUg-Q @ 00:00:17]. Every practitioner treats paging '
                              'plus continuous batching as the non-negotiable baseline for tokens per GPU, '
                              'not an optional upgrade.',
                              'Practitioners also converge on who the contenders are and roughly where '
                              'each fits, even while they argue over the margins. Vizuara claims private '
                              'open-source LLM deployments “almost always” run on vLLM or SGLang, and '
                              'frames the payoff as cutting a $2M-per-year deployment to $200K '
                              "[f4WDLg2sbx4 @ 00:01:59]. Crusoe AI's solutions engineer Martin Calla says "
                              'both engines are built on paged attention, calls vLLM the “veteran” '
                              'throughput default for dense models like Llama, and positions SGLang for '
                              'MoE models such as DeepSeek and Qwen plus function calling and JSON: “If '
                              'you just need raw inference, speed and reliability, vLLM is the stable '
                              'option” [R74kx7GKEbs @ 00:02:10]. System Decisions lands in the same place, '
                              'noting both engines come out of UC Berkeley, with vLLM winning single-turn '
                              'and batch work and SGLang built around radix-tree prefix reuse and '
                              'compressed FSMs for conversational, structured, or agentic traffic '
                              '[KSQQ4-K5eW0 @ 00:05:30]. Tensor Garage compresses it into a single rule of '
                              'thumb from single-GPU testing on an RTX 4090: “llama.cpp to fit and '
                              'interact, vLLM to batch… SGLang to reuse” [Ym3TP9rlzCk @ 00:12:15]. The '
                              'shared prerequisite is a real serving engine with paging and continuous '
                              'batching underneath; none of these operators recommends pushing concurrent '
                              'production traffic through a prototype runtime.'],
               'table': {'caption': 'Where the practitioners agree on getting maximum tokens per GPU',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Decode speed is bound by memory bandwidth, not FLOPS',
                                   'A 70B model streams about 140 GB per token while compute units wait',
                                   'Batch more sequences behind each weight load to raise tokens per GPU',
                                   'DataMListic ([X8CwAqYxH1E @ 00:00:00]) and AI WITH Rithesh '
                                   '([lasG5MsR-gE @ 00:07:36])'],
                                  ['Legacy KV cache allocation wastes most of the reserved memory',
                                   'Traditional systems waste 60 to 80%; a 512-token reservation hit about '
                                   '20% utilization',
                                   'Fix KV allocation before inefficient memory hoarding forces extra '
                                   'hardware purchases',
                                   'KodeKloud ([qdPkA5mxLhg @ 00:07:05]) and IBM Technology ([McLdlg5Gc9s '
                                   '@ 00:01:07])'],
                                  ['PagedAttention with 16-token pages nearly eliminates fragmentation '
                                   'waste',
                                   'Fragmentation drops under 4% and utilization reaches about 95% in '
                                   'testing',
                                   'Expect 4 to 5 times more concurrent users on the same card',
                                   'Neural AI Flair ([18AkpuX3vkY @ 00:01:19]) and KodeKloud ([qdPkA5mxLhg '
                                   '@ 00:08:35])'],
                                  ['Continuous batching beats static batching by a very wide margin',
                                   'Static batching left 14 of 32 slots idle; continuous batching keeps '
                                   'GPU essentially full',
                                   'Keep runtimes without continuous batching, such as Ollama, on '
                                   'prototype duty only',
                                   'DataMListic ([X8CwAqYxH1E @ 00:01:41]) and Uplatz ([jp2pwEpUg-Q @ '
                                   '00:04:37])'],
                                  ['vLLM and SGLang dominate private open-source LLM deployments today',
                                   'Private deployments almost always run vLLM or SGLang, both built on '
                                   'paged attention',
                                   'Shortlist these two engines first when standing up self-hosted '
                                   'inference capacity',
                                   'Vizuara ([f4WDLg2sbx4 @ 00:02:31]) and Crusoe AI ([R74kx7GKEbs @ '
                                   '00:00:54])'],
                                  ['Inference, not training, carries the dominant share of lifecycle cost',
                                   'Training is 10 to 20% of lifecycle cost while inference takes 80 to '
                                   '90%',
                                   'Tokens per GPU optimization is where the serving budget actually gets '
                                   'recovered',
                                   'Lukasz Gawenda ([gkl2KlJ7FP0 @ 00:00:16]) and Uplatz ([jp2pwEpUg-Q @ '
                                   '00:00:00])'],
                                  ['Engine fit follows workload shape rather than brand loyalty or hype',
                                   'llama.cpp to fit and interact, vLLM to batch, SGLang to reuse prefixes',
                                   "Map each endpoint's traffic pattern before committing to a single "
                                   'serving engine',
                                   'Tensor Garage ([Ym3TP9rlzCk @ 00:12:15]) and System Decisions '
                                   '([KSQQ4-K5eW0 @ 00:05:30])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['On vLLM, the tuning surface is small and brutal. Lukasz Gawenda isolates '
                              'three settings that decide throughput and latency: max-model-len (16K in '
                              'their walkthrough, where a 10K-token request passes and an 18K one is '
                              'rejected), max-num-batched-tokens (12K), and max-num-seqs; chunked prefill, '
                              'the V1 default, splits a 30K request into 8 chunks while prioritizing '
                              'decodes, and a smaller token budget buys better inter-token latency while a '
                              'larger one buys better time to first token [ycEQJIyZ2sU @ 00:09:44]. '
                              'Vizuara traces the same budget inside the engine: a 2,048-token step cap '
                              'filled with 127 decode tokens plus 1,921 prefill tokens, with the remaining '
                              '79 pushed to step N+1 and the next-token prediction from the partial '
                              'prefill discarded [IDjyrXKsC5U @ 00:37:00]. AI WITH Rithesh shows why the '
                              'memory fraction matters: vLLM claims 90% of the H100, leaving about 18 GB '
                              'of KV cache on their 27B example, which fills at roughly 28 users holding '
                              '8K tokens each [lasG5MsR-gE @ 00:10:06]. KodeKloud runs the opposite '
                              'extreme on a tiny SmolLM-135M lab, dropping max-model-len to 64 and '
                              'max-num-seqs to 8, serving on localhost:8000/v1 with the API key literally '
                              '“not needed,” and watching throughput climb with only a slight latency rise '
                              'as load steps from 1 to 5 to 10 to 20 users [qdPkA5mxLhg @ 00:11:33].',
                              "SGLang's edge is prefix reuse, and the practitioners who run it put hard "
                              'numbers on exactly how much shared context it takes to pay off. Neural AI '
                              'Flair reports radix cache hit rates of 60 to 90%, and a shared-token rule: '
                              'below 20% shared tokens the engines are equal, above 40% SGLang wins, and '
                              '“Above 70%, expect two times or more throughput on the same hardware”; they '
                              'also report TTFT up to 5 times lower for SGLang with equal time between '
                              'tokens [18AkpuX3vkY @ 00:06:19]. Vizuara explains why vLLM can only reuse '
                              'true prefixes: blocks hold 16 tokens and each block hash chains to the '
                              'previous one, so arbitrary substrings never match, while SGLang runs a '
                              'token-level radix tree with LRU eviction and schedules requests with the '
                              'most cached tokens first; semantic similarity does not count, because keys '
                              'and values depend on position embedding [IDjyrXKsC5U @ 00:48:44]. AI WITH '
                              "Rithesh adds that SGLang's router lifts cache hit rate from 20% to 75% and "
                              'throughput up to 1.9 times, with grammar-forced multi-token output for '
                              'structured responses [lasG5MsR-gE @ 00:18:11]. Micro Learning warns that '
                              'prompt caching needs an exact prefix match and expires on a TTL, so any '
                              'change at the front of a prompt kills the hit [zkMCHA5uzIo @ 00:03:31].',
                              'Quantization is the most direct multiplier the practitioners quote. AI WITH '
                              'Rithesh walks a 27B model from 54 GB in BF16 to 27 GB in FP8 to 14 GB at '
                              '4-bit, lifting single-stream throughput from about 60 to 120 to roughly 240 '
                              'tok/s, notes Marlin W4A16 delivers around 4 times up to batch 16 to 32, and '
                              'points out that an FP8 KV cache halves per-token cost to 32 KB; their vLLM '
                              'recipe is TP=4, FP8 KV cache, and 3 draft tokens [lasG5MsR-gE @ 00:11:12]. '
                              'Lukasz Gawenda, squeezing a 176B-parameter model onto one 96 GB card, set '
                              "SGLang's KV pool fraction to 0.9 and got only 166k tokens, found raising it "
                              'cost 1.3 GB, and advises setting it lower because GUI VRAM use varies '
                              'between restarts, running at concurrency 1 to 2 [RlsxXB5q-cA @ 00:32:34]. '
                              'For measurement, Tensor Garage fixes model, tokenizer, quantization, '
                              'lengths, and concurrency, keeps streaming on, warms up, clears the prefix '
                              'cache, and records median and p99 latency for TPOT and goodput [Ym3TP9rlzCk '
                              "@ 00:00:49]. Gawenda's head-to-head used bench_serving on ShareGPT with "
                              '1,000 prompts at full burst and 10 warm-ups on an L40S-48C vGPU with 14 '
                              'vCPUs serving a Qwen Coder FP8 model [gkl2KlJ7FP0 @ 00:12:39].'],
               'table': {'caption': 'Exact knobs, settings, and measured effects reported by the '
                                    'practitioners',
                         'headers': ['Lever',
                                     'Exact Setting or Number',
                                     'Measured Effect',
                                     'Expert Source'],
                         'rows': [['vLLM max-model-len context ceiling applied per request',
                                   'A 16K cap accepts a 10K request and rejects 18K',
                                   'Rejects oversized multimodal requests such as 18K visual plus 12K text',
                                   'Lukasz Gawenda ([ycEQJIyZ2sU @ 00:01:37]) on the vLLM length cap'],
                                  ['vLLM max-num-batched-tokens budget for chunked prefill scheduling',
                                   '12K budget; chunked prefill splits a 30K request into 8 chunks',
                                   'Smaller budget improves inter-token latency; larger budget improves '
                                   'time to first token',
                                   'Lukasz Gawenda ([ycEQJIyZ2sU @ 00:09:44]) and Vizuara ([IDjyrXKsC5U @ '
                                   '00:37:00])'],
                                  ['Small-lab sequence and length caps for first vLLM tests',
                                   'max-model-len 64 and max-num-seqs 8 on a SmolLM-135M lab',
                                   'Throughput rises across 1, 5, 10, 20 users while latency rises '
                                   'slightly',
                                   'KodeKloud ([qdPkA5mxLhg @ 00:11:33]) hands-on vLLM lab tuning demo'],
                                  ['Weight quantization stepping from BF16 to FP8 to 4-bit',
                                   '54 GB to 27 GB to 14 GB on a 27B model',
                                   'Single-stream throughput rises from about 60 to 120 to roughly 240 '
                                   'tok/s',
                                   'AI WITH Rithesh ([lasG5MsR-gE @ 00:11:12]) quantization walkthrough on '
                                   'H100'],
                                  ['FP8 KV cache precision setting on vLLM serving stacks',
                                   'Per-token KV cost drops from 64 KB down to 32 KB',
                                   'The same cache memory holds twice as many context tokens overall',
                                   'AI WITH Rithesh ([lasG5MsR-gE @ 00:12:55]) KV cache precision '
                                   'breakdown'],
                                  ['SGLang KV pool memory fraction on a single desktop card',
                                   '0.9 fraction gave only 166k tokens; raising it cost 1.3 GB',
                                   'Set it lower because GUI VRAM use varies between restarts',
                                   'Lukasz Gawenda ([RlsxXB5q-cA @ 00:32:34]) single-GPU SGLang tuning '
                                   'run'],
                                  ['SGLang cache-aware router and radix cache on shared prefixes',
                                   'Router raises cache hit rate from 20% up to 75%',
                                   'Throughput climbs up to 1.9 times on repeated-context workloads',
                                   'AI WITH Rithesh ([lasG5MsR-gE @ 00:18:11]) and Neural AI Flair '
                                   '([18AkpuX3vkY @ 00:03:22])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the benchmarkers actually work the engines',
                           'body': 'Small habits the hands-on operators use to get clean numbers and '
                                   'visible bottlenecks before committing GPU spend.',
                           'items': ['Benchmark with everything pinned: fix model, tokenizer, '
                                     'quantization, lengths, and concurrency, keep streaming on, warm up, '
                                     'clear the prefix cache, and record median and p99 [Tensor Garage — '
                                     'Ym3TP9rlzCk @ 00:00:49].',
                                     'Run your own accuracy checks because official benchmarks are leaked; '
                                     'a McNemar test at the p<0.05 threshold found no GGUF vs NVFP4 '
                                     'difference [Lukasz Gawenda — RlsxXB5q-cA @ 00:34:02].',
                                     'Before tuning, feed the vLLM repo into NotebookLM to get through the '
                                     'internals fast [Lukasz Gawenda — gkl2KlJ7FP0 @ 00:11:24].',
                                     'Wire Prometheus and Grafana onto the vLLM server so throughput and '
                                     'latency are visible as user counts climb [KodeKloud — qdPkA5mxLhg @ '
                                     '00:13:06].']},
               'sop_steps': [{'step': 1,
                              'title': 'Size the KV budget before anything else',
                              'action': 'Subtract model weights and a safety buffer from VRAM to get the '
                                        'KV pool you can distribute across users.',
                              'detail': "Vizuara's worked example: Llama 3.1 8B in BF16 takes 16 GB on an "
                                        '80 GB H100, a 10 GB buffer is held back, and 54 GB remains for KV '
                                        'cache across users sending 2,000 tokens each [Vizuara — '
                                        'IDjyrXKsC5U @ 00:12:09].'},
                             {'step': 2,
                              'title': 'Install and expose an OpenAI-compatible endpoint',
                              'action': 'pip install vLLM on a Linux VM or Kubernetes and serve the model '
                                        'through the OpenAI-compatible API.',
                              'detail': "IBM Technology's workflow is pip install on a Linux VM or "
                                        'Kubernetes, then serve through an OpenAI-compatible endpoint, '
                                        'with vLLM optimized for quantized models [IBM Technology — '
                                        'McLdlg5Gc9s @ 00:03:58].'},
                             {'step': 3,
                              'title': 'Set the three throughput and latency knobs',
                              'action': 'Configure max-model-len, max-num-batched-tokens, and '
                                        'max-num-seqs, then tune the chunked prefill budget.',
                              'detail': "Gawenda's settings were max-model-len 16K and "
                                        'max-num-batched-tokens 12K; shrink the budget for better '
                                        'inter-token latency, grow it for better time to first token '
                                        '[Lukasz Gawenda — ycEQJIyZ2sU @ 00:00:00].'},
                             {'step': 4,
                              'title': 'Load test, then route by shared-prefix ratio',
                              'action': 'Burst-test with real-shaped prompts, then move shared-prefix '
                                        'traffic to SGLang once overlap is high enough.',
                              'detail': 'Run bench_serving on ShareGPT with 1,000 prompts at full burst '
                                        'and 10 warm-ups [Lukasz Gawenda — gkl2KlJ7FP0 @ 00:12:39]; switch '
                                        'to SGLang above 40% shared tokens and expect 2 times or more '
                                        'above 70% [Neural AI Flair — 18AkpuX3vkY @ 00:06:19].'}]},
              {'number': 3,
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The head-to-head numbers do not line up, and operators should treat each '
                              'benchmark as a workload fingerprint rather than a verdict. Lukasz Gawenda '
                              'ran bench_serving on ShareGPT with 1,000 prompts at full burst on an L40S '
                              'vGPU with a Qwen Coder FP8 model, and vLLM took the headline: lower total '
                              'duration, end-to-end latency of 220 seconds against 355, and time to first '
                              'token of 138 against 285 [gkl2KlJ7FP0 @ 00:20:38]. SGLang still won the '
                              'per-token race in that same run, posting 1.45 times better TPOT and '
                              'smoother inter-token latency [gkl2KlJ7FP0 @ 00:21:56]. Neural AI Flair '
                              'reports the opposite on the first-token axis, crediting SGLang with up to 5 '
                              'times lower TTFT while calling time between tokens equal [18AkpuX3vkY @ '
                              '00:07:00]. Tensor Garage adds a third reading from published results: '
                              'SGLang cut TTFT by 30 to 58 percent across seven MoE models on an H200, '
                              'while vLLM held an 18 percent decode edge [Ym3TP9rlzCk @ 00:01:46]. The '
                              'street lesson is that first-token speed, steady decode and total batch '
                              'duration can each crown a different engine on the same day, so the metric '
                              'that actually pays your bills decides the winner, not the reputation of the '
                              'repo or the star count on its page.',
                              'Where practitioners do converge is on letting the shape of the traffic pick '
                              'the engine, but they draw the dividing line in different places. Neural AI '
                              'Flair puts a number on it: general throughput on Llama 3 70B lands at '
                              '17,000 to 19,000 tokens per second with both engines within 15 percent of '
                              'each other, shared tokens below 20 percent make them equal, above 40 '
                              'percent SGLang wins, and above 70 percent the operator should expect two '
                              'times or more throughput on the same hardware [18AkpuX3vkY @ 00:06:19]. '
                              'System Decisions draws the line by job type instead, routing stable or '
                              'single-round work to vLLM and conversational, structured or agentic work to '
                              'SGLang, while conceding vLLM can be faster on a single long generation '
                              '[KSQQ4-K5eW0 @ 00:05:30]. Crusoe AI solutions engineer Martin Calla splits '
                              'by model architecture, calling vLLM the veteran throughput default for '
                              'dense models like Llama and pointing SGLang at MoE models such as DeepSeek '
                              'and Qwen, plus function calling and JSON output [R74kx7GKEbs @ 00:02:28]. '
                              'Vizuara adds a hardware axis: heavy prefix sharing on Nvidia or AMD goes to '
                              'SGLang, other chips go to vLLM, and everything else gets measured before '
                              'anyone commits capacity [IDjyrXKsC5U @ 01:22:26].',
                              'A second camp argues the two-horse race is the wrong frame entirely. Uplatz '
                              'lays out a decision map that pushes sub-100 millisecond latency to '
                              'TensorRT-LLM, 100,000-token documents or AMD and Intel hardware to TGI, and '
                              'concurrent chat to vLLM, backing the TGI call with a claim that TGI v3 '
                              'processes 200,000-token prompts up to 13 times faster than vLLM while '
                              'giving up chat throughput; the same channel dismisses Ollama as '
                              'prototype-only because it lacks continuous batching [jp2pwEpUg-Q @ '
                              '00:05:11]. Tensor Garage compresses its single-GPU verdict into one rule: '
                              'llama.cpp to fit and interact, vLLM to batch, SGLang to reuse [Ym3TP9rlzCk '
                              '@ 00:12:15]. KodeKloud keeps llama.cpp in the kit specifically for CPU and '
                              'RAM-only inference where no GPU is available [qdPkA5mxLhg @ 00:13:23]. '
                              "Lukasz Gawenda's oversized Qwen3.8 Flash test adds a fourth option and "
                              'makes the choice before any number is measured: if weights fit in VRAM, run '
                              'SGLang or vLLM for better long context and day-one speculative decoding; if '
                              'you want to name every memory destination yourself, run llama.cpp on the '
                              'widest hardware range; if you would rather not tune at all, FreeToken sizes '
                              'itself [RlsxXB5q-cA @ 00:24:56].'],
               'table': {'caption': 'Engine Selection Splits: Where Named Practitioners Draw the Line',
                         'headers': ['Decision Axis',
                                     'vLLM-Leaning Playbook',
                                     'SGLang or Alternative Playbook',
                                     'Expert Source'],
                         'rows': [['Shared-prefix share of incoming request traffic',
                                   'Below 20 percent shared tokens, vLLM and SGLang perform equally on '
                                   'throughput',
                                   'Above 40 percent SGLang wins and above 70 percent expect two times or '
                                   'more',
                                   'Neural AI Flair ([18AkpuX3vkY @ 00:06:19])'],
                                  ['Full-burst ShareGPT benchmark on an L40S vGPU',
                                   'vLLM posted lower duration and 220 versus 355 seconds end-to-end '
                                   'latency',
                                   'SGLang returned 1.45 times better TPOT and smoother inter-token '
                                   'latency',
                                   'Lukasz Gawenda ([gkl2KlJ7FP0 @ 00:20:38])'],
                                  ['MoE models served on a single H200 card',
                                   'vLLM held an 18 percent advantage on steady decode throughput',
                                   'SGLang cut time to first token by 30 to 58 percent',
                                   'Tensor Garage ([Ym3TP9rlzCk @ 00:01:46])'],
                                  ['Model architecture and required output format',
                                   'vLLM is the veteran throughput default for dense Llama-style models',
                                   'SGLang is optimized for DeepSeek and Qwen MoE, function calling and '
                                   'JSON',
                                   'Crusoe AI ([R74kx7GKEbs @ 00:02:28])'],
                                  ['Job type and conversation pattern of the endpoint',
                                   'Stable, single-round and batch work, plus single long generations, go '
                                   'to vLLM',
                                   'Conversational, structured and agentic pipelines using radix-tree '
                                   'prefix reuse go to SGLang',
                                   'System Decisions ([KSQQ4-K5eW0 @ 00:05:30])'],
                                  ['Silicon vendor combined with prefix sharing level',
                                   'Chips other than Nvidia or AMD run vLLM; otherwise measure before '
                                   'committing',
                                   'Heavy prefix sharing on Nvidia or AMD hardware runs on SGLang',
                                   'Vizuara ([IDjyrXKsC5U @ 01:22:26])'],
                                  ['Very long documents and hard latency floors',
                                   'vLLM handles concurrent chat but struggles with 200,000-token '
                                   'documents',
                                   'TGI v3 runs 200K prompts up to 13 times faster; TensorRT-LLM for '
                                   'sub-100ms',
                                   'Uplatz ([jp2pwEpUg-Q @ 00:05:11])']]}},
              {'number': 4,
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap every practitioner flags is paying for memory that never '
                              'holds a live token. Uplatz warns that static batching reserves memory for '
                              'the worst case, so a GPU can throw an out-of-memory error while it is '
                              'functionally idle [jp2pwEpUg-Q @ 00:00:17]. DataMListic shows the same rot '
                              'from the slot side: in a locked static batch, 14 of 32 slots produced '
                              'nothing, nearly half the batch was dead weight, the queue kept growing the '
                              'whole time, and the GPU stayed busy barely more than half the time '
                              "[X8CwAqYxH1E @ 00:01:41]. KodeKloud's lab makes the waste visible on a "
                              'small model: a 512-token reservation ran at about 20 percent KV '
                              'utilization, meaning 80 percent wasted, until 16-token pages lifted '
                              'utilization to about 95 percent and supported 4 to 5 times more users '
                              '[qdPkA5mxLhg @ 00:07:05]. Neural AI Flair puts the per-request math in '
                              'plain terms: a request that generates 300 of a possible 2,000 tokens wastes '
                              '84 percent of what was reserved, and a 4,000-token context already eats '
                              'more than 1 GB of KV cache per request on an A100 80GB [18AkpuX3vkY @ '
                              '00:00:40]. Any serving stack that still pre-reserves by maximum length is '
                              'burning paid VRAM on empty space.',
                              'The second cluster of failures is configuration and versioning, and it hits '
                              'hardest at cutover. Lukasz Gawenda shows vLLM rejecting an 18,000-token '
                              'request under a 16,000 max-model-len, then walks through an 18,000-token '
                              'visual plus 12,000-token text request, 30,000 tokens total, that blows past '
                              'both the context limit and the batched-token budget until chunked prefill '
                              'splits it into 8 chunks with decodes prioritized [ycEQJIyZ2sU @ 00:07:20]. '
                              'In his separate head-to-head, vLLM and SGLang alternately broke across '
                              'versions as CUDA moved between 12.8 and 13 [gkl2KlJ7FP0 @ 00:08:32]. Tensor '
                              'Garage pins the dependency friction to specifics: vLLM 0.33.0 needs CUDA 13 '
                              'and Python 3.12, while SGLang sits at 0.5.23 [Ym3TP9rlzCk @ 00:10:15]. '
                              "Gawenda's 96 GB single-card run piles on hard crashes: llama.cpp died "
                              'without the flag that sends the engram table to RAM, SGLang crashed unless '
                              '4-bit weights, 8-bit KV cache and an NVMe-resident table all fit at once, '
                              'SGLang crashed his PC several times, and a KV pool fraction of 0.9 yielded '
                              'only 166,000 tokens while raising it cost another 1.3 GB, so he normally '
                              'sets it lower because GUI VRAM use varies between restarts [RlsxXB5q-cA @ '
                              '00:32:34].',
                              'The economics checks cut against pure hardware thinking. Uplatz warns that '
                              "a single ML Ops salary can exceed the entire GPU bill, that TensorRT-LLM's "
                              'FP8 speed on H100s comes with NVIDIA lock-in and six-figure engineers, and '
                              'that vLLM itself carries a 10 to 20 percent compute overhead from memory '
                              'lookups [jp2pwEpUg-Q @ 00:05:50]. AI WITH Rithesh grounds the ceiling in '
                              'arithmetic: on an H100 the decode math takes 55 microseconds against 16 '
                              'milliseconds of memory reads, single-user decode tops out near 60 tokens '
                              'per second, and with vLLM claiming 90 percent of memory the remaining 18 GB '
                              'of cache fills at about 28 users holding 8,000 tokens each [lasG5MsR-gE @ '
                              '00:10:06]. Serverside Acquisitions frames the macro version: hundreds of '
                              'billions spent on chips that sit mostly idle, because decode arithmetic '
                              'intensity collapses and extra FLOPS barely help when memory bandwidth is '
                              'the wall [BFMPHZZBGlg @ 00:02:38]. Lukasz Gawenda adds the operational fine '
                              'print from his own rig: llama.cpp starts in about 16 seconds against more '
                              'than 100 for SGLang, FreeToken starts even slower and returns a 200 on its '
                              'health check before the model is actually loaded, and he scripts Docker to '
                              'auto-start engines so the box is not burning power while idle [RlsxXB5q-cA '
                              '@ 00:41:49].'],
               'table': {'caption': 'Firsthand Failure Modes Reported on Live Inference Rigs',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Operator Check or Fix',
                                     'Expert Source'],
                         'rows': [['Static batching with worst-case memory reservation',
                                   'The GPU runs out of memory while it is functionally idle',
                                   'Move to continuous batching; Ollama lacks it, so keep it for '
                                   'prototypes',
                                   'Uplatz ([jp2pwEpUg-Q @ 00:00:17])'],
                                  ['Locked batch slots held by already finished requests',
                                   '14 of 32 slots produced nothing while the queue kept growing',
                                   'Decide the batch per step so finished rows are evicted and queued '
                                   'requests enter',
                                   'DataMListic ([X8CwAqYxH1E @ 00:01:41])'],
                                  ['Contiguous KV reservation sized per maximum sequence',
                                   'A 512-token reservation ran near 20 percent utilization, 80 percent '
                                   'wasted',
                                   'Use 16-token pages to reach about 95 percent and 4 to 5 times more '
                                   'users',
                                   'KodeKloud ([qdPkA5mxLhg @ 00:07:05])'],
                                  ['Oversized multimodal request hitting engine limits',
                                   '18K visual plus 12K text equals 30K tokens, exceeding both configured '
                                   'limits',
                                   'Size max-model-len and batched-token budget; chunked prefill splits it '
                                   'into 8 chunks',
                                   'Lukasz Gawenda ([ycEQJIyZ2sU @ 00:07:20])'],
                                  ['CUDA and engine version drift between benchmark runs',
                                   'vLLM and SGLang alternately broke when moving between CUDA 12.8 and 13',
                                   'Check each engine against the CUDA build it actually requires before '
                                   'running comparisons',
                                   'Lukasz Gawenda ([gkl2KlJ7FP0 @ 00:08:32])'],
                                  ['Assuming prefix caching reuses any similar text',
                                   'Chained block hashes mean only prefixes are reused, never arbitrary '
                                   'substrings',
                                   'Expect reuse only from identical leading blocks; semantic similarity '
                                   'is not enough',
                                   'Vizuara ([IDjyrXKsC5U @ 00:48:44])'],
                                  ['Readiness signals and startup lag on restarts',
                                   'FreeToken returns 200 on health check before loading; SGLang takes '
                                   'over 100 seconds',
                                   'Route traffic only after the model has actually loaded, not on health '
                                   'status',
                                   'Lukasz Gawenda ([RlsxXB5q-cA @ 00:41:49])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Traffic Gate Before Any Engine Takes Paid Load',
                           'body': 'Every item below comes from a rig that crashed, rejected requests, or '
                                   'burned money in front of a named practitioner. Clear all four before '
                                   'routing production traffic or quoting a tokens-per-GPU number to a '
                                   'buyer.',
                           'items': ['Confirm the largest real request fits both max-model-len and '
                                     'max-num-batched-tokens, because an 18K visual plus 12K text request '
                                     'at 30K tokens exceeded both limits [Lukasz Gawenda — ycEQJIyZ2sU @ '
                                     '00:07:20].',
                                     'Re-run both engines after any CUDA change, because vLLM and SGLang '
                                     'alternately broke across versions between CUDA 12.8 and 13 [Lukasz '
                                     'Gawenda — gkl2KlJ7FP0 @ 00:08:32].',
                                     'Set the SGLang KV pool fraction below the maximum, because 0.9 '
                                     'yielded only 166K tokens, raising it cost 1.3 GB, and GUI VRAM use '
                                     'varies between restarts [Lukasz Gawenda — RlsxXB5q-cA @ 00:32:34].',
                                     'Price the engineering headcount against the GPU bill before choosing '
                                     'a complex engine, because one ML Ops salary can exceed the entire '
                                     'GPU spend [Uplatz — jp2pwEpUg-Q @ 00:05:50].']}}],
 'pull_quote': '"We only stopped letting the slowest request hold everyone else hostage." — DataMListic '
               '(X8CwAqYxH1E @ 00:03:43).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Run a controlled benchmark: fix model, tokenizer, quantization, lengths and '
                      'concurrency, keep streaming on, warm up, clear the prefix cache, and record median '
                      'and p99 [Tensor Garage — Ym3TP9rlzCk @ 00:00:20].',
                      'Measure the shared-token share of your traffic before picking an engine: below 20 '
                      'percent the engines are equal, above 40 percent SGLang wins, above 70 percent '
                      'expect 2x or more [Neural AI Flair — 18AkpuX3vkY @ 00:06:19].',
                      'Tune the three vLLM settings, max-model-len, max-num-batched-tokens and '
                      'max-num-seqs, using a smaller token budget for better ITL and a larger one for '
                      'better TTFT [Lukasz Gawenda — ycEQJIyZ2sU @ 00:09:44].',
                      'Quantize to cut memory reads: 54 GB to 27 GB in FP8 to 14 GB in 4-bit took decode '
                      'from about 60 to 120 to about 240 tok/s, and FP8 KV cache halves it to 32 KB per '
                      'token [AI WITH Rithesh — lasG5MsR-gE @ 00:11:12].',
                      'Load test the OpenAI-compatible endpoint at 1, 5, 10 and 20 concurrent users and '
                      'watch throughput and latency rise, then monitor with Prometheus and Grafana '
                      '[KodeKloud — qdPkA5mxLhg @ 00:10:03].',
                      'Stress both engines with bench_serving on ShareGPT using 1,000 prompts at full '
                      'burst and 10 warm-ups before committing capacity [Lukasz Gawenda — gkl2KlJ7FP0 @ '
                      '00:12:39].'],
 'statutory_citations': [{'title': 'Neural AI Flair — SGLang vs vLLM: Which LLM Inference Framework Should '
                                   'You Use? [00:06:19]',
                          'url': 'https://www.youtube.com/watch?v=18AkpuX3vkY&t=379s',
                          'relevance': 'Primary practitioner testimony on the shared-token thresholds that '
                                       'decide whether SGLang doubles throughput over vLLM.'},
                         {'title': "Lukasz Gawenda — I Benchmarked vLLM vs SGLang So You Don't Have To "
                                   'Shocking Results! [00:20:38]',
                          'url': 'https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=1238s',
                          'relevance': 'Primary practitioner testimony on full-burst benchmark results '
                                       'splitting latency wins to vLLM and TPOT wins to SGLang.'},
                         {'title': 'Uplatz — LLM Inference Engines 2026 | Comparing vLLM, SGLang & Hugging '
                                   'Face TGI | Uplatz [00:05:11]',
                          'url': 'https://www.youtube.com/watch?v=jp2pwEpUg-Q&t=311s',
                          'relevance': 'Primary practitioner testimony on the TensorRT-LLM, TGI and vLLM '
                                       'decision map and engineering cost versus GPU bill.'},
                         {'title': 'Vizuara — Journey of a token in vLLM and SGLang [01:22:26]',
                          'url': 'https://www.youtube.com/watch?v=IDjyrXKsC5U&t=4946s',
                          'relevance': 'Primary practitioner testimony on choosing SGLang versus vLLM by '
                                       'prefix sharing and chip vendor.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'McLdlg5Gc9s',
                       'title': 'What is vLLM? Efficient AI Inference for Large Language Models',
                       'channel': 'IBM Technology',
                       'author': 'IBM Technology',
                       'text': 'The vLLM paper reported 24 times the throughput of Hugging Face '
                               'Transformers and TGI.',
                       'tip': 'The vLLM paper reported 24 times the throughput of Hugging Face '
                              'Transformers and TGI.',
                       'timestamp': 143,
                       'timestamp_seconds': 143,
                       'timestamp_label': '[00:02:23]',
                       'url': 'https://www.youtube.com/watch?v=McLdlg5Gc9s&t=143s',
                       'markdown': '[00:02:23](https://www.youtube.com/watch?v=McLdlg5Gc9s&t=143s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f4WDLg2sbx4',
                       'title': 'How inference works at scale? vLLM and SGLang inference engines',
                       'channel': 'Vizuara',
                       'author': 'Vizuara',
                       'text': 'Deployment cost drops from $2 million a year to $200,000 a year.',
                       'tip': 'Deployment cost drops from $2 million a year to $200,000 a year.',
                       'timestamp': 119,
                       'timestamp_seconds': 119,
                       'timestamp_label': '[00:01:59]',
                       'url': 'https://www.youtube.com/watch?v=f4WDLg2sbx4&t=119s',
                       'markdown': '[00:01:59](https://www.youtube.com/watch?v=f4WDLg2sbx4&t=119s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jp2pwEpUg-Q',
                       'title': 'LLM Inference Engines 2026 | Comparing vLLM, SGLang & Hugging Face TGI | '
                                'Uplatz',
                       'channel': 'Uplatz',
                       'author': 'Uplatz',
                       'text': 'These memory lookups add a 10 to 20% compute overhead.',
                       'tip': 'These memory lookups add a 10 to 20% compute overhead.',
                       'timestamp': 119,
                       'timestamp_seconds': 119,
                       'timestamp_label': '[00:01:59]',
                       'url': 'https://www.youtube.com/watch?v=jp2pwEpUg-Q&t=119s',
                       'markdown': '[00:01:59](https://www.youtube.com/watch?v=jp2pwEpUg-Q&t=119s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ym3TP9rlzCk',
                       'title': 'llama.cpp vs vLLM vs SGLang: Which Is Fastest on One GPU?',
                       'channel': 'Tensor Garage',
                       'author': 'Tensor Garage',
                       'text': 'llama.cpp to fit and interact, vLLM to batch, SGLang to reuse.',
                       'tip': 'llama.cpp to fit and interact, vLLM to batch, SGLang to reuse.',
                       'timestamp': 735,
                       'timestamp_seconds': 735,
                       'timestamp_label': '[00:12:15]',
                       'url': 'https://www.youtube.com/watch?v=Ym3TP9rlzCk&t=735s',
                       'markdown': '[00:12:15](https://www.youtube.com/watch?v=Ym3TP9rlzCk&t=735s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qdPkA5mxLhg',
                       'title': 'Understanding vLLM with a Hands On Demo',
                       'channel': 'KodeKloud',
                       'author': 'KodeKloud',
                       'text': 'Legacy systems waste 60 to 80% of KV cache memory.',
                       'tip': 'Legacy systems waste 60 to 80% of KV cache memory.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=qdPkA5mxLhg&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=qdPkA5mxLhg&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zkMCHA5uzIo',
                       'title': 'LLM Inference Optimization Explained: KV Cache, Flash Attention, vLLM & '
                                'SGLang',
                       'channel': 'Micro Learning',
                       'author': 'Micro Learning',
                       'text': 'Static batching is like a taxi, while continuous batching is like '
                               'UberPool.',
                       'tip': 'Static batching is like a taxi, while continuous batching is like UberPool.',
                       'timestamp': 418,
                       'timestamp_seconds': 418,
                       'timestamp_label': '[00:06:58]',
                       'url': 'https://www.youtube.com/watch?v=zkMCHA5uzIo&t=418s',
                       'markdown': '[00:06:58](https://www.youtube.com/watch?v=zkMCHA5uzIo&t=418s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '18AkpuX3vkY',
                       'title': 'SGLang vs vLLM: Which LLM Inference Framework Should You Use?',
                       'channel': 'Neural AI Flair',
                       'author': 'Neural AI Flair',
                       'text': 'Above 70%, expect two times or more throughput on the same hardware.',
                       'tip': 'Above 70%, expect two times or more throughput on the same hardware.',
                       'timestamp': 379,
                       'timestamp_seconds': 379,
                       'timestamp_label': '[00:06:19]',
                       'url': 'https://www.youtube.com/watch?v=18AkpuX3vkY&t=379s',
                       'markdown': '[00:06:19](https://www.youtube.com/watch?v=18AkpuX3vkY&t=379s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R74kx7GKEbs',
                       'title': 'AI Lab: Open-source inference with vLLM + SGLang | Optimizing KV cache '
                                'with Crusoe Managed Inference',
                       'channel': 'Crusoe AI',
                       'author': 'Crusoe AI',
                       'text': 'If you just need raw inference, speed and reliability, vLLM is the stable '
                               'option.',
                       'tip': 'If you just need raw inference, speed and reliability, vLLM is the stable '
                              'option.',
                       'timestamp': 130,
                       'timestamp_seconds': 130,
                       'timestamp_label': '[00:02:10]',
                       'url': 'https://www.youtube.com/watch?v=R74kx7GKEbs&t=130s',
                       'markdown': '[00:02:10](https://www.youtube.com/watch?v=R74kx7GKEbs&t=130s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ycEQJIyZ2sU',
                       'title': 'vLLM Explained in 10 Min: 3 Settings for Insanely Fast Throughput & '
                                'Latency!',
                       'channel': 'Lukasz Gawenda',
                       'author': 'Lukasz Gawenda',
                       'text': 'A request of 18K visual tokens plus 12K text tokens, 30K in total, exceeds '
                               'both limits.',
                       'tip': 'A request of 18K visual tokens plus 12K text tokens, 30K in total, exceeds '
                              'both limits.',
                       'timestamp': 440,
                       'timestamp_seconds': 440,
                       'timestamp_label': '[00:07:20]',
                       'url': 'https://www.youtube.com/watch?v=ycEQJIyZ2sU&t=440s',
                       'markdown': '[00:07:20](https://www.youtube.com/watch?v=ycEQJIyZ2sU&t=440s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gkl2KlJ7FP0',
                       'title': "I Benchmarked vLLM vs SGLang So You Don't Have To Shocking Results!",
                       'channel': 'Lukasz Gawenda',
                       'author': 'Lukasz Gawenda',
                       'text': 'vLLM and SGLang alternately broke across versions, CUDA 12.8 versus CUDA '
                               '13.',
                       'tip': 'vLLM and SGLang alternately broke across versions, CUDA 12.8 versus CUDA '
                              '13.',
                       'timestamp': 512,
                       'timestamp_seconds': 512,
                       'timestamp_label': '[00:08:32]',
                       'url': 'https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=512s',
                       'markdown': '[00:08:32](https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=512s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gkl2KlJ7FP0',
                       'title': "I Benchmarked vLLM vs SGLang So You Don't Have To Shocking Results!",
                       'channel': 'Lukasz Gawenda',
                       'author': 'Lukasz Gawenda',
                       'text': 'SGLang delivered 1.45 times better time per output token than vLLM.',
                       'tip': 'SGLang delivered 1.45 times better time per output token than vLLM.',
                       'timestamp': 1316,
                       'timestamp_seconds': 1316,
                       'timestamp_label': '[00:21:56]',
                       'url': 'https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=1316s',
                       'markdown': '[00:21:56](https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=1316s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KSQQ4-K5eW0',
                       'title': 'SGLang vs. vLLM: The New Throughput King?',
                       'channel': 'System Decisions',
                       'author': 'System Decisions',
                       'text': 'Stable or single-round work goes to vLLM, while conversational, structured '
                               'or agentic work goes to SGLang.',
                       'tip': 'Stable or single-round work goes to vLLM, while conversational, structured '
                              'or agentic work goes to SGLang.',
                       'timestamp': 330,
                       'timestamp_seconds': 330,
                       'timestamp_label': '[00:05:30]',
                       'url': 'https://www.youtube.com/watch?v=KSQQ4-K5eW0&t=330s',
                       'markdown': '[00:05:30](https://www.youtube.com/watch?v=KSQQ4-K5eW0&t=330s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IDjyrXKsC5U',
                       'title': 'Journey of a token in vLLM and SGLang',
                       'channel': 'Vizuara',
                       'author': 'Vizuara',
                       'text': 'With heavy prefix sharing on Nvidia or AMD, use SGLang; with other chips, '
                               'use vLLM; otherwise, measure.',
                       'tip': 'With heavy prefix sharing on Nvidia or AMD, use SGLang; with other chips, '
                              'use vLLM; otherwise, measure.',
                       'timestamp': 4946,
                       'timestamp_seconds': 4946,
                       'timestamp_label': '[01:22:26]',
                       'url': 'https://www.youtube.com/watch?v=IDjyrXKsC5U&t=4946s',
                       'markdown': '[01:22:26](https://www.youtube.com/watch?v=IDjyrXKsC5U&t=4946s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'X8CwAqYxH1E',
                       'title': 'Continuous Batching - How LLM Servers Keep the GPU Full',
                       'channel': 'DataMListic',
                       'author': 'DataMListic',
                       'text': 'We only stopped letting the slowest request hold everyone else hostage.',
                       'tip': 'We only stopped letting the slowest request hold everyone else hostage.',
                       'timestamp': 223,
                       'timestamp_seconds': 223,
                       'timestamp_label': '[00:03:43]',
                       'url': 'https://www.youtube.com/watch?v=X8CwAqYxH1E&t=223s',
                       'markdown': '[00:03:43](https://www.youtube.com/watch?v=X8CwAqYxH1E&t=223s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lasG5MsR-gE',
                       'title': 'How LLMs Actually Run on a GPU: vLLM, SGLang & Quantization Explained',
                       'channel': 'AI WITH Rithesh',
                       'author': 'AI WITH Rithesh',
                       'text': "When you're serving one user, memory is the bottleneck.",
                       'tip': "When you're serving one user, memory is the bottleneck.",
                       'timestamp': 1170,
                       'timestamp_seconds': 1170,
                       'timestamp_label': '[00:19:30]',
                       'url': 'https://www.youtube.com/watch?v=lasG5MsR-gE&t=1170s',
                       'markdown': '[00:19:30](https://www.youtube.com/watch?v=lasG5MsR-gE&t=1170s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RlsxXB5q-cA',
                       'title': 'Qwen3.8 Flash: Over 7x Faster First Token | llama.cpp vs SGLang vs '
                                'FreeToken. Benchmarked!',
                       'channel': 'Lukasz Gawenda',
                       'author': 'Lukasz Gawenda',
                       'text': 'This is the choice before any number is measured.',
                       'tip': 'This is the choice before any number is measured.',
                       'timestamp': 1496,
                       'timestamp_seconds': 1496,
                       'timestamp_label': '[00:24:56]',
                       'url': 'https://www.youtube.com/watch?v=RlsxXB5q-cA&t=1496s',
                       'markdown': '[00:24:56](https://www.youtube.com/watch?v=RlsxXB5q-cA&t=1496s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BFMPHZZBGlg',
                       'title': 'FLOPS Are a Lie: Why Memory Bandwidth Actually Controls AI Speed',
                       'channel': 'Serverside Acquisitions',
                       'author': 'Serverside Acquisitions',
                       'text': 'The real war for AI speed is being fought across 2,048 microscopic lanes '
                               'of copper, one picojoule and one thermal micron at a time.',
                       'tip': 'The real war for AI speed is being fought across 2,048 microscopic lanes of '
                              'copper, one picojoule and one thermal micron at a time.',
                       'timestamp': 1025,
                       'timestamp_seconds': 1025,
                       'timestamp_label': '[00:17:05]',
                       'url': 'https://www.youtube.com/watch?v=BFMPHZZBGlg&t=1025s',
                       'markdown': '[00:17:05](https://www.youtube.com/watch?v=BFMPHZZBGlg&t=1025s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
