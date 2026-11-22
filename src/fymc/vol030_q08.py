from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small lending & flash-funding arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Dockets, UCC Searches, SEC APIs, Title-Agent Verification, and Escrow Evidence Under FCRA, State Lending Rules, and UCC Article 9",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #30, Lending & Flash-Funding Arbitrage, ranks #04 of 36 with a "
        "93/100 Money-to-Manpower Score. Across the volume's 14 mapped plays, this "
        "chapter develops public_record_api_intelligence into an eighteen-source "
        "directory and a controlled evidence pipeline. County records identify "
        "situations; commercial APIs normalize parcels; licensing registries and "
        "independent callbacks test counterparties; escrow confirmations determine "
        "whether money moves. Conservative annual fee revenue of $120,000 produces "
        "$36,000 owner profit; Base revenue of $535,000 produces $227,375; Scaled "
        "revenue of $950,000 produces $522,500. Principal passing through escrow is "
        "excluded throughout. The operating advantage is faster rejection of weak "
        "files and faster assembly of independently verified closing evidence, "
        "not faster wiring against a convincing dashboard."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual earned funding fees, EMD JV splits, and origination points; escrow principal excluded",
            "note": "30% net margin; $36,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$535,000",
            "context": "Annual earned funding fees, EMD JV splits, and origination points; escrow principal excluded",
            "note": "42.5% net margin; $227,375 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$950,000",
            "context": "Annual earned funding fees, EMD JV splits, and origination points; escrow principal excluded",
            "note": "55% net margin; $522,500 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build the public-record spine before buying enrichment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement public_record_api_intelligence as a provenance system, not a scraped "
                    "lead list. Start with the jurisdictions where the desk can actually fund "
                    "through an independently verified, bonded settlement agent. For each county, "
                    "record its recorder portal, assessor parcel key, civil and probate docket "
                    "access, document prices, export options, and published automation restrictions. "
                    "Use county plus parcel identifier as the property key; use jurisdiction plus "
                    "entity filing number as the company key. Preserve original names alongside "
                    "normalized names because punctuation removal can merge unrelated businesses. "
                    "Every observation needs source URL, retrieval time, source effective date, "
                    "document identifier, content hash, and the operator who resolved ambiguity. "
                    "A recorded deed establishes a historical instrument, not a current title "
                    "opinion. An assessor owner field can lag a transfer, and a probate docket "
                    "can exist without authority to sell. Route these differences to an exception "
                    "queue rather than overwriting the older record. The useful output is a "
                    "compact evidence packet showing what changed, which business relationship "
                    "might need liquidity, and which missing document prevents further action. "
                    "Keep lead discovery separate from underwriting so a promising public signal "
                    "cannot silently become an approved advance."
                ),
                (
                    "The first six directory entries cover fragmented records that national feeds "
                    "often flatten. A newly filed probate matter may identify a property whose "
                    "authorized representative will eventually need a coordinated sale, but the "
                    "filing alone supplies neither transferable rights nor a closing timetable. "
                    "Require letters of administration, the relevant court orders, and settlement "
                    "counsel's interpretation before treating an estate transaction as fundable. "
                    "Unclaimed property is similarly a research trigger: an official ledger may "
                    "show a possible claim, but a name match does not establish entitlement or "
                    "an uncontested recovery. Do not buy supposed claim ownership from an "
                    "intermediary without verified authority and applicable state requirements. "
                    "For a business borrower, compare active entity status, actual signing "
                    "authority, and the correct UCC search jurisdiction; UCC section 9-307 "
                    "often places a registered organization in its organizing state. A clean "
                    "property address search cannot substitute for a debtor-name search. Store "
                    "negative findings with the exact search terms and timestamp, because "
                    "absence from one portal is not evidence of absence everywhere. These "
                    "records prioritize verified outreach to businesses and authorized "
                    "representatives; they do not authorize intrusive contact with relatives "
                    "or extraction of restricted case material."
                ),
                (
                    "Use the named public sources below as jurisdiction examples, then reproduce "
                    "the same source contract wherever the desk operates. Access charges and "
                    "portal limits change; record the current published schedule during onboarding "
                    "instead of embedding a guessed nationwide price. Distinguish polling cadence "
                    "from source latency: checking every hour cannot accelerate a recorder's "
                    "indexing process. Default to a daily retrieval queue, cache unchanged "
                    "responses, and stop automated collection when authentication, CAPTCHA, or "
                    "terms prohibit it. The explicit fallback for public_record_api_intelligence "
                    "is scheduled bulk FOIA/public-record exports, official data feeds, and "
                    "low-frequency cached queues. Federal FOIA does not govern county offices, "
                    "so use the relevant state public-record process for local exports. In an "
                    "illustrative monthly batch, $600 of records and enrichment expense across "
                    "300 candidate events costs $2 per event; if only thirty survive identity "
                    "and relevance checks, acquisition cost is $20 per eligible review. Neither "
                    "number represents a funded-deal cost until actual conversions are known. "
                    "Track that denominator explicitly. If a source becomes stale, preserve "
                    "its last retrieval date, suspend claims of freshness, and substitute a "
                    "document order or a dated manual search."
                ),
            ],
            "table": {
                "caption": "Named Directory, Part 1 of 3: Six Official Record Sources and Their Operating Contracts",
                "headers": [
                    "Named source and specific operator purpose",
                    "Exact access method and cost tier",
                    "Refresh latency and rate-limit operating discipline",
                    "Fallback evidence and decisive interpretation limit",
                ],
                "rows": [
                    [
                        "Maricopa County Recorder: recorded instruments and document identifiers",
                        "Use https://recorder.maricopa.gov/ and select recorded-document search; public lookup is available, with document products priced by the county.",
                        "Capture recording date separately from retrieval time; indexing lag varies, and automated access requires published permission or an agreed export.",
                        "Order the identified instrument directly from the recorder; use a current title commitment for ownership and lien conclusions.",
                    ],
                    [
                        "Maricopa County Assessor: parcel identity and situs reconciliation",
                        "Use https://mcassessor.maricopa.gov/ parcel search; public lookup is free, while bulk products follow the assessor's current distribution terms.",
                        "Assessment and ownership fields follow office updates, not live closings; cache parcel responses and avoid repeated address permutations.",
                        "Compare the legal description with recorded instruments and the settlement file; assessor ownership alone does not clear title.",
                    ],
                    [
                        "Maricopa Superior Court Clerk: civil and probate case evidence",
                        "Start at https://www.clerkofcourt.maricopa.gov/ and follow records access; public indexes and paid copies have different availability rules.",
                        "Docket publication follows clerk processing and case restrictions; poll conservatively and never automate around restricted-document access controls.",
                        "Request accessible docket entries and certified authority documents from the clerk; a case opening does not establish sale authority.",
                    ],
                    [
                        "Florida Treasure Hunt: official unclaimed-property claimant research",
                        "Search https://fltreasurehunt.gov/ using the official owner-search workflow; state search and direct claim submission are free services.",
                        "Holder reporting and state processing determine publication timing; use deliberate manual searches unless an authorized bulk channel is provided.",
                        "Use the state's direct claims process and ownership evidence; a matching name does not establish an assignable receivable.",
                    ],
                    [
                        "Florida Sunbiz: entity status and registered filing identifiers",
                        "Use https://search.sunbiz.org/ for entity searches; basic records are free, while certified documents follow the official fee schedule.",
                        "Retrieve filing history with its effective dates; cache stable records and obtain published bulk data rather than aggressive page scraping.",
                        "Order official entity documents and inspect the operating agreement; registered-agent status does not establish authority to borrow.",
                    ],
                    [
                        "California Secretary of State: debtor-name UCC filing research",
                        "Use https://bizfileonline.sos.ca.gov/ and the UCC service workflow; search products and certified records follow posted state fees.",
                        "Measure coverage using the search certificate's through-date; use permitted account workflows and avoid automated name-variant request floods.",
                        "Obtain an official search report and relevant amendments; confirm debtor location and exact legal name before interpreting results.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the evidence that cheap lead feeds discard",
                "body": "A small desk wins by retaining provenance, resolving identities once, and refusing to convert record hints into unsupported closing assumptions.",
                "items": [
                    "Save the recorder instrument number and legal description before purchasing enrichment; one address can describe several parcels or condominium interests.",
                    "Build a county-specific alias map for subdivisions and street abbreviations, but require a human match when parcel boundaries or legal descriptions disagree.",
                    "Request public-record exports with stable identifiers and modified-date fields; incremental files reduce both clerk workload and duplicate processing.",
                    "Track record-to-qualified-review and qualified-review-to-funded-deal conversion separately; a cheap event feed can still produce expensive completed deals.",
                ],
            },
        },
        {
            "heading": "2. Turn public APIs into a bounded enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run enrichment in an inexpensive-to-expensive order with a documented reason "
                    "for every paid call. First reconcile the parcel and entity against official "
                    "identifiers. Next obtain public company filings, federal registration "
                    "evidence where relevant, sanctions screening inputs, flood context, address "
                    "coordinates, and bank identity. Only then purchase missing property or "
                    "court attributes. The next six directory entries are not interchangeable "
                    "credit scores: SEC filings concern reporting entities, SAM registration "
                    "does not establish creditworthiness, and FDIC bank data does not prove "
                    "that an account belongs to a closing agent. Each source answers a narrow "
                    "question and leaves an explicit remainder. For example, match a bank's "
                    "name and certificate number before reviewing wire instructions, but obtain "
                    "beneficiary-account confirmation through independent controls. Match "
                    "sanctions candidates using identifiers and context, not a normalized name "
                    "alone. Human review resolves possible matches before funds move. Keep "
                    "consumer-report products outside this discovery waterfall unless the desk "
                    "has a documented permissible purpose under 15 U.S.C. 1681b and a workflow "
                    "for the resulting obligations. Public-record availability does not erase "
                    "restrictions attached to a commercial report or permit repurposing "
                    "sensitive information without reviewing its contractual use limits."
                ),
                (
                    "Give every connector its own credentials, request budget, timeout, retry "
                    "policy, and parser version. SEC automated access requires an identifying "
                    "User-Agent and adherence to its fair-access ceiling of ten requests per "
                    "second; operate materially below that ceiling rather than treating it as "
                    "a throughput target. Other services expose limits through documentation, "
                    "contracts, or response headers, so do not copy the SEC number into a "
                    "global setting. Honor HTTP 429 and Retry-After, use exponential backoff "
                    "with jitter, and quarantine repeated authorization failures instead of "
                    "retrying them indefinitely. Conditional requests using ETag or Last-Modified "
                    "reduce unnecessary transfers where supported. Store retrieval status "
                    "separately from the last successful payload so an outage never appears "
                    "as a clean search. A schema change should fail closed for mandatory "
                    "fields such as entity identifier, parcel number, or document date while "
                    "allowing noncritical description fields to enter a review queue. Hash "
                    "the original payload and retain its source reference under an appropriate "
                    "retention schedule. This supports reproducible underwriting without "
                    "keeping unnecessary personal data forever. Alerts should identify the "
                    "affected deals and required manual substitutes, not merely announce "
                    "that a background job stopped."
                ),
                (
                    "Measure the waterfall using reviewed files rather than raw API activity. "
                    "Suppose 300 monthly events produce thirty relevant files, twelve files "
                    "need a paid $5 property lookup, and six require a $15 document package. "
                    "Those illustrative variable charges total $150, or $5 per relevant file, "
                    "before subscriptions, labor, and official copies. If an existing $600 "
                    "monthly research budget already includes those charges, do not add them "
                    "again when calculating the earlier $20 review cost. Maintain a cost "
                    "ledger by provider, deal identifier, and purpose so that retries and "
                    "duplicate purchases are visible. Cache immutable instruments by document "
                    "identifier and version mutable records by retrieval time. A possible "
                    "probate or unclaimed-property trigger stays in discovery until authority "
                    "and ownership are resolved; it never becomes a projected recovery merely "
                    "because several providers repeat the same record. When an API fails, "
                    "degrade to official bulk files, scheduled public-record exports, and "
                    "low-frequency cached queues with conspicuous freshness dates. A mandatory "
                    "closing check cannot degrade to stale evidence: replace it with a "
                    "current independent verification or defer the transaction. This preserves "
                    "the speed advantage without converting missing data into a false "
                    "positive underwriting decision."
                ),
            ],
            "table": {
                "caption": "Named Directory, Part 2 of 3: Six Public APIs and Feeds with Explicit Semantic Limits",
                "headers": [
                    "Named source and specific operator purpose",
                    "Exact access method and cost tier",
                    "Refresh latency and rate-limit operating discipline",
                    "Fallback evidence and decisive interpretation limit",
                ],
                "rows": [
                    [
                        "SEC EDGAR submissions API: reporting-company identity and filings",
                        "Use https://data.sec.gov/submissions/CIK##########.json with a ten-digit CIK; access is free and requires an identifying User-Agent.",
                        "Submissions typically update throughout the day as filings disseminate; remain below ten requests per second and honor fair-access instructions.",
                        "Use https://www.sec.gov/edgar/search/ or published bulk archives; filings describe reporting entities rather than verifying an escrow balance.",
                    ],
                    [
                        "SAM.gov Entity Management API: federal registration corroboration",
                        "Request an authorized key through https://sam.gov/ and use https://api.sam.gov/entity-information/v3/entities under the current public API documentation.",
                        "Public API access is free within assigned permissions; quotas vary by role, and registration changes require processing before appearing.",
                        "Use SAM.gov public entity search and save the retrieval date; an active registration is not evidence of repayment capacity.",
                    ],
                    [
                        "OFAC Sanctions List Service: current official screening inputs",
                        "Download official list files through https://sanctionslist.ofac.treas.gov/; Treasury provides these screening inputs without a subscription charge.",
                        "Refresh on Treasury releases and before funding; compare file hashes, respect service responses, and avoid repeated unchanged downloads.",
                        "Use https://sanctionssearch.ofac.treas.gov/ for documented manual review; assess ownership-based restrictions rather than relying solely on listed-name matches.",
                    ],
                    [
                        "FEMA National Flood Hazard Layer: property flood-context screening",
                        "Start at https://msc.fema.gov/ and select NFHL GIS services or downloads; official map viewing and available downloads are free.",
                        "Map amendments and effective dates govern currency; use service metadata, bounded geographic queries, and published GIS transfer limits.",
                        "Order a current flood determination when required; coordinates and mapped overlays do not replace transaction-specific insurance requirements.",
                    ],
                    [
                        "U.S. Census Geocoder: address standardization and coordinate comparison",
                        "Use https://geocoding.geo.census.gov/geocoder/locations/onelineaddress with documented benchmark and format parameters; public service access is free.",
                        "Benchmark vintages determine address coverage; batch within published limits, cache repeated addresses, and queue timeouts for later review.",
                        "Compare the assessor parcel map and legal description manually; interpolated coordinates cannot establish the correct collateral parcel.",
                    ],
                    [
                        "FDIC BankFind Suite API: bank identity and status corroboration",
                        "Use https://banks.data.fdic.gov/api/institutions with documented filters and fields; public institution data is available without subscription fees.",
                        "Update timing follows the underlying FDIC dataset; retain extract dates, paginate within current limits, and cache institution identifiers.",
                        "Use https://banks.data.fdic.gov/bankfind-suite/bankfind for manual confirmation; deposit insurance status does not authenticate beneficiary-account ownership.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source contract",
                    "action": "Record access rights, price basis, field definitions, freshness rules, and permitted automation before connecting a source.",
                    "detail": "Assign a source owner and a manual substitute; store credentials outside source files and restrict them to the connector's required permissions.",
                },
                {
                    "step": 2,
                    "title": "Resolve identity before enrichment",
                    "action": "Match county parcel keys and jurisdiction-specific entity identifiers before ordering commercial attributes.",
                    "detail": "Keep uncertain matches in a separate queue and preserve original names, legal descriptions, and the evidence used to resolve each collision.",
                },
                {
                    "step": 3,
                    "title": "Apply bounded retrieval and review",
                    "action": "Fetch under provider-specific budgets, preserve provenance, and route stale or conflicting mandatory fields to a human reviewer.",
                    "detail": "Honor rate-limit responses, reuse permissible cached records, and substitute current official evidence when a closing-critical connector fails.",
                },
                {
                    "step": 4,
                    "title": "Publish a dated deal packet",
                    "action": "Attach resolved identities, source dates, outstanding exceptions, and cost totals to the underwriting file.",
                    "detail": "Separate discovery facts from funding evidence, and require current settlement verification before the packet can support a wire request.",
                },
            ],
        },
        {
            "heading": "3. Buy normalization, then independently verify the settlement chain",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Commercial enrichment earns its place when it reduces manual reconciliation "
                    "without obscuring source limitations. ATTOM can normalize property attributes "
                    "and transaction history; Regrid can supply parcel geometry and identifiers; "
                    "CourtListener can surface available opinions and RECAP materials. Coverage "
                    "and freshness vary by dataset, county, and document contribution, so "
                    "measure each service against a sample of current official records before "
                    "expanding the subscription. Do not assume CourtListener is a complete "
                    "state probate docket or that a commercial ownership field reflects "
                    "yesterday's deed. Require the vendor contract to define permitted "
                    "underwriting use, retention, redistribution, and any restrictions on "
                    "individual-level data. Obtain pricing and quotas for the actual product "
                    "rather than transferring a free viewer's terms to an API subscription. "
                    "At a hypothetical $400 monthly platform charge, saving eight analyst "
                    "hours valued at $40 each yields only $320 of labor value; the subscription "
                    "needs additional measurable benefits to justify its cost. Conversely, "
                    "documented reduction in expensive duplicate searches may close that "
                    "gap. Never justify software by assigning a speculative value to fraud "
                    "it supposedly prevented. Track actual exceptions caught, their supporting "
                    "evidence, and the action taken by the desk."
                ),
                (
                    "Settlement verification requires a different evidence standard from property "
                    "research. Check the relevant state insurance or settlement-agent registry, "
                    "confirm the agent's appointment and authority with the title underwriter, "
                    "and verify bond and applicable coverage directly with the issuing party. "
                    "NMLS Consumer Access helps where the relevant license category participates, "
                    "but an absent listing does not establish an exemption and an active "
                    "listing does not authorize every product. State commercial-purpose "
                    "exemptions, usury ceilings, and escrow licensing rules require a "
                    "product-and-jurisdiction matrix tied to the proposed transaction. Florida "
                    "Statutes section 687.03 illustrates why short-duration fees must be "
                    "analyzed with the actual amount and time outstanding; section 626.8417 "
                    "addresses title insurance agency licensing. For a 24-to-72-hour double "
                    "close, require the settlement agent to confirm unconditional end-buyer "
                    "cash on deposit and the exact release mechanics before sending principal. "
                    "An email screenshot, proof-of-funds letter, or bank availability indicator "
                    "does not establish that condition. Earnest-money lending that requires "
                    "earlier deployment stays outside this release rule unless its structure "
                    "can actually satisfy it. Do not let a discovery play silently relax "
                    "the volume's stated funding discipline."
                ),
                (
                    "Use CertifID or an equivalent contracted verification workflow as an "
                    "additional control, not as a substitute for independent callbacks and "
                    "settlement confirmation. Obtain the callback number from a previously "
                    "verified directory or established relationship, never from the same "
                    "email that supplies changed wire instructions. Verify the receiving "
                    "account, beneficiary, transaction reference, expected amount, and permitted "
                    "release conditions with authorized personnel. Require a second reviewer "
                    "for new beneficiaries and instruction changes, with a durable audit "
                    "record linking the evidence to the payment request. A one-person "
                    "full-time desk can use an authorized contractor as that independent "
                    "reviewer without sharing credentials. Treat 0%-APR corporate credit "
                    "as a separately documented liquidity source: promotional purchase terms "
                    "may exclude cash advances, balance transfers, or escrow-related transactions, "
                    "and fees can destroy the apparent spread. Verify issuer terms, "
                    "available capacity, transfer timing, repayment dates, and permitted use; "
                    "never disguise transaction categories to obtain promotional treatment. "
                    "Automated proof-of-funds generation must reflect verified available "
                    "capacity and an expiration time. If any settlement confirmation is "
                    "conditional, stale, or contradictory, hold the wire and obtain fresh "
                    "evidence rather than shortening the checklist to preserve a closing."
                ),
            ],
            "table": {
                "caption": "Named Directory, Part 3 of 3: Six Commercial and Verification Resources Completing the Eighteen-Source Directory",
                "headers": [
                    "Named source and specific operator purpose",
                    "Exact access method and cost tier",
                    "Refresh latency and rate-limit operating discipline",
                    "Fallback evidence and decisive interpretation limit",
                ],
                "rows": [
                    [
                        "ATTOM Property API: normalized property and transaction attributes",
                        "Obtain a licensed API key through https://api.developer.attomdata.com/; use https://api.gateway.attomdata.com/propertyapi/v1.0.0/ under contracted product pricing.",
                        "County ingestion and purchased dataset determine freshness; inspect record dates, meter calls, and respect the contracted request quota.",
                        "Retrieve recorder and assessor evidence directly when ownership conflicts arise; normalized attributes do not replace a current title commitment.",
                    ],
                    [
                        "Regrid parcel products: parcel geometry and identifier reconciliation",
                        "Evaluate https://app.regrid.com/ and obtain API or bulk access through https://regrid.com/; commercial integration uses the quoted subscription tier.",
                        "Refresh schedules vary by county and product; preserve source vintage and follow contracted API limits or licensed bulk-delivery schedules.",
                        "Use the county GIS service and legal description; visual parcel overlap does not establish ownership or remove boundary disputes.",
                    ],
                    [
                        "CourtListener and RECAP: available litigation documents and opinions",
                        "Use https://www.courtlistener.com/api/rest/v3/ with required authentication; public browsing is free, while API access follows current service tiers.",
                        "Coverage depends on court feeds and contributed documents; honor account throttles and never treat delayed coverage as a clean litigation search.",
                        "Search the originating court or authorized PACER account for federal matters; local probate requires the relevant state court's records.",
                    ],
                    [
                        "NMLS Consumer Access: participating license categories and disciplinary context",
                        "Search https://www.nmlsconsumeraccess.org/ by legal name or NMLS identifier; public manual access is free under posted usage conditions.",
                        "Publication follows regulator and licensee updates; retrieve current records manually and do not bypass access controls or session restrictions.",
                        "Contact the state regulator for product-specific authority; a missing entry does not prove that a commercial lending exemption applies.",
                    ],
                    [
                        "Florida DFS license search: title-agent and agency licensing evidence",
                        "Use https://licenseesearch.fldfs.com/ and select the relevant person or agency search; official public license lookup is free.",
                        "Verify current status immediately before onboarding or material changes; preserve the result and use permitted manual search workflows.",
                        "Confirm appointment with the title underwriter and bond with its issuer; license status alone does not authenticate wire instructions.",
                    ],
                    [
                        "CertifID verification workflow: settlement payment instruction corroboration",
                        "Contract through https://www.certifid.com/ for the supported dashboard or integration; pricing and any coverage terms are quotation-based.",
                        "Run transaction-specific checks when instructions arrive and whenever they change; integration quotas and response commitments follow the contract.",
                        "Use independent callbacks and documented bank or settlement confirmation; platform results do not prove unconditional end-buyer cash is deposited.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before any escrow release",
                "body": "A research packet can be complete while a transaction remains unfundable. Release requires current affirmative evidence for every check below.",
                "items": [
                    "Verify the bonded settlement agent, active authority, applicable appointment, and independently confirmed beneficiary instructions; unresolved discrepancies stop the wire.",
                    "Obtain direct settlement confirmation of unconditional end-buyer cash on deposit, identified transaction allocation, and exact authority to complete both closing legs.",
                    "Confirm the state-specific product classification, applicable lending exemption or license, usury treatment of all charges, and escrow release requirements.",
                    "Reconcile committed liquidity, issuer restrictions where credit is used, repayment timing, and an independently reviewed payoff ledger before authorizing principal movement.",
                ],
            },
        },
        {
            "heading": "4. Instrument the payoff ledger and reconcile the scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the desk around a deal ledger with separate accounts for principal "
                    "advanced, principal returned, earned transactional fees, earned EMD JV "
                    "splits, origination points, provider costs, and unresolved cash differences. "
                    "Principal moving through escrow is neither sales revenue nor owner "
                    "profit. Where the desk acts as an agent, evaluate ASC 606 presentation "
                    "and recognize only the earned operator share of applicable arrangements; "
                    "do not record a partner's share as operator revenue and then subtract "
                    "it twice. The supplied Formula v2.0 cases already define the annual "
                    "revenue basis as earned fees, splits, and points. Preserve those totals "
                    "rather than adding settlement billings or applying an invented retained "
                    "share. Conservative revenue of $120,000 at 30% yields $36,000 owner "
                    "profit and $84,000 of implied total costs. Base revenue of $535,000 "
                    "at 42.5% yields $227,375 and $307,625 of implied total costs. Scaled "
                    "revenue of $950,000 at 55% yields $522,500 and $427,500 of implied "
                    "total costs. Those residual costs include every cost represented by "
                    "the scenario margin; they are not interchangeable with the separate "
                    "$2,000-to-$12,000 monthly operating-expense range. Keep scenario totals "
                    "and actual ledger balances visibly distinct in reporting."
                ),
                (
                    "Use an illustrative fee bridge to test the Base arithmetic without "
                    "pretending the scorecard supplied a transaction mix. One possible "
                    "composition is 120 completed funding events earning $2,000 each, 100 "
                    "earned EMD JV distributions of $1,750 each, and sixty origination "
                    "events earning $2,000 each: $240,000 plus $175,000 plus $120,000 "
                    "equals $535,000. These are distinct fee events with documented "
                    "recognition conditions, not necessarily 280 different properties. "
                    "Where one property generates multiple fees, link them to one master "
                    "deal and test for duplicate recognition. Count an EMD distribution "
                    "only when the desk's share is earned under the arrangement, rather "
                    "than when earnest money is deposited. The bridge describes accounting "
                    "volume, not permission to fund an earlier-stage EMD position that "
                    "fails the release conditions. Capacity also depends on concurrency: "
                    "two overlapping $75,000 advances require $150,000 of deployable "
                    "principal before reserves, exceeding the stated $25,000-to-$100,000 "
                    "startup capital range. A proposed partner line is not available "
                    "capacity until committed and usable. For a $100,000 principal "
                    "exposure earning a $2,000 fee, a complete principal loss consumes "
                    "fifty such fees before expenses. That asymmetry explains why "
                    "verification quality outranks raw lead volume."
                ),
                (
                    "A small desk can implement the evidence store with SQLite, encrypted "
                    "document storage, operating-system credential storage, and a scheduled "
                    "Python job using standard HTTP libraries. SQLite transactions should "
                    "make deal-state updates atomic; idempotency keys should prevent duplicate "
                    "provider orders and repeated wire-request creation. Keep payment execution "
                    "outside the discovery worker. A reconciliation job compares expected "
                    "principal, actual return, earned fees, and settlement statements using "
                    "decimal currency arithmetic rather than binary floating-point totals. "
                    "Use structured logs with deal identifiers, response status, elapsed "
                    "time, and payload hashes, but redact account numbers, credentials, "
                    "and unnecessary personal details. Test backup restoration, not merely "
                    "backup creation, and restrict contractor access to assigned files. "
                    "Track source age, ambiguous matches, paid-call duplication, verification "
                    "exceptions, closing delays, and cash differences as operational metrics. "
                    "The Conservative and Base teams each contain one full-time operator "
                    "and two contractors; Scaled uses two full-time operators and three "
                    "contractors. Assign the extra capacity to independent review and "
                    "exception resolution before increasing simultaneous principal exposure. "
                    "End each business day with all open advances tied to a named "
                    "settlement contact and a documented next action. A profitable dashboard "
                    "cannot compensate for an unexplained principal balance."
                ),
            ],
            "table": {
                "caption": "Eight Diagnostic Controls: Tooling, Failure Evidence, and Operator Responses",
                "headers": [
                    "Diagnostic control and concrete implementation target",
                    "Evidence inspected by the responsible operator",
                    "Failure interpretation and immediate operating response",
                    "Unit economics or canonical reconciliation check",
                ],
                "rows": [
                    [
                        "Source freshness monitor using scheduled Python retrieval jobs",
                        "Compare retrieved time, source effective date, last success, and the deal's required verification timing.",
                        "Mark stale sources visibly and obtain current official evidence; suspend dependent decisions rather than silently reusing old results.",
                        "Measure stale-file reviews separately from eligible reviews so apparent acquisition cost does not improve through excluded exceptions.",
                    ],
                    [
                        "Identity collision queue backed by SQLite match records",
                        "Inspect county parcel keys, organizing jurisdictions, filing numbers, original names, and conflicting legal descriptions.",
                        "Require manual resolution before enrichment purchases or underwriting; preserve both candidates rather than merging uncertain identities.",
                        "At $600 across thirty eligible reviews, research cost is $20 per review, before separately excluded expenses.",
                    ],
                    [
                        "Provider request meter with retries and idempotency controls",
                        "Inspect request identifiers, purchased product, charge amount, response status, retry cause, and cached-record eligibility.",
                        "Stop repeat purchases for identical immutable documents; investigate connector bugs when retries create fresh billable orders.",
                        "Twelve $5 lookups plus six $15 document packages equal $150 of illustrative variable research charges.",
                    ],
                    [
                        "Wire instruction comparison with independent second review",
                        "Compare beneficiary identity, account details, callback evidence, instruction version, and the exact requested payment amount.",
                        "Hold any changed or inconsistent instruction until independently reverified; retain the superseded instruction without allowing execution.",
                        "A $100,000 principal loss consumes fifty $2,000 earned fees before any operating costs are recovered.",
                    ],
                    [
                        "Principal concurrency monitor linked to committed liquidity",
                        "Inspect outstanding advances, scheduled releases, expected repayments, reserves, and actually usable funding commitments.",
                        "Defer overlapping advances when available committed liquidity is insufficient; projected repayments cannot serve as current cash.",
                        "Two simultaneous $75,000 advances require $150,000 before reserves, above the stated maximum startup capital.",
                    ],
                    [
                        "Decimal payoff reconciliation with settlement statement matching",
                        "Match principal returned, separately earned fees, partner allocations, charges, and unresolved differences by master deal.",
                        "Assign every unexplained cash difference to an operator and settlement contact; do not classify missing principal as an expense shortcut.",
                        "The illustrative Base bridge totals $240,000 plus $175,000 plus $120,000, producing exactly $535,000 fee revenue.",
                    ],
                    [
                        "Scenario margin check against Formula v2.0 totals",
                        "Compare recognized annual fee revenue, total scenario costs, owner profit, and staffing against the supplied canonical cases.",
                        "Reject reports that add escrow principal to revenue, double-deduct partner shares, or substitute monthly overhead for total costs.",
                        "Conservative profit is $36,000; Base profit is $227,375; Scaled profit is $522,500 under their exact stated margins.",
                    ],
                    [
                        "Recovery drill using restricted backups and sample restoration",
                        "Restore a selected deal packet, ledger snapshot, source hashes, and review history into an isolated test location.",
                        "Repair missing evidence or access failures before expanding volume; keep restored sensitive records restricted and remove test copies afterward.",
                        "Preserve review capacity within 1 FT plus 2 C, then 2 FT plus 3 C at scale.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Public records find the situation; independently verified escrow evidence earns the right to move principal.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Register the eighteen directory sources with jurisdiction coverage, access rights, current pricing, source dates, request limits, and a documented manual fallback.",
        "Create parcel and entity identity keys, preserve raw evidence hashes, and isolate unresolved matches before purchasing commercial enrichment.",
        "Implement public_record_api_intelligence with provider-specific request budgets and scheduled bulk public-record exports when live access becomes unsuitable.",
        "Build a state-by-product matrix covering commercial-purpose exemptions, usury treatment, required licenses, settlement authority, and permissible credit-source use.",
        "Require independently verified beneficiary instructions and unconditional end-buyer cash on deposit with a bonded settlement agent before releasing principal.",
        "Reconcile principal separately from earned fees and reproduce the exact $36,000, $227,375, and $522,500 annual owner-profit cases before publishing the dashboard.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "Document a permissible purpose before obtaining consumer-report products; ordinary public-record discovery is not an automatic authorization to pull those reports.",
        },
        {
            "title": "UCC 9-307 — Location of debtor",
            "url": "https://www.law.cornell.edu/ucc/9/9-307",
            "relevance": "Determine the appropriate debtor jurisdiction before ordering UCC searches, then verify the governing state's enacted version and transaction-specific rules.",
        },
        {
            "title": "Florida Statutes 687.03 — Unlawful rates of interest",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0687/Sections/0687.03.html",
            "relevance": "Analyze short-duration charges against the applicable state interest rules, exceptions, amount, and actual time outstanding rather than assuming a business-purpose label resolves usury treatment.",
        },
        {
            "title": "Florida Statutes 626.8417 — Title insurance agency licensing",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0626/Sections/0626.8417.html",
            "relevance": "Use the applicable agency licensing requirements when verifying a Florida title counterparty; independently confirm appointments, coverage, and payment instructions.",
        },
        {
            "title": "16 CFR 314.4 — Elements of an information security program",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314/section-314.4",
            "relevance": "For a covered institution, map retained customer information to required safeguards, access controls, service-provider oversight, and applicable testing obligations.",
        },
        {
            "title": "12 CFR 229.19 — Miscellaneous funds-availability provisions",
            "url": "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-229/subpart-B/section-229.19",
            "relevance": "Distinguish bank funds-availability treatment from separate collection, settlement, and escrow release conditions; an available balance alone does not prove unconditional end-buyer cash.",
        },
        {
            "title": "31 CFR 501.603 — Reports on blocked and unblocked property",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-501/section-501.603",
            "relevance": "If property is blocked under an applicable sanctions program, follow the relevant reporting requirements; this provision does not replace analysis of the substantive sanctions restriction.",
        },
        {
            "title": "5 U.S.C. 552 — Federal public information and agency records",
            "url": "https://www.law.cornell.edu/uscode/text/5/552",
            "relevance": "Use federal FOIA for covered federal agency records and the appropriate state public-record law for county exports; neither process implies unrestricted access to protected material.",
        },
    ],
}
