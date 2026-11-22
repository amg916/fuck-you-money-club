from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 5 FT + 4 C (9 people) commercial cleaning contracts team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Webhooks, ISSA Labor Budgets, Supervisor Pods, Inspection Evidence, and Contract-to-Cash Controls Under FLSA and OSHA",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #10, Commercial Cleaning Contracts, ranks #28 with a Money-to-Manpower "
        "Score of 56/100 because software coordinates labor rather than replacing cleaning. "
        "This chapter maps four operator plays: territory research and qualification; "
        "labor-aware scheduling; inspection evidence and corrective action; and billing, "
        "renewal, and referral distribution. A 5 FT + 4 C pod targets 70%+ automation "
        "of eligible repetitive administrative events while supervisors retain decisions "
        "about bids, staffing exceptions, safety, and customer commitments. Canonical annual "
        "owner profit remains $20,000 Conservative, $87,000 Base, and $192,000 Scaled; "
        "the Scaled team increases to 6 FT + 5 C. Build around measured ISSA task "
        "rates, durable webhook queues, evidence-backed inspection logs, and reconciled "
        "invoices, then grow through route density rather than indiscriminate lead volume."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual cleaning contract revenue; recognized operator revenue",
            "note": "8% net margin; $20,000 annual owner net profit; 5 FT + 4 C",
        },
        {
            "label": "Base",
            "value": "$725,000",
            "context": "Annual cleaning contract revenue; recognized operator revenue",
            "note": "12.0% net margin; $87,000 annual owner net profit; 5 FT + 4 C",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual cleaning contract revenue; recognized operator revenue",
            "note": "16% net margin; $192,000 annual owner net profit; 6 FT + 5 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Instrument Four Operator Plays Before Automating the Pod",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the automation target as a denominator problem before buying software. "
                    "For Candidate #10, the four mapped plays in this chapter are territory research "
                    "and qualification, labor-aware scheduling, inspection evidence and corrective "
                    "action, and billing with renewal and referral distribution. Each play owns "
                    "explicit administrative events, not an imaginary percentage of all cleaning "
                    "work. Research events include deduplicating properties and retrieving permitted "
                    "business contact information; qualification events include checking service "
                    "geography and recording building type. Fulfillment events include preparing "
                    "rosters, organizing inspection evidence, and matching completed service to "
                    "contract schedules. Acquisition events include maintaining approved service "
                    "pages, routing inquiries, and preparing account-specific outreach drafts. "
                    "Define an event as one completed business outcome with a stable identifier; "
                    "splitting a single invoice into twenty technical operations must not inflate "
                    "the automation rate. Record whether each outcome finished unattended, required "
                    "human judgment, or failed and entered recovery. A 70%+ objective applies only "
                    "to this eligible repetitive workload. It excludes mopping, restroom servicing, "
                    "clinical-area cleaning, travel, training, and supervisory walkthroughs. "
                    "Establish a two-week baseline by event family, including handling minutes and "
                    "rework, before setting targets. Report end-to-end completion beside automation "
                    "coverage so a fast pipeline cannot conceal unanswered customers or missing visits."
                ),
                (
                    "Assign ownership inside the 5 FT + 4 C constraint rather than inventing a "
                    "separate technology department. One illustrative allocation is a working "
                    "owner handling sales and account decisions, one working supervisor handling "
                    "dispatch and inspections, and three full-time cleaners supporting recurring "
                    "routes. Four contractors provide genuinely independent contracted capacity "
                    "where the actual relationship supports that status; the scorecard's C label "
                    "does not determine classification. Count the owner's and supervisor's field "
                    "hours explicitly when testing service capacity. The owner maintains contract "
                    "versions, price floors, and customer concentration limits. The supervisor "
                    "maintains task standards, access restrictions, training records, and exceptions. "
                    "A contractor business receives an agreed scope and evidence requirements "
                    "without being represented as a convenient substitute for employee payroll. "
                    "Use a job identifier shared by HubSpot, a scheduling system such as Jobber, "
                    "and QuickBooks Online, subject to the selected products' supported interfaces. "
                    "Keep the authoritative crosswalk in an access-controlled register. Store "
                    "property identifiers separately from personal contact details and restrict "
                    "building access instructions to assigned personnel. Weekly ownership review "
                    "should examine open exceptions, stale credentials, expiring vendor documents, "
                    "and route overload. This makes the automation accountable to named people "
                    "without pretending nine people can absorb unlimited new buildings."
                ),
                (
                    "Build the first integration as a small Python service with a durable event "
                    "ledger, not a chain of fragile email rules. Receive provider webhooks over "
                    "HTTPS, validate signatures according to each provider's documented scheme, "
                    "check replay controls where supported, and persist the event before returning "
                    "success. A single-host pilot can use sqlite3 transactions, json serialization, "
                    "hashlib digests, and hmac verification; protect the database, back it up, and "
                    "keep external API requests outside write transactions. For greater concurrent "
                    "volume, move the ledger to a managed transactional database without changing "
                    "the event contract. Store source, event identifier, contract revision, object "
                    "identifier, received time, processing state, attempts, and correlation identifier. "
                    "A unique constraint on source and event identifier prevents repeated delivery "
                    "from creating repeated work. Use an outbox for outbound changes and reconcile "
                    "remote results after timeouts instead of blindly repeating invoice creation. "
                    "An LLM may extract proposed fields or draft an explanation, but deterministic "
                    "code validates required fields, arithmetic, allowed status transitions, and "
                    "authorization. Treat web pages, uploaded documents, and customer notes as data, "
                    "never executable instructions. Redact sensitive content before model submission "
                    "and retain the extraction evidence needed for a reviewer to resolve ambiguity."
                ),
            ],
            "table": {
                "caption": "Four-Play Ownership and Durable Event Contract Matrix",
                "headers": [
                    "Event family and assigned operator play",
                    "Authoritative input and required identity evidence",
                    "Automated transformation and persisted output record",
                    "Human responsibility and bounded recovery action",
                ],
                "rows": [
                    [
                        "Property research within the territory qualification play",
                        "Permitted property records linked to normalized street addresses",
                        "Deduplicate buildings and attach dated source references",
                        "Owner resolves ambiguous ownership before any account outreach",
                    ],
                    [
                        "Inbound qualification within the territory qualification play",
                        "Customer inquiry containing building type and requested frequency",
                        "Calculate geographic fit without making a price commitment",
                        "Owner confirms scope through an actual building walkthrough",
                    ],
                    [
                        "Roster preparation within the labor-aware scheduling play",
                        "Approved scope revision with worker availability and qualifications",
                        "Propose assignments respecting access windows and budgeted hours",
                        "Supervisor reviews overtime exposure and uncovered service visits",
                    ],
                    [
                        "Evidence organization within the inspection assurance play",
                        "Inspection submission containing job identity and capture timestamps",
                        "Index authorized evidence and flag missing required observations",
                        "Supervisor determines acceptance and schedules necessary corrective work",
                    ],
                    [
                        "Invoice preparation within the billing distribution play",
                        "Signed contract terms matched against completed service records",
                        "Create draft charges with supporting service period references",
                        "Owner reviews adjustments before releasing customer payment requests",
                    ],
                    [
                        "Referral preparation within the billing distribution play",
                        "Resolved service history and account contact communication preferences",
                        "Prepare account-specific requests using verified service performance evidence",
                        "Account owner authorizes publication and customer introduction requests",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Automate the Administration That Experienced Cleaners Already Distrust",
                "body": (
                    "Start with the recurring sources of dispute: scope versions, access failures, "
                    "unrecorded travel, and invoices that cannot explain their own charges."
                ),
                "items": [
                    "Put the signed task-frequency matrix revision on every schedule and inspection form; a generic building checklist conceals unpaid scope expansion.",
                    "Give each janitorial closet a documented supply minimum and replenishment owner; low-stock alerts are more useful than elaborate cleaning summaries.",
                    "Record locked-door incidents separately from crew lateness, including permitted contact attempts and the customer's access escalation procedure.",
                    "Compare ISSA estimating assumptions with observed minutes by surface and task; do not punish crews for a salesperson's optimistic production rate.",
                ],
            },
        },
        {
            "heading": "2. Schedule Paid Capacity and Inspect Evidence Without Delegating Judgment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start scheduling from a measured task budget, not a contract's attractive "
                    "monthly price. ISSA production-rate references provide estimating inputs; "
                    "actual equipment, soil load, furniture density, security procedures, and "
                    "medical-area protocols determine the usable rate. For illustration, a 20,000 "
                    "cleanable-square-foot office at an assumed blended 4,000 square feet per "
                    "productive hour requires five productive hours per visit. Twenty visits "
                    "produce 100 monthly productive hours. Adding twenty hours for setup, "
                    "supervision, and paid route activity yields 120 budgeted hours. At an "
                    "illustrative loaded labor cost of $24 per hour, labor costs $2,880. A "
                    "$4,500 monthly contract then leaves $1,620 before supplies, equipment, "
                    "insurance, administration, and other overhead; that remainder is not owner "
                    "profit. Store these assumptions beside the bid and replace them with "
                    "observations after mobilization. The scheduling service can propose workers "
                    "against access windows, task qualifications, equipment availability, and "
                    "travel buffers. It must reject overlapping assignments and surface "
                    "insufficient capacity rather than silently shortening visits. Confirm "
                    "acceptance before publishing a changed roster, and preserve the prior "
                    "version so the supervisor can restore it during an outage or dispute. "
                    "Higher software throughput does not create another paid cleaning hour."
                ),
                (
                    "Use payroll rules as explicit scheduling constraints while keeping actual "
                    "time capture independent of the planned budget. Under 29 U.S.C. § 207, "
                    "covered nonexempt employees generally receive overtime after forty hours "
                    "in a workweek; apply relevant state requirements as well. Travel between "
                    "job sites during the workday is work time under 29 CFR § 785.38. Track "
                    "training, required meetings, and other compensable activities under the "
                    "applicable rules rather than hiding them inside production assumptions. "
                    "A projected overtime alert routes to the supervisor, but software must "
                    "never delete worked time to preserve a bid margin. Maintain wage and "
                    "hour records consistent with 29 CFR § 516.2, and preserve corrections "
                    "with the original entry and the reason. Worker classification requires "
                    "a documented assessment under applicable federal and state tests; a "
                    "vendor invoice or signed label alone does not settle it. For California "
                    "work, evaluate Labor Code § 2775 and any genuinely applicable exceptions "
                    "before treating cleaning labor as independent contracting. Separately "
                    "verify insurance requirements against customer contracts and local "
                    "requirements. Where the current staffing model fails those tests, "
                    "reprice or restructure the work instead of asking automation to conceal "
                    "the mismatch. That is an operating constraint, not an integration defect."
                ),
                (
                    "Inspection automation should accelerate evidence handling while leaving "
                    "cleanliness acceptance with a qualified person. Configure mobile forms by "
                    "site, zone, task frequency, and risk: restrooms, break rooms, entrances, "
                    "clinical rooms, and periodic floor work need different observations. Require "
                    "job identity, task completion, exceptions, and timestamps, with offline "
                    "capture for basements and secured facilities. Photos are optional only "
                    "where the contract permits them; prohibit patient details, visible records, "
                    "and unnecessary personal images in medical settings. Assess whether the "
                    "actual service arrangement involves handling protected health information "
                    "rather than assuming every janitorial contract creates the same obligations. "
                    "An LLM can group recurring complaints and draft a corrective-action "
                    "summary, but a photograph cannot establish microbial safety or proper "
                    "disinfectant contact time. OSHA's Hazard Communication Standard, 29 CFR "
                    "§ 1910.1200, makes chemical labeling, safety data sheets, and training "
                    "concrete operating requirements. Where occupational exposure to blood "
                    "or other potentially infectious materials exists, evaluate 29 CFR "
                    "§ 1910.1030 requirements before assigning work. Route spills, exposure "
                    "incidents, chemical substitutions, and disputed completion to the "
                    "supervisor immediately. During connectivity loss, crews follow the "
                    "approved local procedure and synchronize records later; they do not "
                    "improvise chemical mixtures or wait for an LLM to authorize safe work."
                ),
            ],
            "table": {
                "caption": "Scheduling and Inspection Exception Handling for a Nine-Person Pod",
                "headers": [
                    "Operational condition requiring an explicit decision",
                    "Machine check performed before proposing action",
                    "Qualified human decision and required evidence",
                    "Fallback procedure preserving service and records",
                ],
                "rows": [
                    [
                        "A new building exceeds existing nightly route capacity",
                        "Compare task hours against paid availability and travel",
                        "Owner validates additional labor before committing service dates",
                        "Offer a feasible start date or decline scope",
                    ],
                    [
                        "An employee approaches weekly federal overtime hours",
                        "Aggregate actual hours with remaining proposed work assignments",
                        "Supervisor authorizes coverage while preserving all worked time",
                        "Reassign qualified available personnel without erasing time records",
                    ],
                    [
                        "A crew cannot enter the customer's secured building",
                        "Match access window against documented arrival and contact attempts",
                        "Supervisor confirms customer instructions and any contractual visit charge",
                        "Record access failure and activate the agreed escalation sequence",
                    ],
                    [
                        "A mobile inspection arrives without required zone observations",
                        "Compare submitted fields against the current site checklist",
                        "Supervisor determines whether another physical inspection is necessary",
                        "Hold acceptance status and dispatch documented corrective work",
                    ],
                    [
                        "A proposed chemical differs from the approved product",
                        "Match product identity against site standards and safety records",
                        "Trained supervisor checks label directions and task suitability",
                        "Use the approved available product or suspend affected work",
                    ],
                    [
                        "A clinical-area incident may involve occupational exposure",
                        "Route incident indicators without transmitting unnecessary patient information",
                        "Trained personnel follow the applicable exposure response procedure",
                        "Isolate affected work and use established emergency contacts",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Expanding Automated Dispatch",
                "body": (
                    "Consequential decisions remain assigned to the owner or qualified supervisor. "
                    "An automated recommendation cannot substitute for these checks."
                ),
                "items": [
                    "Verify that route capacity includes setup, required training, between-site travel, and realistic absence coverage before accepting another recurring building.",
                    "Verify actual worker relationships, timekeeping rules, and insurance documents before enabling assignments to employees or contractor businesses.",
                    "Verify current chemical instructions, required safety training, site-specific exposure procedures, and authorized evidence capture before publishing mobile forms.",
                    "Verify offline rosters, escalation contacts, restored backups, and a successful duplicate-event test before relying on unattended dispatch preparation.",
                ],
            },
        },
        {
            "heading": "3. Close the Contract-to-Cash Loop and Price Every Automated Outcome",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Make billing a three-way comparison among signed scope, service evidence, "
                    "and invoice terms. A recurring fixed-fee contract normally generates its "
                    "scheduled charge under the agreement; missing inspection evidence should "
                    "trigger review, not an invented switch to hourly billing. Separately "
                    "identify authorized extras, credits, periodic floor work, applicable taxes, "
                    "and customer purchase-order requirements. A Python worker builds a draft "
                    "invoice payload from validated fields and attaches a contract revision "
                    "reference. Human review is mandatory for first invoices, rate changes, "
                    "credits, disputed service, and out-of-scope additions. Stable recurring "
                    "invoices may follow a previously authorized release policy with exception "
                    "thresholds and reconciliation. Use the accounting platform's supported "
                    "idempotency mechanism where available; otherwise retain a local business "
                    "key and query the remote system before retrying an uncertain creation. "
                    "Never interpret an HTTP timeout as proof that an invoice was absent. "
                    "After release, reconcile invoice identifiers, amounts, delivery status, "
                    "payments, and credits back to the ledger. Keep payment credentials in "
                    "the payment provider's controlled workflow rather than in model prompts "
                    "or webhook logs. Collection reminders must pause on an open dispute "
                    "and route to the account owner. Accurate contract-to-cash automation "
                    "protects customer trust by explaining charges, not merely sending them faster."
                ),
                (
                    "Price the automation against completed outcomes rather than token volume "
                    "alone. Consider an illustrative month containing 1,000 eligible administrative "
                    "events across the four plays. Suppose 730 finish unattended and 270 require "
                    "human review before completion: the straight-through completion rate is "
                    "73%, provided retries and failures remain attached to their original events. "
                    "Assume allocated monthly costs of $36 for model requests, $24 for execution "
                    "and queue infrastructure, and $48 for integration subscriptions. Those "
                    "assumptions yield $108 in machine costs, or $0.108 per completed event. "
                    "At two review minutes per referred event, reviewers spend nine hours. "
                    "At a loaded $30 hourly cost, review adds $270. Four additional hours "
                    "of random audits and recovery drills add $120, producing a fully "
                    "counted administrative pipeline cost of $498, or $0.498 per event. "
                    "These are budgeting assumptions, not vendor quotations. If manual "
                    "handling previously averaged four minutes per event, the baseline was "
                    "66.67 hours; thirteen review and audit hours leave about 53.67 hours "
                    "available for other work. Track actual maintenance separately and include "
                    "it before claiming realized savings. Freed time becomes incremental "
                    "profit only when costs fall or usable capacity supports profitable "
                    "contracts without equivalent additional overhead."
                ),
                (
                    "Keep every operating experiment reconciled to the canonical scorecard. "
                    "Conservative annual cleaning contract revenue is $250,000 with an 8% "
                    "net margin and $20,000 owner net profit, implying $230,000 of total "
                    "costs. Base revenue is $725,000 with a 12.0% net margin and $87,000 "
                    "owner net profit, implying $638,000 of costs. Scaled revenue is "
                    "$1,200,000 with a 16% net margin and $192,000 owner net profit, "
                    "implying $1,008,000 of costs. The first two cases use 5 FT + 4 C; "
                    "Scaled uses 6 FT + 5 C, eleven people. These are recognized cleaning "
                    "contract revenues, not customer property values, rent rolls, or payment "
                    "volume. The scorecard does not supply wage schedules, utilization, or "
                    "contractor hours, so validate each case through a bottom-up staffing "
                    "model before treating its headcount as feasible capacity. Place software, "
                    "review time, and implementation amortization inside the relevant total "
                    "cost envelope rather than adding hypothetical savings to published profit. "
                    "The illustrative $498 monthly pipeline equals $5,976 annually; it must "
                    "replace or fit existing costs if canonical profit remains unchanged. "
                    "Reconcile actual results monthly by building, separating labor overruns, "
                    "scope growth, rework, customer credits, and overhead allocation so "
                    "automation receives credit only for measured improvement."
                ),
            ],
            "table": {
                "caption": "Canonical Scenario Reconciliation and Illustrative Automation Unit Economics",
                "headers": [
                    "Scenario or measured operating cost category",
                    "Revenue or event denominator being measured",
                    "Explicit cost arithmetic and accounting treatment",
                    "Profit result or operational decision consequence",
                ],
                "rows": [
                    [
                        "Conservative case with five employees and four contractors",
                        "Annual recognized cleaning contract revenue totals exactly $250,000",
                        "Total annual costs equal $250,000 less $20,000 profit",
                        "Annual owner net profit is $20,000 at 8%",
                    ],
                    [
                        "Base case with five employees and four contractors",
                        "Annual recognized cleaning contract revenue totals exactly $725,000",
                        "Total annual costs equal $725,000 less $87,000 profit",
                        "Annual owner net profit is $87,000 at 12.0%",
                    ],
                    [
                        "Scaled case with six employees and five contractors",
                        "Annual recognized cleaning contract revenue totals exactly $1,200,000",
                        "Total annual costs equal $1,200,000 less $192,000 profit",
                        "Annual owner net profit is $192,000 at 16%",
                    ],
                    [
                        "Illustrative monthly machine costs across four operator plays",
                        "One thousand completed eligible administrative events per month",
                        "Model $36 plus execution $24 plus integrations $48",
                        "Machine cost equals $0.108 per completed administrative event",
                    ],
                    [
                        "Illustrative monthly human review and independent audit costs",
                        "Two hundred seventy reviewed events plus four audit hours",
                        "Nine review hours plus four audit hours times $30",
                        "Human oversight costs $390 before additional maintenance work",
                    ],
                    [
                        "Illustrative combined pipeline cost within existing cost envelopes",
                        "One thousand completed monthly events with 73% unattended completion",
                        "Machine $108 plus human $390 equals $498 monthly",
                        "Annual $5,976 expense must fit canonical scenario costs",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Lock the billable source packet",
                    "action": "Join the signed contract revision, service period, and authorized change records.",
                    "detail": "Reject missing references and route conflicting purchase-order terms to the account owner before drafting charges.",
                },
                {
                    "step": 2,
                    "title": "Validate and review the invoice draft",
                    "action": "Recalculate amounts deterministically and identify every exception requiring a person.",
                    "detail": "Review initial invoices, rate changes, credits, disputes, and extras against their supporting records; the LLM cannot calculate the authoritative total.",
                },
                {
                    "step": 3,
                    "title": "Release once and reconcile remote state",
                    "action": "Submit through the authorized accounting integration using a durable business key.",
                    "detail": "After a timeout, query remote records before retrying; match the returned invoice identifier, customer, currency, and amount.",
                },
                {
                    "step": 4,
                    "title": "Measure collection and automation outcomes",
                    "action": "Reconcile payments and log completed events, review minutes, failures, and recovery work.",
                    "detail": "Pause disputed reminders, investigate unmatched payments, and include audit and maintenance time in the monthly cost report.",
                },
            ],
        },
        {
            "heading": "4. Compound Route Density Through Evidence-Led Distribution and Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build distribution around buildings the pod can actually serve. In the "
                    "territory research play, a scheduled Python job normalizes permitted "
                    "property records, existing CRM accounts, inbound forms, and manually "
                    "verified business contacts into a territory register. Score location, "
                    "building use, estimated service window, approximate cleanable area, and "
                    "fit with existing routes; do not infer private tenant information or "
                    "pretend public floor area equals contracted cleaning area. A reviewer "
                    "checks high-priority opportunities and authorizes outreach claims before "
                    "an approved sequence runs. For commercial email, implement truthful "
                    "sender information, accurate subject lines, required identification "
                    "and address information, and an effective opt-out process under "
                    "15 U.S.C. § 7704. Synchronize suppression across tools and honor "
                    "requests within the statutory period; make internal suppression "
                    "immediate where practicable. Telephone and text outreach require "
                    "separate channel-specific review rather than borrowing email rules. "
                    "Measure cost per qualified walkthrough, proposal, and signed recurring "
                    "contract, then track retained gross contribution after mobilization. "
                    "A hundred distant leads can be worse than one adjacent office "
                    "because travel and supervision consume scarce paid capacity. Feed "
                    "lost-bid reasons and actual first-month labor back into qualification "
                    "so the next campaign selects better buildings instead of simply "
                    "creating more sales activity."
                ),
                (
                    "The programmatic growth loop begins with verified service capability, "
                    "not bulk page production. Maintain a structured inventory of real "
                    "service territories, building types, equipment capabilities, documented "
                    "task standards, and approved customer evidence. Generate draft pages "
                    "for meaningful combinations, such as recurring office cleaning within "
                    "an existing route or clinic cleaning supported by trained personnel. "
                    "Human editors remove duplicate pages, unsupported infection-control "
                    "claims, fabricated testimonials, and locations the crew cannot cover. "
                    "Publish only useful pages containing concrete scope boundaries, "
                    "walkthrough requirements, and an inquiry path that enters the same "
                    "qualification queue. The referral loop begins after resolved inspections "
                    "and stable service, when the billing and distribution play prepares "
                    "a concise account recap. Ask the authorized customer contact for "
                    "an introduction to another property manager or neighboring tenant, "
                    "and obtain permission before publishing customer names, quotations, "
                    "or site images. Track the referring account and resulting contract "
                    "without exposing one customer's inspection history to another. "
                    "A property manager with several buildings can accelerate distribution "
                    "but also increase concentration risk. Review revenue and receivables "
                    "by controlling customer group, not merely street address, and "
                    "balance expansion against collections, service capacity, and the "
                    "cost of replacing that relationship if it ends."
                ),
                (
                    "Make recovery behavior part of the growth system before increasing "
                    "volume. Webhook receivers should acknowledge only durably recorded "
                    "events; workers retry transient failures with bounded exponential "
                    "backoff and jitter, respect provider rate limits, and move exhausted "
                    "attempts into a visible exception queue. Reject invalid signatures "
                    "and malformed payloads without processing them. A daily reconciliation "
                    "compares source-system changes with ledger outcomes because a webhook "
                    "may never arrive. Contract revisions invalidate stale drafts, and "
                    "a per-account pause stops outreach, dispatch changes, or invoice "
                    "release while a dispute is investigated. Maintain local copies "
                    "of approved rosters and emergency contacts, with controlled access "
                    "and a clear synchronization procedure after outages. Test duplicate "
                    "events, delayed events, reordered updates, expired credentials, "
                    "network timeouts, and restoration from backup against representative "
                    "records. Review the four-play dashboard weekly: unattended completion, "
                    "review burden, recovered failures, route labor variance, repeat "
                    "inspection defects, collection aging, and acquisition contribution. "
                    "Expand only the workflows whose error rates and recovery times "
                    "the current pod can support. Candidate #10 remains labor intensive "
                    "at 56/100: the durable flywheel is better evidence producing "
                    "better targeting, denser routes, reliable service, stronger retention, "
                    "and credible referrals, with more paid crew hours added when "
                    "contracted cleaning demand genuinely increases."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheel Triggers, Evidence Requirements, and Failure Recovery",
                "headers": [
                    "Growth or recovery trigger being monitored",
                    "Permitted evidence used by the pipeline",
                    "Automated output prepared for accountable operators",
                    "Failure boundary and practical fallback procedure",
                ],
                "rows": [
                    [
                        "A nearby office submits a recurring service inquiry",
                        "Customer-provided location and requirements matched against actual routes",
                        "Create a qualified walkthrough task with route proximity context",
                        "Owner confirms available labor before promising mobilization dates",
                    ],
                    [
                        "A verified territory supports a useful service page",
                        "Documented crew capabilities and approved local service scope",
                        "Generate an editorial draft with specific walkthrough requirements",
                        "Withhold unsupported claims and remove duplicate low-value pages",
                    ],
                    [
                        "A stable customer becomes eligible for referral outreach",
                        "Resolved inspection history and authorized account contact preferences",
                        "Prepare a concise introduction request without private site evidence",
                        "Account owner reviews requests and honors communication restrictions",
                    ],
                    [
                        "A recipient requests removal from commercial email outreach",
                        "Opt-out event matched against every associated contact record",
                        "Synchronize suppression across CRM exports and sequence tools",
                        "Pause affected sequences until synchronization is positively confirmed",
                    ],
                    [
                        "An accounting webhook never reaches the local receiver",
                        "Daily source reconciliation identifies an unmatched invoice change",
                        "Create a recovery event linked to the remote identifier",
                        "Query existing records before repeating any outward-facing change",
                    ],
                    [
                        "A growing property manager controls several customer buildings",
                        "Revenue and receivables grouped by controlling customer relationship",
                        "Flag concentration trends alongside route density and payment history",
                        "Owner balances new commitments against replacement and collection exposure",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the paperwork around a paid cleaning hour; never mistake faster paperwork for another cleaning hour.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Baseline two weeks of eligible administrative events across the four mapped plays, recording stable identifiers, handling minutes, review needs, and recovery work.",
        "Assign the nine-person pod's owner and supervisor responsibilities, then reconcile field capacity with setup, travel, training, absences, and actual worker relationships.",
        "Implement signed webhook validation, a durable event ledger, duplicate protection, an outbound outbox, bounded retries, and daily source reconciliation.",
        "Pilot one building's versioned ISSA-informed task budget, mobile inspection form, approved chemical records, offline roster, and corrective-action escalation procedure.",
        "Run contract-to-cash reconciliation and measure machine costs, review time, audit time, and maintenance inside the canonical scenario cost envelope.",
        "Launch one route-adjacent acquisition loop and one permission-based referral loop, tracking retained contribution, suppression accuracy, service quality, and customer concentration.",
    ],
    "statutory_citations": [
        {
            "title": "29 U.S.C. § 207 — Maximum hours",
            "url": "https://www.law.cornell.edu/uscode/text/29/207",
            "relevance": "Configure federal overtime alerts for covered nonexempt employees while preserving all actual worked time and applying relevant state requirements.",
        },
        {
            "title": "29 CFR § 785.38 — Travel that is all in the day's work",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-B/part-785/subpart-C/section-785.38",
            "relevance": "Include travel between job sites during the workday in compensable time and route capacity calculations.",
        },
        {
            "title": "29 CFR § 516.2 — Employees subject to minimum wage and overtime provisions",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-V/subchapter-A/part-516/subpart-A/section-516.2",
            "relevance": "Maintain required wage and hour records; scheduling estimates cannot replace actual time and payroll records.",
        },
        {
            "title": "29 CFR § 1910.1200 — Hazard communication",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1200",
            "relevance": "Connect chemical inventories, labels, safety data sheets, and required employee information and training to site operating procedures.",
        },
        {
            "title": "29 CFR § 1910.1030 — Bloodborne pathogens",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-Z/section-1910.1030",
            "relevance": "Where occupational exposure exists, implement applicable exposure control, protective equipment, training, and incident-response requirements.",
        },
        {
            "title": "California Labor Code § 2775 — Employee classification",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2775.&lawCode=LAB",
            "relevance": "Evaluate the applicable classification framework and any valid exceptions before assigning California cleaning work to purported independent contractors.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Implement commercial email sender accuracy, required disclosures, postal address information, effective opt-out handling, and synchronized suppression.",
        },
    ],
}
