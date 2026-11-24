from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "ai-customer-support-tools-automation-agency-business-models",
    "question_prompt": "How do AI customer support agents work, how do leading tools—including Zendesk, Intercom, and Tidio—compare on features, pricing, and AI capabilities, and how can beginners automate small-business support or build an agency selling these services to local businesses?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "AI Customer Support: Tools, Automation & Agency Business Models",
    "subtitle": "Beginner guides to AI customer service agents, platform rankings, Intercom vs Zendesk vs Tidio, small-business budgeting, and building and selling AI support services.",
    "layout_template": "expert_commentary",
    "reading_time_minutes": 15,
    "executive_summary": (
        "The operators converge on a practical product: answer repetitive questions from business-specific knowledge, "
        "connect the workflows that finish the job, and hand difficult conversations to people with context intact. "
        "Travis Wardrop sells missed-call recovery at $300 monthly; Sohaib demonstrates branded messaging agents, "
        "appointment booking, recurring plans, and credit markups. AIWealthPath starts with ten recurring questions "
        "and a weekly twenty-minute review. Platform preferences split by workload: Zendesk for structured operations, "
        "Intercom for conversational support, and Tidio for small stores. AI Tool Lab favors Tidio on small-store "
        "economics, while Daniel Davidson favors SparrowDesk and Gorgias for different operating needs. The sharpest "
        "disagreements concern billing: seats, outcomes, conversations, tickets, and credits do not describe the same "
        "thing, and several speakers identify charges that survive an unsuccessful answer."
    ),
    "key_metrics": [
        {
            "label": "Local automation monthly offer",
            "metric": "Local automation monthly offer",
            "value": "$300–$500 per client per month",
            "confidence": "attributed_practitioner_claim",
            "context": "Travis Wardrop presents this recurring price range for local-business AI solutions fulfilled through resold software.",
            "source": "Travis Wardrop ([CDVbVmBQVyc @ 00:02:04])",
        },
        {
            "label": "DM Champ agency entry plan",
            "metric": "DM Champ agency entry plan",
            "value": "$297 monthly; 1,000 credits; 10 client accounts",
            "confidence": "attributed_practitioner_claim",
            "context": "Sohaib states the agency plan's monthly price and included credits and accounts while explaining branded client delivery.",
            "source": "Sohaib ([lvzJJWDX0ec @ 00:06:50])",
        },
        {
            "label": "Weekly support review",
            "metric": "Weekly support review",
            "value": "20 minutes once a week",
            "confidence": "attributed_practitioner_claim",
            "context": "AIWealthPath recommends reviewing first-response speed, questions answered without people, and incorrect answers.",
            "source": "AIWealthPath ([JKmSoDIpfdI @ 00:03:33])",
        },
        {
            "label": "Zendesk interaction resolution claim",
            "metric": "Zendesk interaction resolution claim",
            "value": "60% or more",
            "confidence": "attributed_practitioner_claim",
            "context": "Zendesk says its AI agents are helping companies resolve this share of customer interactions.",
            "source": "Zendesk ([mnFYeyoS2r8 @ 00:02:45])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The common starting point is repetitive work, not a blank chatbot. Ventra Technologies describes "
                    "a restaurant facing the same late-night WhatsApp questions about opening hours, delivery areas, "
                    "and specials; its service begins with a support audit that identifies recurring conversations, "
                    "then structures company information and configures the agent around that work "
                    "[b5pi4BcdrKk @ 00:03:29]. AIWealthPath makes the intake concrete: open the inbox, WhatsApp, and "
                    "comments, write down the ten questions that recur, and treat a question appearing three times "
                    "weekly as an automation candidate [JKmSoDIpfdI @ 00:00:31]. The first knowledge document contains "
                    "actual delivery times, delivery charges, return windows, refund rules, prices, hours, and contact "
                    "details. Stewart Gauld builds the same foundation inside Zendesk by opening Knowledge, adding "
                    "resources about the business and its products, and preparing the help center before creating "
                    "an agent [nMMWXxBsH2o @ 00:02:18]. Toolstack gives the operational reason: Intercom Fin can "
                    "handle a substantial share of questions when documentation is solid, but messy documentation "
                    "produces confident half answers [aNlthYD5fPY @ 00:01:05]. These speakers put the business's "
                    "answers upstream of the interface. The setup work includes organizing articles, supplying missing "
                    "answers, and making information usable by both customers and the people handling support."
                ),
                (
                    "The agent's job extends beyond retrieving a paragraph when the business connects an operational "
                    "system. Ventra Technologies explains retrieval augmented generation as searching the organized "
                    "knowledge base, extracting the relevant policy, and feeding it to the model before the answer. "
                    "Its next layer uses APIs to retrieve live tracking information, with explicit instructions "
                    "against invented refunds, allergy guesses, or exposed customer information "
                    "[b5pi4BcdrKk @ 00:02:09]. Zendesk demonstrates the action layer through a gift return without "
                    "a receipt: gather details, locate the order, confirm store credit, offer alternatives, process "
                    "the exchange, issue a return label, and update the order system "
                    "[mnFYeyoS2r8 @ 00:01:14]. Its separate explanation describes understanding intent and history, "
                    "finding information, taking action, handing off with context, and learning from outcomes "
                    "[vxbipxTJGgw @ 00:01:10]. AIWealthPath specifies a smaller business's escape route: every "
                    "automated reply offers a person, and two unsuccessful attempts trigger an immediate handover "
                    "with the entire conversation attached [JKmSoDIpfdI @ 00:03:16]. The shared operating pattern "
                    "therefore includes both completed tasks and useful transfers. Customers should not repeat "
                    "their story after escalation, while human staff handle the sensitive conversations that "
                    "Ventra reserves for them. The business supplies policies and workflow connections; the agent "
                    "uses those resources to answer, act, or transfer."
                ),
                (
                    "The agency offer is an operating outcome that the owner recognizes. Travis Wardrop pitches "
                    "missed-call recovery rather than an abstract AI installation: if one recovered call becomes "
                    "a customer worth a few hundred dollars, the owner has a straightforward reason to consider "
                    "a monthly fee [CDVbVmBQVyc @ 00:05:19]. Sohaib uses the messaging equivalent, selling answered "
                    "messages and booked appointments instead of the model behind them. The offer combines a "
                    "setup charge, recurring operation, and a margin on replies; choosing one niche allows the "
                    "agency to reuse an agent across similar clients [lvzJJWDX0ec @ 00:00:50]. Ventra Technologies "
                    "defines the product as recovered human time and operational efficiency, with employees "
                    "redirected toward sales, consultative support, and relationships rather than typing identical "
                    "answers [b5pi4BcdrKk @ 00:04:03]. Simply Contact supplies a different delivery model: "
                    "outsourced human agents combined with voicebots, chatbots, routing, translations, quality "
                    "assurance, and omnichannel support, priced to project scope and support volume "
                    "[DcDfJRzuZNI @ 00:00:19]. The common business objective is not restricted to a standalone "
                    "widget. Wardrop sells a backup for unanswered telephone calls, Sohaib sells a branded "
                    "front desk across messaging channels, Ventra sells integration work, and Simply Contact "
                    "combines automation with a staffed support operation. Each describes reducing repetitive "
                    "handling while keeping useful human involvement."
                ),
            ],
            "table": {
                "caption": "Shared operating foundations and the business work they support",
                "headers": ["Foundation", "Practitioner operating instruction", "Expert Source"],
                "rows": [
                    [
                        "Begin with repeated customer questions rather than an empty agent.",
                        "Audit existing messages and identify repetitive work before configuring the support setup.",
                        "Ventra Technologies ([b5pi4BcdrKk @ 00:03:29])",
                    ],
                    [
                        "Write business answers once with the actual operating details.",
                        "Include delivery times, delivery costs, refund rules, prices, hours, and contact details.",
                        "AIWealthPath ([JKmSoDIpfdI @ 00:01:04])",
                    ],
                    [
                        "Create the knowledge resources before building the customer-facing agent.",
                        "Add product and business articles to Zendesk Knowledge and activate the help center.",
                        "Stewart Gauld ([nMMWXxBsH2o @ 00:02:18])",
                    ],
                    [
                        "Connect operational systems when answering alone does not finish work.",
                        "Zendesk's gift-return example locates an order and processes an exchange with backend updates.",
                        "Zendesk ([mnFYeyoS2r8 @ 00:01:14])",
                    ],
                    [
                        "Make human escalation carry the conversation rather than restart it.",
                        "After two unsuccessful answers, transfer immediately with the whole conversation attached.",
                        "AIWealthPath ([JKmSoDIpfdI @ 00:03:16])",
                    ],
                    [
                        "Sell the owner's desired result instead of the underlying model.",
                        "Sohaib pitches messages answered and calls booked so leads do not wait until morning.",
                        "Sohaib ([lvzJJWDX0ec @ 00:08:20])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Wardrop's voice build starts with Create Agent and Create Custom Agent, then a business name, "
                    "a selected voice, and the opening message. Under agent goals, collect the caller's name, "
                    "email, and inquiry; for the landscaping example, also collect the project address. Wardrop "
                    "says a dentist would not necessarily need that address during the call "
                    "[CDVbVmBQVyc @ 00:06:26]. Buy a backup number, which Wardrop prices at one dollar, and "
                    "forward unanswered calls to it instead of changing the number already displayed on the "
                    "business's website, Google listing, or truck. Create a knowledge base, choose Add Source "
                    "and Web Crawler, paste the website, and extract its information. Add FAQs separately when "
                    "the owner has answers or scripts missing from the site "
                    "[CDVbVmBQVyc @ 00:07:57]. The final step is a real test call before deployment. "
                    "AIWealthPath's written-support build follows a similarly narrow sequence: launch the five "
                    "most common fixed-answer questions, test them in customers' own wording, and only then "
                    "add the next five [JKmSoDIpfdI @ 00:02:09]. Sohaib demonstrates an appointment-oriented "
                    "test by asking about a kitchen remodel with a $25,000 budget and requesting a designer "
                    "call; the agent offers a design consultation instead of inventing a project price "
                    "[lvzJJWDX0ec @ 00:02:57]. These are working demonstrations of collection, retrieval, and "
                    "booking rather than a broad feature pitch."
                ),
                (
                    "Gauld's Zendesk sequence makes the publishing work explicit. After adding knowledge resources, "
                    "activate the help center through its general settings; then open AI Agents and select "
                    "messaging rather than the separate email and web-form route. Create the agent, name it, "
                    "choose its tone and brand, and test it before publication "
                    "[nMMWXxBsH2o @ 00:05:09]. Advanced settings cover the avatar, persona, reply length, language, "
                    "and connected channels. Under Behavior, add the greeting and the option to speak with a "
                    "person when the answer is unknown. Gauld then adds channels such as Facebook Messenger, "
                    "WhatsApp, and Instagram Direct, returns to the agent's brand-and-channels settings, and "
                    "connects them. For the website, edit the messaging channel, copy the widget code, add it "
                    "to the site, and enable automatic embedding in the help center "
                    "[nMMWXxBsH2o @ 00:08:09]. Zendesk distinguishes the initial help-center connection from "
                    "advanced actions, which use drag-and-drop conversation flows and selected backend systems "
                    "[mnFYeyoS2r8 @ 00:02:09]. AIWealthPath adds the operating rhythm after launch: tag messages "
                    "as urgent, refund, order problem, or ready to buy, putting urgent requests and buyers "
                    "at the top of the queue [JKmSoDIpfdI @ 00:02:41]. This gives the owner both automated "
                    "routine responses and a prioritized list of conversations needing attention."
                ),
                (
                    "Sohaib's DM Champ agency build places each client in a separate account under the agency "
                    "dashboard, with its own agents, contacts, and channels funded through a shared credit pool. "
                    "White labeling adds the agency's domain, logo, colors, app name, and branded login experience; "
                    "Sohaib says the platform supports up to three brands "
                    "[lvzJJWDX0ec @ 00:03:31]. Manual credit mode leaves invoicing with the agency. Reselling "
                    "mode uses the agency's Stripe or PayPal checkout, with example plans of 1,000 credits for "
                    "$29 and 5,000 credits for $99. Plans also determine channels, agent counts, and team seats. "
                    "Sohaib illustrates credit resale with 150 credits sold for $25 against a $15 cost, "
                    "leaving $10, and separately describes charging half a credit for a reply that costs "
                    "the agency a quarter credit [lvzJJWDX0ec @ 00:05:28]. Save the working agent as a snapshot, "
                    "make it the default, and new accounts receive it paused until channels are connected. "
                    "Wardrop's alternative is reselling prebuilt software under the agency's branding for "
                    "$300–$500 monthly per client, with no software-company commission split "
                    "[CDVbVmBQVyc @ 00:01:47]. Rocket Research frames the software purchasing decision around "
                    "team size and AI conversation volume, contrasting fixed monthly pricing with seats "
                    "plus usage [swIGkbLXEdM @ 00:02:32]."
                ),
            ],
            "table": {
                "caption": "Quoted commercial mechanics: keep the plan and its meter together",
                "headers": ["Offer or platform", "Exact quoted commercial mechanic", "Expert Source"],
                "rows": [
                    [
                        "Wardrop's branded local-business automation offer uses a recurring client fee.",
                        "The stated selling range is $300–$500 monthly per client for software-fulfilled AI solutions.",
                        "Travis Wardrop ([CDVbVmBQVyc @ 00:02:04])",
                    ],
                    [
                        "DM Champ's entry agency plan includes accounts and shared credits.",
                        "Sohaib quotes $297 monthly with 1,000 credits and ten client accounts included.",
                        "Sohaib ([lvzJJWDX0ec @ 00:06:50])",
                    ],
                    [
                        "DM Champ's larger agency option changes account expansion economics.",
                        "Agency Unlimited is $497 monthly with 2,500 credits; extra entry-plan clients cost $27 monthly.",
                        "Sohaib ([lvzJJWDX0ec @ 00:07:10])",
                    ],
                    [
                        "Intercom Essential seats and Fin outcomes are separate billed components.",
                        "AI Tools for Business quotes $29 yearly-billed seats plus $0.99 per successful Fin outcome.",
                        "AI Tools for Business ([T6Ij8zqR4Bo @ 00:01:13])",
                    ],
                    [
                        "Tidio Starter and ongoing Lyro usage are separate purchased components.",
                        "AI Tools for Business quotes approximately $68 combined: $29 Starter plus $39 Lyro.",
                        "AI Tools for Business ([T6Ij8zqR4Bo @ 00:04:33])",
                    ],
                    [
                        "Corby's quoted flat-rate alternative removes the per-resolution charging structure.",
                        "Rocket Research quotes $99 monthly with unlimited AI conversations, unlimited teammates, and no resolution fees.",
                        "Rocket Research ([swIGkbLXEdM @ 00:00:19])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Build the smallest working service, then make delivery repeatable",
                "body": "These moves come directly from the operators' setup, testing, and client-delivery routines.",
                "items": [
                    "Keep the local business's existing public phone number; forward unanswered calls to the new AI backup number instead. [Travis Wardrop — CDVbVmBQVyc @ 00:07:12]",
                    "Use five fixed-answer questions first, test them in customer wording, and expand only after those answers work correctly. [AIWealthPath — JKmSoDIpfdI @ 00:02:09]",
                    "Save the perfected niche agent as a default snapshot; new client accounts receive it paused until their channels are connected. [Sohaib — lvzJJWDX0ec @ 00:06:05]",
                    "Use the client's website to generate a demo link so they can try the assistant on their own site without installing anything. [Sohaib — lvzJJWDX0ec @ 00:06:36]",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Audit the repeated workload",
                    "action": "Collect recurring questions and identify the routine conversations to automate.",
                    "detail": "Analyze existing customer messages, then structure the company information that the support setup will need. [Ventra Technologies — b5pi4BcdrKk @ 00:03:29]",
                },
                {
                    "step": 2,
                    "title": "Build the knowledge and narrow the launch",
                    "action": "Write complete answers and configure the first five fixed-answer questions.",
                    "detail": "Test each question as a customer would ask it, checking that the reply is correct, friendly, and short before adding the next five. [AIWealthPath — JKmSoDIpfdI @ 00:02:09]",
                },
                {
                    "step": 3,
                    "title": "Test the agent and its human route",
                    "action": "Configure behavior, add the person-contact option, and test before publishing.",
                    "detail": "In Zendesk, add the option to talk to a real person for an unknown question, complete behavior settings, and test before selecting Publish AI Agent. [Stewart Gauld — nMMWXxBsH2o @ 00:06:41]",
                },
                {
                    "step": 4,
                    "title": "Review real support every week",
                    "action": "Track first replies, autonomous answers, and mistakes; repair the knowledge document.",
                    "detail": "Spend twenty minutes weekly reviewing the three measures, then fix the top three incorrect answers and test those questions again. [AIWealthPath — JKmSoDIpfdI @ 00:03:33]",
                },
            ],
        },
        {
            "id": "disagreements-and-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Zendesk and Intercom split the reviewers along workflow lines. Jake's Tech Lab gives Zendesk "
                    "the advantage in ticketing, reporting, multichannel messaging, and security controls, while "
                    "Intercom wins its comparison on AI, entry pricing, and CRM-oriented sales work "
                    "[vSmuuzicQUU @ 00:04:09]. Jake describes Zendesk's deep reporting and larger integration "
                    "catalog against Intercom's conversational analytics and chat-first engagement. SparrowDesk "
                    "draws the same distinction as cases versus conversations: Zendesk emphasizes queues, "
                    "service-level workflows, and complex escalations, while Intercom emphasizes fast messaging, "
                    "product tours, and proactive nudges [db2s9r04icM @ 00:00:14]. Setup speed is where the "
                    "accounts diverge. Zendesk says an agent can begin with a help-center connection and brand "
                    "personality, then take on advanced actions through conversation flows "
                    "[mnFYeyoS2r8 @ 00:01:50]. Daniel Davidson describes Zendesk implementations taking weeks "
                    "or months when the business needs operational depth, multiple departments, custom databases, "
                    "and extensive routing [GYTt2lhl7Ms @ 00:06:52]. The difference remains visible in the "
                    "jobs each speaker describes: a connected knowledge agent on one side, and a complex "
                    "support operation on the other. SparrowDesk favors Intercom for quick configuration "
                    "and Zendesk for control with ongoing tuning. Jake's final recommendation is likewise "
                    "workflow-specific: ticket-centered teams get Zendesk, while chat-first support and "
                    "lead-nurturing teams get Intercom."
                ),
                (
                    "The small-store rankings disagree even when the reviewers like the same answers. AI Tool "
                    "Lab gives Intercom Fin the best answer quality in its four-message test: policy-following "
                    "refund handling, actual tracking information, and a calm refusal of the fabricated-order "
                    "discount demand. It still ranks Fin third because of billing, while Tidio Lyro wins "
                    "the small-store comparison [9wewuc4s038 @ 00:03:18]. Daniel Davidson favors SparrowDesk "
                    "for the balance of setup speed, autonomous support, copilot assistance, and workflow "
                    "usability; for direct storefront control, Davidson points to Gorgias "
                    "[GYTt2lhl7Ms @ 00:09:11]. AI Tool Lab places Gorgias fourth despite its fastest order "
                    "answer, because an automated interaction also consumes a helpdesk ticket allowance "
                    "[9wewuc4s038 @ 00:02:40]. AI Tools for Business divides its recommendations into Tidio "
                    "for a free small-store start, Intercom for buyers willing to pay per outcome, and "
                    "Zendesk for larger-scale suite requirements rather than one- or two-person teams "
                    "[T6Ij8zqR4Bo @ 00:05:53]. These are different buying priorities, not a shared winner. "
                    "One comparison rewards the smallest practical starting bill, another rewards an integrated "
                    "agent-and-copilot workflow, and another rewards direct order operations. Davidson's Gorgias "
                    "recommendation explicitly keeps ticket-volume costs in view, while AI Tool Lab makes "
                    "those same costs the reason to rank it lower."
                ),
                (
                    "The pricing accounts contain disagreements that should remain attached to their speakers. "
                    "SparrowDesk calls Zendesk's per-agent pricing predictable and contrasts it with Intercom's "
                    "seat-plus-usage growth [db2s9r04icM @ 00:01:02]. AI Tools for Business instead describes "
                    "Zendesk's seat charge, small included AI allowance, and roughly $1.50–$2 automated-resolution "
                    "overage; it also says the $19 Support Team tier lacks live chat and AI agents "
                    "[T6Ij8zqR4Bo @ 00:02:32]. Rocket Research says AI agents are included in suite and support "
                    "plans, quotes the $19 annual starting point, and separately identifies usage and Copilot "
                    "charges [swIGkbLXEdM @ 00:01:10]. Those statements do not give the same account of "
                    "entry-plan eligibility. Beyond that comparison, Toolstack recommends choosing around an "
                    "existing ecosystem: HubSpot Breeze connects to CRM history but makes less sense as a "
                    "reason to enter HubSpot solely for support [aNlthYD5fPY @ 00:03:03]. Toolstack similarly "
                    "positions Freshdesk Freddy around triage and response assistance, Salesforce Einstein "
                    "around enterprise CRM operations, and Zoho Desk Zia around the Zoho stack. The alternative "
                    "playbook is therefore not always migration to a ranking winner. Toolstack repeatedly "
                    "points to the support tools already connected to the company's customer information, "
                    "while the pricing reviewers disagree over which headline plan actually delivers AI."
                ),
            ],
            "table": {
                "caption": "Contrasts that change the platform decision without forcing a universal winner",
                "headers": ["Decision or contrast", "Side-by-side practitioner positions", "Expert Source"],
                "rows": [
                    [
                        "Choose structured case handling or conversational engagement as the primary workflow.",
                        "Jake favors Zendesk's ticketing depth; SparrowDesk contrasts its case structure with Intercom's messaging-first experience.",
                        "Jake's Tech Lab ([vSmuuzicQUU @ 00:00:49]); SparrowDesk ([db2s9r04icM @ 00:00:14])",
                    ],
                    [
                        "Separate an initial knowledge agent from a complex support implementation.",
                        "Zendesk describes quick help-center setup; Davidson describes weeks or months for heavier Zendesk operations.",
                        "Zendesk ([mnFYeyoS2r8 @ 00:01:50]); Daniel Davidson ([GYTt2lhl7Ms @ 00:06:52])",
                    ],
                    [
                        "Distinguish the strongest tested answers from the preferred small-store bill.",
                        "AI Tool Lab calls Fin the best answering bot but ranks Tidio first for small-store economics.",
                        "AI Tool Lab ([9wewuc4s038 @ 00:03:18]); AI Tool Lab ([9wewuc4s038 @ 00:06:30])",
                    ],
                    [
                        "Gorgias gains storefront control while retaining its ticket-volume cost exposure.",
                        "Davidson recommends direct storefront control; AI Tool Lab penalizes the simultaneous AI and ticket meters.",
                        "Daniel Davidson ([GYTt2lhl7Ms @ 00:09:11]); AI Tool Lab ([9wewuc4s038 @ 00:02:40])",
                    ],
                    [
                        "Zendesk's predictable-seat description conflicts with the more detailed usage-billing account.",
                        "SparrowDesk emphasizes predictable per-agent pricing; AI Tools for Business adds allowances and automated-resolution overages.",
                        "SparrowDesk ([db2s9r04icM @ 00:01:02]); AI Tools for Business ([T6Ij8zqR4Bo @ 00:02:53])",
                    ],
                    [
                        "Existing CRM integration supplies an alternative to switching for a standalone bot.",
                        "Toolstack favors Breeze for existing HubSpot users; Simply Contact offers human-plus-AI outsourcing instead of software alone.",
                        "Toolstack ([aNlthYD5fPY @ 00:03:03]); Simply Contact ([DcDfJRzuZNI @ 00:00:19])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-and-economics",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Wardrop's live call exposes a useful boundary: when asked how soon someone can visit "
                    "to quote the landscaping work, the agent says it does not have that information and "
                    "will have a team member follow up. It collects the project details rather than booking "
                    "an unsupported visit [CDVbVmBQVyc @ 00:09:47]. Davidson reports a different firsthand "
                    "test with Fin: responses stayed grounded in linked sources, remained neutral, and did "
                    "not fabricate guarantees outside the agent's scope; requests beyond its ability moved "
                    "to a human after confirmation [GYTt2lhl7Ms @ 00:03:55]. The broader failure warnings "
                    "come from Ventra Technologies, which describes raw models inventing return policies, "
                    "prices, and delivery areas without internal business context "
                    "[b5pi4BcdrKk @ 00:01:04]. AIWealthPath names the operating mistakes that keep creating "
                    "those problems: hiding the phone number or email, promising unavailable delivery, leaving "
                    "old prices and policies unchecked, and automating the apology to an upset customer "
                    "[JKmSoDIpfdI @ 00:04:08]. The demonstrated calls and the warnings point to concrete "
                    "checks: what happens when availability is missing, whether a request exceeds scope, "
                    "and whether a person remains reachable. Wardrop's agent did not know the visit schedule; "
                    "the test showed that limitation directly. AIWealthPath's weekly review keeps the "
                    "knowledge document current instead of treating installation as the last operating task."
                ),
                (
                    "AI Tool Lab's four-message exercise tests a wrong-size refund, order tracking, a worn "
                    "item returned after thirty-five days, and a demand for fifty percent off backed by "
                    "a nonexistent order. Its scoring includes answer quality, setup effort, free-tier "
                    "value, and what a solved problem actually costs "
                    "[9wewuc4s038 @ 00:00:39]. The billing findings are sharper than the ranking: Fin can "
                    "count twenty-four hours of customer silence as an assumed resolution; Lyro charges "
                    "for conversations it joins even if the problem remains unresolved; Gorgias consumes "
                    "both AI and ticket allowances; and Chatbase credits vary with model choice and actions "
                    "[9wewuc4s038 @ 00:05:36]. AI Tools for Business separately distinguishes Tidio's recurring "
                    "free-plan conversation allowance from the fifty free Lyro conversations, which it "
                    "describes as a one-time lifetime grant [T6Ij8zqR4Bo @ 00:04:13]. AI Tool Lab also makes "
                    "that one-time Lyro warning, despite later using monthly free-plan wording. Davidson "
                    "adds another meter distinction: Freshdesk's included Freddy sessions count conversations "
                    "the AI touched, not necessarily conversations it resolved "
                    "[GYTt2lhl7Ms @ 00:05:07]. None of those labels should be silently substituted for "
                    "another. The reviewers distinguish a seat, a ticket, a session, a conversation, a "
                    "credit, and an outcome precisely because the reported charges follow different events."
                ),
                (
                    "Sohaib identifies four agency-specific money leaks. Trial credits leave the agency pool "
                    "when the trial starts, so widely promoted trials should keep the allocation low. An "
                    "underfunded pool can block a new buyer's signup without charging them. A reselling "
                    "client's monthly allowance should be zero, or usage can continue draining the agency "
                    "pool after the client's purchased credits run out. Features enabled manually can disappear "
                    "at renewal unless included in the client's plan "
                    "[lvzJJWDX0ec @ 00:07:48]. Sohaib also quotes $27 for each extra client above the entry "
                    "plan and says the $497 Unlimited plan becomes cheaper past about seventeen clients "
                    "[lvzJJWDX0ec @ 00:07:10]. Deployment effort is another stated bottleneck: Gauld calls "
                    "Zendesk potentially complicated, recommends it especially for businesses already using "
                    "the suite, and says Jot Form is the platform they personally use to build AI agents "
                    "[nMMWXxBsH2o @ 00:09:07]. AI Tools for Business supplies the final operating check: "
                    "run the free plan or trial for two weeks, track autonomous resolutions and cost per "
                    "resolution, and keep the tool if it saves an hour daily "
                    "[T6Ij8zqR4Bo @ 00:06:10]. These checks cover the recurring service after the sale: "
                    "credit availability, renewal behavior, account expansion, deployment complexity, and "
                    "whether the agent is actually removing work from the owner."
                ),
            ],
            "table": {
                "caption": "Observed test behavior and explicitly reported operational traps",
                "headers": ["Failure mode or test boundary", "Practitioner finding and concrete check", "Expert Source"],
                "rows": [
                    [
                        "The landscaping agent did not know when someone could visit.",
                        "During Wardrop's test, it acknowledged missing availability and promised team follow-up instead of giving a time.",
                        "Travis Wardrop ([CDVbVmBQVyc @ 00:09:47])",
                    ],
                    [
                        "Fin's bill can treat customer silence as an assumed resolution.",
                        "AI Tool Lab says twenty-four hours without a customer response can trigger the $0.99 outcome charge.",
                        "AI Tool Lab ([9wewuc4s038 @ 00:03:57])",
                    ],
                    [
                        "A Lyro conversation can cost money without resolving the customer's problem.",
                        "AI Tool Lab says paid Lyro usage bills conversations joined rather than only successful resolutions.",
                        "AI Tool Lab ([9wewuc4s038 @ 00:06:49])",
                    ],
                    [
                        "The free Lyro allocation does not replenish like the general plan allowance.",
                        "AI Tools for Business distinguishes fifty monthly free-plan conversations from the one-time fifty-conversation Lyro grant.",
                        "AI Tools for Business ([T6Ij8zqR4Bo @ 00:04:13])",
                    ],
                    [
                        "Agency trials and depleted shared credits can consume money or stop sales.",
                        "Sohaib says trial credits debit immediately and an insufficient agency pool blocks new buyer signups.",
                        "Sohaib ([lvzJJWDX0ec @ 00:07:48])",
                    ],
                    [
                        "Manual client settings can create continued usage or disappear at renewal.",
                        "Set reselling allowance to zero and place needed features in the plan rather than manual overrides.",
                        "Sohaib ([lvzJJWDX0ec @ 00:08:03])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Check the escape route, the meter, and the agency pool",
                "body": "Use the speakers' specific operating checks before treating the service as ready to keep running.",
                "items": [
                    "Confirm that customers can request a person and that two unsuccessful AI attempts trigger a transfer with the conversation attached. [AIWealthPath — JKmSoDIpfdI @ 00:03:16]",
                    "Separate recurring free-plan conversations from the one-time fifty-conversation Lyro grant before budgeting continued AI use. [AI Tools for Business — T6Ij8zqR4Bo @ 00:04:13]",
                    "Keep trial credit allocations low and the agency pool funded so trials do not consume excessive credits and new buyers are not blocked. [Sohaib — lvzJJWDX0ec @ 00:07:48]",
                    "Set reselling clients' monthly allowance to zero and include required features in their plan so usage and renewals behave as intended. [Sohaib — lvzJJWDX0ec @ 00:08:03]",
                ],
            },
        },
    ],
    "pull_quote": (
        "“Customers do not hate AI support, they hate being stuck with no way out.” "
        "— AIWealthPath (JKmSoDIpfdI @ 00:03:33)."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        "List the ten questions that recur across the inbox, WhatsApp, and comments before selecting the first automation workload. [AIWealthPath — JKmSoDIpfdI @ 00:00:31]",
        "Write the actual delivery costs, delivery times, return window, refund rule, prices, hours, and contact details into one help document. [AIWealthPath — JKmSoDIpfdI @ 00:01:04]",
        "For a missed-call offer, retain the business's public number and route unanswered calls to the new AI backup number. [Travis Wardrop — CDVbVmBQVyc @ 00:07:12]",
        "Test the customer-facing agent and configure a real-person option for unknown questions before publishing it. [Stewart Gauld — nMMWXxBsH2o @ 00:06:41]",
        "Package the working niche agent as a default snapshot and connect each new client's channels while the copied agent remains paused. [Sohaib — lvzJJWDX0ec @ 00:06:05]",
        "Run a two-week trial and track autonomous resolutions plus cost per resolution; apply the speaker's hour-per-day time-saving check. [AI Tools for Business — T6Ij8zqR4Bo @ 00:06:10]",
    ],
    "statutory_citations": [
        {
            "title": "Travis Wardrop — How to Sell AI Automation to Local Businesses (Beginner Guide) [00:07:57]",
            "url": "https://www.youtube.com/watch?v=CDVbVmBQVyc&t=477s",
            "relevance": "Primary practitioner testimony on creating the voice agent's knowledge base from a business website and supplementing it with FAQs.",
        },
        {
            "title": "AIWealthPath — How to Automate Your Customer Support With AI in 2026 — Full Beginner Guide [00:03:16]",
            "url": "https://www.youtube.com/watch?v=JKmSoDIpfdI&t=196s",
            "relevance": "Primary practitioner testimony on immediate human access and escalation after two unsuccessful AI attempts.",
        },
        {
            "title": "AI Tool Lab — I Tested 5 AI Customer Support Chatbots — Ranked Worst to Best (2026) [00:05:36]",
            "url": "https://www.youtube.com/watch?v=9wewuc4s038&t=336s",
            "relevance": "Primary practitioner testimony distinguishing assumed resolutions, joined conversations, tickets, and model-request billing.",
        },
        {
            "title": "Sohaib — How to Build an AI Agency Business Model in 2026 [00:07:48]",
            "url": "https://www.youtube.com/watch?v=lvzJJWDX0ec&t=468s",
            "relevance": "Primary practitioner testimony on agency trial-credit costs, shared-pool availability, client allowances, and renewal behavior.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "CDVbVmBQVyc",
            "title": "How to Sell AI Automation to Local Businesses (Beginner Guide)",
            "channel": "Travis Wardrop",
            "author": "Travis Wardrop",
            "text": "We don't want them to have to change their phone number.",
            "tip": "We don't want them to have to change their phone number.",
            "timestamp": 416,
            "timestamp_seconds": 416,
            "timestamp_label": "[00:06:56]",
            "url": "https://www.youtube.com/watch?v=CDVbVmBQVyc&t=416s",
            "markdown": "[00:06:56](https://www.youtube.com/watch?v=CDVbVmBQVyc&t=416s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on retaining the local business's public telephone number while adding an AI backup.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "9wewuc4s038",
            "title": "I Tested 5 AI Customer Support Chatbots — Ranked Worst to Best (2026)",
            "channel": "AI Tool Lab",
            "author": "AI Tool Lab",
            "text": "Its 50 free AI conversations are a one-time batch, not a monthly refill, and paid conversations bill whether the bot solves it or not.",
            "tip": "Its 50 free AI conversations are a one-time batch, not a monthly refill, and paid conversations bill whether the bot solves it or not.",
            "timestamp": 373,
            "timestamp_seconds": 373,
            "timestamp_label": "[00:06:13]",
            "url": "https://www.youtube.com/watch?v=9wewuc4s038&t=373s",
            "markdown": "[00:06:13](https://www.youtube.com/watch?v=9wewuc4s038&t=373s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the Lyro free allocation and the difference between conversations and successful resolutions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "vSmuuzicQUU",
            "title": "Zendesk vs Intercom Comparison 2025 | Which Customer Support Platform is Best?",
            "channel": "Jake's Tech Lab",
            "author": "Jake's Tech Lab",
            "text": "Intercom is super ideal if you want that chat-first AI-powered experience or if your strategy is all about sales and nurturing leads.",
            "tip": "Intercom is super ideal if you want that chat-first AI-powered experience or if your strategy is all about sales and nurturing leads.",
            "timestamp": 284,
            "timestamp_seconds": 284,
            "timestamp_label": "[00:04:44]",
            "url": "https://www.youtube.com/watch?v=vSmuuzicQUU&t=284s",
            "markdown": "[00:04:44](https://www.youtube.com/watch?v=vSmuuzicQUU&t=284s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on choosing Intercom for conversational support and lead nurturing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "b5pi4BcdrKk",
            "title": "How to Build an AI Customer Support Business",
            "channel": "Ventra Technologies",
            "author": "Ventra Technologies",
            "text": "The first phase of this offering is conducting a support audit, analyzing existing customer messages to identify exactly which repetitive questions can safely be automated.",
            "tip": "The first phase of this offering is conducting a support audit, analyzing existing customer messages to identify exactly which repetitive questions can safely be automated.",
            "timestamp": 192,
            "timestamp_seconds": 192,
            "timestamp_label": "[00:03:12]",
            "url": "https://www.youtube.com/watch?v=b5pi4BcdrKk&t=192s",
            "markdown": "[00:03:12](https://www.youtube.com/watch?v=b5pi4BcdrKk&t=192s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on auditing repetitive support work before selling and implementing the setup.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "JKmSoDIpfdI",
            "title": "How to Automate Your Customer Support With AI in 2026 — Full Beginner Guide",
            "channel": "AIWealthPath",
            "author": "AIWealthPath",
            "text": "If the AI cannot answer in two tries, it hands over immediately with the whole conversation attached, so the customer never has to repeat themselves.",
            "tip": "If the AI cannot answer in two tries, it hands over immediately with the whole conversation attached, so the customer never has to repeat themselves.",
            "timestamp": 196,
            "timestamp_seconds": 196,
            "timestamp_label": "[00:03:16]",
            "url": "https://www.youtube.com/watch?v=JKmSoDIpfdI&t=196s",
            "markdown": "[00:03:16](https://www.youtube.com/watch?v=JKmSoDIpfdI&t=196s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the two-attempt escalation rule and preserving conversation context.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "mnFYeyoS2r8",
            "title": "AI Agents: The next generation of AI-powered bots | Zendesk",
            "channel": "Zendesk",
            "author": "Zendesk",
            "text": "Currently, AI agents are helping companies resolve 60% or more of their customer interactions.",
            "tip": "Currently, AI agents are helping companies resolve 60% or more of their customer interactions.",
            "timestamp": 165,
            "timestamp_seconds": 165,
            "timestamp_label": "[00:02:45]",
            "url": "https://www.youtube.com/watch?v=mnFYeyoS2r8&t=165s",
            "markdown": "[00:02:45](https://www.youtube.com/watch?v=mnFYeyoS2r8&t=165s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Zendesk's attributed interaction-resolution claim for its AI agents.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "DcDfJRzuZNI",
            "title": "Top 10 AI Customer Service Companies",
            "channel": "Simply Contact",
            "author": "Simply Contact",
            "text": "Simply Contact is a customer service outsourcing provider that combines human agents with advanced AI tools.",
            "tip": "Simply Contact is a customer service outsourcing provider that combines human agents with advanced AI tools.",
            "timestamp": 19,
            "timestamp_seconds": 19,
            "timestamp_label": "[00:00:19]",
            "url": "https://www.youtube.com/watch?v=DcDfJRzuZNI&t=19s",
            "markdown": "[00:00:19](https://www.youtube.com/watch?v=DcDfJRzuZNI&t=19s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the combined human-and-AI outsourcing delivery model.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "nMMWXxBsH2o",
            "title": "How to use ZenDesk AI Agents | Supercharge Customer Service with AI in 2026",
            "channel": "Stewart Gauld",
            "author": "Stewart Gauld",
            "text": "If a question is unknown, then we also want to add an option to talk to a real person.",
            "tip": "If a question is unknown, then we also want to add an option to talk to a real person.",
            "timestamp": 401,
            "timestamp_seconds": 401,
            "timestamp_label": "[00:06:41]",
            "url": "https://www.youtube.com/watch?v=nMMWXxBsH2o&t=401s",
            "markdown": "[00:06:41](https://www.youtube.com/watch?v=nMMWXxBsH2o&t=401s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on configuring Zendesk agent behavior for unknown questions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "aNlthYD5fPY",
            "title": "Every AI Customer Service Tool Explained",
            "channel": "Toolstack",
            "author": "Toolstack",
            "text": "In practice, results vary a lot depending on how good your knowledge base is.",
            "tip": "In practice, results vary a lot depending on how good your knowledge base is.",
            "timestamp": 65,
            "timestamp_seconds": 65,
            "timestamp_label": "[00:01:05]",
            "url": "https://www.youtube.com/watch?v=aNlthYD5fPY&t=65s",
            "markdown": "[00:01:05](https://www.youtube.com/watch?v=aNlthYD5fPY&t=65s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the dependence of Fin's performance on knowledge-base quality.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "swIGkbLXEdM",
            "title": "How Much Should a Small Business Budget for AI Customer Support in 2026?",
            "channel": "Rocket Research",
            "author": "Rocket Research",
            "text": "Corby provides a straightforward pricing model with a flat monthly fee starting at $99 for the pro plan.",
            "tip": "Corby provides a straightforward pricing model with a flat monthly fee starting at $99 for the pro plan.",
            "timestamp": 19,
            "timestamp_seconds": 19,
            "timestamp_label": "[00:00:19]",
            "url": "https://www.youtube.com/watch?v=swIGkbLXEdM&t=19s",
            "markdown": "[00:00:19](https://www.youtube.com/watch?v=swIGkbLXEdM&t=19s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on a flat-rate alternative to seat-plus-resolution pricing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "T6Ij8zqR4Bo",
            "title": "3 AI Customer Support Tools for US Small Businesses in 2026 — Intercom vs Zendesk vs Tidio",
            "channel": "AI Tools for Business",
            "author": "AI Tools for Business",
            "text": "Use the free plan or the free trial for two weeks and track two numbers: how many chats the AI resolves on its own and what that costs you per resolution.",
            "tip": "Use the free plan or the free trial for two weeks and track two numbers: how many chats the AI resolves on its own and what that costs you per resolution.",
            "timestamp": 370,
            "timestamp_seconds": 370,
            "timestamp_label": "[00:06:10]",
            "url": "https://www.youtube.com/watch?v=T6Ij8zqR4Bo&t=370s",
            "markdown": "[00:06:10](https://www.youtube.com/watch?v=T6Ij8zqR4Bo&t=370s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on measuring autonomous resolutions and their cost during a two-week evaluation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "db2s9r04icM",
            "title": "Intercom vs Zendesk: Pricing, features, AI, and which is better in 2026",
            "channel": "SparrowDesk",
            "author": "SparrowDesk",
            "text": "Zendesk's AI offers more control, but requires heavier setup and ongoing tuning.",
            "tip": "Zendesk's AI offers more control, but requires heavier setup and ongoing tuning.",
            "timestamp": 45,
            "timestamp_seconds": 45,
            "timestamp_label": "[00:00:45]",
            "url": "https://www.youtube.com/watch?v=db2s9r04icM&t=45s",
            "markdown": "[00:00:45](https://www.youtube.com/watch?v=db2s9r04icM&t=45s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony contrasting configuration speed with control and customization.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "vxbipxTJGgw",
            "title": "What are AI Agents for customer service? Zendesk AI explained",
            "channel": "Zendesk",
            "author": "Zendesk",
            "text": "When needed, AI agents can escalate to human agents, pass along context, and ensure a seamless handoff so customers don't have to repeat themselves.",
            "tip": "When needed, AI agents can escalate to human agents, pass along context, and ensure a seamless handoff so customers don't have to repeat themselves.",
            "timestamp": 127,
            "timestamp_seconds": 127,
            "timestamp_label": "[00:02:07]",
            "url": "https://www.youtube.com/watch?v=vxbipxTJGgw&t=127s",
            "markdown": "[00:02:07](https://www.youtube.com/watch?v=vxbipxTJGgw&t=127s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Zendesk testimony on transferring customer context when an AI agent escalates.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "GYTt2lhl7Ms",
            "title": "5 Best AI Customer Support Platforms (2026) - Top 5 Ranked",
            "channel": "Daniel Davidson",
            "author": "Daniel Davidson",
            "text": "A lower bill loses its appeal if your team spends more time correcting answers.",
            "tip": "A lower bill loses its appeal if your team spends more time correcting answers.",
            "timestamp": 551,
            "timestamp_seconds": 551,
            "timestamp_label": "[00:09:11]",
            "url": "https://www.youtube.com/watch?v=GYTt2lhl7Ms&t=551s",
            "markdown": "[00:09:11](https://www.youtube.com/watch?v=GYTt2lhl7Ms&t=551s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on evaluating correction workload alongside the software bill.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "lvzJJWDX0ec",
            "title": "How to Build an AI Agency Business Model in 2026",
            "channel": "Sohaib",
            "author": "Sohaib",
            "text": "The agency plan is $297 a month with 1,000 credits and 10 client accounts included.",
            "tip": "The agency plan is $297 a month with 1,000 credits and 10 client accounts included.",
            "timestamp": 410,
            "timestamp_seconds": 410,
            "timestamp_label": "[00:06:50]",
            "url": "https://www.youtube.com/watch?v=lvzJJWDX0ec&t=410s",
            "markdown": "[00:06:50](https://www.youtube.com/watch?v=lvzJJWDX0ec&t=410s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the quoted DM Champ agency plan and its included capacity.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "lvzJJWDX0ec",
            "title": "How to Build an AI Agency Business Model in 2026",
            "channel": "Sohaib",
            "author": "Sohaib",
            "text": "Trial credits come out of your pool the moment the trial starts, so keep them low on a plan you promote widely.",
            "tip": "Trial credits come out of your pool the moment the trial starts, so keep them low on a plan you promote widely.",
            "timestamp": 468,
            "timestamp_seconds": 468,
            "timestamp_label": "[00:07:48]",
            "url": "https://www.youtube.com/watch?v=lvzJJWDX0ec&t=468s",
            "markdown": "[00:07:48](https://www.youtube.com/watch?v=lvzJJWDX0ec&t=468s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on trial-credit consumption as an agency operating expense.",
        },
    ],
}
