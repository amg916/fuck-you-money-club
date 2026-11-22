from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-day-launch-sprint-kill-fix-scale-gates",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching commercial lead generation, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "A Four-Person Launch Pod Using HubSpot, Google Workspace, Qualified-Appointment Routing, CAN-SPAM Controls, and Cash-Bounded Cohort Decisions",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #18, Commercial Lead Generation, holds Rank #05 with an 89/100 "
        "Money-to-Manpower Score and 54 mapped plays. This sprint turns that opportunity "
        "into a four-person operating system: one full-time owner plus three contractors "
        "cover targeting, inbox operations, and qualification. Days 1–7 establish the "
        "offer and evidence controls; Days 8–14 test outreach; Days 15–21 validate "
        "appointments and client acceptance; Days 22–30 reconcile cash and select Kill, "
        "Fix, or Scale. The canonical annual owner-profit cases are $20,000 Conservative, "
        "$127,500 Base, and $300,000 Scaled, excluding client-funded advertising pass-through "
        "from operator revenue. A $5,000 first-month cash-burn ceiling, explicit sample "
        "requirements, and separate acquisition and delivery scoreboards prevent early "
        "activity from masquerading as a repeatable business."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retainer and accepted-lead revenue; advertising pass-through excluded",
            "note": "20% net margin; $20,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual retainer and accepted-lead revenue; advertising pass-through excluded",
            "note": "30.0% net margin; $127,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$750,000",
            "context": "Annual retainer and accepted-lead revenue; advertising pass-through excluded",
            "note": "40% net margin; $300,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Bound the Offer, Assign the Pod, and Instrument Every Handoff",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one commercial buyer, one territory, and one acceptance "
                    "definition, rather than launching a general appointment agency. A "
                    "workable initial segment is regional commercial HVAC contractors "
                    "selling maintenance agreements to facilities managers at multi-site "
                    "businesses. Define an accepted appointment as a held conversation "
                    "with an eligible decision-maker, inside the contracted territory, "
                    "with a documented service requirement and an agreed next step. "
                    "A calendar booking alone earns no accepted-appointment fee. On "
                    "Day 1, the owner writes the exclusions, duplicate lookback, dispute "
                    "window, and replacement treatment into a two-page pilot scope. "
                    "Candidate #18 has 54 mapped operator plays; use a proposed sprint "
                    "allocation of 12 offer-and-control slots, 14 acquisition slots, "
                    "16 delivery slots, and 12 reporting-and-retention slots. These "
                    "allocations organize the supplied total, rather than assert titles "
                    "for an unavailable play inventory. Link each actual play identifier "
                    "to a deliverable before declaring coverage. Keep all 54 visible, "
                    "but activate only the dependencies needed for the first pilot. "
                    "The owner alone changes pricing and acceptance rules, preventing "
                    "contractors from quietly selling different promises to different "
                    "prospects during the same measurement cohort."
                ),
                (
                    "Assign the four-person pod by failure domain. The full-time owner "
                    "handles discovery, proposals, client acceptance disputes, and cash. "
                    "The research contractor owns account selection and source provenance; "
                    "the infrastructure contractor owns Google Workspace configuration, "
                    "HubSpot fields, and suppression synchronization; the qualification "
                    "contractor owns callbacks, appointment evidence, and disposition "
                    "coding. Contractors receive bounded assignments, not an assumption "
                    "of full-time availability. For the initial month, reserve 30 research "
                    "hours at $25, 20 infrastructure hours at $40, and 30 qualification "
                    "hours at $25, totaling $2,300. Reserve $650 for inboxes, domains, "
                    "CRM, and scheduling; $450 for data and verification; $300 for "
                    "telephone routing; $300 for targeted professional review; and "
                    "$1,000 contingency. The resulting $5,000 cash ceiling excludes "
                    "owner living costs and contains no client advertising advance. "
                    "Set cumulative spending limits of $1,500, $2,750, $3,875, and "
                    "$5,000 at Days 7, 14, 21, and 30. Record owner hours separately "
                    "so apparently inexpensive delivery cannot conceal an overloaded "
                    "founder. Release contingency only against a named defect, written "
                    "estimate, and measurable completion criterion; buying another "
                    "database is not a repair plan by itself."
                ),
                (
                    "Build the evidence model before importing contacts. HubSpot needs "
                    "account ID, contact source, collection date, geography, campaign "
                    "cohort, suppression status, permission evidence where required, "
                    "appointment outcome, client disposition, and fee eligibility. "
                    "Google Workspace sender domains need correctly published SPF and "
                    "DKIM records plus DMARC reporting and alignment checks. Use "
                    "clearly identified business domains, never misleading lookalikes. "
                    "Separate agency-acquisition records from client-delivery records "
                    "because their denominators answer different questions. An agency "
                    "sales meeting cannot become a delivered client lead. Commercial "
                    "email under 15 U.S.C. § 7704 requires accurate routing information, "
                    "nondeceptive subjects, applicable identification, a valid postal "
                    "address, and a working opt-out; process opt-outs immediately "
                    "operationally, within the statutory outside deadline. Telephone "
                    "review must address 47 U.S.C. § 227, 47 CFR § 64.1200, and "
                    "applicable state restrictions based on destination, technology, "
                    "and message purpose. A business title does not establish that "
                    "a number is a business landline. Configure Twilio initially for "
                    "inbound routing and permitted manual callbacks, with recording "
                    "disabled until applicable notice and permission requirements are "
                    "resolved. Run synthetic records through every route before a "
                    "real prospect enters the system."
                ),
            ],
            "table": {
                "caption": "Days 1–7: Four-Person Pod Deliverables and Evidence Requirements",
                "headers": [
                    "Execution day and accountable operator",
                    "Required deliverable before advancing",
                    "Recorded evidence and quantitative check",
                    "Failure response within the cash ceiling",
                ],
                "rows": [
                    [
                        "Day 1: owner selects one commercial segment",
                        "Signed-off pilot scope defines territory and accepted appointments",
                        "One buyer profile includes five explicit exclusion conditions",
                        "Remove adjacent segments before buying any additional records",
                    ],
                    [
                        "Day 2: research contractor builds account universe",
                        "Fifty seed accounts include source and selection rationale",
                        "Owner audits ten accounts against every targeting condition",
                        "Replace weak sources before expanding the account universe",
                    ],
                    [
                        "Day 3: infrastructure contractor configures sender identity",
                        "Business inboxes publish SPF, DKIM, and DMARC records",
                        "Authentication headers pass tests across three recipient providers",
                        "Pause external sending until identity defects are repaired",
                    ],
                    [
                        "Day 4: owner and infrastructure contractor define records",
                        "HubSpot pipelines separate agency acquisition from client delivery",
                        "Ten synthetic records preserve source and suppression status",
                        "Repair field mappings before importing any prospect contacts",
                    ],
                    [
                        "Day 5: qualification contractor tests appointment handling",
                        "Calendly booking and Twilio routing reach assigned operators",
                        "Ten test events produce ten correct CRM dispositions",
                        "Disable broken routing paths and retain manual ownership",
                    ],
                    [
                        "Day 6: owner reviews outreach and pilot terms",
                        "Messages identify sender, purpose, postal address, and opt-out",
                        "Every proposed channel has documented jurisdiction-specific operating requirements",
                        "Remove unsupported channels instead of assuming business exemption",
                    ],
                    [
                        "Day 7: entire pod rehearses complete workflow",
                        "Suppression, booking, rejection, and billing simulations finish successfully",
                        "Cumulative cash spending remains at or below $1,500",
                        "Carry unresolved defects into repair backlog without prospect exposure",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Checks Before Any Prospect Contact",
                "body": (
                    "The owner records evidence for each check. A failed check blocks "
                    "the affected workflow, not unrelated preparation."
                ),
                "items": [
                    "Verify SPF and DKIM results, DMARC alignment, truthful sender identity, and working reply handling using messages delivered to controlled test accounts.",
                    "Run one synthetic opt-out through every inbox, CRM list, and telephone queue; confirm suppression propagates before another contact attempt can be scheduled.",
                    "Execute ten synthetic bookings and callbacks; require ten correct account matches, assigned owners, timestamps, and disposition records.",
                    "Approve the acceptance rubric, dispute clock, fee trigger, contractor access permissions, and $5,000 first-month spending ceiling in one versioned launch record.",
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Test Acquisition Without Mistaking Inbox Activity for Demand",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use Days 8–14 to test whether the selected buyer recognizes "
                    "the problem and will discuss a paid pilot. Prepare 150 verified "
                    "agency-acquisition contacts, divided into two 75-contact cells "
                    "with comparable account size and territory. These are prospects "
                    "for the agency, not leads delivered to a client. Change only "
                    "the offer framing between cells: maintenance-pipeline visibility "
                    "versus qualified facilities conversations, for example. Keep "
                    "sender identity, contact selection, timing, and follow-up rules "
                    "otherwise stable. Begin with a small manually reviewed batch "
                    "and increase only after authentication, reply handling, and "
                    "suppression work correctly. Multiple inboxes provide legitimate "
                    "ownership and continuity; they do not justify multiplying volume "
                    "to escape provider limits. Follow provider terms and stop rather "
                    "than rotate domains after enforcement. Avoid artificial warm-up "
                    "networks and engagement exchanges. Each message should reference "
                    "a verifiable commercial circumstance, not invented familiarity "
                    "or fabricated customer results. End the week with actual "
                    "conversations, recorded objections, and a corrected offer. "
                    "A weak first cell is a research result, not permission to "
                    "purchase thousands of similar addresses before understanding "
                    "why the selected buyers ignored it."
                ),
                (
                    "Define measurement rules before comparing variants. Unique delivered "
                    "contacts equal attempted unique contacts minus hard bounces; count "
                    "a person once per cohort despite follow-ups. Positive replies "
                    "express relevant interest or request a substantive commercial "
                    "discussion; automated replies, referrals without engagement, and "
                    "polite refusals do not qualify. Mature each contact for seven "
                    "calendar days after first delivery before using reply results "
                    "in a checkpoint. Report booked, held, and qualified-held meetings "
                    "separately. A qualified-held agency meeting requires the buyer "
                    "profile, a relevant demand problem, and a concrete next step. "
                    "For client delivery, maintain a separate accepted-submission "
                    "rate and held-to-booked rate, with exclusions fixed in advance. "
                    "Investigate any spam complaint immediately and pause the affected "
                    "source or message while investigating; provider enforcement "
                    "requires an immediate stop. Pause a source when hard bounces "
                    "exceed 2% across at least 100 attempts, or when three hard "
                    "bounces appear in any smaller launch batch. These are internal "
                    "risk controls, not provider safe harbors. Do not optimize open "
                    "rates: image blocking and automated fetching make them poor "
                    "evidence of buyer demand or message quality."
                ),
                (
                    "Make the paid pilot commercially simple enough to sell and "
                    "operationally narrow enough to fulfill. An illustrative offer "
                    "is a $1,500 service retainer for a defined pilot period plus "
                    "$100 for each accepted held appointment, with an initial cap "
                    "of ten billable appointments. Specify what the retainer buys, "
                    "how duplicate contacts are treated, and when disputed submissions "
                    "must receive evidence-backed decisions. Cash collected upfront "
                    "remains distinct from revenue earned as services are performed. "
                    "Use Stripe or ACH invoices with clear service descriptions "
                    "and keep the client's advertising account and funding separate. "
                    "Never book the client's advertising spend, resulting sales, "
                    "or contract value as agency fee revenue. During discovery, "
                    "ask who can accept appointments, what calendar capacity exists, "
                    "and how quickly the client will return dispositions. A client "
                    "with no available salesperson can destroy a sound campaign "
                    "through missed calls. Candidate #18's first-deal range is "
                    "1–4 months, so a Day 14 launch should produce tested mechanics "
                    "and credible buying signals rather than an invented contract. "
                    "If nobody buys, continue only within the approved test budget "
                    "and repair a specific commercial hypothesis."
                ),
            ],
            "table": {
                "caption": "Days 8–14: Controlled Agency-Acquisition Tests and Commercial Proof",
                "headers": [
                    "Execution day and accountable operator",
                    "Acquisition experiment or commercial task",
                    "Required evidence and measurement boundary",
                    "Repair action when evidence falls short",
                ],
                "rows": [
                    [
                        "Day 8: research contractor completes first test cohort",
                        "Prepare two matched cells of seventy-five verified contacts",
                        "Every record has source, territory, and exclusion review",
                        "Remove uncertain matches before assigning contacts to variants",
                    ],
                    [
                        "Day 9: owner approves initial controlled outreach",
                        "Send a manually reviewed subset through authenticated inboxes",
                        "Replies and opt-outs reach their assigned queues correctly",
                        "Suspend affected inboxes when routing or suppression fails",
                    ],
                    [
                        "Day 10: infrastructure contractor audits delivery evidence",
                        "Compare attempted contacts, hard bounces, and provider responses",
                        "Apply source pause at specified hard-bounce trigger levels",
                        "Correct source quality rather than replacing sender domains",
                    ],
                    [
                        "Day 11: owner handles first substantive buyer conversations",
                        "Record demand problem, buying role, timing, and objections",
                        "Separate relevant commercial interest from automated reply activity",
                        "Rewrite one offer element around the dominant objection",
                    ],
                    [
                        "Day 12: qualification contractor exercises permitted callback workflow",
                        "Route requested callbacks and verify available meeting capacity",
                        "Every callback records request evidence and final disposition",
                        "Remove unsupported dialing methods and repair scheduling ownership",
                    ],
                    [
                        "Day 13: owner presents bounded paid pilot",
                        "Issue service scope with retainer and acceptance-based pricing",
                        "Proposal identifies fee trigger, dispute clock, and appointment cap",
                        "Resolve ambiguous acceptance terms before collecting pilot payment",
                    ],
                    [
                        "Day 14: owner freezes first weekly experiment report",
                        "Report preliminary cells without declaring immature contacts failures",
                        "Cumulative cash spending remains at or below $2,750",
                        "Select one repair hypothesis and preserve original cohort records",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Tactics That Protect a Small Appointment Pod",
                "body": (
                    "Experienced operators protect attribution and calendar capacity "
                    "before optimizing message volume."
                ),
                "items": [
                    "Keep a reason-coded rejection library with redacted evidence; review the five most frequent rejection reasons before purchasing another contact batch.",
                    "Reserve two client-approved calendar blocks before promising appointment delivery; unavailable salespeople create avoidable rejection and churn.",
                    "Preserve the original source and cohort fields when contacts move between inbox owners; reassignment must never reset suppression or attribution.",
                    "Measure qualified-held meetings per owner hour alongside reply rate; an apparently successful campaign can still consume the entire four-person pod.",
                ],
            },
        },
        {
            "heading": "3. Days 15–21: Prove Acceptance, Reconcile Unit Costs, and Remove Manual Breakpoints",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Days 15–21 move from message testing to operational proof. "
                    "If a pilot has sold, onboard exactly one client before "
                    "replicating the workflow. Capture service territory, excluded "
                    "accounts, incumbent relationships, buyer roles, calendar capacity, "
                    "and the designated acceptance contact. Configure a client-specific "
                    "HubSpot pipeline and routing destination without copying unrestricted "
                    "access across accounts. Give contractors only the records required "
                    "for their assignments. Submit each appointment with evidence of "
                    "fit, the prospect's expressed requirement, meeting attendance, "
                    "and the agreed next step. Require client disposition within "
                    "three business days under the pilot agreement, but do not "
                    "silently convert delayed responses into accepted fees. Escalate "
                    "late decisions to the owner and exclude unresolved submissions "
                    "from mature acceptance-rate calculations. Report their count "
                    "and age separately so delays remain visible. If no client "
                    "has bought, use clearly labeled synthetic delivery records "
                    "to test mechanics and continue agency acquisition. Synthetic "
                    "records never enter market-performance numerators. This branch "
                    "preserves useful progress without manufacturing acceptance "
                    "evidence, spending on speculative client campaigns, or making "
                    "Day 21 revenue appear mandatory despite the stated first-deal "
                    "time range."
                ),
                (
                    "Calculate delivery contribution using earned service revenue, not "
                    "calendar activity or bank deposits alone. Suppose one completed "
                    "pilot earns its $1,500 retainer and ten accepted-appointment "
                    "fees of $100, producing $2,500 revenue. Direct contractor "
                    "delivery costs of $900, attributable data and software of "
                    "$250, and telephone charges of $100 leave $1,250 contribution, "
                    "or 50%, before shared overhead and owner economics. A rejected "
                    "appointment earns no acceptance fee; a replacement consumes "
                    "capacity and its actual cost stays in the ledger. Allocate "
                    "shared subscriptions once using a documented rule, avoiding "
                    "double counting between acquisition and delivery. Track agency "
                    "customer acquisition cost separately as acquisition spending "
                    "divided by newly paying clients, while recording owner sales "
                    "hours alongside it. With no paying clients, report spending "
                    "and zero wins rather than a fabricated ratio. For a first "
                    "client, divide acquisition cost by observed monthly contribution "
                    "only when that contribution exists and is reasonably repeatable. "
                    "A single pilot cannot establish lifetime value. This distinction "
                    "prevents a high retainer deposit from disguising expensive "
                    "fulfillment, repeated replacements, and an owner who must "
                    "personally rescue every appointment."
                ),
                (
                    "Reconcile the operating model to the canonical scorecard before "
                    "discussing expansion. Conservative revenue of $100,000 could comprise "
                    "two $3,000 monthly retainers for twelve months, yielding $72,000, "
                    "plus 280 accepted appointments at $100, yielding $28,000. "
                    "The 20% net margin leaves $20,000 annual owner profit and "
                    "$80,000 total modeled costs with 1 FT + 3 C. Base "
                    "revenue of $425,000 could comprise five $5,000 monthly retainers, "
                    "yielding $300,000, plus 1,250 accepted appointments at $100, "
                    "yielding $125,000. At 30.0%, owner profit is $127,500 and "
                    "modeled costs are $297,500 with the same pod. Scaled revenue "
                    "of $750,000 could comprise ten $5,000 monthly retainers, "
                    "yielding $600,000, plus 1,500 accepted appointments at $100, "
                    "yielding $150,000. At 40%, owner profit is $300,000 and "
                    "modeled costs are $450,000 with 2 FT + 4 C. "
                    "These are illustrative fee compositions of exact annual "
                    "targets, not first-month forecasts. Base delivery implies "
                    "roughly 104 accepted appointments monthly across five clients; "
                    "prove staffing capacity before selling that load. Different "
                    "retainer scopes explain why appointment volume alone cannot "
                    "predict total revenue or profit."
                ),
            ],
            "table": {
                "caption": "Days 15–21: Client Delivery, Rejection Forensics, and Contribution Accounting",
                "headers": [
                    "Execution day and accountable operator",
                    "Delivery milestone or evidence-building alternative",
                    "Required quality or accounting verification",
                    "Failure response before adding more workload",
                ],
                "rows": [
                    [
                        "Day 15: owner opens one signed pilot",
                        "Capture territory, exclusions, calendar capacity, and acceptance contact",
                        "Without a buyer, label all delivery rehearsals synthetic",
                        "Continue agency acquisition without purchasing speculative client traffic",
                    ],
                    [
                        "Day 16: research contractor validates client targeting",
                        "Review first client account batch against contractual exclusions",
                        "Owner checks ten records for fit and duplicates",
                        "Correct list logic before making any client-branded contact",
                    ],
                    [
                        "Day 17: qualification contractor verifies appointment evidence",
                        "Attach attendance, buyer role, requirement, and next-step records",
                        "Each submitted appointment has all required acceptance evidence",
                        "Return incomplete submissions for repair before requesting fees",
                    ],
                    [
                        "Day 18: infrastructure contractor automates disposition reporting",
                        "Route acceptance decisions into client-specific reporting and billing",
                        "Unresolved submissions display count, owner, and elapsed age",
                        "Replace brittle automation with a documented manual queue",
                    ],
                    [
                        "Day 19: owner reviews rejection reasons with client",
                        "Separate targeting errors from missed calls and scope changes",
                        "Every rejection receives evidence and one accountable repair owner",
                        "Correct underlying cause before offering repeated free replacements",
                    ],
                    [
                        "Day 20: owner reconciles earned revenue and contribution",
                        "Match service delivery, accepted fees, credits, and direct costs",
                        "Pilot economics exclude advertising pass-through and unearned deposits",
                        "Reprice or narrow delivery when contribution remains structurally weak",
                    ],
                    [
                        "Day 21: entire pod reviews capacity and cash",
                        "Document owner hours, contractor hours, and unresolved service defects",
                        "Cumulative cash spending remains at or below $3,875",
                        "Stop adding workload when unresolved defects consume reserved capacity",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the eligible delivery cohort",
                    "action": "Export submitted appointments with immutable account and cohort identifiers.",
                    "detail": "Include submission dates, held status, acceptance evidence, and the three-business-day disposition deadline.",
                },
                {
                    "step": 2,
                    "title": "Resolve disposition without changing definitions",
                    "action": "Obtain accepted, rejected, or unresolved status from the designated client contact.",
                    "detail": "Retain rejection reasons and unresolved age; never infer acceptance solely from silence or calendar attendance.",
                },
                {
                    "step": 3,
                    "title": "Reconcile fees and actual delivery costs",
                    "action": "Match eligible fees to invoice lines and attribute contractor, data, software, and telephone costs.",
                    "detail": "Record credits and replacements explicitly; keep client advertising and unearned deposits outside earned operator revenue.",
                },
                {
                    "step": 4,
                    "title": "Publish the repair and capacity decision",
                    "action": "Issue a weekly report containing acceptance, held rate, contribution, owner hours, and corrective assignments.",
                    "detail": "Authorize the next bounded batch only after the owner confirms cash headroom and available fulfillment capacity.",
                },
            ],
        },
        {
            "heading": "4. Days 22–30 and Beyond: Apply Sample-Aware Kill, Fix, or Scale Decisions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the final nine days to close evidence gaps rather "
                    "than maximize send counts. Day 22 audits targeting and "
                    "suppression; Day 23 starts the last acquisition contacts "
                    "eligible to mature by Day 30. Day 24 reviews proposals "
                    "and objections; Day 25 reconciles client dispositions; "
                    "Day 26 locks cost attribution; Day 27 reviews contractor "
                    "capacity; Day 28 tests reporting recovery; Day 29 freezes "
                    "the checkpoint packet; Day 30 records the decision. "
                    "For agency acquisition, the cumulative mature sample floors "
                    "are 300 unique delivered contacts at Day 30, 600 at "
                    "Day 60, and 1,000 at Day 90. Require positive replies "
                    "of at least 2% and qualified-held meetings of at least "
                    "1% at each checkpoint. The corresponding minimum counts "
                    "are six and three, twelve and six, then twenty and "
                    "ten. Preserve source and variant cuts because cumulative "
                    "averages can hide deteriorating recent performance. Contacts "
                    "still within seven days of first delivery remain pending. "
                    "An underpowered cohort receives Fix or a bounded extension, "
                    "not a declaration that the market has failed. Missing "
                    "revenue at Day 30 alone does not justify killing an "
                    "opportunity whose first deal can require four months."
                ),
                (
                    "Scale requires delivery proof as well as acquisition response. "
                    "At Days 30, 60, and 90, require at least 10, "
                    "20, and 30 resolved client submissions respectively, acceptance "
                    "of at least 80%, and held-to-booked performance of at "
                    "least 70% across at least 10, 20, and 30 due "
                    "bookings. Due bookings exclude future meetings; resolved "
                    "submissions exclude pending client decisions. Require delivery "
                    "contribution of at least 40%, 45%, and 50%, respectively, "
                    "using actual earned revenue and attributable costs. Commercial "
                    "proof rises from one paying pilot and $1,500 cumulative "
                    "collected service fees, to one renewing or extending client "
                    "and $3,000 collected, to two active paying clients and "
                    "$6,000 collected. Collections exclude advertising funds and "
                    "refundable security deposits. At Day 90, require the oldest "
                    "eligible client to renew or extend; if no client has "
                    "reached a decision date, retention remains unproven. Keep "
                    "all acquisition, delivery, cash, and capacity conditions "
                    "conjunctive: passing one does not offset failing another. "
                    "Day 30 Scale therefore means a controlled next test, "
                    "not an automatic staff expansion. Increase approved contact "
                    "volume or client capacity by no more than 25% per "
                    "two-week cycle, changing only one dimension."
                ),
                (
                    "Kill the affected channel immediately for a material permission "
                    "failure, ignored opt-outs, or provider enforcement; preserve "
                    "evidence and investigate before any restart. Stop discretionary "
                    "spending when its ceiling is reached. For commercial viability, "
                    "Day 60 Kill applies when two sequential repaired tests, "
                    "each with at least 300 mature delivered contacts, produce "
                    "zero positive replies. Day 90 Kill applies when two "
                    "completed delivery repair cycles still leave contribution "
                    "below 20% on at least 30 resolved submissions, or when "
                    "at least ten qualified-held agency meetings and five "
                    "written proposals produce zero collected service fees. "
                    "These are internal stop rules for this offer and segment, "
                    "not universal market verdicts. All other misses enter "
                    "Fix with one owner, one hypothesis, and a fourteen-day "
                    "deadline. Authorize no more than $2,500 additional gross "
                    "cash spending per extension, without automatic renewal; "
                    "cumulative ceilings become $10,000 at Day 60 and $15,000 "
                    "at Day 90 if both monthly extensions are approved. "
                    "Require committed cash for remaining obligations before "
                    "authorizing each extension. Reserve 20% of pod capacity "
                    "for defects and client response. Expand beyond 1 FT "
                    "+ 3 C only after measured workload supports the "
                    "canonical Scaled configuration of 2 FT + 4 C."
                ),
            ],
            "table": {
                "caption": "Days 22–30 Execution Closeout and Quantitative Day 30/60/90 Decisions",
                "headers": [
                    "Day or checkpoint and accountable operator",
                    "Required execution or Scale evidence",
                    "Fix condition and bounded repair response",
                    "Kill condition or spending stop trigger",
                ],
                "rows": [
                    [
                        "Day 22: research contractor audits active targeting",
                        "Recheck source provenance, territory fit, and suppression synchronization",
                        "Repair any mismatched records before the next contact batch",
                        "Stop affected outreach immediately for ignored opt-out instructions",
                    ],
                    [
                        "Day 23: owner closes checkpoint acquisition intake",
                        "Start final contacts that can mature by Day 30",
                        "Label later contacts pending rather than counting premature failures",
                        "Stop source purchasing when approved cash headroom is exhausted",
                    ],
                    [
                        "Day 24: owner reviews discovery and proposals",
                        "Attach buyer problem, commercial next step, and proposal status",
                        "Repair one dominant objection with a revised bounded offer",
                        "Stop unsupported claims or offers the pod cannot fulfill",
                    ],
                    [
                        "Day 25: qualification contractor closes disposition gaps",
                        "Chase overdue decisions and verify held appointment evidence",
                        "Keep unresolved submissions visible outside mature acceptance denominators",
                        "Stop billing disputed appointments until contractual eligibility is resolved",
                    ],
                    [
                        "Day 26: owner freezes cohort cost attribution",
                        "Reconcile earned fees, actual costs, credits, and deposits",
                        "Correct misallocated expenses before calculating pilot contribution margins",
                        "Stop discretionary commitments that exceed remaining approved cash",
                    ],
                    [
                        "Day 27: owner reviews four-person pod capacity",
                        "Document committed hours with twenty percent reserved for defects",
                        "Reduce intake when scheduled work consumes the repair reserve",
                        "Stop promising appointments beyond verified client calendar capacity",
                    ],
                    [
                        "Day 28: infrastructure contractor tests reporting recovery",
                        "Restore exports and replay synthetic routing without duplicate fees",
                        "Repair broken event handling before relying on automated reports",
                        "Disable automation that loses suppression or exposes client records",
                    ],
                    [
                        "Day 29: owner freezes decision packet evidence",
                        "Include mature cohorts, collections, delivery outcomes, costs, and capacity",
                        "List missing samples explicitly and propose one bounded extension",
                        "Reject unsupported Scale claims based on bookings or deposits",
                    ],
                    [
                        "Day 30: owner signs next operating decision",
                        "Publish Kill, Fix, or Scale with named accountable owners",
                        "Authorize fourteen-day repairs only against specific measurable hypotheses",
                        "Stop further discretionary spending at the $5,000 initial ceiling",
                    ],
                    [
                        "Day 30 checkpoint: every Scale condition must pass",
                        "Require 300 mature contacts, six positives, three qualified-held meetings; one paid pilot, $1,500 collected; ten resolved submissions, 80% acceptance, ten due bookings, 70% held, 40% contribution",
                        "Fix any missing sample or missed threshold within fourteen days and at most $2,500 newly authorized spending",
                        "Kill affected channels for material control failures; stop unapproved spending, but do not kill solely for zero early sales",
                    ],
                    [
                        "Day 60 checkpoint: every Scale condition must pass",
                        "Require 600 mature contacts, twelve positives, six qualified-held meetings; one renewal or extension, $3,000 collected; twenty resolved submissions, 80% acceptance, twenty due bookings, 70% held, 45% contribution",
                        "Repair response, acceptance, or renewal weakness; cumulative authorized gross spending cannot exceed $10,000 through Day 60",
                        "Kill the offer-segment test after two repaired 300-contact mature cohorts yield zero positive replies across both cohorts",
                    ],
                    [
                        "Day 90 checkpoint: every Scale condition must pass",
                        "Require 1,000 mature contacts, twenty positives, ten qualified-held meetings; two active paying clients, $6,000 collected, oldest eligible client renewed; thirty resolved submissions, 80% acceptance, thirty due bookings, 70% held, 50% contribution",
                        "Fix any remaining miss without automatic extension; cumulative authorized gross spending cannot exceed $15,000 through Day 90",
                        "Kill below 20% contribution after two completed repairs and thirty resolved submissions, or zero collected fees after ten qualified-held meetings and five proposals",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Scale accepted outcomes that survive cost reconciliation, not inbox activity that survives a screenshot.",
    "diagram_id": "diag-08",
    "action_checklist": [
        "Assign all 54 mapped plays to the proposed 12/14/16/12 workstream register, linking actual play identifiers without claiming unverified coverage.",
        "Name the owner and three contractors, reserve their hours, and approve the $5,000 initial ceiling with cumulative weekly spending limits.",
        "Configure authenticated sender identity, synchronized suppression, separate acquisition and delivery pipelines, and ten successful synthetic routing tests.",
        "Run matched acquisition cohorts with seven-day maturation, explicit positive-reply definitions, and separate booked, held, and qualified-held meeting counts.",
        "Use a signed acceptance rubric to reconcile pilot fees, unresolved submissions, replacements, direct costs, owner hours, and client collections.",
        "Publish Day 30/60/90 decision packets using every sample, quality, contribution, collection, renewal, capacity, and cash condition before expanding workload.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Governs commercial-email header accuracy, subject lines, applicable "
                "identification, postal-address disclosure, opt-out mechanisms, and "
                "honoring opt-out requests within ten business days."
            ),
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Requires channel-specific review of automated and prerecorded calling, "
                "destination numbers, and applicable permission requirements before "
                "introducing outbound telephone workflows."
            ),
        },
        {
            "title": "47 CFR § 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Provides operative federal telephone-solicitation, consent, identification, "
                "and do-not-call rules whose applicability must be assessed for the "
                "actual calling method, recipient, and message."
            ),
        },
        {
            "title": "California Civil Code § 1798.100 — General duties of businesses collecting personal information",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": (
                "For covered businesses, supports concrete collection-notice, purpose "
                "limitation, retention, security, and recipient-contract requirements; "
                "business-contact records require an applicability assessment rather "
                "than a blanket exclusion."
            ),
        },
        {
            "title": "California Penal Code § 632 — Confidential communications",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=632.&lawCode=PEN",
            "relevance": (
                "Restricts recording confidential communications without the required "
                "consent of all parties, making recording settings and jurisdictional "
                "review necessary before retaining appointment-call audio."
            ),
        },
    ],
}
