from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) medical equipment resale team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Serial-Level Python Pipelines, Evidence-Linked Service Histories, Biomed Release Controls, and FDA/HIPAA-Aware Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, ranks #20 with a 85/100 Money-to-Manpower "
        "Score because automation accelerates evidence handling, not physical refurbishment. "
        "This chapter maps three operating plays: diagnostic fleet refresh, surgical equipment "
        "redeployment, and veterinary/aesthetic specialty resale. A 1 FT + 3 C pod connects "
        "serial-level inventory, service-history indexing, buyer qualification, and distribution "
        "through durable Python jobs and evidence-constrained language models. Biomed personnel "
        "retain release authority; commercial staff retain pricing and claims authority. The "
        "canonical annual owner profits remain $25,000 Conservative, $164,000 Base, and $396,000 "
        "Scaled, with the last case requiring 1 FT + 3 C. Measure 70%+ automation against "
        "a fixed repetitive-work denominator, including exception handling, rather than counting "
        "generated listings as completed deals."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "10% net margin; $25,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "16.0% net margin; $164,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "22% net margin; $396,000 annual owner net profit; 1 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Build one serial ledger and divide the four-person pod by decision authority",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Organize Candidate #14 around three explicitly mapped operating plays: diagnostic "
                    "fleet refresh for imaging and diagnostic instruments, surgical equipment redeployment "
                    "for documented systems and accessories, and veterinary/aesthetic specialty resale for "
                    "devices with verified intended use and service support. These are operating lanes, "
                    "not separate revenue forecasts. Give the first full-time operator purchasing, pricing, "
                    "cash allocation, and buyer commitments; give the second inventory control, evidence "
                    "quality, workflow maintenance, and dispatch coordination. Assign four contractors to "
                    "biomedical evaluation, specialist repair, decontamination and preparation, and freight "
                    "and installation coordination, subject to actual qualifications. Contractor availability "
                    "must appear as booked capacity rather than assumed continuous coverage. Across all "
                    "three plays, the shared automation backbone performs intake normalization, document "
                    "indexing, buyer matching, and status propagation. It never determines electrical safety "
                    "or invents missing maintenance. Reserve two daily exception windows so purchasing "
                    "questions do not interrupt every bench task. Each unresolved item receives an owner, "
                    "evidence request, and expiration time. When specialist capacity is full, purchasing "
                    "slows before unfinished inventory consumes cash. This division preserves the canonical "
                    "1 FT + 3 C constraint while making the actual bottleneck visible: qualified release "
                    "hours, not the number of descriptions a model can draft."
                ),
                (
                    "Create a Python service around a serial-level asset ledger, initially using sqlite3 "
                    "transactions and an append-only event table on a single managed host. Assign an "
                    "internal asset UUID because manufacturer serial formats can collide across brands. "
                    "Store manufacturer, model, serial, configuration, accessory manifest, acquisition cost, "
                    "location, custody, commercial reservation, and technical status separately. A technical "
                    "state machine moves from received to quarantined, evaluated, repaired when necessary, "
                    "tested, and released; commercial states track available, reserved, sold, and returned. "
                    "A released asset can still be unavailable because another buyer holds its reservation. "
                    "Use UNIQUE constraints for external event identifiers and atomic conditional updates "
                    "for reservation changes. Link service documents through immutable object identifiers, "
                    "hashlib SHA-256 digests, document dates, and controlled storage locations. Preserve "
                    "revisions instead of replacing old evidence. A nightly reconciliation compares physical "
                    "location scans, reservations, marketplace listings, and the accounting inventory balance. "
                    "Begin with a CSV exception report that a person can understand before adding "
                    "dashboards. Test duplicate serials, partial kits, missing probes, and returns with changed "
                    "accessories. An elegant record that cannot distinguish the machine from its separately "
                    "priced transducer will create expensive fulfillment errors long before it creates useful "
                    "automation. Photograph labels during intake and reconcile them against the ledger before "
                    "any listing leaves draft."
                ),
                (
                    "Treat supplier forms, marketplace notifications, and freight callbacks as untrusted "
                    "events entering the same durable inbox. Verify provider signatures using hmac.compare_digest "
                    "where the provider supports shared-secret signing, enforce timestamp tolerance, and "
                    "record the event before acknowledging receipt. Fetch authoritative order details through "
                    "authenticated APIs when callbacks contain only references. A worker validates the schema, "
                    "checks asset identity, performs the permitted transition, and writes an outbound task "
                    "within the same database transaction. This transactional outbox prevents a successful "
                    "reservation from losing its listing-removal request during a crash. Workers retry transient "
                    "failures with bounded exponential delays and jitter; permanent validation failures move "
                    "to an exception queue. Never retry a payment, shipment purchase, or buyer message "
                    "blindly after a timeout. First query the provider using the original idempotency key "
                    "or order reference. An inventory heartbeat detects stale integrations and suspends "
                    "affected channel availability until reconciliation. Keep a printable released-stock list "
                    "and a controlled manual reservation log for outages, then merge those entries before "
                    "restarting publication. Log actor, previous state, new state, evidence identifiers, and "
                    "correlation ID without copying patient information into application logs. Recovery must "
                    "restore the physical-commercial truth, not merely restart a process that was already "
                    "publishing the wrong stock."
                ),
            ],
            "table": {
                "caption": "Four-Person Pod: Serial-Level Ownership Across Three Operating Plays",
                "headers": [
                    "Assigned operator and working responsibility",
                    "Automated preparation and permitted system behavior",
                    "Human decision that remains explicitly assigned",
                    "Evidence retained for recovery and reconciliation",
                ],
                "rows": [
                    [
                        "First full-time operator owns acquisition and commercial commitments.",
                        "Purchase candidates receive comparable sales and landed-cost summaries.",
                        "Approve buying price after reviewing condition and capital exposure.",
                        "Retain signed purchase terms with the acquisition calculation version.",
                    ],
                    [
                        "Second full-time operator owns inventory truth and integration health.",
                        "Serial events update custody, reservations, and channel availability atomically.",
                        "Resolve conflicting identifiers before allowing commercial publication to proceed.",
                        "Retain label photographs, custody scans, and reservation transition records.",
                    ],
                    [
                        "Biomedical evaluation contractor owns documented device-specific technical testing.",
                        "Service indexes assemble applicable procedures and prior repair evidence.",
                        "Sign the test record against actual measured device performance.",
                        "Retain instrument identifiers, calibration evidence, results, and reviewer identity.",
                    ],
                    [
                        "Specialist repair contractor owns qualified corrective maintenance execution.",
                        "Repair queues group fault descriptions by supported model family.",
                        "Assess repair scope and escalate potential remanufacturing activities.",
                        "Retain installed parts, software revisions, labor records, and retests.",
                    ],
                    [
                        "Preparation contractor owns documented decontamination and complete kit assembly.",
                        "Accessory manifests generate packing comparisons and missing-component exception tasks.",
                        "Verify compatible cleaning procedures and physically inspect package contents.",
                        "Retain cleaning records, kit photographs, and signed packing checklists.",
                    ],
                    [
                        "Freight coordination contractor owns carrier handoffs and installation scheduling.",
                        "Released orders generate draft shipment requests and buyer milestones.",
                        "Confirm transport constraints, receiving capabilities, and installation responsibility.",
                        "Retain carrier receipts, shock indicators, photographs, and delivery exceptions.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Receive and isolate",
                    "action": "Create the asset UUID and quarantine the physical device.",
                    "detail": (
                        "Photograph identifiers, record custody and accessories, and route media "
                        "containing patient information into restricted handling before external processing."
                    ),
                },
                {
                    "step": 2,
                    "title": "Normalize and link",
                    "action": "Build the serial ledger and index the authorized service packet.",
                    "detail": (
                        "Hash each document, preserve its revision, and attach extracted claims "
                        "to page-level evidence without converting absent records into completed service."
                    ),
                },
                {
                    "step": 3,
                    "title": "Review and release",
                    "action": "Obtain separate technical release and commercial publication decisions.",
                    "detail": (
                        "Require device-specific testing, decontamination evidence, data disposition, "
                        "accessory reconciliation, and an approved description before publication."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile and recover",
                    "action": "Compare physical inventory, open reservations, published stock, and dispatched orders.",
                    "detail": (
                        "Pause affected listings when records diverge; repair the source ledger "
                        "and replay only idempotent events with traceable external references."
                    ),
                },
            ],
        },
        {
            "heading": "2. Index service histories without delegating safety, patient-data handling, or device claims",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Service-history indexing begins with a restricted document landing area, not a public "
                    "chat interface. Classify incoming files by asset, document type, date, source, and "
                    "potential patient content. An operator separates service records from clinical exports, "
                    "DICOM studies, screenshots, and embedded storage images before any external model "
                    "submission. Where the relationship creates business associate duties, execute the "
                    "required agreement and configure safeguards before handling electronic protected "
                    "health information for the covered entity. HIPAA applicability depends on the parties "
                    "and activity; purchasing used equipment alone does not resolve that analysis. Apply "
                    "45 CFR 164.310(d) media controls where applicable and select sanitization procedures "
                    "appropriate to the actual storage technology. A factory reset is evidence of a reset, "
                    "not proof that every storage component was sanitized. Inventory removable disks, "
                    "service partitions, printer storage, and cached network credentials. Record the method, "
                    "verification result, technician, asset identifier, and disposition of failed media. If "
                    "sanitization would damage validated configuration or licensed software, stop and obtain "
                    "an authorized service path. Keep clinical material out of the resale knowledge base; "
                    "a service index should answer what was tested and repaired, not reveal who was "
                    "examined. Restrict access by role and retain only the records necessary for the "
                    "documented transaction and applicable obligations."
                ),
                (
                    "For cleared records, combine OCR with a constrained extraction request that returns "
                    "document date, observed serial, procedure, measured results, parts replaced, software "
                    "revision, and supporting page references. Python's json module can parse the response, "
                    "but application validators must enforce required fields, length limits, allowed units, "
                    "and exact asset matches. Treat every document instruction as source text, never as "
                    "permission to change the extraction policy or contact another service. Use SQLite "
                    "full-text search when available, with a keyword fallback, before buying a separate "
                    "vector database. Retrieve the smallest relevant packet and require each generated "
                    "claim to cite an existing document and page. Missing preventive maintenance becomes "
                    "a request for evidence, not a fabricated interval or a reassuring adjective. Confidence "
                    "scores prioritize review; they do not establish accuracy. A model can draft a service "
                    "chronology, identify contradictory dates, and flag a serial mismatch, while a qualified "
                    "reviewer resolves those conflicts. Build a test corpus containing rotated scans, "
                    "handwritten corrections, mixed-device invoices, and superseded reports. Measure "
                    "field-level precision, unsupported claims, serial attribution errors, and review minutes. "
                    "A shorter summary that omits an uncertain assertion is operationally superior to "
                    "a polished narrative that attaches another machine's calibration certificate."
                ),
                (
                    "Separate ordinary servicing from changes that could make the business a remanufacturer. "
                    "FDA's servicing and remanufacturing guidance focuses on whether activities significantly "
                    "change performance, safety specifications, or intended use; a cosmetic label such as "
                    "refurbished does not settle the classification. Route changed energy output, altered "
                    "software functions, substituted critical components, and modified intended-use claims "
                    "to device-specific assessment before work or marketing proceeds. Where manufacturer "
                    "requirements attach, evaluate registration and listing under 21 U.S.C. 360 and "
                    "21 CFR Part 807, applicable premarket obligations, and the Quality Management System "
                    "Regulation under 21 CFR Part 820. Do not automatically assign those obligations to "
                    "every domestic reseller, and do not assume a reseller exemption covers importing "
                    "or manufacturing activities. Identify state licensing and radiation-control requirements "
                    "for the equipment and destination. Surgical systems need accessory and sterilization "
                    "compatibility evidence; diagnostic systems need configuration and performance evidence; "
                    "veterinary/aesthetic transactions need especially careful intended-use and buyer-use "
                    "checks. Veterinary-only status does not make a device exempt from every applicable "
                    "control. The publication workflow should block unsupported safety, certification, "
                    "clearance, and outcome claims. Release requires a signed technical packet and a "
                    "separately reviewed commercial description, both linked to the exact configuration "
                    "offered rather than merely the model family."
                ),
            ],
            "table": {
                "caption": "Evidence-Constrained Service Index and Device Release Matrix",
                "headers": [
                    "Incoming evidence and predictable failure condition",
                    "Automated extraction or comparison performed first",
                    "Assigned reviewer and required consequential decision",
                    "Retained artifact supporting later transaction reconstruction",
                ],
                "rows": [
                    [
                        "Mixed-device invoices contain several unrelated serial references together.",
                        "Extract serial candidates and flag cross-asset attribution conflicts.",
                        "Inventory operator assigns each line to the photographed device.",
                        "Store source pages with line-level attribution and correction history.",
                    ],
                    [
                        "Preventive maintenance reports omit measured values or technician identity.",
                        "Detect missing evidence fields without inventing successful test results.",
                        "Biomedical reviewer requests completion or performs the required testing.",
                        "Store signed results with instrument references and applicable procedure.",
                    ],
                    [
                        "Device storage contains clinical exports and saved network credentials.",
                        "Restricted intake identifies storage components without publishing patient content.",
                        "Authorized technician verifies sanitization and preserves necessary operating configuration.",
                        "Store media inventory, disposition record, verification results, and technician.",
                    ],
                    [
                        "Repair proposal changes critical components or device performance specifications.",
                        "Compare proposed configuration against documented original operating characteristics.",
                        "Qualified specialist assesses servicing versus remanufacturing before execution proceeds.",
                        "Store classification rationale, technical comparisons, and assigned regulatory actions.",
                    ],
                    [
                        "Surgical accessory kits combine incompatible adapters and missing identifiers.",
                        "Compare exact component identifiers against the approved accessory manifest.",
                        "Biomedical reviewer confirms compatibility and resolves all missing components.",
                        "Store compatibility evidence, component photographs, and final kit reconciliation.",
                    ],
                    [
                        "Aesthetic marketing draft implies outcomes absent from supporting documentation.",
                        "Flag unsupported indications and remove uncited generated performance claims.",
                        "Commercial reviewer checks intended use and approves supported wording.",
                        "Store approved copy beside source evidence and configuration snapshot.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before a device becomes publicly available",
                "body": (
                    "Automation can assemble the packet, but named reviewers must close "
                    "these four checks for the actual serial and offered configuration."
                ),
                "items": [
                    (
                        "Match the photographed manufacturer, model, serial, software revision, "
                        "and accessory manifest to the ledger and every cited test report."
                    ),
                    (
                        "Require signed device-specific biomed results and documented "
                        "decontamination using compatible procedures before technical release."
                    ),
                    (
                        "Verify patient-data disposition across all identified media and "
                        "resolve storage failures through a documented authorized service path."
                    ),
                    (
                        "Resolve servicing classification, applicable licensing, buyer-use "
                        "restrictions, and unsupported claims before approving the listing."
                    ),
                ],
            },
        },
        {
            "heading": "3. Turn released inventory into programmatic, referral, and outbound distribution loops",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build programmatic distribution from released inventory rather than generating thousands "
                    "of speculative product pages. Each asset page should expose verified configuration, "
                    "included accessories, documented condition, supported service region, shipping constraints, "
                    "and an appropriately redacted evidence summary. Publish availability from the reservation "
                    "ledger and remove purchase actions immediately when stock becomes unavailable. Separate "
                    "durable model-family guides from serial-specific offers so sold stock does not leave "
                    "a trail of misleading availability. Google Search Console can identify useful queries, "
                    "but search impressions are not qualified demand. Measure inquiries that identify a "
                    "buyer, use case, destination, budget range, and purchasing timeframe. Diagnostic fleet "
                    "refresh pages answer probe compatibility and installation questions; surgical pages "
                    "explain complete-system and accessory boundaries; veterinary/aesthetic pages distinguish "
                    "documented intended use from buyer assumptions. Use actual photographs with licensed "
                    "rights and redact hospital identifiers. A Python publishing job renders approved "
                    "fields into templates, validates outbound links, and queues previews for commercial "
                    "review. Only previously approved factual fields may update automatically afterward. "
                    "Material configuration or performance changes require fresh review. Maintain a page "
                    "revision identifier on every inquiry so the sales operator can reconstruct precisely "
                    "what the buyer saw, including the offered accessories and stated delivery conditions "
                    "at the time of contact."
                ),
                (
                    "Create an evidence-sharing loop that helps a buyer complete internal evaluation. "
                    "After qualification, issue an expiring link to a redacted technical packet containing "
                    "the actual serial, configuration, test summary, accessory checklist, and delivery "
                    "requirements. Let the buyer invite their biomedical engineer or procurement colleague "
                    "without exposing another customer's records or unrestricted service files. Track "
                    "packet requests and subsequent questions at the account level rather than treating "
                    "every recipient as a new lead. Successful installations can produce permissioned "
                    "case studies about operational facts, such as configuration delivered and installation "
                    "coordination, without patient outcomes or unsupported clinical claims. Service contractors "
                    "can refer facilities planning replacements, while satisfied buyers can request alerts "
                    "for matching inventory. Keep referral compensation transparent and review arrangements "
                    "that intersect federally reimbursed business before implementation, including potential "
                    "42 U.S.C. 1320a-7b(b) exposure. Avoid paying clinicians simply for steering reimbursable "
                    "business. The flywheel is specific: better evidence shortens technical diligence, "
                    "completed transactions produce permissioned references, references attract better "
                    "sellers and buyers, and better acquisitions improve the next evidence packet. Measure "
                    "each link separately. A widely forwarded packet that produces no suitable inquiries "
                    "has generated distribution activity, not a proven acquisition advantage or permission "
                    "to increase inventory commitments."
                ),
                (
                    "Outbound begins with a small, documented account universe, not scraped personal "
                    "contact lists. Segment facilities by supported equipment family, geography, service "
                    "coverage, and plausible replacement timing. Use public organizational information "
                    "and authorized CRM records to draft relevant messages without asserting that a "
                    "facility owns a particular machine unless that fact is verified. For commercial "
                    "email, implement accurate sender information, nondeceptive subjects, a valid postal "
                    "address, and functioning opt-out handling under 15 U.S.C. 7704. Synchronize suppression "
                    "records before every send and honor applicable opt-out deadlines. Do not silently "
                    "expand the workflow into automated calling or texting; those channels require "
                    "separate analysis of applicable rules. A human approves the initial segment, offer, "
                    "and message template. Automation may then match released assets, prepare individualized "
                    "drafts, schedule permitted sends, and route replies. Buyer qualification extracts "
                    "requested configuration, intended use, location, installation needs, and timeline, "
                    "but humans resolve suitability and unusual payment or export arrangements. Stop "
                    "sequences immediately on a reply, opt-out, reservation conflict, or stale availability "
                    "signal. Attribute deals using account and asset identifiers, deduplicate referrals "
                    "against outbound records, and report acquisition cost per completed sale. More email "
                    "cannot compensate for an unavailable device or a buyer whose installation requirements "
                    "the pod cannot support."
                ),
            ],
            "table": {
                "caption": "Three-Play Distribution Flywheel With Evidence and Stop Conditions",
                "headers": [
                    "Distribution loop and intended operating play",
                    "Automation output linked to released equipment",
                    "Human review and explicit interruption condition",
                    "Commercial measurement that avoids inflated activity counts",
                ],
                "rows": [
                    [
                        "Diagnostic fleet refresh uses durable model-family research pages.",
                        "Publish verified compatibility fields and current serial-specific availability.",
                        "Pause offers when configuration evidence or installation coverage changes.",
                        "Count qualified facility inquiries and completed diagnostic equipment sales.",
                    ],
                    [
                        "Surgical redeployment uses complete-kit comparison and evidence sharing.",
                        "Generate accessory comparisons from the approved component manifest.",
                        "Stop packet distribution when compatibility questions remain materially unresolved.",
                        "Measure technical diligence duration and accepted complete-kit purchase orders.",
                    ],
                    [
                        "Veterinary and aesthetic resale uses separated intended-use segments.",
                        "Match supported configurations to documented buyer requirements and location.",
                        "Review suitability without inventing permitted uses or clinical outcomes.",
                        "Track supported-use inquiries that convert into completed equipment transactions.",
                    ],
                    [
                        "Buyer colleague sharing extends redacted technical evidence packets.",
                        "Issue expiring access links scoped to one evaluated asset.",
                        "Withdraw access when disclosure scope or reservation status changes.",
                        "Deduplicate account contacts before calculating packet-to-sale conversion rates.",
                    ],
                    [
                        "Permissioned references connect successful deliveries with future qualified buyers.",
                        "Request factual installation feedback after documented delivery acceptance.",
                        "Review publication rights and remove identifying clinical information.",
                        "Attribute referral-assisted transactions without counting the same sale twice.",
                    ],
                    [
                        "Account-based outbound matches supported facilities to released stock.",
                        "Prepare relevant drafts after checking availability and suppression records.",
                        "Stop sequences on replies, opt-outs, stale inventory, or conflicts.",
                        "Calculate acquisition cost using completed sales and attributable effort.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the evidence packet do the selling",
                "body": (
                    "Experienced equipment traders reduce buyer uncertainty before increasing "
                    "traffic. These tactics strengthen all three operating plays."
                ),
                "items": [
                    (
                        "Photograph the serial plate, software version screen, connectors, "
                        "and included accessories during one controlled intake session; "
                        "reusing verified images prevents repeated warehouse interruptions."
                    ),
                    (
                        "Index service histories by serial plus component identifier, not "
                        "only model name; probes, handpieces, and modules often carry "
                        "the evidence that determines whether a system is saleable."
                    ),
                    (
                        "Record doorway dimensions, lift requirements, receiving hours, "
                        "and installation responsibility before quoting freight for large "
                        "diagnostic or surgical systems."
                    ),
                    (
                        "Keep sold model-family pages useful with factual buying guides "
                        "and opt-in availability alerts, while clearly removing the sold "
                        "serial from active purchase and reservation paths."
                    ),
                ],
            },
        },
        {
            "heading": "4. Prove automation economics, rehearse recovery, and scale only the supported workload",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Define the 70% target before instrumenting the workflow. Use repetitive task episodes "
                    "such as intake normalization, service-document indexing, qualification-field extraction, "
                    "shipment-status routing, and approved availability updates. Freeze the task taxonomy "
                    "and baseline handling times for the measurement period; do not split easy tasks "
                    "into smaller units after seeing results. An illustrative monthly cohort contains "
                    "1,000 episodes, of which 740 complete correctly without human intervention and "
                    "260 require exception work. That yields 74% touchless completion, but it does "
                    "not automatically yield 74% labor savings. If baseline repetitive handling averages "
                    "six minutes per episode, the original load is 6,000 minutes. At five minutes "
                    "per exception, plus 200 minutes of sampled review and 200 minutes of maintenance, "
                    "the remaining repetitive-work burden is 1,700 minutes: a 71.7% reduction. Validate "
                    "those times through observation rather than adopting them as operating facts. "
                    "Technical testing, physical preparation, commercial release, and consequential "
                    "buyer decisions remain outside the repetitive-task denominator and still require "
                    "staff capacity. Report their hours beside the automation percentage so leadership "
                    "cannot mistake narrower administrative savings for whole-business automation. "
                    "If rework or monitoring increases, include it immediately. A single erroneous "
                    "configuration propagated to six channels is one source defect with six cleanup "
                    "obligations, not six successful automated episodes."
                ),
                (
                    "Price automated runs using explicit assumptions and reconcile them to the scorecard "
                    "without claiming that software creates additional margin automatically. For an "
                    "illustrative indexed-document run, assume 8,000 input tokens at $2 per million "
                    "and 1,000 output tokens at $8 per million, producing $0.024 of model usage. "
                    "Add $0.010 for OCR and $0.006 for allocated queue, storage, and compute: "
                    "$0.040 per run. These are planning assumptions, not vendor quotations. At "
                    "1,000 runs, direct usage is $40. If a costed review sample covers 10% "
                    "of runs for two minutes each at $45 per hour, it adds $150, "
                    "or $0.190 per run including that review. This narrow sample matches the "
                    "200 review minutes above but excludes exception labor, maintenance, physical "
                    "work, and fixed business software. The canonical Conservative case remains "
                    "$250,000 revenue less $225,000 total costs, yielding $25,000 owner profit. "
                    "Base remains $1,025,000 less $861,000, yielding $164,000; Scaled remains "
                    "$1,800,000 less $1,404,000, yielding $396,000. These are gross equipment "
                    "resale proceeds, not commission revenue or customer equipment value handled "
                    "for others. Acquisition and refurbishment stay inside the cost envelope. "
                    "Allocate payroll, contractor utilization, freight, returns, insurance, storage, "
                    "and automation within those totals rather than adding imagined savings to "
                    "the stated owner profits."
                ),
                (
                    "Run a monthly recovery exercise on a copy of operational data with patient "
                    "material excluded. Replay duplicate callbacks, interrupt an outbound listing update, "
                    "expire an API credential, submit an unreadable service scan, and reserve the "
                    "same asset concurrently from two channels. Expected behavior is controlled "
                    "quarantine, one valid reservation, preserved evidence, and a visible owner for "
                    "each unresolved exception. Restore a backup into an isolated environment and "
                    "compare asset counts, reservation balances, document hashes, and open shipment "
                    "references before declaring recovery successful. During model outages, revert "
                    "to deterministic field extraction and manual indexing; during marketplace outages, "
                    "stop affected publication and maintain the source ledger. During carrier outages, "
                    "prepare documents manually but confirm whether a shipment already exists before "
                    "purchasing another label. Review aging stock weekly by model support, parts "
                    "availability, carrying cost, and realistic exit value. Automation should accelerate "
                    "markdown or parts-recovery decisions when evidence supports them, not conceal "
                    "unsellable inventory behind fresh traffic. The Scaled case explicitly expands "
                    "to 1 FT + 3 C; assign added capacity to the measured bottleneck rather "
                    "than claiming the four-person pod produces that case unchanged. Buy additional "
                    "inventory only when released-stock throughput, specialist availability, cash "
                    "conversion, and exception burden support it. The distribution flywheel must "
                    "remain subordinate to device safety and cash discipline."
                ),
            ],
            "table": {
                "caption": "Automation Proof, Canonical Economics, and Recovery Acceptance Matrix",
                "headers": [
                    "Control or scenario being evaluated explicitly",
                    "Calculation or operational test performed consistently",
                    "Failure signal requiring immediate operator intervention",
                    "Required response and retained verification evidence",
                ],
                "rows": [
                    [
                        "Repetitive episode automation uses a fixed monthly task taxonomy.",
                        "Divide 740 correct touchless completions by 1,000 total episodes.",
                        "Exceptions disappear from reporting or task definitions change midperiod.",
                        "Rebuild the cohort and retain versioned definitions with timestamps.",
                    ],
                    [
                        "Labor reduction includes exceptions, sampled review, and workflow maintenance.",
                        "Compare 1,700 remaining minutes against 6,000 measured baseline minutes.",
                        "Review effort or rework rises beyond the recorded workload.",
                        "Update observed handling times and report consequential work hours separately.",
                    ],
                    [
                        "Illustrative document processing includes direct usage and sampled review.",
                        "Allocate $40 usage plus $150 review across 1,000 runs.",
                        "Retry loops or expanded documents exceed the budgeted processing assumptions.",
                        "Cap attempts and inspect per-document usage before resuming expensive jobs.",
                    ],
                    [
                        "Conservative economics preserve $250,000 revenue and $25,000 owner profit.",
                        "Reconcile $225,000 total costs within the canonical 10% margin.",
                        "Acquisition or repair estimates omit freight, returns, or actual staffing.",
                        "Reprice purchases and update the cost ledger without altering canon.",
                    ],
                    [
                        "Base economics preserve $1,025,000 revenue and $164,000 owner profit.",
                        "Reconcile $861,000 total costs within the canonical 16.0% margin.",
                        "Automation savings are added twice or contractor availability is overstated.",
                        "Remove duplicate savings and reconcile booked contractor hours against capacity.",
                    ],
                    [
                        "Scaled economics require $1,800,000 revenue and expanded staffing capacity.",
                        "Reconcile $1,404,000 costs, $396,000 profit, and 22% net margin.",
                        "The proposed workload still assumes only two full-time operators.",
                        "Budget three full-time operators and five contractors against measured bottlenecks.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Automate the movement of verified evidence, never the invention of equipment readiness."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        (
            "Map diagnostic fleet refresh, surgical redeployment, and veterinary/aesthetic "
            "resale onto one serial ledger with separate technical and commercial states."
        ),
        (
            "Assign the two full-time operators and four contractors named decision "
            "responsibilities, scheduled capacity, and daily exception ownership."
        ),
        (
            "Implement signed webhook intake where supported, transactional reservations, "
            "a durable outbox, bounded retries, and a rehearsed manual recovery path."
        ),
        (
            "Create a restricted service-history pipeline with page-level evidence, "
            "patient-data controls, device-specific testing, and signed publication review."
        ),
        (
            "Launch verified inventory pages, expiring buyer evidence packets, and "
            "suppression-aware account outreach with completed-sale attribution."
        ),
        (
            "Measure fixed-cohort touchless completion, net repetitive labor savings, "
            "fully allocated costs, inventory aging, and canonical scenario reconciliation monthly."
        ),
    ],
    "statutory_citations": [
        {
            "title": "21 U.S.C. 360 — Registration of producers of drugs or devices",
            "url": "https://www.law.cornell.edu/uscode/text/21/360",
            "relevance": (
                "Evaluate registration and listing obligations when the actual activities "
                "include device manufacturing, remanufacturing, or other covered operations; "
                "do not classify the business solely by its resale branding."
            ),
        },
        {
            "title": "21 CFR 807.20 — Who must register and submit a device list",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-B/section-807.20",
            "relevance": (
                "Determine registration and listing responsibilities from the operator's "
                "specific manufacturing, importing, and other covered activities."
            ),
        },
        {
            "title": "21 CFR 807.65 — Exemptions for device establishments",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-D/section-807.65",
            "relevance": (
                "Assess applicable establishment exemptions, including relevant domestic "
                "distribution activities, without extending them to unrelated importing "
                "or manufacturing work."
            ),
        },
        {
            "title": "21 CFR 820.10 — Requirements for a quality management system",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-A/section-820.10",
            "relevance": (
                "Where manufacturer obligations attach, implement the applicable quality "
                "management system requirements rather than substituting a resale checklist."
            ),
        },
        {
            "title": "45 CFR 164.310(d) — Device and media controls",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": (
                "For covered handling of electronic protected health information, address "
                "media disposal, reuse, accountability, and movement through documented controls."
            ),
        },
        {
            "title": "45 CFR 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Determine whether the service relationship requires a business associate "
                "agreement before processing protected health information for a covered entity."
            ),
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Build accurate sender information, nondeceptive subjects, postal-address "
                "disclosure, opt-out functionality, and timely suppression into outbound workflows."
            ),
        },
        {
            "title": "42 U.S.C. 1320a-7b(b) — Illegal remunerations",
            "url": "https://www.law.cornell.edu/uscode/text/42/1320a-7b",
            "relevance": (
                "Evaluate referral compensation involving federally reimbursable business "
                "before introducing equipment sourcing or buyer-introduction payments."
            ),
        },
    ],
}
