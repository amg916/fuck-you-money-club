from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) high-ticket brokerage team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Event Workers, Evidence-Linked Buyer Matching, IRC Section 6418 Transfers, State Credit Placement, and Escrow-Controlled Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #26, High-Ticket Brokerage, ranks #10 with an 88/100 Money-to-Manpower "
        "Score across 21 mapped plays. Its automation advantage is disciplined coordination, "
        "not autonomous negotiation: Python workers collect evidence, rank buyer fit, maintain "
        "document checklists, and surface stalled milestones while people control representations "
        "and settlement. This chapter develops two tax-credit placement plays without treating "
        "credit face value, buyer wires, or asset consideration as brokerage revenue. Canonical "
        "annual owner profits are $25,000 Conservative, $206,250 Base, and $500,000 Scaled. "
        "A measured workload model targets 74% net repetitive-work reduction after review. "
        "Evidence-linked outreach and partner referrals compound distribution, while direct "
        "transfer rules, state eligibility checks, escrow instructions, and recoverable event "
        "processing prevent faster software from multiplying expensive closing errors."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "25% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$550,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "37.5% net margin; $206,250 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual retained transaction commissions; underlying asset values excluded",
            "note": "50% net margin; $500,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence ledger before automating buyer introductions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one exclusive mandate, one asset category, and a written commission "
                    "schedule. Candidate #26 covers 21 mapped plays, but a four-person team should "
                    "not launch 21 intake systems simultaneously. The full-time principal owns "
                    "mandates, consequential representations, negotiations, and release decisions; "
                    "three contractors cover research, document operations, and buyer development. "
                    "Contractors are fractional capacity, not three additional full-time salaries. "
                    "Use HubSpot or Pipedrive for relationship state and a separate evidence ledger "
                    "for source documents, permissions, provenance, and review decisions. Give every "
                    "mandate, legal entity, asset, document version, and introduction an immutable "
                    "identifier. A signed NCNDA can support confidentiality and anti-circumvention "
                    "obligations, but it cannot establish a brokerage license, repair defective "
                    "agency disclosure, or replace an enforceable fee agreement. Before ingestion, "
                    "the principal records the asset-specific licensing analysis and permitted "
                    "activities. Securities-related M&A requires attention to Exchange Act Section "
                    "15(a), any applicable Section 15(b)(13) exemption conditions, and state rules. "
                    "Real estate and other regulated assets need separate treatment. Automate "
                    "routing only after these classifications exist, because the same introductory "
                    "email can represent a different regulated activity when the underlying asset "
                    "changes. Reject incomplete mandate records rather than letting the model "
                    "invent missing authority."
                ),
                (
                    "Implement the intake path as signed webhook, durable event record, Python "
                    "worker, validation result, review task, and CRM update. Python's hmac and "
                    "hashlib can verify a provider's documented signature scheme; time validates "
                    "timestamp tolerance, while json parses an explicitly limited request body. "
                    "Persist a unique provider event identifier before acknowledging receipt. A "
                    "small single-worker installation can use sqlite3 transactions and a unique "
                    "constraint for deduplication; distributed workers need a datastore supporting "
                    "their concurrency requirements. Do not claim exactly-once delivery: instead, "
                    "make state transitions idempotent and reconcile uncertain external writes. "
                    "urllib.request can call public APIs with timeouts, and decimal.Decimal should "
                    "handle commission arithmetic. Save source URLs, retrieval timestamps, content "
                    "hashes, and access permissions alongside extracted facts. An LLM receives "
                    "redacted documents as evidence, never instructions from embedded text. Its "
                    "structured response contains extracted fields, supporting page references, "
                    "and explicit missing-field flags. Ordinary Python validators enforce types, "
                    "allowed statuses, date order, and amount bounds before any CRM write. Missing "
                    "evidence creates a review task rather than a fabricated answer. Keep secrets "
                    "outside records and prompts, and scope each service account to the minimum "
                    "objects its worker must touch."
                ),
                (
                    "Buyer matching should begin with deterministic eligibility filters, followed "
                    "by a transparent ranking model. Filter jurisdiction, asset type, check size, "
                    "closing window, mandate restrictions, and verified acquisition authority before "
                    "scoring strategic fit. An illustrative score assigns 35 points to documented "
                    "investment criteria, 25 to available capital evidence, 20 to timing, and 20 "
                    "to relevant execution history. These weights are operating assumptions, not "
                    "predictions of closing probability. The LLM summarizes why a candidate fits "
                    "and cites the buyer profile fields; it does not certify funds or infer tax "
                    "capacity from wealth signals. Require a human to approve the first external "
                    "introduction and every material change to deal claims. Preserve the approved "
                    "teaser hash so later outreach cannot silently acquire stronger assertions. "
                    "A referral loop starts only after a successful introduction or completed "
                    "milestone, with permission to request another relevant buyer or seller. "
                    "Measure qualified responses and completed diligence, not scraped addresses. "
                    "Track rejected matches by reason and update filters weekly, keeping the "
                    "original rejection evidence. If ranking quality deteriorates, disable the "
                    "ranking layer and return to a saved, manually reviewed shortlist while "
                    "retaining the same mandate and introduction records."
                ),
            ],
            "table": {
                "caption": "Evidence-first architecture for exclusive mandates and controlled introductions",
                "headers": [
                    "Operating component",
                    "Concrete implementation",
                    "Human decision boundary",
                    "Recovery and audit evidence",
                ],
                "rows": [
                    [
                        "Mandate intake establishes authority before any external representation",
                        "HubSpot stores signed scope and immutable mandate identifiers",
                        "Principal verifies agency position and asset-specific license requirements",
                        "Missing authority freezes introductions while retaining submitted evidence",
                    ],
                    [
                        "Webhook receiver records authenticated events before downstream processing",
                        "Python verifies signatures and persists unique provider identifiers",
                        "Operator investigates repeated authentication failures before restoring traffic",
                        "Duplicate deliveries return receipts without repeating business transitions",
                    ],
                    [
                        "Evidence extraction preserves document provenance and permission boundaries",
                        "Python hashes source files and stores page-linked extracted fields",
                        "Reviewer resolves missing facts and conflicting seller statements",
                        "Rejected extraction remains traceable to its original source",
                    ],
                    [
                        "Buyer eligibility filters precede optional model-assisted match ranking",
                        "Rules compare jurisdiction, check size, timing, and acquisition authority",
                        "Principal approves introductions using verified buyer profile evidence",
                        "Ranking failures revert to previously reviewed eligible shortlists",
                    ],
                    [
                        "Teaser distribution uses versioned claims and restricted recipients",
                        "CRM records approved document hashes against each introduction",
                        "Reviewer authorizes material claim changes before external delivery",
                        "Withdrawal notices identify affected recipients and superseded versions",
                    ],
                    [
                        "Referral capture expands distribution without exposing confidential mandates",
                        "Permissioned partner forms route introductions into existing evidence records",
                        "Principal reviews referral compensation and applicable licensing restrictions",
                        "Disputed introductions preserve timestamps, agreements, and correspondence history",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the introduction trail before increasing volume",
                "body": (
                    "The durable asset is a verified relationship graph linked to mandates, "
                    "permissions, and fee evidence, not a large contact export."
                ),
                "items": [
                    "Log pre-existing buyer relationships before signing exclusivity, and resolve carve-outs in the fee agreement before introductions begin.",
                    "Version every teaser and record exactly which recipient received each version; corrected claims need a recipient-level withdrawal trail.",
                    "Use buyer rejection reasons to improve eligibility filters instead of asking the model to generate more persuasive unsupported claims.",
                    "Keep counsel, escrow, and tax diligence channels attached to the mandate identifier so a contractor handoff does not erase closing context.",
                ],
            },
        },
        {
            "heading": "2. Automate credit origination without inventing transferability or inventory profits",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For transferable_tax_credit_brokerage_syndication, assemble an origination watchlist "
                    "from federal DOE and EPA project resources, actual ISO or utility "
                    "interconnection queues, state film offices, and historic-preservation registries. "
                    "DOE and EPA are discovery sources, not a universal interconnection queue or "
                    "proof that a project generated transferable credits. Use published downloads "
                    "and permitted APIs before scraping; cache responses, respect access terms, "
                    "and stop collection when permission or source integrity is doubtful. Resolve "
                    "project companies through documented ownership relationships rather than fuzzy "
                    "names alone. A queue position, film announcement, or historic designation "
                    "creates a lead, not a saleable credit. The worker should extract project "
                    "status, location, owner, program, evidence date, and the next verification "
                    "question. A researcher then confirms whether the relevant taxpayer generated "
                    "an eligible credit, whether certification or registration is complete, and "
                    "whether a buyer can use it. Federal Section 6418 and state transfer programs "
                    "belong in separate rule sets. Record the governing tax year and program "
                    "version because eligibility, caps, deadlines, and administrative practices "
                    "change. Until these checks pass, the system labels the opportunity as "
                    "origination research and suppresses executable buyer offers."
                ),
                (
                    "The advertised sourcing band of $0.82 to $0.88 and placement band of $0.92 "
                    "to $0.96 per credit dollar requires careful transaction design. On $1,000,000 "
                    "face value, those bands imply $820,000 to $880,000 of seller-side pricing "
                    "and $920,000 to $960,000 of buyer-side pricing, with a theoretical $40,000 "
                    "to $140,000 gross difference before expenses. That difference is neither "
                    "automatically earned nor automatically brokerage revenue. Under Section 6418, "
                    "an eligible taxpayer transfers credits directly to an unrelated buyer for "
                    "cash; a transferee cannot subsequently transfer the purchased credit. Therefore, "
                    "do not implement a federal buy-and-resell chain. Structure a direct transfer "
                    "with simultaneous escrow disbursements and an expressly disclosed commission "
                    "that the parties accept. A $30,000 retained commission is $30,000 revenue, "
                    "regardless of credit face value or wires passing through independent escrow. "
                    "Require buyer funding before release and never warehouse unhedged credits "
                    "on the operator's balance sheet. Where the mandate requires non-cancelable "
                    "tax-credit insurance, inspect the bound policy, exclusions, limits, insured "
                    "parties, and cancellation provisions before scheduling settlement. If suitable "
                    "coverage or direct-transfer mechanics are unavailable, suspend the transaction; "
                    "insurance does not itself validate eligibility."
                ),
                (
                    "For state_film_historic_brownfield_tax_credit_brokerage, build a jurisdiction-specific "
                    "placement checklist instead of copying the federal workflow. Georgia film "
                    "credits, Louisiana motion-picture credits, state historic rehabilitation "
                    "credits, and brownfield incentives can have different certification, assignment, "
                    "taxpayer, carryforward, notification, and transfer-frequency requirements. Federal "
                    "historic rehabilitation credits do not become outright transferable merely "
                    "because a state program permits assignments. The matching worker asks for "
                    "the certified amount, credit year, usable tax type, permitted transferee, "
                    "remaining life, prior assignments, and required agency acknowledgments. "
                    "A designated tax specialist verifies those answers against current primary "
                    "authority and the actual certificate before the principal authorizes a "
                    "term sheet. Illustratively, placing $500,000 face value at $0.90 produces "
                    "$450,000 of buyer consideration; a separately contracted 3% fee on face "
                    "value yields $15,000 operator revenue, not $450,000. Escrow instructions "
                    "must identify who pays that fee and avoid counting it twice. If certification, "
                    "buyer usability, or assignment restrictions fail diligence, suspend settlement "
                    "under the agreed contingencies and rematch only verified eligible credits. "
                    "Do not guarantee tax savings. Keep this state placement funnel distinct "
                    "from federal transfers so one successful closing cannot incorrectly train "
                    "the matching rules for another jurisdiction."
                ),
            ],
            "table": {
                "caption": "Tax-credit origination, direct-transfer controls, and fee-only economics",
                "headers": [
                    "Workflow and evidence",
                    "Illustrative unit economics",
                    "Required verification",
                    "Risk fallback",
                ],
                "rows": [
                    [
                        "Federal project discovery combines DOE resources with utility queues",
                        "One million credit dollars remain prospective until generation verification",
                        "Researcher confirms taxpayer ownership and eligible credit generation evidence",
                        "Unverified project signals stay research leads without executable offers",
                    ],
                    [
                        "Federal direct transfer replaces an impermissible intermediary resale chain",
                        "Thirty thousand dollars retained commission becomes recognized operator revenue",
                        "Specialist checks unrelated buyer status and transfer election requirements",
                        "Conflicting transfer structure pauses settlement until documents are corrected",
                    ],
                    [
                        "Quoted discount bands describe proposed pricing rather than earned commissions",
                        "One million face implies forty to one hundred forty thousand difference",
                        "Principal reconciles disclosed compensation against final signed settlement instructions",
                        "Unagreed spread economics are excluded from revenue and forecasts",
                    ],
                    [
                        "Buyer-funded escrow coordinates direct transfer and concurrent fee disbursement",
                        "Buyer consideration never enters the brokerage commission revenue total",
                        "Independent escrow confirms cleared funds and authenticated release instructions",
                        "Missing funds or required insurance prevents any settlement release",
                    ],
                    [
                        "State film credit placement uses certified jurisdiction-specific transfer evidence",
                        "Five hundred thousand face at three percent earns fifteen thousand",
                        "Tax specialist verifies buyer usability and required agency notifications",
                        "Failed eligibility suspends settlement and permits only verified rematching",
                    ],
                    [
                        "Historic and brownfield placements require separate state program rulebooks",
                        "Quoted fee basis follows signed terms rather than assumed discounts",
                        "Reviewer distinguishes state assignments from federal historic credit restrictions",
                        "Unresolved transferability removes the credit from active buyer circulation",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before any credit closing",
                "body": (
                    "Automation may prepare the package, but the named reviewer must record "
                    "evidence for each condition before the principal authorizes release."
                ),
                "items": [
                    "Verify seller authority, applicable brokerage permissions, agency disclosures, executed mandate, and the exact commission payer and calculation basis.",
                    "Verify the certified or supported credit amount, governing program, tax year, buyer eligibility, transfer restrictions, and required registration or agency records.",
                    "Verify independent escrow instructions, buyer funding, direct-transfer structure where required, and out-of-band confirmation of every wiring change.",
                    "Verify required bound insurance terms, unresolved diligence exceptions, final document versions, and a documented suspension path if any condition fails.",
                ],
            },
        },
        {
            "heading": "3. Connect document checklists, closing milestones, and permissioned growth loops",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build fulfillment around a finite-state machine rather than a collection of "
                    "calendar reminders. Useful states include mandate signed, buyer screened, "
                    "teaser approved, diligence opened, conditions outstanding, settlement ready, "
                    "closed, and suspended. Each transition requires specified evidence, a responsible "
                    "person, and a permitted actor. The document worker compares an asset-specific "
                    "checklist with actual file versions, flags missing signatures and stale "
                    "certificates, and drafts a precise deficiency request. It cannot decide "
                    "that a missing condition is commercially immaterial. DocuSign completion "
                    "events can populate signature evidence, but a completed envelope does not "
                    "prove every closing condition has been satisfied. Track deadline origin, "
                    "timezone, responsible counterparty, escalation date, and supporting clause. "
                    "When a deadline changes, retain both versions and the authorizing communication. "
                    "Escrow providers remain responsible for their contracted custody and release "
                    "functions; the brokerage tracks status without treating a webhook as "
                    "authority to move money. Verify changed bank instructions through an "
                    "established contact using an independently sourced number. A suspicious "
                    "change freezes settlement communications until resolved. During an outage, "
                    "the operations contractor exports the last approved checklist and runs "
                    "a manual exception log that is reconciled before automated transitions resume."
                ),
                (
                    "Distribution should reuse verified knowledge without publishing confidential "
                    "inventory. Build programmatic pages around specific acquisition criteria, "
                    "jurisdictions, process timelines, and evidence requirements, with human-reviewed "
                    "source links and an update date. Do not auto-publish seller identities, "
                    "buyer tax positions, unsupported returns, or confidential transaction examples. "
                    "A practical loop starts with a useful buyer checklist, captures permission "
                    "for a narrowly defined update, asks for acquisition criteria, and returns "
                    "a reviewed relevant opportunity. After a successful milestone, request "
                    "a permissioned introduction to one comparable counterparty. This is a "
                    "referral mechanism, not an assumption of viral growth. For outbound email, "
                    "apply CAN-SPAM requirements including accurate headers, truthful subject "
                    "lines, required sender information, and working opt-out processing. Maintain "
                    "one suppression ledger across contractors and delivery vendors; honor "
                    "opt-outs within the statutory deadline and preferably immediately. Automated "
                    "calls and texts require their own channel-specific review rather than "
                    "borrowing email rules. Illustratively, 200 eligible emails producing 20 "
                    "replies, eight qualified conversations, and two diligence starts demonstrate "
                    "routing yield, not two future closings. Inspect rejection reasons and "
                    "complaints before increasing volume, and stop a sequence when a recipient's "
                    "eligibility or permission changes."
                ),
                (
                    "Treat every integration failure as a recoverable business event. Retry "
                    "transient network errors with bounded exponential backoff and jitter, honor "
                    "provider rate-limit instructions, and move persistent failures to an "
                    "exception queue with an owner and deadline. Never retry wire instructions "
                    "or client-facing messages blindly after a timeout: first determine whether "
                    "the original action succeeded. Store the intended operation, external "
                    "object identifier, request hash, attempt count, and reconciliation result. "
                    "A malformed model response should trigger deterministic extraction or "
                    "manual review, not an increasingly permissive prompt. Repeated model "
                    "disagreement on credit amounts, parties, or restrictions disables that "
                    "workflow until the underlying cause is understood. Keep a small evaluation "
                    "set of previously reviewed documents, including amended certificates, "
                    "duplicate projects, conflicting signatures, and adversarial embedded "
                    "instructions. Re-run it before changing prompts, parsers, or model versions. "
                    "Measure field accuracy separately from narrative fluency and sample "
                    "low-confidence and high-value cases more heavily. Log who corrected each "
                    "field and why. The principal receives a daily exception digest showing "
                    "blocked closings, aged diligence, changed instructions, and overdue "
                    "reviews, while contractors receive only the tasks and documents needed "
                    "for their assigned responsibilities."
                ),
            ],
            "table": {
                "caption": "Milestone integrity, distribution loops, and exception recovery",
                "headers": [
                    "Automation event",
                    "Permitted machine output",
                    "Consequential human review",
                    "Failure recovery procedure",
                ],
                "rows": [
                    [
                        "Executed mandate initiates the asset-specific diligence checklist workflow",
                        "Worker creates required document tasks with named accountable owners",
                        "Principal confirms scope and exceptions against the signed engagement",
                        "Missing scope returns the matter to mandate clarification status",
                    ],
                    [
                        "New certificate version changes recorded amount or expiration evidence",
                        "Parser proposes field updates with source pages and differences",
                        "Tax specialist verifies material changes before buyer documents update",
                        "Conflicting versions suspend circulation until authoritative evidence is established",
                    ],
                    [
                        "Escrow status message reports progress toward the scheduled closing",
                        "Tracker records status without issuing payment or release instructions",
                        "Principal confirms conditions with the appointed independent escrow contact",
                        "Suspicious instruction changes trigger an immediate settlement communication freeze",
                    ],
                    [
                        "Public educational page captures a permissioned buyer criteria submission",
                        "CRM routes jurisdiction and check-size preferences into eligibility filters",
                        "Reviewer checks published claims and excludes confidential mandate information",
                        "Stale source material removes affected pages from active promotion",
                    ],
                    [
                        "Outbound sequence receives an opt-out or eligibility change event",
                        "Suppression ledger stops pending messages across every connected sender",
                        "Operator investigates complaints and conflicting recipient permission records",
                        "Vendor synchronization failure pauses sending until suppression reconciliation completes",
                    ],
                    [
                        "External timeout leaves message delivery or object creation uncertain",
                        "Worker records pending reconciliation rather than repeating consequential actions",
                        "Operations contractor checks external receipts before authorizing another attempt",
                        "Unresolved delivery state enters an owned manual exception queue",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register and authenticate the event",
                    "action": "Verify the provider signature and persist the unique event identifier.",
                    "detail": "Reject invalid requests, enforce payload limits, and acknowledge only after durable intake recording.",
                },
                {
                    "step": 2,
                    "title": "Extract and validate the proposed change",
                    "action": "Run deterministic checks around evidence-linked model extraction.",
                    "detail": "Compare source versions, required fields, amount bounds, and permitted state transitions before preparing an update.",
                },
                {
                    "step": 3,
                    "title": "Route consequential decisions to the named reviewer",
                    "action": "Present proposed claims, introductions, or closing changes with supporting evidence.",
                    "detail": "Record reviewer identity, decision, document hashes, and exceptions; never let embedded document instructions change workflow authority.",
                },
                {
                    "step": 4,
                    "title": "Execute once logically and reconcile outcomes",
                    "action": "Apply the approved update with an idempotency record and inspect external receipts.",
                    "detail": "Resolve uncertain writes before retrying, preserve the audit trail, and export outstanding exceptions for manual continuation during outages.",
                },
            ],
        },
        {
            "heading": "4. Prove the 70% threshold and scale retained commissions, not transaction volume",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Measure automation against a fixed, observed basket of repetitive work. "
                    "The illustrative weekly baseline below contains 1,000 manual minutes "
                    "across research, qualification, document checking, milestone tracking, "
                    "distribution preparation, and reconciliation. Automation displaces 850 "
                    "minutes but adds 110 minutes of review, leaving 150 minutes of untouched "
                    "manual work plus 110 review minutes. Net reduction is therefore "
                    "(1,000 minus 260) divided by 1,000, or 74%. This is a testable workload "
                    "target, not a claim that software conducts 74% of negotiation or "
                    "professional judgment. Include correction time, failed runs, duplicate "
                    "cleanup, and contractor supervision in the measured remainder. Establish "
                    "the baseline with a representative sample before deployment and use "
                    "the same task definitions afterward. If the weekly basket changes "
                    "materially, publish separate old-basket and new-basket results rather "
                    "than declaring an artificial improvement. Sample all consequential "
                    "outputs for human authorization and use risk-weighted checks on "
                    "routine extraction. A rising correction rate consumes the apparent "
                    "savings immediately. Pause the weakest workflow when net reduction "
                    "falls below the target, retain the working automations, and restore "
                    "the manual procedure until the defective rule or source is repaired."
                ),
                (
                    "Price each automated run explicitly before choosing a model or orchestration "
                    "vendor. Assume, solely for budgeting, 4,000 input tokens at $2 per "
                    "million and 1,000 output tokens at $8 per million: model cost is "
                    "$0.008 plus $0.008, or $0.016. Add $0.004 for allocated execution "
                    "and storage to obtain $0.020 per successful machine attempt. These "
                    "are illustrative rates, not a quoted vendor tariff. With a 10% "
                    "expected additional-attempt allowance, machine cost averages $0.022 "
                    "per completed run. Two minutes of reviewer time at $60 per hour "
                    "adds $2.00, producing $2.022 per reviewed run, or $202.20 for "
                    "100 runs. That review-heavy example is separate from the weekly "
                    "workload basket and should not be substituted into it without "
                    "matching task counts. Track actual token usage, retries, storage, "
                    "delivery charges, and review minutes by mandate. Reserve expensive "
                    "reasoning for conflicting evidence; ordinary date comparisons, fee "
                    "calculations, and completeness checks belong in deterministic code. "
                    "Set per-mandate spend alerts and maximum retry counts. If model "
                    "service disappears, continue matching from verified structured fields "
                    "and issue manually reviewed deficiency requests rather than interrupting "
                    "an otherwise valid closing."
                ),
                (
                    "Reconcile every growth forecast to retained transaction commissions. "
                    "The Conservative case is $100,000 revenue less $75,000 total costs, "
                    "yielding $25,000 owner profit at 25% with 1 FT + 3 C. "
                    "The Base case is $550,000 revenue less $343,750 total costs, "
                    "yielding $206,250 at 37.5% with the same team. The Scaled case "
                    "is $1,000,000 revenue less $500,000 total costs, yielding $500,000 "
                    "at 50% with 2 FT + 4 C. Illustrative fee-equivalent bridges "
                    "are four closings at $25,000, eleven at $50,000, and twenty "
                    "at $50,000 respectively; actual mandates can produce a different "
                    "mix with identical annual retained revenue. Do not add these "
                    "examples to the canonical totals. The $3,000 to $18,000 monthly "
                    "opex planning range is not a substitute for each scenario's "
                    "complete annual cost budget, which must include variable delivery "
                    "and contractor costs. Startup capital remains $15,000 to $100,000 "
                    "and first-deal timing remains 3 to 12 months. Maintain a "
                    "rolling cash forecast that excludes unsigned commissions and "
                    "models delayed or failed closings. Add personnel only when "
                    "review queues and executable mandates justify capacity, not "
                    "because the top of the funnel looks busy."
                ),
            ],
            "table": {
                "caption": "Illustrative 1,000-minute weekly basket yielding 74% net repetitive-work reduction",
                "headers": [
                    "Measured repetitive work",
                    "Baseline and machine displacement",
                    "Required review allocation",
                    "Net labor remaining and safeguard",
                ],
                "rows": [
                    [
                        "Research collects permitted project sources and resolves entity records",
                        "Baseline 250 minutes; machine displacement removes 230 manual minutes",
                        "Thirty review minutes verify source integrity and entity identity",
                        "Fifty minutes remain after review; unsupported records stay quarantined",
                    ],
                    [
                        "Qualification compares documented buyer criteria against eligible mandate attributes",
                        "Baseline 200 minutes; machine displacement removes 170 manual minutes",
                        "Twenty-five review minutes resolve eligibility conflicts before buyer introduction",
                        "Fifty-five minutes remain after review; principal authorizes consequential introductions",
                    ],
                    [
                        "Document checking compares current evidence with asset-specific checklist requirements",
                        "Baseline 200 minutes; machine displacement removes 180 manual minutes",
                        "Twenty-five review minutes inspect material amounts and missing signatures",
                        "Forty-five minutes remain after review; unresolved conditions block progression",
                    ],
                    [
                        "Milestone tracking monitors deadlines and prepares accountable exception reminders",
                        "Baseline 150 minutes; machine displacement removes 140 manual minutes",
                        "Ten review minutes confirm changed deadlines and responsible counterparties",
                        "Twenty minutes remain after review; disputed dates require confirmation",
                    ],
                    [
                        "Distribution preparation assembles approved content for permissioned eligible recipients",
                        "Baseline 100 minutes; machine displacement removes 90 manual minutes",
                        "Ten review minutes inspect claims and recipient suppression synchronization",
                        "Twenty minutes remain after review; uncertain permissions stop delivery",
                    ],
                    [
                        "Reconciliation checks external receipts and resolves uncertain workflow states",
                        "Baseline 100 minutes; machine displacement removes 40 manual minutes",
                        "Ten review minutes inspect exceptions beyond ordinary reconciliation work",
                        "Seventy minutes remain after review; uncertain writes require investigation",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail and the next task, never the authority to promise or release funds.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create one exclusive-mandate evidence ledger with immutable entity identifiers, signed fee terms, licensing classifications, and versioned introduction records.",
        "Deploy an authenticated, durable, idempotent webhook path and test duplicate events, signature failures, timeouts, and manual recovery before external use.",
        "Separate federal direct-transfer rules from state credit placement rules, and require evidence-backed eligibility before matching executable opportunities.",
        "Configure human authorization for material claims, first introductions, changed deadlines, settlement instructions, and every consequential document exception.",
        "Run the fixed 1,000-minute workload experiment, record corrections and review time, and verify the net reduction rather than counting generated outputs.",
        "Reconcile retained commissions, run costs, contractor capacity, failed-closing exposure, and cash timing to the three canonical annual profit scenarios.",
    ],
    "statutory_citations": [
        {
            "title": "26 U.S.C. § 6418 — Transfer of certain credits",
            "url": "https://www.law.cornell.edu/uscode/text/26/6418",
            "relevance": (
                "Establishes eligible credit transfers, unrelated-party and cash requirements, "
                "and the prohibition on a transferee subsequently transferring the purchased credit."
            ),
        },
        {
            "title": "26 CFR § 1.6418-2 — Rules for making transfer elections",
            "url": "https://www.ecfr.gov/current/title-26/section-1.6418-2",
            "relevance": (
                "Supports the federal direct-transfer checklist, including election procedures, "
                "transfer documentation, and related reporting mechanics."
            ),
        },
        {
            "title": "26 CFR § 1.6418-4 — Additional information and registration",
            "url": "https://www.ecfr.gov/current/title-26/section-1.6418-4",
            "relevance": (
                "Provides pre-filing registration requirements; a registration number alone "
                "does not establish substantive credit eligibility."
            ),
        },
        {
            "title": "26 U.S.C. § 47 — Rehabilitation credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/47",
            "relevance": (
                "Identifies the federal rehabilitation credit that must be distinguished "
                "from separately transferable state historic rehabilitation incentives."
            ),
        },
        {
            "title": "15 U.S.C. § 78o — Registration and regulation of brokers and dealers",
            "url": "https://www.law.cornell.edu/uscode/text/15/78o",
            "relevance": (
                "Section 15(a) establishes broker registration requirements; Section 15(b)(13) "
                "contains a conditional M&A broker exemption rather than a universal exemption "
                "for transaction introductions."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Governs commercial email practices including header accuracy, subject lines, "
                "sender information, opt-out mechanisms, and timely suppression."
            ),
        },
    ],
}
