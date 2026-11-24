from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "build-around-chrome-shopify-and-existing-platforms",
    "question_prompt": "What do Chrome-extension, Data Fetcher, and Shopify-app practitioners show about building small products within existing software ecosystems?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Build Around Chrome, Shopify, and Existing Platforms",
    "subtitle": "Chrome-extension businesses, Data Fetcher, spreadsheet-to-Shopify automation, merchant subscription apps, Shopify App Store growth, app portfolios, and an app-flipping case study",
    "layout_template": "tool_resource_directory",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Build where customers already work, then remove a specific piece of friction. "
        "Jack turned client spreadsheets into Profit AI; Andy adapted an established Google Sheets pattern to Airtable; "
        "Superpower ChatGPT added missing features inside an existing interface. Shopify operators repeatedly emphasize "
        "merchant research, distribution, useful differentiation, and customer support. Their economics vary sharply: "
        "Data Fetcher reports $23,000 monthly revenue, while Vlad describes moving a small acquisition from $130 to $200 MRR. "
        "Free launches, paid upgrades, newsletters, affiliate partnerships, and acquisitions offer different routes to revenue. "
        "The disagreements matter: Andy avoids crowded AI platforms, while Superpower built on ChatGPT; Essential Apps "
        "integrates closely with Shopify, while Delight Chat pursues independence. Firsthand failures expose weak validation, "
        "delayed user testing, churn, support burdens, and distracting expansion."
    ),
    "key_metrics": [
        {
            "label": "Data Fetcher recurring revenue",
            "metric": "Data Fetcher recurring revenue",
            "value": "$23,000 per month; 600 paying customers",
            "confidence": "attributed_practitioner_claim",
            "context": "Andy reports these figures while describing Data Fetcher as a solo-founder business.",
            "source": "Starter Story ([NvtsM8Nk72c @ 00:00:35])",
        },
        {
            "label": "Profit AI app and services revenue",
            "metric": "Profit AI app and services revenue",
            "value": "30K MRR for the app; just under 40K MRR for services",
            "confidence": "attributed_practitioner_claim",
            "context": "Jack separates app revenue from services and reports $147,000 made since the December launch.",
            "source": "Starter Story ([d8PdJJcEtE0 @ 00:00:59])",
        },
        {
            "label": "Kaching profitability",
            "metric": "Kaching profitability",
            "value": "90% profitable",
            "confidence": "attributed_practitioner_claim",
            "context": "Ericas reports this profitability while describing the Shopify app business and its portfolio.",
            "source": "Starter Story ([vLLBzUZr6-s @ 00:01:26])",
        },
        {
            "label": "Easy Coming Soon acquisition growth",
            "metric": "Easy Coming Soon acquisition growth",
            "value": "$130 to $200 MRR in less than a month",
            "confidence": "attributed_practitioner_claim",
            "context": "Ruth states the acquisition's starting and subsequent MRR, and Vlad confirms the figures and timeframe.",
            "source": "Ruth and Eric ([8n1RiwLpGK8 @ 00:00:55])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Start with work somebody already does, not an entirely new destination they must learn to visit. "
                    "Jack built spreadsheets for founders and marketing teams, making profit information easier to read "
                    "and use. Those spreadsheets contained fixed costs, variable costs, customer-value calculations, "
                    "an advertising analyzer, and scenario planning. Profit AI brought that reporting into a Shopify "
                    "app after Jack had already spent time doing the work for clients. The problem was not inventing "
                    "another dashboard for its own sake; Jack described data collection as time-consuming and the "
                    "spreadsheets as awkward. Andy reached a similar opportunity through an IPO newsletter project "
                    "that required financial data in Airtable. Data Fetcher connects other platforms through APIs "
                    "and schedules imports instead of making users pull data manually. AI Tomorrow Desk describes "
                    "Blue Dot's starting point as an agency with 15 recruitment consultants whose meeting notes "
                    "were messy and difficult to keep current. Its Chrome extension records Google Meet calls, "
                    "transcribes them, and summarizes the discussion without sending a bot into the meeting. "
                    "Across these accounts, the starting work was already visible: client reporting, moving data, "
                    "and recording what customers said. Each product removed a repeated task from an existing "
                    "working environment rather than asking users to adopt a completely unrelated activity. "
                    "Starter Story [d8PdJJcEtE0 @ 00:04:13]; Starter Story [NvtsM8Nk72c @ 00:01:29]; "
                    "AI Tomorrow Desk [PEtFnOB9gj4 @ 00:01:21]."
                ),
                (
                    "The platform supplies a place to meet buyers, but the founders still work to reach them. "
                    "Andy describes Airtable's marketplace as a steady stream of qualified leads, with trust "
                    "helped by platform approval. Being early mattered: the first Data Fetcher customer arrived "
                    "after a few days. Thomas chooses Shopify for a related reason, describing a smaller product "
                    "scope, a dedicated marketplace, and less buying friction than a standalone SaaS. Their "
                    "existing Shopify experience also matters: Thomas already knows its features and database "
                    "objects from building stores. MicroSaaS presents Shopify's infrastructure and merchant base "
                    "as useful foundations for specialized products, while emphasizing research into merchant "
                    "needs and differentiation through features, support, or integrations. Ericas shows the work "
                    "behind getting a new listing moving. Kaching began at the bottom of the App Store, so "
                    "Ericas contacted clients, friends, and communities, asked people to install the app, and "
                    "made it free to reduce friction. Installs created feedback and opportunities for reviews "
                    "before subscription monetization began. These approaches share a platform-first starting "
                    "point without sharing an expectation that publishing alone finishes distribution. Thomas "
                    "is choosing a channel and scope; Andy benefited from an early marketplace; Ericas manually "
                    "recruited the first users inside a more established ecosystem. "
                    "Starter Story [NvtsM8Nk72c @ 00:03:44]; ThomSaaS Builder [6WjqY6KEpNQ @ 00:04:33]; "
                    "MicroSaaS [CwPQnA6ziY4 @ 00:03:07]; Starter Story [vLLBzUZr6-s @ 00:10:08]."
                ),
                (
                    "Research means looking at existing behavior and the products people already compare. The "
                    "Super Lemon founders searched every letter of the alphabet in Shopify's autocomplete, "
                    "collected the resulting keywords, and examined competing apps. They looked at review "
                    "velocity as well as average ratings: recent reviews suggested continuing demand, while "
                    "a weaker leading app suggested room to compete. They did not want to challenge a "
                    "well-reviewed leader with no obvious opening. Justas likewise looks for competition, "
                    "merchant problems, differentiation, development difficulty, and whether an app helps "
                    "merchants earn revenue. Their warning is direct: an empty category can mean there is "
                    "no real problem, rather than an overlooked prize. MicroSaaS's Chrome guidance approaches "
                    "the same comparison from the user's side: examine functionality, reviews, pricing, "
                    "compatibility, ease of use, customization, and support; try demos or free trials rather "
                    "than choosing by description alone. The channel uses Taskmaster and simplify note to "
                    "illustrate distinct jobs such as task management and note-taking. Super Lemon's keyword "
                    "work and Justas's competitive research keep the builder focused on a particular merchant "
                    "need. MicroSaaS's evaluation criteria identify the questions that a prospective user "
                    "brings when comparing one extension with another: what it does, whether it fits, and "
                    "what using it will actually feel like. "
                    "hexdevs [KP61wa0qiSU @ 00:16:14]; "
                    "The SaaS Hub - The Shopify Podcast [Trud8JKFPok @ 00:16:44]; "
                    "MicroSaaS [Y19YrcyzMvg @ 00:04:13]."
                ),
            ],
            "table": {
                "caption": "The recurring starting point: an existing job, audience, and comparison set",
                "headers": ["Practitioner starting point", "Business mechanic described by the speaker", "Expert Source"],
                "rows": [
                    [
                        "Jack already built accessible reporting spreadsheets for founders and marketing teams working with client data.",
                        "Turn the repeated reporting work into a Shopify app instead of continuing to assemble information manually.",
                        "Starter Story ([d8PdJJcEtE0 @ 00:04:13])",
                    ],
                    [
                        "Andy saw a successful Google Sheets add-on and recognized a related Airtable problem from personal work.",
                        "Borrow the established add-on pattern, then validate the need by reading problems discussed in Airtable forums.",
                        "Starter Story ([NvtsM8Nk72c @ 00:02:21])",
                    ],
                    [
                        "Blue Dot's agency had grown to 15 recruitment consultants handling different client requirements and meeting notes.",
                        "Replace messy note-taking with meeting recording, transcription, and summaries inside the browser-based Google Meet workflow.",
                        "AI Tomorrow Desk ([PEtFnOB9gj4 @ 00:01:21])",
                    ],
                    [
                        "Thomas has already built Shopify stores and knows the platform from the merchant and development sides.",
                        "Choose a specific problem inside an existing system with a dedicated marketplace rather than rebuilding everything.",
                        "ThomSaaS Builder ([6WjqY6KEpNQ @ 00:04:33])",
                    ],
                    [
                        "MicroSaaS describes merchants looking for specialized applications that address particular needs in their online stores.",
                        "Research merchant pain points and differentiate through distinctive features, useful integrations, or exceptional customer support.",
                        "MicroSaaS ([CwPQnA6ziY4 @ 00:04:20])",
                    ],
                    [
                        "MicroSaaS tells Chrome users to compare functionality, reviews, pricing, and compatibility with tools already in use.",
                        "Try available demos or free trials and compare usability, customization, and support before choosing an extension.",
                        "MicroSaaS ([Y19YrcyzMvg @ 00:04:13])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Jack's spreadsheet conversion began with a CSV uploaded to Cursor and an instruction to "
                    "build it. The next work was identifying incorrect calculations and telling Cursor what "
                    "the right calculation should be. Jack says the initial build took roughly three and a "
                    "half to four months, not a single unattended prompt. Their later toolset includes "
                    "Claude Code, terminal-based Codex, Framer, and Google Sheets. Andy's Data Fetcher uses "
                    "TypeScript, React, and Airtable's extension SDK, with TypeScript, Postgres, GraphQL, and "
                    "Node behind the extension. Before building, Andy checks whether the target platform "
                    "has a public API, marketplace, or extension SDK, then considers platform size, problem "
                    "frequency, and prices on an established comparison platform. W3 NOTES teaches a separate "
                    "Chrome implementation path: Manifest V3, Plasmo or WXT for framework support, and "
                    "chrome.storage for state. The channel warns that service workers sleep after about "
                    "30 seconds of inactivity, so simple in-memory variables do not preserve state across "
                    "that interruption. It also presents XPay.js as a way to integrate Stripe payments "
                    "without operating a separate payment backend. These are different build arrangements: "
                    "Jack repeatedly corrected generated calculations, Andy used Airtable's SDK, and W3 NOTES "
                    "focuses on browser-worker state and extension-specific tooling. "
                    "Starter Story [d8PdJJcEtE0 @ 00:06:35]; Starter Story [NvtsM8Nk72c @ 00:05:12]; "
                    "Starter Story [NvtsM8Nk72c @ 00:07:47]; "
                    "W3 NOTES | The Internet Cash Flow Library [WqPZRP04bc0 @ 00:03:24]."
                ),
                (
                    "Arseniy's candy-box implementation keeps the subscription machinery in Shopify while "
                    "customizing the storefront with Hydrogen. A selling plan group contains the products "
                    "and selling arrangement; a selling plan specifies charging, delivery frequency, and "
                    "discount; a subscription contract records the agreement with an individual customer. "
                    "The contract remains separate from the plan, so changing a plan's discount does not "
                    "automatically change existing subscriptions. The box builder offers mini, classic, "
                    "and party sizes, one-time purchase or subscription, and deliveries every two, four, "
                    "or eight weeks. Customers fill the box with flavors, use filters, or choose a "
                    "surprise selection. Arseniy keeps prices, discounts, and frequencies in Shopify rather "
                    "than storefront code so marketing can change them through the admin. The checkout "
                    "shows the delivery rhythm and recurring amount, while the customer account allows "
                    "skipping, pausing, or canceling. SpringRain IT presents SAPP Subscriptions around "
                    "similar operational jobs: daily, weekly, monthly, or custom intervals; billing through "
                    "the Shopify payment system; subscription administration; and a portal for changing "
                    "preferences or deliveries. Its presentation also includes storefront purchase options "
                    "and personalized reminders. Arseniy's example adds a bespoke buying experience; "
                    "SAPP's presentation emphasizes managing subscriptions and giving customers controls "
                    "over the recurring purchase after signup. "
                    "Arseniy Breaks It Down [85VMELOqU2Q @ 00:02:32]; "
                    "Arseniy Breaks It Down [85VMELOqU2Q @ 00:03:57]; "
                    "Arseniy Breaks It Down [85VMELOqU2Q @ 00:04:48]; "
                    "SpringRain IT [d9YQaN8iCZk @ 00:00:44]."
                ),
                (
                    "Ericas turns customer support into a review-producing operation. Kaching asks inside "
                    "the product and in monthly emails showing the revenue the app brought to a merchant. "
                    "Ericas estimates that about 95% of reviews come through support, whose technical "
                    "agents can inspect code and fix problems. The team tracks reviews, maintains a monthly "
                    "leaderboard, runs raffles, and awards a 'persuader of the month' bonus based on "
                    "review requests that become reviews. Vlad's smaller acquisition uses a simpler "
                    "version of the same distribution work: ask for reviews, add a chat button, and "
                    "improve App Store listing SEO. Easy Coming Soon had only six reviews after nine "
                    "months because the previous owner helped customers but did not ask. AI Tomorrow "
                    "Desk describes a different acquisition mix for Blue Dot: roughly 200 LinkedIn "
                    "contacts a day yielded four to seven research calls a week and two to three "
                    "people trying the product. Newsletter placements cost around $100 to $200, and "
                    "about 40 Reddit posts produced roughly 1.5 million views and more than 5,000 "
                    "upvotes. The work was not limited to launch day: Blue Dot also paired articles "
                    "with related YouTube videos, while Kaching repeatedly connected support and demonstrated "
                    "merchant results to review requests. "
                    "Starter Story [vLLBzUZr6-s @ 00:11:16]; "
                    "Starter Story [vLLBzUZr6-s @ 00:12:20]; "
                    "Ruth and Eric [8n1RiwLpGK8 @ 00:02:11]; "
                    "AI Tomorrow Desk [PEtFnOB9gj4 @ 00:03:41]."
                ),
            ],
            "table": {
                "caption": "Execution details, commercial terms, and tools actually described",
                "headers": ["Execution move", "Specific implementation or number", "Expert Source"],
                "rows": [
                    [
                        "Export the working spreadsheet as a CSV, upload it to Cursor, and ask it to build.",
                        "Jack then corrected calculation errors repeatedly and describes an initial build lasting approximately three and a half to four months.",
                        "Starter Story ([d8PdJJcEtE0 @ 00:06:35])",
                    ],
                    [
                        "Use extension-specific persistence rather than assuming background memory remains available throughout the browser session.",
                        "W3 NOTES says service workers sleep after about 30 seconds and teaches saving state through chrome.storage.",
                        "W3 NOTES | The Internet Cash Flow Library ([WqPZRP04bc0 @ 00:03:24])",
                    ],
                    [
                        "Keep subscription prices, discounts, and frequencies in Shopify instead of embedding those settings in storefront code.",
                        "Arseniy lets marketing change the offer through Shopify admin while the custom box builder uses those settings.",
                        "Arseniy Breaks It Down ([85VMELOqU2Q @ 00:04:48])",
                    ],
                    [
                        "Give subscribers a portal for managing preferences and changing the timing or contents of recurring deliveries.",
                        "SAPP presents skip and modify controls alongside storefront purchase options and personalized subscriber notifications and reminders.",
                        "SpringRain IT ([d9YQaN8iCZk @ 00:01:05])",
                    ],
                    [
                        "Show merchants the revenue attributed to the app and ask for a review in that same monthly email.",
                        "Ericas reports that around 95% of app reviews come from customer support, supported by technically capable agents.",
                        "Starter Story ([vLLBzUZr6-s @ 00:11:42])",
                    ],
                    [
                        "Run targeted research outreach before expecting a large volume of people to start using the product.",
                        "Blue Dot's reported 200 daily LinkedIn contacts produced four to seven weekly calls and two to three product trials.",
                        "AI Tomorrow Desk ([PEtFnOB9gj4 @ 00:03:41])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small moves the operators actually used",
                "body": "Demand research, persistent state, support context, and review requests appear as concrete execution moves.",
                "items": [
                    "Search every alphabet letter in Shopify autocomplete, collect the keywords, and compare recent review velocity with the leading app's rating. Super Lemon shortlisted active demand where the leading product left room to compete. [hexdevs — KP61wa0qiSU @ 00:16:31]",
                    "Use three-star extension reviews or Google autocomplete to find complaints, then put Figma mockups on a landing page and watch whether people try to sign up or pay before building, as W3 NOTES teaches. [W3 NOTES | The Internet Cash Flow Library — WqPZRP04bc0 @ 00:02:50]",
                    "Put help beside the exact control causing confusion. Super Lemon reports that two sentences reduced one recurring question from roughly 10 daily messages to one or zero. [hexdevs — KP61wa0qiSU @ 00:33:23]",
                    "For a neglected app that already works, Vlad's first changes were asking for reviews, adding a chat button, and improving the App Store listing's SEO. [Ruth and Eric — 8n1RiwLpGK8 @ 00:02:45]",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Find the platform and the repeated complaint",
                    "action": "Use Andy's platform research and pain-point discovery sequence.",
                    "detail": "Look for a growing platform, inspect its forums, Reddit, or Twitter, and identify a use case. Andy then borrows a proven add-on pattern from a more established platform while adapting the experience to feel native. [Starter Story — NvtsM8Nk72c @ 00:04:47]",
                },
                {
                    "step": 2,
                    "title": "Check integration and commercial room",
                    "action": "Inspect the API, marketplace, or SDK before committing to the build.",
                    "detail": "Andy checks integration access, considers platform user count and problem frequency, compares established-platform price points, and examines the roadmap and support forums for signs that the platform will add the feature itself. [Starter Story — NvtsM8Nk72c @ 00:05:12]",
                },
                {
                    "step": 3,
                    "title": "Ship the smallest useful version",
                    "action": "Follow the Superpower founder's short build-and-launch cycle.",
                    "detail": "The first extension used JavaScript, HTML, and CSS and had only two features. Its founder learned extension development and launched within two or three days, while explicitly crediting early timing. [Starter Story — ty9ZcimL6VE @ 00:05:58]",
                },
                {
                    "step": 4,
                    "title": "Turn repeated customer requests into paid value",
                    "action": "Keep the feedback loop running after users start installing.",
                    "detail": "Super Lemon launched free, built requested features, separated the portion people would pay for from the free portion, and introduced a $3 monthly plan before continuing feature and pricing experiments with paying customers. [hexdevs — KP61wa0qiSU @ 00:36:32]",
                },
            ],
        },
        {
            "id": "disagreements-and-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Free access serves different jobs in these businesses, and the founders do not agree "
                    "on when it should end. Superpower ChatGPT's founder kept every feature free for roughly "
                    "nine months, started a newsletter after three or four months, and earned the first "
                    "sponsorship money before charging for the extension. The founder now thinks monetization "
                    "should have started earlier, while also crediting free access with audience growth. "
                    "When paid features arrived, existing features remained free. Ericas follows a different "
                    "transition: launch an app free, collect reviews, wait for organic installs, grandfather "
                    "existing users, and monetize new users with subscriptions and usage tiers. Jack's "
                    "Profit AI combines a continuing free plan with a 30-day trial of the paid plan. "
                    "The paid price fell from $5,000 a month to $800 after only a couple of existing "
                    "business relationships took the higher offer. Connor Gross describes still other "
                    "models: Honey earns affiliate commissions from retail partners, while Adblock Plus "
                    "allows paying companies through its blocking system. Connor calls that latter "
                    "arrangement ethically questionable while reporting its commercial scale. The practical "
                    "contrast is explicit in their accounts: subscription upgrades are one route, newsletter "
                    "sponsorship is another, and some extensions monetize relationships with companies rather "
                    "than charging the person who installed the tool. "
                    "Starter Story [ty9ZcimL6VE @ 00:08:37]; Starter Story [vLLBzUZr6-s @ 00:13:12]; "
                    "Starter Story [d8PdJJcEtE0 @ 00:02:26]; Connor Gross [7QQuWqdy4l4 @ 00:01:43]."
                ),
                (
                    "Platform selection and expansion produce another clear split. Andy advises against "
                    "building on ChatGPT or Claude because competition is so intense, preferring to use "
                    "those tools to strengthen the business. Superpower's founder built directly on "
                    "ChatGPT and reports roughly $20,000 to $30,000 MRR, while crediting an extremely "
                    "early launch and community feedback. The same founder acknowledges that OpenAI "
                    "could end the product and would probably respond by building for another major "
                    "platform. W3 NOTES recommends a portfolio approach, illustrating it with four "
                    "extensions earning $250 a month each and a roadmap that reinvests profits into "
                    "another tool. Justas operates an actual portfolio but rejects the idea that one "
                    "developer should immediately build ten apps. Essential Apps shares support, "
                    "marketing, and knowledge, yet each application must remain good and needs ownership. "
                    "Justas describes dedicated teams and warns that context switching splits focus. "
                    "Their recommendation is to make one application genuinely useful and get traction "
                    "before considering diversification. The differences are not merely about preferred "
                    "platform names. Andy screens out a crowded AI opportunity, Superpower's founder "
                    "accepted that exposure early, W3 NOTES teaches small-tool multiplication, and Justas "
                    "insists that successful expansion still leaves somebody responsible for improving "
                    "and supporting each existing app. "
                    "Starter Story [NvtsM8Nk72c @ 00:06:39]; Starter Story [ty9ZcimL6VE @ 00:11:16]; "
                    "W3 NOTES | The Internet Cash Flow Library [WqPZRP04bc0 @ 00:05:30]; "
                    "The SaaS Hub - The Shopify Podcast [Trud8JKFPok @ 00:55:41]."
                ),
                (
                    "The platform can also be a long-term home, an integration, or an asset to improve "
                    "and sell. Justas wants Essential Apps as closely integrated with Shopify as possible, "
                    "including Built for Shopify requirements and shared learning across the portfolio. "
                    "The Super Lemon founders choose a different architecture for Delight Chat: it "
                    "should work independently while still integrating with Shopify. They want customers "
                    "from their own website, SEO, and content as well as marketplaces because relying "
                    "on one platform for both the product and acquisition makes them uncomfortable. "
                    "Buying an existing app offers another route. Rags to Riches tells Carlos's "
                    "CartSaver Pro story: an $80,000 purchase supported by $12,000 cash, a $28,000 "
                    "seller note, and a $40,000 revenue-based loan; a UI refresh, tiered pricing, "
                    "and affiliates then precede a reported $418,000 acquisition offer in month eighteen. "
                    "Vlad's purchase has a different purpose and scale. Easy Coming Soon went from "
                    "$130 to $200 MRR, but Vlad says the main reason for buying it was lead "
                    "generation. Merchants stop needing a coming-soon page after opening their stores, "
                    "so Vlad wanted early relationships for another app and affiliate recommendations. "
                    "One acquisition story centers on improving and exiting an asset; the other "
                    "uses a short-lived merchant need to establish contact before the next product "
                    "is ready. "
                    "The SaaS Hub - The Shopify Podcast [Trud8JKFPok @ 00:30:11]; "
                    "hexdevs [KP61wa0qiSU @ 00:50:48]; "
                    "Rags to Riches [KkLDdsg6LOM @ 00:02:20]; "
                    "Ruth and Eric [8n1RiwLpGK8 @ 00:04:11]."
                ),
            ],
            "table": {
                "caption": "Different operators choose different monetization, ownership, and platform exposure",
                "headers": ["One playbook", "Contrasting playbook or operational choice", "Expert Source"],
                "rows": [
                    [
                        "Superpower ChatGPT stayed entirely free initially and earned newsletter sponsorship money before introducing paid extension features.",
                        "Ericas makes the initial cohort free permanently and begins charging new users after organic installs start arriving.",
                        "Starter Story ([ty9ZcimL6VE @ 00:08:37]); Starter Story ([vLLBzUZr6-s @ 00:13:29])",
                    ],
                    [
                        "Andy recommends avoiding ChatGPT and Claude as target platforms because many other builders already compete there.",
                        "Superpower's founder built on ChatGPT early and accepts that OpenAI could make the extension stop working.",
                        "Starter Story ([NvtsM8Nk72c @ 00:06:39]); Starter Story ([ty9ZcimL6VE @ 00:11:16])",
                    ],
                    [
                        "W3 NOTES illustrates a small portfolio with four extensions each earning $250 in monthly recurring income.",
                        "Justas recommends establishing one strong application first and retaining dedicated ownership before adding more applications.",
                        "W3 NOTES | The Internet Cash Flow Library ([WqPZRP04bc0 @ 00:05:30]); The SaaS Hub - The Shopify Podcast ([Trud8JKFPok @ 00:55:41])",
                    ],
                    [
                        "Arseniy recommends starting with Shopify's free subscription app and adding custom design only where the store needs it.",
                        "SpringRain IT presents SAPP as a separate subscription-management application with customizable intervals, customer controls, and reminders.",
                        "Arseniy Breaks It Down ([85VMELOqU2Q @ 00:08:43]); SpringRain IT ([d9YQaN8iCZk @ 00:00:24])",
                    ],
                    [
                        "Justas makes close Shopify integration and Built for Shopify requirements central to the Essential Apps operating philosophy.",
                        "Delight Chat's founders want independent product access and acquisition channels alongside deep integrations with platforms such as Shopify.",
                        "The SaaS Hub - The Shopify Podcast ([Trud8JKFPok @ 00:30:11]); hexdevs ([KP61wa0qiSU @ 00:50:48])",
                    ],
                    [
                        "Rags to Riches describes Carlos improving CartSaver Pro's onboarding, pricing, and affiliate distribution before selling the application.",
                        "Vlad says the central purpose of buying Easy Coming Soon was lead generation, despite improving its small recurring revenue.",
                        "Rags to Riches ([KkLDdsg6LOM @ 00:03:25]); Ruth and Eric ([8n1RiwLpGK8 @ 00:04:11])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Positive interviews did not save Session Fox. The Super Lemon founders had interviewed "
                    "30 people, built for three months, and paid a freelancer to help development. When "
                    "the SDK reached those prospects, only one integrated it after a month; the other "
                    "29 did not, despite follow-ups. Reading The Mom Test changed the questions. Instead "
                    "of accepting enthusiasm, they asked why somebody claiming to need the product "
                    "was not already using available alternatives. Reinterviews revealed that people "
                    "were getting by with analytics or did not care enough to solve the problem. "
                    "Justas describes an even longer wrong turn before Oberlo: the team invented a "
                    "problem internally, worked behind closed doors for about a year, and earned "
                    "30 cents. With roughly a month of salaries left, they switched to problems "
                    "some teammates actually experienced in dropshipping and released several apps. "
                    "Andy reports a different research failure after shipping: almost an entire "
                    "year passed without speaking to users. One afternoon of user testing exposed "
                    "UX problems whose fixes improved revenue and usage almost overnight. These "
                    "are concrete reversals: interview enthusiasm failed to become integration, "
                    "a year of development failed to produce demand, and an operating product "
                    "kept carrying usability problems until its founder watched and questioned "
                    "the people using it. "
                    "hexdevs [KP61wa0qiSU @ 00:07:53]; hexdevs [KP61wa0qiSU @ 00:11:58]; "
                    "The SaaS Hub - The Shopify Podcast [Trud8JKFPok @ 00:03:28]; "
                    "Starter Story [NvtsM8Nk72c @ 00:09:53]."
                ),
                (
                    "Blue Dot's reversal was about the installation decision as much as the transcription "
                    "feature. AI Tomorrow Desk reports that the founders first built a Zoom integration, "
                    "then discovered companies did not want to test a new tool across their entire "
                    "Zoom account. They pivoted to a Chrome extension focused on Google Meet. Their "
                    "Product Hunt launch also disappointed: fifth product of the day and a few hundred "
                    "website visits did less than the founders hoped, while newsletter mentions "
                    "reportedly multiplied traffic. Superpower's founder faces a different bottleneck: "
                    "the host platform can remove the business opportunity. The founder says OpenAI "
                    "could kill the product any day, describes having worried about that for a "
                    "long time, and expects rebuilding elsewhere would make life harder. Jack's "
                    "Profit AI dashboard shows another limitation beneath a large revenue headline. "
                    "Jack reports 43 uninstalls against 47 installs, 122 current users, most of "
                    "them free, and about 38 or 39 paying customers. Jack also cut the paid "
                    "price after very limited uptake at $5,000 a month. Their closing advice "
                    "is not to aim for laziness: the market moves fast and idle builders get "
                    "replaced. These accounts retain the friction alongside the revenue: reluctance "
                    "to install, disappointing launch traffic, platform dependence, and customers "
                    "leaving almost as quickly as new ones arrive. "
                    "AI Tomorrow Desk [PEtFnOB9gj4 @ 00:01:59]; "
                    "Starter Story [ty9ZcimL6VE @ 00:11:16]; "
                    "Starter Story [d8PdJJcEtE0 @ 00:02:26]; "
                    "Starter Story [d8PdJJcEtE0 @ 00:09:38]."
                ),
                (
                    "Operating costs and support work remain visible even in the lean businesses. "
                    "Andy reports roughly $2,500 a month in hosting, $1,000 for SaaS tools, and "
                    "$150 for coworking, alongside a claimed 85% margin. Ericas reports around "
                    "90% profitability, but Kaching also provides technical support around the "
                    "clock and offers full refunds without questions because a one-star review "
                    "is too costly a risk in their view. Super Lemon's founders kept support "
                    "between five and fifteen messages a day by removing repeated confusion "
                    "inside the product. One question fell from roughly ten daily messages "
                    "to one or zero after two explanatory sentences were added. They also "
                    "watched server dashboards, investigated unusual traffic, and added capacity "
                    "as usage grew rather than starting with elaborate infrastructure. Justas "
                    "describes a heavier portfolio operation: support staff are developers with "
                    "Shopify knowledge, and onboarding can take a couple of months to half a "
                    "year. Automated tagging, workflows, and escalation handoffs support those "
                    "people rather than eliminating them. Their warning to a lone developer "
                    "considering ten apps is that success itself can overwhelm support capacity. "
                    "The economics therefore sit beside specific operating arrangements: Andy's "
                    "hosting bill, Kaching's review-sensitive refunds, Super Lemon's contextual "
                    "help, and Essential Apps' trained technical support teams. "
                    "Starter Story [NvtsM8Nk72c @ 00:08:34]; "
                    "Starter Story [vLLBzUZr6-s @ 00:13:29]; "
                    "hexdevs [KP61wa0qiSU @ 00:33:23]; "
                    "The SaaS Hub - The Shopify Podcast [Trud8JKFPok @ 00:33:01]."
                ),
            ],
            "table": {
                "caption": "Reported reversals and the operating checks attached to them",
                "headers": ["Firsthand problem or attributed warning", "Reported response or economic detail", "Expert Source"],
                "rows": [
                    [
                        "Session Fox prospects expressed interest, but only one of the 30 interviewed users eventually integrated the SDK.",
                        "The founders reinterviewed prospects with different questions and shut the product after finding the need was not pressing.",
                        "hexdevs ([KP61wa0qiSU @ 00:11:58])",
                    ],
                    [
                        "Justas's earlier team spent roughly a year building an internally imagined solution without validating it with users.",
                        "The project earned 30 cents, leaving roughly one month of salaries before the team shifted toward experienced dropshipping problems.",
                        "The SaaS Hub - The Shopify Podcast ([Trud8JKFPok @ 00:03:28])",
                    ],
                    [
                        "Andy went almost an entire year without speaking directly to the people using the product they had built.",
                        "One afternoon exposed usability issues, and fixing those issues increased revenue, usage, and other results almost overnight.",
                        "Starter Story ([NvtsM8Nk72c @ 00:09:53])",
                    ],
                    [
                        "Jack's dashboard showed almost as many uninstalls as installs despite substantial reported app revenue and a free plan.",
                        "Jack reported 43 uninstalls, 47 installs, 122 current users, and approximately 38 or 39 paying customers.",
                        "Starter Story ([d8PdJJcEtE0 @ 00:02:49])",
                    ],
                    [
                        "Vlad says coming-soon users often remove the app after a week or month when their store opens.",
                        "The acquisition was primarily intended to generate leads for another app and affiliate recommendations rather than maximize retention.",
                        "Ruth and Eric ([8n1RiwLpGK8 @ 00:04:11])",
                    ],
                    [
                        "Andy says side ventures consumed around six months while supposedly addressing platform risk or market saturation concerns.",
                        "Andy later recognized boredom during slower growth and now uses Claude as a business coach to reinforce focus.",
                        "Starter Story ([NvtsM8Nk72c @ 00:09:04])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks drawn from actual reversals and operating pressure",
                "body": "Check whether customers act, whether the interface works for them, and whether the growing business remains supportable.",
                "items": [
                    "When prospects say they need the product, ask why they are not using existing alternatives. The Session Fox founders changed their conclusion after those questions exposed weak urgency. [hexdevs — KP61wa0qiSU @ 00:08:51]",
                    "Run user testing early and repeatedly. Andy's warning comes from nearly a year without customer conversations and an afternoon that uncovered revenue-affecting UX problems. [Starter Story — NvtsM8Nk72c @ 00:09:53]",
                    "Read installs and uninstalls alongside revenue. Jack openly reports 43 uninstalls and 47 installs while most of Profit AI's 122 users are free. [Starter Story — d8PdJJcEtE0 @ 00:02:49]",
                    "Get one application working well before multiplying the portfolio, and keep someone responsible for it afterward. Justas warns that a single developer with ten successful apps can become overwhelmed by support. [The SaaS Hub - The Shopify Podcast — Trud8JKFPok @ 00:55:41]",
                ],
            },
        },
    ],
    "pull_quote": (
        "'Don't aim for laziness.' — Jack, Starter Story "
        "(d8PdJJcEtE0 @ 00:09:38)."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        "Find a platform pain point in forums, Reddit, or Twitter, then compare it with an already successful add-on pattern from another platform. [Starter Story — NvtsM8Nk72c @ 00:04:47]",
        "Search Shopify autocomplete, list the resulting keywords, and compare competing apps' recent reviews and ratings before selecting a problem. [hexdevs — KP61wa0qiSU @ 00:16:31]",
        "Join the communities where prospective users already ask for features, build a requested feature, and return to tell those users it is available. [Starter Story — ty9ZcimL6VE @ 00:03:59]",
        "For a subscription storefront, keep prices, discounts, and delivery frequencies in Shopify so marketing can update them without changing storefront code. [Arseniy Breaks It Down — 85VMELOqU2Q @ 00:04:48]",
        "Ask for reviews during customer support and in monthly emails that show the revenue the app brought to the merchant. [Starter Story — vLLBzUZr6-s @ 00:11:42]",
        "Review recurring support questions and add contextual help directly where users become confused, following Super Lemon's product-level fixes. [hexdevs — KP61wa0qiSU @ 00:32:14]",
    ],
    "statutory_citations": [
        {
            "title": "Starter Story — I Turned This Spreadsheet Into a $30K/Month Micro-SaaS [00:06:35]",
            "url": "https://www.youtube.com/watch?v=d8PdJJcEtE0&t=395s",
            "relevance": "Primary practitioner testimony on converting a spreadsheet into an app and correcting generated calculations.",
        },
        {
            "title": "Starter Story — How I Built It: $23K/month micro-saas [00:04:47]",
            "url": "https://www.youtube.com/watch?v=NvtsM8Nk72c&t=287s",
            "relevance": "Primary practitioner testimony on platform selection, pain-point research, and borrowing an established add-on pattern.",
        },
        {
            "title": "Starter Story — My Apps Make $4.5M/Year With $0 Marketing [00:11:42]",
            "url": "https://www.youtube.com/watch?v=vLLBzUZr6-s&t=702s",
            "relevance": "Primary practitioner testimony on merchant revenue emails, review requests, and technical customer support.",
        },
        {
            "title": "hexdevs — How to Grow a Micro SaaS to $30,000 MRR on the Shopify App Store [00:16:31]",
            "url": "https://www.youtube.com/watch?v=KP61wa0qiSU&t=991s",
            "relevance": "Primary practitioner testimony on Shopify autocomplete research, keyword selection, and competitor review analysis.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "d8PdJJcEtE0",
            "title": "I Turned This Spreadsheet Into a $30K/Month Micro-SaaS",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": "It's literally downloading the spreadsheet as a CSV, uploading it to Cursor, and saying build it.",
            "tip": "It's literally downloading the spreadsheet as a CSV, uploading it to Cursor, and saying build it.",
            "timestamp": 395,
            "timestamp_seconds": 395,
            "timestamp_label": "[00:06:35]",
            "url": "https://www.youtube.com/watch?v=d8PdJJcEtE0&t=395s",
            "markdown": "[00:06:35](https://www.youtube.com/watch?v=d8PdJJcEtE0&t=395s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the spreadsheet-to-app build process and subsequent correction of calculation errors.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "NvtsM8Nk72c",
            "title": "How I Built It: $23K/month micro-saas",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": "Step two, you then want to find a pain point on that platform and you can look in their forums, on Reddit, on Twitter.",
            "tip": "Step two, you then want to find a pain point on that platform and you can look in their forums, on Reddit, on Twitter.",
            "timestamp": 287,
            "timestamp_seconds": 287,
            "timestamp_label": "[00:04:47]",
            "url": "https://www.youtube.com/watch?v=NvtsM8Nk72c&t=287s",
            "markdown": "[00:04:47](https://www.youtube.com/watch?v=NvtsM8Nk72c&t=287s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on finding platform-specific problems before building an add-on.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PEtFnOB9gj4",
            "title": "How a Simple Chrome Extension Micro SaaS Makes $3000/mo",
            "channel": "AI Tomorrow Desk",
            "author": "AI Tomorrow Desk",
            "text": "They went and scheduled a bunch of interviews and started talking to potential customers.",
            "tip": "They went and scheduled a bunch of interviews and started talking to potential customers.",
            "timestamp": 119,
            "timestamp_seconds": 119,
            "timestamp_label": "[00:01:59]",
            "url": "https://www.youtube.com/watch?v=PEtFnOB9gj4&t=119s",
            "markdown": "[00:01:59](https://www.youtube.com/watch?v=PEtFnOB9gj4&t=119s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Channel account of Blue Dot's validation interviews and the initial Zoom integration mistake.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "7QQuWqdy4l4",
            "title": "Million Dollar Chrome Extensions (And How They Did It)",
            "channel": "Connor Gross",
            "author": "Connor Gross",
            "text": "They tap directly into the activity and the behavior that you're already doing while on Chrome.",
            "tip": "They tap directly into the activity and the behavior that you're already doing while on Chrome.",
            "timestamp": 207,
            "timestamp_seconds": 207,
            "timestamp_label": "[00:03:27]",
            "url": "https://www.youtube.com/watch?v=7QQuWqdy4l4&t=207s",
            "markdown": "[00:03:27](https://www.youtube.com/watch?v=7QQuWqdy4l4&t=207s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Channel explanation of extensions that improve existing browser activity rather than create a separate destination.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ty9ZcimL6VE",
            "title": "How I Built It: $20K/Month Chrome Extension",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": "If you know how to build a simple website, you'll know how to build an extension. JavaScript, HTML, CSS, that's how I built the very first version.",
            "tip": "If you know how to build a simple website, you'll know how to build an extension. JavaScript, HTML, CSS, that's how I built the very first version.",
            "timestamp": 358,
            "timestamp_seconds": 358,
            "timestamp_label": "[00:05:58]",
            "url": "https://www.youtube.com/watch?v=ty9ZcimL6VE&t=358s",
            "markdown": "[00:05:58](https://www.youtube.com/watch?v=ty9ZcimL6VE&t=358s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Founder testimony on the languages used for the first Superpower ChatGPT extension.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Y19YrcyzMvg",
            "title": "Unlock Efficiency: The Power of Micro SaaS Apps in Chrome",
            "channel": "MicroSaaS",
            "author": "MicroSaaS",
            "text": "It's essential to consider factors such as functionality, user reviews, pricing, and compatibility with your existing tools.",
            "tip": "It's essential to consider factors such as functionality, user reviews, pricing, and compatibility with your existing tools.",
            "timestamp": 253,
            "timestamp_seconds": 253,
            "timestamp_label": "[00:04:13]",
            "url": "https://www.youtube.com/watch?v=Y19YrcyzMvg&t=253s",
            "markdown": "[00:04:13](https://www.youtube.com/watch?v=Y19YrcyzMvg&t=253s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Channel guidance on comparing extensions against an existing workflow and toolset.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "WqPZRP04bc0",
            "title": "PROFITABLE CHROME EXTENSION BLUEPRINT | Build And Scale Micro Tools For Passive Monthly Revenue",
            "channel": "W3 NOTES | The Internet Cash Flow Library",
            "author": "W3 NOTES | The Internet Cash Flow Library",
            "text": "First, look at Google autocomplete or the three-star reviews of existing extensions to find real pain points.",
            "tip": "First, look at Google autocomplete or the three-star reviews of existing extensions to find real pain points.",
            "timestamp": 170,
            "timestamp_seconds": 170,
            "timestamp_label": "[00:02:50]",
            "url": "https://www.youtube.com/watch?v=WqPZRP04bc0&t=170s",
            "markdown": "[00:02:50](https://www.youtube.com/watch?v=WqPZRP04bc0&t=170s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Channel teaching on extension demand research and testing interest before coding.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "85VMELOqU2Q",
            "title": "Shopify Subscriptions Explained: Recurring Revenue Built Into Your Store",
            "channel": "Arseniy Breaks It Down",
            "author": "Arseniy Breaks It Down",
            "text": "I don't keep prices, discounts or frequencies in the site code.",
            "tip": "I don't keep prices, discounts or frequencies in the site code.",
            "timestamp": 288,
            "timestamp_seconds": 288,
            "timestamp_label": "[00:04:48]",
            "url": "https://www.youtube.com/watch?v=85VMELOqU2Q&t=288s",
            "markdown": "[00:04:48](https://www.youtube.com/watch?v=85VMELOqU2Q&t=288s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Builder testimony on keeping subscription offer settings in Shopify rather than custom storefront code.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "CwPQnA6ziY4",
            "title": "Micro SaaS on Shopify: Your Path to Success!",
            "channel": "MicroSaaS",
            "author": "MicroSaaS",
            "text": "Developers can explore various ways to set their app apart from competitors, such as offering unique features, providing exceptional customer support, or integrating with other popular Shopify apps.",
            "tip": "Developers can explore various ways to set their app apart from competitors, such as offering unique features, providing exceptional customer support, or integrating with other popular Shopify apps.",
            "timestamp": 296,
            "timestamp_seconds": 296,
            "timestamp_label": "[00:04:56]",
            "url": "https://www.youtube.com/watch?v=CwPQnA6ziY4&t=296s",
            "markdown": "[00:04:56](https://www.youtube.com/watch?v=CwPQnA6ziY4&t=296s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Channel guidance on differentiation through features, support, and Shopify integrations.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KkLDdsg6LOM",
            "title": "From $80K to $418K: How Carlos Flipped a Shopify App into a Life-Changing Exit",
            "channel": "Rags to Riches",
            "author": "Rags to Riches",
            "text": "Out of the $80,000 price tag, Carlos would put down just $12,000 in cash, 15%.",
            "tip": "Out of the $80,000 price tag, Carlos would put down just $12,000 in cash, 15%.",
            "timestamp": 140,
            "timestamp_seconds": 140,
            "timestamp_label": "[00:02:20]",
            "url": "https://www.youtube.com/watch?v=KkLDdsg6LOM&t=140s",
            "markdown": "[00:02:20](https://www.youtube.com/watch?v=KkLDdsg6LOM&t=140s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Narrated CartSaver Pro acquisition case describing cash contribution and a mixed financing structure.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "vLLBzUZr6-s",
            "title": "My Apps Make $4.5M/Year With $0 Marketing",
            "channel": "Starter Story",
            "author": "Starter Story",
            "text": "I think around 95% of our reviews for our apps come from customer support.",
            "tip": "I think around 95% of our reviews for our apps come from customer support.",
            "timestamp": 702,
            "timestamp_seconds": 702,
            "timestamp_label": "[00:11:42]",
            "url": "https://www.youtube.com/watch?v=vLLBzUZr6-s&t=702s",
            "markdown": "[00:11:42](https://www.youtube.com/watch?v=vLLBzUZr6-s&t=702s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Ericas's estimate of customer support's contribution to Kaching app reviews.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Trud8JKFPok",
            "title": "How We Built 10 Shopify Apps Used by 250,000+ Merchants | Justas Galaburda",
            "channel": "The SaaS Hub - The Shopify Podcast",
            "author": "The SaaS Hub - The Shopify Podcast",
            "text": "You always should focus on building one application first, build it real good, to get real traction.",
            "tip": "You always should focus on building one application first, build it real good, to get real traction.",
            "timestamp": 3364,
            "timestamp_seconds": 3364,
            "timestamp_label": "[00:56:04]",
            "url": "https://www.youtube.com/watch?v=Trud8JKFPok&t=3364s",
            "markdown": "[00:56:04](https://www.youtube.com/watch?v=Trud8JKFPok&t=3364s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Justas's advice to establish one application before expanding a portfolio and its support obligations.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "d9YQaN8iCZk",
            "title": "Unlock Recurring Revenue Streams with SAPP Subscriptions Shopify App",
            "channel": "SpringRain IT",
            "author": "SpringRain IT",
            "text": "Offer your customers an easy-to-use portal to manage subscriptions, update preferences, or skip or modify deliveries.",
            "tip": "Offer your customers an easy-to-use portal to manage subscriptions, update preferences, or skip or modify deliveries.",
            "timestamp": 65,
            "timestamp_seconds": 65,
            "timestamp_label": "[00:01:05]",
            "url": "https://www.youtube.com/watch?v=d9YQaN8iCZk&t=65s",
            "markdown": "[00:01:05](https://www.youtube.com/watch?v=d9YQaN8iCZk&t=65s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "SAPP product presentation describing customer-facing subscription and delivery controls.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8n1RiwLpGK8",
            "title": "How I Grew My Shopify App MRR from $130 to $200 In Less Than A Month | SaaS Superheroes [INTERVIEW]",
            "channel": "Ruth and Eric",
            "author": "Ruth and Eric",
            "text": "I did three things. One is asking for reviews. The second thing is just adding a chat button. The third thing is adding more SEO to the App Store listing.",
            "tip": "I did three things. One is asking for reviews. The second thing is just adding a chat button. The third thing is adding more SEO to the App Store listing.",
            "timestamp": 165,
            "timestamp_seconds": 165,
            "timestamp_label": "[00:02:45]",
            "url": "https://www.youtube.com/watch?v=8n1RiwLpGK8&t=165s",
            "markdown": "[00:02:45](https://www.youtube.com/watch?v=8n1RiwLpGK8&t=165s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Vlad's account of the first changes made after acquiring Easy Coming Soon.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "6WjqY6KEpNQ",
            "title": "From Tech Lead to SaaS Founder: Why I’m Starting with a Shopify App",
            "channel": "ThomSaaS Builder",
            "author": "ThomSaaS Builder",
            "text": "A Shopify app usually solves a specific problem within an existing system. You don't have to rebuild a whole generalist platform or recreate the client's entire working environment.",
            "tip": "A Shopify app usually solves a specific problem within an existing system. You don't have to rebuild a whole generalist platform or recreate the client's entire working environment.",
            "timestamp": 291,
            "timestamp_seconds": 291,
            "timestamp_label": "[00:04:51]",
            "url": "https://www.youtube.com/watch?v=6WjqY6KEpNQ&t=291s",
            "markdown": "[00:04:51](https://www.youtube.com/watch?v=6WjqY6KEpNQ&t=291s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Thomas's rationale for choosing the narrower scope of an application within Shopify.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KP61wa0qiSU",
            "title": "How to Grow a Micro SaaS to $30,000 MRR on the Shopify App Store",
            "channel": "hexdevs",
            "author": "hexdevs",
            "text": "We went ahead and actually searched for every alphabet, every letter of the alphabet on the Shopify App Store to see if it autocompleted.",
            "tip": "We went ahead and actually searched for every alphabet, every letter of the alphabet on the Shopify App Store to see if it autocompleted.",
            "timestamp": 991,
            "timestamp_seconds": 991,
            "timestamp_label": "[00:16:31]",
            "url": "https://www.youtube.com/watch?v=KP61wa0qiSU&t=991s",
            "markdown": "[00:16:31](https://www.youtube.com/watch?v=KP61wa0qiSU&t=991s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Super Lemon founder testimony on discovering searchable demand before selecting the app opportunity.",
        },
    ],
}
