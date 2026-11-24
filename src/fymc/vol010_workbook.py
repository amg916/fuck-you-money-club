from __future__ import annotations

import json


def build_volume_010_workbook() -> dict:
    def field(name: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": "textarea",
            "prompt": prompt,
            "example": example,
        }

    def worksheet(
        number: int,
        title: str,
        purpose: str,
        chapter_ref: str,
        instructions: list,
        fields: list,
        completion_gate: str,
    ) -> dict:
        return {
            "worksheet_id": "ws-{0:02d}".format(number),
            "number": number,
            "title": title,
            "purpose": purpose,
            "chapter_ref": chapter_ref,
            "instructions": instructions,
            "fields": fields,
            "completion_gate": completion_gate,
        }

    worksheets = [
        worksheet(
            1,
            "Local Assets, Commercial Intent, and Keyword Selection",
            (
                "Document the local business opportunity, its proposed payment "
                "mechanism, and the search-result evidence behind the selected "
                "pages using the Q1 and Q2 practitioner examples."
            ),
            "Q1: Rank & Rent, Real-Estate SEO & Local GBP; "
            "Q2: Keyword Research, Clustering & Topical Opportunity",
            [
                "Begin with the business's buyer or seller language rather than "
                "choosing a subject only because its traffic is larger.",
                "Record the proposed local asset and payment arrangement separately "
                "from the keyword and page decisions.",
                "Inspect actual search results, competing titles, and competing "
                "page formats before assigning phrases to a landing page.",
                "Separate keyword grouping from keyword qualification, and separate "
                "published pages from topics already ranking.",
                "Use the cited examples as testimony records; enter your own "
                "observations in the printable spaces without replacing the "
                "speakers' reported figures.",
            ],
            [
                field(
                    "Buyer or seller intent",
                    (
                        "Identify the buyer or seller question your proposed page "
                        "answers. Contrast its commercial purpose with a broader "
                        "local information topic, and record the business outcome "
                        "that makes the narrower question worth addressing."
                    ),
                    (
                        "Real Estate SEO & Web Design contrasts the higher-traffic "
                        "activities article with the living-in-Lake-St.-Louis "
                        "article. The latter brought a buyer associated with a "
                        "reported $1.3 million waterfront transaction. This example "
                        "records the article and transaction together rather than "
                        "selecting the activities topic merely for its traffic. "
                        "[Real Estate SEO & Web Design — xDMs5FogvQ8 @ 00:03:19]"
                    ),
                ),
                field(
                    "Local asset payment arrangement",
                    (
                        "Describe whether the local website would receive fixed "
                        "rent, commission, or the proposed hybrid payment. Keep "
                        "the payment arrangement distinct from rankings, and note "
                        "how the speaker connects rental income with additional properties."
                    ),
                    (
                        "Ippei reports that the Grand Rapids tree-service website "
                        "continues producing $2,000 per month. In discussing a "
                        "proposed hybrid, the fixed rental portion funds more "
                        "properties while commission supplies additional upside. "
                        "These are the speaker's rental example and proposed "
                        "arrangement, rather than one interchangeable payment model. "
                        "[Ippei - Rank and Rent SEO — uJ0bhk9MeDE @ 00:07:50] "
                        "[Ippei - Rank and Rent SEO — uJ0bhk9MeDE @ 00:20:44]"
                    ),
                ),
                field(
                    "Market pages and question format",
                    (
                        "List the areas the business actually serves and the "
                        "questions people type about them. Describe which market "
                        "pages come first, where a short answer belongs, and "
                        "which additional areas could be added later."
                    ),
                    (
                        "AeroIDX recommends starting with a few areas that the "
                        "agent actually sells, then adding more every month. "
                        "For frequently asked questions, the channel recommends "
                        "using the wording people type and placing a short "
                        "answer first. The example connects geographic scope "
                        "with a specific answer format. "
                        "[AeroIDX — 6etBe1gPZqE @ 00:05:33] "
                        "[AeroIDX — 6etBe1gPZqE @ 00:02:46]"
                    ),
                ),
                field(
                    "Homepage category connections",
                    (
                        "Record the homepage categories and their corresponding "
                        "detailed pages. Explain how each category description "
                        "would introduce its destination, preserving the surrounding "
                        "topic rather than treating the link as detached from "
                        "the page's local business context."
                    ),
                    (
                        "Caleb Ulku's Core 30 discussion connects each homepage "
                        "category description to its corresponding detailed page "
                        "while preserving topical context. Manan Gupta separately "
                        "describes grouping similar keywords into clusters and "
                        "building a dedicated landing page for each cluster. "
                        "Together, these entries document category connections "
                        "and clustered page assignment. "
                        "[Caleb Ulku — nW4AstHjEtc @ 00:10:29] "
                        "[Manan Gupta — _DewVbSSXe0 @ 00:06:14]"
                    ),
                ),
                field(
                    "Local ranking report conditions",
                    (
                        "Describe the listing's existing SEO foundation and the "
                        "conditions under which its ranking report is collected. "
                        "Record opening hours alongside map coverage so that "
                        "a reported visibility change remains attached to the "
                        "speaker's measurement conditions."
                    ),
                    (
                        "Map Ranking reports an electrician's top-three city "
                        "coverage moving from 21% to 74%. The channel also "
                        "says to check opening hours before a ranking report "
                        "because closed-hours scans alter results. Its separate "
                        "readiness recommendation excludes brand-new listings "
                        "or listings without an SEO foundation. "
                        "[Map Ranking — uH-42eKssR4 @ 00:03:03] "
                        "[Map Ranking — a_7c98JU32w @ 00:04:26] "
                        "[Map Ranking — uH-42eKssR4 @ 00:04:34]"
                    ),
                ),
                field(
                    "Product language and intent",
                    (
                        "Write down the language associated with the products "
                        "being sold, then identify which phrases express "
                        "commercial or transactional intent. Explain how this "
                        "language would guide page selection rather than letting "
                        "a grouping feature choose the opportunity."
                    ),
                    (
                        "Edward Sturm instructs viewers to write down language "
                        "corresponding to the products they sell. Travis Wilkie "
                        "demonstrates switching to commercial and transactional "
                        "intent. Tutorial Stack adds that a phrase appearing "
                        "in a sidebar group still requires further research, "
                        "including difficulty and volume checks before selection. "
                        "[Edward Sturm — 8DuIlUdfY_w @ 00:15:53] "
                        "[Travis Wilkie — wSkIVyKv2rY @ 00:00:53] "
                        "[Tutorial Stack — fLGvfe6OTgc @ 00:02:52]"
                    ),
                ),
                field(
                    "Cluster evidence and destination",
                    (
                        "Record a candidate keyword cluster, its displayed "
                        "difficulty and aggregate volume, and the destination "
                        "you would inspect. Check whether ranking URLs already "
                        "use dedicated pages before deciding that the cluster "
                        "belongs on a main service page."
                    ),
                    (
                        "Robbie Richards demonstrates a car-accident attorney "
                        "cluster containing eight keywords, 5% difficulty, and "
                        "950 aggregate volume. The walkthrough also recommends "
                        "hovering over ranking URLs to see whether dedicated "
                        "competing pages exist before assigning a phrase to "
                        "the main service page. The displayed metrics accompany "
                        "that page-selection inspection. "
                        "[Robbie Richards — P5ET0IvFReQ @ 00:02:38] "
                        "[Robbie Richards — P5ET0IvFReQ @ 00:02:50] "
                        "[Robbie Richards — P5ET0IvFReQ @ 00:03:19]"
                    ),
                ),
                field(
                    "Manual competition inspection",
                    (
                        "Compare the displayed keyword difficulty with the "
                        "titles actually ranking for the exact query. Record "
                        "whether competitors explicitly target the phrase, and "
                        "explain how that observation changes your interpretation "
                        "of an apparently accessible keyword."
                    ),
                    (
                        "WeStudyFunnels examines a treadmill-under-$1,000 query "
                        "showing KD 30 and 3,600 searches, then identifies "
                        "fifteen leading results with matching title targeting. "
                        "The speaker uses that inspection to show why a "
                        "low backlink-led difficulty score can coexist with "
                        "strong domains actively pursuing the exact phrase. "
                        "[WeStudyFunnels — PpHWPSjRYPI @ 00:01:51] "
                        "[WeStudyFunnels — PpHWPSjRYPI @ 00:02:06] "
                        "[WeStudyFunnels — PpHWPSjRYPI @ 00:04:06] "
                        "[WeStudyFunnels — PpHWPSjRYPI @ 00:05:39]"
                    ),
                ),
                field(
                    "Expected page format",
                    (
                        "Open competing pages within the proposed cluster and "
                        "describe the format they actually use. Compare that "
                        "format with your planned destination, and record the "
                        "parent topic and subtopics without assuming grouping "
                        "alone establishes the correct content."
                    ),
                    (
                        "Travis Wilkie's keto-cookie inspection opens competing "
                        "pages and reveals recipes, making the expected format "
                        "visible rather than guessed. Ahrefs Product Updates "
                        "demonstrates beginning with parent-topic grouping and "
                        "then inspecting the subtopics within a selected parent. "
                        "The two demonstrations supply different parts of the "
                        "cluster examination. "
                        "[Travis Wilkie — 0qP8UUWuBSc @ 00:03:06] "
                        "[Ahrefs Product Updates — JMyPIbu7vhw @ 00:02:08]"
                    ),
                ),
                field(
                    "Contested silo and advancement",
                    (
                        "Separate the number of published topics from topics "
                        "ranking in the measured range. Identify the contested "
                        "silo with the smallest gap, then record what evidence "
                        "would support advancing or reassessing the next "
                        "cornerstone in the cluster."
                    ),
                    (
                        "Floyi counts coverage through topics ranking in the "
                        "top 20, not simply published pages, and prioritizes "
                        "contested silos with the smallest gap. David G. "
                        "Quaid's testimony on James Dooley says to stop "
                        "advancing and reassess when the next cornerstone "
                        "receives no clicks after the described wait. "
                        "[Topical Authority SEO | Floyi — 0XswjN-Lops @ 00:01:18] "
                        "[Topical Authority SEO | Floyi — 0XswjN-Lops @ 00:01:37] "
                        "[James Dooley — mE2Y-3fNorE @ 00:06:07]"
                    ),
                ),
            ],
            (
                "Complete the commercial-intent and page-selection records before "
                "advancing the cluster; retain the distinction between published "
                "coverage and top-20 ranking coverage. "
                "[Topical Authority SEO | Floyi — 0XswjN-Lops @ 00:01:18]"
            ),
        ),
        worksheet(
            2,
            "Semantic Architecture and Programmatic Publishing",
            (
                "Translate contextual page boundaries into connected resources, "
                "then document the data, templates, review steps, and maintenance "
                "described in the Q3 and Q4 demonstrations."
            ),
            "Q3: Semantic Authority, Site Architecture & Internal Links; "
            "Q4: Programmatic SEO & AI Content Workflows",
            [
                "Define the source context, central entity, and central search "
                "intent before listing proposed pages.",
                "Group attributes that belong together rather than creating a "
                "separate URL for every minor query.",
                "Map supporting articles, category destinations, and homepage "
                "routes before describing publication scale.",
                "Match dataset fields to template fields and record what the "
                "reader can actually do on the resulting page.",
                "Retain draft review, neighborhood-specific inspection, and "
                "maintenance work in the completed publishing plan.",
            ],
            [
                field(
                    "Topical map foundations",
                    (
                        "Define the source context, central entity, central "
                        "search intent, core section, and outer section for "
                        "the proposed site. Explain how these foundations shape "
                        "the content network rather than treating the map "
                        "as a keyword list."
                    ),
                    (
                        "Behzad Hussain describes an opening phase built "
                        "around five fundamentals: source context, central "
                        "entity, central search intent, core section, and "
                        "outer section. The wider proposed production series "
                        "contains 26 micro steps spanning fundamentals, research, "
                        "processing, and publication planning. This example "
                        "records the foundations before the individual pages. "
                        "[Behzad Hussain — NQCo-V1utn8 @ 00:01:45] "
                        "[Behzad Hussain — NQCo-V1utn8 @ 00:00:38]"
                    ),
                ),
                field(
                    "Contextual URL boundaries",
                    (
                        "Identify attributes that can share a page and "
                        "contexts that require separate destinations. Explain "
                        "the reader task behind each boundary, avoiding a "
                        "plan that opens new URLs merely because additional "
                        "minor query variations have been found."
                    ),
                    (
                        "Koray Tuğberk GÜBÜR groups some casino attributes "
                        "on the same page when their contexts fit together. "
                        "In another discussion, Koray warns that opening "
                        "pages randomly for minor queries dilutes ranking "
                        "signals. The example therefore records contextual "
                        "grouping and the stated objection to unnecessary "
                        "page separation together. "
                        "[Koray Tuğberk GÜBÜR — bWjlnI4gXxo @ 00:01:06] "
                        "[Koray Tuğberk GÜBÜR — qrDPul4eAYw @ 01:08:25]"
                    ),
                ),
                field(
                    "Task and page component",
                    (
                        "Describe the task the page should let a visitor "
                        "perform and the component that communicates that "
                        "task. Record how functionality participates in the "
                        "page's accuracy, instead of describing accuracy only "
                        "as factual statements in text."
                    ),
                    (
                        "Koray Tuğberk GÜBÜR's exact-match-domain example "
                        "uses a direct upload component instead of an "
                        "ordinary button. In the accuracy discussion, Koray "
                        "says accuracy concerns document functionality as "
                        "well as factuality. The worksheet example keeps "
                        "the visible task component connected with that "
                        "broader explanation of document accuracy. "
                        "[Koray Tuğberk GÜBÜR — WrU25krFCtk @ 00:05:31] "
                        "[Koray Tuğberk GÜBÜR — X_ou1eO28gE @ 00:15:40]"
                    ),
                ),
                field(
                    "Hub and category routes",
                    (
                        "Identify the central resource, its supporting "
                        "articles, and any category page that serves a "
                        "search destination. Describe how important pages "
                        "remain reachable from the homepage, and distinguish "
                        "organized support from unrelated articles floating "
                        "independently on the blog."
                    ),
                    (
                        "Brendan Hufford organizes supporting articles around "
                        "a central resource rather than leaving subjects "
                        "independent on the blog. Rank Math SEO shows "
                        "a fishing-boat reviews category ranking for its "
                        "commercial topic. Semrush recommends that the "
                        "site's most important pages be reachable within "
                        "three clicks of the homepage. "
                        "[Brendan Hufford — zSyoobG9KTY @ 00:03:48] "
                        "[Rank Math SEO — 5EkSj0nrCpg @ 00:07:35] "
                        "[Semrush — vnkjR9TE9Ok @ 00:03:35]"
                    ),
                ),
                field(
                    "Internal link revision decision",
                    (
                        "Choose a destination needing attention and describe "
                        "its searcher intent before proposing additional "
                        "links. Record whether removing existing support "
                        "could weaken another competing page, and inspect "
                        "the mobile placement of links included in the revision."
                    ),
                    (
                        "Ahrefs says to check whether a destination matches "
                        "searcher intent before trying to repair performance "
                        "with more PageRank. David Quaid, on Edward Sturm's "
                        "channel, discusses retaining support for vulnerable "
                        "pages. Rank Math SEO separately warns about "
                        "small or closely grouped mobile tap targets. "
                        "[Ahrefs — kpz9-QZRYn8 @ 00:01:29] "
                        "[Edward Sturm — mKy9_UCPEVM @ 00:08:55] "
                        "[Rank Math SEO — 2XsoKvArFjo @ 00:12:54]"
                    ),
                ),
                field(
                    "Dataset to custom field mapping",
                    (
                        "List the property data required by the reusable "
                        "template and match each item to its intended "
                        "custom field. Describe how you will inspect "
                        "the displayed listing for a field-name or "
                        "field-key mismatch before expanding the build."
                    ),
                    (
                        "Hamida demonstrates matching custom fields with "
                        "the correct property data in a WordPress build. "
                        "The later template instruction is to copy the "
                        "correct ACF field name or key so the displayed "
                        "listing draws from its intended property field. "
                        "This example records data matching and template "
                        "reference as connected checks. "
                        "[Hamida - Programmatic SEO Agency — FO1ASxHYnhE @ 00:02:44] "
                        "[Hamida - Programmatic SEO Agency — FO1ASxHYnhE @ 00:04:44]"
                    ),
                ),
                field(
                    "Dataset sentences and metadata",
                    (
                        "Describe the keyword pattern and dataset behind "
                        "the proposed pages. Record which sentences or "
                        "metadata would be assembled through spreadsheet "
                        "formulas, while preserving a separate inspection "
                        "of input quality and internal-linking opportunities "
                        "that automation could overlook."
                    ),
                    (
                        "Matt Diggity demonstrates using ChatGPT for "
                        "spreadsheet formulas that assemble dataset-based "
                        "sentences and metadata. The account also calls "
                        "for inspecting input data and nuanced internal-linking "
                        "opportunities. The client case reports 502 articles "
                        "generated without AI, keeping that production "
                        "description separate from the formula-assistance "
                        "demonstration. "
                        "[Matt Diggity — 4DgWUgtZGqQ @ 00:06:57] "
                        "[Matt Diggity — 4DgWUgtZGqQ @ 00:04:06] "
                        "[Matt Diggity — 4DgWUgtZGqQ @ 00:00:14]"
                    ),
                ),
                field(
                    "Page-specific utility",
                    (
                        "Specify the information that makes each generated "
                        "page useful for its particular subject. Identify "
                        "the question, concern, or pain point being "
                        "answered, and distinguish that material from "
                        "a template whose only meaningful changes are keywords."
                    ),
                    (
                        "Contentbase's Make example includes the app "
                        "name, integration description, clear calls to "
                        "action, available modules, and popular workflows. "
                        "B2BSEOio contrasts useful specificity with pages "
                        "that reuse a template and change a few "
                        "keywords. The paired example identifies page "
                        "components and the concern about repetitive "
                        "generated material. "
                        "[Contentbase — 51GhDWoaU_A @ 00:01:12] "
                        "[B2BSEOio — uI61LP8Ue30 @ 00:04:48]"
                    ),
                ),
                field(
                    "Draft and local review",
                    (
                        "Describe what will be reviewed after an article "
                        "and image reach WordPress as a draft. For "
                        "local pages, identify sections that need more "
                        "precise neighborhood targeting before the "
                        "prepared material becomes part of the published collection."
                    ),
                    (
                        "The digitalemania sends a prepared article "
                        "and image to WordPress as a draft so "
                        "the content can be reviewed before publication. "
                        "Leonidas inspects generated local content and "
                        "explicitly identifies a section needing tighter "
                        "neighborhood targeting. These demonstrations retain "
                        "review work after the initial article or "
                        "landing-page generation. "
                        "[the digitalemania — ufTFZFvsEIM @ 00:01:42] "
                        "[Leonidas @ PPCBasic — 78JTZZ9dRQ8 @ 00:02:42]"
                    ),
                ),
                field(
                    "Small test and maintenance record",
                    (
                        "Describe the smaller implementation you would "
                        "inspect before expanding the page collection. "
                        "Include monitoring, maintenance, updates, QA, "
                        "and developer work, then state which indexing "
                        "observations would be retained when evaluating "
                        "the first published set of pages."
                    ),
                    (
                        "Lorraine Pawell recommends building small, "
                        "testing, and improving before pursuing a much "
                        "larger AI-generated collection, while including "
                        "maintenance and developer time. B2BSEOio's "
                        "healthcare account reports over 1,700 pages "
                        "outside the index and only 400 indexed. "
                        "These accounts distinguish page production "
                        "from the continuing work of sustaining the collection. "
                        "[Lorraine Pawell - SEO AEO & Content Strategy — HYZv8hDMBvw @ 00:13:41] "
                        "[Lorraine Pawell - SEO AEO & Content Strategy — HYZv8hDMBvw @ 00:11:11] "
                        "[B2BSEOio — uI61LP8Ue30 @ 00:01:19]"
                    ),
                ),
            ],
            (
                "Finish the contextual boundaries, field mapping, draft review, "
                "and smaller implementation record before describing expansion. "
                "[Koray Tuğberk GÜBÜR — bWjlnI4gXxo @ 00:01:06] "
                "[Lorraine Pawell - SEO AEO & Content Strategy — HYZv8hDMBvw @ 00:13:41]"
            ),
        ),
        worksheet(
            3,
            "Backlink Portfolios, Digital PR, and Inherited Domains",
            (
                "Keep portfolio acquisition, journalist outreach, expired-domain "
                "rebuilds, and third-party publishing as distinct workflows with "
                "their own source evidence and reported limitations."
            ),
            "Q5: Backlinks, PBN-Style Portfolios & Digital PR; "
            "Q6: Parasite SEO & Expired-Domain Strategies",
            [
                "Record domain metrics alongside historical identity and "
                "backlink evidence rather than using a headline score alone.",
                "Build the journalist story from a real finding, its method, "
                "available data, and an attributable source.",
                "Separate personalized expertise pitches from AI-assisted "
                "site discovery or grammar review.",
                "Map valuable historical URLs before choosing rebuilds, "
                "replacement destinations, or redirects.",
                "Keep host availability and source-specific tracking attached "
                "to any parasite publishing or redirect experiment.",
            ],
            [
                field(
                    "Portfolio acquisition evidence",
                    (
                        "Record the domain evidence you would compare "
                        "across tools before purchasing a portfolio asset. "
                        "Include the speaker's stated rating range as "
                        "one part of the process, and document the "
                        "separate instruction concerning links among portfolio sites."
                    ),
                    (
                        "Grumpy SEO Guy compares domain evidence "
                        "across tools before buying portfolio assets "
                        "and recommends an Ahrefs Domain Rating "
                        "range of 10 to 40 for considered purchases. "
                        "The same account says not to link the "
                        "portfolio sites together in the described "
                        "way; the rating range is not presented "
                        "as the whole acquisition process. "
                        "[Grumpy SEO Guy — ez24lr3G_Mc @ 00:23:17] "
                        "[Grumpy SEO Guy — ez24lr3G_Mc @ 00:35:45] "
                        "[Grumpy SEO Guy — ez24lr3G_Mc @ 00:05:19]"
                    ),
                ),
                field(
                    "Archived identity inspection",
                    (
                        "Describe the domain's current presentation and "
                        "the earlier identity visible in archived history. "
                        "Record any mismatch that affects your purchase "
                        "decision, keeping attractive current metrics "
                        "separate from the historical subject and use "
                        "of the same domain."
                    ),
                    (
                        "Vasco's SEO Tips warns that a rebranded "
                        "domain with attractive current metrics may "
                        "conceal an earlier casino or adult site. "
                        "The channel's instruction is to inspect "
                        "archived history before accepting that asset. "
                        "This example records the current presentation "
                        "and the earlier identity as separate evidence "
                        "within the domain review. "
                        "[Vasco's SEO Tips — voMel_srl_w @ 00:08:41]"
                    ),
                ),
                field(
                    "Trend finding and journalist list",
                    (
                        "Record a real search-interest finding and "
                        "the recent coverage that makes particular "
                        "journalists relevant to it. Keep the finding's "
                        "meaning distinct from a link-conversion claim, "
                        "and explain why a broad journalist category "
                        "alone would not determine recipients."
                    ),
                    (
                        "Fery Kaszoni uses a 1600% increase in "
                        "online electric-car searches in the CarGuide "
                        "campaign email. The figure describes search "
                        "interest, not a backlink conversion rate. "
                        "The outreach advice is to build a "
                        "recent-coverage list rather than assuming "
                        "every journalist in a broad category wants "
                        "the same story. "
                        "[Fery Kaszoni — BpLuK4tA5zw @ 00:01:33] "
                        "[Fery Kaszoni — BpLuK4tA5zw @ 00:03:10]"
                    ),
                ),
                field(
                    "Story evidence and expected links",
                    (
                        "Draft the finding, method line, full-data "
                        "access, and quotable source for a proposed "
                        "story. Record how the speaker distinguishes "
                        "ordinary link expectations from exceptional "
                        "campaign counts, and identify the evidence "
                        "supporting every number in the pitch."
                    ),
                    (
                        "Iron Goo recommends a headline-like finding, "
                        "a method line, full-data access, and a "
                        "quotable source instead of brand adjectives. "
                        "The speaker says to expect a handful "
                        "of good links rather than 50 and "
                        "warns against invented surveys, numbers, "
                        "or experts because journalists can expose "
                        "the fabrication and publish a correction. "
                        "[Iron Goo — Z5OwRBCX5ww @ 00:06:32] "
                        "[Iron Goo — Z5OwRBCX5ww @ 00:12:13] "
                        "[Iron Goo — Z5OwRBCX5ww @ 00:10:26]"
                    ),
                ),
                field(
                    "Personalized expert response",
                    (
                        "Identify the expertise that makes a request "
                        "relevant and describe how the response would "
                        "be personalized. Separate assistance with "
                        "grammar from writing the pitch, and record "
                        "whether the publication's subject matches "
                        "the proposed source's actual knowledge."
                    ),
                    (
                        "Visibility on Purpose favors Qwoted for "
                        "specific expertise and niche publications, "
                        "and instructs viewers to personalize HARO "
                        "and Qwoted answers rather than submit "
                        "AI-written pitches. Julian Goldie separately "
                        "says to pitch requests relevant to the "
                        "source's subject matter and expertise. "
                        "The example preserves that distinction "
                        "between relevance, personalization, and grammar review. "
                        "[Visibility on Purpose — B1uNyKgJlXc @ 00:11:18] "
                        "[Visibility on Purpose — B1uNyKgJlXc @ 00:12:34] "
                        "[Julian Goldie SEO — LY7IFzytdLo @ 00:03:36]"
                    ),
                ),
                field(
                    "Expired-domain rejection record",
                    (
                        "Inspect the expired domain's history, "
                        "referring pages, traffic, relevance, and "
                        "index status. Record the evidence that "
                        "would make you reject an otherwise "
                        "attractive candidate, rather than allowing "
                        "age or a headline metric to settle the choice."
                    ),
                    (
                        "Frey Chu notices that many referring "
                        "pages receive zero traffic and ultimately "
                        "rejects a superficially attractive domain "
                        "after examining links and traffic history. "
                        "MostDomain says age alone does not "
                        "mean power, emphasizing relevance and "
                        "link quality instead. The example records "
                        "specific rejection evidence alongside that "
                        "separate selection principle. "
                        "[Frey Chu — mHkLfhpVYqc @ 00:06:06] "
                        "[Frey Chu — mHkLfhpVYqc @ 00:10:21] "
                        "[MostDomain — hMnUuibx6ZU @ 00:02:08]"
                    ),
                ),
                field(
                    "Historical URL rebuild map",
                    (
                        "List the strongest historical URLs and "
                        "describe which would be rebuilt or "
                        "connected to replacement pages. Record "
                        "the original and replacement locations "
                        "when a permalink changes, distinguishing "
                        "targeted preservation from redirecting most "
                        "linked pages to the homepage."
                    ),
                    (
                        "SirLinksalot says recreating old URLs "
                        "seems stronger than redirecting everything "
                        "or most pages to the homepage. "
                        "When a permalink changes, the speaker "
                        "recommends redirecting the original URL "
                        "into its replacement so old backlinks "
                        "are repurposed. This example separates "
                        "historical-page rebuilding from a specific "
                        "changed-permalink redirect decision. "
                        "[SirLinksalot — nSLIbiyP5vc @ 00:04:11] "
                        "[SirLinksalot — nSLIbiyP5vc @ 00:02:42]"
                    ),
                ),
                field(
                    "Historical crawl and content choice",
                    (
                        "Describe how historical crawl locations "
                        "would inform the rebuild and relevant "
                        "links to new content. Separately record "
                        "whether the content would be fresh "
                        "or restored from archives, retaining "
                        "the speaker's stated complaint scenario "
                        "in that content decision."
                    ),
                    (
                        "Koray Tuğberk GÜBÜR uses log-file "
                        "analysis to find heavily crawled "
                        "historical locations, revive them, and "
                        "link through relevance to new content. "
                        "SirLinksalot prefers fresh content for "
                        "a new affiliate website and mentions "
                        "copyright letters and possible takedowns "
                        "in the archive-content discussion. These "
                        "are separate crawl-path and content-choice records. "
                        "[Koray Tuğberk GÜBÜR — l_Eiy1S5MeA @ 00:11:13] "
                        "[SirLinksalot — lfCYBd5qKMk @ 00:02:17] "
                        "[SirLinksalot — lfCYBd5qKMk @ 00:00:58]"
                    ),
                ),
                field(
                    "Parasite host and final URL",
                    (
                        "Record whether the proposed publishing "
                        "host still ranks and whether its "
                        "pages remain available. Inspect the "
                        "final indexable address, including sharing "
                        "URL behavior, and retain the host-action "
                        "outcomes described in the testimony "
                        "when evaluating a paid placement."
                    ),
                    (
                        "Charles Floate's discussion on Edward "
                        "Sturm's channel says accounts can "
                        "be banned, pages deleted, and paid "
                        "placements lost after host actions. "
                        "The discussion also says to verify "
                        "the final indexable URL instead of "
                        "submitting a sharing address without "
                        "examining canonical or redirect behavior. "
                        "Both checks concern the actual published destination. "
                        "[Edward Sturm — clcy9RbjrXQ @ 00:11:19] "
                        "[Edward Sturm — clcy9RbjrXQ @ 00:28:36]"
                    ),
                ),
                field(
                    "Redirect experiment attribution",
                    (
                        "Record the redirected asset, destination "
                        "article, displayed traffic movement, and "
                        "observation period. Describe how each "
                        "traffic source and individual article "
                        "would remain distinguishable before assigning "
                        "revenue or performance to the redirect "
                        "rather than another simultaneous experiment."
                    ),
                    (
                        "SEO Jesus reports a $2,000 expired "
                        "domain redirected to a LinkedIn "
                        "article and displays traffic moving "
                        "from 3,100 to 7,000. The speaker "
                        "says one week is too early "
                        "for reliable data and identifies "
                        "missing source-specific and article-specific "
                        "tracking links as a problem when "
                        "interpreting mixed experiments. "
                        "[SEO Jesus — AGcswUV4IEA @ 00:00:00] "
                        "[SEO Jesus — AGcswUV4IEA @ 00:06:50] "
                        "[SEO Jesus — AGcswUV4IEA @ 00:06:23] "
                        "[SEO Jesus — AGcswUV4IEA @ 00:09:01]"
                    ),
                ),
            ],
            (
                "Retain historical-domain checks, real story evidence, final-URL "
                "inspection, and separate source tracking in the completed record. "
                "[MostDomain — XdcIcYkuhCc @ 00:07:04] "
                "[Iron Goo — Z5OwRBCX5ww @ 00:10:26] "
                "[SEO Jesus — AGcswUV4IEA @ 00:09:01]"
            ),
        ),
        worksheet(
            4,
            "User-Signal Experiments and Crawl Diagnostics",
            (
                "Record the setup and outcomes described in CTR testimony, "
                "then distinguish engagement observations from crawl requests, "
                "internal discovery, indexing, and actual customer arrivals."
            ),
            "Q7: CTR Manipulation, IP Clicks, Mobile/Residential Proxies & "
            "User-Signal Testing; Q8: Technical Indexing, Crawl Budgets & "
            "Log Diagnostics",
            [
                "Describe existing visibility and engagement before recording "
                "a proposed user-signal experiment.",
                "Keep calculation windows, unusual page averages, device "
                "distribution, and geogrid radius attached to campaign settings.",
                "Record what happens after activity stops and distinguish "
                "direction requests from customers reaching the business.",
                "Use actual request evidence and trends when investigating "
                "crawl allocation rather than relying on a single day.",
                "Inspect internal routes, rendering resources, and crawler "
                "access before assigning a crawl or indexing diagnosis.",
            ],
            [
                field(
                    "Profile readiness and discovery",
                    (
                        "Record the profile's existing reviews, "
                        "rankings, visibility, and engagement before "
                        "considering the demonstrated campaign. Compare "
                        "desktop discovery with the proposed "
                        "mobile interactions, and explain how "
                        "the readiness account applies to "
                        "the listing being examined."
                    ),
                    (
                        "Osborne Digital Marketing says a "
                        "brand-new business without reviews or "
                        "ranking has nothing useful to "
                        "click in the readiness account. "
                        "The channel also advises checking "
                        "whether discovery is mostly desktop "
                        "before choosing a mobile-interaction "
                        "campaign. This example keeps existing "
                        "engagement and existing device discovery "
                        "visible before campaign selection. "
                        "[Osborne Digital Marketing — YGk2zHgGoss @ 00:02:23] "
                        "[Osborne Digital Marketing — 8-9kfC7btJM @ 00:03:16]"
                    ),
                ),
                field(
                    "CTR calculation inputs",
                    (
                        "Record the Search Console period "
                        "and pages used for the better-page "
                        "CTR average. Identify unusual pages "
                        "that would distort the calculation, "
                        "and describe how impressions remain "
                        "part of the record when interpreting "
                        "an encouraging early ranking movement."
                    ),
                    (
                        "Chris Palmer uses a 28-day "
                        "Search Console window for the "
                        "current calculation and excludes a "
                        "one-impression, one-click page from "
                        "the better-page average. Palmer also "
                        "names going too big too fast "
                        "and neglecting impressions among "
                        "their own mistakes. The example "
                        "retains both the calculation inputs "
                        "and that retrospective warning. "
                        "[Chris Palmer SEO — mg7C81Ti3DY @ 00:12:30] "
                        "[Chris Palmer SEO — mg7C81Ti3DY @ 00:13:40] "
                        "[Chris Palmer SEO — mg7C81Ti3DY @ 00:47:52]"
                    ),
                ),
                field(
                    "Demonstrated campaign settings",
                    (
                        "Record the demonstrated call and "
                        "CTR allocation, keyword distribution, "
                        "and device example without treating "
                        "them as universal settings. Describe "
                        "the existing website or profile "
                        "data that would inform the actual "
                        "split, and retain the geogrid radius."
                    ),
                    (
                        "William Jones demonstrates a starting "
                        "allocation of 50 calls and "
                        "50 CTR, subsequently distributed "
                        "across keywords. Yash Singh enters "
                        "a 35/55/10 device distribution "
                        "as an example and says "
                        "actual choices should use existing "
                        "data. Jones also warns against "
                        "expanding a small green geogrid "
                        "as though visibility were unchanged. "
                        "[William Jones — qEmm1oiXm5U @ 00:04:08] "
                        "[Yash Singh — YwzyoEqNVN4 @ 00:02:33] "
                        "[William Jones — qEmm1oiXm5U @ 00:01:48]"
                    ),
                ),
                field(
                    "Post-campaign ranking record",
                    (
                        "Describe the ranking observations during "
                        "the activity and after it "
                        "stops. Keep short-term support "
                        "separate from continuing reviews, "
                        "citations, and content, and record "
                        "the speaker's experience of ongoing "
                        "difficulty or cost rather than "
                        "assuming persistence."
                    ),
                    (
                        "Sterling Sky reports that CTR "
                        "gains did not last and "
                        "rankings moved back toward their "
                        "previous level after activity stopped. "
                        "Isaac Ranks calls the clicks "
                        "short-term support while building "
                        "reviews, citations, and content. "
                        "Semantic Mastery describes increasing "
                        "difficulty and expense with Google "
                        "profiles in the Local Fury account. "
                        "[Sterling Sky Inc — krFtrxJsFok @ 00:01:57] "
                        "[Isaac Ranks — Rank & Rent — vBp6IcY8zg0 @ 00:05:36] "
                        "[Semantic Mastery — VTorygEcF7E @ 00:01:50]"
                    ),
                ),
                field(
                    "Engagement versus customer arrival",
                    (
                        "Separate the recorded engagement "
                        "action from evidence of a "
                        "customer reaching the business. "
                        "Describe which outcome the campaign "
                        "report actually measures, preserving "
                        "the distinction between direction "
                        "requests, ranking changes, and the "
                        "business activity being sought."
                    ),
                    (
                        "Map Labs identifies the gap "
                        "between manufactured direction requests "
                        "and customers actually reaching "
                        "the business as the central "
                        "problem in that engagement account. "
                        "William Jones separately emphasizes "
                        "testing in the CTR setup "
                        "discussion. This example records "
                        "the measured action and the "
                        "customer-arrival question without treating "
                        "them as the same outcome. "
                        "[Map Labs — slTweyz4OSs @ 00:00:43] "
                        "[William Jones — qEmm1oiXm5U @ 00:03:46]"
                    ),
                ),
                field(
                    "Crawl capacity and demand",
                    (
                        "Describe the crawl question in "
                        "terms of what Google can "
                        "crawl and wants to crawl. "
                        "Record the observed trend across "
                        "weeks and months, and explain "
                        "why a single low-crawl day "
                        "does not settle this investigation."
                    ),
                    (
                        "Google Search Central defines crawl "
                        "budget through crawl rate and "
                        "crawl demand: the URLs Google "
                        "can and wants to crawl. "
                        "Andrew Halliday's discussion on "
                        "James Dooley emphasizes stability "
                        "and trends across weeks and "
                        "months rather than treating one "
                        "low-crawl day as the conclusion "
                        "of the investigation. "
                        "[Google Search Central — x_GoMrl6_u0 @ 00:02:35] "
                        "[James Dooley — cv7lfh1AjZc @ 00:02:56]"
                    ),
                ),
                field(
                    "Log activity by section",
                    (
                        "Identify the site section and "
                        "time period being examined in "
                        "the request records. Compare "
                        "frequently visited sections with "
                        "priority service pages, and "
                        "describe the internal routes "
                        "you would inspect between them "
                        "before changing the structure."
                    ),
                    (
                        "TM Blast's pivot table isolates "
                        "266 unique blog crawl events "
                        "over 30 days while examining "
                        "whether older content draws "
                        "activity away from priority "
                        "service pages. FatRank recommends "
                        "using frequently visited sections "
                        "to examine links toward sections "
                        "the operator wants crawled. "
                        "The example connects section-level "
                        "requests with internal-route inspection. "
                        "[TM Blast — 1v7Wiw-ptLU @ 00:02:52] "
                        "[FatRank — 9YOo5zDOsP8 @ 00:06:07]"
                    ),
                ),
                field(
                    "Request identity and query scope",
                    (
                        "Describe how the request identity "
                        "will be checked beyond its "
                        "user-agent label. Record the "
                        "initial query limit and what "
                        "you would inspect before "
                        "expanding results, keeping request "
                        "validation separate from the "
                        "cost of processing the investigation."
                    ),
                    (
                        "The brightonSEO presenter says "
                        "not to validate a bot "
                        "from its user agent alone "
                        "because that label is easy "
                        "to imitate, and instead "
                        "uses IP information. Semrush "
                        "Live recommends beginning a "
                        "new query with a limit "
                        "of 10, iterating before "
                        "expanding its result set "
                        "and processing cost. "
                        "[brightonSEO — Q9Nkmc8Cx6I @ 00:10:56] "
                        "[Semrush Live — eelEuYoflG0 @ 00:09:17]"
                    ),
                ),
                field(
                    "Redesign discovery and resources",
                    (
                        "Inspect whether a redesign "
                        "preserved internal links to "
                        "important service and money "
                        "pages. Separately describe the "
                        "JavaScript and CSS resources "
                        "needed for rendering, rather "
                        "than interpreting a high "
                        "resource-request percentage as a "
                        "reason to block them."
                    ),
                    (
                        "Abdul Latif warns that themes "
                        "and menus can silently remove "
                        "routes to important service "
                        "and money pages after a "
                        "redesign. Pearl Lemon says "
                        "not to block JavaScript "
                        "or CSS merely because "
                        "resource percentages look high; "
                        "the implementation may need "
                        "those files to render "
                        "correctly. The example keeps "
                        "discovery and rendering separate. "
                        "[Abdul Latif — pjmp4gM12iQ @ 00:04:22] "
                        "[Pearl Lemon SEO — aRuxCdZQ1Yo @ 00:07:12]"
                    ),
                ),
                field(
                    "Crawler access and temporary repairs",
                    (
                        "Record any crawler-access restriction "
                        "and whether rules intended "
                        "for AI crawlers also "
                        "affect Google. Describe any "
                        "dynamic-rendering workaround separately "
                        "from a root repair, "
                        "including the maintenance difficulty "
                        "reported in the hospital "
                        "crawl investigation."
                    ),
                    (
                        "Misha Manko identifies strong "
                        "CDN rules aimed at AI "
                        "crawlers that also block "
                        "Google as a possible "
                        "technical exception. In the "
                        "hospital investigation, brightonSEO "
                        "reports 1.3% sitemap crawl "
                        "coverage and warns that "
                        "the dynamic-rendering workaround "
                        "is difficult to maintain "
                        "at scale rather than "
                        "a finished root repair. "
                        "[Misha Manko — vcLkBQxf9Hs @ 00:05:58] "
                        "[brightonSEO — Q9Nkmc8Cx6I @ 00:11:32] "
                        "[brightonSEO — Q9Nkmc8Cx6I @ 00:18:23]"
                    ),
                ),
            ],
            (
                "Complete the baseline, post-stop observations, customer-arrival "
                "distinction, and crawler-access inspection. "
                "[Sterling Sky Inc — krFtrxJsFok @ 00:01:57] "
                "[Map Labs — slTweyz4OSs @ 00:00:43] "
                "[Misha Manko — vcLkBQxf9Hs @ 00:05:58]"
            ),
        ),
        worksheet(
            5,
            "Traffic-Drop Diagnosis and AI Answer Visibility",
            (
                "Separate observed search movement from explanations, then "
                "document repeatable AI-answer comparisons, citation inspection, "
                "page improvements, and identity accuracy."
            ),
            "Q9: Core Updates, Traffic-Drop Diagnosis & Recovery; "
            "Q10: AI Overviews, LLM Search & GEO Visibility",
            [
                "Record the rollout comparison period before describing "
                "a recovery action or interpreting a small movement.",
                "Find the largest losing pages and queries, then check "
                "their relationship to what the business sells.",
                "Inspect crawler access and page evidence without "
                "assuming that coincident actions caused ranking changes.",
                "Choose commercially relevant AI-search questions and "
                "repeat comparisons within the same engine and market.",
                "Inspect cited sources and the assistant's actual "
                "description of the business, not only its inclusion count.",
            ],
            [
                field(
                    "Update comparison window",
                    (
                        "Record the update comparison "
                        "period and the size "
                        "of the observed position "
                        "change. Describe how you "
                        "would distinguish a small "
                        "slip from a larger "
                        "fall before rewriting content "
                        "during an ongoing rollout."
                    ),
                    (
                        "Kate Smoothy says to wait "
                        "at least a week before "
                        "examining the data, then "
                        "compare it with the "
                        "week before rollout. Julian "
                        "Goldie says not to "
                        "rewrite the whole site "
                        "during rollout and to "
                        "distinguish a small position "
                        "slip from a larger "
                        "fall before choosing deeper work. "
                        "[Kate Smoothy | SEO Specialist — zS5xebRUE5Y @ 00:02:29] "
                        "[Julian Goldie SEO — HWSpTVX7qMI @ 00:01:29]"
                    ),
                ),
                field(
                    "Loss concentration and impressions",
                    (
                        "Identify the pages and "
                        "keywords with the largest "
                        "losses before assessing the "
                        "whole library. Record impressions "
                        "alongside clicks so that "
                        "improved rankings without additional "
                        "clicks remain visible in "
                        "the comparison rather than "
                        "being overlooked."
                    ),
                    (
                        "Julian Goldie recommends finding "
                        "the pages and keywords "
                        "with the largest losses "
                        "before grading and improving "
                        "the whole content library. "
                        "BSM recommends beginning with "
                        "impressions when improved rankings "
                        "have not yet produced "
                        "more clicks. The example "
                        "separates loss concentration from "
                        "the choice of observation "
                        "used to notice improvement. "
                        "[Julian Goldie SEO — s_GIhK4WE18 @ 00:07:03] "
                        "[BSM - A Denver SEO Company — 2jejTy2fWTg @ 00:02:36]"
                    ),
                ),
                field(
                    "Business relevance and page evidence",
                    (
                        "Describe whether the reviewed "
                        "page still serves what "
                        "the business sells. Record "
                        "the jobs, photos, numbers, "
                        "mistakes, and factual checks "
                        "that could support its "
                        "content, keeping genuine experience "
                        "separate from an unchanged "
                        "AI draft."
                    ),
                    (
                        "Kasra Dash reports that "
                        "86 of 172 partially "
                        "hit sites had pages "
                        "drifting away from what "
                        "the business sells. True "
                        "SEO says AI can "
                        "research and draft, followed "
                        "by the business's jobs, "
                        "photos, numbers, mistakes, "
                        "fact checking, and a "
                        "real name. The example "
                        "records relevance and reviewed "
                        "experience together. "
                        "[Kasra Dash — I26NAT6T6Gs @ 00:00:19] "
                        "[True SEO — y6yAJ9Ocl3U @ 00:03:00]"
                    ),
                ),
                field(
                    "Technical priority and deletion decision",
                    (
                        "Record any critical crawler-access "
                        "block before listing ordinary "
                        "speed or content work. "
                        "If a penalty is "
                        "suspected, describe the manual-actions "
                        "inspection and why deletion "
                        "would remain a later "
                        "decision in the speaker's "
                        "proposed repair sequence."
                    ),
                    (
                        "Kasra Dash says a "
                        "critical crawler-access block "
                        "should be fixed immediately "
                        "rather than queued behind "
                        "ordinary speed or content "
                        "work. Bill Mcintosh "
                        "treats deletion as a "
                        "last resort and recommends "
                        "inspecting the manual-actions "
                        "report when a penalty "
                        "is suspected. These "
                        "instructions describe different "
                        "parts of the repair sequence. "
                        "[Kasra Dash — yzNo7jJ8WBE @ 00:31:00] "
                        "[Bill Mcintosh — UGKO4HDAk8w @ 00:09:25]"
                    ),
                ),
                field(
                    "Observed movement and explanation",
                    (
                        "Write the observed change "
                        "separately from your proposed "
                        "explanation for it. Record "
                        "what action occurred nearby "
                        "in time, and preserve "
                        "the distinction between an "
                        "observed recovery and knowing "
                        "which action caused that "
                        "movement."
                    ),
                    (
                        "Authority Hacker warns that "
                        "an action and a "
                        "ranking movement can occur "
                        "together without the apparent "
                        "causal connection. Surfside "
                        "PPC separately reports "
                        "working to recover affiliate "
                        "earnings that never recovered. "
                        "These accounts keep "
                        "interpretation separate from "
                        "outcome and preserve an "
                        "unsuccessful recovery account "
                        "rather than converting repair "
                        "work into an assumed result. "
                        "[Authority Hacker Podcast — ePxZx_vQNFo @ 00:42:46] "
                        "[Surfside PPC — 0_SAQbGnl3Y @ 00:00:55]"
                    ),
                ),
                field(
                    "Commercial AI question set",
                    (
                        "Choose the commercial topics "
                        "that matter to the "
                        "business and record the "
                        "questions used to examine "
                        "them. Define inclusion through "
                        "brand naming and page "
                        "citation, rather than allowing "
                        "unrelated generated prompts to "
                        "determine success."
                    ),
                    (
                        "Grow and Convert says "
                        "to choose commercial "
                        "topics yourself instead "
                        "of allowing unrelated "
                        "generated prompts to "
                        "define success. Alex "
                        "Moreau describes the "
                        "objective as getting "
                        "the brand named "
                        "and its pages "
                        "cited in AI "
                        "answers. The example "
                        "connects topic selection "
                        "with a specifically "
                        "described answer-inclusion "
                        "outcome for the business. "
                        "[The Grow and Convert Marketing Show — hEPMrse9c_g @ 00:41:41] "
                        "[Alex Moreau | AI for Ads & SEO-GEO — Oq7qV4_5W-A @ 00:00:16]"
                    ),
                ),
                field(
                    "Repeated answer comparison",
                    (
                        "Record the questions, engine, "
                        "market, and repeated "
                        "captures used for the "
                        "comparison. Describe the "
                        "observed inclusion movement "
                        "without combining different "
                        "engines or presenting "
                        "a small sample "
                        "as a stable trend "
                        "on its own."
                    ),
                    (
                        "The Answer Lab illustrates "
                        "four inclusions in twelve "
                        "observations as 33%, "
                        "with an approximate "
                        "14% to 60% "
                        "margin-of-error range. "
                        "The channel says "
                        "to compare the "
                        "same questions, engine, "
                        "and market, noting "
                        "that a ChatGPT "
                        "number beside a "
                        "Gemini number is "
                        "not a trend. "
                        "The example retains "
                        "that small-sample context. "
                        "[The Answer Lab | GEO & AEO — yeLHXIInymI @ 00:07:04] "
                        "[The Answer Lab | GEO & AEO — yeLHXIInymI @ 00:07:25]"
                    ),
                ),
                field(
                    "Opening answer and cited sources",
                    (
                        "Inspect the page's opening "
                        "answer and the sources "
                        "repeatedly cited for the "
                        "chosen questions. Record "
                        "the business's own "
                        "supporting numbers and "
                        "the relevant blogs "
                        "already appearing, keeping "
                        "page improvement separate "
                        "from citation outreach."
                    ),
                    (
                        "Alex Moreau recommends "
                        "adding the business's "
                        "own supporting numbers "
                        "when a page "
                        "lacks a useful "
                        "opening answer. "
                        "CrowdReply inspects "
                        "citations from recurring "
                        "prompt captures and "
                        "contacts blogs already "
                        "appearing in those "
                        "answers. The example "
                        "keeps owned-page "
                        "improvement and outreach "
                        "to demonstrated sources "
                        "as related but "
                        "distinct pieces of work. "
                        "[Alex Moreau | AI for Ads & SEO-GEO — Oq7qV4_5W-A @ 00:02:44] "
                        "[CrowdReply | Rank in AI Answers — v2nAe-a8JrQ @ 00:09:44]"
                    ),
                ),
                field(
                    "Search crawler and architecture review",
                    (
                        "Check whether the relevant "
                        "search crawler can "
                        "access the site, "
                        "distinguishing search-bot "
                        "settings from training-bot "
                        "settings. Record orphan "
                        "pages, competing answers, "
                        "and platform limits "
                        "before describing a "
                        "larger change to "
                        "the site structure."
                    ),
                    (
                        "Alex Moreau warns "
                        "against confusing OpenAI's "
                        "training-bot setting "
                        "with its search-bot "
                        "setting when checking "
                        "access. Brandon Aday "
                        "recommends inspecting "
                        "orphan pages, competing "
                        "answers, and current "
                        "platform limits before "
                        "prescribing a structural "
                        "overhaul. This example "
                        "records access and "
                        "architecture as separate "
                        "inspections preceding a "
                        "larger proposed site "
                        "change. "
                        "[Alex Moreau | AI for Ads & SEO-GEO — Oq7qV4_5W-A @ 00:04:24] "
                        "[Brandon Aday — CWvcb0rGN0g @ 00:01:13]"
                    ),
                ),
                field(
                    "Answer accuracy and narrative",
                    (
                        "Record what the "
                        "assistant actually says "
                        "about the business, "
                        "not only whether "
                        "the name appears. "
                        "Identify any borrowed "
                        "history or mixed "
                        "identity, and compare "
                        "inclusion, accuracy, and "
                        "the business narrative "
                        "as distinct observations."
                    ),
                    (
                        "Maria Johnsen reports "
                        "Gemini mixing another "
                        "subject's seventeen-year "
                        "history into Johnsen's "
                        "filmmaking biography. "
                        "Fast Hippo Media "
                        "recommends tracking "
                        "inclusion rate, accuracy, "
                        "and how much "
                        "of the answer "
                        "reflects the intended "
                        "narrative. The example "
                        "therefore records the "
                        "content of an "
                        "answer alongside the "
                        "fact that the "
                        "subject appeared. "
                        "[AI Innovations With Maria Johnsen — 8iciP8By_g4 @ 00:13:35] "
                        "[Fast Hippo Media — JrHxc3BMz6g @ 00:01:47]"
                    ),
                ),
            ],
            (
                "Keep observed changes separate from causal explanations and "
                "repeat AI-answer comparisons within the same questions, engine, "
                "and market. "
                "[Authority Hacker Podcast — ePxZx_vQNFo @ 00:42:46] "
                "[The Answer Lab | GEO & AEO — yeLHXIInymI @ 00:07:25]"
            ),
        ),
        worksheet(
            6,
            "Monetization, Commercial Models, and Acquisition Review",
            (
                "Document ad-income observations, placement choices, directory "
                "and SaaS mechanisms, bounded agency trials, and the independent "
                "research described in website-acquisition testimony."
            ),
            "Q11: Display-Ad Monetization, RPM & Affiliate Alternatives; "
            "Q12: Agency, SaaS, Directory & Website-Investment Models",
            [
                "Keep each reported income figure attached to its speaker, "
                "period, sessions, and stated RPM.",
                "Inspect placement contributions and reading behavior before "
                "recording a change to the ad configuration.",
                "Retain dashboard-history and existing-integration consequences "
                "when comparing a move between providers.",
                "Describe the specific customer problem and payment mechanism "
                "for the agency, SaaS, or directory model being considered.",
                "Record independent acquisition research, operating capital, "
                "and target-language capability separately from broker vetting.",
            ],
            [
                field(
                    "Income report and denominator",
                    (
                        "Record the reported earnings, "
                        "sessions, RPM, and "
                        "period together. Describe "
                        "whether a comparison "
                        "uses sessions or "
                        "page views, keeping "
                        "the speaker's income "
                        "report intact rather "
                        "than treating different "
                        "measurement bases as "
                        "interchangeable evidence."
                    ),
                    (
                        "Meghan's Media reports "
                        "46,000 sessions, "
                        "$2,568 in earnings, "
                        "and a $55.22 "
                        "average RPM for "
                        "February. She Knows "
                        "SEO separately says "
                        "the measure changes "
                        "significantly between "
                        "sessions and page "
                        "views. This example "
                        "preserves the reported "
                        "monthly figures while "
                        "keeping the measurement "
                        "basis visible when "
                        "another account is "
                        "used for comparison. "
                        "[Meghan's Media — XXTUzO1Y_1U @ 00:03:53] "
                        "[She Knows SEO — xRuzXK8HIFo @ 00:06:05]"
                    ),
                ),
                field(
                    "Placement contribution and video",
                    (
                        "List the ad placements "
                        "being considered for "
                        "change and their "
                        "reported dollar contributions. "
                        "Record video separately "
                        "where the account "
                        "shows its share, "
                        "and explain which "
                        "earnings evidence would "
                        "be examined before "
                        "removing a placement."
                    ),
                    (
                        "Meghan's Media recommends "
                        "examining each placement's "
                        "dollar contribution before "
                        "removing an ad "
                        "that may supply "
                        "a substantial share "
                        "of income. Carl "
                        "Broadbent identifies "
                        "video ads as "
                        "8.3% of one "
                        "website's displayed "
                        "ad earnings. The "
                        "example keeps placement "
                        "removal decisions attached "
                        "to the contribution "
                        "shown in the account. "
                        "[Meghan's Media — NRcTFL8qghY @ 00:04:05] "
                        "[Carl Broadbent — feVaD3YiPFE @ 00:08:53]"
                    ),
                ),
                field(
                    "Reading layout and visibility",
                    (
                        "Describe the article's "
                        "paragraph layout, line "
                        "height, and internal "
                        "links. Record any "
                        "page-level visibility "
                        "score needing attention, "
                        "then identify loading, "
                        "departures, or scrolling "
                        "as the specific "
                        "behavior to inspect "
                        "in the demonstrated "
                        "walkthrough."
                    ),
                    (
                        "HeyRahat recommends "
                        "shorter paragraphs "
                        "and adjusted line "
                        "height rather than "
                        "large text blocks. "
                        "She Knows SEO "
                        "flags a visibility "
                        "score below 50% "
                        "for attention to "
                        "loading, departures, "
                        "or scrolling. Vitaliy "
                        "Gershfeld recommends "
                        "internal links throughout "
                        "content. These examples "
                        "record layout, observed "
                        "visibility, and continued "
                        "reading routes separately. "
                        "[HeyRahat — 2oU82BZ6KOU @ 00:02:08] "
                        "[She Knows SEO — xRuzXK8HIFo @ 00:08:48] "
                        "[Vitaliy Gershfeld — Gb-4YRsXxSk @ 00:04:13]"
                    ),
                ),
                field(
                    "Provider transition record",
                    (
                        "Record the historical "
                        "dashboard information "
                        "needed before leaving "
                        "a provider. Describe "
                        "any existing integration "
                        "status that the "
                        "speaker says could "
                        "be lost through "
                        "interruption, keeping "
                        "those transition consequences "
                        "separate from expected "
                        "earnings after a switch."
                    ),
                    (
                        "She Knows SEO "
                        "had to request "
                        "a spreadsheet after "
                        "losing historical dashboard "
                        "access on leaving "
                        "Mediavine. David "
                        "Kowalski says removing "
                        "an existing Ezoic "
                        "integration for more "
                        "than seven days "
                        "loses grandfathered "
                        "status under the "
                        "requirements described. "
                        "The example records "
                        "both reported transition "
                        "consequences without substituting "
                        "an earnings comparison. "
                        "[She Knows SEO — dL9VBY-Gj0Y @ 00:15:10] "
                        "[David Kowalski — OzPRqoG7brI @ 00:03:36]"
                    ),
                ),
                field(
                    "Alternative format and traffic test",
                    (
                        "Describe the actual "
                        "formats used by "
                        "an alternative network "
                        "and the behavior "
                        "they create on "
                        "the page. Separately "
                        "record the testing "
                        "budget and early-profitability "
                        "warning attached to "
                        "the speaker's paid-traffic "
                        "alternative to organic "
                        "search."
                    ),
                    (
                        "CanEye's all-format "
                        "Monetag test included "
                        "interrupted scrolling, "
                        "new tabs, and "
                        "large overlays that "
                        "the speaker did "
                        "not want on "
                        "the site. Revenue "
                        "Tactics separately "
                        "includes a testing "
                        "budget in the "
                        "paid-traffic alternative "
                        "and warns early "
                        "campaigns may not "
                        "be immediately profitable. "
                        "These are distinct "
                        "format and traffic "
                        "experiences. "
                        "[CanEye — kZ7NX7BR1X8 @ 00:07:27] "
                        "[Revenue Tactics — 7pZQrsYVmt4 @ 00:10:06]"
                    ),
                ),
                field(
                    "Bounded agency portfolio trial",
                    (
                        "Describe the prospect "
                        "and the bounded "
                        "trial used to "
                        "develop experience "
                        "and a testimonial. "
                        "Keep the speaker's "
                        "limit on the "
                        "number of prospects "
                        "and trial duration "
                        "visible rather than "
                        "turning the example "
                        "into an unrestricted "
                        "service offer."
                    ),
                    (
                        "Gautam Prachi proposes "
                        "offering a free "
                        "SEO trial to "
                        "only one prospect "
                        "for 14 days "
                        "to develop experience "
                        "and a testimonial. "
                        "The example records "
                        "both boundaries with "
                        "the portfolio-building "
                        "purpose. It does "
                        "not replace the "
                        "single prospect or "
                        "the stated duration "
                        "with a broader "
                        "offer to multiple "
                        "prospective clients. "
                        "[Gautam Prachi — ctFRKtUiETo @ 00:05:09]"
                    ),
                ),
                field(
                    "Reusable interface and product fit",
                    (
                        "Describe the reusable "
                        "interface and the "
                        "page-specific data "
                        "supplied through JSON "
                        "or markdown. Explain "
                        "how the resulting "
                        "page connects a "
                        "search query to "
                        "a product that "
                        "actually solves the "
                        "problem, rather than "
                        "only presenting a "
                        "template."
                    ),
                    (
                        "Samik Choudhury "
                        "describes creating "
                        "one reusable template "
                        "so the interface "
                        "does not need "
                        "rewriting for each "
                        "blog page, with "
                        "page-specific content "
                        "supplied through JSON "
                        "or markdown. SaaS "
                        "SEO Engine says "
                        "the product must "
                        "actually solve the "
                        "search query's problem. "
                        "The example connects "
                        "implementation reuse with "
                        "the commercial task "
                        "being served. "
                        "[Samik Choudhury — xbFsXyB1UZo @ 00:01:41] "
                        "[SaaS SEO Engine — kBXz_ArlMVk @ 00:03:49]"
                    ),
                ),
                field(
                    "Route pages and local navigation",
                    (
                        "Record the specific "
                        "costs, questions, "
                        "and calls to "
                        "action needed by "
                        "a route page. "
                        "Describe breadcrumbs "
                        "and state-to-city "
                        "connections for local "
                        "service pages, keeping "
                        "the page's useful "
                        "content separate from "
                        "the routes that "
                        "make it discoverable."
                    ),
                    (
                        "Contentbase's moveBuddha "
                        "discussion recommends "
                        "specific costs, FAQs, "
                        "and calls to "
                        "action rather than "
                        "stopping at a "
                        "moving-route name. "
                        "SaaS SEO Engine "
                        "describes breadcrumbs "
                        "and state-to-city "
                        "links for understandable "
                        "local-service relationships. "
                        "The example records "
                        "both page-specific "
                        "information and the "
                        "navigation connecting "
                        "related local destinations "
                        "within the site. "
                        "[Contentbase — 3Fkd3FP40iU @ 00:01:27] "
                        "[SaaS SEO Engine — kBXz_ArlMVk @ 00:06:13]"
                    ),
                ),
                field(
                    "Directory data and paid listing",
                    (
                        "Describe the directory "
                        "niche and inspect "
                        "whether returned "
                        "records actually fit "
                        "it. Record the "
                        "featured-listing mechanism "
                        "separately from data "
                        "collection, making "
                        "the speaker's warning "
                        "about inaccurate or "
                        "irrelevant scraped "
                        "records part of "
                        "the preparation work."
                    ),
                    (
                        "Frey Chu reports "
                        "Sober Nation's "
                        "featured-listing example "
                        "at $129 a "
                        "month. The directory "
                        "discussion also warns "
                        "that scraped results "
                        "contain junk and "
                        "are not automatically "
                        "accurate for the "
                        "intended niche. This "
                        "example separates "
                        "the reported listing "
                        "price from the "
                        "cleaning work needed "
                        "before collected records "
                        "become directory entries. "
                        "[Frey Chu — NoUJBS6-yNQ @ 00:04:44] "
                        "[Frey Chu — NoUJBS6-yNQ @ 00:12:47]"
                    ),
                ),
                field(
                    "Independent acquisition and operations",
                    (
                        "Record independent "
                        "purchase research "
                        "alongside broker "
                        "vetting, including "
                        "the disclosed "
                        "link arrangements. "
                        "Describe the extra "
                        "operating capital "
                        "and target-language "
                        "capability needed "
                        "to run the "
                        "business, keeping "
                        "acquisition checks "
                        "distinct from ongoing "
                        "content production."
                    ),
                    (
                        "Jaryd Krause reports "
                        "a seller withholding "
                        "a PBN from "
                        "the broker's listing. "
                        "Mike Swigunski says "
                        "to retain extra "
                        "capital to run "
                        "an acquired business. "
                        "Empire Flippers "
                        "recommends writers "
                        "and editors who "
                        "naturally speak "
                        "the target language "
                        "and understand "
                        "its culture. "
                        "These accounts "
                        "separate purchase "
                        "research from "
                        "operating resources "
                        "and content capability. "
                        "[Jaryd Krause - Buying Online Businesses — O0q1EG7DNIc @ 00:06:44] "
                        "[Mike Swigunski — w5fG8eKka5Y @ 00:04:47] "
                        "[Empire Flippers — i598iDr-y8E @ 00:05:44]"
                    ),
                ),
            ],
            (
                "Complete the income basis, placement evidence, transition "
                "consequences, and independent acquisition research before "
                "comparing the commercial models. "
                "[She Knows SEO — xRuzXK8HIFo @ 00:06:05] "
                "[Meghan's Media — NRcTFL8qghY @ 00:04:05] "
                "[Jaryd Krause - Buying Online Businesses — O0q1EG7DNIc @ 00:06:44]"
            ),
        ),
    ]

    sections = [
        {
            "title": "Worksheet 1 testimony bridge: intent before selection",
            "paragraphs": [
                (
                    "Real Estate SEO & Web Design "
                    "([xDMs5FogvQ8 @ 00:01:08]) starts with keywords that "
                    "convert. Jacob Shireman ([Iktexen_-cc @ 00:18:56]) "
                    "checks what actually appears in Google, while "
                    "WeStudyFunnels ([PpHWPSjRYPI @ 00:05:39]) inspects "
                    "exact-query targeting rather than accepting a low "
                    "difficulty score as the complete competition assessment."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Local commercial outcome",
                        "Living-in-Lake-St.-Louis article associated with "
                        "a reported $1.3 million waterfront transaction.",
                        "Real Estate SEO & Web Design "
                        "([xDMs5FogvQ8 @ 00:03:19])",
                    ],
                    [
                        "Ranking coverage",
                        "Count topics ranking in the top 20, not simply "
                        "the number of published pages.",
                        "Topical Authority SEO | Floyi "
                        "([0XswjN-Lops @ 00:01:18])",
                    ],
                ],
            },
        },
        {
            "title": "Worksheet 2 testimony bridge: context before scale",
            "paragraphs": [
                (
                    "Koray Tuğberk GÜBÜR ([bWjlnI4gXxo @ 00:01:06]) "
                    "groups attributes when their contexts fit together. "
                    "Hamida - Programmatic SEO Agency "
                    "([FO1ASxHYnhE @ 00:02:44]) matches custom fields "
                    "to the correct data, and Lorraine Pawell - SEO AEO "
                    "& Content Strategy ([HYZv8hDMBvw @ 00:13:41]) "
                    "recommends smaller tests and improvements before "
                    "a much larger generated collection."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Important-page route",
                        "Reach the most important pages within three "
                        "clicks of the homepage.",
                        "Semrush ([vnkjR9TE9Ok @ 00:03:35])",
                    ],
                    [
                        "Publication review",
                        "Prepared articles and images arrive in WordPress "
                        "as drafts for review before publishing.",
                        "the digitalemania ([ufTFZFvsEIM @ 00:01:42])",
                    ],
                ],
            },
        },
        {
            "title": "Worksheet 3 testimony bridge: distinct link workflows",
            "paragraphs": [
                (
                    "Grumpy SEO Guy ([ez24lr3G_Mc @ 00:23:17]) "
                    "compares evidence across tools for portfolio purchases. "
                    "Iron Goo ([Z5OwRBCX5ww @ 00:06:32]) builds "
                    "journalist materials around a finding, method, data, "
                    "and source. SirLinksalot ([nSLIbiyP5vc @ 00:04:11]) "
                    "prioritizes strong historical URLs over sending most "
                    "linked pages directly to the homepage."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Domain history",
                        "Inspect archived identity before accepting a "
                        "rebranded domain with attractive present metrics.",
                        "Vasco's SEO Tips ([voMel_srl_w @ 00:08:41])",
                    ],
                    [
                        "Experiment tracking",
                        "Use separate tracking links for traffic sources "
                        "and preferably individual LinkedIn articles.",
                        "SEO Jesus ([AGcswUV4IEA @ 00:09:01])",
                    ],
                ],
            },
        },
        {
            "title": "Worksheet 4 testimony bridge: signals and requests",
            "paragraphs": [
                (
                    "Chris Palmer SEO ([mg7C81Ti3DY @ 00:12:30]) "
                    "uses a recent 28-day calculation window. Sterling "
                    "Sky Inc ([krFtrxJsFok @ 00:01:57]) observes "
                    "rankings returning toward their prior level after "
                    "activity stops. Google Search Central "
                    "([x_GoMrl6_u0 @ 00:02:35]) separately defines "
                    "crawl budget through what Google can and wants "
                    "to crawl; these records concern different observations."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Customer arrival",
                        "Direction requests do not establish that "
                        "customers actually reached the business.",
                        "Map Labs ([slTweyz4OSs @ 00:00:43])",
                    ],
                    [
                        "Proxy configuration evidence boundary",
                        "The supplied Q7 digest attributes P2P mobile-IP "
                        "promotion to Anthony Hayes but supplies no "
                        "timestamped HTTP-versus-SOCKS5 configuration "
                        "demonstration. The worksheet instead records "
                        "the documented device-distribution example.",
                        "Yash Singh ([YwzyoEqNVN4 @ 00:02:33])",
                    ],
                    [
                        "Request validation",
                        "Use IP information rather than relying only "
                        "on a user-agent label.",
                        "brightonSEO ([Q9Nkmc8Cx6I @ 00:10:56])",
                    ],
                ],
            },
        },
        {
            "title": "Worksheet 5 testimony bridge: observation and interpretation",
            "paragraphs": [
                (
                    "Authority Hacker Podcast ([ePxZx_vQNFo @ 00:42:46]) "
                    "warns against inferring causality from coincident "
                    "actions and ranking movements. The Answer Lab | "
                    "GEO & AEO ([yeLHXIInymI @ 00:07:25]) "
                    "keeps repeated comparisons within the same questions, "
                    "engine, and market. Fast Hippo Media "
                    "([JrHxc3BMz6g @ 00:01:47]) adds accuracy and "
                    "narrative to inclusion-rate tracking."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Loss review",
                        "Find the pages and keywords with the largest "
                        "losses before assessing the complete library.",
                        "Julian Goldie SEO ([s_GIhK4WE18 @ 00:07:03])",
                    ],
                    [
                        "Commercial question selection",
                        "Choose commercially relevant topics rather "
                        "than accepting unrelated generated prompts.",
                        "The Grow and Convert Marketing Show "
                        "([hEPMrse9c_g @ 00:41:41])",
                    ],
                ],
            },
        },
        {
            "title": "Worksheet 6 testimony bridge: reported income and operations",
            "paragraphs": [
                (
                    "Meghan's Media ([NRcTFL8qghY @ 00:04:05]) "
                    "examines placement-level dollar contributions before "
                    "removal. SaaS SEO Engine ([kBXz_ArlMVk @ 00:03:49]) "
                    "requires the product to solve the query's problem. "
                    "Jaryd Krause - Buying Online Businesses "
                    "([O0q1EG7DNIc @ 00:06:44]) describes withheld "
                    "PBN information, preserving the need for independent "
                    "purchase research alongside broker vetting."
                ),
            ],
            "table": {
                "headers": ["Decision record", "Transcript evidence", "Expert Source"],
                "rows": [
                    [
                        "Bounded portfolio trial",
                        "Free SEO trial for only one prospect, lasting "
                        "14 days, to develop experience and a testimonial.",
                        "Gautam Prachi ([ctFRKtUiETo @ 00:05:09])",
                    ],
                    [
                        "Directory preparation",
                        "Scraped records contain junk and need checking "
                        "against the intended niche.",
                        "Frey Chu ([NoUJBS6-yNQ @ 00:12:47])",
                    ],
                ],
            },
        },
    ]

    workbook = {
        "workbook_id": "wb-010-building-an-seo-empire",
        "volume_id": "vol-010-building-an-seo-empire",
        "title": "Building an SEO Empire — Expert Testimony Operator Workbook",
        "subtitle": (
            "Six printable worksheets across Q1-Q12: local rank-and-rent "
            "assets and keyword qualification; semantic architecture and "
            "programmatic publishing; backlink portfolios, digital PR, "
            "parasite publishing and expired domains; CTR observations "
            "and crawl diagnostics; update diagnosis and AI-answer "
            "visibility; display-ad income, agency trials, SaaS, "
            "directories and website-acquisition operations."
        ),
        "worksheets": worksheets,
        "sections": sections,
        "callouts": [
            {
                "title": "INSIDER PRO-TIPS",
                "items": [
                    (
                        "Use original local pictures and add the town, city, "
                        "or neighborhood to descriptions, captions, and "
                        "alt text. "
                        "[Real Estate SEO & Web Design — xDMs5FogvQ8 @ 00:12:31]"
                    ),
                    (
                        "Inspect ranking URLs for dedicated competing pages "
                        "before assigning a phrase to the main service page. "
                        "[Robbie Richards — P5ET0IvFReQ @ 00:03:19]"
                    ),
                    (
                        "Rebuild the strongest historical URLs before "
                        "sending most linked pages directly to the homepage. "
                        "[SirLinksalot — nSLIbiyP5vc @ 00:04:11]"
                    ),
                    (
                        "Inspect recurring AI-answer citations and contact "
                        "the blogs already appearing in those answers. "
                        "[CrowdReply | Rank in AI Answers — v2nAe-a8JrQ @ 00:09:44]"
                    ),
                ],
            },
            {
                "title": "OPERATOR GATE",
                "items": [
                    (
                        "Check whether the generated page addresses a "
                        "particular question, concern, or pain point rather "
                        "than changing a few keywords in a reused template. "
                        "[B2BSEOio — uI61LP8Ue30 @ 00:04:48]"
                    ),
                    (
                        "Do not invent survey results, campaign numbers, "
                        "or experts; retain Iron Goo's warning that "
                        "journalists can expose the fabrication and "
                        "publish a correction. "
                        "[Iron Goo — Z5OwRBCX5ww @ 00:10:26]"
                    ),
                    (
                        "Inspect rankings after the activity stops "
                        "instead of assuming that the earlier gain "
                        "continues. "
                        "[Sterling Sky Inc — krFtrxJsFok @ 00:01:57]"
                    ),
                    (
                        "Perform independent acquisition research alongside "
                        "broker vetting, retaining the reported incident "
                        "of withheld PBN information. "
                        "[Jaryd Krause - Buying Online Businesses — O0q1EG7DNIc @ 00:06:44]"
                    ),
                ],
            },
        ],
        "sop_steps": [
            {
                "step": 1,
                "title": "Document intent and inspect destinations",
                "detail": (
                    "Complete the local-asset and keyword worksheet using "
                    "buyer or seller intent, actual search results, and "
                    "competing page formats. Then define contextual page "
                    "boundaries before creating the architecture and "
                    "programmatic-publishing record. "
                    "[Real Estate SEO & Web Design — xDMs5FogvQ8 @ 00:01:08] "
                    "[Jacob Shireman — Iktexen_-cc @ 00:18:56] "
                    "[Koray Tuğberk GÜBÜR — bWjlnI4gXxo @ 00:01:06]"
                ),
            },
            {
                "step": 2,
                "title": "Inspect publishing and inherited assets",
                "detail": (
                    "Record custom-field mapping and draft review for "
                    "generated pages. Separately document real PR findings, "
                    "archived domain identity, historical URL destinations, "
                    "and source-specific tracking for redirect experiments. "
                    "[Hamida - Programmatic SEO Agency — FO1ASxHYnhE @ 00:02:44] "
                    "[the digitalemania — ufTFZFvsEIM @ 00:01:42] "
                    "[Iron Goo — Z5OwRBCX5ww @ 00:06:32] "
                    "[SEO Jesus — AGcswUV4IEA @ 00:09:01]"
                ),
            },
            {
                "step": 3,
                "title": "Record observations without merging outcomes",
                "detail": (
                    "Keep CTR calculation inputs, post-stop rankings, "
                    "direction requests, customer arrivals, and crawl "
                    "requests distinct. For update and AI-answer reviews, "
                    "separate observed movement from causal explanation "
                    "and repeat comparisons within the same questions, "
                    "engine, and market. "
                    "[Chris Palmer SEO — mg7C81Ti3DY @ 00:12:30] "
                    "[Map Labs — slTweyz4OSs @ 00:00:43] "
                    "[Authority Hacker Podcast — ePxZx_vQNFo @ 00:42:46] "
                    "[The Answer Lab | GEO & AEO — yeLHXIInymI @ 00:07:25]"
                ),
            },
            {
                "step": 4,
                "title": "Connect monetization with operating evidence",
                "detail": (
                    "Finish the income-denominator, ad-placement, provider "
                    "transition, directory-data, and acquisition records. "
                    "Keep the customer's query-solving task and the "
                    "business's operating resources visible when comparing "
                    "the described commercial models. "
                    "[She Knows SEO — xRuzXK8HIFo @ 00:06:05] "
                    "[Meghan's Media — NRcTFL8qghY @ 00:04:05] "
                    "[SaaS SEO Engine — kBXz_ArlMVk @ 00:03:49] "
                    "[Mike Swigunski — w5fG8eKka5Y @ 00:04:47]"
                ),
            },
        ],
    }

    assert len(workbook["worksheets"]) == 6
    assert all(len(item["instructions"]) == 5 for item in worksheets)
    assert all(len(item["fields"]) == 10 for item in worksheets)
    assert len(json.dumps(workbook).split()) >= 5500
    return workbook
