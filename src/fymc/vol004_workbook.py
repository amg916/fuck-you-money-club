from __future__ import annotations

def build_volume_004_workbook() -> dict:
    return {'workbook_id': 'wb-004-ai-powered-micro-saas',
 'volume_id': 'vol-004-ai-powered-micro-saas',
 'title': 'AI-Powered Micro SaaS — Practitioner Testimony Operator Workbook',
 'subtitle': 'Choose a narrow customer problem, validate a focused vertical offer, launch with tested '
             'tenant isolation, and build recurring value around measured AI costs, reliable delivery, and '
             'sustainable customer economics.',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Select a Narrow Problem and a Defensible Vertical Offer',
                 'purpose': 'Turn a familiar manual workflow or dissatisfied customer segment into a '
                            'specific offer. Establish outside demand, a reachable buyer, a credible '
                            'switching demonstration, and delivery economics before committing to '
                            'development or accepting advance payment.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ["Describe the customer's recurring problem before naming features, "
                                  'models, or an ambitious product category.',
                                  'Separate observations from assumptions, and seek confirmation outside '
                                  'the workplace where the problem first appeared.',
                                  'Explore one buyer segment at a time, recording purchasing behavior '
                                  'rather than combining unrelated expressions of interest.',
                                  'Connect the proposed outcome to an actual acquisition route, a visible '
                                  'switching demonstration, and a bounded delivery promise.',
                                  'Finish with a proceed, revise, or pause decision supported by customer '
                                  'evidence, workflow depth, and realistic delivery costs.'],
                 'fields': [{'name': 'problem_and_current_work',
                             'type': 'textarea',
                             'prompt': 'Describe one recurring task, the person performing it, and the '
                                       'current manual process. Explain what makes the work painful '
                                       'without proposing a feature list. Record the observable effort or '
                                       'repeated inconvenience that makes this problem worth investigating '
                                       'first.',
                             'example': 'Candidate problem: application packaging requires repeated '
                                        'preparation and verification before an installation succeeds. '
                                        'Thomas describes a process that can take an hour. I would '
                                        'investigate that specific preparation burden rather than pitch a '
                                        'broad automation platform, and ask other practitioners whether '
                                        'their packaging work creates the same repeated delay. [Starter '
                                        'Story — LRX8TWC2hTM @ 00:02:18]'},
                            {'name': 'outside_workplace_validation',
                             'type': 'textarea',
                             'prompt': 'Identify how you will check whether the problem exists beyond your '
                                       'own employer or personal workflow. List the outside buyers to '
                                       'approach, the behavior to investigate, and the evidence that would '
                                       'reveal a workplace peculiarity rather than a market.',
                             'example': 'My validation note would distinguish an internal frustration from '
                                        'a repeated problem across other businesses. I would ask outside '
                                        'operators how they currently complete the task and whether they '
                                        'have sought alternatives. Rob Walling warns that an employer can '
                                        'be uniquely dysfunctional; internal inconvenience alone would not '
                                        'justify proceeding. [Rob Walling — 6sgCo6fMSGY @ 00:05:32]'},
                            {'name': 'mechanical_and_judgment_steps',
                             'type': 'textarea',
                             'prompt': 'Map the workflow from its initial input to its finished result. '
                                       'Label each step as mechanical work or judgment, and explain which '
                                       'bounded sequence the first product will handle. Preserve the '
                                       'decisions that require customer understanding instead of promising '
                                       'total automation.',
                             'example': 'The first workflow document would list each action precisely, '
                                        'then distinguish repeatable handling from decisions that depend '
                                        'on context. I would select the mechanical sequence for the '
                                        'initial offer and keep judgment steps explicit. Greg Isenberg '
                                        'recommends documenting every step and separating judgment from '
                                        'mechanical tasks before choosing what to automate. [Greg Isenberg '
                                        '— 9T1yWEq5kP0 @ 00:13:12]'},
                            {'name': 'competitor_complaint_pattern',
                             'type': 'textarea',
                             'prompt': 'Collect repeated complaints about existing products from '
                                       'competitor review pages, public roadmaps, and customer '
                                       'communities. Compare these complaints with requests reaching your '
                                       'own support conversations. Identify the narrow dissatisfaction you '
                                       "could address without reproducing the competitor's entire product "
                                       'scope.',
                             'example': 'My complaint record would group matching requests from '
                                        'Trustpilot, public roadmaps, and Discord, then compare them with '
                                        'incoming support questions. A feature request appearing only once '
                                        'would remain uncertain. The operators describing this process '
                                        'looked across all three competitor channels rather than choosing '
                                        'a product direction from one isolated comment. [Starter Story — '
                                        'Nnpz1wsTjBI @ 00:08:10]'},
                            {'name': 'switching_demonstration',
                             'type': 'textarea',
                             'prompt': 'Specify a demonstration that shows a customer moving from their '
                                       'existing workflow to the desired result. Name the starting '
                                       'artifact, the visible transformation, and the completed output. '
                                       'Explain how this demonstration makes switching tangible rather '
                                       'than merely advertising a cheaper alternative.',
                             'example': 'A form alternative could show the switch directly: the visitor '
                                        'pastes an existing Typeform URL and sees a replacement form '
                                        'appear within seconds. Abhishek uses this approach on the landing '
                                        'page. My demonstration brief would prioritize that observable '
                                        'transformation over a long feature comparison or an unsupported '
                                        'promise of effortless migration. [Starter Story — _KaFS4Dxs5k @ '
                                        '00:03:36]'},
                            {'name': 'distribution_before_building',
                             'type': 'textarea',
                             'prompt': 'Name where prospective customers already look for help and how '
                                       'your offer will reach them. Describe the content or conversation '
                                       'that connects their problem to your outcome. Record what remains '
                                       'unproven about this route before assigning time to product '
                                       'development.',
                             'example': 'My acquisition brief would name the customer source before the '
                                        'development plan. It would explain which existing audience has '
                                        'the problem and what message would bring them to a demonstration. '
                                        'Fomin puts demand and traffic ahead of building, so an impressive '
                                        'application would not count as an acquisition strategy by itself. '
                                        '[Fomin Unscripted — 8lmA9UgwNQs @ 00:03:11]'},
                            {'name': 'serial_vertical_selection',
                             'type': 'textarea',
                             'prompt': 'Choose the first vertical to investigate and explain why its '
                                       'buyers are accessible and understandable. State which buying '
                                       'behaviors you will compare before moving to another segment. Keep '
                                       'alternative segments queued rather than running many unrelated '
                                       'investigations at the same time.',
                             'example': 'I would investigate one buyer segment, record how its operators '
                                        'evaluate and purchase a solution, and only then compare another '
                                        'segment. The decision record would preserve differences instead '
                                        'of averaging them together. Jordan Crawford explicitly advises '
                                        'exploring serially rather than trying ten segments '
                                        'simultaneously, keeping each investigation interpretable before '
                                        'the next begins. [Jordan Crawford (Blueprint) — RINTsdOTWfc @ '
                                        '00:07:14]'},
                            {'name': 'specialized_execution_depth',
                             'type': 'textarea',
                             'prompt': 'Describe the specialized workflow knowledge and evaluation work '
                                       'required beyond a thin model interface. Identify individual '
                                       'stages, their expected outputs, and how you will check changes '
                                       'against previous examples. Explain what customer understanding '
                                       'should improve as the product is used.',
                             'example': 'For a specialized workflow, I would write expected outputs for '
                                        'individual stages before tuning prompts. A search stage would '
                                        'have gold-standard queries rather than only a final answer judged '
                                        'informally. Jake Heller describes this approach; the resulting '
                                        'evaluation work would make workflow execution more concrete than '
                                        'a generic claim of industry expertise. [Y Combinator — '
                                        'eBVi_sLaYsc @ 00:23:51]'},
                            {'name': 'presale_delivery_commitment',
                             'type': 'textarea',
                             'prompt': 'If you plan to accept advance payment, define the exact '
                                       'deliverable, delivery deadline, and refund access. Separate money '
                                       'collected from work completed. Explain how you will communicate '
                                       'the commitment without allowing an expanding wishlist to replace '
                                       'the original promised outcome.',
                             'example': 'Gil reports selling 50 lifetime licenses for $20,000 before '
                                        'building Subscribr, with delivery promised within 60 days and '
                                        'refunds available for two weeks afterward. My presale record '
                                        'would state those categories explicitly: purchased outcome, '
                                        'delivery date, and refund window. Advance receipts would '
                                        'represent an obligation to deliver, not proof that delivery is '
                                        'finished. [Starter Story — 7KqlwjBM_tM @ 00:05:34]'},
                            {'name': 'price_and_delivery_economics',
                             'type': 'textarea',
                             'prompt': 'Compare the proposed price with the infrastructure and service '
                                       'effort needed to deliver the result. Identify what free usage '
                                       'could consume, what price adjustment might become necessary, and '
                                       'which evidence would make you revise the offer before adding more '
                                       'customers.',
                             'example': "Screenshot One's founder describes an early $7 offer leaving "
                                        'almost zero margins, followed by a smaller free plan and higher '
                                        'prices. I would therefore review free usage and delivery costs '
                                        'together before treating a low entry price as an advantage. The '
                                        'proposed offer must leave room to operate, not merely attract '
                                        'initial interest. [Starter Story — TCGXT7ySco8 @ 00:09:04]'}],
                 'completion_gate': 'Proceed only when one buyer and one painful workflow are named, '
                                    'outside validation is documented, an acquisition route is explicit, '
                                    'and the switching demonstration has a bounded outcome. Record '
                                    'remaining assumptions about specialized execution and margins. Do not '
                                    'accept a presale without a deliverable, deadline, and refund '
                                    'commitment that you are prepared to honor.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Prepare a Focused Launch and Test Tenant Isolation',
                 'purpose': 'Translate the chosen offer into a small working application with clear output '
                            'requirements, observable payment behavior, and tested data boundaries. '
                            'Allocate launch effort deliberately while preserving customer context, '
                            'support capacity, and visibility into costly usage.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Carry forward the selected buyer and problem; reject additions that '
                                  'turn the first release into a sprawling platform.',
                                  'Document expected application outputs, model access, payment behavior, '
                                  'and usage limits before calling the release ready.',
                                  'Exercise authorization through the actual application role rather than '
                                  'relying on privileged dashboard results.',
                                  'Test caller context, write permissions, related objects, and pooled '
                                  'access as distinct checks with recorded outcomes.',
                                  'Compare launch preparation with observed response, and keep support '
                                  'feedback connected to the people improving the product.'],
                 'fields': [{'name': 'first_release_output_contract',
                             'type': 'textarea',
                             'prompt': 'Define the useful result the first release must produce and list '
                                       'its required output elements. Describe how you will improve the '
                                       'existing implementation when an element is missing. Keep the scope '
                                       'tied to the original customer problem instead of restarting '
                                       'unnecessarily.',
                             'example': 'For an invoice converter, the output contract would include '
                                        'vendor, date, invoice number, description, quantity, price, and '
                                        'total. Mikey improves the existing application with that '
                                        'extraction structure rather than beginning again. My release '
                                        'checklist would examine those fields in the current build and '
                                        'record missing information as a focused refinement task. [Mikey '
                                        'No Code — aQZkra1kEcg @ 00:20:17]'},
                            {'name': 'model_gateway_and_budget',
                             'type': 'textarea',
                             'prompt': 'Describe how the application will access models and how spending '
                                       'will be bounded for the relevant keys. Record the operational '
                                       'reason for the selected gateway arrangement and the assumptions '
                                       'that require checking, rather than treating a broad provider '
                                       'comparison as settled.',
                             'example': 'The gateway decision would include a budget for each relevant key '
                                        'and a note explaining the intended scope. Paul Zuradzki describes '
                                        'assigning budgets per key, allowing granular control. I would '
                                        "record the configured budget alongside the application's model "
                                        'access instead of assuming that consolidating access '
                                        'automatically provides adequate spending boundaries for every '
                                        'workload. [Paul Zuradzki — Nk7qDiLHyuU @ 00:04:29]'},
                            {'name': 'published_checkout_verification',
                             'type': 'textarea',
                             'prompt': 'Write the payment journey you will test after publishing, '
                                       'including the free usage boundary and the transition to a paid '
                                       'plan. Specify what successful checkout must change inside the '
                                       'application and how you will record actual errors before declaring '
                                       'billing ready.',
                             'example': 'My checkout record would follow a published application through a '
                                        'test-card purchase and verify the resulting paid-plan update. It '
                                        "would also capture any errors encountered along the way. Mikey's "
                                        'launch process checks payment behavior in the working '
                                        'application, so a pricing page alone would not demonstrate that a '
                                        'customer can successfully upgrade. [Mikey No Code — aQZkra1kEcg @ '
                                        '00:23:40]'},
                            {'name': 'heavy_usage_boundary',
                             'type': 'textarea',
                             'prompt': 'Identify usage patterns that could cost more than the ordinary '
                                       'plan can support. Describe how you will spot those accounts and '
                                       'decide whether their consumption requires a different arrangement. '
                                       'Keep generous access separate from an unexamined promise to absorb '
                                       'unlimited delivery costs.',
                             'example': 'Tally encountered users exceeding 50,000 monthly submissions, '
                                        'with costs beyond what ordinary Pro pricing could cover, and '
                                        'introduced manually priced excessive usage. My plan review would '
                                        'therefore separate normal consumption from heavy outliers. I '
                                        'would document when an account needs individual pricing rather '
                                        'than assume the standard plan can absorb every workload. '
                                        '[MicroConf — Dt6HAEuwEug @ 00:31:20]'},
                            {'name': 'launch_effort_allocation',
                             'type': 'textarea',
                             'prompt': 'List the launch activities competing for your time and the '
                                       'response each should produce. Explain which activity you would '
                                       'reduce if attention remains low. Make room for clear positioning '
                                       'and earlier outreach instead of assuming a labor-intensive launch '
                                       'asset will attract viewers.',
                             'example': 'Jack Smith spent hours producing a bespoke Product Hunt video '
                                        'that received two views. My launch plan would therefore compare '
                                        'preparation time with actual audience response and reserve room '
                                        'for more engaging outbound content. A polished video would not '
                                        'automatically receive more time than activities that put the '
                                        'product before potential users. [Jack Smith — hJtOsLAfxxE @ '
                                        '00:09:04]'},
                            {'name': 'application_role_isolation_test',
                             'type': 'textarea',
                             'prompt': 'Define an isolation test using two tenants and a row whose '
                                       'ownership is known. State the application role used for the check '
                                       'and the expected denied result. Explain how you will avoid '
                                       'mistaking privileged database access for evidence that customer '
                                       'boundaries work.',
                             'example': 'The test would establish tenant A as the caller, request a known '
                                        'tenant B row, and expect no returned row. I would run it through '
                                        "the application's role rather than a privileged browsing session. "
                                        'Past The Diagram gives this concrete negative test, making an '
                                        'explicit cross-tenant request part of the verification record. '
                                        '[Past The Diagram — h1KAW_izGl8 @ 00:03:52]'},
                            {'name': 'transaction_scoped_caller_context',
                             'type': 'textarea',
                             'prompt': 'Describe how tenant or user context reaches database operations '
                                       'and how long that context remains active. For transaction-scoped '
                                       'access, state where context is established and when it ends. '
                                       'Identify any execution path that cannot rely on the ordinary '
                                       "request's caller information.",
                             'example': 'For the demonstrated Prisma approach, I would establish context '
                                        'inside a transaction using set_config with its local flag set to '
                                        'true. Alex Rusin explains that this behaves like SET LOCAL and '
                                        'reverts the value when the transaction ends. My implementation '
                                        'note would make that lifetime explicit rather than leave context '
                                        'persistence ambiguous. [Alex Rusin — ctJy5AxgVXM @ 00:05:48]'},
                            {'name': 'policy_and_related_object_review',
                             'type': 'textarea',
                             'prompt': 'Record the policies and related database objects that must respect '
                                       'the same authorization boundary. Include read behavior, permitted '
                                       'writes, views, and related counts. Explain how you will compare '
                                       'the interface with actual permitted actions rather than accept '
                                       'apparently correct screens.',
                             'example': 'My authorization review would include the email view and related '
                                        "folder counts, not just the base email table. Supabase's "
                                        'demonstration needed changes to view execution and email_folders '
                                        'before visible records and counts followed the intended rules. I '
                                        'would record these related checks separately instead of treating '
                                        'one enabled table as complete coverage. [Supabase — PdEutzhsrws @ '
                                        '00:10:37]'},
                            {'name': 'pooled_access_test_evidence',
                             'type': 'textarea',
                             'prompt': 'Describe how you will exercise isolation during pooled or '
                                       'concurrent access. Record the tested configuration, the failure '
                                       'mode being investigated, and the observed result. State the limits '
                                       'of the evidence so a successful run does not become a universal '
                                       'security claim.',
                             'example': 'Alex Rusin reports 800 concurrent requests with no contamination '
                                        'in the tested configuration. My verification record would retain '
                                        'that configuration and the specific context-leakage failure mode '
                                        'under examination. A comparable passing run would support only '
                                        'the exercised setup, not every possible pooling arrangement, '
                                        "database role, or future change to the application's access "
                                        'behavior. [Alex Rusin — ctJy5AxgVXM @ 00:07:51]'},
                            {'name': 'support_capacity_and_feedback',
                             'type': 'textarea',
                             'prompt': 'Describe how support questions will reach the product decision '
                                       'makers and how you will notice support displacing development. '
                                       'Define a response to an overloaded support channel while '
                                       'preserving customer context. Avoid treating outsourced support as '
                                       'permission to stop learning from users.',
                             'example': 'My operating note would track whether support is taking time away '
                                        'from building and whether customer context still reaches the '
                                        "founders. Marie describes both problems around Tally's support "
                                        'operations. Before expanding access to another support channel, I '
                                        'would review its workload and preserve a clear route from '
                                        'recurring questions to product improvements. [MicroConf — '
                                        'Dt6HAEuwEug @ 00:26:44]'}],
                 'completion_gate': 'Release only after the useful output and published checkout have been '
                                    'exercised, free and paid behavior are understood, and costly usage '
                                    'has an explicit review path. Require recorded isolation results '
                                    'through the application role, including caller context and related '
                                    'objects. Mark untested configurations as untested, and assign '
                                    'responsibility for launch response and support feedback.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Control AI Delivery Costs and Prove Sustainable Economics',
                 'purpose': 'Design caching and routing around measured behavior rather than headline '
                            'savings. Connect delivery spending to pricing, credit expiration, customer '
                            'payback, and recurring usefulness so launch attention and temporary subsidies '
                            'do not conceal an uneconomic product.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Separate reusable prompt input, changing context, and cached answers '
                                  'before selecting a cost-reduction technique.',
                                  'Compare routing costs with an explicit baseline, including '
                                  'classification, retries, and output quality checks.',
                                  'Attribute spending to the relevant user, tenant, or workload and '
                                  'connect heavy usage to plan economics.',
                                  'Treat startup credits as conditional, temporary support; document '
                                  'eligibility, expiration, and the unsubsidized bill.',
                                  'Review working functionality, customer retention, and acquisition '
                                  'recovery before interpreting launch enthusiasm as a viable business.'],
                 'fields': [{'name': 'stable_prompt_prefix',
                             'type': 'textarea',
                             'prompt': "Lay out the prompt's stable material and changing working context "
                                       'in their intended order. Explain which updates should affect only '
                                       'the tail and which would invalidate reusable input. State how you '
                                       'will preserve the expensive common prefix across repeated '
                                       'requests.',
                             'example': 'I would place the stable knowledge base before working memory, '
                                        'allowing memory updates to change the tail rather than the '
                                        'expensive prefix. Mastra specifically recommends this ordering. '
                                        'My prompt layout would identify both sections clearly so routine '
                                        'memory changes do not unnecessarily rewrite material that '
                                        'repeated requests could otherwise reuse through prompt caching. '
                                        '[Mastra — eBB0dBqfvuQ @ 00:03:08]'},
                            {'name': 'tool_and_configuration_stability',
                             'type': 'textarea',
                             'prompt': 'Identify tool definitions and configuration material that should '
                                       'remain stable across calls. Specify how names, ordering, schemas, '
                                       'and serialized keys will be handled. Describe where updates can be '
                                       'appended without unnecessarily rewriting reusable prompt content '
                                       'and undermining the intended caching behavior.',
                             'example': 'My reusable configuration would keep tool names, order, and '
                                        'schemas stable, with JSON keys sorted consistently. I would '
                                        'append configuration updates when appropriate instead of '
                                        'rewriting the existing reusable material. Vichu emphasizes these '
                                        'practices because avoidable prefix changes work against cache '
                                        "reuse, even when the application's overall task appears unchanged "
                                        'to the operator. [Learn with Vichu — rECbImLOxqg @ 00:12:48]'},
                            {'name': 'answer_cache_freshness',
                             'type': 'textarea',
                             'prompt': 'List answers whose correctness can change during normal use and '
                                       'describe their expiration requirements. Distinguish reusing input '
                                       'processing from serving a previously generated answer. Explain '
                                       'what would make a cached result unacceptable even when it saves '
                                       'time and model spending.',
                             'example': 'A cached balance cannot remain valid indefinitely when the '
                                        'underlying amount changes. Aman demonstrates a balance moving '
                                        'from 2,500 to 10,000 during the day. My cache note would '
                                        'therefore specify expiration for changing answers and treat a '
                                        'fast but stale response as incorrect, rather than count every '
                                        'avoided model call as a successful optimization. [AmanAI Lab — '
                                        'QaVJRXlOcV4 @ 00:06:00]'},
                            {'name': 'history_compaction_tradeoff',
                             'type': 'textarea',
                             'prompt': 'Describe the conversation history that accumulates during your '
                                       'workload and where compaction could be evaluated. Record the '
                                       'comparison conditions, summary size, and observed cost '
                                       'differences. Keep any proposed setting tied to the tested workload '
                                       'instead of assuming one threshold fits every application.',
                             'example': "Vichu's coding example uses 150 turns, adds 5,000 tokens per "
                                        'turn, and creates 10,000-token summaries. The 100,000-token '
                                        'setting produces eight compactions and a $24 comparison against '
                                        '$123 without compaction. I would preserve those conditions in the '
                                        'evaluation note rather than present the savings as a guaranteed '
                                        "outcome for a different application's history. [Learn with Vichu "
                                        '— rECbImLOxqg @ 00:11:04]'},
                            {'name': 'routing_quality_and_total_cost',
                             'type': 'textarea',
                             'prompt': 'Define the baseline and task set for evaluating model routing. '
                                       'Record output quality alongside classifier, answering model, and '
                                       'retry costs. Explain how you will handle borderline requests that '
                                       'choose different tiers across runs rather than reporting savings '
                                       'from one favorable execution.',
                             'example': "My routing comparison would include the classifier's cost and "
                                        'retries, then inspect the resulting answers. Hunter Sneed '
                                        'observed borderline requests selecting different model tiers '
                                        'across runs. I would retain those variations in the record '
                                        'instead of reporting only the cheapest execution or assuming that '
                                        'a lower-cost route always preserves the required result. [Hunter '
                                        'Sneed — raEBR_2VbXE @ 00:09:22]'},
                            {'name': 'spending_attribution',
                             'type': 'textarea',
                             'prompt': 'Choose the request tags needed to explain who or what consumes '
                                       'model spending. Connect user, tenant, workload, or department '
                                       'labels to the questions you need to answer. Describe how this '
                                       'attribution will reveal expensive patterns hidden inside an '
                                       'aggregate monthly bill.',
                             'example': 'I would tag gateway requests by tenant and workload so the cost '
                                        'review can distinguish ordinary use from an expensive recurring '
                                        'task. Hunter Sneed recommends request tags for users, tenants, '
                                        'workloads, or departments. The operating record would connect '
                                        'spending to those labels instead of presenting only a total that '
                                        'obscures which activity caused the increase. [Hunter Sneed — '
                                        'raEBR_2VbXE @ 00:09:22]'},
                            {'name': 'usage_sensitive_margin_review',
                             'type': 'textarea',
                             'prompt': 'Explain how increased model usage could alter the proposed '
                                       "subscription's economics. Identify the consumption you must "
                                       'measure and the pricing assumptions that depend on it. State what '
                                       'evidence would require a plan revision rather than celebrating '
                                       'revenue while delivery margins deteriorate.',
                             'example': 'My margin review would pair subscription revenue with actual '
                                        'language-model consumption and revisit the plan when heavier '
                                        'usage changes delivery costs. Business Mechanics warns that API '
                                        'spending can turn an apparent 80% gross-margin business into a '
                                        '40% business without careful pricing and metering. I would treat '
                                        'those percentages as a warning, not my measured results. '
                                        '[Business Mechanics — Ju9H1oq7CM8 @ 00:03:00]'},
                            {'name': 'credit_route_and_expiration',
                             'type': 'textarea',
                             'prompt': 'Record the credit application route you may qualify for, the '
                                       'eligibility still requiring confirmation, and any award actually '
                                       'approved. Identify the expiration date, budget alert, and expected '
                                       'bill after credits end. Keep possible awards separate from '
                                       'available operating cash or permanent discounts.',
                             'example': 'My credit register would leave the award unconfirmed until '
                                        'approval and record its expiration from the AWS billing console '
                                        'immediately afterward. XRaise recommends checking that date on '
                                        'day one and setting a budget alert before ordinary billing '
                                        'resumes. The operating forecast would retain the unsubsidized '
                                        'bill rather than assume temporary credits permanently eliminate '
                                        'hosting costs. [XRaise — 8WJ85SV0c0U @ 00:02:55]'},
                            {'name': 'customer_lifetime_and_payback',
                             'type': 'textarea',
                             'prompt': 'Compare the time needed to recover acquisition spending with the '
                                       'time customers actually remain. Record both assumptions and '
                                       'explain the consequence if customers leave first. Identify which '
                                       'acquisition or retention evidence must improve before you increase '
                                       'spending to acquire additional subscribers.',
                             'example': 'Costoday describes a business needing sixteen months to recover '
                                        'acquisition spending while the average customer leaves after ten '
                                        'months. My economics record would flag that mismatch explicitly: '
                                        'recurring charges do not recover the acquisition investment '
                                        'before departure. I would examine the payback and customer-life '
                                        'assumptions together before expanding the same acquisition '
                                        'approach. [Costoday — aOKH0EoSCCc @ 00:06:25]'},
                            {'name': 'launch_functionality_and_retention',
                             'type': 'textarea',
                             'prompt': 'Describe how you will verify the core result and checkout before '
                                       'drawing conclusions from launch sales. Then state which continued '
                                       'customer behavior would demonstrate that the product fulfills its '
                                       'promise. Keep enthusiasm, initial attention, and durable use as '
                                       'separate observations.',
                             'example': 'Before interpreting missing sales, I would test the core workflow '
                                        "and checkout. Sandra reports Clue's functionality failing on "
                                        'launch morning, which makes a simple demand conclusion '
                                        'unreliable. My launch review would separate technical failure '
                                        'from customer response and keep later continued use as a separate '
                                        'question rather than treat launch enthusiasm as completed '
                                        'validation. [Morning Maker Show with Sandra and Dan — r1qeIcDiItU '
                                        '@ 01:10:54]'}],
                 'completion_gate': 'Approve expansion only when caching preserves correctness, routing '
                                    'costs include classification and retries, and spending can be '
                                    'attributed to actual usage. Document margins without temporary '
                                    'credits, approved credit expiration where applicable, and customer '
                                    'lifetime relative to acquisition payback. Verify core functionality '
                                    'and checkout before interpreting demand, and keep retention evidence '
                                    'distinct from launch attention.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Connect Metered Consumption to Recurring-Revenue Economics',
                 'purpose': 'Define exactly what customers purchase, prove that consumption reaches the '
                            'correct invoice, and read recurring revenue without confusing growth with '
                            'cash recovery. Finish with an operating decision grounded in billing '
                            'accuracy, gross retention, acquisition cost, and customer payback.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Complete the billing fields for one actual offer before comparing '
                                  'alternative pricing structures. Keep the customer-facing unit '
                                  'consistent across checkout, usage reporting, and invoices.',
                                  'Record expected behavior separately from observed test results. A '
                                  'configured price, webhook, or spending threshold is not evidence that '
                                  'the full collection path works.',
                                  'Use the same monthly reporting boundary for every revenue movement. '
                                  "Carry ending recurring revenue directly into the following month's "
                                  'opening balance.',
                                  'Keep customer counts, recurring subscription revenue, usage charges, '
                                  'cash receipts, and gross profit distinct. Explain any assumptions used '
                                  'to connect these measures.',
                                  'Finish by naming the billing or economic weakness that deserves action '
                                  'first, assigning responsibility, and specifying the evidence required '
                                  'before increasing acquisition spending.'],
                 'fields': [{'name': 'billable_unit_and_customer_promise',
                             'type': 'textarea',
                             'prompt': 'Define the consumption unit customers purchase, the included '
                                       'allowance, the recurring charge, and the overage rule. Explain how '
                                       'the customer recognizes that unit in everyday use, and identify '
                                       'where checkout wording could accidentally imply a different '
                                       'quantity or price.',
                             'example': 'For a worked billing check, I use the recipe API offer: $40 '
                                        'monthly includes 40 requests, followed by $0.25 per additional '
                                        'request. At 100 requests, the expected invoice is $55. I will '
                                        'compare that calculation with checkout wording and the generated '
                                        'invoice before accepting the configuration. [Stripe Developers — '
                                        'o_6aujJ5WbM @ 00:02:33]'},
                            {'name': 'usage_identity_and_reconciliation',
                             'type': 'textarea',
                             'prompt': 'Describe how each completed customer action becomes reported '
                                       'usage. Identify the customer reference, measured quantity, '
                                       'reporting record, and reconciliation step. Specify how you will '
                                       'trace an invoice quantity back to the individual generated outputs '
                                       'that produced it.',
                             'example': 'My reconciliation worksheet will pair each generated suggestion '
                                        'with its measured token count and the returned usage record ID. I '
                                        'will compare the suggestion records with reported billing usage '
                                        'before reviewing the invoice. Avilla ties every suggestion to its '
                                        'usage report so generation and billing can be reconciled '
                                        'directly. [CJ Avilla (cjav_dev) — v8cN4pEofy8 @ 00:55:55]'},
                            {'name': 'token_price_and_clock_test',
                             'type': 'textarea',
                             'prompt': 'Write the token pricing transformation and a test that exposes an '
                                       'incorrect unit. Include the displayed checkout rate, raw usage, '
                                       'transformed quantity, rounding behavior, and expected charge. '
                                       'Explain how frozen test timestamps affect repeated reports during '
                                       'the test.',
                             'example': 'I will inspect whether checkout prices individual tokens or '
                                        'thousand-token packages before sending repeated test usage. '
                                        'Avilla corrected the price to $0.07 per 1,000 tokens with upward '
                                        'rounding. When a test clock is frozen, I will advance it '
                                        'deliberately rather than assume current-time reports receive new '
                                        'timestamps. [CJ Avilla (cjav_dev) — v8cN4pEofy8 @ 01:09:53]'},
                            {'name': 'payment_event_credit_integrity',
                             'type': 'textarea',
                             'prompt': 'Specify which payment event authorizes a credit grant and how the '
                                       'account balance changes afterward. Describe signature '
                                       'verification, processed event tracking, and a repeated-event test. '
                                       'State the evidence that proves one payment cannot produce multiple '
                                       'credit grants.',
                             'example': 'My acceptance test will submit the same payment event twice and '
                                        'expect only one credit allocation. The implementation must verify '
                                        'the incoming Stripe signature and retain the processed event ID. '
                                        'I will record the balance before processing, after the first '
                                        'grant, and after the retry to expose duplicate issuance. [E '
                                        'Learning by AL SADDAT — 0K7i4CFP_qc @ 00:01:19]'},
                            {'name': 'unpaid_consumption_and_caps',
                             'type': 'textarea',
                             'prompt': 'Choose how the product responds when consumption approaches a '
                                       'spending cap or unpaid balance threshold. Name the warning, '
                                       'collection attempt, access decision, and customer message. Explain '
                                       'whether your reporting cadence supports the response quickly '
                                       'enough for the chosen policy.',
                             'example': 'I will distinguish a budget cap from a collection threshold '
                                        'instead of treating both as the same control. For a '
                                        'threshold-based offer, my test will follow the Sessions example: '
                                        'invoice at $1,000 and disable access if the attempted charge '
                                        'fails. The test must exercise the failure branch, not merely '
                                        'create an invoice. [Stripe Developers — Hr9MP_3-QPg @ 00:08:35]'},
                            {'name': 'month_end_recurring_revenue_boundary',
                             'type': 'textarea',
                             'prompt': 'Define the date and subscription state used for your recurring '
                                       'revenue snapshot. Separate recurring subscription value from cash '
                                       'received and partial-month billing. Explain how the chosen '
                                       'boundary prevents a midmonth customer start from appearing as a '
                                       'later expansion.',
                             'example': 'I will take the subscription snapshot on the last day of each '
                                        'month and show cash receipts separately. A customer starting '
                                        'midmonth will not become an apparent upsell simply because the '
                                        "next invoice covers a full month. This follows the Startup CFO's "
                                        'reason for using a consistent month-end MRR snapshot. [The '
                                        'Startup CFO — Y6tSBvQhyak @ 00:25:12]'},
                            {'name': 'monthly_revenue_movement_walk',
                             'type': 'textarea',
                             'prompt': 'Build the monthly recurring revenue walk from opening balance '
                                       'through gains, contraction, and churn to ending balance. Identify '
                                       'the records supporting each movement and explain any mismatch. '
                                       "State how the ending figure becomes the next reporting period's "
                                       'opening figure.',
                             'example': 'My monthly worksheet will start with the previous closing MRR, '
                                        'add recurring-revenue gains, and subtract contraction and churn. '
                                        'I will investigate any difference between that calculated ending '
                                        'balance and the subscription snapshot before publishing the '
                                        "dashboard. The reconciled ending amount becomes the next month's "
                                        'starting amount, preserving continuity across reports. [Vickery '
                                        'Finance — -XgJLhATOGI @ 00:01:56]'},
                            {'name': 'gross_losses_and_plan_exposure',
                             'type': 'textarea',
                             'prompt': 'Describe how you will review gross retention beside net retention '
                                       'and plan-level cancellations. Identify which losses expansion '
                                       'could conceal, and distinguish customer counts from lost recurring '
                                       'revenue. Name the plan whose cancellation would most change your '
                                       'interpretation of performance.',
                             'example': 'I will show lost recurring revenue by plan alongside cancellation '
                                        'counts, then review gross retention without letting upgrades '
                                        "cancel out the losses. Vickery's workbook illustrates why: one "
                                        "Scale cancellation removes roughly seven Starter cancellations' "
                                        'worth of base revenue. A customer-count summary alone would '
                                        'understate the importance of losing that larger subscription. '
                                        '[Vickery Finance — mt0peG4dE4w @ 00:01:43]'},
                            {'name': 'acquisition_cost_and_cash_recovery',
                             'type': 'textarea',
                             'prompt': 'Record fully loaded acquisition cost and monthly customer gross '
                                       'profit for the segment being evaluated. Calculate the recovery '
                                       'period and place it beside the lifetime-value ratio. Explain why a '
                                       'satisfactory return multiple does not necessarily mean cash '
                                       'returns quickly.',
                             'example': 'For the worked payback case, I enter £6,000 of fully loaded sales '
                                        'and marketing cost and £400 of monthly customer gross profit. '
                                        'Recovery therefore takes 15 months. I will keep that duration '
                                        'visible beside any lifetime-value ratio because the ratio does '
                                        'not show how long acquisition spending remains unrecovered. [One '
                                        'Minute Finance — Xpw9vNbYna0 @ 00:06:48]'},
                            {'name': 'economic_stop_and_review_decision',
                             'type': 'textarea',
                             'prompt': 'Write the decision you will make when acquisition economics become '
                                       'unfavorable. State the lifetime assumption, evidence needed to '
                                       'revise it, and spending response. Explain how you will avoid '
                                       'treating one zero-churn month as proof that customers remain '
                                       'indefinitely.',
                             'example': 'My decision record will explicitly cap modeled customer lifetime '
                                        'rather than extrapolate indefinitely from a zero-churn month. I '
                                        'will document the product-specific reason for the cap and revisit '
                                        'it as cohorts mature. The Startup CFO uses five years in one '
                                        'example, but presents that choice as dependent on the product. '
                                        '[The Startup CFO — Y6tSBvQhyak @ 00:42:46]'}],
                 'completion_gate': 'Complete only when one customer action can be traced through usage '
                                    'reporting to an expected invoice, duplicate payment events cannot '
                                    'grant duplicate credits in the recorded test, and the spending-limit '
                                    'failure response is explicit. Reconcile the monthly revenue walk, '
                                    'expose gross losses, and state an acquisition decision using both '
                                    'return ratio and gross-profit payback.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Choose a Platform Wedge and Earn the Right to Scale',
                 'purpose': 'Turn an existing platform workflow into a narrowly defined product, validate '
                            'urgency against available alternatives, and prepare a launch that the '
                            'business can support. Connect marketplace discovery, user testing, retention, '
                            'pricing presentation, and operating capacity before multiplying applications '
                            'or acquisition spending.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Choose one platform and one recurring customer activity. Describe the '
                                  'existing workflow before proposing features, integrations, additional '
                                  'applications, or a broader portfolio.',
                                  'Collect complaints and buying signals separately. A review, interview, '
                                  'installation, payment, and returning user answer different questions '
                                  'about whether the opportunity deserves investment.',
                                  'Use the platform fields to identify the smallest useful intervention, '
                                  'then schedule direct user testing before treating the implementation as '
                                  'finished.',
                                  'Prepare launch coverage and support ownership alongside promotional '
                                  'work. Document the circumstances that would require smaller onboarding '
                                  'batches or a temporary pause.',
                                  'Make the final growth decision from observed conversion, retention, '
                                  'support load, and capacity. Keep practitioner revenue milestones as '
                                  'context rather than promises for your own application.'],
                 'fields': [{'name': 'platform_workflow_and_pain',
                             'type': 'textarea',
                             'prompt': 'Name the platform, the customer activity already happening there, '
                                       'and the specific friction your application removes. Describe where '
                                       'you will find customer language about that friction and explain '
                                       'why solving it inside the existing workflow is preferable to '
                                       'adding another destination.',
                             'example': 'I will investigate an Airtable workflow before designing a '
                                        'standalone replacement. My research notes will collect the '
                                        'repeated pain described in platform forums, Reddit, and Twitter, '
                                        'then connect each complaint to the activity being interrupted. '
                                        'Andy describes finding a platform pain point this way when '
                                        'explaining the Data Fetcher opportunity and its development path. '
                                        '[Starter Story — NvtsM8Nk72c @ 00:04:47]'},
                            {'name': 'marketplace_demand_and_competition',
                             'type': 'textarea',
                             'prompt': 'Create a marketplace research plan that connects search demand '
                                       'with dissatisfaction in existing products. Specify the search '
                                       'method, review evidence, comparison criteria, and shortlist rule. '
                                       'Explain how you will distinguish an active category with '
                                       'weaknesses from a category with little visible demand.',
                             'example': 'For Shopify research, I will search each alphabet letter in '
                                        'autocomplete and collect the suggested keywords. I will compare '
                                        "recent review activity with the leading application's rating "
                                        'before shortlisting a category. Super Lemon used this combination '
                                        'to look for active demand where the established product still '
                                        'left room for a useful competitor. [hexdevs — KP61wa0qiSU @ '
                                        '00:16:31]'},
                            {'name': 'urgency_and_existing_alternatives',
                             'type': 'textarea',
                             'prompt': 'Write the interview questions that test why a prospect has not '
                                       'adopted an existing alternative. Separate polite enthusiasm from '
                                       'urgent need, and state what answer would weaken your idea. '
                                       'Describe the evidence required before moving from conversations '
                                       'into a product build.',
                             'example': 'My interview will ask which alternatives the prospect knows, '
                                        'whether they tried them, and why the work remains unresolved. If '
                                        'they describe the product as useful but cannot explain why '
                                        'existing options remain unused, I will reconsider urgency. The '
                                        'Session Fox founders changed their conclusion after asking this '
                                        'question rather than accepting initial enthusiasm. [hexdevs — '
                                        'KP61wa0qiSU @ 00:08:51]'},
                            {'name': 'early_testing_and_contextual_help',
                             'type': 'textarea',
                             'prompt': "Plan an early user test around the application's most important "
                                       'action and the control most likely to confuse customers. Record '
                                       'the observed difficulty, a small contextual explanation, and the '
                                       'follow-up measure that will show whether the change reduces '
                                       'repeated support requests.',
                             'example': 'I will watch a user attempt the confusing action, place a short '
                                        'explanation beside the relevant control, and track whether the '
                                        'same question returns. Super Lemon reports that adding two '
                                        'sentences reduced one recurring support question from roughly ten '
                                        'daily messages to one or zero. I will measure my own result '
                                        'rather than assume the same reduction. [hexdevs — KP61wa0qiSU @ '
                                        '00:33:23]'},
                            {'name': 'platform_health_and_portfolio_readiness',
                             'type': 'textarea',
                             'prompt': 'Describe the platform health review you will complete before '
                                       'adding another application. Include installs, uninstalls, free '
                                       'users, paying users, and support ownership. Explain which '
                                       'combination of signals would show that apparent acquisition '
                                       'momentum is masking an application that still needs attention.',
                             'example': 'I will report installs and uninstalls together rather than '
                                        'celebrate installations alone, and I will separate free users '
                                        'from paying customers. Jack reports 47 installs and 43 uninstalls '
                                        "while most of Profit AI's 122 users are free. Those figures make "
                                        'a useful review pattern, not evidence that every installation '
                                        'represents durable recurring revenue. [Starter Story — '
                                        'd8PdJJcEtE0 @ 00:02:49]'},
                            {'name': 'first_sales_learning_log',
                             'type': 'textarea',
                             'prompt': 'Design a learning log for the first customer conversations and '
                                       'sales. Capture the problem, buying hesitation, promised outcome, '
                                       'and what changed in your understanding. State how you will '
                                       'preserve those lessons before turning the conversation into a '
                                       'repeatable acquisition system.',
                             'example': "After each early sale, I will record the buyer's original "
                                        'problem, the question that delayed payment, and the explanation '
                                        'that made the offer understandable. I will not judge the '
                                        'conversation only by its immediate revenue. Andrew describes the '
                                        'first one, two, or three sales as especially valuable for the '
                                        'learning they produce. [Andrew Zacker — -LhzMIH0ktI @ 00:02:10]'},
                            {'name': 'conversion_and_churn_interviews',
                             'type': 'textarea',
                             'prompt': 'Select two interview groups: people who signed up without '
                                       'converting and customers who left. Write the questions that '
                                       'separate purchase friction from disappointing product value. '
                                       'Explain how the answers will change your next product or '
                                       'onboarding decision before acquisition expands.',
                             'example': 'I will maintain separate notes for nonconverting signups and '
                                        'departed customers so their problems do not collapse into one '
                                        'generic churn explanation. The first group will explain what '
                                        'prevented purchase; the second will explain what failed after '
                                        'adoption. Philip explicitly interviewed both groups while '
                                        'repairing conversion and retention before the later growth '
                                        'update. [Starter Story — Ce_wXQ1BJjE @ 00:08:19]'},
                            {'name': 'onboarding_capacity_and_pause_rule',
                             'type': 'textarea',
                             'prompt': 'Define the operational signs that would make you pause open '
                                       'signups or reduce onboarding volume. Name the constrained '
                                       'resource, customer symptoms, batch approach, and restart evidence. '
                                       'Explain who will review whether acquisition is outpacing the '
                                       "product's ability to deliver.",
                             'example': 'My launch plan will permit smaller weekly onboarding batches if '
                                        'account capacity, customer outcomes, or churn deteriorate. I will '
                                        'document the constrained resource and the repair needed before '
                                        'reopening broadly. Philip paused signups when capacity, comment '
                                        'removals, and churn worsened, then used limited weekly batches '
                                        'rather than continuing to admit everyone immediately. [Starter '
                                        'Story — Ce_wXQ1BJjE @ 00:11:10]'},
                            {'name': 'pricing_presentation_experiment',
                             'type': 'textarea',
                             'prompt': 'Specify a pricing-page experiment that changes presentation rather '
                                       'than assuming the price itself is wrong. Describe the variants, '
                                       'conversion measure, review interval, and elimination decision. '
                                       'Explain how you will keep the experiment focused on helping buyers '
                                       'understand the offer.',
                             'example': 'I will compare pricing-page presentations before deciding that '
                                        'weak conversion requires a lower price. My experiment record will '
                                        'identify each version, its conversion result, and the reason for '
                                        'retaining or eliminating it. Spencer tested four pricing pages '
                                        'and removed one every two weeks to find the strongest converter, '
                                        'making presentation an explicit operating variable. [MicroConf — '
                                        'C-e54fVQUlg @ 00:14:48]'},
                            {'name': 'launch_coverage_and_growth_permission',
                             'type': 'textarea',
                             'prompt': 'Write the launch coverage plan and the evidence required before '
                                       'scaling afterward. Assign responsibility through the closing '
                                       'hours, identify how comments become product research, and '
                                       'distinguish launch attention from returning customers. State which '
                                       'unresolved retention issue would block additional acquisition.',
                             'example': 'I will assign launch coverage through the final hours instead of '
                                        'assuming the opening push completes the job. The handoff notes '
                                        'will include unanswered questions and product feedback for later '
                                        'review. Lihong describes losing an initial daily race after '
                                        'falling asleep and subsequently organizing global team shifts to '
                                        'maintain coverage across the launch period. [Lihong Hicken — '
                                        'g1sBB5xzmTI @ 00:08:46]'}],
                 'completion_gate': 'Complete only when the platform problem is supported by customer '
                                    'language, prospects have explained why existing alternatives are '
                                    'inadequate, and an early user test has a named owner. Record installs '
                                    'alongside uninstalls, separate free adoption from payment, and '
                                    'document capacity-based pause criteria. Do not authorize portfolio '
                                    'expansion or broader acquisition without an explicit retention and '
                                    'support review.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Turn Buyer Discovery into Activation and Recovered Revenue',
                 'purpose': 'Build discovery assets around real evaluation questions, connect visibility '
                            'to buyer-reported attribution, and investigate the losses that follow signup. '
                            'Separate weak activation, deliberate cancellation, and failed payments so '
                            'content, onboarding, and recovery work address different problems instead of '
                            'sharing one vague growth target.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Start with recorded buyer language and the questions asked before '
                                  'choosing software. Select content because it helps an evaluation, not '
                                  'merely because it could attract impressions.',
                                  'For each discovery asset, name the buyer question, intended next '
                                  'action, distribution route, and review responsibility. Keep comparison '
                                  'claims open to correction.',
                                  'Check indexing weekly and collect signup attribution directly. Preserve '
                                  'the difference between analytics visits, self-reported signup sources, '
                                  'and qualified pipeline.',
                                  'Divide customer losses into deliberate cancellations and payment '
                                  'failures before choosing interventions. Evaluate activation against '
                                  'retained and departing users rather than convenient activity counts.',
                                  'Finish with an owned recovery test covering timing, payment status, '
                                  'messages, and unsuccessful outcomes. Treat practitioner recovery '
                                  'percentages as attributed results, not guaranteed performance.'],
                 'fields': [{'name': 'buyer_language_and_evaluation_question',
                             'type': 'textarea',
                             'prompt': 'Identify the exact question buyers ask while evaluating your '
                                       'category and the interviews supporting that wording. Describe how '
                                       'you will record, transcribe, and reread customer conversations. '
                                       "Explain how the resulting language will change a comparison page's "
                                       'headline, argument, or description of value.',
                             'example': 'My comparison brief will begin with wording taken from customer '
                                        'interviews rather than an internally invented feature list. I '
                                        'will record the calls, transcribe them, and reread the '
                                        'transcripts before drafting the page. Federico Jorge describes '
                                        'this process as the route to speaking and thinking like customers '
                                        'when building comparison messaging. [UserActive - SaaS Design '
                                        'Agency — JVpDfAIFgYk @ 00:06:38]'},
                            {'name': 'comparison_asset_and_correction_plan',
                             'type': 'textarea',
                             'prompt': 'Outline one comparison or alternatives page for a specific buying '
                                       'decision. State the distinction it should explain, the evidence '
                                       'behind its claims, and the next action for a qualified buyer. '
                                       'Assign responsibility for reviewing competitor objections and '
                                       'correcting disputed material.',
                             'example': 'I will give the comparison page an owner who can review '
                                        'objections and change the published argument when needed. The '
                                        'operating plan will allow correction or removal rather than '
                                        "assume publication ends the work. Gallant's campaign removed one "
                                        'disputed page and corrected another, showing that '
                                        'competitor-response work remains part of managing comparison '
                                        'content. [Josh Gallant — gDJkMfIyJJg @ 00:07:10]'},
                            {'name': 'question_page_and_video_pair',
                             'type': 'textarea',
                             'prompt': 'Plan a page and companion video answering one buyer question. '
                                       'Specify the title wording, opening answer, supporting explanation, '
                                       'and intended next action. Explain how both assets help the buyer '
                                       'evaluate the product rather than merely describe its features or '
                                       'attract broad attention.',
                             'example': 'My content brief will pair one buyer question with a page and a '
                                        "five-to-fifteen-minute video. The title will use the buyer's "
                                        'wording, and the video will answer the question within the first '
                                        'thirty seconds before expanding on the explanation. This follows '
                                        "Ogonowski's question-led format rather than beginning with a "
                                        'lengthy product introduction. [Paul Ogonowski — smAcRrXdcgw @ '
                                        '00:06:20]'},
                            {'name': 'weekly_indexing_review',
                             'type': 'textarea',
                             'prompt': 'Define a weekly indexing review for your priority discovery pages '
                                       'across Google and Bing. Record the page, observed status, reported '
                                       'reason for exclusion, improvement, and follow-up request. Explain '
                                       'how you will prevent publication volume from hiding pages that '
                                       'buyers cannot discover.',
                             'example': 'Each week, I will check priority pages in Google Search Console '
                                        'and Bing rather than assume publication made them discoverable. '
                                        'For a missing page, I will record the stated reason, improve the '
                                        'page, and request indexing again. Coutinho describes this '
                                        'repeated inspection and correction as necessary operating work, '
                                        'including the problems encountered with Bing. [Micael Coutinho — '
                                        'KYpd0fJp3Qw @ 00:05:09]'},
                            {'name': 'discovery_attribution_and_pipeline',
                             'type': 'textarea',
                             'prompt': 'Specify how signup or demo forms will capture first discovery and '
                                       'any question asked of an AI assistant. Compare those answers with '
                                       'referral analytics without merging different denominators. Explain '
                                       'which pipeline outcome will determine whether the discovery work '
                                       'deserves continued investment.',
                             'example': 'I will keep analytics visits and signup-reported discovery in '
                                        'separate columns. Ogonowski reports AI representing 2% of visits '
                                        'in analytics while 23% of new signups reported AI discovery. '
                                        'Those figures use different populations, so I will not subtract '
                                        'them as a conversion gap or treat either measure as the complete '
                                        'attribution story. [Paul Ogonowski — smAcRrXdcgw @ 00:00:41]'},
                            {'name': 'voluntary_and_involuntary_loss_split',
                             'type': 'textarea',
                             'prompt': 'Divide a customer-loss cohort into deliberate cancellations and '
                                       'failed-payment departures. Identify the evidence used to classify '
                                       'each account and the questions appropriate to each group. Explain '
                                       'why a product-value intervention and a payment-update intervention '
                                       'should not be evaluated as interchangeable fixes.',
                             'example': 'My loss review will first separate customers who chose '
                                        'cancellation from accounts lost after payment failure. I will '
                                        'examine product value and engagement for the first group, then '
                                        'review payment recovery for the second. RonBuilds starts with '
                                        'this voluntary-versus-involuntary cohort split before choosing a '
                                        'response, avoiding one undifferentiated explanation for every '
                                        'lost customer. [RonBuilds — FtbQGH3sZ3c @ 00:02:00]'},
                            {'name': 'activation_event_and_first_value',
                             'type': 'textarea',
                             'prompt': 'Name the event you believe represents first customer value and '
                                       'explain how it fits the billing cycle. Compare its occurrence '
                                       'among retained and departing users. State what evidence would make '
                                       'you reject the event as an activation measure.',
                             'example': 'I will not label an easy action as activation simply because many '
                                        'users complete it. My review will compare that event between '
                                        'retained customers and customers who leave, then reconsider the '
                                        'event if it fails to distinguish them. RonBuilds warns that an '
                                        'event everyone performs does not establish meaningful activation. '
                                        '[RonBuilds — FtbQGH3sZ3c @ 00:16:11]'},
                            {'name': 'at_risk_rule_and_prediction_test',
                             'type': 'textarea',
                             'prompt': 'Describe the current usage rule for identifying at-risk customers '
                                       'and the prediction alternative you want to test. Exclude '
                                       'information that would only become available after cancellation. '
                                       'Specify a later-renewal evaluation and the condition for keeping '
                                       'the existing rule.',
                             'example': 'My prediction review will retain the existing usage rule as the '
                                        'comparison rather than assume a model is better. I will exclude '
                                        'future cancellation information from inputs and test against '
                                        'later renewals. If the model cannot beat the current rule, I will '
                                        'keep that rule instead of replacing it with added complexity. '
                                        '[Gamify Data — SFcHnbb87E8 @ 00:01:01]'},
                            {'name': 'dunning_window_experiment',
                             'type': 'textarea',
                             'prompt': 'Choose a failed-payment recovery window to evaluate and explain '
                                       'how you will compare recovered accounts or revenue across '
                                       'attempts. Record the current window, proposed alternative, and '
                                       'review decision. Keep merchant benchmarks separate from the '
                                       'outcome your own customers produce.',
                             'example': 'I will compare the current recovery window with a longer '
                                        'alternative rather than assume the shortest sequence is best. '
                                        'Recurly reports merchant median recovery of 47% for '
                                        'one-to-seven-day windows and 57.7% for fifteen-to-twenty-one-day '
                                        'windows. Those figures justify an experiment, but they do not '
                                        'establish the recovery rate my customer base will achieve. '
                                        '[Recurly — eBy7DfSz09g @ 00:00:21]'},
                            {'name': 'recovery_sequence_and_status_checks',
                             'type': 'textarea',
                             'prompt': 'Write the recovery sequence connecting payment retries, customer '
                                       'messages, and an easy payment-update action. Identify when payment '
                                       'status is checked and what happens after success or another '
                                       'failure. Specify the test that prevents an unnecessary reminder '
                                       'after recovery.',
                             'example': 'For later recovery messages, I will test a payment attempt before '
                                        'sending the email and confirm that success suppresses the '
                                        'reminder. I will not apply that expectation to the immediate '
                                        'first email, which cannot use this option in the demonstrated '
                                        'Churnkey workflow. The recorded test will cover both successful '
                                        'and unsuccessful payment attempts. [Churnkey — B-tr3MgFk_s @ '
                                        '00:10:19]'}],
                 'completion_gate': 'Complete only when a buyer question maps to an owned discovery asset, '
                                    'indexing has a weekly review, and signup attribution preserves its '
                                    'distinct measurement population. Classify customer losses before '
                                    'choosing a remedy, justify activation through '
                                    'retained-versus-departing behavior, and document a recovery test that '
                                    'checks payment status before follow-up. Name the next action and '
                                    'owner for every unresolved failure.'}]}
