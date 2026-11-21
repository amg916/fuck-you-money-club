from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-day-launch-sprint-kill-fix-scale",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching unclaimed property recovery, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "A Three-Person Treasury-Claim Sprint: Finder Restrictions, Corporate Warrant Evidence, Controlled Cash Burn, and Cohort-Based Expansion",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #07 with an "
        "85/100 Money-to-Manpower Score. This sprint operationalizes its 12 mapped "
        "plays through a one-full-time, two-contractor pod, concentrating on "
        "state-treasury property, corporate uncashed warrants, and lawful finder-fee "
        "engagements. Days 1–30 establish jurisdiction rules, audit identity matches, "
        "test transparent outreach, and submit evidence-complete claims. Day 30/60/90 "
        "decisions use explicit denominators, filing defects, acquisition costs, and "
        "cash reserves rather than premature collection promises. Canonical annual "
        "owner profits are $15,000 Conservative, $95,625 Base, and $225,000 Scaled; "
        "recognized service fees, never recovered client principal, fund those "
        "outcomes. With first deals typically taking 3–12 months, the initial "
        "success condition is a defensible operating system and qualified cohort, "
        "not an artificial first-month revenue target."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "25% net margin; $15,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "37.5% net margin; $95,625 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees; client property excluded",
            "note": "50% net margin; $225,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Bound the Jurisdiction, Assign the Pod, and Protect the Runway",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one state, one property class, and one claimant "
                    "type: existing corporations seeking cash already held by a "
                    "state treasury. Corporate uncashed warrants still payable "
                    "by an issuing agency belong in a separate workflow until "
                    "custody and the applicable recovery rules are established. "
                    "The supplied mapping count is twelve; the following are "
                    "sprint workstream labels, not asserted source-taxonomy names. "
                    "P01 covers treasury inventory; P02 covers issuer-held warrants; "
                    "P03 covers corporate claimant authority; P04 covers historical "
                    "address evidence; P05 covers identity matching; P06 covers "
                    "finder eligibility and fee rules; P07 covers owner outreach; "
                    "P08 covers engagement execution; P09 covers evidence assembly; "
                    "P10 covers claim submission; P11 covers status tracking; and "
                    "P12 covers fee collection and reconciliation. Assign every "
                    "record one primary play and explicit supporting plays. The "
                    "full-time founder owns P06–P08 and P12, the research contractor "
                    "owns P01–P05, and the claims contractor owns P09–P11. The "
                    "founder retains final identity and submission decisions. "
                    "Contractors receive narrow case access rather than a complete "
                    "customer export. This partition makes all twelve plays "
                    "observable without pretending a three-person pod can launch "
                    "twelve markets simultaneously. Freeze additional jurisdictions "
                    "until the first cohort clears its documented review."
                ),
                (
                    "On Days 1 and 2, build a rules register from the treasury's "
                    "official claim instructions and current statutes. California "
                    "Code of Civil Procedure §1582 addresses recovery agreements, "
                    "including restricted contracting periods and a ten-percent "
                    "compensation ceiling; Texas Property Code §74.507 separately "
                    "governs recovery-assistance agreements and its own restrictions. "
                    "Do not transplant one state's contract into another. Record "
                    "the controlling section, retrieval date, restricted-period "
                    "trigger, permitted fee calculation, required agreement terms, "
                    "and any applicable registration requirement. Treat a missing "
                    "custody date as a blocked engagement, not permission to infer "
                    "that a waiting period expired. Ask the treasury to clarify "
                    "ambiguous procedures without transmitting unnecessary identity "
                    "documents. On Day 3, configure a case register in Airtable or "
                    "a local SQLite database and a separately permissioned document "
                    "repository in Google Workspace. Store treasury identifiers, "
                    "evidence references, and status events in the register; keep "
                    "tax identifiers and document images out of outreach exports. "
                    "Enable multifactor authentication, individual accounts, access "
                    "logging, and encrypted backups. Document retention and deletion "
                    "rules for rejected prospects before importing records. By "
                    "Day 4, a second person must reproduce five property-to-owner "
                    "matches from the saved evidence alone."
                ),
                (
                    "Set the first-month cash-burn ceiling at $3,500: $1,500 for "
                    "formation and jurisdiction-specific contract review, $750 for "
                    "secure systems and records, $1,000 for contractors, and $250 "
                    "for outreach. At an illustrative $50 hourly rate, the "
                    "contractor allowance buys twenty combined hours, not twenty "
                    "hours each. The founder supplies the remaining operating "
                    "capacity without a first-month draw; personal living expenses "
                    "require a separate reserve. Budget $2,500 for each of Months "
                    "2 and 3, making the ninety-day ceiling $8,500. A $32,500 "
                    "starting balance leaves $24,000 after that ceiling and funds "
                    "another nine months at $2,500 with $1,500 remaining. This "
                    "fits the canonical $5,000–$35,000 startup range while "
                    "acknowledging the 3–12-month first-deal interval. A $5,000 "
                    "launch cannot support the same schedule without reduced "
                    "spending or additional committed funds. Log commitments when "
                    "ordered, not only when invoices clear. On Days 5–7, approve "
                    "one agreement, one direct-claim disclosure, one evidence "
                    "checklist, and the first twenty-record audit. No acquisition "
                    "spending expands while the remaining runway falls below "
                    "six months of the current maintenance budget. The "
                    "$1,500–$8,000 monthly operating range describes planning "
                    "capacity, not permission to exhaust available cash."
                ),
            ],
            "table": {
                "caption": "Week One Daily Deliverables Across the Twelve-Play Operating Map",
                "headers": [
                    "Day and accountable operator",
                    "Execution across mapped operating plays",
                    "Required artifact before work advances",
                    "Quantitative control and failure response",
                ],
                "rows": [
                    [
                        "Day 1: founder defines the initial jurisdiction boundary",
                        "P01 and P06 separate treasury custody from issuer custody",
                        "One state, property class, claimant type, and rules register",
                        "Reject additional markets until this boundary has documented ownership",
                    ],
                    [
                        "Day 2: founder validates contract restrictions with retained reviewer",
                        "P06 and P08 translate statutes into executable engagement requirements",
                        "Dated fee, waiting-period, registration, and agreement requirements with citations",
                        "Block every engagement missing a verified eligibility trigger date",
                    ],
                    [
                        "Day 3: founder provisions restricted systems for both contractors",
                        "P05 and P11 establish evidence references and status history",
                        "Individual accounts, encrypted repository, backup procedure, and access register",
                        "Require multifactor authentication for every account holding claimant evidence",
                    ],
                    [
                        "Day 4: research contractor prepares five independently reviewable matches",
                        "P03 through P05 connect corporate authority and historical addresses",
                        "Five evidence chains linking property identifiers to specific corporations",
                        "Second reviewer reproduces all five matches before broader importing",
                    ],
                    [
                        "Day 5: founder finalizes transparent owner communications and agreements",
                        "P07 and P08 explain direct claiming and priced assistance",
                        "Approved letter, call script, engagement agreement, and disclosure record",
                        "Every template states owners may claim directly without assistance",
                    ],
                    [
                        "Day 6: claims contractor builds the first evidence checklist",
                        "P09 and P10 distinguish required documents from optional research",
                        "Treasury-specific checklist with submission method and document custody rules",
                        "Zero submissions proceed with unverified signing authority or identities",
                    ],
                    [
                        "Day 7: founder audits records and confirms remaining runway",
                        "P01 through P12 receive owners, statuses, and measurable outputs",
                        "Twenty-record audit, committed-spend ledger, and written week-two priorities",
                        "Release outreach only after at least nineteen correct audit matches",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Checks Before Contacting an Owner",
                "body": (
                    "An attractive property amount does not override an unresolved "
                    "identity, custody, contracting, or cash-control defect."
                ),
                "items": [
                    (
                        "Verify the property's present custodian and identifier; "
                        "do not describe an issuer-held warrant as treasury-held property."
                    ),
                    (
                        "Document the applicable fee ceiling, restricted contracting "
                        "period, agreement requirements, and registration position "
                        "before offering paid recovery."
                    ),
                    (
                        "Require two independent identity links, verified corporate "
                        "authority, and a second-person review of ambiguous matches."
                    ),
                    (
                        "Confirm the $3,500 first-month ceiling, six-month maintenance "
                        "reserve, direct-claim disclosure, and restricted document access."
                    ),
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Build a Measurable Cohort and Earn Permission to Proceed",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Days 8–10 turn the initial sample into a hundred-record "
                    "research cohort. Count unique property-owner pairs, not search "
                    "results, duplicate treasury pages, or multiple contacts at "
                    "the same corporation. Preserve the source URL, retrieval "
                    "date, displayed amount category, holder name, and property "
                    "identifier. A treasury's amount band is not a verified "
                    "recoverable balance. Use record matching to propose candidates, "
                    "then validate names against Secretary of State records and "
                    "addresses against dated business documents. A shared name "
                    "alone never establishes ownership. For mergers, require a "
                    "documented chain from the named owner to the current entity; "
                    "for dissolved corporations, determine who can lawfully act "
                    "before offering assistance. Keep issuer-held warrants in a "
                    "separate queue with the issuer's replacement or reissuance "
                    "procedure. Target sixty records with sufficient identity, "
                    "authority, timing, and estimated fee evidence to support "
                    "contact. That is a workload target, not a reason to relax "
                    "eligibility. Independently sample twenty matches and require "
                    "nineteen correct results before outreach. Also review every "
                    "high-value or ambiguous match. The small audit supports a "
                    "controlled pilot; it does not establish a precise population "
                    "error rate or authorize unattended claims."
                ),
                (
                    "On Days 11–14, contact the first twenty eligible owners "
                    "through individualized business letters or manually placed "
                    "calls, then expand toward forty by Day 21. Each message "
                    "identifies the recovery business, describes the property "
                    "without exposing sensitive identifiers, states that the owner "
                    "can claim directly through the treasury without hiring the "
                    "service, and explains the proposed fee basis. Never imply "
                    "government affiliation, exclusive access, or a deadline "
                    "unsupported by the custodian. Give the owner the official "
                    "treasury website and an independently verifiable callback "
                    "route. For commercial email, apply 15 U.S.C. §7704 requirements "
                    "where applicable, including accurate routing information, "
                    "required identification, postal address, and effective opt-out "
                    "handling. Do not introduce automated calls or texts without "
                    "evaluating 47 CFR §64.1200 and applicable state requirements. "
                    "Record delivered contacts, replies, two-way discussions, "
                    "declines, and signed engagements separately. An unanswered "
                    "message is not a conversation, and a returned envelope is "
                    "not a delivered contact. Cap this pilot at two unanswered "
                    "contact attempts per owner and suppress further outreach "
                    "immediately after an objection. Customer distrust is measured "
                    "through stated concerns, not dismissed as a sales objection."
                ),
                (
                    "Use the first ten two-way discussions to test whether the "
                    "service solves a real administrative burden. Ask who controls "
                    "historical records, whether the corporation has already filed, "
                    "and which employee can authorize representation. Offer document "
                    "assembly and status tracking rather than selling public search "
                    "results as proprietary discoveries. A qualified mandate requires "
                    "a valid agreement, a verified signer, lawful timing, a "
                    "defensible ownership chain, and a fee estimate supported by "
                    "available information. Exclude speculative amount bands from "
                    "the mandate fee total until better evidence arrives. Model "
                    "a $30,000 recovery at a lawful ten-percent fee as $3,000 "
                    "of potential service revenue, not $30,000 of revenue. The "
                    "illustration is usable only where that fee and agreement "
                    "are permitted. Reserve $1,000 per eventual collected recovery "
                    "for direct acquisition and handling, including allocated "
                    "effort on unsuccessful files: $350 acquisition and $650 "
                    "delivery. Those are underwriting assumptions to replace with "
                    "cohort costs, not measured launch results. At a verified "
                    "$10,000 recovery, the same fee produces only $1,000 and "
                    "cannot carry that cost structure. Route such cases to "
                    "direct claiming or redesign the workflow before accepting "
                    "them. Do not hide weak unit economics behind a large "
                    "aggregate property balance."
                ),
            ],
            "table": {
                "caption": "Week Two Research, Owner Verification, and Transparent Outreach Schedule",
                "headers": [
                    "Day and measurable work package",
                    "Mapped plays and specific execution",
                    "Evidence retained in the case register",
                    "Decision rule protecting the pilot cohort",
                ],
                "rows": [
                    [
                        "Day 8: research contractor deduplicates the hundred-record candidate cohort",
                        "P01 and P02 distinguish treasury records from issuer obligations",
                        "Source links, retrieval dates, property identifiers, and custody classifications",
                        "One property-owner pair counts once regardless of repeated search appearances",
                    ],
                    [
                        "Day 9: research contractor assembles corporate ownership evidence chains",
                        "P03 and P04 connect legal entities with historical addresses",
                        "Registry extracts, dated address evidence, and merger documents where applicable",
                        "Exclude unsupported successor claims until documentary continuity is established",
                    ],
                    [
                        "Day 10: founder audits twenty independently selected identity matches",
                        "P05 and P06 test identity precision and contracting eligibility",
                        "Audit worksheet recording correct matches, errors, and restriction dates",
                        "Require nineteen correct matches and resolve every discovered material error",
                    ],
                    [
                        "Day 11: founder contacts the first ten eligible owners",
                        "P07 uses transparent letters or individualized manual business calls",
                        "Contact copy, delivery status, direct-claim disclosure, and callback route",
                        "Count delivered contacts separately from attempted messages and returned mail",
                    ],
                    [
                        "Day 12: founder records discussions and classifies trust objections",
                        "P07 and P08 explain priced assistance without implying government affiliation",
                        "Conversation notes covering authority, prior filings, workload, and objections",
                        "Immediately suppress owners who request no further business contact",
                    ],
                    [
                        "Day 13: claims contractor tests two prospective evidence packages",
                        "P09 identifies missing documents before anyone promises submission readiness",
                        "Per-case document checklist with responsible signer and outstanding evidence",
                        "Do not execute an engagement with unresolved statutory contracting restrictions",
                    ],
                    [
                        "Day 14: founder reviews twenty delivered contacts and acquisition spending",
                        "P07 and P12 connect outreach effort with potential fee economics",
                        "Weekly funnel, time ledger, direct costs, and estimated lawful fees",
                        "Stop low-value segments when projected fees cannot support delivery costs",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Tactics That Reduce False Matches and Owner Distrust",
                "body": (
                    "Experienced recovery operators sell documented execution, "
                    "not secrecy around publicly accessible property searches."
                ),
                "items": [
                    (
                        "Preserve historical holder and address details before "
                        "refreshing a treasury search; current registry addresses "
                        "alone often cannot explain an old corporate warrant."
                    ),
                    (
                        "Ask the corporate controller about existing claims before "
                        "building a packet, preventing duplicate submissions and "
                        "avoidable disputes over who performed the recovery work."
                    ),
                    (
                        "Send the official treasury claim route with the first "
                        "substantive message; an owner who independently verifies "
                        "the property becomes a better-qualified prospect."
                    ),
                    (
                        "Batch document requests by signer and entity, but retain "
                        "separate property identifiers, fee calculations, and status "
                        "histories for every claim."
                    ),
                ],
            },
        },
        {
            "heading": "3. Days 15–21: Submit Evidence-Complete Claims and Reconcile the Fee Engine",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Days 15–17 convert signed mandates into reviewable claim "
                    "packets. The claims contractor checks the treasury's current "
                    "instructions against the corporation's legal name, taxpayer "
                    "identifier where required, historical address, signer authority, "
                    "and property identifiers. Obtain sensitive documents through "
                    "the restricted repository rather than ordinary email "
                    "attachments. California Civil Code §1798.81.5 supplies a "
                    "concrete reasonable-security requirement where applicable; "
                    "apply access minimization across the entire workflow rather "
                    "than treating security as a state-specific afterthought. "
                    "E-signature software such as DocuSign can record execution "
                    "evidence, but it does not make an ineligible agreement "
                    "valid or replace a treasury's notarization requirement. The "
                    "founder independently reviews identity and authority before "
                    "submission. Track four distinct events: internal packet "
                    "completion, submission receipt, custodian confirmation of "
                    "intake, and claim determination. In this chapter, an "
                    "accepted packet means the custodian has acknowledged intake "
                    "without a currently identified missing item; it does not "
                    "mean the claim is approved. If the agency offers only an "
                    "automated receipt, retain that narrower status and do not "
                    "inflate the accepted-packet count. A submission queue can "
                    "be automated; authority to attest facts cannot be delegated "
                    "to an unreviewed matching rule."
                ),
                (
                    "On Days 18–19, establish status tracking without overwhelming "
                    "the treasury or the pod. Record the agency's published "
                    "processing guidance and assign the next inquiry from that "
                    "guidance, not an invented seven-day escalation cycle. Store "
                    "each request for additional evidence with its exact wording, "
                    "received date, owner, and response deadline. Separate owner "
                    "delay, agency delay, and operator defect because each "
                    "requires a different remedy. An incorrect identifier or "
                    "missing required authority document is an operator defect; "
                    "a queue awaiting agency review is not. Aim for at most "
                    "one material operator defect among the first ten submitted "
                    "packets, while reporting the actual count whenever fewer "
                    "than ten exist. Freeze related submissions immediately "
                    "after an identity or unauthorized-signature error, regardless "
                    "of the aggregate rate. The founder reviews a daily exception "
                    "queue capped at five active document-chasing cases. Contractors "
                    "work from explicit tasks and time allowances, not open-ended "
                    "instructions to investigate everything. By Day 21, target "
                    "forty delivered contacts, ten substantive discussions, four "
                    "qualified mandates, and two accepted packets. These are "
                    "pilot thresholds rather than revenue predictions. If agency "
                    "acknowledgments are unavailable, retain the evidence-complete "
                    "submissions and classify that part of the expansion decision "
                    "as pending."
                ),
                (
                    "Days 20–21 also reconcile the economic model to the canonical "
                    "scorecard. At the illustrative $3,000 earned fee, twenty "
                    "annual completed recoveries generate $60,000 Conservative "
                    "revenue; eighty-five generate $255,000 Base revenue; and "
                    "150 generate $450,000 Scaled revenue. The associated client "
                    "property totals would be $600,000, $2,550,000, and $4,500,000 "
                    "at a uniform ten-percent fee, but none belongs in operator "
                    "revenue. With $1,000 direct cost per collected recovery, "
                    "direct costs are $20,000, $85,000, and $150,000. Other "
                    "annual operating costs of $25,000, $74,375, and $75,000 "
                    "produce total expenses of $45,000, $159,375, and $225,000. "
                    "Subtracting those expenses yields exactly $15,000, $95,625, "
                    "and $225,000 owner net profit, or 25%, 37.5%, and 50%. "
                    "This allocation illustrates the supplied totals; it is not "
                    "an independently established staffing-cost forecast. Conservative "
                    "and Base retain one full-time operator plus two contractors; "
                    "Scaled requires two full-time operators plus three contractors. "
                    "Do not represent the five-person outcome as achievable by "
                    "the launch pod automatically. Track earned fees, invoices, "
                    "and cash receipts separately under the adopted accounting "
                    "policy. A signed contingency agreement or treasury receipt "
                    "does not itself establish earned revenue, and client "
                    "principal must never subsidize the operator's runway."
                ),
            ],
            "table": {
                "caption": "Week Three Claim Delivery, Exception Handling, and Canonical Revenue Reconciliation",
                "headers": [
                    "Day and accountable execution owner",
                    "Mapped plays and required operating action",
                    "Deliverable retained for independent case review",
                    "Failure condition and immediate operator response",
                ],
                "rows": [
                    [
                        "Day 15: claims contractor assembles the first signed-mandate packets",
                        "P08 and P09 connect executed agreements with required evidence",
                        "Signer authority, property identifiers, required documents, and execution records",
                        "Return incomplete packets to evidence collection rather than submitting guesses",
                    ],
                    [
                        "Day 16: founder independently reviews identity and representation authority",
                        "P05 and P09 challenge ambiguous names and corporate succession",
                        "Second-person review log explaining each accepted identity evidence chain",
                        "Stop affected files immediately after identity or signer-authority defects",
                    ],
                    [
                        "Day 17: authorized submitter files through approved treasury channels",
                        "P10 follows custodian instructions without automated factual attestations",
                        "Submission copy, timestamp, receipt, and submitting representative's documented authority",
                        "An automated receipt proves delivery rather than substantive claim acceptance",
                    ],
                    [
                        "Day 18: claims contractor creates agency-specific status follow-up dates",
                        "P11 uses published processing guidance and received evidence requests",
                        "Status history with next inquiry date and responsible case owner",
                        "Do not classify ordinary agency queue time as operator failure",
                    ],
                    [
                        "Day 19: founder resolves material exceptions and measures handling time",
                        "P09 and P11 distinguish owner delays from preventable packet defects",
                        "Exception register with cause, correction, deadline, and incremental labor",
                        "Cap active document-chasing files at five within the launch pod",
                    ],
                    [
                        "Day 20: founder reconciles modeled fees with the canonical scorecard",
                        "P12 excludes client principal and separates earned fees from cash",
                        "Three-case worksheet reconciling exact revenue, expense, profit, and staffing",
                        "Reject any model treating gross recovered property as operator revenue",
                    ],
                    [
                        "Day 21: founder reviews the forty-contact pilot cohort",
                        "P07 through P11 connect discussions, mandates, submissions, and acknowledgments",
                        "Forty-contact funnel targeting ten discussions, four mandates, two accepted packets",
                        "Classify missing agency acknowledgments as pending rather than inventing acceptance",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Verify the property and authority chain",
                    "action": (
                        "Link the official property record to the claimant and "
                        "the claimant to an authorized signer."
                    ),
                    "detail": (
                        "Retain independent identity evidence, custody classification, "
                        "restriction dates, and a second-person review before engagement."
                    ),
                },
                {
                    "step": 2,
                    "title": "Execute a permitted and transparent engagement",
                    "action": (
                        "Explain direct claiming and execute the jurisdiction-specific "
                        "agreement only when its timing and terms are permitted."
                    ),
                    "detail": (
                        "Record the fee basis, applicable ceiling, signing evidence, "
                        "scope, and approved payment route without requesting control "
                        "of the owner's treasury credentials."
                    ),
                },
                {
                    "step": 3,
                    "title": "Submit the reviewed evidence packet",
                    "action": (
                        "Complete the custodian checklist and submit through the "
                        "authorized channel with documented factual review."
                    ),
                    "detail": (
                        "Preserve the packet and receipt; distinguish submission, "
                        "acknowledged intake, approval, and payment as separate events."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile the outcome and earned service fee",
                    "action": (
                        "Confirm the owner's recovery, establish that contractual "
                        "performance conditions are satisfied, and invoice appropriately."
                    ),
                    "detail": (
                        "Keep client principal outside operating cash, reconcile "
                        "earned revenue separately from collection, and charge failed-file "
                        "effort to the originating acquisition cohort."
                    ),
                },
            ],
        },
        {
            "heading": "4. Days 22–30 and Beyond: Apply Kill, Fix, or Scale Decisions to Mature Evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Days 22–30 close the pilot's evidence gaps instead of "
                    "manufacturing a launch victory. Day 22 reconciles duplicates "
                    "and contact delivery; Day 23 closes outstanding owner-document "
                    "requests; Day 24 rechecks contracting restrictions; Day 25 "
                    "audits packet defects; Day 26 updates the cash forecast; "
                    "Day 27 evaluates fee sensitivity; Day 28 independently "
                    "reviews the cohort; Day 29 drafts the decision memo; and "
                    "Day 30 records Kill, Fix, or Scale by segment. Use "
                    "cumulative delivered unique-owner contacts as the mandate "
                    "conversion denominator: forty at Day 30, eighty at Day "
                    "60, and 120 at Day 90. Do not count repeated follow-ups "
                    "as additional prospects. Target at least 10% qualified "
                    "mandate conversion, producing four, eight, and twelve "
                    "mandates respectively. Target two, four, and six accepted "
                    "packets at those checkpoints. Underfilled samples default "
                    "to Fix or continued observation, never a claimed statistical "
                    "victory. Report matching precision on independent twenty-record "
                    "audits separately from outreach conversion. Count all "
                    "identity or authority incidents explicitly, even after "
                    "correction. The decision memo must name the owner, evidence, "
                    "spend authorization, and next review date for each "
                    "continuing workstream so contractors do not interpret "
                    "silence as permission to expand."
                ),
                (
                    "Kill means stop the defective segment or acquisition method, "
                    "not abandon valid customer obligations. Any confirmed "
                    "unauthorized filing, knowingly false ownership assertion, or "
                    "prohibited fee arrangement stops affected activity immediately. "
                    "Commercial Kill requires both adequate observation and "
                    "persistently weak economics: below 5% qualified conversion "
                    "at the checkpoint's contact denominator, plus projected "
                    "fees below 1.5 times fully loaded direct cost. At Day "
                    "30 this is a provisional segment stop; retest only after "
                    "a documented change. At Days 60 and 90, require a "
                    "completed fourteen-day corrective experiment before treating "
                    "the same commercial result as persistent. Fix covers "
                    "conversion from 5% to below 10%, incomplete sample sizes, "
                    "document bottlenecks, and unsettled agency acknowledgments. "
                    "Change one variable per experiment, such as claimant type, "
                    "evidence request sequence, or the explanation of paid "
                    "assistance. Scale requires every listed quality, economics, "
                    "runway, and capacity condition; good sales cannot offset "
                    "bad identity controls. Increase new-contact volume by at "
                    "most 25% after Day 30 and 50% after later checkpoints, "
                    "subject to contractor hours. These increments authorize "
                    "controlled prospecting only. They do not authorize hiring "
                    "the five-person Scaled team or treating pending fees "
                    "as spendable money."
                ),
                (
                    "Day 60 and Day 90 reviews must distinguish collection "
                    "latency from business failure. With a canonical 3–12-month "
                    "first-deal interval, zero receipts at ninety days alone "
                    "does not justify Kill. Compare each pending claim with "
                    "its custodian's published guidance, outstanding evidence, "
                    "and documented queue position where available. For provisional "
                    "expansion, require estimated lawful fees at least twice "
                    "modeled fully loaded direct costs and at least 1.5 "
                    "times those costs after a 25% fee reduction. The "
                    "$3,000 fee and $1,000 cost illustration passes both "
                    "tests, but observed failed-file effort can overturn it. "
                    "Recalculate costs using actual hours and prospect acquisition "
                    "spending, including work on unsuccessful cases. Retain "
                    "six months of maintenance cash after every new commitment. "
                    "Before permanent staffing expansion, require three collected "
                    "recoveries, actual cohort contribution of at least 50% "
                    "of earned fees after direct costs, and twelve weeks "
                    "of measured capacity data. Three outcomes provide an "
                    "initial calibration, not mature loss-rate evidence. If "
                    "collections remain pending, continue the capped pilot only "
                    "while runway and case evidence support it. Recognize "
                    "revenue only when earned under the adopted policy; "
                    "reconcile invoices and receipts separately. The correct "
                    "Day 90 decision can be a disciplined Fix with viable "
                    "claims, bounded spending, and no revenue yet."
                ),
            ],
            "table": {
                "caption": "Final Nine-Day Closeout and Quantitative Day 30/60/90 Decision Matrix",
                "headers": [
                    "Checkpoint and decision under review",
                    "Required evidence or quantitative operating threshold",
                    "Authorized action within the staffing constraint",
                    "Cash, quality, or interpretation safeguard",
                ],
                "rows": [
                    [
                        "Day 22: founder reconciles the unique-owner outreach denominator",
                        "Deduplicate recipients and verify forty genuinely delivered initial contacts",
                        "Correct the cohort register before calculating any mandate conversion",
                        "Repeated follow-ups and returned letters never inflate delivered-contact counts",
                    ],
                    [
                        "Day 23: claims contractor closes outstanding owner-document requests",
                        "Assign every missing item a responsible signer and response date",
                        "Prioritize five active evidence-chasing files within allocated contractor hours",
                        "Do not purchase additional research without a specific evidentiary purpose",
                    ],
                    [
                        "Day 24: founder rechecks agreements against current restriction evidence",
                        "Confirm each mandate's custody dates, fee calculation, and signing authority",
                        "Suspend affected engagements until any identified restriction is resolved",
                        "An attractive property value never overrides prohibited agreement timing",
                    ],
                    [
                        "Day 25: founder reviews packet quality and material defect counts",
                        "Report actual submitted packets, material errors, and corrected evidence",
                        "Repair recurring checklist defects before releasing additional similar submissions",
                        "Any identity or authority incident stops related submissions immediately",
                    ],
                    [
                        "Day 26: founder refreshes committed spending and maintenance runway",
                        "Keep first-month commitments within $3,500 and ninety-day spending within $8,500",
                        "Remove discretionary purchases when remaining maintenance runway approaches six months",
                        "Include unpaid commitments rather than relying exclusively on bank balances",
                    ],
                    [
                        "Day 27: founder challenges fee assumptions with downside sensitivity",
                        "Require modeled fees at least twice fully loaded direct costs",
                        "Reprice permitted services or stop segments failing the economic test",
                        "After a twenty-five-percent fee reduction, retain at least 1.5-times coverage",
                    ],
                    [
                        "Day 28: second reviewer independently challenges the complete cohort",
                        "Check twenty matches plus every high-value or ambiguous identity chain",
                        "Correct records and reassess affected mandates before expansion discussions",
                        "Nineteen correct sampled matches support only a bounded pilot expansion",
                    ],
                    [
                        "Day 29: founder drafts the segment-level operating decision memo",
                        "Attach contact denominators, conversion, packet status, costs, and available cash",
                        "Assign one corrective experiment or bounded expansion to each segment",
                        "Every continuing activity receives an accountable owner and review date",
                    ],
                    [
                        "Day 30: founder records and communicates the final pilot decision",
                        "Apply the checkpoint criteria below without counting pending principal",
                        "Issue written contractor priorities and the next month's spending ceiling",
                        "Continue valid customer work even when prospect acquisition is stopped",
                    ],
                    [
                        "Day 30 Kill: provisionally stop the defective acquisition segment",
                        "Below two mandates from forty contacts and fee coverage below 1.5-times",
                        "Stop new segment outreach while completing existing legitimate customer obligations",
                        "Rights violations stop immediately regardless of sample size or conversion",
                    ],
                    [
                        "Day 30 Fix: preserve cash while testing one bottleneck",
                        "Two or three mandates from forty contacts, or incomplete evidence",
                        "Run one fourteen-day experiment without increasing the existing spending ceiling",
                        "Fewer than forty delivered contacts cannot establish commercial segment failure",
                    ],
                    [
                        "Day 30 Scale: authorize only a bounded prospecting increase",
                        "Four mandates, two accepted packets, nineteen correct audit matches, economic pass",
                        "Increase new-contact volume by at most twenty-five percent within capacity",
                        "Require zero unresolved critical defects and six months maintenance runway",
                    ],
                    [
                        "Day 60 Kill: stop persistent weakness after a corrective test",
                        "Below four mandates from eighty contacts and fee coverage below 1.5-times",
                        "Stop new acquisition after documenting the completed fourteen-day corrective experiment",
                        "Do not classify missing collections alone as failure within normal latency",
                    ],
                    [
                        "Day 60 Fix: repair conversion, evidence, or agency acknowledgment gaps",
                        "Four through seven mandates from eighty contacts, or unmet quality conditions",
                        "Continue one controlled experiment and prioritize complete customer evidence packets",
                        "Stay within the $2,500 second-month budget and current contractor capacity",
                    ],
                    [
                        "Day 60 Scale: expand the passing cohort within measured capacity",
                        "Eight mandates, four accepted packets, nineteen correct audit matches, economic pass",
                        "Increase new-contact volume by at most fifty percent without automatic hiring",
                        "Maintain six months runway and no unresolved identity or authority incidents",
                    ],
                    [
                        "Day 90 Kill: retire a repeatedly uneconomic acquisition segment",
                        "Below six mandates from 120 contacts and fee coverage below 1.5-times",
                        "Stop new segment spending after a documented corrective experiment failed",
                        "Preserve valid customer delivery and distinguish agency delay from operator defects",
                    ],
                    [
                        "Day 90 Fix: maintain a viable but incompletely proven cohort",
                        "Six through eleven mandates from 120 contacts, or collections still uncalibrated",
                        "Continue capped delivery and targeted corrections rather than permanent staffing expansion",
                        "Zero receipts alone do not defeat the three-to-twelve-month first-deal assumption",
                    ],
                    [
                        "Day 90 Scale: expand prospecting only when every condition passes",
                        "Twelve mandates, six accepted packets, nineteen correct audit matches, economic pass",
                        "Increase new-contact volume by at most fifty percent within measured capacity",
                        "Permanent staffing additionally requires three collections and fifty-percent cohort contribution",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Scale verified ownership, earned fees, and repeatable evidence—not the "
        "face value of property you do not own."
    ),
    "diagram_id": "diag-08",
    "action_checklist": [
        (
            "Assign P01–P12 to the founder and two contractors, then freeze the "
            "pilot to one state, one property class, and one claimant type."
        ),
        (
            "Complete the jurisdiction rules register, direct-claim disclosure, "
            "restricted repository, and twenty-record identity audit before outreach."
        ),
        (
            "Approve the $3,500 first-month and $8,500 ninety-day cash ceilings; "
            "record committed spending and preserve six months of maintenance runway."
        ),
        (
            "Build a hundred-record research cohort and measure forty delivered "
            "unique-owner contacts, ten discussions, four mandates, and two accepted "
            "packets by the first checkpoint."
        ),
        (
            "Reconcile the $60,000, $255,000, and $450,000 annual service-fee cases "
            "to exact owner profits of $15,000, $95,625, and $225,000 without "
            "including client principal."
        ),
        (
            "Issue written Day 30/60/90 segment decisions using contact denominators, "
            "identity quality, fee coverage, packet status, capacity, and runway; "
            "require collected-outcome evidence before permanent staffing expansion."
        ),
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure §1582",
            "url": (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=CCP&sectionNum=1582."
            ),
            "relevance": (
                "Controls agreements to locate, deliver, recover, or assist in "
                "recovering covered unclaimed property, including restricted "
                "contracting periods, compensation limits, and agreement requirements."
            ),
        },
        {
            "title": "Texas Property Code §74.507",
            "url": (
                "https://statutes.capitol.texas.gov/"
                "Docs/PR/htm/PR.74.htm#74.507"
            ),
            "relevance": (
                "Governs agreements for assistance recovering reported property; "
                "use its current fee, timing, and agreement provisions when "
                "designing a Texas recovery engagement."
            ),
        },
        {
            "title": "California Civil Code §1798.81.5",
            "url": (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.81.5"
            ),
            "relevance": (
                "Requires reasonable security procedures and practices for covered "
                "personal information and addresses safeguards in applicable "
                "third-party contractual disclosures."
            ),
        },
        {
            "title": "15 U.S.C. §7704 — Commercial Electronic Mail Requirements",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Provides requirements for covered commercial email, including "
                "header accuracy, deceptive subject lines, identification, postal "
                "address information, and opt-out mechanisms and handling."
            ),
        },
        {
            "title": "47 CFR §64.1200 — Restrictions on Telemarketing and Telephone Solicitation",
            "url": (
                "https://www.ecfr.gov/current/title-47/chapter-I/"
                "subchapter-B/part-64/subpart-L/section-64.1200"
            ),
            "relevance": (
                "Supplies federal restrictions relevant to covered calls, texts, "
                "telephone solicitations, automated dialing, and prerecorded or "
                "artificial-voice outreach; evaluate the actual channel before use."
            ),
        },
    ],
}
