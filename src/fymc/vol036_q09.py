from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "contracts-statutory-guardrails-licensing-and-outreach-scripts",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern gpu compute & telecom capacity arbitrage?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "Prepaid GPU Capacity, FCC Provider Boundaries, STIR/SHAKEN, 10DLC Registration, Data Covenants & Evidence-Backed Sales",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #36, GPU Compute & Telecom Capacity Arbitrage, holds Rank #03 of 36 "
        "with a 94/100 Money-to-Manpower Score across a shelf of 15 mapped plays. "
        "This chapter turns reserved GPU capacity, inference routing, SIP termination, "
        "10DLC messaging, and IPv4 access into precisely bounded commercial obligations. "
        "The three annual owner-profit cases are $27,000 Conservative, $189,000 Base, "
        "and $456,000 Scaled; gross billings must remain distinct from the 65% retained "
        "contribution basis. Build service-specific contracts, determine the actual FCC "
        "provider role, verify upstream resale rights, and restrict outreach to "
        "supportable claims. Prepaid wallets, tenant isolation, documented consent, "
        "and evidence-backed competitor comparisons protect the spread without "
        "promising permissions, retention behavior, or capacity that suppliers cannot deliver."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross billings; $97,500 retained contribution at 65%",
            "note": "18% gross-billings net margin; $27,000 owner profit; 1 FT + 2 C; 27.69% retained margin",
        },
        {
            "label": "Base",
            "value": "$675,000",
            "context": "Annual gross billings; $438,750 retained contribution at 65%",
            "note": "28.0% gross-billings net margin; $189,000 owner profit; 1 FT + 2 C; 43.08% retained margin",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross billings; $780,000 retained contribution at 65%",
            "note": "38% gross-billings net margin; $456,000 owner profit; 2 FT + 3 C; 58.46% retained margin",
        },
    ],
    "sections": [
        {
            "heading": "1. Classify each service before accepting a customer order",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a service inventory, not a single label such as technology reseller. "
                    "A dedicated H100 lease, a metered inference endpoint, outbound SIP termination, "
                    "application-to-person messaging, and an IPv4 sublease create different obligations "
                    "even when one Stripe invoice collects payment. Identify the contracting seller, "
                    "upstream supplier, customer location, traffic destination, numbering responsibility, "
                    "and party controlling service delivery. Pure compute hosting does not become "
                    "telecommunications merely because packets traverse a network. Conversely, buying "
                    "carrier termination wholesale does not remove provider duties when the operator "
                    "sells covered voice services under their own name. For voice, map the offering "
                    "against 47 U.S.C. 153 and the applicable FCC service definitions; evaluate "
                    "Section 214 authority under 47 U.S.C. 214 and 47 CFR Part 63, including "
                    "whether international service requires separate authority. Determine FCC Form "
                    "499-A registration and reporting duties from actual activities and current filing "
                    "instructions. A contribution exemption does not automatically eliminate filing "
                    "duties. Record who owns each filing, its supporting revenue classification, and "
                    "the next review date. Keep compute and telecom order forms separable so that "
                    "adding messaging does not silently expand a GPU customer's service scope or "
                    "cause unrelated usage to inherit unsuitable suspension and billing terms."
                ),
                (
                    "Treat STIR/SHAKEN, the Robocall Mitigation Database, and messaging registration "
                    "as separate systems with separate evidence. Under 47 CFR 64.6301 and 64.6305, "
                    "determine the obligations attached to the operator's actual voice-provider or "
                    "intermediate-provider role, including authentication, mitigation, filing, and "
                    "traffic acceptance requirements where applicable. Do not describe a supplier's "
                    "database entry as the reseller's filing. Verify upstream status and require "
                    "timely traceback cooperation, customer investigation, and route suspension rights. "
                    "A signed call is not proof that its recipient authorized it; attestation and "
                    "consumer permission answer different questions. For 10DLC, The Campaign Registry "
                    "and carrier campaign vetting are industry onboarding mechanisms, not federal "
                    "licenses and not substitutes for TCPA analysis. Capture the actual brand, use "
                    "case, opt-in language, sample messages, help response, and opt-out behavior before "
                    "submitting a campaign. Prohibit moving rejected traffic to another aggregator "
                    "to bypass restrictions. Configure least-cost routing to consider destination, "
                    "quality, permitted traffic, and supplier eligibility before price. If an eligible "
                    "route costs more than the customer's ceiling, pause delivery or obtain a revised "
                    "order rather than silently routing through an unsuitable carrier. Preserve "
                    "traceability without retaining message content longer than the documented purpose requires."
                ),
                (
                    "Build a jurisdiction worksheet around where customers and end users receive "
                    "service, not merely the operator's incorporation state. California Public "
                    "Utilities Code 1001 illustrates why facilities, service classification, and "
                    "state commission authority require a separate analysis; it does not establish "
                    "that every cloud application needs a telephone certificate. Check state "
                    "registration, numbering, emergency-calling, accessibility, tax, and surcharge "
                    "requirements against the specific product. Interconnected VoIP can trigger "
                    "duties that a non-interconnected software feature does not. Florida Statutes "
                    "501.059 adds state telephone-solicitation constraints that cannot be replaced "
                    "by a national campaign template. California consumer-data processing can "
                    "require service-provider or contractor terms under Civil Code 1798.100 and "
                    "related provisions, depending on the parties and thresholds. Maintain separate "
                    "tax mappings for compute, telecommunications, and messaging rather than assuming "
                    "a software tax code fits everything. Screen customer identity, beneficial "
                    "ownership where warranted, destination, and intended use against applicable "
                    "sanctions restrictions; GPU hardware, software, technical transfers, and "
                    "restricted end uses may also require export-control analysis. Do not represent "
                    "every cloud GPU session as a hardware export. Escalate facts that change the "
                    "classification, and keep the affected destination or service disabled until "
                    "the required permissions and operating responsibilities are established."
                ),
            ],
            "table": {
                "caption": "Service Classification and Provider-Responsibility Evidence Matrix",
                "headers": [
                    "Service and actual operating role",
                    "Authority or commercial boundary to evaluate",
                    "Evidence required before customer activation",
                    "Fallback when the boundary remains unresolved",
                ],
                "rows": [
                    [
                        "Dedicated GPU access sold with defined capacity commitments",
                        "Upstream lease must expressly permit customer resale",
                        "Executed resale permission identifying geography and tenancy rights",
                        "Offer only capacity covered by documented supplier permission",
                    ],
                    [
                        "Inference routing sold through an operator-controlled endpoint",
                        "Provider terms govern subprocessors and permitted model usage",
                        "Approved routing inventory with retention and regional restrictions",
                        "Pin workloads to a single contractually eligible endpoint",
                    ],
                    [
                        "Outbound voice termination sold under the operator's name",
                        "FCC classification determines filings and provider-specific operating duties",
                        "Written role analysis plus applicable registration and filing records",
                        "Keep voice sales inactive while classification is resolved",
                    ],
                    [
                        "International telecommunications routes offered to enterprise calling customers",
                        "Section 214 analysis addresses applicable international authorization requirements",
                        "Authority records identifying the entity actually providing service",
                        "Exclude international destinations until authorization requirements are satisfied",
                    ],
                    [
                        "Covered voice traffic received from an upstream provider",
                        "Applicable database and traffic acceptance rules require verification",
                        "Dated provider checks and documented traceback response ownership",
                        "Suspend the affected route and preserve investigation evidence",
                    ],
                    [
                        "Business messaging delivered through registered 10DLC carrier routes",
                        "Carrier registration supplements rather than replaces recipient permission",
                        "Brand campaign records and reproducible opt-in evidence packages",
                        "Stop campaign traffic when registration or permission fails",
                    ],
                    [
                        "IPv4 access leased without transferring address ownership rights",
                        "RIR policies and lessor authority constrain permitted delegation",
                        "Lease authority plus applicable routing authorization and abuse contacts",
                        "Withdraw affected advertisements and migrate only with customer coordination",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four verifications before the first paid production workload",
                "body": (
                    "Apply these checks to the specific service and jurisdiction; a completed "
                    "compute review cannot authorize an unrelated voice launch."
                ),
                "items": [
                    "Verify supplier resale rights, tenant geography, workload permissions, and the exact entity signing the customer order.",
                    "Document applicable FCC, state, emergency-service, registration, and contribution duties with named filing owners.",
                    "Test wallet exhaustion, tenant isolation, payload logging controls, and route suspension using noncustomer test traffic.",
                    "Match customer claims, consent evidence, retention promises, and liability obligations to capabilities proven by each upstream supplier.",
                ],
            },
        },
        {
            "heading": "2. Make data, acceptable use, and supplier promises enforceable",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A compute order should identify GPU model, physical or virtual allocation, "
                    "memory entitlement, scheduling policy, region, maintenance windows, and permitted "
                    "substitution. H100, H200, and B200 capacity are not interchangeable simply "
                    "because a dashboard displays GPU hours. Specify whether a slice provides "
                    "hardware partitioning, time sharing, or exclusive access, and describe the "
                    "isolation actually implemented. Run vLLM behind tenant-scoped credentials and "
                    "apply authorization before LiteLLM chooses a provider. Avoid shared caches "
                    "that expose another customer's prompts, embeddings, adapters, or generated "
                    "output. Use DCGM for device health and utilization evidence, but define a "
                    "separate customer billing meter; device utilization alone does not establish "
                    "billable reserved time or accepted tokens. The acceptable-use schedule should "
                    "prohibit unauthorized access, malware deployment, abusive mining where supplier "
                    "terms prohibit it, unlawful content processing, and abusive calling or messaging. "
                    "Specify investigative access, evidence preservation, immediate isolation for "
                    "active harm, notice when appropriate, and restoration conditions. Customer "
                    "screening is a risk-control process, not a claim that every compute reseller "
                    "is subject to bank-style identification duties. Request identity and business "
                    "purpose proportionate to service risk, and avoid accumulating sensitive "
                    "identity documents without a defined need, restricted access, and deletion schedule."
                ),
                (
                    "Translate zero-data-retention promises into a data-flow schedule covering request "
                    "bodies, responses, cache entries, tracing, crash dumps, abuse systems, support "
                    "tickets, and backups. An operator cannot promise enterprise payload deletion "
                    "while a fallback inference provider retains prompts for product improvement. "
                    "Require explicit upstream settings or written terms supporting the promise, "
                    "and remove ineligible endpoints from the routing pool rather than hoping "
                    "a preferred route always succeeds. Distinguish payload retention from minimal "
                    "billing and security metadata; disclose their fields, purpose, retention "
                    "period, and access controls. Document any mandatory preservation exception "
                    "narrowly instead of marketing absolute deletion that the contract contradicts. "
                    "For health-sector customers, evaluate whether the service creates a business "
                    "associate relationship under 45 CFR 160.103 and whether agreements under "
                    "45 CFR 164.504(e) are required. A business associate agreement is useful "
                    "only when the selected infrastructure can perform its obligations. For "
                    "covered telecommunications customer information, evaluate 47 U.S.C. 222 "
                    "and the implementing FCC requirements separately from a general privacy "
                    "policy. Test log suppression using synthetic sensitive markers, verify "
                    "backups and support exports, and retain the test result. Failed deletion "
                    "or accidental payload capture should trigger the incident procedure and "
                    "customer notice assessment specified in the data-processing schedule."
                ),
                (
                    "Allocate intellectual-property rights by asset rather than saying that everything "
                    "belongs to the customer. The customer retains rights in supplied data, "
                    "weights, adapters, and prompts to the extent they possess those rights; "
                    "the operator receives only the permissions needed to provide the service. "
                    "Generated-output rights remain subject to applicable law and upstream model "
                    "terms, so do not promise exclusive ownership merely because inference was "
                    "paid. Identify the operator's pre-existing orchestration code, templates, "
                    "and metering logic, and prohibit training on customer content unless a "
                    "separate affirmative agreement permits it. Require customers to hold necessary "
                    "model and dataset licenses without claiming this transfers the operator's "
                    "own responsibilities. For IPv4 capacity, identify address blocks, permitted "
                    "announcements, relevant registry policies, routing authorization, abuse "
                    "contacts, and return procedures; possession of an invoice does not establish "
                    "routing authority. Set a remediation period for reputation damage where "
                    "safe, and reserve prompt isolation for active abuse. When a supplier "
                    "terminates capacity, provide an orderly export or migration path for "
                    "customer-controlled artifacts without exposing another tenant's information. "
                    "The practical fallback is fewer eligible services with enforceable promises, "
                    "not a broader catalog whose data, licensing, and routing obligations cannot "
                    "be satisfied by the actual delivery chain."
                ),
            ],
            "table": {
                "caption": "Data, Licensing, and Acceptable-Use Contract Schedule",
                "headers": [
                    "Schedule requiring an explicit customer commitment",
                    "Clause mechanics to write into the agreement",
                    "Operational proof retained by the service owner",
                    "Failure response with a bounded customer remedy",
                ],
                "rows": [
                    [
                        "GPU allocation and supported substitution service schedule",
                        "Name model memory isolation region and substitution permission",
                        "Provisioning records connect each tenant to contracted resources",
                        "Offer approved substitute capacity or contractually defined credits",
                    ],
                    [
                        "Tenant boundary and workload security implementation schedule",
                        "Separate credentials storage namespaces caches and administrative access",
                        "Isolation tests demonstrate cross-tenant access attempts are blocked",
                        "Isolate affected workloads and execute the incident procedure",
                    ],
                    [
                        "Enterprise payload retention and subprocessor restriction schedule",
                        "List payload exclusions metadata periods and permitted subprocessors",
                        "Synthetic-marker tests validate logs backups and support exports",
                        "Disable incompatible routes before accepting additional customer requests",
                    ],
                    [
                        "Customer identity and proportionate service screening schedule",
                        "Collect business purpose authority and risk-relevant identity evidence",
                        "Restricted records show review outcome without unnecessary document copies",
                        "Decline activation when material identity discrepancies remain unresolved",
                    ],
                    [
                        "Customer artifacts and generated output ownership schedule",
                        "Separate supplied assets platform code and model-license limitations",
                        "Versioned model terms accompany each approved inference endpoint",
                        "Remove incompatible models and preserve customer artifact portability",
                    ],
                    [
                        "Abuse investigation suspension and restoration operating schedule",
                        "Define prohibited conduct evidence handling notice and restoration",
                        "Incident records link triggering evidence to scoped suspension",
                        "Suspend the affected service rather than unrelated customer workloads",
                    ],
                    [
                        "Address delegation and routing authority lease schedule",
                        "Identify address blocks delegation rights and announcement responsibilities",
                        "Applicable registry records and routing authorizations match the lease",
                        "Coordinate route withdrawal and return the delegated address capacity",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the spread at the supplier boundary",
                "body": (
                    "Experienced operators purchase enforceable rights and observable service "
                    "behavior, not merely an attractive capacity quote."
                ),
                "items": [
                    "Attach the supplier's precise retention configuration to each enterprise order; exclude unsupported LiteLLM fallbacks automatically.",
                    "Separate DCGM health telemetry from invoice evidence so a busy device does not become an invented customer charge.",
                    "Negotiate GPU substitution and maintenance credits before accepting long commitments; require customer permission for materially different hardware.",
                    "Keep a prequalified voice route with verified provider status and agreed traffic rules; price resilience before a carrier suspension occurs.",
                ],
            },
        },
        {
            "heading": "3. Tie fees, liability, and exit rights to the canonical economics",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the Formula v2.0 scorecard as a reconciliation framework, not a license "
                    "to classify accounting revenue by preference. Conservative gross billings "
                    "of $150,000 leave $97,500 at the stipulated 65% retained share; subtracting "
                    "$70,500 of remaining modeled costs produces $27,000 owner profit. Base "
                    "gross billings of $675,000 leave $438,750; subtracting $249,750 produces "
                    "$189,000. Scaled gross billings of $1,200,000 leave $780,000; subtracting "
                    "$324,000 produces $456,000. The corresponding upstream allocations are "
                    "$52,500, $236,250, and $420,000. Owner-profit margins on gross billings "
                    "are 18%, 28.0%, and 38%; margins on retained contribution are 27.69%, "
                    "43.08%, and 58.46%. These are different denominators, not competing "
                    "versions of the same percentage. ASC 606 principal-versus-agent analysis "
                    "depends on control and the actual arrangement; a 65% modeling factor "
                    "does not independently establish net presentation. Maintain gross customer "
                    "collections, supplier pass-throughs, retained contribution, and recognized "
                    "revenue in separate ledger views. The advertised monthly operating-expense "
                    "range is not an exhaustive reconciliation of every annual modeled cost. "
                    "Keep workload examples below separate from these canonical scenarios, and "
                    "never count customer application sales, token-user commerce, or downstream "
                    "merchant volume as the operator's own billings."
                ),
                (
                    "Define the fee trigger before configuring the wallet. For reserved GPU "
                    "capacity, billing can attach to the contracted reservation interval even "
                    "when utilization is low; for token services, define accepted input and "
                    "output units, tokenizer version, retries, and treatment of failed requests. "
                    "For SIP, state destination rate decks, connection charges, minimum duration, "
                    "rounding increments, and rate-change notice. For messaging, distinguish "
                    "segments, carrier surcharges, registration charges, and delivery status. "
                    "Illustratively, 1,000 accepted GPU-hours billed at $3.00 produce $3,000 "
                    "gross; a $1.05 supplier cost per hour produces $1,050 upstream cost "
                    "and $1,950 retained contribution, before remaining expenses. Those "
                    "assumed rates illustrate the 65% factor and are not market quotes. "
                    "Require a prepaid balance, authorize expected consumption atomically, "
                    "settle measured usage, and release unused authorization. Stripe payment "
                    "success does not eliminate chargebacks or make funds irrevocable. "
                    "Prevent concurrent requests from overspending the same balance, and "
                    "specify service suspension, residual-balance refunds, disputed usage, "
                    "and abandoned-property treatment where applicable. Keep credits "
                    "nontransferable and limited to the operator's own services unless "
                    "a separate stored-value analysis supports broader functionality. A "
                    "wallet protects collections; it cannot repair an uneconomic bare-metal "
                    "commitment or replace an enforceable customer reservation."
                ),
                (
                    "Make the commercial allocation readable enough that sales, support, and "
                    "engineering implement the same agreement. Scope belongs in the order "
                    "form; usage definitions and fee triggers belong in the pricing schedule; "
                    "availability calculations, exclusions, and credits belong in the service "
                    "schedule. Limit anti-circumvention to identified introductions, a defined "
                    "service opportunity, a reasonable period, and documented damages or an "
                    "enforceable fee mechanism. Do not use it to block independent customer "
                    "relationships or conceal supplier identity needed for security review. "
                    "Negotiate a stated liability cap with explicit treatment of confidentiality, "
                    "data incidents, intellectual-property claims, unpaid fees, and conduct "
                    "that applicable law prevents parties from limiting. Avoid assuming "
                    "supplier caps automatically cover the operator's broader promises. "
                    "Specify notice addresses, escalation deadlines, governing law, forum "
                    "or arbitration mechanics, and a practical method for disputing "
                    "meter records. Evaluate UCC Article 2 only where the transaction "
                    "and jurisdiction support its application; cloud services are not "
                    "automatically sales of goods. Renewal should require clear notice "
                    "and a defined cancellation path. Provide export timing, artifact "
                    "format, deletion confirmation, number portability where applicable, "
                    "and treatment of unused prepaid funds. Price these duties into "
                    "the spread before signing, especially when upstream capacity renews "
                    "earlier than the customer's reservation."
                ),
            ],
            "table": {
                "caption": "Commercial Clause Checklist and Canonical Financial Controls",
                "headers": [
                    "Commercial term with a named economic exposure",
                    "Required clause or measurement rule for operators",
                    "Evidence supporting billing or enforcing the promise",
                    "Fallback preserving cash and customer exit rights",
                ],
                "rows": [
                    [
                        "Service scope and supplier-supported delivery obligation schedule",
                        "Specify hardware regions traffic classes exclusions and dependencies",
                        "Signed order maps each promise to supplier capability",
                        "Remove unsupported commitments before accepting the customer reservation",
                    ],
                    [
                        "Usage fee trigger and prepaid balance settlement schedule",
                        "Define accepted units reservations retries rounding and deductions",
                        "Immutable usage identifiers reconcile wallet entries to invoices",
                        "Pause consumption before the available prepaid balance expires",
                    ],
                    [
                        "Conservative case with eighteen percent gross-billings profit margin",
                        "$150,000 gross less $52,500 upstream leaves $97,500 retained",
                        "$97,500 retained less $70,500 remaining costs yields $27,000",
                        "Keep staffing at one full-time operator plus two contractors",
                    ],
                    [
                        "Base case with twenty-eight percent gross-billings profit margin",
                        "$675,000 gross less $236,250 upstream leaves $438,750 retained",
                        "$438,750 retained less $249,750 remaining costs yields $189,000",
                        "Keep staffing at one full-time operator plus two contractors",
                    ],
                    [
                        "Scaled case with thirty-eight percent gross-billings profit margin",
                        "$1,200,000 gross less $420,000 upstream leaves $780,000 retained",
                        "$780,000 retained less $324,000 remaining costs yields $456,000",
                        "Use two full-time operators plus three specialist contractors",
                    ],
                    [
                        "Introduction protection liability allocation and dispute resolution schedule",
                        "Bound protected opportunities caps exceptions deadlines and chosen forum",
                        "Signed schedules and introduction records support any claimed remedy",
                        "Resolve documented disputes without blocking unrelated customer data access",
                    ],
                    [
                        "Renewal cancellation portability and unused prepaid funds schedule",
                        "Specify notice periods export format deletion and refund treatment",
                        "Renewal notices and settlement records demonstrate timely customer communication",
                        "Allow orderly migration before withdrawing committed production capacity",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create a service-specific responsibility record",
                    "action": "Map each proposed order to supplier rights, service classification, and jurisdiction.",
                    "detail": "Name the seller, filing owner, data processors, permitted destinations, and unresolved dependencies before generating a payable invoice.",
                },
                {
                    "step": 2,
                    "title": "Align contract language with configured controls",
                    "action": "Attach pricing, retention, acceptable-use, service, and exit schedules.",
                    "detail": "Check every promise against actual LiteLLM routes, vLLM tenancy, SIP permissions, messaging registration, and prepaid settlement behavior.",
                },
                {
                    "step": 3,
                    "title": "Run synthetic usage through billing and failure paths",
                    "action": "Test accepted units, duplicate events, failed requests, wallet exhaustion, and supplier interruption.",
                    "detail": "Reconcile the customer-facing meter to ledger entries; record exclusions and verify that retries cannot create unauthorized duplicate deductions.",
                },
                {
                    "step": 4,
                    "title": "Activate only the reviewed service configuration",
                    "action": "Archive signed schedules and enable the documented capacity and traffic classes.",
                    "detail": "Assign recurring reviews for filing changes, supplier status, price compression, retention settings, consent evidence, and customer cancellation requests.",
                },
            ],
        },
        {
            "heading": "4. Use evidence-backed comparisons and permission-aware outreach scripts",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play competitor_intent_comparison_hijacking targets high-intent "
                    "comparison, pricing, and cancellation searches through genuinely useful "
                    "decision pages. Build text-only nominative comparisons using dated public "
                    "pricing citations, matched units, region, commitment duration, hardware "
                    "generation, and workload constraints. Nominative fair use is "
                    "fact-dependent and varies by jurisdiction; using a competitor's name "
                    "does not authorize confusion about source, sponsorship, or affiliation. "
                    "Evaluate false-association and advertising risk under 15 U.S.C. 1125(a), "
                    "and substantiate objective claims under the FTC Act. Do not copy logos, "
                    "imitate account portals, suggest endorsement, or publish cancellation "
                    "instructions that require a customer's credentials. A migration guide "
                    "should explain how the customer exports their own artifacts through "
                    "official interfaces. Illustratively, 200 qualified monthly visits at "
                    "the play's 10–18% conversion assumption produce 20–36 conversions. "
                    "If each conversion is an activated customer buying $200 of service, "
                    "gross billings are $4,000–$7,200 and retained contribution at 65% "
                    "is $2,600–$4,680 before acquisition and operating expenses. If conversion "
                    "means a form submission instead, these billings cannot be claimed "
                    "without a separate activation rate. The fallback is narrower text-only "
                    "comparison coverage, timestamped public sources, and suspended claims "
                    "when equivalent current pricing cannot be verified."
                ),
                (
                    "Separate commercial email from calling and messaging workflows because their "
                    "permission rules differ. CAN-SPAM, 15 U.S.C. 7704, governs commercial "
                    "email requirements including accurate headers, nondeceptive subjects, "
                    "required advertising identification, a valid postal address, and a "
                    "working opt-out honored within the statutory period. It does not "
                    "create blanket permission to send automated sales texts. Under "
                    "47 U.S.C. 227 and 47 CFR 64.1200, analyze the actual calling "
                    "technology, message content, destination, consent, and applicable "
                    "do-not-call requirements; business recipients and manually initiated "
                    "calls do not erase every federal or state restriction. Check "
                    "state rules before selecting calling hours or recording discovery "
                    "sessions. Store the recipient's relevant consent evidence, source, "
                    "timestamp, permitted sender, and requested channel rather than "
                    "treating a purchased lead list as authorization. The scripts below "
                    "are exact spoken or written bodies, not a substitute for production "
                    "sender identification, postal-address fields, unsubscribe controls, "
                    "or jurisdiction-specific disclosures. Deploy scripts only after "
                    "the relevant contact eligibility check. Honor a stop request "
                    "across connected systems promptly, and prevent a CRM resynchronization "
                    "from reactivating suppression records. When permission cannot be "
                    "established, use search content or a requested reply instead of "
                    "switching channels to continue unwanted outreach."
                ),
                (
                    "Discovery should expose contractual mismatches before anyone quotes a cheaper "
                    "unit rate. Ask whether GPU spend purchases exclusive reservations or "
                    "interruptible consumption, whether prompts may leave a named region, "
                    "whether outputs include protected health information, and whether "
                    "the customer needs payload retention disabled across every fallback. "
                    "For voice, ask who supplies numbers, originates traffic, obtains "
                    "permission, answers traceback requests, and bears emergency-service "
                    "duties where applicable. For messaging, inspect the opt-in journey "
                    "and campaign use case rather than accepting a screenshot of a "
                    "registration status alone. Quote a pilot with a wallet ceiling, "
                    "named units, a stop condition, and a documented migration path. "
                    "An illustrative $300 prepaid GPU pilot at $3.00 per accepted "
                    "hour funds 100 hours; at the assumed $1.05 upstream rate, "
                    "its $195 retained contribution is not owner profit. If the "
                    "customer needs a $4.00 eligible route under a $3.00 price "
                    "ceiling, pause or revise the order rather than quietly accepting "
                    "a negative spread. Record objections as concrete constraints, "
                    "not permission to exaggerate availability or savings. Send a "
                    "written recap identifying assumptions, evidence still required, "
                    "and excluded services. The strongest close is a bounded test "
                    "whose bill, retention behavior, and exit procedure match the "
                    "signed schedules."
                ),
            ],
            "table": {
                "caption": "Verbatim Outreach and Discovery Scripts with Deployment Conditions",
                "headers": [
                    "Channel and intended buyer interaction context",
                    "Verbatim script body for the stated interaction",
                    "Required evidence before this script is deployed",
                    "Stop condition and appropriate operating fallback response",
                ],
                "rows": [
                    [
                        "Commercial email introducing a relevant GPU comparison service",
                        "'This is a commercial introduction about GPU capacity brokerage. We can compare your required model, region, reservation term, and retention settings against a dated written quote. Reply if you want that comparison, or use unsubscribe to stop these emails.'",
                        "Accurate sender identity postal address and working unsubscribe controls",
                        "Suppress further commercial email after a valid opt-out request",
                    ],
                    [
                        "Requested comparison page explaining competitor pricing methodology clearly",
                        "'This independent comparison uses public prices captured on the date shown. We identify region, hardware, commitment length, and excluded fees. We are not affiliated with the providers compared. Check the linked source before purchasing.'",
                        "Dated source captures and genuinely comparable unit definitions",
                        "Withdraw savings claims when equivalent current evidence disappears",
                    ],
                    [
                        "GPU discovery call with an eligible business prospect",
                        "'Are you buying reserved GPU time or accepted inference units? Which model, region, isolation boundary, and payload-retention settings are mandatory? We will exclude any route that cannot meet those requirements.'",
                        "Contact eligibility review and an accurate supported-capability inventory",
                        "Decline unsupported requirements rather than silently substituting resources",
                    ],
                    [
                        "Enterprise privacy discussion before routing any customer payload",
                        "'Which request fields and outputs must remain unlogged, and may billing metadata be retained? We will list every permitted subprocessor and will not enable a fallback whose retention terms conflict with your order.'",
                        "Verified subprocessor settings and tested payload-log suppression behavior",
                        "Keep customer traffic disabled until retention obligations align",
                    ],
                    [
                        "Voice discovery conversation before proposing wholesale termination rates",
                        "'Who originates your calls, supplies the numbers, maintains recipient permission, and responds to traceback requests? We need the traffic purpose, destinations, and provider responsibilities before offering a production route.'",
                        "Documented traffic purpose customer identity and applicable provider analysis",
                        "Reject traffic that lacks supportable permission or traceability",
                    ],
                    [
                        "Messaging onboarding discussion for a proposed business campaign",
                        "'Please show the actual opt-in journey, sender identity, sample messages, and stop response. Campaign registration does not establish recipient permission. We will activate only the reviewed use case and supported routes.'",
                        "Reproducible opt-in evidence plus required carrier campaign registration",
                        "Suspend changed or rejected campaigns instead of aggregator hopping",
                    ],
                    [
                        "Written pilot recap following completed discovery and qualification",
                        "'Your proposed pilot is capped at $300 prepaid and 100 accepted GPU-hours at $3.00 per hour. The order will name hardware, region, billing rules, retention settings, and the stop condition before you fund the wallet.'",
                        "Executable order and supplier capacity supporting the illustrative quote",
                        "Revise the order if available eligible capacity changes",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A capacity spread survives only when the rights, meter, route, and customer promise describe the same service.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Create separate compute, inference, voice, messaging, and IPv4 responsibility records identifying supplier rights and the actual contracting provider.",
        "Resolve applicable FCC Form 499-A, Section 214, STIR/SHAKEN, Robocall Mitigation Database, state, and emergency-service responsibilities before activating affected services.",
        "Attach signed scope, fee-trigger, acceptable-use, retention, IP, liability, dispute, anti-circumvention, renewal, and exit schedules to every production order.",
        "Test prepaid concurrency controls, customer meters, tenant isolation, payload-log suppression, supplier interruption, and permitted routing fallbacks with synthetic traffic.",
        "Reconcile canonical gross billings, 65% retained contribution, remaining modeled costs, and owner profit separately from the ASC 606 presentation assessment.",
        "Publish only sourced competitor comparisons and deploy outreach scripts through channel-specific eligibility, suppression, identification, and evidence-retention controls.",
    ],
    "statutory_citations": [
        {
            "title": "47 U.S.C. 153 — Communications Act definitions",
            "url": "https://www.law.cornell.edu/uscode/text/47/153",
            "relevance": "Supports service classification by actual offering rather than a reseller's marketing label.",
        },
        {
            "title": "47 U.S.C. 214 — Extensions and discontinuances of service",
            "url": "https://www.law.cornell.edu/uscode/text/47/214",
            "relevance": "Provides the statutory basis for applicable telecommunications authorization analysis.",
        },
        {
            "title": "47 CFR Part 63 — Authorizations and service discontinuance",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-63",
            "relevance": "Contains implementing requirements relevant to domestic and international telecommunications authority and discontinuance.",
        },
        {
            "title": "47 CFR 54.711 — Contributor reporting requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-54.711",
            "relevance": "Supports evaluation of applicable contribution reporting alongside current FCC Form 499-A instructions.",
        },
        {
            "title": "47 CFR 64.6301 — Caller ID authentication",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6301",
            "relevance": "Defines caller ID authentication obligations applicable to covered voice service arrangements.",
        },
        {
            "title": "47 CFR 64.6305 — Robocall mitigation and certification",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6305",
            "relevance": "Addresses covered provider mitigation, certification, database, and traffic acceptance responsibilities.",
        },
        {
            "title": "47 U.S.C. 227 — Restrictions on telephone equipment use",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Establishes TCPA constraints relevant to calling and messaging use cases.",
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Implements federal calling, consent, identification, and do-not-call requirements for applicable communications.",
        },
        {
            "title": "47 U.S.C. 222 — Privacy of customer information",
            "url": "https://www.law.cornell.edu/uscode/text/47/222",
            "relevance": "Requires separate evaluation of telecommunications customer-information obligations where applicable.",
        },
        {
            "title": "45 CFR 164.504 — Uses and disclosures: organizational requirements",
            "url": "https://www.ecfr.gov/current/title-45/section-164.504",
            "relevance": "Specifies business associate agreement requirements relevant to qualifying health-data processing relationships.",
        },
        {
            "title": "California Civil Code 1798.100 — Consumer information duties",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100.",
            "relevance": "Informs applicable privacy notices, processing limitations, and contractual requirements for covered customer-data arrangements.",
        },
        {
            "title": "California Public Utilities Code 1001 — Certificates of public convenience",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PUC&sectionNum=1001.",
            "relevance": "Illustrates state authority questions requiring service-specific analysis rather than blanket cloud-service licensing assumptions.",
        },
        {
            "title": "Florida Statutes 501.059 — Telephone solicitation",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0501/Sections/0501.059.html",
            "relevance": "Adds state-specific telephone-solicitation requirements requiring review before deploying calling or messaging campaigns.",
        },
        {
            "title": "15 U.S.C. 7704 — Commercial electronic mail requirements",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email identification, truthful transmission information, postal-address disclosure, and opt-out handling.",
        },
        {
            "title": "15 U.S.C. 1125(a) — False designations and misleading descriptions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": "Informs competitor comparison, affiliation, source-confusion, and advertising-claim controls.",
        },
        {
            "title": "15 U.S.C. 45 — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Supports substantiation of savings, service-capability, privacy, and retention representations.",
        },
    ],
}
