from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) saas discount brokerage & gpo arbitrage team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Evidence Pipelines, Authorized CSP and VIP Reconciliation, Shared-Savings Ledgers, and TCPA-Aware Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #37, SaaS Discount Brokerage & GPO Arbitrage, ranks #04 of 37 "
        "with a 94/100 Money-to-Manpower Score. This chapter turns 12 mapped plays "
        "into an evidence-first operating system: discover public signals, obtain "
        "authorized invoices, calculate eligible economics, reconcile partner "
        "statements, and distribute verified outcomes. Python handles deterministic "
        "work; language models extract and draft; people authorize consequential "
        "changes. The canonical annual owner-profit cases are $32,000 Conservative, "
        "$225,000 Base, and $522,000 Scaled. Their revenue excludes client subscription "
        "spend and measures retained operator economics. A measured 76% straight-through "
        "task rate is achievable in the illustrative queue, but only with bounded "
        "permissions, exception ownership, and tested recovery. Agency advertising "
        "rewards remain a separate, contract-permitted adjacent play rather than "
        "a reason to manufacture spend."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retained operator revenue; client subscription spend excluded",
            "note": "32% net margin; $32,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$500,000",
            "context": "Annual retained operator revenue; client subscription spend excluded",
            "note": "45.0% net margin; $225,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained operator revenue; client subscription spend excluded",
            "note": "58% net margin; $522,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence graph before automating qualification",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a tenant-scoped evidence graph, not a spreadsheet of guessed renewals. "
                    "Represent each organization, domain, customer authorization, agreement, subscription, "
                    "invoice, and partner relationship as a separate record with a stable identifier. "
                    "A scheduled Python worker can query an approved DNS-over-HTTPS endpoint using "
                    "urllib.request, parse JSON, and record MX and TXT responses with observation time "
                    "and resolver identity. Microsoft-associated MX records and SPF includes suggest "
                    "mail infrastructure; they do not establish license quantity, purchasing channel, "
                    "contract value, or renewal date. Multiple SPF records are an operational anomaly, "
                    "not proof of a migration opportunity. Use those signals to prioritize a permission-based "
                    "spend assessment, then collect invoices and renewal schedules through a customer-controlled "
                    "upload link. Store original documents separately from extracted fields, hash each "
                    "artifact with hashlib, and preserve the source page supporting every commercial "
                    "claim. CRM records should distinguish observed facts, customer assertions, model "
                    "extractions, and reviewer confirmations. A renewal-cliff trigger becomes actionable "
                    "only when a verified agreement establishes its notice deadline. Calculate outreach "
                    "dates backward from that deadline, including review time and vendor processing "
                    "buffers. Missing contractual evidence routes the account to document collection "
                    "rather than an invented savings estimate."
                ),
                (
                    "Map the chapter's twelve plays into explicit workflow lanes: DNS qualification, "
                    "renewal-cliff detection, authorized CSP margin capture, CPOR association tracking, "
                    "Adobe VIP Marketplace reconciliation, Telarus residual reconciliation, Avant residual "
                    "reconciliation, GPO bracket monitoring, benchmark price-floor testing, contingent "
                    "shared-savings audits, referral distribution, and agency advertising rewards. These "
                    "are operating lanes, not twelve independent revenue streams; CPOR tracking and "
                    "benchmarking often support the same earned fee. Microsoft CPOR is a relationship "
                    "and attribution mechanism for eligible workloads, not a universal license-transfer "
                    "instruction or entitlement to a reseller spread. Maintain separate records for "
                    "CSP purchasing authority, eligible CPOR associations, and customer administrative "
                    "permissions. For the discovery lane, an illustrative 200 reviewed domains at "
                    "$0.02 each costs $4 before labor; if 20 customers submit authorized invoices, "
                    "the machine discovery cost is $0.20 per evidence-ready account. This ratio "
                    "does not include outreach labor or prove conversion. If DNS evidence conflicts "
                    "with an invoice, preserve both observations and let the invoice control the "
                    "commercial assessment after verification. Contractors receive only their assigned "
                    "customer records. The owner controls partner credentials, pricing exceptions, "
                    "and contract acceptance, keeping a four-person organization from becoming four "
                    "unrestricted administrators."
                ),
                (
                    "Use language models as bounded document processors with no purchasing privileges. "
                    "Send the minimum invoice excerpt needed to extract currency, SKU, service period, "
                    "quantity, unit price, term, and cancellation language. Remove bank details and "
                    "unnecessary personal identifiers before transmission, and use an approved service "
                    "whose retention terms fit the customer agreement. Require a JSON object containing "
                    "field values, source quotations, page references, and explicit missing-field flags. "
                    "Validate types and required keys in Python; perform money calculations with decimal.Decimal "
                    "rather than accepting model arithmetic. Reject unsupported SKUs, impossible date "
                    "ranges, conflicting currencies, or totals that fail invoice reconciliation. Treat "
                    "instructions embedded in uploaded contracts as document content, never as commands "
                    "to the automation. A reviewer must confirm ambiguous renewal language, customer "
                    "authority, and any proposed external savings claim. Build a regression set from "
                    "redacted, authorized examples covering credits, annual commitments billed monthly, "
                    "midterm seat additions, and overlapping subscriptions. Measure field accuracy "
                    "separately from extraction completion: a populated renewal date is harmful if "
                    "it describes an invoice cycle instead of the contractual commitment. When a "
                    "model service fails, retain the document in a manual extraction queue and "
                    "continue deterministic reconciliation for previously verified accounts."
                ),
            ],
            "table": {
                "caption": "Evidence Acquisition and Twelve-Play Workflow Routing Matrix",
                "headers": [
                    "Workflow lane and commercial purpose",
                    "Evidence required before operational use",
                    "Automated action within bounded authority",
                    "Human review and recovery procedure",
                ],
                "rows": [
                    [
                        "DNS qualification identifies plausible software infrastructure prospects",
                        "Timestamped MX and SPF observations from approved resolvers",
                        "Classify provider indicators without asserting purchased license quantities",
                        "Resolve contradictory signals before drafting specific customer claims",
                    ],
                    [
                        "Renewal-cliff detection prioritizes documented cancellation notice windows",
                        "Customer agreement establishes term and notice deadline",
                        "Schedule reminders backward from verified contractual notice dates",
                        "Review ambiguous wording before contacting the vendor",
                    ],
                    [
                        "Authorized CSP margin capture tracks approved reseller economics",
                        "Customer authority and current distributor terms support eligibility",
                        "Calculate eligible spread using effective dated price schedules",
                        "Reject unsupported transfers and preserve existing customer service",
                    ],
                    [
                        "CPOR association tracking preserves eligible workload attribution evidence",
                        "Applicable program requirements and customer relationship evidence exist",
                        "Track association status separately from subscription purchasing authority",
                        "Escalate disputed attribution without changing customer subscription ownership",
                    ],
                    [
                        "Adobe VIP Marketplace reconciliation detects authorized billing differences",
                        "Customer membership and approved transaction records identify subscriptions",
                        "Compare quantities and anniversary dates against distributor statements",
                        "Resolve discrepancies through authorized distributor support procedures",
                    ],
                    [
                        "Telarus and Avant residual lanes reconcile separate agreements",
                        "Supplier statements and executed agent agreements establish entitlement",
                        "Match customer accounts with earned residual periods",
                        "Dispute missing commissions without assuming perpetual payment rights",
                    ],
                    [
                        "GPO brackets and benchmarks support documented savings audits",
                        "Member authority and comparable eligible purchases establish inputs",
                        "Calculate brackets and comparable costs without duplicate savings",
                        "Verify contractual exclusions before quoting an achievable outcome",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the evidence that earns the spread",
                "body": (
                    "The useful asset is the verified customer-to-contract relationship, "
                    "not the largest prospect database."
                ),
                "items": [
                    "Store commitment end dates separately from invoice dates; monthly NCE invoices can support an annual obligation.",
                    "Snapshot the eligible partner tier when quoting, then recheck it before execution so rebate compression cannot silently erase contribution.",
                    "Attach source quotations to extracted notice clauses; reviewers can verify the decisive language without rereading every document.",
                    "Keep CPOR association status outside the reseller transfer state machine; attribution evidence does not authorize a subscription move.",
                ],
            },
        },
        {
            "heading": "2. Turn partner events into recoverable billing operations",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement a small event pipeline with an HTTPS receiver, durable queue, Python "
                    "worker, and append-only audit journal. Pax8, Ingram, Telarus, and Adobe-related "
                    "distributor integrations require agreement-specific access; do not assume every "
                    "portal exposes a webhook or the same subscription operations. Use documented "
                    "APIs where available, approved scheduled exports otherwise, and manual portal "
                    "verification when neither interface supports the required field. Verify webhook "
                    "signatures according to the provider's specification, reject stale messages when "
                    "timestamps are supported, and persist accepted events before acknowledging receipt. "
                    "Build idempotency keys from provider identity, event identifier, and operation "
                    "type. Store raw event hashes alongside normalized records, then reconcile the "
                    "latest authoritative state because webhook ordering is unreliable. Python's "
                    "sqlite3 supports a modest single-writer deployment; transactions and unique "
                    "constraints prevent duplicate event insertion. Separate ingestion from any "
                    "external write so a replay cannot create a second order. The job state "
                    "machine should distinguish received, validated, review-required, authorized, "
                    "submitted, confirmed, and exception states. Confirmation requires a provider "
                    "receipt or refreshed authoritative record, not merely an HTTP success response "
                    "from an intermediary. Keep a customer-visible change log describing what "
                    "actually changed and who authorized it."
                ),
                (
                    "Automate reconciliation aggressively while keeping commercial commitments behind human "
                    "review. Match each distributor invoice line to the customer agreement, tenant, "
                    "subscription identifier, SKU, quantity, service dates, and effective price. "
                    "Illustratively, 100 eligible subscriptions producing $100 monthly retained spread "
                    "yield $120,000 annual operator revenue, not the face value of customer "
                    "software purchases. A missing customer payment does not extinguish an annual "
                    "NCE distributor obligation. Require prefunded terms or an approved ACH or "
                    "card collection arrangement with advance collection and documented credit limits; "
                    "a debit authorization alone is not cash. Verify settlement, consider return "
                    "exposure, and stop new commitments when available coverage falls below the "
                    "approved threshold. Do not cancel or suspend existing customer service automatically "
                    "because a collection event failed. Route that decision through the contract "
                    "owner and applicable provider procedures. For Adobe VIP Marketplace, preserve "
                    "membership, anniversary, transaction, and distributor identifiers rather than "
                    "repurposing Microsoft fields. For Telarus or Avant, reconcile supplier payments, "
                    "agent splits, eligibility, and clawback periods. An illustrative 150 accounts "
                    "at $100 monthly retained residual produce $180,000 annually only if the "
                    "executed agreements and collected statements support those amounts. Forecast "
                    "residuals separately from earned revenue."
                ),
                (
                    "Design recovery before increasing throughput. Retry timeouts and temporary server "
                    "errors with exponential backoff, jitter, and the provider's rate-limit guidance; "
                    "stop automatic retries on authorization failures or rejected commercial instructions. "
                    "After an ambiguous order timeout, query authoritative order status before "
                    "resubmitting anything. Put exhausted jobs in a dead-letter queue with customer "
                    "impact, evidence links, retry history, and a named owner. A daily reconciliation "
                    "compares provider exports against local subscriptions and commissions, catching "
                    "events that never arrived. Maintain a manual fallback worksheet containing "
                    "verified identifiers, requested operation, reviewer identity, and confirmation "
                    "receipt; import the resulting evidence afterward instead of bypassing the "
                    "ledger. Test restoration from backups and replay events into a nonproduction "
                    "environment without external write credentials. Give each integration a narrow "
                    "credential, rotate it according to provider capabilities, and keep secrets "
                    "outside prompts, application logs, and shared worksheets. Contractor permissions "
                    "should expire with the engagement. The owner reviews every license transfer, "
                    "new annual commitment, rebate dispute settlement, and bank-detail change. "
                    "Routine matched invoice lines may clear automatically, but a tenfold quantity "
                    "jump, changed beneficiary, or new tenant identifier must stop that path. "
                    "This architecture scales reconciliation without outsourcing commercial judgment "
                    "to a language model."
                ),
            ],
            "table": {
                "caption": "Partner Billing State Transitions and Recovery Controls",
                "headers": [
                    "Event or condition requiring operational attention",
                    "Deterministic processing and evidence retention rule",
                    "Consequence requiring an identified human reviewer",
                    "Recovery path preserving customer service continuity",
                ],
                "rows": [
                    [
                        "Signed provider event arrives through documented webhook interface",
                        "Verify authenticity and persist before acknowledging successful receipt",
                        "Reviewer investigates repeated signature failures affecting expected events",
                        "Retrieve approved exports while webhook credentials are repaired",
                    ],
                    [
                        "Repeated event identifier appears after provider delivery retry",
                        "Unique constraint suppresses duplicate processing within provider scope",
                        "Reviewer checks collisions involving materially different event bodies",
                        "Preserve both hashes and investigate provider event semantics",
                    ],
                    [
                        "Annual NCE commitment lacks sufficient collected customer coverage",
                        "Block new commitment submission against uncovered payment exposure",
                        "Owner assesses credit terms and remaining return exposure",
                        "Use prefunding or decline the new annual obligation",
                    ],
                    [
                        "VIP Marketplace quantity differs from authorized customer transaction",
                        "Compare membership identifiers and effective transaction service dates",
                        "Authorized reviewer confirms intended quantities with customer evidence",
                        "Open distributor correction request without unauthorized seat pooling",
                    ],
                    [
                        "Master-agent residual payment falls below expected contract amount",
                        "Reconcile supplier collections and agreed downstream agent splits",
                        "Owner approves dispute amounts using executed agreement terms",
                        "Track disputed revenue separately until entitlement is resolved",
                    ],
                    [
                        "Order submission times out after potentially reaching provider",
                        "Query authoritative order status before considering any resubmission",
                        "Reviewer resolves ambiguous provider state before commitment changes",
                        "Escalate through support while retaining original request identifiers",
                    ],
                    [
                        "Credential expires during scheduled subscription reconciliation work",
                        "Stop affected jobs and preserve queued customer records",
                        "Credential custodian restores narrowly scoped authorized integration access",
                        "Run approved manual exports and reconcile missed periods",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before consequential execution",
                "body": (
                    "Automation may prepare the transaction packet. An identified "
                    "reviewer must establish authority and economics before execution."
                ),
                "items": [
                    "Verify customer authority, destination tenant, eligible program route, and the exact operation permitted by the signed agreement.",
                    "Verify current tier pricing, retained spread, rebate conditions, and every customer pass-through obligation against dated evidence.",
                    "Verify collected coverage for annual obligations, payment-return exposure, and documented credit limits before creating new commitments.",
                    "Verify subscription quantities, effective dates, cancellation constraints, and a recovery procedure that does not depend on reversing an irreversible order.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Normalize the authorized event",
                    "action": "Validate the provider message and resolve its customer-scoped identifiers.",
                    "detail": "Persist the source hash, provider event identifier, receipt time, and applicable agreement version before processing.",
                },
                {
                    "step": 2,
                    "title": "Reconcile the proposed economics",
                    "action": "Compare subscription state, customer authority, collected coverage, and retained contribution.",
                    "detail": "Use Decimal calculations and effective dated schedules; route mismatched quantities or unsupported program assumptions to review.",
                },
                {
                    "step": 3,
                    "title": "Authorize the consequential operation",
                    "action": "Have the designated reviewer approve the specific transaction packet.",
                    "detail": "Record reviewer identity and approved payload hash; changed payloads require a fresh review rather than inherited permission.",
                },
                {
                    "step": 4,
                    "title": "Confirm and reconcile completion",
                    "action": "Retrieve authoritative confirmation and update the customer evidence ledger.",
                    "detail": "Investigate ambiguous results before retrying; compare the next provider statement with the confirmed transaction.",
                },
            ],
        },
        {
            "heading": "3. Price automation against retained contribution, not customer spend",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the benchmark engine around comparable service, not the lowest number "
                    "scraped from a promotional page. Each comparison must match SKU, edition, "
                    "seat quantity, geography, currency, commitment length, billing cadence, support "
                    "scope, and eligibility date. Store quote expiry and evidence provenance. "
                    "Separate seat removal, product substitution, negotiated discount, and rebate "
                    "effects so the same reduction cannot be claimed twice. An illustrative "
                    "customer's eligible annual baseline of $120,000 compared with $100,000 "
                    "of equivalent delivered service creates $20,000 of verified savings. At "
                    "a contracted 30% fee, operator revenue is $6,000 and customer savings "
                    "after that fee are $14,000. Add migration charges or lost benefits "
                    "before assessing savings if the agreement requires them. The 25% to "
                    "35% fee range is a commercial parameter, not permission to choose "
                    "the highest percentage retroactively. A price floor should cover distributor "
                    "cost, delivery effort, expected credit loss, and required contribution after "
                    "client rebates. If a partner reduces a rebate by $3 per seat "
                    "across 1,000 eligible seats monthly, annual contribution falls $36,000 "
                    "unless another contractually valid adjustment offsets it. Freeze affected "
                    "quotes and reprice prospectively; never hide the compression inside fabricated "
                    "benchmark savings."
                ),
                (
                    "Reconcile the canonical Formula v2.0 cases on the supplied retained-revenue "
                    "basis. Conservative revenue of $100,000 less $68,000 total modeled "
                    "costs leaves $32,000 owner profit at 32%. Base revenue of "
                    "$500,000 less $275,000 leaves $225,000 at 45.0%. Scaled "
                    "revenue of $900,000 less $378,000 leaves $522,000 at 58%. "
                    "The first two cases use 1 FT plus 3 contractors; Scaled "
                    "uses 2 FT plus 4 contractors. These are annual scenarios, not "
                    "evidence that software alone creates the margin increase. One illustrative "
                    "Base composition is $120,000 CSP spread, $180,000 master-agent "
                    "residuals, $80,000 GPO administration revenue, and $120,000 contingent "
                    "audit fees. The GPO component could reflect $4,000,000 eligible "
                    "member purchases at a retained 2% rate; the audit component could "
                    "reflect $400,000 verified savings at 30%. Neither eligible purchases "
                    "nor savings become operator revenue. Apply retained_share exactly once "
                    "when converting an upstream fee pool into the operator's contractual "
                    "share. Do not apply it again to already retained inputs. ASC "
                    "606 principal-versus-agent analysis follows the actual promise and control "
                    "facts; the scorecard's net basis does not establish every contract's "
                    "accounting conclusion. Reconcile the management ledger to the adopted "
                    "accounting treatment."
                ),
                (
                    "Measure automation using completed task instances and actual handling time. "
                    "In an illustrative monthly queue of 1,000 eligible tasks, 760 "
                    "complete straight through and 240 require six minutes of manual "
                    "work each. Review a random 10% sample of the straight-through "
                    "tasks: 76 checks at two minutes each. Add 180 minutes "
                    "for exception remediation. Against a six-minute manual baseline for "
                    "every task, handling falls from 6,000 to 1,772 minutes, "
                    "a 70.47% reduction, while the straight-through rate is 76%. "
                    "Include monitoring and rework in subsequent measurements rather than "
                    "quietly excluding them. Budget $0.012 per machine run: $0.006 "
                    "licensed lookup allocation, $0.004 model usage, $0.0015 compute, "
                    "and $0.0005 storage and logging. The model allowance assumes "
                    "2,500 input tokens at $0.80 per million and 500 "
                    "output tokens at $4 per million; these are planning rates, "
                    "not quoted vendor prices. One thousand runs cost $12 before "
                    "labor, retries, fixed subscriptions, and taxes. At $60 per "
                    "hour, the 1,772 handling minutes cost $1,772, making "
                    "this measured batch $1,784 before those excluded costs. "
                    "Cap retry budgets and compare verified contribution per account, "
                    "not token savings alone, before expanding the queue."
                ),
            ],
            "table": {
                "caption": "Canonical Profit Reconciliation and Illustrative Unit-Economics Tests",
                "headers": [
                    "Scenario or unit requiring economic reconciliation",
                    "Retained revenue calculation and recognition boundary",
                    "Cost or profit consequence for operator",
                    "Evidence check and adverse-case fallback procedure",
                ],
                "rows": [
                    [
                        "Conservative annual case uses one employee plus three contractors",
                        "$100,000 retained annual revenue excludes customer subscription purchases",
                        "$68,000 modeled costs leave $32,000 profit at 32%",
                        "Reconcile total costs before claiming the canonical margin",
                    ],
                    [
                        "Base annual case retains the four-person operating structure",
                        "$500,000 retained annual revenue excludes underlying member purchasing",
                        "$275,000 modeled costs leave $225,000 profit at 45.0%",
                        "Match each revenue component to an enforceable entitlement",
                    ],
                    [
                        "Scaled annual case uses two employees plus four contractors",
                        "$900,000 retained annual revenue remains the operator basis",
                        "$378,000 modeled costs leave $522,000 profit at 58%",
                        "Add capacity only when reconciled contribution supports staffing",
                    ],
                    [
                        "Equivalent-service audit verifies a customer renewal savings opportunity",
                        "$20,000 verified savings times 30% earns $6,000",
                        "Customer retains $14,000 after the contracted audit fee",
                        "Recalculate savings when implementation costs change comparable economics",
                    ],
                    [
                        "Eligible GPO member purchases generate retained administration revenue",
                        "$4,000,000 eligible purchases times 2% earns $80,000",
                        "Member purchasing volume never becomes broker recognized revenue",
                        "Remove excluded purchases before assessing bracket eligibility thresholds",
                    ],
                    [
                        "Monthly automated queue processes one thousand eligible tasks",
                        "Machine processing costs $12 before labor and overhead",
                        "Measured handling adds $1,772 at $60 per hour",
                        "Include retries and monitoring before extending savings claims",
                    ],
                    [
                        "Partner tier compression reduces eligible recurring seat contribution",
                        "One thousand seats lose $3 each every month",
                        "Annual contribution decreases $36,000 without an offsetting adjustment",
                        "Freeze affected quotes and renegotiate future authorized pricing",
                    ],
                ],
            },
        },
        {
            "heading": "4. Compound verified distribution without automating promises",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create three distribution loops from verified operations. The programmatic loop "
                    "publishes narrowly scoped renewal guides and calculators using approved pricing "
                    "assumptions, dated evidence, and explicit inputs; it never exposes private "
                    "partner schedules or customer invoices. The referral loop gives satisfied "
                    "customers a shareable assessment link after a verified outcome, with "
                    "permission to use any named testimonial and clear disclosure of "
                    "referral compensation where relevant. The outbound loop routes evidence-supported "
                    "accounts into human-approved email sequences and lawful calling workflows. "
                    "A public MX record does not establish permission for automated "
                    "marketing texts or prerecorded calls. Apply 47 U.S.C. 227 "
                    "and 47 CFR 64.1200 to the actual calling technology, "
                    "number type, and consent context. Commercial email must satisfy "
                    "15 U.S.C. 7704, including accurate headers, a valid postal "
                    "address, and timely opt-out processing. Maintain suppression records "
                    "across the CRM and every sending provider. The FTC's "
                    "Telemarketing Sales Rule does not give business outreach a "
                    "blanket exemption from deception restrictions; review 16 CFR "
                    "310.3 and 310.6 against the campaign. Have a person "
                    "approve initial claims and every material template change, "
                    "then pause sequences automatically when consent records, source "
                    "evidence, or suppression synchronization fail."
                ),
                (
                    "Treat agency_ad_spend_card_multiplier_rebate_cycling as an adjacent, separately tracked play, "
                    "not a mechanism for inflating SaaS revenue. Route only genuine, "
                    "client-authorized advertising purchases through an eligible agency payment "
                    "arrangement whose issuer, advertising platform, and customer contracts "
                    "permit the activity. An illustrative $100,000 monthly advertising "
                    "budget earning a realizable 2% reward produces $2,000 "
                    "of reward value. Deduct $800 processing expense, $300 "
                    "funding cost, $600 contractual client pass-through, and $100 "
                    "expected loss allowance; only $200 remains before overhead "
                    "and tax treatment. Exclude points that cannot be redeemed "
                    "under the operating plan, and do not stack overlapping "
                    "reward assumptions without contractual support. That $100,000 "
                    "is client advertising spend, not brokerage revenue, and "
                    "the $200 is not added to the canonical cases "
                    "presented here. A Python reconciliation job can match "
                    "authorized campaign invoices, settled card transactions, reward "
                    "statements, and client credits while flagging caps and "
                    "excluded merchant categories. People approve funding exposure "
                    "and arrangement changes. Never create artificial purchases, "
                    "circular payments, or extra advertising merely to earn "
                    "rewards. If issuer eligibility changes or contribution "
                    "turns negative, move to client-direct billing or "
                    "prefunded approved agency terms and stop rewards-dependent "
                    "spending immediately."
                ),
                (
                    "Run distribution as a cohort ledger with explicit economic stopping "
                    "rules. Illustratively, 1,000 qualified guide visits producing 50 "
                    "assessment requests, 20 evidence-complete audits, and four signed "
                    "customers imply a 5% request rate, 40% document-completion "
                    "rate, and 20% audit-to-customer rate. At $1,200 "
                    "campaign cost, acquisition cost is $300 per signed "
                    "customer before assessment labor. If each customer produces "
                    "$1,000 first-year retained revenue, the cohort contributes "
                    "$4,000 before acquisition, fulfillment, and overhead, not "
                    "$4,000 owner profit. Track refunds, payment delays, "
                    "churn, and contractor time by cohort before increasing "
                    "spend. The full-time owner controls partner relationships, "
                    "exception economics, and consequential approvals; three contractors "
                    "cover evidence operations, reconciliation, and distribution quality "
                    "under documented scopes. Review weekly samples by risk "
                    "stratum, not just at random: include every new "
                    "vendor adapter, changed model prompt, disputed savings "
                    "calculation, and unusually large commitment. Quarantine an "
                    "adapter when discrepancies exceed its predeclared tolerance, "
                    "revert to approved exports, and replay corrected "
                    "events after testing. Publish only refreshed calculators "
                    "and substantiated outcomes. The flywheel compounds because "
                    "each completed engagement improves authorized evidence, "
                    "benchmark coverage, and referral credibility, while "
                    "the human team retains control over obligations "
                    "that software cannot safely unwind."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels, Reward Economics, and Stop Conditions",
                "headers": [
                    "Distribution mechanism and authorized operating input",
                    "Concrete conversion or contribution measurement rule",
                    "Human decision retained outside automated execution",
                    "Failure signal and immediate recovery action",
                ],
                "rows": [
                    [
                        "Programmatic renewal guides use approved dated benchmark assumptions",
                        "Track qualified visits through evidence-complete customer assessment requests",
                        "Reviewer approves claims and protects confidential partner schedules",
                        "Withdraw stale calculators until current assumptions are verified",
                    ],
                    [
                        "Customer referral links follow verified delivered savings outcomes",
                        "Attribute signed customers without counting duplicate referral submissions",
                        "Customer approves named testimonials and relevant compensation disclosures",
                        "Remove disputed endorsements and retain underlying permission records",
                    ],
                    [
                        "Commercial email campaigns use documented audience selection criteria",
                        "Measure signed customer contribution after outreach and review costs",
                        "Reviewer approves material claims and opt-out processing design",
                        "Pause sending when suppression synchronization fails across providers",
                    ],
                    [
                        "Calling workflows distinguish technology and recipient number context",
                        "Track authorized contacts without treating public records as consent",
                        "Qualified reviewer resolves campaign-specific calling requirements before launch",
                        "Stop affected calls when required authorization evidence fails",
                    ],
                    [
                        "Agency reward lane routes genuine authorized advertising purchases",
                        "$2,000 rewards less $1,800 deductions leaves $200",
                        "Owner verifies issuer eligibility and client economic allocation",
                        "Switch client-direct or prefunded approved terms when economics fail",
                    ],
                    [
                        "Illustrative acquisition cohort converts four customers from visits",
                        "$1,200 campaign spending divided by four customers equals $300",
                        "Owner compares collected contribution against complete acquisition costs",
                        "Reduce spend when cohort payback exceeds approved limits",
                    ],
                    [
                        "Weekly risk-stratified quality review tests changing automation components",
                        "Measure error severity and handling minutes alongside task completion",
                        "Owner approves adapter restoration after corrected replay evidence",
                        "Quarantine defective adapters and reconcile through approved exports",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail and the arithmetic; keep authority over every obligation.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create customer-scoped records linking authorization, contracts, subscriptions, source documents, and effective partner terms before importing prospects.",
        "Deploy a read-only DNS and document-extraction pipeline with source quotations, Decimal validation, and manual handling for ambiguous renewal clauses.",
        "Implement idempotent provider ingestion, authoritative reconciliation, dead-letter ownership, and tested manual-export recovery before enabling external writes.",
        "Reconcile retained revenue to the $100,000, $500,000, and $900,000 canonical cases without including client subscription or advertising spend.",
        "Measure a 1,000-task pilot using straight-through completion, sampled error severity, total handling time, and fully allocated run costs.",
        "Launch reviewed content, referral, and outbound cohorts with synchronized suppressions; isolate agency reward economics and enforce the client-direct fallback.",
    ],
    "statutory_citations": [
        {
            "title": "47 U.S.C. 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Evaluate marketing calls and messages against the statute's "
                "technology, recipient, and consent requirements before activating outreach."
            ),
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Implement applicable calling restrictions, consent controls, "
                "do-not-call procedures, and opt-out handling for the actual campaign."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Commercial email workflows need accurate routing information, "
                "required sender information, and effective opt-out processing."
            ),
        },
        {
            "title": "16 CFR 310.3 — Deceptive telemarketing acts or practices",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310/section-310.3",
            "relevance": (
                "Review telemarketing representations about savings, affiliation, "
                "pricing, and service characteristics for prohibited deception."
            ),
        },
        {
            "title": "16 CFR 310.6 — Exemptions",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310/section-310.6",
            "relevance": (
                "Determine the precise scope of business-call exemptions and "
                "their exceptions rather than assuming every B2B campaign is exempt."
            ),
        },
        {
            "title": "16 CFR 255.5 — Disclosure of material connections",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": (
                "The FTC endorsement guides explain disclosure of material "
                "connections relevant to compensated referrals and published testimonials."
            ),
        },
    ],
}
