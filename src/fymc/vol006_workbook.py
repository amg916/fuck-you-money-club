from __future__ import annotations

def build_volume_006_workbook() -> dict:
    return {'workbook_id': 'wb-006-productized-ai-agencies',
 'volume_id': 'vol-006-productized-ai-agencies',
 'title': 'Productized AI Agencies — Practitioner Testimony Operator Workbook',
 'subtitle': 'Productized AI Agencies: Choose a Paid Business Outcome, Define Repeatable Delivery, Sell '
             'Useful Audits, Build Bounded Retainers, and Win Clients Through Verified Outreach and '
             'Reliable CRM Data',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Define the Outcome, Validate Demand, and Bound the Service',
                 'purpose': 'Turn an automation idea into a business offer someone is willing to buy. '
                            'Specify the outcome, reusable foundation, client-specific work, commercial '
                            'terms, request process, and capacity limits before treating a productized '
                            'service as ready for delivery.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Choose one business problem and describe its effect on time, money, or '
                                  'focus before naming tools, agents, integrations, or subscription '
                                  'features.',
                                  'Record the evidence of willingness to pay separately from enthusiasm '
                                  'about a demonstration, and leave unconfirmed purchase decisions visibly '
                                  'unresolved.',
                                  'Separate the reusable service foundation from the business knowledge, '
                                  'account connections, customization, and testing required for each '
                                  'individual client.',
                                  'Write the initial scope, payment terms, request queue, communication '
                                  'process, and capacity limits together so that the commercial promise '
                                  'matches delivery.',
                                  'Review every financial comparison for attribution and missing costs; '
                                  'distinguish proposed package prices, reported receipts, operating '
                                  'expenses, and teaching income.'],
                 'fields': [{'name': 'business_outcome',
                             'type': 'textarea',
                             'prompt': 'Describe the business result your service will sell, identifying '
                                       'the recurring task it removes and whether the main benefit '
                                       'concerns time, money, or focus. Replace descriptions of workflow '
                                       'components with language the business owner would use when '
                                       'explaining the purchase.',
                             'example': "Proposed offer: remove the owner's recurring LinkedIn research "
                                        'and writing burden so they can focus elsewhere. The purchase is '
                                        "relief from that work, not access to workflow nodes. Nate's "
                                        'reported first $1,200 sale illustrates the distinction; it does '
                                        'not establish what another buyer will pay. [Nate Herk | AI '
                                        'Automation — SAerRtQLD0I @ 00:00:21]'},
                            {'name': 'willing_buyer_evidence',
                             'type': 'textarea',
                             'prompt': 'Identify the business expected to pay, the problem they have '
                                       'acknowledged, and the purchase decision still required before '
                                       'building. Explain how you will avoid treating your own excitement, '
                                       'an attractive demonstration, or an unrequested workflow as '
                                       'evidence of customer demand.',
                             'example': 'Build decision: remain at the offer stage until a business agrees '
                                        'to pay for the identified result. A workflow that looks useful to '
                                        'its creator is not enough. Noah changed their sequence after '
                                        'building workflows nobody wanted, so the proposed service must '
                                        'secure a willing buyer before development begins. [Noah Epstein — '
                                        'fMdUS6amki0 @ 00:02:14]'},
                            {'name': 'reusable_base_and_customization',
                             'type': 'textarea',
                             'prompt': 'Separate the reusable foundation from the client-specific work '
                                       'required to make it useful. List the business knowledge the owner '
                                       'must contribute, the configuration your service includes, and why '
                                       'delivering a template bundle alone would fail to fulfill the '
                                       'promised business outcome.',
                             'example': 'Service design: reuse a strong starting system, then customize it '
                                        "with the owner's subject-matter knowledge. The client supplies "
                                        'the business context needed to make the result relevant; the '
                                        'agency supplies the adaptation. A template bundle is not the '
                                        'completed service and should not be presented as equivalent to '
                                        'it. [Nate Herk | AI Automation — SAerRtQLD0I @ 00:04:08]'},
                            {'name': 'initial_scope_and_payment',
                             'type': 'textarea',
                             'prompt': 'Write the initial service boundary before configuration begins, '
                                       'covering connected tools, included agents, setup payment, and work '
                                       'excluded from the first delivery. Make the distinction between the '
                                       'initial package and later expansion clear enough to prevent an '
                                       'open-ended implementation promise.',
                             'example': 'Initial scope: list the connected tools, limit the first package '
                                        'to three agents, and document setup-payment terms before '
                                        'client-specific configuration. Keep additional agents outside '
                                        "that initial promise. Mikey's approach makes these boundaries "
                                        'explicit rather than letting an appealing growth-suite '
                                        'description become permission to keep adding work without '
                                        'agreement. [Mikey No Code — i4z0kCcByY8 @ 00:38:08]'},
                            {'name': 'package_price_and_status',
                             'type': 'textarea',
                             'prompt': 'Record the setup charge and recurring charge you are considering, '
                                       'then identify exactly what each covers. Label borrowed price '
                                       'examples as package terms rather than collected revenue, and '
                                       'explain which delivery responsibilities make the recurring portion '
                                       'different from the initial installation.',
                             'example': 'Pricing reference: Mikey presents a real estate growth suite at '
                                        '$2,500 setup plus $750 monthly. The package covers three agents, '
                                        'connections, customization, testing, and ongoing operations. '
                                        'Record these as proposed commercial terms, not proof of receipts, '
                                        'and keep initial integration work distinct from the continuing '
                                        'operating responsibilities being offered. [Mikey No Code — '
                                        'i4z0kCcByY8 @ 00:29:31]'},
                            {'name': 'request_and_communication_rules',
                             'type': 'textarea',
                             'prompt': 'Define where clients submit requests, how they set priorities, and '
                                       'which communication routes the service will accept. Explain how '
                                       'you will handle requests arriving through another channel without '
                                       'silently creating a separate process that increases mistakes or '
                                       'weakens the published delivery boundaries.',
                             'example': 'Operating rule: customers use the published request and '
                                        'communication process rather than introducing email exceptions or '
                                        'their own preferred tools. Requests arriving elsewhere are '
                                        'redirected into that process. Williams describes mistakes caused '
                                        'by accommodating separate channels, making consistency part of '
                                        'reliable delivery rather than merely a preference for fewer '
                                        'conversations. [The Futur — 8vwgUwgH2Js @ 00:29:33]'},
                            {'name': 'capacity_and_client_selection',
                             'type': 'textarea',
                             'prompt': 'State how you will decide whether another client fits the '
                                       "service's available capacity. Include the effect of project "
                                       'selection on breaks, sickness, and time away, and identify the '
                                       'situation in which accepting additional revenue would make the '
                                       'existing delivery promise unsustainable.',
                             'example': 'Capacity decision: do not accept another subscription solely '
                                        'because the buyer is ready to pay. Check whether the current '
                                        'workload still leaves room for breaks, sickness, and time away. '
                                        'Williams describes earlier difficulty refusing money as removing '
                                        'that flexibility, so client selection must protect the ability to '
                                        'serve existing accounts. [Creative Crew with Brad Hussey — '
                                        'o-UR3rkPgJ4 @ 00:06:09]'},
                            {'name': 'first_project_foundation',
                             'type': 'textarea',
                             'prompt': 'Describe the extra attention the first client project needs and '
                                       'what reusable foundation it should establish for later requests. '
                                       'Identify which preferences or decisions should carry forward so '
                                       'that repeat delivery does not restart discovery and exploration '
                                       'from the beginning each time.',
                             'example': 'Delivery plan: spend more effort on the first project to '
                                        "establish the client's aesthetic foundation. Preserve that "
                                        'direction for later requests instead of reopening the same '
                                        'exploration each time. Williams uses this early investment to '
                                        'support repeat delivery; the subscription still depends on '
                                        'finished work, not simply granting access to a queue. [Creative '
                                        'Crew with Brad Hussey — o-UR3rkPgJ4 @ 00:14:21]'},
                            {'name': 'daily_delivery_review',
                             'type': 'textarea',
                             'prompt': 'Specify what you will inspect across active client requests each '
                                       'day and which decisions require your attention. Distinguish useful '
                                       'administrative automation from a review habit that catches changed '
                                       'requests, approvals, and unresolved issues before they disappear '
                                       'from your awareness during recurring delivery.',
                             'example': 'Daily review: inspect client cards for changed requests, '
                                        'approvals, and unresolved issues before updating the tracking '
                                        'record. Keep that inspection even if the update itself could be '
                                        'automated. Williams manually updates Airtable because reviewing '
                                        'the cards creates awareness that a fully automated administrative '
                                        'step would remove from their daily routine. [Brett Malinowski — '
                                        'IvZxfvECZnA @ 00:37:20]'},
                            {'name': 'revenue_claim_classification',
                             'type': 'textarea',
                             'prompt': 'Classify the revenue examples influencing your expectations by '
                                       'separating agency or consultancy receipts from teaching and '
                                       'community income. Record the stated period and whether a figure is '
                                       'an average or peak, then explain why those distinctions matter '
                                       'when evaluating your own proposed service.',
                             'example': 'Comparison note: Zubair reports consultancy revenue averaging '
                                        '$10,000 to $15,000 monthly, with a highest month of $30,000. Keep '
                                        'those figures separate from the larger cumulative story, whose '
                                        'majority came from teaching-community income. Neither the peak '
                                        'nor the blended total should become the expected monthly result '
                                        'for a new agency offer. [Zubair Trabzada | AI Workshop — '
                                        'XUYvDbAv1IA @ 00:01:14]'}],
                 'completion_gate': 'Proceed only when a business is willing to pay for a named outcome, '
                                    'the reusable base and client-specific work are separated, and the '
                                    'initial scope and payment terms are explicit. The request process '
                                    'must be workable within available capacity, and financial comparisons '
                                    'must distinguish package prices, agency receipts, and teaching '
                                    'income.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Design the Paid Audit and Earn a Bounded Retainer',
                 'purpose': 'Package useful diagnosis before development, gather evidence from actual '
                            'work, and turn agreed improvements into a priced roadmap. Define recurring '
                            'service only where continuing work, accountable delivery, realistic labor '
                            'allowances, and explicit scope make the relationship workable.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ["Choose the audit's entry scope and price, keeping practitioner pricing "
                                  'examples separate from delivery costs and from your own confirmed '
                                  'sales.',
                                  'Secure interview access and schedule the final presentation during '
                                  'onboarding rather than allowing a missing participant to stall the '
                                  'entire engagement.',
                                  'Observe real work, map handoffs, establish a measurable baseline, and '
                                  'challenge generated recommendations before producing the finished audit '
                                  'presentation.',
                                  'Use successful project delivery to discuss continuing needs, while '
                                  'distinguishing maintenance, prepaid build time, and new features within '
                                  'the recurring offer.',
                                  'Check labor exposure, platform charges, client fit, approval authority, '
                                  'change handling, and exit terms before committing to a monthly '
                                  'relationship.'],
                 'fields': [{'name': 'paid_audit_entry_offer',
                             'type': 'textarea',
                             'prompt': 'Define a small paid audit that can stand on its own before '
                                       'implementation is sold. State the entry price under consideration, '
                                       'the diagnostic work included, and the boundary preventing a fast '
                                       'assessment from expanding into an unpaid development project or an '
                                       'unlimited consulting engagement.',
                             'example': 'Entry offer: a small, fast-to-deliver bronze AI business audit, '
                                        "using Antonio's $1,500 to $3,000 range as a pricing reference. "
                                        'The purchase is diagnosis before development, not a promise to '
                                        'build every opportunity discovered. Keep the audit deliverable '
                                        'distinct from any implementation proposal that might follow the '
                                        'assessment for the client. [Belt Course — YaFtlj9qXQc @ '
                                        '00:04:30]'},
                            {'name': 'audit_access_and_calendar',
                             'type': 'textarea',
                             'prompt': 'List the people whose participation is necessary, confirm access '
                                       'to them, and set the final presentation date during onboarding. '
                                       'Explain how the interview schedule will avoid leaving the audit '
                                       'dependent on one unavailable participant while the promised '
                                       'delivery remains unspecified for the client.',
                             'example': 'Onboarding plan: book the final presentation immediately and '
                                        'coordinate interviewees together. Confirm who must attend before '
                                        'the audit starts. Dunn reports an audit waiting three weeks for '
                                        'one missing person, so interview access is a delivery dependency '
                                        'to resolve early rather than an administrative detail to chase '
                                        'after analysis begins. [Andrew Dunn | AI Consulting — LSmxwtNHu4k '
                                        '@ 00:06:31]'},
                            {'name': 'observed_workflow_and_handoffs',
                             'type': 'textarea',
                             'prompt': "Map the workflow from an employee's actual screen-shared actions "
                                       'rather than relying only on the written procedure. Capture the '
                                       'steps, handoffs, friction, and discrepancies they reveal, while '
                                       'keeping your questions focused on understanding the work instead '
                                       'of prematurely supplying automation answers during the interview.',
                             'example': 'Interview approach: ask the employee to share their screen and '
                                        'explain what they actually do, including each handoff. Compare '
                                        'that account with the written procedure rather than assuming the '
                                        'procedure is accurate. Meyers emphasizes that the interview is '
                                        'not about giving answers; observed work can contradict the '
                                        'documented process. [Carly Meyers — stoZ9wFob2E @ 00:42:17]'},
                            {'name': 'baseline_and_outcome_measure',
                             'type': 'textarea',
                             'prompt': 'Choose the business measure that will show whether the proposed '
                                       'improvement worked, and record its condition before '
                                       'implementation. Define what will be measured afterward using the '
                                       'same comparison, keeping the expected benefit separate from an '
                                       'improvement that has already been demonstrated through actual '
                                       'measurement.',
                             'example': "Measurement plan: record the selected workflow's current "
                                        'performance before changing it, then compare the same measure '
                                        'after implementation. Leave the improvement unconfirmed until '
                                        "both observations exist. Hartnell's point is that without a "
                                        'before-and-after comparison, the team cannot tell whether the '
                                        'implementation succeeded, even when the new workflow appears '
                                        'impressive. [Tom Hartnell — WFW7vb6wXZM @ 00:10:58]'},
                            {'name': 'recommendation_review_and_feasibility',
                             'type': 'textarea',
                             'prompt': 'Describe how you will challenge initial generated recommendations '
                                       'and test their feasibility before preparing the polished roadmap. '
                                       'Identify what must be revised with the client while priorities are '
                                       'still easy to change, rather than allowing presentation quality to '
                                       'conceal weak diagnosis or unsupported recommendations.',
                             'example': 'Review sequence: discuss a bullet list of proposed improvements '
                                        'before building the finished deck. Use that conversation to '
                                        'revise feasibility and priorities while changes remain '
                                        'inexpensive in effort. Dunn presents this intermediate discussion '
                                        'as a way to align the plan before turning it into the polished '
                                        "version of the client's decision. [Andrew Dunn | AI Consulting — "
                                        'LSmxwtNHu4k @ 00:10:24]'},
                            {'name': 'delivery_to_retainer_conversation',
                             'type': 'textarea',
                             'prompt': 'Plan the project handoff so the completed result receives most of '
                                       'the attention before you introduce continuing opportunities. Write '
                                       'what success you will review, what related work remains useful, '
                                       'and how the recurring proposal follows demonstrated value rather '
                                       'than distracting from unfinished initial commitments.',
                             'example': 'Handoff plan: spend roughly seventy percent of the conversation '
                                        'celebrating the completed work and thirty percent introducing the '
                                        'next opportunities. Keep the current result central before '
                                        "discussing a retainer. Saraev's split turns delivery into a "
                                        'natural expansion conversation without allowing the sales pitch '
                                        'to replace recognition of what was actually finished. [Nick '
                                        'Saraev — RmYTguzXrVM @ 00:19:01]'},
                            {'name': 'prepaid_build_time_boundary',
                             'type': 'textarea',
                             'prompt': 'Specify whether the recurring offer sells prepaid build time, '
                                       'maintenance, or both, and state the included quantity clearly. '
                                       'Explain the scheduling benefit and client tradeoff without '
                                       'describing a limited monthly allocation as unlimited availability '
                                       'or suggesting that every future request automatically fits inside '
                                       'it.',
                             'example': 'Prepaid build-time reference: twenty monthly hours at $100 per '
                                        'hour total $2,000, compared with $2,400 at the illustrated $120 '
                                        'variable rate. The client saves $400 while the agency gains '
                                        'scheduling stability. The commitment is a defined block of hours, '
                                        'not an unrestricted promise to complete every requested build '
                                        'that month. [Nick Saraev — RmYTguzXrVM @ 00:23:46]'},
                            {'name': 'maintenance_labor_allowance',
                             'type': 'textarea',
                             'prompt': 'Estimate or limit the developer effort required for monthly '
                                       'maintenance, then explain the pricing buffer you will apply. Show '
                                       'how additional client demands could affect that allowance, and '
                                       'distinguish a cost estimate from a promise that maintenance work '
                                       'will never exceed the original expectation.',
                             'example': 'Maintenance pricing approach: first estimate or limit developer '
                                        'hours, then apply at least two to three times the estimated '
                                        'developer cost when setting the fee. Ottley warns that client '
                                        'demands can double or triple. The buffer belongs beside an '
                                        'explicit labor allowance, not beside an unspecified promise of '
                                        'endless maintenance work. [Liam Ottley — kgE01J875dY @ 00:18:22]'},
                            {'name': 'approval_and_extra_work',
                             'type': 'textarea',
                             'prompt': 'Name the person responsible for sign-off and describe what happens '
                                       'when a request exceeds the agreed phase. Give the client a clear '
                                       'distinction between deferring an addition and purchasing it now, '
                                       'including the effect of a priced change on the delivery schedule '
                                       'and existing commitments.',
                             'example': 'Change rule: route extra requests to the phase-two backlog unless '
                                        'the client chooses a priced change with a schedule adjustment. '
                                        'Keep the sign-off lead explicit so approval does not drift among '
                                        'participants. This separates useful future ideas from current '
                                        'commitments without treating every new request as included in the '
                                        'original fee. [ArriSse Corp — XKoGenFWVHs @ 00:04:40]'},
                            {'name': 'relationship_fit_and_exit',
                             'type': 'textarea',
                             'prompt': 'Assess whether the client and continuing work justify a longer '
                                       'relationship, then state an exit structure that preserves '
                                       'flexibility. Explain how a small maintenance commitment could '
                                       "become burdensome as the agency's main product grows, even when "
                                       'the monthly payment initially appears attractive and predictable.',
                             'example': 'Relationship boundary: prefer a month-to-month maintenance '
                                        'arrangement over a small six-month commitment that may become '
                                        'dead weight. Reconsider whether the continuing work still fits as '
                                        "the main agency product grows. Ottley's warning makes flexibility "
                                        'part of the commercial design, rather than assuming every '
                                        'locked-in recurring payment is automatically desirable. [Liam '
                                        'Ottley — kgE01J875dY @ 00:24:25]'}],
                 'completion_gate': 'Proceed only when the paid audit has a bounded deliverable, confirmed '
                                    'interview access, a scheduled presentation, an observed workflow, and '
                                    'a measurable baseline. Recommendations must survive review before '
                                    'presentation. Any retainer must define continuing work, labor '
                                    'allowances, approval authority, extra-work treatment, and an exit '
                                    'structure rather than relying on recurring billing alone.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Build a Verified Sales Process and Maintain Useful CRM Records',
                 'purpose': 'Connect a narrow business offer to relevant prospects, useful conversations, '
                            'and an accurately counted sales process. Verify outreach claims, separate '
                            'observed results from projections, and maintain contact information without '
                            'repeating unnecessary enrichment or creating conflicting employment records.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Start with one workflow and one business measure, then package a clear '
                                  'offer and a reusable demonstration around that shared customer problem.',
                                  'Check prospect relevance and verify any claimed business gap directly '
                                  'before using it in outreach, an audit presentation, or a proposal.',
                                  'Keep positive replies, booked meetings, attended calls, and completed '
                                  'sales in separate categories; label assumptions and projected outcomes '
                                  'explicitly.',
                                  'Choose a LinkedIn content approach and a human reply process that make '
                                  'the next step clear without confusing engagement with purchase intent.',
                                  'Review enrichment recency, available budget, proposed CRM changes, '
                                  'employment transitions, and duplicate records before treating the '
                                  'contact database as ready for further outreach.'],
                 'fields': [{'name': 'single_workflow_sales_focus',
                             'type': 'textarea',
                             'prompt': 'Choose one measurable business problem for the sales offer, '
                                       'identify the workflow that affects it, and set a review point. '
                                       "Describe the result in the buyer's language rather than starting "
                                       'with a tool list or assuming that automation itself establishes a '
                                       'reason to purchase.',
                             'example': 'Offer focus: begin with one workflow, one metric, and one '
                                        'thirty-day review. Diagnose a business issue such as missed calls '
                                        "or response delays before selecting automation. Reimer's approach "
                                        'keeps the sales conversation anchored to a measurable problem '
                                        'rather than a collection of tools whose usefulness the buyer must '
                                        'infer. [Michael Reimer | HighLevel & AI Systems — IWNNb6VOVz8 @ '
                                        '00:04:33]'},
                            {'name': 'reusable_niche_demonstration',
                             'type': 'textarea',
                             'prompt': 'Describe the shared workflow problem your demonstration will show '
                                       'and the company-specific detail reserved for the outreach message. '
                                       'Explain how you will reuse the demonstration without making the '
                                       'prospecting message generic or spending time recording the same '
                                       'underlying solution separately for every prospective buyer.',
                             'example': 'Demonstration plan: reuse one five-minute niche demonstration '
                                        'when prospects share the same workflow problem. Put '
                                        'company-specific research in the email or LinkedIn message '
                                        "instead of recording the whole demonstration again. Lily's method "
                                        'separates repeatable proof of the workflow from the relevance '
                                        'needed to open a conversation with each individual business. '
                                        '[Lily Latzo | AI Automation — NjvNF17_97w @ 00:07:55]'},
                            {'name': 'prospect_relevance_check',
                             'type': 'textarea',
                             'prompt': 'Define the prospect segment and inspect the actual people returned '
                                       'by your search criteria. Record what makes a contact relevant to '
                                       'the offer and what would disqualify them, especially where a broad '
                                       'job title could describe unrelated industries or a different kind '
                                       'of buying role.',
                             'example': 'Qualification check: inspect the returned profiles before '
                                        'treating a buyers-agent list as suitable for a property offer. '
                                        'Greening-James describes reaching a sports-car agent because '
                                        'qualification was too loose. A matching phrase in a title is not '
                                        "enough; confirm that the person's actual business activity fits "
                                        'the problem being offered. [Ben Greening-James — Lw2iBa2oM44 @ '
                                        '00:06:34]'},
                            {'name': 'verified_audit_claim',
                             'type': 'textarea',
                             'prompt': 'Write the specific business gap you intend to mention and identify '
                                       'the actual page or profile you must inspect before using it. '
                                       'Explain how you will correct the outreach if generated analysis '
                                       'conflicts with visible evidence, rather than presenting an '
                                       'unverified claim as a discovered problem.',
                             'example': 'Verification rule: open the business profile and inspect the '
                                        'review responses before claiming that the business leaves reviews '
                                        'unanswered. Gaddis found real responses where Claude had reported '
                                        'none. If the visible profile contradicts the generated audit, '
                                        'remove or correct the claim before using it to start a sales '
                                        'conversation. [Tom Gaddis | Smart AI Operators — Z3ZaxxexqYE @ '
                                        '00:16:04]'},
                            {'name': 'positive_reply_handoff',
                             'type': 'textarea',
                             'prompt': 'Specify who handles an interested response and what their next '
                                       'conversation should accomplish. For a local-service prospect, '
                                       'describe how the reply becomes a phone conversation and a possible '
                                       'walkthrough rather than another generic promotional message that '
                                       'fails to advance the existing exchange with the buyer.',
                             'example': 'Reply procedure: call a positive local-service respondent, refer '
                                        'to the email exchange, and ask when a walkthrough visit would '
                                        'work. Do not replace that conversation with a polished email '
                                        'flyer. Cushing treats the interested reply as an opening for '
                                        'direct discussion, with the next step grounded in the exchange '
                                        'already underway. [The Workbench — NT0JXm1lCyE @ 00:13:36]'},
                            {'name': 'sales_stage_evidence',
                             'type': 'textarea',
                             'prompt': 'Create separate reporting categories for interested replies, '
                                       'booked meetings, attended calls, and completed deals. State which '
                                       'categories contain observed counts and which contain assumptions, '
                                       'and explain how you will prevent a projected close-rate '
                                       'calculation from appearing in the same column as verified sales '
                                       'results.',
                             'example': "Reporting rule: record Shepherd's roughly twenty booked meetings "
                                        'as bookings, not completed sales. Keep attended calls and closed '
                                        'deals separate until counted. The later discussion of about three '
                                        'deals uses assumed show and close rates, so that number belongs '
                                        'in a projection rather than a statement of confirmed campaign '
                                        'receipts. [Aaron Shepherd | GrowthFlare — RQg5jgraVg8 @ '
                                        '00:19:17]'},
                            {'name': 'linkedin_content_schedule',
                             'type': 'textarea',
                             'prompt': 'Set a starting LinkedIn publishing schedule that connects audience '
                                       "familiarity with the service's business relevance. Assign each "
                                       'planned post a funnel role, identify where industry-specific '
                                       'thinking belongs, and keep the schedule framed as a starting '
                                       'approach rather than a guaranteed source of clients or sales.',
                             'example': 'Starting schedule: publish five weekly posts with one '
                                        'top-of-funnel post, three middle-of-funnel posts, and one '
                                        'bottom-of-funnel post. Place industry-specific thought leadership '
                                        'in the middle group. Clark describes this as a starting '
                                        'distribution, so the calendar organizes the content effort '
                                        'without promising that a particular posting count will produce a '
                                        'sale. [Tommy Clark — MXBaHCO4WI8 @ 00:10:06]'},
                            {'name': 'enrichment_recency_review',
                             'type': 'textarea',
                             'prompt': 'Record the last enrichment date before authorizing another '
                                       'research run and explain what makes a repeat request necessary. '
                                       'Identify how recently refreshed information should affect the '
                                       'decision, keeping the desire for complete records separate from an '
                                       'automatic assumption that every new request warrants additional '
                                       'enrichment.',
                             'example': 'Enrichment check: inspect the previous enrichment date before '
                                        'requesting another run. When it occurred less than thirty days '
                                        'earlier, ask whether another pass is necessary rather than '
                                        'repeating research automatically. RevPartners uses this prompt to '
                                        'make representatives consider recency before spending effort on '
                                        'information that may already be sufficiently current. '
                                        '[RevPartners - RevOps + GTM Engineering on HubSpot — jV1Kp0j9lp0 '
                                        '@ 00:44:08]'},
                            {'name': 'employment_change_reconciliation',
                             'type': 'textarea',
                             'prompt': "Describe how you will reconcile a contact's former employer with a "
                                       'newly identified employer. Include treatment of the old contact, '
                                       'checks for an existing new contact or lead, and confirmation of '
                                       'the new account so that an employment update does not create '
                                       'conflicting records or unnecessary duplicates.',
                             'example': 'Employment-change procedure: mark the old contact as having left '
                                        'the company, then check both contacts and leads for an existing '
                                        'record at the new employer. Also check whether the new account '
                                        "exists. Saruggia's sequence preserves the old relationship "
                                        'context while preventing the job change from automatically '
                                        'producing a duplicate record. [Michael Saruggia - GTM Engineering '
                                        '— DHX8uoA53OI @ 00:06:32]'},
                            {'name': 'result_verification_and_escalation',
                             'type': 'textarea',
                             'prompt': 'Define the observable result that counts as done for an automated '
                                       'sales or client-success task. State how the result will be '
                                       'inspected, how many repair attempts are allowed, and what evidence '
                                       'accompanies escalation when a success message does not match the '
                                       'actual state of the work.',
                             'example': 'Acceptance rule: inspect the actual result against the definition '
                                        'of done rather than trusting a success message. Allow up to three '
                                        'repair attempts, then escalate with proof if the result still '
                                        "fails. Aletto's process keeps completion tied to observable work "
                                        'and makes the unresolved problem visible instead of repeatedly '
                                        'claiming success. [Aletto — IfS3QohXxG8 @ 00:21:55]'}],
                 'completion_gate': 'Proceed only when the offer addresses one measurable workflow '
                                    'problem, the demonstration matches the prospect segment, and every '
                                    'claimed audit gap has been checked directly. Assign human ownership '
                                    'of interested replies, separate observed sales stages from '
                                    'projections, and review enrichment recency and employment records. '
                                    'Automated task completion must be supported by an inspected result, '
                                    'not a success message.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Choose the Delivery Stack and Prove the Voice Workflow',
                 'purpose': 'Select automation and voice platforms around the actual client workflow, '
                            'operating responsibility, and measured consumption. Establish release '
                            'evidence for field mapping, failure detection, customer conversations, and '
                            'human transfers before a polished demonstration becomes a production '
                            'commitment.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Describe one real client workflow and its required integrations before '
                                  'comparing platforms. Keep the selection tied to team capability and '
                                  'ongoing operating responsibility.',
                                  'Separate advertised subscriptions from tasks, credits, executions, '
                                  'model charges, and voice minutes. Record the assumptions behind every '
                                  'comparison rather than treating example prices as universal.',
                                  'Build a repeatable test covering ordinary requests, missing '
                                  'information, emergencies, manipulation attempts, and changed '
                                  'destination fields. Inspect delivered records and messages rather than '
                                  'trusting execution status.',
                                  "Write the voice agent's opening, conversation boundaries, required "
                                  'information, and human handoff. Separate actions needed during the '
                                  'conversation from actions that can happen afterward.',
                                  'Assign owners to connection checks, failure alerts, hosting '
                                  'maintenance, and voice quality review. Leave the release blocked '
                                  'wherever the necessary behavior has not been demonstrated.'],
                 'fields': [{'name': 'platform_fit_and_trial',
                             'type': 'textarea',
                             'prompt': "Describe the client's real workflow, required integrations, "
                                       'branching needs, and available operator skills. Choose a '
                                       'provisional platform, explain the tradeoff, and specify what a '
                                       'week of trial usage must demonstrate before you commit to its '
                                       'ongoing delivery costs.',
                             'example': 'Proposed trial: build the same lead responder on each available '
                                        'free tier or trial, then run it for a week and inspect usage. '
                                        'Compare simple setup, visible branching, and technical control '
                                        "against the team's skills. Choose from observed workflow behavior "
                                        'rather than the cheapest headline subscription. [AI Business '
                                        'Tools & Automation — PKHb0KLNOIg @ 00:06:57]'},
                            {'name': 'monthly_consumption_model',
                             'type': 'textarea',
                             'prompt': 'Calculate monthly consumption from expected workflow runs and the '
                                       'actions inside each run. Distinguish tasks, credits, and '
                                       'executions; identify the AI tier and separate model charges. State '
                                       'billing assumptions and explain how the selected plan retains '
                                       'operating headroom.',
                             'example': 'Comparison baseline: ProfitPilot prices 500 monthly leads at $49 '
                                        'for Zapier, $9 for Make, and €20 for n8n Cloud under annual '
                                        'billing assumptions. Record 2,000 tasks, about 2,500 credits, and '
                                        '500 executions separately. The Zapier calculation assumes '
                                        'Standard AI, and separate model costs remain outside this '
                                        'comparison. [ProfitPilot — d8w8FHZJpdY @ 00:03:09]'},
                            {'name': 'dynamic_mapping_and_workflow_labels',
                             'type': 'textarea',
                             'prompt': 'List every customer field that must be mapped dynamically and '
                                       'identify where each value originates. Describe how you will '
                                       'distinguish production, test, and draft workflows, then specify '
                                       'the output inspection that proves sample identities are not being '
                                       'reused.',
                             'example': 'Proposed mapping review: first name, last name, company, and '
                                        'email come from the arriving lead, never from typed demonstration '
                                        'values. Inspect successive outputs to confirm each identity '
                                        'changes with its input. Marc warns that entering Teddy Joy '
                                        'directly would repeat that name on every automation run. '
                                        '[Automate with Marc | AI Automation — syCqaV7N73s @ 00:08:38]'},
                            {'name': 'responder_stress_test',
                             'type': 'textarea',
                             'prompt': 'Define normal, emergency, blank message, and discount manipulation '
                                       'cases for the responder. Include a destination column change and '
                                       'specify the actual emails and stored fields you will inspect. '
                                       'Explain which unexpected outputs or missing alerts prevent client '
                                       'release.',
                             'example': 'Proposed release test: inspect delivered emails and spreadsheet '
                                        "summaries for every case, not just successful executions. Owner's "
                                        "Bot Lab found that Make repeated a customer's discount wording, "
                                        'and a changed column produced a blank summary without an emailed '
                                        'alert. Those outcomes require repair before this responder is '
                                        "accepted. [Owner's Bot Lab — EtiRX0GduSI @ 00:04:25]"},
                            {'name': 'duplicate_and_failure_operations',
                             'type': 'textarea',
                             'prompt': 'Explain how repeated events will avoid duplicate customer messages '
                                       'and how failures will reach an operator independently of the main '
                                       'workflow. Assign connection checks and document hosting '
                                       'responsibilities, including updates, backups, retained workflow '
                                       'data, and the encryption key.',
                             'example': 'Proposed operating plan: make the responder duplicate safe and '
                                        'maintain a separate workflow whose only responsibility is failure '
                                        'notification. Assign an operator to inspect connections instead '
                                        'of assuming a quiet dashboard means healthy service. Jonas '
                                        'reports hourly checks because connections can disconnect quietly '
                                        'even when workflows remain present. [Jonas | AI Tools & '
                                        'Automation — 4imOFZeP7nk @ 00:07:34]'},
                            {'name': 'voice_scope_and_static_opening',
                             'type': 'textarea',
                             'prompt': "Write the voice agent's narrow business purpose, static AI "
                                       'introduction, and permitted conversation path. Identify the '
                                       'business knowledge it needs and the situations it must hand to '
                                       'people. Specify how call review will verify that the introduction '
                                       'was actually spoken.',
                             'example': 'Proposed receptionist opening: identify the assistant as AI '
                                        "before collecting the caller's booking request. Keep the scope "
                                        'focused on the agreed intake rather than open ended sales work. '
                                        'Add an opening check to quality review; Jowett recommends a '
                                        'static introduction and alerts when that introduction is missing '
                                        'from calls. [Brendan Jowett — Ky2Z6kGp1Vk @ 00:02:03]'},
                            {'name': 'voice_information_capture',
                             'type': 'textarea',
                             'prompt': 'Identify the information the voice workflow must capture and where '
                                       'each item will be stored. Separate structured booking variables '
                                       'from free text descriptions. Explain how the chosen identifier and '
                                       'output checks reduce errors that would make the booking unusable.',
                             'example': "Proposed golf booking record: use the caller's phone number as "
                                        'the booking identifier instead of requiring an email address '
                                        'letter by letter. Inspect the captured identifier before treating '
                                        'the booking as usable. Venture Harbour highlights that one '
                                        'incorrect email character can defeat an otherwise successful '
                                        'booking conversation. [Venture Harbour — ZVSDm5siKr4 @ 00:01:32]'},
                            {'name': 'human_transfer_and_failure_path',
                             'type': 'textarea',
                             'prompt': 'Describe the exact caller requests and emergency conditions that '
                                       'require a human transfer. Define the intended destination, what a '
                                       'successful connection looks like, and what happens when connection '
                                       'fails. Specify the call evidence needed before approving the '
                                       'handoff.',
                             'example': 'Proposed acceptance case: ask for a person during an emergency '
                                        "and verify the transfer outcome, not merely the agent's promise "
                                        "to connect. Review the unsuccessful path separately. Daniel's "
                                        'emergency transfer failed and was marked unsuccessful despite a '
                                        'fallback response, so spoken reassurance alone cannot satisfy '
                                        'this release gate. [Daniel | Tech & Data — PgrkNMNc_Cw @ '
                                        '00:07:31]'},
                            {'name': 'live_and_post_call_actions',
                             'type': 'textarea',
                             'prompt': 'Separate actions essential to continuing the conversation from CRM '
                                       'updates, confirmation emails, and team notifications that can '
                                       'wait. Describe the post call sequence and the evidence you will '
                                       'inspect to ensure delayed work completes without disrupting the '
                                       'caller.',
                             'example': 'Proposed sequence: keep only conversation dependent actions '
                                        'inside the live call. Move CRM updates, confirmation emails, and '
                                        'team notifications afterward when the caller does not need them '
                                        'to continue. Jowett reports silence and broken function calls '
                                        'from live execution, so review both conversational continuity and '
                                        'the resulting downstream records. [Brendan Jowett — Ky2Z6kGp1Vk @ '
                                        '00:07:54]'},
                            {'name': 'voice_platform_operating_decision',
                             'type': 'textarea',
                             'prompt': 'Compare voice platforms using expected minutes, required phone '
                                       'system features, observed latency, development effort, and support '
                                       'experience. Record which costs belong to the chosen scenario and '
                                       'explain what evidence would justify migration rather than another '
                                       'round of troubleshooting.',
                             'example': 'Proposed decision note: retain the current platform unless a '
                                        'required capability justifies the development and learning cost '
                                        'of moving. Compare actual conversation behavior and '
                                        'troubleshooting effort alongside monthly usage. Pijuan warns that '
                                        'switching for a new feature requires rebuilding platform '
                                        'knowledge and introduces fresh troubleshooting work rather than '
                                        'eliminating it. [Alejo Pijuan — 6Fal62hzEs8 @ 00:14:56]'}],
                 'completion_gate': 'Complete only when one real workflow has a justified platform choice, '
                                    'a consumption model with explicit assumptions, dynamic field mapping, '
                                    'inspected stress test outputs, and assigned operating ownership. The '
                                    'voice workflow must have a checked introduction, usable captured '
                                    'information, a demonstrated human transfer and failure path, and '
                                    'verified post call actions. Keep unresolved failures visible; a '
                                    'smooth demonstration does not replace these checks.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Ground the Support Agent and Validate Its Service Economics',
                 'purpose': 'Design a support service around retrievable company knowledge, appropriate '
                            'access, observable answer quality, and reliable human escalation. Connect '
                            "retrieval decisions to customer outcomes while separating the platform's "
                            'billing units from actual successful resolutions.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Choose a repetitive support problem and describe its business outcome '
                                  'before selecting retrieval architecture. Distinguish finding the answer '
                                  'from generating the final response.',
                                  'Collect representative questions, relevant material, unrelated matches, '
                                  'and access boundaries. Establish a test set that can be rerun after '
                                  'prompt, chunking, or embedding changes.',
                                  'Record the retrieval configuration and inspect whether necessary '
                                  'context reaches the answering model. Treat visible documents and '
                                  'technically successful searches as insufficient proof.',
                                  'Start customer support with a limited set of fixed answers and customer '
                                  'wording. Test the request for a person and the two unsuccessful '
                                  'attempts escalation path.',
                                  'Calculate recurring charges, trial exposure, and account configuration '
                                  'separately. Schedule a weekly review that connects response behavior, '
                                  'incorrect answers, human involvement, and ongoing cost.'],
                 'fields': [{'name': 'support_outcome_and_knowledge_need',
                             'type': 'textarea',
                             'prompt': 'Name the repetitive support problem, the company knowledge '
                                       'required to solve it, and the business outcome you will measure. '
                                       'Distinguish retrieval failure from answer generation failure, and '
                                       'explain why your proposed architecture fits the questions '
                                       'customers actually ask.',
                             'example': 'Proposed support objective: return the relevant company procedure '
                                        'before asking the model to explain it. If an answer is wrong, '
                                        'inspect the retrieved material first rather than rewriting the '
                                        'prompt immediately. IBM describes a failure where the answer '
                                        'existed in the data but never reached the model through '
                                        'retrieval. [IBM Technology — UabBYexBD4k @ 00:05:55]'},
                            {'name': 'retrieval_architecture_and_chunking',
                             'type': 'textarea',
                             'prompt': 'Describe whether the questions require bounded whole document '
                                       'reasoning, similarity retrieval, or connected relationships. '
                                       'Record the initial chunk size and overlap where applicable, '
                                       'explain the context you must preserve, and identify the tests that '
                                       'could change those settings.',
                             'example': 'Proposed GraphRAG starting configuration: use 1,200 token chunks '
                                        'with 100 token overlaps only as an initial setting to evaluate. '
                                        'Lucek uses those defaults while indexing a fine tuning guide, '
                                        'producing about 53 chunks. Keep the configuration provisional '
                                        'until important support questions demonstrate that the required '
                                        'context survives the split. [Adam Lucek — 6vG_amAshTk @ '
                                        '00:12:17]'},
                            {'name': 'retrieval_only_relevance_test',
                             'type': 'textarea',
                             'prompt': 'List known relevant cases and unrelated cases for the same '
                                       'questions. Test retrieval without relying on a polished generated '
                                       'answer, record the match scores, and explain how you will choose a '
                                       'similarity cutoff that separates useful evidence from misleading '
                                       'neighbors.',
                             'example': 'Proposed relevance check: search for known support cases, record '
                                        'the scores of genuine matches and unrelated nearest results, then '
                                        'choose the dividing line from those observations. Do not approve '
                                        'a threshold because every search returns something. Case '
                                        "Resolver's team tested retrieval independently before tuning its "
                                        'similarity cutoff against real examples. [Mirketa Inc — '
                                        '8N3k2qP_0SY @ 00:30:10]'},
                            {'name': 'knowledge_access_boundaries',
                             'type': 'textarea',
                             'prompt': 'Identify who may access each knowledge source and how those '
                                       'permissions will remain effective during retrieval. Describe '
                                       'metadata filtering and any finer checks needed afterward. Specify '
                                       'permitted and restricted test cases that prove the assistant does '
                                       'not broaden access.',
                             'example': 'Proposed access review: mirror the permissions already applied by '
                                        'the source system instead of making every indexed document '
                                        'available to every support user. Record which metadata '
                                        'restrictions apply before retrieval and which finer checks remain '
                                        'afterward. Scoffield describes this layered approach as one way '
                                        'to preserve permissions in production retrieval. [Unstructured — '
                                        'ruilmyfVgrI @ 00:16:24]'},
                            {'name': 'evaluation_and_embedding_changes',
                             'type': 'textarea',
                             'prompt': 'Define the questions and expected answers used to compare prompt '
                                       'and chunking changes before deployment. Include a document '
                                       'reimport step after embedding model changes, and identify the '
                                       'business measures that must improve alongside technical retrieval '
                                       'and answer scores.',
                             'example': 'Proposed evaluation pack: assemble 100 to a few hundred important '
                                        'question and answer pairs before changing prompts or chunking. '
                                        'Run the same questions offline after each revision and compare '
                                        'the answers before release. Scoffield recommends this golden set '
                                        'approach so changes are judged against important questions rather '
                                        'than a convincing demonstration. [Unstructured — ruilmyfVgrI @ '
                                        '00:17:28]'},
                            {'name': 'fixed_answer_support_pilot',
                             'type': 'textarea',
                             'prompt': 'Review existing customer messages and identify repetitive '
                                       'questions that can safely receive fixed answers. Select the first '
                                       'five, write the approved response for each, and describe how you '
                                       "will test customer phrasing before expanding the assistant's "
                                       'supported coverage.',
                             'example': 'Proposed pilot: begin with five fixed answer questions instead of '
                                        'loading a broad promise into the assistant. Test each answer '
                                        'using the wording customers actually use and keep expansion '
                                        'blocked until those responses work correctly. AIWealthPath '
                                        'recommends this small starting set before increasing the number '
                                        'of supported customer questions. [AIWealthPath — JKmSoDIpfdI @ '
                                        '00:02:09]'},
                            {'name': 'support_escalation_with_context',
                             'type': 'textarea',
                             'prompt': 'Write the support escalation rule for a direct request for a '
                                       'person and for repeated unsuccessful answers. Name the receiving '
                                       'human role, specify the conversation context transferred, and '
                                       'describe the test proving customers will not need to repeat '
                                       'themselves.',
                             'example': 'Proposed escalation rule: make a person available when requested '
                                        'and transfer immediately after two unsuccessful AI attempts. '
                                        'Attach the complete conversation to the handoff so the receiving '
                                        'operator can continue from the existing context. AIWealthPath '
                                        'explicitly requires this two attempt boundary rather than '
                                        'allowing the assistant to keep trying indefinitely. [AIWealthPath '
                                        '— JKmSoDIpfdI @ 00:03:16]'},
                            {'name': 'billing_units_and_recurring_allowances',
                             'type': 'textarea',
                             'prompt': 'Compare the candidate support plans using their actual billing '
                                       'units, including seats, conversations, outcomes, tickets, or '
                                       'credits. Separate recurring allowances from introductory grants '
                                       'and identify whether an unsuccessful answer can still create a '
                                       'charge under the selected plan.',
                             'example': "Proposed Tidio budget note: do not treat Lyro's fifty free AI "
                                        'conversations as a monthly refill. Record that allocation as a '
                                        'one time batch and budget continued AI use separately. AI Tool '
                                        'Lab also warns that paid conversations can be billed whether the '
                                        "bot solves the customer's problem or not. [AI Tool Lab — "
                                        '9wewuc4s038 @ 00:06:13]'},
                            {'name': 'client_activation_and_credit_controls',
                             'type': 'textarea',
                             'prompt': 'Describe the reusable niche agent, the client specific channels '
                                       'that must be connected, and the checks required before activation. '
                                       'Set out trial credit exposure, agency pool funding, and any '
                                       'reselling plan settings needed for usage and renewals to behave '
                                       'correctly.',
                             'example': 'Proposed onboarding sequence: save the perfected niche agent as a '
                                        'default snapshot, create the client account with that agent '
                                        "paused, and connect the client's channels before activation. Do "
                                        'not confuse a copied configuration with a working client '
                                        'installation. Sohaib uses paused snapshots so reusable delivery '
                                        "still requires the client's actual connections. [Sohaib — "
                                        'lvzJJWDX0ec @ 00:06:05]'},
                            {'name': 'weekly_support_quality_review',
                             'type': 'textarea',
                             'prompt': 'Schedule a weekly review and name its owner. Specify how first '
                                       'response speed, answers completed without people, incorrect '
                                       'answers, and escalations will be inspected. Describe how review '
                                       'findings become knowledge corrections or workflow changes rather '
                                       'than a decorative performance score.',
                             'example': 'Proposed review: reserve twenty minutes each week to inspect '
                                        'first response speed, questions answered without people, and '
                                        'incorrect answers. Keep the underlying conversations available '
                                        'for deciding what needs correction. AIWealthPath recommends this '
                                        'recurring review so the service is assessed through observed '
                                        'support behavior instead of being left untouched after initial '
                                        'installation. [AIWealthPath — JKmSoDIpfdI @ 00:03:33]'}],
                 'completion_gate': 'Complete only when the selected support problem has an observable '
                                    'business outcome, retrieval tests distinguish relevant from unrelated '
                                    'evidence, and access checks preserve source permissions. Require a '
                                    'reusable evaluation set, a documented embedding change process, '
                                    'tested fixed answers, and a demonstrated human handoff with context. '
                                    'Billing assumptions, trial exposure, activation steps, and weekly '
                                    'review ownership must be explicit before recurring service begins.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Deliver, Bound, and Accept the Client System',
                 'purpose': 'Turn completed automation work into an installed, supportable client system '
                            'with named owners and observable acceptance requirements. Define migration '
                            'limits, additional work, privacy handling, consumption visibility, and '
                            'deletion evidence without confusing technical completion with client '
                            'acceptance.',
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Write the installed outcome, responsible owners, onboarding due dates, '
                                  'and hosting decision. Treat documentation and production connections as '
                                  'part of delivery rather than optional extras.',
                                  'Inventory workflows before migration and separate copied workflow '
                                  'definitions from credentials, users, and execution history. Inspect '
                                  'failed executions before retrying uncertain operations.',
                                  'Record every additional request, classify it against the agreed scope, '
                                  'and route it into a reviewed estimate or a later version. Make payment '
                                  'and scheduling consequences visible.',
                                  'Describe privacy handling across incoming data, prompts, responses, '
                                  'logs, storage, and deletion. Check provider promises individually '
                                  'rather than treating training settings as complete protection.',
                                  'Freeze externally observable requirements, test the shipped product, '
                                  'and review remaining acceptance gaps with the owner. Include '
                                  'consumption reporting, support boundaries, and documented decisions in '
                                  'the handoff.'],
                 'fields': [{'name': 'installed_outcome_and_onboarding_owners',
                             'type': 'textarea',
                             'prompt': 'Define the installed client outcome and list the onboarding stages '
                                       'required to reach it. Assign an owner and due date to each stage, '
                                       'identify the client decisions still needed, and explain how '
                                       'stalled dependencies will remain visible until resolved.',
                             'example': 'Proposed onboarding record: give account connection, strategy '
                                        'confirmation, installation, and handoff their own owners and due '
                                        'dates. Keep missing client decisions visible instead of treating '
                                        'advance payment as delivery progress. Bartnick warns that stalled '
                                        'onboarding can leave paid work unfinished and lead to disputes or '
                                        'refunds rather than completed client systems. [Scott Bartnick — '
                                        'd9zqCrUn7mY @ 00:08:30]'},
                            {'name': 'hosting_and_support_boundary',
                             'type': 'textarea',
                             'prompt': "Choose cloud or self hosted delivery using the client's operating "
                                       'preferences and maintenance responsibility. Describe what the '
                                       'handoff includes, distinguish initial support from ongoing '
                                       'maintenance, and state who owns production connections, '
                                       'documentation, updates, and troubleshooting after the initial '
                                       'window.',
                             'example': 'Proposed support boundary: include thirty days of support for the '
                                        'delivered work, then describe ongoing maintenance separately '
                                        'instead of implying permanent assistance in the setup fee. Record '
                                        'the installed workflows, production connections, and '
                                        'documentation in the handoff. Automate AI Consulting offers that '
                                        'initial support window whether or not the client has a retainer. '
                                        '[Automate AI Consulting — 91lw5ubtLMc @ 00:04:45]'},
                            {'name': 'migration_inventory_and_reset_checks',
                             'type': 'textarea',
                             'prompt': 'Create the workflow migration inventory and define the statuses '
                                       'used to prevent repeated imports. Identify credentials that need '
                                       'manual resetting and account for users and execution history that '
                                       'will not transfer. Specify the production checks required after '
                                       'each migrated workflow.',
                             'example': 'Proposed migration gate: track workflows as to process or '
                                        'processed, but keep installation incomplete until credentials are '
                                        'manually reset and production behavior is checked. Herk explains '
                                        'that the migration method does not move credentials, users, or '
                                        'executions. A copied workflow therefore does not prove the '
                                        'destination instance is ready for client use. [Nate Herk | AI '
                                        'Automation — t1PTmpas0bg @ 00:08:56]'},
                            {'name': 'intake_failure_and_retry_inspection',
                             'type': 'textarea',
                             'prompt': 'Describe how pending intake rows, model failures, simultaneous '
                                       'requests, and timeouts will be investigated. Specify what must be '
                                       'inspected before retrying an operation and how you will determine '
                                       'whether a draft or other output already exists despite the '
                                       'reported failure.',
                             'example': 'Proposed retry procedure: inspect the failed execution and look '
                                        'for an existing draft before rerunning intake after a timeout. '
                                        'Test simultaneous requests rather than assuming single request '
                                        'behavior will hold. Hastie highlights that a failed or timed out '
                                        'operation may already have created a draft, making an uninspected '
                                        'retry unsafe for delivery. [Kelsey Hastie — cqaukVEOmJ4 @ '
                                        '00:05:43]'},
                            {'name': 'change_order_review_and_payment',
                             'type': 'textarea',
                             'prompt': 'Define how incoming requests are logged, classified, estimated, '
                                       'and approved before additional work begins. Distinguish current '
                                       'scope from later version ideas, identify missing facts that need '
                                       'clarification, and state when payment is collected so additions do '
                                       'not surprise the final invoice.',
                             'example': 'Proposed change process: price additions when requested and '
                                        'collect change order payment upfront rather than accumulating '
                                        'unseen extras for the final invoice. Keep the approved addition '
                                        'visible beside the original scope. Contractor AI describes '
                                        'relationship damage when the final number is thirty percent '
                                        'higher than the client expected after unaddressed changes. [The '
                                        'Contractor AI | AI Systems for Contractors — J5BBjGKyoUE @ '
                                        '00:26:06]'},
                            {'name': 'observable_acceptance_and_retry_limits',
                             'type': 'textarea',
                             'prompt': 'Write acceptance requirements as who performs an action, what they '
                                       'can do, and how an observer proves it in the shipped product. '
                                       'Include exact retry limits and owner decisions, then distinguish '
                                       'passing tests from a complete review of the agreed done '
                                       'conditions.',
                             'example': 'Proposed acceptance check: require the runner name to appear in '
                                        'the promised product state, not merely exist in code or an API '
                                        'response. Inspect the shipped interface as the user would. '
                                        'neomanex failed a runner name requirement on exactly that '
                                        'distinction, showing why internal implementation evidence cannot '
                                        'replace observable acceptance. [neomanex — wOkT9r5iVME @ '
                                        '00:06:42]'},
                            {'name': 'privacy_settings_and_processing_locations',
                             'type': 'textarea',
                             'prompt': 'List the sensitive fields the workflow actually needs and identify '
                                       'where they travel. Check training use, retention eligibility, '
                                       'exceptions, abuse monitoring, storage location, and inference '
                                       'location separately. Record unresolved provider conditions rather '
                                       'than treating one favorable privacy statement as complete '
                                       'approval.',
                             'example': 'Proposed privacy review: record training behavior separately from '
                                        'retention eligibility, exceptions, abuse monitoring, storage '
                                        'location, and inference location. Keep only sensitive fields '
                                        'necessary for the intended workflow under consideration. Protecto '
                                        'treats these as distinct checks, so a statement about data not '
                                        'being used for training does not close the entire processing '
                                        'review. [Protecto — e8kcLoVVX_A @ 00:01:54]'},
                            {'name': 'redaction_and_observability_records',
                             'type': 'textarea',
                             'prompt': 'Describe how sensitive information will be handled before '
                                       'documents, prompts, and responses move onward or become stored '
                                       'records. Include observability logs in the review and specify '
                                       'tests using actual business data that demonstrate the redaction '
                                       'behavior meets the intended processing boundary.',
                             'example': 'Proposed redaction check: inspect raw prompts and responses as '
                                        'well as incoming documents before they become permanent '
                                        'observability records. Test the handling against the business '
                                        'data the workflow will encounter. Cognitive Capital specifically '
                                        'includes logging in the redaction boundary, so clean customer '
                                        'facing output alone does not complete this review. [Cognitive '
                                        'Capital — j2Bqq0VTv0o @ 00:03:38]'},
                            {'name': 'consumption_and_contract_boundaries',
                             'type': 'textarea',
                             'prompt': 'Specify the consumption reporting and admin visibility required '
                                       'before launch. Identify usage that could exceed expectations, then '
                                       "record the agreement's additional work boundary and aggregate "
                                       'liability cap for review. Explain which missing controls prevent '
                                       'acceptance of the operating arrangement.',
                             'example': 'Proposed launch boundary: require consumption reporting and an '
                                        'admin tool early enough to inspect uploads, viewing, storage, and '
                                        "bandwidth. Taylor reports a customer's first month reached "
                                        '$30,000 after video space was given away without understanding '
                                        'usage. Treat visible consumption as part of delivery rather than '
                                        'discovering exposure only after a bill arrives. [Bryan Taylor — '
                                        'yLxvwa45vR8 @ 00:03:17]'},
                            {'name': 'retention_deletion_and_final_handoff',
                             'type': 'textarea',
                             'prompt': 'Record the agreed retention period, applicable deletion '
                                       'responsibilities, and the evidence needed to verify removal from '
                                       'backups and snapshots. Name the review owner and include '
                                       'unresolved deletion questions in the handoff so a closed support '
                                       'ticket is not mistaken for verified deletion.',
                             'example': 'Proposed deletion record: document backup and snapshot removal, '
                                        'then review the ticket and obtain support verification at the '
                                        'agreed interval. SecureCyberGates gives thirty five days as an '
                                        'example, not a universal retention rule. Set the interval through '
                                        "the project's contract and applicable requirements before "
                                        'treating deletion as complete or closing the handoff item. '
                                        '[SecureCyberGates — TcAbiyEqBFM @ 00:04:39]'}],
                 'completion_gate': 'Complete only when the client system is installed with assigned '
                                    'owners, working production connections, documented support '
                                    'boundaries, and inspected migration or retry risks. Additional work '
                                    'must have an explicit approval and pricing path. Acceptance requires '
                                    'observable shipped behavior, resolved owner decisions, separate '
                                    'privacy checks, visible consumption, and an agreed retention and '
                                    'deletion verification process. Record any remaining gap as unresolved '
                                    'rather than declaring delivery complete because tests passed.'}]}
