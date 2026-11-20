"""Curated 180-citation digital-product baseline (15 per chapter across Q1-Q12) mined from the dedicated Volume 003 YouTube transcript corpus."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'ascension',
     'asset',
     'bundle',
     'cohort',
     'community',
     'course',
     'curriculum',
     'digital',
     'download',
     'ebook',
     'evergreen',
     'format',
     'ladder',
     'membership',
     'model',
     'notion',
     'offer',
     'playbook',
     'product',
     'products',
     'software',
     'template',
     'templates'},
 2: {'audience',
     'b2b',
     'b2c',
     'buyer',
     'checkout',
     'customer',
     'customers',
     'lemon',
     'marketplace',
     'merchant',
     'mor',
     'paddle',
     'pay',
     'payment',
     'payout',
     'platform',
     'processor',
     'prosumer',
     'squeezy',
     'stripe',
     'tax',
     'vat'},
 3: {'anchor',
     'aov',
     'bump',
     'cac',
     'chargeback',
     'cogs',
     'contribution',
     'conversion',
     'economics',
     'ltv',
     'margin',
     'order',
     'price',
     'pricing',
     'profit',
     'refund',
     'revenue',
     'roas',
     'slo',
     'tier',
     'tiers',
     'unit',
     'upsell'},
 4: {'Banking',
     'bank',
     'budget',
     'capital',
     'cloud',
     'contractor',
     'cost',
     'costs',
     'credits',
     'domain',
     'edge',
     'entity',
     'fintech',
     'hosting',
     'ip',
     'lean',
     'llc',
     'opex',
     'reserve',
     'serverless',
     'setup',
     'stack',
     'startup',
     'vercel'},
 5: {'burn',
     'churn',
     'clawback',
     'commoditization',
     'copycat',
     'dispute',
     'fatigue',
     'fraud',
     'friendly',
     'mistake',
     'nexus',
     'piracy',
     'platform',
     'policy',
     'refunds',
     'risk',
     'saturation',
     'stripe',
     'trap',
     'traps',
     'wayfair'},
 6: {'ad',
     'ads',
     'demand',
     'discover',
     'intent',
     'keyword',
     'keywords',
     'library',
     'market',
     'niche',
     'pain',
     'presell',
     'problem',
     'proof',
     'reddit',
     'research',
     'search',
     'signal',
     'signals',
     'spend',
     'validate',
     'validation',
     'waitlist'},
 7: {'architecture',
     'build',
     'checkout',
     'deliver',
     'delivery',
     'design',
     'drip',
     'entitlement',
     'fulfillment',
     'funnel',
     'landing',
     'launch',
     'license',
     'onboarding',
     'packaging',
     'page',
     'post',
     'production',
     'purchase',
     'qa',
     'vsl',
     'webhook'},
 8: {'analytics',
     'api',
     'attribution',
     'beehiiv',
     'cloudflare',
     'cname',
     'crm',
     'database',
     'email',
     'extension',
     'geo',
     'gumroad',
     'lemon',
     'paddle',
     'pixel',
     'pixels',
     'posthog',
     'schema',
     'seo',
     'sparkloop',
     'stack',
     'stripe',
     'tool',
     'tools'},
 9: {'affiliate',
     'billing',
     'cancel',
     'cancellation',
     'click',
     'compliance',
     'consent',
     'copyright',
     'disclosure',
     'dmca',
     'endorsement',
     'ftc',
     'gdpr',
     'ip',
     'license',
     'merchant',
     'mor',
     'privacy',
     'refund',
     'rosca',
     'sales',
     'tax',
     'terms',
     'vat'},
 10: {'ab',
      'agent',
      'ai',
      'automate',
      'automation',
      'bot',
      'chat',
      'chatbot',
      'clip',
      'co',
      'dm',
      'drip',
      'email',
      'faceless',
      'flow',
      'llm',
      'manychat',
      'programmatic',
      'quiz',
      'referral',
      'sequence',
      'split',
      'support',
      'test',
      'testing',
      'trigger',
      'viral',
      'youtube'},
 11: {'agency',
      'catalog',
      'contractor',
      'contractors',
      'creator',
      'delegate',
      'designer',
      'editor',
      'empire',
      'hire',
      'hiring',
      'kpi',
      'kpis',
      'manager',
      'media',
      'multi',
      'operations',
      'operator',
      'portfolio',
      'scale',
      'scaling',
      'sku',
      'sop',
      'sops',
      'team',
      'va'},
 12: {'action',
      'audit',
      'calendar',
      'checklist',
      'cohort',
      'day',
      'days',
      'execute',
      'execution',
      'first',
      'goal',
      'iterate',
      'kpi',
      'launch',
      'milestone',
      'month',
      'ninety',
      'plan',
      'publish',
      'roadmap',
      'ship',
      'sprint',
      'start',
      'steps',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'GuideHatch Tutorials',
      'channel': 'GuideHatch Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=DNdWpxzzTQM&t=75s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "After you've named your project, ensure that it is categorized as a digital "
              'product. Gumroad specializes in digital products, making this the perfect '
              'setting for your Notion template.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': "After you've named your project, ensure that it is categorized as a digital "
             'product. Gumroad specializes in digital products, making this the perfect '
             'setting for your Notion template.',
      'title': 'How to sell Notion templates on Gumroad (Creative Earnings) (GuideHatch '
               'Tutorials)',
      'url': 'https://www.youtube.com/watch?v=DNdWpxzzTQM&t=75s',
      'video_id': 'DNdWpxzzTQM'},
     {'author': 'Tutorials At Desk',
      'channel': 'Tutorials At Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=VEFf-FR0dxw&t=75s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'On the left sidebar of your Gumroad dashboard, click products. Gumroad will ask '
              'what type of product you want to create. In the name field, type the name of '
              'your Notion template. After that, under the product type options, choose '
              'digital product.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'On the left sidebar of your Gumroad dashboard, click products. Gumroad will ask '
             'what type of product you want to create. In the name field, type the name of '
             'your Notion template. After that, under the product type options, choose digital '
             'product.',
      'title': 'How to Sell Notion Templates on Gumroad (2026 Revenue Snapshot) (Tutorials At '
               'Desk)',
      'url': 'https://www.youtube.com/watch?v=VEFf-FR0dxw&t=75s',
      'video_id': 'VEFf-FR0dxw'},
     {'author': 'Extreme Guides',
      'channel': 'Extreme Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=2zWJQPegtuk&t=110s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'A clear and appealing name can help attract more buyers. Select the option for '
              'a digital product after entering the product name. This ensures that Gumroad '
              'recognizes your template as a digital download, which is essential for the '
              'purchasing process.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'A clear and appealing name can help attract more buyers. Select the option for a '
             'digital product after entering the product name. This ensures that Gumroad '
             'recognizes your template as a digital download, which is essential for the '
             'purchasing process.',
      'title': 'How to sell Notion templates on Gumroad[FULL GUIDE] (Extreme Guides)',
      'url': 'https://www.youtube.com/watch?v=2zWJQPegtuk&t=110s',
      'video_id': '2zWJQPegtuk'},
     {'author': 'Stellar Media',
      'channel': 'Stellar Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=YiY_qBBHvvc&t=61s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "'t have then it will be empty like mine. Now in order to sell it click on the "
              'option new product and here you have to enter the name of your product just '
              'like I will do write notion template from this you have to select this option '
              'digital product.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "'t have then it will be empty like mine. Now in order to sell it click on the "
             'option new product and here you have to enter the name of your product just like '
             'I will do write notion template from this you have to select this option digital '
             'product.',
      'title': 'How To Sell Notion Templates On Gumroad 2025 (Step by Step) (Stellar Media)',
      'url': 'https://www.youtube.com/watch?v=YiY_qBBHvvc&t=61s',
      'video_id': 'YiY_qBBHvvc'},
     {'author': 'BrightGuide',
      'channel': 'BrightGuide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=oMxSmqY3mzM&t=22s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "This is where all of your existing items live, and it's also where you can "
              "create a new one. Once you're in the products area, click on new product. This "
              "opens the product creation page where you'll begin entering the basic details "
              'for your Notion template.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "This is where all of your existing items live, and it's also where you can "
             "create a new one. Once you're in the products area, click on new product. This "
             "opens the product creation page where you'll begin entering the basic details "
             'for your Notion template.',
      'title': 'How to Sell Notion Templates on Gumroad (Step By Step 2026) (BrightGuide)',
      'url': 'https://www.youtube.com/watch?v=oMxSmqY3mzM&t=22s',
      'video_id': 'oMxSmqY3mzM'},
     {'author': "Extreme How To's",
      'channel': "Extreme How To's",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=SK_-uXSKE88&t=26s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'Input the title as ultimate template. This title should clearly reflect what '
              'your template offers. After naming your product, set the price between $5 to '
              '$25, keeping in mind that this range is often considered the sweet spot for '
              'Notion templates.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'Input the title as ultimate template. This title should clearly reflect what '
             'your template offers. After naming your product, set the price between $5 to '
             '$25, keeping in mind that this range is often considered the sweet spot for '
             'Notion templates.',
      'title': "How to sell Notion templates on Gumroad[2026 Full Guide] (Extreme How To's)",
      'url': 'https://www.youtube.com/watch?v=SK_-uXSKE88&t=26s',
      'video_id': 'SK_-uXSKE88'},
     {'author': 'Typedream',
      'channel': 'Typedream',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=HXQD-vJDPyU&t=113s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'This saves as a Photoshop (. Smart Objects, with screenshots of your Notion '
              'template. And, this is the final product! I’m going to crop this into a square '
              'because Gumroad thumbnails only accept the square format.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'This saves as a Photoshop (. Smart Objects, with screenshots of your Notion '
             'template. And, this is the final product! I’m going to crop this into a square '
             'because Gumroad thumbnails only accept the square format.',
      'title': 'How to make and sell aesthetic Notion templates with Typedream and Gumroad '
               '(Typedream)',
      'url': 'https://www.youtube.com/watch?v=HXQD-vJDPyU&t=113s',
      'video_id': 'HXQD-vJDPyU'},
     {'author': 'Aeris Vale Tutorials',
      'channel': 'Aeris Vale Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=51s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'It should be catchy and accurately reflect the essence of what your template '
              "offers. After naming your template, you'll need to specify that it's a digital "
              "product which suits our notion template well. Now, it's time to set the price.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'It should be catchy and accurately reflect the essence of what your template '
             "offers. After naming your template, you'll need to specify that it's a digital "
             "product which suits our notion template well. Now, it's time to set the price.",
      'title': 'How To Sell A Notion Template On Gumroad - Step by Step Guide | THELOSTOFFER '
               '#notion #gumroad (Aeris Vale Tutorials)',
      'url': 'https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=51s',
      'video_id': 'ciKrPZ_nIpQ'},
     {'author': 'Nathan Nazareth',
      'channel': 'Nathan Nazareth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:56](https://www.youtube.com/watch?v=6cm2o8zzuNw&t=536s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "It's what our clients inside of our digital products use. And it genuinely is "
              "just a life-changing software if you're running a business. And in just a "
              "minute, I'll show you how to use it live to build your digital product.",
      'timestamp': 536,
      'timestamp_label': '[00:08:56]',
      'timestamp_seconds': 536,
      'tip': "It's what our clients inside of our digital products use. And it genuinely is "
             "just a life-changing software if you're running a business. And in just a "
             "minute, I'll show you how to use it live to build your digital product.",
      'title': 'How to build & sell AI Digital Products (2026 full guide) (Nathan Nazareth)',
      'url': 'https://www.youtube.com/watch?v=6cm2o8zzuNw&t=536s',
      'video_id': '6cm2o8zzuNw'},
     {'author': 'Ceostacks',
      'channel': 'Ceostacks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:49](https://www.youtube.com/watch?v=UE0ReGj5sjU&t=649s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "Putting y'all on all type of game you know what I'm saying the Digital World "
              'Academy course is linked below and the full access to the bundle is link below '
              'as well.',
      'timestamp': 649,
      'timestamp_label': '[00:10:49]',
      'timestamp_seconds': 649,
      'tip': "Putting y'all on all type of game you know what I'm saying the Digital World "
             'Academy course is linked below and the full access to the bundle is link below '
             'as well.',
      'title': 'How to Start Selling DONE FOR YOU Digital Products as a beginner (The easiest '
               'way)! (Ceostacks)',
      'url': 'https://www.youtube.com/watch?v=UE0ReGj5sjU&t=649s',
      'video_id': 'UE0ReGj5sjU'},
     {'author': 'Side Hustle Mastery',
      'channel': 'Side Hustle Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:40](https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=400s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "'ll then go ahead and add a name to the digital product that you're trying to "
              "create in the first place. We'll simply just call this our photography business "
              'notion template.',
      'timestamp': 400,
      'timestamp_label': '[00:06:40]',
      'timestamp_seconds': 400,
      'tip': "'ll then go ahead and add a name to the digital product that you're trying to "
             "create in the first place. We'll simply just call this our photography business "
             'notion template.',
      'title': 'How to Make Money Selling Notion Templates [Gumroad Step-by-Step] (Side Hustle '
               'Mastery)',
      'url': 'https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=400s',
      'video_id': '2j9bt8ET3Ec'},
     {'author': 'Funnel Building Secrets',
      'channel': 'Funnel Building Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=BZ4rml1tc1U&t=65s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': 'Name your upsell page and click create funnel step. Step five, select an upsell '
              'template. Clickfunnels has several upsell templates. Choose one that fits your '
              'style and click edit page. Customize your upsell offer. Include product images '
              'and descriptions.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'Name your upsell page and click create funnel step. Step five, select an upsell '
             'template. Clickfunnels has several upsell templates. Choose one that fits your '
             'style and click edit page. Customize your upsell offer. Include product images '
             'and descriptions.',
      'title': 'How to Set Up an Order Bump and Upsell (Funnel Building Secrets)',
      'url': 'https://www.youtube.com/watch?v=BZ4rml1tc1U&t=65s',
      'video_id': 'BZ4rml1tc1U'},
     {'author': 'How To Tutor',
      'channel': 'How To Tutor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=Sxl5Fxp0qVQ&t=57s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "'ll be able to get redirected into your publish template. So in here copy the "
              'link of your template and then head over to Gumroad and then in here click on '
              'the showtime button and then go ahead and name your product and then set the '
              'product type to digital product.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "'ll be able to get redirected into your publish template. So in here copy the "
             'link of your template and then head over to Gumroad and then in here click on '
             'the showtime button and then go ahead and name your product and then set the '
             'product type to digital product.',
      'title': 'How to Upload Notion Template on Gumroad 2025 (QUICK GUIDE) (How To Tutor)',
      'url': 'https://www.youtube.com/watch?v=Sxl5Fxp0qVQ&t=57s',
      'video_id': 'Sxl5Fxp0qVQ'},
     {'author': 'Skool News',
      'channel': 'Skool News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:01](https://www.youtube.com/watch?v=Oeug9IgSFXc&t=421s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "I don't know notion or Calendarly or Zoom or Loom all the premium software "
              "products right when you sign up to them they're free and they're very useful as "
              "free products but then once you start to use them you realize that there's some "
              'paid upgrades.',
      'timestamp': 421,
      'timestamp_label': '[00:07:01]',
      'timestamp_seconds': 421,
      'tip': "I don't know notion or Calendarly or Zoom or Loom all the premium software "
             "products right when you sign up to them they're free and they're very useful as "
             "free products but then once you start to use them you realize that there's some "
             'paid upgrades.',
      'title': 'Membership TIERS Are Here | Skool News #33 (Skool News)',
      'url': 'https://www.youtube.com/watch?v=Oeug9IgSFXc&t=421s',
      'video_id': 'Oeug9IgSFXc'},
     {'author': 'Alek',
      'channel': 'Alek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:35](https://www.youtube.com/watch?v=T-gfoXzz8k8&t=695s)',
      'relevance': 'Attributed practitioner commentary on digital product formats, value '
                   'ladders, templates, courses, and paid communities; validate market fit '
                   'independently.',
      'source_type': 'video_pro_tip',
      'text': "'re selling is a digital download t-shirt or sweatshirt design. So, they've "
              'built out a design that could be printed on a t-shirt or sweatshirt, and '
              "instead of like drop shipping the actual product itself, they're just selling "
              'the PNG downloads.',
      'timestamp': 695,
      'timestamp_label': '[00:11:35]',
      'timestamp_seconds': 695,
      'tip': "'re selling is a digital download t-shirt or sweatshirt design. So, they've "
             'built out a design that could be printed on a t-shirt or sweatshirt, and instead '
             "of like drop shipping the actual product itself, they're just selling the PNG "
             'downloads.',
      'title': 'Build & Sell Digital Products with A.I. (Full Course) (Alek)',
      'url': 'https://www.youtube.com/watch?v=T-gfoXzz8k8&t=695s',
      'video_id': 'T-gfoXzz8k8'}],
 2: [{'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=20s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
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
     {'author': 'TechWealth Hub',
      'channel': 'TechWealth Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=96s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
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
     {'author': 'Captain Vova (Vova Feldman)',
      'channel': 'Captain Vova (Vova Feldman)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=104s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'Records that already set kind of the standards for the prices for Merchant of '
              "Record in the market. Whether you've been following the events or not, last "
              'year Stripe acquired payment solution called Lemon Squeezy, a Merchant of '
              'Record actually.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Records that already set kind of the standards for the prices for Merchant of '
             "Record in the market. Whether you've been following the events or not, last year "
             'Stripe acquired payment solution called Lemon Squeezy, a Merchant of Record '
             'actually.',
      'title': 'Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain '
               'Vova (Vova Feldman))',
      'url': 'https://www.youtube.com/watch?v=5zGuxRrg_O0&t=104s',
      'video_id': '5zGuxRrg_O0'},
     {'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=i05UCC3UvNY&t=120s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'Stripe Tax can calculate and collect tax for you, but registering and filing '
              'are only included in its Tax Complete plan, which starts at ninety dollars a '
              'month. Lemon Squeezy and Paddle each say they are your merchant of record.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'Stripe Tax can calculate and collect tax for you, but registering and filing are '
             'only included in its Tax Complete plan, which starts at ninety dollars a month. '
             'Lemon Squeezy and Paddle each say they are your merchant of record.',
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=120s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=185s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'They handle a sepa, so dozens of local methods. Lemon Squeezy supports 135 plus '
              'countries for payments and 20 plus payment methods including cards, PayPal, '
              "Apple Pay, Google Pay, Alipay, and WeChat Pay. Paddle's reach is technically "
              'broader. This is mixed on both sides.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'They handle a sepa, so dozens of local methods. Lemon Squeezy supports 135 plus '
             'countries for payments and 20 plus payment methods including cards, PayPal, '
             "Apple Pay, Google Pay, Alipay, and WeChat Pay. Paddle's reach is technically "
             'broader. This is mixed on both sides.',
      'title': 'Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech)',
      'url': 'https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=185s',
      'video_id': 'Qq-EyvVj7IM'},
     {'author': 'HelperMan',
      'channel': 'HelperMan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=IA4eosnOzIE&t=80s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'But there there are definitely some downsides you should know before using it. '
              'First, fees can feel higher compared to using a standard payment processor '
              "directly because you're paying for the extra tax and compliance handling.",
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'But there there are definitely some downsides you should know before using it. '
             'First, fees can feel higher compared to using a standard payment processor '
             "directly because you're paying for the extra tax and compliance handling.",
      'title': 'Lemon Squeezy for Merchant of Record Honest Review - Watch Before Using '
               '(HelperMan)',
      'url': 'https://www.youtube.com/watch?v=IA4eosnOzIE&t=80s',
      'video_id': 'IA4eosnOzIE'},
     {'author': 'How2Genius',
      'channel': 'How2Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=140s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'You can create fully branded storefronts and checkout experiences, including '
              'upsells, bundles, and localized pricing. It also supports a wide range of '
              'payment methods, credit cards, PayPal, Apple Pay, and more, so customers can '
              'pay however they prefer.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'You can create fully branded storefronts and checkout experiences, including '
             'upsells, bundles, and localized pricing. It also supports a wide range of '
             'payment methods, credit cards, PayPal, Apple Pay, and more, so customers can pay '
             'however they prefer.',
      'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
               '(How2Genius)',
      'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=140s',
      'video_id': 'Y5VXhUB7aNM'},
     {'author': 'BrightGuide',
      'channel': 'BrightGuide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=oMxSmqY3mzM&t=62s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'From there, select your currency. Make sure you choose the currency you want to '
              'sell in, especially if your if your audience is based in a particular region. '
              'Once the currency is set, enter your product price. This is the amount '
              'customers will pay for your template.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'From there, select your currency. Make sure you choose the currency you want to '
             'sell in, especially if your if your audience is based in a particular region. '
             'Once the currency is set, enter your product price. This is the amount customers '
             'will pay for your template.',
      'title': 'How to Sell Notion Templates on Gumroad (Step By Step 2026) (BrightGuide)',
      'url': 'https://www.youtube.com/watch?v=oMxSmqY3mzM&t=62s',
      'video_id': 'oMxSmqY3mzM'},
     {'author': 'Framer',
      'channel': 'Framer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=RN0VWAvL-qc&t=218s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'So it is important that you use this link and send it to us or share it on '
              'Twitter or share it anywhere you want so you can copy this share it wherever '
              'you want and then that is how you start selling your templates through lemon '
              'squeezy thanks for watching.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'So it is important that you use this link and send it to us or share it on '
             'Twitter or share it anywhere you want so you can copy this share it wherever you '
             'want and then that is how you start selling your templates through lemon squeezy '
             'thanks for watching.',
      'title': 'How to start selling your Framer templates through Lemon Squeezy (Framer)',
      'url': 'https://www.youtube.com/watch?v=RN0VWAvL-qc&t=218s',
      'video_id': 'RN0VWAvL-qc'},
     {'author': 'Tutorials At Desk',
      'channel': 'Tutorials At Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=VEFf-FR0dxw&t=225s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'After that, follow the on-screen instructions to connect a supported payout '
              'method such as Stripe or PayPal, depending on what Gumroad offers in your '
              "region. You'll be asked to complete identity verification and payment setup.",
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'After that, follow the on-screen instructions to connect a supported payout '
             'method such as Stripe or PayPal, depending on what Gumroad offers in your '
             "region. You'll be asked to complete identity verification and payment setup.",
      'title': 'How to Sell Notion Templates on Gumroad (2026 Revenue Snapshot) (Tutorials At '
               'Desk)',
      'url': 'https://www.youtube.com/watch?v=VEFf-FR0dxw&t=225s',
      'video_id': 'VEFf-FR0dxw'},
     {'author': 'Stephen S.',
      'channel': 'Stephen S.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'So I had to go in and specify the correct tax classification. So in this case, '
              'software as a service personal use for these products. But once you do that, '
              'then the uh checkout API will work and it will open up these pages.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'So I had to go in and specify the correct tax classification. So in this case, '
             'software as a service personal use for these products. But once you do that, '
             'then the uh checkout API will work and it will open up these pages.',
      'title': "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an "
               'Existing App  #mcp (Stephen S.)',
      'url': 'https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s',
      'video_id': 'F-WZgXuQIuQ'},
     {'author': 'HelperMan',
      'channel': 'HelperMan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=o3KRrFnoAgM&t=120s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
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
      'video_id': 'o3KRrFnoAgM'},
     {'author': 'Marketing Mark',
      'channel': 'Marketing Mark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=45s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': 'So, what we want to do to add a one-click upsell, and by one-click upsell I '
              "mean that since we've captured their payment information on our checkout page, "
              'the system has that stored.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'So, what we want to do to add a one-click upsell, and by one-click upsell I mean '
             "that since we've captured their payment information on our checkout page, the "
             'system has that stored.',
      'title': 'How to Build 1 Click Upsells in GoHighLevel (Marketing Mark)',
      'url': 'https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=45s',
      'video_id': '0u4Tmd6BlWA'},
     {'author': "Extreme How To's",
      'channel': "Extreme How To's",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=SK_-uXSKE88&t=106s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': '" This instruction will guide users through the process of obtaining the '
              'template. For pricing options, you can choose to toggle on allow customers to '
              'pay what they want. This feature can attract more buyers as it offers '
              'flexibility in pricing.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': '" This instruction will guide users through the process of obtaining the '
             'template. For pricing options, you can choose to toggle on allow customers to '
             'pay what they want. This feature can attract more buyers as it offers '
             'flexibility in pricing.',
      'title': "How to sell Notion templates on Gumroad[2026 Full Guide] (Extreme How To's)",
      'url': 'https://www.youtube.com/watch?v=SK_-uXSKE88&t=106s',
      'video_id': 'SK_-uXSKE88'},
     {'author': 'Rochelle Be',
      'channel': 'Rochelle Be',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=4e4pRrWsJvU&t=426s)',
      'relevance': 'Attributed practitioner commentary on buyer psychology, Merchant-of-Record '
                   'platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement.',
      'source_type': 'video_pro_tip',
      'text': "'t even know that you're good at problem solving in that area. Okay, so that's "
              "the second circle. We're now on to circle three, which is what people pay for. "
              'Because we want things that people are actually going to pay you money for. You '
              'might be good at rock collecting.',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': "'t even know that you're good at problem solving in that area. Okay, so that's "
             "the second circle. We're now on to circle three, which is what people pay for. "
             'Because we want things that people are actually going to pay you money for. You '
             'might be good at rock collecting.',
      'title': 'How to Start Selling Digital Products in 2026 (Step-by-Step Tutorial) '
               '(Rochelle Be)',
      'url': 'https://www.youtube.com/watch?v=4e4pRrWsJvU&t=426s',
      'video_id': '4e4pRrWsJvU'}],
 3: [{'author': 'Funnel Building Secrets',
      'channel': 'Funnel Building Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=BZ4rml1tc1U&t=106s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Finally, test your funnel to make sure your order bump and upsell flow '
              "smoothly. Place a test order to confirm that both are working correctly. You've "
              'successfully set up an order bump and upsell in ClickFunnels. Two simple tweaks '
              'that can dramatically increase your revenue.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Finally, test your funnel to make sure your order bump and upsell flow smoothly. '
             "Place a test order to confirm that both are working correctly. You've "
             'successfully set up an order bump and upsell in ClickFunnels. Two simple tweaks '
             'that can dramatically increase your revenue.',
      'title': 'How to Set Up an Order Bump and Upsell (Funnel Building Secrets)',
      'url': 'https://www.youtube.com/watch?v=BZ4rml1tc1U&t=106s',
      'video_id': 'BZ4rml1tc1U'},
     {'author': 'Zero to Launch',
      'channel': 'Zero to Launch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=u9nHXAMBUe4&t=249s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': "The statement descriptor is the short text on the buyer's bank statement. I'll "
              'put um plant checklist. An order bump takes one price and only one. On the '
              'upsell, the plus was still there after the first plan. Click save at the bottom '
              'of the section.',
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': "The statement descriptor is the short text on the buyer's bank statement. I'll "
             'put um plant checklist. An order bump takes one price and only one. On the '
             'upsell, the plus was still there after the first plan. Click save at the bottom '
             'of the section.',
      'title': 'Order Bump or Upsell in Systeme.io: Which Should You Add First? (Zero to '
               'Launch)',
      'url': 'https://www.youtube.com/watch?v=u9nHXAMBUe4&t=249s',
      'video_id': 'u9nHXAMBUe4'},
     {'author': 'SamCart',
      'channel': 'SamCart',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=UxhtBuVj4gY&t=140s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'And so for every 100 customers, 30 of them would say, cool, let me add the '
              'order bump. And that was an extra $750 in revenue. But then things got '
              'supercharged when we added our first one-click upsell.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'And so for every 100 customers, 30 of them would say, cool, let me add the order '
             'bump. And that was an extra $750 in revenue. But then things got supercharged '
             'when we added our first one-click upsell.',
      'title': 'The Complete Guide to Upsells ($8 Billion in Data) (SamCart)',
      'url': 'https://www.youtube.com/watch?v=UxhtBuVj4gY&t=140s',
      'video_id': 'UxhtBuVj4gY'},
     {'author': 'Marketing Mark',
      'channel': 'Marketing Mark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=qUqLPLYblBI&t=76s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': "Now you'll see this product below has this tag below it that says bump. So, in "
              "order to do that, once we've added our main product, we'll just go ahead and "
              "we'll add a second product. And we will select that and select our price.",
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "Now you'll see this product below has this tag below it that says bump. So, in "
             "order to do that, once we've added our main product, we'll just go ahead and "
             "we'll add a second product. And we will select that and select our price.",
      'title': 'How to Add Order Bumps in GoHighLevel (Plus Easy One-Click Upsells) (Marketing '
               'Mark)',
      'url': 'https://www.youtube.com/watch?v=qUqLPLYblBI&t=76s',
      'video_id': 'qUqLPLYblBI'},
     {'author': 'Skool News',
      'channel': 'Skool News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=Oeug9IgSFXc&t=69s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'You can have a premium tier that you can set the price for, and you can have a '
              'VIP tier that you can set the price for. Then tiers, which is two to three paid '
              'tiers, right? You can set the prices like that. Um, you can just have two if '
              'you want or three.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'You can have a premium tier that you can set the price for, and you can have a '
             'VIP tier that you can set the price for. Then tiers, which is two to three paid '
             'tiers, right? You can set the prices like that. Um, you can just have two if you '
             'want or three.',
      'title': 'Membership TIERS Are Here | Skool News #33 (Skool News)',
      'url': 'https://www.youtube.com/watch?v=Oeug9IgSFXc&t=69s',
      'video_id': 'Oeug9IgSFXc'},
     {'author': 'CRM Tutorials Library',
      'channel': 'CRM Tutorials Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=pz33EMSEtfY&t=72s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Set the price that matches your offer. Open additional options and enable bump '
              'product. An order bump is a small, complimentary add-on shown on the checkout '
              'page that customers can add with a single click. Great for increasing average '
              'order value without adding friction.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Set the price that matches your offer. Open additional options and enable bump '
             'product. An order bump is a small, complimentary add-on shown on the checkout '
             'page that customers can add with a single click. Great for increasing average '
             'order value without adding friction.',
      'title': 'How to Set Up Main Product, Order Bump, Upsell & Downsell in GoHighLevel | '
               'Step-by-Step (CRM Tutorials Library)',
      'url': 'https://www.youtube.com/watch?v=pz33EMSEtfY&t=72s',
      'video_id': 'pz33EMSEtfY'},
     {'author': 'Maik Kleinert | Content-to-Conversion Systems',
      'channel': 'Maik Kleinert | Content-to-Conversion Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:49](https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=649s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Number four, the order bumps. So for the order bumps, now the money part is $7 '
              'sales is almost zero profit on its own. So at the checkout where the buyer is '
              'already saying yes, I add the order bump.',
      'timestamp': 649,
      'timestamp_label': '[00:10:49]',
      'timestamp_seconds': 649,
      'tip': 'Number four, the order bumps. So for the order bumps, now the money part is $7 '
             'sales is almost zero profit on its own. So at the checkout where the buyer is '
             'already saying yes, I add the order bump.',
      'title': 'I Upsold A $7 Product To $57  With DM Automation + Order Bump Setup ( Full '
               'System Explained ) (Maik Kleinert | Content-to-Conversion Systems)',
      'url': 'https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=649s',
      'video_id': 'pE2Z7vTYfSw'},
     {'author': 'Maria Wendt',
      'channel': 'Maria Wendt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:45](https://www.youtube.com/watch?v=zQQZEPMxT6U&t=465s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': "'s their competitive advantage, so they never talk about it. So, you might be "
              "like, this might be the first time you've ever heard of an order bump or an "
              'upsell.',
      'timestamp': 465,
      'timestamp_label': '[00:07:45]',
      'timestamp_seconds': 465,
      'tip': "'s their competitive advantage, so they never talk about it. So, you might be "
             "like, this might be the first time you've ever heard of an order bump or an "
             'upsell.',
      'title': 'How To Turn Your $24 Digital Product Into $24,000 (Scaling Strategy That '
               'Works) (Maria Wendt)',
      'url': 'https://www.youtube.com/watch?v=zQQZEPMxT6U&t=465s',
      'video_id': 'zQQZEPMxT6U'},
     {'author': 'Profitable Talents',
      'channel': 'Profitable Talents',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:38](https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=398s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'The offer is going to be is going to have an order bump, which is going to be '
              "again fairly cheap, and I'm going to add an upsell. This is going to be "
              'slightly more expensive.',
      'timestamp': 398,
      'timestamp_label': '[00:06:38]',
      'timestamp_seconds': 398,
      'tip': 'The offer is going to be is going to have an order bump, which is going to be '
             "again fairly cheap, and I'm going to add an upsell. This is going to be slightly "
             'more expensive.',
      'title': 'Watch Me Build a Self-Liquidating Offer Funnel From Scratch (Ep. 1) '
               '(Profitable Talents)',
      'url': 'https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=398s',
      'video_id': '_I5YFl6Ym_k'},
     {'author': "Extreme How To's",
      'channel': "Extreme How To's",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=SK_-uXSKE88&t=108s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'For pricing options, you can choose to toggle on allow customers to pay what '
              'they want. This feature can attract more buyers as it offers flexibility in '
              'pricing. Set a minimum price of $5 to ensure that you receive compensation for '
              'your work.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'For pricing options, you can choose to toggle on allow customers to pay what '
             'they want. This feature can attract more buyers as it offers flexibility in '
             'pricing. Set a minimum price of $5 to ensure that you receive compensation for '
             'your work.',
      'title': "How to sell Notion templates on Gumroad[2026 Full Guide] (Extreme How To's)",
      'url': 'https://www.youtube.com/watch?v=SK_-uXSKE88&t=108s',
      'video_id': 'SK_-uXSKE88'},
     {'author': 'How2Genius',
      'channel': 'How2Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=72s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Paddle gives detailed analytics as well. You can track revenue, conversion '
              'rates, churn, and customer behavior all in one dashboard. This makes it easier '
              'to understand which products are performing best, optimize pricing, and '
              'forecast growth.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Paddle gives detailed analytics as well. You can track revenue, conversion '
             'rates, churn, and customer behavior all in one dashboard. This makes it easier '
             'to understand which products are performing best, optimize pricing, and forecast '
             'growth.',
      'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
               '(How2Genius)',
      'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=72s',
      'video_id': 'Y5VXhUB7aNM'},
     {'author': 'Sell Your Service',
      'channel': 'Sell Your Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:33](https://www.youtube.com/watch?v=_csKVgudVVY&t=453s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': "And if you're smart, you'll put an order bump on there as well. And I'll show "
              "you how to do that in high level, in another video. So I'm saying, thanks for "
              "downloading your three-step lead generation plan. It's on his way to your "
              'inbox.',
      'timestamp': 453,
      'timestamp_label': '[00:07:33]',
      'timestamp_seconds': 453,
      'tip': "And if you're smart, you'll put an order bump on there as well. And I'll show "
             "you how to do that in high level, in another video. So I'm saying, thanks for "
             "downloading your three-step lead generation plan. It's on his way to your inbox.",
      'title': 'How To Build A Self Liquidating Offer Funnel In HighLevel | Ryan Deiss (SLO) '
               '(Sell Your Service)',
      'url': 'https://www.youtube.com/watch?v=_csKVgudVVY&t=453s',
      'video_id': '_csKVgudVVY'},
     {'author': 'Tatyana Savage',
      'channel': 'Tatyana Savage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:01](https://www.youtube.com/watch?v=TGNTFquVxZU&t=421s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Moving on to tip number two, you have to treat your Etsy shop like a business '
              'in order for it to make a profit. And every single business requires two types '
              'of investment in order for it to get off the ground.',
      'timestamp': 421,
      'timestamp_label': '[00:07:01]',
      'timestamp_seconds': 421,
      'tip': 'Moving on to tip number two, you have to treat your Etsy shop like a business in '
             'order for it to make a profit. And every single business requires two types of '
             'investment in order for it to get off the ground.',
      'title': 'How to Start a Digital Product Business (& ACTUALLY Make Money) (Tatyana '
               'Savage)',
      'url': 'https://www.youtube.com/watch?v=TGNTFquVxZU&t=421s',
      'video_id': 'TGNTFquVxZU'},
     {'author': 'Stellar Media',
      'channel': 'Stellar Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=YiY_qBBHvvc&t=66s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': 'Now in order to sell it click on the option new product and here you have to '
              'enter the name of your product just like I will do write notion template from '
              'this you have to select this option digital product. Scroll down and here is '
              'the pricing.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Now in order to sell it click on the option new product and here you have to '
             'enter the name of your product just like I will do write notion template from '
             'this you have to select this option digital product. Scroll down and here is the '
             'pricing.',
      'title': 'How To Sell Notion Templates On Gumroad 2025 (Step by Step) (Stellar Media)',
      'url': 'https://www.youtube.com/watch?v=YiY_qBBHvvc&t=66s',
      'video_id': 'YiY_qBBHvvc'},
     {'author': 'GROUNDTECHY',
      'channel': 'GROUNDTECHY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=F73hzfI-XsE&t=276s)',
      'relevance': 'Attributed practitioner commentary on pricing tiers, order bumps, 1-click '
                   'upsells, self-liquidating offers (SLOs), and net contribution margins.',
      'source_type': 'video_pro_tip',
      'text': "Thank you page and it really doesn't matter what they decide on in the second "
              'upsell whether they accept the offer or decline the offer the last step for '
              'them will be the thank you page.',
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': "Thank you page and it really doesn't matter what they decide on in the second "
             'upsell whether they accept the offer or decline the offer the last step for them '
             'will be the thank you page.',
      'title': 'How to Setup Sell funnel Upsells, downsells, order bumps on Systemeio '
               '(GROUNDTECHY)',
      'url': 'https://www.youtube.com/watch?v=F73hzfI-XsE&t=276s',
      'video_id': 'F73hzfI-XsE'}],
 4: [{'author': 'Nathan Nazareth',
      'channel': 'Nathan Nazareth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=dr37DaI8g3U&t=20s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'You also have no inventory or fulfillment cost, no shipping and delivery costs, '
              'no customer service headaches because your customers get the product '
              'immediately. And thanks to AI, you can build your product for 100% free, and it '
              "won't take you as long as you think.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'You also have no inventory or fulfillment cost, no shipping and delivery costs, '
             'no customer service headaches because your customers get the product '
             'immediately. And thanks to AI, you can build your product for 100% free, and it '
             "won't take you as long as you think.",
      'title': "How to Sell AI Digital Products (beginner's guide) (Nathan Nazareth)",
      'url': 'https://www.youtube.com/watch?v=dr37DaI8g3U&t=20s',
      'video_id': 'dr37DaI8g3U'},
     {'author': 'Pete McPherson DYEB',
      'channel': 'Pete McPherson DYEB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=wYKYVjEiqLY&t=21s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'s email address, you'll be promoting a very specific offer stack. A very "
              'specific offer that will liquidate the cost of running ads.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "'s email address, you'll be promoting a very specific offer stack. A very "
             'specific offer that will liquidate the cost of running ads.',
      'title': 'How to launch your SELF-LIQUIDATING OFFER Funnel (with real-world examples!) '
               '(Pete McPherson DYEB)',
      'url': 'https://www.youtube.com/watch?v=wYKYVjEiqLY&t=21s',
      'video_id': 'wYKYVjEiqLY'},
     {'author': 'Social Nest Marketing',
      'channel': 'Social Nest Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:17](https://www.youtube.com/watch?v=-xCVVPZu48k&t=677s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'s going to give us this link, but you have to actually set up a custom domain. "
              "So, I'm just going to put this link in here for right now. But, this won't be "
              "the final link that you're going to use cuz you have to do you have to set up a "
              'custom domain for this um funnel.',
      'timestamp': 677,
      'timestamp_label': '[00:11:17]',
      'timestamp_seconds': 677,
      'tip': "'s going to give us this link, but you have to actually set up a custom domain. "
             "So, I'm just going to put this link in here for right now. But, this won't be "
             "the final link that you're going to use cuz you have to do you have to set up a "
             'custom domain for this um funnel.',
      'title': 'GoHighLevel One-Click Upsell Setup: Payment Link Redirect + Auto-Delivery '
               'Workflow (Part 6) (Social Nest Marketing)',
      'url': 'https://www.youtube.com/watch?v=-xCVVPZu48k&t=677s',
      'video_id': '-xCVVPZu48k'},
     {'author': 'Tatyana Savage',
      'channel': 'Tatyana Savage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:27](https://www.youtube.com/watch?v=TGNTFquVxZU&t=627s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "I started using Xero, who's actually partnering with me for this portion of "
              "today's video. Xero's a cloud-based accounting platform that helps small "
              'businesses manage their finances. And you might be thinking, "I don\'t have a '
              'business.',
      'timestamp': 627,
      'timestamp_label': '[00:10:27]',
      'timestamp_seconds': 627,
      'tip': "I started using Xero, who's actually partnering with me for this portion of "
             "today's video. Xero's a cloud-based accounting platform that helps small "
             'businesses manage their finances. And you might be thinking, "I don\'t have a '
             'business.',
      'title': 'How to Start a Digital Product Business (& ACTUALLY Make Money) (Tatyana '
               'Savage)',
      'url': 'https://www.youtube.com/watch?v=TGNTFquVxZU&t=627s',
      'video_id': 'TGNTFquVxZU'},
     {'author': 'Iman Gadzhi',
      'channel': 'Iman Gadzhi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:36](https://www.youtube.com/watch?v=A-yBamfrXQs&t=1896s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'You start with your product price as your daily budget. So, if your product is '
              '$30, start with $30 a day. Use AI tools to create your ad headlines. Remove '
              "irrelevant search terms that don't convert like notion sound effects if you're "
              'selling productivity templates.',
      'timestamp': 1896,
      'timestamp_label': '[00:31:36]',
      'timestamp_seconds': 1896,
      'tip': 'You start with your product price as your daily budget. So, if your product is '
             '$30, start with $30 a day. Use AI tools to create your ad headlines. Remove '
             "irrelevant search terms that don't convert like notion sound effects if you're "
             'selling productivity templates.',
      'title': 'Copy This Method To Make $2,700/Week with Digital Products (Iman Gadzhi)',
      'url': 'https://www.youtube.com/watch?v=A-yBamfrXQs&t=1896s',
      'video_id': 'A-yBamfrXQs'},
     {'author': 'How To Tutor',
      'channel': 'How To Tutor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=Sxl5Fxp0qVQ&t=100s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "'ve just copied into this section. Scroll down and you can also upload the "
              'cover of the specific product. You can add integrations, create different '
              'versions of this product. And then in this section, you can also incorporate '
              'the domain of your template.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "'ve just copied into this section. Scroll down and you can also upload the cover "
             'of the specific product. You can add integrations, create different versions of '
             'this product. And then in this section, you can also incorporate the domain of '
             'your template.',
      'title': 'How to Upload Notion Template on Gumroad 2025 (QUICK GUIDE) (How To Tutor)',
      'url': 'https://www.youtube.com/watch?v=Sxl5Fxp0qVQ&t=100s',
      'video_id': 'Sxl5Fxp0qVQ'},
     {'author': 'Folioquest',
      'channel': 'Folioquest',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=M61DsgB51BI&t=173s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Now founders have until March 31st, 2027 to move and a fresh reminder that even '
              'beloved startup tools can vanish inside a giant acquisition.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'Now founders have until March 31st, 2027 to move and a fresh reminder that even '
             'beloved startup tools can vanish inside a giant acquisition.',
      'title': 'Lemon Squeezy Winds Down After Stripe Acquisition (Folioquest)',
      'url': 'https://www.youtube.com/watch?v=M61DsgB51BI&t=173s',
      'video_id': 'M61DsgB51BI'},
     {'author': 'Richard Yu',
      'channel': 'Richard Yu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:31](https://www.youtube.com/watch?v=OGyxSOcL1F0&t=571s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'But, seeing it explained in a video versus actually watching it being built in '
              "real time in front of your eyes are two completely different things. So, here's "
              "what I'd like to give to you for absolutely free. Later this week, I'm hosting "
              'an exclusive private VIP workshop.',
      'timestamp': 571,
      'timestamp_label': '[00:09:31]',
      'timestamp_seconds': 571,
      'tip': 'But, seeing it explained in a video versus actually watching it being built in '
             "real time in front of your eyes are two completely different things. So, here's "
             "what I'd like to give to you for absolutely free. Later this week, I'm hosting "
             'an exclusive private VIP workshop.',
      'title': 'How I Built a $57K/Month Digital Product Business From Scratch (Full System) '
               '(Richard Yu)',
      'url': 'https://www.youtube.com/watch?v=OGyxSOcL1F0&t=571s',
      'video_id': 'OGyxSOcL1F0'},
     {'author': 'Stellar Media',
      'channel': 'Stellar Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=YiY_qBBHvvc&t=145s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "And this one is the additional detail and it's an important feature of your "
              'product. If you want to add an additional detail then click on it and add but '
              'for now I will let it be as it is. The amount will be the same and here is the '
              'option of custom domain.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': "And this one is the additional detail and it's an important feature of your "
             'product. If you want to add an additional detail then click on it and add but '
             'for now I will let it be as it is. The amount will be the same and here is the '
             'option of custom domain.',
      'title': 'How To Sell Notion Templates On Gumroad 2025 (Step by Step) (Stellar Media)',
      'url': 'https://www.youtube.com/watch?v=YiY_qBBHvvc&t=145s',
      'video_id': 'YiY_qBBHvvc'},
     {'author': 'Pam Obasa',
      'channel': 'Pam Obasa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:02](https://www.youtube.com/watch?v=Kgj8rFDeRIs&t=1322s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Schedule your breakthrough call there is no cost you can literally come on the '
              'call ask any question that you have and we would be glad to support you so make '
              "sure you click on that link and schedule your call if you need to I'll see you "
              'in the next training.',
      'timestamp': 1322,
      'timestamp_label': '[00:22:02]',
      'timestamp_seconds': 1322,
      'tip': 'Schedule your breakthrough call there is no cost you can literally come on the '
             'call ask any question that you have and we would be glad to support you so make '
             "sure you click on that link and schedule your call if you need to I'll see you "
             'in the next training.',
      'title': 'How To Create A Self-liquidating Offer Funnel For Your Business (Pam Obasa)',
      'url': 'https://www.youtube.com/watch?v=Kgj8rFDeRIs&t=1322s',
      'video_id': 'Kgj8rFDeRIs'},
     {'author': 'Mariana Henninger',
      'channel': 'Mariana Henninger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:16](https://www.youtube.com/watch?v=Ii70ybaGJ68&t=1876s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'Especially at a a lower budget. I mean, 400 is all relative because some people '
              "listening might be like, I can't spend more than $20 a day.",
      'timestamp': 1876,
      'timestamp_label': '[00:31:16]',
      'timestamp_seconds': 1876,
      'tip': 'Especially at a a lower budget. I mean, 400 is all relative because some people '
             "listening might be like, I can't spend more than $20 a day.",
      'title': 'A Low-Ticket Tiny Offer SLO Funnel Fuels High-Ticket Sales with Allie Bjerk '
               '(Mariana Henninger)',
      'url': 'https://www.youtube.com/watch?v=Ii70ybaGJ68&t=1876s',
      'video_id': 'Ii70ybaGJ68'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:34](https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=454s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "So I'm completely I'm comfortable with them, and can make sure you have that "
              'done right after you get the agreements. And the next question, how do you deal '
              'with special situations, like, how do you deal with an estate, an LLC, a '
              'divorced couple?',
      'timestamp': 454,
      'timestamp_label': '[00:07:34]',
      'timestamp_seconds': 454,
      'tip': "So I'm completely I'm comfortable with them, and can make sure you have that "
             'done right after you get the agreements. And the next question, how do you deal '
             'with special situations, like, how do you deal with an estate, an LLC, a '
             'divorced couple?',
      'title': "Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney)",
      'url': 'https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=454s',
      'video_id': 'qGPsbhsEAVQ'},
     {'author': 'Maik Kleinert | Content-to-Conversion Systems',
      'channel': 'Maik Kleinert | Content-to-Conversion Systems',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:17](https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=317s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'What we have set up here is basically which DM trigger. We have all the word in '
              'different capital letters, small, and set up the Instagram account here and '
              'publish post.',
      'timestamp': 317,
      'timestamp_label': '[00:05:17]',
      'timestamp_seconds': 317,
      'tip': 'What we have set up here is basically which DM trigger. We have all the word in '
             'different capital letters, small, and set up the Instagram account here and '
             'publish post.',
      'title': 'I Upsold A $7 Product To $57  With DM Automation + Order Bump Setup ( Full '
               'System Explained ) (Maik Kleinert | Content-to-Conversion Systems)',
      'url': 'https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=317s',
      'video_id': 'pE2Z7vTYfSw'},
     {'author': 'Aeris Vale Tutorials',
      'channel': 'Aeris Vale Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=137s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': "Then input a concise summary to reinforce your product's value. You can also "
              'include additional details that might intrigue or inform your audience further. '
              'Customizing your domain is another option to make your product page feel more '
              'personal or branded.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "Then input a concise summary to reinforce your product's value. You can also "
             'include additional details that might intrigue or inform your audience further. '
             'Customizing your domain is another option to make your product page feel more '
             'personal or branded.',
      'title': 'How To Sell A Notion Template On Gumroad - Step by Step Guide | THELOSTOFFER '
               '#notion #gumroad (Aeris Vale Tutorials)',
      'url': 'https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=137s',
      'video_id': 'ciKrPZ_nIpQ'},
     {'author': 'Doug Boughton',
      'channel': 'Doug Boughton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:43](https://www.youtube.com/watch?v=8lz_gy-Osw8&t=1003s)',
      'relevance': 'Attributed practitioner commentary on zero-COGS serverless stacks, '
                   'cloud/AI credit grants, lean entity setup, and contractor IP ownership.',
      'source_type': 'video_pro_tip',
      'text': 'And if that is you, you get Event Stack for free when you say yes today. So '
              'inside the community, if you go to settings and you grab your link, this is '
              'going to be your affiliate link, your unique link.',
      'timestamp': 1003,
      'timestamp_label': '[00:16:43]',
      'timestamp_seconds': 1003,
      'tip': 'And if that is you, you get Event Stack for free when you say yes today. So '
             'inside the community, if you go to settings and you grab your link, this is '
             'going to be your affiliate link, your unique link.',
      'title': 'Are Free Skool Communities Dying? Why I Turned Mine Paid (Doug Boughton)',
      'url': 'https://www.youtube.com/watch?v=8lz_gy-Osw8&t=1003s',
      'video_id': '8lz_gy-Osw8'}],
 5: [{'author': 'TechWealth Hub',
      'channel': 'TechWealth Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=79s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'Stripe calculates it, collects it, files it, and remits it. Stripes already '
              'best in class at this, but now they are taking on the liability. Third, dispute '
              'management, chargebacks. Fourth, customer support for payment issues.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Stripe calculates it, collects it, files it, and remits it. Stripes already best '
             'in class at this, but now they are taking on the liability. Third, dispute '
             'management, chargebacks. Fourth, customer support for payment issues.',
      'title': 'Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub)',
      'url': 'https://www.youtube.com/watch?v=KRdWGDk-GkY&t=79s',
      'video_id': 'KRdWGDk-GkY'},
     {'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=i05UCC3UvNY&t=172s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'International cards add one point five percent, and currency conversion adds '
              'another one percent. Each dispute costs fifteen dollars, and standard payouts '
              "are free. Stripe Tax's no-code option is half a percent per transaction, where "
              "you're registered to collect.",
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'International cards add one point five percent, and currency conversion adds '
             'another one percent. Each dispute costs fifteen dollars, and standard payouts '
             "are free. Stripe Tax's no-code option is half a percent per transaction, where "
             "you're registered to collect.",
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=172s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=29s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'Stripe Checkout is a standard payment processor, while Paddle and Lemon Squeezy '
              'act as a merchant of record. A merchant of record means the platform becomes '
              'the legal seller of your product.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': 'Stripe Checkout is a standard payment processor, while Paddle and Lemon Squeezy '
             'act as a merchant of record. A merchant of record means the platform becomes the '
             'legal seller of your product.',
      'title': 'Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? '
               '(Tutorly)',
      'url': 'https://www.youtube.com/watch?v=IfaCBBIoVK0&t=29s',
      'video_id': 'IfaCBBIoVK0'},
     {'author': 'Eden',
      'channel': 'Eden',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:26](https://www.youtube.com/watch?v=VJ-JR7uMY34&t=386s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "We're just starting out with your very first product. And so the way that we do "
              'this inside of Eden is with the discover feature or the chat feature being able '
              'to pull trending posts and high performing posts from any platform on social '
              'media.',
      'timestamp': 386,
      'timestamp_label': '[00:06:26]',
      'timestamp_seconds': 386,
      'tip': "We're just starting out with your very first product. And so the way that we do "
             'this inside of Eden is with the discover feature or the chat feature being able '
             'to pull trending posts and high performing posts from any platform on social '
             'media.',
      'title': 'How To Build Your First $10,000 Digital Product (Full Beginner Guide) (Eden)',
      'url': 'https://www.youtube.com/watch?v=VJ-JR7uMY34&t=386s',
      'video_id': 'VJ-JR7uMY34'},
     {'author': 'Stephen S.',
      'channel': 'Stephen S.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=20s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "'ll use this to wire up the checkout using the Stripe power. So now when I go "
              'into the app in Curo here, I can see that over on the left hand side I have '
              'powers.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "'ll use this to wire up the checkout using the Stripe power. So now when I go "
             'into the app in Curo here, I can see that over on the left hand side I have '
             'powers.',
      'title': "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an "
               'Existing App  #mcp (Stephen S.)',
      'url': 'https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=20s',
      'video_id': 'F-WZgXuQIuQ'},
     {'author': 'Richard Yu',
      'channel': 'Richard Yu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:24](https://www.youtube.com/watch?v=RxypuPGBRPI&t=1164s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': '997 tuition and make that program free for you. AI platform, Wix, in order to '
              'build your AI website, which by the way, you are going to need their platform '
              'anyways, regardless of whether you work with me or not, because you need a good '
              'tool to build your website.',
      'timestamp': 1164,
      'timestamp_label': '[00:19:24]',
      'timestamp_seconds': 1164,
      'tip': '997 tuition and make that program free for you. AI platform, Wix, in order to '
             'build your AI website, which by the way, you are going to need their platform '
             'anyways, regardless of whether you work with me or not, because you need a good '
             'tool to build your website.',
      'title': 'I Made $32.7 Million Selling Simple Digital Products (Full Masterclass) '
               '(Richard Yu)',
      'url': 'https://www.youtube.com/watch?v=RxypuPGBRPI&t=1164s',
      'video_id': 'RxypuPGBRPI'},
     {'author': 'Alek',
      'channel': 'Alek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=T-gfoXzz8k8&t=278s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "And so we're able to optimize the products we create from start to finish for "
              "that platform. A lot of people say that Etsy is too competitive or that it's "
              'oversaturated and a race to the bottom.',
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "And so we're able to optimize the products we create from start to finish for "
             "that platform. A lot of people say that Etsy is too competitive or that it's "
             'oversaturated and a race to the bottom.',
      'title': 'Build & Sell Digital Products with A.I. (Full Course) (Alek)',
      'url': 'https://www.youtube.com/watch?v=T-gfoXzz8k8&t=278s',
      'video_id': 'T-gfoXzz8k8'},
     {'author': 'Extreme Guides',
      'channel': 'Extreme Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=2zWJQPegtuk&t=64s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'Once the page loads, log into your Gumroad account or create one if you do not '
              'have an existing account. This platform will be where you list your notion '
              'template for sale. Click on the start selling button to initiate the process of '
              'listing a new product.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Once the page loads, log into your Gumroad account or create one if you do not '
             'have an existing account. This platform will be where you list your notion '
             'template for sale. Click on the start selling button to initiate the process of '
             'listing a new product.',
      'title': 'How to sell Notion templates on Gumroad[FULL GUIDE] (Extreme Guides)',
      'url': 'https://www.youtube.com/watch?v=2zWJQPegtuk&t=64s',
      'video_id': '2zWJQPegtuk'},
     {'author': 'Max Auren',
      'channel': 'Max Auren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=kmRwEjvxk-w&t=364s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'I hope Luigi is not coming for me. And because these ads I show in front of '
              "people that don't know me, we had maybe five refunds on 3,000s of sales so far "
              'because someone already watched the YouTube video.',
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': 'I hope Luigi is not coming for me. And because these ads I show in front of '
             "people that don't know me, we had maybe five refunds on 3,000s of sales so far "
             'because someone already watched the YouTube video.',
      'title': 'How My $7 Sales Funnel Makes Me $18k/m (Max Auren)',
      'url': 'https://www.youtube.com/watch?v=kmRwEjvxk-w&t=364s',
      'video_id': 'kmRwEjvxk-w'},
     {'author': 'Click Guide',
      'channel': 'Click Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=F5Le0mxyMhg&t=32s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "And now, let's get started. Now, both school and circle are great for community "
              'building and course hosting, but they also differ in various ways. For example, '
              'school has a simple user-friendly interface. It has gamification features and '
              'calendar for events.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "And now, let's get started. Now, both school and circle are great for community "
             'building and course hosting, but they also differ in various ways. For example, '
             'school has a simple user-friendly interface. It has gamification features and '
             'calendar for events.',
      'title': 'Skool vs Circle (2026): The Best Online Communities & Courses? (Click Guide)',
      'url': 'https://www.youtube.com/watch?v=F5Le0mxyMhg&t=32s',
      'video_id': 'F5Le0mxyMhg'},
     {'author': 'Nathan Nazareth',
      'channel': 'Nathan Nazareth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:29](https://www.youtube.com/watch?v=dr37DaI8g3U&t=509s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "Shopify's platform is super intuitive, beautiful, easy to use, and like I said, "
              'by coming over to this landing page right here.',
      'timestamp': 509,
      'timestamp_label': '[00:08:29]',
      'timestamp_seconds': 509,
      'tip': "Shopify's platform is super intuitive, beautiful, easy to use, and like I said, "
             'by coming over to this landing page right here.',
      'title': "How to Sell AI Digital Products (beginner's guide) (Nathan Nazareth)",
      'url': 'https://www.youtube.com/watch?v=dr37DaI8g3U&t=509s',
      'video_id': 'dr37DaI8g3U'},
     {'author': 'Baddie In Business',
      'channel': 'Baddie In Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:31](https://www.youtube.com/watch?v=QopRRjoOyyg&t=691s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': "So it just really depends on like what you are doing. There's so many faceless "
              "ways to take content that doesn't really actually show your face or involve you "
              'talking that you can strategize. Another awesome platform is Pinterest.',
      'timestamp': 691,
      'timestamp_label': '[00:11:31]',
      'timestamp_seconds': 691,
      'tip': "So it just really depends on like what you are doing. There's so many faceless "
             "ways to take content that doesn't really actually show your face or involve you "
             'talking that you can strategize. Another awesome platform is Pinterest.',
      'title': 'How to Start Selling Digital Products in 2026 (STEP BY STEP) FREE COURSE '
               '(Baddie In Business)',
      'url': 'https://www.youtube.com/watch?v=QopRRjoOyyg&t=691s',
      'video_id': 'QopRRjoOyyg'},
     {'author': 'Inayah McMillan',
      'channel': 'Inayah McMillan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=ow77v1CM31k&t=416s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'Then I turn that money into assets that continue to pay me. Most people in the '
              'digital product space start with one critical mistake. They start with cheap '
              'offers hoping to upsell later.',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': 'Then I turn that money into assets that continue to pay me. Most people in the '
             'digital product space start with one critical mistake. They start with cheap '
             'offers hoping to upsell later.',
      'title': 'How I Made 10 Million Selling Digital\xa0Products (By 22) (Inayah McMillan)',
      'url': 'https://www.youtube.com/watch?v=ow77v1CM31k&t=416s',
      'video_id': 'ow77v1CM31k'},
     {'author': 'Adnan Pilditch',
      'channel': 'Adnan Pilditch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=mf1WAw0FyaI&t=156s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'And it happened to us at one point. We were leaking members fast. Turn was at '
              '17%, especially when I went to Las Vegas for the school games, I came back to '
              "high churn cuz I wasn't there in the action.",
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'And it happened to us at one point. We were leaking members fast. Turn was at '
             '17%, especially when I went to Las Vegas for the school games, I came back to '
             "high churn cuz I wasn't there in the action.",
      'title': 'Top 7 Secrets To Building a $45,000/Month Skool Community (Adnan Pilditch)',
      'url': 'https://www.youtube.com/watch?v=mf1WAw0FyaI&t=156s',
      'video_id': 'mf1WAw0FyaI'},
     {'author': 'Money Talk With Leon',
      'channel': 'Money Talk With Leon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:41](https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=341s)',
      'relevance': 'Attributed practitioner commentary on digital sales-tax nexus, '
                   'friendly-fraud chargebacks, ad fatigue, piracy, and platform concentration '
                   'risks.',
      'source_type': 'video_pro_tip',
      'text': 'PDF guide using Claude AI, and the platform I build my website on to convince '
              'people to give me their money. Say with me, give me their money. Now, for the '
              'marketing, okay?',
      'timestamp': 341,
      'timestamp_label': '[00:05:41]',
      'timestamp_seconds': 341,
      'tip': 'PDF guide using Claude AI, and the platform I build my website on to convince '
             'people to give me their money. Say with me, give me their money. Now, for the '
             'marketing, okay?',
      'title': 'I Sold Digital Products as a Beginner ‘To Prove It’s Not Luck’ Using Claude AI '
               '(Money Talk With Leon)',
      'url': 'https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=341s',
      'video_id': 'B8Z2fA5X0J4'}],
 6: [{'author': 'Alek',
      'channel': 'Alek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:04](https://www.youtube.com/watch?v=T-gfoXzz8k8&t=484s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "Etsy, it's still one of the best places to do research because you can get "
              'really good demand indicators. You can figure out how well specific product '
              'listings are selling. And so I just made a search for digital downloads.',
      'timestamp': 484,
      'timestamp_label': '[00:08:04]',
      'timestamp_seconds': 484,
      'tip': "Etsy, it's still one of the best places to do research because you can get "
             'really good demand indicators. You can figure out how well specific product '
             'listings are selling. And so I just made a search for digital downloads.',
      'title': 'Build & Sell Digital Products with A.I. (Full Course) (Alek)',
      'url': 'https://www.youtube.com/watch?v=T-gfoXzz8k8&t=484s',
      'video_id': 'T-gfoXzz8k8'},
     {'author': 'Inayah McMillan',
      'channel': 'Inayah McMillan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=ow77v1CM31k&t=139s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'Shopify store, how to run ads, how to find winning products. Still, since I was '
              'just starting, I was only making enough to cover my ad spend. This is a skill '
              'that I started learning in high school.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Shopify store, how to run ads, how to find winning products. Still, since I was '
             'just starting, I was only making enough to cover my ad spend. This is a skill '
             'that I started learning in high school.',
      'title': 'How I Made 10 Million Selling Digital\xa0Products (By 22) (Inayah McMillan)',
      'url': 'https://www.youtube.com/watch?v=ow77v1CM31k&t=139s',
      'video_id': 'ow77v1CM31k'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:26](https://www.youtube.com/watch?v=FJj3hN2KbIg&t=506s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "'s liens on GSCCA, make sure you go further in your research, check to see if "
              "the client is still alive or deceased. If they're deceased, search the "
              'obituary. You can go to the probate court, perform a search as well, and then '
              'you market.',
      'timestamp': 506,
      'timestamp_label': '[00:08:26]',
      'timestamp_seconds': 506,
      'tip': "'s liens on GSCCA, make sure you go further in your research, check to see if "
             "the client is still alive or deceased. If they're deceased, search the obituary. "
             'You can go to the probate court, perform a search as well, and then you market.',
      'title': 'How to Do Surplus Funds in Georgia (Step-by-Step Guide) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=FJj3hN2KbIg&t=506s',
      'video_id': 'FJj3hN2KbIg'},
     {'author': 'Rochelle Be',
      'channel': 'Rochelle Be',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=4e4pRrWsJvU&t=535s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'We can see conversion rates. So we know that if that product has demand, if '
              "people are searching for it, if it's got sales, if it's got good monthly "
              'revenue, the data is showing us that this could be a profitable product. And '
              'that is why we validate first with real data.',
      'timestamp': 535,
      'timestamp_label': '[00:08:55]',
      'timestamp_seconds': 535,
      'tip': 'We can see conversion rates. So we know that if that product has demand, if '
             "people are searching for it, if it's got sales, if it's got good monthly "
             'revenue, the data is showing us that this could be a profitable product. And '
             'that is why we validate first with real data.',
      'title': 'How to Start Selling Digital Products in 2026 (Step-by-Step Tutorial) '
               '(Rochelle Be)',
      'url': 'https://www.youtube.com/watch?v=4e4pRrWsJvU&t=535s',
      'video_id': '4e4pRrWsJvU'},
     {'author': 'Max Auren',
      'channel': 'Max Auren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=kmRwEjvxk-w&t=33s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'The problem is that 10 years ago, you could literally show a basic ad and print '
              'money unless you really sucked at writing copy and making an offer.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'The problem is that 10 years ago, you could literally show a basic ad and print '
             'money unless you really sucked at writing copy and making an offer.',
      'title': 'How My $7 Sales Funnel Makes Me $18k/m (Max Auren)',
      'url': 'https://www.youtube.com/watch?v=kmRwEjvxk-w&t=33s',
      'video_id': 'kmRwEjvxk-w'},
     {'author': 'Money Talk With Leon',
      'channel': 'Money Talk With Leon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=Qqjup9J9CdI&t=81s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "'re probably googling it, asking the question on Reddit or just trying to find "
              "a resolution to their problem and the issues that they're facing emotionally. "
              'Okay, so emotion is what sells PDF guides here. For example, this PDF guide '
              'right here.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "'re probably googling it, asking the question on Reddit or just trying to find a "
             "resolution to their problem and the issues that they're facing emotionally. "
             'Okay, so emotion is what sells PDF guides here. For example, this PDF guide '
             'right here.',
      'title': 'I Made $700K in 2 Days Selling Simple Digital Products (Step by Step) (Money '
               'Talk With Leon)',
      'url': 'https://www.youtube.com/watch?v=Qqjup9J9CdI&t=81s',
      'video_id': 'Qqjup9J9CdI'},
     {'author': 'Richard Yu',
      'channel': 'Richard Yu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=JpNOwmwbf2s&t=312s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "So I don't even have to record the content myself if I don't want to show my "
              "face. And Instagram's algorithm will push this video out to thousands if not "
              'millions of people for free. No ad spend, no huge following needed. And '
              "remember, you're not copying.",
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': "So I don't even have to record the content myself if I don't want to show my "
             "face. And Instagram's algorithm will push this video out to thousands if not "
             'millions of people for free. No ad spend, no huge following needed. And '
             "remember, you're not copying.",
      'title': 'I Made $27 Million Selling Simple Digital Products (Step by Step) (Richard Yu)',
      'url': 'https://www.youtube.com/watch?v=JpNOwmwbf2s&t=312s',
      'video_id': 'JpNOwmwbf2s'},
     {'author': 'Eden',
      'channel': 'Eden',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=VJ-JR7uMY34&t=216s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "A pain point in your own life that you've solved or someone else's life that "
              "you know you can help them solve. So if you've solved the problem in your life "
              'in any domain, health, wealth, relationships, happiness, those are the eternal '
              'markets where profitable problems live.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': "A pain point in your own life that you've solved or someone else's life that you "
             "know you can help them solve. So if you've solved the problem in your life in "
             'any domain, health, wealth, relationships, happiness, those are the eternal '
             'markets where profitable problems live.',
      'title': 'How To Build Your First $10,000 Digital Product (Full Beginner Guide) (Eden)',
      'url': 'https://www.youtube.com/watch?v=VJ-JR7uMY34&t=216s',
      'video_id': 'VJ-JR7uMY34'},
     {'author': 'SamCart',
      'channel': 'SamCart',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=UxhtBuVj4gY&t=97s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'And all we did was our very first thing is we had like a $50 mini course. And '
              'so if we got 100 customers, that meant something like $5,000 in revenue, right? '
              'There was a time where that was super exciting. But it was really tough to '
              'spend money on ads.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'And all we did was our very first thing is we had like a $50 mini course. And so '
             'if we got 100 customers, that meant something like $5,000 in revenue, right? '
             'There was a time where that was super exciting. But it was really tough to spend '
             'money on ads.',
      'title': 'The Complete Guide to Upsells ($8 Billion in Data) (SamCart)',
      'url': 'https://www.youtube.com/watch?v=UxhtBuVj4gY&t=97s',
      'video_id': 'UxhtBuVj4gY'},
     {'author': 'Iman Gadzhi',
      'channel': 'Iman Gadzhi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:12](https://www.youtube.com/watch?v=A-yBamfrXQs&t=672s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "Next is the variety of ad creatives. Just so you understand, when there's more "
              'variations, it usually indicates to profitability because it means that they '
              'are testing creatives and the ads are actually working.',
      'timestamp': 672,
      'timestamp_label': '[00:11:12]',
      'timestamp_seconds': 672,
      'tip': "Next is the variety of ad creatives. Just so you understand, when there's more "
             'variations, it usually indicates to profitability because it means that they are '
             'testing creatives and the ads are actually working.',
      'title': 'Copy This Method To Make $2,700/Week with Digital Products (Iman Gadzhi)',
      'url': 'https://www.youtube.com/watch?v=A-yBamfrXQs&t=672s',
      'video_id': 'A-yBamfrXQs'},
     {'author': 'Make Money with Stacy La',
      'channel': 'Make Money with Stacy La',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:13](https://www.youtube.com/watch?v=gGW2IMNOz68&t=433s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'My personal advice is to stick to one niche, topic, or specific problem to '
              'solve at first. Then, once you start getting sales and learn what works and '
              "what doesn't, you can expand to other niches as well.",
      'timestamp': 433,
      'timestamp_label': '[00:07:13]',
      'timestamp_seconds': 433,
      'tip': 'My personal advice is to stick to one niche, topic, or specific problem to solve '
             'at first. Then, once you start getting sales and learn what works and what '
             "doesn't, you can expand to other niches as well.",
      'title': 'Watch Me Create a 6 Figure Digital Product with AI in 14 Minutes | UPDATED '
               'Tutorial | Genspark (Make Money with Stacy La)',
      'url': 'https://www.youtube.com/watch?v=gGW2IMNOz68&t=433s',
      'video_id': 'gGW2IMNOz68'},
     {'author': 'Profitable Talents',
      'channel': 'Profitable Talents',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:00](https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=360s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "But of course, it's got to be uh self liquidating in a way that if you want to "
              'if I decide to run ads to this new offer and I wanted to make it extremely low '
              'ticket, I need to recoup the the ad budget somehow.',
      'timestamp': 360,
      'timestamp_label': '[00:06:00]',
      'timestamp_seconds': 360,
      'tip': "But of course, it's got to be uh self liquidating in a way that if you want to "
             'if I decide to run ads to this new offer and I wanted to make it extremely low '
             'ticket, I need to recoup the the ad budget somehow.',
      'title': 'Watch Me Build a Self-Liquidating Offer Funnel From Scratch (Ep. 1) '
               '(Profitable Talents)',
      'url': 'https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=360s',
      'video_id': '_I5YFl6Ym_k'},
     {'author': 'Richard Yu',
      'channel': 'Richard Yu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=gjffmgucDSw&t=284s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': "And I'm not talking about building a billion-dollar app with a team of "
              "engineers. I'm talking about a small micro-niche focused app that one specific "
              'problem really well. A fitness app for busy moms, a content planning app for '
              'creators, something simple.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "And I'm not talking about building a billion-dollar app with a team of "
             "engineers. I'm talking about a small micro-niche focused app that one specific "
             'problem really well. A fitness app for busy moms, a content planning app for '
             'creators, something simple.',
      'title': 'FULL COURSE: How to Build & Sell Digital Products With AI (Step by Step) '
               '(Richard Yu)',
      'url': 'https://www.youtube.com/watch?v=gjffmgucDSw&t=284s',
      'video_id': 'gjffmgucDSw'},
     {'author': 'Typedream',
      'channel': 'Typedream',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=HXQD-vJDPyU&t=90s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'For the thumbnail, let’s make it look appealing. I’m going to go to '
              'Mockupworld, which has a TON of cool mockups you can use and edit. Let’s search '
              'for an iPad mockup here, and we are going to select this one. This saves as a '
              'Photoshop (.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'For the thumbnail, let’s make it look appealing. I’m going to go to Mockupworld, '
             'which has a TON of cool mockups you can use and edit. Let’s search for an iPad '
             'mockup here, and we are going to select this one. This saves as a Photoshop (.',
      'title': 'How to make and sell aesthetic Notion templates with Typedream and Gumroad '
               '(Typedream)',
      'url': 'https://www.youtube.com/watch?v=HXQD-vJDPyU&t=90s',
      'video_id': 'HXQD-vJDPyU'},
     {'author': 'Mariana Henninger',
      'channel': 'Mariana Henninger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:31](https://www.youtube.com/watch?v=Ii70ybaGJ68&t=391s)',
      'relevance': 'Attributed practitioner commentary on Ad-Library spend velocity, '
                   'Reddit/search pain mining, pre-sale validation, and demand qualification.',
      'source_type': 'video_pro_tip',
      'text': 'So I thought that was interesting. So originally she had it at 27. AB tested '
              'that and saw that the $17 price point seemed to be Can you Is it relevant to '
              'know what her niche is, any of that or do you think that her results are '
              'pretty?',
      'timestamp': 391,
      'timestamp_label': '[00:06:31]',
      'timestamp_seconds': 391,
      'tip': 'So I thought that was interesting. So originally she had it at 27. AB tested '
             'that and saw that the $17 price point seemed to be Can you Is it relevant to '
             'know what her niche is, any of that or do you think that her results are pretty?',
      'title': 'A Low-Ticket Tiny Offer SLO Funnel Fuels High-Ticket Sales with Allie Bjerk '
               '(Mariana Henninger)',
      'url': 'https://www.youtube.com/watch?v=Ii70ybaGJ68&t=391s',
      'video_id': 'Ii70ybaGJ68'}],
 7: [{'author': 'CRM Tutorials Library',
      'channel': 'CRM Tutorials Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=pz33EMSEtfY&t=21s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "Add a new step and name it checkout page. This is the page where you'll accept "
              'orders from customers, so keep the layout clean and distraction-free. A funnel '
              'step is simply a page in your sales sequence that moves the buyer from interest '
              'to purchase.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Add a new step and name it checkout page. This is the page where you'll accept "
             'orders from customers, so keep the layout clean and distraction-free. A funnel '
             'step is simply a page in your sales sequence that moves the buyer from interest '
             'to purchase.',
      'title': 'How to Set Up Main Product, Order Bump, Upsell & Downsell in GoHighLevel | '
               'Step-by-Step (CRM Tutorials Library)',
      'url': 'https://www.youtube.com/watch?v=pz33EMSEtfY&t=21s',
      'video_id': 'pz33EMSEtfY'},
     {'author': 'LAUNCHTIP',
      'channel': 'LAUNCHTIP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=42s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'So, from here, you can choose your upsell type. Inside of the offers type, as '
              'you can see here, you have on-page offers, you have like cart upsells, you have '
              'post-purchase upsells, and you even have actions offers. So, you basically '
              'choose the one that suits your needs.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'So, from here, you can choose your upsell type. Inside of the offers type, as '
             'you can see here, you have on-page offers, you have like cart upsells, you have '
             'post-purchase upsells, and you even have actions offers. So, you basically '
             'choose the one that suits your needs.',
      'title': 'How to Create a One-Click Upsell Funnel for your Shopify store in 2026 '
               '(LAUNCHTIP)',
      'url': 'https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=42s',
      'video_id': 'k8mwfZ9Nq_c'},
     {'author': 'Typedream',
      'channel': 'Typedream',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=HXQD-vJDPyU&t=141s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'I like to edit the Checkout button so it’s less generic. Once you’re done, we '
              'hit Publish and people can go buy your template through Gumroad. Now, what you '
              'want to do is to create a website or a page that would help funnel traffic into '
              'your Gumroad page.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'I like to edit the Checkout button so it’s less generic. Once you’re done, we '
             'hit Publish and people can go buy your template through Gumroad. Now, what you '
             'want to do is to create a website or a page that would help funnel traffic into '
             'your Gumroad page.',
      'title': 'How to make and sell aesthetic Notion templates with Typedream and Gumroad '
               '(Typedream)',
      'url': 'https://www.youtube.com/watch?v=HXQD-vJDPyU&t=141s',
      'video_id': 'HXQD-vJDPyU'},
     {'author': 'Maria Wendt',
      'channel': 'Maria Wendt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:35](https://www.youtube.com/watch?v=zQQZEPMxT6U&t=815s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'If you have average, you would need about 6,000 people per month to view your '
              "page. I'm going to tell you how to get those views. If you build checkout pages "
              'the way I build checkout pages, you only need about 2,000 people to view your '
              'checkout page.',
      'timestamp': 815,
      'timestamp_label': '[00:13:35]',
      'timestamp_seconds': 815,
      'tip': 'If you have average, you would need about 6,000 people per month to view your '
             "page. I'm going to tell you how to get those views. If you build checkout pages "
             'the way I build checkout pages, you only need about 2,000 people to view your '
             'checkout page.',
      'title': 'How To Turn Your $24 Digital Product Into $24,000 (Scaling Strategy That '
               'Works) (Maria Wendt)',
      'url': 'https://www.youtube.com/watch?v=zQQZEPMxT6U&t=815s',
      'video_id': 'zQQZEPMxT6U'},
     {'author': 'Sell Your Service',
      'channel': 'Sell Your Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=_csKVgudVVY&t=137s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "But the one-time offer is then I'm going to physically show you how to set up "
              'your first ad and create it. With an ATM or an oh oh funnel. Ooh, funnel, a '
              'triple low funnel. You would then redirect them to a page with something called '
              'a one click upsell.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "But the one-time offer is then I'm going to physically show you how to set up "
             'your first ad and create it. With an ATM or an oh oh funnel. Ooh, funnel, a '
             'triple low funnel. You would then redirect them to a page with something called '
             'a one click upsell.',
      'title': 'How To Build A Self Liquidating Offer Funnel In HighLevel | Ryan Deiss (SLO) '
               '(Sell Your Service)',
      'url': 'https://www.youtube.com/watch?v=_csKVgudVVY&t=137s',
      'video_id': '_csKVgudVVY'},
     {'author': 'Marketing Mark',
      'channel': 'Marketing Mark',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=24s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "I'll have a video link down below how to set that up. Next, we're going to go "
              'ahead and add a new step. And this upsell page should go right after your '
              'checkout page.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': "I'll have a video link down below how to set that up. Next, we're going to go "
             'ahead and add a new step. And this upsell page should go right after your '
             'checkout page.',
      'title': 'How to Build 1 Click Upsells in GoHighLevel (Marketing Mark)',
      'url': 'https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=24s',
      'video_id': '0u4Tmd6BlWA'},
     {'author': 'Pete McPherson DYEB',
      'channel': 'Pete McPherson DYEB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:24](https://www.youtube.com/watch?v=wYKYVjEiqLY&t=504s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "Let's start off with my own. Here is basically what it looks like. There is a "
              'sales page and I will open it up and walk you through it in just a second. That '
              "leads to an order page. It's literally like a checkout cart. I will show you "
              'that as well in just a second.',
      'timestamp': 504,
      'timestamp_label': '[00:08:24]',
      'timestamp_seconds': 504,
      'tip': "Let's start off with my own. Here is basically what it looks like. There is a "
             'sales page and I will open it up and walk you through it in just a second. That '
             "leads to an order page. It's literally like a checkout cart. I will show you "
             'that as well in just a second.',
      'title': 'How to launch your SELF-LIQUIDATING OFFER Funnel (with real-world examples!) '
               '(Pete McPherson DYEB)',
      'url': 'https://www.youtube.com/watch?v=wYKYVjEiqLY&t=504s',
      'video_id': 'wYKYVjEiqLY'},
     {'author': 'Social Nest Marketing',
      'channel': 'Social Nest Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:36](https://www.youtube.com/watch?v=-xCVVPZu48k&t=696s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "Then I'mma go back to payments. And then we're going to edit this. So, right "
              'here, I want it to go here when people finish. Like, when you finish the '
              "checkout, it's going to go to this page, right here.",
      'timestamp': 696,
      'timestamp_label': '[00:11:36]',
      'timestamp_seconds': 696,
      'tip': "Then I'mma go back to payments. And then we're going to edit this. So, right "
             'here, I want it to go here when people finish. Like, when you finish the '
             "checkout, it's going to go to this page, right here.",
      'title': 'GoHighLevel One-Click Upsell Setup: Payment Link Redirect + Auto-Delivery '
               'Workflow (Part 6) (Social Nest Marketing)',
      'url': 'https://www.youtube.com/watch?v=-xCVVPZu48k&t=696s',
      'video_id': '-xCVVPZu48k'},
     {'author': 'Richard Yu',
      'channel': 'Richard Yu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:08](https://www.youtube.com/watch?v=kxg_sn2vJm8&t=788s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "I'm going to build the entire storefront live in front of you. A clean, simple "
              "website with a checkout that can take payments immediately, and I'm going to "
              'show you how you can build all of this in less than an afternoon with no code '
              'and no technical experience.',
      'timestamp': 788,
      'timestamp_label': '[00:13:08]',
      'timestamp_seconds': 788,
      'tip': "I'm going to build the entire storefront live in front of you. A clean, simple "
             "website with a checkout that can take payments immediately, and I'm going to "
             'show you how you can build all of this in less than an afternoon with no code '
             'and no technical experience.',
      'title': "How I'd Build a Digital Product From Scratch (After Making $32 Million) "
               '(Richard Yu)',
      'url': 'https://www.youtube.com/watch?v=kxg_sn2vJm8&t=788s',
      'video_id': 'kxg_sn2vJm8'},
     {'author': 'Skool News',
      'channel': 'Skool News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:25](https://www.youtube.com/watch?v=Oeug9IgSFXc&t=505s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'Plus a nice little pro tip. If you just link people to slash plans, they can '
              'view this page whenever. So you could have a pin post where you tell people how '
              "to do this or you could if you're DMing someone you could tell them this or if "
              "you're doing a webinar or a call.",
      'timestamp': 505,
      'timestamp_label': '[00:08:25]',
      'timestamp_seconds': 505,
      'tip': 'Plus a nice little pro tip. If you just link people to slash plans, they can '
             'view this page whenever. So you could have a pin post where you tell people how '
             "to do this or you could if you're DMing someone you could tell them this or if "
             "you're doing a webinar or a call.",
      'title': 'Membership TIERS Are Here | Skool News #33 (Skool News)',
      'url': 'https://www.youtube.com/watch?v=Oeug9IgSFXc&t=505s',
      'video_id': 'Oeug9IgSFXc'},
     {'author': 'GROUNDTECHY',
      'channel': 'GROUNDTECHY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=F73hzfI-XsE&t=273s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'They will see the second upsell and finally they will be redirected to the '
              "thank you page and it really doesn't matter what they decide on in the second "
              'upsell whether they accept the offer or decline the offer the last step for '
              'them will be the thank you page.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'They will see the second upsell and finally they will be redirected to the thank '
             "you page and it really doesn't matter what they decide on in the second upsell "
             'whether they accept the offer or decline the offer the last step for them will '
             'be the thank you page.',
      'title': 'How to Setup Sell funnel Upsells, downsells, order bumps on Systemeio '
               '(GROUNDTECHY)',
      'url': 'https://www.youtube.com/watch?v=F73hzfI-XsE&t=273s',
      'video_id': 'F73hzfI-XsE'},
     {'author': 'Nick Tsai',
      'channel': 'Nick Tsai',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=Mw5p6Dsd_y8&t=176s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': "If it makes sense right so that's the power of self-liquidating offer so if you "
              'want to learn more about how you can build your own slo you can check the link '
              'below for some free training and resources I hope you enjoyed that I will see '
              'you soon in the next video.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "If it makes sense right so that's the power of self-liquidating offer so if you "
             'want to learn more about how you can build your own slo you can check the link '
             'below for some free training and resources I hope you enjoyed that I will see '
             'you soon in the next video.',
      'title': 'What Is Self Liquidating Offer Funnel - How To Generate Leads With SLO (Nick '
               'Tsai)',
      'url': 'https://www.youtube.com/watch?v=Mw5p6Dsd_y8&t=176s',
      'video_id': 'Mw5p6Dsd_y8'},
     {'author': 'Extreme Guides',
      'channel': 'Extreme Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=2zWJQPegtuk&t=42s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'A menu will appear providing several options related to sharing your page. Once '
              'this appears, click on copy link to generate a sharable link for your notion '
              'template. This step is crucial as it allows customers to access your template '
              'directly after purchase.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'A menu will appear providing several options related to sharing your page. Once '
             'this appears, click on copy link to generate a sharable link for your notion '
             'template. This step is crucial as it allows customers to access your template '
             'directly after purchase.',
      'title': 'How to sell Notion templates on Gumroad[FULL GUIDE] (Extreme Guides)',
      'url': 'https://www.youtube.com/watch?v=2zWJQPegtuk&t=42s',
      'video_id': '2zWJQPegtuk'},
     {'author': 'Max Auren',
      'channel': 'Max Auren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=kmRwEjvxk-w&t=204s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'Only if it relates they click and go to our landing page that starts with '
              'confirmation of the promise so that they know they actually clicked on the '
              'right button. We show the tangible product picture again and very short list of '
              'features and benefits with a buy button.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': 'Only if it relates they click and go to our landing page that starts with '
             'confirmation of the promise so that they know they actually clicked on the right '
             'button. We show the tangible product picture again and very short list of '
             'features and benefits with a buy button.',
      'title': 'How My $7 Sales Funnel Makes Me $18k/m (Max Auren)',
      'url': 'https://www.youtube.com/watch?v=kmRwEjvxk-w&t=204s',
      'video_id': 'kmRwEjvxk-w'},
     {'author': 'Inayah McMillan',
      'channel': 'Inayah McMillan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=ow77v1CM31k&t=299s)',
      'relevance': 'Attributed practitioner commentary on product packaging, checkout '
                   'architecture, license/entitlement delivery, onboarding, and post-purchase '
                   'ascension.',
      'source_type': 'video_pro_tip',
      'text': 'No fancy funnel, no complex marketing, just real value delivered in a '
              'straightforward way. As we grew, we noticed something critical. Most people who '
              'purchase information struggle with implementation.',
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': 'No fancy funnel, no complex marketing, just real value delivered in a '
             'straightforward way. As we grew, we noticed something critical. Most people who '
             'purchase information struggle with implementation.',
      'title': 'How I Made 10 Million Selling Digital\xa0Products (By 22) (Inayah McMillan)',
      'url': 'https://www.youtube.com/watch?v=ow77v1CM31k&t=299s',
      'video_id': 'ow77v1CM31k'}],
 8: [{'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:58](https://www.youtube.com/watch?v=i05UCC3UvNY&t=478s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Last, decide whether you need the extras. Lemon Squeezy bundles a store and '
              'affiliate tools, and Paddle bundles billing support. And if you sell one '
              'digital product, our earlier video on Gumroad, Stan Store, and Payhip covers '
              'the all-in-one stores.',
      'timestamp': 478,
      'timestamp_label': '[00:07:58]',
      'timestamp_seconds': 478,
      'tip': 'Last, decide whether you need the extras. Lemon Squeezy bundles a store and '
             'affiliate tools, and Paddle bundles billing support. And if you sell one digital '
             'product, our earlier video on Gumroad, Stan Store, and Payhip covers the '
             'all-in-one stores.',
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=478s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'How2Genius',
      'channel': 'How2Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=181s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Fastspring also integrates with popular CRM and marketing tools, helping you '
              'automate workflows from purchase to onboarding. If your main goal is quick '
              'setup, automatic US and Canadian tax handling, and easy subscription '
              'management, Paddle is the better choice.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Fastspring also integrates with popular CRM and marketing tools, helping you '
             'automate workflows from purchase to onboarding. If your main goal is quick '
             'setup, automatic US and Canadian tax handling, and easy subscription management, '
             'Paddle is the better choice.',
      'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
               '(How2Genius)',
      'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=181s',
      'video_id': 'Y5VXhUB7aNM'},
     {'author': 'TechWealth Hub',
      'channel': 'TechWealth Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=34s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Europe, handling GST in Australia, managing chargebacks and disputes, and '
              "dealing with fraud. It's a nightmare, especially if you're a solo developer or "
              "small team. That's why services like Paddle, Gumroad, and Lemon Squeezy "
              'existed.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'Europe, handling GST in Australia, managing chargebacks and disputes, and '
             "dealing with fraud. It's a nightmare, especially if you're a solo developer or "
             "small team. That's why services like Paddle, Gumroad, and Lemon Squeezy existed.",
      'title': 'Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub)',
      'url': 'https://www.youtube.com/watch?v=KRdWGDk-GkY&t=34s',
      'video_id': 'KRdWGDk-GkY'},
     {'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=160s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'If your customers include larger companies with specific billing requirements, '
              'Paddle provides tools that support more complex payment situations. Lemon '
              'Squeezy charges the same base fee of 5% plus 50 cents.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'If your customers include larger companies with specific billing requirements, '
             'Paddle provides tools that support more complex payment situations. Lemon '
             'Squeezy charges the same base fee of 5% plus 50 cents.',
      'title': 'Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? '
               '(Tutorly)',
      'url': 'https://www.youtube.com/watch?v=IfaCBBIoVK0&t=160s',
      'video_id': 'IfaCBBIoVK0'},
     {'author': 'Click Guide',
      'channel': 'Click Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=F5Le0mxyMhg&t=83s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'The business at $199 per month, provides workflows and automations and API '
              'access. Enterprise plan comes at $419 per month, and it has advanced analytics, '
              'lower transaction fees of 1%. The plus plan comes at a custom pricing.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'The business at $199 per month, provides workflows and automations and API '
             'access. Enterprise plan comes at $419 per month, and it has advanced analytics, '
             'lower transaction fees of 1%. The plus plan comes at a custom pricing.',
      'title': 'Skool vs Circle (2026): The Best Online Communities & Courses? (Click Guide)',
      'url': 'https://www.youtube.com/watch?v=F5Le0mxyMhg&t=83s',
      'video_id': 'F5Le0mxyMhg'},
     {'author': 'Tutorials At Desk',
      'channel': 'Tutorials At Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=VEFf-FR0dxw&t=219s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Then choose your account type, usually either individual or business, depending '
              "on how you're operating. After that, follow the on-screen instructions to "
              'connect a supported payout method such as Stripe or PayPal, depending on what '
              'Gumroad offers in your region.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': 'Then choose your account type, usually either individual or business, depending '
             "on how you're operating. After that, follow the on-screen instructions to "
             'connect a supported payout method such as Stripe or PayPal, depending on what '
             'Gumroad offers in your region.',
      'title': 'How to Sell Notion Templates on Gumroad (2026 Revenue Snapshot) (Tutorials At '
               'Desk)',
      'url': 'https://www.youtube.com/watch?v=VEFf-FR0dxw&t=219s',
      'video_id': 'VEFf-FR0dxw'},
     {'author': 'Stephen S.',
      'channel': 'Stephen S.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=55s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Now if I come down here to the MCP servers, I can see that the Stripe MCP is '
              "there. And for this, I'm going to authorize, jump back into Curo, and now I can "
              'see that I have access to all of these tools.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Now if I come down here to the MCP servers, I can see that the Stripe MCP is '
             "there. And for this, I'm going to authorize, jump back into Curo, and now I can "
             'see that I have access to all of these tools.',
      'title': "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an "
               'Existing App  #mcp (Stephen S.)',
      'url': 'https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=55s',
      'video_id': 'F-WZgXuQIuQ'},
     {'author': 'Doug Boughton',
      'channel': 'Doug Boughton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:29](https://www.youtube.com/watch?v=8lz_gy-Osw8&t=749s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': "Um and I've built a tool around this. It's called Event Stack AI. Uh I sell "
              'this tool for up to $299 a month for the highest plan. My clients get it for '
              'free.',
      'timestamp': 749,
      'timestamp_label': '[00:12:29]',
      'timestamp_seconds': 749,
      'tip': "Um and I've built a tool around this. It's called Event Stack AI. Uh I sell this "
             'tool for up to $299 a month for the highest plan. My clients get it for free.',
      'title': 'Are Free Skool Communities Dying? Why I Turned Mine Paid (Doug Boughton)',
      'url': 'https://www.youtube.com/watch?v=8lz_gy-Osw8&t=749s',
      'video_id': '8lz_gy-Osw8'},
     {'author': 'Captain Vova (Vova Feldman)',
      'channel': 'Captain Vova (Vova Feldman)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=109s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': "Whether you've been following the events or not, last year Stripe acquired "
              'payment solution called Lemon Squeezy, a Merchant of Record actually. And the '
              'question that is kind of inevitable is are they going to sunset that solution?',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "Whether you've been following the events or not, last year Stripe acquired "
             'payment solution called Lemon Squeezy, a Merchant of Record actually. And the '
             'question that is kind of inevitable is are they going to sunset that solution?',
      'title': 'Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain '
               'Vova (Vova Feldman))',
      'url': 'https://www.youtube.com/watch?v=5zGuxRrg_O0&t=109s',
      'video_id': '5zGuxRrg_O0'},
     {'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=162s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Lemon Squeezy is designed for simplicity. The UI is clean, modern, and '
              'genuinely easy to navigate. Setup takes 15 to 30 minutes. They have built-in '
              'email marketing, affiliate management, and a no code storefront builder.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Lemon Squeezy is designed for simplicity. The UI is clean, modern, and genuinely '
             'easy to navigate. Setup takes 15 to 30 minutes. They have built-in email '
             'marketing, affiliate management, and a no code storefront builder.',
      'title': 'Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech)',
      'url': 'https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=162s',
      'video_id': 'Qq-EyvVj7IM'},
     {'author': 'Bree and Steve',
      'channel': 'Bree and Steve',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:32](https://www.youtube.com/watch?v=zmw7OXf39rQ&t=332s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': "So I'm going to hit new database and I'm going to go ahead and resize this so "
              "we're gonna go in and do is add the different habits that you would like to "
              "track so this can be really anything I'm just gonna go ahead and list a couple "
              'of random ones.',
      'timestamp': 332,
      'timestamp_label': '[00:05:32]',
      'timestamp_seconds': 332,
      'tip': "So I'm going to hit new database and I'm going to go ahead and resize this so "
             "we're gonna go in and do is add the different habits that you would like to "
             "track so this can be really anything I'm just gonna go ahead and list a couple "
             'of random ones.',
      'title': 'How To Make & Sell Notion Templates (Make $1000+ MONTH!) (Bree and Steve)',
      'url': 'https://www.youtube.com/watch?v=zmw7OXf39rQ&t=332s',
      'video_id': 'zmw7OXf39rQ'},
     {'author': 'Pete McPherson DYEB',
      'channel': 'Pete McPherson DYEB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:59](https://www.youtube.com/watch?v=wYKYVjEiqLY&t=1139s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'This is a tool that you can use ASAP. Next to go through a bump offer and then '
              'an upsell. It could be the systems and strategies that are related to the '
              "tools. And actually, this is an important point that I didn't mention earlier.",
      'timestamp': 1139,
      'timestamp_label': '[00:18:59]',
      'timestamp_seconds': 1139,
      'tip': 'This is a tool that you can use ASAP. Next to go through a bump offer and then '
             'an upsell. It could be the systems and strategies that are related to the tools. '
             "And actually, this is an important point that I didn't mention earlier.",
      'title': 'How to launch your SELF-LIQUIDATING OFFER Funnel (with real-world examples!) '
               '(Pete McPherson DYEB)',
      'url': 'https://www.youtube.com/watch?v=wYKYVjEiqLY&t=1139s',
      'video_id': 'wYKYVjEiqLY'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=FJj3hN2KbIg&t=165s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'You guys can see here, just a very basic Google search can give us access to '
              'many counties across the entire state of Georgia. We can also use Excess Elite. '
              'Excess Elite is the number one leading database provider. They also have a CRM '
              'that allows you to market.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'You guys can see here, just a very basic Google search can give us access to '
             'many counties across the entire state of Georgia. We can also use Excess Elite. '
             'Excess Elite is the number one leading database provider. They also have a CRM '
             'that allows you to market.',
      'title': 'How to Do Surplus Funds in Georgia (Step-by-Step Guide) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=FJj3hN2KbIg&t=165s',
      'video_id': 'FJj3hN2KbIg'},
     {'author': 'Framer',
      'channel': 'Framer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=RN0VWAvL-qc&t=223s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'Twitter or share it anywhere you want so you can copy this share it wherever '
              'you want and then that is how you start selling your templates through lemon '
              'squeezy thanks for watching.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'Twitter or share it anywhere you want so you can copy this share it wherever you '
             'want and then that is how you start selling your templates through lemon squeezy '
             'thanks for watching.',
      'title': 'How to start selling your Framer templates through Lemon Squeezy (Framer)',
      'url': 'https://www.youtube.com/watch?v=RN0VWAvL-qc&t=223s',
      'video_id': 'RN0VWAvL-qc'},
     {'author': 'ScottishArchivesTV',
      'channel': 'ScottishArchivesTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=307s)',
      'relevance': 'Attributed practitioner commentary on analytics, first-party attribution '
                   'pixels, email/co-reg engines, Chrome micro-tools, and GEO citation '
                   'visibility.',
      'source_type': 'video_pro_tip',
      'text': 'You to run a manual scan make sure that manual only is selected under schedule '
              'the scan if you set up an email address to send your reports to you can enter '
              'it now by clicking add report recipient email entering your email address and '
              'clicking add.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'You to run a manual scan make sure that manual only is selected under schedule '
             'the scan if you set up an email address to send your reports to you can enter it '
             'now by clicking add report recipient email entering your email address and '
             'clicking add.',
      'title': 'Getting Started with Digital Preservation: Fixity Pro (ScottishArchivesTV)',
      'url': 'https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=307s',
      'video_id': '1pRY7lpZ7nA'}],
 9: [{'author': 'Captain Vova (Vova Feldman)',
      'channel': 'Captain Vova (Vova Feldman)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=5zGuxRrg_O0&t=60s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
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
     {'author': 'houdztech',
      'channel': 'houdztech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=31s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'They handle global tax compliance in 100 plus countries, collect sales tax, '
              "VAT, GST, and file it for you. You don't touch any of that complexity. Lemon "
              "Squeezy was acquired by Stripe in 2024, so it's now backed by Stripe's "
              'infrastructure, which is massive.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'They handle global tax compliance in 100 plus countries, collect sales tax, VAT, '
             "GST, and file it for you. You don't touch any of that complexity. Lemon Squeezy "
             "was acquired by Stripe in 2024, so it's now backed by Stripe's infrastructure, "
             'which is massive.',
      'title': 'Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech)',
      'url': 'https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=31s',
      'video_id': 'Qq-EyvVj7IM'},
     {'author': 'How2Genius',
      'channel': 'How2Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=113s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'Like Paddle, Fastring manages payments, subscriptions, and tax compliance. It '
              'automatically calculates and remits US and Canadian sales tax plus VAT and GST '
              'for international sales. This reduces risk and administrative overhead for '
              'digital sellers.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'Like Paddle, Fastring manages payments, subscriptions, and tax compliance. It '
             'automatically calculates and remits US and Canadian sales tax plus VAT and GST '
             'for international sales. This reduces risk and administrative overhead for '
             'digital sellers.',
      'title': 'NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products '
               '(How2Genius)',
      'url': 'https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=113s',
      'video_id': 'Y5VXhUB7aNM'},
     {'author': 'SoloBuild',
      'channel': 'SoloBuild',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:49](https://www.youtube.com/watch?v=i05UCC3UvNY&t=469s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "If it's spread across countries, a merchant of record starts to earn its fee. "
              "Next, decide how much tax paperwork you'll own. Last, decide whether you need "
              'the extras. Lemon Squeezy bundles a store and affiliate tools, and Paddle '
              'bundles billing support.',
      'timestamp': 469,
      'timestamp_label': '[00:07:49]',
      'timestamp_seconds': 469,
      'tip': "If it's spread across countries, a merchant of record starts to earn its fee. "
             "Next, decide how much tax paperwork you'll own. Last, decide whether you need "
             'the extras. Lemon Squeezy bundles a store and affiliate tools, and Paddle '
             'bundles billing support.',
      'title': 'Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild)',
      'url': 'https://www.youtube.com/watch?v=i05UCC3UvNY&t=469s',
      'video_id': 'i05UCC3UvNY'},
     {'author': 'Tutorly',
      'channel': 'Tutorly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=IfaCBBIoVK0&t=90s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
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
     {'author': 'Pam Obasa',
      'channel': 'Pam Obasa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=Kgj8rFDeRIs&t=320s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'It will have the button and once they click this button they move forward and '
              'over here this is what we call your minimum viable sales.',
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'It will have the button and once they click this button they move forward and '
             'over here this is what we call your minimum viable sales.',
      'title': 'How To Create A Self-liquidating Offer Funnel For Your Business (Pam Obasa)',
      'url': 'https://www.youtube.com/watch?v=Kgj8rFDeRIs&t=320s',
      'video_id': 'Kgj8rFDeRIs'},
     {'author': 'HelperMan',
      'channel': 'HelperMan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=IA4eosnOzIE&t=81s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'First, fees can feel higher compared to using a standard payment processor '
              "directly because you're paying for the extra tax and compliance handling.",
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'First, fees can feel higher compared to using a standard payment processor '
             "directly because you're paying for the extra tax and compliance handling.",
      'title': 'Lemon Squeezy for Merchant of Record Honest Review - Watch Before Using '
               '(HelperMan)',
      'url': 'https://www.youtube.com/watch?v=IA4eosnOzIE&t=81s',
      'video_id': 'IA4eosnOzIE'},
     {'author': 'Zero to Launch',
      'channel': 'Zero to Launch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=u9nHXAMBUe4&t=71s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "I'm not changing anything here. To add an upsell, you click add step. You give "
              'it a name and open type. Upsell is in this list, and so is downsell, which can '
              "come after an upsell if they say no. I'm not making another one, so I'll click "
              'cancel.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "I'm not changing anything here. To add an upsell, you click add step. You give "
             'it a name and open type. Upsell is in this list, and so is downsell, which can '
             "come after an upsell if they say no. I'm not making another one, so I'll click "
             'cancel.',
      'title': 'Order Bump or Upsell in Systeme.io: Which Should You Add First? (Zero to '
               'Launch)',
      'url': 'https://www.youtube.com/watch?v=u9nHXAMBUe4&t=71s',
      'video_id': 'u9nHXAMBUe4'},
     {'author': 'TechWealth Hub',
      'channel': 'TechWealth Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=KRdWGDk-GkY&t=73s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'Stripe now handles as your merchant of record. First, global indirect tax, '
              'sales tax, that GST, all of it. Stripe calculates it, collects it, files it, '
              'and remits it. Stripes already best in class at this, but now they are taking '
              'on the liability.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'Stripe now handles as your merchant of record. First, global indirect tax, sales '
             'tax, that GST, all of it. Stripe calculates it, collects it, files it, and '
             'remits it. Stripes already best in class at this, but now they are taking on the '
             'liability.',
      'title': 'Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub)',
      'url': 'https://www.youtube.com/watch?v=KRdWGDk-GkY&t=73s',
      'video_id': 'KRdWGDk-GkY'},
     {'author': 'Money Talk With Leon',
      'channel': 'Money Talk With Leon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:42](https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=582s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': '" Instead of that whole YouTuber research process, which YouTuber would do '
              'affiliate only? Which YouTuber should I Instead of doing all that myself '
              'manually, I said, "Hmm, >> [clears throat] >> there has to be a way to do all '
              'of this with just the click of a button."',
      'timestamp': 582,
      'timestamp_label': '[00:09:42]',
      'timestamp_seconds': 582,
      'tip': '" Instead of that whole YouTuber research process, which YouTuber would do '
             'affiliate only? Which YouTuber should I Instead of doing all that myself '
             'manually, I said, "Hmm, >> [clears throat] >> there has to be a way to do all of '
             'this with just the click of a button."',
      'title': 'I Sold Digital Products as a Beginner ‘To Prove It’s Not Luck’ Using Claude AI '
               '(Money Talk With Leon)',
      'url': 'https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=582s',
      'video_id': 'B8Z2fA5X0J4'},
     {'author': 'CRM Tutorials Library',
      'channel': 'CRM Tutorials Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=pz33EMSEtfY&t=25s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "This is the page where you'll accept orders from customers, so keep the layout "
              'clean and distraction-free. A funnel step is simply a page in your sales '
              'sequence that moves the buyer from interest to purchase. Open the step and '
              'click edit.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "This is the page where you'll accept orders from customers, so keep the layout "
             'clean and distraction-free. A funnel step is simply a page in your sales '
             'sequence that moves the buyer from interest to purchase. Open the step and click '
             'edit.',
      'title': 'How to Set Up Main Product, Order Bump, Upsell & Downsell in GoHighLevel | '
               'Step-by-Step (CRM Tutorials Library)',
      'url': 'https://www.youtube.com/watch?v=pz33EMSEtfY&t=25s',
      'video_id': 'pz33EMSEtfY'},
     {'author': 'Baddie In Business',
      'channel': 'Baddie In Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:01](https://www.youtube.com/watch?v=D237D2sGBRs&t=1081s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "Done with this you're going to just come up over here and click share and then "
              "we're going to just click download and you want to change this to a PDF "
              'standard and just click.',
      'timestamp': 1081,
      'timestamp_label': '[00:18:01]',
      'timestamp_seconds': 1081,
      'tip': "Done with this you're going to just come up over here and click share and then "
             "we're going to just click download and you want to change this to a PDF standard "
             'and just click.',
      'title': 'How to Start Selling Digital Products (STEP BY STEP) FREE COURSE (Baddie In '
               'Business)',
      'url': 'https://www.youtube.com/watch?v=D237D2sGBRs&t=1081s',
      'video_id': 'D237D2sGBRs'},
     {'author': 'Stephen S.',
      'channel': 'Stephen S.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=178s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "So that's what we needed for manage payments in the merchant of record and "
              "let's jump over to the application after setting the environment variable. When "
              'I go back to the app now if I click on one of these plans.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': "So that's what we needed for manage payments in the merchant of record and let's "
             'jump over to the application after setting the environment variable. When I go '
             'back to the app now if I click on one of these plans.',
      'title': "Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an "
               'Existing App  #mcp (Stephen S.)',
      'url': 'https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=178s',
      'video_id': 'F-WZgXuQIuQ'},
     {'author': 'LAUNCHTIP',
      'channel': 'LAUNCHTIP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=30s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': "SellUp and Upsell Add Ons and make sure it's enabled. Once you do so, you can "
              'just go and start creating your one-click upsell funnel. So, from here, you can '
              'choose your upsell type.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "SellUp and Upsell Add Ons and make sure it's enabled. Once you do so, you can "
             'just go and start creating your one-click upsell funnel. So, from here, you can '
             'choose your upsell type.',
      'title': 'How to Create a One-Click Upsell Funnel for your Shopify store in 2026 '
               '(LAUNCHTIP)',
      'url': 'https://www.youtube.com/watch?v=k8mwfZ9Nq_c&t=30s',
      'video_id': 'k8mwfZ9Nq_c'},
     {'author': 'Sell Your Service',
      'channel': 'Sell Your Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=_csKVgudVVY&t=207s)',
      'relevance': 'Attributed practitioner commentary on FTC ROSCA click-to-cancel rules, '
                   'clear refund terms, affiliate disclosures, VAT/sales tax, and DMCA '
                   'enforcement.',
      'source_type': 'video_pro_tip',
      'text': 'And what you say in this video is I will give you 100% of all sales if you sign '
              'up as an affiliate, for lack of a better term.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': 'And what you say in this video is I will give you 100% of all sales if you sign '
             'up as an affiliate, for lack of a better term.',
      'title': 'How To Build A Self Liquidating Offer Funnel In HighLevel | Ryan Deiss (SLO) '
               '(Sell Your Service)',
      'url': 'https://www.youtube.com/watch?v=_csKVgudVVY&t=207s',
      'video_id': '_csKVgudVVY'}],
 10: [{'author': 'Maik Kleinert | Content-to-Conversion Systems',
       'channel': 'Maik Kleinert | Content-to-Conversion Systems',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=101s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'Basically, here on our channel, we have the comment trigger family, so people '
               'commenting family and then the DM automation gets triggered. You have seen '
               'this probably around all the platforms.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'Basically, here on our channel, we have the comment trigger family, so people '
              'commenting family and then the DM automation gets triggered. You have seen this '
              'probably around all the platforms.',
       'title': 'I Upsold A $7 Product To $57  With DM Automation + Order Bump Setup ( Full '
                'System Explained ) (Maik Kleinert | Content-to-Conversion Systems)',
       'url': 'https://www.youtube.com/watch?v=pE2Z7vTYfSw&t=101s',
       'video_id': 'pE2Z7vTYfSw'},
      {'author': 'Adnan Pilditch',
       'channel': 'Adnan Pilditch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:55](https://www.youtube.com/watch?v=mf1WAw0FyaI&t=415s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "That's when leveraging School changed everything because you have chat, "
               "courses, calendar, leaderboards all in one place. You've got clean UX, members "
               'actually use it. No more Frankensteining Discord, Kajabi, Zoom, email tools, '
               'and support threads, etc.',
       'timestamp': 415,
       'timestamp_label': '[00:06:55]',
       'timestamp_seconds': 415,
       'tip': "That's when leveraging School changed everything because you have chat, "
              "courses, calendar, leaderboards all in one place. You've got clean UX, members "
              'actually use it. No more Frankensteining Discord, Kajabi, Zoom, email tools, '
              'and support threads, etc.',
       'title': 'Top 7 Secrets To Building a $45,000/Month Skool Community (Adnan Pilditch)',
       'url': 'https://www.youtube.com/watch?v=mf1WAw0FyaI&t=415s',
       'video_id': 'mf1WAw0FyaI'},
      {'author': 'Money Talk With Leon',
       'channel': 'Money Talk With Leon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:20](https://www.youtube.com/watch?v=B8Z2fA5X0J4&t=560s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
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
      {'author': 'Nathan Nazareth',
       'channel': 'Nathan Nazareth',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:59](https://www.youtube.com/watch?v=6cm2o8zzuNw&t=1199s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'I would strongly recommend posting short form every single day if you can. If '
               "you're playing the long game, one searchable YouTube video every single week "
               'in your niche works, too. Remember, evergreen content beats viral in this '
               'business every single time.',
       'timestamp': 1199,
       'timestamp_label': '[00:19:59]',
       'timestamp_seconds': 1199,
       'tip': 'I would strongly recommend posting short form every single day if you can. If '
              "you're playing the long game, one searchable YouTube video every single week in "
              'your niche works, too. Remember, evergreen content beats viral in this business '
              'every single time.',
       'title': 'How to build & sell AI Digital Products (2026 full guide) (Nathan Nazareth)',
       'url': 'https://www.youtube.com/watch?v=6cm2o8zzuNw&t=1199s',
       'video_id': '6cm2o8zzuNw'},
      {'author': 'Make Money with Stacy La',
       'channel': 'Make Money with Stacy La',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:28](https://www.youtube.com/watch?v=gGW2IMNOz68&t=328s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'From here, all you have to do is choose which tool or agent you want to use '
               'from the menu below the chat, or in the side menu right here.',
       'timestamp': 328,
       'timestamp_label': '[00:05:28]',
       'timestamp_seconds': 328,
       'tip': 'From here, all you have to do is choose which tool or agent you want to use '
              'from the menu below the chat, or in the side menu right here.',
       'title': 'Watch Me Create a 6 Figure Digital Product with AI in 14 Minutes | UPDATED '
                'Tutorial | Genspark (Make Money with Stacy La)',
       'url': 'https://www.youtube.com/watch?v=gGW2IMNOz68&t=328s',
       'video_id': 'gGW2IMNOz68'},
      {'author': 'Baddie In Business',
       'channel': 'Baddie In Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:59](https://www.youtube.com/watch?v=QopRRjoOyyg&t=539s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'Now you do need to install an app to automate your digital product. So when '
               'you make a sale, that ebook will get sent straight to your customer in the '
               'email. Go to apps on your Shopify dashboard.',
       'timestamp': 539,
       'timestamp_label': '[00:08:59]',
       'timestamp_seconds': 539,
       'tip': 'Now you do need to install an app to automate your digital product. So when you '
              'make a sale, that ebook will get sent straight to your customer in the email. '
              'Go to apps on your Shopify dashboard.',
       'title': 'How to Start Selling Digital Products in 2026 (STEP BY STEP) FREE COURSE '
                '(Baddie In Business)',
       'url': 'https://www.youtube.com/watch?v=QopRRjoOyyg&t=539s',
       'video_id': 'QopRRjoOyyg'},
      {'author': 'Iman Gadzhi',
       'channel': 'Iman Gadzhi',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:29](https://www.youtube.com/watch?v=A-yBamfrXQs&t=2069s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "And I'll give you a perfect example. There's this YouTube channel called "
               "Business Basics. It's a channel I've been following for a while. They're "
               'completely faceless.',
       'timestamp': 2069,
       'timestamp_label': '[00:34:29]',
       'timestamp_seconds': 2069,
       'tip': "And I'll give you a perfect example. There's this YouTube channel called "
              "Business Basics. It's a channel I've been following for a while. They're "
              'completely faceless.',
       'title': 'Copy This Method To Make $2,700/Week with Digital Products (Iman Gadzhi)',
       'url': 'https://www.youtube.com/watch?v=A-yBamfrXQs&t=2069s',
       'video_id': 'A-yBamfrXQs'},
      {'author': 'Funnel Building Secrets',
       'channel': 'Funnel Building Secrets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=BZ4rml1tc1U&t=96s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "Click on the product settings to link your upsell product. Make sure you've "
               "added the product in your funnel's products tab so it can be selected here. "
               'Step seven, test everything. Finally, test your funnel to make sure your order '
               'bump and upsell flow smoothly.',
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': "Click on the product settings to link your upsell product. Make sure you've "
              "added the product in your funnel's products tab so it can be selected here. "
              'Step seven, test everything. Finally, test your funnel to make sure your order '
              'bump and upsell flow smoothly.',
       'title': 'How to Set Up an Order Bump and Upsell (Funnel Building Secrets)',
       'url': 'https://www.youtube.com/watch?v=BZ4rml1tc1U&t=96s',
       'video_id': 'BZ4rml1tc1U'},
      {'author': 'Center for Community Progress',
       'channel': 'Center for Community Progress',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:50:21](https://www.youtube.com/watch?v=DG4Uhckk-fU&t=3021s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'Uh the question says, "I\'m curious since even with resolved ownership, uh '
               'what ongoing support to maintain the property and avoiding slipping back to '
               'being a distressed property again?" This is an excellent question and Monica, '
               'thank you for raising that one from the chat.',
       'timestamp': 3021,
       'timestamp_label': '[00:50:21]',
       'timestamp_seconds': 3021,
       'tip': 'Uh the question says, "I\'m curious since even with resolved ownership, uh what '
              'ongoing support to maintain the property and avoiding slipping back to being a '
              'distressed property again?" This is an excellent question and Monica, thank you '
              'for raising that one from the chat.',
       'title': "Heirs' Property 101 (Center for Community Progress)",
       'url': 'https://www.youtube.com/watch?v=DG4Uhckk-fU&t=3021s',
       'video_id': 'DG4Uhckk-fU'},
      {'author': 'Richard Yu',
       'channel': 'Richard Yu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:34](https://www.youtube.com/watch?v=gjffmgucDSw&t=2254s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "But here's where AI changes everything about producing these. If you go the "
               'faceless route, you can either still record yourself but just put a blur of '
               'your face like what Lola does, or you can actually build an AI clone.',
       'timestamp': 2254,
       'timestamp_label': '[00:37:34]',
       'timestamp_seconds': 2254,
       'tip': "But here's where AI changes everything about producing these. If you go the "
              'faceless route, you can either still record yourself but just put a blur of '
              'your face like what Lola does, or you can actually build an AI clone.',
       'title': 'FULL COURSE: How to Build & Sell Digital Products With AI (Step by Step) '
                '(Richard Yu)',
       'url': 'https://www.youtube.com/watch?v=gjffmgucDSw&t=2254s',
       'video_id': 'gjffmgucDSw'},
      {'author': 'Zero to Launch',
       'channel': 'Zero to Launch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:41](https://www.youtube.com/watch?v=u9nHXAMBUe4&t=221s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'Everyone who buys the bump gets that tag, and the help pages suggest using it '
               'in an automation rule to email them. Making a rule is in how to create an '
               'automation rule in system. Click the plus, then one-time payment, and create a '
               'new one.',
       'timestamp': 221,
       'timestamp_label': '[00:03:41]',
       'timestamp_seconds': 221,
       'tip': 'Everyone who buys the bump gets that tag, and the help pages suggest using it '
              'in an automation rule to email them. Making a rule is in how to create an '
              'automation rule in system. Click the plus, then one-time payment, and create a '
              'new one.',
       'title': 'Order Bump or Upsell in Systeme.io: Which Should You Add First? (Zero to '
                'Launch)',
       'url': 'https://www.youtube.com/watch?v=u9nHXAMBUe4&t=221s',
       'video_id': 'u9nHXAMBUe4'},
      {'author': 'Max Auren',
       'channel': 'Max Auren',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:22](https://www.youtube.com/watch?v=kmRwEjvxk-w&t=562s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'But if you still want to go on your own, watch this video where I talk about '
               'the email sequence that actually drives the sales for me after we get someone '
               "through today's funnel.",
       'timestamp': 562,
       'timestamp_label': '[00:09:22]',
       'timestamp_seconds': 562,
       'tip': 'But if you still want to go on your own, watch this video where I talk about '
              'the email sequence that actually drives the sales for me after we get someone '
              "through today's funnel.",
       'title': 'How My $7 Sales Funnel Makes Me $18k/m (Max Auren)',
       'url': 'https://www.youtube.com/watch?v=kmRwEjvxk-w&t=562s',
       'video_id': 'kmRwEjvxk-w'},
      {'author': 'Smart Capital',
       'channel': 'Smart Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:33:33](https://www.youtube.com/watch?v=GmI0MYeyMg0&t=2013s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': 'On screen now, you can see the same finance tracker on a phone screen, with '
               'the mobile view stacked vertically, the key cards at the top and the '
               'transaction table simplified. If your template only looks good on a wide '
               'desktop screen, test it on mobile before launch.',
       'timestamp': 2013,
       'timestamp_label': '[00:33:33]',
       'timestamp_seconds': 2013,
       'tip': 'On screen now, you can see the same finance tracker on a phone screen, with the '
              'mobile view stacked vertically, the key cards at the top and the transaction '
              'table simplified. If your template only looks good on a wide desktop screen, '
              'test it on mobile before launch.',
       'title': 'Sell Notion Templates on Gumroad: What a $29 Sale Really Keeps (2026) (Smart '
                'Capital)',
       'url': 'https://www.youtube.com/watch?v=GmI0MYeyMg0&t=2013s',
       'video_id': 'GmI0MYeyMg0'},
      {'author': 'Pete McPherson DYEB',
       'channel': 'Pete McPherson DYEB',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:02](https://www.youtube.com/watch?v=wYKYVjEiqLY&t=542s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "And they also go into an email sequence, but that's for a later date. And then "
               "I run paid traffic to the sales page. I've also promoted it organically via my "
               'email list and I just, you know, link to it from blog post. I promote it '
               'organically and paid.',
       'timestamp': 542,
       'timestamp_label': '[00:09:02]',
       'timestamp_seconds': 542,
       'tip': "And they also go into an email sequence, but that's for a later date. And then "
              "I run paid traffic to the sales page. I've also promoted it organically via my "
              'email list and I just, you know, link to it from blog post. I promote it '
              'organically and paid.',
       'title': 'How to launch your SELF-LIQUIDATING OFFER Funnel (with real-world examples!) '
                '(Pete McPherson DYEB)',
       'url': 'https://www.youtube.com/watch?v=wYKYVjEiqLY&t=542s',
       'video_id': 'wYKYVjEiqLY'},
      {'author': 'Money Talk With Leon',
       'channel': 'Money Talk With Leon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:02](https://www.youtube.com/watch?v=Qqjup9J9CdI&t=362s)',
       'relevance': 'Attributed practitioner commentary on comment-to-DM triggers, '
                    'quiz/Web2App bridges, faceless YouTube tutorials, and AI customer-support '
                    'workflows.',
       'source_type': 'video_pro_tip',
       'text': "So that's why the message is not formal. But like I said, there's another "
               "message I used to send to people I don't know, creators I don't know. So "
               "anyway, it's a PDF guide that fits your mom faceless YouTube channel "
               'perfectly.',
       'timestamp': 362,
       'timestamp_label': '[00:06:02]',
       'timestamp_seconds': 362,
       'tip': "So that's why the message is not formal. But like I said, there's another "
              "message I used to send to people I don't know, creators I don't know. So "
              "anyway, it's a PDF guide that fits your mom faceless YouTube channel perfectly.",
       'title': 'I Made $700K in 2 Days Selling Simple Digital Products (Step by Step) (Money '
                'Talk With Leon)',
       'url': 'https://www.youtube.com/watch?v=Qqjup9J9CdI&t=362s',
       'video_id': 'Qqjup9J9CdI'}],
 11: [{'author': 'Profitable Talents',
       'channel': 'Profitable Talents',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:32](https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=872s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "'s sustainable and you and the way you can present the offer as well and how "
               "you can scale it without scaling the overwhelm. Uh it's a bit too complex for "
               'a um front-end offer.',
       'timestamp': 872,
       'timestamp_label': '[00:14:32]',
       'timestamp_seconds': 872,
       'tip': "'s sustainable and you and the way you can present the offer as well and how "
              "you can scale it without scaling the overwhelm. Uh it's a bit too complex for a "
              'um front-end offer.',
       'title': 'Watch Me Build a Self-Liquidating Offer Funnel From Scratch (Ep. 1) '
                '(Profitable Talents)',
       'url': 'https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=872s',
       'video_id': '_I5YFl6Ym_k'},
      {'author': 'Maria Wendt',
       'channel': 'Maria Wendt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:33](https://www.youtube.com/watch?v=zQQZEPMxT6U&t=33s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "And so basically what I'm going to do is show you how to scale a cheap $24 "
               "product into essentially a thousandx that per month. I've done that not just "
               'for me but for a ton of ton of students in all different kinds of industries.',
       'timestamp': 33,
       'timestamp_label': '[00:00:33]',
       'timestamp_seconds': 33,
       'tip': "And so basically what I'm going to do is show you how to scale a cheap $24 "
              "product into essentially a thousandx that per month. I've done that not just "
              'for me but for a ton of ton of students in all different kinds of industries.',
       'title': 'How To Turn Your $24 Digital Product Into $24,000 (Scaling Strategy That '
                'Works) (Maria Wendt)',
       'url': 'https://www.youtube.com/watch?v=zQQZEPMxT6U&t=33s',
       'video_id': 'zQQZEPMxT6U'},
      {'author': 'Baddie In Business',
       'channel': 'Baddie In Business',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:31](https://www.youtube.com/watch?v=QopRRjoOyyg&t=631s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'I always recommend three and above. You can click generate and then it will '
               'generate you carousels that you can use for your social media pages.',
       'timestamp': 631,
       'timestamp_label': '[00:10:31]',
       'timestamp_seconds': 631,
       'tip': 'I always recommend three and above. You can click generate and then it will '
              'generate you carousels that you can use for your social media pages.',
       'title': 'How to Start Selling Digital Products in 2026 (STEP BY STEP) FREE COURSE '
                '(Baddie In Business)',
       'url': 'https://www.youtube.com/watch?v=QopRRjoOyyg&t=631s',
       'video_id': 'QopRRjoOyyg'},
      {'author': 'Side Hustle Mastery',
       'channel': 'Side Hustle Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=127s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'Now, what this basically is is that this serves as a personal dashboard for my '
               'company, which is basically uh where I go to run most of the day-to-day '
               'operations inside of my business.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': 'Now, what this basically is is that this serves as a personal dashboard for my '
              'company, which is basically uh where I go to run most of the day-to-day '
              'operations inside of my business.',
       'title': 'How to Make Money Selling Notion Templates [Gumroad Step-by-Step] (Side '
                'Hustle Mastery)',
       'url': 'https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=127s',
       'video_id': '2j9bt8ET3Ec'},
      {'author': 'Mariana Henninger',
       'channel': 'Mariana Henninger',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=Ii70ybaGJ68&t=283s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'There was another update called the Andromeda update like a couple weeks ago '
               "that changed a lot of things too. So it's a lot more about having for her it "
               'was having multiple adsets instead of just trying to scale within one adset.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': 'There was another update called the Andromeda update like a couple weeks ago '
              "that changed a lot of things too. So it's a lot more about having for her it "
              'was having multiple adsets instead of just trying to scale within one adset.',
       'title': 'A Low-Ticket Tiny Offer SLO Funnel Fuels High-Ticket Sales with Allie Bjerk '
                '(Mariana Henninger)',
       'url': 'https://www.youtube.com/watch?v=Ii70ybaGJ68&t=283s',
       'video_id': 'Ii70ybaGJ68'},
      {'author': 'Tatyana Savage',
       'channel': 'Tatyana Savage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:09](https://www.youtube.com/watch?v=TGNTFquVxZU&t=849s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "Pinterest in order to generate traffic and get sales. I don't post anywhere on "
               "social media, and I don't use paid ads.",
       'timestamp': 849,
       'timestamp_label': '[00:14:09]',
       'timestamp_seconds': 849,
       'tip': "Pinterest in order to generate traffic and get sales. I don't post anywhere on "
              "social media, and I don't use paid ads.",
       'title': 'How to Start a Digital Product Business (& ACTUALLY Make Money) (Tatyana '
                'Savage)',
       'url': 'https://www.youtube.com/watch?v=TGNTFquVxZU&t=849s',
       'video_id': 'TGNTFquVxZU'},
      {'author': 'Inayah McMillan',
       'channel': 'Inayah McMillan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=ow77v1CM31k&t=168s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'The thought of spending thousands per month on rent was extremely '
               'nerve-wracking, but I saw that when done correctly, it worked, and I was '
               'willing to take the risk. Within the first 6 months, our portfolio was '
               'generating $10,000 per month.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': 'The thought of spending thousands per month on rent was extremely '
              'nerve-wracking, but I saw that when done correctly, it worked, and I was '
              'willing to take the risk. Within the first 6 months, our portfolio was '
              'generating $10,000 per month.',
       'title': 'How I Made 10 Million Selling Digital\xa0Products (By 22) (Inayah McMillan)',
       'url': 'https://www.youtube.com/watch?v=ow77v1CM31k&t=168s',
       'video_id': 'ow77v1CM31k'},
      {'author': 'Sell Your Service',
       'channel': 'Sell Your Service',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:48](https://www.youtube.com/watch?v=_csKVgudVVY&t=588s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "I think if they sign up a thousand people or something, I don't know. This is "
               'a really good way of quickly, quickly, quickly scaling a product based '
               'business and service-based businesses, if you know how to market it and it '
               'also generates you a ton of customers.',
       'timestamp': 588,
       'timestamp_label': '[00:09:48]',
       'timestamp_seconds': 588,
       'tip': "I think if they sign up a thousand people or something, I don't know. This is a "
              'really good way of quickly, quickly, quickly scaling a product based business '
              'and service-based businesses, if you know how to market it and it also '
              'generates you a ton of customers.',
       'title': 'How To Build A Self Liquidating Offer Funnel In HighLevel | Ryan Deiss (SLO) '
                '(Sell Your Service)',
       'url': 'https://www.youtube.com/watch?v=_csKVgudVVY&t=588s',
       'video_id': '_csKVgudVVY'},
      {'author': 'Money Talk With Leon',
       'channel': 'Money Talk With Leon',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:53](https://www.youtube.com/watch?v=Qqjup9J9CdI&t=653s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "I'm going to read it first, but then I have to explain why, you know, it's "
               'structured like this so it makes sense to you and that way you can understand '
               'how to tweak it and change it because every creator is going to be different.',
       'timestamp': 653,
       'timestamp_label': '[00:10:53]',
       'timestamp_seconds': 653,
       'tip': "I'm going to read it first, but then I have to explain why, you know, it's "
              'structured like this so it makes sense to you and that way you can understand '
              'how to tweak it and change it because every creator is going to be different.',
       'title': 'I Made $700K in 2 Days Selling Simple Digital Products (Step by Step) (Money '
                'Talk With Leon)',
       'url': 'https://www.youtube.com/watch?v=Qqjup9J9CdI&t=653s',
       'video_id': 'Qqjup9J9CdI'},
      {'author': 'Marketing Mark',
       'channel': 'Marketing Mark',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=qUqLPLYblBI&t=94s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "And then it will look like this. You'll have your main product and your bump "
               'product. Then what you want to do is go into your checkout page editor and '
               'click on your order form element. And as you scroll down, you should see the '
               'order bump options right here.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': "And then it will look like this. You'll have your main product and your bump "
              'product. Then what you want to do is go into your checkout page editor and '
              'click on your order form element. And as you scroll down, you should see the '
              'order bump options right here.',
       'title': 'How to Add Order Bumps in GoHighLevel (Plus Easy One-Click Upsells) '
                '(Marketing Mark)',
       'url': 'https://www.youtube.com/watch?v=qUqLPLYblBI&t=94s',
       'video_id': 'qUqLPLYblBI'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:56](https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=596s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "I've got a couple of minor expenses, for the calling team and things like "
               "that. Maybe it's not even necessary. Maybe I can continue to receive income "
               'for the probate deals through my main parent company.',
       'timestamp': 596,
       'timestamp_label': '[00:09:56]',
       'timestamp_seconds': 596,
       'tip': "I've got a couple of minor expenses, for the calling team and things like that. "
              "Maybe it's not even necessary. Maybe I can continue to receive income for the "
              'probate deals through my main parent company.',
       'title': 'Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR '
                'PITCH |  #10 (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=596s',
       'video_id': 'OrEz4Qk-EZ0'},
      {'author': 'Richard Yu',
       'channel': 'Richard Yu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:46](https://www.youtube.com/watch?v=RxypuPGBRPI&t=1126s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'AI system, how to make content that actually drives buyers to your links. And '
               "normally it's $997, just under $1,000. Remember that multi-billion dollar "
               'website, Wix, that I just showed you a few minutes ago?',
       'timestamp': 1126,
       'timestamp_label': '[00:18:46]',
       'timestamp_seconds': 1126,
       'tip': 'AI system, how to make content that actually drives buyers to your links. And '
              "normally it's $997, just under $1,000. Remember that multi-billion dollar "
              'website, Wix, that I just showed you a few minutes ago?',
       'title': 'I Made $32.7 Million Selling Simple Digital Products (Full Masterclass) '
                '(Richard Yu)',
       'url': 'https://www.youtube.com/watch?v=RxypuPGBRPI&t=1126s',
       'video_id': 'RxypuPGBRPI'},
      {'author': 'Social Nest Marketing',
       'channel': 'Social Nest Marketing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=-xCVVPZu48k&t=115s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'But first, I always forget this first step. The first step is you need to go '
               'to the media storage, okay? And I think I have the upsells in here, but the '
               "thing with the upsells is let me see, it's it came in as a folder.",
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': 'But first, I always forget this first step. The first step is you need to go to '
              'the media storage, okay? And I think I have the upsells in here, but the thing '
              "with the upsells is let me see, it's it came in as a folder.",
       'title': 'GoHighLevel One-Click Upsell Setup: Payment Link Redirect + Auto-Delivery '
                'Workflow (Part 6) (Social Nest Marketing)',
       'url': 'https://www.youtube.com/watch?v=-xCVVPZu48k&t=115s',
       'video_id': '-xCVVPZu48k'},
      {'author': 'Nathan Nazareth',
       'channel': 'Nathan Nazareth',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:08](https://www.youtube.com/watch?v=dr37DaI8g3U&t=128s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': 'SOPs, and everything that somebody would need to follow the exact steps that I '
               'took to see success. How much money can you make by selling digital products? '
               "Let's run some numbers here. If you have a 100 customers on a $497 course, "
               "that's $49,700 in pure profit.",
       'timestamp': 128,
       'timestamp_label': '[00:02:08]',
       'timestamp_seconds': 128,
       'tip': 'SOPs, and everything that somebody would need to follow the exact steps that I '
              'took to see success. How much money can you make by selling digital products? '
              "Let's run some numbers here. If you have a 100 customers on a $497 course, "
              "that's $49,700 in pure profit.",
       'title': "How to Sell AI Digital Products (beginner's guide) (Nathan Nazareth)",
       'url': 'https://www.youtube.com/watch?v=dr37DaI8g3U&t=128s',
       'video_id': 'dr37DaI8g3U'},
      {'author': "Bob Diamond - America's Tax Sale Attorney",
       'channel': "Bob Diamond - America's Tax Sale Attorney",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:09](https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=549s)',
       'relevance': 'Attributed practitioner commentary on running a 1-to-4 person multi-SKU '
                    'digital product portfolio with SOPs, creative contractors, and weekly '
                    'KPIs.',
       'source_type': 'video_pro_tip',
       'text': "Court is the judicial system, so that's why it's a judicial claim. Now, when "
               "you have to do those you're going to hire an attorney to do the claim for you, "
               "because you can't represent someone else in court.",
       'timestamp': 549,
       'timestamp_label': '[00:09:09]',
       'timestamp_seconds': 549,
       'tip': "Court is the judicial system, so that's why it's a judicial claim. Now, when "
              "you have to do those you're going to hire an attorney to do the claim for you, "
              "because you can't represent someone else in court.",
       'title': "Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney)",
       'url': 'https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=549s',
       'video_id': 'qGPsbhsEAVQ'}],
 12: [{'author': 'Doug Boughton',
       'channel': 'Doug Boughton',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:58](https://www.youtube.com/watch?v=8lz_gy-Osw8&t=538s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "It's a seven-day traffic sprint that all members get access to, and I'll show "
               "you what happens after those seven days. And then next month, it's my annual "
               'event. Tickets in the past have sold for $997 just for this one event.',
       'timestamp': 538,
       'timestamp_label': '[00:08:58]',
       'timestamp_seconds': 538,
       'tip': "It's a seven-day traffic sprint that all members get access to, and I'll show "
              "you what happens after those seven days. And then next month, it's my annual "
              'event. Tickets in the past have sold for $997 just for this one event.',
       'title': 'Are Free Skool Communities Dying? Why I Turned Mine Paid (Doug Boughton)',
       'url': 'https://www.youtube.com/watch?v=8lz_gy-Osw8&t=538s',
       'video_id': '8lz_gy-Osw8'},
      {'author': 'Richard Yu',
       'channel': 'Richard Yu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:17](https://www.youtube.com/watch?v=gjffmgucDSw&t=1097s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "The content structure, hook, go to problem, daily routine, what's the call to "
               'action, the call to action used, the editing style. It literally teaches you '
               'how to execute on each one of these hook ideas. You have a content calendar.',
       'timestamp': 1097,
       'timestamp_label': '[00:18:17]',
       'timestamp_seconds': 1097,
       'tip': "The content structure, hook, go to problem, daily routine, what's the call to "
              'action, the call to action used, the editing style. It literally teaches you '
              'how to execute on each one of these hook ideas. You have a content calendar.',
       'title': 'FULL COURSE: How to Build & Sell Digital Products With AI (Step by Step) '
                '(Richard Yu)',
       'url': 'https://www.youtube.com/watch?v=gjffmgucDSw&t=1097s',
       'video_id': 'gjffmgucDSw'},
      {'author': 'Make Money with Stacy La',
       'channel': 'Make Money with Stacy La',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:09](https://www.youtube.com/watch?v=gGW2IMNOz68&t=849s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': 'I just showed you in order inside my free video checklist. The checklist '
               'includes every prompt I use in this video that you can copy and paste, as well '
               'as numbered steps that you can follow to build your first digital template '
               'business.',
       'timestamp': 849,
       'timestamp_label': '[00:14:09]',
       'timestamp_seconds': 849,
       'tip': 'I just showed you in order inside my free video checklist. The checklist '
              'includes every prompt I use in this video that you can copy and paste, as well '
              'as numbered steps that you can follow to build your first digital template '
              'business.',
       'title': 'Watch Me Create a 6 Figure Digital Product with AI in 14 Minutes | UPDATED '
                'Tutorial | Genspark (Make Money with Stacy La)',
       'url': 'https://www.youtube.com/watch?v=gGW2IMNOz68&t=849s',
       'video_id': 'gGW2IMNOz68'},
      {'author': 'Aeris Vale Tutorials',
       'channel': 'Aeris Vale Tutorials',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:45](https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=165s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "Lastly, publish your product. Once it's published, voila, you're ready to "
               "start selling on Gumroad. With these steps, you're fully equipped to reach a "
               'wide audience with your amazing Notion template.',
       'timestamp': 165,
       'timestamp_label': '[00:02:45]',
       'timestamp_seconds': 165,
       'tip': "Lastly, publish your product. Once it's published, voila, you're ready to start "
              "selling on Gumroad. With these steps, you're fully equipped to reach a wide "
              'audience with your amazing Notion template.',
       'title': 'How To Sell A Notion Template On Gumroad - Step by Step Guide | THELOSTOFFER '
                '#notion #gumroad (Aeris Vale Tutorials)',
       'url': 'https://www.youtube.com/watch?v=ciKrPZ_nIpQ&t=165s',
       'video_id': 'ciKrPZ_nIpQ'},
      {'author': 'Adnan Pilditch',
       'channel': 'Adnan Pilditch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=mf1WAw0FyaI&t=176s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': 'A short, clear onboarding video that explains to them everything from start to '
               'finish, so they will never get lost. A step-by-step roadmap which shows them '
               'where to go from A to Z. Automated DMs for inactive members after 48 hours. '
               'And we had the three-day activation path.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'A short, clear onboarding video that explains to them everything from start to '
              'finish, so they will never get lost. A step-by-step roadmap which shows them '
              'where to go from A to Z. Automated DMs for inactive members after 48 hours. And '
              'we had the three-day activation path.',
       'title': 'Top 7 Secrets To Building a $45,000/Month Skool Community (Adnan Pilditch)',
       'url': 'https://www.youtube.com/watch?v=mf1WAw0FyaI&t=176s',
       'video_id': 'mf1WAw0FyaI'},
      {'author': 'Side Hustle Mastery',
       'channel': 'Side Hustle Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:42](https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=222s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "Gumroad and start making sales from it. Now, the first thing you're going to "
               'want to do is head up to the top here and click on this share button. Once you '
               "click on that share button, you'll basically just head over to the publish "
               'tab.',
       'timestamp': 222,
       'timestamp_label': '[00:03:42]',
       'timestamp_seconds': 222,
       'tip': "Gumroad and start making sales from it. Now, the first thing you're going to "
              'want to do is head up to the top here and click on this share button. Once you '
              "click on that share button, you'll basically just head over to the publish tab.",
       'title': 'How to Make Money Selling Notion Templates [Gumroad Step-by-Step] (Side '
                'Hustle Mastery)',
       'url': 'https://www.youtube.com/watch?v=2j9bt8ET3Ec&t=222s',
       'video_id': '2j9bt8ET3Ec'},
      {'author': 'Profitable Talents',
       'channel': 'Profitable Talents',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:06](https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=246s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "I'm going to reflect your feedback into the series. This is the first episode "
               "of the series. So I want to start immediately. I haven't prepared anything. So "
               "you get to be with me from day one as I'm thinking.",
       'timestamp': 246,
       'timestamp_label': '[00:04:06]',
       'timestamp_seconds': 246,
       'tip': "I'm going to reflect your feedback into the series. This is the first episode "
              "of the series. So I want to start immediately. I haven't prepared anything. So "
              "you get to be with me from day one as I'm thinking.",
       'title': 'Watch Me Build a Self-Liquidating Offer Funnel From Scratch (Ep. 1) '
                '(Profitable Talents)',
       'url': 'https://www.youtube.com/watch?v=_I5YFl6Ym_k&t=246s',
       'video_id': '_I5YFl6Ym_k'},
      {'author': 'Smart Capital',
       'channel': 'Smart Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:13](https://www.youtube.com/watch?v=GmI0MYeyMg0&t=133s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': 'I want to start with a simple test. Would someone open this template every '
               'single day? If the answer is no, it probably will not sell well, no matter how '
               'pretty it looks. The templates that tend to perform best solve a recurring '
               'job.',
       'timestamp': 133,
       'timestamp_label': '[00:02:13]',
       'timestamp_seconds': 133,
       'tip': 'I want to start with a simple test. Would someone open this template every '
              'single day? If the answer is no, it probably will not sell well, no matter how '
              'pretty it looks. The templates that tend to perform best solve a recurring job.',
       'title': 'Sell Notion Templates on Gumroad: What a $29 Sale Really Keeps (2026) (Smart '
                'Capital)',
       'url': 'https://www.youtube.com/watch?v=GmI0MYeyMg0&t=133s',
       'video_id': 'GmI0MYeyMg0'},
      {'author': 'GuideHatch Tutorials',
       'channel': 'GuideHatch Tutorials',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:10](https://www.youtube.com/watch?v=DNdWpxzzTQM&t=70s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': 'This action will prompt you to enter the name of your project. Choose a name '
               'that is both memorable and descriptive, as this will be the first thing '
               "potential buyers see. After you've named your project, ensure that it is "
               'categorized as a digital product.',
       'timestamp': 70,
       'timestamp_label': '[00:01:10]',
       'timestamp_seconds': 70,
       'tip': 'This action will prompt you to enter the name of your project. Choose a name '
              'that is both memorable and descriptive, as this will be the first thing '
              "potential buyers see. After you've named your project, ensure that it is "
              'categorized as a digital product.',
       'title': 'How to sell Notion templates on Gumroad (Creative Earnings) (GuideHatch '
                'Tutorials)',
       'url': 'https://www.youtube.com/watch?v=DNdWpxzzTQM&t=70s',
       'video_id': 'DNdWpxzzTQM'},
      {'author': 'Maria Wendt',
       'channel': 'Maria Wendt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:16](https://www.youtube.com/watch?v=zQQZEPMxT6U&t=196s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "That's not I mean, again, I do 200 orders a day. So, that's what is the math "
               'on that per month. 200 around 200 orders a day times 30 days. I do 6,000 '
               'orders a month, right?',
       'timestamp': 196,
       'timestamp_label': '[00:03:16]',
       'timestamp_seconds': 196,
       'tip': "That's not I mean, again, I do 200 orders a day. So, that's what is the math on "
              'that per month. 200 around 200 orders a day times 30 days. I do 6,000 orders a '
              'month, right?',
       'title': 'How To Turn Your $24 Digital Product Into $24,000 (Scaling Strategy That '
                'Works) (Maria Wendt)',
       'url': 'https://www.youtube.com/watch?v=zQQZEPMxT6U&t=196s',
       'video_id': 'zQQZEPMxT6U'},
      {'author': 'Eden',
       'channel': 'Eden',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:10](https://www.youtube.com/watch?v=VJ-JR7uMY34&t=1030s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': 'So productivity product titled maybe something like the six month plan for '
               'helping people change their lives and achieve their goals or just to become '
               'productive could absolutely become a product and the thing about this is that '
               "it's validated.",
       'timestamp': 1030,
       'timestamp_label': '[00:17:10]',
       'timestamp_seconds': 1030,
       'tip': 'So productivity product titled maybe something like the six month plan for '
              'helping people change their lives and achieve their goals or just to become '
              'productive could absolutely become a product and the thing about this is that '
              "it's validated.",
       'title': 'How To Build Your First $10,000 Digital Product (Full Beginner Guide) (Eden)',
       'url': 'https://www.youtube.com/watch?v=VJ-JR7uMY34&t=1030s',
       'video_id': 'VJ-JR7uMY34'},
      {'author': 'Alek',
       'channel': 'Alek',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:49](https://www.youtube.com/watch?v=T-gfoXzz8k8&t=229s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "'t know how to drive your own traffic yet, then my recommendation would be to "
               'start on a marketplace website like Etsy. Etsy drives millions of visitors to '
               'their marketplace every single month.',
       'timestamp': 229,
       'timestamp_label': '[00:03:49]',
       'timestamp_seconds': 229,
       'tip': "'t know how to drive your own traffic yet, then my recommendation would be to "
              'start on a marketplace website like Etsy. Etsy drives millions of visitors to '
              'their marketplace every single month.',
       'title': 'Build & Sell Digital Products with A.I. (Full Course) (Alek)',
       'url': 'https://www.youtube.com/watch?v=T-gfoXzz8k8&t=229s',
       'video_id': 'T-gfoXzz8k8'},
      {'author': 'SamCart',
       'channel': 'SamCart',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:00](https://www.youtube.com/watch?v=UxhtBuVj4gY&t=1620s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "We've processed more than $8 billion in total sales, and the average seller "
               'who comes in and turns on these features is watching their revenue double in '
               'the first 12 months. You can start for free at samcart. Link is in the '
               'description.',
       'timestamp': 1620,
       'timestamp_label': '[00:27:00]',
       'timestamp_seconds': 1620,
       'tip': "We've processed more than $8 billion in total sales, and the average seller who "
              'comes in and turns on these features is watching their revenue double in the '
              'first 12 months. You can start for free at samcart. Link is in the description.',
       'title': 'The Complete Guide to Upsells ($8 Billion in Data) (SamCart)',
       'url': 'https://www.youtube.com/watch?v=UxhtBuVj4gY&t=1620s',
       'video_id': 'UxhtBuVj4gY'},
      {'author': 'Click Guide',
       'channel': 'Click Guide',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=F5Le0mxyMhg&t=55s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "Talking about plans, here's the detail on the pricing. School has a flat rate "
               'of $99 per month for one group, including unlimited members and courses. And a '
               '14-day free trial is available for you to get your feet wet before committing.',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': "Talking about plans, here's the detail on the pricing. School has a flat rate "
              'of $99 per month for one group, including unlimited members and courses. And a '
              '14-day free trial is available for you to get your feet wet before committing.',
       'title': 'Skool vs Circle (2026): The Best Online Communities & Courses? (Click Guide)',
       'url': 'https://www.youtube.com/watch?v=F5Le0mxyMhg&t=55s',
       'video_id': 'F5Le0mxyMhg'},
      {'author': 'Bree and Steve',
       'channel': 'Bree and Steve',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:42](https://www.youtube.com/watch?v=zmw7OXf39rQ&t=522s)',
       'relevance': 'Attributed practitioner commentary on a 30-day MVP validation, checkout '
                    'wiring, traffic seeding, and unit-economics launch sprint.',
       'source_type': 'video_pro_tip',
       'text': "I'm going to just label this projects and then new database and I'm going to "
               "go ahead and delete or just hide the name and I'm just going to go in and add "
               'different tasks that someone might have throughout the week.',
       'timestamp': 522,
       'timestamp_label': '[00:08:42]',
       'timestamp_seconds': 522,
       'tip': "I'm going to just label this projects and then new database and I'm going to go "
              "ahead and delete or just hide the name and I'm just going to go in and add "
              'different tasks that someone might have throughout the week.',
       'title': 'How To Make & Sell Notion Templates (Make $1000+ MONTH!) (Bree and Steve)',
       'url': 'https://www.youtube.com/watch?v=zmw7OXf39rQ&t=522s',
       'video_id': 'zmw7OXf39rQ'}]}
