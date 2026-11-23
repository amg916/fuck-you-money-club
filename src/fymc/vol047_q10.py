from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 3 C (4 people) ai data-center powered land, substation headroom & bess site optioning team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Evidence Pipelines, Utility-Validated MW, Assignable Land Options, and Private-Branded Trigger Mail",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #47, ranked #15 of 49 with a 92/100 Money-to-Manpower Score, "
        "turns 11 mapped plays into an evidence-first origination machine. A single "
        "full-time principal and three contractors automate source collection, parcel "
        "screening, document assembly, and buyer routing while retaining human decisions "
        "on utility capacity, zoning, title, and assignment terms. Python workers and "
        "authenticated webhooks move facts; language models extract cited statements, "
        "never invent deliverable megawatts. The canonical annual owner profits remain "
        "$33,000 Conservative, $212,100 Base, and $486,000 Scaled. This chapter prices "
        "routine automation, separates BESS parcels from data-center campuses, and "
        "connects private-branded filing-trigger mail to qualified introductions. The "
        "operating objective is measured removal of repetitive minutes, with recoverable "
        "failures and documented human accountability."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual realized assignment, origination milestone, and development carry revenue",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual realized assignment, origination milestone, and development carry revenue",
            "note": "42.0% net margin; $212,100 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual realized assignment, origination milestone, and development carry revenue",
            "note": "54% net margin; $486,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence pipeline before increasing parcel throughput",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a parcel-centered evidence ledger, not a chatbot searching "
                    "for cheap land. A Python scheduler retrieves permitted downloads from "
                    "PJM, MISO, ERCOT, utility hosting-capacity portals, county GIS services, "
                    "and recorder indexes. Use urllib.request for transport, csv and json "
                    "for structured records, sqlite3 for the local ledger, and hashlib "
                    "for immutable source fingerprints. Each observation carries the source "
                    "URL, retrieval time, effective date, coordinate reference, parser version, "
                    "and parcel identifier. Queue identifiers belong in a separate relationship "
                    "table because one project can span several parcels and one parcel can "
                    "attract several proposals. Keep raw snapshots alongside normalized fields "
                    "so a changed column name cannot silently alter a capacity claim. Public "
                    "availability does not establish permission for unlimited automated access; "
                    "honor access terms, request limits, and licensed reuse boundaries. Schedule "
                    "county ownership refreshes separately from utility engineering updates. A "
                    "daily deed event may justify owner outreach, while a monthly utility map "
                    "cannot support a same-day capacity assertion. The eleven-play map below "
                    "uses one supplied canonical identifier and ten descriptive implementation "
                    "labels. Its purpose is to assign an economic test and a recovery path "
                    "to every repetitive activity before volume increases."
                ),
                (
                    "Measure the seventy-percent objective against observed human minutes, "
                    "not the percentage of screens that contain an AI feature. An illustrative "
                    "benchmark processes 100 routine parcel packets with a 1,000-minute manual "
                    "baseline: 420 research minutes, 240 qualification minutes, 180 fulfillment "
                    "minutes, and 160 acquisition-administration minutes. After including review "
                    "and exception handling, target net reductions of 330, 180, 120, and 100 "
                    "minutes respectively. That removes 730 minutes, or 73%, leaving 270 "
                    "human minutes. Deep utility studies, negotiations, field visits, and title "
                    "resolution remain outside this routine-task benchmark and retain separate "
                    "time budgets. The principal owns utility representations, option commitments, "
                    "and buyer negotiations. Three contractors cover GIS and research, electrical "
                    "feasibility, and title/document operations; any licensed legal work uses "
                    "appropriately qualified counsel. Record reviewer identity and elapsed time "
                    "at each consequential transition. If source deterioration increases review "
                    "time, report the lower achieved automation rate instead of hiding those "
                    "minutes in another category. Run a weekly matched sample against manual "
                    "processing, checking missed restrictions and incorrect parcel joins. A "
                    "faster pipeline that distributes the wrong owner or transformer evidence "
                    "has increased liability and rework rather than productive capacity."
                ),
                (
                    "Treat language models as constrained extraction workers. Submit a bounded "
                    "document excerpt and request fields such as study date, stated project "
                    "type, MW quantity, limiting condition, and supporting quotation. Validate "
                    "the returned JSON against explicit keys, numeric ranges, and required "
                    "evidence spans before storing it. Absence of a supported value produces "
                    "a pending-evidence state, never a fabricated engineering answer. Models "
                    "must not obey instructions embedded in filings, contact landowners, edit "
                    "option terms, or publish packets. An illustrative 100-parcel routine batch "
                    "budgets $6 for licensed source access, $4 for compute, $8 for model "
                    "usage, and $2 for evidence storage: $20 total, or $0.20 per parcel. "
                    "The model allowance assumes two million input tokens at $2 per million "
                    "and half a million output tokens at $8 per million; these are budgeting "
                    "assumptions rather than vendor quotes. Adding 270 review minutes at "
                    "$60 per hour produces $290, or $2.90 per routine packet. This excludes "
                    "mail, surveys, engineering, legal work, and option deposits. Cap spending "
                    "per batch, cache unchanged documents by fingerprint, and reroute malformed "
                    "responses to deterministic parsing or manual entry rather than repeatedly "
                    "paying for an unsupported answer."
                ),
            ],
            "table": {
                "caption": "Eleven-Play Implementation Map with Explicit Cost Tests and Recovery Paths",
                "headers": [
                    "Mapped play or implementation label",
                    "Automated operating mechanism",
                    "Illustrative unit economics",
                    "Human check and failure recovery",
                ],
                "rows": [
                    [
                        "public_filing_trigger_mail_arbitrage",
                        "Join permitted business filings and recorded deeds to verified owner addresses.",
                        "Two hundred private-branded letters at $1.10 require $220 before research.",
                        "Review creative and recipients; suppress ambiguous matches before any mailing.",
                    ],
                    [
                        "Queue change detection for relevant service territories",
                        "Compare dated ISO exports and retain project-level changes with source fingerprints.",
                        "Thirty scheduled scans at $0.50 consume $15 before analyst interpretation.",
                        "Analyst separates generation queue changes from actual retail load availability.",
                    ],
                    [
                        "Substation proximity triage across candidate parcel clusters",
                        "Use licensed GIS distances to rank research work without asserting capacity.",
                        "One hundred distance checks at $0.02 consume $2 of compute.",
                        "Electrical reviewer rejects distance alone as evidence of deliverable power.",
                    ],
                    [
                        "Utility study extraction into a controlled evidence ledger",
                        "Extract dated limits and quotations from authorized utility correspondence packets.",
                        "Twenty bounded extraction jobs at $0.40 require $8 in model allowance.",
                        "Principal verifies every distributed MW statement against its underlying document.",
                    ],
                    [
                        "Wetland and flood constraint screening before deposits",
                        "Intersect parcel boundaries with dated wetland inventories and FEMA hazard layers.",
                        "Fifty automated intersections at $0.10 require $5 before specialist interpretation.",
                        "Environmental reviewer escalates ambiguous boundaries rather than declaring jurisdiction conclusively.",
                    ],
                    [
                        "Mineral reservation and surface access issue extraction",
                        "Flag deed exceptions and lease references inside authorized title document sets.",
                        "Ten document extractions at $0.50 consume $5 before title review.",
                        "Title specialist checks missing instruments and routes defects to qualified counsel.",
                    ],
                    [
                        "Local zoning change detection for target municipalities",
                        "Track official agendas and adopted code text for use-specific changes.",
                        "Twenty monitored jurisdictions at $0.25 require $5 per collection cycle.",
                        "Local reviewer confirms effective dates and separates proposals from adopted restrictions.",
                    ],
                    [
                        "Fiber route evidence matching for campus candidates",
                        "Associate carrier correspondence and route evidence with each campus access plan.",
                        "Ten evidence matches at $0.20 consume $2 before carrier engineering.",
                        "Carrier confirmation replaces map assumptions about capacity and physically diverse entrances.",
                    ],
                    [
                        "Milestone-contingent option document assembly for approved parcels",
                        "Populate approved templates from reviewed terms and versioned parcel schedules.",
                        "Four assemblies at $1 require $4 before legal document review.",
                        "Principal and counsel verify dates, assignment rights, deposits, and owner authority.",
                    ],
                    [
                        "Buyer mandate matching and controlled packet distribution",
                        "Rank authorized buyer requirements against documented capacity and site constraints.",
                        "Forty mandate matches at $0.05 consume $2 before relationship outreach.",
                        "Principal releases accurate packets only to permitted recipients with current mandates.",
                    ],
                    [
                        "Evidence-led market briefs and tracked referral routing",
                        "Publish reviewed aggregate insights and attach attribution codes to permitted referrals.",
                        "One $150 brief producing three accepted introductions costs $50 each.",
                        "Remove unsupported claims and route introductions through lawful compensation structures.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Automate evidence handling, not engineering conclusions",
                "body": "Experienced originators preserve the distinction between an attractive map feature and a transferable, studied commercial position.",
                "items": [
                    "Store substation aliases and utility identifiers separately; similar names can refer to different voltage yards or service arrangements.",
                    "Fingerprint the utility attachment, not just the email thread, so a revised upgrade estimate invalidates the correct downstream packet.",
                    "Keep charging import limits and discharge export limits in different BESS fields; a single MW column hides material constraints.",
                    "Buy the smallest useful source subscription first, then expand only after measured parcel joins and owner matches survive manual sampling.",
                ],
            },
        },
        {
            "heading": "2. Separate map-based screening from utility-backed site qualification",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build two independent qualification schemas. Standalone BESS starts with "
                    "a 5–25 acre parcel envelope, usable area, access geometry, fire access, "
                    "setbacks, topography, charging import, discharge export, and interconnection "
                    "position. An AI data-center campus adds materially different requirements: "
                    "firm load service, energization phases, redundant service architecture, "
                    "fiber diversity, cooling strategy, water availability where required, "
                    "noise limits, and expansion area. A 69kV–345kV line near either property "
                    "is only a screening feature. A hosting-capacity layer can also describe "
                    "a particular generation assumption rather than firm load availability. "
                    "Never translate its displayed number directly into sellable campus MW. "
                    "Store service type, study scope, issuing utility, conditions, expected "
                    "in-service date, and estimated network-upgrade exposure together. FERC "
                    "interconnection requirements under 18 CFR 35.28 provide relevant context "
                    "for covered generation interconnections; they do not replace the utility's "
                    "retail load-service process or establish jurisdiction over every project. "
                    "When a developer requests a capacity headline, respond with the actual "
                    "documented service position and its limitations. Until the utility resolves "
                    "deliverability, price the parcel as a conditional development lead rather "
                    "than a powered asset. This distinction belongs in database fields, "
                    "marketing text, and the assignment agreement."
                ),
                (
                    "Use environmental and title automation to prioritize specialist work, "
                    "not to issue definitive clearance. FEMA's National Flood Hazard Layer "
                    "and the U.S. Fish and Wildlife Service National Wetlands Inventory "
                    "can expose obvious conflicts quickly, but map age, scale, and unmapped "
                    "features limit conclusions. A wetland inventory is not a jurisdictional "
                    "determination under Clean Water Act Section 404, 33 U.S.C. 1344. "
                    "Record source dates and route potential aquatic-resource impacts to an "
                    "environmental specialist before committing to grading assumptions. County "
                    "zoning portals require similar discipline: store adopted text, district "
                    "boundaries, use definitions, effective dates, and temporary moratorium "
                    "actions separately. A staff email may explain process without establishing "
                    "an entitlement. Title extraction must flag severed mineral interests, "
                    "surface-use rights, leases, easements, and missing referenced instruments. "
                    "Do not describe a mineral waiver as secured until the correct rights "
                    "holder has executed an effective instrument. Python can reconcile "
                    "document references and flag exceptions; it cannot resolve competing "
                    "property rights. For campus candidates, obtain carrier evidence covering "
                    "actual serviceability and route separation. Two providers sharing the "
                    "same duct bank do not create physical diversity, and a nearby backbone "
                    "does not establish a usable local connection."
                ),
                (
                    "Value option interests against documented service outcomes and explicit "
                    "downside branches. Consider an illustrative BESS candidate whose utility "
                    "study supports a conditional 20 MW export position and identifies "
                    "$1.2 million of upgrade exposure. At an assumed $6,000 per documented "
                    "MW, a negotiated origination milestone would be $120,000; the developer's "
                    "$60,000 per MW upgrade burden is separate project expenditure, not "
                    "operator revenue. If a restudy doubles upgrades to $2.4 million, "
                    "recalculate buyer demand and milestone probability before paying an "
                    "extension. An illustrative branch with a 40% chance of collecting "
                    "$120,000, $22,000 of remaining diligence and option spending, and "
                    "$8,000 of closing expense only on success produces $22,800 of "
                    "expected incremental contribution: $48,000 less $22,000 less $3,200. "
                    "That estimate supports a decision, not booked revenue. For a campus, "
                    "build a separate load-service schedule; a BESS export study cannot "
                    "substitute for campus import rights. If energization slips beyond the "
                    "12–24 month option term, obtain a priced extension or terminate before "
                    "the next deposit. Carry expired option fees as real portfolio expenses. "
                    "A failed utility validation should reduce the budget immediately rather "
                    "than survive as an optimistic pipeline asset."
                ),
            ],
            "table": {
                "caption": "Site-Specific Evidence Requirements Before Money or Capacity Claims Move",
                "headers": [
                    "Decision requiring documented support",
                    "BESS parcel evidence requirement",
                    "AI campus evidence requirement",
                    "Stop condition and recovery action",
                ],
                "rows": [
                    [
                        "Establish the actual electrical service product",
                        "Separate charging imports from discharge exports and study their operating conditions.",
                        "Obtain utility load-service scope with phased firm MW and timing assumptions.",
                        "Suspend capacity marketing whenever the available study addresses a different service.",
                    ],
                    [
                        "Quantify upgrade exposure before extending option duration",
                        "Identify assigned upgrade estimates and possible restudy or withdrawal consequences.",
                        "Identify substations, feeders, transformers, and upstream works required for staged load.",
                        "Reprice or exit when revised upgrades destroy the buyer's development economics.",
                    ],
                    [
                        "Confirm physical development area after mapped constraints",
                        "Test usable acreage against setbacks, fire access, grading, and equipment spacing.",
                        "Test building blocks against cooling infrastructure, stormwater facilities, and future expansion.",
                        "Order specialist field work when mapped layers conflict with observed conditions.",
                    ],
                    [
                        "Resolve mineral interests and access rights before assignment",
                        "Review surface interference exposure and recorded access serving heavy equipment delivery.",
                        "Review utility easements, campus entrances, and rights supporting long-lived infrastructure corridors.",
                        "Pause packet release until missing instruments and rights holders are resolved.",
                    ],
                    [
                        "Validate the current local land-use pathway",
                        "Confirm storage use classification and applicable fire service requirements with officials.",
                        "Confirm data-center use classification, water constraints, noise limits, and moratorium status.",
                        "Terminate or renegotiate deposits when adopted restrictions defeat the intended use.",
                    ],
                    [
                        "Match infrastructure timing to enforceable option duration",
                        "Align interconnection milestones with deposit dates and negotiated extension rights.",
                        "Align load energization and carrier construction with campus delivery obligations.",
                        "Exercise an agreed extension or exit before avoidable option fees become due.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before distributing a priced site",
                "body": "A named reviewer must complete each check against current evidence; automated scores alone cannot authorize release.",
                "items": [
                    "Verify the parcel, owner authority, option interest, assignment restrictions, and any required broker participation under the relevant state's rules.",
                    "Verify the issuing utility's document, service direction, conditional MW, upgrade exposure, and energization assumptions; label unresolved study work explicitly.",
                    "Verify adopted zoning restrictions, moratorium status, environmental screening limitations, mineral exceptions, and infrastructure dependencies for the intended use.",
                    "Verify deposit exposure, expiration reminders, buyer permissions, compensation terms, and a version-matched statement of every material qualification.",
                ],
            },
        },
        {
            "heading": "3. Assemble transferable option packets and reconcile every scenario",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Turn the option packager into a controlled document compiler. Approved "
                    "fields include legal owner names, parcel schedules, consideration, diligence "
                    "periods, access permissions, assignment conditions, extension prices, notice "
                    "methods, and termination mechanics. The model may propose an extraction "
                    "from a source document, but only reviewed values enter the executable "
                    "template. A milestone-contingent 12–24 month option should make utility "
                    "investigation and land-use diligence commercially usable without implying "
                    "that every deposit is refundable. Counsel must draft the actual "
                    "conditions and notice requirements. Hold the principal's own recorded "
                    "or equitable option interest where appropriate, and involve licensed "
                    "state real-estate brokers when the activity requires licensure. Principal "
                    "status is not a universal exemption for arranging other parties' "
                    "transactions. For example, Texas Occupations Code Section 1101.002 "
                    "defines covered brokerage activity; apply the full local framework "
                    "to the actual compensation and conduct. The generated packet includes "
                    "an evidence index, dated utility qualifications, an upgrade sensitivity, "
                    "an unresolved-issues register, and a buyer-specific summary. Send a "
                    "draft for principal and counsel review before signature. Capture "
                    "execution and delivery evidence separately from template generation "
                    "so a successful API response cannot masquerade as an effective agreement."
                ),
                (
                    "Reconcile the packager's commercial ledger to the canonical Formula "
                    "v2.0 scorecard without importing project asset values. Conservative "
                    "revenue is $110,000, expenses are $77,000, and owner net profit "
                    "is $33,000 at 30%. Base revenue is $505,000, expenses are "
                    "$292,900, and owner net profit is $212,100 at 42.0%. Scaled "
                    "revenue is $900,000, expenses are $414,000, and owner net profit "
                    "is $486,000 at 54%. Conservative and Base use 1 FT plus "
                    "3 C; Scaled uses 2 FT plus 4 C. One illustrative Base "
                    "revenue composition is three $100,000 assignments, five distinct "
                    "$31,000 earned milestones, and $50,000 of realized development carry. "
                    "The total is exactly $505,000. Underlying land consideration, battery "
                    "equipment purchases, campus construction expenditure, and developer upgrade "
                    "payments never enter this revenue total merely because the operator "
                    "helped originate them. Track milestone offsets so a closing payment "
                    "does not count an earlier credited fee twice. Apply ASC 606 "
                    "principal-versus-agent analysis to the actual contracts; third-party "
                    "collections are not automatically gross operator revenue. No separate "
                    "retained-share multiplier is supplied for this candidate, so do not "
                    "invent one. Expected carry remains outside realized case revenue."
                ),
                (
                    "Make automation savings visible inside the expense envelope rather "
                    "than adding them a second time to profit. An illustrative Base "
                    "allocation assigns $108,000 to recurring operations, $96,000 to "
                    "deal-specific contractor work, $55,000 to studies, legal work, and "
                    "travel, $18,000 to expired option fees, and $15,900 to outbound "
                    "acquisition. These mutually exclusive buckets total $292,900. Assign "
                    "each invoice once; recurring operations and contractor work must not "
                    "duplicate the same labor. The $108,000 recurring bucket equals "
                    "$9,000 monthly, inside the stated $1,800–$11,000 monthly operating "
                    "range, while deal expenses remain additional and lumpy. Startup "
                    "capital of $10,000–$50,000 and a two-to-six-month first-deal window "
                    "do not imply that every portfolio can fund its options without "
                    "further receipts. Use a rolling thirteen-week cash schedule that "
                    "shows deposit deadlines, review costs, expected receipts, and missed "
                    "milestone branches. For the $18,000 expiry allocation, six failed "
                    "options at $3,000 each provide a concrete burn assumption. If "
                    "observed failures exceed it, reduce new commitments or revise the "
                    "forecast while preserving the canonical reference case. Staffing "
                    "expansion should follow evidenced reviewer capacity and signed demand, "
                    "not a larger count of unqualified map pins."
                ),
            ],
            "table": {
                "caption": "Canonical Revenue Reconciliation and Packet-Level Ledger Controls",
                "headers": [
                    "Scenario or ledger control",
                    "Revenue construction or accounting treatment",
                    "Expense and profit reconciliation",
                    "Operating interpretation and release condition",
                ],
                "rows": [
                    [
                        "Conservative case with one principal and three contractors",
                        "$110,000 revenue can comprise one $80,000 assignment and two $15,000 milestones.",
                        "$77,000 expenses leave $33,000 owner net profit at exactly 30% margin.",
                        "Count separately earned payments only; do not include developer asset purchases.",
                    ],
                    [
                        "Base case with one principal and three contractors",
                        "$505,000 revenue comprises $300,000 assignments, $155,000 milestones, and $50,000 realized carry.",
                        "$292,900 expenses leave $212,100 owner net profit at exactly 42.0% margin.",
                        "Use reviewed contracts and delivery evidence to support each recognized payment.",
                    ],
                    [
                        "Scaled case with two employees and four contractors",
                        "$900,000 revenue can comprise $600,000 assignments, $240,000 milestones, and $60,000 realized carry.",
                        "$414,000 expenses leave $486,000 owner net profit at exactly 54% margin.",
                        "Six total people require sufficient reviewer capacity before expanding qualified throughput.",
                    ],
                    [
                        "Expired option fees remain visible portfolio operating costs",
                        "Failed utility or zoning candidates generate no assumed assignment revenue.",
                        "Six expired deposits at $3,000 each consume the $18,000 Base allocation.",
                        "Compare actual expiry losses monthly and stop weak candidates before extensions.",
                    ],
                    [
                        "Developer capital and pass-through collections remain separately classified",
                        "Land prices and construction budgets do not become operator revenue through origination.",
                        "Evaluate contract-specific gross versus net presentation before posting third-party collections.",
                        "Bookkeepers reconcile cash movements to contractual rights rather than bank deposits alone.",
                    ],
                    [
                        "Milestone credits and carry require explicit ledger treatment",
                        "Subtract credited advances from closing proceeds to prevent duplicate fee recognition.",
                        "Keep projected carry outside realized revenue until its recognition conditions are met.",
                        "Principal checks the settlement statement against the complete prior payment history.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the reviewed evidence set",
                    "action": "Create a versioned manifest of parcel records, utility documents, title exceptions, and adopted zoning evidence.",
                    "detail": "Store document fingerprints, retrieval dates, reviewer identities, and unresolved issues; preserve the prior version for comparison.",
                },
                {
                    "step": 2,
                    "title": "Compile the conditional option packet",
                    "action": "Populate approved templates from reviewed fields and calculate deposits, extensions, notice dates, and milestone offsets.",
                    "detail": "Keep source quotations linked to material capacity statements; route legal terms to qualified counsel before execution.",
                },
                {
                    "step": 3,
                    "title": "Release through a named human decision",
                    "action": "Have the principal confirm buyer permissions, accurate utility qualifications, compensation structure, and document version.",
                    "detail": "Record the recipient list and release decision; no model-generated score or webhook may substitute for this step.",
                },
                {
                    "step": 4,
                    "title": "Reconcile execution, cash, and expiry exposure",
                    "action": "Match signed documents and settlement records to invoices, milestone credits, deposits, and the rolling cash schedule.",
                    "detail": "Schedule reminders before contractual notice deadlines and terminate unsuccessful candidates through the agreed delivery method.",
                },
            ],
        },
        {
            "heading": "4. Compound qualified distribution without automating misleading claims",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Implement public_filing_trigger_mail_arbitrage as a privately branded "
                    "research-to-contact loop, not an imitation government demand. Where "
                    "access and reuse are permitted, ingest daily Secretary of State "
                    "new-LLC filings and county recorder deed or mortgage events. Resolve "
                    "entity names against actual parcel ownership, suppress duplicates, "
                    "and distinguish registered-agent addresses from useful operating contacts. "
                    "New ownership near a screened infrastructure corridor can trigger "
                    "a truthful invitation to discuss a conditional site option. The "
                    "broader play also supports genuine recurring workplace compliance "
                    "updates, property-tax appeal contingency offers, or permissioned "
                    "exclusive new-mover and B2B introductions through appropriately "
                    "qualified providers. These are separate service funnels, not extra "
                    "revenue silently added to the powered-land scorecard. Prohibit "
                    "government-lookalike poster or deed invoices, official-looking seals, "
                    "invented citation numbers, and language suggesting mandatory payment. "
                    "39 U.S.C. 3001 restricts specified deceptive mailed solicitations; "
                    "California Business and Professions Code Section 17537.9 imposes "
                    "specific requirements on covered recorded-document solicitations. Review "
                    "the actual offer and target state before mailing. A direct-mail "
                    "API may render and dispatch an approved creative, but a human "
                    "must authorize the recipient segment and final proof. If ownership "
                    "resolution is weak, stop the mailing rather than multiplying bad "
                    "matches with personalization."
                ),
                (
                    "Use explicit acquisition arithmetic to decide which distribution "
                    "loop deserves another dollar. An illustrative mailing sends 200 "
                    "letters at $1.10 each, costing $220, with an additional $80 "
                    "of matching and review labor. At a 4% response rate, eight "
                    "responses cost $37.50 each; if two become qualified owner "
                    "conversations, acquisition cost is $150 per qualified conversation. "
                    "A conversation is neither an option nor a closed assignment. "
                    "For a separate subscription test, ten customers paying $240 "
                    "annually create $2,400 of annual gross billings before provider "
                    "shares, fulfillment, refunds, and acquisition costs. An appeal "
                    "provider charging 20% of an actual $10,000 assessment-related "
                    "tax saving earns $2,000 under that illustrative agreement, "
                    "subject to the applicable practice and fee rules. Keep both "
                    "experiments outside the canonical land-option forecast. For the "
                    "core business, publish reviewed territory briefs with dated "
                    "utility context, aggregate constraints, and an invitation to "
                    "submit buyer mandates. Avoid parcel-level disclosures without "
                    "permission. Track qualified introductions from each brief and "
                    "ask satisfied buyers for introductions to adjacent project "
                    "teams. Compensated referrals require state-specific review of "
                    "brokerage restrictions. Commercial email must satisfy applicable "
                    "15 U.S.C. 7704 requirements, including accurate headers, identification, "
                    "postal address, and a working opt-out process."
                ),
                (
                    "Keep the distribution flywheel recoverable. Incoming webhooks "
                    "require signature verification, timestamp checks, replay protection, "
                    "and a persisted event identifier before processing. Use hmac.compare_digest "
                    "for signature comparison and a SQLite uniqueness constraint "
                    "for idempotency. Separate receipt of an event from permission "
                    "to send mail, release documents, or spend deposits. A retry "
                    "should resume the approved action, not create another letter "
                    "or duplicate invoice. Back off after rate-limit responses, "
                    "quarantine malformed payloads, and retain a manual export "
                    "path for source outages. If a utility revises its study, "
                    "invalidate every downstream packet that references the old "
                    "fingerprint and notify recipients who received affected claims. "
                    "If a model fails extraction tests, switch to deterministic "
                    "fields and human review without changing the evidence standard. "
                    "During an outage, continue only work supported by current "
                    "records; pause stale capacity claims and time-sensitive commitments. "
                    "A weekly dashboard should show accepted introductions, utility "
                    "validation rate, deposit burn, review minutes, packet corrections, "
                    "and collected operator fees. Measure source-to-qualified-option "
                    "conversion by cohort rather than celebrating raw traffic. "
                    "Increase distribution only when current evidence, reviewer "
                    "capacity, and cash runway support the added workload. "
                    "The compounding asset is a trusted record of precise "
                    "introductions, not an ever-larger address list."
                ),
            ],
            "table": {
                "caption": "Distribution Economics, Human Release Points, and Failure Recovery",
                "headers": [
                    "Acquisition or recovery mechanism",
                    "Concrete operating measurement",
                    "Required human intervention",
                    "Fallback preserving cost and evidence discipline",
                ],
                "rows": [
                    [
                        "Private-branded filing-trigger mail to verified property owners",
                        "A $300 campaign yielding two qualified conversations costs $150 per conversation.",
                        "Principal approves the segment, private branding, final proof, and commercial offer.",
                        "Suppress uncertain matches and manually verify ownership before restarting the campaign.",
                    ],
                    [
                        "Separate recurring workplace update subscription experiment",
                        "Ten annual customers at $240 produce $2,400 before provider and fulfillment costs.",
                        "Qualified provider verifies genuine service scope and all advertised update commitments.",
                        "Stop renewal promotion when delivery evidence fails and resolve affected customer accounts.",
                    ],
                    [
                        "Separate assessment appeal introduction with qualified provider participation",
                        "A 20% contractual fee on $10,000 actual savings produces $2,000 provider revenue.",
                        "Qualified practitioner checks representation rules, contingency terms, and documented realized savings.",
                        "Avoid quoting savings before assessment evidence and route complex matters to specialists.",
                    ],
                    [
                        "Programmatic territory briefs with permissioned buyer referral requests",
                        "A $150 reviewed brief yielding three accepted introductions costs $50 each.",
                        "Principal removes unsupported capacity claims and checks parcel disclosure permissions.",
                        "Publish aggregate constraints only when project-specific disclosure rights are absent.",
                    ],
                    [
                        "Authenticated webhook processing and duplicate action prevention",
                        "One unique event identifier permits only one authorized mailing dispatch record.",
                        "Operator investigates replay alerts, signature failures, and unexpected recipient changes.",
                        "Quarantine suspect events and reconcile provider records before any manual resend.",
                    ],
                    [
                        "Capacity revision propagation across previously released buyer packets",
                        "One changed source fingerprint identifies every affected packet and recipient.",
                        "Electrical reviewer validates replacement evidence before the principal authorizes redistribution.",
                        "Withdraw stale claims immediately and provide corrected qualifications through tracked delivery.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail aggressively, but never let a map pin sign a power claim.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create separate BESS and campus schemas with explicit utility service direction, study status, documented MW, upgrade exposure, and energization dates.",
        "Benchmark 100 routine parcel packets, include review minutes, and test whether net repetitive-time removal actually reaches 70% or more.",
        "Implement source fingerprints, bounded model extraction, webhook signature checks, replay protection, and idempotent dispatch records.",
        "Compile reviewed 12–24 month option packets with assignment conditions, deposit exposure, extension prices, and tracked notice deadlines.",
        "Launch a 200-letter private-branded pilot only after ownership verification and human creative approval; measure qualified conversations rather than responses alone.",
        "Reconcile realized operator revenue and expired option fees to the exact three scorecard cases, keeping land prices and developer capital outside revenue.",
    ],
    "statutory_citations": [
        {
            "title": "18 CFR 35.28 — Non-discriminatory open access transmission tariff",
            "url": "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
            "relevance": "Provides relevant federal tariff and interconnection requirements; distinguish covered generation interconnection from a utility's retail load-service determination.",
        },
        {
            "title": "33 U.S.C. 1344 — Permits for dredged or fill material",
            "url": "https://www.law.cornell.edu/uscode/text/33/1344",
            "relevance": "Explains why mapped wetland screening cannot substitute for project-specific evaluation of regulated discharges and required permits.",
        },
        {
            "title": "39 U.S.C. 3001 — Nonmailable matter",
            "url": "https://www.law.cornell.edu/uscode/text/39/3001",
            "relevance": "Restricts specified deceptive mail solicitations, including covered government-affiliation implications and invoice-like solicitations requiring prescribed treatment.",
        },
        {
            "title": "California Business and Professions Code Section 17537.9",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17537.9.&lawCode=BPC",
            "relevance": "Sets requirements for covered solicitations offering copies of recorded documents; evaluate deed-related campaigns against the actual statutory scope.",
        },
        {
            "title": "Texas Occupations Code Section 1101.002 — Definitions",
            "url": "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1101.htm#1101.002",
            "relevance": "Defines covered real-estate brokerage activity; evaluate option assignments, introductions, and compensation under the complete applicable state framework.",
        },
        {
            "title": "15 U.S.C. 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email practices including header accuracy, required identification and address information, and opt-out handling.",
        },
    ],
}
