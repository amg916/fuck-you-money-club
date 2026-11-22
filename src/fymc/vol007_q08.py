from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small unclaimed property recovery desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "Treasury Portals, Corporate Successor Evidence, SEC APIs, Evidence-Preserving Pipelines, and IRC § 6418 Origination Controls",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #04 with an 89/100 "
        "Money-to-Manpower Score. Its information advantage comes from connecting "
        "treasury property records to defensible ownership evidence, not buying "
        "larger contact lists. This chapter organizes 12 mapped plays: eleven "
        "chapter-local recovery workflows and the specified transferable-tax-credit "
        "adjacency. An eighteen-source directory separates searchable portals from "
        "documented APIs, while operating matrices translate matches into authorized "
        "claims, controlled enrichment spend, and auditable fee collections. The "
        "canonical annual owner-profit cases remain $15,000 Conservative, $95,625 "
        "Base, and $225,000 Scaled; recovered client assets never become desk revenue. "
        "Build around source provenance, identity resolution, claim-status tracking, "
        "state-specific finder rules, and direct-claim disclosure. Treat tax-credit "
        "origination as a separately qualified workflow with direct eligible transfers "
        "and buyer-funded escrow, not speculative credit inventory."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; excludes recovered client assets",
            "note": "25% net margin; $15,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees; excludes recovered client assets",
            "note": "37.5% net margin; $95,625 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees; excludes recovered client assets",
            "note": "50% net margin; $225,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an eighteen-source directory around custody, ownership, and permitted access",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the custodian, not the enrichment vendor. State treasury "
                    "systems establish that a property record exists; they do not establish "
                    "that your prospect owns it, that the displayed amount is complete, or "
                    "that a finder may charge immediately. Create one source register with "
                    "jurisdiction, official landing URL, documented access method, retrieval "
                    "timestamp, publication date when available, and the current finder "
                    "rule reference. MissingMoney provides useful participating-state "
                    "discovery, while California, Texas, Florida, and New York supply "
                    "jurisdiction-specific search and claim instructions. Coverage differs, "
                    "so a missing aggregator result never closes a lead. Corporate "
                    "uncashed warrants need an additional classification: some remain "
                    "with the issuing agency before eventual treasury custody. Record "
                    "the warrant issuer, issue date, stale-date procedure, and replacement "
                    "route before calling the item escheated property. The directory "
                    "below gives operating check intervals rather than promising publisher "
                    "refresh schedules. Check terms and current official links at "
                    "onboarding, because portal vendors and export permissions change. "
                    "A browser search box is not permission to replay private endpoints "
                    "or bypass interactive access controls. Prefer an agency-approved "
                    "extract when recurring manual search becomes the bottleneck."
                ),
                (
                    "Use entity evidence to turn an attractive name into a defensible "
                    "claimant chain. SEC submissions identify registrants and filing "
                    "histories; secretary-of-state records establish entity status and "
                    "filed name changes; merger documents connect predecessor names "
                    "to surviving corporations. None independently proves entitlement "
                    "to a particular treasury item. A dissolved company may require "
                    "a winding-up representative, and an asset purchase may exclude "
                    "cash receivables that a stock acquisition would leave inside the "
                    "same legal entity. Retrieve the operative document rather than "
                    "inferring succession from matching websites. For an estate, use "
                    "the relevant county court's authorized records channel and obtain "
                    "the appointment instrument needed by the custodian; a death notice "
                    "does not appoint a representative. For a warrant, confirm the "
                    "payee's original legal identity with the issuing agency before "
                    "building a treasury claim. Store public business evidence "
                    "separately from owner identity documents, with narrower access "
                    "for the latter. PACER, county clerks, and state filing offices "
                    "are fallback evidence sources, not universal entitlement APIs. "
                    "Measure evidence completeness by missing required instruments, "
                    "not by the number of commercial databases queried during research."
                ),
                (
                    "The directory deliberately mixes official sources, commercial APIs, "
                    "and diagnostic tools without pretending they have equivalent "
                    "authority. OpenCorporates can accelerate entity discovery, "
                    "Melissa can normalize an address, and Twilio Lookup can describe "
                    "a telephone number; none proves ownership or permission to contact. "
                    "Use commercial results as leads back to authoritative records. "
                    "For sources without published quotas, choose low-volume manual "
                    "research or obtain a written extract arrangement instead of "
                    "inventing a safe requests-per-second number. For documented APIs, "
                    "record the account quota, identify the client where required, "
                    "cache stable responses, and honor throttling responses. Cost "
                    "entries distinguish free public search from paid copies and "
                    "contracted usage; procurement must capture current prices before "
                    "activation. The eleven recovery mappings in this chapter are "
                    "local operating labels: treasury discovery, warrant tracing, "
                    "predecessor resolution, merger succession, estate authority, "
                    "address normalization, contact verification, property deduplication, "
                    "claim packaging, status monitoring, and fee reconciliation. The "
                    "twelfth mapping is the specified transferable-credit adjacency. "
                    "This distinction keeps an incomplete cross-volume roster from "
                    "becoming invented candidate metadata while still giving the "
                    "desk twelve concrete workflows to instrument and evaluate."
                ),
            ],
            "table": {
                "caption": "Eighteen-source access directory: publisher latency differs from desk review cadence",
                "headers": [
                    "Named source and operating purpose",
                    "Exact access method",
                    "Cost tier and purchase control",
                    "Refresh latency and review cadence",
                    "Rate-limit and access hygiene",
                    "Fallback evidence or discovery route",
                ],
                "rows": [
                    [
                        "MissingMoney participating-state property discovery across multiple jurisdictions",
                        "Browser search through https://www.missingmoney.com/ and linked state destinations",
                        "Public search is free; separately budget internal research labor",
                        "State submission timing varies; recheck active prospects monthly",
                        "Use intended searches; obtain permission before bulk extraction",
                        "Search the relevant state treasury's own property portal",
                    ],
                    [
                        "California State Controller property custody and claim requirements",
                        "Official browser search at https://ucpi.sco.ca.gov/ plus Controller instructions",
                        "Public search is free; document procurement may cost extra",
                        "Custodian updates control availability; recheck shortlisted records before outreach",
                        "Use public interface; request permitted extracts for recurring volume",
                        "Contact Controller unclaimed property staff through official published channels",
                    ],
                    [
                        "Texas Comptroller ClaimItTexas property search and owner claims",
                        "Official browser workflow at https://www.claimittexas.gov/ for property research",
                        "Public search is free; track claimant document expenses separately",
                        "Publication timing is custodian-controlled; review active leads monthly",
                        "Respect interactive controls; do not replay undocumented internal endpoints",
                        "Use Texas Comptroller unclaimed property assistance and published instructions",
                    ],
                    [
                        "Florida Department of Financial Services property and representative requirements",
                        "Official portal https://www.fltreasurehunt.gov/ with linked claimant guidance pages",
                        "Public search is free; representative qualification costs remain separate",
                        "Portal changes follow agency operations; revalidate requirements before contracting",
                        "Use permitted searches and current agency extract procedures only",
                        "Contact Florida Bureau of Unclaimed Property through official channels",
                    ],
                    [
                        "New York Comptroller unclaimed funds discovery and claims",
                        "Start at https://www.osc.ny.gov/unclaimed-funds and follow official search links",
                        "Public search is free; certified supporting records may cost",
                        "Agency publication timing varies; recheck each lead before engagement",
                        "Prefer supported portal navigation over guessed search API calls",
                        "Use Comptroller owner assistance and official claimant documentation instructions",
                    ],
                    [
                        "State and county warrant registers for pre-escheat receivables",
                        "Navigate issuing controller or treasurer website to outstanding-warrant publications",
                        "Published lists are often free; requested extracts may incur charges",
                        "Use each list's stated issue date; review new releases",
                        "Download published files once; avoid repeated full-file retrieval loops",
                        "Request warrant status directly from the issuing accounts-payable office",
                    ],
                    [
                        "California Secretary of State filed business identity evidence",
                        "Browser search at https://bizfileonline.sos.ca.gov/search/business for entity filing records",
                        "Search access is free; ordered certified records carry fees",
                        "Filing visibility follows processing; refresh before asserting successor authority",
                        "Use public interface and permitted document-ordering channels without bypasses",
                        "Order authoritative filing copies directly from the filing office",
                    ],
                    [
                        "SEC EDGAR registrant identity and corporate transaction filings",
                        "Use https://www.sec.gov/edgar/search/ and https://data.sec.gov/submissions/CIK##########.json with padded CIK",
                        "Public filings and documented endpoints are available without subscription",
                        "Submissions update with filings; poll only relevant registrants daily",
                        "Identify your client and stay below current SEC access ceilings",
                        "Retrieve the same filing through its official EDGAR accession page",
                    ],
                    [
                        "PACER federal court records for bankruptcy and authority evidence",
                        "Search authorized accounts through https://pacer.uscourts.gov/ and court-specific systems",
                        "Metered access follows current judiciary fee schedules and exemptions",
                        "Dockets change when filed; check relevant proceedings before submission",
                        "Use authorized account workflows and court-specific access restrictions consistently",
                        "Request documents from the court clerk through published procedures",
                    ],
                    [
                        "County probate courts for estate representative appointment evidence",
                        "Use the decedent's relevant court website or clerk record-request process",
                        "Search and copy charges vary by the specific court",
                        "Appointment changes follow docket events; refresh authority before filing",
                        "Follow court access rules; restricted case files remain restricted",
                        "Obtain certified appointment instruments from the authorized estate representative",
                    ],
                    [
                        "OpenCorporates cross-jurisdiction business discovery and historical name leads",
                        "Documented commercial API through https://api.opencorporates.com/ using licensed credentials",
                        "Commercial use follows contracted licensing and current account pricing",
                        "Coverage follows upstream sources; inspect each record's retrieval metadata",
                        "Honor licensed quotas, attribution conditions, caching terms, and restrictions",
                        "Verify consequential facts with the originating official business registry",
                    ],
                    [
                        "Melissa Global Address normalization for claimant address comparison",
                        "Use documented product access through https://docs.melissa.com/ and subscribed endpoint",
                        "Evaluation allowances and paid usage depend on the purchased plan",
                        "Address reference vintages vary; process only changed candidate addresses",
                        "Apply account quotas and prohibit unnecessary identity-document payload submission",
                        "Compare owner-provided evidence against historical addresses in official records",
                    ],
                    [
                        "Twilio Lookup telephone metadata for narrowly scoped contact checks",
                        "Documented endpoint https://lookups.twilio.com/v2/PhoneNumbers/{PhoneNumber} with authorized account credentials",
                        "Charges depend on requested data packages and current pricing",
                        "Lookup returns request-time information; it does not prove ownership",
                        "Limit requested fields and honor account throttling and use restrictions",
                        "Use the claimant's independently confirmed business contact channel instead",
                    ],
                    [
                        "DOE energy project publications for adjacent developer discovery",
                        "Browse official publications and project resources at https://www.energy.gov/",
                        "Public publications are free; extraction and interpretation consume labor",
                        "Release dates vary by program; review relevant releases monthly",
                        "Use published downloads and documented interfaces rather than hidden endpoints",
                        "Verify interconnection status with the actual utility or system operator",
                    ],
                    [
                        "EPA RE-Powering resources for adjacent contaminated-land project leads",
                        "Browse https://www.epa.gov/re-powering and its published maps and datasets",
                        "Public resources are free; project verification requires separate diligence",
                        "Dataset vintages differ; retain publication dates with each lead",
                        "Download permitted datasets once and honor endpoint-specific service limits",
                        "Verify parcel and project facts with local agencies and developers",
                    ],
                    [
                        "PJM interconnection queue records for regional energy development leads",
                        "Navigate https://www.pjm.com/ to Services and Requests then interconnection queues",
                        "Public queue materials are free where published by PJM",
                        "Queue status changes by project; review live prospects weekly",
                        "Use published exports and permitted interfaces within current access terms",
                        "Request supporting queue documents directly from the project developer",
                    ],
                    [
                        "Georgia film office and revenue guidance for state-credit origination",
                        "Use https://georgia.org/film and https://dor.georgia.gov/film-tax-credit official resources",
                        "Published program guidance is free; qualified transaction review costs extra",
                        "Guidance and certification events drive changes; check before each transaction",
                        "Use public publications; do not infer private certification records exist",
                        "Obtain issued certification and transfer documentation from the credit seller",
                    ],
                    [
                        "National Park Service historic rehabilitation program verification resources",
                        "Browse https://www.nps.gov/subjects/taxincentives/ and linked state preservation offices",
                        "Public program information is free; project document costs vary",
                        "Project determinations follow review; confirm current certification with parties",
                        "Respect publication boundaries and obtain restricted project materials from owners",
                        "Verify state transferability separately with state revenue and preservation offices",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn discovery into a provenance-preserving enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the ingestion layer with Python's urllib.request, csv, json, "
                    "sqlite3, hashlib, and datetime before purchasing an orchestration "
                    "platform. Use only documented API or export access authorized "
                    "for the source; browser-only portals stay in a manual research "
                    "queue. Preserve each permitted source artifact with retrieval "
                    "time, original URL, content hash, parser version, and source "
                    "publication date when supplied. A hash supports change detection "
                    "and integrity checks, not confidentiality. Keep raw artifacts "
                    "separate from normalized records so a parser correction can "
                    "be replayed without silently rewriting evidence. Normalize "
                    "business suffixes, punctuation, whitespace, and address "
                    "components into comparison fields while retaining the original "
                    "strings. Use the custodian's property identifier as the primary "
                    "deduplication anchor when available; otherwise build a composite "
                    "candidate key and flag collisions for review. Two records "
                    "sharing a name and amount can still represent different "
                    "properties. A disappearing search result is not proof of "
                    "payment. Represent it as a source observation requiring "
                    "confirmation. SQLite transactions should commit artifact "
                    "metadata and normalized records together, preventing an "
                    "apparently complete lead from pointing to evidence that was "
                    "never actually saved."
                ),
                (
                    "Run enrichment in a strict waterfall: property existence, entity "
                    "identity, historical address, successor authority, claimant "
                    "contact, then document collection. Spend on the next stage "
                    "only when the prior stage supports a plausible claim. "
                    "Illustratively, reviewing 200 records at three minutes each "
                    "requires ten hours; at a $35 loaded hourly rate, discovery "
                    "costs $350. If twenty records survive, assign a $0.25 budget "
                    "ceiling per initial commercial address check, adding $5 "
                    "rather than enriching all 200. Those are internal planning "
                    "assumptions, not quoted vendor prices. If five prospects "
                    "then require twenty minutes of authority review, another "
                    "$58.33 brings cohort research cost to $413.33 before "
                    "outreach and claim preparation. Stop when expected collectible "
                    "fees cannot cover the remaining workload. Matching scores "
                    "must expose evidence: exact historical address, documented "
                    "predecessor name, official entity identifier, and corroborated "
                    "representative authority. A common surname plus a nearby "
                    "city should never trigger automatic claimant selection. "
                    "Route conflicting names, competing successors, estate "
                    "disputes, and multiple plausible owners into an exception "
                    "queue. The fallback is a direct custodian inquiry or "
                    "additional owner evidence, not more aggressive personal-data "
                    "collection from unrelated commercial sources."
                ),
                (
                    "Keep sensitive claimant documents out of enrichment payloads and "
                    "ordinary CRM notes. Store identification, tax identifiers, "
                    "estate instruments, and bank instructions in a restricted "
                    "document repository with access logs and a defined retention "
                    "schedule. Contractors receive only the records needed for "
                    "their assigned review; the owner handles disputed authority "
                    "and payment instructions. Public availability does not "
                    "erase contractual restrictions or make every personal-data "
                    "product suitable for this purpose. Do not obtain consumer "
                    "reports without a qualifying purpose under 15 U.S.C. "
                    "§ 1681b, or motor-vehicle personal information outside "
                    "18 U.S.C. § 2721's permitted-use framework. Prefer "
                    "business filings and claimant-supplied evidence. Outreach "
                    "should identify the recovery business, explain the "
                    "specific property lead without exposing unnecessary "
                    "personal details, disclose the owner's ability to claim "
                    "directly, and state the proposed fee basis. A commercial "
                    "phone lookup is neither contact permission nor proof "
                    "that the person answering owns the asset. Maintain "
                    "suppression requests across vendors and campaigns. "
                    "Measure false matches, unresolved authority conflicts, "
                    "document rework, and accepted claims by source. Those "
                    "diagnostics reveal whether the waterfall is improving "
                    "decision quality rather than merely producing more "
                    "completed database fields."
                ),
            ],
            "table": {
                "caption": "Eleven chapter-local recovery mappings with measurable work units and evidence fallbacks",
                "headers": [
                    "Mapped recovery workflows",
                    "Concrete work unit and cost assumption",
                    "Evidence required before advancing the record",
                    "Failure mode and practical recovery route",
                ],
                "rows": [
                    [
                        "Treasury discovery and warrant tracing establish the actual custodian",
                        "Two hundred three-minute reviews consume ten research hours",
                        "Retain property identifiers, warrant issuer details, and dated source artifacts",
                        "If custody differs, follow issuer replacement procedures before treasury submission",
                    ],
                    [
                        "Predecessor resolution and merger succession connect historic business names",
                        "Five twenty-minute reviews cost $58.33 at $35 hourly",
                        "Connect filed name changes and operative merger instruments to claimant",
                        "If assets were excluded, obtain transaction schedules before asserting entitlement",
                    ],
                    [
                        "Estate authority establishes who can act for deceased owners",
                        "One thirty-minute authority review costs $17.50 before court charges",
                        "Match current appointment instruments to the custodian's representative requirements",
                        "If authority is contested, pause preparation until court evidence resolves",
                    ],
                    [
                        "Address normalization and contact verification reduce avoidable identity errors",
                        "Twenty checks at an illustrative $0.25 ceiling total $5",
                        "Compare normalized addresses with originals and independently confirmed contact channels",
                        "If multiple people match, seek claimant evidence rather than guessing",
                    ],
                    [
                        "Property deduplication and claim packaging prevent duplicate or incomplete submissions",
                        "Ten fifteen-minute packet reviews require two and one-half hours",
                        "Reconcile unique property references with each required supporting document",
                        "If identifiers collide, preserve separate records until custodian confirmation arrives",
                    ],
                    [
                        "Status monitoring and fee reconciliation connect work to collectible fees",
                        "Twelve five-minute weekly reviews consume one staff hour",
                        "Link official status evidence, owner receipt, fee invoice, and payment",
                        "If status disappears, investigate directly rather than recording assumed recovery",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Spend research time where ownership evidence compounds",
                "body": "A small desk wins by reusing verified evidence without reusing unsupported assumptions.",
                "items": [
                    "Build a predecessor-name graph for each corporate client; search every documented former name, but keep each property's entitlement review separate.",
                    "Save the original warrant publication date and issuer contact; a replacement check route can be faster than waiting for treasury custody.",
                    "Request a custodian's current corporate-document checklist before ordering certified merger records; avoid buying documents the claim will not use.",
                    "Batch permitted status reviews by custodian, then route only changed or overdue items to the owner; never equate portal silence with payment.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and permitted access",
                    "action": "Record the official URL, access method, cost basis, and source-specific restrictions.",
                    "detail": "Assign a custodian and review cadence; use manual research when no authorized automated interface exists.",
                },
                {
                    "step": 2,
                    "title": "Capture and normalize without overwriting evidence",
                    "action": "Save the permitted artifact, compute its hash, and write normalized comparison fields.",
                    "detail": "Retain original names and addresses; commit evidence references and parsed records in one database transaction.",
                },
                {
                    "step": 3,
                    "title": "Resolve identity and representative authority",
                    "action": "Collect authoritative business or estate instruments and document conflicting candidate matches.",
                    "detail": "Permit contact enrichment only after the record passes the defined evidence threshold and expected-fee screen.",
                },
                {
                    "step": 4,
                    "title": "Submit, monitor, and reconcile the fee",
                    "action": "Track authorized claim milestones and link owner receipt to the contractual fee calculation.",
                    "detail": "Recognize earned service fees under the desk's accounting policy; keep client asset values outside operator revenue.",
                },
            ],
        },
        {
            "heading": "3. Instrument the desk against the canonical fee economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Anchor every dashboard to recognized service fees, not the "
                    "face value of property discovered or money returned to "
                    "owners. The canonical Conservative case is $60,000 revenue, "
                    "$45,000 implied total expense, and $15,000 owner net "
                    "profit at 25%. Base is $255,000 revenue, $159,375 "
                    "expense, and $95,625 profit at 37.5%. Scaled is "
                    "$450,000 revenue, $225,000 expense, and $225,000 profit "
                    "at 50%. Conservative and Base each use one full-time "
                    "person plus two contractors; Scaled uses two full-time "
                    "people plus three contractors. These are annual scorecard "
                    "outcomes, not promises that this month's leads will "
                    "produce next month's collections. The $1,500–$8,000 "
                    "monthly operating-spend range does not replace the "
                    "scenario's total implied expense envelope; staffing, "
                    "variable processing, and other modeled costs must "
                    "reconcile inside that envelope. Budget $5,000–$35,000 "
                    "startup capital separately and plan for three to "
                    "twelve months before the first deal. A source "
                    "subscription that accelerates discovery but not "
                    "document acceptance may deepen the cash trough. "
                    "Track committed spend and expected collection dates "
                    "weekly so delayed claims do not force premature "
                    "fee invoices or careless acceptance of weak matches."
                ),
                (
                    "Use an explicitly illustrative ten-percent fee only where "
                    "the applicable state rules, waiting period, registration, "
                    "contract form, and property category permit it. At that "
                    "rate, the Conservative revenue corresponds to $600,000 "
                    "recovered client assets, Base to $2,550,000, and "
                    "Scaled to $4,500,000. Those principal amounts stay "
                    "outside recognized desk revenue. If an average successful "
                    "claim produces $2,000 of collectible fees, the "
                    "Conservative case requires thirty successes annually; "
                    "Base can comprise 127 successes at $2,000 plus "
                    "one at $1,000; Scaled requires 225 successes at "
                    "$2,000. These decompositions explain arithmetic without "
                    "asserting a universal claim-size distribution. For "
                    "prospect screening, a $10,000 property with a "
                    "permitted ten-percent fee and a twenty-percent "
                    "probability of collectible success yields $200 "
                    "expected fees. Subtract $70 research, $40 "
                    "documentation, and $15 communication to leave $75 "
                    "before fixed overhead and delay costs. If the "
                    "property is only $1,000, the same probability "
                    "produces $20 expected fees and fails that cost "
                    "screen. Batch related claims with shared authority "
                    "documents where the custodian permits it, but "
                    "never combine owners or omit property-specific "
                    "evidence merely to improve apparent unit economics."
                ),
                (
                    "Make pipeline diagnostics explain lost time rather than "
                    "decorate a dashboard. Use SQLite integrity checks, "
                    "foreign-key enforcement, unique property constraints, "
                    "and unittest fixtures for parser regressions. A "
                    "saved HTML example should demonstrate what happens "
                    "when a portal returns a maintenance page instead "
                    "of search results. Test missing amount fields, "
                    "multiple owner rows, punctuation changes, and "
                    "withdrawn records without silently converting "
                    "absence into zero value. Structured logs should "
                    "record source, batch, parser version, response "
                    "status, elapsed time, and retry count while "
                    "excluding claimant identifiers and document "
                    "contents. Honor Retry-After where supplied, use "
                    "bounded exponential backoff, and stop repeatedly "
                    "failing jobs instead of hammering a source. "
                    "Alert on abrupt count changes, stale active "
                    "claims, duplicate submissions, and fees without "
                    "supporting recovery evidence. Separate submitted, "
                    "accepted, paid-to-owner, invoiced, collected, and "
                    "recognized-fee milestones; cash collection and "
                    "revenue recognition may occur on different dates. "
                    "Reconcile the fee ledger to payment records and "
                    "the accounting ledger monthly. The owner reviews "
                    "exceptions while contractors process documented "
                    "research tasks. This division protects the "
                    "small-team model because automation reduces "
                    "repetitive observation without delegating disputed "
                    "ownership or payment authority to a matching score."
                ),
            ],
            "table": {
                "caption": "Canonical scorecard reconciliation and production diagnostics for recognized service fees",
                "headers": [
                    "Scenario or operating diagnostic",
                    "Exact arithmetic or measurement definition",
                    "Required accounting or technical evidence",
                    "Operator response when the check fails",
                ],
                "rows": [
                    [
                        "Conservative annual case with one full-time person and two contractors",
                        "$60,000 service revenue minus $45,000 expenses equals $15,000 profit",
                        "Reconcile recognized service invoices and allocated expenses to 25% margin",
                        "Reduce unproductive acquisition spend before expanding paid data subscriptions",
                    ],
                    [
                        "Base annual case with one full-time person and two contractors",
                        "$255,000 service revenue minus $159,375 expenses equals $95,625 profit",
                        "Reconcile recognized service invoices and allocated expenses to 37.5% margin",
                        "Investigate document rework and collection delays before adding more leads",
                    ],
                    [
                        "Scaled annual case with two full-time people and three contractors",
                        "$450,000 service revenue minus $225,000 expenses equals $225,000 profit",
                        "Reconcile recognized service invoices and allocated expenses to 50% margin",
                        "Restore per-person throughput before accepting additional recurring fixed costs",
                    ],
                    [
                        "Illustrative ten-percent fee basis separates assets from operator revenue",
                        "Base client recoveries of $2,550,000 generate $255,000 permitted service fees",
                        "Retain jurisdiction-specific contract terms and itemized owner recovery evidence",
                        "Recalculate asset requirements when permitted fees differ from this assumption",
                    ],
                    [
                        "Source freshness diagnostic measures stale observations rather than assumed payment",
                        "Count active records exceeding their assigned custodian review interval",
                        "Store last successful retrieval and last confirmed claim milestone separately",
                        "Recheck through an authorized channel and escalate unresolved source failures",
                    ],
                    [
                        "Fee realization diagnostic follows collectible outcomes across complete research cohorts",
                        "Divide collected fees by cohort research and processing hours",
                        "Preserve unsuccessful records so abandoned leads remain inside productivity calculations",
                        "Pause sources producing attractive face values but poor collectible fees",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before paid engagement or claim submission",
                "body": "A lead advances only when the desk can show the evidence behind the commercial decision.",
                "items": [
                    "Verify the current jurisdiction-specific finder registration, fee ceiling, timing restriction, and contract requirements; document the owner's direct-claim option.",
                    "Verify the property's actual custodian and claimant chain using official records and current representative authority, not a matching score alone.",
                    "Verify source permissions, vendor purpose restrictions, contractor access, and the minimum personal-data fields needed for the task.",
                    "Verify expected collectible fees exceed remaining work costs and that client principal is excluded from the operator revenue forecast.",
                ],
            },
        },
        {
            "heading": "4. Qualify the transferable-credit adjacency without confusing leads, credits, and fees",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The specified adjacent play is "
                    "transferable_tax_credit_brokerage_syndication, Transferable "
                    "Federal & State Tax Credit Brokerage & Syndication "
                    "(IRA § 6418 / Film / Historic), TRACK_1. "
                    "Reuse the desk's provenance and entity-resolution "
                    "capabilities, not its unclaimed-property fee assumptions. "
                    "DOE and EPA publications can identify projects, "
                    "developers, and contaminated-land opportunities, but "
                    "there is no single universal DOE/EPA interconnection "
                    "queue that establishes transferable credits. Actual "
                    "queue research belongs with ISO, RTO, and utility "
                    "sources such as PJM; queue position does not "
                    "prove construction, placed-in-service status, credit "
                    "amount, or tax eligibility. Georgia and Louisiana "
                    "film offices, state revenue agencies, and historic "
                    "preservation programs provide separate lead channels "
                    "whose certification and transfer rules must be "
                    "examined individually. Federal historic rehabilitation "
                    "credits under IRC § 47 are not automatically "
                    "transferable under § 6418. State historic and "
                    "brownfield programs may have their own transfer "
                    "mechanics. Record the exact credit statute, "
                    "issuing authority, project entity, tax year, "
                    "certification stage, and buyer-use constraints "
                    "before soliciting offers. When the public "
                    "record cannot establish eligibility, request "
                    "seller documentation or discard the lead "
                    "instead of converting a project listing "
                    "into an asserted tax asset."
                ),
                (
                    "The supplied commercial spread assumes origination at "
                    "$0.82–$0.88 per dollar of credit and placement "
                    "at $0.92–$0.96. On $1,000,000 face value, "
                    "those ranges imply $820,000–$880,000 seller "
                    "proceeds and $920,000–$960,000 buyer outlay, "
                    "with a paired gross spread of "
                    "$40,000–$140,000 before insurance, diligence, "
                    "escrow, and intermediary costs. At $0.85 "
                    "and $0.94, the illustrative spread is "
                    "$90,000. These are supplied pricing assumptions, "
                    "not current market quotations or automatically "
                    "recognized broker revenue. Crucially, IRC "
                    "§ 6418(e)(2) prevents a transferee from "
                    "making a subsequent transfer election for "
                    "the acquired credit. Therefore, do not "
                    "implement the federal workflow as the "
                    "desk buying a credit and reselling it. "
                    "Structure a direct eligible transfer "
                    "between the originating taxpayer and "
                    "eligible unrelated buyer, with separately "
                    "documented intermediary compensation and "
                    "transaction expenses. A buyer-funded "
                    "escrow can coordinate that direct "
                    "transfer and disbursements without "
                    "making the desk an intermediate "
                    "credit owner. Corporate and high-net-worth "
                    "buyers still require tax-capacity "
                    "analysis; passive-activity restrictions "
                    "can materially constrain an individual's "
                    "ability to use purchased credits. "
                    "For state credits, verify whether "
                    "resale is permitted rather than "
                    "importing federal mechanics or pricing."
                ),
                (
                    "The risk fallback is strict: never hold unhedged "
                    "credit inventory or advance the seller's proceeds "
                    "from the recovery desk's operating cash. "
                    "Require buyer-funded escrow, synchronized "
                    "document delivery, and non-cancelable tax-credit "
                    "insurance as the specified play's execution "
                    "condition, while examining the actual policy's "
                    "exclusions, limits, retention, representations, "
                    "and claim procedures. Non-cancelable wording "
                    "does not erase fraud exclusions or "
                    "establish coverage for every recapture "
                    "event. If suitable coverage or an "
                    "eligible funded buyer cannot be secured, "
                    "decline execution or remain a disclosed "
                    "origination-only intermediary without "
                    "principal exposure. For federal credits, "
                    "verify required pre-filing registration, "
                    "transfer-election documentation, cash "
                    "consideration, and the seller's "
                    "supporting credit calculation under "
                    "the applicable regulations. Keep "
                    "credit face value, seller proceeds, "
                    "buyer outlay, escrow balances, and "
                    "earned intermediary compensation in "
                    "distinct ledger fields. None of "
                    "this illustrative adjacency changes "
                    "Volume 007's $60,000, $255,000, "
                    "and $450,000 canonical service-revenue "
                    "cases. Launch it only with "
                    "separate workflow ownership and "
                    "transaction expertise. The transferable "
                    "skill is disciplined evidence handling; "
                    "the dangerous assumption is that "
                    "finding a public project creates "
                    "a freely tradable asset or "
                    "an immediately collectible brokerage fee."
                ),
            ],
            "table": {
                "caption": "Mapped TRACK_1 credit-origination mechanics: direct transfers, conditional spreads, and bounded exposure",
                "headers": [
                    "Source or transaction workstream",
                    "Concrete unit math or eligibility test",
                    "Required evidence before transaction execution",
                    "Risk fallback and accounting treatment",
                ],
                "rows": [
                    [
                        "DOE and EPA discovery followed by actual interconnection-source verification",
                        "Twenty project leads at fifteen minutes require five research hours",
                        "Verify project entity, queue status, technology, and specific credit pathway",
                        "Discard unsupported eligibility claims rather than valuing every queued project",
                    ],
                    [
                        "Georgia and Louisiana film-credit sourcing through separate state programs",
                        "Evaluate each issued credit against its own transfer and use rules",
                        "Obtain seller certifications, revenue-agency requirements, and remaining transfer eligibility",
                        "Decline execution when certification or lawful transfer mechanics remain unresolved",
                    ],
                    [
                        "Historic rehabilitation and brownfield sourcing through program-specific official records",
                        "Do not treat federal § 47 credits as § 6418 inventory",
                        "Identify the exact state statute and transferable credit instrument",
                        "Use origination-only services when the proposed instrument cannot transfer",
                    ],
                    [
                        "Supplied acquisition and placement ranges applied to one million face value",
                        "$820,000–$880,000 seller proceeds versus $920,000–$960,000 buyer outlay implies $40,000–$140,000 spread",
                        "Document paired executable terms, transaction costs, and separately earned compensation",
                        "Recognize only earned operator compensation, never the credit face value",
                    ],
                    [
                        "Federal direct transfer with simultaneous buyer-funded escrow settlement",
                        "$850,000 seller proceeds and $940,000 buyer outlay imply $90,000 before costs",
                        "Allocate the difference through lawful documented fees and transaction expenses",
                        "Avoid desk ownership because federal acquired credits cannot transfer again",
                    ],
                    [
                        "Insurance and buyer-use diligence before any transaction commitment",
                        "Stress-test proceeds after premium, retention, diligence, and escrow expenses",
                        "Confirm coverage terms, buyer tax capacity, registration, and election documentation",
                        "Decline principal exposure when coverage or committed buyer funding fails",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The edge is not finding a name in a database; it is proving the right claimant, the right authority, and the right fee.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create the eighteen-source register with official URLs, permitted access methods, current pricing, review intervals, and fallback contacts.",
        "Implement artifact hashing, original-field retention, property deduplication, and transaction-safe evidence references in SQLite.",
        "Run a two-hundred-record pilot and measure research cost, identity exceptions, accepted claims, and eventual collectible fees by source.",
        "Document state finder requirements and direct-claim disclosure before contracting; verify current representative authority before submission.",
        "Reconcile the three annual scenarios to recognized service fees, implied total expenses, owner profit, and the exact staffing assumptions.",
        "Keep transferable-credit origination separate; require verified eligibility, direct federal transfers, buyer-funded escrow, suitable insurance, and no desk inventory exposure.",
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure § 1582 — Agreements to locate or recover unclaimed property",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.",
            "relevance": "Check the current timing restrictions, compensation limits, and agreement requirements before offering California recovery services.",
        },
        {
            "title": "Florida Statutes § 717.135 — Recovery agreements and purchase agreements",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0717/Sections/0717.135.html",
            "relevance": "Use the current statutory agreement and compensation requirements when designing Florida recovery contracts and document workflows.",
        },
        {
            "title": "15 U.S.C. § 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "Do not treat unclaimed-property prospecting as an automatic permissible purpose for obtaining consumer reports.",
        },
        {
            "title": "18 U.S.C. § 2721 — Restrictions on motor vehicle personal information",
            "url": "https://www.law.cornell.edu/uscode/text/18/2721",
            "relevance": "Evaluate permitted-use restrictions before accessing motor-vehicle personal information for identity or address research.",
        },
        {
            "title": "26 U.S.C. § 6418 — Transfer of certain credits",
            "url": "https://www.law.cornell.edu/uscode/text/26/6418",
            "relevance": "Establish eligible credit transfers, cash consideration, unrelated-party requirements, and the prohibition on subsequent transfer elections.",
        },
        {
            "title": "26 CFR § 1.6418-2 — Rules for making transfer elections",
            "url": "https://www.ecfr.gov/current/title-26/section-1.6418-2",
            "relevance": "Build the federal transfer workflow around required election mechanics and supporting transaction documentation.",
        },
        {
            "title": "26 CFR § 1.6418-4 — Pre-filing registration requirements",
            "url": "https://www.ecfr.gov/current/title-26/section-1.6418-4",
            "relevance": "Verify required registration before treating a federal transfer as executable; registration alone does not prove substantive eligibility.",
        },
        {
            "title": "26 U.S.C. § 469 — Passive activity losses and credits limited",
            "url": "https://www.law.cornell.edu/uscode/text/26/469",
            "relevance": "Assess whether a prospective buyer can actually use purchased credits, particularly when individuals face passive-activity limitations.",
        },
        {
            "title": "26 U.S.C. § 47 — Rehabilitation credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/47",
            "relevance": "Distinguish federal rehabilitation credits from eligible § 6418 credits and from separately transferable state historic incentives.",
        },
    ],
}
