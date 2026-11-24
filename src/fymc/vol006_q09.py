from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "ai-agents-rag-and-knowledge-graphs-explained",
    "question_prompt": "How do RAG and AI agents work, how can retrieved knowledge help reduce LLM hallucinations, and when should you choose vector retrieval, knowledge graphs, GraphRAG, or agentic workflows? Explore their trade-offs, common retrieval limitations, and practical approaches to building knowledge bases and enterprise RAG systems.",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "AI Agents, RAG, and Knowledge Graphs Explained",
    "subtitle": "An introduction to retrieval-augmented generation, embeddings, vector databases, knowledge graphs, and agentic workflows—covering hallucinations, retrieval strategies, Open WebUI knowledge bases, and enterprise-ready RAG systems.",
    "layout_template": "tool_resource_directory",
    "reading_time_minutes": 15,
    "executive_summary": (
        "Jeff Su, IBM Technology, and Mirketa put the same problem first: a capable model "
        "still needs the company's actual knowledge. Retrieval supplies that context; agents "
        "choose tools and next steps. Professor Patterns demonstrates knowledge-base uploads "
        "in Open WebUI, while Adam Lucek builds GraphRAG with 1,200-token chunks and "
        "100-token overlaps. Cole Medin favors reranking, agentic retrieval, and context-aware "
        "chunking. The architecture debate stays practical: IBM favors long context for bounded "
        "whole-document reasoning; Neo4j emphasizes connected knowledge; Writer preserves graph "
        "relationships through a different storage approach. Mirketa rejects vector search for "
        "every problem. Across these approaches, the recurring bottlenecks are weak retrieval, "
        "broken context, stale information, and added processing costs. Unstructured ties the "
        "build to business outcomes, permission-aware retrieval, and continuing evaluation."
    ),
    "key_metrics": [
        {
            "label": "GraphRAG demonstration chunking",
            "metric": "GraphRAG demonstration chunking",
            "value": "1,200 tokens per chunk; 100-token overlap",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Adam Lucek describes these defaults while indexing the fine-tuning guide; "
                "the demonstration produces about 53 chunks."
            ),
            "source": "Adam Lucek ([6vG_amAshTk @ 00:12:17])",
        },
        {
            "label": "Enterprise evaluation starting set",
            "metric": "Enterprise evaluation starting set",
            "value": "100 to a few hundred Q&A pairs",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Daniel Scoffield recommends a golden set of important questions for "
                "offline testing before prompt or chunking changes are deployed."
            ),
            "source": "Unstructured ([ruilmyfVgrI @ 00:17:28])",
        },
        {
            "label": "Claimed hallucination reduction",
            "metric": "Claimed hallucination reduction",
            "value": "70–90%",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "Hey sidG claims this reduction when RAG is set up correctly; "
                "Mirketa separately emphasizes that grounding can still fail."
            ),
            "source": "Hey sidG ([r4hp_y9_V3w @ 00:02:18])",
        },
        {
            "label": "Reported support resolution improvement",
            "metric": "Reported support resolution improvement",
            "value": "28.6% lower median per-issue resolution time",
            "confidence": "attributed_practitioner_claim",
            "context": (
                "The Neo4j presenters report this result from LinkedIn's customer-support "
                "research while discussing knowledge graphs, rather than their own demo."
            ),
            "source": "AI Engineer ([XNneh6-eyPg @ 00:06:32])",
        },
    ],
    "sections": [
        {
            "id": "practitioner-consensus",
            "title": "The Practitioner Consensus",
            "paragraphs": [
                (
                    "The shared starting point is missing company knowledge, not a model that cannot write. "
                    "Jeff Su illustrates the distinction with a coffee-chat request: an LLM can draft the "
                    "invitation, but it cannot know the next appointment without access to the calendar. "
                    "Their explanation separates limited proprietary knowledge from passivity: the model waits "
                    "for an input rather than independently operating the business [FwOTs4UxQS4 @ 00:01:56]. "
                    "Kaushal makes the same point through a new developer asking for the company's production "
                    "deployment policy. The answer already exists across documents and internal systems; the "
                    "hard part is finding the right knowledge for that question, rather than returning every "
                    "page containing the word production [cxGMp3DBkMk @ 00:01:49]. Mirketa's Rajiv and Alec "
                    "bring that distinction into support. An eligibility-check question can require the customer's "
                    "configuration, a troubleshooting article, three similar resolved cases, and a recent release "
                    "note. Those pieces give the model something specific to reason with instead of a generic "
                    "explanation of claim failures [8N3k2qP_0SY @ 00:04:48]. In each account, the useful change "
                    "is concrete: retrieve the business evidence before generating the response. The knowledge "
                    "layer supplies the circumstances that the base model does not already possess."
                ),
                (
                    "The baseline mechanics are deliberately ordinary: prepare the documents, retrieve relevant "
                    "pieces, and include those pieces with the question. KodeKloud explains embeddings as numerical "
                    "representations that preserve meaning, then applies the same conversion to the user's question. "
                    "Semantic search compares that question representation with stored document representations; "
                    "augmentation inserts the retrieved information into the prompt at runtime "
                    "[_HQ2H_0Ayy0 @ 00:01:50]. This is different from expecting the model to memorize the "
                    "company's entire document collection. IBM's Marina Danilevsky describes the resulting prompt "
                    "as three parts: the instruction, the retrieved content, and the user's question. The model "
                    "then generates an answer that can point back to evidence [T-D1OfcDW1M @ 00:04:00]. "
                    "Mirketa adds an important division of labor: the vector database does retrieval, not "
                    "reasoning. It neither decides the next action nor answers the customer; its job is finding "
                    "candidate information [8N3k2qP_0SY @ 00:12:28]. That separation also explains the attraction "
                    "of retrieval for changing business knowledge. Danilevsky's approach updates the content store "
                    "rather than retraining the model whenever the underlying facts change. The answer is still "
                    "generated, but the relevant knowledge is supplied at answering time, with an identifiable "
                    "source rather than only a remembered association."
                ),
                (
                    "Retrieval and agency solve different parts of the job. Jeff Su's make.com example moves "
                    "news links through Google Sheets, Perplexity summaries, and Claude-written social posts on "
                    "a daily schedule. Because Su sets the path and manually revises disappointing prompts, "
                    "they call it a workflow. The transition to an agent happens when the LLM becomes the "
                    "decision maker, reasoning about the approach and using tools to execute it "
                    "[FwOTs4UxQS4 @ 00:05:25]. Hey sidG makes the business distinction as recalling information "
                    "versus acting on it: finding a travel policy is different from filing an expense report "
                    "or escalating a support ticket. Their hybrid architecture gives the agent retrieval as "
                    "one tool among others, rather than replacing knowledge lookup with orchestration "
                    "[r4hp_y9_V3w @ 00:04:29]. Unstructured's Daniel Scoffield puts the commercial starting point "
                    "before either architecture. Look for high-value friction: expensive employees spending time "
                    "finding important information, support staff moving between sources, or salespeople searching "
                    "internal repositories for questionnaire answers [ruilmyfVgrI @ 00:10:01]. The common operating "
                    "picture is therefore grounded answers attached to an actual workflow. Retrieval supplies "
                    "knowledge, tools provide actions, and the business use case determines which capabilities "
                    "are worth assembling in the first place."
                ),
            ],
            "table": {
                "caption": "The common operating model, from missing knowledge to useful action",
                "headers": [
                    "Operating Principle",
                    "Practitioner Mechanic",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Company knowledge must reach the model before the answer",
                        "Fetch relevant internal information rather than expecting general training to contain the company's private policies or customer configuration.",
                        "Jeff Su ([FwOTs4UxQS4 @ 00:01:56]); AI Engineering with Kaushal ([cxGMp3DBkMk @ 00:04:59])",
                    ],
                    [
                        "Questions and document chunks both receive numerical meaning representations",
                        "Embed the question, compare it with stored document embeddings, and retrieve pieces using semantic similarity instead of exact wording alone.",
                        "KodeKloud ([_HQ2H_0Ayy0 @ 00:01:50])",
                    ],
                    [
                        "The final prompt combines instructions with evidence and question",
                        "Tell the model to retrieve relevant content first, then generate an answer from that content together with the user's request.",
                        "IBM Technology ([T-D1OfcDW1M @ 00:04:00])",
                    ],
                    [
                        "A retrieval database does not decide the customer's next action",
                        "Keep the database's mathematical retrieval job distinct from the model's interpretation and the agent's choice of tools and workflow steps.",
                        "Mirketa Inc ([8N3k2qP_0SY @ 00:12:28])",
                    ],
                    [
                        "An agent changes who selects the next operational step",
                        "Su distinguishes human-programmed paths from an LLM that reasons, acts through tools, observes interim results, and decides whether to iterate.",
                        "Jeff Su ([FwOTs4UxQS4 @ 00:09:29])",
                    ],
                    [
                        "The business starting point is valuable information-search friction",
                        "Scoffield targets important information that expensive employees struggle to locate, then measures outcomes already meaningful to their business leaders.",
                        "Unstructured ([ruilmyfVgrI @ 00:10:01]); Unstructured ([ruilmyfVgrI @ 00:11:34])",
                    ],
                ],
            },
        },
        {
            "id": "street-mechanics",
            "title": "Exact Street Mechanics, Tools & Numbers",
            "paragraphs": [
                (
                    "Professor Patterns demonstrates the shortest visible path to a working knowledge base in "
                    "Open WebUI. Open Workspace, select Knowledge, create a collection, and upload a directory "
                    "of documents. Their example uses candidate resumes in PDF and Word formats. In the chat, "
                    "attach that collection, paste a job description, and ask which candidates fit; they then "
                    "open the underlying resumes to inspect the recommendations [LmXaPUky_u4 @ 00:00:28]. "
                    "The document settings expose the next operational layer: the embedding model, chunk settings, "
                    "top K, and the RAG template. Top K controls how many relevant chunks are passed along, "
                    "while the template provides instructions and citation examples around the retrieved context "
                    "[LmXaPUky_u4 @ 00:09:24]. KodeKloud builds the corresponding Python lab with a virtual "
                    "environment, UV, Chroma DB, Sentence Transformers, OpenAI, and Flask. The lab inspects "
                    "Markdown handbooks, product specifications, meeting notes, and frequently asked questions "
                    "before creating persistent vector storage [_HQ2H_0Ayy0 @ 00:05:28]. Both demonstrations make "
                    "the document collection tangible rather than abstract. One exposes ingestion and retrieval "
                    "through an interface; the other walks through scripts and file-based checks. The common "
                    "sequence is to load known documents, make them searchable, ask concrete questions, and "
                    "inspect the resulting evidence and answer."
                ),
                (
                    "Chunking and ranking are the hands-on adjustments, not decorative settings. In KodeKloud's "
                    "chunking walkthrough, the script uses size 500 and overlap 100, prints chunk statistics, "
                    "and writes a verification file. The ingestion stage later specifies size 500 and stride "
                    "400 while storing embeddings alongside metadata [_HQ2H_0Ayy0 @ 00:06:16]. Cole Medin's "
                    "preferred retrieval adjustment is reranking: first fetch a larger candidate set, then use "
                    "a specialized model, often a cross encoder, to select the few chunks the answering "
                    "model actually receives. They describe this as considering more knowledge without dumping "
                    "20, 50, or more chunks directly into the LLM; the second model adds some cost "
                    "[tLMViADvSNE @ 00:02:48]. Mirketa turns relevance filtering into an empirical task. When "
                    "tuning Case Resolver, Alec tested retrieval separately, measured the scores of real matches "
                    "and unrelated matches on known cases, and placed the similarity cutoff between those "
                    "groups [8N3k2qP_0SY @ 00:30:10]. These are three different controls: how documents are "
                    "broken apart, which candidates get promoted, and whether a candidate is relevant enough "
                    "to use at all. KodeKloud also asks learners to inspect the semantic-search results rather "
                    "than treating a successfully written output file as the end of the exercise."
                ),
                (
                    "Adam Lucek's GraphRAG build starts with a fine-tuning guide converted from PDF to text, "
                    "with the glossary, abstract, title page, and references removed. Initialize the project, "
                    "configure the model and embedding credentials in the settings, and index the corrected "
                    "input directory [6vG_amAshTk @ 00:09:07]. The indexing flow splits text, extracts entities "
                    "and relationships, merges the per-chunk subgraphs, embeds nodes, detects communities, and "
                    "generates community reports. Their demonstration uses 1,200-token chunks with 100-token "
                    "overlaps, producing about 53 chunks [6vG_amAshTk @ 00:12:17]. The Neo4j presenters divide "
                    "construction into a lexical graph of documents and chunks, an entity-and-relationship "
                    "layer, and enrichment through graph algorithms. Existing structured entities can be supplied "
                    "so extraction becomes recognition and relationship finding rather than starting from nothing "
                    "[XNneh6-eyPg @ 00:10:42]. Cole Medin supplies another concrete storage arrangement for "
                    "agentic retrieval: Neon with Postgres and PG Vector, one table containing chunks, and "
                    "another holding document-level information. The agent can choose a semantic search or "
                    "read a whole document [tLMViADvSNE @ 00:03:56]. Across these builds, the richer retrieval "
                    "path comes from explicit stored structure: document membership, entity relationships, "
                    "community summaries, or access to the complete source behind a retrieved chunk."
                ),
            ],
            "table": {
                "caption": "Concrete implementation moves and the settings actually demonstrated",
                "headers": [
                    "Build Move",
                    "Exact Execution Detail",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Create a named knowledge collection and attach it in chat",
                        "In Open WebUI, use Workspace, Knowledge, the plus icon, and a directory upload; select that collection alongside the job-description prompt.",
                        "Professor Patterns ([LmXaPUky_u4 @ 00:00:28])",
                    ],
                    [
                        "Prepare the Python environment and inspect the document collection",
                        "KodeKloud installs UV, Chroma DB, Sentence Transformers, OpenAI, and Flask, then reviews simulated Markdown documents before building persistent storage.",
                        "KodeKloud ([_HQ2H_0Ayy0 @ 00:05:28])",
                    ],
                    [
                        "Record chunk boundaries and inspect the produced ingestion artifacts",
                        "The initial script specifies size 500 and overlap 100; ingestion later specifies size 500 and stride 400, with vectors and metadata stored together.",
                        "KodeKloud ([_HQ2H_0Ayy0 @ 00:06:16]); KodeKloud ([_HQ2H_0Ayy0 @ 00:07:23])",
                    ],
                    [
                        "Retrieve broadly before narrowing the context with another model",
                        "Medin uses a specialized reranker, often a cross encoder, to reduce a larger candidate set to the few chunks sent into generation.",
                        "Cole Medin ([tLMViADvSNE @ 00:02:48])",
                    ],
                    [
                        "Build graph entities and communities from a prepared text document",
                        "Lucek describes 1,200-token chunks with 100-token overlaps, followed by entity extraction, merged relationships, community detection, and community-report generation.",
                        "Adam Lucek ([6vG_amAshTk @ 00:11:21]); Adam Lucek ([6vG_amAshTk @ 00:12:17])",
                    ],
                    [
                        "Preserve both chunk-level retrieval and complete-document access for agents",
                        "Medin's Neon setup uses Postgres with PG Vector, a chunks table, and document-level storage so the agent can choose different search approaches.",
                        "Cole Medin ([tLMViADvSNE @ 00:03:56])",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Adjust the retrieval machinery, not just the final wording",
                "body": (
                    "These implementation choices come directly from the practitioners' "
                    "demonstrations and working preferences."
                ),
                "items": [
                    (
                        "Use a reranker to inspect more candidate knowledge while sending only a few "
                        "high-relevance chunks to the answering model. Medin uses this in almost every "
                        "RAG implementation. [Cole Medin — tLMViADvSNE @ 00:02:17]"
                    ),
                    (
                        "Keep existing entities available during graph extraction. Neo4j describes "
                        "passing known products, partners, clients, or other structured entities into "
                        "the prompt so the model recognizes them and extracts relationships. "
                        "[AI Engineer — XNneh6-eyPg @ 00:11:00]"
                    ),
                    (
                        "Tune the similarity cutoff against known cases. Case Resolver's team measured "
                        "relevant and unrelated match scores before drawing the dividing line. "
                        "[Mirketa Inc — 8N3k2qP_0SY @ 00:30:10]"
                    ),
                    (
                        "After changing the embedding model in Open WebUI, reimport the documents. "
                        "Professor Patterns demonstrates uploading the directory again even though "
                        "the resumes remain visible in the collection. "
                        "[Professor Patterns — LmXaPUky_u4 @ 00:08:04]"
                    ),
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Select the business friction and its outcome",
                    "action": "Identify the important information employees repeatedly struggle to find.",
                    "detail": (
                        "Use Scoffield's high-value, high-friction starting point, then connect the "
                        "project to existing outcomes such as support handle time or sales-cycle "
                        "length. [Unstructured — ruilmyfVgrI @ 00:10:01] "
                        "[Unstructured — ruilmyfVgrI @ 00:11:34]"
                    ),
                },
                {
                    "step": 2,
                    "title": "Load a concrete knowledge collection",
                    "action": "Create a collection, upload documents, and ask questions tied to those documents.",
                    "detail": (
                        "Follow Professor Patterns' Workspace-to-Knowledge sequence in Open WebUI: "
                        "create the collection, upload a directory, attach the collection in chat, "
                        "and inspect the underlying documents behind the recommendations. "
                        "[Professor Patterns — LmXaPUky_u4 @ 00:00:28]"
                    ),
                },
                {
                    "step": 3,
                    "title": "Improve the evidence reaching generation",
                    "action": "Inspect chunks, rerank candidates, and measure the relevance cutoff.",
                    "detail": (
                        "Use Medin's two-stage retrieval to narrow a larger candidate set, then "
                        "apply Mirketa's separate retrieval testing on known relevant and unrelated "
                        "matches. [Cole Medin — tLMViADvSNE @ 00:02:48] "
                        "[Mirketa Inc — 8N3k2qP_0SY @ 00:30:10]"
                    ),
                },
                {
                    "step": 4,
                    "title": "Add structure or tool choice where the question needs it",
                    "action": "Choose graph traversal, broader document access, or iterative retrieval deliberately.",
                    "detail": (
                        "Lucek demonstrates local, global, and DRIFT search for different levels of "
                        "detail; Medin lets an agent choose between semantic chunks and complete "
                        "documents with clear search instructions. "
                        "[Adam Lucek — 6vG_amAshTk @ 00:22:49] "
                        "[Cole Medin — tLMViADvSNE @ 00:04:26]"
                    ),
                },
            ],
        },
        {
            "id": "disagreements-and-alternatives",
            "title": "Where Practitioners Disagree & Alternative Playbooks",
            "paragraphs": [
                (
                    "IBM Technology gives long context a serious place instead of treating a vector database "
                    "as mandatory. For a bounded collection requiring global reasoning, such as comparing full "
                    "requirements with release notes, the speaker favors placing the documents directly in "
                    "context. A search for omitted requirements can retrieve matching snippets without exposing "
                    "the gap between the complete documents [UabBYexBD4k @ 00:06:15]. That simplicity has a "
                    "processing trade-off: IBM's example of a 500-page manual represents roughly 250,000 tokens "
                    "processed repeatedly, while RAG pays the manual's indexing cost upfront. Prompt caching "
                    "partly offsets the repeated work for static information, not constantly changing streams "
                    "[UabBYexBD4k @ 00:07:35]. Cole Medin offers an intermediate playbook through hierarchical "
                    "retrieval: search small chunks precisely, use their metadata to identify the parent file, "
                    "and return the entire document when it is small enough to read "
                    "[tLMViADvSNE @ 00:09:06]. Mirketa draws a different boundary altogether. For account "
                    "balances, case status, entitlement levels, or order numbers, Alec recommends ordinary "
                    "structured database queries. Semantic retrieval earns its place with nuanced documents, "
                    "emails, and case notes [8N3k2qP_0SY @ 00:26:41]. The contrast is about the question "
                    "and the data: complete-document comparison, targeted passage retrieval, and exact structured "
                    "lookup are not the same operational job."
                ),
                (
                    "Graph advocates also take different implementation paths. The Neo4j presenters describe a "
                    "graph retriever beginning with an index search, then following relationships from those "
                    "entry points to bring back additional relevant context. The starting search can be vector, "
                    "full text, or another supported approach; the graph adds connected information rather "
                    "than merely another isolated text fragment [XNneh6-eyPg @ 00:12:44]. Writer's Sam Julien "
                    "reports a historical move away from a conventional graph-database implementation after "
                    "the team encountered scaling costs, expertise limits, and difficulties with the matching "
                    "they needed. Writer instead stored graph-structured data points as JSON in a Lucene-based "
                    "search engine, retaining relationships while using infrastructure the team understood "
                    "[XlAIgmi_Vow @ 00:09:42]. Adam Lucek explores another distinction inside Microsoft's "
                    "GraphRAG: local search gathers specific entity-linked information, global search works "
                    "with community reports, and DRIFT combines broader community information with follow-up "
                    "local searches [6vG_amAshTk @ 00:22:49]. Their comparison produces different answer "
                    "styles, not simply different storage labels. Local retrieval emphasizes particulars; "
                    "global retrieval emphasizes themes; DRIFT generates a more detailed response through "
                    "additional exploration. Lucek explicitly describes graph methods and regular embeddings "
                    "as complementary. Julien likewise argues that the benefits of graph relationships can "
                    "be obtained through different underlying storage approaches."
                ),
                (
                    "The sharpest agentic disagreement concerns how much machinery the problem deserves. Hey "
                    "sidG promotes an agent as the orchestrator, with RAG in its toolbox and a loop that "
                    "retrieves, reads, critiques, and searches again when the evidence is insufficient. They "
                    "also acknowledge the extra latency and compute from repeated thinking and retrieval "
                    "[r4hp_y9_V3w @ 00:04:46]. Kaushal objects to skipping directly from simple RAG to "
                    "agentic RAG while ignoring intermediate choices such as better chunking, metadata, hybrid "
                    "search, and reranking. If classic retrieval already solves the business problem, their "
                    "position is to keep it rather than move automatically to graphs or agents "
                    "[cxGMp3DBkMk @ 00:18:36]. Mirketa challenges another shortcut: agentic does not automatically "
                    "mean autonomous. Alec describes recommendation, preparation, reviewed action, and automatic "
                    "action as different levels; Case Resolver drafts responses and recommendations with "
                    "human review for outgoing work [8N3k2qP_0SY @ 00:30:45]. Cole Medin favors agentic "
                    "retrieval but calls it less predictable and asks for clear instructions about when "
                    "each search method should be used [tLMViADvSNE @ 00:04:26]. These positions share "
                    "retrieval as useful infrastructure while differing on orchestration and autonomy. The "
                    "additional loop is a capability with operational costs, not a requirement attached "
                    "to every knowledge-base project."
                ),
            ],
            "table": {
                "caption": "Alternative playbooks and the conditions each speaker emphasizes",
                "headers": [
                    "Architecture Choice",
                    "Side-by-Side Practitioner Position",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Long context versus retrieval for bounded whole-document reasoning tasks",
                        "IBM favors full context for bounded global comparisons, while preserving retrieval for enterprise collections that cannot fit inside the context window.",
                        "IBM Technology ([UabBYexBD4k @ 00:10:13])",
                    ],
                    [
                        "Ordinary structured queries versus semantic lookup across messy documents",
                        "Mirketa uses database queries for predictable fields and vector retrieval for nuanced unstructured information, rather than applying vector search to everything.",
                        "Mirketa Inc ([8N3k2qP_0SY @ 00:26:41])",
                    ],
                    [
                        "Graph database traversal versus graph relationships stored in search infrastructure",
                        "Neo4j follows relationships after index lookup; Writer describes retaining graph structure as JSON inside a Lucene-based search engine after historical implementation difficulties.",
                        "AI Engineer ([XNneh6-eyPg @ 00:12:44]); AI Engineer ([XlAIgmi_Vow @ 00:09:42])",
                    ],
                    [
                        "Local specifics versus global themes versus combined exploratory retrieval",
                        "Lucek distinguishes local entity-linked evidence, global community reports, and DRIFT's combination of community information with follow-up local searches.",
                        "Adam Lucek ([6vG_amAshTk @ 00:22:49])",
                    ],
                    [
                        "Simple retrieval versus automatic escalation into an agentic architecture",
                        "Kaushal keeps classic RAG when it solves the problem; Hey sidG emphasizes iterative agentic retrieval while acknowledging additional latency and compute.",
                        "AI Engineering with Kaushal ([cxGMp3DBkMk @ 00:18:36]); Hey sidG ([r4hp_y9_V3w @ 00:05:33])",
                    ],
                    [
                        "Confident grounding claims versus explicit limits on hallucination reduction",
                        "Hey sidG claims a 70–90% hallucination drop; Mirketa says wrong, stale, incomplete, or misunderstood retrieval can still produce incorrect confident answers.",
                        "Hey sidG ([r4hp_y9_V3w @ 00:02:18]); Mirketa Inc ([8N3k2qP_0SY @ 00:17:28])",
                    ],
                ],
            },
        },
        {
            "id": "failure-modes-and-economics",
            "title": "Firsthand Failure Modes, Traps & Economics Checks",
            "paragraphs": [
                (
                    "Writer's journey shows where a working retrieval prototype stopped being enough. Sam Julien "
                    "reports that ordinary search handled basic keywords but did not deliver the advanced "
                    "matching the team needed. Vector retrieval then introduced two problems: chunking could "
                    "blur facts, and dense enterprise collections used so much overlapping language that "
                    "nearest-neighbor results became difficult to distinguish. Their Apple timeline example "
                    "confuses the Macintosh date with the nearby Lisa date, while the phone-company example "
                    "has thousands of documents sharing camera and battery terminology "
                    "[XlAIgmi_Vow @ 00:05:34]. Graphs improved context, but converting data into graph structure "
                    "became challenging and costly at scale. The team also encountered expertise limits and "
                    "matching difficulties, leading to a specialized extraction model and a different storage "
                    "approach [XlAIgmi_Vow @ 00:07:47]. Adam Lucek's demonstration exposes the other side of "
                    "richer retrieval: DRIFT gives a longer, more specific answer, but arrives after minutes "
                    "rather than the seconds seen with earlier searches. Their closing comparison explicitly "
                    "includes construction, maintenance, computational overhead, and scaling difficulty "
                    "[6vG_amAshTk @ 00:38:31]. Cole Medin similarly describes LLM-based graph extraction as "
                    "slower and more expensive [tLMViADvSNE @ 00:05:08]. Preserving relationships improves "
                    "what can be retrieved, but these builders do not describe that structure as free."
                ),
                (
                    "Mirketa's most practical retrieval trap is that nearest does not necessarily mean relevant. "
                    "Alec explains that vector search can return the closest available match even when "
                    "the question concerns an undocumented problem. Case Resolver therefore adds similarity "
                    "thresholds and reranking instead of accepting the first returned candidate "
                    "[8N3k2qP_0SY @ 00:11:39]. The same team calls a confident answer built on a stale "
                    "document especially hard to catch: the wording looks correct even though the evidence "
                    "has expired or been replaced. Their framework communicates document age and replacement "
                    "status, while their evaluation separates retrieved information, interpretation, and whether "
                    "the recommendation helped resolve the case [8N3k2qP_0SY @ 00:17:28]. IBM's Marina "
                    "Danilevsky identifies the opposite failure: a model instructed to answer only from "
                    "grounding information may decline an answerable question if the retriever fails to "
                    "surface the right source [T-D1OfcDW1M @ 00:05:35]. KodeKloud's own walkthrough also "
                    "requires careful reading of settings. The initial chunking explanation says overlap "
                    "100, but the closing recap says overlap 400 for the test while retaining stride "
                    "400 for ingestion [_HQ2H_0Ayy0 @ 00:09:18]. Those are different stated settings, not "
                    "a single consistent preset. The working checks remain the retrieved passages, their "
                    "boundaries, and the answers produced from them."
                ),
                (
                    "Enterprise rollout introduces failures beyond the answer itself. Unstructured's Daniel Scoffield "
                    "describes organizations with thousands of pilots and inconsistent ingestion stacks: separate "
                    "teams write PDF scripts, extract Salesforce information differently, and use incompatible "
                    "chunking logic. Their team has repeatedly been brought in to untangle that maintenance "
                    "problem, and Scoffield favors a shared ingestion and RAG ETL layer "
                    "[ruilmyfVgrI @ 00:19:29]. Their evaluation workflow begins with important question-answer "
                    "pairs, tests context relevance and answer faithfulness before changes, and routes negative "
                    "user feedback into retrieval-versus-generation triage. Fixed cases then join the golden "
                    "set [ruilmyfVgrI @ 00:17:28]. Professor Patterns demonstrates a smaller but immediate "
                    "maintenance trap: changing the embedding model in Open WebUI requires reimporting the "
                    "documents even when the collection still displays them [LmXaPUky_u4 @ 00:08:04]. "
                    "Mirketa brings the economics back to support outcomes: did resolution improve, did "
                    "agents accept recommendations, did escalations decline, and did the case remain resolved "
                    "[8N3k2qP_0SY @ 00:30:26]? Scoffield likewise criticizes measuring only technical accuracy "
                    "or tool engagement while ignoring business outcomes. A successful upload, a generated "
                    "answer, and a sophisticated retrieval diagram are separate from that outcome measurement. "
                    "The recurring operational work is keeping ingestion consistent, diagnosing failures at "
                    "the correct stage, and checking whether the system improves the workflow."
                ),
            ],
            "table": {
                "caption": "Observed bottlenecks, demonstrated inconsistencies, and the checks practitioners use",
                "headers": [
                    "Failure or Economic Pressure",
                    "Reported Experience and Practical Check",
                    "Expert Source",
                ],
                "rows": [
                    [
                        "Dense overlapping vocabulary undermined Writer's earlier vector retrieval approach",
                        "Julien reports difficulty comparing similar products across concentrated enterprise documents; preserving relationships and additional context improved the team's retrieval approach.",
                        "AI Engineer ([XlAIgmi_Vow @ 00:06:22])",
                    ],
                    [
                        "Graph construction and scaling exceeded the team's comfortable implementation path",
                        "Writer encountered conversion costs, expertise limits, and matching difficulties, then used specialized extraction and graph-structured JSON in search infrastructure.",
                        "AI Engineer ([XlAIgmi_Vow @ 00:07:47]); AI Engineer ([XlAIgmi_Vow @ 00:09:42])",
                    ],
                    [
                        "A closest vector match can still be irrelevant evidence",
                        "Case Resolver adds thresholds and reranking, with its cutoff tuned by measuring relevant and unrelated matches separately on known test cases.",
                        "Mirketa Inc ([8N3k2qP_0SY @ 00:11:39]); Mirketa Inc ([8N3k2qP_0SY @ 00:30:10])",
                    ],
                    [
                        "More detailed graph answers carried additional retrieval and maintenance overhead",
                        "Lucek observed slower graph retrieval and lists construction, updates, computational overhead, domain expertise, storage, and scaling among the practical drawbacks.",
                        "Adam Lucek ([6vG_amAshTk @ 00:38:31])",
                    ],
                    [
                        "Visible documents remained after an embedding model change required reimporting",
                        "Professor Patterns shows Open WebUI's model-change warning and uploads the directory again rather than treating visible collection entries as completed re-embedding.",
                        "Professor Patterns ([LmXaPUky_u4 @ 00:08:04])",
                    ],
                    [
                        "Independent departmental pilots multiplied inconsistent code and ongoing maintenance",
                        "Scoffield reports repeated cleanup work across divergent enterprise pipelines and recommends a shared ingestion layer plus continuing retrieval and generation evaluation.",
                        "Unstructured ([ruilmyfVgrI @ 00:19:29]); Unstructured ([ruilmyfVgrI @ 00:20:47])",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Checks before calling the knowledge system operational",
                "body": (
                    "Use the practitioners' retrieval, maintenance, permission, and outcome checks "
                    "to distinguish a working demonstration from a dependable business workflow."
                ),
                "items": [
                    (
                        "Can known relevant cases be separated from unrelated nearest matches? "
                        "Test retrieval alone, measure the match scores, and tune the cutoff as "
                        "Case Resolver's team did. [Mirketa Inc — 8N3k2qP_0SY @ 00:30:10]"
                    ),
                    (
                        "Does retrieved access match source-system access? Scoffield describes "
                        "mirroring existing permissions, with metadata prefiltering and finer "
                        "post-retrieval checks as one production approach. "
                        "[Unstructured — ruilmyfVgrI @ 00:15:04] "
                        "[Unstructured — ruilmyfVgrI @ 00:16:24]"
                    ),
                    (
                        "Has a changed embedding model been followed by document reimport? "
                        "Professor Patterns performs that step after Open WebUI's warning even "
                        "though the existing resume collection remains visible. "
                        "[Professor Patterns — LmXaPUky_u4 @ 00:08:04]"
                    ),
                    (
                        "Do the measured benefits reach business outcomes rather than only "
                        "technical scores? Scoffield uses handle time and sales-cycle length; "
                        "Mirketa checks resolution, recommendation acceptance, and escalations. "
                        "[Unstructured — ruilmyfVgrI @ 00:11:34] "
                        "[Mirketa Inc — 8N3k2qP_0SY @ 00:30:26]"
                    ),
                ],
            },
        },
    ],
    "pull_quote": (
        '"You retrieve first, and then you generate second." — '
        "Mirketa Inc (8N3k2qP_0SY @ 00:05:37)."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        (
            "Identify a high-value information-search bottleneck and connect the project to "
            "an existing business outcome before choosing the architecture. "
            "[Unstructured — ruilmyfVgrI @ 00:10:01]"
        ),
        (
            "Create an Open WebUI knowledge collection, upload a document directory, attach "
            "it in chat, and inspect the underlying documents behind the answer. "
            "[Professor Patterns — LmXaPUky_u4 @ 00:00:28]"
        ),
        (
            "Preserve document structure while chunking, then rerank a larger candidate "
            "set into a smaller set of context for generation. "
            "[Cole Medin — tLMViADvSNE @ 00:07:27] "
            "[Cole Medin — tLMViADvSNE @ 00:02:48]"
        ),
        (
            "Match the retrieval path to the question: compare local entity retrieval, "
            "global community summaries, and DRIFT when relationships and broader themes matter. "
            "[Adam Lucek — 6vG_amAshTk @ 00:22:49]"
        ),
        (
            "Distinguish a fixed workflow from an LLM choosing tools and next steps, and "
            "give agentic search clear instructions about when to use each retrieval method. "
            "[Jeff Su — FwOTs4UxQS4 @ 00:05:58] "
            "[Cole Medin — tLMViADvSNE @ 00:04:26]"
        ),
        (
            "Test retrieval separately from generation, route failed answers into diagnosis, "
            "and add corrected question-answer pairs to the continuing evaluation set. "
            "[Mirketa Inc — 8N3k2qP_0SY @ 00:29:36] "
            "[Unstructured — ruilmyfVgrI @ 00:18:30]"
        ),
    ],
    "statutory_citations": [
        {
            "title": "Jeff Su — AI Agents, Clearly Explained [00:05:58]",
            "url": "https://www.youtube.com/watch?v=FwOTs4UxQS4&t=358s",
            "relevance": (
                "Primary practitioner testimony on the distinction between a human-defined "
                "workflow and an LLM acting as the decision maker."
            ),
        },
        {
            "title": "IBM Technology — What is Retrieval-Augmented Generation (RAG)? [00:04:00]",
            "url": "https://www.youtube.com/watch?v=T-D1OfcDW1M&t=240s",
            "relevance": (
                "Primary practitioner testimony on combining instructions, retrieved "
                "content, and the user's question before generation."
            ),
        },
        {
            "title": "Adam Lucek — Knowledge Graph or Vector Database… Which is Better? [00:22:49]",
            "url": "https://www.youtube.com/watch?v=6vG_amAshTk&t=1369s",
            "relevance": (
                "Primary practitioner testimony on local, global, and DRIFT retrieval "
                "over graph-organized knowledge."
            ),
        },
        {
            "title": "Unstructured — Webinar: How to Build Enterprise-Ready RAG Systems [00:17:28]",
            "url": "https://www.youtube.com/watch?v=ruilmyfVgrI&t=1048s",
            "relevance": (
                "Primary practitioner testimony on golden-set evaluation before "
                "deploying prompt and chunking changes."
            ),
        },
    ],
    "source_citations": [
        {
            "source_type": "video_pro_tip",
            "video_id": "FwOTs4UxQS4",
            "title": "AI Agents, Clearly Explained",
            "channel": "Jeff Su",
            "author": "Jeff Su",
            "text": (
                "The one massive change that has to happen in order for this AI workflow "
                "to become an AI agent is for me, the human decision maker, to be replaced by an LLM."
            ),
            "tip": (
                "The one massive change that has to happen in order for this AI workflow "
                "to become an AI agent is for me, the human decision maker, to be replaced by an LLM."
            ),
            "timestamp": 358,
            "timestamp_seconds": 358,
            "timestamp_label": "[00:05:58]",
            "url": "https://www.youtube.com/watch?v=FwOTs4UxQS4&t=358s",
            "markdown": "[00:05:58](https://www.youtube.com/watch?v=FwOTs4UxQS4&t=358s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the decision-making distinction between workflows and agents.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "UabBYexBD4k",
            "title": "Is RAG Still Needed? Choosing the Best Approach for LLMs",
            "channel": "IBM Technology",
            "author": "IBM Technology",
            "text": (
                "The answer existed in the data, but the LLM never saw it because "
                "the retrieval step didn't return the right results."
            ),
            "tip": (
                "The answer existed in the data, but the LLM never saw it because "
                "the retrieval step didn't return the right results."
            ),
            "timestamp": 355,
            "timestamp_seconds": 355,
            "timestamp_label": "[00:05:55]",
            "url": "https://www.youtube.com/watch?v=UabBYexBD4k&t=355s",
            "markdown": "[00:05:55](https://www.youtube.com/watch?v=UabBYexBD4k&t=355s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on silent retrieval failure.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "XlAIgmi_Vow",
            "title": "When Vectors Break Down: Graph-Based RAG for Dense Enterprise Knowledge - Sam Julien, Writer",
            "channel": "AI Engineer",
            "author": "AI Engineer",
            "text": (
                "We take the graph structure, we convert it into JSON, and we put it in the search engine."
            ),
            "tip": (
                "We take the graph structure, we convert it into JSON, and we put it in the search engine."
            ),
            "timestamp": 582,
            "timestamp_seconds": 582,
            "timestamp_label": "[00:09:42]",
            "url": "https://www.youtube.com/watch?v=XlAIgmi_Vow&t=582s",
            "markdown": "[00:09:42](https://www.youtube.com/watch?v=XlAIgmi_Vow&t=582s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Sam Julien's account of storing graph structure in search infrastructure.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "6vG_amAshTk",
            "title": "Knowledge Graph or Vector Database… Which is Better?",
            "channel": "Adam Lucek",
            "author": "Adam Lucek",
            "text": (
                "It is first split by default into chunks of 1,200 tokens with 100-token overlaps."
            ),
            "tip": (
                "It is first split by default into chunks of 1,200 tokens with 100-token overlaps."
            ),
            "timestamp": 737,
            "timestamp_seconds": 737,
            "timestamp_label": "[00:12:17]",
            "url": "https://www.youtube.com/watch?v=6vG_amAshTk&t=737s",
            "markdown": "[00:12:17](https://www.youtube.com/watch?v=6vG_amAshTk&t=737s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the demonstrated GraphRAG chunking defaults.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "cxGMp3DBkMk",
            "title": "RAG Explained: Why LLMs Hallucinate Without a Knowledge Layer",
            "channel": "AI Engineering with Kaushal",
            "author": "AI Engineering with Kaushal",
            "text": "RAG is only as good as its retrieval.",
            "tip": "RAG is only as good as its retrieval.",
            "timestamp": 520,
            "timestamp_seconds": 520,
            "timestamp_label": "[00:08:40]",
            "url": "https://www.youtube.com/watch?v=cxGMp3DBkMk&t=520s",
            "markdown": "[00:08:40](https://www.youtube.com/watch?v=cxGMp3DBkMk&t=520s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on evidence quality as the retrieval bottleneck.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "_HQ2H_0Ayy0",
            "title": "RAG Explained For Beginners",
            "channel": "KodeKloud",
            "author": "KodeKloud",
            "text": "I write a small script that chunks text with a size 500 and overlap 100.",
            "tip": "I write a small script that chunks text with a size 500 and overlap 100.",
            "timestamp": 376,
            "timestamp_seconds": 376,
            "timestamp_label": "[00:06:16]",
            "url": "https://www.youtube.com/watch?v=_HQ2H_0Ayy0&t=376s",
            "markdown": "[00:06:16](https://www.youtube.com/watch?v=_HQ2H_0Ayy0&t=376s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner testimony on the initial chunking script's stated settings.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "XNneh6-eyPg",
            "title": "Practical GraphRAG: Making LLMs smarter with Knowledge Graphs — Michael, Jesus, and Stephen, Neo4j",
            "channel": "AI Engineer",
            "author": "AI Engineer",
            "text": "Median per-issue resolution time was reduced by 28.6%.",
            "tip": "Median per-issue resolution time was reduced by 28.6%.",
            "timestamp": 392,
            "timestamp_seconds": 392,
            "timestamp_label": "[00:06:32]",
            "url": "https://www.youtube.com/watch?v=XNneh6-eyPg&t=392s",
            "markdown": "[00:06:32](https://www.youtube.com/watch?v=XNneh6-eyPg&t=392s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "The Neo4j presenters' reported result from LinkedIn's support research.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8N3k2qP_0SY",
            "title": "Beyond the Case | Episode 6: RAG, AI Agents & Vector Databases — Without the Hype",
            "channel": "Mirketa Inc",
            "author": "Mirketa Inc",
            "text": (
                "When we tuned Case Resolver's similarity cutoff, we tested retrieval on its own, "
                "and then we measured where the real and unrelated matches scored on our test "
                "data, and then we drew the line between them."
            ),
            "tip": (
                "When we tuned Case Resolver's similarity cutoff, we tested retrieval on its own, "
                "and then we measured where the real and unrelated matches scored on our test "
                "data, and then we drew the line between them."
            ),
            "timestamp": 1810,
            "timestamp_seconds": 1810,
            "timestamp_label": "[00:30:10]",
            "url": "https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1810s",
            "markdown": "[00:30:10](https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1810s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Firsthand testimony on tuning Case Resolver's retrieval cutoff.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "T-D1OfcDW1M",
            "title": "What is Retrieval-Augmented Generation (RAG)?",
            "channel": "IBM Technology",
            "author": "IBM Technology",
            "text": (
                "So the prompt now has three parts: the instruction to pay attention to, "
                "the retrieved content, together with the user's question."
            ),
            "tip": (
                "So the prompt now has three parts: the instruction to pay attention to, "
                "the retrieved content, together with the user's question."
            ),
            "timestamp": 240,
            "timestamp_seconds": 240,
            "timestamp_label": "[00:04:00]",
            "url": "https://www.youtube.com/watch?v=T-D1OfcDW1M&t=240s",
            "markdown": "[00:04:00](https://www.youtube.com/watch?v=T-D1OfcDW1M&t=240s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Marina Danilevsky's explanation of the augmented prompt.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "r4hp_y9_V3w",
            "title": "The Future of Enterprise AI: RAG vs. Agentic Workflows",
            "channel": "Hey sidG",
            "author": "Hey sidG",
            "text": (
                "We're talking a 70 to 90% drop in those pesky hallucinations when "
                "you get RAG set up correctly."
            ),
            "tip": (
                "We're talking a 70 to 90% drop in those pesky hallucinations when "
                "you get RAG set up correctly."
            ),
            "timestamp": 138,
            "timestamp_seconds": 138,
            "timestamp_label": "[00:02:18]",
            "url": "https://www.youtube.com/watch?v=r4hp_y9_V3w&t=138s",
            "markdown": "[00:02:18](https://www.youtube.com/watch?v=r4hp_y9_V3w&t=138s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner claim about hallucination reduction from correctly configured RAG.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "LmXaPUky_u4",
            "title": "Open WebUI Knowledge Bases: RAG & Embeddings (Beginner's Guide)",
            "channel": "Professor Patterns",
            "author": "Professor Patterns",
            "text": (
                "If you update or change your embedding model you'll have to reimport all of your documents."
            ),
            "tip": (
                "If you update or change your embedding model you'll have to reimport all of your documents."
            ),
            "timestamp": 484,
            "timestamp_seconds": 484,
            "timestamp_label": "[00:08:04]",
            "url": "https://www.youtube.com/watch?v=LmXaPUky_u4&t=484s",
            "markdown": "[00:08:04](https://www.youtube.com/watch?v=LmXaPUky_u4&t=484s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Demonstrated Open WebUI maintenance requirement after changing embeddings.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ruilmyfVgrI",
            "title": "Webinar: How to Build Enterprise-Ready RAG Systems",
            "channel": "Unstructured",
            "author": "Unstructured",
            "text": (
                "You basically build what's called a golden set. So this is maybe "
                "100 to a few hundred Q&A pairs of your most important questions."
            ),
            "tip": (
                "You basically build what's called a golden set. So this is maybe "
                "100 to a few hundred Q&A pairs of your most important questions."
            ),
            "timestamp": 1048,
            "timestamp_seconds": 1048,
            "timestamp_label": "[00:17:28]",
            "url": "https://www.youtube.com/watch?v=ruilmyfVgrI&t=1048s",
            "markdown": "[00:17:28](https://www.youtube.com/watch?v=ruilmyfVgrI&t=1048s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Daniel Scoffield's proposed starting point for offline RAG evaluation.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "tLMViADvSNE",
            "title": "Every RAG Strategy Explained in 13 Minutes (No Fluff)",
            "channel": "Cole Medin",
            "author": "Cole Medin",
            "text": "I would look at reranking, agentic RAG, and context-aware chunking.",
            "tip": "I would look at reranking, agentic RAG, and context-aware chunking.",
            "timestamp": 747,
            "timestamp_seconds": 747,
            "timestamp_label": "[00:12:27]",
            "url": "https://www.youtube.com/watch?v=tLMViADvSNE&t=747s",
            "markdown": "[00:12:27](https://www.youtube.com/watch?v=tLMViADvSNE&t=747s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Practitioner recommendation for an initial combination of retrieval strategies.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "UabBYexBD4k",
            "title": "Is RAG Still Needed? Choosing the Best Approach for LLMs",
            "channel": "IBM Technology",
            "author": "IBM Technology",
            "text": (
                "You really do need to have a retrieval layer to filter information "
                "down to something that fits into the LLM context window."
            ),
            "tip": (
                "You really do need to have a retrieval layer to filter information "
                "down to something that fits into the LLM context window."
            ),
            "timestamp": 613,
            "timestamp_seconds": 613,
            "timestamp_label": "[00:10:13]",
            "url": "https://www.youtube.com/watch?v=UabBYexBD4k&t=613s",
            "markdown": "[00:10:13](https://www.youtube.com/watch?v=UabBYexBD4k&t=613s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Additional practitioner testimony on retrieval for enterprise-scale collections.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "8N3k2qP_0SY",
            "title": "Beyond the Case | Episode 6: RAG, AI Agents & Vector Databases — Without the Hype",
            "channel": "Mirketa Inc",
            "author": "Mirketa Inc",
            "text": (
                "You can retrieve the wrong information. You can retrieve outdated "
                "information. And you can retrieve just incomplete information."
            ),
            "tip": (
                "You can retrieve the wrong information. You can retrieve outdated "
                "information. And you can retrieve just incomplete information."
            ),
            "timestamp": 1048,
            "timestamp_seconds": 1048,
            "timestamp_label": "[00:17:28]",
            "url": "https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1048s",
            "markdown": "[00:17:28](https://www.youtube.com/watch?v=8N3k2qP_0SY&t=1048s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Additional practitioner testimony on grounding failures despite retrieval.",
        },
        {
            "source_type": "video_pro_tip",
            "video_id": "ruilmyfVgrI",
            "title": "Webinar: How to Build Enterprise-Ready RAG Systems",
            "channel": "Unstructured",
            "author": "Unstructured",
            "text": (
                "You're not creating new metrics here. You're actually moving the needle on their metrics."
            ),
            "tip": (
                "You're not creating new metrics here. You're actually moving the needle on their metrics."
            ),
            "timestamp": 694,
            "timestamp_seconds": 694,
            "timestamp_label": "[00:11:34]",
            "url": "https://www.youtube.com/watch?v=ruilmyfVgrI&t=694s",
            "markdown": "[00:11:34](https://www.youtube.com/watch?v=ruilmyfVgrI&t=694s)",
            "epistemic_status": "attributed_practitioner_claim",
            "relevance": "Additional practitioner testimony on measuring existing business outcomes.",
        },
    ],
}
