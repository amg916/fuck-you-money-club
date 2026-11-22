from __future__ import annotations

CHAPTER_4 = {
    "id": "Q4",
    "chapter_id": "Q4",
    "chapter_number": 4,
    "question_number": 4,
    "slug": "startup-capital-lean-infrastructure-and-pre-flight-stack",
    "question_prompt": "How do you allocate startup capital ($10,000–$60,000 USD) and configure a lean, low-opex ($2,000–$14,000 USD/mo) production stack without wasting cash on bloated overhead?",
    "kicker": "Q4 / THE BIG MONEY PLAYBOOKS",
    "title": "Startup Capital, Lean Infrastructure & Pre-Flight Stack",
    "subtitle": "Prepaid Stripe Wallets, H100/H200/B200 Capacity, LiteLLM Routing, SIP Controls, and FCC Readiness on a Reserve-First Budget",
    "layout_template": "comparison_table",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #36, GPU Compute & Telecom Capacity Arbitrage, ranks #03 of 36 "
        "with a 94/100 Money-to-Manpower Score across 15 mapped plays. Start with "
        "customer-funded consumption, not speculative hardware commitments: retain "
        "55% of opening capital as working-capital reserve, isolate customer credits, "
        "and assemble twelve inexpensive infrastructure layers. Canonical annual "
        "owner profits are $27,000 Conservative, $189,000 Base, and $456,000 Scaled; "
        "their gross billings are distinct from the 65% retained contribution. "
        "This chapter separates recurring overhead from upstream consumption, "
        "prices a reproducible control plane, and defines launch evidence for GPU "
        "isolation, payment settlement, telecom identity, and recovery. Free-edge "
        "publishing supports acquisition; powered-land options remain capped "
        "research experiments rather than substitutes for contracted electricity."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross billings; $97,500 retained contribution at 65%",
            "note": "18% gross-basis net margin; $27,000 annual owner net profit; 27.69% retained margin; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$675,000",
            "context": "Annual gross billings; $438,750 retained contribution at 65%",
            "note": "28.0% gross-basis net margin; $189,000 annual owner net profit; 43.08% retained margin; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross billings; $780,000 retained contribution at 65%",
            "note": "38% gross-basis net margin; $456,000 annual owner net profit; 58.46% retained margin; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Ring-fence float before signing a single capacity commitment",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Allocate opening capital before selecting providers. The three budgets below "
                    "hold 55% in working-capital reserve: $5,500 from $10,000, $16,500 from "
                    "$30,000, and $33,000 from $60,000. These are alternative launch envelopes, "
                    "not additional funding layered onto one business. Reserve cash covers "
                    "settlement delays, refund exposure, expiring credits, and upstream invoices "
                    "arriving before cleared customer payments; it does not authorize speculative "
                    "GPU reservations. Keep customer prepaid balances in a separate ledger "
                    "liability and exclude those balances from freely deployable owner capital. "
                    "Use a business operating account, a separately tracked reserve account, "
                    "and provider-specific payment limits. Confirm the bank's deposit insurance "
                    "treatment and aggregate balances by legal ownership category rather than "
                    "assuming each account creates fresh coverage. Obtain an EIN directly from "
                    "the IRS, register the entity with its state, document beneficial ownership "
                    "for bank onboarding, and keep signed provider contracts under that entity. "
                    "Price technology errors-and-omissions and cyber coverage against actual "
                    "GPU hosting, messaging, and voice activities; inspect telecommunications "
                    "and infrastructure exclusions. At the smallest budget, narrow the product "
                    "to one prepaid inference route. If entity costs or insurance exceed the "
                    "allowance, reduce pilot scope instead of borrowing from the reserve."
                ),
                (
                    "Reconcile the canonical scorecard before describing anything as revenue. "
                    "Conservative gross billings of $150,000 less $52,500 upstream spend leave "
                    "$97,500 retained contribution; subtract $70,500 remaining expenses to reach "
                    "$27,000 owner profit. Base gross billings of $675,000 less $236,250 upstream "
                    "spend leave $438,750; subtract $249,750 to reach $189,000. Scaled gross "
                    "billings of $1,200,000 less $420,000 upstream spend leave $780,000; subtract "
                    "$324,000 to reach $456,000. Thus total monthly scorecard expenses average "
                    "$10,250, $40,500, and $62,000 respectively. The stated $2,000–$14,000 monthly "
                    "planning range cannot represent all-in expenditure in every scenario. "
                    "Treat it here as a controllable recurring-overhead envelope, with upstream "
                    "consumption and additional delivery expenses separately visible. Illustrative "
                    "monthly overhead targets of $2,000, $7,000, and $14,000 consume $24,000, "
                    "$84,000, and $168,000 annually, leaving $46,500, $165,750, and $156,000 "
                    "within the remaining-expense budgets for other modeled operating costs. "
                    "Do not add these costs twice. The 65% retained share is the scorecard's "
                    "economic presentation, not an automatic accounting election. Under ASC "
                    "606-10-55-36 through 55-40, evaluate control and principal-versus-agent "
                    "status for each performance obligation before selecting gross or net "
                    "recognized revenue. Merchant activity and customer model output never "
                    "become operator revenue merely because they traverse the platform."
                ),
                (
                    "Release launch spending in small, reversible increments across the expected "
                    "one-to-four-month path to a first deal. A $2,000 monthly fixed burn consumes "
                    "$8,000 over four months, so a $10,000 launch cannot simultaneously spend "
                    "that amount and preserve its reserve without collections or additional "
                    "capital. Keep the pre-revenue control plane below the operating envelope, "
                    "defer contractor retainers, and require a dated cash forecast before "
                    "expanding availability. For an illustrative GPU offer, a $2.40 hourly "
                    "upstream commitment sold at $4.00 per occupied hour needs 60% utilization "
                    "just to cover capacity; payment fees and support raise the actual threshold. "
                    "A 720-hour month costs $1,728 whether customers consume it or not. At "
                    "50% occupancy, billings reach only $1,440, producing a $288 capacity loss "
                    "before overhead. Purchase hourly capacity first, measure paid utilization, "
                    "and negotiate reservations only after signed demand covers the downside. "
                    "Keep H100, H200, and B200 rate cards separate because memory capacity, "
                    "interconnect topology, and workload performance change effective output "
                    "cost. Finance no annual SaaS contract from anticipated savings alone. "
                    "Track settled cash, wallet liabilities, refundable provider deposits, "
                    "nonrefundable setup fees, and committed capacity separately in the weekly "
                    "thirteen-week forecast; each has a different recovery path."
                ),
            ],
            "table": {
                "caption": "Reserve-First Startup Allocation: Three Complete, Non-Additive Capital Envelopes",
                "headers": [
                    "Capital allocation and permitted operating purpose",
                    "Ten-thousand-dollar launch allocation",
                    "Thirty-thousand-dollar launch allocation",
                    "Sixty-thousand-dollar launch allocation",
                ],
                "rows": [
                    [
                        "Working-capital reserve remains outside discretionary purchasing authority",
                        "$5,500 reserve protects settlement delays and refund exposure",
                        "$16,500 reserve protects larger invoices and settlement interruptions",
                        "$33,000 reserve protects expanded commitments and customer reversals",
                    ],
                    [
                        "Entity, banking, insurance, and contract setup receive explicit ceilings",
                        "$1,500 funds formation, account setup, and initial coverage",
                        "$3,500 funds broader coverage and targeted contract review",
                        "$6,500 funds expanded coverage and multi-product contracting work",
                    ],
                    [
                        "Control-plane setup purchases reproducibility instead of elaborate dashboards",
                        "$500 funds minimal hosting, backups, and initial configuration",
                        "$1,500 funds tested automation and documented recovery setup",
                        "$3,000 funds isolated environments and stronger recovery tooling",
                    ],
                    [
                        "Metered delivery pilots buy evidence before recurring capacity",
                        "$2,000 funds tightly capped customer-linked GPU consumption tests",
                        "$6,000 funds multiple paid workload and carrier trials",
                        "$12,000 funds measured regional capacity and failover trials",
                    ],
                    [
                        "Demand testing and diligence remain capped experimental expenses",
                        "$500 funds acquisition tests without speculative land options",
                        "$2,500 funds measured acquisition and bounded site diligence",
                        "$5,500 funds expanded acquisition experiments and contingent diligence",
                    ],
                ],
            },
        },
        {
            "heading": "2. Assemble twelve priced layers without confusing software with capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build the control plane around twelve explicit layers, not twelve compulsory "
                    "subscriptions. The matrix uses exact reference rate pins and license prices "
                    "for reproducible budgeting; these are planning inputs, not verified current "
                    "checkout quotes. Confirm currency, region, included quotas, tax, and commercial "
                    "eligibility before purchase, then record the accepted rate card with its "
                    "effective date. Cloudflare Workers Paid at a $5 monthly minimum, a "
                    "DigitalOcean Basic droplet at $6 monthly, Supabase Pro from $25 monthly "
                    "for the reference organization configuration, and GitHub Team at $4 per "
                    "user monthly produce a $44 baseline for two GitHub seats. That subtotal "
                    "excludes taxes, excess usage, additional database compute, paid messaging, "
                    "GPU capacity, and payment processing. Cloudflare R2 Standard storage at "
                    "$0.015 per GB-month makes 100 billable GB cost $1.50 before operations "
                    "and applicable allowances. Keep synthetic checks and build logs small "
                    "enough for the chosen observability tier. A cheap control plane is not "
                    "a highly available service by itself: the single droplet needs reproducible "
                    "configuration, tested restoration, and an explicit recovery objective. "
                    "Route synchronous inference outside that small host. Its job is admission, "
                    "accounting coordination, and configuration delivery, not pretending that "
                    "one gigabyte of memory can run production model serving."
                ),
                (
                    "Treat the Stripe balance, internal wallet, and upstream consumption meter "
                    "as separate systems reconciled by immutable identifiers. At the reference "
                    "US domestic-card rate of 2.9% plus $0.30, a $100 top-up costs $3.20 "
                    "and a $10 top-up costs $0.59. Encourage sensible minimum purchases rather "
                    "than absorbing repeated fixed charges on tiny wallets. Fees vary by "
                    "payment method, geography, currency conversion, and dispute activity, so "
                    "save the applicable processor schedule. Credit a wallet from authenticated "
                    "payment events with idempotent processing, not from a browser success "
                    "redirect. Availability for delivery must also reflect settlement and risk "
                    "policy; a successful charge can still reverse. Reserve an estimated "
                    "maximum request cost atomically before dispatch, settle the actual debit "
                    "after completion, and release unused reservations. LiteLLM may coordinate "
                    "model routes, but the authoritative ledger belongs in transactional storage. "
                    "vLLM token counters describe model work; NVIDIA DCGM describes hardware "
                    "behavior. Neither independently proves a customer invoice. Join request "
                    "identifier, tenant identifier, selected model, token counts, elapsed GPU "
                    "time, and price version into a billing event. Reconcile provider invoices "
                    "daily and investigate discrepancies before increasing wallet limits or "
                    "opening another region. Preserve credit adjustments as compensating entries "
                    "rather than editing historical usage."
                ),
                (
                    "Configure tenant boundaries before accepting arbitrary workloads. For managed "
                    "inference, restrict the execution environment to approved serving images, "
                    "disable unnecessary outbound access, scope object-store credentials, and "
                    "separate customer artifacts by authorization policy. For customer-supplied "
                    "containers, use dedicated hosts or an isolation design that has actually "
                    "been assessed; MIG partitions GPU resources but does not by itself "
                    "establish a complete hostile-tenant security boundary. Test GPU memory "
                    "cleanup, host access restrictions, and credential revocation between leases. "
                    "Enterprise zero-data-retention promises require coordinated settings across "
                    "LiteLLM callbacks, upstream model providers, exception reporters, tracing, "
                    "support exports, and backups. Retain necessary billing metadata without "
                    "retaining prompts, responses, audio, or message bodies where the agreement "
                    "excludes them. WireGuard supplies an inexpensive administrative tunnel, "
                    "not identity lifecycle management; distribute individual keys and revoke "
                    "departures promptly. Keep customer traffic off the administrative subnet. "
                    "On telecom routes, OpenSIPS admission rules should enforce authorized "
                    "destinations, concurrency, maximum call duration, and spend ceilings before "
                    "least-cost routing selects a carrier. A cheaper route that fails identity "
                    "requirements, answer quality, or contracted destination restrictions is "
                    "not an eligible substitute. Meter IPv4 leases by assigned address and "
                    "contract period, verify delegation rights, and do not count address "
                    "inventory as recognized sales before the promised service is delivered."
                ),
            ],
            "table": {
                "caption": "Twelve-Layer Infrastructure Matrix: Exact Reference Rate Pins, Functions, and Lean Alternatives",
                "headers": [
                    "Named layer and vendor pricing reference",
                    "Production role and enforceable operating boundary",
                    "Cost calculation and purchasing discipline",
                    "Cheaper implementation and explicit operational tradeoff",
                ],
                "rows": [
                    [
                        "Edge delivery: Cloudflare Pages Free, Workers Paid $5 monthly minimum",
                        "Serve static acquisition properties and bounded admission endpoints",
                        "Budget $5 minimum; separately meter requests and CPU overages",
                        "Use Pages static artifacts only when dynamic execution is unnecessary",
                    ],
                    [
                        "Control host: DigitalOcean Basic, one GiB, $6 monthly reference",
                        "Run lightweight coordination services outside the GPU execution path",
                        "One reference droplet costs $72 annually before added services",
                        "Share an existing authorized host while accepting weaker fault separation",
                    ],
                    [
                        "Wallet database: Supabase Pro, $25 monthly starting reference",
                        "Persist transactional balances, price versions, and idempotent billing events",
                        "Budget $300 annually before added compute and usage charges",
                        "Self-host PostgreSQL for zero license cost with added maintenance",
                    ],
                    [
                        "Artifact storage: Cloudflare R2 Standard, $0.015 per GB-month reference",
                        "Store approved artifacts and encrypted recovery exports without prompts",
                        "One hundred billable GB costs $1.50 before request charges",
                        "Retain smaller artifacts locally while preserving independent recovery copies",
                    ],
                    [
                        "Code delivery: GitHub Team, $4 per user monthly reference",
                        "Protect deployment branches and record reproducible infrastructure changes",
                        "Two seats cost $8 monthly before extra Actions consumption",
                        "Use GitHub Free where required private-repository controls remain sufficient",
                    ],
                    [
                        "Administrative network: WireGuard self-hosted, $0 software license charge",
                        "Restrict management access through individual revocable peer identities",
                        "Budget existing host resources and operator key-management time",
                        "Use OpenSSH tunnels for fewer endpoints with explicit access records",
                    ],
                    [
                        "Observability: Grafana Cloud Free, $0 subscription within plan limits",
                        "Alert on wallet failures, latency, utilization, and carrier anomalies",
                        "Enforce retention and ingestion ceilings before exhausting free allocations",
                        "Run Prometheus locally with less convenient independent incident visibility",
                    ],
                    [
                        "Collections: Stripe standard US domestic cards, 2.9% plus $0.30",
                        "Collect prepaid funds and reconcile signed events into liabilities",
                        "A $100 charge incurs $3.20 under this reference schedule",
                        "Use quoted bank-transfer rails when reconciliation and settlement fit",
                    ],
                    [
                        "Inference routing: LiteLLM open-source edition, $0 software license charge",
                        "Choose eligible providers using price, latency, and retention constraints",
                        "Pay underlying providers separately and cap retries per request",
                        "Use one provider adapter until routing complexity earns savings",
                    ],
                    [
                        "GPU serving: vLLM and NVIDIA DCGM, $0 software license charges",
                        "Serve approved models and correlate usage with hardware telemetry",
                        "Budget actual GPU leases separately from free serving software",
                        "Start with metered inference before administering dedicated GPU capacity",
                    ],
                    [
                        "SIP routing: OpenSIPS self-hosted, $0 software license charge",
                        "Apply destination policy and bounded least-cost routing between carriers",
                        "Carrier commitments and termination rates require separate signed schedules",
                        "Use one contracted carrier initially and retain portable routing configuration",
                    ],
                    [
                        "Messaging: Twilio US long-code SMS, $0.0083 per segment reference",
                        "Send registered business messaging with tenant-specific throughput limits",
                        "Ten thousand segments cost $83 before carrier and registration fees",
                        "Defer messaging entirely until contracted demand supports onboarding expenses",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Spend on measurements that prevent the next expensive surprise",
                "body": "A lean stack earns its margin through narrow routing eligibility, bounded exposure, and reliable evidence rather than a large subscription inventory.",
                "items": [
                    "Benchmark a fixed representative prompt set on each H100, H200, and B200 offer; compare dollars per accepted output token at the required latency, not advertised GPU-hour prices.",
                    "Put a maximum retry budget beside each LiteLLM route. A timeout followed by a second provider can create two upstream charges while the customer sees one response.",
                    "Reconcile SIP call-detail records by carrier call identifier and billing increment. A sixty-second minimum can erase the apparent advantage of a cheaper per-minute rate.",
                    "Keep signed static build artifacts ready for direct upload. A cloud build outage should delay publishing, not force an emergency paid build subscription.",
                ],
            },
        },
        {
            "heading": "3. Use free-edge acquisition and powered-land research as bounded options",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play serverless_edge_free_tier_empire_hosting belongs on the "
                    "acquisition side of this business, not inside the delivery margin "
                    "calculation. Publish useful static GPU price explainers, latency calculators, "
                    "regional capacity directories, and telecom comparison tools as pre-rendered "
                    "HTML and JSON. At $0.00 incremental hosting per eligible property, "
                    "1,000 static properties have a $0 hosting line only while aggregate "
                    "account limits, permitted commercial use, bandwidth, and deployment "
                    "constraints all remain satisfied. Domains, editorial work, maintenance, "
                    "and dynamic APIs still cost money. Prefer 1,000 logical tools or "
                    "directory pages within a manageable set of sites rather than assuming "
                    "a vendor permits 1,000 independent projects. Cloudflare Pages, Workers, "
                    "GitHub Pages, Vercel, Netlify, and Supabase have different product limits "
                    "and commercial-use rules; their free allocations are not interchangeable. "
                    "In particular, do not select a personal-use plan for a commercial "
                    "brokerage or use GitHub Pages as unrestricted commercial application "
                    "hosting. Each property needs accurate source attribution, a useful "
                    "calculator or original comparison, and a clear conversion path. "
                    "Measure qualified enquiries and settled customer revenue by property "
                    "cohort. A thousand near-duplicate pages that generate support noise "
                    "and no paid accounts are overhead, even when the hosting invoice "
                    "remains zero."
                ),
                (
                    "Model acquisition economics with cash rather than page counts. Suppose "
                    "100 static tools each receive 200 qualified monthly visits, producing "
                    "20,000 visits. At a 0.5% enquiry rate, that yields 100 enquiries; "
                    "at a 10% paid conversion rate, it produces ten customers. If each "
                    "customer buys $100 of initial usage, gross billings total $1,000 "
                    "and the canonical retained-share assumption yields $650 before other "
                    "expenses. Ten domestic-card charges at the reference Stripe rate cost "
                    "$32, leaving $618 before content, support, and overhead. These are "
                    "illustrative conversion assumptions, not additions to the annual "
                    "scorecard scenarios. Spending $900 to create that cohort would not "
                    "recover its cost from those first purchases alone. Record repeat "
                    "purchases before claiming a favorable acquisition payback. If build "
                    "minutes become restrictive, pre-build locally or on authorized "
                    "self-hosted runners and upload compiled artifacts through the supported "
                    "deployment API. If traffic exceeds an allocation, consolidate sites, "
                    "cache immutable assets, or purchase the appropriate plan from realized "
                    "margin. Never multiply accounts to bypass vendor limits. Keep forms "
                    "behind rate limits and challenge suspicious submissions; static hosting "
                    "does not make an exposed lead endpoint immune to abuse or "
                    "unbounded downstream API charges."
                ),
                (
                    "The second mapped play, ferc_grid_interconnection_queue_land_speculation, "
                    "requires an even tighter capital boundary. Overlay public ISO or RTO "
                    "interconnection queues with parcel boundaries, zoning, substation locations, "
                    "flood maps, and utility service territories to identify research candidates. "
                    "FERC interconnection reforms under Order No. 2023 and 18 CFR 35.28 "
                    "address generator interconnection processes; a nearby generator queue "
                    "entry does not establish deliverable electric service for a data center. "
                    "Request the serving utility's actual load-service process, capacity "
                    "study requirements, upgrade allocation, deposit schedule, and energization "
                    "timeline. For an illustrative $500 nonrefundable, ninety-day option "
                    "premium plus $300 of capped desktop diligence, the at-risk outlay "
                    "is $800, provided the signed agreement creates no additional mandatory "
                    "payments or purchase obligation. That experiment fits inside the "
                    "$2,500 or $5,500 diligence envelopes, not the $500 smallest-launch "
                    "allowance and never the reserve. Verify title, access, option assignability, "
                    "and termination mechanics before paying. State real-estate licensing "
                    "rules can differ between acquiring an interest for the entity and "
                    "brokering another owner's transaction. If utility evidence or land-use "
                    "feasibility fails, let the contingent option lapse or assess an "
                    "independently viable use. Never advertise secured power based on "
                    "distance to a substation or a queue spreadsheet."
                ),
            ],
            "table": {
                "caption": "Mapped-Play Experiments: Bounded Unit Economics and Explicit Failure Responses",
                "headers": [
                    "Experiment and precise scope of operator work",
                    "Illustrative unit calculation and capital boundary",
                    "Evidence required before increasing committed spending",
                    "Fallback that preserves cash and contractual accuracy",
                ],
                "rows": [
                    [
                        "serverless_edge_free_tier_empire_hosting creates useful static acquisition tools within permitted allocations",
                        "One thousand eligible properties multiply $0 incremental hosting only",
                        "Document account limits, commercial eligibility, traffic, and deployment quotas",
                        "Consolidate logical properties before paying for broader hosting capacity",
                    ],
                    [
                        "Static acquisition cohort measures customers rather than indexed pages",
                        "Twenty thousand visits yield ten customers under stated assumptions",
                        "Track settled purchases and repeat usage against content costs",
                        "Retire unproductive pages and retain tools producing qualified enquiries",
                    ],
                    [
                        "Precompiled publishing removes unnecessary cloud build-minute consumption from experiments",
                        "Ten thousand SMS segments are unrelated to static hosting costs",
                        "Separate hosting, messaging, domains, and editorial expense by cohort",
                        "Upload locally built artifacts without bypassing provider account limits",
                    ],
                    [
                        "ferc_grid_interconnection_queue_land_speculation researches contingent sites without representing secured power",
                        "$500 option premium plus $300 diligence limits initial exposure",
                        "Obtain utility process evidence and independently verify parcel constraints",
                        "Allow the option to expire when required evidence fails",
                    ],
                    [
                        "Powered-land research distinguishes generator queues from customer load service",
                        "An $800 experiment stays outside the protected reserve allocation",
                        "Check assignability, access, title, zoning, and additional payment obligations",
                        "Evaluate independent land uses without implying available electrical capacity",
                    ],
                ],
            },
        },
        {
            "heading": "4. Prove money movement, isolation, carrier standing, and recovery before launch",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Prepare a launch evidence packet that another operator can reproduce. "
                    "Run a real low-value top-up, deliver a bounded workload, reconcile "
                    "the provider charge, issue a partial credit, and verify that the "
                    "wallet and accounting export remain balanced. Replay the processor "
                    "event to prove idempotency; submit simultaneous requests to prove "
                    "that one balance cannot fund duplicate reservations. Disconnect "
                    "the metering path and confirm that new consumption stops rather "
                    "than becoming unpriced service. Restore the database into an isolated "
                    "environment and compare wallet totals, request identifiers, and "
                    "unsettled reservations. Define a recovery-point objective for acknowledged "
                    "billing events and show how an append-only event journal closes "
                    "the gap after restoring a snapshot. Exercise a compromised tenant "
                    "key, an exhausted balance, a provider timeout, and an attempted "
                    "cross-tenant object read. Confirm that security events reach someone "
                    "who can revoke access without logging customer payloads. Assign "
                    "incident ownership across the canonical teams: one full-time operator "
                    "plus two contractors in Conservative and Base, and two full-time "
                    "operators plus three contractors at Scaled. Contractor count does "
                    "not establish round-the-clock coverage. Publish support hours and "
                    "buy an explicit on-call arrangement only when the delivery budget "
                    "and customer commitments justify it."
                ),
                (
                    "Telecom launch requirements depend on the service actually provided. "
                    "Classify the entity's role as reseller, voice service provider, "
                    "gateway provider, messaging intermediary, or infrastructure supplier "
                    "before choosing filings and contracts. Under 47 CFR 64.6301 and "
                    "64.6305, determine applicable caller-ID authentication, robocall "
                    "mitigation, and Robocall Mitigation Database certification duties; "
                    "buying a trunk does not automatically discharge the downstream "
                    "entity's obligations. Confirm provider standing and the circumstances "
                    "in which traffic must be blocked. Evaluate FCC Form 499-A "
                    "registration and reporting using the service model and current "
                    "instructions; a contribution exemption does not automatically remove "
                    "every filing duty. For US application-to-person messaging over "
                    "ten-digit long codes, complete the carrier-required brand and "
                    "campaign registration process through the relevant provider and "
                    "The Campaign Registry ecosystem. Registration is distinct from "
                    "the TCPA restrictions in 47 U.S.C. 227 and implementing rules. "
                    "Collect evidence of authorized messaging purposes, implement "
                    "applicable opt-out handling, and verify number ownership. For "
                    "voice, screen customer identity, destination patterns, and sudden "
                    "concurrency changes. For GPU access, screen intended workloads "
                    "against the upstream acceptable-use policy and investigate abrupt "
                    "mining-like consumption. Apply proportional review and documented "
                    "suspension rules rather than assuming every high-utilization workload "
                    "is abusive."
                ),
                (
                    "Release production with a customer-specific exposure ceiling, not an "
                    "unlimited public signup switch. An illustrative first account with "
                    "$500 prepaid credit, a $100 daily consumption ceiling, and a "
                    "$25 maximum in-flight reservation bounds several failure modes, "
                    "but those controls do not eliminate payment reversals or provider "
                    "billing delay. Calculate maximum loss as outstanding upstream "
                    "consumption plus irreversible commitments plus refund exposure, "
                    "less reliably recoverable funds; do not subtract the entire "
                    "wallet liability as though it were owner cash. Reconcile every "
                    "day during the pilot and review route profitability weekly. "
                    "For SIP, test destination blocking and immediate concurrency "
                    "reduction before allowing international traffic. For SMS, bill "
                    "segments rather than visible messages and test Unicode expansion. "
                    "For inference, test streamed responses, disconnects, retries, and "
                    "output-token caps. For leased IPv4 capacity, retain evidence "
                    "of authorization, abuse contacts, and revocation procedures. "
                    "Increase limits only after settled collections, accepted invoices, "
                    "and observed demand support the change. If any readiness "
                    "check fails, keep the unaffected static acquisition layer "
                    "online while disabling the implicated paid service. That "
                    "separation preserves useful demand generation without selling "
                    "capacity the operator cannot safely meter, fund, or restore. "
                    "The reserve is a shock absorber, not permission to launch "
                    "with unresolved accounting defects."
                ),
            ],
            "table": {
                "caption": "Pre-Flight Evidence Matrix: Observable Tests, Ownership, and Stop Conditions",
                "headers": [
                    "Readiness domain and accountable operational owner",
                    "Required evidence produced by a reproducible test",
                    "Acceptance condition tied to bounded financial exposure",
                    "Immediate response when the condition is unmet",
                ],
                "rows": [
                    [
                        "Operator owns settlement, wallet liabilities, and customer credit accounting",
                        "Signed event replay and concurrent spending tests preserve balances",
                        "Exactly one credit and bounded reservations survive duplicate delivery",
                        "Disable new paid requests while repairing ledger reconciliation",
                    ],
                    [
                        "Infrastructure contractor owns tenant isolation and provider retention settings",
                        "Cross-tenant access fails and payload logging remains disabled",
                        "Approved workloads execute without exposing another customer's artifacts",
                        "Quarantine the affected execution pool and revoke exposed credentials",
                    ],
                    [
                        "Telecom specialist owns service classification and applicable carrier evidence",
                        "Document applicable filings, provider standing, and campaign registration",
                        "Each enabled route satisfies its applicable identity and operating requirements",
                        "Disable affected routes without interrupting independently qualified services",
                    ],
                    [
                        "Operator owns cash forecasting and upstream commitment authorization",
                        "Thirteen-week forecast includes settlement stress and provider invoice timing",
                        "Protected reserve remains at least half of opening capital",
                        "Reduce capacity commitments and defer discretionary acquisition spending",
                    ],
                    [
                        "Infrastructure contractor owns restoration and billing-event recovery exercises",
                        "Isolated restore reproduces balances and resolves outstanding reservations",
                        "Measured recovery meets documented customer service and accounting objectives",
                        "Keep launch limited until recovery evidence is repeatable",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four proofs required before increasing customer exposure",
                "body": "Keep evidence with the deployment version, price schedule, provider contract, and named operator responsible for each test.",
                "items": [
                    "Cash proof: demonstrate a settled collection, balanced wallet liability, bounded refund exposure, and a stress forecast preserving at least 50% of opening capital.",
                    "Metering proof: replay payment events and concurrent requests; verify exact-once ledger effects, capped reservations, and suspension when metering becomes unavailable.",
                    "Service proof: demonstrate tenant isolation and retention settings, then document the applicable telecom filings, provider standing, and messaging registrations for enabled products.",
                    "Recovery proof: restore the ledger and configuration, reconcile post-snapshot events, revoke a tenant credential, and stop an active route without manual database edits.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the launch envelope",
                    "action": "Select one capital column and segregate its 55% reserve.",
                    "detail": "Record authorized spending owners, customer-credit liabilities, provider deposits, and a thirteen-week forecast before purchasing subscriptions or capacity.",
                },
                {
                    "step": 2,
                    "title": "Deploy the minimum reproducible stack",
                    "action": "Configure the twelve layers while purchasing only the services required by the first offer.",
                    "detail": "Store accepted price schedules, infrastructure configuration, retention settings, secrets ownership, and restoration instructions in the controlled project repository.",
                },
                {
                    "step": 3,
                    "title": "Run an end-to-end paid rehearsal",
                    "action": "Collect a small payment, reserve wallet funds, execute work, reconcile costs, and process an adjustment.",
                    "detail": "Repeat events, interrupt the provider, exhaust the wallet, test tenant boundaries, and restore the ledger before increasing any spending limit.",
                },
                {
                    "step": 4,
                    "title": "Launch with bounded exposure",
                    "action": "Enable one qualified customer cohort with explicit daily and in-flight limits.",
                    "detail": "Review daily settlement and consumption evidence, expand only after actual route margins and cash timing support the additional commitments, and keep failed products disabled.",
                },
            ],
        },
    ],
    "pull_quote": "Reserve cash before reserving capacity, and sell only what you can meter, fund, isolate, and restore.",
    "diagram_id": "diag-07",
    "action_checklist": [
        "Choose the $10,000, $30,000, or $60,000 launch envelope and segregate its 55% working-capital reserve before approving discretionary purchases.",
        "Reconcile all three scorecard cases from gross billings through 35% upstream costs, 65% retained contribution, remaining expenses, and exact annual owner profit.",
        "Confirm the twelve infrastructure rate pins against actual checkout terms and signed carrier schedules; record limits, effective dates, and commercial eligibility.",
        "Implement transactional prepaid wallets with authenticated events, idempotent credits, atomic usage reservations, daily reconciliation, and fail-closed spending controls.",
        "Document tenant isolation, enterprise retention settings, applicable FCC obligations, carrier standing, and brand or campaign registration for every enabled product.",
        "Complete a paid rehearsal and isolated recovery test; launch static acquisition separately and keep powered-land experiments outside the protected reserve.",
    ],
    "statutory_citations": [
        {
            "title": "47 CFR 64.6301 — Caller ID authentication",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6301",
            "relevance": "Determine applicable caller-ID authentication duties from the entity's actual voice-service role and supported network technology.",
        },
        {
            "title": "47 CFR 64.6305 — Robocall mitigation and certification",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6305",
            "relevance": "Evaluate applicable mitigation plans, database certifications, provider-status checks, and restrictions on accepting traffic.",
        },
        {
            "title": "47 CFR 54.706 — Contributions",
            "url": "https://www.ecfr.gov/current/title-47/section-54.706",
            "relevance": "Assess federal universal-service contribution treatment for the actual telecommunications and interconnected voice activities offered.",
        },
        {
            "title": "47 CFR 54.711 — Contributor reporting requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-54.711",
            "relevance": "Map applicable contributor reporting duties to current FCC Form 499 instructions rather than assuming a carrier handles every reseller obligation.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Evaluate restrictions governing automated calling and messaging separately from carrier-required brand and campaign registration.",
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Implement applicable calling, messaging, revocation, and do-not-call controls for the specific traffic and customer use case.",
        },
        {
            "title": "18 CFR 35.28 — Non-discriminatory open access transmission tariff",
            "url": "https://www.ecfr.gov/current/title-18/section-35.28",
            "relevance": "Interpret generator-interconnection process evidence without treating a queue entry or nearby substation as proof of available data-center load service.",
        },
        {
            "title": "12 CFR 330.11 — Accounts of a corporation, partnership, or unincorporated association",
            "url": "https://www.ecfr.gov/current/title-12/section-330.11",
            "relevance": "Evaluate business deposit coverage by legal ownership category instead of assuming separate operating and reserve accounts create separate coverage limits.",
        },
    ],
}
