from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 2 FT + 2 C (4 people) specialty finance brokerage team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Event Pipelines, Evidence-Bound Lender Matching, SBA Fee Controls, Renewal Triggers, and Measured Distribution Economics",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #20, Specialty Finance Brokerage, ranks #14 among 29 mapped plays "
        "with a 79/100 Money-to-Manpower Score. Its automation advantage comes from "
        "turning application evidence, lender appetite, and renewal dates into "
        "versioned workflows rather than delegating credit judgment to a model. "
        "A 2 FT + 2 C team can target automation of 70%+ of repetitive task "
        "instances while retaining accountable review of lender submissions, fees, "
        "and borrower communications. Canonical annual owner profits remain "
        "$30,000 Conservative, $196,000 Base, and $450,000 Scaled; recognized revenue "
        "includes retained origination or referral fees, never loan principal. "
        "This chapter connects measured workflow economics to formation referrals "
        "and bankruptcy-claim research, separating adjacent-play receipts and "
        "principal risk from the brokerage scorecard."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained origination or referral fees; loan principal excluded",
            "note": "25% net margin; $30,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$560,000",
            "context": "Annual retained origination or referral fees; loan principal excluded",
            "note": "35.0% net margin; $196,000 annual owner net profit; 2 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual retained origination or referral fees; loan principal excluded",
            "note": "45% net margin; $450,000 annual owner net profit; 3 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Instrument the application pipeline before delegating repetitive work",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Give the four-person brokerage explicit ownership before connecting tools. "
                    "The first full-time operator owns borrower discovery, lender relationships, "
                    "and consequential communications; the second owns underwriting preparation, "
                    "file quality, and fee reconciliation. One contractor maintains integrations "
                    "and access controls, while the other verifies documents and handles overflow "
                    "research. Build a task ledger with application identifier, task type, source "
                    "document hash, workflow version, start time, completion time, reviewer, and "
                    "rework reason. Define the 70%+ target as repetitive task instances completed "
                    "without manual execution, not the percentage of lending decisions delegated. "
                    "An illustrative hundred-task cohort contains 24 intake checks, 20 extraction "
                    "tasks, 18 lender-screening calculations, 16 reminders, and 22 judgment tasks. "
                    "Automating the first 78 achieves 78% by task count only when retries and "
                    "manual rescues are recorded honestly. Human sampling remains separate quality "
                    "work and must appear in labor reporting. Also measure total minutes saved, "
                    "because automating twenty trivial reminders can conceal an unresolved "
                    "two-hour lien problem. Establish a two-week manual baseline, then compare "
                    "matched equipment, receivables, SBA, and bridge applications rather than "
                    "mixing simple renewals with distressed first-time borrowers. Report the "
                    "achieved rate only after exceptions have cleared."
                ),
                (
                    "Implement the workflow as durable events, not an elaborate sequence of "
                    "unrecoverable browser clicks. A portal upload creates application.received; "
                    "a Python handler validates required fields, checks an HMAC signature, rejects "
                    "expired timestamps, and stores the event before acknowledging delivery. "
                    "Use hashlib for content fingerprints, hmac.compare_digest for signature "
                    "comparison, decimal.Decimal for money, and zoneinfo for renewal calendars. "
                    "A managed queue and PostgreSQL event table can provide production durability; "
                    "a stdlib sqlite3 prototype is sufficient for an isolated pilot with "
                    "serialized writes. Every external action receives an idempotency key "
                    "combining application, action, and workflow version. Persist an outbox "
                    "record in the same transaction as the state change, then let a worker "
                    "deliver it and record the provider response. A replay may regenerate "
                    "an internal checklist but must never submit a second lender application "
                    "or send duplicate borrower demands. Encrypt source files in restricted "
                    "object storage, pass short-lived download links, and keep bank statements "
                    "out of ordinary CRM notes. Treat uploaded documents as untrusted data: "
                    "embedded instructions cannot change tool permissions, recipient lists, "
                    "or the evidence requirements imposed by the workflow."
                ),
                (
                    "Application checklists should depend on product, jurisdiction, entity type, "
                    "and lender requirements. Equipment files need vendor quotes, asset descriptions, "
                    "useful life, and applicable lien evidence; receivables files need aging, "
                    "customer concentration, dilution, and existing assignment restrictions. SBA "
                    "files require the selected lender's current program checklist, while bridge "
                    "files need collateral, maturity, repayment source, and verified exit assumptions. "
                    "OCR and an LLM may propose structured fields with document page references; "
                    "deterministic validators reconcile statement periods, totals, legal names, "
                    "and missing signatures. A model's confidence score does not establish "
                    "accuracy. Route mismatched totals, altered-looking statements, and conflicting "
                    "ownership records to a person without accusing the borrower automatically. "
                    "The security design follows applicable duties under 16 CFR Part 314, "
                    "including covered-institution risk assessment, access controls, service-provider "
                    "oversight, and incident procedures. Disable vendor training on borrower "
                    "documents where the service supports that setting, contract for appropriate "
                    "retention, and minimize transmitted fields. If extraction fails twice, "
                    "move the file to a manual queue with original evidence and error history. "
                    "A failed model call should delay one checklist, not expose documents "
                    "or corrupt the entire application's state."
                ),
            ],
            "table": {
                "caption": "Application Automation Ownership, Evidence, and Recovery Matrix",
                "headers": [
                    "Workflow boundary and named mechanism",
                    "Evidence required before automated completion",
                    "Accountable human review and permitted action",
                    "Failure recovery and operational measurement",
                ],
                "rows": [
                    [
                        "Portal intake validates signed webhooks before durable event acceptance",
                        "Application identifier, timestamp, signature, and payload hash remain linked",
                        "Operations lead reviews conflicting borrower identities before file consolidation",
                        "Reject invalid signatures and count retries without creating duplicate applications",
                    ],
                    [
                        "Python checklist rules select equipment documents by lender version",
                        "Vendor quote, asset description, borrower entity, and statement periods reconcile",
                        "File contractor verifies missing collateral details against original supplied documents",
                        "Create a manual exception task instead of inventing equipment attributes",
                    ],
                    [
                        "Receivables extraction reconciles aging totals against supporting financial statements",
                        "Customer balances, dilution history, and assignment restrictions retain source references",
                        "Underwriting operator investigates concentrated debtors before presenting financing options",
                        "Suspend automated matching when aging totals exceed documented reconciliation tolerance",
                    ],
                    [
                        "SBA preparation applies the selected lender's current application checklist",
                        "Eligibility representations and compensation documents retain dated borrower acknowledgments",
                        "Relationship operator confirms program fit and required fee reporting",
                        "Return incomplete packets internally without representing lender acceptance to borrowers",
                    ],
                    [
                        "Restricted object storage serves short-lived links to authorized workers",
                        "Access logs identify user, application, document, and legitimate processing purpose",
                        "Integration contractor tests least-privilege roles without downloading live borrower files",
                        "Revoke exposed links and follow the documented incident response procedure",
                    ],
                    [
                        "Task ledger separates automated execution from manual rescue and sampling",
                        "Start times, completion times, workflow versions, and rework reasons persist",
                        "Operations lead compares matched cohorts before publishing an automation percentage",
                        "Exclude failed attempts from completed automation and report total labor minutes",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make automation survive real borrower files",
                "body": (
                    "The most valuable automation preserves evidence, prevents repeated "
                    "requests, and keeps lender relationships from absorbing software mistakes."
                ),
                "items": [
                    "Fingerprint every uploaded statement so renamed duplicates do not trigger another extraction charge or another borrower request.",
                    "Keep lender exceptions separate from published appetite rules; a one-off equipment approval must not silently become universal policy.",
                    "Record payoff verification dates alongside renewal dates because stale payoff figures can invalidate an otherwise complete refinance packet.",
                    "Use synthetic borrower packets for replay tests, including debtor concentration spikes, mismatched entity names, and duplicate webhook deliveries.",
                ],
            },
        },
        {
            "heading": "2. Bind lender matching and renewal automation to verified evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build lender matching as a transparent constraint engine before adding "
                    "language generation. Each lender record needs product coverage, permitted "
                    "states, minimum operating history, ticket range, collateral requirements, "
                    "industry exclusions, concentration tolerance, current contact, evidence "
                    "source, and last verification date. Represent a rule as data with "
                    "effective dates and a named owner. Python evaluates hard exclusions "
                    "first, then calculates a documented fit score from eligible attributes. "
                    "An LLM can explain why a lender appears suitable, but it cannot "
                    "override an exclusion or manufacture an appetite update. Set different "
                    "freshness windows for stable documentation rules and volatile bridge "
                    "pricing; expired records require confirmation before a borrower receives "
                    "a lender-specific representation. Rank options using borrower fit and "
                    "execution evidence, not simply the highest commission. Preserve the "
                    "alternatives considered, rejection reasons, and compensation arrangements "
                    "so the operator can explain the recommendation. Under 12 CFR 1002.2(l), "
                    "some referral participants fall within creditor coverage for specified "
                    "Regulation B provisions; determine the firm's actual activities rather "
                    "than assuming every broker has identical duties. Do not use protected "
                    "characteristics or unsupported demographic proxies to improve conversion "
                    "scores or shape who receives financing outreach."
                ),
                (
                    "Keep the model behind a narrow output contract: proposed document "
                    "requests, cited lender matches, and draft explanations only. Validate "
                    "JSON keys, types, enumerated products, and citations against records "
                    "already retrieved by the application. If an output cites a nonexistent "
                    "page or lender policy, reject it rather than asking another model "
                    "to certify its plausibility. The relationship operator reviews every "
                    "external lender submission, borrower-specific financing recommendation, "
                    "and fee representation. Where an adverse-action duty applies, the "
                    "responsible creditor must provide accurate reasons under 12 CFR 1002.9; "
                    "a generic model explanation is insufficient. Business-credit notice "
                    "procedures differ by circumstances, so record which entity owns each "
                    "required notice and retain supporting facts. For SBA transactions, "
                    "check agent compensation requirements under 13 CFR 103.5 and the "
                    "applicable SBA Form 159 instructions before representing fees. Check "
                    "state licensing and disclosure scope separately: California Financial "
                    "Code sections 22100 and 22800 address different activities and "
                    "requirements. Document the applicability analysis rather than treating "
                    "one national checklist as universal. A stopped application remains "
                    "visible to its owner, with a specific unresolved issue and next "
                    "contact date, instead of disappearing into a rejected-model queue."
                ),
                (
                    "Renewal tracking begins at funding, when the team records contractual "
                    "maturity, draw availability, reporting covenants, prepayment terms, "
                    "equipment schedules, and the borrower's permitted contact channels. "
                    "Generate internal preparation tasks at 120, 90, and 60 days before "
                    "maturity, adjusting timing to the actual product rather than assuming "
                    "every facility renews annually. Reconfirm balances and business "
                    "conditions before soliciting a refinance. The recurring workflow "
                    "collects fresh statements, compares utilization and receivables aging, "
                    "and identifies material changes for human review. Never infer that "
                    "a past approval remains valid after a customer concentration spike "
                    "or ownership change. Adopt a state machine with received, validated, "
                    "review_required, submission_ready, submitted, funded, and closed "
                    "states; separate terminal outcomes from temporary processing errors. "
                    "Retry transient network failures with bounded exponential backoff "
                    "and jitter, but send permission failures directly to the integration "
                    "owner. A nightly reconciliation compares the CRM, event ledger, "
                    "and lender acknowledgments to detect missing or duplicated transitions. "
                    "During a vendor outage, export the minimum authorized task list "
                    "for manual processing, preserve action identifiers, and reconcile "
                    "those actions before restarting automation. Recovery must restore "
                    "one coherent file history, not create competing versions of the deal."
                ),
            ],
            "table": {
                "caption": "Lender-Matrix Underwriting and Renewal Decision Boundaries",
                "headers": [
                    "Product or consequential decision boundary",
                    "Deterministic screen and supporting evidence",
                    "Human decision that remains explicitly assigned",
                    "Stop condition and practical recovery route",
                ],
                "rows": [
                    [
                        "Equipment placement requires confirmed asset eligibility and vendor identity",
                        "Compare ticket size, asset age, geography, and documented lender exclusions",
                        "Relationship operator evaluates collateral issues and approves the proposed lender packet",
                        "Request corrected vendor evidence when serial numbers or ownership records conflict",
                    ],
                    [
                        "Receivables placement requires documented debtor concentration and dilution analysis",
                        "Calculate aging buckets and largest debtor shares from reconciled source balances",
                        "Underwriting operator reviews disputed invoices and existing receivables assignments",
                        "Remove unsupported invoices and rerun borrowing-base estimates with visible exclusions",
                    ],
                    [
                        "SBA matching requires current program fit and agent compensation controls",
                        "Apply lender checklist versions and link applicable compensation documentation",
                        "Relationship operator verifies representations before submitting the complete application packet",
                        "Hold fee communications until required documentation and responsible parties are identified",
                    ],
                    [
                        "Bridge debt matching requires credible repayment sources and current terms",
                        "Check maturity, collateral evidence, exit assumptions, and lender verification dates",
                        "Senior operator challenges optimistic refinance assumptions before recommending borrower action",
                        "Refresh stale terms directly with the lender rather than extrapolating old quotes",
                    ],
                    [
                        "Borrower-specific recommendations require evidence-bound explanations and recorded alternatives",
                        "Validate cited records and exclude prohibited attributes from ranking inputs",
                        "Accountable operator reviews fit, compensation, and the exact external message",
                        "Reject unsupported model explanations and prepare a documented manual recommendation",
                    ],
                    [
                        "Renewal preparation requires current balances and changed-condition review",
                        "Schedule product-specific tasks from verified contractual dates and contact permissions",
                        "File owner confirms borrower circumstances before initiating new lender outreach",
                        "Pause outreach after material changes and rebuild the application evidence package",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four boundaries before any consequential release",
                "body": (
                    "Automated preparation may continue internally; external submissions "
                    "and borrower-specific recommendations require an accountable reviewer."
                ),
                "items": [
                    "Confirm borrower authorization, recipient identity, and the exact document set before transmitting any lender packet.",
                    "Verify lender appetite freshness, hard-rule eligibility, and source-backed calculations before presenting a match.",
                    "Confirm applicable licensing, commercial-financing disclosures, and SBA compensation documentation before representing fees or terms.",
                    "Check idempotency records, open exceptions, and the prior submission receipt before releasing a retry or renewal message.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Validate and preserve the intake event",
                    "action": "Authenticate the webhook, store its hash, and acknowledge only after durable acceptance.",
                    "detail": "Attach the application identifier and workflow version; route conflicting identities to the file owner.",
                },
                {
                    "step": 2,
                    "title": "Prepare evidence-bound checklist and matches",
                    "action": "Extract cited fields, reconcile totals, and run versioned lender constraints.",
                    "detail": "Reject unsupported fields and create explicit exception tasks instead of silently filling missing evidence.",
                },
                {
                    "step": 3,
                    "title": "Review and release the authorized packet",
                    "action": "Have the assigned operator inspect terms, recipients, fee statements, and unresolved issues.",
                    "detail": "Persist the reviewed payload and an outbox action identifier before the delivery worker submits anything.",
                },
                {
                    "step": 4,
                    "title": "Reconcile delivery and schedule follow-through",
                    "action": "Record lender acknowledgment, update application state, and assign follow-up or renewal tasks.",
                    "detail": "Compare external receipts with internal actions nightly and reconcile manual work before replaying failed events.",
                },
            ],
        },
        {
            "heading": "3. Build distribution loops without confusing adjacent plays with brokerage revenue",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Programmatic distribution should answer specific financing questions with "
                    "reviewed tools, not mass-produce thin location pages. Publish an equipment "
                    "payment calculator, an invoice-aging readiness worksheet, and a maturity "
                    "planning checklist, each using disclosed assumptions and a versioned "
                    "calculation method. Let accountants and equipment vendors share a "
                    "co-branded worksheet that returns a useful borrower action list before "
                    "requesting a meeting. Attribute each referral with a partner identifier "
                    "and preserve borrower permission before sharing application data. The "
                    "viral mechanism is practical utility: an accountant forwards a "
                    "reusable worksheet to another client, who can share an empty copy "
                    "without exposing the first client's balances. For outbound, use "
                    "lawfully obtained business contacts and truthful role-specific messages; "
                    "apply commercial-email requirements under 15 U.S.C. 7704, including "
                    "accurate headers and functioning opt-outs. Maintain suppression centrally "
                    "so contractors cannot reintroduce removed contacts. An illustrative "
                    "monthly funnel of 2,000 qualified visits produces 80 checklist "
                    "starts at 4%, 24 completed intakes at 30%, eight lender-ready files "
                    "at one-third, and two closings at 25%. Those are test assumptions, "
                    "not the canonical annual scorecard. Track acquisition cost per "
                    "funded, retained-fee deal after reversals, not per email reply."
                ),
                (
                    "The mapped play free_llc_fintech_bounty_stacking offers a $0-service-fee "
                    "formation and business-launch concierge, with the founder paying mandatory "
                    "state filing fees. Its sequential post-formation 'Required Business "
                    "Infrastructure Checklist' covers banking, corporate cards, payroll, "
                    "bookkeeping, and merchant services, but distinguish actual operating "
                    "requirements from optional sponsored products. Do not require all "
                    "founders to open every account or condition financing access on "
                    "affiliate enrollment. Collect separate authorization for each application, "
                    "confirm provider eligibility, and disclose material referral relationships "
                    "clearly. Illustrative qualified payouts of $150 for banking, $250 "
                    "for cards, $200 for payroll, $100 for bookkeeping, and $200 for "
                    "merchant services total $900; the mapped $600–$1,800+ range depends "
                    "on live contracts, activation, retention, and reversal terms. Forty "
                    "formations at $900 yield $36,000 only if every modeled payout "
                    "qualifies. Applying a 70% realization assumption gives $25,200; "
                    "subtracting $6,000 fulfillment and a $2,520 reversal allowance "
                    "leaves $16,680 before other acquisition and overhead costs. Keep "
                    "this adjacent-play ledger outside the brokerage scenarios. Pre-qualify "
                    "founders for genuine 30-day operating revenue intent. Where lawful "
                    "and clearly disclosed, release optional free operating-agreement "
                    "and bookkeeping templates after verified bank funding, using provider "
                    "confirmation rather than collecting bank credentials."
                ),
                (
                    "The second mapped play, chapter11_trade_claim_convenience_class_rollup, "
                    "uses public bankruptcy records to identify documented small trade "
                    "claims offered below risk-adjusted expected distributions. PACER "
                    "Schedule E/F research is a lead source, not proof that a claim "
                    "is allowed or transferable on favorable terms. Reconcile the "
                    "schedule with invoices, proofs of claim, objections, debtor identity, "
                    "and the confirmed or proposed plan. For an illustrative $10,000 "
                    "claim, an 80% probability of a 30% distribution and zero otherwise "
                    "produces $2,400 expected gross recovery. Deduct $300 servicing "
                    "and a $600 risk cushion to establish a $1,500 maximum purchase "
                    "price. At a 10% distribution with the same probability and "
                    "servicing assumption, expected net recovery falls to $500, "
                    "creating a $1,000 expected loss against that purchase price. "
                    "Review transfer procedures under Bankruptcy Rule 3001(e), any "
                    "court-specific requirements, and plan treatment under 11 U.S.C. "
                    "1122(b). Never assume splitting or aggregating claims creates "
                    "convenience-class eligibility. Stop affected purchases when objections "
                    "or plan restrictions undermine the thesis, enforce documented "
                    "seller recourse where available, and price only supported "
                    "general-unsecured recoveries. Claims purchased with capital belong "
                    "in a separate investment ledger; neither purchase principal "
                    "nor distributions become brokerage origination revenue."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheel and Mapped-Play Economics With Explicit Risk Fallbacks",
                "headers": [
                    "Distribution asset or mapped operator play",
                    "Illustrative unit economics and measurement basis",
                    "Required evidence and accountable operating boundary",
                    "Failure mode and concrete fallback response",
                ],
                "rows": [
                    [
                        "Equipment calculators attract borrowers through specific asset-financing questions",
                        "Two thousand visits at four percent generate eighty checklist starts",
                        "Reviewed formulas disclose assumptions without presenting indicative outputs as lender offers",
                        "Correct inaccurate assumptions and pause affected pages before purchasing additional traffic",
                    ],
                    [
                        "Accountant worksheets create repeat referrals through reusable practical utility",
                        "Twenty-four completed intakes yield eight lender-ready files under modeled qualification",
                        "Partner identifiers preserve attribution while borrower permission controls document sharing",
                        "Replace low-quality sources with partners whose submissions survive documented qualification checks",
                    ],
                    [
                        "Targeted business email distributes reviewed readiness tools to relevant operators",
                        "Eight lender-ready files at twenty-five percent produce two modeled closings",
                        "Central suppression and accurate message headers support commercial-email operating requirements",
                        "Stop suppressed-address outreach and investigate contractors who reintroduce removed contacts",
                    ],
                    [
                        "free_llc_fintech_bounty_stacking sequences formation assistance and optional product referrals",
                        "Five illustrative qualified payouts total nine hundred dollars per fully activated formation",
                        "Provider contracts determine qualification, activation, reversals, and permitted referral representations",
                        "Pre-qualify operating intent and condition optional template bonuses only on disclosed lawful terms",
                    ],
                    [
                        "Formation bounty realization requires separate receipts and reversal accounting",
                        "Forty formations at seventy percent realization generate twenty-five thousand two hundred dollars",
                        "Separate ledgers exclude these adjacent receipts from canonical brokerage fee scenarios",
                        "Suspend weak providers and revise payout assumptions when activation or retention deteriorates",
                    ],
                    [
                        "chapter11_trade_claim_convenience_class_rollup prices documented claims against supported plan recoveries",
                        "Twenty-four hundred expected recovery supports fifteen hundred purchase after stated deductions",
                        "Invoices, objections, transfer procedures, and plan classification receive transaction-specific review",
                        "Stop affected purchases, enforce available seller recourse, and price supported unsecured recoveries",
                    ],
                ],
            },
        },
        {
            "heading": "4. Price each automated run and scale only the reconciled operating system",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price automation at the application level, including failed attempts "
                    "and human review. An illustrative run costs $0.18 for extraction, "
                    "$0.12 for model processing, $0.04 for queue and storage allocation, "
                    "and $0.06 for messaging and observability: $0.40 total machine "
                    "cost. These are budgeting assumptions rather than vendor quotations. "
                    "Six reviewer minutes at a $60 hourly loaded rate add $6, "
                    "making the standard reviewed run $6.40. Against thirty manual "
                    "minutes at the same rate, the modeled saving is $23.60 "
                    "before development, maintenance, and exception work. If 15% of "
                    "applications need eighteen additional review minutes, expected "
                    "exception labor adds $2.70 per run, producing $9.10 total "
                    "and $20.90 savings. At 400 monthly runs, machine expense "
                    "is $160, standard review is $2,400, and expected exception "
                    "labor is $1,080, totaling $3,640. Add $2,000 monthly integration "
                    "maintenance to reach $5,640 versus $12,000 manual processing. "
                    "These savings demonstrate a capacity hypothesis, not additional "
                    "profit to stack onto the scorecard. Compare this workload "
                    "with actual staffing availability, record opportunity costs, "
                    "and replace estimates with invoices and observed handling "
                    "times before increasing acquisition spend."
                ),
                (
                    "Reconcile every commercial dashboard to the canonical fee-only cases. "
                    "Conservative revenue of $120,000 at a 25% net margin produces "
                    "$30,000 annual owner net profit and implies $90,000 total "
                    "annual expenses with 2 FT + 2 C. Base revenue of "
                    "$560,000 at 35.0% produces $196,000 profit and $364,000 "
                    "expenses with the same team. Scaled revenue of $1,000,000 "
                    "at 45% produces $450,000 profit and $550,000 expenses "
                    "with 3 FT + 3 C. Illustrative bridges are twelve "
                    "retained-fee closings at $10,000, forty at $14,000, and "
                    "fifty at $20,000 respectively; actual fee mixes may differ. "
                    "Loan principal never enters these revenue equations. The "
                    "stated $4,000–$18,000 monthly operating range does not reconcile "
                    "by itself to all modeled total expenses; retain the "
                    "annual expense envelopes and document additional variable, "
                    "compensation, acquisition, and other included costs. Likewise, "
                    "the Conservative envelope may not support market-rate cash "
                    "compensation for every listed person. Specify contractor "
                    "utilization, owner compensation treatment, and cash runway "
                    "before adopting the case operationally. The $20,000–$100,000 "
                    "startup capital range must also cover a potential "
                    "three-to-nine-month wait for the first deal rather "
                    "than assuming immediate closing revenue."
                ),
                (
                    "Build a weekly control meeting around four numbers: cost per "
                    "reviewed application, funded conversion, retained fee after "
                    "clawbacks, and lender concentration. A lender producing 45% "
                    "of retained fees deserves a documented contingency even "
                    "when its close rate looks excellent. Use an internal "
                    "concentration trigger, such as 35%, to require alternate "
                    "coverage research rather than automatically steering borrowers "
                    "toward inferior offers. Track failed closings by cause: "
                    "unsupported borrower facts, stale appetite, valuation gaps, "
                    "timing failures, or lender withdrawal. Reconcile commission "
                    "receipts against agreements and contractual clawback windows; "
                    "keep reversal exposure visible and avoid distributing cash "
                    "needed for foreseeable repayment obligations. Promote a "
                    "workflow only after a replay set passes, a supervised "
                    "pilot shows acceptable error rates, and the file owner "
                    "can operate its manual fallback. Pause consequential "
                    "releases after any unauthorized submission or material "
                    "borrower-data exposure, investigate scope, and restore "
                    "service through controlled replay. At scale, the "
                    "additional full-time operator owns quality and portfolio "
                    "follow-through, while the third contractor supports "
                    "verified sourcing or integration coverage. More traffic "
                    "is useful only when lender capacity, reviewer capacity, "
                    "and retained-fee economics expand together. Automate "
                    "repetition aggressively while keeping judgment, evidence, "
                    "and recovery ownership unmistakably human."
                ),
            ],
            "table": {
                "caption": "Run-Level Costs, Canonical Scenario Reconciliation, and Scaling Controls",
                "headers": [
                    "Operating measurement or canonical scenario",
                    "Explicit arithmetic and recognized revenue basis",
                    "Capacity interpretation and responsible operating owner",
                    "Risk control and reconciliation evidence required",
                ],
                "rows": [
                    [
                        "Standard automated run includes machines and mandatory human review",
                        "Forty cents machine cost plus six dollars review equals six dollars forty",
                        "Six minutes of reviewer time remains scheduled for each standard application",
                        "Compare provider invoices and reviewer timers against the assumed cost allocation",
                    ],
                    [
                        "Exception-adjusted run includes additional review on fifteen percent of files",
                        "Six dollars forty plus two dollars seventy equals nine dollars ten",
                        "Underwriting operator budgets eighteen extra minutes for each modeled exception",
                        "Record exception causes and rebuild estimates when difficult files cluster together",
                    ],
                    [
                        "Conservative canonical case retains two employees and two contractors",
                        "One hundred twenty thousand fee revenue less ninety thousand expenses yields thirty thousand",
                        "Twenty-five percent net margin requires explicit owner compensation and contractor utilization assumptions",
                        "Exclude loan principal and reconcile each retained fee to its closing agreement",
                    ],
                    [
                        "Base canonical case retains two employees and two contractors",
                        "Five hundred sixty thousand revenue less three hundred sixty-four thousand expenses yields one hundred ninety-six thousand",
                        "Thirty-five percent net margin requires measured acquisition and processing capacity",
                        "Keep adjacent formation receipts and claim investment returns outside this fee ledger",
                    ],
                    [
                        "Scaled canonical case uses three employees and three contractors",
                        "One million revenue less five hundred fifty thousand expenses yields four hundred fifty thousand",
                        "Forty-five percent net margin requires quality ownership and diversified lender coverage",
                        "Reconcile variable costs and compensation rather than relying solely on monthly overhead ranges",
                    ],
                    [
                        "Weekly concentration and clawback review protects retained-fee cash quality",
                        "Internal thirty-five percent lender concentration trigger initiates documented alternate coverage research",
                        "Relationship operator preserves borrower fit while developing credible execution alternatives",
                        "Match receipts, reversal windows, and contingent repayment exposure before owner cash distributions",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the repeated work, preserve the evidence, and keep every consequential decision attached to a named human.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Instrument a two-week manual baseline and calculate automation by completed repetitive task instances, manual rescues, review time, and total handling minutes.",
        "Implement authenticated intake, durable event storage, transactional outbox delivery, idempotency keys, bounded retries, and a documented manual recovery path.",
        "Version equipment, receivables, SBA, and bridge lender rules; require cited evidence and accountable review before submissions or borrower-specific recommendations.",
        "Launch one reviewed calculator and one accountant referral worksheet, then measure funded retained-fee acquisition cost after failed closings and commission reversals.",
        "Maintain separate ledgers for formation bounties and purchased claims, validating provider eligibility, optional-product disclosures, plan treatment, and seller recourse.",
        "Reconcile $120,000, $560,000, and $1,000,000 fee-only revenue cases to their exact expense envelopes before expanding reviewer staffing or traffic spend.",
    ],
    "statutory_citations": [
        {
            "title": "16 CFR Part 314 — Standards for Safeguarding Customer Information",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314",
            "relevance": (
                "Determine covered-institution status and implement applicable information-security "
                "program, risk assessment, access-control, service-provider, and incident requirements."
            ),
        },
        {
            "title": "12 CFR 1002.2 — Regulation B Definitions",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.2",
            "relevance": (
                "Paragraph (l) addresses creditor coverage, including specified treatment "
                "of parties regularly referring applicants or selecting creditors."
            ),
        },
        {
            "title": "12 CFR 1002.4 — General Rules Under Regulation B",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.4",
            "relevance": (
                "Apply relevant restrictions on discrimination and discouragement when "
                "designing qualification logic, lender routing, and borrower communications."
            ),
        },
        {
            "title": "12 CFR 1002.9 — Notifications",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1002/section-1002.9",
            "relevance": (
                "Assign applicable creditor notification responsibilities and preserve "
                "accurate reasons, accounting for the provisions governing business credit."
            ),
        },
        {
            "title": "13 CFR 103.5 — Compensation Agreement Requirements",
            "url": "https://www.ecfr.gov/current/title-13/chapter-I/part-103/section-103.5",
            "relevance": (
                "Check SBA agent compensation agreement requirements and applicable "
                "reporting instructions before communicating or collecting transaction fees."
            ),
        },
        {
            "title": "California Financial Code Section 22100 — Finance Lender and Broker Licensing",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22100.",
            "relevance": (
                "Evaluate licensing requirements and applicable exceptions against the "
                "brokerage's actual California lending and brokering activities."
            ),
        },
        {
            "title": "California Financial Code Section 22800 — Commercial Financing Disclosures",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22800.",
            "relevance": (
                "Determine whether covered commercial-financing offers require disclosures "
                "and ensure automation uses the applicable statutory scope."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for Commercial Electronic Mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Design outbound messaging around accurate transmission information, "
                "required identification, functioning opt-outs, and suppression handling."
            ),
        },
        {
            "title": "16 CFR 255.5 — Disclosure of Material Connections",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": (
                "The FTC endorsement guides explain disclosure of material connections "
                "relevant to sponsored fintech recommendations and referral promotions."
            ),
        },
        {
            "title": "11 U.S.C. 1122(b) — Classification of Small Unsecured Claims",
            "url": "https://www.law.cornell.edu/uscode/text/11/1122",
            "relevance": (
                "Evaluate convenience-class treatment under the actual plan without "
                "assuming purchased, split, or aggregated claims qualify for favorable treatment."
            ),
        },
        {
            "title": "Federal Rule of Bankruptcy Procedure 3001(e) — Transferred Claims",
            "url": "https://www.law.cornell.edu/rules/frbp/rule_3001",
            "relevance": (
                "Identify applicable claim-transfer evidence, notice, and objection "
                "procedures before purchasing or attempting to enforce transferred trade claims."
            ),
        },
    ],
}
