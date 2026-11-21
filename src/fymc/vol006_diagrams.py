from __future__ import annotations

VOLUME_006_SUBTITLE = (
    "The Complete Playbook for Productized AI Agencies: "
    "$100,000–$1,000,000 USD in Annual Implementation and Retainer Revenue, "
    "Built from a 2 FT + 3 C (5 People) Pod"
)

VOLUME_006_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Fixed-Scope AI Implementation Studio",
        "subtitle": (
            "Sell bounded workflow sprints with measurable acceptance tests, "
            "explicit system permissions, and a priced support handoff."
        ),
        "audience": (
            "Technical founders and implementation consultants serving B2B "
            "operations teams with repeatable document and service workflows."
        ),
        "research_basis": (
            "18 U.S.C. 1030 addresses unauthorized computer access; "
            "17 U.S.C. 204(a) requires a signed writing for transfers of "
            "copyright ownership other than by operation of law. Translate "
            "these boundaries into written access scope, client-owned service "
            "accounts, and explicit assignments or licenses for deliverables. "
            "These sources support operating controls, not demand estimates."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/18/1030",
            "https://www.law.cornell.edu/uscode/text/17/204",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Managed Automation Reliability Pod",
        "subtitle": (
            "Turn accepted implementations into bounded retainers for "
            "quality evaluation, incident response, and usage control."
        ),
        "audience": (
            "Small AI delivery teams supporting existing client workflows "
            "where output quality and data handling determine renewal."
        ),
        "research_basis": (
            "15 U.S.C. 45 prohibits unfair or deceptive practices. "
            "For covered California businesses, Civil Code 1798.100(d) "
            "requires specified contractual terms when personal information "
            "is disclosed to service providers, contractors, or third parties. "
            "Use evidence-backed service claims, purpose-limited processing "
            "terms, and documented monitoring responsibilities."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100."
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Human-Reviewed Healthcare Workflow Studio",
        "subtitle": (
            "Package administrative workflow assistance with restricted "
            "data access, documented review, and a defined support envelope."
        ),
        "audience": (
            "Experienced healthcare implementation operators serving covered "
            "entities with administrative tasks rather than autonomous "
            "clinical decisions."
        ),
        "research_basis": (
            "When an engagement creates a HIPAA business-associate "
            "relationship, 45 CFR 164.504(e) specifies business-associate "
            "contract requirements; 45 CFR 164.312 specifies technical "
            "safeguards for electronic protected health information. "
            "Start with synthetic fixtures, confirm applicable contracts and "
            "safeguards, and retain human review for consequential outputs "
            "as a delivery requirement."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-45/section-164.504",
            "https://www.ecfr.gov/current/title-45/section-164.312",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_006_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-fixed-scope-delivery",
            "process_flow",
            "Productize the Workflow, Not the Promise",
            "Five stages connect authorized intake to a bounded support retainer.",
            1,
            "operating_framework",
            (
                "The Conservative and Base delivery pod has two full-time "
                "employees and three contractors; contractors are people, "
                "not three additional full-time equivalents. Recognized "
                "revenue comprises implementation fees and support retainers."
            ),
            (
                "Client intake workflows, deployment checklists, and usage "
                "and quality monitoring reduce repeated coordination. "
                "Client sales, savings, and transaction volume remain "
                "outside agency revenue."
            ),
            [
                (
                    "Qualify one workflow",
                    "Name the owner, inputs, outputs, and exception queue",
                    1.0,
                    (
                        "Capture the workflow in a structured intake form. "
                        "Inspect representative redacted examples and reject "
                        "projects whose buyer cannot define an acceptance test."
                    ),
                ),
                (
                    "Contract a bounded sprint",
                    "Price one deliverable with explicit change rules",
                    2.0,
                    (
                        "Specify supported systems, transaction limits, "
                        "acceptance criteria, data-processing terms, and IP "
                        "rights. Quote additional connectors and workflow "
                        "branches as separately priced changes."
                    ),
                ),
                (
                    "Build against fixtures",
                    "Implement with client-owned, least-privilege service accounts",
                    3.0,
                    (
                        "Use GitHub for versioned code and n8n or a Python "
                        "worker for orchestration. Keep credentials outside "
                        "prompts; test retrieval boundaries, malformed inputs, "
                        "and retry idempotency with synthetic fixtures."
                    ),
                ),
                (
                    "Evaluate and deploy",
                    "Require evidence before enabling production writes",
                    4.0,
                    (
                        "Run a held-out evaluation set, record failure "
                        "categories, and rehearse rollback. The client owner "
                        "accepts the bounded workflow; consequential outputs "
                        "retain human review."
                    ),
                ),
                (
                    "Operate within limits",
                    "Monitor usage, quality, incidents, and renewal evidence",
                    5.0,
                    (
                        "Track cost per completed task, exception rate, and "
                        "review workload. Define included support hours, "
                        "response windows, usage ceilings, and overage "
                        "pricing before the retainer begins."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-account-cohort",
            "funnel",
            "Convert One Cohort Without Counting It Twice",
            "A nested account funnel separates selling activity from earned revenue.",
            6,
            "illustrative_model",
            (
                "Illustrative single cohort of 200 distinct accounts observed "
                "over 120 days; each account appears at most once per stage. "
                "Counts are planning assumptions rather than observed "
                "conversion benchmarks or annual scorecard inputs."
            ),
            (
                "Sequential conversion is 25%, 40%, 50%, and 40%; overall "
                "conversion is 2%. Four accepted $12,500 implementations "
                "produce $50,000 of implementation revenue under the stated "
                "acceptance assumption; retainers are excluded."
            ),
            [
                (
                    "Selected accounts",
                    "200 accounts with one documented workflow hypothesis",
                    200.0,
                    (
                        "Build a deduplicated CRM cohort with an identifiable "
                        "operations owner, a recurring workflow, and a "
                        "plausible budget. A contact list alone is not "
                        "evidence of buyer intent."
                    ),
                ),
                (
                    "Engaged accounts",
                    "50 accounts enter a two-way workflow conversation",
                    50.0,
                    (
                        "Count substantive replies or booked conversations, "
                        "not email opens. Fifty divided by 200 gives "
                        "25% engagement for the original account cohort."
                    ),
                ),
                (
                    "Qualified discoveries",
                    "20 accounts verify ownership, budget, and accessible inputs",
                    20.0,
                    (
                        "Confirm who can authorize system access and accept "
                        "delivery. Twenty divided by 50 gives 40% qualification; "
                        "accounts without a bounded use case exit the funnel."
                    ),
                ),
                (
                    "Scoped proposals",
                    "10 accounts receive priced, testable implementation offers",
                    10.0,
                    (
                        "Send a fixed-scope statement of work with exclusions, "
                        "client dependencies, acceptance fixtures, and support "
                        "options. Ten divided by 20 gives 50% proposal conversion."
                    ),
                ),
                (
                    "Accepted implementations",
                    "4 accounts complete a $12,500 implementation each",
                    4.0,
                    (
                        "These four accounts are a subset of the ten proposals. "
                        "Four divided by ten gives 40% completion conversion. "
                        "A deposit alone does not establish earned revenue; "
                        "apply the engagement's recognition policy."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-bridge",
            "waterfall",
            "The $550,000 Base-Case Profit Bridge",
            "Six bars reconcile recognized revenue to $165,000 annual owner net profit.",
            3,
            "illustrative_model",
            (
                "Annual USD. First and last bars are totals; the four middle "
                "bars are signed deductions. The $550,000 revenue, 30.0% "
                "margin, and $165,000 owner net profit are canonical. "
                "Expense categories are an illustrative allocation of the "
                "required $385,000 total costs, not additional scorecard facts."
            ),
            (
                "$550,000 - $210,000 - $65,000 - $42,000 - $68,000 = "
                "$165,000; $165,000 / $550,000 = 30.0%. "
                "Do not add the closing profit total as another cash inflow."
            ),
            [
                (
                    "Recognized agency revenue",
                    "$550,000 from accepted implementations and earned retainers",
                    550000.0,
                    (
                        "Illustrative mix: 22 implementations at $15,000 "
                        "produce $330,000; 110 earned client-months of support "
                        "at $2,000 produce $220,000. Neither client revenue "
                        "nor projected automation savings enters this total."
                    ),
                ),
                (
                    "Delivery labor",
                    "Subtract $210,000 for employee and contractor delivery",
                    -210000.0,
                    (
                        "Allocate delivery compensation and associated labor "
                        "burdens across the two full-time and three contractor "
                        "seats. Contractor engagements are fractional; this "
                        "budget is not five full-time salaries. Balance: $340,000."
                    ),
                ),
                (
                    "Client workload costs",
                    "Subtract $65,000 for attributable runtime and service usage",
                    -65000.0,
                    (
                        "Assign model usage, retrieval infrastructure, and "
                        "workflow execution costs to client projects. These "
                        "variable delivery costs sit outside recurring overhead "
                        "in this illustrative bridge. Balance: $275,000."
                    ),
                ),
                (
                    "Recurring operating overhead",
                    "Subtract $42,000 for shared tools and business operations",
                    -42000.0,
                    (
                        "Budget $3,500 monthly for shared software, insurance, "
                        "accounting, and routine administration. This lies "
                        "within the $2,500–$18,000 monthly operating range; "
                        "that range is not the all-in annual cost ceiling. "
                        "Balance: $233,000."
                    ),
                ),
                (
                    "Other recognized costs",
                    "Subtract $68,000 for acquisition, rework, and remaining expenses",
                    -68000.0,
                    (
                        "Illustratively allocate $30,000 to acquisition, "
                        "$20,000 to delivery remediation, and $18,000 to "
                        "remaining recognized expenses. Keep these separate "
                        "from labor and shared overhead; replace allocations "
                        "with actual ledger categories. Balance: $165,000."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$165,000 residual profit at exactly 30.0% margin",
                    165000.0,
                    (
                        "Closing total after all four expense deductions, "
                        "not gross margin or owner take-home after personal "
                        "taxes. No client transaction volume or unrealized "
                        "efficiency benefit contributes to this residual."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-delivery-yield",
            "horizontal_bars",
            "Compare Sub-Niches by Delivery-Hour Yield",
            "Five fixed-scope offers expose the labor economics behind the price.",
            2,
            "illustrative_model",
            (
                "Numeric values are illustrative implementation-fee USD per "
                "planned delivery hour, before labor, software, acquisition, "
                "and overhead costs. Hours include discovery, build, testing, "
                "and handoff. These are not net margins or market-rate claims."
            ),
            (
                "Rank only similarly bounded offers. Rework expands the "
                "denominator: a $12,000 sprint planned for 60 hours falls "
                "from $200 to $150 per hour if delivery reaches 80 hours."
            ),
            [
                (
                    "B2B support triage",
                    "$12,000 fee divided by 60 hours equals $200/hour",
                    200.0,
                    (
                        "Connect Zendesk to a client-approved knowledge source "
                        "for classification and draft replies. Exclude automatic "
                        "refunds and account changes; collect the fixed fee "
                        "through milestone invoices."
                    ),
                ),
                (
                    "Sales operations routing",
                    "$10,000 fee divided by 55 hours equals $181.82/hour",
                    10000.0 / 55.0,
                    (
                        "Normalize HubSpot intake and suggest routing using "
                        "documented account rules. Exclude purchased contact "
                        "enrichment and autonomous outbound campaigns; the fee "
                        "does not depend on client sales volume."
                    ),
                ),
                (
                    "Accounts payable intake",
                    "$15,000 fee divided by 90 hours equals $166.67/hour",
                    15000.0 / 90.0,
                    (
                        "Extract invoice fields and propose purchase-order "
                        "matches for accounting review. Exclude bank-detail "
                        "changes and payment execution; invoice principal "
                        "belongs to the client, not agency revenue."
                    ),
                ),
                (
                    "Internal knowledge retrieval",
                    "$9,000 fee divided by 60 hours equals $150/hour",
                    150.0,
                    (
                        "Index approved SharePoint documents with preserved "
                        "access boundaries and source citations. Exclude "
                        "unbounded document cleanup; test cross-user retrieval "
                        "leakage before allowing employee access."
                    ),
                ),
                (
                    "Contract intake assistance",
                    "$14,000 fee divided by 100 hours equals $140/hour",
                    140.0,
                    (
                        "Extract renewal dates and route documents to the "
                        "client's designated reviewers. Exclude autonomous "
                        "contract interpretation and signature authority; "
                        "price document-format variation explicitly."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-risk-decisions",
            "decision_tree",
            "Four Checks Before Production Access",
            "Each failed branch has a concrete remediation path.",
            5,
            "operating_framework",
            (
                "Numeric values identify ordered checks, not probabilities "
                "or risk scores. A passing branch proceeds to the next "
                "check; a failing branch pauses the affected activity. "
                "Statutory applicability depends on the client and data."
            ),
            (
                "Keep written access authorization, applicable processing "
                "terms, deliverable rights, and evaluation evidence in the "
                "engagement record. Use synthetic data while unresolved "
                "production dependencies are corrected."
            ),
            [
                (
                    "Authorized system access?",
                    "Yes: scope credentials; no: remain in the sandbox",
                    1.0,
                    (
                        "18 U.S.C. 1030 addresses unauthorized access and "
                        "exceeding authorized access. Record the client's "
                        "authority, named systems, permitted operations, "
                        "credential expiry, and revocation owner before "
                        "connecting any production service account."
                    ),
                ),
                (
                    "Permitted data processing?",
                    "Yes: minimize data; no: repair contracts and routing",
                    2.0,
                    (
                        "Where applicable, California Civil Code 1798.100(d) "
                        "requires specified disclosure-contract terms. For "
                        "HIPAA business-associate work, apply 45 CFR "
                        "164.504(e) contracts and 164.312 technical safeguards. "
                        "Document subprocessors, retention, deletion, and "
                        "permitted destinations before transmitting client data."
                    ),
                ),
                (
                    "Usable input and output rights?",
                    "Yes: record licenses; no: replace restricted materials",
                    3.0,
                    (
                        "Inventory client inputs, reusable agency components, "
                        "and third-party dependencies. Under 17 U.S.C. 204(a), "
                        "copyright ownership transfers generally require a "
                        "signed writing. Assign or license rights actually "
                        "held; do not promise exclusive ownership of every "
                        "model-generated artifact."
                    ),
                ),
                (
                    "Supported claims and safe execution?",
                    "Yes: limited release; no: revise claims or workflow",
                    4.0,
                    (
                        "15 U.S.C. 45 prohibits unfair or deceptive practices. "
                        "Retain evidence for advertised performance under "
                        "stated conditions. As operating controls, require "
                        "human review for consequential decisions, test "
                        "prompt-injection resistance, and verify rollback."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats, Two Explicit Scale Additions",
            "Separate commercial ownership, engineering, quality, and bounded support.",
            11,
            "operating_framework",
            (
                "Each numeric value is one person-slot, not one full-time "
                "equivalent. The first five seats form the Conservative "
                "and Base pod: 2 FT + 3 C. Activate the final two seats "
                "only for the Scaled pod: 3 FT + 4 C."
            ),
            (
                "Canonical annual revenue / margin / owner net profit: "
                "Conservative $100,000 / 20% / $20,000; "
                "Base $550,000 / 30.0% / $165,000; "
                "Scaled $1,000,000 / 40% / $400,000. "
                "Revenue per person-slot is $20,000, $110,000, and "
                "approximately $142,857 respectively; these are not "
                "revenue-per-full-time-equivalent measures."
            ),
            [
                (
                    "FT 1: commercial and product lead",
                    "Core seat owning scope, pricing, and client decisions",
                    1.0,
                    (
                        "Own discovery, signed statements of work, change "
                        "pricing, and renewal evidence. Resolve scope conflicts "
                        "without allowing unpaid features to enter the "
                        "engineering queue."
                    ),
                ),
                (
                    "FT 2: technical delivery lead",
                    "Core seat owning architecture, access, and production release",
                    1.0,
                    (
                        "Own integration boundaries, credential design, "
                        "evaluation thresholds, and rollback readiness. Review "
                        "contractor changes and maintain the deployable "
                        "reference implementation."
                    ),
                ),
                (
                    "C 1: integration engineer",
                    "Core contractor building connectors and reliable workflow execution",
                    1.0,
                    (
                        "Implement API mappings, retries, idempotency, and "
                        "queue handling within the purchased scope. Submit "
                        "versioned changes with reproducible tests and "
                        "document external API limits."
                    ),
                ),
                (
                    "C 2: evaluation specialist",
                    "Core contractor testing quality, permissions, and adversarial inputs",
                    1.0,
                    (
                        "Maintain held-out fixtures, score output defects, "
                        "and test retrieval isolation. Report failed cases "
                        "separately from aggregate accuracy so severe "
                        "exceptions remain visible."
                    ),
                ),
                (
                    "C 3: workflow and support specialist",
                    "Core contractor documenting handoffs and handling bounded support",
                    1.0,
                    (
                        "Map operator procedures, prepare training material, "
                        "and triage support requests. Escalate quality "
                        "regressions to the technical lead and route "
                        "enhancement requests into priced change work."
                    ),
                ),
                (
                    "FT 3: scaled service operations lead",
                    "Scaled-only addition managing capacity, incidents, and renewal readiness",
                    1.0,
                    (
                        "Join when contracted workload supports a dedicated "
                        "operations seat. Own service calendars, client "
                        "reporting, incident coordination, and retainer "
                        "capacity rather than duplicating the sales role."
                    ),
                ),
                (
                    "C 4: scaled implementation specialist",
                    "Scaled-only addition expanding delivery capacity for repeatable packages",
                    1.0,
                    (
                        "Take repeatable connector or migration work from "
                        "the technical lead. Activate against signed delivery "
                        "backlog; preserve the same tests and documentation "
                        "rather than creating a separate custom-service line."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Deploy $30,000 Without Funding Unbounded Custom Work",
            "Four capital buckets distinguish setup spending from operating runway.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD allocations in one illustrative "
                "$30,000 startup stack, inside the canonical $5,000–$60,000 "
                "range. They are not additional annual expenses in the "
                "Base waterfall. Cash reserved for future spending is "
                "not an expense merely because it is allocated."
            ),
            (
                "$6,000 + $4,500 + $3,000 + $16,500 = $30,000. "
                "The $16,500 reserve covers three months at an assumed "
                "$5,500 monthly cash burn, within the $2,500–$18,000 "
                "operating range. A first deal may take 1–4 months."
            ),
            [
                (
                    "Reusable delivery foundation",
                    "$6,000 allocated to fixtures, reference workflows, and setup",
                    6000.0,
                    (
                        "Allocate 20% to synthetic datasets, connector "
                        "templates, evaluation harnesses, and deployment "
                        "automation. Build one repeatable workflow package "
                        "before purchasing tools for additional niches."
                    ),
                ),
                (
                    "Commercial validation assets",
                    "$4,500 allocated to discovery, demonstrations, and targeted selling",
                    4500.0,
                    (
                        "Allocate 15% to buyer interviews, a measured "
                        "demonstration, concise offer materials, and CRM "
                        "setup. Track qualified conversations rather than "
                        "buying broad traffic before scope and pricing work."
                    ),
                ),
                (
                    "Contracts and secure workspace",
                    "$3,000 allocated to engagement documents and access setup",
                    3000.0,
                    (
                        "Allocate 10% to reviewed engagement templates, "
                        "processing terms, insurance setup, a password "
                        "manager, and segregated workspaces. Distinguish "
                        "one-time setup from later recurring subscriptions."
                    ),
                ),
                (
                    "Working-capital reserve",
                    "$16,500 held for operating burn and collection delays",
                    16500.0,
                    (
                        "Allocate 55% to cash runway rather than discretionary "
                        "features. At $5,500 monthly burn, a fourth month "
                        "needs another $5,500; reduce burn or secure additional "
                        "funding before committing to unfunded obligations."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-offer-sprint",
            "timeline_roadmap",
            "Build a Sellable Delivery System in 30 Days",
            "Four weekly milestones produce evidence, not an assumed first-month deal.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone-ending day numbers. The "
                "canonical time to first deal is 1–4 months; this sprint "
                "creates sales and delivery readiness without assuming "
                "signed revenue by day 30."
            ),
            (
                "Finish with one bounded offer, a tested reference workflow, "
                "a permissioned pilot plan, and a measured sales cohort. "
                "Continue discovery and runway management if the first "
                "contract has not closed."
            ),
            [
                (
                    "Days 1-7",
                    "Choose one buyer, one workflow, and one acceptance test",
                    7.0,
                    (
                        "Interview five target operators, map the current "
                        "workflow, and document measurable pain. Produce an "
                        "offer sheet with explicit exclusions and an initial "
                        "unit-cost worksheet; interview counts are targets, "
                        "not evidence of demand by themselves."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build the reference workflow and a held-out test set",
                    14.0,
                    (
                        "Implement with synthetic data, define failure "
                        "categories, and test retries, access boundaries, "
                        "and rollback. Measure delivery hours and runtime "
                        "costs so the fixed fee reflects actual effort."
                    ),
                ),
                (
                    "Days 15-21",
                    "Package commercial terms and demonstrate bounded performance",
                    21.0,
                    (
                        "Prepare the statement of work, processing terms, "
                        "access checklist, and support schedule. Demonstrate "
                        "results against the held-out fixtures; use real "
                        "client data only after the applicable access and "
                        "processing requirements are satisfied."
                    ),
                ),
                (
                    "Days 22-30",
                    "Run qualified sales conversations and rehearse the handoff",
                    30.0,
                    (
                        "Issue scoped proposals to qualified buyers and "
                        "record objections by category. Rehearse intake, "
                        "deployment, incident response, and retainer reporting. "
                        "If no contract closes, continue the 1–4 month "
                        "selling plan without booking hypothetical revenue."
                    ),
                ),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(
                    label=label,
                    value=value,
                    numeric_value=float(number),
                    detail=detail,
                )
                for label, value, number, detail in stages
            ],
        )
        for (
            identifier,
            kind,
            title,
            subtitle,
            chapter,
            tag,
            note,
            caption,
            stages,
        ) in specs
    ]
