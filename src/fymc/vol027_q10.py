from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 7 FT + 3 C (10 people) business acquisition team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Seven ETA Automation Plays: Python Webhooks, Evidence-Linked QoE, SBA Covenant Monitoring, and Measured Distribution Loops",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #13, Business Acquisition, ranks #27 with a 57/100 Money-to-Manpower Score: "
        "automation improves operating discipline, but does not remove capital intensity or leverage. "
        "This chapter maps seven plays: sourcing research, qualification, QoE evidence preparation, "
        "financial reporting, back-office routing, fulfillment coordination, and distribution feedback. "
        "A 7 FT + 3 C pod uses Python, authenticated webhooks, bounded language-model tasks, and "
        "human release decisions to target 70%+ automation of measured repetitive work. Canonical "
        "annual owner profit remains $60,000 Conservative, $243,750 Base, and $540,000 Scaled, "
        "after interest and before principal repayments. The Scaled case requires 8 FT + 4 C. "
        "Build durable evidence trails, price every completed workflow, and convert verified customer "
        "outcomes into repeatable acquisition channels without confusing pipeline value with acquired-business sales."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$750,000",
            "context": "Annual acquired-business sales; interest included in margin",
            "note": "8% margin; $60,000 annual owner net profit; 7 FT + 3 C; before principal repayments",
        },
        {
            "label": "Base",
            "value": "$1,875,000",
            "context": "Annual acquired-business sales; interest included in margin",
            "note": "13.0% margin; $243,750 annual owner net profit; 7 FT + 3 C; before principal repayments",
        },
        {
            "label": "Scaled",
            "value": "$3,000,000",
            "context": "Annual acquired-business sales; interest included in margin",
            "note": "18% margin; $540,000 annual owner net profit; 8 FT + 4 C; before principal repayments",
        },
    ],
    "sections": [
        {
            "heading": "1. Map Seven Plays to Accountable People Before Automating Work",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the acquisition thesis, not an agent shopping list. Candidate #13 buys and "
                    "operates cash-flowing SMBs; its revenue is acquired-business sales, not purchase consideration, "
                    "seller proceeds, or the face value of financing. For this chapter, map the seven operator "
                    "plays explicitly: sourcing research, qualification, QoE evidence preparation, financial reporting, "
                    "back-office routing, fulfillment coordination, and distribution feedback. Give every play an "
                    "input contract, an evidence record, a responsible person, and a reversible output. A broker "
                    "teaser can become a research record automatically; it cannot become an investment conclusion "
                    "merely because a model produces fluent prose. Assign the seven full-time seats to the "
                    "owner and investment lead, general manager, controller, sourcing and growth lead, customer "
                    "success lead, and two delivery operators. Assign the three contractor seats to transaction "
                    "counsel, a QoE specialist, and an automation engineer, with their hours budgeted rather than "
                    "treated as unlimited capacity. This is an illustrative staffing allocation within the "
                    "canonical ten-person constraint, not ten acquisition staff sitting above an uncounted workforce. "
                    "Choose targets whose delivery model actually fits these seats. If the acquired company "
                    "needs more field labor, reconcile that requirement before underwriting its operating margin "
                    "or promising an automated turnaround."
                ),
                (
                    "Define the 70%+ objective using observed work, not the number of software features enabled. "
                    "During ten business days, record eligible repetitive tasks and their manual baseline minutes "
                    "across all seven plays. Freeze that denominator before the pilot. An illustrative week "
                    "contains 1,000 eligible task instances consuming 100 manual hours; automation completes "
                    "760 instances without correction, but exception handling, sampled QA, and system maintenance "
                    "still consume 26 hours. The task automation rate is 76%, while net repetitive labor "
                    "displacement is 74%; report both and also report all operating hours outside the eligible "
                    "pool. Count failed attempts and rework against the result instead of quietly deleting them "
                    "from the sample. Consequential decisions remain human work even when evidence assembly is "
                    "automated: purchase offers, lender representations, employee actions, vendor bank changes, "
                    "customer credits, and public claims require named release authority. Break results out by "
                    "play because fast teaser extraction can otherwise conceal broken fulfillment routing. The "
                    "general manager reviews weekly exception volume against actual staff availability. When "
                    "automation creates more review work than the pod can absorb, reduce intake or narrow "
                    "the workflow. Do not manufacture a favorable percentage by excluding the hardest ordinary "
                    "cases after the measurement period has begun."
                ),
                (
                    "Sequence implementation around the first 100 operating days. Before closing, use seller-authorized "
                    "read access and keep diligence files separate from the acquired company's production systems. "
                    "During days 1 through 30, automate bank-feed reconciliation preparation, daily collections "
                    "visibility, and customer handoff reminders; these expose hidden liabilities and attrition "
                    "before growth experiments amplify them. During days 31 through 60, standardize invoice "
                    "routing, delivery checklists, and renewal alerts. During days 61 through 100, expand sourcing "
                    "and distribution only after service reliability and cash conversion hold steady. The "
                    "canonical $200,000–$1,000,000 startup capital range is acquisition context, not a software "
                    "budget, and the $15,000–$70,000 monthly opex range is not a complete income statement. "
                    "Build an explicit bridge for cost of delivery, overhead, interest, and working capital "
                    "rather than forcing those ranges to equal scenario expenses. The six-to-eighteen-month "
                    "first-deal horizon also means sourcing automation must survive long quiet periods without "
                    "inventing urgency. Maintain a target exclusion register for geography, licensing, customer "
                    "concentration, and incompatible labor requirements. Use the matrix below as ownership design: "
                    "each output has a release boundary and an observable failure signal, so a departing "
                    "contractor cannot leave behind an opaque system nobody can safely operate."
                ),
            ],
            "table": {
                "caption": "Seven Mapped Business Acquisition Plays Within the Ten-Person Pod",
                "headers": [
                    "Mapped operator play",
                    "Accountable pod ownership",
                    "Automated evidence and workflow",
                    "Human release boundary and failure signal",
                ],
                "rows": [
                    [
                        "Play one: sourcing research for thesis-matched acquisition targets",
                        "Sourcing and growth lead owns research freshness and permissions",
                        "Python extracts permitted teaser fields with source document references",
                        "Investment lead reviews fit when source evidence conflicts materially",
                    ],
                    [
                        "Play two: qualification against capital and operating constraints",
                        "Owner and investment lead owns acquisition screening decisions",
                        "Rules compare asking price, concentration, geography, and labor requirements",
                        "Owner releases seller contact after verifying deal thesis alignment",
                    ],
                    [
                        "Play three: QoE evidence preparation before purchase commitments",
                        "Contract QoE specialist supports controller with bounded engagement hours",
                        "Document extraction links revenue claims to invoices and deposits",
                        "Specialist reviews adjustments when cash and ledger evidence disagree",
                    ],
                    [
                        "Play four: financial reporting across cash and covenant measures",
                        "Controller owns reporting accuracy while general manager owns responses",
                        "Scheduled jobs assemble cash forecasts and lender reporting drafts",
                        "Controller releases reports after reconciling balances and contractual definitions",
                    ],
                    [
                        "Play five: back-office routing for invoices and employee records",
                        "Controller owns payment controls with counsel reviewing employment changes",
                        "Workflow routes invoices, onboarding forms, and missing documentation alerts",
                        "Authorized people release payments after independently verifying sensitive changes",
                    ],
                    [
                        "Play six: fulfillment coordination for acquired-business customer commitments",
                        "General manager directs customer success and two delivery operators",
                        "Scheduling rules prepare work packets and flag service exceptions",
                        "Delivery operator accepts commitments when capacity or specifications change",
                    ],
                    [
                        "Play seven: distribution feedback from verified customer operating outcomes",
                        "Sourcing and growth lead coordinates customer success evidence collection",
                        "CRM connects permitted referrals and campaigns to collected sales",
                        "Growth lead releases claims after checking permission and attribution",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Acquisition Thesis From Automated Optimism",
                "body": "Veteran operators use automation to expose disagreement early, not to make every target resemble the investment memorandum.",
                "items": [
                    "Preserve the original seller export and checksum it before normalizing accounts; otherwise a changing chart of accounts can erase the trail behind a QoE adjustment.",
                    "Track seller involvement by customer and delivery task during transition; apparent automation savings can actually be unpaid seller labor that disappears after closing.",
                    "Build concentration alerts from invoiced and collected revenue separately; a large customer's slow payments can matter before their revenue share changes.",
                    "Make the automation engineer document a manual close and dispatch procedure before expanding workflows; contractor availability must not determine whether the business can collect cash.",
                ],
            },
        },
        {
            "heading": "2. Build Evidence-Linked Python and Webhook Pipelines With Safe Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a narrow Python service as the integration spine, with QuickBooks Online or Xero "
                    "as the accounting record and HubSpot as the relationship record where those products "
                    "fit the acquired company. An HTTPS endpoint receives provider events through a managed "
                    "gateway; implement each provider's documented authentication scheme rather than assuming every "
                    "webhook uses the same signature format. Verify the raw body before decoding, check "
                    "timestamps when supported, and reject replayed delivery identifiers. Persist the accepted "
                    "event before acknowledging it, then process asynchronously. A Python 3.9 worker can use "
                    "json, decimal, hashlib, hmac, urllib.request, and sqlite3 without third-party packages. SQLite "
                    "is appropriate for a low-volume single-writer pilot with tested backups; higher concurrency "
                    "requires a deliberately selected durable queue and database, not additional writers bolted "
                    "onto a fragile local file. Store provider, tenant, event identifier, payload digest, received "
                    "time, schema version, attempt count, and processing state. Fetch authoritative records using "
                    "least-privilege credentials where the webhook contains only an identifier. Validate currency, "
                    "dates, required fields, and tenant ownership before creating internal tasks. A malformed "
                    "invoice must enter an exception queue instead of becoming a zero-dollar transaction that "
                    "silently improves the dashboard. Keep sensitive payloads out of routine application logs."
                ),
                (
                    "Insert language models only where probabilistic interpretation is useful: classifying seller "
                    "documents, extracting contract renewal terms, drafting customer follow-ups, and summarizing "
                    "reconciliation exceptions. Treat every uploaded document as untrusted content, including text "
                    "that tells the model to reveal secrets or contact outside services. The extraction prompt "
                    "requires a bounded JSON object with source page, quoted evidence, proposed value, and "
                    "an explicit unresolved state for missing evidence. Python validates the schema and checks "
                    "that quoted text actually appears in the supplied source. Confidence scores may prioritize "
                    "review, but cannot prove a revenue recognition judgment or establish that an add-back "
                    "is recurring. Keep payment credentials and unrestricted network tools outside the model "
                    "context. Use decimal.Decimal for amounts and deterministic reconciliation rules for totals; "
                    "a model does not calculate the final purchase-price bridge. Compare monthly sales across "
                    "the general ledger, invoice register, bank deposits, credit notes, and tax records, explaining "
                    "timing differences rather than forcing equality. The QoE contractor signs off disputed "
                    "adjustments and the controller owns posting decisions. Restrict seller data to authorized "
                    "users and service providers, minimize what leaves the document repository, and set retention "
                    "by transaction need, contractual obligations, and applicable recordkeeping requirements."
                ),
                (
                    "Design every external write for interruption. A workflow state machine should distinguish "
                    "received, validated, drafted, reviewed, released, and reconciled records, with failed events "
                    "held separately for investigation. Persist a stable operation key before sending an invoice "
                    "draft or CRM update. Where the destination supports idempotency keys, use them; otherwise "
                    "query the destination by your external reference before replaying an uncertain request. "
                    "A timeout after transmission does not prove the write failed. Retry transient rate limits "
                    "and server errors with bounded exponential backoff and jitter, honoring provider retry "
                    "instructions, but route authorization failures and invalid schemas to a person. After "
                    "three unsuccessful attempts in this illustrative policy, move the event into a dead-letter "
                    "queue with an owner and response deadline. Reconcile event counts against source-system "
                    "exports each day because webhook delivery alone does not establish completeness. When "
                    "a provider fails, the customer success lead uses the last validated dispatch list and "
                    "the controller prepares payments through the existing bank workflow. Import the resulting "
                    "manual references before restarting automation. Test restoration from backup, duplicate event "
                    "delivery, delayed messages, and partial posting in a sandbox. Release a connector only "
                    "after the operator can demonstrate recovery without duplicate customer charges or lost "
                    "fulfillment commitments."
                ),
            ],
            "table": {
                "caption": "Python Integration Failure Modes and Recoverable Operating Controls",
                "headers": [
                    "Pipeline stage and evidence",
                    "Deterministic processing control",
                    "Named human review responsibility",
                    "Failure recovery and reconciliation evidence",
                ],
                "rows": [
                    [
                        "Broker document intake preserves authorized originals and source timestamps",
                        "Hash files and validate document identifiers before extraction begins",
                        "Sourcing lead checks permission scope and target identity matches",
                        "Quarantine conflicting versions while retaining both original evidence records",
                    ],
                    [
                        "Accounting webhook receipt records tenant and provider delivery identifiers",
                        "Verify provider authentication and persist events before acknowledging receipt",
                        "Automation engineer investigates repeated signature failures and tenant mismatches",
                        "Reconcile source exports daily to detect missed event deliveries",
                    ],
                    [
                        "QoE extraction links proposed adjustments to quoted source passages",
                        "Validate JSON fields and reject unsupported currency conversions automatically",
                        "QoE specialist resolves recurring expense judgments and disputed adjustments",
                        "Return documents for manual extraction when evidence cannot validate",
                    ],
                    [
                        "Invoice preparation connects purchase orders with accepted delivery evidence",
                        "Match amounts using decimal arithmetic and stable operation references",
                        "Controller reviews exceptions before any accounting posting is released",
                        "Query destination records before replaying requests with ambiguous outcomes",
                    ],
                    [
                        "Customer dispatch preparation checks staffing and existing service commitments",
                        "Apply capacity rules before generating proposed customer appointment messages",
                        "Delivery operator confirms unusual requirements and changed service windows",
                        "Use validated dispatch export during provider interruptions and reconcile",
                    ],
                    [
                        "Reporting publication retains report versions and signed review records",
                        "Reconcile ledger balances and flag changed lender calculation definitions",
                        "Controller releases lender packets after checking supporting debt schedules",
                        "Withdraw superseded drafts and issue traceable corrected report versions",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture and authenticate",
                    "action": "Receive the provider event, verify its documented authentication, and persist the event envelope.",
                    "detail": "Record tenant ownership, raw-body digest, delivery identifier, and receipt time; reject invalid requests without processing business content.",
                },
                {
                    "step": 2,
                    "title": "Validate and prepare",
                    "action": "Fetch permitted source records, enforce field contracts, and prepare a reversible draft.",
                    "detail": "Use deterministic money calculations and evidence-linked model extraction; unresolved fields become assigned exceptions rather than invented values.",
                },
                {
                    "step": 3,
                    "title": "Review and release",
                    "action": "Route consequential outputs to the named owner before sending or posting.",
                    "detail": "Save the reviewed version and operation key; changing bank details, amounts, recipients, or commitments requires renewed review.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and recover",
                    "action": "Compare destination state with the expected result and close the event only after reconciliation.",
                    "detail": "Investigate ambiguous writes before retrying, assign dead-letter events, and import manual fallback references before replaying queued work.",
                },
            ],
        },
        {
            "heading": "3. Price Automated Runs and Reconcile Them to Owner Cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Keep the three scorecard scenarios fixed while evaluating automation underneath them. Conservative "
                    "sales of $750,000 at 8% produce $60,000 annual owner net profit; Base sales of "
                    "$1,875,000 at 13.0% produce $243,750; Scaled sales of $3,000,000 at 18% produce $540,000. "
                    "The corresponding expense envelopes are $690,000, $1,631,250, and $2,460,000, respectively. These "
                    "margins include interest and precede principal repayments. Do not add estimated automation "
                    "savings to those profits unless rebuilding the entire scenario with an explicit expense "
                    "bridge. Conservative and Base both use 7 FT + 3 C, while Scaled uses 8 FT "
                    "+ 4 C, or twelve people. A software demonstration cannot justify calling the Scaled "
                    "case a ten-person operation. Principal belongs in a separate cash schedule: an illustrative "
                    "$90,000 annual principal requirement would leave Base profit less principal of $153,750, "
                    "before working-capital movements, capital expenditures, and owner-level taxes. That amount "
                    "is neither revised scorecard profit nor automatically distributable cash. Read the executed "
                    "loan documents for reporting dates, debt-service definitions, restricted payments, and permitted "
                    "indebtedness. SBA program eligibility and use-of-proceeds requirements remain relevant when "
                    "structuring an acquisition; automated summaries cannot replace lender confirmation of the "
                    "actual financing terms, seller-note treatment, and current program requirements."
                ),
                (
                    "Price one workflow with a transparent bill of materials. Assume an evidence-preparation run "
                    "uses 12,000 input tokens at an illustrative $3 per million and 2,000 output tokens "
                    "at an illustrative $15 per million, producing $0.066 of model cost. Add $0.014 "
                    "for queue, storage, and request handling, giving $0.080 before retries and review. "
                    "These are planning rates, not a vendor quotation. If 10% of runs require one "
                    "complete additional attempt, expected machine cost is $0.088 per original run. If "
                    "20% require three minutes of human review at a loaded $45 hourly rate, expected "
                    "review cost is $0.450, making variable cost $0.538 per run. At 2,000 original "
                    "runs monthly, variable cost is $1,076. Add $600 for connector subscriptions and maintenance "
                    "allocation to reach $1,676 monthly, or $0.838 per completed run when all original "
                    "runs eventually complete. Failed terminal runs reduce that denominator and increase effective "
                    "unit cost. Separate cash invoices from allocated employee time so the accounting expense "
                    "bridge does not count the same salary twice. Log actual tokens, retries, review "
                    "minutes, completion outcomes, and maintenance effort by play. A cheap extraction step "
                    "can still create an expensive workflow when ambiguous documents repeatedly consume specialist "
                    "attention downstream."
                ),
                (
                    "Translate labor capacity into economics without pretending that saved minutes immediately become "
                    "cash. If the same illustrative workload previously required four minutes per run at "
                    "$45 per hour, its loaded labor value was $6,000 monthly. Subtracting the $1,676 "
                    "workflow cost yields $4,324 of potential capacity value, not automatic incremental profit. "
                    "The ten-person pod may redeploy that time into collections, customer retention, and delivery "
                    "quality while payroll remains unchanged. Recognize a cash saving only when a real "
                    "expense disappears, such as a reduced contractor invoice or an avoided incremental hire "
                    "supported by capacity records. Monitor review precision, correction rates, and cash outcomes "
                    "together. One erroneous supplier payment can overwhelm months of token savings; independently "
                    "verify bank changes using a previously trusted contact channel and keep payment release "
                    "separate from invoice extraction. Maintain payroll records required by 29 CFR 516.2 "
                    "and tax records under 26 U.S.C. 6001 even when document handling becomes automated. "
                    "For hidden-liability monitoring, compare vendor statements, aged payables, payroll accruals, and "
                    "customer deposits against the opening balance sheet. Escalate discrepancies to the controller "
                    "and transaction counsel before treating them as post-close operating expenses. Review automation "
                    "economics monthly alongside attrition and debt service, because efficiency that damages revenue "
                    "or obscures liabilities does not improve acquisition quality."
                ),
            ],
            "table": {
                "caption": "Canonical Scenario Bridge and Illustrative Automation Cost Ledger",
                "headers": [
                    "Scenario or operating measurement",
                    "Revenue or cost calculation",
                    "Interpretation within the acquisition model",
                    "Evidence required before operator action",
                ],
                "rows": [
                    [
                        "Conservative case retains seven employees and three contractor seats",
                        "$750,000 annual sales multiplied by 8% equals $60,000 profit",
                        "$690,000 expense envelope includes interest but excludes principal repayment",
                        "Controller reconciles annual ledger totals and separate principal schedule",
                    ],
                    [
                        "Base case retains seven employees and three contractor seats",
                        "$1,875,000 annual sales multiplied by 13.0% equals $243,750 profit",
                        "$1,631,250 expense envelope includes interest but excludes principal repayment",
                        "Controller confirms operating expenses and debt interest are included",
                    ],
                    [
                        "Scaled case requires eight employees and four contractor seats",
                        "$3,000,000 annual sales multiplied by 18% equals $540,000 profit",
                        "$2,460,000 expense envelope supports twelve people rather than ten",
                        "General manager verifies delivery capacity before accepting scaled commitments",
                    ],
                    [
                        "Illustrative machine cost includes one retry for ten percent",
                        "$0.080 initial machine cost multiplied by 1.10 equals $0.088",
                        "Machine spending excludes human review and monthly maintenance allocation",
                        "Engineer compares provider usage invoices against original run identifiers",
                    ],
                    [
                        "Illustrative review cost averages across all original workflow runs",
                        "Twenty percent times three minutes times $0.75 equals $0.450",
                        "Combined variable cost becomes $0.538 per original workflow run",
                        "Controller distinguishes allocated employee time from incremental cash spending",
                    ],
                    [
                        "Illustrative monthly workflow cost assumes every original run completes",
                        "Two thousand runs times $0.538 plus $600 equals $1,676",
                        "Monthly cost divided by completed runs produces $0.838 each",
                        "Operator includes terminal failures when evaluating effective completion economics",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Expanding Automation",
                "body": "The general manager records these checks for each material workflow change; automation volume expands only within demonstrated review and recovery capacity.",
                "items": [
                    "Verify the scenario bridge still yields $60,000, $243,750, or $540,000 annual owner profit as applicable, with interest included and principal tracked separately.",
                    "Confirm every payment, lender submission, purchase offer, and employment action has a named human release owner and retained evidence of the reviewed version.",
                    "Demonstrate duplicate-event handling, ambiguous-write reconciliation, backup restoration, and manual fulfillment fallback using test records before production expansion.",
                    "Confirm measured review hours fit the 7 FT + 3 C pod; budget the Scaled case's additional employee and contractor before adopting its throughput assumptions.",
                ],
            },
        },
        {
            "heading": "4. Turn Verified Operating Outcomes Into Distribution Flywheels",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Separate acquisition sourcing from customer demand generation in both the CRM and the "
                    "income statement. The sourcing loop begins with thesis-matched businesses, advances through "
                    "permissioned research and human qualification, and ends with a signed transaction only when "
                    "diligence and financing support it. The operating-company growth loop begins with a real "
                    "customer need and ends with delivered, recognized sales and measured collections. Build "
                    "programmatic pages only from verified service coverage, actual capabilities, and useful operating "
                    "data. A regional maintenance business might publish genuine service-area pages showing response "
                    "windows and equipment supported; it should not generate hundreds of near-identical pages "
                    "for locations it cannot serve. Use Search Console for search performance, HubSpot for "
                    "lead stages, and the accounting ledger for recognized revenue. Assign campaign identifiers "
                    "at inquiry creation and retain them through quote, job, invoice, and collection. The "
                    "growth lead reviews factual claims while a delivery operator confirms capacity before "
                    "publication. Treat model-written pages as drafts and prevent customer records from leaking "
                    "into public examples. Feed lost-quote reasons back into service design and qualification, "
                    "not merely into another batch of content. This connects play seven to plays two "
                    "and six without mistaking website traffic or the seller pipeline's estimated value for "
                    "operator revenue."
                ),
                (
                    "Create a referral loop from completed work rather than manufactured enthusiasm. After the "
                    "customer success lead verifies delivery and resolves open complaints, send a concise request "
                    "for an introduction or an honest review. Do not condition incentives on positive sentiment, "
                    "fabricate testimonials, or ask a model to impersonate a customer; 16 CFR Part 465 "
                    "addresses deceptive review and testimonial practices. Obtain permission before naming a customer "
                    "or publishing their results. A useful viral asset is a shareable maintenance checklist "
                    "or operating benchmark derived from authorized, sufficiently aggregated records, with a clear "
                    "path back to an actual service offering. For outbound acquisition sourcing, prepare a "
                    "small list of thesis-matched owners from permitted sources and have the investment lead "
                    "approve individualized messages. Commercial email must meet applicable 15 U.S.C. 7704 "
                    "requirements, including accurate routing information, truthful subject lines, required identification, "
                    "a valid postal address, and functioning opt-out handling. Process opt-outs within ten "
                    "business days and suppress future sends across connected systems. Keep telephone and text "
                    "campaigns outside this email workflow until their separate rules and permissions are assessed. "
                    "Track reply quality and seller trust, not just delivery volume. An automated message "
                    "that misstates the buyer's capital availability can damage both sourcing relationships and "
                    "later transaction disclosures."
                ),
                (
                    "Run the flywheel as a cohort experiment with operational stop rules. For an illustrative "
                    "customer campaign, $2,400 of fully identified acquisition spending produces 40 qualified inquiries "
                    "and eight new customers, giving $300 acquisition cost per customer. If those customers "
                    "produce $12,000 in collected sales and $4,800 in contribution before acquisition spending, "
                    "the cohort leaves $2,400 after acquisition spending and before overhead, interest, and other "
                    "unallocated expenses. These are channel diagnostics, not an additional scorecard scenario or "
                    "permission to add $2,400 to canonical owner profit. Avoid counting an existing customer's "
                    "routine purchase as newly acquired revenue merely because they clicked an email. Review "
                    "cohorts by first purchase month, source, repeat purchases, refunds, and service load. Pause "
                    "a channel when cancellations, overdue receivables, or delivery backlog exceed the thresholds "
                    "set by the general manager before launch. Return those failure reasons to qualification "
                    "rules and fulfillment planning, creating a feedback loop grounded in business outcomes. "
                    "On the acquisition side, measure research-to-conversation and conversation-to-qualified-opportunity "
                    "rates separately, retaining rejection reasons for the next sourcing cycle. Publish one "
                    "weekly operating packet covering cash, customer retention, exceptions, automation cost, and "
                    "channel cohorts. Scale only the loops whose evidence survives reconciliation and whose "
                    "review burden fits the people actually on payroll and contract."
                ),
            ],
            "table": {
                "caption": "Distribution Loops That Reconcile to Capacity, Customers, and Cash",
                "headers": [
                    "Distribution or sourcing loop",
                    "Verified input and automated draft",
                    "Human release and operating constraint",
                    "Closed-loop measurement and corrective response",
                ],
                "rows": [
                    [
                        "Programmatic search pages for genuinely supported regional service needs",
                        "Generate drafts from verified coverage and actual equipment capabilities",
                        "Growth lead checks claims while delivery operator verifies capacity",
                        "Connect inquiries to collected sales and retire misleading pages",
                    ],
                    [
                        "Customer referral requests following completed and accepted service delivery",
                        "Trigger draft requests after completion and unresolved complaint checks",
                        "Customer success lead reviews timing and respects communication preferences",
                        "Measure referred customers and stop requests when complaints reopen",
                    ],
                    [
                        "Shareable operating checklists built from permitted aggregated service insights",
                        "Prepare useful benchmarks without exposing identifiable customer operating records",
                        "General manager validates methods and customer permissions before publication",
                        "Track qualified inquiries rather than downloads without purchasing intent",
                    ],
                    [
                        "Owner outreach for thesis-matched cash-flowing business acquisition targets",
                        "Prepare researched messages with accurate buyer capabilities and identifiers",
                        "Investment lead releases messages after reviewing source permissions individually",
                        "Suppress opt-outs globally and retain reasons for rejected targets",
                    ],
                    [
                        "Renewal and cross-service reminders grounded in actual customer contracts",
                        "Draft reminders from verified renewal dates and relevant service history",
                        "Customer success lead checks eligibility and existing service issues",
                        "Compare incremental collected sales with refunds and additional workload",
                    ],
                    [
                        "Weekly cohort review linking demand generation with operating delivery",
                        "Join campaign identifiers to quotes, invoices, collections, and exceptions",
                        "General manager pauses channels exceeding predefined service capacity thresholds",
                        "Feed cancellation reasons into qualification rules and scheduling capacity",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence and the repetition; keep ownership of the judgment, the cash, and the customer promise.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Assign all seven mapped plays to the seven employee and three contractor seats, documenting source access, release authority, and manual fallback ownership.",
        "Measure ten business days of repetitive tasks, freeze the eligible denominator, and report both correction-free completion and net labor displacement against the 70%+ objective.",
        "Implement authenticated webhook intake, durable event records, evidence-linked extraction, deterministic money calculations, and destination reconciliation before enabling external writes.",
        "Reconcile the three canonical revenue and profit cases, keep principal separate, and place automation costs inside the existing expense envelopes without double-counting staff time.",
        "Pilot one customer-demand loop and one acquisition-sourcing loop with permitted inputs, human-reviewed messages, suppression handling, and source-to-outcome attribution.",
        "Review the weekly operating packet and demonstrate recovery drills before increasing throughput; move to the Scaled staffing assumption only with eight employees and four contractors budgeted.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 636(a) — SBA Business Loan Authority",
            "url": "https://www.law.cornell.edu/uscode/text/15/636",
            "relevance": "Provides statutory authority for SBA business lending; acquisition financing workflows must preserve the distinction between program authority, lender underwriting, and executed loan terms.",
        },
        {
            "title": "13 CFR 120.110 — Businesses Ineligible for SBA Business Loans",
            "url": "https://www.ecfr.gov/current/title-13/section-120.110",
            "relevance": "Build eligibility screening into acquisition qualification and escalate ownership, activity, or business-model issues before presenting an SBA financing assumption.",
        },
        {
            "title": "13 CFR 120.120 — Permitted Uses of SBA Loan Proceeds",
            "url": "https://www.ecfr.gov/current/title-13/section-120.120",
            "relevance": "Map proposed acquisition expenditures to permitted proceeds uses and retain the lender-reviewed sources-and-uses schedule rather than relying on automated transaction summaries.",
        },
        {
            "title": "29 CFR 516.2 — Employee Records Required Under the FLSA",
            "url": "https://www.ecfr.gov/current/title-29/section-516.2",
            "relevance": "Payroll automation must preserve required records for covered employees, including applicable hours, pay rates, earnings, deductions, and payment information.",
        },
        {
            "title": "26 U.S.C. 6001 — Records, Statements, and Special Returns",
            "url": "https://www.law.cornell.edu/uscode/text/26/6001",
            "relevance": "Maintain tax-supporting records and traceable transaction evidence when replacing manual bookkeeping workflows with automated extraction and routing.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for Commercial Electronic Mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Commercial email workflows must address accurate headers, truthful subjects, required identification and address information, functioning opt-outs, and timely suppression.",
        },
        {
            "title": "16 CFR Part 465 — Consumer Reviews and Testimonials",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465",
            "relevance": "Review and referral systems must avoid fake testimonials, prohibited sentiment-conditioned incentives, and other deceptive practices addressed by the rule.",
        },
    ],
}
