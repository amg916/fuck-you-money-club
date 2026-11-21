from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) land flipping team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Parcel Queues, GIS Evidence, Comparable-Sale Monitoring, Title Exceptions, and Buyer Distribution Under TCPA and CAN-SPAM Rules",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #6, Land Flipping, holds Rank #18 with a 72/100 Money-to-Manpower "
        "Score. This chapter maps six operator plays: owner-source intake, parcel "
        "screening, comparable-sale tracking, underwriting and title routing, sale-packet "
        "fulfillment, and buyer distribution with referral recirculation. A 1 FT + 3 C "
        "pod automates repeatable evidence handling while retaining human decisions over "
        "access, environmental constraints, acquisition prices, and published claims. "
        "Python queues, authenticated webhooks, constrained LLM extraction, and "
        "source-linked GIS records provide the infrastructure. Annual owner net profit "
        "remains $24,000 Conservative, $157,250 Base, and $375,000 Scaled; gross parcel "
        "sale proceeds remain the revenue basis. The 70%+ objective measures verified "
        "routine labor removed, not unattended acquisitions or invented operating savings."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$200,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "12% net margin; $24,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$850,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "18.5% net margin; $157,250 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,500,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "25% net margin; $375,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Give six operator plays one evidence spine and four accountable people",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with six bounded plays rather than a collection of unrelated automations. "
                    "Play one captures owner leads and source permissions; play two screens parcels; "
                    "play three tracks comparable sales; play four assembles underwriting and routes "
                    "title questions; play five fulfills sale packets; play six distributes inventory "
                    "and recirculates buyer referrals. These are this chapter's execution mapping for "
                    "Candidate #6, not six independent businesses. The full-time principal owns capital "
                    "allocation, acquisition offers, final representations, and contractor priorities. "
                    "Contractor one maintains GIS evidence and comparable-sale quality. Contractor two "
                    "coordinates documents with title, escrow, surveyors, and local planning staff. "
                    "Contractor three operates listings, buyer qualification, and permitted outreach. "
                    "Professional firms remain external transaction providers; do not disguise additional "
                    "full-time operating roles as software capacity. Each parcel receives an internal "
                    "identifier separate from its assessor parcel number because county numbering formats "
                    "can change after splits. Store county jurisdiction, original identifier, normalized "
                    "identifier, source date, and geometry version together. An acquisition cannot advance "
                    "because a model likes the neighborhood: it advances because the responsible person "
                    "can inspect the evidence bundle and explain the price, exit path, and unresolved "
                    "exceptions without reopening twenty browser tabs."
                ),
                (
                    "Use Python's sqlite3 for a single-worker pilot, then move persistent records into "
                    "a managed database when concurrent writers justify it. Separate parcels, source "
                    "documents, comparable transactions, workflow events, and publication records. An "
                    "authenticated webhook carries an event identifier, timestamp, payload hash, and "
                    "parcel identifier; verify its signature before accepting work. Python hmac and "
                    "hashlib support signature checking, while json, urllib.request, and concurrent.futures "
                    "cover straightforward integrations without a sprawling framework. A unique event key "
                    "makes retries harmless. A transaction inserts the event and pending job together, "
                    "preventing an acknowledged request from disappearing before processing. Treat county "
                    "PDFs, seller emails, and scraped descriptions as untrusted content, never as "
                    "instructions for the extraction model. Request bounded fields with cited page "
                    "references, reject extra fields, validate types, and require null plus a reason "
                    "when evidence is absent. Keep absent values out of public claims. The model cannot "
                    "send offers, alter bank details, publish listings, or mark title exceptions resolved. "
                    "Those privileges belong to separate workflows with named human authority. Restrict "
                    "service accounts to necessary records, rotate secrets outside source code, and "
                    "retain an audit trail showing which evidence supported each consequential change."
                ),
                (
                    "Define the 70%+ target against measured repetitive work, not against every hour "
                    "the business consumes. For an illustrative weekly cohort, record 1,000 baseline "
                    "minutes spent copying identifiers, downloading permitted records, normalizing "
                    "comparables, assembling packets, and updating distribution lists. If automation "
                    "removes 800 minutes but creates 80 minutes of exception handling and routine "
                    "sample review, net removal is 720 minutes, or 72%. Keep acquisition judgment, "
                    "seller negotiation, access interpretation, and closing authorization outside both "
                    "sides of that routine-work comparison. Report their hours separately so a growing "
                    "exception queue cannot masquerade as leverage. Time the same task definitions "
                    "before and after deployment, and include failed runs, duplicate cleanup, and "
                    "contractor supervision. Review the metric weekly by play and county. A strong "
                    "screening script in one county may collapse when another publishes scanned "
                    "ownership rolls or changes its coordinate reference system. Set workload limits "
                    "by reviewer capacity: when unresolved high-risk cases exceed two working days, "
                    "pause new campaign batches rather than letting automation manufacture unfinished "
                    "inventory. The principal receives a short daily digest of blocked parcels, "
                    "capital exposure, stale comparables, and publication changes instead of hundreds "
                    "of individual success notifications."
                ),
            ],
            "table": {
                "caption": "Six Mapped Plays, Pod Ownership, and Consequential Human Decisions",
                "headers": [
                    "Mapped operator play",
                    "Automated work product",
                    "Accountable pod owner",
                    "Decision retained by a person",
                ],
                "rows": [
                    [
                        "Play one captures owner leads with source provenance",
                        "Normalize identifiers and suppress duplicate owner contact records",
                        "Distribution contractor maintains permissions and source quality records",
                        "Principal authorizes campaign scope before any outbound transmission",
                    ],
                    [
                        "Play two screens vacant and infill parcel constraints",
                        "Intersect parcel geometry with dated hazard and zoning layers",
                        "GIS contractor checks geometry alignment and source freshness",
                        "Principal rejects parcels with unresolved access or use constraints",
                    ],
                    [
                        "Play three tracks closed comparable transactions by submarket",
                        "Normalize acreage and flag unusual deed consideration patterns",
                        "GIS contractor verifies transaction evidence and adjustment rationale",
                        "Principal chooses underwriting comparables and defensible acquisition limits",
                    ],
                    [
                        "Play four routes underwriting evidence and title exceptions",
                        "Assemble document references and assign unresolved exception tasks",
                        "Transaction contractor coordinates title professionals and planning responses",
                        "Principal decides whether remaining exceptions justify committing capital",
                    ],
                    [
                        "Play five fulfills reviewed buyer and closing packets",
                        "Render versioned documents using approved parcel facts only",
                        "Transaction contractor maintains document completeness and revision history",
                        "Principal approves factual representations before public packet release",
                    ],
                    [
                        "Play six distributes inventory and recirculates qualified referrals",
                        "Match buyer preferences and attribute inquiries to campaigns",
                        "Distribution contractor maintains channel quality and suppression controls",
                        "Principal approves new channels and material listing changes",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that prevent fast research from becoming expensive inventory",
                "body": (
                    "Experienced land operators automate evidence retrieval aggressively while "
                    "keeping source interpretation visible to the person risking capital."
                ),
                "items": [
                    "Preserve leading zeros in assessor identifiers; store the raw county value beside the normalized search key.",
                    "Keep access evidence separate from road proximity; a visible track can cross private property without an enforceable easement.",
                    "Save the complete recorded instrument for unusual comparables; nominal deed consideration often signals an unusable price observation.",
                    "Ask the title provider which survey and access exceptions would remain in the issued policy before treating insurance as resolution.",
                ],
            },
        },
        {
            "heading": "2. Build parcel screening and comparable tracking around evidence, not model confidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Parcel screening begins with identity and geometry, then advances through constraints "
                    "in order of their ability to destroy the exit. Query authorized ArcGIS REST "
                    "services or licensed data exports, retaining service identifiers, retrieval times, "
                    "coordinate systems, and permitted reuse terms. Geometry should be checked for "
                    "self-intersection, implausible acreage, and obvious displacement before any spatial "
                    "join is trusted. Use FEMA's National Flood Hazard Layer as a screening input, "
                    "USFWS wetland mapping as an indicator, and county zoning maps as a route to "
                    "the controlling ordinance. None independently establishes buildability. Road frontage "
                    "does not establish legal access, a mapped wetland absence does not establish "
                    "jurisdictional absence, and an assessor's land-use code does not establish permitted "
                    "use. Route suspected contamination, dumping, or prior industrial activity for "
                    "qualified environmental review. When an acquisition strategy relies on federal "
                    "landowner liability protections, evaluate the applicable all appropriate inquiries "
                    "requirements under 40 CFR Part 312 and other required conditions before closing. "
                    "For infill sites, collect setbacks, utility connection evidence, minimum dimensions, "
                    "and parking requirements. For minor subdivisions, request the actual local process, "
                    "infrastructure obligations, and timing rather than assuming that a small lot count "
                    "eliminates subdivision review."
                ),
                (
                    "Comparable-sale tracking should distinguish recorded transfers, verified market sales, "
                    "active asking prices, and withdrawn listings. Ingest only records covered by the "
                    "provider's access and reuse permissions; a public search interface is not an "
                    "unlimited redistribution license. Preserve sale date, recording date, acreage, "
                    "transaction type, location, utility condition, access condition, and verification "
                    "source. Python can calculate price per acre, distance, age, and acreage ratios, "
                    "but the GIS contractor decides whether those ratios describe genuinely comparable "
                    "parcels. Exclude family transfers, assemblages, bundled improvements, and nominal "
                    "consideration unless a documented adjustment makes them usable. Record a reason "
                    "for every exclusion so the model cannot quietly select only supportive evidence. "
                    "Set alerts for new verified sales and material listing changes within a defined "
                    "submarket, not an arbitrary statewide radius. Refresh the underwriting packet "
                    "before an offer and again before repricing inventory. A ninety-day-old observation "
                    "can be useful in a thin market, but its age must remain visible. Use an LLM "
                    "to extract stated utility or access claims from documents, never to manufacture "
                    "missing sale prices or adjustment percentages. Show the principal the selected "
                    "evidence and sensitivity range rather than a deceptively precise valuation."
                ),
                (
                    "Design failure recovery before connecting the pipeline to a live seller campaign. "
                    "A county service returning an empty response is an ingestion exception, not "
                    "proof that the parcel has no restrictions. Distinguish successful retrieval with "
                    "zero matching features from authentication failure, timeout, schema drift, and "
                    "invalid geometry. Retry transient failures with exponential backoff and jitter; "
                    "respect rate limits and stop retries on permanent authorization errors. After "
                    "the retry ceiling, move the job to an exception queue with the last valid "
                    "response and a plain-language recovery task. Cache dated source snapshots so "
                    "reviewers can compare revisions, but prohibit stale snapshots from silently "
                    "replacing current evidence. A manual fallback should produce the same structured "
                    "record and provenance fields as the automated path. Test fixtures should include "
                    "a landlocked parcel, a boundary-crossing parcel, a seller name mismatch, a split "
                    "parcel, and a recorded easement that benefits another tract. Compare outcomes "
                    "against reviewed examples before changing extraction prompts or scoring weights. "
                    "A model update that improves average extraction accuracy but misses one critical "
                    "access exception should not reach consequential workflows until the defect is "
                    "understood and corrected. Retain the previous model configuration for rapid rollback."
                ),
            ],
            "table": {
                "caption": "Parcel and Comparable Evidence Matrix With Explicit Failure Recovery",
                "headers": [
                    "Evidence stream and source",
                    "Deterministic screening operation",
                    "Human interpretation requirement",
                    "Recovery when evidence fails",
                ],
                "rows": [
                    [
                        "County assessor exports establish parcel identifiers and acreage",
                        "Compare raw identifiers against normalized keys and geometry",
                        "GIS contractor investigates mismatched boundaries before further scoring",
                        "Retrieve the county record manually and preserve provenance",
                    ],
                    [
                        "Recorded deeds and easements describe claimed access rights",
                        "Extract recording references and link complete source documents",
                        "Title professionals evaluate benefited tracts and policy exceptions",
                        "Hold acquisition progression until access questions receive resolution",
                    ],
                    [
                        "FEMA flood layers identify mapped flood hazard intersections",
                        "Calculate overlap using verified geometry and matching projections",
                        "Reviewer evaluates usable area alongside local development requirements",
                        "Request current mapping and local floodplain administrator guidance",
                    ],
                    [
                        "USFWS mapping and site history indicate environmental concerns",
                        "Flag mapped features and documented prior industrial activities",
                        "Qualified specialists assess concerns beyond desktop screening capability",
                        "Suspend buildability claims while obtaining appropriate field evidence",
                    ],
                    [
                        "County ordinances establish zoning and subdivision process requirements",
                        "Extract dimensional standards with ordinance section references attached",
                        "Planning responses resolve interpretation and proposed subdivision feasibility",
                        "Record written clarification before underwriting the proposed exit",
                    ],
                    [
                        "Recorded sales and licensed listings support comparable selection",
                        "Separate closed evidence from asking prices and transfers",
                        "GIS contractor verifies market relevance and adjustment support",
                        "Widen the documented search without inventing missing prices",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before capital or public claims move",
                "body": (
                    "A completed automation run creates a reviewable packet. It does not "
                    "authorize an offer, a closing instruction, or a new representation."
                ),
                "items": [
                    "Verify parcel identity, seller authority, legal description, and the exact property covered by the proposed purchase agreement.",
                    "Resolve legal access and material title exceptions with the title provider; identify exclusions that would survive policy issuance.",
                    "Confirm the proposed use against current zoning, subdivision requirements, utility evidence, and material environmental findings.",
                    "Approve acquisition limits and public claims against dated sources; confirm recipient permissions and suppression checks before distribution.",
                ],
            },
        },
        {
            "heading": "3. Turn reviewed inventory into repeatable buyer distribution and referral loops",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Programmatic distribution starts with a reviewed fact registry, not a content "
                    "generator allowed to improvise buildability. Maintain approved fields for acreage, "
                    "jurisdiction, asking price, access description, utility evidence, zoning reference, "
                    "and packet version. Python renders parcel pages and buyer PDFs from that registry; "
                    "an LLM may draft concise explanations using only approved facts. Publish through "
                    "an explicit human action, and require renewed review when a material fact changes. "
                    "Use original photography, licensed imagery, and maps whose redistribution terms "
                    "permit the intended use. Pages should answer actual buyer questions about the "
                    "specific parcel, not repeat interchangeable county prose across hundreds of empty "
                    "locations. Include a dated evidence packet, a clear inquiry route, and an accurate "
                    "inventory status. When a parcel sells, remove the active offer promptly while "
                    "retaining useful historical information only where rights and privacy practices "
                    "allow. This creates a search loop: useful parcel evidence attracts qualified "
                    "questions, those questions reveal missing explanations, and improved packets reduce "
                    "repetitive sales work. Measure qualified inquiries and completed sales by source; "
                    "page counts and raw impressions cannot tell the principal whether the loop "
                    "is releasing trapped inventory."
                ),
                (
                    "Outbound acquisition and buyer remarketing need different recipient logic. Seller "
                    "campaigns begin with permitted owner records and careful identity matching; buyer "
                    "campaigns begin with stated geography, budget, intended use, and channel preferences. "
                    "Use Postmark or Amazon SES for appropriate email workflows, subject to their "
                    "policies, and Twilio only where the communication method and permission records "
                    "support the proposed use. For commercial email, 15 U.S.C. 7704 establishes concrete "
                    "requirements including accurate routing information, a physical postal address, "
                    "and a functioning opt-out mechanism. Apply opt-outs across every connected campaign, "
                    "not merely the vendor that received them. For calling and texting, evaluate "
                    "47 U.S.C. 227 and applicable FCC rules, including technology, purpose, recipient, "
                    "permission, and do-not-call requirements. Do not equate a purchased phone number "
                    "with permission. The distribution contractor reviews audience selection and message "
                    "claims before launch; software performs suppression checks again at send time. "
                    "Cap initial batches so replies fit the pod's working capacity. A campaign "
                    "producing forty seller responses that nobody can investigate is not scalable "
                    "acquisition. Route responses into the same parcel evidence spine, then score "
                    "relevance without allowing automated negotiation or binding offer acceptance."
                ),
                (
                    "Build the referral loop around useful sharing rather than exaggerated incentives. "
                    "Offer a parcel packet link that a buyer can forward without exposing their "
                    "identity or other buyers' contact details. Let the recipient choose whether to "
                    "join an inventory list, and record that choice independently. Tag links with "
                    "campaign and parcel identifiers, but keep personal data out of URLs. After "
                    "a successful disposition, ask which property criteria would justify another "
                    "introduction; use that answer to improve matching rather than blasting the "
                    "entire database. Maintain distinct relationships with builders, adjacent owners, "
                    "recreational buyers, and local brokers because their exit criteria differ. Before "
                    "paying referral compensation or marketing property for another owner, assess "
                    "the applicable state's broker licensing rules. California Business and Professions "
                    "Code section 10131 illustrates why compensated activity on behalf of others "
                    "requires separate analysis from selling the operator's own inventory. Track "
                    "time to first qualified inquiry, qualified-inquiry-to-offer conversion, packet "
                    "revision requests, and days from signed contract to closing. These measures "
                    "reveal whether better information is accelerating the cycle. Reuse successful "
                    "channel patterns only within markets where the evidence, buyer demand, and "
                    "contractor response capacity remain comparable."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels With Attribution and Stop Conditions",
                "headers": [
                    "Distribution loop and audience",
                    "Useful asset delivered repeatedly",
                    "Outcome measured against operating effort",
                    "Condition that stops further distribution",
                ],
                "rows": [
                    [
                        "Search discovery reaches buyers investigating specific local parcels",
                        "Reviewed parcel pages provide dated evidence and inquiry routes",
                        "Track qualified inquiries against page maintenance labor hours",
                        "Withdraw claims when source evidence becomes materially outdated",
                    ],
                    [
                        "Buyer matching serves subscribers with documented purchase criteria",
                        "Send relevant inventory packets matching geography and intended use",
                        "Track qualified offers per correctly matched inventory message",
                        "Suppress recipients immediately after their recorded opt-out request",
                    ],
                    [
                        "Owner outreach reaches carefully verified prospective parcel sellers",
                        "Deliver accurate purchase interest with a manageable response route",
                        "Track investigated seller replies against total campaign expense",
                        "Pause batches when unresolved responses exceed reviewer capacity",
                    ],
                    [
                        "Builder relationships surface infill demand and usable specifications",
                        "Provide dimensional evidence and documented utility connection findings",
                        "Track repeat inquiries and actual closed parcel dispositions",
                        "Stop suitability claims when intended development remains unresolved",
                    ],
                    [
                        "Buyer sharing introduces peers through permission-respecting packet links",
                        "Provide useful public packets without revealing recipient identities",
                        "Track self-selected subscribers and attributable qualified buyer inquiries",
                        "Disable links exposing private documents or superseded representations",
                    ],
                    [
                        "Broker relationships connect inventory with established local demand",
                        "Provide approved listing facts and documented compensation arrangements",
                        "Track completed transactions against commissions and coordination hours",
                        "Suspend arrangements when licensing or authority questions remain",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the reviewed parcel facts",
                    "action": "Create an immutable packet version from approved source-linked fields.",
                    "detail": "Record the reviewer, source dates, material exceptions, and release timestamp before generating channel assets.",
                },
                {
                    "step": 2,
                    "title": "Render and inspect channel assets",
                    "action": "Generate the parcel page, buyer PDF, and audience-specific message draft.",
                    "detail": "Compare claims against the frozen registry and check imagery rights, document visibility, links, and inventory status.",
                },
                {
                    "step": 3,
                    "title": "Authorize a capacity-limited release",
                    "action": "Have the principal approve material claims and the contractor verify audience controls.",
                    "detail": "Recheck suppression at transmission, cap the batch, and attach parcel and campaign identifiers to resulting inquiries.",
                },
                {
                    "step": 4,
                    "title": "Reconcile outcomes and repair assets",
                    "action": "Review replies, packet defects, qualified offers, and closed-sale attribution.",
                    "detail": "Correct the central fact registry first, replace affected assets, and stop active promotion immediately when inventory status changes.",
                },
            ],
        },
        {
            "heading": "4. Price every run, preserve the scorecard, and scale only the working loop",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price automation at the unit that creates work: one parcel through one defined "
                    "research pass. In an illustrative batch of 100 parcels, licensed data retrieval "
                    "costs $0.14 per parcel, bounded model extraction costs $0.025, and job execution "
                    "plus storage costs $0.005. The initial batch therefore costs $17.00. Five "
                    "incremental retry attempts at $0.03 add $0.15, producing $17.15 per batch "
                    "or $0.1715 per parcel. These are planning assumptions, not vendor quotations. "
                    "A routine quality sample of twenty records at three minutes each consumes "
                    "one hour; at an illustrative $45 hourly contractor rate, the combined batch "
                    "cost becomes $62.15, or $0.6215 per parcel. That sample is a pipeline "
                    "control, not a substitute for reviewing every consequential offer or public "
                    "claim. Excluded costs include subscriptions, professional diligence, acquisition "
                    "review, seller negotiation, and closing work; allocate them separately before "
                    "judging profitability. Log tokens, provider charges, retries, reviewer minutes, "
                    "and exception type with the batch identifier. Put hard spending ceilings on "
                    "jobs so a changed PDF format cannot trigger an expensive retry spiral. "
                    "Compare cost per reviewed opportunity and per completed sale, not merely "
                    "the cheapest extraction response."
                ),
                (
                    "Keep the canonical scorecard intact when translating throughput into operating plans. "
                    "Conservative gross parcel sale proceeds are $200,000 at a 12% net margin, "
                    "yielding $24,000 annual owner net profit with 1 FT + 3 C. Base proceeds "
                    "are $850,000 at 18.5%, yielding $157,250 with the same pod. Scaled "
                    "proceeds are $1,500,000 at 25%, yielding $375,000 with 2 FT + 4 C. "
                    "For a simple reconciliation, assume each completed parcel sale produces $50,000: "
                    "four sales support Conservative, seventeen support Base, and thirty support "
                    "Scaled. These illustrative counts explain revenue arithmetic, not expected "
                    "market pricing. The corresponding total expense envelopes are $176,000, "
                    "$692,750, and $1,125,000, including acquisition costs and all other costs "
                    "captured by the scorecard. Do not subtract those acquisition costs again, "
                    "and do not add modeled automation savings on top of the stated profits. "
                    "The $50,000–$400,000 startup capital range and $3,000–$15,000 monthly "
                    "operating expense range describe funding requirements, not extra revenue. "
                    "Model the cash calendar separately because purchase deposits, diligence, "
                    "carrying costs, and selling expenses precede many receipts. A profitable "
                    "annual scenario can still run out of cash while inventory waits for buyers."
                ),
                (
                    "Scale the proven loop by increasing reviewed throughput, not by removing reviewers. "
                    "Maintain a weekly control sheet showing parcels ingested, usable evidence bundles, "
                    "offers authorized, contracts signed, purchases closed, inventory age, and completed "
                    "dispositions. Attribute each transition to its originating batch and channel. "
                    "Separate pipeline counts from recognized gross sale proceeds; an inquiry, signed "
                    "purchase contract, or buyer deposit is not automatically a completed parcel sale. "
                    "Ask the accounting provider to apply the appropriate recognition treatment to "
                    "the transaction structure. Expansion into another county should begin with a "
                    "small reviewed cohort and a source-contract checklist, not a cloned scoring "
                    "threshold. For California subdivisions, Government Code section 66424 supplies "
                    "a statutory definition, while local ordinances and applicable map requirements "
                    "determine the actual process. If failure rates rise, disable the affected "
                    "connector, preserve queued work, and continue only the manual tasks that "
                    "reviewers can safely absorb. Restore from a tested backup and replay events "
                    "using their original idempotency keys. Add the second full-time person and "
                    "fourth contractor only when the Scaled workload and cash plan support them. "
                    "The durable advantage is faster evidence-backed turnover without accumulating "
                    "unreviewed liabilities or overstating available capital."
                ),
            ],
            "table": {
                "caption": "Run Economics, Canonical Scenario Reconciliation, and Scaling Controls",
                "headers": [
                    "Economic or operational control",
                    "Explicit arithmetic or measurement basis",
                    "What the number actually represents",
                    "Required operator response or boundary",
                ],
                "rows": [
                    [
                        "Initial automated batch processes one hundred parcel records",
                        "100 times $0.17 produces $17.00 before incremental retries",
                        "Variable retrieval extraction and execution costs for initial attempts",
                        "Track actual charges separately from subscription and diligence expense",
                    ],
                    [
                        "Retry allowance covers five additional bounded processing attempts",
                        "Five times $0.03 raises batch spending to $17.15",
                        "Incremental processing cost after initial attempts already counted",
                        "Stop permanent failures and investigate repeated source format changes",
                    ],
                    [
                        "Routine sample review inspects twenty of one hundred records",
                        "Sixty minutes at $45 adds $45 to batch costs",
                        "Combined sampled batch costs $62.15 before excluded work",
                        "Review every consequential output regardless of routine sample selection",
                    ],
                    [
                        "Conservative case retains one full-time principal and three contractors",
                        "$200,000 less $176,000 total expenses equals $24,000 profit",
                        "Four illustrative $50,000 sales reconcile the 12% margin",
                        "Keep acquisition costs inside the stated total expense envelope",
                    ],
                    [
                        "Base case retains one full-time principal and three contractors",
                        "$850,000 less $692,750 total expenses equals $157,250 profit",
                        "Seventeen illustrative $50,000 sales reconcile the 18.5% margin",
                        "Do not add hypothetical savings beyond canonical owner profit",
                    ],
                    [
                        "Scaled case uses two full-time people and four contractors",
                        "$1,500,000 less $1,125,000 total expenses equals $375,000 profit",
                        "Thirty illustrative $50,000 sales reconcile the 25% margin",
                        "Fund expanded review capacity before increasing county campaign volume",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the movement of evidence, never the invention of certainty.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Assign all six plays to the principal and three contractors, then record baseline repetitive-task minutes for a representative cohort.",
        "Build source-linked parcel records with authenticated event intake, idempotent jobs, immutable evidence snapshots, and separate publication authority.",
        "Test parcel screening and comparable extraction against reviewed access, geometry, environmental, transfer-type, and subdivision edge cases.",
        "Require documented human decisions before offers, material public claims, closing instructions, or new outbound campaign releases.",
        "Launch one reviewed distribution loop with recipient controls, channel attribution, response-capacity limits, and automatic inventory-status suppression.",
        "Reconcile per-run charges, reviewer labor, cash timing, and completed sale proceeds against the three canonical profit and staffing scenarios.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Commercial email workflows must implement accurate transmission information, "
                "required sender identification and postal address information, functional "
                "opt-outs, and timely suppression of recipients who opt out."
            ),
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Calling and texting designs require analysis of the equipment, message "
                "purpose, recipients, permission requirements, and applicable calling restrictions."
            ),
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": (
                "FCC rules supply operational requirements for covered calls and messages, "
                "including applicable permission and do-not-call procedures."
            ),
        },
        {
            "title": "40 CFR Part 312 — Innocent landowners, standards for conducting all appropriate inquiries",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
            "relevance": (
                "Where applicable federal landowner liability protections are part of the "
                "acquisition strategy, environmental inquiry procedures and timing require "
                "qualified review beyond automated map screening."
            ),
        },
        {
            "title": "California Business and Professions Code section 10131 — Real estate broker activities",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=10131.&lawCode=BPC",
            "relevance": (
                "Compensated real estate activities performed for another party require "
                "licensing analysis distinct from the operator's own-inventory sales workflow."
            ),
        },
        {
            "title": "California Government Code section 66424 — Definition of subdivision",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=66424.&lawCode=GOV",
            "relevance": (
                "Proposed parcel divisions require analysis under the statutory definition "
                "and applicable local subdivision and map requirements before pricing a split exit."
            ),
        },
    ],
}
