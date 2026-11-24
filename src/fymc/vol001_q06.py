from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "genealogical-sources-research-documentation-and-digital-record-tools",
    "question_prompt": "What do these videos teach about creating genealogical source citations, citing layered online materials and vital records, choosing research logs, evaluating source credibility, linking unindexed images to FamilySearch, using Neo4j graphs and GenAI for entity resolution and deduplication, getting started with Transkribus, understanding forensic investigative genetic genealogy, and checking digital file integrity with Fixity Pro?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Genealogical Sources, Research Documentation, and Digital Record Tools",
    "subtitle": "Source citations in Ancestry and online materials; research log styles; source analysis and verification; linking unindexed images to FamilySearch; birth, marriage, and death record citations; graph-based entity resolution and deduplication; beginner Transkribus workflows; forensic investigative genetic genealogy basics; and digital preservation with Fixity Pro.",
    "layout_template": "step_by_step_blueprint",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Christa Cowen, Diana Elder, Rebecca Coford, and Shannon Green treat documentation "
        "as active research: identify the source, record the search, analyze the information, "
        "and preserve the route back. Elder separates physical records from digital delivery; "
        "Ann Tanner attaches an unindexed birth image to the child and both parents. "
        "Transkribus demonstrates model selection, correction, and custom training, while "
        "Neo4j presenters separate candidate similarity from resolution and debate merging "
        "versus retaining relationships. Their demonstration settings are specific: 300 DPI "
        "JPEGs in the Transkribus introduction and a 0.20 threshold in Johannes's graph "
        "example. Jennifer describes genetic-network reconstruction, distant-match bottlenecks, "
        "and endogamy. ScottishArchivesTV demonstrates repeated checksum scans. The alternatives "
        "concern working methods, not permission to abandon citations or overlook conflicting evidence."
    ),
    "key_metrics": [
        {
            "label": "Transkribus recommended image resolution",
            "metric": "Transkribus recommended image resolution",
            "value": "300 DPI JPEGs",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "The introductory tutorial accepts JPEGs, PNGs, and PDFs and recommends "
                "300 DPI JPEGs for recognition."
            ),
            "source": "Transkribus ([TE9fOzkibiE @ 00:02:07])",
        },
        {
            "label": "Initial research-plan size",
            "metric": "Initial research-plan size",
            "value": "Five or ten ideas",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Rebecca Coford starts with a short plan because plans evolve; the selected "
                "records should answer the research question, whether online or offline."
            ),
            "source": "FamilySearch ([KpQQ3n37XXM @ 00:06:55])",
        },
        {
            "label": "Neo4j demonstration similarity threshold",
            "metric": "Neo4j demonstration similarity threshold",
            "value": "0.20",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Johannes calls this an unusually low threshold for the demonstration, "
                "after multiplying structural similarity by embedding cosine similarity."
            ),
            "source": "Neo4j ([GMTY78xqGXQ @ 00:21:58])",
        },
        {
            "label": "Fixity Pro tutorial pricing",
            "metric": "Fixity Pro tutorial pricing",
            "value": "First 30 days free; $4.99 per month or £50 a year",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "ScottishArchivesTV states these trial and subscription figures, using "
                "dollars for the monthly option and pounds for the annual option."
            ),
            "source": "ScottishArchivesTV ([1pRY7lpZ7nA @ 00:00:27])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "Christa Cowen makes the source citation part of the investigation, not decoration "
                    "added after a tree looks finished. Creating it forces questions about who made "
                    "the record, why it exists, when it was created, and how much weight its information "
                    "deserves. A cemetery marker placed sixty years after a death gets different "
                    "treatment from one placed immediately afterward. Diana Elder puts the same work "
                    "inside a defined sequence: objective, analysis of existing research, locality "
                    "research, research plan, logged searches, and written conclusions. The citation "
                    "is created during the search, while the source is open, rather than reconstructed "
                    "when a report is due. Rebecca Coford calls the log a diary of the entire project, "
                    "including successes, failures, expectations, and ideas. A genealogy program or "
                    "online tree does not replace it because those usually show what was found, not "
                    "the searches that failed or the same-name people excluded. Together, these "
                    "practitioners demand more than an attached image: identify the record, explain "
                    "its use, and leave enough detail to recover the work. Elder then reuses the "
                    "citation in a database, online tree, shared document, and report rather than "
                    "writing a different trail from memory for each destination. Cowen likewise "
                    "connects the citation process to avoiding records that belong to somebody else. "
                    "[7M3XZfN7814 @ 00:09:24] [DUAbGD8rVzA @ 00:04:25] "
                    "[PfqiDmLnMIg @ 00:01:34]"
                ),
                (
                    "Shannon Green's credibility routine starts with a citation, then examines the "
                    "source and its information separately. Was it an original, a derivative, or an "
                    "authored work? Who probably supplied the information, and what could that person "
                    "actually know? Calling something derivative is useful because it points the "
                    "researcher toward the original, not because the label itself settles the case. "
                    "Ancestry's vital-record presenter makes the distinction concrete with James "
                    "Thomas Payne's death certificate: it can be strong evidence for the death while "
                    "providing a birth date reported long afterward by someone probably absent from "
                    "the birth. Cowen makes the complementary point that a death certificate supports "
                    "more than a death event. It may also support name, gender, birth details, parents, "
                    "spouse, and burial. Restricting its image to one fact limits that usefulness. "
                    "Green organizes statements chronologically and tracks relatives and associates, "
                    "especially when several people share a name. The working agreement is to evaluate "
                    "the information item, its informant, and its connection to other records, rather "
                    "than treating every statement on a document as equally strong. The record remains "
                    "a source for several questions, but each answer still needs its own analysis. "
                    "A polished tree and a familiar surname do not perform that analysis for the "
                    "researcher. "
                    "[R50W1KDrRPw @ 00:03:14] [ih5iilWPvjI @ 00:15:17] "
                    "[7M3XZfN7814 @ 00:18:52]"
                ),
                (
                    "Diana Elder and Ann Tanner both move beyond an index when the image can reveal "
                    "more. Elder's Alice Frazier example begins with an indexed entry, then requires "
                    "browsing the film to reach the delayed birth certificate. The original adds the "
                    "creation date and witness information that make the record intelligible. Tanner "
                    "already knows the ancestor and the research target; the demonstration is about "
                    "reaching an unindexed Swedish birth record and attaching that exact image. Tanner "
                    "compares the parents and locality against the tree, checks the person's identifier, "
                    "and attaches the source to the child and both parents. Transkribus's introductory "
                    "presenter approaches historical images from the transcription side: collections "
                    "contain documents, documents contain page images, and recognized text can be "
                    "edited beside its image. Tags mark entities, events, and uncertain readings rather "
                    "than leaving all interpretation buried in an undifferentiated text block. These "
                    "are distinct operations, but the image stays available alongside the extracted "
                    "information in each workflow. Elder also sends a citation with a shared document "
                    "so the next researcher receives its identity and location, not just a loose "
                    "picture. Tanner reloads the tree and checks the resulting source link; the "
                    "Transkribus tutorial similarly keeps text and image views synchronized during "
                    "editing instead of treating recognition as the end of the work. "
                    "[FxQgurvv3_g @ 00:12:21] [zTQCnGBnAvc @ 00:06:17] "
                    "[TE9fOzkibiE @ 00:02:51]"
                ),
            ],
            "table": {
                "caption": "The shared documentary baseline and the work each practitioner actually performs.",
                "headers": [
                    "Research decision",
                    "Practitioner execution",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Create the citation while the source and its surrounding information remain open.",
                        "Elder writes it in the research log first, then copies it into other destinations.",
                        "FamilySearch ([DUAbGD8rVzA @ 00:06:50])",
                    ],
                    [
                        "Treat source creation as an opportunity to inspect provenance and evidential weight.",
                        "Cowen asks who created the record, why it was created, and when it was created.",
                        "Ancestry ([7M3XZfN7814 @ 00:09:24])",
                    ],
                    [
                        "Keep unsuccessful searches alongside successful findings rather than maintaining only a tree.",
                        "Coford records what was searched, where, how, why, and what was not found.",
                        "FamilySearch ([PfqiDmLnMIg @ 00:01:34])",
                    ],
                    [
                        "Separate the reliability of a document from the reliability of individual statements.",
                        "The vital-record presenter distinguishes a death certificate's death evidence from its reported birth information.",
                        "Ancestry ([ih5iilWPvjI @ 00:15:40])",
                    ],
                    [
                        "Investigate an authored or derivative source rather than accepting its appearance as proof.",
                        "Green drafts a citation, examines source creation, and evaluates the likely information provider.",
                        "FamilySearch ([R50W1KDrRPw @ 00:03:14])",
                    ],
                    [
                        "Attach the unindexed image to the people actually named in the record.",
                        "Tanner checks the selected person's identifier, adds both parents, and verifies the resulting link.",
                        "BYU Library Family History Center ([zTQCnGBnAvc @ 00:07:57])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Elder builds layered citations by answering five questions: who, what, when, "
                    "where is, and where in. The digital collection has a creator and location; "
                    "the underlying record or microfilm has its own identity and locating details. "
                    "Keep each layer together, separate layers with semicolons, and avoid repeating "
                    "information already supplied adequately elsewhere. A collection title alone "
                    "does not identify the individual's entry. Add the person, relevant event, and "
                    "the waypoints, page, image, volume, or certificate detail needed to reach it. "
                    "Ancestry's vital-record presenter follows a compatible template: responsible "
                    "entity when applicable, database title, medium, website, URL and access date, "
                    "identifying information, and the original-source details used for evaluation. "
                    "Tanner demonstrates the image-finding side in the FamilySearch catalog. Search "
                    "the place, descend through localities to church records, choose the appropriate "
                    "record type and book years, then move through image numbers to bracket the date. "
                    "Image 90 reaches 1852; image 65 reaches July and August 1848; the preceding "
                    "image supplies the April entry. Tanner checks the birth and christening dates, "
                    "parents, and locality before selecting the tree person and adding the parents. "
                    "The attachment includes a descriptive source title and an explanation of the "
                    "match, followed by reloading the person page to check the link. "
                    "[KtpN2Ws9PA4 @ 00:13:05] [ih5iilWPvjI @ 00:12:52] "
                    "[zTQCnGBnAvc @ 00:05:23]"
                ),
                (
                    "Transkribus's introductory workflow starts with a free account and email "
                    "verification, then organizes uploads into collections, documents, and pages. "
                    "It accepts JPEGs, PNGs, and PDFs and recommends 300 DPI JPEGs. In the beginner "
                    "webinar, Hélène creates a collection, uploads pages, names the document, selects "
                    "pages, and starts processing with an AI model. Filter the model list by "
                    "language, handwritten or printed material, and century; inspect descriptions "
                    "and training material rather than choosing solely from a headline score. "
                    "After recognition, edit the text beside the image, correct the layout where "
                    "needed, add tags, and save. Sonja's custom-model route starts with corrected "
                    "text accurately paired with its image lines, saved as ground truth. A dataset "
                    "collects selected page versions for training, validation, and testing. The "
                    "demonstrated automatic validation split is about ten percent; the displayed "
                    "training setup contains 146 training pages and 16 validation pages. Coford's "
                    "documentation habit supplies a different, manual organization mechanism: when "
                    "tax entries overwhelm the research log, move the repeated records into a "
                    "separate data list and note that location in the log. Coford uses tables or "
                    "spreadsheets to rearrange entries, compare spellings, and inspect neighbors, "
                    "while retaining citations and questions rather than stripping the entries "
                    "down to unexplained names and dates. "
                    "[TE9fOzkibiE @ 00:02:07] [bLXMXvhuz6k @ 00:16:47] "
                    "[bLXMXvhuz6k @ 00:48:58] [J1h18kFbXKU @ 00:05:50]"
                ),
                (
                    "Johannes's Neo4j demonstration first creates a graph projection, then computes "
                    "node similarity from shared relationships. For semantic comparison, node "
                    "properties become text, an embedding is written back to each node, and cosine "
                    "similarity is calculated. The Amazon example multiplies the structural and "
                    "semantic scores, applies an explicitly unusually low 0.20 threshold, creates "
                    "same-as relationships, and merges the paired nodes and their relationships. "
                    "The NODES presenter uses a different two-phase construction: candidate selection "
                    "and ranking through custom rules, followed by community-based resolution. "
                    "Rules can use attributes, graph patterns, or both; the final relationship "
                    "score multiplies similarity by rule importance. The examples assign 0.8 to "
                    "the same-identifier rule and 0.5 to similar-name-and-same-address, according "
                    "to the demonstrated dataset. ScottishArchivesTV's Fixity Pro setup addresses "
                    "the stored files instead: choose history and report locations, create a "
                    "named project, add internal or external directories, and select manual or "
                    "scheduled scanning. The first scan marks files new; the next unchanged scan "
                    "marks them confirmed. A deliberate edit then appears as changed. The report "
                    "also records project name, scan completion, date, and duration. Scheduled "
                    "scans require the computer to be on and Fixity open at the selected time, "
                    "rather than merely having a schedule saved. "
                    "[GMTY78xqGXQ @ 00:20:17] [NtfeEhpvcuk @ 00:08:00] "
                    "[1pRY7lpZ7nA @ 00:04:17] [1pRY7lpZ7nA @ 00:07:10]"
                ),
            ],
            "table": {
                "caption": "Concrete execution settings, locating details, and prices stated by the presenters.",
                "headers": [
                    "Operation and setting",
                    "Exact demonstrated handling",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Distinguish collection-level description from the locating details of the individual entry.",
                        "Elder records the image as 351 of 725 and the physical reference as volume E, page 51.",
                        "FamilySearch ([FxQgurvv3_g @ 00:09:25])",
                    ],
                    [
                        "Create an external Ancestry source before attaching its image to supported facts.",
                        "Cowen selects or creates the source, enters citation details, uploads media, and associates relevant facts.",
                        "Ancestry ([7M3XZfN7814 @ 00:17:36])",
                    ],
                    [
                        "Upload page images in one of the formats identified by the introduction.",
                        "The tutorial accepts JPEGs, PNGs, and PDFs, recommending 300 DPI JPEGs for recognition.",
                        "Transkribus ([TE9fOzkibiE @ 00:02:07])",
                    ],
                    [
                        "Prepare corrected ground truth before starting the demonstrated custom-model training job.",
                        "The displayed setup allocates 146 pages to training and 16 pages to validation.",
                        "Transkribus ([bLXMXvhuz6k @ 00:48:58])",
                    ],
                    [
                        "Label the graph threshold as a setting for Johannes's specific demonstration.",
                        "The combined-score example creates same-as relationships above an unusually low threshold of 0.20.",
                        "Neo4j ([GMTY78xqGXQ @ 00:21:58])",
                    ],
                    [
                        "Keep the tutorial's stated subscription currencies attached to their respective billing periods.",
                        "Fixity Pro is described as free for thirty days, then $4.99 monthly or £50 annually.",
                        "ScottishArchivesTV ([1pRY7lpZ7nA @ 00:00:27])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Small moves that make the record usable again",
                "body": "Use the presenters' locating, comparison, and documentation shortcuts without dropping the underlying source.",
                "items": [
                    (
                        "Start a browsed film at its beginning to learn its organization; Elder found "
                        "the delayed birth certificates arranged alphabetically before searching for "
                        "Alice Frazier. [FamilySearch — FxQgurvv3_g @ 00:13:42]"
                    ),
                    (
                        "If shortening a long record URL after a question mark, test the shortened "
                        "link before keeping it in the citation. "
                        "[FamilySearch — FxQgurvv3_g @ 00:08:27]"
                    ),
                    (
                        "Compare recognition versions through the editor's clock icon before settling "
                        "on a model; Hélène also tries a layout model before text recognition. "
                        "[Transkribus — bLXMXvhuz6k @ 00:33:27]"
                    ),
                    (
                        "Keep facts cited when moving them into timelines: Coford copies and pastes "
                        "from the log and insists that source citations follow the facts. "
                        "[FamilySearch — J1h18kFbXKU @ 00:12:06]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Open a focused plan and log",
                    "action": "Write the research goal, cited background, and initial search ideas.",
                    "detail": (
                        "Coford studies the locality, record availability, and losses, identifies "
                        "repositories, and starts with five or ten ideas that can change as research "
                        "progresses. [FamilySearch — KpQQ3n37XXM @ 00:07:35]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Locate, cite, and attach the actual record",
                    "action": "Capture the entry's identifying details and its physical and digital locations.",
                    "detail": (
                        "Elder answers who, what, when, where is, and where in for layered sources. "
                        "Tanner checks the selected person's identifier and includes the parents when "
                        "the birth record names them. [FamilySearch — KtpN2Ws9PA4 @ 00:04:31] "
                        "[BYU Library Family History Center — zTQCnGBnAvc @ 00:07:57]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Recognize the text and correct the result",
                    "action": "Choose a matching model, inspect text and image together, and save corrections.",
                    "detail": (
                        "Hélène filters models by language, script type, and period; text and layout "
                        "can then be corrected in the editor, with tags added to the transcription. "
                        "[Transkribus — bLXMXvhuz6k @ 00:16:47] "
                        "[Transkribus — bLXMXvhuz6k @ 00:23:25]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Scan the stored digital collection",
                    "action": "Create the Fixity project, choose its directories, run the scan, and read the report.",
                    "detail": (
                        "ScottishArchivesTV sets report paths before scanning, distinguishes internal "
                        "from external directories, and compares later reports with the initial scan "
                        "to identify confirmed or changed files. "
                        "[ScottishArchivesTV — 1pRY7lpZ7nA @ 00:03:09] "
                        "[ScottishArchivesTV — 1pRY7lpZ7nA @ 00:07:10]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "Coford does not prescribe one research-log layout for every case. The "
                    "date-searched style records work in the order performed and fits a straightforward "
                    "investigation. The record-category style groups searches under headings such "
                    "as marriage, land, probate, or tax records and becomes a checklist when "
                    "jurisdictions and record types multiply. The plan-and-log style places findings "
                    "under individual search ideas and can be rearranged as the investigation "
                    "changes. Coford explicitly warns that this last format can become too narrow. "
                    "Elder's citation practice is flexible in a related but separate way: an indexed "
                    "record may be easy to relocate with a basic website URL plus the collection "
                    "and identifying information, while another source warrants the complete "
                    "record URL. The question is how somebody will get back to that entry, not "
                    "whether every citation has the same URL length. Coford personally favors Word "
                    "because it is familiar, searchable, easy to print, and easy to reformat, but "
                    "also permits paper and other familiar software. The contrast is between "
                    "organizational choices, not competing claims that one style discovers all "
                    "answers. Every version still records positive and negative searches, "
                    "citations, questions, and analysis. Elder likewise allows judgment about "
                    "citation presentation while requiring enough source-specific detail to "
                    "recover the record and understand what was actually consulted. "
                    "[PfqiDmLnMIg @ 00:07:36] [J1h18kFbXKU @ 00:18:18] "
                    "[KpQQ3n37XXM @ 00:19:42] [KtpN2Ws9PA4 @ 00:11:11]"
                ),
                (
                    "The sharpest disagreement comes at the end of graph deduplication. Johannes "
                    "merges the demonstration's duplicate nodes after creating same-as links. "
                    "Tomas pushes back on treating that final merge as necessary: leave the "
                    "relationship in place, allow a domain expert to review it, or retain it "
                    "permanently. Merging can lose information and make the original mistake "
                    "hard to recognize later. Tomas also describes researchers choosing a high "
                    "threshold because they preferred missed merges to incorrect merges, whereas "
                    "Johannes deliberately uses a low threshold in a small constructed example. "
                    "The NODES presentation offers another representation choice: store resolution "
                    "as an attribute, create an empty linking node, or create a fused node with "
                    "consolidated attributes. Selection depends on access and traversal requirements. "
                    "Its resolution methods also differ: WCC groups connected nodes broadly, while "
                    "the weighted hierarchical method separates more strongly connected communities. "
                    "Those are alternatives within the demonstrated system, not interchangeable "
                    "labels for a single result. Johannes proposes narrowing candidate groups "
                    "before asking an LLM for further analysis, but says they have not personally "
                    "worked with that combination. Tomas considers an LLM decision step potentially "
                    "more automated and more expensive. Neither presentation supplies a universal "
                    "similarity threshold that turns every related pair into the same person "
                    "or company. "
                    "[GMTY78xqGXQ @ 00:33:01] [GMTY78xqGXQ @ 00:27:34] "
                    "[NtfeEhpvcuk @ 00:11:20] [NtfeEhpvcuk @ 00:18:21]"
                ),
                (
                    "Jennifer distinguishes forensic investigative genetic genealogy from forensic "
                    "genealogy generally: probate work can fall under the broader field without "
                    "involving DNA. In the FIG workflow, matches are built backward to a most "
                    "recent common ancestor and then forward through descendants. Multiple genetic "
                    "networks can reveal a union couple connecting otherwise separate families, "
                    "reducing the descendants that need investigation. Jennifer describes an "
                    "initial STR search before the more resource-intensive SNP-based genealogical "
                    "work, with a candidate reviewed and reference DNA compared back to the "
                    "original STR profile for confirmation. Coford's own difficult genealogy "
                    "project shows a different use of DNA: autosomal match lists, pedigrees, "
                    "and timelines were already in progress when Y-DNA results pointed to a "
                    "completely different surname and required a new research log. These are "
                    "different research settings and different DNA roles. Transkribus likewise "
                    "offers multiple routes rather than one mandatory escalation: quick "
                    "recognition for a page, public models for larger work, and custom training "
                    "when the material or vocabulary demands it. Hélène tries multiple models "
                    "and layout adjustments first; Sonja builds custom training from corrected "
                    "examples when those options fall short. The common operational distinction "
                    "is explicit in their demonstrations: select the approach around the actual "
                    "research problem and material, and change course when the results require "
                    "a different working method. "
                    "[KipqHycd59k @ 00:11:16] [KipqHycd59k @ 00:20:23] "
                    "[KpQQ3n37XXM @ 00:02:27] [bLXMXvhuz6k @ 00:33:10]"
                ),
            ],
            "table": {
                "caption": "Real alternatives, explicit disagreements, and the conditions the speakers attach to them.",
                "headers": [
                    "Choice being made",
                    "Side-by-side practitioner positions",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Choose whether the log follows search chronology, record categories, or research-plan questions.",
                        "Coford uses different styles for different complexity levels while keeping the same documentation habits.",
                        "FamilySearch ([PfqiDmLnMIg @ 00:00:23]); FamilySearch ([KpQQ3n37XXM @ 00:09:47])",
                    ],
                    [
                        "Decide whether a transcription belongs inside an individual citation or in person notes.",
                        "Cowen prefers notes for a combined narrative but explicitly accepts the citation text field.",
                        "Ancestry ([7M3XZfN7814 @ 00:14:15])",
                    ],
                    [
                        "Choose digital-first or physical-first order when assembling the layers of a citation.",
                        "Elder leads with the physical layer for the browsed delayed birth certificate to reflect discovery.",
                        "FamilySearch ([FxQgurvv3_g @ 00:16:03])",
                    ],
                    [
                        "Decide whether a same-as relationship should actually lead to deleting and merging nodes.",
                        "Johannes demonstrates merging; Tomas proposes review or keeping same-as relationships without merging at all.",
                        "Neo4j ([GMTY78xqGXQ @ 00:22:42]); Neo4j ([GMTY78xqGXQ @ 00:33:50])",
                    ],
                    [
                        "Represent a resolution result without assuming every application needs a consolidated record.",
                        "The NODES presenter offers attributes, empty linking nodes, and fused nodes with consolidated attributes.",
                        "Neo4j ([NtfeEhpvcuk @ 00:18:21])",
                    ],
                    [
                        "Choose public recognition models or invest work in training for the specific material.",
                        "Hélène compares models and layout settings first; Sonja trains from accurately corrected ground truth.",
                        "Transkribus ([bLXMXvhuz6k @ 00:33:10]); Transkribus ([bLXMXvhuz6k @ 00:39:06])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Green received hints assigning Mary Taylor the same parents in more than "
                    "a dozen trees. Checking those claims showed that the proposed father was "
                    "twelve when Mary was born, the proposed parents married nine years afterward, "
                    "and their location did not fit Mary's Pennsylvania birth. Popularity had "
                    "not repaired the unsupported relationship. Green's David Durst investigation "
                    "went the other way: a widely copied, unsourced biographical sketch contained "
                    "much that could be verified. Separating its statements, sorting them into "
                    "verification buckets, and adding citations produced a stronger sketch and "
                    "identified an omitted child. Elder encountered a different failure: the "
                    "microfilm had skipped the very page needed for a project. Because the "
                    "reference included the page number, the county clerk could locate the "
                    "original book, photograph the page, and send it. Cowen reports discovering "
                    "previously missed evidence while revisiting older citations created with "
                    "less care. The firsthand reversals are specific: copied trees can repeat "
                    "a false family, an unsourced narrative can contain recoverable evidence, "
                    "a digitized sequence can omit a page, and an old citation can conceal "
                    "an incomplete reading. None of these cases is solved by merely collecting "
                    "another image. The researchers return to the statements, identifying "
                    "details, original records, and reasoning that establish what the material "
                    "actually supports. "
                    "[R50W1KDrRPw @ 00:00:51] [R50W1KDrRPw @ 00:17:26] "
                    "[FxQgurvv3_g @ 00:09:46] [7M3XZfN7814 @ 00:22:56]"
                ),
                (
                    "Johannes runs into inflated similarity in the medical example because a "
                    "generic embedding model treats different medical skills as broadly similar. "
                    "The Amazon example also assigns a high semantic score to Amazon Books "
                    "and Amazon Webstore when the nodes contain little beyond industry and "
                    "name. Johannes attributes the difficulty to sparse extraction and "
                    "emphasizes having more discriminating properties available. Hélène's "
                    "Transkribus session hits a visible execution bottleneck: the recognition "
                    "job is number 198 in the queue, so the demonstration switches to prepared "
                    "documents. Sonja shows a trained model with a fifty-percent character "
                    "error rate and explains that correcting a transcription in the editor "
                    "does not retrain the model. Improvement requires another training job, "
                    "using additional corrected ground truth or changed parameters, followed "
                    "by testing on pages outside the ground-truth set. ScottishArchivesTV "
                    "demonstrates a deliberately edited file appearing as changed in Fixity. "
                    "The same report category calls for investigation when the operator did "
                    "not make the change; the tutorial also says moved or deleted files are "
                    "highlighted. These are separate failure mechanisms: resemblance without "
                    "identity, processing delay, an inadequately trained recognizer, and "
                    "unexpected file changes. Each presenter checks the actual output rather "
                    "than assuming that having run the software means the work is complete. "
                    "[GMTY78xqGXQ @ 00:10:15] [bLXMXvhuz6k @ 00:22:21] "
                    "[bLXMXvhuz6k @ 00:50:20] [1pRY7lpZ7nA @ 00:09:03]"
                ),
                (
                    "Jennifer's hardest matching example had a highest match of roughly ten "
                    "centimorgans and was not close to resolution. A separate search-angel "
                    "case changed abruptly when a half sibling appeared. At Firebird Forensics "
                    "Group, unresolved cases could be watched for new matches after the team "
                    "had exhausted productive work; Jennifer contrasts that with for-profit "
                    "case selection and warnings about extensive labor and additional reference "
                    "samples. Repeated DNA tests add cost, so Jennifer describes usually "
                    "sticking with autosomal work rather than automatically ordering another "
                    "type. Endogamy creates another firsthand reversal: a match appeared no "
                    "more distant than a third cousin in the shared-centimorgan tool, but "
                    "research placed the connection at fifth or sixth cousin through three "
                    "different routes. Separate genetic networks become difficult to distinguish "
                    "when everybody connects to everybody else. Coford encountered a documentary "
                    "version of mistaken consolidation when two Elijah Whitmans were treated "
                    "as one man in online trees. Side-by-side timelines showed the men in "
                    "different places at the same time, and Coford shared the cited comparison "
                    "with other researchers. The economics here are the work the speakers "
                    "actually describe: building multiple trees backward and forward, checking "
                    "new matches, paying for additional analysis, and rebuilding research when "
                    "an apparent identity does not survive comparison. "
                    "[KipqHycd59k @ 00:45:20] [KipqHycd59k @ 00:51:41] "
                    "[KipqHycd59k @ 00:52:47] [KpQQ3n37XXM @ 00:16:05]"
                ),
            ],
            "table": {
                "caption": "Observed reversals, demonstrated checks, and the costs or bottlenecks actually described.",
                "headers": [
                    "Observed problem",
                    "Practitioner response or consequence",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "More than a dozen trees repeated the same unsupported parents for Mary Taylor.",
                        "Green checked ages, marriage timing, and residence and rejected the proposed family connection.",
                        "FamilySearch ([R50W1KDrRPw @ 00:00:51])",
                    ],
                    [
                        "The digitized microfilm omitted the precise page needed for Elder's research project.",
                        "A retained page reference let the county clerk retrieve and photograph the original entry.",
                        "FamilySearch ([FxQgurvv3_g @ 00:09:46])",
                    ],
                    [
                        "Sparse node properties produced high semantic similarity between distinct Amazon-related businesses.",
                        "Johannes explains that better extraction supplies more attributes for differentiating entities during resolution.",
                        "Neo4j ([GMTY78xqGXQ @ 00:18:45])",
                    ],
                    [
                        "Editing recognized text alone does not change the model that produced the errors.",
                        "Sonja adds corrected pages to ground truth and trains a new model version.",
                        "Transkribus ([bLXMXvhuz6k @ 00:51:56])",
                    ],
                    [
                        "A changed file appears in the report even when the change was intentional.",
                        "ScottishArchivesTV distinguishes known edits from unexplained changes that require investigation for possible damage.",
                        "ScottishArchivesTV ([1pRY7lpZ7nA @ 00:09:03])",
                    ],
                    [
                        "Very distant DNA matches can leave a case without a productive next move.",
                        "Jennifer describes watching unresolved cases for new matches and the labor costs of difficult cases.",
                        "Allen County Public Library ([KipqHycd59k @ 00:45:20])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks before accepting the result",
                "body": "Use these practitioner-reported checks to decide what still needs investigation.",
                "items": [
                    (
                        "Check the easiest claims before investing in the hardest ones. Green "
                        "reconsiders the harder verification bucket when the easy statements prove "
                        "inaccurate. [FamilySearch — R50W1KDrRPw @ 00:16:35]"
                    ),
                    (
                        "Decide what information a merge would discard. Tomas keeps same-as "
                        "relationships available for review or permanent use instead of automatically "
                        "merging the nodes. [Neo4j — GMTY78xqGXQ @ 00:33:50]"
                    ),
                    (
                        "Test a newly trained recognizer on some pages outside the ground-truth "
                        "set before recognizing all remaining pages. "
                        "[Transkribus — bLXMXvhuz6k @ 00:52:56]"
                    ),
                    (
                        "Investigate changes you cannot explain in the Fixity report; the tutorial "
                        "distinguishes operator edits from changes that could have damaged a file. "
                        "[ScottishArchivesTV — 1pRY7lpZ7nA @ 00:09:27]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        '"The only wrong way is to not record your searches." '
        "— Rebecca Coford, FamilySearch (J1h18kFbXKU @ 00:02:59)."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        (
            "Write a focused research question and a cited background summary, then place "
            "search results under the planned questions. "
            "[FamilySearch — KpQQ3n37XXM @ 00:09:47]"
        ),
        (
            "Create the citation at the first search, identify the physical and digital "
            "layers, and retain the locating details needed to find the individual record. "
            "[FamilySearch — DUAbGD8rVzA @ 00:06:50] "
            "[FamilySearch — KtpN2Ws9PA4 @ 00:13:05]"
        ),
        (
            "For an unindexed FamilySearch image, verify the person identifier and the "
            "record's family details, attach the source, and check the resulting link. "
            "[BYU Library Family History Center — zTQCnGBnAvc @ 00:07:57]"
        ),
        (
            "Recognize historical pages with a model matched to their material, compare "
            "results, correct the transcription, and use corrected ground truth for custom training. "
            "[Transkribus — bLXMXvhuz6k @ 00:33:27] "
            "[Transkribus — bLXMXvhuz6k @ 00:39:06]"
        ),
        (
            "Inspect the rules and representation of graph-resolution results; retain "
            "same-as links when a merge would discard information needed for review. "
            "[Neo4j — GMTY78xqGXQ @ 00:33:50] "
            "[Neo4j — NtfeEhpvcuk @ 00:18:21]"
        ),
        (
            "Run Fixity again after the initial scan, read confirmed and changed statuses, "
            "and investigate changes that do not correspond to work you performed. "
            "[ScottishArchivesTV — 1pRY7lpZ7nA @ 00:07:10] "
            "[ScottishArchivesTV — 1pRY7lpZ7nA @ 00:09:27]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Ancestry — Crafting Source Citations in Your Ancestry Tree | Ancestry [00:09:24]",
            "url": "https://www.youtube.com/watch?v=7M3XZfN7814&t=564s",
            "relevance": "Primary practitioner testimony on citation creation as source analysis.",
        },
        {
            "title": "FamilySearch — Peeling Back the Layers: Citing Sources From Online Materials, Part 2 [00:04:31]",
            "url": "https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=271s",
            "relevance": "Primary practitioner testimony on the five questions used to construct layered citations.",
        },
        {
            "title": "Neo4j — Neo4j Live: Entity Resolution and Deduplication with Neo4j and GenAI [00:33:50]",
            "url": "https://www.youtube.com/watch?v=GMTY78xqGXQ&t=2030s",
            "relevance": "Primary practitioner testimony on retaining same-as relationships instead of merging records.",
        },
        {
            "title": "Allen County Public Library — The Basics of Forensic Investigative Genetic Genealogy [00:45:20]",
            "url": "https://www.youtube.com/watch?v=KipqHycd59k&t=2720s",
            "relevance": "Primary practitioner testimony on distant-match bottlenecks and unresolved-case work.",
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "7M3XZfN7814",
            "title": "Crafting Source Citations in Your Ancestry Tree | Ancestry",
            "channel": "Ancestry",
            "author": "Ancestry",
            "text": "Probably the most important reason why I create source citations is because in the process of creating them, what I'm doing is I'm analyzing this record.",
            "tip": "Probably the most important reason why I create source citations is because in the process of creating them, what I'm doing is I'm analyzing this record.",
            "timestamp": 564,
            "timestamp_seconds": 564,
            "timestamp_label": "[00:09:24]",
            "url": "https://www.youtube.com/watch?v=7M3XZfN7814&t=564s",
            "markdown": "[00:09:24](https://www.youtube.com/watch?v=7M3XZfN7814&t=564s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on analyzing records during citation creation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "DUAbGD8rVzA",
            "title": "Peeling Back the Layers: Citing Sources from Online Materials, Part 1",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "One tip is to create a source citation the very first time you search a source because it's so much easier to do it right when you're looking at the source.",
            "tip": "One tip is to create a source citation the very first time you search a source because it's so much easier to do it right when you're looking at the source.",
            "timestamp": 410,
            "timestamp_seconds": 410,
            "timestamp_label": "[00:06:50]",
            "url": "https://www.youtube.com/watch?v=DUAbGD8rVzA&t=410s",
            "markdown": "[00:06:50](https://www.youtube.com/watch?v=DUAbGD8rVzA&t=410s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on first-contact citation creation and reuse.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KtpN2Ws9PA4",
            "title": "Peeling Back the Layers: Citing Sources From Online Materials, Part 2",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "Semicolons are an important thing to remember with a layered citation because it separates the layers of the citation.",
            "tip": "Semicolons are an important thing to remember with a layered citation because it separates the layers of the citation.",
            "timestamp": 1040,
            "timestamp_seconds": 1040,
            "timestamp_label": "[00:17:20]",
            "url": "https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=1040s",
            "markdown": "[00:17:20](https://www.youtube.com/watch?v=KtpN2Ws9PA4&t=1040s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on punctuation separating citation layers.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "FxQgurvv3_g",
            "title": "Peeling Back the Layers: Citing Sources From Online Materials, Part 3",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "When you are looking for an original record on the microfilm, it doesn't matter what website it's on, if you can go to the beginning of the microfilm, do that because that will give you an idea of how things are set up and how things are organized.",
            "tip": "When you are looking for an original record on the microfilm, it doesn't matter what website it's on, if you can go to the beginning of the microfilm, do that because that will give you an idea of how things are set up and how things are organized.",
            "timestamp": 822,
            "timestamp_seconds": 822,
            "timestamp_label": "[00:13:42]",
            "url": "https://www.youtube.com/watch?v=FxQgurvv3_g&t=822s",
            "markdown": "[00:13:42](https://www.youtube.com/watch?v=FxQgurvv3_g&t=822s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on inspecting film organization before browsing.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "PfqiDmLnMIg",
            "title": "Research Logs: A Variety of Styles to Suit Your Project, Part 1",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "Research logs are a diary of all the research we do for a single project.",
            "tip": "Research logs are a diary of all the research we do for a single project.",
            "timestamp": 94,
            "timestamp_seconds": 94,
            "timestamp_label": "[00:01:34]",
            "url": "https://www.youtube.com/watch?v=PfqiDmLnMIg&t=94s",
            "markdown": "[00:01:34](https://www.youtube.com/watch?v=PfqiDmLnMIg&t=94s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on recording the entire research project.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "J1h18kFbXKU",
            "title": "Research Logs: A Variety of Styles to Suit Your Project, Part 2",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "The only wrong way is to not record your searches.",
            "tip": "The only wrong way is to not record your searches.",
            "timestamp": 179,
            "timestamp_seconds": 179,
            "timestamp_label": "[00:02:59]",
            "url": "https://www.youtube.com/watch?v=J1h18kFbXKU&t=179s",
            "markdown": "[00:02:59](https://www.youtube.com/watch?v=J1h18kFbXKU&t=179s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on maintaining the habit of logging searches.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KpQQ3n37XXM",
            "title": "Research Logs: A Variety of Styles to Suit Your Project, Part 3",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "A simple plan is really no more than five or ten ideas because plans evolve.",
            "tip": "A simple plan is really no more than five or ten ideas because plans evolve.",
            "timestamp": 415,
            "timestamp_seconds": 415,
            "timestamp_label": "[00:06:55]",
            "url": "https://www.youtube.com/watch?v=KpQQ3n37XXM&t=415s",
            "markdown": "[00:06:55](https://www.youtube.com/watch?v=KpQQ3n37XXM&t=415s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on short, adaptable research plans.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "R50W1KDrRPw",
            "title": "From Questionable to Credible: Analyzing and Verifying Genealogical Sources",
            "channel": "FamilySearch",
            "author": "FamilySearch",
            "text": "I critique the source. I organize the information. And then I verify the evidence.",
            "tip": "I critique the source. I organize the information. And then I verify the evidence.",
            "timestamp": 168,
            "timestamp_seconds": 168,
            "timestamp_label": "[00:02:48]",
            "url": "https://www.youtube.com/watch?v=R50W1KDrRPw&t=168s",
            "markdown": "[00:02:48](https://www.youtube.com/watch?v=R50W1KDrRPw&t=168s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the three-stage source-verification process.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "zTQCnGBnAvc",
            "title": "How to Link Unindexed Images to FS by Ann Tanner    10 minutes",
            "channel": "BYU Library Family History Center",
            "author": "BYU Library Family History Center",
            "text": "We select Amanda Matilda. I check her ID number to make sure I've got the correct person.",
            "tip": "We select Amanda Matilda. I check her ID number to make sure I've got the correct person.",
            "timestamp": 477,
            "timestamp_seconds": 477,
            "timestamp_label": "[00:07:57]",
            "url": "https://www.youtube.com/watch?v=zTQCnGBnAvc&t=477s",
            "markdown": "[00:07:57](https://www.youtube.com/watch?v=zTQCnGBnAvc&t=477s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on checking the selected identity before image attachment.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ih5iilWPvjI",
            "title": "Sourcing Your Vitals - Citations for Birth, Marriage and Death Records | Ancestry",
            "channel": "Ancestry",
            "author": "Ancestry",
            "text": "Family history is not about finding records to attach to your family tree. It's about determining kinship between people and understanding their identity and telling their story.",
            "tip": "Family history is not about finding records to attach to your family tree. It's about determining kinship between people and understanding their identity and telling their story.",
            "timestamp": 159,
            "timestamp_seconds": 159,
            "timestamp_label": "[00:02:39]",
            "url": "https://www.youtube.com/watch?v=ih5iilWPvjI&t=159s",
            "markdown": "[00:02:39](https://www.youtube.com/watch?v=ih5iilWPvjI&t=159s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on kinship and identity as the purpose of record analysis.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "GMTY78xqGXQ",
            "title": "Neo4j Live: Entity Resolution and Deduplication with Neo4j and GenAI",
            "channel": "Neo4j",
            "author": "Neo4j",
            "text": "We're just going to use this unusually low threshold of 0.20, but it's going to work for our purposes here.",
            "tip": "We're just going to use this unusually low threshold of 0.20, but it's going to work for our purposes here.",
            "timestamp": 1318,
            "timestamp_seconds": 1318,
            "timestamp_label": "[00:21:58]",
            "url": "https://www.youtube.com/watch?v=GMTY78xqGXQ&t=1318s",
            "markdown": "[00:21:58](https://www.youtube.com/watch?v=GMTY78xqGXQ&t=1318s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony identifying the graph threshold as demonstration-specific.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "TE9fOzkibiE",
            "title": "Getting started with Transkribus",
            "channel": "Transkribus",
            "author": "Transkribus",
            "text": "Transkribus accepts various formats such as JPEGs, PNGs, or PDFs, but recommends 300 DPI JPEGs for recognition.",
            "tip": "Transkribus accepts various formats such as JPEGs, PNGs, or PDFs, but recommends 300 DPI JPEGs for recognition.",
            "timestamp": 127,
            "timestamp_seconds": 127,
            "timestamp_label": "[00:02:07]",
            "url": "https://www.youtube.com/watch?v=TE9fOzkibiE&t=127s",
            "markdown": "[00:02:07](https://www.youtube.com/watch?v=TE9fOzkibiE&t=127s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on accepted document formats and recommended image resolution.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "KipqHycd59k",
            "title": "The Basics of Forensic Investigative Genetic Genealogy",
            "channel": "Allen County Public Library",
            "author": "Allen County Public Library",
            "text": "We are going to build back our DNA matches until we find what we call a most recent common ancestor, an MRCA.",
            "tip": "We are going to build back our DNA matches until we find what we call a most recent common ancestor, an MRCA.",
            "timestamp": 698,
            "timestamp_seconds": 698,
            "timestamp_label": "[00:11:38]",
            "url": "https://www.youtube.com/watch?v=KipqHycd59k&t=698s",
            "markdown": "[00:11:38](https://www.youtube.com/watch?v=KipqHycd59k&t=698s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on reconstructing genetic matches through common ancestors.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "1pRY7lpZ7nA",
            "title": "Getting Started with Digital Preservation: Fixity Pro",
            "channel": "ScottishArchivesTV",
            "author": "ScottishArchivesTV",
            "text": "Fixity Pro is a file integrity checking tool developed by AVP. It is free to access for the first 30 days and then you have the option to pay $4.99 per month or £50 a year.",
            "tip": "Fixity Pro is a file integrity checking tool developed by AVP. It is free to access for the first 30 days and then you have the option to pay $4.99 per month or £50 a year.",
            "timestamp": 27,
            "timestamp_seconds": 27,
            "timestamp_label": "[00:00:27]",
            "url": "https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=27s",
            "markdown": "[00:00:27](https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=27s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the file-integrity tool and its stated subscription figures.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "NtfeEhpvcuk",
            "title": "NODES 2024 - Beyond the Silos  Achieving Data Harmony With Graph Based ER",
            "channel": "Neo4j",
            "author": "Neo4j",
            "text": "What we will consider in the end is the final value that we got by multiplying the similarity score and the importance score of the rule.",
            "tip": "What we will consider in the end is the final value that we got by multiplying the similarity score and the importance score of the rule.",
            "timestamp": 421,
            "timestamp_seconds": 421,
            "timestamp_label": "[00:07:01]",
            "url": "https://www.youtube.com/watch?v=NtfeEhpvcuk&t=421s",
            "markdown": "[00:07:01](https://www.youtube.com/watch?v=NtfeEhpvcuk&t=421s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on combining rule importance with similarity scoring.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "bLXMXvhuz6k",
            "title": "Transkribus Webinar for Beginners (English)",
            "channel": "Transkribus",
            "author": "Transkribus",
            "text": "You have to train a new model. You have to correct more pages, then put them into the dataset, and then train a new version of your model.",
            "tip": "You have to train a new model. You have to correct more pages, then put them into the dataset, and then train a new version of your model.",
            "timestamp": 3136,
            "timestamp_seconds": 3136,
            "timestamp_label": "[00:52:16]",
            "url": "https://www.youtube.com/watch?v=bLXMXvhuz6k&t=3136s",
            "markdown": "[00:52:16](https://www.youtube.com/watch?v=bLXMXvhuz6k&t=3136s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on retraining rather than expecting editor corrections to update a model.",
        },
    ],
}
