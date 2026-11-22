from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small insurance restoration desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "NWS Event Feeds, Parcel and Permit Records, IICRC Drying Evidence, Xactimate Scope Controls, and License-Safe Collections",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #15, Insurance Restoration, ranks #29 with a 54/100 Money-to-Manpower "
        "Score because field labor, working capital, and disputed invoices constrain "
        "software leverage. This chapter maps five operator plays: storm triage, water "
        "mitigation, fire and contents recovery, mold remediation, and reconstruction "
        "with documented supplements and collections. Build one evidence pipeline around "
        "public hazard feeds, parcel and permit verification, licensed counterparties, "
        "instrument readings, and job-cost exports. The canonical annual owner profits "
        "are $40,000 Conservative, $195,000 Base, and $450,000 Scaled, on gross restoration "
        "billings rather than insured property values or claim reserves. A five-employee, "
        "six-contractor pod needs fewer duplicate entries and stronger evidence, not "
        "another dashboard. Every proposed connector must improve dispatch, photo "
        "documentation, or job-cost tracking without assuming authority to negotiate coverage."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "8% net margin; $40,000 annual owner net profit; 5 FT + 6 C",
        },
        {
            "label": "Base",
            "value": "$1,500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "13.0% net margin; $195,000 annual owner net profit; 5 FT + 6 C",
        },
        {
            "label": "Scaled",
            "value": "$2,500,000",
            "context": "Annual gross restoration billings; subcontractor and material costs included in margin",
            "note": "18% net margin; $450,000 annual owner net profit; 6 FT + 7 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an eighteen-source directory around five executable plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Give every source a job before buying access. For this chapter, map "
                    "the five operating plays as P1 storm triage, P2 water mitigation, "
                    "P3 fire and contents recovery, P4 mold remediation, and P5 reconstruction "
                    "with documented supplements and collections. These are workflow assignments, "
                    "not five additional revenue lines. P1 consumes weather alerts, event "
                    "footprints, and service-area parcels; P2 combines an authorized intake "
                    "with moisture evidence and available equipment; P3 needs incident "
                    "context, inventories, and chain of custody; P4 needs qualified assessment, "
                    "containment planning, and jurisdiction-specific licensing; P5 joins permits, "
                    "estimate versions, costs, and invoice evidence. Assign the five full-time "
                    "positions to a dispatcher, estimator, project manager, and two field "
                    "leads. Treat the six contractors as scheduled capacity with verified "
                    "skills, not six interchangeable people available continuously. The dispatcher "
                    "owns public-feed exceptions, the estimator owns scope provenance, and "
                    "the project manager owns access permissions and job-cost reconciliation. "
                    "Field leads collect measurements and supervise site execution. This "
                    "division prevents an eleven-person pod from appointing an imaginary "
                    "data department. Start with the sources that change today's dispatch "
                    "or strengthen an existing authorized job; defer everything that merely "
                    "produces a larger prospect spreadsheet."
                ),
                (
                    "Separate event intelligence from property evidence. A National Weather "
                    "Service alert describes a hazard area and time window; it does not "
                    "establish damage at a particular address. NOAA radar-derived hail "
                    "signatures, preliminary reports, and later Storm Events records have "
                    "different evidentiary strength and publication delays. Keep those distinctions "
                    "in the record rather than presenting every layer as verified hail "
                    "impact. FEMA declarations identify eligible jurisdictions and incident "
                    "periods, while flood maps describe mapped hazards; neither determines "
                    "an individual policy's coverage. County parcel records help resolve "
                    "addresses and ownership references, but an assessor entry is not proof "
                    "that an occupant may authorize work. Obtain that authority directly. "
                    "Permit searches inform reconstruction sequencing without proving that "
                    "concealed conditions satisfy current code. Public fire reports, where "
                    "available through the relevant agency's records process, may arrive "
                    "after operational decisions and may contain redactions. Never substitute "
                    "public narrative for a site safety assessment. Use the directory as "
                    "a routing system: each observation carries its source, retrieval time, "
                    "geographic resolution, and operational purpose. A storm polygon can "
                    "justify staging equipment near existing customers; it cannot justify "
                    "asserting that every enclosed roof requires replacement or that an "
                    "insurer owes payment."
                ),
                (
                    "Maintain a source register beside the directory. For each connector, "
                    "record the official documentation location, permitted use, authentication "
                    "method, account owner, last successful retrieval, observed delay, and "
                    "tested fallback. The access descriptions below identify public entry "
                    "points and vendor-controlled integration routes; commercial prices, account "
                    "entitlements, and numerical request ceilings must come from the current "
                    "contract or service documentation. Do not manufacture a universal "
                    "requests-per-minute figure. Distinguish free public access from the labor "
                    "cost of cleaning records and from fees for certified copies. Store "
                    "event time separately from publication time and ingestion time so an "
                    "old event arriving today cannot trigger a fresh dispatch surge. For "
                    "licensed commercial platforms, confirm whether API access includes your "
                    "subscription before designing around it. A supported CSV export is "
                    "often sufficient for an eleven-person operation and easier to reconcile "
                    "than an undocumented integration. Cache stable parcel attributes, refresh "
                    "license status before assignment, and expire alerts according to their "
                    "own timestamps. Track outages visibly. When a feed fails, label its "
                    "data stale and switch to its named fallback instead of silently "
                    "reusing yesterday's observations as current operating intelligence."
                ),
            ],
            "table": {
                "caption": "Eighteen-Source Restoration Directory: Access, Commercial Terms, Latency, Throttling, and Fallbacks",
                "headers": [
                    "Named source and operational purpose",
                    "Exact access route or supported method",
                    "Cost tier and refresh characteristics",
                    "Rate-limit and retrieval discipline",
                    "Fallback and evidence boundary",
                ],
                "rows": [
                    [
                        "NWS API supplies P1 hazard alerts for assigned service territories.",
                        "GET https://api.weather.gov/alerts/active with documented area or point filters.",
                        "Free public service; alerts update as forecasters issue changes.",
                        "Send an identifying User-Agent; cache responses and back off on throttling.",
                        "Use weather.gov local office pages; alerts do not establish property damage.",
                    ],
                    [
                        "NOAA SWDI provides P1 radar-derived and reported severe-weather observations.",
                        "Use https://www.ncei.noaa.gov/swdiws/ and select documented dataset query formats.",
                        "Free public access; ingestion delay varies by observation dataset.",
                        "Request bounded dates and geography; persist completed responses locally.",
                        "Consult NWS local storm reports; radar signatures require careful interpretation.",
                    ],
                    [
                        "NOAA Storm Events supports retrospective P1 event and timeline checks.",
                        "Download yearly files from https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/ using listed filenames.",
                        "Free bulk files; publication and revisions lag immediate storm response.",
                        "Retrieve directory metadata first; download only changed annual files.",
                        "Use current NWS reports for operations; retain later revisions separately.",
                    ],
                    [
                        "OpenFEMA declarations establish P1 disaster geography and official incident periods.",
                        "Query https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries with documented filters and pagination.",
                        "Free public endpoint; declaration records change as FEMA publishes updates.",
                        "Limit returned fields and pages; checkpoint pagination and retry transient failures.",
                        "Check FEMA disaster pages; declaration status does not establish insurance coverage.",
                    ],
                    [
                        "FEMA NFHL supports P2 flood-hazard context and reconstruction planning.",
                        "Use https://msc.fema.gov/portal/home or the official NFHL ArcGIS service.",
                        "Free public viewing; effective map revisions follow formal publication cycles.",
                        "Honor ArcGIS service capabilities; cache map references and effective dates.",
                        "Request local floodplain records; mapped risk does not prove loss causation.",
                    ],
                    [
                        "USGS Water Data provides P2 nearby gauge trends and flood context.",
                        "Use https://waterdata.usgs.gov/ and its linked documented machine-access services.",
                        "Free observations; station intervals and telemetry delays vary by location.",
                        "Query only relevant stations; follow current API migration and quota documentation.",
                        "Consult local emergency management; river gauges cannot measure indoor water depth.",
                    ],
                    [
                        "King County eReal Property illustrates authoritative parcel and ownership lookup.",
                        "Search https://blue.kingcounty.gov/Assessor/eRealProperty/default.aspx by supported parcel or address fields.",
                        "Free browser lookup; assessment and ownership posting follow county workflows.",
                        "Use permitted exports for bulk work; avoid automating protected browser forms.",
                        "Use the subject county assessor and recorder outside King County.",
                    ],
                    [
                        "Miami-Dade building services illustrate P5 permit and inspection verification.",
                        "Open https://www.miamidade.gov/global/economy/building/home.page and follow permit-record search links.",
                        "Public search access; document-copy charges and posting delays vary.",
                        "Use portal-supported searches; never bypass session controls or access restrictions.",
                        "Contact the actual permitting jurisdiction, including separately administered municipalities.",
                    ],
                    [
                        "Florida DBPR verifies contractors and applicable mold-related professional licenses.",
                        "Use the license search linked from https://www.myfloridalicense.com/ for individual records.",
                        "Free public lookup; updates follow licensing and enforcement processing.",
                        "Perform targeted checks before assignment; retain dated results without bulk scraping.",
                        "Contact the licensing board when names, categories, or status conflict.",
                    ],
                    [
                        "Florida DFS verifies adjuster credentials when a separate licensed role exists.",
                        "Search https://licenseesearch.fldfs.com/ using supported individual or agency identifiers.",
                        "Free public lookup; appointments and license status reflect agency updates.",
                        "Check the relevant license and appointment fields through supported searches.",
                        "Request agency confirmation; contractor registration never substitutes for adjusting authority.",
                    ],
                    [
                        "EPA ECHO provides P3 industrial-site environmental enforcement context.",
                        "Use https://echo.epa.gov/tools/web-services and documented facility-search service parameters.",
                        "Free public services; freshness depends on contributing environmental programs.",
                        "Filter facilities narrowly; record source-system dates and service response limits.",
                        "Consult state environmental records; facility history does not characterize residential debris.",
                    ],
                    [
                        "EPA RRP resources support P5 lead-safe renovation firm verification.",
                        "Open https://www.epa.gov/lead and follow certified renovation firm search links.",
                        "Free directory access; certification changes follow EPA or authorized-state processing.",
                        "Search specific firms; check authorized-state directories where those programs apply.",
                        "Obtain current certificates and training records; directory presence alone is insufficient.",
                    ],
                    [
                        "OSHA establishment search informs contractor diligence and recurring safety concerns.",
                        "Search https://www.osha.gov/ords/imis/establishment.html using employer and location filters.",
                        "Free public search; inspection records may change during case processing.",
                        "Use focused searches; preserve inspection identifiers and current case status.",
                        "Review state-plan records and direct safety documentation before making assignments.",
                    ],
                    [
                        "Verisk Xactimate and XactAnalysis support P5 estimating and assignment documentation.",
                        "Use licensed application exports; request supported integrations through Verisk account channels.",
                        "Paid subscription or contract; exports reflect saved estimates and synchronization.",
                        "Use entitled interfaces only; throttle according to the executed integration agreement.",
                        "Retain estimate PDFs and supported exports; line items do not establish coverage.",
                    ],
                    [
                        "Encircle supports P2 moisture records and P3 documented contents workflows.",
                        "Use licensed workspace exports or vendor-enabled API access for your account.",
                        "Paid product; API entitlement requires confirmation and uploads depend on connectivity.",
                        "Queue uploads and follow vendor limits; reconcile attachments after mobile synchronization.",
                        "Use structured field forms and original photographs during connectivity failures.",
                    ],
                    [
                        "CompanyCam supports timestamped project photography across all five operating plays.",
                        "Use the vendor developer portal and account-authorized documented project interfaces.",
                        "Paid account; integration availability and photo arrival depend on plan and synchronization.",
                        "Respect documented quotas; deduplicate uploads and retry failed attachment transfers.",
                        "Retain original local captures and a job-linked photo manifest.",
                    ],
                    [
                        "QuickBooks Online supports P5 invoice, supplier-cost, and payment reconciliation.",
                        "Use Intuit OAuth and https://quickbooks.api.intuit.com/v3/company/{realmId}/ with documented resources.",
                        "Paid accounting subscription; API and webhook activity follows recorded transactions.",
                        "Honor current Intuit limits and retry guidance; deduplicate webhook events.",
                        "Reconcile supported accounting exports against bank activity and supplier statements.",
                    ],
                    [
                        "Twilio Lookup checks customer-provided telephone formatting and subscribed line intelligence.",
                        "Call https://lookups.twilio.com/v2/PhoneNumbers/{PhoneNumber} using authorized account credentials.",
                        "Field-specific pricing applies; request current terms before enabling paid enrichments.",
                        "Cache necessary results briefly; respect account limits and minimize retained attributes.",
                        "Confirm contact details directly; lookup results never establish permission to market.",
                    ],
                ],
            },
        },
        {
            "heading": "2. Build a permissioned enrichment waterfall instead of a prospect-harvesting machine",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start the waterfall with an authorized service inquiry, an existing "
                    "customer relationship, or an internally defined service-area monitoring "
                    "task. Normalize the supplied address without replacing the original "
                    "entry, then resolve the jurisdiction and candidate parcel. Match on "
                    "multiple attributes: street number, normalized street, unit, municipality, "
                    "and parcel geometry where available. Shared driveways, condominium "
                    "master parcels, and recently subdivided lots require human review. "
                    "Next attach hazard context with an explicit spatial relationship and "
                    "event interval, not a binary damaged-property flag. Retrieve permits "
                    "only when reconstruction planning needs them, and verify the licenses "
                    "of the actual assigned firms rather than similarly named businesses. "
                    "Use contact enrichment last and only for a defined operational "
                    "purpose. Twilio Lookup can validate a customer-provided number's format "
                    "and return purchased intelligence; it does not identify the property's "
                    "decision-maker or create permission for automated outreach. Avoid people-search "
                    "waterfalls that infer residents from disaster footprints. Applicable "
                    "47 CFR 64.1200 requirements depend on the communication technology, "
                    "purpose, and consent facts. The dispatcher should see a small "
                    "exception queue containing unresolved addresses, stale credentials, and "
                    "missing authorization. They should not receive thousands of speculative "
                    "leads that the field pod cannot service."
                ),
                (
                    "Use a compact data model that survives vendor changes. The core "
                    "entities are job, property, event, party, authorization, observation, "
                    "document, estimate version, cost entry, invoice, and payment. Give "
                    "each an internal identifier; keep vendor identifiers in a separate "
                    "mapping table so a software migration does not rewrite job history. "
                    "A source observation needs source URL or resource identifier, retrieval "
                    "time, event time, source revision, geographic precision, and the raw "
                    "payload reference. Documents need their original filename, capture "
                    "time when available, uploader, job association, and cryptographic digest. "
                    "A digest detects later byte changes; it does not prove that a "
                    "photograph depicts the claimed location. Build connectors with Python "
                    "stdlib urllib.request, json, csv, sqlite3, hashlib, and logging when "
                    "a small local prototype is sufficient. Keep production credentials "
                    "in a managed secret store, never the SQLite database or exports. "
                    "Use explicit connect and read timeouts supported by the chosen "
                    "client, bounded retry attempts, randomized backoff, and idempotent writes. "
                    "For concurrency beyond a single local operator, use a managed database "
                    "and tested backups rather than sharing a live SQLite file through "
                    "a consumer synchronization folder."
                ),
                (
                    "Design failure handling around money and field safety, not uptime "
                    "vanity. Poll hazard feeds at a documented, service-appropriate cadence, "
                    "but let the provider's caching guidance and response headers govern "
                    "actual retrieval. On HTTP 429, honor Retry-After when present; on "
                    "authentication failure, stop the connector and alert its owner instead "
                    "of repeatedly submitting credentials. Paginate deterministically and preserve "
                    "a checkpoint only after the local transaction commits. For webhook "
                    "integrations, verify the vendor's documented authentication mechanism, "
                    "persist the event identifier, acknowledge promptly, and process through "
                    "an idempotent worker. Treat duplicate delivery and out-of-order updates "
                    "as normal conditions. A payment webhook must not erase a newer "
                    "accounting adjustment merely because it arrived later. Route unrecoverable "
                    "records to a review queue with source, attempted operation, and a "
                    "safe error message that excludes credentials and unnecessary personal "
                    "data. Set different freshness tolerances for weather, licenses, parcels, "
                    "and costs. A stale parcel description might permit scheduling after "
                    "direct confirmation; an unresolved electrical hazard cannot be cleared "
                    "by a successful API response. The dispatcher owns daily exceptions, "
                    "while the project manager reviews unresolved monetary mismatches before "
                    "the next collection contact."
                ),
            ],
            "table": {
                "caption": "Six-Stage Enrichment Waterfall with Explicit Stop Conditions",
                "headers": [
                    "Waterfall stage and responsible role",
                    "Required input and transformation",
                    "Accepted output and retained evidence",
                    "Exception handling and operating boundary",
                ],
                "rows": [
                    [
                        "Dispatcher establishes the service request before collecting additional personal information.",
                        "Capture customer-supplied address, contact channel, requested service, and authorization status.",
                        "Create a job-linked intake record with timestamped communication preferences.",
                        "Resolve authority directly before treating a parcel owner as the customer.",
                    ],
                    [
                        "Dispatcher resolves the parcel and actual permitting jurisdiction.",
                        "Compare normalized address components with county parcel and municipal records.",
                        "Retain original input, candidate matches, selected parcel, and reviewer identity.",
                        "Route condominium, unit-number, and boundary conflicts to manual review.",
                    ],
                    [
                        "Dispatcher attaches P1 event context without asserting individual property damage.",
                        "Intersect relevant alert geometry and event times with verified service geography.",
                        "Store event identifiers, spatial relationship, issue time, and expiration time.",
                        "Discard expired dispatch triggers while preserving historical event evidence.",
                    ],
                    [
                        "Project manager checks the credentials of each assigned contracting entity.",
                        "Match legal business identity, license category, status, and applicable jurisdiction.",
                        "Retain dated registry results plus directly obtained supporting documents.",
                        "Suspend the assignment when identity or required credential remains unresolved.",
                    ],
                    [
                        "Estimator links P2 through P5 evidence to an authorized scope.",
                        "Join measurements, labeled photographs, inventory entries, and estimate version identifiers.",
                        "Produce a traceable scope packet separating observations from proposed work.",
                        "Return unsupported quantities to field review rather than padding allowances.",
                    ],
                    [
                        "Project manager reconciles payable costs and collectible invoice balances.",
                        "Match supplier bills, subcontractor invoices, customer invoices, and recorded payments.",
                        "Maintain a job-level balance with disputed items identified separately.",
                        "Resolve ledger differences before sending another payment demand to customers.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Define the smallest useful connector",
                    "action": "Choose one P1 feed or one existing-job export and assign an accountable employee.",
                    "detail": "Document the endpoint, entitlement, required fields, freshness tolerance, permitted purpose, and manual fallback before implementation.",
                },
                {
                    "step": 2,
                    "title": "Capture provenance before transforming records",
                    "action": "Store a minimally necessary source snapshot with timestamps and a digest.",
                    "detail": "Apply access controls and retention rules to snapshots; preserve the relationship between every derived field and its source record.",
                },
                {
                    "step": 3,
                    "title": "Test duplicates, delays, and missing fields",
                    "action": "Replay a small fixture set containing repeated events, stale alerts, and ambiguous addresses.",
                    "detail": "Confirm that replay creates no duplicate dispatches, invoices, contacts, or inventory entries and that exceptions reach the assigned owner.",
                },
                {
                    "step": 4,
                    "title": "Reconcile against the operating system",
                    "action": "Compare connector output with the vendor interface or official source before using it operationally.",
                    "detail": "Record discrepancies, test the fallback, restrict credentials to required permissions, and release only the verified workflow to the pod.",
                },
            ],
        },
        {
            "heading": "3. Convert diagnostic observations into defensible quantities and safe field decisions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For P2, the information edge is a repeatable measurement route, "
                    "not a photograph of a dehumidifier. Apply the relevant current "
                    "ANSI/IICRC S500 procedures and document the specific instrument, "
                    "measurement mode, material, location, and reference condition. A "
                    "nonpenetrating meter reading is not automatically comparable with "
                    "a pin reading, and neither can be interpreted without understanding "
                    "the substrate. Capture ambient temperature and relative humidity "
                    "with a suitable thermo-hygrometer; derive psychrometric quantities "
                    "using a documented calculation and the necessary pressure assumptions. "
                    "Compare affected and appropriate reference materials, track equipment "
                    "placement, and record visits against the same labeled measurement "
                    "points. Thermal imaging can guide investigation but does not independently "
                    "measure moisture or identify mold. Field leads should photograph "
                    "the instrument display alongside enough context to locate the reading, "
                    "while retaining structured values for trend analysis. Record inaccessible "
                    "areas and the reason they remain inaccessible instead of inventing "
                    "complete coverage. Electrical exposure, structural instability, and suspected "
                    "hazardous materials require qualified evaluation. The dispatcher must "
                    "not translate a downward humidity trend into permission to enter "
                    "an unsafe building. Drying progress and site safety are distinct "
                    "decisions with different evidence."
                ),
                (
                    "For P3 and P4, organize evidence around custody, boundaries, and "
                    "qualified judgment. Fire contents work needs item identifiers, condition "
                    "photographs, room origin, packing records, storage location, treatment "
                    "history, and customer acknowledgments where appropriate. A barcode "
                    "without a location history merely digitizes a missing box. Record "
                    "disposal authorization separately from an estimator's recommendation; "
                    "destructive disposal cannot be reversed when a dispute appears. "
                    "For mold projects, identify the jurisdiction's assessor and remediator "
                    "requirements, including any independence restrictions, before assigning "
                    "the same entity to multiple roles. Follow the applicable scope "
                    "and relevant ANSI/IICRC S520 practices without presenting an industry "
                    "standard as a statute. Air or surface sampling requires a defined "
                    "question, suitable methods, and competent interpretation; purchasing "
                    "a laboratory report does not create a universal clearance standard. "
                    "Pre-1978 housing and child-occupied facilities can trigger EPA renovation "
                    "requirements under 40 CFR Part 745 when covered work disturbs "
                    "paint. Evaluate applicability and authorized-state programs before demolition. "
                    "Lead, asbestos, respiratory protection, and other occupational hazards "
                    "have their own requirements; a restoration certification does not "
                    "replace them. Preserve the distinction between a field observation, "
                    "a laboratory result, and the qualified person's resulting decision."
                ),
                (
                    "For P5, build supplements as transparent construction evidence. Each "
                    "added quantity should trace to a measurement, photograph, material "
                    "condition, code requirement applicable to the work, or documented "
                    "change in authorized scope. Preserve the Xactimate price-list identifier, "
                    "estimate date, version, unit, quantity, and explanation for any "
                    "manual price adjustment. Price-list availability does not establish "
                    "the actual cost of every local trade, so retain subcontractor "
                    "quotes and purchase documentation where they explain a difference. "
                    "Separate estimating assistance from policy interpretation and claim "
                    "negotiation. Florida Statutes sections 626.854 and 489.147 illustrate "
                    "why contractor communications and public-adjusting activity require "
                    "careful role boundaries; apply the actual jurisdiction's rules. "
                    "Contractors can document their work and discuss construction facts "
                    "within the permitted scope without representing themselves as authorized "
                    "coverage advocates. Collections should reference the executed agreement, "
                    "completed work, invoice, credits, payments, and unresolved factual "
                    "disputes. Do not promise insurer payment or disguise a prohibited "
                    "deductible waiver as marketing. Electronic signatures and records "
                    "can support execution under 15 U.S.C. 7001, subject to its "
                    "conditions and applicable law; retain accessible records and the "
                    "signing evidence rather than only a flattened signature image."
                ),
            ],
            "table": {
                "caption": "Six Diagnostic and Evidence Controls that Prevent Expensive Rework",
                "headers": [
                    "Named tool or evidence system",
                    "Measurement or record worth retaining",
                    "Common failure that weakens the file",
                    "Required operator correction before downstream use",
                ],
                "rows": [
                    [
                        "Tramex or Protimeter instruments support material-specific moisture investigation.",
                        "Retain instrument model, mode, substrate, location, reading, and reference comparison.",
                        "Treating different measurement scales as interchangeable creates misleading drying trends.",
                        "Repeat comparable measurements and document calibration checks according to manufacturer instructions.",
                    ],
                    [
                        "Vaisala or suitable field thermo-hygrometers support psychrometric documentation.",
                        "Retain temperature, relative humidity, location, time, and calculation assumptions.",
                        "Mixing outdoor and indoor readings without context obscures drying performance.",
                        "Label each environment and preserve units before calculating comparative trends.",
                    ],
                    [
                        "FLIR thermal cameras help prioritize further inspection of suspect areas.",
                        "Retain original images, visible-light context, settings, and subsequent verification readings.",
                        "Calling every cool thermal pattern moisture produces unsupported damage assertions.",
                        "Confirm suspected conditions using appropriate inspection and measurement methods.",
                    ],
                    [
                        "Encircle or structured inventory records support fire contents custody.",
                        "Retain item identity, origin room, transfers, treatment, storage, and delivery acknowledgment.",
                        "Reusing item identifiers across jobs breaks ownership and custody traceability.",
                        "Use job-scoped unique identifiers and reconcile every transfer against the manifest.",
                    ],
                    [
                        "Qualified laboratories support explicitly scoped environmental sampling questions.",
                        "Retain sampling plan, collection conditions, chain of custody, and complete report.",
                        "Quoting isolated results without methods or interpretation overstates their meaning.",
                        "Attach qualified interpretation and apply project-specific acceptance criteria where required.",
                    ],
                    [
                        "Xactimate versioned exports support reconstruction quantities and documented change explanations.",
                        "Retain price-list identifier, quantities, units, supporting evidence, and version differences.",
                        "Sending revised totals without quantity explanations increases factual invoice disputes.",
                        "Produce an itemized change narrative with evidence links and authorized scope references.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four evidence habits that survive a difficult restoration file",
                "body": "Capture the facts once at the point of work, then reuse them without changing their meaning.",
                "items": [
                    "Label moisture points physically and digitally; repeat the same material, instrument mode, and location before comparing daily drying readings.",
                    "Photograph equipment serial numbers at placement and removal, then reconcile equipment days against visit logs instead of estimating from memory.",
                    "Export each submitted estimate version before editing; retain a line-item difference report so a supplement explains quantities rather than merely increasing the total.",
                    "For contents transfers, reconcile item counts at pickup, storage intake, treatment release, and delivery; resolve shortages before the customer must discover them.",
                ],
            },
        },
        {
            "heading": "4. Make the data stack earn its place inside the canonical labor and profit cases",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Reconcile tooling decisions to the canonical scorecard before assigning "
                    "a return. Conservative gross restoration billings are $500,000 at "
                    "an 8% net margin, producing $40,000 annual owner net profit. "
                    "Base billings are $1,500,000 at 13.0%, producing $195,000. Both "
                    "use five full-time employees and six contractors. Scaled billings "
                    "are $2,500,000 at 18%, producing $450,000 with six full-time "
                    "employees and seven contractors. These are gross restoration billings, "
                    "with subcontractor and material costs already reflected in the "
                    "margin; do not substitute claim reserves, insured property values, "
                    "or carrier disbursements unrelated to earned work. The corresponding "
                    "implied annual cost envelopes are $460,000, $1,305,000, and $2,050,000. "
                    "Headcount alone does not specify contractor utilization, compensation, "
                    "or local labor economics, so validate those inputs before treating "
                    "any case as executable. The stated $10,000–$45,000 monthly operating "
                    "expense range must not be mistaken for the entire cost envelope "
                    "when direct project costs are additional. Startup capital of "
                    "$75,000–$350,000 and a one-to-six-month first-deal window also require "
                    "a separate cash plan. Software cannot erase the need to fund "
                    "payroll, deposits, equipment, and materials before collections arrive."
                ),
                (
                    "Use a small, explicitly illustrative tooling test rather than "
                    "quietly rewriting those margins. Suppose a proposed connector and "
                    "documentation bundle costs $750 monthly, or $9,000 annually. If "
                    "it is incremental to the canonical cost envelope and creates "
                    "no offset, Base owner profit would fall from $195,000 to "
                    "$186,000; that is a sensitivity, not a replacement scorecard. "
                    "If measured dispatcher effort falls by eight hours weekly across "
                    "fifty weeks, the released capacity is 400 hours. At an "
                    "illustrative $35 loaded hourly rate, that represents $14,000 of "
                    "labor-equivalent capacity, not automatically $14,000 in cash savings. "
                    "Cash benefit exists only when paid hours, overtime, external "
                    "administration, or another real expenditure falls, or when additional "
                    "completed work produces incremental contribution after all associated "
                    "costs. Likewise, faster collection improves liquidity rather than "
                    "creating revenue. At Base annual billings, ten fewer collection "
                    "days release approximately $41,096 under a simplified uniform-billing, "
                    "365-day model. Actual cash effects depend on invoice timing, "
                    "disputed balances, deposits, and payment terms. Measure these separately "
                    "so the pod does not count the same improvement as labor "
                    "savings, extra profit, and working-capital release simultaneously. Keep "
                    "the original three scenarios visible beside every proposed sensitivity."
                ),
                (
                    "Run a four-week pilot across representative authorized jobs, not "
                    "only the easiest files. Track intake-to-dispatch time, duplicate "
                    "entry minutes, missing evidence at first estimate, unresolved cost "
                    "entries, invoice correction frequency, and days from completed work "
                    "to an accurate invoice. Count safety exceptions and customer "
                    "complaints alongside speed. The dispatcher reviews connector failures "
                    "daily; the estimator samples evidence links weekly; the project "
                    "manager reconciles accounting and contractor permissions. Field leads "
                    "confirm that mobile forms work offline and do not distract "
                    "from site controls. Give contractors job-scoped access, remove access "
                    "when assignments end, and restrict interior photographs, inventories, "
                    "and customer contacts to people who need them. Test restoration "
                    "from backup and an export from each paid platform before "
                    "committing the operation to its workflow. Retain records according "
                    "to applicable requirements, contracts, insurer-program obligations, and "
                    "dispute holds; delete unnecessary enrichment under a documented schedule. "
                    "At the pilot review, keep only integrations that improve a "
                    "measured dispatch, photo-documentation, or job-cost outcome. Scaling to "
                    "six employees and seven contractors requires renewed capacity planning, "
                    "not a claim that automation replaced field labor. The winning "
                    "information edge is fewer preventable exceptions per completed, collectible job."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and the Evidence Needed to Justify Tooling",
                "headers": [
                    "Scenario or operating test",
                    "Revenue and profit reconciliation",
                    "People and cost boundary",
                    "Decision evidence required from the pod",
                ],
                "rows": [
                    [
                        "Conservative case remains the original low-volume annual operating scenario.",
                        "$500,000 gross billings multiplied by 8% equals $40,000 owner profit.",
                        "Five employees plus six contractors; implied total annual costs equal $460,000.",
                        "Validate local labor utilization, material spending, and collection timing before launch.",
                    ],
                    [
                        "Base case remains the original annual planning benchmark.",
                        "$1,500,000 gross billings multiplied by 13.0% equals $195,000 owner profit.",
                        "Five employees plus six contractors; implied total annual costs equal $1,305,000.",
                        "Reconcile job costs and invoice quality without adding unearned claim proceeds.",
                    ],
                    [
                        "Scaled case remains the original expanded small-team annual scenario.",
                        "$2,500,000 gross billings multiplied by 18% equals $450,000 owner profit.",
                        "Six employees plus seven contractors; implied total annual costs equal $2,050,000.",
                        "Demonstrate field capacity, supervisory coverage, and working-capital support for higher throughput.",
                    ],
                    [
                        "Illustrative connector pilot tests value without changing canonical assumptions.",
                        "$750 monthly equals $9,000 annually in incremental proposed tooling expense.",
                        "Four hundred released hours represent capacity unless actual spending decreases.",
                        "Document realized cost reductions or incremental contribution separately from faster collections.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before the desk relies on a new integration",
                "body": "The project manager records these checks for the specific workflow, account, jurisdiction, and assigned people.",
                "items": [
                    "Verify the connector's documented access rights, current commercial entitlement, credential permissions, throttling behavior, and tested manual fallback.",
                    "Verify customer authorization, parcel match, permitted communication channel, and the actual jurisdiction before dispatch or contact enrichment.",
                    "Verify contractor and remediation credentials, hazardous-material procedures, and the boundary between construction documentation and separately licensed adjusting activity.",
                    "Verify duplicate-safe processing, original evidence retention, accounting reconciliation, and measured benefit within the five-employee, six-contractor capacity plan.",
                ],
            },
        },
    ],
    "pull_quote": "The best restoration data stack turns a field observation into a traceable scope, a correct invoice, and a collected balance without inventing authority.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Assign P1 storm triage, P2 water mitigation, P3 fire contents, P4 mold remediation, and P5 reconstruction documentation to named owners within the eleven-person pod.",
        "Create the eighteen-source register with access routes, entitlements, source timestamps, measured latency, permitted purposes, and tested fallbacks.",
        "Pilot one official hazard feed and one existing-job export using stable identifiers, bounded retries, provenance records, and duplicate-safe writes.",
        "Standardize moisture points, instrument metadata, equipment serial-number logs, contents custody, and estimate-version evidence across authorized jobs.",
        "Verify jurisdiction-specific licenses, site hazards, communication permissions, and public-adjusting boundaries before routing work or contacting customers.",
        "Review the four-week pilot against canonical revenue, margin, staffing, and owner-profit cases; separate realized savings, released capacity, and collection acceleration.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 7001 — General rule of validity for electronic records and signatures",
            "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section7001&num=0&edition=prelim",
            "relevance": "Supports electronic contracting subject to statutory conditions; retain accessible records and evaluate applicable consumer-consent requirements.",
        },
        {
            "title": "40 CFR 745.85 — Work practice standards for covered renovations",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-R/part-745/subpart-E/section-745.85",
            "relevance": "Defines lead-safe work practices for covered renovation activities, including containment, cleaning, and verification requirements.",
        },
        {
            "title": "40 CFR 745.89 — Firm certification under the renovation program",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-R/part-745/subpart-E/section-745.89",
            "relevance": "Provides the federal firm-certification framework; check authorized-state administration and the specific project's applicability.",
        },
        {
            "title": "29 CFR 1926.62 — Lead exposure in construction",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1926/subpart-D/section-1926.62",
            "relevance": "Requires construction employers to address occupational lead exposure through applicable assessment, protection, training, and recordkeeping duties.",
        },
        {
            "title": "47 CFR 64.1200 — Restrictions on telephone calls and related communications",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": "Constrains covered automated and telemarketing communications; a public property record or telephone lookup does not itself establish required consent.",
        },
        {
            "title": "Florida Statutes 626.854 — Public adjuster definitions and restrictions",
            "url": "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0626/Sections/0626.854.html",
            "relevance": "Distinguishes regulated public-adjusting activity from permitted contractor construction discussions; apply current provisions to the actual role and communications.",
        },
        {
            "title": "Florida Statutes 489.147 — Prohibited property-insurance practices",
            "url": "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0400-0499/0489/Sections/0489.147.html",
            "relevance": "Establishes contractor restrictions involving property-insurance activity, advertising, inducements, and unlicensed public adjusting.",
        },
        {
            "title": "Texas Insurance Code 707.002 — Payment of deductible",
            "url": "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.707.htm#707.002",
            "relevance": "Requires payment of applicable property-insurance deductibles and restricts prohibited waiver or rebate arrangements within the chapter's scope.",
        },
    ],
}
