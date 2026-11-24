from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "set-privacy-contract-and-acceptance-boundaries",
    "question_prompt": "Which data-handling, requirements, contractual, and cost risks must be addressed before an AI client project is treated as complete?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "Set Privacy, Contract, and Acceptance Boundaries",
    "subtitle": "Data-retention policies, OpenAI privacy and training settings, local PII redaction, AWS guardrails, frozen requirements, scope creep, indemnity clauses, and uncapped API costs.",
    "layout_template": "action_worksheet_summary",
    "reading_time_minutes": 15,
    "executive_summary": (
        "The operators converge on explicit boundaries: define the shipped outcome, make requirements observable, "
        "separate extra work from the original fee, and control sensitive data before sending it onward. "
        "Augusto Digital reports shipping a human-reviewed quoting workflow in six weeks; neomanex reports "
        "36 requirements passing after five testing rounds. Bryan Taylor's customer incurred $30,000 in "
        "first-month costs after giving away video storage and usage. Privacy approaches diverge: Micah "
        "Johnson favors the API for sensitive business work, Matt Williams demonstrates local Ollama models, "
        "and Protecto separates training, retention, and residency rather than treating any one promise as "
        "complete protection. ProtaSystem presses for priced change orders and an aggregate liability cap. "
        "SecureCyberGates makes retention and deletion verification explicit, while Cognitive Capital emphasizes "
        "testing redaction against actual business data."
    ),
    "key_metrics": [
        {
            "label": "First-month video-service cost",
            "metric": "First-month video-service cost",
            "value": "$30,000",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Bryan Taylor reports that a customer giving away video space incurred this cost in the "
                "first month; uploads, viewing, storage, and bandwidth drove usage beyond expectations."
            ),
            "source": "Bryan Taylor ([yLxvwa45vR8 @ 00:03:17])",
        },
        {
            "label": "Frozen requirements passing",
            "metric": "Frozen requirements passing",
            "value": "36 out of 36 in round five",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "neomanex reports this result after repeated fixes and testing. A subsequent done-when "
                "review still found four gaps, including two requiring the owner's decision."
            ),
            "source": "neomanex ([wOkT9r5iVME @ 00:07:01])",
        },
        {
            "label": "Human-reviewed quoting launch",
            "metric": "Human-reviewed quoting launch",
            "value": "6 weeks",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Augusto Digital says its quoting team hit the six-week date by moving live pricing "
                "lookups and other additions to version two."
            ),
            "source": "Augusto Digital ([VzBpfD_Dcq8 @ 00:08:05])",
        },
        {
            "label": "Example deletion review interval",
            "metric": "Example deletion review interval",
            "value": "35 days",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "SecureCyberGates describes an example backup and snapshot deletion process followed by "
                "ticket review and support verification; the speaker says the number can be defined "
                "in the project contract."
            ),
            "source": "SecureCyberGates ([TcAbiyEqBFM @ 00:04:39])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Start with a finish line the client can recognize, not a growing collection of AI features. "
                    "Augusto Digital calls its anchor 'one outcome, one owner, one date.' Its quoting engagement "
                    "was not a general sales platform: the mandate was a draft quote for every incoming request, "
                    "reviewed by a human, live in six weeks. Live pricing and historical customer information "
                    "went onto the version-two list instead of moving the launch. Bryan Taylor starts at the "
                    "same business end: outline the goal, work backward to the functions required, and keep "
                    "returning to that mission while building. The warning is concrete: tangents leave more "
                    "software to maintain than the original task required. AI Automation Society adds the client "
                    "relationship behind that discipline. Its speakers describe pushing customers toward basic "
                    "data movement and synchronization without AI when those automations offered the quickest "
                    "return. They also describe customers who insisted on their original document and threatened "
                    "to find another vendor. Their response after repeated disappointing engagements was more "
                    "honest expectation management, not endless extra work to make the customer happy. The "
                    "shared operating position is narrow delivery with an explicit business purpose, rather "
                    "than accepting every request because it sounds technically possible. "
                    "[VzBpfD_Dcq8 @ 00:07:01] [yLxvwa45vR8 @ 00:01:33] [3XIdI6vcGz0 @ 00:01:54]"
                ),
                (
                    "Treat training permission, retention, and processing location as separate conversations. "
                    "Protecto names three controls: no training determines whether content trains models; zero "
                    "data retention concerns covered content after processing; residency concerns where storage "
                    "or processing happens. None substitutes for the others, and provider commitments vary by "
                    "service, endpoint, and feature. Micah Johnson makes the product distinction operational: "
                    "consumer ChatGPT training can be switched off under settings and data controls, while the "
                    "API does not use submitted data for training by default under the agreement Johnson "
                    "describes. Johnson also says deleted conversations normally enter a thirty-day removal "
                    "window with legal and safety exceptions, and business administrators can access conversation "
                    "content. Cloud in places another boundary around the customer's own implementation. AWS "
                    "secures the cloud infrastructure, while the customer configures data access, IAM roles, "
                    "guardrails, networking, encryption keys, and MFA. These speakers do not describe a single "
                    "privacy switch that finishes the job. Protecto explicitly includes the application's logs, "
                    "retrieval pipeline, tools, and databases in the problem, even when a model is stateless. "
                    "Its preferred first move is data minimization: replace sensitive values before the model "
                    "call and restore them only for authorized recipients. The banking example removes real "
                    "names and account numbers when analysis does not need them. "
                    "[e8kcLoVVX_A @ 00:00:17] [lBhO8Q-MxYI @ 00:00:33] [ZE-vxHSGB7w @ 00:12:13]"
                ),
                (
                    "Make the commercial promise as explicit as the technical promise. ProtaSystem contrasts "
                    "a vague 'website redesign' with six pages and two revision rounds, then describes how "
                    "informal messages and fear of a poor rating turn small favors into unpaid delivery. Its "
                    "mechanism is a work pause when the boundary is crossed, followed by a quoted, documented, "
                    "priced addition. GTIA's Mike Sencka describes the same margin leak from the project "
                    "management side: engineers work beyond what the customer is paying for, and the extra "
                    "work goes untracked. Sencka wants overages identified while the job is active, when managers "
                    "can still discuss the expanded scope and negotiate with the customer. ProtaSystem also "
                    "targets uncapped indemnification and proposes an aggregate liability cap tied to the "
                    "amount actually paid to the contractor. Innovative Compass Consulting contributes a "
                    "different boundary around AI deliverables: it describes output ownership under OpenAI's "
                    "terms, but says another user may receive similar or identical output. It also places "
                    "fact-checking responsibility on the user before publication or a major decision. Those "
                    "are distinct issues in the speakers' accounts: what the client bought, what additional "
                    "work costs, what liability the agreement assigns, and what the generated output actually "
                    "establishes. Neither ownership language nor a successful generation removes the need to "
                    "review what is being delivered. "
                    "[6l0a6If9Oyk @ 00:01:46] [TtU19Z-ASZk @ 00:04:21] [DIfo9jAMZYY @ 00:02:52]"
                ),
            ],
            "table": {
                "caption": "Baseline boundaries the speakers put around delivery, data, and payment.",
                "headers": ["Boundary", "Practitioner mechanics", "Expert Source"],
                "rows": [
                    [
                        "Define the first shipped outcome before expanding the feature list.",
                        "Augusto Digital fixes one outcome, one owner, and one date, then places additional requests on a version-two list.",
                        "Augusto Digital ([VzBpfD_Dcq8 @ 00:07:01])",
                    ],
                    [
                        "Keep the business mission visible throughout the actual software build.",
                        "Taylor says to outline the goal and required functions, then avoid tangents that increase maintenance and technical debt.",
                        "Bryan Taylor ([yLxvwa45vR8 @ 00:01:33])",
                    ],
                    [
                        "Distinguish training permission from retention duration and processing location.",
                        "Protecto separates the three controls and says commitments must be checked against the service, endpoint, and feature actually used.",
                        "Protecto ([e8kcLoVVX_A @ 00:00:17])",
                    ],
                    [
                        "Separate cloud infrastructure protection from customer-controlled access and configuration.",
                        "Cloud in assigns IAM roles, user access, guardrails, network configuration, key handling, and MFA to the customer's responsibilities.",
                        "Cloud in ([ZE-vxHSGB7w @ 00:12:13])",
                    ],
                    [
                        "Replace vague deliverables with a bounded quantity and revision allowance.",
                        "ProtaSystem uses six pages with two revision rounds as the concrete alternative to an open-ended website redesign promise.",
                        "ProtaSystem ([6l0a6If9Oyk @ 00:01:46])",
                    ],
                    [
                        "Keep output ownership separate from uniqueness and factual review.",
                        "Innovative Compass Consulting says similar prompts can produce similar or identical outputs and users must check accuracy before consequential use.",
                        "Innovative Compass Consulting ([DIfo9jAMZYY @ 00:02:52])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics-tools-numbers",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "neomanex turns a broad initiative into requirements that can fail in public view. Its "
                    "runner initiative had sixteen requirements; the first plan took thirteen and split them "
                    "into thirty-six. Each line specifies who acts, what they can do, and how someone proves "
                    "it from outside the code. One broad promise about a disappearing runner becomes separate "
                    "checks for a lost runner, a preempted machine, duplicate execution, and retry behavior. "
                    "The run must end within three minutes with the appropriate reason; retry means exactly "
                    "one additional attempt, not an unbounded loop. The owner reads every line, makes the "
                    "decisions, and freezes the requirements. Beside them sit a won't-do list and a done-when "
                    "list with one box per requirement. Every design component must point back to a requirement "
                    "or be cut. Test journeys quote their requirements word for word. Augusto Digital handles "
                    "a less deterministic acceptance problem by defining the human workflow rather than "
                    "demanding perfect AI output. Its example is a draft with an eighty-five-percent confidence "
                    "score that an operator can review and approve in under two minutes. That example is "
                    "an acceptance definition, not a reported accuracy result. The measurable workflow and "
                    "hard date are agreed with the project owner before coding begins. "
                    "[wOkT9r5iVME @ 00:01:20] [wOkT9r5iVME @ 00:04:42] [VzBpfD_Dcq8 @ 00:11:30]"
                ),
                (
                    "Cognitive Capital's local-redaction pilot starts with one stream, such as support tickets. "
                    "Run the filter, inspect before-and-after differences, choose conditional or absolute "
                    "masking, and put the filter before the vector database. Its wider placement is ingestion, "
                    "logging, and retrieval: mask before long-term storage and embeddings, scrub prompts and "
                    "responses before observability records are written, and filter retrieved passages before "
                    "sending them back to an LLM. The safe-ingest example stores masked text in the vector "
                    "database while keeping an encrypted reference pointer to the original in a tightly "
                    "restricted traditional database. Protecto extends the same protection-layer pattern "
                    "through agent workflows, explicitly including database queries and tool results rather "
                    "than only the first prompt. Cloud in supplies an AWS implementation vocabulary: S3, "
                    "Bedrock knowledge bases, Lambda orchestration, Cognito, IAM, KMS, CloudWatch, and CloudTrail. "
                    "Its emphasis is scoped access to particular models and sources, logs showing who accessed "
                    "what, and evidence of configuration and testing. Cloud in also recommends short log "
                    "retention, S3 lifecycle rules, private access, and isolation between environments. These "
                    "are the speakers' concrete placements and controls: redaction before durable copies, "
                    "another check at retrieval, restricted access to originals, and activity records the "
                    "operations team can inspect when something goes wrong. "
                    "[j2Bqq0VTv0o @ 00:05:27] [e8kcLoVVX_A @ 00:01:38] [ZE-vxHSGB7w @ 00:17:03]"
                ),
                (
                    "SecureCyberGates starts retention with the project and the data category, not a universal "
                    "number. The walkthrough describes clients choosing archive periods and repeatedly says "
                    "actual periods depend on the project contract and applicable requirements. Its examples "
                    "include two years online plus five additional archival years, but a later category "
                    "list uses different periods for logs, archives, employee records, and communications. "
                    "The deletion procedure is more specific: raise a ticket, run the shredding work, allow "
                    "the example backup cycle to roll through thirty-five days, delete manual snapshots, "
                    "and return the ticket to support for verification. The speaker explicitly allows the "
                    "contract to define that interval. Bryan Taylor puts comparable visibility around cost: "
                    "build reporting and an admin tool early, rather than discovering consumption after a "
                    "customer has used a free service heavily. Taylor names SendGrid and Twilio while warning "
                    "against uncontrolled automated outreach and unexpected usage charges. ProtaSystem puts "
                    "the same specificity into commercial paperwork: quote extra work before continuing, "
                    "and negotiate a liability cap based on the amount paid. It also describes Claus Radar "
                    "as scanning for net-ninety terms, early IP handovers, and uncapped liabilities, then "
                    "drafting plain-English counterproposals. Those are the promoted tool's described "
                    "functions, not a demonstrated contract-review result. "
                    "[TcAbiyEqBFM @ 00:03:55] [yLxvwa45vR8 @ 00:03:04] [6l0a6If9Oyk @ 00:04:59]"
                ),
            ],
            "table": {
                "caption": "Specific execution patterns, tools, and numbers without turning examples into universal defaults.",
                "headers": ["Execution target", "Exact practitioner method", "Expert Source"],
                "rows": [
                    [
                        "Translate a broad runner promise into separately observable acceptance checks.",
                        "neomanex specifies a three-minute ending, a visible reason, one recorded attempt, and exactly one retry when retry is enabled.",
                        "neomanex ([wOkT9r5iVME @ 00:01:42])",
                    ],
                    [
                        "Freeze the requirement list before downstream design and test work.",
                        "The owner controls changes; the won't-do list excludes migration during a run and more than one retry for that plan.",
                        "neomanex ([wOkT9r5iVME @ 00:04:04])",
                    ],
                    [
                        "Try local masking on one selected stream before wider deployment.",
                        "Cognitive Capital selects support tickets, reviews masking differences, chooses the masking policy, and inserts the filter before the vector database.",
                        "Cognitive Capital ([j2Bqq0VTv0o @ 00:05:27])",
                    ],
                    [
                        "Retain an operational trail showing model access and user activity.",
                        "Cloud in calls for CloudWatch alarms and CloudTrail so the team can trace who supplied data and how a model was used.",
                        "Cloud in ([ZE-vxHSGB7w @ 00:26:15])",
                    ],
                    [
                        "Keep deletion work open until backup handling and verification finish.",
                        "SecureCyberGates describes a thirty-five-day example followed by review and support verification, with the interval defined through the project contract.",
                        "SecureCyberGates ([TcAbiyEqBFM @ 00:04:39])",
                    ],
                    [
                        "Quote expanded work separately before continuing beyond the agreed boundary.",
                        "ProtaSystem pauses work, documents the new request, and prices the addition instead of allowing continuous unpaid revisions under the original fee.",
                        "ProtaSystem ([6l0a6If9Oyk @ 00:02:38])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small wording and placement choices that change the result",
                "body": "Use the speakers' concrete refinements rather than broad promises.",
                "items": [
                    (
                        "Replace 'once more' with 'exactly one more attempt' where that is the intended retry "
                        "behavior. neomanex caught a design that otherwise could retry forever. "
                        "[neomanex — wOkT9r5iVME @ 00:05:45]"
                    ),
                    (
                        "Put the requester's name beside each not-yet idea. Augusto Digital uses that "
                        "visible credit to acknowledge the idea without moving it into the current build. "
                        "[Augusto Digital — VzBpfD_Dcq8 @ 00:10:27]"
                    ),
                    (
                        "Scrub observability records as well as incoming documents. Cognitive Capital "
                        "specifically targets raw prompts and responses before they become permanent logs. "
                        "[Cognitive Capital — j2Bqq0VTv0o @ 00:03:38]"
                    ),
                    (
                        "When a sensitive local-model conversation needs a cloud model, start a new chat. "
                        "Williams warns that switching the existing conversation also sends its data onward. "
                        "[Matt Williams — KeqxPxb_sak @ 00:03:57]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Fix the first outcome and its owner",
                    "action": "Write the measurable workflow and launch date; open the not-yet list.",
                    "detail": (
                        "Augusto Digital defines one outcome, one owner, and one date, then records "
                        "out-of-scope requests visibly with their requesters' names. "
                        "[Augusto Digital — VzBpfD_Dcq8 @ 00:07:01] "
                        "[Augusto Digital — VzBpfD_Dcq8 @ 00:10:27]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Freeze observable requirements",
                    "action": "Write who, what, and externally visible proof for each requirement.",
                    "detail": (
                        "Follow neomanex's frozen list, explicit exclusions, and one done-when box per "
                        "requirement; have test journeys quote the requirements they check. "
                        "[neomanex — wOkT9r5iVME @ 00:02:25] "
                        "[neomanex — wOkT9r5iVME @ 00:06:03]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Separate provider promises and minimize inputs",
                    "action": "Check training, retention, residency, and the sensitive fields actually needed.",
                    "detail": (
                        "Protecto checks the actual service, endpoint, and feature, including retention "
                        "exceptions and abuse monitoring, then tokenizes sensitive values before model calls. "
                        "[Protecto — e8kcLoVVX_A @ 00:00:50] "
                        "[Protecto — e8kcLoVVX_A @ 00:01:54]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Test shipped behavior and verify deletion work",
                    "action": "Run requirement journeys and finish the deletion ticket's verification.",
                    "detail": (
                        "neomanex runs tests on the shipped system and follows with a separate done-when "
                        "review. SecureCyberGates sends completed shredding work back to support to verify "
                        "deletion after the example backup interval. "
                        "[neomanex — wOkT9r5iVME @ 00:07:21] "
                        "[SecureCyberGates — TcAbiyEqBFM @ 00:05:06]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-alternative-playbooks",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "The clearest architectural split is where sensitive work should run. Micah Johnson "
                    "recommends the API rather than consumer ChatGPT for proprietary business data, pointing "
                    "to the different training default. Matt Williams instead demonstrates replacing the "
                    "model behind the ChatGPT desktop interface with local Ollama models. In the Mac setup, "
                    "Williams enables the ChatGPT integration in Ollama, restarts ChatGPT, adds local models, "
                    "and restarts again so they appear in the picker. The practical proof is disconnecting "
                    "the network and continuing to chat. Williams keeps cloud models for public research "
                    "and low-stakes brainstorming, while recommending local inference for material whose "
                    "disclosure would hurt. Serop describes a third route observed among European businesses: "
                    "use models through an existing cloud relationship with European hosting, rather than "
                    "contracting directly with the model company. Serop also discusses privately hosted "
                    "open-source models, but stresses investment cost, setup, and security responsibilities. "
                    "Williams is more upbeat about everyday local performance, while still noting slower "
                    "first loads and a per-user setup that does not automatically cover a team. These are "
                    "different operating choices, not one unanimous deployment recipe. Johnson prioritizes "
                    "the API agreement, Serop discusses hosting and existing contracts, and Williams "
                    "demonstrates keeping inference on the user's own hardware. "
                    "[lBhO8Q-MxYI @ 00:03:41] [KeqxPxb_sak @ 00:06:39] [u-qrX9uP_t4 @ 00:03:13]"
                ),
                (
                    "The speakers also differ sharply over how much confidence to place in privacy controls. "
                    "Johnson presents the training toggle as a useful action and distinguishes the API's "
                    "default from the consumer product. WNT takes a much more adversarial reading: it "
                    "criticizes overlapping policy documents, questions the absence of technical verification "
                    "for training exclusions, and argues that memory, metadata, and anonymized aggregate "
                    "data leave users with less control than the interface suggests. WNT acknowledges "
                    "the stated promise that history-disabled conversations will not train models, then "
                    "challenges the trust required to accept it. Its suggestion that the retention window "
                    "could permit extraction is a critical interpretation, not a reported observation of "
                    "that extraction. Serop is explicit about a different evidentiary footing: the video "
                    "discusses other users' posts claiming training settings had switched back on. Serop "
                    "does not conclude malicious intent and instead suggests frequent product updates may "
                    "reset configuration. The practical response offered is to recheck the setting after "
                    "updates and minimize shared information. Preserve that disagreement: WNT attacks the "
                    "credibility of the policy structure, Serop proposes a configuration-failure explanation, "
                    "and Johnson teaches the available controls. Their accounts do not establish that a "
                    "specific opted-out client conversation was actually used for training. "
                    "[lBhO8Q-MxYI @ 00:00:17] [A0tzwuw-nEg @ 00:02:06] [u-qrX9uP_t4 @ 00:01:28]"
                ),
                (
                    "Scope changes have competing operational treatments rather than a single response. "
                    "ProtaSystem pauses work at the boundary and prices the requested addition through a "
                    "formal change order. Augusto Digital often refuses to pull the addition into version "
                    "one at all: the request enters a named not-yet list, and scope is reviewed on a "
                    "ninety-day rhythm instead of at every demo. Its quoted first win used human review, "
                    "while pricing integrations waited for a later version funded by the first deployment's "
                    "return. The difference matters in the speakers' mechanics: one process commercializes "
                    "extra work when the boundary is crossed, while the other protects sequencing and the "
                    "launch date even when an idea is attractive. AI Automation Society complicates both "
                    "approaches with its firsthand account of customer expectations. Some clients welcomed "
                    "the suggestion to start with basic non-AI automation; others demanded execution of "
                    "their original wish list. The speakers say merely performing the written scope could "
                    "still leave customers without value, followed by pressure for more work. Their response "
                    "is to push back earlier and explain what has failed in previous engagements. Augusto "
                    "Digital likewise casts the external partner as the person willing to carry the "
                    "uncomfortable version-two conversation. None of these accounts endorses quietly "
                    "absorbing every addition to avoid disagreement. "
                    "[6l0a6If9Oyk @ 00:02:38] [VzBpfD_Dcq8 @ 00:14:48] [3XIdI6vcGz0 @ 00:02:21]"
                ),
            ],
            "table": {
                "caption": "Different playbooks, with the disagreement or tradeoff left visible.",
                "headers": ["Decision under discussion", "Contrasting practitioner approaches", "Expert Source"],
                "rows": [
                    [
                        "Choose between provider-managed API use and local model inference.",
                        "Johnson favors the API agreement for sensitive work; Williams recommends local Ollama models for information whose exposure would hurt.",
                        "Micah Johnson ([lBhO8Q-MxYI @ 00:03:41]); Matt Williams ([KeqxPxb_sak @ 00:07:54])",
                    ],
                    [
                        "Decide whether local deployment fits an individual or organizational workload.",
                        "Williams demonstrates a per-user desktop integration; Serop discusses company-owned servers and emphasizes significant investment and correct security setup.",
                        "Matt Williams ([KeqxPxb_sak @ 00:06:57]); Serop | AI Automation ([u-qrX9uP_t4 @ 00:05:28])",
                    ],
                    [
                        "Distinguish skeptical policy interpretation from reports of settings changing.",
                        "WNT questions verifiability of exclusions; Serop discusses other users' reports and suggests product updates rather than intentional misconduct.",
                        "WNT ([A0tzwuw-nEg @ 00:02:06]); Serop | AI Automation ([u-qrX9uP_t4 @ 00:01:28])",
                    ],
                    [
                        "Decide whether an additional request becomes paid work or later scope.",
                        "ProtaSystem pauses for a priced change order; Augusto Digital protects the first launch by placing additions on the future roadmap.",
                        "ProtaSystem ([6l0a6If9Oyk @ 00:02:38]); Augusto Digital ([VzBpfD_Dcq8 @ 00:10:10])",
                    ],
                    [
                        "Separate a vendor's training commitment from complete application privacy.",
                        "Johnson emphasizes the API's training default; Protecto says training, retention, residency, and the application's own stores remain separate questions.",
                        "Micah Johnson ([lBhO8Q-MxYI @ 00:00:33]); Protecto ([e8kcLoVVX_A @ 00:00:17])",
                    ],
                    [
                        "Handle customers who want AI features before basic operational fixes.",
                        "AI Automation Society reports both trust-building acceptance and resistance; Augusto Digital gives the external partner responsibility for protecting launch scope.",
                        "AI Automation Society ([3XIdI6vcGz0 @ 00:01:54]); Augusto Digital ([VzBpfD_Dcq8 @ 00:16:33])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics-checks",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Taylor's strongest cost warning is an actual customer build, not the hypothetical "
                    "overnight calling bill discussed earlier in the conversation. The customer gave away "
                    "video space and incurred thirty thousand dollars in the first month. Uploading, storing, "
                    "and watching the videos drove bandwidth and storage usage far beyond what the team "
                    "thought it was building. Taylor says those costs were higher at the time and are "
                    "lower now, but keeps the lesson focused on reporting and administrative visibility. "
                    "The example does not establish a current hosting price or an AI token rate. GTIA's "
                    "Sencka describes a second economic leak: inaccurate project dates contaminate scheduling, "
                    "business intelligence, and customer communication, while untracked scope turns engineering "
                    "hours into unpaid work. The bathroom-renovation example is an analogy about timing, "
                    "not an MSP invoice case: an extra charge discussed during the job is a different "
                    "conversation from a surprise bill four months after completion. Sencka's answer is "
                    "continuous project observation so managers can identify overages early and negotiate "
                    "while the customer relationship and active work still provide context. Together, the "
                    "accounts keep two costs visible without conflating them: metered consumption can "
                    "explode under a free offer, and delivery labor can leak when extra scope is "
                    "neither tracked nor discussed promptly. "
                    "[yLxvwa45vR8 @ 00:03:17] [TtU19Z-ASZk @ 00:03:20] [TtU19Z-ASZk @ 00:04:37]"
                ),
                (
                    "neomanex's runner build shows why implementation and acceptance are not interchangeable. "
                    "Testing agents ran twenty-five checks on a real cluster and saved two hundred eighty "
                    "screenshots. Eight checks failed in the first round. One requirement said the run "
                    "detail page must name its runner; the information existed in code and could be "
                    "requested through the API, but it was absent from the page. The tester failed it "
                    "because the requirement named what the user must see. Fixes and retests moved through "
                    "eight, three, one, and one failures before the fifth round reached thirty-six "
                    "requirements passing. Even then, a separate agent walking the done-when list found "
                    "four gaps: two needed fixes and two went to the owner for a decision. Augusto "
                    "Digital reports a different firsthand bottleneck: scope creep appeared in five "
                    "meetings across six weeks of one engagement, driven by enthusiasm after a successful "
                    "demo. Its speakers also recount a developer describing ninety percent of a drifting "
                    "project's code as brittle workarounds; that number belongs to the developer's account, "
                    "not an audit by the hosts. Augusto's recovery method is a two-week rumble: halt "
                    "peripheral development, resequence the work into a build-ready first win, and push "
                    "the remainder onto a structured future roadmap. "
                    "[wOkT9r5iVME @ 00:06:21] [wOkT9r5iVME @ 00:07:21] [VzBpfD_Dcq8 @ 00:01:32] [VzBpfD_Dcq8 @ 00:17:38]"
                ),
                (
                    "Privacy failures do not all begin at the model provider. Williams identifies a "
                    "specific trap in the local-model workflow: switching an existing sensitive conversation "
                    "to an OpenAI model sends that conversation's data there too. The demonstrated local "
                    "setup also operates per user, so it does not silently extend protection across a "
                    "company. Cognitive Capital focuses on mundane leakage through support tickets, API "
                    "keys, observability logs, and embedded text. Its benchmark discussion explicitly rejects "
                    "the shortcut from a strong published score to domain accuracy: false negatives miss "
                    "secrets, while excessive redaction can destroy useful downstream analysis. Its checks "
                    "include reviewing masking differences and planting partial addresses, unusual nicknames, "
                    "and implied identities in test data. Privado AI supplies a reported enforcement history "
                    "rather than a firsthand agency incident. The account begins with a March 2023 breach "
                    "exposing some chat histories and partial payment details, then describes an Italian "
                    "processing restriction and a later fifteen-million-euro fine involving several privacy "
                    "issues. The speaker says some issues were partially or fully resolved while others "
                    "remained, and describes further demands concerning information, policy, and age checks. "
                    "Keep the reported chain intact: it was not presented as a fine for one agency's "
                    "missing redaction filter. Each speaker identifies a different failure surface and "
                    "a different kind of evidence. "
                    "[KeqxPxb_sak @ 00:03:57] [j2Bqq0VTv0o @ 00:02:22] [3wH9U_IzNn8 @ 00:01:31]"
                ),
            ],
            "table": {
                "caption": "Observed failures, reported incidents, and clearly identified illustrative traps.",
                "headers": ["Failure or economic exposure", "What the speaker actually reports", "Expert Source"],
                "rows": [
                    [
                        "A free video offer generated substantial paid infrastructure consumption.",
                        "Taylor's customer incurred thirty thousand dollars in the first month through storage, bandwidth, uploads, and viewing beyond the expected usage.",
                        "Bryan Taylor ([yLxvwa45vR8 @ 00:03:17])",
                    ],
                    [
                        "Correct backend data failed the explicitly promised user-visible requirement.",
                        "neomanex's tester could retrieve runner information through the API, but failed the check because the promised page did not display it.",
                        "neomanex ([wOkT9r5iVME @ 00:06:42])",
                    ],
                    [
                        "Passing the main testing rounds did not finish every acceptance decision.",
                        "A separate done-when review found four gaps after the testing result: two required fixes and two required the owner's decision.",
                        "neomanex ([wOkT9r5iVME @ 00:07:21])",
                    ],
                    [
                        "Successful demos triggered repeated scope discussions within one active engagement.",
                        "Augusto Digital reports five scope-creep meetings across six weeks, with stakeholders responding to success by requesting additional capabilities.",
                        "Augusto Digital ([VzBpfD_Dcq8 @ 00:01:32])",
                    ],
                    [
                        "Changing models inside a sensitive chat changes where its data goes.",
                        "Williams warns that switching from a local model to an OpenAI model sends the existing conversation data onward; a new chat avoids that carryover.",
                        "Matt Williams ([KeqxPxb_sak @ 00:03:57])",
                    ],
                    [
                        "A reported privacy incident expanded into a broader enforcement history.",
                        "Privado AI recounts exposed histories and partial payment details, a temporary Italian processing restriction, and later action involving multiple privacy issues.",
                        "Privado AI ([3wH9U_IzNn8 @ 00:01:31])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks tied to the failures the speakers describe",
                "body": "Use these checks before calling the corresponding work finished.",
                "items": [
                    (
                        "Can each promised screen or state be observed in the shipped product? neomanex "
                        "failed a runner-name requirement even though the value existed in code and the API. "
                        "[neomanex — wOkT9r5iVME @ 00:06:42]"
                    ),
                    (
                        "Is consumption visible through reporting and an admin tool? Taylor puts those "
                        "early in the build and recounts the customer's thirty-thousand-dollar video bill. "
                        "[Bryan Taylor — yLxvwa45vR8 @ 00:03:04]"
                    ),
                    (
                        "Has the agreement bounded extra work and liability? ProtaSystem calls for a "
                        "priced change-order pause and an aggregate cap tied to the amount actually paid. "
                        "[ProtaSystem — 6l0a6If9Oyk @ 00:02:38] "
                        "[ProtaSystem — 6l0a6If9Oyk @ 00:03:49]"
                    ),
                    (
                        "Have training, retention eligibility, exceptions, abuse monitoring, storage "
                        "location, inference location, and necessary sensitive fields been checked separately? "
                        "[Protecto — e8kcLoVVX_A @ 00:01:54]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        "'One outcome, one owner, one date.' — Augusto Digital "
        "(VzBpfD_Dcq8 @ 00:07:01)."
    ),
    "diagram_id": "diag-08",
    "action_checklist": [
        (
            "Define the human-reviewed first outcome, assign its owner and date, and put additional "
            "requests on a visible not-yet list. "
            "[Augusto Digital — VzBpfD_Dcq8 @ 00:07:01] "
            "[Augusto Digital — VzBpfD_Dcq8 @ 00:10:27]"
        ),
        (
            "Freeze requirements written as who, what, and observable proof; add explicit exclusions "
            "and a done-when box for every requirement. "
            "[neomanex — wOkT9r5iVME @ 00:02:25] "
            "[neomanex — wOkT9r5iVME @ 00:04:04]"
        ),
        (
            "Specify bounded deliverables and revisions, pause for priced additions, and negotiate "
            "an aggregate liability cap tied to payment received. "
            "[ProtaSystem — 6l0a6If9Oyk @ 00:01:46] "
            "[ProtaSystem — 6l0a6If9Oyk @ 00:03:49]"
        ),
        (
            "Check the training setting and product agreement; recheck settings after updates "
            "rather than assuming an earlier selection remains unchanged. "
            "[Micah Johnson — lBhO8Q-MxYI @ 00:00:17] "
            "[Serop | AI Automation — u-qrX9uP_t4 @ 00:01:47]"
        ),
        (
            "Pilot local masking on one stream, inspect the differences, and scrub ingestion, "
            "logging, and retrieved passages before their next use. "
            "[Cognitive Capital — j2Bqq0VTv0o @ 00:03:05] "
            "[Cognitive Capital — j2Bqq0VTv0o @ 00:05:27]"
        ),
        (
            "Build usage reporting early and complete deletion work through the contract-defined "
            "backup interval and support verification. "
            "[Bryan Taylor — yLxvwa45vR8 @ 00:03:04] "
            "[SecureCyberGates — TcAbiyEqBFM @ 00:04:39]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Protecto — Zero Data Retention Is Not Enough for AI Security (3 Controls Explained) #ai #aisecurity [00:00:17]",
            "url": "https://www.youtube.com/watch?v=e8kcLoVVX_A&t=17s",
            "relevance": "Primary practitioner testimony separating no training, zero data retention, and data residency.",
        },
        {
            "title": "neomanex — Stop AI Agent Scope Creep: Frozen Requirements and a Done When List [00:06:42]",
            "url": "https://www.youtube.com/watch?v=wOkT9r5iVME&t=402s",
            "relevance": "Primary practitioner testimony on a shipped interface failing an observable requirement despite backend implementation.",
        },
        {
            "title": "ProtaSystem — Uncapped Indemnity & Scope Creep: The Contract Traps Every Freelancer Faces [00:03:49]",
            "url": "https://www.youtube.com/watch?v=6l0a6If9Oyk&t=229s",
            "relevance": "Primary practitioner testimony advocating an aggregate liability cap tied to the amount actually paid.",
        },
        {
            "title": "Bryan Taylor — Custom Software Development Pitfalls: Scope Creep, AI Dependence, and Uncapped API Costs [00:03:17]",
            "url": "https://www.youtube.com/watch?v=yLxvwa45vR8&t=197s",
            "relevance": "Primary practitioner testimony on a customer's first-month video-service consumption costs.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "TtU19Z-ASZk",
            "title": "Project Risk, Scope Creep, and AI Automation for MSPs",
            "channel": "Global Technology Industry Association (GTIA)",
            "author": "Global Technology Industry Association (GTIA)",
            "text": "Scope creep is a direct bottom line margin leak. It's your engineers working on something more than you're getting paid for. It's not getting tracked.",
            "tip": "Scope creep is a direct bottom line margin leak. It's your engineers working on something more than you're getting paid for. It's not getting tracked.",
            "timestamp": 261,
            "timestamp_seconds": 261,
            "timestamp_label": "[00:04:21]",
            "url": "https://www.youtube.com/watch?v=TtU19Z-ASZk&t=261s",
            "markdown": "[00:04:21](https://www.youtube.com/watch?v=TtU19Z-ASZk&t=261s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony connecting untracked engineering work to project margin leakage.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "yLxvwa45vR8",
            "title": "Custom Software Development Pitfalls: Scope Creep, AI Dependence, and Uncapped API Costs",
            "channel": "Bryan Taylor",
            "author": "Bryan Taylor",
            "text": "We built a software once for a customer and they were giving it away and it ended up costing them $30,000 their first month because they didn't realize that they're giving away all this video space.",
            "tip": "We built a software once for a customer and they were giving it away and it ended up costing them $30,000 their first month because they didn't realize that they're giving away all this video space.",
            "timestamp": 197,
            "timestamp_seconds": 197,
            "timestamp_label": "[00:03:17]",
            "url": "https://www.youtube.com/watch?v=yLxvwa45vR8&t=197s",
            "markdown": "[00:03:17](https://www.youtube.com/watch?v=yLxvwa45vR8&t=197s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Firsthand account of unexpected customer video-service costs.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "VzBpfD_Dcq8",
            "title": "Ep. 17: Stopping AI Scope Creep | Augusto Podcast",
            "channel": "Augusto Digital",
            "author": "Augusto Digital",
            "text": "One outcome, one owner, one date.",
            "tip": "One outcome, one owner, one date.",
            "timestamp": 421,
            "timestamp_seconds": 421,
            "timestamp_label": "[00:07:01]",
            "url": "https://www.youtube.com/watch?v=VzBpfD_Dcq8&t=421s",
            "markdown": "[00:07:01](https://www.youtube.com/watch?v=VzBpfD_Dcq8&t=421s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The practitioner's central scope anchor for a shipped first outcome.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "wOkT9r5iVME",
            "title": "Stop AI Agent Scope Creep: Frozen Requirements and a Done When List",
            "channel": "neomanex",
            "author": "neomanex",
            "text": "Every requirement has the same three parts. Who does it, what they can do, and how you'd prove it from the outside.",
            "tip": "Every requirement has the same three parts. Who does it, what they can do, and how you'd prove it from the outside.",
            "timestamp": 145,
            "timestamp_seconds": 145,
            "timestamp_label": "[00:02:25]",
            "url": "https://www.youtube.com/watch?v=wOkT9r5iVME&t=145s",
            "markdown": "[00:02:25](https://www.youtube.com/watch?v=wOkT9r5iVME&t=145s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Observable requirements used throughout design, implementation, and acceptance testing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "6l0a6If9Oyk",
            "title": "Uncapped Indemnity & Scope Creep: The Contract Traps Every Freelancer Faces",
            "channel": "ProtaSystem",
            "author": "ProtaSystem",
            "text": "When a boundary is crossed, work pauses until the new request is quoted, documented, and priced as an addition.",
            "tip": "When a boundary is crossed, work pauses until the new request is quoted, documented, and priced as an addition.",
            "timestamp": 158,
            "timestamp_seconds": 158,
            "timestamp_label": "[00:02:38]",
            "url": "https://www.youtube.com/watch?v=6l0a6If9Oyk&t=158s",
            "markdown": "[00:02:38](https://www.youtube.com/watch?v=6l0a6If9Oyk&t=158s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The speaker's formal change-order response to unpaid scope expansion.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "3XIdI6vcGz0",
            "title": "The Scope Creep Mistake That Can Wreck AI Projects",
            "channel": "AI Automation Society",
            "author": "AI Automation Society",
            "text": "If we want our customers or clients to be happy at the end of this stuff, we have to be very, very honest, manage expectations effectively.",
            "tip": "If we want our customers or clients to be happy at the end of this stuff, we have to be very, very honest, manage expectations effectively.",
            "timestamp": 201,
            "timestamp_seconds": 201,
            "timestamp_label": "[00:03:21]",
            "url": "https://www.youtube.com/watch?v=3XIdI6vcGz0&t=201s",
            "markdown": "[00:03:21](https://www.youtube.com/watch?v=3XIdI6vcGz0&t=201s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Client-work experience behind early pushback and expectation management.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TcAbiyEqBFM",
            "title": "23-[5.16] SOC2 – Data Retention Policy",
            "channel": "SecureCyberGates",
            "author": "SecureCyberGates",
            "text": "The actual retention time depends on project contract and also regulatory laws.",
            "tip": "The actual retention time depends on project contract and also regulatory laws.",
            "timestamp": 235,
            "timestamp_seconds": 235,
            "timestamp_label": "[00:03:55]",
            "url": "https://www.youtube.com/watch?v=TcAbiyEqBFM&t=235s",
            "markdown": "[00:03:55](https://www.youtube.com/watch?v=TcAbiyEqBFM&t=235s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Project-specific retention periods rather than universal adoption of the walkthrough's example numbers.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "lBhO8Q-MxYI",
            "title": "OpenAI's New Privacy Policy: What Every Business Owner Needs to Know",
            "channel": "Micah Johnson",
            "author": "Micah Johnson",
            "text": "If you use the API, your data is not used for training by default. That's a completely different agreement.",
            "tip": "If you use the API, your data is not used for training by default. That's a completely different agreement.",
            "timestamp": 33,
            "timestamp_seconds": 33,
            "timestamp_label": "[00:00:33]",
            "url": "https://www.youtube.com/watch?v=lBhO8Q-MxYI&t=33s",
            "markdown": "[00:00:33](https://www.youtube.com/watch?v=lBhO8Q-MxYI&t=33s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Johnson's distinction between API training defaults and consumer ChatGPT controls.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ZE-vxHSGB7w",
            "title": "Securing SMB GenAI Pipelines  Guardrails, Data Privacy & ISO SOC2 Compliance on AWS",
            "channel": "Cloud in",
            "author": "Cloud in",
            "text": "No account in your current organization or current infra should have all the access to all the services.",
            "tip": "No account in your current organization or current infra should have all the access to all the services.",
            "timestamp": 1406,
            "timestamp_seconds": 1406,
            "timestamp_label": "[00:23:26]",
            "url": "https://www.youtube.com/watch?v=ZE-vxHSGB7w&t=1406s",
            "markdown": "[00:23:26](https://www.youtube.com/watch?v=ZE-vxHSGB7w&t=1406s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Least-privilege access as part of the customer's GenAI pipeline configuration.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "e8kcLoVVX_A",
            "title": "Zero Data Retention Is Not Enough for AI Security (3 Controls Explained) #ai #aisecurity",
            "channel": "Protecto",
            "author": "Protecto",
            "text": "The model may be stateless, but your system is not. Your logs are not stateless. Your retrieval pipeline is not stateless. Your tools and databases are not stateless.",
            "tip": "The model may be stateless, but your system is not. Your logs are not stateless. Your retrieval pipeline is not stateless. Your tools and databases are not stateless.",
            "timestamp": 65,
            "timestamp_seconds": 65,
            "timestamp_label": "[00:01:05]",
            "url": "https://www.youtube.com/watch?v=e8kcLoVVX_A&t=65s",
            "markdown": "[00:01:05](https://www.youtube.com/watch?v=e8kcLoVVX_A&t=65s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Application-level persistence beyond a provider's zero-retention commitment.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "j2Bqq0VTv0o",
            "title": "OpenAI Privacy Filter: Redact PII Locally (AI Workflow Explained)",
            "channel": "Cognitive Capital",
            "author": "Cognitive Capital",
            "text": "First, pick a stream. Isolate a single data stream, like your support tickets. Don't try to boil the ocean on day one.",
            "tip": "First, pick a stream. Isolate a single data stream, like your support tickets. Don't try to boil the ocean on day one.",
            "timestamp": 327,
            "timestamp_seconds": 327,
            "timestamp_label": "[00:05:27]",
            "url": "https://www.youtube.com/watch?v=j2Bqq0VTv0o&t=327s",
            "markdown": "[00:05:27](https://www.youtube.com/watch?v=j2Bqq0VTv0o&t=327s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The first step of a local-redaction pilot with before-and-after review.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "3wH9U_IzNn8",
            "title": "Italian DPA fines OpenAI €15M, CPPA settles with data brokers, and Google allows fingerprinting.",
            "channel": "Privado AI",
            "author": "Privado AI",
            "text": "It starts in March 2023 when there was a relatively minor data breach involving ChatGPT. Some people's chat histories and partial payment details were exposed.",
            "tip": "It starts in March 2023 when there was a relatively minor data breach involving ChatGPT. Some people's chat histories and partial payment details were exposed.",
            "timestamp": 91,
            "timestamp_seconds": 91,
            "timestamp_label": "[00:01:31]",
            "url": "https://www.youtube.com/watch?v=3wH9U_IzNn8&t=91s",
            "markdown": "[00:01:31](https://www.youtube.com/watch?v=3wH9U_IzNn8&t=91s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Reported incident at the beginning of the speaker's Italian enforcement chronology.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "u-qrX9uP_t4",
            "title": "OpenAI's Secret Data Training: What You Need To Know",
            "channel": "Serop | AI Automation",
            "author": "Serop | AI Automation",
            "text": "I don't think OpenAI or Anthropic and so on are doing this maliciously.",
            "tip": "I don't think OpenAI or Anthropic and so on are doing this maliciously.",
            "timestamp": 88,
            "timestamp_seconds": 88,
            "timestamp_label": "[00:01:28]",
            "url": "https://www.youtube.com/watch?v=u-qrX9uP_t4&t=88s",
            "markdown": "[00:01:28](https://www.youtube.com/watch?v=u-qrX9uP_t4&t=88s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Serop's interpretation of other users' reports, contrasted with a more adversarial account of privacy controls.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "DIfo9jAMZYY",
            "title": "OpenAI's Policies Explained: EU Privacy, Security, Safety, and Your Data Rights (ChatGPT, Sora,API)",
            "channel": "Innovative Compass Consulting",
            "author": "Innovative Compass Consulting",
            "text": "The AI could give another user a very similar or even identical response if they ask a similar question.",
            "tip": "The AI could give another user a very similar or even identical response if they ask a similar question.",
            "timestamp": 186,
            "timestamp_seconds": 186,
            "timestamp_label": "[00:03:06]",
            "url": "https://www.youtube.com/watch?v=DIfo9jAMZYY&t=186s",
            "markdown": "[00:03:06](https://www.youtube.com/watch?v=DIfo9jAMZYY&t=186s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The speaker distinguishes output ownership from uniqueness.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KeqxPxb_sak",
            "title": "Stop Sending Your Private Data to OpenAI's Servers",
            "channel": "Matt Williams",
            "author": "Matt Williams",
            "text": "If you shared a private document with a local model, then switch mid conversation to an OpenAI model, all the data will go there, too.",
            "tip": "If you shared a private document with a local model, then switch mid conversation to an OpenAI model, all the data will go there, too.",
            "timestamp": 237,
            "timestamp_seconds": 237,
            "timestamp_label": "[00:03:57]",
            "url": "https://www.youtube.com/watch?v=KeqxPxb_sak&t=237s",
            "markdown": "[00:03:57](https://www.youtube.com/watch?v=KeqxPxb_sak&t=237s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The privacy trap when changing from local inference to cloud inference inside an existing conversation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "A0tzwuw-nEg",
            "title": "AI Reads OpenAI's Privacy Policy, Finds Data Trap | WNT #lawyer #openai",
            "channel": "WNT",
            "author": "WNT",
            "text": "The FAQ mentions that disabling chat history means conversations won't be used to train our models, but provides zero technical verification of this claim.",
            "tip": "The FAQ mentions that disabling chat history means conversations won't be used to train our models, but provides zero technical verification of this claim.",
            "timestamp": 126,
            "timestamp_seconds": 126,
            "timestamp_label": "[00:02:06]",
            "url": "https://www.youtube.com/watch?v=A0tzwuw-nEg&t=126s",
            "markdown": "[00:02:06](https://www.youtube.com/watch?v=A0tzwuw-nEg&t=126s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "WNT's skeptical interpretation of training exclusions and their verifiability, rather than evidence of a specific training event.",
        },
    ],
}
