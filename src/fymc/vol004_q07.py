CHAPTER_7 = {
    "id": "Q7", "chapter_id": "Q7", "chapter_number": 7, "question_number": 7,
    "slug": "production-ai-saas-architecture-rag-and-onboarding",
    "question_prompt": "How do three people operate a dependable AI micro-SaaS from ingestion to paid activation?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process: Multi-Tenant Architecture, RAG & Activation",
    "subtitle": "Postgres Row-Level Security (RLS), Tiered Model Routing, Semantic Caching, Golden-Dataset Evals & Sub-5-Minute First-Value Onboarding",
    "layout_template": "research_exhibit", "reading_time_minutes": 14,
    "executive_summary": "Build one narrow intelligence workflow, not a general assistant. The public_record_api_intelligence play turns scattered public filings into source-linked alerts that buyers can act on immediately. Three people can operate it when isolation, ingestion, billing, and evaluation are repeatable systems rather than founder rituals. Use Postgres as the authority, route simple work cheaply, and reserve expensive synthesis for evidence-rich requests. Deliver a useful trial artifact before asking customers to configure integrations. Measure gross subscription billings separately from inference and hosting costs, then subtract delivery labor and operating expenses before calling the remainder owner profit.",
    "key_metrics": [
        {"label": "Routing mix", "value": "85% / 15%", "context": "Small / frontier", "note": "Target, not observed performance."},
        {"label": "Token bill reduction", "value": "40–65%", "context": "Cache hypothesis", "note": "Measure against uncached workload."},
        {"label": "First value", "value": "<5 minutes", "context": "Trial artifact", "note": "Track p90 and failures."}
    ],
    "sections": [
        {
            "heading": "1. Own the public-record ingestion spine",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Start public_record_api_intelligence with one buyer and one decision: a regional supplier wants newly permitted commercial projects before competitors contact them. Ingest municipal permits, court dockets, federal registries, and secretary of state (SOS) filings only where access and reuse permit the intended service. These sources have different clocks, identifiers, correction practices, and coverage. Store source URL, jurisdiction, native record identifier, publication time, observation time, retrieval status, and content hash with every version. Preserve the original document separately from extracted facts. Normalize addresses, legal entity names, project amounts, and event types without discarding source text. A changed permit becomes a new version of an existing record, not a second sales lead. Sell verified changes and useful joins, not an unsupported claim that every public record is instantly available.",
                "Run connectors as queued jobs with per-source rate limits, bounded retries, and checkpoints committed only after durable writes. A unique source and native identifier plus version hash makes replay safe. Quarantine malformed records rather than silently skipping them; expose stale feeds in the operator view. Resolve entities with deterministic identifiers first, then scored name and address matches; retain ambiguous candidates for review instead of merging them automatically. Link a permit to an entity and relevant docket only when evidence supports that relationship. Publish a change event through a transactional outbox after normalization succeeds. Subscribers receive an alert or API event carrying provenance, confidence, and timestamps. The product advantage is accumulated connector maintenance and reliable identity resolution across fragmented sources, not a claim that customers could never reproduce one isolated lookup manually.",
                "Define real-time as a measured latency from source availability to customer delivery, not from an event that the source has not published. Track polling delay, processing delay, delivery delay, and source outage separately. A daily source cannot support a truthful second-by-second freshness promise. Federal FOIA, 5 U.S.C. section 552, supplies a federal agency access framework with exemptions; it does not compel municipal feeds, open sealed dockets, or grant universal redistribution rights. State access rules and individual source restrictions still matter. Minimize personal fields irrelevant to the buyer, honor corrections, and propagate deletions through indexes and caches. Assign the full-time founder product and reliability ownership, one contractor connector upkeep, and another contractor data quality and customer operations. Write backup ownership for every feed so contractor absence cannot strand paid alerts."
            ],
            "table": {
                "caption": "Failure detection before customers discover it",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Public means unrestricted", "Sources lacking documented reuse basis", "Use permitted fields and delivery channels"],
                    ["Every match is certain", "Reviewed false entity merges", "Keep ambiguous entities separate"],
                    ["Polling means live", "Source-to-delivery p95 age", "Show freshness and replay backlog"],
                    ["Shared retrieval is harmless", "Cross-tenant canary matches", "Fail closed under database RLS"]
                ]
            }
        },
        {
            "heading": "2. Make tenant isolation a database invariant",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Give every tenant-owned relational row and pgvector chunk a non-null tenant_id. Enable and FORCE ROW LEVEL SECURITY on each table, using both USING and WITH CHECK policies against a transaction-local tenant setting. Compare tenant_id to nullif(current_setting('app.tenant_id', true), '')::uuid so missing or reset context cannot authorize access. The application role must not own tables, hold BYPASSRLS, or be a superuser; FORCE does not constrain privileged bypass roles. Set context with parameterized set_config inside the same explicit transaction as the query, using its local flag. Derive that identifier from authenticated membership, never from a request body alone. Reset pooled connections by transaction completion, including error paths. Keep administrative migrations on a separate credential unavailable to request handlers, and test isolation through the actual runtime database role used by production traffic.",
                "Use composite tenant-scoped unique keys and foreign keys so an alert cannot reference another customer's document even through a guessed identifier. Cover documents, chunks, saved searches, memberships, exports, jobs, billing links, and audit events. A global permitted-source corpus may live in a separate ingestion schema, but customer annotations and derived retrieval copies remain tenant scoped. Do not grant the request role an alternate unfiltered path into that corpus. Background workers must authenticate their job ownership and establish the same transaction context as synchronous requests. Apply tenant filters before vector retrieval results reach prompts; RLS is the backstop, not a substitute for query design. Measure recall under filtered approximate search and use an exact tenant-scoped fallback when a small eligible corpus makes approximate indexing unreliable or needlessly complicated to operate.",
                "Build retrieval as evidence assembly: select eligible sources, enforce freshness, retrieve tenant-scoped chunks, rerank, then attach stable record and version identifiers. Treat retrieved prose as untrusted data, never as tool instructions. Require structured JSON-schema outputs with explicit fields for entity_id, event_type, evidence_ids, confidence, and abstention_reason. Reject unknown properties, invalid enum values, and references absent from the retrieved evidence. Schema validity is necessary but does not prove factual accuracy; independently check dates, amounts, and citation support. Allow one bounded repair attempt, then return a transparent unresolved result rather than fabricated completion. Keep write-capable tools behind server-side authorization with allowlisted operations and argument validation. Log prompt version, model version, evidence versions, latency, and cost without copying unnecessary sensitive source text into general application logs or contractor debugging channels."
            ]
        },
        {
            "heading": "3. Route, cache, and evaluate before spending",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Implement two routing tiers with explicit task contracts. Target a fast small model for 85% of classification and extraction requests, and a frontier model for 15% of evidence-backed synthesis requests. These percentages are a planning mix, not a universal performance result. Route by task type, evidence length, schema complexity, and calibrated validation outcomes rather than trusting model confidence alone. Escalation counts toward frontier usage, including failed small-model attempts. Set input limits, maximum output tokens, per-tenant budgets, concurrency limits, and deadlines before calling either provider. Retry transient failures with jitter within a bounded request budget; do not retry malformed source facts as if they were network errors. When capacity disappears, queue synthesis and return validated extracted facts with their sources instead of silently switching to an untested model or producing unsupported prose.",
                "Check an exact response cache first, then consider a semantic response cache only for tasks proven insensitive to small wording differences. Scope both by tenant, authorization scope, task, schema version, prompt version, model version, evidence snapshot, and freshness window. Embed queries within that boundary; never search a shared answer pool and filter after generation. A high similarity score cannot establish equivalent dates, jurisdictions, amounts, or entity identities, so compare those structured constraints separately. Disable semantic reuse for volatile account state and ambiguous entity searches. Invalidate affected entries when source versions or permissions change, and verify authorization again on reads. Treat a 40–65% token-bill reduction as a testable target. Report actual avoided token dollars after embedding, lookup, invalidation, and repair costs, comparing equivalent traffic against a measured uncached baseline.",
                "Create a versioned 50-case golden-eval CI gate: twenty extraction cases, ten grounded synthesis cases, ten isolation and injection cases, five cache freshness cases, and five abstention cases. Freeze inputs, source snapshots, expected fields, citations, and acceptable abstentions; include malformed documents and conflicting dates. Require all isolation and stale-answer checks to pass, at least nineteen of twenty extraction cases to meet exact required-field checks, and at least nine of ten synthesis cases to satisfy the citation rubric. Add latency and cost budgets measured on the same workload, with repeated runs for stochastic cases. Fail CI on regression before promoting prompt, retrieval, routing, or model changes. Fifty cases are a minimum regression harness, not statistical proof of reliability. Expand it with production failures and review it using NIST AI RMF measurement principles."
            ],
            "sop_steps": [
                {"step": 1, "title": "Freeze evidence", "action": "Version fifty fixtures.", "detail": "Record expected fields, citations, abstentions, and tenant identity."},
                {"step": 2, "title": "Replay candidates", "action": "Run both routing tiers.", "detail": "Include retries, cache hits, and uncached controls in cost accounting."},
                {"step": 3, "title": "Enforce thresholds", "action": "Fail CI on isolation or freshness defects.", "detail": "Apply field, citation, latency, and cost thresholds before promotion."},
                {"step": 4, "title": "Observe production", "action": "Canary the passing version.", "detail": "Compare sampled evidence support and restore the prior version on regression."}
            ]
        },
        {
            "heading": "4. Turn subscription events into durable entitlements",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Treat Stripe webhooks as duplicated, delayed, and potentially reordered messages. Verify the signature against the raw body with the configured endpoint secret and timestamp tolerance before parsing business fields. Insert the event into a durable inbox with a unique provider event identifier, then acknowledge receipt; a database failure must not receive a success response. Process asynchronously with retries and a dead-letter queue. Resolve customer and subscription identifiers through server-owned tenant mappings rather than trusting editable metadata as authorization. Maintain local states such as trialing, active, past_due, canceled, and expired with an explicit transition table. Do not grant service merely because a checkout browser redirected successfully. Derive entitlements from confirmed subscription and payment policy, recording why each transition occurred and which durable event or reconciliation observation caused it to happen.",
                "Serialize processing per subscription and retrieve current provider state when an event could overwrite newer information. Event creation timestamps alone cannot resolve every ordering race. Commit the updated subscription, entitlement version, event completion, and notification outbox in one database transaction. Use unique effect keys for welcome messages and credits so retries do not repeat customer-visible actions. External sends still need provider idempotency support or delivery deduplication because a worker can crash after sending but before marking completion. Reconcile subscriptions periodically against the provider to recover missing events. Model cancellation at period end separately from immediate termination, and specify a bounded past-due grace policy. Use stable idempotency keys for outgoing billing mutations, but recognize that these keys do not replace inbound deduplication, transaction atomicity, or reconciliation of independently changed provider state.",
                "Expose price, renewal interval, included usage, overage treatment, trial ending behavior, and cancellation access beside the purchase decision. For covered online consumer negative-option transactions, 15 U.S.C. section 8403 requires clear material disclosures before obtaining billing information, express informed consent before charging, and simple mechanisms to stop recurring charges. A B2B label alone does not settle statutory scope; evaluate the actual transaction and applicable rules. Keep a dated record of the offered terms and the purchase action without inserting unrelated onboarding friction. Provide self-service cancellation that updates provider state and then reconciles local access. Instrument payment recovery separately from acquisition: a recovered invoice is not a newly acquired customer. Tie usage limits to durable entitlement versions so cached permissions cannot preserve premium access after the subscription has actually ended."
            ],
            "callout": {
                "kind": "OPERATOR GATE", "title": "Prove replay safety before collecting subscriptions",
                "body": "A successful happy-path checkout is insufficient evidence of a durable billing system.",
                "items": ["Replay one event ten times: one entitlement transition.", "Deliver cancellation before an older update: no resurrection.", "Crash after inbox persistence: processing resumes.", "Reconcile a missing event: provider and local access converge."]
            }
        },
        {
            "heading": "5. Deliver first value, then reconcile owner economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Design onboarding around a finished artifact rather than an empty workspace. Within the first minute, ask for a service territory and buyer category, offering a preselected example that users can change immediately. By minute two, retrieve permitted recent records from the warmed ingestion store; do not make a new trial wait for municipal crawling. By minute three, render three source-linked opportunities with entity names, observed changes, freshness timestamps, and a concise reason each matches the selection. By minute four, let the user save one opportunity or export a brief. Treat that saved or exported evidence-backed brief as the Aha! artifact. Then offer a watchlist and optional integration. When coverage is absent, show a clearly labeled sample territory and its real records, never invented local leads presented as discoveries for that customer's market.",
                "Measure elapsed signup-to-artifact time for every eligible trial, targeting p90 below five minutes and reporting failures rather than excluding abandoned sessions. Track selection completion, evidence opening, artifact saving, watchlist creation, and a second useful visit as separate events. A page render is not activation, and an automated export nobody requests is not value. Test the flow on a slow connection with a fresh account and no configured integrations. Keep source timestamps visible so stale data cannot masquerade as successful onboarding. Interview trials that save nothing: missing coverage, weak matching, and unclear next actions require different fixes. The founder owns weekly funnel review, the data contractor investigates irrelevant matches, and the connector contractor fixes freshness failures. Promote improvements only when time to a meaningful artifact improves without raising unsupported claims or customer support load.",
                "Use annual scenario accounting, not a screenshot of monthly revenue multiplied by twelve. Conservative models $50,000 gross subscription billings at 15% net owner margin, producing $7,500; Base models $375,000 at 30%, producing $112,500; Scaled models $700,000 at 45%, producing $315,000. Staffing is respectively 1 FT + 2 C, 1 FT + 2 C, and 2 FT + 3 C, where FT includes the owner and C means fractional contractors, not full-time equivalents. The table subtracts inference and hosting COGS, paid labor, and other operating costs. Owner profit is cash available before personal tax and before imputing a replacement salary for the working owner; it is not passive economic profit. Conservative cannot sustainably fund a market-rate owner salary. Validate hours, churn, source fees, refunds, and acquisition spend before adopting any scenario as a budget."
            ],
            "table": {
                "caption": "Illustrative annual cash model; no growth forecast or owner salary deduction",
                "headers": ["Scenario / staffing", "Gross subscription billings", "Inference + hosting COGS", "Paid labor", "Other operating costs", "Net owner profit / margin"],
                "rows": [
                    ["Conservative / 1 FT + 2 C", "$50,000", "$10,000", "$15,000", "$17,500", "$7,500 / 15%"],
                    ["Base / 1 FT + 2 C", "$375,000", "$45,000", "$110,000", "$107,500", "$112,500 / 30%"],
                    ["Scaled / 2 FT + 3 C", "$700,000", "$70,000", "$220,000", "$95,000", "$315,000 / 45%"]
                ]
            }
        }
    ],
    "pull_quote": "Your moat is not the model call; it is the dependable chain from fragmented evidence to a tenant-safe artifact worth paying for.",
    "diagram_id": "diag-01-micro-saas-wedge-workflow",
    "action_checklist": [
        "Choose one buyer, jurisdiction, and source-linked alert worth paying for.",
        "Test RLS using two tenants, missing context, and the production role.",
        "Version fifty evaluation cases with evidence and expected abstentions.",
        "Instrument routing costs and tenant-scoped cache invalidation.",
        "Replay duplicate and reordered Stripe events in a test environment.",
        "Time trial signup through a saved artifact and reconcile monthly margins."
    ],
    "statutory_citations": [
        {"title": "NIST AI Risk Management Framework, AI 100-1", "url": "https://doi.org/10.6028/NIST.AI.100-1", "relevance": "Voluntary framework for mapping, measuring, and managing AI risks; not certification."},
        {"title": "5 U.S.C. section 552", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title5-section552&num=0&edition=prelim", "relevance": "Federal agency records access, procedures, and exemptions; not universal public-data permission."},
        {"title": "15 U.S.C. section 8403", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim", "relevance": "Internet negative-option consumer charges: material disclosure, express informed consent, and simple cancellation mechanisms."}
    ]
}
