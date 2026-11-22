from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small nemt & medical courier dispatch arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "NPPES, CLIA, Medicaid Procurement, RouteGenie, MediRoutes, X12 Remittances & UN3373 Custody Evidence",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #34, Rank #08 of 36, scores 90/100 by turning fragmented healthcare "
        "logistics information into repeatable dispatch decisions. This chapter connects nine "
        "mapped plays: standing-order scouting, laboratory lane prospecting, workers' compensation "
        "sourcing, credential verification, exclusion screening, dispatch telemetry, claims "
        "reconciliation, specimen custody, and rank-and-rent call routing. An eighteen-source "
        "directory separates free discovery records from permissioned operational evidence. "
        "The canonical annual owner profits are $30,000 Conservative, $166,500 Base, and "
        "$384,000 Scaled; corresponding retained dispatch revenue is $112,500, $416,250, and "
        "$720,000 after driver settlements. Build the edge through dated source records, "
        "contract-specific interfaces, and exception queues, not purchased patient lists. "
        "Use commercial tooling only when measurable recovery, route density, or collection "
        "speed covers its full operating cost."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross contracted billings; $112,500 retained at 45%",
            "note": "12% gross-billings net margin; $30,000 owner profit; 2 FT + 2 C; 26.67% retained net margin",
        },
        {
            "label": "Base",
            "value": "$925,000",
            "context": "Annual gross contracted billings; $416,250 retained at 45%",
            "note": "18.0% gross-billings net margin; $166,500 owner profit; 2 FT + 2 C; 40.0% retained net margin",
        },
        {
            "label": "Scaled",
            "value": "$1,600,000",
            "context": "Annual gross contracted billings; $720,000 retained at 45%",
            "note": "24% gross-billings net margin; $384,000 owner profit; 3 FT + 3 C; 53.33% retained net margin",
        },
    ],
    "sections": [
        {
            "heading": "1. Build a dated facility and contracting graph before buying enrichment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with organizations, service locations, and contracting entities, not patient "
                    "records. The desk's nine working applications are standing-order scouting, "
                    "laboratory lane prospecting, workers' compensation sourcing, credential verification, "
                    "exclusion screening, dispatch telemetry, claims reconciliation, specimen custody, "
                    "and rank_and_rent_pay_per_call_routing. These labels organize this chapter's "
                    "workflow; they are not substitutes for a payer's actual authorization rules. "
                    "Use the NPPES NPI Registry to identify organizational providers, then join CMS "
                    "facility datasets and CLIA records to physical locations. Store NPI, CLIA "
                    "identifier where applicable, organization name, service address, source URL, "
                    "retrieval time, source publication date, and match confidence. Keep an address "
                    "history because a mailing address can differ from the pickup entrance. An NPI "
                    "establishes an enumeration record, not Medicaid enrollment, ownership of a "
                    "vehicle fleet, or demand for transportation. A CLIA certificate establishes "
                    "a laboratory's certification attributes, not permission to carry every specimen "
                    "category. For standing-order scouting, forty verified facilities producing "
                    "eight qualified conversations and two contracts is a testable funnel, not a "
                    "forecast. At thirty weekly legs per contract and $40 contracted billings per "
                    "leg, two contracts represent $124,800 annual billings over fifty-two weeks; "
                    "apply the actual settlement schedule before calling that opportunity revenue."
                ),
                (
                    "Build an enrichment waterfall that stops as soon as the next operating "
                    "decision becomes supportable. First resolve the legal organization through "
                    "NPPES and the relevant Secretary of State registry. Second establish facility "
                    "type through CMS, CLIA, or a state licensing portal. Third confirm service "
                    "geography and a published business telephone number from the organization's "
                    "own website. Fourth use SAM.gov, state procurement notices, and public contract "
                    "awards to identify the buying office and renewal calendar. Finally call the "
                    "published switchboard to verify the transportation or laboratory logistics "
                    "contact. Never purchase patient-level demand estimates or append health "
                    "conditions to business contacts. Twenty laboratory prospects costing twelve "
                    "minutes each consume four research hours; at an illustrative $30 loaded "
                    "hourly cost, the batch costs $120 before subscriptions. One verified route "
                    "opportunity can justify that research, but only after pickup windows and "
                    "required packaging are confirmed. If a commercial enrichment vendor cannot "
                    "explain provenance, retain the public switchboard and continue manually. "
                    "When a portal blocks automated access, use its documented download or request "
                    "public procurement documents through the agency's records process. Public "
                    "availability does not establish permission to bypass authentication, scrape "
                    "restricted pages, or redistribute protected material."
                ),
                (
                    "Separate discovery freshness from eligibility freshness. A quarterly facility "
                    "file can support territory planning while being too old to clear tomorrow's "
                    "assignment. Preserve both the date a source published its record and the date "
                    "the desk retrieved it; these answer different questions. Before bidding, "
                    "verify that the solicitation remains open, amendments are incorporated, and "
                    "the contracting organization actually buys the service being offered. Before "
                    "assignment, verify required provider enrollment, driver qualifications, insurance, "
                    "and exclusions against the applicable program and contract. OIG's LEIE and "
                    "SAM exclusions serve different purposes, so a clear result in one cannot "
                    "replace the other. Resolve possible matches with authorized identifiers through "
                    "the official process rather than rejecting someone on name similarity alone. "
                    "For workers' compensation sourcing, six employer or administrator conversations "
                    "yielding one ten-trip weekly lane at $55 per trip would produce $28,600 "
                    "annual billings; the fallback is a written spot-service arrangement, not "
                    "invented standing demand. Assign every source an owner and expiration rule. "
                    "If the newest registry snapshot cannot be downloaded, retain the last "
                    "verified version for prospecting, mark its age visibly, and suspend decisions "
                    "that require current verification until the authoritative check succeeds."
                ),
            ],
            "table": {
                "caption": "Official Discovery Directory, Sources 1–9: Access, Economics, Freshness, and Recovery",
                "headers": [
                    "Named source and exact access",
                    "Operator decision and record key",
                    "Cost tier and purchasing boundary",
                    "Refresh latency and freshness test",
                    "Rate-limit hygiene and fallback source",
                ],
                "rows": [
                    [
                        "CMS NPPES NPI Registry: GET https://npiregistry.cms.hhs.gov/api/?version=2.1 with documented search parameters.",
                        "Resolve organizational NPI and practice location before contacting the facility's published business office.",
                        "Public searches and CMS dissemination downloads are free; budget staff time for ambiguous identity matches.",
                        "CMS describes daily registry updates; dissemination files have separate monthly and weekly publication schedules.",
                        "Use documented bounded result windows and cached queries; use CMS NPPES dissemination files for bulk coverage.",
                    ],
                    [
                        "CMS Provider Data Catalog: select datasets and distribution links at https://data.cms.gov/provider-data/.",
                        "Identify dialysis facilities and other listed provider categories using dataset identifiers and facility addresses.",
                        "Public datasets are free to download; storage and address reconciliation remain desk operating expenses.",
                        "Read each dataset's release metadata; publication cadence and historical coverage differ across provider categories.",
                        "Prefer published downloads over repeated searches; use facility websites and state licenses to resolve discrepancies.",
                    ],
                    [
                        "CMS CLIA Laboratory Search: use the CLIA search interface at https://qcor.cms.gov/.",
                        "Check laboratory certificate identifiers, addresses, and certification attributes before discussing specimen pickup requirements.",
                        "Public lookup access is free; operational confirmation still requires direct conversation with laboratory personnel.",
                        "Record the displayed record date and query time; reconfirm critical certificate details before onboarding.",
                        "Use the interactive workflow without bypassing controls; request confirmation from the state CLIA agency when needed.",
                    ],
                    [
                        "SAM.gov Contract Opportunities: browse https://sam.gov/ or request the documented opportunities API with an API key.",
                        "Track federal courier solicitations, amendments, deadlines, and award-office contacts using the notice identifier.",
                        "Public opportunity access is free; API registration does not create contracting eligibility or purchasing authority.",
                        "Check active notices each business day; agency amendments can change requirements between scheduled pipeline runs.",
                        "Observe current key quotas and server responses; fall back to saved searches and contracting-office notices.",
                    ],
                    [
                        "SAM.gov Entity Information: search entity and exclusion records through the official https://sam.gov/ interface.",
                        "Confirm federal entity identity and applicable exclusion records without treating them as Medicaid enrollment evidence.",
                        "Public searches are free; some datasets and API permissions require authenticated accounts or additional access.",
                        "Recheck at onboarding and applicable contract milestones; preserve query time and the matched entity identifier.",
                        "Automate only through authorized published interfaces; use official manual searches when entitlement limits block automation.",
                    ],
                    [
                        "HHS OIG LEIE: download exclusion files and use the verification workflow at https://exclusions.oig.hhs.gov/.",
                        "Screen required individuals and entities, then resolve possible matches through the official identity-verification process.",
                        "Public search and download access are free; allocate staff effort for potential-match resolution and documentation.",
                        "The downloadable database is updated monthly; screening frequency must also satisfy state and contract requirements.",
                        "Download each release once and hash locally; use the official online search when a file cannot be obtained.",
                    ],
                    [
                        "California Cal eProcure: search public bid events and posted documents at https://caleprocure.ca.gov/.",
                        "Locate state transportation and courier buying events, then capture amendments and the named procurement contact.",
                        "Public browsing generally carries no search charge; supplier participation can require registration and documented qualifications.",
                        "Monitor shortlisted events each business day; an amendment can supersede a previously downloaded requirements document.",
                        "Use saved searches and permitted downloads; obtain inaccessible attachments directly from the listed procurement officer.",
                    ],
                    [
                        "California Secretary of State bizfile: search business entities at https://bizfileonline.sos.ca.gov/.",
                        "Resolve entity names and filing status before connecting a provider brand to the proposed contracting party.",
                        "Basic public searches are free; certified records and selected filings can carry published government fees.",
                        "Capture the displayed filing date and retrieval time; filed records can lag actual operational changes.",
                        "Use manual searches unless automation is explicitly supported; request official records when name matches remain ambiguous.",
                    ],
                    [
                        "California DWC: access medical provider network and workers' compensation resources through https://www.dir.ca.gov/dwc/.",
                        "Identify published network organizations and program contacts without treating network inclusion as a transportation purchase order.",
                        "Published program resources are free; direct commercial outreach and qualification require separate desk labor.",
                        "Check each document's revision date; verify current network or administrator contacts before proposing a lane.",
                        "Cache official documents and avoid repeated bulk requests; confirm stale contacts through the administrator's published switchboard.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Find the route constraint that the public record cannot show",
                "body": "Public records locate prospects; operational interviews establish whether a lane can actually earn its settlement spread.",
                "items": [
                    "Ask dialysis centers for recurring chair-start and discharge-window patterns in aggregate; obtain patient details only through the authorized booking workflow.",
                    "Ask laboratories whether the posted street address is the receiving dock, patient service center, or administrative office before calculating route miles.",
                    "Capture solicitation amendments as separate hashed documents; compare response deadlines and insurance requirements against the original release.",
                    "Maintain separate identity and location records so a renamed laboratory does not appear to create a new service lane or duplicate prospect.",
                ],
            },
        },
        {
            "heading": "2. Buy interfaces that produce evidence, not dashboards that merely display activity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Move into permissioned systems only after the public-data graph identifies "
                    "a qualified opportunity. RouteGenie and MediRoutes can support dispatch and "
                    "vehicle visibility, but do not assume every subscription exposes the same "
                    "API, webhook, or broker integration. Obtain written interface documentation, "
                    "field definitions, export rights, retention terms, and the relevant business "
                    "associate agreement before transmitting protected health information. Ask "
                    "whether a trip event represents device capture, server receipt, dispatcher "
                    "entry, or a later correction. Each timestamp supports a different audit "
                    "claim. Test an authorized sandbox with a created trip, reassignment, late "
                    "pickup, cancellation, completed leg, and corrected completion. Require "
                    "durable event identifiers and preserve original events when corrections "
                    "arrive. For dispatch telemetry, reducing eight daily status calls by three "
                    "minutes each saves two hours over five operating days; value that at the "
                    "desk's actual labor cost rather than promising staff elimination. If the "
                    "vendor interface fails, retain a secure export and documented telephone "
                    "dispatch procedure with later reconciliation. Do not quietly switch to "
                    "personal messaging accounts. A resilient small desk needs one tested "
                    "manual path, one exception owner, and a clear recovery sequence more "
                    "than it needs a second live map."
                ),
                (
                    "Treat claims and payments as a contract-specific exchange, not a universal "
                    "837P pipeline. Some NEMT arrangements use professional claims with payer "
                    "companion guides; others require a broker portal, proprietary trip file, "
                    "or invoice. Where authorized, an 837P carries claim submissions, a 999 "
                    "reports implementation acknowledgments, a 277CA reports claim acceptance "
                    "status, and an 835 explains remittance adjustments and payment allocation. "
                    "Neither transport-level delivery nor an accepted claim proves payment. "
                    "Stedi can support documented healthcare transaction workflows, while "
                    "Availity access and transaction availability depend on the payer connection "
                    "and product. Keep payer identifiers, control numbers, trip references, "
                    "adjustment codes, and bank reconciliation evidence linked without copying "
                    "full patient details into every table. For claims reconciliation, recovering "
                    "six payable $45 legs from a missing-document queue restores $270 of "
                    "billings; under the illustrative 45% retained-share convention, that "
                    "represents $121.50 before additional overhead, not $270 of profit. A "
                    "corrected submission still needs duplicate detection. When a clearinghouse "
                    "connection is unavailable, use the payer's permitted portal or secure "
                    "file route, retain the submission receipt, and reconcile its identifier "
                    "before the automated connector resumes. Never resubmit blindly because "
                    "a local request timed out."
                ),
                (
                    "Keep routing intelligence separate from medical data. Google Maps Platform "
                    "Routes API can estimate travel times from coordinates without receiving "
                    "patient names, diagnoses, or specimen identifiers. Review current product "
                    "terms before storing results or combining them with other map products. "
                    "For specimen custody, a Zebra scanner can capture a laboratory-issued "
                    "barcode into an approved application, but the scanner itself does not "
                    "establish chain of custody. Record the authorized pickup, handoff, "
                    "temperature evidence where required, receiving acceptance, and exception "
                    "resolution. One missed $80 STAT collection can also cause a redraw, "
                    "contract penalty, or lost account; those consequences need their own "
                    "evidence rather than an invented multiplier. Classification controls "
                    "packaging: DOT's Category B provisions in 49 CFR 173.199 do not cover "
                    "every infectious substance or every specimen shipment. Separate commercial "
                    "acquisition telemetry as well. Twilio or Ringba may meter inbound business "
                    "calls, but call metadata and recordings can expose sensitive information. "
                    "Use nonclinical routing scripts, minimize retained content, and verify "
                    "the specific vendor services eligible for the required agreement. If "
                    "navigation or scanning fails, use an approved route sheet and numbered "
                    "custody record, then reconcile the delayed events without fabricating "
                    "GPS fixes or original scan times."
                ),
            ],
            "table": {
                "caption": "Permissioned Tool Directory, Sources 10–18: Contracted Interfaces and Operational Fallbacks",
                "headers": [
                    "Named tool and exact access",
                    "Operator decision and evidence produced",
                    "Cost tier and purchasing boundary",
                    "Refresh latency and freshness test",
                    "Rate-limit hygiene and fallback source",
                ],
                "rows": [
                    [
                        "RouteGenie: request a licensed demonstration and documented integration access through https://routegenie.com/.",
                        "Connect authorized trip assignments and vehicle events while preserving original timestamps and correction history.",
                        "Commercial subscription and integration pricing require a written quote; include onboarding and interface support costs.",
                        "Measure actual device-to-server event delay during acceptance testing; offline devices can upload events much later.",
                        "Follow the contracted interface limits and retry guidance; fall back to permitted exports and secure dispatcher procedures.",
                    ],
                    [
                        "MediRoutes: obtain licensed access and confirm available integration documentation through https://mediroutes.com/.",
                        "Verify trip lifecycle events and broker-specific connections instead of assuming dashboard fields are available through automation.",
                        "Commercial licensing depends on the purchased arrangement; obtain line items for integrations, training, and support.",
                        "Test event availability against dispatcher timestamps; a displayed vehicle position can be older than the screen refresh.",
                        "Use only vendor-authorized connectors and bounded polling; maintain a tested secure export and telephone-dispatch fallback.",
                    ],
                    [
                        "Stedi: review healthcare API documentation at https://www.stedi.com/docs/ and obtain authorized payer connectivity.",
                        "Track supported eligibility, claims, and remittance workflows with payer-specific identifiers and durable transaction receipts.",
                        "Commercial usage pricing and payer connection requirements vary; calculate charges from the intended transaction mix.",
                        "Delivery and payer-response latency are separate measurements; acceptance messages do not establish payment timing.",
                        "Apply documented limits, backoff, and deduplication controls; use the contracted payer portal when that route is permitted.",
                    ],
                    [
                        "Availity Essentials: register through https://www.availity.com/ and verify the specific payer and product connection.",
                        "Check supported eligibility and claim-status functions without assuming every payer accepts the same electronic transactions.",
                        "Some payer-sponsored portal functions have no provider charge; premium products and integrations have separate commercial terms.",
                        "Record payer response timestamps and search time; portal availability does not make an older response current.",
                        "Respect account permissions and published interface terms; use the payer's own authorized channel for unavailable transactions.",
                    ],
                    [
                        "Google Maps Platform Routes API: enable the product and use documented methods at https://developers.google.com/maps/documentation/routes.",
                        "Estimate route duration using coordinates while excluding patient identities and clinical details from requests.",
                        "Usage-based SKU pricing and available allowances change; set billing alerts and compare costs against measured planning savings.",
                        "Traffic-aware results describe a requested departure context; cache only where current product terms permit storage.",
                        "Set project quotas and bounded retries; use dispatch-approved route sheets when the service is unavailable.",
                    ],
                    [
                        "Twilio Programmable Voice: use authenticated APIs and signed webhooks documented at https://www.twilio.com/docs/voice.",
                        "Measure business-line routing and qualifying call durations without placing clinical information in acquisition event records.",
                        "Usage charges include numbers, minutes, and selected features; validate current rates for the actual call geography.",
                        "Webhooks arrive asynchronously and can be retried; reconcile event receipt times with final call status.",
                        "Verify signatures and honor concurrency limits; route failures to a staffed business line and reconcile call records.",
                    ],
                    [
                        "Ringba: configure a licensed account and request supported routing and reporting interfaces through https://www.ringba.com/.",
                        "Route commercial service calls using buyer availability, duration rules, dispute evidence, and funded buyer balances.",
                        "Commercial platform and telephony costs depend on the agreement; require explicit pricing for every billable component.",
                        "Live routing and finalized reporting can differ; reconcile answered duration and reversals before issuing buyer statements.",
                        "Use documented account limits and duplicate-event controls; suspend buyer routing when balances or reporting become unreliable.",
                    ],
                    [
                        "Zebra DataWedge: configure supported Android scanners using documentation at https://techdocs.zebra.com/datawedge/.",
                        "Deliver barcode scans into an approved custody application with validated symbologies and authenticated operator identity.",
                        "Compatible hardware and application development create costs; confirm DataWedge availability for the selected device model.",
                        "Local scans can occur immediately while synchronization is delayed; preserve device time and server receipt separately.",
                        "Debounce duplicate scans and queue offline events; use numbered custody forms under the laboratory's approved procedure.",
                    ],
                    [
                        "FMCSA SAFER Company Snapshot: search authorized carrier records through https://safer.fmcsa.dot.gov/.",
                        "Check applicable USDOT carrier identity and displayed operating information without assuming every NEMT operator needs federal registration.",
                        "Public snapshot searches are free; insurance and state passenger-carrier requirements need additional authoritative verification.",
                        "Inspect displayed record and update dates; a snapshot does not establish real-time insurance or operating eligibility.",
                        "Use permitted searches without bulk scraping; consult FMCSA Licensing and Insurance and applicable state regulator records.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify the evidence path before the first live assignment",
                "body": "A successful connection test is insufficient unless the desk can prove authorization, event integrity, and recovery.",
                "items": [
                    "Confirm the payer or broker accepts the selected submission channel and document required enrollment, companion-guide rules, and submission identifiers.",
                    "Execute required business associate agreements and verify that the exact purchased services, accounts, and subprocessors fit the protected-data workflow.",
                    "Replay cancellation, duplicate webhook, reassignment, delayed GPS, and corrected completion cases using synthetic records before loading live trips.",
                    "Demonstrate secure manual dispatch, numbered specimen custody, credential rechecks, and payment reconciliation during a simulated vendor outage.",
                ],
            },
        },
        {
            "heading": "3. Engineer the pipeline around lineage, bounded retries, and auditable exceptions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement a narrow pipeline with separate discovery, eligibility, operations, "
                    "and settlement domains. A small authorized service can use Python's urllib "
                    "for documented HTTPS endpoints, csv for source exports, sqlite3 for staging, "
                    "hashlib for content fingerprints, and logging for redacted diagnostics. "
                    "Those modules do not supply encrypted storage or a complete healthcare "
                    "security program; deploy them within managed access controls, encrypted "
                    "storage, backups, and monitored infrastructure appropriate to the records. "
                    "Keep credentials outside source files and never print authorization headers "
                    "or patient payloads. Assign internal facility, contract, trip, specimen, "
                    "and settlement identifiers rather than joining on display names. Preserve "
                    "raw source snapshots under restricted access, then normalize into versioned "
                    "records with source lineage. A facility relocation should create a new "
                    "location version, not silently rewrite historical trip evidence. For "
                    "credential verification, checking twenty contractors at six minutes each "
                    "takes two hours; resolving only four changed records can reduce repetitive "
                    "review, but cannot replace mandated checks. Model valid-from and valid-to "
                    "dates, reviewer identity, and evidence references. If the authoritative "
                    "source is unavailable when a required credential expires, prevent assignment "
                    "under that credential and move the work to an independently verified "
                    "operator rather than extending the date locally."
                ),
                (
                    "Design ingestion as at-least-once delivery with controlled deduplication. "
                    "For public files, store the source URL, retrieval timestamp, release date, "
                    "byte count, checksum, and parser version. Reject a supposed CSV download "
                    "when its content is an HTML login page. For vendor events, deduplicate "
                    "by vendor account and event identifier, retaining payload hashes to "
                    "detect conflicting reuse. Where identifiers are absent, agree a composite "
                    "key with the vendor; timestamp rounding alone can collapse distinct "
                    "handoffs. Respect Retry-After when supplied, use exponential backoff with "
                    "jitter for transient failures, and stop retrying authentication or "
                    "permission failures until configuration is corrected. A payment submission "
                    "timeout belongs in a reconciliation queue because retrying a non-idempotent "
                    "operation can create a duplicate. For exclusion screening, a local monthly "
                    "LEIE index can narrow candidate matches across fifty roster records, but "
                    "official identity verification remains necessary for plausible matches. "
                    "Track match status separately from assignment eligibility. Quarantine "
                    "schema changes rather than shifting columns by position. If a source "
                    "adds a new identifier field or changes date formatting, preserve the "
                    "original file and route a small sample to review. Restart from a "
                    "committed checkpoint only after counts and identifiers reconcile."
                ),
                (
                    "Make diagnostics operationally legible: each alert needs an affected "
                    "contract, a last-good timestamp, an owner, and a concrete next action. "
                    "Track discovery-file age, credential expirations, unmatched trip events, "
                    "unacknowledged submissions, unpaid accepted claims, and custody exceptions "
                    "as separate queues. A green HTTP response cannot clear any of them by "
                    "itself. Use synthetic records to test daylight-saving transitions, "
                    "time-zone offsets, repeated barcodes, split outbound and return legs, "
                    "and assignments crossing midnight. Store timestamps with offsets and "
                    "retain the original device value; do not overwrite an implausible clock "
                    "reading with a cleaner invented event. For dispatch evidence, compare "
                    "GPS sample age against the contract's verification requirement rather "
                    "than declaring a universal tolerance. For specimen custody, link each "
                    "handoff to an authorized receiving identity and record temperature "
                    "requirements supplied by the laboratory. OSHA's bloodborne-pathogens "
                    "standard applies according to occupational exposure, while DOT packaging "
                    "requirements depend on shipment classification. For independent owner-operators, "
                    "contract labels alone do not establish worker status; scheduling, control, "
                    "equipment, and state-specific tests require operational review. When "
                    "telemetry is missing, document the exception and seek the contract's "
                    "permitted alternative evidence instead of backfilling a fictional route."
                ),
            ],
            "table": {
                "caption": "Diagnostic Runbook: Four Failure Classes With Evidence-Preserving Recovery",
                "headers": [
                    "Failure class and detection test",
                    "Specific evidence to retain",
                    "Bounded response and accountable owner",
                    "Recovery condition and verification method",
                ],
                "rows": [
                    [
                        "A public download returns success but contains HTML instead of the expected structured records.",
                        "Retain response metadata, file checksum, retrieval timestamp, parser version, and a redacted format sample.",
                        "The data owner pauses publication, checks the official distribution page, and retrieves the permitted replacement.",
                        "Resume only after expected columns, record counts, and sampled identifiers reconcile against the source release.",
                    ],
                    [
                        "A trip completion arrives twice with the same vendor event identifier but different recorded mileage.",
                        "Preserve both payload hashes, account identifier, receipt times, original device timestamps, and the vendor correction reference.",
                        "The dispatch lead quarantines settlement changes and asks the authorized vendor contact to explain event precedence.",
                        "Release settlement only after the correction chain identifies the accepted mileage and retains the superseded record.",
                    ],
                    [
                        "A submitted claim has no local acknowledgment because the network request timed out after transmission.",
                        "Retain control numbers, payload fingerprint, transmission timestamp, payer connection, and the transport error without patient logs.",
                        "The receivables owner queries the authorized status channel before deciding whether any resubmission is necessary.",
                        "Resume automated submission only when the existing transaction is located or the payer confirms safe corrective handling.",
                    ],
                    [
                        "A specimen reaches the laboratory without a synchronized pickup scan or with an unresolved temperature excursion.",
                        "Retain the numbered backup record, handler identities, laboratory instructions, temperature evidence, and receiving disposition.",
                        "The custody lead contacts the laboratory immediately and follows its handling instructions without inventing missing events.",
                        "Close the exception only after laboratory disposition and reconciled custody evidence are attached to the shipment record.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and permitted purpose",
                    "action": "Create a source record before connecting any portal, file feed, or commercial endpoint.",
                    "detail": "Record the owner, access method, contract authority, data classification, refresh expectation, spending limit, and manual fallback.",
                },
                {
                    "step": 2,
                    "title": "Land immutable evidence and validate structure",
                    "action": "Retrieve through an authorized channel, fingerprint the payload, and validate its format before normalization.",
                    "detail": "Preserve release and retrieval timestamps separately; reject login pages, unexpected columns, duplicate identifiers, and impossible event dates.",
                },
                {
                    "step": 3,
                    "title": "Resolve identities and publish bounded decisions",
                    "action": "Join verified identifiers and publish only records that satisfy the specific operating decision's freshness requirement.",
                    "detail": "Send ambiguous facilities, possible exclusions, expired credentials, and conflicting trip corrections to named reviewers rather than silently accepting matches.",
                },
                {
                    "step": 4,
                    "title": "Reconcile downstream evidence and exercise recovery",
                    "action": "Compare assignments, completed events, custody receipts, submissions, remittances, and bank activity on the operating cadence.",
                    "detail": "Test a vendor outage with synthetic records, document manual actions, and verify that recovery creates neither duplicate claims nor duplicate driver payments.",
                },
            ],
        },
        {
            "heading": "4. Price the information edge against retained contribution and cash timing",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep the scorecard's denominators visible in every dashboard. Conservative "
                    "gross billings of $250,000 produce $137,500 of driver settlements and "
                    "$112,500 retained dispatch revenue at 45%; $82,500 of remaining costs "
                    "leave $30,000 owner profit. Base billings of $925,000 produce $508,750 "
                    "of settlements and $416,250 retained revenue; $249,750 of remaining "
                    "costs leave $166,500 profit. Scaled billings of $1,600,000 produce "
                    "$880,000 of settlements and $720,000 retained revenue; $336,000 of "
                    "remaining costs leave $384,000 profit. Those profits equal 12%, 18.0%, "
                    "and 24% of gross billings, or 26.67%, 40.0%, and 53.33% of retained "
                    "revenue. Under this scorecard's ASC 606 net-presentation convention, "
                    "retain the $112,500–$720,000 range as recognized dispatch revenue; "
                    "actual principal-versus-agent conclusions depend on contractual control. "
                    "Do not label underlying client collections, medical charges, or all "
                    "driver pass-throughs as operator revenue. Team counts remain 2 FT + "
                    "2 C, 2 FT + 2 C, and 3 FT + 3 C. The supplied $3,500–$18,000 "
                    "monthly operating range is not a replacement for these full annual "
                    "residual costs; its narrower expense scope must be documented before "
                    "comparing either figure with a vendor quote."
                ),
                (
                    "Treat acquisition tooling as a separate application with its own economics "
                    "and healthcare boundaries. The mapped TRACK_2 play "
                    "rank_and_rent_pay_per_call_routing builds local foundation-repair, water-restoration, "
                    "probate-liquidation, and commercial-roofing hubs, then routes qualifying "
                    "calls through Ringba or Twilio. Its supplied price band is $75–$300 "
                    "per inbound call lasting over ninety seconds. At twenty accepted calls "
                    "and $125 each, gross call fees are $2,500; an illustrative $650 "
                    "traffic-and-telephony cost and $250 dispute allowance leave $1,600 "
                    "before labor, overhead, and taxes. This is a separate acquisition "
                    "example, not an addition to the canonical NEMT scenarios. For a "
                    "healthcare logistics desk, reuse the routing instrumentation and business "
                    "inquiry triage, not an automatic per-patient referral fee. Remuneration "
                    "for federal healthcare program referrals can implicate 42 U.S.C. "
                    "1320a-7b(b); a ninety-second call rule does not resolve that issue. "
                    "Maintain organic city and calculator pages as a traffic fallback "
                    "independent of a Google Business Profile suspension, while recognizing "
                    "that organic rankings still fluctuate. Verify Maps listings only with "
                    "genuine eligible partner locations. Require prepaid auto-refill wallets "
                    "for the separate commercial buyers and pause routing when a funded "
                    "balance cannot cover the agreed qualifying-call charge."
                ),
                (
                    "Buy tools against measured cash effects, then stress-test settlement timing. "
                    "An illustrative $600 monthly integration requires $1,333.33 in additional "
                    "gross billings to recover its fee at a 45% retained share, before "
                    "incremental overhead; use $1,334 as a rounded planning threshold. Count "
                    "recoveries only when they would otherwise have been lost, and do not "
                    "double-count faster collection as additional revenue. At Base annual "
                    "billings, a steady-state forty-five-day collection interval represents "
                    "approximately $114,041 of gross receivables using a 365-day year. "
                    "Forty-five days of driver settlements alone represent approximately "
                    "$62,723; weekly payouts, denials, payroll, and reserves determine the "
                    "actual funding need. That illustrates why the supplied $15,000–$65,000 "
                    "startup range can become tight before the first two-to-five-month deal "
                    "cycle produces reliable cash. Negotiate settlement terms and stage route "
                    "growth instead of financing expansion through overdue driver payments. "
                    "Review tools after thirty days of measured operation: verified prospect "
                    "cost, prevented duplicate payments, recovered payable trips, custody "
                    "exceptions, and days to cash. Keep a tool when attributable retained "
                    "benefit exceeds its subscription, integration, review labor, and failure "
                    "recovery costs. Retire it when exports and a controlled manual process "
                    "produce the same evidence more economically."
                ),
            ],
            "table": {
                "caption": "Economic Control Matrix: Canonical Cases and a Separate Tool-Purchase Test",
                "headers": [
                    "Case and fixed operating scale",
                    "Gross billings and settlement bridge",
                    "Retained revenue and residual operating costs",
                    "Owner profit and decision boundary",
                ],
                "rows": [
                    [
                        "Conservative case uses two full-time staff and two contractors under the supplied scorecard.",
                        "$250,000 annual gross billings less $137,500 driver settlements produces the fixed 45% retained share.",
                        "$112,500 retained dispatch revenue less $82,500 remaining annual costs preserves the canonical operating bridge.",
                        "$30,000 owner profit equals 12% of gross billings and 26.67% of retained dispatch revenue.",
                    ],
                    [
                        "Base case uses two full-time staff and two contractors without changing the scorecard headcount.",
                        "$925,000 annual gross billings less $508,750 driver settlements produces the fixed 45% retained share.",
                        "$416,250 retained dispatch revenue less $249,750 remaining annual costs preserves the canonical operating bridge.",
                        "$166,500 owner profit equals 18.0% of gross billings and 40.0% of retained dispatch revenue.",
                    ],
                    [
                        "Scaled case uses three full-time staff and three contractors, totaling six people in the scorecard.",
                        "$1,600,000 annual gross billings less $880,000 driver settlements produces the fixed 45% retained share.",
                        "$720,000 retained dispatch revenue less $336,000 remaining annual costs preserves the canonical operating bridge.",
                        "$384,000 owner profit equals 24% of gross billings and 53.33% of retained dispatch revenue.",
                    ],
                    [
                        "Illustrative tool test evaluates one $600 monthly integration separately from the canonical case totals.",
                        "At 45% retained share, approximately $1,333.33 additional monthly billings covers only the stated subscription expense.",
                        "Add implementation labor, exception review, storage, and recovery costs before calculating the actual purchasing threshold.",
                        "Authorize renewal only when attributable retained benefit exceeds total incremental costs without counting existing collections twice.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The information edge is the shortest defensible path from a dated source record to a paid, fully evidenced trip.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Build a forty-facility prospect register joining NPI, CLIA where applicable, physical service location, contracting entity, and dated source evidence.",
        "Document access, pricing, freshness, permitted automation, and a tested fallback for each of the eighteen directory sources before connecting it.",
        "Run synthetic trip, custody, cancellation, correction, duplicate-event, and submission-timeout tests through the selected authorized interfaces.",
        "Separate protected operational records from public prospecting data and verify required agreements, access roles, encryption, and redacted logging.",
        "Reconcile gross billings, 55% driver settlements, 45% retained dispatch revenue, remaining costs, and owner profit to all three canonical scenarios.",
        "Measure thirty days of recovered payable work, prevented duplicates, collection timing, and exception labor before renewing commercial tools or expanding routes.",
    ],
    "statutory_citations": [
        {
            "title": "45 CFR 164.502(e) and 164.504(e) — Business associate arrangements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": "Define required contractual safeguards for applicable business associate relationships before sharing protected trip, patient, or specimen information.",
        },
        {
            "title": "45 CFR 164.312 — HIPAA technical safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312",
            "relevance": "Map applicable access control, audit control, integrity, authentication, and transmission-security requirements to the operational data pipeline.",
        },
        {
            "title": "42 CFR 431.53 — Assurance of transportation",
            "url": "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-431/subpart-B/section-431.53",
            "relevance": "Establishes the Medicaid state-plan transportation assurance; it does not replace state enrollment, broker contracting, or trip authorization requirements.",
        },
        {
            "title": "42 CFR 455.436 — Federal database checks",
            "url": "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-455/subpart-E/section-455.436",
            "relevance": "Specifies state Medicaid agency database-check obligations, including recurring exclusion checks; operators must also implement applicable state and contractual screening duties.",
        },
        {
            "title": "42 U.S.C. 1320a-7b(b) — Illegal remunerations",
            "url": "https://www.law.cornell.edu/uscode/text/42/1320a-7b",
            "relevance": "Explains why commercial pay-per-call acquisition economics cannot automatically be transferred to referrals involving federal healthcare program business.",
        },
        {
            "title": "29 CFR 1910.1030 — Bloodborne pathogens",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1030",
            "relevance": "Apply exposure controls, training, protective measures, and related employer duties where the work creates occupational exposure.",
        },
        {
            "title": "49 CFR 173.199 — Category B infectious substances",
            "url": "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-C/part-173/subpart-E/section-173.199",
            "relevance": "Use the applicable classification, packaging, marking, and handling provisions for Category B shipments rather than treating every specimen as interchangeable.",
        },
        {
            "title": "California Labor Code section 2775 — Worker classification framework",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2775.",
            "relevance": "Evaluate the applicable California classification framework and relevant exceptions before assuming an owner-operator agreement establishes independent-contractor status.",
        },
        {
            "title": "42 CFR 493.3 — CLIA applicability",
            "url": "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-493/subpart-A/section-493.3",
            "relevance": "Distinguish laboratory certification scope from courier permissions and laboratory-specific specimen transport instructions.",
        },
    ],
}
