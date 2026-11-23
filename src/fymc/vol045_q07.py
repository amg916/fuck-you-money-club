from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "idr-production-blueprint-and-90-day-cohort-walk",
    "question_prompt": "How does an operator execute no surprises act (idr) medical arbitration & out-of-network recovery end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "835 Remittance Intake, Federal Jurisdiction Screening, Business-Day Deadlines, SQLite Settlement Controls, and Cash-Only Contingency Accounting",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #45, Rank #09 of 49, scores 94/100 by converting specialized claim recovery "
        "into a tightly controlled small-team operation. This chapter operationalizes 12 mapped "
        "plays, including a separately bounded WOTC and research-credit documentation analogue. "
        "The production spine joins authorized 835 intake, federal-versus-state screening, "
        "documented negotiation, timely IDR initiation, evidence preparation, and bank-confirmed "
        "settlement. Six executable reference modules demonstrate integer-cent accounting, "
        "serialized writes, duplicate rejection, and auditable fee statements. A worked "
        "90-day mature-book walk reconciles $126,250 of operator revenue and $54,287.50 of "
        "owner profit to the annual Base case. Annual owner profits remain $33,000 Conservative, "
        "$217,150 Base, and $504,000 Scaled; underlying provider receipts and unpaid awards "
        "never become operator revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned operator contingency revenue, excluding baseline provider collections",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned operator contingency revenue, excluding baseline provider collections",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned operator contingency revenue, excluding baseline provider collections",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an admissible claim inventory before buying arbitration capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Begin with provider authority, a HIPAA Business Associate Agreement, and a "
                    "read-only remittance feed rather than a spreadsheet of attractive charges. "
                    "Obtain the original 837 claim, every associated 835 transaction, the explanation "
                    "of benefits, relevant plan documents, service location, provider specialty, "
                    "service date, and proof of initial payment or denial receipt. Parse CARC and "
                    "RARC combinations into review queues, but never let an adjustment code establish "
                    "federal jurisdiction by itself. A plan administrator's identity does not establish "
                    "whether the coverage is self-funded, fully insured, or governed by an applicable "
                    "state payment regime. For each claim, preserve the evidence supporting the "
                    "applicable federal or state route and the person who verified it. Screen the "
                    "covered service category, network relationships, emergency circumstances, facility "
                    "status, and any relevant notice-and-consent facts. Federal IDR is not a universal "
                    "appeal mechanism for every denied medical claim. Reject duplicates, contract "
                    "disputes outside this pathway, and unsupported eligibility assertions before "
                    "paying a filing-related fee. This first screen makes the difference between a "
                    "recoverable underpayment and an expensive administrative rejection. Store the "
                    "initial payer allowance and actual initial cash separately; neither field is "
                    "automatically the QPA."
                ),
                (
                    "Build one immutable claim identity from the provider identifier, payer claim "
                    "control number, service-line identity, and service date, retaining an alias map "
                    "for corrected claims. The reference ledger uses a provider-scoped claim key "
                    "and rejects a second enrollment even when a different cohort label is supplied. "
                    "A corrected remittance updates the economic evidence through an adjustment "
                    "event; it does not create another billable recovery. Attach a document manifest "
                    "containing secure object references, hashes, source timestamps, and access "
                    "restrictions. Keep clinical records outside the SQLite demonstration database, "
                    "which is an accounting reference rather than an encrypted records repository. "
                    "Use restricted storage such as an appropriately configured Amazon S3 deployment "
                    "under the required service agreement, with separate access roles for intake, "
                    "clinical review, and settlement. Export only the minimum evidence needed by "
                    "the authorized recipient. Score priority using documented incremental recovery "
                    "potential, remaining time, evidence completeness, expected unrecovered fees, and "
                    "review minutes. A $4,000 potential increment with $800 of entity-fee exposure "
                    "is a different assignment from a $600 increment with identical exposure. "
                    "Where the record is incomplete, request the missing evidence or decline the "
                    "case instead of manufacturing a favorable eligibility classification."
                ),
                (
                    "Maintain an externally reviewed business-day calendar and version every deadline "
                    "calculation. The usual federal sequence starts with the window for initiating "
                    "open negotiation within 30 business days after receipt of the initial payment "
                    "or denial, followed by a 30-business-day negotiation period and a four-business-day "
                    "IDR initiation window after that period ends. The four-day window concerns "
                    "initiation, not a universal batching or entity-selection period. Preserve "
                    "delivery evidence, recipient addresses, portal acknowledgments, and the calendar "
                    "version used; an internal task completion flag is not evidence of service. "
                    "Route extensions, portal interruptions, and disputed receipt dates to a named "
                    "reviewer using the applicable current process rather than silently extending "
                    "a deadline. For the 90-day cooling-off restriction, identify the initiating "
                    "party, noninitiating party, and relevant same or similar items or services "
                    "under the governing rule. Do not implement a simplistic payer-and-CPT lock "
                    "that ignores party identity or applicable exceptions. Batching likewise requires "
                    "a current eligibility test, not merely a shared spreadsheet tab. Plays one "
                    "through seven below turn these requirements into assigned queues, artifacts, "
                    "and measurable stop conditions before any arbitration package is released."
                ),
            ],
            "table": {
                "caption": "Mapped Plays 1–7: Authorized Intake Through Federal IDR Initiation",
                "headers": [
                    "Mapped operating play",
                    "Required production artifact",
                    "Unit economics and workload measure",
                    "Failure response and accountable owner",
                ],
                "rows": [
                    [
                        "Play 1 — Provider-authorized remittance ingestion and identity resolution",
                        "Signed service authority, executed BAA, and hashed remittance source manifest",
                        "One hundred monthly leads enter one provider-scoped duplicate-control queue",
                        "Intake lead quarantines unmatched remittances before creating any recovery mandate",
                    ],
                    [
                        "Play 2 — CARC and RARC recovery-priority classification",
                        "Original adjustment codes linked to clinical and payment evidence",
                        "Rank a $4,000 potential increment above a $600 equivalent-exposure increment",
                        "Reviewer rejects code-only eligibility conclusions and requests supporting source records",
                    ],
                    [
                        "Play 3 — Federal versus state payment-route determination",
                        "Plan evidence, service category, location, and documented jurisdiction conclusion",
                        "Twenty of one hundred illustrative leads leave before entity-fee exposure",
                        "Jurisdiction reviewer routes state cases separately without federal filing charges",
                    ],
                    [
                        "Play 4 — Initial payment and incremental-recovery baseline locking",
                        "Original payer allowance, QPA disclosure when available, and initial cash evidence",
                        "A $1,000 initial payment remains excluded from a later $4,000 increment",
                        "Settlement reviewer investigates corrected remittances before changing the locked baseline",
                    ],
                    [
                        "Play 5 — Timely open-negotiation service and response tracking",
                        "Approved notice, receipt evidence, verified calendar, and negotiation correspondence",
                        "Track both the initiation window and the separate negotiation period",
                        "Deadline owner escalates missing delivery proof before treating negotiation as started",
                    ],
                    [
                        "Play 6 — Eligible batching and cooling-off restriction management",
                        "Party-specific restriction register and current-rule batching eligibility worksheet",
                        "Separate ineligible groupings before multiplying an illustrative $800 deposit exposure",
                        "Filing reviewer splits unsupported groups and documents the permitted alternative route",
                    ],
                    [
                        "Play 7 — Certified entity selection and timely IDR initiation",
                        "Portal acknowledgment, case identifier, selection record, and verified fee reserve",
                        "Eighty eligible illustrative filings create individually tracked deadlines and deposits",
                        "Assigned operator stops duplicate submission and reconciles uncertain portal outcomes manually",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before an external filing",
                "body": (
                    "The reviewer signs the evidence manifest, not a generic completeness checkbox. "
                    "No preparation token alone establishes that a notice or filing reached its recipient."
                ),
                "items": [
                    "Verify provider authority, the BAA, federal eligibility evidence, and the original payment or denial receipt artifact.",
                    "Recalculate the negotiation and initiation deadlines against the reviewed calendar, including any documented applicable extension.",
                    "Verify current batching conditions and the party-specific cooling-off register; separate claims that cannot share the proposed submission.",
                    "Confirm the actual fee schedule, provider-funded reserve, permitted evidence package, and named owner of the portal acknowledgment.",
                ],
            },
        },
        {
            "heading": "2. Install six reference modules with serialized ledger writes and explicit external handoffs",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The six reference modules below can be concatenated, in order, into one "
                    "Python 3.9 script and run against a local SQLite database. They use integer "
                    "cents, foreign keys, unique source identities, immutable money events, and "
                    "BEGIN IMMEDIATE transactions. Every read-modify-write operation acquires the "
                    "write reservation before reading the state it will change. Concurrent local "
                    "writers therefore cannot both claim the same preparation token or independently "
                    "advance the same case version. A repeated request succeeds only when its "
                    "recorded identity and contents match; conflicting reuse fails visibly. Keep "
                    "the database on a local filesystem supported by SQLite locking, not a shared "
                    "network drive, and give each process its own connection. A lock timeout "
                    "means the transaction did not complete and must be retried with the same "
                    "request identity. For multiple application hosts, port the transaction boundaries "
                    "to PostgreSQL with row locks and identical uniqueness constraints. These "
                    "guarantees cover the ledger, not a payer portal. No local database can "
                    "atomically commit an independent website submission. The design therefore "
                    "creates durable preparation work, permanently assigns it once claimed, and "
                    "requires external receipt reconciliation before recording successful service."
                ),
                (
                    "The state machine deliberately distinguishes readiness from completed delivery. "
                    "Verification records reviewed federal eligibility and a provider-controlled "
                    "reserve; it does not represent operator custody of client money. Queueing "
                    "open negotiation creates a preparation token, while confirmation requires a "
                    "unique receipt and the delivered date. The reviewer supplies the verified "
                    "negotiation end and IDR deadline after checking the actual service evidence. "
                    "The same prepare, claim, and confirm sequence governs IDR initiation. A "
                    "crashed worker does not release its claimed token automatically, because "
                    "automatic reassignment could duplicate a submission that reached the portal "
                    "just before the crash. Reconcile the external case status, then perform "
                    "a separately audited recovery action if reassignment is necessary. The "
                    "reference intentionally provides no blind resend function. Store only opaque "
                    "evidence references in the ledger; authenticate users, authorize reviewer "
                    "roles, encrypt storage and transport, and capture application audit records "
                    "in the surrounding service. The executable core does not replace those "
                    "deployment controls. Its purpose is narrower and testable: prevent duplicate "
                    "local postings, conflicting transition acknowledgments, double allocation of "
                    "one remittance line, and simultaneous ownership of the same external-action task."
                ),
                (
                    "Reconciliation works at the provider-cohort level because unsuccessful files "
                    "still consume cash. Sum actual payer cash above each locked initial-payment "
                    "baseline, deduct administrative charges, entity deposits less received refunds, "
                    "and allocated casework costs, then apply the contracted contingency percentage "
                    "to the positive remainder. Until an entity refund actually arrives, the "
                    "deposit remains an economic deduction in this conservative cash model. "
                    "The fee statement stores a ledger sequence cutoff and cumulative earned "
                    "cents; later collections or reversals create a new statement adjustment "
                    "rather than rewriting history. A separate receipt table records operator "
                    "bank collections, allowing the reconciliation view to expose earned but "
                    "unpaid service fees. Initial provider cash, provider reserves, entity refunds, "
                    "and provider settlement proceeds are not operator revenue. The Base model "
                    "uses a 20% retained contingency share only as its illustrative contract "
                    "mechanic; the canonical $505,000 already represents operator service revenue, "
                    "so applying that percentage again would understate revenue fivefold. Evaluate "
                    "ASC 606 presentation against the actual service contract and principal-agent "
                    "facts. Keep any fee reversals visible, and investigate negative client-fee "
                    "balances instead of erasing them to make a dashboard look reconciled."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table — Six Copy-Pasteable Modules",
                "headers": [
                    "Reference module and execution order",
                    "Copy-pasteable Python source",
                    "Transaction boundary and operating interpretation",
                    "Verification evidence and deployment boundary",
                ],
                "rows": [
                    [
                        "Module 1 — Create the database and immutable accounting structures",
                        '''import json
import sqlite3
from contextlib import contextmanager
from datetime import date

db = sqlite3.connect(
    "idr_reference.sqlite3", timeout=30, isolation_level=None
)
db.row_factory = sqlite3.Row
db.execute("PRAGMA foreign_keys = ON")
db.execute("PRAGMA journal_mode = WAL")
db.execute("PRAGMA synchronous = FULL")
db.executescript("""
CREATE TABLE IF NOT EXISTS cohort (
    cohort_id TEXT PRIMARY KEY,
    provider_id TEXT NOT NULL,
    period TEXT NOT NULL,
    fee_bps INTEGER NOT NULL CHECK(fee_bps BETWEEN 0 AND 10000),
    UNIQUE(provider_id, period),
    UNIQUE(cohort_id, provider_id)
);
CREATE TABLE IF NOT EXISTS claim (
    case_id TEXT PRIMARY KEY,
    cohort_id TEXT NOT NULL,
    provider_id TEXT NOT NULL,
    claim_key TEXT NOT NULL,
    initial_cents INTEGER NOT NULL CHECK(initial_cents >= 0),
    intake_json TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'intake'
        CHECK(state IN (
            'intake', 'verified', 'open_pending',
            'negotiating', 'idr_pending', 'filed'
        )),
    version INTEGER NOT NULL DEFAULT 0,
    verification_json TEXT,
    open_last TEXT,
    negotiation_end TEXT,
    idr_last TEXT,
    reserve_cents INTEGER NOT NULL DEFAULT 0
        CHECK(reserve_cents >= 0),
    FOREIGN KEY(cohort_id, provider_id)
        REFERENCES cohort(cohort_id, provider_id),
    UNIQUE(provider_id, claim_key)
);
CREATE TABLE IF NOT EXISTS money_event (
    seq INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL UNIQUE,
    case_id TEXT NOT NULL REFERENCES claim(case_id),
    kind TEXT NOT NULL CHECK(kind IN (
        'payer_cash', 'admin_fee', 'entity_deposit',
        'entity_refund', 'casework'
    )),
    cents INTEGER NOT NULL,
    source_system TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    evidence_ref TEXT NOT NULL,
    UNIQUE(source_system, source_ref),
    CHECK(kind = 'payer_cash' OR cents >= 0)
);
CREATE TABLE IF NOT EXISTS outbox (
    token TEXT PRIMARY KEY,
    case_id TEXT NOT NULL REFERENCES claim(case_id),
    action TEXT NOT NULL CHECK(action IN ('open', 'idr')),
    state TEXT NOT NULL DEFAULT 'prepared'
        CHECK(state IN ('prepared', 'claimed', 'confirmed')),
    actor TEXT,
    receipt TEXT UNIQUE,
    confirmation_json TEXT,
    UNIQUE(case_id, action)
);
CREATE TABLE IF NOT EXISTS transition_log (
    seq INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id TEXT NOT NULL REFERENCES claim(case_id),
    version INTEGER NOT NULL,
    state TEXT NOT NULL,
    evidence_ref TEXT NOT NULL,
    UNIQUE(case_id, version)
);
CREATE TABLE IF NOT EXISTS fee_statement (
    token TEXT PRIMARY KEY,
    cohort_id TEXT NOT NULL REFERENCES cohort(cohort_id),
    cutoff INTEGER NOT NULL,
    earned_cents INTEGER NOT NULL,
    delta_cents INTEGER NOT NULL,
    UNIQUE(cohort_id, cutoff)
);
CREATE TABLE IF NOT EXISTS fee_cash (
    token TEXT PRIMARY KEY,
    cohort_id TEXT NOT NULL REFERENCES cohort(cohort_id),
    cents INTEGER NOT NULL,
    bank_ref TEXT NOT NULL UNIQUE
);
CREATE TRIGGER IF NOT EXISTS money_no_update
BEFORE UPDATE ON money_event
BEGIN SELECT RAISE(ABORT, 'append correction evidence instead'); END;
CREATE TRIGGER IF NOT EXISTS money_no_delete
BEFORE DELETE ON money_event
BEGIN SELECT RAISE(ABORT, 'preserve original accounting evidence'); END;
CREATE TRIGGER IF NOT EXISTS statement_no_update
BEFORE UPDATE ON fee_statement
BEGIN SELECT RAISE(ABORT, 'issue a later statement adjustment'); END;
CREATE TRIGGER IF NOT EXISTS statement_no_delete
BEFORE DELETE ON fee_statement
BEGIN SELECT RAISE(ABORT, 'preserve original fee statement'); END;
""")

@contextmanager
def tx():
    db.execute("BEGIN IMMEDIATE")
    try:
        yield
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))

def iso(value):
    return date.fromisoformat(value).isoformat()

def require(condition, message):
    if not condition:
        raise ValueError(message)
''',
                        "All mutable accounting operations below serialize before reading dependent records; schema initialization runs before serving application traffic.",
                        "Use one connection per process, supported local disk locking, restricted database access, and independently tested encrypted backups.",
                    ],
                    [
                        "Module 2 — Enroll authorized claims and score review priority",
                        '''def enroll(cohort_id, provider_id, period, case_id, claim_key,
           initial_cents, fee_bps, evidence_ref,
           potential_increment_cents, expected_cost_cents,
           review_minutes):
    require(type(initial_cents) is int and initial_cents >= 0,
            "initial payment must be nonnegative integer cents")
    require(type(fee_bps) is int and 0 <= fee_bps <= 10000,
            "fee basis points must be an integer percentage")
    require(review_minutes > 0, "positive review time required")
    require(bool(evidence_ref), "source evidence required")
    payload = canonical({
        "cohort": cohort_id, "provider": provider_id,
        "period": period, "case": case_id, "claim": claim_key,
        "initial": initial_cents, "fee_bps": fee_bps,
        "evidence": evidence_ref,
        "potential": potential_increment_cents,
        "expected_cost": expected_cost_cents,
        "minutes": review_minutes,
    })
    with tx():
        old = db.execute(
            "SELECT intake_json FROM claim WHERE case_id = ?",
            (case_id,)
        ).fetchone()
        if old:
            require(old["intake_json"] == payload,
                    "case identity reused with conflicting intake")
        else:
            cohort = db.execute(
                "SELECT * FROM cohort WHERE cohort_id = ?",
                (cohort_id,)
            ).fetchone()
            if cohort:
                require(
                    (cohort["provider_id"], cohort["period"],
                     cohort["fee_bps"]) ==
                    (provider_id, period, fee_bps),
                    "cohort contract mismatch"
                )
            else:
                db.execute(
                    "INSERT INTO cohort VALUES (?, ?, ?, ?)",
                    (cohort_id, provider_id, period, fee_bps)
                )
            db.execute("""
                INSERT INTO claim (
                    case_id, cohort_id, provider_id, claim_key,
                    initial_cents, intake_json
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (case_id, cohort_id, provider_id, claim_key,
                  initial_cents, payload))
            db.execute("""
                INSERT INTO money_event (
                    event_id, case_id, kind, cents,
                    source_system, source_ref, evidence_ref
                ) VALUES (?, ?, 'payer_cash', ?, 'baseline', ?, ?)
            """, ("baseline/" + case_id, case_id, initial_cents,
                  case_id, evidence_ref))
            db.execute("""
                INSERT INTO transition_log (
                    case_id, version, state, evidence_ref
                ) VALUES (?, 0, 'intake', ?)
            """, (case_id, evidence_ref))
    return max(
        0, potential_increment_cents - expected_cost_cents
    ) // review_minutes
''',
                        "Enrollment and baseline posting commit together; the score ranks review effort without asserting legal eligibility or expected cash collection.",
                        "Replaying identical enrollment returns the same score; conflicting identity reuse or cross-cohort duplicate claims fail under unique constraints.",
                    ],
                    [
                        "Module 3 — Verify evidence, reserve funds, and claim external preparation work",
                        '''def verify(case_id, checks, open_last, reserve_cents):
    needed = {
        "authority", "baa", "federal_eligible",
        "receipt_verified", "calendar_verified",
        "batching_checked", "cooling_checked"
    }
    require(all(checks.get(key) is True for key in needed),
            "every reviewed eligibility check must pass")
    require(bool(checks.get("evidence_ref")),
            "verification evidence reference required")
    require(type(reserve_cents) is int and reserve_cents >= 0,
            "verified provider reserve must use integer cents")
    last = iso(open_last)
    payload = canonical({
        "checks": checks, "open_last": last,
        "reserve_cents": reserve_cents
    })
    with tx():
        row = db.execute(
            "SELECT * FROM claim WHERE case_id = ?", (case_id,)
        ).fetchone()
        require(row is not None, "case must exist")
        if row["verification_json"] is not None:
            require(row["verification_json"] == payload,
                    "verification replay conflicts with original")
            return
        require(row["state"] == "intake", "case already advanced")
        db.execute("""
            UPDATE claim SET state = 'verified',
                version = version + 1, verification_json = ?,
                open_last = ?, reserve_cents = ?
            WHERE case_id = ?
        """, (payload, last, reserve_cents, case_id))
        db.execute("""
            INSERT INTO transition_log (
                case_id, version, state, evidence_ref
            ) VALUES (?, ?, 'verified', ?)
        """, (case_id, row["version"] + 1, checks["evidence_ref"]))

def queue_action(case_id, action, required_reserve_cents=0):
    require(action in ("open", "idr"), "supported action required")
    require(type(required_reserve_cents) is int
            and required_reserve_cents >= 0,
            "required reserve must use nonnegative integer cents")
    token = action + "/" + case_id
    today = date.today().isoformat()
    with tx():
        old = db.execute(
            "SELECT token FROM outbox WHERE case_id = ? AND action = ?",
            (case_id, action)
        ).fetchone()
        if old:
            return old["token"]
        row = db.execute(
            "SELECT * FROM claim WHERE case_id = ?", (case_id,)
        ).fetchone()
        require(row is not None, "case must exist")
        if action == "open":
            require(row["state"] == "verified",
                    "open negotiation requires verified intake")
            require(today <= row["open_last"],
                    "open negotiation initiation window expired")
        else:
            require(row["state"] == "negotiating",
                    "IDR requires confirmed open negotiation")
            require(row["negotiation_end"] < today <= row["idr_last"],
                    "outside reviewed IDR initiation window")
            require(required_reserve_cents > 0,
                    "current filing reserve amount required")
            require(row["reserve_cents"] >= required_reserve_cents,
                    "provider reserve is insufficient")
        pending = "open_pending" if action == "open" else "idr_pending"
        db.execute("""
            INSERT INTO outbox (token, case_id, action)
            VALUES (?, ?, ?)
        """, (token, case_id, action))
        db.execute("""
            UPDATE claim SET state = ?, version = version + 1
            WHERE case_id = ?
        """, (pending, case_id))
        db.execute("""
            INSERT INTO transition_log (
                case_id, version, state, evidence_ref
            ) VALUES (?, ?, ?, ?)
        """, (case_id, row["version"] + 1, pending, token))
    return token

def claim_action(token, actor):
    require(bool(actor), "authenticated actor identifier required")
    with tx():
        row = db.execute(
            "SELECT * FROM outbox WHERE token = ?", (token,)
        ).fetchone()
        require(row is not None, "preparation token must exist")
        if row["state"] != "prepared":
            return False
        db.execute("""
            UPDATE outbox SET state = 'claimed', actor = ?
            WHERE token = ?
        """, (actor, token))
        return True
''',
                        "Provider-controlled reserves are verification facts rather than operator escrow balances; claimed work never automatically returns to the preparation queue.",
                        "One serialized claimant receives permission to act; repeated claims return false even for the same actor, preventing automatic duplicate delivery.",
                    ],
                    [
                        "Module 4 — Confirm delivery and post source-identified cash events",
                        '''def confirm_action(token, actor, receipt, delivered_on,
                   negotiation_end=None, idr_last=None):
    delivered = iso(delivered_on)
    require(bool(receipt), "external receipt identity required")
    payload = canonical({
        "actor": actor, "receipt": receipt,
        "delivered": delivered,
        "negotiation_end": negotiation_end, "idr_last": idr_last
    })
    with tx():
        task = db.execute(
            "SELECT * FROM outbox WHERE token = ?", (token,)
        ).fetchone()
        require(task is not None, "preparation token must exist")
        if task["state"] == "confirmed":
            require(task["confirmation_json"] == payload,
                    "confirmation replay conflicts with original")
            return
        require(task["state"] == "claimed" and task["actor"] == actor,
                "only the assigned actor may confirm delivery")
        row = db.execute(
            "SELECT * FROM claim WHERE case_id = ?",
            (task["case_id"],)
        ).fetchone()
        require(delivered <= date.today().isoformat(),
                "delivery cannot be recorded in the future")
        if task["action"] == "open":
            end = iso(negotiation_end)
            last = iso(idr_last)
            require(row["state"] == "open_pending",
                    "case is not awaiting open negotiation")
            require(delivered <= row["open_last"],
                    "delivered outside reviewed initiation window")
            require(delivered <= end < last,
                    "reviewed deadline ordering is inconsistent")
            target = "negotiating"
        else:
            require(row["state"] == "idr_pending",
                    "case is not awaiting IDR initiation")
            require(row["negotiation_end"] < delivered <= row["idr_last"],
                    "delivered outside reviewed IDR window")
            end, last, target = (
                row["negotiation_end"], row["idr_last"], "filed"
            )
        db.execute("""
            UPDATE outbox SET state = 'confirmed', receipt = ?,
                confirmation_json = ? WHERE token = ?
        """, (receipt, payload, token))
        db.execute("""
            UPDATE claim SET state = ?, version = version + 1,
                negotiation_end = ?, idr_last = ?
            WHERE case_id = ?
        """, (target, end, last, row["case_id"]))
        db.execute("""
            INSERT INTO transition_log (
                case_id, version, state, evidence_ref
            ) VALUES (?, ?, ?, ?)
        """, (row["case_id"], row["version"] + 1, target, receipt))

def post_money(event_id, case_id, kind, cents,
               source_system, source_ref, evidence_ref):
    allowed = {
        "payer_cash", "admin_fee", "entity_deposit",
        "entity_refund", "casework"
    }
    require(kind in allowed and type(cents) is int,
            "supported event and integer cents required")
    require(kind == "payer_cash" or cents >= 0,
            "cost and refund entries must be nonnegative")
    require(source_system != "baseline", "baseline namespace reserved")
    require(bool(source_ref) and bool(evidence_ref),
            "allocation identity and evidence required")
    values = (
        event_id, case_id, kind, cents,
        source_system, source_ref, evidence_ref
    )
    with tx():
        old = db.execute("""
            SELECT event_id, case_id, kind, cents,
                source_system, source_ref, evidence_ref
            FROM money_event WHERE event_id = ?
        """, (event_id,)).fetchone()
        if old:
            require(tuple(old) == values,
                    "money event replay conflicts with original")
            return
        if kind == "entity_refund":
            balance = db.execute("""
                SELECT COALESCE(SUM(
                    CASE kind
                        WHEN 'entity_deposit' THEN cents
                        WHEN 'entity_refund' THEN -cents
                        ELSE 0 END
                ), 0) FROM money_event WHERE case_id = ?
            """, (case_id,)).fetchone()[0]
            require(cents <= balance,
                    "entity refund exceeds recorded deposits")
        db.execute("""
            INSERT INTO money_event (
                event_id, case_id, kind, cents,
                source_system, source_ref, evidence_ref
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, values)

def post_fee_receipt(token, cohort_id, cents, bank_ref):
    require(type(cents) is int and cents != 0,
            "signed nonzero integer receipt cents required")
    require(bool(bank_ref), "unique operator bank evidence required")
    values = (token, cohort_id, cents, bank_ref)
    with tx():
        old = db.execute(
            "SELECT * FROM fee_cash WHERE token = ?", (token,)
        ).fetchone()
        if old:
            require(tuple(old) == values,
                    "fee receipt replay conflicts with original")
            return
        db.execute(
            "INSERT INTO fee_cash VALUES (?, ?, ?, ?)", values
        )
''',
                        "A bank source reference must identify an approved deposit-line allocation; signed payer adjustments preserve recoupments without rewriting initial cash.",
                        "External fee corrections require reviewed compensating accounting outside this narrow event vocabulary; no fabricated refund category is supplied.",
                    ],
                    [
                        "Module 5 — Reconcile cohort fee bases and freeze auditable statements",
                        '''db.executescript("""
CREATE VIEW IF NOT EXISTS case_cash AS
SELECT c.case_id, c.cohort_id,
    MAX(0, COALESCE(SUM(
        CASE WHEN e.kind = 'payer_cash' THEN e.cents ELSE 0 END
    ), 0) - c.initial_cents) AS incremental_cents,
    COALESCE(SUM(
        CASE e.kind
            WHEN 'admin_fee' THEN e.cents
            WHEN 'entity_deposit' THEN e.cents
            WHEN 'entity_refund' THEN -e.cents
            WHEN 'casework' THEN e.cents
            ELSE 0 END
    ), 0) AS deduction_cents
FROM claim c
LEFT JOIN money_event e ON e.case_id = c.case_id
GROUP BY c.case_id, c.cohort_id, c.initial_cents;

CREATE VIEW IF NOT EXISTS cohort_basis AS
SELECT h.cohort_id, h.fee_bps,
    COALESCE(SUM(c.incremental_cents), 0) AS incremental_cents,
    COALESCE(SUM(c.deduction_cents), 0) AS deduction_cents,
    MAX(0, COALESCE(SUM(
        c.incremental_cents - c.deduction_cents
    ), 0)) AS eligible_cents
FROM cohort h
LEFT JOIN case_cash c ON c.cohort_id = h.cohort_id
GROUP BY h.cohort_id, h.fee_bps;

CREATE VIEW IF NOT EXISTS cohort_reconciliation AS
SELECT b.*,
    CAST((b.eligible_cents * b.fee_bps + 5000) / 10000
         AS INTEGER) AS earned_fee_cents,
    COALESCE((
        SELECT SUM(f.cents) FROM fee_cash f
        WHERE f.cohort_id = b.cohort_id
    ), 0) AS received_fee_cents,
    CAST((b.eligible_cents * b.fee_bps + 5000) / 10000
         AS INTEGER) -
    COALESCE((
        SELECT SUM(f.cents) FROM fee_cash f
        WHERE f.cohort_id = b.cohort_id
    ), 0) AS fee_receivable_cents
FROM cohort_basis b;
""")

def freeze_statement(token, cohort_id):
    with tx():
        old = db.execute(
            "SELECT * FROM fee_statement WHERE token = ?", (token,)
        ).fetchone()
        if old:
            require(old["cohort_id"] == cohort_id,
                    "statement token reused for another cohort")
            return dict(old)
        cutoff = db.execute("""
            SELECT COALESCE(MAX(e.seq), 0)
            FROM money_event e
            JOIN claim c ON c.case_id = e.case_id
            WHERE c.cohort_id = ?
        """, (cohort_id,)).fetchone()[0]
        same = db.execute("""
            SELECT * FROM fee_statement
            WHERE cohort_id = ? AND cutoff = ?
        """, (cohort_id, cutoff)).fetchone()
        if same:
            return dict(same)
        row = db.execute("""
            SELECT earned_fee_cents FROM cohort_reconciliation
            WHERE cohort_id = ?
        """, (cohort_id,)).fetchone()
        require(row is not None, "cohort must exist")
        previous = db.execute("""
            SELECT earned_cents FROM fee_statement
            WHERE cohort_id = ? ORDER BY cutoff DESC LIMIT 1
        """, (cohort_id,)).fetchone()
        prior = previous["earned_cents"] if previous else 0
        earned = row["earned_fee_cents"]
        db.execute(
            "INSERT INTO fee_statement VALUES (?, ?, ?, ?, ?)",
            (token, cohort_id, cutoff, earned, earned - prior)
        )
        return dict(db.execute(
            "SELECT * FROM fee_statement WHERE token = ?", (token,)
        ).fetchone())
''',
                        "Cohort aggregation includes costs from lost and dismissed cases; integer rounding occurs once per cumulative provider-cohort entitlement calculation.",
                        "Fee statements freeze earned contribution, while separate bank receipts expose collection delays and negative balances requiring documented settlement adjustments.",
                    ],
                    [
                        "Module 6 — Run structural, accounting, replay, and ownership checks",
                        '''def qa_checks():
    require(db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
            "SQLite structural integrity check failed")
    require(not db.execute("PRAGMA foreign_key_check").fetchall(),
            "foreign key inconsistency detected")
    require(not db.execute("""
        SELECT c.case_id
        FROM claim c LEFT JOIN money_event e
          ON e.case_id = c.case_id AND e.source_system = 'baseline'
        GROUP BY c.case_id, c.initial_cents
        HAVING COUNT(e.seq) != 1
            OR COALESCE(SUM(e.cents), 0) != c.initial_cents
    """).fetchall(), "initial cash baseline does not reconcile")
    require(not db.execute("""
        SELECT case_id FROM money_event
        GROUP BY case_id
        HAVING SUM(CASE kind
            WHEN 'entity_deposit' THEN cents
            WHEN 'entity_refund' THEN -cents ELSE 0 END) < 0
    """).fetchall(), "entity refunds exceed recorded deposits")
    require(not db.execute("""
        SELECT token FROM outbox
        WHERE state = 'confirmed'
          AND (receipt IS NULL OR confirmation_json IS NULL)
    """).fetchall(), "confirmed delivery lacks receipt evidence")
    require(not db.execute("""
        SELECT c.case_id FROM claim c
        LEFT JOIN transition_log t
          ON t.case_id = c.case_id AND t.version = c.version
        WHERE t.seq IS NULL OR t.state != c.state
    """).fetchall(), "case state does not match transition evidence")
    warnings = db.execute("""
        SELECT cohort_id, fee_receivable_cents
        FROM cohort_reconciliation
        WHERE fee_receivable_cents != 0
    """).fetchall()
    return {
        "structural_checks": "passed",
        "fee_collection_exceptions": [dict(row) for row in warnings],
    }

def assert_duplicate_claim_fails(token, actor):
    first = claim_action(token, actor)
    second = claim_action(token, actor)
    require(first is True and second is False,
            "preparation token did not enforce one-time ownership")
''',
                        "Run QA after each import and before statements; execute the ownership test only against a disposable prepared token in a test database.",
                        "Add separate-process contention, crash recovery, holiday-calendar, duplicate-remittance, and backup-restore tests before deploying; this chapter reports no executed test results.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Run negotiation, evidence, awards, and cash recovery as separate queues",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Assign negotiation and arbitration preparation to different work queues, even "
                    "when one full-time operator owns both. Negotiation should articulate the "
                    "specific payment disagreement, identify the relevant service lines, and "
                    "preserve any binding settlement terms with payment instructions. For IDR, "
                    "prepare the required offer and permitted supporting evidence under the "
                    "current governing standards and submission schedule. Baseball arbitration "
                    "selects an offer; it does not automatically award the operator's spreadsheet "
                    "target. The QPA is a required consideration, but the brief must also "
                    "address other applicable permissible information without presenting prohibited "
                    "material. Use specialty training, patient acuity, complexity, facility teaching "
                    "status where relevant, and documented good-faith contracting efforts only "
                    "as supported and applicable. FAIR Health subscriptions can support internal "
                    "research, but usual-and-customary charge evidence does not become permissible "
                    "merely because it came from a named vendor. Do not base the determination "
                    "request on prohibited billed charges, usual-and-customary charges, or public "
                    "payer reimbursement rates. Have a qualified reviewer verify the evidence "
                    "against current regulations and controlling decisions, especially where "
                    "rule text and implementation guidance have changed. Preserve both submitted "
                    "offers, the final determination, and the exact service-line scope."
                ),
                (
                    "Treat a favorable determination as an account to collect, not cash in "
                    "the owner-profit column. Record the award amount, initial payment offset, "
                    "applicable payment deadline, entity-fee refund status, and payer remittance "
                    "instructions in a separate award register. The federal framework generally "
                    "requires the resulting payment within 30 calendar days after the determination; "
                    "review the case-specific obligation and any valid adjustment before escalation. "
                    "Match each later 835 line to bank evidence and allocate partial payments "
                    "without repeating the initial allowance deduction. If an award establishes "
                    "a $5,000 total payment and $1,000 already arrived, a later $4,000 deposit "
                    "is the increment, not another $5,000 recovery. A $2,000 partial deposit "
                    "supports only $2,000 of incremental cash at that point. Track payer "
                    "recoupments as signed events and recalculate the cumulative fee entitlement. "
                    "Escalate overdue payment through the applicable documented payer and agency "
                    "channels; do not rebill protected patients to replace the missing award "
                    "cash. Provider-funded deposits stay outside operator working capital, and "
                    "entity refunds must be matched to actual receipts. The owner dashboard "
                    "should show filed cases, favorable determinations, paid determinations, "
                    "incremental cash, earned fees, and collected operator fees as distinct measures."
                ),
                (
                    "The twelfth mapped play, wotc_hourly_payroll_tax_credit_contingency_engine, is "
                    "a process analogue and a separate service line, not another medical recovery "
                    "fee. For employer-authorized WOTC work, verify statutory authorization for "
                    "the relevant hiring period, qualifying group evidence, certification procedure, "
                    "and submission timing before promising a credit workflow. Form 8850 generally "
                    "must reach the designated state workforce agency within 28 days after work "
                    "begins, subject to applicable relief. An illustrative eligible worker with "
                    "400 qualifying hours and $6,000 of qualifying first-year wages could support "
                    "a $2,400 credit under the general 40% calculation; 25 such workers imply "
                    "$60,000 of employer credits, not operator revenue. A hypothetical permitted "
                    "10% outcome-linked fee would produce $6,000 only under a valid engagement "
                    "and professional-fee analysis. Separately substantiate Section 41 qualified "
                    "research expenses, business components, experimentation, wage allocation, and "
                    "Section 280C coordination; never recycle WOTC screening into an R&D claim. "
                    "Review applicable contingent-fee restrictions, including 31 CFR § 10.27 "
                    "where relevant, with the responsible tax professional. Exclude unsupported "
                    "claims and use fixed-fee payroll or research-documentation services under "
                    "independent tax review when outcome-linked pricing is unavailable. None of "
                    "these employer credits or fees enters the medical Base-case ledger."
                ),
            ],
            "table": {
                "caption": "Mapped Plays 8–12 and Two Cash-Protection Exceptions",
                "headers": [
                    "Operating play or exception",
                    "Production action and required artifact",
                    "Concrete unit calculation or exposure",
                    "Risk fallback and ownership assignment",
                ],
                "rows": [
                    [
                        "Play 8 — Evidence-supported final-offer preparation and arbitration submission",
                        "Clinical reviewer links each permitted assertion to the retained source record",
                        "A $5,000 total offer includes the already received $1,000 baseline",
                        "Remove prohibited price evidence and obtain qualified review before submission",
                    ],
                    [
                        "Play 9 — Determination tracking and overdue payer collection",
                        "Collections owner records determination delivery, payment obligation, and remittance correspondence",
                        "Sixty paid results out of sixty-five favorable results produce cash",
                        "Leave five unpaid favorable results outside current contingency revenue recognition",
                    ],
                    [
                        "Play 10 — Entity-fee refund matching and failed-file cost allocation",
                        "Settlement reviewer matches each deposit, refund, loss, and dismissal expense",
                        "Eighty $800 deposits less sixty-five refunds leave $12,000 unrecovered",
                        "Investigate retained dismissal fees against the actual entity cancellation schedule",
                    ],
                    [
                        "Play 11 — Incremental-cash settlement and operator-fee reconciliation",
                        "Controller issues a provider-cohort statement and matches operator bank receipts",
                        "$240,000 less $20,000 and $9,583.35 yields a $42,083.33 fee",
                        "Hold disputed allocations and issue later adjustments rather than editing history",
                    ],
                    [
                        "Play 12 — wotc_hourly_payroll_tax_credit_contingency_engine as a separately bounded analogue",
                        "Employer authority, timely certification materials, and independently substantiated research documentation",
                        "Twenty-five $2,400 employer credits produce $60,000 of credit value",
                        "Use permitted fixed-fee documentation services when contingent pricing is restricted",
                    ],
                    [
                        "Exception — Partial payment followed by a payer recoupment",
                        "Retain original bank match and append the signed recoupment evidence",
                        "$4,000 received less a $1,000 recoupment leaves $3,000 incremental cash",
                        "Recalculate cumulative entitlement and document any resulting provider fee credit",
                    ],
                    [
                        "Exception — Award success without timely operator-fee collection",
                        "Track provider settlement and operator invoice collection in separate registers",
                        "A $42,083.33 earned fee with $30,000 received leaves $12,083.33 outstanding",
                        "Escalate contract collection without counting the unpaid balance as owner cash",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four tactics that prevent attractive awards from becoming bad economics",
                "body": (
                    "The best operating improvements remove false positives, preserve clocks, "
                    "and accelerate evidence-backed cash matching."
                ),
                "items": [
                    "Capture initial-payment receipt evidence during intake; reconstructing it during the four-business-day initiation window creates avoidable deadline risk.",
                    "Track entity-fee refund receipt separately from the determination date, because a favorable decision does not prove the deposit returned.",
                    "Assign a stable source allocation identity to every 835 line and bank match; changing import filenames must never create another recovery.",
                    "Maintain separate favorable-result and paid-result denominators, then rank payer follow-up by collectible increment and days past the applicable payment obligation.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Qualify and lock the source record",
                    "action": "Verify authority, federal eligibility, initial cash, and duplicate identity.",
                    "detail": "Reject or reroute unsupported claims before deposits; preserve evidence references and the reviewed deadline calendar.",
                },
                {
                    "step": 2,
                    "title": "Serve negotiation and initiate eligible disputes",
                    "action": "Prepare, claim, deliver, and confirm each external action using its unique token.",
                    "detail": "Preserve recipient proof and portal acknowledgment; never retry an uncertain external submission without status reconciliation.",
                },
                {
                    "step": 3,
                    "title": "Submit permitted evidence and collect the determination",
                    "action": "Review the offer, supporting record, entity correspondence, and resulting payment obligation.",
                    "detail": "Track fee exposure and favorable-but-unpaid outcomes separately from received incremental cash.",
                },
                {
                    "step": 4,
                    "title": "Reconcile deposits, deductions, and operator receipts",
                    "action": "Match bank evidence, post immutable events, freeze the statement, and verify service-fee collection.",
                    "detail": "Include unsuccessful-file costs and actual refund timing; publish unresolved exceptions instead of silently forcing the balance.",
                },
            ],
        },
        {
            "heading": "4. Walk a mature 90-day book without pretending a startup collects immediately",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a mature-book illustration, not a claim "
                    "that every new IDR file converts within ninety days. Each month brings "
                    "100 authorized leads; twenty scrub out before federal filing, leaving "
                    "eighty eligible files. For the mature cohorts collected during this window, "
                    "sixty-five files receive favorable determinations, ten lose, and five "
                    "dismissals retain the assumed paid entity fees. Sixty favorable files "
                    "actually pay a $4,000 increment during the modeled collection period, "
                    "producing $240,000 of incremental provider cash. Five favorable files "
                    "remain unpaid, representing $20,000 of prospective increments excluded "
                    "from this period's revenue. Later receipts enter a later ledger cutoff "
                    "and cannot be counted twice. Fees are explicit modeling assumptions, "
                    "not representations of current CMS or entity schedules: eighty $100 "
                    "administrative charges equal $8,000; eighty $800 entity deposits equal "
                    "$64,000; sixty-five received $800 refunds equal $52,000. Unrecovered "
                    "fees therefore equal $20,000. Verify actual administrative charges, "
                    "entity schedules, refund eligibility, and dismissal terms before funding "
                    "a real cohort. The five dismissed cases illustrate fee-retention exposure, "
                    "rather than asserting that every dismissal has an identical refund outcome."
                ),
                (
                    "Allocate $9,583.35 of provider-borne casework to each of the first two "
                    "settling cohorts and $9,583.30 to the third. Across the quarter, "
                    "$720,000 of incremental cash minus $60,000 of unrecovered fees and "
                    "$28,750 of casework leaves $631,250 of fee-eligible contribution. A "
                    "20% contingency produces exactly $126,250 of operator service revenue, "
                    "with monthly fees of $42,083.33, $42,083.33, and $42,083.34. The "
                    "provider separately bears the identified cohort expenses; they are not "
                    "charged again inside operator overhead. Operator overhead is $23,987.50 "
                    "monthly, or $71,962.50 quarterly, including modeled owner-team labor, "
                    "contractor capacity, infrastructure, insurance, and business administration. "
                    "For operating planning, that monthly total can be decomposed into "
                    "$16,000 of labor and contractor expense plus $7,987.50 of other "
                    "overhead. The latter fits the stated $1,800–$10,500 operating-overhead "
                    "range; that range cannot substitute for the scorecard's all-in expense "
                    "total. Quarterly owner profit is $54,287.50. Repeating this mature "
                    "quarter four times yields $505,000 revenue, $287,850 expenses, and "
                    "$217,150 profit, exactly 43.0%. Those are operator figures; provider "
                    "settlement value and initial collections remain outside recognized revenue."
                ),
                (
                    "Month 1 collections come from pre-window cohort P1, Month 2 from "
                    "P2, and Month 3 from P3; each entered early enough to complete "
                    "its actual negotiation, determination, and collection sequence. New "
                    "cohorts A, B, and C are tracked independently and contribute no "
                    "assumed cash within this walk. Their eventual timing depends on "
                    "negotiated settlements, proceedings, refunds, and payer behavior, not "
                    "a fixed ninety-day promise. Provider-controlled reserves fund their "
                    "case expenses, so those reserves do not improve operator cumulative "
                    "cash. Assuming the mature cohorts' operator invoices are paid in "
                    "the same month, cumulative operating cash reaches $18,095.83, "
                    "$36,191.66, and $54,287.50 after monthly overhead. A cold start "
                    "with identical staffing but no pre-window cohorts instead consumes "
                    "$71,962.50 before setup costs if no operator fees arrive during "
                    "the quarter. That exceeds the stated $10,000–$45,000 startup "
                    "capital range and requires staged staffing, earlier documented "
                    "negotiated collections, or additional runway. Time to first deal "
                    "of one to four months is not time to unrestricted owner "
                    "cash. Stress-test slower refunds, fewer paid favorable outcomes, "
                    "and provider invoice delays before adding the second full-time "
                    "seat; capacity expansion should follow reconciled throughput rather "
                    "than the volume of favorable decision notices."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and cohort identity",
                    "Lead progression, scrubs, losses, and cash timing",
                    "Operator revenue and operating expense",
                    "Cumulative operator cash and reconciliation evidence",
                ],
                "rows": [
                    [
                        "Month 1 — Newly acquired provider cohort A",
                        "One hundred leads; twenty pre-filing scrubs; eighty eligible files begin their reviewed process",
                        "Zero operator revenue assumed from A; provider reserves fund its separate case expenses",
                        "No A receipts enter cumulative cash; preserve lead-to-case and reserve evidence",
                    ],
                    [
                        "Month 1 — Mature pre-window collection cohort P1",
                        "Eighty filed; sixty-five favorable; sixty paid; ten losses; five fee-retaining dismissals",
                        "$240,000 incremental cash yields $42,083.33 revenue; operator overhead totals $23,987.50",
                        "$18,095.83 cumulative operating cash after bank-matched fee receipt and monthly overhead",
                    ],
                    [
                        "Month 2 — Newly acquired provider cohort B",
                        "One hundred leads; twenty pre-filing scrubs; eighty eligible files receive separate deadline ownership",
                        "Zero operator revenue assumed from B; earlier cohort A remains separately tracked",
                        "New-file counts create no cash uplift; preserve independent cohort collection ledgers",
                    ],
                    [
                        "Month 2 — Mature pre-window collection cohort P2",
                        "Sixty paid favorable files produce $240,000; five favorable files remain unpaid",
                        "$42,083.33 operator revenue less $23,987.50 overhead produces $18,095.83 operating cash",
                        "$36,191.66 cumulative operating cash after the second matched collection and expense cycle",
                    ],
                    [
                        "Month 3 — Newly acquired provider cohort C",
                        "One hundred leads; twenty pre-filing scrubs; eighty eligible files enter the continuing pipeline",
                        "Zero operator revenue assumed from C; A and B receive no invented receipts",
                        "Future collection potential stays outside current revenue and cumulative operator cash",
                    ],
                    [
                        "Month 3 — Mature pre-window collection cohort P3",
                        "$240,000 incremental receipts less $20,000 fees and $9,583.30 casework establish the basis",
                        "$42,083.34 operator revenue less $23,987.50 overhead produces $18,095.84 operating cash",
                        "$54,287.50 cumulative operating cash; quarterly cents reconcile without hidden rounding adjustments",
                    ],
                    [
                        "Quarter total — Mature-book collections and fresh pipeline kept separate",
                        "Three hundred new leads coexist with 180 paid favorable results from earlier cohorts",
                        "$126,250 operator revenue less $71,962.50 overhead equals $54,287.50 owner profit",
                        "Four identical mature quarters reconcile to $505,000 revenue and $217,150 annual profit",
                    ],
                    [
                        "Cold-start comparison — No mature cohorts available for collection",
                        "A, B, and C still require work while assumed operator collections remain zero",
                        "Three months of unchanged staffing consume $71,962.50 before separate setup expenditures",
                        "A $45,000 opening balance would leave a $26,962.50 funding shortfall before setup",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "An award is an instruction to collect; only reconciled incremental cash can fund the contingency.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Execute provider authority and the BAA, then establish a provider-scoped claim identity and immutable initial-payment evidence before importing recovery candidates.",
        "Assign a reviewer to federal-versus-state eligibility, current batching conditions, party-specific cooling-off restrictions, and every business-day deadline calculation.",
        "Implement and test the six reference modules in an isolated environment, including separate-process contention, duplicate events, crash recovery, and restored-backup reconciliation.",
        "Confirm current administrative and entity charges, document provider-controlled reserves, and price fees only on incremental cash after the contracted deductions.",
        "Separate favorable determinations, paid determinations, earned operator fees, and collected operator fees in the daily operating report.",
        "Reconcile the mature quarter to $126,250 revenue and $54,287.50 owner profit, then fund the separate cold-start runway before committing to Base-case staffing.",
    ],
    "statutory_citations": [
        {
            "title": "42 U.S.C. § 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes the federal payment-dispute framework, negotiation and IDR mechanics, "
                "determination considerations, payment timing, and related restrictions."
            ),
        },
        {
            "title": "45 CFR § 149.510 — Federal independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.510",
            "relevance": (
                "Provides operational requirements for negotiation, initiation, entity selection, "
                "batching, determinations, fees, and subsequent disputes; apply the currently "
                "operative provisions and controlling decisions to each filing."
            ),
        },
        {
            "title": "45 CFR § 164.502 — Uses and disclosures of protected health information",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.502",
            "relevance": (
                "Supports permitted-use analysis, business-associate handling, and applicable "
                "minimum-necessary controls for intake and evidence preparation."
            ),
        },
        {
            "title": "45 CFR § 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Defines contractual requirements governing business-associate handling of "
                "provider records and downstream service arrangements."
            ),
        },
        {
            "title": "26 U.S.C. § 51 — Work opportunity credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/51",
            "relevance": (
                "Governs qualifying groups, wages, hours, certification timing, and hiring-period "
                "authorization for the separately bounded employer-credit operating analogue."
            ),
        },
        {
            "title": "26 U.S.C. § 41 — Credit for increasing research activities",
            "url": "https://www.law.cornell.edu/uscode/text/26/41",
            "relevance": (
                "Requires separate substantiation of qualified research and associated expenses "
                "rather than treating payroll screening as research-credit evidence."
            ),
        },
        {
            "title": "26 U.S.C. § 280C — Disallowance of deduction for certain expenses",
            "url": "https://www.law.cornell.edu/uscode/text/26/280C",
            "relevance": (
                "Coordinates deductions and credits in the separate tax-service analogue, "
                "including applicable wage and research-expense adjustments."
            ),
        },
        {
            "title": "31 CFR § 10.27 — Fees",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-A/part-10/subpart-B/section-10.27",
            "relevance": (
                "Requires professional review of applicable fee restrictions before offering "
                "outcome-linked pricing for tax-related services."
            ),
        },
    ],
}
