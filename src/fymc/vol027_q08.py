from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small business acquisition desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "Secretary of State Searches, UCC Liens, PACER, QuickBooks and Bank Evidence for ETA Sourcing, QoE and SBA/Seller-Note Execution",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #13, Business Acquisition, ranks #27 with a Money-to-Manpower "
        "Score of 57/100: evidence automation helps, but ownership remains capital "
        "and labor intensive. This directory maps seven operator plays: target "
        "origination, entity verification, liability discovery, revenue validation, "
        "QoE normalization, financing structure, and the 100-day turnaround. Build "
        "one traceable evidence spine rather than buying disconnected lead lists. "
        "The canonical annual owner profit cases are $60,000 Conservative, $243,750 "
        "Base, and $540,000 Scaled, after interest and before principal repayments. "
        "Use public records to challenge claims, then permissioned accounting and "
        "bank evidence to resolve them. A seven-employee, three-contractor operating "
        "pod needs exception queues, disciplined access, and specialist escalation, "
        "not another full-time research department."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$750,000",
            "context": "Annual acquired-business sales; not acquisition fees or transaction principal",
            "note": "8% margin; $60,000 annual owner net profit; 7 FT + 3 C; after interest, before principal repayments",
        },
        {
            "label": "Base",
            "value": "$1,875,000",
            "context": "Annual acquired-business sales; not acquisition fees or transaction principal",
            "note": "13.0% margin; $243,750 annual owner net profit; 7 FT + 3 C; after interest, before principal repayments",
        },
        {
            "label": "Scaled",
            "value": "$3,000,000",
            "context": "Annual acquired-business sales; not acquisition fees or transaction principal",
            "note": "18% margin; $540,000 annual owner net profit; 8 FT + 4 C; after interest, before principal repayments",
        },
    ],
    "sections": [
        {
            "heading": "1. Build a jurisdiction-aware directory before building a target list",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Organize the acquisition desk around seven explicitly mapped plays: "
                    "P1 target origination, P2 entity verification, P3 liability discovery, "
                    "P4 revenue validation, P5 QoE normalization, P6 financing structure, "
                    "and P7 the 100-day turnaround. These are this chapter's operating "
                    "labels, not seven additional businesses or revenue streams. Assign "
                    "every collected field to a play and a decision: a former legal "
                    "name improves lien searches; a permit expiration changes the "
                    "transition calendar; bank settlements challenge recorded sales. "
                    "For the seven-full-time, three-contractor model, a practical "
                    "allocation is an owner-operator, an operating manager, an "
                    "administrative controller, and four delivery employees, supported "
                    "by contracted transaction counsel, a QoE accountant, and an "
                    "integration specialist. These are capacity assignments within "
                    "the ten-person envelope, not hires layered onto the scorecard. "
                    "The delivery employees protect customer service while the owner "
                    "and controller maintain the evidence queue. During the search "
                    "period, the buyer and retained specialists cover those functions "
                    "before the acquired operating team transfers. Keep only enough "
                    "active diligence files to inspect each exception weekly; "
                    "software cannot make ten people simultaneously operate the "
                    "business, rebuild its books, and close several transactions."
                ),
                (
                    "Start each target with a jurisdiction map containing formation "
                    "state, operating locations, property counties, historical names, "
                    "and license issuers. Secretary of State records establish filed "
                    "identity and status, not the actual ownership of every entity. "
                    "An organizer or registered agent is not automatically an owner. "
                    "Apply enacted state versions of UCC sections 9-301, 9-307, "
                    "9-503, and 9-507 when choosing filing offices and debtor-name "
                    "searches; fixture filings and certain collateral require "
                    "additional treatment. A web search result is a lead, while "
                    "a dated official search report supports a transaction workpaper. "
                    "Search federal litigation through PACER and state litigation "
                    "through the relevant judiciary because neither substitutes "
                    "for the other. County land records can expose mortgages, "
                    "recorded liens, and property transfers, but tax-lien filing "
                    "locations vary with applicable rules and property type. "
                    "Treat every negative result as scoped evidence: record the "
                    "name, office, date range, and indexing limitations. A clean "
                    "screen never establishes that all liabilities are absent. "
                    "Have counsel define closing search coverage, payoff evidence, "
                    "and termination deliverables rather than letting an entity "
                    "matching script decide whether a lien has disappeared."
                ),
                (
                    "Use the directory below as an acquisition-specific retrieval "
                    "plan, not a claim that every portal offers bulk access. "
                    "Cost descriptions distinguish public viewing, transaction "
                    "charges, and negotiated commercial products; verify current "
                    "prices before procurement. Refresh descriptions describe "
                    "source behavior rather than promised delivery times. Capture "
                    "both source publication time and retrieval time so a fresh "
                    "download does not disguise old underlying records. For an "
                    "API, read the documented quota, respect Retry-After when "
                    "provided, and use bounded exponential backoff with jitter. "
                    "For a human-only portal, perform a documented manual search "
                    "or purchase its authorized export instead of bypassing "
                    "access controls. Preserve search receipts and source files "
                    "because public interfaces change during a six-to-eighteen-month "
                    "deal cycle. Do not infer loan balances from SBA origination "
                    "datasets, transferable permits from active license displays, "
                    "or customer retention from federal award totals. Each "
                    "source earns its place only when it changes outreach, "
                    "price, structure, or a post-close operating action. The "
                    "controller owns provenance; counsel interprets legal findings; "
                    "the owner decides whether the evidence justifies spending "
                    "the next diligence dollar or extending exclusivity."
                ),
            ],
            "table": {
                "caption": "Eighteen-source acquisition directory: access, pricing class, latency, retrieval discipline, and fallback evidence",
                "headers": [
                    "Named source and mapped acquisition decision",
                    "Exact access method and permitted scope",
                    "Cost tier and refresh latency expectation",
                    "Rate-limit hygiene and fallback evidence source",
                ],
                "rows": [
                    [
                        "State Secretary of State business search supports P1 sourcing and P2 identity verification",
                        "Open the formation state's official business-search portal; purchase filing images and certificates directly",
                        "Basic viewing is often free; documents carry state fees; indexing follows each office's processing cycle",
                        "Use manual search unless bulk access is licensed; fall back to certified filings and seller organizational records",
                    ],
                    [
                        "State UCC filing office exposes P3 secured-creditor claims against the correct debtor",
                        "Order official debtor-name searches and filing copies through the jurisdiction's designated UCC search service",
                        "Searches and certified reports usually carry state fees; recent filings may await indexing",
                        "Respect portal restrictions and search logic; supplement with counsel-directed searches, payoff letters, and closing updates",
                    ],
                    [
                        "PACER Case Locator identifies P3 federal litigation and bankruptcy proceedings requiring docket review",
                        "Register at pacer.uscourts.gov, search Case Locator, then retrieve documents from the relevant federal court",
                        "Metered access uses the published fee schedule and applicable waivers; court and index updates differ",
                        "Limit queries to documented entity variants; fall back to court clerks and certified docket documents",
                    ],
                    [
                        "CourtListener RECAP provides P3 federal case discovery and reusable public docket documents",
                        "Use courtlistener.com/recap or its documented REST API with authentication where the chosen endpoint requires",
                        "Public browsing is free; API terms vary; coverage depends partly on contributed PACER documents",
                        "Honor account quotas and attribution terms; verify consequential findings against PACER and the issuing court",
                    ],
                    [
                        "Official state judiciary portals reveal P3 local lawsuits missing from federal court searches",
                        "Select each operating state's official court case-search service and inspect relevant county coverage",
                        "Public indexes may be free; document charges vary; court posting delays and exclusions differ",
                        "Avoid unsupported automated scraping; request clerk searches or copies when online coverage is incomplete",
                    ],
                    [
                        "County recorder land records connect P3 property transfers, mortgages, and recorded lien evidence",
                        "Search the official recorder or register-of-deeds grantor-grantee index using legal names and parcels",
                        "Index access may be free; images and certified copies incur local fees; recording indexes can lag",
                        "Follow county session limits; obtain a title search and counsel-directed lien coverage where necessary",
                    ],
                    [
                        "County assessor GIS links P2 operating addresses with parcels and P3 property-tax questions",
                        "Use the official assessor parcel search or the county's published ArcGIS REST service",
                        "Public viewing is generally free; assessed values follow local cycles rather than market-price updates",
                        "Use documented GIS pagination; verify taxes with the collector and ownership with recorded deeds",
                    ],
                    [
                        "State licensing boards and municipal permit portals test P2 authority and P7 transfer timing",
                        "Query the issuing agency's official license verification page by license number and legal entity",
                        "Basic verification is often free; certified histories cost extra; disciplinary postings follow agency workflows",
                        "Respect manual-only interfaces; obtain written agency confirmation of transfer, qualification, and renewal requirements",
                    ],
                    [
                        "OSHA Establishment Search identifies P3 inspections and safety issues affecting the operating plan",
                        "Search establishment records through osha.gov/ords/imis/establishment.html using names, locations, and inspection dates",
                        "Public access is free; inspection updates and case status reflect administrative processing delays",
                        "Search historical names without aggressive retries; reconcile findings with seller logs and specialist safety review",
                    ],
                    [
                        "EPA ECHO identifies P3 regulated facilities, enforcement records, and environmental operating questions",
                        "Use echo.epa.gov facility search or the documented ECHO web services for relevant regulatory programs",
                        "Public searches and services are free; refresh timing depends on the underlying program dataset",
                        "Use published service parameters and bounded requests; verify material findings with the responsible state agency",
                    ],
                    [
                        "SAM.gov exclusions and entity records support P2 identity checks and P6 federal-contract diligence",
                        "Use sam.gov public search; obtain an API key for documented services requiring authenticated access",
                        "Public searches are free; API availability and quotas depend on service; updates follow record processing",
                        "Cache entity identifiers and respect key limits; verify contracts and eligibility with contracting personnel",
                    ],
                    [
                        "USAspending.gov award data supports P1 contractor sourcing and P4 customer concentration investigation",
                        "Use usaspending.gov search, downloadable award files, or documented POST endpoints at api.usaspending.gov",
                        "Public access is free; reporting schedules and subsequent agency corrections govern data freshness",
                        "Prefer scoped downloads over repeated broad queries; reconcile awards with contracts, invoices, and actual receipts",
                    ],
                    [
                        "SBA public loan datasets identify P1 borrower cohorts and P6 historical funding questions",
                        "Download published 7(a) and 504 FOIA loan files through data.sba.gov and retain dataset metadata",
                        "Published files are free; update cadence is dataset-specific; origination fields do not establish current balances",
                        "Download each release once and version it; obtain current lender statements and seller-authorized payoff evidence",
                    ],
                    [
                        "Census County Business Patterns measures P1 industry density and P7 local market context",
                        "Use census.gov/programs-surveys/cbp or its documented Census Data API with published industry and geography variables",
                        "Public datasets are free; annual releases have reporting lag and may suppress sensitive cells",
                        "Use an API key where required by current rules; compare with Census bulk files and local records",
                    ],
                    [
                        "BLS QCEW benchmarks P5 wage assumptions and P7 labor-market pressure by industry",
                        "Download quarterly files from bls.gov/cew or use the documented QCEW open-data file interfaces",
                        "Public files are free; quarterly releases lag employment activity and later revisions can change values",
                        "Cache geography and industry extracts; triangulate with payroll registers and current local recruiting quotes",
                    ],
                    [
                        "SEC EDGAR provides P4 public-customer risk signals and P5 comparable accounting disclosures",
                        "Retrieve company submissions and XBRL data through data.sec.gov using the documented EDGAR interfaces",
                        "Public access is free; acceptance timestamps identify filings; private target coverage is usually absent",
                        "Identify the client in User-Agent and follow SEC fair-access limits; use issuer filings as fallback",
                    ],
                    [
                        "QuickBooks Online Accounting API supports permissioned P4 receipts analysis and P5 ledger reconstruction",
                        "Register an Intuit application, complete OAuth authorization, and query documented accounting entities and reports",
                        "Production access depends on current Intuit program terms and account subscriptions; posting timing follows seller bookkeeping",
                        "Respect realm-specific throttling and pagination; request accountant exports and reconcile them to controlled ledger totals",
                    ],
                    [
                        "Plaid Transactions and Balance support authorized P4 bank reconciliation and P6 liquidity review",
                        "Create a Plaid account, use Link authorization, then call documented Transactions Sync and Balance endpoints",
                        "Commercial production pricing follows product contracts; history depth and refresh timing depend on institution support",
                        "Handle cursors, webhooks, and throttling carefully; fall back to complete bank statements and lender confirmations",
                    ],
                ],
            },
        },
        {
            "heading": "2. Run an evidence-first enrichment waterfall with explicit stop rules",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run enrichment in a fixed order: official entity identity, "
                    "company-owned website, licensed business directory, commercial "
                    "contact discovery, and human verification. OpenCorporates can "
                    "help connect legal names and jurisdictions, but confirm decisive "
                    "facts against the filing office and license API access under "
                    "its current terms. Apollo can suggest business contacts; Hunter "
                    "can test domain-based email hypotheses; neither establishes "
                    "ownership, authority to sell, or permission to retrieve private "
                    "records. Store each provider's claim separately rather than "
                    "overwriting an official fact with a higher-confidence marketing "
                    "score. A target record needs a stable internal identifier, "
                    "legal-name history, formation identifier, website domain, "
                    "operating address, source timestamp, and match rationale. "
                    "Require at least two independent matching attributes before "
                    "merging records, and send shared addresses, common names, "
                    "and franchise locations to human review. Stop buying credits "
                    "when the legal entity is unresolved or the business falls "
                    "outside the owner's acquisition criteria. A cheap contact "
                    "attached to the wrong debtor can create expensive diligence "
                    "work, mistaken outreach, and an incorrect concentration "
                    "analysis later. Preserve rejected matches so the next "
                    "provider cannot silently recreate the same mistake."
                ),
                (
                    "Set a deliberately small enrichment allowance inside the "
                    "existing operating budget rather than describing subscriptions "
                    "as incremental profit. As an illustrative purchasing rule, "
                    "authorize $300 monthly for screening 100 named targets: "
                    "$3 per screened target before labor and specialist work. "
                    "If only 20 targets meet the mandate, that becomes $15 "
                    "per qualified target, not $3. Three seller conversations "
                    "would imply $100 of subscription expense per conversation, "
                    "without proving that enrichment caused any conversation. "
                    "Use these denominators to cancel tools that produce "
                    "decorative coverage. Do not extrapolate this screening "
                    "budget into deal economics or replace the canonical "
                    "$15,000–$70,000 monthly operating-expense range with it. "
                    "The owner approves target criteria, the controller manages "
                    "provider credits, and the integration contractor maintains "
                    "connectors within a capped assignment. Counsel reviews "
                    "permitted use where a product includes personal information. "
                    "Keep commercial outreach accurate and apply the concrete "
                    "requirements of 15 U.S.C. 7704 when sending commercial "
                    "email, including truthful headers, required sender details, "
                    "and functioning opt-out handling. A verified address "
                    "measures deliverability; it does not erase messaging "
                    "obligations or justify repeated contact after suppression."
                ),
                (
                    "Implement the first pipeline with Python's csv, json, "
                    "sqlite3, hashlib, and urllib modules before buying an "
                    "orchestration platform. Store immutable source artifacts "
                    "separately from normalized SQLite tables, then attach "
                    "artifact hashes, retrieval times, request parameters, "
                    "and transformation versions to each derived finding. "
                    "Keep API credentials outside exports and redact tokens "
                    "from request logs. Use least-privilege database roles "
                    "where the deployed database supports them; protect "
                    "local SQLite files through operating-system permissions "
                    "and encrypted storage. Idempotent imports should key "
                    "records by source and native identifier, with "
                    "versioned snapshots for changing fields. Test entity "
                    "collisions, empty pages, repeated cursors, deleted "
                    "transactions, changed accounting periods, and malformed "
                    "currency strings. Quarantine incomplete responses rather "
                    "than converting missing amounts to zero. Maintain a "
                    "queue with severity, owner, due date, evidence link, "
                    "and decision impact. Only the owner and controller "
                    "need routine access to the acquisition dashboard; "
                    "delivery employees receive the operational tasks "
                    "relevant to their work. This keeps P1 through "
                    "P7 connected without exposing payroll, customer "
                    "contracts, or seller bank details across the "
                    "entire ten-person pod. Review access again when "
                    "a bidder withdraws or a contractor finishes."
                ),
            ],
            "table": {
                "caption": "Six-stage enrichment and ingestion waterfall with commercial stop rules",
                "headers": [
                    "Stage and named tool or source",
                    "Evidence accepted into the target record",
                    "Spend control and retrieval operating rule",
                    "Exception handling and accountable pod owner",
                ],
                "rows": [
                    [
                        "First stage uses official corporate and licensing registries",
                        "Accept filed entity identifiers, jurisdiction, status, and explicitly documented license attributes",
                        "Pay document fees only after confirming mandate fit and search jurisdiction",
                        "Controller separates registered agents from owners and escalates conflicting entity names",
                    ],
                    [
                        "Second stage inspects the company's own website and contact pages",
                        "Accept published domains, operating locations, service descriptions, and clearly attributed management names",
                        "Use ordinary permitted browsing and capture dated evidence without bulk harvesting",
                        "Owner resolves franchise, subsidiary, and trading-name ambiguity before commercial enrichment",
                    ],
                    [
                        "Third stage uses licensed OpenCorporates searches or API access",
                        "Accept attributed cross-jurisdiction leads while retaining each original registry reference",
                        "Check license terms, credit consumption, and documented quotas before scheduled retrieval",
                        "Controller verifies decisive claims through the appropriate official filing office",
                    ],
                    [
                        "Fourth stage uses Apollo contact discovery within contracted access",
                        "Accept suggested professional contacts with provider timestamps and explicit confidence limitations",
                        "Cap credits by qualified target and stop when entity identity remains unresolved",
                        "Owner confirms commercial relevance and prevents provider guesses becoming ownership facts",
                    ],
                    [
                        "Fifth stage uses Hunter domain search and email verification",
                        "Accept delivery-status signals separately from identity, ownership, and outreach authorization",
                        "Purchase verification only for selected contacts and honor provider request limits",
                        "Controller maintains suppression records and routes ambiguous contacts to manual review",
                    ],
                    [
                        "Sixth stage uses Python ingestion and a controlled SQLite evidence ledger",
                        "Accept validated records carrying source identifiers, artifact hashes, and transformation versions",
                        "Run incremental jobs with bounded retries and a documented monthly connector budget",
                        "Integration contractor fixes quarantined imports while controller signs reconciled batch totals",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four ways experienced buyers prevent expensive false certainty",
                "body": "Spend enrichment credits on resolved entities and reserve specialist time for findings capable of changing the transaction.",
                "items": [
                    "Build the historical debtor-name list before ordering UCC searches; include documented mergers and name changes so counsel can determine the correct search coverage.",
                    "Compare operating addresses across permits, payroll locations, and customer invoices; a mailing address alone can conceal an unreviewed operating site.",
                    "Use accounting document numbers and bank settlement references as reconciliation anchors; matching only dates and amounts breaks when deposits are batched.",
                    "Retain rejected entity matches with reasons; otherwise a refreshed commercial dataset can reintroduce a previously disproved owner or subsidiary relationship.",
                ],
            },
        },
        {
            "heading": "3. Turn permissioned records into a reproducible QoE and financing bridge",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Move from public research to seller-authorized access only "
                    "after defining the entity, period, purpose, and recipients "
                    "of each dataset. Request monthly trial balances, general "
                    "ledgers, bank statements, accounts-receivable aging, payroll "
                    "registers, tax returns, and customer-level sales for a "
                    "consistent diligence period. QuickBooks OAuth authorization "
                    "must come from an authorized account administrator, "
                    "and permissions must be limited to what the platform "
                    "actually supports; do not advertise a read-only "
                    "restriction that the granted scope does not enforce. "
                    "Where appropriate, use controlled accountant exports "
                    "instead. Plaid access similarly requires authorized "
                    "connection of the relevant accounts, supported "
                    "institutions, and an agreed retention policy. Public "
                    "registries do not expose confidential federal tax "
                    "returns: 26 U.S.C. 6103 governs disclosure, and "
                    "seller-provided returns or properly authorized transcript "
                    "procedures serve a different evidentiary role. Do "
                    "not substitute personal consumer reports for ordinary "
                    "business diligence. If a proposed report is covered "
                    "by the Fair Credit Reporting Act, establish an "
                    "actual permissible purpose under 15 U.S.C. 1681b "
                    "and applicable procedural duties before ordering it. "
                    "A signed acquisition interest letter alone does "
                    "not create unrestricted access to personal records."
                ),
                (
                    "Build the revenue bridge from invoices to ledger "
                    "postings, settlement batches, bank deposits, and reported "
                    "tax figures, preserving timing differences explicitly. "
                    "Separate sales taxes collected, customer deposits, "
                    "loan proceeds, owner contributions, refunds, chargebacks, "
                    "and transfers between accounts. A deposit is not "
                    "automatically revenue; an invoice is not automatically "
                    "cash. For marketplace or payment businesses, distinguish "
                    "merchant throughput from the target's recognized fees. "
                    "For this candidate, the scorecard revenue basis is "
                    "acquired-business sales, not acquisition purchase price, "
                    "borrowed principal, or a broker's transaction fee. "
                    "Use Decimal arithmetic for money and reconcile "
                    "every import to its source control total. "
                    "Construct customer cohorts using stable customer "
                    "identifiers so renamed accounts do not imitate "
                    "retention or attrition. Analyze concentration by "
                    "both revenue and gross contribution where reliable "
                    "cost attribution exists. Trace unusual month-end "
                    "journal entries and post-period credits before "
                    "accepting apparent growth. The contracted QoE "
                    "accountant evaluates evidence-supported adjustments; "
                    "the owner retains responsibility for the bid. "
                    "Every proposed add-back needs a ledger reference, "
                    "business rationale, recurrence assessment, and "
                    "replacement-cost treatment. Removing the seller's "
                    "pay while ignoring the replacement manager's "
                    "cost overstates transferable earnings."
                ),
                (
                    "Keep financing analysis separate from the earnings "
                    "bridge. The canonical Conservative case is $750,000 "
                    "of sales multiplied by 8%, producing $60,000; "
                    "Base is $1,875,000 multiplied by 13.0%, "
                    "producing $243,750; Scaled is $3,000,000 "
                    "multiplied by 18%, producing $540,000. These "
                    "owner-profit figures are after interest and "
                    "before principal repayments. Do not subtract "
                    "interest twice, label these amounts EBITDA, "
                    "or present them as cash available after "
                    "all debt service. Build a separate liquidity "
                    "bridge deducting scheduled principal, required "
                    "capital expenditure, and working-capital increases, "
                    "with other cash adjustments shown explicitly. "
                    "For SBA-backed financing, obtain current lender "
                    "requirements and the applicable SBA procedures; "
                    "eligibility, seller-note treatment, equity injection, "
                    "and standby provisions depend on the transaction "
                    "and current program rules. Historical SBA "
                    "datasets cannot establish approval or current "
                    "indebtedness. For conventional and seller debt, "
                    "model contractual maturities, amortization, "
                    "security interests, and covenant definitions "
                    "from actual documents. Never substitute a "
                    "generic debt-service ratio for the lender's "
                    "defined calculation. Counsel and the lender "
                    "resolve intercreditor terms; the controller "
                    "maintains the payment calendar and flags "
                    "the earliest projected cash shortfall."
                ),
            ],
            "table": {
                "caption": "Six acquisition forensics tests linking source records to earnings and leverage decisions",
                "headers": [
                    "Diagnostic and affected mapped operator play",
                    "Source records and concrete reconciliation procedure",
                    "Failure signal requiring a specific response",
                    "Owner and transaction or operating consequence",
                ],
                "rows": [
                    [
                        "Invoice-to-cash testing supports P4 recognized-sales validation",
                        "Join invoices, ledger postings, settlement batches, and bank receipts using stable references",
                        "Unexplained deposits, duplicate invoices, and later credits require separately documented adjustments",
                        "QoE accountant quantifies exposure before owner revises price or collection assumptions",
                    ],
                    [
                        "Customer cohort testing supports P4 concentration and P7 retention",
                        "Map historical customer identifiers to monthly sales and reliable contribution measures",
                        "Recent departures or renamed accounts can disguise deteriorating repeat-customer economics",
                        "Operating manager prioritizes retention work without counting unsigned renewals as contracted revenue",
                    ],
                    [
                        "Payroll reconstruction supports P5 replacement-cost and labor normalization",
                        "Reconcile payroll registers, employment agreements, tax filings, and actual staffing schedules",
                        "Unpaid family labor or departing seller duties create real replacement-cost requirements",
                        "Controller and QoE accountant revise earnings bridge within the existing staffing envelope",
                    ],
                    [
                        "Debt reconciliation supports P3 lien resolution and P6 financing structure",
                        "Tie lender statements and note schedules to ledger balances and dated payoff letters",
                        "Unrecorded borrowing or unresolved security interests require explicit closing deliverables",
                        "Counsel and lender resolve releases while controller rebuilds contractual cash payments",
                    ],
                    [
                        "Working-capital testing supports P5 earnings quality and P6 liquidity planning",
                        "Reconcile receivable aging, inventory evidence, payable aging, and subsequent cash settlement",
                        "Old receivables or obsolete inventory can overstate usable acquisition working capital",
                        "Owner negotiates evidenced working-capital terms and funds the operating cash requirement",
                    ],
                    [
                        "Permit and contract review supports P2 authority and P7 continuity",
                        "Compare issued licenses and executed contracts with transaction structure and assignment provisions",
                        "Change-of-control restrictions or nontransferable permits can interrupt otherwise profitable operations",
                        "Counsel secures required permissions while operating manager sequences continuity actions",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before using the diligence model in a bid",
                "body": "Advance the model only when each check has an accountable owner and evidence that another reviewer can reproduce.",
                "items": [
                    "Entity check: confirm the seller, operating subsidiaries, asset owners, debtor names, and relevant jurisdictions against official records and transaction documents.",
                    "Access check: document seller authority, granted accounting and bank scopes, permitted recipients, retention period, and revocation procedure before ingestion.",
                    "Reconciliation check: tie every imported period to source totals, explain material exceptions, and obtain QoE accountant review of proposed earnings adjustments.",
                    "Cash check: preserve the canonical profit basis, model principal separately, and test actual lender covenants and working-capital needs before fixing purchase terms.",
                ],
            },
        },
        {
            "heading": "4. Convert diligence evidence into a bounded 100-day operating system",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "At signing, convert unresolved diligence findings into "
                    "a transition register rather than leaving them "
                    "inside a report. Every item needs an "
                    "operating consequence, accountable person, due date, "
                    "supporting artifact, and escalation threshold. A "
                    "customer concentration finding becomes a retention "
                    "conversation owned by the operating manager; "
                    "a covenant becomes a scheduled calculation "
                    "owned by the controller; a permit condition "
                    "becomes an agency-confirmed task reviewed by "
                    "counsel. During days 1–30, stabilize access, "
                    "cash visibility, payroll, customer communication, "
                    "and essential vendor payments. During days "
                    "31–60, close the first repeatable monthly "
                    "reporting cycle and resolve inherited account "
                    "mapping errors. During days 61–100, automate "
                    "only workflows that already reconcile manually. "
                    "Do not migrate accounting systems simply "
                    "because the integration contractor prefers "
                    "another platform. Require a documented "
                    "operating benefit and a reversible migration "
                    "plan. Keep the four delivery employees "
                    "focused on service continuity, collecting "
                    "only the operational evidence needed for "
                    "exception resolution. P7 succeeds when "
                    "the acquired business keeps customers "
                    "and produces dependable records, not "
                    "when the acquisition desk displays "
                    "the largest collection of dashboards. "
                    "Preserve the seller's original records "
                    "through the agreed retention period."
                ),
                (
                    "Refresh evidence according to decision exposure. "
                    "Bank liquidity may need daily review, "
                    "accounting exceptions weekly review, and "
                    "formal ledger reconciliations monthly review. "
                    "Use lender reporting deadlines and "
                    "license renewal dates rather than an "
                    "arbitrary universal schedule. Repeat lien "
                    "and litigation searches at counsel-directed "
                    "transaction milestones; repeatedly downloading "
                    "annual Census releases adds no "
                    "information. Record stale-source warnings "
                    "separately from actual adverse findings. "
                    "An unavailable portal is a retrieval "
                    "exception, not evidence that a "
                    "license expired. Maintain replayable "
                    "imports and test recovery from "
                    "a revoked token, corrupted file, "
                    "changed column name, and interrupted "
                    "download. Track exception age, unreconciled "
                    "dollars, connector failures, and "
                    "customer-retention actions completed, "
                    "rather than celebrating API-call "
                    "volume. The controller should "
                    "be able to reproduce the "
                    "monthly cash bridge without "
                    "the contractor being online. "
                    "Store current runbooks alongside "
                    "access inventories, backup locations, "
                    "and credential-rotation responsibilities. "
                    "Remove departed seller and "
                    "contractor access promptly while "
                    "preserving required records. This "
                    "turns back-office automation into "
                    "durable operating capacity instead "
                    "of a fragile dependency on "
                    "one technically skilled person "
                    "or a forgotten personal account."
                ),
                (
                    "Measure the information edge against the "
                    "same scorecard throughout ownership. "
                    "Conservative and Base retain seven "
                    "full-time employees plus three "
                    "contractors; Scaled permits eight "
                    "full-time employees plus four "
                    "contractors, totaling twelve people. "
                    "The larger case is a "
                    "separate operating scenario, not "
                    "permission to quietly expand "
                    "the Base pod. Put subscription "
                    "fees, connector maintenance, "
                    "specialist retainers, and reporting "
                    "labor inside the expense "
                    "model supporting each margin. "
                    "If those costs were omitted, "
                    "show the resulting variance "
                    "rather than claiming that "
                    "automation preserves the stated "
                    "profit automatically. Keep the "
                    "$200,000–$1,000,000 startup-capital "
                    "range distinct from annual "
                    "sales, owner profit, and "
                    "borrowed acquisition principal. "
                    "Evaluate tools by fewer "
                    "unresolved liabilities, faster "
                    "reconciled closes, earlier "
                    "attrition detection, and "
                    "better-supported financing "
                    "decisions. None of those "
                    "benefits creates revenue "
                    "until the operating "
                    "business actually earns "
                    "recognized sales. Review "
                    "the seven plays "
                    "quarterly and retire "
                    "datasets that no "
                    "longer change a "
                    "decision. The desk's "
                    "advantage is a "
                    "short, defensible path "
                    "from source evidence "
                    "to action, maintained "
                    "within the team's "
                    "real capacity and "
                    "the debt structure's "
                    "actual cash demands."
                ),
            ],
            "table": {
                "caption": "Four operating cadences that preserve the ten-person Base pod",
                "headers": [
                    "Cadence and evidence-driven operating objective",
                    "Named owner within the existing team",
                    "Required output and concrete diagnostic measures",
                    "Escalation rule and explicit capacity boundary",
                ],
                "rows": [
                    [
                        "Daily liquidity review protects payroll and essential vendor continuity",
                        "Controller prepares the cash view and owner decides payment priorities",
                        "Produce available cash, upcoming obligations, blocked settlements, and documented retrieval exceptions",
                        "Escalate projected cash shortfalls immediately without diverting delivery employees into bookkeeping",
                    ],
                    [
                        "Weekly exception review connects all seven mapped operator plays",
                        "Owner chairs a short review with controller and operating manager",
                        "Resolve aged evidence questions, customer retention tasks, and accountable next actions",
                        "Bring contractors only for assigned specialist issues within their contracted hours",
                    ],
                    [
                        "Monthly close review validates records and actual lender reporting obligations",
                        "Controller owns reconciliation with scoped assistance from the QoE accountant",
                        "Publish reconciled sales, margin variance, cash bridge, and covenant calculations",
                        "Pause unreliable dashboard outputs until control totals and material exceptions reconcile",
                    ],
                    [
                        "Quarterly tooling review removes unused feeds and fragile access dependencies",
                        "Owner reviews costs while integration contractor demonstrates documented recovery procedures",
                        "Record decision utility, subscription expense, access inventory, and successful import replay",
                        "Retire redundant products before adding recurring costs or expanding the staffing model",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Scope the target and evidence rights",
                    "action": "Create the jurisdiction map, seven-play assignment, and seller-authorized data request.",
                    "detail": "Controller records legal identifiers and recipients; counsel specifies search coverage; owner limits active files to available review capacity.",
                },
                {
                    "step": 2,
                    "title": "Capture and normalize without destroying provenance",
                    "action": "Retrieve permitted source artifacts, hash originals, and import versioned records into the evidence ledger.",
                    "detail": "Integration contractor implements bounded retries and duplicate controls; controller quarantines incomplete batches and verifies source control totals.",
                },
                {
                    "step": 3,
                    "title": "Reconcile earnings, liabilities, and debt cash flows",
                    "action": "Trace recognized sales, challenge add-backs, and build a separate principal and working-capital bridge.",
                    "detail": "QoE accountant supports adjustments, counsel resolves legal findings, and lender-specific covenant definitions govern financing calculations.",
                },
                {
                    "step": 4,
                    "title": "Transfer findings into the first 100 days",
                    "action": "Assign each surviving exception to a named operating owner with a deadline and supporting evidence.",
                    "detail": "Operating manager protects customer continuity while controller runs reporting; automate only reconciled processes and remove obsolete access.",
                },
            ],
        },
    ],
    "pull_quote": "The acquisition edge is not more data; it is fewer unsupported assumptions between a public record, a bank receipt, and the price you pay.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create one jurisdiction and identity map per target, including former names, operating sites, filing offices, and license issuers.",
        "Assign every source and finding to P1 origination, P2 identity, P3 liabilities, P4 revenue, P5 QoE, P6 financing, or P7 turnaround.",
        "Implement a capped enrichment waterfall that verifies official identity before purchasing contact credits and preserves rejected matches.",
        "Obtain authorized accounting and bank evidence, retain hashed originals, and reconcile every imported period to documented source totals.",
        "Preserve the $60,000, $243,750, and $540,000 canonical profit cases while modeling principal repayments and working-capital cash needs separately.",
        "Launch the 100-day exception register within the 7 FT + 3 C Base pod and require a reproducible monthly close before expanding automation.",
    ],
    "statutory_citations": [
        {
            "title": "UCC sections 9-301 and 9-307 — Governing law and location of debtor",
            "url": "https://www.law.cornell.edu/ucc/9/9-301",
            "relevance": "Article 9 supplies the framework for locating relevant filing jurisdictions; consult the applicable state's enacted provisions, debtor-location rules, and collateral-specific exceptions.",
        },
        {
            "title": "UCC section 9-503 — Name of debtor and secured party",
            "url": "https://www.law.cornell.edu/ucc/9/9-503",
            "relevance": "Debtor-name requirements inform official lien-search design; legal names, entity records, and state search procedures matter more than a trade-name web search.",
        },
        {
            "title": "26 U.S.C. 6103 — Confidentiality and disclosure of returns and return information",
            "url": "https://www.law.cornell.edu/uscode/text/26/6103",
            "relevance": "Federal tax returns are not ordinary public-registry data; use seller-provided records and applicable authorized disclosure procedures.",
        },
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "A consumer report requires an applicable permissible purpose; ordinary interest in acquiring a business does not create unrestricted access to personal credit information.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Commercial email sourcing must address truthful transmission information, required identification and address details, and functioning opt-out procedures.",
        },
        {
            "title": "13 CFR Part 120 — Business loans",
            "url": "https://www.ecfr.gov/current/title-13/chapter-I/part-120",
            "relevance": "SBA financing analysis must reflect applicable program regulations together with current agency procedures, lender requirements, and transaction-specific terms.",
        },
        {
            "title": "31 U.S.C. 3727 — Assignments of claims",
            "url": "https://www.law.cornell.edu/uscode/text/31/3727",
            "relevance": "Federal receivables require review of statutory assignment restrictions and exceptions; an award-data match alone establishes neither assignability nor collected revenue.",
        },
        {
            "title": "48 CFR 42.1204 — Applicability of novation agreements",
            "url": "https://www.ecfr.gov/current/title-48/chapter-1/subchapter-G/part-42/subpart-42.12/section-42.1204",
            "relevance": "For targets holding federal contracts, assess whether the transaction requires government recognition of a successor contractor instead of assuming contract continuity.",
        },
    ],
}
