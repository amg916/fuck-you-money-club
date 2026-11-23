from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small customs duty drawback, tariff refund & antitrust claim recovery desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "ACE Evidence, HTS Versioning, Liquidation Calendars, Court Dockets and Authorized Spend Feeds Under 19 U.S.C. §§ 1313 and 1514",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #44, ranked #03 of 49 with a 95/100 Money-to-Manpower Score, "
        "wins through evidence quality rather than indiscriminate lead volume. This "
        "chapter maps 12 operational plays across drawback, tariff refunds, settled "
        "antitrust distributions and authorized purchasing-group spend recovery. "
        "The directory separates public discovery from permissioned ACE records, "
        "commercial manifests and claimant-owned transaction evidence. Conservative, "
        "Base and Scaled annual owner profits are $35,200, $231,750 and $533,600, "
        "respectively; recognized revenue consists of earned operator fees, never "
        "importer refund principal or settlement pools. Build a versioned source "
        "registry, line-level evidence joins and deadline-first work queues. Route "
        "formal customs filings through licensed brokers or trade counsel, preserve "
        "court-specific claimant disclosures, and release invoices only against "
        "documented contractual earning events."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned contingency-fee revenue; excludes client recoveries",
            "note": "32% net margin; $35,200 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$515,000",
            "context": "Annual earned contingency-fee revenue; excludes client recoveries",
            "note": "45.0% net margin; $231,750 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$920,000",
            "context": "Annual earned contingency-fee revenue; excludes client recoveries",
            "note": "58% net margin; $533,600 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Separate public discovery from permissioned proof",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a source registry, not a scraper. Public manifests, tariff "
                    "schedules and court dockets reveal possible opportunities; they do not "
                    "establish ownership, eligibility or collectible value. This desk maps "
                    "12 operational plays: manifest prospecting, HTS substitution screening, "
                    "direct-identification tracing, export reconciliation, drawback packet "
                    "assembly, liquidation monitoring, Post-Summary Correction triage, protest "
                    "routing, settlement eligibility screening, accounts-payable evidence "
                    "packaging, distribution reconciliation and authorized GPO shared-savings "
                    "recovery. These are working mappings, not twelve independently verified "
                    "income streams. Record each source's owner, access agreement, permitted "
                    "uses, retrieval time, source-effective date, document hash and responsible "
                    "reviewer. A Panjiva consignee match creates a research task, while an "
                    "authorized ACE entry line and commercial invoice support an actual "
                    "customs analysis. A settlement announcement creates a monitoring task, "
                    "while the operative court order and administrator instructions establish "
                    "claim requirements. Keep public discovery records outside client evidence "
                    "folders until identity and authorization are resolved. Retain original "
                    "downloads alongside parsed records so later corrections remain explainable. "
                    "The directory below specifies desk polling targets separately from source "
                    "publication timing; a daily poll cannot make a delayed upstream feed "
                    "current. Assign every unresolved source limitation to a named work queue "
                    "rather than converting it into an optimistic recovery estimate."
                ),
                (
                    "Use an enrichment waterfall that becomes more expensive only when "
                    "evidence improves. First, identify the legal entity through its own "
                    "website, secretary-of-state records and, for reporting companies, SEC "
                    "filings. Second, inspect ImportGenius or Panjiva shipment records under "
                    "the purchased license; ocean-manifest visibility does not cover every "
                    "transport mode, confidential shipment or importer relationship. Third, "
                    "request a narrow client-authorized ACE extract, broker statement and "
                    "sample export packet. Fourth, obtain complete transaction histories only "
                    "after the broker confirms a plausible statutory route. Illustratively, "
                    "screening 100 entities at four minutes each consumes 6.7 analyst hours; "
                    "reviewing 20 authorized samples at 30 minutes adds ten hours. At a "
                    "planning rate of $45 per hour, that waterfall costs about $750 before "
                    "commercial data charges. Those are workload assumptions, not vendor "
                    "prices or expected conversion rates. Reject a name-only join when two "
                    "subsidiaries share a brand. Require legal name, address history and a "
                    "client-confirmed account or importer identifier. For settlement work, "
                    "extend the identity graph to predecessor entities and acquired purchasing "
                    "accounts, but obtain evidence of claim ownership before consolidation. "
                    "A failed identity match returns to manual review; it never becomes a "
                    "fabricated tax identifier or an inferred claimant authorization."
                ),
                (
                    "Treat retrieval engineering as an evidence-control function. Prefer "
                    "documented APIs and authorized exports over browser automation, and "
                    "never circumvent authentication, access restrictions or a provider's "
                    "download controls. Store a per-host request budget, honor Retry-After, "
                    "use exponential backoff with jitter and cache unchanged resources using "
                    "ETag or Last-Modified where supported. The SEC ceiling is ten requests "
                    "per second across the requester; a two-request-per-second desk cap leaves "
                    "headroom but does not replace current access guidance. For sources "
                    "without published quotas, begin with single-request concurrency and a "
                    "five-second interval, then obtain permission before increasing throughput. "
                    "A successful HTTP response does not prove completeness: compare row "
                    "counts, reporting periods and source totals before accepting a refresh. "
                    "Record whether latency measures publication delay, retrieval delay or "
                    "analyst review delay. When a feed fails, preserve the last verified "
                    "snapshot, flag its age and route deadline-sensitive matters to the "
                    "broker or administrator directly. Do not silently substitute a secondary "
                    "database for an operative tariff schedule or court order. Keep encrypted "
                    "client evidence separate from public caches, restrict access by matter, "
                    "and remove credentials from logs. Every directory entry needs an owner "
                    "who can explain both its commercial terms and its evidentiary limits."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Cost, Refresh Discipline and Evidence Fallbacks",
                "headers": [
                    "Named source and exact access route",
                    "Cost tier and permission boundary",
                    "Refresh latency and request discipline",
                    "Operator use and fallback evidence",
                ],
                "rows": [
                    [
                        "CBP ACE Secure Data Portal; enter through ace.cbp.gov using an approved organizational account.",
                        "Government portal access carries no data subscription; broker extraction and implementation services may be separately billed.",
                        "Request authorized reports each business day; underlying report availability varies, so retain extraction and coverage timestamps.",
                        "Obtain importer-authorized entry detail; fall back to broker-provided entry summaries, payment records and reconciliation extracts.",
                    ],
                    [
                        "CBP Cargo Systems Messaging Service; use cbp.gov/trade/automated/cargo-systems-messaging-service and subscribe to relevant email notices.",
                        "Public notices and email subscriptions are free; they disclose system guidance rather than confidential importer transactions.",
                        "Read alerts on arrival and review the archive daily; deduplicate message identifiers instead of repeatedly downloading attachments.",
                        "Track operational changes and filing interruptions; confirm material interpretations with the cited CBP publication and responsible broker.",
                    ],
                    [
                        "USITC Harmonized Tariff Schedule; search hts.usitc.gov and retain the applicable revision's downloadable schedule.",
                        "Public browsing and published downloads are free; classification analysis still requires product specifications and qualified review.",
                        "Check revision postings each business day; download each changed release once and cache its effective-date metadata.",
                        "Resolve historical tariff provisions; fall back to archived official editions and controlling legal modifications.",
                    ],
                    [
                        "USITC DataWeb; query dataweb.usitc.gov through its supported interface and export authorized aggregate trade tables.",
                        "Public trade statistics are free with site registration where required; aggregates do not identify a client's paid duties.",
                        "Refresh when monthly trade releases publish; reuse saved queries and exports rather than running repetitive bulk searches.",
                        "Prioritize product-country corridors; fall back to Census trade releases, never aggregate estimates for individual refund calculations.",
                    ],
                    [
                        "CBP CROSS rulings database; search rulings.cbp.gov by tariff provision, product description and ruling identifier.",
                        "Public ruling searches are free; published facts must match the client's merchandise before supporting an analysis.",
                        "Review relevant searches weekly and before filing; use sequential queries because a general bulk API entitlement is absent.",
                        "Find classification reasoning and revocations; fall back to official Customs Bulletin publications and broker legal research.",
                    ],
                    [
                        "Federal Register API; request federalregister.gov/api/v1/documents.json with documented filters for relevant agencies and tariff actions.",
                        "Public API access is free; retain document identifiers and links to official published text.",
                        "Poll filtered results daily with cached responses; honor throttling signals and avoid repeatedly requesting unchanged document pages.",
                        "Track effective dates and amendments; use GovInfo's official edition when authoritative published text is required.",
                    ],
                    [
                        "CBP official notices of liquidation; navigate from cbp.gov to the official liquidation notices service.",
                        "Public notice access is free; importer-specific interpretation and reconciliation remain authorized broker work.",
                        "Inspect new notices each business day; record actual liquidation dates rather than treating retrieval time as the deadline trigger.",
                        "Cross-check entry liquidation events; fall back to authorized ACE records and direct broker confirmation of discrepancies.",
                    ],
                    [
                        "Regulations.gov API; obtain an API key and use api.regulations.gov/v4/documents with documented docket filters.",
                        "Public API access uses the key's assigned quota; private comments or unavailable attachments cannot be presumed accessible.",
                        "Check relevant dockets daily; budget against the issued quota, cache attachments and stop on access denials.",
                        "Monitor agency dockets and supporting documents; fall back to the docket website and linked official Federal Register notices.",
                    ],
                    [
                        "PACER Case Locator and court CM/ECF; use pcl.uscourts.gov to locate the case, then its court docket.",
                        "Ordinary electronic access is generally $0.10 per page under PACER's fee schedule; caps, exemptions and exceptions require checking.",
                        "Review live matters each business day and after alerts; purchase only needed documents and retain lawful local copies.",
                        "Retrieve operative orders and claims procedures; fall back to the issuing court's public site or clerk-assisted retrieval.",
                    ],
                    [
                        "CourtListener RECAP; search courtlistener.com/recap and use documented API access only under the assigned account terms.",
                        "Public browsing is available without PACER document charges; API permissions and paid access depend on current service terms.",
                        "Check daily for relevant additions; observe account quotas because contributed docket coverage and upload timing vary.",
                        "Locate potentially useful docket copies; verify operative documents against PACER or the issuing court before acting.",
                    ],
                    [
                        "Court-authorized settlement administrator portal; follow the exact website named in the operative notice or court order.",
                        "Claimants can file directly without a recovery-service fee; retain any administrator-specific access and representation requirements.",
                        "Review weekly, then daily near deadlines; use permitted portal functions and never submit automated duplicate claims.",
                        "Capture class definitions, deadlines and claimant instructions; fall back to the administrator's published contact and court docket.",
                    ],
                    [
                        "ImportGenius; use importgenius.com account search, licensed exports or contracted API endpoints where included.",
                        "Paid subscription and API rights depend on the executed order form; confirm export limits before purchasing.",
                        "Schedule weekly prospecting pulls unless contracted freshness supports more; obey licensed quotas and measure shipment-to-publication lag.",
                        "Discover shipment relationships and prospect candidates; fall back to client shipping records and authorized broker entry extracts.",
                    ],
                    [
                        "S&P Global Panjiva; access panjiva.com through the licensed interface, export entitlement or separately contracted data delivery.",
                        "Commercial pricing and delivery rights are contractual; do not assume a web subscription includes API or redistribution rights.",
                        "Refresh qualified prospect lists weekly; apply contracted request limits and preserve provider coverage notes with every extract.",
                        "Cross-check supplier and consignee relationships; fall back to original bills of lading and client-confirmed corporate identities.",
                    ],
                    [
                        "SEC EDGAR; search sec.gov/edgar/search and retrieve public company submissions through data.sec.gov/submissions/CIK##########.json.",
                        "Public filings and submissions endpoints are free; use an identifying User-Agent with a monitored contact address.",
                        "Poll relevant entities daily at two requests per second maximum internally; remain below SEC's published ten-request ceiling.",
                        "Verify public-company names, subsidiaries and acquisitions; fall back to state corporate registries and signed client ownership records.",
                    ],
                    [
                        "OpenCorporates; search opencorporates.com and obtain API access from api.opencorporates.com under the applicable license.",
                        "Commercial reuse and API entitlement depend on licensing; public search visibility does not grant unrestricted republication rights.",
                        "Refresh active entity checks monthly and before filing; obey account quotas and record underlying registry update dates.",
                        "Resolve candidate legal entities and historical names; verify consequential facts against the originating governmental corporate registry.",
                    ],
                    [
                        "Una; use una.com membership inquiry and the authorized member or supplier contracting workflow.",
                        "Membership, supplier funding and eligible categories depend on executed agreements; confirm every administrative-fee basis in writing.",
                        "Reconcile member eligibility monthly and rebate statements quarterly; use approved exports rather than scraping restricted member accounts.",
                        "Verify authorized GPO purchasing brackets; fall back to signed supplier schedules and member-level paid invoice evidence.",
                    ],
                    [
                        "OMNIA Partners; enter omniapartners.com and select the appropriate private-sector membership and supplier-contract resources.",
                        "Program economics and membership rights are contract-specific; distinguish private-sector agreements from separate public-sector purchasing arrangements.",
                        "Review contract changes monthly and statements quarterly; request authorized files when a documented API is unavailable.",
                        "Validate supplier scope and eligible member purchases; fall back to executed agreements and supplier-confirmed transaction statements.",
                    ],
                    [
                        "OpenRefine; download from openrefine.org and run a local project against an approved working copy.",
                        "Open-source software has no license charge; hosting, analyst time and optional external reconciliation services add costs.",
                        "Run diagnostics on every intake batch; local transforms need no network requests unless an external service is explicitly enabled.",
                        "Cluster messy names and inspect transformations; fall back to original CSV files and a reviewed manual crosswalk.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy evidence depth only after the lead survives basic tests",
                "body": "Experienced desks preserve scarce analyst time by distinguishing prospect signals from filing-grade records.",
                "items": [
                    "Ask for ten representative entry lines and two complete export packets before licensing a large historical manifest extract.",
                    "Version HTS headings by effective date; a current eight-digit match cannot repair an incompatible historical classification.",
                    "Search settlement dockets using acquired entities and predecessor names, then document claim ownership before combining purchasing histories.",
                    "Keep a source-age field beside every deadline-sensitive record; stale public copies trigger direct broker or administrator confirmation.",
                ],
            },
        },
        {
            "heading": "2. Build line-level joins that survive an adversarial document review",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the pipeline around immutable source objects and reversible "
                    "transformations. A modest desk can use encrypted object storage, SQLite "
                    "for local investigation, PostgreSQL for shared case records and Git for "
                    "parser changes; select deployment tools according to actual operating "
                    "capacity. Python's csv, decimal, hashlib, datetime and sqlite3 modules "
                    "cover a substantial first implementation without subscription sprawl. "
                    "Create separate tables for entities, authorizations, entry lines, tariff "
                    "versions, export events, invoice lines, settlement matters, claim packets "
                    "and cash receipts. Each derived record must retain source-object hash, "
                    "source row, transformation version and reviewer decision. Use Decimal "
                    "for currency and explicit unit codes for quantities. Preserve the "
                    "original date string alongside its parsed date, particularly when "
                    "documents mix month-first and day-first conventions. A file checksum "
                    "proves that bytes stayed unchanged, not that the underlying commercial "
                    "event occurred. Reconcile line totals to broker statements or client "
                    "ledgers before proceeding. Quarantine malformed rows instead of dropping "
                    "them. Assign stable ingestion keys so the same invoice imported twice "
                    "does not double a potential recovery. If the client replaces a file, "
                    "store both versions and explain the delta rather than overwriting the "
                    "earlier evidence. This architecture makes corrections inspectable without "
                    "turning an analyst's spreadsheet into the sole system of record."
                ),
                (
                    "Separate candidate matching from legal eligibility. For manifest "
                    "prospecting, normalize names and addresses but retain the original "
                    "strings; a fuzzy match should generate a review queue, never a "
                    "file-ready importer identity. For direct-identification tracing and "
                    "export reconciliation, connect authorized entry lines to inventory "
                    "movements, invoices and export transport evidence using the identification "
                    "method applicable to the claim. For HTS substitution screening, an "
                    "eight-digit concordance is only a candidate filter: subsection-specific "
                    "rules, special classifications, quantity limitations and duty comparisons "
                    "still require broker review. Illustratively, 2,400 entry lines reduced "
                    "to 360 candidate lines by product and date filters create a manageable "
                    "work queue. If 90 lack export support and 30 fail legal screening, "
                    "240 remain for documentation, not automatic payment. At eight minutes "
                    "per retained line, review requires 32 hours; at $45 per hour, direct "
                    "analyst labor is $1,440. Preserve rejected lines with reason codes so "
                    "the next import does not resurrect them. Do not manufacture a missing "
                    "export date from an invoice date. Request carrier records or client "
                    "transport archives, and defer unsupported quantities. Drawback packet "
                    "assembly succeeds when every claimed quantity has a reproducible "
                    "allocation and no prior claim has already consumed the same entitlement."
                ),
                (
                    "Run diagnostic tests before analysts inspect individual opportunities. "
                    "Check duplicate entry-line keys, negative quantities, currencies outside "
                    "the contract, impossible date sequences, unmatched unit conversions and "
                    "multiple allocations of the same exported quantity. Build an exception "
                    "report for invoice totals that diverge from ledger controls by more "
                    "than a documented rounding tolerance. For settlement eligibility and "
                    "accounts-payable evidence packaging, test transaction dates against the "
                    "court-defined class period, map product descriptions to included products "
                    "and exclude credits or reversals according to administrator instructions. "
                    "A $500,000 purchase ledger with $20,000 of excluded credits supports "
                    "$480,000 of screened purchases, not a $480,000 expected distribution. "
                    "Store the allocation formula separately because settlement payments may "
                    "depend on approved claims, caps and deductions that remain unresolved. "
                    "For liquidation monitoring, calculate deadlines from verified legal "
                    "events, maintain jurisdiction-appropriate calendars and display source "
                    "documents next to every computed date. A parser test suite should "
                    "include amended entries, split shipments, duplicate filenames and "
                    "acquired entities sharing an address. Use synthetic fixtures for "
                    "development and restrict production evidence to authorized staff. When "
                    "a test fails, freeze the affected output partition, preserve the "
                    "diagnostic report and continue unrelated matters rather than silently "
                    "passing contaminated records downstream."
                ),
            ],
            "table": {
                "caption": "Four Pipeline Contracts Linking Discovery Signals to Defensible Evidence",
                "headers": [
                    "Pipeline object and stable identity",
                    "Mandatory join and diagnostic controls",
                    "Measurable processing assumption or control",
                    "Failure response and retained evidence",
                ],
                "rows": [
                    [
                        "Entry-line objects use authorized importer, entry number, line identifier and source-version keys.",
                        "Join paid-duty records to effective tariff versions; reconcile every extracted total against broker-provided controls.",
                        "Review 240 retained lines at eight minutes each; budget 32 analyst hours before specialist escalation.",
                        "Quarantine inconsistent duty totals and retain original statements; broker confirmation precedes any claim calculation.",
                    ],
                    [
                        "Export-event objects retain shipment identifier, item quantity, transport document and legally relevant dates.",
                        "Connect inventory allocations with export evidence; prevent the same quantity from supporting overlapping recovery claims.",
                        "Track unmatched quantities separately from supported quantities; report coverage by units rather than document count.",
                        "Request carrier archives or client shipping records; unsupported allocations remain excluded from the proposed packet.",
                    ],
                    [
                        "Settlement transaction objects retain claimant entity, invoice identifier, product category, date and net eligible amount.",
                        "Apply operative class definitions and administrator instructions; test exclusions, credits, acquisitions and duplicate submissions explicitly.",
                        "A $500,000 ledger less $20,000 excluded credits yields $480,000 screened purchases, not a predicted award.",
                        "Escalate disputed eligibility to the administrator; preserve their response and the controlling instructions with the matter.",
                    ],
                    [
                        "Receipt objects retain payer, beneficiary, matter identifier, bank reference and contractual fee-calculation version.",
                        "Match administrator or CBP payment evidence with the beneficiary's receipt; separate client principal from operator fees.",
                        "Invoice a 30% earned fee on $80,000 realized recovery only when contractual conditions support $24,000.",
                        "Hold disputed invoices and investigate mismatched remittances; never recognize an entire client recovery as desk revenue.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register authority and source boundaries",
                    "action": "Create the matter, verify the client signatory and record the permitted scope of each requested export.",
                    "detail": "Store the engagement, data permission and applicable customs power of attorney separately from public prospecting material.",
                },
                {
                    "step": 2,
                    "title": "Ingest and reconcile immutable evidence",
                    "action": "Hash original files, parse into versioned staging tables and reconcile amounts and quantities against source controls.",
                    "detail": "Publish row counts, rejected-row reasons, currency checks and duplicate keys before promoting records into the case dataset.",
                },
                {
                    "step": 3,
                    "title": "Apply lane-specific eligibility and deadlines",
                    "action": "Run dated tariff rules or settlement definitions, then route exceptions to the broker, counsel or administrator.",
                    "detail": "Retain the controlling authority, reviewer decision and deadline source with every proposed recovery line.",
                },
                {
                    "step": 4,
                    "title": "Package, transmit and reconcile outcomes",
                    "action": "Deliver an indexed evidence packet through the authorized channel and retain filing acknowledgments and subsequent receipts.",
                    "detail": "Track amendments and distributions separately; calculate earned fees only from the applicable contractual earning event.",
                },
            ],
        },
        {
            "heading": "3. Give each recovery lane its own legal clock and cash model",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The drawback lane starts with 19 U.S.C. § 1313 and the applicable "
                    "provisions of 19 CFR Part 190, not a universal refund percentage "
                    "applied to every import charge. Many eligible claims recover 99% of "
                    "qualifying duties, taxes and fees, but the statutory route, exclusions "
                    "and comparison rules control the actual base. Screen antidumping and "
                    "countervailing duties out of drawback calculations, and examine each "
                    "additional tariff regime independently; never classify every Chapter "
                    "99 charge as either eligible or barred. For an illustrative file with "
                    "$100,000 of fully eligible duty and no limiting adjustment, a 99% "
                    "recovery produces $99,000 for the client before the agreed fee. A "
                    "30% contingency produces $29,700 of operator revenue. Budgeting 40 "
                    "documentation hours at $45 plus a hypothetical $2,000 broker charge "
                    "leaves $25,900 before other costs; obtain actual quotes before accepting "
                    "the engagement. Check the import-based five-year claim period and "
                    "subsection-specific export or destruction conditions. Accelerated "
                    "payment requires CBP approval and appropriate bond coverage; ordinary "
                    "processing does not create an identical incremental bond requirement. "
                    "Use a six-to-eighteen-month collection assumption for initial planning, "
                    "explicitly replacing it with broker-supported case estimates. Missing "
                    "export traces trigger partial exclusion or deferral, not invented "
                    "shipment evidence."
                ),
                (
                    "The tariff-refund lane must distinguish Post-Summary Corrections from "
                    "protests. PSC triage concerns eligible unliquidated entries and current "
                    "ACE program rules; protest routing concerns protestable decisions under "
                    "19 U.S.C. § 1514 and applicable procedures in 19 CFR Part 174. The "
                    "usual PSC window is within 300 days of entry and at least 15 days "
                    "before scheduled liquidation, whichever deadline arrives first, subject "
                    "to current CBP rules and entry circumstances. A protest generally must "
                    "be filed within 180 days after liquidation or the relevant protestable "
                    "decision. Store those as distinct event-driven clocks rather than "
                    "a single five-year recovery horizon. Illustratively, $80,000 of verified "
                    "overpaid duties, fully refunded, produces a $24,000 fee at 30%. "
                    "Twenty-four documentation hours at $45 and a hypothetical $1,500 "
                    "specialist charge leave $21,420 before other costs. A PSC or protest "
                    "does not itself require a drawback accelerated-payment bond, although "
                    "the underlying import bond and disputed liabilities remain relevant. "
                    "Plan three-to-twelve months for a straightforward refund while "
                    "recognizing contested matters can take substantially longer. Route "
                    "formal work through the licensed customs broker or trade counsel "
                    "with valid authority. If liquidation timing defeats PSC eligibility, "
                    "assess an available protest route immediately instead of backdating "
                    "an amendment."
                ),
                (
                    "The settled antitrust lane begins with the operative class definition, "
                    "allocation plan and administrator instructions, not an advertised gross "
                    "settlement fund. Settlement eligibility screening identifies the claimant, "
                    "covered purchases, class period and exclusions; accounts-payable evidence "
                    "packaging establishes the supported transaction base. Distribution "
                    "reconciliation then matches actual payments to approved claims. The "
                    "collectible contingency base is the claimant's realized distribution "
                    "under the engagement, not its total purchases or the court's aggregate "
                    "fund. Illustratively, a $40,000 received distribution generates a "
                    "$12,000 fee at 30%. Twelve documentation hours at $45 and a hypothetical "
                    "$300 secure-delivery allocation leave $11,160 before other costs. "
                    "There is ordinarily no customs surety bond for this lane. Planning "
                    "may require six-to-twenty-four months after submission, with appeals, "
                    "deficiencies or supplemental distributions extending the period. Capture "
                    "court-required third-party filer disclosures and explain that eligible "
                    "claimants may submit directly without paying a recovery-service fee. "
                    "Do not claim administrator affiliation or submit duplicate claims to "
                    "improve perceived odds. These three examples are independent unit "
                    "models, not components of the canonical annual scorecard. Each requires "
                    "its own evidence cost, collection forecast and fee-recognition event. "
                    "When eligibility is disputed, seek administrator clarification, preserve "
                    "the reply and suspend any related fee demand."
                ),
            ],
            "table": {
                "caption": "Separate Collectible Bases, Documentation Budgets, Security Requirements and Cash Clocks",
                "headers": [
                    "Lane and controlling eligibility basis",
                    "Illustrative collectible base and operator economics",
                    "Documentation cost and security treatment",
                    "Cash assumption and failure fallback",
                ],
                "rows": [
                    [
                        "Duty drawback applies the chosen 19 U.S.C. § 1313 subsection and relevant Part 190 requirements.",
                        "$100,000 eligible duty times 99% equals $99,000 recovery; a 30% fee yields $29,700 operator revenue.",
                        "Model $1,800 analyst labor plus $2,000 broker work; accelerated payment additionally needs approved bond arrangements.",
                        "Plan six to eighteen months initially; exclude unsupported exports and replace estimates with case-specific broker evidence.",
                    ],
                    [
                        "Post-Summary Correction addresses eligible unliquidated entries under current ACE correction rules and entry-specific timing.",
                        "$80,000 verified overpayment fully refunded supports $24,000 revenue at 30%; never include refunded principal as revenue.",
                        "Illustrative tariff-file budget combines $1,080 labor and $1,500 specialist work; no separate drawback acceleration bond applies.",
                        "Plan three to twelve months for straightforward matters; reassess protest availability if liquidation prevents correction.",
                    ],
                    [
                        "Protests require a protestable decision, proper claimant authority and timely action under 19 U.S.C. § 1514.",
                        "Use the same $80,000 example only as an alternative route; never count PSC and protest recoveries twice.",
                        "Obtain separate counsel or broker estimates for contested cases; preserve underlying import-bond obligations without inventing new security requirements.",
                        "Contested cases may exceed twelve months materially; escalate approaching deadlines and assess remaining remedies with trade counsel.",
                    ],
                    [
                        "Settled antitrust claims follow the operative court order, class definition, allocation plan and administrator instructions.",
                        "$40,000 realized claimant distribution supports $12,000 operator revenue at 30%; purchase volume remains evidence only.",
                        "Model $540 analyst labor plus $300 delivery allocation; customs surety bonds do not apply to settlement claims.",
                        "Plan six to twenty-four months with extension risk; obtain administrator clarification and suspend disputed contingent fees.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before an opportunity becomes a submitted recovery packet",
                "body": "A positive spreadsheet estimate is insufficient until authority, eligibility, timing and evidence all reconcile.",
                "items": [
                    "Verify the client signatory, claimant ownership and formal-filing authority; retain the broker's valid customs power of attorney where applicable.",
                    "Confirm the exact drawback subsection, tariff remedy or settlement class definition; remove barred charges and unsupported purchases before calculating fees.",
                    "Validate deadlines against liquidation records, import dates or operative court orders; resolve conflicting source dates with the responsible specialist.",
                    "Reconcile supported quantities and collectible amounts, confirm accelerated-payment security when requested, and preserve required third-party filer disclosures.",
                ],
            },
        },
        {
            "heading": "4. Operate the tool stack against earned fees, not impressive transaction volume",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The twelfth mapped play is "
                    "private_b2b_gpo_umbrella_rebate_arbitrage, a TRACK_1 adjacent spend-recovery "
                    "workflow rather than a customs remedy. Pool 10,000–75,000+ seats and "
                    "indirect spend across hundreds of SMB members only through authorized "
                    "master GPO brackets, using Una, OMNIA or an eligible private vertical "
                    "SaaS, parcel or telecom program. Seat totals describe negotiating "
                    "scale; they are not revenue. Quarter-end comparisons may use Vendr "
                    "or Tropic methodologies and licensed benchmark access, but confidential "
                    "customer benchmarks cannot be presumed transferable. Target ranges "
                    "of 3%–12% vendor-paid administrative rebates and 25%–35% Year-1 "
                    "shared-savings fees require contract-level verification. For one "
                    "illustrative member cohort, a documented $120,000 baseline reduced "
                    "to $108,000 yields $12,000 gross savings; a 30% shared-savings fee "
                    "is $3,600, leaving $8,400 before other member costs. A separate 3% "
                    "administrative rebate on $108,000 eligible paid spend is $3,240 only "
                    "if the supplier agreement permits that base and compensation. Disclose "
                    "both payments and any required offsets; never add a retained vendor "
                    "rebate to client savings. Keep this adjacent example outside the "
                    "canonical customs-and-settlement revenue cases. If eligibility or "
                    "baseline calculations are disputed, suspend fees, reconcile with "
                    "members and suppliers, refund unearned amounts and move affected "
                    "members to eligible purchasing agreements."
                ),
                (
                    "Tie subscriptions and staffing to the canonical Formula v2.0 "
                    "scorecard, not to gross merchandise value or an administrator's "
                    "settlement pool. Conservative annual earned-fee revenue is $110,000; "
                    "the 32% margin yields $35,200 owner profit and $74,800 total modeled "
                    "costs. Base revenue is $515,000; the 45.0% margin yields $231,750 "
                    "owner profit and $283,250 costs. Scaled revenue is $920,000; the "
                    "58% margin yields $533,600 owner profit and $386,400 costs. "
                    "Conservative and Base each use one full-time operator plus three "
                    "contractors; Scaled uses two full-time staff plus four contractors. "
                    "Contractor count does not imply six full-time salaries. Treat the "
                    "$1,500–$9,500 monthly operating-expense range as a planning category, "
                    "not a substitute for all annual costs, including variable specialist "
                    "work. The $8,000–$35,000 startup range funds setup and working "
                    "capacity; a first engagement in one to three months does not mean "
                    "a refund arrives then. Under the stated revenue basis, gross revenue "
                    "means the operator's earned fees, not the client's recovered principal. "
                    "If an arrangement requires principal-versus-agent assessment under "
                    "ASC 606, apply the appropriate presentation to that arrangement rather "
                    "than mechanically changing these supplied cases. Maintain separate "
                    "cash, earned-fee and client-recovery ledgers so timing differences "
                    "cannot inflate apparent profitability."
                ),
                (
                    "Use a weekly operating review to decide which tools deserve renewal. "
                    "Measure verified opportunities per paid source, analyst minutes per "
                    "supported line, unresolved evidence age, deadline exceptions, accepted "
                    "packets, realized distributions and collected fees. A $600 monthly "
                    "data allocation costs $7,200 annually; at a 30% fee, it requires "
                    "$24,000 of incremental realized client recoveries merely to cover "
                    "that subscription before labor. That is a diagnostic hurdle, not "
                    "a forecast or a vendor price quote. Compare the paid source "
                    "against a public-data and client-export control sample before attributing "
                    "wins. Use OpenRefine for reversible entity cleanup, SQLite queries "
                    "for duplicate detection and a broker-reviewed checklist for tariff "
                    "logic; no dashboard replaces the specialist's eligibility decision. "
                    "Track workload separately from money: 30 signed engagements with "
                    "incomplete export records can consume more capacity than ten "
                    "fully documented claims. Close abandoned matters with a reason "
                    "code and retention schedule, then remove unnecessary access. Test "
                    "restoration of encrypted backups quarterly and verify that departed "
                    "contractors lose matter permissions promptly. The durable information "
                    "edge is not a secret database. It is the ability to turn "
                    "authorized, time-stamped records into a reproducible packet, collect "
                    "the resulting earned fee and explain every rejected dollar."
                ),
            ],
            "table": {
                "caption": "Tooling Economics and Adjacent GPO Controls Without Revenue Double Counting",
                "headers": [
                    "Operating model or diagnostic decision",
                    "Exact revenue and profit reconciliation",
                    "Capacity or evidence requirement",
                    "Control against inflated results",
                ],
                "rows": [
                    [
                        "Conservative Formula v2.0 case uses earned customs and settlement contingency fees only.",
                        "$110,000 annual revenue minus $74,800 modeled costs equals $35,200 owner profit at 32%.",
                        "One full-time operator and three contractors share documented intake, specialist review and collection responsibilities.",
                        "Exclude client refund principal and adjacent GPO examples; reconcile every fee to its contractual earning event.",
                    ],
                    [
                        "Base Formula v2.0 case retains the same small-team structure while processing more supported recoveries.",
                        "$515,000 annual revenue minus $283,250 modeled costs equals $231,750 owner profit at 45.0%.",
                        "One full-time operator and three contractors need measured throughput, complete evidence packets and controlled specialist spending.",
                        "Do not substitute monthly software overhead for total modeled costs or recognize unsigned contingent estimates as revenue.",
                    ],
                    [
                        "Scaled Formula v2.0 case increases staff capacity without treating client recoveries as operator sales.",
                        "$920,000 annual revenue minus $386,400 modeled costs equals $533,600 owner profit at 58%.",
                        "Two full-time staff and four contractors require matter-level permissions, documented handoffs and independent receipt reconciliation.",
                        "Keep purchase volume, duty principal and settlement funds outside operator revenue; verify fee presentation for each arrangement.",
                    ],
                    [
                        "Authorized GPO play remains an adjacent example with independently verified member and supplier compensation terms.",
                        "$12,000 savings supports $3,600 shared-savings fees; a separately permitted 3% rebate on $108,000 equals $3,240.",
                        "Verify member eligibility, baseline comparability, eligible paid spend, dual-compensation disclosure and any contractual rebate offsets.",
                        "Suspend disputed fees, reconcile baselines, refund unearned amounts and transfer affected members to eligible purchasing agreements.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A discovery signal earns attention; only authorized evidence, a live deadline and a realized recovery can earn the fee.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create the eighteen-source registry with access owner, license scope, polling target, source-effective date and documented fallback.",
        "Obtain a narrow authorized ACE sample, export packet and settlement purchase extract before buying broad commercial enrichment.",
        "Implement immutable file hashes, line-level source references, Decimal currency calculations and duplicate-allocation diagnostics.",
        "Separate drawback, PSC, protest and settlement clocks; have the responsible broker, counsel or administrator resolve exceptions.",
        "Validate GPO member eligibility and both compensation bases; document benchmark rights, baseline adjustments and required offsets.",
        "Reconcile earned fees, client receipts and total modeled costs monthly against the exact Conservative, Base and Scaled scorecard cases.",
    ],
    "statutory_citations": [
        {
            "title": "19 U.S.C. § 1313 — Drawback and refunds",
            "url": "https://www.law.cornell.edu/uscode/text/19/1313",
            "relevance": "Establishes drawback routes, subsection-specific eligibility, recovery limitations and the import-based claim period.",
        },
        {
            "title": "19 U.S.C. § 1514 — Finality of decisions; protests",
            "url": "https://www.law.cornell.edu/uscode/text/19/1514",
            "relevance": "Identifies protestable customs decisions, eligible protesting parties and applicable protest timing.",
        },
        {
            "title": "19 CFR Part 111 — Customs brokers",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-111",
            "relevance": "Governs customs-broker licensing, customs-business responsibilities and the professional filing channel used by this desk.",
        },
        {
            "title": "19 CFR Part 141, Subpart C — Powers of attorney",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-141/subpart-C",
            "relevance": "Provides customs power-of-attorney requirements relevant to authorized broker representation and retained authority records.",
        },
        {
            "title": "19 CFR Part 190 — Modernized drawback",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-190",
            "relevance": "Supplies operational rules for drawback eligibility, supporting evidence, filing and recordkeeping.",
        },
        {
            "title": "19 CFR § 190.92 — Accelerated payment",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-190/subpart-I/section-190.92",
            "relevance": "Addresses accelerated drawback payment, application conditions and associated bond requirements.",
        },
        {
            "title": "19 CFR Part 174 — Protests",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-174",
            "relevance": "Provides protest procedures, content requirements and review mechanics distinct from Post-Summary Corrections.",
        },
        {
            "title": "19 CFR § 191.3 — Duties, taxes, and fees subject or not subject to drawback",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-191/subpart-A/section-191.3",
            "relevance": "Provides an additional regulatory cross-check on excluded charges, including antidumping and countervailing duties; apply the governing modernized rules to the actual claim.",
        },
        {
            "title": "Federal Rule of Civil Procedure 23 — Class actions",
            "url": "https://www.law.cornell.edu/rules/frcp/rule_23",
            "relevance": "Provides the federal class-action framework; the operative settlement order and administrator instructions supply matter-specific claim and disclosure requirements.",
        },
    ],
}
