from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "judgment-recovery-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute judgment recovery end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Commercial Docket Screening, Bankruptcy Holds, Lien Priority, SQLite Cash Controls, and a Base-Case Cohort Reconciliation",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #8, Judgment Recovery, ranks #15 with a 77/100 Money-to-Manpower "
        "Score across 15 mapped plays. This chapter converts commercial judgment "
        "screening into an evidence-backed production system: establish authority, "
        "verify collectible equity, authorize counsel-led enforcement, capture cleared "
        "receipts, and reconcile client liabilities before recognizing earned service "
        "fees. Annual owner profit remains $12,000 Conservative, $84,000 Base, and "
        "$200,000 Scaled. A six-module SQLite reference uses integer cents, serialized "
        "writes, immutable event identities, and balanced entries. The worked 90-day "
        "walk separates inherited pipeline from newly admitted cohorts and reconciles "
        "to the $280,000 Base revenue run rate. The medical-receivables play receives "
        "its own eligibility, HIPAA, ERISA, and federal dispute-resolution branch "
        "rather than being mislabeled as judgment enforcement."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees, excluding client recoveries and asset values.",
            "note": "20% net margin; $12,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Base",
            "value": "$280,000",
            "context": "Annual recognized service fees, excluding client recoveries and asset values.",
            "note": "30.0% net margin; $84,000 annual owner net profit; 1 FT + 3 C.",
        },
        {
            "label": "Scaled",
            "value": "$500,000",
            "context": "Annual recognized service fees, excluding client recoveries and asset values.",
            "note": "40% net margin; $200,000 annual owner net profit; 2 FT + 4 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Admit Collectible Commercial Files, Not Impressive Judgment Balances",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with an authority packet, not a debtor search. Obtain the entered judgment, "
                    "docket history, service evidence, creditor identity, assignment chain where applicable, "
                    "and the agreement defining your service fee and reimbursable expenses. Record the "
                    "court, case number, debtor's exact legal name, judgment date, principal, interest "
                    "method, payments, credits, and renewal deadline as separate fields. A $250,000 "
                    "judgment with $40,000 already satisfied is not a $250,000 collection opportunity; "
                    "the collectible balance must also reflect applicable interest and subsequent credits. "
                    "Use PACER for relevant federal proceedings and the issuing court's own docket "
                    "for state judgments. Do not substitute a commercial aggregator's timestamp for "
                    "the clerk's entry date. Classify the underlying obligation before contact: commercial "
                    "post-judgment work is the focus, while personal, family, or household obligations "
                    "require a different consumer-debt analysis under 15 U.S.C. 1692a(5). State licensing "
                    "rules can reach activities beyond that federal definition. Have jurisdiction-qualified "
                    "counsel determine who may enforce, appear, sign filings, and receive funds. An "
                    "assignment does not automatically authorize a nonlawyer to represent another "
                    "person or business in court. Missing authority keeps the file in review, regardless "
                    "of the apparent asset value. Give every uploaded document a source reference, "
                    "retrieval date, content hash, and named reviewer."
                ),
                (
                    "Screen collectible equity before purchasing another report or commissioning service. "
                    "A useful file-level estimate is realizable asset proceeds minus senior claims, "
                    "applicable exemptions, sale friction, and incremental enforcement expense. For "
                    "example, $90,000 of estimated realizable proceeds less $55,000 of senior liens, "
                    "$10,000 of protected value, and $8,000 of execution expense leaves $17,000 "
                    "before allocation to the judgment. At a contracted 30% recovery fee, that produces "
                    "only $5,100 of operator revenue before the operator's own costs. The arithmetic "
                    "is a screening model, not evidence that the asset can actually be seized. Verify "
                    "ownership, situs, lien attachment, perfection, and priority using the applicable "
                    "recording system and governing law. UCC Section 9-317 addresses particular "
                    "priority contests involving security interests and lien creditors; it does not "
                    "replace real-property recording statutes or bankruptcy analysis. Search PACER "
                    "for bankruptcy and inspect the actual petition and orders. A filing may trigger "
                    "11 U.S.C. 362, so suspend affected enforcement and route questions about scope "
                    "or exceptions to counsel. Rank files by expected net fee per funded work hour, "
                    "but never let a score override a stay, expired enforcement right, disputed identity, "
                    "or incomplete chain of authority."
                ),
                (
                    "Run the admitted file through four evidence-backed decisions: verify authority, "
                    "approve a cost-limited enforcement plan, execute through the authorized actor, "
                    "and reconcile cleared cash. The owner controls the commercial budget; counsel "
                    "controls legal judgment and filings; a licensed investigator or permitted research "
                    "provider supplies lawfully obtained facts; a bookkeeper reconciles receipts and "
                    "liabilities. These are responsibilities, not permission to share legal fees with "
                    "nonlawyers. Use contracts and payment arrangements that fit the applicable "
                    "professional and collection rules. In the Base team, one full-time operator "
                    "coordinates three contractors without treating them as three full-time salaries. "
                    "Reserve $600 for initial work on a file only when the expected fee justifies "
                    "that exposure; require a new written budget before a $2,400 examination, levy, "
                    "or contested motion. Maintain a deadline register with the triggering document, "
                    "rule, timezone, calculation, reviewer, and completion evidence. Calendar automation "
                    "creates reminders, not legal conclusions. Stop work when the debtor identity "
                    "changes, ownership evidence contradicts the target, a bankruptcy event arrives, "
                    "or the next dollar of expense exceeds expected incremental recovery. Preserve "
                    "the reason for every decline so future sourcing rewards collectible inventory "
                    "rather than merely increasing docket volume."
                ),
            ],
            "table": {
                "caption": "Commercial Judgment Admission and Enforcement Evidence Matrix",
                "headers": [
                    "Operating checkpoint and accountable actor",
                    "Evidence required before advancing the file",
                    "Economic test and permitted next action",
                    "Failure response and retained audit evidence",
                ],
                "rows": [
                    [
                        "Creditor authority review performed by the assigned operator",
                        "Entered judgment, engagement agreement, assignment documents, and creditor identity",
                        "Confirm the service-fee basis before budgeting any investigative expense",
                        "Keep the matter in review until counsel resolves ownership defects",
                    ],
                    [
                        "Underlying obligation classification reviewed with jurisdiction-qualified collection counsel",
                        "Original transaction documents establish business purpose or consumer purpose",
                        "Route consumer obligations outside the commercial production track immediately",
                        "Preserve classification reasoning and apply the correct contact requirements",
                    ],
                    [
                        "Judgment balance calculation independently checked by the bookkeeper",
                        "Principal, permitted interest, prior receipts, credits, and court-awarded costs",
                        "Separate the recoverable balance from prospective operator service revenue",
                        "Reject unsupported interest calculations and obtain corrected payment histories",
                    ],
                    [
                        "Bankruptcy status review before every consequential enforcement instruction",
                        "Petition docket, debtor identifiers, relevant orders, and current review timestamp",
                        "Suspend affected collection activity while counsel evaluates stay coverage",
                        "Record the hold without deleting earlier actions or received cash",
                    ],
                    [
                        "Asset ownership and priority review conducted before targeted execution",
                        "Official ownership records, recorded liens, exemptions analysis, and realizable valuation",
                        "Subtract senior claims and friction before estimating collectible equity",
                        "Decline negative-equity targets instead of escalating unrecoverable enforcement spend",
                    ],
                    [
                        "Jurisdictional enforcement planning performed by the authorized legal actor",
                        "Applicable writ requirements, domestication documents, service rules, and filing authority",
                        "Approve a written expense ceiling against expected incremental fee recovery",
                        "Return defective service or stale writs for correction before action",
                    ],
                    [
                        "Settlement authority confirmation obtained before communicating binding acceptance",
                        "Written settlement range, permitted concessions, payment instructions, and release conditions",
                        "Evaluate net cleared recovery rather than the headline settlement amount",
                        "Escalate installment defaults without issuing unauthorized threats or promises",
                    ],
                    [
                        "Cash allocation review completed before any client disbursement instruction",
                        "Cleared bank receipt, earned-fee evidence, contractual allocation, and verified payee",
                        "Recognize only earned service fees and preserve the client liability",
                        "Hold disputed allocations and reconcile every correction through documented entries",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy Better Evidence Before Buying More Enforcement",
                "body": (
                    "Experienced operators protect capital by making cheap evidence eliminate "
                    "expensive mistakes before counsel or investigators incur additional charges."
                ),
                "items": [
                    "Compare debtor names against the judgment and ownership record; a similar business name does not establish executable ownership.",
                    "Price a senior-lien payoff update before ordering a levy when a modest balance change could erase collectible equity.",
                    "Ask counsel to identify the document that starts each deadline; store that document beside the calculated reminder.",
                    "Separate stayed files from insolvent files in sourcing reports, because a temporary legal hold and absent equity require different follow-up strategies.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Assemble and classify the authority packet",
                    "action": "Register the source identity and preserve hashed intake evidence.",
                    "detail": (
                        "Confirm the creditor, underlying obligation, judgment balance, "
                        "assignment chain, and jurisdiction-specific licensing requirements."
                    ),
                },
                {
                    "step": 2,
                    "title": "Verify equity and authorize bounded expenditure",
                    "action": "Complete bankruptcy, ownership, priority, and exemption checks.",
                    "detail": (
                        "Have the authorized reviewer approve a documented enforcement "
                        "plan and maximum next-stage expense before issuing instructions."
                    ),
                },
                {
                    "step": 3,
                    "title": "Execute only through the authorized actor",
                    "action": "Prepare a uniquely identified action and preserve execution evidence.",
                    "detail": (
                        "Recheck current holds before action; reconcile uncertain external "
                        "results rather than sending duplicate court or payment instructions."
                    ),
                },
                {
                    "step": 4,
                    "title": "Reconcile receipt, fee, and client distribution",
                    "action": "Post cleared bank evidence and independently verify the allocation.",
                    "detail": (
                        "Match the bank receipt to the case, establish that the fee is "
                        "earned, confirm the actual client transfer, and retain the audit trail."
                    ),
                },
            ],
        },
        {
            "heading": "2. Build the Ledger Before Automating the Workflow",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use one canonical case identity and an append-only cash subledger. Store money "
                    "as integer cents, never binary floating-point amounts, and use a stable upstream "
                    "reference rather than a person's name as the duplicate key. The six modules "
                    "below can be pasted in order into one Python 3.9 script; their database path "
                    "is an operator-selected project file. SQLite serializes each write transaction "
                    "with BEGIN IMMEDIATE, while UNIQUE constraints reject competing identities. "
                    "Every operation opens its own connection, so workers do not share mutable "
                    "connection state. A lock timeout raises an error without committing partial "
                    "work; retry the same business identity after backoff. Intake fingerprints the "
                    "complete submitted payload, making a conflicting replay visible instead of "
                    "silently accepting changed terms. The ranking score only prioritizes review "
                    "and cannot authorize enforcement. State changes use compare-and-swap checks "
                    "inside the same write transaction as their audit events. A hold cancels "
                    "prepared instructions without pretending that already completed external acts "
                    "can be undone. This provides race-free local posting and state transitions "
                    "under the stated single-database design. It does not manufacture an atomic "
                    "transaction across a bank, a court portal, and your database; those boundaries "
                    "require explicit acknowledgments and controlled reconciliation."
                ),
                (
                    "Treat a cleared receipt, an earned fee, and a completed client payment as "
                    "three different events. A $10,000 cleared recovery initially debits bank cash "
                    "and credits client payable by $10,000. When a contracted 30% fee is earned "
                    "and authorized, debit client payable $3,000 and credit service-fee revenue "
                    "$3,000. When the actual $7,000 client transfer is confirmed, debit client "
                    "payable and credit bank cash by $7,000. The remaining $3,000 is operator "
                    "cash before operating expenses, not another recovery. The reference makes "
                    "each receipt support only one fee allocation and one full net remittance; "
                    "installments enter as separate cleared receipts. Its reconciliation view "
                    "proves that bank cash equals client payable plus earned fees within this "
                    "limited subledger. It deliberately excludes operating expenses, taxes, "
                    "chargebacks, interest allocation, reimbursed litigation costs, and pooled "
                    "trust-account administration. Extend those through reviewed journal types "
                    "and explicit account mappings before using them, rather than editing posted "
                    "rows. Actual client-money handling must follow the relevant account and "
                    "professional rules; an ordinary SQLite file is not an escrow account. "
                    "Bank evidence establishes settlement, while the accounting policy and "
                    "contract establish when the service fee has been earned."
                ),
                (
                    "Keep external execution outside database transactions. The prepared-command "
                    "table is an instruction register, not an autonomous levy or payment engine. "
                    "A responsible actor rechecks the current hold status, verifies the intended "
                    "recipient and authority, executes through the proper system, and then records "
                    "the resulting evidence. Where a provider supports idempotency keys, reuse "
                    "the command identity; where it does not, an uncertain result goes to manual "
                    "reconciliation and is never automatically resent. Payment posting below "
                    "requires a bank-confirmation reference and therefore records a completed "
                    "transfer rather than initiating one. The application must obtain those "
                    "references from authenticated source records, not from untrusted debtor "
                    "messages. Separate permissions for intake, authorization, bank reconciliation, "
                    "and release of funds; the example functions assume trusted callers and "
                    "do not implement identity management. Protect the database directory, encrypt "
                    "storage through the deployment environment, back up through SQLite's backup "
                    "interface, and test restoration before production. Run QA after every import "
                    "and before closing the period. Failure of a balance, foreign-key, or event "
                    "cardinality check blocks downstream accounting exports. Preserve the failing "
                    "query results and resolve the underlying evidence instead of modifying "
                    "numbers until the dashboard appears balanced."
                ),
            ],
            "table": {
                "caption": "6-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and operational responsibility",
                    "Copy-pasteable Python and SQLite implementation",
                    "Concurrency boundary and evidence requirement",
                    "Acceptance test and production operating restriction",
                ],
                "rows": [
                    [
                        "Module one creates constrained storage and serialized transaction primitives",
                        '''import hashlib
import json
import sqlite3
from contextlib import contextmanager

DB = "judgment_recovery.sqlite3"

def digest(payload):
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

def connect():
    db = sqlite3.connect(DB, timeout=15, isolation_level=None)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("PRAGMA synchronous = FULL")
    db.execute("PRAGMA busy_timeout = 15000")
    return db

@contextmanager
def transaction():
    db = connect()
    try:
        db.execute("BEGIN IMMEDIATE")
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()

def initialize():
    db = connect()
    try:
        db.execute("PRAGMA journal_mode = WAL")
        db.executescript("""
        BEGIN IMMEDIATE;
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY,
            source TEXT NOT NULL,
            source_ref TEXT NOT NULL,
            payload_hash TEXT NOT NULL,
            face_cents INTEGER NOT NULL CHECK(face_cents > 0),
            fee_bps INTEGER NOT NULL CHECK(fee_bps BETWEEN 1 AND 9999),
            score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
            state TEXT NOT NULL DEFAULT 'review'
                CHECK(state IN ('review', 'verified', 'authorized', 'hold')),
            UNIQUE(source, source_ref)
        );
        CREATE TABLE IF NOT EXISTS state_events (
            event_key TEXT PRIMARY KEY,
            case_id INTEGER NOT NULL REFERENCES cases(id),
            prior_state TEXT NOT NULL,
            next_state TEXT NOT NULL,
            actor TEXT NOT NULL,
            evidence_ref TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS commands (
            command_key TEXT PRIMARY KEY,
            case_id INTEGER NOT NULL REFERENCES cases(id),
            action_ref TEXT NOT NULL,
            evidence_ref TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'prepared'
                CHECK(status IN ('prepared', 'cancelled')),
            UNIQUE(case_id, action_ref)
        );
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY,
            bank_ref TEXT NOT NULL UNIQUE,
            case_id INTEGER NOT NULL REFERENCES cases(id),
            gross_cents INTEGER NOT NULL CHECK(gross_cents > 0),
            payload_hash TEXT NOT NULL,
            cleared INTEGER NOT NULL CHECK(cleared = 1)
        );
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            event_key TEXT NOT NULL UNIQUE,
            evidence_ref TEXT NOT NULL UNIQUE,
            receipt_id INTEGER NOT NULL REFERENCES receipts(id),
            kind TEXT NOT NULL CHECK(kind IN ('receipt', 'fee', 'payout')),
            amount_cents INTEGER NOT NULL CHECK(amount_cents >= 0),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(receipt_id, kind)
        );
        CREATE TABLE IF NOT EXISTS ledger_lines (
            event_id INTEGER NOT NULL REFERENCES events(id),
            account TEXT NOT NULL
                CHECK(account IN ('bank', 'client_payable', 'fee_revenue')),
            signed_cents INTEGER NOT NULL,
            UNIQUE(event_id, account)
        );
        CREATE VIEW IF NOT EXISTS cash_reconciliation AS
        SELECT
            r.case_id,
            SUM(CASE WHEN l.account = 'bank'
                THEN l.signed_cents ELSE 0 END) AS bank_cents,
            -SUM(CASE WHEN l.account = 'client_payable'
                THEN l.signed_cents ELSE 0 END) AS client_due_cents,
            -SUM(CASE WHEN l.account = 'fee_revenue'
                THEN l.signed_cents ELSE 0 END) AS fee_cents,
            SUM(l.signed_cents) AS imbalance_cents
        FROM receipts AS r
        JOIN events AS e ON e.receipt_id = r.id
        JOIN ledger_lines AS l ON l.event_id = e.id
        GROUP BY r.case_id;
        COMMIT;
        """)
    finally:
        db.close()

initialize()''',
                        "Every writer acquires the SQLite write lock before reading mutable business state; durable uniqueness remains enforced inside the database.",
                        "Use a local filesystem supported by SQLite; initialize before workers start, and never share one connection across concurrent workers.",
                    ],
                    [
                        "Module two admits immutable intake identities and computes review priority",
                        '''def intake(source, source_ref, payload):
    if not source or not source_ref:
        raise ValueError("Stable source identity is required")
    required = (
        "face_cents", "fee_bps", "commercial", "authority_packet",
        "equity_evidence", "bankruptcy_checked", "stay_flag"
    )
    if any(key not in payload for key in required):
        raise ValueError("Complete screening evidence is required")
    for key in ("face_cents", "fee_bps"):
        if type(payload[key]) is not int:
            raise ValueError("Amounts and basis points must be integers")
    for key in required[2:]:
        if type(payload[key]) is not bool:
            raise ValueError("Screening flags must be explicit booleans")
    if payload["face_cents"] <= 0:
        raise ValueError("Positive judgment balance is required")
    if not 1 <= payload["fee_bps"] <= 9999:
        raise ValueError("Contracted basis points are outside supported limits")
    if not payload["commercial"]:
        raise ValueError("Route this obligation to a separate review track")
    score = (
        30 * int(payload["authority_packet"])
        + 40 * int(payload["equity_evidence"])
        + 30 * int(payload["bankruptcy_checked"])
    )
    if payload["stay_flag"]:
        score = 0
    fingerprint = digest(payload)
    with transaction() as db:
        db.execute(
            """INSERT INTO cases
            (source, source_ref, payload_hash, face_cents, fee_bps, score, state)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(source, source_ref) DO NOTHING""",
            (
                source, source_ref, fingerprint, payload["face_cents"],
                payload["fee_bps"], score,
                "hold" if payload["stay_flag"] else "review"
            )
        )
        row = db.execute(
            "SELECT id, payload_hash FROM cases WHERE source=? AND source_ref=?",
            (source, source_ref)
        ).fetchone()
        if row["payload_hash"] != fingerprint:
            raise ValueError("Conflicting intake replay requires documented review")
        return row["id"]''',
                        "The stable source pair and payload fingerprint prevent simultaneous imports from creating duplicate cases or silently changing original terms.",
                        "Submit the same payload twice and receive one case identity; submit changed terms under that identity and receive an explicit error.",
                    ],
                    [
                        "Module three controls verification, client-fund release authority, and prepared instructions",
                        '''ALLOWED_TRANSITIONS = {
    ("review", "verified"),
    ("verified", "authorized"),
    ("review", "hold"),
    ("verified", "hold"),
    ("authorized", "hold"),
    ("hold", "review"),
}

def transition(case_id, prior, target, event_key, actor, evidence_ref):
    if (prior, target) not in ALLOWED_TRANSITIONS:
        raise ValueError("Unsupported state transition")
    if not all((event_key, actor, evidence_ref)):
        raise ValueError("Event identity, actor, and evidence are required")
    expected = (case_id, prior, target, actor, evidence_ref)
    with transaction() as db:
        previous = db.execute(
            """SELECT case_id, prior_state, next_state, actor, evidence_ref
            FROM state_events WHERE event_key=?""", (event_key,)
        ).fetchone()
        if previous:
            if tuple(previous) != expected:
                raise ValueError("Conflicting state-event replay")
            return
        changed = db.execute(
            "UPDATE cases SET state=? WHERE id=? AND state=?",
            (target, case_id, prior)
        ).rowcount
        if changed != 1:
            raise ValueError("Case state changed; refresh evidence before retry")
        db.execute(
            """INSERT INTO state_events
            (event_key, case_id, prior_state, next_state, actor, evidence_ref)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (event_key,) + expected
        )
        if target == "hold":
            db.execute(
                """UPDATE commands SET status='cancelled'
                WHERE case_id=? AND status='prepared'""", (case_id,)
            )

def prepare_command(case_id, command_key, action_ref, evidence_ref):
    if not all((command_key, action_ref, evidence_ref)):
        raise ValueError("Instruction identity and evidence are required")
    with transaction() as db:
        case = db.execute(
            "SELECT state FROM cases WHERE id=?", (case_id,)
        ).fetchone()
        if case is None or case["state"] != "authorized":
            raise ValueError("Current case authority does not permit preparation")
        old = db.execute(
            """SELECT case_id, action_ref, evidence_ref, status
            FROM commands WHERE command_key=?""", (command_key,)
        ).fetchone()
        if old:
            if tuple(old) != (case_id, action_ref, evidence_ref, "prepared"):
                raise ValueError("Conflicting or cancelled instruction replay")
            return command_key
        db.execute(
            """INSERT INTO commands
            (command_key, case_id, action_ref, evidence_ref)
            VALUES (?, ?, ?, ?)""",
            (command_key, case_id, action_ref, evidence_ref)
        )
        return command_key''',
                        "Authority checks and instruction insertion share one serialized transaction; a concurrent hold either precedes preparation or cancels the prepared record.",
                        "Prepared records never execute external actions; recheck authority at execution and manually resolve uncertain external acknowledgments before any resend.",
                    ],
                    [
                        "Module four posts cleared receipts and contract-based earned-fee allocations",
                        '''def write_event(db, event_key, evidence_ref, receipt_id, kind, amount, lines):
    if not event_key or not evidence_ref:
        raise ValueError("Unique event and source evidence identities are required")
    if type(amount) is not int or amount < 0:
        raise ValueError("Event amount must be nonnegative integer cents")
    if sum(value for account, value in lines) != 0:
        raise ValueError("Journal entries must balance")
    old = db.execute(
        """SELECT id, evidence_ref, receipt_id, kind, amount_cents
        FROM events WHERE event_key=?""", (event_key,)
    ).fetchone()
    if old:
        if tuple(old)[1:] != (evidence_ref, receipt_id, kind, amount):
            raise ValueError("Conflicting money-event replay")
        return old["id"]
    cursor = db.execute(
        """INSERT INTO events
        (event_key, evidence_ref, receipt_id, kind, amount_cents)
        VALUES (?, ?, ?, ?, ?)""",
        (event_key, evidence_ref, receipt_id, kind, amount)
    )
    event_id = cursor.lastrowid
    db.executemany(
        "INSERT INTO ledger_lines VALUES (?, ?, ?)",
        [(event_id, account, value) for account, value in lines]
    )
    return event_id

def post_receipt(case_id, bank_ref, gross_cents):
    if not bank_ref or type(gross_cents) is not int or gross_cents <= 0:
        raise ValueError("Cleared bank identity and positive integer cents required")
    fingerprint = digest([case_id, bank_ref, gross_cents])
    with transaction() as db:
        db.execute(
            """INSERT INTO receipts
            (bank_ref, case_id, gross_cents, payload_hash, cleared)
            VALUES (?, ?, ?, ?, 1)
            ON CONFLICT(bank_ref) DO NOTHING""",
            (bank_ref, case_id, gross_cents, fingerprint)
        )
        receipt = db.execute(
            "SELECT id, payload_hash FROM receipts WHERE bank_ref=?", (bank_ref,)
        ).fetchone()
        if receipt["payload_hash"] != fingerprint:
            raise ValueError("Conflicting cleared-receipt replay")
        write_event(
            db, "receipt:" + bank_ref, "bank-receipt:" + bank_ref,
            receipt["id"], "receipt", gross_cents,
            [("bank", gross_cents), ("client_payable", -gross_cents)]
        )
        return receipt["id"]

def allocate(receipt_id, kind, event_key, evidence_ref):
    if kind not in ("fee", "payout"):
        raise ValueError("Only fee or payout allocation is supported")
    if kind == "fee" and not evidence_ref.startswith("earned:"):
        raise ValueError("Earned-fee review evidence is required")
    if kind == "payout" and not evidence_ref.startswith("bank-paid:"):
        raise ValueError("Completed bank-transfer evidence is required")
    with transaction() as db:
        row = db.execute(
            """SELECT r.gross_cents, c.fee_bps, c.state
            FROM receipts AS r JOIN cases AS c ON c.id=r.case_id
            WHERE r.id=? AND r.cleared=1""", (receipt_id,)
        ).fetchone()
        if row is None:
            raise ValueError("A cleared receipt is required")
        gross = row["gross_cents"]
        fee = (gross * row["fee_bps"] + 5000) // 10000
        amount = fee if kind == "fee" else gross - fee
        lines = (
            [("client_payable", fee), ("fee_revenue", -fee)]
            if kind == "fee"
            else [("client_payable", amount), ("bank", -amount)]
        )
        replay = db.execute(
            "SELECT id FROM events WHERE event_key=?", (event_key,)
        ).fetchone()
        if replay:
            return write_event(
                db, event_key, evidence_ref, receipt_id, kind, amount, lines
            )
        if row["state"] != "authorized":
            raise ValueError("New allocation requires current case authorization")
        if kind == "payout":
            earned = db.execute(
                """SELECT amount_cents FROM events
                WHERE receipt_id=? AND kind='fee'""", (receipt_id,)
            ).fetchone()
            if earned is None or earned["amount_cents"] != fee:
                raise ValueError("Post the supported earned fee before remittance")
        return write_event(
            db, event_key, evidence_ref, receipt_id, kind, amount, lines
        )''',
                        "Receipt identity, natural event identity, and source evidence are independently unique; cash journals and both ledger lines commit together or fully roll back.",
                        "Only authenticated cleared-bank records enter post_receipt; allocate records earned fees or completed payments and cannot initiate a bank transfer.",
                    ],
                    [
                        "Module five exposes reconciliation totals without mixing principal and revenue",
                        '''def reconciliation_rows():
    db = connect()
    try:
        return [
            dict(row) for row in db.execute(
                """SELECT case_id, bank_cents, client_due_cents, fee_cents,
                imbalance_cents
                FROM cash_reconciliation ORDER BY case_id"""
            )
        ]
    finally:
        db.close()

def reconcile_bank(verified_subledger_bank_cents):
    if type(verified_subledger_bank_cents) is not int:
        raise ValueError("Bank comparison must use integer cents")
    rows = reconciliation_rows()
    for row in rows:
        if row["imbalance_cents"] != 0:
            raise ValueError("Case journal imbalance detected")
        if row["bank_cents"] != row["client_due_cents"] + row["fee_cents"]:
            raise ValueError("Cash allocation equation failed")
        if row["client_due_cents"] < 0:
            raise ValueError("Client liability became negative")
    recorded = sum(row["bank_cents"] for row in rows)
    if recorded != verified_subledger_bank_cents:
        raise ValueError("Verified bank balance does not match subledger cash")
    return {
        "bank_cents": recorded,
        "client_due_cents": sum(row["client_due_cents"] for row in rows),
        "fee_cents": sum(row["fee_cents"] for row in rows),
    }''',
                        "A single read snapshot supplies each report; bank reconciliation compares the exact subledger scope rather than unrelated operating-account movements.",
                        "Reconcile account-level timing differences separately; export fee_cents as recognized service revenue only after the earned-fee evidence review.",
                    ],
                    [
                        "Module six checks journal integrity and proves duplicate-event behavior",
                        '''def qa_checks():
    db = connect()
    try:
        db.execute("BEGIN")
        if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise AssertionError("Database integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise AssertionError("Broken foreign-key relationships")
        broken = db.execute(
            """SELECT e.id
            FROM events AS e LEFT JOIN ledger_lines AS l ON l.event_id=e.id
            GROUP BY e.id
            HAVING COUNT(l.account) != 2 OR COALESCE(SUM(l.signed_cents), 0) != 0"""
        ).fetchall()
        if broken:
            raise AssertionError("Unbalanced or incomplete event journals")
        missing = db.execute(
            """SELECT r.id FROM receipts AS r
            LEFT JOIN events AS e ON e.receipt_id=r.id AND e.kind='receipt'
            WHERE e.id IS NULL"""
        ).fetchall()
        if missing:
            raise AssertionError("Receipt exists without its cash event")
        for event in db.execute(
            """SELECT e.id, e.kind, e.amount_cents, r.gross_cents, c.fee_bps
            FROM events AS e
            JOIN receipts AS r ON r.id=e.receipt_id
            JOIN cases AS c ON c.id=r.case_id"""
        ).fetchall():
            gross = event["gross_cents"]
            fee = (gross * event["fee_bps"] + 5000) // 10000
            if event["kind"] == "receipt":
                amount = gross
                expected = {"bank": gross, "client_payable": -gross}
            elif event["kind"] == "fee":
                amount = fee
                expected = {"client_payable": fee, "fee_revenue": -fee}
            else:
                amount = gross - fee
                expected = {"client_payable": amount, "bank": -amount}
            actual = {
                row["account"]: row["signed_cents"]
                for row in db.execute(
                    "SELECT account, signed_cents FROM ledger_lines WHERE event_id=?",
                    (event["id"],)
                )
            }
            if event["amount_cents"] != amount or actual != expected:
                raise AssertionError("Event allocation differs from contract arithmetic")
        orphan_payouts = db.execute(
            """SELECT p.id FROM events AS p
            LEFT JOIN events AS f
              ON f.receipt_id=p.receipt_id AND f.kind='fee'
            WHERE p.kind='payout' AND f.id IS NULL"""
        ).fetchall()
        if orphan_payouts:
            raise AssertionError("Client payout lacks an earned-fee allocation")
        db.commit()
    finally:
        db.close()

def smoke_test():
    global DB
    import os
    import tempfile

    original = DB
    with tempfile.TemporaryDirectory() as directory:
        DB = os.path.join(directory, "test.sqlite3")
        try:
            initialize()
            payload = {
                "face_cents": 1000000, "fee_bps": 3000,
                "commercial": True, "authority_packet": True,
                "equity_evidence": True, "bankruptcy_checked": True,
                "stay_flag": False
            }
            case_id = intake("test-court", "test-case", payload)
            assert intake("test-court", "test-case", payload) == case_id
            transition(case_id, "review", "verified", "v1", "reviewer", "packet:1")
            transition(case_id, "verified", "authorized", "a1", "reviewer", "plan:1")
            receipt_id = post_receipt(case_id, "bank:1", 1000000)
            assert post_receipt(case_id, "bank:1", 1000000) == receipt_id
            allocate(receipt_id, "fee", "fee:1", "earned:review:1")
            allocate(receipt_id, "fee", "fee:1", "earned:review:1")
            allocate(receipt_id, "payout", "payout:1", "bank-paid:transfer:1")
            allocate(receipt_id, "payout", "payout:1", "bank-paid:transfer:1")
            assert reconcile_bank(300000) == {
                "bank_cents": 300000, "client_due_cents": 0, "fee_cents": 300000
            }
            transition(case_id, "authorized", "hold", "h1", "reviewer", "petition:1")
            try:
                prepare_command(case_id, "instruction:2", "levy:2", "review:2")
            except ValueError:
                pass
            else:
                raise AssertionError("Held case accepted a new instruction")
            qa_checks()
        finally:
            DB = original

# Run smoke_test() explicitly in an isolated test process.
# Extend testing with concurrent workers before deployment.''',
                        "QA reads one database snapshot; duplicate-event tests demonstrate local idempotency without sending court filings, messages, or payments to external systems.",
                        "The supplied smoke test is a reference and has not been executed here; add contention, timeout, restoration, and external-acknowledgment tests before deployment.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before Live Cash or Enforcement",
                "body": (
                    "The reference deliberately separates database integrity from legal authority, "
                    "access control, and actual custody of client funds."
                ),
                "items": [
                    "Verify collection licensing, creditor authority, debt classification, counsel responsibilities, and the latest bankruptcy evidence for the jurisdiction.",
                    "Verify that every case state change identifies an authorized reviewer and a retrievable evidence record through the production access-control layer.",
                    "Verify the designated client-money account, contractual fee treatment, cleared-bank source, and independently confirmed recipient before releasing funds.",
                    "Verify duplicate handling, competing-worker behavior, backup restoration, and manual handling of uncertain external actions before enabling production integrations.",
                ],
            },
        },
        {
            "heading": "3. Route the Medical-Receivables Play Through Its Own Eligibility and Evidence Track",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The mapped play hospital_lien_medical_receivables_arbitrage is the Out-of-Network "
                    "Medical Claim & ERISA Appeal Contingency Recovery track, identified as TRACK_1. "
                    "Despite its internal identifier, an underpaid insurance claim is not automatically "
                    "a hospital lien, an assigned judgment, or an executable asset. Partner intake "
                    "may include surgical centers, air or ground ambulance operators, and specialty "
                    "clinics, but separate those populations before selecting a recovery mechanism. "
                    "Federal No Surprises Act payment dispute procedures apply only to eligible "
                    "items and services; ground ambulance services generally fall outside that "
                    "federal framework. A state payment rule, plan appeal, negotiated correction, "
                    "or other supported route may apply instead. Capture service date, provider "
                    "type, emergency status, network status, plan funding information, payer, "
                    "initial payment or denial date, applicable state-law determination, and "
                    "the relevant remittance identifiers. Do not infer federal IDR eligibility "
                    "from an out-of-network label alone. For eligible disputes, 45 CFR 149.510 "
                    "provides the open-negotiation and federal independent dispute resolution "
                    "framework. The operator should build deadline evidence and validated submission "
                    "packages, while qualified reviewers resolve eligibility and legal interpretation. "
                    "Automating a filing with the wrong payer, wrong service grouping, or wrong "
                    "jurisdiction can convert an apparently attractive recovery into unrecoverable "
                    "fees and lost time."
                ),
                (
                    "For the federal route, ordinarily initiate the 30-business-day open-negotiation "
                    "period within 30 business days after receipt of the initial payment or notice "
                    "of denial, then observe the four-business-day initiation window after that "
                    "negotiation period ends, subject to applicable extensions and current rules. "
                    "Store delivery evidence and calculate deadlines from the actual triggering "
                    "event, not from the date a spreadsheet reached your office. Validate batching "
                    "and administrative requirements against the live federal process before "
                    "submission. If the IDR window has elapsed, examine whether an ERISA "
                    "administrative appeal remains available; group-health claim procedures generally "
                    "provide at least 180 days to appeal an adverse benefit determination under "
                    "29 CFR 2560.503-1(h)(3)(i). That is a separate remedy with its own eligibility, "
                    "record, exhaustion, and timing requirements, not an automatic extension of "
                    "IDR. Obtain the plan documents, denial rationale, appeal instructions, and "
                    "valid representative authorization. An assignment may encounter an anti-assignment "
                    "clause, and authorization to assist does not itself establish litigation standing "
                    "under 29 U.S.C. 1132. If neither route survives review, stop paid work or "
                    "negotiate a documented correction rather than manufacturing a statutory "
                    "deadline or promising that every denial can be monetized."
                ),
                (
                    "Price the play on incremental recovered cash, with the contract defining the "
                    "baseline and exclusions. If the eligible incremental recovery is $100,000, "
                    "a 20% fee yields $20,000 of operator revenue and $80,000 attributable "
                    "to the client before separately agreed expenses; a 35% fee yields $35,000 "
                    "and $65,000 respectively. At 30%, the split is $30,000 and $70,000. "
                    "A preexisting payer payment cannot be counted again simply because the "
                    "operator imported its remittance. Match X12 837 claims, 835 remittances, "
                    "claim identifiers, service lines, reversals, and appeal outcomes through an "
                    "encrypted, access-controlled pipeline. Where the relationship requires one, "
                    "execute the business associate agreement before receiving protected health "
                    "information and apply the HIPAA Security Rule's technical safeguards. "
                    "Ordinary project SQLite is not a complete health-data security architecture. "
                    "Keep clinical attachments outside general collection dashboards and minimize "
                    "the fields visible to each role. Budget dispute fees, medical review, and "
                    "appeal labor against expected incremental collections; a $4,000 expected "
                    "fee cannot support unlimited expert review. This branch illustrates one "
                    "of the volume's 15 mapped plays, not extra revenue to add to the canonical "
                    "scorecard. Count its earned fees within the same annual service-revenue "
                    "total if deployed."
                ),
            ],
            "table": {
                "caption": "TRACK_1 Medical Receivables Eligibility, Unit Economics, and Risk Fallbacks",
                "headers": [
                    "Play component and intake population",
                    "Required mechanics and primary legal reference",
                    "Concrete economics and recognition treatment",
                    "Failure mode and supported fallback route",
                ],
                "rows": [
                    [
                        "hospital_lien_medical_receivables_arbitrage operates as a separate TRACK_1 claims branch",
                        "Confirm provider authority, recovery contract, claim ownership, and plan-specific representation requirements",
                        "At 30% of $100,000 incremental recovery, recognize $30,000 service revenue",
                        "Keep insurance claims outside judgment enforcement until an enforceable judgment actually exists",
                    ],
                    [
                        "Surgical-center and specialty-clinic claims require service-level eligibility review",
                        "Check federal scope, applicable state payment rules, network facts, and denial evidence",
                        "At 20%, a $25,000 incremental recovery supports a $5,000 operator fee",
                        "Route ineligible federal disputes to supported appeals or negotiated payer corrections",
                    ],
                    [
                        "Air-ambulance and ground-ambulance claims must enter different routing queues",
                        "Assess eligible air-ambulance disputes under federal rules without extending coverage to ground transport",
                        "A $12,000 recovery at 35% produces $4,200 before operator expenses",
                        "For ground transport, examine applicable state rules and plan appeal rights",
                    ],
                    [
                        "Federal IDR submissions require documented negotiation and initiation windows",
                        "Apply 45 CFR 149.510 timing, eligibility, current process requirements, and delivery evidence",
                        "Subtract dispute fees and review expense before assigning the next spending budget",
                        "When the federal window lapses, examine a still-timely independent appeal route",
                    ],
                    [
                        "ERISA administrative appeals require plan documents and representative authority",
                        "Apply 29 CFR 2560.503-1 and evaluate standing separately under 29 U.S.C. 1132",
                        "A $10,000 recovery at 30% leaves $3,000 for operator cost coverage",
                        "Do not treat an expired appeal period or defective assignment as recoverable inventory",
                    ],
                    [
                        "Encrypted EDI and restricted document storage support the entire medical branch",
                        "Execute required BAAs and apply 45 CFR 164.312 technical safeguards",
                        "Count only incremental cleared collections supported by matched remittance and claim records",
                        "Quarantine unmatched remittances and restrict health-data access until identity and purpose are verified",
                    ],
                ],
            },
        },
        {
            "heading": "4. Walk Three Cohorts Without Turning Pipeline Principal Into Revenue",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a mature-operation illustration, not a "
                    "promise of first cash within three months. The canonical time to first deal "
                    "remains 6–24 months. This operator enters Month 1 with two previously "
                    "developed, authorized legacy batches, L1 and L2, that settle during Months "
                    "1 and 2. Each new monthly intake contains 40 sourced files; 24 are "
                    "screened out or held outside admission, and 16 enter the active cohort. "
                    "Across 90 days, that is 120 sourced files, 72 excluded or held, and "
                    "48 admitted. The Month 1 admitted cohort produces six paying files in "
                    "Month 3, abandons two after additional evidence destroys the recovery case, "
                    "and retains eight unresolved files. The Month 2 cohort abandons two and "
                    "retains fourteen; all sixteen Month 3 admissions remain unresolved at "
                    "quarter end. Thus six new-cohort files pay, four are abandoned, and "
                    "thirty-eight remain active. The twelve legacy paying files are additional "
                    "opening inventory, not newly sourced successes. This separation prevents "
                    "a misleading conversion rate and exposes the working-capital burden "
                    "of building replacement inventory while inherited matters generate cash. "
                    "Prior development costs belong to their original periods when assessing "
                    "full-lifecycle cohort returns."
                ),
                (
                    "Use a 30% contracted recovery fee for the worked cash arithmetic, distinct "
                    "from the Base scenario's coincidentally equal 30% owner-profit margin. "
                    "Months 1 and 2 each collect $77,777.80 of client recovery cash, "
                    "recognize $23,333.34 of earned service fees, and remit $54,444.46 "
                    "to clients. Month 3 collects $77,777.73, recognizes $23,333.32, "
                    "and remits $54,444.41. The three months therefore reconcile to "
                    "$233,333.33 recovered, $70,000 recognized revenue, and $163,333.33 "
                    "client distributions. The six paying files in each month average roughly "
                    "$12,962.96 recovered and $3,888.89 in fees; actual receipt allocations "
                    "use integer cents rather than those rounded averages. Deduct $8,000 "
                    "monthly fixed overhead plus variable delivery expense of $8,333.34, "
                    "$8,333.34, and $8,333.32. Total quarter expense is $49,000, "
                    "leaving $21,000 owner operating profit under the scorecard convention. "
                    "Abandoned-file investigation costs are already inside variable expense, "
                    "not additional deductions. This distinguishes the supplied $2,000–$12,000 "
                    "monthly overhead range from total delivery-inclusive costs. All modeled "
                    "receipts clear, fees become earned, client transfers complete, and operating "
                    "bills are paid within the stated month; different timing changes cash, "
                    "even when the earned revenue eventually matches."
                ),
                (
                    "Annualizing the quarter produces exactly $280,000 service revenue, $196,000 "
                    "expense, and $84,000 owner net profit: the canonical Base case with "
                    "one full-time operator and three contractors. The Conservative case stays "
                    "$60,000 revenue, $48,000 expense, and $12,000 profit at 20%, "
                    "also with one full-time operator and three contractors. Scaled stays "
                    "$500,000 revenue, $300,000 expense, and $200,000 profit at 40%, "
                    "with two full-time operators and four contractors. These are separate "
                    "operating scenarios, not stages guaranteed by the cohort. Start the cash "
                    "walk with $30,000 unrestricted operator capital, within the stated "
                    "$10,000–$75,000 startup range, and exclude client money from that "
                    "reserve. Net monthly operating cash of $7,000 produces ending unrestricted "
                    "balances of $37,000, $44,000, and $51,000 without owner draws. "
                    "If one month's expected fee receipts slip while modeled bills still "
                    "fall due, the business must fund $16,333.34 of expense from its "
                    "own reserve rather than borrowing client principal. Track that delay "
                    "sensitivity beside the attractive annual margin. Refresh cohort status, "
                    "bankruptcy checks, unspent budgets, and expected receipt dates weekly. "
                    "Scale only after fee receipts, expense evidence, and outstanding client "
                    "liabilities reconcile across successive closes, not because the docket "
                    "pipeline contains a larger nominal judgment balance."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period, lead cohort, and file disposition",
                    "Cleared recovery timing and fee recognition",
                    "Client remittance, overhead, and delivery expense",
                    "Operator cash flow and reconciliation checkpoint",
                ],
                "rows": [
                    [
                        "Month 1 sources 40 files; exclude 12 for insolvency, eight for priority deficits, and hold four for stays; admit cohort M1 with 16 files.",
                        "Legacy batch L1 supplies six paying files, $77,777.80 recovered cash, and $23,333.34 earned fees; newly admitted M1 generates no receipts yet.",
                        "Remit $54,444.46 to clients; pay $8,000 fixed overhead and $8,333.34 variable delivery expense, including current investigative work.",
                        "Operator net cash increases $7,000; cumulative operating cash is $7,000, and the $30,000 opening reserve becomes $37,000.",
                    ],
                    [
                        "Month 2 sources 40 files; exclude ten for insolvency, ten for priority deficits, and hold four for stays; admit cohort M2 with 16 files.",
                        "Legacy batch L2 supplies six paying files, $77,777.80 recovered cash, and $23,333.34 earned fees; M1 abandons two files after further review.",
                        "Remit $54,444.46 to clients; pay $8,000 fixed overhead and $8,333.34 variable delivery expense, already including abandoned-file investigation costs.",
                        "Operator net cash increases $7,000; cumulative operating cash reaches $14,000, and unrestricted ending cash reaches $44,000 without draws.",
                    ],
                    [
                        "Month 3 sources 40 files; exclude fourteen for insolvency, six for priority deficits, and hold four for stays; admit cohort M3 with 16 files.",
                        "M1 supplies six paying files, $77,777.73 recovered cash, and $23,333.32 earned fees; M2 abandons two files while M3 remains developing.",
                        "Remit $54,444.41 to clients; pay $8,000 fixed overhead and $8,333.32 variable delivery expense, including all current-quarter loss investigation costs.",
                        "Operator net cash increases $7,000; cumulative operating cash reaches $21,000, and unrestricted ending cash reaches $51,000 without draws.",
                    ],
                    [
                        "Quarter-end cohort roll-forward shows 120 sourced, 72 excluded or held, 48 admitted, six paying, four abandoned, and 38 active new-cohort files.",
                        "Eighteen total paying files include twelve legacy matters; combined recoveries are $233,333.33 and recognized service fees total exactly $70,000.",
                        "Client distributions total $163,333.33; fixed overhead totals $24,000 and variable delivery expense totals $25,000, producing $49,000 total expense.",
                        "Subtracting $49,000 expense from $70,000 fees yields $21,000 profit; all modeled client liabilities are discharged after completed monthly remittances.",
                    ],
                    [
                        "Base annualization repeats the mature quarterly economics four times without treating unresolved new files as automatically successful future collections.",
                        "Four quarters of $70,000 recognized fees produce exactly $280,000 annual revenue; recovered client principal remains outside the operator revenue total.",
                        "Four quarters of $49,000 operating expense produce $196,000 annual expense, comprising $96,000 fixed overhead and $100,000 variable delivery costs.",
                        "Annual owner profit is $84,000 at 30.0%, supported by the canonical Base staffing of one full-time operator and three contractors.",
                    ],
                    [
                        "Liquidity sensitivity shifts one expected fee-receipt month without changing the obligation to protect client money or pay committed operator bills.",
                        "A delayed $23,333.34 fee receipt reduces that month's cash inflow; no revenue is invented to fill the resulting cash timing gap.",
                        "The operator must fund $16,333.34 of scheduled expenses from unrestricted capital if that month produces no other operator receipts.",
                        "A $30,000 opening reserve falls to $13,666.66 in that isolated delayed-receipt month; client principal never funds the shortfall.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A judgment balance is inventory; only an earned, reconciled fee is operator revenue.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one evidence-backed case identity and verify creditor authority, obligation type, enforcement rights, and current bankruptcy status before admission.",
        "Estimate realizable equity after senior claims, exemptions, and execution expense; approve a capped next-stage budget rather than an open-ended enforcement mandate.",
        "Install the six ledger modules in an isolated project, run the supplied smoke test, and add concurrent-worker, recovery, and permission tests before live deployment.",
        "Require authenticated cleared-bank evidence, earned-fee review, and completed-transfer confirmation for the three separate cash events.",
        "Route hospital_lien_medical_receivables_arbitrage through service-level federal eligibility checks, protected EDI handling, required BAAs, and independently evaluated ERISA appeal windows.",
        "Close the 90-day cohort with separate legacy and new-file counts, $70,000 recognized fees, $49,000 expense, $21,000 owner profit, and reconciled client distributions.",
    ],
    "statutory_citations": [
        {
            "title": "11 U.S.C. 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": (
                "A bankruptcy filing can stay judgment enforcement and collection activity; "
                "record the petition evidence and have counsel determine scope and exceptions."
            ),
        },
        {
            "title": "15 U.S.C. 1692a(5) — Definition of debt",
            "url": "https://www.law.cornell.edu/uscode/text/15/1692a",
            "relevance": (
                "Classify the underlying obligation by its actual purpose rather than assuming "
                "all judgments fall within, or outside, federal consumer-debt collection rules."
            ),
        },
        {
            "title": "28 U.S.C. 1654 — Appearance personally or by counsel",
            "url": "https://www.law.cornell.edu/uscode/text/28/1654",
            "relevance": (
                "Federal appearance authority requires separate analysis; owning an assignment "
                "does not itself authorize a nonlawyer to represent another party."
            ),
        },
        {
            "title": "UCC Section 9-317 — Interests taking priority over an unperfected security interest",
            "url": "https://www.law.cornell.edu/ucc/9/9-317",
            "relevance": (
                "Provides the model-law priority framework for specified lien-creditor contests; "
                "verify the enacted state provision and distinguish real-property lien rules."
            ),
        },
        {
            "title": "42 U.S.C. 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes federal surprise-billing protections and relevant payment-dispute "
                "mechanics for eligible services, rather than all out-of-network claims."
            ),
        },
        {
            "title": "45 CFR 149.510 — Federal independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.510",
            "relevance": (
                "Controls federal IDR eligibility and process requirements, including open "
                "negotiation and initiation timing used by the medical-receivables branch."
            ),
        },
        {
            "title": "29 CFR 2560.503-1 — Claims procedure",
            "url": "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XXV/subchapter-G/part-2560/section-2560.503-1",
            "relevance": (
                "Provides ERISA claims-procedure requirements, including the group-health "
                "appeal period and review process that must be assessed independently of IDR."
            ),
        },
        {
            "title": "29 U.S.C. 1132 — ERISA civil enforcement",
            "url": "https://www.law.cornell.edu/uscode/text/29/1132",
            "relevance": (
                "Requires separate attention to who may pursue civil enforcement; assistance "
                "authorization and an assignment do not automatically resolve standing."
            ),
        },
        {
            "title": "45 CFR 164.502(e) and 164.504(e) — Business associate relationships",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Structure required business associate arrangements before transferring protected "
                "health information into the medical-claims recovery workflow."
            ),
        },
        {
            "title": "45 CFR 164.312 — Technical safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312",
            "relevance": (
                "Apply access controls, audit controls, integrity protections, authentication, "
                "and transmission security to protected electronic health information."
            ),
        },
    ],
}
