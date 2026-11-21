from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 2 FT + 3 C (5 people) government surplus auctions team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Auction Alerts, Evidence-Linked Bid Limits, SF-97 Document Control, DEMIL Screening, and B2B Inventory-to-Buyer Loops",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #17, Government Surplus Auctions, ranks #26 with a Money-to-Manpower "
        "Score of 62/100: automation must reduce clerical drag without disguising capital "
        "and handling intensity. This chapter maps six operator plays: auction discovery, "
        "evidence qualification, bid-limit underwriting, removal coordination, inventory "
        "remarketing, and buyer reactivation. A 2 FT + 3 C pod uses Python collectors, "
        "structured LLM extraction, deterministic worksheets, and exception queues to "
        "target 70%+ automation of measured repetitive tasks. Humans retain bidding, "
        "condition, title, restricted-item, and release decisions. Canonical annual owner "
        "profits remain $12,000 Conservative, $80,500 Base, and $200,000 Scaled; the "
        "Scaled case requires 3 FT + 4 C. Evidence-linked listings and segmented B2B "
        "outreach create repeatable distribution without treating auction principal, "
        "unrealized inventory value, or buyer deposits as additional revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross resale proceeds; acquisition, transport, and refurbishment included in margin",
            "note": "8% net margin; $12,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$575,000",
            "context": "Annual gross resale proceeds; acquisition, transport, and refurbishment included in margin",
            "note": "14.0% net margin; $80,500 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual gross resale proceeds; acquisition, transport, and refurbishment included in margin",
            "note": "20% net margin; $200,000 annual owner net profit; 3 FT + 4 C (7 people)",
        },
    ],
    "sections": [
        {
            "heading": "1. Instrument six operator plays before automating the auction inbox",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the operating system around six mapped plays: auction discovery, "
                    "evidence qualification, bid-limit underwriting, removal coordination, "
                    "inventory remarketing, and buyer reactivation. These are this chapter's "
                    "execution labels, not six separate revenue businesses. The first full-time "
                    "operator owns sourcing, underwriting, and purchase authorization; the "
                    "second owns inventory, sales, and collection. Assign the three contractors "
                    "to inspection, transport, and refurbishment or specialist documentation, "
                    "with written availability rather than assumed daily coverage. Contractors "
                    "can contribute evidence but cannot silently change a bid ceiling or "
                    "release an asset. Every lot receives a stable internal identifier linked "
                    "to platform, seller, auction identifier, lot identifier, and original URL. "
                    "GSA Auctions, GovPlanet, GovDeals, and Public Surplus differ in seller "
                    "relationships, documents, fees, and pickup procedures; record the actual "
                    "seller instead of inferring federal ownership from the platform name. "
                    "Store source snapshots, retrieval timestamps, and document hashes alongside "
                    "normalized fields. A Python sqlite3 database is sufficient for one "
                    "controlled writer; use a transaction-backed shared database when multiple "
                    "workers must reserve the same stock. The central design objective is "
                    "one accountable asset record, not an elaborate dashboard that reproduces "
                    "contradictory spreadsheets across five people's inboxes."
                ),
                (
                    "Acquire listings through seller-provided alerts, permitted exports, and "
                    "documented interfaces where available. Do not assume these auction "
                    "platforms provide public bid APIs or outgoing webhooks. A mailbox "
                    "collector can use imaplib and email to ingest alerts; urllib.request "
                    "can retrieve permitted resources with explicit timeouts and rate limits. "
                    "Persist raw messages before parsing, then emit your own signed internal "
                    "event for a newly observed or changed lot. Validate its signature, "
                    "timestamp, body size, and event identifier before processing. Use "
                    "hashlib.sha256 over stable source identifiers and content to separate "
                    "duplicate deliveries from genuine revisions. Auction closing times need "
                    "zoneinfo time zones and daylight-saving handling, not server-local "
                    "arithmetic. Keep the advertised closing time separate from the latest "
                    "observed extension; soft-close behavior makes an early snapshot unsuitable "
                    "for final bidding. A seller's changed removal deadline should create "
                    "an exception immediately, even when the title and asking price remain "
                    "unchanged. If collection fails, retain the last successful snapshot, "
                    "mark freshness explicitly, and send the sourcing operator a direct "
                    "link for manual review. Never let a failed fetch look like an "
                    "empty auction or permission to reuse stale terms."
                ),
                (
                    "Define the automation denominator before claiming seventy percent. "
                    "Instrument repeatable digital task instances, such as deduplication, "
                    "field extraction, worksheet recalculation, pickup reminders, listing "
                    "draft creation, and buyer-segment assignment. In an illustrative "
                    "two-week sample of 200 eligible instances, 144 completed without "
                    "manual editing yields 72% straight-through task completion. Count "
                    "a task requiring correction as assisted, even if software produced "
                    "most of the draft. Report human-review minutes, exception frequency, "
                    "and rework separately; this result does not mean seventy-two percent "
                    "of total labor, inspection, loading, or judgment disappeared. Keep "
                    "consequential decisions outside that denominator and report their "
                    "counts visibly so the metric cannot improve through selective "
                    "omission. Initially inspect every extraction, then reduce sampling "
                    "only for low-risk fields after measured accuracy supports the change. "
                    "Continue reviewing fees, deadlines, identifiers, restriction language, "
                    "and money before commitment. The weekly pod meeting should compare "
                    "automated completions with missed pickups, inventory aging, and "
                    "realized contribution per lot. A system that processes more alerts "
                    "while buying slower-moving equipment has accelerated the wrong "
                    "activity. Pause a failing play independently rather than disabling "
                    "inventory controls or buyer suppression with the entire workflow."
                ),
            ],
            "table": {
                "caption": "Six Mapped Operator Plays and Accountable Pod Ownership",
                "headers": [
                    "Mapped operator play",
                    "Automated work and retained evidence",
                    "Accountable human and consequential decision",
                    "Failure signal and practical recovery",
                ],
                "rows": [
                    [
                        "Play one: discover relevant federal and municipal auction lots",
                        "Collect permitted alerts, preserve source snapshots, and deduplicate revisions",
                        "Sourcing lead chooses categories, geography, and acceptable seller exposure",
                        "Stale collection timestamp triggers manual platform review before bidding",
                    ],
                    [
                        "Play two: qualify condition, eligibility, documents, and resale restrictions",
                        "Extract quoted facts with document references and explicit uncertainty flags",
                        "Inspection contractor verifies condition; sourcing lead resolves restriction questions",
                        "Conflicting identifiers suspend qualification until seller evidence resolves them",
                    ],
                    [
                        "Play three: calculate executable bid ceilings from landed economics",
                        "Recalculate Decimal worksheets using fees, freight, repairs, and reserves",
                        "Sourcing lead signs the version and submits authorized bids",
                        "Changed premium schedule invalidates the ceiling and requires recalculation",
                    ],
                    [
                        "Play four: coordinate payment, carrier booking, and timely removal",
                        "Generate reminders, appointment packets, release checklists, and deadline escalations",
                        "Operations lead confirms payment; transport contractor confirms equipment capacity",
                        "Unconfirmed pickup appointment triggers backup carrier calls before deadline",
                    ],
                    [
                        "Play five: track serialized stock and publish evidence-backed listings",
                        "Create asset records, draft descriptions, and synchronize availability events",
                        "Operations lead verifies condition claims and authorizes public listing",
                        "Duplicate reservation blocks release until stock ownership is reconciled",
                    ],
                    [
                        "Play six: reactivate buyers and compound qualified referral demand",
                        "Segment available inventory, prepare outreach, and record attributable introductions",
                        "Sales owner approves campaigns and handles negotiation with buyers",
                        "Suppression mismatch stops sending while recipient preferences are reconciled",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Automate the paperwork that experienced surplus operators distrust",
                "body": (
                    "The strongest shortcuts preserve provenance and surface exceptions "
                    "before cash, trucks, or customer promises become committed."
                ),
                "items": [
                    "Snapshot seller-specific payment and removal terms at review and again before bidding; platform branding does not standardize local pickup rules.",
                    "Request loading-door dimensions, forklift availability, dock height, and loading assistance in writing before calculating freight for oversized machinery.",
                    "Treat SF-97 availability, the actual vehicle identifier, and the destination state's title process as separate checks rather than one vehicle-document checkbox.",
                    "Record why qualified buyers reject a lot; missing voltage, dimensions, attachments, or test evidence often explains poor conversion better than price.",
                ],
            },
        },
        {
            "heading": "2. Separate probabilistic extraction from deterministic bid and release controls",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the LLM as a constrained evidence extractor, never as the "
                    "source of auction terms. Send a bounded document excerpt and request "
                    "a JSON object containing field name, extracted value, exact supporting "
                    "quotation, source location, and an uncertainty flag. Python json "
                    "parsing, explicit type checks, required-field validation, and allowlisted "
                    "units should reject malformed output. Treat seller descriptions, PDFs, "
                    "and emails as untrusted data: instructions embedded inside them must "
                    "not change the extraction policy, call tools, or publish listings. "
                    "Keep API credentials outside prompts, redact buyer details, and send "
                    "only the material required for the task. OCR can confuse vehicle "
                    "identifiers, decimal points, and equipment model suffixes, so compare "
                    "critical fields against photographed plates or original documents. "
                    "An absent SF-97 reference means documentary status requires review, "
                    "not that a certificate will accompany the sale. SF-97 supports "
                    "vehicle titling; it is not itself a state-issued title. Where a "
                    "DEMIL designation or controlled item is involved, record the applicable "
                    "seller conditions and verified disposition requirements. Do not "
                    "translate a code into unrestricted resale eligibility from memory. "
                    "Route unresolved items to the sourcing operator before any purchase "
                    "or external product claim."
                ),
                (
                    "Calculate bid ceilings with decimal.Decimal and an explicit fee "
                    "basis. For an illustrative equipment lot, assume realizable resale "
                    "proceeds of $12,000, freight of $900, refurbishment of $600, selling "
                    "costs of $600, a defect reserve of $800, and required contribution "
                    "of $2,200 before shared overhead. This leaves $6,900 for hammer "
                    "price plus buyer premium. With a 10% premium on hammer and no "
                    "acquisition tax in this example, the algebraic hammer ceiling is "
                    "$6,272.72 when rounded downward to cents. The executable ceiling "
                    "must be the highest permitted auction increment below that amount; "
                    "a $100 increment would cap the bid at $6,200. A verified tax "
                    "obligation, minimum premium, payment surcharge, or different taxable "
                    "base changes the formula and requires recalculation. Do not treat "
                    "the $2,200 contribution target as annual owner profit or an achieved "
                    "lot outcome. Attach freight quotes, comparable sales, and repair "
                    "assumptions to the worksheet version. Model restricted access, missing "
                    "attachments, and incomplete testing as costs or reasons to reject "
                    "the lot rather than allowing optimistic language to inflate the "
                    "resale estimate. The human bidder must see the current version "
                    "and remaining cash exposure before acting."
                ),
                (
                    "Implement a durable state machine: discovered, evidence collected, "
                    "qualified, bid authorized, won, removal scheduled, received, listed, "
                    "reserved, sold, and released. Rejected and disputed are explicit "
                    "branches, not deleted records. Each transition requires an actor, "
                    "timestamp, source version, and evidence appropriate to the action. "
                    "A generated email is not a sent email, a payment instruction "
                    "is not cleared payment, and a pickup reservation is not physical "
                    "receipt. Use an outbox table so a database commit and its pending "
                    "notification remain recoverable after a process crash. Retry safe "
                    "reads with capped exponential backoff; reconcile payment, reservation, "
                    "and publication status before retrying actions that could duplicate "
                    "commitments. For deadline-sensitive tasks, alert a named person rather "
                    "than trusting endless retries. The inspector uploads condition evidence, "
                    "the transport contractor confirms collection constraints, and the "
                    "operations lead reconciles received quantity and serial numbers "
                    "against the purchase record. Contractual removal dates remain "
                    "controlling unless the seller provides a written extension. Preserve "
                    "both the original deadline and authorized revision. The same "
                    "discipline prevents a vehicle with unresolved title documents from "
                    "being advertised as ready for immediate registration simply because "
                    "a listing template inserted that phrase."
                ),
            ],
            "table": {
                "caption": "Evidence, Bid Arithmetic, and Release Exception Controls",
                "headers": [
                    "High-consequence field or event",
                    "Machine validation and evidence requirement",
                    "Required human verification before commitment",
                    "Fallback when evidence remains unresolved",
                ],
                "rows": [
                    [
                        "Auction eligibility and bidder account match the actual seller",
                        "Store seller terms, registration status, and dated account evidence",
                        "Sourcing lead confirms eligibility before authorizing any purchase commitment",
                        "Exclude the lot until the seller confirms acceptable participation",
                    ],
                    [
                        "Vehicle identifier and SF-97 availability support intended titling route",
                        "Compare document identifiers with plate photographs and seller statements",
                        "Operations lead checks destination motor vehicle requirements and exceptions",
                        "Withhold registration claims and resolve documents before committing funds",
                    ],
                    [
                        "DEMIL designation or restricted property requires item-specific disposition review",
                        "Flag source restriction language and preserve original supporting documents",
                        "Sourcing lead verifies sale conditions and required specialist involvement",
                        "Reject unresolved lots rather than assuming unrestricted resale permission",
                    ],
                    [
                        "Buyer premium and taxable basis determine executable hammer ceiling",
                        "Apply versioned Decimal formulas and round down to allowed increments",
                        "Sourcing lead checks fee schedule against the current auction terms",
                        "Invalidate prior authorization when any material cost input changes",
                    ],
                    [
                        "Removal deadline and loading limitations determine feasible transport capacity",
                        "Calculate reminders from seller time zone and confirmed appointment",
                        "Transport contractor confirms vehicle, loading equipment, access, and schedule",
                        "Activate backup carrier or decline purchase before accepting impossible timing",
                    ],
                    [
                        "Outbound release requires matched inventory, buyer terms, and payment",
                        "Reconcile serial record, reservation status, and verified payment evidence",
                        "Operations lead authorizes release under documented collection risk policy",
                        "Hold the asset while resolving payment discrepancies or duplicate reservations",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before money or inventory moves",
                "body": (
                    "Automation may assemble the packet, but the accountable operator "
                    "records the final decision against the exact source version."
                ),
                "items": [
                    "Verify seller identity, bidder eligibility, applicable resale documentation, and item restrictions using current terms rather than a previous auction's packet.",
                    "Verify the bid ceiling includes buyer premium, applicable taxes, loading, transport, repairs, selling expense, and a realistic defect reserve.",
                    "Verify removal capacity with a confirmed appointment, suitable carrier equipment, named site contact, and an escalation path before the contractual deadline.",
                    "Verify serial numbers, condition claims, title-related documents, payment status, and the receiving party before publishing consequential claims or releasing inventory.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze and identify the evidence",
                    "action": "Save current auction terms, photographs, identifiers, and document hashes.",
                    "detail": "Assign a lot identifier and retain retrieval times so later revisions can be compared without overwriting the purchase basis.",
                },
                {
                    "step": 2,
                    "title": "Extract and validate the decision packet",
                    "action": "Run bounded extraction, validate structured output, and calculate landed costs.",
                    "detail": "Reject unsupported fields and route critical discrepancies to the sourcing lead with direct links to the underlying evidence.",
                },
                {
                    "step": 3,
                    "title": "Authorize the specific commercial action",
                    "action": "Record human authorization for the current ceiling, bid, publication, or release.",
                    "detail": "Invalidate authorization when material terms change; never carry a prior signature onto a modified document version.",
                },
                {
                    "step": 4,
                    "title": "Reconcile execution and close exceptions",
                    "action": "Compare platform results, receipts, physical inventory, and customer commitments.",
                    "detail": "Use manual platform checks during outages, then backfill audit events before restarting automated notifications and stock synchronization.",
                },
            ],
        },
        {
            "heading": "3. Turn verified inventory into programmatic, referral, and outbound distribution",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start the distribution flywheel at receiving, not after a listing "
                    "has failed. The inventory record should contain measured dimensions, "
                    "weight basis, voltage, serial number, attachments, testing method, "
                    "observed defects, title-related status, location, and loading constraints. "
                    "Generate a draft asset page from those fields and attach original "
                    "photographs that the business owns or is authorized to reuse. "
                    "The operations lead checks every condition assertion before publication. "
                    "Separate observed operation from full functional testing: a machine "
                    "that powers on has not demonstrated rated output under load. "
                    "Generate programmatic category pages only when they offer meaningful "
                    "inventory, buying criteria, or documented sold examples; thin pages "
                    "that substitute town names create maintenance work without helping "
                    "industrial buyers. Mark sold assets accurately, remove purchase "
                    "actions, and offer relevant available stock rather than baiting "
                    "buyers with unavailable bargains. Store page version and publication "
                    "identifier so a corrected voltage or defect disclosure can propagate "
                    "across the website and approved marketplaces. Do not delete adverse "
                    "condition evidence from the internal record when marketing copy "
                    "changes. Better evidence reduces repeated questions, improves freight "
                    "quoting, and gives procurement teams something concrete to circulate "
                    "internally before asking for a purchase order."
                ),
                (
                    "Build outbound around buyer fit and available inventory, not bulk "
                    "address volume. Maintain company-level segments such as municipal "
                    "fleet repair shops, warehouse operators, fabrication businesses, "
                    "equipment dealers, and educational laboratories. Capture category "
                    "interest, service geography, voltage requirements, loading capability, "
                    "and whether the buyer needs title-ready vehicles. An LLM can draft "
                    "a short message from approved facts, but deterministic rules must "
                    "exclude sold stock, suppressed recipients, and unsupported claims. "
                    "U.S. commercial email, including business-to-business messages, must "
                    "meet applicable requirements of 15 U.S.C. 7704, including accurate "
                    "headers, nondeceptive subject lines, required advertising identification, "
                    "a valid postal address, and a working opt-out mechanism. Honor "
                    "opt-outs within the statutory period and preserve suppression across "
                    "system migrations. Do not purchase scraped personal addresses or "
                    "use automated outreach to conceal sender identity. Start with "
                    "existing customers, inquiries, and appropriately sourced business "
                    "contacts; obtain permission before publicizing customer names or "
                    "purchase details. Cap outreach by the team's ability to answer "
                    "technical questions and arrange inspection. Measure qualified replies, "
                    "inspection bookings, paid orders, and gross resale proceeds attributable "
                    "to a campaign. Open rates are unreliable operational targets, "
                    "and a lead without payment is not recognized resale revenue."
                ),
                (
                    "The referral loop should make verification portable. After a "
                    "completed sale, send the buyer a concise asset packet with "
                    "operating observations, collection instructions already fulfilled, "
                    "and a shareable link to related available equipment. Ask whether "
                    "another location or purchasing colleague needs similar stock; "
                    "request an introduction instead of uploading the buyer's address "
                    "book. With permission, publish a factual case note explaining "
                    "the application, preparation performed, and logistics solved. "
                    "Avoid implying government endorsement merely because the asset "
                    "originated in a public auction. Track introductions with opaque "
                    "referral identifiers rather than personal information in URLs. "
                    "Feed sold prices, elapsed days, lost-sale reasons, and repeat "
                    "requests back into discovery filters and bid worksheets. If "
                    "buyers repeatedly need single-phase equipment while intake keeps "
                    "finding three-phase machines, adjust category qualification instead "
                    "of increasing email frequency. Reserve inventory atomically when "
                    "a serious buyer enters the agreed sales process, and give "
                    "reservations an explicit expiry. A stock change should update "
                    "the website, marketplace queue, and planned outreach before the "
                    "next campaign runs. This closes the flywheel: trustworthy "
                    "evidence attracts qualified demand, demand improves acquisition "
                    "selection, and better selection reduces unsold stock consuming "
                    "the pod's limited cash and handling capacity."
                ),
            ],
            "table": {
                "caption": "Evidence-Led Distribution Loops for Physical Surplus Inventory",
                "headers": [
                    "Distribution loop and intended buyer",
                    "Reusable evidence or automated production",
                    "Human review and operating constraint",
                    "Outcome measured beyond superficial traffic",
                ],
                "rows": [
                    [
                        "Programmatic equipment pages serve buyers searching exact operating specifications",
                        "Render verified dimensions, voltage, attachments, defects, and availability automatically",
                        "Operations lead checks claims and prevents duplicate low-value pages",
                        "Track qualified inquiries and paid orders per available asset",
                    ],
                    [
                        "Marketplace syndication reaches category buyers outside the owned website",
                        "Prepare channel-specific drafts with consistent serial records and photographs",
                        "Sales owner confirms permitted posting methods and current selling fees",
                        "Measure realized proceeds after channel costs and handling effort",
                    ],
                    [
                        "Segmented inventory email reaches appropriate existing and sourced business contacts",
                        "Match verified stock against recorded geography and equipment requirements",
                        "Sales owner checks suppression, sender information, and campaign capacity",
                        "Count qualified replies, inspections booked, and attributable completed sales",
                    ],
                    [
                        "Buyer referral packets help purchasing colleagues evaluate similar equipment",
                        "Create shareable asset links without exposing private customer information",
                        "Sales owner requests introductions and permission for customer references",
                        "Attribute introduced accounts and repeat purchases to originating relationships",
                    ],
                    [
                        "Sold equipment case notes demonstrate preparation and logistics competence",
                        "Assemble factual timelines from inspection, refurbishment, and collection records",
                        "Operations lead removes private details and unsupported endorsement implications",
                        "Track relevant inbound inquiries rather than general social engagement",
                    ],
                    [
                        "Buyer demand feedback improves future discovery and bid discipline",
                        "Aggregate rejected specifications, requested categories, and observed selling times",
                        "Sourcing lead revises filters without extrapolating from one conversation",
                        "Compare inventory aging, purchase accuracy, and realized lot contribution",
                    ],
                ],
            },
        },
        {
            "heading": "4. Price automated runs, rehearse recovery, and scale within the scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price automation per accepted result, not merely per API request. "
                    "For an illustrative extraction run, assume 6,000 input tokens at "
                    "$2 per million and 1,200 output tokens at $8 per million. "
                    "Model expense is $0.0216; add $0.004 for parsing and storage "
                    "and $0.006 for allocated execution and messaging, producing "
                    "$0.0316 per run. These are planning assumptions, not quoted "
                    "vendor prices. One hundred runs therefore cost $3.16 before "
                    "review. If twenty need two minutes of review each at an "
                    "internal labor valuation of $30 per hour, review adds $20 "
                    "and the batch costs $23.16, or $0.2316 per run. Count "
                    "retries, abandoned outputs, OCR charges, and failed validations "
                    "in the actual numerator. Divide by accepted results when "
                    "reporting cost per usable extraction. Allocate fixed subscriptions "
                    "separately rather than hiding them in negligible token expense. "
                    "This example covers extraction review only; mandatory purchase "
                    "and release decisions still consume time. The economic comparison "
                    "is the previous manual process at equivalent quality. Saving "
                    "three clerical minutes does not justify one missed removal "
                    "deadline, an erroneous title claim, or a single purchase "
                    "made above the defensible bid ceiling."
                ),
                (
                    "Keep every annual scenario tied to the canonical gross resale "
                    "basis. Conservative revenue is $150,000 at an 8% net margin, "
                    "yielding $12,000 annual owner net profit and $138,000 in "
                    "implied total costs. Base revenue is $575,000 at 14.0%, "
                    "yielding $80,500 profit and $494,500 costs. Both use 2 FT "
                    "+ 3 C. Scaled revenue is $1,000,000 at 20%, yielding "
                    "$200,000 profit and $800,000 costs with 3 FT + 4 C. "
                    "Purchase, transport, and refurbishment are already included in "
                    "the margin basis; do not subtract those costs again or "
                    "add auction purchase volume to resale revenue. Automation "
                    "subscriptions, review labor, storage, and selling expenses must "
                    "fit within the modeled cost envelope, not sit beneath it "
                    "as invisible extras. These totals do not establish a "
                    "specific wage schedule or prove that every listed team "
                    "member receives full-year market compensation. Build the actual "
                    "staffing budget before committing to hires. The $25,000–$200,000 "
                    "startup capital range and $3,000–$15,000 monthly operating "
                    "expense range are planning context, not additional revenue. "
                    "Distinguish inventory cash purchases, recurring expenses, and "
                    "owner distributions so a profitable sale does not conceal "
                    "an approaching cash shortage."
                ),
                (
                    "Scale only after the measured workload fits the pod. Review "
                    "weekly exception age, deadline breaches, stock accuracy, human "
                    "minutes per qualified lot, and cash committed to unsold "
                    "assets. Assign every recurring exception to one owner and "
                    "one remediation date. Keep encrypted database backups, test "
                    "restoration, restrict access by role, and rotate credentials "
                    "when contractors leave. Rehearse a mailbox outage, malformed "
                    "LLM response, duplicate webhook, database lock, and unavailable "
                    "carrier before increasing auction coverage. During an outage, "
                    "use a dated manual queue for deadlines and commitments, "
                    "then reconcile it before resuming automated messages. Do "
                    "not batch-replay purchase or release actions merely because "
                    "notifications accumulated. Require a current inventory and "
                    "payment check for each consequential action. The first "
                    "expansion should remove the observed bottleneck: better "
                    "inspection coverage, reliable transport capacity, or faster "
                    "buyer response, rather than indiscriminate additional scraping. "
                    "Moving into the Scaled case changes the roster to seven "
                    "people; it is not evidence that the original five-person "
                    "pod can absorb unlimited lots. Keep the seventy-percent "
                    "target tied to repetitive digital work, and retain "
                    "physical verification where defects, loading conditions, "
                    "and title documents determine whether an apparent bargain "
                    "becomes saleable inventory."
                ),
            ],
            "table": {
                "caption": "Automation Economics, Recovery Drills, and Canonical Scenario Reconciliation",
                "headers": [
                    "Measured unit or operating scenario",
                    "Explicit economics or acceptance requirement",
                    "Accountable monitoring and review practice",
                    "Recovery action or interpretation boundary",
                ],
                "rows": [
                    [
                        "Illustrative extraction run with bounded input and structured output",
                        "Model plus execution assumptions total $0.0316 before human review",
                        "Operations lead tracks tokens, retries, validation failures, and invoices",
                        "Reprice from actual usage before expanding collection or document volume",
                    ],
                    [
                        "Illustrative batch includes one hundred runs and twenty reviewed outputs",
                        "Forty review minutes add $20, producing $23.16 total batch cost",
                        "Record actual review duration rather than assuming effortless exception handling",
                        "Separate mandatory transaction decisions from this extraction-only review example",
                    ],
                    [
                        "Conservative annual scenario retains two full-time staff and three contractors",
                        "$150,000 gross resale proceeds at 8% yields $12,000 owner profit",
                        "Keep acquisition and operating costs within the $138,000 implied envelope",
                        "Do not treat inventory purchase volume as additional recognized revenue",
                    ],
                    [
                        "Base annual scenario retains two full-time staff and three contractors",
                        "$575,000 gross resale proceeds at 14.0% yields $80,500 owner profit",
                        "Reconcile all modeled costs against the $494,500 implied annual envelope",
                        "Investigate margin variance before buying additional lots or adding subscriptions",
                    ],
                    [
                        "Scaled annual scenario requires three full-time staff and four contractors",
                        "$1,000,000 gross resale proceeds at 20% yields $200,000 owner profit",
                        "Budget expanded capacity inside the $800,000 implied total cost envelope",
                        "Do not attribute seven-person throughput to the original five-person pod",
                    ],
                    [
                        "Recovery drill covers duplicate events, stale terms, and collection outages",
                        "No duplicate commitments occur and deadline ownership remains continuously visible",
                        "Named operators reconcile manual records before enabling queued external actions",
                        "Restore verified state instead of replaying every pending event blindly",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail and the follow-up, but never let a fast workflow turn an unverified lot into an authorized purchase.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Assign the six mapped plays to the sourcing lead, operations lead, and three specialist contractors; document escalation ownership and actual contractor availability.",
        "Build permitted alert ingestion with immutable source snapshots, stable lot identifiers, freshness checks, signed internal events, and a manual collection fallback.",
        "Implement evidence-linked extraction and Decimal bid worksheets; require renewed human authorization whenever fees, deadlines, restrictions, or material assumptions change.",
        "Create a serialized inventory state machine connecting receiving evidence, SF-97 and title-related checks, restriction review, reservations, payment verification, and release.",
        "Publish verified asset pages and segmented buyer outreach with synchronized stock, durable suppression, permission-based referrals, and attribution to completed resale transactions.",
        "Measure straight-through repetitive tasks, accepted-result cost, review minutes, inventory aging, and recovery performance while preserving the exact three canonical profit cases.",
    ],
    "statutory_citations": [
        {
            "title": "40 U.S.C. 545 — Procedure for disposal",
            "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title40-section545&num=0&edition=prelim",
            "relevance": (
                "Provides federal surplus property disposal authority and procedures. "
                "Read the applicable federal sale terms rather than assuming municipal "
                "auctions or commercial remarketing sales use identical rules."
            ),
        },
        {
            "title": "41 CFR Part 102-38 — Sale of Personal Property",
            "url": "https://www.ecfr.gov/current/title-41/subtitle-C/chapter-102/subchapter-B/part-102-38",
            "relevance": (
                "Establishes federal personal property sales requirements, including "
                "sale methods and restrictions. Preserve seller-specific terms and "
                "verify eligibility before authorizing participation."
            ),
        },
        {
            "title": "49 U.S.C. 32705 — Disclosure requirements on transfer of motor vehicles",
            "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section32705&num=0&edition=prelim",
            "relevance": (
                "Supports odometer disclosure controls for applicable vehicle transfers. "
                "Check implementing rules and exemptions, and keep mileage evidence "
                "distinct from SF-97 availability and state title processing."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Other protections for users of commercial electronic mail",
            "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section7704&num=0&edition=prelim",
            "relevance": (
                "Governs commercial email headers, subject lines, required identification, "
                "postal addresses, opt-out mechanisms, and honoring opt-out requests. "
                "Apply these controls to B2B inventory campaigns and preserve suppression."
            ),
        },
        {
            "title": "15 CFR 736.2 — General prohibitions",
            "url": "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-736/section-736.2",
            "relevance": (
                "Sets general prohibitions under the Export Administration Regulations. "
                "For proposed exports, assess jurisdiction, classification, destination, "
                "end user, and end use separately from domestic auction eligibility."
            ),
        },
        {
            "title": "22 CFR 121.1 — The United States Munitions List",
            "url": "https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-121/section-121.1",
            "relevance": (
                "Identifies defense article categories relevant to jurisdiction review. "
                "A seller's DEMIL designation does not independently settle export "
                "classification or authorize unrestricted transfer."
            ),
        },
    ],
}
