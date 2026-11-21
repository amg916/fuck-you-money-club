from __future__ import annotations

_SCHEMA_MODULE = r'''
import hashlib
import json
import sqlite3
import uuid
from contextlib import contextmanager

SCHEMA = """
CREATE TABLE IF NOT EXISTS deal (
    deal_id TEXT PRIMARY KEY,
    source_key TEXT NOT NULL UNIQUE,
    asset_key TEXT NOT NULL UNIQUE,
    request_hash TEXT NOT NULL,
    stage TEXT NOT NULL CHECK (
        stage IN ('SCORED','VERIFIED','ESCROW','CLOSED','REJECTED')
    ),
    score INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    version INTEGER NOT NULL CHECK (version >= 1)
);
CREATE TABLE IF NOT EXISTS evidence (
    deal_id TEXT NOT NULL REFERENCES deal(deal_id),
    kind TEXT NOT NULL,
    digest TEXT NOT NULL CHECK (length(digest) = 64),
    reviewer TEXT NOT NULL CHECK (length(trim(reviewer)) > 0),
    PRIMARY KEY (deal_id, kind)
);
CREATE TABLE IF NOT EXISTS workflow_event (
    event_key TEXT PRIMARY KEY,
    deal_id TEXT NOT NULL REFERENCES deal(deal_id),
    request_hash TEXT NOT NULL,
    from_stage TEXT NOT NULL,
    to_stage TEXT NOT NULL,
    result_version INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS cash_event (
    source_key TEXT PRIMARY KEY,
    request_hash TEXT NOT NULL,
    effective_date TEXT NOT NULL,
    kind TEXT NOT NULL,
    deal_id TEXT REFERENCES deal(deal_id)
);
CREATE TABLE IF NOT EXISTS journal (
    source_key TEXT NOT NULL REFERENCES cash_event(source_key),
    line_number INTEGER NOT NULL,
    debit_account TEXT NOT NULL CHECK (
        debit_account IN (
            'cash','asset_basis','equity','royalty_revenue',
            'trading_gain','rights_loss','opex','deal_cost'
        )
    ),
    credit_account TEXT NOT NULL CHECK (
        credit_account IN (
            'cash','asset_basis','equity','royalty_revenue',
            'trading_gain','rights_loss','opex','deal_cost'
        )
    ),
    amount_cents INTEGER NOT NULL CHECK (
        typeof(amount_cents) = 'integer' AND amount_cents > 0
    ),
    PRIMARY KEY (source_key, line_number),
    CHECK (debit_account <> credit_account)
);
"""

def open_ledger(path=":memory:"):
    connection = sqlite3.connect(
        path, isolation_level=None, timeout=30.0
    )
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 30000")
    if path != ":memory:":
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA synchronous = FULL")
    connection.executescript(SCHEMA)
    for table in ("evidence", "workflow_event", "cash_event", "journal"):
        for operation in ("UPDATE", "DELETE"):
            name = "{}_block_{}".format(table, operation.lower())
            connection.execute(
                "CREATE TRIGGER IF NOT EXISTS {} BEFORE {} ON {} "
                "BEGIN SELECT RAISE(ABORT, 'immutable audit record'); END"
                .format(name, operation, table)
            )
    return connection

db = open_ledger()

def fingerprint(value):
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

@contextmanager
def atomic():
    db.execute("BEGIN IMMEDIATE")
    try:
        yield
        db.execute("COMMIT")
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
'''.strip()

_INTAKE_MODULE = r'''
def intake(source_key, asset_key, title_packet, operator_match,
           docket_match, price_buffer):
    flags = (title_packet, operator_match, docket_match, price_buffer)
    if any(type(value) is not bool for value in flags):
        raise ValueError("screening inputs must be explicit booleans")
    if not source_key.strip() or not asset_key.strip():
        raise ValueError("stable source and canonical asset keys required")
    payload = [source_key, asset_key] + list(flags)
    digest = fingerprint(payload)
    score = sum(
        weight for weight, passed in zip((30, 25, 20, 25), flags)
        if passed
    )
    stage = "SCORED" if score >= 70 else "REJECTED"
    with atomic():
        prior = db.execute(
            "SELECT * FROM deal WHERE source_key = ?", (source_key,)
        ).fetchone()
        if prior:
            if prior["request_hash"] != digest:
                raise ValueError("intake replay changed its payload")
            return prior["deal_id"]
        deal_id = uuid.uuid4().hex
        db.execute(
            "INSERT INTO deal VALUES (?, ?, ?, ?, ?, ?, 1)",
            (deal_id, source_key, asset_key, digest, stage, score)
        )
        db.execute(
            "INSERT INTO workflow_event VALUES (?, ?, ?, ?, ?, ?)",
            ("intake:" + source_key, deal_id, digest, "NEW", stage, 1)
        )
        return deal_id
'''.strip()

_WORKFLOW_MODULE = r'''
REQUIRED = {
    ("SCORED", "VERIFIED"): ("title", "underwriting"),
    ("SCORED", "REJECTED"): ("rejection",),
    ("VERIFIED", "ESCROW"): ("escrow",),
    ("ESCROW", "CLOSED"): ("closing",),
}

def register_evidence(deal_id, kind, digest, reviewer):
    if len(digest) != 64 or any(
        character not in "0123456789abcdef" for character in digest
    ):
        raise ValueError("provide the lowercase SHA-256 artifact digest")
    if not reviewer.strip():
        raise ValueError("named authorized reviewer required")
    with atomic():
        prior = db.execute(
            "SELECT digest, reviewer FROM evidence "
            "WHERE deal_id = ? AND kind = ?",
            (deal_id, kind)
        ).fetchone()
        if prior:
            if (prior["digest"], prior["reviewer"]) != (digest, reviewer):
                raise ValueError("immutable evidence collision")
            return
        db.execute(
            "INSERT INTO evidence VALUES (?, ?, ?, ?)",
            (deal_id, kind, digest, reviewer)
        )

def advance(event_key, deal_id, expected_version, target):
    digest = fingerprint(
        [event_key, deal_id, expected_version, target]
    )
    with atomic():
        prior = db.execute(
            "SELECT * FROM workflow_event WHERE event_key = ?",
            (event_key,)
        ).fetchone()
        if prior:
            if prior["request_hash"] != digest:
                raise ValueError("workflow replay changed its payload")
            return prior["result_version"]
        current = db.execute(
            "SELECT stage, version FROM deal WHERE deal_id = ?",
            (deal_id,)
        ).fetchone()
        if current is None:
            raise ValueError("deal does not exist")
        if current["version"] != expected_version:
            raise ValueError("stale workflow version")
        transition = (current["stage"], target)
        if transition not in REQUIRED:
            raise ValueError("unsupported state transition")
        present = {
            row["kind"] for row in db.execute(
                "SELECT kind FROM evidence WHERE deal_id = ?",
                (deal_id,)
            )
        }
        if not set(REQUIRED[transition]).issubset(present):
            raise ValueError("required reviewed evidence is missing")
        next_version = expected_version + 1
        changed = db.execute(
            "UPDATE deal SET stage = ?, version = ? "
            "WHERE deal_id = ? AND version = ? AND stage = ?",
            (target, next_version, deal_id, expected_version,
             current["stage"])
        ).rowcount
        if changed != 1:
            raise ValueError("concurrent transition refused")
        db.execute(
            "INSERT INTO workflow_event VALUES (?, ?, ?, ?, ?, ?)",
            (event_key, deal_id, digest, current["stage"],
             target, next_version)
        )
        return next_version
'''.strip()

