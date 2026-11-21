from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-domain-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 1 C (2 people) domain investing team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Queues, Registrar Reconciliation, Comparable-Sale Evidence, and Human-Controlled UDRP/ACPA Screening",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #16, Domain Investing, ranks #17 with a 74/100 Money-to-Manpower Score. "
        "Its leverage comes from processing inventory evidence and buyer intent without automating speculative judgment. "
        "This chapter maps eight operator plays: auction sourcing, asset qualification, comparable-sale monitoring, renewal control, "
        "inbound routing, programmatic distribution, outbound upgrades, and transfer fulfillment. A 1 FT + 1 C pod uses Python "
        "workers, authenticated webhooks, constrained language-model outputs, and exception queues to target 72% net time removal "
        "from a measured repetitive-work baseline. Canonical annual owner profits remain $3,000 Conservative, $44,000 Base, "
        "and $120,000 Scaled; the Scaled case requires 2 FT + 2 C. Gross domain sale proceeds, acquisition costs, renewal "
        "exposure, dispute screening, and transfer evidence stay visible throughout."
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
            "heading": "1. Instrument Eight Plays Before Delegating Repetitive Work",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build one asset ledger before connecting auction feeds or a language model. Each domain receives an immutable "
                    "asset identifier, its ASCII IDNA representation, readable display form, registrar account reference, acquisition "
                    "cash paid, expiration timestamp, renewal quote, listing identifiers, and evidence links. Store timestamps in UTC "
                    "and money as integer cents with an explicit currency. A Python scheduled worker can ingest permitted registrar "
                    "exports, normalize marketplace records, and persist changes in SQLite; keep a single writer and enable tested "
                    "backups. Do not treat RDAP responses as an ownership ledger: public registration data can be redacted, delayed, "
                    "or insufficient to establish account control. Reconcile ownership against authenticated registrar records and "
                    "keep contradictory observations in an exception queue. This chapter's eight-play mapping covers auction sourcing, "
                    "asset qualification, comparable-sale monitoring, renewal control, inbound routing, programmatic distribution, "
                    "outbound upgrades, and transfer fulfillment. These are operating workstreams, not eight independent businesses "
                    "or eight additional revenue categories. The full-time owner controls capital, pricing, disputes, and transfers; "
                    "the contractor maintains evidence quality and exception resolution within scheduled hours. Neither role should "
                    "spend the morning copying identical expiration dates between dashboards. Assign every field a source, refresh "
                    "interval, and named reviewer before using it in a consequential decision."
                ),
                (
                    "Use a durable event table rather than a chain of fragile scripts. Each record should contain event_id, "
                    "asset_id, event_type, source, observed_at, payload_hash, processing_state, attempt_count, and next_attempt_at. "
                    "For providers offering signed webhooks, verify the documented signature against the raw request bytes, enforce "
                    "their timestamp tolerance, and reject duplicate delivery identifiers. Providers without suitable webhooks should "
                    "be polled through permitted interfaces; never invent an endpoint or evade a marketplace's access controls. "
                    "Acknowledge a webhook only after durable persistence, then let workers perform enrichment asynchronously. Python's "
                    "json, sqlite3, hashlib, hmac, datetime, and urllib modules cover a lean implementation, although public ingress "
                    "still needs a production-capable TLS endpoint. Route events through explicit states such as received, enriched, "
                    "review_required, authorized, completed, and failed. A model may propose a structured classification, but ordinary "
                    "Python validates required fields, enumerated values, lengths, and referenced evidence identifiers. Treat landing-page "
                    "text, inquiry messages, and auction descriptions as untrusted data, including instructions embedded inside them. "
                    "Keep model credentials separate from registrar credentials. A generated instruction must never become a registrar "
                    "command merely because it arrived in valid JSON. Record the prompt version and model identifier so disputed "
                    "classifications can be reproduced or compared after a change."
                ),
                (
                    "Measure the automation target in minutes removed, not messages generated. Start with a two-week time study "
                    "and classify repetitive handling separately from negotiation, purchase decisions, and dispute assessment. An illustrative "
                    "weekly baseline of 1,000 repetitive-work minutes can yield 800 minutes of machine-executed work while introducing "
                    "80 minutes of sampling, exception review, and maintenance. Remaining human effort is therefore 280 minutes, and "
                    "net removal is 720 minutes, or 72%. That arithmetic does not assert that machines replace 72% of the "
                    "owner's entire job. Log actual handling times across all eight plays, including retries and failed batches. "
                    "The contractor owns routine reconciliation and prepares concise evidence packets; the owner handles irreversible "
                    "actions during two scheduled review windows, with urgent expiration and security exceptions interrupting immediately. "
                    "Review every proposed purchase, material price change, externally sent outbound pitch, ownership transfer, and "
                    "decision to abandon an asset. Sample low-risk research classifications after initial calibration, but return a "
                    "category to full review when its error rate rises. A weekly dashboard should expose minutes saved, unresolved "
                    "exceptions, late renewals, incorrect buyer routing, and unauthorized-action attempts. If review effort exceeds the "
                    "time saved, reduce the workflow's scope rather than celebrating its event volume. Preserve the manual worksheet "
                    "until the automated ledger consistently reconciles."
                ),
            ],
            "table": {
                "caption": "Eight-Play Operating Map for the Owner and Contractor Pod",
                "headers": [
                    "Mapped operator play and business purpose",
                    "Machine work with a bounded scope",
                    "Human responsibility and authority boundary",
                    "Evidence retained for recovery and measurement",
                ],
                "rows": [
                    [
                        "Play one: auction sourcing for relevant acquisition candidates",
                        "Import permitted auction exports and deduplicate domain records",
                        "Owner approves each bid ceiling before auction participation",
                        "Retain auction identifiers, timestamps, ceilings, and actual bids",
                    ],
                    [
                        "Play two: asset qualification before capital becomes committed",
                        "Assemble history, spelling variants, and trademark search evidence",
                        "Contractor investigates flags; owner resolves acquisition suitability decisions",
                        "Retain search dates, source links, and unresolved conflicts",
                    ],
                    [
                        "Play three: comparable-sale monitoring for disciplined asking prices",
                        "Cluster reported sales by extension, structure, and transaction date",
                        "Owner chooses comparable relevance and any resulting price change",
                        "Retain reported prices, source terms, and exclusion explanations",
                    ],
                    [
                        "Play four: renewal control protecting economically justified inventory",
                        "Reconcile expiration dates and forecast upcoming renewal cash",
                        "Owner approves retention policy and individual abandonment decisions",
                        "Retain payment receipts, registrar confirmations, and exception resolution",
                    ],
                    [
                        "Play five: inbound routing toward qualified buyer conversations",
                        "Classify inquiry intent and draft evidence-grounded response suggestions",
                        "Owner handles negotiation and approves binding commercial representations",
                        "Retain original inquiry, classification reasons, and response history",
                    ],
                    [
                        "Play six: programmatic distribution through accurate inventory pages",
                        "Refresh approved listing facts and measure qualified inquiry attribution",
                        "Owner approves public templates and material asset claims",
                        "Retain published versions, change records, and attribution events",
                    ],
                    [
                        "Play seven: outbound upgrades for individually researched prospects",
                        "Prepare relevant prospect packets and suppression-checked draft messages",
                        "Owner approves recipients, domain rationale, and final message content",
                        "Retain contact provenance, opt-out status, and delivery outcomes",
                    ],
                    [
                        "Play eight: transfer fulfillment after verified transaction milestones",
                        "Prepare checklists, reconcile transaction status, and flag transfer stalls",
                        "Owner authorizes credential release through verified transfer channels",
                        "Retain escrow status evidence, registrar receipts, and closure records",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Use Automation to Expose Inventory Friction",
                "body": "Experienced operators automate evidence collection first because a faster bad acquisition compounds carrying costs.",
                "items": [
                    "Keep auction closing time separate from registrar expiration time; a successful auction result does not establish immediate transfer availability.",
                    "Snapshot the actual renewal quote for premium-priced names instead of multiplying a standard registration rate across the portfolio.",
                    "Quarantine unusually high comparable sales until venue, date, payment structure, and reported transaction scope have been checked.",
                    "Maintain an owner-approved fast-transfer enrollment register and disable conflicting instant-purchase listings immediately after a sale.",
                ],
            },
        },
        {
            "heading": "2. Build Renewal, Comparable-Sale, and Inquiry Pipelines That Fail Safely",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Renewal tracking starts with authenticated registrar data and a cash forecast, not a calendar reminder alone. "
                    "Schedule daily reconciliation and create review tasks at 90, 60, 30, 14, and seven days before expiration, "
                    "adjusted for the registrar and registry's actual rules. Those intervals are operating choices, not universal "
                    "grace periods. Record whether auto-renew is enabled, which payment instrument funds it, and when the registrar "
                    "attempts collection. A renewal is complete only after the authenticated expiration date advances and the payment "
                    "record reconciles; a successful HTTP response proves neither condition by itself. Permit automatic renewals only "
                    "within an owner-approved retention policy and spending limit. Route premium renewal surprises, payment failures, "
                    "and account mismatches to immediate human review. Use annual carrying cost and observed inquiry quality to "
                    "prepare keep-or-drop packets, but never let a model silently abandon inventory. The Anti-cybersquatting Consumer "
                    "Protection Act, 15 U.S.C. § 1125(d), makes bad-faith intent and specified domain conduct material; acquisition "
                    "screening must examine the actual name and context. USPTO trademark searches inform that work without exhausting "
                    "possible rights. ICANN's UDRP is a contractual dispute mechanism, distinct from the statute. Preserve acquisition "
                    "rationale and historical use evidence before a dispute requires them."
                ),
                (
                    "Comparable-sale monitoring should produce an evidence packet, not a synthetic appraisal disguised as market truth. "
                    "Import authorized NameBio exports where available under the account's terms, marketplace reports, and the portfolio's "
                    "own closed transactions. Deduplicate repeated reports using the normalized domain, transaction date, venue, and "
                    "reported amount. Store the original currency and any conversion rate separately from the source price. Classify "
                    "extension, character count, word count, linguistic meaning, buyer segment, and whether the record appears to "
                    "describe a domain alone or an operating website. A model can suggest comparable clusters and explain exclusions; "
                    "the owner must review the actual source records before changing reserves or asking prices. Report the count "
                    "and dispersion of observations instead of manufacturing precision from three exceptional sales. Separate wholesale "
                    "auction outcomes from end-user retail purchases and identify installment arrangements when reported. For expired-authority "
                    "assets, use permitted Ahrefs or Majestic exports alongside Internet Archive evidence to investigate topical changes "
                    "and suspicious link histories. Historical links do not establish current traffic, transferable trust, or a future "
                    "search position. Record missing evidence as an explicit investigation task in the ledger rather than filling "
                    "the gap with a model's plausible story. Never publish estimated traffic as measured traffic."
                ),
                (
                    "Inbound routing should distinguish a buyer, a broker, a spam message, a dispute notice, and an account-security "
                    "alert before optimizing response speed. Connect the landing-page form and dedicated sales mailbox to one event "
                    "queue, retain the original message, and attach only the minimum necessary content to model requests. Strip active "
                    "markup, isolate attachments, and avoid fetching arbitrary inquiry links automatically. Deterministic rules should elevate "
                    "ownership complaints, legal-service language, registrar security warnings, and unexpected payment instructions regardless of model "
                    "confidence. For ordinary inquiries, extract the requested domain, proposed budget, timing, and contact channel, then "
                    "draft a response using approved inventory facts. An acknowledgment may be automatic within a preapproved template; "
                    "offers, discounts, exclusivity promises, and escrow instructions need owner review. Confidence scores require calibration "
                    "against labeled cases and cannot substitute for evidence. Failure handling is equally concrete: cap retries, use "
                    "exponential backoff with jitter, and move exhausted events into a failed-event queue with a named assignee. "
                    "If the model provider is unavailable, route through deterministic categories and the original message. If the "
                    "registrar feed fails, retain the last confirmed date with its observation timestamp and start manual reconciliation. "
                    "Silence from a vendor must appear as stale evidence, never as a clean bill of health."
                ),
            ],
            "table": {
                "caption": "Evidence, Escalation, and Recovery Rules for Core Domain Pipelines",
                "headers": [
                    "Pipeline condition requiring explicit handling",
                    "Deterministic check before trusting the event",
                    "Human escalation and bounded operating response",
                    "Recovery evidence required to close the incident",
                ],
                "rows": [
                    [
                        "Renewal payment accepted without an advanced expiration date",
                        "Compare authenticated registrar dates against the previous snapshot",
                        "Contractor investigates immediately while owner protects remaining renewal time",
                        "Close only with updated expiration evidence and reconciled payment",
                    ],
                    [
                        "Premium renewal quote exceeds the approved carrying budget",
                        "Compare current quote with asset-specific authorized renewal limits",
                        "Owner decides retention before any additional charge is initiated",
                        "Retain revised spending authorization or documented abandonment instruction",
                    ],
                    [
                        "Comparable sale appears repeatedly across several reporting sources",
                        "Match normalized domain, transaction date, currency, and reported price",
                        "Contractor merges duplicate reports without inflating comparable sample size",
                        "Preserve original source references beneath one transaction record",
                    ],
                    [
                        "Buyer inquiry contains a plausible ownership dispute allegation",
                        "Prioritize explicit claim language independently of model confidence",
                        "Owner pauses affected outreach and obtains specialist assessment",
                        "Retain original message, asset history, and documented handling decision",
                    ],
                    [
                        "Webhook delivery repeats after an upstream network timeout",
                        "Check unique delivery identifier before applying any state change",
                        "Contractor reviews only conflicting payloads or inconsistent transaction states",
                        "Retain one committed transition and all duplicate delivery references",
                    ],
                    [
                        "Model response cites evidence absent from the asset ledger",
                        "Validate every cited source identifier against stored evidence records",
                        "Reject the draft and route original evidence for review",
                        "Retain rejected output, validation error, and corrected human classification",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Boundaries Before Enabling Live Actions",
                "body": "Research automation can run broadly; money, public claims, and ownership changes require narrower authority.",
                "items": [
                    "Confirm authenticated account control, current expiration evidence, and the exact renewal quote before enabling policy-based renewal execution.",
                    "Complete documented trademark and historical-use screening before approving a bid, outreach campaign, or disputed asset listing.",
                    "Test that the model has no registrar write credentials and cannot bypass review through a forged event state or embedded instruction.",
                    "Verify duplicate handling, failed-event ownership, backup restoration, and manual transfer procedures using a nonproduction transaction rehearsal.",
                ],
            },
        },
        {
            "heading": "3. Compound Qualified Distribution Without Manufacturing Demand",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Programmatic distribution begins with accurate inventory pages that answer a buyer's next question, not thousands "
                    "of thin pages chasing unrelated searches. Generate one canonical landing page per owned domain from approved "
                    "ledger fields: spelling, pronunciation guidance where useful, extension, asking-price policy, transaction method, and "
                    "a working inquiry channel. Group relevant assets into genuinely useful collections, such as short industrial "
                    "software names or plain-language local service names, only when the portfolio supports those descriptions. Do "
                    "not invent businesses, testimonials, search demand, or revenue associated with an undeveloped asset. An approved "
                    "template may publish routine factual updates automatically; material claims and new positioning require review. "
                    "Keep ownership verification and listing status synchronized with Afternic or Sedo through permitted account workflows "
                    "and exports rather than assumed APIs. Fixed-price listings create execution risk when prices disagree across "
                    "venues or an asset remains purchasable after sale. Make sale detection trigger immediate delisting tasks, "
                    "including a manual fallback when remote updates fail. The distribution loop is specific: useful collection "
                    "pages attract relevant visitors, inquiries reveal vocabulary and objections, and approved revisions improve the "
                    "next visitor's understanding. Track qualified conversations per owned domain and per collection, not merely page "
                    "count, impressions, or model-generated descriptions. Retire pages immediately when ownership ends."
                ),
                (
                    "Outbound upgrades should start with a plausible commercial fit and clean rights screening, not a purchased "
                    "list sprayed with generated praise. A prospect using a long descriptive address may value a shorter "
                    "generic alternative, but similarity to their protected brand can create the opposite outcome. Never frame "
                    "a purchase as protection from threatened misuse, impersonate the prospect, or register a mark-targeting name "
                    "to extract payment. The contractor prepares a short packet explaining the domain's generic meaning, the "
                    "prospect's observable use case, the contact source, and existing suppression status. The owner approves each "
                    "recipient and final message during the launch phase; later batches still require recipient-level evidence and "
                    "explicit authorization. For commercial email, 15 U.S.C. § 7704 requires accurate transmission information, appropriate "
                    "identification, a valid physical postal address, and a working opt-out mechanism, among other requirements. Honor "
                    "opt-outs within ten business days and preferably suppress immediately across every connected tool. U.S. rules "
                    "do not settle every recipient jurisdiction's requirements, so restrict initial targeting to assessed markets. "
                    "Separate transactional buyer correspondence from prospecting campaigns. Use a low-volume, relevance-led cadence, measure "
                    "qualified replies and complaints, and stop a segment when weak fit creates objections. Do not interpret "
                    "email opens as reliable purchase intent."
                ),
                (
                    "Create a referral loop around completed service, not speculative appreciation claims. After a successful transfer, "
                    "send a concise handover guide covering registrar access, renewal settings, DNS responsibility, and the buyer's "
                    "chosen next steps. Offer an optional shareable acquisition note that contains only facts the buyer has "
                    "approved for publication; many buyers reasonably prefer confidentiality. A useful naming checklist or domain-transfer "
                    "worksheet can earn referrals from designers, branding consultants, and small-business advisers without exposing buyer "
                    "data. If a partner receives compensation for an endorsement, assess the disclosure requirements in 16 CFR "
                    "Part 255 and make the relationship clear where the endorsement appears. Attribute introductions with simple "
                    "referral identifiers rather than invasive enrichment. The owner reviews public case studies and partner economics; "
                    "the contractor maintains approved collateral and checks links monthly. Close the loop by recording which "
                    "referrals produce qualified inquiries, completed transactions, and repeat introductions. Neither social sharing nor search "
                    "distribution has a dependable viral coefficient in an illiquid domain portfolio. Treat each channel as a "
                    "measured experiment with a fixed effort budget. Stop creating content that attracts other sellers but no "
                    "plausible buyers. Reinvest successful language into inventory descriptions, inquiry replies, and prospect research while "
                    "preserving the same underlying evidence and price discipline."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels Measured by Qualified Demand and Closed Transactions",
                "headers": [
                    "Channel and concrete buyer acquisition mechanism",
                    "Reusable input approved for public distribution",
                    "Conversion measure that avoids superficial activity counts",
                    "Stop condition protecting the two-person operating pod",
                ],
                "rows": [
                    [
                        "Owned landing pages convert visitors already investigating specific domains",
                        "Verified ownership facts and owner-approved transaction process descriptions",
                        "Qualified inquiries divided by relevant sessions during consistent periods",
                        "Pause publication when ownership or transaction instructions become stale",
                    ],
                    [
                        "Curated collection pages connect related names with specific buyers",
                        "Distinct portfolio groupings supported by actual available inventory",
                        "Buyer conversations attributed to collections rather than raw impressions",
                        "Retire collections generating seller chatter without credible buyer interest",
                    ],
                    [
                        "Marketplace distribution exposes owned assets to existing purchase intent",
                        "Reconciled prices and eligible listing status for each venue",
                        "Closed gross proceeds after identifying venue-specific selling costs",
                        "Disable conflicting listings whenever price or ownership diverges",
                    ],
                    [
                        "Outbound upgrades introduce generic alternatives to individually researched prospects",
                        "Rights-screened asset rationale and suppression-checked recipient contact evidence",
                        "Qualified replies and completed sales per reviewed prospect cohort",
                        "Stop segments producing complaints or repeated commercial-fit objections",
                    ],
                    [
                        "Professional referrals connect naming advisers with suitable inventory",
                        "Approved referral terms and clear compensation relationship disclosures",
                        "Completed transactions attributable to documented professional referral introductions",
                        "Pause partners making unsupported promises or misrepresenting ownership",
                    ],
                    [
                        "Buyer-approved handover stories demonstrate an orderly acquisition experience",
                        "Explicit publication permission and fact-checked transaction process details",
                        "Relevant introductions and qualified inquiries from published buyer stories",
                        "Remove publication when permission ends or material facts change",
                    ],
                ],
            },
        },
        {
            "heading": "4. Price Automated Runs, Reconcile Profit, and Rehearse Recovery",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price one run as a completed, validated event rather than a single model request. An illustrative "
                    "blended run costs $0.012 for model usage, $0.006 for permitted data access, and $0.004 for allocated "
                    "queue, storage, and monitoring services: $0.022 in machine cost. These are planning assumptions, not published "
                    "vendor quotes; replace them with invoices, actual token usage, export-license costs, and retry charges. At "
                    "6,000 completed runs monthly, machine cost is $132. Add eight contractor review hours at $35, or "
                    "$280, and the combined monthly workflow cost becomes $412, approximately $0.0687 per completed run. Owner "
                    "review time remains a separate capacity measurement unless the operating budget explicitly prices it. Count "
                    "failed attempts in the numerator and only completed events in the denominator, preventing cheap-looking "
                    "metrics that conceal retry waste. This workflow budget is a subset of operating expense, not an "
                    "extra profit deduction after the canonical margin. The volume's $500–$5,000 monthly operating range must "
                    "also accommodate hosting, subscriptions, administration, and other recurring overhead within the selected scenario. "
                    "The lower-revenue case cannot absorb the range's upper end while preserving its stated profit. Reduce "
                    "run volume or remove unnecessary enrichment when the carrying budget becomes tighter than the automation budget."
                ),
                (
                    "Reconcile the scorecard before telling a growth story. Conservative gross domain sale proceeds are $20,000; "
                    "a 15% net margin produces $3,000 annual owner net profit and leaves $17,000 for the modeled "
                    "cost envelope. Base proceeds are $160,000; a 27.5% margin produces $44,000 profit and a $116,000 "
                    "cost envelope. Scaled proceeds are $300,000; a 40% margin produces $120,000 profit and a $180,000 "
                    "cost envelope. These totals already include acquisition and renewal costs in the margin, alongside other "
                    "modeled costs; do not deduct the same costs again when presenting owner profit. Revenue here means "
                    "gross sales of the operator's domain assets, not marketplace-wide transaction volume, escrow balances, or "
                    "buyers' later business revenue. Keep working-capital cash requirements distinct from annual profit because "
                    "inventory purchases can precede sales by many months and unsold inventory remains illiquid. The startup "
                    "capital range is $10,000–$150,000, and time to first deal can be 3–24 months. Automation does not "
                    "compress that interval by assertion. Conservative and Base use 1 FT + 1 C; Scaled uses 2 FT "
                    "+ 2 C. The canonical Scaled economics therefore cannot be presented as a two-person outcome merely "
                    "because the software processes additional records."
                ),
                (
                    "Transfer fulfillment is where event discipline protects the asset itself. After agreeing terms, reconcile the "
                    "transaction against the escrow provider's authenticated dashboard or documented API, verify the domain spelling, "
                    "confirm the buyer's receiving details through the agreed channel, and follow the provider's funded-transaction "
                    "instructions. A screenshot or emailed payment claim is insufficient. Check registrar-specific transfer eligibility, "
                    "applicable locks, and whether an internal account push or inter-registrar transfer is intended. The owner "
                    "authorizes unlocking and release of the transfer code through the verified channel; keep those secrets "
                    "out of model prompts, general logs, and contractor research worksheets. Record delivery evidence and final "
                    "settlement separately because transfer initiation is not transaction completion. Rehearse recovery quarterly: replay a "
                    "duplicate webhook, restore the ledger from backup, simulate model downtime, and process a renewal from "
                    "the manual worksheet. A failed transfer should freeze conflicting listing activity and open a named "
                    "incident without repeatedly issuing sensitive credentials. Add staffing when response and reconciliation service levels "
                    "deteriorate, not when a dashboard reaches an arbitrary domain count. The durable flywheel is accurate "
                    "inventory, defensible acquisition choices, timely buyer service, documented handover, and reinvested realized proceeds. "
                    "Automation strengthens those links; it does not create liquidity or erase dispute exposure."
                ),
            ],
            "table": {
                "caption": "Canonical Economics and Illustrative Automation Cost Reconciliation",
                "headers": [
                    "Scenario or measurement with an explicit scope",
                    "Revenue or cost calculation stated without mixing bases",
                    "Staffing and capacity assumption behind the measurement",
                    "Operator interpretation and required accounting treatment",
                ],
                "rows": [
                    [
                        "Conservative annual case using gross domain sale proceeds",
                        "$20,000 proceeds minus $17,000 modeled costs equals $3,000 profit",
                        "One full-time owner plus one contractor supports this case",
                        "Preserve 15% margin by fitting all costs inside envelope",
                    ],
                    [
                        "Base annual case using gross domain sale proceeds",
                        "$160,000 proceeds minus $116,000 modeled costs equals $44,000 profit",
                        "One full-time owner plus one contractor remains the assumption",
                        "Preserve 27.5% margin without deducting acquisition costs twice",
                    ],
                    [
                        "Scaled annual case using gross domain sale proceeds",
                        "$300,000 proceeds minus $180,000 modeled costs equals $120,000 profit",
                        "Two full-time workers plus two contractors support this case",
                        "Preserve 40% margin and disclose the four-person team",
                    ],
                    [
                        "Illustrative machine expense per completed and validated event",
                        "$0.012 model plus $0.006 data plus $0.004 infrastructure",
                        "Contractor monitors failures within separately budgeted review hours",
                        "Replace assumed rates with actual invoices and completed-event counts",
                    ],
                    [
                        "Illustrative monthly machine and contractor review operating subtotal",
                        "6,000 runs cost $132; eight review hours cost $280",
                        "Eight contractor hours priced at $35 per working hour",
                        "$412 subtotal belongs inside operating expense and cost envelopes",
                    ],
                    [
                        "Illustrative weekly repetitive-work savings after added review effort",
                        "1,000 baseline minutes less 280 remaining equals 720 saved",
                        "Owner and contractor retain judgment work outside this baseline",
                        "Report 72% net removal only when observed timings support it",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Establish the ledger and manual baseline",
                    "action": "Reconcile every owned domain against authenticated registrar records and measure two weeks of repetitive work.",
                    "detail": "Assign all events to one of the eight plays; record expiration evidence, cost basis, review owner, and manual handling minutes.",
                },
                {
                    "step": 2,
                    "title": "Run read-only automation beside the existing process",
                    "action": "Enable renewal alerts, comparable clustering, and inquiry classification without granting asset-changing credentials.",
                    "detail": "Compare outputs with human decisions, label errors, test duplicate delivery, and reject unsupported model evidence references.",
                },
                {
                    "step": 3,
                    "title": "Authorize narrowly bounded production actions",
                    "action": "Enable approved acknowledgments, factual listing refreshes, and policy-limited renewals after successful reconciliation tests.",
                    "detail": "Keep bids, material pricing changes, outbound messages, abandonment decisions, and transfer-code release under explicit owner review.",
                },
                {
                    "step": 4,
                    "title": "Audit economics and rehearse fallback execution",
                    "action": "Review completed-run costs weekly and restore the ledger from a tested backup during quarterly recovery exercises.",
                    "detail": "Recalculate net minutes saved, reconcile scenario cost envelopes, investigate stale records, and adjust contractor hours before service levels deteriorate.",
                },
            ],
        },
    ],
    "pull_quote": "Automate the evidence trail, not the judgment that puts capital or ownership at risk.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create one asset ledger with authenticated ownership evidence, UTC expiration dates, renewal quotes, and approved venue listings.",
        "Map events to the eight operator plays and establish a measured repetitive-work baseline before claiming 70%+ automation.",
        "Deploy renewal reconciliation, comparable-sale evidence packets, and inquiry routing with durable event identifiers and bounded retries.",
        "Keep purchase authority, material pricing decisions, outreach approval, asset abandonment, and transfer credentials under owner control.",
        "Launch accurate collection pages, individually reviewed outbound upgrades, and permission-based referral stories with qualified-inquiry attribution.",
        "Reconcile automation expense inside the canonical cost envelopes and rehearse duplicate delivery, provider downtime, ledger restoration, and manual fulfillment.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 1125(d) — Cyberpiracy prevention",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": (
                "Screen acquisitions and outbound positioning for the statute's bad-faith intent and domain-name criteria; "
                "preserve evidence of legitimate rationale instead of treating exact-match availability as sufficient clearance."
            ),
        },
        {
            "title": "15 U.S.C. § 1117(d) — Statutory damages for specified domain-name violations",
            "url": "https://www.law.cornell.edu/uscode/text/15/1117",
            "relevance": (
                "For violations of section 1125(d)(1), the claimant may elect statutory damages of $1,000 to $100,000 per domain "
                "as the court considers just; acquisition screening should account for exposure beyond the purchase price."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmitting commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Build accurate sender information, required message identification, a valid physical postal address, and "
                "working opt-out processing into outbound upgrades; honor opt-outs within ten business days."
            ),
        },
        {
            "title": "16 CFR § 255.5 — Disclosure of material connections in endorsements",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": (
                "Assess referral payments and other material connections when partners endorse the operator or inventory, "
                "and make required disclosures clear and conspicuous."
            ),
        },
    ],
}
