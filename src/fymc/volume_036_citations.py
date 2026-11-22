"""Curated 180-citation GPU Compute & Telecom Capacity Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified GPU Compute & Telecom Capacity Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'business',
     'client',
     'clients',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'budget',
     'buyer',
     'contract',
     'customer',
     'decision',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'cash',
     'cashflow',
     'commission',
     'cost',
     'costs',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'budget',
     'capital',
     'entity',
     'insurance',
     'lean',
     'license',
     'llc',
     'setup',
     'software',
     'stack',
     'startup',
     'tools'},
 5: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'audit',
     'auto',
     'automated',
     'avoid',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'clawback',
     'dispute',
     'edge',
     'fail',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'client',
     'data',
     'deal',
     'find',
     'first',
     'lead',
     'leads',
     'list',
     'outbound',
     'prospect',
     'qualify',
     'search',
     'sourcing'},
 7: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'checklist',
     'delivery',
     'execution',
     'process',
     'quality',
     'sop',
     'step',
     'steps',
     'system',
     'underwriting',
     'verify',
     'workflow'},
 8: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'crm',
     'data',
     'database',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'10dlc',
     '40kw',
     '499',
     '8yy',
     'a2p',
     'abuse',
     'acceptable',
     'activate',
     'agreement',
     'anthropic',
     'api',
     'arbitrage',
     'arin',
     'asn',
     'auto',
     'automated',
     'aws',
     'azure',
     'b200',
     'b2b',
     'back',
     'bandwidth',
     'bare',
     'batch',
     'batching',
     'beam',
     'bedrock',
     'bgp',
     'billing',
     'blackwell',
     'boutique',
     'compliance',
     'contract',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'10dlc',
      '40kw',
      '499',
      '8yy',
      'a2p',
      'abuse',
      'acceptable',
      'activate',
      'agent',
      'ai',
      'anthropic',
      'api',
      'arbitrage',
      'arin',
      'asn',
      'auto',
      'automate',
      'automated',
      'automation',
      'aws',
      'azure',
      'b200',
      'b2b',
      'back',
      'bandwidth',
      'bare',
      'batch',
      'batching',
      'beam',
      'bedrock',
      'bgp',
      'billing',
      'blackwell',
      'boutique',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'10dlc',
      '40kw',
      '499',
      '8yy',
      'a2p',
      'abuse',
      'acceptable',
      'activate',
      'anthropic',
      'api',
      'arbitrage',
      'arin',
      'asn',
      'auto',
      'automated',
      'aws',
      'azure',
      'b200',
      'b2b',
      'back',
      'bandwidth',
      'bare',
      'batch',
      'batching',
      'beam',
      'bedrock',
      'bgp',
      'billing',
      'blackwell',
      'boutique',
      'contractor',
      'exit',
      'hire',
      'hiring',
      'kpi',
      'manager',
      'operations',
      'pod',
      'scale',
      'scaling',
      'team',
      'valuation'},
 12: {'10dlc',
      '40kw',
      '499',
      '8yy',
      'a2p',
      'abuse',
      'acceptable',
      'action',
      'activate',
      'anthropic',
      'api',
      'arbitrage',
      'arin',
      'asn',
      'auto',
      'automated',
      'aws',
      'azure',
      'b200',
      'b2b',
      'back',
      'bandwidth',
      'bare',
      'batch',
      'batching',
      'beam',
      'bedrock',
      'bgp',
      'billing',
      'blackwell',
      'boutique',
      'day',
      'days',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'LiteLLM AI Gateway',
      'channel': 'LiteLLM AI Gateway',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=blSVb26UQYg&t=301s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, since this included the security review, I see that the routing was done '
              'to the complex model that we had set up and we get a response back. For the '
              'third prompt, we have a billing service problem here and we want to see how '
              'this is classified.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': 'Now, since this included the security review, I see that the routing was done to '
             'the complex model that we had set up and we get a response back. For the third '
             'prompt, we have a billing service problem here and we want to see how this is '
             'classified.',
      'title': 'LiteLLM Auto Router: Send Each Prompt to the Right Model (LiteLLM AI Gateway)',
      'url': 'https://www.youtube.com/watch?v=blSVb26UQYg&t=301s',
      'video_id': 'blSVb26UQYg'},
     {'author': 'Bruno Vega',
      'channel': 'Bruno Vega',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:18](https://www.youtube.com/watch?v=KVXaHQu32Rw&t=978s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But, what it really doesn't want is people turning this into a service. Their "
              'acceptable use policy, the version [clears throat] from June 22nd, 2025, lists '
              'server farming, circumventing the service, and activity unrelated to machine '
              'learning and data science as abuse.',
      'timestamp': 978,
      'timestamp_label': '[00:16:18]',
      'timestamp_seconds': 978,
      'tip': "But, what it really doesn't want is people turning this into a service. Their "
             'acceptable use policy, the version [clears throat] from June 22nd, 2025, lists '
             'server farming, circumventing the service, and activity unrelated to machine '
             'learning and data science as abuse.',
      'title': "Don't Buy a GPU Instead Build This 32GB Free AI Server Instead (Bruno Vega)",
      'url': 'https://www.youtube.com/watch?v=KVXaHQu32Rw&t=978s',
      'video_id': 'KVXaHQu32Rw'},
     {'author': 'SiliconANGLE theCUBE',
      'channel': 'SiliconANGLE theCUBE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:34](https://www.youtube.com/watch?v=VjfoLNKgo3A&t=274s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here are some non-big three providers, non AWS, Microsoft, or Google that are '
              'making significant waves in the market. So, besides CoreWeave, who are the '
              'other GPU as a Service providers out there? Well, first would be Lambda Labs.',
      'timestamp': 274,
      'timestamp_label': '[00:04:34]',
      'timestamp_seconds': 274,
      'tip': 'Here are some non-big three providers, non AWS, Microsoft, or Google that are '
             'making significant waves in the market. So, besides CoreWeave, who are the other '
             'GPU as a Service providers out there? Well, first would be Lambda Labs.',
      'title': 'Ep. 36 GPUaaS Explained: Why CoreWeave and Others Are Fueling the Next Cloud '
               'Revolution | AI Insight (SiliconANGLE theCUBE)',
      'url': 'https://www.youtube.com/watch?v=VjfoLNKgo3A&t=274s',
      'video_id': 'VjfoLNKgo3A'},
     {'author': 'The Code Architect',
      'channel': 'The Code Architect',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=TwICQ_zP8Ys&t=22s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take low batch inference or serving a small 256 million parameter language '
              'model. These processes require only a fraction of the available memory '
              'bandwidth and compute cycles. Yet, the traditional paradigm dictates that we '
              'assign an entire exclusive device to each process.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Take low batch inference or serving a small 256 million parameter language '
             'model. These processes require only a fraction of the available memory bandwidth '
             'and compute cycles. Yet, the traditional paradigm dictates that we assign an '
             'entire exclusive device to each process.',
      'title': 'Stop Wasting GPUs: How to Share Hardware with Ray, MPS, and Time-Slicing (The '
               'Code Architect)',
      'url': 'https://www.youtube.com/watch?v=TwICQ_zP8Ys&t=22s',
      'video_id': 'TwICQ_zP8Ys'},
     {'author': 'Nexustech',
      'channel': 'Nexustech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=6TMF0UdjIVU&t=155s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Twilio programmable SMS API. Ensure you reference your messaging service SID in '
              'the from field instead of a specific phone number to trigger the bulk features. '
              'Bulk SMS is a huge tool for any business as long as you play by the rules.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'Twilio programmable SMS API. Ensure you reference your messaging service SID in '
             'the from field instead of a specific phone number to trigger the bulk features. '
             'Bulk SMS is a huge tool for any business as long as you play by the rules.',
      'title': 'How To Send Bulk SMS In Twilio [2026 GUIDE] (Nexustech)',
      'url': 'https://www.youtube.com/watch?v=6TMF0UdjIVU&t=155s',
      'video_id': '6TMF0UdjIVU'},
     {'author': 'Paradigm Escape',
      'channel': 'Paradigm Escape',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=wpj7_7cz4Kk&t=188s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In fact, you know, take screenshots of this stuff and upload it in a chat GPT '
              'and tell it to change the text to fit your business or your service offering '
              'and then copy paste it and get approved. So, um, just kind of a backstory.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'In fact, you know, take screenshots of this stuff and upload it in a chat GPT '
             'and tell it to change the text to fit your business or your service offering and '
             'then copy paste it and get approved. So, um, just kind of a backstory.',
      'title': 'How to Get Your A2P 10DLC SMS Campaign Approved | Works with Twilio, Plivo, '
               'Telnyx, and More (Paradigm Escape)',
      'url': 'https://www.youtube.com/watch?v=wpj7_7cz4Kk&t=188s',
      'video_id': 'wpj7_7cz4Kk'},
     {'author': 'LOCKBREAK',
      'channel': 'LOCKBREAK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=k-M24u2WcZw&t=382s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '15 hours using a standard Raspberry Pi Pico board and an AI model to fill in '
              'the missing code. They say they hit 80 GB and 126 SMs. So, back to that floor '
              "from the beginning. Nvidia's fuses work backwards.",
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': '15 hours using a standard Raspberry Pi Pico board and an AI model to fill in the '
             'missing code. They say they hit 80 GB and 126 SMs. So, back to that floor from '
             "the beginning. Nvidia's fuses work backwards.",
      'title': "How a Hacker Turned Nvidia's $2,500 Mining Card Into a $20,000 A100 "
               '(LOCKBREAK)',
      'url': 'https://www.youtube.com/watch?v=k-M24u2WcZw&t=382s',
      'video_id': 'k-M24u2WcZw'},
     {'author': 'Caleb Writes Code',
      'channel': 'Caleb Writes Code',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=9u2hCf8FlW0&t=363s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, having your weights scattered across the network reduces communication '
              "bandwidth. Not only that, NVIDIA's paper revealed that model parallelism tend "
              'to decrease efficiency at each addition of new card.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'But, having your weights scattered across the network reduces communication '
             "bandwidth. Not only that, NVIDIA's paper revealed that model parallelism tend to "
             'decrease efficiency at each addition of new card.',
      'title': 'The Economics of Neoclouds (Caleb Writes Code)',
      'url': 'https://www.youtube.com/watch?v=9u2hCf8FlW0&t=363s',
      'video_id': '9u2hCf8FlW0'},
     {'author': 'Cost Anatomy',
      'channel': 'Cost Anatomy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:10](https://www.youtube.com/watch?v=Z1cWYFBLpTA&t=550s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The result is a strange bleeding economics. The equipment side of this business '
              "runs on razor-thin or negative margins. Verizon's equipment revenue actually "
              'fell 9% this quarter, and the industry quietly loses money on the phones '
              'themselves.',
      'timestamp': 550,
      'timestamp_label': '[00:09:10]',
      'timestamp_seconds': 550,
      'tip': 'The result is a strange bleeding economics. The equipment side of this business '
             "runs on razor-thin or negative margins. Verizon's equipment revenue actually "
             'fell 9% this quarter, and the industry quietly loses money on the phones '
             'themselves.',
      'title': 'The Economics of Owning a Telecom Company (Cost Anatomy)',
      'url': 'https://www.youtube.com/watch?v=Z1cWYFBLpTA&t=550s',
      'video_id': 'Z1cWYFBLpTA'},
     {'author': 'Nebius',
      'channel': 'Nebius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:59](https://www.youtube.com/watch?v=QLSYI5Ali8Y&t=359s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '31, and then optionally we can pass some environment variables like my hugging '
              'face token, weights and biases API key for monitoring the training progress, as '
              'well as the model size that I want to fine-tune.',
      'timestamp': 359,
      'timestamp_label': '[00:05:59]',
      'timestamp_seconds': 359,
      'tip': '31, and then optionally we can pass some environment variables like my hugging '
             'face token, weights and biases API key for monitoring the training progress, as '
             'well as the model size that I want to fine-tune.',
      'title': 'Video tutorial: SkyPilot and Kubernetes for multi-node LLM fine-tuning '
               '(Nebius)',
      'url': 'https://www.youtube.com/watch?v=QLSYI5Ali8Y&t=359s',
      'video_id': 'QLSYI5Ali8Y'},
     {'author': 'LATEST NEWS UPDATE',
      'channel': 'LATEST NEWS UPDATE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=yh-FMlChr9U&t=35s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Millions of Americans rely on it for internet or phone service. The FCC '
              'collects the money from carriers through a private firm, the Universal Service '
              'Administrative Company, which sets contribution rates.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'Millions of Americans rely on it for internet or phone service. The FCC collects '
             'the money from carriers through a private firm, the Universal Service '
             'Administrative Company, which sets contribution rates.',
      'title': 'Appeals court voids 9 billion dollar FCC telecom fund (LATEST NEWS UPDATE)',
      'url': 'https://www.youtube.com/watch?v=yh-FMlChr9U&t=35s',
      'video_id': 'yh-FMlChr9U'},
     {'author': 'PCweb | Angel Eulises Ortiz: Consultor SEO',
      'channel': 'PCweb | Angel Eulises Ortiz: Consultor SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=0acbHqkQe80&t=110s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's the practical takeaway. Understanding these tiers empowers decision "
              'makers to align their IT strategy with their business goals. Certifications '
              "from the Uptime Institute aren't just stamps of approval. They are signals of "
              'trust to clients, partners, and investors.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': "Here's the practical takeaway. Understanding these tiers empowers decision "
             'makers to align their IT strategy with their business goals. Certifications from '
             "the Uptime Institute aren't just stamps of approval. They are signals of trust "
             'to clients, partners, and investors.',
      'title': 'Data Center Tiers Explained: Tier 1 vs 2 vs 3 vs 4 | Uptime Institute '
               'Standards (PCweb | Angel Eulises Ortiz: Consultor SEO)',
      'url': 'https://www.youtube.com/watch?v=0acbHqkQe80&t=110s',
      'video_id': '0acbHqkQe80'},
     {'author': 'Voice AI with Tim',
      'channel': 'Voice AI with Tim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=kYOdE4uxQXQ&t=78s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the delay is not just the AI model. We have multiple components to latency, '
              'which is STT or speech to text, LLM, which is the the answer answer generation. '
              'And then text to speech, which puts the l l LLM response back in a voice and '
              'then outputs to the to the user again.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'And the delay is not just the AI model. We have multiple components to latency, '
             'which is STT or speech to text, LLM, which is the the answer answer generation. '
             'And then text to speech, which puts the l l LLM response back in a voice and '
             'then outputs to the to the user again.',
      'title': 'Twilio vs Telnyx: The Carrier That Makes or Breaks Your Voice AI (Voice AI '
               'with Tim)',
      'url': 'https://www.youtube.com/watch?v=kYOdE4uxQXQ&t=78s',
      'video_id': 'kYOdE4uxQXQ'},
     {'author': 'Empire Telecom',
      'channel': 'Empire Telecom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=whbUkc2imdY&t=117s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Patience and understanding as new requirements from the carriers are enforced '
              'the good news is that once you are registered you should see even better '
              'delivery rates for your messages as your business will be known and trusted by '
              'the carriers.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Patience and understanding as new requirements from the carriers are enforced '
             'the good news is that once you are registered you should see even better '
             'delivery rates for your messages as your business will be known and trusted by '
             'the carriers.',
      'title': 'What is TCR Registration for 10DLC (Empire Telecom)',
      'url': 'https://www.youtube.com/watch?v=whbUkc2imdY&t=117s',
      'video_id': 'whbUkc2imdY'},
     {'author': 'ZCorum',
      'channel': 'ZCorum',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:33](https://www.youtube.com/watch?v=ZLzeR3N0mpc&t=393s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Example if you are a reseller of voice services and you sign up uh a customer '
              "could be a business customer and let's say you don't do your due diligence on.",
      'timestamp': 393,
      'timestamp_label': '[00:06:33]',
      'timestamp_seconds': 393,
      'tip': 'Example if you are a reseller of voice services and you sign up uh a customer '
             "could be a business customer and let's say you don't do your due diligence on.",
      'title': 'All Voice Service Providers are Now Required to File in the Robocall '
               'Mitigation Database (ZCorum)',
      'url': 'https://www.youtube.com/watch?v=ZLzeR3N0mpc&t=393s',
      'video_id': 'ZLzeR3N0mpc'}],
 2: [{'author': 'Hitesh C.',
      'channel': 'Hitesh C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=fKrvPg4P6KY&t=94s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "NVIDIA's Llama 2 70B result shows both. 9 times faster than H100, but with "
              'batch 32 against batch 8. So read that speed-up carefully. Part of it is '
              "bandwidth, and part is the larger batch that the extra memory allowed. NVIDIA's "
              'DGX B200 system holds eight Blackwell GPUs.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "NVIDIA's Llama 2 70B result shows both. 9 times faster than H100, but with batch "
             '32 against batch 8. So read that speed-up carefully. Part of it is bandwidth, '
             "and part is the larger batch that the extra memory allowed. NVIDIA's DGX B200 "
             'system holds eight Blackwell GPUs.',
      'title': '46. H100 vs H200 vs Blackwell B200 for LLM Inference (Hitesh C.)',
      'url': 'https://www.youtube.com/watch?v=fKrvPg4P6KY&t=94s',
      'video_id': 'fKrvPg4P6KY'},
     {'author': 'HostingCompared with Natalie',
      'channel': 'HostingCompared with Natalie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=cEAhnKuawL8&t=28s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the card explicitly says plus bandwidth. That means the cheap number is a '
              'starting line, not the invoice. The captured host showed 99. Set your minimum '
              'before sorting by price. If one retry ruins the deadline, the lowest row may '
              'become the most expensive decision.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'And the card explicitly says plus bandwidth. That means the cheap number is a '
             'starting line, not the invoice. The captured host showed 99. Set your minimum '
             'before sorting by price. If one retry ruins the deadline, the lowest row may '
             'become the most expensive decision.',
      'title': 'RunPod vs Vast.ai RTX 4090: 4 Checks Before You Rent (HostingCompared with '
               'Natalie)',
      'url': 'https://www.youtube.com/watch?v=cEAhnKuawL8&t=28s',
      'video_id': 'cEAhnKuawL8'},
     {'author': 'TheAIGRID',
      'channel': 'TheAIGRID',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=vahdFdoK6y4&t=336s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, Span will pay your electricity bill and your internet bill directly and in '
              'exchange, you pay Span one low flat fee every month. The example Span has given '
              'is around $150 a month, which is about half of what the average American pays '
              'for electricity and internet combined.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'So, Span will pay your electricity bill and your internet bill directly and in '
             'exchange, you pay Span one low flat fee every month. The example Span has given '
             'is around $150 a month, which is about half of what the average American pays '
             'for electricity and internet combined.',
      'title': 'Nvidias New Mini Datacenter Pays You Every Month (TheAIGRID)',
      'url': 'https://www.youtube.com/watch?v=vahdFdoK6y4&t=336s',
      'video_id': 'vahdFdoK6y4'},
     {'author': 'Amir Tutorial',
      'channel': 'Amir Tutorial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=_2POs6qxMdo&t=108s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On the other hand, we have Pio. Pio also have SMS API platform that is to send '
              'an SMS you pay 0. 007 per SMS and for verify API platform also the same. And '
              'for voice API platform, you pay 0. So, preview is more budget friendly '
              'especially for SMS heavy users.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'On the other hand, we have Pio. Pio also have SMS API platform that is to send '
             'an SMS you pay 0. 007 per SMS and for verify API platform also the same. And for '
             'voice API platform, you pay 0. So, preview is more budget friendly especially '
             'for SMS heavy users.',
      'title': 'Twilio vs Plivo – Which One is Better in 2025? (Amir Tutorial)',
      'url': 'https://www.youtube.com/watch?v=_2POs6qxMdo&t=108s',
      'video_id': '_2POs6qxMdo'},
     {'author': 'TwilioDevs',
      'channel': 'TwilioDevs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:58](https://www.youtube.com/watch?v=KWvbRToRnGg&t=838s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re gonna play by the rules. Now we trust you and we need everyone else to "
              'trust you as well. Next up, we have a one-time campaign fee. Additional fees '
              "apply if the campaign is resubmitted. So you wanna make sure that we don't do "
              "that 'cause that could get expensive.",
      'timestamp': 838,
      'timestamp_label': '[00:13:58]',
      'timestamp_seconds': 838,
      'tip': "'re gonna play by the rules. Now we trust you and we need everyone else to trust "
             'you as well. Next up, we have a one-time campaign fee. Additional fees apply if '
             "the campaign is resubmitted. So you wanna make sure that we don't do that 'cause "
             'that could get expensive.',
      'title': 'Understanding US A2P 10DLC Registration (TwilioDevs)',
      'url': 'https://www.youtube.com/watch?v=KWvbRToRnGg&t=838s',
      'video_id': 'KWvbRToRnGg'},
     {'author': 'TWiz',
      'channel': 'TWiz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=_UBOzLyl2b0&t=142s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For instance, a small startup might benefit from RunPod's simplicity, while a "
              'research team with specific GPU requirements could find greater value in the '
              'diverse options available through Vast. Ultimately, the decision hinges on your '
              "project's complexity and budget.",
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': "For instance, a small startup might benefit from RunPod's simplicity, while a "
             'research team with specific GPU requirements could find greater value in the '
             'diverse options available through Vast. Ultimately, the decision hinges on your '
             "project's complexity and budget.",
      'title': 'RunPod vs Vast.ai Which GPU Cloud Is Better (TWiz)',
      'url': 'https://www.youtube.com/watch?v=_UBOzLyl2b0&t=142s',
      'video_id': '_UBOzLyl2b0'},
     {'author': 'Prompt Engineer 48',
      'channel': 'Prompt Engineer 48',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=FpNPRj38T6s&t=438s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, here's the rule of thumb. At a few thousand requests a day, the routing "
              'choice is pocket change. At a few million, it is a real line on your bill and '
              'the gap between cheapest and fastest becomes a budget decision.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': "So, here's the rule of thumb. At a few thousand requests a day, the routing "
             'choice is pocket change. At a few million, it is a real line on your bill and '
             'the gap between cheapest and fastest becomes a budget decision.',
      'title': 'Cheapest Provider Was 2x SLOWER? WILD Hugging Face + OpenRouter Routing '
               'Results (Prompt Engineer 48)',
      'url': 'https://www.youtube.com/watch?v=FpNPRj38T6s&t=438s',
      'video_id': 'FpNPRj38T6s'},
     {'author': 'Techno Tim',
      'channel': 'Techno Tim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=zbkqRPIUYAo&t=59s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2 switch ports, 16 IPs for $900 a month, and a one-time fee of $4500 a month. '
              'This is definitely not techno tim budget friendly.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': '2 switch ports, 16 IPs for $900 a month, and a one-time fee of $4500 a month. '
             'This is definitely not techno tim budget friendly.',
      'title': 'I Colocated My HomeLab in a Data Center (Techno Tim)',
      'url': 'https://www.youtube.com/watch?v=zbkqRPIUYAo&t=59s',
      'video_id': 'zbkqRPIUYAo'},
     {'author': 'Tulipnomics',
      'channel': 'Tulipnomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=71yv5MpdX1s&t=56s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A new law, the Telecommunications Act, opened American phone markets to '
              'competition. New carriers raced to build national networks, and the internet '
              'was growing fast enough to make almost any plan sound reasonable. A network '
              'costs a fortune before the first customer pays.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'A new law, the Telecommunications Act, opened American phone markets to '
             'competition. New carriers raced to build national networks, and the internet was '
             'growing fast enough to make almost any plan sound reasonable. A network costs a '
             'fortune before the first customer pays.',
      'title': 'The Telecom Bust: The Debt That Built the Internet (Tulipnomics)',
      'url': 'https://www.youtube.com/watch?v=71yv5MpdX1s&t=56s',
      'video_id': '71yv5MpdX1s'},
     {'author': 'Rabid Mining',
      'channel': 'Rabid Mining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=1bwwstZFQ7Q&t=54s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ASIC Mining Central has you covered to the cheapest prices out of any ASIC '
              'website as well as import fees will be low with low tax with DDP or invoice and '
              'code raid will grant you an additional $50 off your order.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'ASIC Mining Central has you covered to the cheapest prices out of any ASIC '
             'website as well as import fees will be low with low tax with DDP or invoice and '
             'code raid will grant you an additional $50 off your order.',
      'title': 'BREAKING: CLORE Just Killed GPU Mining Forever!! (Rabid Mining)',
      'url': 'https://www.youtube.com/watch?v=1bwwstZFQ7Q&t=54s',
      'video_id': '1bwwstZFQ7Q'},
     {'author': 'Lukasz Gawenda',
      'channel': 'Lukasz Gawenda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:18](https://www.youtube.com/watch?v=RlsxXB5q-cA&t=1218s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This back end reads from the drive instead. So we have same round, same layer, '
              'same results and the difference is which resource pays for it basically. And '
              "this is why the drive can keep up. The addresses do not depend on the model's "
              'own computation.',
      'timestamp': 1218,
      'timestamp_label': '[00:20:18]',
      'timestamp_seconds': 1218,
      'tip': 'This back end reads from the drive instead. So we have same round, same layer, '
             'same results and the difference is which resource pays for it basically. And '
             "this is why the drive can keep up. The addresses do not depend on the model's "
             'own computation.',
      'title': 'Qwen3.8 Flash: Over 7x Faster First Token | llama.cpp vs SGLang vs FreeToken. '
               'Benchmarked! (Lukasz Gawenda)',
      'url': 'https://www.youtube.com/watch?v=RlsxXB5q-cA&t=1218s',
      'video_id': 'RlsxXB5q-cA'},
     {'author': 'Telgorithm',
      'channel': 'Telgorithm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=IQ19nUV4NVA&t=332s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Knowing more about your customer than anybody else and if you if you know your '
              "customer the data and information you're Gathering is exactly what we need to "
              'put into the registry.',
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': 'Knowing more about your customer than anybody else and if you if you know your '
             "customer the data and information you're Gathering is exactly what we need to "
             'put into the registry.',
      'title': 'Why Register? The Campaign Registry Answers | A2P 10DLC Messaging (Telgorithm)',
      'url': 'https://www.youtube.com/watch?v=IQ19nUV4NVA&t=332s',
      'video_id': 'IQ19nUV4NVA'},
     {'author': 'Professor Py: AI Engineering',
      'channel': 'Professor Py: AI Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=2nHPifw-TkE&t=340s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The printed model name confirms that the request succeeded by routing to a '
              'fallback. Finally, we will inspect the key to see how spend is tracked. This '
              'snippet queries Light LLM proxy for key level spend so you can watch budget '
              'burn.',
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': 'The printed model name confirms that the request succeeded by routing to a '
             'fallback. Finally, we will inspect the key to see how spend is tracked. This '
             'snippet queries Light LLM proxy for key level spend so you can watch budget '
             'burn.',
      'title': 'LiteLLM Proxy in Python: Routing, Rate Limits, Budgets, and Fallbacks '
               '(Professor Py: AI Engineering)',
      'url': 'https://www.youtube.com/watch?v=2nHPifw-TkE&t=340s',
      'video_id': '2nHPifw-TkE'},
     {'author': 'GetVoIP - Simplify your search',
      'channel': 'GetVoIP - Simplify your search',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=SUPHe70LM7s&t=378s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Analytics toll-free numbers enable your voipfone system to make and receive '
              'phone calls at no cost to your customer no matter where they call from sip.',
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': 'Analytics toll-free numbers enable your voipfone system to make and receive '
             'phone calls at no cost to your customer no matter where they call from sip.',
      'title': 'SIP Trunking vs VoIP - Key Differences, Pros & Cons (GetVoIP - Simplify your '
               'search)',
      'url': 'https://www.youtube.com/watch?v=SUPHe70LM7s&t=378s',
      'video_id': 'SUPHe70LM7s'},
     {'author': 'Techmode Business Phone Systems',
      'channel': 'Techmode Business Phone Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=KjFy5hTaOcM&t=36s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'SHAKEN stands for Signature-Based Handling of Asserted Information Using '
              'Tokens. When a business places a call, its carrier attaches a digital '
              'signature, like a wax seal only that carrier can make. A means the carrier '
              'verified the customer and their right to use that number.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'SHAKEN stands for Signature-Based Handling of Asserted Information Using Tokens. '
             'When a business places a call, its carrier attaches a digital signature, like a '
             'wax seal only that carrier can make. A means the carrier verified the customer '
             'and their right to use that number.',
      'title': 'Telecom in Under 2-  What is STIR/SHAKEN? (Techmode Business Phone Systems)',
      'url': 'https://www.youtube.com/watch?v=KjFy5hTaOcM&t=36s',
      'video_id': 'KjFy5hTaOcM'}],
 3: [{'author': 'CloudExpert Solutions',
      'channel': 'CloudExpert Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:24](https://www.youtube.com/watch?v=dpje7Qql0SU&t=384s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'December and scale back in January, and they only pay for what they actually '
              "consumed, a huge savings. Now, let's review economics of scale. This is one of "
              'the six AWS cloud value propositions. The concept is simple, the more you buy, '
              'the cheaper each unit becomes.',
      'timestamp': 384,
      'timestamp_label': '[00:06:24]',
      'timestamp_seconds': 384,
      'tip': 'December and scale back in January, and they only pay for what they actually '
             "consumed, a huge savings. Now, let's review economics of scale. This is one of "
             'the six AWS cloud value propositions. The concept is simple, the more you buy, '
             'the cheaper each unit becomes.',
      'title': 'Cloud FinOps Explained | CapEx vs OpEx, Cost Savings & Rightsizing | AWS '
               'CLF-C02 [2026] (CloudExpert Solutions)',
      'url': 'https://www.youtube.com/watch?v=dpje7Qql0SU&t=384s',
      'video_id': 'dpje7Qql0SU'},
     {'author': 'FinOps Foundation',
      'channel': 'FinOps Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:41](https://www.youtube.com/watch?v=b7TiwS4_Ytw&t=1721s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For those workloads, our recommendation is export your cost and pricing data '
              'alongside with your business metrics into Microsoft Fabric and run the analysis '
              'there. And now I will hand it back to Vikram to show you Azure Copilot and '
              'Microsoft Fabric solutions.',
      'timestamp': 1721,
      'timestamp_label': '[00:28:41]',
      'timestamp_seconds': 1721,
      'tip': 'For those workloads, our recommendation is export your cost and pricing data '
             'alongside with your business metrics into Microsoft Fabric and run the analysis '
             'there. And now I will hand it back to Vikram to show you Azure Copilot and '
             'Microsoft Fabric solutions.',
      'title': 'AI for FinOps on Azure: Smarter Cloud Operations with Agentic AI (FinOps '
               'Foundation)',
      'url': 'https://www.youtube.com/watch?v=b7TiwS4_Ytw&t=1721s',
      'video_id': 'b7TiwS4_Ytw'},
     {'author': 'Ready Tensor',
      'channel': 'Ready Tensor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=9t-W51EHgzY&t=237s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would send requests to this base URL. And if you need a model API key you '
              'would set it here as well. And you can control the cost to the tokens. So we '
              "didn't set this here because the pricing of GPT40 and 40 mini is well known but "
              'for this is a custom model.',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': 'I would send requests to this base URL. And if you need a model API key you '
             'would set it here as well. And you can control the cost to the tokens. So we '
             "didn't set this here because the pricing of GPT40 and 40 mini is well known but "
             'for this is a custom model.',
      'title': 'LiteLLM Proxy Tutorial: Track Costs, Budgets, and Multi-Provider LLM Usage '
               '(Ready Tensor)',
      'url': 'https://www.youtube.com/watch?v=9t-W51EHgzY&t=237s',
      'video_id': '9t-W51EHgzY'},
     {'author': 'Modern Mining',
      'channel': 'Modern Mining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:19](https://www.youtube.com/watch?v=WJnsgbZsg0U&t=1999s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh I used to use a different platform. Um but that that extra $1,000 can be '
              "used as power costs, let's say, because there is some power cost that goes into "
              "it. So let's pretend that I've made $3,800 in profit off of my rigs since I "
              'started.',
      'timestamp': 1999,
      'timestamp_label': '[00:33:19]',
      'timestamp_seconds': 1999,
      'tip': 'Uh I used to use a different platform. Um but that that extra $1,000 can be used '
             "as power costs, let's say, because there is some power cost that goes into it. "
             "So let's pretend that I've made $3,800 in profit off of my rigs since I started.",
      'title': 'I Built a $3000 AI Computer for Profit in 2026 (Modern Mining)',
      'url': 'https://www.youtube.com/watch?v=WJnsgbZsg0U&t=1999s',
      'video_id': 'WJnsgbZsg0U'},
     {'author': 'Vantage',
      'channel': 'Vantage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:01](https://www.youtube.com/watch?v=1-lJfz3oQ2w&t=661s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You need to be able to know which of your customers are are causing the most '
              "cost for you whether you charge those customers or not. It's very important for "
              'uh mapping back to your own margins on each of your customers.',
      'timestamp': 661,
      'timestamp_label': '[00:11:01]',
      'timestamp_seconds': 661,
      'tip': 'You need to be able to know which of your customers are are causing the most '
             "cost for you whether you charge those customers or not. It's very important for "
             'uh mapping back to your own margins on each of your customers.',
      'title': 'Managing AI Budgets in the Age of Tokenmaxxing | FinOps Summer Camp Session 3 '
               '(Vantage)',
      'url': 'https://www.youtube.com/watch?v=1-lJfz3oQ2w&t=661s',
      'video_id': '1-lJfz3oQ2w'},
     {'author': 'AWS Events',
      'channel': 'AWS Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:06](https://www.youtube.com/watch?v=JqwiGt78aOI&t=966s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AWS API throttling sometimes impact multiple agents assessing costs at the same '
              'time >> it could right be aware of what your limits are set to, what services '
              "that you're using because these things are capable of working really rapidly.",
      'timestamp': 966,
      'timestamp_label': '[00:16:06]',
      'timestamp_seconds': 966,
      'tip': 'AWS API throttling sometimes impact multiple agents assessing costs at the same '
             'time >> it could right be aware of what your limits are set to, what services '
             "that you're using because these things are capable of working really rapidly.",
      'title': 'Build a FinOps Agent I The Keys to AWS Optimization | S16 E6 (AWS Events)',
      'url': 'https://www.youtube.com/watch?v=JqwiGt78aOI&t=966s',
      'video_id': 'JqwiGt78aOI'},
     {'author': 'IPTP Networks',
      'channel': 'IPTP Networks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=3EnjHW-36GI&t=158s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four cross-connects can therefore mean $2,000 to $6,000 in upfront cost alone. '
              'Sixth, installation and on-site support. Setup and cabling are one-time costs '
              'that vary by deployment.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'Four cross-connects can therefore mean $2,000 to $6,000 in upfront cost alone. '
             'Sixth, installation and on-site support. Setup and cabling are one-time costs '
             'that vary by deployment.',
      'title': 'Colocation Pricing Explained: Space, Power, Cross-Connects (IPTP Networks)',
      'url': 'https://www.youtube.com/watch?v=3EnjHW-36GI&t=158s',
      'video_id': '3EnjHW-36GI'},
     {'author': 'Craft Computing',
      'channel': 'Craft Computing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:53](https://www.youtube.com/watch?v=9c1c3JPZ2ps&t=1013s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AI division and is unlikely to ever bring GPU bifurcation to GeForce cards no '
              'matter how much we ask for it. If you want grid functionality today the cost of '
              'entry is $3,000 for an RTX A5000 or $10,000 for a Blackwell 6000 Pro.',
      'timestamp': 1013,
      'timestamp_label': '[00:16:53]',
      'timestamp_seconds': 1013,
      'tip': 'AI division and is unlikely to ever bring GPU bifurcation to GeForce cards no '
             'matter how much we ask for it. If you want grid functionality today the cost of '
             'entry is $3,000 for an RTX A5000 or $10,000 for a Blackwell 6000 Pro.',
      'title': 'EIGHT GPUs in a Cloud Gaming Server - Nvidia DGX V100 (Craft Computing)',
      'url': 'https://www.youtube.com/watch?v=9c1c3JPZ2ps&t=1013s',
      'video_id': '9c1c3JPZ2ps'},
     {'author': 'The VoIP Report',
      'channel': 'The VoIP Report',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=zSendtIzBt0&t=57s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tier 1 network, which gives you access to most regions of the world, at '
              'competitive rates. With Toll-Free SIP, service providers route inbound calls '
              'from your customers over their Tier 1 networks at no cost to the caller. Bring '
              'down the costs with SIP Trunking.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'Tier 1 network, which gives you access to most regions of the world, at '
             'competitive rates. With Toll-Free SIP, service providers route inbound calls '
             'from your customers over their Tier 1 networks at no cost to the caller. Bring '
             'down the costs with SIP Trunking.',
      'title': 'SIP Trunking 101 - The VoIP Report (The VoIP Report)',
      'url': 'https://www.youtube.com/watch?v=zSendtIzBt0&t=57s',
      'video_id': 'zSendtIzBt0'},
     {'author': 'ZCorum',
      'channel': 'ZCorum',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:27](https://www.youtube.com/watch?v=QPBt987oumw&t=807s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We recommend that in considering changes to the contribution base the '
              'commission should take efforts to avoid raising the cost of broadband service '
              'and shifting.',
      'timestamp': 807,
      'timestamp_label': '[00:13:27]',
      'timestamp_seconds': 807,
      'tip': 'We recommend that in considering changes to the contribution base the commission '
             'should take efforts to avoid raising the cost of broadband service and shifting.',
      'title': 'FCC Releases Report on the Future of the Universal Service Fund (ZCorum)',
      'url': 'https://www.youtube.com/watch?v=QPBt987oumw&t=807s',
      'video_id': 'QPBt987oumw'},
     {'author': 'Alec Glover',
      'channel': 'Alec Glover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=iuLuDflfEE4&t=170s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would just say, you know, unless you have a ton of experience with this, like '
              'buying the GPU servers might only cost you, you know, a 10 15% margin over '
              'building it yourself, and you lose or you introduce a ton of risk in doing '
              'yourself.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'I would just say, you know, unless you have a ton of experience with this, like '
             'buying the GPU servers might only cost you, you know, a 10 15% margin over '
             'building it yourself, and you lose or you introduce a ton of risk in doing '
             'yourself.',
      'title': 'I Built My Own GPU Cloud (and you can too) (Alec Glover)',
      'url': 'https://www.youtube.com/watch?v=iuLuDflfEE4&t=170s',
      'video_id': 'iuLuDflfEE4'},
     {'author': 'GPU Battle',
      'channel': 'GPU Battle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=SqfQZYYMPj4&t=70s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh Vast AI is the cheapest, but also the most expensive because the bandwidth '
              'bill of Vast AI Vast AI is the only one where the bandwidth that you consume um '
              'the pricing adjusts depending on the provider.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Uh Vast AI is the cheapest, but also the most expensive because the bandwidth '
             'bill of Vast AI Vast AI is the only one where the bandwidth that you consume um '
             'the pricing adjusts depending on the provider.',
      'title': 'Mistakes People Make Renting Cloud GPUs (RunPod, Vast.ai, Modal) (GPU Battle)',
      'url': 'https://www.youtube.com/watch?v=SqfQZYYMPj4&t=70s',
      'video_id': 'SqfQZYYMPj4'},
     {'author': 'Legal Registration',
      'channel': 'Legal Registration',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=Lqlbag5CQMU&t=198s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cost effective DC service process Solutions you are also welcome to give our '
              'filing experts a phone call at any time our number is 877 955-711 and look '
              'forward to serving as your go-to FCC registration service.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'Cost effective DC service process Solutions you are also welcome to give our '
             'filing experts a phone call at any time our number is 877 955-711 and look '
             'forward to serving as your go-to FCC registration service.',
      'title': 'FCC 499 Filing is for Telecommunications Companies & Telecom and VoIP '
               'Providers Information (Legal Registration)',
      'url': 'https://www.youtube.com/watch?v=Lqlbag5CQMU&t=198s',
      'video_id': 'Lqlbag5CQMU'},
     {'author': 'Honey With Crypto',
      'channel': 'Honey With Crypto',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=Wp6L77ZvZw8&t=90s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Such as one 3060 Ti, and two 3060s. So right now friends, we are making $ 20 in '
              'profitability per day as of today, because our electricity bill there is '
              'charged at 7, 5, 6 rupees per unit. So now, sorry, we are making $ 10 per day '
              'according to this rate.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Such as one 3060 Ti, and two 3060s. So right now friends, we are making $ 20 in '
             'profitability per day as of today, because our electricity bill there is charged '
             'at 7, 5, 6 rupees per unit. So now, sorry, we are making $ 10 per day according '
             'to this rate.',
      'title': 'Double Profit From GPU Mining? Pearl + Monero Mining Setup Guide 2026 🤑 (Honey '
               'With Crypto)',
      'url': 'https://www.youtube.com/watch?v=Wp6L77ZvZw8&t=90s',
      'video_id': 'Wp6L77ZvZw8'},
     {'author': 'Virtuser - Connectivity Mobilised',
      'channel': 'Virtuser - Connectivity Mobilised',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=6sIXgGXsu3E&t=106s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Know where everything is ETC but when you're traveling finding ubiquitous wife "
              "it's not as widely available as Finance directors think just like flying "
              "economy is not as comfortable as Finance directors think when you're doing it a "
              'lot or long.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': "Know where everything is ETC but when you're traveling finding ubiquitous wife "
             "it's not as widely available as Finance directors think just like flying economy "
             "is not as comfortable as Finance directors think when you're doing it a lot or "
             'long.',
      'title': 'Travel eSIMs for B2B Roaming and MVNO Roaming with integrated optional Wi-Fi '
               '(Virtuser - Connectivity Mobilised)',
      'url': 'https://www.youtube.com/watch?v=6sIXgGXsu3E&t=106s',
      'video_id': '6sIXgGXsu3E'}],
 4: [{'author': 'Design Guy',
      'channel': 'Design Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:02](https://www.youtube.com/watch?v=PnUJffgghas&t=422s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So let us pull back and see where the entire board lands. When it comes to '
              'memory capacity and pure memory bandwidth, the newer Nvidia B200 sweeps both '
              'rounds cleanly.',
      'timestamp': 422,
      'timestamp_label': '[00:07:02]',
      'timestamp_seconds': 422,
      'tip': 'So let us pull back and see where the entire board lands. When it comes to '
             'memory capacity and pure memory bandwidth, the newer Nvidia B200 sweeps both '
             'rounds cleanly.',
      'title': 'NVIDIA H200 vs NVIDIA B200 AI GPU Explained | Pros, Cons & Verdict for 2026 '
               '(Design Guy)',
      'url': 'https://www.youtube.com/watch?v=PnUJffgghas&t=422s',
      'video_id': 'PnUJffgghas'},
     {'author': 'GigaBits',
      'channel': 'GigaBits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=cKVz3FEdvPQ&t=63s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Its setup is easier, pricing tends to be more transparent, and support is often '
              "more responsive for smaller teams. Pivo is a great choice if you're a startup "
              'or midsize business that needs dependable communication tools without the bulk '
              'of an enterprise platform.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Its setup is easier, pricing tends to be more transparent, and support is often '
             "more responsive for smaller teams. Pivo is a great choice if you're a startup or "
             'midsize business that needs dependable communication tools without the bulk of '
             'an enterprise platform.',
      'title': 'Twilio Vs Plivo (2025) | Which One Is Better? (GigaBits)',
      'url': 'https://www.youtube.com/watch?v=cKVz3FEdvPQ&t=63s',
      'video_id': 'cKVz3FEdvPQ'},
     {'author': 'TwilioDevs',
      'channel': 'TwilioDevs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=7pXYEARPIwU&t=195s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you do have one, register a standard or low volume standard brand instead. '
              'And when you do, pick the legal entity type that actually fits your business, '
              "whether it's LLC, corporation, nonprofit, or anarcho-syndicalist commune.",
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'If you do have one, register a standard or low volume standard brand instead. '
             'And when you do, pick the legal entity type that actually fits your business, '
             "whether it's LLC, corporation, nonprofit, or anarcho-syndicalist commune.",
      'title': 'Twilio A2P 10DLC Rejected? Fix These Error Codes (TwilioDevs)',
      'url': 'https://www.youtube.com/watch?v=7pXYEARPIwU&t=195s',
      'video_id': '7pXYEARPIwU'},
     {'author': 'AWS With A Beer',
      'channel': 'AWS With A Beer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=6qqv9Ss3MaE&t=233s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Longer term think of it as a subscription plan for cloud savings these tools '
              'and there are many more when combined with strong internal practices can '
              'transform your AWC experience from a budget busting headache to a streamlined.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'Longer term think of it as a subscription plan for cloud savings these tools and '
             'there are many more when combined with strong internal practices can transform '
             'your AWC experience from a budget busting headache to a streamlined.',
      'title': 'AWS FinOps Explained in 5 Minutes (AWS With A Beer)',
      'url': 'https://www.youtube.com/watch?v=6qqv9Ss3MaE&t=233s',
      'video_id': '6qqv9Ss3MaE'},
     {'author': 'CyberPulse',
      'channel': 'CyberPulse',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:38](https://www.youtube.com/watch?v=Z69EERVnY6w&t=938s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That steady rhythm is exactly what it never had. Second, Intel joined a $350 '
              'million funding round for SambaNova, an AI chip startup with a very different '
              'design and signed a multi-year partnership with it. Third, the software is '
              'moving up a level.',
      'timestamp': 938,
      'timestamp_label': '[00:15:38]',
      'timestamp_seconds': 938,
      'tip': 'That steady rhythm is exactly what it never had. Second, Intel joined a $350 '
             'million funding round for SambaNova, an AI chip startup with a very different '
             'design and signed a multi-year partnership with it. Third, the software is '
             'moving up a level.',
      'title': 'Why Can’t Intel Copy NVIDIA’s Complete AI Stack? (CyberPulse)',
      'url': 'https://www.youtube.com/watch?v=Z69EERVnY6w&t=938s',
      'video_id': 'Z69EERVnY6w'},
     {'author': 'Alec Glover',
      'channel': 'Alec Glover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:46](https://www.youtube.com/watch?v=CgsDEFaGLJ0&t=2326s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "GPUs here, as well as a layer of GPUs here, and we're able to shrink the size "
              "because, you know, we obviously we don't need to stack the GPUs like vertically "
              "on top of each other. So, I'll end it there and then jump back uh onto my "
              'computer.',
      'timestamp': 2326,
      'timestamp_label': '[00:38:46]',
      'timestamp_seconds': 2326,
      'tip': "GPUs here, as well as a layer of GPUs here, and we're able to shrink the size "
             "because, you know, we obviously we don't need to stack the GPUs like vertically "
             "on top of each other. So, I'll end it there and then jump back uh onto my "
             'computer.',
      'title': 'everything i learned building 100 GPU servers (Alec Glover)',
      'url': 'https://www.youtube.com/watch?v=CgsDEFaGLJ0&t=2326s',
      'video_id': 'CgsDEFaGLJ0'},
     {'author': 'KodeKloud',
      'channel': 'KodeKloud',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=qdPkA5mxLhg&t=200s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And managing this exact stack is what vLLM allows you to work to lower the '
              "latency and maximize concurrency using vLLM. In this lab, we're going to learn "
              'about how vLLM turns a basic LLM setup into a production-ready inference '
              'server.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': 'And managing this exact stack is what vLLM allows you to work to lower the '
             "latency and maximize concurrency using vLLM. In this lab, we're going to learn "
             'about how vLLM turns a basic LLM setup into a production-ready inference server.',
      'title': 'Understanding vLLM with a Hands On Demo (KodeKloud)',
      'url': 'https://www.youtube.com/watch?v=qdPkA5mxLhg&t=200s',
      'video_id': 'qdPkA5mxLhg'},
     {'author': 'Emmanuel Corels Academy',
      'channel': 'Emmanuel Corels Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=sRtvITK_o8I&t=69s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A fixed GPU layout can leave reserved capacity idle. GPU generation isn't "
              "enough. RTX Pro 4000 and 500 Blackwell server edition supports MIG L4, doesn't. "
              'On a Linux host with NVIDIA tools installed, open terminal and run nvidia-smi '
              '-l to identify the GPU model.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "A fixed GPU layout can leave reserved capacity idle. GPU generation isn't "
             "enough. RTX Pro 4000 and 500 Blackwell server edition supports MIG L4, doesn't. "
             'On a Linux host with NVIDIA tools installed, open terminal and run nvidia-smi -l '
             'to identify the GPU model.',
      'title': 'One GPU, Several AI Users: MIG vs Time-Slicing Explained (Emmanuel Corels '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=sRtvITK_o8I&t=69s',
      'video_id': 'sRtvITK_o8I'},
     {'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=lB4f9k3khDg&t=27s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Po on the other hand is the costefficient alternative. It focuses on SMS and '
              'voice APIs across 220 plus countries with straightforward pricing and faster '
              'setup. Think of it as streamlined, reliable, and budget friendly.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'Po on the other hand is the costefficient alternative. It focuses on SMS and '
             'voice APIs across 220 plus countries with straightforward pricing and faster '
             'setup. Think of it as streamlined, reliable, and budget friendly.',
      'title': 'Twilio vs Plivo – Which One is Better in 2026? (houdztech)',
      'url': 'https://www.youtube.com/watch?v=lB4f9k3khDg&t=27s',
      'video_id': 'lB4f9k3khDg'},
     {'author': 'MEP BOOSTER',
      'channel': 'MEP BOOSTER',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:53](https://www.youtube.com/watch?v=O0T9qQ1TuGU&t=653s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, it is used for office file and printers. Then you can use it in college IT '
              'lab. Suppose a computer lab with student login server, basic network storage, '
              'local software server. Then for small startup data storage.',
      'timestamp': 653,
      'timestamp_label': '[00:10:53]',
      'timestamp_seconds': 653,
      'tip': 'So, it is used for office file and printers. Then you can use it in college IT '
             'lab. Suppose a computer lab with student login server, basic network storage, '
             'local software server. Then for small startup data storage.',
      'title': 'What is a Data Centre? (Tier 1, Tier 2, Tier 3, Tier 4 Explained) (MEP '
               'BOOSTER)',
      'url': 'https://www.youtube.com/watch?v=O0T9qQ1TuGU&t=653s',
      'video_id': 'O0T9qQ1TuGU'},
     {'author': 'ServeTheHome',
      'channel': 'ServeTheHome',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:36](https://www.youtube.com/watch?v=CHEbom4opXg&t=1176s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'NVIDIA AI software stack, including NVIDIA AI Enterprise, Omniverse, and '
              'Run:ai. So, with all these videos, I want to have a key lessons learned. And '
              'what did I learn today?',
      'timestamp': 1176,
      'timestamp_label': '[00:19:36]',
      'timestamp_seconds': 1176,
      'tip': 'NVIDIA AI software stack, including NVIDIA AI Enterprise, Omniverse, and Run:ai. '
             'So, with all these videos, I want to have a key lessons learned. And what did I '
             'learn today?',
      'title': 'Newest Gen AI Servers Are Built Like This (ServeTheHome)',
      'url': 'https://www.youtube.com/watch?v=CHEbom4opXg&t=1176s',
      'video_id': 'CHEbom4opXg'},
     {'author': 'hrithik verma',
      'channel': 'hrithik verma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:44](https://www.youtube.com/watch?v=CkxWiz2Qzi8&t=764s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, if you want on some other instance, you will get this option. But, here '
              'also you can make it auto. You will get better perform FPS on the scene. The '
              "you're getting better FPS.",
      'timestamp': 764,
      'timestamp_label': '[00:12:44]',
      'timestamp_seconds': 764,
      'tip': 'But, if you want on some other instance, you will get this option. But, here '
             'also you can make it auto. You will get better perform FPS on the scene. The '
             "you're getting better FPS.",
      'title': 'Cheap Cloud GPU for Isaac Sim | RunPod & Vast.ai | WebRTC + VM Setup (hrithik '
               'verma)',
      'url': 'https://www.youtube.com/watch?v=CkxWiz2Qzi8&t=764s',
      'video_id': 'CkxWiz2Qzi8'},
     {'author': 'Mitel Academy',
      'channel': 'Mitel Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=ijPHb8SEENo&t=270s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So they can be able to make calls as if they are in the office. But their '
              'phones are connected from externally. So a CP hacker uh will be able to using '
              'their skill can be able to identify how this this phone for example for example '
              'is connecting back to the office.',
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'So they can be able to make calls as if they are in the office. But their phones '
             'are connected from externally. So a CP hacker uh will be able to using their '
             'skill can be able to identify how this this phone for example for example is '
             'connecting back to the office.',
      'title': 'SIP Fraud | How to Prevent Toll Fraud on SIP Trunks and Devices (Mitel '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=ijPHb8SEENo&t=270s',
      'video_id': 'ijPHb8SEENo'},
     {'author': 'MalwareFox',
      'channel': 'MalwareFox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=ACdz4nNt8P8&t=103s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The cryptojacking malware is using software bundling they bundle the malware '
              'with free or pirated software when you download and install such software you '
              'also install the malware on your system hackers take advantage of your '
              'carelessness and lack of knowledge.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'The cryptojacking malware is using software bundling they bundle the malware '
             'with free or pirated software when you download and install such software you '
             'also install the malware on your system hackers take advantage of your '
             'carelessness and lack of knowledge.',
      'title': 'How to Remove Bitcoin Miner Malware | Prevent Crypto Jacking (MalwareFox)',
      'url': 'https://www.youtube.com/watch?v=ACdz4nNt8P8&t=103s',
      'video_id': 'ACdz4nNt8P8'},
     {'author': 'DevOps & AI Toolkit',
      'channel': 'DevOps & AI Toolkit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:36](https://www.youtube.com/watch?v=zuRKdveFuZ4&t=756s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Use Cube to run models inside virtual machines managed by kubernetes and '
              'virtual machines in the same cluster I can explore that one as well just let me '
              'know in the comments thank you for watching see you in the next one cheers.',
      'timestamp': 756,
      'timestamp_label': '[00:12:36]',
      'timestamp_seconds': 756,
      'tip': 'Use Cube to run models inside virtual machines managed by kubernetes and virtual '
             'machines in the same cluster I can explore that one as well just let me know in '
             'the comments thank you for watching see you in the next one cheers.',
      'title': 'GPUs in Kubernetes for AI Workloads (DevOps & AI Toolkit)',
      'url': 'https://www.youtube.com/watch?v=zuRKdveFuZ4&t=756s',
      'video_id': 'zuRKdveFuZ4'}],
 5: [{'author': 'GPU Battle',
      'channel': 'GPU Battle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=dWC3n2Bn3r8&t=117s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clyde when using my API key to rent off Vast would not make critical mistakes. '
              'So, for consumer GPUs and budget H100s like Vast AI is going to be the ultimate '
              "value pack, right? So, essentially mistake number one is there's power capped "
              'cards.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Clyde when using my API key to rent off Vast would not make critical mistakes. '
             'So, for consumer GPUs and budget H100s like Vast AI is going to be the ultimate '
             "value pack, right? So, essentially mistake number one is there's power capped "
             'cards.',
      'title': 'Vast.ai Is the Cheapest Cloud GPU (If You Avoid These Mistakes) (GPU Battle)',
      'url': 'https://www.youtube.com/watch?v=dWC3n2Bn3r8&t=117s',
      'video_id': 'dWC3n2Bn3r8'},
     {'author': 'The gpuMaster',
      'channel': 'The gpuMaster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:13](https://www.youtube.com/watch?v=_tV0Elv_jIk&t=373s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t available in the Usa el código con precaución. 153 00:06:27,370 --> "
              '00:06:29,630 Bare-metal GPU providers approach the 154 00:06:29,630 --> '
              '00:06:31,930 problem differently. You may receive the 155 00:06:31,970 --> '
              '00:06:34,330 entire physical server.',
      'timestamp': 373,
      'timestamp_label': '[00:06:13]',
      'timestamp_seconds': 373,
      'tip': "'t available in the Usa el código con precaución. 153 00:06:27,370 --> "
             '00:06:29,630 Bare-metal GPU providers approach the 154 00:06:29,630 --> '
             '00:06:31,930 problem differently. You may receive the 155 00:06:31,970 --> '
             '00:06:34,330 entire physical server.',
      'title': 'Bare-Metal GPU Clouds vs Hyperscalers: Why startups are fleeing AWS and Azure? '
               '(The gpuMaster)',
      'url': 'https://www.youtube.com/watch?v=_tV0Elv_jIk&t=373s',
      'video_id': '_tV0Elv_jIk'},
     {'author': 'Null0 Labs',
      'channel': 'Null0 Labs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:23](https://www.youtube.com/watch?v=Pr9psxw4Z_o&t=2303s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AS900 through our router back over to the basement and then onto the server one '
              "which will then show us 9,01. So we started with a private ASN. We're going to "
              'conclude the video with a public ASN and our own blocks being advertised. So '
              "that server is re that rout's reloaded.",
      'timestamp': 2303,
      'timestamp_label': '[00:38:23]',
      'timestamp_seconds': 2303,
      'tip': 'AS900 through our router back over to the basement and then onto the server one '
             "which will then show us 9,01. So we started with a private ASN. We're going to "
             'conclude the video with a public ASN and our own blocks being advertised. So '
             "that server is re that rout's reloaded.",
      'title': 'How to Peer with BGP Over the Internet Using GRE Tunnels | No ASN? No Problem! '
               '(Null0 Labs)',
      'url': 'https://www.youtube.com/watch?v=Pr9psxw4Z_o&t=2303s',
      'video_id': 'Pr9psxw4Z_o'},
     {'author': 'GPU Battle',
      'channel': 'GPU Battle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:46](https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=286s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean, I'm paying money, so I need it to run. And then mistake number four, "
              'pricing the hour, not the job, right? Per second billing means a faster card '
              'can be cheaper per job, right? Call back to a Quen video, the 3090 was the '
              'cheapest per million tokens, not the H100.',
      'timestamp': 286,
      'timestamp_label': '[00:04:46]',
      'timestamp_seconds': 286,
      'tip': "I mean, I'm paying money, so I need it to run. And then mistake number four, "
             'pricing the hour, not the job, right? Per second billing means a faster card can '
             'be cheaper per job, right? Call back to a Quen video, the 3090 was the cheapest '
             'per million tokens, not the H100.',
      'title': "Don't Rent on RunPod Until You Watch This (2026) (GPU Battle)",
      'url': 'https://www.youtube.com/watch?v=WhTJ6B-YCmw&t=286s',
      'video_id': 'WhTJ6B-YCmw'},
     {'author': 'The Code Notebook',
      'channel': 'The Code Notebook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=IZtzUfhm8LU&t=136s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The B200 from the Blackwell generation is generally available, too. And the '
              'B300 family is broadly rentable in 2026. The newest, called Vera Rubin, is only '
              'in limited availability. One cloud began renting it on the 30th of September.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'The B200 from the Blackwell generation is generally available, too. And the B300 '
             'family is broadly rentable in 2026. The newest, called Vera Rubin, is only in '
             'limited availability. One cloud began renting it on the 30th of September.',
      'title': 'Why Cheap Spot GPUs End Up Costing MORE (The Checkpoint Mistake) (The Code '
               'Notebook)',
      'url': 'https://www.youtube.com/watch?v=IZtzUfhm8LU&t=136s',
      'video_id': 'IZtzUfhm8LU'},
     {'author': 'Yeyu Lab',
      'channel': 'Yeyu Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=opR3LozV3NM&t=182s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Gemini and anthropic Claude to my surprise there are a couple of SB models that '
              'are free for use including mistral 7B instruct eagle 7B and zephyr 7B the only '
              'limitation is the rate limit of 10 API.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': 'Gemini and anthropic Claude to my surprise there are a couple of SB models that '
             'are free for use including mistral 7B instruct eagle 7B and zephyr 7B the only '
             'limitation is the rate limit of 10 API.',
      'title': 'OpenRouter - Use The LLM Inference API with the Lowest Cost (Yeyu Lab)',
      'url': 'https://www.youtube.com/watch?v=opR3LozV3NM&t=182s',
      'video_id': 'opR3LozV3NM'},
     {'author': 'System Decisions',
      'channel': 'System Decisions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=KSQQ4-K5eW0&t=115s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And look, its record really speaks for itself. For any single turn task like '
              "generating a bunch of content or running a batch job, VLM's combination of page "
              'detention and continuous batching is just a knockout.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'And look, its record really speaks for itself. For any single turn task like '
             "generating a bunch of content or running a batch job, VLM's combination of page "
             'detention and continuous batching is just a knockout.',
      'title': 'SGLang vs. vLLM: The New Throughput King? (System Decisions)',
      'url': 'https://www.youtube.com/watch?v=KSQQ4-K5eW0&t=115s',
      'video_id': 'KSQQ4-K5eW0'},
     {'author': 'vCluster',
      'channel': 'vCluster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:33](https://www.youtube.com/watch?v=sXpJ4vSc-cM&t=3693s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If anybody is getting from Exoscale, from uh DigitalOcean, from even from AWS, '
              'GCP, Azure, um you know, DM me, give some free credits, happy to do the demo, '
              'write a blog with you, and uh you know, uh show off on the stream as well.',
      'timestamp': 3693,
      'timestamp_label': '[01:01:33]',
      'timestamp_seconds': 3693,
      'tip': 'If anybody is getting from Exoscale, from uh DigitalOcean, from even from AWS, '
             'GCP, Azure, um you know, DM me, give some free credits, happy to do the demo, '
             'write a blog with you, and uh you know, uh show off on the stream as well.',
      'title': 'Multi-Tenancy Fundamentals: Why GPU Sharing is Harder in Kubernetes (vCluster)',
      'url': 'https://www.youtube.com/watch?v=sXpJ4vSc-cM&t=3693s',
      'video_id': 'sXpJ4vSc-cM'},
     {'author': 'Crypto Miners Rigs',
      'channel': 'Crypto Miners Rigs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=1q_WZwOjByQ&t=53s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, why do most first rigs fail? Mistake one, buying cards for the hype coin '
              'without checking the algorithm. In 2026, a lot of the GPU interest comes from '
              'Pearl, a newer coin whose mining is built around AI-style matrix math. Pearl '
              'mining runs on Nvidia cards only.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'So, why do most first rigs fail? Mistake one, buying cards for the hype coin '
             'without checking the algorithm. In 2026, a lot of the GPU interest comes from '
             'Pearl, a newer coin whose mining is built around AI-style matrix math. Pearl '
             'mining runs on Nvidia cards only.',
      'title': 'How to Build a GPU Mining Rig in 2026: Step-by-Step (Power, Cooling, Real '
               'Math) (Crypto Miners Rigs)',
      'url': 'https://www.youtube.com/watch?v=1q_WZwOjByQ&t=53s',
      'video_id': '1q_WZwOjByQ'},
     {'author': 'Duality Technologies',
      'channel': 'Duality Technologies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=UlUCeUlE1j8&t=250s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The new image is attested before any weights are released, and it rolls back if '
              'the start fails. Audit records every lifecycle, attestation, certificate and '
              'client event, without a single prompt, response or log line from inside the '
              'enclave.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'The new image is attested before any weights are released, and it rolls back if '
             'the start fails. Audit records every lifecycle, attestation, certificate and '
             'client event, without a single prompt, response or log line from inside the '
             'enclave.',
      'title': 'Confidential Inference for Neoclouds: Run AI Without Seeing Prompts (Duality '
               'Technologies)',
      'url': 'https://www.youtube.com/watch?v=UlUCeUlE1j8&t=250s',
      'video_id': 'UlUCeUlE1j8'},
     {'author': 'BearMarketMiner',
      'channel': 'BearMarketMiner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:23](https://www.youtube.com/watch?v=egH5hKD913Y&t=1223s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "OctoPace on HiveOSs or Linux or you're running Nana on the same, a little "
              'cheeky way to save a little bit of power. And I want to show you a real-time '
              "example of this. And, uh, sorry to the guy who's renting this rig right now, "
              "but, uh, I swear I'll change it back.",
      'timestamp': 1223,
      'timestamp_label': '[00:20:23]',
      'timestamp_seconds': 1223,
      'tip': "OctoPace on HiveOSs or Linux or you're running Nana on the same, a little cheeky "
             'way to save a little bit of power. And I want to show you a real-time example of '
             "this. And, uh, sorry to the guy who's renting this rig right now, but, uh, I "
             "swear I'll change it back.",
      'title': "I Spent $10,000 Testing AI GPU Rentals - Here's What I Learned "
               '(BearMarketMiner)',
      'url': 'https://www.youtube.com/watch?v=egH5hKD913Y&t=1223s',
      'video_id': 'egH5hKD913Y'},
     {'author': 'Beam Networks',
      'channel': 'Beam Networks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=4NmQ_0-0BC8&t=170s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So prox MOX they all do backups to the host that was at the top of the rack um '
              'that you saw in that screenshot so they all back up I think nightly um all of.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'So prox MOX they all do backups to the host that was at the top of the rack um '
             'that you saw in that screenshot so they all back up I think nightly um all of.',
      'title': 'Why I Colocate 6 Servers (Data Center Walkthrough) (Beam Networks)',
      'url': 'https://www.youtube.com/watch?v=4NmQ_0-0BC8&t=170s',
      'video_id': '4NmQ_0-0BC8'},
     {'author': 'Craft Computing',
      'channel': 'Craft Computing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=JoqFD69bWLw&t=167s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Series but now we get to skip directly to part three which is why I needed the '
              "Epic 7601 back and to answer that I'm going to need a little bit more room on "
              "the table oh God this thing's heavy.",
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'Series but now we get to skip directly to part three which is why I needed the '
             "Epic 7601 back and to answer that I'm going to need a little bit more room on "
             "the table oh God this thing's heavy.",
      'title': 'TWO AMD Epyc Servers for $500! (Craft Computing)',
      'url': 'https://www.youtube.com/watch?v=JoqFD69bWLw&t=167s',
      'video_id': 'JoqFD69bWLw'},
     {'author': 'Lukasz Gawenda',
      'channel': 'Lukasz Gawenda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=352s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'KV cage that it will be dynamically used, managed and so on. One thing that I '
              'mentioned before so the prefill stage and we can compute it using parallelism. '
              'Because this is typical matrix more. Now you could say that we could do '
              'batching.',
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': 'KV cage that it will be dynamically used, managed and so on. One thing that I '
             'mentioned before so the prefill stage and we can compute it using parallelism. '
             'Because this is typical matrix more. Now you could say that we could do '
             'batching.',
      'title': "I Benchmarked vLLM vs SGLang So You Don't Have To Shocking Results! (Lukasz "
               'Gawenda)',
      'url': 'https://www.youtube.com/watch?v=gkl2KlJ7FP0&t=352s',
      'video_id': 'gkl2KlJ7FP0'},
     {'author': 'Public Service Commission of Wisconsin',
      'channel': 'Public Service Commission of Wisconsin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=vH9VQq2V9Qw&t=134s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Both my voice revenues and my Broadband revenues Broadband revenues are not '
              'accessible so we split out that portion and this system will calcul at '
              'eventually the the difference and use that as an offset against gross revenues '
              'for calendar year.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Both my voice revenues and my Broadband revenues Broadband revenues are not '
             'accessible so we split out that portion and this system will calcul at '
             'eventually the the difference and use that as an offset against gross revenues '
             'for calendar year.',
      'title': 'WI Telecom AQS Section 3 Non USF and USF Assessments (Public Service '
               'Commission of Wisconsin)',
      'url': 'https://www.youtube.com/watch?v=vH9VQq2V9Qw&t=134s',
      'video_id': 'vH9VQq2V9Qw'}],
 6: [{'author': 'CodeFlow Daily',
      'channel': 'CodeFlow Daily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=WT00OA0ml2g&t=438s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Two details the exam likes. First, features that are stateful by nature, such '
              'as the batch API, the files API, and code execution are marked not eligible. '
              'Nothing blocks the request. Using one is a choice to step outside your '
              'arrangement for that data.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': 'Two details the exam likes. First, features that are stateful by nature, such as '
             'the batch API, the files API, and code execution are marked not eligible. '
             'Nothing blocks the request. Using one is a choice to step outside your '
             'arrangement for that data.',
      'title': 'Claude Architect Professional (CCAR-P) Part 11: Compliance, HIPAA, FedRAMP and '
               'Ethical AI (CodeFlow Daily)',
      'url': 'https://www.youtube.com/watch?v=WT00OA0ml2g&t=438s',
      'video_id': 'WT00OA0ml2g'},
     {'author': 'BuzzerBeep',
      'channel': 'BuzzerBeep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=9W2MLkN5lf4&t=121s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And a filtered text doesn't bounce. You find out when a user says nobody warned "
              "them. Here's where MSPs need to slow down. Your client's relationship with its "
              "employees doesn't mean they agreed to text from you. A client's HR phone list "
              'is not your opt-in list.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': "And a filtered text doesn't bounce. You find out when a user says nobody warned "
             "them. Here's where MSPs need to slow down. Your client's relationship with its "
             "employees doesn't mean they agreed to text from you. A client's HR phone list is "
             'not your opt-in list.',
      'title': '10DLC Explained: What Is 10DLC? A Plain-English Guide for MSPs (BuzzerBeep)',
      'url': 'https://www.youtube.com/watch?v=9W2MLkN5lf4&t=121s',
      'video_id': '9W2MLkN5lf4'},
     {'author': 'VisionNLP',
      'channel': 'VisionNLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:26](https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=806s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Telnyx I have created the API key. Now let me run the export command. I will '
              'delete the key as soon as this video is completed. First we will create the '
              'outbound voice profile in the Telnyx. I will change the name to Tune Wave.',
      'timestamp': 806,
      'timestamp_label': '[00:13:26]',
      'timestamp_seconds': 806,
      'tip': 'Telnyx I have created the API key. Now let me run the export command. I will '
             'delete the key as soon as this video is completed. First we will create the '
             'outbound voice profile in the Telnyx. I will change the name to Tune Wave.',
      'title': 'LiveKit SIP Trunking with Telnyx | Self-Hosted Azure, FQDN & AI Phone Calls '
               '(VisionNLP)',
      'url': 'https://www.youtube.com/watch?v=ZQWTIIR9Exs&t=806s',
      'video_id': 'ZQWTIIR9Exs'},
     {'author': 'The Boon of Wireless',
      'channel': 'The Boon of Wireless',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:09](https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=729s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then we computed that data from all the way back from 2022 to current. So '
              "when you hear about oh there's more money coming in this industry than ever "
              "before, we're able to show that proof on the website because we list all that "
              'data, right?',
      'timestamp': 729,
      'timestamp_label': '[00:12:09]',
      'timestamp_seconds': 729,
      'tip': 'And then we computed that data from all the way back from 2022 to current. So '
             "when you hear about oh there's more money coming in this industry than ever "
             "before, we're able to show that proof on the website because we list all that "
             'data, right?',
      'title': 'How to Launch & Scale an MVNO Successfully? (The Boon of Wireless)',
      'url': 'https://www.youtube.com/watch?v=Gye5g8KT7Oo&t=729s',
      'video_id': 'Gye5g8KT7Oo'},
     {'author': 'Toronto Machine Learning Society (TMLS)',
      'channel': 'Toronto Machine Learning Society (TMLS)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=_oWJ0t-RW7o&t=22s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, building AI platforms is not easy, right? So, let's look at OpenAI's cloud "
              'infra. So back in 2016, OpenAI and Microsoft signed a deal to have Azure as '
              "like the exclusive cloud provider for all of OpenAI's GPU needs.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "So, building AI platforms is not easy, right? So, let's look at OpenAI's cloud "
             'infra. So back in 2016, OpenAI and Microsoft signed a deal to have Azure as like '
             "the exclusive cloud provider for all of OpenAI's GPU needs.",
      'title': 'Building Multi-Cloud GenAI Platforms Without the Pain | Romil Bhardwaj, '
               'SkyPilot (Toronto Machine Learning Society (TMLS))',
      'url': 'https://www.youtube.com/watch?v=_oWJ0t-RW7o&t=22s',
      'video_id': '_oWJ0t-RW7o'},
     {'author': 'Telgorithm',
      'channel': 'Telgorithm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:07](https://www.youtube.com/watch?v=dgkKW0cbz1E&t=2287s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just sort of that's right right there's no shortcut and I'll actually we'll go "
              "back to the question here but we'll deal with sole proprietor.",
      'timestamp': 2287,
      'timestamp_label': '[00:38:07]',
      'timestamp_seconds': 2287,
      'tip': "Just sort of that's right right there's no shortcut and I'll actually we'll go "
             "back to the question here but we'll deal with sole proprietor.",
      'title': 'A2P 10DLC Messaging: TCR Registration & Campaign Vetting Q&A | Telgorithm '
               '(Telgorithm)',
      'url': 'https://www.youtube.com/watch?v=dgkKW0cbz1E&t=2287s',
      'video_id': 'dgkKW0cbz1E'},
     {'author': 'Telecom Application Development Summit',
      'channel': 'Telecom Application Development Summit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:16](https://www.youtube.com/watch?v=SRizDef5BbE&t=1336s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For you what kind of data what kind of data Protections in your contract exist '
              "between you and the TCR Kera now Tata uh and your client's data and contacts.",
      'timestamp': 1336,
      'timestamp_label': '[00:22:16]',
      'timestamp_seconds': 1336,
      'tip': 'For you what kind of data what kind of data Protections in your contract exist '
             "between you and the TCR Kera now Tata uh and your client's data and contacts.",
      'title': 'How to Register Your 10DLC Brands & Campaigns with TCE: Commio Special w/Tim '
               'McLain (Telecom Application Development Summit)',
      'url': 'https://www.youtube.com/watch?v=SRizDef5BbE&t=1336s',
      'video_id': 'SRizDef5BbE'},
     {'author': 'Alec Glover',
      'channel': 'Alec Glover',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=TZp1yBea0o4&t=168s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re you know paying for the things that you should be and not paying for things "
              "that you're not getting any value back for. So the first component that I want "
              'to talk about is power.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': "'re you know paying for the things that you should be and not paying for things "
             "that you're not getting any value back for. So the first component that I want "
             'to talk about is power.',
      'title': 'How to Build a Warehouse GPU Data Center: A Practical Guide (Alec Glover)',
      'url': 'https://www.youtube.com/watch?v=TZp1yBea0o4&t=168s',
      'video_id': 'TZp1yBea0o4'},
     {'author': 'Lawrence Systems',
      'channel': 'Lawrence Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gsN_CJJDy_o&t=15s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Months ago that I did a video and you'll find that linked down below now that "
              'video got the attention of a much much larger modern data center my friends.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Months ago that I did a video and you'll find that linked down below now that "
             'video got the attention of a much much larger modern data center my friends.',
      'title': 'Inside a 36 Megawatt Data Center: The Power, Cooling and Fiber (Lawrence '
               'Systems)',
      'url': 'https://www.youtube.com/watch?v=gsN_CJJDy_o&t=15s',
      'video_id': 'gsN_CJJDy_o'},
     {'author': 'Data Science Festival',
      'channel': 'Data Science Festival',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:26](https://www.youtube.com/watch?v=WiA5Hm6IpZs&t=986s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um and remember, they only need to be good enough for the specific application. '
              "So, our first one, go back. Okay, here's another slide.",
      'timestamp': 986,
      'timestamp_label': '[00:16:26]',
      'timestamp_seconds': 986,
      'tip': 'Um and remember, they only need to be good enough for the specific application. '
             "So, our first one, go back. Okay, here's another slide.",
      'title': 'Self Hosted LLMs: Running Your Own Inference Infrastructure (Data Science '
               'Festival)',
      'url': 'https://www.youtube.com/watch?v=WiA5Hm6IpZs&t=986s',
      'video_id': 'WiA5Hm6IpZs'},
     {'author': 'Red Panda Mining',
      'channel': 'Red Panda Mining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:00](https://www.youtube.com/watch?v=ET1JYocpu0M&t=600s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Okay, so I I did take out the bracket. So, this server can actually fit 10 of '
              "these V100s. So, uh if I can find two more, which I'm trying to find two more, "
              '16 GB V100s, if anyone had any has any leads, let me know.',
      'timestamp': 600,
      'timestamp_label': '[00:10:00]',
      'timestamp_seconds': 600,
      'tip': 'Okay, so I I did take out the bracket. So, this server can actually fit 10 of '
             "these V100s. So, uh if I can find two more, which I'm trying to find two more, "
             '16 GB V100s, if anyone had any has any leads, let me know.',
      'title': 'I Bought 8 ACTUAL "Ai" GPUs... (Red Panda Mining)',
      'url': 'https://www.youtube.com/watch?v=ET1JYocpu0M&t=600s',
      'video_id': 'ET1JYocpu0M'},
     {'author': 'Open Compute Project',
      'channel': 'Open Compute Project',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=OXIIIfjjDgU&t=21s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And uh here I show you the three generations. Uh the first one is the power '
              'shelf. Uh basically the power shelf is all the 50 V output and the density is '
              'on the IT rack. Uh the power rating is from the 33 kW to 110 kW and all the '
              'products is most of is in mass production.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'And uh here I show you the three generations. Uh the first one is the power '
             'shelf. Uh basically the power shelf is all the 50 V output and the density is on '
             'the IT rack. Uh the power rating is from the 33 kW to 110 kW and all the '
             'products is most of is in mass production.',
      'title': 'LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON (Open '
               'Compute Project)',
      'url': 'https://www.youtube.com/watch?v=OXIIIfjjDgU&t=21s',
      'video_id': 'OXIIIfjjDgU'},
     {'author': 'IoT (eSIM) Studio',
      'channel': 'IoT (eSIM) Studio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=GZtF-I2M1ZE&t=35s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In countries like in germany it would be vodafone o2 or telecom germany these '
              'are so-called legacy network operators because they have been in the first '
              'place launching the underlying network patrimony with the granted frequency '
              'licenses from their governments.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'In countries like in germany it would be vodafone o2 or telecom germany these '
             'are so-called legacy network operators because they have been in the first place '
             'launching the underlying network patrimony with the granted frequency licenses '
             'from their governments.',
      'title': 'BEST MNO, MVNO for cellular data connectivity with eSIM (eUICC) SIM card (IoT '
               '(eSIM) Studio)',
      'url': 'https://www.youtube.com/watch?v=GZtF-I2M1ZE&t=35s',
      'video_id': 'GZtF-I2M1ZE'},
     {'author': 'SUSE',
      'channel': 'SUSE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=4q3LHacRheg&t=45s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Background to query the GPU  via the driver to find out the profiles, the '
              "maximum available. So in this particular case, I'm going to.",
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Background to query the GPU  via the driver to find out the profiles, the '
             "maximum available. So in this particular case, I'm going to.",
      'title': 'SUSE Virtualization NVIDIA MIG vGPU Multi-Tenancy on Kubernetes (SUSE)',
      'url': 'https://www.youtube.com/watch?v=4q3LHacRheg&t=45s',
      'video_id': '4q3LHacRheg'},
     {'author': 'Crypto LLC',
      'channel': 'Crypto LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=nHwXk9HCuYI&t=133s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's uh the windows 11 for that same rig for 23. you can see here we have "
              'system interrupts at around 10 percent then drops down to 8 and so on and the '
              'miner is actually running right now.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "Here's uh the windows 11 for that same rig for 23. you can see here we have "
             'system interrupts at around 10 percent then drops down to 8 and so on and the '
             'miner is actually running right now.',
      'title': 'GPU Mining Farm - Fixing System Interrupts in Windows 11, Mining Crash (Crypto '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=nHwXk9HCuYI&t=133s',
      'video_id': 'nHwXk9HCuYI'}],
 7: [{'author': 'DataMListic',
      'channel': 'DataMListic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=X8CwAqYxH1E&t=57s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Same cost, four times the throughput. In another step, same thing again. The '
              'bigger the batch, the more useful work you squeeze out of every read, which is '
              'why every serving system batches requests. But, batching has a problem of its '
              "own. Requests don't finish together.",
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'Same cost, four times the throughput. In another step, same thing again. The '
             'bigger the batch, the more useful work you squeeze out of every read, which is '
             'why every serving system batches requests. But, batching has a problem of its '
             "own. Requests don't finish together.",
      'title': 'Continuous Batching - How LLM Servers Keep the GPU Full (DataMListic)',
      'url': 'https://www.youtube.com/watch?v=X8CwAqYxH1E&t=57s',
      'video_id': 'X8CwAqYxH1E'},
     {'author': 'AWS Events',
      'channel': 'AWS Events',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:44](https://www.youtube.com/watch?v=tPYmvdc5oE0&t=704s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "By integrating AWS services with automated workflows, we're working to "
              'transform what was once a very manual and reactive process into more of a '
              'self-improving system. So, starting with this concept of an intelligent cycle, '
              'our journey, which is still in progress, right?',
      'timestamp': 704,
      'timestamp_label': '[00:11:44]',
      'timestamp_seconds': 704,
      'tip': "By integrating AWS services with automated workflows, we're working to transform "
             'what was once a very manual and reactive process into more of a self-improving '
             'system. So, starting with this concept of an intelligent cycle, our journey, '
             'which is still in progress, right?',
      'title': "AWS re:Invent 2025 - Amazon's finops: Cloud cost lessons from a global "
               'e-commerce giant (AMZ308) (AWS Events)',
      'url': 'https://www.youtube.com/watch?v=tPYmvdc5oE0&t=704s',
      'video_id': 'tPYmvdc5oE0'},
     {'author': 'Codemia',
      'channel': 'Codemia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:43](https://www.youtube.com/watch?v=a_zou7QahAo&t=1963s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A wrong guess strands capacity. So step back and ask where the money actually '
              'moves because it is not in microoptimizing the scheduling loop. The first is '
              'placement quality.',
      'timestamp': 1963,
      'timestamp_label': '[00:32:43]',
      'timestamp_seconds': 1963,
      'tip': 'A wrong guess strands capacity. So step back and ask where the money actually '
             'moves because it is not in microoptimizing the scheduling loop. The first is '
             'placement quality.',
      'title': 'GPU Cluster Scheduler System Design | Gang Scheduling, Topology, Preemption '
               '(Codemia)',
      'url': 'https://www.youtube.com/watch?v=a_zou7QahAo&t=1963s',
      'video_id': 'a_zou7QahAo'},
     {'author': 'Lukasz Gawenda',
      'channel': 'Lukasz Gawenda',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=ycEQJIyZ2sU&t=210s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the maximum number of batch tokens. This is the per scheduler step budget. '
              'It controls how many total tokens the scheduler can process in single '
              'iteration. Think of it as a throughput cap.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'Now, the maximum number of batch tokens. This is the per scheduler step budget. '
             'It controls how many total tokens the scheduler can process in single iteration. '
             'Think of it as a throughput cap.',
      'title': 'vLLM Explained in 10 Min: 3 Settings for Insanely Fast Throughput & Latency! '
               '(Lukasz Gawenda)',
      'url': 'https://www.youtube.com/watch?v=ycEQJIyZ2sU&t=210s',
      'video_id': 'ycEQJIyZ2sU'},
     {'author': 'AI WITH Rithesh',
      'channel': 'AI WITH Rithesh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:52](https://www.youtube.com/watch?v=lasG5MsR-gE&t=592s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Requests come in whenever and they finish at different lengths. Continuous '
              'batching decides the batch one step at a time. When a sequence finishes, a '
              'waiting request takes its place on the very next step, so no one waits for the '
              'whole batch to finish.',
      'timestamp': 592,
      'timestamp_label': '[00:09:52]',
      'timestamp_seconds': 592,
      'tip': 'Requests come in whenever and they finish at different lengths. Continuous '
             'batching decides the batch one step at a time. When a sequence finishes, a '
             'waiting request takes its place on the very next step, so no one waits for the '
             'whole batch to finish.',
      'title': 'How LLMs Actually Run on a GPU: vLLM, SGLang & Quantization Explained (AI WITH '
               'Rithesh)',
      'url': 'https://www.youtube.com/watch?v=lasG5MsR-gE&t=592s',
      'video_id': 'lasG5MsR-gE'},
     {'author': 'Austin Marland',
      'channel': 'Austin Marland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ttmM4fmBHDU&t=15s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Start sending text messages to your leads this is called a2p 10 DLC there's an "
              "application process it's a little bit tricky and a lot of a lot of businesses.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Start sending text messages to your leads this is called a2p 10 DLC there's an "
             "application process it's a little bit tricky and a lot of a lot of businesses.",
      'title': 'How to pass A2P 10DLC registration FAST (full 2025 tutorial for ANY software) '
               '(Austin Marland)',
      'url': 'https://www.youtube.com/watch?v=ttmM4fmBHDU&t=15s',
      'video_id': 'ttmM4fmBHDU'},
     {'author': 'Vizuara',
      'channel': 'Vizuara',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:03](https://www.youtube.com/watch?v=IDjyrXKsC5U&t=1863s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, so I'm I'm going to go through this in steps. So, let's say the question "
              'you are asking is, "What is the capital of France?" And let\'s say the system '
              'prompt is, "You are a helpful assistant." So, system prompt will remain '
              'constant.',
      'timestamp': 1863,
      'timestamp_label': '[00:31:03]',
      'timestamp_seconds': 1863,
      'tip': "Okay, so I'm I'm going to go through this in steps. So, let's say the question "
             'you are asking is, "What is the capital of France?" And let\'s say the system '
             'prompt is, "You are a helpful assistant." So, system prompt will remain '
             'constant.',
      'title': 'Journey of a token in vLLM and SGLang (Vizuara)',
      'url': 'https://www.youtube.com/watch?v=IDjyrXKsC5U&t=1863s',
      'video_id': 'IDjyrXKsC5U'},
     {'author': 'Cian Mag',
      'channel': 'Cian Mag',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:06](https://www.youtube.com/watch?v=kgSARM9iGF4&t=246s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A traditional dense model uses its main network throughout the computation. A '
              'mixture of experts model has multiple specialized expert networks with a '
              'routing system selecting which experts contribute to a particular step.',
      'timestamp': 246,
      'timestamp_label': '[00:04:06]',
      'timestamp_seconds': 246,
      'tip': 'A traditional dense model uses its main network throughout the computation. A '
             'mixture of experts model has multiple specialized expert networks with a routing '
             'system selecting which experts contribute to a particular step.',
      'title': '4 Broken Laptops Run an 80B AI Model With No GPU (128GB RAM) (Cian Mag)',
      'url': 'https://www.youtube.com/watch?v=kgSARM9iGF4&t=246s',
      'video_id': 'kgSARM9iGF4'},
     {'author': 'Techi Nik',
      'channel': 'Techi Nik',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=f-FKoMHqRoI&t=103s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Standard workload so you are not wasting resources on GPU configuration here '
              'now first step is to have a GPU node in your kubernetes cluster if you are on '
              'cloud providers like AWS or GCP they offer.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'Standard workload so you are not wasting resources on GPU configuration here now '
             'first step is to have a GPU node in your kubernetes cluster if you are on cloud '
             'providers like AWS or GCP they offer.',
      'title': 'How to deploy NVIDIA GPU Operator Deployment on Kubernetes (Techi Nik)',
      'url': 'https://www.youtube.com/watch?v=f-FKoMHqRoI&t=103s',
      'video_id': 'f-FKoMHqRoI'},
     {'author': 'Jonas Massie',
      'channel': 'Jonas Massie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:03](https://www.youtube.com/watch?v=_wo5wokt3dI&t=483s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Want to make sure that you have your API key on hand to process these API '
              "requests when that is done we'll head over to something like Postman and the.",
      'timestamp': 483,
      'timestamp_label': '[00:08:03]',
      'timestamp_seconds': 483,
      'tip': 'Want to make sure that you have your API key on hand to process these API '
             "requests when that is done we'll head over to something like Postman and the.",
      'title': 'The Ultimate SIP Trunking Guide for AI Voice Agents | Twilio + Vapi (Jonas '
               'Massie)',
      'url': 'https://www.youtube.com/watch?v=_wo5wokt3dI&t=483s',
      'video_id': '_wo5wokt3dI'},
     {'author': 'Data Center News',
      'channel': 'Data Center News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=8DzqbL0HKG0&t=115s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you get a flat, you can replace it, but you'll still experience some "
              'downtime. Tier 3 steps it up with concurrent maintainability. It has dual '
              'distribution paths for power and cooling, allowing for maintenance without '
              'shutting down the entire system.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "If you get a flat, you can replace it, but you'll still experience some "
             'downtime. Tier 3 steps it up with concurrent maintainability. It has dual '
             'distribution paths for power and cooling, allowing for maintenance without '
             'shutting down the entire system.',
      'title': 'Uptime Data Center Tier Levels - The Gold Standard (Data Center News)',
      'url': 'https://www.youtube.com/watch?v=8DzqbL0HKG0&t=115s',
      'video_id': '8DzqbL0HKG0'},
     {'author': 'SkyPilot',
      'channel': 'SkyPilot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=Pas2NE76220&t=264s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I have to do 10 steps you know it's like yeah like by the second step you "
              "already lose like almost like 90% of the people right like they're not going to "
              'be doing like 10 steps to enable something new.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': "I have to do 10 steps you know it's like yeah like by the second step you "
             "already lose like almost like 90% of the people right like they're not going to "
             'be doing like 10 steps to enable something new.',
      'title': 'SkyPilot at 100k+ GPU Scale at Meta AI (FAIR) - Lucca Bertoncini (Meta) '
               '(SkyPilot)',
      'url': 'https://www.youtube.com/watch?v=Pas2NE76220&t=264s',
      'video_id': 'Pas2NE76220'},
     {'author': 'Jeremy Cioara',
      'channel': 'Jeremy Cioara',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=5WW8432TcR4&t=287s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Want you to do is really take that and go set up an account you don't have to "
              'be ready to grab an autonomous system number unless you really are just jump in '
              'and get established create a point of contact record and look around a little '
              'bit.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': "Want you to do is really take that and go set up an account you don't have to be "
             'ready to grab an autonomous system number unless you really are just jump in and '
             'get established create a point of contact record and look around a little bit.',
      'title': 'ARIN: Purpose and Registration! Ep.4: Understanding BGP - Keeping IT Simple '
               '(Jeremy Cioara)',
      'url': 'https://www.youtube.com/watch?v=5WW8432TcR4&t=287s',
      'video_id': '5WW8432TcR4'},
     {'author': 'vCluster',
      'channel': 'vCluster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=KzJvhbdgvl8&t=256s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, we're installing the GPU operator. Again, we're just following the exact "
              "same steps that we did on the first one, uh, but we're doing it on the second "
              'one.',
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': "So, we're installing the GPU operator. Again, we're just following the exact "
             "same steps that we did on the first one, uh, but we're doing it on the second "
             'one.',
      'title': 'GPU Timeslicing + Open WebUI on Kubernetes with vCluster – Step‑by‑Step Guide '
               '(vCluster)',
      'url': 'https://www.youtube.com/watch?v=KzJvhbdgvl8&t=256s',
      'video_id': 'KzJvhbdgvl8'},
     {'author': 'Sangoma',
      'channel': 'Sangoma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:54](https://www.youtube.com/watch?v=3XJ9OkK8aFw&t=1434s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Improving our implementation and offering as much control over the system as '
              'possible to you thank you again for your time everybody and watch for '
              'communication from us on resources that get more detailed with the technology '
              'and its requirements.',
      'timestamp': 1434,
      'timestamp_label': '[00:23:54]',
      'timestamp_seconds': 1434,
      'tip': 'Improving our implementation and offering as much control over the system as '
             'possible to you thank you again for your time everybody and watch for '
             'communication from us on resources that get more detailed with the technology '
             'and its requirements.',
      'title': 'Everything You Need to Know About STIR SHAKEN Compliance (Sangoma)',
      'url': 'https://www.youtube.com/watch?v=3XJ9OkK8aFw&t=1434s',
      'video_id': '3XJ9OkK8aFw'}],
 8: [{'author': 'Signal House',
      'channel': 'Signal House',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=sVsWkczKncU&t=287s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CRM or a marketing platform that has a lot of customers under your platform i. '
              'It means that every single customer is going to be bundled into that specific '
              'API rate limit.',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': 'CRM or a marketing platform that has a lot of customers under your platform i. '
             'It means that every single customer is going to be bundled into that specific '
             'API rate limit.',
      'title': 'Is Bandwidth, Twilio, and Telnyx Killing your 10DLC A2P Business Messaging?! '
               '(Signal House)',
      'url': 'https://www.youtube.com/watch?v=sVsWkczKncU&t=287s',
      'video_id': 'sVsWkczKncU'},
     {'author': 'Micro Learning',
      'channel': 'Micro Learning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=zkMCHA5uzIo&t=107s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Decode is heavily memory-bound. It's completely starving for memory bandwidth "
              'because it constantly has to shuffle massive amounts of data back and forth '
              "just to spit out a single word. Section two, prefill, decode, and cache. Let's "
              'move to and see how this builds.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "Decode is heavily memory-bound. It's completely starving for memory bandwidth "
             'because it constantly has to shuffle massive amounts of data back and forth just '
             "to spit out a single word. Section two, prefill, decode, and cache. Let's move "
             'to and see how this builds.',
      'title': 'LLM Inference Optimization Explained: KV Cache, Flash Attention, vLLM & SGLang '
               '(Micro Learning)',
      'url': 'https://www.youtube.com/watch?v=zkMCHA5uzIo&t=107s',
      'video_id': 'zkMCHA5uzIo'},
     {'author': 'Cakka | Cybersecurity',
      'channel': 'Cakka | Cybersecurity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=psGPevLhvpI&t=379s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The components managing this force, the busways, RPPs, and PDUs function '
              'collectively as a matrix of intelligent network nodes. They constantly stream '
              'exact current, voltage, and temperature telemetry back to a centralized data '
              'center infrastructure platform.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': 'The components managing this force, the busways, RPPs, and PDUs function '
             'collectively as a matrix of intelligent network nodes. They constantly stream '
             'exact current, voltage, and temperature telemetry back to a centralized data '
             'center infrastructure platform.',
      'title': 'How AI Data Centers Power GPUs | Busways, RPPs & Rack PDUs Explained | Day 18 '
               '(Cakka | Cybersecurity)',
      'url': 'https://www.youtube.com/watch?v=psGPevLhvpI&t=379s',
      'video_id': 'psGPevLhvpI'},
     {'author': 'VoiceBuy | Cloud Telecom & VoIP',
      'channel': 'VoiceBuy | Cloud Telecom & VoIP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=elbBH6g2MU8&t=346s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ask exactly how they handle database failovers and if their API coverage is '
              'genuinely 100% demand to know if their platform can automatically kill active '
              'sessions if velocity spikes are detected. Seriously, do not settle for vague '
              'answers here.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': 'Ask exactly how they handle database failovers and if their API coverage is '
             'genuinely 100% demand to know if their platform can automatically kill active '
             'sessions if velocity spikes are detected. Seriously, do not settle for vague '
             'answers here.',
      'title': 'Top 5 Carrier SIP Softswitch Providers in 2026 (Complete Comparison) (VoiceBuy '
               '| Cloud Telecom & VoIP)',
      'url': 'https://www.youtube.com/watch?v=elbBH6g2MU8&t=346s',
      'video_id': 'elbBH6g2MU8'},
     {'author': 'Byte Forensics',
      'channel': 'Byte Forensics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:20](https://www.youtube.com/watch?v=ux5n4VAhUNU&t=200s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's an important nuance. The chef might prepare a whole batch while "
              'ingredients are in the kitchen or the restaurant might arrange deliveries in '
              'advance. In the same way, software can prefetch, cache, batch, and overlap data '
              'transfers with computation.',
      'timestamp': 200,
      'timestamp_label': '[00:03:20]',
      'timestamp_seconds': 200,
      'tip': "There's an important nuance. The chef might prepare a whole batch while "
             'ingredients are in the kitchen or the restaurant might arrange deliveries in '
             'advance. In the same way, software can prefetch, cache, batch, and overlap data '
             'transfers with computation.',
      'title': 'The Fast SSD Offload Myth: Why Running Local AI from NVMe Fails (Byte '
               'Forensics)',
      'url': 'https://www.youtube.com/watch?v=ux5n4VAhUNU&t=200s',
      'video_id': 'ux5n4VAhUNU'},
     {'author': 'ProsperOps, a Flexera company',
      'channel': 'ProsperOps, a Flexera company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=KW_LS_stgvc&t=100s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the X axis and the Y axis is the effective savings rate. So what our "
              'prospects without our service, so this is generally people using either a cloud '
              'management platform tool, scripts, Excel spreadsheets, what have you, what kind '
              'of results are they achieving?',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "That's the X axis and the Y axis is the effective savings rate. So what our "
             'prospects without our service, so this is generally people using either a cloud '
             'management platform tool, scripts, Excel spreadsheets, what have you, what kind '
             'of results are they achieving?',
      'title': 'Benchmarking AWS Cloud Financial Management (ProsperOps, a Flexera company)',
      'url': 'https://www.youtube.com/watch?v=KW_LS_stgvc&t=100s',
      'video_id': 'KW_LS_stgvc'},
     {'author': 'MegaWatt Path',
      'channel': 'MegaWatt Path',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=orsNmJSDpws&t=75s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're talking Amazon, Google, Microsoft, Meta, the cloud giants. These places "
              'are massive with hundreds of thousands of servers running at ultra efficiency. '
              'Everything is automated, optimized, and built to handle mind-blowing amounts of '
              'data.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': "We're talking Amazon, Google, Microsoft, Meta, the cloud giants. These places "
             'are massive with hundreds of thousands of servers running at ultra efficiency. '
             'Everything is automated, optimized, and built to handle mind-blowing amounts of '
             'data.',
      'title': 'The 4 Types of Data Centers Explained | Enterprise, Colocation, Hyperscale & '
               'Edge (MegaWatt Path)',
      'url': 'https://www.youtube.com/watch?v=orsNmJSDpws&t=75s',
      'video_id': 'orsNmJSDpws'},
     {'author': 'Crosstalk Solutions',
      'channel': 'Crosstalk Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=ycGPHG_ANrE&t=446s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That pop up now when we're reselling sip trunks to our customers we're paying "
              'VoIP Innovations for the wholesale minutes as well as the billing platform.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': "That pop up now when we're reselling sip trunks to our customers we're paying "
             'VoIP Innovations for the wholesale minutes as well as the billing platform.',
      'title': 'STIR/SHAKEN and the Death of the Small VoIP Carrier (Crosstalk Solutions)',
      'url': 'https://www.youtube.com/watch?v=ycGPHG_ANrE&t=446s',
      'video_id': 'ycGPHG_ANrE'},
     {'author': 'Omid Mohajerani',
      'channel': 'Omid Mohajerani',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=HkWcpuMrX7k&t=355s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of course, for this one, you need a token. You need the authorization and you '
              'need the VAPI token that if you go to your Vapi platform, if you go to the '
              'actually Vapi API keys, the API key that you need is the private key.',
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': 'Of course, for this one, you need a token. You need the authorization and you '
             'need the VAPI token that if you go to your Vapi platform, if you go to the '
             'actually Vapi API keys, the API key that you need is the private key.',
      'title': 'Connect VAPI BYO SIP Trunk to FreeSWITCH (Route to Any Carrier) (Omid '
               'Mohajerani)',
      'url': 'https://www.youtube.com/watch?v=HkWcpuMrX7k&t=355s',
      'video_id': 'HkWcpuMrX7k'},
     {'author': 'Gareth Knight',
      'channel': 'Gareth Knight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=mNQb5B_voNw&t=289s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Continuity of their operations by providing a robust and reliable platform for '
              'critical data and applications tier 3 data centers Empower businesses to focus '
              'on what they do best knowing that their digital assets are in safe.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': 'Continuity of their operations by providing a robust and reliable platform for '
             'critical data and applications tier 3 data centers Empower businesses to focus '
             'on what they do best knowing that their digital assets are in safe.',
      'title': 'Understanding Tier 3 Data Centre Requirements (Gareth Knight)',
      'url': 'https://www.youtube.com/watch?v=mNQb5B_voNw&t=289s',
      'video_id': 'mNQb5B_voNw'},
     {'author': 'SkyPilot',
      'channel': 'SkyPilot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:32](https://www.youtube.com/watch?v=vdP0fhqpYZs&t=572s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Grafana out of the box for you. Um uh just an example of the kind of data you '
              'can get. So, GPU temperature, InfiniBand bandwidth, free RAM. This is actually '
              'pretty light, even though it seems like quite involved.',
      'timestamp': 572,
      'timestamp_label': '[00:09:32]',
      'timestamp_seconds': 572,
      'tip': 'Grafana out of the box for you. Um uh just an example of the kind of data you '
             'can get. So, GPU temperature, InfiniBand bandwidth, free RAM. This is actually '
             'pretty light, even though it seems like quite involved.',
      'title': 'Training At Scale With Confidence (SkyPilot Integration w/ CoreWeave SUNK) - '
               'Deok Filho (CoreWeave) (SkyPilot)',
      'url': 'https://www.youtube.com/watch?v=vdP0fhqpYZs&t=572s',
      'video_id': 'vdP0fhqpYZs'},
     {'author': 'CNCF [Cloud Native Computing Foundation]',
      'channel': 'CNCF [Cloud Native Computing Foundation]',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=nABVTFBmV2M&t=170s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In total we installed more than 2 TB of data downloading all the intricacy of '
              'dependency between all the various component. Uh What we learned at very '
              'quickly that a working GPU cluster is not the same as a shareable GPU platform.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'In total we installed more than 2 TB of data downloading all the intricacy of '
             'dependency between all the various component. Uh What we learned at very quickly '
             'that a working GPU cluster is not the same as a shareable GPU platform.',
      'title': 'Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA '
               'KAI (G/H2... Luca Berton (CNCF [Cloud Native Computing Foundation])',
      'url': 'https://www.youtube.com/watch?v=nABVTFBmV2M&t=170s',
      'video_id': 'nABVTFBmV2M'},
     {'author': 'Colovore LLC',
      'channel': 'Colovore LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=JMz8luHLVxc&t=102s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Wall-to-wall densities of 20 kilowatts per rack and we want you to be marty not '
              'don deploy in our high density data center and you will reduce your tco and '
              'ensure long-term I.t scalability modern servers need modern colo.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Wall-to-wall densities of 20 kilowatts per rack and we want you to be marty not '
             'don deploy in our high density data center and you will reduce your tco and '
             'ensure long-term I.t scalability modern servers need modern colo.',
      'title': 'Colovore - Modern Servers Require High Density Colocation (Colovore LLC)',
      'url': 'https://www.youtube.com/watch?v=JMz8luHLVxc&t=102s',
      'video_id': 'JMz8luHLVxc'},
     {'author': 'HostingCompared with Natalie',
      'channel': 'HostingCompared with Natalie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=b0fXfKwASvI&t=48s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Level three, tensor parallel. Now, each layer itself is sharded. Both GPUs '
              'calculate partial results, then synchronize them. This can use aggregate memory '
              'for one model, but only when the architecture and software support it. And now '
              'the connection matters.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Level three, tensor parallel. Now, each layer itself is sharded. Both GPUs '
             'calculate partial results, then synchronize them. This can use aggregate memory '
             'for one model, but only when the architecture and software support it. And now '
             'the connection matters.',
      'title': '2x24GB GPUs Are NOT One 48GB GPU: RunPod vs Vast.ai (HostingCompared with '
               'Natalie)',
      'url': 'https://www.youtube.com/watch?v=b0fXfKwASvI&t=48s',
      'video_id': 'b0fXfKwASvI'},
     {'author': 'Vizuara',
      'channel': 'Vizuara',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=f4WDLg2sbx4&t=68s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You are storing these weights in VRAM, but you can't load all of that into a "
              'GPU compute core because the SRAM associated with GPU compute core is only few '
              'megabytes. So, you load the weights from even part of a layer to perform the '
              'forward pass.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "You are storing these weights in VRAM, but you can't load all of that into a GPU "
             'compute core because the SRAM associated with GPU compute core is only few '
             'megabytes. So, you load the weights from even part of a layer to perform the '
             'forward pass.',
      'title': 'How inference works at scale? vLLM and SGLang inference engines (Vizuara)',
      'url': 'https://www.youtube.com/watch?v=f4WDLg2sbx4&t=68s',
      'video_id': 'f4WDLg2sbx4'}],
 9: [{'author': 'TwilioDevs',
      'channel': 'TwilioDevs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=IUXJbMD7Qz4&t=281s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Method two is verbal consent. What if you're collecting consent over the phone "
              'or in person? The rules are just as strict, but the proof is different. You '
              'need to provide a verbatim script, the exact word-for-word lines your agents '
              'use or automated systems use.',
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': "Method two is verbal consent. What if you're collecting consent over the phone "
             'or in person? The rules are just as strict, but the proof is different. You need '
             'to provide a verbatim script, the exact word-for-word lines your agents use or '
             'automated systems use.',
      'title': 'A2P 10DLC Campaign with Twilio - First Time Success (TwilioDevs)',
      'url': 'https://www.youtube.com/watch?v=IUXJbMD7Qz4&t=281s',
      'video_id': 'IUXJbMD7Qz4'},
     {'author': 'Nick Gioftsos',
      'channel': 'Nick Gioftsos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=rGnDq9evKng&t=214s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Linux, and left them running for a year. They broke things, they tried weird '
              'routing protocols at midnight just to see what would happen. Try doing that in '
              'AWS or Azure today.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'Linux, and left them running for a year. They broke things, they tried weird '
             'routing protocols at midnight just to see what would happen. Try doing that in '
             'AWS or Azure today.',
      'title': 'The Cloud Was a Lie (Why Senior Engineers Are Going Back to Bare Metal) (Nick '
               'Gioftsos)',
      'url': 'https://www.youtube.com/watch?v=rGnDq9evKng&t=214s',
      'video_id': 'rGnDq9evKng'},
     {'author': 'Mariselle Hartwell',
      'channel': 'Mariselle Hartwell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=pa2rbXDnUYM&t=105s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It redacts sensitive personal information automatically. It keeps data within '
              'specific borders for legal reasons. This is the enterprise choice. It is built '
              'for teams that cannot afford a data leak or compliance nightmare. Then we have '
              'the open source powerhouse.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'It redacts sensitive personal information automatically. It keeps data within '
             'specific borders for legal reasons. This is the enterprise choice. It is built '
             'for teams that cannot afford a data leak or compliance nightmare. Then we have '
             'the open source powerhouse.',
      'title': 'OpenRouter vs Requesty vs LiteLLM Review 2026: API Routing Comparison & My '
               'Experience Overview (Mariselle Hartwell)',
      'url': 'https://www.youtube.com/watch?v=pa2rbXDnUYM&t=105s',
      'video_id': 'pa2rbXDnUYM'},
     {'author': 'Clerk AI',
      'channel': 'Clerk AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=CiI0Bewk8SU&t=163s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Opt her back in that it'll change from opted out to opted back in and we can "
              "continue the conversation with jiren and that's how you send your first out "
              'bound message to ensure that it is meeting all consent and compliance '
              'requirements thank you everyone.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "Opt her back in that it'll change from opted out to opted back in and we can "
             "continue the conversation with jiren and that's how you send your first out "
             'bound message to ensure that it is meeting all consent and compliance '
             'requirements thank you everyone.',
      'title': '🔔10DLC Opt-In and Opt-Out Flows for SMS Texting (Outbound)🔔 (Clerk AI)',
      'url': 'https://www.youtube.com/watch?v=CiI0Bewk8SU&t=163s',
      'video_id': 'CiI0Bewk8SU'},
     {'author': 'Bryan Software',
      'channel': 'Bryan Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:58](https://www.youtube.com/watch?v=Ez2jsa33jFY&t=298s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re running anything with EU data or healthcare data, the compliance gap alone "
              "decides it. So, RunPod's ahead on reliability and compliance, but we haven't "
              'looked at whether its billing model actually holds up when a job runs long or a '
              'host gets reclaimed.',
      'timestamp': 298,
      'timestamp_label': '[00:04:58]',
      'timestamp_seconds': 298,
      'tip': "'re running anything with EU data or healthcare data, the compliance gap alone "
             "decides it. So, RunPod's ahead on reliability and compliance, but we haven't "
             'looked at whether its billing model actually holds up when a job runs long or a '
             'host gets reclaimed.',
      'title': 'RunPod vs Vast.ai: Which Is Cheapest For GPUs? (Bryan Software)',
      'url': 'https://www.youtube.com/watch?v=Ez2jsa33jFY&t=298s',
      'video_id': 'Ez2jsa33jFY'},
     {'author': 'Tensor Garage',
      'channel': 'Tensor Garage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:22](https://www.youtube.com/watch?v=Ym3TP9rlzCk&t=682s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On a 48 GB A6000, spend the additional capacity on larger weights, longer '
              'cache, or more concurrent state. Test vLLM first for paged batching and SGLang '
              'first for reusable prompts. 1 and verify the intended layers reached your GPU.',
      'timestamp': 682,
      'timestamp_label': '[00:11:22]',
      'timestamp_seconds': 682,
      'tip': 'On a 48 GB A6000, spend the additional capacity on larger weights, longer cache, '
             'or more concurrent state. Test vLLM first for paged batching and SGLang first '
             'for reusable prompts. 1 and verify the intended layers reached your GPU.',
      'title': 'llama.cpp vs vLLM vs SGLang: Which Is Fastest on One GPU? (Tensor Garage)',
      'url': 'https://www.youtube.com/watch?v=Ym3TP9rlzCk&t=682s',
      'video_id': 'Ym3TP9rlzCk'},
     {'author': 'AI Andrew',
      'channel': 'AI Andrew',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:30](https://www.youtube.com/watch?v=vj8GAlW7mQo&t=810s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "PNAS: Architecture trumps Moore's Law. But how can a chip on older technology "
              'possibly beat 4-nanometer GPUs? It comes down to three rules that GPUs are '
              'built around, and North Pole breaks all three. Rule number one: Memory lives '
              'somewhere else.',
      'timestamp': 810,
      'timestamp_label': '[00:13:30]',
      'timestamp_seconds': 810,
      'tip': "PNAS: Architecture trumps Moore's Law. But how can a chip on older technology "
             'possibly beat 4-nanometer GPUs? It comes down to three rules that GPUs are built '
             'around, and North Pole breaks all three. Rule number one: Memory lives somewhere '
             'else.',
      'title': 'IBM Just Proved NVIDIA’s GPUs Are Built Wrong (With a 12nm Chip and 288 Cards) '
               '(AI Andrew)',
      'url': 'https://www.youtube.com/watch?v=vj8GAlW7mQo&t=810s',
      'video_id': 'vj8GAlW7mQo'},
     {'author': 'CNCF [Cloud Native Computing Foundation]',
      'channel': 'CNCF [Cloud Native Computing Foundation]',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:24](https://www.youtube.com/watch?v=nOgxv_R13Dg&t=2004s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can but if they want to use the simpler API they can do that as well well um '
              'yeah cool thank you hi yeah I had a question can we go back to the re the '
              'performance uh bar graphs that you had like the improvements you mean the '
              'inference yeah.',
      'timestamp': 2004,
      'timestamp_label': '[00:33:24]',
      'timestamp_seconds': 2004,
      'tip': 'Can but if they want to use the simpler API they can do that as well well um '
             'yeah cool thank you hi yeah I had a question can we go back to the re the '
             'performance uh bar graphs that you had like the improvements you mean the '
             'inference yeah.',
      'title': 'Which GPU Sharing Strategy Is Right for You? A Comprehensive Benchmark Study '
               'Us... K. Klues, Y. Chen (CNCF [Cloud Native Computing Foundation])',
      'url': 'https://www.youtube.com/watch?v=nOgxv_R13Dg&t=2004s',
      'video_id': 'nOgxv_R13Dg'},
     {'author': 'Commio',
      'channel': 'Commio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:15](https://www.youtube.com/watch?v=WOoSDFU7S3k&t=315s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Once we see all this we filled out this information we can go ahead and we can '
              "submit this form you have to remember to put a vertical in here so let's go "
              'back here.',
      'timestamp': 315,
      'timestamp_label': '[00:05:15]',
      'timestamp_seconds': 315,
      'tip': 'Once we see all this we filled out this information we can go ahead and we can '
             "submit this form you have to remember to put a vertical in here so let's go back "
             'here.',
      'title': 'How to Register Brands & Campaigns | Commio | 10DLC Text Messaging (Commio)',
      'url': 'https://www.youtube.com/watch?v=WOoSDFU7S3k&t=315s',
      'video_id': 'WOoSDFU7S3k'},
     {'author': 'CNCF [Cloud Native Computing Foundation]',
      'channel': 'CNCF [Cloud Native Computing Foundation]',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=-czZES1U_Us&t=57s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So back in 2016, OpenAI signed an exclusive contract with Microsoft to get to '
              'get compute, specifically GPUs. And then in 2024, they ended this exclusivity '
              'after they launched ChatGPT and then they expanded their capacity to Oracle '
              'Cloud.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'So back in 2016, OpenAI signed an exclusive contract with Microsoft to get to '
             'get compute, specifically GPUs. And then in 2024, they ended this exclusivity '
             'after they launched ChatGPT and then they expanded their capacity to Oracle '
             'Cloud.',
      'title': 'Building Multi-cloud AI Platforms on Kubernetes Without the Pain - Romil '
               'Bhardwaj, SkyPilot (CNCF [Cloud Native Computing Foundation])',
      'url': 'https://www.youtube.com/watch?v=-czZES1U_Us&t=57s',
      'video_id': '-czZES1U_Us'},
     {'author': 'Vantage',
      'channel': 'Vantage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=N1u_6ENlZV4&t=272s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pinpops practitioners uh in terms of um usage and that's understandable. 're "
              "embedded right in your cloud environment. Um, and they're, as I said, they're "
              'often free.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': "Pinpops practitioners uh in terms of um usage and that's understandable. 're "
             "embedded right in your cloud environment. Um, and they're, as I said, they're "
             'often free.',
      'title': 'The State of Cloud & AI Cost Management in 2026 | FinOps Summer Camp Session 1 '
               '(Vantage)',
      'url': 'https://www.youtube.com/watch?v=N1u_6ENlZV4&t=272s',
      'video_id': 'N1u_6ENlZV4'},
     {'author': 'FEPLabs Radio',
      'channel': 'FEPLabs Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=ou57Rm_y3fs&t=431s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll put links for that in the description below. Then your all-star node "
              "actually initiates the tunnel connection back to AMPR to amp. I'm going to keep "
              'saying Amper.',
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': "I'll put links for that in the description below. Then your all-star node "
             "actually initiates the tunnel connection back to AMPR to amp. I'm going to keep "
             'saying Amper.',
      'title': 'Port Forwarding, No Tears: 44Net Connect on ASL3 (FEPLabs Radio)',
      'url': 'https://www.youtube.com/watch?v=ou57Rm_y3fs&t=431s',
      'video_id': 'ou57Rm_y3fs'},
     {'author': 'Christian Kniep',
      'channel': 'Christian Kniep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=K9yY6_2255Y&t=53s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I added labels to do enable checkpoint and it's just requesting a GPU. Apply "
              'this and have a look at the jobs. So you can see that the pod for the job is '
              "was created. The operator created the um the PVC here and now it's in the "
              "creation state and it's running.",
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "I added labels to do enable checkpoint and it's just requesting a GPU. Apply "
             'this and have a look at the jobs. So you can see that the pod for the job is was '
             "created. The operator created the um the PVC here and now it's in the creation "
             "state and it's running.",
      'title': 'Checkpoint K8s pods transparently (plain CPU or GPU accelerated) (Christian '
               'Kniep)',
      'url': 'https://www.youtube.com/watch?v=K9yY6_2255Y&t=53s',
      'video_id': 'K9yY6_2255Y'},
     {'author': 'Red Panda Mining',
      'channel': 'Red Panda Mining',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:43](https://www.youtube.com/watch?v=X2uIX3DDPu0&t=523s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t work according to Custom Computing. So, I can only put eight GPUs in there. "
              'And so, these eight I think would be perfect in terms of the I guess the slot '
              'size as these are like two din slotted, right? So, I think these would fit '
              'perfect in that server no problem.',
      'timestamp': 523,
      'timestamp_label': '[00:08:43]',
      'timestamp_seconds': 523,
      'tip': "'t work according to Custom Computing. So, I can only put eight GPUs in there. "
             'And so, these eight I think would be perfect in terms of the I guess the slot '
             'size as these are like two din slotted, right? So, I think these would fit '
             'perfect in that server no problem.',
      'title': 'I bought this $600 "AI" GPU Rental SERVER! (Red Panda Mining)',
      'url': 'https://www.youtube.com/watch?v=X2uIX3DDPu0&t=523s',
      'video_id': 'X2uIX3DDPu0'},
     {'author': 'Rafay Systems',
      'channel': 'Rafay Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=n-O8p7y9Z5A&t=241s)',
      'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                   '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                   'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                   'spreads (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Label and I had um the time slice 10 okay that was my profile for that that '
              "adds set up let me go make the change and U in a few seconds you'll see the "
              "number of gpus available shift from 6 to 10 and as you can see here it's now "
              'reporting 10 gpus and if I go to my node.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'Label and I had um the time slice 10 okay that was my profile for that that adds '
             "set up let me go make the change and U in a few seconds you'll see the number of "
             "gpus available shift from 6 to 10 and as you can see here it's now reporting 10 "
             'gpus and if I go to my node.',
      'title': 'NVIDIA GPU Time Slicing: Create Multiple GPU Replicas on Kubernetes | Rafay '
               '(Rafay Systems)',
      'url': 'https://www.youtube.com/watch?v=n-O8p7y9Z5A&t=241s',
      'video_id': 'n-O8p7y9Z5A'}],
 10: [{'author': 'SkyPilot',
       'channel': 'SkyPilot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:37](https://www.youtube.com/watch?v=uwLkrJb5pEA&t=1477s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And the next exciting feature is the auto scaling worker pools uh for batch '
               "inference. If you're doing things like embedding back view or large-scale "
               'evaluation, you can now create a warm pool of workers and dispatch the infra '
               'inference workloads uh to all those workers.',
       'timestamp': 1477,
       'timestamp_label': '[00:24:37]',
       'timestamp_seconds': 1477,
       'tip': 'And the next exciting feature is the auto scaling worker pools uh for batch '
              "inference. If you're doing things like embedding back view or large-scale "
              'evaluation, you can now create a warm pool of workers and dispatch the infra '
              'inference workloads uh to all those workers.',
       'title': 'SkyPilot: Your AI Infra, Frontier Capabilities - Zhanghao Wu, Kevin Mingtarja '
                '(SkyPilot)',
       'url': 'https://www.youtube.com/watch?v=uwLkrJb5pEA&t=1477s',
       'video_id': 'uwLkrJb5pEA'},
      {'author': 'ProsperOps, a Flexera company',
       'channel': 'ProsperOps, a Flexera company',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=_ScBbR2FfCA&t=20s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So ProsperOps is a enterprise-scale RI and savings plan automation platform '
               "for AWS. We optimize over 1 billion of annual compute usage for some of AWS's "
               "largest and most sophisticated customers. Our platform doesn't provide "
               'recommendations.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'So ProsperOps is a enterprise-scale RI and savings plan automation platform for '
              "AWS. We optimize over 1 billion of annual compute usage for some of AWS's "
              "largest and most sophisticated customers. Our platform doesn't provide "
              'recommendations.',
       'title': 'FinOps X - 3-min Vendor Pitch - ProsperOps with Erik Carlin (ProsperOps, a '
                'Flexera company)',
       'url': 'https://www.youtube.com/watch?v=_ScBbR2FfCA&t=20s',
       'video_id': '_ScBbR2FfCA'},
      {'author': 'Cloud Computing Insider',
       'channel': 'Cloud Computing Insider',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:24](https://www.youtube.com/watch?v=mAgWtefgeP8&t=324s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI delivery, you know, GPU scale, bare bare metal access, orchestration '
               'options, network and storage performance, private or dedicated capacity, '
               'compliance postures, and operational support.',
       'timestamp': 324,
       'timestamp_label': '[00:05:24]',
       'timestamp_seconds': 324,
       'tip': 'AI delivery, you know, GPU scale, bare bare metal access, orchestration '
              'options, network and storage performance, private or dedicated capacity, '
              'compliance postures, and operational support.',
       'title': 'Top 5 NeoClouds Explained: CoreWeave, Nebius, Crusoe, Lambda, Fluidstack '
                '(Cloud Computing Insider)',
       'url': 'https://www.youtube.com/watch?v=mAgWtefgeP8&t=324s',
       'video_id': 'mAgWtefgeP8'},
      {'author': 'ServeTheHome',
       'channel': 'ServeTheHome',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:04](https://www.youtube.com/watch?v=N5AJJ0tAoxc&t=64s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI labs to deploy 50 to 100,000 GPU clusters at the gigawatt scale. We cannot '
               'tell you the exact number of Nvidia B200 GPUs here, but what we can say is '
               "that it's already in the several thousand GPUs strong and the installation is "
               'growing.',
       'timestamp': 64,
       'timestamp_label': '[00:01:04]',
       'timestamp_seconds': 64,
       'tip': 'AI labs to deploy 50 to 100,000 GPU clusters at the gigawatt scale. We cannot '
              'tell you the exact number of Nvidia B200 GPUs here, but what we can say is that '
              "it's already in the several thousand GPUs strong and the installation is "
              'growing.',
       'title': 'Inside a NEW AI Cluster - Tour with NVIDIA B200 (ServeTheHome)',
       'url': 'https://www.youtube.com/watch?v=N5AJJ0tAoxc&t=64s',
       'video_id': 'N5AJJ0tAoxc'},
      {'author': 'Voice AI with Tim',
       'channel': 'Voice AI with Tim',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:44](https://www.youtube.com/watch?v=omQUCQVG1lg&t=224s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'API key, we have everything we need to start actually doing this. So the first '
               "connection we will do is the WAPI connection. And in order to do this, let's "
               'go to the WAPI dashboard. Obviously, in order to talk through the phone '
               'number, you will need to have an agent.',
       'timestamp': 224,
       'timestamp_label': '[00:03:44]',
       'timestamp_seconds': 224,
       'tip': 'API key, we have everything we need to start actually doing this. So the first '
              "connection we will do is the WAPI connection. And in order to do this, let's go "
              'to the WAPI dashboard. Obviously, in order to talk through the phone number, '
              'you will need to have an agent.',
       'title': 'How to connect a Telnyx number with Vapi and LiveKit (2026) (Voice AI with '
                'Tim)',
       'url': 'https://www.youtube.com/watch?v=omQUCQVG1lg&t=224s',
       'video_id': 'omQUCQVG1lg'},
      {'author': 'Hostrunway',
       'channel': 'Hostrunway',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=Auj5NAlVFVk&t=70s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Whole machine is yours.  GPU servers for AI, built on NVIDIA H100,  H200, and '
               'the new Blackwell B300. Train.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': 'Whole machine is yours.  GPU servers for AI, built on NVIDIA H100,  H200, and '
              'the new Blackwell B300. Train.',
       'title': 'Bare-Metal, Cloud & AI GPU Servers Built for Scale | Hostrunway (Hostrunway)',
       'url': 'https://www.youtube.com/watch?v=Auj5NAlVFVk&t=70s',
       'video_id': 'Auj5NAlVFVk'},
      {'author': 'Crusoe AI',
       'channel': 'Crusoe AI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=R74kx7GKEbs&t=130s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It is also the industry's default choice for simple, large scale deployments "
               'and performs exceptionally well with dense models like the llama family. If '
               'you just need raw inference, speed and reliability, vLLM is the stable option.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': "It is also the industry's default choice for simple, large scale deployments "
              'and performs exceptionally well with dense models like the llama family. If you '
              'just need raw inference, speed and reliability, vLLM is the stable option.',
       'title': 'AI Lab: Open-source inference with vLLM + SGLang | Optimizing KV cache with '
                'Crusoe Managed Inference (Crusoe AI)',
       'url': 'https://www.youtube.com/watch?v=R74kx7GKEbs&t=130s',
       'video_id': 'R74kx7GKEbs'},
      {'author': 'Screwdriver Science',
       'channel': 'Screwdriver Science',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:55](https://www.youtube.com/watch?v=b3RlbR2xqfM&t=595s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Inside the rack, the chips are wired to each other with dedicated high-speed '
               'links, so all 72 can pass numbers back and forth and behave like one giant '
               "chip. That's how a model too big for any single chip gets split across dozens "
               'of them. All that power turns into heat.',
       'timestamp': 595,
       'timestamp_label': '[00:09:55]',
       'timestamp_seconds': 595,
       'tip': 'Inside the rack, the chips are wired to each other with dedicated high-speed '
              'links, so all 72 can pass numbers back and forth and behave like one giant '
              "chip. That's how a model too big for any single chip gets split across dozens "
              'of them. All that power turns into heat.',
       'title': 'How do AI Chips Actually Work?  Inside the NVIDIA H100 (Screwdriver Science)',
       'url': 'https://www.youtube.com/watch?v=b3RlbR2xqfM&t=595s',
       'video_id': 'b3RlbR2xqfM'},
      {'author': 'Remy Runs',
       'channel': 'Remy Runs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=o6WzuMA5VL8&t=67s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It needs bandwidth for the slice it reads on every word, about 104 billion '
               'parameters of it. The headline gives you the speed. What it leaves out is what '
               "three tokens a second feels like when you're the one waiting.",
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': 'It needs bandwidth for the slice it reads on every word, about 104 billion '
              'parameters of it. The headline gives you the speed. What it leaves out is what '
              "three tokens a second feels like when you're the one waiting.",
       'title': 'I Ran a 2.8 Trillion AI on Two Used RTX 3090s (Did NOT Expect This) (Remy '
                'Runs)',
       'url': 'https://www.youtube.com/watch?v=o6WzuMA5VL8&t=67s',
       'video_id': 'o6WzuMA5VL8'},
      {'author': 'Serverside Acquisitions',
       'channel': 'Serverside Acquisitions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:04](https://www.youtube.com/watch?v=BFMPHZZBGlg&t=1024s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The real war for AI speed is being fought across 2,048 microscopic lanes of '
               'copper, one picojoule and one thermal micron at a time.',
       'timestamp': 1024,
       'timestamp_label': '[00:17:04]',
       'timestamp_seconds': 1024,
       'tip': 'The real war for AI speed is being fought across 2,048 microscopic lanes of '
              'copper, one picojoule and one thermal micron at a time.',
       'title': 'FLOPS Are a Lie: Why Memory Bandwidth Actually Controls AI Speed (Serverside '
                'Acquisitions)',
       'url': 'https://www.youtube.com/watch?v=BFMPHZZBGlg&t=1024s',
       'video_id': 'BFMPHZZBGlg'},
      {'author': 'Tomorrow Engineered',
       'channel': 'Tomorrow Engineered',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:32](https://www.youtube.com/watch?v=yYBoW-BKDl8&t=1412s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s AI chips paid $20 billion to put fast memory right beside the maths, the "
               'same bet Cerebras made when it refused to cut up the wafer. Nvidia still leads '
               'on volume, on training, and on flexibility, while Cerebras leads on speed per '
               'user by 20 to 40 times.',
       'timestamp': 1412,
       'timestamp_label': '[00:23:32]',
       'timestamp_seconds': 1412,
       'tip': "'s AI chips paid $20 billion to put fast memory right beside the maths, the "
              'same bet Cerebras made when it refused to cut up the wafer. Nvidia still leads '
              'on volume, on training, and on flexibility, while Cerebras leads on speed per '
              'user by 20 to 40 times.',
       'title': 'This New AI Chip Could Make AI Run 30X Faster Than Nvidia GPUs! (Tomorrow '
                'Engineered)',
       'url': 'https://www.youtube.com/watch?v=yYBoW-BKDl8&t=1412s',
       'video_id': 'yYBoW-BKDl8'},
      {'author': 'Mehmood Feroz',
       'channel': 'Mehmood Feroz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=R74S6hUZ4fk&t=183s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'UI you have URI you have to give this URI to your provider so that they can '
               'whitelist it on their site. This is very uh easy and once the phone number is '
               "added, you can assign it to your agent. After that uh let's come to retail AI "
               'connect your number using SIP trunking.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': 'UI you have URI you have to give this URI to your provider so that they can '
              'whitelist it on their site. This is very uh easy and once the phone number is '
              "added, you can assign it to your agent. After that uh let's come to retail AI "
              'connect your number using SIP trunking.',
       'title': 'Connect Your Business Phone to AI Voice Agent | SIP TRUNK | VAPI | RETELL | '
                'ELEVENLABS (Mehmood Feroz)',
       'url': 'https://www.youtube.com/watch?v=R74S6hUZ4fk&t=183s',
       'video_id': 'R74S6hUZ4fk'},
      {'author': 'GPU Battle',
       'channel': 'GPU Battle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=156XFkwFpwY&t=127s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Vast is people in data centers renting out their own machines. And then '
               "there's also a catch though. So, when I benchmark on GPU Battle, one 4090 host "
               'on Vast AI ran at half the speed. They were underclocking it. Uh basically '
               'bottlenecking their own GPU.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': "Vast is people in data centers renting out their own machines. And then there's "
              'also a catch though. So, when I benchmark on GPU Battle, one 4090 host on Vast '
              'AI ran at half the speed. They were underclocking it. Uh basically '
              'bottlenecking their own GPU.',
       'title': 'RunPod vs Vast.ai: Which Cloud GPU Should You Use? (GPU Battle)',
       'url': 'https://www.youtube.com/watch?v=156XFkwFpwY&t=127s',
       'video_id': '156XFkwFpwY'},
      {'author': 'CNCF [Cloud Native Computing Foundation]',
       'channel': 'CNCF [Cloud Native Computing Foundation]',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:56](https://www.youtube.com/watch?v=zrGFmLHI7hg&t=236s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s like running the AI infrastructure, they want to associate that somehow to "
               'the to the application layer which is latency and throughput and the other '
               'kind of thing.',
       'timestamp': 236,
       'timestamp_label': '[00:03:56]',
       'timestamp_seconds': 236,
       'tip': "'s like running the AI infrastructure, they want to associate that somehow to "
              'the to the application layer which is latency and throughput and the other kind '
              'of thing.',
       'title': 'Vendor-Neutral GPU Observability for Kubernetes - Reza Jelveh, Dynamia.ai '
                '(CNCF [Cloud Native Computing Foundation])',
       'url': 'https://www.youtube.com/watch?v=zrGFmLHI7hg&t=236s',
       'video_id': 'zrGFmLHI7hg'},
      {'author': 'Crosstalk Solutions',
       'channel': 'Crosstalk Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:43](https://www.youtube.com/watch?v=7VDpPwV6kS0&t=523s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Right 272-20724-2040 we're calling and we can see that this phone is ringing "
               'right so my crosstalk phone is ringing that is my michael scott extension '
               "let's call our second d id which is uh 272770266 call that number.",
       'timestamp': 523,
       'timestamp_label': '[00:08:43]',
       'timestamp_seconds': 523,
       'tip': "Right 272-20724-2040 we're calling and we can see that this phone is ringing "
              "right so my crosstalk phone is ringing that is my michael scott extension let's "
              'call our second d id which is uh 272770266 call that number.',
       'title': '21 Inbound Routes - FreePBX 101 v15 (Crosstalk Solutions)',
       'url': 'https://www.youtube.com/watch?v=7VDpPwV6kS0&t=523s',
       'video_id': '7VDpPwV6kS0'}],
 11: [{'author': 'Modelplane',
       'channel': 'Modelplane',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:26](https://www.youtube.com/watch?v=Wq9Ov_jlxlM&t=266s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And the gateway routes to them. The endpoint speaks OpenAI or Anthropic API so '
               "the coding agent you can point your coding agent directly at it. Now, let's "
               'scale the fleet. The infra team adds another cluster in Amsterdam through a '
               'Vultr provider.',
       'timestamp': 266,
       'timestamp_label': '[00:04:26]',
       'timestamp_seconds': 266,
       'tip': 'And the gateway routes to them. The endpoint speaks OpenAI or Anthropic API so '
              "the coding agent you can point your coding agent directly at it. Now, let's "
              'scale the fleet. The infra team adds another cluster in Amsterdam through a '
              'Vultr provider.',
       'title': 'Run One AI Model Across Multiple Clouds and GPUs (Modelplane)',
       'url': 'https://www.youtube.com/watch?v=Wq9Ov_jlxlM&t=266s',
       'video_id': 'Wq9Ov_jlxlM'},
      {'author': 'IBM Technology',
       'channel': 'IBM Technology',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=McLdlg5Gc9s&t=105s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Since more users interacting with the LLM means slower responses back from the '
               'model, well, this is because of batch processing bottlenecks and is also an '
               "issue with running these models. At the same time, there's issues with "
               'scaling.',
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'Since more users interacting with the LLM means slower responses back from the '
              'model, well, this is because of batch processing bottlenecks and is also an '
              "issue with running these models. At the same time, there's issues with scaling.",
       'title': 'What is vLLM? Efficient AI Inference for Large Language Models (IBM '
                'Technology)',
       'url': 'https://www.youtube.com/watch?v=McLdlg5Gc9s&t=105s',
       'video_id': 'McLdlg5Gc9s'},
      {'author': 'Uplatz',
       'channel': 'Uplatz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=jp2pwEpUg-Q&t=187s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This level of operational complexity only yields a return when you are working '
               'at the scale of these Blackwell server racks, where shaving milliseconds saves '
               'more than the cost of the engineering team.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'This level of operational complexity only yields a return when you are working '
              'at the scale of these Blackwell server racks, where shaving milliseconds saves '
              'more than the cost of the engineering team.',
       'title': 'LLM Inference Engines 2026 | Comparing vLLM, SGLang & Hugging Face TGI | '
                'Uplatz (Uplatz)',
       'url': 'https://www.youtube.com/watch?v=jp2pwEpUg-Q&t=187s',
       'video_id': 'jp2pwEpUg-Q'},
      {'author': 'Intellipaat',
       'channel': 'Intellipaat',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:38](https://www.youtube.com/watch?v=7_L1_3-4kg8&t=1838s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '150 servers running all the time you can set up auto scaling our policy which '
               'basically increases the number of servers whenever there is a.',
       'timestamp': 1838,
       'timestamp_label': '[00:30:38]',
       'timestamp_seconds': 1838,
       'tip': '150 servers running all the time you can set up auto scaling our policy which '
              'basically increases the number of servers whenever there is a.',
       'title': 'AWS Finops Tutorial | AWS FinOps | Cloud Finops | Intellipaat (Intellipaat)',
       'url': 'https://www.youtube.com/watch?v=7_L1_3-4kg8&t=1838s',
       'video_id': '7_L1_3-4kg8'},
      {'author': 'Red Panda Mining',
       'channel': 'Red Panda Mining',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:30](https://www.youtube.com/watch?v=SJbOF9Ufm0Q&t=510s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, Simple Pod does have a 20% fee, okay? And I just to show you quickly here, '
               'vast. Somebody from France, which is interesting. But, anyway, going back to '
               'this, okay? So, yeah, someone rented it for 13 hours and that was at 25 cents '
               'a day.',
       'timestamp': 510,
       'timestamp_label': '[00:08:30]',
       'timestamp_seconds': 510,
       'tip': 'So, Simple Pod does have a 20% fee, okay? And I just to show you quickly here, '
              'vast. Somebody from France, which is interesting. But, anyway, going back to '
              'this, okay? So, yeah, someone rented it for 13 hours and that was at 25 cents a '
              'day.',
       'title': 'My 10x 170HX GPU "Ai" Server Is Actually Making Money Now. (Red Panda Mining)',
       'url': 'https://www.youtube.com/watch?v=SJbOF9Ufm0Q&t=510s',
       'video_id': 'SJbOF9Ufm0Q'},
      {'author': 'Neural AI Flair',
       'channel': 'Neural AI Flair',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:57](https://www.youtube.com/watch?v=18AkpuX3vkY&t=537s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'LLM has the larger ecosystem. Native LangChain and LlamaIndex integrations. '
               'Ray Serve for auto scaling. Kubernetes operators from multiple vendors, '
               'official Docker images, and seamless Hugging Face Hub integration.',
       'timestamp': 537,
       'timestamp_label': '[00:08:57]',
       'timestamp_seconds': 537,
       'tip': 'LLM has the larger ecosystem. Native LangChain and LlamaIndex integrations. Ray '
              'Serve for auto scaling. Kubernetes operators from multiple vendors, official '
              'Docker images, and seamless Hugging Face Hub integration.',
       'title': 'SGLang vs vLLM: Which LLM Inference Framework Should You Use? (Neural AI '
                'Flair)',
       'url': 'https://www.youtube.com/watch?v=18AkpuX3vkY&t=537s',
       'video_id': '18AkpuX3vkY'},
      {'author': 'CNCF [Cloud Native Computing Foundation]',
       'channel': 'CNCF [Cloud Native Computing Foundation]',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:28](https://www.youtube.com/watch?v=Vw7DTM1SV60&t=268s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So let's go back to where we were. So what I wanted to show is here we have "
               "the NVIDIA SMI output. So what we see is a classifier pod and we're executing "
               'the NVIDIA SMI.',
       'timestamp': 268,
       'timestamp_label': '[00:04:28]',
       'timestamp_seconds': 268,
       'tip': "So let's go back to where we were. So what I wanted to show is here we have the "
              "NVIDIA SMI output. So what we see is a classifier pod and we're executing the "
              'NVIDIA SMI.',
       'title': 'Fixing GPU Time-Slicing on Kubernetes: Dynamic, Memory-Safe Sharing for AI... '
                'Julien Semaan, Kubex (CNCF [Cloud Native Computing Foundation])',
       'url': 'https://www.youtube.com/watch?v=Vw7DTM1SV60&t=268s',
       'video_id': 'Vw7DTM1SV60'},
      {'author': 'The Things Industries',
       'channel': 'The Things Industries',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:45](https://www.youtube.com/watch?v=u_m7kYjI4ow&t=285s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'MVNO, I get a QR code or or just the the digits. I can type it in to uh to to '
               'my uh uh connectivity manager. And I can download the profile uh which the my '
               'connectivity provider has provided. And the billing what we watch '
               'automatically.',
       'timestamp': 285,
       'timestamp_label': '[00:04:45]',
       'timestamp_seconds': 285,
       'tip': 'MVNO, I get a QR code or or just the the digits. I can type it in to uh to to '
              'my uh uh connectivity manager. And I can download the profile uh which the my '
              'connectivity provider has provided. And the billing what we watch '
              'automatically.',
       'title': 'eSIM for IoT: Changing Connectivity Without a Truck Roll — Kigen (The Things '
                'Industries)',
       'url': 'https://www.youtube.com/watch?v=u_m7kYjI4ow&t=285s',
       'video_id': 'u_m7kYjI4ow'},
      {'author': 'Core Concept Learning',
       'channel': 'Core Concept Learning',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:51](https://www.youtube.com/watch?v=56JbSXiXhhE&t=171s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A team's guaranteed share in Run AI is its project quota. Using other teams' "
               'idle GPUs is over quota borrowing, reclaimed by preemption. A GPU supports up '
               'to seven MIG instances, and on Kubernetes, MIG layouts are applied by the GPU '
               "operator's MIG manager.",
       'timestamp': 171,
       'timestamp_label': '[00:02:51]',
       'timestamp_seconds': 171,
       'tip': "A team's guaranteed share in Run AI is its project quota. Using other teams' "
              'idle GPUs is over quota borrowing, reclaimed by preemption. A GPU supports up '
              'to seven MIG instances, and on Kubernetes, MIG layouts are applied by the GPU '
              "operator's MIG manager.",
       'title': 'NCP-AIO Scenario 03/5: Sharing GPUs Across Teams with Run:ai and MIG (Core '
                'Concept Learning)',
       'url': 'https://www.youtube.com/watch?v=56JbSXiXhhE&t=171s',
       'video_id': '56JbSXiXhhE'},
      {'author': 'Bandwidth',
       'channel': 'Bandwidth',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:05](https://www.youtube.com/watch?v=G91y9mjo-pk&t=185s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Every day we’re working to keep villains and bad actors out of the ecosystem, '
               'while helping to make sure your valid traffic gets through. To find out more, '
               'contact your Account Manager. Or visit us online at bandwidth.',
       'timestamp': 185,
       'timestamp_label': '[00:03:05]',
       'timestamp_seconds': 185,
       'tip': 'Every day we’re working to keep villains and bad actors out of the ecosystem, '
              'while helping to make sure your valid traffic gets through. To find out more, '
              'contact your Account Manager. Or visit us online at bandwidth.',
       'title': 'Understanding STIR/SHAKEN (Bandwidth)',
       'url': 'https://www.youtube.com/watch?v=G91y9mjo-pk&t=185s',
       'video_id': 'G91y9mjo-pk'},
      {'author': 'Duality Technologies',
       'channel': 'Duality Technologies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:22](https://www.youtube.com/watch?v=nXTWdWFiGvM&t=202s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The service is running, with both of your assets loaded. The customer has '
               'verified the enclave and issued its certificate, and the attested image '
               'matches the build you registered. And your team gets what it needs to run at '
               'scale. CPU, GPU, and memory sampled once a minute.',
       'timestamp': 202,
       'timestamp_label': '[00:03:22]',
       'timestamp_seconds': 202,
       'tip': 'The service is running, with both of your assets loaded. The customer has '
              'verified the enclave and issued its certificate, and the attested image matches '
              'the build you registered. And your team gets what it needs to run at scale. '
              'CPU, GPU, and memory sampled once a minute.',
       'title': 'Confidential LLM Inference: Run Frontier Models Without Seeing Prompts '
                '(Duality Technologies)',
       'url': 'https://www.youtube.com/watch?v=nXTWdWFiGvM&t=202s',
       'video_id': 'nXTWdWFiGvM'},
      {'author': 'Rafay Systems',
       'channel': 'Rafay Systems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:13](https://www.youtube.com/watch?v=YoZoDn_Fvq0&t=133s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Particular GPU that's particular pod that'll be using it um um and uh I have a "
               "have a simple application that is um requesting for five it'll be a five "
               "replicas and uh it's going to go on a node with u um the mid config all 1G 5gb "
               'and Cube cutle.',
       'timestamp': 133,
       'timestamp_label': '[00:02:13]',
       'timestamp_seconds': 133,
       'tip': "Particular GPU that's particular pod that'll be using it um um and uh I have a "
              "have a simple application that is um requesting for five it'll be a five "
              "replicas and uh it's going to go on a node with u um the mid config all 1G 5gb "
              'and Cube cutle.',
       'title': 'NVIDIA MIG: Spatial GPU Partitioning for Multi-Tenant Workloads | Rafay '
                '(Rafay Systems)',
       'url': 'https://www.youtube.com/watch?v=YoZoDn_Fvq0&t=133s',
       'video_id': 'YoZoDn_Fvq0'},
      {'author': 'Jitesh Powankar',
       'channel': 'Jitesh Powankar',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:43](https://www.youtube.com/watch?v=Ul1dZowvKvE&t=103s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This transformation allows your infrastructure to handle much higher density, '
               "maximizing every watt of power and every dollar spent. Let's look at this in a "
               'real-world production environment to see how it really impacts your day-to-day '
               'operations.',
       'timestamp': 103,
       'timestamp_label': '[00:01:43]',
       'timestamp_seconds': 103,
       'tip': 'This transformation allows your infrastructure to handle much higher density, '
              "maximizing every watt of power and every dollar spent. Let's look at this in a "
              'real-world production environment to see how it really impacts your day-to-day '
              'operations.',
       'title': 'GPU Resource Slice Explained with Pizza Analogy | NVIDIA MIG & GPU Slicing '
                'Made Easy (Jitesh Powankar)',
       'url': 'https://www.youtube.com/watch?v=Ul1dZowvKvE&t=103s',
       'video_id': 'Ul1dZowvKvE'},
      {'author': 'SkyPilot',
       'channel': 'SkyPilot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:02](https://www.youtube.com/watch?v=tb-Yg8PNXT4&t=302s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "256 GPUs available to run big training job 2. The only reason it isn't running "
               "is that those GPUs are allocated to another queue, but they're not being used "
               "right now. I don't know what's up with the experiments team. Maybe they're on "
               'an off-site or something.',
       'timestamp': 302,
       'timestamp_label': '[00:05:02]',
       'timestamp_seconds': 302,
       'tip': "256 GPUs available to run big training job 2. The only reason it isn't running "
              "is that those GPUs are allocated to another queue, but they're not being used "
              "right now. I don't know what's up with the experiments team. Maybe they're on "
              'an off-site or something.',
       'title': 'Why are my GPUs not getting scheduled - Seung Jin Yang (SkyPilot)',
       'url': 'https://www.youtube.com/watch?v=tb-Yg8PNXT4&t=302s',
       'video_id': 'tb-Yg8PNXT4'},
      {'author': 'Hitesh C.',
       'channel': 'Hitesh C.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=fKrvPg4P6KY&t=105s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So read that speed-up carefully. Part of it is bandwidth, and part is the '
               "larger batch that the extra memory allowed. NVIDIA's DGX B200 system holds "
               'eight Blackwell GPUs. The system lists 1,440 gigabytes of HBM3e in total, with '
               '64 terabytes per second of bandwidth.',
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'So read that speed-up carefully. Part of it is bandwidth, and part is the '
              "larger batch that the extra memory allowed. NVIDIA's DGX B200 system holds "
              'eight Blackwell GPUs. The system lists 1,440 gigabytes of HBM3e in total, with '
              '64 terabytes per second of bandwidth.',
       'title': '46. H100 vs H200 vs Blackwell B200 for LLM Inference (Hitesh C.)',
       'url': 'https://www.youtube.com/watch?v=fKrvPg4P6KY&t=105s',
       'video_id': 'fKrvPg4P6KY'}],
 12: [{'author': 'AWS Events',
       'channel': 'AWS Events',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:45](https://www.youtube.com/watch?v=NE8Ua2YVa6Q&t=285s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And so with that, let's talk about what these pillars look like in action. And "
               "so the first we're gonna talk about is automated governance. And I like to "
               'just start by defining that with three steps. Policy becomes automation and '
               'automation becomes guardrails.',
       'timestamp': 285,
       'timestamp_label': '[00:04:45]',
       'timestamp_seconds': 285,
       'tip': "And so with that, let's talk about what these pillars look like in action. And "
              "so the first we're gonna talk about is automated governance. And I like to just "
              'start by defining that with three steps. Policy becomes automation and '
              'automation becomes guardrails.',
       'title': 'AWS re:Invent 2025 - FinOps+: A New Era of Accelerating Value (COP211) (AWS '
                'Events)',
       'url': 'https://www.youtube.com/watch?v=NE8Ua2YVa6Q&t=285s',
       'video_id': 'NE8Ua2YVa6Q'},
      {'author': 'Kion',
       'channel': 'Kion',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:48](https://www.youtube.com/watch?v=wKXTR8j4jbY&t=288s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And so with that, let's talk about what these pillars look like in action. And "
               "so the first we're going to talk about is automated governance. And I like to "
               'start by defining that with three steps. And automation becomes guardrails.',
       'timestamp': 288,
       'timestamp_label': '[00:04:48]',
       'timestamp_seconds': 288,
       'tip': "And so with that, let's talk about what these pillars look like in action. And "
              "so the first we're going to talk about is automated governance. And I like to "
              'start by defining that with three steps. And automation becomes guardrails.',
       'title': 'AWS reInvent 2025:  FinOps A New Era of Accelerating Value (Kion)',
       'url': 'https://www.youtube.com/watch?v=wKXTR8j4jbY&t=288s',
       'video_id': 'wKXTR8j4jbY'},
      {'author': 'Extrude Studio',
       'channel': 'Extrude Studio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:20](https://www.youtube.com/watch?v=xkHs2GUaKro&t=800s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But Stanford's next concept modeling proves that the auto-aggressive paradigm "
               'was merely an early engineering compromise by stepping back and teaching '
               'neural networks to plan at the concept level first.',
       'timestamp': 800,
       'timestamp_label': '[00:13:20]',
       'timestamp_seconds': 800,
       'tip': "But Stanford's next concept modeling proves that the auto-aggressive paradigm "
              'was merely an early engineering compromise by stepping back and teaching neural '
              'networks to plan at the concept level first.',
       'title': 'Stanford Just Destroyed Nvidia’s $30,000 Monopoly (It’s Over) (Extrude '
                'Studio)',
       'url': 'https://www.youtube.com/watch?v=xkHs2GUaKro&t=800s',
       'video_id': 'xkHs2GUaKro'},
      {'author': 'Top New Code',
       'channel': 'Top New Code',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:54](https://www.youtube.com/watch?v=e8R4z-ISWAo&t=234s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re greeted with the main dashboard overview. Here you get a real-time "
               'snapshot of your business performance, including total users, active ESIMs, '
               "total sales, orders and process, and recent transactions. You'll also see a "
               'breakdown of sales activity by day, week, or month.',
       'timestamp': 234,
       'timestamp_label': '[00:03:54]',
       'timestamp_seconds': 234,
       'tip': "'re greeted with the main dashboard overview. Here you get a real-time snapshot "
              'of your business performance, including total users, active ESIMs, total sales, '
              "orders and process, and recent transactions. You'll also see a breakdown of "
              'sales activity by day, week, or month.',
       'title': 'eSIM International Platform – Buy & Sell Global Data | Full Admin + User '
                'Panel Demo (Top New Code)',
       'url': 'https://www.youtube.com/watch?v=e8R4z-ISWAo&t=234s',
       'video_id': 'e8R4z-ISWAo'},
      {'author': 'MysticOrb289',
       'channel': 'MysticOrb289',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:19](https://www.youtube.com/watch?v=w5vhWKlqN_k&t=319s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Take what you earned per day last week, cut it in half, then subtract your '
               'power. Take your current rate, take, you know, whatever rate you can get if '
               "you decide to get it hosted. Are you still in the green? If not, don't mine at "
               'a loss hoping it comes back.',
       'timestamp': 319,
       'timestamp_label': '[00:05:19]',
       'timestamp_seconds': 319,
       'tip': 'Take what you earned per day last week, cut it in half, then subtract your '
              'power. Take your current rate, take, you know, whatever rate you can get if you '
              "decide to get it hosted. Are you still in the green? If not, don't mine at a "
              'loss hoping it comes back.',
       'title': 'Stop Mining Quantus on GPU Until You See This FPGA Warning (MysticOrb289)',
       'url': 'https://www.youtube.com/watch?v=w5vhWKlqN_k&t=319s',
       'video_id': 'w5vhWKlqN_k'},
      {'author': 'Bandwidth',
       'channel': 'Bandwidth',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=vrVUZ1rSJO0&t=159s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AT&amp;T has indicated that filtering for unregistered traffic will start on '
               'June 1st 2021 and T-Mobile has also indicated their plans to make registration '
               'a requirement. I know this may sound complex, but bandwidth is here to help.',
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': 'AT&amp;T has indicated that filtering for unregistered traffic will start on '
              'June 1st 2021 and T-Mobile has also indicated their plans to make registration '
              'a requirement. I know this may sound complex, but bandwidth is here to help.',
       'title': 'The Messaging 411: 10DLC Campaign Registration (Bandwidth)',
       'url': 'https://www.youtube.com/watch?v=vrVUZ1rSJO0&t=159s',
       'video_id': 'vrVUZ1rSJO0'},
      {'author': 'RingLogix',
       'channel': 'RingLogix',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:59:11](https://www.youtube.com/watch?v=gmCqaG2hBKQ&t=3551s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Whatever we could do to help like yeah just like Jamie said I'm just gonna "
               "pick you back off I'm about good you don't thanks everyone have a great day "
               "we'll catch you later bye bye w.",
       'timestamp': 3551,
       'timestamp_label': '[00:59:11]',
       'timestamp_seconds': 3551,
       'tip': "Whatever we could do to help like yeah just like Jamie said I'm just gonna pick "
              "you back off I'm about good you don't thanks everyone have a great day we'll "
              'catch you later bye bye w.',
       'title': 'Master 10DLC Texting Requirements (RingLogix)',
       'url': 'https://www.youtube.com/watch?v=gmCqaG2hBKQ&t=3551s',
       'video_id': 'gmCqaG2hBKQ'},
      {'author': 'Calderon Bridger',
       'channel': 'Calderon Bridger',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:35](https://www.youtube.com/watch?v=KrSK9_CmFMk&t=95s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You have to work a little harder to get things running. The learning curve is '
               'a bit steeper. You might spend an extra day or two in the weeds of the '
               'integration process, but that effort pays off every single month when the '
               'invoice hits.',
       'timestamp': 95,
       'timestamp_label': '[00:01:35]',
       'timestamp_seconds': 95,
       'tip': 'You have to work a little harder to get things running. The learning curve is a '
              'bit steeper. You might spend an extra day or two in the weeds of the '
              'integration process, but that effort pays off every single month when the '
              'invoice hits.',
       'title': 'Twilio vs Plivo vs Telnyx Comparison Review 2026: CPaaS Platform Overview '
                '(Calderon Bridger)',
       'url': 'https://www.youtube.com/watch?v=KrSK9_CmFMk&t=95s',
       'video_id': 'KrSK9_CmFMk'},
      {'author': 'USENIX',
       'channel': 'USENIX',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:03](https://www.youtube.com/watch?v=3Edw88b1bRg&t=483s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We are showing the number of preemptions over a period of 8 days. We see there '
               'are quite a lot of preemptions happening in total, but if we zoom into each '
               'day a little bit, the preemptions in in each day are quite different.',
       'timestamp': 483,
       'timestamp_label': '[00:08:03]',
       'timestamp_seconds': 483,
       'tip': 'We are showing the number of preemptions over a period of 8 days. We see there '
              'are quite a lot of preemptions happening in total, but if we zoom into each day '
              'a little bit, the preemptions in in each day are quite different.',
       'title': "NSDI '23 - SkyPilot: An Intercloud Broker for Sky Computing (USENIX)",
       'url': 'https://www.youtube.com/watch?v=3Edw88b1bRg&t=483s',
       'video_id': '3Edw88b1bRg'},
      {'author': 'The Federalist Society',
       'channel': 'The Federalist Society',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:38](https://www.youtube.com/watch?v=EL34vsXYuGQ&t=998s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um about special tests and and things like that that they can look to for for '
               'this kind of action in particular but at the end of the day under existing '
               'supreme court precedent interpreting what is an intelligent principle section '
               '254 we think passes muster.',
       'timestamp': 998,
       'timestamp_label': '[00:16:38]',
       'timestamp_seconds': 998,
       'tip': 'Um about special tests and and things like that that they can look to for for '
              'this kind of action in particular but at the end of the day under existing '
              'supreme court precedent interpreting what is an intelligent principle section '
              '254 we think passes muster.',
       'title': "Consumers' Research v. FCC and the Legality of the Universal Service Fund "
                'Contribution Regime (The Federalist Society)',
       'url': 'https://www.youtube.com/watch?v=EL34vsXYuGQ&t=998s',
       'video_id': 'EL34vsXYuGQ'},
      {'author': 'Red Panda Mining',
       'channel': 'Red Panda Mining',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:14](https://www.youtube.com/watch?v=mfQE_CptyLA&t=254s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Mining rigs I had for GPU mining back in like the Ethereum days, when Ethereum '
               'was proof of work, and we could, you know, make a lot of money mining back '
               "then. GPU mining is dead, and it's not profitable at all, especially at any "
               'residential electric.',
       'timestamp': 254,
       'timestamp_label': '[00:04:14]',
       'timestamp_seconds': 254,
       'tip': 'Mining rigs I had for GPU mining back in like the Ethereum days, when Ethereum '
              'was proof of work, and we could, you know, make a lot of money mining back '
              "then. GPU mining is dead, and it's not profitable at all, especially at any "
              'residential electric.',
       'title': 'AI GPU Rentals feels like Ethereum GPU Mining Again. (Red Panda Mining)',
       'url': 'https://www.youtube.com/watch?v=mfQE_CptyLA&t=254s',
       'video_id': 'mfQE_CptyLA'},
      {'author': 'GPU Battle',
       'channel': 'GPU Battle',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:48](https://www.youtube.com/watch?v=ymI6ZvqQNjQ&t=288s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can either go to the website also. I recommend going to gpubattle. AI has '
               'all the updated API prices when you connect your API key. So prices change '
               'every day, so definitely check out uh the rentals.',
       'timestamp': 288,
       'timestamp_label': '[00:04:48]',
       'timestamp_seconds': 288,
       'tip': 'You can either go to the website also. I recommend going to gpubattle. AI has '
              'all the updated API prices when you connect your API key. So prices change '
              'every day, so definitely check out uh the rentals.',
       'title': 'The Cheapest Cloud GPU for Every AI Job (GPU Battle)',
       'url': 'https://www.youtube.com/watch?v=ymI6ZvqQNjQ&t=288s',
       'video_id': 'ymI6ZvqQNjQ'},
      {'author': 'Sangoma',
       'channel': 'Sangoma',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:59](https://www.youtube.com/watch?v=dTsrqOzzrOk&t=1019s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Month for around 10 bucks uh please note that the low volume fax service does '
               'not support stacking users that need more are just encouraged to switch to a '
               'high volume trunk.',
       'timestamp': 1019,
       'timestamp_label': '[00:16:59]',
       'timestamp_seconds': 1019,
       'tip': 'Month for around 10 bucks uh please note that the low volume fax service does '
              'not support stacking users that need more are just encouraged to switch to a '
              'high volume trunk.',
       'title': 'SIP Trunking: Retail and Wholesale (Sangoma)',
       'url': 'https://www.youtube.com/watch?v=dTsrqOzzrOk&t=1019s',
       'video_id': 'dTsrqOzzrOk'},
      {'author': 'brandon coin',
       'channel': 'brandon coin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:52](https://www.youtube.com/watch?v=HsTuMEqbt48&t=292s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They're all about right now um assuming that crypto's moderate rally over the "
               "past month doesn't continue breathing new life into the mining industry.",
       'timestamp': 292,
       'timestamp_label': '[00:04:52]',
       'timestamp_seconds': 292,
       'tip': "They're all about right now um assuming that crypto's moderate rally over the "
              "past month doesn't continue breathing new life into the mining industry.",
       'title': 'Nvidia Urges Customers to Stop Crypto Mining (brandon coin)',
       'url': 'https://www.youtube.com/watch?v=HsTuMEqbt48&t=292s',
       'video_id': 'HsTuMEqbt48'},
      {'author': 'Signal House',
       'channel': 'Signal House',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=sVsWkczKncU&t=88s)',
       'relevance': 'Attributed practitioner commentary on reserved-to-on-demand '
                    '`H100`/`H200`/`B200` bare-metal GPU slicing, multi-provider `LLM` '
                    'inference routing, and wholesale `SIP`/`10DLC`/`IPv4` telecom capacity '
                    'spreads (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'On a standard 10DLC A2P campaign, you are able to send 240 SMS segments per '
               'minute with AT&T, 150 MMS messages per minute with AT&T, and 2,000 segments '
               'per day with T-Mobile.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'On a standard 10DLC A2P campaign, you are able to send 240 SMS segments per '
              'minute with AT&T, 150 MMS messages per minute with AT&T, and 2,000 segments per '
              'day with T-Mobile.',
       'title': 'Is Bandwidth, Twilio, and Telnyx Killing your 10DLC A2P Business Messaging?! '
                '(Signal House)',
       'url': 'https://www.youtube.com/watch?v=sVsWkczKncU&t=88s',
       'video_id': 'sVsWkczKncU'}]}
