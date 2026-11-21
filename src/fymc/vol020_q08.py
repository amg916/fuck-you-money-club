from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small government contract brokering desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "SAM.gov, USAspending, Municipal Bid Portals, Entity Verification, and FAR-Aware Evidence Pipelines for a Five-Person Procurement Desk",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #4, Government Contract Brokering, holds Rank #20 with a "
        "70/100 Money-to-Manpower Score: a Disciplined Specialist Play. Its edge "
        "comes from verified procurement evidence, not a larger contact list. "
        "This chapter maps seven operator plays: solicitation discovery, award "
        "intelligence, prime qualification, supplier discovery, lawful teaming, "
        "bid control, and post-award monitoring. Eighteen named resources feed "
        "a traceable pipeline operated by two full-time staff and three "
        "contractors. Recognized service fees produce annual owner profit of "
        "$18,000 Conservative, $126,000 Base, and $300,000 Scaled; client award "
        "values never become desk revenue. Use authoritative records first, "
        "commercial enrichment second, and documented human verification before "
        "any eligibility, deadline, pricing, or teaming decision."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual recognized service fees, excluding client contract values",
            "note": "15% net margin; $18,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$560,000",
            "context": "Annual recognized service fees, excluding client contract values",
            "note": "22.5% net margin; $126,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual recognized service fees, excluding client contract values",
            "note": "30% net margin; $300,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an authoritative source directory around seven billable plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Give Candidate #4 seven explicit operating lanes before buying "
                    "subscriptions: P1 solicitation discovery, P2 award intelligence, "
                    "P3 prime qualification, P4 supplier discovery, P5 lawful teaming, "
                    "P6 bid control, and P7 post-award monitoring. These are this "
                    "chapter's operational mapping, not seven separate revenue "
                    "forecasts. P1 finds actionable notices; P2 identifies buying "
                    "patterns; P3 checks whether a proposed prime can actually "
                    "perform; P4 develops supplier alternatives; P5 documents a "
                    "permitted relationship; P6 controls submissions; P7 tracks "
                    "delivery and payment dependencies. Assign the first full-time "
                    "employee to capture and client decisions and the second to "
                    "data operations and bid calendars. Use three scoped contractors "
                    "for procurement review, supplier diligence, and proposal or "
                    "delivery support. Contractor count does not imply five full-time "
                    "salaries. Record hours, turnaround commitments, and coverage "
                    "explicitly. Every source must serve a lane, produce a named "
                    "artifact, and have an escalation owner. A notice without a "
                    "responsible reviewer is merely inventory. An award record "
                    "without transaction interpretation is potentially misleading. "
                    "A vendor profile without entity verification is a lead, not "
                    "a qualified partner. Start with two agency families and one "
                    "municipality so the five-person pod can inspect evidence "
                    "rather than spend its week maintaining connectors."
                ),
                (
                    "Use the directory below as a source register, not as a promise "
                    "of universal API access. Cost entries distinguish free public "
                    "records from separately priced delivery, analytics, and account "
                    "features. Refresh entries describe desk retrieval targets or "
                    "publication dependence, not provider service commitments. Check "
                    "current documentation and account entitlements when configuring "
                    "each connector; numeric quotas and commercial prices can change. "
                    "SAM.gov opportunity records support discovery, while the issuing "
                    "office's solicitation documents and amendments establish the "
                    "working requirements. USAspending supports spending analysis, "
                    "but obligations, outlays, ceilings, and modifications answer "
                    "different questions. Municipal notices often point into another "
                    "portal for attachments, registration, or submission. Preserve "
                    "that chain instead of treating the first search result as the "
                    "complete procurement. A published notice may arrive after a "
                    "portal update, and a vendor email may arrive after both. Store "
                    "publication time, retrieval time, and the source's own update "
                    "field separately. Never manufacture a source timestamp when "
                    "only retrieval time exists. For an active pursuit, subscribe "
                    "to official notifications and inspect the issuing portal on "
                    "the bid calendar's schedule. The directory's fallback is an "
                    "alternate retrieval route, not authority to override newer "
                    "instructions or extend a deadline."
                ),
                (
                    "Federal and municipal evidence require different identifiers. "
                    "Carry the federal notice identifier, solicitation number, "
                    "agency hierarchy, office, NAICS, product or service code, and "
                    "place of performance as distinct fields. Link awards using "
                    "the award identifier plus awarding agency and relevant parent "
                    "award identifiers; a short award number alone can collide. "
                    "For entities, preserve UEI, CAGE when applicable, legal name, "
                    "address, and registration status without assuming every "
                    "municipal supplier has federal identifiers. Keep municipal "
                    "vendor and solicitation identifiers in their own namespaces. "
                    "Use Census NAICS definitions for classification interpretation, "
                    "but do not replace the solicitation's assigned code with a "
                    "classifier's preferred label. P2 research can combine "
                    "USAspending transactions with source award notices to identify "
                    "repeat buyers and incumbent concentration. It cannot establish "
                    "an incumbent's actual profit or the government's next buying "
                    "decision. P3 and P4 can combine SAM registration, exclusions, "
                    "SBA profiles, and supplier documents, but each proves a "
                    "different proposition. A registry entry does not establish "
                    "available capacity. A certification claim needs program-specific "
                    "verification. Record the question each source answers so "
                    "analysts stop turning one credible fact into several "
                    "unsupported conclusions during qualification meetings and "
                    "client-facing opportunity reviews."
                ),
            ],
            "table": {
                "caption": "Eighteen named sources: access, cost, freshness, request discipline, and fallback",
                "headers": [
                    "Named source and mapped plays",
                    "Exact access route and method",
                    "Cost tier and commercial boundary",
                    "Refresh and latency treatment",
                    "Rate-limit and access hygiene",
                    "Fallback and evidence limitation",
                ],
                "rows": [
                    [
                        "SAM.gov Opportunities API supports P1 discovery and P6 amendment tracking",
                        "Use https://api.sam.gov/opportunities/v2/search with a SAM API key and documented filters",
                        "Public API access is free; account-specific permissions govern available usage",
                        "Retrieve daily discovery windows; separately inspect active pursuits before submissions",
                        "Respect account quotas, paginate documented windows, and back off on throttling",
                        "Use https://sam.gov/opportunities and issuing-office attachments when API coverage differs",
                    ],
                    [
                        "SAM.gov Entity Information API supports P3 registration and P4 identity checks",
                        "Follow https://open.gsa.gov/api/entity-api/ for current endpoints, keys, and permitted fields",
                        "Public registration checks are free; restricted fields require separate authorization",
                        "Refresh before qualification decisions; retain registration dates and retrieval timestamps",
                        "Request only permitted fields and cache by UEI within account limits",
                        "Use SAM.gov entity search and obtain dated registration evidence from suppliers",
                    ],
                    [
                        "SAM.gov Exclusions search supports P3, P4, and P5 eligibility investigation",
                        "Open https://sam.gov and select Exclusions search for official record review",
                        "Public search is free; analyst identity resolution remains an operating expense",
                        "Recheck before recommendations and commitments; preserve matching record effective dates",
                        "Use supported search or documented exports; avoid repeated automated interface scraping",
                        "Investigate aliases and identifiers through official records rather than name-only matches",
                    ],
                    [
                        "USAspending API supports P2 incumbent analysis and P7 award-change monitoring",
                        "Use documented POST searches at https://api.usaspending.gov/api/v2/search/spending_by_award/",
                        "Public API and downloadable spending datasets are available without subscription charges",
                        "Refresh research weekly; agency reporting and corrections create variable publication lag",
                        "Page bounded searches, cache responses, and retry transient failures with jitter",
                        "Use https://www.usaspending.gov downloads and reconcile material findings against award documents",
                    ],
                    [
                        "SAM.gov Contract Data supports P2 award research and P7 modification checks",
                        "Navigate https://sam.gov Contract Data search and reports using current account requirements",
                        "Public data access is free; report features may require signed-in access",
                        "Review material pursuits weekly; publication timing follows reporting and system processing",
                        "Prefer supported reports and exports rather than automating interactive report sessions",
                        "Cross-check USAspending transactions and contracting-office documents before interpreting award totals",
                    ],
                    [
                        "SBA Small Business Search supports P3 certifications and P4 supplier discovery",
                        "Follow current supplier-search links from https://www.sba.gov/federal-contracting to official search tools",
                        "Public supplier discovery is free; paid directories are unnecessary for baseline checks",
                        "Refresh during qualification; profile claims and program status have different update cycles",
                        "Use supported search features and avoid assuming bulk extraction is permitted",
                        "Request current program evidence and check the relevant SBA certification source",
                    ],
                    [
                        "SBA SUBNet supports P4 subcontract searches and P5 teaming lead development",
                        "Access https://subnet.sba.gov/ and inspect posted subcontracting opportunities and instructions",
                        "Public opportunity browsing is free; participating primes control their own procurement processes",
                        "Review twice weekly; posting volume and timeliness depend on participating organizations",
                        "Use available searches and alerts without aggressive polling of listing pages",
                        "Visit the prime contractor's supplier portal and verify the opportunity contact",
                    ],
                    [
                        "Census NAICS reference supports P1 filters and P3 industry-code interpretation",
                        "Search official code definitions and crosswalks at https://www.census.gov/naics/",
                        "Published classification references are free; analyst interpretation requires solicitation-specific review",
                        "Update when classification editions change; retain the edition used for analysis",
                        "Download reference files once and reuse locally instead of repeated page requests",
                        "Compare the solicitation code with applicable SBA size standards and amendments",
                    ],
                    [
                        "Acquisition.gov FAR supports P5 teaming review and P6 clause extraction",
                        "Read official FAR parts and clause text at https://www.acquisition.gov/browse/index/far",
                        "Official regulation access is free; specialist interpretation is separately scoped work",
                        "Check current text during review and preserve solicitation-incorporated clause edition dates",
                        "Cache retrieved references and avoid broad crawling unrelated to active requirements",
                        "Use eCFR Title 48 and the solicitation's incorporated clauses for reconciliation",
                    ],
                    [
                        "eCFR API supports P5 rule research and P6 dated regulatory evidence",
                        "Use https://www.ecfr.gov/developers/documentation/api/v1 for documented version and content requests",
                        "Public regulatory text and documented API access require no commercial subscription",
                        "Inspect available version dates; current text can differ from incorporated editions",
                        "Cache versioned responses and retry throttled requests with bounded exponential delays",
                        "Use Acquisition.gov for FAR presentation and GovInfo for official historical publications",
                    ],
                    [
                        "GovInfo API supports P5 historical authority research and P6 publication checks",
                        "Use https://api.govinfo.gov/docs/ and obtain the required government API key",
                        "Public publications are free; API access follows documented key usage conditions",
                        "Refresh when relevant publications appear; publication availability determines evidence latency",
                        "Honor documented key limits and use collections metadata before fetching full packages",
                        "Download publications directly from https://www.govinfo.gov and preserve package identifiers",
                    ],
                    [
                        "NYC City Record Online supports P1 municipal notices and P2 award notices",
                        "Search procurement notices through https://a856-cityrecord.nyc.gov/ using agency and date filters",
                        "Public notice search is free; procurement participation can require separate registrations",
                        "Inspect each business day; publication timing differs from underlying procurement updates",
                        "Use offered searches and exports without bypassing interface controls or session restrictions",
                        "Follow the issuing agency and PASSPort references for operative documents and deadlines",
                    ],
                    [
                        "NYC PASSPort supports P1 opportunity review and P6 municipal submission control",
                        "Start at https://www.nyc.gov/passport and follow official public or vendor access links",
                        "Public information is free; vendor workflows require appropriate account setup and permissions",
                        "Check active pursuits daily and again before submitting through the designated workflow",
                        "Use authorized accounts and native notifications; never share credentials across clients",
                        "Use City Record notices and agency procurement contacts to resolve access problems",
                    ],
                    [
                        "NYC Open Data supports P2 municipal analysis and P7 public-record reconciliation",
                        "Select datasets at https://data.cityofnewyork.us/ and use their documented Socrata API endpoints",
                        "Public dataset access is free; application tokens can affect permitted request handling",
                        "Read each dataset's update metadata because refresh schedules vary by publishing agency",
                        "Use selective queries, bounded pages, application tokens where appropriate, and cached extracts",
                        "Download the same dataset as CSV and reconcile against agency procurement records",
                    ],
                    [
                        "OpenGov Procurement supports P1 municipal discovery and P6 portal-specific bid tracking",
                        "Search participating agency portals through https://procurement.opengov.com/ and follow vendor instructions",
                        "Public browsing is commonly free; verify current vendor features and account charges",
                        "Use native notifications and inspect active project pages before every submission decision",
                        "Prefer authorized exports and notifications; do not assume a public extraction API",
                        "Check the issuing agency website and obtain clarification through its designated channel",
                    ],
                    [
                        "Bonfire supports P1 public opportunities and P6 agency-specific electronic submissions",
                        "Enter the agency's linked Bonfire portal and follow its project registration instructions",
                        "Basic participation and optional discovery products have different terms; confirm current pricing",
                        "Treat project updates as event-driven and inspect attachments before final package preparation",
                        "Use native alerts and authorized downloads without bypassing authenticated portal controls",
                        "Return to the agency procurement page and designated contact for missing documents",
                    ],
                    [
                        "GovTribe supports P2 research acceleration and P4 federal supplier relationship discovery",
                        "Use https://govtribe.com/ under a purchased account; confirm export or API entitlements",
                        "Commercial subscription pricing requires a current quote and documented feature-level comparison",
                        "Treat aggregation latency as vendor-dependent; verify consequential findings against official records",
                        "Stay within licensed seats, export allowances, and any separately contracted API limits",
                        "Rebuild essential findings from SAM.gov, USAspending, and the underlying procurement documents",
                    ],
                    [
                        "OpenCorporates supports P3 legal-entity resolution and P4 supplier identity enrichment",
                        "Consult https://api.opencorporates.com/documentation/API-Reference and use an authorized API token",
                        "Commercial use and API capacity depend on licensing; obtain current written terms",
                        "Registry ingestion timing varies; retain jurisdiction, company number, and underlying source date",
                        "Cache permitted results, respect contracted request limits, and minimize personal-data collection",
                        "Verify legal status directly with the relevant state business registry and supplier",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that outperform a larger subscription stack",
                "body": (
                    "The desk wins through evidence timing, identifier discipline, "
                    "and selective attention rather than indiscriminate collection."
                ),
                "items": [
                    "For P1 and P6, preserve attachment hashes alongside notice identifiers; a replaced attachment deserves review even when the title remains identical.",
                    "For P2, inspect award modifications before describing an incumbent's contract size; cumulative ceilings and individual obligations are different measures.",
                    "For P3 and P4, match UEI or jurisdiction-specific company identifiers before names; similarly named suppliers can have unrelated eligibility and delivery records.",
                    "For P5, keep a written workshare model before introducing a prime and subcontractor; enthusiastic introductions cannot repair a prohibited performance structure.",
                ],
            },
        },
        {
            "heading": "2. Run an evidence-first enrichment waterfall with reversible joins",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement the enrichment waterfall as a sequence of questions, "
                    "not a sequence of vendors. First retrieve the authoritative "
                    "notice and its attachments. Second resolve the issuing office, "
                    "deadline, submission channel, set-aside designation, and required "
                    "qualifications. Third identify likely suppliers from existing "
                    "client records, official registrations, and program directories. "
                    "Fourth enrich unresolved corporate relationships through a "
                    "licensed commercial source. Fifth ask the supplier for evidence "
                    "that public records cannot establish: current production "
                    "capacity, insurance, delivery commitments, pricing validity, and "
                    "available personnel. Stop enrichment when the next field cannot "
                    "change a pursuit decision. The data operator owns collection, "
                    "the capture lead owns interpretation, and the relevant "
                    "contractor reviews exceptions within a defined service window. "
                    "Keep the original value, normalized value, source locator, "
                    "retrieval timestamp, and matching rationale for every material "
                    "field. Label deterministic identifier matches separately from "
                    "name-and-address candidates. Never merge two entities solely "
                    "because a commercial database assigns a shared domain. Parent "
                    "companies, operating subsidiaries, and joint ventures can carry "
                    "different registrations and obligations. Make merges reversible "
                    "with an explicit linkage record rather than overwriting source "
                    "rows. This lets P3 qualification and P4 discovery share data "
                    "without turning uncertain research into an asserted legal identity."
                ),
                (
                    "A small stdlib-based pipeline can begin with urllib.request "
                    "for permitted HTTP requests, json for payloads, sqlite3 for "
                    "structured records, hashlib for attachment fingerprints, and "
                    "logging for execution events. Keep downloaded evidence outside "
                    "the database and store its content hash, byte length, media "
                    "type, and authorized storage reference. Save retrieval "
                    "parameters without API secrets. Use an append-only raw layer, "
                    "a normalized layer, and a decision layer containing human "
                    "assessments. Fetch overlapping update windows because late "
                    "publication and corrected records can defeat a simple "
                    "last-seen timestamp. Deduplicate using source-specific keys and "
                    "content versions, not titles. Advance a retrieval checkpoint "
                    "only after every page in that window has been stored and "
                    "validated. Retry network failures and appropriate server errors "
                    "with bounded exponential backoff and jitter; honor Retry-After "
                    "when supplied. Authentication errors require credential or "
                    "permission review, not repeated retries. Reject unexpected "
                    "HTML login pages masquerading as successful downloads. Store "
                    "provider quotas as connector configuration instead of assuming "
                    "one universal request budget. Keep the scheduler modest enough "
                    "that the second full-time employee can understand every failed "
                    "job and restore essential bid-calendar coverage manually during "
                    "an outage without depending on an unavailable specialist."
                ),
                (
                    "Treat dates, money, and amendments as separate normalization "
                    "problems. Preserve the deadline exactly as published, its "
                    "stated timezone, and an explicitly verified UTC conversion. "
                    "Python 3.9 zoneinfo can handle named zones when timezone data "
                    "is available; never silently substitute the workstation's "
                    "local zone. Escalate ambiguous abbreviations to the issuing "
                    "office through the permitted question channel. Store monetary "
                    "values using decimal.Decimal during transformation and exact "
                    "decimal text or integer minor units in SQLite. Keep award "
                    "ceilings, obligations, deobligations, and desk service fees in "
                    "different fields. Version solicitation attachments independently "
                    "from notice metadata because either can change alone. For P6, "
                    "an amendment event must create a review task, identify "
                    "affected requirements, and record whether acknowledgment is "
                    "required. For P7, supplier milestones and invoice events "
                    "should come from the authorized client's records, with public "
                    "award data serving as context rather than a receivables ledger. "
                    "Restrict client files by project and avoid copying sensitive "
                    "proposal content into broad research indexes. Public access "
                    "does not eliminate purpose limitations or contractual "
                    "restrictions. Retain the smallest useful contact dataset, "
                    "prefer role-based procurement contacts, and document deletion "
                    "rules for expired research copies while preserving required "
                    "bid evidence under the client engagement's retention schedule."
                ),
            ],
            "table": {
                "caption": "Six waterfall stages with explicit stopping rules and accountable outputs",
                "headers": [
                    "Waterfall stage and operating lane",
                    "Required evidence and transformation",
                    "Stop condition or escalation trigger",
                    "Owner and retained decision artifact",
                ],
                "rows": [
                    [
                        "Authoritative notice retrieval starts P1 discovery and P6 bid control",
                        "Capture notice identifiers, attachments, publication fields, retrieval time, and hashes",
                        "Stop candidate promotion when required attachments or submission instructions remain inaccessible",
                        "Data operator retains source packet and assigns unresolved access to capture lead",
                    ],
                    [
                        "Requirement extraction connects P1 discovery with P3 prime qualification decisions",
                        "Extract deadline, location, scope, qualifications, set-aside language, and incorporated clauses",
                        "Escalate conflicting dates or eligibility language through the designated question channel",
                        "Capture lead signs the requirement matrix and records the controlling amendment",
                    ],
                    [
                        "Identifier resolution connects P3 prime checks with P4 supplier discovery",
                        "Match legal identifiers first and preserve weaker name-address matches as candidates",
                        "Stop automatic merging when jurisdictions, entity numbers, or legal names conflict",
                        "Diligence contractor retains match rationale and requests supplier confirmation when necessary",
                    ],
                    [
                        "Commercial enrichment accelerates P2 research and unresolved P4 supplier questions",
                        "Retrieve only licensed fields needed to resolve a specific pursuit decision",
                        "Stop spending when additional enrichment cannot change qualification or supplier selection",
                        "Data operator records subscription cost, source lineage, and authoritative verification status",
                    ],
                    [
                        "Supplier verification supports P4 alternatives and P5 workable teaming structures",
                        "Obtain dated capacity evidence, quotation validity, workshare assumptions, and delivery commitments",
                        "Escalate unsupported capacity claims or structures inconsistent with solicitation performance requirements",
                        "Supplier contractor prepares evidence packet for capture lead and procurement reviewer",
                    ],
                    [
                        "Decision publication connects P6 bid execution with P7 post-award monitoring",
                        "Publish reviewed changes to client-specific calendars, requirement matrices, and milestone registers",
                        "Stop publication of unresolved eligibility conclusions or ambiguous operative submission deadlines",
                        "Capture lead records disposition while data operator preserves the complete evidence chain",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture a bounded evidence window",
                    "action": "Retrieve configured sources and preserve raw responses before transformation.",
                    "detail": (
                        "Record source, query, retrieval time, pagination position, "
                        "response status, and content hashes; exclude credentials "
                        "from logs and exported evidence."
                    ),
                },
                {
                    "step": 2,
                    "title": "Normalize without erasing source meaning",
                    "action": "Resolve identifiers and extract deadlines, classifications, amounts, and attachment versions.",
                    "detail": (
                        "Keep original values beside normalized values; quarantine "
                        "ambiguous identity matches, deadline conversions, and "
                        "unrecognized payload shapes for review."
                    ),
                },
                {
                    "step": 3,
                    "title": "Review changed decision fields",
                    "action": "Route material changes to the capture lead and the appropriate scoped contractor.",
                    "detail": (
                        "Prioritize deadline, scope, eligibility, workshare, "
                        "quotation-expiry, and acknowledgment changes; record "
                        "reviewer, evidence reference, and disposition."
                    ),
                },
                {
                    "step": 4,
                    "title": "Publish and reconcile the desk queue",
                    "action": "Update authorized client calendars and confirm the retrieval window completed.",
                    "detail": (
                        "Advance checkpoints only after complete storage and "
                        "validation; reconcile unresolved tasks against upcoming "
                        "deadlines and retain a manual source-check fallback."
                    ),
                },
            ],
        },
        {
            "heading": "3. Diagnose silent failures before they become missed bids or bad structures",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Measure source health separately from business activity. A job "
                    "that returns HTTP 200 can still retrieve a login page, an "
                    "empty result caused by a changed filter, or only the first "
                    "page of a large response. Maintain connector tests for "
                    "expected media type, required keys, date parsing, page "
                    "coverage, and attachment accessibility. Compare counts with "
                    "recent comparable windows, but investigate deviations rather "
                    "than declaring every quiet holiday an outage. Use a small "
                    "fixture set containing known amendments, multiple pages, "
                    "duplicate notices, negative award adjustments, and missing "
                    "optional fields. Python unittest can exercise these cases "
                    "without making live requests. urllib.error distinguishes "
                    "HTTP and network failures; json identifies malformed payloads; "
                    "sqlite3 queries expose duplicate identifiers and orphaned "
                    "attachments. Optional workstation tools such as curl and jq "
                    "accelerate diagnosis but are not dependencies of the stdlib "
                    "pipeline. Never paste API keys, client proposal material, or "
                    "restricted attachments into public debugging services. Save "
                    "redacted request metadata so another authorized operator can "
                    "reproduce a failure. The useful incident report states which "
                    "sources and pursuit windows were affected, which manual "
                    "checks replaced automation, and whether any client deadline "
                    "or requirement decision remained unverified after recovery."
                ),
                (
                    "Apply procurement rules to the proposed service and "
                    "relationship, not merely to the data source. FAR Subpart 3.4 "
                    "and FAR 52.203-5 address contingent-fee arrangements, with "
                    "defined exceptions that require factual review; calling a "
                    "payment a consulting fee does not settle its treatment. "
                    "41 U.S.C. 2102 restricts disclosure and obtaining of covered "
                    "bid, proposal, and source-selection information before award. "
                    "A person offering an internal evaluation spreadsheet is not "
                    "providing ordinary public-record enrichment. Under 41 U.S.C. "
                    "8702, kickbacks connected to covered prime contracts and "
                    "subcontracts are prohibited. Structure P5 introductions and "
                    "supplier payments accordingly, with a documented service "
                    "scope and no hidden compensation for favorable treatment. "
                    "FAR 52.215-23, where included, addresses excessive pass-through "
                    "charges; 13 CFR 125.6 establishes limitations on subcontracting "
                    "for covered set-aside arrangements. Evaluate applicable "
                    "exceptions, contract type, similarly situated entities, "
                    "performance period, and solicitation clauses rather than "
                    "applying a universal percentage to every procurement. "
                    "Municipal transactions require their own local rules and "
                    "solicitation terms. The procurement-review contractor "
                    "documents these determinations, while the capture lead "
                    "ensures that the supplier list, workshare model, and fee "
                    "agreement reflect the same facts before a recommendation "
                    "reaches the client."
                ),
                (
                    "Use adversarial operational tests against your own workflow "
                    "without probing agency systems beyond authorized access. "
                    "Change a stored deadline in a test fixture and confirm "
                    "that the calendar receives a review task rather than an "
                    "unreviewed overwrite. Replace an attachment with different "
                    "bytes under the same filename and confirm the hash "
                    "comparison raises an amendment investigation. Introduce two "
                    "suppliers with similar names and different UEIs, then "
                    "confirm that enrichment keeps them separate. Simulate "
                    "throttling, expired credentials, an incomplete final page, "
                    "and a timezone conversion failure. In each case, the "
                    "pipeline should retain the last verified record, mark "
                    "freshness accurately, and identify the person responsible "
                    "for manual coverage. Do not label stale records current "
                    "because the scheduler ran successfully. Give P6 deadlines "
                    "higher operational priority than P2 historical research "
                    "when capacity is constrained. For P7, simulate a supplier "
                    "milestone slipping while the public award record stays "
                    "unchanged; the client-facing exception must still appear. "
                    "Review incidents weekly with both full-time employees "
                    "and only the contractor needed for the issue. Close "
                    "an incident after a reproducible test passes, affected "
                    "pursuits are reconciled, and the revised procedure has "
                    "a clear owner rather than after an error message disappears."
                ),
            ],
            "table": {
                "caption": "Six forensic checks that expose technically successful but operationally wrong pipelines",
                "headers": [
                    "Diagnostic tool and failure pattern",
                    "Concrete test and evidence captured",
                    "Interpretation and immediate operator response",
                    "Lane owner and recovery completion evidence",
                ],
                "rows": [
                    [
                        "curl response inspection identifies successful requests returning authentication pages",
                        "Inspect status, content type, redirect chain, and redacted response body",
                        "Suspend parsing when HTML replaces expected JSON and review authorized access",
                        "Data operator restores P1 retrieval and reconciles missed source windows",
                    ],
                    [
                        "Python json and unittest expose payload drift and missing required fields",
                        "Run stored fixtures against field validation and explicit optional-field handling",
                        "Quarantine changed payloads instead of silently publishing empty deadlines or identities",
                        "Data operator releases corrected P1 and P3 records after fixture tests pass",
                    ],
                    [
                        "SQLite reconciliation queries detect partial pagination and repeated award transactions",
                        "Compare stored source keys, page manifests, transaction identifiers, and checkpoint boundaries",
                        "Replay incomplete windows and separate legitimate modifications from accidental duplicate ingestion",
                        "Data operator verifies P2 totals against preserved authoritative transaction records",
                    ],
                    [
                        "hashlib and difflib reveal replaced attachments and changed operative requirements",
                        "Compare byte fingerprints, extracted text versions, filenames, and source retrieval times",
                        "Route material changes for P6 review without treating every formatting change equally",
                        "Capture lead records amendment disposition and any required client acknowledgment action",
                    ],
                    [
                        "datetime and zoneinfo tests expose ambiguous deadlines and daylight-saving conversion mistakes",
                        "Test published local times against verified named zones and stored UTC results",
                        "Escalate ambiguous source language rather than borrowing the workstation timezone",
                        "Capture lead confirms P6 calendar entries against controlling solicitation instructions",
                    ],
                    [
                        "SQLite incident queries expose stale supplier milestones hidden by unchanged awards",
                        "Compare client-authorized milestone dates, supplier updates, and unresolved delivery exceptions",
                        "Escalate delivery risk even when public award records show no modification",
                        "Delivery contractor resolves P7 exceptions with documented supplier and client evidence",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before publishing a pursuit recommendation",
                "body": (
                    "A passed technical job is insufficient. The capture lead "
                    "records these four checks against the specific pursuit."
                ),
                "items": [
                    "Verify the current solicitation packet, every located amendment, the operative deadline and timezone, and the designated submission channel directly against the issuing source.",
                    "Verify the proposed prime's identity, relevant registration and certification evidence, and exclusions findings; investigate potential matches instead of inferring eligibility from a name search.",
                    "Verify fee terms, supplier compensation, required workshare, and subcontracting structure against applicable clauses and program rules with the procurement-review contractor.",
                    "Verify complete retrieval coverage, acknowledged material changes, supplier quotation validity, and a named backup operator before the recommendation enters the client queue.",
                ],
            },
        },
        {
            "heading": "4. Fund the tooling from service economics and protect five-person capacity",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep Candidate #4's scorecard intact when justifying the "
                    "stack. Conservative recognized service revenue is $120,000, "
                    "with a 15% net margin and $18,000 annual owner net "
                    "profit; implied total annual costs are $102,000. Base "
                    "revenue is $560,000, with a 22.5% net margin and "
                    "$126,000 owner profit; implied costs are $434,000. "
                    "Scaled revenue is $1,000,000, with a 30% net margin "
                    "and $300,000 owner profit; implied costs are $700,000. "
                    "Conservative and Base use two full-time employees plus "
                    "three contractors. Scaled uses three full-time employees "
                    "plus four contractors, seven people total. Those are "
                    "canonical cases, not outputs of this chapter's connector "
                    "design. Client contract ceilings, obligations, subcontract "
                    "values, and supplier invoices never become desk revenue "
                    "merely because the pipeline tracks them. Recognize only "
                    "the desk's earned service fees under its actual "
                    "engagement terms. The supplied monthly operating-expense "
                    "range of $5,000 to $25,000 is a planning range, "
                    "not a substitute for each case's complete annual cost "
                    "bridge. Separate recurring overhead, direct delivery "
                    "labor, variable contractor costs, and other expenses "
                    "so the scorecard's margins reconcile without double "
                    "counting or pretending that every cost belongs in "
                    "one monthly overhead bucket."
                ),
                (
                    "Evaluate paid intelligence through a bounded test before "
                    "adding another recurring obligation. An illustrative $400 "
                    "monthly subscription plus $100 for incremental storage "
                    "and monitoring totals $6,000 annually; these are desk "
                    "planning assumptions, not vendor quotations. If verified "
                    "automation saves ten contractor hours each month at an "
                    "avoidable $60 hourly cost, the annual benefit is $7,200 "
                    "and the direct contribution is $1,200 before implementation "
                    "and review costs. Saved salaried time creates capacity, "
                    "not automatic cash savings. Count it separately through "
                    "faster qualified briefs or fewer overdue reviews. Keep "
                    "this test inside the existing scenario cost envelope; "
                    "otherwise the published margin must change, so it "
                    "cannot be presented as the canonical case. Use "
                    "the $25,000 to $150,000 startup capital range to "
                    "plan setup and runway against the six-to-eighteen-month "
                    "time to first deal. Neither range proves that the "
                    "smallest capital budget covers the longest delay. "
                    "At $5,000 monthly operating expense, six months "
                    "already consumes $30,000 before setup costs or "
                    "additional delivery spending. Favor engagement structures "
                    "with earned, documented service milestones where "
                    "appropriate, and review contingent-fee restrictions "
                    "before linking compensation to awards. A discovery "
                    "platform cannot cure payment delays or a fee "
                    "arrangement that the procurement structure does not permit."
                ),
                (
                    "Manage the pod through exception volume, not the number "
                    "of scraped records. The data operator publishes a "
                    "morning source-health report and a deduplicated change "
                    "queue. The capture lead reviews deadline and eligibility "
                    "changes first, then assigns supplier and proposal "
                    "exceptions to the relevant contractors. Batch lower "
                    "priority incumbent research into a weekly P2 review. "
                    "Measure collection freshness, missed amendments, unresolved "
                    "identity matches, qualified briefs per reviewer hour, "
                    "supplier quotation expiry, and milestone exceptions. "
                    "Set internal service targets from actual staffing "
                    "coverage, distinguishing those targets from agency "
                    "publication timing and portal availability. Track "
                    "the fraction of recommendations with complete "
                    "evidence lineage; a high alert count can hide "
                    "poor decision quality. Review paid subscriptions "
                    "monthly against verified decision use, not logins. "
                    "Retire connectors that produce no actionable "
                    "evidence, while preserving the authoritative manual "
                    "fallback. Expand into another municipality only "
                    "after existing active pursuits have dependable "
                    "coverage and a tested backup operator. At "
                    "the Scaled case, assign added capacity to "
                    "documented bottlenecks such as supplier verification "
                    "or bid review rather than assuming more sources "
                    "produce proportionally more fees. The durable "
                    "advantage is a shorter, auditable path from "
                    "public evidence to an executable client decision, "
                    "with supplier failure and payment uncertainty "
                    "still visible in the operating queue."
                ),
            ],
            "table": {
                "caption": "Canonical economic bridge and capacity controls for the procurement information stack",
                "headers": [
                    "Scenario or operating control",
                    "Specific service-revenue or cost basis",
                    "Staffing and accountable operating constraint",
                    "Reconciliation or intervention required",
                ],
                "rows": [
                    [
                        "Conservative canonical case preserves the supplied fifteen-percent net margin",
                        "$120,000 recognized service fees less $102,000 total costs equals $18,000 profit",
                        "Two full-time employees and three contractors cover tightly bounded pursuit lanes",
                        "Keep tooling within total costs and distinguish contractor headcount from purchased hours",
                    ],
                    [
                        "Base canonical case preserves the supplied twenty-two-and-one-half-percent net margin",
                        "$560,000 recognized service fees less $434,000 total costs equals $126,000 profit",
                        "Two full-time employees and three contractors require controlled exception volume",
                        "Bridge direct delivery and recurring overhead without replacing the canonical revenue basis",
                    ],
                    [
                        "Scaled canonical case preserves the supplied thirty-percent net margin",
                        "$1,000,000 recognized service fees less $700,000 total costs equals $300,000 profit",
                        "Three full-time employees and four contractors create a seven-person operating team",
                        "Add capacity against measured bottlenecks while maintaining source and client segregation",
                    ],
                    [
                        "Illustrative tooling test measures avoidable costs rather than assumed award success",
                        "$6,000 annual tooling cost compares with $7,200 verified avoidable contractor expense",
                        "Data operator records actual hours saved and capture lead verifies useful outputs",
                        "$1,200 direct contribution excludes implementation costs and remains inside scenario budgeting",
                    ],
                    [
                        "Runway planning reconciles startup resources with a potentially extended first-deal cycle",
                        "$25,000 to $150,000 startup capital faces six to eighteen months before first deal",
                        "Capture lead forecasts cash alongside the supplied $5,000 to $25,000 monthly range",
                        "Model setup, delivery costs, collection timing, and reserves instead of assuming coverage",
                    ],
                    [
                        "Source expansion requires reliable coverage of existing active client pursuits",
                        "Count reviewed actionable changes rather than raw notices or commercial database records",
                        "Both full-time employees maintain documented backup procedures for critical bid-calendar tasks",
                        "Pause low-value research connectors when deadline, identity, or supplier exceptions accumulate",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The information edge is not seeing more notices; it is proving which facts changed before they change the bid.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Assign P1 through P7 to the two full-time employees and three scoped contractors, with named backups and documented response coverage.",
        "Register the eighteen sources with access terms, current entitlements, retrieval cadence, authoritative fallback, and the decision each source supports.",
        "Build raw, normalized, and decision layers with source-specific identifiers, attachment hashes, retrieval checkpoints, and reversible entity links.",
        "Test pagination loss, authentication pages, duplicate transactions, replaced attachments, ambiguous timezones, and delayed supplier milestones before relying on alerts.",
        "Document pursuit-specific fee, eligibility, workshare, amendment, and submission checks using the controlling solicitation and applicable primary authorities.",
        "Reconcile tooling and delivery costs to the exact Conservative, Base, and Scaled service-fee cases, then retain only subscriptions with demonstrated operating value.",
    ],
    "statutory_citations": [
        {
            "title": "41 U.S.C. 2102 — Prohibitions on disclosing and obtaining procurement information",
            "url": "https://www.law.cornell.edu/uscode/text/41/2102",
            "relevance": (
                "Distinguishes legitimate public procurement research from prohibited "
                "disclosure or obtaining of covered contractor bid, proposal, and "
                "source-selection information before award."
            ),
        },
        {
            "title": "41 U.S.C. 8702 — Prohibition on kickbacks",
            "url": "https://www.law.cornell.edu/uscode/text/41/8702",
            "relevance": (
                "Requires the desk to examine supplier compensation and referral "
                "arrangements for prohibited payments connected with covered "
                "prime contracts and subcontracts."
            ),
        },
        {
            "title": "FAR Subpart 3.4 — Contingent Fees",
            "url": "https://www.acquisition.gov/far/subpart-3.4",
            "relevance": (
                "Provides the federal framework for evaluating contingent-fee "
                "arrangements, relevant definitions, exceptions, and associated "
                "contracting consequences."
            ),
        },
        {
            "title": "FAR 52.203-5 — Covenant Against Contingent Fees",
            "url": "https://www.acquisition.gov/far/52.203-5",
            "relevance": (
                "Requires examination of the applicable contract covenant and "
                "actual compensation facts before adopting award-linked service "
                "fees or intermediary arrangements."
            ),
        },
        {
            "title": "FAR 52.215-23 — Limitations on Pass-Through Charges",
            "url": "https://www.acquisition.gov/far/52.215-23",
            "relevance": (
                "Where applicable, governs excessive pass-through charges and "
                "related duties; the desk must connect proposed workshare and "
                "added value to the incorporated clause."
            ),
        },
        {
            "title": "13 CFR 125.6 — Limitations on subcontracting",
            "url": "https://www.ecfr.gov/current/title-13/chapter-I/part-125/section-125.6",
            "relevance": (
                "Establishes performance limitations for covered small-business "
                "contracts, including rules requiring contract-specific analysis "
                "of similarly situated entities and applicable exceptions."
            ),
        },
        {
            "title": "FAR 4.1102 — System for Award Management policy",
            "url": "https://www.acquisition.gov/far/4.1102",
            "relevance": (
                "Supports registration checks at relevant procurement stages "
                "while requiring attention to stated exceptions rather than "
                "assuming every participant has identical registration duties."
            ),
        },
        {
            "title": "FAR 9.405 — Effect of listing",
            "url": "https://www.acquisition.gov/far/9.405",
            "relevance": (
                "Explains procurement consequences associated with exclusions "
                "and informs investigation of potential matches before supplier "
                "or prime recommendations."
            ),
        },
        {
            "title": "FAR 15.206 — Amending the solicitation",
            "url": "https://www.acquisition.gov/far/15.206",
            "relevance": (
                "Supports amendment-aware evidence handling for negotiated "
                "federal acquisitions, including review of changes affecting "
                "requirements, proposal preparation, and submission timing."
            ),
        },
    ],
}
