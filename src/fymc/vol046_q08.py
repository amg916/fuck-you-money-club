from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small mass-tort case acquisition, hitech record triage & law-firm msos desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "PACER, FDA Signals, Patient-Directed Records, Identity Evidence, and Fixed-Fee MSO Instrumentation",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #46, Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs, ranks "
        "#13 of 49 with a 93/100 Money-to-Manpower Score and 13 mapped plays. This chapter turns "
        "public litigation signals, medical coding references, permissioned identity checks, and "
        "record-retrieval evidence into a small-team operating system. Its eighteen-source directory "
        "separates free discovery from metered verification and protected clinical processing. The "
        "paid_to_organic_media_arbitrage play is measured through collected administrative fees, "
        "not clicks or settlement awards. Canonical annual owner profits are $41,600 Conservative, "
        "$267,900 Base, and $625,000 Scaled. Preserve that distinction with fixed or cost-plus "
        "contracts, documented patient instructions, source-linked extraction, and a conversion "
        "ledger that exposes duplicates, unusable records, replacement obligations, and collection delays."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$160,000",
            "context": "Annual gross contracted MSO administrative and vendor-fee revenue",
            "note": "26% net margin; $41,600 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$705,000",
            "context": "Annual gross contracted MSO administrative and vendor-fee revenue",
            "note": "38.0% net margin; $267,900 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,250,000",
            "context": "Annual gross contracted MSO administrative and vendor-fee revenue",
            "note": "50% net margin; $625,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Turn Public Litigation and Product Signals into a Versioned Research Queue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a matter dictionary, not a purchased claimant list. Give each campaign a "
                    "stable matter identifier, product family, alleged injury vocabulary, exposure dates, "
                    "responsible attorney, and written intake criteria. The Judicial Panel on Multidistrict "
                    "Litigation supplies consolidation status and transfer orders; PACER supplies the actual "
                    "docket and filed documents. CourtListener's RECAP collection is a useful lower-cost "
                    "discovery layer, but missing documents and delayed uploads make it an incomplete mirror. "
                    "Record court, docket number, document number, retrieval time, source URL, and a content "
                    "hash for every instruction-changing order. A clerk-entered scheduling change is different "
                    "from a lawyer's commentary about that change. Route Rule 702 expert-evidence decisions "
                    "and changes to plaintiff fact sheets to the supervising firm before changing intake "
                    "questions. Public availability does not authorize harvesting injured people's identities "
                    "for unsolicited outreach. Research litigation posture and product evidence; obtain "
                    "claimant information through an attributable, permissioned interaction. An inexpensive "
                    "daily docket check can prevent a week of advertising against criteria that the receiving "
                    "firm has already abandoned. Preserve superseded criteria so later rejection disputes can "
                    "be reconstructed against the instructions actually active when the inquiry arrived."
                ),
                (
                    "Use FDA sources to enrich the matter dictionary, never to manufacture eligibility. "
                    "The openFDA enforcement endpoint exposes structured recall records, while FAERS "
                    "supports adverse-event signal research. Neither establishes that a product caused an "
                    "individual injury, and report counts require attention to duplicate reports, follow-up "
                    "submissions, reporting changes, and absent exposure denominators. DailyMed contributes "
                    "label text, ingredient names, dosage forms, and label revision identifiers useful for "
                    "search normalization. Store the original claimant wording alongside normalized terms; "
                    "a brand-to-ingredient mapping should not silently become proof of ingestion. Public "
                    "source refreshes differ from event dates, so carry both the source publication date "
                    "and the ingestion timestamp. A revised label may arrive after an exposure, and an "
                    "adverse-event report may describe an event years earlier. Join records by documented "
                    "identifiers and reviewed mappings rather than fuzzy brand matches alone. For each "
                    "campaign, maintain a compact evidence packet containing the firm's current criteria, "
                    "relevant orders, product references, and excluded interpretations. This packet gives "
                    "media buyers a controlled vocabulary without inviting them to promise recoveries, "
                    "diagnose injuries, or extrapolate legal causation from a government database entry. "
                    "Counsel determines which factual claims may appear in each advertisement."
                ),
                (
                    "Implement the public-source collector with an allowlisted host registry and a "
                    "per-source retrieval policy. Python's urllib.request, json, sqlite3, hashlib, and "
                    "datetime are sufficient for a modest research cache; no browser automation is "
                    "necessary where an official download or API exists. Store ETag and Last-Modified "
                    "values when supplied, use conditional requests, and impose request timeouts, "
                    "response-size ceilings, bounded retries, and jittered exponential backoff. Respect "
                    "Retry-After and published account quotas rather than assuming that a successful "
                    "request permits an unlimited crawl. Treat a changed response schema as an exception "
                    "requiring review, not an invitation to populate blank eligibility fields. Keep a "
                    "last-success timestamp and visibly distinguish a stale snapshot from a fresh response. "
                    "PACER spending deserves its own daily cap because repeated docket pulls and large "
                    "reports can erase the savings from free discovery. Fetch an authoritative document "
                    "once, retain its permitted internal copy, and reference that copy in subsequent work. "
                    "The first directory below names six research sources; the next two directories add "
                    "twelve verification and processing resources. Together they form an eighteen-source "
                    "stack with explicit access, cost, refresh, and fallback decisions."
                ),
            ],
            "table": {
                "caption": "Named Directory, Entries 1–6: Official Litigation and Product Research",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access route and cost tier",
                    "Refresh behavior and request hygiene",
                    "Fallback source and evidence limitation",
                ],
                "rows": [
                    [
                        "JPML centralizes multidistrict litigation status and transfer-order research.",
                        "Use jpml.uscourts.gov statistics and docket links; public publications are free.",
                        "Check posted publication dates daily during active matters; cache unchanged reports.",
                        "Confirm operative instructions through the transferee court's filed orders and docket.",
                    ],
                    [
                        "PACER provides authoritative federal docket entries and filed litigation documents.",
                        "Use pacer.uscourts.gov registered access; generally $0.10 per page, with applicable caps.",
                        "Poll only selected matters daily; budget separately for reports with cap exceptions.",
                        "Use court notices or RECAP discovery, then purchase missing authoritative documents.",
                    ],
                    [
                        "CourtListener RECAP provides reusable federal docket discovery and available document copies.",
                        "Use courtlistener.com/api/rest/v3/ with required authentication; account quotas and paid tiers vary.",
                        "Coverage follows ingestion activity; honor documented throttles and avoid repeated full-docket downloads.",
                        "Return to PACER when document coverage, timestamp freshness, or completeness is insufficient.",
                    ],
                    [
                        "openFDA enforcement records expose structured product-recall identifiers and published classification details.",
                        "Query api.fda.gov/drug/enforcement.json or device/enforcement.json; public API access is free.",
                        "Inspect published update schedules; cache results and obey current keyed account limits.",
                        "Cross-check FDA recall notices and manufacturer communications before changing campaign criteria.",
                    ],
                    [
                        "FDA FAERS supports aggregate adverse-event research without establishing individual legal causation.",
                        "Use fda.gov FAERS quarterly downloads or api.fda.gov/drug/event.json; public access is free.",
                        "Quarterly files and API releases can differ; version datasets and deduplicate reports.",
                        "Use original FDA documentation and reviewed medical literature for unresolved signal interpretation.",
                    ],
                    [
                        "DailyMed supplies official submitted label references, ingredients, and revision-linked product terminology.",
                        "Use dailymed.nlm.nih.gov/dailymed/services/v2/ REST resources; public service access is free.",
                        "Refresh relevant label identifiers daily; cache responses and retry throttled requests conservatively.",
                        "Check Drugs@FDA approval materials and historical labels when exposure-period wording matters.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Spend on Authoritative Exceptions, Not Repeated Discovery",
                "body": "The useful edge is a traceable change in operating criteria, not a larger pile of downloaded documents.",
                "items": [
                    "Subscribe to receiving-firm docket updates and purchase only missing PACER documents that change exposure, injury, filing, or evidentiary instructions.",
                    "Hash each downloaded order and attach the criteria version it changed; preserve the previous version for vendor replacement disputes.",
                    "Keep FAERS signal counts outside claimant eligibility fields so campaign researchers cannot accidentally promote aggregate reports into individual proof.",
                    "Use label revision identifiers and exposure dates together; current DailyMed wording may not describe the product during the claimant's use period.",
                ],
            },
        },
        {
            "heading": "2. Separate Identity Resolution, Provider Discovery, and Patient-Directed Record Access",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build an enrichment waterfall that asks the cheapest relevant question first. Validate "
                    "contact syntax locally, inspect the originating campaign and permission artifact, then "
                    "resolve an existing claimant using an internal identifier and limited matching attributes. "
                    "Use keyed HMAC tokens for normalized sensitive identifiers where deterministic matching "
                    "is necessary; plain hashes of telephone numbers are vulnerable to enumeration. Send "
                    "only the minimum required attributes to a contracted identity vendor after confirming "
                    "the permitted purpose, product terms, and applicable privacy restrictions. A LexisNexis "
                    "Risk Solutions product can contribute identity signals under its particular agreement; "
                    "it is not a universal registry of signed retainers. Duplicate representation requires "
                    "claimant confirmation and a receiving firm's controlled conflict or prior-representation "
                    "process. Do not circulate identities across unrelated firms to build an informal "
                    "blacklist. NPPES helps identify provider names, addresses, taxonomy, and identifiers, "
                    "but an NPI does not establish current licensure or prove treatment. Match the treating "
                    "facility from claimant-provided information, then confirm the records department through "
                    "an official channel. This sequencing reserves paid checks for unresolved cases and "
                    "prevents a weak match from silently excluding a legitimate claimant. Record the "
                    "reason for every merge and preserve a reversible separation procedure."
                ),
                (
                    "Treat medical-record acquisition as several distinct request routes. Under 45 CFR "
                    "164.524, an individual generally has access rights to protected health information "
                    "in a designated record set, subject to specified exceptions. The ordinary federal "
                    "response period is thirty calendar days, with one permitted thirty-day extension "
                    "when the required written explanation and completion date are supplied; shorter "
                    "applicable state requirements may matter. A HIPAA authorization under 45 CFR 164.508 "
                    "is a different instrument from an individual access request. Following Ciox Health "
                    "v. Azar and HHS guidance, do not assume that every third-party-directed request "
                    "receives the individual-access fee limitation or the same mandatory transmission "
                    "scope. Select the correct route with the firm's documented instructions, identify "
                    "the requested records precisely, and retain the signed direction and delivery "
                    "destination. Electronic health-record transmission rights under 42 U.S.C. 17935(e) "
                    "do not make every provider portal a general-purpose extraction API. Pharmacy records "
                    "require their own custodian identification and scope, including dispensing dates, "
                    "drug identifiers, quantities, and reversals where available. Track requests, "
                    "acknowledgments, invoices, extensions, partial returns, and missing facilities "
                    "separately. Escalate overdue or misrouted requests through the custodian's published "
                    "process instead of repeatedly resubmitting duplicate forms."
                ),
                (
                    "Normalize returned clinical evidence only after preserving the original files and "
                    "their provenance. CMS ICD-10-CM releases provide date-sensitive diagnosis vocabulary; "
                    "they do not transform a billing code into a confirmed injury. Save the code system, "
                    "release version, encounter date, source page, and surrounding clinical statement. "
                    "A chronology parser should distinguish patient-reported history, clinician assessment, "
                    "ruled-out conditions, and copied-forward text. Require source-page citations and "
                    "human review for exposure and diagnosis assertions that determine acceptance. "
                    "HealthIT.gov's Certified Health IT Product List helps locate certified products and "
                    "associated interoperability information, but certification does not grant access "
                    "to a claimant's chart. FHIR access still depends on the actual provider endpoint, "
                    "supported implementation, identity workflow, and authorization context. Establish "
                    "the MSO's role for each engagement rather than assuming every participant is a "
                    "HIPAA business associate. Where a covered entity or business associate relationship "
                    "requires one, execute the appropriate agreement and verify that every downstream "
                    "processing service supports the intended use. Separate public research from "
                    "protected clinical storage, restrict worker access by matter, and log exports. "
                    "State bar and Arizona ABS lookups verify professional or entity status; they "
                    "cannot substitute for analyzing the particular contract and ownership arrangement."
                ),
            ],
            "table": {
                "caption": "Named Directory, Entries 7–12: Provider, Clinical Reference, and Professional Verification",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access route and cost tier",
                    "Refresh behavior and request hygiene",
                    "Fallback source and evidence limitation",
                ],
                "rows": [
                    [
                        "NPPES NPI Registry resolves provider identifiers, practice locations, and reported taxonomy.",
                        "Query npiregistry.cms.hhs.gov/api/?version=2.1 with search parameters; public API access is free.",
                        "Cache provider matches; registry updates do not ensure immediate practice-location accuracy.",
                        "Confirm records custody with the provider's official records office and licensing board.",
                    ],
                    [
                        "CMS ICD-10-CM files support versioned diagnosis normalization and encounter-date code validation.",
                        "Download release files from cms.gov/medicare/coding-billing/icd-10-codes; public reference downloads are free.",
                        "Load each applicable effective-date release; avoid repeated downloads during ordinary record processing.",
                        "Use CDC NCHS ICD-10-CM publications and clinician-reviewed source text for disputed mappings.",
                    ],
                    [
                        "HealthIT CHPL identifies certified health-record products and available interoperability reference links.",
                        "Search chpl.healthit.gov; public portal access is free and API access follows current terms.",
                        "Recheck products when onboarding providers; respect current API-key requirements and account limits.",
                        "Request the provider's actual endpoint documentation because certification alone grants no access.",
                    ],
                    [
                        "ClinicalTrials.gov helps distinguish registered study populations, interventions, and documented research status.",
                        "Query clinicaltrials.gov/api/v2/studies using documented filters; public API access is free.",
                        "Check study update dates; paginate bounded queries and cache unchanged study versions.",
                        "Consult linked publications and study contacts; registration does not establish claimant eligibility.",
                    ],
                    [
                        "Arizona Supreme Court ABS directory verifies listed alternative business structure entity status.",
                        "Use azcourts.gov/cld/Alternative-Business-Structure public listings; directory access requires no purchase.",
                        "Recheck before contracting and periodically afterward; preserve dated evidence of listed status.",
                        "Verify relevant licensing orders and entity scope directly with Arizona licensing authorities.",
                    ],
                    [
                        "State Bar of California Attorney Search verifies California attorney status and public discipline.",
                        "Search apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch; public individual lookups are free.",
                        "Check at onboarding and renewal; use manual bounded searches rather than bulk scraping.",
                        "Use the corresponding official state bar directory for lawyers licensed elsewhere.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Purpose, Permission, Contract, and Clinical Traceability",
                "body": "Release a matter into paid processing only when all four checks have attributable evidence.",
                "items": [
                    "Confirm the receiving attorney's current status, the contracted entity, and fixed or cost-plus scope; verify any claimed Arizona ABS authorization separately.",
                    "Retain the claimant's records instruction, intended recipient, covered dates, and selected access route before transmitting a retrieval request.",
                    "Verify vendor permitted purpose, required service agreements, regional settings, access controls, and subcontractor handling before uploading protected records.",
                    "Require source-linked exposure and injury evidence, duplicate-resolution notes, and a dated firm acceptance checklist before marking the packet complete.",
                ],
            },
        },
        {
            "heading": "3. Instrument Permission, Protected Processing, and Vendor Failure Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create an append-only event ledger spanning raw inquiry, signed law-firm retainer, "
                    "usable EMR or pharmacy proof, deficiency-free accepted case, and collected MSO or "
                    "vendor fee. Each event needs a matter identifier, claimant token, timestamp, actor, "
                    "source artifact, criteria version, and reason code. Keep identity details in a "
                    "separate restricted store; media dashboards should receive aggregate cohort counts "
                    "rather than diagnoses or uploaded records. TrustedForm certificates can document "
                    "aspects of a web interaction, but the certificate is evidence to inspect, not "
                    "automatic proof that every later call is permitted. Preserve the actual disclosure, "
                    "named firm, page version, source URL, timestamp, and revocation history. The FCC's "
                    "2023 one-to-one consent rule was vacated in Insurance Marketing Coalition v. FCC; "
                    "do not present it as an operative nationwide mandate. Nevertheless, firm-specific "
                    "permission is a sensible contractual control, alongside the applicable TCPA rules "
                    "for the communication technology, state requirements, and advertising restrictions. "
                    "A Twilio line-type result does not prove ownership, willingness to receive contact, "
                    "or permission for automated outreach. Reconcile suppression events across intake, "
                    "dialing, messaging, and vendors before another contact attempt. Keep evidence of "
                    "the suppression distribution and record failed propagation as an operational incident."
                ),
                (
                    "Protected processing requires a different service boundary from marketing analytics. "
                    "Use a dedicated cloud project or account, least-privilege service identities, "
                    "encryption, explicit retention schedules, and controlled export destinations. "
                    "Google Cloud Healthcare API can store supported clinical formats and expose "
                    "documented interfaces, but it does not retrieve records from arbitrary hospitals. "
                    "Amazon Textract can produce OCR and structured extraction for supported documents; "
                    "its output still requires quality checks against the original page. Confirm current "
                    "service eligibility, executed agreements where required, region, logging behavior, "
                    "and permitted features before any protected upload. A general-purpose language "
                    "model should not receive clinical content merely because its interface is convenient. "
                    "Configure any approved parser to return structured assertions with page references, "
                    "uncertainty reasons, and explicit abstentions when evidence is absent. Validate dates, "
                    "drug identifiers, negation, and patient identity before generating a chronology. "
                    "Documents themselves are untrusted input; embedded instructions must never control "
                    "the parser's tools or export destinations. Test with synthetic records and approved "
                    "de-identified fixtures before live use. Measure page-level OCR errors, unsupported "
                    "assertions, and reviewer corrections, not just processing speed. Preserve the original "
                    "artifact so a reviewer can resolve a disagreement without rerunning an opaque pipeline."
                ),
                (
                    "A small desk needs predictable recovery more than elaborate infrastructure. Use "
                    "idempotency keys for retrieval orders, certificate claims, invoice creation, and "
                    "webhook processing. Verify webhook signatures, reject stale replays within a "
                    "documented tolerance, and retain only the minimum debugging payload. Put failed "
                    "jobs into a restricted exception queue with an owner and next action. Distinguish "
                    "authentication failure, quota exhaustion, provider outage, malformed source file, "
                    "and missing claimant instruction; these require different remedies. Monitor queue "
                    "age, successful fetch latency, records turnaround, human-review minutes, and "
                    "collection lag. Cloud request metrics can show technical health while the business "
                    "quietly accumulates unusable records, so report acceptance outcomes by source and "
                    "criteria version. Google Search Console supplies delayed organic search performance, "
                    "not a live ledger of paid conversions. Join its aggregate landing-page signals "
                    "to first-party campaign reporting without exporting claimant identity. Reconcile "
                    "vendor invoices against completed jobs weekly and test restore procedures monthly. "
                    "When a vendor fails, fall back to documented manual custody, secure upload, or "
                    "deferred processing, not an unapproved consumer service. Every fallback should "
                    "preserve the same permission, provenance, and deletion requirements as the primary "
                    "route. Assign a maximum tolerated age to each queue before launch."
                ),
            ],
            "table": {
                "caption": "Named Directory, Entries 13–18: Commercial APIs, Processing Rails, and Diagnostics",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access route and cost tier",
                    "Refresh behavior and request hygiene",
                    "Fallback source and evidence limitation",
                ],
                "rows": [
                    [
                        "ActiveProspect TrustedForm preserves interaction evidence associated with lead capture and disclosure.",
                        "Integrate documented capture script and api.trustedform.com endpoints; retention and verification require purchased terms.",
                        "Capture at submission; claim promptly under current product rules and honor account throttles.",
                        "Retain first-party disclosure snapshots and event logs; missing certificates require explicit evidence review.",
                    ],
                    [
                        "LexisNexis Risk Solutions supports contracted identity checks and reviewed fraud-risk signal enrichment.",
                        "Provision the selected product through risk.lexisnexis.com; credentials, endpoints, and pricing are contract-specific.",
                        "Query only unresolved permitted-purpose cases; deduplicate requests and enforce purchased transaction limits.",
                        "Use claimant confirmation and firm-controlled review; vendor results cannot establish duplicate representation alone.",
                    ],
                    [
                        "Twilio Lookup supplies telephone formatting and optional line-type or identity-related network signals.",
                        "Call lookups.twilio.com/v2/PhoneNumbers/{PhoneNumber} with authenticated requests; paid packages carry usage charges.",
                        "Retrieve near contact time where needed; respect account concurrency and back off after throttling.",
                        "Use direct claimant confirmation and suppression records; telephone enrichment never supplies contact permission.",
                    ],
                    [
                        "Google Search Console identifies organic query demand and landing-page search performance trends.",
                        "Use searchconsole.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query with OAuth; API access has no usage fee.",
                        "Expect reporting delay and incomplete recent periods; partition queries within documented project quotas.",
                        "Use first-party aggregate landing-page events when search reports lag or suppress query detail.",
                    ],
                    [
                        "Google Cloud Healthcare API provides controlled FHIR, DICOM, and HL7v2 storage interfaces.",
                        "Use healthcare.googleapis.com/v1 projects, locations, and datasets; storage and operations are usage-priced.",
                        "Ingestion follows authorized submissions; monitor regional quotas and exponential backoff on throttling.",
                        "Use an approved encrypted document repository when structured ingestion fails or endpoints differ.",
                    ],
                    [
                        "Amazon Textract extracts document text and supported structured fields for evidence preparation.",
                        "Use regional Textract API operations with IAM; OCR and advanced extraction are usage-priced.",
                        "Process asynchronous job notifications; enforce regional service quotas and bounded retry budgets.",
                        "Route difficult pages to authorized human transcription while preserving original document provenance.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register and classify the source",
                    "action": "Record the exact endpoint, owner, permitted purpose, pricing basis, and fallback.",
                    "detail": "Separate public research, contact evidence, identity checks, and protected clinical processing before credentials are issued.",
                },
                {
                    "step": 2,
                    "title": "Test a bounded evidence transaction",
                    "action": "Run synthetic fixtures through authentication, pagination, throttling, and schema validation.",
                    "detail": "Confirm that logs exclude protected payloads and that repeated submissions cannot create duplicate paid jobs.",
                },
                {
                    "step": 3,
                    "title": "Attach provenance to every transformation",
                    "action": "Persist source hashes, retrieval timestamps, criteria versions, and page-linked extraction results.",
                    "detail": "Require reviewer correction paths for mismatched identities, negated diagnoses, and unsupported exposure assertions.",
                },
                {
                    "step": 4,
                    "title": "Reconcile operational and cash outcomes",
                    "action": "Compare accepted packets, contractual service delivery, issued invoices, and actual collections.",
                    "detail": "Escalate aged replacements and overdue receivables separately so accounting recognition is not confused with cash arrival.",
                },
            ],
        },
        {
            "heading": "4. Price the Complete Waterfall and Stop Buying When Evidence Economics Break",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Apply paid_to_organic_media_arbitrage, the TRACK_2 Paid-to-Organic Media Arbitrage "
                    "play, to permissioned audience development rather than claimant resale. Test "
                    "secondary ad networks, vetted newsletter sponsorships, and long-tail search pages "
                    "against the receiving firm's advertising instructions. The generic play monetizes "
                    "cheap attention through B2B leads, affiliate payouts, and retained audiences; this "
                    "volume narrows monetization to contracted administrative and marketing services "
                    "where the actual arrangement is permitted. Do not import high-ticket affiliate "
                    "commissions tied to a legal engagement or recovery. Suppose $10,000 buys 5,000 "
                    "clicks at $2 and produces 1,000 raw inquiries at a twenty-percent submission rate. "
                    "After two hundred duplicate or invalid inquiries, eight hundred unique inquiries "
                    "yield two hundred signed law-firm retainers at twenty-five percent. Sixty percent "
                    "produce usable clinical proof, and eighty percent of those pass the firm's "
                    "deficiency checklist, leaving ninety-six accepted cases. Media cost is $10 per "
                    "raw inquiry but approximately $104.17 per accepted case. Neither figure is a "
                    "permitted fee quote or a recovery forecast. Build an opted-in first-party "
                    "newsletter around public educational material, not condition-based advertising "
                    "audiences. Avoid sensitive-health remarketing and vendor uploads that reveal "
                    "claimant status. Measure retained audience value through attributable service demand."
                ),
                (
                    "Reconcile that illustrative monthly cohort to the canonical Base operating envelope. "
                    "Contracted service revenue averages $58,750 monthly, or $705,000 annually; this is "
                    "fixed or cost-plus service consideration, not ninety-six contingent case bounties. "
                    "Allocate $10,000 to media, $6,000 to retrieval at two hundred requests averaging "
                    "$30, and $20,425 to all remaining labor, software, occupancy, insurance, and "
                    "operating costs. Total monthly expense is $36,425, leaving $22,325 owner profit. "
                    "Annual expense is $437,100 and annual owner profit is exactly $267,900, a 38.0% "
                    "margin. The $30 retrieval assumption is a budgeting average, not a statutory "
                    "fee entitlement. Revenue allocated across ninety-six accepted packets is about "
                    "$611.98 each, solely an internal productivity measure. Define service deliverables, "
                    "replacement periods, documented defects, and remedy caps in the contract without "
                    "linking compensation to settlements or legal fees. ABA Model Rule 5.4 is a "
                    "model professional rule; applicable state enactments and substantive arrangements "
                    "control. Fixed pricing alone cannot cure impermissible referral payments, "
                    "interference with professional judgment, or unlawful ownership. Arizona ABS "
                    "participation requires the relevant authorization, not an address or a generic "
                    "co-venture label. The law firm retains legal screening and representation decisions."
                ),
                (
                    "Stress the waterfall before increasing spend. If duplicate losses rise to thirty "
                    "percent, the same thousand inquiries leave seven hundred unique prospects and "
                    "175 retainers at the existing conversion rate. If usable-proof conversion falls "
                    "to fifty percent, the cohort produces 87.5 expected proof packets and seventy "
                    "expected accepted cases after the eighty-percent acceptance step; these are "
                    "planning expectations, not fractional people in the production ledger. Raising "
                    "media expense to $12,500 and retrieval to $40 for each of 175 requests produces "
                    "$7,000 retrieval expense. Holding other expense at $20,425 leaves $18,825 monthly "
                    "profit on unchanged $58,750 service revenue. This sensitivity is not a replacement "
                    "scorecard scenario. Replacement labor, contractual credits, or customer attrition "
                    "would worsen it further. Pause acquisition when duplicate-adjusted accepted-case "
                    "cost breaches the contracted service budget, usable-proof rates deteriorate, or "
                    "replacement work consumes reserved capacity. Shift toward first-party newsletter "
                    "distribution and reviewed organic pages while investigating the vendor. Keep "
                    "collected fees separate from earned revenue and receivables; delayed payment "
                    "reduces cash availability without automatically changing recognized revenue. "
                    "Canonical Conservative and Scaled results remain $41,600 and $625,000 annual "
                    "owner profit. Settlement awards, trust balances, and client recoveries never "
                    "enter the MSO revenue denominator."
                ),
            ],
            "table": {
                "caption": "Conversion Ledger and Formula v2.0 Reconciliation: Five Stages and Three Canonical Cases",
                "headers": [
                    "Stage or canonical operating scenario",
                    "Unit math and recognized operating basis",
                    "Required evidence or expense reconciliation",
                    "Failure signal and concrete operating response",
                ],
                "rows": [
                    [
                        "Raw inquiry begins the attributable monthly acquisition cohort.",
                        "Five thousand clicks at $2 produce one thousand inquiries for $10,000.",
                        "Retain campaign identifiers, disclosure versions, source timestamps, and contact-permission evidence.",
                        "Pause vendor spend when invalid submissions or permission defects exceed agreed tolerances.",
                    ],
                    [
                        "Signed law-firm retainer follows duplicate screening and independent attorney-controlled intake.",
                        "Eight hundred unique inquiries convert at twenty-five percent into two hundred retainers.",
                        "Preserve firm-confirmed execution status and controlled prior-representation resolution without cross-firm blacklists.",
                        "Quarantine identity conflicts and unresolved representation disputes before buying additional retrieval services.",
                    ],
                    [
                        "Usable HITECH EMR or pharmacy proof establishes source-linked factual evidence.",
                        "Two hundred retrieval requests at $30 yield 120 usable proof packets.",
                        "Budget $6,000 retrieval expense and preserve authorizations, source pages, and reviewer decisions.",
                        "Escalate missing custodians and nonqualifying evidence rather than relabeling incomplete packets.",
                    ],
                    [
                        "Deficiency-free accepted case reflects the receiving firm's current evidence checklist.",
                        "One hundred twenty proof packets at eighty-percent acceptance produce ninety-six accepted cases.",
                        "Retain dated acceptance, checklist version, defect notices, and contract-specific replacement-window deadlines.",
                        "Reserve rework capacity and dispute defects against the criteria active at delivery.",
                    ],
                    [
                        "Collected MSO or vendor fee closes the cash-conversion ledger.",
                        "Monthly service revenue averages $58,750; invoice collection timing remains separately tracked.",
                        "Match bank receipts to invoices while recognizing earned consideration under applicable contract terms.",
                        "Escalate overdue balances without substituting trust funds or expected settlements for receipts.",
                    ],
                    [
                        "Conservative canonical case uses one full-time operator and three contractors.",
                        "$160,000 annual gross MSO revenue at 26% produces $41,600 owner profit.",
                        "Annual expense totals $118,400, excluding settlement awards and law-firm trust balances.",
                        "Keep contracted scope within staffing capacity and reconcile actual retrieval outlays monthly.",
                    ],
                    [
                        "Base canonical case uses one full-time operator and three contractors.",
                        "$705,000 annual gross MSO revenue at 38.0% produces $267,900 owner profit.",
                        "Annual expense totals $437,100, equivalent to the illustrative $36,425 monthly budget.",
                        "Investigate duplicate spikes, clinical rejection, replacement work, and delayed customer collections separately.",
                    ],
                    [
                        "Scaled canonical case uses two full-time operators and four contractors.",
                        "$1,250,000 annual gross MSO revenue at 50% produces $625,000 owner profit.",
                        "Annual expense totals $625,000 while the total team remains six people.",
                        "Add volume only after measured review capacity and contracted service demand support expansion.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The information edge is the shortest auditable path from permissioned inquiry to usable proof and collected service fees.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Register all eighteen named sources with access owner, current pricing, request limits, refresh expectations, and a documented fallback.",
        "Create a versioned matter dictionary linking current firm criteria to authoritative docket documents and dated product references.",
        "Implement a reversible duplicate-resolution workflow using limited identifiers, permitted-purpose checks, and firm-controlled representation review.",
        "Separate individual access requests from authorizations and record the applicable custodian, response deadline, fee route, and secure delivery destination.",
        "Test protected-document extraction with synthetic fixtures, page-linked assertions, reviewer corrections, webhook verification, and restore exercises.",
        "Reconcile the five-stage cohort ledger to $705,000 Base revenue, $437,100 expense, $267,900 owner profit, and separately tracked collections.",
    ],
    "statutory_citations": [
        {
            "title": "45 CFR 164.524 — Access of Individuals to Protected Health Information",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524",
            "relevance": (
                "Defines individual access rights, request handling, response timing, permitted extensions, "
                "forms of access, and applicable fee provisions."
            ),
        },
        {
            "title": "45 CFR 164.508 — Uses and Disclosures for Which an Authorization Is Required",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.508",
            "relevance": (
                "Supports distinguishing a valid authorization from an individual access request and "
                "checking required authorization elements."
            ),
        },
        {
            "title": "42 U.S.C. 17935(e) — Access to Certain Information in Electronic Format",
            "url": "https://www.law.cornell.edu/uscode/text/42/17935",
            "relevance": (
                "Provides the statutory electronic-record access framework without granting unrestricted "
                "access to provider systems."
            ),
        },
        {
            "title": "45 CFR 164.504(e) — Business Associate Contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Defines required contractual assurances where the service relationship is subject "
                "to HIPAA business associate requirements."
            ),
        },
        {
            "title": "45 CFR 164.312 — Technical Safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312",
            "relevance": (
                "Supplies technical safeguard requirements relevant to access controls, audit controls, "
                "integrity, authentication, and transmission security."
            ),
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on Telephone Equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Provides the TCPA statutory framework for evaluating calling and messaging practices "
                "alongside current implementing rules and court decisions."
            ),
        },
        {
            "title": "47 CFR 64.1200 — Delivery Restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Provides implementing requirements for covered telephone communications, permission, "
                "identification, and do-not-call practices."
            ),
        },
        {
            "title": "Federal Rule of Evidence 702 — Testimony by Expert Witnesses",
            "url": "https://www.law.cornell.edu/rules/fre/rule_702",
            "relevance": (
                "Explains why expert-evidence rulings can change litigation viability and require "
                "attorney-reviewed updates to campaign and intake criteria."
            ),
        },
        {
            "title": "California Business and Professions Code 6152 — Unlawful Runner and Capper Conduct",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=6152.",
            "relevance": (
                "Illustrates state-specific restrictions requiring review of solicitation and referral "
                "arrangements beyond the wording of a fixed-fee MSO contract."
            ),
        },
    ],
}
