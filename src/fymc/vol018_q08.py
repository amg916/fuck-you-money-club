from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small land flipping desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Recorder Evidence, Regrid and ATTOM Enrichment, FEMA and USFWS Screens, and Title-Insured Parcel Decisions",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #6, Land Flipping, ranks #15 with a 86/100 Money-to-Manpower "
        "Score. Its information advantage comes from resolving parcel identity, "
        "ownership, access, buildability, and resale evidence before committing "
        "capital. This chapter maps six plays: rural discount resales, infill "
        "builder lots, tax-delinquent owner purchases, estate-owned acquisitions, "
        "access-and-title cures, and minor subdivisions. A 1 FT + 3 C pod combines "
        "official records, selective commercial enrichment, and reproducible GIS "
        "checks rather than buying every available subscription. Conservative, "
        "Base, and Scaled annual owner profits remain $24,000, $157,250, and "
        "$375,000 respectively; gross parcel sale proceeds are the revenue basis. "
        "The directory and operating sequence below identify acquisition costs, "
        "source delays, request controls, fallback evidence, and the precise "
        "questions automation must leave for qualified human review."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$200,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "12% net margin; $24,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$850,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "18.5% net margin; $157,250 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,500,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "25% net margin; $375,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence-ranked directory before purchasing parcel feeds",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one county and build a source register, not a nationwide "
                    "spreadsheet of loosely matched parcels. The examples below use "
                    "Maricopa County and Arizona institutions to make access paths "
                    "concrete; replace those local sources when entering another "
                    "jurisdiction. Store county FIPS, the assessor's original parcel "
                    "identifier, a separately normalized identifier, source URL, retrieval "
                    "time, effective date, and document reference. Preserve leading zeros "
                    "and punctuation in the original field. A parcel split can retire an "
                    "identifier while the recorder continues indexing documents under "
                    "an older legal description. Consequently, assessor ownership is a "
                    "discovery signal, a recorded instrument is transaction evidence, "
                    "and a title commitment is a separate examination with exceptions "
                    "and requirements. None substitutes for a boundary survey. Assign "
                    "each disputed fact to its appropriate source: taxes to the "
                    "treasurer, permitted uses to the planning authority, recorded "
                    "easement language to the instrument, and insurability to the title "
                    "provider. The principal owns the source register and decides which "
                    "disagreements block an offer. The GIS contractor collects and "
                    "normalizes evidence without silently resolving conflicts. This "
                    "separation prevents an attractive commercial map from becoming an "
                    "unsupported ownership, access, or buildability assertion in a "
                    "buyer presentation."
                ),
                (
                    "Treat the directory's cost descriptions as purchasing categories "
                    "rather than fixed vendor quotes. Public viewing often costs "
                    "nothing, while certified copies, bulk extracts, survey work, and "
                    "commercial API rights have separate charges. Request written "
                    "pricing for the actual geography, fields, annual volume, caching "
                    "rights, and permitted downstream use. A website subscription does "
                    "not automatically include API access or permission to resell "
                    "records. Refresh latency also has two clocks: when an event "
                    "occurred and when the source published it. Capture both whenever "
                    "available. A deed recorded yesterday may appear promptly in a "
                    "recorder search but much later in an assessor roll or commercial "
                    "ownership feed. Before sending offers, inspect the latest recorder "
                    "and tax information for the shortlisted parcels instead of "
                    "relying on last month's enriched export. Use published bulk "
                    "downloads first, documented APIs second, and ordinary manual "
                    "retrieval when automated access is unavailable. Start permitted "
                    "API work with one worker, honor documented limits and Retry-After, "
                    "and stop repeated failures for investigation. Never turn a blocked "
                    "portal into a scraping contest. The fallback is an authorized "
                    "records request or a staff-assisted document order, with the "
                    "resulting delay reflected in the acquisition schedule."
                ),
                (
                    "Use hazard and physical-condition tools to generate questions, "
                    "not automatic conclusions about development rights. FEMA's "
                    "effective flood information can identify mapped hazards, but "
                    "local floodplain rules, map revisions, elevation evidence, and "
                    "engineering still control the practical project. USFWS wetlands "
                    "mapping is an inventory rather than a parcel-specific federal "
                    "jurisdiction determination. Soil survey interpretations describe "
                    "mapped soil units; they do not replace a septic evaluation or "
                    "geotechnical investigation. EPA records flag reported facilities "
                    "and cleanup activity, while a clean search does not establish "
                    "clean land. For transactions seeking applicable CERCLA liability "
                    "protections, have an environmental professional address the "
                    "conditions and timing under 40 CFR Part 312; several specified "
                    "components require updating within 180 days before acquisition, "
                    "and the broader inquiry generally must occur within one year. "
                    "Do not advertise a browser search as that inquiry. Likewise, "
                    "BLM patents illuminate historic conveyances but do not resolve "
                    "every current reservation or access question. The GIS contractor "
                    "screens these layers, the survey and civil coordinator scopes "
                    "field questions, and the title and closing contractor examines "
                    "recorded interests. The principal funds deeper work only when "
                    "the remaining spread supports its cost and elapsed time."
                ),
            ],
            "table": {
                "caption": "Eighteen named sources: access, cost category, latency, request hygiene, and fallback evidence",
                "headers": [
                    "Named source and operational role",
                    "Exact access method",
                    "Cost category and use boundary",
                    "Refresh latency to record",
                    "Request discipline",
                    "Fallback and evidentiary limit",
                ],
                "rows": [
                    [
                        "Maricopa County Assessor for parcel identity and assessed ownership",
                        "Open https://mcassessor.maricopa.gov/ and search parcel number or owner",
                        "Public lookup is free; confirm separate bulk extract terms",
                        "Roll and transfer processing create event-to-publication delays",
                        "Use offered exports; do not automate undocumented browser endpoints",
                        "Compare recorded deeds when assessed ownership trails a transfer",
                    ],
                    [
                        "Maricopa County Recorder for deeds, easements, and recorded plats",
                        "Open https://recorder.maricopa.gov/ and select recorded document search",
                        "Search access and copy charges follow the posted fee schedule",
                        "Record recording date separately from search-index availability",
                        "Search narrowly by instrument or party; respect portal controls",
                        "Order official copies when images or indexing are incomplete",
                    ],
                    [
                        "Maricopa County Treasurer for balances and tax-sale research",
                        "Open https://treasurer.maricopa.gov/ and search the parcel account",
                        "Public account lookup is free; obtain transaction-specific payoff figures",
                        "Payments, penalties, and posted balances can change between checks",
                        "Recheck shortlisted accounts before offers and before closing",
                        "Request a dated payoff when posted balances need reconciliation",
                    ],
                    [
                        "Maricopa County Planning and Development for unincorporated land controls",
                        "Open https://www.maricopa.gov/ and select Planning and Development",
                        "Published maps are free; applications and written determinations may cost",
                        "Code amendments and case decisions update on separate schedules",
                        "Retrieve applicable code text; verify jurisdiction before requesting interpretation",
                        "Use the relevant city's planning department for incorporated parcels",
                    ],
                    [
                        "Maricopa County Superior Court for probate case discovery",
                        "Open https://www.clerkofcourt.maricopa.gov/ and navigate to case information",
                        "Public case access varies; certified document orders carry posted charges",
                        "Docket entry timing differs from document availability and finality",
                        "Respect restricted records; request documents through authorized court channels",
                        "Obtain current authority documents rather than relying on docket summaries",
                    ],
                    [
                        "Arizona Corporation Commission eCorp for entity identity and filings",
                        "Open https://ecorp.azcc.gov/ and search the exact entity name",
                        "Public entity searches are free; certified records have separate fees",
                        "Filing acceptance and search publication can occur at different times",
                        "Search exact names and entity identifiers before broad name variants",
                        "Request organizational authority evidence; registry status alone proves little",
                    ],
                    [
                        "Maricopa County Department of Transportation for public roadway evidence",
                        "Open https://www.maricopa.gov/ and navigate to Transportation road information",
                        "Published resources are free; specific records requests may incur charges",
                        "Accepted roadway status and published map revisions can diverge",
                        "Request the named road segment and supporting acceptance documents",
                        "Recorder instruments and surveys address rights beyond roadway map coverage",
                    ],
                    [
                        "FEMA Map Service Center for effective flood hazard products",
                        "Open https://msc.fema.gov/portal/home and search location or map panel",
                        "Federal map viewing and available product downloads are free",
                        "Use panel effective dates and applicable map revision dates",
                        "Download relevant panels once; cache files with retrieval timestamps",
                        "Consult the local floodplain administrator for parcel-specific project questions",
                    ],
                    [
                        "USFWS National Wetlands Inventory for mapped wetland screening",
                        "Open https://www.fws.gov/program/national-wetlands-inventory/wetlands-mapper and use mapper or downloads",
                        "Federal inventory viewing and published spatial downloads are free",
                        "Project imagery dates and inventory publication dates vary geographically",
                        "Prefer regional downloads; avoid repeated identical map service queries",
                        "Commission delineation and agency review when the proposed activity requires",
                    ],
                    [
                        "USDA NRCS Web Soil Survey for soils and limitations",
                        "Open https://websoilsurvey.nrcs.usda.gov/app/ and define the area of interest",
                        "Public soil reports and available soil data downloads are free",
                        "Survey vintage and updated interpretations vary by survey area",
                        "Save the selected area report instead of repeatedly regenerating it",
                        "Use local septic evaluation and geotechnical testing for design decisions",
                    ],
                    [
                        "USGS National Map Downloader for elevation and terrain inputs",
                        "Open https://apps.nationalmap.gov/downloader/ and select elevation product coverage",
                        "Federal elevation downloads are free; processing creates local resource costs",
                        "Check acquisition year, publication date, resolution, and vertical reference",
                        "Download intersecting tiles once and retain the accompanying metadata",
                        "Order current survey elevations when available terrain resolution is insufficient",
                    ],
                    [
                        "EPA Envirofacts for reported environmental facilities and program records",
                        "Open https://enviro.epa.gov/ and select relevant Envirofacts search resources",
                        "Public searches and supported federal data access are free",
                        "Underlying program update cycles differ; inspect each record's dates",
                        "Use documented interfaces and bounded geography rather than unrestricted harvesting",
                        "Check state cleanup records and commission environmental professional review",
                    ],
                    [
                        "BLM General Land Office Records for historic patents and surveys",
                        "Open https://glorecords.blm.gov/ and search patents or survey records",
                        "Public search and available document image viewing are free",
                        "Historic document dates differ from later digitization and indexing",
                        "Search township, range, section, and names to constrain results",
                        "Current title examination must address later conveyances and reservations",
                    ],
                    [
                        "U.S. Census TIGER/Line for geographic joins and area context",
                        "Open https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html and select release",
                        "Published federal geographic downloads are free for operator analysis",
                        "Release vintage is periodic and cannot establish current road rights",
                        "Cache release files locally and preserve geographic identifier fields",
                        "County engineering and recorded instruments establish stronger access evidence",
                    ],
                    [
                        "Regrid parcel products for normalized geometry and owner screening",
                        "Open https://regrid.com/ and request the appropriate data or API plan",
                        "Commercial access requires plan-specific pricing, credits, and permitted-use terms",
                        "County source vintage and vendor ingestion timing differ by coverage",
                        "Use issued credentials and contractual quotas; cache where expressly permitted",
                        "Return to assessor geometry and recorder evidence for disputed attributes",
                    ],
                    [
                        "ATTOM property APIs for transaction enrichment and comparable discovery",
                        "Open https://api.developer.attomdata.com/ and use documented property API endpoints",
                        "Commercial endpoint access and call allowances depend on the contract",
                        "Sale-event coverage and publication delay differ across local recording systems",
                        "Send required credentials securely; meter requests by endpoint and parcel",
                        "Verify consideration, parcel allocation, and transaction context through primary records",
                    ],
                    [
                        "First American DataTree for document discovery and property research",
                        "Open https://www.datatree.com/ and use the contracted property research interface",
                        "Subscription and document retrieval charges depend on purchased service rights",
                        "Index and image coverage depend on source jurisdictions and product feeds",
                        "Use licensed export features; browser access does not imply automation rights",
                        "Order missing instruments from the recorder and obtain separate title services",
                    ],
                    [
                        "QGIS desktop for geometry, coordinate systems, and parcel diagnostics",
                        "Download from https://qgis.org/ and run Check Validity in Processing Toolbox",
                        "Desktop software is free; staff time and source licenses still cost",
                        "Results inherit input vintage and must retain the processing timestamp",
                        "Process downloaded layers locally and limit unnecessary live service requests",
                        "Compare official plats and licensed surveys before treating boundaries as definitive",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn six plays into a paid-enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Map the six plays to distinct evidence requirements instead of "
                    "using one universal land score. Rural discount resales need "
                    "credible access and sales evidence for genuinely comparable "
                    "acreage. Infill builder lots need jurisdiction, setbacks, utility "
                    "serviceability, and a plausible building envelope. Tax-delinquent "
                    "owner purchases need current balances and owner authority; they "
                    "are negotiated acquisitions, not an assumption that a tax lien "
                    "conveys ownership. Estate-owned acquisitions require the correct "
                    "representative and transaction authority, not merely a deceased "
                    "name on an assessor record. Access-and-title cures require a "
                    "documented, executable cure whose cost and counterparties are "
                    "understood before relying on improved resale value. Minor "
                    "subdivisions require local division rules, state definitions, "
                    "survey work, service constraints, and recordable results. Arizona's "
                    "subdivision definitions in A.R.S. 32-2101 illustrate why a desk "
                    "cannot treat a locally labeled minor division as automatically "
                    "outside every state requirement. Assign one primary play to each "
                    "candidate, with secondary opportunities recorded separately. This "
                    "makes rejection reasons measurable. An inaccessible rural tract "
                    "must not quietly become an access-cure opportunity unless the "
                    "principal approves a new evidence budget and a specific cure "
                    "path. Otherwise automation simply relabels risk until every "
                    "parcel appears investable."
                ),
                (
                    "Run enrichment from cheapest disqualifier to most expensive "
                    "confirmation. Stage one uses an authorized county extract to "
                    "remove duplicates, unsuitable acreage, obvious jurisdiction "
                    "mismatches, and retired parcel identifiers. Stage two joins "
                    "public hazard layers, tax records, and recorded subdivision "
                    "references. Stage three buys commercial transaction attributes "
                    "only for surviving parcels, then checks the underlying sales "
                    "against deed type, parcel count, improvement status, and transfer "
                    "context. Stage four commissions the targeted title, survey, "
                    "civil, or environmental work needed by the actual play. For "
                    "an illustrative processing batch, 5,000 source parcels might "
                    "become 600 geographic matches, 120 desktop survivors, 30 paid "
                    "enrichments, and six document-intensive reviews. Those counts "
                    "describe workload, not expected closings or a replacement "
                    "revenue forecast. Set a maximum purchased-data cost per reviewed "
                    "candidate before releasing the batch. If a commercial source "
                    "returns a bundled sale of ten parcels, do not assign its entire "
                    "consideration to each component. If consideration is missing "
                    "or protected by local disclosure practice, retain the sale as "
                    "unpriced evidence and seek another supported comparable. The "
                    "waterfall saves money by preserving uncertainty rather than "
                    "manufacturing a price from incomplete fields."
                ),
                (
                    "Keep the four-person pod small by assigning decisions as carefully "
                    "as tasks. The full-time principal sets buying criteria, negotiates, "
                    "allocates capital, and approves releases of funds. Contractor one "
                    "handles GIS, source ingestion, and comparable packets. Contractor "
                    "two coordinates licensed survey and civil investigations within "
                    "the qualifications actually held, arranging additional specialist "
                    "services only when required. Contractor three provides title and "
                    "closing coordination through properly qualified providers. Do "
                    "not count a data subscription as a person or describe the pod "
                    "as able to perform every regulated service internally. Escalated "
                    "professional services are purchased transaction costs, with "
                    "scope and price approved before ordering. At the canonical "
                    "Conservative and Base levels, staffing remains 1 FT + 3 C; "
                    "Scaled uses 2 FT + 4 C. Size each review queue to available "
                    "decision hours rather than accumulating thousands of unresolved "
                    "leads. Give each exception an owner, next evidence request, due "
                    "date, and spending ceiling. A weekly twenty-minute exception "
                    "meeting should decide whether to reject, investigate, or "
                    "negotiate a conditional acquisition. It should not become a "
                    "tour of maps. The operational advantage is fewer unsupported "
                    "commitments per completed deal, not a larger raw contact list."
                ),
            ],
            "table": {
                "caption": "Six mapped land plays and their distinct enrichment decisions",
                "headers": [
                    "Mapped operator play",
                    "Lowest-cost qualifying evidence",
                    "Paid confirmation and responsible role",
                    "Specific rejection or escalation trigger",
                ],
                "rows": [
                    [
                        "Rural discount resales using documented acreage and credible access",
                        "County geometry, recorded access references, and verified acreage comparables",
                        "GIS contractor prepares comparisons; title provider examines access-related interests",
                        "Reject unsupported road rights or prices derived from improved properties",
                    ],
                    [
                        "Infill builder lots matched to a feasible building envelope",
                        "Planning jurisdiction, setbacks, lot dimensions, and utility provider service records",
                        "Survey and civil coordinator confirms envelope and obtains service estimates",
                        "Escalate utility extension costs that consume the documented resale spread",
                    ],
                    [
                        "Tax-delinquent owner purchases negotiated directly with authorized property owners",
                        "Treasurer balances cross-checked against recorder ownership and parcel identity",
                        "Title and closing contractor obtains current payoff and ownership requirements",
                        "Reject transactions whose payoff and acquisition cost exceed buying limits",
                    ],
                    [
                        "Estate-owned acquisitions supported by current authority to convey",
                        "Probate case references matched to deeds and the correct estate",
                        "Title provider and qualified counsel resolve authority and conveyance requirements",
                        "Pause offers requiring signatures from people without demonstrated authority",
                    ],
                    [
                        "Access-and-title cures with documented counterparties and executable remedies",
                        "Recorded exceptions, easement instruments, legal descriptions, and adjoining ownership",
                        "Title provider and licensed surveyor define the insurable cure",
                        "Reject speculative neighbor cooperation or cures without a closing sequence",
                    ],
                    [
                        "Minor subdivisions producing recordable and practically saleable resulting parcels",
                        "Local division rules, state definitions, dimensions, access, and service constraints",
                        "Survey and civil coordinator prices required plans, reviews, and improvements",
                        "Escalate road construction or agency timelines beyond the carrying budget",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four ways experienced land desks avoid buying misleading certainty",
                "body": "Use these tactics before increasing lead volume or purchasing another national dataset.",
                "items": [
                    "Search recorder documents under both the current parcel and its parent legal description after a split; indexing often follows the older description.",
                    "For an access claim, capture the easement's instrument number, beneficiary language, route, and exceptions rather than saving only a road screenshot.",
                    "Ask a utility provider for the service point and extension scope; a line visible across the street does not establish an inexpensive connection.",
                    "Separate vacant-lot sales from improved, assemblage, related-party, and bundled transfers before calculating acreage or frontage price distributions.",
                ],
            },
        },
        {
            "heading": "3. Make the pipeline reproducible and expose silent data failures",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement a small evidence store before adopting elaborate "
                    "orchestration. Python's csv, json, sqlite3, hashlib, urllib.request, "
                    "and datetime modules can ingest permitted exports and documented "
                    "API responses without a separate application platform. Preserve "
                    "the original response or downloaded file, calculate a SHA-256 "
                    "digest, and load normalized records into SQLite inside a "
                    "transaction. Use separate tables for parcels, source observations, "
                    "recorded instruments, comparable sales, review decisions, and "
                    "request costs. An observation should include the asserted field, "
                    "value, source, retrieval timestamp, effective date when published, "
                    "and evidence location. Missing attributes stay explicitly empty "
                    "in the database with a reason code; they must never become "
                    "invented ownership or buildability facts. Keep original parcel "
                    "identifiers as text and use county plus identifier as the initial "
                    "business key. Add parent-child links for splits and merges "
                    "rather than rewriting history. Store geographic data with its "
                    "coordinate reference system and export review layers for QGIS. "
                    "Calculate area only in an appropriate projected reference system "
                    "or with a suitable geodesic method; degree-based polygon area "
                    "is not acreage. Keep credentials outside source files, redact "
                    "them from logs, and restrict raw owner-contact data to the "
                    "people performing authorized acquisition work."
                ),
                (
                    "Make every batch idempotent and observable. A source observation "
                    "key can combine the source, source record identifier, publication "
                    "version, and payload digest so rerunning a download does not "
                    "create duplicate evidence. Log HTTP status, elapsed time, returned "
                    "record count, retry count, bytes, and metered credits without "
                    "recording secrets. Follow the provider's pagination mechanism "
                    "until its documented completion condition is reached; a successful "
                    "first page is not a complete county extract. Reject a load when "
                    "required columns disappear, record counts collapse unexpectedly, "
                    "or parcel identifiers lose leading zeros. Use bounded retries "
                    "for temporary failures, exponential backoff with jitter, and "
                    "Retry-After where supplied. A permission failure requires "
                    "credential or entitlement review, not a faster retry loop. "
                    "Schedule source-specific refreshes: current tax and recorder "
                    "checks near transaction decisions, periodic commercial updates "
                    "under the purchased plan, and hazard-layer replacement when "
                    "published versions change. Keep the previous successful snapshot "
                    "available for comparison. A changed owner, new recorded "
                    "instrument, revised flood layer, or altered parcel geometry "
                    "should create a review task, not automatically change an active "
                    "offer. The principal needs a short exception queue with evidence "
                    "links, not a dashboard that silently overwrites yesterday's "
                    "underwriting."
                ),
                (
                    "Diagnose suspicious results with independent checks before tuning "
                    "the scoring formula. In QGIS, inspect invalid polygons, duplicate "
                    "features, multipart parcels, slivers, and mismatched coordinate "
                    "systems. Compare calculated area with assessor acreage, but "
                    "investigate material differences rather than declaring one "
                    "source correct by default. A centroid can fall outside an "
                    "irregular parcel or on the wrong side of a road; use an "
                    "interior point for display and the actual polygon for "
                    "intersections. Test whether the flood layer intersects the "
                    "proposed building area, not merely whether any corner of the "
                    "property touches a mapped zone. Comparable diagnostics should "
                    "flag repeated sale identifiers, implausible unit prices, "
                    "multiple parcels sharing full consideration, and listings "
                    "mistaken for closed sales. Retain rejected comparable evidence "
                    "with the rejection reason so another analyst does not "
                    "reintroduce it next month. Before scaling, create a small "
                    "labeled test set containing an ordinary parcel, a split, a "
                    "bundled sale, a disputed-access tract, and a constrained infill "
                    "lot. Every pipeline change should reproduce the expected "
                    "warnings. This is a more useful quality test than increasing "
                    "a model's apparent precision while its ownership joins and "
                    "area calculations remain wrong."
                ),
            ],
            "table": {
                "caption": "Six diagnostic tests that catch expensive parcel-data errors",
                "headers": [
                    "Observed failure signature",
                    "Reproducible diagnostic action",
                    "Evidence required for resolution",
                    "Operator response and accountable role",
                ],
                "rows": [
                    [
                        "Different counties produce matching normalized parcel identifier strings",
                        "Group records by identifier and compare county FIPS values",
                        "Retained source identifiers and county-qualified keys demonstrate distinct properties",
                        "GIS contractor repairs joins before any affected offer packet proceeds",
                    ],
                    [
                        "Polygon acreage differs materially from the assessor's stated acreage",
                        "Inspect reference systems, multipart features, geometry validity, and unit conversion",
                        "Official plat and survey evidence clarify boundaries and acreage differences",
                        "Survey coordinator scopes verification before the principal prices usable acreage",
                    ],
                    [
                        "One sale appears repeatedly with identical total recorded consideration",
                        "Group by instrument reference and inspect the complete conveyed parcel set",
                        "Recorded instrument and supported allocation establish usable comparable treatment",
                        "GIS contractor excludes unsupported component prices from the valuation set",
                    ],
                    [
                        "Assessor ownership conflicts with the most recent recorded conveyance",
                        "Compare recording dates, grantee names, legal descriptions, and parcel histories",
                        "Current instrument chain and title examination resolve the acquisition counterparty",
                        "Title and closing contractor addresses requirements before signatures are relied upon",
                    ],
                    [
                        "A nightly extract suddenly returns only one page of records",
                        "Inspect pagination tokens, completion markers, counts, and response schema changes",
                        "Documented endpoint behavior and complete archived responses support the repaired load",
                        "GIS contractor quarantines the batch and preserves the previous accepted snapshot",
                    ],
                    [
                        "A parcel score improves after a missing hazard layer disappears",
                        "Check source coverage, service errors, dataset vintage, and join completeness",
                        "Successful layer retrieval and explicit coverage checks distinguish absence from failure",
                        "Principal blocks automatic repricing until the screening evidence is restored",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register and retrieve authorized inputs",
                    "action": "Record source terms, geography, fields, publication dates, and request limits before ingestion.",
                    "detail": "Save original files or responses with retrieval timestamps and digests; document the county-specific fallback contact.",
                },
                {
                    "step": 2,
                    "title": "Normalize without erasing source evidence",
                    "action": "Load county-qualified identifiers, original values, geometry references, and linked observations into SQLite.",
                    "detail": "Preserve parent-child parcel relationships and reject malformed loads before they replace an accepted snapshot.",
                },
                {
                    "step": 3,
                    "title": "Screen and purchase targeted evidence",
                    "action": "Run public-data exclusions, assign the primary play, and enrich only the survivors within budget.",
                    "detail": "Send identity, access, title, environmental, and buildability exceptions to the contractor responsible for that evidence.",
                },
                {
                    "step": 4,
                    "title": "Release a dated decision packet",
                    "action": "Assemble supported comparables, unresolved conditions, source dates, investigation costs, and the acquisition ceiling.",
                    "detail": "The principal records reject, investigate, or negotiate, then schedules transaction-stage refreshes for material facts.",
                },
            ],
        },
        {
            "heading": "4. Underwrite the tooling against gross sale proceeds and release capital deliberately",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Keep the canonical economics visible in every purchasing "
                    "decision. Conservative annual gross parcel sale proceeds are "
                    "$200,000, with a 12% net margin and $24,000 owner net profit. "
                    "Base proceeds are $850,000, with an 18.5% net margin and "
                    "$157,250 profit. Scaled proceeds are $1,500,000, with a 25% "
                    "net margin and $375,000 profit. The corresponding total "
                    "cost envelopes are $176,000, $692,750, and $1,125,000; these "
                    "include acquisition costs rather than treating land purchases "
                    "as someone else's transaction volume. The desk's revenue basis "
                    "is its gross parcel sale proceeds, not client deal volume, "
                    "borrowed principal, or an imagined recurring software fee. "
                    "The stated startup capital range is $15,000 to $75,000, "
                    "monthly operating expense range is $3,000 to $15,000, and "
                    "time to first deal is three to twelve months. These are "
                    "planning ranges, not instructions to combine every upper "
                    "bound with the Conservative case. Tool subscriptions, records "
                    "orders, professional investigations, carrying costs, and "
                    "disposition expenses must fit the selected case's total "
                    "cost envelope. A new subscription earns its place by "
                    "reducing purchased research, avoiding a demonstrated error, "
                    "or freeing constrained review time. More records alone "
                    "do not increase the modeled margin."
                ),
                (
                    "Use transaction-level cost codes to determine whether the "
                    "information stack actually helps. Separate recurring "
                    "subscriptions from per-record purchases, parcel-specific "
                    "investigations, title and closing charges, and broader "
                    "operating overhead. For an illustrative internal authorization, "
                    "a $600 monthly data-and-records allowance equals $7,200 "
                    "annually; it must be contained within the selected scenario's "
                    "existing cost envelope, not added while preserving its "
                    "profit unchanged. Track cost per desktop survivor, cost per "
                    "decision-ready packet, contractor hours per packet, and "
                    "elapsed days between identification and a defensible offer. "
                    "Do not optimize cost per lead when cheap leads repeatedly "
                    "fail access or ownership checks. Review rejected transactions "
                    "quarterly to identify which source or question produced "
                    "the decisive finding. Remove duplicated feeds when they "
                    "do not improve coverage, speed, or evidence quality. Keep "
                    "a renewal calendar tied to actual usage and export rights "
                    "so cancellation does not strand required transaction "
                    "records. Measure the concentration of cash in unsold "
                    "parcels separately from research throughput. Illiquidity "
                    "can defeat an otherwise efficient desk, particularly "
                    "when a subdivision or title cure extends the holding "
                    "period. Capital release therefore follows resolved "
                    "transaction questions, not the number of completed "
                    "automation tasks."
                ),
                (
                    "Before an acquisition becomes irreversible, require a dated "
                    "decision packet that another qualified reviewer can "
                    "reconstruct. It should identify the exact interest being "
                    "purchased, supported seller authority, current tax and "
                    "title requirements, access evidence, intended-use "
                    "constraints, comparable selection, and the remaining "
                    "cash exposure. Confirm the proposed disposition structure "
                    "with the appropriate professionals: selling owned land "
                    "differs from representing another owner, and Arizona's "
                    "licensing exemptions in A.R.S. 32-2121 have conditions "
                    "rather than creating a blanket exemption for every "
                    "property-related service. Recording requirements under "
                    "A.R.S. 33-411 also belong in the closing workflow, not "
                    "in an automated assumption that a signed document "
                    "has completed every necessary step. For land involving "
                    "possible discharges of dredged or fill material into "
                    "waters subject to federal jurisdiction, evaluate "
                    "33 U.S.C. 1344 with qualified project support before "
                    "pricing unrestricted development. Public accessibility "
                    "of a record does not authorize every downstream use; "
                    "retain license terms and avoid unnecessary collection "
                    "of personal information. When the deal closes, archive "
                    "the executed instruments, final settlement statement, "
                    "policy documents, and evidence supporting material "
                    "representations. Then reconcile actual proceeds and "
                    "all costs against underwriting, so the next buying "
                    "rule reflects completed transactions rather than "
                    "optimistic listing prices."
                ),
            ],
            "table": {
                "caption": "Scenario reconciliation and operating controls for the four-person land desk",
                "headers": [
                    "Control or economic case",
                    "Exact operating basis",
                    "Required evidence or arithmetic",
                    "Decision consequence for the principal",
                ],
                "rows": [
                    [
                        "Conservative case uses one full-time principal and three contractors",
                        "$200,000 annual gross parcel proceeds with a 12% net margin",
                        "$200,000 less $176,000 total costs equals $24,000 owner profit",
                        "Keep acquisition, research, carrying, and disposition costs inside that envelope",
                    ],
                    [
                        "Base case uses one full-time principal and three contractors",
                        "$850,000 annual gross parcel proceeds with an 18.5% net margin",
                        "$850,000 less $692,750 total costs equals $157,250 owner profit",
                        "Purchase incremental evidence only where the transaction spread supports it",
                    ],
                    [
                        "Scaled case uses two full-time staff and four contractors",
                        "$1,500,000 annual gross parcel proceeds with a 25% net margin",
                        "$1,500,000 less $1,125,000 total costs equals $375,000 owner profit",
                        "Scale qualified review capacity before increasing unresolved acquisition volume",
                    ],
                    [
                        "Illustrative data allowance remains an internal cost allocation only",
                        "$600 monthly authorization creates a $7,200 annual purchasing ceiling",
                        "Supplier invoices and parcel-linked usage substantiate recurring and variable spend",
                        "Offset new spending within existing costs or explicitly revise underwriting",
                    ],
                    [
                        "Parcel carrying exposure measures cash concentration rather than lead throughput",
                        "Track acquisition cash, elapsed holding days, taxes, and required improvements",
                        "Updated sale timetable and actual obligations show remaining cash exposure",
                        "Stop additional purchases when unsold inventory exhausts available working capital",
                    ],
                    [
                        "Closing reconciliation turns completed deals into defensible buying rules",
                        "Compare gross proceeds and every attributable cost with original underwriting",
                        "Settlement records, supplier invoices, and archived evidence explain each variance",
                        "Adjust filters and offer ceilings using realized results rather than listings",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before releasing acquisition funds",
                "body": "Each check requires dated evidence, a responsible reviewer, and a written disposition of remaining exceptions.",
                "items": [
                    "Identity and authority: reconcile county-qualified parcel identifiers, legal descriptions, current ownership, and the actual signer's power to convey.",
                    "Access and title: obtain the title provider's requirements, inspect relevant access instruments, and price any executable cure before relying on it.",
                    "Use and physical constraints: confirm jurisdiction, intended-use feasibility, utility scope, and necessary survey, civil, environmental, or wetland investigations.",
                    "Cash and exit: reconcile purchase price, all projected costs, holding exposure, supported comparables, and the remaining cash reserve against the selected scenario.",
                ],
            },
        },
    ],
    "pull_quote": "Buy the parcel only after the evidence explains the discount, the access, and the exit.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Choose one county and register official parcel, recorder, tax, planning, court, and roadway sources with access terms and fallback contacts.",
        "Assign every candidate one of the six mapped plays and specify the evidence that can reject or advance that play.",
        "Build a SQLite evidence store with preserved identifiers, source timestamps, document references, payload digests, and split-or-merge history.",
        "Run public-data screening before purchasing commercial enrichment, and record request costs and contractor time against each surviving parcel.",
        "Test the pipeline against splits, bundled sales, coordinate errors, missing hazard coverage, and disputed-access examples before increasing batch size.",
        "Release acquisition funds only after completing the four pre-flight checks and reconciling all projected costs with the selected canonical scenario.",
    ],
    "statutory_citations": [
        {
            "title": "40 CFR 312.20 — All appropriate inquiries",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312/subpart-C/section-312.20",
            "relevance": (
                "Defines inquiry requirements and acquisition timing for applicable "
                "CERCLA liability protections; desktop environmental searches alone "
                "do not perform the required professional inquiry."
            ),
        },
        {
            "title": "33 U.S.C. 1344 — Permits for dredged or fill material",
            "url": "https://www.law.cornell.edu/uscode/text/33/1344",
            "relevance": (
                "Creates the federal permitting framework relevant to covered "
                "discharges of dredged or fill material; inventory mapping does "
                "not independently decide parcel-specific jurisdiction."
            ),
        },
        {
            "title": "A.R.S. 32-2101 — Real estate and subdivision definitions",
            "url": "https://www.azleg.gov/ars/32/02101.htm",
            "relevance": (
                "Supplies Arizona definitions that must be checked alongside local "
                "land-division requirements before underwriting a minor subdivision."
            ),
        },
        {
            "title": "A.R.S. 32-2121 — Exceptions to real estate licensing requirements",
            "url": "https://www.azleg.gov/ars/32/02121.htm",
            "relevance": (
                "Identifies conditional licensing exceptions; distinguish selling "
                "owned property from activities performed for other owners."
            ),
        },
        {
            "title": "A.R.S. 33-411 — Recording instruments affecting real property",
            "url": "https://www.azleg.gov/ars/33/00411.htm",
            "relevance": (
                "Addresses recording and acknowledgment requirements affecting "
                "real-property instruments; integrate the applicable requirements "
                "into the title and closing workflow."
            ),
        },
    ],
}
