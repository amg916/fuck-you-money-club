from __future__ import annotations

def build_volume_003_workbook() -> dict:
    return {'workbook_id': 'wb-003-digital-product-empire',
 'volume_id': 'vol-003-digital-product-empire',
 'title': 'Digital Product Empire — Practitioner Testimony Operator Workbook',
 'subtitle': 'Digital Product Empire: Choose a Necessary Buyer Outcome, Build and Inspect the Product, '
             'Compare Storefront Economics, and Connect Payments to Relevant Offers and Reliable Delivery',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Define the Buyer, Offer, and Inspected First Product',
                 'purpose': 'Turn a digital product idea into a specific buyer promise, a practical '
                            'production plan, and a distribution path. Separate practitioner results from '
                            'your own expectations, and make usefulness, customer instructions, and '
                            'inspection requirements explicit before preparing the product for sale.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete the buyer and problem fields before selecting a file format, '
                                  'building pages, or choosing an application for production.',
                                  'Write each answer as an operating decision for your product rather than '
                                  "copying another seller's revenue milestone as your target.",
                                  'Choose one initial distribution route and connect the free sample, paid '
                                  'product, and any later offer around the same buyer.',
                                  'Specify where AI assists production, where your judgment changes the '
                                  'output, and which functions require inspection before publication.',
                                  'Finish with a clear release decision that identifies unresolved demand, '
                                  'product quality, access, or support problems instead of assuming '
                                  'completion.'],
                 'fields': [{'name': 'specific_buyer_and_problem',
                             'type': 'textarea',
                             'prompt': 'Name one buyer and one problem the product will address. Describe '
                                       'the situation that makes the problem necessary to solve, then '
                                       'exclude adjacent audiences or topics that would turn the offer '
                                       'into a broad collection of information.',
                             'example': 'I will narrow the ebook to one person facing one problem rather '
                                        'than promise a complete guide to everything about baseball. The '
                                        'product description must make that boundary understandable before '
                                        'I draft chapters. Moran attributes their unsuccessful broad '
                                        'baseball book to missing this specificity. [Brian Moran — '
                                        '3iU4a1yWGn0 @ 00:03:00]'},
                            {'name': 'demand_before_production',
                             'type': 'textarea',
                             'prompt': 'Record what you need to learn about the buyer and topic before '
                                       'committing hours to production. Identify the assumption most '
                                       'likely to produce an unwanted template, and describe how your '
                                       'research will determine whether to continue, narrow, or change the '
                                       'idea.',
                             'example': 'I will research the intended buyer and topic before building '
                                        'another paid Notion template. A student or teacher label alone '
                                        "will not count as evidence that the product is wanted. Jaro's "
                                        'first two templates for those audiences made zero sales, so '
                                        'attractive construction cannot replace this decision. [Victor '
                                        'Jaro — DUY7O02C0Ps @ 00:02:42]'},
                            {'name': 'offer_before_format',
                             'type': 'textarea',
                             'prompt': 'Write the offer as a buyer outcome before naming the software or '
                                       'file format. Explain what the customer receives, why those '
                                       'components belong together, and which appealing additions you will '
                                       'leave out because they do not support that outcome.',
                             'example': 'I will define the outcome before deciding whether the product '
                                        'needs a guide, member area, or resource app. The initial offer '
                                        'statement must explain what the buyer is purchasing without '
                                        'leading with software names. I will add components only when they '
                                        "serve that promise, following Nazareth's offer-first sequence. "
                                        '[Nathan Nazareth — 6cm2o8zzuNw @ 00:01:25]'},
                            {'name': 'initial_price_position',
                             'type': 'textarea',
                             'prompt': 'Choose an initial price position and explain the product quality '
                                       "and specificity supporting it. Distinguish a practitioner's "
                                       'suggested range from evidence about your own buyers, and identify '
                                       'what remains unproven rather than presenting a premium price as '
                                       'automatically justified.',
                             'example': 'For an edited PDF addressing a specific pain, I will consider a '
                                        "starting price within Yu's suggested $27 to $47 range. I will not "
                                        'describe that range as a proven result for my product. My '
                                        'decision depends on delivering a focused resource rather than '
                                        'publishing an untouched draft. [Richard Yu — rYUS7ibZhYo @ '
                                        '00:06:03]'},
                            {'name': 'free_sample_to_paid_outcome',
                             'type': 'textarea',
                             'prompt': 'Describe one small win a free sample will help the buyer achieve. '
                                       'Connect that win directly to the paid product, explain why the '
                                       'sample has standalone value, and remove material that attracts '
                                       'people who do not need the paid outcome.',
                             'example': 'I will make the free budgeting and meal-planning resource deliver '
                                        'one small, useful result that leads naturally into the paid '
                                        'product. It will not be a general giveaway unrelated to the '
                                        'purchase. The sample must be specific, outcome-focused, and '
                                        'useful enough that it could reasonably stand as a paid resource. '
                                        '[Rochelle Be — 4e4pRrWsJvU @ 00:22:39]'},
                            {'name': 'distribution_while_building',
                             'type': 'textarea',
                             'prompt': 'Select an initial audience-building activity that can run while '
                                       'you create the product. State what you will share, how it relates '
                                       "to the buyer's problem, and how you will avoid treating a finished "
                                       'product as a substitute for distribution.',
                             'example': 'While making free Notion templates, I will share practical tips, '
                                        'insights, and behind-the-scenes creation posts. These posts will '
                                        'stay connected to the organizational problem the template '
                                        'addresses rather than merely announce that I am building '
                                        'something. Audience-building will begin during production instead '
                                        'of waiting until a paid template is finished. [Victor Jaro — '
                                        'DUY7O02C0Ps @ 00:03:32]'},
                            {'name': 'ai_workflow_and_human_judgment',
                             'type': 'textarea',
                             'prompt': 'Describe the AI-assisted task you will turn into a reusable '
                                       'product workflow. Identify the prompts, supplied assets, and steps '
                                       'the buyer needs, and explain how you will distinguish a repeatable '
                                       'working process from a generic collection of generated '
                                       'information.',
                             'example': 'For an AI thumbnail workflow, I will return to the conversation '
                                        'that completed the task and request a summary of its steps, '
                                        'prompts, and supplied assets. I will use that record to assemble '
                                        "the workflow product, keeping the buyer's repeatable process "
                                        'central rather than selling disconnected instructions or generic '
                                        'information. [Emmanuel Adanu — _YY-8C1VR9o @ 00:03:20]'},
                            {'name': 'production_and_export_method',
                             'type': 'textarea',
                             'prompt': 'Specify how you will create consistent product pages without '
                                       'rebuilding each layout. Name the point at which a page becomes '
                                       'your reusable pattern, explain which content still requires '
                                       'customization, and record the intended export format for the '
                                       'finished ebook.',
                             'example': 'I will establish one Canva page layout that works, then duplicate '
                                        'it for the remaining ebook pages. Each duplicate will receive the '
                                        'content appropriate to that page rather than retain filler from '
                                        'the original. Once the ebook is assembled, I will export it as '
                                        'PDF standard for delivery. [Baddie In Business — EZ9234g-l7Q @ '
                                        '00:08:29]'},
                            {'name': 'generated_product_inspection',
                             'type': 'textarea',
                             'prompt': 'List the parts of the generated product that require direct '
                                       'inspection before sale. Include both visible presentation and '
                                       'working behavior where applicable, then state what must be '
                                       'corrected before release rather than allowing fast generation to '
                                       'stand in for quality review.',
                             'example': 'I will inspect every generated page and line, then check any '
                                        'tabs, formulas, appearance, and functions included in the '
                                        'product. A polished mockup will not count as proof that the '
                                        'underlying resource works. Anything incorrect or unfinished will '
                                        'return to revision before I make the product available for '
                                        'purchase. [Make Money with Stacy La — gGW2IMNOz68 @ 00:10:59]'},
                            {'name': 'customer_instructions_and_support',
                             'type': 'textarea',
                             'prompt': 'Write the customer guidance needed before and after purchase. '
                                       'Separate download questions from usage questions, identify where '
                                       'each answer belongs, and explain how clear instructions will '
                                       'reduce avoidable support without suggesting that digital delivery '
                                       'eliminates the need to help customers.',
                             'example': 'I will place download instructions and frequently asked questions '
                                        'in the listing images, then include usage instructions inside the '
                                        'delivered files. This separates access questions from questions '
                                        'about using the resource. I will still check customer messages, '
                                        'but repeated confusion should lead to clearer guidance rather '
                                        'than remain an unresolved support burden. [Tatyana Savage — '
                                        'TGNTFquVxZU @ 00:13:01]'}],
                 'completion_gate': 'Proceed only when one buyer, one problem, a clear offer, an initial '
                                    'price rationale, and an audience-building route are written down. The '
                                    'product must have a defined inspection process and customer '
                                    'instructions. Keep unresolved demand assumptions and unfinished '
                                    'generated content visible; neither a polished layout nor another '
                                    "seller's sales milestone closes those gaps."},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Package the Notion Template and Calculate Storefront Proceeds',
                 'purpose': 'Prepare a focused template that a beginner can understand and duplicate, then '
                            'compare selling routes without confusing commission with total cost. Connect '
                            'listing research, product access, payout readiness, and controlled updates to '
                            'a storefront decision you can explain.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ["Start with the template's problem-solving framework and remove features "
                                  'that make the first successful use harder for a new customer.',
                                  'Review competing listings and customer reviews before expanding the '
                                  'catalog, recording the specific demand or presentation questions that '
                                  'remain unresolved.',
                                  'Treat publication, delivery, duplication permissions, payout setup, and '
                                  'customer onboarding as separate checks rather than one general launch '
                                  'task.',
                                  'Keep every fee comparison tied to its stated product price and '
                                  'assumptions; do not label a commission-only calculation as final '
                                  'proceeds.',
                                  'Choose one listing change at a time, retain a clean master copy, and '
                                  'test updates through a fresh customer experience.'],
                 'fields': [{'name': 'beginner_framework_and_feature_cut',
                             'type': 'textarea',
                             'prompt': "Describe the template's core problem-solving framework as if the "
                                       'buyer has never used Notion. Identify features you will remove, '
                                       'the first action the buyer should take, and the guidance that '
                                       'prevents complexity from becoming the reason for a refund.',
                             'example': 'I will organize the template around a focused framework rather '
                                        'than display every feature I can build. The opening instructions '
                                        'will assume the customer is new to Notion and make the first '
                                        "action clear. Mike and Matty's early refund over overwhelming "
                                        'complexity makes simplification part of the product, not optional '
                                        'polish. [Mike and Matty — keOebOEv-Oc @ 00:05:06]'},
                            {'name': 'category_and_review_research',
                             'type': 'textarea',
                             'prompt': 'Record the category and competitor-review research you will '
                                       'complete before building additional templates. Describe what '
                                       'buyers appear to value, what questions need further investigation, '
                                       'and how those findings will influence your product scope rather '
                                       'than merely decorate the listing copy.',
                             'example': 'Before expanding the template catalog, I will examine the '
                                        'category and competing customer reviews. I will record what '
                                        'customers like and which product decisions those observations '
                                        'support. I will not skip research because production feels '
                                        'faster; Timothy describes repeatedly making that mistake before '
                                        'emphasizing research ahead of catalog building. [Brandon Timothy '
                                        '— 0plVE1LRxYo @ 00:08:29]'},
                            {'name': 'ai_template_customization',
                             'type': 'textarea',
                             'prompt': 'Explain how you will turn an AI-assisted template build into a '
                                       'finished product with intentional presentation. Identify what must '
                                       'wait until generation finishes, what you will customize manually, '
                                       'and how you will avoid presenting initial output as the completed '
                                       'customer experience.',
                             'example': 'I will let the Claude build finish before judging the template as '
                                        'complete or making final presentation decisions. Then I will '
                                        'spend time adjusting the result and making it my own. The initial '
                                        'output is a starting point for customization, not a reason to '
                                        'skip the work of finishing the product. [Money With Mak — '
                                        'V6xU-P9FHJA @ 00:14:37]'},
                            {'name': 'benefit_led_listing_description',
                             'type': 'textarea',
                             'prompt': "Draft the listing description around the template's benefits, "
                                       'relevant features, and distinctive approach. Make the intended use '
                                       'understandable without relying on a long feature inventory, and '
                                       'identify any claim that needs clearer explanation before a buyer '
                                       'can make an informed purchase.',
                             'example': 'My description will explain the organizational problem the '
                                        'template addresses, the features supporting that result, and what '
                                        'makes its approach distinctive. I will replace vague praise with '
                                        "clear explanations of the buyer's use. The description should be "
                                        'compelling because the solution is understandable, not because '
                                        'the page lists the most features. [Aeris Vale Tutorials — '
                                        'ciKrPZ_nIpQ @ 00:01:32]'},
                            {'name': 'public_access_and_duplication_audit',
                             'type': 'textarea',
                             'prompt': 'Describe the exact access audit you will perform on the delivered '
                                       'template link. Include duplication availability, private material, '
                                       'internal planning sections, and placeholder text, then state which '
                                       'failures block publication even when the sales page and payment '
                                       'setup are ready.',
                             'example': 'I will open the link intended for customers and confirm that '
                                        'duplication remains available. Before release, I will remove '
                                        'private notes, internal planning sections, and placeholder text '
                                        'from the published page. A working sales page will not override a '
                                        'failed access check or excuse exposing material that does not '
                                        'belong in the product. [Tutorials At Desk — VEFf-FR0dxw @ '
                                        '00:05:09]'},
                            {'name': 'delivery_link_and_customer_instruction',
                             'type': 'textarea',
                             'prompt': 'Write the delivery instruction that accompanies the template link. '
                                       'Explain how the buyer reaches their usable copy, identify where '
                                       'the instruction appears, and distinguish receiving a link from '
                                       'successfully understanding the duplication action needed to begin '
                                       'using the purchased template.',
                             'example': "Beside the delivered template link, I will write: 'Click the "
                                        "link, hit duplicate, and it's yours.' I will make that direction "
                                        'easy to find instead of assuming a first-time customer knows what '
                                        'duplication means. The delivery message must connect access to '
                                        "the action that produces the customer's usable copy. [Extreme How "
                                        "To's — SK_-uXSKE88 @ 00:01:28]"},
                            {'name': 'storefront_publication_readiness',
                             'type': 'textarea',
                             'prompt': 'Record the payout and verification steps that could prevent the '
                                       'storefront from publishing your product. Separate an unfinished '
                                       'account requirement from a product problem, and specify what you '
                                       'will complete before returning to publication rather than '
                                       'repeatedly retrying the same blocked action.',
                             'example': 'If Gumroad blocks publication because payout setup is missing, I '
                                        'will complete the country, account type, supported payment '
                                        'connection, and requested verification before trying again. I '
                                        'will keep that account task separate from template editing. A '
                                        'finished product does not remove the requirement to complete the '
                                        "storefront's publication prerequisites. [Tutorials At Desk — "
                                        'VEFf-FR0dxw @ 00:03:20]'},
                            {'name': 'commission_vs_complete_cost',
                             'type': 'textarea',
                             'prompt': 'Build a comparison that separates platform commission from '
                                       'processing and any other stated charges. Use the same selling '
                                       'price for both options, label incomplete totals clearly, and '
                                       'explain why a lower commission alone does not establish how much '
                                       'cash the seller ultimately keeps.',
                             'example': 'For the reported $29 comparison, I will record Gumroad commission '
                                        'as $2.90 and Payhip Free commission as $1.45, each before '
                                        'processing. I will not call $26.10 or $27.55 final proceeds. '
                                        'Those intermediate balances omit processing and must remain '
                                        'labeled that way until the complete applicable charges are '
                                        'accounted for. [Smart Capital — GmI0MYeyMg0 @ 00:08:46]'},
                            {'name': 'buyer_checkout_total',
                             'type': 'textarea',
                             'prompt': 'Describe how you will inspect the complete buyer checkout '
                                       'breakdown rather than only the advertised product price. Record '
                                       'any added buyer service charge separately from seller deductions, '
                                       'and explain how an unexpected total could change the experience '
                                       'promised by your listing.',
                             'example': "I will read the checkout breakdown from the buyer's side before "
                                        'considering the listing ready. Skool News demonstrates a $7.50 '
                                        'added charge on a $150 offer, so the advertised price alone may '
                                        'not describe the amount presented at checkout. I will distinguish '
                                        'that buyer charge from deductions used to calculate seller '
                                        'proceeds. [Skool News — ZoLyT1PDXow @ 00:10:01]'},
                            {'name': 'controlled_listing_experiment',
                             'type': 'textarea',
                             'prompt': 'Choose one listing element to change and describe how you will '
                                       'evaluate it without mixing several simultaneous edits. Record the '
                                       'conversion measure, observation period, and spreadsheet entry you '
                                       'need before deciding whether the change helped or whether another '
                                       'element should be tested.',
                             'example': 'I will change one listing element and leave the test running for '
                                        'at least two weeks before changing another. I will record '
                                        'conversion rate in a spreadsheet so the decision is not based '
                                        'only on how the new version looks. Further edits will wait until '
                                        'this individual change has an observation record. [Smart Capital '
                                        '— GmI0MYeyMg0 @ 00:12:22]'}],
                 'completion_gate': 'Proceed only when the template has a beginner-friendly framework, a '
                                    'clear listing, a tested public link, and an understandable '
                                    'duplication instruction. Resolve publication prerequisites and '
                                    'distinguish incomplete fee calculations from final proceeds. Before '
                                    'announcing any template update, duplicate it into a fresh account and '
                                    'confirm the customer experience still works.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Assign Payment Responsibilities and Test the Offer Sequence',
                 'purpose': 'Compare payment control with merchant-of-record responsibilities, preserve '
                            'the functions needed for delivery and migration, and build an offer sequence '
                            'whose prices, acceptance actions, and access rules match what customers '
                            'actually purchase. Keep reported platform terms distinct from confirmed '
                            'arrangements for your business.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Write down who handles the payment and tax responsibilities before '
                                  'comparing headline fees or choosing a migration destination.',
                                  'Treat platform coverage, eligibility, migration dates, and quoted '
                                  'pricing as items requiring confirmation for the arrangement you intend '
                                  'to use.',
                                  'Include payout minimums, timing, account approval, and missing delivery '
                                  'functions in the decision rather than focusing only on transaction '
                                  'charges.',
                                  'Map the checkout bump, post-payment offer, refusal route, and '
                                  'purchased-product delivery before checking the visible pages for '
                                  'inconsistent prices.',
                                  'Place a real test order through the intended sequence; a preview, '
                                  'purchase tag, or attractive button is not proof of correct '
                                  'fulfillment.'],
                 'fields': [{'name': 'processor_or_merchant_of_record',
                             'type': 'textarea',
                             'prompt': 'State whether you intend to use a standard payment processor or a '
                                       'merchant of record. Explain the responsibility distinction in '
                                       'plain language, identify why it matters to your product business, '
                                       'and avoid assuming that every payment connection provides the same '
                                       'administrative handoff.',
                             'example': 'I will distinguish standard Stripe Checkout from a '
                                        'merchant-of-record arrangement before comparing costs. Tutorly '
                                        'describes Stripe Checkout as a payment processor and Paddle or '
                                        'Lemon Squeezy as the legal seller under their merchant-of-record '
                                        'model. My decision will specify which arrangement I am '
                                        'considering instead of treating every checkout connection as '
                                        'equivalent. [Tutorly — IfaCBBIoVK0 @ 00:00:32]'},
                            {'name': 'tax_activation_and_integration',
                             'type': 'textarea',
                             'prompt': 'Describe how you will verify tax activation separately from '
                                       'payment connectivity. Identify the dashboard setting and '
                                       'course-platform integration involved in your intended setup, and '
                                       'state what evidence is still missing if payments work but the '
                                       'tax-related configuration has not been inspected.',
                             'example': 'I will not interpret an active Stripe connection as proof that '
                                        'Stripe Tax is enabled. For the demonstrated course-platform '
                                        'setup, I will check activation in the Stripe dashboard and then '
                                        'the platform integration. Until both steps are addressed, '
                                        'successful payment connectivity will remain separate from '
                                        'confirmation of the intended tax configuration. [OCH Platform — '
                                        'H8_HQ-GZOwc @ 00:00:17]'},
                            {'name': 'administrative_handoff_cost',
                             'type': 'textarea',
                             'prompt': 'Compare the extra cost of a tax-handling arrangement with your own '
                                       "filing time and accountant costs. Keep the practitioner's example "
                                       'separate from your figures, and explain which missing expense '
                                       'estimates prevent you from declaring the lower transaction fee the '
                                       'cheaper operating choice.',
                             'example': 'I will price my own filing work and accountant support before '
                                        "preferring the lower headline fee. SoloBuild's forty-sales "
                                        'illustration puts the monthly gap at about $40, or $480 annually. '
                                        'I will use that as a comparison example, not my actual expense '
                                        'estimate, until my administrative costs are written down. '
                                        '[SoloBuild — i05UCC3UvNY @ 00:07:02]'},
                            {'name': 'payout_timing_and_minimum',
                             'type': 'textarea',
                             'prompt': 'Record the payout minimum and timing associated with the payment '
                                       'option under consideration. Explain how those conditions differ '
                                       'from recording a sale, and identify the point at which funds '
                                       'become available rather than assuming every successful checkout '
                                       'produces immediately usable cash.',
                             'example': 'For the Paddle arrangement SoloBuild describes, I will record the '
                                        '$100 minimum and monthly payout schedule, with payment sent by '
                                        'the fifteenth when the threshold is reached. I will distinguish a '
                                        'completed sale from an available payout. The comparison must show '
                                        'timing and eligibility for payment, not only the transaction '
                                        'charge. [SoloBuild — i05UCC3UvNY @ 00:05:36]'},
                            {'name': 'migration_eligibility_and_license_priority',
                             'type': 'textarea',
                             'prompt': 'Identify the seller-location eligibility and existing license-key '
                                       'requirements that could rule out a migration destination. Put '
                                       'these checks before promotional pricing, and explain what must '
                                       'remain workable for existing customers before you consider a '
                                       'replacement checkout suitable for your product.',
                             'example': 'I will check seller-location eligibility before treating Managed '
                                        'Payments as the default destination for an existing plugin '
                                        'business. Gaurav reports that their India-based business is '
                                        'excluded from that route. A fee comparison cannot settle the '
                                        'migration decision while the intended seller is ineligible or the '
                                        'existing license requirements remain unresolved. [Gaurav Tiwari — '
                                        'cNc29NtuCYU @ 00:01:33]'},
                            {'name': 'replacement_delivery_functions',
                             'type': 'textarea',
                             'prompt': 'Inventory the functions your current selling arrangement provides '
                                       'beyond accepting payment. Assign a replacement path for file '
                                       'delivery, license keys, download links, storefront pages, and '
                                       'affiliates where relevant, and identify any missing function that '
                                       'would leave a paying customer without the purchased experience.',
                             'example': 'I will list file delivery, license keys, download links, '
                                        'storefront functions, and affiliates separately from payment '
                                        'processing. Heyymilian reports that Managed Payments does not '
                                        'include the corresponding Lemon Squeezy functions. I will '
                                        'therefore require a replacement plan for every function my '
                                        'product uses instead of assuming checkout migration preserves the '
                                        'entire selling experience. [heyymilian — 0R3CB1EcgKA @ 00:02:21]'},
                            {'name': 'migration_schedule_and_buffer',
                             'type': 'textarea',
                             'prompt': 'Write a migration schedule that distinguishes the reported '
                                       'tool-opening date, recommended starting point, and work duration. '
                                       'Include catalogs, webhooks, and live subscriptions where '
                                       'applicable, and explain why waiting until the final processing '
                                       'deadline would leave insufficient room for a difficult transition.',
                             'example': 'I will plan around the reported December 2, 2026 opening of '
                                        'automated exports and migration tools, with work beginning by '
                                        'mid-January rather than at the processing cutoff. Folioquest '
                                        'describes moving catalogs, webhooks, and live subscriptions as '
                                        'taking four to eight weeks. These reported dates will guide '
                                        'planning while I confirm the applicable arrangements. [Folioquest '
                                        '— M61DsgB51BI @ 00:01:36]'},
                            {'name': 'order_bump_price_and_total',
                             'type': 'textarea',
                             'prompt': 'Define the main offer, related checkout bump, and combined charge '
                                       'when the buyer selects both. Record the expected total with and '
                                       'without the bump, and describe the visible checkout behavior you '
                                       'must inspect before treating the additional offer as correctly '
                                       'connected.',
                             'example': "Using Marketing Mark's demonstrated price structure, I will "
                                        'expect the main offer alone to total $27 and the selected $17 '
                                        'bump to produce a $44 combined charge. I will inspect the '
                                        'displayed total as the bump is toggled rather than assume that '
                                        'adding promotional copy also connects the correct product and '
                                        'price. [Marketing Mark — qUqLPLYblBI @ 00:03:11]'},
                            {'name': 'upsell_acceptance_and_refusal',
                             'type': 'textarea',
                             'prompt': "Write the buyer-facing explanation for the post-payment offer's "
                                       'acceptance button and define a separate refusal path. Make the '
                                       'charging action unmistakable, then state how you will check that '
                                       'accepting or declining leads to the intended next step without '
                                       "confusing the customer's purchase decision.",
                             'example': 'I will place wording near the upsell acceptance button explaining '
                                        'that clicking it charges the buyer, and I will provide a separate '
                                        'refusal button. I will inspect both routes before release. The '
                                        'extra offer should make the next purchase understandable rather '
                                        'than rely on a buyer mistaking a charge button for ordinary '
                                        'navigation. [Marketing Mark — 0u4Tmd6BlWA @ 00:02:08]'},
                            {'name': 'complete_purchase_and_delivery_test',
                             'type': 'textarea',
                             'prompt': 'Describe the test order that will verify the checkout and '
                                       'additional offers together. Record the selected products, prices '
                                       'shown, route taken, and access received, then identify how you '
                                       'will handle a mismatch instead of declaring success because an '
                                       'individual preview page looks correct.',
                             'example': 'I will place a test order through checkout and the additional '
                                        'offers, recording what I selected, what the pages charged, and '
                                        'which products became accessible. Any mismatch will remain an '
                                        'unresolved release issue. Funnel Building Secrets calls for a '
                                        'test order, so checking page appearance alone will not close this '
                                        'verification step. [Funnel Building Secrets — BZ4rml1tc1U @ '
                                        '00:01:49]'}],
                 'completion_gate': 'Proceed only when payment responsibilities, tax activation, '
                                    'eligibility, payout timing, and required delivery functions are '
                                    'documented. The checkout must show the intended prices, the upsell '
                                    'must disclose its charging action and offer refusal, and an actual '
                                    'test order must confirm routing and purchased access. Unconfirmed '
                                    'migration terms and failed fulfillment checks remain explicit '
                                    'blockers.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Design the Acquisition Funnel and Prove Its Economics',
                 'purpose': 'Connect a quickly usable entry product to related offers, specify the '
                            'recovery window, and evaluate advertising against complete customer spending. '
                            'Keep practitioner results separate from your own operating evidence, and '
                            'identify the checkout, tracking, and consumption problems that can undermine '
                            'apparent success.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ["Describe the buyer's first useful result before choosing an entry "
                                  'price, advertising angle, or additional offer. Keep every product in '
                                  'the sequence connected to that result.',
                                  'Map the entry offer, order bump, upsells, acceptance routes, refusal '
                                  'routes, and delivery. State which transactions belong in your initial '
                                  'order calculation.',
                                  'Calculate average cart value and acquisition cost from the same buyer '
                                  'group. Declare whether your recovery requirement is immediate or allows '
                                  'several days.',
                                  'Separate advertising tests by angle, inspect what the purchase pixel '
                                  'records, and compare entry-price experiments using downstream purchases '
                                  'rather than entry conversion alone.',
                                  'Complete the worksheet with proposed decisions and actual observations '
                                  'clearly distinguished. Do not approve additional spending while '
                                  'essential checkout or measurement questions remain unresolved.'],
                 'fields': [{'name': 'entry_result_and_consumption',
                             'type': 'textarea',
                             'prompt': 'Describe the small result your entry product delivers, the '
                                       'materials required to reach it, and how the buyer will recognize '
                                       'completion. Explain why the product can be consumed quickly enough '
                                       'to support a relevant next purchase rather than delaying progress.',
                             'example': 'Proposed entry offer: a deeper version of one useful lesson, '
                                        'packaged with extra downloads rather than a long challenge. The '
                                        'buyer should finish the lesson and use one download before '
                                        'receiving the next invitation. Max packaged an expanded recording '
                                        'into a $7 offer; that example supports packaging, not a promised '
                                        'conversion rate. [Max Auren — kmRwEjvxk-w @ 00:05:14]'},
                            {'name': 'related_offer_stack',
                             'type': 'textarea',
                             'prompt': 'List the entry product, one order bump, and two possible upsells '
                                       'in their intended order. For each addition, explain the next buyer '
                                       'problem it solves and why it belongs beside the opening purchase '
                                       'rather than serving an unrelated audience.',
                             'example': 'Proposed stack: an opening strategy lesson, a related tool '
                                        'download, an implementation system, and a deeper support offer. '
                                        'Each addition must help the same buyer apply the opening lesson. '
                                        'I will begin with one bump and two upsells, not add offers simply '
                                        "to lengthen checkout or imitate somebody else's reported order "
                                        'value. [Maria Wendt — zQQZEPMxT6U @ 00:08:35]'},
                            {'name': 'average_cart_value_calculation',
                             'type': 'textarea',
                             'prompt': 'Specify which sales, bumps, upsells, and downsells enter your '
                                       'average cart value calculation. Identify the buyer count used as '
                                       'the denominator, then distinguish the resulting average from the '
                                       'advertised entry price so that acquisition decisions use the '
                                       'complete order picture.',
                             'example': 'My calculation will add entry sales, accepted bumps, upsells, and '
                                        'downsells, then divide that total by the number of buyers. '
                                        'Montoya reports a rounded $45 average cart value, which is not '
                                        'their $5 entry price. I will leave my own average unconfirmed '
                                        'until the included transactions and buyer count are available. '
                                        '[Jonathan Montoya — lJzDn-Qma9o @ 00:11:00]'},
                            {'name': 'cash_recovery_window',
                             'type': 'textarea',
                             'prompt': 'Choose whether this funnel must recover acquisition spending '
                                       'immediately or within several days. Explain which purchases count '
                                       'within that window, how you will compare acquisition cost with '
                                       'customer spending, and what evidence would prevent you from '
                                       'describing the funnel as self-liquidating.',
                             'example': 'Proposed rule: judge recovery from the initial order rather than '
                                        'assuming a later coaching sale will cover a shortfall. Fazio '
                                        'reports roughly $2,000 to $2,500 acquisition cost against about '
                                        '$2,500 initial order value. Those are their economics; my funnel '
                                        'remains unproven until its own acquisition cost and initial '
                                        'spending can be compared. [Daniel Fazio — By4MPc6yyFA @ '
                                        '00:05:13]'},
                            {'name': 'checkout_permission_and_routing',
                             'type': 'textarea',
                             'prompt': 'Write the acceptance and refusal routes for every additional '
                                       'offer, including the wording that makes a one-click charge '
                                       'explicit. Identify how an accepted purchase avoids a discounted '
                                       'version of itself and record whether the payment connection '
                                       'supports the intended checkout behavior.',
                             'example': 'Proposed acceptance copy will explain that clicking purchases the '
                                        'additional product, with a separate refusal choice. An accepted '
                                        'upsell will lead to the next different offer, not its own '
                                        'discounted alternative. I will inspect both routes before '
                                        'treating the sequence as ready; Montoya specifically warns '
                                        'against purchases that customers did not intend. [Jonathan '
                                        'Montoya — g9_sJ3XLyHs @ 00:33:31]'},
                            {'name': 'advertising_angle_test',
                             'type': 'textarea',
                             'prompt': 'Describe the advertising angles you will test, the visible product '
                                       'presentation, and the price disclosure. Assign each angle its own '
                                       'test budget, explain how you will avoid under-testing an angle, '
                                       'and define which purchase evidence matters more than attention '
                                       'alone.',
                             'example': 'Proposed creative will show the product mockup and state its '
                                        'price so visitors understand that an offer is being sold. Each '
                                        'angle will receive a separate test budget rather than compete for '
                                        'uneven campaign allocation. I will compare purchases, not declare '
                                        'success because one angle generates attractive click activity '
                                        "without buyers. [Sam O'Halloran — xglFE-qJgUY @ 00:03:06]"},
                            {'name': 'purchase_tracking_reconciliation',
                             'type': 'textarea',
                             'prompt': 'Record what your purchase pixel actually captures and compare that '
                                       'scope with the transactions included in your order totals. '
                                       'Identify any missing bump or upsell value, explain how that '
                                       'omission changes interpretation, and state which advertising '
                                       'conclusions must wait for reconciliation.',
                             'example': 'My review will compare the displayed purchase value with the '
                                        "entry product and any accepted additions. O'Halloran found that "
                                        'their pixel recorded only a $17 entry sale and missed order-bump '
                                        'value. If the same gap appears here, I will correct the '
                                        'interpretation before using displayed advertising returns to '
                                        "judge the whole funnel. [Sam O'Halloran — xglFE-qJgUY @ "
                                        '00:16:12]'},
                            {'name': 'entry_price_comparison',
                             'type': 'textarea',
                             'prompt': 'Define an entry-price comparison that includes entry purchases, '
                                       'average cart value, and participation in later offers. Explain '
                                       'what would justify keeping the new price, what would justify '
                                       'restoring the earlier price, and why additional upfront cash alone '
                                       'cannot settle the decision.',
                             'example': 'I will compare the complete purchase sequence before keeping a '
                                        'higher entry price. McAdam reports that $47 collected more '
                                        'upfront cash but reduced upsell participation compared with $27. '
                                        'My decision will therefore include downstream orders and '
                                        'acquisition recovery, rather than treating a larger opening '
                                        'payment as automatic evidence of a better funnel. [Jamie McAdam — '
                                        'Ck6CfmXv244 @ 00:03:46]'},
                            {'name': 'consumption_and_followup',
                             'type': 'textarea',
                             'prompt': 'Describe how buyers will be encouraged to consume the opening '
                                       'product and how follow-up will connect that use to the next '
                                       'relevant offer. Separate immediate purchase opportunities from '
                                       'slower buyer development, and identify what you will inspect when '
                                       'upgrades fail to appear.',
                             'example': 'Proposed follow-up will ask whether the buyer has used the ebook '
                                        'before repeating an upgrade invitation. McAdam describes buyers '
                                        'becoming warmer after a slow journey of roughly four months. I '
                                        'will distinguish a consumption delay from a checkout failure and '
                                        'avoid presenting that reported timeline as a guaranteed schedule '
                                        'for my buyers. [Jamie McAdam — Ck6CfmXv244 @ 00:11:09]'},
                            {'name': 'scaling_decision',
                             'type': 'textarea',
                             'prompt': 'Write the conditions for increasing advertising spend after the '
                                       'initial tests. Include acquisition cost, additional customer '
                                       'spending, the chosen recovery window, and unresolved operational '
                                       'problems. Explain how you will recognize that reaching colder '
                                       'audiences has weakened the economics rather than merely increased '
                                       'volume.',
                             'example': 'Proposed scaling rule: increase spending only when the additional '
                                        'acquisition still returns additional money within the chosen '
                                        'recovery window. Pole warns that acquisition costs rise as '
                                        'audiences become colder. I will not assume that an earlier '
                                        'profitable batch proves a larger batch will work, and unresolved '
                                        'checkout or tracking gaps will remain blockers. [Jan Pole — '
                                        'J5lslxUECxE @ 00:05:05]'}],
                 'completion_gate': 'Complete all ten fields, trace acceptance and refusal routes, '
                                    'identify the payment connection, and reconcile the purchase-value '
                                    'scope. Approve an acquisition test only when the recovery window and '
                                    'complete-order calculation are explicit. Approve scaling only when '
                                    'actual additional spending supports the decision; practitioner '
                                    'revenue claims are not substitutes for your own results.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Build the Membership and Learning Delivery Operating Plan',
                 'purpose': 'Choose a community and course-delivery structure that members can navigate '
                            'and the operator can sustain. Translate onboarding, access, interaction, '
                            'pricing, capacity, and launch decisions into a practical plan that '
                            'prioritizes implementation over an expanding library of lessons.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Select the community structure and learning delivery model separately. '
                                  "Explain how each choice supports the member's intended progress and "
                                  'your available operating attention.',
                                  "Write the member's first three days in sequence, including the welcome, "
                                  'roadmap, useful first action, personal contact, and accountability '
                                  'check.',
                                  'Map paid access, upgrade navigation, cancellation follow-up, and '
                                  'ongoing interaction. Distinguish currently available personal attention '
                                  'from support that can continue as membership grows.',
                                  'Plan cohort milestones, implementation time, and enrollment capacity '
                                  'using recent audience growth rather than the largest historical launch '
                                  'or total accumulated audience.',
                                  'Inspect actual student access and identify any launch materials that '
                                  'require changes before evergreen reuse. Record unresolved platform '
                                  'behavior or pricing questions instead of assuming they are settled.'],
                 'fields': [{'name': 'community_structure_choice',
                             'type': 'textarea',
                             'prompt': 'Choose one paid community, a limited free community leading to '
                                       'paid access, or an email list alongside the paid offer. Explain '
                                       'the work required by your choice, including posts, messages, and '
                                       'calls, and identify what you are deliberately not opening.',
                             'example': 'Proposed structure: one paid group, with an email list serving '
                                        'people who are not ready to join. I will not open a second free '
                                        'room unless I can handle its posts, messages, and possible calls. '
                                        "O'Neill describes each extra community as another job, making "
                                        "simplicity the better fit for this operating plan. [Brian O'Neill "
                                        '— TBf_yWZQ0e4 @ 00:00:33]'},
                            {'name': 'paid_access_and_upgrade_path',
                             'type': 'textarea',
                             'prompt': 'Map what a paying member receives immediately and where they can '
                                       'find any upgrade options. Identify the classroom, courses, events, '
                                       'or tier restrictions that require configuration, then describe how '
                                       'you will inspect the member experience rather than rely on a '
                                       'successful payment alone.',
                             'example': 'For a proposed Whop subscription, I will explicitly enable the '
                                        "courses app in the product's app configuration and inspect "
                                        'whether the purchased membership includes classroom access. A '
                                        'payment confirmation will not stand in for that inspection. '
                                        "Leonard's demonstration connects the subscription to the learning "
                                        'area through this configuration step rather than assuming access '
                                        'follows automatically. [Guides by Leonard — UVDszvU8i0o @ '
                                        '00:02:51]'},
                            {'name': 'three_day_member_activation',
                             'type': 'textarea',
                             'prompt': 'Write the first three days of membership as an ordered activation '
                                       'path. Include the welcome post, onboarding video or roadmap, first '
                                       'useful action, customer-success message, and accountability '
                                       'contact, making each step clear enough that a confused new member '
                                       'knows what to do next.',
                             'example': 'Proposed activation: day one provides a welcome post, roadmap, '
                                        'and clear first action; day two brings a customer-success '
                                        'message; day three adds a support accountability check. Pilditch '
                                        'used this sequence with one month of their SaaS as the quick win. '
                                        'I will choose a relevant first action rather than imply that '
                                        'every membership needs that bonus. [Adnan Pilditch — mf1WAw0FyaI '
                                        '@ 00:03:13]'},
                            {'name': 'inactivity_and_cancellation_review',
                             'type': 'textarea',
                             'prompt': 'Describe how you will notice early inactivity, contact members who '
                                       'have not started, and learn from cancellations. Separate unclear '
                                       'onboarding from insufficient content, and specify the repair you '
                                       'will try before assuming that another course or lesson will solve '
                                       'the retention problem.',
                             'example': 'Proposed repair sequence: clarify the onboarding video and '
                                        'ordered roadmap, then message members after 48 hours of '
                                        'inactivity. I will investigate confusion before adding lessons. '
                                        'Pilditch reports reducing churn from 17% to 11% after onboarding '
                                        'and engagement repairs; those figures describe their experience, '
                                        'not the reduction I can promise for this group. [Adnan Pilditch — '
                                        'mf1WAw0FyaI @ 00:02:56]'},
                            {'name': 'recurring_support_commitment',
                             'type': 'textarea',
                             'prompt': 'Define the recurring interaction members can expect, including '
                                       'question collection, live support, and recording follow-up. State '
                                       'which personal attention is available at the current group size '
                                       'and which support promise must remain sustainable if enrollment '
                                       'grows beyond your initial operating capacity.',
                             'example': 'Proposed support includes collecting questions before a Q&A and '
                                        'directing absent members to the relevant recording segment '
                                        'afterward. I will describe this repeatable process separately '
                                        'from unusually close founding-member attention. Boughton says '
                                        'their personal attention below 100 standard members cannot be '
                                        'promised indefinitely, so the ongoing offer will not depend on '
                                        'unlimited individual access. [Doug Boughton — 8lz_gy-Osw8 @ '
                                        '00:18:46]'},
                            {'name': 'membership_pricing_change',
                             'type': 'textarea',
                             'prompt': 'Record the proposed membership price or tier change, who receives '
                                       'each level of access, and how existing members are affected. '
                                       'Explain the downgrade implications of introducing a free option '
                                       'and identify whether a successful paid group actually needs the '
                                       'proposed pricing-model change.',
                             'example': 'Proposed decision: keep the existing paid structure until I can '
                                        "explain the new tier's purpose and its effect on current members. "
                                        'I will not select a free pricing model merely to experiment with '
                                        'acquisition. Skool News warns that this choice lets paying '
                                        'members downgrade and notes that an already successful paid group '
                                        'may need no change. [Skool News — Oeug9IgSFXc @ 00:24:58]'},
                            {'name': 'learning_delivery_model',
                             'type': 'textarea',
                             'prompt': 'Choose live cohort, on-demand instruction with live support, '
                                       'rolling launches, or evergreen delivery. Explain why that model '
                                       'fits the learning outcome and workload, what must be tested before '
                                       'automation, and which parts require interaction rather than simply '
                                       'transferring information through recorded lessons.',
                             'example': 'Proposed starting model: teach the first version live with only '
                                        'the initial material prepared, then use the response to decide '
                                        'what deserves fuller production. Rava recommends creating a '
                                        'little content before launch and checking interest. This approach '
                                        'leaves room to adjust the learning path instead of treating an '
                                        'untested recorded library as a finished solution. [Christina Rava '
                                        '— 75qWaUNMrnA @ 00:02:12]'},
                            {'name': 'cohort_milestones_and_implementation',
                             'type': 'textarea',
                             'prompt': "Outline the cohort's learning milestones, live implementation "
                                       'opportunities, and catch-up time. Identify the work students must '
                                       'complete between sessions and explain how the schedule gives them '
                                       'room to apply the material instead of continually receiving new '
                                       'lessons without finishing earlier assignments.',
                             'example': 'Proposed eight-week schedule includes an implementation week in '
                                        'week four, with no new material or live sessions during that '
                                        'interval. Students use the time to finish earlier work before '
                                        'continuing. Martin uses this structure to make room for '
                                        'application and catch-up; I will make that purpose explicit '
                                        'rather than describe the quieter week as missing delivery. [Lydia '
                                        'Martin | Your Online Business Mentor — vGWZU-6bK0Y @ 00:03:42]'},
                            {'name': 'cohort_capacity_and_price_response',
                             'type': 'textarea',
                             'prompt': 'Estimate cohort size from recent audience growth and explain how '
                                       'expenses fit that expected enrollment. Record the price assumption '
                                       'separately, identify evidence that would challenge it, and avoid '
                                       'using either the largest past launch or a tuition increase as '
                                       'automatic proof of stronger economics.',
                             'example': 'My enrollment plan will examine what a 1% to 3% capture of recent '
                                        'audience growth would produce, then size expenses for that cohort '
                                        'rather than the total audience accumulated over years. Lackey '
                                        'uses this question to plan for post-peak demand. The estimate '
                                        'will remain a planning assumption until actual enrollment '
                                        'provides a comparison. [Jessica Lackey — he4Uj-EhNfI @ 00:20:01]'},
                            {'name': 'access_and_evergreen_readiness',
                             'type': 'textarea',
                             'prompt': 'List the access checks and launch-material changes required before '
                                       'reusing the course for another cohort or evergreen sales. '
                                       'Distinguish administrator previews from student access, identify '
                                       'dated videos or emails, and explain how changes will avoid '
                                       'disrupting learners already using the current version.',
                             'example': 'Before reusing a converting live launch, I will review its videos '
                                        'and emails and remove dates that would make automated delivery '
                                        'confusing. That editing is separate from checking what students '
                                        'can actually access. Darrington recommends repurposing proven '
                                        'launch materials into an automated introduction and follow-up '
                                        'sequence, not treating every live-launch asset as ready '
                                        'unchanged. [Brittany Darrington — LhSL-O1SNLs @ 00:04:18]'}],
                 'completion_gate': 'Complete all ten fields and document the first three member days, '
                                    'paid-access configuration, inactivity response, sustainable support '
                                    'promise, and delivery schedule. Confirm student access rather than '
                                    'relying on administrator previews. Hold pricing changes or evergreen '
                                    'conversion until their effects on existing members, dated materials, '
                                    'and operating capacity have been addressed.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Connect Newsletter Expertise and Faceless Content to Product Sales',
                 'purpose': 'Build a reader-focused publishing system that connects useful newsletter '
                            'issues and faceless demonstrations to relevant products. Plan discovery, '
                            'advertising, product validation, production checks, and purchase routing '
                            'while separating audience growth, attributed earnings, illustrative '
                            'arithmetic, and verified sales.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Name the reader and their recurring problem, then choose an issue '
                                  "format and faceless demonstration that make the product's usefulness "
                                  'visible without relying on follower counts.',
                                  'Select a discovery route and explain its workload or platform tradeoff. '
                                  'Treat reported acquisition shares as examples rather than guaranteed '
                                  'results for a new publication.',
                                  'Map newsletter advertising separately from product sales. Include offer '
                                  'suitability, publication deadlines, plan costs, and unresolved '
                                  'withdrawal requirements where they affect the chosen model.',
                                  'Inspect generated content before publication and follow the proposed '
                                  'buyer route through the description link, sales page, and intended '
                                  'checkout. Record faults instead of assuming embedded buttons work.',
                                  'Complete the evidence ledger with audience figures, sales, earnings, '
                                  'costs, and illustrative calculations in separate categories. Only '
                                  'describe outcomes that the available records actually support.'],
                 'fields': [{'name': 'reader_problem_and_positioning',
                             'type': 'textarea',
                             'prompt': "Define the reader's specific problem, the useful change your "
                                       'publication helps them make, and the recurring questions that '
                                       'indicate demand. Explain how comments or conversations will refine '
                                       'the offer before you decide that readers want a course, coaching '
                                       'program, or paid subscription.',
                             'example': 'Proposed research begins with readers who repeatedly comment '
                                        'about the same obstacle. I will ask about their goals, current '
                                        'work, and what blocks progress before presenting an offer. Write '
                                        '• Build • Scale recommends turning recurring comments into '
                                        'direct-message conversations rather than immediately pitching, '
                                        'giving the publication a clearer problem to address in its next '
                                        'issue. [Write • Build • Scale — HDQk5g412yI @ 00:07:05]'},
                            {'name': 'repeatable_issue_workflow',
                             'type': 'textarea',
                             'prompt': 'Describe a repeatable newsletter format, a clear title and '
                                       'subtitle, and the drafting routine that keeps publication '
                                       'manageable. Identify which parts require editorial judgment and '
                                       'when the working process is stable enough to save for reuse rather '
                                       'than redesigning every issue.',
                             'example': 'Proposed routine: keep the title clear, make the subtitle explain '
                                        'the opening benefit, and reuse a consistent issue structure once '
                                        'it works. Only then will I save the drafting process as a Claude '
                                        'skill. The Dope Act publisher describes this kind of repeatable '
                                        'workflow, including preparing a Friday edition on Friday morning. '
                                        '[beehiiv — a-8NoqWX86M @ 00:04:34]'},
                            {'name': 'newsletter_discovery_tradeoff',
                             'type': 'textarea',
                             'prompt': 'Choose the primary discovery route for the newsletter and explain '
                                       'the platform tradeoff it creates. Separate social distribution, '
                                       'recommendations, and internal platform discovery from '
                                       'monetization, and describe what acquisition evidence would justify '
                                       'accepting a revenue share or paying for the selected publishing '
                                       'setup.',
                             'example': 'I will evaluate discovery alongside platform cost rather than '
                                        'choose solely from a fee comparison. Cole reports that over half '
                                        "of Write With AI's readers came from inside Substack's ecosystem. "
                                        'That explains their willingness to accept its revenue share, but '
                                        'I will not assume a new publication receives the same acquisition '
                                        'benefit. [Nicolas Cole — RaVsgiJeovE @ 00:12:49]'},
                            {'name': 'advertising_offer_calendar',
                             'type': 'textarea',
                             'prompt': 'Document how you will select suitable newsletter advertisements, '
                                       'schedule them inside the claimed publication window, and handle a '
                                       'changed issue date. Include the reason for rejecting poor matches '
                                       'and identify the person or workflow responsible for moving or '
                                       'canceling an advertisement before its deadline.',
                             'example': 'Proposed ad calendar will pair each claimed offer with an '
                                        'intended issue and its publication deadline. The offers tutorial '
                                        'describes up to five simultaneous claims and five days to '
                                        'publish. If the issue moves, I will move or cancel the '
                                        'advertisement rather than let the old plan silently expire or '
                                        'assume the claim remains usable indefinitely. [beehiiv — '
                                        'ELxfeUy81Vk @ 00:00:57]'},
                            {'name': 'newsletter_net_economics',
                             'type': 'textarea',
                             'prompt': 'Compare expected advertising receipts with the publishing plan '
                                       'bill using the same subscriber count and billing cadence. Record '
                                       'withdrawal requirements separately, distinguish reported earnings '
                                       'from after-cost profit, and explain what would make advertising an '
                                       'insufficient reason to maintain the chosen paid plan.',
                             'example': 'My comparison will place advertising receipts and software '
                                        'charges beside each other at the same list size and billing '
                                        'cadence. Stack Receipts shows $39 at 1,000 subscribers falling '
                                        'below both quoted Light prices. I will not call that arrangement '
                                        'profitable merely because an advertising payment exists, and '
                                        'unresolved withdrawal requirements will stay visible in the plan. '
                                        '[Stack Receipts — fd2DFt_F31U @ 00:05:30]'},
                            {'name': 'expertise_offer_and_homework',
                             'type': 'textarea',
                             'prompt': 'Select a product, mini course, coaching offer, or short live '
                                       "cohort that addresses the reader's established problem. State the "
                                       'promised outcome, the assignments required to reach it, and the '
                                       'change you will make if completing those assignments cannot '
                                       'realistically deliver the promised transformation.',
                             'example': 'Proposed offer: a short live cohort focused on one reader '
                                        'problem, with assignments that directly produce the stated '
                                        'result. I will review the homework before expanding the sales '
                                        'promise. McGarry says the program must improve or promise less '
                                        'when completing the assignments cannot realistically achieve the '
                                        'outcome; reported cohort revenue does not remove that obligation. '
                                        '[Matt McGarry - GrowLetter — 1JVlUJAc6to @ 00:14:26]'},
                            {'name': 'faceless_demonstration_plan',
                             'type': 'textarea',
                             'prompt': 'Choose a faceless content format that demonstrates the product '
                                       'solving a real buyer problem. Describe what appears on screen, '
                                       'what the narration explains, and how the title and thumbnail work '
                                       'together, keeping the presentation focused on usefulness rather '
                                       'than anonymous content volume.',
                             'example': 'Proposed video will show a digital planner on a tablet while a '
                                        'screen recording demonstrates how it works. Narration will '
                                        'explain the useful steps rather than rely on a visible presenter. '
                                        'Success With Sam describes this product demonstration format, '
                                        'which lets the viewer see the item in use before considering the '
                                        'related purchase. [Success With Sam — H3AW2eLqDt4 @ 00:01:54]'},
                            {'name': 'generated_content_quality_check',
                             'type': 'textarea',
                             'prompt': 'List the visual, text, voiceover, and presentation checks required '
                                       'before publishing generated faceless content. Explain how you will '
                                       'handle awkward overlays or additional production costs, and '
                                       'specify which editing tasks can move into the social platform when '
                                       'the generated version does not work.',
                             'example': 'Before publication, I will preview the complete video, inspect '
                                        'text placement, and check whether the overlay obscures important '
                                        'visual material. Rochelle encountered text covering a face and '
                                        'additional credit use when adding voiceover. If the generated '
                                        'text treatment remains awkward, I will move that work into the '
                                        'social platform rather than publish the unchecked version. '
                                        '[Rochelle Be — lfsfJDOVCV4 @ 00:09:47]'},
                            {'name': 'content_to_checkout_path',
                             'type': 'textarea',
                             'prompt': 'Write the route from useful content to the product description, '
                                       'sales page, and intended checkout. Include the outcome stated near '
                                       'the link, the purchase button inspection, and any '
                                       'affiliate-product review needed before recommending an offer whose '
                                       'refunds could remove your commission.',
                             'example': 'Proposed buyer route places a relevant product link prominently '
                                        'in the description, then sends the visitor to the intended sales '
                                        'page. I will press the purchase button in live preview and '
                                        'confirm the destination. Brem performs this check after embedding '
                                        'Gumroad into Framer, so a visible button alone will not count as '
                                        'a working sales route. [Brem — I5oEOJ8u02s @ 00:11:09]'},
                            {'name': 'audience_and_sales_evidence',
                             'type': 'textarea',
                             'prompt': 'Create separate entries for views, followers, product purchases, '
                                       'attributed earnings, costs, and illustrative conversion '
                                       'arithmetic. Explain which entries are observed, which remain '
                                       'untested, and what additional evidence is needed before describing '
                                       'a faceless content experiment as a functioning digital product '
                                       'sales system.',
                             'example': 'My evidence ledger will separate reach from purchases and leave '
                                        'monetization unconfirmed until sales are recorded. DIGITAL INCOME '
                                        'PROJECT reports 10,000 followers and over 500,000 views in 30 '
                                        'days, then says monetization is still being tested. I will '
                                        'preserve that distinction instead of relabeling audience growth '
                                        'as product revenue or using it to imply a sales forecast. '
                                        '[DIGITAL INCOME PROJECT — h_KMRUYNThE @ 00:12:01]'}],
                 'completion_gate': 'Complete all ten fields, document a repeatable issue format, and '
                                    'connect a specific reader problem to a relevant offer. Resolve '
                                    'claimed-ad deadlines and compare receipts with matching plan costs. '
                                    'Inspect the generated content and checkout destination. Keep '
                                    'monetization unproven wherever only audience results, practitioner '
                                    'claims, or illustrative arithmetic are available.'}]}
