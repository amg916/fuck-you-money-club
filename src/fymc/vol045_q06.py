from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-and-first-idr-recovery-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in no surprises act (idr) medical arbitration & out-of-network recovery, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (1–4 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "Mine NPPES, CMS Dispute Reports and Practice Transitions; Qualify ERISA Jurisdiction; Convert Protected Remittance Audits into Cash-Based Recovery Mandates",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #45, No Surprises Act (IDR) Medical Arbitration & Out-of-Network Recovery, "
        "holds Rank #09 of 49 and a 94/100 Money-to-Manpower Score. This chapter maps 12 "
        "sourcing plays into one disciplined acquisition system: identify exposed physician groups, "
        "verify timely eligible claims, demonstrate recoverable economics, and secure narrow paid "
        "mandates. Public records establish account-level intent; authorized remittance audits "
        "establish actual opportunity. The first 3–10 wins mean signed, operationally accepted "
        "mandates within 1–4 months, not promised arbitration collections. Canonical annual owner "
        "profit is $33,000 Conservative, $217,150 Base, and $504,000 Scaled. Revenue consists "
        "only of earned contingency shares on incremental cash after specified deductions. "
        "Deadline discipline, jurisdiction screening, and payer cash reconciliation protect the "
        "spread better than indiscriminate filing volume."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned contingency revenue; excludes baseline provider collections",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned contingency revenue; excludes baseline provider collections",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned contingency revenue; excludes baseline provider collections",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Mine account-level intent without confusing public signals with eligible claims",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with independent emergency medicine, anesthesiology, radiology, pathology, "
                    "and neonatology groups serving facilities where federal surprise-billing protections "
                    "may apply. Build an account universe from the CMS National Plan and Provider "
                    "Enumeration System downloadable files and NPI Registry API, then resolve organization "
                    "names against practice websites and state business registries. An NPI taxonomy identifies "
                    "a prospect category; it does not establish network status, coverage, standing, or a "
                    "recoverable dispute. Store organization NPI, specialty, operating states, facility "
                    "relationships, public business contact, source URL, and retrieval date. Treat the billing "
                    "manager, revenue-cycle director, and practice administrator as separate buying roles "
                    "rather than buying three copies of the same lead. Use CMS federal IDR public-use "
                    "reports to prioritize broad service and payer patterns, never to infer a specific "
                    "practice's unpaid award. A public hiring notice for an arbitration analyst, a new "
                    "facility staffing contract, or a billing-vendor transition is a stronger conversation "
                    "trigger than generic specialty membership. Screen each trigger manually before outreach. "
                    "A practice that recently moved entirely in-network can look attractive in stale directories "
                    "while having almost no new federal IDR inventory. Refresh high-priority accounts monthly "
                    "and preserve historical source snapshots."
                ),
                (
                    "Implement public_record_api_intelligence as a modest, auditable collection pipeline, not "
                    "an indiscriminate scrape. A scheduled Python urllib job can fetch permitted official "
                    "feeds, while sqlite3 retains source hashes, timestamps, and deduplication keys. Use "
                    "county civil dockets for public practice ownership disputes or billing-vendor litigation "
                    "that indicates operational change; use probate registries only when a publicly documented "
                    "practice succession creates a legitimate business contact. Unclaimed property ledgers "
                    "can reveal a provider entity's stale payment address, but those assets are a separate "
                    "recovery category and must never enter the IDR revenue forecast. Do not extract patient "
                    "details from court exhibits or assume that public accessibility authorizes unrestricted "
                    "reuse. A practical research budget is 100 accounts at 12 minutes each, or 20 hours; "
                    "at an illustrative $40 hourly research cost, account discovery costs $800 before "
                    "outreach. If access restrictions, unstable interfaces, or missing coverage undermine "
                    "an API, switch to scheduled bulk FOIA/public-record exports, official data feeds, and "
                    "low-frequency cached queues. Respect access terms and request only business-level "
                    "fields. The fallback preserves research continuity, not filing timeliness: statutory "
                    "clocks must come from authorized claim records, never delayed public-record responses."
                ),
                (
                    "The twelve plays below are a chapter-local sourcing map; only "
                    "public_record_api_intelligence is a supplied cross-series identifier. Combine them "
                    "into three queues: immediately contactable practice triggers, partner-introduced accounts, "
                    "and inbound education requests. Every queue feeds the same qualification process. "
                    "An HFMA chapter presentation can generate permission-based introductions, while an "
                    "RBMA educational session may surface radiology groups with fragmented remittance "
                    "workflows. A billing company is valuable because it can introduce several authorized "
                    "clients, not because it can disclose every client's records. Require each provider's "
                    "authorization and the appropriate HIPAA arrangements before receiving protected "
                    "information. Do not offer percentage referral payments to clinicians or billing vendors "
                    "without evaluating the actual federal and state restrictions; unpaid introductions "
                    "avoid making referral compensation the acquisition thesis. At an illustrative 20 "
                    "accounts per weekly research batch, four batches produce 80 distinct accounts, not "
                    "80 qualified mandates. Deduplicate across partner lists and events using organization "
                    "identity rather than contact email. Measure qualified meetings per source and subsequent "
                    "cash contribution per cohort. Retire a channel after two completed test cohorts if "
                    "it produces meetings but no timely, eligible, economically workable inventory."
                ),
            ],
            "table": {
                "caption": "Twelve Mapped Sourcing Plays with Evidence, Unit Tests and Fallbacks",
                "headers": [
                    "Mapped sourcing play and intended buyer",
                    "Observable trigger and evidence to retain",
                    "Illustrative unit test before expanding spend",
                    "Failure mode and concrete fallback action",
                ],
                "rows": [
                    [
                        "public_record_api_intelligence targets physician groups experiencing documented operating changes",
                        "Retain official docket identifiers and business registry source dates",
                        "Research 100 accounts for $800 before outreach expense",
                        "Replace unstable interfaces with scheduled exports and cached queues",
                    ],
                    [
                        "NPPES specialty clustering identifies independent facility-based physician organizations",
                        "Match organization taxonomy against current practice and facility websites",
                        "Review 200 records to retain 80 verified organizations",
                        "Discard stale directory matches after direct organization verification",
                    ],
                    [
                        "CMS dispute-pattern mining prioritizes service categories for account research",
                        "Retain report period and distinguish disputes from unique providers",
                        "Test two specialty cohorts with 25 accounts apiece",
                        "Use aggregate patterns only when provider attribution remains unavailable",
                    ],
                    [
                        "Practice-transition monitoring reaches administrators during billing-system or ownership changes",
                        "Archive public staffing announcements and named business transition dates",
                        "Contact ten verified transitions before purchasing additional monitoring",
                        "Stop outreach when transition leaves no eligible recent inventory",
                    ],
                    [
                        "RCM employment-trigger monitoring identifies groups expanding recovery operations",
                        "Capture current job advertisements mentioning arbitration or payer disputes",
                        "Test fifteen hiring triggers against fifteen ordinary specialty leads",
                        "Offer overflow capacity when internal hiring reduces outsourcing demand",
                    ],
                    [
                        "Billing-vendor introductions reach existing clients through authorized relationship owners",
                        "Obtain provider-approved introductions without transferring protected claim records",
                        "Ask three vendors for two appropriate introductions each",
                        "Use unpaid introductions when proposed referral compensation requires review",
                    ],
                    [
                        "Healthcare counsel introductions surface unresolved payer payment process problems",
                        "Request business introductions without privileged documents or patient details",
                        "Hold five counsel meetings seeking two relevant practice introductions",
                        "Keep counsel independent and separate representation from recovery operations",
                    ],
                    [
                        "Specialty-association teaching attracts administrators seeking deadline-control workflow improvements",
                        "Use opt-in registrations tied to a practical deadline worksheet",
                        "Invite thirty administrators and seek five requested follow-up meetings",
                        "Replace broad webinars with smaller specialty-specific working sessions",
                    ],
                    [
                        "Facility staffing-contract monitoring detects newly responsible physician billing groups",
                        "Verify announced contract dates and the actual billing organization",
                        "Research ten contract changes before opening individual account campaigns",
                        "Reject facility announcements that identify no relevant provider counterparty",
                    ],
                    [
                        "Secure remittance micro-audits convert permission into evidence-based recovery mandates",
                        "Receive authorized 835 files through contracted protected transfer systems",
                        "Inspect twenty recent lines before expanding the review scope",
                        "Stop immediately when deadlines or jurisdiction eliminate workable inventory",
                    ],
                    [
                        "Deadline-calculator inbound captures administrators researching federal dispute timing mechanics",
                        "Collect business contacts without patient identifiers or uploaded remittances",
                        "Measure qualified meetings from the first hundred relevant visits",
                        "Replace calculator conclusions with human verification of source dates",
                    ],
                    [
                        "Existing-client introductions extend trusted operating results to peer practices",
                        "Request introductions only after verified service and cash reconciliation",
                        "Ask five satisfied clients for one relevant introduction each",
                        "Use process references without disclosing another provider's protected records",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Find the operational leak before pitching arbitration volume",
                "body": (
                    "Experienced operators prospect for recoverable workflow failures and documented "
                    "business changes, not merely large out-of-network balances."
                ),
                "items": [
                    "Ask who reconciles initial payment receipt dates; an unowned date field often explains missed initiation windows.",
                    "Compare organization NPI and contracting entity before merging accounts; one staffing brand can contain several distinct billing groups.",
                    "Use public IDR reports to select a specialty conversation, then require authorized claim evidence before estimating recoveries.",
                    "Keep a separate ledger for unclaimed property and ordinary receivables leads so unrelated assets never inflate the federal IDR pipeline.",
                ],
            },
        },
        {
            "heading": "2. Score eligibility, deadline runway and collectible contribution before accepting inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Qualification begins with a protected evidence package, not a spreadsheet of billed "
                    "charges. Execute the service agreement, HIPAA Business Associate Agreement, and access "
                    "instructions before handling protected health information; extend appropriate obligations "
                    "to subcontractors. Request a limited recent sample containing the 835 remittance, "
                    "underlying claim, service date, initial payment or denial receipt evidence, provider "
                    "and facility identifiers, plan information, and prior negotiation correspondence. "
                    "An 835 CARC/RARC classifier can identify adjustment patterns, but cannot conclusively "
                    "determine federal jurisdiction or plan funding. A commercial payer logo does not "
                    "distinguish its insured products from self-funded administrative-services business. "
                    "Confirm coverage, applicable state law, service setting, network relationships, and "
                    "the payment-determination method before calculating an opportunity. Some self-funded "
                    "plans can opt into specified state arrangements; some services follow an applicable "
                    "All-Payer Model Agreement. Exclude Medicare and Medicaid inventory from this commercial "
                    "federal IDR sourcing model and route ordinary contractual disputes elsewhere. The "
                    "federal mechanism is not a universal underpayment remedy. Record the basis for each "
                    "eligibility decision and its reviewer. If a missing document could change the "
                    "jurisdictional result, put the claim in a document-request queue rather than purchasing "
                    "an arbitration filing on an assumption."
                ),
                (
                    "Build separate states for initial-payment receipt, open-negotiation initiation, negotiation "
                    "completion, IDR initiation, entity selection, submissions, determination, and cash receipt. "
                    "Under the federal framework, the open-negotiation notice generally must be initiated "
                    "within 30 business days after receipt of the initial payment or denial; the negotiation "
                    "period itself then runs for 30 business days. IDR initiation generally occurs during "
                    "the four-business-day period beginning after negotiation ends. The four days are an "
                    "initiation window, not permission to batch unrelated claims. Verify current CMS "
                    "instructions, applicable extensions, litigation effects, and the rule version governing "
                    "the particular dispute before scheduling action. Keep service dates distinct from "
                    "receipt dates and retain proof of notice transmission. The 90-calendar-day restriction "
                    "following a determination requires party and same-or-similar-service tracking, with "
                    "the applicable later initiation window handled explicitly. Do not reduce it to "
                    "a single universal payer/CPT timer. Batching requires its own current-rule eligibility "
                    "check; a shared payer brand alone is insufficient. Assign an accountable human to "
                    "each imminent deadline and an escalation backup. A nightly exception report should "
                    "surface missing receipt evidence, disputed plan classification, expired clocks, and "
                    "cooling-off conflicts before staff prepare an offer."
                ),
                (
                    "Use a 100-point account score only after mandatory eligibility checks pass: verified "
                    "federal inventory earns 25 points, deadline runway 20, evidence completeness 20, "
                    "collectible contribution 20, and administrator access 15. Seventy-five points qualifies "
                    "a practice for a bounded pilot; no score rescues an ineligible claim. Define the "
                    "contractual fee base as incremental cash collected above the actual initial payer "
                    "payment, less non-refundable administrative fees, unrecovered entity fees, and agreed "
                    "casework costs, floored at zero. QPA and initial allowed payment are distinct fields; "
                    "never replace the actual baseline with an assumed QPA payment. Illustratively, "
                    "$20,000 initially collected plus $10,000 subsequently collected creates $10,000 of "
                    "incremental cash. Deduct $1,500 of administrative and unrecovered entity fees and "
                    "$1,000 of casework costs: the distributable recovery is $7,500 and a 30% operator "
                    "share is $2,250. These are aggregate sample costs, not published fee quotes. A "
                    "$12,000 paper uplift with only $10,000 collected still supports only that $2,250 "
                    "fee. Track entity-fee deposits separately: recognize a refund only when supported "
                    "by actual disposition and receipt, and conservatively reserve losing or ineligible "
                    "cases for full forfeiture unless the governing refund process establishes otherwise."
                ),
            ],
            "table": {
                "caption": "Qualification Scorecard and Non-Negotiable Evidence Checks",
                "headers": [
                    "Qualification component and assigned scoring weight",
                    "Evidence required before awarding the available points",
                    "Acceptance standard tied to operational execution",
                    "Failure response that preserves cash and deadlines",
                ],
                "rows": [
                    [
                        "Verified federal inventory contributes twenty-five available account scoring points",
                        "Review plan funding evidence and applicable state payment method",
                        "Document why federal dispute resolution governs the sampled services",
                        "Route state-governed inventory to an appropriate separate recovery workflow",
                    ],
                    [
                        "Deadline runway contributes twenty available account scoring points",
                        "Preserve initial remittance receipt and negotiation notice transmission evidence",
                        "Require sufficient verified runway for documented timely procedural action",
                        "Reject expired claims unless a supported exception actually applies",
                    ],
                    [
                        "Evidence completeness contributes twenty available account scoring points",
                        "Match claim records with remittances and relevant clinical support",
                        "Require retrievable materials supporting eligibility and permissible offer factors",
                        "Request missing records before incurring avoidable dispute filing costs",
                    ],
                    [
                        "Collectible contribution contributes twenty available account scoring points",
                        "Model incremental receipts after administrative fees and casework deductions",
                        "Require positive expected contribution under a delayed collection stress",
                        "Narrow inventory when fees consume the plausible recovery spread",
                    ],
                    [
                        "Administrator access contributes fifteen available account scoring points",
                        "Identify authorized signatory and responsible revenue-cycle operating contact",
                        "Confirm access instructions and a workable weekly exception meeting",
                        "Pause onboarding when nobody owns documents or deadline escalation",
                    ],
                    [
                        "Mandatory eligibility checks override every numerical account scoring result",
                        "Verify protected transfer arrangements and provider representation authority",
                        "Require jurisdiction and timing checks before each filing commitment",
                        "Decline unsupported filings regardless of prospect size or score",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before any paid filing commitment",
                "body": (
                    "A signed mandate authorizes scoped work; it does not establish that every "
                    "submitted claim belongs in federal IDR."
                ),
                "items": [
                    "Verify service eligibility, plan funding, specified state law, and any applicable alternative payment-determination method.",
                    "Reconstruct receipt and notice dates from retained evidence; calculate both negotiation periods and the separate IDR initiation window.",
                    "Validate current batching requirements and any same-party, same-or-similar-service cooling-off restriction before combining disputes.",
                    "Confirm authority, protected data handling, current fees, loss reserves, and positive cash-based economics after every agreed deduction.",
                ],
            },
        },
        {
            "heading": "3. Run a narrow outbound cadence that converts evidence into signed mandates",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Run a five-touch, fifteen-business-day sequence around one documented business trigger. "
                    "On day one, email the practice administrator a short observation and offer a "
                    "twenty-line eligibility-and-deadline review, without requesting patient information by "
                    "email. On day three, place a manual call to the published business number and ask "
                    "who owns out-of-network recovery operations. On day six, send a permission-respecting "
                    "professional-network message with a one-page explanation of the cash-based fee "
                    "waterfall. On day ten, send a useful deadline-control worksheet; on day fifteen, "
                    "close the loop and stop unless they invite further contact. Commercial email must "
                    "use accurate routing and subject information, the required sender identification "
                    "and postal address, a functioning opt-out, and timely suppression under 15 U.S.C. "
                    "§ 7704. Manual business outreach does not justify automated texts or prerecorded "
                    "calls; evaluate the actual channel under 47 U.S.C. § 227 and applicable state "
                    "rules before adding automation. Maintain one suppression list across email and "
                    "partner campaigns. Never claim to represent CMS, a payer, or a certified IDR "
                    "entity. The useful promise is a bounded assessment with documented exclusions, "
                    "not an expected award or a guaranteed collection date."
                ),
                (
                    "Use explicit planning assumptions rather than fabricated industry conversion benchmarks. "
                    "A starter cohort of 300 raw organization records might yield 180 verified eligible-profile "
                    "accounts, a 60% research yield. If 30 engage in a relevant conversation, that is "
                    "16.7% of verified accounts; 15 discovery meetings represent 50% of conversations. "
                    "Eight authorized sample reviews represent 53.3% of meetings, and three accepted "
                    "mandates represent 37.5% of sample reviews, or 1% of raw records. These are "
                    "test targets, not observed performance. Review source quality if the first 60 verified "
                    "accounts produce fewer than six relevant conversations; review qualification or "
                    "positioning if ten meetings produce fewer than two authorized samples. Do not "
                    "compensate for poor conversion by filing marginal claims. If total acquisition "
                    "spend is $4,500 and three mandates sign, acquisition cost is $1,500 per mandate. "
                    "At an illustrative $2,250 earned fee per completed recovery cohort and $750 "
                    "of additional operator delivery overhead, one collected cohort contributes $1,500 "
                    "before acquisition expense, merely recovering that acquisition cost. Require evidence "
                    "of repeat eligible inventory before paying for scale. Ten mandates at the same "
                    "raw conversion would require 1,000 records and enough delivery capacity to "
                    "service them without missing deadlines."
                ),
                (
                    "The discovery call should establish authority, inventory, process failure, and economics "
                    "in that order. Ask who can authorize representation, how many recent potentially "
                    "covered claims exist, which person owns receipt-date evidence, and whether another "
                    "vendor already controls the same disputes. When the administrator says their billing "
                    "company handles appeals, distinguish contractual appeals from timely federal open "
                    "negotiation and IDR, then request a scoped coordination discussion rather than "
                    "attacking the incumbent. When they cite a high published prevailing-offer percentage, "
                    "explain that selection outcomes are not cash realization rates and request actual "
                    "remittance history. When they demand a recovery guarantee, offer a fixed sample "
                    "scope, documented eligibility findings, and cash-contingent compensation instead. "
                    "When they resist data access, begin with aggregate counts and move to a minimum "
                    "necessary protected sample only after contracting. The pilot mandate should identify "
                    "the authorized provider entities, service-date range, payer scope, fee waterfall, "
                    "expense funding, dispute authority, termination treatment, and reconciliation process. "
                    "Require affirmative instructions about settlement authority; a contingency agreement "
                    "alone should not imply unlimited discretion. Send the diagnostic findings within "
                    "five business days of receiving complete records, while escalating any nearer "
                    "statutory deadline immediately rather than waiting for the scheduled presentation."
                ),
            ],
            "table": {
                "caption": "Outreach Cadence, Conversion Controls and Concrete Objection Responses",
                "headers": [
                    "Touchpoint or objection requiring a precise response",
                    "Operator language grounded in an observable business issue",
                    "Requested next action and evidence of conversion",
                    "Stop condition or practical fallback for the prospect",
                ],
                "rows": [
                    [
                        "Day one email follows a verified practice operating trigger",
                        "Your staffing expansion may warrant checking recent recovery deadlines",
                        "Request a short administrator discussion without exchanging patient records",
                        "Suppress immediately when the recipient declines further commercial contact",
                    ],
                    [
                        "Day three manual call identifies the actual workflow owner",
                        "Who maintains initial payment receipt evidence for disputed services",
                        "Record the responsible person's business role and requested follow-up",
                        "Leave one concise message rather than repeatedly interrupting staff",
                    ],
                    [
                        "Day six professional message explains the incremental cash waterfall",
                        "Our fee excludes your baseline collections and unrecovered expenses",
                        "Offer a protected sample review after authority is established",
                        "Provide aggregate workflow education when protected access remains premature",
                    ],
                    [
                        "Day ten worksheet answers the incumbent billing vendor objection",
                        "We can inspect deadlines without replacing your existing billing team",
                        "Request a coordinated meeting with the authorized billing relationship owner",
                        "Decline duplicate representation when dispute ownership cannot be resolved",
                    ],
                    [
                        "Published success statistics trigger a cash realization evidence discussion",
                        "Selected offers and collected dollars measure different operating outcomes",
                        "Request anonymized aggregate collection timing before estimating acquisition economics",
                        "Use conservative cash assumptions when collection history lacks support",
                    ],
                    [
                        "Day fifteen closeout addresses delay without manufacturing artificial urgency",
                        "We will pause outreach unless a scoped review becomes useful",
                        "Record explicit permission before scheduling any later commercial follow-up",
                        "Retain suppression preferences and remove unnecessary prospect information promptly",
                    ],
                ],
            },
        },
        {
            "heading": "4. Land three mandates, prove the cash waterfall and scale only repeatable cohorts",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Sequence the first four months around evidence delivery, not a premature filing target. "
                    "During weeks one and two, configure the CRM, source register, suppression list, secure "
                    "transfer environment, service agreement, and Business Associate Agreement. During weeks "
                    "three and four, complete the first account cohort, run discovery calls, and accept "
                    "only samples with adequate procedural runway. During weeks five through eight, "
                    "deliver diagnostics, sign the first three bounded mandates, and initiate authorized "
                    "negotiations on eligible inventory. During weeks nine through sixteen, expand toward "
                    "ten mandates only if staffing and deadline coverage remain adequate. Count a sourcing "
                    "win when the provider signs and the operating team accepts a viable scoped inventory; "
                    "count a collected recovery separately. Fresh negotiations and subsequent arbitration "
                    "can push cash beyond the acquisition window. Maintain distinct dashboard columns "
                    "for signed mandates, accepted claims, negotiations initiated, disputes initiated, "
                    "determinations, incremental collections, and earned fees. Existing disputes inherited "
                    "from another vendor require explicit authority and procedural verification before "
                    "any handoff. Never advertise a first-month collection timetable simply because one "
                    "prospect has an old unpaid award. The acquisition plan must survive a slower cash "
                    "cycle than the sales cycle."
                ),
                (
                    "Turn the diagnostic into a concise operating exhibit: eligible inventory, rejected "
                    "inventory with reasons, next procedural dates, permitted evidence gaps, projected "
                    "expenses, and a cash-waterfall example. Separate QPA-related information from prohibited "
                    "pricing evidence. FAIR Health products may assist internal research where permitted, "
                    "but a usual-and-customary charge benchmark must not be repackaged as permissible "
                    "federal IDR valuation evidence. The federal framework excludes usual and customary "
                    "charges, billed charges, and public payer reimbursement rates as determination factors. "
                    "Use documented patient acuity, provider training and experience, facility characteristics, "
                    "market share where relevant, and other permitted credible information without counting "
                    "a factor twice through QPA and supplemental evidence. Assign submission drafting "
                    "and eligibility review to different people when possible. After determination, "
                    "track the statutory payment timetable, payment exceptions, and actual bank or "
                    "remittance evidence; unpaid awards remain receivables rather than collected contingency "
                    "revenue. Escalate delayed payment through the appropriate payer and CMS processes "
                    "using retained records. Never transfer a protected patient balance to the patient "
                    "to finance the dispute. Keep administrative fees, entity deposits, returned deposits, "
                    "casework costs, baseline receipts, and incremental receipts in separate ledger fields "
                    "so a provider can reproduce every invoice."
                ),
                (
                    "Reconcile scale to the canonical scorecard, not to physician collections. Conservative "
                    "annual operator revenue is $110,000, with $77,000 of operator expenses and $33,000 "
                    "owner profit at 30% margin using one full-time worker and two contractors. Base "
                    "revenue is $505,000, expenses $287,850, and owner profit $217,150 at 43.0%, with "
                    "the same team structure. Scaled revenue is $900,000, expenses $396,000, and owner "
                    "profit $504,000 at 56%, using two full-time workers and three contractors. An "
                    "illustrative $2,500 average earned fee requires 44, 202, and 360 collected recovery "
                    "cohorts annually, respectively; cohort size is a modeling unit, not an authorized "
                    "batching rule. Provider cash, paper awards, and refunded deposits are not substitutes "
                    "for those fee totals. Costs already reimbursed or deducted in determining the "
                    "contingency base must not be charged again as unreimbursed operator expenses. "
                    "Use separate settlement and operator ledgers to prevent that duplication. Before "
                    "hiring or buying another lead list, stress collection timing by an additional "
                    "60 days, reduce expected cash realization, and include losing or ineligible-case "
                    "fee exposure. Pause expansion if the resulting working-capital requirement exceeds "
                    "funded reserves, even when the mandate pipeline looks strong. High margin comes "
                    "from disciplined selection and repeatable execution, not from celebrating uncollected awards."
                ),
            ],
            "table": {
                "caption": "First-Deal Operating Milestones and Canonical Annual Reconciliation",
                "headers": [
                    "Milestone or canonical annual operating scenario",
                    "Evidence and volume required to substantiate progress",
                    "Cash or expense treatment used in reporting",
                    "Capacity decision and corresponding risk containment action",
                ],
                "rows": [
                    [
                        "Weeks one through four establish the protected acquisition foundation",
                        "Complete account research and identify responsible provider operating contacts",
                        "Track research and outreach spend before expecting earned fees",
                        "Limit samples to records the team can review promptly",
                    ],
                    [
                        "Weeks five through eight target three accepted provider mandates",
                        "Require signed authority and a documented viable claim inventory",
                        "Separate signed mandates from actual incremental cash collection events",
                        "Assign deadline ownership before initiating any authorized dispute action",
                    ],
                    [
                        "Weeks nine through sixteen permit expansion toward ten mandates",
                        "Verify adequate staffing and repeatable evidence retrieval across accounts",
                        "Maintain funded reserves while awards and payer receipts diverge",
                        "Pause new intake when deadline exceptions exceed available coverage",
                    ],
                    [
                        "Conservative scenario uses one full-time worker and two contractors",
                        "$110,000 earned fees equal 44 illustrative $2,500 collected cohorts",
                        "$77,000 expenses leave $33,000 owner profit at 30% margin",
                        "Protect cash by selecting timely eligible inventory before expansion",
                    ],
                    [
                        "Base scenario retains one full-time worker and two contractors",
                        "$505,000 earned fees equal 202 illustrative $2,500 collected cohorts",
                        "$287,850 expenses leave $217,150 owner profit at 43.0% margin",
                        "Automate exception detection while preserving individual human deadline accountability",
                    ],
                    [
                        "Scaled scenario uses two full-time workers and three contractors",
                        "$900,000 earned fees equal 360 illustrative $2,500 collected cohorts",
                        "$396,000 expenses leave $504,000 owner profit at 56% margin",
                        "Add delivery capacity before accepting additional deadline-sensitive provider inventories",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build one evidence-backed account cohort",
                    "action": "Resolve 100 specialty practice accounts from official sources and documented operating triggers.",
                    "detail": (
                        "Deduplicate provider organizations, retain source dates, identify business contacts, "
                        "and exclude patient information from the prospecting database."
                    ),
                },
                {
                    "step": 2,
                    "title": "Qualify a protected twenty-line sample",
                    "action": "Secure authority and HIPAA arrangements before reviewing claim-level records.",
                    "detail": (
                        "Verify jurisdiction, receipt dates, negotiation status, batching constraints, "
                        "permitted evidence, and the incremental cash waterfall for each sampled line."
                    ),
                },
                {
                    "step": 3,
                    "title": "Convert diagnostics into three bounded mandates",
                    "action": "Present exclusions, deadlines, expense funding, fee mechanics, and explicit settlement authority.",
                    "detail": (
                        "Count a mandate only after signature and operational acceptance; coordinate with "
                        "existing vendors and avoid duplicate representation of the same disputes."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile collections before increasing acquisition spend",
                    "action": "Match payer remittances and deposits to baseline receipts, incremental receipts, expenses, and earned fees.",
                    "detail": (
                        "Compare acquisition cost and delivery contribution by source cohort, stress "
                        "a 60-day collection delay, and expand only within funded capacity."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "The best IDR lead is a timely, eligible claim with a documented cash path, not the largest unpaid balance.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Build a deduplicated 100-account specialty cohort using NPPES, verified practice websites, and dated public operating triggers.",
        "Configure the five-touch cadence, shared suppression list, source attribution, and explicit raw-record-to-mandate conversion targets.",
        "Execute provider authority and HIPAA Business Associate Agreements before accepting protected remittance samples.",
        "Score each account only after jurisdiction, receipt evidence, negotiation timing, batching, and cooling-off checks pass.",
        "Sign three bounded mandates with explicit expense funding, settlement authority, and fees based on net incremental cash collected.",
        "Reconcile every collection and fee refund, compare source-level acquisition contribution, and stress cash timing before pursuing ten mandates.",
    ],
    "statutory_citations": [
        {
            "title": "42 U.S.C. § 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes federal surprise-billing protections and the negotiation and IDR framework, "
                "including relevant determination factors, excluded factors, and payment requirements."
            ),
        },
        {
            "title": "45 CFR § 149.510 — Federal independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.510",
            "relevance": (
                "Governs open negotiation, IDR initiation, batching, subsequent disputes, fees, and "
                "determinations; apply operative requirements alongside controlling judicial decisions "
                "and current agency instructions."
            ),
        },
        {
            "title": "45 CFR § 149.30 — Definitions",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-A/section-149.30",
            "relevance": (
                "Defines concepts including the out-of-network rate and specified state law, supporting "
                "claim-specific screening before selecting the federal process."
            ),
        },
        {
            "title": "45 CFR § 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Supports required contractual controls for protected information handled by recovery "
                "operators and their business-associate subcontractors."
            ),
        },
        {
            "title": "45 CFR § 164.502(b) — Minimum necessary standard",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502",
            "relevance": (
                "Supports limiting protected claim samples and access to the information reasonably "
                "necessary for the authorized recovery function, subject to applicable exceptions."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Governs commercial email routing, subject accuracy, required disclosures, opt-out "
                "mechanisms, and suppression practices in prospecting campaigns."
            ),
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Requires channel-specific review before introducing automated calls, prerecorded "
                "messages, or texts into the business acquisition sequence."
            ),
        },
        {
            "title": "42 U.S.C. § 1320a-7b(b) — Illegal remunerations",
            "url": "https://www.law.cornell.edu/uscode/text/42/1320a-7b",
            "relevance": (
                "Requires evaluating referral remuneration where federal healthcare program business "
                "is implicated; it does not make every ordinary business introduction prohibited."
            ),
        },
        {
            "title": "29 U.S.C. § 1144 — ERISA preemption and state-law interaction",
            "url": "https://www.law.cornell.edu/uscode/text/29/1144",
            "relevance": (
                "Explains why plan funding and applicable state insurance rules require substantive "
                "review rather than classification from a payer brand or adjustment code alone."
            ),
        },
    ],
}
