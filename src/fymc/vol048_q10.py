from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 2 C (3 people) data-mined qui tam, sec & irs whistleblower analytics team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Evidence Pipelines, CMS and Open Payments Joins, Counsel-Controlled Seal Tracking, and Retainer-Funded Distribution",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #48, Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics, ranks "
        "#16 of 49 with a 92/100 Money-to-Manpower Score. This chapter maps 11 operator "
        "plays into a counsel-facing evidence factory: conditional startup credits, "
        "three anomaly engines, corroboration, extraction, qualification, seal tracking, "
        "and three distribution loops. Python handles repeatable transformations; people "
        "decide identity, evidentiary sufficiency, confidentiality, and release. The "
        "Conservative, Base, and Scaled annual owner-profit cases remain $30,400, "
        "$219,375, and $510,400. Retainers fund operations while contingent awards stay "
        "outside spendable cash until realized. A timed batch model targets 74% repetitive-work "
        "automation without removing reviewer accountability. Public-disclosure screening, "
        "representative-claim gaps, non-intervention, dismissal, and zero recovery determine "
        "which promising anomalies never become filings."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$95,000",
            "context": "Annual operator revenue from paid retainers and support deliverables",
            "note": "32% net margin; $30,400 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$487,500",
            "context": "Annual operator revenue from paid retainers and support deliverables",
            "note": "45.0% net margin; $219,375 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$880,000",
            "context": "Annual operator revenue from paid retainers and support deliverables",
            "note": "58% net margin; $510,400 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build a replayable anomaly engine before adding model capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the business as a reproducible research service, not an allegation generator. "
                    "Map eleven chapter operating plays to owned queues; the credit play retains its supplied "
                    "identifier, while the other ten names describe this chapter's implementation rather than "
                    "additional catalog identifiers. Plays two through four are CMS anomaly detection, Open "
                    "Payments relationship resolution, and procurement/import corroboration. A Python scheduler "
                    "downloads authorized CMS Part B and Part D releases, Open Payments bulk files, SAM.gov "
                    "records, and lawfully licensed manifest extracts. Use urllib.request for bounded downloads, "
                    "csv and gzip for streaming, hashlib for fingerprints, and sqlite3 for job state. Write each "
                    "source into an immutable landing directory with acquisition time, release date, license "
                    "reference, schema version, and SHA-256 digest. Never interpret an absent or suppressed CMS "
                    "cell as zero activity. Separate provider identifiers from names, preserve historical "
                    "addresses, and attach a confidence score to every proposed join. Partition records by "
                    "reporting period before calculating peer comparisons so revised releases cannot silently "
                    "rewrite an earlier dossier. The owner reviews exceptional joins; one contractor maintains "
                    "ingestion, while another reconstructs source evidence. A failed download produces a stale-source "
                    "warning and pauses dependent scoring rather than recycling yesterday's results as fresh evidence."
                ),
                (
                    "The first mapped play, cloud_ai_startup_credit_aggregation_arbitrage, belongs in the "
                    "capacity budget, not the revenue forecast. A genuine Delaware or Wyoming operating company "
                    "may apply through verified incubator, venture-partner, or founder-perk channels to AWS Activate, "
                    "Microsoft's startup programs, Google Cloud for Startups, Cloudflare, OpenAI, and Anthropic "
                    "where current eligibility permits. The supplied $25,000–$350,000 opportunity range describes "
                    "potential programs and combinations, not an entitlement or an additive balance every applicant "
                    "receives. Record actual award letters, expiration dates, service exclusions, affiliation rules, "
                    "and restrictions on overlapping benefits. Do not manufacture shell entities to repeat an offer, "
                    "resell API keys, or move a client dossier merely to consume credits. Budget the illustrative "
                    "batch at $12 undiscounted machine expense; if $8 is eligible and valid credits cover it, cash "
                    "machine expense becomes $4 until exhaustion. Maintain the $12 shadow cost for pricing. Each "
                    "entity must operate a genuine standalone vertical product with defensible separation. A "
                    "preprovisioned local open-weight service using an appropriately licensed Llama or DeepSeek "
                    "model behind vLLM can preserve extraction capacity, but memory limits, licenses, and benchmark "
                    "results determine suitability. Tested failover reduces interruption; it does not make migration "
                    "instantaneous or eliminate hardware expense."
                ),
                (
                    "Score behavior within relevant peer groups rather than ranking raw billing totals. CMS "
                    "features might include procedure mix, beneficiary-adjusted intensity, and year-over-year "
                    "changes, with specialty and geography held constant where the source permits. Open Payments "
                    "features identify relationships for review, not proof that a payment induced a claim. "
                    "Procurement and manifest features compare award timing, shipping descriptions, country fields, "
                    "and contract requirements; a consignee name alone cannot establish importer responsibility "
                    "or domestic-origin misrepresentation. Price these three engines as one reusable batch: "
                    "40 candidates consume the illustrative $12 machine budget, or $0.30 each, before human work. "
                    "Deduplicate on source identifiers and reporting windows, then attach explanations showing "
                    "which records changed the score. Implement signed incoming webhooks with hmac, timestamp "
                    "checks, idempotency keys, payload limits, and replay rejection; the webhook only enqueues "
                    "work. Use a durable outbox for notifications so a restarted worker cannot issue duplicate "
                    "client messages. Missing schemas move to quarantine, suspicious entity matches require "
                    "review, and rate-limit responses trigger bounded exponential backoff with jitter. When a "
                    "vendor feed disappears, retain the dated last-good snapshot for historical comparison, "
                    "label its age prominently, and stop generating claims about current conduct."
                ),
            ],
            "table": {
                "caption": "Source-to-Queue Controls for the First Four Mapped Plays",
                "headers": [
                    "Operating component and concrete scope",
                    "Automated transformation and unit basis",
                    "Required reviewer decision before use",
                    "Failure recovery and retained evidence",
                ],
                "rows": [
                    [
                        "Play one aggregates eligible startup compute benefits",
                        "Track twelve dollar undiscounted machine batch expense",
                        "Owner verifies actual awards and overlapping restrictions",
                        "Restore paid capacity before valid benefits expire",
                    ],
                    [
                        "Play two examines CMS procedure utilization patterns",
                        "Normalize reporting periods before specialty peer comparisons",
                        "Reviewer distinguishes suppression from genuine zero activity",
                        "Quarantine changed schemas and replay preserved inputs",
                    ],
                    [
                        "Play three resolves Open Payments recipient relationships",
                        "Join identifiers while retaining competing name matches",
                        "Reviewer checks entity identity and relevant chronology",
                        "Detach uncertain relationships instead of forcing matches",
                    ],
                    [
                        "Play four combines procurement and manifest evidence",
                        "Compare dated shipments against specific contract requirements",
                        "Reviewer establishes what each source actually proves",
                        "Suspend unsupported origin allegations pending primary records",
                    ],
                    [
                        "Authorized download workers preserve original source releases",
                        "Stream compressed records without loading entire archives",
                        "Owner approves licenses and permitted acquisition methods",
                        "Resume bounded transfers using validated content fingerprints",
                    ],
                    [
                        "Signed webhook intake queues only authenticated events",
                        "Reject replays using timestamps and idempotency records",
                        "Maintainer inspects unusual senders and signature failures",
                        "Hold failed events without publishing duplicate notifications",
                    ],
                    [
                        "Local model service supplies tested extraction continuity",
                        "Benchmark representative documents before routing production workloads",
                        "Reviewer compares citations against the original documents",
                        "Use deterministic extraction when model quality declines",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make every attractive anomaly cheap to disprove",
                "body": (
                    "The durable asset is a repeatable evidence trail that survives a skeptical "
                    "counsel review, not a large pile of model-generated suspicions."
                ),
                "items": [
                    "Preserve both original and revised CMS releases; a revision can explain an apparent utilization discontinuity before counsel spends interview time.",
                    "Keep separate observed, inferred, and disputed relationship fields in Open Payments joins; never let a confidence score overwrite the source identity.",
                    "Buy manifest coverage only after testing whether the required shipper, consignee, date, and commodity fields exist for the selected trade lane.",
                    "Set credit-expiration alerts at sixty and thirty days, then test the paid and local routes using public documents before protected work depends on them.",
                ],
            },
        },
        {
            "heading": "2. Automate corroboration and dossiers without manufacturing evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Play five is the FOIA and primary-source corroboration builder. Convert each candidate "
                    "into a question ledger: alleged mechanism, relevant period, missing records, possible "
                    "innocent explanation, and the exact record that could resolve the uncertainty. FOIA under "
                    "5 U.S.C. § 552 provides access procedures and exemptions, not an immediate production "
                    "promise or a substitute for discovery. Generate draft requests naming custodians, date "
                    "ranges, record types, and preferred electronic formats; a person approves scope and "
                    "submission because the request itself communicates information outside the firm. Track "
                    "acknowledgment, tracking number, fee correspondence, production batches, and appeal dates "
                    "without treating the statutory determination period as a delivery deadline. For each "
                    "produced file, preserve the original, extract text into a separate derivative, and log "
                    "redactions and missing attachments. Budget $2 of the $12 machine batch for retrieval "
                    "orchestration and indexing; fees and licensed records are separately authorized expenses "
                    "inside the engagement budget. If an agency withholds documents, record the asserted "
                    "exemption and route the decision to counsel. Switch to accessible primary sources, "
                    "narrow the hypothesis, or close the candidate rather than filling evidentiary holes "
                    "with an LLM's plausible reconstruction of records it has never seen."
                ),
                (
                    "Play six is citation-bound extraction and dossier assembly. A model receives only "
                    "approved document excerpts, a constrained field schema, and instructions to return "
                    "quoted spans with page or row locators. Treat embedded document instructions as hostile "
                    "content: they cannot request secrets, change destinations, invoke tools, or amend the "
                    "extraction contract. Parse returned JSON with strict size and type checks; validate "
                    "every quoted span against stored text before it enters the evidence ledger. Python's "
                    "stdlib handles orchestration, JSON, and hashing; PDF parsing and OCR require separately "
                    "selected services or local executables rather than pretending they exist in the stdlib. "
                    "Budget $4 for model extraction, $3 for approved OCR or parsing, and $3 for storage, "
                    "scoring, and orchestration, including the $2 corroboration allocation already described. "
                    "Those categories total $12 rather than adding a second retrieval charge. Prepare an "
                    "evidence packet containing source inventory, chronology, entity map, competing explanations, "
                    "and unresolved questions. A deterministic template supplies headings and source links "
                    "when the model fails. No model invents missing invoices, beneficiary details, contract "
                    "clauses, interviews, or representative claims. Counsel receives an explicitly incomplete "
                    "packet when decisive documents remain unavailable, with each unsupported proposition "
                    "removed from the factual narrative."
                ),
                (
                    "Play seven is counsel-fit qualification, with an explicit separation between statistical "
                    "interest and filing sufficiency. The full-time owner checks practice focus, jurisdiction, "
                    "conflicts routing, available evidence, engagement economics, and willingness to pay for "
                    "bounded support work. Counsel assesses the FCA public-disclosure bar under 31 U.S.C. "
                    "§ 3730(e)(4), including the statutory channels of disclosure, substantially similar "
                    "allegations, original-source requirements, and the government's ability to oppose dismissal. "
                    "Publicly accessible data does not automatically create a viable relator, and neither "
                    "does it automatically resolve the statutory analysis. Build a Rule 9(b) matrix linking "
                    "who, what, when, where, and how to actual source passages; representative-claim demands "
                    "and acceptable alternatives vary by circuit and factual context. Aggregate CMS summaries "
                    "often cannot establish claim submission, falsity, or knowledge. The model flags missing "
                    "elements but never declares them satisfied. For four accepted packets from forty candidates, "
                    "the illustrative $272 fully loaded batch costs $68 per accepted packet; rejection of all "
                    "forty is a valid outcome, not permission to lower standards. If counsel declines, retain "
                    "the reason, stop external circulation, and reuse only nonconfidential method lessons "
                    "rather than shopping an identifiable allegation across a mailing list."
                ),
            ],
            "table": {
                "caption": "Corroboration, Extraction, and Counsel Qualification Evidence Matrix",
                "headers": [
                    "Question requiring a concrete answer",
                    "Automated packet component and source",
                    "Human examination that remains mandatory",
                    "Stop condition and practical fallback",
                ],
                "rows": [
                    [
                        "Which primary record could disprove the hypothesis",
                        "Question ledger links missing records to propositions",
                        "Analyst identifies plausible innocent explanations before escalation",
                        "Close candidates supported only by unexplained correlations",
                    ],
                    [
                        "Which agency records warrant a bounded request",
                        "FOIA draft specifies custodians dates and formats",
                        "Counsel checks request content before external submission",
                        "Narrow requests when burdens or exemptions dominate",
                    ],
                    [
                        "Which exact passage supports each factual statement",
                        "Extraction schema requires quotations and stable locators",
                        "Reviewer checks quotations against preserved source files",
                        "Remove statements whose quoted support cannot validate",
                    ],
                    [
                        "Which entity actually appears in the source",
                        "Entity map retains identifiers and alternative matches",
                        "Reviewer resolves names using independent primary records",
                        "Keep ambiguous parties separate until identity resolves",
                    ],
                    [
                        "Which allegations face the public disclosure bar",
                        "Disclosure timeline records channels dates and similarities",
                        "Counsel applies statutory exceptions to actual facts",
                        "Stop relator positioning when counsel finds disqualification",
                    ],
                    [
                        "Which claim particulars remain absent from evidence",
                        "Rule 9(b) worksheet indexes available claim particulars",
                        "Counsel evaluates circuit requirements and pleading sufficiency",
                        "Request specific records instead of inventing particulars",
                    ],
                    [
                        "Which firm can responsibly evaluate this engagement",
                        "Practice fit score uses public professional information",
                        "Owner checks conflicts routing and engagement boundaries",
                        "Send generic capabilities before sharing sensitive allegations",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the authorized evidence inputs",
                    "action": "Create a batch manifest and hash every acquired source.",
                    "detail": "Record acquisition authority, reporting period, source version, and permitted recipients before extraction begins.",
                },
                {
                    "step": 2,
                    "title": "Generate bounded factual derivatives",
                    "action": "Run deterministic joins, constrained extraction, and quotation validation.",
                    "detail": "Quarantine schema changes, suspicious document instructions, uncertain identities, and unsupported factual propositions.",
                },
                {
                    "step": 3,
                    "title": "Conduct adversarial human examination",
                    "action": "Review alternative explanations, disclosure history, and claim-specific gaps.",
                    "detail": "The analyst verifies sources; licensed counsel evaluates filing sufficiency and program eligibility.",
                },
                {
                    "step": 4,
                    "title": "Release only the authorized packet",
                    "action": "Approve the named recipient and export a versioned evidence dossier.",
                    "detail": "Log the export digest and decision, reconcile delivery, and preserve a replayable record without placing matter content in general telemetry.",
                },
            ],
        },
        {
            "heading": "3. Fund the service with retainers and isolate contingent recovery",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Play eight is the counsel-controlled litigation-support and seal tracker. Store matter "
                    "identifiers, named access holders, counsel instructions, deadlines, and authorized export "
                    "history in a separate protected workspace. Under 31 U.S.C. § 3730(b)(2), FCA complaints "
                    "are filed by licensed relator counsel under seal, initially for at least sixty days, "
                    "with statutory government service and disclosure requirements; extensions can continue "
                    "far longer. Do not synchronize protected matter titles into ordinary CRM records, public "
                    "issue trackers, shared calendars, model telemetry, or marketing analytics. A reminder "
                    "uses an opaque identifier and points authorized counsel to the protected record. "
                    "Retain the actual sealing order because restrictions are matter-specific. A seal "
                    "breach creates serious litigation and recovery risk, but dismissal or share loss is "
                    "not mechanically automatic in every case. Route SEC Form TCR and IRS Form 211 through "
                    "counsel under this operating model, with separate program-specific intake and deadline "
                    "rules. Never transplant the FCA seal process onto those programs. The often-cited "
                    "2–5+ year horizon describes possible investigation and recovery delays, not a universal "
                    "seal duration or an expected payment date. If instructions conflict or access fails, "
                    "suspend exports and seek counsel's clarification while preserving the audit trail."
                ),
                (
                    "Reconcile the canonical Formula v2.0 cases using a retainer-only cash planning bridge "
                    "with zero realized awards. Conservative revenue is five firms at $1,500 monthly for "
                    "twelve months, plus $5,000 of separately scoped support: $95,000 revenue less $64,600 "
                    "costs equals $30,400 owner profit and 32% margin. Base revenue is eight firms at "
                    "$4,500 monthly plus $55,500 support: $487,500 less $268,125 equals $219,375 and 45.0%. "
                    "Scaled revenue is ten firms at $6,500 monthly plus $100,000 support: $880,000 less "
                    "$369,600 equals $510,400 and 58%. These illustrative contract mixes reproduce the "
                    "supplied totals; they do not assert an observed customer roster. The first two cases "
                    "use 1 FT + 2 C; Scaled uses 2 FT + 3 C. Costs include contractor delivery, "
                    "research, infrastructure, acquisition, insurance, and other operating expenses rather "
                    "than merely cloud invoices. Recognize support revenue as services are delivered under "
                    "the applicable contract treatment. Client recoveries, healthcare payments, shipment values, "
                    "and government loss estimates are not operator revenue. Only a lawfully entitled, "
                    "realized net award share belongs in the award ledger; principal-versus-agent assessment "
                    "under ASC 606 prevents presenting another party's gross recovery as the operator's sales. "
                    "A service contract cannot manufacture statutory whistleblower eligibility."
                ),
                (
                    "Stress-test the award pipeline independently of that operating bridge. In an illustrative "
                    "cohort of one hundred leads, remove thirty after public-disclosure analysis and twenty "
                    "more for unresolved particularity defects, leaving fifty counsel-selected matters. Assume "
                    "80% non-intervention, leaving forty such matters and ten interventions. Apply a 25% "
                    "government-dismissal sensitivity to the forty, leaving thirty; assume recovery in 20% "
                    "of those thirty and 60% of the ten interventions. Only twelve original leads recover; "
                    "eighty-eight produce zero recovery. These are deliberately hypothetical sensitivity inputs, "
                    "not measured DOJ non-intervention or Granston dismissal rates. The historical Granston "
                    "memorandum concerns government dismissal practice; operative authority is 31 U.S.C. "
                    "§ 3730(c)(2)(A), subject to governing procedure and case law. Counsel should replace "
                    "assumptions with dated, relevant evidence without conflating non-intervention with dismissal. "
                    "FCA shares generally range from 15%–25% with intervention and 25%–30% without, subject "
                    "to statutory qualifications. SEC and CFTC awards generally use 10%–30% ranges subject "
                    "to qualifying conditions, while IRS section 7623(b) generally uses 15%–30% with its "
                    "own thresholds and reductions. Thus one universal 15%–30% multiplier is wrong. Even "
                    "eligible awards remain zero in spendable cash until collection; test the entire year "
                    "with no awards and delayed retainer receipts before hiring."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Revenue Bridge and Recovery-Risk Separation",
                "headers": [
                    "Case or control with operating boundary",
                    "Revenue construction or factual decision basis",
                    "Cost and profit or recovery treatment",
                    "Staffing requirement or cash protection rule",
                ],
                "rows": [
                    [
                        "Conservative annual service case excludes contingent receipts",
                        "Five monthly retainers produce $90,000 plus $5,000 support",
                        "$95,000 less $64,600 yields $30,400 at 32%",
                        "One full-time owner and two contractors deliver",
                    ],
                    [
                        "Base annual service case excludes contingent receipts",
                        "Eight monthly retainers produce $432,000 plus $55,500 support",
                        "$487,500 less $268,125 yields $219,375 at 45.0%",
                        "One full-time owner and two contractors deliver",
                    ],
                    [
                        "Scaled annual service case excludes contingent receipts",
                        "Ten monthly retainers produce $780,000 plus $100,000 support",
                        "$880,000 less $369,600 yields $510,400 at 58%",
                        "Two full-time staff and three contractors deliver",
                    ],
                    [
                        "Award ledger records only legally entitled receipts",
                        "Counsel documents eligibility allocation and collection status",
                        "Recognize applicable net share rather than gross recovery",
                        "Uncollected awards fund neither payroll nor subscriptions",
                    ],
                    [
                        "Public disclosure review precedes relator case positioning",
                        "Counsel evaluates statutory channels and original-source facts",
                        "Illustrative cohort removes thirty of one hundred",
                        "Continue paid research only within legitimate engagement scope",
                    ],
                    [
                        "Particularity review identifies missing representative claim support",
                        "Counsel evaluates available detail against circuit requirements",
                        "Illustrative cohort removes twenty additional deficient leads",
                        "Suspend filing preparation until essential factual gaps resolve",
                    ],
                    [
                        "Government decisions remain distinct modeled recovery risks",
                        "Hypothetical eighty percent non-intervention leaves forty matters",
                        "Twenty-five percent dismissal sensitivity removes ten matters",
                        "Keep all contingent outcomes outside operating cash coverage",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before a consequential release",
                "body": (
                    "An automated score can open a review task. Only accountable people may "
                    "authorize an allegation-bearing export, filing instruction, or protected disclosure."
                ),
                "items": [
                    "Verify source hashes, entity identities, exact quotation support, and the unresolved-evidence register before releasing any factual dossier.",
                    "Obtain counsel's documented assessment of public-disclosure exposure, Rule 9(b) gaps, program eligibility, and the proper filing channel.",
                    "Match each recipient and export to the engagement, current sealing order, confidentiality instructions, and approved processing environment.",
                    "Confirm the engagement remains solvent with zero award receipts and that no external message exposes protected matter details or promises recovery.",
                ],
            },
        },
        {
            "heading": "4. Compound safe distribution and measure automation net of rework",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Play nine is programmatic methods publishing, not automated accusation publishing. Produce "
                    "pages explaining dataset coverage, reporting lags, suppression, entity resolution, and "
                    "reproducible validation techniques using synthetic examples or carefully selected public "
                    "material cleared for reuse. Python can generate static pages, sitemaps, and structured "
                    "download manifests; a reviewer approves every new template and checks sampled outputs "
                    "for accidental identifiers. Play ten is permission-aware counsel outbound: build a small "
                    "list from public professional directories, score practice fit, and draft individualized "
                    "capability messages without attaching case allegations. Apply 15 U.S.C. § 7704 requirements "
                    "where applicable, including accurate headers, required sender information, a functioning "
                    "opt-out, and timely suppression. Do not scrape restricted directories or evade sending "
                    "limits. Play eleven is the counsel referral and reusable-tool loop: a useful source-coverage "
                    "worksheet travels between practitioners and links back to a booking page, without "
                    "exporting client matters. Price the distribution experiment at $240 monthly tools plus "
                    "six human hours at $60, or $600 total. If one paying engagement results, acquisition "
                    "cost is $600 before additional sales work; if none results, record the full loss "
                    "and change the audience or offer rather than inflating lead quality with automated volume."
                ),
                (
                    "Measure the 70%+ target against a frozen repetitive-work baseline, not against all "
                    "professional judgment. In one illustrative forty-candidate batch, manual collection takes "
                    "300 minutes, normalization 180, initial qualification 160, packet drafting 220, and "
                    "routing preparation 140: 1,000 minutes total. Automation removes 250, 160, 110, 180, "
                    "and 40 minutes respectively, totaling 740 minutes or 74%. The remaining 260 minutes "
                    "include verification, exceptions, and recipient checks; at $60 per hour they cost "
                    "$260, plus $12 machine expense, or $272 per batch. That is $6.80 per candidate "
                    "and $68 per accepted packet if four qualify. The timed scope excludes attorney "
                    "pleading work, specialist interviews, and bespoke investigations, which require separate "
                    "pricing. Counsel-fit software assists rather than replacing the attorney's statutory "
                    "analysis. At one hundred, one hundred fifty, and two hundred annual batches, direct "
                    "batch expense is $27,200, $40,800, and $54,400 respectively, already included within "
                    "the scenario cost envelopes. These volumes are capacity illustrations, not additional "
                    "revenue assumptions. Require two successive measured cycles above 70% after corrections; "
                    "if identity errors or packet rework consume saved time, report the lower achieved "
                    "rate and restrict automation to the transformations that remain reliable."
                ),
                (
                    "Close the flywheel with quality signals that cannot leak case strategy. Store channel "
                    "source, broad practice category, booked consultation, signed retainer, renewal, and "
                    "reviewer rework minutes in the commercial CRM; keep allegation text and evidence "
                    "inside the protected matter workspace. A client-approved, nonidentifying methods improvement "
                    "can become a worksheet update, which attracts another counsel conversation and supplies "
                    "better qualification questions. Never describe a live sealed matter as a success story "
                    "or circulate a supposedly anonymous pattern that identifies the parties. Define operational "
                    "service objectives for data freshness, replay completion, citation validity, and access "
                    "revocation. Test restoration using synthetic dossiers, rotate webhook secrets, and rehearse "
                    "a queue backlog with outbound delivery disabled. When an API, model, or source changes, "
                    "pin the last validated pipeline, route uncertain packets to manual review, and communicate "
                    "revised delivery dates rather than silently degrading accuracy. Startup capital of "
                    "$10,000–$45,000 and monthly opex of $1,500–$9,500 are planning ranges, not substitutes "
                    "for the fully loaded annual scorecard costs; delivery intensity and contractor expense "
                    "can make those totals much larger. With first deals potentially four to twelve months "
                    "away, size runway from actual cash commitments. Scale reviewers before increasing "
                    "outreach whenever the exception queue exceeds contracted turnaround capacity."
                ),
            ],
            "table": {
                "caption": "Distribution Flywheels, Measured Automation, and Recovery Fallbacks",
                "headers": [
                    "Loop or workload with defined scope",
                    "Specific production math and measurement basis",
                    "Human responsibility before consequential external use",
                    "Recovery action when economics or quality fails",
                ],
                "rows": [
                    [
                        "Play nine publishes reusable public methods pages",
                        "Measure consultations per approved worksheet download cohort",
                        "Reviewer checks examples for identifiable protected facts",
                        "Remove affected pages and investigate disclosure scope",
                    ],
                    [
                        "Play ten develops targeted counsel capability outreach",
                        "Monthly tools cost $240 before six review hours",
                        "Owner approves recipients messaging and suppression handling",
                        "Pause sending when objections or delivery failures rise",
                    ],
                    [
                        "Play eleven encourages practitioner sharing of worksheets",
                        "Six review hours at $60 add $360",
                        "Counsel clears any client-derived material before reuse",
                        "Replace sensitive examples with independently created synthetic records",
                    ],
                    [
                        "Repetitive research baseline contains one thousand minutes",
                        "Automated transformations remove seven hundred forty minutes",
                        "Reviewers retain two hundred sixty accountable minutes",
                        "Recalculate achieved savings after errors and rework",
                    ],
                    [
                        "Forty candidate batch carries fully loaded expense",
                        "$260 human expense plus $12 machine equals $272",
                        "Owner validates contractor rates and actual run invoices",
                        "Use undiscounted costs when startup benefits expire",
                    ],
                    [
                        "Four accepted packets allocate the complete batch",
                        "$272 divided by four yields $68 each",
                        "Reviewer rejects weak packets despite sunk processing costs",
                        "Record zero acceptance without manufacturing substitute evidence",
                    ],
                    [
                        "Annual capacity examples remain inside canonical costs",
                        "One hundred fifty batches consume $40,800 directly",
                        "Owner reconciles remaining expenses against Base cost envelope",
                        "Limit acquisition when delivery queues exceed safe capacity",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the search for evidence, never the decision that an allegation is ready to travel.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create an immutable source manifest for CMS, Open Payments, SAM.gov, and authorized manifest inputs, then test schema quarantine and replay.",
        "Implement all eleven mapped operating plays with named owners, undiscounted unit costs, permitted inputs, and documented failure fallbacks.",
        "Benchmark a forty-candidate batch against the 1,000-minute baseline and count reviewer corrections before reporting automation above 70%.",
        "Require source-bound quotations, public-disclosure analysis, Rule 9(b) gap review, and counsel-authorized recipients before dossier release.",
        "Reconcile $95,000, $487,500, and $880,000 annual revenue cases to their exact costs and profits while holding uncollected awards at zero cash.",
        "Launch one cleared methods worksheet, a narrowly targeted counsel outreach cohort, and a referral loop that excludes protected matter details.",
    ],
    "statutory_citations": [
        {
            "title": "31 U.S.C. § 3730(b)(2) — Qui tam filing, government disclosure, and seal",
            "url": "https://www.law.cornell.edu/uscode/text/31/3730",
            "relevance": "Licensed relator counsel controls complaint filing, government service, supporting disclosure, and compliance with the initial seal and subsequent orders.",
        },
        {
            "title": "31 U.S.C. § 3730(e)(4) — Public-disclosure bar and original-source definition",
            "url": "https://www.law.cornell.edu/uscode/text/31/3730",
            "relevance": "Counsel evaluates statutory disclosure channels, substantially similar allegations, original-source facts, and government opposition before advancing a public-data lead.",
        },
        {
            "title": "Federal Rule of Civil Procedure 9(b) — Particularity for fraud or mistake",
            "url": "https://www.law.cornell.edu/rules/frcp/rule_9",
            "relevance": "The evidence worksheet identifies claim particulars and factual gaps without assuming that aggregate statistical anomalies satisfy pleading requirements.",
        },
        {
            "title": "31 U.S.C. § 3730(c)(2)(A) and (d) — Dismissal authority and relator awards",
            "url": "https://www.law.cornell.edu/uscode/text/31/3730",
            "relevance": "Model government dismissal separately from non-intervention and apply the relevant award range, qualifications, and reductions rather than a universal multiplier.",
        },
        {
            "title": "5 U.S.C. § 552 — Freedom of Information Act",
            "url": "https://www.law.cornell.edu/uscode/text/5/552",
            "relevance": "Track requests, determinations, fees, exemptions, productions, and appeals without assuming that statutory determination periods promise immediate record delivery.",
        },
        {
            "title": "15 U.S.C. § 78u-6 and 17 CFR § 240.21F-9 — SEC whistleblower awards and submission procedures",
            "url": "https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.21F-9",
            "relevance": "Counsel applies SEC submission procedures and award eligibility, including the statutory framework's qualifying enforcement threshold and general 10%–30% award range.",
        },
        {
            "title": "26 U.S.C. § 7623(b) — IRS whistleblower awards",
            "url": "https://www.law.cornell.edu/uscode/text/26/7623",
            "relevance": "Counsel evaluates the general 15%–30% range, reductions, proceeds exceeding $2 million, and the individual-taxpayer gross-income condition exceeding $200,000 in a relevant year.",
        },
        {
            "title": "7 U.S.C. § 26 — CFTC whistleblower incentives and protection",
            "url": "https://www.law.cornell.edu/uscode/text/7/26",
            "relevance": "Keep CFTC eligibility and its general 10%–30% award framework separate from FCA and IRS assumptions.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Apply accurate routing information, applicable identification and address requirements, functional opt-out mechanisms, and timely suppression to commercial counsel outreach.",
        },
        {
            "title": "State Farm Fire & Casualty Co. v. United States ex rel. Rigsby, 580 U.S. 26 (2016)",
            "url": "https://www.supremecourt.gov/opinions/16pdf/15-513_43j7.pdf",
            "relevance": "The Supreme Court held that an FCA seal violation does not require automatic dismissal, while leaving serious consequences and case-specific judicial assessment.",
        },
        {
            "title": "United States ex rel. Polansky v. Executive Health Resources, Inc., 599 U.S. 419 (2023)",
            "url": "https://www.supremecourt.gov/opinions/22pdf/21-1052_fd9g.pdf",
            "relevance": "Government dismissal after intervention, including later intervention, must be assessed under the governing procedural framework rather than treated as identical to initial non-intervention.",
        },
    ],
}
