from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in government contract brokering, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "SAM.gov Bid-Desk Controls, FAR Fee Restrictions, Supplier Defaults, Lifeline Recoveries & Cash-Exposure Circuit Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #4, Government Contract Brokering, ranks #27 with a 79/100 "
        "Money-to-Manpower Score: a High-Leverage Operator Play, not effortless "
        "procurement arbitrage. Seven chapter-mapped plays anchor this teardown: "
        "federal bid-desk retainers, municipal solicitation monitoring, prime/sub "
        "teaming support, fixed-fee proposal production, subcontract administration, "
        "invoice-evidence operations, and white-label MVNO/Lifeline aggregation. "
        "The canonical annual owner-profit cases are $18,000 Conservative, "
        "$126,000 Base, and $300,000 Scaled, against recognized service revenue "
        "of $120,000, $560,000, and $1,000,000. Award face values and carrier "
        "subsidies do not become broker revenue. The chapter converts common "
        "failure mechanisms into evidence tests, loss limits, and stop-work "
        "triggers. The question's 80% framing is not an observed failure rate; "
        "the operating controls stand without that unsupported statistic."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual recognized service fees, excluding client contract value",
            "note": "15% net margin; $18,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$560,000",
            "context": "Annual recognized service fees, excluding client contract value",
            "note": "22.5% net margin; $126,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual recognized service fees, excluding client contract value",
            "note": "30% net margin; $300,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Separate Paid Procurement Work from Influence Selling",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is selling access instead of a measurable "
                    "service. A federal bid desk can research public solicitations, "
                    "maintain calendars, draft responses, and document supplier "
                    "qualifications; it cannot promise an award through personal "
                    "influence. FAR Subpart 3.4 and the solicitation's applicable "
                    "FAR 52.203-5 clause govern contingent-fee arrangements, including "
                    "the bona fide employee or agency exception. Do not assume that "
                    "calling a percentage payment consulting makes the exception "
                    "available. A prohibited arrangement can expose the contractor "
                    "to annulment or recovery of the fee. The second trap is treating "
                    "a teaming introduction as an unrestricted referral business: "
                    "41 U.S.C. chapter 87 addresses kickbacks connected with federal "
                    "prime contracts and subcontracts. The third is accepting "
                    "nonpublic competitor pricing or source-selection material; "
                    "41 U.S.C. 2102 reaches prohibited disclosure and knowing "
                    "receipt before award. Require a written scope, a documented "
                    "fee rationale, and a source log for every sensitive attachment. "
                    "Quarantine unsolicited restricted material, stop its circulation, "
                    "preserve the message, and route it to designated counsel and "
                    "the responsible contracting channel. Never delete evidence "
                    "to make a bid file look clean."
                ),
                (
                    "Map the first four operating plays to delivered units, not "
                    "award percentages. Federal bid-desk retainers might charge "
                    "$1,500 monthly for twelve staff hours at $60 plus $180 "
                    "of allocated tooling, leaving $600 contribution before "
                    "central overhead. Municipal solicitation monitoring might "
                    "charge $600 for four hours at $60 plus $60 of portal "
                    "and alert administration, leaving $300. Prime/sub teaming "
                    "support might charge $2,000 for twenty hours at $60 plus "
                    "$300 of documented diligence, leaving $500. Fixed-fee proposal "
                    "production might charge $10,000 against $6,000 direct labor "
                    "and $1,000 specialist review, leaving $3,000. These are "
                    "illustrative service packages, not additional scorecard "
                    "revenue or official catalog identifiers. The fallbacks are "
                    "equally specific: cap monitored jurisdictions, require written "
                    "client qualification before introductions, and reduce proposal "
                    "scope when amendments expand the workload. Make payments "
                    "depend on accepted deliverables rather than an award unless "
                    "the actual arrangement has been reviewed under applicable "
                    "restrictions. A fixed fee does not cure influence selling, "
                    "kickbacks, organizational conflicts, or misuse of protected "
                    "information. Price revision cycles and submission support "
                    "explicitly; unlimited revisions quietly turn attractive "
                    "contribution into unpaid overtime."
                ),
                (
                    "The fourth trap is impersonating the client in SAM.gov or a "
                    "municipal portal. Use authorized roles, individual credentials, "
                    "and multifactor authentication; never collect a principal's "
                    "password to accelerate registration. SAM.gov registration and "
                    "the Unique Entity ID are free, although a separately disclosed "
                    "assistance service can carry a fee. The fifth trap is treating "
                    "an active registration as proof of size, ownership, licensing, "
                    "or performance capability. Verify the solicitation's actual "
                    "representations and the responsible client's supporting "
                    "records. The sixth is submitting through a borrowed identity "
                    "after an access restriction. That can convert an administrative "
                    "problem into a false representation or security incident. "
                    "Record portal receipts, amendment acknowledgments, and the "
                    "controlling deadline with its time zone. FAR 52.215-1 contains "
                    "specific late-proposal rules when included; a successful upload "
                    "to the wrong workspace does not establish timely receipt. "
                    "Municipal procurement codes and portal instructions require "
                    "separate review rather than automatic transplantation of FAR "
                    "rules. Treat unexplained role changes, a rejected receipt, or "
                    "one missing mandatory acknowledgment as a submission stop. "
                    "Platform access restrictions and government suspension or "
                    "debarment are different processes; neither should be described "
                    "as an automatic permanent ban."
                ),
            ],
            "table": {
                "caption": "Federal and Municipal Entry Traps: Evidence Before Submission",
                "headers": [
                    "Failure mechanism",
                    "Required evidence",
                    "Early warning trigger",
                    "Operator circuit breaker",
                ],
                "rows": [
                    [
                        "Award-linked commissions disguised as ordinary procurement consulting fees",
                        "Written fee analysis addressing the applicable contingent-fee restrictions",
                        "Any payment term depends solely on winning government business",
                        "Replace unsupported fee structures before accepting the client engagement",
                    ],
                    [
                        "Supplier referral payments rewarding improper influence over subcontract selection",
                        "Documented service purpose and independent review of compensation recipients",
                        "Any undisclosed side payment appears in the supplier relationship",
                        "Suspend introductions and preserve payment records for immediate review",
                    ],
                    [
                        "Competitor bid material entering the proposal team's shared workspace",
                        "Source register identifying public origin and permitted document access",
                        "Any attachment contains restricted markings or unexplained competitor pricing",
                        "Quarantine the attachment and stop circulation without destroying evidence",
                    ],
                    [
                        "Shared portal credentials masking the actual authorized submission actor",
                        "Named user roles and written authorization from the client principal",
                        "One login requires another person's password or authentication code",
                        "Request authorized delegation and pause submissions until access works",
                    ],
                    [
                        "Registration status mistaken for verified eligibility on restricted competitions",
                        "Current ownership records and solicitation-specific representation support from clients",
                        "Client cannot substantiate one material size or ownership representation",
                        "Remove the opportunity until the responsible client resolves eligibility",
                    ],
                    [
                        "Late uploads and missed amendments invalidating otherwise competitive proposals",
                        "Portal receipt and acknowledgment checklist matched to controlling solicitation",
                        "Submission rehearsal fails or mandatory amendment acknowledgment remains missing",
                        "Escalate before deadline and retain the complete submission evidence",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before Any Client Submission",
                "body": (
                    "Submission authority, fee structure, eligibility evidence, and "
                    "receipt readiness must all be documented for the actual opportunity."
                ),
                "items": [
                    "Match the client's authorized portal role to the person submitting; test multifactor access without sharing credentials.",
                    "Review the compensation agreement against FAR Subpart 3.4, applicable clauses, and jurisdiction-specific restrictions.",
                    "Obtain client-approved support for material representations, subcontract structure, and any claimed set-aside eligibility.",
                    "Rehearse the upload, confirm every amendment, and assign one person to capture the final timestamped receipt.",
                ],
            },
        },
        {
            "heading": "2. Stop Pass-Through Structures and Supplier Defects Before They Become Debt",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The seventh trap is building a nominal prime that contributes "
                    "little beyond an invoice. FAR 52.215-23, when applicable, "
                    "addresses excessive pass-through charges; its subcontracting "
                    "threshold is a disclosure and analysis issue, not a universal "
                    "ban on subcontracting. Separately, FAR 52.219-14 and 13 CFR "
                    "125.6 impose category-specific limitations on covered small "
                    "business set-asides. For covered service contracts, the "
                    "restriction generally limits payments to subcontractors that "
                    "are not similarly situated entities to 50% of the amount "
                    "paid by the government, subject to the rule's details and "
                    "exclusions. Supplies and construction have different tests. "
                    "Do not substitute headcount, gross margin, or a teammate's "
                    "marketing claim for the governing calculation. The eighth "
                    "trap is ostensible-subcontractor affiliation under 13 CFR "
                    "121.103: an otherwise eligible small prime can lose eligibility "
                    "through an impermissible reliance structure. Map primary and "
                    "vital work, management control, relevant experience, and actual "
                    "execution responsibilities before pricing. If the structure "
                    "fails, move to a permissible support role or decline the "
                    "opportunity. Adding a nominal project manager after submission "
                    "does not retroactively repair inaccurate representations "
                    "or an unsupported performance plan."
                ),
                (
                    "The ninth trap is quoting supplier promises as if they were "
                    "binding capacity. A distributor's email is not a reserved "
                    "production slot, an authorized substitution, or evidence of "
                    "domestic-origin conformity. Build a requirement-to-evidence "
                    "matrix covering delivery dates, inspection, packaging, "
                    "origin clauses, cybersecurity terms, and required flowdowns. "
                    "Buy American and trade-agreement clauses do not apply "
                    "identically to every purchase; read the clauses actually "
                    "incorporated. For a $200,000 client supply award, a $12,000 "
                    "broker service fee remains $12,000 of potential operator "
                    "revenue, not $200,000. If the operator guarantees supplier "
                    "performance and must fund $20,000 of emergency replacement "
                    "cost, the exposure exceeds that fee before ordinary labor "
                    "costs. Do not accept that mismatch through casual indemnity "
                    "language. Require verified lead times, inspection rights, "
                    "written substitution procedures, and an allocated remedy "
                    "for each material defect. A second qualified supplier is "
                    "useful only when switching is contractually permitted and "
                    "the replacement meets the same specifications. If neither "
                    "condition holds, the fallback is to stop quoting the item "
                    "and alert the prime, not quietly ship a near-match. "
                    "Record supplier exceptions before the client commits."
                ),
                (
                    "The fifth mapped play, subcontract administration, can charge "
                    "$1,000 monthly for eight hours at $60 plus $120 of "
                    "document control, leaving $400 contribution before overhead. "
                    "Its fallback is a capped exception queue and a written "
                    "handoff to the prime for unresolved technical decisions. "
                    "The sixth, invoice-evidence operations, can charge $500 per "
                    "accepted invoice packet against four hours at $60 and $60 "
                    "of review, leaving $200. Its fallback is paid remediation "
                    "of missing acceptance records, not submission of unsupported "
                    "quantities. The tenth trap is confusing administrative "
                    "assistance with authority to certify delivery, change scope, "
                    "or bind the government. Only appropriately authorized "
                    "officials can make those commitments. FAR 32.905 links "
                    "payment processing to a proper invoice and applicable "
                    "acceptance requirements; an invoice number alone starts "
                    "no reliable cash forecast. Track evidence from delivery "
                    "through acceptance, invoice receipt, rejection, correction, "
                    "and payment. A client contract should state whether the "
                    "operator's service fee is independent of government "
                    "collection. Pay-when-paid language transfers delay exposure "
                    "to the desk; reject open-ended terms unless price, reserves, "
                    "and enforceable remedies support the exposure. Never "
                    "manufacture acceptance evidence to release a stuck receivable."
                ),
            ],
            "table": {
                "caption": "Teaming, Delivery, and Invoice Defects That Create Asymmetric Exposure",
                "headers": [
                    "Structural defect",
                    "Forensic calculation or evidence",
                    "Loss or recovery mechanism",
                    "Permissible operating fallback",
                ],
                "rows": [
                    [
                        "Nominal prime adding unsupported charges without meaningful performance value",
                        "Identify applicable pass-through clauses and document actual prime contribution",
                        "Government may disallow excessive charges under the applicable contract",
                        "Restructure actual responsibilities or decline unsupported intermediary pricing entirely",
                    ],
                    [
                        "Covered set-aside work exceeding permitted subcontracting payment limits",
                        "Calculate category-specific limits using qualifying payments and entity status",
                        "Nonconforming performance can create contractual remedies and eligibility consequences",
                        "Reduce restricted subcontracting before commitment and monitor actual payments",
                    ],
                    [
                        "Small prime unusually reliant on its proposed subcontractor's capabilities",
                        "Document primary work ownership and assess ostensible-subcontractor affiliation factors",
                        "Affiliation findings can undermine size eligibility for the procurement",
                        "Select a support structure consistent with genuine prime responsibility",
                    ],
                    [
                        "Unreserved supplier capacity supporting firm client delivery commitments",
                        "Obtain binding lead times and independently verify critical production capacity",
                        "Emergency replacement costs can exceed the entire operator service fee",
                        "Quote only supported delivery windows or withdraw the unsupported item",
                    ],
                    [
                        "Product substitutions bypassing origin requirements and written specification controls",
                        "Match replacement evidence to incorporated clauses and authorized change procedures",
                        "Rejected goods can trigger replacement expenses and delayed acceptance",
                        "Use qualified alternatives only after the required written authorization",
                    ],
                    [
                        "Invoice packets claiming acceptance without responsible official supporting evidence",
                        "Reconcile quantities and acceptance records before certifying invoice completeness",
                        "Rejected invoices delay collection while false records increase liability",
                        "Return incomplete packets for paid remediation without fabricating support",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Veteran Bid-Desk Tactics That Preserve Recoverable Margin",
                "body": (
                    "Experienced desks price evidence work and isolate responsibilities "
                    "before a delivery problem becomes an operator-funded rescue."
                ),
                "items": [
                    "Ask the prime for its clause matrix before quoting administration; price mandatory reporting and flowdowns as explicit work units.",
                    "Compare the supplier's promised ship date with the required acceptance date, including transit, inspection, and correction time.",
                    "Keep separate folders for public solicitation research, client-controlled representations, and government acceptance evidence.",
                    "Maintain a qualified replacement supplier file, but confirm substitution authority before treating that supplier as usable backup.",
                ],
            },
        },
        {
            "heading": "3. Treat Lifeline Aggregation as a Separate Recovery-Risk Business",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The seventh mapped play is "
                    "mvno_lifeline_acp_telecom_subsidy_aggregation: White-Label MVNO "
                    "& Federal/State Low-Income Telecom Subsidy Aggregation. Its "
                    "catalog identifier includes ACP, but ACP ended June 1, 2024; "
                    "do not model new ACP reimbursements or sell ACP enrollment "
                    "as a currently funded channel. Lifeline is a distinct program. "
                    "Federal support can reach $9.25 monthly for qualifying "
                    "service, with up to $25 additional support for eligible "
                    "residents of qualifying Tribal lands, producing $34.25 "
                    "before any separately validated state support. That is not "
                    "a universal $44 household payment. California LifeLine "
                    "has separate state requirements and support mechanics; "
                    "never add headline benefits without checking the approved "
                    "service, location, carrier status, and interaction rules. "
                    "An MVNO arrangement does not itself confer Eligible "
                    "Telecommunications Carrier status or authority to claim "
                    "Lifeline support. Determine which ETC holds the obligation, "
                    "which systems establish eligibility, and which entity "
                    "submits reimbursement claims. The eleventh trap is buying "
                    "enrollments before establishing that responsibility chain. "
                    "A master aggregator earns its contracted service fee; "
                    "carrier support receipts are not automatically the "
                    "aggregator's recognized revenue. Obtain the executed carrier "
                    "agreement before recruiting field agents."
                ),
                (
                    "The twelfth trap is selling hypothetical network economics "
                    "as an unlimited-service entitlement. At 1,000 valid subscriber "
                    "months, $9.25 support produces $9,250 of carrier support. "
                    "Assumed $3 wholesale network cost produces $3,000 of network "
                    "expense and a $6,250 spread before devices, support staff, "
                    "taxes, eligibility work, usage costs, agent payments, "
                    "recoveries, and carrier overhead. The $2–$4 wholesale range "
                    "is an underwriting assumption requiring an actual tariff "
                    "or contract; unlimited data promises may destroy it. An "
                    "aggregator charging $2 per validated subscriber month "
                    "records $2,000 of service revenue on those same units, "
                    "not $9,250. If 100 units become ineligible for payment, "
                    "reversing $200 of aggregator fees reduces recognized "
                    "service revenue to $1,800; the ETC's associated $925 "
                    "support adjustment is separate unless indemnity terms "
                    "shift it. A $10,000 field campaign paying $10 for each "
                    "of 1,000 activations takes five valid months of $2 "
                    "fees merely to recover acquisition cash, ignoring all "
                    "other costs and attrition. The fallback is a small "
                    "verified cohort with capped acquisition exposure, "
                    "payment holdbacks, and carrier reconciliation before "
                    "national expansion. Do not fund hundreds of thousands "
                    "of speculative activations."
                ),
                (
                    "The thirteenth trap is treating a submitted household record "
                    "as durable eligibility. Apply 47 CFR 54.409, 54.410, "
                    "54.407, and 54.405 to eligibility, certification, support, "
                    "and de-enrollment responsibilities. Use the National "
                    "Verifier, National Lifeline Accountability Database, or "
                    "applicable state process as required for the carrier "
                    "and jurisdiction. Block duplicate households, fabricated "
                    "documents, agent-controlled identities, and unsupported "
                    "Tribal claims. These shortcuts can produce recoveries, "
                    "termination, program exclusion, or false-claims exposure; "
                    "fake traffic and forged usage records compound the harm. "
                    "For service subject to the nonusage rules, deploy "
                    "Day-20 SMS or IVR reminders, but distinguish reminders "
                    "from qualifying usage. A subscriber's response to direct "
                    "contact confirming continued service can qualify under "
                    "the rule when properly captured; a delivered message "
                    "alone does not. Follow the applicable 30-day nonusage "
                    "and subsequent 15-day notice process rather than "
                    "inventing immediate disconnection. Reverse field-agent "
                    "commissions for lines failing the contractual 30-day "
                    "usage test only through enforceable terms and applicable "
                    "worker-payment rules. That commercial reversal does "
                    "not replace the carrier's statutory process. Preserve "
                    "consented contact records, actual usage evidence, "
                    "exception decisions, and the linkage from subscriber "
                    "month to claim."
                ),
            ],
            "table": {
                "caption": "Lifeline Cohort Controls: Reimbursements, Usage Evidence, and Agent Recoveries",
                "headers": [
                    "Cohort failure mode",
                    "Evidence or unit economics",
                    "Internal intervention threshold",
                    "Containment and recovery action",
                ],
                "rows": [
                    [
                        "Legacy ACP language presented as a currently funded acquisition channel",
                        "Current program funding and carrier-approved offer documents establish eligibility",
                        "Any advertisement promises an active benefit from ended ACP funding",
                        "Stop the advertisement and replace it with verified program language",
                    ],
                    [
                        "Tribal and state support stacked without documented household qualification",
                        "Validate location and each support component against applicable program rules",
                        "Any subscriber month lacks evidence for one claimed support component",
                        "Exclude unsupported components and reconcile affected claims with the carrier",
                    ],
                    [
                        "Aggregator revenue inflated by recording the carrier's entire subsidy receipt",
                        "One thousand validated months at two dollars produce two thousand dollars",
                        "Ledger credits exceed the aggregator's earned contractual service fee",
                        "Correct revenue classification and separate carrier receipts from operator fees",
                    ],
                    [
                        "Acquisition commissions paid before usage and eligibility evidence become reliable",
                        "Ten dollar commissions require five valid two dollar fee months",
                        "Unreconciled agent exposure exceeds the written cohort acquisition budget",
                        "Pause recruitment and apply enforceable holdbacks before expanding enrollment",
                    ],
                    [
                        "Day twenty reminders mistaken for independently verified qualifying subscriber usage",
                        "Store actual qualifying usage or captured subscriber confirmation evidence",
                        "Any active line approaches thirty days without qualifying usage evidence",
                        "Run permitted outreach and follow the applicable notice sequence",
                    ],
                    [
                        "Duplicate or fabricated enrollments entering support and commission calculations",
                        "Reconcile eligibility decisions and household checks against carrier subscriber records",
                        "Any confirmed fabrication triggers immediate suspension of the implicated source",
                        "Preserve evidence and coordinate corrections without generating artificial usage",
                    ],
                ],
            },
        },
        {
            "heading": "4. Reconcile the Scorecard and Install Cash-Loss Circuit Breakers",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use the canonical scorecard as the annual control total. "
                    "Conservative recognized service revenue is $120,000, with "
                    "$102,000 implied total costs and $18,000 owner net "
                    "profit at 15%. Base is $560,000, $434,000 costs, and "
                    "$126,000 profit at 22.5%. Scaled is $1,000,000, "
                    "$700,000 costs, and $300,000 profit at 30%. "
                    "Illustrative revenue bridges are ten $1,000 monthly "
                    "retainers for Conservative; twenty $1,500 monthly "
                    "retainers plus twenty $10,000 accepted projects for "
                    "Base; and twenty-five $2,000 monthly retainers plus "
                    "forty $10,000 accepted projects for Scaled. These "
                    "bridges explain totals, not a promised customer mix "
                    "or extra revenue layered onto the seven plays. "
                    "The staffing labels remain 2 FT + 3 C for "
                    "Conservative and Base, and 3 FT + 4 C for "
                    "Scaled. Conservative costs leave little room for two "
                    "full-time salaries, contractor purchases, and overhead; "
                    "the scorecard alone does not establish a workable "
                    "compensation plan. Build role-level hours and loaded "
                    "rates before hiring. Do not silently treat unpaid "
                    "owner labor as free capacity or move payroll "
                    "outside the model to preserve its stated margin."
                ),
                (
                    "The fourteenth trap is confusing profitable bookings with "
                    "spendable cash. Startup capital of $20,000–$90,000 "
                    "and monthly operating expense of $5,000–$25,000 "
                    "produce only one month of runway at the "
                    "lowest-capital, highest-burn combination, versus thirty "
                    "months at the opposite extremes, before setup "
                    "spending or collections. First deals may take "
                    "3–12 months, so underwrite runway against a "
                    "dated sales pipeline rather than the best endpoint. "
                    "The monthly expense range is an operating "
                    "planning input, not a substitute for total "
                    "annual scorecard costs, which also must accommodate "
                    "delivery labor and other attributable expense. Use "
                    "a rolling thirteen-week cash forecast excluding "
                    "restricted cash and disputed receipts. At Base, "
                    "$434,000 annual costs average approximately $36,167 "
                    "monthly. Ninety days of that full-cost run rate "
                    "requires approximately $108,500 before incremental "
                    "recovery exposure. A $24,000 unrecoverable defect "
                    "cost reduces Base profit from $126,000 to "
                    "$102,000 and margin to approximately 18.21%, "
                    "assuming revenue is unchanged. That single "
                    "event consumes approximately 19.05% of planned "
                    "owner profit. Contract deposits, staged billing, "
                    "and bounded supplier liabilities matter more "
                    "than a dashboard showing impressive award "
                    "face values."
                ),
                (
                    "Instrument the desk around evidence age and exposure, "
                    "not vanity submission counts. Flag more than 10% "
                    "unbilled completed work, receivables beyond contractual "
                    "terms by fifteen days, or rework exceeding 10% "
                    "of delivery hours; these are internal starting "
                    "thresholds, not statutory standards. Require "
                    "opportunity-level contribution estimates before accepting "
                    "another amendment cycle. Measure buyer concentration "
                    "against collected service fees and pause incremental "
                    "unsecured exposure when one client exceeds 25% "
                    "without a specific reserve decision. Set a "
                    "zero-tolerance stop for unsupported material "
                    "certifications, fabricated records, or unexplained "
                    "restricted documents. False Claims Act exposure "
                    "under 31 U.S.C. 3729 can include treble "
                    "damages and adjusted civil penalties; small "
                    "service fees do not bound potential liability "
                    "for knowingly causing false claims. When an "
                    "exception hits, preserve originals, isolate "
                    "affected submissions, quantify the maximum "
                    "plausible loss, and assign corrective ownership. "
                    "Apply mandatory disclosure duties when their "
                    "actual contractual and regulatory conditions "
                    "are met; FAR 52.203-13 is not a "
                    "universal clause in every municipal engagement. "
                    "Restart only after the responsible person "
                    "verifies corrected evidence and revised cash "
                    "capacity. Automation should accelerate alerts "
                    "and reconciliations, never manufacture eligibility, "
                    "acceptance, or government authority."
                ),
            ],
            "table": {
                "caption": "Weekly Forensic Dashboard and Explicit Internal Stop Thresholds",
                "headers": [
                    "Metric and calculation",
                    "Internal warning threshold",
                    "Evidence reviewed by owner",
                    "Required operating response",
                ],
                "rows": [
                    [
                        "Unbilled completed work divided by total completed service value",
                        "More than ten percent remains unbilled after scheduled billing",
                        "Accepted deliverables matched against invoice drafts and client disputes",
                        "Resolve missing acceptance evidence before adding discretionary delivery work",
                    ],
                    [
                        "Days past the invoice's actual contractual payment due date",
                        "Any material invoice remains unpaid fifteen days beyond terms",
                        "Invoice receipt and rejection history alongside client collection correspondence",
                        "Escalate collections and cap further unsecured client service exposure",
                    ],
                    [
                        "Rework hours divided by total recorded client delivery hours",
                        "More than ten percent reflects preventable defects or uncontrolled revisions",
                        "Time entries classified by amendment changes and internal defects",
                        "Reprice expanded scope and correct the repeatable production defect",
                    ],
                    [
                        "Largest client's collected fees divided by total collected service fees",
                        "One client exceeds twenty five percent without an exposure reserve",
                        "Cash receipts ledger and outstanding commitments for that client",
                        "Require a reserve decision before increasing unsecured delivery commitments",
                    ],
                    [
                        "Unrestricted cash divided by forecast weekly unavoidable cash outflows",
                        "Runway falls below thirteen weeks after plausible recovery exposure",
                        "Rolling cash forecast including payroll and disputed supplier commitments",
                        "Freeze discretionary acquisition spending and negotiate bounded payment milestones",
                    ],
                    [
                        "Unsupported material certifications or suspected fabricated records discovered weekly",
                        "Any single substantiated exception triggers immediate workstream isolation",
                        "Original records and responsible signer's documented factual supporting basis",
                        "Preserve evidence and assess correction and applicable disclosure duties",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the affected commitment",
                    "action": "Pause the specific submission, enrollment source, supplier order, or invoice implicated by the exception.",
                    "detail": (
                        "Do not disable unrelated client work automatically. Preserve "
                        "original files, timestamps, approvals, and portal messages "
                        "with access limited to authorized reviewers."
                    ),
                },
                {
                    "step": 2,
                    "title": "Build the exposure ledger",
                    "action": "Separate earned service fees, client award value, carrier support, refunds, replacement costs, and contingent obligations.",
                    "detail": (
                        "Record best-supported and plausible adverse outcomes. "
                        "Show who owes each amount, when it could become payable, "
                        "and whether any reserve or insurance actually responds."
                    ),
                },
                {
                    "step": 3,
                    "title": "Correct through the responsible channel",
                    "action": "Assign the prime, ETC, client principal, or authorized contracting contact to the correction appropriate to their authority.",
                    "detail": (
                        "Use designated counsel for material misrepresentation or "
                        "disclosure questions. Do not silently edit submitted "
                        "evidence or create a replacement account to bypass restrictions."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile and authorize restart",
                    "action": "Verify corrected source evidence, revised unit economics, and sufficient unrestricted cash before resuming the affected work.",
                    "detail": (
                        "Document the accountable owner's restart decision, "
                        "reconcile resulting credits or recoveries, and add "
                        "a targeted control that detects the original failure."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "A procurement intermediary survives by controlling evidence and exposure, not by counting the government's dollars as their own.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Reconcile the three annual cases to recognized service fees, implied costs, exact margins, and the canonical staffing counts.",
        "Review every fee agreement for contingent-fee restrictions, kickback exposure, liability allocation, and an explicit service deliverable.",
        "Build an opportunity-specific clause and eligibility matrix covering subcontract limits, supplier evidence, amendments, and authorized portal roles.",
        "Validate each telecom cohort against current program funding, ETC responsibilities, qualifying usage evidence, and contracted commission-recovery terms.",
        "Launch a weekly dashboard for unbilled work, overdue invoices, rework hours, client concentration, runway, and unsupported representations.",
        "Rehearse the four-step exception SOP using one supplier default and one rejected subscriber cohort before accepting further exposure.",
    ],
    "statutory_citations": [
        {
            "title": "FAR Subpart 3.4 — Contingent Fees",
            "url": "https://www.acquisition.gov/far/subpart-3.4",
            "relevance": (
                "Defines the federal contingent-fee framework and bona fide "
                "agency considerations relevant to award-linked broker compensation."
            ),
        },
        {
            "title": "FAR 52.203-5 — Covenant Against Contingent Fees",
            "url": "https://www.acquisition.gov/far/52.203-5",
            "relevance": (
                "States the contractual covenant and remedies for prohibited "
                "contingent-fee arrangements when the clause applies."
            ),
        },
        {
            "title": "41 U.S.C. 2102 — Prohibitions on Disclosing and Obtaining Procurement Information",
            "url": "https://www.law.cornell.edu/uscode/text/41/2102",
            "relevance": (
                "Controls prohibited disclosure and knowing receipt of "
                "contractor bid, proposal, and source-selection information."
            ),
        },
        {
            "title": "41 U.S.C. 8702 — Prohibitions Relating to Kickbacks",
            "url": "https://www.law.cornell.edu/uscode/text/41/8702",
            "relevance": (
                "Addresses kickbacks connected with federal prime contracts "
                "and subcontracts, including improper compensation structures."
            ),
        },
        {
            "title": "FAR 52.215-23 — Limitations on Pass-Through Charges",
            "url": "https://www.acquisition.gov/far/52.215-23",
            "relevance": (
                "Provides the applicable contractual framework for excessive "
                "pass-through charges and required subcontracting notifications."
            ),
        },
        {
            "title": "13 CFR 125.6 — Limitations on Subcontracting",
            "url": "https://www.ecfr.gov/current/title-13/section-125.6",
            "relevance": (
                "Specifies category-dependent subcontracting limits and "
                "similarly situated entity treatment for covered contracts."
            ),
        },
        {
            "title": "13 CFR 121.103 — Affiliation",
            "url": "https://www.ecfr.gov/current/title-13/section-121.103",
            "relevance": (
                "Includes ostensible-subcontractor affiliation principles "
                "relevant to small-prime teaming structures."
            ),
        },
        {
            "title": "FAR 32.905 — Payment Documentation and Process",
            "url": "https://www.acquisition.gov/far/32.905",
            "relevance": (
                "Links federal payment processing to proper invoice "
                "documentation and applicable acceptance requirements."
            ),
        },
        {
            "title": "47 CFR 54.403 — Lifeline Support Amount",
            "url": "https://www.ecfr.gov/current/title-47/section-54.403",
            "relevance": (
                "Establishes federal Lifeline support amounts, including "
                "additional support for qualifying Tribal lands."
            ),
        },
        {
            "title": "47 CFR 54.407 — Reimbursement for Offering Lifeline",
            "url": "https://www.ecfr.gov/current/title-47/section-54.407",
            "relevance": (
                "Governs reimbursement and qualifying usage conditions "
                "relevant to subscriber-month validation and outreach evidence."
            ),
        },
        {
            "title": "47 CFR 54.405 — Carrier Obligation to Offer Lifeline",
            "url": "https://www.ecfr.gov/current/title-47/section-54.405",
            "relevance": (
                "Includes carrier responsibilities and de-enrollment "
                "procedures, including the applicable nonusage notice process."
            ),
        },
        {
            "title": "47 CFR 54.409 — Consumer Qualification for Lifeline",
            "url": "https://www.ecfr.gov/current/title-47/section-54.409",
            "relevance": (
                "Establishes consumer eligibility criteria that must "
                "support enrollment and household qualification decisions."
            ),
        },
        {
            "title": "47 CFR 54.410 — Subscriber Eligibility Determination and Certification",
            "url": "https://www.ecfr.gov/current/title-47/section-54.410",
            "relevance": (
                "Sets eligibility determination and certification "
                "requirements supporting valid subscriber records."
            ),
        },
        {
            "title": "31 U.S.C. 3729 — False Claims",
            "url": "https://www.law.cornell.edu/uscode/text/31/3729",
            "relevance": (
                "Addresses liability for knowingly presenting or causing "
                "false claims and related conduct, including damages and penalties."
            ),
        },
        {
            "title": "FAR 52.203-13 — Contractor Code of Business Ethics and Conduct",
            "url": "https://www.acquisition.gov/far/52.203-13",
            "relevance": (
                "Contains ethics and disclosure obligations when the "
                "clause applies and its specified conditions are met."
            ),
        },
    ],
}
