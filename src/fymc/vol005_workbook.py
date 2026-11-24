from __future__ import annotations

def build_volume_005_workbook() -> dict:
    return {'workbook_id': 'wb-005-high-ticket-affiliate-marketing',
 'volume_id': 'vol-005-high-ticket-affiliate-marketing',
 'title': 'High-Ticket Affiliate Marketing — Practitioner Testimony Operator Workbook',
 'subtitle': 'High-Ticket Affiliate Marketing: Select Offers with Defensible Economics, Build Trust-Based '
             'Buyer Journeys, and Turn Search Visibility into Qualified Customer Actions',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Offer Fit, Recurring Economics, and Partnership Readiness',
                 'purpose': 'Choose affiliate offers around a specific buyer problem, realistic commission '
                            'conditions, and content you can actually produce. Separate attractive payout '
                            'illustrations from verified program terms, then prepare applications, '
                            'destination links, and partner relationships without assuming acceptance or '
                            'immediate earnings.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Start with one buyer problem and describe the useful software outcome '
                                  'before listing commission percentages or searching for additional '
                                  'programs.',
                                  'Compare recurring and fixed payouts using their actual duration, '
                                  'retention conditions, attribution windows, refund exposure, and '
                                  'withdrawal timing.',
                                  "Inspect both the network listing and the company's affiliate page; "
                                  'leave conflicting or unavailable terms explicitly unresolved.',
                                  'Prepare accurate applications for relevant programs, then narrow '
                                  'accepted partnerships to the few you can support with useful content.',
                                  'Complete the acquisition, link, and relationship checks before treating '
                                  'an advertised commission or dashboard balance as dependable cash.'],
                 'fields': [{'name': 'buyer_problem_and_offer_fit',
                             'type': 'textarea',
                             'prompt': 'Describe one audience, the software problem they need solved, and '
                                       'the content that would help them choose. Explain why the proposed '
                                       'offer belongs in that decision, including the search demand and '
                                       'competitive weakness you still need to examine.',
                             'example': 'Planned audience: buyers comparing subscription software for a '
                                        'specific business task. I will shortlist offers only when useful '
                                        'comparison content, plausible search demand, and commission '
                                        'economics intersect. Adam Enfroy describes that intersection '
                                        'rather than selecting the largest payout alone. Demand and '
                                        'competing content remain research tasks, not established '
                                        'advantages for my proposed page. [Adam Enfroy — rv01CKLsaY0 @ '
                                        '00:12:46]'},
                            {'name': 'recurring_commission_model',
                             'type': 'textarea',
                             'prompt': 'Write the subscription price, commission percentage, monthly '
                                       'commission, and possible annual total for one recurring offer. '
                                       'Label arithmetic illustrations separately from confirmed terms, '
                                       'and identify the continued customer payments required before the '
                                       'annual amount could actually be earned.',
                             'example': 'Illustration: a $300 monthly subscription at 40% produces $120 '
                                        'monthly commission; twelve paid months produce $1,440. These are '
                                        "Adam Enfroy's illustrative economics, not my verified program "
                                        'terms or a guaranteed annual payment. My offer record will keep '
                                        'the twelve-month calculation conditional on continued '
                                        "subscription payments and the program's confirmed commission "
                                        'duration. [Adam Enfroy — rv01CKLsaY0 @ 00:01:23]'},
                            {'name': 'retention_and_duration_comparison',
                             'type': 'textarea',
                             'prompt': 'Compare two recurring offers by commission percentage, likely paid '
                                       'duration, and available retention evidence. Explain which offer '
                                       'deserves further investigation and why a larger percentage could '
                                       'produce less income when customers leave sooner or the commission '
                                       'period ends earlier.',
                             'example': 'Comparison note: I will not automatically favor a 50% recurring '
                                        'headline over a 20% offer. Smart Capital contrasts 50% for one '
                                        'month with 20% over three years, making retention central to the '
                                        'decision. My shortlist will leave customer duration unverified '
                                        'until supporting information is available, rather than treating '
                                        'either scenario as typical. [Smart Capital — LBA0vmJPE5w @ '
                                        '00:09:47]'},
                            {'name': 'attribution_and_refund_conditions',
                             'type': 'textarea',
                             'prompt': 'Record the cookie window, refund conditions, and circumstances '
                                       'that could remove a commission from the offer you are evaluating. '
                                       'Explain which earnings remain conditional, what terms require '
                                       'clarification, and why a dashboard amount should not automatically '
                                       'become spendable income.',
                             'example': 'Terms checklist: confirm the attribution window and identify '
                                        'whether a refunded purchase cancels the associated commission. '
                                        'Smart Capital contrasts 90-day attribution with 24 hours and '
                                        "warns that refunds erase commissions. Until my chosen program's "
                                        'terms are checked, I will mark its window and refund exposure '
                                        'unresolved rather than borrowing either example as fact. [Smart '
                                        'Capital — GCv_2yM5JtI @ 00:06:23]'},
                            {'name': 'network_and_direct_offer_reconciliation',
                             'type': 'textarea',
                             'prompt': "Compare the same company's network listing with its own affiliate "
                                       'page. Record matching terms, differences, and unanswered questions '
                                       'about payouts or eligibility. State which source needs '
                                       'clarification before you choose an application route or publish a '
                                       'financial claim.',
                             'example': "Planned comparison: place the company's affiliate page beside its "
                                        'PartnerStack listing and record any differences before applying. '
                                        'Mr. Money reports that these offers can differ. I will not assume '
                                        'the network version is identical or automatically superior; '
                                        'conflicting payout language will remain an open question until '
                                        'the applicable partnership terms are clarified. [Mr. Money — '
                                        'VHaXNPiHd6Q @ 00:06:45]'},
                            {'name': 'application_accuracy_and_focus',
                             'type': 'textarea',
                             'prompt': 'Prepare an accurate application summary covering your location, '
                                       'audience, and intended content. Identify any details needing '
                                       'correction before submission, then describe how you will select a '
                                       'manageable working group from accepted programs instead of '
                                       'accumulating unrelated affiliate links.',
                             'example': 'Application note: my location entry must match my actual '
                                        'circumstances, and my audience description must explain the '
                                        'content I intend to create. Kris reports repeated rejection after '
                                        'entering the United States while actually in Mexico. I will '
                                        'resolve inconsistent details before submitting and keep rejected '
                                        'applications separate from accepted, usable partnerships. [Kris '
                                        'the Entrepreneur — JFjxGPpUYBk @ 00:04:21]'},
                            {'name': 'commercial_content_candidate',
                             'type': 'textarea',
                             'prompt': 'Choose one accepted or prospective product and outline comparison, '
                                       'alternative, and pricing searches worth examining. Specify the '
                                       'buyer decision each search represents and the useful content you '
                                       'could create, rather than treating program availability as proof '
                                       'of audience demand.',
                             'example': 'Planned research sequence: search the product name with versus, '
                                        'inspect suggested competitors, then examine alternatives and '
                                        'pricing queries. Khris Steven uses these searches to develop '
                                        'commercial content ideas. I will retain only topics where I can '
                                        'explain a real choice, recording the intended buyer decision '
                                        'before drafting an article or recording a video. [Khris Steven — '
                                        '-C4gk3OAfmk @ 00:06:13]'},
                            {'name': 'tracking_link_destination',
                             'type': 'textarea',
                             'prompt': 'Specify the content topic, intended next action, and exact product '
                                       'destination your affiliate link should serve. Explain how that '
                                       "destination matches the visitor's task, and record whether program "
                                       'acceptance and custom link creation are complete or still awaiting '
                                       'confirmation.',
                             'example': 'Planned tutorial: demonstrate voice changing, then direct '
                                        'interested viewers to the voice changer rather than an unrelated '
                                        'product page. AI Affiliator demonstrates selecting the ElevenLabs '
                                        'voice changer destination in a custom PartnerStack link. My '
                                        'worksheet will mark acceptance and link creation pending until '
                                        'completed; the destination choice alone does not establish an '
                                        'active partnership. [AI Affiliator — zDC4zO_iL1A @ 00:00:56]'},
                            {'name': 'partner_support_and_materials',
                             'type': 'textarea',
                             'prompt': 'Draft a partner manager request tied to a specific audience and '
                                       'planned campaign. Identify the materials or distinctive offer that '
                                       'would improve the content, and distinguish a requested discount '
                                       'from an approved benefit you may actually present to buyers.',
                             'example': 'Draft request: I am preparing product comparison content for an '
                                        'audience with a defined buying problem. Could you provide '
                                        'suitable campaign materials or confirm whether a distinctive '
                                        'discount is available? Kris describes asking engaged partners for '
                                        'support and gives a 20% code example. I will not advertise that '
                                        'discount without program approval. [Kris the Entrepreneur — '
                                        'C-RMQqTVMOE @ 00:07:06]'},
                            {'name': 'acquisition_delay_and_workload',
                             'type': 'textarea',
                             'prompt': 'Describe the content workload and acquisition delay your plan must '
                                       'tolerate before commissions appear. Separate publishing activity '
                                       'from customer acquisition and profitable advertising, then state '
                                       'what evidence you need before calling the offer an operating '
                                       'income source.',
                             'example': 'Operating assumption: useful content may require sustained work '
                                        'before producing a commission. Cesar reports publishing daily and '
                                        'waiting one year for their first commission, while distinguishing '
                                        'running ads from running profitable ads. I will record content '
                                        'effort, acquisition expense, and actual commissions separately '
                                        'instead of describing an installed funnel as an established '
                                        'income stream. [Cesar O. Vlogs — 0BMb7aXEG78 @ 01:33:39]'}],
                 'completion_gate': 'Proceed only when the buyer problem, offer fit, commission '
                                    'calculation, retention uncertainty, attribution terms, and refund '
                                    'conditions are recorded. Applications must contain accurate details; '
                                    'acceptance and link status must be explicit. Leave unresolved terms '
                                    "visible, and do not substitute another practitioner's earnings or "
                                    'timelines for your own operating evidence.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Trust-Based Funnels and Borrowed-Authority Risk Checks',
                 'purpose': 'Design a buyer journey with a clear next action, then inspect the points '
                            'where trust, applications, booking, and attendance can break. Evaluate '
                            'external publishing opportunities without confusing a ranking discussion with '
                            'a visible contribution, a destination visit, or a useful customer action.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Map the journey from incoming traffic through capture, education, and '
                                  'the intended offer or booking action before designing additional pages.',
                                  "Write each page's job separately, including the trust-building "
                                  'explanation and the action the visitor should take next.',
                                  'Inspect buttons, page continuity, calendar loading, and invitation '
                                  'contents through the actual visitor journey rather than assuming they '
                                  'work.',
                                  'For external placements, inspect native platform conditions, community '
                                  'permissions, unrestricted search visibility, and the full opportunity '
                                  'cost.',
                                  'Keep funnel outcomes and external visibility stages separate, and '
                                  'record the evidence that would justify continued work or a change.'],
                 'fields': [{'name': 'buyer_journey_and_page_roles',
                             'type': 'textarea',
                             'prompt': 'Map the intended visitor journey from traffic source to lead '
                                       'capture, trust building, and the affiliate offer. Give each step '
                                       'one clear job, and explain what the visitor should understand '
                                       'before being asked to take the next action.',
                             'example': 'Planned journey: a useful content visit leads to capture, '
                                        "followed by a bridge video explaining the product's relevance "
                                        'before the affiliate offer. Smart Capital distinguishes the '
                                        "landing page's lead collection from the bridge video's trust "
                                        'building. I will write those jobs separately so neither page '
                                        'becomes a collection of competing requests. [Smart Capital — '
                                        'rO96TZ7xl6A @ 00:13:12]'},
                            {'name': 'opt_in_promise_and_repeat_action',
                             'type': 'textarea',
                             'prompt': 'Write the specific resource promised on the opt-in page and the '
                                       'supporting explanation that makes requesting it worthwhile. '
                                       'Identify where the action appears again after the copy, and define '
                                       'the signup result without confusing it with a later purchase.',
                             'example': 'Planned page: offer a clearly described resource, explain its '
                                        'immediate usefulness, and repeat the request button beneath the '
                                        'supporting copy. Alex Cattoni recommends the repeated bottom CTA '
                                        'so readers need not scroll back up. I will count resource signups '
                                        'as opt-ins, leaving subsequent purchases as a separate result '
                                        'rather than inflating sales performance. [Alex Cattoni — '
                                        'vC_LEc8pGp8 @ 00:07:32]'},
                            {'name': 'video_to_application_action',
                             'type': 'textarea',
                             'prompt': 'Describe how a visitor moves from watching the video to finding '
                                       'and completing the application. Specify the button behavior and '
                                       'the application outcome you would compare, while keeping another '
                                       "operator's reported improvement separate from your own expected "
                                       'result.',
                             'example': 'Planned change: place an explicit button beneath the video that '
                                        'scrolls to the survey, rather than relying on visitors to notice '
                                        'the application below. Ryan Mathews reports 10–20% more '
                                        'applications in their split tests. My comparison will measure '
                                        'completed applications for my page; their reported lift is a '
                                        'reason to test, not a forecast. [Ryan Mathews — mhUqtWNsZ8A @ '
                                        '00:06:10]'},
                            {'name': 'page_continuity_and_credibility',
                             'type': 'textarea',
                             'prompt': 'Identify the visual and explanatory continuity between your opt-in '
                                       'and pre-frame pages. Describe how the visitor will recognize the '
                                       'same journey, and specify any button or message changes that could '
                                       'make the next page feel disconnected from the original promise.',
                             'example': 'Planned continuity check: keep the action button color consistent '
                                        'between the opt-in and pre-frame pages, and carry the same '
                                        'promised next step into the introduction. Joshua Gill uses button '
                                        'continuity to reinforce that visitors have not been redirected to '
                                        'somebody else. I will inspect both pages together before adding '
                                        'more design variations. [Joshua Gill - Bossnation Academy — '
                                        'lnRu8Ty8cuk @ 00:17:29]'},
                            {'name': 'booking_calendar_loading_check',
                             'type': 'textarea',
                             'prompt': 'Describe the booking page inspection you will perform as a '
                                       'visitor. Record whether the calendar appears promptly, what '
                                       'someone sees while waiting, and the explicit instruction you would '
                                       'add if loading behavior creates uncertainty or interrupts the '
                                       'intended booking action.',
                             'example': 'Planned inspection: open the booking page and watch the calendar '
                                        'load before declaring the booking step ready. If waiting leaves '
                                        'the next action unclear, add an explicit loading instruction. '
                                        'Jamie McAdam introduced that instruction after observing '
                                        'abandonment at this step. My record will distinguish an observed '
                                        'loading problem from an untested assumption about visitors. '
                                        '[Jamie McAdam — khf473ZL71w @ 00:05:33]'},
                            {'name': 'meeting_invitation_completeness',
                             'type': 'textarea',
                             'prompt': 'Define the completed booking experience, including what accepting '
                                       "the invitation should place in the prospect's calendar. Record the "
                                       'meeting information and access link checks, and state which '
                                       'missing element would prevent you from approving the booking flow.',
                             'example': 'Acceptance test: after booking, accept the invitation and inspect '
                                        'the calendar entry for both the meeting and its usable meeting '
                                        'link. Ryan Mathews rejected an add-to-calendar implementation '
                                        'because it omitted that link. I will not mark booking complete '
                                        'merely because a confirmation page appears or a calendar event '
                                        'exists without access information. [Ryan Mathews — mhUqtWNsZ8A @ '
                                        '00:15:27]'},
                            {'name': 'attendance_and_affordability_diagnosis',
                             'type': 'textarea',
                             'prompt': 'Explain how you will investigate a funnel with strong attendance '
                                       'but weak purchases. Separate the success of getting people into '
                                       'calls from their ability to buy, and identify the affordability '
                                       'questions needed before changing the page or expanding '
                                       'acquisition.',
                             'example': 'Diagnostic note: if prospects attend but rarely purchase, '
                                        'investigate whether their business costs leave room for the main '
                                        'offer. Jamie McAdam describes affordability blocking purchases '
                                        'despite a high show rate. I will keep attendance and sales '
                                        'separate, recording the purchase obstacle before assuming that '
                                        'more bookings or different page copy will solve the problem. '
                                        '[Jamie McAdam — Ck6CfmXv244 @ 00:02:18]'},
                            {'name': 'native_platform_permission_check',
                             'type': 'textarea',
                             'prompt': 'Choose one external discussion or publishing opportunity and '
                                       'describe the native page checks required before contributing. '
                                       'Record whether participation remains possible and whether the '
                                       'community allows the intended link or promotion, rather than '
                                       'relying on search visibility alone.',
                             'example': 'Planned opportunity record: open the actual Reddit discussion '
                                        'before drafting a contribution, then check whether participation '
                                        'and the intended promotion are permitted. Rankso found a '
                                        'Google-visible comparison thread that was archived. I will mark '
                                        'an archived discussion unavailable for commenting even if its '
                                        'search position looks attractive; visibility does not reopen '
                                        'participation. [Rankso SEO — gGfsCEiyizs @ 00:11:29]'},
                            {'name': 'external_visibility_measurement',
                             'type': 'textarea',
                             'prompt': 'Create separate evidence entries for discussion visibility, your '
                                       "contribution's visibility, visits to the destination, and useful "
                                       'customer actions. Explain what would establish each stage and '
                                       "which conclusions remain unavailable when only the discussion's "
                                       'search appearance has been observed.',
                             'example': 'Measurement record: a ranking discussion is stage one, a visible '
                                        'contribution is stage two, destination visits are stage three, '
                                        'and useful customer actions are stage four. Rankso warns against '
                                        'treating one stage as proof of the next. I will leave later '
                                        'entries unverified until observed rather than reporting the '
                                        "discussion's ranking as customer acquisition. [Rankso SEO — "
                                        'gGfsCEiyizs @ 00:23:17]'},
                            {'name': 'placement_cost_and_durability',
                             'type': 'textarea',
                             'prompt': 'Evaluate a paid external placement by recording placement expense, '
                                       'supporting-link work, traffic-push expense, and unresolved ranking '
                                       'risk. Explain how you will distinguish regional manual-action '
                                       'relief from continuing algorithmic behavior before treating the '
                                       'opportunity as a durable acquisition asset.',
                             'example': 'Planned evaluation: list the placement charge alongside '
                                        'supporting-link and traffic-push expenses before comparing the '
                                        'opportunity with expected customer value. SEO Boardroom '
                                        'emphasizes those additional costs when researching placements. I '
                                        'will keep durability unresolved and avoid treating relief from a '
                                        'manual action as proof that a hosted section will retain its '
                                        'rankings. [SEO Boardroom — L6ZLGvFvaT8 @ 00:06:16]'}],
                 'completion_gate': 'Approve the journey only after every page has a defined next action '
                                    'and the application, calendar loading, and invitation checks have '
                                    'recorded outcomes. External opportunities require native '
                                    'participation checks, permission review, explicit expenses, and '
                                    'separate visibility stages. Unverified rankings, opt-ins, or '
                                    'attendance must not be presented as sales.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Buyer-Intent Content and AI Visibility Evidence',
                 'purpose': 'Build reviews and comparisons around a real purchasing decision, maintain the '
                            'facts that make recommendations useful, and inspect technical access before '
                            'rewriting. Track search and AI visibility alongside qualified actions without '
                            'treating citations, page counts, or traffic as interchangeable with '
                            'customers.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Choose a comparison or alternative query that expresses a real buyer '
                                  'decision, then inspect the current results and competing page format.',
                                  'Define the buyer profile and selection criteria before writing product '
                                  'sections, verdicts, or recommendations.',
                                  'Record current prices, features, evidence, and the actual dates '
                                  'checked; leave unsupported comparisons out of the recommendation.',
                                  "Inspect the live page's access and rendered answer before ordering "
                                  'another rewrite or expanding the content portfolio.',
                                  'Repeat AI citation checks and connect content reporting to qualified '
                                  'customer actions, keeping visibility and revenue evidence separate.'],
                 'fields': [{'name': 'buyer_decision_and_query',
                             'type': 'textarea',
                             'prompt': 'Select one comparison or alternative query and explain the '
                                       "purchase decision behind it. Describe the buyer's existing product "
                                       'awareness, the uncertainty your page should resolve, and why the '
                                       'topic deserves priority beyond its potential to attract more '
                                       'visits.',
                             'example': 'Planned topic: a comparison for buyers who already recognize two '
                                        'software options but need help choosing for a specific task. '
                                        'Vasco Aires emphasizes buying intent rather than traffic alone. I '
                                        "will prioritize the page only when I can explain the buyer's "
                                        'decision and provide a useful next action, not simply because '
                                        'visits look attainable. [Vasco Aires — C2ne_saHpSs @ 00:17:11]'},
                            {'name': 'competitor_page_and_search_inspection',
                             'type': 'textarea',
                             'prompt': 'Record a competing page, its target query, first-screen answer, '
                                       'structure, and apparent search intent. Inspect the same query '
                                       'yourself, then decide whether the opportunity calls for a new page '
                                       'or an update to content you already maintain.',
                             'example': "Research entry: inspect the competitor's opening screen, "
                                        'headings, and answer format, then search the same term to '
                                        'understand the decision being served. ToolTester Pro recommends '
                                        'this direct inspection rather than relying only on a winning URL. '
                                        'My next step will be a documented new-page or update decision '
                                        'based on the actual answer gap. [ToolTester Pro — boGwMjAxtuk @ '
                                        '00:10:43]'},
                            {'name': 'buying_criteria_and_best_for_segments',
                             'type': 'textarea',
                             'prompt': 'Draft the buying guide criteria before outlining individual '
                                       'product sections. Explain how those criteria create distinct '
                                       'best-for recommendations, what differences matter to the buyer, '
                                       'and which generic praise you will remove because it does not help '
                                       'anyone choose.',
                             'example': 'Drafting order: write the selection criteria first, then use '
                                        'those criteria to structure product sections and explain who each '
                                        'option fits. Seeking Profit recommends writing the buying guide '
                                        'before the reviews even when it appears later on the page. I will '
                                        'replace interchangeable praise with recommendations tied to the '
                                        "buyer's actual decision. [Seeking Profit — fo-OxsDnUVQ @ "
                                        '00:05:23]'},
                            {'name': 'alternative_fit_and_rejection_rule',
                             'type': 'textarea',
                             'prompt': 'Explain why the proposed alternative genuinely answers the '
                                       "searcher's request, including the job it performs and the relevant "
                                       'differences. Write a rejection rule for stretched comparisons so a '
                                       'tempting ranking opportunity does not override the suitability of '
                                       'the recommendation.',
                             'example': 'Rejection rule: pass on an alternative topic when the recommended '
                                        'product does not genuinely fit the request, even if the query '
                                        'appears reachable. Alex COLLINSEO warns against stretching the '
                                        'relationship and assuming rankings will produce sales. I will '
                                        'document the shared buyer job first and drop the topic when that '
                                        'connection cannot be explained. [Alex COLLINSEO — MzA9HXeEoMA @ '
                                        '00:06:11]'},
                            {'name': 'intent_specific_next_action',
                             'type': 'textarea',
                             'prompt': 'Assign the appropriate next action to each intent group your '
                                       'content serves. Distinguish readers seeking an affiliate program '
                                       'from buyers checking pricing or trials, and explain how your page '
                                       'avoids sending these different visitors into one generic pitch.',
                             'example': 'Action map: an affiliate-program query receives partnership '
                                        'information, while a pricing or trial query receives the relevant '
                                        'buying action. Tony Hayes distinguishes those intent groups '
                                        'instead of applying one pitch everywhere. I will inspect the '
                                        "page's main action against its query before publication and keep "
                                        'partnership interest separate from interest in purchasing the '
                                        'product. [Affiliate Marketing How To — H6zM2ZJJCzk @ 00:14:17]'},
                            {'name': 'changing_facts_and_check_dates',
                             'type': 'textarea',
                             'prompt': 'List the prices, features, and other changing facts that could '
                                       'invalidate your recommendation. Record what you actually checked '
                                       'and when, identify unresolved statements, and explain how you will '
                                       'prevent a displayed freshness date from implying work that never '
                                       'occurred.',
                             'example': 'Maintenance record: keep a short list of vulnerable facts, '
                                        'including the prices and features that determine the '
                                        'recommendation. The SEO Desk calls for real last-check dates '
                                        'rather than cosmetic freshness. My entry will state which facts '
                                        'were checked and leave unchecked items unresolved; changing a '
                                        'date alone will not count as a completed content review. [The SEO '
                                        'Desk — DyyeBcHNuHU @ 00:09:29]'},
                            {'name': 'attribute_specific_comparison_evidence',
                             'type': 'textarea',
                             'prompt': 'Define one customer profile and one product attribute that justify '
                                       'a focused comparison. Specify the real prices, specifications, and '
                                       'customer evidence needed to support the answer, and explain how '
                                       'this page differs from generic content repeated across product '
                                       'combinations.',
                             'example': 'Planned page: answer one attribute-specific comparison with '
                                        'actual prices, specifications, and customer evidence, rather than '
                                        'generating a broad wall of interchangeable text. Kasra Dash '
                                        'emphasizes real values for each attribute page. I will leave '
                                        'unsupported sections unfinished until the evidence is available '
                                        'instead of filling them with generic claims that could describe '
                                        'any competing product. [Kasra Dash — qP0qmnleojY @ 00:06:53]'},
                            {'name': 'live_page_access_and_answer_check',
                             'type': 'textarea',
                             'prompt': 'Describe the live page checks you will complete before '
                                       'commissioning another rewrite. Record status, canonical, '
                                       'indexability, rendered answer, and access obstructions, then '
                                       'explain which observed problem requires correction before weak '
                                       'visibility can reasonably be blamed on the written content.',
                             'example': 'Inspection order: check the live status, canonical, indexability, '
                                        'rendered answer, and access obstructions before requesting new '
                                        'copy. Digital Niche Agency identifies these checks as an '
                                        'operating gate. I will record the actual result for each item and '
                                        'resolve observed access problems first, rather than assuming '
                                        'another rewrite will fix an answer that cannot be reached '
                                        'properly. [Digital Niche Agency — ClT7JBQFJGA @ 00:38:45]'},
                            {'name': 'ai_citation_repeat_check',
                             'type': 'textarea',
                             'prompt': 'Define how you will record initial AI citations and repeat the '
                                       'same checks after an external placement. Identify the prompts and '
                                       'engines being observed, distinguish early inclusion from durable '
                                       'visibility, and state what remains unknown about resulting '
                                       'customer activity.',
                             'example': 'Planned record: preserve the prompts, engines, and initial '
                                        'citation observations, then repeat the checks rather than '
                                        'declaring the placement durable after five days. The Berlin '
                                        'presenters continued testing that exact durability question. My '
                                        'report will separate early answer inclusion from persistence and '
                                        'will not treat either observation as evidence that a prospect '
                                        'became a customer. [E-commerce Berlin Expo — ELiV_0RMFr4 @ '
                                        '00:19:31]'},
                            {'name': 'qualified_action_scoreboard',
                             'type': 'textarea',
                             'prompt': 'Choose the qualified customer action your content should generate '
                                       'and describe how you will report it alongside visits and '
                                       'visibility. Separate demos, trials, and purchases where relevant, '
                                       "and explain why another operator's result is context rather than "
                                       'your performance target.',
                             'example': 'Scoreboard plan: report qualified demos separately from visits, '
                                        'rankings, and AI citations, then keep purchases distinct from '
                                        'demo requests. Rob Hoffman reports roughly ten qualified weekly '
                                        "demos from Team Town's comparison pages using GA4. That is their "
                                        'reported outcome, not my forecast; my page earns a performance '
                                        'claim only when its own customer actions are observed. [Rob '
                                        'Hoffman — mPeQxVCunPU @ 00:32:55]'}],
                 'completion_gate': 'Publish or expand only when the buyer decision, comparison fit, '
                                    'selection criteria, and next action are explicit. Supporting facts '
                                    'must carry real check dates, technical access checks must have '
                                    'recorded outcomes, and citation reporting must distinguish initial '
                                    'inclusion from persistence. Keep visits, qualified actions, and '
                                    'purchases separate throughout the scoreboard.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Qualify Buyers, Route Calls, and Validate Lead Delivery',
                 'purpose': 'Build a buyer-first operating plan for pay-per-call or lead arbitrage. '
                            'Separate generated activity from payable outcomes, document delivery '
                            'requirements, and establish evidence that buyer capacity, routing, payment, '
                            'and acquisition economics justify expansion.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ["Choose one call or lead opportunity and describe the buyer's payable "
                                  'category before selecting traffic sources, landing pages, or publisher '
                                  'relationships.',
                                  'Complete every field with offer-specific conditions; leave unresolved '
                                  'requirements visibly pending rather than replacing them with '
                                  'assumptions about what buyers normally accept.',
                                  'Map the complete journey from visitor or publisher through '
                                  'qualification, routing, buyer response, revenue reporting, and payment '
                                  'to the intermediary.',
                                  'Use a small initial test to collect call recordings or lead response '
                                  'logs, then reconcile generated activity against accepted outcomes and '
                                  'actual payments.',
                                  'Authorize expansion only after the relevant launch checks, buyer '
                                  'capacity checks, and payment gates are satisfied; distinguish worked '
                                  'examples from your own measured results.'],
                 'fields': [{'name': 'buyer_category_and_payable_action',
                             'type': 'textarea',
                             'prompt': 'Define the service category buyers already purchase and the exact '
                                       "action they will pay for. Explain how your audience's language "
                                       'maps to that category, then distinguish an inquiry, a connected '
                                       'conversation, and an accepted payable outcome in your proposed '
                                       'campaign.',
                             'example': 'For a proposed hoarding cleanup campaign, I will first '
                                        'investigate buyers purchasing junk removal, cleanouts, or '
                                        'biohazard cleanup. I will not treat every ringing phone as earned '
                                        'revenue. My offer record will identify the accepted category and '
                                        "the buyer's qualification conditions before I create traffic "
                                        'content or estimate earnings. [WordsAtScale — DJFaYJ3O7aU @ '
                                        '00:00:47]'},
                            {'name': 'buyer_capacity_and_fallbacks',
                             'type': 'textarea',
                             'prompt': 'List prospective buyers, their available capacity, and the '
                                       'fallback route when a buyer cannot receive traffic. State whether '
                                       'you are building call distribution or a lead auction, and explain '
                                       'how your buyer coverage supports that specific operating model.',
                             'example': 'My call distribution plan will seek at least three buyers before '
                                        'depending on continuous availability. Each buyer entry will show '
                                        'capacity and an alternative destination during downtime. A single '
                                        'enthusiastic buyer will not count as a resilient operation, and I '
                                        'will keep unresolved coverage gaps visible before increasing '
                                        'traffic commitments. [Ringba — a4Aa0kexuh8 @ 00:04:37]'},
                            {'name': 'call_campaign_launch_checks',
                             'type': 'textarea',
                             'prompt': 'Create a launch checklist covering the telephone number, tracking, '
                                       'insertion order, caps, qualification filters, and traffic '
                                       'restrictions. For each item, specify what you will inspect and '
                                       'what unresolved condition prevents paid traffic from starting on '
                                       'the selected offer.',
                             'example': 'Before buying traffic for a call offer, I will test the published '
                                        'number and verify tracking against the agreed insertion order. I '
                                        'will also record caps, filters, and restrictions in the campaign '
                                        'record. Any missing requirement remains a launch blocker rather '
                                        'than an issue to discover after advertising money has been spent. '
                                        '[OfferVault — rsmZ9FBIPks @ 00:18:33]'},
                            {'name': 'call_economics_and_paid_outcomes',
                             'type': 'textarea',
                             'prompt': 'Build a compact economics record separating visitors, calls, paid '
                                       'calls, payout per accepted call, gross receipts, and acquisition '
                                       'costs. Explain which figures are measured and which remain '
                                       'illustrative, then identify the operational question that unpaid '
                                       'calls require you to investigate.',
                             'example': 'My comparison case records 165 visitors, nine calls, and three '
                                        'paid calls at $55 each, producing $165 gross against about $34 in '
                                        'reported costs. I will retain the May through July context and '
                                        'investigate why generated calls were not all payable rather than '
                                        'projecting nine payouts from nine calls. [Bens Review Videos — '
                                        'eqw-Rqw7PNY @ 00:05:05]'},
                            {'name': 'network_payment_proof',
                             'type': 'textarea',
                             'prompt': 'Describe the small initial test you will run with a new network, '
                                       'the call evidence you will retain, and how you will reconcile '
                                       'accepted outcomes with payments. State the payment milestone '
                                       "required before you increase the campaign's scale or operational "
                                       'commitments.',
                             'example': 'I will begin with a small network test and retain call recordings '
                                        'alongside the accepted call record. My expansion decision '
                                        'requires the network to have paid twice, not merely displayed '
                                        'earnings. Until both payments are confirmed, larger traffic '
                                        'commitments remain on hold even if early call volume appears '
                                        'encouraging. [WordsAtScale — DJFaYJ3O7aU @ 00:03:47]'},
                            {'name': 'lead_acquisition_spread',
                             'type': 'textarea',
                             'prompt': 'Write the acquisition and resale arithmetic for your chosen lead '
                                       'model. Distinguish publisher payments from paid traffic costs, '
                                       "identify the buyer's payable action, and label illustrative "
                                       'assumptions clearly so a positive example spread is not mistaken '
                                       'for verified campaign profit.',
                             'example': 'For an illustrative paid traffic model, I will record $2 per '
                                        'click, ten percent form completion, $20 cost per lead, and a $65 '
                                        'sale value. Hernandez describes the resulting $45 difference as '
                                        'profit in the example. I will keep this arithmetic separate from '
                                        'any claim that my campaign has achieved those results. [Rafael '
                                        'Hernandez ⚡️ — UGKIfB-aGpg @ 00:04:54]'},
                            {'name': 'active_auction_buyer_readiness',
                             'type': 'textarea',
                             'prompt': 'Assess whether a proposed lead auction has enough active buyer '
                                       'demand to function as intended. Record buyer appetite, available '
                                       'funding, and response speed, then explain why completed '
                                       'integrations alone do not establish a competitive or dependable '
                                       'market for incoming leads.',
                             'example': 'My auction readiness record will distinguish technically '
                                        'connected buyers from buyers that are hungry, funded, and fast. I '
                                        'will seek four to six or more active buyers in the vertical '
                                        'rather than describe one or two connections as a real auction. '
                                        'Unconfirmed buyer appetite will remain an explicit operating '
                                        'limitation. [Rafael Hernandez ⚡️ — A_xXkLg_0xI @ 00:05:29]'},
                            {'name': 'delivery_mapping_and_response_logs',
                             'type': 'textarea',
                             'prompt': 'Document the chosen delivery method, mapped fields, expected '
                                       'response, and timeout handling. Explain how you will inspect an '
                                       'individual lead when delivery is uncertain, including failed '
                                       'attempts, eventual buyer acceptance, and any returned price before '
                                       'recording the lead as sold.',
                             'example': 'For a delivery discrepancy, I will open the individual lead log '
                                        'instead of relying on an aggregate total. The demonstrated '
                                        'boberdoo sequence has two failed attempts before a third match '
                                        'returns a $25 price. My review will preserve that sequence so a '
                                        'failed first attempt is not mistaken for the final outcome. '
                                        '[boberdoo.com — SZ3UyKpdEjg @ 00:11:35]'},
                            {'name': 'bid_return_and_margin_configuration',
                             'type': 'textarea',
                             'prompt': 'Specify how the seller receives a price from your ping tree and '
                                       'how margin settings affect the offered amount. Record the best '
                                       'price return choice deliberately, then describe the test that will '
                                       'confirm the configured behavior before live delivery begins.',
                             'example': 'In my proposed boberdoo setup, I will record whether the best '
                                        'price return setting is no or yes and document the associated '
                                        'margin and maximum offer settings. I will test the returned '
                                        'seller price before launch rather than assume the highest buyer '
                                        'bid is automatically passed through under every configuration. '
                                        '[boberdoo.com — SZ3UyKpdEjg @ 00:04:50]'},
                            {'name': 'publisher_payment_and_measurement_plan',
                             'type': 'textarea',
                             'prompt': 'Describe the payment relationship among buyer, arbitrage company, '
                                       "and publisher. Identify the publisher's preferred performance "
                                       'measure, explain how you will communicate offer economics in that '
                                       'language, and state how collected buyer revenue will be '
                                       'distinguished from obligations owed to publishers.',
                             'example': 'My publisher agreement outline will keep the buyer paying the '
                                        'arbitrage company, followed by the company paying publishers. I '
                                        'will record buyer receipts separately from publisher amounts '
                                        'owed, so incoming revenue is not confused with the retained '
                                        'spread. Publisher discussions will use the performance measure '
                                        "appropriate to the publisher's traffic rather than headline "
                                        'payouts alone. [Eric Beer — lI1fQGR95XA @ 00:06:08]'}],
                 'completion_gate': 'Complete all ten fields and identify every unresolved buyer or '
                                    'delivery requirement. Do not launch paid calls without verified '
                                    'numbers, tracking, terms, caps, filters, and restrictions. Do not '
                                    'expand a new call network before two payments. For lead delivery, '
                                    'require a confirmed test response and distinguish active buying '
                                    'demand from merely completed integrations.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Verify Attribution and Bound Paid Acquisition',
                 'purpose': 'Connect referral identifiers, conversion events, buyer acceptance, and '
                            'advertising reports into an inspectable acquisition record. Establish what '
                            'earns a commission, prove the tracking journey, and evaluate paid traffic '
                            'using attributable outcomes rather than disconnected dashboards.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Select one offer and one paid traffic route, then define the precise '
                                  'conversion event that should create revenue or commission.',
                                  'Trace the identifier from the original click through the destination '
                                  "and back through the advertiser's conversion response without inventing "
                                  'platform macros.',
                                  'Run the relevant customer journey and inspect event details, rejection '
                                  'reasons, duplicate handling, and advertising platform receipt before '
                                  'trusting campaign totals.',
                                  'Separate attributed practitioner examples from your own campaign '
                                  'assumptions, and distinguish affiliate payouts, acquisition costs, and '
                                  'any proposed backend revenue.',
                                  'Keep spending and expansion conditional on working conversion delivery, '
                                  'applicable offer restrictions, and funding appropriate to the chosen '
                                  'traffic model.'],
                 'fields': [{'name': 'conversion_and_commission_definition',
                             'type': 'textarea',
                             'prompt': 'Define the action that earns commission, the reward amount or '
                                       'percentage, and the duration or cancellation condition. '
                                       'Distinguish initial registration from the billing or customer '
                                       'milestone that actually creates payable revenue, and identify the '
                                       'system responsible for recording that event.',
                             'example': 'For a Task Flow style subscription setup, my configuration record '
                                        'will specify a twenty percent monthly commission lasting until '
                                        'the customer cancels. Registration alone will not be described as '
                                        'a completed stream of future earnings. I will connect the reward '
                                        'definition to subscription billing and preserve the cancellation '
                                        'condition in revenue expectations. [Daniel | Tech & Data — '
                                        'SWQet1wMMyA @ 00:03:03]'},
                            {'name': 'transaction_identifier_round_trip',
                             'type': 'textarea',
                             'prompt': 'Map where the transaction identifier originates, how it enters the '
                                       'destination URL, where it is retained, and how the advertiser '
                                       'returns it. Record evidence for both directions and explain what '
                                       'you will inspect when an expected conversion cannot be attributed.',
                             'example': 'My Everflow test record will show the transaction identifier '
                                        'leaving in the base destination URL and returning with the '
                                        "advertiser's conversion response. I will inspect both directions "
                                        'before blaming a missing dashboard total. A destination that '
                                        'receives an identifier does not prove that the advertiser '
                                        'correctly returns it when the conversion happens. [Everflow - '
                                        'Partner Marketing Platform — NSernIgs5XQ @ 00:14:26]'},
                            {'name': 'postback_rejection_investigation',
                             'type': 'textarea',
                             'prompt': 'Describe the evidence you will collect when a postback arrives but '
                                       'does not create the expected conversion. Include acceptance '
                                       'status, rejection details, event identity, and offer association, '
                                       'then explain how a corrected test will establish that the '
                                       'underlying mismatch is resolved.',
                             'example': 'If an Everflow conversion is absent, I will open the advertiser '
                                        'postback details and read the rejection reason. In the '
                                        'demonstrated failure, the event identifier did not belong to the '
                                        'offer. My corrective action will address that association and '
                                        'repeat the test, rather than treating receipt of any postback as '
                                        'success. [Everflow - Partner Marketing Platform — FMpj69YFsHA @ '
                                        '00:23:47]'},
                            {'name': 'campaign_integration_and_event_parameter',
                             'type': 'textarea',
                             'prompt': 'Record the selected campaign integration and the exact custom '
                                       'conversion parameter you intend to send. Explain how you will '
                                       'preserve required formatting and verify campaign selection, '
                                       'keeping a configured account integration separate from an '
                                       'integration actually enabled for the tested campaign.',
                             'example': "My ClickFlare checklist will include the campaign's selected "
                                        'pixel integration and the custom conversion parameter. For a '
                                        'custom conversion, I will make ct match the conversion parameter, '
                                        'preserve case, and remove spaces. I will compare the configured '
                                        'value with the test result instead of assuming a similarly named '
                                        'event will match. [ClickFlare — cSLdoNWYxfE @ 00:13:26]'},
                            {'name': 'facebook_click_and_duplicate_evidence',
                             'type': 'textarea',
                             'prompt': 'Plan a user journey test for the Facebook conversion flow, '
                                       'including creation of the Facebook click identifier and inspection '
                                       'of the outgoing payload. State the event identifier used for '
                                       'duplicate handling and distinguish transport success from '
                                       'recognition by the advertising platform.',
                             'example': 'I will click through the Facebook journey as a user would and '
                                        'inspect the conversion payload for the actual Facebook click '
                                        'identifier. A successful conversion response alone will not '
                                        'satisfy my test because Carlos says Facebook will not recognize '
                                        'the conversion when that identifier is missing. Duplicate '
                                        'handling will receive a separate check. [Carlos Corona — '
                                        'zOQZw8jApe0 @ 00:28:16]'},
                            {'name': 'conversion_maturity_and_quality',
                             'type': 'textarea',
                             'prompt': 'Specify when an apparent conversion becomes mature enough for your '
                                       "campaign's revenue decision. Identify shipment, refund timing, "
                                       'buyer acceptance, or customer quality conditions relevant to the '
                                       'offer, and explain how preliminary actions remain separate from '
                                       'the payable outcomes used to evaluate acquisition.',
                             'example': 'For an offer with a refund period, I will define the revenue '
                                        'decision around the agreed mature conversion rather than assume '
                                        'every initial order is final. RedTrack describes establishing '
                                        'conversion after shipment or after the refund period expires. My '
                                        'record will name the selected condition and keep earlier activity '
                                        'distinguishable from that event. [RedTrack.io — oZcc_4NfA3g @ '
                                        '00:04:55]'},
                            {'name': 'payout_and_acquisition_comparison',
                             'type': 'textarea',
                             'prompt': 'Compare the offer payout with the acquisition cost you can '
                                       'actually attribute to the selected funnel. Identify the keyword '
                                       'intent and landing page alignment behind the comparison, and label '
                                       'any practitioner benchmark as an example rather than an expected '
                                       'outcome for your campaign.',
                             'example': "My benchmark note will identify Gomes's reported $57 affiliate "
                                        'payout and acquisition cost below $35 for an aligned article '
                                        'style funnel using specific middle funnel keywords. I will not '
                                        'copy those figures into my results column. My campaign must '
                                        'supply its own attributable sales and costs before I describe its '
                                        'economics as favorable. [Aldo Gomes — rc7rwCDzbg4 @ 00:00:00]'},
                            {'name': 'advertising_platform_conversion_receipt',
                             'type': 'textarea',
                             'prompt': 'Create a reconciliation procedure between the affiliate tracker '
                                       'and the advertising platform. Explain how you will verify keyword '
                                       'attribution and conversion delivery separately, investigate a '
                                       'tracked sale missing from platform reporting, and avoid optimizing '
                                       'spend from an incomplete view of campaign outcomes.',
                             'example': 'My Google campaign check will compare a tracked sale with '
                                        "Google's received conversion record. Gomes installed ClickMagick "
                                        'but omitted audience optimization, leaving a sale visible in '
                                        "tracking and absent from Google's reporting. I will therefore "
                                        'verify both keyword attribution and delivery instead of treating '
                                        'installation of the tracking tool as proof that reporting is '
                                        'complete. [Aldo Gomes — TpcIvpsamnM @ 00:07:05]'},
                            {'name': 'brand_bidding_permission_and_payment',
                             'type': 'textarea',
                             'prompt': "Document the product's brand bidding restrictions and the evidence "
                                       'that commissions remain payable for your proposed campaign. '
                                       'Explain how you will respond when an advertisement stays live but '
                                       'the vendor relationship changes, keeping ad platform availability '
                                       'separate from permission to earn commissions.',
                             'example': "Before using a product's brand terms, I will inspect its "
                                        'restrictions and verify that the vendor still pays commissions '
                                        'for the activity. A live Google or Microsoft advertisement will '
                                        'not serve as permission evidence. Mana describes product bans '
                                        'that do not automatically stop the advertisement, so I will check '
                                        'the relationship directly. [Ivan Mana — HRjV85omYRA @ 00:07:43]'},
                            {'name': 'initial_budget_and_expansion_conditions',
                             'type': 'textarea',
                             'prompt': 'Choose an initial budget appropriate to the traffic route and '
                                       'state what must be observed before increasing spend. Include '
                                       'working tracking, landing page visits, and relevant acquisition '
                                       'signals, while distinguishing a small opening campaign example '
                                       'from the larger funding commitment discussed for native '
                                       'advertising.',
                             'example': 'For a Facebook opening test, I will use the demonstrated $25 '
                                        'daily campaign budget as a planning reference, not a profit '
                                        'guarantee. Before increasing spend, I will inspect tracking, '
                                        'landing page visitors, and potential CPMs. I will not transfer '
                                        'that opening budget assumption to a native campaign with a '
                                        'different stated funding commitment. [Powerhouse Affiliate — '
                                        'cuIiOD3qJ2o @ 00:15:12]'}],
                 'completion_gate': 'Complete all ten fields and demonstrate a traceable identifier round '
                                    'trip, the correct accepted conversion event, and receipt by the '
                                    'relevant advertising platform. Resolve rejection details and '
                                    'applicable duplicate handling. Keep brand bidding blocked where '
                                    'permission or commission eligibility is unresolved, and do not expand '
                                    'spending using illustrative payouts or incomplete conversion '
                                    'reporting.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Grow a Relevant Newsletter and Audit Affiliate Promotions',
                 'purpose': 'Design newsletter acquisition around reader value, source-level engagement, '
                            'and acquisition payback. Pair welcome flows and paid recommendations with '
                            'visible relationship disclosures, supported claims, and checks that preserve '
                            'trust across email, video, social posts, and advertising.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Define the specific reader and promised outcome before choosing paid '
                                  'subscriber acquisition, recommendation partners, or referral rewards.',
                                  'Carry the acquisition promise into the welcome experience and evaluate '
                                  'reader sources over a meaningful observation period rather than a few '
                                  'early days.',
                                  'Resolve paid recommendation eligibility and reapplication consequences '
                                  'before applying or counting recommendation income in the acquisition '
                                  'plan.',
                                  'Review every affiliate recommendation at its actual point of '
                                  'presentation, including mobile layouts, individual posts, and visual or '
                                  'spoken endorsements.',
                                  'Keep result claims, editorial facts, and visible advertising copy '
                                  'supported and checked; remove unsupported earnings promises before '
                                  'releasing the completed campaign.'],
                 'fields': [{'name': 'reader_profile_and_subscriber_value',
                             'type': 'textarea',
                             'prompt': "Define a good subscriber in terms of the audience's specific needs "
                                       'and the value your newsletter delivers. Explain how you will '
                                       'estimate subscriber worth before choosing an acquisition '
                                       'allowance, and distinguish relevant readers from a larger but '
                                       'poorly matched subscriber count.',
                             'example': 'My proposed local newsletter will define a good subscriber as '
                                        'someone seeking its specific local information rather than anyone '
                                        'willing to enter an email address. I will document the reader '
                                        'benefit and the basis for subscriber value before setting an '
                                        'acquisition allowance. A lower signup cost will not override a '
                                        'mismatch with that audience. [SparkLoop — i_xgpz4ZZB8 @ '
                                        '00:13:27]'},
                            {'name': 'landing_promise_and_welcome_continuity',
                             'type': 'textarea',
                             'prompt': 'Write the acquisition promise and explain how the welcome email '
                                       "repeats it for the subscriber's actual source. Identify the "
                                       'referring newsletter when relevant, restore benefits a referred '
                                       'reader may not have seen, and give the subscriber a clear reason '
                                       'to continue reading.',
                             'example': 'For subscribers arriving through a partner newsletter, my welcome '
                                        'draft will name that referring publication and explain the '
                                        'benefits of receiving my newsletter. I will not assume these '
                                        'readers studied my landing page. The opening message will '
                                        'reintroduce the audience promise before moving toward an offer or '
                                        'asking the new subscriber for further action. [SparkLoop — '
                                        'i_xgpz4ZZB8 @ 00:32:17]'},
                            {'name': 'paid_source_observation_plan',
                             'type': 'textarea',
                             'prompt': 'Set a source-level review plan for paid subscriber acquisition, '
                                       'including the observation period and engagement evidence you will '
                                       'inspect. Explain how you will avoid drawing conclusions from tiny '
                                       'samples or blaming an entire channel for the performance of one '
                                       'weak source.',
                             'example': 'I will review each paid subscriber source over approximately '
                                        'thirty days instead of judging it after three days. The review '
                                        'will consider downstream engagement and sample size before I '
                                        'decide whether the source deserves further spending. A poor '
                                        'result from one source will trigger investigation rather than an '
                                        'immediate verdict against the entire channel. [SparkLoop — '
                                        'uVhFrwe935U @ 00:26:10]'},
                            {'name': 'acquisition_cost_and_payback_record',
                             'type': 'textarea',
                             'prompt': 'Create a record separating subscriber acquisition cost, subsequent '
                                       'earnings, and the time needed to recover acquisition spending. '
                                       'Label reported cost ranges as contextual benchmarks, identify '
                                       'variation by creative or week, and state which observations would '
                                       'support continued paid growth for your newsletter.',
                             'example': "My benchmark record will show Office Party's reported optimized "
                                        'cost of $0.50 to $1.50 per subscriber after audience and creative '
                                        'testing. I will preserve the variation by week and creative '
                                        'rather than assume that range is immediately available. My own '
                                        'acquisition costs and subsequent earnings will determine whether '
                                        'continued spending is justified. [SparkLoop — 6rbq9lhZYqY @ '
                                        '00:14:09]'},
                            {'name': 'paid_recommendation_application_gate',
                             'type': 'textarea',
                             'prompt': 'List the eligibility requirements and reapplication consequences '
                                       'you must resolve before seeking paid recommendation access. '
                                       'Explain how pending acceptance affects your acquisition economics, '
                                       'and record the questions that would make waiting more appropriate '
                                       'than submitting an application with unresolved requirements.',
                             'example': 'Before applying for paid recommendations, I will ask what '
                                        'requirements apply and whether rejection permits another '
                                        'application. Zelaya reports a final rejection and says knowing '
                                        'the consequence would have changed the timing. I will keep '
                                        'expected recommendation income out of committed acquisition '
                                        'funding until eligibility and the application outcome are '
                                        'sufficiently clear. [Wanda Zelaya Real Estate Channel — '
                                        'bHypgQE6iLY @ 00:02:53]'},
                            {'name': 'referral_reward_and_sharing_path',
                             'type': 'textarea',
                             'prompt': 'Choose a referral reward that fits your readers and explain how '
                                       'the newsletter makes sharing immediately actionable. Identify the '
                                       'referral link placement and concrete sharing destinations, then '
                                       'assess whether the reward motivates participation without '
                                       'undermining the value of your paid services.',
                             'example': "My referral section will include the reader's sharing link and "
                                        'concrete destinations inside the newsletter, rather than send '
                                        'readers to a separate hub just to discover how sharing works. I '
                                        'will review reward fit separately and avoid choosing a service '
                                        'merely because its normal price looks impressive on a referral '
                                        'reward ladder. [SparkLoop — ucyDCgyYRko @ 00:47:08]'},
                            {'name': 'affiliate_relationship_language',
                             'type': 'textarea',
                             'prompt': 'Draft the relationship explanation beside each affiliate '
                                       'recommendation or link. Specify what compensation connection the '
                                       'reader needs to understand and where the wording appears, keeping '
                                       'the individual recommendation clear rather than relying only on a '
                                       'general account notice or distant disclosure page.',
                             'example': "Beside a recommended software link, my draft will state, 'I may "
                                        "receive a commission if you click on this link.' The explanation "
                                        'will sit next to the recommendation rather than depend on readers '
                                        'finding a separate page. I will repeat the relevant relationship '
                                        'explanation wherever an individual affiliate recommendation would '
                                        'otherwise leave compensation unclear. [Lawyer Explains - Erika '
                                        'Kullberg — 723U5nGxhTU @ 00:05:55]'},
                            {'name': 'mobile_and_format_disclosure_review',
                             'type': 'textarea',
                             'prompt': 'Plan a presentation review that checks disclosure visibility on '
                                       'phones and matches the disclosure to the endorsement format. '
                                       'Explain how visual and spoken recommendations will carry the '
                                       'relationship explanation, and identify any collapsed caption or '
                                       'layout that could hide it from the audience.',
                             'example': 'My release checklist will include a phone view of the '
                                        'recommendation, not just the desktop layout. If the relationship '
                                        'explanation becomes hard to see on the smaller screen, I will '
                                        'change the placement before release. A disclosure that looks '
                                        'clear on a computer will not count as a completed mobile '
                                        'presentation check. [Find Your Influence — Hq1UDKzazVQ @ '
                                        '00:11:57]'},
                            {'name': 'claims_and_earnings_support',
                             'type': 'textarea',
                             'prompt': 'Inventory the product claims, testimonials, before and after '
                                       'images, and earnings statements used in your promotion. Identify '
                                       'the supporting record for each item, distinguish achieved results '
                                       'from targets, and remove claims whose accuracy depends only on '
                                       'trusting supplied advertiser or network copy.',
                             'example': 'My promotion review will flag every testimonial, product '
                                        'performance statement, and before and after image for supporting '
                                        'documentation. Copy supplied by a network will receive the same '
                                        'review as copy I write. I will remove unsupported claims rather '
                                        'than assume the advertiser already completed the necessary checks '
                                        'or that repeated promotional wording establishes truth. [AM Days '
                                        '— 0ELJUfzzK1M @ 00:06:27]'},
                            {'name': 'competitor_name_ad_copy_controls',
                             'type': 'textarea',
                             'prompt': 'Review any competitor keyword campaign separately from the visible '
                                       'advertisement it can generate. Record whether dynamic keyword '
                                       'insertion or automatically created assets are enabled, explain how '
                                       'competitor names could enter public copy, and specify the '
                                       'inspection required before the campaign is released.',
                             'example': 'For a proposed competitor keyword campaign, I will avoid dynamic '
                                        'keyword insertion and turn off automatically created assets. My '
                                        'review will inspect visible ad copy rather than assume keyword '
                                        'selection and displayed wording are the same issue. The campaign '
                                        'remains pending until the inspected advertisement no longer '
                                        'introduces competitor names through those automated features. '
                                        '[Analytics Playbook: Learn Marketing Analytics — HMW_yXXlRPs @ '
                                        '00:02:22]'}],
                 'completion_gate': 'Complete all ten fields with a specific reader promise, source-level '
                                    'observation plan, and acquisition payback record. Resolve '
                                    'recommendation eligibility before relying on that income. Check '
                                    'relationship explanations beside individual recommendations, inspect '
                                    'mobile and endorsement formats, and remove unsupported claims. Do not '
                                    'release competitor campaigns with unreviewed automated name insertion '
                                    'or treat projected newsletter revenue as achieved income.'}]}
