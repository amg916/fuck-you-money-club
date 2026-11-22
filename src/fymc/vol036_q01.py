from __future__ import annotations

CHAPTER_1 = {
    "id": "Q1",
    "chapter_id": "Q1",
    "chapter_number": 1,
    "question_number": 1,
    "slug": "gpu-compute-telecom-capacity-arbitrage-business-model",
    "question_prompt": "What exactly is gpu compute & telecom capacity arbitrage, how is real operator revenue recognized vs underlying asset/client GMV, and what separates durable small-team moats from fragile beginner hype?",
    "kicker": "Q1 / THE BIG MONEY PLAYBOOKS",
    "title": "What Exactly Is GPU Compute & Telecom Capacity Arbitrage?",
    "subtitle": "H100/H200/B200 Reservations, vLLM Metering, Wholesale SIP, Registered 10DLC, and ASC 606 Principal-versus-Agent Economics",
    "layout_template": "opportunity_overview",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #36, GPU Compute & Telecom Capacity Arbitrage, ranks #03 of 36 "
        "with a 94/100 Money-to-Manpower Score. The operator converts authorized "
        "wholesale GPU reservations, inference endpoints, and carrier capacity into "
        "metered services with tighter routing, collection, and support economics. "
        "This chapter maps 15 plays, separating the core capacity business from "
        "adjacent commercial-card rebate distribution. Canonical annual owner profits "
        "are $27,000 Conservative, $189,000 Base, and $456,000 Scaled. Gross service "
        "billings are not customer merchandise volume, and the modeled 65% retained "
        "share is not an automatic accounting conclusion. Durable operators own "
        "workload qualification, tenant isolation, prepaid collection, carrier "
        "permissions, and auditable unit economics; fragile operators merely rent "
        "expensive hardware and advertise an attractive hourly price."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross service billings; $97,500 retained contribution",
            "note": "18% gross-basis net margin; $27,000 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$675,000",
            "context": "Annual gross service billings; $438,750 retained contribution",
            "note": "28.0% gross-basis net margin; $189,000 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross service billings; $780,000 retained contribution",
            "note": "38% gross-basis net margin; $456,000 owner profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Sell a Measured Service, Not a Speculative Hardware Position",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "GPU compute and telecom capacity arbitrage buys an explicitly "
                    "resalable input under one pricing schedule and sells a defined "
                    "service under another. The input might be an eight-GPU H100 "
                    "server, an H200 reservation, a qualified B200 deployment, "
                    "wholesale SIP termination, registered messaging throughput, "
                    "or an IPv4 lease with documented usage rights. The customer "
                    "buys completed inference, GPU time, delivered message segments, "
                    "connected voice minutes, or address availability, rather than "
                    "ownership of the underlying infrastructure. The spread exists "
                    "because the operator aggregates demand, absorbs commitment "
                    "risk, meters accurately, and solves integration problems that "
                    "individual buyers cannot justify solving themselves. This is "
                    "not riskless arbitrage: reservation invoices continue during "
                    "idle periods, model quality varies across endpoints, and "
                    "carriers change destination rates. Start with one workload "
                    "class and one upstream agreement whose resale, support, "
                    "geographic, and suspension clauses match the downstream offer. "
                    "An advertised cloud price is a sourcing lead, not permission "
                    "to subdivide an account. Maintain a service specification "
                    "covering model version, quantization, latency, concurrency, "
                    "data handling, billing increments, and credit remedies. That "
                    "specification is the product; the GPU or trunk is its input. "
                    "A signed customer order should make that distinction explicit "
                    "before any noncancelable capacity purchase."
                ),
                (
                    "The central mapped play, gpu_reserved_to_spot_inference_slicing, "
                    "combines reserved hardware with isolated inference and "
                    "interruptible queues, while keeping authorized telecom resale "
                    "as a separate service ledger. Consider an illustrative "
                    "eight-GPU reservation costing $2 per available GPU-hour. "
                    "Across 720 hours, the commitment is $11,520. Selling 80% "
                    "of 5,760 available GPU-hours at $5 generates $23,040; "
                    "allocating another $2,880 to service operations leaves "
                    "$8,640, or 37.5% of billings. This illustrates the play's "
                    "35%–55% target net spread, not a replacement for the "
                    "chapter's canonical scenarios. At 50% utilization, receipts "
                    "fall to $14,400 and the same costs consume every dollar. "
                    "Use vLLM for compatible serving workloads, LiteLLM for "
                    "policy-based endpoint selection, and NVIDIA DCGM for hardware "
                    "telemetry. None independently supplies a complete billing or "
                    "security boundary. Benchmark accepted output, model quality, "
                    "memory pressure, and tail latency before selling fractional "
                    "capacity. Where supported and qualified, hardware partitioning "
                    "can improve isolation, but separate credentials, networks, "
                    "storage, and lifecycle controls remain necessary. Suspend "
                    "abusive workloads, preserve required evidence, reroute only "
                    "compliant traffic to authorized alternatives, and renegotiate "
                    "excess reservations before idle capacity becomes an existential "
                    "cash drain. Never quietly substitute a weaker model merely "
                    "to protect the advertised spread."
                ),
                (
                    "Five operator archetypes clarify what a small team actually "
                    "does. A reservation slicer owns scheduling and utilization; "
                    "an inference broker owns quality-aware routing and application "
                    "integration; a managed endpoint operator sells deployment "
                    "reliability; a telecom reseller owns route economics and "
                    "traffic legitimacy; an address-capacity broker owns usage "
                    "rights, registry coordination, and reputation recovery. These "
                    "roles can share invoicing and observability without sharing "
                    "all permissions or statutory duties. A developer using "
                    "Twilio messaging is not automatically a wholesale voice "
                    "provider, and an IPv4 lessor does not become a carrier merely "
                    "by leasing addresses. Contract the actual activity instead "
                    "of adopting every obligation associated with the word telecom. "
                    "The supplied scorecard allocates 24 points to revenue "
                    "potential, 24 to margin potential, 20 to team efficiency, "
                    "13 to startup accessibility, and 13 to automation, totaling "
                    "94. Those weights favor repeatable metering and collection, "
                    "not ownership of racks. Budget $10,000–$60,000 of startup "
                    "capital and a one-to-four-month first-deal window, with "
                    "customer qualification preceding commitments. Contractors "
                    "should cover named specialties such as GPU operations and "
                    "carrier integration; they are not invisible full-time "
                    "capacity. The owner retains pricing authority, supplier "
                    "exposure limits, incident accountability, and the decision "
                    "to discontinue an uneconomic service."
                ),
            ],
            "table": {
                "caption": "Five Operator Archetypes and the Deliverable Each Actually Sells",
                "headers": [
                    "Operator archetype",
                    "Purchased input and named tooling",
                    "Customer deliverable and economic moat",
                    "Failure boundary and required operating response",
                ],
                "rows": [
                    [
                        "Reservation slicer serving isolated batch and inference workloads",
                        "Authorized H100 or H200 reservations with vLLM serving",
                        "Measured GPU-hours supported by predictable scheduling and tenant separation",
                        "Idle commitments consume cash; shrink reservations before renewing capacity",
                    ],
                    [
                        "Inference broker routing workloads across qualified model providers",
                        "LiteLLM routing over independently contracted compatible provider endpoints",
                        "Accepted tokens at documented quality and latency service levels",
                        "Endpoint changes damage output quality; retain tested pinned alternatives",
                    ],
                    [
                        "Managed endpoint operator supporting private enterprise application deployments",
                        "Dedicated bare-metal capacity with deployment automation and DCGM telemetry",
                        "Reserved availability plus implementation support and verifiable retention controls",
                        "Support scope expands silently; price incident coverage and change requests",
                    ],
                    [
                        "Telecom reseller delivering authorized voice and registered messaging",
                        "Wholesale SIP agreements and approved Bandwidth or Twilio integrations",
                        "Metered minutes or message segments with traffic-specific route controls",
                        "Abusive traffic creates carrier exposure; suspend customers and investigate promptly",
                    ],
                    [
                        "Address-capacity broker coordinating legitimate IPv4 leasing and routing",
                        "Documented lessor authority with ARIN records and appropriate route authorization",
                        "Usable address blocks supported by reputation checks and routing coordination",
                        "Blacklisting destroys usability; isolate abuse and enforce contractual remediation",
                    ],
                ],
            },
        },
        {
            "heading": "2. Reconcile Billings, Retained Contribution, and Owner Profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use three separate accounting views: customer billings, "
                    "retained contribution after upstream supply, and owner net "
                    "profit after remaining operating costs. Formula v2.0 supplies "
                    "a 65% retained share, meaning upstream bare-metal and carrier "
                    "commitments consume 35% of modeled gross billings. For the "
                    "Conservative case, $150,000 less $52,500 leaves $97,500; "
                    "subtracting $70,500 of remaining costs produces $27,000. "
                    "For Base, $675,000 less $236,250 leaves $438,750; "
                    "subtracting $249,750 produces $189,000. For Scaled, "
                    "$1,200,000 less $420,000 leaves $780,000; subtracting "
                    "$324,000 produces $456,000. Gross-basis owner margins "
                    "are exactly 18%, 28.0%, and 38%. Dividing profit by "
                    "retained contribution instead produces 27.69%, 43.08%, "
                    "and 58.46%, rounded to two decimals. Label the denominator "
                    "every time; otherwise a sales deck can accidentally present "
                    "two different margins as comparable. The retained revenue "
                    "range is therefore $97,500–$780,000, with $438,750 "
                    "at Base. Neither customer product sales nor an enterprise "
                    "customer's total application spend belongs in these service "
                    "billings. Track GPU-hours, tokens, minutes, segments, and "
                    "address-months in separate quantity fields, then reconcile "
                    "each to its applicable invoice rate. Annual scenario totals "
                    "are portfolio assumptions, not vendor quotations or evidence "
                    "that every individual service retains precisely 65%."
                ),
                (
                    "ASC 606 presentation follows control of the specified service, "
                    "not the percentage a spreadsheet retains. Apply the "
                    "principal-versus-agent analysis in ASC 606-10-55-36 through "
                    "55-40 to each performance obligation. An operator controlling "
                    "capacity before transfer, carrying fulfillment responsibility, "
                    "and exercising meaningful pricing discretion may present "
                    "customer service revenue gross with upstream supply as cost. "
                    "An agent arranging another provider's service generally "
                    "presents the fee or commission it earns. The scorecard's "
                    "65% retained-revenue view is a management normalization; "
                    "it does not establish agent status or make all retained "
                    "contribution automatically recognizable revenue. Document "
                    "contracts, control indicators, credits, and performance "
                    "obligations before choosing ledger treatment. Prepaid Stripe "
                    "wallet collections normally create a customer liability "
                    "until the contracted service is delivered; payment success "
                    "alone does not demonstrate earned revenue. Maintain an "
                    "append-only usage ledger tying request identifiers to "
                    "billable quantities, provider charges, credits, and settlement "
                    "events. Distinguish input tokens, output tokens, cached "
                    "tokens, retries, and rejected requests in the rate card. "
                    "For voice, define answer supervision and rounding; for "
                    "messaging, disclose segment counting and carrier surcharges. "
                    "Reconcile refunds and service credits against the original "
                    "usage record rather than burying them in a generic "
                    "marketing expense. That discipline makes gross and net "
                    "presentations auditable without confusing either with cash."
                ),
                (
                    "The supplied monthly operating-expense range of $2,000–$14,000 "
                    "cannot represent every residual cost in every canonical "
                    "case: Base residual costs alone average $20,812.50 "
                    "monthly, and Scaled residual costs average $27,000. "
                    "Preserve the canonical profits and treat the stated range "
                    "as a core-overhead planning band, with additional labor, "
                    "variable service costs, selling expense, and reserves "
                    "itemized separately. The source does not allocate those "
                    "categories, so the operating budget must substantiate them "
                    "before a commitment. Do not subtract upstream supply "
                    "twice or silently reduce labor to force a preferred "
                    "margin. Conservative and Base each use one full-time "
                    "operator plus two contractors; Scaled uses two full-time "
                    "operators plus three contractors, five people total. "
                    "Separately model settlement timing, refundable wallet "
                    "balances, supplier deposits, disputed payments, and annual "
                    "renewals because accounting profit does not fund a "
                    "reservation invoice before cash arrives. Stress-test "
                    "utilization, selling-price compression, destination mix, "
                    "and customer concentration independently. A ten-point "
                    "utilization decline is not equivalent to a ten-percent "
                    "unit-price cut when reserved supply remains fixed. "
                    "For owned hardware, include depreciation and replacement "
                    "economics; for rented hardware, capture renewal repricing "
                    "and stranded commitments. The 35%–55% spread aspiration "
                    "belongs to selected optimized offers, while the canonical "
                    "18%–38% gross-basis owner margins describe the broader "
                    "business after its complete cost stack."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Annual Reconciliation Without Gross-versus-Retained Confusion",
                "headers": [
                    "Scenario and staffed operating footprint",
                    "Gross billings and upstream supply deduction",
                    "Retained contribution and remaining expense bridge",
                    "Owner profit and explicitly named margin denominators",
                ],
                "rows": [
                    [
                        "Conservative operation uses one full-time operator plus two contractors",
                        "$150,000 gross billings minus $52,500 upstream supply commitments",
                        "$97,500 retained contribution minus $70,500 remaining annual operating costs",
                        "$27,000 owner profit; 18% gross-basis margin; 27.69% retained-basis margin",
                    ],
                    [
                        "Base operation uses one full-time operator plus two contractors",
                        "$675,000 gross billings minus $236,250 upstream supply commitments",
                        "$438,750 retained contribution minus $249,750 remaining annual operating costs",
                        "$189,000 owner profit; 28.0% gross-basis margin; 43.08% retained-basis margin",
                    ],
                    [
                        "Scaled operation uses two full-time operators plus three contractors",
                        "$1,200,000 gross billings minus $420,000 upstream supply commitments",
                        "$780,000 retained contribution minus $324,000 remaining annual operating costs",
                        "$456,000 owner profit; 38% gross-basis margin; 58.46% retained-basis margin",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the Spread Before Optimizing the Router",
                "body": (
                    "The strongest operational advantage is an auditable relationship "
                    "between customer promises, supplier obligations, and cash exposure."
                ),
                "items": [
                    "Price reserved GPU commitments against paid utilization, excluding benchmark time, maintenance, and free customer trials from the utilization numerator.",
                    "Use DCGM to explain hardware behavior, but bill from authenticated application events reconciled against accepted work and contract-defined retry treatment.",
                    "Maintain a destination-level SIP margin floor including billing increments, number charges, taxes where applicable, and supplier minimum commitments.",
                    "Set wallet replenishment and concurrency limits from maximum in-flight spend; a positive wallet balance alone cannot prevent parallel-request overspend.",
                ],
            },
        },
        {
            "heading": "3. Compare Fifteen Plays by Units, Moats, and Reversal Risk",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The fifteen-row matrix maps distinct sellable offers rather "
                    "than claiming fifteen independent profit engines. Rows share "
                    "infrastructure, so revenue must be assigned once to the "
                    "actual customer deliverable. All unit prices below are "
                    "illustrative negotiated economics, not current published "
                    "vendor tariffs or assertions that a named platform permits "
                    "resale by default. For token routing, one hundred million "
                    "billable tokens sold at $3 per million creates $300 "
                    "of service billings; buying the matching workload at "
                    "$1.80 per million costs $180 before routing, support, "
                    "and collection. Real invoices require separate input and "
                    "output weights, cache treatment, and model-specific pricing. "
                    "For SIP, one million connected minutes sold at $0.009 "
                    "produces $9,000; $0.006 upstream termination costs "
                    "$6,000 before number rental, surcharges, and support. "
                    "For messaging, one million segments with a $0.002 "
                    "service markup yields $2,000 of markup, not the "
                    "customer's resulting sales and not necessarily gross "
                    "accounting revenue. Compare offers using contribution per "
                    "constrained resource: GPU-hour, concurrent session, approved "
                    "message throughput, support hour, or committed cash dollar. "
                    "A large apparent spread on a tiny or operationally "
                    "fragile workload may be inferior to a narrower spread "
                    "on predictable replenishing demand. Require a measured "
                    "customer workload before accepting a supplier minimum."
                ),
                (
                    "The adjacent mapped play "
                    "b2b_commercial_vcc_interchange_rebate_arbitrage is an "
                    "accounts-payable distribution business, not GPU utilization "
                    "income. It embeds automated AP or faster vendor settlement "
                    "into freight, construction, medical supply, property "
                    "management, or media workflows, then routes participating "
                    "vendors to issuer-approved commercial virtual cards. A "
                    "negotiated 140–195 basis-point rebate on $100 million "
                    "of eligible settled card volume implies $1.4 million–"
                    "$1.95 million of gross rebates before customer sharing, "
                    "platform fees, reversals, and service costs. The $100 "
                    "million is third-party invoice volume, never operator "
                    "revenue. Commercial-card classification, issuer terms, "
                    "merchant acceptance, and any cap must be verified; "
                    "neither an uncapped rebate nor a particular interchange "
                    "category follows automatically from issuing a virtual "
                    "card. Use issuer-supported Level-3 line-item metadata "
                    "accurately rather than inventing invoice fields. For "
                    "card-averse vendors, an authorized early-pay ACH "
                    "alternative with a 1.5%–2% discount on a $10,000 "
                    "invoice means $150–$200 of supplier-funded discount, "
                    "whose beneficiary depends on contract allocation. "
                    "Concentrate on fragmented vendors with genuine acceptance "
                    "fit. Returned payments and refunded invoices require "
                    "reversal handling. This adjacent play is mapped for "
                    "comparison only; none of its hypothetical rebates is "
                    "added to the volume's canonical $150,000, $675,000, "
                    "or $1,200,000 service-billing scenarios."
                ),
                (
                    "A durable moat is operational evidence that customers "
                    "cannot cheaply reproduce: a regression corpus for their "
                    "model outputs, repeatable deployment manifests, defensible "
                    "meter reconciliation, and an escalation record showing "
                    "how incidents were contained. Cheapest-provider routing "
                    "alone is fragile because published prices converge and "
                    "the cheapest endpoint can fail the customer's quality "
                    "test. Maintain provider-specific limits for context "
                    "length, tool behavior, structured output, throughput, "
                    "region, and retention before allowing automatic failover. "
                    "Contract enterprise zero-data-retention at every relevant "
                    "processor, then disable prompt logging, redact error "
                    "traces, and test backups and support workflows for "
                    "payload leakage. Retain necessary billing metadata "
                    "without retaining customer content. Telecom moats come "
                    "from clean traffic history, accurate registration, "
                    "route-specific quality measurements, and fast abuse "
                    "response, not from finding permissive carriers. IPv4 "
                    "moats require clean provenance and responsive routing "
                    "coordination; a letter of authorization does not erase "
                    "bad reputation. Every offer needs a stop condition "
                    "that can run without the founder awake: a negative "
                    "margin floor, exhausted prepaid balance, failed quality "
                    "benchmark, revoked usage right, or credible abuse signal. "
                    "The fallback must preserve customer commitments and "
                    "supplier rules rather than moving prohibited traffic "
                    "to another account. This is how a small team keeps "
                    "complexity bounded while increasing billed volume."
                ),
            ],
            "table": {
                "caption": "Fifteen Mapped Sub-Verticals: Illustrative Units, Named Rails, Defensible Moats, and Failure Fallbacks",
                "headers": [
                    "Mapped play and specific customer deliverable",
                    "Named platform or contracted infrastructure rail",
                    "Illustrative fee structure and defensible operating advantage",
                    "Clawback or failure trigger and concrete fallback",
                ],
                "rows": [
                    [
                        "gpu_reserved_to_spot_inference_slicing: reserved clusters serving isolated inference and interruptible batches",
                        "Authorized H100/H200/B200 bare metal, vLLM, LiteLLM, and NVIDIA DCGM",
                        "Eight GPUs at $2 hourly cost; $5 sales at 80% utilization support scheduling-led contribution",
                        "Idle reservations or abusive jobs erase spread; suspend abuse, reroute permitted work, and reduce commitments",
                    ],
                    [
                        "Multi-provider token routing for latency-sensitive enterprise application requests",
                        "LiteLLM with separately authorized OpenAI, Anthropic, and Together AI endpoints",
                        "One hundred million tokens at $3 per million yields $300; quality-tested routing protects retention",
                        "Model drift or retention mismatch blocks substitution; pin versions and select a contract-compatible tested endpoint",
                    ],
                    [
                        "Embedding pipeline brokerage for recurring enterprise document indexing jobs",
                        "vLLM-compatible embedding deployments with customer-controlled Qdrant indexing workflows",
                        "Fifty million tokens at $0.20 per million yields $10; recurring document connectors justify additional service fees",
                        "Dimension changes invalidate indexes; version embeddings and rebuild only under an agreed migration plan",
                    ],
                    [
                        "Interruptible overnight inference batches with explicit completion deadlines",
                        "Authorized Runpod or Vast.ai capacity with checkpointed batch scheduling",
                        "One thousand sold GPU-hours at $2.40 yields $2,400 against illustrative $1.40 hourly supply",
                        "Preemption threatens deadlines; checkpoint work and reserve a priced noninterruptible recovery allocation",
                    ],
                    [
                        "Dedicated private inference endpoints with reserved customer availability",
                        "Contracted CoreWeave capacity running isolated customer-specific vLLM deployment stacks",
                        "A $4,000 monthly endpoint against $2,500 supply leaves $1,500 before support and credits",
                        "Availability breaches trigger contractual credits; maintain tested replacement capacity and bounded service remedies",
                    ],
                    [
                        "Customer-authorized LoRA training jobs with reproducible artifact delivery",
                        "Hugging Face PEFT workflows on appropriately isolated reserved GPU workers",
                        "Forty GPU-hours billed at $6 creates $240 against $80 supply at $2 hourly",
                        "Unusable adapters cause rework; use acceptance benchmarks and preserve reproducible training configuration",
                    ],
                    [
                        "Cache-aware inference packaging for repetitive approved enterprise prompts",
                        "Supported vLLM prefix caching with strictly controlled tenant-scoped cache policies",
                        "One million requests with $0.001 processing savings releases $1,000 before cache infrastructure costs",
                        "Cross-tenant exposure or stale outputs defeats savings; isolate caches and disable affected reuse immediately",
                    ],
                    [
                        "Wholesale SIP termination resale for screened business calling traffic",
                        "Authorized Bandwidth or Telnyx agreements with Kamailio and FreeSWITCH routing",
                        "One million minutes at $0.009 versus $0.006 supply leaves $3,000 before remaining costs",
                        "Fraud, surcharge changes, or poor answer quality require route suspension and authorized carrier substitution",
                    ],
                    [
                        "Registered 10DLC messaging capacity with segment-aware customer billing",
                        "The Campaign Registry with approved Twilio or Bandwidth messaging relationships",
                        "One million segments carrying $0.002 markup yields $2,000 before registration and support expenses",
                        "Misregistered campaigns or unlawful traffic cause blocking; stop sending and correct documented campaign details",
                    ],
                    [
                        "Business number inventory management with authorized SIP service attachment",
                        "Telnyx or Bandwidth number provisioning under the applicable resale agreement",
                        "Five hundred numbers billed at $2 monthly yields $1,000 against illustrative $500 number rental",
                        "Porting disputes or emergency-calling gaps require ownership verification and service-specific provisioning remediation",
                    ],
                    [
                        "IPv4 address leasing coordination for legitimate hosting customer allocations",
                        "Documented IPXO arrangements with ARIN record checks and routing authorization",
                        "A 256-address block at $0.60 monthly yields $153.60 against $89.60 supply at $0.35",
                        "Abuse listings or revoked authority destroy usability; isolate offending allocations and enforce replacement terms",
                    ],
                    [
                        "Customer burst-capacity brokerage around predictable product launch windows",
                        "Explicitly permitted AWS EC2 Capacity Blocks or contracted specialist GPU reservations",
                        "Two hundred reserved GPU-hours at $5 retail yields $1,000 against illustrative $600 supply",
                        "Unused launch capacity remains payable; require customer deposits and noncancelable reservation acknowledgment",
                    ],
                    [
                        "Managed GPU development workspaces for small machine-learning teams",
                        "JupyterHub with isolated containers on contracted Lambda or comparable GPU capacity",
                        "Twenty workspaces at $150 monthly yields $3,000 against a measured $1,800 resource allowance",
                        "Idle notebooks and privileged workloads consume margin; enforce sleep policies and restrict execution privileges",
                    ],
                    [
                        "Region-qualified inference continuity packages for production application operators",
                        "LiteLLM with separately contracted Azure and AWS regional service alternatives",
                        "A $1,000 monthly continuity fee against $600 reserved backup cost leaves $400 before testing",
                        "Regional transfer restrictions or model incompatibility block failover; use only prequalified permitted destinations",
                    ],
                    [
                        "b2b_commercial_vcc_interchange_rebate_arbitrage: embedded AP settlement and commercial-card distribution",
                        "Issuer-approved Visa or Mastercard commercial programs with authorized Marqeta or Stripe Issuing integrations",
                        "$100 million eligible volume at 140–195 basis points yields $1.4 million–$1.95 million gross rebates",
                        "Refunds reverse rebates and vendors may reject cards; provide accurate Level-3 data and agreed early-pay ACH",
                    ],
                ],
            },
        },
        {
            "heading": "4. Build the Permission, Metering, and Incident System Before Scaling",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For telecom, determine the service role before automating "
                    "provisioning. Covered voice providers face STIR/SHAKEN and "
                    "Robocall Mitigation Database requirements under 47 CFR "
                    "64.6301 and 64.6305; duties differ by provider "
                    "category, network, and applicable exceptions. A reseller "
                    "cannot assume its upstream provider's filing automatically "
                    "discharges its own obligations. Authentication attests "
                    "specified calling information; it does not establish "
                    "that a call is wanted or lawful. Apply the Telephone "
                    "Consumer Protection Act, 47 U.S.C. 227, and the "
                    "implementing restrictions in 47 CFR 64.1200 to the "
                    "actual calling or messaging activity. Registered 10DLC "
                    "campaigns support carrier delivery requirements but "
                    "do not replace required permission, identification, "
                    "or opt-out handling. Evaluate FCC Form 499-A "
                    "registration and reporting using the entity's actual "
                    "telecommunications activity and applicable instructions; "
                    "contribution exemptions do not necessarily remove "
                    "registration or reporting duties. Where interconnected "
                    "VoIP is supplied, address applicable emergency-calling "
                    "requirements under 47 CFR 9.11. Keep customer "
                    "identity, intended traffic, number authority, destination "
                    "limits, and escalation contacts together in the "
                    "provisioning record. Automated least-cost routing must "
                    "exclude unauthorized routes and destinations regardless "
                    "of price. Treat sudden destination changes, unusually "
                    "short calls, and spending acceleration as investigation "
                    "signals rather than proof of legitimate growth."
                ),
                (
                    "For compute, establish separate control-plane and workload "
                    "identities, least-privilege access, tenant-specific secrets, "
                    "network restrictions, and a tested destruction process "
                    "for ephemeral storage. Quantized serving improves "
                    "economics only when output quality remains acceptable; "
                    "it does not sanitize inputs or isolate customer data. "
                    "Prevent unauthorized privileged containers and "
                    "customer-controlled access to host management interfaces. "
                    "AUP screening should prohibit specifically disallowed "
                    "mining, credential abuse, and unlawful content processing "
                    "without treating every high-utilization job as abuse. "
                    "Bind wallet checks to a server-side reservation of "
                    "estimated maximum request cost, then settle against "
                    "actual metered usage; otherwise concurrent requests "
                    "can all pass the same balance check. Stripe webhooks "
                    "need signature verification, replay-safe event handling, "
                    "and reconciliation with settlement records before "
                    "crediting balances. Record request metadata sufficient "
                    "to explain billing while excluding protected payloads "
                    "from ordinary logs. Preserve evidence under documented "
                    "retention rules when investigating incidents, and "
                    "distinguish that narrow process from routine content "
                    "retention promises. The Computer Fraud and Abuse "
                    "Act, 18 U.S.C. 1030, reinforces the importance "
                    "of authorization boundaries; it does not prescribe "
                    "a complete tenant-isolation design. Test isolation "
                    "with your own authorized accounts and workloads, "
                    "including storage reuse, cache separation, and "
                    "failed-request logging, before admitting external tenants."
                ),
                (
                    "The launch sequence should prove one closed loop: "
                    "an approved customer requests an authorized service, "
                    "the system reserves spend, the upstream fulfills "
                    "the work, the meter records accepted units, and "
                    "the ledger releases or consumes the reservation "
                    "exactly once. Exercise duplicate webhooks, delayed "
                    "provider invoices, partial responses, model outages, "
                    "message segmentation, and SIP rounding during the "
                    "pilot. Then compare customer charges with upstream "
                    "charges and explain every material variance. Use "
                    "a daily exception queue for negative contribution, "
                    "unallocated usage, stale deposits, failed replenishment, "
                    "and unexplained credits. Assign each exception a "
                    "person and response time instead of adding another "
                    "dashboard nobody owns. Before expanding commitments, "
                    "require evidence of repeat paid demand across "
                    "multiple billing cycles and enough cash to survive "
                    "the next supplier invoice without spending refundable "
                    "customer balances. Scale the capacity unit that "
                    "already works rather than launching every mapped "
                    "offer simultaneously. Keep the canonical portfolio "
                    "cases visible, but manage the business through "
                    "measured cohorts and destination-specific economics. "
                    "A small team earns its efficiency by narrowing "
                    "promises, automating reversible routine work, and "
                    "escalating consequential exceptions. The final "
                    "decision is whether customers repeatedly buy a "
                    "reliable service at a price covering every "
                    "obligation, not whether a demonstration can "
                    "generate tokens or connect a call."
                ),
            ],
            "table": {
                "caption": "Four Launch Verification Records Connecting Authority, Delivery, and Cash",
                "headers": [
                    "Verification record and accountable operating owner",
                    "Required evidence before admitting paid customer traffic",
                    "Automated measurement and exception handling mechanism",
                    "Failure response before additional commitments are accepted",
                ],
                "rows": [
                    [
                        "Supplier authority record maintained by the commercial contract owner",
                        "Executed resale rights, region permissions, rate schedules, and suspension terms",
                        "Versioned supplier terms connected to service-specific purchasing and routing rules",
                        "Disable unsupported offers and obtain corrected rights before accepting orders",
                    ],
                    [
                        "Compute isolation record maintained by the infrastructure operations specialist",
                        "Tested tenant boundaries, payload retention settings, and quality acceptance results",
                        "DCGM telemetry correlated with application meters and authorized isolation tests",
                        "Quarantine affected workers and restore only after documented corrective testing",
                    ],
                    [
                        "Telecom eligibility record maintained by the designated service operations owner",
                        "Applicable provider filings, campaign records, number authority, and traffic permissions",
                        "Destination margin floors with complaint escalation and registration status monitoring",
                        "Stop affected traffic and correct the underlying authorization or configuration",
                    ],
                    [
                        "Revenue reconciliation record maintained by the owner and accounting support",
                        "Matched wallet liabilities, delivered units, supplier charges, and customer credits",
                        "Daily ledger reconciliation with duplicate-event protection and aged exception reporting",
                        "Freeze additional exposure until missing charges or unsupported balances are resolved",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Checks That Must Produce Evidence",
                "body": (
                    "Release paid traffic only when the service-specific records "
                    "demonstrate authority, isolation, metering, and controlled exposure."
                ),
                "items": [
                    "Verify executed upstream resale rights and confirm that each proposed fallback provider permits the same customer workload and geographic handling.",
                    "Run two-tenant isolation and zero-data-retention tests covering caches, storage reuse, traces, backups, and support access.",
                    "Complete applicable telecom provider filings and campaign registrations; verify number authority, opt-out handling, destination controls, and emergency-calling scope.",
                    "Replay a complete prepaid billing cycle with concurrent requests, duplicate events, refunds, and supplier reconciliation; prove that balances cannot be spent twice.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Qualify one narrow paid workload",
                    "action": "Collect a representative authorized workload and a signed service specification.",
                    "detail": "Record required quality, latency, region, usage units, retention, support boundaries, and customer acceptance criteria before pricing.",
                },
                {
                    "step": 2,
                    "title": "Secure matching supply and fallback rights",
                    "action": "Contract the smallest viable capacity commitment with a compatible authorized backup.",
                    "detail": "Compare cancellation exposure, resale permission, destination pricing, minimum spend, and the cash required through the first renewal.",
                },
                {
                    "step": 3,
                    "title": "Prove collection and usage reconciliation",
                    "action": "Run a prepaid pilot and reconcile every delivered unit to both ledgers.",
                    "detail": "Reserve in-flight spend, validate settlement events, classify credits, and document the principal-versus-agent assessment for each deliverable.",
                },
                {
                    "step": 4,
                    "title": "Expand only the measured profitable unit",
                    "action": "Increase capacity after repeat paid demand and incident tests support the next commitment.",
                    "detail": "Review utilization, quality, destination contribution, exception workload, customer concentration, and available cash before each supplier renewal.",
                },
            ],
        },
    ],
    "pull_quote": (
        "The durable spread belongs to the operator who controls promises, "
        "permissions, meters, and cash—not the operator who merely finds a cheaper GPU."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        "Choose one archetype and write a service specification covering billable units, quality, latency, region, retention, and credit remedies.",
        "Obtain executed upstream resale permission and a contract-compatible fallback before committing to GPU reservations or wholesale telecom minimums.",
        "Build a ledger separating gross service billings, 65% modeled retained contribution, upstream costs, remaining costs, and owner profit.",
        "Benchmark vLLM and LiteLLM against the customer's acceptance corpus, then test tenant isolation and the complete payload-retention path.",
        "Implement prepaid spend reservation, idempotent Stripe event handling, DCGM-linked observability, and daily supplier-to-customer reconciliation.",
        "Verify applicable voice-provider duties, 10DLC registration, number authority, and incident ownership before increasing traffic or commitments.",
    ],
    "statutory_citations": [
        {
            "title": "47 CFR 64.6301 — Caller ID Authentication",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6301",
            "relevance": (
                "Establishes caller ID authentication duties for covered providers; "
                "map the actual service role and network before provisioning voice traffic."
            ),
        },
        {
            "title": "47 CFR 64.6305 — Robocall Mitigation and Certification",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6305",
            "relevance": (
                "Supports provider-specific mitigation, certification, database, "
                "and traffic-acceptance controls rather than reliance on upstream assurances alone."
            ),
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on Telephone Equipment Use",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Provides the statutory framework for restrictions affecting covered "
                "calling and messaging activity; carrier registration does not replace these duties."
            ),
        },
        {
            "title": "47 CFR 64.1200 — Delivery Restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": (
                "Supplies activity-specific calling and messaging restrictions, "
                "including applicable permission and do-not-call requirements."
            ),
        },
        {
            "title": "47 CFR 64.1195 — Registration of Interstate Telecommunications Providers",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1195",
            "relevance": (
                "Requires covered providers to address registration through the "
                "specified filing framework before offering covered services."
            ),
        },
        {
            "title": "47 CFR 54.706 and 54.711 — Contributions and Reporting",
            "url": "https://www.ecfr.gov/current/title-47/section-54.706",
            "relevance": (
                "Defines covered contribution activity; read alongside section 54.711 "
                "and applicable FCC Form 499 instructions to determine reporting treatment."
            ),
        },
        {
            "title": "47 CFR 54.711 — Contributor Reporting Requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-54.711",
            "relevance": (
                "Anchors reporting obligations associated with universal service "
                "contributions and the applicable revenue reporting framework."
            ),
        },
        {
            "title": "47 CFR 9.11 — Interconnected VoIP Emergency Calling",
            "url": "https://www.ecfr.gov/current/title-47/section-9.11",
            "relevance": (
                "Requires service-specific emergency-calling analysis when the "
                "operator supplies interconnected VoIP rather than merely unrelated capacity."
            ),
        },
        {
            "title": "18 U.S.C. 1030 — Fraud and Related Activity in Connection with Computers",
            "url": "https://www.law.cornell.edu/uscode/text/18/1030",
            "relevance": (
                "Provides statutory context for authorization boundaries, "
                "customer workload screening, and controlled access to shared infrastructure."
            ),
        },
    ],
}
