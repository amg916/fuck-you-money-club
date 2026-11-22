from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "freight-brokerage-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute freight brokerage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "FMCSA Authority, Highway/RMIS Carrier Verification, SQLite Posting Controls, Customs Evidence Custody & Shipper-to-Carrier Working Capital",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #12, Freight Brokerage, ranks #19 with a 85/100 Money-to-Manpower "
        "Score: this is a high-leverage, system-disciplined operating business. Eight mapped "
        "plays connect niche acquisition, shipper credit, carrier identity, load matching, "
        "shipment tracking, invoice reconciliation, float management, and customs first-sale "
        "coordination. This chapter turns those plays into a controlled shipment lifecycle, "
        "a six-module SQLite reference implementation, and a worked 90-day cash cohort. "
        "Canonical annual owner profits are $30,000 Conservative, $165,000 Base, and "
        "$400,000 Scaled, measured against gross shipper billings that include carrier "
        "costs. The Base walk produces $750,000 quarterly billings and $41,250 profit, "
        "while exposing the $145,000 receivables-minus-payables investment. Customs savings "
        "remain importer benefits, never invented brokerage revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$1,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "3% net margin; $30,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$3,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "5.5% net margin; $165,000 annual owner net profit; 3 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$5,000,000",
            "context": "Annual gross shipper billings including carrier costs",
            "note": "8% net margin; $400,000 annual owner net profit; 4 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Turn eight mapped plays into one controlled shipment lifecycle",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a narrow service promise: scheduled dry-van replenishment between "
                    "two distribution clusters, with named pickup windows, equipment requirements, "
                    "and exception ownership. Candidate #12 ranks #19 because attractive billings "
                    "conceal purchased transportation, labor, and working capital. The canonical "
                    "Base operation has three full-time staff and two contractors, not an "
                    "unattended matching bot. Assign commercial intake and credit to one employee, "
                    "carrier procurement and dispatch to another, and tracking plus accounting "
                    "coordination to the third; contractors provide defined coverage and bookkeeping "
                    "capacity. The owner must have an explicit place in that staffing budget. "
                    "Map eight plays across this workflow: niche acquisition, shipper credit, "
                    "carrier identity defense, load matching, shipment tracking, invoice reconciliation, "
                    "float management, and customs first-sale coordination. These are chapter-level "
                    "operating mappings, not seven invented catalog identifiers accompanying the one "
                    "supplied identifier. Each play requires a measurable unit, an accountable "
                    "operator, and a fallback that preserves service without surrendering payment "
                    "controls. A signed tender becomes work only after credit exposure, carrier "
                    "identity, and capacity are checked; a sales conversation alone creates neither "
                    "a shipment nor recognized revenue."
                ),
                (
                    "Establish active FMCSA property-broker authority, process-agent designation, and "
                    "the required $75,000 BMC-84 surety bond or BMC-85 trust arrangement before "
                    "arranging covered transportation. Apply 49 U.S.C. § 13904, § 13906, "
                    "49 CFR § 387.307, and Part 366 to the actual entity that signs contracts. "
                    "The security amount is not automatically a $75,000 cash expense: a bond "
                    "has underwriting, premiums, and possible collateral; a trust has its own "
                    "funding requirements. Review current FMCSA implementation requirements rather "
                    "than relying on an old onboarding checklist. Verify carriers through FMCSA "
                    "Licensing and Insurance and SAFER, then use Highway or RMIS as additional "
                    "identity and document-workflow evidence. A vendor badge does not establish "
                    "coverage for the particular commodity or defeat identity theft. Independently "
                    "confirm dispatch contact and payment instructions using previously validated "
                    "channels. Bind the authorized carrier, driver, tractor, trailer, and pickup "
                    "reference to the shipment record before release. When a last-minute substitute "
                    "appears, stop the release instruction, call the validated carrier, and "
                    "rebook verified capacity if necessary. The commercial penalty for a missed "
                    "pickup is usually smaller than the combined cargo and duplicate-payment exposure."
                ),
                (
                    "The required customs_first_sale_rule_valuation_arbitrage mapping belongs at the "
                    "importer's customs workstream, not inside domestic freight revenue recognition. "
                    "Under 19 U.S.C. § 1401a, 19 CFR § 152.103, and the "
                    "Nissho Iwai framework, an earlier sale needs substantiated transaction-value "
                    "eligibility, including a bona fide sale for export to the United States. "
                    "At an illustrative 25% ad valorem rate, one million units valued at "
                    "$18 produce $4.5 million duty; an eligible $8 value produces $2 million, "
                    "saving $2.5 million, or 55.56%, before required valuation adjustments. "
                    "That example does not establish a universal 35–55% saving: assists, royalties, "
                    "related-party issues, product-specific duties, and inadequate destination evidence "
                    "can change or eliminate the result. For merchandise programs spanning "
                    "$10 million to $250 million, model entry-level eligibility before aggregation. "
                    "Use a confidential, encrypted customs-broker evidence vault to protect factory "
                    "invoices from casual commercial disclosure while preserving required importer "
                    "record access and lawful CBP access. Obtain a written customs-counsel analysis; "
                    "it supports decisions but does not bind CBP. If evidence fails, retain the "
                    "supportable valuation and separate any agreed coordination fee from duty savings."
                ),
            ],
            "table": {
                "caption": "Eight Mapped Freight Brokerage Plays: Units, Controls, and Failure Fallbacks",
                "headers": [
                    "Mapped operating play and accountable owner",
                    "Concrete unit economics or operating measure",
                    "Evidence required before the next action",
                    "Fallback when the control fails",
                ],
                "rows": [
                    [
                        "Niche acquisition owned by the commercial intake employee",
                        "Forty monthly opportunities yield twenty completed shipments after screening",
                        "Capture lane, equipment, commodity, appointment, and buyer authority",
                        "Decline unsuitable freight rather than buying unfamiliar execution risk",
                    ],
                    [
                        "Shipper credit owned by the commercial intake employee",
                        "Twenty invoices at $12,500 create $250,000 monthly receivables",
                        "Aggregate billed balances and committed tenders against approved exposure",
                        "Require prepayment or reduce accepted volume before dispatch",
                    ],
                    [
                        "Carrier identity defense owned by the procurement employee",
                        "One $10,500 diverted payment consumes 5.25 load contributions",
                        "Match authority, validated contacts, equipment, insurance, and remittance beneficiary",
                        "Suspend release and procure independently verified replacement capacity",
                    ],
                    [
                        "Load matching owned by the carrier procurement employee",
                        "$12,500 shipper price less $10,500 carrier cost leaves $2,000",
                        "Use DAT or Truckstop benchmarks alongside signed carrier acceptance",
                        "Reprice before acceptance or reject uneconomic service commitments",
                    ],
                    [
                        "Shipment tracking owned by the tracking coordination employee",
                        "Twenty monthly shipments require documented pickup and delivery milestones",
                        "Use project44 or FourKites events with driver contact corroboration",
                        "Switch to scheduled calls when automated location evidence disappears",
                    ],
                    [
                        "Invoice reconciliation owned by the accounting coordination employee",
                        "Twenty matched invoice packets support $250,000 monthly shipper billings",
                        "Match tender, carrier confirmation, delivery proof, and accessorial authorization",
                        "Hold disputed invoice components without duplicating the shipment record",
                    ],
                    [
                        "Float management owned by the designated treasury operator",
                        "$250,000 receivables less $105,000 payables ties up $145,000",
                        "Maintain dated collection forecasts and carrier payment maturity schedules",
                        "Slow bookings or use pre-agreed funding before cash exhaustion",
                    ],
                    [
                        "customs_first_sale_rule_valuation_arbitrage coordinated with importer counsel and customs broker",
                        "One million units at 25% illustrate $2.5 million savings",
                        "Preserve qualifying sale, destination, adjustments, and confidential invoice evidence",
                        "Use supportable valuation when eligibility cannot be adequately documented",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the load contribution before chasing another tender",
                "body": "Use practical controls that catch expensive exceptions before freight or money moves.",
                "items": [
                    "Call the carrier through an independently validated number when a dispatcher changes pickup identity or remittance instructions; never validate the change through the incoming message alone.",
                    "Save the rate benchmark and exact equipment assumptions when quoting; a refrigerated or team-driver substitution can erase an otherwise attractive dry-van spread.",
                    "Record detention start, appointment time, and authorization contact while the truck waits; a retrospective accessorial claim is much harder to collect.",
                    "Ask the shipper which invoice fields their payment system rejects before the first load; correct purchase-order formatting often improves cash timing more than another reminder email.",
                ],
            },
        },
        {
            "heading": "2. Implement six ledger modules with serialized, idempotent state changes",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat the following six modules as a sequential, copy-pasteable SQLite "
                    "reference, executed in one Python process with a local database file. "
                    "Module one opens a connection in explicit transaction mode; every business "
                    "mutation subsequently uses BEGIN IMMEDIATE before reading mutable balances "
                    "or states. SQLite therefore serializes competing writers, including separate "
                    "connections to that same local database. Unique shipment sources prevent "
                    "duplicate intake, while immutable request bodies distinguish legitimate retries "
                    "from conflicting reuse of an idempotency key. Balanced integer-cent postings "
                    "replace spreadsheet adjustments. The reference deliberately contains no bank "
                    "API calls, carrier booking calls, or message publication inside transactions. "
                    "Its race protection covers local ledger operations, not an impossible promise "
                    "of exactly-once execution across unrelated external systems. Keep the database "
                    "on supported local storage, assign one connection per worker, and retry a "
                    "busy transaction using the identical request key. Do not share the connection "
                    "concurrently between threads or move the file onto a network share. For "
                    "Postgres, preserve the request-key constraint and lock the shipment row before "
                    "checking exposure or applying cash; changing databases without preserving "
                    "those semantics would reintroduce duplicate payments and overcollection races."
                ),
                (
                    "Module two scores intake deterministically and records only qualified shipments. "
                    "The score is an operational margin screen, not the candidate's 85/100 "
                    "portfolio score. An illustrative $12,500 bill and $10,500 carrier commitment "
                    "produce a sixteen-percent purchased-transportation spread and pass the threshold. "
                    "Module three progresses qualified, verified, reserved, dispatched, delivered, "
                    "billed, and settled states with evidence references attached to the event. "
                    "Verification requires authority, identity, insurance, and credit evidence; reserve "
                    "requires capacity and liquidity evidence. These references must resolve to "
                    "reviewed artifacts in the deployed application. A string alone cannot verify "
                    "an insurance policy. Customs escrow means document custody here, not an "
                    "unlicensed movement of customer money, and its evidence remains outside the "
                    "freight state machine unless the shipment actually requires customs coordination. "
                    "Billing posts receivables and gross shipper revenue, plus carrier expense "
                    "and payable, in the same transaction as the state change. This deliberately "
                    "simplified model bills immediately after delivery and fixes accepted prices. "
                    "A deployed system needs separately controlled credit notes, accessorial changes, "
                    "disputes, and delivery-period accruals; never edit historical postings to "
                    "pretend those events did not happen."
                ),
                (
                    "Module four records confirmed collections, carrier payments, and operating "
                    "expenses; it does not initiate transfers. Use a bank transaction identifier "
                    "as the request key, not a random identifier generated on every retry. "
                    "The shipment lock implied by the writer transaction makes balance checks "
                    "and postings indivisible: two callers cannot both spend the same remaining "
                    "payable. Module five exposes shipment balances and aggregate profit without "
                    "counting collections as new revenue. Module six runs assertions against "
                    "an isolated in-memory fixture, verifies retry behavior, rejects excessive "
                    "collections, and checks settlement and ledger balance. Those checks are "
                    "provided as executable reference tests, not represented as already executed. "
                    "The implementation omits authentication, authorization, backups, and external "
                    "delivery adapters; supply those before operational deployment. Restrict direct "
                    "database access because application-level posting invariants assume writers use "
                    "these functions. External dispatch should use an outbox plus the provider's "
                    "idempotency facility; ambiguous bank responses require statement lookup before "
                    "any resend. Preserve shipment evidence under 49 CFR § 371.3 and "
                    "apply separate retention rules to customs records. The practical architecture "
                    "is a small deterministic accounting core surrounded by explicitly fallible "
                    "integrations, rather than an automation that silently treats every webhook "
                    "as both authentic and economically final."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Sequential module and concrete operating responsibility",
                    "Copy-pasteable Python reference implementation",
                    "Concurrency boundary and required deployment control",
                ],
                "rows": [
                    [
                        "Module one establishes schema and the serialized transaction boundary",
                        '''import json
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS shipments (
    shipment_id TEXT PRIMARY KEY,
    source_key TEXT NOT NULL UNIQUE,
    bill_cents INTEGER NOT NULL CHECK (bill_cents > 0),
    carrier_cents INTEGER NOT NULL
        CHECK (carrier_cents > 0 AND carrier_cents <= bill_cents),
    score INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    state TEXT NOT NULL CHECK (state IN (
        'qualified', 'verified', 'reserved', 'dispatched',
        'delivered', 'billed', 'settled'
    ))
);
CREATE TABLE IF NOT EXISTS events (
    request_key TEXT PRIMARY KEY,
    request_body TEXT NOT NULL,
    result_body TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS postings (
    posting_id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL REFERENCES events(request_key),
    shipment_id TEXT REFERENCES shipments(shipment_id),
    account TEXT NOT NULL CHECK (account IN (
        'AR', 'REVENUE', 'CARRIER_COST', 'AP', 'CASH', 'OPEX'
    )),
    cents INTEGER NOT NULL CHECK (
        typeof(cents) = 'integer' AND cents != 0
    ),
    UNIQUE (event_key, account)
);
CREATE TRIGGER IF NOT EXISTS postings_no_update
BEFORE UPDATE ON postings
BEGIN
    SELECT RAISE(ABORT, 'append only ledger');
END;
CREATE TRIGGER IF NOT EXISTS postings_no_delete
BEFORE DELETE ON postings
BEGIN
    SELECT RAISE(ABORT, 'append only ledger');
END;
"""
db = sqlite3.connect(
    "freight_ledger.sqlite3", isolation_level=None, timeout=30
)
db.execute("PRAGMA foreign_keys = ON")
db.execute("PRAGMA journal_mode = WAL")
db.execute("PRAGMA synchronous = FULL")
db.executescript(SCHEMA)

def require_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("nonempty text required")
    return value

def require_cents(value):
    if type(value) is not int or value <= 0:
        raise ValueError("positive integer cents required")
    return value

def atomic(request_key, payload, operation):
    require_text(request_key)
    body = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    db.execute("BEGIN IMMEDIATE")
    try:
        old = db.execute(
            "SELECT request_body, result_body FROM events "
            "WHERE request_key = ?", (request_key,)
        ).fetchone()
        if old is not None:
            if old[0] != body:
                raise ValueError("request key reused with different content")
            result = json.loads(old[1])
        else:
            db.execute(
                "INSERT INTO events VALUES (?, ?, ?)",
                (request_key, body, "{}")
            )
            result = operation()
            db.execute(
                "UPDATE events SET result_body = ? WHERE request_key = ?",
                (json.dumps(result, sort_keys=True), request_key)
            )
        db.execute("COMMIT")
        return result
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise

def post(event_key, shipment_id, lines):
    if not db.in_transaction:
        raise RuntimeError("posting requires an active transaction")
    if len(lines) < 2 or sum(value for _, value in lines) != 0:
        raise ValueError("journal must balance")
    if len({account for account, _ in lines}) != len(lines):
        raise ValueError("aggregate repeated accounts before posting")
    if any(type(value) is not int or value == 0 for _, value in lines):
        raise ValueError("nonzero integer postings required")
    db.executemany(
        "INSERT INTO postings "
        "(event_key, shipment_id, account, cents) VALUES (?, ?, ?, ?)",
        [(event_key, shipment_id, account, value)
         for account, value in lines]
    )

def balance(shipment_id, account):
    return db.execute(
        "SELECT COALESCE(SUM(cents), 0) FROM postings "
        "WHERE shipment_id = ? AND account = ?",
        (shipment_id, account)
    ).fetchone()[0]
''',
                        "All business writers must enter atomic before inspecting mutable state; local file access remains restricted.",
                    ],
                    [
                        "Module two accepts qualified intake using stable source identifiers",
                        '''def intake(request_key, shipment_id, source_key, bill, carrier):
    require_text(shipment_id)
    require_text(source_key)
    require_cents(bill)
    require_cents(carrier)
    if carrier > bill:
        raise ValueError("carrier commitment exceeds shipper bill")
    score = min(100, ((bill - carrier) * 1000) // bill)
    if score < 80:
        raise ValueError("spread below eight percent intake threshold")
    payload = {
        "op": "intake", "shipment": shipment_id,
        "source": source_key, "bill": bill, "carrier": carrier
    }

    def operation():
        old = db.execute(
            "SELECT shipment_id, bill_cents, carrier_cents "
            "FROM shipments WHERE source_key = ?", (source_key,)
        ).fetchone()
        if old is not None:
            if old != (shipment_id, bill, carrier):
                raise ValueError("source already has different shipment terms")
            return {"shipment_id": shipment_id, "score": score}
        db.execute(
            "INSERT INTO shipments VALUES (?, ?, ?, ?, ?, ?)",
            (shipment_id, source_key, bill, carrier, score, "qualified")
        )
        return {"shipment_id": shipment_id, "score": score}

    return atomic(request_key, payload, operation)
''',
                        "Unique source keys and serialized inspection prevent simultaneous duplicate intake; accepted prices remain immutable.",
                    ],
                    [
                        "Module three verifies evidence and advances the shipment state",
                        '''NEXT = {
    "qualified": "verified", "verified": "reserved",
    "reserved": "dispatched", "dispatched": "delivered",
    "delivered": "billed", "billed": "settled"
}
REQUIRED = {
    "verified": ("authority", "carrier_identity", "insurance", "shipper_credit"),
    "reserved": ("capacity", "liquidity"),
    "dispatched": ("driver_equipment", "pickup_release"),
    "delivered": ("delivery_proof",),
    "billed": ("invoice_packet",),
    "settled": ("bank_match",)
}

def advance(request_key, shipment_id, target, evidence):
    require_text(shipment_id)
    if target not in REQUIRED or not isinstance(evidence, dict):
        raise ValueError("valid target and evidence mapping required")
    if any(not isinstance(k, str) or not isinstance(v, str)
           for k, v in evidence.items()):
        raise ValueError("evidence references must be text")
    if any(not evidence.get(name, "").strip() for name in REQUIRED[target]):
        raise ValueError("required evidence reference missing")
    payload = {
        "op": "advance", "shipment": shipment_id,
        "target": target, "evidence": evidence
    }

    def operation():
        row = db.execute(
            "SELECT state, bill_cents, carrier_cents FROM shipments "
            "WHERE shipment_id = ?", (shipment_id,)
        ).fetchone()
        if row is None or NEXT.get(row[0]) != target:
            raise ValueError("invalid shipment transition")
        if target == "settled":
            if balance(shipment_id, "AR") or balance(shipment_id, "AP"):
                raise ValueError("open receivable or payable remains")
        if target == "billed":
            bill, carrier = row[1], row[2]
            post(request_key, shipment_id, [
                ("AR", bill), ("REVENUE", -bill),
                ("CARRIER_COST", carrier), ("AP", -carrier)
            ])
        db.execute(
            "UPDATE shipments SET state = ? WHERE shipment_id = ?",
            (target, shipment_id)
        )
        return {"shipment_id": shipment_id, "state": target}

    return atomic(request_key, payload, operation)
''',
                        "Evidence review occurs in the authorized application; state validation and billing postings commit together atomically.",
                    ],
                    [
                        "Module four applies bank-confirmed cash without duplicate economic effects",
                        '''def apply_cash(request_key, shipment_id, kind, amount):
    require_cents(amount)
    if kind not in ("collection", "carrier_payment", "expense"):
        raise ValueError("unsupported cash operation")
    if kind == "expense":
        if shipment_id is not None:
            raise ValueError("operating expense uses no shipment identifier")
    else:
        require_text(shipment_id)
    payload = {
        "op": "cash", "shipment": shipment_id,
        "kind": kind, "amount": amount
    }

    def operation():
        if kind == "expense":
            lines = [("OPEX", amount), ("CASH", -amount)]
        else:
            row = db.execute(
                "SELECT state FROM shipments WHERE shipment_id = ?",
                (shipment_id,)
            ).fetchone()
            if row is None or row[0] != "billed":
                raise ValueError("cash requires an open billed shipment")
            if kind == "collection":
                if amount > balance(shipment_id, "AR"):
                    raise ValueError("collection exceeds open receivable")
                lines = [("CASH", amount), ("AR", -amount)]
            else:
                if amount > -balance(shipment_id, "AP"):
                    raise ValueError("payment exceeds open carrier payable")
                lines = [("AP", amount), ("CASH", -amount)]
        post(request_key, shipment_id, lines)
        return {"shipment_id": shipment_id, "kind": kind, "cents": amount}

    return atomic(request_key, payload, operation)
''',
                        "Use stable bank transaction keys; this function records confirmed movement and never sends a transfer.",
                    ],
                    [
                        "Module five separates recognized billings from cash and liabilities",
                        '''VIEWS = """
CREATE VIEW IF NOT EXISTS shipment_reconciliation AS
SELECT
    s.shipment_id,
    s.state,
    COALESCE(SUM(CASE WHEN p.account = 'AR'
        THEN p.cents ELSE 0 END), 0) AS receivable_cents,
    -COALESCE(SUM(CASE WHEN p.account = 'AP'
        THEN p.cents ELSE 0 END), 0) AS payable_cents,
    -COALESCE(SUM(CASE WHEN p.account = 'REVENUE'
        THEN p.cents ELSE 0 END), 0) AS billed_cents,
    COALESCE(SUM(CASE WHEN p.account = 'CARRIER_COST'
        THEN p.cents ELSE 0 END), 0) AS carrier_cost_cents
FROM shipments s
LEFT JOIN postings p ON p.shipment_id = s.shipment_id
GROUP BY s.shipment_id, s.state;

CREATE VIEW IF NOT EXISTS ledger_summary AS
SELECT
    COALESCE(SUM(CASE WHEN account = 'CASH'
        THEN cents ELSE 0 END), 0) AS operating_cash_change_cents,
    -COALESCE(SUM(CASE WHEN account = 'REVENUE'
        THEN cents ELSE 0 END), 0) AS gross_billings_cents,
    COALESCE(SUM(CASE WHEN account = 'CARRIER_COST'
        THEN cents ELSE 0 END), 0) AS carrier_cost_cents,
    COALESCE(SUM(CASE WHEN account = 'OPEX'
        THEN cents ELSE 0 END), 0) AS operating_expense_cents,
    -COALESCE(SUM(CASE WHEN account IN
        ('REVENUE', 'CARRIER_COST', 'OPEX')
        THEN cents ELSE 0 END), 0) AS owner_profit_cents
FROM postings;
"""
db.executescript(VIEWS)
''',
                        "Cash change excludes opening capital; gross billings include purchased transportation under the canonical scenario presentation.",
                    ],
                    [
                        "Module six exercises retry, balance, settlement, and rollback invariants",
                        '''def assert_ledger_clean():
    assert db.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []
    assert db.execute(
        "SELECT event_key FROM postings GROUP BY event_key "
        "HAVING SUM(cents) != 0"
    ).fetchall() == []
    assert db.execute(
        "SELECT shipment_id FROM shipment_reconciliation "
        "WHERE receivable_cents < 0 OR payable_cents < 0 "
        "OR (state = 'settled' AND "
        "(receivable_cents != 0 OR payable_cents != 0))"
    ).fetchall() == []

def reference_tests():
    global db
    production_db = db
    db = sqlite3.connect(":memory:", isolation_level=None)
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.executescript(SCHEMA)
        db.executescript(VIEWS)
        first = intake("i1", "load-1", "tender-1", 1250000, 1050000)
        assert intake("i1", "load-1", "tender-1", 1250000, 1050000) == first
        try:
            intake("i1", "load-1", "tender-1", 1260000, 1050000)
        except ValueError:
            pass
        else:
            raise AssertionError("conflicting retry accepted")
        for target in (
            "verified", "reserved", "dispatched", "delivered", "billed"
        ):
            evidence = {name: "fixture-reviewed" for name in REQUIRED[target]}
            advance("state-" + target, "load-1", target, evidence)
        before = db.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        try:
            apply_cash("too-large", "load-1", "collection", 1250001)
        except ValueError:
            pass
        else:
            raise AssertionError("excess collection accepted")
        assert db.execute("SELECT COUNT(*) FROM events").fetchone()[0] == before
        apply_cash("bank-in-1", "load-1", "collection", 1250000)
        apply_cash("bank-in-1", "load-1", "collection", 1250000)
        apply_cash("bank-out-1", "load-1", "carrier_payment", 1050000)
        apply_cash("bank-overhead-1", None, "expense", 10000)
        advance("close-1", "load-1", "settled", {"bank_match": "fixture-reviewed"})
        assert balance("load-1", "AR") == 0
        assert balance("load-1", "AP") == 0
        summary = db.execute(
            "SELECT operating_cash_change_cents, owner_profit_cents "
            "FROM ledger_summary"
        ).fetchone()
        assert summary == (190000, 190000)
        assert_ledger_clean()
    finally:
        db.close()
        db = production_db

# Run explicitly in a controlled development session:
# reference_tests()
''',
                        "Fixtures use an isolated database; add concurrent-connection and integration fault tests before operating with live funds.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Execute dispatch, evidence custody, billing, and exception recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Production work starts before the first API event. The intake owner "
                    "captures the shipper's legal entity, payment contact, purchase-order format, "
                    "commodity, declared value, origin, destination, appointment windows, and special "
                    "handling. The procurement owner confirms whether the proposed carrier's insurance "
                    "actually addresses the commodity, deductible, exclusions, and requested limit; "
                    "a certificate is evidence to investigate, not a promise that a future "
                    "claim will be paid. Record which employee reviewed each artifact and "
                    "when it expires. Before dispatch, compare the pickup driver's identity "
                    "and equipment against the carrier's validated instructions and the facility's "
                    "release process. Never email an unrestricted pickup reference to an "
                    "unverified replacement dispatcher. The tracking owner then watches pickup "
                    "confirmation, appointment changes, and delivery proof, escalating missed events "
                    "through a documented call tree. At delivery, collect legible proof, "
                    "count exceptions, temperature records where relevant, and signed accessorial "
                    "authorization. A clean packet should reach billing on the delivery day "
                    "in this model. Measure the hours from delivery to accepted invoice, "
                    "because every avoidable billing delay extends the cash bridge even when "
                    "the shipper technically pays within their agreed terms."
                ),
                (
                    "Separate three incidents that often become one vague accounting dispute. "
                    "Identity fraud means the accepted counterparty or payment beneficiary may "
                    "be false; a cargo claim means the goods suffered an alleged loss; "
                    "a billing dispute means the contracted amount or documentation is contested. "
                    "For suspected double brokering, freeze unconfirmed release or remittance "
                    "instructions, preserve messages and identity evidence, and contact the shipper "
                    "and verified carrier through independent channels. For cargo damage, preserve "
                    "delivery exceptions and insurer notification evidence while applying the actual "
                    "contracts and claim procedures. 49 U.S.C. § 14706 addresses carrier "
                    "liability for covered transportation; it does not make every broker a "
                    "carrier or settle contractual allocation automatically. For disputed accessorials, "
                    "segregate the challenged component and pursue the supported invoice amount. "
                    "Do not erase the original invoice or create a second shipment to "
                    "make collections look cleaner. Route corrections through an authorized reversal "
                    "and replacement journal in the deployed ledger. One $2,500 absorbed "
                    "claim consumes 1.25 standard $2,000 load contributions before overhead. "
                    "That sensitivity belongs in the risk review, not as an unrecorded "
                    "deduction hidden inside the canonical Base figures."
                ),
                (
                    "Close every day with three queues: shipments missing evidence, invoices "
                    "awaiting acceptance, and bank movements awaiting allocation. Assign a person "
                    "and next action to every item rather than counting raw webhook "
                    "volume as productivity. Match bank deposits to remittance details; where "
                    "one payment covers several invoices, use a controlled allocation batch "
                    "whose components total the deposit. The reference implementation deliberately "
                    "handles one shipment per collection event, so extend it before accepting "
                    "multi-invoice remittances or customer credits. Likewise, validate factoring "
                    "notices and beneficiary changes independently before changing a carrier payee. "
                    "The weekly treasury review combines committed but unbilled loads, open "
                    "receivables, scheduled carrier payments, payroll, and usable funding. A "
                    "$100,000 revolving facility is not $100,000 of available cash if "
                    "its borrowing base excludes disputed invoices. Model actual advance rates, "
                    "reserves, fees, and recourse. Keep permission to book freight separate "
                    "from permission to change payment details, even when one employee covers "
                    "both desks temporarily through documented review. Broker transaction records "
                    "under 49 CFR § 371.3 should explain who arranged the movement, "
                    "what was charged and paid, and how the retained evidence connects "
                    "the commercial agreement to the cash."
                ),
            ],
            "table": {
                "caption": "Dispatch-to-Cash Forensic Matrix and Exception Ownership",
                "headers": [
                    "Operating event and designated accountable desk",
                    "Minimum evidence preserved with the shipment",
                    "Specific failure signal requiring immediate investigation",
                    "Recovery action and economic consequence",
                ],
                "rows": [
                    [
                        "Pickup release reviewed by the carrier procurement desk",
                        "Validated carrier contact, driver identity, equipment, and facility release",
                        "Replacement dispatcher requests pickup details through an unverified address",
                        "Withhold release instructions and independently authenticate replacement capacity",
                    ],
                    [
                        "Shipment tracking reviewed by the shipment coordination desk",
                        "Pickup timestamp, location evidence, appointment updates, and escalation history",
                        "Tracking stops while driver contact and equipment details change",
                        "Call validated contacts and notify shipper of confirmed service exposure",
                    ],
                    [
                        "Delivery acceptance reviewed by the shipment coordination desk",
                        "Signed delivery proof, shortage notes, photographs, and relevant temperature records",
                        "Unsigned proof arrives with unexplained damage or quantity differences",
                        "Preserve evidence and notify responsible claims parties without deleting charges",
                    ],
                    [
                        "Invoice release reviewed by the designated billing operator",
                        "Tender terms, carrier confirmation, delivery proof, and authorized accessorial evidence",
                        "Shipper portal rejects purchase order or duplicate invoice identifier",
                        "Correct the packet and track delivery-to-acceptance delay separately",
                    ],
                    [
                        "Carrier remittance reviewed by the designated treasury operator",
                        "Accepted invoice, independent beneficiary confirmation, and authenticated assignment documents",
                        "Payment account changes immediately before the contractual payment date",
                        "Pause changed instructions while honoring verified obligations through reviewed channels",
                    ],
                    [
                        "Daily ledger close reviewed by the accounting coordination desk",
                        "Bank statement references, balanced postings, and unresolved allocation queue",
                        "Cash appears twice or receivables change without corresponding journals",
                        "Quarantine the event and investigate before releasing subsequent allocations",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before the first live shipment",
                "body": "Require evidence that the business can arrange, execute, finance, and reconcile the movement.",
                "items": [
                    "Verify active broker authority, required process-agent filing, and current bond or trust security for the contracting entity using official FMCSA records.",
                    "Authenticate the carrier's authority, identity, relevant insurance, dispatcher contact, and proposed pickup equipment before distributing release instructions.",
                    "Approve shipper exposure and a dated carrier-payment cash forecast that includes committed loads, payroll, and funding restrictions.",
                    "Exercise duplicate intake, conflicting request keys, interrupted transactions, and excess-payment rejection against a test database before connecting production adapters.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Qualify the tender and reserve exposure",
                    "action": "Capture shipment requirements, approve shipper credit, and lock accepted commercial terms.",
                    "detail": "Record the source tender identifier and include booked but unbilled commitments in the external credit-control calculation.",
                },
                {
                    "step": 2,
                    "title": "Verify capacity and execute the movement",
                    "action": "Authenticate carrier identity, confirm equipment, release pickup details, and monitor milestones.",
                    "detail": "Escalate substitutions through independently validated contacts and preserve each release decision with reviewer identity.",
                },
                {
                    "step": 3,
                    "title": "Match evidence and post the invoice",
                    "action": "Reconcile tender, rate confirmation, delivery proof, and authorized accessorials before billing.",
                    "detail": "Post receivable, gross revenue, purchased transportation, and carrier payable in one balanced transaction.",
                },
                {
                    "step": 4,
                    "title": "Allocate bank cash and close balances",
                    "action": "Apply confirmed collections and carrier payments using stable bank transaction identifiers.",
                    "detail": "Settle only after receivable and payable balances reach zero and unresolved operational claims remain separately visible.",
                },
            ],
        },
        {
            "heading": "4. Walk the 90-day cohort from qualified leads to reconciled cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The cohort begins after authority, staffing, shipper onboarding, and carrier "
                    "procurement are ready; it is an operating quarter, not a claim "
                    "that a cold start reaches maturity immediately. The stated first-deal "
                    "window remains two to six months. Each month produces forty screened "
                    "opportunities, thirty qualified opportunities, twenty-five quotes, and twenty-two "
                    "accepted tenders. Two accepted tenders are scrubbed before dispatch without "
                    "cancellation charges, leaving twenty completed shipments. Each completed shipment "
                    "bills $12,500 and costs $10,500 in purchased transportation. Monthly "
                    "gross shipper billings therefore equal $250,000, carrier cost equals "
                    "$210,000, and contribution before operating expenses equals $40,000. "
                    "Budget $26,250 monthly cash operating expenses: $17,500 payroll and "
                    "employment costs, $4,000 contractors, $1,500 systems and communications, "
                    "$1,250 insurance and authority-related costs, and $2,000 sales and "
                    "administration. These are illustrative budget allocations, not quoted vendor "
                    "prices. They produce $13,750 monthly owner profit, exactly 5.5% "
                    "of billings. This quarter assumes no realized cargo loss or credit "
                    "write-off; scrubbed opportunities create no revenue, carrier commitment, or "
                    "cash loss. Keep losses explicit rather than quietly declaring every "
                    "rejected lead an expense."
                ),
                (
                    "Use $250,000 opening unrestricted operating cash, separately from any "
                    "restricted trust or bond collateral. Assume every invoice generated in "
                    "a month is collected in the next month. Assume half of each "
                    "month's carrier charges is paid during that month and half during "
                    "the next month; this is a monthly cash-bucket convention, not a "
                    "claim that all individual invoices have identical payment terms. Operating "
                    "expenses are paid as incurred. Month one collects nothing, pays "
                    "$105,000 to carriers and $26,250 overhead, and closes with "
                    "$118,750 cash. Month two collects $250,000 from the first "
                    "cohort, pays $210,000 across the first and second carrier cohorts, "
                    "and pays $26,250 overhead, closing with $132,500. Month three "
                    "repeats those flows and closes with $146,250. Month-end balances "
                    "alone do not prove intramonth liquidity: schedule actual collection dates "
                    "against payroll and carrier maturities before accepting the cohort. If "
                    "receipts arrive after concentrated payment dates, stagger accepted loads, "
                    "negotiate supported terms, or arrange usable funding. The illustrative "
                    "opening cash also excludes prelaunch spending, so a business needing "
                    "the full reserve plus setup costs can exceed the stated startup range."
                ),
                (
                    "At day ninety, cumulative billings are $750,000, carrier expense "
                    "is $630,000, operating expense is $78,750, and owner profit "
                    "is $41,250. Collections total $500,000 and carrier cash payments "
                    "total $525,000; after overhead, cumulative operating cash flow is "
                    "negative $103,750. The reconciliation is exact: $41,250 profit "
                    "minus $250,000 ending receivables plus $105,000 ending payables "
                    "equals negative $103,750 cash flow. Opening cash plus that movement "
                    "equals $146,250, and ending cash plus receivables less payables "
                    "equals $291,250, or opening capital plus earned profit. Annualizing "
                    "the operating volume produces $3 million billings, $2.52 million "
                    "carrier costs, $315,000 overhead, and $165,000 owner profit, "
                    "matching the canonical Base case with three full-time staff and "
                    "two contractors. The Conservative case remains $1 million at 3%, "
                    "or $30,000 profit; Scaled remains $5 million at 8%, or "
                    "$400,000 with four full-time staff and three contractors. Those "
                    "cases require different productivity and cost structures, not mechanical "
                    "reuse of this Base budget. Finally, an extra month of collection "
                    "delay adds roughly $250,000 receivables at this throughput before "
                    "any offsetting terms changes, illustrating why profitable growth can still "
                    "exhaust operating cash."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort measure and explicit modeling convention",
                    "Month 1 operating cohort and cash outcome",
                    "Month 2 operating cohort and cash outcome",
                    "Month 3 operating cohort and cash outcome",
                ],
                "rows": [
                    [
                        "Lead funnel measured before accepted tender conversion",
                        "Forty opportunities, thirty qualified, twenty-five quotes, twenty-two accepted tenders",
                        "Forty opportunities, thirty qualified, twenty-five quotes, twenty-two accepted tenders",
                        "Forty opportunities, thirty qualified, twenty-five quotes, twenty-two accepted tenders",
                    ],
                    [
                        "Scrubs and realized losses kept outside invented revenue",
                        "Two pre-dispatch scrubs; twenty completions; zero realized loss dollars",
                        "Two pre-dispatch scrubs; twenty completions; zero realized loss dollars",
                        "Two pre-dispatch scrubs; twenty completions; zero realized loss dollars",
                    ],
                    [
                        "Gross shipper billings include purchased carrier transportation",
                        "Twenty completed shipments times $12,500 produce $250,000 billings",
                        "Twenty completed shipments times $12,500 produce $250,000 billings",
                        "Twenty completed shipments times $12,500 produce $250,000 billings",
                    ],
                    [
                        "Accrued carrier expense precedes the complete cash settlement",
                        "Twenty purchased movements times $10,500 produce $210,000 expense",
                        "Twenty purchased movements times $10,500 produce $210,000 expense",
                        "Twenty purchased movements times $10,500 produce $210,000 expense",
                    ],
                    [
                        "Operating expenses and earned owner profit reconcile monthly",
                        "$26,250 cash overhead leaves $13,750 earned owner profit",
                        "$26,250 cash overhead leaves $13,750 earned owner profit",
                        "$26,250 cash overhead leaves $13,750 earned owner profit",
                    ],
                    [
                        "Customer collections follow the preceding monthly invoice cohort",
                        "Zero collections because this walk starts without opening receivables",
                        "$250,000 collected from Month 1 accepted invoice packets",
                        "$250,000 collected from Month 2 accepted invoice packets",
                    ],
                    [
                        "Carrier cash payments combine current and preceding cohorts",
                        "$105,000 paid against Month 1 purchased carrier movements",
                        "$105,000 prior cohort plus $105,000 current cohort equals $210,000",
                        "$105,000 prior cohort plus $105,000 current cohort equals $210,000",
                    ],
                    [
                        "Monthly cash movement differs from earned accounting profit",
                        "Zero collections less $105,000 carriers less $26,250 overhead: -$131,250",
                        "$250,000 collections less $210,000 carriers less $26,250 overhead: +$13,750",
                        "$250,000 collections less $210,000 carriers less $26,250 overhead: +$13,750",
                    ],
                    [
                        "Cumulative cash movement uses zero opening operating balances",
                        "Cumulative operating cash flow reaches negative $131,250 after overhead",
                        "Cumulative operating cash flow improves to negative $117,500",
                        "Cumulative operating cash flow improves to negative $103,750",
                    ],
                    [
                        "Ending unrestricted cash begins with $250,000 owner funding",
                        "$250,000 opening cash less $131,250 movement leaves $118,750",
                        "$118,750 opening cash plus $13,750 movement leaves $132,500",
                        "$132,500 opening cash plus $13,750 movement leaves $146,250",
                    ],
                    [
                        "Open balance sheet items explain the working-capital investment",
                        "$250,000 receivables less $105,000 payables requires $145,000 funding",
                        "$250,000 receivables less $105,000 payables requires $145,000 funding",
                        "$250,000 receivables less $105,000 payables requires $145,000 funding",
                    ],
                    [
                        "Accumulated profit bridges opening capital to ending net assets",
                        "$13,750 cumulative profit increases opening capital to $263,750",
                        "$27,500 cumulative profit increases opening capital to $277,500",
                        "$41,250 cumulative profit increases opening capital to $291,250",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A load is not finished when the truck unloads; it is finished when identity, evidence, obligations, and cash agree.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Verify the contracting entity's FMCSA authority, process-agent filing, and current $75,000 bond or trust arrangement before accepting covered brokerage work.",
        "Assign named owners to intake, carrier identity, dispatch, tracking, billing, and treasury within the canonical three-full-time-plus-two-contractor Base team.",
        "Execute the six reference modules in a development environment and add concurrent-writer, external retry, correction-journal, and bank-allocation tests before deployment.",
        "Build a dated thirteen-week cash forecast using $12,500 shipper bills, $10,500 carrier commitments, actual payment maturities, and explicit funding restrictions.",
        "Run the forty-opportunity monthly cohort and reconcile $250,000 billings, $26,250 overhead, and $13,750 owner profit without treating collections as new revenue.",
        "Route first-sale customs coordination through the importer, licensed customs broker, and counsel; preserve confidential valuation evidence and record only contracted brokerage fees.",
    ],
    "statutory_citations": [
        {
            "title": "49 U.S.C. § 13904 — Registration of brokers",
            "url": "https://www.law.cornell.edu/uscode/text/49/13904",
            "relevance": "Establishes the federal registration framework for brokers arranging covered transportation.",
        },
        {
            "title": "49 U.S.C. § 13906 — Security requirements",
            "url": "https://www.law.cornell.edu/uscode/text/49/13906",
            "relevance": "Provides statutory security requirements, including the $75,000 property-broker bond or trust framework.",
        },
        {
            "title": "49 CFR § 387.307 — Property broker surety bond or trust fund",
            "url": "https://www.ecfr.gov/current/title-49/section-387.307",
            "relevance": "Governs property-broker security arrangements and related operating requirements; check the current text before launch.",
        },
        {
            "title": "49 CFR Part 366 — Designation of process agent",
            "url": "https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-366",
            "relevance": "Supplies process-agent designation requirements relevant to broker registration and operations.",
        },
        {
            "title": "49 CFR § 371.3 — Records to be kept by brokers",
            "url": "https://www.ecfr.gov/current/title-49/section-371.3",
            "relevance": "Requires transaction records, generally retained for three years, and addresses parties' review rights.",
        },
        {
            "title": "49 U.S.C. § 14706 — Liability of carriers under receipts and bills of lading",
            "url": "https://www.law.cornell.edu/uscode/text/49/14706",
            "relevance": "Provides the carrier cargo-liability framework for covered transportation; broker contracts and conduct require separate analysis.",
        },
        {
            "title": "19 U.S.C. § 1401a — Value",
            "url": "https://www.law.cornell.edu/uscode/text/19/1401a",
            "relevance": "Establishes customs valuation methods and transaction-value adjustments relevant to earlier-sale valuation analysis.",
        },
        {
            "title": "19 CFR § 152.103 — Transaction value",
            "url": "https://www.ecfr.gov/current/title-19/section-152.103",
            "relevance": "Defines transaction-value mechanics, including adjustments and relationship considerations that can affect first-sale eligibility.",
        },
        {
            "title": "19 U.S.C. § 1641 — Customs brokers",
            "url": "https://www.law.cornell.edu/uscode/text/19/1641",
            "relevance": "Distinguishes regulated customs business from domestic freight coordination and supports routing entry work through authorized parties.",
        },
        {
            "title": "19 CFR § 163.4 — Record retention period",
            "url": "https://www.ecfr.gov/current/title-19/section-163.4",
            "relevance": "Sets customs record-retention periods, generally five years subject to specified exceptions, for supporting entry and valuation evidence.",
        },
    ],
}
