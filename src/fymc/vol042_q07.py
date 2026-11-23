from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort-walk",
    "question_prompt": "How does an operator execute cell-tower, digital-billboard & ios lease arbitrage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "FCC ASR and DOT AADT Intake, Lender SNDA Evidence, SQLite Settlement Controls, and Retained-Spread Cash Reconciliation",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #42, ranked #11 of 42 with a 91/100 Money-to-Manpower "
        "Score, turns infrastructure rights into documented retained spreads "
        "rather than treating property values or institutional purchase principal "
        "as revenue. This chapter connects that execution system to the shelf's "
        "11 mapped plays, including property-tax assessment appeal contingency. "
        "Follow parcel intake through verified authority, assignable contracts, "
        "escrow evidence, balanced ledger entries, and bank reconciliation. Six "
        "copy-pasteable reference modules implement serialized SQLite writes and "
        "content-checked retries. A worked 90-day cohort produces $133,750 retained "
        "revenue, $80,250 operating costs, and $53,500 owner profit. Four equivalent "
        "quarterly production blocks reconcile to the $214,000 Base annual profit; "
        "Conservative and Scaled annual profits remain $33,600 and $494,000."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual scorecard revenue from retained infrastructure spreads and assignment fees",
            "note": "28% net margin; $33,600 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$535,000",
            "context": "Annual scorecard revenue excluding purchase principal and underlying tenant billings",
            "note": "40.0% net margin; $214,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$950,000",
            "context": "Annual scorecard revenue measured on the same retained-spread basis",
            "note": "52% net margin; $494,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Turn parcel signals into transferable, fundable rights",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a rights inventory, not a list of attractive parcels. "
                    "Import FCC Antenna Structure Registration records, state DOT annual "
                    "average daily traffic layers, county assessor rolls, and recorded "
                    "parcel geometry into QGIS. ASR coverage is incomplete for the "
                    "telecom universe, so supplement rooftop and smaller structure leads "
                    "with recorded leases and owner-authorized documents. Every intake "
                    "record needs a jurisdiction, parcel identifier, source snapshot date, "
                    "owner contact provenance, and proposed transaction type. Separate "
                    "tower easement acquisition, billboard permit-linked assignment, and "
                    "IOS seasonal master leasing before scoring; each purchases different "
                    "rights and fails for different reasons. The intake script uses "
                    "integer cents and a deterministic source key, preventing a refreshed "
                    "assessor export from creating another payable opportunity. Its score "
                    "prioritizes documented spread and evidence completeness, not legal "
                    "eligibility. Preserve the original export and its SHA-256 digest "
                    "outside the database, then store that digest with subsequent "
                    "verification events. A contractor may collect records, but only "
                    "the designated deal lead can confirm ownership against title "
                    "evidence. Missing instruments trigger a document request, while "
                    "confirmed nonassignability ends that branch before deposits or "
                    "engineering invoices accumulate against a speculative exit."
                ),
                (
                    "Underwrite tower rights from the actual rent schedule, escalation "
                    "clause, remaining term, renewal rights, termination language, and "
                    "access easement. An illustrative $30,000 annual eligible rent stream "
                    "purchased at 16 times rent costs $480,000; a buyer paying 18 times "
                    "rent offers $540,000. After $15,000 of transaction charges, the "
                    "retained spread is $45,000, not $540,000. The advertised 16–22 "
                    "times range is a screening reference, never an executable bid. "
                    "Obtain buyer-specific pricing and settlement instructions before "
                    "committing acquisition capital. With only $12,000–$60,000 startup "
                    "capital, use a permitted assignment or an escrow-controlled, "
                    "buyer-funded simultaneous closing rather than pretending the team "
                    "can warehouse six-figure easements. Review existing mortgage "
                    "priority and obtain the required lender subordination, "
                    "nondisturbance, and attornment agreement, or an equivalent approved "
                    "instrument appropriate to the transaction. A perpetual easement "
                    "does not make the associated tenant rent perpetual. Model tenant "
                    "termination and equipment removal separately. If lender execution "
                    "outlasts the option period, negotiate a documented extension before "
                    "expiry; otherwise release the transaction and preserve the buyer "
                    "relationship. Do not silently replace a missing consent with a "
                    "higher assumed exit multiple."
                ),
                (
                    "For billboards, connect traffic counts to a legally usable display "
                    "location rather than converting AADT directly into advertising "
                    "revenue. Check state-controlled route coverage, spacing, lighting, "
                    "digital conversion rules, municipal zoning, and whether the permit "
                    "and ground lease can transfer together. A $50,000 assignment receipt "
                    "less $20,000 of directly attributable acquisition and closing "
                    "charges creates a $30,000 retained assignment spread. For IOS, "
                    "document heavy-axle use, turning geometry, drainage, access hours, "
                    "fire access, and environmental conditions before accepting rent "
                    "liability. One activated month with 100 occupied spaces at $600 "
                    "produces $60,000 tenant billings; a $35,000 head-lease obligation "
                    "leaves $25,000 retained spread before operating overhead. The "
                    "cohort below assumes only four contracted activation months "
                    "annually and no rent liability outside them. If the owner requires "
                    "twelve paid months, rebuild the economics rather than retaining "
                    "the seasonal case. NNN language allocates specified expenses; it "
                    "does not erase the operator's contractual liability. Keep the "
                    "scorecard's retained economic basis separate from statutory "
                    "reporting: lease accounting generally belongs under ASC 842, "
                    "while applicable service and assignment arrangements require their "
                    "own ASC 606 principal-versus-agent assessment and recognition analysis."
                ),
            ],
            "table": {
                "caption": "Rights-to-Cash Intake Matrix for Telecom, Billboard, and IOS Transactions",
                "headers": [
                    "Workstream and specific source of evidence",
                    "Required operating decision before spending further",
                    "Concrete unit economics and retained basis",
                    "Failure response preserving capital and optionality",
                ],
                "rows": [
                    [
                        "FCC ASR export joined to recorded county parcel ownership",
                        "Confirm the structure and recorded rent rights concern identical premises",
                        "Thirty thousand annual rent supports separate buyer multiple sensitivity calculations",
                        "Request missing rooftop records instead of treating absent registration as rejection",
                    ],
                    [
                        "Recorded telecom lease together with amendments and payment history",
                        "Verify escalation dates, termination rights, access scope, and assignment language",
                        "Four hundred eighty thousand acquisition against five hundred forty thousand exit",
                        "Replace unsupported exit assumptions with an executable buyer-specific written indication",
                    ],
                    [
                        "Mortgage schedule, title commitment, and transaction-specific lender correspondence",
                        "Identify required lender signatures and establish a dated consent tracker",
                        "Fifteen thousand transaction charges reduce sixty thousand gross spread to forty-five thousand",
                        "Extend the option explicitly or terminate before nonrefundable obligations increase",
                    ],
                    [
                        "State DOT route classification and current outdoor-advertising permit records",
                        "Confirm spacing, digital operation, transferable permit rights, and location eligibility",
                        "Fifty thousand assignment receipt less twenty thousand acquisition charges retains thirty thousand",
                        "Offer another eligible location rather than acquiring an unusable sign entitlement",
                    ],
                    [
                        "Municipal zoning determination and engineer-reviewed heavy-vehicle access drawing",
                        "Confirm fleet storage use, turning movements, surface loading, and fire access",
                        "One hundred occupied spaces multiplied by six hundred yields sixty thousand",
                        "Reduce vehicle class or abandon the yard when authorized use fails",
                    ],
                    [
                        "Environmental professional report, drainage records, and applicable stormwater authorization",
                        "Resolve recognized environmental conditions and determine permit applicability before possession",
                        "Thirty-five thousand activated head rent leaves twenty-five thousand retained monthly spread",
                        "Require remediation allocation or reject uncapped environmental and drainage exposure",
                    ],
                    [
                        "Buyer settlement statement and separately documented operator compensation agreement",
                        "Separate purchase principal, reimbursed charges, deposits, and earned operator compensation",
                        "Only retained spreads enter the scorecard rather than institutional acquisition principal",
                        "Hold recognition until the completed transaction supports the agreed compensation amount",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the spread before negotiating the headline multiple",
                "body": (
                    "The best small-team advantage is early discovery of a document "
                    "defect that would otherwise consume weeks of buyer attention."
                ),
                "items": [
                    "Ask the title examiner to identify mortgage recording references before sending the lender an SNDA request; attach the precise legal description and signature requirements.",
                    "Ask the billboard buyer to underwrite the permitted face and digital operating restrictions, not a traffic-count screenshot or an assumed future conversion.",
                    "Walk the IOS entrance with the intended tractor-trailer configuration; compare turning geometry with the lease exhibit before installing an RFID reader.",
                    "Price tower termination and renewal language separately from the buyer's rent multiple, and obtain a fresh indication whenever the underlying lease amendments change.",
                ],
            },
        },
        {
            "heading": "2. Implement six modules with serialized writes and explicit recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the following six modules as a local SQLite reference "
                    "implementation, not as an unattended bank integration. Save each "
                    "code cell under its indicated filename in one project directory. "
                    "Initialize with sqlite3 from Python by executing schema.sql through "
                    "Connection.executescript, then execute views.sql the same way. The "
                    "remaining Python files expose callable functions; qa.py runs "
                    "directly after initialization. Every writer enables foreign keys, "
                    "waits for the database lock, and executes BEGIN IMMEDIATE before "
                    "reading mutable business state. This serializes read-modify-write "
                    "operations across processes sharing this local database. Unique "
                    "source keys collapse repeated intake, event keys bind retries "
                    "to their original payload, and a partial unique index prevents "
                    "two settlement postings for one deal. A reused key carrying "
                    "different content raises an error rather than overwriting evidence. "
                    "If the process fails before commit, SQLite rolls back the "
                    "transaction; after commit, the same key returns the recorded "
                    "result. Keep the database on a supported local filesystem, "
                    "not a shared network drive. Multiple hosts require a database "
                    "such as Postgres with corresponding row locks, uniqueness "
                    "constraints, and transaction boundaries, not synchronized copies "
                    "of this SQLite file."
                ),
                (
                    "The state machine deliberately excludes remote side effects. "
                    "It can qualify, verify, place into escrow, or scrub an opportunity, "
                    "but it cannot wire funds, submit a permit, or create an "
                    "easement. Verification events carry the digest of an evidence "
                    "packet whose title, consent, zoning, and environmental conclusions "
                    "were reviewed by the responsible specialists. A digest proves "
                    "which packet was used; it does not prove that the conclusions "
                    "are correct. CLOSED is reached only through a settlement posting "
                    "that checks the current ESCROW state and records balanced cash "
                    "and retained-revenue entries in the same database transaction. "
                    "Consequently, competing settlement workers cannot both close "
                    "and recognize the same deal. External settlement remains a "
                    "separate process: use the escrow provider's transaction reference, "
                    "retain its final statement, and confirm actual bank receipt "
                    "before posting. A timeout while asking a provider for status "
                    "means query that reference again, not issue another payment. "
                    "When a provider supports idempotency keys, reuse the same stable "
                    "key; otherwise use a documented single-operator release procedure. "
                    "Local atomicity cannot manufacture exactly-once behavior inside "
                    "an unrelated bank or government filing portal."
                ),
                (
                    "The ledger is intentionally narrow: it records cash-settled "
                    "retained revenue, operating expense, and refundable deposits. "
                    "Signed journal amounts use debit-positive convention. Settlement "
                    "debits CASH and credits REVENUE; expense debits OPEX and credits "
                    "CASH; deposit receipts credit DEPOSIT rather than revenue. "
                    "Finalization requires at least two balanced lines, and triggers "
                    "prevent edits to posted entries. The reconciliation view "
                    "distinguishes operating profit from cash movement because deposit "
                    "liabilities can move cash without creating earnings. Refunds "
                    "reverse the deposit movement through a separately keyed posting. "
                    "This is a transaction-control subledger, not a replacement for "
                    "the statutory general ledger: accruals, lease assets, taxes, "
                    "distributions, and correction entries need a separately specified "
                    "accounting interface. For the illustrated cohort, earned spreads "
                    "and expenses settle within their stated months, with no deposit "
                    "balance or unpaid accrual at quarter end. Run QA after every "
                    "import and before issuing the owner statement. Back up through "
                    "SQLite's backup API, verify restoration, and preserve evidence "
                    "files alongside their digest manifest. Database triggers "
                    "constrain ordinary application writes; filesystem permissions "
                    "and restricted deployment access must prevent unauthorized "
                    "schema changes or direct replacement of the database."
                ),
            ],
            "table": {
                "caption": "Six-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module filename and precise execution responsibility",
                    "Copy-pasteable implementation using only standard library components",
                    "Concurrency boundary and required operational verification",
                ],
                "rows": [
                    [
                        "schema.sql establishes constrained deal, event, posting, and journal storage",
                        """PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
CREATE TABLE IF NOT EXISTS deal (
    id INTEGER PRIMARY KEY,
    source_key TEXT NOT NULL UNIQUE,
    payload_hash TEXT NOT NULL,
    play TEXT NOT NULL,
    spread_cents INTEGER NOT NULL CHECK(spread_cents >= 0),
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    state TEXT NOT NULL DEFAULT 'NEW'
        CHECK(state IN ('NEW','QUALIFIED','VERIFIED','ESCROW','CLOSED','SCRUBBED')),
    version INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS event (
    event_key TEXT PRIMARY KEY,
    deal_id INTEGER NOT NULL REFERENCES deal(id),
    payload_hash TEXT NOT NULL,
    target TEXT NOT NULL,
    evidence_hash TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS posting (
    posting_key TEXT PRIMARY KEY,
    payload_hash TEXT NOT NULL,
    deal_id INTEGER REFERENCES deal(id),
    kind TEXT NOT NULL
        CHECK(kind IN ('settlement','opex','deposit','refund')),
    month TEXT NOT NULL,
    evidence_hash TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'DRAFT'
        CHECK(status IN ('DRAFT','POSTED')),
    CHECK(kind != 'settlement' OR deal_id IS NOT NULL)
);
CREATE UNIQUE INDEX IF NOT EXISTS one_settlement_per_deal
ON posting(deal_id) WHERE kind = 'settlement';
CREATE TABLE IF NOT EXISTS journal (
    posting_key TEXT NOT NULL REFERENCES posting(posting_key),
    line_no INTEGER NOT NULL,
    account TEXT NOT NULL CHECK(account IN ('CASH','REVENUE','OPEX','DEPOSIT')),
    cents INTEGER NOT NULL CHECK(typeof(cents) = 'integer' AND cents != 0),
    UNIQUE(posting_key, line_no)
);
CREATE TRIGGER IF NOT EXISTS posting_insert_draft
BEFORE INSERT ON posting WHEN NEW.status != 'DRAFT'
BEGIN SELECT RAISE(ABORT, 'Insert draft before balanced finalization'); END;
CREATE TRIGGER IF NOT EXISTS posting_finalize
BEFORE UPDATE OF status ON posting WHEN NEW.status = 'POSTED'
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT(*) FROM journal WHERE posting_key = OLD.posting_key) < 2
        OR
        (SELECT COALESCE(SUM(cents), 0) FROM journal
         WHERE posting_key = OLD.posting_key) != 0
    THEN RAISE(ABORT, 'Posting requires balanced journal lines') END;
END;
CREATE TRIGGER IF NOT EXISTS posting_no_edit
BEFORE UPDATE ON posting WHEN OLD.status = 'POSTED'
BEGIN SELECT RAISE(ABORT, 'Posted records are immutable'); END;
CREATE TRIGGER IF NOT EXISTS posting_no_delete
BEFORE DELETE ON posting WHEN OLD.status = 'POSTED'
BEGIN SELECT RAISE(ABORT, 'Posted records are immutable'); END;
CREATE TRIGGER IF NOT EXISTS journal_insert_draft
BEFORE INSERT ON journal
WHEN COALESCE((SELECT status FROM posting
              WHERE posting_key = NEW.posting_key), '') != 'DRAFT'
BEGIN SELECT RAISE(ABORT, 'Journal insertion requires draft posting'); END;
CREATE TRIGGER IF NOT EXISTS journal_no_edit
BEFORE UPDATE ON journal
BEGIN SELECT RAISE(ABORT, 'Replace draft lines instead of updating'); END;
CREATE TRIGGER IF NOT EXISTS journal_no_delete_posted
BEFORE DELETE ON journal
WHEN (SELECT status FROM posting
      WHERE posting_key = OLD.posting_key) = 'POSTED'
BEGIN SELECT RAISE(ABORT, 'Posted journal lines are immutable'); END;
""",
                        "Initialize before workers start; uniqueness and immutable posting triggers constrain every writer",
                    ],
                    [
                        "intake.py deduplicates immutable source snapshots and calculates transparent priority scores",
                        """from __future__ import annotations
import hashlib
import json
import sqlite3

def ingest(source_key, play, spread_cents, evidence_count, db="ledger.db"):
    if not source_key or not play:
        raise ValueError("Source key and play are required")
    if type(spread_cents) is not int or spread_cents < 0:
        raise ValueError("Spread must be nonnegative integer cents")
    if type(evidence_count) is not int or not 0 <= evidence_count <= 5:
        raise ValueError("Evidence count must range from zero through five")
    payload = [source_key, play, spread_cents, evidence_count]
    digest = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
    score = min(50, spread_cents // 100000) + evidence_count * 10
    con = sqlite3.connect(db, timeout=30, isolation_level=None)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        con.execute("BEGIN IMMEDIATE")
        old = con.execute(
            "SELECT id, payload_hash FROM deal WHERE source_key = ?",
            (source_key,),
        ).fetchone()
        if old:
            if old[1] != digest:
                raise ValueError("Source key reused with different content")
            result = old[0]
        else:
            result = con.execute(
                "INSERT INTO deal(source_key,payload_hash,play,spread_cents,score) "
                "VALUES (?,?,?,?,?)",
                (source_key, digest, play, spread_cents, score),
            ).lastrowid
        con.commit()
        return result
    except Exception:
        if con.in_transaction:
            con.rollback()
        raise
    finally:
        con.close()
""",
                        "One write reservation covers lookup and insertion; changed evidence requires a new versioned snapshot",
                    ],
                    [
                        "workflow.py advances verification and escrow states without initiating external transfers",
                        """from __future__ import annotations
import hashlib
import json
import sqlite3

ALLOWED = {
    "NEW": {"QUALIFIED", "SCRUBBED"},
    "QUALIFIED": {"VERIFIED", "SCRUBBED"},
    "VERIFIED": {"ESCROW", "SCRUBBED"},
    "ESCROW": {"SCRUBBED"},
}

def advance(event_key, deal_id, target, evidence_hash, db="ledger.db"):
    if not event_key or len(evidence_hash) != 64:
        raise ValueError("Event key and SHA-256 evidence digest are required")
    int(evidence_hash, 16)
    payload = [deal_id, target, evidence_hash]
    digest = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
    con = sqlite3.connect(db, timeout=30, isolation_level=None)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        con.execute("BEGIN IMMEDIATE")
        old = con.execute(
            "SELECT payload_hash FROM event WHERE event_key = ?", (event_key,)
        ).fetchone()
        if old:
            if old[0] != digest:
                raise ValueError("Event key content conflict")
            con.commit()
            return target
        row = con.execute(
            "SELECT state, version FROM deal WHERE id = ?", (deal_id,)
        ).fetchone()
        if row is None or target not in ALLOWED.get(row[0], set()):
            raise ValueError("Disallowed state transition")
        changed = con.execute(
            "UPDATE deal SET state=?, version=version+1 WHERE id=? AND version=?",
            (target, deal_id, row[1]),
        ).rowcount
        if changed != 1:
            raise RuntimeError("Concurrent state change")
        con.execute(
            "INSERT INTO event(event_key,deal_id,payload_hash,target,evidence_hash) "
            "VALUES (?,?,?,?,?)",
            (event_key, deal_id, digest, target, evidence_hash),
        )
        con.commit()
        return target
    except Exception:
        if con.in_transaction:
            con.rollback()
        raise
    finally:
        con.close()
""",
                        "Evidence review happens before invocation; serialized transition checks prevent competing state changes",
                    ],
                    [
                        "posting.py posts balanced cash events and closes settled deals atomically",
                        """from __future__ import annotations
import datetime
import hashlib
import json
import sqlite3

PAIRS = {
    "settlement": ("CASH", "REVENUE"),
    "opex": ("OPEX", "CASH"),
    "deposit": ("CASH", "DEPOSIT"),
    "refund": ("DEPOSIT", "CASH"),
}

def post(key, kind, month, cents, evidence_hash, deal_id=None, db="ledger.db"):
    if not key or kind not in PAIRS or type(cents) is not int or cents <= 0:
        raise ValueError("Posting requires key, supported kind, and positive cents")
    parsed = datetime.datetime.strptime(month, "%Y-%m")
    if parsed.strftime("%Y-%m") != month:
        raise ValueError("Month must use four-digit year and two-digit month")
    if len(evidence_hash) != 64:
        raise ValueError("SHA-256 evidence digest is required")
    int(evidence_hash, 16)
    payload = [kind, month, cents, evidence_hash, deal_id]
    digest = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
    con = sqlite3.connect(db, timeout=30, isolation_level=None)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        con.execute("BEGIN IMMEDIATE")
        old = con.execute(
            "SELECT payload_hash,status FROM posting WHERE posting_key=?", (key,)
        ).fetchone()
        if old:
            if old != (digest, "POSTED"):
                raise ValueError("Posting key conflict or incomplete posting")
            con.commit()
            return key
        if kind == "settlement":
            row = con.execute(
                "SELECT state FROM deal WHERE id=?", (deal_id,)
            ).fetchone()
            if row != ("ESCROW",):
                raise ValueError("Settlement requires escrow state")
        con.execute(
            "INSERT INTO posting(posting_key,payload_hash,deal_id,kind,month,"
            "evidence_hash) VALUES (?,?,?,?,?,?)",
            (key, digest, deal_id, kind, month, evidence_hash),
        )
        debit, credit = PAIRS[kind]
        con.executemany(
            "INSERT INTO journal(posting_key,line_no,account,cents) VALUES (?,?,?,?)",
            [(key, 1, debit, cents), (key, 2, credit, -cents)],
        )
        con.execute("UPDATE posting SET status='POSTED' WHERE posting_key=?", (key,))
        if kind == "settlement":
            con.execute(
                "UPDATE deal SET state='CLOSED',version=version+1 WHERE id=?",
                (deal_id,),
            )
        con.commit()
        return key
    except Exception:
        if con.in_transaction:
            con.rollback()
        raise
    finally:
        con.close()
""",
                        "Unique settlement index plus one transaction prevents duplicate recognition even under different retry keys",
                    ],
                    [
                        "views.sql reconciles recognized retained revenue, expenses, deposits, and monthly cash",
                        """CREATE VIEW IF NOT EXISTS monthly_reconciliation AS
SELECT
    p.month,
    -SUM(CASE WHEN j.account='REVENUE' THEN j.cents ELSE 0 END)
        AS revenue_cents,
    SUM(CASE WHEN j.account='OPEX' THEN j.cents ELSE 0 END)
        AS opex_cents,
    -SUM(CASE WHEN j.account IN ('REVENUE','OPEX')
              THEN j.cents ELSE 0 END) AS profit_cents,
    SUM(CASE WHEN j.account='CASH' THEN j.cents ELSE 0 END)
        AS cash_delta_cents,
    -SUM(CASE WHEN j.account='DEPOSIT' THEN j.cents ELSE 0 END)
        AS deposit_delta_cents
FROM posting AS p
JOIN journal AS j ON j.posting_key=p.posting_key
WHERE p.status='POSTED'
GROUP BY p.month;
""",
                        "Compare bank movement with cash delta; profit differs whenever refundable deposit balances change",
                    ],
                    [
                        "qa.py checks integrity, settlement coverage, balanced entries, and bank movement",
                        """from __future__ import annotations
import json
import sqlite3

def check(db="ledger.db", bank_cash_delta_cents=None):
    con = sqlite3.connect(db, timeout=30, isolation_level=None)
    try:
        con.execute("PRAGMA foreign_keys = ON")
        con.execute("BEGIN")
        failures = []
        integrity = con.execute("PRAGMA integrity_check").fetchall()
        if integrity != [("ok",)]:
            failures.append("Database integrity check failed")
        if con.execute("PRAGMA foreign_key_check").fetchall():
            failures.append("Foreign key violations detected")
        bad = con.execute(
            "SELECT p.posting_key FROM posting p LEFT JOIN journal j "
            "ON j.posting_key=p.posting_key GROUP BY p.posting_key "
            "HAVING p.status!='POSTED' OR COUNT(j.line_no)<2 "
            "OR COALESCE(SUM(j.cents),0)!=0"
        ).fetchall()
        if bad:
            failures.append("Incomplete or unbalanced postings detected")
        missing = con.execute(
            "SELECT d.id FROM deal d WHERE d.state='CLOSED' AND NOT EXISTS "
            "(SELECT 1 FROM posting p WHERE p.deal_id=d.id "
            "AND p.kind='settlement' AND p.status='POSTED')"
        ).fetchall()
        if missing:
            failures.append("Closed deals lack posted settlement")
        wrong = con.execute(
            "SELECT p.posting_key FROM posting p JOIN deal d ON d.id=p.deal_id "
            "WHERE p.kind='settlement' AND p.status='POSTED' AND d.state!='CLOSED'"
        ).fetchall()
        if wrong:
            failures.append("Settlement postings lack closed deal state")
        con.row_factory = sqlite3.Row
        rows = [
            dict(row) for row in con.execute(
                "SELECT * FROM monthly_reconciliation ORDER BY month"
            )
        ]
        for row in rows:
            if row["cash_delta_cents"] != (
                row["profit_cents"] + row["deposit_delta_cents"]
            ):
                failures.append("Cash bridge failed for " + row["month"])
        movement = sum(row["cash_delta_cents"] for row in rows)
        if bank_cash_delta_cents is not None:
            if type(bank_cash_delta_cents) is not int:
                raise ValueError("Bank movement must use integer cents")
            if movement != bank_cash_delta_cents:
                failures.append("Bank movement differs from ledger movement")
        con.commit()
        if failures:
            raise RuntimeError("; ".join(failures))
        return {
            "months": rows,
            "bank_reconciled": bank_cash_delta_cents is not None,
            "cash_delta_cents": movement,
        }
    finally:
        if con.in_transaction:
            con.rollback()
        con.close()

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
""",
                        "Read transaction fixes the QA snapshot; bank verification requires an independently sourced movement total",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Initialize and test isolated ledger storage",
                    "action": "Execute schema.sql and views.sql using sqlite3.Connection.executescript in a temporary project database.",
                    "detail": "Run integrity checks, confirm foreign-key enforcement per connection, and prove restoration from a SQLite backup before using live settlement evidence.",
                },
                {
                    "step": 2,
                    "title": "Prove retry behavior before processing money",
                    "action": "Invoke intake and workflow twice with identical keys, then repeat with deliberately changed payloads.",
                    "detail": "Identical requests must return the prior result; changed content must raise an error without inserting another record or advancing state.",
                },
                {
                    "step": 3,
                    "title": "Exercise competing settlement and crash recovery",
                    "action": "Run two local processes against one ESCROW deal using distinct posting keys, then test process termination before commit.",
                    "detail": "Only one settlement may commit; the other must fail its state or uniqueness check. An interrupted uncommitted transaction must leave no partial journal.",
                },
                {
                    "step": 4,
                    "title": "Reconcile evidence, ledger, and independent cash",
                    "action": "Call check with the bank's integer-cent operating cash movement after excluding separately tracked capital and distributions.",
                    "detail": "Compare every posting with its settlement or invoice artifact, clear exceptions individually, and retain the QA result with the monthly evidence manifest.",
                },
            ],
        },
        {
            "heading": "3. Make specialist review, tax appeals, and exception ownership explicit",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Assign the Base team as one full-time principal and three "
                    "contractor functions: title and transaction counsel, environmental "
                    "and civil diligence, and GIS plus bookkeeping operations. "
                    "Contractor functions describe responsibility, not a promise that "
                    "one person holds every professional credential. The principal "
                    "owns pricing, buyer commitments, cash exposure, and the weekly "
                    "exception meeting. Counsel resolves assignment restrictions, "
                    "brokerage status, recorded interests, and closing instruments. "
                    "The environmental professional controls Phase I scope and "
                    "findings; the civil specialist confirms drainage and access "
                    "where needed. Operations maintains source snapshots, deadlines, "
                    "posting evidence, and reconciliation. Separate the person "
                    "preparing a payment instruction from the person independently "
                    "confirming escrow destination details through an established "
                    "contact channel. Buying or assigning a principal interest "
                    "does not automatically satisfy every state licensing exemption; "
                    "document the exact local rule and the actual conduct performed. "
                    "When activity is brokerage, engage the required licensee rather "
                    "than renaming a commission. Contractor invoices must reference "
                    "the deal and work product so that failed diligence remains "
                    "visible in acquisition cost. Review aging weekly by the "
                    "specific missing instrument and responsible counterparty, "
                    "not by a vague probability-of-closing percentage."
                ),
                (
                    "The mapped play property_tax_assessment_appeal_contingency adds a "
                    "separate, deadline-driven service queue rather than magically "
                    "increasing tower rent. Ingest county valuation rolls when "
                    "annual notices release, normalize parcel class and valuation "
                    "date, and compare assessed-to-market ratios across genuinely "
                    "comparable neighbors. An AVM flag starts review; it is not "
                    "proof of unequal assessment or a permitted filing position. "
                    "For illustration, a supportable $200,000 reduction multiplied "
                    "by a 2.0% applicable effective tax rate implies $4,000 annual "
                    "tax savings. A 40% first-year contingency yields $1,600 "
                    "service revenue only after the contract's verification and "
                    "collection conditions are satisfied. Across ten successful "
                    "parcels, that becomes $16,000 before specialist fees and "
                    "filing costs. The operating range is 30–50% of the first "
                    "year's verified reduction, not a percentage of property "
                    "value or a recurring claim on future savings. Track the "
                    "jurisdiction's actual deadline, service authorization, appeal "
                    "basis, submission receipt, and final tax outcome. In regulated "
                    "states, partner with licensed local property-tax consultants "
                    "or attorneys of record and automate pre-deadline batch "
                    "electronic filing through authorized channels. Keep this "
                    "adjacent service outside the Base cohort dollars unless "
                    "the annual model explicitly replaces another revenue component."
                ),
                (
                    "Treat statutory requirements as operating inputs with named "
                    "evidence owners. The Highway Beautification Act, 23 U.S.C. "
                    "131, and 23 CFR Part 750 establish the federal outdoor "
                    "advertising framework, while state programs and municipal "
                    "rules determine the site's concrete restrictions. Federal "
                    "eligibility is not a local sign permit. For IOS acquisitions "
                    "where all appropriate inquiries matters, 40 CFR Part 312 "
                    "governs that inquiry framework; an environmental professional "
                    "must determine scope, timing, and any need for further "
                    "investigation. A Phase I report neither authorizes stormwater "
                    "discharges nor resolves every operational environmental "
                    "obligation. Evaluate 40 CFR 122.26 and the applicable state "
                    "program against actual industrial activity and exposure, "
                    "rather than assuming every yard requires the same permit. "
                    "Texas property-tax representation illustrates why the "
                    "adjacent appeal service needs jurisdictional routing: "
                    "Occupations Code Chapter 1152 addresses property-tax "
                    "consultants, and Tax Code 41.44 addresses protest timing. "
                    "Archive the applicable rule version and transaction facts "
                    "with each decision. When facts change, such as a new "
                    "vehicle class, revised digital display operation, or "
                    "different appeal representative, reopen the corresponding "
                    "review before continuing work under stale evidence."
                ),
            ],
            "table": {
                "caption": "Exception Ownership and Adjacent Appeal Play Operating Matrix",
                "headers": [
                    "Specific exception or mapped operating play",
                    "Evidence owner and concrete verification artifact",
                    "Unit economics or deadline exposure measurement",
                    "Required fallback when the preferred path fails",
                ],
                "rows": [
                    [
                        "Tower mortgage priority prevents immediate recording of purchased easement rights",
                        "Transaction counsel obtains lender requirements and final signed consent instruments",
                        "Track extension cost against the remaining executable retained transaction spread",
                        "Extend the option in writing or release before acquisition funds become exposed",
                    ],
                    [
                        "Billboard spacing or digital conversion restrictions defeat the proposed display",
                        "Permit specialist retains state determination and municipal zoning disposition",
                        "Remove projected assignment revenue until a transferable permitted configuration exists",
                        "Reprice a permitted static configuration or move acquisition work to another parcel",
                    ],
                    [
                        "IOS environmental findings create unresolved remediation or operational discharge exposure",
                        "Environmental professional documents findings while civil specialist addresses drainage design",
                        "Cap investigatory spending against the activated month's twenty-five thousand retained spread",
                        "Allocate remediation contractually or decline possession until the exposure is resolved",
                    ],
                    [
                        "property_tax_assessment_appeal_contingency uses annual notice rolls and comparable equity ratios",
                        "Authorized representative validates AVM flags against local protest grounds and evidence",
                        "Two hundred thousand reduction at two percent produces four thousand annual savings",
                        "Route regulated representation to licensed consultants or attorneys before batch filing",
                    ],
                    [
                        "First-year contingency calculation must follow verified tax reduction and contract terms",
                        "Bookkeeper matches final tax outcome, owner invoice, and collected contingency payment",
                        "Forty percent of four thousand verified savings produces sixteen hundred service revenue",
                        "Defer billing or recognition when outcome verification and contractual earning conditions remain incomplete",
                    ],
                    [
                        "Bank destination changes arrive during an otherwise ready infrastructure settlement",
                        "Principal confirms instructions through previously established escrow provider contact details",
                        "Suspend the affected transfer without adding projected proceeds to available working capital",
                        "Resolve the changed destination independently rather than replying to the amendment email",
                    ],
                    [
                        "Quarter-end cash movement differs from retained revenue less recorded operating expenses",
                        "Bookkeeper reconciles posting evidence, deposit movements, timing differences, and bank activity",
                        "Cash movement equals operating profit plus refundable deposit liability movement here",
                        "Investigate individual unmatched entries and issue no reconciled statement before resolution",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before irreversible exposure",
                "body": (
                    "Record a dated decision and evidence digest for each check; "
                    "a checked box without its supporting instrument is insufficient."
                ),
                "items": [
                    "Confirm owner authority, legal description, transferable rights, mortgage priority, and every transaction-specific lender consent before releasing acquisition funds.",
                    "Confirm billboard route classification, applicable spacing and lighting restrictions, municipal entitlement, and the permitted method of transferring the display rights.",
                    "Confirm IOS heavy-axle use, operational drainage requirements, environmental findings, and the exact activated-month rent obligation before taking possession.",
                    "Confirm buyer funding, independently verified escrow instructions, balanced posting tests, and a cash buffer sufficient for delayed closings before signing a nonrefundable commitment.",
                ],
            },
        },
        {
            "heading": "4. Walk three monthly cohorts from source records to reconciled owner cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a constructed production "
                    "case, not a report of completed transactions. Begin with "
                    "$60,000 operator cash and no receivables, deposits, borrowings, "
                    "or existing lease obligations. Month 1 sources cohort A's "
                    "60 opportunities. Forty-eight fail desktop screening; of "
                    "12 reviewed candidates, nine fail document or economic "
                    "diligence and three advance. No retained revenue arrives "
                    "that month, while $18,000 of paid operating costs creates "
                    "an $18,000 cumulative operating deficit and leaves $42,000 "
                    "cash. In Month 2, two cohort A tower assignments settle "
                    "for retained spreads of $20,000 and $25,000. Their "
                    "underlying easement purchase principal moves through "
                    "buyer-controlled escrow and never enters this operator "
                    "cash schedule. Month 2 also sources cohort B's 60 "
                    "opportunities: 50 fail desktop review and eight of "
                    "ten diligence candidates are scrubbed, leaving a "
                    "billboard assignment and an IOS activation. Paid "
                    "Month 2 costs total $27,000, so $45,000 receipts "
                    "generate $18,000 operating cash and restore the "
                    "opening $60,000 balance. Scrubbed leads create no "
                    "fictional revenue write-off; their consumed labor "
                    "and diligence invoices remain inside the operating "
                    "cost schedule."
                ),
                (
                    "Month 3 receives $30,000 from cohort A's billboard "
                    "assignment, $33,750 from cohort B's billboard assignment, "
                    "and $25,000 retained IOS spread from cohort B's first "
                    "contracted activation. Those five completed transactions "
                    "produce quarterly retained revenue of $133,750. Month 3 "
                    "sources cohort C's 60 opportunities; 52 fail desktop "
                    "screening, six more fail diligence, and two remain "
                    "documented carry-forward candidates with no recognized "
                    "revenue. Month 3 paid operating costs are $35,250, "
                    "leaving $53,500 incremental cash and $113,500 closing "
                    "cash. The cost schedule separates recurring overhead "
                    "of $4,000, $5,000, and $6,000 from variable "
                    "professional, acquisition, diligence, and closing support "
                    "costs of $14,000, $22,000, and $29,250. These "
                    "variable costs are additional to charges already "
                    "deducted in computing retained deal spreads; never "
                    "post the same charge twice. Thus recurring monthly "
                    "overhead stays within the stated $2,000–$12,000 range "
                    "while total production costs can exceed it. To "
                    "reproduce the ledger, post settlements of 2000000, "
                    "2500000, 3000000, 3375000, and 2500000 cents "
                    "against five separately verified ESCROW deals, and "
                    "post monthly expense totals of 1800000, 2700000, "
                    "and 3525000 cents."
                ),
                (
                    "Quarterly profit equals $133,750 minus $80,250, or "
                    "$53,500, giving exactly 40.0% margin. Four equivalent "
                    "production blocks yield $535,000 annual retained "
                    "revenue, $321,000 costs, and $214,000 owner net "
                    "profit. The annual construction contains eight tower "
                    "assignments totaling $180,000, eight billboard "
                    "assignments totaling $255,000, and four IOS activation "
                    "months totaling $100,000 retained spread. It does "
                    "not assume twelve IOS rent months or add repeat "
                    "revenue from the same activation. Cohort C remains "
                    "pipeline, not an extra cash asset. Repeating "
                    "production requires replenishing buyer capacity, "
                    "maintaining the same cost discipline, and signing "
                    "seasonal terms that actually support four paid "
                    "activation months. A delayed $33,750 billboard "
                    "closing shifts cash and recognition into the "
                    "later period; it cannot remain in Month 3 "
                    "merely to preserve the target. The separate "
                    "Conservative case remains $120,000 revenue less "
                    "$86,400 costs, producing $33,600 at 28%; Scaled "
                    "remains $950,000 less $456,000, producing $494,000 "
                    "at 52%. Base and Conservative use one full-time "
                    "operator plus three contractors; Scaled uses two "
                    "plus four. These are distinct annual assumptions, "
                    "not automatic outcomes of multiplying the lead "
                    "count or shortening specialist review."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period or cohort and production scope",
                    "Lead progression, scrubs, and unresolved obligations",
                    "Recognized retained revenue and actual cash timing",
                    "Paid operating costs and cumulative cash bridge",
                ],
                "rows": [
                    [
                        "Month 1 launches cohort A using sixty thousand opening operator cash",
                        "Sixty sourced; forty-eight desktop scrubs; nine diligence scrubs; three advance",
                        "Zero retained receipts because all three transactions remain unfinished",
                        "Eighteen thousand costs; cumulative operating cash negative eighteen thousand; bank forty-two thousand",
                    ],
                    [
                        "Month 2 closes two tower transactions while sourcing cohort B",
                        "Sixty new leads; fifty desktop scrubs; eight diligence scrubs; two advance",
                        "Twenty thousand plus twenty-five thousand retained tower receipts equals forty-five thousand",
                        "Twenty-seven thousand costs; cumulative operating cash zero; bank sixty thousand",
                    ],
                    [
                        "Month 3 closes two billboard assignments and one IOS activation",
                        "Cohort C contributes sixty leads; fifty-two desktop scrubs; six diligence scrubs",
                        "Thirty thousand plus thirty-three thousand seven hundred fifty plus twenty-five thousand received",
                        "Thirty-five thousand two hundred fifty costs; cumulative cash fifty-three thousand five hundred",
                    ],
                    [
                        "Cohort A disposition across its complete ninety-day transaction lifecycle",
                        "Fifty-seven total scrubs leave two completed towers and one completed billboard",
                        "Month 2 receives forty-five thousand; Month 3 receives thirty thousand",
                        "Shared production costs remain allocated by month rather than duplicated against cohorts",
                    ],
                    [
                        "Cohort B disposition across its first sixty days of production",
                        "Fifty-eight total scrubs leave one completed billboard and one activated IOS yard",
                        "Month 3 receives fifty-eight thousand seven hundred fifty retained combined spread",
                        "IOS head rent already reduces retained spread and is excluded from overhead",
                    ],
                    [
                        "Cohort C disposition at the ninety-day reporting cutoff date",
                        "Fifty-eight total scrubs leave two carry-forward candidates requiring further verified execution",
                        "Zero recognized receipts; neither pending candidate contributes to reported operating cash",
                        "Consumed diligence spending remains included in Month 3 paid production costs",
                    ],
                    [
                        "Quarter totals and four-block annual Base-Case production reconciliation",
                        "One hundred eighty leads; one hundred seventy-three scrubs; five completions; two pending",
                        "Quarter revenue $133,750; four equivalent blocks produce annual revenue $535,000",
                        "Quarter costs $80,250; profit $53,500; ending cash $113,500; annual profit $214,000",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "A spread becomes owner cash only when the rights transfer, the evidence "
        "survives review, and the bank agrees with the ledger."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        "Build a versioned parcel intake from FCC ASR, state DOT AADT, assessor rolls, and recorded interests; assign stable source keys before contractor outreach.",
        "Price each tower, billboard, and IOS opportunity on retained spread, with buyer-specific execution evidence and explicit treatment of principal, deposits, and head rent.",
        "Initialize the six reference modules in an isolated project database, then test duplicate keys, competing settlement workers, rollback recovery, and backup restoration.",
        "Collect title, lender consent, permit, environmental, and heavy-axle evidence under dated ownership before taking nonrefundable acquisition or possession exposure.",
        "Route property-tax appeal candidates to authorized local representatives, calculate first-year verified savings, and preserve filing receipts before jurisdictional deadlines.",
        "Recreate the three-month cohort using integer cents, reconcile $53,500 operating cash to independent bank movement, and preserve the $535,000 annual retained-revenue basis.",
    ],
    "statutory_citations": [
        {
            "title": "23 U.S.C. 131 — Control of outdoor advertising",
            "url": "https://www.law.cornell.edu/uscode/text/23/131",
            "relevance": (
                "Establishes the federal outdoor-advertising framework relevant "
                "to controlled highways; site underwriting must also identify "
                "the applicable state program and municipal requirements."
            ),
        },
        {
            "title": "23 CFR Part 750 — Highway Beautification",
            "url": "https://www.ecfr.gov/current/title-23/chapter-I/subchapter-H/part-750",
            "relevance": (
                "Provides implementing outdoor-advertising rules that inform "
                "route eligibility, state control, and permit diligence before "
                "billboard rights are acquired or assigned."
            ),
        },
        {
            "title": "47 CFR 17.4 — Antenna structure registration",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-17/section-17.4",
            "relevance": (
                "Defines antenna structure registration requirements and helps "
                "operators understand why the ASR database is a useful intake "
                "source but not a complete inventory of telecom lease rights."
            ),
        },
        {
            "title": "40 CFR Part 312 — Innocent Landowners, Standards for Conducting All Appropriate Inquiries",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
            "relevance": (
                "Supplies the all appropriate inquiries framework where "
                "applicable to environmental diligence; the environmental "
                "professional must determine transaction-specific scope and timing."
            ),
        },
        {
            "title": "40 CFR 122.26 — Storm water discharges",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-122/section-122.26",
            "relevance": (
                "Supports activity-specific evaluation of industrial stormwater "
                "requirements alongside the authorized state program rather "
                "than assuming identical treatment for every IOS operation."
            ),
        },
        {
            "title": "Texas Occupations Code Chapter 1152 — Property Tax Consultants",
            "url": "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1152.htm",
            "relevance": (
                "Provides a concrete jurisdictional example for routing "
                "property-tax representation through appropriately registered "
                "professionals and evaluating applicable exemptions."
            ),
        },
        {
            "title": "Texas Tax Code 41.44 — Notice of Protest",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.41.htm#41.44",
            "relevance": (
                "Establishes protest notice timing and related exceptions "
                "that must be reflected in the parcel-level filing calendar "
                "before automated batch submission."
            ),
        },
    ],
}
