from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "medical-equipment-resale-public-records-apis-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small medical equipment resale desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "AccessGUDID, openFDA, UCC Searches, Biomedical Test Records, and HIPAA-Aware Asset Pipelines for a Four-Person Resale Pod",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, ranks #20 with a 85/100 Money-to-Manpower Score. "
        "Its information advantage comes from connecting identity, ownership, serviceability, and buyer demand before committing capital. "
        "This chapter maps three operator plays: diagnostic replacement sourcing, surgical surplus recovery, and veterinary/aesthetic buyer matching. "
        "AccessGUDID and FDA records establish product context; procurement, surplus, and provider records expose opportunities; biomedical testing and controlled sanitization establish resale readiness. "
        "The operating design fits two full-time staff plus four contractors, with bounded queues instead of constant manual research. "
        "Canonical annual owner profit remains $25,000 Conservative, $164,000 Base, and $396,000 Scaled. "
        "These are equipment-resale outcomes, not data-subscription revenue, and every proposed tool must protect contribution, reduce stranded inventory, or shorten a documented operating task."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "10% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "16.0% net margin; $164,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "22% net margin; $396,000 annual owner net profit; 1 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an eighteen-source directory around three executable resale plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the directory around three mapped plays, not around an indiscriminate collection of listings. "
                    "Play one, diagnostic replacement sourcing, finds clinics replacing ultrasound and other diagnostic equipment, then connects exact configurations to documented buyer requirements. "
                    "Play two, surgical surplus recovery, targets hospital disposals and surgical-center closures where accessories, ownership documents, and service records often determine whether a lot is economically recoverable. "
                    "Play three, veterinary/aesthetic buyer matching, starts with a qualified buyer specification and works backward to suitable equipment; it never assumes that human-device labeling transfers to another use. "
                    "Assign the first full-time operator sourcing, supplier communication, and commercial negotiation; assign the second inventory control, evidence review, and buyer fulfillment. "
                    "The four contractors cover biomedical inspection, decontamination and specialist transport, data sanitization, and device-specific regulatory or ownership-document review. "
                    "These are scoped assignments rather than four people continuously researching every listing. "
                    "The directory below identifies access routes and operational limits; free access does not mean unrestricted republication. "
                    "Capture source terms and retrieval dates before building a connector. "
                    "Public records create leads and product context, while photographs, contracts, service evidence, and physical inspection establish facts about the individual asset. "
                    "A product listing alone never establishes the seller's authority to transfer that asset."
                ),
                (
                    "Start device research with a photograph of the label, manufacturer, commercial model, serial number, and any device identifier. "
                    "AccessGUDID can resolve a device identifier into labeling attributes, but its records generally describe device versions rather than the custody history of an individual serial. "
                    "Use FDA classification and clearance records to understand product codes, intended use, and the relevant regulatory pathway. "
                    "A registration or listing entry does not establish FDA approval, present serviceability, or an unrestricted right to resell. "
                    "Search recall records using manufacturer aliases, product codes, model strings, and affected production ranges; a recall notice can cover a serial interval without naming the photographed commercial variant. "
                    "Treat MAUDE reports as investigation prompts, not comparative failure rates, because reporting patterns and exposure denominators differ. "
                    "The biomedical contractor resolves safety questions against manufacturer instructions and applicable corrective actions. "
                    "For veterinary and aesthetic opportunities, inspect the exact intended use, energy-delivery characteristics, accessories, and applicable federal and state requirements before matching a buyer. "
                    "A veterinary listing is not a shortcut around restrictions on the same device when marketed for human treatment. "
                    "Record the conclusion and supporting documents separately from raw search hits so an ambiguous database match cannot silently become a cleared inventory status."
                ),
                (
                    "Separate source publication latency from the desk's polling schedule. "
                    "A daily collector cannot make an intermittently updated registry current, and an auction event timestamp does not prove that equipment remains available. "
                    "Store source publication time when exposed, retrieval time, the query used, and a content hash. "
                    "The directory's refresh intervals are desk schedules unless the source itself supplies a dated release; confirm current provider documentation before enabling automation. "
                    "For openFDA, register a key when appropriate, read the current quota rules, constrain queries, and prefer bulk downloads for broad historical work. "
                    "For commercial marketplaces, use licensed feeds or permitted exports instead of reverse-engineering private endpoints. "
                    "An HTTP 429 response should suspend that source's worker using Retry-After when supplied and bounded exponential backoff otherwise. "
                    "Never rotate credentials to outrun a service limit. "
                    "When a connector fails, retain the last successful snapshot with its age and route consequential decisions to a dated manual check. "
                    "The sourcing operator needs a short exception queue, not a screen full of stale apparent bargains. "
                    "Review supplier prices and endpoint terms monthly, and retire a paid source when it produces neither qualified opportunities nor measurable labor savings across two consecutive review periods."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost, Freshness, Request Discipline, and Fallback Evidence",
                "headers": [
                    "Named resource and assigned operating use",
                    "Exact portal or API access method",
                    "Cost tier and permitted-use consideration",
                    "Refresh latency and rate-limit discipline",
                    "Decision output and fallback evidence route",
                ],
                "rows": [
                    [
                        "AccessGUDID identifies labeled device versions across all three plays",
                        "Open https://accessgudid.nlm.nih.gov/ and use Search or Download",
                        "Public lookup and downloads are free; retain source attribution",
                        "Read each release date; ingest daily and prefer published downloads",
                        "Resolve device identifiers; fall back to manufacturer label documentation",
                    ],
                    [
                        "FDA classification records identify device product codes and regulatory context",
                        "Query https://api.fda.gov/device/classification.json using documented search fields",
                        "Public API access is free within current published service limits",
                        "Poll relevant codes weekly; cache responses and back off on throttling",
                        "Confirm classification context; fall back to FDA Product Classification search",
                    ],
                    [
                        "FDA 510(k) records support diagnostic and surgical product research",
                        "Query https://api.fda.gov/device/510k.json by documented applicant or device fields",
                        "Public API access is free; retain underlying decision references",
                        "Refresh watched models weekly; treat publication lag separately from retrieval",
                        "Locate clearance records; fall back to FDA clearance letters and summaries",
                    ],
                    [
                        "FDA registration and listing records establish establishment and listing context",
                        "Query https://api.fda.gov/device/registrationlisting.json with documented establishment filters",
                        "Public API access is free; records do not establish approval",
                        "Refresh suppliers monthly and before purchase; use cached narrow queries",
                        "Investigate establishment context; fall back to FDA registration lookup",
                    ],
                    [
                        "FDA device enforcement reports identify published recall enforcement information",
                        "Query https://api.fda.gov/device/enforcement.json using product and firm terms",
                        "Public API access is free within documented quota conditions",
                        "Poll watched inventory daily; respect endpoint limits and publication delays",
                        "Flag recall candidates; fall back to FDA notices and manufacturer confirmation",
                    ],
                    [
                        "FDA MAUDE reports expose device-event narratives requiring technical investigation",
                        "Query https://api.fda.gov/device/event.json using documented model and manufacturer fields",
                        "Public API access is free; interpret reporting limitations explicitly",
                        "Review target families weekly; use bulk files for historical analysis",
                        "Generate inspection questions; fall back to FDA MAUDE portal searches",
                    ],
                    [
                        "FDA Medical Device Recalls portal provides recall-specific investigation details",
                        "Search https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm by product or firm",
                        "Public web searches are free; preserve dated notice references",
                        "Recheck before bid and shipment; use manual lookup without aggressive crawling",
                        "Compare affected configurations; fall back to recalling firm's corrective-action documents",
                    ],
                    [
                        "SAM.gov Contract Opportunities reveals equipment procurement and replacement signals",
                        "Use https://sam.gov/ or https://api.sam.gov/opportunities/v2/search with an authorized key",
                        "Public search is free; API access requires provider account conditions",
                        "Poll saved filters daily; paginate within current published account limits",
                        "Identify public buying signals; fall back to contracting-office solicitation documents",
                    ],
                    [
                        "USAspending award data supports account research rather than asset identification",
                        "POST documented filters to https://api.usaspending.gov/api/v2/search/spending_by_award/",
                        "Public API access is free; award values are not equipment comparables",
                        "Refresh target accounts monthly; cache requests and honor service responses",
                        "Trace purchasing organizations; fall back to award documents and agency records",
                    ],
                    [
                        "GovDeals surplus listings support diagnostic and surgical disposal sourcing",
                        "Search https://www.govdeals.com/ and enable permitted account notifications",
                        "Browsing is generally free; buyer premiums and transaction terms vary",
                        "Review alerts daily; use permitted exports rather than assumed API access",
                        "Capture lot terms and photos; fall back to seller inspection appointments",
                    ],
                    [
                        "Public Surplus auction listings expose local public-sector disposal opportunities",
                        "Search https://www.publicsurplus.com/ and configure available category notifications",
                        "Browsing is generally free; auction fees and buyer obligations vary",
                        "Check closing dates daily; avoid automated collection without permission",
                        "Identify inspectable lots; fall back to agency surplus coordinators",
                    ],
                    [
                        "California Secretary of State UCC records illustrate jurisdiction-specific lien research",
                        "Use https://bizfileonline.sos.ca.gov/ and its UCC search or order functions",
                        "Check the current fee schedule; certified searches and copies may cost",
                        "Search before commitment and near closing; respect interactive portal restrictions",
                        "Investigate debtor filings; fall back to certified searches in proper jurisdictions",
                    ],
                    [
                        "CMS NPPES API enriches provider identity for buyer account research",
                        "GET https://npiregistry.cms.hhs.gov/api/?version=2.1 with documented search parameters",
                        "Public API access is free; provider identity does not prove purchasing intent",
                        "Refresh leads monthly; cache identifiers and follow documented pagination constraints",
                        "Resolve business identities; fall back to registry pages and direct verification",
                    ],
                    [
                        "CMS Care Compare datasets support facility segmentation and account validation",
                        "Use https://data.cms.gov/provider-data/ and each dataset's published download controls",
                        "Public dataset access is free; preserve dataset-specific documentation and dates",
                        "Ingest dated releases monthly; prefer downloads over repeated row searches",
                        "Segment facility accounts; fall back to state licensing directories",
                    ],
                    [
                        "eBay Browse API provides active-listing context for secondary-market asking prices",
                        "GET https://api.ebay.com/buy/browse/v1/item_summary/search with authorized OAuth credentials",
                        "Developer access conditions and quotas apply; commercial agreements can differ",
                        "Refresh shortlisted comparisons weekly; respect assigned application call limits",
                        "Compare active offers only; fall back to licensed sold data or dealer quotes",
                    ],
                    [
                        "Siemens Healthineers documentation supports configuration and serviceability research",
                        "Visit https://www.siemens-healthineers.com/ and follow product-specific documentation routes",
                        "Public documents may be free; service access and contracts can cost",
                        "Check revision dates per asset; use authorized downloads and account permissions",
                        "Verify supported configurations; fall back to manufacturer support and supplied manuals",
                    ],
                    [
                        "Fluke Biomedical analyzers and Ansur support controlled biomedical test evidence",
                        "Use https://www.flukebiomedical.com/ for analyzer specifications and authorized software channels",
                        "Hardware, calibration, and applicable software licenses require current supplier quotations",
                        "Check calibration before use; retain local results without assuming cloud APIs",
                        "Produce repeatable test records; fall back to qualified independent biomedical laboratories",
                    ],
                    [
                        "Blancco sanitization tools support eligible removable-media erasure and evidence capture",
                        "Use https://www.blancco.com/ to obtain licensed products and supported-device requirements",
                        "Commercial licensing is quote-based; confirm per-asset costs and media compatibility",
                        "Verify current supported methods per job; restrict connectors to licensed interfaces",
                        "Document supported erasure; fall back to manufacturer procedures or controlled media destruction",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn source records into a bounded, auditable enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a compact asset ledger backed by SQLite or PostgreSQL, with object storage for photographs, manuals, contracts, and test artifacts. "
                    "The inventory key belongs to the desk, not to a marketplace listing that may disappear. "
                    "Create separate entities for asset, product family, seller organization, buyer requirement, source observation, work order, and disposition. "
                    "Within the asset record, preserve manufacturer text exactly as photographed alongside normalized aliases; store model, serial, device identifier, software version, installed options, probe or handpiece inventory, voltage, and physical location. "
                    "An older device without a UDI still needs an internal identity and a documented label photograph, not an invented identifier. "
                    "Record measurement units explicitly so a service interval expressed in operating hours does not become calendar months. "
                    "Use controlled statuses such as received, identity review, technical hold, buyer matched, and released. "
                    "A listing's description remains a seller assertion until independently supported. "
                    "Keep the raw source observation immutable and attach corrected interpretations as new records. "
                    "This design lets the second full-time operator explain why a bid changed without reconstructing an email chain. "
                    "It also keeps patient-bearing content outside the ordinary commercial research store, where broader contractor access would create unnecessary exposure."
                ),
                (
                    "Run the enrichment waterfall in order of cost and decision value. "
                    "First, normalize seller identity and device labels using deterministic rules, preserving every original value. "
                    "Second, query public product and recall records, joining by exact identifiers before attempting model aliases. "
                    "Third, establish seller authority, lien questions, and possession through contracts, debtor searches, and direct confirmation. "
                    "UCC searches must follow the debtor's legal identity and applicable filing jurisdiction; a convenient local search alone can miss relevant filings. "
                    "Fourth, request service history, manufacturer support status, option-transfer conditions, and an accessory manifest. "
                    "Fifth, obtain buyer-specific demand evidence and only then purchase specialist inspection or additional commercial enrichment. "
                    "A fuzzy match may propose a candidate record but must not clear a recall, transfer a software license, or release a device. "
                    "Use an explicit unresolved flag that blocks the affected decision while allowing unrelated research to continue. "
                    "Each step should have an exit condition: reject the lead, request a specific document, or advance with named evidence. "
                    "The desk gains more from rejecting an unsupported platform before freight is booked than from adding another hundred vaguely similar listings to its database. "
                    "Reserve expensive contractor time for assets that survive these inexpensive checks."
                ),
                (
                    "Schedule collectors as small independent jobs rather than one fragile overnight script. "
                    "Python urllib.request, json, sqlite3, hashlib, and logging can support an initial implementation without a sprawling integration stack. "
                    "Store credentials outside source code, restrict each token to its required function, and redact authorization headers from logs. "
                    "Use request timeouts, bounded retries, incremental checkpoints, and idempotent writes keyed by source plus record identifier and version. "
                    "A successful HTTP response still needs schema checks: an empty result caused by a changed query is not proof that recalls disappeared. "
                    "Track fetched records, rejected records, response age, parsing errors, and queue depth separately. "
                    "Add fixtures for aliases, duplicate listings, replaced serial photographs, withdrawn auctions, and records containing multiple devices. "
                    "When a listing changes price, retain both observations instead of rewriting the original underwriting evidence. "
                    "Send the sourcing operator one daily digest containing new actionable leads and changed material facts; send the operations operator stale evidence and blocked transitions. "
                    "Keep public research polling modest and contractor document requests consolidated. "
                    "For the four-person pod, a dependable twenty-record review queue beats a continuous stream of several thousand unranked alerts, especially when the same equipment is cross-listed through several brokers."
                ),
            ],
            "table": {
                "caption": "Six-Stage Enrichment Waterfall with Explicit Evidence and Stop Conditions",
                "headers": [
                    "Ordered enrichment stage and assigned owner",
                    "Required evidence and normalized data output",
                    "Failure condition that stops the affected decision",
                    "Fallback action that preserves operating capacity",
                ],
                "rows": [
                    [
                        "Stage one: sourcing operator establishes individual asset identity",
                        "Label photographs, serial transcription, model aliases, and accessory inventory",
                        "Photographs conflict with seller description or identify multiple mixed assets",
                        "Request targeted photographs before paying for additional specialist research",
                    ],
                    [
                        "Stage two: operations operator resolves product and recall context",
                        "Exact product matches, dated recall searches, and affected-range comparison",
                        "Recall scope remains unresolved for the specific configuration or serial",
                        "Obtain manufacturer confirmation and preserve the written response",
                    ],
                    [
                        "Stage three: specialist contractor reviews ownership and filing evidence",
                        "Seller authority, correct debtor names, jurisdiction searches, and release documents",
                        "Possession exists but authority or lien-release evidence remains deficient",
                        "Pause purchase commitment while seller supplies the missing transfer evidence",
                    ],
                    [
                        "Stage four: biomedical contractor reviews serviceability before physical testing",
                        "Service records, supported software, transferable options, and parts availability",
                        "Critical components lack support or required options cannot transfer",
                        "Reprice as an explicitly documented alternative disposition or reject",
                    ],
                    [
                        "Stage five: sourcing operator validates the intended buyer specification",
                        "Written configuration requirements, delivery location, installation needs, and budget",
                        "Buyer demand depends on unsupported use or incompatible accessories",
                        "Seek a qualified alternate buyer without changing the device claims",
                    ],
                    [
                        "Stage six: operations operator authorizes narrowly scoped paid diligence",
                        "Inspection scope, contractor quotation, expected decision value, and deadline",
                        "Diligence cost consumes the remaining acceptable contribution allowance",
                        "Reject the lead or negotiate revised acquisition economics first",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that prevent expensive false bargains",
                "body": "Use small evidence requests to expose large hidden costs before transport, inspection, or refurbishment commitments.",
                "items": [
                    "Request photographs of installed-option screens alongside the serial plate; an advertised feature may depend on a nontransferable license or missing module.",
                    "Ask for every probe, handpiece, cable, footswitch, and cart identifier; a complete accessory set can matter more than the chassis discount.",
                    "Search recalls through manufacturer aliases and the underlying product family, then resolve affected serial ranges with the recalling firm.",
                    "Compare the seller's legal name on the invoice, ownership documents, and relevant UCC search; a broker's listing account is not evidence of title.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the evidence envelope",
                    "action": "Assign an internal asset identifier and preserve the original listing, label images, and seller contact.",
                    "detail": "Record retrieval timestamps and content hashes; separate seller statements from independently verified facts.",
                },
                {
                    "step": 2,
                    "title": "Execute inexpensive public checks",
                    "action": "Resolve product identity, recall context, supplier identity, and buyer-account relevance.",
                    "detail": "Use exact identifiers first; route ambiguous matches into a named exception queue rather than silently accepting them.",
                },
                {
                    "step": 3,
                    "title": "Commission decision-specific specialist work",
                    "action": "Obtain ownership review, biomedical scope, decontamination evidence, and sanitization planning only for surviving candidates.",
                    "detail": "Give each contractor a fixed deliverable, deadline, access boundary, and rule for reporting an incomplete result.",
                },
                {
                    "step": 4,
                    "title": "Refresh material facts before commitment",
                    "action": "Recheck availability, recall status, transfer conditions, shipping scope, and the asset-level bid ceiling.",
                    "detail": "Preserve the decision packet and identify the operator responsible for resolving every remaining condition.",
                },
            ],
        },
        {
            "heading": "3. Join diagnostic tools to custody, sanitization, and release evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A diagnostic tool earns its place when it produces a defensible answer to a device-specific question. "
                    "An electrical safety analyzer can measure relevant leakage and protective-earth characteristics, but passing those checks does not establish image quality, therapeutic output, alarm behavior, or calibration accuracy. "
                    "For ultrasound, commission probe inspection and appropriate phantom testing under a documented protocol; for electrosurgical equipment, use suitable load testing and the manufacturer's procedures. "
                    "The biomedical contractor selects instruments, applicable limits, test conditions, and required competence rather than copying a universal checklist across device families. "
                    "Capture analyzer model, serial, calibration status, firmware, environmental conditions when material, technician identity, measured values, acceptance criteria, and exceptions. "
                    "Attach native result files as well as a readable report so exported summaries cannot conceal omitted steps. "
                    "Use manufacturer-authorized diagnostic access and licensed service tools; an inaccessible service menu is a cost or feasibility issue, not permission to bypass access controls. "
                    "Distinguish routine servicing from modifications that may change safety, performance specifications, or intended use. "
                    "Where activities make the operator a manufacturer or remanufacturer, evaluate the resulting FDA obligations, including applicable quality-system requirements under 21 CFR Part 820, before work begins rather than after the asset has been advertised."
                ),
                (
                    "Handle patient-bearing storage as a separate controlled workflow from commercial enrichment. "
                    "A powered-on workstation can expose patient names, study identifiers, network settings, or credentials even when its main application appears empty. "
                    "At intake, document storage components and isolate the device from ordinary office networks; do not import screenshots or disk images into the lead database. "
                    "Determine whether the desk is acting as a business associate for a covered entity, because HIPAA duties follow the actual relationship and information handled rather than the equipment's resale label. "
                    "Use appropriate contractual arrangements where required and implement device and media controls consistent with 45 CFR 164.310(d). "
                    "The sanitization contractor must reconcile confidentiality with continued clinical function: overwriting an embedded system can destroy licensed software, calibration data, or recovery partitions. "
                    "Obtain an OEM-supported procedure, verify media type and encryption behavior, and validate the result against the selected sanitization method. "
                    "A factory reset alone is insufficient evidence unless its documented behavior meets the required outcome. "
                    "If supported sanitization cannot be established, remove or replace media through an authorized service path or reject resale of the affected configuration. "
                    "Preserve serial-linked completion evidence without retaining the patient content that the workflow is meant to eliminate."
                ),
                (
                    "Treat decontamination, custody, and technical release as linked but distinct records. "
                    "A seller's statement that an asset was cleaned is not a device-specific reprocessing record, especially for probes, lumens, or components contacting tissue. "
                    "Require documented handling and cleaning procedures consistent with manufacturer instructions, the asset's previous use, and the contractor's scope. "
                    "Where workers have occupational exposure to blood or other potentially infectious materials, evaluate OSHA's Bloodborne Pathogens requirements under 29 CFR 1910.1030. "
                    "Record receiving condition, packaging, responsible parties, transport events, and any damage before a contractor signs a technical report. "
                    "The operations operator checks that the tested chassis, installed accessories, and final shipment share the same identifiers; swapping a probe after testing breaks that evidence chain. "
                    "An unresolved recall remains a hold until the applicable remedy or other disposition is documented. "
                    "Keep restricted health information out of buyer packets while including configuration, permitted test results, service scope, sanitization evidence, and warranty terms. "
                    "Release should require specific evidence, not a reassuring percentage score. "
                    "The four contractors supply bounded specialist outputs, while the two full-time operators retain responsibility for the commercial decision and inventory status. "
                    "That separation prevents a transport booking or an attractive offer from being mistaken for technical readiness."
                ),
            ],
            "table": {
                "caption": "Six Diagnostic and Custody Controls That Convert Inspection into Saleable Evidence",
                "headers": [
                    "Asset-specific control and responsible specialist",
                    "Required instrument or primary evidence source",
                    "Stored result and specific acceptance basis",
                    "Failure response before advertising or shipment",
                ],
                "rows": [
                    [
                        "Electrical safety testing by the qualified biomedical contractor",
                        "Calibrated Fluke Biomedical analyzer and applicable manufacturer test procedure",
                        "Serial-linked measurements compared with documented device-specific acceptance limits",
                        "Hold the asset and quote corrective work before release",
                    ],
                    [
                        "Diagnostic imaging performance review by a modality-qualified technician",
                        "Appropriate phantom, probe inspection tools, and supported diagnostic software",
                        "Recorded image-quality observations, probe findings, and prescribed test outcomes",
                        "Reject defective probes or reprice with explicitly identified replacements",
                    ],
                    [
                        "Surgical output and accessory testing by a qualified specialist",
                        "Suitable analyzer loads, manufacturer procedures, and complete accessory manifest",
                        "Measured outputs and accessory compatibility tied to tested configuration",
                        "Block shipment when the final configuration differs from tested equipment",
                    ],
                    [
                        "Patient-data sanitization by the restricted-access media contractor",
                        "OEM-supported procedure and compatible licensed sanitization or destruction method",
                        "Media identifiers, selected method, validation outcome, and completion record",
                        "Replace supported media or reject the affected resale configuration",
                    ],
                    [
                        "Decontamination review by the designated handling and transport contractor",
                        "Manufacturer cleaning instructions and device-specific processing records",
                        "Documented process, responsible party, date, and handling restrictions",
                        "Quarantine the asset until suitable processing evidence is established",
                    ],
                    [
                        "Recall and configuration release review by the operations operator",
                        "Current recall records, corrective-action documents, and final serial photographs",
                        "Resolved affected-range analysis and evidence matching the shipped accessories",
                        "Keep inventory on hold until every material mismatch is resolved",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before committing or releasing capital",
                "body": "Apply these checks at the relevant purchase and shipment decisions; an unresolved condition remains visible rather than disappearing into a blended risk score.",
                "items": [
                    "Identity and transfer: reconcile chassis and accessory identifiers, seller authority, relevant lien findings, and transferable software rights.",
                    "Safety and function: resolve applicable recalls, confirm device-specific inspection scope, and match accepted test evidence to the final configuration.",
                    "Data and handling: confirm supported sanitization, required contractual responsibilities, decontamination evidence, and restricted-access custody records.",
                    "Economics and delivery: refresh buyer requirements, binding acquisition terms, freight scope, remaining work costs, and the approved asset-level cash commitment.",
                ],
            },
        },
        {
            "heading": "4. Price the information advantage against the canonical operating economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep the scorecard fixed while evaluating tools. "
                    "Conservative annual gross equipment resale proceeds are $250,000 at a 10% net margin, producing $25,000 owner net profit with two full-time staff and four contractors. "
                    "Base proceeds are $1,025,000 at 16.0%, producing $164,000 with the same four-person pod. "
                    "Scaled proceeds are $1,800,000 at 22%, producing $396,000 with three full-time staff and five contractors. "
                    "The corresponding total expense envelopes are $225,000, $861,000, and $1,404,000; acquisition and refurbishment are already inside those envelopes. "
                    "Do not subtract acquisition twice or treat equipment purchase principal as separate customer transaction volume. "
                    "The stated startup capital range is $20,000 to $95,000, monthly operating expenditure range is $4,000 to $18,000, and first-deal horizon is three to nine months. "
                    "Those ranges are planning constraints, not additional amounts to append mechanically to each scenario. "
                    "A proposed subscription, inspection package, or contractor retainer must either fit the modeled expense envelope through an identified allocation or appear in a separately labeled sensitivity. "
                    "Information tooling does not automatically improve the canonical margin. "
                    "It earns its budget by preventing measurable losses, reducing paid work, or enabling documented equipment sales without exceeding the team's delivery capacity."
                ),
                (
                    "Underwrite individual assets with a cash bridge that keeps contribution distinct from annual owner profit. "
                    "For an illustrative $40,000 resale, $24,000 acquisition, $4,000 refurbishment, $2,000 freight, and $1,000 selling and warranty provision leave $9,000 before shared overhead and other annual expenses. "
                    "That $9,000 is transaction contribution, not the Base case's 16.0% owner margin applied to a single device. "
                    "If inspection identifies another $3,000 repair, contribution falls to $6,000 unless acquisition price or another cost changes. "
                    "Use this bridge to value research: a $300 specialist review is attractive when it answers a material question before an irreversible purchase, but its value is not established by counting database fields. "
                    "For a separate tooling sensitivity, an incremental $250 monthly subscription costs $3,000 annually. "
                    "At unchanged Base revenue and all other costs, owner profit would become $161,000, so preserving the canonical $164,000 requires an equal documented offset or a different operating change. "
                    "Do not bury that subscription inside an asserted automation benefit. "
                    "Track prevented purchases using the original bid packet and the discovered defect, but distinguish such avoided exposure from realized cash savings. "
                    "Unspent speculative capital is useful, yet it is not additional booked equipment revenue."
                ),
                (
                    "Run a weekly operating review around inventory age, evidence completeness, contractor turnaround, and cash committed to unresolved assets. "
                    "The sourcing operator owns qualified opportunities and buyer confirmations; the operations operator owns blocked records, release packets, and refresh failures. "
                    "Measure contractor workload in inspection hours, sanitization jobs, transport events, and specialist reviews rather than assuming four contractors equal four full-time employees. "
                    "Limit simultaneous acquisitions to the number the pod can inspect, store, document, and sell within its cash capacity. "
                    "For diagnostic replacement sourcing, review manufacturer support and installed-option risks before negotiating collection. "
                    "For surgical surplus recovery, review lot-level accessory completeness and decontamination evidence before assigning a blended bid. "
                    "For veterinary/aesthetic matching, review intended use, buyer requirements, and device-specific obligations before promising compatibility. "
                    "Use age-based alerts to trigger a documented price review, parts disposition assessment, or buyer campaign; never erase a failed asset from the denominator. "
                    "Compare actual gross resale proceeds and total expenses against the chosen canonical case every month. "
                    "Move to the Scaled staffing assumption only when additional throughput supports three full-time staff and five contractors within the $1,404,000 expense envelope. "
                    "The operational advantage is a shorter, better-supported decision cycle, not a larger database whose inspection backlog ties up the same scarce capital."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Tooling Sensitivities Without Revenue-Basis Drift",
                "headers": [
                    "Scenario or explicitly separate operating illustration",
                    "Revenue basis and exact expense reconciliation",
                    "Profit or contribution interpretation for operators",
                    "Staffing implication and required management action",
                ],
                "rows": [
                    [
                        "Conservative canonical case for the equipment resale operation",
                        "$250,000 gross proceeds less $225,000 total modeled expenses",
                        "$25,000 annual owner net profit at 10% net margin",
                        "Two full-time staff plus four contractors; keep tools inside expenses",
                    ],
                    [
                        "Base canonical case for the same four-person operating pod",
                        "$1,025,000 gross proceeds less $861,000 total modeled expenses",
                        "$164,000 annual owner net profit at 16.0% net margin",
                        "Two full-time staff plus four contractors; prioritize bounded specialist queues",
                    ],
                    [
                        "Scaled canonical case with the specified eight-person operating team",
                        "$1,800,000 gross proceeds less $1,404,000 total modeled expenses",
                        "$396,000 annual owner net profit at 22% net margin",
                        "Three full-time staff plus five contractors; validate throughput before expansion",
                    ],
                    [
                        "Illustrative individual transaction before allocation of shared annual overhead",
                        "$40,000 sale less $24,000 acquisition, $4,000 refurbishment, $2,000 freight, $1,000 provision",
                        "$9,000 transaction contribution before shared overhead and other annual expenses",
                        "Use contractor findings to revise the bid ceiling before commitment",
                    ],
                    [
                        "Illustrative repair surprise affecting only the example transaction bridge",
                        "$9,000 initial contribution less $3,000 additional required repair expenditure",
                        "$6,000 revised transaction contribution before shared overhead and other annual expenses",
                        "Renegotiate acquisition or reject when remaining contribution becomes inadequate",
                    ],
                    [
                        "Separate Base sensitivity for an unoffset incremental software subscription",
                        "$164,000 canonical profit less $3,000 annual incremental subscription expenditure",
                        "$161,000 sensitivity profit; canonical Base remains $164,000 by definition",
                        "Document an equal offset before claiming unchanged canonical economics",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The valuable database is the one that stops a bad purchase before the truck is booked.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Assign the three mapped plays to named owners within the two-full-time, four-contractor pod, and define each contractor's evidence deliverable.",
        "Create an internal asset ledger with immutable source observations, label photographs, serial-linked accessories, timestamps, and restricted document access.",
        "Configure permitted public-source collectors with cached queries, current quota checks, bounded retries, freshness alerts, and manual fallback routes.",
        "Run identity, recall, ownership, supportability, and buyer-fit checks before commissioning expensive physical inspection or transport.",
        "Require device-specific biomedical results, supported sanitization, decontamination records, and final configuration reconciliation before shipment.",
        "Reconcile monthly resale proceeds and total expenses to the selected canonical case, and label every incremental tooling cost as an allocation or separate sensitivity.",
    ],
    "statutory_citations": [
        {
            "title": "21 U.S.C. 360 — Registration of producers of drugs or devices",
            "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title21-section360&num=0&edition=prelim",
            "relevance": "Evaluate registration and listing duties against the actual activities performed; a public listing does not establish product approval or individual-asset readiness.",
        },
        {
            "title": "21 CFR 807.3 — Establishment registration and device listing definitions",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-A/section-807.3",
            "relevance": "Use the regulatory definitions when assessing whether refurbishment, processing, or other activities create obligations beyond ordinary resale.",
        },
        {
            "title": "21 CFR Part 820 — Quality Management System Regulation",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820",
            "relevance": "Assess applicable manufacturer quality-system duties when activities constitute manufacturing or remanufacturing rather than assuming every resale desk has identical obligations.",
        },
        {
            "title": "45 CFR 164.310(d) — Device and media controls",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": "For regulated entities and applicable business-associate activities, implement appropriate controls for electronic protected health information on devices and media, including disposal and reuse.",
        },
        {
            "title": "45 CFR 164.502(e) — Disclosures to business associates",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502",
            "relevance": "Determine whether patient-data handling makes the desk a business associate and establish the required assurances before handling protected information.",
        },
        {
            "title": "29 CFR 1910.1030 — Bloodborne Pathogens",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1030",
            "relevance": "Where occupational exposure exists, apply the required exposure-control, work-practice, training, and protective measures to receiving and handling used equipment.",
        },
        {
            "title": "California Commercial Code Section 9315 — Secured party rights on disposition of collateral",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=COM&sectionNum=9315.",
            "relevance": "A security interest can continue after disposition subject to statutory exceptions; investigate relevant filings and obtain appropriate release evidence rather than equating possession with unencumbered ownership.",
        },
        {
            "title": "California Commercial Code Section 9307 — Location of debtor",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=COM&sectionNum=9307.",
            "relevance": "Apply the relevant debtor-location rules when determining filing jurisdictions; use the governing state's enacted provisions rather than searching only where the equipment sits.",
        },
    ],
}
