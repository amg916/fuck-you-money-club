from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small enterprise software reselling desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "SAM.gov Award Signals, AWS CPPO, Microsoft CSP, Tenant Diagnostics, and Evidence-Linked Renewal Pipelines",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #23, Enterprise Software Reselling, ranks #19 with a 72/100 Money-to-Manpower Score. "
        "Its information advantage comes from connecting procurement evidence to authorized channel economics, "
        "not collecting indiscriminate contact lists. This chapter maps nine plays: public-award timing, entity "
        "verification, deal-registration protection, AWS CPPO private offers, Microsoft CSP provisioning, renewal "
        "rescue, license reconciliation, implementation spreads, and commercial VCC settlement rebates. An "
        "eighteen-source directory specifies access, cost structure, refresh behavior, request discipline, and "
        "fallback evidence. The canonical annual owner profits remain $24,000 Conservative, $196,000 Base, and "
        "$500,000 Scaled, calculated on gross license resale and service billings with vendor costs included. "
        "Public records prioritize investigation; partner permissions, customer authorization, accepted offers, "
        "and reconciled settlements establish what the desk can actually sell and collect."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$300,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "8% net margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,400,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "14.0% net margin; $196,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$2,500,000",
            "context": "Annual gross license resale and service billings; vendor costs included in margin",
            "note": "20% net margin; $500,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an eighteen-source directory around evidence the desk can use",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the buying event, not the email address. The public-award timing play connects SAM.gov "
                    "opportunity notices, USAspending award records, and the buyer's published procurement calendar to "
                    "a specific software requirement. Capture notice identifier, agency, incumbent, contract vehicle, "
                    "period of performance, option language, and source retrieval time. An award ceiling is neither "
                    "available budget nor reseller revenue; obligations, modifications, and option exercises answer "
                    "different questions. For an illustrative prospecting batch, twenty relevant awards producing four "
                    "qualified $25,000 opportunities create $100,000 of prospective gross billings, not booked sales. "
                    "A contracting officer's current solicitation outranks an enrichment vendor's inferred renewal date. "
                    "FAR 4.1102 governs when prospective contractors generally need SAM registration, subject to its "
                    "exceptions; registration alone does not confer a contract vehicle, publisher authorization, or "
                    "permission to sell through another contractor's schedule. When an award description is sparse, "
                    "follow the linked notice and agency documents before approaching the incumbent's customer. "
                    "For state and municipal demand, use the issuing authority's procurement portal and appropriation "
                    "documents instead of assuming federal coverage. Store the exact passage supporting the trigger "
                    "so the salesperson can distinguish a funded requirement from a broad strategic aspiration."
                ),
                (
                    "The entity and buying-center verification play prevents a surprisingly expensive class of channel "
                    "errors: registering the wrong subsidiary, quoting the wrong tenant, or confusing a distributor "
                    "with the end customer. Join records using UEI, CIK, legal entity name, registered address, verified "
                    "domain, and customer-confirmed billing entity; never let a domain match silently merge two "
                    "companies. Delaware's entity search supplies formation clues, while paid status products answer "
                    "different questions; neither reveals a complete corporate buying hierarchy. SEC submissions "
                    "can establish public-company identity and published acquisitions, but a filing is not evidence "
                    "that every subsidiary shares a software agreement. Use ICANN Lookup to inspect registration "
                    "metadata where available, remembering that redaction and privacy services limit attribution. "
                    "A fifty-account review at six minutes per account consumes five analyst hours; budget that work "
                    "before buying thousands of enriched contacts. Record conflicting evidence and ask the customer "
                    "which entity owns the tenant and purchase order. If the subsidiary relationship remains unresolved, "
                    "retain separate account records and suspend only the affected quote. This keeps clean opportunities "
                    "moving without manufacturing certainty. The fallback is a customer-issued ordering document "
                    "and publisher account confirmation, not a guessed parent-company relationship derived from branding."
                ),
                (
                    "Use the directory below as an access register, not a promise that every source exposes a public "
                    "API or a fixed refresh interval. Free access often still requires an account, API key, registered "
                    "application, or restricted role. Paid enrichment plans change; record the actual subscribed quota "
                    "and unit price rather than hard-coding a promotional tariff. Separate source publication delay "
                    "from the desk's polling interval: polling an award feed hourly cannot accelerate an agency's "
                    "reporting. Every connector should retain request time, source update time when supplied, response "
                    "status, pagination cursor, and permitted retention period. Honor Retry-After, use exponential "
                    "backoff with jitter, and cap concurrent requests per credential. Never rotate identities to "
                    "evade a limit. For browser-only partner workspaces, use permitted exports or human review instead "
                    "of undocumented automation. Cache stable identifiers, but recheck permissions and commercial "
                    "terms before each offer. The nine mapped plays in this chapter are operational workflows; only "
                    "the VCC play carries the supplied machine identifier. Their unit examples explain decision "
                    "mechanics and are not additional scorecard forecasts. Assign one owner to each connector so "
                    "a broken feed produces a visible exception rather than silently aging prospect records."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost Structure, Freshness, Request Hygiene, and Evidence Fallbacks",
                "headers": [
                    "Named source and operating purpose",
                    "Exact access method and cost structure",
                    "Refresh behavior and request-limit discipline",
                    "Fallback source and interpretation boundary",
                ],
                "rows": [
                    [
                        "SAM.gov Opportunities supplies federal solicitations, amendments, and procurement timing signals.",
                        "Use GET https://api.sam.gov/opportunities/v2/search with an authorized API key; public access has no subscription charge.",
                        "Poll selected notice windows daily; amendments follow publication, and quotas depend on access class. Cache pages and honor service errors.",
                        "Open the notice at sam.gov and the issuing agency's attachments; the solicitation controls over extracted summaries.",
                    ],
                    [
                        "SAM.gov Entity Information supports UEI matching and federal registration checks.",
                        "Search entities through https://sam.gov using the available account permissions; public lookup is free, while restricted fields require entitlement.",
                        "Recheck registration before submission and ordering; source updates follow processing, not the desk's polling schedule. Avoid bulk browser extraction.",
                        "Request current entity confirmation from the bidder and compare official records; public registration does not establish publisher reseller authorization.",
                    ],
                    [
                        "USAspending links federal award recipients, obligations, agencies, and historical spending.",
                        "POST https://api.usaspending.gov/api/v2/search/spending_by_award/ with documented filters; public API access has no subscription charge.",
                        "Ingest filtered results daily; agency reporting creates variable lag. Paginate conservatively and retry transient failures with bounded backoff.",
                        "Check linked award identifiers against agency notices and contract documents; obligations and award ceilings represent different quantities.",
                    ],
                    [
                        "SEC EDGAR submissions establish issuer identity and locate acquisition disclosures.",
                        "GET https://data.sec.gov/submissions/CIK##########.json using a zero-padded ten-digit CIK and identifying User-Agent; public access is free.",
                        "Filings appear after SEC processing; stay below the SEC ceiling of ten requests per second across all machines and cache responses.",
                        "Use https://www.sec.gov/edgar/search/ and the issuer's filed documents; investor presentations cannot replace the underlying filing evidence.",
                    ],
                    [
                        "GSA eLibrary verifies schedule contractors, contract numbers, categories, and published terms.",
                        "Search https://www.gsaelibrary.gsa.gov through its public interface; public browsing carries no subscription charge.",
                        "Check at qualification and before quoting; updates follow contract administration. Use human review rather than assuming an unrestricted bulk API.",
                        "Obtain the contractor's current awarded terms and modifications; a category listing does not prove a particular SKU is authorized.",
                    ],
                    [
                        "GSA Advantage provides published catalog products and government purchasing references.",
                        "Search https://www.gsaadvantage.gov through the public catalog; browsing is free, while purchasing requires eligible access.",
                        "Refresh relevant product evidence before quoting; catalog updates follow supplier maintenance. Respect site restrictions and avoid automated mass extraction.",
                        "Compare current contract price lists and buyer requirements; displayed catalog pricing does not automatically equal negotiated transaction pricing.",
                    ],
                    [
                        "Acquisition.gov supplies the current FAR text and procurement-rule references.",
                        "Read https://www.acquisition.gov/browse/index/far and linked official sections; public access is free without a commercial data plan.",
                        "Review applicable sections when a solicitation changes; rule updates follow published effective dates. Cache citations instead of repeatedly crawling.",
                        "Use the solicitation's incorporated clauses and official Federal Register changes; agency supplements can add requirements beyond baseline FAR text.",
                    ],
                    [
                        "Delaware Division of Corporations helps distinguish legal entities from trading names.",
                        "Use https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx; basic entity search is free, while status products and certificates carry published fees.",
                        "Retrieve evidence during onboarding and material entity changes; administrative processing controls freshness. Perform targeted searches rather than bulk scraping.",
                        "Request a current formation or status document from the counterparty; basic search results do not establish complete ownership relationships.",
                    ],
                    [
                        "AWS Partner Central supports partner relationships and deal-registration evidence.",
                        "Access https://partnercentral.awspartner.com with the organization's assigned roles; workspace access depends on AWS partner enrollment and program terms.",
                        "Review deal changes daily and before quoting; visibility follows partner permissions. Use supported exports or specifically entitled integrations.",
                        "Obtain written confirmation from the publisher's channel manager; a submitted registration is not the same as an accepted registration.",
                    ],
                    [
                        "AWS Marketplace Catalog API inspects marketplace entities and permitted offer changes.",
                        "Use the AWS SDK or signed Catalog API operations ListEntities and DescribeEntity; AWS credentials and appropriate IAM permissions are required.",
                        "Refresh offer evidence before publication and acceptance review; changes can process asynchronously. Follow operation-specific quotas and backoff responses.",
                        "Use AWS Marketplace Management Portal records; Catalog access alone does not establish CPPO selling authorization or expose every buyer transaction.",
                    ],
                    [
                        "AWS Marketplace Agreement Service verifies agreements visible to an authorized participant.",
                        "Use signed SearchAgreements, DescribeAgreement, and GetAgreementTerms requests through an AWS SDK; commercial marketplace charges follow the transaction terms.",
                        "Retrieve after acceptance and during reconciliation; agreement visibility and service processing can lag. Follow documented regional endpoints and quotas.",
                        "Compare permitted seller reports and buyer confirmation; an agreement record alone does not establish that cash has settled.",
                    ],
                    [
                        "Microsoft Partner Center connects CSP customers, subscriptions, orders, and billing evidence.",
                        "Call https://api.partnercenter.microsoft.com/v1 with the required application and partner authorization; CSP participation and distributor costs follow contracted terms.",
                        "Refresh subscription events daily and billing records when published; use pagination, endpoint-specific limits, and Retry-After rather than unrestricted polling.",
                        "Use Partner Center exports or authorized distributor feeds; customer association does not grant unrestricted administrative access to every workload.",
                    ],
                    [
                        "Microsoft Graph subscribedSkus supports authorized license inventory and entitlement comparison.",
                        "GET https://graph.microsoft.com/v1.0/subscribedSkus with documented permissions and customer authorization; ordinary directory calls generally have no separate metered API charge.",
                        "Snapshot daily during reconciliation and after provisioning; directory propagation can delay changes. Honor Graph throttling and its Retry-After guidance.",
                        "Request a customer-generated Microsoft 365 license export; purchased capacity is not identical to assigned licenses or demonstrated application usage.",
                    ],
                    [
                        "Azure Cost Management Query exposes authorized subscription and billing-scope consumption evidence.",
                        "POST https://management.azure.com/{scope}/providers/Microsoft.CostManagement/query?api-version=2023-03-01 using an authorized scope; access depends on account type and roles.",
                        "Query daily with bounded date ranges; usage and adjustments arrive after consumption. Respect resource-specific throttling and avoid overlapping repeated queries.",
                        "Use authorized cost exports and finalized invoices; preliminary usage should not be treated as a settled customer receivable.",
                    ],
                    [
                        "Salesforce REST API connects CRM evidence, task routing, and account-level exception queues.",
                        "Use https://YOUR_INSTANCE.my.salesforce.com/services/data/ to discover supported versions; API availability depends on purchased edition, licenses, and organization settings.",
                        "Use incremental queries or entitled events; inspect the selected version's limits resource and response headers before scheduling bulk synchronization.",
                        "Import controlled CSV exports with stable external identifiers; do not overwrite salesperson decisions merely because enrichment returned a different value.",
                    ],
                    [
                        "People Data Labs Company Enrichment supplies commercial firmographic matching candidates.",
                        "GET https://api.peopledatalabs.com/v5/company/enrich with a licensed API key; paid credit plans and any trial allowance follow current account terms.",
                        "Enrich after public identity checks and cache permitted results; provider sourcing has variable age. Enforce credit ceilings and returned rate-limit headers.",
                        "Use the company's published website and official entity records; inferred attributes require verification before affecting account ownership or eligibility.",
                    ],
                    [
                        "Hunter Domain Search helps identify published business-contact patterns for verified companies.",
                        "GET https://api.hunter.io/v2/domain-search with an account API key; free allowance and paid credit tiers follow the subscribed plan.",
                        "Run only after domain verification and deduplicate requests; source dates can differ from retrieval dates. Respect account quotas and response limits.",
                        "Use the company's published contact page and switchboard; a returned address neither establishes buying authority nor authorizes indiscriminate outreach.",
                    ],
                    [
                        "ICANN Lookup supplies registration-data context for domain identity investigations.",
                        "Search https://lookup.icann.org through the public interface; lookup is free, and underlying RDAP availability varies by registry.",
                        "Check during account onboarding or suspicious domain changes; registry publication controls freshness. Respect upstream limits and avoid repeated exhaustive searches.",
                        "Compare customer-confirmed domains and official company websites; redacted registration data cannot establish beneficial ownership or tenant control.",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn authorized channel evidence into defensible quotes and renewal actions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The deal-registration protection play starts with publisher rules, accepted registration status, "
                    "covered account, eligible products, expiration, and named channel owner. Attach those facts to "
                    "the opportunity before producing a price. One hundred seats at $200 monthly produces $240,000 "
                    "of annual gross billings; at an illustrative $180 monthly vendor cost, the license spread is "
                    "$24,000 before support, commissions, payment costs, and overhead. A registration discount can "
                    "change that spread, but a submitted form does not earn it. Detect duplicate customer identifiers, "
                    "expired protection, geography restrictions, and opportunities already held by another partner. "
                    "When protection fails, ask the publisher for written terms or quote the unprotected economics; "
                    "do not preserve an expired discount inside a spreadsheet. The AWS CPPO private-offer play adds "
                    "a separate chain: publisher selling authorization, permitted buyer, wholesale economics, "
                    "reseller offer, acceptance, and settlement. An illustrative $100,000 customer offer against "
                    "$88,000 publisher cost leaves $12,000 before marketplace charges and delivery expenses. "
                    "Validate which party bears each charge and whether credits reduce proceeds. Capture immutable "
                    "offer and agreement identifiers rather than screenshots alone. If the authorization disappears "
                    "before acceptance, stop that offer and obtain renewed terms or use a publisher-approved alternative route."
                ),
                (
                    "The Microsoft CSP provisioning play needs distributor or direct-bill evidence, customer agreement "
                    "status, subscription term, billing frequency, cancellation window, and tenant-specific authorization. "
                    "Annual commitment and monthly payment are different fields: monthly collection does not necessarily "
                    "remove annual vendor liability. Two hundred seats at $30 monthly produces $72,000 annual gross "
                    "billings; an illustrative $66,000 vendor invoice leaves $6,000 before operating expenses. "
                    "Model a late-paying customer against the actual supplier due date, not the customer's preferred "
                    "payment schedule. The renewal rescue play joins the original accepted order to current subscription "
                    "records and customer-confirmed renewal intent. One hundred annual seats at $500 represent $50,000 "
                    "of renewal billings, not $50,000 of profit. Schedule ninety-, sixty-, and thirty-day tasks where "
                    "the actual commitment allows those interventions, then calculate the last effective change date "
                    "from the current contract. Keep commercial data collection separate from workload administration; "
                    "Partner Center visibility does not replace customer authorization for Graph access. Use granular "
                    "delegated roles where supported and revoke unused relationships. When API evidence conflicts "
                    "with the distributor's invoice, preserve both records, suspend the disputed adjustment, and "
                    "resolve the mismatch before promising a cancellation, credit, or seat reduction."
                ),
                (
                    "The license reconciliation play compares purchased capacity, assigned seats, disabled accounts, "
                    "group-based allocation, and customer-approved usage evidence without equating absence of one "
                    "signal with absence of business need. Twenty removable seats at $40 monthly imply $9,600 "
                    "of annual customer savings only when the commitment permits reduction. That savings figure "
                    "is not operator revenue, and seat removal can reduce the reseller's own recurring spread. "
                    "Charge for the assessment or expand implementation work only under an agreed statement of work. "
                    "The implementation-spreads play converts verified entitlement gaps into scoped delivery: eighty "
                    "hours billed at $175 yields $14,000 of service billings; eighty delivery hours costing $100 "
                    "yields $8,000 of direct cost and a $6,000 contribution before overhead. Define migration batches, "
                    "identity prerequisites, rollback procedures, acceptance tests, and customer responsibilities. "
                    "Keep change orders separate from the original estimate. Diagnostic tools should answer concrete "
                    "questions: Graph identifies entitlement discrepancies, Azure Cost Management identifies consumption "
                    "patterns, and a customer-approved export establishes the baseline when API access is unavailable. "
                    "Never purchase a broad administrative role merely to simplify discovery. If usage telemetry is "
                    "restricted, deliver an entitlement-only assessment and identify the missing evidence explicitly "
                    "rather than inventing utilization percentages."
                ),
            ],
            "table": {
                "caption": "Six Channel Forensic Checks That Protect Quote Spread and Customer Commitments",
                "headers": [
                    "Evidence object and exact operational question",
                    "Required join and verification procedure",
                    "Failure mode that changes transaction economics",
                    "Concrete recovery and retained audit evidence",
                ],
                "rows": [
                    [
                        "Publisher registration: determine whether protection covers this customer, product, and territory.",
                        "Join accepted registration identifier to legal buyer, product family, expiration date, and named publisher owner.",
                        "Expired or mismatched registration removes the assumed discount and can leave the quote below cost.",
                        "Obtain renewed written terms or reprice using unprotected costs; retain the superseded quote and decision record.",
                    ],
                    [
                        "AWS CPPO authorization: establish permitted resale economics before creating the buyer offer.",
                        "Match selling authorization, product identifier, buyer account, allowed duration, and publisher wholesale terms.",
                        "An authorization change or excluded buyer invalidates the expected route and can prevent offer creation.",
                        "Refresh publisher permission and regenerate the offer; retain authorization versions and the affected opportunity identifier.",
                    ],
                    [
                        "AWS agreement and settlement: distinguish accepted commitments from actual collectible proceeds.",
                        "Join offer identifier, agreement identifier, billing schedule, seller report, marketplace charges, and settlement reference.",
                        "Acceptance without matching settlement can hide deductions, collection delay, or incorrect expected payment timing.",
                        "Reconcile permitted marketplace reports and open the relevant support case without marking unsettled cash as collected.",
                    ],
                    [
                        "Microsoft CSP subscription: establish the real commitment and permitted adjustment dates.",
                        "Match customer tenant, subscription identifier, SKU, term, billing cycle, renewal setting, and supplier invoice.",
                        "Monthly customer billing can mask annual vendor exposure and make an apparently flexible cancellation expensive.",
                        "Confirm current publisher rules and distributor terms; obtain customer authorization before any permitted subscription change.",
                    ],
                    [
                        "License assignment inventory: identify removable capacity without disrupting necessary business access.",
                        "Compare purchased capacity, assignments, group rules, account status, customer confirmation, and permitted reduction date.",
                        "Removing seats from sparse telemetry can interrupt service while contractual charges continue through the committed term.",
                        "Use a customer-reviewed exception list and reversible assignment changes; retain before-and-after inventory snapshots.",
                    ],
                    [
                        "Implementation work package: establish the billable scope and direct delivery exposure.",
                        "Join signed scope, hourly assumptions, named deliverables, subcontractor rates, acceptance tests, and change-order identifiers.",
                        "Unpriced migration exceptions consume the projected service spread and turn license profit into delivery losses.",
                        "Pause only the affected work package, document the dependency, and price the approved change before continuing.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the small details that determine whether the spread survives",
                "body": "Channel profit usually fails at a join between commercial records, not at the headline discount.",
                "items": [
                    "Save the publisher authorization and accepted registration version used for every quote; a later portal view may no longer show the original economics.",
                    "Store subscription commitment length separately from invoice frequency so monthly collection never disguises annual vendor exposure.",
                    "Put the last effective renewal-change date on the CRM task, not merely the service anniversary; derive it from the current agreement.",
                    "Reconcile marketplace deductions against the specific offer and settlement period before paying sales commissions on apparent spread.",
                ],
            },
        },
        {
            "heading": "3. Engineer a provenance-first enrichment waterfall and exception pipeline",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the enrichment waterfall in this order: customer-provided identity, official entity evidence, "
                    "company-published domain and buying context, licensed company enrichment, then targeted contact "
                    "discovery. Reject the common shortcut of enriching a guessed domain and treating the returned "
                    "person as proof of account ownership. Every field needs source URL or request reference, retrieval "
                    "time, source date when available, confidence rationale, usage restriction, and verification owner. "
                    "Keep source observations immutable; materialize the preferred account view separately so an analyst "
                    "can reverse an incorrect merge. A practical record contains legal_entity_id, domain, tenant_id, "
                    "publisher_customer_id, opportunity_id, observed_at, and evidence_reference. Encrypt customer "
                    "identifiers, restrict exports, and exclude tokens from logs. For an illustrative waterfall, "
                    "researching 200 accounts with official and customer records might resolve 140; enriching the "
                    "remaining 60 at an assumed $0.50 per successful lookup costs $30 before contact discovery. "
                    "Those figures are workload assumptions, not vendor tariffs. If confidence remains weak, "
                    "route the account to manual review rather than repeatedly purchasing the same ambiguous match. "
                    "Apply provider retention terms to cached data and record deletion deadlines. A cheap enrichment "
                    "credit becomes expensive when it creates a duplicate registration, misdirected quote, or avoidable "
                    "customer complaint."
                ),
                (
                    "Implement the first pipeline with Python's urllib.request, json, sqlite3, datetime, hashlib, "
                    "and logging modules, or use the same controls in an existing integration platform. Separate "
                    "connectors from normalization, identity resolution, and business actions. A successful HTTP "
                    "response is not proof of complete ingestion: validate required fields, traverse pagination, "
                    "record counts, and persist the last completed checkpoint only after committing the batch. "
                    "Use stable source identifiers plus payload hashes to make reruns idempotent. Preserve raw "
                    "responses only where the license permits retention, and redact credentials before storage. "
                    "For time-based queries, overlap the previous window and deduplicate because late updates "
                    "and clock differences otherwise create gaps. Handle deletions and revoked permissions as "
                    "explicit states rather than silently retaining stale authority. A failed connector must not "
                    "erase the last verified customer record. Alert on authentication failures, repeated throttling, "
                    "schema drift, empty-result anomalies, and unusual record-count changes. When a provider changes "
                    "an endpoint, freeze automated quote inputs from that connector while allowing unrelated workflows "
                    "to continue. Keep secrets in the organization's selected secret store, scope keys narrowly, "
                    "and test rotation. Operators need evidence of freshness and completeness, not a decorative "
                    "dashboard that remains green after a partial import."
                ),
                (
                    "Make the output a queue of decisions, not a warehouse of interesting facts. Each exception "
                    "should name the customer, conflicting evidence, affected commercial action, accountable person, "
                    "due time, and recovery instruction. A renewal alert without a verified commitment date should "
                    "request verification, not automatically send a price. A license mismatch should produce a "
                    "reviewable delta, not silently remove access. Run contract tests against retained, sanitized "
                    "fixtures covering pagination, expired credentials, repeated events, changed field types, and "
                    "revoked customer permissions. Measure match accuracy on a manually adjudicated sample and "
                    "track false positives separately from unresolved records. For outreach, 15 U.S.C. 7704 establishes "
                    "requirements including accurate headers, nondeceptive subjects, sender identification, a valid "
                    "postal address, and a working opt-out mechanism where applicable; suppress opted-out recipients "
                    "across every connected sending tool. If a covered business processes California residents' "
                    "personal information, map applicable duties under Cal. Civ. Code 1798.100 to collection, "
                    "retention, and contracted service-provider processing. Public availability does not erase "
                    "provider terms or relevant privacy duties. Use role-based access and short retention for "
                    "contact exports. If the desk cannot explain why a field is needed for a live account action, "
                    "stop collecting it and simplify the pipeline."
                ),
            ],
            "table": {
                "caption": "Six Pipeline Controls with Observable Failure Tests and Recovery Paths",
                "headers": [
                    "Control and record being protected",
                    "Implementation and observable success condition",
                    "Diagnostic test using permitted sample data",
                    "Fallback action preserving usable customer evidence",
                ],
                "rows": [
                    [
                        "Identity resolution protects legal buyers from accidental parent-company or subsidiary merges.",
                        "Require stable identifiers or analyst-confirmed evidence before merging; preserve original records and the merge rationale.",
                        "Replay two subsidiaries sharing a domain and verify that distinct billing entities remain independently addressable.",
                        "Split the proposed merge into separate accounts and request customer-issued ordering evidence before quoting.",
                    ],
                    [
                        "Incremental ingestion protects updated opportunities from skipped pages and late-arriving source changes.",
                        "Commit checkpoints only after complete pagination; overlap query windows and deduplicate using stable source identifiers.",
                        "Inject a repeated page and a delayed amendment; verify one current record with both observations retained.",
                        "Replay the last completed window from the saved checkpoint without resetting unrelated connectors or duplicating tasks.",
                    ],
                    [
                        "Credential isolation protects customer permissions and prevents secrets from leaking into operational logs.",
                        "Use scoped credentials from the selected secret store; redact authorization headers and record credential ownership.",
                        "Expire a test credential and inspect logs for clean redaction plus an actionable authentication exception.",
                        "Suspend that connector, rotate through the authorized owner, and retain the last verified snapshot with its timestamp.",
                    ],
                    [
                        "Quota management protects subscribed credits and keeps authorized requests within service limits.",
                        "Apply per-provider concurrency limits, Retry-After handling, bounded retries, cached lookups, and daily credit budgets.",
                        "Simulate a throttled response and verify delayed retries without identity rotation or duplicated billable enrichment.",
                        "Queue the remaining work for the next permitted window and use already licensed evidence for urgent review.",
                    ],
                    [
                        "Schema validation protects quote inputs from silently changed provider response formats.",
                        "Validate required identifiers and value types before normalization; route unexpected payloads into a restricted exception queue.",
                        "Replace a subscription date with an incompatible value and verify that no renewal action is generated.",
                        "Use the last verified contractual date while an operator checks the source and updates the connector test.",
                    ],
                    [
                        "Suppression synchronization protects recipients from repeated outreach after an applicable opt-out request.",
                        "Maintain a shared suppression identifier and propagate changes to CRM, enrichment exports, and every sending system.",
                        "Submit a test opt-out and verify that subsequent campaign exports exclude the matching permitted identifiers.",
                        "Pause the affected mailing segment until suppression delivery is confirmed across all connected systems.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and permission boundary",
                    "action": "Record the named provider, authorized account, permitted fields, owner, quota, and retention terms.",
                    "detail": "Test one narrow request or permitted export; document the fallback before allowing the source to influence a quote.",
                },
                {
                    "step": 2,
                    "title": "Load evidence without changing commercial records",
                    "action": "Ingest a small batch into immutable observations with timestamps, stable identifiers, and redacted request references.",
                    "detail": "Verify pagination, duplicates, source lag, and failed-request handling before advancing the checkpoint.",
                },
                {
                    "step": 3,
                    "title": "Resolve identity and review material discrepancies",
                    "action": "Join confirmed entities, tenants, subscriptions, and offers; assign ambiguous matches to a named operator.",
                    "detail": "Keep source disagreements visible and prevent unresolved evidence from automatically changing prices, commitments, or customer access.",
                },
                {
                    "step": 4,
                    "title": "Publish bounded actions and reconcile outcomes",
                    "action": "Create verified renewal tasks, quote inputs, and license-review exceptions with evidence links and due dates.",
                    "detail": "Compare completed actions with accepted orders, supplier invoices, and settlements; feed errors back into connector fixtures.",
                },
            ],
        },
        {
            "heading": "4. Underwrite the VCC extension without confusing payment volume with reseller revenue",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The ninth mapped play, b2b_commercial_vcc_interchange_rebate_arbitrage, embeds an automated accounts "
                    "payable and vendor-settlement service beside the software relationship. Freight brokers, construction "
                    "general contractors, medical suppliers, property managers, and media agencies can have substantial "
                    "third-party invoice flows, but invoice volume belongs to their payment operation, not the reseller's "
                    "top line. Work through an authorized issuing and payment-platform partner; the software desk should "
                    "not assume custody of customer funds or issuing authority. The play's 140–195 basis-point "
                    "rebate range is a commercial underwriting assumption requiring a signed schedule, eligible volume "
                    "definition, exclusions, chargeback treatment, and payout timing. It is not a universal network "
                    "entitlement or a promise of uncapped earnings. At $10,000,000 of eligible settled invoices, "
                    "175 basis points produces $175,000 of platform-level rebate before contractual adjustments. "
                    "If the desk receives a contracted forty-percent share, its potential receipts are $70,000 "
                    "before its own costs, not $10,000,000 and not the full $175,000. Verify whether the agreement "
                    "treats those receipts as service compensation or another accounting category. This optional "
                    "sandbox example is excluded from the canonical resale and services scorecard. A rejected "
                    "card authorization, reversed invoice, or ineligible merchant must reduce the eligible-volume ledger."
                ),
                (
                    "Build a vendor acceptance waterfall before selling instant settlement. Start with the customer's "
                    "authorized AP export, deduplicate vendor identities, verify invoice approval and beneficiary "
                    "details through established controls, and segment existing card acceptance. Request the platform's "
                    "documented APIs for card creation, transaction webhooks, settlement reports, and rebate statements; "
                    "account access and permitted fields depend on the actual contract. Bind each single-use credential "
                    "to the intended invoice, amount, expiry, and supported merchant controls without storing sensitive "
                    "card data in the CRM. The specified fallback injects Level-3 line-item invoice metadata where "
                    "the issuer, processor, merchant, and network support it; metadata alone neither forces acceptance "
                    "nor guarantees qualification. For card-averse suppliers, offer an agreed early-pay ACH discount "
                    "of 1.5%–2% for payment within ten days against a clearly stated original due date. On a "
                    "$100,000 invoice, that is $1,500–$2,000 of supplier-funded discount before funding and platform "
                    "costs; allocate the benefit according to contract rather than claiming it all as desk income. "
                    "Focus acquisition on fragmented long-tail vendor bases, but validate actual acceptance with a "
                    "small authorized cohort. If early payment consumes working capital, price that cost and retain "
                    "ordinary ACH as the no-discount fallback."
                ),
                (
                    "Keep the scorecard anchored while the data stack expands. Conservative remains $300,000 gross "
                    "license resale and service billings multiplied by 8%, producing $24,000 annual owner net profit "
                    "with 2 FT + 3 C. Base remains $1,400,000 multiplied by 14.0%, producing $196,000 with "
                    "2 FT + 3 C. Scaled remains $2,500,000 multiplied by 20%, producing $500,000 with "
                    "3 FT + 4 C. Vendor costs are already included in those margins; do not subtract them "
                    "again or add client cloud consumption, AP principal, customer savings, and marketplace "
                    "commitments to revenue. The directory is an operating architecture, not evidence that any "
                    "scenario has been achieved. Track software spread, implementation contribution, tool subscriptions, "
                    "contractor expense, bad debt, and collection timing in separate reconciled accounts. Gross "
                    "presentation also requires review of whether the desk controls the promised goods or services "
                    "before transfer; a marketplace label alone does not settle principal-versus-agent treatment. "
                    "Respect the $25,000–$150,000 startup capital range, $5,000–$25,000 monthly operating expense "
                    "range, and three-to-twelve-month first-deal horizon when buying tools. Start with official "
                    "records and existing partner exports, then purchase enrichment only when a measured bottleneck "
                    "justifies it. Scale connector coverage after match quality and collected contribution improve, "
                    "not because a vendor dashboard displays more accounts."
                ),
            ],
            "table": {
                "caption": "VCC and Reseller Economics: Unit Math, Recognition Boundaries, and Risk Fallbacks",
                "headers": [
                    "Illustrative transaction or canonical operating case",
                    "Exact arithmetic and economic interpretation",
                    "Evidence needed before using the result",
                    "Risk fallback and operational accounting treatment",
                ],
                "rows": [
                    [
                        "Commercial VCC sandbox using ten million dollars of eligible settled invoice principal.",
                        "$10,000,000 multiplied by 1.75% equals $175,000 upstream rebate; forty-percent desk participation equals $70,000 before desk costs.",
                        "Signed rebate schedule, accepted merchant cohort, settled transaction ledger, exclusions, reversals, and participation agreement establish eligibility.",
                        "Exclude invoice principal from revenue and exclude this optional example from canonical cases; reconcile actual earned compensation separately.",
                    ],
                    [
                        "Early-pay ACH alternative for a card-averse supplier with a hundred-thousand-dollar approved invoice.",
                        "$100,000 multiplied by 1.5%–2% equals $1,500–$2,000 discount before funding costs and contractual benefit allocation.",
                        "Supplier acceptance, original due date, ten-day payment terms, beneficiary verification, and completed settlement establish the discount.",
                        "Use ordinary ACH when the supplier declines; never book the customer's entire discount as the desk's own compensation.",
                    ],
                    [
                        "Conservative canonical case with two full-time staff and three contractors.",
                        "$300,000 gross resale and service billings multiplied by 8% equals $24,000 annual owner net profit.",
                        "Accepted customer orders, supplier invoices, service billings, operating expenses, and collection records support the scenario comparison.",
                        "Vendor costs remain inside the stated margin; monitor overdue receivables without counting underlying customer payment volume.",
                    ],
                    [
                        "Base canonical case with two full-time staff and three contractors.",
                        "$1,400,000 gross resale and service billings multiplied by 14.0% equals $196,000 annual owner net profit.",
                        "Reconciled channel economics, collected implementation invoices, retained renewals, and complete operating costs support the scenario comparison.",
                        "Do not add illustrative deal spreads or optional rebate receipts to the canonical profit; rebuild any revised forecast explicitly.",
                    ],
                    [
                        "Scaled canonical case with three full-time staff and four contractors.",
                        "$2,500,000 gross resale and service billings multiplied by 20% equals $500,000 annual owner net profit.",
                        "Seven-person staffing costs, vendor charges, delivery capacity, collected billings, and tool expenses support the scenario comparison.",
                        "Expand automation only with reliable exceptions and sufficient working capital; preserve customer and supplier commitment boundaries.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four boundaries before releasing an offer or payment workflow",
                "body": "A public signal can justify investigation; these checks establish whether the proposed transaction is executable.",
                "items": [
                    "Confirm the legal buyer, publisher authorization, protected account scope, and current commercial terms against retained source evidence.",
                    "Confirm customer permission for each tenant, billing scope, AP dataset, and administrative action; keep discovery credentials narrower than execution credentials.",
                    "Confirm commitment dates, supplier payment exposure, marketplace deductions, and collection assumptions before accepting the quoted spread.",
                    "Confirm VCC acceptance, eligible settled volume, contracted rebate allocation, supported Level-3 fields, and agreed ACH fallback before projecting earned receipts.",
                ],
            },
        },
    ],
    "pull_quote": "The strongest reseller dataset links every buying signal to verified authority, every quote to current cost, and every profit claim to reconciled evidence.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create the eighteen-source access register with a named owner, authorized credential, polling interval, quota, retention rule, and fallback for each source.",
        "Join ten target accounts using official entity identifiers and customer-confirmed tenant or buying entities; resolve conflicts before purchasing contact enrichment.",
        "Attach accepted publisher registration, CPPO authorization, or CSP commitment evidence to every live quote and calculate spread after identifiable transaction costs.",
        "Implement checkpointed ingestion, overlapping update windows, bounded retries, immutable observations, and a visible queue for identity and renewal exceptions.",
        "Pilot VCC settlement only with an authorized platform and consenting vendor cohort; reconcile eligible principal, upstream rebate, desk share, and ACH alternatives separately.",
        "Reconcile operating reports to $24,000, $196,000, and $500,000 canonical annual owner profits without adding client principal, customer savings, or illustrative deal examples.",
    ],
    "statutory_citations": [
        {
            "title": "FAR 4.1102 — System for Award Management registration policy",
            "url": "https://www.acquisition.gov/far/4.1102",
            "relevance": "Establishes the general SAM registration requirement and exceptions for prospective federal contractors; registration must be checked in the actual procurement context.",
        },
        {
            "title": "FAR 8.405-1 — Ordering procedures for supplies and services not requiring a statement of work",
            "url": "https://www.acquisition.gov/far/8.405-1",
            "relevance": "Explains applicable Federal Supply Schedule ordering procedures; a catalog listing does not eliminate the ordering activity's required purchasing process.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Supplies concrete requirements for commercial email content, identification, opt-out handling, and other prohibited practices relevant to enriched prospect outreach.",
        },
        {
            "title": "Cal. Civ. Code 1798.100 — General duties of businesses collecting personal information",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": "For covered businesses, connects personal-information collection to notice, purpose, retention, and contractual duties when using service providers or other recipients.",
        },
        {
            "title": "17 CFR 240.13a-1 — Requirements of annual reports",
            "url": "https://www.ecfr.gov/current/title-17/section-240.13a-1",
            "relevance": "Provides primary authority for annual reporting by covered Exchange Act registrants, supporting the distinction between filed issuer evidence and commercial enrichment claims.",
        },
    ],
}
