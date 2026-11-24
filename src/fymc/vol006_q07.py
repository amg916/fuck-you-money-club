from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "zapier-make-n8n-ai-automation-costs-self-hosted-agents",
    "question_prompt": "How do Zapier, Make and n8n compare on usability, small-business and per-workflow costs, team needs and building the same AI lead responder? Where does UiPath fit, and how can self-hosted n8n, Claude MCP, AI assistants and Groq/Gemini support AI agents, workflow creation and an AI automation agency while reducing software fees?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "Zapier vs Make vs n8n: AI Automation Tools, Costs & Self-Hosted Agents",
    "subtitle": "2025–2026 comparisons of pricing, ease of use, team fit and developer workflows, plus UiPath, AI lead responders, automation agencies and self-hosted n8n with Claude MCP, AI assistants and Groq/Gemini.",
    "layout_template": "thirty_day_roadmap",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Practitioners broadly agree: Zapier gets simple automations running fastest, Make exposes branching "
        "visually, and n8n gives technical operators deeper control and self-hosting. The economics turn on "
        "tasks, credits, and complete workflow executions—not just the advertised subscription. ProfitPilot "
        "prices a four-action lead workflow at $49 on Zapier, $9 on Make, and €20 on n8n Cloud for "
        "500 monthly leads under stated billing assumptions. Owner's Bot Lab nevertheless ranks n8n first "
        "in its responder test, while Paired Recruiting favors Make for remote teams. Jonas runs client "
        "workflows on free n8n software but pays for hosting. SaaS Master and Cuebic AI demonstrate "
        "AI-assisted workflow creation; the operational catches are credentials, silent failures, duplicate "
        "messages, maintenance, and model charges."
    ),
    "key_metrics": [
        {
            "label": "Four-action workflow at 500 monthly leads",
            "metric": "Four-action workflow at 500 monthly leads",
            "value": "Zapier $49; Make $9; n8n Cloud €20 per month",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "ProfitPilot's annual-billing calculation uses 2,000 Zapier tasks, about 2,500 Make credits, "
                "and 500 n8n executions. It assumes Standard-tier Zapier AI and excludes separate model costs."
            ),
            "source": "ProfitPilot ([d8w8FHZJpdY @ 00:03:09])",
        },
        {
            "label": "Lead-responder stress test",
            "metric": "Lead-responder stress test",
            "value": "20 leads; 4 emergencies; zero false alarms; zero prices quoted",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Owner's Bot Lab reports these results across all three tools. Make repeated the customer's "
                "50% discount wording, producing a stricter final score of 19 out of 20 for Make."
            ),
            "source": "Owner's Bot Lab ([EtiRX0GduSI @ 00:04:03])",
        },
        {
            "label": "Client payment workflow complexity",
            "metric": "Client payment workflow complexity",
            "value": "67 steps counted as one n8n execution",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Jonas describes a Stripe payment workflow that updates a CRM, creates a project, and handles "
                "failed payments within a dashboard containing over 100 workflows."
            ),
            "source": "Jonas | AI Tools & Automation ([4imOFZeP7nk @ 00:05:15])",
        },
        {
            "label": "Starter automation pack",
            "metric": "Starter automation pack",
            "value": "$1,500 setup plus $500 monthly",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "The AI Blueprint teaches this price for two custom core workflows with ongoing maintenance "
                "and uptime monitoring; it is the proposed starter offer, not a reported client receipt."
            ),
            "source": "The AI Blueprint ([1mZ0bWq9y-M @ 00:02:20])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The common starting point is a broken handoff, not an AI agent looking for something to do. "
                    "Erin at Paired Recruiting describes remote teams losing time because a form arrives, a lead "
                    "sits unseen, or the next person never learns that work is ready. Their basic automation "
                    "moves a submission into a CRM, notifies the team, and creates a task without someone "
                    "coordinating every transfer. LearnAI Today describes the same operating pattern through "
                    "inquiries, welcome emails, and invoice entry: identify the trigger, apply the rules, and "
                    "perform the action. Jonas reduces the architecture to two parts, triggers and actions, "
                    "including triggers that come from another automation. That agreement matters for the "
                    "productized offer: the deliverable is an operating process, not merely a connection between "
                    "two logos. Paired's examples extend into onboarding, documents, content status updates, and "
                    "internal coordination. Jonas sells chatbots, lead follow-ups, and payment syncs built from "
                    "that same pattern. The tools differ in how builders express the sequence, but the underlying "
                    "job remains moving information and starting the next useful action without repeated manual "
                    "checking. Paired's instruction is to start with one process, get it working, and build from "
                    "there. Paired Recruiting [TdMOpd_cG0A @ 00:00:44]; LearnAI Today "
                    "[Pd96DxQ36U8 @ 00:00:37]; Jonas [4imOFZeP7nk @ 00:01:07]."
                ),
                (
                    "The usability consensus is unusually consistent. Simplified positions Zapier as the starting "
                    "point for nontechnical users, Make as the stronger visual environment for advanced scenarios, "
                    "and n8n as the more developer-oriented choice. Marc reaches the same conclusion after "
                    "building a sales email workflow on all three: Zapier is quickest, Make is close behind, "
                    "and n8n requires more familiarity before the workflow comes together. Importantly, Marc "
                    "builds those examples without writing code; n8n's technical positioning does not mean every "
                    "workflow requires programming. LearnAI Today explains the distinction through the editors: "
                    "Zapier stacks actions in a top-to-bottom list, Make maps modules across a canvas, and n8n "
                    "combines a visual node editor with code where built-in nodes fall short. Team fit therefore "
                    "stays central to each recommendation. Marc favors Zapier for owners and marketing or "
                    "operations teams minimizing build time, Make for advanced no-code builders, and n8n for "
                    "technical teams wanting infrastructure control. Simplified also includes integration needs, "
                    "workflow complexity, budget, and existing team skills in the decision. None of these "
                    "comparisons makes the most technically elaborate platform the automatic winner for a simple "
                    "handoff. The recurring trade is speed and managed convenience against visual flexibility "
                    "and deeper control. Simplified [IYV8OVFzq_c @ 00:00:46]; Automate with Marc "
                    "[syCqaV7N73s @ 00:28:03]; LearnAI Today [Pd96DxQ36U8 @ 00:03:34]."
                ),
                (
                    "The billing consensus starts with what gets counted. ProfitPilot identifies a Zapier task "
                    "as a successful action, excludes triggers and built-in tools such as Filter, Paths, and "
                    "Formatter, and counts most Make modules as credits, including the trigger. Routers and "
                    "error handlers are exceptions in that Make comparison. One n8n execution is a complete "
                    "workflow run rather than a charge for each individual step. AI Business Tools & Automation "
                    "uses a five-action lead workflow to show why those definitions matter: 500 leads become "
                    "about 2,500 tasks, 3,000 credits, or 500 executions under its assumptions. Whizz AI agrees "
                    "that Make often offers the low-cost visual route for a small business, while n8n appeals "
                    "to operators avoiding per-step charging and seeking control. Self-hosting changes who runs "
                    "the software, not whether operational work exists. Whizz explicitly assigns updates, "
                    "security, and continued operation to the self-hosting team. ProfitPilot also separates "
                    "model costs from the platform figures. The baseline comparison is consequently a named "
                    "workflow at a named volume, with its actual billing unit and AI configuration visible. "
                    "AI Business Tools & Automation tells buyers to build a real workflow, run it for a week, "
                    "and read the usage meter rather than choose from headline prices alone. ProfitPilot "
                    "[d8w8FHZJpdY @ 00:00:46]; AI Business Tools & Automation "
                    "[PKHb0KLNOIg @ 00:00:54]; Whizz AI [Pz3jLYQwsX4 @ 00:04:57]."
                ),
            ],
            "table": {
                "caption": "The shared operating baseline before choosing an automation platform",
                "headers": ["Operating decision", "Practitioner mechanics and team fit", "Expert Source"],
                "rows": [
                    [
                        "Begin with a handoff that currently requires repeated manual coordination",
                        "Paired describes form submission, CRM entry, notification, and task creation as one connected process rather than four separate manual obligations.",
                        "Paired Recruiting ([TdMOpd_cG0A @ 00:01:44])",
                    ],
                    [
                        "Use Zapier when getting a simple workflow running is the priority",
                        "Marc calls Zapier fast and beginner-friendly for business owners and nontechnical teams that want to spend little time building.",
                        "Automate with Marc | AI Automation ([syCqaV7N73s @ 00:00:42])",
                    ],
                    [
                        "Use Make when the team needs visible branching and data movement",
                        "LearnAI Today explains routers, iterators, filters, and inspection of module data as the strengths of Make's visual scenario builder.",
                        "LearnAI Today ([Pd96DxQ36U8 @ 00:02:42])",
                    ],
                    [
                        "Use n8n when technical control and flexible workflow building matter",
                        "Simplified highlights data transformation, multiple triggers, and developer-friendly customization rather than treating every platform as interchangeable.",
                        "Simplified ([IYV8OVFzq_c @ 00:02:58])",
                    ],
                    [
                        "Count billable work rather than comparing subscription headlines in isolation",
                        "ProfitPilot distinguishes successful Zapier actions, most Make modules including triggers, and one complete workflow execution for n8n.",
                        "ProfitPilot ([d8w8FHZJpdY @ 00:00:46])",
                    ],
                    [
                        "Separate free self-hosted software from the job of keeping it operating",
                        "Whizz AI says self-hosting places continued operation, updates, and security with the operator even when the software itself costs nothing.",
                        "Whizz AI ([Pz3jLYQwsX4 @ 00:04:57])",
                    ],
                ],
            },
        },
        {
            "id": "exact-street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Marc's repeatable lead-writer build starts with a Google Sheet containing first name, last "
                    "name, company, phone, and email. A newly added row triggers the AI writer, and Gmail sends "
                    "the result. In Zapier, select Google Sheets, choose the new-row event, connect the account, "
                    "select the spreadsheet and worksheet, and test the incoming record. The AI step uses a "
                    "custom prompt with dynamically mapped lead fields, a concise email under 150 words, and "
                    "separate email-subject and email-body outputs. Map those outputs into Gmail rather than "
                    "copying a sample lead's details into fixed text. Marc's Make version watches new rows, "
                    "connects OpenAI through an API key, selects GPT 4.1 mini, maps the lead fields, and sends "
                    "the result through Gmail. Its subject is fixed rather than generated separately. The "
                    "n8n version uses a row-added trigger, an AI Agent with an attached chat model, expression "
                    "mapping, and Gmail. Owner's Bot Lab shows why output structure matters: its responder "
                    "needs separate emergency status, summary, and reply fields, and Zapier supplied those "
                    "separately while Make needed another component and n8n used copied code. Marc's simple "
                    "writer and that emergency responder share mapping mechanics without being identical builds. "
                    "Automate with Marc [syCqaV7N73s @ 00:07:35]; Owner's Bot Lab "
                    "[EtiRX0GduSI @ 00:01:30]."
                ),
                (
                    "SaaS Master's self-hosted route begins in a VPS dashboard, opens Docker Manager, and uses "
                    "Compose's one-click deployment to select n8n with the AI Assistant. After creating the "
                    "instance account, the next connection is instance-level MCP: enable it in n8n settings, "
                    "copy the connection URL, and add a custom connector in Claude. A new chat can then "
                    "brainstorm and build workflows against that connection. Their working example is Fresh "
                    "Product Radar, which examines GitHub, Hugging Face, and Product Hunt, uses an AI step, "
                    "and continues into filters, Google Sheets, and email. Cuebic AI demonstrates a different "
                    "configuration route inside its instance dashboard. Enable the AI assistant, choose "
                    "OpenRouter, provide its API key, select the model, optionally add Brave search, enable "
                    "agents and the knowledge base, then apply the changes. After reloading the workspace, "
                    "Cuebic first checks that the assistant responds and then asks it to add an if node "
                    "to an existing workflow. The demonstration distinguishes an assistant that changes "
                    "workflow structure from an agent configured with channels, tools, skills, subagents, "
                    "schedules, a model, and instructions. These are two demonstrated paths to AI-assisted "
                    "building on self-hosted n8n, not a requirement to connect every node manually. SaaS Master "
                    "[TdMeBa69Y8Y @ 00:02:03]; Cuebic AI [BxxP4kEqOdg @ 00:01:39]."
                ),
                (
                    "12_5 Tech teaches the self-hosted agent as four connected blocks: a Gmail, Telegram, or "
                    "webhook trigger; an AI Agent node with memory and tools; a Groq model or Gemini Flash; "
                    "and actions in Slack, Sheets, or Gmail. Its deployment instructions emphasize Docker "
                    "Compose, a pinned image, port 5678, a fixed encryption key, persistent workflow data, "
                    "and seven-day execution pruning. The operational point is specific: recreating the "
                    "container without the fixed key can break saved API credentials, while unpruned execution "
                    "logs can fill a small VPS disk. Fireship demonstrates another route using a prebuilt "
                    "Ubuntu VPS template, then either importing JSON workflows or creating a trigger and "
                    "adding conditional logic, API calls, and an AI Agent. Their agent example draws on "
                    "earlier workflow data and can attach a model, memory, and MCP tools. Jonas supplies "
                    "the practical transition from local experimentation to ongoing client service: running "
                    "on a laptop is useful for testing, but shutting that computer down stops the app. "
                    "They move it to a small server costing around €6 monthly. Free community software "
                    "and an always-running deployment are separate parts of these operators' setups. 12_5 Tech "
                    "[0EeWohGy6RM @ 00:00:39]; Fireship [bS9R6aCVEzw @ 00:02:44]; Jonas "
                    "[4imOFZeP7nk @ 00:04:34]."
                ),
                (
                    "The AI Blueprint packages the build around business outcomes: saving time, cutting payroll "
                    "costs, or generating customer revenue. Its lead-intelligence architecture captures a website "
                    "submission with a webhook, uses an HTTP node and Crawl4AI to extract company information, "
                    "passes that material into an AI Agent for pain-point analysis and a proposal outline, "
                    "then syncs the result into HubSpot or Notion and notifies sales in Slack. The taught "
                    "starter offer is two custom core workflows for $1,500 setup and $500 monthly maintenance "
                    "and uptime monitoring. Its larger offer is $3,000 setup plus $1,500 monthly for end-to-end "
                    "CRM and support automation. Acquisition is equally concrete: choose an industry, record "
                    "a three-minute demonstration of its weekly bottleneck, contact 20 LinkedIn decision "
                    "makers, and offer a seven-day installation trial. Jonas describes sellable work they "
                    "have actually built: Instagram and WhatsApp chatbots, follow-ups, payment syncs, lead "
                    "research, and ongoing upkeep. Paired Recruiting supplies the corresponding team bottleneck: "
                    "after choosing a capable tool, someone still has to build, maintain, fix, and improve "
                    "the workflows. Those maintenance responsibilities are explicitly part of the service "
                    "rather than an afterthought to the initial automation delivery. The AI Blueprint "
                    "[1mZ0bWq9y-M @ 00:01:42]; Jonas [4imOFZeP7nk @ 00:07:48]; Paired Recruiting "
                    "[TdMOpd_cG0A @ 00:08:14]."
                ),
            ],
            "table": {
                "caption": "Exact builds, billing assumptions, and service packages taught by practitioners",
                "headers": ["Build or economic comparison", "Exact mechanics and attributed figures", "Expert Source"],
                "rows": [
                    [
                        "Build the three-stage sales writer with dynamic lead fields",
                        "Marc connects a new Google Sheets row to an AI writer and Gmail, keeping generated subject and body separate in Zapier.",
                        "Automate with Marc | AI Automation ([syCqaV7N73s @ 00:09:44])",
                    ],
                    [
                        "Price ProfitPilot's four-action lead workflow at 500 monthly leads",
                        "Annual-billing examples are $49 for 2,000 Zapier tasks, $9 for about 2,500 Make credits, and €20 for n8n Starter.",
                        "ProfitPilot ([d8w8FHZJpdY @ 00:03:09])",
                    ],
                    [
                        "Keep the five-action pricing example separate from the four-action example",
                        "AI Business Tools & Automation counts 2,500 Zapier tasks at 500 leads, exceeding its stated 2,000-task tier and reaching the $89 tier.",
                        "AI Business Tools & Automation ([PKHb0KLNOIg @ 00:01:31])",
                    ],
                    [
                        "Connect a self-hosted n8n instance to Claude through MCP",
                        "SaaS Master enables instance-level MCP, copies the connection URL, and adds a custom connector before requesting workflow creation in chat.",
                        "SaaS Master ([TdMeBa69Y8Y @ 00:03:03])",
                    ],
                    [
                        "Configure an assistant and test a concrete workflow modification",
                        "Cuebic AI enables provider-backed AI features, reloads n8n, and asks the assistant to add an if node to an existing workflow.",
                        "Cuebic AI ([BxxP4kEqOdg @ 00:02:57])",
                    ],
                    [
                        "Package two core workflows with recurring maintenance and uptime work",
                        "The AI Blueprint teaches $1,500 setup plus $500 monthly for the starter pack, alongside a larger CRM and support automation offer.",
                        "The AI Blueprint ([1mZ0bWq9y-M @ 00:02:20])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small configuration choices that change the build",
                "body": "Use the specific shortcuts and structural choices these builders demonstrate.",
                "items": [
                    (
                        "Map first name, last name, company, and email dynamically. Marc explains that typing "
                        "the example person's name directly would repeat it on every run. "
                        "[Automate with Marc | AI Automation — syCqaV7N73s @ 00:08:38]"
                    ),
                    (
                        "Keep most processing in ordinary workflow steps and call the model where needed. "
                        "SaaS Master places a DeepSeek step inside Product Radar and estimates roughly "
                        "eight or nine cents to run that complex workflow. "
                        "[SaaS Master — TdMeBa69Y8Y @ 00:04:50]"
                    ),
                    (
                        "Label workflows prod, test, and draft. Jonas uses those labels to keep a dashboard "
                        "of over 100 workflows organized. "
                        "[Jonas | AI Tools & Automation — 4imOFZeP7nk @ 00:06:53]"
                    ),
                    (
                        "Use an existing workflow to test the assistant's editing ability. Cuebic AI asks "
                        "for an if node and shows it being added to the open workflow. "
                        "[Cuebic AI — BxxP4kEqOdg @ 00:02:57]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Define the handoff and connect the trigger",
                    "action": "Create the lead sheet and test the incoming row.",
                    "detail": (
                        "Marc uses first name, last name, company, phone, and email columns, selects the "
                        "new-row event, chooses the spreadsheet and worksheet, and checks the fetched "
                        "record before continuing. "
                        "[Automate with Marc | AI Automation — syCqaV7N73s @ 00:05:02]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Generate and map the response",
                    "action": "Feed dynamic lead fields into the AI writer and map its output into Gmail.",
                    "detail": (
                        "Marc requests an engaging email under 150 words and defines separate subject "
                        "and body outputs in Zapier so the following Gmail step can receive each "
                        "field directly. "
                        "[Automate with Marc | AI Automation — syCqaV7N73s @ 00:09:08]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Configure the self-hosted agent environment",
                    "action": "Deploy with Compose and preserve credentials and workflow data.",
                    "detail": (
                        "12_5 Tech teaches a pinned deployment, a fixed backed-up encryption key, "
                        "persistent data, seven-day execution pruning, and Groq, Gemini, or local "
                        "Ollama credentials connected to the AI Agent node. "
                        "[12_5 Tech — 0EeWohGy6RM @ 00:02:15]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Test delivery and read real usage",
                    "action": "Run the workflow against your own destination and inspect its usage meter.",
                    "detail": (
                        "Jonas tests messaging workflows on their own phone before client delivery. "
                        "AI Business Tools & Automation recommends running one real workflow for "
                        "a week on each free tier or trial and reading the usage meter. "
                        "[Jonas | AI Tools & Automation — 4imOFZeP7nk @ 00:07:08] "
                        "[AI Business Tools & Automation — PKHb0KLNOIg @ 00:06:57]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-alternative-playbooks",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Make wins the broad remote-team recommendation but loses the most frustrating build in "
                    "Owner's Bot Lab's responder test. Erin at Paired Recruiting calls Make the usual middle "
                    "ground once teams need real branching without a developer. Owner's Bot Lab instead "
                    "reports lagging text entry, an extra component to separate AI output, and a spreadsheet "
                    "lookup failure caused by a missing character in the ID. Its n8n build reached a first "
                    "working run in about ten minutes, the only clean timing, while Zapier was the smoothest "
                    "of the two builds without a clean time. The final scores were Make 76, Zapier 84, "
                    "and n8n 94. Those results sit beside the builder's stated conditions: Make came first, "
                    "n8n second, Zapier third; the n8n setup was pasted in; and part of its parsing used "
                    "copied code. Marc's independently built sales writer still ends with Zapier quickest, "
                    "Make close behind, and n8n taking more familiarity. The disagreement is therefore real "
                    "but specific: a remote-team recommendation, a timed responder exercise, and a simpler "
                    "email-writer comparison emphasize different experiences. Owner's Bot Lab itself still "
                    "recommends Zapier for getting something working tonight and n8n for technical operators "
                    "or adding more automations. Paired Recruiting [TdMOpd_cG0A @ 00:07:45]; "
                    "Owner's Bot Lab [EtiRX0GduSI @ 00:05:22]; Automate with Marc "
                    "[syCqaV7N73s @ 00:28:03]."
                ),
                (
                    "The pricing differences also need their original workflow attached. ProfitPilot's 500-lead "
                    "example has four actions, Standard-tier Zapier AI, and annual billing: $49 for Zapier, "
                    "$9 for Make, and €20 for n8n. AI Business Tools & Automation adds a fifth action "
                    "and reaches 2,500 Zapier tasks, placing its example in the stated $89 tier. It also "
                    "reports Make starting figures of $9 and about $12, explaining that country and region "
                    "affect the displayed price. Owner's Bot Lab quotes its responder at $49 annually billed "
                    "or $73.50 month-to-month on Zapier, and $12 or $16 on Make, with n8n around €20 "
                    "under annual billing. These are not identical baskets of work or identical purchase "
                    "conditions. Licensing language differs too. Fireship describes n8n as an open-source "
                    "alternative to Zapier, whereas AI Business Tools & Automation explicitly identifies "
                    "the Sustainable Use License as fair-code, permits internal business or personal use, "
                    "and describes limits on commercial redistribution plus paid enterprise features. The "
                    "useful side-by-side keeps those statements attributed instead of turning every mention "
                    "of free software into the same offer. ProfitPilot's lowest-price result belongs to its "
                    "chosen workflow and volumes; the responder's easiest billing result belongs to "
                    "Owner's Bot Lab's test. ProfitPilot [d8w8FHZJpdY @ 00:03:09]; AI Business Tools "
                    "& Automation [PKHb0KLNOIg @ 00:03:43]; Owner's Bot Lab "
                    "[EtiRX0GduSI @ 00:04:42]; Fireship [bS9R6aCVEzw @ 00:00:56]."
                ),
                (
                    "UiPath enters when the job involves documents and interfaces rather than only cloud-app "
                    "handoffs. Everyday AI Automation describes invoice processing they have personally worked "
                    "with: use document understanding and an extract-document-data activity, identify vendor, "
                    "invoice number, date, purchase order, and total, then write those values into Excel or "
                    "Google Sheets. The next stage can open a browser application, locate fields, type the "
                    "values, and click through the process. They sometimes stop before final submission "
                    "for human review. Their Make example similarly creates a Gmail draft after an OpenAI "
                    "response, whereas Marc's three-platform demonstration sends the email automatically "
                    "and separately discusses adding a person or research agent later. That is an alternative "
                    "operating design, not a dispute about whether email can be automated. LearnAI Today "
                    "also rejects an exclusive platform choice: some teams prototype in Zapier and move "
                    "heavier workloads to Make or n8n. Everyday AI Automation's broader framework is to "
                    "identify the trigger, incoming information, decisions, systems, repetitive manual work, "
                    "and useful AI role before selecting technology. UiPath therefore has a distinct place "
                    "alongside the three API-oriented builders when the actual work includes reading "
                    "documents, navigating browsers, and entering data through application interfaces. "
                    "Everyday AI Automation [SrWNK0955xw @ 00:08:03]; Automate with Marc "
                    "[syCqaV7N73s @ 00:03:27]; LearnAI Today [Pd96DxQ36U8 @ 00:07:24]."
                ),
            ],
            "table": {
                "caption": "Contrasts that should remain separate rather than becoming one universal ranking",
                "headers": ["Competing recommendation or result", "What each practitioner actually emphasizes", "Expert Source"],
                "rows": [
                    [
                        "Make is the remote-team middle ground but not every builder's easiest experience",
                        "Paired favors accessible branching for teams; Owner's Bot Lab calls Make its most frustrating responder build and scores it below Zapier and n8n.",
                        "Paired Recruiting ([TdMOpd_cG0A @ 00:07:45]); Owner's Bot Lab ([EtiRX0GduSI @ 00:05:22])",
                    ],
                    [
                        "Zapier finishes quickest for Marc while n8n earns the only clean responder timing",
                        "Marc builds a simple sales writer without code; Owner's Bot Lab reports about ten minutes for n8n after pasting setup and using copied parsing code.",
                        "Automate with Marc | AI Automation ([syCqaV7N73s @ 00:28:03]); Owner's Bot Lab ([EtiRX0GduSI @ 00:02:28])",
                    ],
                    [
                        "Two 500-lead examples produce different Zapier task tiers and prices",
                        "ProfitPilot counts four actions and 2,000 tasks; AI Business Tools & Automation counts five actions and 2,500 tasks, crossing its stated tier boundary.",
                        "ProfitPilot ([d8w8FHZJpdY @ 00:03:09]); AI Business Tools & Automation ([PKHb0KLNOIg @ 00:01:50])",
                    ],
                    [
                        "Integration counts differ across the comparison speakers and their stated figures",
                        "Simplified reports Make around 1,500-plus, Zapier 6,000-plus, and n8n 1,000-plus; LearnAI Today reports more than 3,000, 9,000, and 2,000 respectively.",
                        "Simplified ([IYV8OVFzq_c @ 00:02:03]); LearnAI Today ([Pd96DxQ36U8 @ 00:05:15])",
                    ],
                    [
                        "A generated response can become a draft or an automatically sent message",
                        "Everyday AI Automation maps the response into a Gmail draft for review; Marc's introductory writer sends automatically and discusses additional components separately.",
                        "Everyday AI Automation ([SrWNK0955xw @ 00:04:03]); Automate with Marc | AI Automation ([syCqaV7N73s @ 00:03:27])",
                    ],
                    [
                        "UiPath handles interface-based work that differs from ordinary application handoffs",
                        "Everyday AI Automation describes extracting invoice fields, writing them into spreadsheets, and using browser typing activities when the next application requires interface interaction.",
                        "Everyday AI Automation ([SrWNK0955xw @ 00:08:23])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics-checks",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Owner's Bot Lab's build exposes small failures that an attractive workflow diagram does "
                    "not show. Leaving one character out of the spreadsheet ID cost about five minutes "
                    "in Make. An n8n test fetched every row rather than one. Zapier's emergency-email field "
                    "duplicated content and had to be rebuilt, and accidentally running a test twice sent "
                    "the customer two replies. The later 20-lead exercise included fourteen ordinary jobs, "
                    "four emergencies, a blank message, and an attempt to obtain a 50% discount. All three "
                    "caught the four emergencies without false alarms or quoted prices, but Make repeated "
                    "the discount wording and received the builder's stricter 19-out-of-20 score. Changing "
                    "a spreadsheet column then left a summary blank in one tested setup, and none of "
                    "the tools emailed a failure alert. Jonas addresses those same operational categories "
                    "with duplicate-safe workflows, testing on their own phone, and a separate workflow "
                    "whose sole job is announcing another workflow's failure. Their hourly connection check "
                    "looks for WhatsApp disconnections and node problems because connections can fail quietly. "
                    "The firsthand lesson is not that a successful run proves ongoing reliability: the "
                    "builders explicitly test destinations, bad inputs, duplicated runs, and broken "
                    "connections. Owner's Bot Lab [EtiRX0GduSI @ 00:01:51]; Jonas "
                    "[4imOFZeP7nk @ 00:07:08]."
                ),
                (
                    "Marc hits a concrete credential failure while testing n8n's AI Agent: authorization fails, "
                    "they suspect a revoked API key, switch to another account, and get an output. Their "
                    "Make build also carries a procedural warning to save each module's edits, and the "
                    "received email works even though its formatting could be better. Those are different "
                    "checks: a valid connection, retained configuration, and acceptable output. Jonas adds "
                    "the hosting failure that local experiments conceal: the application stops when the "
                    "computer shuts down. Their production choice is a small server, not a permanently "
                    "assumed laptop session. 12_5 Tech calls out two further self-hosted failure mechanisms: "
                    "saved credentials breaking when a recreated container lacks the fixed encryption key, "
                    "and execution logs filling a small VPS disk without pruning. Its recap calls for "
                    "backing up the key and enabling seven-day pruning. LearnAI Today assigns updates, "
                    "backups, security, and uptime to the self-hosting operator, while distinguishing n8n "
                    "Cloud as the managed alternative. The operating burden survives the removal of a "
                    "software subscription. These speakers name specific work—credential repair, module "
                    "saving, output inspection, server continuity, and upkeep—rather than treating a free "
                    "installation as a finished client service. Automate with Marc "
                    "[syCqaV7N73s @ 00:25:05]; Jonas [4imOFZeP7nk @ 00:04:34]; 12_5 Tech "
                    "[0EeWohGy6RM @ 00:01:15]; LearnAI Today [Pd96DxQ36U8 @ 00:04:39]."
                ),
                (
                    "ProfitPilot's sharpest economics check is the AI dropdown, not the subscription headline. "
                    "It reports Standard AI by Zapier at one task, Advanced at three, and Premium at five, "
                    "with new paid-plan AI steps defaulting to Premium. In its four-action example, that "
                    "changes each run from four tasks to eight and the 500-lead monthly figure from $49 "
                    "to $89. A Premium AI step making two tool calls reaches fifteen tasks for that "
                    "step alone. ProfitPilot says to test output before switching tiers, and also notes "
                    "that Make AI features can consume multiple credits and an external OpenAI key brings "
                    "token charges. Its 2,000-lead Make example reaches exactly 10,000 credits, leaving "
                    "no headroom; extra credits are described as costing 25% more. AI Business Tools & "
                    "Automation adds that exhausted Make credits stop scenarios and queue incoming webhooks "
                    "up to the plan's storage limit. Jonas's zero-software-cost business still uses a "
                    "server around €6 monthly, while SaaS Master's Product Radar still uses a paid AI "
                    "API step despite self-hosting. Keep the speakers' categories intact: free software, "
                    "hosting expenditure, metered workflow usage, model charges, and ongoing maintenance "
                    "are not interchangeable figures. ProfitPilot [d8w8FHZJpdY @ 00:04:26]; "
                    "AI Business Tools & Automation [PKHb0KLNOIg @ 00:04:03]; Jonas "
                    "[4imOFZeP7nk @ 00:05:01]; SaaS Master [TdMeBa69Y8Y @ 00:05:41]."
                ),
            ],
            "table": {
                "caption": "Observed breakages and practitioner-reported billing traps",
                "headers": ["Failure or economic trap", "Observed effect and practitioner response", "Expert Source"],
                "rows": [
                    [
                        "A single missing spreadsheet identifier character stalled the Make responder",
                        "Owner's Bot Lab reports about five minutes lost before locating the missing character and getting the spreadsheet step to work.",
                        "Owner's Bot Lab ([EtiRX0GduSI @ 00:01:51])",
                    ],
                    [
                        "Running the same test twice sent the customer duplicate replies",
                        "Owner's Bot Lab reports the accidental duplicate; Jonas separately teaches duplicate-safe design and testing only against their own destination before delivery.",
                        "Owner's Bot Lab ([EtiRX0GduSI @ 00:03:25]); Jonas | AI Tools & Automation ([4imOFZeP7nk @ 00:07:20])",
                    ],
                    [
                        "An AI Agent test failed because its authorization did not work",
                        "Marc suspects a revoked API key, selects another connected account, reruns the node, and receives the generated email output.",
                        "Automate with Marc | AI Automation ([syCqaV7N73s @ 00:25:05])",
                    ],
                    [
                        "A recreated container can lose access to saved API credentials",
                        "12_5 Tech attributes this failure to losing the fixed encryption key and calls for backing it up alongside persistent deployment configuration.",
                        "12_5 Tech ([0EeWohGy6RM @ 00:01:15])",
                    ],
                    [
                        "Premium AI billing changes the cost of an otherwise unchanged Zapier workflow",
                        "ProfitPilot reports eight instead of four tasks per run and a $49-to-$89 monthly change at 500 leads in its calculation.",
                        "ProfitPilot ([d8w8FHZJpdY @ 00:04:49])",
                    ],
                    [
                        "Free software still leaves a server and ongoing repair responsibilities",
                        "Jonas pays around €6 monthly for hosting and sells maintenance because client automations need someone available to fix failures.",
                        "Jonas | AI Tools & Automation ([4imOFZeP7nk @ 00:05:01]); Jonas | AI Tools & Automation ([4imOFZeP7nk @ 00:08:56])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "The checks these operators perform before calling a workflow dependable",
                "body": "Check the destination, the failure path, the retained credentials, and the billing configuration.",
                "items": [
                    (
                        "Run normal, emergency, blank-message, and discount-manipulation cases; inspect actual "
                        "emails and spreadsheet fields. Owner's Bot Lab's stress test found repeated discount "
                        "wording, and its column-change test exposed a blank summary without an emailed alert. "
                        "[Owner's Bot Lab — EtiRX0GduSI @ 00:03:44] "
                        "[Owner's Bot Lab — EtiRX0GduSI @ 00:04:25]"
                    ),
                    (
                        "Make the workflow duplicate-safe, add a separate failure-notification workflow, "
                        "and check connections. Jonas reports hourly checks because connections disconnect quietly. "
                        "[Jonas | AI Tools & Automation — 4imOFZeP7nk @ 00:07:20] "
                        "[Jonas | AI Tools & Automation — 4imOFZeP7nk @ 00:07:34]"
                    ),
                    (
                        "Preserve and back up the fixed encryption key, retain workflow data, and prune "
                        "execution history after seven days in the deployment taught by 12_5 Tech. "
                        "[12_5 Tech — 0EeWohGy6RM @ 00:02:15] "
                        "[12_5 Tech — 0EeWohGy6RM @ 00:02:35]"
                    ),
                    (
                        "Inspect every Zapier AI tier and count modules or executions against actual monthly "
                        "runs. ProfitPilot says to choose the smallest plan that still leaves headroom. "
                        "[ProfitPilot — d8w8FHZJpdY @ 00:04:26] "
                        "[ProfitPilot — d8w8FHZJpdY @ 00:06:39]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        '"Most remote teams don\'t have a tool problem, they have a time problem." '
        "— Paired Recruiting (TdMOpd_cG0A @ 00:00:00)."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        (
            "Choose one repetitive process and identify its trigger, incoming information, decisions, "
            "systems, and useful AI role before selecting a platform. "
            "[Everyday AI Automation — SrWNK0955xw @ 00:11:46] "
            "[Paired Recruiting — TdMOpd_cG0A @ 00:08:58]"
        ),
        (
            "Build the lead writer with dynamically mapped contact fields, then inspect the generated "
            "subject and body before mapping them into Gmail. "
            "[Automate with Marc | AI Automation — syCqaV7N73s @ 00:08:38] "
            "[Automate with Marc | AI Automation — syCqaV7N73s @ 00:09:44]"
        ),
        (
            "Calculate tasks, credits, or executions for the actual workflow and volume; inspect the "
            "Zapier AI tier and read the usage meter after a week of real testing. "
            "[ProfitPilot — d8w8FHZJpdY @ 00:06:39] "
            "[AI Business Tools & Automation — PKHb0KLNOIg @ 00:06:57]"
        ),
        (
            "For self-hosted agents, preserve the encryption key and workflow data, enable seven-day "
            "pruning, and connect the chosen Groq, Gemini, or local Ollama credentials. "
            "[12_5 Tech — 0EeWohGy6RM @ 00:02:15] "
            "[12_5 Tech — 0EeWohGy6RM @ 00:02:35]"
        ),
        (
            "Connect instance-level MCP to Claude or configure the dashboard assistant, then test a "
            "specific creation or editing request against the n8n workspace. "
            "[SaaS Master — TdMeBa69Y8Y @ 00:03:03] "
            "[Cuebic AI — BxxP4kEqOdg @ 00:02:57]"
        ),
        (
            "Package a specific business bottleneck with maintenance, demonstrate it in a three-minute "
            "screen capture, and use the taught targeted outreach and seven-day trial offer. "
            "[The AI Blueprint — 1mZ0bWq9y-M @ 00:02:20] "
            "[The AI Blueprint — 1mZ0bWq9y-M @ 00:02:58] "
            "[The AI Blueprint — 1mZ0bWq9y-M @ 00:03:16]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Automate with Marc | AI Automation — The difference between Zapier, Make and n8n (2026) [00:02:33]",
            "url": "https://www.youtube.com/watch?v=syCqaV7N73s&t=153s",
            "relevance": "Primary practitioner testimony on building the same Google Sheets, AI writer, and email workflow across three platforms.",
        },
        {
            "title": "ProfitPilot — Zapier vs Make vs n8n: What One AI Workflow Really Costs (2026 Pricing) [00:04:26]",
            "url": "https://www.youtube.com/watch?v=d8w8FHZJpdY&t=266s",
            "relevance": "Primary practitioner testimony on AI task multipliers, billing assumptions, and the cost of the same lead workflow.",
        },
        {
            "title": "Owner's Bot Lab — I Built the Same AI Lead Responder in Zapier, Make and n8n (Only One Was Easy) [00:03:44]",
            "url": "https://www.youtube.com/watch?v=EtiRX0GduSI&t=224s",
            "relevance": "Primary practitioner testimony on responder stress tests, emergencies, blank messages, and attempted discount manipulation.",
        },
        {
            "title": "Jonas | AI Tools & Automation — I Run My AI Automation Business for $0 in Software (Zapier vs Make vs n8n) [00:06:39]",
            "url": "https://www.youtube.com/watch?v=4imOFZeP7nk&t=399s",
            "relevance": "Primary practitioner testimony on client workflow labels, testing, duplicate safety, error alerts, and connection monitoring.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "IYV8OVFzq_c",
            "title": "N8N vs Make vs Zapier (2025) - Honest Review",
            "channel": "Simplified",
            "author": "Simplified",
            "text": "The choice of platform depends on the complexity of your automations, the integrations you require, the initial skills of your team, and your budget.",
            "tip": "The choice of platform depends on the complexity of your automations, the integrations you require, the initial skills of your team, and your budget.",
            "timestamp": 236,
            "timestamp_seconds": 236,
            "timestamp_label": "[00:03:56]",
            "url": "https://www.youtube.com/watch?v=IYV8OVFzq_c&t=236s",
            "markdown": "[00:03:56](https://www.youtube.com/watch?v=IYV8OVFzq_c&t=236s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on selecting a platform by workflow complexity, integrations, skills, and budget.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "syCqaV7N73s",
            "title": "The difference between Zapier, Make and n8n (2026)",
            "channel": "Automate with Marc | AI Automation",
            "author": "Automate with Marc | AI Automation",
            "text": "If I type in Teddy Joy right here, it's going to be hardcoded for every run of this automation.",
            "tip": "If I type in Teddy Joy right here, it's going to be hardcoded for every run of this automation.",
            "timestamp": 518,
            "timestamp_seconds": 518,
            "timestamp_label": "[00:08:38]",
            "url": "https://www.youtube.com/watch?v=syCqaV7N73s&t=518s",
            "markdown": "[00:08:38](https://www.youtube.com/watch?v=syCqaV7N73s&t=518s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on dynamic mapping rather than hardcoding a sample lead.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PKHb0KLNOIg",
            "title": "Zapier vs Make vs n8n: Which Costs Less for Small Businesses? (2026)",
            "channel": "AI Business Tools & Automation",
            "author": "AI Business Tools & Automation",
            "text": "Before you commit, build one real workflow on each free tier or trial, run it for a week, and read the usage meter.",
            "tip": "Before you commit, build one real workflow on each free tier or trial, run it for a week, and read the usage meter.",
            "timestamp": 417,
            "timestamp_seconds": 417,
            "timestamp_label": "[00:06:57]",
            "url": "https://www.youtube.com/watch?v=PKHb0KLNOIg&t=417s",
            "markdown": "[00:06:57](https://www.youtube.com/watch?v=PKHb0KLNOIg&t=417s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on testing actual workflow usage before selecting a paid plan.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Pd96DxQ36U8",
            "title": "Zapier vs Make vs n8n (2026): Which Automation Tool Should You Use?",
            "channel": "LearnAI Today",
            "author": "LearnAI Today",
            "text": "Self-hosting means handling updates, backups, security, and uptime yourself.",
            "tip": "Self-hosting means handling updates, backups, security, and uptime yourself.",
            "timestamp": 279,
            "timestamp_seconds": 279,
            "timestamp_label": "[00:04:39]",
            "url": "https://www.youtube.com/watch?v=Pd96DxQ36U8&t=279s",
            "markdown": "[00:04:39](https://www.youtube.com/watch?v=Pd96DxQ36U8&t=279s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the operational responsibilities accompanying self-hosting.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "1mZ0bWq9y-M",
            "title": "How to Build an AI Automation Agency with n8n and AI Agents (2026 Masterclass)",
            "channel": "The AI Blueprint",
            "author": "The AI Blueprint",
            "text": "Two custom core workflows for a one-time setup fee of $1,500 plus $500 per month for ongoing maintenance and uptime monitoring.",
            "tip": "Two custom core workflows for a one-time setup fee of $1,500 plus $500 per month for ongoing maintenance and uptime monitoring.",
            "timestamp": 140,
            "timestamp_seconds": 140,
            "timestamp_label": "[00:02:20]",
            "url": "https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=140s",
            "markdown": "[00:02:20](https://www.youtube.com/watch?v=1mZ0bWq9y-M&t=140s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the taught starter automation package and recurring maintenance offer.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TdMOpd_cG0A",
            "title": "Zapier vs Make vs n8n: Which Automation Tool Is Best for Your Team? (HONEST REVIEW)",
            "channel": "Paired Recruiting",
            "author": "Paired Recruiting",
            "text": "In most cases, Make ends up being the best middle ground. It's flexible enough to handle real workflows, but still accessible without needing a developer.",
            "tip": "In most cases, Make ends up being the best middle ground. It's flexible enough to handle real workflows, but still accessible without needing a developer.",
            "timestamp": 465,
            "timestamp_seconds": 465,
            "timestamp_label": "[00:07:45]",
            "url": "https://www.youtube.com/watch?v=TdMOpd_cG0A&t=465s",
            "markdown": "[00:07:45](https://www.youtube.com/watch?v=TdMOpd_cG0A&t=465s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on Make as a remote-team middle ground.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "4imOFZeP7nk",
            "title": "I Run My AI Automation Business for $0 in Software (Zapier vs Make vs n8n)",
            "channel": "Jonas | AI Tools & Automation",
            "author": "Jonas | AI Tools & Automation",
            "text": "Make it duplicate safe and set up error alerts. I literally have one workflow whose only job is to tell me when another workflow fails.",
            "tip": "Make it duplicate safe and set up error alerts. I literally have one workflow whose only job is to tell me when another workflow fails.",
            "timestamp": 440,
            "timestamp_seconds": 440,
            "timestamp_label": "[00:07:20]",
            "url": "https://www.youtube.com/watch?v=4imOFZeP7nk&t=440s",
            "markdown": "[00:07:20](https://www.youtube.com/watch?v=4imOFZeP7nk&t=440s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on duplicate safety and dedicated failure alerts in client workflows.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "d8w8FHZJpdY",
            "title": "Zapier vs Make vs n8n: What One AI Workflow Really Costs (2026 Pricing)",
            "channel": "ProfitPilot",
            "author": "ProfitPilot",
            "text": "Standard costs one task, Advanced costs three, and Premium costs five. If the AI calls tools, each tool call is billed at the same rate.",
            "tip": "Standard costs one task, Advanced costs three, and Premium costs five. If the AI calls tools, each tool call is billed at the same rate.",
            "timestamp": 266,
            "timestamp_seconds": 266,
            "timestamp_label": "[00:04:26]",
            "url": "https://www.youtube.com/watch?v=d8w8FHZJpdY&t=266s",
            "markdown": "[00:04:26](https://www.youtube.com/watch?v=d8w8FHZJpdY&t=266s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on Zapier AI task multipliers and tool-call billing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "EtiRX0GduSI",
            "title": "I Built the Same AI Lead Responder in Zapier, Make and n8n (Only One Was Easy)",
            "channel": "Owner's Bot Lab",
            "author": "Owner's Bot Lab",
            "text": "All three caught four out of four emergencies, zero false alarms, zero prices quoted.",
            "tip": "All three caught four out of four emergencies, zero false alarms, zero prices quoted.",
            "timestamp": 243,
            "timestamp_seconds": 243,
            "timestamp_label": "[00:04:03]",
            "url": "https://www.youtube.com/watch?v=EtiRX0GduSI&t=243s",
            "markdown": "[00:04:03](https://www.youtube.com/watch?v=EtiRX0GduSI&t=243s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the measured emergency-handling results of the responder test.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "SrWNK0955xw",
            "title": "Zapier vs Make vs n8n vs UiPath: What You Need to Know in 2026",
            "channel": "Everyday AI Automation",
            "author": "Everyday AI Automation",
            "text": "With UiPath, we can create a workflow that reads the invoice using document understanding. We add an extract document data activity, choose the appropriate document type, and identify the fields we want extracted.",
            "tip": "With UiPath, we can create a workflow that reads the invoice using document understanding. We add an extract document data activity, choose the appropriate document type, and identify the fields we want extracted.",
            "timestamp": 503,
            "timestamp_seconds": 503,
            "timestamp_label": "[00:08:23]",
            "url": "https://www.youtube.com/watch?v=SrWNK0955xw&t=503s",
            "markdown": "[00:08:23](https://www.youtube.com/watch?v=SrWNK0955xw&t=503s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on invoice extraction and the document-processing role of UiPath.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Pz3jLYQwsX4",
            "title": "n8n vs Zapier vs Make (2026): Which AI Automation Tool Is Actually Worth It?",
            "channel": "Whizz AI",
            "author": "Whizz AI",
            "text": "If you self-host the free version, you are responsible for keeping it running, updating it, and securing it. That is a real job, even if the software itself costs nothing.",
            "tip": "If you self-host the free version, you are responsible for keeping it running, updating it, and securing it. That is a real job, even if the software itself costs nothing.",
            "timestamp": 297,
            "timestamp_seconds": 297,
            "timestamp_label": "[00:04:57]",
            "url": "https://www.youtube.com/watch?v=Pz3jLYQwsX4&t=297s",
            "markdown": "[00:04:57](https://www.youtube.com/watch?v=Pz3jLYQwsX4&t=297s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony distinguishing zero software cost from self-hosting responsibilities.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TdMeBa69Y8Y",
            "title": "n8n Self Hosted With Claude MCP - Let AI Build Your Workflows",
            "channel": "SaaS Master",
            "author": "SaaS Master",
            "text": "Head on over to settings, click on instance level MCP. Let's go ahead and enable.",
            "tip": "Head on over to settings, click on instance level MCP. Let's go ahead and enable.",
            "timestamp": 183,
            "timestamp_seconds": 183,
            "timestamp_label": "[00:03:03]",
            "url": "https://www.youtube.com/watch?v=TdMeBa69Y8Y&t=183s",
            "markdown": "[00:03:03](https://www.youtube.com/watch?v=TdMeBa69Y8Y&t=183s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on enabling instance-level MCP for AI-assisted workflow creation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "BxxP4kEqOdg",
            "title": "n8n AI Assistant & AI Agents on Self-Hosted n8n",
            "channel": "Cuebic AI",
            "author": "Cuebic AI",
            "text": "I'll open the AI assistant and ask it to add an if node to this workflow. The assistant processes the request, and there we go. The if node has been added to the workflow.",
            "tip": "I'll open the AI assistant and ask it to add an if node to this workflow. The assistant processes the request, and there we go. The if node has been added to the workflow.",
            "timestamp": 177,
            "timestamp_seconds": 177,
            "timestamp_label": "[00:02:57]",
            "url": "https://www.youtube.com/watch?v=BxxP4kEqOdg&t=177s",
            "markdown": "[00:02:57](https://www.youtube.com/watch?v=BxxP4kEqOdg&t=177s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony demonstrating an assistant modifying an existing self-hosted workflow.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "bS9R6aCVEzw",
            "title": "n8n will change your life as a developer...",
            "channel": "Fireship",
            "author": "Fireship",
            "text": "The AI agent node allows us to choose any custom model we want, as well as provide data for memory and tools for the model context protocol.",
            "tip": "The AI agent node allows us to choose any custom model we want, as well as provide data for memory and tools for the model context protocol.",
            "timestamp": 309,
            "timestamp_seconds": 309,
            "timestamp_label": "[00:05:09]",
            "url": "https://www.youtube.com/watch?v=bS9R6aCVEzw&t=309s",
            "markdown": "[00:05:09](https://www.youtube.com/watch?v=bS9R6aCVEzw&t=309s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on models, memory, and MCP tools in an n8n AI Agent node.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "0EeWohGy6RM",
            "title": "Build Free AI Agents & Workflow Automation With Zero Zapier Fees (Self-Hosted n8n + Free Groq/Gemini",
            "channel": "12_5 Tech",
            "author": "12_5 Tech",
            "text": "Enable seven-day execution pruning to protect small VPS disks.",
            "tip": "Enable seven-day execution pruning to protect small VPS disks.",
            "timestamp": 155,
            "timestamp_seconds": 155,
            "timestamp_label": "[00:02:35]",
            "url": "https://www.youtube.com/watch?v=0EeWohGy6RM&t=155s",
            "markdown": "[00:02:35](https://www.youtube.com/watch?v=0EeWohGy6RM&t=155s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on execution-history pruning in a small self-hosted deployment.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "syCqaV7N73s",
            "title": "The difference between Zapier, Make and n8n (2026)",
            "channel": "Automate with Marc | AI Automation",
            "author": "Automate with Marc | AI Automation",
            "text": "Choose Zapier if you want speed and simplicity. Choose Make if you want power without coding and choose n8n if you want full control and flexibility.",
            "tip": "Choose Zapier if you want speed and simplicity. Choose Make if you want power without coding and choose n8n if you want full control and flexibility.",
            "timestamp": 1713,
            "timestamp_seconds": 1713,
            "timestamp_label": "[00:28:33]",
            "url": "https://www.youtube.com/watch?v=syCqaV7N73s&t=1713s",
            "markdown": "[00:28:33](https://www.youtube.com/watch?v=syCqaV7N73s&t=1713s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony summarizing platform selection after the three-platform build demonstration.",
        },
    ],
}
