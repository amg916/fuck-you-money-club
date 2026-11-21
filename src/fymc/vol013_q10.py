from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) intellectual property licensing team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Royalty Ledgers, Evidence-Bound AI, Renewal Webhooks, and Patent, Brand, Catalog, and Dataset Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #19, Intellectual Property Licensing, holds Rank #13 with a "
        "79/100 Money-to-Manpower Score. Map automation to four operator plays: "
        "patent field-of-use licensing, brand category licensing, catalog rights "
        "licensing, and dataset access licensing. A 1 FT + 3 C pod can target "
        "70%+ repetitive-work reduction by separating evidence collection from "
        "rights decisions, royalty computation from payment release, and prospect "
        "discovery from outbound publication. Python workers, signed webhooks, "
        "versioned contract records, and exception queues carry the repeatable "
        "load; people approve consequential outputs. Canonical annual owner "
        "profits remain $12,500 Conservative, $180,625 Base, and $480,000 Scaled. "
        "The scalable asset is a verified rights-and-obligations ledger that "
        "improves every renewal, audit, referral, and qualified licensing conversation."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$50,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "25% net margin; $12,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "42.5% net margin; $180,625 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual license-fee and royalty revenue; excludes licensee product sales",
            "note": "60% net margin; $480,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build One Evidence Ledger for Four Licensing Plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with four explicit operator plays rather than one generic "
                    "licensing funnel: patent field-of-use licenses, brand category "
                    "licenses, catalog reproduction or distribution licenses, and "
                    "dataset access licenses. Each play shares an asset identifier, "
                    "counterparty identifier, executed agreement, territory, permitted "
                    "use, effective dates, reporting calendar, and evidence bundle. "
                    "Each also needs different proof. Patent records require ownership "
                    "documents, claim scope, jurisdiction, and remaining term; brand "
                    "records require category restrictions and quality-control duties. "
                    "Catalog records distinguish composition, recording, image, and "
                    "other relevant rights instead of assuming one clearance covers "
                    "everything. Dataset records distinguish ownership assertions from "
                    "source permissions, privacy restrictions, and redistribution "
                    "limits. Store normalized records in PostgreSQL or, for an initial "
                    "single-writer implementation, SQLite through Python's sqlite3 "
                    "module. Keep signed documents in restricted object storage and "
                    "record their SHA-256 digests. A search result establishes a lead, "
                    "not authority to license. USPTO Assignment Center and Copyright "
                    "Office records help locate evidence, but public recordation alone "
                    "does not establish a complete chain of title. The full-time "
                    "operator owns commercial decisions; three contractors cover rights "
                    "review, automation and royalty operations, and channel development. "
                    "Their scopes must state response times, review limits, and who "
                    "can substitute during a reporting deadline."
                ),
                (
                    "Implement intake as a durable event pipeline, not a chain of "
                    "unrecoverable spreadsheet edits. An HTTPS receiver accepts uploads "
                    "or supported vendor notifications, verifies the provider's "
                    "signature over the original request bytes, and persists an event "
                    "before acknowledging receipt. Use hmac.compare_digest where the "
                    "provider specifies HMAC, a documented timestamp tolerance, and "
                    "a unique provider event identifier to reject replayed deliveries. "
                    "A Python worker validates the envelope with json, checks required "
                    "fields, and writes a transaction containing the event, asset "
                    "version, and pending work item. Store a content digest alongside "
                    "the event identifier because duplicate documents can arrive "
                    "through different channels. The LLM receives only approved "
                    "document excerpts and returns proposed fields with page references, "
                    "quoted evidence, and an explicit review-needed flag. Validate "
                    "types, permitted values, date formats, and reference locations "
                    "before displaying the proposal. Treat document text as evidence, "
                    "never as instructions that can change tools or permissions. "
                    "Reject embedded requests to publish files, reveal credentials, "
                    "or modify counterparties. Extraction can prepare territory and "
                    "renewal fields, but a person confirms their contractual meaning. "
                    "Keep the accepted value, rejected proposal, reviewer, timestamp, "
                    "and source version so later amendments remain explainable."
                ),
                (
                    "Define the automation denominator before promising 70%+. Measure "
                    "recurring research, qualification, fulfillment preparation, and "
                    "acquisition administration in minutes, while tracking negotiation "
                    "and substantive rights review separately. In an illustrative "
                    "100-item batch, manual execution consumes ten minutes per item, "
                    "or 1,000 minutes. Eighty routine items need one minute of human "
                    "review after automation; twenty exceptions need nine minutes "
                    "each. Retained work is 260 minutes, a 74% reduction within the "
                    "defined repetitive workload. This does not mean that 74% of "
                    "licensing decisions become autonomous. Instrument the first "
                    "four weeks with started_at, completed_at, active_review_seconds, "
                    "exception_reason, and rework_seconds. Report the median and "
                    "slowest decile by play, because dataset permissions and patent "
                    "scope can dominate exceptions. The rights contractor reviews "
                    "new asset authority and material amendments; the operations "
                    "contractor resolves report mappings; the channel contractor "
                    "validates buyer fit. The full-time operator approves price, "
                    "exclusivity, contract issuance, and dispute responses. Consolidate "
                    "routine reviews into scheduled batches, but route expiring notice "
                    "rights and suspected unauthorized use immediately. Automation "
                    "earns additional scope only after sampled outputs remain accurate "
                    "and the exception queue stays within its assigned response window. "
                    "Count correction time against the claimed savings rather than "
                    "hiding it in another person's workload."
                ),
            ],
            "table": {
                "caption": "Four-Play Rights Ledger and Shared Event Controls",
                "headers": [
                    "Record or workflow under operational control",
                    "Evidence required before accepting automated proposals",
                    "Repeatable machine action with bounded authority",
                    "Human decision and recoverable failure response",
                ],
                "rows": [
                    [
                        "Patent field-of-use licensing across expressly identified national rights",
                        "Executed assignments, patent identifiers, claim references, and territorial schedules",
                        "Match identifiers and prepare term alerts without interpreting infringement",
                        "Rights specialist confirms authority and commissions claim analysis when needed",
                    ],
                    [
                        "Brand category licensing with explicit product quality obligations",
                        "Executed grants, approved categories, territories, and inspection provisions",
                        "Route sample submissions and record dated inspection evidence",
                        "Operator withholds release when product approvals remain incomplete",
                    ],
                    [
                        "Catalog reproduction and distribution licensing for identified works",
                        "Work identifiers, ownership shares, clearance documents, and permitted media",
                        "Assemble rights packets and flag conflicting media permissions",
                        "Rights specialist resolves missing shares before issuing any grant",
                    ],
                    [
                        "Dataset access licensing with documented downstream use restrictions",
                        "Source agreements, collection provenance, permitted purposes, and redistribution limits",
                        "Generate scoped delivery manifests without expanding source permissions",
                        "Operator confirms recipient purpose and excludes restricted source records",
                    ],
                    [
                        "Shared intake ledger linking every asset and counterparty",
                        "Original document digest, verified sender, and immutable intake timestamp",
                        "Deduplicate submissions and create transactional work queue entries",
                        "Operations contractor reconciles conflicting versions before replacing accepted fields",
                    ],
                    [
                        "Shared review queue assigning every consequential licensing decision",
                        "Quoted source evidence, proposed change, reviewer identity, and deadline",
                        "Prioritize exceptions while preserving original documents and proposals",
                        "Full-time operator resolves authority conflicts and records decision rationale",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Authority Before Activating a Licensing Workflow",
                "body": (
                    "These four checks precede automated delivery, contract issuance, "
                    "or external claims about available rights."
                ),
                "items": [
                    "Match each asset to executed ownership or sublicensing documents; reconcile gaps instead of treating registry results as complete authority.",
                    "Verify territory, field of use, exclusivity, sublicensing, and existing grants against the current executed agreement and amendments.",
                    "Test reviewer routing with an expired patent, an incomplete catalog clearance, an unapproved brand sample, and a restricted dataset source.",
                    "Confirm webhook signatures, replay rejection, least-privilege credentials, and manual recovery before accepting production events.",
                ],
            },
        },
        {
            "heading": "2. Automate Royalty Reporting Without Automating Contract Interpretation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Turn each executed agreement into a versioned royalty specification "
                    "with an effective interval. Required fields include currency, "
                    "royalty base, rate tiers, permitted deductions, minimum guarantee "
                    "period, advance recoupment rules, reporting deadline, audit rights, "
                    "and payment terms. Use decimal.Decimal for monetary operations "
                    "and preserve the contract's rounding sequence; binary floating "
                    "point should not decide invoices. A Python adapter reads CSV "
                    "reports with csv.DictReader, normalizes product identifiers, and "
                    "rejects unsupported currencies or periods before calculation. "
                    "Require source totals, row counts, and a report digest so a "
                    "corrected file cannot silently overwrite a settled period. For "
                    "an illustrative credited annual minimum, a $30,000 guarantee "
                    "and $24,000 earned royalty produce $30,000 total consideration "
                    "for that period, not $54,000. If earned royalty reaches $42,000, "
                    "the incremental amount above the credited guarantee is $12,000. "
                    "Different agreements can make minimums noncreditable or advances "
                    "recoupable across periods, so never generalize this example into "
                    "a universal rule. Separate amounts earned, billed, received, "
                    "and recognized under the applicable accounting treatment. The "
                    "scorecard revenue line contains operator license fees and "
                    "royalties, never the licensee's underlying product sales. "
                    "A reviewer signs off the contract specification before the "
                    "calculation engine handles its first live report."
                ),
                (
                    "Design reconciliation around independent evidence rather than "
                    "assuming a clean spreadsheet is truthful. Compare reported units "
                    "with contractually available shipment summaries, distributor "
                    "statements, approved SKU lists, prior periods, and return "
                    "schedules. Where the agreement permits access, ingest Shopify "
                    "exports or NetSuite reports through a licensee-authorized "
                    "connection; collect only fields needed for the reconciliation. "
                    "An unexpected rate drop, omitted territory, newly active product, "
                    "or deduction spike becomes a reason-coded exception, not an "
                    "automatic accusation. Store report versions and calculation "
                    "outputs so an audit can reproduce the original invoice. LLMs "
                    "can classify narrative deduction explanations and draft "
                    "clarification requests, but deterministic code calculates money. "
                    "Before an invoice leaves the queue, the operations contractor "
                    "checks the source period, minimum credit, prior payments, and "
                    "material variances; the operator approves disputed charges. "
                    "For failures, distinguish transport errors from semantic errors. "
                    "Retry a temporary connection failure with bounded exponential "
                    "backoff and jitter; quarantine an invalid royalty base without "
                    "repeatedly executing it. After the retry ceiling, retain the "
                    "payload and alert an assigned person. A provider timeout after "
                    "invoice submission requires checking the external invoice "
                    "identifier before resending, preventing duplicate demands "
                    "on a licensee and preserving a coherent collection history."
                ),
                (
                    "Renewal alerts and obligation tracking should share the same "
                    "contract version as the royalty engine. Record expiry, notice "
                    "lead time, delivery method, recipient address, cure periods, "
                    "insurance evidence, product approvals, attribution, and audit "
                    "windows as separately owned obligations. A scheduled Python "
                    "worker uses datetime and zoneinfo to prepare reminders from "
                    "reviewed date rules, then creates internal tasks at 120, 90, "
                    "60, and 30 days where those intervals fit the agreement. "
                    "Those internal reminders do not replace contractual notice "
                    "requirements. If a notice must arrive by registered mail, an "
                    "email task alone does not satisfy delivery. Store dispatch "
                    "evidence and receipt evidence separately, and escalate when "
                    "either remains missing. Amendment intake must invalidate "
                    "affected future jobs and regenerate them against the new "
                    "version; preserve completed actions for auditability. Trademark "
                    "licenses need actual quality-control activity, not merely a "
                    "clause stored in a database. Patent royalty schedules need "
                    "review around expiration rather than automatic extension of "
                    "the same payment basis. On scheduler failure, export the next "
                    "ninety days of obligations into a dated CSV and assign daily "
                    "manual checks until recovery. Rebuild the queue from accepted "
                    "contract records, compare counts and dates, and close the "
                    "incident only after missed deadlines have named owners."
                ),
            ],
            "table": {
                "caption": "Royalty, Renewal, and Obligation Failure-Recovery Matrix",
                "headers": [
                    "Operational event requiring a reproducible processing record",
                    "Deterministic test before moving the workflow forward",
                    "Assigned human review for material business consequences",
                    "Recovery evidence retained after a processing failure",
                ],
                "rows": [
                    [
                        "Quarterly royalty report arrives through authenticated licensee upload",
                        "Validate reporting period, currency, row counts, and source totals",
                        "Operations contractor reviews unexplained differences against independent permitted evidence",
                        "Preserve original file, digest, rejection reasons, and corrected submission",
                    ],
                    [
                        "Credited minimum guarantee intersects earned royalties within one period",
                        "Apply reviewed credit rules without counting the guarantee twice",
                        "Operator approves exceptions involving disputed credits or cross-period recoupment",
                        "Retain prior calculations and reconcile every revised invoice balance",
                    ],
                    [
                        "Licensee submits returns or deductions exceeding historical operating patterns",
                        "Compare deduction categories against expressly permitted contract line items",
                        "Operations contractor requests supporting schedules before accepting material adjustments",
                        "Quarantine unsupported rows while preserving uncontested amounts for review",
                    ],
                    [
                        "Renewal deadline approaches under contract-specific notice delivery requirements",
                        "Calculate reviewed deadlines and confirm recipient and delivery method",
                        "Operator approves commercial renewal position and actual notice content",
                        "Retain dispatch receipts, delivery evidence, and manually assigned follow-up",
                    ],
                    [
                        "Executed amendment changes reporting rates or future obligation dates",
                        "Version effective intervals and regenerate only affected pending jobs",
                        "Rights specialist confirms amendment scope before revised calculations activate",
                        "Compare old and new schedules and preserve completed historical actions",
                    ],
                    [
                        "Invoice provider times out after receiving an issuance request",
                        "Query the provider identifier before retrying the issuance operation",
                        "Operations contractor resolves ambiguous outcomes before contacting the licensee",
                        "Record external status, retry history, and duplicate-prevention decision evidence",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the accepted source package",
                    "action": "Record the executed contract version, report digest, period, and licensee identifier.",
                    "detail": "Reject mismatched periods and unsupported source formats before any monetary calculation starts.",
                },
                {
                    "step": 2,
                    "title": "Calculate and reconcile deterministically",
                    "action": "Apply Decimal-based rate tiers, permitted deductions, minimum credits, and reviewed rounding rules.",
                    "detail": "Compare totals with authorized independent evidence and attach reason codes to every material difference.",
                },
                {
                    "step": 3,
                    "title": "Review consequential outputs",
                    "action": "Present the invoice draft and exception evidence to the assigned contractor and operator.",
                    "detail": "Block external issuance until required reviews are recorded against the exact calculation version.",
                },
                {
                    "step": 4,
                    "title": "Issue once and preserve the trail",
                    "action": "Use a stable issuance identifier, record the provider response, and schedule collection follow-up.",
                    "detail": "Resolve ambiguous provider outcomes by status lookup; retain both source evidence and accepted results.",
                },
            ],
        },
        {
            "heading": "3. Compound Verified Rights into Qualified Distribution",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build programmatic distribution from the accepted rights ledger, "
                    "not from scraped descriptions that imply ownership. Generate "
                    "public landing-page drafts for meaningful combinations of asset "
                    "family, permitted use, territory, and buyer problem. Patent "
                    "pages can describe an application area without asserting that "
                    "a prospect infringes; brand pages can show approved categories "
                    "and the sample-review process. Catalog pages should expose "
                    "cleared preview material with media and territory limits, "
                    "while dataset pages should publish schemas, provenance "
                    "summaries, and synthetic samples where appropriate. Python "
                    "renders structured records into templates, checks required "
                    "fields, escapes untrusted text, and submits drafts for human "
                    "publication review. Avoid thousands of near-identical pages: "
                    "each published page needs distinct buyer utility, current "
                    "availability, and an accountable owner. Track qualified "
                    "inquiries, accepted briefs, diligence completion, and signed "
                    "licenses rather than celebrating impressions. Add a request "
                    "form that captures intended use, geography, distribution "
                    "channel, expected volume, and decision timing. Feed that "
                    "structured demand back into packaging decisions. Repeated "
                    "requests for a territory outside the current grant indicate "
                    "an acquisition opportunity, not permission to sell rights "
                    "the operator lacks. Archive or revise pages immediately "
                    "when exclusivity, ownership, or permission changes make "
                    "their published offers inaccurate."
                ),
                (
                    "Use outbound automation to prioritize a small, defensible "
                    "prospect list, not to manufacture volume. The channel "
                    "contractor defines buyer signals for each play: manufacturers "
                    "entering a relevant application, category operators with "
                    "distribution capability, publishers needing identifiable "
                    "catalog rights, or data teams with a permitted use case. "
                    "Python collects authorized public facts and records the "
                    "source URL, retrieval date, and reason for fit. An LLM "
                    "drafts a concise use-case hypothesis from those facts; "
                    "it must not invent funding, partnerships, infringement, "
                    "or purchasing intent. Review initial messages and every "
                    "new campaign pattern before sending. For U.S. commercial "
                    "email, implement 15 U.S.C. 7704 requirements concerning "
                    "accurate headers, nondeceptive subjects, required sender "
                    "information, opt-out mechanisms, and timely suppression. "
                    "Treat other jurisdictions as separate routing rules rather "
                    "than assuming the U.S. process applies everywhere. Maintain "
                    "a shared suppression list across contractors and tools, "
                    "and stop sequences when someone replies or opts out. "
                    "Integrate a CRM such as HubSpot through least-privilege "
                    "credentials, with a local outbox recording proposed sends "
                    "and delivery status. Cap daily releases to the pod's "
                    "capacity to answer substantive rights questions. A "
                    "positive reply creates a review task, not an automatic "
                    "license offer or unrestricted sample delivery."
                ),
                (
                    "Create a referral loop only where sharing is itself "
                    "permitted. After a successful catalog placement, ask the "
                    "licensee for permission to publish a narrowly described "
                    "case study and provide a tracked introduction link for "
                    "another producer. For brand deals, approved launch "
                    "materials can direct qualified category partners to "
                    "the availability page without implying open sublicensing. "
                    "For datasets, a reproducible evaluation notebook can "
                    "demonstrate schema and permitted analysis using synthetic "
                    "records; never embed restricted source data in a public "
                    "demo. For patents, an approved technical application note "
                    "can attract implementers without disclosing confidential "
                    "claim analysis. Attribute referrals through campaign "
                    "identifiers and record any agreed partner compensation "
                    "separately from royalty deductions. The flywheel is "
                    "specific: clearer evidence improves qualification, better "
                    "qualification reduces diligence friction, successful "
                    "licenses produce approved proof, and approved proof "
                    "creates more relevant inquiries. Measure conversion "
                    "by rights family and acquisition cohort because one "
                    "large deal can distort averages. Rights packaging should "
                    "also respect competition constraints under 15 U.S.C. "
                    "1 and 2; have qualified counsel assess sensitive "
                    "territorial, exclusivity, tying, and pricing provisions. "
                    "Do not let a recommendation model coordinate downstream "
                    "prices or treat competitor disclosures as a shortcut "
                    "to commercial strategy. Share only approved, "
                    "counterparty-appropriate evidence."
                ),
            ],
            "table": {
                "caption": "Distribution Loops with Rights-Specific Qualification and Review",
                "headers": [
                    "Distribution mechanism and intended licensing buyer outcome",
                    "Reusable asset generated from reviewed operational evidence",
                    "Qualification signal worth spending scarce operator time",
                    "Publication boundary and measurable learning feedback loop",
                ],
                "rows": [
                    [
                        "Patent application pages attract implementers within supported fields",
                        "Approved technical summaries referencing available jurisdictions and remaining terms",
                        "Prospect identifies intended implementation, territory, timing, and decision authority",
                        "Specialist reviews scope claims; track completed technical diligence conversations",
                    ],
                    [
                        "Brand category pages attract capable manufacturers and distributors",
                        "Approved category briefs with quality checks and submission requirements",
                        "Prospect demonstrates distribution reach and capacity for product inspection",
                        "Operator reviews brand presentation; track accepted sample review submissions",
                    ],
                    [
                        "Catalog rights pages attract producers with defined release plans",
                        "Cleared previews with explicit media, territory, and duration parameters",
                        "Prospect supplies production identity, intended usage, budget, and timing",
                        "Rights reviewer confirms clearance; track briefs progressing to signed licenses",
                    ],
                    [
                        "Dataset evaluation packages attract buyers with permitted analytical purposes",
                        "Synthetic records, schema documentation, and reviewed provenance summary pages",
                        "Prospect explains recipient roles, permitted purpose, and redistribution needs",
                        "Specialist excludes restricted records; track completed controlled evaluation requests",
                    ],
                    [
                        "Reviewed outbound sequences introduce relevant rights to selected prospects",
                        "Evidence-linked message drafts with accurate sender and opt-out details",
                        "Public operating facts support a specific plausible licensing application",
                        "Channel contractor reviews releases; track replies and suppress all opt-outs",
                    ],
                    [
                        "Permission-based customer introductions connect adjacent qualified licensing buyers",
                        "Approved case studies and tracked links without confidential deal terms",
                        "Referred buyer matches available territory and demonstrated operating requirements",
                        "Operator approves shared proof; track referral diligence and resulting licenses",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make Every Completed License Improve the Next One",
                "body": (
                    "Veteran operators reuse verified evidence and workflow learning, "
                    "not confidential terms or unchecked ownership assertions."
                ),
                "items": [
                    "Publish a field-of-use intake worksheet for patent prospects; it separates application fit from infringement analysis before specialist time is spent.",
                    "Build brand sample-review calendars into onboarding so quality evidence accumulates throughout the license rather than just before renewal.",
                    "Attach stable work identifiers and clearance versions to catalog previews; downstream inquiries then refer to the exact rights package reviewed.",
                    "Distribute synthetic dataset examples with realistic schema constraints; reserve actual records for authorized, scoped evaluation delivery.",
                ],
            },
        },
        {
            "heading": "4. Price the Automation, Prove the Savings, and Rehearse Recovery",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Budget automated runs explicitly instead of calling software "
                    "labor free. For an illustrative routine work item, allow "
                    "$0.018 for model usage, $0.006 for execution and storage, "
                    "and $0.010 for allocated messaging and monitoring, totaling "
                    "$0.034 of machine cost. These are planning assumptions, "
                    "not vendor quotations; measure actual token counts, "
                    "invocations, storage, and subscription allocations. Using "
                    "the earlier batch, retained human effort averages "
                    "2.6 minutes per item. At an illustrative loaded "
                    "review rate of $45 per hour, that adds $1.95, "
                    "producing $1.984 per completed item before separately "
                    "allocated build costs. One thousand monthly items "
                    "therefore consume $34 of machine expense and "
                    "$1,950 of review capacity, or $1,984 combined. "
                    "The ten-minute manual baseline costs $7.50 per "
                    "item at the same rate, a modeled capacity "
                    "difference of $5,516 across that monthly volume. "
                    "Retained salaries and contractor commitments mean "
                    "capacity savings do not automatically become cash "
                    "savings or additional owner profit. Add failed "
                    "runs, rework, specialist escalation, and subscription "
                    "minimums to the measured ledger. Cache accepted "
                    "extractions by document digest and schema version, "
                    "but invalidate them when source documents or "
                    "interpretation rules change. Optimize expensive "
                    "exceptions before chasing fractions of a cent "
                    "in routine model usage."
                ),
                (
                    "Reconcile the operating plan to the canonical scorecard "
                    "without inserting automation savings as a second "
                    "profit stream. Conservative revenue is $50,000, "
                    "with $37,500 of total costs and $12,500 "
                    "owner net profit at a 25% margin. Base "
                    "revenue is $425,000, with $244,375 of costs "
                    "and $180,625 profit at 42.5%. Scaled revenue "
                    "is $800,000, with $320,000 of costs and "
                    "$480,000 profit at 60%. Conservative and "
                    "Base retain 1 FT + 3 C; Scaled "
                    "uses 2 FT + 4 C, six people. "
                    "These total annual cost envelopes are broader "
                    "than the stated $2,000–$15,000 monthly operating "
                    "expense range: reconcile specialist work, rights "
                    "acquisition treatment, and deal-specific costs "
                    "rather than treating that range as total "
                    "annual expenditure. Startup capital remains "
                    "$25,000–$250,000, and first-deal timing remains "
                    "6–24 months. Build the evidence ledger and "
                    "one reporting adapter before funding elaborate "
                    "acquisition infrastructure. A possible Base "
                    "revenue composition is $250,000 of recognized "
                    "license fees plus $175,000 of incremental "
                    "royalties, provided credited minimums are "
                    "not counted twice. That composition illustrates "
                    "the revenue basis; it does not replace "
                    "the canonical case. Test whether collected "
                    "cash covers contractor commitments during "
                    "long diligence cycles, and keep contract "
                    "pipeline value separate from recognized "
                    "revenue and bank receipts."
                ),
                (
                    "Operate the system with a weekly exception review "
                    "and a monthly recovery rehearsal. Track unmatched "
                    "reports, overdue notices, unsupported extracted "
                    "fields, duplicate issuance attempts, suppression "
                    "failures, and aging rights questions. Sample "
                    "accepted outputs as well as rejected ones; "
                    "otherwise the dashboard only shows errors "
                    "the system already knows about. Preserve "
                    "a small reviewed test set for each "
                    "play, including a disputed deduction, a "
                    "changed territory, an expired right, and "
                    "a dataset redistribution restriction. Run "
                    "that set before changing prompts, parsers, "
                    "rate rules, or vendor integrations. A "
                    "failed test freezes the affected automated "
                    "action while unrelated workflows continue. "
                    "Back up the ledger and evidence "
                    "references, then prove restoration into "
                    "an isolated environment with outgoing "
                    "messages disabled. Check record counts, "
                    "document digests, pending obligations, and "
                    "external issuance identifiers before resuming. "
                    "If the LLM becomes unavailable, use "
                    "manual extraction templates; if the CRM "
                    "fails, retain the outbox and suspend "
                    "sends; if reporting ingestion fails, "
                    "accept reviewed CSV submissions. Add "
                    "the second full-time role and fourth "
                    "contractor for the Scaled case only "
                    "when sustained review demand justifies "
                    "the commitments within its cost envelope. "
                    "The target is dependable throughput "
                    "with intact rights controls, not "
                    "the largest possible number of "
                    "unattended actions. Record each incident's "
                    "cause, affected contracts, corrective action, "
                    "and verification evidence."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Measured Automation Operating Controls",
                "headers": [
                    "Scenario or control with an explicit operating boundary",
                    "Revenue or cost measure with its calculation basis",
                    "Staffing or reviewer capacity supporting the stated result",
                    "Decision rule preventing overstated profit or unreliable throughput",
                ],
                "rows": [
                    [
                        "Conservative canonical case during early licensing portfolio development",
                        "$50,000 revenue less $37,500 costs yields $12,500 owner profit",
                        "1 FT + 3 C with tightly scoped specialist assignments",
                        "Preserve 25% margin assumptions without adding hypothetical automation savings",
                    ],
                    [
                        "Base canonical case using the original four-person operating pod",
                        "$425,000 revenue less $244,375 costs yields $180,625 owner profit",
                        "1 FT + 3 C handling reviewed evidence and exception queues",
                        "Preserve 42.5% margin and exclude all underlying licensee product sales",
                    ],
                    [
                        "Scaled canonical case with six people supporting expanded throughput",
                        "$800,000 revenue less $320,000 costs yields $480,000 owner profit",
                        "2 FT + 4 C with explicit reporting and rights coverage",
                        "Preserve 60% margin while budgeting added commitments inside total costs",
                    ],
                    [
                        "Illustrative completed work item including retained human review effort",
                        "$0.034 machine expense plus $1.95 review capacity equals $1.984",
                        "Average review consumes 2.6 minutes at $45 per hour",
                        "Measure retries and rework before claiming savings against manual execution",
                    ],
                    [
                        "Illustrative monthly batch containing one thousand recurring operational items",
                        "$34 machine expense plus $1,950 review capacity equals $1,984",
                        "Retained review requires approximately 43.33 hours across assigned reviewers",
                        "Separate released capacity from actual reductions in committed cash spending",
                    ],
                    [
                        "Monthly restoration rehearsal covering ledger integrity and external actions",
                        "Measure restore duration, missing records, and unresolved external issuance states",
                        "Operations contractor restores records while operator controls resumption decisions",
                        "Disable outward sends until obligations and duplicate protections reconcile",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail and the arithmetic; keep authority, interpretation, and external commitments with accountable people.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create four rights-ledger templates for patent, brand, catalog, and dataset plays, each with source evidence, territory, permitted use, and reviewer ownership.",
        "Deploy a signed-event intake queue with document digests, replay rejection, versioned extraction proposals, and explicit human review of consequential fields.",
        "Implement one Decimal-based royalty adapter and test minimum credits, amendments, deductions, corrected reports, and duplicate invoice prevention.",
        "Generate contract-specific renewal and obligation tasks, then verify actual notice delivery requirements and rehearse the manual calendar fallback.",
        "Publish one reviewed distribution asset per play and connect inquiry qualification, suppression handling, permission-based referrals, and cohort measurement.",
        "Measure repetitive-work minutes, complete-item costs, rework, and recovery results; reconcile all spending to the canonical scenario cost envelopes.",
    ],
    "statutory_citations": [
        {
            "title": "35 U.S.C. 261 — Ownership and assignment",
            "url": "https://www.law.cornell.edu/uscode/text/35/261",
            "relevance": (
                "Patent assignments require written instruments; recordation and "
                "priority provisions make executed transfer evidence and registry "
                "checks important components of chain-of-title review."
            ),
        },
        {
            "title": "17 U.S.C. 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Transfers of copyright ownership generally require a signed "
                "writing; catalog workflows must distinguish ownership transfers "
                "and exclusive grants from other permission arrangements."
            ),
        },
        {
            "title": "17 U.S.C. 101 — Definitions",
            "url": "https://www.law.cornell.edu/uscode/text/17/101",
            "relevance": (
                "The definition of transfer of copyright ownership includes "
                "exclusive licenses and excludes nonexclusive licenses, informing "
                "which evidence and writing requirements apply."
            ),
        },
        {
            "title": "15 U.S.C. 1055 — Use by related companies",
            "url": "https://www.law.cornell.edu/uscode/text/15/1055",
            "relevance": (
                "Related-company trademark use provisions support workflows "
                "that document authorized use and actual quality controls "
                "rather than merely storing a license document."
            ),
        },
        {
            "title": "15 U.S.C. 1127 — Trademark definitions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1127",
            "relevance": (
                "The related-company definition addresses control over the "
                "nature and quality of goods or services, making inspection "
                "and sample-review evidence operationally significant."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Commercial email workflows must handle accurate transmission "
                "information, nondeceptive subjects, required disclosures, opt-out "
                "mechanisms, and statutory suppression deadlines."
            ),
        },
        {
            "title": "15 U.S.C. 1 — Restraints of trade",
            "url": "https://www.law.cornell.edu/uscode/text/15/1",
            "relevance": (
                "Licensing restrictions involving territories, exclusivity, tying, "
                "or pricing require fact-specific competition review rather "
                "than automatic reuse across unrelated deals."
            ),
        },
        {
            "title": "15 U.S.C. 2 — Monopolization",
            "url": "https://www.law.cornell.edu/uscode/text/15/2",
            "relevance": (
                "Exclusionary licensing strategies require scrutiny of market "
                "power and conduct; automated packaging cannot substitute "
                "for that assessment."
            ),
        },
    ],
}
