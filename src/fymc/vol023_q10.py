from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "mineral-rights-automation-ai-leverage-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) mineral rights team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Royalty Ledgers, NMA/NPRI Evidence Graphs, Pooling-Docket Alerts, and Buyer Distribution Under Texas Natural Resources Code Section 91.402",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #7, Mineral Rights, ranks #25 with a 81/100 Money-to-Manpower Score: "
        "automation improves evidence throughput, but capital, depletion, and title still control returns. "
        "This chapter maps five plays: NMA acquisitions, NPRI underwriting, pooling-docket positioning, "
        "royalty recovery, and institutional flips. A 1 FT + 3 C pod uses Python ingestion, "
        "source-linked LLM extraction, production alerts, and permissioned buyer distribution to target "
        "70% repetitive-work reduction without delegating title conclusions or binding commitments. "
        "Canonical annual owner profits remain $6,000 Conservative, $69,875 Base, and $180,000 Scaled; "
        "the Scaled case requires 2 FT + 4 C. Build the flywheel around verified exceptions and "
        "reusable diligence, not bulk owner solicitation. Every automated result needs provenance, "
        "a recovery path, and an accountable reviewer."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$30,000",
            "context": "Annual royalty receipts and realized rights-trading gains, excluding returned basis",
            "note": "20% margin; $6,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$215,000",
            "context": "Annual royalty receipts and realized rights-trading gains, excluding returned basis",
            "note": "32.5% margin; $69,875 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$400,000",
            "context": "Annual royalty receipts and realized rights-trading gains, excluding returned basis",
            "note": "45% margin; $180,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build one evidence pipeline for five mineral-rights plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with five explicit work queues rather than five disconnected software products. "
                    "NMA acquisitions convert severed mineral ownership into tract-level purchase candidates; "
                    "NPRI underwriting separates royalty participation from executive and leasing rights; "
                    "pooling-docket positioning identifies public procedural developments before underwriting "
                    "assumptions become stale; royalty recovery reconciles contracted economics against actual "
                    "payments; institutional flips package verified interests for repeat buyers. These are this "
                    "chapter's five mapped plays, with production monitoring serving all five. The full-time "
                    "principal owns investment decisions, seller relationships, and cash authorization. Three "
                    "contractor seats cover land/title work, petroleum and royalty analysis, and automation "
                    "operations; licensed counsel handles legal interpretation within the land/title service "
                    "scope where required. Define contractor deliverables and availability explicitly, because "
                    "three contractors do not equal three full-time employees. Use one shared asset identifier "
                    "but separate tract, deed, lease, well, unit, interest, and payment entities. A well can "
                    "cross multiple tracts, and a tract can participate in multiple units. Flattening those "
                    "relationships into one spreadsheet row silently corrupts both royalty decimals and "
                    "acquisition rankings. Begin in one county and one operator population so the pod learns "
                    "source quirks before increasing geographic coverage. Require every opportunity to identify "
                    "its primary play, evidence owner, and next human decision."
                ),
                (
                    "Implement ingestion with Python's urllib.request, csv, json, hashlib, sqlite3, decimal, "
                    "and datetime modules. A scheduler retrieves licensed feeds, permitted public downloads, "
                    "and owner-authorized statement exports; it never bypasses access controls or assumes a "
                    "public webpage permits unlimited scraping. Enverus or an operator portal can be a source "
                    "when the subscription permits the intended use, while Texas Railroad Commission downloads "
                    "supply public production and regulatory observations. Store the original artifact, retrieval "
                    "time, source URL, content hash, reporting period, and parser version before extraction. "
                    "For PDF images, call a contracted OCR endpoint through HTTPS rather than pretending the "
                    "standard library can reliably extract scanned deed text. Pass OCR text to an LLM with "
                    "a constrained JSON schema requesting instrument number, parties, dates, legal description, "
                    "fractions, reservations, and supporting page spans. Treat document text as evidence, never "
                    "as executable instructions. Reject unexpected fields, oversized responses, invalid dates, "
                    "and fractions without their original wording. Use Decimal for money and Fraction for "
                    "recorded fractional interests; save the untouched expression alongside normalized values. "
                    "Land review resolves ambiguous conveyancing language rather than letting a model manufacture "
                    "a clean ownership percentage. Version accepted extractions so later corrections remain "
                    "traceable to their source and reviewer."
                ),
                (
                    "Receive vendor webhooks through an HTTPS endpoint with vendor-prescribed signature "
                    "verification, timestamp checks, replay protection, and an explicit payload-size limit. "
                    "Acknowledge only after a transaction durably records the event; a worker then processes "
                    "pending rows. Where signatures are unavailable, retrieve the authoritative object through "
                    "an authenticated API before trusting the notification. Build an idempotency key from "
                    "source, artifact hash, and event type, not simply the seller's name. Duplicate notices "
                    "must not create duplicate owners, payments, or offers. Separate immutable source records "
                    "from interpreted facts and investment hypotheses. For example, a recorded deed is a "
                    "source, a reviewer-approved conveyed fraction is an interpretation, and expected horizontal "
                    "development is a hypothesis. Link each fact to page coordinates or an exact source "
                    "excerpt, and expose those links beside every proposed action. A probabilistic extraction "
                    "score is useful for queue ordering but cannot establish marketable title. The automation "
                    "contractor maintains schemas and retry behavior; the land contractor accepts ownership "
                    "facts; the principal accepts economic assumptions. This separation lets the same evidence "
                    "support seller qualification, payment disputes, and buyer diligence without repeatedly "
                    "buying the same research or allowing one mistaken extraction to propagate invisibly "
                    "through every play. Weekly sampling checks whether that separation remains intact."
                ),
            ],
            "table": {
                "caption": "Five-Play Evidence Architecture and Shared Infrastructure Responsibilities",
                "headers": [
                    "Mapped play or shared operating component",
                    "Automated evidence preparation and routing work",
                    "Human decision retained by the pod",
                    "Specific failure condition requiring an exception",
                ],
                "rows": [
                    [
                        "NMA acquisition queue for severed mineral ownership",
                        "Join recorded instruments to tract identifiers and sellers",
                        "Land reviewer confirms conveyed ownership before principal pricing",
                        "Reservation language changes the modeled mineral ownership fraction",
                    ],
                    [
                        "NPRI underwriting queue for nonparticipating royalty interests",
                        "Extract royalty wording with original fractions and pages",
                        "Qualified reviewer interprets fixed versus floating royalty language",
                        "Lease royalty multiplication contradicts the recorded grant language",
                    ],
                    [
                        "Pooling docket positioning queue for public procedural changes",
                        "Match applications and orders against verified tract descriptions",
                        "Principal evaluates timing only after jurisdiction specific review",
                        "Application amendment removes acreage previously included in targeting",
                    ],
                    [
                        "Royalty recovery queue for statement and lease exceptions",
                        "Compare payment decimals and deductions against reviewed obligations",
                        "Royalty analyst validates claims before contacting operator personnel",
                        "Prior period adjustments explain the apparent payment shortfall",
                    ],
                    [
                        "Institutional flip queue for repeat buyer diligence packages",
                        "Assemble permissioned evidence indexes and buyer matching suggestions",
                        "Principal authorizes distribution and accepts binding transaction terms",
                        "Buyer access includes documents outside the seller permission",
                    ],
                    [
                        "Shared event ledger connecting every mapped operator play",
                        "Preserve source hashes and versioned reviewer acceptance records",
                        "Automation contractor releases tested parser and schema revisions",
                        "Duplicate notification attempts to recreate an accepted transaction",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the details that experienced mineral buyers inspect first",
                "body": "Speed comes from eliminating repeated evidence assembly, not from skipping instrument interpretation.",
                "items": [
                    "Store gross acres, conveyed mineral fraction, and resulting NMA separately; never label a normalized royalty acre calculation as NMA.",
                    "Capture fixed-versus-floating NPRI wording verbatim with the granting and reservation clauses, because isolated fractions can reverse the economic interpretation.",
                    "Resolve pooling notices by legal description and docket identifier; owner-name matching alone misses trusts, estates, and spelling variants.",
                    "Index suspense releases and prior-period adjustments separately from current production receipts so a catch-up check does not inflate the forward royalty curve.",
                ],
            },
        },
        {
            "heading": "2. Reconcile royalties and monitor production without inventing entitlement",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build royalty reconciliation around production month, product, well or allocation group, "
                    "payor, owner account, and statement revision. Cash date alone cannot explain an operator "
                    "payment. Ingest line-level volumes, price, gross sales, ownership decimal, taxes, deductions, "
                    "and adjustments using a source-specific field dictionary. Some statements report property "
                    "gross values while others already report the owner's share; multiplying an owner-level "
                    "amount by the royalty decimal again understates revenue. For an illustrative lease with "
                    "a reviewed 0.00125000 payment decimal, 10,000 barrels at $70 create $700,000 property "
                    "gross sales and $875 owner gross entitlement before applicable charges. If permitted "
                    "owner-level taxes and deductions total $95, the illustrative net is $780. The calculation "
                    "is a test fixture, not an additional scorecard revenue stream. Compare the modeled decimal "
                    "with the division order and reviewed lease or instrument analysis; none independently "
                    "resolves every title issue. Texas Natural Resources Code Section 91.402 supplies payment "
                    "timing rules and specified exceptions, so the queue must distinguish delayed remittance "
                    "from title-related suspense before generating correspondence. Require the royalty analyst "
                    "to attach statement lines, contractual support, and the reconciliation bridge to any "
                    "proposed recovery request. Record disputed amounts separately until collected or otherwise "
                    "recognized under the established accounting policy."
                ),
                (
                    "Production monitoring should detect changed evidence, not promise early knowledge of "
                    "future drilling. Maintain separate dates for production month, filing date, retrieval "
                    "date, and revision date. Texas Railroad Commission oil reporting can be lease-level, "
                    "while other datasets use well-level records; never manufacture well precision by spreading "
                    "lease volumes equally. Preserve API identifiers, operator changes, unit relationships, "
                    "and allocation methods. A Python job compares the latest accepted series with its prior "
                    "version, checks missing periods, and calculates rolling changes only across comparable "
                    "units and products. Trigger review when volumes fall materially against a documented "
                    "baseline, when a previously inactive interest receives production, or when reported "
                    "production diverges from paid volumes beyond the expected payment lag. Thresholds should "
                    "reflect asset history and reporting cadence rather than a universal percentage. The "
                    "petroleum contractor distinguishes normal decline, downtime, workovers, reporting revisions, "
                    "and allocation changes before updating the underwriting curve. Keep commodity price "
                    "changes separate from physical depletion: a revenue increase can conceal falling "
                    "production. Route confirmed findings into acquisition valuations, NPRI cash-flow models, "
                    "recovery cases, and buyer updates, but preserve their observation dates so institutional "
                    "buyers can reproduce the conclusion. Stale inputs should visibly reduce confidence "
                    "rather than quietly inherit yesterday's accepted status."
                ),
                (
                    "For pooling-docket curve-jumping, monitor public applications, hearing settings, amendments, "
                    "orders, and subsequent development evidence as distinct events. Oklahoma Corporation "
                    "Commission proceedings and Texas Railroad Commission proceedings operate under different "
                    "statutes and procedures; a generic pooling label is insufficient. Have the land/title "
                    "contractor identify the governing jurisdiction, instrument, acreage, affected interests, "
                    "and any election deadline from the actual documents. An application is not an order, "
                    "an order is not a drilled well, and a permit is not a royalty payment. The principal "
                    "may reprioritize research when a public event changes the opportunity set, but the system "
                    "must not auto-submit elections, waive rights, or send binding acquisition terms. Track "
                    "deadlines with both a normalized date and the source language, including service facts "
                    "that affect the calculation. For a changed or withdrawn filing, invalidate dependent "
                    "alerts and send a correction to internal recipients. The same event history becomes "
                    "a buyer-facing diligence timeline only after review and permission checks. This is "
                    "how public procedural information supports distribution without turning uncertain "
                    "development assumptions into sales claims. Maintain a daily human review calendar "
                    "for active deadlines even when automated monitoring appears healthy, and designate "
                    "a backup reviewer before the primary contractor becomes unavailable."
                ),
            ],
            "table": {
                "caption": "Royalty and Production Exception Matrix for Reproducible Decisions",
                "headers": [
                    "Observed exception within the mineral evidence stream",
                    "Deterministic check performed before human interpretation",
                    "Reviewer evidence required before external communication",
                    "Recovery action preserving the accepted historical record",
                ],
                "rows": [
                    [
                        "Payment decimal differs from the accepted interest model",
                        "Compare exact decimals without rounding away material differences",
                        "Attach division order and reviewed lease calculation support",
                        "Suspend the proposed claim until ownership interpretation resolves",
                    ],
                    [
                        "Statement deduction exceeds the reviewed contractual treatment",
                        "Group charge codes by product and production month",
                        "Inspect lease language and applicable jurisdictional treatment first",
                        "Reclassify unsupported mappings while retaining original statement codes",
                    ],
                    [
                        "Reported production drops sharply against comparable accepted periods",
                        "Separate missing filings from actual reported zero volumes",
                        "Petroleum reviewer examines downtime and operator reporting revisions",
                        "Refresh the curve only after documenting the explanation",
                    ],
                    [
                        "Suspense release produces an unusually large cash receipt",
                        "Match receipt components against their historical production months",
                        "Royalty analyst distinguishes catchup payments from recurring economics",
                        "Exclude catchup distortion from forward monthly production forecasts",
                    ],
                    [
                        "Pooling application changes acreage after the first alert",
                        "Compare amended legal descriptions with the prior version",
                        "Land reviewer confirms affected tracts and deadline consequences",
                        "Invalidate dependent alerts and issue traceable internal corrections",
                    ],
                    [
                        "Buyer diligence finds competing versions of production evidence",
                        "Display retrieval dates and source revision relationships together",
                        "Analyst selects the supported series with documented reasoning",
                        "Publish a corrected package with prior access history",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before money, rights, or external representations move",
                "body": "Automation prepares the record; named reviewers authorize consequential outputs.",
                "items": [
                    "Verify tract identity, conveyed interest, lease relationship, and unresolved title exceptions against source instruments before issuing a purchase proposal.",
                    "Reconcile every proposed royalty claim to statement lines, reviewed payment decimals, applicable charges, and actual adjustment history.",
                    "Confirm docket status, governing jurisdiction, source-backed deadlines, and reviewer coverage before relying on a pooling event.",
                    "Check recipient permissions, current valuation assumptions, documentary support, and principal authorization before releasing a buyer package or binding terms.",
                ],
            },
        },
        {
            "heading": "3. Prove the automation rate and price every exception",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Measure the 70% target against repetitive-work minutes, not the percentage of records "
                    "that touched an LLM. Establish a manual baseline separately for research collection, "
                    "qualification preparation, diligence fulfillment, and acquisition-channel administration. "
                    "An illustrative monthly pilot processes 1,000 tasks that previously required six minutes "
                    "each, or 6,000 minutes. Suppose 800 tasks pass deterministic checks and 200 need "
                    "six-minute exception handling. Sample 80 of the passed tasks for six-minute human reviews, "
                    "then reserve 120 minutes for monitoring and maintenance. Retained work totals 1,200 "
                    "plus 480 plus 120, or 1,800 minutes; the reduction is exactly 70%. Acquisition judgment, "
                    "title conclusions, negotiations, and cash authorization remain outside this repetitive "
                    "task denominator. Publish results by queue as well as in aggregate so easy document "
                    "downloads cannot conceal poor royalty accuracy. Stratify samples across sources, parsers, "
                    "interest types, and monetary exposure, and inspect every consequential output even when "
                    "its preparatory extraction passed. Expand review when errors cluster. If exception "
                    "handling takes twelve minutes rather than six, the same pilot retains 3,000 minutes "
                    "and saves only 50%. That sensitivity makes exception design a more important "
                    "investment than adding another model to an already fragile workflow."
                ),
                (
                    "Price model calls as explicit planning assumptions rather than current vendor quotations. "
                    "Assume one run consumes 5,000 input tokens at $2 per million and 800 output tokens "
                    "at $8 per million: model cost is $0.0164. Add $0.0100 for allocated OCR and transport, "
                    "producing $0.0264 variable cost per run. Two runs per task across 1,000 tasks cost "
                    "$52.80 monthly. Add $75 for scheduled hosting, storage, and monitoring, then value "
                    "the pilot's thirty retained labor hours at an illustrative blended $60 hourly, or "
                    "$1,800. Total monthly workflow cost becomes $1,927.80, equivalent to $1.9278 per "
                    "completed task and $23,133.60 annually. Vendor and platform cost alone is $127.80 "
                    "monthly; cheap tokens do not make exception labor disappear. This budget excludes "
                    "acquisition capital, title projects outside the measured workflow, licensed data "
                    "subscriptions, and transaction-specific counsel. Allocate those separately within the "
                    "business case. Do not charge retained contractor labor twice if the same hours already "
                    "sit in the operating budget. Cache accepted extraction results by artifact hash and "
                    "parser version, cap retries, and route repeated failures to review. A second model "
                    "call is useful only when it improves a measured error class."
                ),
                (
                    "Keep the canonical economics fixed while allocating the proposed workflow inside them. "
                    "Conservative revenue is $30,000 with $24,000 implied total costs and $6,000 owner "
                    "profit at 20%; Base revenue is $215,000 with $145,125 costs and $69,875 profit at "
                    "32.5%; Scaled revenue is $400,000 with $220,000 costs and $180,000 profit at 45%. "
                    "The first two cases use 1 FT + 3 C; Scaled uses 2 FT + 4 C. These are annual "
                    "business scenarios, not outputs generated by the illustrative token model. The "
                    "pilot's $23,133.60 annual workflow allocation fits within Base costs but would consume "
                    "almost the entire Conservative cost allowance, so that case needs a smaller workload "
                    "and budget. Monthly operating overhead of $1,000–$12,000 is a separate planning "
                    "range, not a substitute for total scenario costs. Startup capital remains "
                    "$15,000–$75,000 and time to first deal remains 3–9 months. Revenue means royalty "
                    "receipts plus realized rights-trading gains excluding returned basis; gross sale "
                    "proceeds and underlying producer sales are different measures. Track depletion "
                    "analysis under 26 U.S.C. Sections 611 and 613A separately from operational yield "
                    "metrics, and have the tax preparer determine eligibility and treatment rather than "
                    "letting the workflow infer deductions from a generic percentage."
                ),
            ],
            "table": {
                "caption": "Pilot Cost Controls and Financial Boundaries Without Revenue Inflation",
                "headers": [
                    "Measured component or canonical economic boundary",
                    "Explicit calculation used in the operating model",
                    "Interpretation retained in the management reporting view",
                    "Action when actual performance breaks the assumption",
                ],
                "rows": [
                    [
                        "Manual baseline for one thousand repetitive monthly tasks",
                        "One thousand tasks multiplied by six minutes each",
                        "Six thousand minutes excludes consequential investment decision work",
                        "Rebaseline changed task scope before claiming further savings",
                    ],
                    [
                        "Retained exception sampling and maintenance effort each month",
                        "Twelve hundred plus four hundred eighty plus one hundred twenty minutes",
                        "Eighteen hundred retained minutes yields seventy percent reduction",
                        "Increase staffing estimates when exception durations exceed assumptions",
                    ],
                    [
                        "Illustrative variable cost for each automated processing run",
                        "Model cost of $0.0164 plus allocated services of $0.0100",
                        "Each run costs $0.0264 before platform and labor",
                        "Cap repeated attempts and inspect the failing source",
                    ],
                    [
                        "Illustrative full monthly workflow expense for Base planning",
                        "Variable $52.80 plus platform $75 plus labor $1,800",
                        "Monthly $1,927.80 allocation includes the measured retained labor",
                        "Avoid duplicating contractor hours already booked elsewhere internally",
                    ],
                    [
                        "Conservative and Base canonical annual owner profit boundaries",
                        "$30,000 less $24,000 and $215,000 less $145,125 respectively",
                        "Owner profits remain $6,000 and $69,875 respectively each year",
                        "Reduce workflow scale rather than silently increasing scenario revenue",
                    ],
                    [
                        "Scaled canonical annual profit and required staffing boundary",
                        "$400,000 recognized revenue less $220,000 total scenario costs",
                        "$180,000 owner profit requires two full time plus four contractors",
                        "Add capacity only when actual workload supports the expansion",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Baseline the actual repetitive work",
                    "action": "Time a representative sample in all four workflow categories.",
                    "detail": "Record source, task type, minutes, reviewer, and rework; keep investment decisions outside the automation denominator.",
                },
                {
                    "step": 2,
                    "title": "Replay without external effects",
                    "action": "Run archived documents through versioned extraction and reconciliation.",
                    "detail": "Compare outputs against reviewer-accepted fixtures before enabling live queue updates, seller correspondence, or buyer notifications.",
                },
                {
                    "step": 3,
                    "title": "Pilot with explicit labor and spend limits",
                    "action": "Track successful tasks, exceptions, sampled errors, tokens, and retained minutes.",
                    "detail": "Calculate cost per completed task, not merely per API request, and include monitoring and recovery labor.",
                },
                {
                    "step": 4,
                    "title": "Expand only the verified workflow",
                    "action": "Approve a larger batch after reviewing accuracy and net time saved.",
                    "detail": "Keep binding terms, title conclusions, rights elections, and money movement under named human authorization at every volume.",
                },
            ],
        },
        {
            "heading": "4. Turn verified work into distribution and recover cleanly from failures",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the acquisition flywheel from reusable explanations of observed owner problems. "
                    "A reviewed royalty discrepancy can become an anonymized statement-reading guide; a "
                    "verified tract research process can become a county-specific diligence checklist; "
                    "a production revision can become an educational example explaining reporting lag. "
                    "Publish only aggregated or permissioned information, removing owner identifiers and "
                    "confidential instrument annotations. Programmatic pages should add original utility: "
                    "local source links, an explanation of NMA versus NPRI, reporting cadence, and a "
                    "clear intake path. Do not generate thousands of nearly identical acreage pages "
                    "or publish speculative ownership claims as facts. Use source-linked draft generation "
                    "followed by the relevant contractor's review and the principal's publication decision. "
                    "The traffic loop is article, useful calculator or checklist, voluntary owner inquiry, "
                    "qualified evidence request, verified opportunity, and another permissioned educational "
                    "asset. A shareable royalty reconciliation template can support referrals without "
                    "exposing a user's uploaded statement or creating a public owner leaderboard. Measure "
                    "qualified inquiries and verified opportunities per published asset rather than raw "
                    "visits. These assets support NMA acquisitions, NPRI qualification, and royalty recovery "
                    "while leaving docket positioning dependent on primary public records rather than "
                    "attention metrics. Schedule updates when source procedures change, and retire pages "
                    "whose operational guidance can no longer be verified."
                ),
                (
                    "For outbound distribution, separate owner acquisition from institutional buyer placement. "
                    "Owner outreach should use verified contact provenance, restrained cadence, accurate "
                    "identity, and a suppression list shared across campaigns. Commercial email must "
                    "follow 15 U.S.C. Section 7704 requirements, including accurate routing information, "
                    "nondeceptive subjects, required identification and address information, and functioning "
                    "opt-out handling. Do not convert a purchased list into automated calling or texting "
                    "without evaluating the distinct rules for those channels. Institutional buyers "
                    "receive a reviewed teaser matched to explicit preferences for basin, interest "
                    "type, check size, producing status, and evidence completeness. Release detailed "
                    "documents through recipient-specific access with an expiration date and an access "
                    "log. The loop is buyer feedback, improved qualification rules, better diligence "
                    "packages, shorter clarification cycles, and more repeat buyer engagement. Treat "
                    "referral incentives as a separate operating decision requiring review of transaction "
                    "structure and applicable licensing rules. If outside capital is pooled, assess "
                    "securities implications before soliciting investors; 15 U.S.C. Section 77b "
                    "expressly addresses fractional undivided interests in oil, gas, or other mineral "
                    "rights within its securities definition. A productive asset story does not remove "
                    "those questions. Distribution automation ranks recipients and drafts communications; "
                    "the principal authorizes actual offers, releases, and material representations."
                ),
                (
                    "Make recovery visible enough that the four-person pod can operate through vendor "
                    "outages without losing deadlines. Maintain pending, processing, accepted, rejected, "
                    "and quarantined event states with attempt counts and last-error categories. Retry "
                    "temporary network failures with bounded exponential backoff; quarantine schema "
                    "changes, signature failures, contradictory fractions, and source access problems "
                    "instead of retrying them indefinitely. If an LLM endpoint fails, continue deterministic "
                    "CSV reconciliation and route scanned instruments to manual review. If a production "
                    "feed stalls, label affected observations stale and stop automated valuation "
                    "refreshes while retaining the last accepted version. If outbound delivery fails, "
                    "reconcile provider delivery identifiers before resending so the same owner or "
                    "buyer does not receive repeated messages. Back up the database and original "
                    "artifacts, test restoration, and maintain a daily export of active deadlines "
                    "and high-value exceptions. Assign a secondary reviewer for urgent title and "
                    "docket questions; software availability cannot substitute for qualified coverage. "
                    "Review the complete flywheel weekly: research throughput, exception age, correction "
                    "rate, qualified inquiries, accepted buyer packages, collected royalties, and "
                    "realized trading gains. Increase automation only where accepted evidence remains "
                    "reproducible and retained labor actually falls. The objective is a smaller "
                    "distance between reliable facts and authorized action, not a larger volume "
                    "of unreviewed machine output."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheel Controls and Failure-Recovery Runbook",
                "headers": [
                    "Growth surface or operational failure being managed",
                    "Automated action allowed within the defined workflow",
                    "Human review and evidence needed before release",
                    "Fallback that protects relationships and decision quality",
                ],
                "rows": [
                    [
                        "County specific educational pages attracting qualified owner inquiries",
                        "Draft source linked explanations from accepted research templates",
                        "Contractor checks accuracy and principal authorizes public publication",
                        "Unpublish stale guidance until source procedures are reverified",
                    ],
                    [
                        "Shareable royalty worksheet generating voluntary referrals from owners",
                        "Create clean templates without embedded owner payment information",
                        "Reviewer tests formulas against accepted statement example fixtures",
                        "Disable sharing when uploaded documents could become exposed",
                    ],
                    [
                        "Owner outreach sequence supporting disciplined acquisition qualification",
                        "Prepare drafts using verified contacts and suppression checks",
                        "Principal verifies identity claims and permitted channel use",
                        "Stop sends immediately when suppression synchronization becomes unreliable",
                    ],
                    [
                        "Institutional buyer matching for reviewed rights sale packages",
                        "Rank buyers against explicit basin and interest preferences",
                        "Principal approves recipient access and material package representations",
                        "Revoke incorrect access and investigate affected document exposure",
                    ],
                    [
                        "Model or OCR outage affecting scanned instrument interpretation",
                        "Continue deterministic processing for unaffected structured source records",
                        "Land reviewer manually handles urgent source instrument questions",
                        "Queue remaining scans without inventing missing extracted fields",
                    ],
                    [
                        "Production feed interruption during an active acquisition review",
                        "Mark observations stale and preserve accepted prior versions",
                        "Petroleum reviewer assesses whether fresh evidence is essential",
                        "Pause valuation refreshes while monitoring public sources manually",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail, not the judgment that turns a mineral interest into a binding commitment.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create five tagged queues for NMA acquisitions, NPRI underwriting, pooling-docket positioning, royalty recovery, and institutional flips, each with a named reviewer.",
        "Implement immutable source storage, artifact hashes, versioned extractions, and idempotent event processing before connecting any external messaging workflow.",
        "Replay royalty statements against accepted test fixtures covering owner-level amounts, payment decimals, deductions, suspense releases, and prior-period adjustments.",
        "Measure a representative repetitive-task baseline and report retained exception, sampling, and maintenance minutes before claiming 70% automation.",
        "Budget model calls, OCR, platform costs, contractor review, licensed data, and transaction work inside the unchanged canonical scenario cost allowances.",
        "Launch one reviewed educational resource and one permissioned buyer-package workflow, then test stale-feed handling, suppression synchronization, and database restoration.",
    ],
    "statutory_citations": [
        {
            "title": "Texas Natural Resources Code Section 91.402 — Time for Payment of Proceeds",
            "url": "https://statutes.capitol.texas.gov/Docs/NR/htm/NR.91.htm#91.402",
            "relevance": "Supports Texas royalty payment timing analysis and identification of specified withholding exceptions before generating a payment inquiry.",
        },
        {
            "title": "26 U.S.C. Section 611 — Allowance of Deduction for Depletion",
            "url": "https://www.law.cornell.edu/uscode/text/26/611",
            "relevance": "Establishes the depletion deduction framework that tax reviewers evaluate separately from operating cash yield and scorecard revenue.",
        },
        {
            "title": "26 U.S.C. Section 613A — Limitations on Percentage Depletion in Case of Oil and Gas Wells",
            "url": "https://www.law.cornell.edu/uscode/text/26/613A",
            "relevance": "Provides oil and gas percentage depletion limitations and exceptions requiring taxpayer-specific review rather than automatic application of a generic rate.",
        },
        {
            "title": "15 U.S.C. Section 7704 — Other Protections for Users of Commercial Electronic Mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email practices relevant to owner outreach and buyer distribution, including identification, address, and opt-out requirements.",
        },
        {
            "title": "15 U.S.C. Section 77b(a)(1) — Definition of Security",
            "url": "https://www.law.cornell.edu/uscode/text/15/77b",
            "relevance": "Includes fractional undivided interests in oil, gas, or other mineral rights within the statutory securities definition, informing review of offering structures.",
        },
        {
            "title": "Texas Natural Resources Code Chapter 102 — Mineral Interest Pooling",
            "url": "https://statutes.capitol.texas.gov/Docs/NR/htm/NR.102.htm",
            "relevance": "Provides Texas mineral interest pooling provisions that must be distinguished from other jurisdictions when interpreting applications, orders, and affected interests.",
        },
    ],
}
