from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "automated-e-commerce-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute automated e-commerce end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Authorized-Dealer Intake, 3PL Routing, SQLite Event Controls, FTC Shipping Duties, and a Cash-Reconciled Retail Cohort",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #28, Automated E-Commerce, ranks #21 with a 85/100 "
        "Money-to-Manpower Score across 18 mapped plays. Execution depends on "
        "authorized inventory, contribution-positive acquisition, deterministic order "
        "routing, and settlement evidence—not unattended storefront software. This "
        "chapter connects sixteen retail workstreams with two adjacent mapped plays, "
        "then supplies a six-module SQLite reference and a worked three-month cash "
        "bridge. Annual owner profit remains $12,500 Conservative, $129,375 Base, "
        "and $360,000 Scaled. The Base walk produces $93,750 monthly recognized "
        "retail revenue and $10,781.25 monthly profit while exposing processor "
        "settlement lag, inventory funding, returns, and fixed overhead. Operators "
        "can reproduce the ledger checks, assign exception ownership, and distinguish "
        "earned profit from immediately spendable cash."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual recognized retail sales net of refunds",
            "note": "5% net margin; $12,500 annual owner profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,125,000",
            "context": "Annual recognized retail sales net of refunds",
            "note": "11.5% net margin; $129,375 annual owner profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$2,000,000",
            "context": "Annual recognized retail sales net of refunds",
            "note": "18% net margin; $360,000 annual owner profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Qualify inventory, underwrite contribution, and release only executable orders",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with an authorized-dealer packet, not an advertising campaign. "
                    "The operator records supplier identity, resale authorization, permitted "
                    "channels, warranty responsibility, landed unit cost, carton dimensions, "
                    "lead time, and the exact product identifiers accepted by the warehouse. "
                    "Match the purchase order, supplier invoice, and receiving report before "
                    "making stock available. Product images and descriptions require usable "
                    "rights; a distributor invoice alone does not establish every marketing "
                    "permission. For imported goods, assign importer-of-record responsibility "
                    "and classify duties before underwriting margin under 19 U.S.C. 1484. "
                    "For consumer products, identify applicable testing, certification, "
                    "traceability, and reporting duties rather than assuming the supplier "
                    "absorbs them. Section 15(b) of the Consumer Product Safety Act, "
                    "15 U.S.C. 2064(b), creates reporting obligations when the statutory "
                    "conditions are met. Quarantine a suspect lot, preserve customer and "
                    "shipment identifiers, and give one named employee authority to stop "
                    "sales. This chapter organizes sixteen retail workstreams plus the "
                    "two specified adjacent plays into eighteen operating lanes; it does "
                    "not manufacture additional catalog identifiers. The storefront owns "
                    "retail revenue only when it sells goods as principal; marketplace "
                    "volume or a partner merchant's turnover is not operator revenue."
                ),
                (
                    "Underwrite each SKU through a contribution worksheet that reconciles "
                    "to the ledger. In the Base illustration, 1,000 fulfilled orders at "
                    "$100 create $100,000 before refunds. Refunds of $6,250 leave $93,750 "
                    "recognized retail revenue. Product cost is $37,500, fulfillment is "
                    "$7,500, advertising is $18,750, and processor expense is $3,000, "
                    "leaving $27,000 before $16,218.75 fixed operating expense. That "
                    "produces $10,781.25 monthly owner profit, exactly 11.5% of revenue. "
                    "The $18.75 advertising allowance per fulfilled order is a blended "
                    "operating assumption, not permission to buy every incremental order "
                    "at that price. Segment new-customer acquisition from repeat orders "
                    "and evaluate refunds by original acquisition cohort. At the stated "
                    "mix, pre-advertising contribution is $45.75 per fulfilled order; "
                    "additional acquisition spend consumes that contribution dollar for "
                    "dollar before overhead changes. Shopify or WooCommerce can capture "
                    "orders, while a 3PL performs physical execution, but neither dashboard "
                    "replaces this calculation. If a carrier surcharge or advertising "
                    "auction destroys the SKU's allowance, suppress that SKU's campaign, "
                    "revise its offer, or stop replenishment. Do not disguise an operating "
                    "loss with projected repeat purchases that have not occurred."
                ),
                (
                    "Translate the worksheet into explicit release criteria. Intake checks "
                    "price version, available stock, destination serviceability, dealer "
                    "restrictions, and payment evidence before any warehouse instruction. "
                    "Use integer cents and stable storefront order identifiers; a repeated "
                    "webhook must retrieve the existing order rather than reserve another "
                    "unit. Separate available inventory from quarantine, damaged stock, "
                    "and inbound purchase orders. A reorder alert should compare usable "
                    "stock with lead-time demand plus safety stock, not merely announce "
                    "that a shelf is nearly empty. At thirty daily units, twenty days "
                    "of replenishment lead time, and ten days of buffer, the reorder "
                    "point is 900 usable units. Demand volatility, supplier reliability, "
                    "and carton economics determine whether that buffer is adequate. "
                    "The 3PL must return accepted quantities, shipment identifiers, and "
                    "delivery exceptions that can be joined to the original order. "
                    "Under 16 CFR 435.2, shipping representations require an appropriate "
                    "basis, and delays require the prescribed customer options and "
                    "refund handling. A stockout therefore triggers customer communication "
                    "and a recorded disposition, not an indefinite payment hold. The "
                    "matrix assigns paired workstreams so the two-person core team "
                    "can delegate specialist work without surrendering exception ownership."
                ),
            ],
            "table": {
                "caption": "Sixteen Retail Workstreams Paired into Eight Evidence-Producing Operating Lanes",
                "headers": [
                    "Paired operating workstreams",
                    "Required evidence and system record",
                    "Release condition and accountable operator",
                    "Failure response and economic consequence",
                ],
                "rows": [
                    [
                        "Dealer authorization and supplier intake establish selling rights",
                        "Store signed channel permissions beside supplier identity and invoices",
                        "Merchandising owner confirms authorized products before catalog publication",
                        "Suspend unsupported listings before advertising creates stranded customer orders",
                    ],
                    [
                        "Product safety and import classification establish landed obligations",
                        "Link lot records, applicable certificates, tariff classification, and entry evidence",
                        "Operations owner verifies required documentation before releasing received inventory",
                        "Quarantine affected lots and calculate duty corrections before repricing",
                    ],
                    [
                        "Catalog quality and accessibility testing improve executable customer journeys",
                        "Version product claims, image rights, semantic labels, and keyboard evidence",
                        "Storefront owner tests product selection through completed checkout manually",
                        "Repair broken templates rather than buying traffic into unusable pages",
                    ],
                    [
                        "Inventory availability and replenishment planning prevent oversold physical stock",
                        "Join warehouse receipts, reservation counts, lead times, and reorder calculations",
                        "Operations owner reserves usable stock inside the intake transaction",
                        "Pause affected advertisements and resolve delayed orders with recorded options",
                    ],
                    [
                        "Checkout integrity and tax determination separate liabilities from revenue",
                        "Retain price version, destination treatment, payment reference, and tax calculation",
                        "Payment owner matches captured amount against the accepted order",
                        "Reject mismatched captures and investigate without releasing warehouse instructions",
                    ],
                    [
                        "Order routing and shipment verification connect promises to execution",
                        "Persist immutable routing payloads and warehouse acceptance reference identifiers",
                        "Operations owner releases only captured orders with available reserved units",
                        "Retry using stable provider keys or move unsupported integrations offline",
                    ],
                    [
                        "Returns disposition and retention segmentation protect realized customer value",
                        "Attach refund reasons, recoverable inventory decisions, and channel preferences",
                        "Support owner separates damage, remorse, fraud, and delivery failures",
                        "Suppress unsuitable offers and quarantine returns requiring product inspection",
                    ],
                    [
                        "Settlement matching and cohort review distinguish earnings from liquidity",
                        "Reconcile order journals, processor balances, bank deposits, and advertising invoices",
                        "Bookkeeping owner signs the cash bridge before increasing acquisition budgets",
                        "Freeze budget expansion when unexplained clearing balances exceed documented timing",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before paid acquisition",
                "body": (
                    "The operator records evidence for each check before making the "
                    "offer purchasable or increasing its acquisition budget."
                ),
                "items": [
                    "Verify dealer permissions, applicable product evidence, landed costs, and lot traceability against the exact sellable SKU.",
                    "Run a duplicate-order test and a competing-order stock test; neither may create a second reservation for the same accepted order.",
                    "Match a captured payment, warehouse acceptance, refund, processor settlement, and bank deposit using persistent identifiers.",
                    "Confirm shipping promises, delay handling, subscription terms where applicable, keyboard checkout, and customer-support ownership using recorded test cases.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Receive and qualify",
                    "action": "Create the supplier, SKU, cost, and inventory evidence packet.",
                    "detail": "Separate usable inventory from quarantine and reconcile the receiving report to the supplier invoice before storefront availability changes.",
                },
                {
                    "step": 2,
                    "title": "Accept and verify",
                    "action": "Reserve stock atomically and authenticate the captured-payment event.",
                    "detail": "Compare integer cents, merchant account, order reference, and capture identifier before creating the warehouse outbox record.",
                },
                {
                    "step": 3,
                    "title": "Route and fulfill",
                    "action": "Submit the immutable shipment request with its persistent idempotency key.",
                    "detail": "Store warehouse acceptance, then recognize sales and product cost at the documented shipment or delivery recognition point.",
                },
                {
                    "step": 4,
                    "title": "Refund and reconcile",
                    "action": "Post verified refund, fee, and deposit events before reviewing cohort performance.",
                    "detail": "Resolve clearing differences, update return disposition, and compare realized contribution against the original acquisition allowance.",
                },
            ],
        },
        {
            "heading": "2. Implement the six-module ledger and an idempotent order workflow",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference below is a deliberately narrow, executable single-SKU "
                    "order kernel, not an entire storefront connector. Save the SQL "
                    "cells as schema.sql and reconcile.sql, then concatenate the Python "
                    "cells in order into reference.py in the same directory. Run "
                    "python reference.py to execute the temporary-database checks. All "
                    "amounts are integer cents, every journal row contains equal debit "
                    "and credit amounts, and every external event has a unique operation "
                    "key. SQLite BEGIN IMMEDIATE serializes competing writers before "
                    "stock reservation or state changes; conditional updates enforce "
                    "availability within that same transaction. Reusing an order key "
                    "with different commercial terms raises an error instead of silently "
                    "changing history. The schema assumes a single merchant ledger "
                    "and a durable local filesystem suitable for SQLite locking. "
                    "Use PostgreSQL with equivalent uniqueness and row-locking behavior "
                    "when deployment requires multiple database hosts; do not put this "
                    "SQLite file on an unreliable shared drive. Back up the database "
                    "and test restoration before accepting live orders. Application "
                    "access is the supported write path, and direct database edits "
                    "are prohibited operationally. These boundaries matter: database "
                    "constraints cannot authenticate an untrusted processor message or "
                    "prove that a physical shipment actually arrived."
                ),
                (
                    "Verification means matching authenticated provider evidence to "
                    "the order, not trusting a browser redirect. The payment adapter "
                    "must verify the provider signature, merchant account, currency, "
                    "captured status, amount, and order reference before calling verify. "
                    "The internal held state is an inventory reservation; it is not "
                    "escrow and does not authorize custody services. A captured payment "
                    "debits processor clearing and credits deferred sales until fulfillment "
                    "meets the documented recognition policy. This example recognizes "
                    "at confirmed delivery. Production orders need taxes, discounts, "
                    "multiple lines, partial shipments, cancellations, and jurisdiction-specific "
                    "handling added as explicit events, not hidden mutations. The outbox "
                    "separates committed intent from external network execution. Concurrent "
                    "workers can submit the same immutable request, but they must "
                    "use the same provider key, and the provider must guarantee "
                    "idempotent creation with stable response identity throughout the "
                    "retry window. A local transaction alone cannot prevent duplicate "
                    "remote shipments after a timeout. If an integration lacks that "
                    "contract, disable automatic submission and use a controlled "
                    "search-and-reconcile queue. Early delivery notifications remain "
                    "in the adapter's durable retry inbox until warehouse acceptance "
                    "has been recorded; they never force the order backward."
                ),
                (
                    "Reconciliation starts with separate asset, liability, revenue, "
                    "and expense balances. Captures increase processor clearing; refunds, "
                    "fees, and bank settlements reduce it. Delivery releases deferred "
                    "sales and posts product cost against inventory. The order view "
                    "therefore reports recognized sales separately from bank cash, "
                    "while the trial-balance view includes inventory funding, advertising, "
                    "fulfillment expense, overhead, and owner capital when those "
                    "events are posted. A batch payout must be allocated from "
                    "processor detail rather than posted as unexplained revenue. "
                    "Sales taxes belong in a payable account, not in sales; "
                    "the cohort excludes tax flows to keep its retail comparison "
                    "clean. The reference rejects refund totals above delivered order "
                    "value and rejects changed payloads under reused journal keys. "
                    "Its concurrent tests exercise repeated intake, repeated capture, "
                    "competing outbox workers, repeated delivery, and repeated refunds. "
                    "Before deployment, add authenticated adapter tests, crash injection "
                    "between provider response and local acknowledgment, backup recovery, "
                    "and expired-provider-key behavior. Never describe these checks "
                    "as proof against every infrastructure failure. Within the stated "
                    "database and provider contracts, stock changes and local postings "
                    "are serialized and remote retries preserve one shipment identity. "
                    "A failed invariant stops routing while an operator resolves "
                    "the evidence gap."
                ),
            ],
            "table": {
                "caption": "6-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and executable file placement",
                    "Copy-pasteable schema or reference implementation",
                    "Concurrency and evidence contract",
                    "Operational extension before live customer use",
                ],
                "rows": [
                    [
                        "Module 1: Save this database definition as schema.sql",
                        '''PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;
CREATE TABLE stock (
    sku TEXT PRIMARY KEY,
    available INTEGER NOT NULL CHECK (available >= 0),
    unit_cost INTEGER NOT NULL CHECK (unit_cost >= 0)
);
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    external_key TEXT NOT NULL UNIQUE,
    payload TEXT NOT NULL,
    sku TEXT NOT NULL REFERENCES stock(sku),
    qty INTEGER NOT NULL CHECK (qty > 0),
    gross INTEGER NOT NULL CHECK (gross > 0),
    cost INTEGER NOT NULL CHECK (cost >= 0),
    state TEXT NOT NULL CHECK (
        state IN ('held', 'paid', 'shipped', 'fulfilled')
    ),
    capture_ref TEXT UNIQUE
);
CREATE TABLE accounts (
    name TEXT PRIMARY KEY
);
INSERT INTO accounts(name) VALUES
    ('cash'), ('processor'), ('deferred'), ('sales'),
    ('returns'), ('fees'), ('inventory'), ('cogs'),
    ('fulfillment'), ('advertising'), ('overhead'),
    ('equity'), ('tax_payable');
CREATE TABLE journal (
    id INTEGER PRIMARY KEY,
    op_key TEXT NOT NULL UNIQUE,
    order_id INTEGER REFERENCES orders(id),
    debit TEXT NOT NULL REFERENCES accounts(name),
    credit TEXT NOT NULL REFERENCES accounts(name),
    cents INTEGER NOT NULL CHECK (cents > 0),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (debit <> credit)
);
CREATE TABLE outbox (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL UNIQUE REFERENCES orders(id),
    provider_key TEXT NOT NULL UNIQUE,
    body TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'done')),
    receipt TEXT UNIQUE,
    CHECK (
        (status = 'pending' AND receipt IS NULL)
        OR (status = 'done' AND receipt IS NOT NULL)
    )
);
CREATE INDEX journal_order_lookup ON journal(order_id);
CREATE INDEX pending_outbox_lookup ON outbox(status, id);''',
                        "Unique order, capture, operation, and provider keys prevent duplicate local identities; inventory checks reject negative available quantities.",
                        "Add explicit line items, currencies, tax liabilities, reservation expiry, reversals, and durable authenticated incoming-event storage before broader deployment.",
                    ],
                    [
                        "Module 2: Begin reference.py with intake, scoring, and posting primitives",
                        '''from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager


def connect(path):
    connection = sqlite3.connect(
        str(path), timeout=30, isolation_level=None
    )
    connection.execute("PRAGMA foreign_keys=ON")
    connection.execute("PRAGMA busy_timeout=30000")
    connection.execute("PRAGMA synchronous=FULL")
    return connection


@contextmanager
def atomic(path):
    connection = connect(path)
    try:
        connection.execute("BEGIN IMMEDIATE")
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def positive_int(value):
    if type(value) is not int or value <= 0:
        raise ValueError("Expected a positive integer")


def book(connection, key, order_id, debit, credit, cents):
    positive_int(cents)
    if not isinstance(key, str) or not key:
        raise ValueError("A persistent operation key is required")
    expected = (order_id, debit, credit, cents)
    existing = connection.execute(
        "SELECT order_id, debit, credit, cents "
        "FROM journal WHERE op_key = ?", (key,)
    ).fetchone()
    if existing is not None:
        if existing != expected:
            raise ValueError("Operation key payload changed")
        return
    connection.execute(
        "INSERT INTO journal "
        "(op_key, order_id, debit, credit, cents) "
        "VALUES (?, ?, ?, ?, ?)",
        (key, order_id, debit, credit, cents),
    )


def record(path, key, order_id, debit, credit, cents):
    with atomic(path) as connection:
        book(connection, key, order_id, debit, credit, cents)


def score(gross, refunds, goods, fulfillment, ads, fees):
    values = (gross, refunds, goods, fulfillment, ads, fees)
    if any(type(value) is not int or value < 0 for value in values):
        raise ValueError("Scoring inputs must be nonnegative cents")
    net_sales = gross - refunds
    if net_sales <= 0:
        raise ValueError("Expected positive net retail sales")
    contribution = net_sales - goods - fulfillment - ads - fees
    return {
        "net_sales": net_sales,
        "contribution": contribution,
        "contribution_basis_points": contribution * 10000 // net_sales,
    }


def intake(path, external_key, sku, qty, unit_price):
    positive_int(qty)
    positive_int(unit_price)
    if not isinstance(external_key, str) or not external_key:
        raise ValueError("A storefront order key is required")
    payload = json.dumps(
        {"sku": sku, "qty": qty, "unit_price": unit_price},
        sort_keys=True, separators=(",", ":"),
    )
    with atomic(path) as connection:
        existing = connection.execute(
            "SELECT id, payload FROM orders WHERE external_key = ?",
            (external_key,),
        ).fetchone()
        if existing is not None:
            if existing[1] != payload:
                raise ValueError("Order key payload changed")
            return existing[0]
        stock = connection.execute(
            "SELECT unit_cost FROM stock WHERE sku = ?", (sku,)
        ).fetchone()
        if stock is None:
            raise ValueError("SKU has no receiving record")
        changed = connection.execute(
            "UPDATE stock SET available = available - ? "
            "WHERE sku = ? AND available >= ?",
            (qty, sku, qty),
        ).rowcount
        if changed != 1:
            raise ValueError("Insufficient usable inventory")
        cursor = connection.execute(
            "INSERT INTO orders "
            "(external_key, payload, sku, qty, gross, cost, state) "
            "VALUES (?, ?, ?, ?, ?, ?, 'held')",
            (
                external_key, payload, sku, qty,
                qty * unit_price, qty * stock[0],
            ),
        )
        return cursor.lastrowid''',
                        "BEGIN IMMEDIATE encloses duplicate detection, stock reservation, order creation, and balanced journal writes within serialized transactions.",
                        "Use score outputs with documented refund assumptions; authenticate commercial inputs and restrict direct database access to controlled maintenance.",
                    ],
                    [
                        "Module 3: Append verified-payment, delivery, and refund state transitions",
                        '''def verify(path, order_id, capture_ref, captured_cents):
    positive_int(captured_cents)
    if not isinstance(capture_ref, str) or not capture_ref:
        raise ValueError("A verified capture reference is required")
    with atomic(path) as connection:
        order = connection.execute(
            "SELECT external_key, sku, qty, gross, state, capture_ref "
            "FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if order is None or order[3] != captured_cents:
            raise ValueError("Capture does not match accepted order")
        external_key, sku, qty, gross, state, previous = order
        if state != "held":
            if previous != capture_ref:
                raise ValueError("Order already has another capture")
            book(
                connection, "capture:" + capture_ref, order_id,
                "processor", "deferred", gross,
            )
            return
        connection.execute(
            "UPDATE orders SET state = 'paid', capture_ref = ? "
            "WHERE id = ? AND state = 'held'",
            (capture_ref, order_id),
        )
        book(
            connection, "capture:" + capture_ref, order_id,
            "processor", "deferred", gross,
        )
        body = json.dumps(
            {"order_key": external_key, "sku": sku, "qty": qty},
            sort_keys=True, separators=(",", ":"),
        )
        connection.execute(
            "INSERT INTO outbox(order_id, provider_key, body) "
            "VALUES (?, ?, ?)",
            (order_id, "ship:" + external_key, body),
        )


def deliver(path, order_id):
    with atomic(path) as connection:
        order = connection.execute(
            "SELECT state, gross, cost FROM orders WHERE id = ?",
            (order_id,),
        ).fetchone()
        if order is None or order[0] not in ("shipped", "fulfilled"):
            raise ValueError("Retry after warehouse acceptance is recorded")
        book(
            connection, "sale:" + str(order_id), order_id,
            "deferred", "sales", order[1],
        )
        if order[2]:
            book(
                connection, "cost:" + str(order_id), order_id,
                "cogs", "inventory", order[2],
            )
        connection.execute(
            "UPDATE orders SET state = 'fulfilled' "
            "WHERE id = ? AND state = 'shipped'", (order_id,)
        )


def refund(path, order_id, refund_ref, cents):
    positive_int(cents)
    if not isinstance(refund_ref, str) or not refund_ref:
        raise ValueError("A verified refund reference is required")
    key = "refund:" + refund_ref
    with atomic(path) as connection:
        existing = connection.execute(
            "SELECT id FROM journal WHERE op_key = ?", (key,)
        ).fetchone()
        if existing is not None:
            book(connection, key, order_id, "returns", "processor", cents)
            return
        order = connection.execute(
            "SELECT state, gross FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if order is None or order[0] != "fulfilled":
            raise ValueError("This refund path requires fulfilled goods")
        refunded = connection.execute(
            "SELECT COALESCE(SUM(cents), 0) FROM journal "
            "WHERE order_id = ? AND debit = 'returns'",
            (order_id,),
        ).fetchone()[0]
        if refunded + cents > order[1]:
            raise ValueError("Refund exceeds delivered order value")
        book(connection, key, order_id, "returns", "processor", cents)''',
                        "Capture references remain unique, state changes never move backward, and refund limits are checked under the same write lock as posting.",
                        "Call only after authenticated evidence; add separate pre-delivery cancellation and reserved-stock release events rather than misusing delivered-goods refunds.",
                    ],
                    [
                        "Module 4: Append idempotent shipment submission with immutable outbox requests",
                        '''def dispatch_one(path, send):
    connection = connect(path)
    try:
        job = connection.execute(
            "SELECT id, order_id, provider_key, body FROM outbox "
            "WHERE status = 'pending' ORDER BY id LIMIT 1"
        ).fetchone()
    finally:
        connection.close()
    if job is None:
        return False
    job_id, order_id, provider_key, body = job
    receipt = send(body, idempotency_key=provider_key)
    if not isinstance(receipt, str) or not receipt:
        raise ValueError("Provider must return a stable shipment identifier")
    with atomic(path) as connection:
        current = connection.execute(
            "SELECT status, receipt FROM outbox WHERE id = ?", (job_id,)
        ).fetchone()
        if current[0] == "done":
            if current[1] != receipt:
                raise ValueError("Provider broke stable idempotency identity")
            return True
        connection.execute(
            "UPDATE outbox SET status = 'done', receipt = ? "
            "WHERE id = ? AND status = 'pending'",
            (receipt, job_id),
        )
        connection.execute(
            "UPDATE orders SET state = 'shipped' "
            "WHERE id = ? AND state = 'paid'", (order_id,)
        )
    return True''',
                        "Duplicate workers may contact the provider, but stable remote idempotency prevents duplicate shipment creation and local acknowledgment remains atomic.",
                        "Supply an authenticated adapter with documented key retention; preserve timed-out jobs and stop automatic retries before that retention window expires.",
                    ],
                    [
                        "Module 5: Save these reconciliation definitions as reconcile.sql",
                        '''CREATE VIEW order_reconciliation AS
SELECT
    o.id AS order_id,
    o.external_key,
    o.state,
    o.gross AS accepted_gross_cents,
    COALESCE(SUM(CASE
        WHEN j.credit = 'sales' THEN j.cents
        WHEN j.debit = 'returns' THEN -j.cents
        ELSE 0 END), 0) AS net_sales_cents,
    COALESCE(SUM(CASE
        WHEN j.debit = 'processor' THEN j.cents
        WHEN j.credit = 'processor' THEN -j.cents
        ELSE 0 END), 0) AS processor_balance_cents,
    COALESCE(SUM(CASE
        WHEN j.credit = 'deferred' THEN j.cents
        WHEN j.debit = 'deferred' THEN -j.cents
        ELSE 0 END), 0) AS deferred_balance_cents,
    COALESCE(SUM(CASE
        WHEN j.debit = 'cash' THEN j.cents
        WHEN j.credit = 'cash' THEN -j.cents
        ELSE 0 END), 0) AS bank_cash_cents,
    COALESCE(SUM(CASE
        WHEN j.debit = 'fees' THEN j.cents
        WHEN j.credit = 'fees' THEN -j.cents
        ELSE 0 END), 0) AS processor_fee_cents
FROM orders AS o
LEFT JOIN journal AS j ON j.order_id = o.id
GROUP BY o.id, o.external_key, o.state, o.gross;

CREATE VIEW trial_balance AS
SELECT account, SUM(signed_cents) AS debit_balance_cents
FROM (
    SELECT debit AS account, cents AS signed_cents FROM journal
    UNION ALL
    SELECT credit AS account, -cents AS signed_cents FROM journal
)
GROUP BY account;''',
                        "Views distinguish recognized sales, deferred sales, processor receivables, and bank movement without counting settlements as new retail revenue.",
                        "Allocate payout batches to order-level lines; post overhead without order identifiers and reconcile tax liabilities outside the simplified retail cohort.",
                    ],
                    [
                        "Module 6: Append reproducible concurrency checks and ledger assertions",
                        '''def run_checks():
    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path
    from tempfile import TemporaryDirectory

    def check(condition, message):
        if not condition:
            raise AssertionError(message)

    folder = Path(__file__).resolve().parent
    with TemporaryDirectory() as temporary:
        path = Path(temporary) / "ledger.sqlite"
        connection = connect(path)
        try:
            connection.executescript(
                (folder / "schema.sql").read_text(encoding="utf-8")
            )
            connection.executescript(
                (folder / "reconcile.sql").read_text(encoding="utf-8")
            )
            connection.execute(
                "INSERT INTO stock(sku, available, unit_cost) "
                "VALUES ('DEMO-SKU', 1, 3750)"
            )
        finally:
            connection.close()

        record(path, "opening-inventory", None, "inventory", "equity", 3750)

        with ThreadPoolExecutor(max_workers=8) as pool:
            ids = list(pool.map(
                lambda unused: intake(
                    path, "store-a:1001", "DEMO-SKU", 1, 10000
                ),
                range(16),
            ))
        check(len(set(ids)) == 1, "Duplicate intake created extra orders")
        order_id = ids[0]

        try:
            intake(path, "store-a:1001", "DEMO-SKU", 1, 11000)
        except ValueError:
            pass
        else:
            raise AssertionError("Changed order payload was accepted")

        try:
            intake(path, "store-a:1002", "DEMO-SKU", 1, 10000)
        except ValueError:
            pass
        else:
            raise AssertionError("Unavailable stock was sold")

        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(
                lambda unused: verify(path, order_id, "capture-1001", 10000),
                range(16),
            ))

        def send(body, idempotency_key):
            check(json.loads(body)["qty"] == 1, "Shipment quantity changed")
            return "receipt:" + idempotency_key

        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(
                lambda unused: dispatch_one(path, send), range(16)
            ))
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(
                lambda unused: deliver(path, order_id), range(16)
            ))
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(
                lambda unused: refund(path, order_id, "refund-1001", 500),
                range(16),
            ))

        record(path, "fee-1001", order_id, "fees", "processor", 300)
        record(path, "payout-1001", order_id, "cash", "processor", 9200)
        connection = connect(path)
        try:
            row = connection.execute(
                "SELECT net_sales_cents, processor_balance_cents, "
                "deferred_balance_cents, bank_cash_cents "
                "FROM order_reconciliation WHERE order_id = ?",
                (order_id,),
            ).fetchone()
            check(row == (9500, 0, 0, 9200), "Order cash bridge failed")
            check(
                connection.execute(
                    "SELECT available FROM stock WHERE sku = 'DEMO-SKU'"
                ).fetchone()[0] == 0,
                "Reservation count changed under repeated intake",
            )
            check(
                connection.execute(
                    "SELECT COUNT(*) FROM orders"
                ).fetchone()[0] == 1,
                "Rejected orders left durable records",
            )
            check(
                connection.execute(
                    "SELECT COUNT(*) FROM outbox WHERE status = 'done'"
                ).fetchone()[0] == 1,
                "Shipment acknowledgment count is incorrect",
            )
            check(
                connection.execute(
                    "SELECT SUM(debit_balance_cents) FROM trial_balance"
                ).fetchone()[0] == 0,
                "Trial balance does not sum to zero",
            )
        finally:
            connection.close()

        result = score(
            10000000, 625000, 3750000, 750000, 1875000, 300000
        )
        check(result["net_sales"] == 9375000, "Base sales mismatch")
        check(result["contribution"] == 2700000, "Base contribution mismatch")
    print("Reference concurrency and ledger checks passed")


if __name__ == "__main__":
    run_checks()''',
                        "The supplied checks exercise repeated concurrent events and verify one reservation, one order, one shipment acknowledgment, and a cleared processor balance.",
                        "Execute locally before adaptation; these supplied checks have not been run here and do not exercise a live warehouse or payment provider.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Walk three acquisition cohorts from accepted orders to reconciled cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk models three identical monthly "
                    "acquisition cohorts, not a claim that a new store reaches "
                    "steady volume immediately. Each month starts with 5,000 qualified "
                    "visits and 1,050 submitted orders. Fifty fail pre-capture checks "
                    "for address, inventory, payment, or duplicate-order reasons, leaving "
                    "1,000 captured and delivered orders at $100 each. The model "
                    "assumes delivery and refund recognition occur within the acquisition "
                    "month. Fifty orders receive full $100 refunds and twenty-five "
                    "different orders receive $50 partial refunds, producing $6,250 "
                    "total refunds. There are 950 orders retaining some revenue, "
                    "including the twenty-five partially refunded orders, and $93,750 "
                    "net retail sales. Refunded products have zero recovery value "
                    "in this example, so product cost remains $37,500 for all "
                    "1,000 shipped units. No separate chargeback loss is assumed; "
                    "adding chargebacks requires reducing profit or offsetting another "
                    "documented cost. The fifty pre-capture scrubs create neither "
                    "sales nor processor receipts. Acquisition spending covers the "
                    "whole traffic cohort, including failed submissions and subsequent "
                    "refunds. These definitions prevent a common reporting error: "
                    "dividing advertising by only successful retained customers while "
                    "quietly removing the acquisition costs of everyone else."
                ),
                (
                    "Processor cash follows a different clock from revenue. After "
                    "$6,250 refunds and $3,000 processor expense, each cohort yields "
                    "$90,750 net settlement entitlement. Assume 80% reaches the bank "
                    "during its acquisition month and 20% reaches the bank the "
                    "following month. This is a stress assumption for settlement "
                    "timing, not a statement about any provider's standard schedule. "
                    "Current-month cash is therefore $72,600, with $18,150 carried "
                    "as a processor receivable. Nonprocessor cash spending is "
                    "$79,968.75 each month: $37,500 inventory replacement, $7,500 "
                    "fulfillment, $18,750 advertising, and $16,218.75 fixed overhead. "
                    "The first month consumes $7,368.75 cash despite earning "
                    "$10,781.25. Months two and three each receive $90,750 "
                    "because the prior cohort's deferred settlement joins current "
                    "receipts, producing $10,781.25 monthly operating cash. The "
                    "operator funds $90,000 before day one: $60,000 bank cash "
                    "and $30,000 opening inventory. Frequent replenishment keeps "
                    "inventory at $30,000 while monthly purchases equal recognized "
                    "product cost. This requires workable supplier lead times and "
                    "warehouse receiving capacity. If purchases must precede sales "
                    "by several months, increase working capital explicitly instead "
                    "of treating the opening inventory assumption as universal."
                ),
                (
                    "At day ninety, cumulative operating cash flow is $14,193.75, "
                    "and bank cash is $74,193.75 after adding the opening "
                    "$60,000. The balance sheet also holds $18,150 processor "
                    "receivable and $30,000 inventory. Together those assets equal "
                    "$122,343.75: the original $90,000 owner capital plus "
                    "$32,343.75 cumulative owner profit. There are no supplier "
                    "payables, debt, tax balances, or owner distributions in "
                    "this illustration. Fixed overhead contains the modeled staffing, "
                    "contractors, software, insurance, and administrative allocation; "
                    "those costs must not be deducted a second time. Twelve "
                    "identical operating months produce $1,125,000 recognized "
                    "retail revenue and $129,375 owner profit, matching the "
                    "Base scorecard exactly. The first-year cash result still "
                    "differs because the final cohort retains its $18,150 "
                    "receivable until the next month. Conservative remains "
                    "$250,000 revenue at 5%, or $12,500 profit, with "
                    "2 FT + 3 C; Scaled remains $2,000,000 at 18%, "
                    "or $360,000, with 3 FT + 4 C. Those are separate "
                    "annual scenarios, not interpolated outcomes from this cohort. "
                    "Compare actual weekly settlements, refunds, purchase commitments, "
                    "and acquisition costs against this bridge before increasing "
                    "the next cohort's budget."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort or reconciliation checkpoint",
                    "Traffic, scrubs, losses, and recognized retail sales",
                    "Cash timing, operating costs, and earned profit",
                    "Cumulative cash flow and balance-sheet evidence",
                ],
                "rows": [
                    [
                        "Month 1 cohort establishes the first settlement receivable",
                        "5,000 visits; 1,050 submissions; 50 pre-capture scrubs; 1,000 delivered orders; $6,250 refunds; $93,750 net sales.",
                        "$72,600 bank receipts; $79,968.75 nonprocessor spending; $16,218.75 fixed overhead included; $10,781.25 earned profit.",
                        "Operating cash flow totals negative $7,368.75; bank cash reaches $52,631.25; processor receivable equals $18,150.",
                    ],
                    [
                        "Month 2 cohort collects its predecessor's deferred settlement",
                        "Another 5,000 visits yield 1,000 delivered orders after 50 scrubs; identical refunds leave another $93,750 net sales.",
                        "$72,600 current receipts plus $18,150 prior receipts equal $90,750; nonprocessor spending remains $79,968.75.",
                        "Monthly cash flow equals $10,781.25; cumulative cash flow reaches $3,412.50; bank cash reaches $63,412.50.",
                    ],
                    [
                        "Month 3 cohort completes the ninety-day operating bridge",
                        "A third 1,000-order delivered cohort produces $93,750 net sales; cumulative refunds equal $18,750 across three cohorts.",
                        "$90,750 bank receipts less $79,968.75 spending produces $10,781.25 cash; cumulative earned profit equals $32,343.75.",
                        "Cumulative cash flow reaches $14,193.75; bank cash equals $74,193.75; month-three processor receivable remains $18,150.",
                    ],
                    [
                        "Monthly expense bridge includes every modeled operating category",
                        "$100,000 delivered gross sales minus $6,250 refunds equals $93,750 recognized retail revenue before operating expenses.",
                        "$37,500 goods; $7,500 fulfillment; $18,750 advertising; $3,000 processor fees; $16,218.75 overhead; total expense $82,968.75.",
                        "$93,750 revenue minus $82,968.75 expense equals $10,781.25 profit; processor fees are withheld rather than paid twice.",
                    ],
                    [
                        "Opening funding and closing assets reconcile owner capital",
                        "$90,000 opening owner capital purchases $30,000 inventory and leaves $60,000 available bank cash before acquisition begins.",
                        "Monthly replacement purchases equal consumed inventory cost; ending inventory remains $30,000 without supplier credit or debt.",
                        "$74,193.75 bank plus $18,150 receivable plus $30,000 inventory equals $90,000 capital plus $32,343.75 profit.",
                    ],
                    [
                        "Annual Base run rate matches the canonical scorecard",
                        "Twelve monthly cohorts recognize $1,125,000 retail revenue after $75,000 refunds against $1,200,000 delivered gross sales.",
                        "Annual expenses equal $995,625; annual owner profit equals $129,375; net margin equals exactly 11.5%.",
                        "With unchanged timing, first-year operating cash equals $111,225; the remaining $18,150 profit resides in processor receivables.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Operate the two adjacent plays without corrupting the retail model",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The mapped play ssl_ada_wcag_compliance_scanner_outbound belongs "
                    "beside storefront quality control, but its service revenue stays "
                    "outside the retail Base case. Run headless Axe-core checks "
                    "only on owned or authorized domains, supplement them with "
                    "keyboard and screen-reader testing, and preserve the tested "
                    "URL, template version, viewport, rule version, DOM location, "
                    "and reproducible failure. Public PACER filings can reveal "
                    "industry patterns; verify the actual docket and distinguish "
                    "an allegation from an adjudicated finding before describing "
                    "it to a merchant. Do not imply that a filing "
                    "predicts a particular merchant's liability. Title III's "
                    "42 U.S.C. 12182 is relevant, while website coverage "
                    "and remedies depend on applicable law and jurisdiction. "
                    "WCAG audit results are engineering evidence, not automatic "
                    "legal conclusions. Illustratively, forty authorized domain "
                    "reviews at 1.5 labor hours and $60 per hour cost "
                    "$3,600. Six remediation retainers at $900 generate $5,400; "
                    "after another $300 tooling allocation, that leaves $1,500 "
                    "before other overhead. The fallback is concrete HTML or "
                    "Liquid template repair, verified focus behavior, labeled "
                    "controls, and manual assistive-technology retesting. Never sell "
                    "a single JavaScript snippet as protection against lawsuits "
                    "or replace recorded code fixes with a decorative overlay."
                ),
                (
                    "The mapped play web2app_quiz_subscription_billing_bypass requires "
                    "equally careful revenue separation. Use a transparent web "
                    "quiz to explain an actual subscription offer and route "
                    "customers to external checkout only where current platform "
                    "rules, regional terms, and product category permit it. "
                    "An entitlement service should bind the successful purchase "
                    "to the correct customer account, process refunds and "
                    "cancellations, and reconcile access state against verified "
                    "billing events. Do not grant access from an editable "
                    "return URL. Compare actual fees instead of assuming a "
                    "universal 30% saving: one hundred monthly subscribers at "
                    "$20 produce $2,000 before refunds. A hypothetical 15% "
                    "store charge costs $300; a hypothetical web processor "
                    "charge of 2.9% plus $0.30 per payment costs $88, "
                    "creating a $212 initial difference. Additional support "
                    "of $120 and $80 incremental churn cost leave only "
                    "$12 before any applicable platform charges or taxes. "
                    "Those assumptions require validation for the actual region "
                    "and agreement. Under 15 U.S.C. 8403, covered online "
                    "negative-option transactions require clear material terms, "
                    "express informed agreement before charging, and a simple "
                    "mechanism to stop recurring charges. The fallback is "
                    "approved in-app billing with simpler disclosures and "
                    "cancellation, not disguised links or concealed renewal terms."
                ),
                (
                    "Close the operating loop with weekly evidence reviews "
                    "rather than a larger dashboard collection. The merchandising "
                    "owner reviews supplier exceptions and SKU contribution; "
                    "the operations owner reviews stock reservations, warehouse "
                    "acceptance, delivery failures, and product complaints. "
                    "Contract specialists handle bookkeeping, creative production, "
                    "or technical remediation under explicit task boundaries. "
                    "For the Base team's 2 FT + 3 C, contractor "
                    "headcount does not imply three additional full-time salaries; "
                    "the actual hours and rates must fit the modeled "
                    "overhead and other expense categories. Retention automation "
                    "should follow verified fulfillment, product suitability, "
                    "customer preferences, and observed purchase intervals. "
                    "Suppress review requests after unresolved damage claims, "
                    "stop replenishment reminders for recalled lots, and "
                    "separate transactional shipping messages from promotional "
                    "campaigns. Track refund-adjusted contribution by acquisition "
                    "month before crediting retention with an economic lift. "
                    "Applicable privacy rules depend on jurisdiction, covered "
                    "data, and statutory thresholds; collect only operationally "
                    "necessary fields and restrict access by role. If "
                    "advertising prices rise 20% while volume stays fixed, "
                    "the monthly $18,750 allowance becomes $22,500 and "
                    "profit falls $3,750 to $7,031.25. Respond with "
                    "offer repair, channel changes, or lower spend rather "
                    "than editing the scorecard. Automation earns expansion "
                    "only when exceptions remain visible and cash reconciles."
                ),
            ],
            "table": {
                "caption": "Adjacent-Play Economics and Retail Exception Fallbacks",
                "headers": [
                    "Play or operating risk under review",
                    "Concrete unit economics and measurement boundary",
                    "Evidence required before automated execution",
                    "Fallback that preserves customer and ledger integrity",
                ],
                "rows": [
                    [
                        "ssl_ada_wcag_compliance_scanner_outbound connects authorized audits with code remediation",
                        "Forty reviews cost $3,600 labor; six $900 retainers less $300 tooling leave $1,500 before remaining overhead.",
                        "Retain domain authorization, reproducible DOM findings, manual tests, and accurately characterized public court records.",
                        "Deliver verified HTML or Liquid repairs; never represent snippets or automated scans as lawsuit prevention.",
                    ],
                    [
                        "web2app_quiz_subscription_billing_bypass compares permitted checkout routes by actual region",
                        "$2,000 monthly subscriptions yield a hypothetical $212 fee difference; $200 support and churn costs leave $12.",
                        "Verify current regional platform terms, authenticated billing events, subscription disclosures, and matching customer entitlements.",
                        "Use approved in-app billing where required and simplify renewal communication, cancellation, and refund-driven access changes.",
                    ],
                    [
                        "Advertising inflation compresses contribution before overhead can adjust",
                        "A 20% increase on $18,750 advertising adds $3,750 expense and reduces monthly profit to $7,031.25.",
                        "Reconcile channel invoices with cohort orders and refund-adjusted contribution before accepting attributed dashboard returns.",
                        "Reduce acquisition exposure, improve offers, and protect cash rather than assuming future repeat purchases recover losses.",
                    ],
                    [
                        "Inventory shortages create customer promises without executable warehouse capacity",
                        "Thirty daily units across twenty lead-time days plus ten buffer days require a 900-unit reorder point.",
                        "Compare usable units, committed reservations, confirmed inbound receipts, and supplier performance before publishing availability.",
                        "Pause affected campaigns and apply documented shipping-delay options instead of silently extending delivery promises.",
                    ],
                    [
                        "Product complaints require lot-level containment and reporting assessment",
                        "One affected lot can expose every associated order; reserve replacement and refund capacity before restarting sales.",
                        "Link complaint details, lot identifiers, supplier evidence, incident timing, and applicable reporting criteria for review.",
                        "Quarantine stock, preserve customer traceability, assess statutory reporting duties, and stop inappropriate retention messages.",
                    ],
                    [
                        "Retention automation can overstate value when refunds remain unresolved",
                        "Measure repeat-order contribution after goods, fulfillment, advertising, fees, and refunds rather than counting message-attributed gross sales.",
                        "Use verified fulfillment, customer preferences, product suitability, and resolved support cases before triggering promotional journeys.",
                        "Suppress unsuitable campaigns, honor applicable opt-outs, and keep transactional shipment communications separate from promotional sequences.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four practices that keep automation economically honest",
                "body": (
                    "Experienced operators shorten the evidence path between a "
                    "customer event, a physical action, and a reconciled ledger entry."
                ),
                "items": [
                    "Reserve merchant-qualified order keys permanently; provider retries must reuse the original immutable payload and key rather than generate a fresh shipment request.",
                    "Audit refunded cohorts using original advertising spend; removing failed customers from the denominator must never remove their acquisition costs.",
                    "Maintain separate service and subscription ledgers for the two adjacent plays so their illustrative margins cannot inflate canonical retail owner profit.",
                    "Keep a timed settlement bridge beside the contribution report; the Base walk earns $32,343.75 in ninety days but generates only $14,193.75 operating cash.",
                ],
            },
        },
    ],
    "pull_quote": "An automated store is controlled only when every promised unit, posted dollar, and bank deposit can be traced to the same durable evidence.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Assemble one authorized-dealer SKU packet with landed cost, channel permissions, product evidence, receiving records, and a documented shipping promise.",
        "Save the six reference modules, run their local concurrency checks, and add authenticated provider adapters before connecting customer traffic.",
        "Test repeated captures, duplicate routing attempts, early delivery events, refunds, and processor payouts against persistent order and operation keys.",
        "Reproduce the $93,750 monthly Base revenue, $82,968.75 expense, and $10,781.25 profit bridge without counting processor settlements as additional sales.",
        "Fund and monitor the opening $60,000 cash plus $30,000 inventory assumption, replacing it with actual supplier lead-time and settlement requirements.",
        "Keep accessibility-service and subscription-play economics separate while documenting lawful outreach, permitted billing routes, customer disclosures, and measurable fallback actions.",
    ],
    "statutory_citations": [
        {
            "title": "16 CFR 435.2 — Mail, Internet, or Telephone Order Merchandise Rule",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435/section-435.2",
            "relevance": "Supports substantiated shipping representations, prescribed delay handling, customer cancellation options, and timely refund procedures.",
        },
        {
            "title": "15 U.S.C. 2064(b) — Consumer product hazard reporting",
            "url": "https://www.law.cornell.edu/uscode/text/15/2064",
            "relevance": "Connects manufacturer, distributor, and retailer reporting duties to qualifying information about consumer product defects, hazards, and statutory nonconformity.",
        },
        {
            "title": "19 U.S.C. 1484 — Entry of merchandise",
            "url": "https://www.law.cornell.edu/uscode/text/19/1484",
            "relevance": "Anchors importer-of-record entry responsibilities and reasonable-care duties affecting product classification, value, and import documentation.",
        },
        {
            "title": "42 U.S.C. 12182 — Prohibition of discrimination by public accommodations",
            "url": "https://www.law.cornell.edu/uscode/text/42/12182",
            "relevance": "Provides the Title III statutory reference for accessibility analysis while requiring attention to applicable jurisdiction and the distinction between engineering findings and legal conclusions.",
        },
        {
            "title": "15 U.S.C. 8403 — Negative option marketing on the Internet",
            "url": "https://www.law.cornell.edu/uscode/text/15/8403",
            "relevance": "Requires clear material disclosures, express informed agreement before covered recurring charges, and simple mechanisms to stop those charges.",
        },
        {
            "title": "15 U.S.C. 45 — Unfair methods of competition and unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Supports accurate product claims, truthful subscription offers, and evidence-based descriptions of accessibility remediation rather than unsupported protective promises.",
        },
    ],
}