_POSTING_MODULE = r'''
from datetime import date

def asset_balance(deal_id):
    return db.execute(
        "SELECT COALESCE(SUM("
        "CASE WHEN j.debit_account = 'asset_basis' "
        "THEN j.amount_cents ELSE 0 END - "
        "CASE WHEN j.credit_account = 'asset_basis' "
        "THEN j.amount_cents ELSE 0 END), 0) "
        "FROM journal j JOIN cash_event e USING(source_key) "
        "WHERE e.deal_id = ?",
        (deal_id,)
    ).fetchone()[0]

def post(source_key, day, kind, amount_cents,
         deal_id=None, basis_cents=0):
    if date.fromisoformat(day).isoformat() != day:
        raise ValueError("use an ISO calendar date")
    if type(amount_cents) is not int or amount_cents <= 0:
        raise ValueError("positive integer cents required")
    if type(basis_cents) is not int or basis_cents < 0:
        raise ValueError("basis must use nonnegative integer cents")
    if kind != "sale" and basis_cents != 0:
        raise ValueError("basis parameter belongs only to a sale")
    digest = fingerprint(
        [source_key, day, kind, amount_cents, deal_id, basis_cents]
    )
    with atomic():
        prior = db.execute(
            "SELECT request_hash FROM cash_event WHERE source_key = ?",
            (source_key,)
        ).fetchone()
        if prior:
            if prior["request_hash"] != digest:
                raise ValueError("cash replay changed its payload")
            return
        if kind in ("purchase", "opening_asset", "royalty", "sale"):
            deal = db.execute(
                "SELECT stage FROM deal WHERE deal_id = ?", (deal_id,)
            ).fetchone()
            if deal is None or deal["stage"] != "CLOSED":
                raise ValueError("closed ownership packet required")
        if kind in ("purchase", "opening_asset"):
            earlier = db.execute(
                "SELECT 1 FROM cash_event WHERE deal_id = ? "
                "AND kind IN ('purchase','opening_asset')",
                (deal_id,)
            ).fetchone()
            if earlier:
                raise ValueError("asset already has an acquisition entry")
        if kind == "funding":
            lines = [("cash", "equity", amount_cents)]
        elif kind == "opening_asset":
            lines = [("asset_basis", "equity", amount_cents)]
        elif kind == "purchase":
            lines = [("asset_basis", "cash", amount_cents)]
        elif kind == "royalty":
            lines = [("cash", "royalty_revenue", amount_cents)]
        elif kind == "opex":
            lines = [("opex", "cash", amount_cents)]
        elif kind == "deal_cost":
            lines = [("deal_cost", "cash", amount_cents)]
        elif kind == "sale":
            if basis_cents <= 0 or asset_balance(deal_id) != basis_cents:
                raise ValueError("sale must retire the complete recorded lot")
            recovered = min(amount_cents, basis_cents)
            lines = [("cash", "asset_basis", recovered)]
            if amount_cents > basis_cents:
                lines.append(
                    ("cash", "trading_gain", amount_cents - basis_cents)
                )
            elif amount_cents < basis_cents:
                lines.append(
                    ("rights_loss", "asset_basis",
                     basis_cents - amount_cents)
                )
        else:
            raise ValueError("unsupported posting kind")
        db.execute(
            "INSERT INTO cash_event VALUES (?, ?, ?, ?, ?)",
            (source_key, digest, day, kind, deal_id)
        )
        for number, (debit, credit, amount) in enumerate(lines, 1):
            db.execute(
                "INSERT INTO journal VALUES (?, ?, ?, ?, ?)",
                (source_key, number, debit, credit, amount)
            )
'''.strip()

_RECONCILIATION_MODULE = r'''
VIEWS = """
CREATE VIEW IF NOT EXISTS ledger_legs AS
SELECT source_key, debit_account AS account,
       amount_cents AS signed_cents
FROM journal
UNION ALL
SELECT source_key, credit_account AS account,
       -amount_cents AS signed_cents
FROM journal;

CREATE VIEW IF NOT EXISTS monthly_reconciliation AS
SELECT substr(e.effective_date, 1, 7) AS month,
       SUM(CASE WHEN l.account = 'cash'
           THEN l.signed_cents ELSE 0 END) AS cash_change_cents,
       -SUM(CASE WHEN l.account IN ('royalty_revenue','trading_gain')
           THEN l.signed_cents ELSE 0 END) AS revenue_cents,
       SUM(CASE WHEN l.account IN ('opex','deal_cost','rights_loss')
           THEN l.signed_cents ELSE 0 END) AS expense_cents,
       -SUM(CASE WHEN l.account IN (
           'royalty_revenue','trading_gain','opex',
           'deal_cost','rights_loss'
       ) THEN l.signed_cents ELSE 0 END) AS profit_cents
FROM ledger_legs l
JOIN cash_event e USING(source_key)
GROUP BY substr(e.effective_date, 1, 7);
"""

def install_views():
    db.executescript(VIEWS)

def bank_tieout(bank_closing_cents):
    if type(bank_closing_cents) is not int:
        raise ValueError("bank balance must use integer cents")
    book = db.execute(
        "SELECT COALESCE(SUM(signed_cents), 0) "
        "FROM ledger_legs WHERE account = 'cash'"
    ).fetchone()[0]
    return {
        "book_cents": book,
        "bank_cents": bank_closing_cents,
        "difference_cents": book - bank_closing_cents,
    }

install_views()
'''.strip()

