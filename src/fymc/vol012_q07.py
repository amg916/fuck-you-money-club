from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "equipment-brokerage-complete-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute equipment brokerage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Serial-Level Intake, UCC Lien Releases, Independent Inspections, Escrow Instructions, SQLite Event Receipts, and Commission-Only Cash Reconciliation",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #11, Equipment Brokerage, ranks #12 with an 81/100 Money-to-Manpower "
        "Score. This chapter converts seven mapped plays into one controlled production "
        "system: lender dispositions, CNC matching, fleet breakups, plant relocations, "
        "inspection-led recovery, buyer alerts, and queue-informed site intelligence. "
        "Six are chapter-defined operating applications; the seventh retains its supplied "
        "cross-track identifier. The ledger recognizes broker commissions, never equipment "
        "principal or land-option value. Canonical annual owner profits remain $25,000 "
        "Conservative, $157,500 Base, and $360,000 Scaled. A six-module SQLite reference "
        "serializes writes, rejects reused event identifiers with changed payloads, and "
        "reconciles paired postings. The worked cohort demonstrates $112,500 quarterly "
        "commissions and $39,375 operating cash generation from a seasoned pipeline, "
        "while separating that steady-state illustration from a cold-start launch."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual broker commissions; equipment transaction value excluded",
            "note": "25% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$450,000",
            "context": "Annual broker commissions; equipment transaction value excluded",
            "note": "35.0% net margin; $157,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual broker commissions; equipment transaction value excluded",
            "note": "45% net margin; $360,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build the evidence packet before publishing an executable offer",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start each mandate with an asset identity, an authorized seller, and an explicit "
                    "commission contract. Capture manufacturer, model, serial photograph, engine or spindle "
                    "hours, location, accessory inventory, ownership entity, and the person empowered to "
                    "sign. A machine advertised on MachineryTrader or Surplus Record is a sourcing lead, "
                    "not proof that the advertiser can convey it. Normalize manufacturer and serial into "
                    "one asset key; retain original photographs and documents under versioned object "
                    "references. The broker's intake score measures commercial readiness only: asset fit, "
                    "reachable authority contact, buyer fit, and service records each contribute twenty-five "
                    "points. A perfect score does not establish ownership, condition, export eligibility, "
                    "or clear title. Record fee percentage, fee payer, earning event, payment deadline, "
                    "and treatment of inspection failures before introducing buyers. At a $250,000 sale "
                    "and five percent commission, the broker earns $12,500 only when the contracted "
                    "earning event occurs. The $250,000 belongs to the equipment transaction, not broker "
                    "revenue. Assign one employee as deal owner and use three contractors for inspection, "
                    "transport coordination, and specialist document work. Contractors receive scoped "
                    "tasks, deadlines, and evidence requirements rather than broad authority to change "
                    "price, release funds, or promise equipment performance."
                ),
                (
                    "Clear ownership and liens through the seller's actual legal identity, not merely "
                    "the machine's yard address. Under UCC sections 9-301 and 9-307, the debtor's "
                    "location generally determines the governing perfection jurisdiction, subject to "
                    "important exceptions. Search the appropriate filing office using the debtor's exact "
                    "name, inspect relevant amendments, and investigate certificate-of-title rules for "
                    "titled equipment or vehicles. A clean serial search alone misses blanket security "
                    "interests. Obtain a lender payoff letter identifying the covered assets, good-through "
                    "date, per-diem accrual, wire instructions, and release mechanics. UCC section "
                    "9-315 explains why an unauthorized sale can leave a security interest attached; "
                    "section 9-513 addresses termination statements but does not make every termination "
                    "an asset-specific release. Independently call a previously established lender number "
                    "to verify settlement instructions. Commission an equipment-class inspection: cold "
                    "start and undercarriage measurements for excavators, spindle tests and controller "
                    "alarms for CNC machines, and diagnostic reports for fleet vehicles. Preserve raw "
                    "findings, not just a pass label. If the seller refuses inspection or the lender "
                    "cannot document release, suspend the listing or terminate the mandate before "
                    "spending more on freight reservations and buyer acquisition."
                ),
                (
                    "Translate the evidence packet into a controlled offer and settlement instruction "
                    "set. The seller's purchase agreement should identify the exact machine, included "
                    "tooling, inspection rights, acceptance procedure, risk-of-loss allocation, and "
                    "loading responsibilities. Express descriptions can matter under UCC section "
                    "2-313; warranty exclusions require the specificity and presentation addressed "
                    "by section 2-316. Do not transform an inspector's limited observations into a "
                    "broker promise of future uptime. For a fleet transaction, determine whether the "
                    "activity triggers a state vehicle-dealer license; California Vehicle Code section "
                    "11700 illustrates why truck brokerage and stationary CNC brokerage need different "
                    "classification work. For exports, record equipment classification, destination, "
                    "end user, end use, and the applicable EAR analysis before arranging shipment. "
                    "Use a suitable independent escrow provider with verified instructions, rather than "
                    "routing purchase principal through the broker's operating account. Release conditions "
                    "should connect cleared buyer funds, lender payoff, asset release, agreed acceptance, "
                    "and commission disbursement. Document exceptions in signed amendments. When an "
                    "inspection changes the price, update the commission calculation and settlement "
                    "statement together; an informal discount in email must not leave an obsolete fee "
                    "in the accounting system or an inconsistent payoff amount with escrow."
                ),
            ],
            "table": {
                "caption": "Serial-to-Settlement Evidence and Exception Ownership Matrix",
                "headers": [
                    "Operating checkpoint and accountable person",
                    "Evidence required before advancing the transaction",
                    "Named tool or controlling authority",
                    "Failure response preserving cash and credibility",
                ],
                "rows": [
                    [
                        "Deal owner establishes seller identity and signing authority",
                        "Entity record, authorized signature, serial images, and executed mandate",
                        "Secretary of State records and DocuSign execution certificate",
                        "Suspend marketing when ownership authority remains unsupported by documents",
                    ],
                    [
                        "Deal owner records price and commission earning conditions",
                        "Signed fee percentage, payer identity, trigger, and payment deadline",
                        "HubSpot deal record linked to executed commission agreement",
                        "Reject verbal fee changes until both documents are amended",
                    ],
                    [
                        "Document contractor investigates blanket liens and titled assets",
                        "Debtor-name searches, payoff terms, and asset-specific release instructions",
                        "UCC sections 9-301, 9-307, 9-315, and 9-513",
                        "Stop settlement when creditor release scope excludes advertised assets",
                    ],
                    [
                        "Independent inspector measures equipment condition against buyer requirements",
                        "Cold-start video, diagnostic outputs, measurements, and signed inspection limitations",
                        "OEM diagnostic tools and EquipmentWatch valuation cross-checks support review",
                        "Reprice through signed amendments or withdraw defective inventory promptly",
                    ],
                    [
                        "Specialist reviewer classifies shipment and dealer-license requirements",
                        "Equipment classification, destination, end use, and jurisdiction-specific activity analysis",
                        "15 CFR parts 734, 736, 738, and 744",
                        "Hold shipment until required authorization and activity classification resolve",
                    ],
                    [
                        "Escrow coordinator verifies payoff and commission distribution instructions",
                        "Authenticated beneficiary details, signed release conditions, and acceptance evidence",
                        "Independent escrow statement reconciled against executed purchase agreement",
                        "Reject changed wire instructions until independently authenticated by callback",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that protect equipment commissions",
                "body": "Prevent expensive disputes at intake rather than negotiating around missing evidence at settlement.",
                "items": [
                    "Request the controller's alarm-history export before scheduling a CNC demonstration; a warm machine and cleared screen can conceal intermittent faults.",
                    "Photograph serial plates together with surrounding machine features, then compare those photographs with inspection and pickup evidence.",
                    "Obtain lender payoff per-diem figures before choosing a closing date; a delayed wire can otherwise leave a small unpaid balance blocking release.",
                    "Ask the rigger for written loading assumptions, floor restrictions, disconnect scope, and insurance evidence before promising a pickup window.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Identify and contract",
                    "action": "Create one normalized asset record and execute the commission mandate.",
                    "detail": "Record seller authority, price, fee payer, earning trigger, and document references before buyer introductions.",
                },
                {
                    "step": 2,
                    "title": "Verify and price",
                    "action": "Complete independent condition review and jurisdiction-specific lien research.",
                    "detail": "Resolve exceptions with written repricing, asset-specific release instructions, or a documented withdrawal.",
                },
                {
                    "step": 3,
                    "title": "Settle through controlled instructions",
                    "action": "Match escrow conditions to acceptance, payoff, release, and commission disbursement.",
                    "detail": "Authenticate beneficiary changes outside the requesting email channel and retain the signed final statement.",
                },
                {
                    "step": 4,
                    "title": "Recognize and reconcile",
                    "action": "Post the earned commission once and match actual bank receipts.",
                    "detail": "Separate equipment principal from broker cash, resolve receivable differences, and close the evidence packet.",
                },
            ],
        },
        {
            "heading": "2. Implement six serialized modules for evidence, events, and the commission ledger",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference below uses Python's standard sqlite3 module and one local SQLite "
                    "database. Copy the six code cells into one script in their displayed order, or "
                    "load them sequentially into the same namespace. Initialize the schema before "
                    "starting workers; each worker opens its own connection with identical pragmas "
                    "and never shares a connection between threads. SQLite must live on storage "
                    "with reliable local locking, not a casually shared network filesystem. Every "
                    "business mutation enters BEGIN IMMEDIATE before reading decision state. That "
                    "serializes competing writers and closes the read-check-write race around state "
                    "advancement, duplicate commission creation, and receipt allocation. A busy worker "
                    "may receive a lock timeout; its caller retries the same event identifier, never "
                    "a newly minted identifier. The event receipt stores the complete canonical request "
                    "and committed response. Replaying the same request returns that response; changing "
                    "the payload while retaining its identifier raises an error. Database uniqueness "
                    "provides a second defense for intake keys, active assets, invoices, earned-fee "
                    "postings, and bank references. Restrict database file access to the application "
                    "account and backups. These guarantees govern this single-database write path, "
                    "not arbitrary direct edits, external escrow systems, or uncoordinated application "
                    "copies operating separate databases."
                ),
                (
                    "The state machine separates commercial readiness from verified evidence. An intake "
                    "record can advance to VERIFIED only after authority, asset identity, condition, "
                    "lien, and export checks exist. ESCROW_READY additionally requires verified escrow "
                    "instructions. Issuing the commission invoice requires delivery or acceptance "
                    "evidence satisfying the mandate's earning condition, and all required checks "
                    "must be current at that transaction. The reference uses a seven-day freshness "
                    "window as an explicit operating assumption; a live payoff may require a much "
                    "shorter deadline. Replace that window with document-specific expiry rules before "
                    "handling such transactions. Evidence records are append-only in this minimal "
                    "model, and reviewers submit their authenticated identity through the application. "
                    "The script records that identity but does not authenticate it. Corrections, "
                    "refunds, reversals, partial asset releases, and changed mandates require additional "
                    "versioned workflows; do not bypass constraints to improvise them. A withdrawn "
                    "deal may be scrubbed before invoicing, while an invoiced deal requires a proper "
                    "credit or reversal extension. Purchase principal never enters the ledger. Pair "
                    "each amount with debit and credit accounts in one row, ensuring structural "
                    "balance without relying on a later process to discover an orphaned journal leg."
                ),
                (
                    "The accounting sequence is deliberately narrow: earning creates a receivable and "
                    "commission revenue; collecting debits operating cash and credits that receivable; "
                    "paying an operating expense debits expense and credits cash. Amounts are positive "
                    "integer cents, and the program rejects percentages that produce fractional cents "
                    "instead of silently choosing a rounding policy. The recognition event requires "
                    "the full contracted fee to be earned; milestone commissions need a separate "
                    "schedule extension. Receipts may be partial but cannot exceed the open invoice. "
                    "A unique bank reference prevents two workers from allocating the same imported "
                    "bank line to different deals. Export bank transactions from the broker's own "
                    "account, normalize them outside the write transaction, and post only authenticated "
                    "matches. Never keep a database transaction open while calling escrow, sending "
                    "email, or fetching an inspection. External notifications should follow committed "
                    "receipts; add a transactional outbox and provider-supported idempotency before "
                    "automating outward actions. The supplied QA module checks a consistent snapshot, "
                    "but these snippets have not been executed here. Before deployment, run crash "
                    "injection, simultaneous duplicate deliveries, changed-payload retries, stale-evidence "
                    "attempts, and concurrent overcollection tests. Prove backups restore successfully "
                    "and reconcile the restored ledger to bank statements before accepting live work."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite-or-Postgres Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and narrowly defined production responsibility",
                    "Copy-pasteable Python and SQLite reference implementation",
                    "Operating boundary and required verification evidence",
                ],
                "rows": [
                    [
                        "Module 1: Create constrained SQLite storage before starting workers",
                        '''import json
import sqlite3
import time

SCHEMA = """
CREATE TABLE IF NOT EXISTS event_receipt (
    event_id TEXT PRIMARY KEY,
    request_json TEXT NOT NULL,
    response_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS deal (
    deal_id INTEGER PRIMARY KEY,
    intake_key TEXT NOT NULL UNIQUE,
    asset_key TEXT NOT NULL,
    price_cents INTEGER NOT NULL CHECK(price_cents > 0),
    fee_cents INTEGER NOT NULL CHECK(fee_cents > 0),
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    state TEXT NOT NULL CHECK(state IN (
        'INTAKE', 'VERIFIED', 'ESCROW_READY',
        'INVOICED', 'PAID', 'SCRUBBED'
    ))
);
CREATE UNIQUE INDEX IF NOT EXISTS one_active_asset
ON deal(asset_key)
WHERE state NOT IN ('PAID', 'SCRUBBED');
CREATE TABLE IF NOT EXISTS evidence (
    evidence_id INTEGER PRIMARY KEY,
    deal_id INTEGER NOT NULL REFERENCES deal(deal_id),
    kind TEXT NOT NULL CHECK(kind IN (
        'authority', 'asset', 'condition', 'lien',
        'export', 'escrow', 'delivery'
    )),
    reference TEXT NOT NULL,
    verifier TEXT NOT NULL,
    checked_at INTEGER NOT NULL,
    UNIQUE(deal_id, kind)
);
CREATE TABLE IF NOT EXISTS invoice (
    invoice_id INTEGER PRIMARY KEY,
    deal_id INTEGER NOT NULL UNIQUE REFERENCES deal(deal_id),
    fee_cents INTEGER NOT NULL CHECK(fee_cents > 0)
);
CREATE TABLE IF NOT EXISTS journal (
    journal_id INTEGER PRIMARY KEY,
    event_id TEXT NOT NULL UNIQUE REFERENCES event_receipt(event_id)
        DEFERRABLE INITIALLY DEFERRED,
    deal_id INTEGER REFERENCES deal(deal_id),
    kind TEXT NOT NULL CHECK(kind IN ('FEE', 'RECEIPT', 'EXPENSE')),
    amount_cents INTEGER NOT NULL CHECK(amount_cents > 0),
    debit_account TEXT NOT NULL,
    credit_account TEXT NOT NULL,
    bank_ref TEXT UNIQUE,
    CHECK(
        (kind = 'FEE' AND deal_id IS NOT NULL AND bank_ref IS NULL
         AND debit_account = 'AR'
         AND credit_account = 'COMMISSION')
        OR
        (kind = 'RECEIPT' AND deal_id IS NOT NULL AND bank_ref IS NOT NULL
         AND debit_account = 'CASH'
         AND credit_account = 'AR')
        OR
        (kind = 'EXPENSE' AND deal_id IS NULL AND bank_ref IS NOT NULL
         AND debit_account = 'EXPENSE'
         AND credit_account = 'CASH')
    )
);
CREATE UNIQUE INDEX IF NOT EXISTS one_earned_fee
ON journal(deal_id) WHERE kind = 'FEE';
"""

def connect_database(path):
    connection = sqlite3.connect(
        path, timeout=30, isolation_level=None
    )
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA synchronous = FULL")
    connection.execute("PRAGMA busy_timeout = 30000")
    return connection

db = connect_database("broker_ledger.sqlite3")
db.executescript(SCHEMA)
''',
                        "Use one local database and separate worker connections; initialize migrations before admitting live mutation requests.",
                    ],
                    [
                        "Module 2: Serialize requests and score authorized equipment intake",
                        '''def nonempty(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("A substantive text value is required")
    return value.strip()

def positive_cents(value):
    if type(value) is not int or value <= 0:
        raise ValueError("Amounts must be positive integer cents")
    return value

def atomic_event(event_id, payload, work):
    event_id = nonempty(event_id)
    request_json = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    )
    db.execute("BEGIN IMMEDIATE")
    try:
        prior = db.execute(
            "SELECT request_json, response_json FROM event_receipt "
            "WHERE event_id = ?", (event_id,)
        ).fetchone()
        if prior is not None:
            if prior["request_json"] != request_json:
                raise ValueError("Event identifier reused with changed payload")
            result = json.loads(prior["response_json"])
        else:
            result = work()
            db.execute(
                "INSERT INTO event_receipt VALUES (?, ?, ?)",
                (event_id, request_json, json.dumps(result, sort_keys=True))
            )
        db.execute("COMMIT")
        return result
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise

def intake(event_id, intake_key, manufacturer, serial,
           price_cents, fee_bps, signals):
    intake_key = nonempty(intake_key)
    asset_key = (
        nonempty(manufacturer).upper() + ":" + nonempty(serial).upper()
    )
    positive_cents(price_cents)
    if type(fee_bps) is not int or not 1 <= fee_bps <= 10000:
        raise ValueError("Fee basis points outside supported range")
    required = {"authority_contact", "asset_fit",
                "buyer_fit", "service_records"}
    if set(signals) != required:
        raise ValueError("Supply exactly the four scoring signals")
    if any(type(value) is not bool for value in signals.values()):
        raise ValueError("Scoring signals must be explicit booleans")
    fee_cents, remainder = divmod(price_cents * fee_bps, 10000)
    if remainder:
        raise ValueError("Contract fee requires explicit cent rounding")
    positive_cents(fee_cents)
    score = 25 * sum(signals.values())
    payload = {
        "op": "intake", "intake_key": intake_key,
        "asset_key": asset_key, "price_cents": price_cents,
        "fee_bps": fee_bps, "signals": dict(signals)
    }
    def work():
        cursor = db.execute(
            "INSERT INTO deal "
            "(intake_key, asset_key, price_cents, fee_cents, score, state) "
            "VALUES (?, ?, ?, ?, ?, 'INTAKE')",
            (intake_key, asset_key, price_cents, fee_cents, score)
        )
        return {"deal_id": cursor.lastrowid, "score": score}
    return atomic_event(event_id, payload, work)
''',
                        "Use stable upstream event identifiers; commercial scores never substitute for authenticated seller and equipment verification.",
                    ],
                    [
                        "Module 3: Enforce evidence freshness and escrow state transitions",
                        '''CORE_CHECKS = {"authority", "asset", "condition", "lien", "export"}
ALL_CHECKS = CORE_CHECKS | {"escrow", "delivery"}
FRESH_SECONDS = 7 * 24 * 60 * 60

def current_deal(deal_id):
    if type(deal_id) is not int or deal_id <= 0:
        raise ValueError("Deal identifier must be a positive integer")
    row = db.execute(
        "SELECT * FROM deal WHERE deal_id = ?", (deal_id,)
    ).fetchone()
    if row is None:
        raise ValueError("Deal record does not exist")
    return row

def require_checks(deal_id, required):
    now = int(time.time())
    rows = db.execute(
        "SELECT kind, checked_at FROM evidence WHERE deal_id = ?",
        (deal_id,)
    ).fetchall()
    present = {
        row["kind"] for row in rows
        if now - FRESH_SECONDS <= row["checked_at"] <= now
    }
    if not required.issubset(present):
        raise ValueError("Required evidence is missing or expired")

def record_check(event_id, deal_id, kind, reference,
                 verifier, checked_at):
    if kind not in ALL_CHECKS:
        raise ValueError("Evidence kind is outside the supported set")
    reference = nonempty(reference)
    verifier = nonempty(verifier)
    if type(checked_at) is not int:
        raise ValueError("Evidence timestamp must be integer epoch seconds")
    payload = {
        "op": "check", "deal_id": deal_id, "kind": kind,
        "reference": reference, "verifier": verifier,
        "checked_at": checked_at
    }
    def work():
        row = current_deal(deal_id)
        if row["state"] not in {"INTAKE", "VERIFIED", "ESCROW_READY"}:
            raise ValueError("Evidence is closed for this deal state")
        now = int(time.time())
        if not now - FRESH_SECONDS <= checked_at <= now:
            raise ValueError("Evidence timestamp is outside freshness window")
        db.execute(
            "INSERT INTO evidence "
            "(deal_id, kind, reference, verifier, checked_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (deal_id, kind, reference, verifier, checked_at)
        )
        return {"deal_id": deal_id, "recorded_kind": kind}
    return atomic_event(event_id, payload, work)

def advance(event_id, deal_id, target, reason):
    reason = nonempty(reason)
    payload = {
        "op": "advance", "deal_id": deal_id,
        "target": target, "reason": reason
    }
    def work():
        row = current_deal(deal_id)
        allowed = {
            "INTAKE": {"VERIFIED", "SCRUBBED"},
            "VERIFIED": {"ESCROW_READY", "SCRUBBED"},
            "ESCROW_READY": {"SCRUBBED"}
        }
        if target not in allowed.get(row["state"], set()):
            raise ValueError("State transition is not permitted")
        if target == "VERIFIED":
            require_checks(deal_id, CORE_CHECKS)
        if target == "ESCROW_READY":
            require_checks(deal_id, CORE_CHECKS | {"escrow"})
        db.execute(
            "UPDATE deal SET state = ? WHERE deal_id = ?",
            (target, deal_id)
        )
        return {"deal_id": deal_id, "state": target}
    return atomic_event(event_id, payload, work)
''',
                        "Authenticate reviewers outside this reference; implement versioned evidence renewals and document-specific expiration before broader production use.",
                    ],
                    [
                        "Module 4: Recognize earned fees and allocate bank cash once",
                        '''def issue_invoice(event_id, deal_id, earning_reference):
    earning_reference = nonempty(earning_reference)
    payload = {
        "op": "invoice", "deal_id": deal_id,
        "earning_reference": earning_reference
    }
    def work():
        row = current_deal(deal_id)
        if row["state"] != "ESCROW_READY":
            raise ValueError("Deal is not ready for commission recognition")
        require_checks(deal_id, ALL_CHECKS)
        db.execute(
            "INSERT INTO invoice (deal_id, fee_cents) VALUES (?, ?)",
            (deal_id, row["fee_cents"])
        )
        db.execute(
            "INSERT INTO journal "
            "(event_id, deal_id, kind, amount_cents, "
            "debit_account, credit_account, bank_ref) "
            "VALUES (?, ?, 'FEE', ?, 'AR', 'COMMISSION', NULL)",
            (event_id, deal_id, row["fee_cents"])
        )
        db.execute(
            "UPDATE deal SET state = 'INVOICED' WHERE deal_id = ?",
            (deal_id,)
        )
        return {"deal_id": deal_id, "fee_cents": row["fee_cents"]}
    return atomic_event(event_id, payload, work)

def collect_fee(event_id, deal_id, bank_ref, amount_cents):
    bank_ref = nonempty(bank_ref)
    positive_cents(amount_cents)
    payload = {
        "op": "collect", "deal_id": deal_id,
        "bank_ref": bank_ref, "amount_cents": amount_cents
    }
    def work():
        row = current_deal(deal_id)
        if row["state"] != "INVOICED":
            raise ValueError("Deal does not have an open invoice")
        invoice_row = db.execute(
            "SELECT fee_cents FROM invoice WHERE deal_id = ?", (deal_id,)
        ).fetchone()
        if invoice_row is None:
            raise ValueError("Invoice record is missing")
        paid = db.execute(
            "SELECT COALESCE(SUM(amount_cents), 0) FROM journal "
            "WHERE deal_id = ? AND kind = 'RECEIPT'", (deal_id,)
        ).fetchone()[0]
        total_paid = paid + amount_cents
        if total_paid > invoice_row["fee_cents"]:
            raise ValueError("Receipt exceeds the remaining commission")
        db.execute(
            "INSERT INTO journal "
            "(event_id, deal_id, kind, amount_cents, "
            "debit_account, credit_account, bank_ref) "
            "VALUES (?, ?, 'RECEIPT', ?, 'CASH', 'AR', ?)",
            (event_id, deal_id, amount_cents, bank_ref)
        )
        if total_paid == invoice_row["fee_cents"]:
            db.execute(
                "UPDATE deal SET state = 'PAID' WHERE deal_id = ?",
                (deal_id,)
            )
        return {"deal_id": deal_id, "collected_cents": total_paid}
    return atomic_event(event_id, payload, work)

def pay_expense(event_id, bank_ref, amount_cents, cost_reference):
    bank_ref = nonempty(bank_ref)
    cost_reference = nonempty(cost_reference)
    positive_cents(amount_cents)
    payload = {
        "op": "expense", "bank_ref": bank_ref,
        "amount_cents": amount_cents, "cost_reference": cost_reference
    }
    def work():
        db.execute(
            "INSERT INTO journal "
            "(event_id, deal_id, kind, amount_cents, "
            "debit_account, credit_account, bank_ref) "
            "VALUES (?, NULL, 'EXPENSE', ?, 'EXPENSE', 'CASH', ?)",
            (event_id, amount_cents, bank_ref)
        )
        return {"expense_cents": amount_cents, "bank_ref": bank_ref}
    return atomic_event(event_id, payload, work)
''',
                        "One imported bank line supports one allocation here; batch splits, reversals, refunds, and opening balances require explicit extensions.",
                    ],
                    [
                        "Module 5: Reconcile receivables and expose balanced account movements",
                        '''db.executescript("""
CREATE VIEW IF NOT EXISTS deal_reconciliation AS
SELECT
    d.deal_id,
    d.state,
    COALESCE(i.fee_cents, 0) AS invoiced_cents,
    COALESCE(j.earned_cents, 0) AS earned_cents,
    COALESCE(j.received_cents, 0) AS received_cents,
    COALESCE(i.fee_cents, 0) - COALESCE(j.received_cents, 0)
        AS receivable_cents
FROM deal AS d
LEFT JOIN invoice AS i ON i.deal_id = d.deal_id
LEFT JOIN (
    SELECT deal_id,
        SUM(CASE WHEN kind = 'FEE' THEN amount_cents ELSE 0 END)
            AS earned_cents,
        SUM(CASE WHEN kind = 'RECEIPT' THEN amount_cents ELSE 0 END)
            AS received_cents
    FROM journal
    WHERE deal_id IS NOT NULL
    GROUP BY deal_id
) AS j ON j.deal_id = d.deal_id;

CREATE VIEW IF NOT EXISTS account_movements AS
SELECT account, SUM(signed_cents) AS net_debit_cents
FROM (
    SELECT debit_account AS account, amount_cents AS signed_cents
    FROM journal
    UNION ALL
    SELECT credit_account AS account, -amount_cents AS signed_cents
    FROM journal
)
GROUP BY account;
""")

def reconciliation_snapshot():
    db.execute("BEGIN")
    try:
        deals = [
            dict(row) for row in db.execute(
                "SELECT * FROM deal_reconciliation ORDER BY deal_id"
            )
        ]
        movements = [
            dict(row) for row in db.execute(
                "SELECT * FROM account_movements ORDER BY account"
            )
        ]
        db.execute("COMMIT")
        return {"deals": deals, "account_movements": movements}
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
''',
                        "Cash output represents movement since ledger inception; reconcile separately documented opening cash to the bank's ending balance.",
                    ],
                    [
                        "Module 6: Run snapshot QA and reject broken ledger invariants",
                        '''def run_qa():
    db.execute("BEGIN")
    try:
        integrity = [
            row[0] for row in db.execute("PRAGMA integrity_check")
        ]
        if integrity != ["ok"]:
            raise AssertionError("Database integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise AssertionError("Foreign-key check failed")
        broken = db.execute("""
            SELECT deal_id FROM deal_reconciliation
            WHERE invoiced_cents != earned_cents
               OR receivable_cents < 0
               OR (state = 'PAID'
                   AND (invoiced_cents <= 0 OR receivable_cents != 0))
               OR (state = 'INVOICED'
                   AND (invoiced_cents <= 0 OR receivable_cents <= 0))
               OR (state NOT IN ('INVOICED', 'PAID')
                   AND invoiced_cents != 0)
        """).fetchall()
        if broken:
            raise AssertionError("Deal and ledger reconciliation failed")
        fee_mismatch = db.execute("""
            SELECT i.deal_id FROM invoice AS i
            JOIN deal AS d ON d.deal_id = i.deal_id
            WHERE i.fee_cents != d.fee_cents
        """).fetchall()
        if fee_mismatch:
            raise AssertionError("Invoice differs from contracted fee")
        total = db.execute(
            "SELECT COALESCE(SUM(net_debit_cents), 0) "
            "FROM account_movements"
        ).fetchone()[0]
        if total != 0:
            raise AssertionError("Account movements do not balance")
        db.execute("COMMIT")
        return {"integrity": "ok", "ledger_balance_cents": total}
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
''',
                        "Run concurrency and crash tests in an isolated database; snapshot QA cannot establish authenticity of external documents.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before live settlement",
                "body": "Require evidence for each check before accepting live commission postings or automated customer notifications.",
                "items": [
                    "Replay one intake event simultaneously from separate connections and verify exactly one committed deal and one event receipt.",
                    "Attempt two concurrent receipts exceeding one invoice together; verify that only a permissible allocation commits and the other fails.",
                    "Demonstrate that expired payoff evidence, missing acceptance evidence, and changed escrow instructions stop the relevant transition.",
                    "Restore a backup into isolation, run the QA module, and match commission receipts and expenses to independently downloaded bank records.",
                ],
            },
        },
        {
            "heading": "3. Walk a seasoned 90-day cohort from lead scrubs to collected commission cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The worked cohort represents a seasoned Base operation, not a promise that a "
                    "new brokerage closes nine deals in its first ninety days. Time to first deal "
                    "remains two to nine months. At day zero, two earlier cohorts each contain five "
                    "signed mandates undergoing diligence; neither has earned a commission or created "
                    "a receivable. Three deals from the earlier cohort close in Month 1, three from "
                    "the later cohort close in Month 2, and three from Month 1 intake close in "
                    "Month 3. Each sold machine has a $250,000 price and a five percent contracted "
                    "fee, producing $12,500 commission. Nine closings therefore represent $2,250,000 "
                    "equipment transaction value but only $112,500 recognized broker revenue. Each "
                    "month also brings thirty fresh leads. Eight duplicate listings, seven poor-fit "
                    "machines, and five unsupported seller-authority claims are scrubbed before "
                    "expensive diligence, leaving ten qualified opportunities. Five fail to secure "
                    "an acceptable mandate, leaving five signed candidates. Eventually three close, "
                    "one fails inspection, and one fails lien release. Track early lead scrubs "
                    "separately from post-mandate losses so the team can distinguish sourcing noise "
                    "from costly execution failures. Month 2 and Month 3 intake remain future "
                    "pipeline at the observation cutoff."
                ),
                (
                    "Commission recognition and cash collection intentionally diverge during the "
                    "quarter. Month 1 earns $37,500 but collects only $25,000, leaving $12,500 "
                    "receivable. Month 2 earns another $37,500 and collects $37,500: $12,500 "
                    "from the previous month's receivable plus $25,000 from current closings. "
                    "Its ending receivable remains $12,500. Month 3 earns $37,500 and collects "
                    "$50,000, comprising the prior balance plus all current fees, so ending "
                    "receivables return to zero. Assume all operating costs are paid in their "
                    "month, with no opening or ending expense payables. Monthly fixed overhead "
                    "is $10,000, within the stated $2,500 to $14,000 monthly operating-overhead "
                    "range. Another $14,375 covers variable contractor work, paid acquisition, "
                    "inspection coordination, travel, and failed-deal handling, making total "
                    "monthly costs $24,375. This explicitly treats the quoted overhead range "
                    "as fixed operating overhead rather than the entire cost base. If that "
                    "range were intended to include every expense, it would not reconcile "
                    "to the canonical Base margin. The quarter therefore records $73,125 "
                    "costs and $39,375 owner operating profit. That residual is before owner "
                    "distributions and any personal tax treatment; it does not imply that "
                    "every dollar should immediately leave the business."
                ),
                (
                    "Beginning operating cash is $30,000, an illustrative funding balance within "
                    "the $10,000 to $75,000 startup-capital range, not revenue. Month 1 adds "
                    "$625 after paying $24,375 costs, ending at $30,625. Month 2 adds "
                    "$13,125 and ends at $43,750. Month 3 adds $25,625 and ends at "
                    "$69,375. Cumulative operating cash generation is consequently $39,375, "
                    "matching quarterly profit because opening and ending receivables and expense "
                    "payables are zero. Within each month, however, a late escrow disbursement "
                    "can create a working-capital trough even when the month-end statement looks "
                    "healthy. Maintain a weekly cash schedule using actual payroll, contractor, "
                    "and settlement dates. Annualizing this steady quarter yields thirty-six "
                    "closings, $9,000,000 equipment value, $450,000 broker commissions, "
                    "$292,500 costs, and $157,500 owner profit at 35.0 percent. The other "
                    "canonical cases remain $100,000 revenue less $75,000 costs for $25,000 "
                    "profit, and $800,000 revenue less $440,000 costs for $360,000 profit. "
                    "Do not multiply deal count alone to claim the Scaled case; its higher "
                    "margin requires better acquisition efficiency, contractor utilization, and "
                    "fee mix while expanding staffing from one employee and three contractors "
                    "to two employees and four contractors."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort or accounting period under observation",
                    "Lead funnel, closings, and documented losses",
                    "Recognized commissions and actual collection timing",
                    "Operating costs and cumulative cash reconciliation",
                ],
                "rows": [
                    [
                        "Opening position includes two seasoned five-mandate cohorts",
                        "Ten opening mandates later yield six closings and four documented losses",
                        "No opening commission receivables; no equipment principal enters broker cash",
                        "$30,000 opening funding; cumulative operating cash generation starts at zero",
                    ],
                    [
                        "Month 1 combines earlier-cohort closings with fresh intake",
                        "Thirty leads become ten qualified and five mandates; opening cohort closes three, loses two",
                        "$37,500 earned; $25,000 collected; $12,500 ending commission receivable",
                        "$10,000 fixed plus $14,375 variable; $625 cumulative generation; $30,625 ending cash",
                    ],
                    [
                        "Month 2 combines later opening-cohort closings with fresh intake",
                        "Thirty leads become ten qualified and five mandates; opening cohort closes three, loses two",
                        "$37,500 earned; $12,500 prior plus $25,000 current collected; $12,500 receivable",
                        "$24,375 total costs; $13,125 monthly generation; $13,750 cumulative; $43,750 ending cash",
                    ],
                    [
                        "Month 3 closes the five-mandate Month 1 cohort",
                        "Three close, one fails inspection, one fails release; thirty fresh leads yield five mandates",
                        "$37,500 earned; $12,500 prior plus $37,500 current collected; zero ending receivables",
                        "$24,375 total costs; $25,625 monthly generation; $39,375 cumulative; $69,375 ending cash",
                    ],
                    [
                        "Quarter cutoff retains Month 2 and Month 3 intake",
                        "Ten unclosed mandates target later months; expected attrition creates no present revenue",
                        "$112,500 total earned and collected; nine sales represent $2,250,000 equipment value",
                        "$73,125 costs; $39,375 profit; $30,000 opening cash plus generation equals $69,375",
                    ],
                    [
                        "Base annual run rate repeats the seasoned quarterly pattern",
                        "Thirty-six completed sales at $250,000 each represent $9,000,000 equipment value",
                        "$450,000 annual commissions equal thirty-six contracted fees of $12,500",
                        "$292,500 annual costs leave $157,500 profit and exactly 35.0 percent margin",
                    ],
                ],
            },
        },
        {
            "heading": "4. Route seven plays through one revenue boundary and explicit loss fallbacks",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Seven mapped plays feed the same controlled brokerage pipeline; they are not "
                    "seven independent revenue forecasts to add together. Because only one external "
                    "play identifier is supplied, the first six names below are chapter-defined "
                    "operating applications rather than invented catalog identifiers. Lender dispositions "
                    "source motivated sellers but demand asset-specific release evidence. CNC matching "
                    "uses controller type, travel envelope, spindle specifications, tooling, and power "
                    "requirements to reduce irrelevant buyer introductions. Fleet breakups trade one "
                    "large buyer dependency for several smaller settlements while increasing title "
                    "and transport coordination. Plant relocations exploit a dated shutdown or lease "
                    "deadline, but removal costs can erase apparent price advantage. Inspection-led "
                    "recovery preserves a viable transaction through disclosed repricing rather than "
                    "concealing defects. Buyer alerts accelerate matching only when recipients have "
                    "current purchasing authority, budgets, technical requirements, and geographic "
                    "constraints. Use HubSpot saved views or a small SQL matching job to select "
                    "buyers, then review each introduction before sending detailed asset information. "
                    "In every channel, count a lead once, an active mandate once, and a commission "
                    "once. Attribute a primary sourcing channel and retain secondary touches separately "
                    "so multiple contractors cannot each claim the same closed deal as incremental "
                    "production or inflate the operating forecast."
                ),
                (
                    "The required cross-track play, ferc_grid_interconnection_queue_land_speculation, "
                    "belongs to FERC / ISO Substation Interconnection Queue & Powered-Land Option "
                    "Flipping, TRACK_1. Its equipment-brokerage use is adjacent demand intelligence, "
                    "not a claim that the brokerage controls deliverable power. Overlay public PJM, "
                    "MISO, or CAISO queue records with county parcel data, zoning, substation "
                    "locations, and independently checked access constraints. Queue records frequently "
                    "describe generation interconnection rather than a site's entitlement to new "
                    "industrial load. Queue position, project status, and nearby infrastructure are "
                    "signals requiring utility studies, service discussions, land-use review, and "
                    "actual contractual rights. In a separately funded option exercise, an illustrative "
                    "$3,000 nonrefundable option premium plus $2,000 diligence budget creates "
                    "$5,000 direct exposure, assuming the contract permits lapse without further "
                    "purchase obligation. Neither that spending nor a possible option assignment "
                    "belongs in the equipment commission scorecard. If independently verified site "
                    "development later produces two $250,000 equipment transactions at five percent, "
                    "only their $25,000 earned commissions enter this brokerage ledger. When power "
                    "or zoning fails, let contingent options lapse or reposition the land for "
                    "independently viable uses without advertising secured capacity or promising an "
                    "energization date that the utility has not committed to deliver."
                ),
                (
                    "Control scale through throughput and exception economics rather than listing "
                    "volume. At the Base run rate, five signed mandates per monthly intake cohort "
                    "produce three eventual closings, a sixty percent mandate-to-close rate. Losing "
                    "one additional closing removes $12,500 gross commission, while much of the "
                    "inspection, acquisition, and coordination cost may already be spent. Measure "
                    "days from mandate to verified packet, verified packet to accepted offer, "
                    "accepted offer to earned commission, and earned commission to collected cash. "
                    "Keep separate reason codes for defective equipment, unsupported authority, "
                    "unreleased liens, buyer withdrawal, and uneconomic transport. A weekly owner "
                    "review should examine stale mandates, approaching payoff expiries, unmatched "
                    "receipts, and contractors carrying excessive work in progress. Automate inventory "
                    "matching and buyer alerts first because they improve search throughput without "
                    "delegating title judgments or custody of funds. Expand to the six-person Scaled "
                    "team only after observed pipeline and contribution economics support it; more "
                    "people do not cure fraudulent inventory or lumpy commissions. Maintain a "
                    "liquidity reserve for delayed closings and fund growth from collected broker "
                    "fees, not anticipated equipment principal. The operating objective is a "
                    "repeatable evidence-to-cash cycle with bounded loss exposure, not a dashboard "
                    "full of impressive machine values and unsupported expected commissions."
                ),
            ],
            "table": {
                "caption": "Seven Mapped Plays: Commission Unit Math, Evidence Requirements, and Loss Fallbacks",
                "headers": [
                    "Mapped operating play and catalog status",
                    "Illustrative commission math without double-counting equipment principal",
                    "Evidence required to make the opportunity executable",
                    "Risk fallback when the original thesis fails",
                ],
                "rows": [
                    [
                        "Lender dispositions: chapter-defined sourcing application for industrial equipment",
                        "Two completed $250,000 sales at five percent generate $25,000 commissions",
                        "Lender authority, debtor identity, payoff instructions, and asset-specific releases",
                        "Withdraw unreleasable assets and redirect buyers toward independently verified inventory",
                    ],
                    [
                        "CNC specification matching: chapter-defined technical buyer-routing application",
                        "Three completed $250,000 machine sales at five percent generate $37,500",
                        "Controller compatibility, spindle tests, tooling inventory, and buyer power requirements",
                        "Disclose inspection defects, reprice in writing, or terminate the mandate",
                    ],
                    [
                        "Fleet breakup brokerage: chapter-defined multi-unit disposition application",
                        "Four completed $125,000 vehicle sales at five percent generate $25,000",
                        "Unit-level ownership records, lien releases, diagnostics, and dealer-license classification",
                        "Sell independently cleared units only when contracts permit partial settlement",
                    ],
                    [
                        "Plant relocation brokerage: chapter-defined deadline-driven equipment disposition application",
                        "One completed $500,000 equipment package at five percent generates $25,000",
                        "Removal deadline, rigging scope, landlord access, and machine acceptance conditions",
                        "Reconfigure the package only after revising removal economics and written terms",
                    ],
                    [
                        "Inspection-led recovery: chapter-defined disclosed repricing and transaction-preservation application",
                        "Two repriced $250,000 sales at five percent produce $25,000 earned commissions",
                        "Independent findings, buyer acceptance, revised price, and amended commission calculation",
                        "Abandon unsafe or uneconomic equipment instead of hiding corrective-work requirements",
                    ],
                    [
                        "Inventory matching and buyer alerts: chapter-defined automation-assisted distribution application",
                        "Three $250,000 closings generate $37,500; alerts themselves generate no recognized revenue",
                        "Current buyer specifications, permissioned contact records, and verified available inventory",
                        "Pause stale alerts and manually review mismatches before sending further introductions",
                    ],
                    [
                        "ferc_grid_interconnection_queue_land_speculation: supplied TRACK_1 cross-track option and intelligence play",
                        "$5,000 separate option diligence exposure; two eventual equipment sales could earn $25,000",
                        "Public queue overlay, parcel rights, zoning, utility studies, and independent land-use viability",
                        "Let contingent options lapse or reposition viable land without claiming secured power",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A machine's sale price measures the transaction; verified, collected commission measures the brokerage.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Execute a commission mandate defining fee payer, earning event, payment timing, asset identity, and amendment procedures.",
        "Assemble seller-authority evidence, independent inspection findings, debtor-name lien research, and authenticated asset-release instructions.",
        "Install the six SQLite reference modules in isolation and test duplicate delivery, lock contention, overcollection, crash recovery, and backup restoration.",
        "Route equipment principal through suitable independent settlement arrangements and post only earned broker commissions to revenue.",
        "Reproduce the ninety-day bridge from $112,500 commissions and $73,125 costs to $39,375 operating generation and $69,375 ending cash.",
        "Review seven sourcing applications using distinct channel attribution, explicit loss fallbacks, and a separate boundary for land-option exposure.",
    ],
    "statutory_citations": [
        {
            "title": "UCC § 9-301 — Law Governing Perfection and Priority of Security Interests",
            "url": "https://www.law.cornell.edu/ucc/9/9-301",
            "relevance": "Determine the governing perfection jurisdiction and applicable exceptions before choosing lien-search offices; confirm the relevant state's enacted text.",
        },
        {
            "title": "UCC § 9-307 — Location of Debtor",
            "url": "https://www.law.cornell.edu/ucc/9/9-307",
            "relevance": "Identify debtor location, including registered-organization rules, rather than assuming the equipment's physical location controls every search.",
        },
        {
            "title": "UCC § 9-315 — Secured Party's Rights on Disposition of Collateral",
            "url": "https://www.law.cornell.edu/ucc/9/9-315",
            "relevance": "Evaluate whether a security interest continues after disposition and obtain effective creditor authorization or release before settlement.",
        },
        {
            "title": "UCC § 9-513 — Termination Statement",
            "url": "https://www.law.cornell.edu/ucc/9/9-513",
            "relevance": "Understand termination-statement mechanics while distinguishing termination of a filing from the transaction's required asset-specific release.",
        },
        {
            "title": "UCC § 2-313 — Express Warranties by Affirmation, Promise, Description, Sample",
            "url": "https://www.law.cornell.edu/ucc/2/2-313",
            "relevance": "Control equipment descriptions and seller promises so advertising and transaction documents do not conflict with observed condition.",
        },
        {
            "title": "UCC § 2-316 — Exclusion or Modification of Warranties",
            "url": "https://www.law.cornell.edu/ucc/2/2-316",
            "relevance": "Review the wording and presentation of seller warranty exclusions alongside express descriptions and inspection provisions.",
        },
        {
            "title": "California Vehicle Code § 11700 — Dealer Licensing Requirement",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11700.&lawCode=VEH",
            "relevance": "Classify fleet and vehicle activities against California's dealer-license requirement rather than applying stationary-equipment assumptions to every asset.",
        },
        {
            "title": "15 CFR Part 734 — Scope of the Export Administration Regulations",
            "url": "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734",
            "relevance": "Determine whether equipment and associated technology fall within EAR scope before selecting an export authorization path.",
        },
        {
            "title": "15 CFR Part 736 — General Prohibitions",
            "url": "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-736",
            "relevance": "Evaluate relevant prohibited export conduct before arranging shipment or proceeding with restricted transactions.",
        },
        {
            "title": "15 CFR Part 738 — Commerce Control List Overview and the Country Chart",
            "url": "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-738",
            "relevance": "Connect equipment classification and reasons for control to destination-based license analysis.",
        },
        {
            "title": "15 CFR Part 744 — Control Policy: End-User and End-Use Based",
            "url": "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744",
            "relevance": "Check end-user and end-use restrictions independently of an equipment classification or destination-only assessment.",
        },
        {
            "title": "18 CFR § 35.28 — Non-Discriminatory Open Access Transmission Tariff",
            "url": "https://www.ecfr.gov/current/title-18/chapter-I/subchapter-C/part-35/section-35.28",
            "relevance": "Ground interconnection and transmission context without treating public queue records as proof that a specific industrial site has secured deliverable power.",
        },
    ],
}
