from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "win-b2b-clients-linkedin-better-crm-data",
    "question_prompt": "How can LinkedIn acquisition and CRM enrichment support a B2B prospecting process with better targeting and more useful contact data?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Win B2B Clients with LinkedIn and Better CRM Data",
    "subtitle": "LinkedIn content, ads, direct outreach, intent-based targeting, HubSpot and Clay prospecting, job-change updates, and Claude Code contact enrichment.",
    "layout_template": "step_by_step_blueprint",
    "reading_time_minutes": 15,
    "executive_summary": (
        "LinkedIn acquisition starts with a recognizable offer, relevant prospects, and a profile "
        "that makes the next step obvious. Content-led practitioners build familiarity before "
        "messaging; outbound operators segment lists and start conversations around observed "
        "business activity. Adam Holmgren separates cold advertising from retargeting rather than "
        "expecting an immediate signup. Tommy Clark recommends five weekly posts in a 1:3:1 "
        "content mix, while Lead Gen Jay favors three weekly case studies. Automation divides "
        "the field: Patrick Dang prefers manual conversations, Alex Berman uses Expandi, and "
        "Ben Greening-James automates preparation before human replies. CRM specialists address "
        "missing fields, stale employment records, duplicate contacts, and expensive repeated "
        "research. Their implementations range from Claude Code enrichment with MoltSets to "
        "scheduled Clay job-change checks, HubSpot prospecting cards, and custom enrichment rules."
    ),
    "key_metrics": [
        {
            "label": "Cold thought-leader engagement target",
            "metric": "Cold thought-leader engagement target",
            "value": "Above 15%",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Adam Holmgren calls above 15% good for cold thought-leader ad CTR. "
                "For this format, the reported CTR includes engagement such as likes "
                "and see-more clicks, rather than only website visits."
            ),
            "source": "Adam Holmgren ([qy4FW_qglNo @ 00:06:20])",
        },
        {
            "label": "Weekly content starting mix",
            "metric": "Weekly content starting mix",
            "value": "1 top-of-funnel, 3 middle-of-funnel, 1 bottom-of-funnel",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Tommy Clark recommends this starting distribution when publishing five "
                "LinkedIn posts per week, with industry-specific thought leadership "
                "occupying the middle of the funnel."
            ),
            "source": "Tommy Clark ([MXBaHCO4WI8 @ 00:10:06])",
        },
        {
            "label": "Workspace connection and message results",
            "metric": "Workspace connection and message results",
            "value": "About 31,000 connections sent; 34% accepted; close to 10,000 messages; about 26% responses",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Jack describes these as the previous year's results in the displayed "
                "workspace, before explaining the universal inbox and intent-focused "
                "Sales Navigator prospecting process."
            ),
            "source": "Jack ([4RYnbUHayhM @ 00:01:24])",
        },
        {
            "label": "Scheduled employment-data recheck",
            "metric": "Scheduled employment-data recheck",
            "value": "Every month",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Michael Saruggia schedules Salesforce report enrichment and company "
                "comparison monthly, checking whether the employer stored in Salesforce "
                "still matches the person's LinkedIn employment information."
            ),
            "source": "Michael Saruggia - GTM Engineering ([DHX8uoA53OI @ 00:10:19])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Start with the buyer and the offer, not the sending tool. Patrick Dang "
                    "reduces the business to who you want to work with, what you sell, and "
                    "whether that audience actually wants it. They validate through customer "
                    "conversations or by examining existing offers aimed at the same market; "
                    "content cannot rescue something people will not pay for. Tommy Clark "
                    "carries that specificity into the profile: explain why someone should "
                    "follow you in one clear sentence, state your role and the value of your "
                    "content, and provide an obvious next step through featured links. Their "
                    "recommended destinations include a website or demo page alongside a "
                    "newsletter or lead magnet for visitors who are not ready to buy. Chris "
                    "Prouty adds the company page, arguing that prospects inspect it when "
                    "deciding whether a business has expertise and authority. These operators "
                    "all put understandable positioning ahead of elaborate execution. Dang "
                    "wants a defined customer with a problem; Clark wants that customer to "
                    "recognize the reason to follow; Prouty wants the business page to show "
                    "what working together can accomplish. Their starting work is making "
                    "the offer and identity legible before trying to manufacture more attention. "
                    "[lzh20RhrVW4 @ 00:00:40] [MXBaHCO4WI8 @ 00:04:45] "
                    "[8yepbhYel-Q @ 00:00:50]"
                ),
                (
                    "Content becomes prospecting material when it gives someone a reason to "
                    "recognize you and a reason to answer. Lead Gen Jay teaches miniature "
                    "case studies built from a client problem, a specific intervention, and "
                    "a numerical result, followed by a question that invites a relevant "
                    "conversation. Their next move is not a random pitch: look for business "
                    "owners and founders making substantive comments about response rates, "
                    "lead generation, or acquisition. Ross Simmons on HubSpot Marketing "
                    "similarly connects outreach to an observable interaction, including a "
                    "prospect liking your post or a colleague's post. They tell sellers to "
                    "explain why they want to connect rather than expecting an unexplained "
                    "request to carry the conversation. Patrick Dang operationalizes the "
                    "same connection between attention and outreach through three daily "
                    "queues: incoming connection requests, people engaging with content, and "
                    "profile viewers. They inspect each person against the offer before "
                    "starting a conversation, then establish fit before booking a call. Jay "
                    "uses proof, Simmons uses context, and Dang uses identifiable engagement. "
                    "None treats a visible audience as the finished sales process: each "
                    "describes a deliberate move from recognition into a conversation about "
                    "the prospect's business, needs, or interest. "
                    "[R32IyS7IErQ @ 00:01:30] [uPo9D-wZv6s @ 00:05:41] "
                    "[lzh20RhrVW4 @ 00:08:56]"
                ),
                (
                    "The CRM specialists describe a parallel problem behind the prospecting "
                    "screen: records exist, but the information needed to use them does not. "
                    "Jacob Tuwiner traces messy HubSpot data to accumulated list imports, "
                    "forms, webinar leads, and different teams using the system differently. "
                    "Their examples reach from weak customer reporting to incorrect time-zone "
                    "targeting and contact names polluted by test entries. Michael Saruggia "
                    "focuses on employment changes: a person once associated with an account "
                    "moves elsewhere, while the old email and company relationship remain "
                    "inside the CRM. RevPartners responds with company enrichment, contact "
                    "demographics, additional buying-role contacts, and account research before "
                    "layering scoring onto the records. AIMS Consulting Services starts more "
                    "narrowly by identifying missing work emails, mobile numbers, and job "
                    "titles, then asking an enrichment workflow to fill those gaps. The shared "
                    "starting point is usable account and contact information, not simply "
                    "more rows. Tuwiner wants reporting and segmentation to work; Saruggia "
                    "wants employment records to reflect the person's current company; "
                    "RevPartners wants representatives to see relevant accounts and people "
                    "inside HubSpot; AIMS wants missing details returned to the CRM without "
                    "the export-and-reupload routine they associate with data loss. "
                    "[LxiIsByGTbU @ 00:00:26] [DHX8uoA53OI @ 00:01:48] "
                    "[jV1Kp0j9lp0 @ 00:11:46] [fk7OXnsQu-o @ 00:03:25]"
                ),
            ],
            "table": {
                "caption": "What the practitioners establish before scaling prospecting",
                "headers": ["Starting point", "Practitioner execution", "Expert Source"],
                "rows": [
                    [
                        "Define the customer and the problem before publishing more content.",
                        "Dang validates demand through customer feedback or by studying comparable existing offers.",
                        "Patrick Dang ([lzh20RhrVW4 @ 00:01:31])",
                    ],
                    [
                        "Give profile visitors a clear next step beyond simply following.",
                        "Clark pairs a website or demo destination with a newsletter or lead magnet.",
                        "Tommy Clark ([MXBaHCO4WI8 @ 00:06:52])",
                    ],
                    [
                        "Show the business behind the individual with a useful company page.",
                        "Prouty says prospects inspect company pages for expertise, authority, and the service offered.",
                        "Chris Prouty ([8yepbhYel-Q @ 00:00:50])",
                    ],
                    [
                        "Use actual audience interactions as context for making the connection.",
                        "Simmons references engagement with your content or a colleague's content when reaching out.",
                        "HubSpot Marketing ([uPo9D-wZv6s @ 00:05:41])",
                    ],
                    [
                        "Stop treating disconnected imports as a dependable picture of customers.",
                        "Tuwiner describes forms, imported lists, and different teams accumulating inconsistent CRM information.",
                        "Jacob Tuwiner | AI Sales Automation ([LxiIsByGTbU @ 00:00:26])",
                    ],
                    [
                        "Give representatives account research and buying-role contacts inside their CRM.",
                        "RevPartners combines enrichment, persona information, and signals before assigning target account tiers.",
                        "RevPartners - RevOps + GTM Engineering on HubSpot ([jV1Kp0j9lp0 @ 00:11:46])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Adam Holmgren's advertising account has two campaign groups: cold "
                    "audiences and retargeting. The cold layer uses text ads, image ads, and "
                    "thought-leader ads; the retargeting layer keeps text and thought-leader "
                    "ads but substitutes conversation ads for images. Their cold audience "
                    "centers on marketing roles at technology companies and agencies, with "
                    "11 to 200 employees and a preferred audience size of 50,000 to 70,000. "
                    "They exclude competitors, previous employers, signups, and companies "
                    "outside the product's fit. Manual bids start around two-thirds of "
                    "LinkedIn's recommendation, then get checked against daily budget "
                    "delivery. Before sponsoring an organic post, Holmgren adds a website "
                    "link and product information so landing-page clicks can be tracked "
                    "separately from social actions. Their retargeting combines website "
                    "traffic, company-page visits, and cold-ad engagement across 90-day "
                    "windows. Prouty's route into paid distribution begins after organic "
                    "content gains traction, then uses ads to expand reach and recognition. "
                    "Clark supplies a specific organic publishing baseline: five weekly "
                    "posts, split into one broad post, three industry-specific thought "
                    "leadership posts, and one bottom-of-funnel post. Holmgren's cold "
                    "thought-leader content likewise discusses company growth and the "
                    "technology stack without making the product the immediate pitch. "
                    "[qy4FW_qglNo @ 00:03:19] [qy4FW_qglNo @ 00:11:11] "
                    "[8yepbhYel-Q @ 00:02:09] [MXBaHCO4WI8 @ 00:10:06]"
                ),
                (
                    "Alex Berman's outbound sequence opens with a screening question: "
                    "'Hey first name, are you running cold email campaigns for company "
                    "name?' They add social proof 15 minutes later, follow up after five "
                    "days with a LinkedIn article, follow up four days after that, then "
                    "return after two months and again three months later. Their lists "
                    "come from niche influencers' connections in Sales Navigator or "
                    "followers found through ordinary LinkedIn search, with the search "
                    "URL imported into Expandi. Cleverly instead demonstrates three "
                    "segments: companies resembling a strong client, local prospects, "
                    "and potential referral partners. They put the segment's distinguishing "
                    "feature in the first six words of the connection request and offer "
                    "to email a useful resource rather than immediately demanding a demo. "
                    "Ben Greening-James spreads contact across a 14-day sequence: connect, "
                    "engage, open softly, introduce the business trigger on day five, "
                    "and add another channel around day seven. Expandi implements branching "
                    "around profile visits, connection status, acceptance, messages, and "
                    "email fallback. Each describes a concrete sending mechanism; the "
                    "scripts and timing remain different. Berman's quick screening question, "
                    "Cleverly's segment-based offer, and Greening-James's delayed trigger "
                    "are separate sequences rather than one shared cadence. "
                    "[Kjfkoa15cNU @ 00:03:42] [h66nRoG6w0E @ 00:10:30] "
                    "[Lw2iBa2oM44 @ 00:17:18] [IqCv6BL9r6o @ 00:04:42]"
                ),
                (
                    "AIMS Consulting Services connects HubSpot, installs the MoltSets skill "
                    "in Claude Code, names the missing fields, and requests waterfall "
                    "enrichment while explicitly preserving existing information. The "
                    "demonstration checks available tokens, excludes sample contacts, "
                    "reports unavailable phone credits, verifies emails, and presents "
                    "the proposed CRM updates. Michael Saruggia's employment workflow "
                    "starts with scheduled Salesforce reports or HubSpot lists imported "
                    "into Clay. Find the LinkedIn profile from the email, enrich the "
                    "person, compare the latest experience with the CRM employer, and "
                    "double-check recent changes. Their routine marks the old record "
                    "'left company,' looks for existing contacts and leads, checks the "
                    "new account, finds the new email, and routes the result into a "
                    "campaign. RevPartners offers three on-demand requests inside HubSpot: "
                    "company enrichment, finding new contacts, and enriching an existing "
                    "contact. A property or list triggers a webhook to Clay; workflows "
                    "show progress and the last enrichment date, while Clay returns "
                    "completion information. The demonstrations preserve different "
                    "operational details: AIMS examines the batch and credit availability, "
                    "Saruggia reconciles old and new employment records, and RevPartners "
                    "places enriched information in prospecting cards that representatives "
                    "can use without navigating the underlying Clay tables themselves. "
                    "[fk7OXnsQu-o @ 00:03:25] [DHX8uoA53OI @ 00:06:32] "
                    "[jV1Kp0j9lp0 @ 00:43:15]"
                ),
            ],
            "table": {
                "caption": "Specific settings, scripts, and data operations demonstrated",
                "headers": ["Execution lever", "Exact practitioner setting or workflow", "Expert Source"],
                "rows": [
                    [
                        "Start paid bidding below the recommendation while watching actual daily delivery.",
                        "Holmgren starts manual bidding at roughly two-thirds of the recommendation and checks budget spending.",
                        "Adam Holmgren ([qy4FW_qglNo @ 00:04:47])",
                    ],
                    [
                        "Use relevant client proof instead of an immediate meeting demand.",
                        "Jay waits 48 hours after acceptance, engages with two or three posts, then shares value.",
                        "Lead Gen Jay ([R32IyS7IErQ @ 00:05:36])",
                    ],
                    [
                        "Budget for the list-building product before automating the sending process.",
                        "Cleverly quotes Sales Navigator at about $120 monthly and suggests around 20 requests daily.",
                        "Cleverly | #1 B2B Lead Generation Agency ([h66nRoG6w0E @ 00:00:28]); Cleverly | #1 B2B Lead Generation Agency ([h66nRoG6w0E @ 00:09:42])",
                    ],
                    [
                        "Import influencer audiences through the appropriate LinkedIn search URL.",
                        "Berman uses connections-of searches when connected and followers-of searches when not connected.",
                        "Alex Berman ([Kjfkoa15cNU @ 00:06:01]); Alex Berman ([Kjfkoa15cNU @ 00:06:52])",
                    ],
                    [
                        "Compare employment records using a profile that persists across jobs.",
                        "Saruggia keeps the LinkedIn URL as the identifier while employer and work email change.",
                        "Michael Saruggia - GTM Engineering ([DHX8uoA53OI @ 00:09:45])",
                    ],
                    [
                        "Request missing CRM information without replacing information already held.",
                        "AIMS specifies missing fields, email verification, waterfall enrichment, and preservation of existing data.",
                        "AIMS Consulting Services ([fk7OXnsQu-o @ 00:03:25]); AIMS Consulting Services ([fk7OXnsQu-o @ 00:03:57])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small details inside the working playbooks",
                "body": "These are specific adjustments the practitioners make inside their own acquisition and enrichment routines.",
                "items": [
                    (
                        "Separate social engagement from product curiosity: Holmgren edits "
                        "thought-leader posts before sponsorship to add a site link, then "
                        "looks for landing-page clicks above 10% of total social actions. "
                        "[Adam Holmgren — qy4FW_qglNo @ 00:06:42] "
                        "[Adam Holmgren — qy4FW_qglNo @ 00:07:00]"
                    ),
                    (
                        "Put the segment's reason for relevance in the first six words of "
                        "the connection request; Cleverly uses this to make persona-based "
                        "copy look personal rather than generic. "
                        "[Cleverly | #1 B2B Lead Generation Agency — h66nRoG6w0E @ 00:10:30]"
                    ),
                    (
                        "Change the follow-up medium: Will Aitken favors a casual video or "
                        "voice note around 30 seconds, often recorded while walking outside, "
                        "and adds context to the original question. "
                        "[Sales Feed — 3_RnVI6UFkA @ 00:13:35]"
                    ),
                    (
                        "Check the last enrichment date before requesting another run. "
                        "RevPartners prompts representatives to consider whether another "
                        "enrichment is necessary when the previous one was less than 30 "
                        "days earlier. "
                        "[RevPartners - RevOps + GTM Engineering on HubSpot — jV1Kp0j9lp0 @ 00:44:08]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build the target list around fit and activity",
                    "action": "Use Sales Navigator to isolate the audience and inspect recent activity.",
                    "detail": (
                        "Jack begins with Sales Navigator and targets active leads, including "
                        "people posting within the last 30 days. They demonstrate a personal "
                        "injury audience narrowing from 28,000 results to 2,500, then use "
                        "LinkedIn response data to decide where deeper enrichment and email "
                        "investment belong. "
                        "[Jack — 4RYnbUHayhM @ 00:03:11] "
                        "[Jack — 4RYnbUHayhM @ 00:03:37]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Make the profile and content answer the buyer's questions",
                    "action": "Set a clear follow proposition, next-step links, and a repeatable publishing mix.",
                    "detail": (
                        "Clark asks for one clear reason to follow, featured links leading "
                        "to the site and a newsletter or lead magnet, and a five-post week "
                        "starting with a 1:3:1 top-, middle-, and bottom-of-funnel mix. "
                        "[Tommy Clark — MXBaHCO4WI8 @ 00:06:52] "
                        "[Tommy Clark — MXBaHCO4WI8 @ 00:10:06]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Turn observed relevance into a short conversation",
                    "action": "Make an observation, ask a relevant question, and establish interest before booking.",
                    "detail": (
                        "Simmons uses one or two lines rather than an essay, pairing an "
                        "observation with a question. Greening-James checks pain and urgency, "
                        "then commonly offers two meeting times instead of immediately "
                        "sending a calendar link. "
                        "[HubSpot Marketing — uPo9D-wZv6s @ 00:08:15] "
                        "[Ben Greening-James — Lw2iBa2oM44 @ 00:24:44]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Return useful data and maintain employment changes",
                    "action": "Fill missing fields, preserve existing information, and schedule employment checks.",
                    "detail": (
                        "AIMS requests enrichment without overwriting existing information "
                        "and reviews the returned report before CRM updates. Saruggia "
                        "schedules monthly employer comparisons, marks departed contacts, "
                        "and reconciles their new contact and account information. "
                        "[AIMS Consulting Services — fk7OXnsQu-o @ 00:03:57] "
                        "[AIMS Consulting Services — fk7OXnsQu-o @ 00:05:10] "
                        "[Michael Saruggia - GTM Engineering — DHX8uoA53OI @ 00:10:19]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "There is no single practitioner agreement on how a profile should "
                    "look or how often its owner should publish. Tommy Clark recommends "
                    "a straightforward corporate headshot, explicitly rejects AI for "
                    "that picture, and says the header matters relatively little. Alex "
                    "Berman wants a distinctive photo and gives the banner, headline, "
                    "and custom button central roles in the funnel; they are comfortable "
                    "using ChatGPT to fill out supporting profile sections. Ross Simmons "
                    "also treats the banner as a billboard and encourages AI headshot "
                    "tools when someone lacks a good photograph. The writing advice "
                    "diverges as well: Clark wants the about section written personally, "
                    "while Berman says the less important profile material can be "
                    "generated. Publishing frequency is another explicit split. Clark's "
                    "starting cadence is five weekly posts, mostly middle-of-funnel "
                    "thought leadership. Lead Gen Jay says tests of posting three to "
                    "five times daily and spamming comments failed across more than "
                    "100 agencies; their recommendation is three weekly posts centered "
                    "on client problems and case-study proof. Jay's failed high-volume "
                    "routine is not Clark's five-post week. The actual alternatives "
                    "are different photo preferences, different uses of AI, and different "
                    "content schedules tied to the practitioners' own approaches. "
                    "[MXBaHCO4WI8 @ 00:05:11] [Kjfkoa15cNU @ 00:01:25] "
                    "[uPo9D-wZv6s @ 00:03:23] [R32IyS7IErQ @ 00:00:47]"
                ),
                (
                    "Automation creates the sharpest operating disagreement. Patrick Dang "
                    "says manual connection requests and personally written messages "
                    "work better for their team, because the automation they tried "
                    "limited how quickly they could complete the work. They track "
                    "prospects in a Google Sheet and use a conversational framework "
                    "rather than a fixed sales script. Expandi takes the opposite "
                    "position, criticizing untracked manual work and fragmented tools "
                    "while demonstrating profile visits, conditional connection "
                    "requests, messages, email fallback, and campaign analytics in one "
                    "system. Ben Greening-James occupies the middle: start manually "
                    "when learning, then use Prosp for connection requests, profile "
                    "engagement, and the soft opener before a human handles replies. "
                    "Will Aitken on Sales Feed prefers a blank connection request "
                    "unless the note is genuinely highly personalized. Their outreach "
                    "then uses an observation plus a short question, followed by "
                    "video or voice for additional context. They usually stop LinkedIn "
                    "follow-up after that unanswered attempt, keeping the channel "
                    "available for a later return. These choices also differ in "
                    "what the operator is optimizing: Dang emphasizes completing "
                    "personal conversations quickly, Expandi emphasizes a unified "
                    "automated workflow, Greening-James separates preparation from "
                    "human dialogue, and Aitken emphasizes preserving access to the buyer. "
                    "[lzh20RhrVW4 @ 00:16:13] [IqCv6BL9r6o @ 00:02:37] "
                    "[Lw2iBa2oM44 @ 00:13:04] [3_RnVI6UFkA @ 00:15:46]"
                ),
                (
                    "The CRM implementations differ in scope and in how much architecture "
                    "they put between enrichment and the sales team. Jacob Tuwiner "
                    "positions Sculpted around Clay, HubSpot, and a proprietary integration "
                    "layer with enrichment rules that they say extend beyond Clay's "
                    "basic import use cases. RevPartners demonstrates webhook-driven "
                    "tables, mapped HubSpot properties, custom prospecting cards, and "
                    "account ownership tiers. Their highest-intent accounts receive "
                    "personalized multichannel attention, while good-fit accounts "
                    "without intent stay with marketing rather than receiving active "
                    "outbound. AIMS Consulting Services demonstrates a more direct "
                    "prompt-and-skill route through Claude Code and MoltSets, then "
                    "names Phantom Buster as an alternative for HubSpot enrichment "
                    "and job-change tracking. Jack starts elsewhere again: use "
                    "LinkedIn outreach as a litmus test before deeper enrichment "
                    "through Clay and Apollo and before investing in larger email "
                    "activity. They describe learning which client types respond "
                    "before allowing those observations to influence the rest of "
                    "paid marketing. The distinction is visible in the work each "
                    "operator sells or demonstrates: Tuwiner emphasizes custom "
                    "HubSpot rules, RevPartners emphasizes assisted prospecting "
                    "inside an organized account system, AIMS emphasizes completing "
                    "missing CRM data, and Jack emphasizes finding responsive "
                    "segments before expanding acquisition spend. "
                    "[LxiIsByGTbU @ 00:02:14] [jV1Kp0j9lp0 @ 00:13:30] "
                    "[fk7OXnsQu-o @ 00:07:04] [4RYnbUHayhM @ 00:02:18]"
                ),
            ],
            "table": {
                "caption": "Keep these alternative playbooks distinct",
                "headers": ["Decision being made", "Contrasting practitioner positions", "Expert Source"],
                "rows": [
                    [
                        "Choose whether the connection request should contain any written note.",
                        "Simmons recommends a personalized explanation; Aitken favors blank requests unless the note is highly personalized.",
                        "HubSpot Marketing ([uPo9D-wZv6s @ 00:04:59]); Sales Feed ([3_RnVI6UFkA @ 00:06:08])",
                    ],
                    [
                        "Choose how soon the sequence introduces a meaningful business message.",
                        "Jay waits 48 hours after acceptance; Berman adds social proof 15 minutes after the opener.",
                        "Lead Gen Jay ([R32IyS7IErQ @ 00:05:36]); Alex Berman ([Kjfkoa15cNU @ 00:04:39])",
                    ],
                    [
                        "Choose between a manual prospecting routine and integrated campaign automation.",
                        "Dang reports better manual execution; Expandi promotes conditional campaigns with email fallback and live tracking.",
                        "Patrick Dang ([lzh20RhrVW4 @ 00:16:41]); Expandi ([IqCv6BL9r6o @ 00:02:50])",
                    ],
                    [
                        "Choose a publishing schedule rather than conflating different volume recommendations.",
                        "Clark starts with five posts weekly; Jay recommends three weekly case studies; Dang publishes daily.",
                        "Tommy Clark ([MXBaHCO4WI8 @ 00:09:54]); Lead Gen Jay ([R32IyS7IErQ @ 00:01:15]); Patrick Dang ([lzh20RhrVW4 @ 00:04:15])",
                    ],
                    [
                        "Choose how profile photography should support credibility and recognition.",
                        "Clark rejects AI headshots; Simmons encourages AI assistance when a suitable photograph is unavailable.",
                        "Tommy Clark ([MXBaHCO4WI8 @ 00:05:11]); HubSpot Marketing ([uPo9D-wZv6s @ 00:03:23])",
                    ],
                    [
                        "Choose which enrichment implementation matches the practitioner's demonstrated service scope.",
                        "Tuwiner emphasizes custom HubSpot rules; AIMS demonstrates a Claude Code skill and missing-field enrichment.",
                        "Jacob Tuwiner | AI Sales Automation ([LxiIsByGTbU @ 00:03:16]); AIMS Consulting Services ([fk7OXnsQu-o @ 00:02:23])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-economics",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Bad targeting is not an abstract warning in Ben Greening-James's "
                    "account. They searched for buyers agents, treated the list as "
                    "ready, and automated outreach about property services. One recipient "
                    "was a sports-car buyers agent, not a property buyers agent, and "
                    "responded by offering help buying a sports car. Greening-James "
                    "attributes the mismatch to inadequate filters and now emphasizes "
                    "Boolean qualification, company information, and checking the "
                    "lead list. Will Aitken describes the same title-matching problem "
                    "from the receiving side: their deliberately inflated title, "
                    "'Chief Vice President Director of Managing Things,' attracts "
                    "senders who assume they are a relevant executive. Lead Gen Jay "
                    "reports a separate failure at the messaging stage: sending "
                    "100 pitches daily produced zero responses. Their replacement "
                    "sequence waits after connection acceptance, engages with recent "
                    "posts, and offers a relevant resource before pursuing the "
                    "conversation. Greening-James also admits that early automated "
                    "pitching booked some calls, but says it damaged trust by "
                    "selling before establishing relevance or whether the recipient "
                    "was in the market. These firsthand stories identify distinct "
                    "breakpoints: a title can describe the wrong business, a senior-looking "
                    "headline can attract irrelevant sellers, and connection acceptance "
                    "does not mean someone wants an immediate pitch. "
                    "[Lw2iBa2oM44 @ 00:06:04] [3_RnVI6UFkA @ 00:01:00] "
                    "[R32IyS7IErQ @ 00:04:05]"
                ),
                (
                    "The tooling failures are equally concrete. Alex Berman says their "
                    "team spent more than a year and $100,000 building a LinkedIn "
                    "outreach tool, only for a LinkedIn code change shortly before "
                    "launch to invalidate the work and require thousands more in "
                    "repairs. AIMS Consulting Services hits a smaller but immediate "
                    "constraint during enrichment: the account has no phone tokens, "
                    "so Claude Code asks whether mobile-number extraction should "
                    "be skipped. The same demonstration identifies sample contacts "
                    "that should not be processed and presents a report before "
                    "writing the enriched information. RevPartners shows that an "
                    "enrichment request is not instant completion: new contacts "
                    "appear while company firmographics are still pending. Their "
                    "workflow records progress, errors, completion, and the last "
                    "enrichment date, and their presenter explains that the illustrated "
                    "automatic flow requires Clay Pro. Michael Saruggia adds the "
                    "record-reconciliation problem: a job change must not simply "
                    "produce another unchecked person record. Their routine looks "
                    "for an existing contact and lead, marks the old employment "
                    "record, and checks the account before creating or updating "
                    "the new destination. These are the operating details each "
                    "demonstration exposes beyond choosing an enrichment vendor "
                    "or connecting an outreach tool. "
                    "[Kjfkoa15cNU @ 00:02:58] [fk7OXnsQu-o @ 00:04:27] "
                    "[jV1Kp0j9lp0 @ 00:44:56] [DHX8uoA53OI @ 00:06:32]"
                ),
                (
                    "Read the reported numbers in the terms the operator actually "
                    "uses. Adam Holmgren is not judging LinkedIn advertising by "
                    "immediate ad-click-to-trial conversions: they describe repeated "
                    "exposure followed by later direct or branded visits. Their "
                    "thought-leader CTR includes social engagement, and they "
                    "separately inspect landing-page clicks; one retargeting example "
                    "shows zero landing-page clicks, which they say probably "
                    "explains why it was paused. Jack's workspace results are "
                    "connection acceptance and message response figures, while "
                    "their operating method uses LinkedIn response data to decide "
                    "which audiences deserve further email investment. Ben "
                    "Greening-James explicitly presents rough planning numbers: "
                    "100 weekly connection requests, 30% acceptance, 150 messages, "
                    "20% replies, and a 15% booking conversion leading to four "
                    "or five weekly meetings. Their example then applies a 10% "
                    "close rate to describe two monthly deals. Patrick Dang "
                    "reports five meetings daily but also describes an existing "
                    "YouTube audience exceeding 250,000 subscribers feeding "
                    "LinkedIn profile visits. Their routine combines that traffic "
                    "with daily posting and manual conversations. Holmgren's "
                    "brand-building account, Jack's workspace response data, "
                    "Greening-James's planning example, and Dang's audience-fed "
                    "meeting claim describe different measurements and different "
                    "operating setups, not one interchangeable acquisition result. "
                    "[qy4FW_qglNo @ 00:09:58] [4RYnbUHayhM @ 00:01:24] "
                    "[Lw2iBa2oM44 @ 00:26:07] [lzh20RhrVW4 @ 00:03:12]"
                ),
            ],
            "table": {
                "caption": "Reported breakdowns and the checks practitioners use",
                "headers": ["Observed trap or bottleneck", "Practitioner response or economic distinction", "Expert Source"],
                "rows": [
                    [
                        "A broad buyers-agent search delivered the wrong kind of buyer.",
                        "Greening-James reached a sports-car agent with property messaging and emphasizes stronger lead-list filters.",
                        "Ben Greening-James ([Lw2iBa2oM44 @ 00:06:34])",
                    ],
                    [
                        "A year of software development broke before the planned launch.",
                        "Berman reports $100,000 spent before a LinkedIn change required thousands more in repairs.",
                        "Alex Berman ([Kjfkoa15cNU @ 00:02:58])",
                    ],
                    [
                        "The enrichment account lacked the credits needed for phone extraction.",
                        "AIMS shows Claude Code identifying unavailable phone tokens and asking whether to skip mobile numbers.",
                        "AIMS Consulting Services ([fk7OXnsQu-o @ 00:04:39])",
                    ],
                    [
                        "A synchronization does not automatically mean every email was validated.",
                        "Tyler explains that validation depends on whether those steps were configured in the workflow.",
                        "RevPartners - RevOps + GTM Engineering on HubSpot ([jV1Kp0j9lp0 @ 00:52:04])",
                    ],
                    [
                        "Large engagement numbers can coexist with no landing-page clicks.",
                        "Holmgren identifies a zero-click retargeting example and says that probably explains its pause.",
                        "Adam Holmgren ([qy4FW_qglNo @ 00:09:58])",
                    ],
                    [
                        "Research automation still leaves ongoing operational work inside the business.",
                        "Diana describes revenue operations as a product rather than a project and recommends starting with one use case.",
                        "RevPartners - RevOps + GTM Engineering on HubSpot ([jV1Kp0j9lp0 @ 00:57:50])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks drawn from the practitioners' own breakdowns",
                "body": "Use the specific checks the operators attach to bad lists, incomplete enrichment, stale jobs, and misleading response signals.",
                "items": [
                    (
                        "Inspect what the job-title filter actually returns. Greening-James's "
                        "buyers-agent campaign reached a sports-car agent because the "
                        "qualification was too loose for the property offer. "
                        "[Ben Greening-James — Lw2iBa2oM44 @ 00:06:34]"
                    ),
                    (
                        "Check the enrichment budget and proposed changes before updating "
                        "the CRM. AIMS's run exposed missing phone tokens, excluded sample "
                        "contacts, and requested confirmation after producing the report. "
                        "[AIMS Consulting Services — fk7OXnsQu-o @ 00:04:27] "
                        "[AIMS Consulting Services — fk7OXnsQu-o @ 00:05:10]"
                    ),
                    (
                        "Reconcile the old and new employment records. Saruggia marks the "
                        "old contact as left company, checks both contacts and leads for "
                        "an existing new record, and checks whether the new account exists. "
                        "[Michael Saruggia - GTM Engineering — DHX8uoA53OI @ 00:06:32]"
                    ),
                    (
                        "Use LinkedIn response data before expanding the email investment. "
                        "Jack describes LinkedIn as the litmus test for deciding which "
                        "client types warrant the larger email effort and says the work "
                        "must be ROI positive to continue. "
                        "[Jack — 4RYnbUHayhM @ 00:02:18] "
                        "[Jack — 4RYnbUHayhM @ 00:02:32]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        "\"Your profile isn't just a resume. It's a landing page.\" "
        "— HubSpot Marketing (uPo9D-wZv6s @ 00:03:10)."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        (
            "Define the target customer and the offer, then validate demand through "
            "customer conversations or by examining comparable offers already being sold. "
            "[Patrick Dang — lzh20RhrVW4 @ 00:01:31]"
        ),
        (
            "Set the profile's follow proposition and featured destinations, and create "
            "a company page that clearly shows what the business does for clients. "
            "[Tommy Clark — MXBaHCO4WI8 @ 00:06:52] "
            "[Chris Prouty — 8yepbhYel-Q @ 00:00:50]"
        ),
        (
            "Publish problem-solution-result case studies and ask a specific question "
            "that identifies readers interested in the problem you solve. "
            "[Lead Gen Jay — R32IyS7IErQ @ 00:01:30] "
            "[Lead Gen Jay — R32IyS7IErQ @ 00:02:35]"
        ),
        (
            "Inspect incoming connections, content engagement, and profile viewers for "
            "offer fit, then begin short conversations using an observed detail and "
            "a relevant question. "
            "[Patrick Dang — lzh20RhrVW4 @ 00:08:56] "
            "[Sales Feed — 3_RnVI6UFkA @ 00:11:09]"
        ),
        (
            "Identify missing CRM fields, request enrichment without overwriting existing "
            "information, and examine token availability and the returned update report. "
            "[AIMS Consulting Services — fk7OXnsQu-o @ 00:03:57] "
            "[AIMS Consulting Services — fk7OXnsQu-o @ 00:04:39]"
        ),
        (
            "Schedule employer comparisons, reconcile departed contacts with new records, "
            "and expose enrichment status and the last enrichment date inside HubSpot. "
            "[Michael Saruggia - GTM Engineering — DHX8uoA53OI @ 00:10:19] "
            "[RevPartners - RevOps + GTM Engineering on HubSpot — jV1Kp0j9lp0 @ 00:43:52]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Adam Holmgren — LinkedIn Ads Strategy for B2B: The Exact Campaigns That Took Us from 0 to 200 Customers [00:10:31]",
            "url": "https://www.youtube.com/watch?v=qy4FW_qglNo&t=631s",
            "relevance": (
                "Primary practitioner testimony on advertising for brand recall "
                "rather than immediate ad-click conversion."
            ),
        },
        {
            "title": "Ben Greening-James — How I Sell B2B Services on LinkedIn (Step-by-Step) [00:06:04]",
            "url": "https://www.youtube.com/watch?v=Lw2iBa2oM44&t=364s",
            "relevance": (
                "Primary practitioner testimony on a real targeting failure caused "
                "by an insufficiently qualified buyers-agent list."
            ),
        },
        {
            "title": "RevPartners - RevOps + GTM Engineering on HubSpot — Revolutionize Your Sales: Automated AI Prospecting with HubSpot & Clay [00:43:15]",
            "url": "https://www.youtube.com/watch?v=jV1Kp0j9lp0&t=2595s",
            "relevance": (
                "Primary practitioner testimony on HubSpot properties that trigger "
                "company enrichment, new-contact discovery, and contact enrichment."
            ),
        },
        {
            "title": "Michael Saruggia - GTM Engineering — Fix Your CRM Data With Clay.Com (Job Changes Problem) [00:09:45]",
            "url": "https://www.youtube.com/watch?v=DHX8uoA53OI&t=585s",
            "relevance": (
                "Primary practitioner testimony on persistent LinkedIn profile "
                "identifiers and reconciliation of old employment records."
            ),
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "qy4FW_qglNo",
            "title": "LinkedIn Ads Strategy for B2B: The Exact Campaigns That Took Us from 0 to 200 Customers",
            "channel": "Adam Holmgren",
            "author": "Adam Holmgren",
            "text": "We are not trying to create conversions from these ads. We are trying to get them to remember me, to remember Fibbler as a brand.",
            "tip": "We are not trying to create conversions from these ads. We are trying to get them to remember me, to remember Fibbler as a brand.",
            "timestamp": 631,
            "timestamp_seconds": 631,
            "timestamp_label": "[00:10:31]",
            "url": "https://www.youtube.com/watch?v=qy4FW_qglNo&t=631s",
            "markdown": "[00:10:31](https://www.youtube.com/watch?v=qy4FW_qglNo&t=631s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "MXBaHCO4WI8",
            "title": "The Best LinkedIn Lead Generation Strategy for 2026",
            "channel": "Tommy Clark",
            "author": "Tommy Clark",
            "text": "One of those posts should be top of funnel, three of those posts should be middle of funnel, one of those posts should be bottom of funnel. This is a good starting point.",
            "tip": "One of those posts should be top of funnel, three of those posts should be middle of funnel, one of those posts should be bottom of funnel. This is a good starting point.",
            "timestamp": 606,
            "timestamp_seconds": 606,
            "timestamp_label": "[00:10:06]",
            "url": "https://www.youtube.com/watch?v=MXBaHCO4WI8&t=606s",
            "markdown": "[00:10:06](https://www.youtube.com/watch?v=MXBaHCO4WI8&t=606s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "R32IyS7IErQ",
            "title": "How To Land Clients With LinkedIn (3 Exclusive Tactics)",
            "channel": "Lead Gen Jay",
            "author": "Lead Gen Jay",
            "text": "After they accept you're going to wait 48 hours before sending any outreach. Don't fall into the trap of instant messaging.",
            "tip": "After they accept you're going to wait 48 hours before sending any outreach. Don't fall into the trap of instant messaging.",
            "timestamp": 336,
            "timestamp_seconds": 336,
            "timestamp_label": "[00:05:36]",
            "url": "https://www.youtube.com/watch?v=R32IyS7IErQ&t=336s",
            "markdown": "[00:05:36](https://www.youtube.com/watch?v=R32IyS7IErQ&t=336s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8yepbhYel-Q",
            "title": "B2B LinkedIn Content Marketing - How To Get B2B Clients From LinkedIn",
            "channel": "Chris Prouty",
            "author": "Chris Prouty",
            "text": "The first tip I'm going to give you is to optimize your LinkedIn company page.",
            "tip": "The first tip I'm going to give you is to optimize your LinkedIn company page.",
            "timestamp": 50,
            "timestamp_seconds": 50,
            "timestamp_label": "[00:00:50]",
            "url": "https://www.youtube.com/watch?v=8yepbhYel-Q&t=50s",
            "markdown": "[00:00:50](https://www.youtube.com/watch?v=8yepbhYel-Q&t=50s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Kjfkoa15cNU",
            "title": "How I Do LinkedIn Outreach in 2026",
            "channel": "Alex Berman",
            "author": "Alex Berman",
            "text": "Hey first name, are you running cold email campaigns for company name?",
            "tip": "I start with a question asking whether they are running cold email campaigns for their company.",
            "timestamp": 222,
            "timestamp_seconds": 222,
            "timestamp_label": "[00:03:42]",
            "url": "https://www.youtube.com/watch?v=Kjfkoa15cNU&t=222s",
            "markdown": "[00:03:42](https://www.youtube.com/watch?v=Kjfkoa15cNU&t=222s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "uPo9D-wZv6s",
            "title": "The Latest LinkedIn Lead Generation Strategies That Generated $2M+ (No Cold InMails)",
            "channel": "HubSpot Marketing",
            "author": "HubSpot Marketing",
            "text": "Your profile isn't just a resume. It's a landing page.",
            "tip": "Your profile isn't just a resume. It's a landing page.",
            "timestamp": 190,
            "timestamp_seconds": 190,
            "timestamp_label": "[00:03:10]",
            "url": "https://www.youtube.com/watch?v=uPo9D-wZv6s&t=190s",
            "markdown": "[00:03:10](https://www.youtube.com/watch?v=uPo9D-wZv6s&t=190s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "h66nRoG6w0E",
            "title": "The Only LinkedIn Outreach Strategy You Need in 2026",
            "channel": "Cleverly | #1 B2B Lead Generation Agency",
            "author": "Cleverly | #1 B2B Lead Generation Agency",
            "text": "You want to mention that in the first six words of your connection request, so it looks personal. Doesn't look copy-paste.",
            "tip": "You want to mention that in the first six words of your connection request, so it looks personal. Doesn't look copy-paste.",
            "timestamp": 630,
            "timestamp_seconds": 630,
            "timestamp_label": "[00:10:30]",
            "url": "https://www.youtube.com/watch?v=h66nRoG6w0E&t=630s",
            "markdown": "[00:10:30](https://www.youtube.com/watch?v=h66nRoG6w0E&t=630s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "Lw2iBa2oM44",
            "title": "How I Sell B2B Services on LinkedIn (Step-by-Step)",
            "channel": "Ben Greening-James",
            "author": "Ben Greening-James",
            "text": "I always just tell people to leave their connection request blank and it significantly increases the amount of connection acceptance rates that you get.",
            "tip": "I always just tell people to leave their connection request blank and it significantly increases the amount of connection acceptance rates that you get.",
            "timestamp": 616,
            "timestamp_seconds": 616,
            "timestamp_label": "[00:10:16]",
            "url": "https://www.youtube.com/watch?v=Lw2iBa2oM44&t=616s",
            "markdown": "[00:10:16](https://www.youtube.com/watch?v=Lw2iBa2oM44&t=616s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "lzh20RhrVW4",
            "title": "How To Get Clients On LinkedIn (Full Lead Generation Masterclass)",
            "channel": "Patrick Dang",
            "author": "Patrick Dang",
            "text": "We just find that doing it manually works better for us, manually connecting, manually writing each message, not using a sales script.",
            "tip": "We just find that doing it manually works better for us, manually connecting, manually writing each message, not using a sales script.",
            "timestamp": 1001,
            "timestamp_seconds": 1001,
            "timestamp_label": "[00:16:41]",
            "url": "https://www.youtube.com/watch?v=lzh20RhrVW4&t=1001s",
            "markdown": "[00:16:41](https://www.youtube.com/watch?v=lzh20RhrVW4&t=1001s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "IqCv6BL9r6o",
            "title": "The Best LinkedIn Outreach Strategy for 2026",
            "channel": "Expandi",
            "author": "Expandi",
            "text": "For the first step, we're going to visit the lead's profile. This warms up the contact, tells LinkedIn that you're active, and they get a notification before you actually send the message.",
            "tip": "For the first step, we're going to visit the lead's profile. This warms up the contact, tells LinkedIn that you're active, and they get a notification before you actually send the message.",
            "timestamp": 282,
            "timestamp_seconds": 282,
            "timestamp_label": "[00:04:42]",
            "url": "https://www.youtube.com/watch?v=IqCv6BL9r6o&t=282s",
            "markdown": "[00:04:42](https://www.youtube.com/watch?v=IqCv6BL9r6o&t=282s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "3_RnVI6UFkA",
            "title": "The Best LinkedIn Lead Generation Strategy for 2026",
            "channel": "Sales Feed",
            "author": "Sales Feed",
            "text": "The goal here is not to book a meeting with that very first message. The goal here is to get a response.",
            "tip": "The goal here is not to book a meeting with that very first message. The goal here is to get a response.",
            "timestamp": 739,
            "timestamp_seconds": 739,
            "timestamp_label": "[00:12:19]",
            "url": "https://www.youtube.com/watch?v=3_RnVI6UFkA&t=739s",
            "markdown": "[00:12:19](https://www.youtube.com/watch?v=3_RnVI6UFkA&t=739s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "4RYnbUHayhM",
            "title": "How to Get B2B Clients on LinkedIn in 2026 (Intent-Based Outreach System)",
            "channel": "Jack",
            "author": "Jack",
            "text": "Last year alone in this workspace, sent out about 31,000 connections. We got 34% of those back and we sent out close to 10,000 messages with about 26% of those coming back.",
            "tip": "Last year alone in this workspace, sent out about 31,000 connections. We got 34% of those back and we sent out close to 10,000 messages with about 26% of those coming back.",
            "timestamp": 84,
            "timestamp_seconds": 84,
            "timestamp_label": "[00:01:24]",
            "url": "https://www.youtube.com/watch?v=4RYnbUHayhM&t=84s",
            "markdown": "[00:01:24](https://www.youtube.com/watch?v=4RYnbUHayhM&t=84s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "fk7OXnsQu-o",
            "title": "Auto-Enrich 1,000+ CRM Contacts Using Claude Code + MoltSets",
            "channel": "AIMS Consulting Services",
            "author": "AIMS Consulting Services",
            "text": "The idea is very simple. Identify what's missing, enrich those records and update it back onto the CRM.",
            "tip": "The idea is very simple. Identify what's missing, enrich those records and update it back onto the CRM.",
            "timestamp": 38,
            "timestamp_seconds": 38,
            "timestamp_label": "[00:00:38]",
            "url": "https://www.youtube.com/watch?v=fk7OXnsQu-o&t=38s",
            "markdown": "[00:00:38](https://www.youtube.com/watch?v=fk7OXnsQu-o&t=38s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "jV1Kp0j9lp0",
            "title": "Revolutionize Your Sales: Automated AI Prospecting with HubSpot & Clay",
            "channel": "RevPartners - RevOps + GTM Engineering on HubSpot",
            "author": "RevPartners - RevOps + GTM Engineering on HubSpot",
            "text": "If you set up your workflow to validate every work email, then totally. But it's depending on how you configure it.",
            "tip": "If you set up your workflow to validate every work email, then totally. But it's depending on how you configure it.",
            "timestamp": 3124,
            "timestamp_seconds": 3124,
            "timestamp_label": "[00:52:04]",
            "url": "https://www.youtube.com/watch?v=jV1Kp0j9lp0&t=3124s",
            "markdown": "[00:52:04](https://www.youtube.com/watch?v=jV1Kp0j9lp0&t=3124s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "DHX8uoA53OI",
            "title": "Fix Your CRM Data With Clay.Com (Job Changes Problem)",
            "channel": "Michael Saruggia - GTM Engineering",
            "author": "Michael Saruggia - GTM Engineering",
            "text": "From Adidas you move into Apple but the LinkedIn profile does not change.",
            "tip": "From Adidas you move into Apple but the LinkedIn profile does not change.",
            "timestamp": 585,
            "timestamp_seconds": 585,
            "timestamp_label": "[00:09:45]",
            "url": "https://www.youtube.com/watch?v=DHX8uoA53OI&t=585s",
            "markdown": "[00:09:45](https://www.youtube.com/watch?v=DHX8uoA53OI&t=585s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "LxiIsByGTbU",
            "title": "The CRM Data Problem & How We Solve It with Clay",
            "channel": "Jacob Tuwiner | AI Sales Automation",
            "author": "Jacob Tuwiner | AI Sales Automation",
            "text": "Sales reps start wasting tons of time going through horrible accounts that aren't actually qualified and doing manual research as opposed to just selling. Marketing can't segment properly. Leadership has very low visibility to what's actually going on on the ground.",
            "tip": "Sales reps start wasting tons of time going through horrible accounts that aren't actually qualified and doing manual research as opposed to just selling. Marketing can't segment properly. Leadership has very low visibility to what's actually going on on the ground.",
            "timestamp": 120,
            "timestamp_seconds": 120,
            "timestamp_label": "[00:02:00]",
            "url": "https://www.youtube.com/watch?v=LxiIsByGTbU&t=120s",
            "markdown": "[00:02:00](https://www.youtube.com/watch?v=LxiIsByGTbU&t=120s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Verbatim practitioner testimony from Chapter Q6.",
        },
    ],
}

# Keep the source statement declarative while retaining Berman's spoken opener.
CHAPTER_6["source_citations"][4]["text"] = (
    "I start with, 'Hey first name, are you running cold email campaigns for company name?'."
)
