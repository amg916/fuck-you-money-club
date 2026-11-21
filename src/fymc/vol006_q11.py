from __future__ import annotations

CHAPTER_11 = {
    "id": "Q11",
    "chapter_id": "Q11",
    "chapter_number": 11,
    "question_number": 11,
    "slug": "pod-architecture-contractor-kpis-exit-valuation",
    "question_prompt": "How do you structure a lean 2 FT + 3 C (5 people) -> 3 FT + 4 C (7 people) pod, enforce weekly scorecards, and build transferable books that command a premium exit multiple (or durable cash cow)?",
    "kicker": "Q11 / THE BIG MONEY PLAYBOOKS",
    "title": "Pod Architecture, Contractor KPIs & Exit Valuation",
    "subtitle": "Five-to-Seven-Person Delivery Pods, Weekly Acceptance Economics, Accrual Cohorts, Signed IP Transfers, and Buyer-Tested Earnings",
    "layout_template": "action_checklist",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #29, Productized AI Agencies, holds Rank #06 with an 86/100 "
        "Money-to-Manpower Score across 23 mapped plays. The operating asset is a "
        "repeatable delivery pod, not the founder's ability to rescue every deployment. "
        "Assign five seats across scope control, architecture, implementation, independent "
        "QA, and monitoring; expand to seven only against funded backlog and measured "
        "capacity. Canonical annual owner profit is $20,000 Conservative, $165,000 Base, "
        "and $400,000 Scaled. Preserve those cases through acceptance-linked contractor "
        "payments, customer and counterparty exposure limits of 25%, accrual books, "
        "signed IP assignments, and documented access authority. Weekly evidence must "
        "connect delivered work to recognized fees and support obligations. A buyer "
        "pays for transferable earnings; a continuing owner collects the same discipline "
        "as durable cash."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual implementation fees and support retainers; excludes client automation gains.",
            "note": "20% net margin; $20,000 annual owner net profit; 2 FT + 3 C.",
        },
        {
            "label": "Base",
            "value": "$550,000",
            "context": "Annual implementation fees and support retainers; excludes client automation gains.",
            "note": "30.0% net margin; $165,000 annual owner net profit; 2 FT + 3 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual implementation fees and support retainers; excludes client automation gains.",
            "note": "40% net margin; $400,000 annual owner net profit; 3 FT + 4 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Give every play one accountable seat and a funded capacity envelope",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build Candidate #29 around two employee seats and three bounded "
                    "contractor work packages. FT1 owns commercial qualification, scope, "
                    "pricing, collections, and customer relationships; FT2 owns architecture, "
                    "technical acceptance, access authorization, and production accountability. "
                    "C1 implements approved integrations, C2 independently tests outputs "
                    "and security boundaries, and C3 maintains monitoring, runbooks, and "
                    "scheduled support coverage. Contractors are not three additional "
                    "unlimited employees hidden inside a retainer. Maintain the existing "
                    "23-play register with its authoritative identifiers, then allocate "
                    "primary accountability across these seats: four plays to FT1, six "
                    "to FT2, five to C1, four to C2, and four to C3. This is a "
                    "work-allocation model, not a replacement taxonomy for the mapped "
                    "plays. Every register entry needs one accountable owner, one backup, "
                    "an acceptance artifact, a client-data boundary, and an estimated "
                    "monthly load. Keep sales promises, implementation work, and final "
                    "acceptance visibly separate even when a small team shares meetings. "
                    "FT2 may reject C1's delivery without renegotiating commercial scope; "
                    "FT1 may sell an extension only after capacity and pricing are "
                    "recalculated. Store the register in Linear or Jira and attach "
                    "versioned evidence in the agency's authorized GitHub organization."
                ),
                (
                    "Size work from available delivery hours rather than impressive "
                    "headcount. As an explicit planning example, reserve 40 weekly "
                    "hours across the two full-time seats for delivery after sales, "
                    "administration, and leadership, and contract another 45 hours of "
                    "specialist capacity. At 70% planned utilization, that creates "
                    "59.5 scheduled delivery hours while preserving 25.5 hours for "
                    "variance, investigation, and interruptions. A sprint requiring "
                    "45 delivery hours consumes roughly three quarters of that "
                    "weekly envelope; two simultaneous starts would exceed it. "
                    "Measure actual effort for four weeks before raising concurrency. "
                    "The Conservative scorecard's $100,000 revenue and $20,000 owner "
                    "profit leave only $80,000 for total annual costs. That amount "
                    "generally cannot sustain two market-paid full-time employees, "
                    "three contractors, and operating overhead. Preserve the canonical "
                    "2 FT + 3 C label, but flag its staffing feasibility instead "
                    "of silently treating employees as fractional. Owner compensation, "
                    "local wage requirements, payroll burden, and startup funding "
                    "need an explicit reconciliation. Funding supplies cash, not "
                    "profit, and founder labor still has a replacement cost. Do "
                    "not launch a payroll commitment until actual contracts and "
                    "available capital cover the resulting obligations."
                ),
                (
                    "Expand to 3 FT + 4 C by adding FT3 as delivery manager "
                    "and customer-success owner, plus C4 as a second implementation "
                    "specialist with recovery capability. Transfer four existing "
                    "play accountabilities to FT3 and two to C4; rebalance the "
                    "original seats so the register still totals exactly 23, "
                    "rather than manufacturing new plays to justify hiring. The "
                    "third employee should remove founder coordination and renewal "
                    "dependence before adding another technical bottleneck. Require "
                    "eight weeks of signed, contribution-positive backlog, demonstrated "
                    "support demand, and a cash forecast that survives the largest "
                    "customer paying thirty days late. These are internal planning "
                    "thresholds, not claims about every agency's demand cycle. Use "
                    "named backups for each privileged system, but never shared "
                    "credentials; maintain individual accounts, least-privilege roles, "
                    "and documented emergency access. Contractor classification "
                    "depends on actual working conditions, not the label in a "
                    "statement of work. Assess applicable wage, tax, and state "
                    "tests, including California Labor Code section 2775 where "
                    "relevant. Specify deliverables and service windows without "
                    "assuming that compulsory employee-like schedules become "
                    "independent contracting merely because invoices arrive "
                    "through Deel or another payment platform."
                ),
            ],
            "table": {
                "caption": "Five Core Seats and the Funded Seven-Person Expansion",
                "headers": [
                    "Seat and bounded operational responsibility",
                    "Evidence required before accepting completed work",
                    "Capacity and commercial control mechanism",
                    "Backup and transferability requirement for buyers",
                ],
                "rows": [
                    [
                        "FT1 owns pricing, customer relationships, scope, and collection decisions.",
                        "Signed scope connects promised outcomes to measurable acceptance artifacts.",
                        "Four initial play accountabilities remain inside documented weekly capacity.",
                        "FT3 later inherits renewal routines and documented customer relationship history.",
                    ],
                    [
                        "FT2 owns architecture, authorized access, technical acceptance, and recovery.",
                        "Release record contains reviewer identity, test results, and rollback instructions.",
                        "Six initial play accountabilities exclude unlimited production support commitments.",
                        "C3 rehearses recovery while FT2 retains final production accountability.",
                    ],
                    [
                        "C1 delivers bounded integrations against approved specifications and milestones.",
                        "Versioned code and fixtures reproduce every contracted acceptance result.",
                        "Five initial play accountabilities use priced packages with change orders.",
                        "C4 later reproduces builds using documented dependencies and client permissions.",
                    ],
                    [
                        "C2 independently evaluates output quality, permissions, and regression behavior.",
                        "Reviewer attaches adversarial cases and evidence from representative workflow samples.",
                        "Four initial play accountabilities retain independence from implementation acceptance.",
                        "FT2 maintains secondary review capability without eliminating independent testing.",
                    ],
                    [
                        "C3 owns scheduled monitoring, support triage, and current operating runbooks.",
                        "Incident tickets show detection, acknowledgement, containment, and restoration timestamps.",
                        "Four initial play accountabilities fit explicitly purchased coverage windows.",
                        "FT2 holds individual recovery access and tests the handoff quarterly.",
                    ],
                    [
                        "FT3 and C4 add coordination capacity and implementation recovery depth.",
                        "Backlog analysis demonstrates funded demand and documented founder workload reduction.",
                        "Transfer six existing accountabilities while preserving twenty-three total mapped plays.",
                        "Customer meetings and rebuild exercises demonstrate independence from founding personnel.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the small pod feel larger without concealing labor",
                "body": (
                    "Reduce handoff friction before buying more hours; preserve independent "
                    "review and explicit ownership across all 23 mapped plays."
                ),
                "items": [
                    "Have C2 author failure fixtures before C1 starts implementation, using authorized synthetic examples and a frozen acceptance rubric.",
                    "Sell one production connector per sprint until measured connector maintenance costs support a broader fixed-price package.",
                    "Record a clean-room rebuild walkthrough with redacted configuration, then ask the backup contractor to reproduce it without founder assistance.",
                    "Give FT1 a weekly report of unpaid scope changes so commercial leakage is corrected before it becomes contractor overtime.",
                ],
            },
        },
        {
            "heading": "2. Pay for accepted work and run one evidence-backed weekly scorecard",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Contract compensation should make quality observable without "
                    "forcing specialists to absorb unlimited client ambiguity. An "
                    "illustrative $6,000 integration package can pay $1,200 after "
                    "approved design, $3,600 after independently verified staging "
                    "acceptance, and $1,200 after production handoff with a complete "
                    "runbook. Define invoice dates, review deadlines, written rejection "
                    "reasons, and dispute handling; pay undisputed amounts when due "
                    "under the agreement and applicable law. Price scope changes "
                    "separately rather than withholding earned fees to obtain extra "
                    "features. Establish a five-business-day acceptance review window "
                    "and a thirty-day correction period for reproducible defects "
                    "against the frozen specification. New model behavior, upstream "
                    "API changes, and customer process changes require triage before "
                    "anyone assigns responsibility. Keep QA compensation independent "
                    "of the number of releases approved, and never reward a "
                    "reviewer for hiding defects to accelerate collections. As "
                    "a sprint illustration, a $15,000 implementation fee less "
                    "$6,000 implementation, $1,200 independent QA, $300 attributable "
                    "usage, and $1,500 allocated employee delivery cost produces "
                    "$6,000 delivery contribution, or 40%. That contribution "
                    "still must cover selling, administration, support obligations, "
                    "and other overhead before it becomes owner profit."
                ),
                (
                    "Publish Friday's scorecard from source systems, not a manually "
                    "polished slide. Linear supplies accepted milestones and "
                    "cycle times; GitHub supplies reviewed changes; Harvest supplies "
                    "effort; the accounting ledger supplies accrued revenue and "
                    "costs; authorized monitoring supplies usage and incident "
                    "events. Track first-pass acceptance as accepted first "
                    "submissions divided by all first submissions, with the "
                    "sample count beside the rate. Use an initial 90% "
                    "target, but investigate small samples rather than ranking "
                    "contractors on one unusual ticket. Track rework hours "
                    "divided by total delivery hours, targeting below 10%, "
                    "and on-time milestones divided by milestones due, targeting "
                    "at least 95%. Define a blocker before measuring it "
                    "and report its age and accountable decision maker. "
                    "Pair automation completion with error severity, human "
                    "override rate, and the proportion of consequential decisions "
                    "reviewed by an authorized person. A faster workflow "
                    "that silently sends inaccurate customer communications is "
                    "not a quality improvement. Review contribution by project, "
                    "retainer consumption, overdue receivables, and committed "
                    "capacity in the same meeting. Each adverse signal "
                    "gets one owner, one corrective action, and a "
                    "dated evidence requirement rather than another status discussion."
                ),
                (
                    "Write service levels around coverage the pod can actually "
                    "supply. An illustrative managed retainer can include weekday "
                    "coverage from 09:00 to 17:00 in the named client "
                    "timezone, one-business-hour acknowledgement for a production "
                    "blocker, and four-covered-hour acknowledgement for degraded "
                    "service. Acknowledgement is not restoration. Define containment, "
                    "customer updates, escalation, and recovery objectives separately; "
                    "do not promise continuous response from three part-time "
                    "contractor packages. For an exposed data path or "
                    "unauthorized action, empower the designated responder to "
                    "disable the affected automation, preserve necessary evidence, "
                    "and notify FT2 immediately through the documented channel. "
                    "Applicable customer contracts and incident laws determine "
                    "external notification duties. Test the fallback with "
                    "synthetic records, including expired credentials, model "
                    "timeouts, duplicate webhook delivery, and malformed structured "
                    "outputs. Use idempotency keys and transaction boundaries "
                    "where supported instead of assuming a retry is "
                    "harmless. The Monday review approves only the corrective "
                    "work that fits purchased capacity and records whether "
                    "a client change order is required. Persistent "
                    "misses trigger narrower scope, additional purchased "
                    "coverage, or a replacement supplier after an orderly "
                    "handoff, not concealed unpaid overtime or optimistic "
                    "changes to the scorecard definitions."
                ),
            ],
            "table": {
                "caption": "Weekly Contractor Quality and Pod Economics Scorecard",
                "headers": [
                    "Metric with a reproducible operating definition",
                    "Initial threshold and required interpretation",
                    "Authoritative evidence and accountable reviewing seat",
                    "Corrective action when performance leaves bounds",
                ],
                "rows": [
                    [
                        "First-pass acceptance divides accepted initial submissions by all initial submissions.",
                        "Target at least ninety percent while displaying underlying sample counts.",
                        "C2 records frozen-rubric outcomes; FT2 verifies disputed acceptance decisions.",
                        "Examine failed fixtures and repair specification ambiguity before assigning blame.",
                    ],
                    [
                        "Rework share divides corrective delivery hours by total delivery hours.",
                        "Target below ten percent while separating paid customer scope changes.",
                        "Harvest entries link to defect tickets reviewed jointly by FT2.",
                        "Reduce concurrent starts and fix repeated causes before adding capacity.",
                    ],
                    [
                        "On-time delivery divides timely accepted milestones by all milestones due.",
                        "Target at least ninety-five percent against the agreed acceptance calendar.",
                        "Linear milestone history preserves original commitments and documented customer delays.",
                        "Replan capacity openly and price requested acceleration before promising recovery.",
                    ],
                    [
                        "Project contribution subtracts attributable delivery costs from recognized project fees.",
                        "Compare actual contribution with quoted economics and remaining delivery obligations.",
                        "Ledger entries and contractor accruals reconcile through FT1 each Friday.",
                        "Issue scoped change orders or stop repeating structurally unprofitable packages.",
                    ],
                    [
                        "Incident acknowledgement measures elapsed covered time until a responder engages.",
                        "Production blockers receive acknowledgement within one purchased business coverage hour.",
                        "Monitoring events and response tickets retain timestamps reviewed by C3.",
                        "Repair routing and coverage; distinguish acknowledgement failures from restoration delays.",
                    ],
                    [
                        "Support consumption compares accrued service effort with purchased retainer capacity.",
                        "Escalate at eighty percent consumption before the coverage period closes.",
                        "C3 links support tickets, usage charges, and remaining contractual obligations.",
                        "Obtain an authorized extension or schedule permissible work into renewal.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the measurement interval",
                    "action": "Close the weekly delivery window at the agreed Friday cutoff.",
                    "detail": "Preserve original due dates, first submissions, accepted changes, covered incident hours, and source-system links.",
                },
                {
                    "step": 2,
                    "title": "Reconcile labor and acceptance",
                    "action": "Match contractor milestones and employee effort to accepted project artifacts.",
                    "detail": "Accrue earned but uninvoiced delivery costs and separate defects from newly requested customer functionality.",
                },
                {
                    "step": 3,
                    "title": "Resolve exceptions with named owners",
                    "action": "Review quality, contribution, concentration, and capacity in one thirty-minute meeting.",
                    "detail": "Assign each exception a responsible seat, corrective action, deadline, and evidence needed to close it.",
                },
                {
                    "step": 4,
                    "title": "Publish the next capacity commitment",
                    "action": "Approve only the following week's work that fits purchased coverage and available cash.",
                    "detail": "Send authorized customer updates, record priced scope changes, and archive the scorecard for cohort and buyer review.",
                },
            ],
        },
        {
            "heading": "3. Reconcile accrual books, cohort retention, and concentrated exposures",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Keep implementation revenue, managed support revenue, client "
                    "business outcomes, and cash receipts in separate fields. "
                    "Candidate #29 earns fees and retainers; a client's "
                    "increased sales, reduced payroll effort, or processed "
                    "transaction value is not agency revenue. The canonical "
                    "annual bridges are exact: Conservative revenue of "
                    "$100,000 less $80,000 total costs equals $20,000 "
                    "owner profit; Base revenue of $550,000 less "
                    "$385,000 equals $165,000; Scaled revenue of "
                    "$1,000,000 less $600,000 equals $400,000. Those "
                    "are respectively 20%, 30.0%, and 40% net "
                    "margins, not delivery contribution percentages. Do not "
                    "turn the $2,500-$18,000 monthly operating-expense "
                    "planning range into a substitute for complete "
                    "annual costs; document which direct labor and "
                    "other costs sit outside that narrower budget. "
                    "An illustrative Base revenue bridge is twenty "
                    "$15,000 implementations plus ten accounts averaging "
                    "$25,000 recognized annual support fees. A Scaled "
                    "bridge is twenty-five $20,000 implementations plus "
                    "twenty accounts averaging $25,000 support fees. "
                    "Both reconcile exactly, but neither demonstrates "
                    "delivery feasibility until hours and service "
                    "obligations fit the relevant pod. Conservative "
                    "could comprise four $15,000 implementations and "
                    "four $10,000 annual support accounts, subject "
                    "to the staffing cost constraint already identified."
                ),
                (
                    "Use accrual schedules that explain when services "
                    "are earned, not merely when Stripe pays "
                    "the bank. For a $24,000 annual stand-ready "
                    "support arrangement collected in advance, recognizing "
                    "$2,000 monthly is appropriate only when "
                    "the service obligation is satisfied evenly "
                    "through that period. Record the unearned "
                    "balance as a contract liability. Implementation "
                    "recognition depends on the contractual performance "
                    "obligations and the applicable accounting framework; "
                    "a deposit or invoice milestone alone does "
                    "not establish that delivery has occurred. "
                    "Have the accountant document that policy "
                    "and apply it consistently. Accrue accepted "
                    "contractor work before the invoice arrives, "
                    "allocate attributable model and hosting usage, "
                    "and reconcile bank, receivable, payable, and "
                    "contract-liability balances monthly. Maintain customer "
                    "cohorts by first support-service month, recording "
                    "starting recurring fees, expansion, contraction, "
                    "churn, contribution, and support hours. Gross "
                    "revenue retention excludes expansion; net revenue "
                    "retention includes it, while both exclude "
                    "new customers from the starting cohort. "
                    "Report implementation fees separately so a "
                    "large sprint cannot disguise shrinking recurring "
                    "support. Preserve signed scope changes and "
                    "credit notes alongside the ledger entries "
                    "so a buyer can reproduce both "
                    "revenue timing and delivery economics."
                ),
                (
                    "Set a maximum 25% customer concentration "
                    "policy against trailing-twelve-month recognized revenue, "
                    "forward contracted fees, and gross receivables, "
                    "testing each denominator separately. Aggregate "
                    "entities under common control; five subsidiaries "
                    "of one sponsor do not create "
                    "five independent revenue risks. At Base "
                    "revenue, the trailing annual customer limit "
                    "is $137,500; at Scaled it is "
                    "$250,000; at Conservative it is "
                    "$25,000. During startup, the first "
                    "customer necessarily breaches a diversified "
                    "revenue limit. Record that exception "
                    "with a dated diversification plan, "
                    "and restrict new fixed commitments "
                    "until exposure falls within policy. "
                    "Apply the same 25% maximum "
                    "to material reseller or referral "
                    "counterparties using attributable recognized fees. "
                    "For critical delivery suppliers, measure "
                    "non-substitutable delivery exposure rather "
                    "than pretending low invoice spend "
                    "means low dependency. A sole "
                    "model provider may support every "
                    "workflow despite costing little; tested "
                    "fallbacks reduce this exposure only "
                    "when authorized and operational. Track "
                    "contractor replacement time and cash "
                    "held with payment intermediaries separately. "
                    "A cap does not repair "
                    "a breach automatically: require an "
                    "owner, an exposure-reduction action, "
                    "and evidence that the alternative "
                    "works before describing the book "
                    "as diversified."
                ),
            ],
            "table": {
                "caption": "Canonical Earnings Bridges and Concentration Control Ledger",
                "headers": [
                    "Accounting view or exposure being controlled",
                    "Exact reconciliation or explicit internal limit",
                    "Evidence required to substantiate the reported position",
                    "Failure mode and required operator response",
                ],
                "rows": [
                    [
                        "Conservative annual fee revenue uses the five-person canonical staffing label.",
                        "$100,000 revenue less $80,000 costs produces $20,000 owner profit.",
                        "Cost schedule identifies wages, contractor obligations, overhead, and funding assumptions.",
                        "Unfunded full-time payroll makes this roster infeasible despite the arithmetic.",
                    ],
                    [
                        "Base annual fees exclude all customer revenue attributed to automation.",
                        "$550,000 revenue less $385,000 costs produces $165,000 owner profit.",
                        "Twenty implementations and ten support accounts reconcile the illustrative revenue bridge.",
                        "Missing contractor accruals inflate earnings and must enter the closing ledger.",
                    ],
                    [
                        "Scaled annual fees support three employees and four contractor packages.",
                        "$1,000,000 revenue less $600,000 costs produces $400,000 owner profit.",
                        "Twenty-five implementations and twenty support accounts reconcile the illustrative revenue bridge.",
                        "Revenue growth without measured capacity creates hidden support debt and churn.",
                    ],
                    [
                        "Customer groups aggregate common ownership across revenue, backlog, and receivables.",
                        "Each separately measured customer exposure remains at or below twenty-five percent.",
                        "Customer hierarchy and ledger exports establish all three exposure denominators.",
                        "Document startup exceptions and reduce dependency before adding fixed commitments.",
                    ],
                    [
                        "Resellers and referral counterparties aggregate all attributable recognized customer fees.",
                        "No counterparty contributes more than twenty-five percent of recognized fees.",
                        "Contract source tags distinguish direct relationships from intermediary-controlled customer access.",
                        "Build direct acquisition and transfer rights before the intermediary controls renewals.",
                    ],
                    [
                        "Critical suppliers expose workflows that cannot currently operate through substitutes.",
                        "Target non-substitutable recognized-fee exposure at or below twenty-five percent.",
                        "Authorized failover tests identify which customer workflows remain provider dependent.",
                        "Record concentration breaches until replacement paths pass actual operating tests.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Build transferable earnings before negotiating an exit multiple",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Transferability begins with ownership and "
                    "permissions, not a broker presentation. "
                    "Under 17 U.S.C. section 204(a), "
                    "a copyright ownership transfer generally "
                    "requires a signed writing from "
                    "the owner or authorized agent. "
                    "Obtain signed contractor assignments "
                    "covering commissioned code, prompts "
                    "where protectable, documentation, tests, "
                    "and other protectable deliverables; "
                    "do not rely exclusively on "
                    "a work-made-for-hire label for "
                    "contractor software. Separate preexisting "
                    "tools, third-party components, and "
                    "client-owned materials in schedules "
                    "with the actual licenses needed "
                    "for continued operation and transfer. "
                    "A contractor cannot assign rights "
                    "they never owned, and an "
                    "agency cannot promise exclusive "
                    "ownership of every machine-generated "
                    "output. Document customer access "
                    "authority, processing instructions, subprocessors, "
                    "retention limits, and deletion "
                    "procedures. California service-provider "
                    "arrangements, where applicable, require "
                    "contract terms and practices "
                    "consistent with Civil Code "
                    "section 1798.100(d) and relevant "
                    "implementing rules. Review customer "
                    "assignment and change-of-control "
                    "clauses before modeling a "
                    "sale. Maintain human review "
                    "for consequential decisions and "
                    "retain evidence supporting performance "
                    "claims under the FTC Act's "
                    "prohibition on deceptive practices. "
                    "These records protect ongoing "
                    "delivery and let a buyer "
                    "identify rights they can "
                    "actually acquire."
                ),
                (
                    "Use valuation multiples as "
                    "negotiation sensitivities, not as "
                    "automatic rewards for mentioning "
                    "AI. An illustrative owner-operated "
                    "agency might be tested at "
                    "2.0-3.0 times normalized seller's "
                    "discretionary earnings, while a "
                    "manager-run agency with durable "
                    "retention and transferable contracts "
                    "might be tested at "
                    "3.0-5.0 times normalized EBITDA. "
                    "These are planning ranges, "
                    "not observed transaction comparables. "
                    "Actual bids depend on "
                    "scale, customer quality, growth, "
                    "market conditions, and deal "
                    "structure. The canonical $165,000 "
                    "Base owner profit is "
                    "neither automatically SDE nor "
                    "EBITDA. Build a bridge "
                    "showing owner wages already "
                    "expensed, genuine discretionary costs, "
                    "interest, taxes, depreciation, amortization, "
                    "and required replacement management. "
                    "If that bridge independently "
                    "supports $165,000 SDE, the "
                    "illustrative 2.0-3.0 range implies "
                    "$330,000-$495,000 enterprise value. "
                    "If a separately verified "
                    "Scaled bridge supports $300,000 "
                    "normalized EBITDA after replacement "
                    "management, 3.0-5.0 implies "
                    "$900,000-$1,500,000 enterprise value. "
                    "The $300,000 example is "
                    "an assumed valuation input, "
                    "not a revision to "
                    "the $400,000 canonical owner "
                    "profit. Never combine an "
                    "SDE add-back with an "
                    "EBITDA multiple while omitting "
                    "the employee needed to "
                    "replace the departing owner."
                ),
                (
                    "Prepare a buyer room "
                    "that reconciles monthly ledgers "
                    "to contracts, cohort retention, "
                    "bank activity, delivery evidence, "
                    "and the 23-play register. "
                    "Include the weekly scorecards, "
                    "contractor agreements, signed IP "
                    "chain, customer transfer restrictions, "
                    "security incidents, recovery tests, "
                    "and a schedule of "
                    "unfulfilled prepaid services. "
                    "Share redacted summaries first; "
                    "disclose customer data only "
                    "through authorized, necessary diligence "
                    "access with controlled recipients "
                    "and an access log. "
                    "Run a four-week founder-absence "
                    "exercise in which the "
                    "pod handles renewals, deployment "
                    "decisions, and incident triage "
                    "without undocumented intervention. "
                    "Measure delivery misses and "
                    "replacement labor rather than "
                    "declaring independence because "
                    "the founder stopped attending "
                    "standups. Enterprise value "
                    "does not equal cash "
                    "received: reconcile debt, "
                    "cash treatment, normalized "
                    "working capital, transaction "
                    "costs, holdbacks, and "
                    "contingent consideration separately. "
                    "Prepaid support liabilities "
                    "need explicit treatment "
                    "so the seller cannot "
                    "retain all collections "
                    "while leaving unfunded "
                    "service obligations behind. "
                    "If bids undervalue "
                    "durable earnings, retain "
                    "the business with "
                    "the same concentration "
                    "limits and management "
                    "coverage. Distributions should "
                    "follow payroll, tax "
                    "obligations, service reserves, "
                    "and the cash "
                    "forecast; recurring owner "
                    "profit is valuable "
                    "only when operations "
                    "can keep producing it."
                ),
            ],
            "table": {
                "caption": "Buyer Diligence, Earnings Normalization, and Transfer Evidence",
                "headers": [
                    "Buyer question and specific asset being examined",
                    "Evidence that the small pod must produce",
                    "Valuation interpretation without overstating canonical owner profit",
                    "Remediation that also improves continued owner cash flow",
                ],
                "rows": [
                    [
                        "Can the agency transfer ownership of its reusable delivery assets?",
                        "Signed assignments and component schedules establish the actual ownership chain.",
                        "Missing rights impair transferability regardless of the proposed earnings multiple.",
                        "Resolve contractor assignments and licenses before reusing or selling deliverables.",
                    ],
                    [
                        "Will customer contracts survive assignment or a change in control?",
                        "Executed agreements identify consent requirements, termination rights, and renewal dates.",
                        "Restricted transfers weaken certainty of the buyer's projected recurring earnings.",
                        "Negotiate workable transfer provisions during ordinary renewals without misrepresenting intentions.",
                    ],
                    [
                        "Can normalized Base seller earnings support an owner-operated acquisition case?",
                        "Independent earnings bridge supports the assumed $165,000 discretionary earnings input.",
                        "Illustrative 2.0-3.0 times produces $330,000-$495,000 enterprise value before deal adjustments.",
                        "Document legitimate add-backs and distinguish owner benefits from recurring operating costs.",
                    ],
                    [
                        "Can the Scaled pod operate under fully costed replacement management?",
                        "Separate normalization work supports the illustrative $300,000 managed EBITDA input.",
                        "Illustrative 3.0-5.0 times produces $900,000-$1,500,000 enterprise value before deal adjustments.",
                        "Measure replacement responsibilities and eliminate founder-only customer or deployment authority.",
                    ],
                    [
                        "Do recurring fees survive without excessive support effort or customer concentration?",
                        "Cohort schedules reconcile retention, contribution, support consumption, and grouped customer exposure.",
                        "Durable contribution strengthens negotiating leverage more than unprofitable recurring invoice volume.",
                        "Reprice expensive retainers and diversify concentrated relationships before expanding fixed payroll.",
                    ],
                    [
                        "How much closing value becomes immediately available cash for the seller?",
                        "Purchase-price bridge separates debt, working capital, holdbacks, costs, and contingent payments.",
                        "Headline enterprise value can materially exceed the seller's immediately received proceeds.",
                        "Model payment timing and prepaid service obligations before accepting transaction economics.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify the book before presenting premium valuation claims",
                "body": (
                    "Use four pre-flight checks before expanding the pod or circulating "
                    "a buyer earnings package; retain unresolved exceptions in the record."
                ),
                "items": [
                    "Reconcile all three canonical cases exactly, and identify whether each proposed earnings multiple uses verified SDE or normalized EBITDA.",
                    "Confirm that all 23 mapped plays have named owners, tested backups, acceptance evidence, and capacity within the five-person or seven-person roster.",
                    "Verify signed IP transfers, customer-system authorization, processing terms, third-party licenses, and contract transfer requirements before sharing diligence materials.",
                    "Test customer and counterparty concentrations against the 25% limits, and document working fallbacks or dated remediation for every exception.",
                ],
            },
        },
    ],
    "pull_quote": (
        "A transferable agency sells evidence-backed earnings, not the founder's willingness to remain indispensable."
    ),
    "diagram_id": "diag-06",
    "action_checklist": [
        "Assign the existing 23 mapped plays across FT1, FT2, C1, C2, and C3 with one accountable owner, backup, acceptance artifact, and measured capacity estimate each.",
        "Price contractor packages with staged acceptance payments, independent QA, explicit correction boundaries, and service windows the pod can actually staff.",
        "Publish a weekly source-linked scorecard covering acceptance, rework, delivery timeliness, contribution, support consumption, incident response, and corrective-action ownership.",
        "Close monthly accrual books to the canonical revenue and owner-profit bridges, separating client business outcomes, deposits, earned fees, contractor accruals, and service liabilities.",
        "Enforce customer and counterparty exposure limits of 25%, aggregate common-control entities, and record startup or supplier exceptions with tested reduction plans.",
        "Complete signed IP assignments, contract-transfer review, a four-week founder-absence test, and separate SDE and EBITDA bridges before evaluating sale proceeds or continued distributions.",
    ],
    "statutory_citations": [
        {
            "title": "17 U.S.C. section 204(a) — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Copyright ownership transfers generally require a signed writing from "
                "the rights owner or authorized agent; maintain an auditable contractor "
                "assignment chain for protectable agency deliverables."
            ),
        },
        {
            "title": "17 U.S.C. section 101 — Definitions, including work made for hire",
            "url": "https://www.law.cornell.edu/uscode/text/17/101",
            "relevance": (
                "Commissioned works satisfy the statutory work-made-for-hire definition "
                "only under specified conditions; contractor software should not rely "
                "on that label as a substitute for appropriate signed assignments."
            ),
        },
        {
            "title": "California Labor Code section 2775 — Worker classification framework",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2775.&lawCode=LAB",
            "relevance": (
                "Evaluate applicable worker-classification requirements and statutory "
                "exceptions using actual operating facts before treating recurring "
                "delivery seats as independent contractors."
            ),
        },
        {
            "title": "California Civil Code section 1798.100(d) — Personal-information contract requirements",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": (
                "For covered arrangements, contracts governing disclosures to service "
                "providers, contractors, or third parties must include required "
                "purposes, protections, oversight rights, and remediation provisions."
            ),
        },
        {
            "title": "15 U.S.C. section 45(a) — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": (
                "Keep evidence supporting AI performance, savings, reliability, and "
                "service claims; misleading claims can create exposure under the "
                "FTC Act's prohibition on unfair or deceptive practices."
            ),
        },
        {
            "title": "29 U.S.C. sections 206 and 207 — Minimum wage and overtime requirements",
            "url": "https://www.law.cornell.edu/uscode/text/29/chapter-8",
            "relevance": (
                "Budget applicable wage and overtime obligations for covered employees; "
                "contract labels and optimistic unit economics do not remove statutory "
                "pay requirements, and state requirements may be more protective."
            ),
        },
    ],
}
