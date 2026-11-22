from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-and-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small subject-to & wraparound note arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "County Instruments, ATTOM Enrichment, NMLS Verification, RMLO Underwriting, and Licensed-Servicer Reconciliation",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #35, Subject-To & Wraparound Note Arbitrage, ranks #09 of 36 "
        "with a 90/100 Money-to-Manpower Score. This directory supplies the evidence "
        "layer supporting the volume's 11 mapped plays: recorded ownership, debt "
        "provenance, borrower qualification, protected escrow movements, and verified "
        "servicing cash flows. Sixteen named resources form a staged enrichment "
        "waterfall, not a license to treat estimated equity as executable spread. "
        "The canonical annual owner profits are $28,000 Conservative, $190,000 Base, "
        "and $442,000 Scaled. Revenue means retained upfront spreads and annual "
        "wraparound interest margin, excluding home value and pass-through debt "
        "service. Build one traceable property record, purchase deeper evidence only "
        "when justified, and stop funding when documentary conflicts or payment "
        "exceptions remain unresolved."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual operator revenue from retained spreads; property value and pass-through debt service excluded.",
            "note": "28% net margin; $28,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Base",
            "value": "$475,000",
            "context": "Annual operator revenue from retained spreads; property value and pass-through debt service excluded.",
            "note": "40.0% net margin; $190,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Scaled",
            "value": "$850,000",
            "context": "Annual operator revenue from retained spreads; property value and pass-through debt service excluded.",
            "note": "52% net margin; $442,000 annual owner net profit; 2 FT + 4 C, six people total.",
        },
    ],
    "sections": [
        {
            "heading": "1. Anchor every opportunity to recorded instruments, not lead-list estimates",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a county-specific evidence map before buying a national lead subscription. "
                    "For each target county, record the recorder's document coverage, assessor parcel format, "
                    "tax collector billing calendar, foreclosure procedure, and courthouse retrieval route. "
                    "An assessor identifies taxable property; a recorder indexes instruments; neither establishes "
                    "a current mortgage balance or insurable title. Link county, parcel identifier, legal "
                    "description, instrument number, recording date, and source retrieval timestamp. Preserve "
                    "leading zeros and original owner spellings. Condominium units, parent parcels, and "
                    "subdivided lots require separate relationship records rather than aggressive address "
                    "deduplication. A notice of default is a dated procedural event, not evidence that "
                    "the borrower wants an offer or that a sale remains scheduled. Retrieve the actual "
                    "notice, then verify postponements and cancellations through the responsible trustee "
                    "or court. In Texas, nonjudicial sale mechanics under Property Code section 51.002 "
                    "make timing material; the posted date does not substitute for transaction-specific "
                    "review. Assign every lead an evidence state: discovered, document retrieved, owner "
                    "confirmed, debt verified, or executable. Only the final state may enter acquisition "
                    "cash planning, and that state still requires a current title commitment and "
                    "transaction-specific closing review."
                ),
                (
                    "Use the directory in this section and the next as one sixteen-resource waterfall. "
                    "Rows one through eight establish public-record provenance; rows nine through sixteen "
                    "add paid enrichment, regulatory verification, and execution diagnostics. County systems "
                    "differ, so a named portal is a deployment example, not nationwide coverage. "
                    "NYC ACRIS supplies recorded property documents for its covered boroughs, while "
                    "Staten Island requires its separate recording channel. Maricopa recorder and assessor "
                    "records illustrate why instrument ownership and parcel assessment should be joined "
                    "without assuming identical refresh schedules. Harris County foreclosure postings "
                    "are useful event signals, but the trustee remains the source for current sale "
                    "instructions. Never interpret absence from one index as absence of liens. Federal "
                    "tax liens, judgments, probate interests, municipal assessments, and bankruptcy "
                    "proceedings may require separate searches and title examination. Store source "
                    "coverage explicitly, including counties and years searched. Where a portal "
                    "provides only a browser interface, use that interface or purchase authorized "
                    "bulk access; do not manufacture an undocumented scraping entitlement. A "
                    "restricted portal, broken image link, or missing instrument triggers a clerk "
                    "request or title-company retrieval, not a guessed field silently carried into "
                    "an investment memorandum."
                ),
                (
                    "Budget retrieval by expected decision value. An illustrative first pass of 400 "
                    "records at $0.25 each costs $100; reviewing 40 resulting candidates for ten "
                    "minutes each at $45 per hour adds $300. The $400 screen therefore costs "
                    "$10 per reviewed candidate before title, underwriting, or closing expenses. These "
                    "are internal planning assumptions, not quoted vendor prices. Require a written "
                    "commercial quote before substituting purchased API usage into that model. A "
                    "recorded $210,000 mortgage from six years ago does not establish today's payoff: "
                    "modifications, arrears, advances, partial releases, and subordinate liens can "
                    "reverse apparent equity. Obtain seller-authorized statements, reinstatement figures "
                    "where relevant, and payoff information with expiration dates through accepted "
                    "channels. Distinguish an interest rate printed in an original note from an "
                    "adjustable rate currently effective. The low-rate acquisition thesis survives "
                    "only if actual payment obligations, insurance, taxes, and acceleration exposure "
                    "are affordable together. Under 12 U.S.C. 1701j-3, do not assume an ordinary "
                    "subject-to acquisition or wrap sale falls within a protected transfer exception. "
                    "If acceleration cannot be absorbed through a documented refinance, payoff, "
                    "or sale plan, reject the acquisition rather than assigning the risk a "
                    "zero-dollar spreadsheet value."
                ),
            ],
            "table": {
                "caption": "Named Resource Directory, Part A: Eight Public-Record Evidence Sources",
                "headers": [
                    "Named resource and precise access route",
                    "Cost tier and evidence obtained",
                    "Refresh latency and request handling",
                    "Fallback source and operator decision",
                ],
                "rows": [
                    [
                        "01. NYC ACRIS: open a836-acris.nyc.gov and search borough, block, lot, or document identifier.",
                        "Public browser searching is free; certified copies follow applicable clerk charges and ordering procedures.",
                        "Search at underwriting and before closing; indexing follows recording rather than guaranteed instant publication.",
                        "Request recorder copies through the relevant office; use Richmond County channels for Staten Island.",
                    ],
                    [
                        "02. Maricopa County Recorder: use recorder.maricopa.gov recorded-document search by party or instrument number.",
                        "Public index access supports discovery; document products and certifications follow the recorder's posted charges.",
                        "Recheck newly recorded instruments before funding; use permitted browser searches rather than unrestricted automated polling.",
                        "Order missing instruments from recorder staff or obtain the title company's documented instrument retrieval.",
                    ],
                    [
                        "03. Maricopa County Assessor: search mcassessor.maricopa.gov by parcel, owner name, or situs address.",
                        "Public parcel lookup supplies assessment attributes; assessment values do not establish current market proceeds.",
                        "Assessment and ownership updates follow office processing; retain effective dates separately from retrieval dates.",
                        "Resolve parcel conflicts against recorded legal descriptions, assessor staff responses, and a current survey.",
                    ],
                    [
                        "04. Harris County Tax Office: use hctax.net property-tax account search for billed balances.",
                        "Public account lookup supports tax screening; obtain authoritative settlement figures through applicable tax-office procedures.",
                        "Balances can change with payments and penalties; refresh before closing and after material payment events.",
                        "Request written tax figures and have the closing agent reconcile taxing jurisdictions and exemptions.",
                    ],
                    [
                        "05. Harris County Clerk: access cclerk.hctx.net foreclosure notices through its real-property search services.",
                        "Public notice access identifies posted proceedings; certified evidence and additional retrieval can incur charges.",
                        "Review active files each business day; avoid rapid repeated searches and confirm actual sale status.",
                        "Contact the named trustee and retrieve applicable court records before relying on a scheduled sale.",
                    ],
                    [
                        "06. PACER: register at pacer.uscourts.gov and search the Case Locator and relevant court docket.",
                        "Metered electronic access follows PACER's published fee schedule; track project charges and applicable fee waivers.",
                        "Docket activity appears after filing and processing; check critical matters again immediately before funding.",
                        "Use the bankruptcy court clerk or counsel for identity conflicts, restricted documents, and stay analysis.",
                    ],
                    [
                        "07. FEMA Map Service Center: search msc.fema.gov by address and retrieve effective map products.",
                        "Public flood-map access is free; separate elevation work and insurance quotations carry transaction-specific costs.",
                        "Refresh when maps change and during underwriting; compare effective panels with pending revisions where available.",
                        "Obtain lender flood determination and an insurance quote; inspect elevation evidence when mapped boundaries conflict.",
                    ],
                    [
                        "08. Texas Secretary of State SOSDirect: enter sos.state.tx.us and select SOSDirect UCC searches.",
                        "Account-based searches and copies carry posted charges; certified results support targeted personal-property lien examination.",
                        "Search debtor names using correct legal identity; purchase authorized results instead of repeated speculative queries.",
                        "Have counsel select the proper filing jurisdiction; supplement with county real-property and fixture-filing searches.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy the missing fact, not another overlapping lead list",
                "body": "A veteran desk pays for evidence that changes funding decisions and preserves the chain connecting every number to its source.",
                "items": [
                    "Order the recorded modification before modeling a low-rate spread; original mortgage metadata can conceal changed maturity or payment terms.",
                    "Keep trustee postponement evidence beside the foreclosure notice; a stale sale date can corrupt both outreach priority and cancellation timing.",
                    "Store the exact parcel and legal description returned by title; street-address normalization must never merge adjacent collateral.",
                    "Separate seller arrears from recurring debt service so a temporary reinstatement burden does not masquerade as permanent monthly margin.",
                ],
            },
        },
        {
            "heading": "2. Enrich selectively and verify the people controlling origination and servicing",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Design enrichment as a sequence of questions, not a purchase of every field "
                    "a vendor offers. First resolve parcel identity through county records. Next "
                    "request property and recorded-mortgage attributes from ATTOM or an alternative "
                    "contracted provider. Then obtain the specific missing document through DataTree "
                    "or the recorder. Reserve title examination, borrower underwriting, insurance "
                    "quotes, and servicing setup for transactions that survive those checks. ATTOM "
                    "Property API, CoreLogic Trestle, and DataTree serve different access and coverage "
                    "needs; Trestle is an authorized listing-data channel, not a universal lien "
                    "registry. BatchData contact enrichment is a lead-contact aid, not proof of "
                    "ownership or permission to contact someone through every channel. Reject "
                    "contact matches that cannot be tied to the intended party through an "
                    "independent signal. Vendor-estimated equity and mortgage balances remain estimates "
                    "even when delivered through a polished API. Keep separate fields for "
                    "observed document facts, vendor estimates, seller representations, and verified "
                    "servicer figures. A field-level source ledger lets the operator replace "
                    "a weak estimate without erasing the historical basis of an earlier decision. "
                    "When two providers disagree, request the primary instrument instead of "
                    "averaging incompatible values into apparent precision."
                ),
                (
                    "Verify the originator and servicer before sending an owner-occupant buyer into "
                    "the workflow. Use NMLS Consumer Access to inspect the individual RMLO, sponsoring "
                    "company, license status, and relevant state authority; retrieve the underlying "
                    "state regulator record when the scope is unclear. NMLS identifiers are "
                    "identifiers, not a universal authorization to perform every activity in every "
                    "jurisdiction. This desk routes every owner-occupant wrap buyer through a "
                    "licensed RMLO and documented repayment analysis, while counsel determines "
                    "the transaction's precise federal and state coverage. Regulation Z section "
                    "1026.43 sets ability-to-repay requirements for covered transactions; exemptions "
                    "and seller-financer provisions require specific analysis rather than slogans "
                    "about a permitted annual deal count. Texas adds wrap-mortgage requirements "
                    "under Finance Code Chapter 159, and Property Code section 5.016 addresses "
                    "specified transfers involving existing liens. Hire a third-party servicer "
                    "licensed where required, verify that status, and document responsibility "
                    "for underlying payments, escrow administration, statements, complaints, and "
                    "exception escalation. A vendor's ability to collect ACH payments does not "
                    "establish authority to service a particular wrap loan. Obtain a sample "
                    "report demonstrating both buyer collections and independently verified "
                    "underlying mortgage disbursements before signing the servicing agreement."
                ),
                (
                    "Keep borrower qualification outside the public-record enrichment lake. Income "
                    "documents, consumer reports, account credentials, and identification belong in "
                    "restricted systems with purpose-specific access and retention schedules. "
                    "15 U.S.C. 1681b governs permissible purposes for consumer reports; a property "
                    "lead alone does not establish one. Let the authorized RMLO obtain the "
                    "necessary reports through its established process and return the decision "
                    "evidence needed for the transaction. Track applicable adverse-action and "
                    "record-retention responsibilities explicitly rather than assuming the contractor "
                    "owns every obligation. For outreach, check applicable calling restrictions "
                    "and suppression requirements before using enriched phone numbers. On the "
                    "technical side, Postman collections should reference environment-managed "
                    "credentials, contain synthetic test payloads, and exclude live borrower "
                    "documents from shared workspaces. A local SQLite ledger can retain "
                    "source hashes, retrieval timestamps, document identifiers, and reconciliation "
                    "states without duplicating sensitive files. An illustrative waterfall that "
                    "screens 100 parcels, purchases 20 document packages, and commissions five "
                    "title reviews should report spend at each transition. If a package "
                    "costs an assumed $18, that stage costs $360, not $1,800 across all "
                    "initial leads. Replace the assumption with contracted pricing and stop "
                    "purchasing enrichment when the underlying opportunity fails."
                ),
            ],
            "table": {
                "caption": "Named Resource Directory, Part B: Eight Commercial, Regulatory, and Diagnostic Tools",
                "headers": [
                    "Named resource and precise access route",
                    "Cost tier and permitted use",
                    "Refresh latency and rate-limit hygiene",
                    "Fallback source and evidence requirement",
                ],
                "rows": [
                    [
                        "09. ATTOM Property API: obtain an account at attomdata.com and call documented endpoints using issued credentials.",
                        "Commercial subscription or contracted usage pricing applies; confirm geography, fields, storage rights, and permitted redistributions.",
                        "Underlying sources have different lags; follow contracted quotas, cache permitted responses, and respect retry instructions.",
                        "Replace disputed mortgage attributes with recorded instruments and seller-authorized current statements from the actual servicer.",
                    ],
                    [
                        "10. First American DataTree: subscribe through datatree.com and retrieve indexed property documents within contracted coverage.",
                        "Commercial seat, package, or negotiated access costs apply; confirm image availability before purchasing broad coverage.",
                        "Index and image latency varies by county; avoid duplicate purchases by caching document identifiers lawfully.",
                        "Request the instrument directly from the recorder or through the closing title company's examination team.",
                    ],
                    [
                        "11. CoreLogic Trestle: request access through trestle.corelogic.com for authorized RESO Web API listing feeds.",
                        "Contracted platform and listing entitlements determine cost; property listing access requires the relevant data authorization.",
                        "Use documented incremental synchronization and provider quotas; listing changes and sold records have feed-specific timing.",
                        "Obtain permitted comparable sales through an authorized broker, appraiser, or county recorded-sale evidence where available.",
                    ],
                    [
                        "12. BatchData: obtain credentials through batchdata.com and use contracted property or contact enrichment endpoints.",
                        "Commercial usage pricing depends on products and volume; confirm contact provenance and permitted outreach-related processing.",
                        "Contact freshness differs from property-record freshness; log retrieval dates and throttle within account-specific limits.",
                        "Use owner-provided contact details or independently verified correspondence; discard ambiguous matches rather than expanding outreach.",
                    ],
                    [
                        "13. NMLS Consumer Access: search nmlsconsumeraccess.org by individual name, company name, or NMLS identifier.",
                        "Public verification access is free; inspect state-specific status rather than relying on promotional license claims.",
                        "Check at onboarding and before origination; use public search interfaces without presuming bulk extraction rights.",
                        "Ask the relevant state regulator to resolve sponsorship, authority, disciplinary history, or apparent status conflicts.",
                    ],
                    [
                        "14. Texas Department of Savings and Mortgage Lending: use sml.texas.gov licensing and mortgage-company verification links.",
                        "Public regulator resources support authority checks; verify whether this department regulates the specific proposed activity.",
                        "Recheck authority before engagement and upon notices; retain dated results instead of repeatedly polling public pages.",
                        "Contact the responsible regulator directly, including another agency when the activity falls outside this department's jurisdiction.",
                    ],
                    [
                        "15. Postman: use the desktop application with vendor-documented endpoints and a dedicated test environment.",
                        "Free and paid product tiers exist; select features deliberately and keep production borrower records outside shared collections.",
                        "Run scheduled synthetic checks within provider quotas; implement capped retries and honor applicable Retry-After responses.",
                        "Reproduce failures with Python urllib.request using redacted fixtures and retain response status plus correlation identifiers.",
                    ],
                    [
                        "16. Python sqlite3 and hashlib: build a local evidence ledger using standard-library database and digest functions.",
                        "Standard-library tooling has no separate license fee; budget encrypted storage, backups, maintenance, and operator review time.",
                        "Update after each authorized ingest; hash snapshots and run daily reconciliation against expected source-event counts.",
                        "Restore verified backups and reconcile source documents manually when database checks or ingestion totals fail.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Resolve collateral identity",
                    "action": "Join county parcel identifiers to recorded legal descriptions before ordering paid enrichment.",
                    "detail": "Route unit-number conflicts, split parcels, and multiple owner matches to human review; preserve every original source identifier.",
                },
                {
                    "step": 2,
                    "title": "Purchase only decision-changing evidence",
                    "action": "Order missing instruments and current debt evidence after the initial screen passes.",
                    "detail": "Log contracted unit cost, retrieval timestamp, coverage period, and the precise underwriting question each purchase resolves.",
                },
                {
                    "step": 3,
                    "title": "Verify authorized counterparties",
                    "action": "Check RMLO, company, servicer, and relevant state authority before transmitting restricted transaction records.",
                    "detail": "Retain dated verification results and assign responsibility for underwriting, servicing, disclosures, notices, and record retention.",
                },
                {
                    "step": 4,
                    "title": "Publish a bounded evidence packet",
                    "action": "Generate a deal packet containing verified facts, unresolved exceptions, and expiration-sensitive documents.",
                    "detail": "Keep consumer reports and identity documents in their restricted systems; expose only the necessary decision evidence to the acquisition desk.",
                },
            ],
        },
        {
            "heading": "3. Build an auditable event pipeline and protect every escrow advance",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a small, inspectable pipeline before commissioning a warehouse. Python "
                    "urllib.request handles authorized HTTP retrieval; csv and json parse documented "
                    "exports; sqlite3 stores normalized records; hashlib fingerprints the retrieved "
                    "bytes. Maintain source, parcel, instrument, obligation, event, counterparty, "
                    "and exception tables. Give each ingest a run identifier and preserve "
                    "the source timestamp separately from the local fetch timestamp. Use "
                    "idempotency keys such as county plus instrument number plus document "
                    "version so retries cannot duplicate liens or funding instructions. "
                    "Explicitly represent pending verification, source unavailable, and conflicting "
                    "evidence as workflow states rather than invented numbers. Reject malformed "
                    "currency fields, impossible dates, and parcel joins that increase the "
                    "candidate count unexpectedly. A local scheduler may request updates daily, "
                    "but it cannot make a county source update daily. On HTTP 429, "
                    "respect the documented retry interval; on repeated authentication failures, "
                    "stop and repair credentials instead of cycling identities. Apply bounded "
                    "exponential backoff with jitter for transient failures and send exhausted "
                    "jobs to an exception queue. Every morning, compare expected files, "
                    "received files, parsed rows, unique parcels, and newly opened exceptions. "
                    "A green network response with zero usable records is an operational "
                    "failure, not a successful refresh."
                ),
                (
                    "The mapped play earnest_money_gator_escrow_lending belongs to TRACK_1 and needs "
                    "its own escrow-control ledger. Advance $2,500–$25,000 refundable-contingency "
                    "earnest-money deposits directly to title escrow under documented joint-venture "
                    "or promissory protections, with security recorded or perfected where legally "
                    "appropriate. Negotiate a 15%–30% share of an earned assignment fee or "
                    "a lawful fixed return; neither label resolves licensing, usury, or "
                    "enforceability questions by itself. For concrete unit math, a $5,000 "
                    "advance paired with a 20% share of an earned $15,000 assignment "
                    "fee produces $3,000 of contractual fee participation before expenses "
                    "and loss exposure. The $5,000 principal repayment is separate from "
                    "that income. If no assignment fee is earned, the modeled participation "
                    "is zero, and principal recovery follows the governing documents. Store "
                    "the purchase contract, escrow acknowledgment, deposit receipt, contingency "
                    "language, cancellation deadline, notice method, release conditions, and "
                    "authorized signers. Verify wiring instructions by calling a previously "
                    "validated escrow number rather than one supplied in a last-minute email. "
                    "Do not equate a portal balance with a legal right to withdraw "
                    "funds. Refundability depends on timely valid contingency exercise and "
                    "the escrow release terms, including any required signatures or dispute process."
                ),
                (
                    "Convert contract deadlines into explicit events with local time zones, "
                    "notice recipients, required delivery methods, and evidence of receipt. "
                    "A reminder two days before expiration is useful only if someone "
                    "owns the cancellation decision and can deliver the prescribed notice. "
                    "Maintain separate fields for requested cancellation, delivered cancellation, "
                    "acknowledged cancellation, agreed release, and returned cash. If escrow "
                    "disputes arise, freeze additional advances, seek timely authorized "
                    "cancellation, and pursue counsel-reviewed escrow release or contractual "
                    "remedies. Never solve a disputed deposit by substituting another "
                    "counterparty's funds. For note servicing, ingest collections and disbursements "
                    "as separate events and reconcile them to the underlying lender's "
                    "statement, tax records, and insurance evidence. A buyer payment does "
                    "not prove the senior lien was paid. Flag a missing lender "
                    "confirmation immediately and obtain a documented explanation from the "
                    "servicer. Keep escrow principal movements out of revenue reports, "
                    "and do not add the illustrative assignment participation to the "
                    "canonical volume scenarios without a reconciled allocation. An audit "
                    "trail should answer who authorized each movement, which contractual "
                    "condition permitted it, when cash cleared, and which external "
                    "record independently confirms the result. That discipline makes a "
                    "small desk resilient to both clerical errors and counterparties "
                    "who describe requested payments as completed payments."
                ),
            ],
            "table": {
                "caption": "Five Pipeline Controls Connecting Source Evidence to Cash Authorization",
                "headers": [
                    "Event or control being tested",
                    "Required record and unit-level measurement",
                    "Failure trigger requiring human intervention",
                    "Fallback action and closure evidence",
                ],
                "rows": [
                    [
                        "A new recorded instrument enters the collateral evidence ledger.",
                        "Store county, instrument identifier, retrieval timestamp, document hash, and linked legal description.",
                        "Instrument identity duplicates another record or legal descriptions disagree across linked parcels.",
                        "Quarantine the relationship and obtain recorder or title confirmation before changing the ownership model.",
                    ],
                    [
                        "An authorized vendor request fails during the daily enrichment batch.",
                        "Record response status, permitted retry interval, attempt count, and account-specific usage budget.",
                        "Repeated authentication failures or exhausted transient retries leave required underwriting evidence stale.",
                        "Stop automated requests and use contracted exports or primary-source retrieval with documented provenance.",
                    ],
                    [
                        "A $5,000 earnest-money advance is proposed for title escrow.",
                        "Verify executed protections, confirmed escrow instructions, contingency deadlines, and independent callback evidence.",
                        "Escrow recipient changes unexpectedly or contract language does not support the assumed refund path.",
                        "Withhold funding until counsel and escrow resolve the discrepancy through documented authorized channels.",
                    ],
                    [
                        "A contingency deadline approaches while the assignment remains unresolved.",
                        "Track deadline timezone, authorized decision maker, delivery method, and acknowledgment of any notice.",
                        "Cancellation has been discussed but required delivery evidence or valid contractual grounds remain missing.",
                        "Freeze further advances and pursue timely authorized cancellation followed by documented escrow-release procedures.",
                    ],
                    [
                        "A wrap buyer payment clears but underlying disbursement remains unverified.",
                        "Match servicing receipt, senior-loan payment confirmation, escrow allocation, and applicable statement periods.",
                        "Servicer reports a payment without independent lender evidence or a supported settlement-timing explanation.",
                        "Escalate the exception immediately and document payment correction, account posting, and revised cash reconciliation.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before money or borrower data moves",
                "body": "Each check requires attributable evidence and an assigned reviewer; a checked box without the supporting record is incomplete.",
                "items": [
                    "Collateral check: reconcile deed, legal description, title commitment, current debt terms, and any active foreclosure or bankruptcy issue.",
                    "Origination check: verify RMLO and company authority, applicable repayment analysis, state wrap requirements, and the buyer's documented underwriting result.",
                    "Escrow check: confirm the actual recipient independently, execute the advance protections, and calendar every contingency and release requirement.",
                    "Servicing check: test buyer collection, underlying-payment confirmation, tax and insurance reconciliation, exception ownership, and acceleration-response liquidity.",
                ],
            },
        },
        {
            "heading": "4. Diagnose retained spread and reconcile tooling costs to the canonical scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build dashboards around retained economics rather than impressive collateral "
                    "totals. The canonical Conservative case contains $100,000 annual operator "
                    "revenue, $72,000 total modeled costs, and $28,000 owner net profit "
                    "at 28%. Base contains $475,000 revenue, $285,000 costs, and "
                    "$190,000 profit at 40.0%. Scaled contains $850,000 revenue, "
                    "$408,000 costs, and $442,000 profit at 52%. Teams remain "
                    "1 FT plus 3 contractors, 1 FT plus 3 contractors, and "
                    "2 FT plus 4 contractors respectively. Although the scorecard "
                    "labels its top line gross revenue, that line already represents "
                    "the operator's retained upfront spreads and annual wraparound "
                    "interest margin, not underlying home face value or pass-through "
                    "debt service. Do not apply another retained-share haircut without "
                    "an explicit model amendment. Reconcile applicable principal-versus-agent "
                    "presentation under ASC 606 with the accountant while distinguishing "
                    "interest accounting from service-fee revenue. The chapter supplies no "
                    "new loan-count assumption and does not manufacture a financing mix "
                    "to backsolve those totals. Keep the illustrative deal calculations "
                    "separate from the scorecard ledger. The stated $2,000–$12,000 "
                    "monthly operating range describes an operating envelope, not a "
                    "complete definition of every cost deducted in each annual "
                    "scenario; closing, acquisition, contractor, and loss-related costs "
                    "require their own mapped accounts."
                ),
                (
                    "For an illustrative performing loan, a $250,000 wrap balance at "
                    "8% annual interest produces $20,000 of first-year interest before "
                    "amortization effects; a $200,000 underlying balance at 4% produces "
                    "$8,000 on the same simplified basis. The $12,000 difference "
                    "is an interest-margin illustration, not cash available to distribute. "
                    "Actual scheduled payments include principal movements, and actual "
                    "interest depends on declining balances, payment dates, and loan "
                    "terms. Subtract servicing charges, unrecovered expenses, and allocated "
                    "operating costs when measuring contribution; keep tax and insurance "
                    "escrows segregated from spread. If illustrative servicing costs "
                    "$35 monthly, its annual $420 reduces that simplified margin "
                    "to $11,580 before other costs. These assumptions do not "
                    "replace the canonical scenarios. Stress the cash ledger with "
                    "missed buyer payments while the underlying mortgage remains "
                    "payable, and separately stress lender acceleration. A reserve "
                    "covering several monthly payments cannot necessarily repay the "
                    "senior principal on demand. Record the source, amount, "
                    "availability, and expiration of each proposed liquidity backstop. "
                    "If a refinance depends on future underwriting or a "
                    "property sale depends on optimistic pricing, show that "
                    "dependency openly and reduce commitments until a feasible "
                    "fallback exists."
                ),
                (
                    "Measure the data stack by prevented mistakes and completed evidence "
                    "cycles. Report cost per verified candidate, document-conflict rate, "
                    "stale-evidence count, time from seller authorization to current "
                    "debt confirmation, and days from servicer receipt to independently "
                    "verified underlying posting. Define thresholds locally from contract "
                    "deadlines and servicing agreements rather than presenting invented "
                    "industry standards. A useful daily board separates blocked "
                    "acquisitions, expiring contingencies, unverified disbursements, insurance "
                    "exceptions, and tax delinquencies. Assign a named role and "
                    "next action to every exception, then close it only when "
                    "the confirming evidence is attached. With $12,000–$65,000 "
                    "startup capital and a two-to-six-month first-deal horizon, "
                    "fixed software subscriptions can consume runway before any "
                    "retained spread arrives. Start with one county cluster, "
                    "one contracted enrichment provider, a title relationship, a "
                    "licensed RMLO, and a qualified third-party servicer. Add "
                    "another feed only after identifying the decision it improves "
                    "and measuring duplicate coverage. Review canceled deals as "
                    "carefully as closed ones: an inexpensive instrument retrieval "
                    "that exposes a modification or disputed lien may outperform "
                    "hundreds of extra contacts. The information edge is a "
                    "shorter, better-evidenced path from public signal to verified "
                    "obligation, not the largest database or the fastest "
                    "unreviewed offer."
                ),
            ],
            "table": {
                "caption": "Canonical Formula v2.0 Reconciliation and Two Diagnostic Unit Tests",
                "headers": [
                    "Scenario or diagnostic calculation being reconciled",
                    "Revenue basis or tested cash movement",
                    "Costs, profit, and staffing reconciliation",
                    "Operator interpretation and required fallback action",
                ],
                "rows": [
                    [
                        "Conservative annual case uses the canonical Formula v2.0 scorecard.",
                        "$100,000 retained operator revenue excludes home value and pass-through debt service.",
                        "$72,000 modeled costs leave $28,000 profit at 28%; staffing is 1 FT plus 3 contractors.",
                        "Preserve the exact scenario totals; map subscriptions and transaction expenses without counting pass-through collections.",
                    ],
                    [
                        "Base annual case uses the canonical Formula v2.0 scorecard.",
                        "$475,000 retained operator revenue excludes underlying principal and third-party debt-service collections.",
                        "$285,000 modeled costs leave $190,000 profit at 40.0%; staffing is 1 FT plus 3 contractors.",
                        "Reconcile every retained fee and interest-margin component before comparing actual performance against the annual plan.",
                    ],
                    [
                        "Scaled annual case uses the canonical Formula v2.0 scorecard.",
                        "$850,000 retained operator revenue remains separate from collateral value and escrow account balances.",
                        "$408,000 modeled costs leave $442,000 profit at 52%; staffing is 2 FT plus 4 contractors.",
                        "Scale only with verified payment controls and six-person responsibilities; added leads cannot substitute for servicing capacity.",
                    ],
                    [
                        "Illustrative earnest-money participation tests principal separation from earned income.",
                        "$5,000 advanced principal plus 20% of an earned $15,000 assignment fee yields $3,000 participation.",
                        "Principal repayment is separate; participation remains before expenses, loss exposure, and transaction-specific tax treatment.",
                        "If the assignment fails, freeze advances and follow authorized cancellation and counsel-reviewed release or remedy procedures.",
                    ],
                    [
                        "Illustrative annual interest spread tests servicing cost and amortization boundaries.",
                        "$250,000 at 8% less $200,000 at 4% gives $12,000 before amortization effects.",
                        "$35 monthly servicing equals $420 annually, leaving $11,580 before other expenses and actual-balance adjustments.",
                        "Use actual schedules for distributions; reserve for buyer default and separately assess senior-lender acceleration liquidity.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The edge is not finding a cheap mortgage; it is proving who owes what, who can move the money, and whether every underlying obligation was paid.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Build a county source map linking recorder, assessor, tax office, foreclosure channel, and title-company fallback to each target parcel.",
        "Configure the sixteen-resource waterfall with contracted costs, coverage dates, permitted request budgets, caching rights, and source-specific fallback procedures.",
        "Verify RMLO, company, and servicer authority for each operating state, then test the exact underwriting and underlying-payment evidence they will deliver.",
        "Create an escrow-advance ledger containing executed protections, independently verified wire instructions, contingency deadlines, notice evidence, and release conditions.",
        "Run daily ingestion and servicing diagnostics for duplicate instruments, stale debt figures, missing documents, unmatched payments, and expiring contractual rights.",
        "Reconcile retained revenue and modeled costs to $28,000, $190,000, and $442,000 annual owner profits without counting property value, escrow principal, or pass-through debt service.",
    ],
    "statutory_citations": [
        {
            "title": "12 U.S.C. 1701j-3 — Preemption of due-on-sale prohibitions",
            "url": "https://www.law.cornell.edu/uscode/text/12/1701j-3",
            "relevance": "Evaluate lender acceleration rights and the statute's specific protected-transfer categories; an ordinary subject-to or wrap transaction requires transaction-specific analysis.",
        },
        {
            "title": "12 CFR 1026.43 — Minimum standards for transactions secured by a dwelling",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-E/section-1026.43",
            "relevance": "Determine ability-to-repay coverage and preserve the underwriting evidence required for covered owner-occupant transactions.",
        },
        {
            "title": "12 CFR 1026.36 — Prohibited acts or practices and certain requirements for credit secured by a dwelling",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-E/section-1026.36",
            "relevance": "Review loan-originator provisions and narrowly conditioned seller-financer exclusions without treating a deal-count shorthand as complete qualification.",
        },
        {
            "title": "12 U.S.C. 5103 — License or registration required",
            "url": "https://www.law.cornell.edu/uscode/text/12/5103",
            "relevance": "Support SAFE Act originator verification and route the desk's owner-occupant wrap buyers through appropriately licensed RMLOs.",
        },
        {
            "title": "Texas Property Code section 5.016 — Conveyance of residential property encumbered by lien",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.016",
            "relevance": "Identify applicable notices, timing, and exceptions for covered conveyances involving an existing recorded lien.",
        },
        {
            "title": "Texas Finance Code Chapter 159 — Wrap Mortgage Loan Financing",
            "url": "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
            "relevance": "Evaluate Texas wrap-mortgage origination, disclosure, servicing, and related duties using the applicable statutory definitions and exemptions.",
        },
        {
            "title": "Texas Property Code section 51.002 — Sale of real property under contract lien",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.51.htm#51.002",
            "relevance": "Anchor Texas nonjudicial foreclosure-event monitoring to actual notice and sale procedures instead of stale aggregator dates.",
        },
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "Separate public property enrichment from consumer-report access and document the applicable permissible purpose before obtaining a report.",
        },
        {
            "title": "11 U.S.C. 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "Escalate relevant bankruptcy filings for counsel review before collection, foreclosure-related action, or reliance on an existing sale schedule.",
        },
    ],
}
