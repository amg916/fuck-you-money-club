from __future__ import annotations

CHAPTER_4 = {
    "id": "Q4",
    "chapter_id": "Q4",
    "chapter_number": 4,
    "question_number": 4,
    "slug": "startup-capital-lean-infrastructure-pre-flight-stack",
    "question_prompt": "How do you allocate startup capital ($5,000–$60,000 USD) and configure a lean, low-opex ($2,500–$18,000 USD/mo) production stack without wasting cash on bloated overhead?",
    "kicker": "Q4 / THE BIG MONEY PLAYBOOKS",
    "title": "Startup Capital, Lean Infrastructure & Pre-Flight Stack",
    "subtitle": "Reserve-First Funding, Postgres Waterfalls, Authorized Messaging, and Tenant-Isolated Delivery Under 18 U.S.C. § 1030",
    "layout_template": "comparison_table",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #29, Productized AI Agencies, holds Rank #06 with an 86/100 "
        "Money-to-Manpower Score across 23 mapped plays. Allocate sixty percent of "
        "startup cash to working capital, then buy only infrastructure that supports "
        "a contracted workflow, measurable acceptance test, or recoverable deployment. "
        "This chapter converts the $5,000–$60,000 funding range into reserve-first "
        "budgets and a twelve-layer production stack, with explicit limits on "
        "outbound automation and enrichment waterfalls. Recognized revenue consists "
        "of implementation fees and support retainers, never client sales attributed "
        "to automation. Canonical annual owner profit remains $20,000 Conservative, "
        "$165,000 Base, and $400,000 Scaled. Earn those outcomes through bounded "
        "scope, authorized access, tenant isolation, usage metering, and tested "
        "recovery rather than prepaid software collections or speculative hiring."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual implementation-fee and support-retainer revenue only",
            "note": "20% net margin; $20,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$550,000",
            "context": "Annual implementation-fee and support-retainer revenue only",
            "note": "30.0% net margin; $165,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,000,000",
            "context": "Annual implementation-fee and support-retainer revenue only",
            "note": "40% net margin; $400,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Protect sixty percent of capital before funding delivery",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with cash survival, not a software shopping list. At $5,000 "
                    "of opening capital, place $3,000 in working-capital reserve, $700 "
                    "in deployment setup, $800 in entity, contract, and insurance "
                    "preparation, and $500 in measured customer acquisition. At $20,000, "
                    "allocate $12,000, $2,500, $2,500, and $3,000 respectively. At "
                    "$60,000, allocate $36,000, $9,000, $6,000, and $9,000. Each "
                    "allocation preserves sixty percent as liquid float; none assumes "
                    "that every discretionary dollar must immediately be spent. These "
                    "are planning envelopes, not universal vendor quotes. Entity fees "
                    "and insurance depend on jurisdiction and underwriting. If mandatory "
                    "formation or coverage costs exceed the smallest envelope, reduce "
                    "acquisition spending, defer the start, or add capital rather than "
                    "raid the reserve. Keep tax liabilities, refundable deposits, and "
                    "funds owed to suppliers separately identified; they are not free "
                    "runway. With first deals typically taking one to four months, "
                    "$3,000 covers only 1.2 months at a $2,500 monthly burn. The "
                    "smallest launch therefore requires existing runway, an early paid "
                    "diagnostic, or substantially lower pre-delivery spending. Do not "
                    "hire a nominal full-time team against a reserve that cannot "
                    "fund its actual obligations."
                ),
                (
                    "Use three monthly cash envelopes without pretending they are the "
                    "canonical annual income statements. A $2,500 envelope comprises "
                    "$250 software, $1,400 delivery contractors, $300 acquisition, "
                    "$300 administration and insurance, and $250 contingency. An "
                    "$8,000 envelope comprises $750, $4,700, $1,000, $800, and "
                    "$750 in those same categories. An $18,000 envelope comprises "
                    "$1,500, $11,500, $2,000, $1,500, and $1,500. Owner payroll, "
                    "additional employees, project-specific subcontracting, taxes, and "
                    "other costs must be added whenever incurred; these envelopes "
                    "cannot support two salaried employees by assertion. The canonical "
                    "Conservative case remains $100,000 revenue less $80,000 total "
                    "costs, producing $20,000 profit. Base remains $550,000 less "
                    "$385,000, producing $165,000. Scaled remains $1,000,000 less "
                    "$600,000, producing $400,000. Staffing stays 2 FT + 3 C, "
                    "2 FT + 3 C, and 3 FT + 4 C respectively. The scorecard "
                    "does not supply compensation assumptions, so test local labor "
                    "economics before adopting any case. Reconcile every monthly "
                    "cash forecast to a complete annual cost ledger. The operating "
                    "envelope is a spending-control device, not an alternate margin "
                    "calculation or a claim that seven people cost $18,000 monthly."
                ),
                (
                    "Translate sales into recognized service revenue with explicit "
                    "units. One illustrative Conservative mix is eight $10,000 "
                    "implementations plus twenty $1,000 support client-months, totaling "
                    "$100,000. Base can comprise twenty $20,000 implementations plus "
                    "one hundred $1,500 support client-months, totaling $550,000. "
                    "Scaled can comprise twenty-five $28,000 implementations plus "
                    "one hundred fifty $2,000 support client-months, totaling "
                    "$1,000,000. These mixes demonstrate arithmetic, not additional "
                    "forecast evidence. Attribute no client sales, recovered invoices, "
                    "or processed transaction volume to agency revenue. For a "
                    "$10,000 fixed-scope sprint, a negotiated 50/30/20 collection "
                    "schedule creates $5,000 at booking, $3,000 at a demonstrated "
                    "milestone, and $2,000 at acceptance. Collection timing does not "
                    "itself determine revenue recognition; record undelivered obligations "
                    "and refund exposure. Tie contractor commitments to funded "
                    "milestones and maintain an aging report for every receivable. "
                    "Define two integrations, one workflow, specified test cases, and "
                    "a fixed revision allowance before signing. Price an added "
                    "integration separately instead of absorbing it into support. "
                    "Review remaining delivery hours weekly: a $3,000 cost overrun "
                    "consumes fifteen percent of Conservative annual profit. Maintain "
                    "a thirteen-week cash forecast with base collections, delayed "
                    "collections, and refund stress cases before releasing reserve cash."
                ),
            ],
            "table": {
                "caption": "Reserve-First Capital Allocation and Cash-Control Matrix",
                "headers": [
                    "Funding decision and operating purpose",
                    "Exact allocation or arithmetic rule",
                    "Release condition and accountable evidence",
                    "Failure response preserving operating capacity",
                ],
                "rows": [
                    [
                        "Small launch funded with five thousand dollars",
                        "$3,000 reserve; $700 setup; $800 hygiene; $500 acquisition",
                        "Founder documents paid scope before committing delivery purchases",
                        "Delay launch when required insurance exceeds available allocation",
                    ],
                    [
                        "Working launch funded with twenty thousand dollars",
                        "$12,000 reserve; $2,500 setup; $2,500 hygiene; $3,000 acquisition",
                        "Bookkeeper reconciles reserve balance against outstanding supplier commitments",
                        "Freeze discretionary subscriptions when thirteen-week forecast becomes negative",
                    ],
                    [
                        "Expanded launch funded with sixty thousand dollars",
                        "$36,000 reserve; $9,000 setup; $6,000 hygiene; $9,000 acquisition",
                        "Delivery lead releases setup budget against signed implementations",
                        "Retain unused allocation rather than prepay speculative capacity",
                    ],
                    [
                        "Minimum monthly operating envelope before additional payroll",
                        "$250 software; $1,400 contractors; $300 acquisition; $300 administration; $250 contingency",
                        "Owner separately budgets employee compensation and actual project overruns",
                        "Reduce delivery commitments before missing contractor payment obligations",
                    ],
                    [
                        "Middle monthly operating envelope before additional payroll",
                        "$750 software; $4,700 contractors; $1,000 acquisition; $800 administration; $750 contingency",
                        "Accountant reconciles cash spending against complete annual expense ledger",
                        "Reprice low-contribution accounts before adding another recurring tool",
                    ],
                    [
                        "Upper monthly operating envelope before additional payroll",
                        "$1,500 software; $11,500 contractors; $2,000 acquisition; $1,500 administration; $1,500 contingency",
                        "Finance owner validates capacity without replacing canonical cost totals",
                        "Stop unfunded expansion when collections lag delivery commitments",
                    ],
                ],
            },
        },
        {
            "heading": "2. Assemble twelve replaceable layers instead of a platform empire",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Choose one default stack and make exceptions earn their "
                    "maintenance burden. The twelve-layer matrix gives exact reference "
                    "tier prices, not live procurement quotes; confirm current vendor "
                    "terms, taxes, regional availability, and included usage before "
                    "purchase. Annual-billing prices represent monthly equivalents and "
                    "can require upfront payment. Start with GitHub Free, Cloudflare "
                    "Free, a Render Starter worker, Supabase Pro when production "
                    "needs justify it, metered OpenAI inference, Make Free for low "
                    "volume orchestration, Bitwarden Teams, Google Workspace Business "
                    "Starter, Sentry Developer, Better Stack's free uptime service, "
                    "Stripe standard payments, and Tawk.to's free chat software. "
                    "For two operators, the listed paid fixed components total "
                    "$54 monthly: $7 Render, $25 Supabase, $8 Bitwarden, and "
                    "$14 Workspace. Add model usage, payment fees, domain renewal, "
                    "backup storage, bandwidth, and any workflow upgrades separately. "
                    "This is a component subtotal, not a complete production "
                    "operating budget. Free plans can lack required retention, "
                    "availability commitments, or administrative controls. Upgrade "
                    "because a signed requirement needs those features, not because "
                    "a pricing page labels a tier professional. Keep vendor accounts "
                    "under the agency or client entity rather than an individual "
                    "contractor's personal identity."
                ),
                (
                    "Separate the control plane from each client's data plane. "
                    "GitHub stores reviewed code and deployment definitions; it should "
                    "not store client exports or production credentials. Cloudflare "
                    "handles DNS and selected edge protections, while the application "
                    "still enforces authentication, authorization, and rate limits. "
                    "Render executes bounded jobs against tenant-scoped Supabase "
                    "records. Make connects approved events, not unrestricted "
                    "administrative sessions. Give each integration the narrowest "
                    "supported scope, separate development and production credentials, "
                    "and record who authorized access. Under 18 U.S.C. § 1030, "
                    "access boundaries have concrete legal significance; a service "
                    "contract does not authorize every account or dataset a "
                    "technician can reach. Use distinct client projects when shared "
                    "isolation would be difficult to test. For a shared database, "
                    "test row-level policies with two deliberately different tenant "
                    "identities and verify that service credentials never enter a "
                    "browser bundle. Store secrets in deployment secret facilities, "
                    "use Bitwarden for human credential workflows, and redact "
                    "tokens from logs. If a client requires private connectivity "
                    "or data residency beyond the lean architecture, price that "
                    "requirement explicitly or decline that scope rather than "
                    "implying the default stack already provides it."
                ),
                (
                    "Meter workload before selecting a model or committing to an "
                    "annual automation subscription. At the reference GPT-4.1 mini "
                    "rates of $0.40 per million input tokens and $1.60 per "
                    "million output tokens, a task using 2,000 input and 500 "
                    "output tokens costs $0.0016 in uncached text inference. "
                    "Ten thousand such tasks cost $16 before retries, tool "
                    "charges, retrieval, and storage. A twenty percent retry "
                    "allowance makes the inference estimate $19.20, not a "
                    "complete delivery cost. A single hour of debugging at "
                    "$75 exceeds that monthly model bill. Optimize repeated "
                    "failures before shaving token fractions. Record tenant, "
                    "workflow version, model version, token count, latency, and "
                    "review outcome without retaining unnecessary source content. "
                    "Set application-enforced usage limits because provider billing "
                    "alerts may not stop spending. Sentry receives sanitized "
                    "exceptions; uptime checks exercise a harmless health endpoint; "
                    "backup jobs write recoverable copies outside the primary "
                    "failure domain. Test restoration into an isolated environment "
                    "and compare record counts and sampled hashes. An outage "
                    "fallback should queue work or switch to manual processing, "
                    "not silently send client content to an unapproved model "
                    "provider merely because that provider is cheaper."
                ),
            ],
            "table": {
                "caption": "Twelve-Layer Named-Vendor Stack with Reference Prices and Lean Substitutes",
                "headers": [
                    "Layer and named vendor deployment choice",
                    "Exact reference tier price and basis",
                    "Production role and required control boundary",
                    "Cheaper lean alternative and operational tradeoff",
                ],
                "rows": [
                    [
                        "Layer 01: GitHub Free source and release management",
                        "Free tier: $0 subscription, with included usage limits",
                        "Review changes and preserve reproducible releases without embedded secrets",
                        "Local Git plus encrypted remote backups sacrifices hosted collaboration",
                    ],
                    [
                        "Layer 02: Cloudflare Free DNS and edge services",
                        "Free tier: $0 subscription, excluding separately purchased domain registration",
                        "Manage DNS and supported protections without replacing application authorization",
                        "Registrar-provided DNS avoids another dashboard but reduces edge tooling",
                    ],
                    [
                        "Layer 03: Render Starter application execution service",
                        "Starter compute reference: $7 monthly per selected service instance",
                        "Run bounded workers with health checks and scoped deployment secrets",
                        "Existing authorized client compute avoids incremental hosting but increases coordination",
                    ],
                    [
                        "Layer 04: Supabase Pro relational storage and authentication",
                        "Pro reference: $25 monthly subscription, plus applicable usage charges",
                        "Store tenant-scoped records and validate row-level authorization policies explicitly",
                        "Supabase Free costs $0 but production requirements may exceed limits",
                    ],
                    [
                        "Layer 05: OpenAI GPT-4.1 mini text inference",
                        "Uncached text: $0.40/million input tokens; $1.60/million output tokens",
                        "Execute evaluated tasks with token ceilings and documented data routing",
                        "Deterministic rules avoid inference charges when extraction needs no generation",
                    ],
                    [
                        "Layer 06: Make Free event orchestration service",
                        "Free tier: $0 subscription, subject to current included allowances",
                        "Connect authorized triggers with deduplication and recoverable execution records",
                        "Python scheduled jobs remove orchestration subscription but require maintenance ownership",
                    ],
                    [
                        "Layer 07: Bitwarden Teams shared human credential management",
                        "Teams reference: $4 per user monthly when billed annually",
                        "Control shared human credentials with access reviews and timely offboarding",
                        "Bitwarden Free individual vaults cost $0 but lack equivalent team controls",
                    ],
                    [
                        "Layer 08: Google Workspace Business Starter business identity",
                        "Business Starter reference: $7 per user monthly with annual commitment",
                        "Provide managed email identities and enforce supported multifactor authentication",
                        "Existing client-managed identities avoid duplicate seats but require explicit ownership",
                    ],
                    [
                        "Layer 09: Sentry Developer application error visibility",
                        "Developer tier: $0 subscription, subject to current event allowances",
                        "Capture sanitized exceptions and connect failures to specific workflow versions",
                        "Structured local logs avoid subscriptions but demand manual incident review",
                    ],
                    [
                        "Layer 10: Better Stack free uptime monitoring",
                        "Free uptime tier: $0 subscription, within current monitor allowances",
                        "Check harmless health endpoints and route actionable service alerts",
                        "Independent scheduled probes cost little but require reliable external hosting",
                    ],
                    [
                        "Layer 11: Stripe standard domestic online card collection",
                        "U.S. domestic online cards reference: 2.9% plus $0.30 per transaction",
                        "Collect service invoices and reconcile fees, refunds, and unsettled balances",
                        "Bank ACH invoicing may cost less; compare actual bank tariffs",
                    ],
                    [
                        "Layer 12: Tawk.to free customer chat software",
                        "Core chat software: $0 subscription; optional paid services excluded",
                        "Route support requests without inviting credentials into conversational transcripts",
                        "Shared support email avoids another widget but weakens queue visibility",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy reversibility before buying another subscription",
                "body": (
                    "A cheap stack becomes expensive when credentials, data formats, "
                    "or workflow logic cannot move without a complete rebuild."
                ),
                "items": [
                    "Export Make workflow definitions and keep the business rules in tested Python functions whenever practical.",
                    "Tag every paid API request with a tenant and workflow identifier so one noisy client cannot hide inside aggregate spending.",
                    "Negotiate client-owned production accounts for sensitive deployments, while documenting the agency's exact support access and removal process.",
                    "Benchmark ten deliberately difficult examples before increasing model spend; malformed inputs and missing context often dominate model choice.",
                ],
            },
        },
        {
            "heading": "3. Fund signal-based acquisition and permissioned enrichment economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Deploy high_velocity_dm_outbound_systems as a warm-signal operating "
                    "system, not a mass-message engine. Publish a useful workflow "
                    "diagnostic and invite a specific comment, reaction, or inbound "
                    "message through a platform-supported interaction. A reaction "
                    "counts only where the platform permits that messaging route "
                    "and the invitation clearly describes the requested follow-up. "
                    "Require that user-initiated trigger before automated dispatch, "
                    "and send external links only after the prospect replies. "
                    "Route permitted conversations among authorized business inboxes "
                    "for ownership and response coverage, never to evade limits. "
                    "For illustration, 400 qualifying interactions at a thirty "
                    "percent reply rate produce 120 replies; a twenty percent "
                    "booking rate produces 24 calls; a twenty-five percent "
                    "close rate produces six projects. At $10,000 each, that "
                    "is $60,000 in potential signed implementation value, recognized "
                    "only as contractual obligations are delivered. With $1,200 "
                    "campaign spending and twelve labor hours at $50, modeled "
                    "acquisition cost is $300 per closed project. Track actual "
                    "cohorts rather than presenting these conversion assumptions as "
                    "proven results. If replies halve, recalculate capacity and "
                    "acquisition economics before increasing dispatch volume. Preserve "
                    "the trigger record so operators can distinguish requested "
                    "follow-up from opportunistic unsolicited contact."
                ),
                (
                    "PeerFloodError and silent Message Request graveyards are "
                    "signals to stop and inspect the channel, not instructions "
                    "to rotate accounts. Pause dispatch after platform restrictions, "
                    "duplicate messages, missing trigger evidence, or recipient "
                    "objections. Fall back to the public conversation or wait "
                    "for an inbound message where permitted. Use approved APIs "
                    "and platform-native automation; an internal trigger record "
                    "does not override channel rules. Maintain recipient suppression "
                    "across inboxes, deduplicate event identifiers, and expire "
                    "stale signals. Store only the conversation metadata needed "
                    "for service and measurement. For commercial email follow-up, "
                    "apply 15 U.S.C. § 7704 requirements, including accurate "
                    "headers, required identification and address information, and "
                    "timely processing of opt-out requests; do not assume those "
                    "email rules describe every social messaging channel. Review "
                    "performance claims under 15 U.S.C. § 45: saying an "
                    "automation saved forty hours requires a defensible baseline "
                    "and measured comparison. Keep paid pilot results separate "
                    "from estimates and exclude rejected outputs from success "
                    "counts. If a client requests appointment volume without "
                    "limits on method, rewrite the scope around permitted "
                    "signals, qualified conversations, and response handling before "
                    "building any automated outreach."
                ),
                (
                    "Treat free_tier_api_waterfall_multiplexing as a rights-aware "
                    "enrichment service. Evaluate thirty to sixty providers with "
                    "genuine ongoing developer allowances, often fifty to one "
                    "thousand lookups monthly, rather than expiring trials. "
                    "Maintain forty or more interchangeable adapters as the "
                    "catalog matures, but activate only providers whose terms "
                    "permit the intended caching, derived output, and resale. "
                    "Do not manufacture accounts to multiply allowances. Forty "
                    "providers with five hundred eligible lookups each offer "
                    "twenty thousand nominal calls, not twenty thousand complete "
                    "records. At a sixty percent valid Postgres cache-hit rate, "
                    "ten thousand requested records leave four thousand misses. "
                    "At two calls per miss, upstream demand becomes eight "
                    "thousand calls before retries and field-specific bottlenecks. "
                    "Twenty customers paying $199 monthly generate $3,980 "
                    "monthly service revenue within the $99–$499 offering range. "
                    "An illustrative $600 labor, $100 infrastructure, and $200 "
                    "paid-overflow budget leaves $3,080 contribution before "
                    "acquisition and general overhead, not owner profit. Prioritize "
                    "fresh local graph hits; if quotas tighten, use permitted "
                    "public-web, DNS, or MX extraction and label unresolved "
                    "fields accurately. MX presence does not verify a mailbox. "
                    "Respect website restrictions and privacy duties, and count "
                    "this service inside agency revenue rather than adding it "
                    "again to canonical totals."
                ),
            ],
            "table": {
                "caption": "Mapped Play Unit Economics, Rights Checks, and Failure Fallbacks",
                "headers": [
                    "Operating play and measurable production unit",
                    "Illustrative arithmetic with explicitly bounded assumptions",
                    "Required evidence before spending or dispatch",
                    "Fallback when the primary mechanism fails",
                ],
                "rows": [
                    [
                        "high_velocity_dm_outbound_systems: qualifying user-triggered interaction entering supported messaging workflow",
                        "400 triggers produce 120 replies at thirty percent response",
                        "Retain invitation wording, trigger timestamp, and supported channel permission",
                        "Wait for inbound contact when channel authorization is insufficient",
                    ],
                    [
                        "high_velocity_dm_outbound_systems: qualified sales conversation converted into project",
                        "120 replies yield 24 calls and six modeled projects",
                        "Separate booked calls, attended calls, contracts, and recognized revenue",
                        "Revise offer relevance before increasing permitted message frequency",
                    ],
                    [
                        "high_velocity_dm_outbound_systems: acquisition cost including operator handling time",
                        "$1,200 spending plus $600 labor divided by six equals $300",
                        "Record actual operator hours and acquisition spend by cohort",
                        "Pause restricted inboxes rather than rotating identities around limits",
                    ],
                    [
                        "free_tier_api_waterfall_multiplexing: nominal provider capacity before field-specific constraints",
                        "Forty adapters times five hundred allowances equals twenty thousand calls",
                        "Document current entitlements, resale rights, caching restrictions, and expiry",
                        "Remove restricted adapters and shrink the promised field coverage",
                    ],
                    [
                        "free_tier_api_waterfall_multiplexing: cache-adjusted external request demand per monthly batch",
                        "10,000 requests minus sixty percent hits requires 8,000 upstream calls",
                        "Validate freshness windows and two-call assumption against observed workloads",
                        "Use permitted public DNS extraction without claiming mailbox verification",
                    ],
                    [
                        "free_tier_api_waterfall_multiplexing: subscription contribution before acquisition and general overhead",
                        "Twenty $199 subscriptions less $900 modeled costs leaves $3,080",
                        "Include support labor and paid overflow despite free lookup allowances",
                        "Cap usage, disclose degraded fields, and reprice unsustainable accounts",
                    ],
                ],
            },
        },
        {
            "heading": "4. Verify entity hygiene, data boundaries, and recoverable delivery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Establish the entity, bank account, and bookkeeping before "
                    "mixing customer deposits with personal spending. Obtain an "
                    "EIN directly through the IRS when required, maintain "
                    "state registrations and applicable local licenses, and "
                    "review current ownership-reporting obligations rather than "
                    "relying on an old formation checklist. Use an entity-owned "
                    "operating account and a separately tracked reserve balance. "
                    "Confirm account ownership, bank identity, deposit-insurance "
                    "treatment, transfer controls, and payment approval authority "
                    "before moving material funds. Enable multifactor authentication "
                    "and independently verify changed supplier banking instructions. "
                    "Ask an insurance broker for technology errors and "
                    "omissions and cyber coverage matching the actual services, "
                    "data types, subcontractors, and contractual indemnities. "
                    "Compare exclusions, deductibles, defense provisions, and "
                    "retroactive dates, not just premiums. A certificate alone "
                    "does not establish that a particular automation failure "
                    "is covered. The service agreement should define acceptance, "
                    "support hours, usage limits, suspension rights, incident "
                    "notice duties, subprocessors, retention, and deletion. Under "
                    "17 U.S.C. § 204(a), transfers of copyright ownership "
                    "generally require a signed writing; distinguish assigned "
                    "client deliverables from licensed agency templates and "
                    "third-party components. Secure contractor assignments where "
                    "needed before promising ownership that the agency has "
                    "not actually acquired."
                ),
                (
                    "Turn data-processing terms into executable configuration. "
                    "Inventory source systems, personal-information categories, "
                    "authorized purposes, recipients, storage locations, and "
                    "retention periods for each workflow. Where the California "
                    "Consumer Privacy Act applies, California Civil Code "
                    "§ 1798.100(d) requires specified contractual protections "
                    "when a business discloses personal information to covered "
                    "recipients; configure the relevant restrictions instead "
                    "of relying on a generic confidentiality paragraph. "
                    "A client administrator should authorize named system "
                    "access, scopes, and duration. Capture that authorization "
                    "before connecting production accounts. Seed staging with "
                    "synthetic records and run cross-tenant access attempts, "
                    "prompt-injection samples, malformed payloads, expired "
                    "tokens, and duplicate webhook deliveries. Treat retrieved "
                    "documents as data rather than executable instructions; "
                    "keep tool permissions outside model-generated text. "
                    "Require human review for consequential employment, "
                    "credit, healthcare, or comparable decisions and define "
                    "who has authority to act. A low-confidence result "
                    "must enter a review queue, not quietly become an "
                    "automated decision. Preserve enough evidence to explain "
                    "an output while minimizing retained client content. "
                    "Test deletion through caches, exports, and scheduled "
                    "backup expiration, documenting any retention obligations "
                    "that prevent immediate removal from particular records."
                ),
                (
                    "Launch only after four evidence-backed checks pass: "
                    "commercial funding, authorized access, measured quality, "
                    "and recoverable operations. For commercial funding, "
                    "confirm the signed scope, collected deposit, supplier "
                    "commitments, and reserve runway under a thirty-day "
                    "collection delay. For access, verify tenant separation, "
                    "credential rotation, provider routing permissions, and "
                    "a tested offboarding procedure. For quality, use a "
                    "versioned evaluation set containing normal cases and "
                    "known failure modes; agree the acceptance threshold "
                    "with the client before seeing production results. "
                    "For recovery, restore a backup, replay a failed "
                    "job safely, disable outbound actions, and demonstrate "
                    "a manual work queue. Assign each test an owner, "
                    "timestamp, artifact, and repeat condition. A successful "
                    "demo is insufficient evidence of reliable recovery. "
                    "Limit the first production batch to an agreed "
                    "volume that a human can inspect, then expand "
                    "only when measured outcomes remain within the "
                    "contracted thresholds. Route incidents to an accountable "
                    "person rather than a shared inbox without coverage. "
                    "After each launch, compare estimated hours, actual "
                    "hours, token charges, support demand, and collection "
                    "timing. Feed those numbers into the next fixed-price "
                    "quote so growth strengthens contribution instead of "
                    "concealing unpaid labor beneath attractive software margins."
                ),
            ],
            "table": {
                "caption": "Pre-Launch Evidence Register for Entity, Data, Quality, and Recovery",
                "headers": [
                    "Control area and accountable operating owner",
                    "Evidence required before the first production batch",
                    "Concrete verification procedure and passing condition",
                    "Response when evidence or behavior fails",
                ],
                "rows": [
                    [
                        "Entity and banking ownership assigned to business principal",
                        "Formation records, bank ownership evidence, and reconciled opening balances",
                        "Verify payment authority and independently confirm changed supplier instructions",
                        "Hold transfers until authorized signers resolve the ownership discrepancy",
                    ],
                    [
                        "Insurance and contract alignment assigned to operating principal",
                        "Broker-reviewed coverage terms and signed scope with bounded obligations",
                        "Compare exclusions and deductibles against actual workflow failure exposures",
                        "Narrow service commitments or obtain suitable coverage before delivery",
                    ],
                    [
                        "Client access authorization assigned to designated client administrator",
                        "Named systems, permitted scopes, access duration, and revocation owner",
                        "Attempt prohibited cross-tenant reads and verify requests are rejected",
                        "Remove credentials and repair isolation before reconnecting production systems",
                    ],
                    [
                        "Output quality and human review assigned to delivery lead",
                        "Versioned evaluation results and client-agreed thresholds for consequential outputs",
                        "Exercise adversarial inputs and confirm uncertain outputs reach reviewers",
                        "Return workflow to manual processing while correcting failure causes",
                    ],
                    [
                        "Restore and replay readiness assigned to incident owner",
                        "Completed restore record and replay logs showing duplicate prevention",
                        "Recover isolated data and replay failed jobs without repeated actions",
                        "Suspend automation until recovery works within the agreed objective",
                    ],
                    [
                        "Spend and service limits assigned to account owner",
                        "Tenant usage ceilings, collection status, and documented suspension conditions",
                        "Exhaust test allowance and confirm expensive actions stop safely",
                        "Queue requests and notify client instead of creating uncapped charges",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks with artifacts, owners, and stop conditions",
                "body": (
                    "A check passes only when the designated owner can reproduce "
                    "the result and locate the supporting artifact."
                ),
                "items": [
                    "Funding check: verify collected deposit, signed scope, and reserve coverage after modeling a thirty-day collection delay.",
                    "Access check: demonstrate authorized scopes, rejected cross-tenant access, working revocation, and approved provider data routes.",
                    "Quality check: meet the client's predetermined evaluation threshold and demonstrate human review for consequential decisions.",
                    "Recovery check: restore an isolated backup, replay one failed job without duplicate effects, and stop outbound actions on demand.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Lock the commercial envelope",
                    "action": "Record scope, milestones, collections, and reserve allocation.",
                    "detail": (
                        "Attach the signed service schedule and thirteen-week cash "
                        "forecast; identify every supplier commitment before release."
                    ),
                },
                {
                    "step": 2,
                    "title": "Provision bounded production access",
                    "action": "Create entity-controlled accounts and tenant-scoped credentials.",
                    "detail": (
                        "Retain client authorization, enforce multifactor authentication, "
                        "and test credential removal with the designated administrator."
                    ),
                },
                {
                    "step": 3,
                    "title": "Prove quality and recovery",
                    "action": "Run the evaluation set, restore exercise, and replay test.",
                    "detail": (
                        "Save results with workflow versions; verify manual review, "
                        "duplicate prevention, and application-enforced usage ceilings."
                    ),
                },
                {
                    "step": 4,
                    "title": "Release a bounded first batch",
                    "action": "Process the agreed pilot volume and reconcile actual economics.",
                    "detail": (
                        "Compare accepted outputs, operator hours, API charges, "
                        "support requests, and collections before expanding throughput."
                    ),
                },
            ],
        },
    ],
    "pull_quote": "Protect the reserve, meter the workflow, and buy capacity only after a customer funds the constraint.",
    "diagram_id": "diag-07",
    "action_checklist": [
        "Select the $5,000, $20,000, or $60,000 capital envelope and ring-fence sixty percent as liquid working capital.",
        "Build a thirteen-week cash forecast that includes real staffing obligations, delayed collections, refund exposure, and supplier commitments.",
        "Confirm all twelve stack prices and contractual limits, then provision only the components required by the first signed workflow.",
        "Implement user-triggered messaging with supported platform routes, cross-inbox suppression, and external links withheld until a prospect replies.",
        "Catalog enrichment-provider rights and quotas, validate cache freshness, and enforce paid-overflow limits before selling subscriptions.",
        "Complete the four pre-flight checks, retain reproducible artifacts, and release a human-reviewable first production batch.",
    ],
    "statutory_citations": [
        {
            "title": "18 U.S.C. § 1030 — Fraud and related activity in connection with computers",
            "url": "https://www.law.cornell.edu/uscode/text/18/1030",
            "relevance": (
                "Establish authorized client-system access and document scope; "
                "technical reach does not establish permission."
            ),
        },
        {
            "title": "15 U.S.C. § 45 — Unfair methods of competition and unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": (
                "Substantiate material performance and savings claims with "
                "measured baselines and accurately described results."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Apply commercial-email requirements to email follow-up, including "
                "accurate transmission information and required opt-out handling."
            ),
        },
        {
            "title": "17 U.S.C. § 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Document copyright transfers in signed writings where required "
                "and distinguish client assignments from agency template licenses."
            ),
        },
        {
            "title": "California Civil Code § 1798.100(d) — Personal-information disclosure contracts",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV",
            "relevance": (
                "Where applicable, implement required recipient contract terms "
                "and align data use, retention, and downstream processing with them."
            ),
        },
    ],
}
