from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 2 FT + 3 C (5 people) government contract brokering team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Build a Python Bid Desk Across SAM.gov, Municipal Portals, FAR Controls, Evidence Queues, and Permissioned Partner Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #4, Government Contract Brokering, ranks #20 with a 70/100 "
        "Money-to-Manpower Score: a disciplined specialist play, not an autonomous "
        "award machine. This chapter maps seven operating plays: solicitation "
        "intelligence, qualification, lawful teaming, bid production, fulfillment "
        "evidence, service-fee collections, and partner distribution. A 2 FT + 3 C "
        "pod uses Python ingestion, authenticated webhooks, evidence-linked LLM "
        "extraction, and exception queues to target 70%+ automation of measured "
        "repetitive work while people retain consequential decisions. Recognized "
        "service fees support annual owner profit of $18,000 Conservative, "
        "$126,000 Base, and $300,000 Scaled; the Scaled case requires 3 FT + 4 C. "
        "The operating advantage comes from reusable evidence and trustworthy "
        "distribution, not procurement shortcuts or counting client awards as revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual recognized service fees; excludes client contract value",
            "note": "15% net margin; $18,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$560,000",
            "context": "Annual recognized service fees; excludes client contract value",
            "note": "22.5% net margin; $126,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual recognized service fees; excludes client contract value",
            "note": "30% net margin; $300,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Turn seven operating plays into one evidence-linked work queue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Design the desk around seven mapped operating plays rather than "
                    "seven disconnected software subscriptions. The chapter's operational "
                    "mapping is solicitation intelligence, qualification, lawful teaming, "
                    "bid production, fulfillment evidence, service-fee collections, and "
                    "partner distribution; these labels organize delivery without adding "
                    "new scorecard assumptions. Assign the first full-time person as capture "
                    "lead and the second as operations lead. Allocate the three contractors "
                    "to procurement review, proposal production, and supplier verification, "
                    "with purchased hours and backup coverage recorded explicitly. Contractor "
                    "headcount does not mean unlimited availability. Every opportunity "
                    "receives a stable identifier, buyer, jurisdiction, notice type, "
                    "solicitation number, source URL, retrieval timestamp, document digest, "
                    "deadline, assigned reviewer, and next action. Keep opportunity records "
                    "separate from client engagements and supplier records: one procurement "
                    "can produce several client discussions but should never become several "
                    "supposed awards. Use SQLite for a single-writer pilot and a managed "
                    "relational store when concurrent workers justify migration. A shared "
                    "queue, not a chat transcript, determines ownership. The capture lead "
                    "owns pursuit decisions; the operations lead owns queue health and "
                    "evidence completeness. This division keeps the five-person pod from "
                    "silently delegating binding commitments to whichever contractor "
                    "happens to receive an alert."
                ),
                (
                    "Build the ingestion worker with Python urllib.request, json, hashlib, "
                    "sqlite3, and zoneinfo. Query the SAM.gov Opportunities API using "
                    "documented filters, pagination, and account-specific limits; obtain "
                    "credentials through the operator's authorized account and keep them "
                    "outside prompts and logs. Treat municipal Bonfire, OpenGov Procurement, "
                    "and BidNet Direct feeds as separate connectors because access methods "
                    "and attachment permissions vary. Where no authorized machine interface "
                    "exists, route portal email into a review inbox and let a person "
                    "retrieve restricted material. Never bypass authentication to improve "
                    "coverage. Store each original document before extracting fields, then "
                    "deduplicate on jurisdiction, solicitation identifier, and document "
                    "digest rather than title alone. A changed digest creates an amendment "
                    "event even when the title remains identical. Polling workers emit "
                    "versioned events into an outbox; a dispatcher posts them to the "
                    "calendar and task service using authenticated webhooks. Validate "
                    "provider signatures, reject stale delivery timestamps, and enforce "
                    "unique event identifiers. Persist the event before acknowledging "
                    "delivery so a process restart cannot erase an amendment. Limit "
                    "document size and isolate parsing because public procurement "
                    "attachments remain untrusted input."
                ),
                (
                    "Measure the 70%+ target against repetitive labor minutes, not total "
                    "headcount, award dollars, or the percentage of records touched by "
                    "software. Establish a matched baseline across research, qualification "
                    "preparation, fulfillment evidence indexing, and acquisition-list "
                    "preparation. In an illustrative sample, those tasks previously "
                    "consumed 1,000 active minutes; automation removes 780 minutes but "
                    "introduces 60 minutes of exception handling, leaving 280 minutes "
                    "and a 72% net reduction. Count the exception minutes even when "
                    "contractors perform them. Keep final bid approval, supplier judgment, "
                    "and client commitments outside the automation claim unless their "
                    "actual repetitive components were separately timed. Instrument each "
                    "run with task category, source version, outcome, reviewer minutes, "
                    "and correction reason. Compare similar document lengths and notice "
                    "types so an easy week does not masquerade as a productivity gain. "
                    "Require stable results across four weekly samples before changing "
                    "staffing assumptions. A sample that saves 650 minutes after rework "
                    "supports 65%, and the dashboard must say so. Use the recovered "
                    "capacity for additional qualified pursuits and faster amendment "
                    "reviews before promising more clients. The seven-play design scales "
                    "only when each additional pursuit has an accountable human owner."
                ),
            ],
            "table": {
                "caption": "Python Ingestion and Event Reliability Matrix for Federal and Municipal Notices",
                "headers": [
                    "Control surface and operating trigger",
                    "Automated operation and persisted evidence",
                    "Named human responsibility and release condition",
                    "Failure recovery and observable service measure",
                ],
                "rows": [
                    [
                        "SAM.gov discovery starts from saved agency and classification filters",
                        "Python paginates authorized responses and stores retrieval timestamps",
                        "Capture lead checks filter coverage against representative live opportunities",
                        "Backoff preserves the last successful cursor and records feed age",
                    ],
                    [
                        "Municipal discovery separates each portal and its permitted access",
                        "Connector records original links and routes restricted attachments separately",
                        "Operations lead confirms retrieval rights before activating each connector",
                        "Manual inbox retrieval continues while the connector remains suspended",
                    ],
                    [
                        "Amendment detection compares document digests within each solicitation record",
                        "Changed content creates a versioned event and affected-task list",
                        "Proposal contractor reviews changed instructions before dependent drafting resumes",
                        "Prior versions remain searchable and affected deadlines become visibly disputed",
                    ],
                    [
                        "Webhook delivery begins only after durable local event persistence",
                        "Dispatcher signs requests and records unique receiver acknowledgment identifiers",
                        "Operations lead reviews repeated delivery failures and suspicious signatures",
                        "Bounded retries move exhausted events into a monitored exception queue",
                    ],
                    [
                        "Deadline normalization requires source timezone and original closing language",
                        "Calendar worker stores local closing time and normalized UTC equivalent",
                        "Capture lead resolves ambiguous timezone language before publishing reminders",
                        "Disputed deadlines trigger conservative internal cutoffs and direct source review",
                    ],
                    [
                        "Automation measurement samples repetitive work across all four requested domains",
                        "Timer ledger subtracts review and recovery minutes from gross savings",
                        "Operations lead validates matched workloads before reporting the achieved percentage",
                        "Falling savings reopen workflow design instead of hiding contractor rework",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture and fingerprint the authoritative source",
                    "action": "Persist the notice, attachments, retrieval time, and SHA-256 digests before extraction.",
                    "detail": "Assign the jurisdiction and solicitation identifier; retain separate versions whenever content changes.",
                },
                {
                    "step": 2,
                    "title": "Extract into a constrained opportunity record",
                    "action": "Request schema-constrained fields with supporting page references and source excerpts.",
                    "detail": "Reject unsupported dates, missing evidence, oversized responses, and fields outside the permitted schema.",
                },
                {
                    "step": 3,
                    "title": "Route consequential differences to the responsible person",
                    "action": "Create review tasks for deadlines, eligibility, pricing, certifications, and supplier commitments.",
                    "detail": "Keep dependent drafts blocked until the assigned reviewer records a disposition against the current source digest.",
                },
                {
                    "step": 4,
                    "title": "Publish internal tasks and reconcile delivery",
                    "action": "Dispatch calendar and checklist events through the durable outbox and verify acknowledgments.",
                    "detail": "Reconcile open events daily; preserve a manual operating sheet for service interruptions and urgent amendments.",
                },
            ],
        },
        {
            "heading": "2. Use LLMs for evidence extraction while people control procurement representations",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Place the LLM behind a narrow extraction contract rather than "
                    "giving it authority over the bid desk. Supply public solicitation "
                    "text, an explicit field schema, and instructions to return source "
                    "excerpts for every consequential assertion. Procurement attachments "
                    "can contain malicious instructions or merely confusing boilerplate; "
                    "treat both as document content, never as executable directions. "
                    "The model receives no portal password, signing authority, or ability "
                    "to email a contracting officer. Validate JSON types, allowable "
                    "enumerations, deadline syntax, and excerpt presence before displaying "
                    "results. Preserve the distinction between a requirement, an evaluation "
                    "factor, an optional attachment, and background narrative. A missing "
                    "performance location should create a reviewer task, not a plausible "
                    "location invented from the agency address. Use deterministic checks "
                    "for attachment counts and required forms, then reserve model work "
                    "for clause classification and cross-document comparison. Benchmark "
                    "the extractor on a frozen set of reviewed solicitations containing "
                    "amendments, scanned schedules, and conflicting dates. Track false "
                    "clearances separately from harmless extra review tasks: declaring "
                    "a bidder eligible when evidence is absent is more costly than "
                    "asking a reviewer to inspect an additional page."
                ),
                (
                    "Qualification must test the proposed transaction, not simply find "
                    "the word subcontractor. FAR 52.203-5 restricts contingent-fee "
                    "arrangements where the clause applies, subject to its defined "
                    "exceptions; labeling a success payment a consulting retainer does "
                    "not change its substance. Prefer documented fees for actual "
                    "research, proposal, and administration services, and have the "
                    "procurement reviewer examine compensation structure before engagement. "
                    "Procurement integrity under 41 U.S.C. 2102 and FAR 3.104 requires "
                    "rejecting protected bid, proposal, or source-selection information "
                    "received outside authorized channels. Anti-kickback controls under "
                    "41 U.S.C. 8702 require scrutiny of supplier referral payments, gifts, "
                    "and credits intended to obtain or reward favorable treatment. "
                    "For covered set-asides, evaluate FAR 52.219-14 by contract category "
                    "and the treatment of similarly situated entities; do not apply "
                    "one universal subcontracting percentage. Where applicable, FAR "
                    "52.215-23 addresses excessive pass-through charges, making an "
                    "empty intermediary structure especially fragile. Municipal work "
                    "requires its own ordinance and solicitation review rather than "
                    "an assumption that federal clauses govern. Automation assembles "
                    "these questions with citations; the reviewer resolves applicability, "
                    "and the authorized prime signs its own representations."
                ),
                (
                    "Make the bid calendar a dependency graph with explicit evidence "
                    "locks. An amendment affecting delivery dates should reopen supplier "
                    "availability, pricing validity, staffing assumptions, and the draft "
                    "schedule instead of merely changing a calendar entry. Generate "
                    "internal reminders at seven days, three days, and one day when "
                    "the procurement timeline permits, with an earlier cutoff for "
                    "uploads requiring large attachments. Capture the solicitation's "
                    "actual submission mechanism: portal upload, sealed package, and "
                    "authorized email are different workflows. The proposal contractor "
                    "can assemble a checklist from reviewed clauses, but the capture "
                    "lead verifies every required attachment, signature, acknowledgment, "
                    "and price schedule against the latest source version. Require "
                    "supplier quotations to identify scope, exclusions, validity period, "
                    "lead time, and the person authorized to commit resources. No "
                    "model-generated capability statement becomes a factual claim "
                    "without supporting evidence. For restricted client material, "
                    "use only processing environments approved for that data category "
                    "and contractual obligations; otherwise keep extraction local or "
                    "manual. The final submission remains a deliberate human action, "
                    "followed by receipt capture and an independent check that the "
                    "submitted files match the approved package."
                ),
            ],
            "table": {
                "caption": "Procurement Representation Controls and Evidence Requirements",
                "headers": [
                    "Consequential representation requiring a review",
                    "Machine assistance permitted within the workflow",
                    "Evidence required before an authorized decision",
                    "Human disposition and retained audit record",
                ],
                "rows": [
                    [
                        "Eligibility depends on solicitation terms and the proposed performing entity",
                        "Extractor identifies size standards and cited participation restrictions",
                        "Current entity records and solicitation-specific eligibility analysis support conclusions",
                        "Procurement reviewer records applicability before capture lead approves pursuit",
                    ],
                    [
                        "Compensation structure includes referral payments and success-linked service charges",
                        "Checklist flags award-linked language across engagement and supplier agreements",
                        "Reviewed agreement describes actual services and the relevant clause analysis",
                        "Procurement reviewer documents treatment before either party signs commitments",
                    ],
                    [
                        "Information provenance includes unsolicited material about competing bids or evaluations",
                        "Intake labels source identity and restricts suspicious document distribution",
                        "Authorized public release or permitted disclosure supports continued use",
                        "Capture lead isolates questionable material and obtains qualified direction",
                    ],
                    [
                        "Subcontract allocation affects covered set-aside performance and entity treatment",
                        "Worksheet calculates proposed allocations using the applicable contract category",
                        "Prime supplies performance plan and documented similarly situated assessments",
                        "Procurement reviewer checks applicable limits before the prime certifies",
                    ],
                    [
                        "Intermediary pricing can create excessive pass-through concerns where applicable",
                        "Worksheet separates performed services from underlying supplier contract amounts",
                        "Scope and cost support demonstrate actual added operating value",
                        "Capture lead rejects unsupported structures before presenting client economics",
                    ],
                    [
                        "Submission completeness changes whenever an amendment modifies governing instructions",
                        "Checklist compares required files against the approved package manifest",
                        "Latest amendment acknowledgments and signed schedules match source requirements",
                        "Authorized submitter retains receipt and independently verifies delivered files",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before any consequential release",
                "body": "Extraction can run unattended; binding representations and external commitments require named review against current evidence.",
                "items": [
                    "Verify the latest solicitation and every amendment by digest; reconcile closing time, timezone, submission channel, and required acknowledgments.",
                    "Have the procurement reviewer examine contingent compensation, information provenance, referral benefits, and jurisdiction-specific restrictions before engagement.",
                    "Confirm the prime's eligibility, applicable subcontracting limits, supplier capacity, and actual intermediary services before presenting the structure.",
                    "Require the authorized signer to approve factual claims and the final file manifest; capture and independently check the submission receipt.",
                ],
            },
        },
        {
            "heading": "3. Price automated runs and recover failures without breaking the scorecard",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price an automated run as a bounded document-processing attempt, "
                    "not an entire successful procurement. For an illustrative planning "
                    "rate, 6,000 input tokens at $2 per million cost $0.012, "
                    "and 1,500 output tokens at $12 per million cost $0.018. "
                    "Add $0.020 for allocated compute, storage, and event delivery "
                    "plus a $0.010 retry reserve: total direct cost is $0.060 "
                    "per run. These are budgeting assumptions rather than a vendor "
                    "quote; substitute the contracted model tariff and measured token "
                    "usage before purchasing capacity. At 3,000 runs monthly, direct "
                    "processing costs $180. If 90 runs require eight minutes of "
                    "exception review at a loaded $60 hourly rate, that review "
                    "costs $720, producing $900 combined expense or $0.30 per "
                    "run. Final bid reviews, software subscriptions, connector "
                    "maintenance, ordinary fulfillment labor, and sales work remain "
                    "additional expenses. Log those costs separately to prevent a "
                    "cheap extraction metric from concealing an expensive desk. "
                    "Route long documents through section selection and digest-based "
                    "caching, but invalidate cached decisions when relevant source "
                    "content changes. Cost controls must never suppress a material "
                    "amendment merely because the monthly token budget is nearly spent."
                ),
                (
                    "Reconcile the operating model to recognized service fees, not "
                    "the face value of client awards. Conservative revenue is "
                    "$120,000 at a 15% net margin, leaving $18,000 annual "
                    "owner net profit and $102,000 implied annual expenses. "
                    "Base revenue is $560,000 at 22.5%, leaving $126,000 "
                    "profit and $434,000 expenses. Scaled revenue is $1,000,000 "
                    "at 30%, leaving $300,000 profit and $700,000 expenses. "
                    "Illustrative fee arithmetic is twelve $10,000 completed service "
                    "packages, twenty-eight $20,000 packages, and forty $25,000 "
                    "packages respectively; actual recognition follows the engagement's "
                    "earned-service terms, not invoice issuance alone. These are "
                    "alternative annual scenarios, not additive revenue streams. "
                    "Conservative and Base retain 2 FT + 3 C; Scaled requires "
                    "3 FT + 4 C. The Conservative expense ceiling is tight "
                    "for that staffing label, so explicitly budget compensation, "
                    "contractor hours, and owner labor rather than pretending "
                    "headcount establishes affordability. The stated $5,000–$25,000 "
                    "monthly operating range is a planning envelope, not permission "
                    "to exclude delivery labor from scenario expenses. Startup "
                    "capital of $25,000–$150,000 and a 6–18 month first-deal "
                    "window demand a separate cash runway schedule before hiring "
                    "or committing to annual software contracts."
                ),
                (
                    "Fulfillment automation begins after scope and responsibility "
                    "are settled. Create an evidence register for supplier milestones, "
                    "inspection records, delivery confirmations, client acceptance, "
                    "and the service desk's own completed work. Keep client goods "
                    "and subcontractor obligations separate from the operator's "
                    "service-fee ledger. The collections play drafts invoices from "
                    "reviewed milestones, reconciles receipts, and alerts the operations "
                    "lead to disputes; it does not charge clients for a model's "
                    "unsupported completion inference. Federal prompt-payment rules "
                    "do not automatically determine when a private client owes "
                    "this desk, so monitor the actual engagement terms and cash "
                    "aging. Supplier failure requires a named escalation path, "
                    "documented alternatives, and buyer or prime authorization where "
                    "changes require it. For technical failures, set connector "
                    "timeouts, bounded retries, and a circuit breaker that stops "
                    "repeated processing of a corrupt attachment. Preserve a daily "
                    "export of active pursuits, deadlines, and evidence links so "
                    "the pod can operate manually during an outage. Restore "
                    "from tested backups, replay idempotent events, and reconcile "
                    "every external action before restarting automatic dispatch. "
                    "A recovered database is insufficient if the calendar still "
                    "contains superseded deadlines or invoices were transmitted twice."
                ),
            ],
            "table": {
                "caption": "Scenario Reconciliation, Unit Costs, and Recovery Economics",
                "headers": [
                    "Scenario or operating cost boundary",
                    "Explicit calculation and recognized economic basis",
                    "Staffing or human workload allocation",
                    "Management response and reconciliation requirement",
                ],
                "rows": [
                    [
                        "Conservative annual case recognizes only completed operator service fees",
                        "$120,000 revenue less $102,000 expenses yields $18,000 owner profit",
                        "Two full-time people plus three contractors require explicit compensation budgets",
                        "Preserve the 15% margin assumption while exposing staffing affordability constraints",
                    ],
                    [
                        "Base annual case expands delivered services without counting client awards",
                        "$560,000 revenue less $434,000 expenses yields $126,000 owner profit",
                        "Two full-time people plus three contractors retain measured review responsibilities",
                        "Maintain 22.5% margin through priced scope and controlled delivery hours",
                    ],
                    [
                        "Scaled annual case requires increased capacity rather than invisible overtime",
                        "$1,000,000 revenue less $700,000 expenses yields $300,000 owner profit",
                        "Three full-time people plus four contractors constitute seven people",
                        "Maintain 30% margin while funding the additional delivery and review capacity",
                    ],
                    [
                        "Direct processing estimate covers one bounded document attempt only",
                        "$0.030 model usage plus $0.030 infrastructure and retry allocation",
                        "Routine successful extraction consumes no separately assigned exception review minutes",
                        "Replace assumed tariffs with contracted rates and actual usage measurements",
                    ],
                    [
                        "Monthly extraction workload includes explicitly budgeted exception handling labor",
                        "Three thousand runs cost $180 before $720 exception review",
                        "Ninety exceptions require twelve reviewer hours at sixty dollars hourly",
                        "Report $0.30 blended run cost while separately tracking remaining overhead",
                    ],
                    [
                        "Recovery expense includes reconciliation after duplicate or interrupted event delivery",
                        "Incident ledger records repair labor and every externally repeated action",
                        "Operations lead owns restoration while capture lead reviews urgent deadlines",
                        "Resume dispatch only after calendars and invoice records reconcile",
                    ],
                ],
            },
        },
        {
            "heading": "4. Build distribution loops from reviewed procurement intelligence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build programmatic distribution from the same reviewed opportunity "
                    "records used by the desk, but publish a deliberately smaller "
                    "public dataset. A useful page serves a specific buyer problem: "
                    "municipal facilities maintenance bids in one region, upcoming "
                    "federal laboratory supply opportunities, or a supplier-readiness "
                    "checklist for one contract category. Include authoritative links, "
                    "last-checked timestamps, closing dates, and a clear explanation "
                    "of what the service desk actually provides. Do not republish "
                    "client pricing, restricted attachments, or another bidder's "
                    "capability evidence. Generate drafts automatically, then have "
                    "the capture lead approve substantive pages before first "
                    "publication and material revisions. Expire closed notices "
                    "visibly and distinguish opportunity summaries from official "
                    "government instructions. Thin location pages containing "
                    "identical text will not create a durable acquisition "
                    "advantage. Instead, combine verified local portal coverage "
                    "with original comparisons of submission mechanics and "
                    "supplier preparation requirements. Track indexed pages, "
                    "qualified inquiries, accepted engagements, and earned fees "
                    "by source. Impressions are diagnostic, not revenue. "
                    "One accurate niche page that generates a service-ready "
                    "client can outperform hundreds of automatically published "
                    "pages that attract suppliers unable to meet the underlying requirements."
                ),
                (
                    "Create a permissioned sharing loop around supplier usefulness "
                    "rather than promised influence. After a reviewed shortlist "
                    "is delivered, offer the recipient a shareable public digest "
                    "and a separate invitation link for colleagues who want "
                    "future notices. The recipient chooses whether to share; "
                    "the system never uploads their address book. Attribute "
                    "referrals with campaign identifiers that reveal no private "
                    "client relationship. Partner with relevant APEX Accelerators, "
                    "trade associations, and complementary proposal specialists "
                    "through educational resources and transparent service "
                    "descriptions; never imply government endorsement. For "
                    "commercial outbound email, use accurate headers and "
                    "subjects, identify the sender, provide a valid postal "
                    "address and working opt-out, and honor suppression "
                    "requirements under 15 U.S.C. 7704. Screen business "
                    "contacts against the desk's suppression list before "
                    "any send. Keep outreach specific: identify the public "
                    "notice, explain a documented capability fit, and invite "
                    "a conversation rather than asserting award likelihood. "
                    "The capture lead approves recipient criteria and "
                    "message templates before dispatch. Referral compensation "
                    "requires the same contingent-fee and anti-kickback "
                    "analysis as other compensation; a marketing label "
                    "does not remove procurement risk."
                ),
                (
                    "Close the flywheel with evidence from delivery, not "
                    "vanity engagement. A completed qualification checklist "
                    "improves the next supplier intake; an amendment "
                    "postmortem improves the extraction test set; an "
                    "accepted service milestone supports a client-approved "
                    "case study; a helpful public digest attracts "
                    "another properly matched supplier. These connections "
                    "join all seven plays without granting software "
                    "independent authority to pursue, certify, submit, "
                    "or commit resources. Run a weekly forty-five-minute "
                    "pod review covering feed freshness, disputed deadlines, "
                    "false clearances, supplier exceptions, unpaid service "
                    "fees, and acquisition quality. Give each defect "
                    "one owner and one measurable repair. Track "
                    "qualified-lead conversion and service contribution by "
                    "channel, then throttle distribution when the human "
                    "review queue exceeds capacity. For example, stop "
                    "new campaign sends when unresolved material amendments "
                    "threaten active submissions; keep essential client "
                    "notifications running. Add the Scaled case's third "
                    "full-time person and fourth contractor only after "
                    "earned service demand and cash coverage support "
                    "that capacity. The durable advantage is a growing "
                    "library of verified requirements, capable suppliers, "
                    "and trustworthy operating evidence, not a larger "
                    "pile of unreviewed model output."
                ),
            ],
            "table": {
                "caption": "Seven-Play Distribution Flywheel and Human Capacity Controls",
                "headers": [
                    "Distribution asset and linked operating plays",
                    "Automated preparation with bounded publication authority",
                    "Human quality control and information boundary",
                    "Conversion measure and corrective operating action",
                ],
                "rows": [
                    [
                        "Reviewed niche pages connect solicitation intelligence with partner distribution",
                        "Renderer drafts pages from current public opportunity records",
                        "Capture lead verifies accuracy and removes private client evidence",
                        "Measure qualified inquiries and retire pages attracting persistently unsuitable prospects",
                    ],
                    [
                        "Supplier readiness worksheets connect qualification with lawful teaming",
                        "Generator assembles reviewed requirements and evidence-request checklists",
                        "Procurement reviewer confirms applicability before client-facing use begins",
                        "Measure completed evidence packs rather than downloaded worksheet totals",
                    ],
                    [
                        "Shareable public digests connect useful research with recipient-led referrals",
                        "Email service creates public links and separate subscription invitations",
                        "Capture lead approves content while recipients control onward sharing",
                        "Measure referred qualified engagements without importing recipients' private contacts",
                    ],
                    [
                        "Targeted business outreach connects public notices with documented supplier capabilities",
                        "Preparation worker matches reviewed business criteria and applies suppression lists",
                        "Capture lead approves audience criteria and truthful message templates",
                        "Measure positive qualified responses and stop poorly matched campaigns",
                    ],
                    [
                        "Client-approved case studies connect fulfillment evidence with service-fee collections",
                        "Drafting worker summarizes accepted milestones and verified service outcomes",
                        "Client authorizes publication and reviewer removes protected commercial details",
                        "Measure attributable earned fees rather than underlying client award amounts",
                    ],
                    [
                        "Weekly operating review connects bid production with all seven plays",
                        "Dashboard combines review backlog and channel-level service contribution",
                        "Operations lead assigns repairs while capture lead controls pursuit capacity",
                        "Throttle acquisition whenever material amendments exceed safe review capacity",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make procurement intelligence useful enough to circulate",
                "body": "The strongest distribution asset saves a supplier real preparation time while preserving source accuracy and client confidentiality.",
                "items": [
                    "Maintain a municipal portal coverage ledger showing last successful retrieval; a quiet connector can mean broken access rather than absent opportunities.",
                    "Publish amendment deltas with source links instead of repeatedly sending entire notices; suppliers notice the specific change affecting price or delivery.",
                    "Ask suppliers to refresh quotation validity and lead times before a pursuit becomes urgent; stale supplier evidence destroys otherwise efficient bid assembly.",
                    "Turn accepted service milestones into client-approved case studies that describe the desk's work and earned fees without claiming credit for an entire award.",
                ],
            },
        },
    ],
    "pull_quote": "Automate the movement of evidence, never the authority to make a procurement promise.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Assign the seven operating plays across the capture lead, operations lead, and three contractors, including purchased hours and backup responsibilities.",
        "Build source-preserving SAM.gov and municipal ingestion with document digests, a durable event outbox, signed webhooks, and a manual recovery sheet.",
        "Benchmark repetitive labor across four weekly samples and report net savings after exception review before claiming 70%+ automation.",
        "Require evidence-linked extraction and named review for compensation structure, eligibility, subcontract allocation, supplier commitments, and final submissions.",
        "Reconcile run costs, review labor, earned service fees, and cash runway to the exact Conservative, Base, and Scaled scenario economics.",
        "Launch reviewed niche pages, shareable public digests, and targeted outreach with suppression controls; throttle acquisition when consequential review capacity is exhausted.",
    ],
    "statutory_citations": [
        {
            "title": "FAR 52.203-5 — Covenant Against Contingent Fees",
            "url": "https://www.acquisition.gov/far/52.203-5",
            "relevance": "Review award-linked compensation and the clause's defined exceptions before structuring procurement service or referral arrangements.",
        },
        {
            "title": "41 U.S.C. 2102 — Prohibitions on Disclosing and Obtaining Procurement Information",
            "url": "https://www.law.cornell.edu/uscode/text/41/2102",
            "relevance": "Control the intake and use of contractor bid, proposal, and source-selection information before award.",
        },
        {
            "title": "FAR 3.104 — Procurement Integrity",
            "url": "https://www.acquisition.gov/far/3.104",
            "relevance": "Build information-provenance review and escalation procedures around applicable procurement-integrity requirements.",
        },
        {
            "title": "41 U.S.C. 8702 — Prohibition on Kickbacks",
            "url": "https://www.law.cornell.edu/uscode/text/41/8702",
            "relevance": "Examine supplier payments, credits, gifts, and referral benefits for prohibited inducements or rewards.",
        },
        {
            "title": "FAR 52.219-14 — Limitations on Subcontracting",
            "url": "https://www.acquisition.gov/far/52.219-14",
            "relevance": "Test covered performance structures using the applicable contract category and similarly situated entity rules.",
        },
        {
            "title": "FAR 52.215-23 — Limitations on Pass-Through Charges",
            "url": "https://www.acquisition.gov/far/52.215-23",
            "relevance": "Where applicable, document substantive intermediary work and review charges associated with subcontracted performance.",
        },
        {
            "title": "31 U.S.C. 3902 — Interest Penalties",
            "url": "https://www.law.cornell.edu/uscode/text/31/3902",
            "relevance": "Distinguish applicable federal agency payment obligations from the desk's separate private service-fee collection terms.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for Transmission of Messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Implement accurate commercial email identification, postal-address disclosure, functioning opt-outs, and timely suppression handling.",
        },
    ],
}
