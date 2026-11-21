from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "probate-automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 2 FT + 3 C (5 people) probate real estate team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Docket Alerts, Evidence-Bound AI, Court-Sale Checklists, Attorney Referral Loops, and Recorded-Access GIS Diligence",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #9, Probate Real Estate, ranks #16 with a 76/100 Money-to-Manpower "
        "Score. This chapter translates 11 mapped plays into an evidence-first operating "
        "system: authorized docket ingestion, reviewed qualification, executor concierge "
        "coordination, transaction checklists, attorney distribution, and recorded-access "
        "parcel research. A 2 FT + 3 C team targets 70%+ removal of measured repetitive "
        "work without automating authority determinations, valuation commitments, or sale "
        "instructions. Canonical annual owner profits remain $24,000 Conservative, "
        "$140,250 Base, and $315,000 Scaled; recognized revenue means retained brokerage "
        "commissions after brokerage splits, never property values. Python workers and "
        "signed webhooks assemble evidence; people authorize consequential actions. "
        "Costed runs, exception queues, verified source links, and recoverable checklists "
        "turn distribution into repeatable capacity rather than another unstaffed inbox."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "20% net margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$510,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "27.5% net margin; $140,250 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "35% net margin; $315,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Instrument eleven plays before automating the probate evidence chain",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a work ledger, not an AI subscription. The two full-time "
                    "roles are a properly licensed brokerage lead and an operations lead; "
                    "three contractors supply bounded research, transaction support, and "
                    "distribution production within their permitted scopes. Measure repetitive "
                    "minutes by docket collection, identity matching, qualification preparation, "
                    "checklist maintenance, and distribution preparation. In an illustrative "
                    "1,000-minute weekly sample, automate 740 minutes and retain 260 minutes "
                    "of corrections, exceptions, and required review: 74% net repetitive-work "
                    "removal. Include review within the remaining time rather than hiding it "
                    "outside the denominator. This does not mean eliminating 74% of negotiation, "
                    "fiduciary judgment, or relationship work. Freeze the sample definition for "
                    "four weeks, record failures as labor, and compare like-for-like case "
                    "complexity. The eleven mappings below are this chapter's operating "
                    "decomposition, not eleven additional revenue streams. Only the supplied "
                    "GIS mapping carries a canonical play identifier. Each mapping must "
                    "produce either a sourced fact, a reviewed task, or a measurable "
                    "distribution event. Give every event an owner and a terminal state. "
                    "If the team cannot explain what happens when the automation stops, "
                    "the process is not ready for unattended execution."
                ),
                (
                    "Build the intake worker with Python's urllib.request, json, hashlib, "
                    "sqlite3, and datetime modules. Use court-provided feeds, licensed "
                    "data exports, or expressly permitted portal access; do not bypass "
                    "authentication or access restrictions. Many probate courts lack stable "
                    "APIs, so maintain a manual retrieval path and a source-specific "
                    "polling schedule. Store jurisdiction, case number, document identifier, "
                    "retrieval timestamp, source URL, content digest, and parser version. "
                    "An idempotency key combining jurisdiction, case number, document "
                    "identifier, and digest distinguishes a revised filing from a repeated "
                    "notification. Download into quarantine, validate expected content type "
                    "and size, then commit the evidence record and pending job in one "
                    "SQLite transaction. Treat names as matching clues, never unique keys. "
                    "An estate caption can resemble another case, and a decedent's "
                    "mailing address may not identify estate-owned property. Require "
                    "separate links between case, authorized representative, parcel, "
                    "vesting document, and proposed service. Route low-confidence matches "
                    "to the researcher before creating any contact task. Maintain an "
                    "explicit deletion schedule and least-privilege access because public "
                    "court availability does not justify unrestricted internal copying "
                    "of sensitive estate records."
                ),
                (
                    "Use an LLM as an evidence extractor behind a deterministic "
                    "validator. Supply only necessary document excerpts, instruct the "
                    "model to treat document text as data, and permit no outbound "
                    "messages or transaction tools. Require a JSON object containing "
                    "field value, document identifier, page reference, quoted supporting "
                    "text, and extraction status. An absent fact becomes a review task "
                    "rather than a guessed representative, deadline, or sale power. "
                    "Validate types, allowed states, date formats, and source references "
                    "in Python; reject extra keys and unsupported claims. Store the "
                    "model identifier, prompt version, and input digest so reviewers "
                    "can reproduce the decision path without retaining unnecessary "
                    "personal details in logs. For webhook inputs, verify the provider's "
                    "documented signature over the original bytes with hmac.compare_digest, "
                    "enforce timestamp tolerance, and reject reused event identifiers. "
                    "A valid signature proves message origin, not authority to sell "
                    "property. Persist accepted events before acknowledging receipt and "
                    "process them asynchronously. Limit retry counts and route exhausted "
                    "jobs to a visible exception queue. The operations lead owns daily "
                    "queue clearance; the brokerage lead owns any interpretation that "
                    "could change who receives advice or what action proceeds."
                ),
            ],
            "table": {
                "caption": "Eleven mapped operating plays with evidence outputs and recovery ownership",
                "headers": [
                    "Mapped play and bounded operating scope",
                    "Automated input and concrete evidence output",
                    "Human decision before consequential external action",
                    "Failure fallback preserving useful service delivery",
                ],
                "rows": [
                    [
                        "Court docket alerts for newly filed estate matters",
                        "Authorized court feed produces timestamped case change records",
                        "Researcher confirms jurisdiction and correct estate identity",
                        "Manual portal retrieval replaces unavailable authorized feed access",
                    ],
                    [
                        "Estate representative authority extraction for brokerage intake",
                        "Filed appointment documents produce source-linked authority summaries",
                        "Broker and estate counsel resolve document limitations",
                        "Suspend action tasks until current authority evidence arrives",
                    ],
                    [
                        "Parcel ownership resolution across estate and recorder records",
                        "Assessor references and recorded deeds produce parcel links",
                        "Researcher separates tax mailing addresses from ownership",
                        "Order title research when recorded ownership remains ambiguous",
                    ],
                    [
                        "Executor qualification preparation using reviewed service needs",
                        "Intake responses produce prioritized service preparation notes",
                        "Broker confirms client identity and permitted engagement scope",
                        "Replace inferred circumstances with direct authorized intake questions",
                    ],
                    [
                        "Executor concierge coordination for property readiness tasks",
                        "Approved work orders produce scheduled vendor task packets",
                        "Representative approves scope and costs before vendor dispatch",
                        "Offer alternate qualified vendors without changing authorized scope",
                    ],
                    [
                        "Probate transaction checklists tied to verified authority",
                        "Reviewed milestones produce owner-assigned transaction task dependencies",
                        "Transaction lead verifies dates against controlling documents",
                        "Pause dependent tasks and manually reconstruct affected milestones",
                    ],
                    [
                        "Probate attorney referral flywheel through useful reporting",
                        "Permissioned updates produce source-backed estate progress summaries",
                        "Broker reviews recipient authority and relationship disclosures",
                        "Send minimal factual updates through established secure channels",
                    ],
                    [
                        "Programmatic county education pages for organic discovery",
                        "Verified local procedures produce reviewed jurisdiction-specific drafts",
                        "Qualified reviewer checks current rules and misleading claims",
                        "Unpublish outdated pages until source checks are complete",
                    ],
                    [
                        "Professional outbound sequences for relevant probate service relationships",
                        "Business contact research produces relevance-ranked outreach drafts",
                        "Staff checks suppression records and channel-specific requirements",
                        "Use individual professional introductions instead of automated sequences",
                    ],
                    [
                        "Permissioned resource sharing and executor service introductions",
                        "Approved resource requests produce attributable opt-in introductions",
                        "Team verifies sharing permission without exposing estate details",
                        "Provide public educational resources without tracking private recipients",
                    ],
                    [
                        "gis_landlocked_parcel_easement_assemblage: voluntary recorded-access and strip research",
                        "GIS geometry and recorded instruments produce access questions",
                        "Title counsel and surveyor verify rights before commitment",
                        "Exercise diligence contingencies and offer survey-backed voluntary access services",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the source document the operating advantage",
                "body": (
                    "Experienced probate operators reduce rereading and premature outreach "
                    "by preserving the exact evidence that supports each next action."
                ),
                "items": [
                    "Maintain separate fields for appointment date, document retrieval date, and verified sale-authority status; a fresh download does not mean fresh authority.",
                    "Index parcels by jurisdiction and assessor identifier, but preserve the recorded legal description for title and survey review.",
                    "Ask referral attorneys which status changes actually reduce their follow-up work, then automate those updates rather than sending generic market newsletters.",
                    "Keep a county-specific manual retrieval sheet beside every docket connector so staff can recover service during portal redesigns.",
                ],
            },
        },
        {
            "heading": "2. Turn authority, court-sale timing, and parcel access into reviewed checklists",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Model a transaction as dependencies, not a universal closing-date "
                    "template. Begin with representative identity, appointment evidence, "
                    "scope of authority, property ownership, engagement terms, and the "
                    "jurisdiction's sale procedure. California illustrates why branching "
                    "matters: Probate Code section 10501 distinguishes powers available "
                    "under full versus limited authority, while sections 10580 through "
                    "10592 address notice of proposed action procedures when applicable. "
                    "Sales subject to court confirmation follow a different path; "
                    "section 10308 addresses qualifying increased offers at confirmation. "
                    "Do not generalize that path to every state or every California "
                    "estate. Have estate counsel or the responsible qualified professional "
                    "identify the applicable route and record the supporting instrument. "
                    "Only then generate draft tasks for notices, valuation evidence, "
                    "marketing, hearings, objections, and closing conditions. Never derive "
                    "a controlling deadline solely from an LLM reading a docket caption. "
                    "Use the actual order, applicable rule, service details, and reviewed "
                    "calendar calculation. A new objection, amended order, or authority "
                    "change invalidates dependent tasks and triggers re-review. This "
                    "design prevents a polished automated checklist from advancing a "
                    "sale that the representative cannot presently authorize."
                ),
                (
                    "Define consequential outputs narrowly and explicitly: legal-authority "
                    "conclusions, pricing recommendations, listing publication, offer "
                    "submission, vendor spending, notices, and settlement instructions "
                    "require the designated person's review. AI can assemble comparable "
                    "property evidence, but the licensed professional selects adjustments "
                    "and approves pricing. A concierge worker can prepare a cleanout "
                    "scope, but the authorized representative approves disposal and "
                    "spending before anything leaves the property. Store review identity, "
                    "timestamp, evidence version, and approved action scope. Approval "
                    "expires when material inputs change; it does not attach forever "
                    "to the estate record. Use two-person verification for changed "
                    "payment instructions, with an independently sourced callback "
                    "number rather than contact details inside the change request. "
                    "California Business and Professions Code section 10130 anchors "
                    "the licensing boundary for brokerage activity; contractor titles "
                    "do not expand permitted work. Route questions about fiduciary "
                    "duties, conflicts, or contested authority to estate counsel. "
                    "For acquisitions, disclose the operator's buyer-side interest "
                    "and separate it from brokerage representation under the applicable "
                    "duties. Never let an automated qualification score decide which "
                    "family member controls the engagement or whether an estate should "
                    "accept an affiliated buyer's offer."
                ),
                (
                    "The required gis_landlocked_parcel_easement_assemblage play belongs "
                    "inside this evidence system, not outside it. Overlay county "
                    "parcel geometry with roads and candidate access corridors, then "
                    "retrieve deeds, easement instruments, plats, and relevant title "
                    "exceptions. Geometry screens opportunities; it cannot establish "
                    "legal access, extinguishment, scope, maintenance obligations, or "
                    "the right to transfer an easement. Illustratively, screen 100 "
                    "parcels at $0.04 each for $4 of variable compute, review ten "
                    "candidates for twenty minutes each at $45 per hour for $150, "
                    "and purchase three record packets at $60 for $180. Initial "
                    "screening costs $334 before title counsel, survey work, travel, "
                    "or any option payment. If one candidate supports a voluntary "
                    "strip option, a $2,000 option payment plus $3,000 of scoped "
                    "diligence adds $5,000 of separate capital exposure; neither "
                    "amount is brokerage revenue. Obtain title and survey review "
                    "before negotiating recorded access terms, and use a documented "
                    "diligence contingency with a realistic expiry. Do not obstruct "
                    "existing access or manufacture pressure against neighbors. If "
                    "rights or economics fail, exercise diligence contingencies and "
                    "offer survey-backed voluntary access services instead. Recognize "
                    "any separate service economics outside the canonical brokerage "
                    "scorecard."
                ),
            ],
            "table": {
                "caption": "Six probate-specific review checkpoints with invalidation triggers",
                "headers": [
                    "Checkpoint and responsible human review owner",
                    "Required evidence before advancing dependent work",
                    "Automation permitted before the human decision",
                    "Trigger requiring immediate suspension and re-review",
                ],
                "rows": [
                    [
                        "Representative authority reviewed by broker and estate counsel",
                        "Current appointment documents and applicable authority limitations",
                        "Extract source passages and prepare authority comparison",
                        "New order changes powers or identifies contested authority",
                    ],
                    [
                        "Sale procedure selected by responsible qualified reviewer",
                        "Jurisdiction rules and documented authority determine sale route",
                        "Draft separate confirmation and independent-administration task branches",
                        "Objection or court direction changes the documented route",
                    ],
                    [
                        "Marketing release controlled by responsible licensed broker",
                        "Executed engagement and reviewed property facts support publication",
                        "Prepare listing drafts with traceable factual source links",
                        "Ownership discrepancy or material property fact changes emerge",
                    ],
                    [
                        "Concierge spending authorized by the estate representative",
                        "Written scope identifies vendor costs and property handling",
                        "Collect quotes and organize approved scheduling alternatives",
                        "Disputed personal property or increased spending changes scope",
                    ],
                    [
                        "Access rights assessed by title counsel and surveyor",
                        "Recorded instruments and survey evidence support proposed corridor",
                        "Compare parcel shapes and flag possible access conflicts",
                        "Instrument scope contradicts apparent roadway or mapped boundary",
                    ],
                    [
                        "Settlement changes verified by two designated people",
                        "Independent callback and matching transaction records confirm instructions",
                        "Flag changed account details without transmitting estate funds",
                        "Unverified recipient changes or urgent payment pressure appears",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before an external action",
                "body": (
                    "Stop the affected action when any check fails; continue unrelated "
                    "research that does not depend on the disputed fact."
                ),
                "items": [
                    "Verify the representative, property, current appointment evidence, and action-specific authority against source documents.",
                    "Verify the governing sale route, applicable notices, reviewed dates, and unresolved objections with the responsible qualified reviewer.",
                    "Verify the recipient, permitted channel, suppression status, and exact message version before releasing any outreach.",
                    "Verify recorded access evidence, conflict disclosures, capital exposure, and signed diligence terms before committing to a parcel option.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the evidence event",
                    "action": "Persist the source digest, jurisdiction, case identifier, and document version.",
                    "detail": "Reject duplicate events while preserving revised filings as separate evidence versions.",
                },
                {
                    "step": 2,
                    "title": "Assemble the proposed checklist change",
                    "action": "Generate source-linked draft tasks without sending messages or changing commitments.",
                    "detail": "Mark affected dependencies and assign a named reviewer for every consequential change.",
                },
                {
                    "step": 3,
                    "title": "Review and release the bounded action",
                    "action": "Record the reviewer, supporting evidence version, approved scope, and release timestamp.",
                    "detail": "Recheck current evidence immediately before execution so stale reviews cannot authorize new facts.",
                },
                {
                    "step": 4,
                    "title": "Reconcile execution and recover exceptions",
                    "action": "Confirm delivery or completion, then reconcile the action against the durable event ledger.",
                    "detail": "Route uncertain outcomes to manual verification before retrying any externally visible action.",
                },
            ],
        },
        {
            "heading": "3. Build permissioned distribution loops around attorney usefulness and county accuracy",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The attorney referral loop starts with service reliability. Offer "
                    "probate practices a concise, permissioned property-readiness report: "
                    "verified authority status, occupancy questions, approved vendor "
                    "milestones, marketing progress, and unresolved decisions. Share "
                    "only information the client has authorized for that recipient. "
                    "A Python worker can assemble the report from reviewed states, "
                    "but the broker releases it after checking accuracy and tone. "
                    "Measure introductions, accepted consultations, signed engagements, "
                    "and closed commissions by originating relationship. An illustrative "
                    "cohort of twenty attorney relationships producing two introductions "
                    "each creates forty introductions; a 50% consultation rate, 50% "
                    "engagement rate, and 60% closing rate yields six expected closings. "
                    "At $17,000 retained commission each, that cohort contributes "
                    "$102,000 toward, not on top of, the $510,000 Base case. Track "
                    "actual cohorts over the four-to-eighteen-month first-deal horizon "
                    "rather than declaring monthly projections earned revenue. Do not "
                    "pay for referrals involving covered settlement services contrary "
                    "to 12 U.S.C. section 2607 and Regulation X. Document bona fide "
                    "services and any permitted arrangements independently; a newsletter "
                    "label does not cure a disguised referral payment. Relationship "
                    "quality comes from reducing execution uncertainty, not purchasing "
                    "access to distressed families."
                ),
                (
                    "Programmatic acquisition should mean structured publishing, not "
                    "hundreds of interchangeable county pages. Build one reviewed "
                    "page per genuinely supported jurisdiction, using current court "
                    "links, filing terminology, local sale-path explanations, and "
                    "a practical executor property-readiness worksheet. Publish source "
                    "dates and an editorial owner; remove stale procedural claims "
                    "when the source changes. Google Search Console identifies "
                    "questions bringing qualified visitors, while first-party form "
                    "events connect requests to permissioned follow-up. In an "
                    "illustrative monthly cohort, 1,200 relevant visits at a 3% "
                    "request rate produce 36 requests. A 25% consultation rate "
                    "produces nine consultations; a 20% engagement rate produces "
                    "1.8 expected engagements; a 60% eventual closing rate produces "
                    "1.08 expected closings. These are planning expectations, not "
                    "fractional transactions booked into revenue. Deduplicate people "
                    "and estates across attorney and organic sources before "
                    "attributing results. A shareable worksheet can generate a "
                    "second visit from a sibling or adviser without revealing "
                    "a decedent's address or case history. Avoid public client "
                    "maps, fabricated testimonials, and implied court endorsement. "
                    "If a page cannot answer a local question better than "
                    "the underlying official source, link to that source and "
                    "spend the production budget on a useful service workflow."
                ),
                (
                    "Outbound automation should prioritize relevant professional "
                    "relationships rather than converting docket exposure into "
                    "indiscriminate family solicitation. Research probate attorneys, "
                    "qualified property vendors, and other appropriate business "
                    "contacts, then draft an individually relevant introduction "
                    "with a specific operational resource. A public email address "
                    "does not establish permission for every marketing channel. "
                    "Commercial email must follow applicable CAN-SPAM requirements, "
                    "including accurate routing information, required identification, "
                    "a valid postal address, and a functioning opt-out process. "
                    "Telephone and text programs require a separate assessment "
                    "under 47 U.S.C. section 227, implementing rules, and "
                    "applicable state requirements; do not assume manual and "
                    "automated campaigns share identical obligations. Illustratively, "
                    "100 reviewed professional emails costing two minutes each "
                    "at $40 per hour consume $133.33 of labor. Twelve replies, "
                    "four meetings, and one productive referral relationship "
                    "would create useful learning, but no commission until a "
                    "resulting transaction closes. Suppress opt-outs centrally "
                    "before every send, cap frequency, and stop sequences after "
                    "a reply or complaint. When delivery quality deteriorates, "
                    "pause the campaign and inspect targeting, permission, and "
                    "message substance instead of rotating identities or increasing "
                    "volume. The useful loop is better service producing better "
                    "introductions, not more automation producing more intrusion."
                ),
            ],
            "table": {
                "caption": "Distribution loops with explicit attribution and recovery controls",
                "headers": [
                    "Distribution loop and intended recipient value",
                    "Illustrative measurable conversion or production unit",
                    "Release control protecting the relationship and record",
                    "Failure response before increasing distribution volume",
                ],
                "rows": [
                    [
                        "Attorney progress reports reduce repetitive estate status questions",
                        "Forty introductions yield six expected eventual closed transactions",
                        "Broker checks client permission and report evidence freshness",
                        "Correct inaccurate status and suspend the affected report",
                    ],
                    [
                        "County procedure pages answer concrete executor preparation questions",
                        "Twelve hundred visits yield thirty-six requested resource deliveries",
                        "Editorial owner verifies current official jurisdiction source links",
                        "Remove stale claims and publish reviewed replacement wording",
                    ],
                    [
                        "Shareable executor worksheets support private family task coordination",
                        "Measure attributed resource requests without exposing estate identities",
                        "Recipients choose sharing rather than automatic family enrollment",
                        "Provide an untracked public version for sensitive situations",
                    ],
                    [
                        "Professional email introductions offer relevant property execution resources",
                        "One hundred reviewed messages consume three-and-one-third labor hours",
                        "Suppression checks and accurate sender details precede release",
                        "Pause sequences after replies complaints or deteriorating relevance",
                    ],
                    [
                        "Vendor service coordination creates useful reciprocal professional introductions",
                        "Track completed work orders and voluntarily requested introductions",
                        "Representative approves vendor scope without required referral exchange",
                        "Replace unreliable vendors using documented service quality evidence",
                    ],
                    [
                        "Closed transaction learning improves future preparation and attribution",
                        "Reconcile each closed estate to one primary acquisition source",
                        "Broker separates actual commissions from forecast pipeline estimates",
                        "Resolve duplicate attribution before comparing channel acquisition costs",
                    ],
                ],
            },
        },
        {
            "heading": "4. Price every automated run and scale only after recovery works",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Cost the automation at its real unit boundary. Assume an "
                    "illustrative completed evidence run uses 4,000 input tokens "
                    "at $2 per million, 1,000 output tokens at $6 per million, "
                    "and $0.004 of variable compute and storage: $0.018 per run. "
                    "These are budgeting assumptions, not quoted vendor tariffs. "
                    "At 6,000 runs monthly, variable machine cost is $108. If "
                    "8% need three minutes of exception handling, 480 exceptions "
                    "consume 24 hours; at $40 per hour, review costs $960. "
                    "The resulting $1,068 is $0.178 per processed run before "
                    "fixed software, paid court records, acquisition labor, "
                    "ordinary transaction review, and supervision. If exceptions "
                    "double to 16%, handling rises to 48 hours and $1,920; "
                    "total variable machine-plus-exception cost becomes $2,028. "
                    "That sensitivity matters more than trimming a fraction "
                    "of a cent from inference. Record tokens, retrieval charges, "
                    "retries, review minutes, and accepted outputs separately. "
                    "Report both cost per processed run and cost per accepted "
                    "evidence packet so failed output is not disguised as "
                    "productivity. Use weekly samples to compare machine-extracted "
                    "facts against source documents and to identify which "
                    "parser, court feed, or document type generates rework."
                ),
                (
                    "Reconcile improvements to the canonical scorecard without "
                    "changing its revenue definition. Conservative retains $120,000 "
                    "of annual brokerage commissions after splits, incurs $96,000 "
                    "of total modeled costs, and leaves $24,000 owner net profit "
                    "at 20% with 2 FT + 3 C. Base retains $510,000, incurs "
                    "$369,750, and leaves $140,250 at 27.5% with the same "
                    "team count. Scaled retains $900,000, incurs $585,000, and "
                    "leaves $315,000 at 35% with 3 FT + 4 C. Illustrative "
                    "closing bridges are eight closings at $15,000 retained "
                    "each, thirty at $17,000, and fifty at $18,000 respectively; "
                    "actual negotiated commissions and brokerage splits must "
                    "replace those assumptions. Home sale prices, acquisition "
                    "principal, escrow balances, and option proceeds do not "
                    "belong in these brokerage revenue totals. Treat the "
                    "cost envelopes as reconciliation constraints, not proof "
                    "that local wages and contractor demand fit. Build an "
                    "actual staffing budget with hours, payroll costs, and "
                    "contractor scopes before committing spend. The $3,000 "
                    "to $18,000 monthly operating range is not a substitute "
                    "for all-in annual scenario costs. Allocate automation "
                    "expenses within those totals; do not deduct them again "
                    "after calculating canonical profit or count hypothetical "
                    "labor savings as additional revenue."
                ),
                (
                    "Prove recovery before expanding geography or outreach. "
                    "Maintain a durable event ledger, bounded exponential "
                    "backoff for transient failures, and a queue for jobs "
                    "requiring manual intervention. Honor source rate limits "
                    "and stop retrying permanent authorization failures. "
                    "Reconcile source event counts against accepted records "
                    "daily; a silent connector can look healthy while "
                    "missing an amended order. Test restoring the database "
                    "and document index from encrypted backups, then replay "
                    "a controlled event set without duplicate messages or "
                    "vendor bookings. An external send can succeed even "
                    "when its acknowledgment is lost, so inspect provider "
                    "delivery records before replaying uncertain actions. "
                    "Keep a manual board containing current case owners, "
                    "reviewed milestones, and upcoming deadlines for service "
                    "continuity. Expand only after measured repetitive-work "
                    "removal exceeds 70%, review queues clear within "
                    "documented service targets, and source-backed accuracy "
                    "holds across representative samples. Housing downturns "
                    "reduce closing probability, family disputes increase "
                    "review hours, and court delays extend cash collection. "
                    "Stress the plan with fewer closings and longer "
                    "holding periods rather than merely higher software "
                    "usage. Move to the seven-person Scaled configuration "
                    "when sustained workload supports it, preserving named "
                    "owners for authority review, client decisions, and "
                    "distribution quality instead of letting automation "
                    "create ownerless obligations."
                ),
            ],
            "table": {
                "caption": "Unit economics, canonical reconciliation, and failure-recovery thresholds",
                "headers": [
                    "Measured operating unit or canonical scenario",
                    "Exact planning math and recognized revenue boundary",
                    "Cost or labor detail requiring operator attention",
                    "Decision rule and concrete recovery action",
                ],
                "rows": [
                    [
                        "One completed evidence extraction run before human handling",
                        "Four thousand input tokens plus one thousand output tokens",
                        "Illustrative machine charges total $0.018 for each run",
                        "Validate evidence references before accepting the extracted packet",
                    ],
                    [
                        "Monthly workload with eight percent exception incidence",
                        "Six thousand runs produce four hundred eighty exceptions",
                        "Machine and exception handling together cost $1,068 monthly",
                        "Inspect document categories causing repeated three-minute manual reviews",
                    ],
                    [
                        "Monthly workload with sixteen percent exception incidence",
                        "Six thousand runs produce nine hundred sixty exceptions",
                        "Forty-eight review hours raise combined costs to $2,028",
                        "Repair the failing connector before increasing processing volume",
                    ],
                    [
                        "Conservative scenario using two full-time and three contractors",
                        "Eight illustrative closings retain $120,000 after brokerage splits",
                        "$96,000 total modeled costs leave $24,000 owner profit",
                        "Validate actual staffing costs against the twenty-percent margin",
                    ],
                    [
                        "Base scenario using two full-time and three contractors",
                        "Thirty illustrative closings retain $510,000 after brokerage splits",
                        "$369,750 total modeled costs leave $140,250 owner profit",
                        "Preserve the 27.5% margin through reconciled actual expenses",
                    ],
                    [
                        "Scaled scenario using three full-time and four contractors",
                        "Fifty illustrative closings retain $900,000 after brokerage splits",
                        "$585,000 total modeled costs leave $315,000 owner profit",
                        "Expand staffing only when workload supports thirty-five-percent economics",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Automate the evidence trail, not the authority to act."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        "Baseline four weeks of repetitive work by task, including exceptions and human review, then calculate net minutes removed against the same task mix.",
        "Build an authorized docket ingestion ledger with source digests, versioned evidence, idempotent jobs, signed-webhook verification, and a manual retrieval fallback.",
        "Configure jurisdiction-specific transaction dependencies and require action-specific human review for authority, deadlines, marketing, vendor spending, and settlement changes.",
        "Pilot one attorney reporting cohort and one reviewed county resource page, deduplicating estate attribution and enforcing channel-specific suppression controls.",
        "Run the recorded-access GIS screening model with title and survey review, separate capital accounting, and enforceable diligence contingencies before any option commitment.",
        "Reconcile retained commissions and total costs to all three canonical scenarios, then test backup restoration and uncertain-send recovery before expanding volume.",
    ],
    "statutory_citations": [
        {
            "title": "California Business and Professions Code section 10130",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "relevance": (
                "Requires the applicable real estate license for covered brokerage "
                "activity; use it to bound staff and contractor responsibilities."
            ),
        },
        {
            "title": "California Probate Code section 10501",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "relevance": (
                "Identifies actions requiring court supervision and distinctions "
                "associated with limited authority under independent administration."
            ),
        },
        {
            "title": "California Probate Code section 10580",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
            "relevance": (
                "Provides part of the notice of proposed action framework; determine "
                "applicability before generating notice-related transaction tasks."
            ),
        },
        {
            "title": "California Probate Code section 10308",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10308.",
            "relevance": (
                "Addresses increased offers at a real property sale confirmation "
                "hearing; distinguish confirmation sales from other authorized routes."
            ),
        },
        {
            "title": "12 U.S.C. section 2607 — Referral fees and fee splitting",
            "url": "https://www.law.cornell.edu/uscode/text/12/2607",
            "relevance": (
                "Restricts referral payments and unearned fee arrangements involving "
                "covered settlement services, subject to statutory scope and exceptions."
            ),
        },
        {
            "title": "12 CFR section 1024.14 — Prohibition against kickbacks and unearned fees",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1024/section-1024.14",
            "relevance": (
                "Supplies Regulation X detail for evaluating referral arrangements "
                "and payments claimed to compensate actual services."
            ),
        },
        {
            "title": "15 U.S.C. section 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Supports accurate sender information, required commercial-message "
                "content, opt-out handling, and suppression controls for outbound email."
            ),
        },
        {
            "title": "47 U.S.C. section 227 — Restrictions on telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Requires channel-specific assessment before telephone or text "
                "automation; equipment, purpose, recipient, and permission affect applicability."
            ),
        },
    ],
}
