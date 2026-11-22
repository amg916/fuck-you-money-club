from __future__ import annotations

CHAPTER_11 = {
    "id": "Q11",
    "chapter_id": "Q11",
    "chapter_number": 11,
    "question_number": 11,
    "slug": "pod-architecture-contractor-kpis-and-exit-valuation",
    "question_prompt": "How do you structure a lean 1 FT + 2 C (3 people) -> 2 FT + 3 C (5 people) pod, enforce weekly scorecards, and build transferable books that command a premium exit multiple (or durable cash cow)?",
    "kicker": "Q11 / THE BIG MONEY PLAYBOOKS",
    "title": "Pod Architecture, Contractor KPIs & Exit Valuation",
    "subtitle": "Five-Seat Capacity Brokerage: DCGM Metering, LiteLLM Routing, SIP Quality, ASC 606 Books, and Written IP Transfers",
    "layout_template": "action_checklist",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #36, GPU Compute & Telecom Capacity Arbitrage, ranks #03 of 36 "
        "with a 94/100 Money-to-Manpower Score across 15 mapped plays. Build the "
        "business around accountable seats, prepaid exposure, reproducible metering, "
        "and transferable customer contracts rather than founder heroics. The "
        "Conservative, Base, and Scaled cases produce $27,000, $189,000, and $456,000 "
        "in annual owner net profit from $150,000, $675,000, and $1,200,000 in gross "
        "billings. Their retained contribution is $97,500, $438,750, and $780,000. "
        "This chapter assigns the three-person and five-person pods, specifies "
        "contractor compensation and weekly evidence, caps customer and upstream "
        "concentration at 25%, and converts accrual books into a buyer-ready earnings "
        "bridge. Exit multiples remain underwriting assumptions; recurring contribution, "
        "replaceable labor, and executable transfer rights determine the offer."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross billings; $97,500 retained contribution at 65%",
            "note": "18% gross-billings net margin; $27,000 annual owner net profit; 27.69% retained margin; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$675,000",
            "context": "Annual gross billings; $438,750 retained contribution at 65%",
            "note": "28.0% gross-billings net margin; $189,000 annual owner net profit; 43.08% retained margin; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross billings; $780,000 retained contribution at 65%",
            "note": "38% gross-billings net margin; $456,000 annual owner net profit; 58.46% retained margin; 2 FT + 3 C (5 people)",
        },
    ],
    "sections": [
        {
            "heading": "1. Assign Fifteen Plays to Accountable Seats, Not Fifteen Specialists",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the 15 mapped plays as one controlled capacity book, not "
                    "15 businesses requiring separate teams. For seat allocation, use "
                    "this chapter's operating decomposition: P01 H100 reservations, P02 "
                    "H200 reservations, P03 B200 reservations, P04 supported GPU "
                    "partition resale, and P05 GPU burst fulfillment form the compute "
                    "lane. P06 multi-provider token routing, P07 batch inference, P08 "
                    "dedicated endpoints, P09 inference failover, and P10 private "
                    "zero-retention inference form the inference lane. P11 SIP "
                    "origination, P12 SIP termination, P13 registered 10DLC messaging, "
                    "P14 authorized IPv4 leasing, and P15 carrier overflow form the "
                    "telecom lane. These identifiers organize the supplied opportunity "
                    "scope; they are not additional scorecard revenue assumptions. "
                    "Initially activate only plays whose support and accounting "
                    "evidence the three-person pod can maintain. The founder, the "
                    "single full-time seat, owns pricing, customer qualification, "
                    "commitments, collections, and vendor negotiations. Contractor "
                    "one owns compute reliability across P01 through P10; contractor "
                    "two owns carrier operations across P11 through P15. The founder "
                    "retains accountability for both lanes and the consolidated "
                    "ledger. Give every play one accountable owner, a documented "
                    "backup, an economic unit, and a suspension procedure before "
                    "selling it. Capacity without a supportable operating owner "
                    "stays outside the active catalog."
                ),
                (
                    "Buy contractor deliverables and bounded coverage rather than "
                    "pretending two part-time specialists provide continuous human "
                    "coverage. Illustrative procurement bands are $90-$140 per hour "
                    "for GPU engineering and $70-$110 for carrier operations, with "
                    "monthly hour ceilings and separately priced scheduled coverage. "
                    "At the Conservative case, even two eight-hour monthly retainers "
                    "at $100 and $85 consume $17,760 annually, leaving $52,740 of the "
                    "$70,500 post-upstream expense envelope for every other modeled "
                    "cost. That arithmetic rules out an unfunded round-the-clock "
                    "promise. Use prepaid shutdown controls, upstream support, and "
                    "explicit service windows instead. Contracts should identify "
                    "deliverables, acceptance tests, response windows, invoicing "
                    "evidence, security duties, and remediation of defective work. "
                    "A priority-one incident receives acknowledgment within 15 "
                    "minutes only during purchased coverage; outside coverage, "
                    "automated containment runs and the published escalation "
                    "schedule applies. Pay the fixed accepted-work fee first; any "
                    "bonus should depend on collected contribution and measured "
                    "quality, never merely GPU occupancy or terminated minutes. "
                    "Require reproducible tests for routing changes, tenant "
                    "isolation, wallet exhaustion, and carrier rollback. Worker "
                    "status follows the actual relationship, including control "
                    "and independence, rather than the contract heading. Review "
                    "applicable classification requirements before imposing "
                    "employee-like schedules on contractors."
                ),
                (
                    "Expand to two full-time seats and three contractors only when "
                    "measured workload and contribution support the replacement "
                    "capacity. The second full-time seat becomes service delivery "
                    "and revenue operations lead, taking daily exceptions, customer "
                    "onboarding, invoice reconciliation, and incident coordination "
                    "away from the founder. The third contractor provides independent "
                    "metering, security, and ledger QA; this person must not approve "
                    "their own production changes. Existing compute and telecom "
                    "contractors retain specialist execution. Track founder hours "
                    "by sales, operations, and engineering for eight weeks before "
                    "authorizing the hire, then verify those hours actually move. "
                    "A useful internal hiring test is collected incremental "
                    "contribution covering 1.5 times the added fully loaded "
                    "monthly cost for three consecutive months, with six months "
                    "of that cost reserved in unrestricted cash. These are "
                    "management thresholds, not changes to the canonical Scaled "
                    "case. That case allows $324,000 of annual post-upstream "
                    "expenses before $456,000 owner profit. Fit the proposed "
                    "staffing, software, insurance, support, and service-credit "
                    "budget inside that envelope or publish a separate downside "
                    "forecast. Maintain organization-owned repositories, vendor "
                    "accounts, and recovery methods so the new lead can operate "
                    "without borrowing the founder's personal identity or "
                    "receiving shared administrator credentials."
                ),
            ],
            "table": {
                "caption": "Three-Person and Five-Person Seat Ownership Across Fifteen Operating Plays",
                "headers": [
                    "Seat or operating boundary",
                    "Accountable production scope",
                    "Acceptance evidence and compensation",
                    "Backup and authority boundary",
                ],
                "rows": [
                    [
                        "Founder full-time seat in the initial pod",
                        "Own prices, commitments, collections, and all commercial exceptions",
                        "Review collected contribution and signed commitments every Friday",
                        "Delegate execution while retaining budget and pricing authority",
                    ],
                    [
                        "Compute contractor covering plays P01 through P05",
                        "Maintain GPU reservations, supported partitions, and burst delivery",
                        "Pay accepted hours against isolation and metering test evidence",
                        "Founder can suspend sales using documented capacity controls",
                    ],
                    [
                        "Same compute contractor covering P06 through P10",
                        "Maintain token routing, batch jobs, endpoints, and failover",
                        "Require versioned routing tests before accepting change invoices",
                        "Carrier contractor follows containment runbook without changing models",
                    ],
                    [
                        "Telecom contractor covering plays P11 through P15",
                        "Maintain SIP routes, messaging registrations, and address leases",
                        "Pay accepted milestones supported by carrier and CDR evidence",
                        "Founder authorizes carrier commitments and emergency spending increases",
                    ],
                    [
                        "Second full-time seat in the expanded pod",
                        "Own onboarding, exception queues, support coordination, and reconciliation",
                        "Measure independently closed tickets and reduced founder operating hours",
                        "Founder retains commercial strategy and exceptional credit decisions",
                    ],
                    [
                        "Third contractor providing independent expanded-pod quality assurance",
                        "Sample meters, access controls, ledgers, and recovery exercises",
                        "Pay completed audit packets with reproducible discrepancy findings",
                        "Cannot approve production changes that they originally implemented",
                    ],
                    [
                        "Purchased coverage boundary applying to every contractor",
                        "Specify staffed windows and automated containment outside coverage",
                        "Match response commitments to funded schedules and escalation tests",
                        "Do not sell continuous response without contracted staffing",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make Specialist Knowledge Portable Before It Becomes Leverage",
                "body": "The strongest small pod stores operational judgment in tested artifacts, not private contractor conversations.",
                "items": [
                    "Require the GPU contractor to attach DCGM samples, scheduler allocation IDs, and tenant-isolation results to each partitioning change; verify the exact GPU and software combination supports the promised configuration.",
                    "Keep LiteLLM routing policies and vLLM deployment manifests in organization-owned version control, with provider credentials injected from a secret store rather than copied into support tickets.",
                    "Pay telecom quality bonuses only after accepted SIP calls, customer disputes, and carrier invoices reconcile; raw minutes reward expensive low-quality routes and abuse.",
                    "Record a quarterly replacement drill in which the backup suspends a tenant, rotates scoped credentials, restores routing, and explains the resulting ledger entries without founder intervention.",
                ],
            },
        },
        {
            "heading": "2. Run a Weekly Scorecard That Rewards Collected Quality",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Publish one weekly scorecard by Monday noon using the preceding "
                    "Sunday cutoff, with immutable source extracts and named "
                    "exception owners. The founder reviews economic exposure; "
                    "contractors explain controllable operating causes. For compute, "
                    "separate reserved GPU-hours, allocatable hours, sold hours, "
                    "delivered hours, and credited hours. Utilization means sold "
                    "billable hours divided by committed allocatable hours, with "
                    "maintenance treatment stated explicitly; it is not average "
                    "GPU activity reported by DCGM. For inference, report contribution "
                    "per million delivered tokens by model and provider, separately "
                    "tracking input, output, cache, retry, and batch billing rules. "
                    "Use LiteLLM request identifiers and provider usage records to "
                    "reconcile customer charges, while vLLM throughput and latency "
                    "metrics explain delivery quality. For telecom, measure "
                    "contribution per accepted minute or message, answer-seizure "
                    "ratio, average call duration, post-dial delay, and disputed "
                    "usage by destination. Do not reward answer-seizure ratio "
                    "improvements created by rejecting difficult legitimate "
                    "destinations. Compare each metric with its contracted service "
                    "target and a four-week baseline. A red metric requires an "
                    "owner, quantified exposure, next action, and due date, rather "
                    "than a narrative about traffic growth. Preserve definitions "
                    "across weeks so a denominator change cannot masquerade as "
                    "an operational improvement."
                ),
                (
                    "Set internal escalation thresholds before contractor bonuses "
                    "are calculated. Investigate a meter-to-invoice difference "
                    "above 0.5% of sampled billings, any confirmed cross-tenant "
                    "exposure, or any spend exceeding an approved prepaid limit. "
                    "Treat these as management controls; contractual remedies "
                    "still follow the signed service terms. Wallet enforcement "
                    "must reserve estimated cost before dispatch and settle "
                    "actual usage afterward, because Stripe payment status alone "
                    "cannot stop concurrent requests from overspending a balance. "
                    "Bound in-flight GPU jobs, token requests, and SIP sessions; "
                    "account for delayed carrier records, settlement reversals, "
                    "and chargebacks. Suspend new dispatch when available credit "
                    "cannot cover the maximum permitted exposure. For QA, sample "
                    "at least five transactions per active play weekly and all "
                    "manual adjustments, then increase sampling when errors "
                    "cluster. Score contractor work using accepted changes, "
                    "repeat incident frequency, evidence completeness, and "
                    "response performance within purchased coverage. A proposed "
                    "bonus pool of 5% of accepted monthly fees is an explicit "
                    "expense, not an invisible deduction from customer credits. "
                    "Do not withhold ordinary accepted fees because upstream "
                    "pricing moved. The founder owns procurement risk; specialists "
                    "own the measurable deliverables and operating controls "
                    "they agreed to perform."
                ),
                (
                    "Enforce a 25% cap separately on customer concentration and "
                    "upstream counterparty concentration, aggregating entities "
                    "under common control. Measure customer concentration using "
                    "both trailing-quarter gross billings and retained contribution; "
                    "use the higher percentage for decisions. Measure supplier "
                    "concentration using both trailing-quarter upstream spend and "
                    "next-quarter noncancelable commitments. A routing dashboard "
                    "showing four brands is insufficient when all four depend "
                    "on one bare-metal owner or carrier group. Record underlying "
                    "dependencies where contracts and supplier disclosures allow "
                    "them to be established. A small launch book may breach "
                    "the cap immediately because its first customer represents "
                    "all sales. Label that condition a launch exception, limit "
                    "irreversible commitments, diversify, and do not represent "
                    "the book as meeting the mature operating standard. Once "
                    "diversified, block incremental concentrated commitments "
                    "until exposure falls within limits. Maintain at least four "
                    "independent material counterparties where feasible, but "
                    "do not force technically unsuitable traffic onto a provider "
                    "just to improve a percentage. Test substitution with "
                    "representative workloads and calls. A portable customer "
                    "contract still has little value when its model behavior, "
                    "number inventory, or latency requirement depends on one "
                    "nontransferable upstream arrangement. Report the tested "
                    "substitution cost beside each concentration measure."
                ),
            ],
            "table": {
                "caption": "Weekly Scorecard Definitions, Evidence, and Escalation Actions",
                "headers": [
                    "Metric and economic denominator",
                    "Primary evidence and accountable owner",
                    "Internal review threshold or target",
                    "Required response when performance deteriorates",
                ],
                "rows": [
                    [
                        "Sold GPU-hours divided by committed allocatable GPU-hours",
                        "Compute contractor reconciles scheduler allocations against reservation invoices",
                        "Investigate contribution deterioration against the four-week operating baseline",
                        "Reduce new reservations before discounting already profitable workloads",
                    ],
                    [
                        "Collected contribution per million delivered inference tokens",
                        "Compute contractor joins LiteLLM identifiers with provider usage",
                        "Every active model route must show positive incremental contribution",
                        "Reprice or suspend routes with negative incremental economics",
                    ],
                    [
                        "Telecom contribution per accepted minute or delivered message",
                        "Carrier contractor reconciles rated records with customer invoices",
                        "Investigate quality shifts against destination-specific contracted service targets",
                        "Rollback affected routes while preserving evidence and customer communications",
                    ],
                    [
                        "Metered charges compared with sampled customer invoice amounts",
                        "Independent reviewer retains reproducible calculations and adjustment histories",
                        "Escalate sampled billing differences exceeding one-half of one percent",
                        "Correct affected cohorts and expand sampling before further settlement",
                    ],
                    [
                        "Unreserved exposure across all concurrently dispatched customer work",
                        "Service owner reconciles wallet reservations and unsettled usage",
                        "Allow no dispatch exceeding approved available prepaid exposure",
                        "Stop new work and settle outstanding reservations deterministically",
                    ],
                    [
                        "Largest customer share of billings and retained contribution",
                        "Founder aggregates related customers using trailing-quarter ledger records",
                        "Keep both concentration measures at or below twenty-five percent",
                        "Restrict incremental exposure and pursue independent replacement customer cohorts",
                    ],
                    [
                        "Largest supplier share of spend and forward commitments",
                        "Founder aggregates related suppliers and documents infrastructure dependencies",
                        "Keep both concentration measures at or below twenty-five percent",
                        "Diversify commitments only after representative technical substitution testing",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the weekly evidence",
                    "action": "Export wallet events, scheduler allocations, provider usage, rated carrier records, and incident histories at the agreed cutoff.",
                    "detail": "Store access-controlled extracts with timestamps, source versions, and checksums; keep customer content outside the scorecard packet.",
                },
                {
                    "step": 2,
                    "title": "Reconcile economics and exposure",
                    "action": "Join usage to invoices and commitments, then calculate contribution, prepaid exposure, concentration, and disputed adjustments.",
                    "detail": "Separate settled cash, earned amounts, deferred customer credits, and estimated upstream accruals instead of blending them into a cash total.",
                },
                {
                    "step": 3,
                    "title": "Assign corrective work",
                    "action": "Hold a 30-minute review that assigns every exception an owner, exposure amount, due date, and acceptance test.",
                    "detail": "Escalate security and wallet failures immediately; the weekly meeting never delays containment of a live incident.",
                },
                {
                    "step": 4,
                    "title": "Accept work and archive decisions",
                    "action": "Verify corrective evidence, approve accepted contractor invoices, and record changes to pricing or commitments.",
                    "detail": "Carry unresolved exceptions into the next scorecard and preserve the original metric definitions for buyer diligence.",
                },
            ],
        },
        {
            "heading": "3. Close Accrual Books That Survive a Change of Owner",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Reconcile the scorecard through three distinct layers: customer "
                    "gross billings, retained contribution after upstream charges, "
                    "and owner net profit after the remaining modeled expenses. "
                    "Conservative produces $150,000 gross billings, $52,500 upstream "
                    "cost, $97,500 retained contribution, $70,500 remaining expenses, "
                    "and $27,000 owner profit. Base produces $675,000 gross billings, "
                    "$236,250 upstream cost, $438,750 retained contribution, "
                    "$249,750 remaining expenses, and $189,000 owner profit. "
                    "Scaled produces $1,200,000 gross billings, $420,000 upstream "
                    "cost, $780,000 retained contribution, $324,000 remaining "
                    "expenses, and $456,000 owner profit. Owner profit divided "
                    "by gross billings yields 18%, 28.0%, and 38%; divided by "
                    "retained contribution it yields 27.69%, 43.08%, and 58.46%. "
                    "The 65% retained-share convention is a scenario bridge, "
                    "not proof that every contract receives identical ASC 606 "
                    "presentation. Document principal-versus-agent conclusions "
                    "by performance obligation, including control before "
                    "transfer, fulfillment responsibility, inventory risk, "
                    "and pricing discretion. An agent generally recognizes "
                    "its fee rather than underlying pass-through billings; "
                    "a principal may recognize gross revenue with corresponding "
                    "cost of service. Never substitute customer model spending, "
                    "carrier traffic value, or prepaid wallet deposits for "
                    "earned operator revenue. Preserve both the management "
                    "bridge and the reporting-policy reconciliation so buyers "
                    "can compare contracts consistently."
                ),
                (
                    "Close by service month, not by the date Stripe transfers "
                    "cash. Record unearned prepaid customer balances as contract "
                    "liabilities until the corresponding service is delivered, "
                    "subject to the applicable contract and accounting policy. "
                    "Accrue upstream GPU reservations and carrier usage in the "
                    "same period as delivery, including estimates for late "
                    "carrier records with subsequent true-ups. Track committed "
                    "but unused capacity separately so apparently healthy "
                    "customer cohorts cannot conceal idle reservations. Cohorts "
                    "should retain acquisition month, customer group, play "
                    "identifier, provider, model or destination, contract term, "
                    "and pricing version. Report gross billed usage, earned "
                    "revenue under the documented presentation policy, retained "
                    "contribution, service credits, refunds, chargebacks, and "
                    "support burden without netting away operational failures. "
                    "Reconcile opening wallet liability plus top-ups minus "
                    "earned consumption, refunds, and other supported adjustments "
                    "to the closing balance. Reconcile bank cash separately. "
                    "A buyer inheriting prepaid balances inherits a delivery "
                    "obligation, so sale proceeds cannot treat that cash as "
                    "automatically surplus. Keep customer acquisition expense "
                    "and recurring account service costs visible by cohort. "
                    "The founder signs a monthly close checklist covering "
                    "cutoff, accrual reversals, usage completeness, disputed "
                    "invoices, deferred balances, and comparison with each "
                    "canonical scenario's expense envelope."
                ),
                (
                    "Build transferability while contracts are still easy to "
                    "negotiate. Obtain written copyright assignments signed "
                    "by the rights owner for custom code and documentation "
                    "under 17 U.S.C. section 204(a); do not assume contractor "
                    "work automatically belongs to the company. Identify "
                    "preexisting contractor tools, third-party licenses, "
                    "model licenses, and open-source obligations separately "
                    "because an assignment cannot transfer rights the "
                    "contractor never owned. Customer and supplier agreements "
                    "should specify assignment, change-of-control treatment, "
                    "service credits, data handling, and responsibility for "
                    "prepaid balances. Review actual transfer mechanics for "
                    "numbers, messaging campaigns, address leases, and reserved "
                    "hardware instead of assuming credentials are the asset. "
                    "For voice operations, map the entity's actual role to "
                    "47 CFR sections 64.6301 and 64.6305, including applicable "
                    "STIR/SHAKEN and Robocall Mitigation Database duties. "
                    "Evaluate contribution and reporting obligations under "
                    "47 CFR sections 54.706 and 54.711 and current FCC Form "
                    "499 instructions. TCR registration is an industry "
                    "messaging requirement, not a replacement for statutory "
                    "calling or texting rules. Enforce authorization, AUP "
                    "screening, tenant isolation, and promised zero retention. "
                    "Provide buyers aggregated usage and redacted contracts "
                    "first; move restricted customer records only through "
                    "documented, authorized diligence procedures."
                ),
            ],
            "table": {
                "caption": "Accrual, Ownership, and Transfer Evidence Required for a Durable Book",
                "headers": [
                    "Record or control being maintained",
                    "Required content within the operating file",
                    "Monthly reconciliation or acceptance procedure",
                    "Buyer concern resolved by the evidence",
                ],
                "rows": [
                    [
                        "Gross billings and retained contribution scenario bridge",
                        "Show upstream charges and remaining expenses as separate layers",
                        "Recalculate all three cases using the canonical supplied amounts",
                        "Prevents pass-through activity from inflating the earnings narrative",
                    ],
                    [
                        "Contract-level principal-versus-agent assessment for each service obligation",
                        "Document control, fulfillment responsibility, inventory risk, and pricing discretion",
                        "Reassess presentation when material commercial contract terms change",
                        "Explains why recognized revenue can differ from billings",
                    ],
                    [
                        "Customer wallet liability and unsettled delivery exposure ledger",
                        "Preserve top-ups, earned consumption, refunds, and supported adjustments",
                        "Tie closing liability to transaction detail and service cutoff",
                        "Separates spendable operating cash from inherited service obligations",
                    ],
                    [
                        "Upstream reservation accruals and late carrier usage estimates",
                        "Identify committed capacity, delivered usage, estimates, and subsequent corrections",
                        "Match costs to service periods before evaluating cohort profitability",
                        "Exposes idle commitments and expenses hidden by invoice timing",
                    ],
                    [
                        "Customer cohort contribution and recurring support cost records",
                        "Retain acquisition month, related group, play, provider, and pricing",
                        "Trace credits and disputes back to original delivered usage",
                        "Distinguishes repeatable margins from promotional or concentrated revenue",
                    ],
                    [
                        "Signed contractor intellectual property and license ownership file",
                        "Separate assigned work from preexisting tools and third-party licenses",
                        "Verify signatures and repository history before accepting final deliverables",
                        "Establishes transferable rights without overstating ownership of dependencies",
                    ],
                    [
                        "Customer and supplier transfer terms with regulatory responsibility",
                        "Record assignment rights, change-of-control terms, filings, and balances",
                        "Test required notices and consent paths before marketing assets",
                        "Identifies contracts or registrations requiring action before transfer",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Scaling or Marketing the Book",
                "body": "Record a dated pass or an explicit blocking defect for each condition; evidence must be reproducible by someone outside the founder seat.",
                "items": [
                    "Reconcile the last three monthly closes from bank and wallet records through usage, upstream accruals, retained contribution, and owner profit, with every material adjustment explained.",
                    "Verify customer and upstream concentration are each at or below 25% under both defined measures; identify any launch exception rather than presenting it as diversified.",
                    "Demonstrate written IP assignments, organization-controlled accounts, tested recovery, and a contract-by-contract transfer map for GPU commitments, SIP numbers, messaging campaigns, and IPv4 leases.",
                    "Verify applicable voice-provider filings, Form 499 responsibilities, messaging registration, AUP screening, tenant isolation, and zero-retention behavior against actual entity roles and signed customer promises.",
                ],
            },
        },
        {
            "heading": "4. Value Transferable Earnings, Then Choose Exit or Distribution",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Price the business on an explicit earnings definition before "
                    "discussing a multiple. Owner net profit in the scorecard is "
                    "not automatically seller's discretionary earnings or adjusted "
                    "EBITDA. Build a bridge from reported results to normalized "
                    "earnings, identifying owner compensation already expensed, "
                    "genuine nonrecurring costs, recurring contractor work, and "
                    "the cost of replacing founder labor. Do not add back an "
                    "essential engineer merely because they invoice as a "
                    "contractor. For an illustrative Base acquisition, assume "
                    "the $189,000 owner profit requires an additional $90,000 "
                    "annual replacement manager cost that is not already "
                    "included in modeled expenses. Transferable earnings then "
                    "equal $99,000. Applying an underwriting range of 2.5 to "
                    "4.0 times those earnings implies $247,500 to $396,000 "
                    "of enterprise value. This is a negotiating model, not "
                    "an observed comparable-sales claim. If management cost "
                    "already sits in the expense ledger, deduct only the "
                    "incremental replacement requirement. A small owner-operated "
                    "buyer might instead analyze SDE and personally perform "
                    "the founder role, but their multiple and debt capacity "
                    "must match that labor assumption. Present both labor "
                    "bridges clearly rather than selecting whichever produces "
                    "the largest headline price. Substantiate every add-back "
                    "with invoices, payroll records, or contracts."
                ),
                (
                    "For the Scaled case, assume the $456,000 owner profit "
                    "still requires $120,000 of incremental founder replacement "
                    "cost beyond expenses already modeled. That leaves $336,000 "
                    "of illustrative transferable earnings. A 3.0 to 4.5 "
                    "times underwriting range produces $1,008,000 to $1,512,000 "
                    "of enterprise value. The higher range requires evidence "
                    "of renewal behavior, durable contribution after hardware "
                    "repricing, low concentration, transferable commitments, "
                    "clean ownership, and operation without founder escalation. "
                    "It does not follow simply from using H200 or B200 "
                    "hardware. Stress the book by reducing gross billings "
                    "10% while holding upstream commitments and other "
                    "modeled expenses fixed: Base owner profit falls from "
                    "$189,000 to $121,500, and Scaled falls from $456,000 "
                    "to $336,000 before additional replacement costs. These "
                    "are downside sensitivities, not revised canonical cases. "
                    "At Conservative scale, $27,000 owner profit supports "
                    "little independent management capacity; a buyer may "
                    "prefer a customer-book or asset purchase. Translate "
                    "enterprise value into expected proceeds by addressing "
                    "debt, cash treatment, working capital, prepaid obligations, "
                    "transaction costs, escrow, and contingent consideration. "
                    "Avoid counting wallet obligations twice if they are "
                    "already included in the agreed working-capital mechanism. "
                    "Value an earnout by its measurable collection conditions, "
                    "not its advertised maximum."
                ),
                (
                    "Run an exit rehearsal before hiring a broker. For 30 "
                    "days, have the service lead or designated backup conduct "
                    "daily operations while the founder performs only "
                    "documented commercial exceptions. Log every intervention "
                    "and repair the underlying dependency. Assemble a "
                    "controlled diligence room containing monthly accrual "
                    "statements, cohort contribution, concentration schedules, "
                    "signed contracts, IP assignments, incident summaries, "
                    "supplier commitments, regulatory responsibility records, "
                    "and tested recovery procedures. Use redacted configuration "
                    "inventories rather than live secrets, customer prompts, "
                    "call content, or unrestricted traffic records. Ask "
                    "prospective buyers to specify earnings treatment, "
                    "replacement staffing, working capital, transfer "
                    "conditions, and payment certainty in their proposals. "
                    "Compare expected net proceeds with retaining the "
                    "business, reserving capital for renewals and disputes, "
                    "and distributing only genuinely surplus cash. A durable "
                    "cash cow still needs refreshed GPU pricing, carrier "
                    "quality reviews, customer diversification, and contractor "
                    "backup; harvesting is not abandonment. Keep the same "
                    "weekly scorecard whether selling or holding. When the "
                    "pod can produce accurate books, enforce prepaid "
                    "exposure, and recover service without the founder, "
                    "the owner gains two credible options: accept a "
                    "well-supported transfer price or retain a controlled "
                    "stream of distributions. That operational choice is "
                    "more valuable than a multiple attached to unverifiable "
                    "gross traffic."
                ),
            ],
            "table": {
                "caption": "Illustrative Earnings Bridges and Buyer Underwriting, Not Market Comparables",
                "headers": [
                    "Valuation case or diligence issue",
                    "Explicit earnings assumption and calculation",
                    "Illustrative value or operating implication",
                    "Evidence required before accepting the assumption",
                ],
                "rows": [
                    [
                        "Conservative case with founder still performing essential work",
                        "$27,000 annual owner profit precedes any additional replacement requirement",
                        "Limited standalone management capacity may favor customer-book asset pricing",
                        "Document founder hours and actual transferable customer contribution",
                    ],
                    [
                        "Base case with incremental replacement manager expense assumed",
                        "$189,000 owner profit less $90,000 equals $99,000 transferable earnings",
                        "Applying 2.5-4.0 times produces $247,500-$396,000 illustrative enterprise value",
                        "Verify replacement cost is absent from existing modeled expenses",
                    ],
                    [
                        "Scaled case with incremental founder replacement expense assumed",
                        "$456,000 owner profit less $120,000 equals $336,000 transferable earnings",
                        "Applying 3.0-4.5 times produces $1,008,000-$1,512,000 illustrative enterprise value",
                        "Prove independent operations and sustainable earnings through monthly records",
                    ],
                    [
                        "Base downside with fixed commitments and ten-percent billing decline",
                        "$607,500 reduced billings less unchanged costs leaves $121,500 profit",
                        "Replacement staffing would further reduce the stressed transferable earnings",
                        "Check contract flexibility before assuming upstream costs decline proportionately",
                    ],
                    [
                        "Scaled downside with fixed commitments and ten-percent billing decline",
                        "$1,080,000 reduced billings less unchanged costs leaves $336,000 profit",
                        "Additional $120,000 replacement expense leaves $216,000 stressed transferable earnings",
                        "Demonstrate repricing resilience using actual renewals and supplier terms",
                    ],
                    [
                        "Enterprise value converted into expected seller cash proceeds",
                        "Adjust for debt, cash, working capital, costs, and contingencies",
                        "Prevent prepaid balances from being deducted through overlapping mechanisms",
                        "Reconcile purchase agreement definitions against the closing balance sheet",
                    ],
                    [
                        "Hold decision compared with a supported acquisition proposal",
                        "Compare expected net proceeds against risk-adjusted distributable cash flows",
                        "Reserve renewal commitments and service obligations before making distributions",
                        "Maintain tested backup staffing and current customer retention evidence",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A premium book is one whose margins, rights, and recovery procedures survive the founder leaving the room.",
    "diagram_id": "diag-06",
    "action_checklist": [
        "Assign P01-P15 to the founder, compute contractor, and telecom contractor; record a backup, economic unit, suspension procedure, and funded coverage window for every active play.",
        "Execute deliverable-based contractor agreements with bounded hours, reproducible QA acceptance, security duties, written IP assignments, and explicit treatment of preexisting tools.",
        "Publish the weekly scorecard from frozen usage evidence, including retained contribution, wallet exposure, service quality, contractor exceptions, and both 25% concentration tests.",
        "Close monthly accrual books that reconcile the three canonical cases, customer wallet liabilities, upstream commitments, cohort adjustments, and contract-specific revenue presentation.",
        "Test the five-person expansion against the $324,000 Scaled post-upstream expense envelope and verify that the second full-time seat removes documented founder workload.",
        "Rehearse founder absence for 30 days, assemble a redacted transferability file, and compare buyer offers using replacement-adjusted earnings and expected proceeds rather than gross billings.",
    ],
    "statutory_citations": [
        {
            "title": "17 U.S.C. section 204(a) — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": "Obtain written transfers signed by the rights owner for contractor-created code and documentation; distinguish assigned work from licensed dependencies.",
        },
        {
            "title": "47 CFR section 64.6301 — Caller ID authentication requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6301",
            "relevance": "Determine applicable caller ID authentication duties from the entity's actual voice-provider role and network arrangements before allocating contractor responsibilities.",
        },
        {
            "title": "47 CFR section 64.6305 — Robocall mitigation and certification",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6305",
            "relevance": "Maintain applicable mitigation plans, certifications, database filings, and provider-acceptance controls with named owners and retained evidence.",
        },
        {
            "title": "47 CFR section 54.706 — Contributions",
            "url": "https://www.ecfr.gov/current/title-47/section-54.706",
            "relevance": "Evaluate universal service contribution obligations using the services supplied, the entity's role, and applicable exceptions rather than assuming every reseller receives identical treatment.",
        },
        {
            "title": "47 CFR section 54.711 — Contributor reporting requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-54.711",
            "relevance": "Connect applicable contributor reporting duties to the accounting close and current FCC Form 499 instructions; maintain support for reported amounts.",
        },
        {
            "title": "47 CFR section 64.1200 — Restrictions on telemarketing, telephone solicitation, and facsimile advertising",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Map applicable calling and texting restrictions to customer use cases; industry messaging registration does not substitute for required authorization or other applicable restrictions.",
        },
        {
            "title": "47 U.S.C. section 222 — Privacy of customer information",
            "url": "https://www.law.cornell.edu/uscode/text/47/222",
            "relevance": "Where applicable, protect customer proprietary network information during operations and buyer diligence instead of disclosing unrestricted telecom customer records.",
        },
        {
            "title": "26 U.S.C. section 3121(d) — Definition of employee",
            "url": "https://www.law.cornell.edu/uscode/text/26/3121",
            "relevance": "Assess federal employment-tax classification using the actual working relationship; contractor labels and invoices alone do not establish independent status.",
        },
    ],
}
