from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-day-launch-sprint-kill-fix-scale-gates",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching ai data-center powered land, substation headroom & bess site optioning, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "A Four-Person Launch Pod for Utility-Validated MW, Separate BESS and AI Campus Options, Controlled Fee Burn, and Day-30/60/90 Capital Decisions",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #47 ranks #15 of 49 with a 92/100 Money-to-Manpower Score. "
        "This sprint sequences 11 mapped plays into a four-person origination pod: "
        "one full-time principal and three contractors covering GIS, electrical diligence, "
        "and property rights. Days 1–7 establish buyer specifications and screen parcels; "
        "Days 8–14 test utility and zoning feasibility; Days 15–21 negotiate contingent "
        "options; Days 22–30 package evidence and make capital decisions. Separate "
        "5–25-acre standalone BESS sites from fiber-, water-, and zoning-constrained "
        "AI campuses. Cap first-month cash deployment at $7,500 against a $25,000 "
        "launch account. Annual owner-profit cases remain $33,000 Conservative, $212,100 "
        "Base, and $486,000 Scaled. Day-30/60/90 thresholds expand diligence only when "
        "documented utility progress, buyer engagement, and remaining cash justify it."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual realized option assignment, origination milestone, and development-carry revenue",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual realized option assignment, origination milestone, and development-carry revenue",
            "note": "42.0% net margin; $212,100 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual realized option assignment, origination milestone, and development-carry revenue",
            "note": "54% net margin; $486,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Translate Eleven Plays into a Funded, Four-Person Search",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Launch a narrow search rather than a speculative land portfolio. "
                    "Candidate #47 has eleven mapped operator plays; use the following "
                    "execution labels to connect them to observable work products. P01 "
                    "captures developer requirements; P02 screens 69kV–345kV substations "
                    "and corridors; P03 reconciles queue records; P04 identifies parcel "
                    "owners; P05 checks floodplain, wetlands, mineral interests, and access; "
                    "P06 verifies zoning pathways; P07 obtains utility service evidence; "
                    "P08 verifies fiber and water; P09 structures assignable contingent "
                    "options; P10 packages developer diligence; P11 negotiates assignment, "
                    "milestone, and carry economics. These labels organize this chapter, "
                    "rather than purporting to reproduce an external play taxonomy. Start "
                    "with two adjacent jurisdictions and one utility territory. Select "
                    "three credible developers whose written acquisition criteria cover "
                    "either standalone storage or AI campuses. Record requested MW, "
                    "acceptable service dates, acreage, security requirements, and upgrade "
                    "budgets separately for each buyer. The principal owns outreach and "
                    "investment decisions; a GIS contractor owns screening; an electrical "
                    "contractor owns utility questions; a property-rights contractor owns "
                    "title and option coordination. Retain appropriately licensed counsel "
                    "or brokerage expertise within that third workstream. No contractor "
                    "may promise capacity, sign an option, or authorize additional spending."
                ),
                (
                    "Fund the illustrative sprint with $25,000, inside the canonical "
                    "$10,000–$50,000 startup range, and cap first-month cash deployment "
                    "at $7,500. Allocate $4,500 to operating expense: $1,200 GIS support, "
                    "$1,500 electrical support, $1,200 property-rights support, and $600 "
                    "for software, records, and communications. Allocate another $1,000 "
                    "to targeted external diligence and $2,000 to option consideration, "
                    "leaving $17,500 untouched. The principal takes no cash draw during "
                    "this sprint; personal living costs require separate funding. These "
                    "are procurement ceilings, not assertions that specialist work fits "
                    "every local market. Obtain fixed-scope quotes before ordering, and "
                    "reduce parcel volume if quotes exceed the envelope. Reserve the "
                    "entire $2,000 option allocation as potentially unrecoverable because "
                    "utility or zoning diligence can eliminate otherwise attractive "
                    "sites. This loss allowance describes the same cash, not another "
                    "expense added twice. No study deposit, extension payment, or "
                    "nonrefundable reservation may sit outside the ledger. Maintain "
                    "weekly committed, paid, refundable, and remaining balances. A "
                    "$10,000-funded launch must use a smaller screening-only scope until "
                    "additional funding or developer-paid diligence becomes available; "
                    "it cannot responsibly copy this $25,000 cash plan."
                ),
                (
                    "Build one evidence register in SQLite or a controlled spreadsheet, "
                    "with QGIS handling spatial overlays. Every parcel record needs its "
                    "assessor identifier, owner source, acreage, utility territory, "
                    "nearest relevant facilities, source date, and separate confidence "
                    "fields for physical observations and utility conclusions. Import "
                    "public PJM queue material where applicable, FEMA flood layers, "
                    "USFWS wetland screening layers, county zoning maps, and recorded "
                    "property instruments. Public layers identify questions; they do "
                    "not establish service availability, jurisdictional wetland boundaries, "
                    "or marketable title. Set a first-week funnel of forty raw parcels, "
                    "twelve desk-screen survivors, and six owner contacts with verified "
                    "contact provenance. Split the twelve survivors between the two "
                    "asset types rather than pooling acreage or power assumptions. "
                    "Storage candidates must fit a 5–25-acre usable footprint with "
                    "access, setbacks, and a plausible interconnection pathway. Campus "
                    "candidates require buyer-specific expandable area, cooling strategy, "
                    "fiber access, and a credible load-service pathway. Put proximity "
                    "measurements in a geography field, never a deliverable-MW field. "
                    "At the end of Day 7, the principal signs the source register "
                    "and rejects records that cannot be reproduced from dated evidence."
                ),
            ],
            "table": {
                "caption": "Days 1–7: Buyer Specifications, Budget Authority, and Reproducible Parcel Screening",
                "headers": [
                    "Execution day and mapped play",
                    "Accountable pod member and concrete action",
                    "Required deliverable and evidence trail",
                    "Quantitative acceptance threshold or spending constraint",
                ],
                "rows": [
                    [
                        "Day 1 establishes the P01 buyer mandate",
                        "Principal interviews developers and separates storage from campus requirements",
                        "Three dated buyer briefs identify power, timing, land, and infrastructure needs",
                        "Proceed with two jurisdictions inside one selected utility territory",
                    ],
                    [
                        "Day 2 establishes funding across all eleven plays",
                        "Principal approves contractor scopes and opens the committed-cash ledger",
                        "Written purchase limits distinguish operating expense, diligence, and option consideration",
                        "Authorize at most $7,500 against the $25,000 launch account",
                    ],
                    [
                        "Day 3 activates P02 geographic opportunity screening",
                        "GIS contractor maps relevant substations and 69kV–345kV transmission corridors",
                        "Forty parcel records preserve dated source links and assessor identifiers",
                        "Assign zero deliverable MW from geographic proximity alone",
                    ],
                    [
                        "Day 4 connects P03 queues with P07 service questions",
                        "Electrical contractor separates generation interconnection records from large-load service evidence",
                        "Utility contact register identifies applicable tariffs and formal inquiry channels",
                        "Every priority parcel receives an explicitly labeled service-evidence status",
                    ],
                    [
                        "Day 5 advances P04 ownership and P05 fatal-flaw screening",
                        "Property-rights contractor verifies ownership while GIS contractor flags physical constraints",
                        "Parcel evidence packs retain access, flood, wetland, and mineral questions",
                        "Reduce forty raw parcels to twelve reproducible desk-screen survivors",
                    ],
                    [
                        "Day 6 tests P06 zoning and P08 infrastructure",
                        "Principal requests planning guidance and buyer-specific fiber and water specifications",
                        "Two separate screening templates prevent storage and campus assumption mixing",
                        "Reject explicit use prohibitions unless a documented feasible alternative exists",
                    ],
                    [
                        "Day 7 consolidates P01 through P08 screening evidence",
                        "Principal reviews sources and approves the second-week outreach list",
                        "Twelve surviving records include six owner contacts with verified provenance",
                        "Carry forward only records with dated evidence and named next actions",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy Evidence Before Buying More Option Time",
                "body": "Experienced originators protect bargaining leverage by resolving the most expensive uncertainties before increasing nonrefundable consideration.",
                "items": [
                    "Ask the utility which specific service study, tariff process, and customer authorization apply before purchasing an elaborate electrical concept package.",
                    "Request separate BESS charging and export assumptions; export feasibility does not establish import service or acceptable operating restrictions.",
                    "Ask fiber providers for route-level feasibility, construction responsibility, and diversity evidence; two carriers can share the same vulnerable conduit.",
                    "Negotiate diligence extensions against identifiable utility or planning events, with capped payments and written notice mechanics instead of automatic monthly fee escalation.",
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Replace Apparent Headroom with Utility and Land-Use Evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The second week converts attractive map positions into explicit "
                    "utility questions. P07 should produce a utility-authored response "
                    "or a documented route to the required study, not an originator's "
                    "estimate dressed as capacity. Ask for the proposed service point, "
                    "voltage, import and export requirements, study prerequisites, "
                    "upgrade responsibility, indicative timing, and treatment of "
                    "competing requests. A queue entry establishes an application "
                    "record, not available headroom. A hosting-capacity map may describe "
                    "a different voltage class or operating condition from the proposed "
                    "project. For storage, document charging load and discharging output "
                    "separately, including restrictions that could undermine dispatch "
                    "economics. For an AI campus, obtain the buyer's ramp schedule and "
                    "critical service requirements before asking about firm supply. "
                    "Use 18 CFR 35.28 to understand applicable transmission-provider "
                    "interconnection obligations, while checking the actual tariff and "
                    "jurisdiction; generator procedures do not automatically supply "
                    "a campus load-service commitment. Maintain three evidence levels: "
                    "inquiry submitted, preliminary utility response, and study-supported "
                    "service parameters. Only the final category supports modeled "
                    "deliverable MW, and even then quote the utility's conditions "
                    "and remaining contractual dependencies alongside the number."
                ),
                (
                    "P05 and P06 run in parallel because electrical progress cannot "
                    "repair unusable property rights or a prohibited land use. For "
                    "a Virginia search, check local authority under Va. Code "
                    "§ 15.2-2280 and obtain the current ordinance, parcel district, "
                    "use classification, application calendar, and any adopted "
                    "moratorium. A staff conversation is a lead, not an entitlement. "
                    "Record whether storage is treated as a utility facility, "
                    "industrial use, or another local category, and identify "
                    "setbacks, fire access, landscaping, noise, and equipment-height "
                    "requirements. Examine the usable pad after constraints, not "
                    "the assessor's gross acreage. Check mineral reservations, "
                    "surface-use rights, easements, road access, and restrictions "
                    "that could block foundations or utility corridors. Wetland "
                    "screening under Clean Water Act Section 404, 33 U.S.C. "
                    "§ 1344, identifies potential permitting work; database absence "
                    "does not resolve jurisdiction or authorize fill. Campus "
                    "water diligence must specify cooling architecture, source, "
                    "required volume, wastewater disposition, and provider response. "
                    "Do not charge a standalone BESS parcel for a campus-scale "
                    "water assumption, but do capture its actual fire-protection "
                    "and emergency-response requirements. Each unresolved item "
                    "gets a named resolver, price ceiling, and decision date."
                ),
                (
                    "By Day 14, classify six priority parcels against the actual "
                    "developer briefs and reduce them to no more than four "
                    "negotiation candidates. Use a downside residual rather than "
                    "a headline price per nearby megawatt. Start with the "
                    "developer's supported project value at the documented service "
                    "date; subtract land consideration, remaining development "
                    "spending, supported upgrade exposure, financing and delay "
                    "costs, and the developer's required return. The resulting "
                    "headroom limits an assignment fee; it is not itself booked "
                    "revenue. Where utility-supported MW or upgrade responsibility "
                    "is absent, leave capacity-derived valuation at zero and "
                    "negotiate only inexpensive contingent control. Stress the "
                    "buyer model using a twelve-month service delay and a "
                    "fifty-percent increase in the currently supported upgrade "
                    "estimate. These are internal stress assumptions, not "
                    "predictions of utility outcomes. Obtain buyer confirmation "
                    "that the stressed residual still supports the proposed "
                    "fee before increasing consideration. If no usable upgrade "
                    "estimate exists, the stress test remains incomplete and "
                    "the site cannot pass the capital-expansion test. Send "
                    "developers an evidence summary that distinguishes observed "
                    "facts, utility conditions, operator assumptions, and "
                    "questions still awaiting third-party resolution."
                ),
            ],
            "table": {
                "caption": "Days 8–14: Separate Service Evidence, Land-Use Authority, and Downside Valuation",
                "headers": [
                    "Execution day and mapped play",
                    "Accountable pod member and concrete action",
                    "Required deliverable and evidence trail",
                    "Quantitative acceptance threshold or spending constraint",
                ],
                "rows": [
                    [
                        "Day 8 advances P07 utility service qualification",
                        "Electrical contractor submits authorized inquiries through the utility's designated channel",
                        "Six parcel inquiries specify load, export, voltage, location, and timing",
                        "Record submission receipts without presenting them as available capacity",
                    ],
                    [
                        "Day 9 reconciles P03 queue and P07 service evidence",
                        "Electrical contractor identifies tariff applicability and competing-request dependencies",
                        "Service-status sheet separates preliminary comments from study-supported parameters",
                        "Allow no capacity-derived valuation without utility-supported deliverability assumptions",
                    ],
                    [
                        "Day 10 resolves P06 local zoning questions",
                        "Property-rights contractor obtains ordinances and written planning interpretations where available",
                        "Six parcel records identify use classification, restrictions, and application sequence",
                        "Remove parcels subject to an effective incompatible-use moratorium",
                    ],
                    [
                        "Day 11 deepens P05 usable-area and rights screening",
                        "GIS and property-rights contractors reconcile constraints against proposed site layouts",
                        "Constraint maps distinguish gross acreage from usable pads and access corridors",
                        "Storage candidates retain a buyer-compatible footprint within 5–25-acre parcels",
                    ],
                    [
                        "Day 12 verifies P08 campus infrastructure dependencies",
                        "Principal requests fiber routes and cooling-specific water service responses",
                        "Campus files identify construction responsibility and any shared fiber-route dependency",
                        "Do not merge campus infrastructure requirements into standalone storage economics",
                    ],
                    [
                        "Day 13 connects P01 buyer economics with P11 pricing",
                        "Principal asks developers to evaluate evidence-linked downside residual models",
                        "Models disclose utility assumptions, upgrade exposure, timing, and required developer returns",
                        "Stress supported upgrades by fifty percent and timing by twelve months",
                    ],
                    [
                        "Day 14 selects the P09 option negotiation shortlist",
                        "Principal ranks survivors using buyer fit and unresolved diligence cost",
                        "No more than four candidate files enter documented owner negotiations",
                        "Unstudied power supports contingent control only, never a deliverable-MW premium",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Verifications Before Any Nonrefundable Site Payment",
                "body": "The principal signs these checks for each parcel; failure pauses payment even when the broader sprint remains on schedule.",
                "items": [
                    "Verify the option grantor's authority, the exact legal description, and the access rights needed to conduct the proposed diligence.",
                    "Verify the utility evidence label, keeping preliminary discussion separate from study-supported MW, cost allocation, and energization conditions.",
                    "Verify current zoning, moratorium status, and the buyer-compatible usable footprint; document unresolved permit work and its funded next step.",
                    "Verify principal or licensed-broker capacity, assignment language, termination rights, notice dates, and the remaining $2,000 aggregate option-payment allowance.",
                ],
            },
        },
        {
            "heading": "3. Days 15–21: Purchase Conditional Control and Build an Assignable Evidence Pack",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "P09 aims for two executed, diligence-contingent options, not "
                    "maximum acreage under expensive paper. Seek twelve to "
                    "twenty-four months of contractual control, with negotiated "
                    "termination rights tied to utility feasibility, zoning, "
                    "title, access, and buyer-defined physical requirements. "
                    "That duration is a target, not an assumption that owners "
                    "will accept cheap long-term exclusivity. If an owner "
                    "requires consideration beyond the sprint allocation, "
                    "negotiate staged extensions, obtain developer funding, "
                    "or stop. Specify permitted assignees, assignment notice, "
                    "any owner consent, diligence access, cooperation with "
                    "utility requests, and treatment of studies after "
                    "termination. Have counsel determine whether recording "
                    "a memorandum is appropriate and authorized; avoid "
                    "publishing commercial terms unnecessarily. Validate "
                    "the principal-trading structure against applicable "
                    "state licensing rules. Va. Code § 54.1-2100 defines "
                    "broker activity, while § 54.1-2103 addresses specified "
                    "exemptions; neither should be reduced to a universal "
                    "claim that calling compensation an assignment fee "
                    "eliminates licensing requirements. Where the activity "
                    "requires brokerage licensure, use a properly licensed "
                    "participant under a documented arrangement. Never "
                    "market another owner's parcel as though the pod "
                    "already controls it. Log execution, effective dates, "
                    "payment receipts, and every termination notice deadline."
                ),
                (
                    "Keep the workload inside the one-FT-plus-three-contractor "
                    "pod by enforcing work-in-process limits. The principal "
                    "handles at most four active owner negotiations and "
                    "three substantive developer conversations per week. "
                    "The electrical contractor carries no more than six "
                    "live utility inquiries; the GIS contractor updates "
                    "only the twelve survivors; the property-rights "
                    "contractor prepares no more than two executable "
                    "option packages during this sprint. Batch factual "
                    "questions daily and hold one thirty-minute exception "
                    "meeting twice weekly. Automated reminders can track "
                    "utility response dates, owner commitments, and option "
                    "notices, but do not automate interpretations of "
                    "capacity or legal rights. P10 should produce a "
                    "versioned evidence pack containing the legal description, "
                    "control instrument, rights exceptions, constraint map, "
                    "zoning pathway, utility correspondence, study status, "
                    "buyer infrastructure requirements, and financial "
                    "assumptions. Redact personal contact details and "
                    "share proprietary studies only with appropriate "
                    "rights and recipient restrictions. Maintain a "
                    "change log identifying what changed, its source, "
                    "and which prior claims became stale. If a restudy "
                    "or municipal action changes feasibility, withdraw "
                    "the affected pricing sheet immediately and notify "
                    "every developer who received it before negotiating further."
                ),
                (
                    "P11 separates executable economics from attractive "
                    "but unearned deal value. An option assignment "
                    "earns operator revenue only under the applicable "
                    "contract and accounting treatment; a per-MW "
                    "milestone must identify the verified capacity "
                    "basis, triggering event, payer, and payment "
                    "date. Development carry remains outside realized "
                    "revenue until the relevant entitlement and "
                    "recognition conditions are satisfied. Do not "
                    "count land purchase price, battery procurement, "
                    "campus construction spending, customer electricity "
                    "purchases, or underlying project value as "
                    "origination revenue. Review principal-versus-agent "
                    "presentation under ASC 606 if the operator "
                    "collects money on another party's behalf; "
                    "pass-through collections do not become operator "
                    "revenue simply by crossing its bank account. "
                    "For each proposed transaction, maintain separate "
                    "columns for contract face amount, recognition "
                    "status, cash received, third-party obligations, "
                    "and remaining collection risk. Give buyers "
                    "an itemized transfer schedule rather than "
                    "a single opaque premium. Where future "
                    "upgrade costs remain unresolved, use conditional "
                    "pricing or buyer-funded study milestones "
                    "instead of manufacturing certainty. The "
                    "first thirty days should create defensible "
                    "control and a collection pathway; the "
                    "canonical two-to-six-month first-deal window "
                    "makes a Day-30 cash receipt possible but unnecessary."
                ),
            ],
            "table": {
                "caption": "Days 15–21: Contingent Option Execution, Controlled Workload, and Buyer Transfer Readiness",
                "headers": [
                    "Execution day and mapped play",
                    "Accountable pod member and concrete action",
                    "Required deliverable and evidence trail",
                    "Quantitative acceptance threshold or spending constraint",
                ],
                "rows": [
                    [
                        "Day 15 converts P09 diligence findings into owner terms",
                        "Principal proposes contingent control while property-rights contractor checks transaction structure",
                        "Term sheets identify duration, consideration, assignment, access, and termination mechanics",
                        "Target twelve to twenty-four months without exceeding funded payment limits",
                    ],
                    [
                        "Day 16 verifies P04 ownership before P09 execution",
                        "Property-rights contractor checks signing authority and recorded rights affecting development",
                        "Written exceptions list addresses easements, minerals, access, and legal description",
                        "Resolve every exception that would defeat the proposed diligence access",
                    ],
                    [
                        "Day 17 links P07 milestones to P09 option protections",
                        "Electrical and property-rights contractors align study events with extension mechanics",
                        "Draft clauses identify utility cooperation and capped event-based extension payments",
                        "Reject automatic fee escalation beyond the approved aggregate option allowance",
                    ],
                    [
                        "Day 18 executes the strongest P09 control opportunity",
                        "Principal signs only after parcel-specific verification checks are complete",
                        "Executed option and payment receipt enter the controlled evidence register",
                        "Keep cumulative option consideration within the total $2,000 sprint allocation",
                    ],
                    [
                        "Day 19 assembles P10 developer diligence materials",
                        "GIS contractor and principal compile dated exhibits with explicit evidence labels",
                        "Versioned pack distinguishes property rights, utility status, assumptions, and unresolved issues",
                        "Every external capacity statement reproduces its utility conditions and source date",
                    ],
                    [
                        "Day 20 advances P10 distribution and P11 commercial terms",
                        "Principal shares authorized materials with selected developers and records substantive feedback",
                        "Buyer response log captures fee structure, remaining diligence, and decision authority",
                        "Target two documented buyer responses rather than counting email opens",
                    ],
                    [
                        "Day 21 completes P09 control and P11 transfer mechanics",
                        "Principal executes a second suitable option or records its specific blocker",
                        "Transfer schedule separates assignment consideration, milestone payments, and contingent carry",
                        "Limit active executed options to two until Day-30 evidence review",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the current evidence version",
                    "action": "Export the parcel register and preserve the underlying utility, title, and zoning documents.",
                    "detail": "Assign a version date and identify every capacity statement that depends on a pending study or contract.",
                },
                {
                    "step": 2,
                    "title": "Reconcile rights and cash before signing",
                    "action": "Confirm grantor authority, assignability, termination notices, and total committed consideration.",
                    "detail": "Include unpaid contractual commitments in the $7,500 sprint ceiling and preserve the $17,500 launch reserve.",
                },
                {
                    "step": 3,
                    "title": "Transfer evidence without overstating readiness",
                    "action": "Send an authorized buyer pack separating storage import/export questions from campus load-service dependencies.",
                    "detail": "Document recipients, sharing rights, utility conditions, upgrade exposure, and the exact milestones proposed for payment.",
                },
                {
                    "step": 4,
                    "title": "Close the loop on each buyer objection",
                    "action": "Assign one resolver, one cost ceiling, and one decision date to every material objection.",
                    "detail": "Withdraw stale pricing immediately after adverse utility, title, or municipal evidence and preserve the correction record.",
                },
            ],
        },
        {
            "heading": "4. Days 22–30 and Beyond: Reconcile Cash, Then Apply Kill / Fix / Scale Thresholds",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The final nine days test whether the pod has "
                    "created evidence that a developer will actually "
                    "underwrite. Days 22–24 close buyer questions and "
                    "repeat the upgrade-and-delay stress test wherever "
                    "the utility evidence supports it. Days 25–27 "
                    "reconcile consideration, contractor commitments, "
                    "and termination dates, then obtain written "
                    "developer feedback on next actions. Days "
                    "28–30 produce a signed decision memo "
                    "for each controlled parcel and the pod "
                    "as a whole. Kill means stop new "
                    "spending and exercise available termination "
                    "rights when justified; it does not "
                    "mean abandon contractual duties. Fix means "
                    "one bounded remediation cycle with a "
                    "named resolver, a deadline within fourteen "
                    "days, and no more than $1,000 of "
                    "previously uncommitted diligence spending. Scale "
                    "at Day 30 means authorize another "
                    "controlled diligence cycle, not hire a "
                    "second employee or accumulate paid options. "
                    "The evidence thresholds below are internal "
                    "management rules, not universal conversion "
                    "benchmarks. An unanswered utility inquiry "
                    "can justify a bounded pause within "
                    "the two-to-six-month sales cycle, but "
                    "cannot justify a rising capacity valuation. "
                    "A confirmed fatal flaw overrides every "
                    "positive funnel count and every optimistic buyer conversation."
                ),
                (
                    "Reconcile the annual scorecard before interpreting "
                    "a promising pipeline. Conservative revenue is "
                    "$110,000, with $77,000 total costs and "
                    "$33,000 owner net profit at 30%. "
                    "Base revenue is $505,000, with $292,900 "
                    "costs and $212,100 profit at 42.0%. "
                    "Scaled revenue is $900,000, with $414,000 "
                    "costs and $486,000 profit at 54%. "
                    "Conservative and Base use one FT "
                    "plus three contractors; Scaled uses two "
                    "FT plus four contractors, six people "
                    "total. Illustrative revenue bridges are "
                    "two $40,000 assignments plus $30,000 "
                    "milestones for Conservative; five $75,000 "
                    "assignments, $100,000 milestones, and $30,000 "
                    "realized carry for Base; and eight "
                    "$85,000 assignments, $160,000 milestones, "
                    "and $60,000 realized carry for Scaled. "
                    "These bridges reconcile the supplied totals "
                    "without claiming those fee sizes are "
                    "market quotations. Annual costs include "
                    "failed options, specialist work, transaction "
                    "expense, and other operating costs; "
                    "the $1,800–$11,000 monthly operating "
                    "range is not the entire annual "
                    "cost base. Treat the sprint's possible "
                    "$2,000 expired-option loss as part "
                    "of those costs when incurred, not "
                    "an extra deduction from the canonical "
                    "profit. Maintain separate realized results "
                    "and scenario forecasts so pipeline "
                    "enthusiasm never changes recognized operator revenue."
                ),
                (
                    "Apply the decision hierarchy consistently: a "
                    "hard failure triggers Kill first; "
                    "Scale requires every listed condition; "
                    "all other viable cases enter Fix "
                    "only if the remediation budget and "
                    "deadline are credible. Day 60 requires "
                    "documented utility study progress, two "
                    "controlled viable sites, and a developer "
                    "term sheet before expanding option "
                    "exposure. Day 90 requires one "
                    "executed developer agreement, a documented "
                    "payment trigger, and study-supported "
                    "parameters for any capacity-based "
                    "pricing. Continuing utility delay can "
                    "remain Fix when buyers support "
                    "the revised timetable and fund "
                    "the incremental work; otherwise "
                    "freeze expansion. Preserve a cash "
                    "floor equal to three months "
                    "of committed operating expense "
                    "plus unavoidable site obligations. "
                    "At the illustrative $4,500 "
                    "monthly operating level, that "
                    "floor starts at $13,500 "
                    "before site obligations. Without "
                    "new receipts, another $4,500 "
                    "month reduces the initial "
                    "$17,500 reserve to $13,000, "
                    "so the pod must cut "
                    "commitments or secure funding "
                    "before authorizing that month. "
                    "Developer deposits count as "
                    "available cash only to the "
                    "extent contracts permit their "
                    "use after associated obligations. "
                    "Move toward the six-person "
                    "Scaled configuration only when "
                    "collected fees and contracted "
                    "work support the added "
                    "fixed cost without consuming this reserve."
                ),
            ],
            "table": {
                "caption": "Days 22–30 Execution and Day-30/60/90 Kill / Fix / Scale Decision Matrix",
                "headers": [
                    "Execution day or decision checkpoint",
                    "Required action or Kill threshold",
                    "Evidence deliverable or Fix threshold",
                    "Acceptance requirement or Scale threshold",
                ],
                "rows": [
                    [
                        "Day 22 reopens P10 buyer diligence questions",
                        "Principal requests ranked objections from each engaged developer decision-maker",
                        "Objection log identifies technical, commercial, and property-rights blockers separately",
                        "Every material objection receives an owner and dated next action",
                    ],
                    [
                        "Day 23 updates P07 utility evidence",
                        "Electrical contractor follows the designated channel without creating duplicate requests",
                        "Updated register preserves response dates, study prerequisites, and conditional language",
                        "Maintain zero unsupported claims of firm deliverable megawatts",
                    ],
                    [
                        "Day 24 retests P11 downside transaction economics",
                        "Principal reruns supported upgrade estimates and realistic energization-date sensitivities",
                        "Buyer model shows twelve-month delay and fifty-percent upgrade-cost stress",
                        "Increase consideration only when supported stressed residual covers the proposed fee",
                    ],
                    [
                        "Day 25 audits P09 consideration and termination exposure",
                        "Property-rights contractor verifies notices, payment obligations, and remaining option duration",
                        "Calendar highlights every contractual action falling within the next sixty days",
                        "Identify zero missed notices and no unbudgeted automatic extensions",
                    ],
                    [
                        "Day 26 reconciles cash across all eleven plays",
                        "Principal matches bank payments, unpaid commitments, and refundable deposits",
                        "Cash report distinguishes the $7,500 sprint allocation from the remaining reserve",
                        "Preserve at least $17,500 after full first-month committed deployment",
                    ],
                    [
                        "Day 27 advances P10 feedback into P11 commitments",
                        "Principal requests written commercial next steps from interested developer counterparties",
                        "Response records identify decision authority, diligence conditions, and proposed payment events",
                        "Count at least two substantive written responses toward Day-30 expansion readiness",
                    ],
                    [
                        "Day 28 prepares parcel-level Kill or Fix recommendations",
                        "Pod reviews utility, zoning, title, and infrastructure changes since initial screening",
                        "Decision memo assigns one status and evidence-linked rationale to each option",
                        "Any confirmed incurable fatal flaw stops additional parcel spending",
                    ],
                    [
                        "Day 29 prices the next bounded work cycle",
                        "Principal obtains fixed-scope remediation quotes and recalculates the cash floor",
                        "Forward budget includes operating commitments and unavoidable site payments",
                        "Approve no cycle that breaches three months of committed operating reserve",
                    ],
                    [
                        "Day 30 signs the pod investment decision",
                        "Principal applies the hierarchy and sends required contractual notices promptly",
                        "Signed memo distinguishes site termination, bounded remediation, and evidence-led expansion",
                        "Do not increase headcount merely because initial screening targets were achieved",
                    ],
                    [
                        "Day 30 applies first-month Kill / Fix / Scale thresholds",
                        "Kill expansion upon spend above $7,500, reserve below $17,500, or zero viable sites; terminate fatal-flaw sites",
                        "Fix remaining viable gaps within fourteen days and $1,000; fund the cycle without breaching the forward cash floor",
                        "Scale diligence only with two contingent options, two written buyer responses, one utility-authored scoping response, and a funded forward cash floor",
                    ],
                    [
                        "Day 60 applies second-cycle Kill / Fix / Scale thresholds",
                        "Kill new commitments when cash falls below three-month operating reserve plus unavoidable obligations, or every controlled site has a fatal flaw",
                        "Fix missing study progress or buyer terms within fourteen days and $1,000; otherwise pause expansion without claiming service certainty",
                        "Scale site exposure only with two viable options, one scoped study accepted into the utility process, one developer term sheet, and preserved cash floor",
                    ],
                    [
                        "Day 90 applies monetization Kill / Fix / Scale thresholds",
                        "Kill unfunded expansion after missed remediation deadlines, negative supported downside residual, or breach of the recalculated cash floor",
                        "Fix collection timing or study delays only with written buyer support, funded incremental work, and a fourteen-day reassessment date",
                        "Scale transaction throughput only with one executed developer agreement, explicit payment trigger, supported capacity pricing, positive stressed residual, and preserved cash floor",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Option the land cheaply, document the power precisely, and scale only the evidence your cash can carry.",
    "diagram_id": "diag-08",
    "action_checklist": [
        "Open a $25,000 launch ledger with a $7,500 first-month deployment ceiling, a $2,000 maximum option-loss allocation, and a $17,500 remaining reserve.",
        "Assign P01–P11 across one full-time principal and three scoped contractors, limiting the search to two jurisdictions inside one utility territory.",
        "Screen forty parcels into twelve survivors, separating 5–25-acre standalone BESS sites from buyer-specific AI campus requirements.",
        "Submit six authorized utility inquiries and preserve separate evidence fields for import, export, study status, upgrade exposure, and energization conditions.",
        "Negotiate at most two contingent assignable options, verify the transaction's licensing structure, and calendar every payment and termination deadline.",
        "Sign Day-30/60/90 decisions using the stated hierarchy, downside residual tests, buyer evidence, and a three-month committed-operating-cash floor.",
    ],
    "statutory_citations": [
        {
            "title": "18 CFR § 35.28 — Non-discriminatory open access transmission tariff",
            "url": "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
            "relevance": (
                "Provides the federal tariff framework relevant to covered transmission providers "
                "and interconnection procedures. Determine jurisdiction and actual tariff applicability; "
                "generation interconnection evidence does not establish campus load-service availability."
            ),
        },
        {
            "title": "33 U.S.C. § 1344 — Permits for dredged or fill material",
            "url": "https://www.law.cornell.edu/uscode/text/33/1344",
            "relevance": (
                "Supports early evaluation of potential dredge-and-fill permitting exposure. "
                "Wetland maps are screening evidence, while jurisdiction, proposed impacts, "
                "and the applicable authorization pathway require project-specific assessment."
            ),
        },
        {
            "title": "Va. Code § 15.2-2280 — Zoning ordinances generally",
            "url": "https://law.lis.virginia.gov/vacode/title15.2/chapter22/section15.2-2280/",
            "relevance": (
                "Establishes local zoning authority relevant to the illustrative Virginia search. "
                "Obtain the current local ordinance, parcel district, use classification, "
                "and restrictions before spending on site control."
            ),
        },
        {
            "title": "Va. Code § 54.1-2100 — Real estate broker and salesperson definitions",
            "url": "https://law.lis.virginia.gov/vacode/title54.1/chapter21/section54.1-2100/",
            "relevance": (
                "Defines regulated real-estate activities relevant to compensated parcel sourcing "
                "and transaction negotiation. Evaluate actual conduct rather than assuming "
                "an assignment-fee label settles licensing treatment."
            ),
        },
        {
            "title": "Va. Code § 54.1-2103 — Exemptions from chapter",
            "url": "https://law.lis.virginia.gov/vacode/title54.1/chapter21/section54.1-2103/",
            "relevance": (
                "Identifies specified exemptions that must be evaluated against the actual "
                "ownership interest and transaction structure. Use licensed brokerage participation "
                "where the proposed conduct requires it."
            ),
        },
    ],
}
