from __future__ import annotations


def build_volume_036_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-036-gpu-compute-and-telecom-capacity-arbitrage",
        "volume_id": "vol-036-gpu-compute-and-telecom-capacity-arbitrage",
        "title": "GPU Compute & Telecom Capacity Arbitrage — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for GPU Reservation Spreads, "
            "Metered Inference Routing, Wholesale Telecom Capacity, Prepaid "
            "Working Capital, Evidence-Based Controls, and Small-Team Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal, Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify one executable capacity spread before committing cash. "
                    "Translate supplier reservations, customer demand, workload restrictions, "
                    "and telecom permissions into comparable units, documented rights, "
                    "and measurable loss limits. Separate attractive quoted prices from "
                    "capacity that the operator can actually deliver and collect."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one initial lane: reserved GPU slicing, routed inference, "
                        "SIP termination, registered messaging, or authorized IPv4 leasing. "
                        "Record the buyer, supplier, service geography, settlement currency, "
                        "and billable unit before comparing any headline prices or annualized spreads."
                    ),
                    (
                        "Obtain dated supplier quotes and a buyer demand artifact. "
                        "Read resale permissions, cancellation terms, minimum commitments, "
                        "and usage restrictions together. A customer deposit does not "
                        "repair a supplier agreement that prohibits the proposed resale arrangement."
                    ),
                    (
                        "Normalize every quote to its actual charging basis, including "
                        "GPU-hours, input and output tokens, rounded call duration, "
                        "message segments, or address-months. Include setup fees and "
                        "quality requirements before calculating a spread or selecting a route."
                    ),
                    (
                        "Interview the customer about workload behavior and traffic origin. "
                        "Require identity, payment authority, intended use, and relevant "
                        "permission evidence. Reject concealed crypto-mining, unauthorized "
                        "network access, or abusive calling rather than attempting to price those risks."
                    ),
                    (
                        "Assign a specific operator to each unresolved condition and "
                        "place an expiry date on every quote. Advance only when "
                        "the customer purchase, upstream capacity, payment arrangement, "
                        "and operational restrictions describe the same deliverable service."
                    ),
                ],
                "fields": [
                    field(
                        "Initial lane and executable opportunity",
                        "textarea",
                        (
                            "Describe one capacity product, its customer problem, delivery "
                            "region, upstream resource, and charging unit. Explain why "
                            "the buyer will pay more than the operator's fully loaded "
                            "acquisition cost."
                        ),
                        (
                            "Start with private H100 batch inference for two document-processing "
                            "companies in one U.S. region. Reserve one eight-GPU server "
                            "for $8,000 monthly and sell measured GPU-hours at $2.40. "
                            "Customers value isolated queues, predictable throughput, and prepaid "
                            "invoices rather than ownership of hardware."
                        ),
                    ),
                    field(
                        "Counterparty identity and payment authority",
                        "textarea",
                        (
                            "Record customer and supplier legal identities, authorized signers, "
                            "billing contacts, business-purpose evidence, and payment verification. "
                            "Specify what evidence will be retained without unnecessarily "
                            "copying sensitive identity documents into operational systems."
                        ),
                        (
                            "Customer A supplies its entity registration, company-domain contact, "
                            "signed order, and payment authorization from its controller. "
                            "The supplier provides its contracting entity and bank verification. "
                            "The operator stores verification status and restricted evidence "
                            "references, while support staff see only account identifiers."
                        ),
                    ),
                    field(
                        "Reservation rights and supplier concentration",
                        "textarea",
                        (
                            "Capture reservation duration, renewal notice, resale rights, "
                            "support response, hardware replacement, and concentration exposure. "
                            "Identify obligations that continue after a customer cancels "
                            "and the exact mechanism for reducing those commitments."
                        ),
                        (
                            "The supplier permits managed-service resale but prohibits transferring "
                            "its control-panel credentials. The $8,000 reservation runs for "
                            "one month with seven days' renewal notice. Customer cancellation "
                            "does not release that charge. A second supplier offers tested "
                            "replacement capacity without an annual commitment."
                        ),
                    ),
                    field(
                        "GPU generation and isolation fit",
                        "textarea",
                        (
                            "Specify the GPU model, memory requirement, partitioning method, "
                            "interconnect dependency, driver compatibility, and tenant boundary. "
                            "Require a workload benchmark rather than treating H100, H200, "
                            "and B200 capacity as interchangeable inventory."
                        ),
                        (
                            "The first workload fits one 80 GB H100 and requires "
                            "no cross-node interconnect. MIG is considered only after verifying "
                            "supported profiles on the exact hardware. Regulated customer "
                            "jobs receive dedicated hosts; neither Kubernetes namespaces nor "
                            "a quoted GPU fraction alone establish adequate isolation."
                        ),
                    ),
                    field(
                        "Inference token and quality normalization",
                        "textarea",
                        (
                            "Define input, output, cached-input, and retry billing separately. "
                            "Specify the model version, quality benchmark, latency objective, "
                            "and data-processing region required before two provider offers "
                            "can be compared or substituted."
                        ),
                        (
                            "A request averages 2,000 input and 500 output tokens. "
                            "At $1 and $4 per million respectively, upstream cost is "
                            "$0.004 before retries. The customer pays $0.007. Only providers "
                            "passing the same 200-document accuracy set and region restriction "
                            "may receive this traffic."
                        ),
                    ),
                    field(
                        "SIP and messaging demand qualification",
                        "textarea",
                        (
                            "Describe traffic purpose, destination mix, customer permissions, "
                            "number ownership, and charging increments. Distinguish voice "
                            "minutes from SMS segments, and document carrier surcharges "
                            "that could consume an apparently positive wholesale spread."
                        ),
                        (
                            "The buyer requests 200,000 domestic support-call minutes monthly, "
                            "not outbound prospecting. Compare 60/60 and 6/6 duration rounding "
                            "before accepting a $0.004 upstream rate. A separate messaging "
                            "order forecasts 30,000 segments, with brand registration, campaign "
                            "approval, and carrier fees priced independently."
                        ),
                    ),
                    field(
                        "IPv4 authority and deliverability evidence",
                        "textarea",
                        (
                            "Identify the address holder, contractual leasing authority, "
                            "routing permissions, reputation evidence, and return process. "
                            "Separate address-use rights from ownership claims, and specify "
                            "how routing incidents affect the customer service promise."
                        ),
                        (
                            "The lessor documents authority over a /24 containing 256 "
                            "addresses and issues a letter authorizing the agreed announcement. "
                            "The operator checks registry records, route visibility, and blocklist "
                            "history before pricing address-months. The contract requires route "
                            "withdrawal and credential removal within 24 hours of termination."
                        ),
                    ),
                    field(
                        "Qualified demand and commitment coverage",
                        "textarea",
                        (
                            "Quantify customer demand using signed minimums, prepaid balances, "
                            "measured history, and expected concurrency. Distinguish expressions "
                            "of interest from obligations that support a reservation, "
                            "and identify correlated customer churn exposure."
                        ),
                        (
                            "Two customers each sign a $5,000 monthly minimum covering "
                            "2,083.33 GPU-hours at $2.40, with true-up for additional use. "
                            "Their combined $10,000 commitment exceeds the $8,000 reservation. "
                            "Both serve seasonal document workflows, so the operator still "
                            "models simultaneous demand contraction and renewal loss."
                        ),
                    ),
                    field(
                        "Spread floor and repricing trigger",
                        "textarea",
                        (
                            "Calculate the initial spread after delivery costs, then "
                            "define price floors, quote expiry, and repricing rights. "
                            "State how GPU generation changes or carrier rate updates "
                            "will be handled without silently changing contracted quality."
                        ),
                        (
                            "At 4,800 sold GPU-hours, revenue is $11,520 against an "
                            "$8,000 server commitment. Another $600 of direct delivery "
                            "cost leaves $2,920 before shared expenses. Quotes expire after "
                            "72 hours; renewal pricing is reviewed whenever comparable "
                            "qualified capacity falls 15% or more."
                        ),
                    ),
                    field(
                        "Underwriting decision and loss boundary",
                        "textarea",
                        (
                            "Write the accept, revise, or reject decision with "
                            "named evidence, outstanding conditions, exposure ceiling, and "
                            "decision owner. Include objective stop conditions for customer "
                            "abuse, supplier failure, and deteriorating demand."
                        ),
                        (
                            "Accept a one-month pilot after both customer payments settle "
                            "and the supplier signs resale permission. Limit upstream exposure "
                            "to $8,000 and prohibit automatic annual renewal. Suspend new "
                            "jobs when available prepaid credit reaches the reservation buffer; "
                            "terminate abusive workloads under the documented AUP process."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner signs a dated underwriting record containing verified "
                    "counterparties, permitted resale, normalized units, demand evidence, "
                    "an explicit cash-exposure ceiling, and a tested alternative supplier."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile the canonical annual scenarios while keeping gross "
                    "customer billings, upstream commitments, retained contribution, and "
                    "owner profit separate. Calculate reservation break-even, prepaid "
                    "liabilities, settlement delays, and refund reserves so accounting "
                    "profit never substitutes for available operating cash or funded delivery capacity."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the three canonical scenarios exactly before modeling "
                        "individual products. Apply the 65% retained share consistently "
                        "and calculate owner profit against both gross billings and "
                        "retained contribution. Do not substitute customer business revenue for operator revenue."
                    ),
                    (
                        "Build a separate monthly cash schedule for reservations, "
                        "contractors, platform overhead, refunds, and payment settlement. "
                        "The stated monthly overhead range is not a license "
                        "to omit other expenses required to reconcile the annual owner-profit figures."
                    ),
                    (
                        "Treat customer prepayments as delivery obligations until earned "
                        "under the applicable accounting treatment. Separate available "
                        "spendable cash from restricted balances, processor holds, tax "
                        "collections, and amounts needed to complete already accepted customer usage."
                    ),
                    (
                        "Calculate GPU economics at several utilization levels and "
                        "telecom economics using rounded billable units. Include payment "
                        "fees, retries, service credits, and unused commitments. Reconcile "
                        "each experimental lane separately rather than forcing every product to retain 65%."
                    ),
                    (
                        "Stress the cash schedule with a delayed payout, a "
                        "customer cancellation, and a supplier price increase. Record "
                        "the funding source and stop condition for each deficit. "
                        "Approve growth only when both contribution and near-term liquidity remain positive."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative canonical reconciliation",
                        "textarea",
                        (
                            "Enter gross annual billings, upstream allocation, retained "
                            "contribution, remaining expenses, owner profit, and both "
                            "margin denominators. Preserve the canonical staffing assumption "
                            "and distinguish this annual benchmark from a particular pilot quotation."
                        ),
                        (
                            "Conservative: $150,000 gross billings less $52,500 upstream allocation "
                            "equals $97,500 retained contribution. Deduct $70,500 remaining expenses "
                            "to produce $27,000 annual owner net profit. Gross margin "
                            "is 18%; retained net margin is 27.69%. Staffing is "
                            "one full-time operator plus two contractors."
                        ),
                    ),
                    field(
                        "Base canonical reconciliation",
                        "textarea",
                        (
                            "Reconcile the Base case to its exact annual owner "
                            "profit and monthly equivalents. Identify upstream cost separately "
                            "from remaining expenses so supplier commitments cannot be "
                            "deducted twice or omitted from liquidity planning."
                        ),
                        (
                            "Base: $675,000 gross billings less $236,250 upstream allocation "
                            "equals $438,750 retained contribution. Remaining expenses of $249,750 "
                            "leave $189,000 owner profit: 28.0% of gross and 43.08% "
                            "of retained contribution. Monthly equivalents are $56,250 gross "
                            "and $15,750 profit, with one employee and two contractors."
                        ),
                    ),
                    field(
                        "Scaled reconciliation and presentation policy",
                        "textarea",
                        (
                            "Enter the Scaled case and document whether accounting "
                            "presentation is gross or net after a principal-versus-agent "
                            "assessment. Treat retained share as the scorecard convention, "
                            "not automatic proof of ASC 606 classification."
                        ),
                        (
                            "Scaled: $1,200,000 gross less $420,000 upstream equals $780,000 "
                            "retained contribution; $324,000 remaining expenses leave $456,000 profit. "
                            "Margins are 38% gross and 58.46% retained, with two "
                            "employees and three contractors. The accountant documents control "
                            "and principal-versus-agent conclusions under ASC 606-10-55-36 through 55-40."
                        ),
                    ),
                    field(
                        "GPU utilization and break-even calculator",
                        "textarea",
                        (
                            "Calculate available GPU-hours, sold hours, realized revenue, "
                            "fixed commitment, variable delivery costs, and break-even utilization. "
                            "Show the effect of unsold reservation hours explicitly "
                            "instead of dividing the supplier bill only by advertised capacity."
                        ),
                        (
                            "Eight GPUs across a 30-day month provide 5,760 GPU-hours. "
                            "At $2.40 revenue and $0.10 variable cost per sold "
                            "hour, an $8,000 commitment breaks even at 3,478.26 hours, "
                            "or 60.39% utilization. At 80% utilization, contribution before "
                            "shared expenses is $2,598.40."
                        ),
                    ),
                    field(
                        "Inference and telecom transaction economics",
                        "textarea",
                        (
                            "Choose one inference request and one telecom transaction "
                            "to cost completely. Include token direction, retries, duration "
                            "rounding, message segmentation, and payment allocation where relevant, "
                            "then state which quality constraints limit cheaper routing."
                        ),
                        (
                            "An inference request billed at $0.007 costs $0.004 upstream "
                            "plus $0.0002 retry allowance, leaving $0.0028 before overhead. "
                            "A 61-second call billed in 60-second increments consumes two "
                            "minutes: $0.020 customer revenue at $0.010 per minute "
                            "less $0.008 upstream leaves $0.012."
                        ),
                    ),
                    field(
                        "Prepaid wallet liability and spend controls",
                        "textarea",
                        (
                            "Record settled prepayments, earned usage, pending reservations, "
                            "refund claims, and available credit. Explain how the "
                            "cash account differs from the customer balance ledger "
                            "and whether any actual third-party escrow arrangement exists."
                        ),
                        (
                            "A customer prepays $10,000 and consumes $2,400 of accepted "
                            "service, leaving a $7,600 service-credit obligation. A $400 "
                            "in-flight reservation reduces available spending to $7,200 without "
                            "earning more revenue. Funds reside in operating cash with "
                            "a designated reserve; the arrangement is not escrow."
                        ),
                    ),
                    field(
                        "Reserve float and payout-delay stress",
                        "textarea",
                        (
                            "Define the reserve amount, funding source, release rule, "
                            "and stress assumptions for refunds and processor holds. "
                            "Prevent overlapping reserve categories from being counted "
                            "as separate available sources of working capital."
                        ),
                        (
                            "Maintain a $12,000 cash buffer: $8,000 for the next "
                            "server payment, $2,000 for expected refunds, and $2,000 "
                            "for payout-delay exposure. A seven-day processor delay cannot "
                            "be funded by counting the same customer wallet balance "
                            "twice. The owner replenishes any reserve draw before expansion."
                        ),
                    ),
                    field(
                        "Startup funding and overhead boundary",
                        "textarea",
                        (
                            "Allocate startup capital within the canonical range and "
                            "reconcile monthly overhead with all other annual expenses. "
                            "Label deposits, refundable balances, prepaid services, and "
                            "expense items separately to avoid distorting the profit calculation."
                        ),
                        (
                            "A $30,000 launch budget funds $8,000 initial capacity, $12,000 "
                            "reserve, $4,000 integration, $3,000 contracting and accounting, and "
                            "$3,000 overhead runway. This fits the $10,000–$60,000 range. "
                            "Base monthly overhead of $8,000 sits within $2,000–$14,000; "
                            "another $12,812.50 monthly covers remaining modeled non-upstream expenses."
                        ),
                    ),
                    field(
                        "Cash conversion and receivables policy",
                        "textarea",
                        (
                            "Map customer collection, processor settlement, supplier due "
                            "dates, and service delivery on an actual monthly "
                            "calendar. Quantify the largest funding gap and specify "
                            "which customers, if any, may receive invoiced credit."
                        ),
                        (
                            "Customer wallets fund on day 25, processor payouts arrive "
                            "on day 28, and the supplier charges $8,000 on day "
                            "1. A payout hold extending to day 5 creates an "
                            "$8,000 temporary funding need. Pilot accounts receive no "
                            "postpaid terms; exceptions require separately funded credit exposure."
                        ),
                    ),
                    field(
                        "Sensitivity decision and capital release",
                        "textarea",
                        (
                            "Run a combined utilization decline and price reduction "
                            "against the lane economics, then state the renewal "
                            "decision. Keep this stress case distinct from the "
                            "fixed canonical annual scenarios used for scorecard comparison."
                        ),
                        (
                            "At 55% utilization, 3,168 GPU-hours sold for $2.04 each "
                            "generate $6,462.72. Subtract $316.80 variable cost and the "
                            "$8,000 commitment: the lane loses $1,854.08 before overhead. "
                            "Do not renew without prepaid minimums or a lower "
                            "reservation price; the canonical scenarios remain unchanged."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three annual scenarios reconcile exactly, the accountant has "
                    "documented revenue presentation, wallet liabilities tie to delivery "
                    "records, and the owner has funded the largest modeled cash deficit."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn an accepted order into reproducible provisioning, metering, "
                    "charging, and reconciliation steps. Establish durable event identities, "
                    "tenant boundaries, credit reservations, and quality checks before "
                    "live traffic. Make duplicate messages, partial failures, and supplier "
                    "disputes recoverable without charging customers twice or losing service evidence."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign stable identifiers to customers, contracts, orders, "
                        "resources, and usage events before provisioning. Document the "
                        "state transitions and responsible service for each object. "
                        "A human-readable invoice number alone is insufficient for safe retries and reconciliation."
                    ),
                    (
                        "Implement the wallet as durable ledger entries with "
                        "atomic reservations and explicit releases. Authenticate provider "
                        "webhooks, deduplicate events, and reconcile settlement independently. "
                        "A successful HTTP response from Stripe does not prove that every subsequent service was delivered."
                    ),
                    (
                        "Run a synthetic workload and a controlled telecom "
                        "test through the complete billing path. Check resource "
                        "identity, timestamps, rounding, quality, customer balance changes, "
                        "and supplier charges before enabling any unattended production volume."
                    ),
                    (
                        "Exercise duplicate delivery, worker crashes, delayed callbacks, "
                        "and exhausted credit deliberately in the test environment. "
                        "Require deterministic outcomes and documented manual repair procedures. "
                        "Do not use live customer requests to discover whether retries duplicate paid work."
                    ),
                    (
                        "Close the pilot with a three-way reconciliation of "
                        "customer usage, internal ledger entries, and supplier records. "
                        "Investigate variance above the written tolerance before issuing "
                        "the final statement or expanding the reservation commitment."
                    ),
                ],
                "fields": [
                    field(
                        "Order identity and state machine",
                        "textarea",
                        (
                            "Define immutable order identifiers, allowed states, transition "
                            "conditions, and expiration behavior. Explain how customer "
                            "cancellation interacts with provisioning already in progress "
                            "and how operators inspect stalled orders without editing balances."
                        ),
                        (
                            "Order ord-036-001 moves from funded to reserved, provisioning, "
                            "active, and closed. A failed deployment enters repair_required "
                            "with its wallet hold intact until resource status is "
                            "confirmed. Cancellation before activation releases the hold only "
                            "after the supplier confirms that no billable allocation remains."
                        ),
                    ),
                    field(
                        "Append-only ledger and balanced postings",
                        "textarea",
                        (
                            "Specify ledger accounts, entry identifiers, immutable corrections, "
                            "and reconciliation ownership. Separate cash receipt, customer "
                            "credit liability, earned service, payment fees, and supplier "
                            "expense rather than representing every event as a balance overwrite."
                        ),
                        (
                            "A settled $1,000 top-up debits cash and credits customer "
                            "credit liability. Accepted service worth $120 debits that "
                            "liability and credits the appropriate earned-service account. A "
                            "$5 correction uses a reversing entry linked to the "
                            "original event; operators never erase the original charge."
                        ),
                    ),
                    field(
                        "Webhook and job idempotency keys",
                        "textarea",
                        (
                            "Choose idempotency keys for payments, usage events, and "
                            "provisioning requests. Define uniqueness constraints, transaction "
                            "boundaries, replay handling, and the recovery path when "
                            "an external action succeeds but the local acknowledgment is lost."
                        ),
                        (
                            "PostgreSQL enforces uniqueness on provider plus event_id for "
                            "webhooks and tenant plus request_id for service jobs. "
                            "A transaction records the event and its ledger effect "
                            "together. After an ambiguous supplier timeout, the worker "
                            "queries the existing allocation identifier before requesting another server."
                        ),
                    ),
                    field(
                        "Tenant isolation and resource assignment",
                        "textarea",
                        (
                            "Record host ownership, tenant mapping, GPU assignment, "
                            "network policy, credential scope, and cleanup verification. "
                            "Identify workloads requiring dedicated hosts and define "
                            "how residual storage or device state is handled between customers."
                        ),
                        (
                            "Tenant acme-01 receives a dedicated worker pool, scoped "
                            "service account, isolated storage prefix, and outbound destination "
                            "policy. Sensitive jobs use a dedicated host. On release, "
                            "the worker revokes credentials, removes encrypted temporary volumes, "
                            "and follows the supplier-supported reset procedure before another tenant starts."
                        ),
                    ),
                    field(
                        "DCGM and billable usage metering",
                        "textarea",
                        (
                            "Define the authoritative billable measurement and explain "
                            "how DCGM telemetry supports verification without replacing "
                            "contract terms. Specify clock synchronization, missing-sample "
                            "handling, and treatment of idle allocations or failed jobs."
                        ),
                        (
                            "The contract charges allocated GPU-seconds, rounded once per "
                            "job to the next whole second. Scheduler allocation timestamps "
                            "determine billing; DCGM reports utilization and health for "
                            "dispute support. Missing telemetry flags review rather than "
                            "creating estimated charges. Failed provisioning before allocation generates no usage."
                        ),
                    ),
                    field(
                        "Atomic credit reservation and settlement",
                        "textarea",
                        (
                            "Describe maximum-charge estimation, balance locking, settlement, "
                            "and release of unused reservations. Include concurrent "
                            "requests and long-running workloads so a positive balance "
                            "check cannot authorize several jobs against the same dollars."
                        ),
                        (
                            "A job reserves $20 from a $100 available balance "
                            "inside a database transaction. A concurrent $90 reservation "
                            "fails because only $80 remains available. When the first "
                            "job finishes at $13.20, settlement earns $13.20 and "
                            "releases $6.80. Interrupted jobs retain holds until reconciliation."
                        ),
                    ),
                    field(
                        "Inference routing and response integrity",
                        "textarea",
                        (
                            "Define the approved provider set, request identity, "
                            "quality checks, streaming behavior, and retry boundaries. "
                            "Explain how LiteLLM or vLLM routing respects "
                            "region restrictions and avoids duplicate customer charges during provider failure."
                        ),
                        (
                            "LiteLLM routes an eligible request to a vLLM endpoint "
                            "only after region and benchmark checks pass. A failure "
                            "before output may trigger one bounded retry. Once streamed "
                            "content reaches the customer, the request is not silently "
                            "replayed; partial-delivery handling follows the published charging rule."
                        ),
                    ),
                    field(
                        "Telecom CDR and message reconciliation",
                        "textarea",
                        (
                            "Identify call-detail and message-event sources, correlation "
                            "keys, final-status rules, and duplicate handling. Specify "
                            "how duration rounding, SMS encoding, carrier fees, "
                            "and delayed delivery receipts affect the customer's final charge."
                        ),
                        (
                            "Call call-104 joins SIP session metadata to the carrier "
                            "CDR using the provider correlation identifier. A 61-second "
                            "connected call becomes two billed minutes under 60/60 terms. "
                            "Messaging counts encoded segments, not screen-visible messages; duplicate "
                            "delivery receipts update status without creating another usage charge."
                        ),
                    ),
                    field(
                        "Failure injection and recovery acceptance",
                        "textarea",
                        (
                            "List reproducible test cases for crashes, duplicate "
                            "events, exhausted credit, supplier outages, and clock "
                            "drift. Define the expected ledger result and "
                            "service outcome for each before marking the pipeline production-ready."
                        ),
                        (
                            "Replay one payment webhook 100 times: exactly one top-up "
                            "must exist. Kill a worker after supplier allocation: "
                            "recovery must adopt the existing server. Submit two jobs "
                            "against the last $10: aggregate reservations cannot exceed "
                            "$10. Shift a test clock five minutes and require an alert."
                        ),
                    ),
                    field(
                        "Daily close and exception ownership",
                        "textarea",
                        (
                            "Set the reconciliation cadence, materiality tolerance, evidence "
                            "location, and repair owner. Explain how corrections "
                            "reach customer statements and how unresolved supplier "
                            "variance affects further purchasing or automatic wallet deductions."
                        ),
                        (
                            "At 09:00 UTC, compare prior-day accepted usage, ledger "
                            "charges, and supplier records. Investigate variance exceeding $10 "
                            "or 0.5%, whichever is lower. The operations contractor "
                            "owns evidence collection; the owner authorizes corrections. Disputed "
                            "usage remains separately tracked until the customer statement is reconciled."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Duplicate-event, concurrency, worker-crash, isolation, and outage tests "
                    "all pass; every pilot charge traces to accepted usage; and the "
                    "daily close has no unresolved variance above the written tolerance."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Map the actual service architecture to contractual, communications, "
                    "privacy, and export requirements. Collect evidence for each "
                    "applicable obligation rather than assuming an upstream carrier "
                    "covers the reseller. Convert findings into named owners, "
                    "service restrictions, renewal dates, and enforceable customer and supplier terms."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Draw the service and contracting chain before selecting "
                        "forms or registrations. Identify who sells to the "
                        "end user, controls traffic, assigns numbers, receives payments, "
                        "and holds customer records. Obligations depend on those facts, not the brokerage label."
                    ),
                    (
                        "Create a requirement register with authoritative citations, "
                        "applicability reasoning, evidence, owner, and review date. "
                        "Separate statutes and FCC rules from carrier policies "
                        "and The Campaign Registry requirements, which can impose additional contractual conditions."
                    ),
                    (
                        "Write customer and supplier addenda around operational facts: "
                        "resale authority, service units, data handling, abuse response, "
                        "refunds, routing restrictions, and termination. Require matching "
                        "upstream terms before promising zero retention or a particular incident response time."
                    ),
                    (
                        "Verify filings and registrations using current official "
                        "instructions and records before launching the affected "
                        "service. Record role-specific exemptions with their supporting "
                        "facts rather than assuming that a small team or prepaid model eliminates obligations."
                    ),
                    (
                        "Test the control behind each signed clause and "
                        "retain dated evidence in access-controlled storage. A "
                        "privacy promise, caller-authentication statement, or tax treatment "
                        "is incomplete until an assigned operator can demonstrate how the service enforces it."
                    ),
                ],
                "fields": [
                    field(
                        "Service-role and jurisdiction determination",
                        "textarea",
                        (
                            "Classify each offered product and contracting role "
                            "using actual architecture, customer geography, and traffic "
                            "flow. Identify federal, state, and carrier requirements "
                            "that need a documented applicability determination before accepting orders."
                        ),
                        (
                            "The pilot sells managed GPU processing and wholesale SIP "
                            "termination to a verified business provider, not residential "
                            "telephone service. The owner documents whether the voice "
                            "arrangement creates telecommunications-provider or interconnected-VoIP obligations. "
                            "State registration, tax, and numbering questions receive separate "
                            "written determinations before broader distribution."
                        ),
                    ),
                    field(
                        "Capacity resale and service addendum",
                        "textarea",
                        (
                            "Draft operative terms covering permitted resale, metering, "
                            "minimum commitments, service credits, termination, and upstream "
                            "dependencies. State which customer remedies remain available "
                            "when a supplier rejects or delays the operator's reimbursement claim."
                        ),
                        (
                            "Addendum: customer purchases allocated GPU-seconds at the stated "
                            "rate; unused prepaid credit follows the written refund "
                            "schedule. Supplier permits managed-service resale and isolates "
                            "customer workloads. Customer service credits are calculated from "
                            "measured unavailability and do not depend on the operator "
                            "first collecting a supplier credit."
                        ),
                    ),
                    field(
                        "Privacy, retention, and telecom records",
                        "textarea",
                        (
                            "Map prompts, outputs, identifiers, call records, and "
                            "billing data to retention periods and access roles. "
                            "Assess applicable privacy duties, including California Civil "
                            "Code 1798.100 and communications-specific customer-information requirements where the service qualifies."
                        ),
                        (
                            "Prompt and output bodies are excluded from logs and "
                            "deleted from transient buffers after completion. Billing metadata "
                            "follows a separately documented schedule. Where applicable, "
                            "47 U.S.C. 222 and 47 CFR 64.2001–64.2011 govern "
                            "CPNI handling. Zero-data-retention contracts identify precisely which "
                            "content categories are excluded from storage."
                        ),
                    ),
                    field(
                        "Workload security and export screening",
                        "textarea",
                        (
                            "Document tenant restrictions, customer and destination screening, "
                            "remote-access controls, and incident procedures. Assess actual "
                            "hardware, software, technology, destination, and end-use facts "
                            "against applicable export rules rather than assuming every GPU rental is identical."
                        ),
                        (
                            "The operator screens contracting parties and records authorized "
                            "access countries before provisioning. A specialist reviews relevant "
                            "EAR provisions in 15 CFR Parts 734, 742, and "
                            "744 for the proposed service. The AUP prohibits hidden "
                            "crypto-mining and unauthorized scanning; network controls and account "
                            "suspension enforce those restrictions."
                        ),
                    ),
                    field(
                        "Caller authentication and mitigation filings",
                        "textarea",
                        (
                            "Determine which voice-provider duties apply under the "
                            "current FCC rules. Record caller-authentication implementation, "
                            "Robocall Mitigation Database status, upstream responsibilities, "
                            "and the evidence needed to support any claimed exemption or limited role."
                        ),
                        (
                            "Review 47 CFR 64.6301 and 64.6305 against the operator's "
                            "voice-provider role. Retain applicable Robocall Mitigation Database "
                            "filing evidence and supplier caller-authentication commitments. Never "
                            "promise A-level attestation solely because a call is prepaid; "
                            "the originating provider must support its attestation with "
                            "the required customer and number information."
                        ),
                    ),
                    field(
                        "Calling permissions and 10DLC registration",
                        "textarea",
                        (
                            "Record the lawful calling or messaging basis, "
                            "permission evidence, opt-out processing, campaign identity, "
                            "and carrier acceptance. Distinguish TCPA requirements from "
                            "10DLC registration and describe how revoked permission stops future traffic."
                        ),
                        (
                            "Review 47 U.S.C. 227 and 47 CFR 64.1200 for "
                            "the actual campaign. Register the brand and campaign "
                            "through the appropriate 10DLC provider before sending eligible "
                            "traffic. Retain message samples and permission evidence; process "
                            "STOP events promptly. Registration alone does not establish "
                            "permission to contact a recipient."
                        ),
                    ),
                    field(
                        "Form 499, contributions, and tax treatment",
                        "textarea",
                        (
                            "Determine Form 499-A registration and reporting duties, "
                            "contribution treatment, reseller documentation, and transaction taxes. "
                            "Record the current official instructions used and "
                            "separate any contribution exemption from other filing or reporting obligations."
                        ),
                        (
                            "The accountant reviews current FCC Form 499-A instructions "
                            "and 47 CFR 54.706 and 54.708. Wholesale treatment "
                            "requires appropriate reseller evidence; a small contribution "
                            "amount does not automatically remove every filing duty. "
                            "Collected telecom taxes remain separate liabilities rather than "
                            "being counted as arbitrage spread or wallet earnings."
                        ),
                    ),
                    field(
                        "Emergency calling and number-service scope",
                        "textarea",
                        (
                            "Determine whether the offered service includes interconnected "
                            "VoIP, emergency calling, number assignment, or portability. "
                            "Document applicable duties and customer-facing limitations without "
                            "assuming a contract label can remove obligations created by the actual service."
                        ),
                        (
                            "The initial wholesale termination order does not market "
                            "a complete user telephone service. Before adding interconnected "
                            "VoIP, review 47 CFR 9.11 and relevant numbering "
                            "and portability rules. Validate registered-location handling and "
                            "emergency routing with qualified providers using designated test "
                            "procedures, never casual live emergency calls."
                        ),
                    ),
                    field(
                        "IPv4 rights, routing, and abuse terms",
                        "textarea",
                        (
                            "Record address-use authority, registry policy constraints, "
                            "routing authorization, reputation handling, and end-of-term "
                            "withdrawal. Explain which rights the customer receives "
                            "and how abuse notices or third-party claims interrupt service."
                        ),
                        (
                            "The /24 agreement grants a time-limited use right, "
                            "not ownership of internet number resources. The holder "
                            "authorizes the origin ASN and maintains applicable RPKI "
                            "records. The operator logs abuse contacts and requires "
                            "prompt route withdrawal at termination, while registry records "
                            "and regional registry policies remain controlling evidence."
                        ),
                    ),
                    field(
                        "Evidence register and corrective actions",
                        "textarea",
                        (
                            "Assign each requirement an evidence artifact, accountable "
                            "owner, review interval, and corrective deadline. Explain "
                            "which affected service stops if evidence expires "
                            "and how customers receive accurate notice of any operational restriction."
                        ),
                        (
                            "The register links the signed resale addendum, privacy "
                            "settings export, applicable FCC filing receipt, carrier campaign "
                            "status, and tax determination. The owner reviews changes "
                            "monthly. An expired campaign authorization blocks new campaign "
                            "traffic while unrelated GPU service continues; customer notices "
                            "state the specific restriction and remediation owner."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Every offered service has a documented role determination, current "
                    "required evidence, matching supplier and customer terms, and tested "
                    "controls; unresolved requirements block only the affected service."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate repetitive acquisition and delivery work without "
                    "automating unsupported promises or uncontrolled commitments. Connect "
                    "qualified demand, routing policy, credit controls, supplier health, "
                    "and incident response into a measurable operating loop. Preserve "
                    "a practical fallback whenever a provider, model, carrier, or integration fails."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Choose automation only after documenting the manual "
                        "decision and its evidence. Specify the input, "
                        "output, retry boundary, cost ceiling, and human "
                        "exception owner. Optimize predictable work first, especially prepaid provisioning, usage reconciliation, and qualified lead follow-up."
                    ),
                    (
                        "Connect routing choices to quality and permission "
                        "constraints before considering price. Maintain explicit "
                        "provider allowlists, data-region rules, and spending "
                        "limits. A lower unit quote is useful only when the resulting service remains acceptable to the customer."
                    ),
                    (
                        "Build acquisition around a measurable customer problem "
                        "and a paid benchmark. Track each lead "
                        "through qualification, pilot, conversion, and renewal. "
                        "Use actual performance evidence and authorized references instead of presenting theoretical capacity savings as delivered customer results."
                    ),
                    (
                        "Set alarms for utilization, realized spread, "
                        "wallet exposure, abuse indicators, and supplier "
                        "concentration. Every alert needs an owner "
                        "and an immediate safe action; avoid dashboards that report problems without identifying how commitments or traffic will change."
                    ),
                    (
                        "Test fallback capacity and operational rollback "
                        "before relying on either during an incident. "
                        "Record the maximum affordable fallback duration "
                        "and the customer notification threshold. Revisit the automation after every material failure or change in supplier terms."
                    ),
                ],
                "fields": [
                    field(
                        "Automation event map and control owner",
                        "textarea",
                        (
                            "Map lead qualification, payment settlement, provisioning, "
                            "usage collection, charging, reconciliation, and renewal "
                            "to named services. Identify the events requiring "
                            "human judgment and the evidence each automated transition must carry."
                        ),
                        (
                            "A signed order and settled payment create a provisioning "
                            "event in PostgreSQL. A worker allocates approved capacity, "
                            "records the supplier identifier, and enables usage. Nightly "
                            "reconciliation creates an exception queue. The owner alone "
                            "changes reservation ceilings; workers cannot purchase an annual "
                            "commitment from an incoming customer request."
                        ),
                    ),
                    field(
                        "LiteLLM and vLLM routing policy",
                        "textarea",
                        (
                            "Define provider eligibility, model version pinning, "
                            "quality thresholds, latency targets, and maximum "
                            "request cost. Explain how routing decisions "
                            "are audited and how data restrictions remain binding during automatic fallback."
                        ),
                        (
                            "LiteLLM selects between two approved endpoints serving the "
                            "same tested model configuration, including a vLLM pool. "
                            "A 200-case evaluation must score at least 96% "
                            "on the agreed acceptance metric. Requests with a "
                            "U.S.-only restriction never route elsewhere, even when the "
                            "cheapest eligible endpoint has exhausted capacity."
                        ),
                    ),
                    field(
                        "Stripe wallet and exposure automation",
                        "textarea",
                        (
                            "Specify low-balance alerts, optional replenishment authorization, "
                            "payment failure behavior, and maximum open "
                            "usage exposure. Distinguish a queued top-up "
                            "request from settled funds that may safely support additional service reservations."
                        ),
                        (
                            "Alert at $100 available credit and stop new reservations "
                            "below each job's estimated maximum charge. An authorized "
                            "$500 replenishment request does not increase credit until "
                            "the settlement policy permits it. Failed payment leaves "
                            "existing bounded jobs running but blocks new work; "
                            "the owner reviews any chargeback-linked account immediately."
                        ),
                    ),
                    field(
                        "Least-cost SIP and messaging workflow",
                        "textarea",
                        (
                            "Define eligible carriers, destination restrictions, "
                            "quality measurements, rate-deck validation, and "
                            "campaign provisioning states. Explain how automated "
                            "least-cost routing prevents loops, unauthorized destinations, and traffic sent before required registrations become active."
                        ),
                        (
                            "The SIP router compares validated rate decks only among "
                            "carriers meeting the call-quality threshold. Premium-rate destinations "
                            "remain disabled unless specifically authorized. Messaging provisioning "
                            "moves from submitted to provider-confirmed active; it does "
                            "not send during review. Route failures have bounded "
                            "retries and cannot bounce indefinitely between two carriers."
                        ),
                    ),
                    field(
                        "Acquisition offer and proof asset",
                        "textarea",
                        (
                            "Define a narrow buyer segment, specific "
                            "performance problem, paid pilot offer, and "
                            "evidence asset. State which measured result "
                            "supports the sales claim and what permission is required before sharing customer-identifiable results."
                        ),
                        (
                            "Target document-automation teams spending over $8,000 monthly on "
                            "batch inference. Offer a $750 paid benchmark using "
                            "their approved sample set. Deliver throughput, acceptance accuracy, "
                            "latency, and cost-per-document measurements. Publish only an authorized "
                            "case study or anonymized aggregate that cannot reveal "
                            "the customer's documents, identity, or confidential workflow."
                        ),
                    ),
                    field(
                        "Funnel conversion and acquisition cost",
                        "textarea",
                        (
                            "Record prospect volume, qualified conversations, "
                            "paid pilots, converted accounts, acquisition "
                            "spend, and expected contribution. Calculate "
                            "conversion rates and payback using realized contribution rather than gross contracted customer spending."
                        ),
                        (
                            "A $2,400 campaign produces 40 qualified conversations, eight "
                            "paid pilots, and three recurring customers. Pilot conversion "
                            "is 20%; recurring conversion from pilots is 37.5%. "
                            "Acquisition cost is $800 per recurring account before "
                            "pilot offsets. At $400 monthly contribution per account, "
                            "simple acquisition payback is two months."
                        ),
                    ),
                    field(
                        "Utilization and price-compression alarms",
                        "textarea",
                        (
                            "Specify observation windows, minimum sample "
                            "sizes, alert thresholds, and actions "
                            "for falling utilization or market prices. "
                            "Separate temporary demand noise from evidence that the next supplier renewal would destroy expected contribution."
                        ),
                        (
                            "Alert when trailing seven-day sold utilization falls below "
                            "65% on the initial server. Review comparable H100 "
                            "offers weekly and rerun the renewal model after "
                            "a 15% qualified price decline. The response is "
                            "shorter commitments and revised customer minimums, not an "
                            "automatic purchase of newer H200 or B200 inventory."
                        ),
                    ),
                    field(
                        "Abuse detection and bounded response",
                        "textarea",
                        (
                            "Define observable abuse indicators, "
                            "account restrictions, evidence handling, "
                            "and restoration criteria. Use "
                            "behavioral and contractual signals appropriate to the service while avoiding unnecessary inspection or retention of customer content."
                        ),
                        (
                            "Alert on an unapproved mining process, a sudden "
                            "premium-destination calling spike, or repeated messages after "
                            "recorded opt-outs. Freeze new affected usage, preserve "
                            "minimal event metadata, and notify the responsible owner. "
                            "Restoration requires corrected configuration and documented customer "
                            "explanation; unrelated tenants continue operating within their limits."
                        ),
                    ),
                    field(
                        "Fallback supplier and maximum rescue cost",
                        "textarea",
                        (
                            "Document a tested replacement "
                            "provider, available capacity, switching "
                            "procedure, and maximum affordable "
                            "duration. Explain which workloads cannot move because of model, region, privacy, networking, or customer-contract restrictions."
                        ),
                        (
                            "The backup offers eight compatible GPUs at $3.00 "
                            "per GPU-hour. A 12-hour rescue costs $288 before "
                            "transfer expenses, compared with $230.40 revenue at $2.40. "
                            "The owner funds the $57.60 direct shortfall to "
                            "preserve service. Workloads lacking approved backup-region terms "
                            "pause instead of moving without authorization."
                        ),
                    ),
                    field(
                        "Rollback ownership and incident learning",
                        "textarea",
                        (
                            "Assign rollback authority, "
                            "customer communication timing, "
                            "restoration checks, and "
                            "post-incident follow-up. Record how a failed automation changes tests, limits, or supplier policy rather than merely producing a narrative report."
                        ),
                        (
                            "A routing release that raises error rate above "
                            "2% for five minutes rolls back to the "
                            "previous signed configuration. The on-call contractor acknowledges "
                            "within ten minutes and the owner handles material "
                            "customer notices. The incident adds a regression test "
                            "and verifies whether fallback costs remained within budget."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each automation has bounded authority, observable outcomes, an "
                    "exception owner, and a tested rollback; acquisition metrics use "
                    "realized contribution; and fallback costs fit the funded reserve."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Convert the validated model into a disciplined first-month "
                    "execution plan and a transferable operating record. Assign "
                    "small-team responsibilities, stage capital against evidence, measure "
                    "cash and quality together, and preserve clean contracts "
                    "and reconciliations that support renewal, expansion, financing, or a future sale."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan the first 30 days as an "
                        "evidence-building sprint rather than assuming an "
                        "immediate sale. The canonical first-deal window "
                        "is one to four months, so the sprint must remain useful when contracting or customer procurement takes longer."
                    ),
                    (
                        "Assign the Base pod of one "
                        "full-time operator and two contractors "
                        "to explicit deliverables and backup "
                        "coverage. Keep customer acquisition, infrastructure operations, and ledger review visible without pretending that contractor hours are unlimited or free."
                    ),
                    (
                        "Release capital in stages tied to "
                        "signed rights, collected payments, tested "
                        "delivery, and reconciled usage. Keep "
                        "the reserve intact until the associated risk has expired; a promising sales conversation does not justify an irreversible supplier commitment."
                    ),
                    (
                        "Review weekly demand, utilization, realized "
                        "spread, wallet coverage, support burden, "
                        "and customer quality outcomes together. "
                        "Use a written stop, repair, or expand decision so the scorecard produces action rather than a collection of disconnected attractive metrics."
                    ),
                    (
                        "Maintain an exit-readiness ledger from "
                        "the first contract onward. Preserve "
                        "assignability terms, customer concentration, supplier "
                        "dependencies, accounting reconciliations, and access ownership. A transferable business requires evidence that another operator can deliver the same service without relying on undocumented founder knowledge."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7: qualification and architecture",
                        "textarea",
                        (
                            "Schedule the initial "
                            "customer interviews, supplier "
                            "quotes, role assessment, "
                            "and architecture decisions. Assign owners and concrete artifacts, and specify what would cause the team to reject the proposed initial lane."
                        ),
                        (
                            "By day 7, the owner completes ten buyer interviews "
                            "and obtains two dated H100 supplier quotes. The "
                            "infrastructure contractor benchmarks one approved workload; the "
                            "operations contractor drafts the requirement register. Reject "
                            "the lane if resale is prohibited or buyers "
                            "will not support a contribution-positive price."
                        ),
                    ),
                    field(
                        "Days 8–14: contracting and ledger build",
                        "textarea",
                        (
                            "Define the second-week "
                            "contract, payment, ledger, "
                            "and isolation deliverables. "
                            "Separate required implementation work from optional polish and identify the evidence needed before accepting customer prepayments for the promised service."
                        ),
                        (
                            "By day 14, complete the supplier resale addendum, "
                            "customer order, refund policy, and wallet ledger schema. "
                            "Pass duplicate-webhook and concurrent-reservation tests in a "
                            "test environment. The owner verifies delivery readiness "
                            "before collecting a live pilot payment; no paid "
                            "campaign depends on an untested automatic provisioning path."
                        ),
                    ),
                    field(
                        "Days 15–21: bounded paid pilot",
                        "textarea",
                        (
                            "Specify the pilot "
                            "customer count, duration, "
                            "spending ceiling, quality "
                            "metrics, and daily review cadence. Include a useful alternative deliverable if customer procurement prevents a paid engagement during the third week."
                        ),
                        (
                            "Run one seven-day paid benchmark with a $750 "
                            "customer budget and $300 upstream cost ceiling. "
                            "Review quality, usage, and wallet coverage daily. "
                            "If procurement remains open, finish synthetic failure "
                            "tests and the customer benchmark proposal instead; "
                            "do not report synthetic activity as a closed deal."
                        ),
                    ),
                    field(
                        "Days 22–30: reconciliation and renewal choice",
                        "textarea",
                        (
                            "Define the final-week "
                            "closeout artifacts, customer "
                            "review, renewal decision, "
                            "and unresolved-risk register. Require an explicit explanation when the team continues testing rather than expanding or claiming that the launch has reached recurring profitability."
                        ),
                        (
                            "By day 30, issue the reconciled pilot statement, "
                            "review benchmark results with the buyer, and record "
                            "renewal intent separately from signed minimums. Purchase "
                            "another reservation only after the cash and "
                            "utilization tests pass. If contracting continues, schedule "
                            "the next review within the one-to-four-month first-deal window."
                        ),
                    ),
                    field(
                        "Pod responsibilities and paid capacity",
                        "textarea",
                        (
                            "Allocate owner and "
                            "contractor responsibilities, weekly "
                            "hours, escalation coverage, "
                            "and handoff artifacts. State when staffing must change and how additional labor costs enter the lane economics rather than disappearing into an automation claim."
                        ),
                        (
                            "The full-time owner handles sales, supplier commitments, "
                            "and cash decisions. Contractor A supplies 15 "
                            "weekly infrastructure hours; contractor B supplies ten "
                            "operations and reconciliation hours. At Scaled, plan "
                            "two full-time staff plus three contractors. Add "
                            "coverage only after pricing and remaining-expense budgets support it."
                        ),
                    ),
                    field(
                        "Canonical scorecard and KPI definitions",
                        "textarea",
                        (
                            "Record the candidate "
                            "score and scenario "
                            "anchors alongside operational "
                            "KPIs with explicit denominators. Distinguish the editorial ranking from observed business performance and prevent annual targets from being presented as completed revenue."
                        ),
                        (
                            "Candidate #36 ranks #03 with 94/100: revenue 24, "
                            "margin 24, team efficiency 20, startup accessibility "
                            "13, automation 13. Track sold utilization, realized "
                            "retained contribution, and cash coverage weekly. Annual "
                            "owner-profit anchors remain $27,000, $189,000, and $456,000; "
                            "the ranking is not evidence of achieved operating results."
                        ),
                    ),
                    field(
                        "Weekly stop, repair, or expand decision",
                        "textarea",
                        (
                            "Set weekly decision "
                            "thresholds for cash, "
                            "demand, quality, abuse, "
                            "and reconciliation. Specify who decides and what evidence justifies increasing capacity, preserving the current pilot, or allowing a supplier reservation to expire."
                        ),
                        (
                            "Expand only with four reconciled weeks, funded "
                            "next-month commitments, at least 75% sold utilization, "
                            "and quality above the contracted threshold. Repair "
                            "when reconciliation exceptions persist beyond one day. "
                            "Stop renewal if modeled contribution turns negative "
                            "or customer permissions fail. The owner records the decision "
                            "and supporting measurements every Friday."
                        ),
                    ),
                    field(
                        "Concentration and transferable contract register",
                        "textarea",
                        (
                            "List major customers "
                            "and suppliers with "
                            "revenue shares, renewal "
                            "dates, assignability terms, and change-of-control requirements. Explain how concentrated relationships or nontransferable permissions affect expansion plans and the evidence a prospective buyer would need."
                        ),
                        (
                            "At $56,250 monthly Base gross billings, a "
                            "$22,500 customer represents 40% concentration. Flag "
                            "its 30-day cancellation right and assignment "
                            "restriction. Record the supplier's consent requirement "
                            "for contract transfer. Reduce dependence through "
                            "additional qualified customers rather than presenting unsigned pipeline "
                            "as diversification already achieved."
                        ),
                    ),
                    field(
                        "Diligence evidence and access ownership",
                        "textarea",
                        (
                            "Identify the records "
                            "needed to verify "
                            "earnings, service rights, "
                            "security, and operating continuity. Assign custodians and access restrictions, and distinguish transferable company assets from personal accounts or customer data that cannot be disclosed freely."
                        ),
                        (
                            "Maintain monthly reconciliations, supplier invoices, signed orders, "
                            "filing evidence, code ownership records, and incident "
                            "summaries in company-controlled storage. Company accounts "
                            "own Stripe, repositories, domains, and infrastructure. "
                            "A prospective buyer first receives aggregated metrics "
                            "and redacted agreements; sensitive customer records require "
                            "a documented access basis and controlled disclosure."
                        ),
                    ),
                    field(
                        "Exit-readiness valuation bridge and next sprint",
                        "textarea",
                        (
                            "Bridge reported owner "
                            "profit to buyer-reviewed "
                            "earnings, identifying replacement "
                            "labor, unusual costs, liabilities, and transfer friction. End with the next concrete operating improvements rather than assigning an unsupported sale multiple or claiming a transaction outcome."
                        ),
                        (
                            "Start the Base bridge at $189,000 annual "
                            "owner net profit. If buyer replacement "
                            "labor adds $90,000 not already included, "
                            "illustrative earnings fall to $99,000 before "
                            "other adjustments. Keep wallet liabilities separate. "
                            "Next sprint: reduce customer concentration, test operator "
                            "handoff, and resolve contract-transfer restrictions before discussing valuation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The 30-day sprint has dated deliverables and honest status, "
                    "the pod owns every recurring control, canonical targets remain "
                    "distinct from actual results, and the evidence ledger supports "
                    "both the next operating decision and an independent earnings review."
                ),
            },
        ],
    }
