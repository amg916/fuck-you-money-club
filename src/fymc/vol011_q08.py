from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small high-ticket brokerage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "Secretary of State, UCC, EDGAR, SAM.gov, Asset Registries, Escrow Evidence & Section 179D Allocation Records",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #26, High-Ticket Brokerage, ranks #11 with an 82/100 Money-to-Manpower "
        "Score across 21 mapped plays. Its information edge comes from resolving ownership, "
        "authority, encumbrances, buyer capacity, and closing dependencies before competing "
        "desks do. This chapter connects official registries, commercial enrichment, "
        "reproducible evidence, and milestone tooling without treating scraped contacts as "
        "qualified buyers. Canonical annual owner profit is $25,000 Conservative, $206,250 "
        "Base, and $500,000 Scaled; revenue means retained transaction commissions, never "
        "underlying asset consideration. Use a provenance-first waterfall, explicit licensing "
        "checks, and independent escrow verification. The mapped social-account and Section "
        "179D plays receive separate transferability and eligibility tests, preventing a "
        "seductive lead list from becoming an uncloseable mandate."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "25% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$550,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "37.5% net margin; $206,250 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "50% net margin; $500,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Resolve the seller, asset, and authority before buying another lead",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start every exclusive mandate with an identity spine, not a contact spreadsheet. "
                    "Assign a deal identifier, record the seller's exact legal name and formation "
                    "jurisdiction, then attach the state entity number, asset identifier, signing "
                    "authority, and expected closing venue. Separate registered agent, officer, "
                    "beneficial owner, and authorized seller; a registry hit establishes neither "
                    "ownership of the offered asset nor permission to sell it. Obtain the engagement "
                    "letter, organizational documents, and seller authorization directly, then compare "
                    "them with official records. For equipment, preserve serial numbers and invoice "
                    "chains; for aircraft, use the registration and airframe identifiers; for property, "
                    "use parcel and recorded instrument references. For business sales, distinguish "
                    "an asset purchase from a securities transaction before selecting the broker's "
                    "operating structure. Exchange Act registration and the conditional M&A broker "
                    "exemption in 15 U.S.C. 78o(b)(13) require a transaction-specific assessment; "
                    "the exemption does not erase state requirements or permit custody of client "
                    "funds. Place every conflict into an exception queue with a named resolver. "
                    "The first deliverable is a defensible identity packet that an escrow officer, "
                    "buyer, and transaction adviser can independently follow without relying on "
                    "the salesperson's memory."
                ),
                (
                    "Treat each registry as an instrument with a narrow measurement range. A Secretary "
                    "of State record supports entity existence and filing status, while a UCC search "
                    "supports a particular debtor-name and jurisdiction inquiry. Neither substitutes "
                    "for a lien release, title opinion, or ownership representation. Apply the adopted "
                    "state versions of UCC Sections 9-301, 9-307, 9-503, and 9-506 when deciding "
                    "where and under which name to search; include former names and merger history "
                    "when the facts require them. County recorder indexes can lag document submission, "
                    "and asset registries can lag a recent transfer. Request certified searches or "
                    "specialist title work when closing exposure justifies the expense. PACER supplies "
                    "federal court records, not a complete national judgment or litigation search; "
                    "add the relevant state courts and bankruptcy review. OFAC screening likewise "
                    "requires identity resolution, not a binary decision from a similar surname. "
                    "Record search parameters, retrieval time, source update date when exposed, and "
                    "coverage limits. Recheck material facts before accepting a mandate and again "
                    "before releasing closing instructions. If the record conflicts with the seller's "
                    "story, stop distributing that assertion rather than silently overwriting the "
                    "evidence with a more convenient commercial database entry."
                ),
                (
                    "Use the directory below as a research routing map, not a promise that every "
                    "source has a supported API or immediate publication. Its refresh entries "
                    "distinguish source publication from the desk's polling policy. Assign one "
                    "owner to maintain endpoint documentation, permitted use, account requirements, "
                    "and current prices quarterly. Public access does not imply permission for "
                    "unlimited extraction, commercial redistribution, or unrestricted personal-data "
                    "use. Where only a browser portal exists, use authorized manual retrieval or "
                    "an approved records provider rather than defeating access controls. Download "
                    "a reusable official bulk file once when offered, retain its publication date, "
                    "and update only the changed records. Conditional requests and shared caching "
                    "reduce load and prevent several contractors from paying for the same document. "
                    "For an illustrative 40-mandate research queue, a $15 initial records allowance "
                    "per mandate creates a $600 procurement envelope, not a claim about registry "
                    "pricing. Escalate certified searches against specific closing exposure instead "
                    "of purchasing them indiscriminately. When a source is unavailable, label the "
                    "fact as awaiting evidence, identify the alternate official source, and assign "
                    "a deadline. A stale record may support historical analysis; it must not masquerade "
                    "as current clearance for a high-value transfer."
                ),
            ],
            "table": {
                "caption": "Sixteen-source official directory: access, cost class, freshness, and evidence fallbacks",
                "headers": [
                    "Named source and precise research purpose",
                    "Exact access method and cost class",
                    "Publication latency and request hygiene",
                    "Coverage limitation and concrete fallback",
                ],
                "rows": [
                    [
                        "State Secretary of State business entity search establishes the legal identity spine",
                        "Use the formation state's official entity-search portal; basic searches are often free, while certified documents carry state fees",
                        "Filing acceptance and online publication differ by state; retrieve at intake and preclosing, respecting portal session restrictions",
                        "Officer lists do not establish signing authority; obtain resolutions and certified organizational records directly from the seller",
                    ],
                    [
                        "State UCC filing office search identifies indexed security-interest filings against debtors",
                        "Use the relevant state's official UCC portal; pay published search, copy, and certification fees as applicable",
                        "Indexing delay varies by filing office; retain search logic and timestamp, then order an appropriate closing update",
                        "An index result is not lien clearance; obtain certified searches, payoff letters, and authenticated release arrangements",
                    ],
                    [
                        "County recorder and assessor portals connect parcels with recorded instruments",
                        "Search the property's official county recorder and assessor websites; viewing and document-copy charges vary locally",
                        "Assessor cycles and recorder indexing have different delays; cache retrieved instruments and verify recording status before closing",
                        "Assessor ownership is not conclusive title evidence; use a title company and certified recorded instruments",
                    ],
                    [
                        "PACER Case Locator and court dockets expose federal litigation events",
                        "Access pacer.uscourts.gov with a registered account; standard electronic access generally costs $0.10 per page, subject to exceptions",
                        "Court and locator update timing differ; narrow searches, monitor charges, and avoid repeatedly downloading identical docket documents",
                        "Federal coverage excludes many state disputes; search relevant state courts and obtain court-certified documents when necessary",
                    ],
                    [
                        "SEC EDGAR submissions and company facts reveal issuer filings",
                        "Use sec.gov/edgar/search, data.sec.gov/submissions, and data.sec.gov/api/xbrl/companyfacts; public access is free",
                        "Publication follows SEC processing; identify the requester, cache responses, and keep aggregate traffic below the published ten-request-per-second ceiling",
                        "Private sellers may have no filings; obtain seller-authorized records and corroborate public-company evidence against original submissions",
                    ],
                    [
                        "SAM.gov entity registration and exclusions support government-counterparty checks",
                        "Use sam.gov public search and documented APIs linked through open.gsa.gov; API access requires the applicable free key",
                        "Registration and exclusion updates depend on source processing; follow endpoint quotas, cache responses, and honor retry instructions",
                        "Registration does not prove procurement authority; confirm the contracting officer and inspect signed award or delegation documents",
                    ],
                    [
                        "USAspending award records reveal federal customer concentration and obligations",
                        "Use usaspending.gov and documented endpoints at api.usaspending.gov; public search and API access are free",
                        "Agency reporting and corrections create variable delay; batch bounded queries and back off when service capacity is constrained",
                        "Obligations are not seller collections or profit; reconcile awards with contracts, invoices, and authorized cash-receipt evidence",
                    ],
                    [
                        "OFAC sanctions lists and search support restricted-party identity review",
                        "Use ofac.treasury.gov sanctions search and official Sanctions List Service downloads; official access is free",
                        "Lists update when Treasury publishes changes; ingest published versions, retain timestamps, and rescreen material parties before closing",
                        "Name similarity alone does not resolve identity; compare identifiers, investigate ownership, and escalate unresolved matches before proceeding",
                    ],
                    [
                        "FAA aircraft registry connects registration identifiers with recorded aircraft information",
                        "Use registry.faa.gov aircraft inquiry and official releasable database downloads; public inquiry is free, with separate document charges",
                        "Public releases and processing queues can lag transactions; follow posted release dates and prefer bulk data over repeated queries",
                        "Registry inquiry is not a complete title examination; obtain FAA records and a qualified aircraft title specialist",
                    ],
                    [
                        "USCG National Vessel Documentation Center supports documented-vessel ownership research",
                        "Use official NVDC services linked from dco.uscg.mil; request an Abstract of Title under the published fee schedule",
                        "Document processing and service availability vary; track request receipts and refresh material evidence against the planned closing date",
                        "Federal documentation does not cover every vessel; add state titling, mortgage review, and specialist maritime closing support",
                    ],
                    [
                        "FMCSA SAFER Company Snapshot corroborates motor-carrier identity and operating profile",
                        "Use safer.fmcsa.dot.gov Company Snapshot by USDOT number or legal name; public snapshot access is free",
                        "Individual fields follow different update cycles; inspect displayed dates and avoid treating every field as live operating status",
                        "A carrier record does not prove equipment ownership; add Licensing and Insurance checks plus vehicle-title evidence",
                    ],
                    [
                        "EPA ECHO facility records reveal environmental enforcement and permit context",
                        "Use echo.epa.gov facility search and documented ECHO web services; public searches and supported services are free",
                        "Underlying program databases publish on differing schedules; retain field dates and use bounded, cached facility queries",
                        "Database absence does not establish clean conditions; obtain state permit records and appropriate independent environmental assessment",
                    ],
                    [
                        "ENERGY STAR Portfolio Manager supports owner-authorized building performance evidence",
                        "Use portfoliomanager.energystar.gov and authorized Portfolio Manager web services; the government platform is free",
                        "Meter information follows account uploads and provider exchanges; poll only authorized properties and respect service documentation",
                        "Benchmarking does not establish Section 179D eligibility; obtain plans, qualifying calculations, and independent certification evidence",
                    ],
                    [
                        "IRS Tax Exempt Organization Search corroborates listed nonprofit status",
                        "Use apps.irs.gov/app/eos and official IRS downloadable datasets; public searches and supported downloads are free",
                        "Publication timing differs across determination, revocation, and return datasets; preserve dataset dates and reuse official bulk files",
                        "Listing alone does not establish allocation eligibility; obtain governing documents and transaction-specific tax eligibility analysis",
                    ],
                    [
                        "USPTO Assignment Center reveals recorded patent and trademark assignment chains",
                        "Use assignmentcenter.uspto.gov official search and record services; public searching is free, with applicable filing or copy fees",
                        "Recordation follows submission and processing; preserve execution and recordation dates separately and recheck relevant assets before closing",
                        "Recordation does not validate every conveyance; obtain executed assignments and reconcile schedules with specialist intellectual-property review",
                    ],
                    [
                        "ICANN registration-data lookup corroborates domain registrar and registration events",
                        "Use lookup.icann.org and the registrar or registry's published RDAP service; basic public lookup is generally free",
                        "RDAP reflects published registration data, with privacy redactions; honor provider limits, cache responses, and avoid bulk personal-data harvesting",
                        "Redacted registration does not defeat ownership verification; use authorized DNS challenges and registrar-supported transfer confirmation",
                    ],
                ],
            },
        },
        {
            "heading": "2. Buy enrichment only after the mandate survives primary-source checks",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the enrichment waterfall around an identified company and a documented "
                    "purpose. Begin with the entity spine and company website, then add commercial "
                    "company identifiers, relevant executives, and permitted business contact channels. "
                    "OpenCorporates can improve cross-jurisdiction discovery, D&B Direct+ can supply "
                    "licensed business identifiers and attributes, and Crunchbase can suggest ownership "
                    "or funding events. None should silently replace a primary document. For each "
                    "attribute, store the provider, retrieval date, matching inputs, confidence, and "
                    "redistribution permission. A matching name is weaker than agreement across "
                    "jurisdiction, address, domain, and registration number. Distinguish a buyer's "
                    "announced fund size from available acquisition capital, and distinguish a "
                    "portfolio company's employee count from the parent organization's purchasing "
                    "authority. Contact enrichment follows qualification rather than preceding it. "
                    "People Data Labs and Hunter can support permitted discovery and verification "
                    "under their current terms, but a deliverable address does not establish "
                    "permission, relevance, or buyer interest. Route ambiguous records to a human "
                    "researcher instead of spraying outreach across possible identities. Maintain "
                    "suppression records and apply channel-specific rules, including CAN-SPAM for "
                    "commercial email and applicable restrictions on automated calls or texts. "
                    "The desired output is a small, explainable buyer shortlist, not a maximal "
                    "collection of personal records."
                ),
                (
                    "Price the waterfall by accepted evidence, not nominal API credits. Consider "
                    "an illustrative batch of 200 company candidates: official checks eliminate "
                    "80, commercial company matching resolves 90 of the remaining 120, and human "
                    "review accepts 60 for outreach research. At assumed internal budgeting rates "
                    "of $0.20 for each of 120 company lookups and $0.10 for each of 60 contact "
                    "verifications, variable API spend is $30. These are planning assumptions, "
                    "not vendor quotations, and exclude subscriptions, minimum commitments, "
                    "registry fees, and researcher time. If 12 recipients become qualified buyer "
                    "conversations, that narrow variable cost is $2.50 per conversation; the "
                    "fully loaded acquisition cost remains higher. Log every lookup against a "
                    "deal or research campaign so an unused annual subscription cannot disappear "
                    "inside overhead. Purchase a second provider only when its incremental matches "
                    "justify the incremental expense and permitted usage. When two sources "
                    "disagree, preserve both claims and seek stronger evidence rather than "
                    "averaging identities. Cache only for the contractually allowed period, "
                    "respect deletion obligations, and remove unnecessary personal attributes. "
                    "The cheapest reliable fallback is often a targeted call through the "
                    "company's published switchboard, not a third bulk-data contract."
                ),
                (
                    "The mapped play aged_high_karma_social_account_brokerage needs an explicit "
                    "asset-rights test before anyone prices audience access. Account age, karma, "
                    "followers, and verification badges are observations, not transferable property "
                    "rights or proof of authentic influence. Reddit, LinkedIn, X, and TikTok impose "
                    "different account, identity, advertising, and transfer restrictions; inspect "
                    "the current rules for the exact proposed transaction. This desk excludes "
                    "fabricated personas, manufactured reputation, proxy-based filter evasion, and "
                    "covert coordinated promotion. It does not operationalize account fleets or "
                    "promise search placement or model citations. Instead, evaluate permitted "
                    "creator-business acquisitions, licensed content, disclosed sponsorships, or "
                    "platform-supported transfers with written authority. An illustrative $80,000 "
                    "permitted business acquisition at a 10% retained commission produces $8,000 "
                    "broker revenue, not $80,000. If expected diligence costs are $2,000, the "
                    "remaining $6,000 is transaction contribution before shared overhead and "
                    "other costs, not the chapter's annual owner profit. Require seller-authorized "
                    "analytics, audience-quality sampling, content-rights schedules, and an escrow "
                    "condition covering the supported transfer method. If platform permission "
                    "or identity continuity cannot be established, exclude the account from "
                    "the sale and value independently transferable assets instead. If those "
                    "assets cannot support the economics, decline the mandate rather than "
                    "substituting a concealment technique."
                ),
            ],
            "table": {
                "caption": "Commercial enrichment waterfall with procurement tiers, refresh controls, and fallbacks",
                "headers": [
                    "Named service and narrow buying purpose",
                    "Access method and procurement cost tier",
                    "Freshness and rate-limit operating discipline",
                    "Acceptance test and alternate evidence route",
                ],
                "rows": [
                    [
                        "OpenCorporates supports entity discovery across multiple formation jurisdictions",
                        "Use opencorporates.com and documented api.opencorporates.com access; commercial API use requires the applicable licensed plan",
                        "Registry-derived coverage and freshness vary by jurisdiction; inspect source dates and enforce the plan's request allowance",
                        "Accept only resolved entity matches with source references; return to the official registry for decisive evidence",
                    ],
                    [
                        "D&B Direct+ supports licensed business identifiers and company attributes",
                        "Use developer.dnb.com documentation and contracted Direct+ credentials; pricing is a negotiated commercial subscription or usage arrangement",
                        "Attribute refresh differs by product and source; follow contractual quotas and preserve delivery timestamps for each response",
                        "Treat DUNS-linked records as matching assistance; obtain current seller records when ownership or authority is material",
                    ],
                    [
                        "Crunchbase supports discovery of funding events and potential strategic buyers",
                        "Use crunchbase.com licensed products and documented API offerings; API access is paid under the applicable commercial package",
                        "Event reporting and corrections can lag announcements; honor licensed quotas and verify material events through original announcements",
                        "Funding totals do not establish deployable acquisition capital; obtain buyer criteria and authorized proof of capacity",
                    ],
                    [
                        "People Data Labs supports permitted company and professional-profile enrichment",
                        "Use documented endpoints at docs.peopledatalabs.com with account credentials; trial allowances and paid credit plans depend on current terms",
                        "Dataset refresh is not real-time employment verification; cap credit consumption and review match confidence before retaining records",
                        "Do not merge ambiguous personal identities automatically; use the employer's published directory or authorized introduction instead",
                    ],
                    [
                        "Hunter supports domain-based business contact discovery and address checks",
                        "Use hunter.io and documented api.hunter.io/v2 endpoints; free allowances and paid credit tiers follow the current pricing schedule",
                        "Verification is a point-in-time signal rather than permanent deliverability; obey endpoint limits and suppress rejected addresses",
                        "A valid mailbox does not establish outreach suitability; use published business channels when identity remains unresolved",
                    ],
                    [
                        "Google Places API supports corroborating public operating locations",
                        "Use developers.google.com/maps/documentation/places and a restricted project key; billing is metered by selected service and fields",
                        "Place records can lag closures and relocations; set project quotas and follow current caching and attribution rules",
                        "A place listing does not establish entity ownership; compare official records and confirm directly with the business",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four evidence advantages that survive buyer diligence",
                "body": "Spend research money where a stronger record changes mandate acceptance, buyer matching, or closing probability.",
                "items": [
                    "Order former-name and merger-history searches before assuming a clean current-name UCC result covers the seller's entire borrowing history.",
                    "Ask the buyer for acquisition size, funding source, geography, and exclusion criteria before paying to enrich additional executives at that organization.",
                    "Keep the NCNDA introduction ledger separate from the public lead list, recording acknowledged introductions and contract-specific exclusions without claiming universal enforceability.",
                    "For audience businesses, compare seller-authorized analytics with revenue concentration and transfer permissions; a platform badge is never the closing deliverable.",
                ],
            },
        },
        {
            "heading": "3. Build an auditable evidence pipeline instead of a fragile scraping stack",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A small desk can operate a durable pipeline with Python's urllib.request, "
                    "json, csv, sqlite3, hashlib, and logging modules, plus an authorized CRM "
                    "or spreadsheet for workflow visibility. Keep raw evidence separate from "
                    "normalized assertions. A source record should contain a source identifier, "
                    "request parameters with secrets removed, retrieval timestamp in UTC, "
                    "response status, publication date when available, content hash, and "
                    "permitted retention period. An assertion should link an entity or asset "
                    "to a field, value, effective date, evidence reference, and reviewer. "
                    "A SHA-256 hash helps detect later file changes; it does not prove that "
                    "the original statement was true. Use stable keys and unique constraints "
                    "to prevent repeated imports from creating duplicate buyers or duplicated "
                    "milestone tasks. Do not place API keys, full bank details, or unnecessary "
                    "identity documents in logs. Protect stored evidence with account-level "
                    "access controls and encrypted storage, and keep client-specific workspaces "
                    "separate. Test backup restoration, not merely backup creation. For "
                    "an illustrative 300 evidence packets averaging 2 MB, raw storage is "
                    "about 600 MB before versions and backups; document quality, permission "
                    "management, and reviewer time dominate the economics, not disk capacity."
                ),
                (
                    "Design connectors to fail visibly and narrowly. Set connection and read "
                    "timeouts, bound response sizes, validate content types, and reject schema "
                    "changes that would silently move an address into an ownership field. "
                    "Use per-provider concurrency limits and exponential backoff with jitter; "
                    "honor Retry-After and never rotate identities to defeat quotas. Quarantine "
                    "authentication failures until the account owner resolves them. A daily "
                    "scheduled run is a desk policy, not evidence that the underlying registry "
                    "updates daily. Preserve the last successful retrieval and display its "
                    "age beside every material assertion. Build contract tests from permitted "
                    "fixtures covering empty results, multiple matches, revoked credentials, "
                    "expired pagination tokens, and truncated downloads. Use sqlite3 "
                    "transactions so a failed import does not leave half a buyer cohort "
                    "marked as verified. Track fetched records, accepted matches, exceptions, "
                    "cost units, and human review minutes as separate counters. If a "
                    "provider disappears, route affected cases to the documented manual "
                    "procedure rather than allowing automated buyer matching to continue "
                    "on stale attributes. Reconciliation should expose disagreements between "
                    "sources, not smooth them away into a deceptively confident score. "
                    "A useful automation result is an accurate exception list with owners "
                    "and deadlines, even when no record qualifies for unattended acceptance."
                ),
                (
                    "Connect evidence to a closing state machine: mandate signed, identity "
                    "resolved, buyer qualified, diligence opened, definitive documents executed, "
                    "funding confirmed, escrow conditions satisfied, and commission settled. "
                    "Each transition needs a responsible person and a supporting artifact. "
                    "Buyer-seller matching ranks fit against documented criteria; it does "
                    "not invent capacity. Document checklists must distinguish received, "
                    "reviewed, accepted, expired, and superseded materials. For an NCNDA, "
                    "record the covered parties, introduced opportunity, effective period, "
                    "exceptions, and acknowledged delivery; a generic template cannot "
                    "establish every commission claim. Keep underlying purchase money outside "
                    "the desk's ordinary operating account, using properly authorized escrow "
                    "and asset-specific handling arrangements. Verify escrow instructions "
                    "through independently obtained contact details and a second communication "
                    "channel; an email thread alone cannot authenticate changed bank details. "
                    "Diagnostic tools test systems, not counterparties' honesty: a valid TLS "
                    "certificate proves neither escrow authority nor account ownership. "
                    "Before closing, rerun the material entity, sanctions, lien, and authority "
                    "checks under the transaction team's required timetable. After settlement, "
                    "reconcile the escrow statement, commission entitlement, co-broker "
                    "allocations, and bank receipt. Preserve the evidence needed to explain "
                    "the retained amount while deleting personal information that no longer "
                    "has a justified retention purpose."
                ),
            ],
            "table": {
                "caption": "Six diagnostic controls for authorized endpoints, evidence stores, and closing records",
                "headers": [
                    "Named tool and bounded diagnostic task",
                    "Access method and direct cost treatment",
                    "Execution cadence and failure signal",
                    "Specific recovery and evidentiary limitation",
                ],
                "rows": [
                    [
                        "curl inspects documented HTTP status, headers, and response types",
                        "Use curl against authorized API endpoints with redacted credentials; the utility adds no per-request software charge",
                        "Run during connector setup and incident diagnosis; inspect rate-limit responses, redirects, content type, and Retry-After headers",
                        "Stop on access rejection and inspect provider documentation; a successful response does not validate the returned business claim",
                    ],
                    [
                        "dig checks brokerage-controlled DNS records and domain-verification challenges",
                        "Use an installed dig client against public DNS or explicitly authorized zones; standard queries carry no tool subscription",
                        "Run when onboarding domains or investigating routing failures; compare answers with TTLs and expected authoritative nameservers",
                        "Resolve mismatched records with the authorized domain administrator; DNS control alone does not prove asset-sale authority",
                    ],
                    [
                        "OpenSSL s_client inspects TLS handshakes on authorized service endpoints",
                        "Use openssl s_client with the documented hostname and port; local execution requires no commercial verification subscription",
                        "Run when certificate or handshake errors appear; inspect hostname coverage, expiry, trust chain, and negotiated protocol",
                        "Repair endpoint configuration or contact the provider; certificate validity does not authenticate an escrow beneficiary's bank account",
                    ],
                    [
                        "Python json and csv validate provider payloads before normalization",
                        "Use standard-library parsers with explicit required-field checks; execution costs belong to the desk's ordinary compute budget",
                        "Validate every import and quarantine changed structures; detect missing identifiers, malformed dates, and unexpected column movement",
                        "Preserve the rejected raw response under permitted retention; repair mapping tests before restarting affected transaction workflows",
                    ],
                    [
                        "Python sqlite3 and hashlib preserve linkage and detect evidence changes",
                        "Use local database transactions and SHA-256 content hashes; protect database files through separately configured encrypted storage",
                        "Enforce unique keys on each import and test restoration regularly; alert on orphan evidence references or hash differences",
                        "Restore from a tested backup and compare source records; neither a hash nor database integrity proves factual accuracy",
                    ],
                    [
                        "CRM audit logs and escrow statements reconcile transaction milestones",
                        "Use authorized CRM exports and directly obtained settlement records; subscriptions and escrow charges follow existing contracted arrangements",
                        "Review milestone exceptions weekly and reconcile each settlement promptly; investigate changed beneficiaries, missing documents, and commission differences",
                        "Call the verified escrow contact through an independent channel; restrict settlement changes until discrepancies are resolved",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the identity and authority packet",
                    "action": "Capture legal names, jurisdictions, asset identifiers, seller authority, and signed mandate scope.",
                    "detail": "Assign one deal identifier and record which official sources can corroborate each material assertion before purchasing enrichment.",
                },
                {
                    "step": 2,
                    "title": "Retrieve and normalize permitted evidence",
                    "action": "Fetch authorized official records, then enrich only unresolved attributes that affect qualification.",
                    "detail": "Store retrieval dates, source dates, match inputs, usage rights, and evidence references; quarantine conflicts for named human review.",
                },
                {
                    "step": 3,
                    "title": "Advance milestones through documented review",
                    "action": "Match buyers against recorded criteria and connect every diligence milestone to an accepted artifact.",
                    "detail": "Keep licensing, transferability, sanctions, lien, and escrow exceptions visible; do not let a CRM status substitute for evidence.",
                },
                {
                    "step": 4,
                    "title": "Recheck and reconcile the closing",
                    "action": "Refresh material records, authenticate escrow instructions independently, and reconcile retained commission after settlement.",
                    "detail": "Archive the supporting settlement packet under the retention schedule and record failed-closing causes for the next pipeline review.",
                },
            ],
        },
        {
            "heading": "4. Screen allocation opportunities and reconcile tooling to retained commissions",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play section_179d_municipal_deduction_allocation_arbitrage concerns "
                    "documented allocations to eligible designers, not a marketplace for freely "
                    "transferable deductions. Under 26 U.S.C. 179D, first identify the qualifying "
                    "building owner, eligible property, designer contribution, and applicable "
                    "construction and placed-in-service dates. The statute terminates eligibility "
                    "for property whose construction begins after June 30, 2026; document the "
                    "applicable construction-start analysis rather than assuming every public "
                    "retrofit remains eligible. Government ownership and specified tax-exempt "
                    "ownership require their own eligibility analysis. IRS organization records, "
                    "public procurement awards, building permits, and owner-authorized Portfolio "
                    "Manager data help identify candidates, but none establishes a deduction "
                    "amount. Obtain the design contract, scope of services, allocation "
                    "authorization, qualifying technical calculations, and certification required "
                    "under applicable rules. Determine whether prevailing-wage and apprenticeship "
                    "requirements affect the available amount, and retain the substantiation "
                    "supporting that determination. Municipal staff may possess useful records "
                    "without possessing authority to sign the allocation. Confirm the owner's "
                    "delegation and procurement requirements before proposing compensation. Where "
                    "a federal contract is implicated, examine the actual solicitation and "
                    "contract clauses, including applicable contingent-fee restrictions, rather "
                    "than treating public-sector access as permission to charge a success fee. "
                    "Every eligibility conclusion belongs to a documented project review."
                ),
                (
                    "Use unit math to prevent deduction amounts from leaking into brokerage "
                    "revenue. An illustrative 100,000-square-foot building multiplied by an "
                    "independently substantiated hypothetical $2.00-per-square-foot applicable "
                    "amount produces a $200,000 deduction before other applicable limitations. "
                    "That assumed rate is not a published rate for a particular tax year, "
                    "and the deduction is neither a $200,000 cash payment nor operator "
                    "revenue. Actual tax benefit depends on the recipient's tax position "
                    "and applicable limitations. A separately contracted $6,000 fixed "
                    "documentation fee would compensate defined services, subject to "
                    "eligibility, procurement, and professional-scope requirements. It is "
                    "outside this volume's retained-transaction-commission scorecard and "
                    "must not be inserted into the canonical cases. If a proposed "
                    "contingent arrangement is impermissible or the allocation is doubtful, "
                    "pause the allocation, obtain independent tax review, and offer fixed-fee "
                    "documentation support only for eligible projects. Do not cure an "
                    "ineligible project by renaming the fee. Record who prepares the "
                    "calculation, who independently certifies the technical work, who "
                    "authorizes allocation, and who claims the deduction. If those "
                    "responsibilities collapse into one unsupported broker assertion, "
                    "the opportunity has failed diligence regardless of the potential "
                    "headline deduction or enthusiasm of the lead source."
                ),
                (
                    "Keep the canonical operating model fixed while using local assumptions "
                    "to test throughput. Conservative retained commissions are $100,000, "
                    "with $75,000 total costs and $25,000 owner profit at 25%, supported "
                    "by 1 FT + 3 C. Base retained commissions are $550,000, with "
                    "$343,750 total costs and $206,250 owner profit at 37.5%, also "
                    "with 1 FT + 3 C. Scaled retained commissions are $1,000,000, "
                    "with $500,000 total costs and $500,000 owner profit at 50%, "
                    "supported by 2 FT + 4 C. Illustrative mixes of four $25,000 "
                    "retained commissions, eleven $50,000 commissions, and twenty "
                    "$50,000 commissions reproduce those revenue totals without "
                    "counting asset consideration. A Base desk that provisionally "
                    "budgets $12,000 annually for data and tooling has allocated "
                    "part of its $343,750 cost envelope, not created an additional "
                    "profit deduction outside the model. Track failed-closing expense "
                    "and commission collection timing separately from lead volume. "
                    "Startup capital of $15,000–$100,000, monthly operating expenditure "
                    "of $3,000–$18,000, and a 3–12 month first-deal horizon require "
                    "cash planning; the monthly range does not describe every annual "
                    "variable cost. Approve subscriptions against verified research "
                    "capacity and expected closing contribution, then cancel tools "
                    "that merely make an unqualified pipeline look larger."
                ),
            ],
            "table": {
                "caption": "Canonical commission reconciliation and mapped-play failure controls",
                "headers": [
                    "Scenario or mapped operating decision",
                    "Concrete unit math and retained-revenue treatment",
                    "Expense, team, or evidence requirement",
                    "Failure fallback and management action",
                ],
                "rows": [
                    [
                        "Conservative canonical case for the specialist brokerage desk",
                        "Four illustrative retained commissions of $25,000 equal $100,000 annual revenue; underlying asset consideration stays excluded",
                        "Total annual costs equal $75,000; 25% margin yields $25,000 owner profit with 1 FT + 3 C",
                        "If closings slip, revise cash timing and discretionary spend; do not recognize unearned commissions to preserve targets",
                    ],
                    [
                        "Base canonical case for the same small operating team",
                        "Eleven illustrative retained commissions of $50,000 equal $550,000 annual revenue; co-broker pass-through amounts stay outside retained fees",
                        "Total annual costs equal $343,750; 37.5% margin yields $206,250 owner profit with 1 FT + 3 C",
                        "Allocate the illustrative $12,000 tooling budget inside total costs; remove subscriptions that fail incremental contribution tests",
                    ],
                    [
                        "Scaled canonical case with six total team members",
                        "Twenty illustrative retained commissions of $50,000 equal $1,000,000 annual revenue; purchase principal remains separate throughout reconciliation",
                        "Total annual costs equal $500,000; 50% margin yields $500,000 owner profit with 2 FT + 4 C",
                        "Add reviewer capacity before increasing automated deal intake; pause matching when unresolved authority or transfer exceptions accumulate",
                    ],
                    [
                        "aged_high_karma_social_account_brokerage requires permitted asset rights before valuation",
                        "A permitted $80,000 business transaction at 10% retained commission yields $8,000 revenue; account reputation itself proves no transfer right",
                        "Illustrative $2,000 diligence cost leaves $6,000 contribution before overhead; require authorized analytics and supported transfer documentation",
                        "Exclude prohibited account transfers and covert manipulation; value transferable content or business assets, otherwise decline the mandate",
                    ],
                    [
                        "section_179d_municipal_deduction_allocation_arbitrage requires project eligibility and authorized allocation",
                        "Illustrative 100,000 square feet times hypothetical $2.00 equals $200,000 deduction before applicable limitations, never brokerage revenue",
                        "A separately permitted $6,000 documentation fee belongs outside this commission scorecard; obtain independent technical and tax substantiation",
                        "Pause doubtful allocations and obtain independent tax review; offer fixed-fee documentation support only for eligible projects",
                    ],
                    [
                        "Failed-closing reserve and collection timing protect operating continuity",
                        "Three abandoned mandates costing an illustrative $2,000 each consume $6,000 cash without producing any retained commission revenue",
                        "Track that expense within the applicable annual cost envelope; monitor outstanding invoices separately from collected settlement receipts",
                        "Reduce speculative diligence purchases and stage contracted work; never use client purchase funds to bridge operating cash shortages",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before marketing a mandate",
                "body": "A mandate enters active distribution only when the responsible reviewer can point to the supporting evidence for each check.",
                "items": [
                    "Verify asset-specific licensing, agency disclosures, seller authority, and any claimed securities-broker exemption against the actual transaction structure and jurisdictions.",
                    "Resolve ownership, material encumbrances, sanctions identity matches, and asset-transfer restrictions; assign documented resolution dates to every remaining exception.",
                    "Confirm permitted source access, commercial data usage rights, outreach restrictions, and platform-supported transfer mechanics before enrichment or buyer distribution.",
                    "Authenticate escrow arrangements independently; for Section 179D projects, confirm construction timing, eligible owner and designer roles, certification, and allocation authority.",
                ],
            },
        },
    ],
    "pull_quote": "The best brokerage database is the one that can prove why a deal is sellable, transferable, and payable.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create one identity packet per mandate linking entity numbers, asset identifiers, signing authority, engagement terms, and official supporting records.",
        "Register the sixteen directory sources with access owners, current cost schedules, publication timestamps, permitted uses, and documented manual fallbacks.",
        "Run a small enrichment batch and measure accepted entity matches, qualified buyer conversations, researcher minutes, and fully loaded acquisition costs.",
        "Implement evidence hashes, source-linked assertions, bounded retries, exception queues, and a tested restoration procedure before automating buyer matching.",
        "Apply separate transferability screening to the social-account play and project-specific eligibility screening to Section 179D allocation opportunities.",
        "Reconcile every settled commission against escrow evidence and the canonical annual revenue, total-cost, margin, profit, and staffing cases.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 78o(b)(13) — Conditional exemption for certain M&A brokers",
            "url": "https://www.law.cornell.edu/uscode/text/15/78o",
            "relevance": "Assess the actual business-sale structure, eligibility conditions, and excluded activities before relying on the federal M&A broker exemption; separately assess state requirements.",
        },
        {
            "title": "26 U.S.C. 179D — Energy efficient commercial buildings deduction",
            "url": "https://www.law.cornell.edu/uscode/text/26/179D",
            "relevance": "Determine qualifying property, eligible allocation recipients, certification, applicable amount requirements, and the construction-start termination rule before developing an allocation mandate.",
        },
        {
            "title": "6 Del. C. Sections 9-301, 9-307, 9-503, and 9-506 — Secured-transactions search framework",
            "url": "https://delcode.delaware.gov/title6/c009/",
            "relevance": "Illustrates enacted UCC rules governing debtor location, governing law, debtor names, and misleading filing errors; apply the relevant jurisdiction's enacted provisions to the actual debtor.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Structure commercial buyer outreach around accurate transmission information, required sender identification, functioning opt-out mechanisms, and timely suppression.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on certain telephone equipment and communications",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Evaluate proposed calling and texting methods before activating enriched phone records, including applicable restrictions on automated communications.",
        },
        {
            "title": "48 CFR 52.203-5 — Covenant Against Contingent Fees",
            "url": "https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/section-52.203-5",
            "relevance": "Review applicability and the actual contract clause when compensation relates to obtaining federal contracts; do not assume every public-project success fee is permissible.",
        },
        {
            "title": "31 CFR Part 501 — Reporting, Procedures and Penalties Regulations",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-501",
            "relevance": "Support sanctions-related recordkeeping and reporting analysis alongside the applicable sanctions program, identity resolution, and ownership review.",
        },
    ],
}
