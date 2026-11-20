"""Curated 180-citation AI-Powered Micro SaaS baseline (15 per chapter across Q1-Q12) mined strictly from verified AI Micro-SaaS and SaaS-billing YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'agent',
     'ai',
     'automation',
     'b2b',
     'compliance',
     'copilot',
     'micro',
     'moat',
     'model',
     'models',
     'niche',
     'product',
     'rag',
     'saas',
     'software',
     'subscription',
     'vertical',
     'wedge',
     'workflow',
     'wrapper'},
 2: {'annual',
     'b2b',
     'billing',
     'budget',
     'buyer',
     'buyers',
     'card',
     'checkout',
     'contract',
     'customer',
     'customers',
     'enterprise',
     'interchange',
     'invoice',
     'merchant',
     'mor',
     'paddle',
     'payment',
     'procurement',
     'seat',
     'seats',
     'smb',
     'stripe',
     'subscription',
     'vcc'},
 3: {'arpu',
     'arr',
     'cac',
     'churn',
     'cogs',
     'compute',
     'credit',
     'credits',
     'economics',
     'gross',
     'inference',
     'ltv',
     'margin',
     'margins',
     'meter',
     'metering',
     'mrr',
     'net',
     'payback',
     'plan',
     'price',
     'pricing',
     'profit',
     'retention',
     'revenue',
     'tier',
     'tiers',
     'token',
     'tokens',
     'usage'},
 4: {'activate',
     'anthropic',
     'aws',
     'azure',
     'bootstrap',
     'budget',
     'capital',
     'cloud',
     'cloudflare',
     'cost',
     'costs',
     'credits',
     'database',
     'edge',
     'free',
     'gcp',
     'grant',
     'hosting',
     'infra',
     'infrastructure',
     'lean',
     'multiplex',
     'openai',
     'opex',
     'postgres',
     'router',
     'serverless',
     'stack',
     'startup',
     'vercel'},
 5: {'abuse',
     'api',
     'ban',
     'cache',
     'caching',
     'chargeback',
     'churn',
     'cost',
     'dependency',
     'drift',
     'dunning',
     'fraud',
     'hallucination',
     'injection',
     'latency',
     'leak',
     'limit',
     'limits',
     'lock',
     'mistake',
     'outage',
     'platform',
     'prompt',
     'rate',
     'risk',
     'runaway',
     'security',
     'spike',
     'trap',
     'wrapper'},
 6: {'accessibility',
     'ada',
     'audit',
     'builtwith',
     'churn',
     'competitor',
     'demand',
     'discover',
     'docket',
     'domain',
     'g2',
     'idea',
     'ideas',
     'intent',
     'interview',
     'keyword',
     'leads',
     'market',
     'niche',
     'pain',
     'presell',
     'problem',
     'reddit',
     'research',
     'review',
     'reviews',
     'scanner',
     'signals',
     'validate',
     'validation',
     'wcag'},
 7: {'activation',
     'api',
     'architecture',
     'auth',
     'billing',
     'build',
     'cache',
     'caching',
     'deploy',
     'eval',
     'evals',
     'evaluation',
     'feature',
     'guardrail',
     'itenant',
     'latency',
     'launch',
     'log',
     'logging',
     'meter',
     'mvp',
     'onboard',
     'onboarding',
     'pipeline',
     'production',
     'queue',
     'rag',
     'schema',
     'ship',
     'tenant',
     'webhook'},
 8: {'analytics',
     'api',
     'apis',
     'auth',
     'chrome',
     'cloudflare',
     'database',
     'docker',
     'enrichment',
     'extension',
     'geo',
     'github',
     'llm',
     'monitoring',
     'neon',
     'observability',
     'pixel',
     'postgres',
     'posthog',
     'queue',
     'redis',
     'router',
     'sdk',
     'sentry',
     'stack',
     'stripe',
     'supabase',
     'telemetry',
     'tool',
     'tools',
     'vector'},
 9: {'accessibility',
     'agreement',
     'baa',
     'billing',
     'cancel',
     'ccpa',
     'compliance',
     'consent',
     'contract',
     'copyright',
     'data',
     'disclosure',
     'dmca',
     'dpa',
     'enterprise',
     'ftc',
     'gdpr',
     'hipaa',
     'ip',
     'license',
     'privacy',
     'retention',
     'rosca',
     'security',
     'sla',
     'soc',
     'subprocessor',
     'tax',
     'tcpa',
     'terms',
     'training',
     'vat'},
 10: {'ab',
      'acquisition',
      'agent',
      'alert',
      'alerts',
      'automate',
      'automation',
      'billing',
      'bot',
      'calculator',
      'cancel',
      'churn',
      'comparison',
      'cron',
      'dunning',
      'email',
      'faceless',
      'flow',
      'funnel',
      'hijack',
      'loop',
      'loops',
      'onboarding',
      'plg',
      'programmatic',
      'quiz',
      'referral',
      'seo',
      'support',
      'test',
      'viral',
      'youtube'},
 11: {'acquire',
      'acquisition',
      'agency',
      'buy',
      'contractor',
      'contractors',
      'customer',
      'delegate',
      'developer',
      'engineer',
      'exit',
      'extension',
      'founder',
      'growth',
      'hire',
      'hiring',
      'kpi',
      'kpis',
      'microacquire',
      'multiple',
      'multiples',
      'operations',
      'operator',
      'pod',
      'portfolio',
      'rollup',
      'scale',
      'scaling',
      'sop',
      'support',
      'team'},
 12: {'action',
      'audit',
      'beta',
      'checklist',
      'cohort',
      'customer',
      'day',
      'days',
      'deploy',
      'execute',
      'execution',
      'first',
      'goal',
      'iterate',
      'kpi',
      'launch',
      'milestone',
      'month',
      'mrr',
      'mvp',
      'ninety',
      'pilot',
      'plan',
      'roadmap',
      'ship',
      'sprint',
      'start',
      'steps',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Practical Founders - with Greg Head',
      'channel': 'Practical Founders - with Greg Head',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=Avxi60Ny5SM&t=20s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': "We think software plus AI is the right approach. And so they're harvesting and "
              'creating that data moat that is going to help make them defensible and using '
              'the AI tools. Why not use the AI tools to provide more automation?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "We think software plus AI is the right approach. And so they're harvesting and "
             'creating that data moat that is going to help make them defensible and using the '
             'AI tools. Why not use the AI tools to provide more automation?',
      'title': 'AI Is Not Killing Vertical SaaS - It’s Practical Leverage (Practical Founders '
               '- with Greg Head)',
      'url': 'https://www.youtube.com/watch?v=Avxi60Ny5SM&t=20s',
      'video_id': 'Avxi60Ny5SM'},
     {'author': 'Indy Pixels | Abdalla Emam',
      'channel': 'Indy Pixels | Abdalla Emam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=NwYdSzPW6yg&t=45s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': "AI development tool, and I'm excited about this one, so let's get in. First, "
              "let's define the term. An AI wrapper usually means a product that sits on top "
              'of an existing AI model.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "AI development tool, and I'm excited about this one, so let's get in. First, "
             "let's define the term. An AI wrapper usually means a product that sits on top of "
             'an existing AI model.',
      'title': 'The Harsh Truth About AI Wrappers (From a Venture Investor) (Indy Pixels | '
               'Abdalla Emam)',
      'url': 'https://www.youtube.com/watch?v=NwYdSzPW6yg&t=45s',
      'video_id': 'NwYdSzPW6yg'},
     {'author': 'Sabyr Nurgaliyev',
      'channel': 'Sabyr Nurgaliyev',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=YVRP3QoP6bs&t=78s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'It is be the answer inside the LLM. And Reddit is a step to get there. Meet '
              'Viewst, a B2B SaaS that turn one ad creative into hundreds of HTML5 banners for '
              'marketing teams. Solid product, zero reviews, but completely invisible to AI '
              'search. Day zero, ChatGPT citations zero.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'It is be the answer inside the LLM. And Reddit is a step to get there. Meet '
             'Viewst, a B2B SaaS that turn one ad creative into hundreds of HTML5 banners for '
             'marketing teams. Solid product, zero reviews, but completely invisible to AI '
             'search. Day zero, ChatGPT citations zero.',
      'title': 'I Ranked a B2B SaaS on ChatGPT in 30 Days With Reddit (Sabyr Nurgaliyev)',
      'url': 'https://www.youtube.com/watch?v=YVRP3QoP6bs&t=78s',
      'video_id': 'YVRP3QoP6bs'},
     {'author': 'Verticals: A Weekly Biz Show On Vertical AI',
      'channel': 'Verticals: A Weekly Biz Show On Vertical AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:31](https://www.youtube.com/watch?v=y6eOdHpH5W8&t=2071s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'How so I I just kind of wanted to shift to you know again with with with you '
              "guys' corpus of of customers you have a pretty interesting perspective on you "
              'know how AI is diffusing throughout the vertical software ecosystem.',
      'timestamp': 2071,
      'timestamp_label': '[00:34:31]',
      'timestamp_seconds': 2071,
      'tip': 'How so I I just kind of wanted to shift to you know again with with with you '
             "guys' corpus of of customers you have a pretty interesting perspective on you "
             'know how AI is diffusing throughout the vertical software ecosystem.',
      'title': 'How to Build a Vertical SaaS Company AI Can’t Replace | Sahill Poddar '
               '(Verticals: A Weekly Biz Show On Vertical AI)',
      'url': 'https://www.youtube.com/watch?v=y6eOdHpH5W8&t=2071s',
      'video_id': 'y6eOdHpH5W8'},
     {'author': 'Paul Zuradzki',
      'channel': 'Paul Zuradzki',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=Nk7qDiLHyuU&t=70s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'I can have my cloud models using an API key. And then when I connect with my '
              "coding agent, say I'm using the pi coding harness, and you can see in the "
              'bottom right here is my model selection.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'I can have my cloud models using an API key. And then when I connect with my '
             "coding agent, say I'm using the pi coding harness, and you can see in the bottom "
             'right here is my model selection.',
      'title': 'LiteLLM AI Gateway: Routing, API Keys, Budgets, and Guardrails for Local and '
               'Cloud Models (Paul Zuradzki)',
      'url': 'https://www.youtube.com/watch?v=Nk7qDiLHyuU&t=70s',
      'video_id': 'Nk7qDiLHyuU'},
     {'author': 'BergTube',
      'channel': 'BergTube',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=-_NbEobmiAY&t=87s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': "We're moving from tools for humans to AI that delivers outcomes. Think about "
              'your current tech stack. How many tabs do you have open right now? Vertical AI '
              'collapses those tabs into a single autonomous workflow. It understands the '
              'specific language of your niche.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "We're moving from tools for humans to AI that delivers outcomes. Think about "
             'your current tech stack. How many tabs do you have open right now? Vertical AI '
             'collapses those tabs into a single autonomous workflow. It understands the '
             'specific language of your niche.',
      'title': 'The Death of SaaS | Why "Vertical AI" is Taking Over in 2026 (BergTube)',
      'url': 'https://www.youtube.com/watch?v=-_NbEobmiAY&t=87s',
      'video_id': '-_NbEobmiAY'},
     {'author': 'Zues Ordaz',
      'channel': 'Zues Ordaz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=63s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'SaaS and immediately think you need to code or you need a technical co-founder '
              "or you need seed or investor money. That's the wrong lens entirely. The most "
              "profitable micro-SaaS businesses don't sell software. They sell time back to "
              'the consumer.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'SaaS and immediately think you need to code or you need a technical co-founder '
             "or you need seed or investor money. That's the wrong lens entirely. The most "
             "profitable micro-SaaS businesses don't sell software. They sell time back to the "
             'consumer.',
      'title': 'The Micro SaaS Business Almost Nobody Is Building (Until Now) (Zues Ordaz)',
      'url': 'https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=63s',
      'video_id': 'I-4eEpO2G0Q'},
     {'author': 'Jono Finds',
      'channel': 'Jono Finds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=XZPNjgJ4E0c&t=78s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'He had built one of those before. The product gives you one key and one billing '
              'account with access to over 300 models across more than 60 providers. The '
              'interface is compatible with the dominant software development kit, so '
              'switching requires changing a single line of code.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'He had built one of those before. The product gives you one key and one billing '
             'account with access to over 300 models across more than 60 providers. The '
             'interface is compatible with the dominant software development kit, so switching '
             'requires changing a single line of code.',
      'title': 'OpenRouter vs LiteLLM: Pay 5% or Host It Yourself? (2026) (Jono Finds)',
      'url': 'https://www.youtube.com/watch?v=XZPNjgJ4E0c&t=78s',
      'video_id': 'XZPNjgJ4E0c'},
     {'author': 'Execute Automation',
      'channel': 'Execute Automation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=QkElI_HcuT8&t=156s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'So essentially running one local AI model with omlx or lama is easy to do with '
              'pi or the codeex coding agent without any issue.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'So essentially running one local AI model with omlx or lama is easy to do with '
             'pi or the codeex coding agent without any issue.',
      'title': 'I Built an Auto Router for Local LLMs with LiteLLM + Pi Coding Agent (Execute '
               'Automation)',
      'url': 'https://www.youtube.com/watch?v=QkElI_HcuT8&t=156s',
      'video_id': 'QkElI_HcuT8'},
     {'author': 'Jordan Crawford (Blueprint)',
      'channel': 'Jordan Crawford (Blueprint)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:01](https://www.youtube.com/watch?v=RINTsdOTWfc&t=481s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': "'t have like the type of lens that I do, they don't really realize that there "
              'are some segments that just are ready to drop, ready to buy that just pick up '
              'the product so much easier. And the models are amazing at helping you find '
              'those and figuring out what you should test.',
      'timestamp': 481,
      'timestamp_label': '[00:08:01]',
      'timestamp_seconds': 481,
      'tip': "'t have like the type of lens that I do, they don't really realize that there "
             'are some segments that just are ready to drop, ready to buy that just pick up '
             'the product so much easier. And the models are amazing at helping you find those '
             'and figuring out what you should test.',
      'title': 'Why Vertical SaaS Companies Will Win in the AI GTM Race (Jordan Crawford '
               '(Blueprint))',
      'url': 'https://www.youtube.com/watch?v=RINTsdOTWfc&t=481s',
      'video_id': 'RINTsdOTWfc'},
     {'author': 'Simon Høiberg',
      'channel': 'Simon Høiberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=QIA9Ry42Lbs&t=326s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'This process is called fine-tuning. Then, when a new B-roll clip is created, we '
              'chain two models. The custom image generation model will generate an image. The '
              'image is then fed to a video generation model and used as the starting frame '
              'for the clip.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': 'This process is called fine-tuning. Then, when a new B-roll clip is created, we '
             'chain two models. The custom image generation model will generate an image. The '
             'image is then fed to a video generation model and used as the starting frame for '
             'the clip.',
      'title': 'Get rich building niche AI SaaS (...not another ChatGPT wrapper) (Simon '
               'Høiberg)',
      'url': 'https://www.youtube.com/watch?v=QIA9Ry42Lbs&t=326s',
      'video_id': 'QIA9Ry42Lbs'},
     {'author': 'Rob Walling',
      'channel': 'Rob Walling',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:52](https://www.youtube.com/watch?v=6sgCo6fMSGY&t=832s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': '"I was a freelance software developer and I was asked to build our product, '
              'permitting software, by municipalities. I was asked three times and on the '
              "third time I decided, 'Okay, these guys can't find a SaaS solution that fits "
              'their needs.',
      'timestamp': 832,
      'timestamp_label': '[00:13:52]',
      'timestamp_seconds': 832,
      'tip': '"I was a freelance software developer and I was asked to build our product, '
             'permitting software, by municipalities. I was asked three times and on the third '
             "time I decided, 'Okay, these guys can't find a SaaS solution that fits their "
             'needs.',
      'title': "Give Me 36 Minutes and I'll Teach You How to Find $1M SaaS Ideas (Rob Walling)",
      'url': 'https://www.youtube.com/watch?v=6sgCo6fMSGY&t=832s',
      'video_id': '6sgCo6fMSGY'},
     {'author': 'Dan Martell',
      'channel': 'Dan Martell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:17](https://www.youtube.com/watch?v=UEHdYNXiIUU&t=377s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'So that it’s actually an incredible deal because you get new innovation and new '
              "updates and new capabilities that you didn't have to pay for, and it's just "
              'part of the subscription. So there you go, a five minute breakdown of what is '
              'Software as a Service, SaaS.',
      'timestamp': 377,
      'timestamp_label': '[00:06:17]',
      'timestamp_seconds': 377,
      'tip': 'So that it’s actually an incredible deal because you get new innovation and new '
             "updates and new capabilities that you didn't have to pay for, and it's just part "
             'of the subscription. So there you go, a five minute breakdown of what is '
             'Software as a Service, SaaS.',
      'title': 'What Is SaaS? (Explained in 5 Minutes) (Dan Martell)',
      'url': 'https://www.youtube.com/watch?v=UEHdYNXiIUU&t=377s',
      'video_id': 'UEHdYNXiIUU'},
     {'author': "Bootstrapper's Paradise",
      'channel': "Bootstrapper's Paradise",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=GK9LZkd6aHM&t=328s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': 'But the new rule is that the best product with the best distribution wins. Now, '
              'when AI can build an MVP in weeks and replicate features in days, product '
              "quality alone isn't a moat. What is a mode is owning the channel that connects "
              'you to your customers.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': 'But the new rule is that the best product with the best distribution wins. Now, '
             'when AI can build an MVP in weeks and replicate features in days, product '
             "quality alone isn't a moat. What is a mode is owning the channel that connects "
             'you to your customers.',
      'title': "Vertical AI vs Traditional SaaS | Game Over (Bootstrapper's Paradise)",
      'url': 'https://www.youtube.com/watch?v=GK9LZkd6aHM&t=328s',
      'video_id': 'GK9LZkd6aHM'},
     {'author': 'HelperMan',
      'channel': 'HelperMan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=o3KRrFnoAgM&t=120s)',
      'relevance': 'Attributed practitioner commentary on vertical B2B AI micro-SaaS wedges, '
                   'workflow moats, and avoiding thin single-prompt wrappers.',
      'source_type': 'video_pro_tip',
      'text': "Overall, after 6 months of using Paddle, I think it's one of the best payment "
              'solutions for SaaS businesses and digital product creators who want simplicity '
              'and global compliance support.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "Overall, after 6 months of using Paddle, I think it's one of the best payment "
             'solutions for SaaS businesses and digital product creators who want simplicity '
             'and global compliance support.',
      'title': 'Paddle for Merchant of Record Honest Review - Watch Before Using (HelperMan)',
      'url': 'https://www.youtube.com/watch?v=o3KRrFnoAgM&t=120s',
      'video_id': 'o3KRrFnoAgM'}],
 2: [{'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=255s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': "If you're a growing or established SAS company with dollar1000k plus in annual "
              'revenue, you need advanced subscription management, revenue recovery, hybrid '
              "billing models, or you're selling to enterprise customers.",
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': "If you're a growing or established SAS company with dollar1000k plus in annual "
             'revenue, you need advanced subscription management, revenue recovery, hybrid '
             "billing models, or you're selling to enterprise customers.",
      'title': 'Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech)',
      'url': 'https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=255s',
      'video_id': 'Qq-EyvVj7IM'},
     {'author': 'Ampvoro',
      'channel': 'Ampvoro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=fGLomKpo_LI&t=30s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': "'re assigning it to customers. Under pricing, select recurring. This is an "
              'important step because subscriptions need recurring billing rather than a '
              'one-time payment. After that, enter the subscription amount.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "'re assigning it to customers. Under pricing, select recurring. This is an "
             'important step because subscriptions need recurring billing rather than a '
             'one-time payment. After that, enter the subscription amount.',
      'title': 'How to Set Up Stripe Billing for Subscriptions [2026 Full Tutorial] (Ampvoro)',
      'url': 'https://www.youtube.com/watch?v=fGLomKpo_LI&t=30s',
      'video_id': 'fGLomKpo_LI'},
     {'author': 'TechWealth Hub',
      'channel': 'TechWealth Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=96s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Fourth, customer support for payment issues. And the crazy part, you enable all '
              'of this with one line of code. In your Stripe checkout session, you add managed '
              'payments enabled. You now have paddle level tax compliance with Stripe level '
              'infrastructure.',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': 'Fourth, customer support for payment issues. And the crazy part, you enable all '
             'of this with one line of code. In your Stripe checkout session, you add managed '
             'payments enabled. You now have paddle level tax compliance with Stripe level '
             'infrastructure.',
      'title': 'Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub)',
      'url': 'https://www.youtube.com/watch?v=KRdWGDk-GkY&t=96s',
      'video_id': 'KRdWGDk-GkY'},
     {'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=20s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'This choice splits our three contenders into two completely different '
              'categories. Stripe Checkout is a standard payment processor, while Paddle and '
              'Lemon Squeezy act as a merchant of record. A merchant of record means the '
              'platform becomes the legal seller of your product.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'This choice splits our three contenders into two completely different '
             'categories. Stripe Checkout is a standard payment processor, while Paddle and '
             'Lemon Squeezy act as a merchant of record. A merchant of record means the '
             'platform becomes the legal seller of your product.',
      'title': 'Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? '
               '(Tutorly)',
      'url': 'https://www.youtube.com/watch?v=IfaCBBIoVK0&t=20s',
      'video_id': 'IfaCBBIoVK0'},
     {'author': 'Indie Hacker News',
      'channel': 'Indie Hacker News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=_lbbl0hdJIg&t=51s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Usage events go in, invoices and payments come out. And the customer table near '
              'the bottom raises the obvious question. What are all those teams not paying '
              "Stripe? 7% of your billing volume, and that's on top of the card fees.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Usage events go in, invoices and payments come out. And the customer table near '
             'the bottom raises the obvious question. What are all those teams not paying '
             "Stripe? 7% of your billing volume, and that's on top of the card fees.",
      'title': 'Someone open-sourced Stripe Billing (Mistral uses it) (Indie Hacker News)',
      'url': 'https://www.youtube.com/watch?v=_lbbl0hdJIg&t=51s',
      'video_id': '_lbbl0hdJIg'},
     {'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:16](https://www.youtube.com/watch?v=i05UCC3UvNY&t=316s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Paddle charges five percent plus fifty cents per checkout transaction on its '
              'pay-as-you-go plan, with no monthly fee. That price includes tax handling, '
              "fraud protection, subscriptions, and support for your customers' billing "
              'questions.',
      'timestamp': 316,
      'timestamp_label': '[00:05:16]',
      'timestamp_seconds': 316,
      'tip': 'Paddle charges five percent plus fifty cents per checkout transaction on its '
             'pay-as-you-go plan, with no monthly fee. That price includes tax handling, fraud '
             "protection, subscriptions, and support for your customers' billing questions.",
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=316s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'E Learning by AL SADDAT',
      'channel': 'E Learning by AL SADDAT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=0K7i4CFP_qc&t=65s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Never overwrite a single credits integer without an audit trail. Every topup, '
              'reservation, settlement, and refund appends an immutable ledger transaction '
              'row. So every customer invoice is 100% auditable. Third, item potent Stripe '
              'billing and web hook verification.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'Never overwrite a single credits integer without an audit trail. Every topup, '
             'reservation, settlement, and refund appends an immutable ledger transaction row. '
             'So every customer invoice is 100% auditable. Third, item potent Stripe billing '
             'and web hook verification.',
      'title': 'Real-Time Token Usage Metering, Credit Ledgers & Stripe Billing Webhooks (E '
               'Learning by AL SADDAT)',
      'url': 'https://www.youtube.com/watch?v=0K7i4CFP_qc&t=65s',
      'video_id': '0K7i4CFP_qc'},
     {'author': 'How2Genius',
      'channel': 'How2Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=144s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'It also supports a wide range of payment methods, credit cards, PayPal, Apple '
              'Pay, and more, so customers can pay however they prefer. Fastring subscription '
              'management tools are strong, offering pration, renewals, and flexible billing '
              'cycles.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'It also supports a wide range of payment methods, credit cards, PayPal, Apple '
             'Pay, and more, so customers can pay however they prefer. Fastring subscription '
             'management tools are strong, offering pration, renewals, and flexible billing '
             'cycles.',
      'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
               '(How2Genius)',
      'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=144s',
      'video_id': 'Y5VXhUB7aNM'},
     {'author': 'Stripe Developers',
      'channel': 'Stripe Developers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=Hr9MP_3-QPg&t=301s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Meter connects with the price. The price goes onto subscription and then you '
              'charge the customer. And so does the charge uh I I suppose the charge can be '
              'taken automatically or invoice or absolutely.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': 'Meter connects with the price. The price goes onto subscription and then you '
             'charge the customer. And so does the charge uh I I suppose the charge can be '
             'taken automatically or invoice or absolutely.',
      'title': 'Enabling pay-as-you-go with usage based billing (Stripe Developers)',
      'url': 'https://www.youtube.com/watch?v=Hr9MP_3-QPg&t=301s',
      'video_id': 'Hr9MP_3-QPg'},
     {'author': 'Stephen S.',
      'channel': 'Stephen S.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:26](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=266s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Then I linked my application to Stripe through the chat and asked Curo to '
              'create the right back-end pricing and subscription structure for the prices '
              'that I already had displayed on my website and link the checkout. Now I also '
              'removed like authentication here.',
      'timestamp': 266,
      'timestamp_label': '[00:04:26]',
      'timestamp_seconds': 266,
      'tip': 'Then I linked my application to Stripe through the chat and asked Curo to create '
             'the right back-end pricing and subscription structure for the prices that I '
             'already had displayed on my website and link the checkout. Now I also removed '
             'like authentication here.',
      'title': "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an "
               'Existing App  #mcp (Stephen S.)',
      'url': 'https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=266s',
      'video_id': 'F-WZgXuQIuQ'},
     {'author': 'CJ Avilla (cjav_dev)',
      'channel': 'CJ Avilla (cjav_dev)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:53](https://www.youtube.com/watch?v=v8cN4pEofy8&t=2153s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': "Customer.subscription.created so eda data type let's print out their types and "
              "then let's say event.all.map or I guess dot find event.type is equal to "
              'customer.subscription.created.',
      'timestamp': 2153,
      'timestamp_label': '[00:35:53]',
      'timestamp_seconds': 2153,
      'tip': "Customer.subscription.created so eda data type let's print out their types and "
             "then let's say event.all.map or I guess dot find event.type is equal to "
             'customer.subscription.created.',
      'title': 'Usage based metered billing with Ruby on Rails and Stripe (CJ Avilla '
               '(cjav_dev))',
      'url': 'https://www.youtube.com/watch?v=v8cN4pEofy8&t=2153s',
      'video_id': 'v8cN4pEofy8'},
     {'author': 'Neta Arbel | Growthgrid',
      'channel': 'Neta Arbel | Growthgrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:35](https://www.youtube.com/watch?v=UEllU5g4QdQ&t=455s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': '90 payment terms instead of direct card bill and that will actually improve '
              'your runway and get you a lot of working capital, you should negotiate with a '
              'reseller who will route your billing through them and will get you better '
              'payment terms.',
      'timestamp': 455,
      'timestamp_label': '[00:07:35]',
      'timestamp_seconds': 455,
      'tip': '90 payment terms instead of direct card bill and that will actually improve your '
             'runway and get you a lot of working capital, you should negotiate with a '
             'reseller who will route your billing through them and will get you better '
             'payment terms.',
      'title': 'How To Get More AWS/GCP Credits After You Already Used Startup Credits (Neta '
               'Arbel | Growthgrid)',
      'url': 'https://www.youtube.com/watch?v=UEllU5g4QdQ&t=455s',
      'video_id': 'UEllU5g4QdQ'},
     {'author': 'Captain Vova (Vova Feldman)',
      'channel': 'Captain Vova (Vova Feldman)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=85s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': "And that's very interesting because Stripe is already known to be one of the "
              "more expensive payment processors. So, we'll need to see how would be the "
              'adoption, right? Whether existing customers of Stripe will adopt Managed '
              "Payments just because it's right there and easy.",
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': "And that's very interesting because Stripe is already known to be one of the "
             "more expensive payment processors. So, we'll need to see how would be the "
             'adoption, right? Whether existing customers of Stripe will adopt Managed '
             "Payments just because it's right there and easy.",
      'title': 'Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain '
               'Vova (Vova Feldman))',
      'url': 'https://www.youtube.com/watch?v=5zGuxRrg_O0&t=85s',
      'video_id': '5zGuxRrg_O0'},
     {'author': 'This Works Tutorials',
      'channel': 'This Works Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=00KM5yk235k&t=32s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Next, move to the top navigation and click products. This opens a menu of '
              "Stripe's tools. In the revenue category, select usage-based billing. This takes "
              'you to the product page dedicated to charging customers based on how much they '
              'actually use.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'Next, move to the top navigation and click products. This opens a menu of '
             "Stripe's tools. In the revenue category, select usage-based billing. This takes "
             'you to the product page dedicated to charging customers based on how much they '
             'actually use.',
      'title': 'Stripe Usage-Based Billing Guide [2026 Full Guide] (This Works Tutorials)',
      'url': 'https://www.youtube.com/watch?v=00KM5yk235k&t=32s',
      'video_id': '00KM5yk235k'},
     {'author': 'GuideFrame',
      'channel': 'GuideFrame',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=xssyCPxzFWA&t=89s)',
      'relevance': 'Attributed practitioner commentary on B2B budget holders, Stripe vs. '
                   'Merchant-of-Record billing, annual prepay cashflow, and embedded payment '
                   'spreads.',
      'source_type': 'video_pro_tip',
      'text': 'Adjust the parameters as needed based on customer feedback and usage patterns. '
              'Document any changes to your API or product information for future reference. '
              'This concludes the steps to update Stripe billing for usage-based pricing.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Adjust the parameters as needed based on customer feedback and usage patterns. '
             'Document any changes to your API or product information for future reference. '
             'This concludes the steps to update Stripe billing for usage-based pricing.',
      'title': 'How to update Stripe Billing to add usage-based pricing - Full Guide '
               '(GuideFrame)',
      'url': 'https://www.youtube.com/watch?v=xssyCPxzFWA&t=89s',
      'video_id': 'xssyCPxzFWA'}],
 3: [{'author': 'Business Mechanics',
      'channel': 'Business Mechanics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:02](https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=842s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': "In the optimistic scenario, you've built a product with strong retention, a "
              'healthy net revenue retention above 110%, a CAC payback period under 12 months, '
              "and monthly churn under 2%. Revenue compounds because you're not just adding "
              'new customers.',
      'timestamp': 842,
      'timestamp_label': '[00:14:02]',
      'timestamp_seconds': 842,
      'tip': "In the optimistic scenario, you've built a product with strong retention, a "
             'healthy net revenue retention above 110%, a CAC payback period under 12 months, '
             "and monthly churn under 2%. Revenue compounds because you're not just adding new "
             'customers.',
      'title': 'The Economics of Owning a SaaS Company (Business Mechanics)',
      'url': 'https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=842s',
      'video_id': 'Ju9H1oq7CM8'},
     {'author': 'GuideFrame',
      'channel': 'GuideFrame',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=xssyCPxzFWA&t=43s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'Set the price per unit in the specified currency. Determine if there is a '
              'minimum price or a maximum price to charge. If necessary, configure pricing '
              'tiers by clicking add tier to establish varying rates based on usage. Save the '
              'pricing plan after reviewing all the details.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'Set the price per unit in the specified currency. Determine if there is a '
             'minimum price or a maximum price to charge. If necessary, configure pricing '
             'tiers by clicking add tier to establish varying rates based on usage. Save the '
             'pricing plan after reviewing all the details.',
      'title': 'How to update Stripe Billing to add usage-based pricing - Full Guide '
               '(GuideFrame)',
      'url': 'https://www.youtube.com/watch?v=xssyCPxzFWA&t=43s',
      'video_id': 'xssyCPxzFWA'},
     {'author': 'Costoday',
      'channel': 'Costoday',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:19](https://www.youtube.com/watch?v=aOKH0EoSCCc&t=619s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': "A SAS company with two ZUA's customers paying $100 a month, $2. 4 $4 million in "
              'annual recurring revenue, a taxi payback period of 9 months, monthly churn held '
              'at 2% and net revenue retention at 115% through consistent upselling. Annual '
              'revenue approximately $2.',
      'timestamp': 619,
      'timestamp_label': '[00:10:19]',
      'timestamp_seconds': 619,
      'tip': "A SAS company with two ZUA's customers paying $100 a month, $2. 4 $4 million in "
             'annual recurring revenue, a taxi payback period of 9 months, monthly churn held '
             'at 2% and net revenue retention at 115% through consistent upselling. Annual '
             'revenue approximately $2.',
      'title': 'The Economics of Owning a SaaS Company (Costoday)',
      'url': 'https://www.youtube.com/watch?v=aOKH0EoSCCc&t=619s',
      'video_id': 'aOKH0EoSCCc'},
     {'author': 'One Minute Finance',
      'channel': 'One Minute Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=Xpw9vNbYna0&t=271s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': '18,000 pounds left in real contribution to help cover your operating expenses '
              'and eventually generate a profit. You absolutely have to calculate LTV on gross '
              'profit, not revenue, or your entire financial model just collapses. Okay, '
              'section three, the LTV to CAC ratio.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': '18,000 pounds left in real contribution to help cover your operating expenses '
             'and eventually generate a profit. You absolutely have to calculate LTV on gross '
             'profit, not revenue, or your entire financial model just collapses. Okay, '
             'section three, the LTV to CAC ratio.',
      'title': 'Core Unit Economics: The Financial Formulas Behind SaaS, E-Commerce, and '
               'Marketplaces (One Minute Finance)',
      'url': 'https://www.youtube.com/watch?v=Xpw9vNbYna0&t=271s',
      'video_id': 'Xpw9vNbYna0'},
     {'author': 'ChartMogul',
      'channel': 'ChartMogul',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=zo3QHrXiprs&t=360s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'There are two types of revenue retention or revenue churn rate that we look at '
              'in SAS normally. The first is gross revenue retention rate and the second is '
              'net revenue retention rate.',
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': 'There are two types of revenue retention or revenue churn rate that we look at '
             'in SAS normally. The first is gross revenue retention rate and the second is net '
             'revenue retention rate.',
      'title': '11 essential SaaS metrics explained in 11 minutes (ChartMogul)',
      'url': 'https://www.youtube.com/watch?v=zo3QHrXiprs&t=360s',
      'video_id': 'zo3QHrXiprs'},
     {'author': 'Efficient NLP',
      'channel': 'Efficient NLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=Q_U4pRggC5I&t=127s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'You can kind of see this in the token economics. Uh here is the Anthropic '
              'pricing page right now and they price um $5 per million tokens for the Opus '
              'model. The price for a cache read is 10 times cheaper at 50 cents per million '
              'tokens.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'You can kind of see this in the token economics. Uh here is the Anthropic '
             'pricing page right now and they price um $5 per million tokens for the Opus '
             'model. The price for a cache read is 10 times cheaper at 50 cents per million '
             'tokens.',
      'title': 'Why agents recompute the same prompt, and how prompt caching fixes it '
               '(Efficient NLP)',
      'url': 'https://www.youtube.com/watch?v=Q_U4pRggC5I&t=127s',
      'video_id': 'Q_U4pRggC5I'},
     {'author': 'Medical Chat',
      'channel': 'Medical Chat',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=yo4GOxbqovo&t=78s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'Instead of a flat fee, you charge only for what people actually use. Bill per '
              'message or by credits, so your heavier, smarter models simply cost a little '
              'more. Add volume tiers and the price drops as usage grows. Your biggest '
              'customers get your best rate.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Instead of a flat fee, you charge only for what people actually use. Bill per '
             'message or by credits, so your heavier, smarter models simply cost a little '
             'more. Add volume tiers and the price drops as usage grows. Your biggest '
             'customers get your best rate.',
      'title': 'Make Your AI Chatbot Pay For Itself — Stripe Usage Metering, Paywalls & Caps '
               '(Chat Data) (Medical Chat)',
      'url': 'https://www.youtube.com/watch?v=yo4GOxbqovo&t=78s',
      'video_id': 'yo4GOxbqovo'},
     {'author': 'Stripe Developers',
      'channel': 'Stripe Developers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=o_6aujJ5WbM&t=50s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'The second price represents a tiered pricing model. And if we scroll down to '
              "the bottom, you can notice that it's associated with two tiers. The first tier "
              'represents a quantity from 1 to 40 and the second tier captures all the rest.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'The second price represents a tiered pricing model. And if we scroll down to the '
             "bottom, you can notice that it's associated with two tiers. The first tier "
             'represents a quantity from 1 to 40 and the second tier captures all the rest.',
      'title': 'Monetizing your APIs with usage-based billing (Stripe Developers)',
      'url': 'https://www.youtube.com/watch?v=o_6aujJ5WbM&t=50s',
      'video_id': 'o_6aujJ5WbM'},
     {'author': 'CodeLucky',
      'channel': 'CodeLucky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=hyC9WOKzUMc&t=221s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'Your customer acquisition cost feeds into your monthly recurring revenue which '
              'grows into your annual recurring revenue. Your churn rate directly impacts your '
              'lifetime value. Lower churn increases LTV and lower CAC improves your overall '
              'LTV to CAC ratio.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Your customer acquisition cost feeds into your monthly recurring revenue which '
             'grows into your annual recurring revenue. Your churn rate directly impacts your '
             'lifetime value. Lower churn increases LTV and lower CAC improves your overall '
             'LTV to CAC ratio.',
      'title': 'SaaS Metrics Explained: MRR, ARR, Churn, LTV & CAC | Product Management for '
               'Beginners (CodeLucky)',
      'url': 'https://www.youtube.com/watch?v=hyC9WOKzUMc&t=221s',
      'video_id': 'hyC9WOKzUMc'},
     {'author': 'XRaise',
      'channel': 'XRaise',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=vLchERSjKS8&t=113s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': "So plan for your bill to come back in year two. And they don't cover "
              "everything. Credits work on Google's own cloud products billed by usage. They "
              "can't be used on third-party services, including what you buy through Google "
              'Cloud Marketplace.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "So plan for your bill to come back in year two. And they don't cover everything. "
             "Credits work on Google's own cloud products billed by usage. They can't be used "
             'on third-party services, including what you buy through Google Cloud '
             'Marketplace.',
      'title': 'Google Cloud Credits for Startups 2026: $350K or $2K? (XRaise)',
      'url': 'https://www.youtube.com/watch?v=vLchERSjKS8&t=113s',
      'video_id': 'vLchERSjKS8'},
     {'author': 'Trapture Explains',
      'channel': 'Trapture Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=VmuCPx8GGTU&t=167s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': '150,000 over time as you build with sustained Azure usage. Once those credits '
              'are used, Microsoft says your workload simply move to standard pay as you go '
              "pricing. If you don't qualify for a program yet, there are free tiers.",
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': '150,000 over time as you build with sustained Azure usage. Once those credits '
             'are used, Microsoft says your workload simply move to standard pay as you go '
             "pricing. If you don't qualify for a program yet, there are free tiers.",
      'title': 'Free Cloud Credits for Startups: Tech Stack on a Budget (Trapture Explains)',
      'url': 'https://www.youtube.com/watch?v=VmuCPx8GGTU&t=167s',
      'video_id': 'VmuCPx8GGTU'},
     {'author': 'IBM Technology',
      'channel': 'IBM Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=o0gkdZBtwEg&t=81s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': "You'll submit a long prompt and then wait for a bit. Then suddenly tokens will "
              'stream back fast. That lag before your first token is the model processing your '
              "prompt. This is the pre-fill phase. It's one of the two phases in LLM "
              "inferencing, and it's highly compute bound.",
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "You'll submit a long prompt and then wait for a bit. Then suddenly tokens will "
             'stream back fast. That lag before your first token is the model processing your '
             "prompt. This is the pre-fill phase. It's one of the two phases in LLM "
             "inferencing, and it's highly compute bound.",
      'title': 'How KV Cache Speeds Up LLMs for Faster AI Models on GPUs (IBM Technology)',
      'url': 'https://www.youtube.com/watch?v=o0gkdZBtwEg&t=81s',
      'video_id': 'o0gkdZBtwEg'},
     {'author': 'E Learning by AL SADDAT',
      'channel': 'E Learning by AL SADDAT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=0K7i4CFP_qc&t=52s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'Once the stream completes, settle the exact prompt plus completion tokens cost '
              'and immediately release any unused reserve back to the tenants available '
              'balance. Second, immutable double entry credit ledger. Never overwrite a single '
              'credits integer without an audit trail.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Once the stream completes, settle the exact prompt plus completion tokens cost '
             'and immediately release any unused reserve back to the tenants available '
             'balance. Second, immutable double entry credit ledger. Never overwrite a single '
             'credits integer without an audit trail.',
      'title': 'Real-Time Token Usage Metering, Credit Ledgers & Stripe Billing Webhooks (E '
               'Learning by AL SADDAT)',
      'url': 'https://www.youtube.com/watch?v=0K7i4CFP_qc&t=52s',
      'video_id': '0K7i4CFP_qc'},
     {'author': 'Indie Hacker News',
      'channel': 'Indie Hacker News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=_lbbl0hdJIg&t=135s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'So if your app retries a request, nobody gets built twice. Pricing sits on top '
              'of that. Graduated tiers and packages can live in the same plan as minimum '
              'commitments or plane seats.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'So if your app retries a request, nobody gets built twice. Pricing sits on top '
             'of that. Graduated tiers and packages can live in the same plan as minimum '
             'commitments or plane seats.',
      'title': 'Someone open-sourced Stripe Billing (Mistral uses it) (Indie Hacker News)',
      'url': 'https://www.youtube.com/watch?v=_lbbl0hdJIg&t=135s',
      'video_id': '_lbbl0hdJIg'},
     {'author': 'cruxbits8',
      'channel': 'cruxbits8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=xncObRtKRsw&t=173s)',
      'relevance': 'Attributed practitioner commentary on token/inference metering, '
                   'seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. '
                   'net margins.',
      'source_type': 'video_pro_tip',
      'text': 'After the first turn, almost every input token on every later turn is a cache '
              'read. The whole conversation runs at a tenth of the price. Every response tells '
              'you how many tokens it wrote to the cache, and how many it read back.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'After the first turn, almost every input token on every later turn is a cache '
             'read. The whole conversation runs at a tenth of the price. Every response tells '
             'you how many tokens it wrote to the cache, and how many it read back.',
      'title': 'How Prompt Caching makes LLM calls 10x Cheaper (cruxbits8)',
      'url': 'https://www.youtube.com/watch?v=xncObRtKRsw&t=173s',
      'video_id': 'xncObRtKRsw'}],
 4: [{'author': 'Trapture Explains',
      'channel': 'Trapture Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=VmuCPx8GGTU&t=21s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'When you start, the stack decision feels huge. Which cloud, which database, '
              'which hosting? But for an early product, two simpler questions matter more. '
              "What can I get free and what will I pay every month once it's life? The monthly "
              'bill is the part that stays.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'When you start, the stack decision feels huge. Which cloud, which database, '
             'which hosting? But for an early product, two simpler questions matter more. What '
             "can I get free and what will I pay every month once it's life? The monthly bill "
             'is the part that stays.',
      'title': 'Free Cloud Credits for Startups: Tech Stack on a Budget (Trapture Explains)',
      'url': 'https://www.youtube.com/watch?v=VmuCPx8GGTU&t=21s',
      'video_id': 'VmuCPx8GGTU'},
     {'author': 'InnMind',
      'channel': 'InnMind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=a3Sjk-St_ng&t=139s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'But AWS credits pay for Claude on Amazon Bedrock. So right now AWS is your free '
              'Claude. The other 2 clouds need no partner. Microsoft: up to $5,000 in Azure '
              'credits after they verify your business, & up to $150,000 as you use more. '
              "These credits pay for OpenAI's GPT models.",
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'But AWS credits pay for Claude on Amazon Bedrock. So right now AWS is your free '
             'Claude. The other 2 clouds need no partner. Microsoft: up to $5,000 in Azure '
             'credits after they verify your business, & up to $150,000 as you use more. These '
             "credits pay for OpenAI's GPT models.",
      'title': 'Startup Credits 2026: Up to $48,000 With No Investor (AWS, Claude, Azure, '
               'Google) (InnMind)',
      'url': 'https://www.youtube.com/watch?v=a3Sjk-St_ng&t=139s',
      'video_id': 'a3Sjk-St_ng'},
     {'author': 'Neta Arbel | Growthgrid',
      'channel': 'Neta Arbel | Growthgrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=MO1ZQ4wyWeM&t=135s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': '100,000 in AWS credits that you can use for your cloud usage, go to '
              "cloudcredits. It's not going to cost you any money. I'm going to route you to "
              'an AWS activate provider who will be able to get you the credits.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': '100,000 in AWS credits that you can use for your cloud usage, go to '
             "cloudcredits. It's not going to cost you any money. I'm going to route you to an "
             'AWS activate provider who will be able to get you the credits.',
      'title': 'How to Get $100K in Credits for Claude as a Startup (Neta Arbel | Growthgrid)',
      'url': 'https://www.youtube.com/watch?v=MO1ZQ4wyWeM&t=135s',
      'video_id': 'MO1ZQ4wyWeM'},
     {'author': 'Madhukar Reddy',
      'channel': 'Madhukar Reddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=pX2JNv1VPsQ&t=363s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': "And then here, which AWS topics would like to follow? I think it's elastic "
              "compute cloud. And let's go with AI and machine learning, cost management, AR. "
              'And then you can choose Internet of Things, security, serverless.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': "And then here, which AWS topics would like to follow? I think it's elastic "
             "compute cloud. And let's go with AI and machine learning, cost management, AR. "
             'And then you can choose Internet of Things, security, serverless.',
      'title': 'I Built an AI Startup | Got AWS Credits | AWS Activate Founder Tier (Madhukar '
               'Reddy)',
      'url': 'https://www.youtube.com/watch?v=pX2JNv1VPsQ&t=363s',
      'video_id': 'pX2JNv1VPsQ'},
     {'author': 'Zero Degree Coder',
      'channel': 'Zero Degree Coder',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=K3JxsrRNpBI&t=201s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'Also, please make sure to create your AWS console account as well. So, first '
              'you have to prepare a company email address, then go to the AWS activate. Open '
              'AWS activate /startup/credits. After that, create AWS builder ID.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'Also, please make sure to create your AWS console account as well. So, first you '
             'have to prepare a company email address, then go to the AWS activate. Open AWS '
             'activate /startup/credits. After that, create AWS builder ID.',
      'title': 'How to Get $1,000 FREE AWS Credits for Your Startup (Step-by-Step 2026) (Zero '
               'Degree Coder)',
      'url': 'https://www.youtube.com/watch?v=K3JxsrRNpBI&t=201s',
      'video_id': 'K3JxsrRNpBI'},
     {'author': 'Founder Brief',
      'channel': 'Founder Brief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=DmdDoIC4IgM&t=60s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': "But today, we're looking at a genuinely powerful, verified solution to keep "
              'your equity exactly where it belongs, right in your pocket. So, here is our '
              'blueprint for today. One, unlocking free cloud capital. Two, choosing your '
              'funding tier.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "But today, we're looking at a genuinely powerful, verified solution to keep your "
             'equity exactly where it belongs, right in your pocket. So, here is our blueprint '
             'for today. One, unlocking free cloud capital. Two, choosing your funding tier.',
      'title': 'Up to $350K Google Cloud Credits? How to ApplyGoogleCloud #StartupCredits '
               '#FoundersSecondary (Founder Brief)',
      'url': 'https://www.youtube.com/watch?v=DmdDoIC4IgM&t=60s',
      'video_id': 'DmdDoIC4IgM'},
     {'author': 'Microsoft Developer',
      'channel': 'Microsoft Developer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:52](https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=292s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': "'s built, typically a Postgres database is kind of at the bottom of the stack, "
              'and so that every application on top of the database will at least have the '
              'default security model of your database.',
      'timestamp': 292,
      'timestamp_label': '[00:04:52]',
      'timestamp_seconds': 292,
      'tip': "'s built, typically a Postgres database is kind of at the bottom of the stack, "
             'and so that every application on top of the database will at least have the '
             'default security model of your database.',
      'title': 'Everything you need to know about Postgres Row Level Security | POSETTE 2024 '
               '(Microsoft Developer)',
      'url': 'https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=292s',
      'video_id': 'vZT1Qx2xUCo'},
     {'author': 'Neta Arbel | Growthgrid',
      'channel': 'Neta Arbel | Growthgrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=UEllU5g4QdQ&t=146s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': "'re just an idea, don't try to get the startup packages of credits because you "
              "will simply won't get it. Signal number two is your cloud spend.",
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "'re just an idea, don't try to get the startup packages of credits because you "
             "will simply won't get it. Signal number two is your cloud spend.",
      'title': 'How To Get More AWS/GCP Credits After You Already Used Startup Credits (Neta '
               'Arbel | Growthgrid)',
      'url': 'https://www.youtube.com/watch?v=UEllU5g4QdQ&t=146s',
      'video_id': 'UEllU5g4QdQ'},
     {'author': 'Vinod Sharma',
      'channel': 'Vinod Sharma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=_oN2fQHccDc&t=117s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'And then we will be using a IML not building it. And then uh some description. '
              'So I had this website uh the content from here. So I copy some of the lines '
              'from there. You could say bootstrap or other. I said 25 to 50% because hosting '
              'will be my major expense.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'And then we will be using a IML not building it. And then uh some description. '
             'So I had this website uh the content from here. So I copy some of the lines from '
             'there. You could say bootstrap or other. I said 25 to 50% because hosting will '
             'be my major expense.',
      'title': 'How I Got $1,000 From AWS For My Startup! (Vinod Sharma)',
      'url': 'https://www.youtube.com/watch?v=_oN2fQHccDc&t=117s',
      'video_id': '_oN2fQHccDc'},
     {'author': 'TWiz',
      'channel': 'TWiz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=NwDtEKBC_uo&t=145s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'Open router and Light LLM serve different needs in AI gateway management. Open '
              'router offers broad model access through a flexible open-source API, perfect '
              'for developers wanting variety and cost efficiency across cloud providers.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Open router and Light LLM serve different needs in AI gateway management. Open '
             'router offers broad model access through a flexible open-source API, perfect for '
             'developers wanting variety and cost efficiency across cloud providers.',
      'title': 'OpenRouter vs LiteLLM Which AI Gateway Should You Use (TWiz)',
      'url': 'https://www.youtube.com/watch?v=NwDtEKBC_uo&t=145s',
      'video_id': 'NwDtEKBC_uo'},
     {'author': 'Jono Finds',
      'channel': 'Jono Finds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=XZPNjgJ4E0c&t=142s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'At 100,000 a month in usage, you are paying 5,000 a month for routing. That is '
              '60,000 a year, enough to fund the infrastructure and engineering time to run '
              'your own gateway. Credits expire after a year. Failed requests on the free tier '
              'still count against your daily limit.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'At 100,000 a month in usage, you are paying 5,000 a month for routing. That is '
             '60,000 a year, enough to fund the infrastructure and engineering time to run '
             'your own gateway. Credits expire after a year. Failed requests on the free tier '
             'still count against your daily limit.',
      'title': 'OpenRouter vs LiteLLM: Pay 5% or Host It Yourself? (2026) (Jono Finds)',
      'url': 'https://www.youtube.com/watch?v=XZPNjgJ4E0c&t=142s',
      'video_id': 'XZPNjgJ4E0c'},
     {'author': 'Costoday',
      'channel': 'Costoday',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=aOKH0EoSCCc&t=225s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'Then comes the part that never makes it into the pitch deck, cloud '
              'infrastructure. Hosting a small SAS product reliably with backups, monitoring, '
              'and redundancy across regions easily runs several thousand a month even before '
              'you have meaningful traffic.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'Then comes the part that never makes it into the pitch deck, cloud '
             'infrastructure. Hosting a small SAS product reliably with backups, monitoring, '
             'and redundancy across regions easily runs several thousand a month even before '
             'you have meaningful traffic.',
      'title': 'The Economics of Owning a SaaS Company (Costoday)',
      'url': 'https://www.youtube.com/watch?v=aOKH0EoSCCc&t=225s',
      'video_id': 'aOKH0EoSCCc'},
     {'author': 'XRaise',
      'channel': 'XRaise',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=vLchERSjKS8&t=170s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'Go for the funded tier and plan for year two. Google says these rules change '
              'every year, so check the current terms before you apply. We keep startup '
              'credits, perks, and accelerators in one place at X-rays. The links in the '
              'description.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'Go for the funded tier and plan for year two. Google says these rules change '
             'every year, so check the current terms before you apply. We keep startup '
             'credits, perks, and accelerators in one place at X-rays. The links in the '
             'description.',
      'title': 'Google Cloud Credits for Startups 2026: $350K or $2K? (XRaise)',
      'url': 'https://www.youtube.com/watch?v=vLchERSjKS8&t=170s',
      'video_id': 'vLchERSjKS8'},
     {'author': 'Hunter Sneed',
      'channel': 'Hunter Sneed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:25](https://www.youtube.com/watch?v=raEBR_2VbXE&t=925s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'So, again, if OpenAI goes down, if Anthropic goes down, if a third-party '
              'provider goes down, you can go ahead and route it where you have again '
              "secondary and fall back models, and you don't have to change anything in your "
              "code. It's all just routes to that one endpoint.",
      'timestamp': 925,
      'timestamp_label': '[00:15:25]',
      'timestamp_seconds': 925,
      'tip': 'So, again, if OpenAI goes down, if Anthropic goes down, if a third-party '
             'provider goes down, you can go ahead and route it where you have again secondary '
             "and fall back models, and you don't have to change anything in your code. It's "
             'all just routes to that one endpoint.',
      'title': 'AI Model Routing Explained: Cut LLM Costs With LiteLLM (Hunter Sneed)',
      'url': 'https://www.youtube.com/watch?v=raEBR_2VbXE&t=925s',
      'video_id': 'raEBR_2VbXE'},
     {'author': 'Starter Story',
      'channel': 'Starter Story',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=363s)',
      'relevance': 'Attributed practitioner commentary on cloud/LLM startup credit grants, '
                   'multi-provider API waterfall routers, and near-zero-COGS serverless '
                   'stacks.',
      'source_type': 'video_pro_tip',
      'text': 'Told for affiliate management. On the technical side, we rely heavily on '
              "Entropic's cloud models, GitHub for version control, Vercel for hosting, "
              "Railway for cloud, and Neon for databases. Let's talk about the growth.",
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'Told for affiliate management. On the technical side, we rely heavily on '
             "Entropic's cloud models, GitHub for version control, Vercel for hosting, Railway "
             "for cloud, and Neon for databases. Let's talk about the growth.",
      'title': 'I Built A Micro-Version Of A $1B SaaS. Now I Make $50K/Month (Starter Story)',
      'url': 'https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=363s',
      'video_id': 'Nnpz1wsTjBI'}],
 5: [{'author': 'Spec & Ship',
      'channel': 'Spec & Ship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=QaCS2XJLLm4&t=58s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'Modern model APIs solve this with key-value prefix caching where cached input '
              'tokens cost up to 90% less than fresh input tokens. A KV cache is an exact '
              'byte-for-byte prefix match from the very top of the prompt downward.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Modern model APIs solve this with key-value prefix caching where cached input '
             'tokens cost up to 90% less than fresh input tokens. A KV cache is an exact '
             'byte-for-byte prefix match from the very top of the prompt downward.',
      'title': 'Why Your Claude Code Limit Vanishes: Cut AI Coding Costs by 70% with Cache & '
               'Model Routing (Spec & Ship)',
      'url': 'https://www.youtube.com/watch?v=QaCS2XJLLm4&t=58s',
      'video_id': 'QaCS2XJLLm4'},
     {'author': 'Learn with Vichu',
      'channel': 'Learn with Vichu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=rECbImLOxqg&t=21s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'Send the same million tokens twice. Cache writes cost more than normal input. '
              'So, how does caching still save 90%? Put a timestamp at the top of your prompt '
              'and the cache never hits. Why can one extra token double the price of the whole '
              'request?',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Send the same million tokens twice. Cache writes cost more than normal input. '
             'So, how does caching still save 90%? Put a timestamp at the top of your prompt '
             'and the cache never hits. Why can one extra token double the price of the whole '
             'request?',
      'title': 'How Prompt Caching Saves 90% (GPT-6 Astra) – Cut Your LLM API Bill (Learn with '
               'Vichu)',
      'url': 'https://www.youtube.com/watch?v=rECbImLOxqg&t=21s',
      'video_id': 'rECbImLOxqg'},
     {'author': 'The Macroscope',
      'channel': 'The Macroscope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=uTTjkSZnkDI&t=278s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': '" The semantic cache recognizes they mean the exact same thing and just serves '
              'the stored response. You literally skip the generation latency and the API cost '
              "entirely. You've also got to implement cascading model routing.",
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': '" The semantic cache recognizes they mean the exact same thing and just serves '
             'the stored response. You literally skip the generation latency and the API cost '
             "entirely. You've also got to implement cascading model routing.",
      'title': 'Stop Wasting AI Tokens: The Ultimate LLM Cost Reduction Guide (Save 90%!) (The '
               'Macroscope)',
      'url': 'https://www.youtube.com/watch?v=uTTjkSZnkDI&t=278s',
      'video_id': 'uTTjkSZnkDI'},
     {'author': 'AmanAI Lab',
      'channel': 'AmanAI Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:42](https://www.youtube.com/watch?v=QaVJRXlOcV4&t=822s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'I will need the Groq API key and have created a cost optimization agent, and '
              'after that , let me tell you, I am handling it in three ways. Meaning, for '
              'demonstration purposes, I have created it. I am handling three questions. '
              'First, I wrote a question for cache miss.',
      'timestamp': 822,
      'timestamp_label': '[00:13:42]',
      'timestamp_seconds': 822,
      'tip': 'I will need the Groq API key and have created a cost optimization agent, and '
             'after that , let me tell you, I am handling it in three ways. Meaning, for '
             'demonstration purposes, I have created it. I am handling three questions. First, '
             'I wrote a question for cache miss.',
      'title': 'Prompt Caching & Cost Optimization for AI Agents | Reduce LLM Cost & Latency '
               '(AmanAI Lab)',
      'url': 'https://www.youtube.com/watch?v=QaVJRXlOcV4&t=822s',
      'video_id': 'QaVJRXlOcV4'},
     {'author': 'Webronaq',
      'channel': 'Webronaq',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:40](https://www.youtube.com/watch?v=6rvk2w3y7K0&t=280s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'That single change often covers most of your bill. Step three: enable prompt '
              'caching at the gateway. Coinbase took its cache hit rate from 5 percent to 60 '
              'percent. Even a 30 percent hit rate meaningfully cuts costs. Step four: add a '
              'quality fallback chain.',
      'timestamp': 280,
      'timestamp_label': '[00:04:40]',
      'timestamp_seconds': 280,
      'tip': 'That single change often covers most of your bill. Step three: enable prompt '
             'caching at the gateway. Coinbase took its cache hit rate from 5 percent to 60 '
             'percent. Even a 30 percent hit rate meaningfully cuts costs. Step four: add a '
             'quality fallback chain.',
      'title': 'LLM Model Routing: Cut AI API Costs by 80 Percent (Webronaq)',
      'url': 'https://www.youtube.com/watch?v=6rvk2w3y7K0&t=280s',
      'video_id': '6rvk2w3y7K0'},
     {'author': 'Mastra',
      'channel': 'Mastra',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=eBB0dBqfvuQ&t=167s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'Project Discovery, the team behind Neqo, an autonomous security testing '
              'platform, were only getting a 7% cache hit because their working memory changed '
              'on nearly every step, which kept invalidating the bulk of their cache.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'Project Discovery, the team behind Neqo, an autonomous security testing '
             'platform, were only getting a 7% cache hit because their working memory changed '
             'on nearly every step, which kept invalidating the bulk of their cache.',
      'title': 'Prompt Caching Reduced My Agent Costs by 90% (Mastra)',
      'url': 'https://www.youtube.com/watch?v=eBB0dBqfvuQ&t=167s',
      'video_id': 'eBB0dBqfvuQ'},
     {'author': 'cruxbits8',
      'channel': 'cruxbits8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=xncObRtKRsw&t=77s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'Writing into the cache the first time costs a small premium, 1 and 1/4 times '
              'the normal rate. You pay a little extra once to save a lot every time after. A '
              'write costs 1 and 1/4 times, a read costs a 10th. So, caching pays for itself '
              'after just one hit.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Writing into the cache the first time costs a small premium, 1 and 1/4 times the '
             'normal rate. You pay a little extra once to save a lot every time after. A write '
             'costs 1 and 1/4 times, a read costs a 10th. So, caching pays for itself after '
             'just one hit.',
      'title': 'How Prompt Caching makes LLM calls 10x Cheaper (cruxbits8)',
      'url': 'https://www.youtube.com/watch?v=xncObRtKRsw&t=77s',
      'video_id': 'xncObRtKRsw'},
     {'author': 'ClankerEngineer',
      'channel': 'ClankerEngineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=4x4nM0uPmg0&t=180s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'LLM calls are costing you the most, which ones are taking the longest time. '
              "It's a great way of evaluating your application. While on the topic of caching, "
              "it's a very important part not only for cost management, but in a chatbot like "
              'this, latency is of course critical.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': "LLM calls are costing you the most, which ones are taking the longest time. It's "
             "a great way of evaluating your application. While on the topic of caching, it's "
             'a very important part not only for cost management, but in a chatbot like this, '
             'latency is of course critical.',
      'title': 'How I cut token costs by 90%: AI cost optimization guide (ClankerEngineer)',
      'url': 'https://www.youtube.com/watch?v=4x4nM0uPmg0&t=180s',
      'video_id': '4x4nM0uPmg0'},
     {'author': 'Efficient NLP',
      'channel': 'Efficient NLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=Q_U4pRggC5I&t=314s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': '5 minutes, 1 hour, or not at all. As we mentioned before, prompt caching is not '
              'free and telling the server to cache it increases the cost per token depending '
              'on the length of time you want to have it cached.',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': '5 minutes, 1 hour, or not at all. As we mentioned before, prompt caching is not '
             'free and telling the server to cache it increases the cost per token depending '
             'on the length of time you want to have it cached.',
      'title': 'Why agents recompute the same prompt, and how prompt caching fixes it '
               '(Efficient NLP)',
      'url': 'https://www.youtube.com/watch?v=Q_U4pRggC5I&t=314s',
      'video_id': 'Q_U4pRggC5I'},
     {'author': 'IBM Technology',
      'channel': 'IBM Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=u57EnkQaUTY&t=178s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'This is the prefilled phase that happens before the LLM actually can generate '
              'its first token of output. So what we can do is cache the KV pairs. So this '
              'here is where the prompt caching actually applies. It stores these precomputed '
              'KV pairs.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'This is the prefilled phase that happens before the LLM actually can generate '
             'its first token of output. So what we can do is cache the KV pairs. So this here '
             'is where the prompt caching actually applies. It stores these precomputed KV '
             'pairs.',
      'title': 'What is Prompt Caching? Optimize LLM Latency with AI Transformers (IBM '
               'Technology)',
      'url': 'https://www.youtube.com/watch?v=u57EnkQaUTY&t=178s',
      'video_id': 'u57EnkQaUTY'},
     {'author': 'Engineering Insider',
      'channel': 'Engineering Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=0-5l8CAjz6I&t=197s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'And Gemini offers around a 75% reduction. This layer alone can basically slash '
              'that system prompt cost we just talked about. Provider caching only handles '
              'identical prefixes. Semantic caching is your custom layer for the trickier '
              'stuff. And how do I return an item?',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'And Gemini offers around a 75% reduction. This layer alone can basically slash '
             'that system prompt cost we just talked about. Provider caching only handles '
             'identical prefixes. Semantic caching is your custom layer for the trickier '
             'stuff. And how do I return an item?',
      'title': 'How to Reduce AI App Costs: Caching, Model Routing, and LLM Optimization '
               '(Engineering Insider)',
      'url': 'https://www.youtube.com/watch?v=0-5l8CAjz6I&t=197s',
      'video_id': '0-5l8CAjz6I'},
     {'author': 'Bryan Software',
      'channel': 'Bryan Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:53](https://www.youtube.com/watch?v=SDB5hKMHUA8&t=293s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'You source and manage every model yourself, and its practical context ceiling '
              'tops out closer to 1 million tokens through its cost map. For raw reach and '
              'instant access, OpenRouter wins this test clean. Light LLM does give you more '
              'control over rate limits.',
      'timestamp': 293,
      'timestamp_label': '[00:04:53]',
      'timestamp_seconds': 293,
      'tip': 'You source and manage every model yourself, and its practical context ceiling '
             'tops out closer to 1 million tokens through its cost map. For raw reach and '
             'instant access, OpenRouter wins this test clean. Light LLM does give you more '
             'control over rate limits.',
      'title': 'OpenRouter vs LiteLLM: Which Should You Self-Host? (Bryan Software)',
      'url': 'https://www.youtube.com/watch?v=SDB5hKMHUA8&t=293s',
      'video_id': 'SDB5hKMHUA8'},
     {'author': 'BuilderJoy',
      'channel': 'BuilderJoy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=iNadOdD_hxI&t=62s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': 'Bien, primeramente cuando nosotros trabajamos sin lo que es Road Level Security '
              'o los RLS, nosotros tenemos un cliente que consulta una API y manda un out '
              'token.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'Bien, primeramente cuando nosotros trabajamos sin lo que es Road Level Security '
             'o los RLS, nosotros tenemos un cliente que consulta una API y manda un out '
             'token.',
      'title': 'Supabase RLS: Cómo Proteger tus Datos con Row Level Security (Guía Completa) '
               '(BuilderJoy)',
      'url': 'https://www.youtube.com/watch?v=iNadOdD_hxI&t=62s',
      'video_id': 'iNadOdD_hxI'},
     {'author': 'Alex Rusin',
      'channel': 'Alex Rusin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:08](https://www.youtube.com/watch?v=ctJy5AxgVXM&t=608s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': "The get people route is just an order by now. Let's run npm run dev and go to "
              "API test. We can get A's people, we can get B's people and be hitting an unsafe "
              "route gets 404. Now let's close that right hole. Let's go ahead and prompt "
              'Cloud Code add with check to the policy.',
      'timestamp': 608,
      'timestamp_label': '[00:10:08]',
      'timestamp_seconds': 608,
      'tip': "The get people route is just an order by now. Let's run npm run dev and go to "
             "API test. We can get A's people, we can get B's people and be hitting an unsafe "
             "route gets 404. Now let's close that right hole. Let's go ahead and prompt Cloud "
             'Code add with check to the policy.',
      'title': "Claude Code + Prisma: Multi-Tenant Postgres API That Can't Leak Data (Alex "
               'Rusin)',
      'url': 'https://www.youtube.com/watch?v=ctJy5AxgVXM&t=608s',
      'video_id': 'ctJy5AxgVXM'},
     {'author': 'Hugging Face',
      'channel': 'Hugging Face',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:38](https://www.youtube.com/watch?v=SkM4k4SKvCM&t=998s)',
      'relevance': 'Attributed practitioner commentary on runaway LLM token bills, prompt '
                   'injection, model drift, involuntary churn, and single-vendor API lock-in.',
      'source_type': 'video_pro_tip',
      'text': "So, for example, right here, I'm using Pi, and as you can see right here, you "
              'see CH, that is the cache hit rate for this particular provider. In this case, '
              "I'm using Kimi K3. And if you're using Tau, you have it right here on the "
              'right.',
      'timestamp': 998,
      'timestamp_label': '[00:16:38]',
      'timestamp_seconds': 998,
      'tip': "So, for example, right here, I'm using Pi, and as you can see right here, you "
             'see CH, that is the cache hit rate for this particular provider. In this case, '
             "I'm using Kimi K3. And if you're using Tau, you have it right here on the right.",
      'title': 'Prompt Caching Explained: Stop Overpaying for AI Agents (Hugging Face)',
      'url': 'https://www.youtube.com/watch?v=SkM4k4SKvCM&t=998s',
      'video_id': 'SkM4k4SKvCM'}],
 6: [{'author': 'Rob Walling',
      'channel': 'Rob Walling',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:39](https://www.youtube.com/watch?v=6sgCo6fMSGY&t=939s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'The second is the clients are literally paying you to understand their '
              "problems. You're getting paid to do market research and customer development. "
              "The third is you build real expertise in the domain as you're getting paid.",
      'timestamp': 939,
      'timestamp_label': '[00:15:39]',
      'timestamp_seconds': 939,
      'tip': 'The second is the clients are literally paying you to understand their problems. '
             "You're getting paid to do market research and customer development. The third is "
             "you build real expertise in the domain as you're getting paid.",
      'title': "Give Me 36 Minutes and I'll Teach You How to Find $1M SaaS Ideas (Rob Walling)",
      'url': 'https://www.youtube.com/watch?v=6sgCo6fMSGY&t=939s',
      'video_id': '6sgCo6fMSGY'},
     {'author': 'TechFuelAI',
      'channel': 'TechFuelAI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=9Rig_F79rWo&t=224s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'So, before you write a single line of code, your idea has to pass a crucial '
              'test. Can AI just fabricate this? To survive, you need at least one of these '
              'three moats. Think authentic, verified practitioner reviews. An AI can easily '
              'write a fake review, right?',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'So, before you write a single line of code, your idea has to pass a crucial '
             'test. Can AI just fabricate this? To survive, you need at least one of these '
             'three moats. Think authentic, verified practitioner reviews. An AI can easily '
             'write a fake review, right?',
      'title': 'Micro-SaaS in 2026 🚀 | Build a Profitable SaaS Business with Just $50/Month '
               '(TechFuelAI)',
      'url': 'https://www.youtube.com/watch?v=9Rig_F79rWo&t=224s',
      'video_id': '9Rig_F79rWo'},
     {'author': 'Fomin Unscripted',
      'channel': 'Fomin Unscripted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=xWcG7R7Xm2Y&t=98s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': "That's what I'm looking for. And I'm not saying you need to find some "
              "completely new idea that nobody's ever thought of. Honestly, I'd rather build "
              'something in a market where people are already paying for solutions. At least '
              'you know there is demand.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': "That's what I'm looking for. And I'm not saying you need to find some completely "
             "new idea that nobody's ever thought of. Honestly, I'd rather build something in "
             'a market where people are already paying for solutions. At least you know there '
             'is demand.',
      'title': 'how to scale a micro SaaS to $10k MRR with zero ad spend (Fomin Unscripted)',
      'url': 'https://www.youtube.com/watch?v=xWcG7R7Xm2Y&t=98s',
      'video_id': 'xWcG7R7Xm2Y'},
     {'author': 'Starter Story',
      'channel': 'Starter Story',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:53](https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=653s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': '"Every business idea is taken. That\'s Here\'s like a list of 50 ways to make '
              'your app different." Starting something brand new, yeah, it seems like '
              "impossible. The thing is that you don't need to execute perfectly if you are "
              'just in a good market or a good niche.',
      'timestamp': 653,
      'timestamp_label': '[00:10:53]',
      'timestamp_seconds': 653,
      'tip': '"Every business idea is taken. That\'s Here\'s like a list of 50 ways to make '
             'your app different." Starting something brand new, yeah, it seems like '
             "impossible. The thing is that you don't need to execute perfectly if you are "
             'just in a good market or a good niche.',
      'title': 'I Built A Micro-Version Of A $1B SaaS. Now I Make $50K/Month (Starter Story)',
      'url': 'https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=653s',
      'video_id': 'Nnpz1wsTjBI'},
     {'author': "Bootstrapper's Paradise",
      'channel': "Bootstrapper's Paradise",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=GK9LZkd6aHM&t=133s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'But building a billing automation tool built specifically for small law firms '
              "like the app I'm building in public called Clockless understands the domain, "
              "speaks the language, and solves the exact problem. Enterprise giants can't go "
              'this deep into every niche.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'But building a billing automation tool built specifically for small law firms '
             "like the app I'm building in public called Clockless understands the domain, "
             "speaks the language, and solves the exact problem. Enterprise giants can't go "
             'this deep into every niche.',
      'title': "Vertical AI vs Traditional SaaS | Game Over (Bootstrapper's Paradise)",
      'url': 'https://www.youtube.com/watch?v=GK9LZkd6aHM&t=133s',
      'video_id': 'GK9LZkd6aHM'},
     {'author': 'Simon Høiberg',
      'channel': 'Simon Høiberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=QIA9Ry42Lbs&t=81s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'AI character of yourself, then use that character to create AI generated B-roll '
              'clips. So, this SAS is solving a problem I have myself and I know a few other '
              "people who have the same problem, but it's not a big market and that's the "
              'whole point.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'AI character of yourself, then use that character to create AI generated B-roll '
             'clips. So, this SAS is solving a problem I have myself and I know a few other '
             "people who have the same problem, but it's not a big market and that's the whole "
             'point.',
      'title': 'Get rich building niche AI SaaS (...not another ChatGPT wrapper) (Simon '
               'Høiberg)',
      'url': 'https://www.youtube.com/watch?v=QIA9Ry42Lbs&t=81s',
      'video_id': 'QIA9Ry42Lbs'},
     {'author': 'Greg Isenberg',
      'channel': 'Greg Isenberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=ndqX4vbR7Rc&t=268s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': "I have I I have I felt this pain point. So, um you're you're starting starting "
              'to notice that a lot of these um ideas have like very good brand, very big pain '
              'point clear.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': "I have I I have I felt this pain point. So, um you're you're starting starting "
             'to notice that a lot of these um ideas have like very good brand, very big pain '
             'point clear.',
      'title': 'Making $$$ with MicroSaaS (Greg Isenberg)',
      'url': 'https://www.youtube.com/watch?v=ndqX4vbR7Rc&t=268s',
      'video_id': 'ndqX4vbR7Rc'},
     {'author': 'Stripe Developers',
      'channel': 'Stripe Developers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=j7TlXzIV4uo&t=94s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'So this could range from chat apps to games, even to writing assistants or '
              'other AI assistants, AI agents that are, you know, more niche for a particular '
              'domain. And even a coding or, like, dev tools that will allow for, you know, '
              'creating new projects as well.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'So this could range from chat apps to games, even to writing assistants or other '
             'AI assistants, AI agents that are, you know, more niche for a particular domain. '
             'And even a coding or, like, dev tools that will allow for, you know, creating '
             'new projects as well.',
      'title': 'Token billing for LLM apps | live demo with Metronome + Stripe (Stripe '
               'Developers)',
      'url': 'https://www.youtube.com/watch?v=j7TlXzIV4uo&t=94s',
      'video_id': 'j7TlXzIV4uo'},
     {'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=i05UCC3UvNY&t=343s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': "'ve reached the one hundred dollar minimum. Paddle also reviews new accounts. "
              'That includes a domain review and identity verification, plus business '
              "verification for companies. It isn't required for individuals or sole traders. "
              'NOVA: Wait, Stripe does that too now?',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': "'ve reached the one hundred dollar minimum. Paddle also reviews new accounts. "
             'That includes a domain review and identity verification, plus business '
             "verification for companies. It isn't required for individuals or sole traders. "
             'NOVA: Wait, Stripe does that too now?',
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=343s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'Fomin Unscripted',
      'channel': 'Fomin Unscripted',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=8lmA9UgwNQs&t=32s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'I actually do the opposite. I look for things people are already paying for. If '
              'thousands of people are already paying for something, you know there is market '
              "for it. You don't have to guess whether people want it. You already know there "
              'is demand.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'I actually do the opposite. I look for things people are already paying for. If '
             'thousands of people are already paying for something, you know there is market '
             "for it. You don't have to guess whether people want it. You already know there "
             'is demand.',
      'title': 'how to find saas ideas worth $10,000,000 (steal this method) (Fomin '
               'Unscripted)',
      'url': 'https://www.youtube.com/watch?v=8lmA9UgwNQs&t=32s',
      'video_id': '8lmA9UgwNQs'},
     {'author': 'Mikey No Code',
      'channel': 'Mikey No Code',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:18](https://www.youtube.com/watch?v=aQZkra1kEcg&t=738s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': "'s stack a second filter because this next one eliminates weak ideas fast. And "
              "it's the problem-pay matrix. So, now we're going to add a second filter, and "
              'this one protects you from building something that looks good on paper, maybe, '
              "but won't make money in reality.",
      'timestamp': 738,
      'timestamp_label': '[00:12:18]',
      'timestamp_seconds': 738,
      'tip': "'s stack a second filter because this next one eliminates weak ideas fast. And "
             "it's the problem-pay matrix. So, now we're going to add a second filter, and "
             'this one protects you from building something that looks good on paper, maybe, '
             "but won't make money in reality.",
      'title': 'Micro Saas Tutorial for Beginners: How to Build a SaaS with AI (2026) (Mikey '
               'No Code)',
      'url': 'https://www.youtube.com/watch?v=aQZkra1kEcg&t=738s',
      'video_id': 'aQZkra1kEcg'},
     {'author': 'Zues Ordaz',
      'channel': 'Zues Ordaz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=457s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': "SaaS aren't the ones with the most coding experience. They're the ones who "
              'identified the right problem, built the right solution, and got it in front of '
              'the right people fast. Base 44 handles the build, you bring the business idea.',
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': "SaaS aren't the ones with the most coding experience. They're the ones who "
             'identified the right problem, built the right solution, and got it in front of '
             'the right people fast. Base 44 handles the build, you bring the business idea.',
      'title': 'The Micro SaaS Business Almost Nobody Is Building (Until Now) (Zues Ordaz)',
      'url': 'https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=457s',
      'video_id': 'I-4eEpO2G0Q'},
     {'author': 'Sabyr Nurgaliyev',
      'channel': 'Sabyr Nurgaliyev',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=YVRP3QoP6bs&t=83s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'And Reddit is a step to get there. Meet Viewst, a B2B SaaS that turn one ad '
              'creative into hundreds of HTML5 banners for marketing teams. Solid product, '
              'zero reviews, but completely invisible to AI search. Day zero, ChatGPT '
              'citations zero. Page cited by ChatGPT zero.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'And Reddit is a step to get there. Meet Viewst, a B2B SaaS that turn one ad '
             'creative into hundreds of HTML5 banners for marketing teams. Solid product, zero '
             'reviews, but completely invisible to AI search. Day zero, ChatGPT citations '
             'zero. Page cited by ChatGPT zero.',
      'title': 'I Ranked a B2B SaaS on ChatGPT in 30 Days With Reddit (Sabyr Nurgaliyev)',
      'url': 'https://www.youtube.com/watch?v=YVRP3QoP6bs&t=83s',
      'video_id': 'YVRP3QoP6bs'},
     {'author': 'Ampvoro',
      'channel': 'Ampvoro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=fGLomKpo_LI&t=102s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'This connects the customer to the recurring plan you set up earlier. Before '
              "moving forward, review the billing details carefully. It's always a good idea "
              'to double-check the customer, product, and pricing information to avoid '
              'mistakes.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'This connects the customer to the recurring plan you set up earlier. Before '
             "moving forward, review the billing details carefully. It's always a good idea to "
             'double-check the customer, product, and pricing information to avoid mistakes.',
      'title': 'How to Set Up Stripe Billing for Subscriptions [2026 Full Tutorial] (Ampvoro)',
      'url': 'https://www.youtube.com/watch?v=fGLomKpo_LI&t=102s',
      'video_id': 'fGLomKpo_LI'},
     {'author': 'Business Beast Mode',
      'channel': 'Business Beast Mode',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=iGqudu6WmHs&t=20s)',
      'relevance': 'Attributed practitioner commentary on technographic churn scraping, '
                   'automated ADA/review diagnostic scanners, Reddit pain mining, and '
                   'paid-pilot validation.',
      'source_type': 'video_pro_tip',
      'text': 'We sell our most basic package is 60 bucks a month, and we also sell for like '
              '360 for the year. So, we try to do annuals as much as possible to reduce churn. '
              'So, what we need to So, what are the activation signals that you have '
              'determined so far?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'We sell our most basic package is 60 bucks a month, and we also sell for like '
             '360 for the year. So, we try to do annuals as much as possible to reduce churn. '
             'So, what we need to So, what are the activation signals that you have determined '
             'so far?',
      'title': 'Alex Hormozi: Fix SaaS Churn With This Onboarding Strategy (AMA) (Business '
               'Beast Mode)',
      'url': 'https://www.youtube.com/watch?v=iGqudu6WmHs&t=20s',
      'video_id': 'iGqudu6WmHs'}],
 7: [{'author': 'Webronaq',
      'channel': 'Webronaq',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=6rvk2w3y7K0&t=221s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'In March 2026, Portkey released Gateway 2. 0 as fully open source under Apache '
              '2. 0, opening its entire production feature set to self-hosters. That includes '
              'semantic caching, guardrails for PII redaction, and support for more than 1,600 '
              'models.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'In March 2026, Portkey released Gateway 2. 0 as fully open source under Apache '
             '2. 0, opening its entire production feature set to self-hosters. That includes '
             'semantic caching, guardrails for PII redaction, and support for more than 1,600 '
             'models.',
      'title': 'LLM Model Routing: Cut AI API Costs by 80 Percent (Webronaq)',
      'url': 'https://www.youtube.com/watch?v=6rvk2w3y7K0&t=221s',
      'video_id': '6rvk2w3y7K0'},
     {'author': 'IBM Technology',
      'channel': 'IBM Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:37](https://www.youtube.com/watch?v=u57EnkQaUTY&t=517s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'But some providers actually require you to explicitly mark which parts of your '
              'prompt should be cached in your API calls. So these are the explicit types of '
              "caching. So, so, that's prompt caching. And with the right use case it's a way "
              'to reduce LLM costs and latency.',
      'timestamp': 517,
      'timestamp_label': '[00:08:37]',
      'timestamp_seconds': 517,
      'tip': 'But some providers actually require you to explicitly mark which parts of your '
             'prompt should be cached in your API calls. So these are the explicit types of '
             "caching. So, so, that's prompt caching. And with the right use case it's a way "
             'to reduce LLM costs and latency.',
      'title': 'What is Prompt Caching? Optimize LLM Latency with AI Transformers (IBM '
               'Technology)',
      'url': 'https://www.youtube.com/watch?v=u57EnkQaUTY&t=517s',
      'video_id': 'u57EnkQaUTY'},
     {'author': 'Efficient NLP',
      'channel': 'Efficient NLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=Q_U4pRggC5I&t=300s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'Different API providers expose different ways for developers to control prompt '
              'caching. Anthropic exposes our cache control mechanism that lets you control '
              'exactly how long you want each part of the prompt to be cached, whether for 5 '
              'minutes, 1 hour, or not at all.',
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': 'Different API providers expose different ways for developers to control prompt '
             'caching. Anthropic exposes our cache control mechanism that lets you control '
             'exactly how long you want each part of the prompt to be cached, whether for 5 '
             'minutes, 1 hour, or not at all.',
      'title': 'Why agents recompute the same prompt, and how prompt caching fixes it '
               '(Efficient NLP)',
      'url': 'https://www.youtube.com/watch?v=Q_U4pRggC5I&t=300s',
      'video_id': 'Q_U4pRggC5I'},
     {'author': 'E Learning by AL SADDAT',
      'channel': 'E Learning by AL SADDAT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=0K7i4CFP_qc&t=86s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': "IDs so retried web hooks never grant duplicate credits. Let's build a clean "
              'rockolid AI credit ledger and Stripe billing web hook service. The tenant '
              'credit ledger maintains available credits, reserved holds, and a full ledger '
              'history.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': "IDs so retried web hooks never grant duplicate credits. Let's build a clean "
             'rockolid AI credit ledger and Stripe billing web hook service. The tenant credit '
             'ledger maintains available credits, reserved holds, and a full ledger history.',
      'title': 'Real-Time Token Usage Metering, Credit Ledgers & Stripe Billing Webhooks (E '
               'Learning by AL SADDAT)',
      'url': 'https://www.youtube.com/watch?v=0K7i4CFP_qc&t=86s',
      'video_id': '0K7i4CFP_qc'},
     {'author': 'Skillfyme',
      'channel': 'Skillfyme',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:15](https://www.youtube.com/watch?v=aYNSsflxcwg&t=2535s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': "I mentioned a Redis server has to be up and running okay so that's a additional "
              'additional overhead but it works well in the production setup. Okay so yeah so '
              "that's how the Redis cache work I mean you can try it when you have your ready "
              'server up and running.',
      'timestamp': 2535,
      'timestamp_label': '[00:42:15]',
      'timestamp_seconds': 2535,
      'tip': "I mentioned a Redis server has to be up and running okay so that's a additional "
             'additional overhead but it works well in the production setup. Okay so yeah so '
             "that's how the Redis cache work I mean you can try it when you have your ready "
             'server up and running.',
      'title': 'Reduce LLM API Costs with Caching & Smart Model Routing | LangChain '
               '(Skillfyme)',
      'url': 'https://www.youtube.com/watch?v=aYNSsflxcwg&t=2535s',
      'video_id': 'aYNSsflxcwg'},
     {'author': 'Hugging Face',
      'channel': 'Hugging Face',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:05](https://www.youtube.com/watch?v=SkM4k4SKvCM&t=725s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'On Anthropic, it is five minutes by default, if I remember correctly, on the '
              "API, and one hour if you're authenticated with Claude Code, etc. But as you can "
              'see here, it was full cache, and then right here is where I went for lunch.',
      'timestamp': 725,
      'timestamp_label': '[00:12:05]',
      'timestamp_seconds': 725,
      'tip': 'On Anthropic, it is five minutes by default, if I remember correctly, on the '
             "API, and one hour if you're authenticated with Claude Code, etc. But as you can "
             'see here, it was full cache, and then right here is where I went for lunch.',
      'title': 'Prompt Caching Explained: Stop Overpaying for AI Agents (Hugging Face)',
      'url': 'https://www.youtube.com/watch?v=SkM4k4SKvCM&t=725s',
      'video_id': 'SkM4k4SKvCM'},
     {'author': 'Engineering Insider',
      'channel': 'Engineering Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=0-5l8CAjz6I&t=54s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'You build a beautifully functioning rag chatbot. Your users absolutely love it. '
              'And then, bam, you get hit with this staggering number, 22 and a half grand.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'You build a beautifully functioning rag chatbot. Your users absolutely love it. '
             'And then, bam, you get hit with this staggering number, 22 and a half grand.',
      'title': 'How to Reduce AI App Costs: Caching, Model Routing, and LLM Optimization '
               '(Engineering Insider)',
      'url': 'https://www.youtube.com/watch?v=0-5l8CAjz6I&t=54s',
      'video_id': '0-5l8CAjz6I'},
     {'author': 'International PHP Conference',
      'channel': 'International PHP Conference',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=DabJ0hxiXAo&t=140s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'So, if the tenant context is completely missing, it evaluates to a safe empty '
              'result. Until a specific policy is written, non-super user roles will see '
              'exactly zero rows. To build complete isolation, the article details creating a '
              'dual-layered policy.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'So, if the tenant context is completely missing, it evaluates to a safe empty '
             'result. Until a specific policy is written, non-super user roles will see '
             'exactly zero rows. To build complete isolation, the article details creating a '
             'dual-layered policy.',
      'title': 'PostgreSQL RLS for Safer Multi-Tenant SaaS (International PHP Conference)',
      'url': 'https://www.youtube.com/watch?v=DabJ0hxiXAo&t=140s',
      'video_id': 'DabJ0hxiXAo'},
     {'author': 'Past The Diagram',
      'channel': 'Past The Diagram',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=h1KAW_izGl8&t=20s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'API or from a psql session someone opened at midnight. It is called row-level '
              'security, and once it is on, the query I showed you in episode 1, the one with '
              'no tenant filter, returns exactly the rows it should and nothing else.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'API or from a psql session someone opened at midnight. It is called row-level '
             'security, and once it is on, the query I showed you in episode 1, the one with '
             'no tenant filter, returns exactly the rows it should and nothing else.',
      'title': 'Postgres Row-Level Security for Multi-Tenant SaaS (Past The Diagram)',
      'url': 'https://www.youtube.com/watch?v=h1KAW_izGl8&t=20s',
      'video_id': 'h1KAW_izGl8'},
     {'author': 'AmanAI Lab',
      'channel': 'AmanAI Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:04](https://www.youtube.com/watch?v=QaVJRXlOcV4&t=604s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'Plus, you will really have to implement this as well. Sorry, you will have to '
              'implement this as well. Now I will show you an architecture. We will implement '
              'this same architecture through coding. First, they checked the exact cache.',
      'timestamp': 604,
      'timestamp_label': '[00:10:04]',
      'timestamp_seconds': 604,
      'tip': 'Plus, you will really have to implement this as well. Sorry, you will have to '
             'implement this as well. Now I will show you an architecture. We will implement '
             'this same architecture through coding. First, they checked the exact cache.',
      'title': 'Prompt Caching & Cost Optimization for AI Agents | Reduce LLM Cost & Latency '
               '(AmanAI Lab)',
      'url': 'https://www.youtube.com/watch?v=QaVJRXlOcV4&t=604s',
      'video_id': 'QaVJRXlOcV4'},
     {'author': 'Supabase',
      'channel': 'Supabase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=Ow_Uzedfohk&t=22s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': "So let's learn how so most people have this mental model of this kind of "
              'three-piece architecture where you have a client an api and a database and the '
              'client is only able to directly communicate.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "So let's learn how so most people have this mental model of this kind of "
             'three-piece architecture where you have a client an api and a database and the '
             'client is only able to directly communicate.',
      'title': 'Implement Authorization using Row Level Security (RLS) with Supabase (Step By '
               'Step Guide) (Supabase)',
      'url': 'https://www.youtube.com/watch?v=Ow_Uzedfohk&t=22s',
      'video_id': 'Ow_Uzedfohk'},
     {'author': 'cruxbits8',
      'channel': 'cruxbits8',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=xncObRtKRsw&t=109s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'Every cached question after that, 50 cents. 50 cents versus $5 over and over. '
              'Turning it on is almost nothing. You add a single cache control marker to the '
              'part you want stored. Your system prompt, your tools, that handbook, and the '
              'API handles the rest.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'Every cached question after that, 50 cents. 50 cents versus $5 over and over. '
             'Turning it on is almost nothing. You add a single cache control marker to the '
             'part you want stored. Your system prompt, your tools, that handbook, and the API '
             'handles the rest.',
      'title': 'How Prompt Caching makes LLM calls 10x Cheaper (cruxbits8)',
      'url': 'https://www.youtube.com/watch?v=xncObRtKRsw&t=109s',
      'video_id': 'xncObRtKRsw'},
     {'author': 'YourTechGuru',
      'channel': 'YourTechGuru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=6EoRbAAAE-8&t=76s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'With Light LLM, you can have multi-API calling capabilities, custom load '
              'balancing algorithms, semantic caching, and failover chains, all without ever '
              'having to trust your data or infrastructure to others.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': 'With Light LLM, you can have multi-API calling capabilities, custom load '
             'balancing algorithms, semantic caching, and failover chains, all without ever '
             'having to trust your data or infrastructure to others.',
      'title': 'OpenRouter vs LiteLLM (2026): Which Is The Best LLM Tool For Production? '
               '(YourTechGuru)',
      'url': 'https://www.youtube.com/watch?v=6EoRbAAAE-8&t=76s',
      'video_id': '6EoRbAAAE-8'},
     {'author': 'Verticals: A Weekly Biz Show On Vertical AI',
      'channel': 'Verticals: A Weekly Biz Show On Vertical AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:59](https://www.youtube.com/watch?v=y6eOdHpH5W8&t=1319s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'Um, another key learning has been that while every vertical SAS gets a foot in '
              'the door with one aha moment, one veg or key feature, in order to really build '
              'a fort, you have to be solving for many different business needs um over time.',
      'timestamp': 1319,
      'timestamp_label': '[00:21:59]',
      'timestamp_seconds': 1319,
      'tip': 'Um, another key learning has been that while every vertical SAS gets a foot in '
             'the door with one aha moment, one veg or key feature, in order to really build a '
             'fort, you have to be solving for many different business needs um over time.',
      'title': 'How to Build a Vertical SaaS Company AI Can’t Replace | Sahill Poddar '
               '(Verticals: A Weekly Biz Show On Vertical AI)',
      'url': 'https://www.youtube.com/watch?v=y6eOdHpH5W8&t=1319s',
      'video_id': 'y6eOdHpH5W8'},
     {'author': 'ClankerEngineer',
      'channel': 'ClankerEngineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=4x4nM0uPmg0&t=209s)',
      'relevance': 'Attributed practitioner commentary on multi-tenant RAG architecture, '
                   'semantic caching, webhook idempotency, evals, and sub-5-minute user '
                   'activation.',
      'source_type': 'video_pro_tip',
      'text': 'What we all learn as an AI engineer is everything kind of has a trade-off. So, '
              'to mitigate the additional latency overhead, I sought to implement caching in '
              'other ways of the application.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'What we all learn as an AI engineer is everything kind of has a trade-off. So, '
             'to mitigate the additional latency overhead, I sought to implement caching in '
             'other ways of the application.',
      'title': 'How I cut token costs by 90%: AI cost optimization guide (ClankerEngineer)',
      'url': 'https://www.youtube.com/watch?v=4x4nM0uPmg0&t=209s',
      'video_id': '4x4nM0uPmg0'}],
 8: [{'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=L1jV8eRvnKc&t=169s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'Open router provides basic activity dashboards with usage tracking and cost '
              'monitoring through their web interface. Light LLM offers deeper observability '
              'through integration with external tools. You can pipe logs to Langfuse, MLflow '
              'or your existing monitoring stack.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'Open router provides basic activity dashboards with usage tracking and cost '
             'monitoring through their web interface. Light LLM offers deeper observability '
             'through integration with external tools. You can pipe logs to Langfuse, MLflow '
             'or your existing monitoring stack.',
      'title': 'Openrouter vs Litellm: Which Network Routing Software is BETTER in 2026? '
               '(houdztech)',
      'url': 'https://www.youtube.com/watch?v=L1jV8eRvnKc&t=169s',
      'video_id': 'L1jV8eRvnKc'},
     {'author': 'Bryan Software',
      'channel': 'Bryan Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:00](https://www.youtube.com/watch?v=SDB5hKMHUA8&t=240s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'OpenRouter wins this one outright. Sign up, add credits, swap in one API key, '
              "and you're calling 500 models. Light LLM requires an install, Docker, a "
              'PostgreSQL database, Redis, and a YAML config file just to define your model '
              'list. Community consensus is blunt.',
      'timestamp': 240,
      'timestamp_label': '[00:04:00]',
      'timestamp_seconds': 240,
      'tip': 'OpenRouter wins this one outright. Sign up, add credits, swap in one API key, '
             "and you're calling 500 models. Light LLM requires an install, Docker, a "
             'PostgreSQL database, Redis, and a YAML config file just to define your model '
             'list. Community consensus is blunt.',
      'title': 'OpenRouter vs LiteLLM: Which Should You Self-Host? (Bryan Software)',
      'url': 'https://www.youtube.com/watch?v=SDB5hKMHUA8&t=240s',
      'video_id': 'SDB5hKMHUA8'},
     {'author': 'Hunter Sneed',
      'channel': 'Hunter Sneed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:24](https://www.youtube.com/watch?v=raEBR_2VbXE&t=384s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'Okay, so what I have here is a little web front end that goes over essentially '
              'how we go ahead and classify requests using the router and it all goes through '
              "a tool called Light LLM. I'll go ahead and I'll flip through their GitHub. They "
              'do have a paid offering as well.',
      'timestamp': 384,
      'timestamp_label': '[00:06:24]',
      'timestamp_seconds': 384,
      'tip': 'Okay, so what I have here is a little web front end that goes over essentially '
             'how we go ahead and classify requests using the router and it all goes through a '
             "tool called Light LLM. I'll go ahead and I'll flip through their GitHub. They do "
             'have a paid offering as well.',
      'title': 'AI Model Routing Explained: Cut LLM Costs With LiteLLM (Hunter Sneed)',
      'url': 'https://www.youtube.com/watch?v=raEBR_2VbXE&t=384s',
      'video_id': 'raEBR_2VbXE'},
     {'author': 'The Macroscope',
      'channel': 'The Macroscope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=uTTjkSZnkDI&t=257s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': "And what if we just don't send the request to the LLM at all? By implementing "
              'semantic caching using tools like Redis LangChain, you use vector embeddings to '
              'intercept questions. Say one user asks, "What is machine learning?" And another '
              'asks, "Can you explain ML?"',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': "And what if we just don't send the request to the LLM at all? By implementing "
             'semantic caching using tools like Redis LangChain, you use vector embeddings to '
             'intercept questions. Say one user asks, "What is machine learning?" And another '
             'asks, "Can you explain ML?"',
      'title': 'Stop Wasting AI Tokens: The Ultimate LLM Cost Reduction Guide (Save 90%!) (The '
               'Macroscope)',
      'url': 'https://www.youtube.com/watch?v=uTTjkSZnkDI&t=257s',
      'video_id': 'uTTjkSZnkDI'},
     {'author': 'Stripe Developers',
      'channel': 'Stripe Developers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=o_6aujJ5WbM&t=99s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': "Since the aggregation method is set to sum, what it'll do is add up all of the "
              "usage reports that we submit to the Stripe API. Now let's head over to our IDE "
              "and generate some requests to see what this looks like. I'm going to have "
              'GitHub Copilot help me out a little bit.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': "Since the aggregation method is set to sum, what it'll do is add up all of the "
             "usage reports that we submit to the Stripe API. Now let's head over to our IDE "
             "and generate some requests to see what this looks like. I'm going to have GitHub "
             'Copilot help me out a little bit.',
      'title': 'Monetizing your APIs with usage-based billing (Stripe Developers)',
      'url': 'https://www.youtube.com/watch?v=o_6aujJ5WbM&t=99s',
      'video_id': 'o_6aujJ5WbM'},
     {'author': 'YourTechGuru',
      'channel': 'YourTechGuru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=6EoRbAAAE-8&t=45s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'The advantage of Open Router is its scalability and simplicity. The solution '
              'makes the process of accessing many LLMs from various providers simple enough '
              'to be easily navigated by engineers. Light LLM is an open-source proxy server '
              'and Python SDK that you own end-to-end.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'The advantage of Open Router is its scalability and simplicity. The solution '
             'makes the process of accessing many LLMs from various providers simple enough to '
             'be easily navigated by engineers. Light LLM is an open-source proxy server and '
             'Python SDK that you own end-to-end.',
      'title': 'OpenRouter vs LiteLLM (2026): Which Is The Best LLM Tool For Production? '
               '(YourTechGuru)',
      'url': 'https://www.youtube.com/watch?v=6EoRbAAAE-8&t=45s',
      'video_id': '6EoRbAAAE-8'},
     {'author': 'Trapture Explains',
      'channel': 'Trapture Explains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=VmuCPx8GGTU&t=287s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'Fifth, AI or third-party API calls which grow with your users, say another '
              '1,000. And a small line for everything else, monitoring, a design tool, a '
              'password manager, say 500. That illustrative bill comes to about ₹4,600 a '
              "month. The exact figure isn't the point.",
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': 'Fifth, AI or third-party API calls which grow with your users, say another '
             '1,000. And a small line for everything else, monitoring, a design tool, a '
             'password manager, say 500. That illustrative bill comes to about ₹4,600 a month. '
             "The exact figure isn't the point.",
      'title': 'Free Cloud Credits for Startups: Tech Stack on a Budget (Trapture Explains)',
      'url': 'https://www.youtube.com/watch?v=VmuCPx8GGTU&t=287s',
      'video_id': 'VmuCPx8GGTU'},
     {'author': 'CyberSecurityTV',
      'channel': 'CyberSecurityTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:05](https://www.youtube.com/watch?v=3yDr4mrZXAw&t=365s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'If you want a quick sanity check on your RLS or a live demo of a scanner, ping '
              'the set, contact at the rateify. The tool is available on GitHub. See you in '
              'the next session.',
      'timestamp': 365,
      'timestamp_label': '[00:06:05]',
      'timestamp_seconds': 365,
      'tip': 'If you want a quick sanity check on your RLS or a live demo of a scanner, ping '
             'the set, contact at the rateify. The tool is available on GitHub. See you in the '
             'next session.',
      'title': 'Supabase RLS Security Explained: How to Protect Your Database From Data Leaks '
               '| CyberSecurityTV (CyberSecurityTV)',
      'url': 'https://www.youtube.com/watch?v=3yDr4mrZXAw&t=365s',
      'video_id': '3yDr4mrZXAw'},
     {'author': 'Valen I AI Agent for Work',
      'channel': 'Valen I AI Agent for Work',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=CJf8KAHBVKA&t=29s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'If the most SaaS product are just layers on top of the APIs right now, how '
              "easily could you replace them today? Exactly, and that's a big risk. AI tools, "
              'especially LLMs, can commoditize those API wrappers overnight.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'If the most SaaS product are just layers on top of the APIs right now, how '
             "easily could you replace them today? Exactly, and that's a big risk. AI tools, "
             'especially LLMs, can commoditize those API wrappers overnight.',
      'title': 'Death of SaaS Company in 2026 (said ChatGPT) (Valen I AI Agent for Work)',
      'url': 'https://www.youtube.com/watch?v=CJf8KAHBVKA&t=29s',
      'video_id': 'CJf8KAHBVKA'},
     {'author': 'Hugging Face',
      'channel': 'Hugging Face',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=SkM4k4SKvCM&t=245s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'Now, of course, there are some APIs that abstract this away. So, for example, '
              'responses API. Responses API makes it look like the LLM remembers what it said '
              "before. But what's actually happening behind the scenes is that the LLM is "
              'reprocessing the whole thing.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': 'Now, of course, there are some APIs that abstract this away. So, for example, '
             'responses API. Responses API makes it look like the LLM remembers what it said '
             "before. But what's actually happening behind the scenes is that the LLM is "
             'reprocessing the whole thing.',
      'title': 'Prompt Caching Explained: Stop Overpaying for AI Agents (Hugging Face)',
      'url': 'https://www.youtube.com/watch?v=SkM4k4SKvCM&t=245s',
      'video_id': 'SkM4k4SKvCM'},
     {'author': 'Microsoft Developer',
      'channel': 'Microsoft Developer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=42s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': "I'm the CEO and co-founder of a company called Supabase. We are a Postgres "
              "hosting company. And, if you use us or if you're familiar with us, you'll know "
              'that we also host a bunch of tools that make it really easy to use Postgres.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': "I'm the CEO and co-founder of a company called Supabase. We are a Postgres "
             "hosting company. And, if you use us or if you're familiar with us, you'll know "
             'that we also host a bunch of tools that make it really easy to use Postgres.',
      'title': 'Everything you need to know about Postgres Row Level Security | POSETTE 2024 '
               '(Microsoft Developer)',
      'url': 'https://www.youtube.com/watch?v=vZT1Qx2xUCo&t=42s',
      'video_id': 'vZT1Qx2xUCo'},
     {'author': 'SmartMoneyTutorials',
      'channel': 'SmartMoneyTutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=sfzubTrNiiU&t=53s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': "Next, choose your existing project. If you're starting fresh, you can create a "
              "new project instead. But I'll proceed with an existing one to keep things "
              'moving. Remember, Subbase autogenerates a REST API and provides client '
              'libraries like the JavaScript SDK.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "Next, choose your existing project. If you're starting fresh, you can create a "
             "new project instead. But I'll proceed with an existing one to keep things "
             'moving. Remember, Subbase autogenerates a REST API and provides client libraries '
             'like the JavaScript SDK.',
      'title': 'How To Create RLS Policies In Supabase [Step-By-Step 2026] '
               '(SmartMoneyTutorials)',
      'url': 'https://www.youtube.com/watch?v=sfzubTrNiiU&t=53s',
      'video_id': 'sfzubTrNiiU'},
     {'author': 'Skillfyme',
      'channel': 'Skillfyme',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:07](https://www.youtube.com/watch?v=aYNSsflxcwg&t=1867s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'But with Pinecone and with you can remove we can delete an entry from the '
              'vector database. So, this is the put mechanism. I mean when you want to get '
              'something, so you get the query.',
      'timestamp': 1867,
      'timestamp_label': '[00:31:07]',
      'timestamp_seconds': 1867,
      'tip': 'But with Pinecone and with you can remove we can delete an entry from the vector '
             'database. So, this is the put mechanism. I mean when you want to get something, '
             'so you get the query.',
      'title': 'Reduce LLM API Costs with Caching & Smart Model Routing | LangChain '
               '(Skillfyme)',
      'url': 'https://www.youtube.com/watch?v=aYNSsflxcwg&t=1867s',
      'video_id': 'aYNSsflxcwg'},
     {'author': 'TWiz',
      'channel': 'TWiz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=NwDtEKBC_uo&t=20s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': "Open router's open source community-driven approach versus light LLM's focus on "
              'lightweight on-premise model deployment. Open router is an open source AI '
              'gateway that connects users with multiple large language models through a '
              'unified API.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Open router's open source community-driven approach versus light LLM's focus on "
             'lightweight on-premise model deployment. Open router is an open source AI '
             'gateway that connects users with multiple large language models through a '
             'unified API.',
      'title': 'OpenRouter vs LiteLLM Which AI Gateway Should You Use (TWiz)',
      'url': 'https://www.youtube.com/watch?v=NwDtEKBC_uo&t=20s',
      'video_id': 'NwDtEKBC_uo'},
     {'author': 'Supabase',
      'channel': 'Supabase',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=hu2SQjvCXIw&t=198s)',
      'relevance': 'Attributed practitioner commentary on Postgres/vector stacks, '
                   'PostHog/Sentry telemetry, Manifest V3 Chrome extensions, first-party '
                   'pixels, and GEO citations.',
      'source_type': 'video_pro_tip',
      'text': 'Published and the other has not so we can now see what this would look like for '
              'different roles we have the postgres role which is the default role used by the '
              'Supabase Dashboard so this has admin.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'Published and the other has not so we can now see what this would look like for '
             'different roles we have the postgres role which is the default role used by the '
             'Supabase Dashboard so this has admin.',
      'title': 'Use AI to enable and generate RLS policies for Postgres with Supabase '
               '(Supabase)',
      'url': 'https://www.youtube.com/watch?v=hu2SQjvCXIw&t=198s',
      'video_id': 'hu2SQjvCXIw'}],
 9: [{'author': 'BergTube',
      'channel': 'BergTube',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=-_NbEobmiAY&t=435s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "If you're using cloud agents, make sure they have zero retention policies. You "
              "don't want your client secrets training someone else's model. Ugh, imagine the "
              'legal headache of a data leak. Phew, luckily, local AI models are getting much '
              'better.',
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': "If you're using cloud agents, make sure they have zero retention policies. You "
             "don't want your client secrets training someone else's model. Ugh, imagine the "
             'legal headache of a data leak. Phew, luckily, local AI models are getting much '
             'better.',
      'title': 'The Death of SaaS | Why "Vertical AI" is Taking Over in 2026 (BergTube)',
      'url': 'https://www.youtube.com/watch?v=-_NbEobmiAY&t=435s',
      'video_id': '-_NbEobmiAY'},
     {'author': 'This Works Tutorials',
      'channel': 'This Works Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=00KM5yk235k&t=46s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "Here's what usage-based billing means in practical terms. Instead of a fixed "
              'monthly price, you tie charges to measurable consumption like API calls, data '
              'processed, minutes of video, or number of active credits.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "Here's what usage-based billing means in practical terms. Instead of a fixed "
             'monthly price, you tie charges to measurable consumption like API calls, data '
             'processed, minutes of video, or number of active credits.',
      'title': 'Stripe Usage-Based Billing Guide [2026 Full Guide] (This Works Tutorials)',
      'url': 'https://www.youtube.com/watch?v=00KM5yk235k&t=46s',
      'video_id': '00KM5yk235k'},
     {'author': 'TWiz',
      'channel': 'TWiz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=NwDtEKBC_uo&t=97s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Light LLM works by optimizing model loading and inference, reducing latency and '
              "improving privacy since data stays within the user's environment. Its strengths "
              'include simplicity in setup, fast response times, and enhanced data security.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'Light LLM works by optimizing model loading and inference, reducing latency and '
             "improving privacy since data stays within the user's environment. Its strengths "
             'include simplicity in setup, fast response times, and enhanced data security.',
      'title': 'OpenRouter vs LiteLLM Which AI Gateway Should You Use (TWiz)',
      'url': 'https://www.youtube.com/watch?v=NwDtEKBC_uo&t=97s',
      'video_id': 'NwDtEKBC_uo'},
     {'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=L1jV8eRvnKc&t=205s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Open Router offers organizational management and budget tracking through their '
              "dashboard, but it's less programmatic. Privacy and data residency critical "
              'difference. Open Router offers zero data retention routing.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Open Router offers organizational management and budget tracking through their '
             "dashboard, but it's less programmatic. Privacy and data residency critical "
             'difference. Open Router offers zero data retention routing.',
      'title': 'Openrouter vs Litellm: Which Network Routing Software is BETTER in 2026? '
               '(houdztech)',
      'url': 'https://www.youtube.com/watch?v=L1jV8eRvnKc&t=205s',
      'video_id': 'L1jV8eRvnKc'},
     {'author': 'Captain Vova (Vova Feldman)',
      'channel': 'Captain Vova (Vova Feldman)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=60s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'re selling countries like Australia, India, and all the other geolocations "
              "that basically require dealing with VAT, GST, and sales taxes. So, they don't "
              'really offer global sales tax compliance like other Merchant of Records like '
              'Freemius.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "'re selling countries like Australia, India, and all the other geolocations that "
             "basically require dealing with VAT, GST, and sales taxes. So, they don't really "
             'offer global sales tax compliance like other Merchant of Records like Freemius.',
      'title': 'Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain '
               'Vova (Vova Feldman))',
      'url': 'https://www.youtube.com/watch?v=5zGuxRrg_O0&t=60s',
      'video_id': '5zGuxRrg_O0'},
     {'author': 'Mikey No Code',
      'channel': 'Mikey No Code',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:06](https://www.youtube.com/watch?v=aQZkra1kEcg&t=786s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'t spend on tools, conversion becomes an uphill battle. So, think about "
              'problems like tax filing mistakes, chargebacks, or cleaning up financial data '
              'before an audit. And those are high pain and high pay because mistakes directly '
              'cost money.',
      'timestamp': 786,
      'timestamp_label': '[00:13:06]',
      'timestamp_seconds': 786,
      'tip': "'t spend on tools, conversion becomes an uphill battle. So, think about problems "
             'like tax filing mistakes, chargebacks, or cleaning up financial data before an '
             'audit. And those are high pain and high pay because mistakes directly cost '
             'money.',
      'title': 'Micro Saas Tutorial for Beginners: How to Build a SaaS with AI (2026) (Mikey '
               'No Code)',
      'url': 'https://www.youtube.com/watch?v=aQZkra1kEcg&t=786s',
      'video_id': 'aQZkra1kEcg'},
     {'author': 'Dan Martell',
      'channel': 'Dan Martell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=UEHdYNXiIUU&t=197s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Internet, through a traditional login, a username and password. Prior to that, '
              'there was VPNs required and deep security and all these other things, and it '
              'was just a no go for businesses to trust their proprietary customer data on '
              "somebody else's system.",
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Internet, through a traditional login, a username and password. Prior to that, '
             'there was VPNs required and deep security and all these other things, and it was '
             'just a no go for businesses to trust their proprietary customer data on somebody '
             "else's system.",
      'title': 'What Is SaaS? (Explained in 5 Minutes) (Dan Martell)',
      'url': 'https://www.youtube.com/watch?v=UEHdYNXiIUU&t=197s',
      'video_id': 'UEHdYNXiIUU'},
     {'author': 'updownx',
      'channel': 'updownx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=MEkM0aC1JaI&t=47s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'This allows for granular control over data access, especially in multi-tenant '
              'environments. This code creates a table named accounts with row level security. '
              'It includes three fields: manager, company, and contact make mail.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'This allows for granular control over data access, especially in multi-tenant '
             'environments. This code creates a table named accounts with row level security. '
             'It includes three fields: manager, company, and contact make mail.',
      'title': 'PostgreSQL Row-Level Security Explained with Multi-Tenancy (updownx)',
      'url': 'https://www.youtube.com/watch?v=MEkM0aC1JaI&t=47s',
      'video_id': 'MEkM0aC1JaI'},
     {'author': 'Shortcut Academy',
      'channel': 'Shortcut Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=4ncm-XBGErs&t=30s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Select the table you want to protect with rowle security. Inside the table '
              'view, switch to the security or policies tab. Here you can toggle rowle '
              'security on. RLS is a Postgress feature that lets you filter data on a per row '
              "basis based on who's making the request.",
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Select the table you want to protect with rowle security. Inside the table view, '
             'switch to the security or policies tab. Here you can toggle rowle security on. '
             'RLS is a Postgress feature that lets you filter data on a per row basis based on '
             "who's making the request.",
      'title': 'How to Create Policy (rls) in Supabase [2026 Full Guide] (Shortcut Academy)',
      'url': 'https://www.youtube.com/watch?v=4ncm-XBGErs&t=30s',
      'video_id': '4ncm-XBGErs'},
     {'author': 'Money Tools Academy',
      'channel': 'Money Tools Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=OBXv-uTBD7A&t=107s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Go ahead and turn on the row level security toggle. Once enabled, the table '
              "will have RLS active, which means access can be restricted to your project's "
              'policy rules. This is especially useful when you want users to see or modify '
              "only the data they're allowed to access.",
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Go ahead and turn on the row level security toggle. Once enabled, the table will '
             "have RLS active, which means access can be restricted to your project's policy "
             'rules. This is especially useful when you want users to see or modify only the '
             "data they're allowed to access.",
      'title': 'How to Turn On Row Level Security in Supabase (Full Guide 2026) (Money Tools '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=OBXv-uTBD7A&t=107s',
      'video_id': 'OBXv-uTBD7A'},
     {'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=90s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'VAT or sales tax, and file those tax returns yourself. For a small business '
              'selling in one location, this may not be a big issue. But once you start '
              'getting customers from multiple countries, tax compliance can become '
              'complicated very quickly.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'VAT or sales tax, and file those tax returns yourself. For a small business '
             'selling in one location, this may not be a big issue. But once you start getting '
             'customers from multiple countries, tax compliance can become complicated very '
             'quickly.',
      'title': 'Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? '
               '(Tutorly)',
      'url': 'https://www.youtube.com/watch?v=IfaCBBIoVK0&t=90s',
      'video_id': 'IfaCBBIoVK0'},
     {'author': 'Indie Hacker News',
      'channel': 'Indie Hacker News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=_lbbl0hdJIg&t=108s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Y Combinator plus around led by First Mark, and the license is the part to '
              'remember for later. Quick backstory on that bank. The founders were early at '
              'Konto in France, and their post calling billing a nightmare for engineers hit '
              'the top of Hacker News.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'Y Combinator plus around led by First Mark, and the license is the part to '
             'remember for later. Quick backstory on that bank. The founders were early at '
             'Konto in France, and their post calling billing a nightmare for engineers hit '
             'the top of Hacker News.',
      'title': 'Someone open-sourced Stripe Billing (Mistral uses it) (Indie Hacker News)',
      'url': 'https://www.youtube.com/watch?v=_lbbl0hdJIg&t=108s',
      'video_id': '_lbbl0hdJIg'},
     {'author': 'International PHP Conference',
      'channel': 'International PHP Conference',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=DabJ0hxiXAo&t=182s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'The transaction is immediately aborted before the data ever enters the wrong '
              'tenant database. The database rejects it and returns a loud error stating that '
              'the new row violates the row-level security policy.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': 'The transaction is immediately aborted before the data ever enters the wrong '
             'tenant database. The database rejects it and returns a loud error stating that '
             'the new row violates the row-level security policy.',
      'title': 'PostgreSQL RLS for Safer Multi-Tenant SaaS (International PHP Conference)',
      'url': 'https://www.youtube.com/watch?v=DabJ0hxiXAo&t=182s',
      'video_id': 'DabJ0hxiXAo'},
     {'author': 'Milan Jovanović',
      'channel': 'Milan Jovanović',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=OwCgDPa0DnA&t=166s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'re getting back the notes for our first user. So now we are exposing data from "
              'other users and this is a big security concern. So let me show you how we can '
              'solve this using role level security.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': "'re getting back the notes for our first user. So now we are exposing data from "
             'other users and this is a big security concern. So let me show you how we can '
             'solve this using role level security.',
      'title': 'Building Multi-Tenant APIs Using EF Core and Row-Level Security (Milan '
               'Jovanović)',
      'url': 'https://www.youtube.com/watch?v=OwCgDPa0DnA&t=166s',
      'video_id': 'OwCgDPa0DnA'},
     {'author': 'SmartMoneyTutorials',
      'channel': 'SmartMoneyTutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=Sctm5VrwWTw&t=144s)',
      'relevance': 'Attributed practitioner commentary on zero-retention LLM DPAs, SOC 2 '
                   'readiness, FTC ROSCA cancellation parity, TCPA consent, and IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'If there are no policies, all access is denied by default. Make sure you have '
              'or plan to add the appropriate policies to allow the exact reads and rights '
              'your app needs. This keeps your data secure while preventing unexpected query '
              'failures.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': 'If there are no policies, all access is denied by default. Make sure you have or '
             'plan to add the appropriate policies to allow the exact reads and rights your '
             'app needs. This keeps your data secure while preventing unexpected query '
             'failures.',
      'title': 'How To Enable Row Level Security In Supabase [RLS Guide 2026] '
               '(SmartMoneyTutorials)',
      'url': 'https://www.youtube.com/watch?v=Sctm5VrwWTw&t=144s',
      'video_id': 'Sctm5VrwWTw'}],
 10: [{'author': 'Business Beast Mode',
       'channel': 'Business Beast Mode',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:58](https://www.youtube.com/watch?v=iGqudu6WmHs&t=418s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'And then just the one more thing on booking the onboarding call. Like, what '
               'does that flow actually look like? Is it like a button in the UI? Is it like a '
               'an email that says "Book your onboarding call"?',
       'timestamp': 418,
       'timestamp_label': '[00:06:58]',
       'timestamp_seconds': 418,
       'tip': 'And then just the one more thing on booking the onboarding call. Like, what '
              'does that flow actually look like? Is it like a button in the UI? Is it like a '
              'an email that says "Book your onboarding call"?',
       'title': 'Alex Hormozi: Fix SaaS Churn With This Onboarding Strategy (AMA) (Business '
                'Beast Mode)',
       'url': 'https://www.youtube.com/watch?v=iGqudu6WmHs&t=418s',
       'video_id': 'iGqudu6WmHs'},
      {'author': "Bootstrapper's Paradise",
       'channel': "Bootstrapper's Paradise",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:41](https://www.youtube.com/watch?v=GK9LZkd6aHM&t=341s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Founder-led content, an email list, a YouTube channel, a community, SEO or AEO '
               "authority in your niche. These are assets that compound over time and can't be "
               'replicated quickly by a competitor with a bigger engineering team or deeper '
               'pockets.',
       'timestamp': 341,
       'timestamp_label': '[00:05:41]',
       'timestamp_seconds': 341,
       'tip': 'Founder-led content, an email list, a YouTube channel, a community, SEO or AEO '
              "authority in your niche. These are assets that compound over time and can't be "
              'replicated quickly by a competitor with a bigger engineering team or deeper '
              'pockets.',
       'title': "Vertical AI vs Traditional SaaS | Game Over (Bootstrapper's Paradise)",
       'url': 'https://www.youtube.com/watch?v=GK9LZkd6aHM&t=341s',
       'video_id': 'GK9LZkd6aHM'},
      {'author': 'BergTube',
       'channel': 'BergTube',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:03](https://www.youtube.com/watch?v=-_NbEobmiAY&t=243s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'These are the tasks that follow a clear A to B path. Think about your client '
               'onboarding process or maybe how you handle support tickets. If a task is '
               'repetitive, a vertical AI agent can own it. You should look for agentic '
               'versions of your current tools.',
       'timestamp': 243,
       'timestamp_label': '[00:04:03]',
       'timestamp_seconds': 243,
       'tip': 'These are the tasks that follow a clear A to B path. Think about your client '
              'onboarding process or maybe how you handle support tickets. If a task is '
              'repetitive, a vertical AI agent can own it. You should look for agentic '
              'versions of your current tools.',
       'title': 'The Death of SaaS | Why "Vertical AI" is Taking Over in 2026 (BergTube)',
       'url': 'https://www.youtube.com/watch?v=-_NbEobmiAY&t=243s',
       'video_id': '-_NbEobmiAY'},
      {'author': 'How2Genius',
       'channel': 'How2Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=176s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Its reporting tools are detailed, giving insights into revenue, churn, '
               'customer location, and payment methods. Fastspring also integrates with '
               'popular CRM and marketing tools, helping you automate workflows from purchase '
               'to onboarding.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'Its reporting tools are detailed, giving insights into revenue, churn, customer '
              'location, and payment methods. Fastspring also integrates with popular CRM and '
              'marketing tools, helping you automate workflows from purchase to onboarding.',
       'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
                '(How2Genius)',
       'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=176s',
       'video_id': 'Y5VXhUB7aNM'},
      {'author': 'Greg Isenberg',
       'channel': 'Greg Isenberg',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:43](https://www.youtube.com/watch?v=9T1yWEq5kP0&t=823s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': "That's the opportunity here. If you can create those agent workflows, automate "
               "a lot of that stuff, that's where a lot of the value is going to be. Step 15, "
               "you're going to want to design agents to complete the full tasks. Step 16, "
               'connect agents to real tools.',
       'timestamp': 823,
       'timestamp_label': '[00:13:43]',
       'timestamp_seconds': 823,
       'tip': "That's the opportunity here. If you can create those agent workflows, automate "
              "a lot of that stuff, that's where a lot of the value is going to be. Step 15, "
              "you're going to want to design agents to complete the full tasks. Step 16, "
              'connect agents to real tools.',
       'title': "SaaS is minting millionaires again (here's how) (Greg Isenberg)",
       'url': 'https://www.youtube.com/watch?v=9T1yWEq5kP0&t=823s',
       'video_id': '9T1yWEq5kP0'},
      {'author': 'Alex Rusin',
       'channel': 'Alex Rusin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:55](https://www.youtube.com/watch?v=ctJy5AxgVXM&t=655s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Every isolation claim needs a test and this is exactly the kind of thing an '
               "agent is good at. The logic is simple and there's a lot of it. So here we have "
               'a in the test folder isolation.',
       'timestamp': 655,
       'timestamp_label': '[00:10:55]',
       'timestamp_seconds': 655,
       'tip': 'Every isolation claim needs a test and this is exactly the kind of thing an '
              "agent is good at. The logic is simple and there's a lot of it. So here we have "
              'a in the test folder isolation.',
       'title': "Claude Code + Prisma: Multi-Tenant Postgres API That Can't Leak Data (Alex "
                'Rusin)',
       'url': 'https://www.youtube.com/watch?v=ctJy5AxgVXM&t=655s',
       'video_id': 'ctJy5AxgVXM'},
      {'author': 'CodeLucky',
       'channel': 'CodeLucky',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:25](https://www.youtube.com/watch?v=hyC9WOKzUMc&t=85s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Using our previous example, if your MR is $9,900, your ARR would be $118,800. '
               'ARR helps you see the bigger picture of your annual revenue potential. Churn '
               'rate measures the percentage of customers who cancel their subscription during '
               'a specific period.',
       'timestamp': 85,
       'timestamp_label': '[00:01:25]',
       'timestamp_seconds': 85,
       'tip': 'Using our previous example, if your MR is $9,900, your ARR would be $118,800. '
              'ARR helps you see the bigger picture of your annual revenue potential. Churn '
              'rate measures the percentage of customers who cancel their subscription during '
              'a specific period.',
       'title': 'SaaS Metrics Explained: MRR, ARR, Churn, LTV & CAC | Product Management for '
                'Beginners (CodeLucky)',
       'url': 'https://www.youtube.com/watch?v=hyC9WOKzUMc&t=85s',
       'video_id': 'hyC9WOKzUMc'},
      {'author': 'Costoday',
       'channel': 'Costoday',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:13](https://www.youtube.com/watch?v=aOKH0EoSCCc&t=133s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'The moment a customer has to think about your product, you have already '
               'started losing them. Every feature you ship, every server you provision, every '
               'support ticket you close either deepens that habit or quietly gives the '
               'customer a reason to cancel.',
       'timestamp': 133,
       'timestamp_label': '[00:02:13]',
       'timestamp_seconds': 133,
       'tip': 'The moment a customer has to think about your product, you have already started '
              'losing them. Every feature you ship, every server you provision, every support '
              'ticket you close either deepens that habit or quietly gives the customer a '
              'reason to cancel.',
       'title': 'The Economics of Owning a SaaS Company (Costoday)',
       'url': 'https://www.youtube.com/watch?v=aOKH0EoSCCc&t=133s',
       'video_id': 'aOKH0EoSCCc'},
      {'author': 'Practical Founders - with Greg Head',
       'channel': 'Practical Founders - with Greg Head',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:38:51](https://www.youtube.com/watch?v=Avxi60Ny5SM&t=2331s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': "'t ready to talk to an agent, sorry, an agentic or a machine. They want to "
               'hear somebody with an accent that sounds like theirs >> and and I will lose '
               "credibility if I move too fast >> to full automation. So it's this it's this "
               "balance, >> right? It's [laughter] always Yeah.",
       'timestamp': 2331,
       'timestamp_label': '[00:38:51]',
       'timestamp_seconds': 2331,
       'tip': "'t ready to talk to an agent, sorry, an agentic or a machine. They want to hear "
              'somebody with an accent that sounds like theirs >> and and I will lose '
              "credibility if I move too fast >> to full automation. So it's this it's this "
              "balance, >> right? It's [laughter] always Yeah.",
       'title': 'AI Is Not Killing Vertical SaaS - It’s Practical Leverage (Practical Founders '
                '- with Greg Head)',
       'url': 'https://www.youtube.com/watch?v=Avxi60Ny5SM&t=2331s',
       'video_id': 'Avxi60Ny5SM'},
      {'author': 'GuideFrame',
       'channel': 'GuideFrame',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:38](https://www.youtube.com/watch?v=xssyCPxzFWA&t=98s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'This concludes the steps to update Stripe billing for usage-based pricing. If '
               'the page does not load, refresh the browser or try again in a private or '
               'incognito window. Make sure you are using the correct email address, then '
               'retype it carefully to avoid small typos.',
       'timestamp': 98,
       'timestamp_label': '[00:01:38]',
       'timestamp_seconds': 98,
       'tip': 'This concludes the steps to update Stripe billing for usage-based pricing. If '
              'the page does not load, refresh the browser or try again in a private or '
              'incognito window. Make sure you are using the correct email address, then '
              'retype it carefully to avoid small typos.',
       'title': 'How to update Stripe Billing to add usage-based pricing - Full Guide '
                '(GuideFrame)',
       'url': 'https://www.youtube.com/watch?v=xssyCPxzFWA&t=98s',
       'video_id': 'xssyCPxzFWA'},
      {'author': 'Spec & Ship',
       'channel': 'Spec & Ship',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:52](https://www.youtube.com/watch?v=QaCS2XJLLm4&t=232s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Another silent budget drain is terminal standout pollution. Every time your '
               'agent runs npm install, Docker build, or a full test suite without quiet '
               'flags, thousands of lines of progress bars and deprecation warnings get '
               'appended permanently to your chat context.',
       'timestamp': 232,
       'timestamp_label': '[00:03:52]',
       'timestamp_seconds': 232,
       'tip': 'Another silent budget drain is terminal standout pollution. Every time your '
              'agent runs npm install, Docker build, or a full test suite without quiet flags, '
              'thousands of lines of progress bars and deprecation warnings get appended '
              'permanently to your chat context.',
       'title': 'Why Your Claude Code Limit Vanishes: Cut AI Coding Costs by 70% with Cache & '
                'Model Routing (Spec & Ship)',
       'url': 'https://www.youtube.com/watch?v=QaCS2XJLLm4&t=232s',
       'video_id': 'QaCS2XJLLm4'},
      {'author': 'Learn with Vichu',
       'channel': 'Learn with Vichu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=rECbImLOxqg&t=179s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Let us put real numbers on it. A support agent for an online store. Who it is, '
               'its tone, its goals, 1,500 tokens. Next, a set of rules, refunds, shipping, '
               'what it must never say, 4,000 tokens. Then, the tool definitions, search '
               'orders, refund, track a parcel, 2,500 tokens.',
       'timestamp': 179,
       'timestamp_label': '[00:02:59]',
       'timestamp_seconds': 179,
       'tip': 'Let us put real numbers on it. A support agent for an online store. Who it is, '
              'its tone, its goals, 1,500 tokens. Next, a set of rules, refunds, shipping, '
              'what it must never say, 4,000 tokens. Then, the tool definitions, search '
              'orders, refund, track a parcel, 2,500 tokens.',
       'title': 'How Prompt Caching Saves 90% (GPT-6 Astra) – Cut Your LLM API Bill (Learn '
                'with Vichu)',
       'url': 'https://www.youtube.com/watch?v=rECbImLOxqg&t=179s',
       'video_id': 'rECbImLOxqg'},
      {'author': 'The Startup CFO',
       'channel': 'The Startup CFO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:40:51](https://www.youtube.com/watch?v=Y6tSBvQhyak&t=2451s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'Um its own acquisition sales efficiency how much money you spending sales and '
               'marketing to get one more Euro of ARR Capital efficiency about this by the way '
               'above one is good below one is bad inverages.',
       'timestamp': 2451,
       'timestamp_label': '[00:40:51]',
       'timestamp_seconds': 2451,
       'tip': 'Um its own acquisition sales efficiency how much money you spending sales and '
              'marketing to get one more Euro of ARR Capital efficiency about this by the way '
              'above one is good below one is bad inverages.',
       'title': 'SaaS Metrics: MRR, churn and KPIs every startup should track (The Startup '
                'CFO)',
       'url': 'https://www.youtube.com/watch?v=Y6tSBvQhyak&t=2451s',
       'video_id': 'Y6tSBvQhyak'},
      {'author': 'Money Talk With Leon',
       'channel': 'Money Talk With Leon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:20](https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=560s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': 'I said to myself, "Hmm, what if I can literally find these YouTubers, like '
               'YouTubers with their emails, instead of trying to, you know, search and then '
               'find a YouTuber and figure out, "Oh my god, they don\'t even have their email '
               'on their YouTube.',
       'timestamp': 560,
       'timestamp_label': '[00:09:20]',
       'timestamp_seconds': 560,
       'tip': 'I said to myself, "Hmm, what if I can literally find these YouTubers, like '
              'YouTubers with their emails, instead of trying to, you know, search and then '
              'find a YouTuber and figure out, "Oh my god, they don\'t even have their email '
              'on their YouTube.',
       'title': 'I Sold Digital Products as a Beginner ‘To Prove It’s Not Luck’ Using Claude '
                'AI (Money Talk With Leon)',
       'url': 'https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=560s',
       'video_id': 'B8Z2fA5X0J4'},
      {'author': 'Fomin Unscripted',
       'channel': 'Fomin Unscripted',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:56](https://www.youtube.com/watch?v=29mXPG15AGM&t=56s)',
       'relevance': "Attributed practitioner commentary on '[Competitor] alternative' "
                    'comparison calculators, PLG viral loops, faceless YouTube tutorials, and '
                    'smart dunning.',
       'source_type': 'video_pro_tip',
       'text': "I'd go on YouTube, Google, Reddit and look at what people are already "
               "searching for. Let's say you find a bunch of people looking for a way to "
               'generate a specific document or check some information online or automate '
               'something they have to do every single day.',
       'timestamp': 56,
       'timestamp_label': '[00:00:56]',
       'timestamp_seconds': 56,
       'tip': "I'd go on YouTube, Google, Reddit and look at what people are already searching "
              "for. Let's say you find a bunch of people looking for a way to generate a "
              'specific document or check some information online or automate something they '
              'have to do every single day.',
       'title': 'it’s almost unfair how easy it is to build a SaaS that makes $15,000 a month '
                '(Fomin Unscripted)',
       'url': 'https://www.youtube.com/watch?v=29mXPG15AGM&t=56s',
       'video_id': '29mXPG15AGM'}],
 11: [{'author': 'Valen I AI Agent for Work',
       'channel': 'Valen I AI Agent for Work',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:39](https://www.youtube.com/watch?v=CJf8KAHBVKA&t=159s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "If a transaction is approved but later results in a chargeback, they don't get "
               "paid. So, it aligns their revenue with the customer's core success, turning "
               "them from a feature vendor into a true growth partner. And that's quite "
               'difficult for the SaaS founder to scale.',
       'timestamp': 159,
       'timestamp_label': '[00:02:39]',
       'timestamp_seconds': 159,
       'tip': "If a transaction is approved but later results in a chargeback, they don't get "
              "paid. So, it aligns their revenue with the customer's core success, turning "
              "them from a feature vendor into a true growth partner. And that's quite "
              'difficult for the SaaS founder to scale.',
       'title': 'Death of SaaS Company in 2026 (said ChatGPT) (Valen I AI Agent for Work)',
       'url': 'https://www.youtube.com/watch?v=CJf8KAHBVKA&t=159s',
       'video_id': 'CJf8KAHBVKA'},
      {'author': 'ChartMogul',
       'channel': 'ChartMogul',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:35](https://www.youtube.com/watch?v=zo3QHrXiprs&t=575s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "And therefore, it's good to understand, you know, how much on average you're "
               "paying to acquire a new customer. That's what the cost of acquisition cost is. "
               'Another thing that I want to talk about is something called MR movements.',
       'timestamp': 575,
       'timestamp_label': '[00:09:35]',
       'timestamp_seconds': 575,
       'tip': "And therefore, it's good to understand, you know, how much on average you're "
              "paying to acquire a new customer. That's what the cost of acquisition cost is. "
              'Another thing that I want to talk about is something called MR movements.',
       'title': '11 essential SaaS metrics explained in 11 minutes (ChartMogul)',
       'url': 'https://www.youtube.com/watch?v=zo3QHrXiprs&t=575s',
       'video_id': 'zo3QHrXiprs'},
      {'author': 'CodeLucky',
       'channel': 'CodeLucky',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:22](https://www.youtube.com/watch?v=hyC9WOKzUMc&t=142s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'In our example, with a $99 monthly fee and a 5% turn rate, the LTV would be '
               '$1,980. LTV tells you how much each customer is worth to your business over '
               'time. Customer acquisition cost or CAC is the total amount you spend on '
               'marketing and sales to acquire one new customer.',
       'timestamp': 142,
       'timestamp_label': '[00:02:22]',
       'timestamp_seconds': 142,
       'tip': 'In our example, with a $99 monthly fee and a 5% turn rate, the LTV would be '
              '$1,980. LTV tells you how much each customer is worth to your business over '
              'time. Customer acquisition cost or CAC is the total amount you spend on '
              'marketing and sales to acquire one new customer.',
       'title': 'SaaS Metrics Explained: MRR, ARR, Churn, LTV & CAC | Product Management for '
                'Beginners (CodeLucky)',
       'url': 'https://www.youtube.com/watch?v=hyC9WOKzUMc&t=142s',
       'video_id': 'hyC9WOKzUMc'},
      {'author': 'Sequoia Capital',
       'channel': 'Sequoia Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:44](https://www.youtube.com/watch?v=Uqr2U24uxOs&t=2924s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "Um you know our first engineer was like Rachel's second engineer got Yogi. "
               'Second hire was um uh also in the Sequoia portfolio.',
       'timestamp': 2924,
       'timestamp_label': '[00:48:44]',
       'timestamp_seconds': 2924,
       'tip': "Um you know our first engineer was like Rachel's second engineer got Yogi. "
              'Second hire was um uh also in the Sequoia portfolio.',
       'title': 'What’s the Future of Vertical SaaS in an AGI World? Jamie Cuffe, CEO of Pace '
                '(Sequoia Capital)',
       'url': 'https://www.youtube.com/watch?v=Uqr2U24uxOs&t=2924s',
       'video_id': 'Uqr2U24uxOs'},
      {'author': 'Business Mechanics',
       'channel': 'Business Mechanics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=210s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'SaaS business because it determines whether growth makes you rich or bankrupts '
               'you. Every SaaS company spends money to acquire a customer through paid '
               'advertising, sales salaries, content marketing, conferences, whatever the '
               'channel.',
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': 'SaaS business because it determines whether growth makes you rich or bankrupts '
              'you. Every SaaS company spends money to acquire a customer through paid '
              'advertising, sales salaries, content marketing, conferences, whatever the '
              'channel.',
       'title': 'The Economics of Owning a SaaS Company (Business Mechanics)',
       'url': 'https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=210s',
       'video_id': 'Ju9H1oq7CM8'},
      {'author': 'Indy Pixels | Abdalla Emam',
       'channel': 'Indy Pixels | Abdalla Emam',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:20](https://www.youtube.com/watch?v=NwYdSzPW6yg&t=200s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "If your AI product becomes embedded inside company's operations, it becomes "
               'very hard to replace. For example, AI managing customer support pipelines, AI '
               'handling insurance claims workflows, coordinating caregiver scheduling, '
               'running internal documentation systems.',
       'timestamp': 200,
       'timestamp_label': '[00:03:20]',
       'timestamp_seconds': 200,
       'tip': "If your AI product becomes embedded inside company's operations, it becomes "
              'very hard to replace. For example, AI managing customer support pipelines, AI '
              'handling insurance claims workflows, coordinating caregiver scheduling, running '
              'internal documentation systems.',
       'title': 'The Harsh Truth About AI Wrappers (From a Venture Investor) (Indy Pixels | '
                'Abdalla Emam)',
       'url': 'https://www.youtube.com/watch?v=NwYdSzPW6yg&t=200s',
       'video_id': 'NwYdSzPW6yg'},
      {'author': 'Madhukar Reddy',
       'channel': 'Madhukar Reddy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:55](https://www.youtube.com/watch?v=pX2JNv1VPsQ&t=235s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'So, it increases chances of getting credits. Just fill in the details, so '
               "you're going to get an email confirmation email on your domain's email. So, "
               "here fill in fill in your details. And then, let's say developer or engineer "
               'or you can choose entrepreneur, co-founder.',
       'timestamp': 235,
       'timestamp_label': '[00:03:55]',
       'timestamp_seconds': 235,
       'tip': 'So, it increases chances of getting credits. Just fill in the details, so '
              "you're going to get an email confirmation email on your domain's email. So, "
              "here fill in fill in your details. And then, let's say developer or engineer or "
              'you can choose entrepreneur, co-founder.',
       'title': 'I Built an AI Startup | Got AWS Credits | AWS Activate Founder Tier (Madhukar '
                'Reddy)',
       'url': 'https://www.youtube.com/watch?v=pX2JNv1VPsQ&t=235s',
       'video_id': 'pX2JNv1VPsQ'},
      {'author': 'New Machina',
       'channel': 'New Machina',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=orVropqNnCA&t=140s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'In healthcare, imagine a medical co-pilot that helps doctors interpret patient '
               'symptoms and suggests diagnosis. In customer service, imagine a customer '
               "service chatbot trained specifically for a telecom company's proprietary "
               'support processes.',
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': 'In healthcare, imagine a medical co-pilot that helps doctors interpret patient '
              'symptoms and suggests diagnosis. In customer service, imagine a customer '
              "service chatbot trained specifically for a telecom company's proprietary "
              'support processes.',
       'title': 'What are Vertical Agents ? (New Machina)',
       'url': 'https://www.youtube.com/watch?v=orVropqNnCA&t=140s',
       'video_id': 'orVropqNnCA'},
      {'author': 'TechFuelAI',
       'channel': 'TechFuelAI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:17](https://www.youtube.com/watch?v=9Rig_F79rWo&t=317s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'Shopify, Salesforce, Stripe. Why does this matter for you as a solo founder? '
               'Because it drastically lowers your customer acquisition costs.',
       'timestamp': 317,
       'timestamp_label': '[00:05:17]',
       'timestamp_seconds': 317,
       'tip': 'Shopify, Salesforce, Stripe. Why does this matter for you as a solo founder? '
              'Because it drastically lowers your customer acquisition costs.',
       'title': 'Micro-SaaS in 2026 🚀 | Build a Profitable SaaS Business with Just $50/Month '
                '(TechFuelAI)',
       'url': 'https://www.youtube.com/watch?v=9Rig_F79rWo&t=317s',
       'video_id': '9Rig_F79rWo'},
      {'author': 'One Minute Finance',
       'channel': 'One Minute Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:04](https://www.youtube.com/watch?v=Xpw9vNbYna0&t=424s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'For over a year, you are essentially out of pocket, just waiting for that '
               'customer to pay off their own acquisition debt before they contribute a single '
               "penny to your company's actual growth.",
       'timestamp': 424,
       'timestamp_label': '[00:07:04]',
       'timestamp_seconds': 424,
       'tip': 'For over a year, you are essentially out of pocket, just waiting for that '
              'customer to pay off their own acquisition debt before they contribute a single '
              "penny to your company's actual growth.",
       'title': 'Core Unit Economics: The Financial Formulas Behind SaaS, E-Commerce, and '
                'Marketplaces (One Minute Finance)',
       'url': 'https://www.youtube.com/watch?v=Xpw9vNbYna0&t=424s',
       'video_id': 'Xpw9vNbYna0'},
      {'author': 'houdztech',
       'channel': 'houdztech',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=L1jV8eRvnKc&t=47s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'Same problem, fundamentally different philosophies. No servers to manage, no '
               'infrastructure to maintain. All updates, scaling, and operations handled by '
               'their team. Light LLM requires you to deploy and manage your own '
               'infrastructure.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': 'Same problem, fundamentally different philosophies. No servers to manage, no '
              'infrastructure to maintain. All updates, scaling, and operations handled by '
              'their team. Light LLM requires you to deploy and manage your own '
              'infrastructure.',
       'title': 'Openrouter vs Litellm: Which Network Routing Software is BETTER in 2026? '
                '(houdztech)',
       'url': 'https://www.youtube.com/watch?v=L1jV8eRvnKc&t=47s',
       'video_id': 'L1jV8eRvnKc'},
      {'author': 'Business Beast Mode',
       'channel': 'Business Beast Mode',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:49](https://www.youtube.com/watch?v=iGqudu6WmHs&t=409s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "I wouldn't try and scale past where you're at right now until you fix this. "
               "And then scaling will simply occur cuz even if you don't change your front "
               'end, if you cut your churn by, you know, 2/3, the business will triple.',
       'timestamp': 409,
       'timestamp_label': '[00:06:49]',
       'timestamp_seconds': 409,
       'tip': "I wouldn't try and scale past where you're at right now until you fix this. And "
              "then scaling will simply occur cuz even if you don't change your front end, if "
              'you cut your churn by, you know, 2/3, the business will triple.',
       'title': 'Alex Hormozi: Fix SaaS Churn With This Onboarding Strategy (AMA) (Business '
                'Beast Mode)',
       'url': 'https://www.youtube.com/watch?v=iGqudu6WmHs&t=409s',
       'video_id': 'iGqudu6WmHs'},
      {'author': 'Zero Degree Coder',
       'channel': 'Zero Degree Coder',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:13](https://www.youtube.com/watch?v=K3JxsrRNpBI&t=373s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': "Okay, this is optional, so you can just put the founder's first name, "
               "founder's last name, email address, founder's role. What type of customer you "
               'primarily use? So, I just selected like Android, App Store, you know, those '
               'are all the things.',
       'timestamp': 373,
       'timestamp_label': '[00:06:13]',
       'timestamp_seconds': 373,
       'tip': "Okay, this is optional, so you can just put the founder's first name, founder's "
              "last name, email address, founder's role. What type of customer you primarily "
              'use? So, I just selected like Android, App Store, you know, those are all the '
              'things.',
       'title': 'How to Get $1,000 FREE AWS Credits for Your Startup (Step-by-Step 2026) (Zero '
                'Degree Coder)',
       'url': 'https://www.youtube.com/watch?v=K3JxsrRNpBI&t=373s',
       'video_id': 'K3JxsrRNpBI'},
      {'author': 'updownx',
       'channel': 'updownx',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:19](https://www.youtube.com/watch?v=MEkM0aC1JaI&t=79s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'Permissive policies use the or operator to combine multiple policies, allowing '
               'an operation if any policy permits it. For example, a permissive policy might '
               'allow an admin to view all rows.',
       'timestamp': 79,
       'timestamp_label': '[00:01:19]',
       'timestamp_seconds': 79,
       'tip': 'Permissive policies use the or operator to combine multiple policies, allowing '
              'an operation if any policy permits it. For example, a permissive policy might '
              'allow an admin to view all rows.',
       'title': 'PostgreSQL Row-Level Security Explained with Multi-Tenancy (updownx)',
       'url': 'https://www.youtube.com/watch?v=MEkM0aC1JaI&t=79s',
       'video_id': 'MEkM0aC1JaI'},
      {'author': 'Paul Zuradzki',
       'channel': 'Paul Zuradzki',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:45](https://www.youtube.com/watch?v=Nk7qDiLHyuU&t=225s)',
       'relevance': 'Attributed practitioner commentary on running a 3-person ($375k-$700k '
                    'ARR) SaaS pod, micro-extension rollups, and 3x-6x ARR exit readiness.',
       'source_type': 'video_pro_tip',
       'text': 'So you can imagine a similar idea of like, rather than have people juggling '
               'multiple API keys and multiple base URLs, you want to provide one URL, and '
               'then one key per developer per profile or that kind of thing.',
       'timestamp': 225,
       'timestamp_label': '[00:03:45]',
       'timestamp_seconds': 225,
       'tip': 'So you can imagine a similar idea of like, rather than have people juggling '
              'multiple API keys and multiple base URLs, you want to provide one URL, and then '
              'one key per developer per profile or that kind of thing.',
       'title': 'LiteLLM AI Gateway: Routing, API Keys, Budgets, and Guardrails for Local and '
                'Cloud Models (Paul Zuradzki)',
       'url': 'https://www.youtube.com/watch?v=Nk7qDiLHyuU&t=225s',
       'video_id': 'Nk7qDiLHyuU'}],
 12: [{'author': 'Starter Story',
       'channel': 'Starter Story',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:32](https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=392s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "Product Hunt, Reddit, SEO, and then X, Twitter. To this day, we haven't used "
               'any paid channels at all. We launched our MVP on Product Hunt in week one, '
               'then made our first $50 MRR from that launch.',
       'timestamp': 392,
       'timestamp_label': '[00:06:32]',
       'timestamp_seconds': 392,
       'tip': "Product Hunt, Reddit, SEO, and then X, Twitter. To this day, we haven't used "
              'any paid channels at all. We launched our MVP on Product Hunt in week one, then '
              'made our first $50 MRR from that launch.',
       'title': 'I Built A Micro-Version Of A $1B SaaS. Now I Make $50K/Month (Starter Story)',
       'url': 'https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=392s',
       'video_id': 'Nnpz1wsTjBI'},
      {'author': 'Fomin Unscripted',
       'channel': 'Fomin Unscripted',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:34](https://www.youtube.com/watch?v=29mXPG15AGM&t=274s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "And you really don't need any of that just to get started. You can start with "
               'one small product, get your first customer, then your first 10, then your '
               'first 100, and just keep improving it as you go. Maybe you eventually get to '
               '500 people paying you 30 bucks a month.',
       'timestamp': 274,
       'timestamp_label': '[00:04:34]',
       'timestamp_seconds': 274,
       'tip': "And you really don't need any of that just to get started. You can start with "
              'one small product, get your first customer, then your first 10, then your first '
              '100, and just keep improving it as you go. Maybe you eventually get to 500 '
              'people paying you 30 bucks a month.',
       'title': 'it’s almost unfair how easy it is to build a SaaS that makes $15,000 a month '
                '(Fomin Unscripted)',
       'url': 'https://www.youtube.com/watch?v=29mXPG15AGM&t=274s',
       'video_id': '29mXPG15AGM'},
      {'author': 'One Minute Finance',
       'channel': 'One Minute Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:23](https://www.youtube.com/watch?v=Xpw9vNbYna0&t=623s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': 'I challenge you to open up your CRM today, pull the real data, and include '
               'every last software subscription and commission check. Second, map out your '
               'customer retention curves by cohort over a 12-month period.',
       'timestamp': 623,
       'timestamp_label': '[00:10:23]',
       'timestamp_seconds': 623,
       'tip': 'I challenge you to open up your CRM today, pull the real data, and include '
              'every last software subscription and commission check. Second, map out your '
              'customer retention curves by cohort over a 12-month period.',
       'title': 'Core Unit Economics: The Financial Formulas Behind SaaS, E-Commerce, and '
                'Marketplaces (One Minute Finance)',
       'url': 'https://www.youtube.com/watch?v=Xpw9vNbYna0&t=623s',
       'video_id': 'Xpw9vNbYna0'},
      {'author': 'TechFuelAI',
       'channel': 'TechFuelAI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=9Rig_F79rWo&t=340s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': '300,000, and take what, 6 to 12 months? Today, because of AI coding tools and '
               'these insanely powerful no-code platforms, your cost to hit MVP is somewhere '
               'between $200 and $500, and you can launch it in 2 to 14 days.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': '300,000, and take what, 6 to 12 months? Today, because of AI coding tools and '
              'these insanely powerful no-code platforms, your cost to hit MVP is somewhere '
              'between $200 and $500, and you can launch it in 2 to 14 days.',
       'title': 'Micro-SaaS in 2026 🚀 | Build a Profitable SaaS Business with Just $50/Month '
                '(TechFuelAI)',
       'url': 'https://www.youtube.com/watch?v=9Rig_F79rWo&t=340s',
       'video_id': '9Rig_F79rWo'},
      {'author': 'Starter Story',
       'channel': 'Starter Story',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=_KaFS4Dxs5k&t=34s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "'ll go over where to start looking for ideas, how to identify if one is worth "
               'working on, and how to get your first customer without actually building '
               "anything. I think you're going to like this one. I'm Pat Walls and this is "
               'Starter Story.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': "'ll go over where to start looking for ideas, how to identify if one is worth "
              'working on, and how to get your first customer without actually building '
              "anything. I think you're going to like this one. I'm Pat Walls and this is "
              'Starter Story.',
       'title': 'I Copied a $100M SaaS, Undercut Their Prices, and Hit $10K/Month (Starter '
                'Story)',
       'url': 'https://www.youtube.com/watch?v=_KaFS4Dxs5k&t=34s',
       'video_id': '_KaFS4Dxs5k'},
      {'author': 'This Works Tutorials',
       'channel': 'This Works Tutorials',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=00KM5yk235k&t=78s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "Stripe's usage-based billing along with options like start now and contact "
               'sales. The key idea is speed and flexibility. Stripe is positioning this as a '
               'way to launch quickly, scale confidently, and keep pricing adaptable as your '
               'product and customer needs change.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': "Stripe's usage-based billing along with options like start now and contact "
              'sales. The key idea is speed and flexibility. Stripe is positioning this as a '
              'way to launch quickly, scale confidently, and keep pricing adaptable as your '
              'product and customer needs change.',
       'title': 'Stripe Usage-Based Billing Guide [2026 Full Guide] (This Works Tutorials)',
       'url': 'https://www.youtube.com/watch?v=00KM5yk235k&t=78s',
       'video_id': '00KM5yk235k'},
      {'author': 'InnMind',
       'channel': 'InnMind',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:32](https://www.youtube.com/watch?v=a3Sjk-St_ng&t=332s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "Linear, Notion & Miro give the startup offer only to accounts that don't pay "
               'yet. E2B: first-time users only. Apply BEFORE you enter your card. Once you '
               'pay, you are a customer, & customers pay full price. Mistake 3: you start too '
               'early.',
       'timestamp': 332,
       'timestamp_label': '[00:05:32]',
       'timestamp_seconds': 332,
       'tip': "Linear, Notion & Miro give the startup offer only to accounts that don't pay "
              'yet. E2B: first-time users only. Apply BEFORE you enter your card. Once you '
              'pay, you are a customer, & customers pay full price. Mistake 3: you start too '
              'early.',
       'title': 'Startup Credits 2026: Up to $48,000 With No Investor (AWS, Claude, Azure, '
                'Google) (InnMind)',
       'url': 'https://www.youtube.com/watch?v=a3Sjk-St_ng&t=332s',
       'video_id': 'a3Sjk-St_ng'},
      {'author': 'Milan Jovanović',
       'channel': 'Milan Jovanović',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:12](https://www.youtube.com/watch?v=OwCgDPa0DnA&t=432s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "And let's go ahead and execute this. And notice that in the query plan there "
               'is an additional filter that checks if the user ID is equal to our current '
               'setting with the name of app. So you can see how all of this works from SQL.',
       'timestamp': 432,
       'timestamp_label': '[00:07:12]',
       'timestamp_seconds': 432,
       'tip': "And let's go ahead and execute this. And notice that in the query plan there is "
              'an additional filter that checks if the user ID is equal to our current setting '
              'with the name of app. So you can see how all of this works from SQL.',
       'title': 'Building Multi-Tenant APIs Using EF Core and Row-Level Security (Milan '
                'Jovanović)',
       'url': 'https://www.youtube.com/watch?v=OwCgDPa0DnA&t=432s',
       'video_id': 'OwCgDPa0DnA'},
      {'author': 'Supabase',
       'channel': 'Supabase',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:35](https://www.youtube.com/watch?v=PdEutzhsrws&t=395s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': 'So this means we need to use an upsert action, which first attempts to insert '
               'a new user, but if one already exists, it will instead update its supabase_id '
               'column to link it to that new user in the auth schema.',
       'timestamp': 395,
       'timestamp_label': '[00:06:35]',
       'timestamp_seconds': 395,
       'tip': 'So this means we need to use an upsert action, which first attempts to insert a '
              'new user, but if one already exists, it will instead update its supabase_id '
              'column to link it to that new user in the auth schema.',
       'title': 'Advanced Row Level Security (RLS) Policies // Authorization Deep Dive '
                '(Supabase)',
       'url': 'https://www.youtube.com/watch?v=PdEutzhsrws&t=395s',
       'video_id': 'PdEutzhsrws'},
      {'author': 'Starter Story',
       'channel': 'Starter Story',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=LRX8TWC2hTM&t=187s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': 'So, how did you find your first customer for this boring SaaS? And how did you '
               'grow it from there? Once we had, at the time, what we thought was a working '
               'MVP, we knew it was time to get it out there and see if anyone actually was '
               'interested in using the product.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'So, how did you find your first customer for this boring SaaS? And how did you '
              'grow it from there? Once we had, at the time, what we thought was a working '
              'MVP, we knew it was time to get it out there and see if anyone actually was '
              'interested in using the product.',
       'title': 'I Make $60K/Month From the Most Boring SaaS on the Internet (Starter Story)',
       'url': 'https://www.youtube.com/watch?v=LRX8TWC2hTM&t=187s',
       'video_id': 'LRX8TWC2hTM'},
      {'author': 'Business Mechanics',
       'channel': 'Business Mechanics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:54](https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=474s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': 'A customer who never fully sets up the product, never connects it to their '
               'existing workflow, never gets a colleague to also start using it, is a '
               "customer who's mentally already halfway out the door the day their trial "
               'converts to paid.',
       'timestamp': 474,
       'timestamp_label': '[00:07:54]',
       'timestamp_seconds': 474,
       'tip': 'A customer who never fully sets up the product, never connects it to their '
              'existing workflow, never gets a colleague to also start using it, is a customer '
              "who's mentally already halfway out the door the day their trial converts to "
              'paid.',
       'title': 'The Economics of Owning a SaaS Company (Business Mechanics)',
       'url': 'https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=474s',
       'video_id': 'Ju9H1oq7CM8'},
      {'author': 'Medical Chat',
       'channel': 'Medical Chat',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=yo4GOxbqovo&t=50s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': 'Chat Data quietly creates the product and price on your Stripe account. No '
               "dashboard wrangling required. Now, let's walk through what you can actually "
               "build. First up, a paid expert bot. Say you've got a research co-pilot that's "
               'genuinely valuable.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'Chat Data quietly creates the product and price on your Stripe account. No '
              "dashboard wrangling required. Now, let's walk through what you can actually "
              "build. First up, a paid expert bot. Say you've got a research co-pilot that's "
              'genuinely valuable.',
       'title': 'Make Your AI Chatbot Pay For Itself — Stripe Usage Metering, Paywalls & Caps '
                '(Chat Data) (Medical Chat)',
       'url': 'https://www.youtube.com/watch?v=yo4GOxbqovo&t=50s',
       'video_id': 'yo4GOxbqovo'},
      {'author': 'Founder Brief',
       'channel': 'Founder Brief',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=DmdDoIC4IgM&t=187s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "Because Google isn't just handing these credits out to anyone with a business "
               "plan on a napkin, you've got to tick these four essential boxes. First, you "
               'need to be building proprietary software or a tech-enabled business. Second, '
               'company age limits matter immensely here.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': "Because Google isn't just handing these credits out to anyone with a business "
              "plan on a napkin, you've got to tick these four essential boxes. First, you "
              'need to be building proprietary software or a tech-enabled business. Second, '
              'company age limits matter immensely here.',
       'title': 'Up to $350K Google Cloud Credits? How to ApplyGoogleCloud #StartupCredits '
                '#FoundersSecondary (Founder Brief)',
       'url': 'https://www.youtube.com/watch?v=DmdDoIC4IgM&t=187s',
       'video_id': 'DmdDoIC4IgM'},
      {'author': 'Greg Isenberg',
       'channel': 'Greg Isenberg',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:09](https://www.youtube.com/watch?v=9T1yWEq5kP0&t=129s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "'s about building cash flowing startup you know $100,000 a month a million "
               "dollar a month type thing. So that's what you're going to want to do first. Uh "
               "second, you're going to want to map uh this subnich's workflow end to end.",
       'timestamp': 129,
       'timestamp_label': '[00:02:09]',
       'timestamp_seconds': 129,
       'tip': "'s about building cash flowing startup you know $100,000 a month a million "
              "dollar a month type thing. So that's what you're going to want to do first. Uh "
              "second, you're going to want to map uh this subnich's workflow end to end.",
       'title': "SaaS is minting millionaires again (here's how) (Greg Isenberg)",
       'url': 'https://www.youtube.com/watch?v=9T1yWEq5kP0&t=129s',
       'video_id': '9T1yWEq5kP0'},
      {'author': 'Stripe Developers',
       'channel': 'Stripe Developers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:24](https://www.youtube.com/watch?v=Hr9MP_3-QPg&t=624s)',
       'relevance': 'Attributed practitioner commentary on a 30-day problem-interview, '
                    'clickable prototype, metered MVP build, and first-10-paying-customers '
                    'sprint.',
       'source_type': 'video_pro_tip',
       'text': "Okay, so what are you going to show us here? So what I'm going to show us is "
               'like basically a couple of steps. First, I will go ahead and create a meter. '
               "That's basically where you define what I'm charging for. Uh how do I want to "
               'aggregate usage? Then I will set up a price.',
       'timestamp': 624,
       'timestamp_label': '[00:10:24]',
       'timestamp_seconds': 624,
       'tip': "Okay, so what are you going to show us here? So what I'm going to show us is "
              'like basically a couple of steps. First, I will go ahead and create a meter. '
              "That's basically where you define what I'm charging for. Uh how do I want to "
              'aggregate usage? Then I will set up a price.',
       'title': 'Enabling pay-as-you-go with usage based billing (Stripe Developers)',
       'url': 'https://www.youtube.com/watch?v=Hr9MP_3-QPg&t=624s',
       'video_id': 'Hr9MP_3-QPg'}]}