_QA_MODULE = r'''
def require(condition, message):
    if not condition:
        raise AssertionError(message)

def expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError("expected a refused operation")

def fixture_closed_deal(label):
    deal_id = intake(
        "fixture-source:" + label, "fixture-asset:" + label,
        True, True, True, True
    )
    for kind in ("title", "underwriting", "escrow", "closing"):
        register_evidence(
            deal_id, kind, fingerprint(["fixture", label, kind]),
            "fixture reviewer"
        )
    for version, target in enumerate(
        ("VERIFIED", "ESCROW", "CLOSED"), 1
    ):
        advance(label + ":" + target, deal_id, version, target)
    return deal_id

def run_qa():
    global db
    original = db
    db = open_ledger()
    try:
        install_views()
        legacy = fixture_closed_deal("legacy")
        lot = fixture_closed_deal("cohort-one")
        post("fixture:funding", "2026-12-31", "funding", 10000000)
        post("fixture:legacy", "2026-12-31", "opening_asset",
             15000000, legacy)
        post("fixture:purchase", "2027-01-15", "purchase",
             6000000, lot)
        for month, royalty, prospect_cost in (
            ("01", 400000, 300000),
            ("02", 450000, 300000),
            ("03", 525000, 328125),
        ):
            post("fixture:royalty:" + month, "2027-" + month + "-28",
                 "royalty", royalty, legacy)
            post("fixture:opex:" + month, "2027-" + month + "-28",
                 "opex", 900000)
            post("fixture:prospects:" + month,
                 "2027-" + month + "-28", "deal_cost", prospect_cost)
        post("fixture:sale", "2027-03-20", "sale",
             10000000, lot, 6000000)
        count = db.execute("SELECT COUNT(*) FROM journal").fetchone()[0]
        post("fixture:sale", "2027-03-20", "sale",
             10000000, lot, 6000000)
        require(
            db.execute("SELECT COUNT(*) FROM journal").fetchone()[0]
            == count, "cash replay created extra entries"
        )
        expect_value_error(
            lambda: post("fixture:sale", "2027-03-20", "sale",
                         10000001, lot, 6000000)
        )
        expect_value_error(
            lambda: post("fixture:second-sale", "2027-03-21", "sale",
                         10000000, lot, 6000000)
        )
        expect_value_error(
            lambda: advance("fixture:stale", lot, 1, "VERIFIED")
        )
        require(
            advance("cohort-one:CLOSED", lot, 3, "CLOSED") == 4,
            "workflow replay changed its recorded result"
        )
        rows = db.execute(
            "SELECT * FROM monthly_reconciliation "
            "WHERE month BETWEEN '2027-01' AND '2027-03' "
            "ORDER BY month"
        ).fetchall()
        require(
            [row["cash_change_cents"] for row in rows]
            == [-6800000, -750000, 9296875],
            "monthly cash movement mismatch"
        )
        revenue = sum(row["revenue_cents"] for row in rows)
        expenses = sum(row["expense_cents"] for row in rows)
        profit = sum(row["profit_cents"] for row in rows)
        require(revenue == 5375000, "quarter revenue mismatch")
        require(expenses == 3628125, "quarter cost mismatch")
        require(profit == 1746875, "quarter profit mismatch")
        require(revenue * 4 == 21500000, "annual revenue mismatch")
        require(profit * 4 == 6987500, "annual owner profit mismatch")
        require(profit * 1000 == revenue * 325, "margin mismatch")
        require(asset_balance(lot) == 0, "sold lot retained basis")
        require(asset_balance(legacy) == 15000000,
                "legacy asset basis changed")
        require(bank_tieout(11746875)["difference_cents"] == 0,
                "closing bank balance mismatch")
        require(
            db.execute(
                "SELECT COALESCE(SUM(signed_cents), 0) FROM ledger_legs"
            ).fetchone()[0] == 0,
            "double-entry trial balance mismatch"
        )
        require(
            not db.execute("PRAGMA foreign_key_check").fetchall(),
            "foreign key integrity failure"
        )
        return {
            "quarter_revenue_cents": revenue,
            "quarter_profit_cents": profit,
            "closing_cash_cents": 11746875,
        }
    finally:
        db.close()
        db = original

# Run only after concatenating the six reference modules in order.
# This fixture uses a separate in-memory database.
# Invoke run_qa() explicitly; importing these snippets runs no fixture.
'''.strip()


CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "mineral-rights-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": (
        "How does an operator execute mineral rights end-to-end from intake "
        "to reconciled cash, backed by an auditable technical/ledger blueprint "
        "and a worked 90-day cohort walk?"
    ),
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": (
        "The Complete Operating Process, Production Blueprint & "
        "90-Day Cohort Walk"
    ),
    "subtitle": (
        "NMA and NPRI Title Chains, OCC Pooling Dockets, SQLite Audit Trails, "
        "Texas Payment Rules, Escrow Evidence, and Institutional Exit Math"
    ),
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #7, Mineral Rights, holds Rank #23 with a 63/100 "
        "Money-to-Manpower Score because capital, title work, and depletion "
        "constrain throughput. This chapter maps five operating plays: severed-mineral "
        "aggregation, NPRI yield acquisition, pooling-docket curve-jumping, royalty "
        "recovery, and institutional flips. A 1 FT + 3 C pod converts recorded "
        "instruments into reviewed ownership, controlled closings, and reconciled "
        "receipts using six executable SQLite reference modules. The mature-book "
        "90-day walk separates $60,000 returned basis from $40,000 realized gain "
        "and reaches the Base annual run rate without counting sale proceeds twice. "
        "Canonical annual owner profits remain $6,000 Conservative, $69,875 Base, "
        "and $180,000 Scaled. The controls target three recurring losses: buying "
        "the wrong interest, paying for speculative production, and treating "
        "unmatched cash as earned revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$30,000",
            "context": (
                "Annual royalty receipts and realized rights-trading gains; "
                "returned basis excluded"
            ),
            "note": "20% margin; $6,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$215,000",
            "context": (
                "Annual royalty receipts and realized rights-trading gains; "
                "returned basis excluded"
            ),
            "note": "32.5% margin; $69,875 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$400,000",
            "context": (
                "Annual royalty receipts and realized rights-trading gains; "
                "returned basis excluded"
            ),
            "note": "45% margin; $180,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": (
                "1. Convert Five Mineral Plays into One Capacity-Limited Deal Queue"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one economic-interest record, not one mailing-list row. "
                    "The full-time principal owns pricing, capital allocation, seller "
                    "communication, and the final cash tie-out. Three contractors provide "
                    "land and title research, petroleum engineering, and bookkeeping; "
                    "specialist counsel is purchased within the title contractor's scoped "
                    "engagement rather than silently adding another permanent seat. Map "
                    "each opportunity to five explicit work lanes: severed-mineral "
                    "aggregation purchases fragmented NMA; NPRI yield acquisition buys "
                    "documented nonparticipating royalty cash flows; pooling-docket "
                    "curve-jumping prices public development changes; royalty recovery "
                    "corrects receipts on owned interests; institutional flips assemble "
                    "transferable packages for larger buyers. One parcel can serve several "
                    "lanes, but it receives one asset identity and one allocated basis. "
                    "Maintain separate gross acres, fractional mineral ownership, net "
                    "mineral acres, royalty burden, depth limits, and effective dates. "
                    "Never express an NPRI as NMA without preserving the instrument's "
                    "actual royalty definition. An asset key combines jurisdiction, "
                    "recorded vesting instrument, tract, depth interval, and interest "
                    "fraction. A normalized seller name alone cannot establish ownership "
                    "or prevent duplicate purchases. Cap simultaneous title examinations "
                    "at the contractor's documented weekly capacity, and require a "
                    "specific reason whenever the principal advances a lower-ranked file "
                    "ahead of a complete one."
                ),
                (
                    "Build the ownership packet from county records before using a "
                    "spreadsheet decimal to quote a price. Preserve deeds, reservations, "
                    "probate orders, assignments, leases, amendments, and relevant pooling "
                    "orders with document dates and retrieval provenance. Texas Property "
                    "Code §13.001 makes recording status consequential for priority; "
                    "recording a document does not independently establish that the "
                    "grantor owned the interest conveyed. The title reviewer must resolve "
                    "severances, executive rights, NPRI burdens, and depth restrictions "
                    "against the specific conveyance. For a simple area-proportional unit "
                    "with uniform ownership and no competing burdens, twenty NMA in a "
                    "640-acre unit at a one-fifth lease royalty produces a 0.00625 "
                    "decimal: 20 divided by 640 multiplied by 0.20. That illustration "
                    "is not a substitute for horizontal allocation language, tract "
                    "participation factors, or an instrument-specific NPRI calculation. "
                    "Compare the supported decimal with the operator's division-order "
                    "decimal and investigate differences before signing. Use Texas RRC "
                    "well and production records, Oklahoma Corporation Commission "
                    "dockets, and county indexes as distinct evidence sources. Enverus "
                    "or other licensed aggregators can accelerate screening, but an "
                    "aggregator's ownership estimate never replaces the recorded chain. "
                    "Store the exact downloaded artifact, not merely a search-results "
                    "URL that may change next week."
                ),
                (
                    "Translate each lane into an explicit acquisition thesis and failure "
                    "condition. Aggregation requires contiguous economic usefulness to a "
                    "buyer, not simply many small deeds. NPRI yield underwriting requires "
                    "lease-specific deduction treatment and a defensible production "
                    "forecast. Docket curve-jumping requires a public filing, tract match, "
                    "procedural status, and pricing that survives delayed drilling; a "
                    "pooling application is neither a completed well nor a royalty "
                    "payment. Recovery work requires an owned receivable supported by "
                    "statements, not a projected benefit counted immediately as revenue. "
                    "An institutional flip requires transferable title, a buyer's "
                    "document checklist, and enough spread after acquisition basis and "
                    "selling costs. The engineer builds a monthly decline case using "
                    "well age, downtime, product mix, realized differentials, deductions, "
                    "and plausible abandonment timing. The principal then prices the "
                    "asset against a delayed-development case rather than paying today's "
                    "price for an optimistic permit narrative. Allocate contractor "
                    "hours to exceptions: disputed title, anomalous decimals, and "
                    "material forecast variance. Routine data collection should be "
                    "batched. The canonical 6–24 month time to first deal remains the "
                    "startup expectation; the later 90-day example describes a mature "
                    "book and prepared pipeline, not an accelerated promise for a new "
                    "entrant. Rejecting an attractive headline yield is productive "
                    "when its title or depletion assumptions cannot survive examination."
                ),
            ],
            "table": {
                "caption": (
                    "Five-Play Routing and Ownership Evidence Matrix for the "
                    "1 FT + 3 C Mineral Pod"
                ),
                "headers": [
                    "Work lane or control",
                    "Required source and calculation",
                    "Accountable pod handoff",
                    "Stop condition and retained evidence",
                ],
                "rows": [
                    [
                        "Severed-mineral aggregation across a defined acquisition area",
                        "County vesting chain supports tract fractions and depth intervals",
                        "Land contractor presents consolidated ownership to full-time principal",
                        "Stop purchases when conveyances leave material ownership gaps unresolved",
                    ],
                    [
                        "NPRI yield acquisition using instrument-specific royalty language",
                        "Read fixed versus floating fractions against operative lease terms",
                        "Title contractor resolves interpretation before engineer forecasts receipts",
                        "Retain marked instruments explaining every decimal assumption and burden",
                    ],
                    [
                        "Pooling-docket curve-jumping using public development evidence only",
                        "Match OCC application lands, amendments, orders, and procedural dates",
                        "Engineer separates development probability from current producing reserves",
                        "Stop repricing when tract identity or procedural status remains disputed",
                    ],
                    [
                        "Royalty recovery for already owned and documented interests",
                        "Match operator statements, supported decimals, suspense notices, and deposits",
                        "Bookkeeping contractor prepares exceptions for principal's operator correspondence",
                        "Count recovered receipts only after supported settlement reaches the ledger",
                    ],
                    [
                        "Institutional flips assembled around transferable buyer-ready mineral packages",
                        "Buyer diligence list identifies acceptable title, geography, and production",
                        "Principal owns negotiation while title contractor prepares indexed evidence",
                        "Reject bids whose contingencies transfer unlimited cure expense backward",
                    ],
                    [
                        "Shared ownership identity across all five acquisition lanes",
                        "Canonical keys preserve jurisdiction, instrument, tract, depths, and fraction",
                        "Land contractor proposes identity; principal resolves duplicate-interest exceptions",
                        "Quarantine collisions rather than inserting a second purchase candidate",
                    ],
                    [
                        "Shared depletion and commodity downside review before pricing",
                        "Engineer models monthly volumes, downtime, realized prices, and deductions",
                        "Principal sets maximum purchase basis from stressed cash receipts",
                        "Retain forecast versions explaining changed assumptions and valuation movement",
                    ],
                    [
                        "Shared capital and contractor capacity allocation across active files",
                        "Weekly queue measures committed dollars and remaining specialist hours",
                        "Principal sequences work against available cash and reviewed capacity",
                        "Suspend new commitments before existing closings consume reserved liquidity",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Win Through Better Interest Definition, Not Faster Mailing",
                "body": (
                    "Experienced mineral buyers shorten the exception queue before "
                    "increasing lead volume."
                ),
                "items": [
                    (
                        "Maintain a separate NPRI interpretation worksheet showing whether "
                        "the fraction applies to production or to the lease royalty; "
                        "never bury that distinction inside an NMA column."
                    ),
                    (
                        "Archive OCC docket amendments beside the original application; "
                        "changed lands or relief can erase the supposed pricing edge."
                    ),
                    (
                        "Ask prospective institutional buyers for their current title "
                        "and geography requirements before buying an aggregation parcel."
                    ),
                    (
                        "Compare statement production months, not deposit months, when "
                        "diagnosing decline; payment lag can imitate a production collapse."
                    ),
                ],
            },
        },
        {
            "heading": (
                "2. Build the Six-Module Ledger Before Increasing Acquisition Volume"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the six reference modules in table order as one Python 3.9 "
                    "script. They depend only on the standard library and initialize "
                    "an isolated in-memory SQLite ledger; choose a durable local file "
                    "through open_ledger when implementing the reviewed design. Keep "
                    "SQLite on a local filesystem, use one connection per worker, "
                    "and serialize mutations with BEGIN IMMEDIATE. Concurrent writers "
                    "either acquire the write lock or fail without a partial commit. "
                    "UNIQUE constraints protect source identities and economic-interest "
                    "identities, while request hashes reject a reused key carrying "
                    "different data. Workflow updates additionally compare both the "
                    "expected version and current stage. These controls eliminate "
                    "check-then-write races within the reference mutation paths; "
                    "they do not turn direct database access into an authenticated "
                    "application. Restrict filesystem access, expose only authorized "
                    "operations, and preserve reviewed deployment migrations. A timeout "
                    "is a retryable failure using the identical event key, never "
                    "permission to generate a replacement transaction identity. Hash "
                    "the actual evidence artifact before registration and retain its "
                    "retrievable location in the surrounding document index. The "
                    "reference stores the digest and reviewer, not private deed "
                    "contents. Immutable audit rows detect accidental mutation; "
                    "separately retained backups are still necessary against database "
                    "replacement or privileged tampering."
                ),
                (
                    "The ledger uses integer cents and balanced account pairs rather "
                    "than binary floating-point amounts or an editable revenue total. "
                    "Each journal row contains one equal debit and credit, and every "
                    "cash event plus all associated rows commits atomically. An "
                    "acquisition debits asset basis and credits cash. A profitable "
                    "sale credits basis only for the retired investment and credits "
                    "trading gain for the excess; a below-basis sale separately "
                    "records rights loss. The implementation deliberately supports "
                    "complete-lot dispositions, so a partial assignment must first "
                    "receive a reviewed allocation design rather than slipping "
                    "through an unsupported parameter. Opening contributed assets "
                    "and equity funding are balance-sheet entries, not operator "
                    "revenue. The management view recognizes supported royalty "
                    "receipts on collection and realized sale gains on settlement. "
                    "Maintain a separate tax and accrual workpaper for depletion, "
                    "withholding, receivables, and jurisdiction-specific treatment; "
                    "26 U.S.C. §§611–612 make depletion and adjusted basis substantive "
                    "accounting topics. Successful acquisition costs that belong "
                    "in basis must be included in the acquired lot's recorded "
                    "amount. The cohort's separate prospect costs concern abandoned "
                    "searches and screening rather than the purchased lot. This "
                    "distinction keeps the sale spread, operating expenses, and "
                    "returned investment from being counted inconsistently."
                ),
                (
                    "Treat workflow state as evidence of an operational decision, "
                    "not as an instruction to move money. SCORED means the screening "
                    "inputs passed a routing threshold; VERIFIED requires reviewed "
                    "title and underwriting artifacts; ESCROW requires escrow "
                    "instructions; CLOSED requires the completed closing packet. "
                    "The reference makes no external payment calls and therefore "
                    "cannot create a bank-side retry race. Record a settlement "
                    "only after independent bank and escrow evidence establishes "
                    "its occurrence. If a later integration initiates payments, "
                    "add a durable outbox, a provider-supported idempotency key, "
                    "and status recovery before enabling dispatch; a local SQL "
                    "transaction alone cannot ensure exactly-once external effects. "
                    "The QA module creates its own database, exercises replay "
                    "and conflict behavior, retires the sold basis, and checks "
                    "quarterly revenue, expenses, profit, and ending cash. It is "
                    "a runnable fixture, not evidence that an installed system "
                    "has passed testing. Extend deployment tests with two "
                    "independent connections contending for the same transition "
                    "and transaction key, process interruption before commit, "
                    "and restoration from backup. The bookkeeper owns exception "
                    "reports; the principal owns clearing them. Retain the "
                    "original bank transaction identifier as the source key "
                    "so reimporting a statement cannot manufacture another receipt."
                ),
            ],
            "table": {
                "caption": (
                    "Production Engineering / SQLite Ledger & Idempotent Workflow "
                    "Reference Table — Six Copy-Pasteable Modules"
                ),
                "headers": [
                    "Module and execution order",
                    "Runnable Python and embedded SQL",
                    "Mineral operating boundary",
                    "Invariant and acceptance evidence",
                ],
                "rows": [
                    [
                        "Module one establishes schema, immutable records, and transaction boundaries",
                        _SCHEMA_MODULE,
                        "Use local SQLite storage with one connection per worker",
                        "Unique identities and immediate transactions serialize every supported mutation",
                    ],
                    [
                        "Module two imports canonical interests and scores documented screening inputs",
                        _INTAKE_MODULE,
                        "The screening score routes work without establishing title or value",
                        "Identical replays return the existing deal; changed payloads fail",
                    ],
                    [
                        "Module three registers reviewed artifacts and advances escrow evidence states",
                        _WORKFLOW_MODULE,
                        "Named reviewers attest evidence through separately authenticated operating procedures",
                        "Version comparison and required evidence prevent stale or incomplete transitions",
                    ],
                    [
                        "Module four posts balanced receipts, purchases, full-lot sales, and costs",
                        _POSTING_MODULE,
                        "Settlement records describe completed events without initiating external money movement",
                        "Atomic account pairs exclude returned basis from recognized trading revenue",
                    ],
                    [
                        "Module five exposes monthly reconciliation and independent bank balance comparison",
                        _RECONCILIATION_MODULE,
                        "Collected royalty management reporting remains separate from tax depletion workpapers",
                        "Revenue, expense, cash movement, and bank differences remain independently visible",
                    ],
                    [
                        "Module six runs isolated replay, basis, trial-balance, and cohort checks",
                        _QA_MODULE,
                        "Synthetic evidence belongs only to the separate fixture database",
                        "Expected quarter and annual arithmetic are asserted without touching production",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the canonical interest and freeze intake inputs",
                    "action": (
                        "Normalize the tract and instrument identity, then call intake "
                        "with a stable source key and reviewed screening flags."
                    ),
                    "detail": (
                        "Resolve asset-key collisions manually; preserve the original "
                        "request rather than changing an idempotent replay."
                    ),
                },
                {
                    "step": 2,
                    "title": "Register reviewed evidence before advancing the file",
                    "action": (
                        "Hash the actual title and engineering packets and register "
                        "their authorized reviewers before calling advance."
                    ),
                    "detail": (
                        "Supply the current version and a durable event key; refusal "
                        "leaves both stage and audit records unchanged."
                    ),
                },
                {
                    "step": 3,
                    "title": "Close externally and post the independently observed settlement",
                    "action": (
                        "Complete authorized escrow procedures, register closing evidence, "
                        "and post acquisition or receipt entries from bank identifiers."
                    ),
                    "detail": (
                        "The reference never sends funds; cash entries follow bank "
                        "and escrow confirmation, not a workflow button."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile the book and preserve the close package",
                    "action": (
                        "Run the monthly view, compare bank closing cash, investigate "
                        "all differences, and retain an immutable period export."
                    ),
                    "detail": (
                        "Retain statement-level royalty allocations and the sold-lot "
                        "basis workpaper beside the general ledger."
                    ),
                },
            ],
        },
        {
            "heading": (
                "3. Execute Closing, Production Monitoring, and Receipt Recovery "
                "Without Losing the Chain"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Before any wire, the principal reviews a compact closing packet "
                    "with the purchase agreement, conveyance, ownership schedule, "
                    "resolved exceptions, settlement statement, and independently "
                    "verified payee instructions. The land contractor confirms that "
                    "the deed's legal description and reserved rights match the "
                    "priced interest, including depths and effective dates. The "
                    "engineer confirms that the acquired interval actually "
                    "participates in the modeled wells. The bookkeeper checks "
                    "that allocated purchase basis equals the closing schedule "
                    "and that no earlier event already recorded the same "
                    "settlement. Verify changed wire instructions using an "
                    "established contact channel, not the telephone number "
                    "inside the change request. Record conveyances promptly "
                    "under the applicable county process and preserve acceptance "
                    "and instrument numbers. Escrow release conditions must "
                    "identify the required executed instruments and delivery "
                    "evidence; a generic email saying title is clean is "
                    "insufficient. Existing tax liens, probate limitations, "
                    "and conflicting assignments require issue-specific "
                    "resolution. The four-person pod stays efficient by "
                    "presenting one indexed exception schedule rather than "
                    "circulating multiple contradictory checklists. No participant "
                    "should silently change the purchased fraction after "
                    "pricing. A material scope change returns the file "
                    "to reviewed underwriting and a documented revised "
                    "agreement before the external closing proceeds."
                ),
                (
                    "After closing, submit the operator's ownership-transfer package "
                    "and track each payor's acknowledgment, required tax form, "
                    "division-order status, and suspense reason. Texas Natural "
                    "Resources Code §91.402 specifies payment timing with "
                    "enumerated circumstances permitting withholding; §91.403 "
                    "addresses interest on late payments subject to its "
                    "terms. Build jurisdiction-specific deadline fields instead "
                    "of applying a universal countdown. Royalty automation "
                    "should normalize payor, property, API identifier, product, "
                    "production month, decimal, volume, price, deductions, "
                    "tax withholding, and net remittance. Oil and gas "
                    "measurement units must remain explicit. Match the "
                    "statement total to the deposit, then explain allocation "
                    "differences across properties. The reference general "
                    "ledger records the supported collected amount; its "
                    "statement subledger must preserve gross-to-net detail "
                    "for later accounting classification. Use EnergyLink "
                    "where the payor supports it, and retain the "
                    "original statement rather than trusting an extracted "
                    "CSV alone. Reconciliation exceptions should distinguish "
                    "missing statements, duplicate deposits, stale ownership, "
                    "decimal disagreement, and revised production periods. "
                    "A recovery estimate remains an exception balance "
                    "until the payor resolves it and the relevant "
                    "receipt arrives. This prevents the royalty-recovery "
                    "play from inflating the same month's cash, "
                    "revenue, and projected sale value simultaneously."
                ),
                (
                    "Run production monitoring monthly, but route only material "
                    "exceptions to the engineer. Compare observed volumes "
                    "with the acquisition forecast after aligning reporting "
                    "months and accounting for revisions. A lower royalty "
                    "check can reflect price, downtime, deductions, payment "
                    "lag, or ownership changes; it does not automatically "
                    "prove reservoir decline. Preserve forecast versions "
                    "and document whether a change alters hold value, "
                    "sale timing, or reserve cash. Institutional buyers "
                    "should receive an indexed package containing the "
                    "supported interest schedule, recorded instruments, "
                    "payor history, production series, deductions analysis, "
                    "and unresolved exceptions. Avoid advertising a "
                    "pooling application as booked production. Before "
                    "a flip closes, reconcile the sale perimeter "
                    "to the acquisition lot and confirm that "
                    "the ledger can retire exactly that basis; "
                    "partial dispositions need an allocation extension "
                    "outside the reference implementation. If outside "
                    "capital is pooled, evaluate the offering structure "
                    "before soliciting investors: 15 U.S.C. §77b(a)(1) "
                    "includes fractional undivided interests in oil, "
                    "gas, or other mineral rights within its "
                    "security definition. An entity wrapper does "
                    "not itself settle the analysis. Keep asset "
                    "operations separate from investor subscriptions "
                    "and distributions, and obtain a structure-specific "
                    "review before accepting funds."
                ),
            ],
            "table": {
                "caption": (
                    "Closing-to-Cash Forensic Controls and Named Evidence Sources"
                ),
                "headers": [
                    "Observed event or failure",
                    "Evidence and concrete operator test",
                    "Assigned response within the existing pod",
                    "Ledger and release treatment",
                ],
                "rows": [
                    [
                        "Seller changes bank instructions immediately before scheduled escrow release",
                        "Independently call the established contact and compare settlement beneficiaries",
                        "Principal pauses external authorization while escrow confirms authenticated instructions",
                        "Record no payment event until independently supported settlement actually occurs",
                    ],
                    [
                        "Recorded deed reserves depths included in the acquisition forecast",
                        "Compare executed reservation language against the engineer's well interval mapping",
                        "Title contractor and engineer resolve the purchased perimeter together",
                        "Revise underwriting before closing rather than changing basis labels afterward",
                    ],
                    [
                        "Operator division-order decimal differs from the reviewed ownership calculation",
                        "Trace lease royalty, tract participation, NPRI burdens, and effective dates",
                        "Land contractor assembles the calculation; principal coordinates payor correction",
                        "Preserve disputed amounts outside collected revenue until supported receipts arrive",
                    ],
                    [
                        "EnergyLink statement total does not match the observed bank deposit",
                        "Compare remittance identifier, payor adjustments, withholding, and multiple-property allocations",
                        "Bookkeeping contractor opens one exception tied to the bank identifier",
                        "Post supported collected cash once and retain the allocation workpaper",
                    ],
                    [
                        "Texas royalty payment arrives beyond the applicable statutory payment period",
                        "Review Texas Natural Resources Code payment exceptions and interest provisions",
                        "Principal sends documented correspondence using contractor-prepared ownership and timing evidence",
                        "Recognize collected recoveries separately from estimates and unresolved suspense balances",
                    ],
                    [
                        "Institutional exit package omits part of the acquired mineral lot",
                        "Reconcile buyer interest schedule against recorded acquisitions and remaining basis",
                        "Principal obtains reviewed allocation mechanics before accepting partial-disposition settlement",
                        "Reference posting refuses unsupported partial basis retirement and duplicate sales",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Verifications Before Capital Leaves Escrow",
                "body": (
                    "Require affirmative evidence for each check; an attractive price "
                    "does not compensate for an unverified purchased interest."
                ),
                "items": [
                    (
                        "Title identity: match grantor authority, legal description, "
                        "depths, reservations, and fractional interest to the signed "
                        "purchase schedule and reviewed title packet."
                    ),
                    (
                        "Economic identity: independently reproduce the modeled decimal, "
                        "decline assumptions, deduction treatment, and delayed-development "
                        "purchase ceiling."
                    ),
                    (
                        "Settlement identity: verify escrow instructions and beneficiary "
                        "details through an established channel and reconcile the "
                        "settlement statement to available capital."
                    ),
                    (
                        "Ledger identity: confirm unique asset and settlement keys, "
                        "reviewed basis allocation, current workflow version, and "
                        "retrievable closing evidence before posting."
                    ),
                ],
            },
        },
        {
            "heading": (
                "4. Walk a Mature 90-Day Cohort from Lead Scrubs to Base-Case Cash"
            ),
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The worked cohort begins after the business has established "
                    "a producing book and a prepared acquisition pipeline. "
                    "Opening assets are $100,000 unrestricted cash and "
                    "$150,000 contributed mineral basis, representing $250,000 "
                    "of capital within the canonical $150,000–$2,000,000 "
                    "startup range. Opening equity is not revenue. "
                    "The existing book produces collected royalties of "
                    "$4,000, $4,500, and $5,250 across three months. "
                    "Month 1 also closes a fully prepared $60,000 "
                    "mineral lot, including its capitalizable acquisition "
                    "costs; Month 3 sells the entire lot for "
                    "$100,000. Its $60,000 returned basis replenishes "
                    "capital, while only the $40,000 realized gain "
                    "enters scorecard revenue. The 54 newly logged "
                    "leads support continuing pipeline work, but the "
                    "illustration does not assert that cold intake "
                    "produced a fully reviewed institutional exit "
                    "inside ninety days. The purchased lot belongs "
                    "to Month 1's tracked cohort because its "
                    "closing enters this operating window; its "
                    "preparation predates the window. Use explicit "
                    "origination, intake, verification, purchase, and "
                    "sale dates in the operating workbook so "
                    "a fast closing cannot conceal a long "
                    "development history. The ledger fixture models "
                    "the existing book and closed lot; the "
                    "cohort register separately tracks unpurchased prospects."
                ),
                (
                    "Month 1 logs eighteen opportunities: nine fail initial "
                    "screening, six fail documented title review, two "
                    "remain repricing files, and one prepared lot "
                    "closes. Month 2 logs eighteen more: nine "
                    "fail screening, six remain in title remediation, "
                    "and three enter the bid queue without "
                    "a purchase commitment. Month 3 logs eighteen: "
                    "ten fail screening, five remain in title "
                    "remediation, and three enter the bid queue. "
                    "These dispositions total 54 without inventing "
                    "additional acquisitions. Rejected prospects have "
                    "no acquired asset basis; their actual "
                    "search expense remains visible. Each month "
                    "carries $9,000 recurring operating expense, "
                    "within the canonical $1,000–$12,000 monthly "
                    "opex range. Additional abandoned-prospect and "
                    "screening costs are $3,000, $3,000, and "
                    "$3,281.25. Those costs are separate from "
                    "recurring opex and from the purchased "
                    "lot's capitalized basis. The resulting quarter "
                    "has $27,000 recurring opex plus $9,281.25 "
                    "prospect expense, totaling $36,281.25. The "
                    "principal and three contractors must fit "
                    "their actual workload and charges inside "
                    "those budgets; the headcount labels do "
                    "not create free specialist capacity. The "
                    "quarter's cash low point is $24,500 "
                    "at Month 2 close, before the "
                    "institutional buyer's settlement replenishes liquidity."
                ),
                (
                    "Reconcile the quarter in two independent directions. Revenue "
                    "is $13,750 collected royalties plus $40,000 realized "
                    "trading gain, totaling $53,750. Subtract $36,281.25 "
                    "costs to obtain $17,468.75 owner profit, "
                    "exactly 32.5% of recognized revenue. Cash "
                    "starts at $100,000, receives $13,750 royalties "
                    "and $100,000 sale proceeds, and pays "
                    "$60,000 acquisition basis plus $36,281.25 "
                    "costs, ending at $117,468.75. The acquired "
                    "and sold lot has zero remaining basis; "
                    "the opening mineral book retains $150,000 "
                    "before separately assessed depletion adjustments. "
                    "Four equivalent operating quarters produce "
                    "$215,000 revenue, $145,125 costs, and "
                    "$69,875 annual owner net profit. This "
                    "is a run-rate reconciliation, not a "
                    "claim that seasonal receipts or institutional "
                    "closings arrive evenly. If the sale "
                    "slips beyond Day 90, the same "
                    "quarter ends with $17,468.75 cash, "
                    "$60,000 unsold lot basis, and a "
                    "$22,531.25 operating loss before any "
                    "impairment assessment. No projected exit "
                    "gain fills that gap. Preserve this "
                    "liquidity stress alongside the canonical "
                    "Conservative $6,000, Base $69,875, and "
                    "Scaled $180,000 annual profit cases. "
                    "Scaling to 2 FT + 4 C "
                    "requires additional verified throughput, not "
                    "counting returned principal as higher revenue."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and cohort identity",
                    "Lead disposition and acquired basis",
                    "Collected cash and recognized operator revenue",
                    "Operating expense and recognized owner result",
                    "Net movement and cumulative cash position",
                ],
                "rows": [
                    [
                        "Month 1 opens with $100,000 unrestricted operating cash",
                        "Eighteen leads: nine screening rejects, six title rejects, two repricing files, one prepared $60,000 purchase",
                        "Collect $4,000 legacy royalties; recognized revenue equals $4,000 only",
                        "Pay $9,000 recurring opex and $3,000 prospect costs; owner result is negative $8,000",
                        "Pay $60,000 acquisition; net cash negative $68,000; cumulative movement negative $68,000; closing cash $32,000",
                    ],
                    [
                        "Month 2 continues existing-book collections without another acquisition",
                        "Eighteen leads: nine screening rejects, six title-remediation files, three uncommitted bids",
                        "Collect $4,500 legacy royalties; recognized revenue equals $4,500 only",
                        "Pay $9,000 recurring opex and $3,000 prospect costs; owner result is negative $7,500",
                        "Net cash negative $7,500; cumulative movement negative $75,500; closing cash $24,500",
                    ],
                    [
                        "Month 3 closes the previously acquired institutional exit",
                        "Eighteen leads: ten screening rejects, five title-remediation files, three uncommitted bids",
                        "Collect $5,250 royalties and $100,000 sale proceeds; recognized revenue $45,250 excludes $60,000 returned basis",
                        "Pay $9,000 recurring opex and $3,281.25 prospect costs; owner profit equals $32,968.75",
                        "Net cash positive $92,968.75; cumulative movement positive $17,468.75; closing cash $117,468.75",
                    ],
                    [
                        "Quarter close reconciles all three distinct tracked cohorts",
                        "Fifty-four leads contain one acquisition and one complete-lot disposition; sold basis becomes zero",
                        "Collected cash totals $113,750; recognized revenue totals $53,750 after excluding returned basis",
                        "Recurring opex $27,000 plus prospect costs $9,281.25 yields $17,468.75 owner profit",
                        "Opening cash $100,000 plus cumulative movement $17,468.75 equals closing cash $117,468.75",
                    ],
                    [
                        "Annual equivalent repeats four comparable mature operating quarters",
                        "Four equivalent $60,000 acquisitions and complete-lot exits recycle $240,000 total basis",
                        "Royalty receipts $55,000 plus realized gains $160,000 equal canonical revenue $215,000",
                        "Costs $145,125 leave canonical owner profit $69,875 at exactly 32.5% margin",
                        "Without distributions or other changes, annual cash increases $69,875 from the same opening position",
                    ],
                    [
                        "Delayed-exit stress keeps the Month 3 sale outside ninety days",
                        "Retain the unsold $60,000 lot while continuing all stated prospect scrubs and expenses",
                        "Collect only $13,750 royalties; no sale proceeds or realized trading gain enters this quarter",
                        "Unchanged $36,281.25 costs create negative $22,531.25 owner result before impairment assessment",
                        "Cumulative cash movement negative $82,531.25 leaves $17,468.75 cash and the unsold acquired basis",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Buy the interest the deed actually conveys, and count only the "
        "cash economics the ledger can reconcile."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        (
            "Assign every opportunity to the five operating lanes and establish "
            "a canonical jurisdiction–instrument–tract–depth–fraction identity "
            "before requesting another title search."
        ),
        (
            "Build a reviewed title and decimal packet that separates NMA, "
            "NPRI language, lease royalty, unit participation, and effective dates."
        ),
        (
            "Concatenate the six reference modules, invoke run_qa() in a "
            "controlled environment, and add deployment-specific concurrency, "
            "backup-restoration, and authorization tests before live use."
        ),
        (
            "Require independent settlement verification, current workflow "
            "versions, reviewed evidence hashes, and stable bank event keys "
            "before posting a completed closing."
        ),
        (
            "Reconcile each royalty deposit to its original statement and "
            "property allocations, then route decimal, suspense, production, "
            "and withholding exceptions to the responsible contractor."
        ),
        (
            "Reproduce the $53,750 quarterly revenue, $17,468.75 quarterly "
            "profit, and $117,468.75 ending cash bridge while retaining the "
            "delayed-sale liquidity stress beside the Base run rate."
        ),
    ],
    "statutory_citations": [
        {
            "title": "Texas Property Code §13.001 — Validity of Unrecorded Instrument",
            "url": (
                "https://statutes.capitol.texas.gov/Docs/PR/htm/"
                "PR.13.htm#13.001"
            ),
            "relevance": (
                "Recording and notice affect priority; preserve county recording "
                "evidence while separately examining the grantor's actual title."
            ),
        },
        {
            "title": (
                "Texas Natural Resources Code §91.402 — Time for Payment of Proceeds"
            ),
            "url": (
                "https://statutes.capitol.texas.gov/Docs/NR/htm/"
                "NR.91.htm#91.402"
            ),
            "relevance": (
                "Build Texas payor follow-up dates and suspense reviews around "
                "the applicable payment rules and stated withholding exceptions."
            ),
        },
        {
            "title": (
                "Texas Natural Resources Code §91.403 — Payment of Interest "
                "on Late Payments"
            ),
            "url": (
                "https://statutes.capitol.texas.gov/Docs/NR/htm/"
                "NR.91.htm#91.403"
            ),
            "relevance": (
                "Evaluate supported late-payment interest separately from "
                "unresolved recovery estimates and recognize actual collections."
            ),
        },
        {
            "title": "26 U.S.C. §611 — Allowance of Deduction for Depletion",
            "url": "https://www.law.cornell.edu/uscode/text/26/611",
            "relevance": (
                "Maintain depletion workpapers separately from the chapter's "
                "collected-receipt management ledger and cash reconciliation."
            ),
        },
        {
            "title": "26 U.S.C. §612 — Basis for Cost Depletion",
            "url": "https://www.law.cornell.edu/uscode/text/26/612",
            "relevance": (
                "Preserve adjusted-basis support rather than treating acquisition "
                "principal, sale proceeds, and taxable depletion as interchangeable."
            ),
        },
        {
            "title": "15 U.S.C. §77b(a)(1) — Definition of Security",
            "url": "https://www.law.cornell.edu/uscode/text/15/77b",
            "relevance": (
                "The definition includes fractional undivided mineral interests; "
                "review proposed pooled offerings before soliciting outside capital."
            ),
        },
    ],
}
