from __future__ import annotations

CHAPTER_1 = {
    "id": "Q1",
    "chapter_id": "Q1",
    "chapter_number": 1,
    "question_number": 1,
    "slug": "find-a-narrow-problem-worth-building-for",
    "question_prompt": "How do practitioners find narrow SaaS opportunities through existing products, boring problems, tiny utilities, and small-business case studies?",
    "kicker": "Q1 / THE BIG MONEY PLAYBOOKS",
    "title": "Find a Narrow Problem Worth Building For",
    "subtitle": "Micro-versions of established SaaS, lower-priced alternatives, boring business software, tiny integrations, Subscribr, My Ask AI, and screenshot-product case studies",
    "layout_template": "opportunity_overview",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Start where people already spend money or repeatedly do work by hand. "
        "Rob Walling reports that 48% of surveyed founders found their problem at work; "
        "Thomas turned application packaging into Packager, while Abhishek found dissatisfied "
        "Typeform users. Greg Isenberg maps workflows before automating mechanical tasks. "
        "Fomin and Brett Malinowski put distribution beside demand, not after development. "
        "Gil collected $20,000 before building Subscribr; My Ask AI reportedly collected "
        "around $5,000 before launch. But the playbooks diverge: Screenshot One's founder "
        "wants outside customers actually using the product, Nexus Research's builder favors "
        "one-time purchases, and freemium survives in some businesses while draining others. "
        "Screenshot One's near-zero early margins and Blackmagic's API-driven sale make "
        "pricing, infrastructure costs, and platform dependence part of choosing the problem."
    ),
    "key_metrics": [
        {
            "label": "Day-job problem discovery",
            "metric": "Day-job problem discovery",
            "value": "48%",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Rob Walling attributes this share to founders finding a problem at their "
                "day job in a survey of over 200 SaaS founders earning at least $1,000 monthly."
            ),
            "source": "Rob Walling ([6sgCo6fMSGY @ 00:00:58])",
        },
        {
            "label": "Subscribr pre-build sales",
            "metric": "Subscribr pre-build sales",
            "value": "$20,000",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Gil reports selling 50 lifetime licenses before building, with delivery "
                "promised in 60 days and a further two-week refund window after delivery."
            ),
            "source": "Starter Story ([7KqlwjBM_tM @ 00:05:34])",
        },
        {
            "label": "Screenshot One operating margins",
            "metric": "Screenshot One operating margins",
            "value": "40% to 60%",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "The founder reports these profit margins alongside approximately two "
                "million screenshots rendered and $3,000 to $4,000 in monthly server costs."
            ),
            "source": "Starter Story ([TCGXT7ySco8 @ 00:10:42])",
        },
        {
            "label": "Google Sheets builder milestone",
            "metric": "Google Sheets builder milestone",
            "value": "$300 MRR after roughly one year",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "AI Tomorrow Desk describes a no-code Google Sheets website builder "
                "taking roughly a year to reach this recurring-revenue milestone."
            ),
            "source": "AI Tomorrow Desk ([TzwPPvJaXCI @ 00:00:16])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Look first at work somebody already has to finish. Rob Walling reports "
                    "that 48% of surveyed founders found their opportunity at their day job, "
                    "where they already understood the workarounds, buying process, and potential "
                    "customers. Their examples were not abstract inventions: support software "
                    "missing boring operational features, repeated spreadsheet preparation, and "
                    "meeting notes written up by hand. Thomas followed that route with Packager. "
                    "Packaging an application for Microsoft Intune could take an hour, and other "
                    "IT administrators were describing the same frustration in forums. Existing "
                    "solutions felt too technical or too expensive, so Thomas built a browser-based "
                    "tool around one job: deploying applications. Zues Ordaz describes a comparable "
                    "problem inside their agency, moving between Calendly, Gmail, Typeform, Google "
                    "Calendar, and a spreadsheet to manage clients. Their proposed product grew "
                    "from that recurring copy-and-paste work, not from a search for another broad "
                    "software category. The common starting point is specific operational friction "
                    "experienced close enough to describe. Thomas also deliberately targeted smaller "
                    "businesses while competitors focused on customers with millions of devices. "
                    "That customer boundary mattered as much as the deployment feature: the product "
                    "served a smaller audience wanting a different tool, rather than attempting "
                    "to match every incumbent capability. "
                    "[6sgCo6fMSGY @ 00:01:14] [LRX8TWC2hTM @ 00:02:18] "
                    "[I-4eEpO2G0Q @ 00:01:59] [LRX8TWC2hTM @ 00:06:08]"
                ),
                (
                    "Existing spending is an invitation to investigate, not a reason to abandon "
                    "a category. Abhishek discovered that users of their earlier chatbot builder "
                    "mostly wanted conversational forms. Those customers were treating it as a "
                    "Typeform alternative, and Typeform's price increase exposed an opening. "
                    "Abhishek did not stop at cheaper pricing: they searched Twitter, Reddit, "
                    "and the incumbent's own forum for requested features the incumbent was "
                    "not providing. David and Daniel took a similar approach in AI app building. "
                    "They inspected competitors' Trustpilot reviews, public roadmaps, and Discord "
                    "communities, then listened when customers asked to turn websites into mobile "
                    "apps. Their differentiation included more output types and removing technical "
                    "language that made nontechnical customers uncomfortable. Your Average Tech "
                    "Bro describes the same rejection of originality with Nexus Research: familiar "
                    "AI document reading, combined with note-taking, aimed at college students "
                    "they knew how to reach. These founders were not claiming that being newer "
                    "was enough. Each described a concrete difference in features, accessibility, "
                    "or audience. Abhishek's advice is to find what people are searching for "
                    "before building, while David recommends starting with an industry or interest "
                    "you genuinely know and asking what the established product would look like "
                    "for people like you. "
                    "[_KaFS4Dxs5k @ 00:01:22] [Nnpz1wsTjBI @ 00:08:10] "
                    "[QBajJCMxByw @ 00:01:23] [Nnpz1wsTjBI @ 00:09:18]"
                ),
                (
                    "Distribution belongs inside the opportunity decision. Fomin looks for "
                    "problems people actively search for on YouTube, Google, and sometimes Reddit, "
                    "then asks how those people will reach the website. Their preferred examples "
                    "are deliberately ordinary: generating documents, checking information, or "
                    "converting formats. Before building, Fomin considers whether a simple video "
                    "can show the solution and whether people already watch or search for that "
                    "subject. Brett Malinowski describes an aggressive content-first version through "
                    "Study Buddy: Oliver saw a similar tool attracting millions of TikTok views, "
                    "hired a developer, and demonstrated the product filling in college homework. "
                    "Brett's point is that Oliver selected a proven content approach before "
                    "building around it. Shawn at Bootstrapper's Paradise reaches the same "
                    "distribution emphasis through quieter utilities. Sync to Sheets connects "
                    "Notion databases with Google Sheets, while Receipt AI takes a photographed "
                    "receipt, asks for its folder, and sends it to accounting software. Shawn "
                    "recommends mastering one repeatable acquisition channel rather than treating "
                    "shipping as the finish line. Their examples range from creator demonstrations "
                    "to narrow integrations, but the commercial question stays recognizable: who "
                    "needs this particular result, and which channel already gives the founder "
                    "a way to reach those people? "
                    "[8lmA9UgwNQs @ 00:02:22] [7MpAQeeep-U @ 00:03:39] "
                    "[7MpAQeeep-U @ 00:04:28] [AFXt0sgCf70 @ 00:02:03]"
                ),
            ],
            "table": {
                "caption": "Where practitioners actually found the narrow opening",
                "headers": ["Opportunity signal", "Practitioner execution", "Expert Source"],
                "rows": [
                    [
                        "Repeated work inside an industry the founder already understood",
                        "Thomas found Intune packaging complaints and built affordable browser-based application deployment.",
                        "Starter Story ([LRX8TWC2hTM @ 00:02:18])",
                    ],
                    [
                        "Existing customers repurposed an earlier product for conversational forms",
                        "Abhishek investigated Typeform dissatisfaction instead of inventing an entirely unfamiliar category.",
                        "Starter Story ([_KaFS4Dxs5k @ 00:01:22])",
                    ],
                    [
                        "Agency operations required manually connecting information across several tools",
                        "Zues described client management scattered across Calendly, Gmail, Typeform, calendars, and spreadsheets.",
                        "Zues Ordaz ([I-4eEpO2G0Q @ 00:01:59])",
                    ],
                    [
                        "People actively searched for a simple job to finish immediately",
                        "Fomin favored document generation, information checks, and conversions with visible search demand.",
                        "Fomin Unscripted ([8lmA9UgwNQs @ 00:00:56])",
                    ],
                    [
                        "A narrowly scoped integration joined two tools customers already used",
                        "Shawn described Sync to Sheets connecting Notion databases directly with Google Sheets.",
                        "Bootstrapper's Paradise ([AFXt0sgCf70 @ 00:02:34])",
                    ],
                    [
                        "Developer expertise narrowed the founder's search to API products",
                        "Screenshot One's founder chose screenshot automation after seeing numerous competitors in Google.",
                        "Starter Story ([TCGXT7ySco8 @ 00:02:31])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Abhishek gives a direct competitor-research sequence: choose a popular tool, "
                    "search Twitter and Reddit for its name followed by 'alternative,' identify "
                    "the missing feature or painful price, and approach those users with a basic "
                    "landing page explaining the replacement. Their bonus step is migration. "
                    "A customer can paste a Typeform URL into the new product's landing page "
                    "and receive a converted form within seconds. That makes the proposed switch "
                    "visible instead of leaving it as a promise. The first version was equally "
                    "stripped down: name, email, star-rating fields, and CSV export, without "
                    "Google Sheets integrations or an API. Abhishek says that version took two "
                    "weeks. David's research adds Trustpilot, public roadmaps, and competitor "
                    "Discord servers to the search surface; their customer support conversations "
                    "then supplied a specific request for mobile apps. Screenshot One's founder "
                    "adds a capacity question before committing: are there enough companies needing "
                    "the product and willing to pay enough to satisfy the founder's revenue goal? "
                    "Their example goal was $10,000 MRR. The shared mechanics are concrete: locate "
                    "buyers already using the category, identify the reason they might switch, "
                    "make the narrower offer understandable, and keep the initial feature set "
                    "close to that reason. "
                    "[_KaFS4Dxs5k @ 00:03:09] [_KaFS4Dxs5k @ 00:06:27] "
                    "[Nnpz1wsTjBI @ 00:08:10] [TCGXT7ySco8 @ 00:03:18]"
                ),
                (
                    "For workflow opportunities, Greg Isenberg starts with a subniche inside a "
                    "large market and maps the customer's day end to end. Their roofing example "
                    "moves from incoming leads through qualification, site visits, photos, "
                    "estimates, quotes, and follow-up. Greg then highlights where money changes "
                    "hands and which steps are repetitive, using anything from pen and paper "
                    "to Google Docs. The next move is to perform the workflow manually, document "
                    "it precisely, and separate judgment from mechanical tasks before turning "
                    "the latter into agent workflows. Zues makes the integration version tangible "
                    "with a Base44 client revenue tracker. Their prompt requests a login screen, "
                    "dashboard, revenue figures, leads, conversion rate, tasks, client database, "
                    "lead form, and analytics charts. After the initial build, they connect "
                    "Calendly, Google Meet, Typeform, Google Calendar, and Gmail. They describe "
                    "Calendly leads syncing hourly, Typeform responses importing daily at 8:00 "
                    "a.m., and a one-week follow-up event appearing when a lead becomes a "
                    "client. Packager shows another exact boundary: choose an application, deploy "
                    "it to Intune, and let the back-end package and upload it. Thomas names "
                    "Bubble, GitHub Actions, and Microsoft Azure as parts of that implementation. "
                    "These are specific workflows and integrations, rather than an instruction "
                    "to build a general-purpose business platform. "
                    "[9T1yWEq5kP0 @ 00:02:16] [9T1yWEq5kP0 @ 00:13:12] "
                    "[I-4eEpO2G0Q @ 00:02:57] [LRX8TWC2hTM @ 00:09:30]"
                ),
                (
                    "Gil's Subscribr sequence begins before checkout: open an X account, follow "
                    "people in the YouTube space, create useful material with existing software "
                    "skills, and use giveaways to build an email list. They reached more than "
                    "a thousand subscribers, emailed findings roughly weekly, and contacted people "
                    "individually about the proposed scriptwriting app. The pre-sale then offered "
                    "50 lifetime licenses, with the first ten cheapest and the price increasing "
                    "after each group of ten. Gil reports selling out in two or three days "
                    "and collecting $20,000 before building. They promised delivery in 60 days, "
                    "allowed refund requests before delivery, and gave buyers another two weeks "
                    "to try the delivered product. Their launch playbook uses daily benefit-focused "
                    "emails for seven days, a launch date before detailed offer disclosure, "
                    "several queued launch-day emails, ending reminders, and visibility across "
                    "social channels. Brett describes Link Drip funding development with a "
                    "$75 lifetime pre-sale promoted through Simon's YouTube audience, producing "
                    "$70,000 before development. AI Tomorrow Desk reports a smaller version "
                    "for My Ask AI: around $5,000 collected from a short product description "
                    "before launch. The offers and audiences differed, but each example put "
                    "money behind interest before the full product existed. "
                    "[7KqlwjBM_tM @ 00:04:12] [7KqlwjBM_tM @ 00:11:13] "
                    "[7MpAQeeep-U @ 00:01:19] [faUYuDkHBmc @ 00:01:06]"
                ),
            ],
            "table": {
                "caption": "Executable moves, named tools, and reported commercial details",
                "headers": ["Execution move", "Exact implementation or figure", "Expert Source"],
                "rows": [
                    [
                        "Search for dissatisfied users before presenting a replacement offer",
                        "Use Twitter and Reddit searches for the incumbent's name followed by alternative.",
                        "Starter Story ([_KaFS4Dxs5k @ 00:03:09])",
                    ],
                    [
                        "Remove migration friction while showing what the replacement produces",
                        "Abhishek lets visitors paste a Typeform URL and generate a replacement form.",
                        "Starter Story ([_KaFS4Dxs5k @ 00:03:36])",
                    ],
                    [
                        "Map the whole workflow before choosing the mechanical task",
                        "Greg highlights money-changing steps and repetitive work before designing the software wedge.",
                        "Greg Isenberg ([9T1yWEq5kP0 @ 00:03:57])",
                    ],
                    [
                        "Connect the client tracker to the customer's existing operational tools",
                        "Zues connects Calendly, Google Meet, Typeform, Google Calendar, and Gmail after building.",
                        "Zues Ordaz ([I-4eEpO2G0Q @ 00:03:38])",
                    ],
                    [
                        "Create scarcity through a limited pre-sale with increasing prices",
                        "Gil offered fifty lifetime licenses, increasing the price after each ten buyers.",
                        "Starter Story ([7KqlwjBM_tM @ 00:05:00])",
                    ],
                    [
                        "Test willingness to pay with a short description before launch",
                        "My Ask AI reportedly collected around five thousand dollars before launching the product.",
                        "AI Tomorrow Desk ([faUYuDkHBmc @ 00:01:06])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the pain, switch, and purchase concrete",
                "body": (
                    "Abhishek makes migration visible, David reads competitor complaints, "
                    "Brett emphasizes outcome demonstrations, and Gil sells benefits before launch."
                ),
                "items": [
                    (
                        "Show the switch instead of merely promising it: Abhishek's landing "
                        "page converts a pasted Typeform URL into a replacement form within "
                        "seconds. [Starter Story — _KaFS4Dxs5k @ 00:03:36]"
                    ),
                    (
                        "Read competitors' Trustpilot pages, public roadmaps, and Discord "
                        "servers, then compare those complaints with requests arriving in "
                        "your own support chat. [Starter Story — Nnpz1wsTjBI @ 00:08:10]"
                    ),
                    (
                        "Demonstrate the customer's desired outcome rather than making only "
                        "a product tutorial: Brett describes Castmagic appearing inside videos "
                        "about creating content across platforms. "
                        "[Brett Malinowski — 7MpAQeeep-U @ 00:08:24]"
                    ),
                    (
                        "Warm the pre-sale with daily emails for seven days, emphasizing "
                        "benefits; announce the date before revealing the details and queue "
                        "launch-day messages and ending reminders. "
                        "[Starter Story — 7KqlwjBM_tM @ 00:11:13]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Locate the repeated operational problem",
                    "action": "Audit frustrating tools and manual processes in familiar work.",
                    "detail": (
                        "Rob asks which daily tools frustrate you or coworkers, which manual "
                        "processes should be automated, and whether incumbent tools are truly "
                        "clunky rather than merely disliked. "
                        "[Rob Walling — 6sgCo6fMSGY @ 00:06:17]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Find the dissatisfied buyer",
                    "action": "Search a popular product's alternatives and missing features.",
                    "detail": (
                        "Follow Abhishek's sequence: search Twitter and Reddit for the "
                        "product plus alternative, identify the gap, and contact those "
                        "users with a basic landing page explaining the solution. "
                        "[Starter Story — _KaFS4Dxs5k @ 00:03:09]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Identify the acquisition route",
                    "action": "Work out how customers will find the product before building.",
                    "detail": (
                        "Fomin asks whether a simple video can demonstrate the solution, "
                        "whether people already watch such videos, and whether they "
                        "search for the problem on YouTube. "
                        "[Fomin Unscripted — 8lmA9UgwNQs @ 00:02:22]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Put a purchase behind the interest",
                    "action": "Calculate the pre-sale target and present the offer.",
                    "detail": (
                        "Gil worked backward from needing about $20,000 for roughly three "
                        "months of living costs to fifty buyers and the email audience "
                        "needed to reach them, then ran the pre-sale. "
                        "[Starter Story — 7KqlwjBM_tM @ 00:10:23]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "The founders do not use the same finish line for validation. Gil argues "
                    "that friendly feedback and hypothetical willingness to pay can send a "
                    "builder into months of development with false confidence. Their preferred "
                    "test is collecting money before building. Screenshot One's founder draws "
                    "a sharper distinction between support and use: people can even pay for "
                    "a nonexistent product because they are nice, yet that does not establish "
                    "that the finished software helps them. Their ultimate validation is at "
                    "least ten paying customers from outside the founder's network who actually "
                    "use the product. Rob Walling describes an earlier conversational test for "
                    "Drip: they asked seventeen other founders about the problem, received "
                    "ten or eleven positive answers, and then began building. BigIdeasDB gives "
                    "another threshold: speak with ten people, proceed when three name a "
                    "price, launch the smallest working version, and charge from day one. "
                    "Those approaches put different weight on conversation, payment, and observed "
                    "use. Gil's pre-sale also included a delivery commitment and refund terms; "
                    "Screenshot One's standard specifically excludes purchases made merely to "
                    "support the founder. Treat these as different practitioner tests rather "
                    "than replacing their distinctions with a single universal customer count "
                    "or a promise that enthusiastic interviews settle the business. "
                    "[7KqlwjBM_tM @ 00:07:52] [TCGXT7ySco8 @ 00:03:49] "
                    "[6sgCo6fMSGY @ 00:25:54] [BBgfgbj170o @ 00:10:06]"
                ),
                (
                    "Free access and recurring billing split the playbooks just as clearly. "
                    "Your Average Tech Bro says forever-free access produced weak conversion "
                    "in their own apps and recommends a short trial followed by paid access. "
                    "They also prefer one-time purchases where possible: on Perfect Interview, "
                    "they recall roughly 0.5% conversion for a subscription against about "
                    "1.2% to 1.3% for a same-priced one-time offer. Abhishek runs the opposite "
                    "model for the Typeform alternative, reporting more than 90% of features "
                    "available free, around 35,000 registered users, roughly 500 paying customers, "
                    "and conversion between about 1.5% and less than 2%. David reports no "
                    "free users for Shipper, explaining that the expensive service directs "
                    "its money toward a better product for paying customers. AI Tomorrow Desk "
                    "describes My Ask AI with a free-forever plan for one assistant and "
                    "paid plans offering more assistants, content, and branding removal. "
                    "These are not interchangeable pricing prescriptions. The same conversation "
                    "about narrow products contains a paid-only AI builder, a generous free "
                    "form builder, a customer-service chatbot with a free entry tier, and "
                    "a founder reporting better conversion from one-time purchases. The "
                    "reported conversion figures belong to those particular products and "
                    "offers; the founders themselves chose different ways to collect revenue. "
                    "[QBajJCMxByw @ 00:05:36] [_KaFS4Dxs5k @ 00:07:14] "
                    "[Nnpz1wsTjBI @ 00:02:13] [faUYuDkHBmc @ 00:01:44]"
                ),
                (
                    "Even the headline economics differ across the commentators. BigIdeasDB "
                    "reports 3,787 startups with active revenue, a $4,298 monthly average, "
                    "a $145 median, and 6.1% clearing $10,000 a month. Zues opens with "
                    "an analysis of more than 8,000 micro-SaaS businesses and a $500 monthly "
                    "median. Shawn instead describes the median profitable micro-SaaS as "
                    "about $4,200 MRR. Keep each figure attached to its speaker and stated "
                    "population rather than treating all three as the same benchmark. "
                    "The small-business examples also resist a single growth timetable. "
                    "AI Tomorrow Desk describes a Google Sheets no-code website builder "
                    "taking roughly a year to reach $300 MRR, with a free tier and "
                    "paid options at $29 and $49 monthly. BigIdeasDB contrasts Submagic "
                    "reaching a million dollars in annual revenue within three months "
                    "with Bannerbear taking about five years to reach that level. Their "
                    "strategic alternatives are explicit too: build near AI or developer "
                    "tools for a tailwind, or choose a slower category and pursue less "
                    "competition. Shawn emphasizes a focused integration with a repeatable "
                    "channel, while Zues proposes selling an agency dashboard. The shared "
                    "narrow-product idea therefore contains very different reported revenue "
                    "distributions, customer types, product shapes, and development histories. "
                    "[BBgfgbj170o @ 00:01:03] [I-4eEpO2G0Q @ 00:00:00] "
                    "[AFXt0sgCf70 @ 00:00:58] [TzwPPvJaXCI @ 00:00:16]"
                ),
            ],
            "table": {
                "caption": "Different practitioner choices, kept side by side",
                "headers": ["Decision", "Contrasting practitioner positions", "Expert Source"],
                "rows": [
                    [
                        "Decide whether money before delivery establishes sufficient buying interest",
                        "Gil rejects hypothetical willingness to pay and collects money before building the product.",
                        "Starter Story ([7KqlwjBM_tM @ 00:08:08])",
                    ],
                    [
                        "Decide whether payment must be accompanied by actual outside usage",
                        "Screenshot One's founder wants ten paying outsiders using the software, not supportive acquaintances.",
                        "Starter Story ([TCGXT7ySco8 @ 00:03:49])",
                    ],
                    [
                        "Choose whether a generous free tier belongs in the offer",
                        "Abhishek reports over ninety percent of features free and roughly five hundred paying customers.",
                        "Starter Story ([_KaFS4Dxs5k @ 00:07:14])",
                    ],
                    [
                        "Choose whether limited resources justify removing forever-free product access",
                        "Your Average Tech Bro favors short trials after experiencing weak conversion from free access.",
                        "Your Average Tech Bro ([QBajJCMxByw @ 00:05:36])",
                    ],
                    [
                        "Choose between a recurring subscription and a one-time purchase offer",
                        "Perfect Interview reportedly converted about 0.5% on subscriptions versus 1.2% to 1.3% one-time.",
                        "Your Average Tech Bro ([QBajJCMxByw @ 00:07:07])",
                    ],
                    [
                        "Choose between a fast-growing category and a slower competitive environment",
                        "BigIdeasDB presents AI or developer-tool tailwinds alongside sharper products in slower analytics markets.",
                        "BigIdeasDB ([BBgfgbj170o @ 00:09:17])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "The most expensive-looking mistake in these accounts is often building "
                    "the wrong thing for too long. Your Average Tech Bro recalls six or "
                    "seven failed apps across the first two years, followed by a change "
                    "toward proven categories and deliberate marketing. They describe the "
                    "engineering trap directly: adding features feels productive even when "
                    "there are no users and no revenue. Screenshot One's founder spent "
                    "five months preparing the first launch because they wanted everything "
                    "perfect, then called that a mistake. Their later approach aims for "
                    "one month or less, starts with one small feature, lets friends click "
                    "through it for breakage, and reaches prospective customers before "
                    "building out the surrounding machinery. David's Shipper story gives "
                    "the other side of early shipping. The initial version broke frequently; "
                    "the first two months were the toughest, and confidence in the product "
                    "arrived around month three. By months five and six, David says the "
                    "team was shipping features competitors lacked. These founders do not "
                    "describe a polished first release as the prerequisite for finding "
                    "buyers. They describe wasted time in perfectionism, a rough product "
                    "that needed improvement, and the need to put marketing and customer "
                    "contact beside the engineering work rather than indefinitely behind it. "
                    "[QBajJCMxByw @ 00:00:22] [QBajJCMxByw @ 00:02:11] "
                    "[TCGXT7ySco8 @ 00:04:19] [Nnpz1wsTjBI @ 00:05:04]"
                ),
                (
                    "A small product does not automatically produce cheap delivery. Screenshot "
                    "One's founder initially chose $7 monthly because $5 felt too cheap, "
                    "then discovered margins were almost zero. They reduced the free plan "
                    "and raised prices. Later, with around two million screenshots rendered, "
                    "they report server costs of $3,000 to $4,000 monthly, total expenses "
                    "around $4,500, and profit margins between 40% and 60%. Gil's "
                    "Subscribr has a different cost center: around $3,500 monthly in AI "
                    "compute, about $2,000 in advertising, and another $1,500 for items "
                    "including scraping, hosting, and email. Gil also says the first ten "
                    "pre-sale buyers might not even have been profitable at their introductory "
                    "offer, although the broader pre-sale funded the build. Shawn describes "
                    "a much lighter operating profile for Sync to Sheets, where the "
                    "largest monthly bill was under $90 for email infrastructure. Tightening "
                    "that product's free-plan limits reportedly lifted revenue from $5,000 "
                    "to more than $8,000. These accounts put concrete operating costs "
                    "beside the attractive revenue headlines. The founders changed free "
                    "limits, prices, or spending priorities when those economics demanded "
                    "it; Gil explicitly favors profit over growth and warns about expensive "
                    "agencies and distracting product directions eating into that profit. "
                    "[TCGXT7ySco8 @ 00:09:04] [TCGXT7ySco8 @ 00:10:42] "
                    "[7KqlwjBM_tM @ 00:13:45] [AFXt0sgCf70 @ 00:02:50]"
                ),
                (
                    "Customer fit and platform dependence can reverse an apparently working "
                    "opportunity. Screenshot One's cancellation form produced vague answers, "
                    "so the founder inspected each departing customer's company and use case, "
                    "then emailed a specific yes-or-no question about the suspected reason. "
                    "Those conversations revealed customers expecting a no-code product. "
                    "The founder changed the copy to emphasize developers and the need "
                    "to write integration code, reporting monthly churn moving from about "
                    "11% toward 7%. AI Tomorrow Desk recounts a different reversal for "
                    "Tony's Blackmagic. A Twitter profile progress bar became a more "
                    "useful product after adding a Chrome sidebar with analytics and "
                    "CRM features, but Twitter API pricing changes later forced a sale. "
                    "The account puts Blackmagic at $14,000 MRR when it sold for "
                    "$128,000 because API access had become too expensive. Gil's "
                    "pre-sale carried another explicit exposure: if the product was "
                    "not delivered successfully, buyers could ask for their money "
                    "back, and the founder had committed to a 60-day build. Each "
                    "case names a real pressure point rather than a generic warning: "
                    "the wrong customer expectation, a changed platform bill, or "
                    "cash collected against an undelivered product. Finding the "
                    "narrow problem includes understanding the particular promises "
                    "and dependencies attached to solving it. "
                    "[TCGXT7ySco8 @ 00:07:15] [TCGXT7ySco8 @ 00:07:59] "
                    "[VqUDhVcVrA4 @ 00:02:05] [7KqlwjBM_tM @ 00:05:34]"
                ),
            ],
            "table": {
                "caption": "Reported mistakes, reversals, and operating constraints",
                "headers": ["Observed trap", "Reported consequence or response", "Expert Source"],
                "rows": [
                    [
                        "Repeatedly building applications without a working market and distribution approach",
                        "Your Average Tech Bro recalls six or seven failed apps before changing strategy.",
                        "Your Average Tech Bro ([QBajJCMxByw @ 00:00:22])",
                    ],
                    [
                        "Delaying the first launch while attempting to make everything perfect",
                        "Screenshot One took five months initially; the founder now aims substantially shorter.",
                        "Starter Story ([TCGXT7ySco8 @ 00:04:19])",
                    ],
                    [
                        "Choosing an entry price without enough room for delivery costs",
                        "Screenshot One's early seven-dollar plan had almost zero margins, prompting pricing changes.",
                        "Starter Story ([TCGXT7ySco8 @ 00:09:04])",
                    ],
                    [
                        "Attracting customers who expected a different kind of product",
                        "Screenshot One emphasized developer integration after discovering customers had expected no-code functionality.",
                        "Starter Story ([TCGXT7ySco8 @ 00:07:59])",
                    ],
                    [
                        "Depending on platform access whose pricing later changed materially",
                        "AI Tomorrow Desk reports Blackmagic sold for $128,000 after Twitter API costs increased.",
                        "AI Tomorrow Desk ([VqUDhVcVrA4 @ 00:02:05])",
                    ],
                    [
                        "Collecting pre-sale money while still owing delivery and refund options",
                        "Gil committed to sixty-day delivery and another two weeks for customers to request refunds.",
                        "Starter Story ([7KqlwjBM_tM @ 00:05:34])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks drawn from the founders' actual pressure points",
                "body": (
                    "Use Rob's outside-demand check, Fomin's traffic question, Screenshot "
                    "One's margin reversal, and Gil's delivery commitment before copying the headline."
                ),
                "items": [
                    (
                        "Check that the problem exists beyond your own workplace. Rob "
                        "warns that an employer can be uniquely dysfunctional and says "
                        "to validate outside that bubble. "
                        "[Rob Walling — 6sgCo6fMSGY @ 00:05:32]"
                    ),
                    (
                        "Name where customers will come from before spending time building. "
                        "Fomin puts demand and traffic ahead of development, rather than "
                        "assuming an impressive product will attract buyers. "
                        "[Fomin Unscripted — 8lmA9UgwNQs @ 00:03:11]"
                    ),
                    (
                        "Check the price against the delivery economics. Screenshot One's "
                        "founder reduced the free plan and raised prices after the early "
                        "$7 offer left almost zero margins. "
                        "[Starter Story — TCGXT7ySco8 @ 00:09:04]"
                    ),
                    (
                        "Treat a pre-sale as a delivery commitment. Gil's $20,000 came "
                        "with a 60-day delivery promise and refund access continuing "
                        "for two weeks after delivery. "
                        "[Starter Story — 7KqlwjBM_tM @ 00:05:34]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        '"Don\'t tell me your idea, tell me what problem it solves." '
        "— Rob Walling (6sgCo6fMSGY @ 00:01:14)."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        (
            "List frustrating daily tools and manual processes from work, then "
            "check whether the incumbent is genuinely clunky rather than simply "
            "not your preference. [Rob Walling — 6sgCo6fMSGY @ 00:06:17]"
        ),
        (
            "Search Twitter and Reddit for a popular product plus alternative, "
            "identify the missing feature or painful pricing, and explain the "
            "replacement on a basic landing page. "
            "[Starter Story — _KaFS4Dxs5k @ 00:03:09]"
        ),
        (
            "Map the customer's workflow end to end, highlight where money "
            "changes hands, and identify repetitive mechanical steps. "
            "[Greg Isenberg — 9T1yWEq5kP0 @ 00:03:57]"
        ),
        (
            "Choose the audience and distribution approach before building; "
            "Nexus Research's builder chose college students because they "
            "knew how to make content for that audience. "
            "[Your Average Tech Bro — QBajJCMxByw @ 00:04:21]"
        ),
        (
            "Build an email relationship with useful material and weekly "
            "communication, then work backward from the funding target to "
            "the pre-sale buyer count. "
            "[Starter Story — 7KqlwjBM_tM @ 00:09:36]"
        ),
        (
            "Look for ten paying customers outside your network who actually "
            "use the product, then focus features and marketing on customers "
            "like them. [Starter Story — TCGXT7ySco8 @ 00:11:20]"
        ),
    ],
    "statutory_citations": [
        {
            "title": (
                "Rob Walling — Give Me 36 Minutes and I'll Teach You How to Find "
                "$1M SaaS Ideas [00:01:14]"
            ),
            "url": "https://www.youtube.com/watch?v=6sgCo6fMSGY&t=74s",
            "relevance": (
                "Primary practitioner testimony on finding commercial problems "
                "inside existing work rather than starting with abstract ideas."
            ),
        },
        {
            "title": (
                "Starter Story — I Copied a $100M SaaS, Undercut Their Prices, "
                "and Hit $10K/Month [00:03:09]"
            ),
            "url": "https://www.youtube.com/watch?v=_KaFS4Dxs5k&t=189s",
            "relevance": (
                "Primary practitioner testimony on alternative searches, "
                "unserved pain points, landing pages, and migration."
            ),
        },
        {
            "title": (
                "Starter Story — How I Built It: $30K/month Micro-SaaS "
                "(Subscribr Breakdown) [00:05:34]"
            ),
            "url": "https://www.youtube.com/watch?v=7KqlwjBM_tM&t=334s",
            "relevance": (
                "Primary practitioner testimony on collecting pre-sale revenue "
                "before development and committing to delivery and refunds."
            ),
        },
        {
            "title": "Starter Story — How I Built It: $12K/Month Micro SaaS [00:10:42]",
            "url": "https://www.youtube.com/watch?v=TCGXT7ySco8&t=642s",
            "relevance": (
                "Primary practitioner testimony on screenshot delivery costs "
                "and the operating margins behind a narrow API business."
            ),
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "9T1yWEq5kP0",
            "title": "SaaS is minting millionaires again (here's how)",
            "channel": "Greg Isenberg",
            "author": "Greg Isenberg",
            "text": (
                "You're going to want to document every step precisely. "
                "You're going to want to separate judgment from mechanical tasks."
            ),
            "tip": (
                "You're going to want to document every step precisely. "
                "You're going to want to separate judgment from mechanical tasks."
            ),
            "timestamp": 792,
            "timestamp_seconds": 792,
            "timestamp_label": "[00:13:12]",
            "url": "https://www.youtube.com/watch?v=9T1yWEq5kP0&t=792s",
            "markdown": "[00:13:12](https://www.youtube.com/watch?v=9T1yWEq5kP0&t=792s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on documenting workflows before automating mechanical tasks.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "7MpAQeeep-U",
            "title": "5 Micro SaaS Making $100,000/Month (Ai + No Code)",
            "channel": "Brett Malinowski",
            "author": "Brett Malinowski",
            "text": (
                "He doesn't choose a product and then figure out how to sell it. "
                "First he finds a proven content strategy and then he builds a product around it."
            ),
            "tip": (
                "He doesn't choose a product and then figure out how to sell it. "
                "First he finds a proven content strategy and then he builds a product around it."
            ),
            "timestamp": 268,
            "timestamp_seconds": 268,
            "timestamp_label": "[00:04:28]",
            "url": "https://www.youtube.com/watch?v=7MpAQeeep-U&t=268s",
            "markdown": "[00:04:28](https://www.youtube.com/watch?v=7MpAQeeep-U&t=268s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner account of selecting a content strategy before the product.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Nnpz1wsTjBI",
            "title": "I Built A Micro-Version Of A $1B SaaS. Now I Make $50K/Month",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": (
                "We looked at all of our competitors' Trustpilot pages. "
                "We looked at their public roadmaps, and we've joined their Discord servers."
            ),
            "tip": (
                "We looked at all of our competitors' Trustpilot pages. "
                "We looked at their public roadmaps, and we've joined their Discord servers."
            ),
            "timestamp": 490,
            "timestamp_seconds": 490,
            "timestamp_label": "[00:08:10]",
            "url": "https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=490s",
            "markdown": "[00:08:10](https://www.youtube.com/watch?v=Nnpz1wsTjBI&t=490s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on finding differentiation through competitor communities and reviews.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "_KaFS4Dxs5k",
            "title": "I Copied a $100M SaaS, Undercut Their Prices, and Hit $10K/Month",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": (
                "Step one, you look for a popular tool and search social platforms "
                "like Twitter and Reddit with keywords like X alternative."
            ),
            "tip": (
                "Step one, you look for a popular tool and search social platforms "
                "like Twitter and Reddit with keywords like X alternative."
            ),
            "timestamp": 189,
            "timestamp_seconds": 189,
            "timestamp_label": "[00:03:09]",
            "url": "https://www.youtube.com/watch?v=_KaFS4Dxs5k&t=189s",
            "markdown": "[00:03:09](https://www.youtube.com/watch?v=_KaFS4Dxs5k&t=189s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on locating buyers actively seeking an incumbent replacement.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8lmA9UgwNQs",
            "title": "how to find saas ideas worth $10,000,000 (steal this method)",
            "channel": "Fomin Unscripted",
            "author": "Fomin Unscripted",
            "text": (
                "Before I build anything, I want to know where my customers "
                "are going to come from."
            ),
            "tip": (
                "Before I build anything, I want to know where my customers "
                "are going to come from."
            ),
            "timestamp": 142,
            "timestamp_seconds": 142,
            "timestamp_label": "[00:02:22]",
            "url": "https://www.youtube.com/watch?v=8lmA9UgwNQs&t=142s",
            "markdown": "[00:02:22](https://www.youtube.com/watch?v=8lmA9UgwNQs&t=142s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on evaluating acquisition before development.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "I-4eEpO2G0Q",
            "title": "The Micro SaaS Business Almost Nobody Is Building (Until Now)",
            "channel": "Zues Ordaz",
            "author": "Zues Ordaz",
            "text": (
                "I run an agency and every month I was jumping between five "
                "different platforms just to manage one client."
            ),
            "tip": (
                "I run an agency and every month I was jumping between five "
                "different platforms just to manage one client."
            ),
            "timestamp": 119,
            "timestamp_seconds": 119,
            "timestamp_label": "[00:01:59]",
            "url": "https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=119s",
            "markdown": "[00:01:59](https://www.youtube.com/watch?v=I-4eEpO2G0Q&t=119s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Firsthand agency workflow frustration behind a client revenue tracker.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "6sgCo6fMSGY",
            "title": "Give Me 36 Minutes and I'll Teach You How to Find $1M SaaS Ideas",
            "channel": "Rob Walling",
            "author": "Rob Walling",
            "text": "Don't tell me your idea, tell me what problem it solves.",
            "tip": "Don't tell me your idea, tell me what problem it solves.",
            "timestamp": 74,
            "timestamp_seconds": 74,
            "timestamp_label": "[00:01:14]",
            "url": "https://www.youtube.com/watch?v=6sgCo6fMSGY&t=74s",
            "markdown": "[00:01:14](https://www.youtube.com/watch?v=6sgCo6fMSGY&t=74s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner framing for finding a commercial problem before choosing software.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "LRX8TWC2hTM",
            "title": "I Make $60K/Month From the Most Boring SaaS on the Internet",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": (
                "It can sometimes take an hour to successfully package an application "
                "and verify that it's going to install."
            ),
            "tip": (
                "It can sometimes take an hour to successfully package an application "
                "and verify that it's going to install."
            ),
            "timestamp": 138,
            "timestamp_seconds": 138,
            "timestamp_label": "[00:02:18]",
            "url": "https://www.youtube.com/watch?v=LRX8TWC2hTM&t=138s",
            "markdown": "[00:02:18](https://www.youtube.com/watch?v=LRX8TWC2hTM&t=138s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on the repetitive Intune packaging problem behind Packager.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "7KqlwjBM_tM",
            "title": "How I Built It: $30K/month Micro-SaaS (Subscribr Breakdown)",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": "I made my first $20,000 before the idea was even built.",
            "tip": "I made my first $20,000 before the idea was even built.",
            "timestamp": 334,
            "timestamp_seconds": 334,
            "timestamp_label": "[00:05:34]",
            "url": "https://www.youtube.com/watch?v=7KqlwjBM_tM&t=334s",
            "markdown": "[00:05:34](https://www.youtube.com/watch?v=7KqlwjBM_tM&t=334s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on funding Subscribr through pre-build purchases.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "BBgfgbj170o",
            "title": "8 Micro SaaS Examples in 2026 That Make $1M+ a Year (Verified)",
            "channel": "BigIdeasDB",
            "author": "BigIdeasDB",
            "text": (
                "The average across those is $4,298 a month and the median is $145 a month."
            ),
            "tip": (
                "The average across those is $4,298 a month and the median is $145 a month."
            ),
            "timestamp": 63,
            "timestamp_seconds": 63,
            "timestamp_label": "[00:01:03]",
            "url": "https://www.youtube.com/watch?v=BBgfgbj170o&t=63s",
            "markdown": "[00:01:03](https://www.youtube.com/watch?v=BBgfgbj170o&t=63s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Attributed revenue distribution for startups reporting active revenue.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "QBajJCMxByw",
            "title": "5 Lessons I Learned Building A $400/month Micro-SaaS Side Hustle",
            "channel": "Your Average Tech Bro",
            "author": "Your Average Tech Bro",
            "text": (
                "I do not build a product unless I can figure out the distribution strategy first."
            ),
            "tip": (
                "I do not build a product unless I can figure out the distribution strategy first."
            ),
            "timestamp": 261,
            "timestamp_seconds": 261,
            "timestamp_label": "[00:04:21]",
            "url": "https://www.youtube.com/watch?v=QBajJCMxByw&t=261s",
            "markdown": "[00:04:21](https://www.youtube.com/watch?v=QBajJCMxByw&t=261s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on changing from feature-first building to distribution-first selection.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "AFXt0sgCf70",
            "title": "Micro-SaaS is About to Explode | Here's Why",
            "channel": "Bootstrapper's Paradise",
            "author": "Bootstrapper's Paradise",
            "text": (
                "It's a Google Workspace add-on that syncs Notion databases with "
                "Google Sheets. That's it, one focused integration."
            ),
            "tip": (
                "It's a Google Workspace add-on that syncs Notion databases with "
                "Google Sheets. That's it, one focused integration."
            ),
            "timestamp": 154,
            "timestamp_seconds": 154,
            "timestamp_label": "[00:02:34]",
            "url": "https://www.youtube.com/watch?v=AFXt0sgCf70&t=154s",
            "markdown": "[00:02:34](https://www.youtube.com/watch?v=AFXt0sgCf70&t=154s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner account of a narrow integration rather than a horizontal platform.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "VqUDhVcVrA4",
            "title": "From Zero to $45K MRR Micro SaaS: Solopreneur SaaS Success Story",
            "channel": "AI Tomorrow Desk",
            "author": "AI Tomorrow Desk",
            "text": (
                "With the Twitter API pricing change they were forced to sell Blackmagic, "
                "which was doing 14K MRR at the time."
            ),
            "tip": (
                "With the Twitter API pricing change they were forced to sell Blackmagic, "
                "which was doing 14K MRR at the time."
            ),
            "timestamp": 125,
            "timestamp_seconds": 125,
            "timestamp_label": "[00:02:05]",
            "url": "https://www.youtube.com/watch?v=VqUDhVcVrA4&t=125s",
            "markdown": "[00:02:05](https://www.youtube.com/watch?v=VqUDhVcVrA4&t=125s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Reported platform-pricing reversal affecting an established narrow product.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "faUYuDkHBmc",
            "title": "This Micro SaaS Does 14K MRR. Micro SaaS Case Study",
            "channel": "AI Tomorrow Desk",
            "author": "AI Tomorrow Desk",
            "text": (
                "They got around five thousand dollars in pre-sales for the product "
                "prior to launching based on just a short description of what it would do."
            ),
            "tip": (
                "They got around five thousand dollars in pre-sales for the product "
                "prior to launching based on just a short description of what it would do."
            ),
            "timestamp": 66,
            "timestamp_seconds": 66,
            "timestamp_label": "[00:01:06]",
            "url": "https://www.youtube.com/watch?v=faUYuDkHBmc&t=66s",
            "markdown": "[00:01:06](https://www.youtube.com/watch?v=faUYuDkHBmc&t=66s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Reported pre-sale validation for My Ask AI before product launch.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TzwPPvJaXCI",
            "title": "From Zero to $300 MRR - Micro SaaS Stories",
            "channel": "AI Tomorrow Desk",
            "author": "AI Tomorrow Desk",
            "text": (
                "The product is a no-code builder for Google Sheets and took "
                "them roughly a year to hit this milestone."
            ),
            "tip": (
                "The product is a no-code builder for Google Sheets and took "
                "them roughly a year to hit this milestone."
            ),
            "timestamp": 16,
            "timestamp_seconds": 16,
            "timestamp_label": "[00:00:16]",
            "url": "https://www.youtube.com/watch?v=TzwPPvJaXCI&t=16s",
            "markdown": "[00:00:16](https://www.youtube.com/watch?v=TzwPPvJaXCI&t=16s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Reported small-business timeline to a $300 recurring-revenue milestone.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TCGXT7ySco8",
            "title": "How I Built It: $12K/Month Micro SaaS",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": (
                "Once you have at least ten paying customers from outside your network "
                "and you didn't know them, they just came and bought your product "
                "and use it, that's for me ultimate validation."
            ),
            "tip": (
                "Once you have at least ten paying customers from outside your network "
                "and you didn't know them, they just came and bought your product "
                "and use it, that's for me ultimate validation."
            ),
            "timestamp": 244,
            "timestamp_seconds": 244,
            "timestamp_label": "[00:04:04]",
            "url": "https://www.youtube.com/watch?v=TCGXT7ySco8&t=244s",
            "markdown": "[00:04:04](https://www.youtube.com/watch?v=TCGXT7ySco8&t=244s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony distinguishing supportive purchases from outside paying usage.",
        },
    ],
}
