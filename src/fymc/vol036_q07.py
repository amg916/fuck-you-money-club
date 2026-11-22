from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute gpu compute & telecom capacity arbitrage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Prepaid H100/H200/B200 Capacity, LiteLLM Routing, SIP Settlement, SQLite Reservations, and FCC Operating Controls",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #36, GPU Compute & Telecom Capacity Arbitrage, holds Rank #03 of 36 "
        "with a 94/100 Money-to-Manpower Score. This chapter turns 15 mapped plays into "
        "an executable intake-to-cash operating system: qualified demand, verified prepaid "
        "funds, atomic capacity reservations, idempotent dispatch, measured delivery, and "
        "reconciled settlement. Annual owner profit is $27,000 Conservative, $189,000 Base, "
        "and $456,000 Scaled. The Base case separates $675,000 gross billings from "
        "$438,750 retained contribution and $249,750 subsequent operating costs. A six-module "
        "SQLite reference makes duplicate requests and interrupted workers recoverable, "
        "while the worked cohort tracks prepaid liabilities and cash without treating "
        "wallet deposits as earned revenue. Hardware utilization, telecom authorization, "
        "tenant isolation, and evidence quality determine whether the spread survives."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$150,000",
            "context": "Annual gross billings; $97,500 retained at 65%.",
            "note": "18% gross-basis net margin; $27,000 owner profit; 1 FT + 2 C; 27.69% retained-basis net margin.",
        },
        {
            "label": "Base",
            "value": "$675,000",
            "context": "Annual gross billings; $438,750 retained at 65%.",
            "note": "28.0% gross-basis net margin; $189,000 owner profit; 1 FT + 2 C; 43.08% retained-basis net margin.",
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross billings; $780,000 retained at 65%.",
            "note": "38% gross-basis net margin; $456,000 owner profit; 2 FT + 3 C; 58.46% retained-basis net margin.",
        },
    ],
    "sections": [
        {
            "heading": "1. Qualify demand, prove the upstream right, and price the actual unit",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start intake with a commercial workload, not a discounted GPU advertisement. "
                    "Record the buyer entity, authorized contact, intended application, service region, "
                    "data classification, delivery window, concurrency ceiling, and replenishment owner. "
                    "For inference, require model version, input and output token distributions, "
                    "latency percentile, context length, and retention requirements. For bare metal, "
                    "capture accelerator generation, memory, interconnect, isolation boundary, image "
                    "digest, and checkpoint behavior. For telecom, collect originating numbers, "
                    "destination mix, expected calls per second, messaging use case, and evidence "
                    "supporting the traffic's authorization. A quote becomes executable only after "
                    "the upstream contract permits resale and the proposed tenant configuration. "
                    "Keep customer deposits, gross service billings, retained contribution, and owner "
                    "profit in separate fields. The Base monthly service target is $56,250: "
                    "$19,687.50 upstream allocation leaves $36,562.50 retained contribution, then "
                    "$20,812.50 subsequent costs leave $15,750 owner profit. Never size a credit "
                    "wallet from the customer's business sales, loan balances, or traffic forecasts "
                    "that have not become paid orders. Price a bounded service unit and reserve "
                    "only the cost exposure that its prepaid balance can support. Put quote expiry, "
                    "interruption treatment, and replenishment thresholds into the order before "
                    "the first capacity commitment is signed."
                ),
                (
                    "Use saas_technographic_churn_pixel_scraping as an account-timing signal rather "
                    "than a claim of privileged knowledge. Crawl permitted public commercial pages "
                    "and query public DNS TXT and CNAME records weekly for changes associated with "
                    "Salesforce, HubSpot, Marketo, Segment, or NetSuite. Store timestamped observations, "
                    "response hashes, and the previously observed state; a weekly comparison brackets "
                    "a change within seven days and cannot establish its exact day. A tag removal "
                    "can reflect a deployment error, regional variation, or server-side migration "
                    "instead of cancellation. Confirm the hypothesis using passive DNS history, "
                    "public job-posting technographic mentions, and a direct procurement conversation. "
                    "Treat Month 10–11 outreach as a proposed annual renewal window only after "
                    "someone validates the underlying contract cycle. For example, 120 monitored "
                    "accounts producing 12 change signals, six corroborated migrations, and two "
                    "paid $6,250 monthly orders generate $12,500 gross billings, not 120 customers. "
                    "At the canonical blended retention assumption, those two orders contribute "
                    "$8,125 before subsequent costs. If corroboration fails, keep the account in "
                    "research and buy no reserved capacity. Migration evidence should identify a "
                    "specific inference, batch-processing, or telephony requirement before a "
                    "salesperson proposes an infrastructure replacement."
                ),
                (
                    "The fifteen-play map below is a demand-routing menu, not fifteen additive "
                    "revenue forecasts. Assign each order one primary service SKU and record any "
                    "secondary routing tactic without booking the same dollar twice. A worked "
                    "$6,250 monthly bundle can contain 1,500 GPU-hours at $2.50, 500 million-token "
                    "units at $3, and 100,000 authorized SIP minutes at $0.01. These illustrative "
                    "tariffs require workload benchmarking and carrier destination checks; they "
                    "are not vendor quotations. Nine bundles produce the Base monthly billings "
                    "and 13,500 GPU-hours. Against 24 accelerators with 720 available hours each, "
                    "that compute component consumes 78.125% of theoretical hours before maintenance "
                    "and fragmentation. Check concurrent peaks separately because aggregate hours "
                    "cannot prove schedulability. Benchmark H100, H200, and B200 on the actual model, "
                    "including memory fit, output speed, and failed-request cost. Attach a cheaper "
                    "generation, delayed batch window, or customer-approved alternative model as "
                    "the fallback; never silently degrade an enterprise promise. On telecom "
                    "routes, compare billable increments and destination surcharges rather than "
                    "headline per-minute rates. A thin spread disappears when a carrier rounds "
                    "every short call upward or rejects traffic that the reseller already accepted."
                ),
            ],
            "table": {
                "caption": "Fifteen-Play Intake Map: Observable Units, Paid Demand, and Explicit Failure Fallbacks",
                "headers": [
                    "Mapped operating play or paired plays",
                    "Illustrative unit calculation and routing decision",
                    "Evidence required before accepting paid demand",
                    "Failure mode and bounded operating fallback",
                ],
                "rows": [
                    [
                        "saas_technographic_churn_pixel_scraping links public software changes to migration discovery.",
                        "Two corroborated orders times $6,250 produce $12,500 monthly gross billings.",
                        "Keep dated DNS observations, page hashes, job references, and buyer-confirmed timing.",
                        "Weekly scans cannot establish exact change dates; corroborate before reserving capacity.",
                    ],
                    [
                        "Reserved H100 resale and H200 batch placement match two distinct workload profiles.",
                        "One thousand hours at $2.50 produce $2,500 before actual upstream charges.",
                        "Require resale permission, benchmark results, memory requirements, and signed interruption terms.",
                        "Falling utilization triggers shorter commitments or customer-approved migration to cheaper hardware.",
                    ],
                    [
                        "B200 premium bursts and supported MIG partition resale separate urgency from isolation.",
                        "Four partitions sold for ten hours each create forty billable partition-hours.",
                        "Verify hardware-supported profiles, per-partition metering, and the contracted tenant isolation boundary.",
                        "Memory fragmentation requires whole-device scheduling; partition counts never imply linear performance.",
                    ],
                    [
                        "Multi-provider inference routing and tenant-scoped prompt caching reduce measured execution costs.",
                        "Ten million input tokens at $3 per million produce $30 billings.",
                        "Record model identity, provider permissions, cache policy, and output-quality acceptance tests.",
                        "Disable persistence for zero-retention customers and route only to contractually approved providers.",
                    ],
                    [
                        "Deferred batch inference and committed token-block resale convert flexible demand into utilization.",
                        "Five hundred million-token units at $3 generate $1,500 monthly gross billings.",
                        "Obtain completion deadlines, token definitions, retry rules, and upstream commitment expiration.",
                        "Missed batch windows use approved overflow capacity or release the unearned wallet reservation.",
                    ],
                    [
                        "SIP least-cost routing and authorized DID inventory resale serve verified communications demand.",
                        "One hundred thousand minutes at $0.01 generate $1,000 before termination costs.",
                        "Validate number rights, destination rates, billing increments, identity authentication, and traffic purpose.",
                        "Fraud spikes suspend the tenant; alternate routes must preserve required identity handling.",
                    ],
                    [
                        "Registered 10DLC campaign provisioning and approved messaging-route selection support two messaging services.",
                        "Ten thousand messages at $0.012 generate $120 before carrier fees and surcharges.",
                        "Require documented messaging authority, brand records, campaign registration, and opt-out handling.",
                        "Rejected campaigns remain unsent; never substitute unregistered numbers to bypass carrier restrictions.",
                    ],
                    [
                        "Authorized IPv4 subleasing and standby capacity resale monetize two separately contracted assets.",
                        "Thirty-two addresses at $2 monthly generate $64; standby fees require separate contracts.",
                        "Verify address authority, upstream sublease permission, routing authorization, and reserved standby availability.",
                        "Abuse complaints isolate affected assignments; unavailable standby capacity receives no availability billing.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the spread before trying to enlarge it",
                "body": "Veteran operators optimize evidence, billable units, and recoverability before increasing committed inventory.",
                "items": [
                    "Benchmark cost per accepted output token, not tokens generated before retries, safety rejection, or customer cancellation.",
                    "Keep DCGM utilization samples separate from customer billing events; power draw and GPU occupancy do not establish accepted delivery.",
                    "Replay destination-weighted SIP call records against proposed tariffs, including connection fees, rounding increments, and expensive prefixes.",
                    "Use DNS changes to request a migration discovery meeting; corroborated job postings and buyer timing prevent expensive false renewal assumptions.",
                ],
            },
        },
        {
            "heading": "2. Implement an atomic prepaid ledger and an idempotent dispatch boundary",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The six reference modules form one executable SQLite service core when "
                    "concatenated in table order. They use integer cents, immutable request "
                    "fingerprints, unique payment identifiers, and BEGIN IMMEDIATE transactions. "
                    "Every balance-changing operation and state transition obtains the database "
                    "write lock before reading its decision inputs, eliminating competing "
                    "read-then-write reservations inside this design. Use a local persistent disk, "
                    "one authoritative database, foreign keys, WAL mode, and bounded lock waits. "
                    "A busy database returns an error for a later retry; it must never cause "
                    "an alternate untracked dispatch. Separate connections are required for "
                    "concurrent workers. For Postgres, replace the database-wide write lock "
                    "with ordered row locks covering the wallet, request, and reservation; retain "
                    "the same uniqueness constraints. Do not place SQLite on an unreliable shared "
                    "filesystem or split writes between independently replicated files. The "
                    "reference deliberately treats reservations as internal prepaid balance "
                    "holds, not third-party escrow. It also keeps customer identities and raw "
                    "workload content outside the ledger. Production authentication, payment "
                    "verification, secrets management, backup restoration, and provider-specific "
                    "adapters remain explicit integration responsibilities rather than fictional "
                    "features hidden behind a successful database insert."
                ),
                (
                    "Intake computes prices from a server-controlled tariff and rejects reuse "
                    "of an external order key with different content. A settled-payment handler "
                    "credits the wallet only after checking the processor signature, payment "
                    "object, currency, merchant account, and usable funds status. Stripe event "
                    "deduplication alone is insufficient because multiple events can describe "
                    "one payment; the schema also makes the payment identifier unique. Screening "
                    "checks authorization, resale scope, capacity, and service-specific evidence "
                    "before reserving funds. A numeric score prioritizes review but never "
                    "substitutes for those checks. The reservation transaction subtracts existing "
                    "active holds from wallet balance before approving another request. It "
                    "creates the dispatch job in that same transaction, so a crash cannot leave "
                    "a payable request without recoverable work. Cancellation can release a "
                    "reservation only while its job is still pending. Dispatch first changes "
                    "that status under the same lock, preventing a simultaneous cancellation "
                    "from releasing money behind a running workload. The pending job is the "
                    "transactional outbox; a worker can discover it after a process restart "
                    "without relying on a message published between two unrelated commits."
                ),
                (
                    "External execution needs a stronger condition than a local unique key. "
                    "The provider adapter must persistently honor the supplied idempotency key "
                    "for the complete retry lifetime and return the same authenticated result "
                    "for the same immutable request. If an upstream lacks that facility, an "
                    "operator-controlled provisioning service must supply it with durable "
                    "resource lookup; otherwise ambiguous dispatches stop for investigation. "
                    "A timeout means uncertain execution, not permission to buy another GPU "
                    "instance or originate another call. Repeating concurrent dispatch attempts "
                    "is safe only under that external contract. Settlement validates delivered "
                    "units against the reservation and writes billing, upstream accrual, wallet "
                    "debit, and terminal state atomically. Distinct cost-payment events then "
                    "separate accrued profit from cash actually transferred upstream. The "
                    "reconciliation view exposes gross billings, retained contribution, operating "
                    "profit, collected cash, and open wallet liabilities without asserting that "
                    "one accounting presentation fits every contract. ASC 606 principal-versus-agent "
                    "analysis determines external revenue presentation; this scorecard uses "
                    "65% retained contribution as its comparison basis. Run the QA module "
                    "after migrations and daily close, then test interruption, duplicated "
                    "callbacks, and parallel reservations against a disposable database before "
                    "connecting any live payment or provisioning adapter."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Reference module and execution responsibility",
                    "Copy-pasteable Python and embedded SQLite artifact",
                    "Atomicity and idempotency operating contract",
                    "Required production verification and recovery evidence",
                ],
                "rows": [
                    [
                        "Module 1 creates the authoritative schema and serialized transaction helper.",
                        """import hashlib
import json
import sqlite3
from contextlib import contextmanager

SCHEMA = '''
CREATE TABLE IF NOT EXISTS wallets (
    tenant TEXT PRIMARY KEY,
    balance INTEGER NOT NULL DEFAULT 0 CHECK (balance >= 0)
);
CREATE TABLE IF NOT EXISTS requests (
    id TEXT PRIMARY KEY,
    tenant TEXT NOT NULL REFERENCES wallets(tenant),
    external_key TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    sku TEXT NOT NULL,
    units INTEGER NOT NULL CHECK (units > 0),
    unit_price INTEGER NOT NULL CHECK (unit_price > 0),
    score INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    state TEXT NOT NULL CHECK (
        state IN ('SCREENED','RESERVED','RUNNING','REVIEW',
                  'SETTLED','CANCELLED')
    ),
    UNIQUE (tenant, external_key)
);
CREATE TABLE IF NOT EXISTS payments (
    payment_id TEXT PRIMARY KEY,
    event_id TEXT NOT NULL UNIQUE,
    tenant TEXT NOT NULL REFERENCES wallets(tenant),
    cents INTEGER NOT NULL CHECK (cents > 0)
);
CREATE TABLE IF NOT EXISTS holds (
    request_id TEXT PRIMARY KEY REFERENCES requests(id),
    cents INTEGER NOT NULL CHECK (cents > 0),
    status TEXT NOT NULL CHECK (
        status IN ('HELD','CAPTURED','RELEASED')
    )
);
CREATE TABLE IF NOT EXISTS jobs (
    request_id TEXT PRIMARY KEY REFERENCES requests(id),
    provider_key TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL CHECK (
        status IN ('PENDING','DISPATCHED','REVIEW','SETTLED','VOID')
    ),
    receipt_id TEXT UNIQUE,
    delivered_units INTEGER,
    upstream_cents INTEGER
);
CREATE TABLE IF NOT EXISTS ledger (
    event_key TEXT PRIMARY KEY,
    tenant TEXT NOT NULL,
    request_id TEXT REFERENCES requests(id),
    kind TEXT NOT NULL CHECK (
        kind IN ('TOPUP','BILLING','UPSTREAM_ACCRUAL',
                 'UPSTREAM_PAID','OPEX_ACCRUAL','OPEX_PAID')
    ),
    cents INTEGER NOT NULL CHECK (cents >= 0)
);
CREATE INDEX IF NOT EXISTS requests_tenant
    ON requests(tenant);
CREATE INDEX IF NOT EXISTS jobs_status
    ON jobs(status);
CREATE INDEX IF NOT EXISTS ledger_kind
    ON ledger(kind);
'''

def connect(path):
    db = sqlite3.connect(path, timeout=30, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("PRAGMA busy_timeout=30000")
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA synchronous=FULL")
    db.executescript(SCHEMA)
    return db

@contextmanager
def atomic(db):
    db.execute("BEGIN IMMEDIATE")
    try:
        yield
        db.execute("COMMIT")
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise

def digest(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def put_event(db, key, tenant, request_id, kind, cents):
    old = db.execute(
        "SELECT tenant, request_id, kind, cents FROM ledger "
        "WHERE event_key=?", (key,)
    ).fetchone()
    expected = (tenant, request_id, kind, cents)
    if old is not None:
        if tuple(old) != expected:
            raise ValueError("Conflicting immutable ledger event")
        return
    db.execute(
        "INSERT INTO ledger VALUES (?, ?, ?, ?, ?)",
        (key, tenant, request_id, kind, cents)
    )
""",
                        "All mutations use one authoritative database; uniqueness protects immutable identifiers across retries.",
                        "Restore backups on local persistent storage and confirm foreign keys before accepting traffic.",
                    ],
                    [
                        "Module 2 scores verified intake and credits independently verified settled payments.",
                        """TARIFF_CENTS = {
    "gpu_hour": 250,
    "million_tokens": 300,
    "sip_hundred_minutes": 100,
}

def positive_integer(value):
    if type(value) is not int or value <= 0:
        raise ValueError("Expected a positive integer")
    return value

def credit_settled(db, payment_id, event_id, tenant, cents):
    # Call only from the authenticated payment-verification adapter.
    positive_integer(cents)
    with atomic(db):
        db.execute(
            "INSERT OR IGNORE INTO wallets(tenant) VALUES (?)",
            (tenant,)
        )
        rows = db.execute(
            "SELECT * FROM payments WHERE payment_id=? OR event_id=?",
            (payment_id, event_id)
        ).fetchall()
        if rows:
            if len(rows) != 1:
                raise ValueError("Conflicting payment identifiers")
            old = rows[0]
            if (old["payment_id"], old["tenant"], old["cents"]) != (
                payment_id, tenant, cents
            ):
                raise ValueError("Conflicting payment content")
            return
        db.execute(
            "INSERT INTO payments VALUES (?, ?, ?, ?)",
            (payment_id, event_id, tenant, cents)
        )
        db.execute(
            "UPDATE wallets SET balance=balance+? WHERE tenant=?",
            (cents, tenant)
        )
        put_event(
            db, "payment:" + payment_id, tenant, None, "TOPUP", cents
        )

def intake(db, tenant, external_key, sku, units, evidence):
    positive_integer(units)
    price = TARIFF_CENTS[sku]
    required = ("authorized", "resale_allowed", "capacity_checked")
    if any(evidence.get(name) is not True for name in required):
        raise ValueError("Required screening evidence is incomplete")
    score = 60
    score += 20 if evidence.get("benchmark_passed") is True else 0
    score += 20 if evidence.get("timing_confirmed") is True else 0
    content = {
        "tenant": tenant, "external_key": external_key,
        "sku": sku, "units": units, "unit_price": price,
        "evidence": evidence,
    }
    fingerprint = digest(content)
    request_id = digest([tenant, external_key])
    with atomic(db):
        db.execute(
            "INSERT OR IGNORE INTO wallets(tenant) VALUES (?)",
            (tenant,)
        )
        old = db.execute(
            "SELECT fingerprint FROM requests WHERE id=?",
            (request_id,)
        ).fetchone()
        if old is not None:
            if old["fingerprint"] != fingerprint:
                raise ValueError("Order key reused with different content")
            return request_id
        db.execute(
            "INSERT INTO requests VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (request_id, tenant, external_key, fingerprint,
             sku, units, price, score, "SCREENED")
        )
    return request_id
""",
                        "Server tariffs determine price; payment objects and order fingerprints reject conflicting duplicate submissions.",
                        "Evidence flags come from trusted reviewers; payment identifiers include processor and merchant namespaces.",
                    ],
                    [
                        "Module 3 implements prepaid reservation and cancellation before external dispatch begins.",
                        """def reserve(db, request_id):
    with atomic(db):
        req = db.execute(
            "SELECT * FROM requests WHERE id=?", (request_id,)
        ).fetchone()
        if req is None:
            raise ValueError("Request does not exist")
        if req["state"] in ("RESERVED", "RUNNING", "REVIEW", "SETTLED"):
            return
        if req["state"] != "SCREENED":
            raise ValueError("Request cannot be reserved")
        held = db.execute(
            "SELECT COALESCE(SUM(h.cents),0) FROM holds h "
            "JOIN requests r ON r.id=h.request_id "
            "WHERE r.tenant=? AND h.status='HELD'",
            (req["tenant"],)
        ).fetchone()[0]
        balance = db.execute(
            "SELECT balance FROM wallets WHERE tenant=?",
            (req["tenant"],)
        ).fetchone()[0]
        charge = req["units"] * req["unit_price"]
        if balance - held < charge:
            raise ValueError("Insufficient unreserved prepaid balance")
        db.execute(
            "INSERT INTO holds VALUES (?, ?, 'HELD')",
            (request_id, charge)
        )
        db.execute(
            "INSERT INTO jobs(request_id,provider_key,status) "
            "VALUES (?, ?, 'PENDING')",
            (request_id, "service:" + request_id)
        )
        db.execute(
            "UPDATE requests SET state='RESERVED' WHERE id=?",
            (request_id,)
        )

def cancel_pending(db, request_id):
    with atomic(db):
        job = db.execute(
            "SELECT status FROM jobs WHERE request_id=?",
            (request_id,)
        ).fetchone()
        if job is None:
            raise ValueError("Reservation does not exist")
        if job["status"] == "VOID":
            return
        if job["status"] != "PENDING":
            raise ValueError("Resolve external execution before release")
        db.execute(
            "UPDATE jobs SET status='VOID' WHERE request_id=?",
            (request_id,)
        )
        db.execute(
            "UPDATE holds SET status='RELEASED' WHERE request_id=?",
            (request_id,)
        )
        db.execute(
            "UPDATE requests SET state='CANCELLED' WHERE id=?",
            (request_id,)
        )
""",
                        "Wallet availability, reservation creation, and outbox insertion share a single serialized transaction.",
                        "Cancellation releases internal reserved credit only; customer cash refunds need a separate verified workflow.",
                    ],
                    [
                        "Module 4 dispatches through durable provider idempotency and atomically captures verified delivery.",
                        """def settle(db, request_id, receipt):
    delivered = receipt["delivered_units"]
    upstream = receipt["upstream_cents"]
    receipt_id = receipt["receipt_id"]
    if type(delivered) is not int or delivered < 0:
        raise ValueError("Invalid delivered units")
    if type(upstream) is not int or upstream < 0:
        raise ValueError("Invalid upstream cents")
    if not isinstance(receipt_id, str) or not receipt_id:
        raise ValueError("A namespaced receipt identifier is required")
    with atomic(db):
        req = db.execute(
            "SELECT * FROM requests WHERE id=?", (request_id,)
        ).fetchone()
        job = db.execute(
            "SELECT * FROM jobs WHERE request_id=?", (request_id,)
        ).fetchone()
        if req is None or job is None:
            raise ValueError("Dispatch record does not exist")
        if receipt["provider_key"] != job["provider_key"]:
            raise ValueError("Receipt belongs to another dispatch")
        facts = (receipt_id, delivered, upstream)
        if job["status"] == "SETTLED":
            stored = (
                job["receipt_id"], job["delivered_units"],
                job["upstream_cents"]
            )
            if stored != facts:
                raise ValueError("Conflicting settlement receipt")
            return
        if job["status"] not in ("DISPATCHED", "REVIEW"):
            raise ValueError("Dispatch has not started")
        if delivered > req["units"]:
            raise ValueError("Delivery exceeds authorized quantity")
        hold = db.execute(
            "SELECT * FROM holds WHERE request_id=?", (request_id,)
        ).fetchone()
        charge = delivered * req["unit_price"]
        if hold["status"] != "HELD" or charge > hold["cents"]:
            raise ValueError("Reservation does not cover delivery")
        db.execute(
            "UPDATE wallets SET balance=balance-? WHERE tenant=?",
            (charge, req["tenant"])
        )
        db.execute(
            "UPDATE holds SET status='CAPTURED' WHERE request_id=?",
            (request_id,)
        )
        put_event(
            db, "billing:" + request_id, req["tenant"],
            request_id, "BILLING", charge
        )
        put_event(
            db, "upstream:" + request_id, req["tenant"],
            request_id, "UPSTREAM_ACCRUAL", upstream
        )
        db.execute(
            "UPDATE jobs SET status='SETTLED',receipt_id=?,"
            "delivered_units=?,upstream_cents=? WHERE request_id=?",
            (receipt_id, delivered, upstream, request_id)
        )
        db.execute(
            "UPDATE requests SET state='SETTLED' WHERE id=?",
            (request_id,)
        )

def dispatch(db, request_id, provider):
    # Adapter must verify receipts and durably deduplicate execution.
    with atomic(db):
        job = db.execute(
            "SELECT * FROM jobs WHERE request_id=?", (request_id,)
        ).fetchone()
        if job is None:
            raise ValueError("Dispatch job does not exist")
        if job["status"] == "SETTLED":
            return
        if job["status"] == "VOID":
            raise ValueError("Cancelled dispatch cannot execute")
        req = db.execute(
            "SELECT * FROM requests WHERE id=?", (request_id,)
        ).fetchone()
        payload = {
            "request_id": request_id,
            "tenant": req["tenant"],
            "sku": req["sku"],
            "units": req["units"],
        }
        key = job["provider_key"]
        db.execute(
            "UPDATE jobs SET status='DISPATCHED' WHERE request_id=?",
            (request_id,)
        )
        db.execute(
            "UPDATE requests SET state='RUNNING' WHERE id=?",
            (request_id,)
        )
    try:
        receipt = provider.execute_or_lookup(key, payload)
        settle(db, request_id, receipt)
    except Exception:
        with atomic(db):
            db.execute(
                "UPDATE jobs SET status='REVIEW' "
                "WHERE request_id=? AND status='DISPATCHED'",
                (request_id,)
            )
            db.execute(
                "UPDATE requests SET state='REVIEW' "
                "WHERE id=? AND state='RUNNING'",
                (request_id,)
            )
        raise
""",
                        "Concurrent retries reuse one immutable provider key; local settlement and cancellation cannot double-spend holds.",
                        "Adapters lacking durable execution lookup must stop ambiguous jobs rather than promise duplicate-free provisioning.",
                    ],
                    [
                        "Module 5 separates accrued unit economics from actual upstream and operating cash payments.",
                        """RECON_SQL = '''
CREATE VIEW IF NOT EXISTS reconciliation AS
WITH sums AS (
    SELECT
      COALESCE(SUM(CASE WHEN kind='TOPUP'
        THEN cents ELSE 0 END),0) AS receipts,
      COALESCE(SUM(CASE WHEN kind='BILLING'
        THEN cents ELSE 0 END),0) AS billings,
      COALESCE(SUM(CASE WHEN kind='UPSTREAM_ACCRUAL'
        THEN cents ELSE 0 END),0) AS upstream_accrual,
      COALESCE(SUM(CASE WHEN kind='UPSTREAM_PAID'
        THEN cents ELSE 0 END),0) AS upstream_paid,
      COALESCE(SUM(CASE WHEN kind='OPEX_ACCRUAL'
        THEN cents ELSE 0 END),0) AS opex_accrual,
      COALESCE(SUM(CASE WHEN kind='OPEX_PAID'
        THEN cents ELSE 0 END),0) AS opex_paid
    FROM ledger
)
SELECT *,
       billings-upstream_accrual AS retained_contribution,
       billings-upstream_accrual-opex_accrual AS owner_profit,
       receipts-upstream_paid-opex_paid AS operating_cash_delta,
       receipts-billings AS wallet_liability,
       upstream_accrual-upstream_paid AS upstream_payable,
       opex_accrual-opex_paid AS operating_payable
FROM sums;
'''

def install_reporting(db):
    db.executescript(RECON_SQL)

def record_cost(db, source_key, kind, cents, request_id=None):
    allowed = {
        "UPSTREAM_ACCRUAL", "UPSTREAM_PAID",
        "OPEX_ACCRUAL", "OPEX_PAID"
    }
    if kind not in allowed:
        raise ValueError("Unsupported cost event")
    if type(cents) is not int or cents < 0:
        raise ValueError("Expected nonnegative integer cents")
    if request_id is not None and kind == "UPSTREAM_ACCRUAL":
        raise ValueError("Request upstream accrual belongs to settlement")
    with atomic(db):
        put_event(
            db, "cost:" + kind + ":" + source_key,
            "operator", request_id, kind, cents
        )
""",
                        "Source invoice lines and bank settlement identifiers remain immutable across cost-event retries.",
                        "Allocate commitment minimums once; never accrue the same invoice through both request receipts and adjustments.",
                    ],
                    [
                        "Module 6 checks balance invariants and exercises a duplicate-safe disposable smoke scenario.",
                        """def qa(db):
    with atomic(db):
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise AssertionError("Database integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise AssertionError("Foreign key check failed")
        wallets = db.execute("SELECT * FROM wallets").fetchall()
        for wallet in wallets:
            tenant = wallet["tenant"]
            expected = db.execute(
                "SELECT COALESCE(SUM(CASE "
                "WHEN kind='TOPUP' THEN cents "
                "WHEN kind='BILLING' THEN -cents ELSE 0 END),0) "
                "FROM ledger WHERE tenant=?", (tenant,)
            ).fetchone()[0]
            held = db.execute(
                "SELECT COALESCE(SUM(h.cents),0) FROM holds h "
                "JOIN requests r ON r.id=h.request_id "
                "WHERE r.tenant=? AND h.status='HELD'", (tenant,)
            ).fetchone()[0]
            if wallet["balance"] != expected or held > expected:
                raise AssertionError("Wallet reconciliation failed")
        jobs = db.execute(
            "SELECT j.*,r.state,h.status AS hold_status,"
            "r.unit_price FROM jobs j "
            "JOIN requests r ON r.id=j.request_id "
            "JOIN holds h ON h.request_id=j.request_id"
        ).fetchall()
        expected_states = {
            "PENDING": ("RESERVED", "HELD"),
            "DISPATCHED": ("RUNNING", "HELD"),
            "REVIEW": ("REVIEW", "HELD"),
            "SETTLED": ("SETTLED", "CAPTURED"),
            "VOID": ("CANCELLED", "RELEASED"),
        }
        for job in jobs:
            actual = (job["state"], job["hold_status"])
            if actual != expected_states[job["status"]]:
                raise AssertionError("Workflow state mismatch")
            if job["status"] == "SETTLED":
                billed = db.execute(
                    "SELECT cents FROM ledger WHERE event_key=?",
                    ("billing:" + job["request_id"],)
                ).fetchone()
                wanted = job["delivered_units"] * job["unit_price"]
                if billed is None or billed["cents"] != wanted:
                    raise AssertionError("Settlement billing mismatch")
        extra = db.execute(
            "SELECT COUNT(*) FROM requests r "
            "LEFT JOIN jobs j ON j.request_id=r.id "
            "WHERE r.state<>'SCREENED' AND j.request_id IS NULL"
        ).fetchone()[0]
        if extra:
            raise AssertionError("Workflow job is missing")
    return True

def smoke():
    db = connect(":memory:")
    install_reporting(db)
    try:
        credit_settled(db, "test:payment:1", "test:event:1", "tenant-a", 10000)
        credit_settled(db, "test:payment:1", "test:event:2", "tenant-a", 10000)
        evidence = {
            "authorized": True, "resale_allowed": True,
            "capacity_checked": True, "benchmark_passed": True,
            "timing_confirmed": True,
        }
        rid = intake(db, "tenant-a", "order-1", "gpu_hour", 10, evidence)
        reserve(db, rid)
        reserve(db, rid)

        class TestProvider:
            def execute_or_lookup(self, key, payload):
                return {
                    "provider_key": key,
                    "receipt_id": "test:receipt:" + key,
                    "delivered_units": payload["units"],
                    "upstream_cents": 875,
                }

        dispatch(db, rid, TestProvider())
        dispatch(db, rid, TestProvider())
        record_cost(db, "test:bank:1", "UPSTREAM_PAID", 875, rid)
        qa(db)
        row = dict(db.execute("SELECT * FROM reconciliation").fetchone())
        if (row["billings"], row["retained_contribution"],
                row["wallet_liability"]) != (2500, 1625, 7500):
            raise AssertionError("Smoke reconciliation failed")
        return row
    finally:
        db.close()
""",
                        "QA reads one serialized snapshot and fails explicitly when ledger or state invariants diverge.",
                        "The smoke scenario is supplied, not executed here; add parallel-worker and crash-recovery integration tests.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build the isolated reference service",
                    "action": "Concatenate the six artifacts in order and invoke smoke() against its disposable database.",
                    "detail": "Use a separate production database path, restricted filesystem permissions, authenticated service endpoints, and tested encrypted backups.",
                },
                {
                    "step": 2,
                    "title": "Connect trusted evidence and payment adapters",
                    "action": "Map verified Stripe payment objects and reviewed service evidence into credit_settled() and intake().",
                    "detail": "Reject client-supplied approval flags; namespace identifiers by processor account and handle disputes through a separately controlled ledger extension.",
                },
                {
                    "step": 3,
                    "title": "Prove crash-safe dispatch before committing inventory",
                    "action": "Run concurrent reservations, simultaneous cancellation and dispatch, repeated callbacks, and worker termination after provider acceptance.",
                    "detail": "Require one upstream resource per provider key and one billing event per request; unresolved execution retains its hold.",
                },
                {
                    "step": 4,
                    "title": "Close the ledger against external evidence",
                    "action": "Match payment settlements, accepted meter records, carrier invoices, operating bills, and bank transfers before reporting profit.",
                    "detail": "Run qa(), inspect reconciliation, age review jobs, and document every residual variance with a source record and accountable operator.",
                },
            ],
        },
        {
            "heading": "3. Operate metering, tenant isolation, and telecom authority as one delivery system",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build delivery around an immutable service identifier that appears in the "
                    "order, workload scheduler, provider request, meter event, and ledger receipt. "
                    "LiteLLM can route model requests, while vLLM serves approved models on "
                    "reserved accelerators; neither component independently proves customer "
                    "acceptance or accounting accuracy. Capture request identifiers, model "
                    "versions, token counts, timestamps, and status codes without storing prompt "
                    "or response bodies for zero-retention customers. Use NVIDIA DCGM to detect "
                    "hardware faults, throttling, and capacity contention, then reconcile its "
                    "operational telemetry with application-level delivery records. A ten-minute "
                    "occupied GPU interval may contain failed loading or retry work that the "
                    "contract does not permit billing. Separate tenants through the promised "
                    "hardware or virtualization boundary, restricted network paths, scoped "
                    "credentials, and per-tenant storage controls. A MIG allocation partitions "
                    "supported GPU resources but does not replace host security or application "
                    "authorization. Test cross-tenant access with synthetic records and verify "
                    "that crash dumps, traces, caches, and support exports honor the same "
                    "retention policy. When a provider cannot meet the agreed boundary, remove "
                    "that provider from the customer's routing policy rather than weakening "
                    "the customer commitment during a utilization dip."
                ),
                (
                    "Telecom delivery adds role-specific operating duties that cannot be collapsed "
                    "into one registration checkbox. Determine whether the business acts as a "
                    "voice service provider, gateway provider, intermediate provider, messaging "
                    "reseller, or customer of a carrier, and preserve the corresponding contracts. "
                    "Apply 47 CFR 64.6301 and 64.6305 according to the actual role, including "
                    "applicable caller-ID authentication, mitigation, certification, and database "
                    "obligations. Do not interpret a carrier's STIR/SHAKEN signature as permission "
                    "for a customer to make unlawful calls. Review calling authority and suppression "
                    "requirements under 47 U.S.C. 227 and 47 CFR 64.1200 using the actual traffic "
                    "type. Brand and campaign enrollment through The Campaign Registry is a "
                    "carrier ecosystem requirement for relevant 10DLC traffic, not a substitute "
                    "for statutory calling or messaging duties. Assess FCC Form 499-A reporting "
                    "and contribution treatment using 47 CFR 54.706 and 54.711, service "
                    "classification, and the current form instructions. Least-cost routing must "
                    "preserve required identity handling and permitted traffic classes. Suspend "
                    "unexpected international destinations, rapid number rotation, or abuse "
                    "complaints while investigating; do not switch carriers simply to evade "
                    "a carrier's protective restriction."
                ),
                (
                    "Daily operations should produce a short exception queue rather than a "
                    "large dashboard that nobody owns. The full-time operator controls quoting, "
                    "cash allocation, customer acceptance, and commitment changes. One contractor "
                    "handles platform reliability and metering; another handles carrier operations, "
                    "evidence review, and reconciliation support. Contractors receive scoped "
                    "access rather than shared administrator credentials. Every morning, compare "
                    "open holds with running jobs, accepted delivery with billing events, and "
                    "upstream invoices with recorded accruals. Every afternoon, examine prepaid "
                    "runway, next-day concurrency, expensive destinations, and approaching "
                    "commitment renewals. Define a replenishment threshold that covers the maximum "
                    "uninterruptible service interval; stopping at exactly zero can leave "
                    "unfunded work already in flight. Freeze new dispatch on unexplained ledger "
                    "variance, unresolved tenant isolation, or ambiguous provider execution, "
                    "while preserving evidence and existing safe workloads. Revenue corrections "
                    "need append-only adjustment records in the extended production ledger, "
                    "not edits to settled events. Track chargebacks, service credits, and taxes "
                    "separately when applicable; the reference core intentionally excludes those "
                    "additional workflows. A useful close ends with attributable residuals and "
                    "documented next actions, not a forced match produced by overwriting "
                    "the carrier invoice or deleting an inconvenient meter event."
                ),
            ],
            "table": {
                "caption": "Delivery Evidence and Exception Ownership Across Compute, Inference, and Telecom",
                "headers": [
                    "Control surface and accountable operating owner",
                    "Required evidence retained without unnecessary customer content",
                    "Concrete test or reconciliation acceptance criterion",
                    "Failure response that preserves cash and evidence",
                ],
                "rows": [
                    [
                        "Platform contractor owns accelerator scheduling and hardware health evidence.",
                        "Retain scheduler assignments, GPU identifiers, DCGM fault counters, and workload timestamps.",
                        "Compare accepted GPU-hours with reserved windows; investigate unexplained overlap before billing.",
                        "Quarantine unhealthy devices and shift only to customer-approved compatible capacity.",
                    ],
                    [
                        "Platform contractor owns LiteLLM routing and vLLM model deployment controls.",
                        "Retain approved model digests, provider policies, token counters, and request outcomes.",
                        "Replay synthetic requests across approved providers and compare latency, cost, and output acceptance.",
                        "Remove failing providers from policy without persisting customer prompts for debugging.",
                    ],
                    [
                        "Full-time operator owns tenant isolation and enterprise retention commitments.",
                        "Retain access-test results, deletion settings, credential scopes, and contract-specific routing restrictions.",
                        "Confirm synthetic tenant records cannot cross authorization boundaries or enter persistent diagnostics.",
                        "Stop affected tenant dispatch until isolation and retention behavior match the contract.",
                    ],
                    [
                        "Carrier contractor owns SIP route authorization and caller identity handling.",
                        "Retain destination tariffs, call detail records, number authority, and applicable authentication records.",
                        "Reprice sampled calls using actual increments and verify permitted identity treatment.",
                        "Suspend suspicious traffic and investigate with the contracted carrier before changing routes.",
                    ],
                    [
                        "Carrier contractor owns 10DLC brand, campaign, and suppression operations.",
                        "Retain registration references, approved use cases, messaging authority evidence, and opt-out events.",
                        "Reject messages outside registered scope and confirm suppression propagates before another send.",
                        "Keep rejected campaigns inactive and resolve evidence gaps rather than rotating numbers.",
                    ],
                    [
                        "Full-time operator owns provider classification, reporting calendar, and carrier documentation.",
                        "Retain role analysis, applicable database submissions, Form 499 records, and service classifications.",
                        "Review 47 CFR 64.6305 and 54.711 applicability against actual services and contracts.",
                        "Pause unsupported service expansion and obtain the missing classification or reporting evidence.",
                    ],
                    [
                        "Full-time operator owns ledger close with independent contractor review.",
                        "Retain payment objects, accepted receipts, supplier invoices, bank references, and variance explanations.",
                        "Wallet liabilities equal collected deposits less earned billings within the core model.",
                        "Hold distributions while material differences remain; preserve immutable originals for correction.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before accepting production exposure",
                "body": "Each check requires recorded evidence tied to the customer, service, and current upstream contract.",
                "items": [
                    "Verify usable prepaid funds, unreserved wallet availability, and enough coverage for the longest uninterruptible delivery interval.",
                    "Verify resale rights, actual concurrency, model or hardware compatibility, and a priced fallback that preserves the promised service.",
                    "Verify applicable telecom role duties, traffic authority, carrier registration requirements, and suppression handling before routing communications.",
                    "Verify durable provider idempotency, crash recovery, tenant isolation, and retention controls with synthetic production-like tests.",
                ],
            },
        },
        {
            "heading": "4. Walk three paid cohorts to Base-case profit and reconciled cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The worked walk begins with a launch-ready sales pipeline and $30,000 "
                    "opening operating cash contributed by the owner. This opening capital "
                    "is not revenue, and the model purchases no hardware. Leased capacity "
                    "costs appear in upstream expense. The example is a steady-volume "
                    "replacement-cohort stress test, not a claim that an unprepared startup "
                    "immediately reaches Base economics; the scorecard allows one to four "
                    "months to the first deal. Each active monthly customer buys the "
                    "$6,250 bundle described earlier. Month 1 screens 30 leads, scrubs "
                    "12, and closes nine of the remaining 18 as cohort A. "
                    "Month 2 screens 36 leads, scrubs 16, and closes three of "
                    "20 qualified accounts as cohort B; six A customers renew. "
                    "Month 3 screens 40 leads, scrubs 18, and closes three of "
                    "22 qualified accounts as cohort C; four A and two B "
                    "customers renew. Every month therefore serves nine customers and "
                    "bills $56,250. Nonrenewals remove future volume rather than reversing "
                    "accepted prior service. The unusually visible churn forces the "
                    "operator to prove replacement demand before renewing the next "
                    "capacity commitment instead of assuming every pilot becomes permanent."
                ),
                (
                    "Cash collections deliberately differ from earned billings. Month 1 "
                    "collects $67,500 before dispatch: $56,250 for that month's delivered "
                    "service plus $11,250 remaining prepaid credit belonging to customers "
                    "who continue into Month 2. Month 2 collects another $56,250 "
                    "before its service intervals and finishes with the same $11,250 "
                    "wallet liability, assigned to continuing customers. Month 3 collects "
                    "$45,000 before service and consumes the carried $11,250, ending "
                    "with no unearned credit. Credit never transfers between unrelated "
                    "customer wallets. Departing accounts have exhausted their balances "
                    "before nonrenewal. All three months pay $19,687.50 upstream and "
                    "$20,812.50 subsequent operating costs within the month. The latter "
                    "contains $10,000 recurring overhead and $10,812.50 delivery labor "
                    "and contractor allocation, paid in cash here. This explicitly "
                    "separates the headline $2,000–$14,000 monthly overhead range from "
                    "the complete cost stack needed to reproduce Base owner profit. "
                    "Operating cash increases $27,000, $15,750, and $4,500 respectively. "
                    "The early cash surplus is partly a service obligation, not "
                    "additional profit. No tax collections, chargebacks, disputed invoices, "
                    "or separate customer refunds are assumed in this worked cohort; "
                    "introducing any of them requires additional cash and liability rows."
                ),
                (
                    "At Day 90, cumulative billings and collections both equal $168,750. "
                    "Upstream expense and payments total $59,062.50, leaving $109,687.50 "
                    "retained contribution. Subsequent costs total $62,437.50, so both "
                    "cumulative owner profit and operating cash increase equal $47,250. "
                    "Opening capital plus that increase produces $77,250 bank cash "
                    "before owner distributions. Annualizing the steady monthly service "
                    "volume yields $675,000 gross billings, $236,250 upstream costs, "
                    "$438,750 retained contribution, $249,750 subsequent costs, and "
                    "$189,000 owner profit. That is 28.0% of gross billings "
                    "and 43.08% of retained contribution, with one full-time operator "
                    "and two contractors. Conservative economics likewise reconcile "
                    "$150,000 gross less $52,500 upstream less $70,500 subsequent "
                    "costs to $27,000 profit. Scaled economics reconcile $1,200,000 "
                    "gross less $420,000 upstream less $324,000 subsequent costs "
                    "to $456,000 profit, supported by two full-time people and "
                    "three contractors. These are complete scenario bridges, not "
                    "margins applied to customer deposits. Before distributing cash, "
                    "reserve the next upstream commitment, actual payroll obligations, "
                    "and any customer credit liability. Stress the next cohort "
                    "against falling hardware resale prices and replacement-sales delays; "
                    "a profitable closed quarter cannot finance an indefinitely "
                    "underutilized future commitment."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and paid customer cohort movement",
                    "Lead screening, scrubs, and commercial losses",
                    "Earned gross billings and upstream expense",
                    "Collected cash timing and remaining wallet liability",
                    "Subsequent operating costs and earned owner profit",
                    "Operating cash movement and cumulative cash position",
                ],
                "rows": [
                    [
                        "Month 1 serves nine new cohort A customers at $6,250 each.",
                        "Thirty leads minus twelve scrubs leave eighteen qualified; nine close and nine remain unconverted.",
                        "$56,250 earned billings less $19,687.50 upstream produce $36,562.50 retained contribution.",
                        "$67,500 collected before service leaves $11,250 unearned credit in continuing customers' wallets.",
                        "$10,000 overhead plus $10,812.50 delivery labor leaves $15,750 earned owner profit.",
                        "$27,000 cash increase yields $27,000 cumulative increase and $57,000 closing bank cash.",
                    ],
                    [
                        "Month 2 serves six renewing A customers plus three new B customers.",
                        "Thirty-six leads minus sixteen scrubs yield twenty qualified; three close while three A customers leave.",
                        "$56,250 earned billings less $19,687.50 upstream again produce $36,562.50 retained contribution.",
                        "$56,250 collected before service preserves $11,250 unearned credit allocated only to continuing customers.",
                        "$20,812.50 complete subsequent costs again leave $15,750 earned owner profit.",
                        "$15,750 cash increase yields $42,750 cumulative increase and $72,750 closing bank cash.",
                    ],
                    [
                        "Month 3 serves four renewing A, two renewing B, and three new C customers.",
                        "Forty leads minus eighteen scrubs yield twenty-two qualified; three close while two A and one B leave.",
                        "$56,250 earned billings less $19,687.50 upstream maintain $36,562.50 retained contribution.",
                        "$45,000 collected before service plus $11,250 carried credit funds delivery; closing wallet liability is zero.",
                        "$20,812.50 complete subsequent costs again leave $15,750 earned owner profit.",
                        "$4,500 cash increase yields $47,250 cumulative increase and $77,250 closing bank cash.",
                    ],
                    [
                        "Quarter total comprises twenty-seven customer-months across fifteen distinct paying customers.",
                        "One hundred six leads produce forty-six scrubs, sixty qualified accounts, and fifteen new wins.",
                        "$168,750 earned billings less $59,062.50 upstream produce $109,687.50 retained contribution.",
                        "$168,750 total collections equal earned billings after all carried prepaid credit is consumed.",
                        "$62,437.50 subsequent costs leave $47,250 quarterly owner profit at 28.0% gross margin.",
                        "$47,250 cumulative operating cash increase reconciles exactly to quarterly earned owner profit.",
                    ],
                    [
                        "Base annual run rate repeats nine active monthly customers without adding duplicate service revenue.",
                        "Replacement sales must sustain nine active customers; annual lead counts require their own forecast.",
                        "$675,000 gross billings less $236,250 upstream produce $438,750 retained contribution at 65%.",
                        "Steady-state earned collections equal $675,000 annually when opening and closing wallet liabilities match.",
                        "$249,750 subsequent costs leave $189,000 profit, or 43.08% of retained contribution.",
                        "One full-time operator and two contractors support the modeled Base operating cost allocation.",
                    ],
                    [
                        "Conservative and Scaled bridges preserve the same canonical sixty-five-percent retained contribution assumption.",
                        "Conservative staffing is one full-time plus two contractors; Scaled staffing is two plus three.",
                        "Conservative retains $97,500 from $150,000; Scaled retains $780,000 from $1,200,000 gross billings.",
                        "Prepaid collection timing must be modeled separately because these annual scorecards specify earned economics.",
                        "Subsequent costs of $70,500 and $324,000 yield respective profits of $27,000 and $456,000.",
                        "Gross margins are 18% and 38%; retained margins are 27.69% and 58.46%, respectively.",
                    ],
                    [
                        "Day 90 liquidity decision separates available bank cash from future contracted operating exposure.",
                        "No wallet losses occur here; adding disputes or refunds requires explicit replacement cash assumptions.",
                        "The next monthly upstream commitment remains $19,687.50 before any revised capacity purchase.",
                        "$77,250 bank cash contains original $30,000 capital and $47,250 accumulated operating cash increase.",
                        "Preserving one modeled month of upstream and subsequent costs reserves $40,500 before distributions.",
                        "$36,750 remains after that reserve, before taxes, new commitments, or additional risk buffers.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A capacity spread becomes profit only when authorized delivery, an immutable meter event, and reconciled cash describe the same service.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one intake record linking buyer authority, workload requirements, upstream resale rights, prepaid funding, and a bounded service tariff.",
        "Corroborate technographic changes with passive DNS, public job evidence, and buyer timing before treating Month 10–11 as a renewal opportunity.",
        "Implement the six ledger modules, then test duplicate payments, parallel reservations, cancellation races, and interrupted provider execution.",
        "Connect tenant-scoped LiteLLM/vLLM delivery and application meters; use DCGM for health and capacity evidence rather than automatic billing.",
        "Document applicable telecom roles, authentication and mitigation duties, 10DLC requirements, reporting obligations, and suppression operations.",
        "Close the three-month cohort against bank settlements and supplier records; reproduce $47,250 quarterly profit before annualizing to $189,000.",
    ],
    "statutory_citations": [
        {
            "title": "47 U.S.C. 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Evaluate calling and messaging restrictions against the actual equipment, recipients, authorization, and traffic use case before accepting customer campaigns.",
        },
        {
            "title": "47 CFR 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Implement applicable calling, messaging, identification, authorization, and suppression requirements rather than treating carrier acceptance as sufficient authority.",
        },
        {
            "title": "47 CFR 64.6301 — Caller ID authentication",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6301",
            "relevance": "Determine applicable caller-ID authentication duties from the operator's actual provider role and network arrangements before configuring SIP routes.",
        },
        {
            "title": "47 CFR 64.6305 — Robocall mitigation and certification",
            "url": "https://www.ecfr.gov/current/title-47/section-64.6305",
            "relevance": "Assess applicable mitigation, certification, database, and traffic-handling obligations for the business and its upstream relationships.",
        },
        {
            "title": "47 CFR 54.706 — Contributions",
            "url": "https://www.ecfr.gov/current/title-47/section-54.706",
            "relevance": "Classify offered telecommunications services and determine contribution treatment using actual service scope, customer relationships, and applicable exceptions.",
        },
        {
            "title": "47 CFR 54.711 — Contributor reporting requirements",
            "url": "https://www.ecfr.gov/current/title-47/section-54.711",
            "relevance": "Build the applicable contributor reporting calendar and reconcile relevant service revenue classifications to current FCC Form 499 instructions.",
        },
        {
            "title": "47 U.S.C. 222 — Privacy of customer information",
            "url": "https://www.law.cornell.edu/uscode/text/47/222",
            "relevance": "Evaluate telecommunications customer information duties and restrict access to traffic records, customer relationships, and related protected information.",
        },
    ],
}
