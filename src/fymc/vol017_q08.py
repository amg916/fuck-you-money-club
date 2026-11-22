from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small domain investing desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "RDAP, USPTO, CZDS, Archive Evidence, Auction Feeds, and Permissioned Enrichment Under ACPA and Copyright Rules",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #16, Domain Investing, holds Rank #22 with a 83/100 Money-to-Manpower Score. "
        "Its information edge comes from evidence sequencing, not indiscriminate scraping. "
        "This chapter maps eight operating plays: Brandable Inventory Screening; Exact-Match Buyer Mapping; "
        "Expired-Authority Provenance Audits; Drop-Catch Auction Underwriting; UDRP/ACPA Conflict Screening; "
        "Outbound Upgrade Routing; Renewal and Comparable-Sale Control; and Perceptual-Match Rights Monitoring. "
        "The directory connects official records, licensed commercial datasets, diagnostic tools, and bounded enrichment "
        "to acquisition decisions. Canonical annual owner profits are $3,000 Conservative, $44,000 Base, and "
        "$120,000 Scaled, on gross domain sale proceeds of $20,000, $160,000, and $300,000 respectively. "
        "Acquisition costs and renewals remain inside those margins. Build a provenance ledger that records "
        "source age, access rights, decision impact, and fallback before purchasing another subscription."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$20,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "15% net margin; $3,000 annual owner net profit; 1 FT + 1 C",
        },
        {
            "label": "Base",
            "value": "$160,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "27.5% net margin; $44,000 annual owner net profit; 1 FT + 1 C",
        },
        {
            "label": "Scaled",
            "value": "$300,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "40% net margin; $120,000 annual owner net profit; 2 FT + 2 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Establish source authority before enriching a domain",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a candidate ledger keyed by the lowercase ASCII domain, while retaining its original Unicode "
                    "display form and normalization method. Record the source URL, retrieval timestamp, observation timestamp, "
                    "response status, permitted use, and acquisition hypothesis. These fields prevent a cached registration "
                    "record from masquerading as a current ownership check. Use IANA's RDAP bootstrap file to discover the "
                    "appropriate registry service; do not manufacture endpoints from the suffix. ICANN Lookup supplies a "
                    "human-readable cross-check for supported registrations, but redacted contacts do not identify a buyer "
                    "or establish anonymity as misconduct. Registration, expiration, and update events describe registry "
                    "state rather than a fixed auction release schedule. For Brandable Inventory Screening, an illustrative "
                    "batch of 1,000 names might lose 700 to pronunciation, length, or collision filters before commercial "
                    "enrichment. At an assumed ten cents per paid lookup, screening first saves $70 against enriching every "
                    "name. That is avoided research expense, not domain revenue. Where RDAP is unavailable, fall back to "
                    "the registry's published lookup service and record the gap. Never convert an inaccessible record into "
                    "a clean ownership finding. Preserve response hashes so later reviewers can distinguish changed data "
                    "from changed interpretation without repeatedly requesting the same historical evidence."
                ),
                (
                    "Trademark research belongs ahead of bidding, not after an attractive comparable sale appears. Search "
                    "USPTO Trademark Search for exact wording, stems, phonetic neighbors, and relevant goods or services; "
                    "open TSDR to inspect status and prosecution documents. A dead federal record does not erase common-law "
                    "rights, foreign rights, or continuing marketplace use. WIPO decisions help identify recurring fact "
                    "patterns, but a prior decision involving another string does not resolve the present dispute. Under "
                    "15 U.S.C. 1125(d), confusing similarity and bad-faith intent matter; a geographic or dictionary label "
                    "can still be problematic in its acquisition and use context. UDRP/ACPA Conflict Screening should "
                    "therefore preserve the intended use, plausible independent buyers, advertising categories, and correspondence. "
                    "For Exact-Match Buyer Mapping, use California bizfile or the relevant state's official registry to verify "
                    "entity existence, then inspect the entity's own website for actual operations. SEC EDGAR is useful for "
                    "public-company subsidiaries and business descriptions, not for asserting every subsidiary needs the domain. "
                    "If 40 apparent prospects produce eight independently verified operators, price outreach labor against "
                    "eight, not 40. A registry listing establishes a record; it does not establish interest, purchasing "
                    "authority, or a transferable trademark license."
                ),
                (
                    "Treat freshness as a property of each observation, rather than of the vendor's reputation. DNS answers "
                    "are current only within their observed resolver context and cache lifetime; an archive capture describes "
                    "one historical fetch. A zone file shows delegated names within its coverage, not every registration "
                    "or every available purchase. CZDS access is subject to participating registry agreements, and zone "
                    "differences do not prove that a deleted name can immediately be acquired. Store provider timestamps "
                    "separately from ingestion time, and label desk refresh targets as internal scheduling choices. For "
                    "Drop-Catch Auction Underwriting, refresh the auction page before the bid and verify the platform's "
                    "current participation, payment, and transfer rules. An illustrative $900 acquisition ceiling falls "
                    "to $840 when $60 of unavoidable transfer and near-term renewal expense was omitted from the original "
                    "worksheet. Do not raise the ceiling because another bidder appears. The following directory distinguishes "
                    "public access from paid entitlements and request-time checks from historical indexes. Exact commercial "
                    "prices and quotas must come from the desk's current account terms; budget controls should stop "
                    "requests when those entitlements are exhausted. The fallback is a narrower evidence set and a lower "
                    "bid, not unauthorized scraping."
                ),
            ],
            "table": {
                "caption": "Eighteen Named Sources: Access, Decision Use, Cost Basis, Freshness, and Safe Fallback",
                "headers": [
                    "Named source and exact access method",
                    "Specific operating question answered",
                    "Cost tier and entitlement boundary",
                    "Refresh latency and desk scheduling",
                    "Rate hygiene and fallback evidence",
                ],
                "rows": [
                    [
                        "ICANN Lookup: open https://lookup.icann.org/en and submit the candidate domain.",
                        "Cross-check registrar, domain status, and publicly displayed registration events before acquisition.",
                        "Public interactive lookup is free; displayed contact redactions remain intact.",
                        "Request-time display reflects upstream registration data; recheck immediately before bidding.",
                        "Use interactive checks sparingly; fall back to the registry's published lookup.",
                    ],
                    [
                        "IANA RDAP bootstrap: GET https://data.iana.org/rdap/dns.json, then query the listed service.",
                        "Locate authoritative RDAP endpoints instead of guessing services from domain suffixes.",
                        "Bootstrap access is free; individual registry service policies still govern queries.",
                        "Cache bootstrap responses using HTTP validators; registration freshness belongs to upstream responses.",
                        "Honor upstream throttling and Retry-After; fall back to published registry lookup.",
                    ],
                    [
                        "ICANN CZDS: register at https://czds.icann.org and request participating registry zone access.",
                        "Compare delegated-name snapshots to discover additions and removals for further investigation.",
                        "Participating gTLD zone access is generally free under accepted registry agreements.",
                        "Exports are commonly daily; inspect actual file timestamps and registry schedules.",
                        "Download each authorized snapshot once; fall back to individual RDAP observations.",
                    ],
                    [
                        "USPTO: search https://tmsearch.uspto.gov and inspect case documents through https://tsdr.uspto.gov.",
                        "Find federal trademark records, relevant goods, owners, and prosecution history.",
                        "Public searching and case viewing are free; separate bulk products have terms.",
                        "Record retrieval time and document dates; recheck material findings before acquisition.",
                        "Use supported interfaces without parallel scraping; fall back to counsel-led record review.",
                    ],
                    [
                        "WIPO domain decisions: search https://www.wipo.int/amc/en/domains/search/ using disputed strings and parties.",
                        "Compare documented UDRP fact patterns, remedies, and findings about bad faith.",
                        "Public case searching is free; case text still requires contextual interpretation.",
                        "Decisions appear after publication; older cases do not establish present ownership.",
                        "Read selected decisions manually; supplement with other providers' published decisions.",
                    ],
                    [
                        "California Secretary of State: search entities through https://bizfileonline.sos.ca.gov.",
                        "Verify California entity names and filed status before building buyer hypotheses.",
                        "Basic public searching is free; document orders and certifications may cost extra.",
                        "Filing dates control interpretation; desk refresh occurs before material buyer outreach.",
                        "Use permitted interactive access; fall back to the entity's state registry.",
                    ],
                    [
                        "SEC EDGAR: search https://www.sec.gov/edgar/search/ and retrieve filings through official links.",
                        "Check public-company business descriptions, subsidiaries, and acquisition-related naming changes.",
                        "Public filings and data APIs are free under SEC fair-access conditions.",
                        "New filings follow submission processing; retrieve specific filing dates with evidence.",
                        "Use an identifying User-Agent within SEC limits; fall back to issuer filings.",
                    ],
                    [
                        "Internet Archive CDX: GET https://web.archive.org/cdx/search/cdx?url=example.org&output=json for capture discovery.",
                        "Locate historical site captures for ownership narratives, content changes, and contamination.",
                        "Public access is generally free; service availability and reuse conditions vary.",
                        "Capture dates describe historical observations; missing captures do not prove inactivity.",
                        "Cache indexes and back off on failures; fall back to Common Crawl.",
                    ],
                    [
                        "Common Crawl: discover indexes at https://index.commoncrawl.org/collinfo.json and query selected collection endpoints.",
                        "Recover independent crawl observations when archive coverage is sparse or contradictory.",
                        "Index access and public datasets are free; compute and storage incur costs.",
                        "Collection dates define observation periods; coverage is batch-based rather than continuous.",
                        "Query narrowly and cache results; fall back to archived captures and manual evidence.",
                    ],
                    [
                        "NameBio: search completed sales through https://namebio.com using available account features.",
                        "Build comparable-sale cohorts by extension, length, date, venue, and price.",
                        "Public searches and paid products differ; obtain explicit rights for exports.",
                        "Reported sales appear after ingestion; retain sale date separately from retrieval date.",
                        "Use licensed search or export access; fall back to documented venue results.",
                    ],
                    [
                        "Ahrefs API v3: request https://api.ahrefs.com/v3/site-explorer/backlinks with eligible credentials and parameters.",
                        "Inspect referring pages and link context before paying for expired-authority claims.",
                        "API availability and units depend on current plan or purchased entitlement.",
                        "Provider crawl timestamps govern freshness; request time does not refresh every backlink.",
                        "Budget account units and cache responses; fall back to Majestic and manual checks.",
                    ],
                    [
                        "Majestic API: call https://api.majestic.com/api/json using the documented GetBackLinkData command.",
                        "Cross-check anchor distribution, referring domains, and evidence behind claimed authority.",
                        "API access requires suitable paid entitlement; query volume consumes allocated resources.",
                        "Fresh and historic indexes cover different periods; record chosen index explicitly.",
                        "Respect account resource limits; fall back to Ahrefs samples and source-page inspection.",
                    ],
                    [
                        "Google Web Risk: GET https://webrisk.googleapis.com/v1/uris:search with configured project credentials.",
                        "Check candidate URLs against supported threat lists before controlled browsing.",
                        "Commercial usage follows Google Cloud pricing and any applicable free allowance.",
                        "Responses reflect provider threat data; absence of a match is limited evidence.",
                        "Honor project quotas and cache expiry; fall back to VirusTotal and isolation.",
                    ],
                    [
                        "VirusTotal: GET https://www.virustotal.com/api/v3/domains/{domain} using an appropriately licensed API key.",
                        "Review existing domain reputation observations without automatically submitting private acquisition material.",
                        "Public API restrictions can exclude commercial workflows; obtain suitable commercial rights.",
                        "Inspect analysis timestamps; stored reports can substantially predate the acquisition decision.",
                        "Honor licensed quotas; fall back to Web Risk and isolated manual diagnostics.",
                    ],
                    [
                        "Google Public DNS: GET https://dns.google/resolve?name=example.org&type=MX for JSON DNS observations.",
                        "Check routing, mail configuration, and basic technical context without inferring ownership.",
                        "Public resolver access is free; it is not a bulk-data entitlement.",
                        "Responses reflect resolver cache and TTL; compare authoritative answers when material.",
                        "Cache by TTL and limit concurrency; fall back to local or authoritative DNS.",
                    ],
                    [
                        "GoDaddy Domains API: GET https://api.godaddy.com/v1/domains using an eligible account's credentials.",
                        "Reconcile owned inventory, renewal state, and account-visible domain management information.",
                        "Production eligibility and feature access vary; registration and renewal charges remain separate.",
                        "Account responses are request-time observations; reconcile payment state against billing records.",
                        "Follow account-specific quotas; fall back to authorized dashboard exports and invoices.",
                    ],
                    [
                        "DropCatch: inspect auctions and account exports through https://www.dropcatch.com.",
                        "Verify auction status, bidding rules, deadlines, and acquisition-specific charges before committing.",
                        "Public browsing and account access differ; successful acquisitions incur platform charges.",
                        "Auction status changes during bidding; refresh immediately before the final decision.",
                        "Use supported account workflows only; fall back to manual listing verification.",
                    ],
                    [
                        "Hunter: GET https://api.hunter.io/v2/domain-search with licensed credentials for a verified business domain.",
                        "Locate potential business contacts after entity and domain relevance are established.",
                        "Free allowances and paid credit tiers vary; verification can consume separate credits.",
                        "Inspect source dates and confidence; reverify selected contacts before permitted outreach.",
                        "Set hard credit ceilings; fall back to the company's published contact channel.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy better evidence before buying more inventory",
                "body": "The highest-value data purchase often eliminates a bad acquisition rather than discovering a spectacular sale.",
                "items": [
                    "Save the auction page and cost worksheet together; deadline changes and omitted renewal charges can alter the bid without changing the domain.",
                    "Keep registry event timestamps separate from archive dates; neither one alone proves continuous control by the same registrant.",
                    "Split comparable sales by venue and buyer context before calculating medians; wholesale liquidation and end-user upgrades answer different pricing questions.",
                    "Recheck the strongest referring pages manually; a large authority score can survive after the few economically meaningful links disappear.",
                ],
            },
        },
        {
            "heading": "2. Spend commercial credits only after independent forensic checks",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Expired-Authority Provenance Audits begin with historical use, not a single vendor score. Sample captures "
                    "across the domain's visible life, compare page titles and language shifts, and inspect whether the "
                    "current backlink story matches the old site's subject. Ahrefs and Majestic observe different crawl "
                    "universes, so disagreement is a research prompt rather than a mathematical defect. Inspect high-value "
                    "referring pages for live links, redirects, sponsorship labels, hacked templates, and sitewide repetition. "
                    "A domain with 800 reported referring domains may have only 12 independently useful editorial relationships; "
                    "those 12 still do not promise ranking transfer after a change of ownership or content. Google Web Risk "
                    "and licensed VirusTotal access add threat observations, not a certificate of cleanliness. Browse suspicious "
                    "history in an isolated environment without production credentials, and avoid uploading private deal documents "
                    "to public analysis services. For an illustrative $1,200 candidate, assume $80 of research and a $120 "
                    "renewal reserve: the cash exposure is already $1,400 before selling fees. If provenance remains contradictory, "
                    "value the string without the authority premium or pass. The fallback protects capital without pretending "
                    "that an incomplete crawl proves fraud or that a clean sample proves the entire history."
                ),
                (
                    "Renewal and Comparable-Sale Control requires a deliberately narrow definition of comparable. Separate "
                    "completed sales from asking prices, payment plans from cash settlements, and bundled transactions from "
                    "single-domain deals. NameBio provides discovery, but preserve the reported venue, date, extension, and "
                    "any available verification context. A reported $20,000 sale with no disclosed payment structure cannot "
                    "be treated as immediate cash available to your desk. Use cohorts with similar length, commercial meaning, "
                    "language, and buyer breadth; document why each included observation belongs. For an illustrative five-sale "
                    "cohort of $2,000, $3,000, $4,000, $7,000, and $24,000, the median is $4,000 while the mean is "
                    "$8,000. Underwriting against the mean doubles the apparent center because of one outlier. Stress-test a "
                    "$4,000 exit with a 15% assumed selling fee, producing $3,400 before acquisition, renewal, research, and "
                    "other operating costs. That fee is a model assumption, not a universal marketplace tariff. When reliable "
                    "comparables are scarce, replace false precision with a lower acquisition ceiling and a renewal stop date. "
                    "Track realized portfolio sell-through separately; a database of successful transactions contains no complete "
                    "denominator for the names that never sold."
                ),
                (
                    "Outbound Upgrade Routing should identify relevant businesses before identifying individual people. Start "
                    "with official entity records and the business's published website, then inspect whether the proposed "
                    "domain offers a defensible descriptive improvement. Avoid candidates whose only plausible value comes "
                    "from another party's distinctive mark. Use Hunter or a comparable licensed service only after that "
                    "relevance check, and verify the chosen address through permitted methods rather than broad mailbox probing. "
                    "A practical waterfall is company contact page, licensed domain search, licensed verification, then a "
                    "manual business channel if evidence remains weak. For 50 researched companies, assume 20 suitable contacts "
                    "and six minutes of review each: two staff hours, not 50 automatic messages. At $35 per hour and "
                    "$10 of assumed enrichment charges, preparation costs $80 before any response. An affirmative reply is "
                    "not recognized revenue; only a completed domain transaction belongs in the sale ledger. Commercial email "
                    "must satisfy applicable requirements, including accurate headers, a valid postal address, and functioning "
                    "opt-out handling under 15 U.S.C. 7704. Maintain suppression independently of the vendor export so deleted "
                    "leads cannot reappear in the next batch. If contact relevance fails, stop outreach and retain the domain "
                    "only on its independent investment merits."
                ),
            ],
            "table": {
                "caption": "Four Diagnostic Workflows That Convert Vendor Signals into Bounded Acquisition Decisions",
                "headers": [
                    "Workflow and evidence inspected",
                    "Concrete unit economics",
                    "Decision rule and recorded proof",
                    "Failure response and fallback",
                ],
                "rows": [
                    [
                        "Expired-authority audit combines archive captures, referring-page samples, and historical anchor context.",
                        "A $1,200 purchase plus $80 research and $120 renewal reserve exposes $1,400.",
                        "Record live source pages and chronology before assigning any authority premium.",
                        "Remove the premium or decline when history and backlink evidence remain contradictory.",
                    ],
                    [
                        "Comparable-sale review separates completed cash sales from listings, bundles, and installment structures.",
                        "Five illustrated sales produce a $4,000 median and an $8,000 mean.",
                        "Use the relevant cohort and retain every inclusion rationale with the worksheet.",
                        "Lower the bid and shorten the holding plan when reliable comparables disappear.",
                    ],
                    [
                        "Buyer-contact waterfall checks the company website before licensed discovery and address verification.",
                        "Twenty contacts require two review hours; $70 labor plus $10 credits equals $80.",
                        "Send only after relevance, channel suitability, and suppression checks are recorded.",
                        "Use a published business channel or stop rather than guessing personal addresses.",
                    ],
                    [
                        "Reputation diagnostics combine licensed threat reports with isolated inspection of suspicious history.",
                        "Budget review time separately because a free lookup does not eliminate analyst expense.",
                        "Record report age, observed URLs, and the limits of each diagnostic result.",
                        "Avoid production browsing and reject contaminated inventory when remediation cannot be established.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before the desk commits money or contacts",
                "body": "A failed check pauses the affected action while other supported research can continue.",
                "items": [
                    "Confirm the seller or auction platform can deliver control, and verify transfer restrictions, payment deadlines, and the domain's current status.",
                    "Document trademark searches, independent buyer hypotheses, historical use, and any unresolved UDRP or ACPA concerns before acquisition.",
                    "Confirm current vendor permissions, commercial-use eligibility, credit ceilings, and retention restrictions before production enrichment.",
                    "Reconcile the all-in bid, next renewal date, cash reserve, and outreach suppression state against the same candidate identifier.",
                ],
            },
        },
        {
            "heading": "3. Build a small, replayable pipeline instead of an opaque scraper",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A small desk can build a durable research pipeline with Python's urllib.request, json, sqlite3, hashlib, "
                    "csv, and datetime modules, plus operating-system scheduling. This chapter module contains editorial data; "
                    "it does not execute those requests. In the implementation, separate candidate intake, source adapters, "
                    "normalization, evidence storage, and decision exports. Give every observation a stable source identifier "
                    "and content digest, and every acquisition decision a versioned worksheet. Store UTC timestamps with "
                    "explicit timezone offsets. A canonical domain key should preserve both Unicode presentation and the "
                    "validated ASCII form; pin the chosen IDNA behavior because Python's built-in codec and newer standards "
                    "can differ. Reject malformed labels before sending requests, and treat visually confusable names as a "
                    "manual review issue rather than silently merging them. Protect credentials outside source control and "
                    "redact query strings containing keys from logs. Separate rights to query, retain, transform, and "
                    "redistribute data: a paid subscription does not automatically grant all four. If contract terms prohibit "
                    "retaining raw responses, store permitted fields and audit metadata instead. This architecture makes a "
                    "research conclusion reproducible without requiring the next operator to inherit undocumented browser tabs, "
                    "shared passwords, or an unbounded collection of personal contact records."
                ),
                (
                    "Use a cost-aware waterfall whose expensive stages depend on earlier evidence, not on elapsed time. "
                    "An illustrative monthly batch starts with 1,000 candidates, sends 120 survivors to a ten-cent commercial "
                    "lookup, and sends 40 of those to a fifty-cent deeper report. Paid requests cost $12 plus $20, or "
                    "$32. Add eight analyst hours at $35 and the batch costs $312 before subscriptions and infrastructure. "
                    "If four acquisitions result, attributable screening cost is $78 per acquired name; if none result, "
                    "the full $312 remains a research expense. Neither outcome creates sale proceeds. Cache identical requests "
                    "within the source's permitted freshness window, use conditional requests where supported, and impose "
                    "per-provider concurrency and daily spend limits. HTTP 429 should trigger Retry-After handling and jittered "
                    "backoff; authentication failures should stop that adapter rather than rotate identities. Distinguish a "
                    "transport failure, an empty successful response, and a genuinely negative finding in the database. "
                    "Use bounded retries and a manual review queue for unresolved failures. If a paid source becomes "
                    "unavailable, continue free verification and defer the expensive decision; switching to an unlicensed "
                    "mirror would trade a visible data gap for an invisible contractual and evidence-quality problem."
                ),
                (
                    "Renewal tracking deserves stronger controls than speculative lead scoring because its cost is both "
                    "predictable and repetitive. Reconcile registrar exports, invoices, and the internal inventory weekly, "
                    "with desk alerts at 90, 60, and 30 days before the recorded renewal date. Those are internal "
                    "reminders, not assumptions about a registry's grace period. Distinguish registry expiration, registrar "
                    "billing date, auto-renew settings, payment-card validity, and transfer eligibility. For 200 names at an "
                    "illustrative $15 annual renewal each, carrying expense is $3,000 before premium renewals; ten names "
                    "renewing at $150 instead of $15 add another $1,350. A billing mismatch therefore matters more than "
                    "a prettier dashboard. Reconcile inbound inquiries to domain identifiers and route them by asking-price "
                    "band, language, and evidence of buyer relevance. Preserve the original message, but limit personal "
                    "data access and retention to the business purpose. Do not treat automated contact scoring as authority "
                    "to accept a price, initiate a transfer, or issue a refund. Require explicit transaction authorization "
                    "through the desk's own systems. Test restores from backups, replay one historical batch, and compare "
                    "results before changing adapter logic. A pipeline earns trust when it exposes missing evidence and "
                    "unexpected spending rather than smoothing them away."
                ),
            ],
            "table": {
                "caption": "Four Pipeline Controls with Explicit Evidence, Spend, and Recovery Boundaries",
                "headers": [
                    "Control and stored evidence",
                    "Implementation and refresh rule",
                    "Measured economic or operational threshold",
                    "Recovery path when the control fails",
                ],
                "rows": [
                    [
                        "Provenance records retain source identity, retrieval time, observation time, and permitted response digest.",
                        "Use SQLite transactions and versioned schemas; validate every adapter response before insertion.",
                        "Every acquisition worksheet links to retrievable evidence or an explicitly documented evidence gap.",
                        "Quarantine malformed responses and repeat only authorized requests after correcting the adapter.",
                    ],
                    [
                        "Provider budgets track requested units, returned units, errors, and current entitlement balances.",
                        "Apply bounded concurrency, conditional retrieval, and provider-specific cache lifetimes before scheduling requests.",
                        "The illustrated enrichment batch costs $32 in requests and $280 in analyst labor.",
                        "Stop paid stages at the spending ceiling and finish permitted free-source verification.",
                    ],
                    [
                        "Renewal reconciliation compares registrar state, actual invoices, internal ownership, and payment readiness.",
                        "Run weekly reconciliation with internal reminders at 90, 60, and 30 days.",
                        "Two hundred ordinary $15 renewals cost $3,000 before premium pricing adjustments.",
                        "Escalate mismatches for account review without automatically changing billing or transfer settings.",
                    ],
                    [
                        "Outreach suppression stores the minimum channel identifiers needed to prevent repeat unwanted contact.",
                        "Check suppression before every send and preserve restrictions across fresh vendor imports.",
                        "Every permitted outbound message must pass the same current suppression comparison.",
                        "Pause the affected campaign and repair synchronization before generating further outbound messages.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Normalize and identify the candidate",
                    "action": "Validate the domain, preserve its display form, and assign an immutable internal identifier.",
                    "detail": "Record intake source, proposed play, maximum research budget, and any immediate trademark concerns before enrichment.",
                },
                {
                    "step": 2,
                    "title": "Collect authoritative and historical evidence",
                    "action": "Run permitted RDAP, trademark, archive, DNS, and entity checks in the defined source order.",
                    "detail": "Save source dates and retrieval dates separately; route conflicting or inaccessible evidence to manual review.",
                },
                {
                    "step": 3,
                    "title": "Purchase only decision-relevant enrichment",
                    "action": "Request licensed comparable, backlink, or contact data only when the candidate survives earlier checks.",
                    "detail": "Apply current account quotas, commercial-use restrictions, cache rules, and the candidate's remaining research budget.",
                },
                {
                    "step": 4,
                    "title": "Underwrite and reconcile the operating decision",
                    "action": "Approve or reject the investment worksheet through the desk's authorized transaction process.",
                    "detail": "Link all-in cost, renewal reserves, evidence limitations, contact restrictions, and the next review date to the same record.",
                },
            ],
        },
        {
            "heading": "4. Reconcile the scorecard and isolate rights-monitoring economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The scorecard recognizes gross domain sale proceeds, not the buyer's future website sales, the face "
                    "value of inquiries, or a portfolio's asking prices. Conservative revenue is $20,000 and owner profit "
                    "is $3,000, leaving a $17,000 modeled expense envelope. Base revenue is $160,000 and owner profit "
                    "is $44,000, leaving $116,000. Scaled revenue is $300,000 and owner profit is $120,000, leaving "
                    "$180,000. Those figures preserve margins of 15%, 27.5%, and 40%, with teams of 1 FT plus 1 C, "
                    "1 FT plus 1 C, and 2 FT plus 2 C respectively. Illustrative transaction mixes are five sales "
                    "at $4,000, 20 at $8,000, and 25 at $12,000; they explain arithmetic, not predicted sell-through. "
                    "Acquisition costs, renewals, transaction fees, tooling, and other operating costs must fit inside "
                    "the relevant envelope without being deducted twice. Track cash committed to unsold inventory separately "
                    "from the scenario's profit bridge, and reconcile inventory treatment with the actual accounting method. "
                    "Team counts are operating capacity assumptions, not salary quotations. A $2,400 annual software bundle "
                    "consumes 80% of Conservative owner profit if added without offsetting savings or additional realized "
                    "contribution. Start with evidence that changes bids before buying features that merely expand reports."
                ),
                (
                    "The eighth mapped play is copyright_phash_reverse_image_statutory_settlement, the TRACK_2 Perceptual-Hash "
                    "(pHash) Reverse-Image & Audio-Stem Statutory Settlement Engines play. Keep it operationally separate from "
                    "domain trading. Buying an expired domain does not buy the former operator's photographs, recordings, "
                    "licenses, or enforcement authority. Work only for a represented rights holder with documented authority "
                    "and a verified reference library. ExifTool can inspect metadata; perceptual hashes and licensed reverse-image "
                    "services such as TinEye can prioritize visual candidates; Chromaprint can help compare suitable audio "
                    "references. Audio-stem similarity still requires checking composition, recording, samples, and actual licensed "
                    "uses. A match is a triage signal, not an infringement conclusion. Human and counsel review must address "
                    "ownership, registrations, license scope, fair use under 17 U.S.C. 107, other exceptions, and territorial "
                    "facts before any demand. Section 504 permits specified statutory-damages ranges when available, generally "
                    "$750 to $30,000 per work, with court-determined adjustments; it does not price each matching URL. "
                    "Section 412 can bar statutory damages and attorney's fees because of registration timing, subject to "
                    "its exceptions. Section 411(a) also generally requires registration or refusal before suit for United "
                    "States works, subject to statutory exceptions. Preserve these distinctions in the review record rather "
                    "than encoding a demand amount into the matching algorithm."
                ),
                (
                    "Budget the rights-monitoring pilot as a service experiment, not a hidden uplift to domain sales. "
                    "Assume 200 authorized reference comparisons at two cents each, costing $4; 12 flagged candidates "
                    "reviewed for ten minutes each at $45 per hour, costing $90; and two counsel reviews of half "
                    "an hour each at $250 per hour, costing $250. Total illustrated cost is $344. Two voluntary "
                    "licenses at $150 each produce $300 gross receipts and a $44 loss before other costs, demonstrating "
                    "why automated matches cannot substitute for unit economics. These are hypothetical service charges, "
                    "not quoted vendor prices, infringement valuations, or expected settlements. Keep any resulting service "
                    "revenue outside the canonical domain scorecard unless an expressly revised model includes it. Preserve "
                    "the original reference, suspected-use URL, capture date, relevant context, comparison settings, and reviewer "
                    "disposition, while respecting source access rights. Never multiply statutory maximums by detected pages "
                    "to manufacture a receivable. If ownership, licensing, exceptions, or eligibility cannot support the "
                    "position, withdraw unsupported demands and retain matching only for authorized monitoring and voluntary "
                    "licensing. The same discipline applies across all eight plays: evidence should narrow the action, "
                    "cap the spending, and make the fallback executable before anyone mistakes an interesting signal "
                    "for money already earned."
                ),
            ],
            "table": {
                "caption": "Canonical Domain Economics and a Separately Ring-Fenced Rights-Monitoring Pilot",
                "headers": [
                    "Scenario and recognized revenue basis",
                    "Illustrative transaction or workload arithmetic",
                    "Costs, owner profit, and team reconciliation",
                    "Operating constraint and fallback action",
                ],
                "rows": [
                    [
                        "Conservative recognizes exactly $20,000 annual gross proceeds from completed domain sales.",
                        "Five illustrative completed sales at $4,000 each reconcile to $20,000 revenue.",
                        "A $17,000 expense envelope leaves $3,000 profit; 15% margin; 1 FT + 1 C.",
                        "Preserve capital through free-source screening and decline subscriptions without demonstrated contribution.",
                    ],
                    [
                        "Base recognizes exactly $160,000 annual gross proceeds from completed domain sales.",
                        "Twenty illustrative completed sales at $8,000 each reconcile to $160,000 revenue.",
                        "A $116,000 expense envelope leaves $44,000 profit; 27.5% margin; 1 FT + 1 C.",
                        "Tie every paid dataset to acquisition quality, renewal savings, or realized transaction contribution.",
                    ],
                    [
                        "Scaled recognizes exactly $300,000 annual gross proceeds from completed domain sales.",
                        "Twenty-five illustrative completed sales at $12,000 each reconcile to $300,000 revenue.",
                        "A $180,000 expense envelope leaves $120,000 profit; 40% margin; 2 FT + 2 C.",
                        "Expand review capacity without loosening evidence standards, licensing boundaries, or bid ceilings.",
                    ],
                    [
                        "Rights-monitoring receipts remain separate from all three canonical domain-sale revenue cases.",
                        "Two hypothetical voluntary licenses at $150 each produce $300 in gross receipts.",
                        "Illustrated matching, analyst, and counsel costs total $344, producing a $44 pilot loss.",
                        "Withdraw unsupported demands; retain authorized monitoring and voluntary licensing as the fallback.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The information edge is not finding more domains; it is knowing which evidence deserves another dollar.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create a candidate ledger with normalized domain identifiers, evidence timestamps, source permissions, response digests, and versioned bid worksheets.",
        "Configure authoritative RDAP discovery, trademark review, archive sampling, and buyer-entity verification before paid enrichment begins.",
        "Set provider-specific quotas, spending ceilings, cache lifetimes, credential handling, and supported fallback paths for all commercial sources.",
        "Reconcile owned inventory and registrar invoices weekly, with internal renewal reminders at 90, 60, and 30 days.",
        "Validate completed-sale comparables and all-in acquisition costs against the exact Conservative, Base, and Scaled expense envelopes.",
        "Keep represented-rights-holder monitoring separate from domain ownership, require human and counsel review, and withdraw unsupported demands.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 1125(d) — Anticybersquatting consumer protection",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": "Review bad-faith intent, confusing similarity, statutory factors, and remedies before acquiring or marketing domains associated with another party's mark.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Implement accurate transmission information, required sender disclosures, a valid postal address, and effective opt-out processing for covered outbound email.",
        },
        {
            "title": "16 CFR Part 316 — CAN-SPAM Rule",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-316",
            "relevance": "Apply the implementing rules when determining commercial message treatment and designing lawful unsubscribe procedures.",
        },
        {
            "title": "17 U.S.C. 107 — Fair use",
            "url": "https://www.law.cornell.edu/uscode/text/17/107",
            "relevance": "Require contextual human review of the statutory fair-use factors rather than treating perceptual similarity as sufficient evidence of infringement.",
        },
        {
            "title": "17 U.S.C. 411 — Registration and civil infringement actions",
            "url": "https://www.law.cornell.edu/uscode/text/17/411",
            "relevance": "Verify applicable registration or refusal requirements and statutory exceptions before contemplating litigation involving United States works.",
        },
        {
            "title": "17 U.S.C. 412 — Registration timing and available remedies",
            "url": "https://www.law.cornell.edu/uscode/text/17/412",
            "relevance": "Check infringement commencement, publication, registration timing, and statutory exceptions before asserting eligibility for statutory damages or attorney's fees.",
        },
        {
            "title": "17 U.S.C. 504 — Actual damages, profits, and statutory damages",
            "url": "https://www.law.cornell.edu/uscode/text/17/504",
            "relevance": "Distinguish actual damages and attributable profits from eligible statutory awards; avoid multiplying damages ranges by matching URLs.",
        },
        {
            "title": "17 U.S.C. 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": "Verify the required signed writing for applicable copyright ownership transfers; domain acquisition alone does not transfer historical site content rights.",
        },
    ],
}
