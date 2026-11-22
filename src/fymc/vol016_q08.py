from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "probate-public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small probate real estate desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Probate Dockets, Recorder Chains, ATTOM Enrichment, Verified GBP Locations, and California Probate Code Authority Checks",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #9, Probate Real Estate, ranks #26 with a 80/100 Money-to-Manpower Score. "
        "This chapter supplies the records and tooling layer supporting the volume's 11 mapped plays: "
        "court events become verified authority, parcels become defensible property files, and local discovery "
        "becomes attributable brokerage demand. Build around county dockets, recorder instruments, assessor "
        "identifiers, licensed data vendors, and evidence-linked transaction checklists. Retained brokerage "
        "commissions after brokerage splits produce annual owner profit of $24,000 Conservative, $140,250 "
        "Base, and $315,000 Scaled; property sale values never become desk revenue. The operational edge "
        "is disciplined reconciliation, not indiscriminate scraping: distinguish petitioners from appointed "
        "representatives, reserve costly enrichment for qualified parcels, and route authority disputes "
        "to the responsible professional before outreach or listing commitments."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "20% net margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$510,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "27.5% net margin; $140,250 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "35% net margin; $315,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an authority-first directory rather than a deceased-owner mailing list",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one county and write a source contract for every field the desk intends to use. "
                    "The probate court establishes case events and representative authority; the assessor establishes "
                    "assessment identifiers; the recorder supplies recorded instruments; none substitutes for the others. "
                    "A petition naming an executor does not establish appointment, and an assessor ownership label does "
                    "not establish current title. Store jurisdiction, case number, filing type, event date, retrieval "
                    "timestamp, document locator, and reviewer alongside each extracted assertion. For California work, "
                    "read the issued letters and relevant orders before classifying independent administration authority. "
                    "Probate Code section 10501 reserves specified actions for court supervision, while section 10580 "
                    "governs notice of proposed action subject to statutory exceptions. Other states require separate "
                    "authority mappings rather than copied California rules. The working queue should distinguish petition "
                    "filed, representative appointed, authority reviewed, property linked, and listing discussion permitted. "
                    "Those statuses describe evidence, not an automatic right to contact anyone. Keep probate-attorney "
                    "service information separate from beneficiary contact information, and never extract sealed documents "
                    "or restricted personal identifiers. When a portal omits an attachment, request the document through "
                    "the clerk's published channel and leave the affected authority decision pending until reviewed."
                ),
                (
                    "Use the directory below as an acquisition plan, not a promise that every jurisdiction offers an "
                    "API. Its refresh entries specify desk polling targets unless a provider explicitly supplies a "
                    "publication cadence; a daily check cannot make a stale source current. At onboarding, record the "
                    "actual access URL, account owner, permitted purpose, current fee schedule, export rights, and "
                    "renewal date in a vendor register. Begin with browser research and approved downloads. Introduce "
                    "automation only where the source permits it, honoring published quotas, robots directives where "
                    "applicable, and contractual restrictions. A CAPTCHA, login challenge, or blocked request is a "
                    "stop signal, not an engineering puzzle to circumvent. Court and recorder charges vary by document "
                    "and access product, so approve a monthly document budget rather than inventing a universal per-page "
                    "price. Free assessor lookups still consume staff time and may prohibit bulk reuse. Commercial "
                    "coverage claims need a county-specific sample: compare twenty recent appointments and twenty "
                    "recorded transfers against primary records before accepting a feed. Record missingness by field "
                    "and county, because an excellent statewide match rate can conceal a weak launch market. Keep "
                    "manual clerk retrieval available for every transaction-critical document."
                ),
                (
                    "Build the first opportunity file from a court event, then join property evidence, not the reverse. "
                    "A deceased name appearing on a parcel export is merely a research clue: trusts, joint ownership, "
                    "transfer-on-death instruments, and prior conveyances can remove property from the expected probate "
                    "path. Normalize parcel identifiers within their county namespace and preserve the original text, "
                    "including leading zeros. Match a decedent to a parcel using at least two independent attributes, "
                    "then confirm the relevant recorded instrument before treating the estate as a seller. Household "
                    "addresses, suffixes, and common surnames create expensive false positives. FEMA and Census layers "
                    "supply property context, not valuation or title conclusions. A flood-zone intersection should "
                    "trigger map-panel review and transaction-specific diligence, while a geocoder match should trigger "
                    "coordinate inspection when parcel centroids and street addresses disagree. Ask title personnel "
                    "to resolve vesting conflicts rather than selecting whichever vendor returned the newest timestamp. "
                    "The desk's advantage is a concise evidence packet that an attorney or licensed agent can inspect "
                    "quickly. Include the source, observation date, disputed fields, and next responsible person. Exclude "
                    "family narratives and speculative distress labels; neither improves authority verification or "
                    "a professional referral conversation."
                ),
            ],
            "table": {
                "caption": (
                    "Eighteen named sources: access routes, procurement tiers, desk refresh targets, "
                    "request hygiene, and evidence-preserving fallbacks"
                ),
                "headers": [
                    "Named source and operating role",
                    "Exact access method",
                    "Cost tier and purchasing rule",
                    "Refresh target and latency interpretation",
                    "Rate-limit and access hygiene",
                    "Fallback source and verification action",
                ],
                "rows": [
                    [
                        "Los Angeles Superior Court probate case events and documents",
                        "Use lacourt.org, Online Services, Case Access, then Probate; search available case indexes.",
                        "Use published court access and copy fees; budget documents separately from discovery.",
                        "Check active files each business day; publication timing remains controlled by the court.",
                        "Use permitted interactive access; do not automate challenges or bypass session restrictions.",
                        "Request missing orders from the clerk or authorized counsel, preserving the case number.",
                    ],
                    [
                        "Orange County Superior Court probate registers of action",
                        "Use occourts.org, Online Services, Case Access; select the applicable probate search service.",
                        "Check the current court fee schedule before ordering copies or enhanced access.",
                        "Review active matters each business day and confirm hearing changes against the register.",
                        "Keep searches within published terms; stop on access restrictions or throttling responses.",
                        "Use clerk copy requests and counsel-provided filed documents when online attachments are absent.",
                    ],
                    [
                        "Riverside Superior Court probate public access records",
                        "Use riverside.courts.ca.gov, Online Services, then Public Access for probate case research.",
                        "Separate public search access from chargeable document retrieval using the current fee schedule.",
                        "Poll manually each business day for active files; docket entry delays remain possible.",
                        "Use authorized sessions and exports only; avoid concurrent scripted searches without permission.",
                        "Confirm missing events through the clerk and compare counsel's stamped copies against identifiers.",
                    ],
                    [
                        "Los Angeles County Assessor parcel identity and assessment context",
                        "Use assessor.lacounty.gov and the Assessor Portal to search addresses or assessor identification numbers.",
                        "Start with public lookup access; price bulk products under the county's current terms.",
                        "Check during intake and before listing; assessment data may lag recorded ownership changes.",
                        "Prefer permitted exports and cache parcel responses; avoid repetitive address-by-address scraping.",
                        "Compare recorder instruments and title research when displayed ownership conflicts with transaction evidence.",
                    ],
                    [
                        "Los Angeles County Registrar-Recorder recorded real estate instruments",
                        "Use lavote.gov, Records, Real Estate Records; follow published search and copy procedures.",
                        "Apply the recorder's current search, copy, certification, and delivery charges to each request.",
                        "Refresh before listing and closing milestones; recording and indexing dates can differ.",
                        "Follow available online, mail, and in-person channels rather than assuming unrestricted online images.",
                        "Order official copies or use authorized title research, retaining instrument numbers and recording dates.",
                    ],
                    [
                        "Orange County Clerk-Recorder official real property records",
                        "Use ocrecorder.com, Official Records, and the linked records search and copy services.",
                        "Public index research and purchased copies have separate terms; verify the current schedule.",
                        "Review at intake and material milestones; a new deed can precede downstream vendor updates.",
                        "Respect search-session restrictions and purchase document images through the designated service.",
                        "Request recorder copies and reconcile them with the title officer's current vesting evidence.",
                    ],
                    [
                        "California Department of Real Estate license verification service",
                        "Use dre.ca.gov, Licensees, Verify a License; search license number and responsible broker.",
                        "Public license lookup supports free verification; retain dated evidence rather than buying enrichment.",
                        "Check before referrals, advertising activation, and periodic partner reviews for status changes.",
                        "Use interactive verification or expressly authorized access; do not infer a public bulk API.",
                        "Contact the department through published channels when displayed status or broker affiliation conflicts.",
                    ],
                    [
                        "California Secretary of State bizfile business entity records",
                        "Use bizfileonline.sos.ca.gov, Business Search; inspect entity status and available filed statements.",
                        "Public searches are available online; certified records and selected filings can incur fees.",
                        "Check entity parties at onboarding and before execution; filing dates do not prove current authority.",
                        "Use permitted searches and downloads; cache retrieved statements with their filing dates.",
                        "Obtain organizational documents and authorized signatory evidence through the transaction's responsible professional.",
                    ],
                    [
                        "FEMA Map Service Center and National Flood Hazard Layer",
                        "Use msc.fema.gov for panels and hazards.fema.gov for published NFHL GIS services.",
                        "Public map and service access is available without a commercial enrichment subscription.",
                        "Review effective map dates at intake and before property representations or material diligence decisions.",
                        "Batch GIS requests within published service limits and cache effective panel references locally.",
                        "Inspect the effective FEMA panel and obtain property-specific elevation or survey evidence where needed.",
                    ],
                    [
                        "United States Census Geocoder address normalization and coordinates",
                        "Use geocoding.geo.census.gov/geocoder with documented single-address or batch endpoints and benchmark parameters.",
                        "Public geocoding is available without a commercial subscription; retain processing and review costs.",
                        "Reprocess changed addresses only; benchmark vintage describes reference geography rather than property ownership.",
                        "Follow documented batch limits; queue requests and retain the benchmark with every result.",
                        "Compare county GIS parcels and inspected street locations when returned coordinates appear inconsistent.",
                    ],
                    [
                        "United States Postal Service address and ZIP Code lookup",
                        "Use tools.usps.com ZIP Code Lookup interactively; procure licensed address products for bulk workflows.",
                        "Interactive lookup supports basic checks; bulk address standardization requires separately priced authorized products.",
                        "Validate before physical mailing; postal deliverability does not establish residence or estate authority.",
                        "Do not scrape the consumer lookup; use licensed bulk services with contracted throughput.",
                        "Review returned mail and verified correspondence addresses, keeping original and standardized address versions.",
                    ],
                    [
                        "ATTOM property data API for parcel and transaction enrichment",
                        "Use api.developer.attomdata.com documentation and an issued account key for contracted property endpoints.",
                        "Purchase a scoped commercial plan after a county sample; meter credits and storage rights.",
                        "Refresh qualified parcels at intake and milestones; inspect field-level source and update dates.",
                        "Honor the account quota, cache licensed responses, and back off on throttling responses.",
                        "Resolve deed and owner discrepancies using county records and current title research, not vendor precedence.",
                    ],
                    [
                        "Regrid parcel data downloads and licensed API access",
                        "Use regrid.com product documentation and contracted API or download access for selected counties.",
                        "Choose licensed commercial coverage with explicit export rights and a county-level acquisition budget.",
                        "Track each county dataset's vintage; refresh on licensed releases instead of repeated identical lookups.",
                        "Use bounded spatial queries and contractual request limits; avoid unnecessary statewide retrieval.",
                        "Fall back to county GIS and assessor parcel identifiers when geometry or coverage disagrees.",
                    ],
                    [
                        "BatchData property and contact enrichment API services",
                        "Use developer.batchdata.com documentation with contracted credentials and only the permitted enrichment endpoints.",
                        "Treat lookup and enrichment charges as metered costs; approve a monthly hard spending ceiling.",
                        "Enrich only reviewed records; a fresh response timestamp does not prove fresh contact ownership.",
                        "Deduplicate requests, respect provider quotas, and suppress prohibited or unnecessary contact queries.",
                        "Prefer verified representative correspondence details and discard conflicting contact matches pending direct verification.",
                    ],
                    [
                        "Google Business Profile APIs for eligible partner locations",
                        "Use developers.google.com/my-business with approved API access, OAuth, and legitimate profile-manager permissions.",
                        "Google profile management has no listing fee; budget verification, staffing, and optional software separately.",
                        "Inspect operating details weekly; platform review and profile-update propagation can delay visible changes.",
                        "Follow project quotas and location eligibility rules; never automate around verification or suspension controls.",
                        "Use the actual business website and transparent city pages while profile issues are resolved.",
                    ],
                    [
                        "Google Search Console API for owned local discovery pages",
                        "Use developers.google.com/webmaster-tools with verified site ownership and authorized search analytics access.",
                        "The service has no usage subscription charge; budget connector maintenance and reporting labor.",
                        "Import daily but assess weekly cohorts; search reporting is delayed and recent rows may change.",
                        "Respect property and project quotas; cache historical ranges and avoid repeated full-history requests.",
                        "Use first-party inquiry forms and server logs for operational counts without equating visits with leads.",
                    ],
                    [
                        "Twilio programmable voice records and signed event webhooks",
                        "Use twilio.com/docs/voice APIs and configured status callbacks under a controlled account.",
                        "Budget number rental, usage, and selected features using current destination-specific published pricing.",
                        "Process callbacks promptly and reconcile daily; webhook delivery can repeat or arrive out of order.",
                        "Validate request signatures, deduplicate event identifiers, and honor account concurrency and API limits.",
                        "Reconcile carrier call logs with CRM dispositions; maintain a tested direct business-number fallback.",
                    ],
                    [
                        "Google Maps Platform Geocoding API for address diagnostics",
                        "Use developers.google.com/maps/documentation/geocoding with restricted credentials and a billing-enabled project.",
                        "Apply current usage pricing, applicable credits, and project budgets before enabling production traffic.",
                        "Geocode changed addresses only; coordinates indicate a match result rather than legal parcel boundaries.",
                        "Restrict keys, cap quota, and follow caching and display terms instead of retaining unrestricted copies.",
                        "Use Census Geocoder and county parcel GIS when permitted alternatives better fit the workflow.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four shortcuts that preserve the evidence chain",
                "body": "Reduce repeat research without treating a convenient secondary feed as controlling evidence.",
                "items": [
                    "Save the appointment order and issued letters as separate evidence objects; a docket entry announcing appointment can precede accessible letters.",
                    "Index recorder instruments by county plus instrument number, because identical instrument numbers can occur in different jurisdictions.",
                    "Ask referral attorneys which case events justify a property discussion; configure alerts for those events instead of sending every docket change.",
                    "Maintain a county-specific missing-document queue with clerk request dates, assigned researchers, and the transaction decision each missing item blocks.",
                ],
            },
        },
        {
            "heading": "2. Construct an enrichment waterfall with reversible identity decisions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Separate discovery, evidence, enrichment, and outreach into different records and permission scopes. A "
                    "minimal schema has case, person, authority_event, parcel, instrument, organization, contact_point, "
                    "and lead tables, connected by explicit relationship records. Each relationship needs a basis, "
                    "reviewer, observation time, and status so a mistaken join can be reversed without deleting source "
                    "history. Use county plus case number for case identity and county plus parcel identifier for parcel "
                    "identity; never use a person's name as the primary key. Python's sqlite3, csv, hashlib, datetime, "
                    "and urllib modules can support the initial workflow without a large integration platform. Hash "
                    "downloaded documents for duplicate detection, but do not confuse a checksum with proof of authenticity. "
                    "Retain originals in access-controlled storage and keep extracted text beside parser version and page "
                    "references. Limit sensitive contact access to staff who perform the corresponding task. Apply a "
                    "documented retention schedule to unsuccessful prospect records, and preserve transaction records "
                    "for the period required by the applicable brokerage and jurisdiction. The result should be a "
                    "compact evidence graph: an operator can trace a proposed seller, parcel, and outreach route back "
                    "to specific records rather than trusting an unexplained confidence score."
                ),
                (
                    "Order enrichment by expected decision value. First normalize free court and parcel identifiers; "
                    "second retrieve authority documents for plausible property matters; third buy property attributes "
                    "only where they resolve a real qualification question; fourth obtain contact enrichment only for "
                    "a documented permissible workflow. Do not purchase beneficiary phone numbers merely because a "
                    "vendor offers them. An illustrative monthly batch contains 200 docket events, 80 distinct cases, "
                    "30 plausible parcel links, and 12 evidence-reviewed opportunities. If property enrichment costs "
                    "$0.50 for each of 30 lookups and authorized contact research costs $2 for each of 12 records, "
                    "variable vendor spend is $39, or $3.25 per reviewed opportunity. These are planning assumptions, "
                    "not quoted supplier prices, and exclude documents, labor, postage, and software. Enriching all "
                    "200 events at the same combined $2.50 would instead cost $500 and repeatedly charge for the "
                    "same estate. A missing contact should produce a research task, not progressively more intrusive "
                    "searches. Prefer the representative's verified correspondence channel or a professional introduction "
                    "where appropriate. Keep purchased match scores separate from verified identities, and prohibit "
                    "automatic outreach when vendor identities disagree with the court record."
                ),
                (
                    "Make ingestion idempotent and alerting selective. Store a source event key built from jurisdiction, "
                    "case number, event type, source identifier, and document revision when available. Replaying yesterday's "
                    "export should update observations without creating another lead or another reminder. Preserve "
                    "source_event_at, source_published_at when supplied, and fetched_at as distinct fields; absent "
                    "publication timing must remain absent rather than fabricated. Use scheduled jobs with bounded "
                    "retries, exponential backoff, jitter, and a dead-letter queue for persistent failures. For a "
                    "documented API, honor Retry-After and pagination tokens; for a restricted portal, route work to "
                    "an authorized manual task. Put tokens in managed secrets or restricted environment configuration, "
                    "never in exported spreadsheets or referral packets. A transaction checklist should react to "
                    "material events such as amended letters, a changed hearing, recorded transfer, or representative "
                    "replacement, while ignoring cosmetic webpage changes. Send each alert to one accountable owner "
                    "with the supporting document and required next action. An unresolved authority change should "
                    "pause affected listing activity for review, not silently disappear after a retry succeeds. "
                    "Test restoration from backups and replay a sample month before relying on the pipeline for "
                    "live appointment tracking."
                ),
            ],
            "table": {
                "caption": "Six-stage evidence waterfall with measurable exit conditions and controlled spending",
                "headers": [
                    "Stage and required input",
                    "Deterministic processing and evidence retained",
                    "Spending and throughput discipline",
                    "Failure condition and operator fallback",
                ],
                "rows": [
                    [
                        "Discovery starts with permitted court exports or researched docket events.",
                        "Deduplicate county, case number, event identifier, and source revision before creating tasks.",
                        "Process an illustrative 200 events into 80 distinct monthly case records.",
                        "Missing case identifiers require clerk-supported research rather than speculative person matching.",
                    ],
                    [
                        "Authority review starts with issued letters and relevant court orders.",
                        "Record appointment, restrictions, representative identity, and document page supporting each conclusion.",
                        "Purchase documents only for cases with a plausible property-service decision.",
                        "Unavailable attachments remain in a named research queue until primary evidence arrives.",
                    ],
                    [
                        "Parcel linkage starts with normalized names and independent location evidence.",
                        "Preserve county-qualified parcel identifiers and two independent identity attributes for reviewer inspection.",
                        "Limit illustrative paid property lookups to 30 evidence-supported parcel candidates.",
                        "Conflicting vesting goes to title personnel before any seller-authority representation.",
                    ],
                    [
                        "Property enrichment starts with reviewed parcel matches and defined questions.",
                        "Store requested attributes, vendor source dates, response identifiers, and licensed retention conditions.",
                        "Illustrative 30 lookups at $0.50 create $15 of variable vendor expense.",
                        "Stale ownership fields yield to recorded instruments and current title evidence.",
                    ],
                    [
                        "Contact research starts with a documented permissible professional outreach workflow.",
                        "Keep contact provenance, recipient role, suppression status, and verification outcome together.",
                        "Illustrative 12 reviewed records at $2 create $24 of additional expense.",
                        "Disputed identities remain excluded from outreach while verified correspondence channels are researched.",
                    ],
                    [
                        "Task release starts with authority, identity, and channel checks completed.",
                        "Assign one owner, one evidence-linked next action, and a concrete follow-up date.",
                        "Track $39 vendor spend separately from research labor and document charges.",
                        "Any material source change returns the affected task to targeted human review.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Acquire and fingerprint the evidence",
                    "action": "Download a permitted case export and save each relevant source document.",
                    "detail": "Record jurisdiction, access method, retrieval time, document locator, and SHA-256 checksum; keep source originals outside the editable research worksheet.",
                },
                {
                    "step": 2,
                    "title": "Resolve authority before enriching contacts",
                    "action": "Review issued letters, orders, and county-qualified parcel matches.",
                    "detail": "Assign an operator to each disputed relationship and request missing instruments through the clerk, recorder, or responsible transaction professional.",
                },
                {
                    "step": 3,
                    "title": "Spend only against a decision",
                    "action": "Run contracted enrichment for reviewed records with a specific unresolved question.",
                    "detail": "Deduplicate vendor requests, meter credits, preserve provenance, and stop the batch when the approved monthly spending ceiling is reached.",
                },
                {
                    "step": 4,
                    "title": "Release and reconcile accountable tasks",
                    "action": "Create evidence-linked CRM tasks and verify daily ingestion totals.",
                    "detail": "Compare source counts, accepted events, duplicate events, rejected rows, and assigned tasks; investigate differences before treating the batch as complete.",
                },
            ],
        },
        {
            "heading": "3. Turn legitimate local discovery into attributable probate demand",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play google_maps_gbp_lead_gen_network applies only through genuine local businesses and "
                    "accurate representations. Partner with licensed local tradespeople who actually operate from an "
                    "eligible physical shop or yard, verify the operating facts, and let the business owner complete "
                    "Google's required verification with authorized manager support. A brokerage cannot borrow a "
                    "contractor's address to manufacture its own office, and partnership does not make an otherwise "
                    "ineligible location eligible. Distinct businesses need independently supportable profiles and "
                    "real-world operations. Service-area businesses should hide their addresses when Google's rules "
                    "require it; virtual offices, fabricated signage, and duplicate city profiles are not substitutes "
                    "for eligibility. Wire a business-controlled call-tracking number that reaches the actual operator, "
                    "retain the canonical business number where appropriate, and test routing after every change. "
                    "Use review requests consistently after genuine service experiences, without incentives or selective "
                    "solicitation based on expected ratings. Pair each legitimate listing with useful organic city "
                    "pages describing the actual service provider, coverage, and contact route. If verification fails "
                    "or a profile is suspended, stop profile expansion and use those accurate pages and existing "
                    "referral relationships while the real business resolves the issue through Google's channels."
                ),
                (
                    "Separate estate-service demand from brokerage intent before assigning value to a call. A cleanout "
                    "request, locksmith inquiry, and executor seeking listing representation are different products "
                    "with different professional responsibilities. Suppose one legitimate location produces 30 monthly "
                    "inbound calls, 18 are qualified for its advertised service, and six voluntarily request a "
                    "brokerage introduction. If two of those six book consultations and 0.25 retained listings "
                    "eventually close per monthly cohort, a $8,500 retained commission implies $2,125 expected "
                    "brokerage revenue for that cohort. This is an illustrative attribution model with a long "
                    "conversion lag, not cash collected that month. A $600 monthly allocation for routing, content, "
                    "and tracking equals $33.33 per qualified service call, $100 per requested introduction, and "
                    "$2,400 per eventual closing under those assumptions. Count the commission only after the "
                    "transaction closes and the brokerage split is applied. Do not add contractor job value, "
                    "property sale price, or hypothetical lead resale value to brokerage revenue. If two consecutive "
                    "mature cohorts miss the introduction target, inspect category fit, routing, and page intent "
                    "before buying more software. Preserve organic pages as the fallback rather than creating "
                    "additional unsupported locations."
                ),
                (
                    "Design the referral flywheel around useful service and documented economics rather than disguised "
                    "payments for settlement business. Probate attorneys can receive concise evidence packets and "
                    "reliable status updates without being paid for introductions. Under 12 U.S.C. section 2607, "
                    "fees or things of value for referrals of covered settlement-service business create specific "
                    "prohibitions; actual services and applicable exceptions require careful factual treatment. State "
                    "brokerage rules also govern compensation and unlicensed activity. Evaluate any paid marketing "
                    "arrangement for real deliverables, reasonable pricing, and restrictions on steering, rather than "
                    "renaming a per-closing bounty as advertising. For inbound attribution, store campaign, landing "
                    "page, called number, call disposition, requested service, and explicit handoff choice. Recording "
                    "is optional and should remain off until the applicable recording rules and notice process "
                    "are implemented. Outbound calls and texts require a separate review of 47 CFR section 64.1200, "
                    "applicable do-not-call rules, technology, recipient consent where required, and state restrictions. "
                    "A public probate filing supplies none of those permissions by itself. Keep opt-outs synchronized "
                    "across the CRM and calling platform. When a contractor lacks capacity, route only through an "
                    "agreed, transparent process; never represent a brokerage desk as the trade business that the "
                    "caller selected."
                ),
            ],
            "table": {
                "caption": "Six local-discovery controls connecting genuine locations to measurable brokerage outcomes",
                "headers": [
                    "Control and business evidence",
                    "Implementation using named tools",
                    "Illustrative unit math or measurement",
                    "Risk fallback and accountable action",
                ],
                "rows": [
                    [
                        "Location eligibility requires an actual operating business with accurate customer-facing details.",
                        "Use Google Business Profile owner access and the platform's current verification process.",
                        "Maintain one evidence file for each independently eligible operating business location.",
                        "If verification fails, use accurate organic pages while the owner resolves eligibility.",
                    ],
                    [
                        "Call routing must reach the advertised business rather than an undisclosed substitute.",
                        "Configure Twilio routing, authenticated callbacks, canonical contact details, and tested failover.",
                        "Thirty monthly inbound calls yield eighteen qualified service conversations in the illustration.",
                        "Routing failures switch to the tested direct number and create an incident task.",
                    ],
                    [
                        "Brokerage handoffs require caller choice and separation from ordinary trade-service requests.",
                        "Capture requested service and explicit handoff choice in the CRM disposition fields.",
                        "Six requested introductions from eighteen qualified calls represent a one-third handoff share.",
                        "Declined introductions stay with the requested service and do not enter brokerage outreach.",
                    ],
                    [
                        "Attribution uses mature cohorts because probate conversion extends beyond a single month.",
                        "Join CRM closing records to campaign identifiers without overwriting the original source.",
                        "One-quarter eventual closing times $8,500 retained commission equals $2,125 expected cohort revenue.",
                        "If mature cohorts underperform, repair intent and routing before increasing acquisition spending.",
                    ],
                    [
                        "Marketing expense stays separate from contractor receipts and property sale values.",
                        "Tag content, number rental, routing, and reporting costs in the brokerage ledger.",
                        "A $600 monthly allocation divided by six introductions equals $100 per introduction.",
                        "Do not recognize lead resale or contractor job receipts inside retained brokerage commissions.",
                    ],
                    [
                        "Referral arrangements require genuine services and review of applicable compensation restrictions.",
                        "Retain written deliverables, invoices, license checks, and documented compensation analysis.",
                        "Track actual service costs without creating an automatic payment for each closing.",
                        "Replace problematic payment terms with unpaid introductions or a properly structured service arrangement.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before activating a local acquisition channel",
                "body": "A profile, call route, and CRM workflow must all describe the same real service relationship.",
                "items": [
                    "Verify the operating location, business ownership, required licenses, and profile eligibility; obtain authorized manager access without creating a fictitious branch.",
                    "Test inbound routing and failover, confirm accurate business identification, and leave call recording disabled until the applicable process is implemented.",
                    "Document the marketing deliverables and compensation structure; resolve covered settlement-service referral restrictions before exchanging payments or benefits.",
                    "Check handoff choice, channel-specific contact permissions, suppression synchronization, and evidence access before releasing the first brokerage follow-up task.",
                ],
            },
        },
        {
            "heading": "4. Diagnose data decay and reconcile every dashboard to retained commissions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Measure information quality before measuring lead volume. The daily control sheet should show "
                    "expected source jobs, completed jobs, source rows, accepted events, duplicates, rejected records, "
                    "unresolved identity conflicts, and oldest unreviewed material event. Use Python unittest fixtures "
                    "for parser behavior and sqlite3 reconciliation queries for counts; keep representative sample "
                    "documents with sensitive content minimized. A portal redesign can return a successful HTTP "
                    "status while replacing docket content with a login page, so validate content structure and "
                    "required identifiers rather than status codes alone. For an authorized API, log response status, "
                    "latency, request identifier, quota headers when supplied, and retry count without logging "
                    "credentials or unnecessary personal data. Alert when a normally active source produces zero "
                    "records, but compare against court calendars and historical variation before declaring an "
                    "outage. Manually inspect ten accepted joins and every rejected high-value case each week. "
                    "Track false joins separately from missed joins because their operational consequences differ: "
                    "a missed case costs opportunity, while a false join can expose private estate information to "
                    "the wrong household. Every incident needs an owner, affected records, corrective action, and "
                    "a replay plan that avoids duplicate outreach."
                ),
                (
                    "Reconcile the commercial dashboard to the canonical scorecard before discussing leverage. Conservative "
                    "revenue is $120,000 of retained brokerage commissions after splits, with a 20% net margin and "
                    "$24,000 annual owner net profit; implied annual expenses are $96,000. Base revenue is $510,000, "
                    "with a 27.5% net margin, $140,250 owner profit, and $369,750 expenses. Scaled revenue is "
                    "$900,000, with a 35% net margin, $315,000 owner profit, and $585,000 expenses. An illustrative "
                    "transaction bridge is 20 closings at $6,000 retained, 60 at $8,500 retained, and 90 at "
                    "$10,000 retained respectively; these are scenario-specific averages, not a standard commission "
                    "schedule. Negotiated compensation, brokerage splits, market prices, and transaction mix determine "
                    "actual retained amounts. The teams remain 2 FT + 3 C, 2 FT + 3 C, and 3 FT + "
                    "4 C respectively. Contractor counts do not establish full-time contractor utilization. Treat the "
                    "$3,000–$18,000 monthly operating range as a planning input whose cost scope must be reconciled, "
                    "not as the complete annual expense ledger. Keep acquisition principal, resale proceeds, client "
                    "repair funds, and executor-concierge receipts in separately classified ledgers; they cannot inflate "
                    "this commission-only scorecard."
                ),
                (
                    "Budget runway for the actual delay between information and cash. The stated startup range is "
                    "$15,000–$100,000, while time to first deal is 4–18 months; neither implies that the lowest "
                    "capital amount funds the longest delay. At $3,000 monthly operating expense, eighteen months "
                    "consumes $54,000 before startup purchases, transaction-variable costs, or other excluded "
                    "obligations. Use a rolling cash schedule that distinguishes contracted software, discretionary "
                    "enrichment, document purchases, staff commitments, and closing-dependent receipts. Review court "
                    "delays, family disputes, and housing-market changes as separate timing stresses rather than "
                    "one generic haircut. Docket alerts can reduce missed events but cannot accelerate a contested "
                    "hearing; transaction checklists can reduce omissions but cannot settle beneficiary disagreements. "
                    "Make staffing explicit: the two-person core owns brokerage execution and research operations, "
                    "while contracted support handles clearly scoped legal, title, field, or administrative work "
                    "within appropriate professional boundaries. At seven people, add queue ownership and escalation "
                    "rules before adding counties. The weekly operating meeting should close with three decisions: "
                    "which evidence gaps block action, which channel deserves the next dollar, and which expected "
                    "closings moved in time. A larger scraped list is not a substitute for answers backed by "
                    "documents, measured conversion, and reconciled cash."
                ),
            ],
            "table": {
                "caption": "Scorecard reconciliation and evidence-quality diagnostics for the small probate desk",
                "headers": [
                    "Scenario or diagnostic control",
                    "Revenue basis or required evidence",
                    "Arithmetic and operating interpretation",
                    "Owner action and failure response",
                ],
                "rows": [
                    [
                        "Conservative scenario uses two full-time people and three contracted contributors.",
                        "$120,000 annual revenue consists solely of retained brokerage commissions after splits.",
                        "20% margin produces $24,000 owner profit and implies $96,000 annual expenses.",
                        "Bridge an illustrative twenty closings at $6,000 retained without counting underlying property values.",
                    ],
                    [
                        "Base scenario retains two full-time people and three contracted contributors.",
                        "$510,000 annual revenue consists solely of retained brokerage commissions after splits.",
                        "27.5% margin produces $140,250 owner profit and implies $369,750 annual expenses.",
                        "Bridge an illustrative sixty closings at $8,500 retained and reconcile actual negotiated compensation.",
                    ],
                    [
                        "Scaled scenario uses three full-time people and four contracted contributors.",
                        "$900,000 annual revenue consists solely of retained brokerage commissions after splits.",
                        "35% margin produces $315,000 owner profit and implies $585,000 annual expenses.",
                        "Bridge an illustrative ninety closings at $10,000 retained while retaining accountable queue ownership.",
                    ],
                    [
                        "Evidence-quality monitoring covers source freshness, identity errors, and unresolved authority changes.",
                        "Retain source timestamps, reviewer decisions, incident records, and document-linked exception queues.",
                        "Review ten accepted joins weekly and every rejected high-value case before task release.",
                        "Pause affected activity, correct relationships, and replay safely without generating duplicate outreach.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The probate desk wins when every claimed opportunity can be traced to authority, a parcel, a permitted conversation, and a retained commission.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Select one launch county and document court, assessor, recorder, license-verification, and clerk-copy access methods with current fees and permitted uses.",
        "Create county-qualified case and parcel identifiers, document hashes, source timestamps, and reversible relationship records before purchasing enrichment.",
        "Audit twenty appointments and twenty recorded transfers against proposed vendor coverage, then set hard monthly document and enrichment spending ceilings.",
        "Implement the four-step evidence SOP with a missing-document queue, named reviewers, idempotent imports, and tested backup restoration.",
        "Activate google_maps_gbp_lead_gen_network only for genuine eligible businesses, with verified licenses, accurate city pages, tested routing, and reviewed referral economics.",
        "Reconcile the weekly pipeline to retained commissions, the three canonical profit cases, mature acquisition cohorts, and a cash schedule reflecting court and family delays.",
    ],
    "statutory_citations": [
        {
            "title": "California Probate Code section 10501 — Actions requiring court supervision",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "relevance": "Map statutory limits on independent administration against issued letters and orders before assuming a representative can complete a proposed transaction without court supervision.",
        },
        {
            "title": "California Probate Code section 10580 — Notice of proposed action",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
            "relevance": "Build evidence-linked checklist tasks for notice requirements under independent administration, accounting for the statute's exceptions and the actual proposed action.",
        },
        {
            "title": "12 U.S.C. section 2607 — Prohibition against kickbacks and unearned fees",
            "url": "https://www.law.cornell.edu/uscode/text/12/2607",
            "relevance": "Review marketing payments, benefits, and attorney or contractor referral arrangements involving covered settlement services; distinguish genuine services from prohibited referral compensation.",
        },
        {
            "title": "47 CFR section 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Configure outbound calling and texting workflows around applicable consent, do-not-call, identification, and opt-out requirements rather than assuming public records authorize contact.",
        },
        {
            "title": "California Business and Professions Code section 10130 — Real estate license requirement",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "relevance": "Separate unlicensed research and administrative tasks from acts requiring a California real estate license, and verify the responsible brokerage before advertising or representation.",
        },
        {
            "title": "California Business and Professions Code section 10137 — Compensation and licensed activity",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10137.",
            "relevance": "Review compensation to unlicensed people and broker-salesperson payment relationships before monetizing introductions or assigning tasks that require licensure.",
        },
    ],
}
