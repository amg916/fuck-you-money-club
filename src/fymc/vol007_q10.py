from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 2 C (3 people) unclaimed property recovery team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Record Matching, Treasury Claim-State Webhooks, California Finder Restrictions, and Evidence-Led Acquisition Loops",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #07 with an 85/100 "
        "Money-to-Manpower Score. This chapter maps 12 operator plays into an evidence-led "
        "system for treasury records, corporate uncashed warrants, claim fulfillment, and "
        "distribution. A 1 FT + 2 C team targets more than 70% repetitive-work reduction "
        "through Python normalization, bounded LLM extraction, permissioned status collection, "
        "and exception queues; humans retain identity, authority, agreement, and submission "
        "decisions. Canonical annual owner profits remain $15,000 Conservative, $95,625 Base, "
        "and $225,000 Scaled, with recognized service fees separated from owner assets. "
        "The Scaled case requires 2 FT + 3 C. Unit-cost budgets, replay-safe events, "
        "state-specific finder restrictions, and a quarantined debt-adjacency test make "
        "automation measurable without turning uncertain matches into consequential actions."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees, excluding recovered owner assets",
            "note": "25% net margin; $15,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees, excluding recovered owner assets",
            "note": "37.5% net margin; $95,625 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees, excluding recovered owner assets",
            "note": "50% net margin; $225,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence ledger before connecting automation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with an event ledger, not a browser robot that clicks through treasury "
                    "forms. Give every imported property a source jurisdiction, official property "
                    "identifier, retrieval timestamp, source checksum, and permitted-use record. "
                    "Python's csv, sqlite3, hashlib, and datetime modules are sufficient for a "
                    "single-worker pilot: preserve the original row, create a normalized working "
                    "record, and append subsequent decisions rather than overwriting history. "
                    "Normalize punctuation and address components while retaining original spellings, "
                    "because a dissolved corporation and its similarly named successor can have "
                    "different ownership rights. Keep claimant documents in encrypted object storage "
                    "with narrowly scoped access; the ledger holds document references, not copied "
                    "identity numbers. Separate property, claimant, engagement, claim, and invoice "
                    "entities so one owner with six properties does not become six contradictory "
                    "customer profiles. A property listing establishes a research lead, not entitlement "
                    "or permission to contact someone through every available channel. Route licensed "
                    "bulk files and expressly permitted public downloads through ingestion adapters. "
                    "Where a treasury offers only interactive access, assign a scheduled human lookup "
                    "rather than bypassing access controls. Record the source restriction beside the "
                    "adapter so future contractors cannot mistake technical access for permitted reuse."
                ),
                (
                    "Use explicit transitions: discovered, research-ready, identity-reviewed, "
                    "agreement-reviewed, document-ready, submitted, evidence-requested, paid, and "
                    "closed. An internal webhook announces a proposed transition; it never proves "
                    "that a treasury accepted a claim. Implement receivers with Python's http.server "
                    "only for a local prototype, placing production handlers behind a managed HTTPS "
                    "endpoint with authentication, request-size limits, and durable queuing. Verify "
                    "HMAC signatures using hmac.compare_digest, reject stale timestamps, and enforce "
                    "an idempotency key combining engagement identifier, event type, and upstream event "
                    "identifier. Store the event before acknowledging receipt. A worker then validates "
                    "the current state, applies an allowed transition, and emits an audit entry. "
                    "Duplicate payment notifications must not generate duplicate invoices or owner "
                    "messages. Assume events can arrive late and out of order; a document-request "
                    "event received after payment becomes an exception rather than reopening the "
                    "claim automatically. The full-time operator owns exceptions and final decisions. "
                    "Contractor one handles evidence research; contractor two assembles packets and "
                    "checks status. Neither contractor can silently change fee rules or release "
                    "claimant documents externally. Maintain a daily reconciliation between ledger "
                    "states, official acknowledgments, and the operator's unresolved-work queue."
                ),
                (
                    "Define the 70% target against measured repetitive labor, not the proportion of "
                    "screens containing an AI button. In an illustrative weekly batch, baseline "
                    "research, qualification preparation, fulfillment preparation, and acquisition "
                    "administration consume 30, 18, 24, and 18 hours respectively: 90 hours total. "
                    "After automation, those same tasks consume 6, 5, 8, and 5 hours, or 24 "
                    "hours. The reduction is 66 divided by 90, or 73.3%. Separately reserve "
                    "12 hours for identity decisions, authority review, conversations, and exception "
                    "resolution; these consequential activities are outside both repetitive-work "
                    "measurements. Resulting weekly effort is 36 hours for this batch, distributed "
                    "across the three-person team without implying three full-time salaries. Validate "
                    "the result with four weeks of tagged time entries before advertising capacity. "
                    "Count retries, correction work, and rejected drafts in the automated workload. "
                    "Track accepted packets per paid labor hour alongside automation percentage, "
                    "because faster production of unusable packets destroys leverage. Start within "
                    "the $5,000–$35,000 startup-capital range, reserve cash for the 3–12 month "
                    "first-deal interval, and expand only after measured throughput survives an "
                    "exception-heavy week. A low exception count is credible only when reviewers "
                    "sample supposedly clean records as well as flagged ones."
                ),
            ],
            "table": {
                "caption": "Permissioned Python Pipeline and Evidence-Ledger Control Matrix",
                "headers": [
                    "Pipeline component and specific operating purpose",
                    "Concrete implementation and retained evidence fields",
                    "Human decision preserved outside unattended execution",
                    "Failure recovery without losing source provenance",
                ],
                "rows": [
                    [
                        "Treasury file ingestion preserves the official property listing",
                        "Use csv parsing with jurisdiction identifiers and source checksums",
                        "Research contractor confirms publication terms and permitted reuse",
                        "Quarantine malformed files while preserving their original downloaded bytes",
                    ],
                    [
                        "Entity normalization creates comparable names without erasing distinctions",
                        "Store original text beside normalized tokens and address components",
                        "Operator resolves successor entities and conflicting ownership histories",
                        "Reprocess affected rows using the previous normalization version",
                    ],
                    [
                        "Webhook receiver records authenticated requests before acknowledging delivery",
                        "Verify signatures and timestamps before committing durable event records",
                        "Operator authorizes changes to externally consequential transition rules",
                        "Reject forged requests and replay valid unprocessed ledger events",
                    ],
                    [
                        "State worker separates proposed transitions from verified claim outcomes",
                        "Enforce allowed transitions using transactional updates and unique keys",
                        "Packet contractor compares submission evidence with official acknowledgment",
                        "Route conflicting events into an assigned exception work queue",
                    ],
                    [
                        "Document storage limits exposure of claimant identity evidence",
                        "Use encrypted storage references with expiring narrowly scoped links",
                        "Operator authorizes each external recipient and document purpose",
                        "Revoke exposed links and investigate recorded document access events",
                    ],
                    [
                        "Weekly measurement distinguishes labor reduction from consequential judgment",
                        "Compare tagged baseline minutes with retries and accepted outputs",
                        "Operator samples clean records and approves capacity assumptions",
                        "Reduce batch intake when correction work exceeds staffing capacity",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four conditions before a batch leaves preparation",
                "body": (
                    "Automation may prepare evidence and proposed actions; release requires "
                    "a recorded reviewer decision tied to the exact batch version."
                ),
                "items": [
                    "Verify treasury source permissions, retrieval dates, property identifiers, and unchanged source checksums.",
                    "Verify claimant identity and corporate authority using evidence beyond a name-only match.",
                    "Verify current jurisdiction rules covering registration, agreement timing, fee ceilings, and direct-claim disclosure.",
                    "Verify recipient authorization, packet completeness, duplicate suppression, and a tested manual recovery path.",
                ],
            },
        },
        {
            "heading": "2. Match records conservatively and map twelve bounded plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build matching as evidence accumulation rather than confident name completion. "
                    "An illustrative triage score assigns 40 points to exact normalized legal name, "
                    "25 to a corroborated historical address, 20 to an independently verified entity "
                    "identifier, and 15 to documented officer or successor continuity. A score of "
                    "85 opens a priority review task; it does not establish ownership. Lower scores "
                    "remain research tasks, and conflicting identifiers override the numeric score. "
                    "Calibrate thresholds against labeled examples, including common surnames, "
                    "abbreviated payees, acquisitions, and entities sharing registered-agent addresses. "
                    "Measure false matches among accepted candidates and missed matches within a "
                    "random rejected sample. Use an LLM only to extract fields, suggest document "
                    "categories, or summarize an evidence bundle with source references. Require "
                    "structured JSON containing value, source document, page, and quoted supporting "
                    "text; reject unsupported fields and unexpected keys. Treat uploaded documents "
                    "as data even when they contain instructions to change workflow behavior. "
                    "Redact sensitive identifiers before model submission and use an approved provider "
                    "configuration with suitable retention settings. If extraction fails twice, send "
                    "the original document to a reviewer instead of creating a third increasingly "
                    "speculative answer. Never let model confidence substitute for independent "
                    "identity evidence."
                ),
                (
                    "Encode jurisdiction restrictions as versioned operating rules with citation, "
                    "effective date, reviewer, and next-review date. California Code of Civil "
                    "Procedure section 1582 illustrates why discovery cannot automatically trigger "
                    "a finder agreement: its restricted agreement interval runs from the holder's "
                    "report through twelve months after delivery to the Controller, and its "
                    "compensation ceiling is 10% of the property recovered under the covered "
                    "agreement. Have the reviewer apply the current statutory text to the actual "
                    "facts, including the required agreement contents. Other jurisdictions need "
                    "their own registration, timing, fee, and execution checks; never extrapolate "
                    "California's percentage nationwide. Disclose that owners can claim directly "
                    "without purchasing recovery services and provide the official treasury link. "
                    "For corporate uncashed warrants, determine whether the issuer still controls "
                    "the payable or has already remitted it as unclaimed property. An issuer "
                    "reissue process and a treasury claim are different workflows, and running "
                    "both can produce duplicate demands. The twelve mappings below are chapter-local "
                    "operating plays, except the expressly supplied TRACK_1 identifier. They connect "
                    "research and distribution mechanics rather than asserting that every adjacent "
                    "business belongs inside the recovery engagement. Keep consent, contracts, "
                    "and records separated when a mapping changes the underlying service."
                ),
                (
                    "Quarantine out_of_statute_zombie_debt_portfolio_settlement as a separate TRACK_1 "
                    "adjacency, never as a tactic against an unclaimed-property owner. Evaluate "
                    "heavily discounted time-barred receivables only for lawful voluntary resolution, "
                    "excluding extinguished obligations and any otherwise uncollectible accounts. "
                    "Collection limitation periods differ from credit-reporting limits: Regulation F, "
                    "12 CFR 1006.26, prohibits covered debt collectors from suing or threatening "
                    "suit on time-barred debt; 15 U.S.C. 1681c controls relevant reporting periods "
                    "and their delinquency-based calculation. State law can extinguish obligations "
                    "or impose additional requirements, so account-level jurisdiction review precedes "
                    "any contact. Illustratively, 100 eligible accounts with $100,000 face value "
                    "might cost $2,000, with $800 validation expense and $600 outreach expense. "
                    "Five voluntary payments of $500 produce $2,500 cash, leaving a $900 deficit "
                    "against $3,400 cash outlay before overhead. Face value is neither collected "
                    "cash nor recovery-service revenue; purchased-receivable accounting also needs "
                    "separate treatment. Do not promise tradeline deletion, re-age delinquency, "
                    "or imply payment is required to obtain treasury property. Suppress affected "
                    "accounts, correct reporting, and suspend collection until counsel approves "
                    "remediation whenever eligibility or reporting fails. Keep this experiment "
                    "outside all three canonical recovery scenarios and reject it when its "
                    "unit economics or evidence cannot support operation."
                ),
            ],
            "table": {
                "caption": "Twelve Mapped Plays with Explicit Unit Economics and Risk Fallbacks",
                "headers": [
                    "Mapped play and bounded operating application",
                    "Illustrative unit math for evaluating the mechanism",
                    "Evidence required before consequential human release",
                    "Risk fallback when the operating assumption fails",
                ],
                "rows": [
                    [
                        "treasury_bulk_record_matching: prioritize permissioned state property research batches",
                        "Screen 1,000 records for $4 before separate human review",
                        "Retain official identifiers and corroborating claimant ownership evidence",
                        "Quarantine ambiguous names rather than contacting every possible owner",
                    ],
                    [
                        "corporate_warrant_reconciliation: reconcile issuer payables against treasury listings",
                        "Review 100 warrant entries in two contractor hours",
                        "Confirm issuer custody before choosing reissue or treasury recovery",
                        "Pause duplicate demands until issuer and treasury custody reconcile",
                    ],
                    [
                        "successor_entity_evidence_graph: map acquisitions and historical corporate identities",
                        "Review ten entity histories at twenty minutes each",
                        "Require documented ownership succession rather than shared officer names",
                        "Escalate broken ownership chains to qualified document review",
                    ],
                    [
                        "finder_rule_calendar: schedule state-specific agreement eligibility and review",
                        "Check fifty engagements in one weekly calendar batch",
                        "Verify current registration requirements and actual statutory timing facts",
                        "Hold agreements when eligibility dates lack reliable source evidence",
                    ],
                    [
                        "claim_packet_prefill: assemble supported fields into reviewer-ready packets",
                        "Prepare twenty packets at three automated minutes each",
                        "Compare every consequential field with its cited source evidence",
                        "Return unsupported fields to manual preparation without fabricated values",
                    ],
                    [
                        "claim_status_event_tracking: translate permissioned observations into internal events",
                        "Poll forty permitted endpoints for two illustrative dollars",
                        "Require official acknowledgment before marking any claim submitted",
                        "Schedule manual checks when access permissions or adapters fail",
                    ],
                    [
                        "owner_document_reminder_sequence: request missing evidence through private links",
                        "Send sixty permitted reminders at two illustrative cents each",
                        "Confirm recipient identity and the specific missing document purpose",
                        "Stop reminders after disputes and offer a human callback",
                    ],
                    [
                        "accountant_referral_loop: distribute useful checklists through professional relationships",
                        "Ten introductions at $75 yield $750 acquisition spend",
                        "Obtain owner authorization before sharing any property-specific information",
                        "Stop paid incentives where applicable rules restrict referral compensation",
                    ],
                    [
                        "jurisdiction_education_pages: publish reviewed state-specific recovery process guidance",
                        "Six pages costing $150 each require $900 investment",
                        "Verify current primary authorities and official direct-claim destinations",
                        "Withdraw stale instructions while preserving useful general education",
                    ],
                    [
                        "corporate_outbound_research: contact verified business representatives with evidence",
                        "One hundred $3 research touches produce $300 cost",
                        "Check representative relevance and suppress previously declined outreach",
                        "Pause the cohort when replies reveal systematic identity errors",
                    ],
                    [
                        "owner_initiated_referral_sharing: let satisfied clients share generic resources",
                        "Twenty invitations producing two clients cost $20 each",
                        "Separate permission to request feedback from permission to publish",
                        "Remove sensitive details and stop requests after client objection",
                    ],
                    [
                        "out_of_statute_zombie_debt_portfolio_settlement: separate TRACK_1 voluntary-resolution experiment only",
                        "Five $500 receipts against $3,400 outlay lose $900",
                        "Separate limitation periods from reporting limits and exclude ineligible obligations",
                        "Suppress affected accounts, correct reporting, and suspend collection until counsel approves remediation",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Use treasury-specific evidence to reduce expensive false positives",
                "body": (
                    "Experienced operators improve the evidence path before increasing "
                    "the number of names entering outreach."
                ),
                "items": [
                    "Keep the holder-reported address as historical evidence; a current mailing address alone cannot resolve ownership.",
                    "Check issuer custody before preparing a corporate warrant claim, preventing simultaneous reissue and treasury demands.",
                    "Cluster properties by verified owner only after identity review, then reuse authorized evidence without assuming identical state requirements.",
                    "Preserve every official request and acknowledgment with its date; a portal label can change while the underlying evidence remains decisive.",
                ],
            },
        },
        {
            "heading": "3. Price automated runs and recover safely from failures",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price the pipeline at the accepted-output level. An illustrative run ingests "
                    "1,000 permitted records for $1 of compute and storage, normalizes them for "
                    "$3, sends 100 redacted extraction requests at $0.02 each for $2, performs "
                    "40 permitted status checks for $2, and sends 60 authorized messages at "
                    "$0.02 each for $1.20. Direct machine expense is $9.20. Add a 20% retry "
                    "reserve of $1.84, making the budget $11.04 per run. These are planning "
                    "assumptions, not vendor quotations; replace each rate with observed invoices. "
                    "If 20 candidates require four minutes of contractor review at $30 hourly, "
                    "review costs $40. Three packet checks at twelve minutes and $40 hourly "
                    "add $24. Total run cost is therefore $75.04, or approximately $25.01 "
                    "per accepted packet when all three pass. If only one packet passes, "
                    "the cost is $75.04, demonstrating why cheap extraction cannot rescue "
                    "weak targeting. Report machine expense, reviewer expense, accepted packets, "
                    "and eventual fee receipts separately. Do not count an assembled packet "
                    "as a paid recovery. Allocate unsuccessful research across the cohort "
                    "rather than hiding it in a miscellaneous software account. Maintain "
                    "the same denominator when comparing manual and automated processing."
                ),
                (
                    "Reconcile throughput to the canonical scorecard using an illustrative average "
                    "recognized service fee of $750 per completed engagement. Conservative requires "
                    "80 completions for $60,000 revenue; Base requires 340 for $255,000; Scaled "
                    "requires 600 for $450,000. At an illustrative lawful 10% contracted fee, "
                    "each engagement represents $7,500 of recovered owner property, not $7,500 "
                    "of operator revenue. Owner assets would total $600,000, $2,550,000, and "
                    "$4,500,000 respectively, entirely outside recognized service-fee revenue. "
                    "The canonical margins imply total annual expenses of $45,000, $159,375, "
                    "and $225,000, leaving owner profits of $15,000, $95,625, and $225,000. "
                    "Allocate labor, acquisition, research failures, software, insurance, and "
                    "administration inside those totals; the run model is one component, "
                    "not an additional profit projection. Average monthly total expenses "
                    "are $3,750, $13,281.25, and $18,750. Consequently, the supplied "
                    "$1,500–$8,000 monthly opex planning range cannot serve as an all-in "
                    "expense ceiling for every scenario. Use the scenario-derived expense "
                    "totals when budgeting these outcomes and resolve category definitions "
                    "before committing cash. Preserve staffing at 1 FT + 2 C for "
                    "Conservative and Base, and 2 FT + 3 C for Scaled. "
                    "A software improvement does not authorize silently removing the second "
                    "full-time role from the Scaled case."
                ),
                (
                    "Treat claim tracking as reconciliation against external evidence. Treasury "
                    "systems do not universally expose APIs or webhooks, so adapters may consume "
                    "authorized exports, owner-forwarded correspondence, or scheduled manual "
                    "observations. Each observation records claim identifier, source timestamp, "
                    "observed status, document request, and next permitted action. Never infer "
                    "payment from a disappearing portal row. Use bounded exponential backoff "
                    "with jitter for transient failures, respect published rate limits, and "
                    "move repeated failures into a dead-letter queue with an assigned owner. "
                    "After three failed attempts, stop unattended retries until the next "
                    "reviewed schedule; distinguish a temporary outage from revoked access. "
                    "Detect schema drift through required-field checks and a small set of "
                    "known test records. A changed date format should quarantine the batch, "
                    "not rewrite agreement eligibility dates. Keep daily encrypted backups "
                    "and run a monthly restore exercise that reconciles event counts and "
                    "document references. During an outage, contractors use a minimal manual "
                    "worksheet containing identifiers, next actions, and reviewer initials. "
                    "Import that worksheet with unique event keys after service returns. "
                    "Customer updates should state the last verified milestone and the "
                    "next action, avoiding invented treasury deadlines. Release invoices "
                    "only after the engagement's contractual earning conditions and supporting "
                    "recovery evidence are satisfied."
                ),
            ],
            "table": {
                "caption": "Run-Cost Controls and Claim-State Failure-Recovery Matrix",
                "headers": [
                    "Observed condition requiring an operational response",
                    "Detection evidence and explicit accounting treatment",
                    "Bounded automated response before human intervention",
                    "Human fallback preserving claimant and revenue accuracy",
                ],
                "rows": [
                    [
                        "Extraction response omits evidence for a consequential field",
                        "Schema validation records the missing citation and request cost",
                        "Retry once using the same redacted source bundle",
                        "Reviewer reads original evidence and rejects unsupported field values",
                    ],
                    [
                        "Treasury status adapter encounters a changed response structure",
                        "Required-field checks fail before any claim state changes",
                        "Quarantine the response and disable affected transition processing",
                        "Contractor verifies status manually and documents the changed interface",
                    ],
                    [
                        "Repeated delivery reports attempt to create duplicate messages",
                        "Unique event keys identify repeated notifications before dispatch",
                        "Acknowledge prior processing without repeating customer communication actions",
                        "Operator investigates contradictory payloads using retained event evidence",
                    ],
                    [
                        "One accepted packet replaces three expected accepted packets",
                        "Run cost remains $75.04 despite reduced usable output",
                        "Flag the cohort for targeting and evidence-quality review",
                        "Operator reduces intake until accepted-packet economics recover adequately",
                    ],
                    [
                        "Portal record disappears without a supporting payment acknowledgment",
                        "Store disappearance as an observation rather than earned revenue",
                        "Create a verification task without sending payment claims",
                        "Reviewer obtains official evidence before invoicing the service fee",
                    ],
                    [
                        "Outage forces temporary manual tracking of active engagements",
                        "Record minimal identifiers with timestamps and responsible reviewer initials",
                        "Suspend unattended changes while preserving queued authenticated events",
                        "Reconcile manual actions before replaying events into restored systems",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze and identify the affected batch",
                    "action": "Stop the failing adapter and assign an incident owner.",
                    "detail": (
                        "Preserve source files, event identifiers, software version, and "
                        "the last verified external milestone for every affected claim."
                    ),
                },
                {
                    "step": 2,
                    "title": "Continue essential work through the manual queue",
                    "action": "Route time-sensitive document requests to the packet contractor.",
                    "detail": (
                        "Use only verified recipient details and record each manual action "
                        "with a unique identifier to prevent duplicate replay."
                    ),
                },
                {
                    "step": 3,
                    "title": "Repair and replay a bounded test sample",
                    "action": "Validate the corrected adapter against retained source examples.",
                    "detail": (
                        "Compare expected transitions with actual results, including duplicate, "
                        "late, conflicting, and malformed events before restoring batch processing."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile before resuming normal throughput",
                    "action": "Match ledger events, official acknowledgments, and customer messages.",
                    "detail": (
                        "Record corrected costs and reviewer minutes, resolve discrepancies, "
                        "and expand the resumed batch only after the sample reconciles."
                    ),
                },
            ],
        },
        {
            "heading": "4. Compound trusted distribution without outrunning review capacity",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build programmatic education around questions owners actually need answered: "
                    "how to locate an official treasury portal, document a corporate name change, "
                    "or distinguish an issuer-held warrant from escheated property. Generate page "
                    "drafts from a jurisdiction rules table, then require an editor to verify "
                    "citations, dates, direct-claim links, and state-specific instructions. Do not "
                    "publish pages naming apparent owners or suggesting that an unverified amount "
                    "belongs to them. A six-page pilot at $150 production cost per page "
                    "costs $900. If it produces 30 qualified inquiries and three paid "
                    "engagements, acquisition cost is $300 per engagement before ongoing maintenance. "
                    "At the illustrative $750 fee, that leaves $450 before fulfillment and "
                    "other expenses, not $450 profit. Attribute results through first-party "
                    "landing-page parameters and engagement identifiers without embedding sensitive "
                    "property details in URLs. Improve pages using aggregated missing-document "
                    "patterns from completed cases, stripping identifiers before editorial use. "
                    "This creates a useful loop: real operational friction improves education, "
                    "better education attracts prepared owners, and prepared owners reduce "
                    "packet revisions. Retire pages whose rules cannot be maintained. Traffic "
                    "growth matters only when resulting engagements fit the evidence standards, "
                    "review capacity, and fee economics of the operation."
                ),
                (
                    "Use professional referrals and narrow corporate outreach before broad automated "
                    "messaging. Accountants, business attorneys, and corporate administrators often "
                    "understand historical names and authorized signatories better than a scraped "
                    "contact list. Give partners a generic evidence checklist and official "
                    "direct-claim links; share a specific property's details only with appropriate "
                    "authorization. An illustrative campaign researching 100 corporate contacts "
                    "at $3 each costs $300. Eight substantive replies, four qualified "
                    "engagements, and two eventual paid recoveries yield $150 acquisition cost "
                    "per paid engagement, before fulfillment. Treat those conversions as a "
                    "test hypothesis rather than a forecast. For commercial email, implement "
                    "15 U.S.C. 7704 requirements including accurate headers, nondeceptive subjects, "
                    "required identification and address information, and a functioning opt-out "
                    "that is honored within the statutory period. Do not disguise a private "
                    "service as a treasury notice. Suppress declined recipients across every "
                    "campaign, and retain only the minimal suppression data necessary to "
                    "honor that choice. A satisfied owner may voluntarily share a generic "
                    "resource link, but their recovery amount, documents, and testimonial "
                    "require separate publication permission. Avoid public leaderboards, "
                    "exposed claim identifiers, and referral incentives that conflict with "
                    "applicable professional or finder rules."
                ),
                (
                    "Connect distribution to capacity through a weekly cohort dashboard. Track "
                    "source records, reviewed matches, qualified owners, signed eligible agreements, "
                    "accepted submissions, paid engagements, recognized fees, and attributable "
                    "expense. Separate these stages by acquisition month because a 3–12 month "
                    "first-deal interval makes same-month conversion ratios misleading. At Base, "
                    "340 paid engagements annually average 28.33 monthly, while Scaled averages "
                    "50; these are throughput requirements, not treasury processing promises. "
                    "If an illustrative 40% of qualified engagements eventually pay, Base "
                    "requires 850 qualified engagements annually, approximately 70.83 monthly. "
                    "If only 20% pay, that requirement doubles to 1,700 annually. Use "
                    "observed aging and conversion before buying more traffic. Set work-in-progress "
                    "limits from reviewer minutes: 120 available packet-review minutes daily "
                    "at twelve minutes per packet support ten reviews, not unlimited submissions. "
                    "When identity exceptions or missing-document requests consume that reserve, "
                    "slow acquisition instead of allowing unsafe automatic release. Reinvest "
                    "only within the canonical expense envelope and keep cash runway "
                    "separate from recognized profit. The distribution flywheel becomes "
                    "scalable when each completed cohort improves source selection, document "
                    "readiness, and trust while preserving the owner's direct-claim choice. "
                    "Automate preparation aggressively; expand consequential throughput only "
                    "as fast as evidence quality and staffed review permit."
                ),
            ],
            "table": {
                "caption": "Distribution Cohorts, Capacity Limits, and Measurable Stop Conditions",
                "headers": [
                    "Distribution mechanism and intended qualified audience",
                    "Illustrative cohort economics with explicit conversion denominator",
                    "Evidence or capacity condition required for continuation",
                    "Stop condition and practical lower-risk fallback",
                ],
                "rows": [
                    [
                        "Reviewed jurisdiction pages answer specific owner process questions",
                        "Spend $900 for three paid engagements at $300 acquisition",
                        "Maintain verified citations and useful official direct-claim links",
                        "Withdraw outdated instructions until an editor verifies replacement text",
                    ],
                    [
                        "Corporate outreach targets representatives with relevant authority evidence",
                        "Spend $300 for two paid engagements at $150 acquisition",
                        "Confirm contact relevance and maintain centralized suppression records",
                        "Pause the cohort when replies expose repeated entity mismatches",
                    ],
                    [
                        "Professional referral resources improve document readiness before engagement",
                        "Spend $750 on ten introductions before measuring paid conversion",
                        "Share generic checklists before obtaining property-specific owner authorization",
                        "Remove incentives that conflict with applicable professional referral rules",
                    ],
                    [
                        "Owner-initiated sharing distributes generic educational resources voluntarily",
                        "Spend $40 for two resulting clients at $20 each",
                        "Obtain separate permission before publishing identifiable client stories",
                        "Stop requests after objection and remove unauthorized identifying content",
                    ],
                    [
                        "Base acquisition planning uses eventually paid engagement cohorts",
                        "At 40% conversion, 850 qualified engagements yield 340 payments",
                        "Verify aging and conversion using completed historical acquisition cohorts",
                        "Reduce spend when actual conversion requires unaffordable qualification volume",
                    ],
                    [
                        "Reviewer capacity constrains daily packet release despite machine throughput",
                        "Twelve minutes per packet permits ten daily two-hour reviews",
                        "Reserve additional review time for identity and authority exceptions",
                        "Throttle incoming work before backlog overwhelms consequential decision capacity",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Automate the evidence trail, not the leap from a matching name to a rightful owner."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create separate property, claimant, engagement, claim, invoice, and immutable event records with source provenance.",
        "Benchmark repetitive labor across four weeks and test the 73.3% illustrative reduction against actual correction time.",
        "Implement jurisdiction-specific agreement rules, direct-claim disclosures, identity review, and document-release permissions.",
        "Deploy signed internal webhooks with idempotency keys, bounded retries, dead-letter ownership, and a tested manual fallback.",
        "Reconcile $750 illustrative fee throughput to the exact three revenue, expense, profit, and staffing scenarios.",
        "Launch one reviewed education cohort and one narrow corporate outreach cohort, expanding only after paid conversion and reviewer capacity reconcile.",
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure § 1582",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582.",
            "relevance": (
                "Controls covered finder agreements, including the restricted agreement "
                "interval, compensation ceiling, and required agreement information."
            ),
        },
        {
            "title": "12 CFR § 1006.26 — Collection of time-barred debts",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1006/subpart-B/section-1006.26",
            "relevance": (
                "Prohibits covered debt collectors from bringing or threatening legal "
                "action against consumers to collect time-barred debts; applies to "
                "the separately quarantined TRACK_1 evaluation."
            ),
        },
        {
            "title": "15 U.S.C. § 1681c(a)(4) and (c)(1)",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681c",
            "relevance": (
                "Establishes relevant credit-reporting age restrictions and the "
                "delinquency-based calculation for covered collection and charge-off "
                "accounts, distinct from collection limitation periods."
            ),
        },
        {
            "title": "15 U.S.C. § 1692e — False or misleading representations",
            "url": "https://www.law.cornell.edu/uscode/text/15/1692e",
            "relevance": (
                "Restricts false or misleading representations by covered debt "
                "collectors, including representations concerning an obligation's "
                "character, amount, or legal status."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Commercial electronic mail requirements",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Sets commercial-email requirements covering transmission information, "
                "subject lines, opt-out mechanisms, sender identification, postal "
                "address information, and honoring opt-out requests."
            ),
        },
    ],
}
