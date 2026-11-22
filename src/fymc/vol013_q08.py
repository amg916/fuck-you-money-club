from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small intellectual property licensing desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "USPTO Assignment Records, Copyright Catalogs, SEC Exhibits, Music Identifiers, Dataset Provenance, and Auditable Royalty Pipelines",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #19, Intellectual Property Licensing, ranks #09 with a "
        "88/100 Money-to-Manpower Score. This directory maps four operator plays: "
        "patent licensing, brand licensing, catalog licensing, and dataset licensing. "
        "The edge comes from reconciling public evidence with executed rights "
        "documents, then converting contract obligations into reproducible royalty "
        "calculations. A 1 FT + 3 C pod can run the Conservative and Base cases; "
        "the Scaled case requires 2 FT + 4 C. Annual owner net profit is "
        "$12,500, $180,625, and $480,000 respectively. Recognized operator revenue "
        "consists of license fees and royalties, never licensees' underlying sales. "
        "Use this stack to identify rights owners, expose evidence gaps, validate "
        "reporting, and protect minimum guarantees without building an oversized desk."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$50,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "25% net margin; $12,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "42.5% net margin; $180,625 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "60% net margin; $480,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an eighteen-source directory around four distinct rights plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Organize the directory around four operator plays, not four "
                    "undifferentiated prospect lists. Patent licensing starts with "
                    "publication numbers, issued claims, ownership instruments, "
                    "prosecution history, maintenance status, and territorial family "
                    "members. Brand licensing starts with the exact mark, goods and "
                    "services, owner entity, live registration status, and proposed "
                    "quality-control mechanism. Catalog licensing separates musical "
                    "compositions, sound recordings, photographs, footage, and text "
                    "because identical titles can conceal different rights holders. "
                    "Dataset licensing starts with collection provenance, source "
                    "permissions, personal-data exposure, permitted transformations, "
                    "and redistribution scope. Assign every lead a play before "
                    "buying enrichment. The directory below names eighteen working "
                    "sources and describes access rather than assuming that every "
                    "portal offers an unrestricted API. Cost categories distinguish "
                    "free searches from paid documents, subscriptions, and negotiated "
                    "contracts; they are procurement categories, not current price "
                    "quotes. Latency describes the source's practical evidence "
                    "boundary rather than promising a service level. Record the "
                    "observed update timestamp during onboarding. The full-time "
                    "operator owns source selection, while three contractors cover "
                    "rights research, pipeline engineering, and royalty accounting. "
                    "Specialist counsel can occupy the rights-research allocation "
                    "when interpretation requires it. Contractor seats describe "
                    "capacity, not three additional full-time salaries. Reserve "
                    "specialist hours for disputed links, not routine identifier copying."
                ),
                (
                    "Public records reveal evidence, not a complete permission "
                    "graph. USPTO assignment recordation is especially useful for "
                    "locating conveyance documents and discovering owner-name "
                    "changes, but recording an instrument does not establish its "
                    "validity or legal effect under 37 CFR 3.54. Read the instrument "
                    "and reconcile schedules, signatures, effective dates, exclusions, "
                    "and subsequent transfers. Under 35 U.S.C. 261, patent "
                    "assignments require a written instrument, and recordation "
                    "timing can affect priority against later purchasers or "
                    "mortgagees. A patent family hit therefore cannot substitute "
                    "for a chain-of-title packet. For marks, use TSDR to inspect "
                    "the prosecution file and registration history, then verify "
                    "that the proposed license covers the actual goods, territory, "
                    "channels, and quality controls. For copyrighted catalogs, "
                    "registration and recordation searches help identify claimants "
                    "and transactions, but omissions, older records, pseudonyms, "
                    "and unrecorded transfers prevent a clean search from proving "
                    "exclusive ownership. Section 204 of Title 17 generally "
                    "requires a signed writing for transfers of copyright "
                    "ownership. Treat a registry result as a dated observation "
                    "linked to a document, never as a universal green light. "
                    "Escalate contradictory instruments before issuing a term "
                    "sheet that represents exclusivity or sublicensing authority."
                ),
                (
                    "Treat access policy as part of source engineering. Start "
                    "each connector with the provider's current documentation, "
                    "account entitlement, permitted retention rules, and published "
                    "request limits. A browser search interface is not permission "
                    "to scrape its internal endpoints. Prefer official downloads "
                    "for bulk analysis, documented APIs for incremental refreshes, "
                    "and saved manual extracts when no supported machine interface "
                    "exists. The SEC requires fair-access behavior; identify the "
                    "client and remain below its published maximum rather than "
                    "using every available request slot. Other services may impose "
                    "account-specific quotas, so store limits as configuration "
                    "rather than hard-coded folklore. Honor Retry-After, back off "
                    "with jitter, cache unchanged documents, and halt on repeated "
                    "authorization failures. Record collection time separately "
                    "from filing time, publication time, and the source's last "
                    "update. An overnight pipeline cannot eliminate a registry's "
                    "publication delay. When access fails, preserve the last "
                    "successful snapshot, mark its age, and route a targeted "
                    "manual check instead of silently presenting old evidence as "
                    "fresh. This design lets the four-person pod maintain a "
                    "narrow, useful evidence system without funding a universal "
                    "web crawler or depending on fragile screen automation. "
                    "Review connector health before each material rights decision."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost, Refresh Limits, and Evidence Fallbacks",
                "headers": [
                    "Named source and licensing use",
                    "Exact supported access starting point",
                    "Cost tier and refresh boundary",
                    "Rate-limit and collection hygiene",
                    "Fallback evidence and interpretation limit",
                ],
                "rows": [
                    [
                        "USPTO Patent Public Search for claim and publication discovery",
                        "Open ppubs.uspto.gov/pubwebapp/ and search publication identifiers or classification fields",
                        "Public searching is free; publication events determine document availability",
                        "Use interactive searches; use official bulk products for large collections",
                        "Retrieve published documents through Patent Center; claims still require interpretation",
                    ],
                    [
                        "USPTO Patent Center for application history and prosecution documents",
                        "Open patentcenter.uspto.gov and retrieve publicly accessible application records",
                        "Public records are free; event posting can lag underlying correspondence",
                        "Respect document-access restrictions; do not automate unsupported internal endpoints",
                        "Cross-check published patent documents and obtain authorized applicant records",
                    ],
                    [
                        "USPTO Assignment Center for recorded patent and trademark conveyances",
                        "Start at assignmentcenter.uspto.gov and follow the public assignment search",
                        "Public searching is free; recordation and indexing create timing gaps",
                        "Search exact identifiers and entity variants; cache retrieved conveyance references",
                        "Request executed instruments and schedules directly from the proposed licensor",
                    ],
                    [
                        "USPTO Trademark Search for marks, owners, and goods descriptions",
                        "Open tmsearch.uspto.gov and search word marks, owners, or registration numbers",
                        "Public searching is free; status reflects the searchable registry snapshot",
                        "Use supported searches; avoid extracting undocumented browser service calls",
                        "Use TSDR documents and direct ownership evidence for material conflicts",
                    ],
                    [
                        "USPTO TSDR for trademark status and documentary case history",
                        "Open tsdr.uspto.gov using the serial number or registration number",
                        "Public document access is free; case events post after processing",
                        "Cache case documents; verify current API entitlement before programmatic retrieval",
                        "Compare Trademark Search entries with the underlying dated office documents",
                    ],
                    [
                        "USPTO Open Data Portal for documented patent data products",
                        "Open data.uspto.gov and select documented APIs or available bulk datasets",
                        "Public products generally have free access; release cadence varies by product",
                        "Use required accounts and keys; configure each product's published quotas",
                        "Use official bulk releases or targeted Patent Center document retrieval",
                    ],
                    [
                        "EPO Espacenet and Open Patent Services for international families",
                        "Use worldwide.espacenet.com interactively or developers.epo.org for OPS registration",
                        "Espacenet is free; OPS has usage tiers and product-specific update timing",
                        "Authenticate OPS requests; honor fair-use thresholds and response throttling",
                        "Confirm enforceable national rights through the relevant national patent office",
                    ],
                    [
                        "WIPO PATENTSCOPE for PCT applications and international search documents",
                        "Open patentscope.wipo.int and search publication numbers, applicants, or classifications",
                        "Public searching is free; publication schedules and national collections differ",
                        "Use supported exports; do not assume unrestricted public API availability",
                        "Check national registers because PCT publication does not establish national grant",
                    ],
                    [
                        "WIPO Global Brand Database for cross-border trademark discovery",
                        "Open branddb.wipo.int and search marks, holders, or image similarities",
                        "Public searching is free; participating collection updates have differing delays",
                        "Use permitted interactive workflows and observe export or session restrictions",
                        "Verify status and scope against each relevant national trademark register",
                    ],
                    [
                        "U.S. Copyright Office public records systems for catalog claims",
                        "Start at copyright.gov/public-records/ and select the applicable records system",
                        "Public searches are free; certified searches and copies may incur fees",
                        "Follow collection-specific access rules; distinguish older records from current coverage",
                        "Obtain signed transfers, creator agreements, and recordation documents from counterparties",
                    ],
                    [
                        "SEC EDGAR for disclosed licenses, royalty terms, and counterparties",
                        "Use sec.gov/edgar/search/ and documented data.sec.gov submissions or companyfacts endpoints",
                        "Public access is free; accepted filings appear before every downstream index refreshes",
                        "Send identifying User-Agent details; stay below the published ten requests per second",
                        "Read actual filing exhibits; redactions and disclosure thresholds limit completeness",
                    ],
                    [
                        "Delaware Division of Corporations entity search for legal-name resolution",
                        "Follow corp.delaware.gov links to the official entity-name search service",
                        "Basic name searching is free; status certificates and detailed reports cost extra",
                        "Use supported searches; order certificates rather than repeatedly polling results",
                        "Obtain formation documents and check the entity's actual jurisdiction directly",
                    ],
                    [
                        "The MLC Public Work Search for composition matching",
                        "Open portal.themlc.com/search and search works, writers, publishers, or identifiers",
                        "Public searching is free; registrations and matching updates create timing differences",
                        "Use permitted searches and available exports; seek permission before bulk collection",
                        "Reconcile publisher schedules and other repertoire sources; entries are not blanket licenses",
                    ],
                    [
                        "ASCAP and BMI Songview for performing-rights repertoire cross-checks",
                        "Enter Songview through the official ASCAP or BMI repertoire-search pages",
                        "Public searching is free; participating repertoire updates do not cover every right",
                        "Respect portal terms and session controls; avoid unsupported bulk extraction",
                        "Obtain publisher confirmations for synchronization, mechanical, and disputed ownership questions",
                    ],
                    [
                        "MusicBrainz Web Service for recording and release identifier enrichment",
                        "Use musicbrainz.org/doc/MusicBrainz_API and documented /ws/2/ lookup endpoints",
                        "Public API access has usage conditions; commercial arrangements may require separate terms",
                        "Identify the application and observe the documented one-request-per-second public limit",
                        "Use licensed dumps where permitted; identifiers never establish recording ownership",
                    ],
                    [
                        "OpenAlex API for scholarly provenance and associated dataset discovery",
                        "Use docs.openalex.org for current authentication, API endpoints, and snapshot guidance",
                        "Free and paid access options depend on current plans and usage budgets",
                        "Configure current key requirements and quotas; cache identifiers and use permitted snapshots",
                        "Verify original repository licenses and source publications before offering dataset rights",
                    ],
                    [
                        "People Data Labs Company Enrichment API for business-entity matching",
                        "Use docs.peopledatalabs.com and the documented company enrichment endpoint",
                        "Metered API plans and contracted tiers apply; profile recency varies by record",
                        "Keep API keys server-side and enforce spend ceilings before fallback requests",
                        "Confirm domains and legal names through official filings and company-owned pages",
                    ],
                    [
                        "Hunter Domain Search and Email Verifier for business-contact routing",
                        "Use hunter.io/api-documentation for authenticated domain search and verification endpoints",
                        "Limited free allowances and paid credit plans apply; verification is point-in-time",
                        "Budget domain searches separately from verification and honor plan-specific throttles",
                        "Use official licensing inboxes; email deliverability does not establish purchasing authority",
                    ],
                ],
            },
        },
        {
            "heading": "2. Resolve owners before spending on commercial enrichment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create an entity-resolution waterfall that spends money only "
                    "after public evidence establishes a plausible transaction. "
                    "First normalize asset identifiers: publication and application "
                    "numbers for patents, serial and registration numbers for "
                    "marks, ISWC for compositions, ISRC for recordings, and "
                    "versioned repository identifiers for datasets. Preserve raw "
                    "values alongside normalized values so punctuation cleanup "
                    "cannot conceal a mistaken match. Second resolve the "
                    "contracting entity using jurisdiction, formation identifier "
                    "where available, prior names, acquisition history, and "
                    "official domain. Third attach documentary ownership evidence "
                    "and identify the missing link. Fourth enrich the company, "
                    "then locate a relevant licensing or business-development "
                    "contact. People Data Labs can help distinguish businesses "
                    "with similar names; Hunter can help route a message to a "
                    "business mailbox. Neither service proves title, authority, "
                    "or willingness to license. Require a confidence explanation "
                    "such as matching registration number plus recorded transfer, "
                    "not an opaque score alone. Merge records only when the "
                    "identifier evidence supports the merge. A shared postal "
                    "address, outside lawyer, distributor, or corporate parent "
                    "is a relationship signal, not proof that two legal entities "
                    "are interchangeable. This ordering avoids enriching hundreds "
                    "of irrelevant subsidiaries before the desk knows which entity "
                    "can actually sign."
                ),
                (
                    "Give each play a different evidence packet and commercial "
                    "question. The patent packet contains the claim set, family "
                    "map, assignment chain, prosecution events, and a technically "
                    "supported use hypothesis; keyword overlap is insufficient. "
                    "The brand packet contains registration documents, actual "
                    "market use, licensed categories, territory, channel restrictions, "
                    "and a workable product-review process. The catalog packet "
                    "distinguishes composition from master rights, identifies "
                    "writers and performers where relevant, and records ownership "
                    "shares, territory, media, term, and any required third-party "
                    "permissions. Songview and The MLC help reconcile composition "
                    "metadata, but neither replaces a synchronization license or "
                    "a master-use agreement. The dataset packet records every "
                    "upstream source, collection date, source terms, version, "
                    "redistribution permission, attribution requirement, and "
                    "deletion dependency. Public availability does not itself "
                    "authorize commercial redistribution. Under 17 U.S.C. 102(b), "
                    "copyright does not extend to ideas, procedures, systems, or "
                    "methods; a claimed dataset right therefore needs a precise "
                    "basis rather than a sweeping assertion that all facts are "
                    "owned. Contract restrictions and other applicable rights "
                    "must be analyzed separately. Write the proposed grant in "
                    "plain operational terms before pricing it, because enrichment "
                    "cannot repair an incoherent description of the asset or "
                    "the permitted use."
                ),
                (
                    "Operate the waterfall through a weekly exception queue. "
                    "The full-time operator selects commercially credible targets "
                    "and owns counterpart communications. The rights contractor "
                    "resolves ownership gaps and flags questions requiring "
                    "specialist interpretation. The engineering contractor maintains "
                    "connectors, matching rules, and freshness reports. The royalty "
                    "contractor checks whether the contemplated reporting fields "
                    "can support the proposed fee structure. Batch ordinary "
                    "research, but give exclusive-rights conflicts and contradictory "
                    "transfers immediate attention. Store enrichment cost per "
                    "qualified rights packet, not merely cost per email address. "
                    "A cheap contact record becomes expensive when the desk "
                    "spends two hours approaching the wrong owner. Use a "
                    "stop-loss rule: after the agreed research budget is consumed, "
                    "record the unresolved issue and request documents directly "
                    "rather than purchasing another nearly identical profile. "
                    "Maintain a suppression list for contacts who decline "
                    "outreach and for invalid addresses. For commercial email, "
                    "implement the sender identification, truthful routing, postal "
                    "address, and opt-out requirements that apply under 15 U.S.C. "
                    "7704. Keep outreach permission and asset-licensing permission "
                    "as separate records. A responsive executive may lack signing "
                    "authority; a verified mailbox establishes neither authority "
                    "nor ownership. Measure the queue by resolved blockers and "
                    "qualified conversations, not raw enrichment volume."
                ),
            ],
            "table": {
                "caption": "Six-Step Evidence-First Enrichment Waterfall for the Four-Person Pod",
                "headers": [
                    "Waterfall stage and responsible seat",
                    "Required inputs and practical matching rule",
                    "Release condition and stored evidence",
                    "Stop condition and next useful action",
                ],
                "rows": [
                    [
                        "Full-time operator defines one play and the intended commercial grant",
                        "Record asset category, target territory, use case, and likely buyer segment",
                        "Proceed when the proposed use can be described without ambiguous rights labels",
                        "Pause broad prospecting when the commercial grant remains internally contradictory",
                    ],
                    [
                        "Rights contractor resolves asset identifiers against relevant official records",
                        "Match exact registration or publication identifiers before comparing names and titles",
                        "Save source documents, retrieval dates, raw identifiers, and normalization decisions",
                        "Separate lookalike works or assets instead of forcing a convenient merge",
                    ],
                    [
                        "Rights contractor assembles title evidence and identifies any missing transfer",
                        "Compare signed instruments, asset schedules, exclusions, and effective transaction dates",
                        "Document a supported ownership path and explicitly bounded unresolved questions",
                        "Request missing instruments directly before representing exclusive or sublicensable rights",
                    ],
                    [
                        "Engineering contractor resolves the legal entity before commercial API enrichment",
                        "Compare official names, jurisdictions, domains, and documented predecessor entity relationships",
                        "Retain match reasons and vendor response versions for later correction",
                        "Reject parent-subsidiary substitution when the contracting entity is not established",
                    ],
                    [
                        "Full-time operator enriches relevant business contacts within a fixed budget",
                        "Use company domains and licensing roles before purchasing individual contact details",
                        "Store contact provenance, verification date, outreach status, and suppression preferences",
                        "Use the official licensing inbox when commercial profiles conflict or expire",
                    ],
                    [
                        "Royalty contractor tests reporting feasibility before economic terms become final",
                        "Map proposed royalty definitions to fields the licensee can actually export",
                        "Approve the evidence packet for negotiation with a reproducible reporting specification",
                        "Redesign reporting terms when deductions or territories cannot be independently reconciled",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Spend on missing evidence, not redundant profiles",
                "body": (
                    "Experienced licensing desks use enrichment to shorten a "
                    "specific decision, not to decorate an incomplete rights file."
                ),
                "items": [
                    "Search predecessor names and assignment schedules before assuming that the current registry owner is the complete contracting story.",
                    "For music, retain both ISWC and ISRC where relevant; matching a song title never clears both composition and recording rights.",
                    "Read EDGAR license exhibits for audit windows, deduction definitions, and minimum-guarantee mechanics, while treating redacted schedules as evidence gaps.",
                    "Ask dataset suppliers for one versioned provenance manifest and one worked downstream-use example before buying a broad commercial data subscription.",
                ],
            },
        },
        {
            "heading": "3. Build a reproducible evidence pipeline with visible exceptions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a small evidence architecture with explicit lineage. "
                    "SQLite is sufficient for an initial desk if one controlled "
                    "writer handles imports; PostgreSQL becomes useful when "
                    "concurrent work and access separation justify the operational "
                    "burden. Store entities, assets, source observations, ownership "
                    "assertions, contracts, reporting periods, and exceptions as "
                    "separate tables. An ownership assertion must reference "
                    "evidence, scope, and effective dates; it must not overwrite "
                    "the raw registry observation. Keep original PDFs, CSVs, and "
                    "JSON responses in versioned object storage with access "
                    "controls and retention aligned to source permissions. "
                    "Calculate SHA-256 digests using Python's hashlib, but "
                    "remember that a digest detects later changes rather than "
                    "proving that the original claim was true. Use deterministic "
                    "record keys and ingestion identifiers so rerunning a job "
                    "does not duplicate licenses or obligations. Separate "
                    "retrieved_at, source_updated_at, effective_from, and "
                    "effective_to timestamps. Preserve currency, units, timezone, "
                    "and source precision rather than normalizing them away "
                    "without a trace. Every dashboard assertion should resolve "
                    "to the underlying observation and document. This structure "
                    "makes a rights dispute or royalty challenge answerable "
                    "through evidence, instead of requiring the operator to "
                    "reconstruct months of decisions from email threads. "
                    "Keep correction history append-only where source permissions allow."
                ),
                (
                    "Build connectors as short, testable adapters. Python's "
                    "urllib.request, csv, json, sqlite3, decimal, and unittest "
                    "can support a lean first implementation without third-party "
                    "dependencies. Configure credentials outside source files, "
                    "redact them from logs, and separate read access from "
                    "administrative permissions. A connector should emit a "
                    "source identifier, retrieval timestamp, response digest, "
                    "schema version, and explicit success or failure state. "
                    "Validate required fields before loading transformed tables. "
                    "A provider returning an HTML login page with a successful "
                    "HTTP status must fail content validation rather than enter "
                    "the warehouse as usable data. Handle pagination with saved "
                    "checkpoints and deduplicate on stable identifiers. Use "
                    "conditional requests where supported, bounded retries for "
                    "transient failures, and immediate escalation for revoked "
                    "credentials. Diagnose HTTP behavior with curl or Postman "
                    "against authorized endpoints, inspect certificates with "
                    "OpenSSL, and use SQL EXPLAIN when queries slow down. "
                    "For document comparisons, use difflib on extracted text "
                    "and retain the original page reference. OCR output is a "
                    "search aid, not the governing contract text. A single "
                    "misread decimal or omitted exception can reverse an "
                    "obligation, so verify extracted rates and deadlines against "
                    "the signed document before activating calculations or alerts."
                ),
                (
                    "Define refresh cadence by decision risk rather than by "
                    "the availability of a scheduler. Recheck title and status "
                    "before an offer, signature, renewal, or material expansion "
                    "of territory; monitor active assets at a cadence matched "
                    "to the relevant source and contract. Refresh royalty "
                    "reporting when a statement arrives, then reconcile it "
                    "against the agreed delivery deadline. Store renewal, "
                    "notice, cure, audit, and minimum-guarantee dates as "
                    "structured obligations with named owners and separate "
                    "reminder offsets. Calendar reminders alone cannot "
                    "distinguish an expiring license from an auto-renewal "
                    "requiring timely cancellation. The engineering contractor "
                    "runs daily connector health checks, while the operator "
                    "reviews only changes that alter a decision or require "
                    "action. Test against frozen sample records: renamed "
                    "owners, split territories, duplicate statement uploads, "
                    "missing pages, refunded sales, and expired API keys. "
                    "Track source age, parse failures, unmatched identifiers, "
                    "and unresolved obligations on one exception board. "
                    "Require each exception to carry an owner, next action, "
                    "and due date. If a source disappears, the desk should "
                    "know which conclusions depend on it and which manual "
                    "checks preserve deal continuity. This dependency map is "
                    "more valuable than another dashboard showing total "
                    "records collected without any indication of decision readiness."
                ),
            ],
            "table": {
                "caption": "Six Pipeline Diagnostics That Prevent Silent Rights and Reporting Errors",
                "headers": [
                    "Failure signature and likely consequence",
                    "Named diagnostic tool and practical test",
                    "Evidence retained for reproducible investigation",
                    "Pod owner and recovery procedure",
                ],
                "rows": [
                    [
                        "Successful HTTP response contains a login page instead of expected records",
                        "Use curl headers and Python content validation before accepting the payload",
                        "Retain redacted headers, content type, response digest, and retrieval timestamp",
                        "Engineering contractor repairs authentication and reruns only the affected checkpoint",
                    ],
                    [
                        "Source schema changes silently remove an ownership or territory field",
                        "Run unittest fixtures against required keys and representative transformed records",
                        "Save schema versions and a minimal permitted sample demonstrating the difference",
                        "Engineering contractor quarantines the import while rights research checks material changes",
                    ],
                    [
                        "Entity matching joins a parent corporation to a subsidiary's asset",
                        "Run SQL conflict queries across jurisdictions, entity identifiers, and assignment references",
                        "Retain competing matches and the exact evidence used for each relationship",
                        "Rights contractor splits the records and requests the correct contracting instrument",
                    ],
                    [
                        "Repeated statement imports inflate the reported license-fee or royalty total",
                        "Compare file hashes and unique contract-period-version keys before posting entries",
                        "Keep upload manifests, deduplication decisions, and superseded statement version references",
                        "Royalty contractor reverses duplicate postings through a visible correction record",
                    ],
                    [
                        "OCR converts a contractual rate or deadline into an incorrect value",
                        "Compare difflib output with the signed PDF page and extraction coordinates",
                        "Retain page references and the human-confirmed rate or obligation field",
                        "Rights contractor confirms meaning before engineering enables the resulting calculation",
                    ],
                    [
                        "A healthy scheduler repeatedly serves evidence older than the decision allows",
                        "Query source timestamps separately from retrieval timestamps and connector run status",
                        "Store freshness thresholds, last material source update, and affected contract identifiers",
                        "Full-time operator orders targeted manual checks before relying on stale evidence",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and its permitted use",
                    "action": "Record official access documentation, account scope, retention terms, quotas, and fallback procedure.",
                    "detail": "Assign one connector owner and distinguish public observations from private counterparty documents.",
                },
                {
                    "step": 2,
                    "title": "Capture a reproducible evidence snapshot",
                    "action": "Save the authorized response or document with timestamps, identifiers, version information, and a SHA-256 digest.",
                    "detail": "Preserve the original representation and record any extraction or normalization applied afterward.",
                },
                {
                    "step": 3,
                    "title": "Validate the decision-bearing fields",
                    "action": "Test identifiers, title links, territorial scope, rates, reporting periods, and date interpretations.",
                    "detail": "Route contradictions to the rights or royalty contractor instead of silently choosing a convenient value.",
                },
                {
                    "step": 4,
                    "title": "Publish bounded conclusions and schedule rechecks",
                    "action": "Attach evidence links, freshness limits, obligation owners, and next-action dates to the operator view.",
                    "detail": "Recheck material rights before signature and preserve an audit trail of later corrections.",
                },
            ],
        },
        {
            "heading": "4. Reconcile royalty evidence to the scorecard without counting licensee sales",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The pipeline earns its keep when it converts a signed "
                    "definition into a repeatable statement calculation. Suppose "
                    "a brand agreement pays five percent of defined net sales, "
                    "and an accepted annual report shows $2,000,000 of eligible "
                    "sales after contractually permitted deductions. The computed "
                    "royalty is $100,000, not $2,000,000 of operator revenue. "
                    "If that same annual period carries a $60,000 recoupable "
                    "minimum guarantee already paid and credited against those "
                    "royalties, the remaining royalty balance is $40,000; "
                    "adding the guarantee again would overstate the economics. "
                    "Actual recognition timing follows the agreement and the "
                    "applicable accounting treatment, so store earned amounts, "
                    "invoiced amounts, cash receipts, and guarantee credits "
                    "separately. Apply equivalent discipline to patent royalties "
                    "per covered unit, catalog fees per permitted exploitation, "
                    "and dataset subscriptions by authorized delivery or usage "
                    "tier. A perpetual license, a refundable advance, and an "
                    "annual access fee do not automatically share the same "
                    "recognition pattern. Use Decimal arithmetic, explicit "
                    "currency codes, contract-specific rounding, and documented "
                    "exchange-rate conventions. The royalty contractor owns "
                    "the calculation specification; the engineer implements "
                    "it; the operator approves commercial exceptions. Keep "
                    "every override attributable and reversible without deleting "
                    "the original statement or its calculation inputs."
                ),
                (
                    "Reconcile three layers: the licensee's operational ledger, "
                    "the contractual royalty base, and the desk's recognized "
                    "revenue. Obtain only the records authorized by reporting "
                    "and audit provisions, using customer-approved exports "
                    "rather than assuming access to storefront or accounting "
                    "systems. Shopify order exports, Stripe balance and "
                    "transaction reports, and QuickBooks Online ledger extracts "
                    "can support different reconciliation tasks, but payment "
                    "settlements are not automatically the royalty base. "
                    "Taxes, shipping, refunds, bundles, intercompany transfers, "
                    "foreign exchange, and channel timing require the actual "
                    "contract definition. Match sampled transactions to SKU "
                    "mappings and permitted territories, then trace totals "
                    "to the submitted statement. For catalog licenses, test "
                    "the reported media and exploitation period; for datasets, "
                    "test delivery versions, authorized seats, and any "
                    "contractually measurable usage. Investigate underreporting "
                    "through documented exceptions and the agreed audit "
                    "process, not covert access to licensee systems. Preserve "
                    "the contractual notice period and record-retention window "
                    "so a valid discrepancy does not become an unusable "
                    "claim through delay. Where terms affect exclusivity, "
                    "territorial allocation, tying, or competitor coordination, "
                    "review the actual arrangement against applicable competition "
                    "rules, including 15 U.S.C. 1. Ownership of an asset "
                    "does not remove the need to evaluate the surrounding "
                    "commercial restrictions."
                ),
                (
                    "Keep the chapter's economics anchored to Candidate #19. "
                    "Conservative recognized revenue is $50,000 at a twenty-five "
                    "percent net margin, producing $12,500 annual owner net "
                    "profit and $37,500 of total implied costs. Base revenue "
                    "is $425,000 at forty-two and one-half percent, producing "
                    "$180,625 profit and $244,375 of implied costs. Scaled "
                    "revenue is $800,000 at sixty percent, producing $480,000 "
                    "profit and $320,000 of implied costs. These are the "
                    "three canonical cases, not outputs of the illustrative "
                    "brand agreement above. Conservative and Base retain "
                    "one full-time operator plus three contractors; Scaled "
                    "uses two full-time operators plus four contractors. "
                    "Startup capital of $12,000 to $75,000 and monthly "
                    "operating outlays of $2,000 to $12,000 describe planning "
                    "ranges, not a complete reconciliation of every annual "
                    "scenario cost. Do not force those ranges to replace "
                    "the implied total expense figures. With six to "
                    "twenty-four months to a first deal, buy expensive "
                    "commercial coverage only when qualified opportunities "
                    "justify it. Review connector maintenance hours, "
                    "enrichment spend, statement rework, and rights-exception "
                    "backlog monthly. Add capacity when verified obligations "
                    "and deal throughput demand it, rather than treating "
                    "automation as a reason to multiply unqualified targets "
                    "or subscribe to every available database."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Contract-Level Reconciliation Controls",
                "headers": [
                    "Case or control being evaluated",
                    "Recognized revenue or contractual calculation",
                    "Profit, cost, or evidence reconciliation",
                    "Staffing and specific operator response",
                ],
                "rows": [
                    [
                        "Conservative canonical case for Candidate #19 intellectual property licensing",
                        "Annual recognized license fees and royalties total exactly $50,000",
                        "At 25% margin, owner profit is $12,500 and implied costs are $37,500",
                        "Use 1 FT + 3 C and prioritize free evidence sources",
                    ],
                    [
                        "Base canonical case for Candidate #19 intellectual property licensing",
                        "Annual recognized license fees and royalties total exactly $425,000",
                        "At 42.5% margin, owner profit is $180,625 and implied costs are $244,375",
                        "Use 1 FT + 3 C with targeted commercial data subscriptions",
                    ],
                    [
                        "Scaled canonical case for Candidate #19 intellectual property licensing",
                        "Annual recognized license fees and royalties total exactly $800,000",
                        "At 60% margin, owner profit is $480,000 and implied costs are $320,000",
                        "Use 2 FT + 4 C with separated review and production duties",
                    ],
                    [
                        "Illustrative brand royalty calculation remains separate from canonical scenario totals",
                        "Five percent of $2,000,000 eligible sales produces $100,000 earned royalties",
                        "A $60,000 paid recoupable guarantee leaves $40,000 due for that period",
                        "Royalty contractor separates earned royalties, guarantee credits, invoices, and cash receipts",
                    ],
                    [
                        "Licensee transaction testing verifies contractual deductions and covered commercial activity",
                        "Recalculate the royalty base from authorized exports using the signed definition",
                        "Trace refunds, taxes, bundles, territory mappings, and exchange-rate adjustments individually",
                        "Engineering contractor supplies reproducible tests while the royalty contractor resolves exceptions",
                    ],
                    [
                        "Renewal and audit tracking protect actionable contractual rights over time",
                        "Store notice deadlines, reporting due dates, guarantee periods, and audit windows",
                        "Link each alert to signed clauses and the relevant evidence snapshot",
                        "Full-time operator assigns action owners and documents timely counterparty communications",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four conditions before activating a licensing workflow",
                "body": (
                    "The desk should be able to demonstrate rights scope, "
                    "permitted data access, calculation integrity, and operational ownership."
                ),
                "items": [
                    "Verify the contracting entity's title chain, relevant territory, permitted uses, sublicensing authority, and any conflicting exclusive grant.",
                    "Verify each connector's authorized access method, current account entitlement, retention permissions, request limits, and working fallback.",
                    "Verify a sample royalty statement against signed definitions, guarantee credits, authorized deductions, and the separation of licensee sales from operator revenue.",
                    "Verify renewal notices, reporting deadlines, audit windows, and quality-control duties have named owners within the stated staffing case.",
                ],
            },
        },
    ],
    "pull_quote": "A licensing desk's information edge is the shortest auditable path from a public clue to a payable contractual right.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create four evidence-packet templates for patent, brand, catalog, and dataset licensing, each with asset identifiers and a precise proposed grant.",
        "Register the eighteen directory sources with current access documentation, cost category, observed latency, configured quotas, and a tested fallback.",
        "Implement the public-records-first enrichment waterfall and cap commercial API spend per qualified rights packet.",
        "Build a versioned evidence store with document digests, separate source and retrieval timestamps, and explicit ownership assertions.",
        "Test one authorized royalty statement end to end, including deductions, currency, minimum-guarantee credits, duplicate imports, and recognized revenue separation.",
        "Assign renewal, audit, reporting, and connector exceptions across the 1 FT + 3 C pod, expanding only to the canonical 2 FT + 4 C Scaled structure when justified.",
    ],
    "statutory_citations": [
        {
            "title": "35 U.S.C. 261 — Ownership; assignment",
            "url": "https://www.law.cornell.edu/uscode/text/35/261",
            "relevance": "Supports written patent-assignment evidence and analysis of recordation timing against later purchasers or mortgagees.",
        },
        {
            "title": "37 CFR 3.54 — Effect of recording",
            "url": "https://www.ecfr.gov/current/title-37/chapter-I/subchapter-A/part-3/section-3.54",
            "relevance": "Establishes that USPTO recordation does not determine an instrument's validity or its effect on title.",
        },
        {
            "title": "15 U.S.C. 1060 — Assignment of marks",
            "url": "https://www.law.cornell.edu/uscode/text/15/1060",
            "relevance": "Informs trademark-transfer review, including the associated goodwill and the restrictions applicable to certain applications.",
        },
        {
            "title": "15 U.S.C. 1055 — Use by related companies",
            "url": "https://www.law.cornell.edu/uscode/text/15/1055",
            "relevance": "Provides statutory context for controlled related-company use when designing a brand-license quality-control process.",
        },
        {
            "title": "17 U.S.C. 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": "Supports obtaining signed transfer instruments rather than treating catalog identifiers or public entries as sufficient title evidence.",
        },
        {
            "title": "17 U.S.C. 205 — Recordation of transfers and other documents",
            "url": "https://www.law.cornell.edu/uscode/text/17/205",
            "relevance": "Frames copyright recordation review and the conditions affecting constructive notice and priority between conflicting transfers.",
        },
        {
            "title": "17 U.S.C. 102 — Subject matter of copyright",
            "url": "https://www.law.cornell.edu/uscode/text/17/102",
            "relevance": "Requires precision about protected expression and the exclusion of ideas, procedures, systems, and methods when describing dataset rights.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Supports concrete commercial-email controls for sender identification, truthful routing, postal addresses, and opt-out handling.",
        },
        {
            "title": "15 U.S.C. 1 — Trusts and related restraints of trade",
            "url": "https://www.law.cornell.edu/uscode/text/15/1",
            "relevance": "Provides a primary competition-law reference when evaluating licensing restrictions and coordination between competitors.",
        },
    ],
}
