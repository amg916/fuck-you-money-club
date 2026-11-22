from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small specialty finance brokerage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "SEC Filing Triggers, UCC Searches, PACER Dockets, Borrower-Permissioned APIs, and State Credit Transfer Verification",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #20, Specialty Finance Brokerage, ranks #06 among 29 mapped plays "
        "with a Money-to-Manpower Score of 89/100. Its information edge comes from "
        "joining authoritative records to permissioned borrower evidence, not buying "
        "the largest contact list. This chapter specifies registry access, enrichment "
        "waterfalls, refresh controls, and lender-matrix diagnostics for equipment, "
        "receivables, SBA, bridge, litigation-facility, and transferable-credit opportunities. "
        "The canonical annual owner profits are $30,000 Conservative, $196,000 Base, "
        "and $450,000 Scaled; revenue means retained origination or referral fees, "
        "never funded principal. Three mapped plays become bounded operating workflows: "
        "SEC event sourcing, counsel-led litigation facility diligence, and verified "
        "state tax-credit placement. The desk wins by identifying financeable events "
        "quickly while refusing stale liens, unsupported medical-access pricing, and "
        "credits that cannot legally transfer."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained origination or referral fees; excludes loan principal",
            "note": "25% net margin; $30,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$560,000",
            "context": "Annual retained origination or referral fees; excludes loan principal",
            "note": "35.0% net margin; $196,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual retained origination or referral fees; excludes loan principal",
            "note": "45% net margin; $450,000 annual owner net profit; 3 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an authoritative directory before buying enrichment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a source register, not a prospect spreadsheet. Each "
                    "record needs a legal entity identifier, jurisdiction, retrieval "
                    "timestamp, source URL, document identifier, permitted use, and "
                    "named reviewer. Match SEC issuers by CIK, state entities by "
                    "filing number, properties by parcel identifier, and litigation "
                    "matters by court plus case number. Names alone fail when a "
                    "borrower uses several operating companies, a property sits in "
                    "a special-purpose entity, or a guarantor shares a common surname. "
                    "Store original downloads separately from normalized fields and "
                    "hash each artifact with SHA-256 so later changes remain visible. "
                    "The directory below separates source publication latency from "
                    "your polling schedule; checking every minute cannot accelerate "
                    "a county office that posts documents the following business "
                    "day. Public access also does not make unrestricted redistribution "
                    "permissible. Record portal terms, paid-search rights, and document "
                    "retention restrictions before exposing results to lenders. For "
                    "an equipment borrower, the minimum useful bundle is entity "
                    "status, borrower-authorized financial evidence, jurisdiction-correct "
                    "UCC results, and asset identification. For an acquisition bridge, "
                    "add property, litigation, and transaction evidence rather than "
                    "substituting a commercial confidence score for primary records."
                ),
                (
                    "Treat access prices as procurement facts with effective dates. "
                    "SEC data is free, but PACER retrieval, official UCC searches, "
                    "certified copies, and commercial API products have different "
                    "billing units. PACER generally charges $0.10 per page and caps "
                    "many individual documents at $3; the cap has exceptions, and "
                    "quarterly charges of $30 or less are waived under its published "
                    "policy. Measure actual retrieval counts instead of assigning "
                    "every lawsuit a fixed research cost. Middesk and Plaid require "
                    "product-specific commercial arrangements; request written "
                    "pricing for the exact verification or financial-data product "
                    "before modeling cost per application. A borrower-provided "
                    "statement is a fallback, not an equivalent substitute for a "
                    "live authorized connection: reconcile account ownership, "
                    "statement dates, and missing months explicitly. Likewise, an "
                    "aggregated lien search is a discovery aid, while the lender "
                    "may require an official search and later closing-date updates. "
                    "Apply a per-case research budget before enrichment begins. "
                    "If five prospective borrowers each consume $40 of paid "
                    "verification and only one signs an engagement, acquisition "
                    "research cost is $200 per engagement, before labor or marketing. "
                    "That denominator matters more than a vendor's cheapest advertised call."
                ),
                (
                    "Organize the waterfall around unanswered underwriting questions. "
                    "First resolve the legal entity through the relevant secretary "
                    "of state; then obtain permissioned bank or accounting evidence; "
                    "then order liens, property records, and specialized program "
                    "checks only when the proposed facility requires them. OFAC "
                    "screening should retain the list version, matching inputs, "
                    "and disposition of possible matches; a similar name is not "
                    "a confirmed identity. SBA historical loan data helps identify "
                    "lenders active in a geography or industry, but it cannot "
                    "establish current appetite, eligibility, or delegated authority. "
                    "NMLS Consumer Access covers participating licenses and entities, "
                    "not every commercial brokerage permission in every state. "
                    "Maintain a separate state activity matrix describing product, "
                    "borrower location, collateral location, compensation, and "
                    "applicable licensing requirements. Refresh lender appetite "
                    "through direct written confirmation and date every exception. "
                    "A practical six-field matrix records facility size, advance "
                    "basis, prohibited industries, minimum operating history, "
                    "geographic coverage, and required evidence. Add named contacts "
                    "and expected response times as operating fields. Never let "
                    "an enrichment vendor silently overwrite verified borrower "
                    "facts; preserve the conflicting value, its source, and the "
                    "review decision so another analyst can reconstruct the lender submission."
                ),
            ],
            "table": {
                "caption": "Eighteen named sources with access, pricing, latency, request controls, and evidence fallbacks",
                "headers": [
                    "Named source and specific underwriting purpose",
                    "Exact access route and commercial cost basis",
                    "Publication latency and recommended desk refresh",
                    "Request hygiene and permitted collection method",
                    "Fallback evidence and material interpretation limit",
                ],
                "rows": [
                    [
                        "SEC EDGAR submissions API identifies issuer filings and event history",
                        "GET https://data.sec.gov/submissions/CIK##########.json; public access carries no API subscription fee",
                        "Submission metadata updates throughout the day; process recent changes every few minutes",
                        "Use identified User-Agent and shared five-request-per-second token bucket across all workers",
                        "Mirror SEC submissions.zip nightly; inspect archived filings when live requests fail",
                    ],
                    [
                        "SEC Current Filings Atom feed discovers Form D and Form 8-K events",
                        "Request https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&output=atom; repeat with type=D without subscription charges",
                        "Recent filings appear as published; acceptance time differs from underlying event time",
                        "Share SEC request budget, deduplicate accession numbers, and stop aggressive retries after throttling",
                        "Recover missed windows through daily indexes and filing archives; parse Form D XML separately",
                    ],
                    [
                        "California Secretary of State bizfile verifies California business entity records",
                        "Search https://bizfileonline.sos.ca.gov/search/business; basic searches are free and document charges vary",
                        "Refresh at onboarding and closing; filing acceptance controls when changes become visible",
                        "Use portal-supported retrieval methods and request official bulk arrangements before systematic collection",
                        "Obtain certified records or use the actual formation state's official entity registry",
                    ],
                    [
                        "California Secretary of State UCC portal locates filed security interests",
                        "Enter through https://www.sos.ca.gov/business-programs/ucc; official searches and copies follow posted fees",
                        "Order initial searches during diligence and lender-required updates near funding",
                        "Search exact legal debtor names and correct jurisdictions; avoid unsupported automated portal scraping",
                        "Use qualified search providers and certified results; filed notices do not establish current balances",
                    ],
                    [
                        "PACER federal court records establish docket history and filed litigation documents",
                        "Use https://pacer.uscourts.gov and PACER Case Locator; retrieval generally costs $0.10 per page",
                        "Court entries appear after filing and processing; review active matters daily when material",
                        "Use permitted account access, track billable retrievals, and protect sealed or restricted material",
                        "Check RECAP for available copies; return to the court for missing authoritative records",
                    ],
                    [
                        "CourtListener RECAP API accelerates discovery of publicly available federal docket copies",
                        "Use https://www.courtlistener.com/help/api/ with required authentication; quotas and paid products depend on service",
                        "Availability depends on contributed or collected records; coverage can lag the actual court docket",
                        "Respect current account quotas and response headers; cache document identifiers and exponential retries",
                        "Retrieve missing documents through PACER; never interpret absent RECAP entries as absent litigation",
                    ],
                    [
                        "SBA open data describes historical 7(a) and 504 lending activity",
                        "Download published datasets through https://data.sba.gov; government dataset access is free",
                        "Refresh after published dataset releases; historical records are not live lender commitments",
                        "Download once per release, retain release dates, and filter locally by relevant attributes",
                        "Confirm current programs through SBA materials and direct lender appetite interviews",
                    ],
                    [
                        "NMLS Consumer Access checks participating financial services license records and identifiers",
                        "Search https://www.nmlsconsumeraccess.org; public lookup is free through supported website functions",
                        "Recheck before engagement and periodically; regulator submissions determine visible update timing",
                        "Use ordinary permitted searches and regulator-approved data services rather than bypassing access controls",
                        "Ask the responsible state regulator directly where commercial brokerage activity falls outside coverage",
                    ],
                    [
                        "California DFPI verifies covered lenders, brokers, and commercial financing requirements",
                        "Navigate https://dfpi.ca.gov to licensee searches and commercial financing resources; public access is free",
                        "Review before entering California business and whenever published rules or licenses change",
                        "Save dated official results and use published downloads instead of undocumented endpoints",
                        "Request regulator clarification and applicable statutory text when product-specific treatment remains unresolved",
                    ],
                    [
                        "OFAC Sanctions List Service supplies official sanctions datasets for screening",
                        "Download supported files from https://ofac.treasury.gov/sanctions-list-service; official data access is free",
                        "Refresh on published updates and rescreen relevant parties before transaction execution",
                        "Validate file integrity, preserve list versions, and resolve potential matches through identity evidence",
                        "Use official Sanctions List Search and documented manual review during feed interruption",
                    ],
                    [
                        "EPA Cleanups in My Community identifies environmental cleanup sites and programs",
                        "Search https://www.epa.gov/cleanups/cleanups-my-community; public mapping and linked records are free",
                        "Refresh at property screening and diligence milestones; program reporting cycles vary",
                        "Use published downloads or supported interfaces and record each dataset's update date",
                        "Obtain state environmental files and professional environmental reports; map absence proves little",
                    ],
                    [
                        "FEMA Map Service Center verifies effective flood mapping around proposed collateral",
                        "Search https://msc.fema.gov/portal/home by address or coordinates; public map access is free",
                        "Check effective dates and pending revisions whenever collateral underwriting changes",
                        "Retrieve supported map products, preserve panel identifiers, and avoid excessive repeated tile requests",
                        "Obtain lender-accepted flood determinations and local records for parcel-specific resolution",
                    ],
                    [
                        "Los Angeles County Registrar-Recorder supplies recorded real property document evidence",
                        "Start at https://www.lavote.gov under real estate records; copies and searches follow posted schedules",
                        "Recording and indexing timing varies; request lender-required closing updates through title professionals",
                        "Use approved ordering channels and restrict stored personal information to documented transaction needs",
                        "Obtain a title commitment and recorded instruments; tax assessor ownership alone is insufficient",
                    ],
                    [
                        "Georgia Department of Revenue administers Georgia film tax credit transfer requirements",
                        "Use https://dor.georgia.gov/film-tax-credit and linked Georgia Tax Center procedures; public guidance is free",
                        "Check current rules during engagement and transaction-specific status before settlement",
                        "Access taxpayer records only through authorized accounts and retain current transfer documentation",
                        "Suspend settlement while obtaining agency confirmation, audit evidence, and buyer eligibility documentation",
                    ],
                    [
                        "Massachusetts Department of Revenue publishes state historic rehabilitation credit requirements",
                        "Use https://www.mass.gov and search Massachusetts historic rehabilitation tax credit; public guidance is free",
                        "Refresh for award periods, rule changes, and each proposed transfer or recapture review",
                        "Use official forms and authorized taxpayer communications; do not infer private account status",
                        "Obtain award certificates and program confirmation before matching credits with eligible buyers",
                    ],
                    [
                        "National Park Service historic preservation incentives explain federal rehabilitation certification mechanics",
                        "Visit https://www.nps.gov/subjects/taxincentives/index.htm; guidance and program materials are publicly accessible",
                        "Review current guidance during project screening and each certification milestone",
                        "Preserve dated program documents and verify project-specific certifications through authorized project participants",
                        "Consult the relevant state preservation office; federal certification does not create outright transferability",
                    ],
                    [
                        "Middesk business verification API enriches entity identity and selected business records",
                        "Request contracted API access through https://www.middesk.com; pricing and search coverage require written quotes",
                        "Use responses and webhooks where supported; underlying registry freshness varies by jurisdiction",
                        "Honor contracted quotas, webhook signatures, idempotency requirements, and permitted redistribution terms",
                        "Return to official entity and UCC records whenever coverage, freshness, or identity conflicts",
                    ],
                    [
                        "Plaid permissioned financial products connect borrower-authorized account and transaction evidence",
                        "Use Plaid Link and documented endpoints at https://plaid.com/docs; production pricing depends on contracted products",
                        "Refresh follows product and institution capabilities; stale connections require explicit borrower reconnection",
                        "Verify webhook authenticity, protect access tokens, and follow product-specific limits and retry guidance",
                        "Collect complete borrower statements securely and reconcile ownership, dates, balances, and missing periods",
                    ],
                ],
            },
        },
        {
            "heading": "2. Turn SEC events into permissioned, evidence-backed lender conversations",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement sec_edgar_8k_vendor_trigger_arbitrage as an event queue, "
                    "not an automatic sales blast. Poll SEC Current Filings for "
                    "Form 8-K and Form D, then fetch the issuer submission record "
                    "and original filing using its accession number. Parse Item "
                    "5.02 for executive departures or appointments, Item 1.01 for "
                    "material agreements, and Item 2.01 for completed acquisitions "
                    "or dispositions. Form D is a notice of an exempt securities "
                    "offering; it does not prove that all stated capital was "
                    "raised, that the issuer needs debt, or that a securities "
                    "intermediary may solicit investors. Route each event to a "
                    "specific commercial hypothesis: acquisition integration may "
                    "need equipment financing, a new contract may create receivables "
                    "capacity needs, and executive turnover may simply warrant "
                    "waiting. Many domestic issuer Form 8-K events have a four-business-day "
                    "filing deadline, so sub-hour reaction means time after public "
                    "publication, not privileged access to the underlying event. "
                    "Record filing acceptance, ingestion, analyst review, and first "
                    "outreach timestamps separately. This makes speed measurable "
                    "without misrepresenting freshness or assuming that every "
                    "commercial database updates later than your own workflow. "
                    "Exclude amended duplicates unless the amendment changes the financing hypothesis."
                ),
                (
                    "Use one organization-wide token bucket at five requests per "
                    "second, with a descriptive User-Agent containing an operating "
                    "contact. This deliberately conservative ceiling sits below "
                    "the SEC's published maximum of ten requests per second; "
                    "distributing workers must not multiply the allowance. Back "
                    "off on throttling, honor Retry-After when supplied, and stop "
                    "retry storms during service degradation. Mirror the SEC "
                    "nightly submissions.zip bulk archive for historical filing "
                    "metadata, then use filing indexes and archived documents "
                    "when the required text is absent from that archive. The "
                    "companyfacts.zip archive serves extracted financial facts, "
                    "not a complete substitute for filing documents or Form D "
                    "terms. Cache by accession number and content hash, and "
                    "quarantine malformed payloads rather than discarding them. "
                    "An illustrative monthly funnel starts with 400 filtered "
                    "events, advances 40 analyst-qualified situations, produces "
                    "eight permissioned applications, and closes one placement. "
                    "At $10,000 retained fees and $800 incremental research and "
                    "outreach expense, contribution before all other operating "
                    "costs is $9,200. That is workflow math, not an additional "
                    "profit forecast or a promise that event sourcing closes "
                    "one deal every month. Measure cohorts through actual fee collection."
                ),
                (
                    "Connect the queue to lender matching only after the desk "
                    "can explain the financing need. A vendor contract announcement "
                    "does not establish assignable receivables, acceptable account "
                    "debtors, dilution history, or a borrowing base. An equipment "
                    "purchase announcement does not establish title, useful life, "
                    "serial numbers, or an acceptable appraisal. Require those "
                    "facts before sending an application to a lender. Store "
                    "matching rules as versioned records with hard exclusions "
                    "separate from preferences; an out-of-state borrower cannot "
                    "be rescued by a high weighted score when the lender lacks "
                    "coverage. Commercial outreach should use verified business "
                    "contact channels, accurate sender identity, an effective "
                    "opt-out, and a suppression list consistent with 15 U.S.C. "
                    "7704. Purchased mobile numbers do not establish permission "
                    "for automated calls or texts. Route personal credit reports "
                    "through a documented permissible-purpose process under "
                    "15 U.S.C. 1681b rather than treating a business financing "
                    "inquiry as blanket access to every principal's file. Where "
                    "the desk participates in credit decisions or covered "
                    "referrals, apply the relevant Regulation B duties and "
                    "retain reasoned routing records. Do not use neighborhood, "
                    "surname, or demographic proxies to rank borrowers."
                ),
            ],
            "table": {
                "caption": "Event pipeline diagnostics that distinguish genuine opportunity from parser noise",
                "headers": [
                    "Observed event and proposed financing hypothesis",
                    "Verification test before borrower or lender outreach",
                    "Diagnostic metric and explicit operating intervention",
                    "Failure fallback preserving the authoritative evidence trail",
                ],
                "rows": [
                    [
                        "Form 8-K Item 1.01 announces a potentially financeable customer agreement",
                        "Read exhibits for payment terms, termination rights, assignment restrictions, and counterparty identity",
                        "Track analyst-qualified events divided by parsed events; tighten rules when irrelevant agreements dominate",
                        "Request borrower contracts securely and pause receivables matching until assignability receives lender review",
                    ],
                    [
                        "Form 8-K Item 2.01 describes a completed acquisition or disposition",
                        "Confirm transaction completion, financing already arranged, acquired assets, and surviving obligor structure",
                        "Measure qualified integration financing conversations rather than counting every acquisition headline as demand",
                        "Offer later equipment or working-capital review when acquisition funding is already complete",
                    ],
                    [
                        "Form 8-K Item 5.02 changes executive leadership or management responsibilities",
                        "Separate departures from appointments and inspect whether a disclosed financing event actually exists",
                        "Track incorrect contact routing and suppress outreach that relies on departed executives",
                        "Wait for verified successor contacts and pursue only a documented commercial financing hypothesis",
                    ],
                    [
                        "Form D reports offering information that may suggest a changing capital structure",
                        "Read amounts sold, offering type, issuer identity, and amendments before drawing conclusions",
                        "Deduplicate issuer and offering histories; reject securities solicitation tasks outside authorized business scope",
                        "Discuss commercial debt only with verified issuer representatives and appropriately qualified counterparties",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four advantages that survive contact with underwriting",
                "body": (
                    "Speed earns attention only when the first conversation contains "
                    "a correct entity, a defensible hypothesis, and a usable evidence packet."
                ),
                "items": [
                    "Store both event date and SEC acceptance timestamp; score response speed from publication rather than pretending delayed disclosure is real-time business intelligence.",
                    "Ask each receivables lender for three recent decline reasons and encode the exact exclusions before adding another contact-enrichment subscription.",
                    "Compare UCC debtor names with formation records before paying for broader searches; a punctuation or entity-suffix error can undermine the entire search strategy.",
                    "Track fee collection and clawback windows by lender cohort; a fast term sheet is less valuable than a durable, collectible retained fee.",
                ],
            },
        },
        {
            "heading": "3. Separate specialist collateral evidence from prohibited assumptions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat litigation_finance_mass_tort_docket_securitization as a "
                    "specialist facility diligence track, not permission to purchase "
                    "patients or divide legal fees. An Arizona Alternative Business "
                    "Structure must actually hold the relevant authorization; its "
                    "existence does not export Arizona ownership rules into other "
                    "jurisdictions. A co-counsel arrangement likewise does not make "
                    "a finance broker a law firm. Verify retained counsel, client "
                    "engagements, assignment restrictions, case inventory, adverse "
                    "rulings, limitation dates, and lender collateral rights before "
                    "discussing a credit facility. CourtListener and PACER establish "
                    "public docket events, not injury causation, medical eligibility, "
                    "retainer validity, or settlement value. Keep medical records "
                    "inside counsel-controlled systems and send lenders only "
                    "authorized, minimized evidence through a documented access "
                    "process. Do not budget universal $6.50 HITECH patient-directed "
                    "record retrievals. The optional HIPAA flat-fee method concerns "
                    "certain individual requests for electronic copies; it is not "
                    "a blanket price ceiling for third-party litigation requests. "
                    "HHS guidance following Ciox distinguishes third-party directives "
                    "from the individual access fee limitation. Determine the "
                    "requestor, record format, transmission instruction, applicable "
                    "access rule, and actual provider charge before approving "
                    "acquisition spending. Counsel must separately assess solicitation, "
                    "referral compensation, confidentiality, and professional-conduct restrictions."
                ),
                (
                    "The mapped inventory range of 1,000–25,000 retained matters "
                    "at $1,200–$2,500 acquisition cost implies $1.2 million–$62.5 "
                    "million of acquisition spending before verification, case "
                    "work, interest, or losses. That scale is institutional "
                    "collateral exposure, not brokerage revenue. Proposed tranche "
                    "resales at 2.5–4 times cost and proposed 35–40% settlement "
                    "fee splits are transaction assumptions requiring jurisdiction-specific "
                    "legal and commercial validation; neither belongs in this "
                    "desk's fee forecast. For example, 1,000 matters at $1,500 "
                    "cost create a $1.5 million acquisition basis. Recovering "
                    "50% of that basis requires $750,000 of actual proceeds, "
                    "not merely a funder's expression of interest. Diversifying "
                    "across six to ten mass-tort or single-event commercial "
                    "casualty niches can reduce some concentration, but common "
                    "counsel, evidentiary standards, or appellate outcomes can "
                    "still correlate losses. PFAS, AFFF, Paraquat, NEC, rideshare "
                    "assault, and device claims each require separate eligibility "
                    "and evidence frameworks. The suggested fallback of paying "
                    "media vendors only on EMR-verified retainers requires "
                    "professional-conduct review; use a lawful alternative "
                    "compensation structure where per-retainer payment is restricted. "
                    "If assignment, referral compensation, or medical access "
                    "cannot be established, stop that track and offer only "
                    "appropriately authorized commercial facility brokerage."
                ),
                (
                    "Implement state_film_historic_brownfield_tax_credit_brokerage "
                    "with a certificate-to-taxpayer evidence chain. Verify the "
                    "specific state statute, issuing agency, award certificate, "
                    "eligible tax year, transfer count, buyer restrictions, "
                    "carryforward period, recapture exposure, and required notices. "
                    "Film commissions may explain production qualification, "
                    "while the revenue department controls tax administration; "
                    "neither marketing material nor a producer spreadsheet replaces "
                    "the actual award and transfer record. State historic and "
                    "brownfield programs differ materially, and federal historic "
                    "rehabilitation credits under 26 U.S.C. 47 cannot simply "
                    "be sold outright because a state program permits transfers. "
                    "Illustratively, a verified $1 million state credit sold "
                    "at $0.90 per dollar produces $900,000 seller consideration. "
                    "A separately disclosed 2% placement fee on that consideration "
                    "is $18,000 of operator revenue, assuming the engagement "
                    "allocates that fee to the broker. Neither the $1 million "
                    "face amount nor $900,000 settlement flow is operator "
                    "revenue. Buyer usable value depends on its own tax "
                    "position and program restrictions. Use diligence contingencies "
                    "and appropriately structured third-party settlement; suspend "
                    "settlement when certification or eligibility fails, then "
                    "rematch only verified credits without promising tax savings. "
                    "For brownfields, reconcile environmental site identity with "
                    "the actual credit-bearing taxpayer and award."
                ),
            ],
            "table": {
                "caption": "Specialist evidence tests for litigation facilities and transferable state credits",
                "headers": [
                    "Specialist transaction and concrete evidence requirement",
                    "Named source or authorized verification counterparty",
                    "Unit economics separated from retained brokerage revenue",
                    "Stop condition and economically bounded fallback",
                ],
                "rows": [
                    [
                        "Litigation facility requires verified counsel authority and enforceable collateral documentation",
                        "Arizona Judicial Branch ABS directory, state bar records, PACER, and engaged specialist counsel",
                        "One thousand matters at $1,500 acquisition cost represent $1.5 million collateral acquisition spending",
                        "Stop unsupported assignments and restrict work to authorized facility placement with documented compensation",
                    ],
                    [
                        "Medical verification requires authorized access and case-specific evidentiary review",
                        "Treating providers, counsel-controlled record systems, HHS access guidance, and qualified clinical reviewers",
                        "Provider charges and clinical review costs must be quoted separately rather than assuming $6.50 universally",
                        "Reject improperly obtained records and reacquire only through a documented lawful request pathway",
                    ],
                    [
                        "State film credit placement requires final eligible credit and verified transfer procedure",
                        "State revenue department, issuing program administrator, taxpayer authorization, and transaction-specific certificates",
                        "A 2% fee on $900,000 seller consideration yields $18,000 retained revenue before operating expenses",
                        "Suspend settlement for unresolved audits or transfer restrictions and rematch only verified eligible credits",
                    ],
                    [
                        "Historic or brownfield credit requires exact program identity and buyer usability analysis",
                        "State preservation office, environmental agency, revenue department, and buyer's engaged tax professionals",
                        "Record face amount, negotiated consideration, placement fee, and recapture exposure in separate ledger fields",
                        "Reject assumed federal transferability and return to the applicable state statute and award documentation",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before transmitting a specialist financing package",
                "body": (
                    "A senior operator records the evidence supporting each check. "
                    "An unresolved check pauses the affected transaction rather than "
                    "being buried in a lender presentation."
                ),
                "items": [
                    "Verify the broker's product and state permissions, written fee terms, lender identity, and any separate securities-registration implications before accepting the mandate.",
                    "Verify litigation counsel authority, lawful compensation structure, collateral rights, and medical-record access without treating ABS status as nationwide permission.",
                    "Verify credit certification, state transferability, buyer eligibility, tax-year restrictions, and settlement contingencies directly against the operative program documents.",
                    "Verify borrower authorization, minimum necessary data sharing, recipient access, and source freshness before releasing bank, personal, medical, or tax information.",
                ],
            },
        },
        {
            "heading": "4. Instrument the desk around collectible fees, not data volume",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a compact stack whose components have clear responsibilities. "
                    "PostgreSQL can hold normalized entities, source observations, "
                    "lender rules, applications, and fee events; encrypted object "
                    "storage holds originals; a CRM such as HubSpot tracks "
                    "relationships without becoming the medical or banking document "
                    "repository. A scheduled Python worker can fetch permitted "
                    "sources, validate schemas, calculate hashes, and write "
                    "append-only ingestion logs. Separate API credentials by "
                    "environment, restrict service accounts, enable multifactor "
                    "authentication for operators, and keep secrets out of URLs "
                    "and logs. Apply the FTC Safeguards Rule, 16 CFR Part "
                    "314, where the business falls within its coverage, with "
                    "a documented security program proportionate to the actual "
                    "information handled. Diagnose failures through request "
                    "identifiers, status codes, source timestamps, and redacted "
                    "payload samples rather than copying borrower records "
                    "into public debugging tools. Use curl for controlled "
                    "endpoint checks, Python json for payload validation, "
                    "SQLite for isolated replay fixtures, and PostgreSQL "
                    "EXPLAIN for slow matching queries. Test expired credentials, "
                    "partial downloads, duplicate webhooks, renamed entities, "
                    "and disconnected bank accounts before relying on unattended "
                    "processing. Every automated route needs a named human "
                    "owner and a documented manual continuation."
                ),
                (
                    "Reconcile the operating dashboard to the canonical scorecard "
                    "before optimizing conversion. Conservative revenue is "
                    "$120,000, representable as twelve collected placements "
                    "averaging $10,000 retained fees; $90,000 of total annual "
                    "costs leaves $30,000 owner net profit at 25%. Base "
                    "revenue is $560,000, representable as twenty-eight "
                    "placements averaging $20,000; $364,000 of total costs "
                    "leaves $196,000 at 35.0%. Scaled revenue is $1,000,000, "
                    "representable as forty placements averaging $25,000; "
                    "$550,000 of total costs leaves $450,000 at 45%. "
                    "These deal counts illustrate the supplied totals rather "
                    "than changing them. Conservative and Base each use "
                    "two full-time staff plus two contractors; Scaled uses "
                    "three full-time staff plus three contractors. Contractor "
                    "counts do not imply full-time utilization. The stated "
                    "$4,000–$18,000 monthly operating-expense range is a "
                    "planning band, not a substitute for these scenario "
                    "total-cost budgets, which must include applicable labor, "
                    "variable acquisition costs, and other expenses. Startup "
                    "capital remains $20,000–$100,000 and the first deal "
                    "may take three to nine months. Separate principal "
                    "funded, fees contractually earned, fees collected, "
                    "co-broker deductions, and reversal exposure so a large "
                    "loan cannot inflate recognized operator revenue."
                ),
                (
                    "Instrument the full application path with timestamps for "
                    "intake completeness, first lender match, lender response, "
                    "term sheet, closing, fee receipt, and clawback expiry. "
                    "Calculate failed-closing cost by cohort, including paid "
                    "searches and analyst hours, then identify which missing "
                    "documents predicted failure. Track lender concentration "
                    "by collected fees and active pipeline separately; ten "
                    "lenders in the CRM do not diversify a desk whose "
                    "receipts depend on one institution. For a simple "
                    "capacity check, twenty-eight Base closings at a 25% "
                    "complete-application closing rate require 112 complete "
                    "applications annually, about nine to ten monthly. "
                    "If that rate falls to 20%, the same closing "
                    "target requires 140 complete applications, increasing "
                    "review workload without increasing revenue per deal. "
                    "Renewal tracking should start from contractual maturity "
                    "and borrower permission, not assumed repeat eligibility. "
                    "Maintain a fee calendar covering conditions precedent, "
                    "payment dates, early-payoff provisions, and clawback "
                    "windows. Before adding an API subscription, compare "
                    "its annual cost against hours saved at a realistic "
                    "loaded labor rate and attributable improvement in "
                    "collected fees. A $6,000 subscription saving 120 "
                    "hours at $40 per hour saves only $4,800; it "
                    "needs another $1,200 of demonstrable value to break even."
                ),
            ],
            "table": {
                "caption": "Operational diagnostics tied to fee collection, security, and workload",
                "headers": [
                    "Diagnostic signal and exact measurement basis",
                    "Investigation procedure using named operator tools",
                    "Concrete intervention within the existing team",
                    "Revenue interpretation and evidence retention requirement",
                ],
                "rows": [
                    [
                        "Source freshness measures publication-to-ingestion lag separately from underlying business event age",
                        "Compare SEC acceptance timestamps, worker logs, and stored document hashes for sampled events",
                        "Repair stalled queues, replay missed accession numbers, and reduce nonessential enrichment requests",
                        "Retain the replay manifest; faster ingestion alone does not establish additional earned fees",
                    ],
                    [
                        "Application completeness measures lender-required evidence present before the first underwriting submission",
                        "Query PostgreSQL missing-field reports and inspect secure document checklists by facility type",
                        "Assign borrower follow-up to one owner and prevent duplicate requests across team members",
                        "Attribute reduced rework to labor savings rather than counting requested principal as revenue",
                    ],
                    [
                        "Closing durability measures collected fees after applicable reversals and contractual clawback exposure",
                        "Reconcile CRM deal status with bank receipts, lender statements, and signed compensation schedules",
                        "Investigate repeated early-payoff reversals and renegotiate prospective terms where commercially possible",
                        "Apply the chosen accounting policy consistently and preserve fee adjustments with supporting documents",
                    ],
                    [
                        "Access control measures authorized recipients, credential scope, and sensitive document exposure",
                        "Review identity-provider logs, storage access logs, webhook verification failures, and redacted error traces",
                        "Revoke unnecessary access, rotate compromised credentials, and follow the documented incident response process",
                        "Retain incident evidence securely and assess applicable reporting duties without exposing borrower records",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register sources and permitted purposes",
                    "action": "Create a dated source inventory with official URLs, account owners, fees, quotas, retention rules, and authorized uses.",
                    "detail": "Select one equipment, one receivables, and one bridge workflow; identify the primary record and manual fallback for every required underwriting field.",
                },
                {
                    "step": 2,
                    "title": "Build a replayable ingestion path",
                    "action": "Implement shared SEC throttling, accession deduplication, encrypted artifact storage, schema checks, and a failed-record queue.",
                    "detail": "Replay a representative test batch including amended filings, missing documents, throttled responses, and conflicting entity names before enabling scheduled processing.",
                },
                {
                    "step": 3,
                    "title": "Validate matching and specialist boundaries",
                    "action": "Have a senior operator confirm lender exclusions, borrower permissions, licensing scope, and specialist collateral evidence.",
                    "detail": "Keep litigation medical evidence with authorized counsel and state credit usability with qualified transaction participants; transmit only the necessary verified package.",
                },
                {
                    "step": 4,
                    "title": "Close the evidence-to-cash loop",
                    "action": "Reconcile collected fees, failed-closing costs, source expenses, lender concentration, and clawback exposure every month.",
                    "detail": "Compare results against the exact Conservative, Base, and Scaled totals; remove subscriptions that cannot demonstrate underwriting value or measurable operating savings.",
                },
            ],
        },
    ],
    "pull_quote": "The information edge is a verified financing fact delivered before the lender has to ask for it.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create the eighteen-source register with dated pricing, permitted access methods, publication latency, refresh schedules, and a named fallback owner.",
        "Deploy one shared five-request-per-second SEC token bucket, accession-level deduplication, and a nightly submissions.zip mirror for historical recovery.",
        "Build separate equipment, receivables, SBA, and bridge lender matrices with hard exclusions, required evidence, and dated lender confirmations.",
        "Require specialist review of litigation compensation, medical access, collateral rights, and state credit transferability before distributing financing materials.",
        "Test malformed payloads, expired tokens, duplicate webhooks, stale liens, and disconnected bank accounts using redacted fixtures and recorded recovery steps.",
        "Reconcile monthly fee collections and total costs to $30,000, $196,000, and $450,000 annual owner-profit cases without counting principal or credit face amounts as revenue.",
    ],
    "statutory_citations": [
        {
            "title": "17 CFR 249.308 — Form 8-K",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-249/section-249.308",
            "relevance": "Identifies the current-report form underlying event ingestion; read the form and its instructions for item-specific content and filing deadlines.",
        },
        {
            "title": "17 CFR 230.503 — Filing of notice of sales",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-230/section-230.503",
            "relevance": "Governs Form D notice filing for covered exempt offerings; a notice does not establish completed fundraising or authorize securities brokerage.",
        },
        {
            "title": "California Financial Code Section 22100",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22100.",
            "relevance": "Establishes licensing requirements for covered finance lender or broker activity, subject to applicable definitions and exemptions.",
        },
        {
            "title": "California Financial Code Section 22802",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22802.",
            "relevance": "Specifies disclosures for covered commercial financing offers; determine provider responsibilities, transaction scope, and applicable implementing rules.",
        },
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": "Requires a valid permissible purpose before obtaining a principal's consumer report; business contact enrichment is not a substitute.",
        },
        {
            "title": "12 CFR 1002.4 — General rules under Regulation B",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.4",
            "relevance": "Addresses discrimination and discouragement in credit activity; apply alongside the creditor definition and other duties applicable to the desk's role.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Provides concrete sender-identity, message, and opt-out requirements relevant to commercial event-triggered email outreach.",
        },
        {
            "title": "16 CFR Part 314 — Standards for safeguarding customer information",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314",
            "relevance": "Requires covered financial institutions to maintain appropriate information-security safeguards; coverage and specific obligations depend on the actual business.",
        },
        {
            "title": "45 CFR 164.524 — Access of individuals to protected health information",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524",
            "relevance": "Defines individual access rights and applicable fee restrictions; do not convert the optional electronic-copy flat-fee method into a universal litigation procurement price.",
        },
        {
            "title": "HHS notice concerning the Ciox Health court order",
            "url": "https://www.hhs.gov/hipaa/court-order-right-of-access/index.html",
            "relevance": "Explains the court order's effect on third-party directives and the patient-rate limitation; use with the underlying access regulation.",
        },
        {
            "title": "26 U.S.C. 47 — Rehabilitation credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/47",
            "relevance": "Defines the federal rehabilitation credit; federal credit treatment must not be inferred from state transferable-credit programs.",
        },
        {
            "title": "Massachusetts General Laws, Chapter 62, Section 6J",
            "url": "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section6J",
            "relevance": "Provides state historic rehabilitation credit provisions, including transfer mechanics; verify the taxpayer regime, current rules, award, and applicable restrictions.",
        },
    ],
}
