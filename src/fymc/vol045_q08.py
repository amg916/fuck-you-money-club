from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small no surprises act (idr) medical arbitration & out-of-network recovery desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "CMS IDR Records, NPPES, ERISA Plan Evidence, X12 835 Pipelines, and Cash-Verified QPA Recovery",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #45, Rank #09 of 49, scores 94/100 by turning documented "
        "out-of-network underpayments into a tightly controlled recovery workflow. "
        "This chapter connects 18 named resources to 12 mapped plays spanning "
        "provider discovery, jurisdiction screening, remittance normalization, "
        "deadline control, evidence assembly, and collected-cash reconciliation. "
        "Public records identify opportunities; authorized claim records establish "
        "eligibility; bank-matched receipts establish earned contingency revenue. "
        "Formula v2.0 fixes annual owner profit at $33,000 Conservative, $217,150 "
        "Base, and $504,000 Scaled, without counting baseline provider collections. "
        "The operating edge is a versioned evidence chain, not indiscriminate "
        "scraping: every source needs an access method, freshness rule, fallback, "
        "and accountable owner before its output influences a filing."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned operator contingency revenue; excludes baseline provider collections",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish authoritative identities before enriching an opportunity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with an identity ledger, not a prospect spreadsheet. Give each "
                    "provider organization, rendering clinician, payer legal entity, employer "
                    "plan, and disputed service a separate internal identifier. NPPES supplies "
                    "an NPI and published taxonomy; it does not establish network status, "
                    "licensure, ownership, or federal IDR eligibility. Join an organization "
                    "NPI to the signed engagement, authorized billing records, and relevant "
                    "practice locations before attaching claims. Use CMS Care Compare to "
                    "corroborate publicly reported affiliations, then verify current practice "
                    "relationships directly. An apparent hospital affiliation is neither "
                    "proof of employment nor proof that a particular encounter qualifies "
                    "under the No Surprises Act. Store the source URL, retrieval time, "
                    "effective period, and original artifact hash beside every asserted "
                    "attribute. Keep contradictory observations rather than overwriting them. "
                    "A directory address changed yesterday cannot retroactively establish "
                    "the service location six months earlier. The first three chapter-local "
                    "mapped plays are Provider Identity Resolution, Practice Affiliation "
                    "Verification, and Federal-versus-State Routing. At 100 prospective "
                    "practices and six minutes per identity check, initial screening consumes "
                    "ten hours; resolving only twenty ambiguous matches at fifteen minutes "
                    "each adds five hours. That bounded queue beats letting every ambiguous "
                    "record consume a full arbitration analyst review."
                ),
                (
                    "Jurisdiction is a document question, not a payer-logo classifier. "
                    "DOL Form 5500 records can corroborate an employer plan's existence "
                    "and reported arrangements, but filing exemptions, reporting lag, and "
                    "sponsor subsidiaries prevent a reliable one-field determination of "
                    "funding status. Obtain the applicable plan documents, coverage details, "
                    "initial remittance, service location, and evidence concerning any "
                    "state election that matters to the encounter. Separate ERISA status "
                    "from self-funding; neither label alone resolves every federal-versus-state "
                    "payment issue. Test whether a specified state law or applicable "
                    "All-Payer Model Agreement determines the payment amount before routing "
                    "to federal IDR under 42 U.S.C. § 300gg-111. Medicare, Medicaid, and "
                    "other excluded coverage must leave this commercial workflow. Record "
                    "why the service category and circumstances meet the relevant federal "
                    "protections, including emergency care or covered nonemergency services "
                    "at participating facilities. For thirty uncertain claims, a twelve-minute "
                    "document check costs six analyst hours; compare that with thirty "
                    "avoidable filing expenditures and dismissed cases. The fallback is "
                    "a missing-evidence queue with a named requester and deadline, not "
                    "an automated federal filing based on an insurance card. State "
                    "insurance department materials supplement, but do not replace, "
                    "encounter-specific plan evidence."
                ),
                (
                    "Use CMS IDR public-use releases to understand the market's case "
                    "mix, reporting periods, and operational congestion. They are aggregate "
                    "observations, not a provider prospect list, a current case-status API, "
                    "or a forecast that your offers will be collected. Preserve each "
                    "release with its methodology because submissions, disputes, determinations, "
                    "and payment outcomes have different denominators. A reported prevailing "
                    "offer share cannot supply a collection probability without separate "
                    "receipt evidence. The directory in this chapter contains eighteen "
                    "named resources across three matrices; the fourth matrix contains "
                    "operating tests rather than additional directory entries. Cost tiers "
                    "distinguish free public access, included customer access, and negotiated "
                    "licenses, because commercial endpoints rarely have universal pricing. "
                    "Refresh cadence likewise separates a source's publication schedule "
                    "from the desk's polling schedule. Do not manufacture a latency "
                    "commitment where the publisher provides none. Maintain an acquisition "
                    "manifest containing retrieval timestamps, response status, content "
                    "hashes, parser version, and row counts. A public download that "
                    "silently changes columns should fail into quarantine instead of "
                    "rewriting the identity ledger. For six public sources checked "
                    "weekly, twenty minutes of review per source budgets two hours; "
                    "measure whether detected changes actually affect routing before "
                    "increasing that frequency."
                ),
            ],
            "table": {
                "caption": "Official Discovery Directory: Six Public Identity and Jurisdiction Resources",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method",
                    "Cost tier and acquisition boundary",
                    "Refresh and latency treatment",
                    "Rate-limit and retrieval hygiene",
                    "Fallback evidence when coverage breaks",
                ],
                "rows": [
                    [
                        "CMS NPPES NPI Registry resolves published provider identifiers",
                        "Query https://npiregistry.cms.hhs.gov/api/ with version=2.1 and documented search parameters",
                        "Public API access is free; bulk processing adds storage costs",
                        "Check weekly; reconcile bulk files against their published release dates",
                        "Cache NPI responses, bound pagination, and back off throttled requests",
                        "Use CMS NPPES downloadable files plus signed provider identity records",
                    ],
                    [
                        "CMS NPPES downloadable files support reproducible provider population snapshots",
                        "Download published files through https://download.cms.gov/nppes/NPI_Files.html and retain manifests",
                        "Public downloads are free; budget bandwidth and local indexing work",
                        "Ingest monthly replacement files and available weekly incremental updates",
                        "Download each artifact once; reuse hashes instead of repeated transfers",
                        "Use targeted NPI Registry queries for records awaiting bulk reconciliation",
                    ],
                    [
                        "CMS Care Compare datasets corroborate publicly reported clinician affiliations",
                        "Select dataset and download CSV through https://data.cms.gov/provider-data/ resource pages",
                        "Public access is free; analyst matching remains an operating expense",
                        "Read each dataset release date; affiliation changes may lag encounters",
                        "Prefer complete published downloads over repeated broad interactive queries",
                        "Request current practice rosters and encounter-specific facility relationship evidence",
                    ],
                    [
                        "DOL Form 5500 Search supports employer plan identity research",
                        "Search sponsor names and EINs at https://www.efast.dol.gov/5500Search/ official interface",
                        "Public search is free; document interpretation requires trained staff time",
                        "Annual filings arrive with lag; preserve plan year and amendments",
                        "Use targeted searches and published downloads rather than scraping sessions",
                        "Request summary plan documents and administrator confirmation for relevant coverage",
                    ],
                    [
                        "CMS No Surprises resources publish IDR reports and implementation materials",
                        "Navigate https://www.cms.gov/nosurprises to IDR reports, downloads, and technical guidance",
                        "Public releases are free; no private dispute feed is implied",
                        "Check weekly; ingest only when publication version or content changes",
                        "Cache downloads and record methodology revisions beside each imported release",
                        "Retain prior releases and use case-specific receipts for operational status",
                    ],
                    [
                        "Texas Department of Insurance illustrates state surprise-billing routing research",
                        "Use official balance-billing materials at https://www.tdi.texas.gov/medical-billing/index.html and linked authorities",
                        "Public materials are free; state-specific interpretation adds casework expense",
                        "Check before routing Texas encounters and after published rule changes",
                        "Retrieve linked primary materials once and preserve dated source copies",
                        "Use applicable state statutes and plan evidence when guidance conflicts",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make uncertainty visible before it becomes a filing expense",
                "body": (
                    "The strongest desk separates corroboration from proof and maintains "
                    "dated evidence for every material routing decision."
                ),
                "items": [
                    "Keep the payer brand, claims administrator, and plan sponsor in separate fields; the logo on an ERA does not identify the governing payment regime.",
                    "Compare NPI taxonomy against the actual disputed service; a specialty label alone cannot establish clinical complexity or facility eligibility.",
                    "Save the CMS report methodology alongside the spreadsheet; changes in reporting denominators can masquerade as improvements in recovery performance.",
                    "Attach the service-date version of coverage evidence to the case; current directory information cannot establish historical network participation.",
                ],
            },
        },
        {
            "heading": "2. Normalize claim evidence and build a defensible enrichment waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The next four mapped plays are ERA Underpayment Triage, Remittance "
                    "Code Explanation, QPA Disclosure Reconciliation, and Licensed Benchmark "
                    "Enrichment. Begin with authorized X12 835 delivery through the provider's "
                    "clearinghouse or payer channel. Preserve the original interchange and "
                    "parse transaction, claim, service-line, adjustment, remark, and payment "
                    "reference structures without flattening them prematurely. A CARC explains "
                    "an adjustment category; it does not prove the payer violated the "
                    "Act or that the claim belongs in federal IDR. RARCs add context "
                    "but cannot replace the benefit document and actual notice. Track "
                    "payer claim identifiers, service dates, modifiers, units, rendering "
                    "NPI, location, and remittance trace references as distinct fields. "
                    "Corrected claims and reversals must reference their predecessors. "
                    "If 2,000 service lines arrive monthly and rules flag eight percent, "
                    "160 lines need review; at seven minutes each, the queue consumes "
                    "about 18.7 hours before evidence collection. That is a staffing "
                    "input, not 160 payable disputes. Route missing QPA disclosures "
                    "to a document request, contradictory adjustments to analyst review, "
                    "and suspected duplicates to a reconciliation queue. Never promote "
                    "a code match directly into a demand packet without verifying "
                    "the coverage and service circumstances."
                ),
                (
                    "The enrichment waterfall should spend progressively, stopping whenever "
                    "a cheaper authoritative source answers the question. First use the "
                    "engagement records, 835, explanation of benefits, and payer's required "
                    "QPA disclosures. Next consult official identity and jurisdiction records. "
                    "Then request missing encounter evidence from the provider through a "
                    "secure channel. Only after eligibility is supportable should the desk "
                    "buy licensed benchmark observations or commission clinical analysis. "
                    "FAIR Health products can inform market context under their license "
                    "terms; access to a website does not establish permission to scrape "
                    "or redistribute a database. CMS Medicare schedules can help detect "
                    "unit errors and implausible coding assumptions, but public-payer "
                    "reimbursement rates are among the prohibited considerations in federal "
                    "IDR determinations. Likewise, do not use usual-and-customary charges "
                    "or billed charges as award-setting evidence. Keep those diagnostics "
                    "outside the submitted merits packet. Offer construction must follow "
                    "the current governing statute, operative rules, and applicable judicial "
                    "decisions, rather than treating a benchmark multiplier as entitlement. "
                    "If twenty eligible cases require an illustrative $35 licensed "
                    "lookup allocation each, the enrichment budget is $700; if ten "
                    "fail routing first, purchasing only the remaining ten saves $350 "
                    "without sacrificing admissible evidence."
                ),
                (
                    "Treat HIPAA architecture as part of the data model. Execute "
                    "Business Associate Agreements where required under 45 CFR §§ 164.502(e) "
                    "and 164.504(e), and confirm that the selected vendor service, storage "
                    "region, support access, and subcontracting arrangement are covered. "
                    "A vendor's healthcare marketing page is not the agreement. Apply "
                    "minimum-necessary access to caseworkers, segregate prospecting data "
                    "from claim evidence, encrypt stored and transmitted records, and "
                    "record access events without copying clinical narratives into ordinary "
                    "application logs. HHS OCR's breach portal is a diligence signal "
                    "about reported incidents, not a certification of current security. "
                    "Use it to frame vendor questions rather than automatically rejecting "
                    "every listed entity. Validate parsers against authorized test fixtures "
                    "or genuinely synthetic examples before processing production remittances. "
                    "A payment reversal, split remittance, duplicate interchange, negative "
                    "adjustment, or changed claim identifier must produce an explainable "
                    "result. Five fixtures covering those patterns are worth more than "
                    "a dashboard showing thousands of untested rows. For restricted "
                    "data, fallback means an approved provider transfer channel and "
                    "manual structured extraction, not uploading the record to a public "
                    "converter or general enrichment service. Retain required security "
                    "documentation separately from the retention schedule chosen for "
                    "the underlying claim artifacts."
                ),
            ],
            "table": {
                "caption": "Evidence Directory: Six Claim, Benchmark, and Vendor-Diligence Resources",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method",
                    "Cost tier and acquisition boundary",
                    "Refresh and latency treatment",
                    "Rate-limit and retrieval hygiene",
                    "Fallback evidence when coverage breaks",
                ],
                "rows": [
                    [
                        "Availity Essentials provides authorized payer transactions and remittance access",
                        "Use https://www.availity.com/ customer enrollment and contracted payer-supported delivery channels",
                        "Basic and paid offerings differ; confirm transaction and connectivity charges",
                        "Remittance arrival follows payer release and the contracted delivery schedule",
                        "Honor contracted transaction limits; deduplicate files using interchange control identifiers",
                        "Obtain provider-authorized payer portal exports or existing clearinghouse remittance delivery",
                    ],
                    [
                        "X12 external code lists explain adjustment and remittance remark codes",
                        "Read published CARC and RARC lists through https://x12.org/codes official pages",
                        "Published access and redistribution rights differ; verify intended license scope",
                        "Track effective and retirement dates rather than assuming timeless code meanings",
                        "Cache permitted reference copies and avoid repeatedly crawling identical lists",
                        "Preserve payer notice explanations and obtain properly licensed reference material",
                    ],
                    [
                        "FAIR Health licensed products provide carefully bounded market context",
                        "Request product scope and delivery terms through https://www.fairhealth.org/ sales channels",
                        "Commercial pricing is negotiated; consumer access does not license extraction",
                        "Record release vintage, geography, sample scope, and contractual update schedule",
                        "Use only contracted query channels and observe purchased usage allowances",
                        "Proceed with permissible case evidence rather than inventing benchmark observations",
                    ],
                    [
                        "CMS Physician Fee Schedule files support internal coding sanity checks",
                        "Download applicable year files through https://www.cms.gov/medicare/payment/fee-schedules/physician official pages",
                        "Public files are free; these rates are excluded award-setting considerations",
                        "Load service-year versions and applicable revisions with dated manifests",
                        "Download once per release and perform repeated comparisons locally",
                        "Use licensed coding references and provider coding review for discrepancies",
                    ],
                    [
                        "HHS OCR breach portal informs focused vendor security diligence",
                        "Search reported incidents at https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf official public interface",
                        "Public access is free; absence does not establish vendor safety",
                        "Check during onboarding and periodically; reports are not live telemetry",
                        "Use narrow manual searches and avoid harvesting unrelated incident records",
                        "Request vendor incident history, remediation evidence, and contractual security commitments",
                    ],
                    [
                        "CMS QPA disclosure guidance clarifies payer information request requirements",
                        "Use https://www.cms.gov/nosurprises guidance and current official implementing rule links",
                        "Public guidance is free; obtaining payer-specific disclosures requires authorized requests",
                        "Review revisions monthly and verify operative requirements before disputed filings",
                        "Cache guidance versions and keep payer requests outside public channels",
                        "Use 45 CFR § 149.140 and the payer's actual disclosures",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Accept a traceable source artifact",
                    "action": "Receive the authorized ERA and associated notice through an approved channel.",
                    "detail": "Record sender, receipt time, content hash, coverage period, and immutable storage reference before parsing.",
                },
                {
                    "step": 2,
                    "title": "Normalize without losing lineage",
                    "action": "Extract claim and service-line records while retaining adjustment relationships.",
                    "detail": "Preserve original identifiers, reversals, payer traces, code-list versions, and links back to source segments.",
                },
                {
                    "step": 3,
                    "title": "Resolve eligibility before buying enrichment",
                    "action": "Verify service circumstances, applicable payment regime, and deadline evidence.",
                    "detail": "Request missing plan documents first; buy licensed context only for cases that remain supportable.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and release a review packet",
                    "action": "Compare parsed totals with the remittance and route exceptions to an analyst.",
                    "detail": "Require an explained difference of zero or a documented adjustment before the packet enters deadline processing.",
                },
            ],
        },
        {
            "heading": "3. Control deadlines, portal evidence, and restrained commercial signals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The next three mapped plays are Open-Negotiation Deadline Control, "
                    "IDR Portal Receipt Capture, and Cooling-Off Cohort Control. Model "
                    "deadlines as events with evidence, not dates someone typed into "
                    "a calendar. Under the federal framework, distinguish the window "
                    "for initiating open negotiation after initial payment or denial "
                    "from the thirty-business-day negotiation period itself. Then calculate "
                    "the four-business-day initiation window following that period using "
                    "the operative counting instructions and any applicable extensions. "
                    "Certified entity selection is a separate procedural step; four "
                    "business days is not a universal entity-selection or batching "
                    "deadline. Capture the triggering notice, delivery method, receipt "
                    "evidence, calculation version, holiday assumptions, and reviewer. "
                    "Maintain both the statutory due date and an earlier internal "
                    "target. If twelve cases approach a filing window and each "
                    "needs twenty minutes of final verification, reserve four analyst "
                    "hours before the internal target. Portal downtime does not "
                    "automatically suspend a deadline. Preserve outage evidence and "
                    "follow CMS's current documented assistance or extension process. "
                    "Never treat an email to support as proof of a filed dispute. "
                    "The fallback is a documented escalation using authorized channels, "
                    "with the case visibly unresolved until an actual receipt exists."
                ),
                (
                    "Use the CMS Federal IDR portal as the submission system of "
                    "record, not as an assumed general-purpose API. Do not invent "
                    "a bulk endpoint or automate interactive credentials around portal "
                    "restrictions. Capture confirmation identifiers, submitted versions, "
                    "fee instructions, entity communications, and determinations through "
                    "authorized access. Reconcile internal status to those artifacts "
                    "daily during active filing windows. Cooling-off logic must attach "
                    "the determination event to the relevant parties and same or "
                    "similar items or services under the operative rule. Do not "
                    "reduce every case to payer brand plus procedure code. Track "
                    "the ninety-calendar-day restriction and the applicable subsequent "
                    "initiation window separately; do not confuse this clock with "
                    "the thirty-business-day negotiation clock. Batching needs its own "
                    "dated eligibility test because governing rules and judicial "
                    "decisions can change permissible grouping. Similar spreadsheet "
                    "rows are not sufficient proof. At forty candidate lines, "
                    "a proposed four-case batch may reduce duplicated preparation, "
                    "but model four separate filings until grouping is confirmed. "
                    "Fee savings belong in the forecast only after eligibility "
                    "is documented. Google Calendar or Microsoft Outlook can mirror "
                    "internal reminders, but the event ledger and preserved source "
                    "documents must remain authoritative when reminders are edited "
                    "or invitations fail."
                ),
                (
                    "The eleventh mapped play is saas_technographic_churn_pixel_scraping, "
                    "applied only to permitted public commercial pages and DNS records "
                    "for prospect timing, never patient-facing authenticated systems. "
                    "Weekly comparisons can observe additions or removals of Salesforce, "
                    "HubSpot, Marketo, Segment, or NetSuite indicators where those "
                    "indicators are actually public. A weekly crawl cannot establish "
                    "the exact installation day; retain an interval between the "
                    "last negative and first positive observation. A removed script "
                    "might reflect a tag-manager change, regional delivery, or "
                    "site redesign rather than churn. Treat months ten through "
                    "eleven after an observed installation as a weak outreach "
                    "hypothesis, not a known annual renewal date. For 200 practice "
                    "domains checked weekly, approximately 800 monthly page checks "
                    "at an illustrative $0.02 allocated processing cost total $16; "
                    "twenty ambiguous signals receiving eight minutes of review "
                    "consume another 160 minutes. Those figures exclude commercial "
                    "license charges and are not vendor quotes. Confirm apparent "
                    "switches with passive DNS TXT/CNAME history and public job-posting "
                    "mentions before routing outreach. Stop on access restrictions, "
                    "cache results, and never use this play as evidence of "
                    "claim eligibility, clinical acuity, payer behavior, or collectible "
                    "IDR proceeds."
                ),
            ],
            "table": {
                "caption": "Workflow Directory: Six Filing, Calendar, and Commercial-Signal Resources",
                "headers": [
                    "Named resource and operating purpose",
                    "Exact access method",
                    "Cost tier and acquisition boundary",
                    "Refresh and latency treatment",
                    "Rate-limit and retrieval hygiene",
                    "Fallback evidence when coverage breaks",
                ],
                "rows": [
                    [
                        "CMS Federal IDR portal records authorized dispute submissions and receipts",
                        "Enter through https://www.cms.gov/nosurprises/help-resolve-payment-disputes and its current official portal link",
                        "Access requires authorization; administrative and entity fees follow operative schedules",
                        "Review active cases daily; preserve each actual submission confirmation immediately",
                        "Use permitted interactive workflows; assume no undocumented bulk submission interface",
                        "Follow published CMS assistance procedures while retaining deadline and outage evidence",
                    ],
                    [
                        "CMS certified IDR entity list supports entity and fee verification",
                        "Open the current certified entity list through https://www.cms.gov/nosurprises official navigation",
                        "Public list is free; entity charges depend on applicable published terms",
                        "Verify certification, availability, conflicts, and fees before each selection decision",
                        "Cache dated list copies and inspect changes before reusing prior selections",
                        "Confirm current details through official CMS instructions and entity communications",
                    ],
                    [
                        "OPM federal holiday schedules assist business-day calendar validation",
                        "Read annual schedules at https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ official calendar page",
                        "Public calendar access is free; deadline interpretation remains case-specific work",
                        "Load applicable years and verify observed days before deadline calculation",
                        "Retrieve annual schedules once and test locally against operative counting rules",
                        "Use controlling procedural instructions when calendar assumptions produce conflicting dates",
                    ],
                    [
                        "BuiltWith domain technology reports corroborate public commercial software observations",
                        "Use https://api.builtwith.com/ documentation with an authorized subscription API key",
                        "Commercial access is plan-dependent; confirm credits and permitted reuse contractually",
                        "Provider observation dates may lag changes; preserve returned detection timestamps",
                        "Cache domain results, cap credits, and obey documented account throttles",
                        "Inspect permitted public page evidence and independently corroborate vendor migration",
                    ],
                    [
                        "DNSDB passive DNS records help bracket historical domain infrastructure changes",
                        "Use contracted DNSDB API access documented at https://docs.dnsdb.info/ official site",
                        "Commercial access and query allowances depend on the selected agreement",
                        "Historical first-seen and last-seen observations are not exact deployment timestamps",
                        "Check remaining quota and narrow queries to authorized commercial research scope",
                        "Use present DNS TXT/CNAME answers plus public job-posting technology mentions",
                    ],
                    [
                        "Google Public DNS resolves current public TXT and CNAME answers",
                        "Query https://dns.google/resolve with name and type parameters for permitted domains",
                        "Public resolver access is free; it supplies no contractual monitoring SLA",
                        "Answers reflect DNS caching and TTL rather than deployment event history",
                        "Honor TTL, cache answers, serialize retries, and stop repeated failed lookups",
                        "Use the operating-system resolver and preserve response time with returned records",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four facts before the filing package leaves the desk",
                "body": (
                    "A complete packet needs a supported jurisdiction decision, a "
                    "defensible clock, permissible evidence, and a case-level cash model."
                ),
                "items": [
                    "Confirm coverage, service circumstances, applicable state payment rules, and federal eligibility from encounter-specific documents rather than payer branding.",
                    "Recompute negotiation and initiation deadlines from preserved triggering events, current counting instructions, and documented extensions.",
                    "Check batching eligibility, cooling-off relationships, entity status, and the current fee schedule using dated official sources.",
                    "Remove prohibited award-setting considerations and verify that expected contingency earnings depend on incremental collected cash after unrecovered fees and casework allocations.",
                ],
            },
        },
        {
            "heading": "4. Reconcile collections, test failure modes, and protect the scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The twelfth mapped play is Cash-Verified Contingency Reconciliation. "
                    "Build its ledger around money received, not offers selected. "
                    "Suppose the payer initially paid $1,200, an IDR determination "
                    "sets total payment at $4,200, and only $2,400 of the "
                    "additional $3,000 has actually arrived. Collected incremental cash "
                    "is $2,400; the remaining $600 stays a receivable and earns "
                    "no contingency fee under this model. For illustration, allocate "
                    "$120 of non-refundable administrative expense, $80 of other "
                    "unrecovered case fees, and $200 of casework to the collected "
                    "increment. These are modeling amounts, not the current CMS "
                    "fee schedule. The distributable recovery basis is $2,000; a "
                    "25% contractual operator share earns $500. Record certified "
                    "entity fee deposits separately while disposition is pending. "
                    "Return of the prevailing party's deposit must be supported "
                    "by the applicable procedure and actual refund evidence; losing "
                    "or ineligible-case deposits must not become assumed refunds. "
                    "Treat unrecovered amounts as costs unless a documented refund "
                    "right supports a receivable. Define who advances expenses, "
                    "how recoveries reimburse them, and which casework charges reduce "
                    "the sharing basis. A dollar allocated before the split "
                    "cannot also be deducted a second time from the same "
                    "operator earnings calculation."
                ),
                (
                    "Formula v2.0 remains fixed despite the illustrative case arithmetic. "
                    "Conservative recognized operator revenue is $110,000, allowable total "
                    "operator expense is $77,000, and owner net profit is $33,000 "
                    "at 30%. Base revenue is $505,000, expense is $287,850, and "
                    "profit is $217,150 at 43.0%. Scaled revenue is $900,000, "
                    "expense is $396,000, and profit is $504,000 at 56%. "
                    "These figures exclude initial provider collections, payer principal, "
                    "uncollected awards, and recoveries belonging to the provider. "
                    "At the illustrative $500 earned share per completed collection "
                    "equivalent, the revenue targets require 220, 1,010, and 1,800 "
                    "equivalents annually. They are collection equivalents, not required "
                    "filing counts or promised outcomes. If only 80% of otherwise "
                    "comparable completed matters reach that collection level during "
                    "the year, illustrative work volumes rise to 275, about 1,263, "
                    "and 2,250 matters respectively. Test whether the assigned "
                    "1 FT + 2 C, 1 FT + 2 C, and "
                    "2 FT + 3 C teams can support those queues. "
                    "Apply principal-versus-agent analysis under ASC 606 to actual "
                    "contracts; the scorecard here counts earned operator shares, "
                    "not gross provider recoveries passed through an account. "
                    "Maintain separate expense buckets so case allocations and "
                    "operator overhead reconcile without duplicate deductions."
                ),
                (
                    "Turn the scorecard into a diagnostic dashboard with four "
                    "independent measures: evidence completeness, procedural timeliness, earned "
                    "revenue, and cash aging. Do not combine them into a "
                    "single success percentage. An eligible, timely, prevailing dispute "
                    "can still have an unpaid balance. Match supplemental ERAs "
                    "to bank deposits and provider posting records, then flag "
                    "unmatched receipts, recoupments, reversals, and cross-claim offsets "
                    "before issuing the contingency invoice. Use SQLite for a "
                    "small local reconciliation prototype or PostgreSQL for a "
                    "controlled multiuser ledger; neither product choice substitutes "
                    "for access restrictions, backup testing, and audit history. "
                    "Keep protected records out of source control, telemetry "
                    "exports, and prospecting systems. Test recovery from a backup "
                    "using a restricted environment and document elapsed restoration "
                    "time. A nightly job should produce an exception count, "
                    "oldest unresolved age, and named owner, not merely a "
                    "green execution status. Review the eight controls below "
                    "weekly and before every material parser or rule change. "
                    "If an input feed fails, freeze affected decisions while "
                    "preserving unaffected work. The useful automation boundary "
                    "is precise: software assembles traceable evidence and calculations; "
                    "accountable staff resolve disputed facts, confirm submissions, "
                    "and authorize collection-based billing only after the "
                    "underlying cash movement is matched."
                ),
            ],
            "table": {
                "caption": "Eight Diagnostic Controls Linking Evidence Quality to Earned Operator Revenue",
                "headers": [
                    "Control and concrete failure mode",
                    "Repeatable test and required evidence",
                    "Operating threshold or unit calculation",
                    "Fallback and accountable operator action",
                ],
                "rows": [
                    [
                        "Duplicate remittance ingestion inflates apparent incremental recovery and revenue",
                        "Replay the identical interchange and compare claim, line, and cash counts",
                        "Second ingestion creates zero additional recognized receipts or earned shares",
                        "Quarantine collisions and have the reconciliation owner inspect original artifacts",
                    ],
                    [
                        "Incorrect jurisdiction exposes the desk to unrecovered ineligible-case fees",
                        "Require encounter documents supporting coverage, service circumstances, and payment regime",
                        "Every filed case carries a dated and reviewable routing rationale",
                        "Hold submission while the assigned analyst obtains missing plan evidence",
                    ],
                    [
                        "Deadline calculation mistakes convert otherwise supportable recoveries into lost opportunities",
                        "Test holiday boundaries, receipt events, extensions, and negotiation completion dates",
                        "Independent recomputation must match before the internal submission target expires",
                        "Escalate conflicts immediately and preserve the operative procedural source",
                    ],
                    [
                        "Cooling-off grouping errors hide restricted disputes inside superficially similar batches",
                        "Compare parties, services, determination events, and operative grouping requirements",
                        "Every proposed grouping retains its specific eligibility evidence and calculation",
                        "Separate disputed groupings and forecast individual costs until eligibility resolves",
                    ],
                    [
                        "Prohibited benchmark material contaminates an otherwise useful arbitration evidence packet",
                        "Scan final exhibits for billed charges and public-payer rate arguments",
                        "Submitted merits arguments contain only permissible, supported consideration of evidence",
                        "Remove diagnostic exhibits and rebuild the packet with eligible evidence",
                    ],
                    [
                        "Award-based invoicing recognizes operator earnings before incremental cash actually arrives",
                        "Match supplemental payments to bank records, remittances, and provider posting entries",
                        "Illustrative $2,400 collected increment less $400 allocations supports $500 share",
                        "Keep unpaid differences in receivables and defer associated contingency billing",
                    ],
                    [
                        "Refund assumptions and duplicate expenses distort the retained operator margin",
                        "Reconcile fee deposits, confirmed refunds, case allocations, and overhead separately",
                        "Base $505,000 revenue less $287,850 expense equals $217,150 owner profit",
                        "Reverse unsupported refunds and remove duplicated deductions before closing records",
                    ],
                    [
                        "Feed outages or schema changes silently corrupt downstream operational decisions",
                        "Validate source hashes, schema versions, row counts, and required field populations",
                        "Affected records remain quarantined until lineage and totals reconcile successfully",
                        "Restore the last verified snapshot and assign manual handling explicitly",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "A public signal earns attention, a documented claim earns a filing, "
        "and reconciled incremental cash earns the contingency fee."
    ),
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create an eighteen-resource acquisition manifest recording access rights, cost tier, source vintage, local refresh cadence, retry policy, and fallback evidence.",
        "Build separate provider, payer, employer-plan, encounter, and remittance identifiers; attach dated jurisdiction evidence before federal routing.",
        "Test the 835 parser against duplicates, reversals, split payments, negative adjustments, and changed identifiers before ingesting live production files.",
        "Implement separate negotiation, initiation, entity-selection, batching, and cooling-off states with preserved triggering documents and independently checked deadlines.",
        "Keep public-domain technographic research separate from protected claim records; corroborate apparent software switches before commercial outreach.",
        "Close monthly books against matched incremental receipts, confirmed fee dispositions, and nonduplicated expenses; reconcile all three scenarios to the fixed Formula v2.0 scorecard.",
    ],
    "statutory_citations": [
        {
            "title": "42 U.S.C. § 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes the federal surprise-billing framework, negotiation and "
                "IDR provisions, payment considerations, and excluded considerations."
            ),
        },
        {
            "title": "45 CFR § 149.510 — Federal independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.510",
            "relevance": (
                "Provides procedural requirements for negotiation, initiation, entity "
                "selection, fees, batching, and subsequent disputes; verify operative "
                "provisions against applicable court orders and current CMS implementation."
            ),
        },
        {
            "title": "45 CFR § 149.140 — Qualifying payment amount methodology",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-B/section-149.140",
            "relevance": (
                "Supports QPA methodology checks and the required disclosure workflow; "
                "the initial payment and the QPA must remain distinct recorded fields."
            ),
        },
        {
            "title": "45 CFR § 164.502 — Uses and disclosures of protected health information",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502",
            "relevance": (
                "Governs permitted uses and disclosures, minimum-necessary requirements "
                "where applicable, and business associate handling of protected records."
            ),
        },
        {
            "title": "45 CFR § 164.504 — Organizational requirements",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Specifies business associate contract requirements relevant to "
                "clearinghouses, recovery desks, storage services, and subcontractors."
            ),
        },
        {
            "title": "45 CFR § 164.312 — Technical safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312",
            "relevance": (
                "Anchors access control, audit controls, integrity protections, "
                "authentication, and transmission security for electronic protected records."
            ),
        },
        {
            "title": "29 U.S.C. § 1144 — ERISA preemption and statutory exceptions",
            "url": "https://www.law.cornell.edu/uscode/text/29/1144",
            "relevance": (
                "Informs analysis of plan funding, state insurance regulation, "
                "and preemption without making a payer logo a jurisdiction decision."
            ),
        },
        {
            "title": "Texas Insurance Code Chapter 1467 — Out-of-network claim dispute resolution",
            "url": "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.1467.htm",
            "relevance": (
                "Provides a concrete state dispute-resolution framework that must "
                "be evaluated before routing an applicable Texas encounter to federal IDR."
            ),
        },
    ],
}
