from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "ai-voice-agents-builds-comparisons-real-world-tests",
    "question_prompt": "What do these videos teach about building AI voice agents and receptionists, using Vapi to call new leads within 60 seconds, automating insurance first-notice-of-loss (FNOL) calls with Bland AI, comparing voice-agent platforms and call handling, choosing Retell or Vapi for a voice AI agency, and understanding the technology’s limitations?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "AI Voice Agents: Build Tutorials, Platform Comparisons & Real-World Tests",
    "subtitle": "Beginner guides, reviews, and comparisons covering Bland AI, Retell, Vapi, ElevenLabs, Synthflow, Play AI, Air AI, and CloudTalk—with AI receptionists, rapid lead calling, insurance FNOL automation, agency platform selection, and voice-agent pitfalls.",
    "layout_template": "legal_compliance_callout",
    "reading_time_minutes": 15,
    "executive_summary": (
        "The builders converge on focused call flows, business-specific knowledge, explicit human handoffs, "
        "and testing beyond a smooth demonstration. Alex Leischow connects specialized Vapi assistants into "
        "a squad and reports a lead callback within 10 seconds. Bland partitions insurance intake around "
        "safety, policy lookup, loss details, and escalation. Anthony Shoosh builds a prompted gym receptionist; "
        "Sonny Sangha uses Norm to generate and repair dental booking workflows. Platform verdicts split: "
        "Venture Harbour favors Vapi's cost and latency, while Alejo Pijuan favors Retell after deployment "
        "failures and support delays. Stephanie Nyarko chooses according to customization needs and agency "
        "size; David Alex prefers CloudTalk for businesses wanting an integrated phone system. Brendan Jowett "
        "puts the operational emphasis on simpler scope, post-call automation, and preserving human sales work."
    ),
    "key_metrics": [
        {
            "label": "Speed-to-lead demonstration",
            "metric": "Speed-to-lead demonstration",
            "value": "Callback within 10 seconds",
            "confidence": "attributed_practitioner_claim",
            "context": "Alex reports this callback time after submitting the plumbing quote form; the tutorial's stated target is within 60 seconds.",
            "source": "Alex Leischow ([8yIHmsMHMYc @ 00:15:01])",
        },
        {
            "label": "Retell standardized latency test",
            "metric": "Retell standardized latency test",
            "value": "714 milliseconds end-to-end",
            "confidence": "attributed_practitioner_claim",
            "context": "Voice AI Decoded recalls this standardized test result while showing a separate call-log reading of 756 milliseconds.",
            "source": "Voice AI Decoded ([UiKoEHbio38 @ 00:07:37])",
        },
        {
            "label": "Vapi monthly comparison scenario",
            "metric": "Vapi monthly comparison scenario",
            "value": "Around $180 per month",
            "confidence": "attributed_practitioner_claim",
            "context": "Venture Harbour estimates 2,000 monthly minutes using a standard GPT-4.1 setup without the additional HIPAA option; Retell is about $80 more in that comparison.",
            "source": "Venture Harbour ([ZVSDm5siKr4 @ 00:13:44])",
        },
        {
            "label": "CloudTalk AI entry package",
            "metric": "CloudTalk AI entry package",
            "value": "$99 per month for 200 AI minutes",
            "confidence": "attributed_practitioner_claim",
            "context": "David Alex describes AI voice agents as an add-on to the phone-system plans, covering receptionist and specialist agent types.",
            "source": "David Alex ([Ucjk1DJkxuE @ 00:08:42])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The recurring job is answering, qualifying, collecting details, and getting the caller to the "
                    "right next step—not simply attaching a convincing voice to a phone number. Anthony Shoosh's "
                    "Planet Fitness receptionist has a defined goal, call flow, background, and example dialogue. "
                    "It greets the caller, lets the caller explain the request, answers membership questions, "
                    "explains signup, and closes after offering further help. His business information sits in an "
                    "attached knowledge base rather than depending on the voice alone [S5UwzzP_Qec @ 00:06:05]. "
                    "Daniel builds an auto-repair receptionist around the same operational specificity. Conductor "
                    "asks how appointments should work, where emergency inquiries should go, and what the shop is "
                    "called before generating the workflow [PgrkNMNc_Cw @ 00:02:43]. Brendan Jowett approaches that "
                    "preparation through existing operations: his team asks clients for call recordings, scripts, "
                    "and resources, and he says a workflow nobody has handled manually is a poor starting point "
                    "for automation [Ky2Z6kGp1Vk @ 00:11:01]. These builders describe concrete business conversations "
                    "before configuring the agent. Shoosh supplies example membership exchanges; Daniel reviews "
                    "branches for pricing, missing contact information, and requests for a person; Jowett wants "
                    "the objections and unusual questions that actual callers have already raised. The shared "
                    "baseline is a recognizable service process with business information and a defined next action."
                ),
                (
                    "Focused pieces recur across the builds, even when the overall call can take several routes. "
                    "Alex Leischow says a long, complicated assistant prompt becomes confused and produces unnatural "
                    "calls. His plumbing example instead uses about eight assistants, each responsible for a "
                    "specific function, with a router deciding whether the inquiry belongs to sales, service, "
                    "billing, or an emergency path [8yIHmsMHMYc @ 00:04:12]. Voice AI Decoded recommends Retell's "
                    "conversation-flow canvas because separate steps give the model only the context needed at "
                    "that point, rather than sending one gigantic prompt throughout the conversation "
                    "[UiKoEHbio38 @ 00:00:26]. Venture Harbour applies that approach to a golf receptionist: keep "
                    "the global prompt relatively small, use it for persona and listening style, and put task "
                    "instructions in the relevant nodes [ZVSDm5siKr4 @ 00:04:43]. Bland's insurance design likewise "
                    "partitions the call according to the understanding needed at each stage, beginning with "
                    "whether everyone is safe and whether immediate assistance is needed [W1Y3bHct_e0 @ 00:00:15]. "
                    "The implementations differ—assistants connected by tools, visual conversation nodes, or "
                    "insurance pathways—but each builder separates responsibilities. Alex still supports multiple "
                    "business departments; Venture Harbour still checks availability and books appointments; Bland "
                    "still distinguishes auto, property, and other losses. Narrow instructions do not mean every "
                    "caller must follow one identical script."
                ),
                (
                    "Testing and escalation are part of the working build, not decorative dashboard features. "
                    "Daniel tests a corrected phone number, refusal to provide contact information, and a roadside "
                    "breakdown during a normal booking conversation. The agent updates the number without restarting "
                    "the process, stops asking when contact information is refused, and attempts an emergency "
                    "transfer [PgrkNMNc_Cw @ 00:06:04]. Venture Harbour first proves that a golf booking reaches "
                    "Google Calendar, then adds a globally accessible human-transfer branch and an unavailable-slot "
                    "branch instead of stopping at that successful call [ZVSDm5siKr4 @ 00:06:22]. Alejo Pijuan says "
                    "both Vapi and Retell have voice tests, chat tests, and testing suites; he describes simulated "
                    "caller personas and success criteria that can be run together after changes to check whether "
                    "performance improved or deteriorated [6Fal62hzEs8 @ 00:09:20]. These are practical checks on "
                    "conversation behavior and workflow execution. Daniel also reads the transcript, generated "
                    "summary, outcome, and sentiment rather than treating a completed conversation as automatically "
                    "successful. Venture Harbour watches the actual calendar and tests an already occupied time. "
                    "Pijuan treats repeated simulations as a way to evaluate changes, not merely demonstrate the "
                    "voice. Across these approaches, the operator examines what the agent did when the caller "
                    "corrected information, departed from the main route, or needed a person."
                ),
            ],
            "table": {
                "caption": "Shared operating patterns across the receptionist, lead-response, and insurance builds",
                "headers": ["Operating pattern", "Practitioner execution", "Expert Source"],
                "rows": [
                    [
                        "Give the receptionist a specific business job before tuning its voice",
                        "Shoosh structures the prompt around goal, call flow, background, and example dialogue for membership inquiries.",
                        "Anthony Shoosh ([S5UwzzP_Qec @ 00:05:07])",
                    ],
                    [
                        "Resolve appointment and escalation details before generating the workflow",
                        "Conductor asks Daniel how scheduling should work and where emergency calls should be forwarded before producing its plan.",
                        "Daniel | Tech & Data ([PgrkNMNc_Cw @ 00:02:59])",
                    ],
                    [
                        "Separate complex calls into assistants with narrowly defined responsibilities",
                        "Alex uses about eight assistants so routing, sales, service, billing, and emergency handling do not occupy one oversized prompt.",
                        "Alex Leischow ([8yIHmsMHMYc @ 00:04:46])",
                    ],
                    [
                        "Keep broad instructions small and put task context in nodes",
                        "Venture Harbour limits global instructions to tone, listening style, and purpose while putting booking logic into relevant conversation nodes.",
                        "Venture Harbour ([ZVSDm5siKr4 @ 00:04:43])",
                    ],
                    [
                        "Make urgent departures accessible from anywhere in the conversation",
                        "Bland uses global nodes for immediate emergency direction, live-agent requests, callbacks, and handling an existing claim separately.",
                        "Bland ([W1Y3bHct_e0 @ 00:00:42])",
                    ],
                    [
                        "Evaluate changed agents against repeatable simulated caller scenarios",
                        "Pijuan describes persona simulations with success criteria that can run in batches to identify performance degradation after changes.",
                        "Alejo Pijuan ([6Fal62hzEs8 @ 00:09:38])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Alex Leischow's speed-to-lead build starts with a website form carrying the caller's name, "
                    "number, address, and request. The router's opening message receives those fields dynamically, "
                    "so the callback can identify the submitted inquiry and confirm the address instead of "
                    "starting cold. Its only job is deciding which workflow should take over "
                    "[8yIHmsMHMYc @ 00:05:05]. Specialized assistants then handle their own questioning: sales "
                    "collects project details, while service investigates the issue and whether it is an emergency. "
                    "Handoff tools connect those assistants inside a squad; separate tools end the call or "
                    "transfer to a live person. In the plumbing demonstration, the caller describes old pipes, "
                    "rust, and an approximately twenty-year age, and the agent says a coordinator will follow up "
                    "with the estimate. Alex reports receiving the callback within ten seconds. Make then supports "
                    "the downstream work: logging the call in Airtable, notifying the relevant team by email, "
                    "updating a CRM, or sending Slack notifications from the call data. Anthony Shoosh shows the "
                    "corresponding post-call mechanism in Bland: specify extracted details such as name, phone "
                    "number, and reason for calling, then place the destination webhook in the advanced settings "
                    "[S5UwzzP_Qec @ 00:10:09]. In both walkthroughs, the conversation produces structured information "
                    "that another workflow can use after the caller hangs up."
                ),
                (
                    "For direct appointment booking, Venture Harbour builds a Vapi workflow with a greeting, a "
                    "booking conversation, availability checking, event creation, confirmation, and a polite ending. "
                    "The booking prompt collects the requested date and time, name, number of players, nine or "
                    "eighteen holes, and contact number. It passes the current time through a now variable so "
                    "relative dates can be converted into actual dates [ZVSDm5siKr4 @ 00:00:54]. The Google Calendar "
                    "tools require the calendar ID, the correct timezone, and an enabled integration. The unavailable "
                    "branch checks for the nearest alternative and returns to the booking conversation. Sonny Sangha "
                    "takes a generated-workflow route in Bland: upload the dental clinic information, ask Norm to "
                    "create the receptionist, and connect appointment booking. His example uses Cal.com, a "
                    "sixty-minute dental consultation event, an API key, and the event type ID "
                    "[JSYOZvtkAx4 @ 00:09:33]. Daniel's Retell route begins with a written plan, then Build produces "
                    "nine connected nodes, including branches for failed transfers and callers withholding contact "
                    "information [PgrkNMNc_Cw @ 00:04:23]. These walkthroughs show three distinct construction "
                    "methods: manually assembled Vapi nodes, Norm-generated Bland personas and pathways, and "
                    "Conductor-generated Retell workflows. Each includes more than spoken appointment language: "
                    "there is either a connected booking tool or an explicit process for collecting details and "
                    "passing the request onward."
                ),
                (
                    "Bland's FNOL pathway starts by checking safety, then collects policy information and can "
                    "dynamically look up the policy from details the caller supplies. Once the policy is confirmed, "
                    "the flow separates auto, property, and other losses; auto handling includes vehicle information "
                    "and injuries, while assistance tools can support towing or a rental car "
                    "[W1Y3bHct_e0 @ 00:01:35]. The design confirms the collected information, creates the claim, "
                    "and provides a closing message. A missing policy or a more delicate issue can go to a specialist "
                    "through a warm transfer. Its interrupted emergency demonstration tells the caller to stop "
                    "the claim conversation and call 911. For a simpler inbound build, Shoosh buys a Bland number, "
                    "chooses a voice, uses the recommended prompt structure, and reports a $15 monthly number "
                    "charge plus nine cents per minute [S5UwzzP_Qec @ 00:04:37]. Those figures differ from Sonny "
                    "Sangha's stated fourteen-cent rate and Voice AI Decoded's roughly eleven-to-twelve-cent "
                    "Bland estimate. Voice AI Decoded also reports Retell at about thirteen cents per minute for "
                    "a standard stack and explains that model and telephony choices change the total "
                    "[UiKoEHbio38 @ 00:08:42]. The practitioners attach prices to their particular configurations "
                    "and comparisons; their quoted Bland rates are not identical, even though the monthly number "
                    "price recurs across the walkthroughs."
                ),
            ],
            "table": {
                "caption": "Build components, quoted prices, and the exact work each component performs",
                "headers": ["Build component or number", "Execution detail", "Expert Source"],
                "rows": [
                    [
                        "Personalize the first callback with the submitted form fields",
                        "Alex feeds the name, address, and request into the router message, which confirms the inquiry before selecting the appropriate assistant.",
                        "Alex Leischow ([8yIHmsMHMYc @ 00:05:22])",
                    ],
                    [
                        "Connect specialized assistants through explicit handoff tools and a squad",
                        "Create tools targeting the sales, service, billing, or transfer assistant, then connect those tools and assistants on the squad canvas.",
                        "Alex Leischow ([8yIHmsMHMYc @ 00:10:44])",
                    ],
                    [
                        "Wire Google Calendar availability and event creation as separate tools",
                        "Use the calendar ID, align the timezone, authorize the Google Calendar integration, and attach both tools to the booking workflow.",
                        "Venture Harbour ([ZVSDm5siKr4 @ 00:03:17])",
                    ],
                    [
                        "Give Norm the booking service details it actually needs",
                        "Sonny uses a Cal.com consultation event, supplies an API key, and answers the request for the event type ID.",
                        "Sonny Sangha ([JSYOZvtkAx4 @ 00:11:13])",
                    ],
                    [
                        "Look up policy information dynamically during insurance intake",
                        "Bland lets the agent invoke policy lookup from supplied details and then vary subsequent questions according to the reported loss type.",
                        "Bland ([W1Y3bHct_e0 @ 00:01:35])",
                    ],
                    [
                        "Separate the Vapi platform charge from provider-dependent usage charges",
                        "Venture Harbour quotes a five-cent platform fee per minute, with language-model inference and text-to-speech charges added on top.",
                        "Venture Harbour ([ZVSDm5siKr4 @ 00:13:12])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small build decisions the practitioners actually use",
                "body": "Keep the conversational details and the downstream data handling as deliberate as the voice selection.",
                "items": [
                    "Use a phone number instead of an email address as the golf booking identifier; Venture Harbour avoids letter-by-letter email capture because one wrong character makes it useless. [Venture Harbour — ZVSDm5siKr4 @ 00:01:32]",
                    "Extract number of holes as a numeric variable instead of leaving it buried in a calendar title; Venture Harbour notices the second booking omitted that detail. [Venture Harbour — ZVSDm5siKr4 @ 00:11:04]",
                    "Use Bland's knowledge-base query logs to inspect test questions, retrieved results, and confidence scores, as Sonny does for the dental clinic's insurance information. [Sonny Sangha — JSYOZvtkAx4 @ 00:08:05]",
                    "Inspect Retell's latency breakdown by transcription, language model, and speech generation before changing components; Voice AI Decoded identifies the language-model stage as the main opportunity in the displayed call. [Voice AI Decoded — UiKoEHbio38 @ 00:07:53]",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Define the service and collect its operating information",
                    "action": "Write the business goal and expected call flow before assembling the agent.",
                    "detail": "Follow Shoosh's goal, call flow, background, and example-dialogue prompt structure; attach the business knowledge base used to answer customer questions. [Anthony Shoosh — S5UwzzP_Qec @ 00:05:07]",
                },
                {
                    "step": 2,
                    "title": "Split routing from specialist questioning",
                    "action": "Create focused assistants and connect them with handoff tools.",
                    "detail": "Alex builds separate functional assistants, creates the handoff tools, and combines them inside a squad so a confirmed sales inquiry moves from the router to the sales assistant. [Alex Leischow — 8yIHmsMHMYc @ 00:11:23]",
                },
                {
                    "step": 3,
                    "title": "Connect the operational tools",
                    "action": "Configure booking availability and event creation against the actual calendar.",
                    "detail": "Venture Harbour obtains the Google Calendar ID, sets the timezone, enables the integration, and attaches the availability and booking tools to the workflow. [Venture Harbour — ZVSDm5siKr4 @ 00:03:17]",
                },
                {
                    "step": 4,
                    "title": "Exercise the unsuccessful routes as well as the main route",
                    "action": "Test corrections, withheld details, and interrupted conversations before reviewing outcomes.",
                    "detail": "Daniel deliberately corrects an incorrect phone number, refuses to provide contact information, and introduces an emergency; he then inspects summaries, outcomes, and sentiment. [Daniel | Tech & Data — PgrkNMNc_Cw @ 00:06:04]",
                },
            ],
        },
        {
            "id": "disagreements-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Vapi wins Venture Harbour's comparison on affordability and response speed, but Alejo Pijuan "
                    "reaches the opposite agency recommendation after live deployments. Venture Harbour prices a "
                    "standard two-thousand-minute monthly setup at about $180 for Vapi, around $80 less than "
                    "Retell, and says Vapi produced the lowest end-to-end latency in his recent platform test "
                    "[ZVSDm5siKr4 @ 00:13:44]. Pijuan reports recurring platform problems, including a three-to-four-second "
                    "delay at the beginning of live calls that persisted for weeks despite stripping back the "
                    "configuration. He favors Retell when clients require high reliability and says Retell held "
                    "a roughly two-hundred-to-three-hundred-millisecond latency advantage in his experience "
                    "[6Fal62hzEs8 @ 00:04:29]. Stephanie Nyarko does not select one universal winner. She recommends "
                    "ElevenLabs for the first straightforward receptionist, Retell for a small agency needing "
                    "flexibility without managing every provider integration, and Vapi for larger agencies building "
                    "custom tooling [J8C_262TFUU @ 00:13:40]. Her own voice tests also separate the orchestration "
                    "platform from the speech provider: Vapi with ElevenLabs sounded nearly identical to native "
                    "ElevenLabs, while Cartesia reduced latency with a voice-quality tradeoff. The disagreement "
                    "therefore includes measured responsiveness, deployment reliability, configuration burden, and "
                    "the agency's desired service model. Venture Harbour's favorable tutorial economics and Pijuan's "
                    "unfavorable operating experience are different reported results, not one shared verdict."
                ),
                (
                    "Even feature descriptions conflict. ToThePoint Guide calls ElevenLabs only a voice generator "
                    "and says Retell does not allow custom voice uploads [pMdWgl-3ihA @ 00:04:02]. Stephanie Nyarko "
                    "describes ElevenLabs Agents running calls natively, says her receptionist was working in less "
                    "than twenty minutes, and distinguishes that convenience from the limited routing customization "
                    "[J8C_262TFUU @ 00:06:37]. Voice AI Decoded explicitly demonstrates Retell's custom-voice "
                    "options: supply an ElevenLabs voice ID and API key, or upload audio to create an instant "
                    "voice through ElevenLabs [UiKoEHbio38 @ 00:02:26]. Bland produces another contrast between "
                    "a tested agent and a configured platform. CX Foundation's live demo cannot transfer the "
                    "caller, send a text, send an email, or switch into French, although the reviewer praises "
                    "its clarity and silence handling [ -j4XDojlGLc @ 00:06:21]. Those restrictions describe the "
                    "agent reached during that call. The same review finds it willing to discuss pricing but "
                    "unable to authorize matching a competitor's quote. Nyarko's broader selection method is "
                    "to choose the platform that supports the client's job without fighting its configuration. "
                    "Voice AI Decoded likewise recommends trying the competing platforms for the intended use "
                    "case. Their accounts do not support treating every reviewer's feature checklist or every "
                    "public demo's limitations as an identical description of all possible builds."
                ).replace("[ -j4XDojlGLc", "[-j4XDojlGLc"),
                (
                    "David Alex frames CloudTalk versus Vapi as a product-category choice rather than a voice "
                    "beauty contest. CloudTalk combines a business phone system with an AI agent product that "
                    "can also operate separately; he emphasizes shared routing, human escalation with context, "
                    "and a common dashboard. Vapi, in his description, means assembling and maintaining the "
                    "speech, model, voice, and carrier components [Ucjk1DJkxuE @ 00:04:06]. His price presentation "
                    "includes annual-billing phone-system plans at $25, $29, and $49 per user per month, followed "
                    "by AI add-ons. Tin Explains AI makes a related distinction within the specialist platforms: "
                    "Vapi offers more control and setup, while Retell is more immediately usable for contact-center "
                    "work and scheduling [I-30cbMO974 @ 00:00:56]. ToThePoint Guide offers another route for "
                    "nontechnical agencies, describing Synthflow's no-code workflows and white-labeling, with "
                    "quoted usage around fifteen to eighteen cents per minute; Play AI is presented as a budget "
                    "option at five cents per minute with a $20 monthly subscription [pMdWgl-3ihA @ 00:03:23]. "
                    "These alternatives trade customization against how much infrastructure the operator wants "
                    "to own. David prefers CloudTalk for businesses without dedicated engineers, Tin favors "
                    "Retell when rapid setup matters, and ToThePoint points to different products for no-code "
                    "agency packaging or a smaller usage price."
                ),
            ],
            "table": {
                "caption": "Conflicting results and alternative platform-selection rules",
                "headers": ["Decision or disputed point", "Side-by-side practitioner positions", "Expert Source"],
                "rows": [
                    [
                        "Choose between Vapi responsiveness and Retell deployment reliability",
                        "Venture Harbour reports Vapi winning his latency test; Pijuan reports persistent opening delays on deployed Vapi agents and prefers Retell reliability.",
                        "Venture Harbour ([ZVSDm5siKr4 @ 00:14:15]); Alejo Pijuan ([6Fal62hzEs8 @ 00:04:29])",
                    ],
                    [
                        "Distinguish native ElevenLabs agents from its speech-generation business",
                        "ToThePoint describes only voice generation; Nyarko describes native Agents and a working receptionist built in less than twenty minutes.",
                        "ToThePoint Guide ([pMdWgl-3ihA @ 00:04:02]); Stephanie Nyarko ([J8C_262TFUU @ 00:06:37])",
                    ],
                    [
                        "Compare conflicting accounts of custom voice support in Retell",
                        "ToThePoint says custom uploads are unavailable; Voice AI Decoded demonstrates ElevenLabs voice IDs and audio-based instant voice creation inside Retell.",
                        "ToThePoint Guide ([pMdWgl-3ihA @ 00:01:14]); Voice AI Decoded ([UiKoEHbio38 @ 00:02:26])",
                    ],
                    [
                        "Separate a public demonstration's limits from configured transfer functionality",
                        "CX Foundation's demo cannot transfer; Shoosh describes a dispatch destination and prompt instructions that trigger transfer for out-of-scope questions.",
                        "CX Foundation ([-j4XDojlGLc @ 00:05:14]); Anthony Shoosh ([S5UwzzP_Qec @ 00:08:44])",
                    ],
                    [
                        "Select an integrated phone operation or a configurable voice toolkit",
                        "David favors CloudTalk's shared human-and-AI operation for smaller businesses; Tin favors Vapi when a developer can manage custom logic and integrations.",
                        "David Alex ([Ucjk1DJkxuE @ 00:04:25]); Tin Explains AI ([I-30cbMO974 @ 00:03:26])",
                    ],
                    [
                        "Match no-code packaging and budget preferences to alternative platforms",
                        "ToThePoint positions Synthflow around no-code agency white-labeling and Play AI around lower pricing with fewer customization options.",
                        "ToThePoint Guide ([pMdWgl-3ihA @ 00:03:41]); ToThePoint Guide ([pMdWgl-3ihA @ 00:04:42])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "The most concrete integration trap is making the caller wait while every business automation "
                    "runs. Brendan Jowett says his agency made that mistake: CRM updates, confirmation emails, "
                    "and Slack notifications were triggered while the customer remained on the line. The agent "
                    "would announce a task, fall silent for five seconds, and invite a confused interruption "
                    "that could break the function call [Ky2Z6kGp1Vk @ 00:07:54]. His replacement is to collect "
                    "the information during the conversation and trigger those jobs through an end-of-call "
                    "webhook, where they are easier to track and rerun. Venture Harbour encounters a related "
                    "problem in the golf demo: latency becomes noticeable around calendar tools. He proposes "
                    "checking availability in the background while collecting other booking details, explicitly "
                    "describing this as reducing perceived latency rather than necessarily shortening the "
                    "underlying operation [ZVSDm5siKr4 @ 00:09:23]. Sonny Sangha encounters different failures "
                    "during generated setup: the receptionist does not retrieve the knowledge base correctly, "
                    "then a booking tool fails to fire correctly. Norm diagnoses and revises those parts before "
                    "retesting [JSYOZvtkAx4 @ 00:14:34]. These examples distinguish unnecessary live administration "
                    "from tools needed to answer the caller's immediate request. Jowett moves notifications "
                    "after the call; Venture Harbour keeps availability checking but changes its timing; Sonny "
                    "tests whether the knowledge and booking connections actually execute."
                ),
                (
                    "A fluent voice does not settle whether the requested action succeeded. CX Foundation's "
                    "Bland call starts with an odd vocal outburst, then handles interruptions, silence, and "
                    "pricing discussion well. When the caller asks for a person, however, the agent offers an "
                    "email address rather than a transfer; it also cannot send that address by text or email "
                    "[-j4XDojlGLc @ 00:05:00]. Daniel's emergency test makes the distinction even clearer. "
                    "Retell recognizes the roadside situation and activates the correct transfer path, but the "
                    "transfer fails; the fallback explains the situation and directs the caller to emergency "
                    "services. The monitoring result still records the interaction as unsuccessful with negative "
                    "sentiment [PgrkNMNc_Cw @ 00:07:31]. Brendan Jowett builds explicit escape routes for callers "
                    "asking for a real person or support and says the agent should transfer rather than argue "
                    "or attempt to deescalate that request [Ky2Z6kGp1Vk @ 00:07:18]. These are operational checks "
                    "on the destination and outcome, not just whether the agent said reassuring words. CX "
                    "Foundation praises the demo's clarity while naming the missing communication capabilities. "
                    "Daniel keeps the failed outcome visible despite the useful fallback. Jowett treats "
                    "frustration, poor connections, accents, hallucinations, and loops as reasons to build the "
                    "unhappy route before relying on the happy one."
                ),
                (
                    "Agency economics also include time spent building, troubleshooting, and moving clients. "
                    "Alejo Pijuan says advanced work can take one to two weeks in Retell versus one to two months "
                    "in Vapi in his experience, and warns that a powerful feature matters commercially only "
                    "when it creates or saves money for the client [6Fal62hzEs8 @ 00:07:46]. He also describes "
                    "unanswered Vapi support tickets lasting weeks, acknowledges unresolved Retell tickets too, "
                    "and cautions against switching platforms for a single flashy feature. Stephanie Nyarko "
                    "makes the same time-cost distinction at smaller volume: her comparison uses fifty "
                    "three-minute calls per month, and she considers a modest platform-price difference less "
                    "important than the operator's time and ability to do the job [J8C_262TFUU @ 00:14:33]. "
                    "Brendan Jowett supplies the scope correction. Clients sometimes use booking systems with "
                    "no API or too few endpoints; texting a booking form can avoid weeks spent forcing a "
                    "fragile telephone booking integration [Ky2Z6kGp1Vk @ 00:05:15]. He also reports no negative "
                    "impact from upfront AI disclosure, recommends a static first message, and prefers humans "
                    "for relationship-heavy sales and businesses receiving only a handful of calls daily. "
                    "His agency's operating lesson is not to maximize automated features: start with a useful "
                    "first version, retain human handling where it works better, and expand after learning how "
                    "callers actually use the system."
                ),
            ],
            "table": {
                "caption": "Reported breakdowns and the checks practitioners use to expose or avoid them",
                "headers": ["Failure or economic trap", "Reported experience and response", "Expert Source"],
                "rows": [
                    [
                        "Running every administrative automation while the caller is still waiting",
                        "Jowett reports five-second silences and interruptions breaking tool calls; his team moves emails, CRM updates, and notifications into post-call workflows.",
                        "Brendan Jowett ([Ky2Z6kGp1Vk @ 00:07:54])",
                    ],
                    [
                        "Letting calendar tool execution create obvious conversational dead air",
                        "Venture Harbour notices latency in the golf demo and proposes running availability checks while collecting the remaining booking information.",
                        "Venture Harbour ([ZVSDm5siKr4 @ 00:09:23])",
                    ],
                    [
                        "Assuming a generated receptionist correctly queries its attached knowledge",
                        "Sonny observes missed knowledge retrieval and a failing booking tool; Norm changes the configuration and runs the conversation tests again.",
                        "Sonny Sangha ([JSYOZvtkAx4 @ 00:14:34])",
                    ],
                    [
                        "Counting an attempted emergency transfer as a successful outcome",
                        "Daniel's transfer fails even though the emergency branch activates; Retell records an unsuccessful interaction and negative sentiment while the fallback continues.",
                        "Daniel | Tech & Data ([PgrkNMNc_Cw @ 00:07:31])",
                    ],
                    [
                        "Selling a platform feature without accounting for deployment troubleshooting",
                        "Pijuan reports opening delays lasting weeks and recurring platform issues that damaged client relationships despite repeated attempts to simplify the configuration.",
                        "Alejo Pijuan ([6Fal62hzEs8 @ 00:04:29])",
                    ],
                    [
                        "Forcing phone bookings through software with inadequate integration endpoints",
                        "Jowett describes client booking systems without useful APIs and suggests sending an online booking form instead of spending weeks building around the limitation.",
                        "Brendan Jowett ([Ky2Z6kGp1Vk @ 00:05:15])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks drawn from actual build and deployment problems",
                "body": "Use the failed routes, delayed tools, and support burden to evaluate the working service.",
                "items": [
                    "Test the human-transfer request and its failure path, not just the spoken promise to connect someone; Daniel's emergency transfer failed and was marked unsuccessful despite the fallback response. [Daniel | Tech & Data — PgrkNMNc_Cw @ 00:07:31]",
                    "Move CRM updates, confirmation emails, and team notifications after the call when they are not needed to continue the conversation; Jowett reports live execution causing silence and broken function calls. [Brendan Jowett — Ky2Z6kGp1Vk @ 00:07:54]",
                    "Use a static opening for the AI introduction and check whether it was spoken; Jowett reports no negative impact from upfront disclosure and recommends QA alerts for the opening. [Brendan Jowett — Ky2Z6kGp1Vk @ 00:02:03]",
                    "Include development time and migration learning in the platform decision; Pijuan warns that switching for a new feature means rebuilding platform knowledge and encountering fresh troubleshooting work. [Alejo Pijuan — 6Fal62hzEs8 @ 00:14:56]",
                ],
            },
        },
    ],
    "pull_quote": (
        "\"An agent with one clear goal will always outperform an agent trying to juggle five different tasks "
        "all at the same time.\" — Brendan Jowett (Ky2Z6kGp1Vk @ 00:06:38)."
    ),
    "diagram_id": "diag-04",
    "action_checklist": [
        "Collect existing call recordings, scripts, and business resources so the agent can replicate an understood service process. [Brendan Jowett — Ky2Z6kGp1Vk @ 00:11:13]",
        "Map the form fields into the callback opening and let the router confirm whether the lead needs sales, service, billing, or another configured route. [Alex Leischow — 8yIHmsMHMYc @ 00:05:22]",
        "Add globally accessible insurance paths for immediate emergency direction, live-agent requests, callbacks, and existing claims. [Bland — W1Y3bHct_e0 @ 00:00:42]",
        "Test a requested booking against an already occupied calendar slot, then confirm that the alternative-slot branch still collects the booking details. [Venture Harbour — ZVSDm5siKr4 @ 00:08:19]",
        "Compare voice-provider choices with the same receptionist prompt; Nyarko tests ElevenLabs, Cartesia, and Google through Vapi and reports different quality-latency tradeoffs. [Stephanie Nyarko — J8C_262TFUU @ 00:10:58]",
        "Run persona simulations with explicit success criteria after changing the agent, checking for degraded behavior rather than assuming the revision improved it. [Alejo Pijuan — 6Fal62hzEs8 @ 00:09:38]",
    ],
    "statutory_citations": [
        {
            "title": "Alex Leischow — How to Build an AI Voice Agent That Calls Every Lead in 60 Seconds (VAPI Tutorial) [00:11:23]",
            "url": "https://www.youtube.com/watch?v=8yIHmsMHMYc&t=683s",
            "relevance": "Primary practitioner testimony on specialized assistants, handoff tools, and squads for multi-route lead callbacks.",
        },
        {
            "title": "Bland — How to automate FNOL insurance calls using AI voice agents [00:00:42]",
            "url": "https://www.youtube.com/watch?v=W1Y3bHct_e0&t=42s",
            "relevance": "Primary practitioner testimony on global escape routes in insurance first-notice-of-loss intake.",
        },
        {
            "title": "Alejo Pijuan — The Best Platform for your Voice AI Agency: Retell vs Vapi [00:04:29]",
            "url": "https://www.youtube.com/watch?v=6Fal62hzEs8&t=269s",
            "relevance": "Primary practitioner testimony on persistent deployment latency and its effect on client relationships.",
        },
        {
            "title": "Brendan Jowett — The Darkside of AI Voice Agents (The Truth) [00:07:54]",
            "url": "https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=474s",
            "relevance": "Primary practitioner testimony on moving administrative automations out of the live call.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "S5UwzzP_Qec",
            "title": "Bland AI Basics: Everything You Need to Start Building Voice Agents",
            "channel": "Anthony Shoosh",
            "author": "Anthony Shoosh",
            "text": "You're going to want to have a call flow section, a background section, and an example dialogue section.",
            "tip": "You're going to want to have a call flow section, a background section, and an example dialogue section.",
            "timestamp": 320,
            "timestamp_seconds": 320,
            "timestamp_label": "[00:05:20]",
            "url": "https://www.youtube.com/watch?v=S5UwzzP_Qec&t=320s",
            "markdown": "[00:05:20](https://www.youtube.com/watch?v=S5UwzzP_Qec&t=320s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q8.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "-j4XDojlGLc",
            "title": "We Tested Bland AI’s Voice Agent. Here’s What Happened",
            "channel": "CX Foundation",
            "author": "CX Foundation",
            "text": "It did not yet have the capability to send me a text message or an email directly from the phone conversation, nor did it have the ability to transfer me directly to a live agent.",
            "tip": "It did not yet have the capability to send me a text message or an email directly from the phone conversation, nor did it have the ability to transfer me directly to a live agent.",
            "timestamp": 397,
            "timestamp_seconds": 397,
            "timestamp_label": "[00:06:37]",
            "url": "https://www.youtube.com/watch?v=-j4XDojlGLc&t=397s",
            "markdown": "[00:06:37](https://www.youtube.com/watch?v=-j4XDojlGLc&t=397s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on the tested Bland demo's missing communication actions.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PgrkNMNc_Cw",
            "title": "Retell AI Review (2026): Create AI Voice Agents in Under 10 Minutes",
            "channel": "Daniel | Tech & Data",
            "author": "Daniel | Tech & Data",
            "text": "The completed flow appeared as 9 connected nodes.",
            "tip": "The completed flow appeared as 9 connected nodes.",
            "timestamp": 263,
            "timestamp_seconds": 263,
            "timestamp_label": "[00:04:23]",
            "url": "https://www.youtube.com/watch?v=PgrkNMNc_Cw&t=263s",
            "markdown": "[00:04:23](https://www.youtube.com/watch?v=PgrkNMNc_Cw&t=263s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony on the Conductor-generated auto-repair workflow.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "UiKoEHbio38",
            "title": "Retell AI vs Bland AI (Don't choose WRONG!)",
            "channel": "Voice AI Decoded",
            "author": "Voice AI Decoded",
            "text": "When I've done standardized latency testing across different tools, I believe with Retell I was getting 714 milliseconds of end-to-end latency.",
            "tip": "When I've done standardized latency testing across different tools, I believe with Retell I was getting 714 milliseconds of end-to-end latency.",
            "timestamp": 457,
            "timestamp_seconds": 457,
            "timestamp_label": "[00:07:37]",
            "url": "https://www.youtube.com/watch?v=UiKoEHbio38&t=457s",
            "markdown": "[00:07:37](https://www.youtube.com/watch?v=UiKoEHbio38&t=457s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on the reported Retell latency measurement.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8yIHmsMHMYc",
            "title": "How to Build an AI Voice Agent That Calls Every Lead in 60 Seconds (VAPI Tutorial)",
            "channel": "Alex Leischow",
            "author": "Alex Leischow",
            "text": "We got a call within 10 seconds, basically confirming what we needed and then letting me know that someone on the sales team is going to follow up with me.",
            "tip": "We got a call within 10 seconds, basically confirming what we needed and then letting me know that someone on the sales team is going to follow up with me.",
            "timestamp": 901,
            "timestamp_seconds": 901,
            "timestamp_label": "[00:15:01]",
            "url": "https://www.youtube.com/watch?v=8yIHmsMHMYc&t=901s",
            "markdown": "[00:15:01](https://www.youtube.com/watch?v=8yIHmsMHMYc&t=901s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on the plumbing lead callback demonstration.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "W1Y3bHct_e0",
            "title": "How to automate FNOL insurance calls using AI voice agents",
            "channel": "Bland",
            "author": "Bland",
            "text": "We've got some global nodes set up here. This basically is just like an escape hatch for the agent.",
            "tip": "We've got some global nodes set up here. This basically is just like an escape hatch for the agent.",
            "timestamp": 42,
            "timestamp_seconds": 42,
            "timestamp_label": "[00:00:42]",
            "url": "https://www.youtube.com/watch?v=W1Y3bHct_e0&t=42s",
            "markdown": "[00:00:42](https://www.youtube.com/watch?v=W1Y3bHct_e0&t=42s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on globally accessible FNOL escalation paths.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ZVSDm5siKr4",
            "title": "Build a Voice Agent in 15 Minutes Using VAPI (Easiest Tutorial)",
            "channel": "Venture Harbour",
            "author": "Venture Harbour",
            "text": "Vapi is coming out at around about $180 per month.",
            "tip": "Vapi is coming out at around about $180 per month.",
            "timestamp": 824,
            "timestamp_seconds": 824,
            "timestamp_label": "[00:13:44]",
            "url": "https://www.youtube.com/watch?v=ZVSDm5siKr4&t=824s",
            "markdown": "[00:13:44](https://www.youtube.com/watch?v=ZVSDm5siKr4&t=824s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony for the stated 2,000-minute monthly comparison scenario.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "pMdWgl-3ihA",
            "title": "Best AI Voice Agent 2025: Retell vs Vapi vs Bland vs Synthflow vs ElevenLabs vs Play AI vs Air AI vs",
            "channel": "ToThePoint Guide",
            "author": "ToThePoint Guide",
            "text": "It offers no-code workflows, deep integration hooks and even full white-labeling for agencies.",
            "tip": "It offers no-code workflows, deep integration hooks and even full white-labeling for agencies.",
            "timestamp": 221,
            "timestamp_seconds": 221,
            "timestamp_label": "[00:03:41]",
            "url": "https://www.youtube.com/watch?v=pMdWgl-3ihA&t=221s",
            "markdown": "[00:03:41](https://www.youtube.com/watch?v=pMdWgl-3ihA&t=221s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony describing Synthflow's agency-oriented positioning.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Ky2Z6kGp1Vk",
            "title": "The Darkside of AI Voice Agents (The Truth)",
            "channel": "Brendan Jowett",
            "author": "Brendan Jowett",
            "text": "A major mistake that we made is trying to get every single automation to run during the call.",
            "tip": "A major mistake that we made is trying to get every single automation to run during the call.",
            "timestamp": 474,
            "timestamp_seconds": 474,
            "timestamp_label": "[00:07:54]",
            "url": "https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=474s",
            "markdown": "[00:07:54](https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=474s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony on an agency's live-call automation mistake.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "J8C_262TFUU",
            "title": "ElevenLabs vs Vapi vs Retell AI: I Built the Same AI Receptionist on All 3",
            "channel": "Stephanie Nyarko",
            "author": "Stephanie Nyarko",
            "text": "I tested it with ElevenLabs, and I got nearly identical call quality to the native ElevenLabs agents platform.",
            "tip": "I tested it with ElevenLabs, and I got nearly identical call quality to the native ElevenLabs agents platform.",
            "timestamp": 673,
            "timestamp_seconds": 673,
            "timestamp_label": "[00:11:13]",
            "url": "https://www.youtube.com/watch?v=J8C_262TFUU&t=673s",
            "markdown": "[00:11:13](https://www.youtube.com/watch?v=J8C_262TFUU&t=673s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony comparing Vapi with ElevenLabs speech against native ElevenLabs Agents.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "6Fal62hzEs8",
            "title": "The Best Platform for your Voice AI Agency: Retell vs Vapi",
            "channel": "Alejo Pijuan",
            "author": "Alejo Pijuan",
            "text": "When we experienced a 3 to 4 second lag at the beginning of every single call on live voice agents for weeks without resolution, it destroyed our credibility.",
            "tip": "When we experienced a 3 to 4 second lag at the beginning of every single call on live voice agents for weeks without resolution, it destroyed our credibility.",
            "timestamp": 269,
            "timestamp_seconds": 269,
            "timestamp_label": "[00:04:29]",
            "url": "https://www.youtube.com/watch?v=6Fal62hzEs8&t=269s",
            "markdown": "[00:04:29](https://www.youtube.com/watch?v=6Fal62hzEs8&t=269s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on a reported Vapi deployment reliability problem.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "JSYOZvtkAx4",
            "title": "I Built an AI Voice Agent That Actually Works (AI Receptionist Full Beginner Tutorial)",
            "channel": "Sonny Sangha",
            "author": "Sonny Sangha",
            "text": "It found that it was actually hallucinating, so it needs to fix that, so it goes to the actual knowledge base instead of guessing.",
            "tip": "It found that it was actually hallucinating, so it needs to fix that, so it goes to the actual knowledge base instead of guessing.",
            "timestamp": 650,
            "timestamp_seconds": 650,
            "timestamp_label": "[00:10:50]",
            "url": "https://www.youtube.com/watch?v=JSYOZvtkAx4&t=650s",
            "markdown": "[00:10:50](https://www.youtube.com/watch?v=JSYOZvtkAx4&t=650s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on Norm testing and correcting a generated receptionist.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Ucjk1DJkxuE",
            "title": "CloudTalk vs Vapi: Which AI Voice Agent Actually Handles Calls Better in 2026?",
            "channel": "David Alex",
            "author": "David Alex",
            "text": "AI voice agents are an add-on on top of any plan, starting at $99 a month for 200 minutes of AI call time.",
            "tip": "AI voice agents are an add-on on top of any plan, starting at $99 a month for 200 minutes of AI call time.",
            "timestamp": 522,
            "timestamp_seconds": 522,
            "timestamp_label": "[00:08:42]",
            "url": "https://www.youtube.com/watch?v=Ucjk1DJkxuE&t=522s",
            "markdown": "[00:08:42](https://www.youtube.com/watch?v=Ucjk1DJkxuE&t=522s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on CloudTalk's quoted AI add-on pricing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "I-30cbMO974",
            "title": "Vapi Vs Retell Comparison - Which One Is A Better Ai Voice Solution?",
            "channel": "Tin Explains AI",
            "author": "Tin Explains AI",
            "text": "Vapi has more power but more setup. Retell has less setup but more of what just works.",
            "tip": "Vapi has more power but more setup. Retell has less setup but more of what just works.",
            "timestamp": 306,
            "timestamp_seconds": 306,
            "timestamp_label": "[00:05:06]",
            "url": "https://www.youtube.com/watch?v=I-30cbMO974&t=306s",
            "markdown": "[00:05:06](https://www.youtube.com/watch?v=I-30cbMO974&t=306s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony summarizing the setup-versus-control platform choice.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8yIHmsMHMYc",
            "title": "How to Build an AI Voice Agent That Calls Every Lead in 60 Seconds (VAPI Tutorial)",
            "channel": "Alex Leischow",
            "author": "Alex Leischow",
            "text": "The whole key is to build specific functional agents or assistants and then connect them via handoff tools inside a larger organism called a squad.",
            "tip": "The whole key is to build specific functional agents or assistants and then connect them via handoff tools inside a larger organism called a squad.",
            "timestamp": 683,
            "timestamp_seconds": 683,
            "timestamp_label": "[00:11:23]",
            "url": "https://www.youtube.com/watch?v=8yIHmsMHMYc&t=683s",
            "markdown": "[00:11:23](https://www.youtube.com/watch?v=8yIHmsMHMYc&t=683s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Near-verbatim practitioner testimony on the specialist-assistant architecture.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Ky2Z6kGp1Vk",
            "title": "The Darkside of AI Voice Agents (The Truth)",
            "channel": "Brendan Jowett",
            "author": "Brendan Jowett",
            "text": "We've honestly seen no negative impact from upfront disclosure. If anything, the results have improved.",
            "tip": "We've honestly seen no negative impact from upfront disclosure. If anything, the results have improved.",
            "timestamp": 148,
            "timestamp_seconds": 148,
            "timestamp_label": "[00:02:28]",
            "url": "https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=148s",
            "markdown": "[00:02:28](https://www.youtube.com/watch?v=Ky2Z6kGp1Vk&t=148s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony on the agency's experience with upfront AI disclosure.",
        },
    ],
}
