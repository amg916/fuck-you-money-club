from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "probate-real-estate-complete-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute probate real estate end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Executor Authority, California Probate Code Sale Paths, SQLite Event Controls, Escrow Evidence & Retained-Commission Cash",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #9, Probate Real Estate, ranks #26 with a 80/100 Money-to-Manpower "
        "Score. Its 11 mapped plays connect docket sourcing, executor verification, "
        "brokerage production, acquisitions screening, attorney relationships, and "
        "property-tax appeals without mixing estate proceeds with operator revenue. "
        "This chapter specifies the evidence required at every handoff, a six-module "
        "SQLite reference implementation, and a worked mature-pipeline cohort that "
        "collects $127,500 over 90 days. Five monthly closings retaining $8,500 each "
        "support the $510,000 Base annual revenue case. Annual owner net profit remains "
        "$24,000 Conservative, $140,250 Base, and $315,000 Scaled. The operating rule is "
        "simple: court authority controls the sale, escrow evidence controls completion, "
        "and independently matched bank credits control cash reporting."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "20% margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$510,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "27.5% margin; $140,250 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "35% margin; $315,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Turn eleven mapped plays into one authority-first production queue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a parcel-level case record, not a spreadsheet of deceased owners. "
                    "A county docket alert creates a research task containing jurisdiction, docket "
                    "number, assessor parcel identifier, filing date, and source reference. The "
                    "unique production identity is county plus docket plus parcel; multiple heirs "
                    "and multiple alert vendors must not create multiple prospects. Use county "
                    "court portals and assessor records as authoritative sources, with ATTOM or "
                    "Regrid supplying enrichment rather than appointment evidence. An executor "
                    "named in a will is not automatically an appointed personal representative. "
                    "Obtain current letters, the appointment order, applicable sale powers, and "
                    "the representative's verified contact channel before discussing a listing "
                    "agreement. Record estate counsel separately from the client: counsel may "
                    "coordinate instructions without becoming the brokerage's principal. The "
                    "chapter's eleven mapped plays are the operating workstreams listed below, "
                    "not eleven additive revenue forecasts. Each receives an owner, an evidence "
                    "requirement, and a stop condition. A household with three properties can "
                    "produce three parcel files, but one disputed appointment pauses all affected "
                    "files. This identity discipline protects both outreach quality and later "
                    "commission reconciliation, where a familiar surname is an unsafe matching key."
                ),
                (
                    "Choose the legal sale path before buying photography, arranging a cleanout, "
                    "or promising a closing date. In California, Probate Code section 10501 "
                    "distinguishes transactions requiring court supervision and limits the powers "
                    "available under limited independent administration. Sections 10580 through "
                    "10592 govern notice of proposed action where applicable; a valid objection "
                    "can change the execution path. Court-supervised sales also carry confirmation "
                    "and potential overbid mechanics under the applicable confirmation provisions. "
                    "Estate counsel should identify which requirements apply to this appointment "
                    "and this asset, then provide a written transaction-specific instruction. "
                    "The broker owns pricing, marketing, negotiations, and brokerage disclosures; "
                    "counsel owns legal interpretation; escrow owns its settlement instructions. "
                    "Do not collapse those responsibilities into a generic green checkbox. Before "
                    "entry, confirm occupancy, authorized access, insurance, and whether a tenant "
                    "or another person has possessory rights. A field contractor receives a "
                    "bounded work order, never authority to remove occupants or discard disputed "
                    "property. When family instructions conflict, preserve the competing messages, "
                    "stop discretionary work, and obtain direction from the authorized representative "
                    "and counsel. A delayed listing is cheaper than funding an irreversible "
                    "cleanout on the instruction of the wrong relative."
                ),
                (
                    "Run the Base team as two full-time people and three contracted functions: "
                    "an owner-operator, a licensed production professional, and contracted "
                    "transaction coordination, field services, and bookkeeping. Assign each "
                    "function a measurable queue rather than counting every vendor as another "
                    "employee. The operator reviews thirty fresh leads monthly in the illustrative "
                    "cohort, while the production professional manages the active listing and "
                    "escrow inventory. Contractors receive only the fields needed for their "
                    "assigned work. Attorney relationships should earn introductions through "
                    "reliable status reports, accurate authority packets, and clean settlement "
                    "documentation, not payments tied to covered settlement-service referrals. "
                    "RESPA section 8, codified at 12 U.S.C. section 2607, matters when the "
                    "transaction falls within its coverage; state professional and brokerage "
                    "rules require a separate review. Acquisitions belong in a distinct "
                    "principal-investment lane with conflict disclosures, separate books, "
                    "and independent valuation support. Executor concierge work likewise "
                    "requires a defined scope and payer. Neither purchase principal nor "
                    "reimbursed estate expenses become retained brokerage commissions. Review "
                    "the eleven workstreams together every Monday, but budget only commission "
                    "production into the canonical scorecard. Any additional service must "
                    "justify its own economics and permissions before entering a separate forecast."
                ),
            ],
            "table": {
                "caption": "Eleven Mapped Probate Operator Plays: Evidence, Unit Economics & Failure Paths",
                "headers": [
                    "Mapped operator play",
                    "Production unit and practical economics",
                    "Required evidence before committing resources",
                    "Failure path and responsible operating response",
                ],
                "rows": [
                    [
                        "Docket-alert sourcing and parcel-level opportunity deduplication",
                        "Thirty monthly leads enter one controlled production cohort.",
                        "Save court source, docket identifier, parcel identifier, and retrieval timestamp.",
                        "Duplicate alerts merge into existing files before any additional outreach.",
                    ],
                    [
                        "Executor identity verification and appointment-power review",
                        "One authority packet supports each distinct estate appointment.",
                        "Current letters and appointment orders identify the authorized representative.",
                        "Conflicting appointments pause associated parcels until counsel resolves authority.",
                    ],
                    [
                        "Title, occupancy, insurance, and access triage",
                        "One preliminary title review precedes paid listing preparation.",
                        "Document liens, access permission, occupants, coverage, and ownership vesting.",
                        "Unresolved access or ownership moves the file into documented hold.",
                    ],
                    [
                        "Executor concierge coordination with bounded vendor work",
                        "Quote estate-paid services separately from the brokerage commission forecast.",
                        "Representative signs scope, spending ceiling, payer, and property-access instructions.",
                        "Disputed belongings remain untouched until authorized instructions resolve disposition.",
                    ],
                    [
                        "Probate listing production and negotiated brokerage compensation",
                        "A $500,000 sale at 2.5% produces $12,500 before splits.",
                        "Executed listing agreement and agency disclosures establish compensation terms.",
                        "Unaccepted pricing assumptions trigger a new broker price opinion.",
                    ],
                    [
                        "Buyer qualification and documented offer-management services",
                        "Five completed monthly sales require financeable, executable purchase contracts.",
                        "Retain proof of funds, financing conditions, and offer presentation records.",
                        "Financing deterioration activates backup buyers without bypassing estate instructions.",
                    ],
                    [
                        "Court-supervised sale coordination and independent-administration execution",
                        "One procedural calendar tracks each notice or confirmation requirement.",
                        "Counsel identifies applicable orders, notice deadlines, objections, and hearing dates.",
                        "Court continuances reset expected cash dates rather than manufacture receivables.",
                    ],
                    [
                        "Escrow completion and retained-commission cash reconciliation",
                        "A negotiated 68% retention converts $12,500 into $8,500.",
                        "Final settlement, brokerage disbursement statement, and bank credit must agree.",
                        "Short payment creates an exception rather than an unexplained expense.",
                    ],
                    [
                        "Probate-attorney relationship development through documented service quality",
                        "Track introductions, qualified appointments, and completed files without referral bounties.",
                        "Keep service reports and independently priced actual-service arrangements where permitted.",
                        "Reject compensation arrangements that improperly purchase covered settlement-service referrals.",
                    ],
                    [
                        "Principal acquisitions screening with segregated investment accounting",
                        "A proposed $300,000 purchase remains investment principal, not brokerage revenue.",
                        "Document capacity, conflicts, independent valuation, funding, and transaction-specific authority.",
                        "Unresolved conflicts remove the acquisition offer from the brokerage workflow.",
                    ],
                    [
                        "property_tax_assessment_appeal_contingency",
                        "Forty percent of $2,200 verified savings produces an $880 fee.",
                        "Annual assessment notice, comparable evidence, authorization, and final relief establish eligibility.",
                        "Licensed local specialists file permitted batches before jurisdiction-specific deadlines.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect scarce executor attention and keep contested files cheap",
                "body": (
                    "Experienced probate operators spend early effort on authority, occupancy, "
                    "and cash evidence rather than cosmetic pipeline volume."
                ),
                "items": [
                    "Ask counsel for the exact sale-power paragraph and operative order; attach both to the parcel record rather than relying on an email saying the executor can sell.",
                    "Give the representative one weekly exception report covering access, title, notices, buyer conditions, and the next decision requiring their instruction.",
                    "Photograph meter readings and property condition during authorized visits; separate safeguarding work from renovations that require another spending instruction.",
                    "Request the brokerage disbursement calculation before the anticipated funding date so split deductions can be challenged before the bank credit arrives.",
                ],
            },
        },
        {
            "heading": "2. Build a six-module ledger with serialized decisions and replay-safe events",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the six reference modules below as one executable local SQLite program, "
                    "pasted in numbered order into a Python 3.9 file. They create a production "
                    "reference core, not a replacement for a brokerage transaction-management "
                    "system. SQLite runs on one local filesystem; do not place this database "
                    "on a shared network drive or copy it between competing writers. Each "
                    "worker opens its own connection and executes mutations through run_once. "
                    "BEGIN IMMEDIATE serializes writers before they inspect mutable state; "
                    "unique constraints and version comparisons enforce identity and transition "
                    "invariants inside the same transaction. A retry with the same event key "
                    "and identical payload returns the original result. Reusing that key for "
                    "different instructions fails. A lock timeout is a failed attempt, not "
                    "permission to bypass the transaction; retry the unchanged event with "
                    "bounded backoff. Integer cents eliminate binary rounding from journal "
                    "postings. The reference supports one full retained-commission receipt "
                    "per parcel transaction, ordinary cash expenses, capital funding, and "
                    "commission refunds. Partial receipts, accrual accounting, investment "
                    "purchases, and additional service fees require explicit extensions rather "
                    "than improvised account reuse. This bounded scope makes the included "
                    "invariants inspectable and the Base cash model reproducible."
                ),
                (
                    "Separate documentary verification from software validation. A nonempty "
                    "authority reference proves that an operator supplied a reference; it "
                    "does not prove that a court granted the represented power. The authorized "
                    "reviewer must inspect the underlying documents before calling the state "
                    "transition function. Store documents in an access-controlled repository "
                    "and pass immutable object versions or content-addressed references into "
                    "the event payload. NEW becomes VERIFIED only with authority, title, and "
                    "sale-path evidence. LISTED requires the executed listing and agency "
                    "disclosures; ESCROW requires the contract, escrow instructions, and "
                    "current procedural clearance. CLOSED requires settlement evidence, "
                    "recording evidence, procedural completion, and a refreshed authority "
                    "check. HOLD is deliberately conservative: resumption returns through "
                    "VERIFIED instead of jumping directly back to escrow. The version field "
                    "rejects an operator acting on a stale screen, even when their requested "
                    "transition would otherwise be allowed. A CLOSED file cannot be silently "
                    "reopened; refunds correct cash through new journal entries. These controls "
                    "prevent local check-then-write races, but they cannot make an external "
                    "court action, bank system, or document repository transactional with "
                    "SQLite. No reference module sends payments, publishes listings, or "
                    "submits court documents."
                ),
                (
                    "Treat the final statement and the bank export as independent inputs. "
                    "The posting function checks the signed bank amount against the proposed "
                    "cash entry, then stores the statement reference and unique bank-line "
                    "identity in the same transaction as the balanced journal. A database "
                    "trigger refuses an unbalanced seal; sealed headers and all posting "
                    "lines are immutable. Source uniqueness prevents the same bank line "
                    "from financing two different journals, while a partial unique index "
                    "prevents duplicate full commission receipts on the same file. Refunds "
                    "cannot exceed that file's remaining recognized commission. Every "
                    "mutation also receives a durable payload, reviewer or source reference, "
                    "and replay result. Reconciliation views expose book cash, bank cash, "
                    "and differences rather than hiding missing matches inside aggregate "
                    "revenue. The QA function raises explicit failures instead of relying "
                    "on Python assertions that optimization could disable. Before deployment, "
                    "exercise concurrent duplicate submissions, stale versions, wrong "
                    "amounts, illegal transitions, and forced process termination against "
                    "a disposable database. Add authenticated application access, encrypted "
                    "backups, recovery drills, and restricted document permissions outside "
                    "this core. The snippets have not been executed here; their acceptance "
                    "tests and deployment review remain operator responsibilities."
                ),
            ],
            "table": {
                "caption": "Six-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and execution responsibility",
                    "Copy-pasteable Python and embedded SQLite implementation",
                    "Invariant and operational boundary being enforced",
                ],
                "rows": [
                    [
                        "Module 1: initialize constrained tables and serialize every mutation",
                        '''import hashlib
import json
import sqlite3

db = sqlite3.connect(
    "probate_ops.sqlite3",
    timeout=30.0,
    isolation_level=None,
)
db.row_factory = sqlite3.Row
db.execute("PRAGMA foreign_keys = ON")
db.execute("PRAGMA busy_timeout = 30000")
db.execute("PRAGMA journal_mode = WAL")
db.execute("PRAGMA synchronous = FULL")

db.executescript("""
CREATE TABLE IF NOT EXISTS files (
    file_id INTEGER PRIMARY KEY,
    county TEXT NOT NULL,
    docket TEXT NOT NULL,
    parcel TEXT NOT NULL,
    executor_ref TEXT NOT NULL,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    expected_fee_cents INTEGER NOT NULL CHECK(expected_fee_cents > 0),
    state TEXT NOT NULL DEFAULT 'NEW'
        CHECK(state IN (
            'NEW', 'VERIFIED', 'LISTED', 'ESCROW',
            'CLOSED', 'HOLD', 'LOST'
        )),
    version INTEGER NOT NULL DEFAULT 0 CHECK(version >= 0),
    UNIQUE(county, docket, parcel)
);
CREATE TABLE IF NOT EXISTS events (
    event_key TEXT PRIMARY KEY,
    digest TEXT NOT NULL,
    payload TEXT NOT NULL,
    result TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE TABLE IF NOT EXISTS accounts (
    code TEXT PRIMARY KEY,
    category TEXT NOT NULL
        CHECK(category IN ('asset', 'revenue', 'expense', 'equity'))
);
INSERT OR IGNORE INTO accounts VALUES ('cash', 'asset');
INSERT OR IGNORE INTO accounts VALUES ('commission', 'revenue');
INSERT OR IGNORE INTO accounts VALUES ('operating_cost', 'expense');
INSERT OR IGNORE INTO accounts VALUES ('owner_capital', 'equity');

CREATE TABLE IF NOT EXISTS journals (
    journal_id INTEGER PRIMARY KEY,
    source TEXT NOT NULL UNIQUE,
    file_id INTEGER REFERENCES files(file_id),
    kind TEXT NOT NULL CHECK(kind IN ('fee', 'cost', 'refund', 'capital')),
    posted_on TEXT NOT NULL,
    sealed INTEGER NOT NULL DEFAULT 0 CHECK(sealed IN (0, 1)),
    CHECK(kind NOT IN ('fee', 'refund') OR file_id IS NOT NULL)
);
CREATE UNIQUE INDEX IF NOT EXISTS one_fee_per_file
    ON journals(file_id) WHERE kind = 'fee';

CREATE TABLE IF NOT EXISTS postings (
    journal_id INTEGER NOT NULL REFERENCES journals(journal_id),
    line_no INTEGER NOT NULL,
    account TEXT NOT NULL REFERENCES accounts(code),
    debit INTEGER NOT NULL CHECK(debit >= 0),
    credit INTEGER NOT NULL CHECK(credit >= 0),
    PRIMARY KEY(journal_id, line_no),
    CHECK((debit > 0 AND credit = 0) OR
          (credit > 0 AND debit = 0))
);
CREATE TABLE IF NOT EXISTS bank_lines (
    bank_account TEXT NOT NULL,
    bank_line TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK(amount_cents != 0),
    statement_ref TEXT NOT NULL CHECK(length(statement_ref) > 0),
    journal_id INTEGER NOT NULL UNIQUE REFERENCES journals(journal_id),
    PRIMARY KEY(bank_account, bank_line)
);
CREATE TRIGGER IF NOT EXISTS check_journal_seal
BEFORE UPDATE OF sealed ON journals
WHEN OLD.sealed = 0 AND NEW.sealed = 1
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT(*) FROM postings
         WHERE journal_id = NEW.journal_id) < 2
        OR
        (SELECT COALESCE(SUM(debit - credit), 0) FROM postings
         WHERE journal_id = NEW.journal_id) != 0
        OR
        (SELECT COUNT(*) FROM bank_lines
         WHERE journal_id = NEW.journal_id) != 1
    THEN RAISE(ABORT, 'journal cannot be sealed') END;
END;
CREATE TRIGGER IF NOT EXISTS sealed_journal_no_update
BEFORE UPDATE ON journals WHEN OLD.sealed = 1
BEGIN
    SELECT RAISE(ABORT, 'sealed journal is immutable');
END;
CREATE TRIGGER IF NOT EXISTS journal_no_delete
BEFORE DELETE ON journals
BEGIN
    SELECT RAISE(ABORT, 'journal deletion is disabled');
END;
CREATE TRIGGER IF NOT EXISTS posting_insert_requires_draft
BEFORE INSERT ON postings
WHEN (SELECT sealed FROM journals
      WHERE journal_id = NEW.journal_id) != 0
BEGIN
    SELECT RAISE(ABORT, 'posting requires an unsealed journal');
END;
CREATE TRIGGER IF NOT EXISTS posting_no_update
BEFORE UPDATE ON postings
BEGIN
    SELECT RAISE(ABORT, 'posting updates are disabled');
END;
CREATE TRIGGER IF NOT EXISTS posting_no_delete
BEFORE DELETE ON postings
BEGIN
    SELECT RAISE(ABORT, 'posting deletion is disabled');
END;
CREATE TRIGGER IF NOT EXISTS bank_insert_requires_draft
BEFORE INSERT ON bank_lines
WHEN (SELECT sealed FROM journals
      WHERE journal_id = NEW.journal_id) != 0
BEGIN
    SELECT RAISE(ABORT, 'bank match requires an unsealed journal');
END;
CREATE TRIGGER IF NOT EXISTS bank_no_update
BEFORE UPDATE ON bank_lines
BEGIN
    SELECT RAISE(ABORT, 'bank match updates are disabled');
END;
CREATE TRIGGER IF NOT EXISTS bank_no_delete
BEFORE DELETE ON bank_lines
BEGIN
    SELECT RAISE(ABORT, 'bank match deletion is disabled');
END;
CREATE TRIGGER IF NOT EXISTS event_no_update
BEFORE UPDATE ON events
BEGIN
    SELECT RAISE(ABORT, 'event updates are disabled');
END;
CREATE TRIGGER IF NOT EXISTS event_no_delete
BEFORE DELETE ON events
BEGIN
    SELECT RAISE(ABORT, 'event deletion is disabled');
END;
""")

def required_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("a substantive text value is required")
    return value.strip()

def positive_cents(value):
    if type(value) is not int or value <= 0:
        raise ValueError("amount must be positive integer cents")
    return value

def run_once(event_key, payload, operation):
    event_key = required_text(event_key)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    db.execute("BEGIN IMMEDIATE")
    try:
        previous = db.execute(
            "SELECT digest, result FROM events WHERE event_key = ?",
            (event_key,),
        ).fetchone()
        if previous is not None:
            if previous["digest"] != digest:
                raise ValueError("event key was reused with different instructions")
            result = json.loads(previous["result"])
        else:
            result = operation()
            db.execute(
                "INSERT INTO events(event_key, digest, payload, result) "
                "VALUES (?, ?, ?, ?)",
                (event_key, digest, encoded, json.dumps(result, sort_keys=True)),
            )
        db.execute("COMMIT")
        return result
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
''',
                        "One local writer transaction owns each decision; database identities and durable replay results prevent duplicate effects.",
                    ],
                    [
                        "Module 2: normalize intake identity and calculate an explainable queue score",
                        '''def intake(event_key, county, docket, parcel, executor_ref,
           authority_seen, title_clear, ready_to_list,
           expected_fee_cents=850000):
    identity = [
        required_text(county).upper(),
        required_text(docket).upper(),
        required_text(parcel).upper(),
    ]
    executor_ref = required_text(executor_ref)
    expected_fee_cents = positive_cents(expected_fee_cents)
    flags = [authority_seen, title_clear, ready_to_list]
    if any(type(value) is not bool for value in flags):
        raise ValueError("scoring evidence flags must be Boolean")
    score = (
        40 * int(authority_seen)
        + 35 * int(title_clear)
        + 25 * int(ready_to_list)
    )
    payload = {
        "operation": "intake",
        "identity": identity,
        "executor_ref": executor_ref,
        "flags": flags,
        "expected_fee_cents": expected_fee_cents,
    }

    def apply():
        existing = db.execute(
            "SELECT * FROM files WHERE county = ? AND docket = ? AND parcel = ?",
            identity,
        ).fetchone()
        if existing is not None:
            if (
                existing["executor_ref"] != executor_ref
                or existing["expected_fee_cents"] != expected_fee_cents
                or existing["score"] != score
            ):
                raise ValueError("existing identity needs a reviewed amendment")
            return {"file_id": existing["file_id"], "created": False}
        cursor = db.execute(
            "INSERT INTO files(county, docket, parcel, executor_ref, score, "
            "expected_fee_cents) VALUES (?, ?, ?, ?, ?, ?)",
            tuple(identity) + (executor_ref, score, expected_fee_cents),
        )
        return {"file_id": cursor.lastrowid, "created": True}

    return run_once(event_key, payload, apply)
''',
                        "Scoring ranks evidence readiness without granting sale authority; duplicate parcels cannot silently overwrite reviewed facts.",
                    ],
                    [
                        "Module 3: enforce versioned verification, listing, escrow, and completion states",
                        '''TRANSITIONS = {
    "NEW": {"VERIFIED", "HOLD", "LOST"},
    "VERIFIED": {"LISTED", "HOLD", "LOST"},
    "LISTED": {"ESCROW", "HOLD", "LOST"},
    "ESCROW": {"CLOSED", "HOLD", "LOST"},
    "HOLD": {"VERIFIED", "LOST"},
    "CLOSED": set(),
    "LOST": set(),
}
REQUIRED_PROOF = {
    "VERIFIED": {"authority", "title", "sale_path"},
    "LISTED": {"listing", "agency_disclosures"},
    "ESCROW": {"contract", "escrow_instructions", "procedural_clearance"},
    "CLOSED": {
        "settlement", "recording", "procedural_completion",
        "authority_recheck",
    },
    "HOLD": {"reason"},
    "LOST": {"reason"},
}

def move_file(event_key, file_id, expected_version, target, proof, reviewer):
    if type(file_id) is not int or file_id <= 0:
        raise ValueError("file identity must be a positive integer")
    if type(expected_version) is not int or expected_version < 0:
        raise ValueError("expected version must be a nonnegative integer")
    reviewer = required_text(reviewer)
    target = required_text(target)
    if target not in REQUIRED_PROOF or not isinstance(proof, dict):
        raise ValueError("supported target and proof mapping are required")
    proof = {
        required_text(key): required_text(value)
        for key, value in proof.items()
    }
    if not REQUIRED_PROOF[target].issubset(proof):
        raise ValueError("required documentary references are missing")
    payload = {
        "operation": "move",
        "file_id": file_id,
        "expected_version": expected_version,
        "target": target,
        "proof": proof,
        "reviewer": reviewer,
    }

    def apply():
        row = db.execute(
            "SELECT state, version FROM files WHERE file_id = ?",
            (file_id,),
        ).fetchone()
        if row is None:
            raise ValueError("file does not exist")
        if row["version"] != expected_version:
            raise ValueError("stale file version")
        if target not in TRANSITIONS[row["state"]]:
            raise ValueError("state transition is not permitted")
        cursor = db.execute(
            "UPDATE files SET state = ?, version = version + 1 "
            "WHERE file_id = ? AND version = ?",
            (target, file_id, expected_version),
        )
        if cursor.rowcount != 1:
            raise RuntimeError("versioned transition failed")
        return {
            "file_id": file_id,
            "state": target,
            "version": expected_version + 1,
        }

    return run_once(event_key, payload, apply)
''',
                        "Stale screens fail inside the writer transaction; documentary truth still requires an authenticated human reviewer.",
                    ],
                    [
                        "Module 4: post balanced cash journals against independently sourced bank lines",
                        '''import datetime

def post_cash(event_key, kind, amount_cents, bank_account, bank_line,
              bank_cents, statement_ref, posted_on, file_id=None):
    if kind not in {"fee", "cost", "refund", "capital"}:
        raise ValueError("unsupported cash journal kind")
    amount_cents = positive_cents(amount_cents)
    bank_account = required_text(bank_account)
    bank_line = required_text(bank_line)
    statement_ref = required_text(statement_ref)
    posted_on = required_text(posted_on)
    if datetime.date.fromisoformat(posted_on).isoformat() != posted_on:
        raise ValueError("date must use the YYYY-MM-DD format")
    expected_bank = amount_cents if kind in {"fee", "capital"} else -amount_cents
    if type(bank_cents) is not int or bank_cents != expected_bank:
        raise ValueError("bank amount does not match proposed cash")
    if file_id is not None and (type(file_id) is not int or file_id <= 0):
        raise ValueError("file identity must be a positive integer")
    if kind in {"fee", "refund"} and file_id is None:
        raise ValueError("commission entries require a file")
    source = json.dumps([bank_account, bank_line], separators=(",", ":"))
    payload = {
        "operation": "post_cash",
        "kind": kind,
        "amount_cents": amount_cents,
        "bank_account": bank_account,
        "bank_line": bank_line,
        "bank_cents": bank_cents,
        "statement_ref": statement_ref,
        "posted_on": posted_on,
        "file_id": file_id,
    }

    def apply():
        if kind in {"fee", "refund"}:
            file_row = db.execute(
                "SELECT state, expected_fee_cents FROM files WHERE file_id = ?",
                (file_id,),
            ).fetchone()
            if file_row is None or file_row["state"] != "CLOSED":
                raise ValueError("commission requires a completed file")
            if kind == "fee" and amount_cents != file_row["expected_fee_cents"]:
                raise ValueError("receipt differs from the approved retained fee")
            if kind == "refund":
                remaining = db.execute(
                    "SELECT COALESCE(SUM(p.credit - p.debit), 0) "
                    "FROM postings p JOIN journals j "
                    "ON j.journal_id = p.journal_id "
                    "WHERE j.file_id = ? AND j.sealed = 1 "
                    "AND p.account = 'commission'",
                    (file_id,),
                ).fetchone()[0]
                if amount_cents > remaining:
                    raise ValueError("refund exceeds retained commission balance")
        legs = {
            "fee": [
                ("cash", amount_cents, 0),
                ("commission", 0, amount_cents),
            ],
            "cost": [
                ("operating_cost", amount_cents, 0),
                ("cash", 0, amount_cents),
            ],
            "refund": [
                ("commission", amount_cents, 0),
                ("cash", 0, amount_cents),
            ],
            "capital": [
                ("cash", amount_cents, 0),
                ("owner_capital", 0, amount_cents),
            ],
        }[kind]
        cursor = db.execute(
            "INSERT INTO journals(source, file_id, kind, posted_on) "
            "VALUES (?, ?, ?, ?)",
            (source, file_id, kind, posted_on),
        )
        journal_id = cursor.lastrowid
        for line_no, (account, debit, credit) in enumerate(legs, start=1):
            db.execute(
                "INSERT INTO postings(journal_id, line_no, account, debit, credit) "
                "VALUES (?, ?, ?, ?, ?)",
                (journal_id, line_no, account, debit, credit),
            )
        db.execute(
            "INSERT INTO bank_lines(bank_account, bank_line, amount_cents, "
            "statement_ref, journal_id) VALUES (?, ?, ?, ?, ?)",
            (bank_account, bank_line, bank_cents, statement_ref, journal_id),
        )
        db.execute(
            "UPDATE journals SET sealed = 1 WHERE journal_id = ?",
            (journal_id,),
        )
        return {"journal_id": journal_id, "bank_cents": bank_cents}

    return run_once(event_key, payload, apply)
''',
                        "Cash and evidence commit together; duplicate bank identities, excess refunds, and unbalanced seals fail without partial postings.",
                    ],
                    [
                        "Module 5: expose journal-level matching and monthly operating cash",
                        '''db.executescript("""
CREATE VIEW IF NOT EXISTS v_journal_reconciliation AS
SELECT
    j.journal_id,
    j.source,
    j.file_id,
    j.kind,
    j.posted_on,
    SUM(CASE WHEN p.account = 'cash'
             THEN p.debit - p.credit ELSE 0 END) AS book_cash_cents,
    MAX(b.amount_cents) AS bank_cash_cents,
    SUM(CASE WHEN p.account = 'cash'
             THEN p.debit - p.credit ELSE 0 END)
        - MAX(b.amount_cents) AS difference_cents,
    MAX(b.statement_ref) AS statement_ref
FROM journals j
JOIN postings p ON p.journal_id = j.journal_id
LEFT JOIN bank_lines b ON b.journal_id = j.journal_id
WHERE j.sealed = 1
GROUP BY j.journal_id;

CREATE VIEW IF NOT EXISTS v_monthly_cash AS
SELECT
    substr(j.posted_on, 1, 7) AS month,
    SUM(CASE WHEN p.account = 'commission'
             THEN p.credit - p.debit ELSE 0 END) AS revenue_cents,
    SUM(CASE WHEN p.account = 'operating_cost'
             THEN p.debit - p.credit ELSE 0 END) AS expense_cents,
    SUM(CASE WHEN p.account = 'commission'
             THEN p.credit - p.debit
             WHEN p.account = 'operating_cost'
             THEN p.credit - p.debit ELSE 0 END) AS owner_profit_cents,
    SUM(CASE WHEN p.account = 'cash'
             THEN p.debit - p.credit ELSE 0 END) AS cash_change_cents,
    SUM(CASE WHEN p.account = 'owner_capital'
             THEN p.credit - p.debit ELSE 0 END) AS capital_cents
FROM journals j
JOIN postings p ON p.journal_id = j.journal_id
WHERE j.sealed = 1
GROUP BY substr(j.posted_on, 1, 7);
""")
''',
                        "Capital funding never becomes commission revenue; every sealed bank movement remains visible beside its book amount.",
                    ],
                    [
                        "Module 6: validate journal integrity, bank control totals, and optional Base month",
                        '''def qa(bank_control_total_cents, base_month=None):
    if type(bank_control_total_cents) is not int:
        raise ValueError("bank control total must use integer cents")
    if base_month is not None:
        base_month = required_text(base_month)
    if db.in_transaction:
        raise RuntimeError("QA requires its own consistent snapshot")
    db.execute("BEGIN")
    try:
        failures = []
        integrity = db.execute("PRAGMA integrity_check").fetchall()
        if [row[0] for row in integrity] != ["ok"]:
            failures.append("database integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            failures.append("foreign key check failed")
        if db.execute(
            "SELECT COUNT(*) FROM journals WHERE sealed != 1"
        ).fetchone()[0]:
            failures.append("unsealed journals exist")
        if db.execute(
            "SELECT COUNT(*) FROM ("
            "SELECT journal_id FROM postings GROUP BY journal_id "
            "HAVING SUM(debit - credit) != 0)"
        ).fetchone()[0]:
            failures.append("unbalanced journals exist")
        if db.execute(
            "SELECT COUNT(*) FROM v_journal_reconciliation "
            "WHERE bank_cash_cents IS NULL OR difference_cents != 0"
        ).fetchone()[0]:
            failures.append("book and bank matches differ")
        stored_bank_total = db.execute(
            "SELECT COALESCE(SUM(amount_cents), 0) FROM bank_lines"
        ).fetchone()[0]
        if stored_bank_total != bank_control_total_cents:
            failures.append("independent bank control total differs")
        if base_month is not None:
            row = db.execute(
                "SELECT revenue_cents, expense_cents, owner_profit_cents "
                "FROM v_monthly_cash WHERE month = ?",
                (base_month,),
            ).fetchone()
            expected = (4250000, 3081250, 1168750)
            if row is None or tuple(row) != expected:
                failures.append("Base month does not reconcile")
        if failures:
            raise RuntimeError("; ".join(failures))
        result = {
            "status": "passed",
            "bank_control_total_cents": stored_bank_total,
        }
        db.execute("COMMIT")
        return result
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
''',
                        "QA reads one snapshot; independent full-period bank totals detect omitted net cash while line-level review detects offsetting omissions.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Open a uniquely identified parcel file",
                    "action": "Normalize county, docket, and parcel identifiers before calling intake.",
                    "detail": "Retain leading zeros, use stable county identifiers, and attach source evidence; queue scoring never substitutes for appointment review.",
                },
                {
                    "step": 2,
                    "title": "Verify authority and advance documentary states",
                    "action": "Have the authorized reviewer inspect evidence before each move_file call.",
                    "detail": "Pass the displayed version and immutable document references; investigate stale-version failures instead of replacing them with blind retries.",
                },
                {
                    "step": 3,
                    "title": "Match completion evidence to actual retained cash",
                    "action": "Compare settlement, brokerage split statement, and independently imported bank transaction.",
                    "detail": "Post only the operator's retained commission; reject partial or inconsistent receipts until the supported workflow has been explicitly extended.",
                },
                {
                    "step": 4,
                    "title": "Close the reporting period against an external control",
                    "action": "Run QA using the bank's net transaction total over the same complete ledger period.",
                    "detail": "Also compare line counts, gross credits, gross debits, and opening-to-closing balances; net totals alone can conceal offsetting omissions.",
                },
            ],
        },
        {
            "heading": "3. Reconcile brokerage economics and isolate the tax-appeal sidecar",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the Base case backward from retained commissions, not forward from "
                    "property values. The illustrative unit is a $500,000 completed sale "
                    "with a negotiated 2.5% brokerage-side commission, producing $12,500 "
                    "before the brokerage split. A negotiated 68% operator retention produces "
                    "$8,500 recognized operator revenue. These are scenario inputs, not "
                    "standardized compensation terms. Five completed and collected transactions "
                    "per month therefore produce $42,500 monthly revenue and $510,000 annually. "
                    "Underlying monthly property consideration is $2,500,000; it never "
                    "enters operator revenue. Budget $15,000 monthly fixed operating expense "
                    "and $3,162.50 incremental expense per collected closing. Five closings "
                    "add $15,812.50 variable expense, yielding total monthly expense of "
                    "$30,812.50 and owner net profit of $11,687.50. Annual expense is "
                    "$369,750, leaving exactly $140,250 at 27.5%. The $3,000–$18,000 "
                    "monthly operating range is used here for the fixed overhead envelope, "
                    "not represented as a ceiling on all transaction-dependent spending. "
                    "The owner-operator occupies one full-time seat; their residual "
                    "economic return is the owner-profit line, not another salary "
                    "deducted afterward. Track owner distributions separately from "
                    "operating expense so a cash withdrawal cannot change the measured "
                    "production margin."
                ),
                (
                    "Make the cost envelope inspectable before accepting the five-closing "
                    "target. The illustrative $15,000 fixed monthly budget allocates "
                    "$9,000 to nonowner payroll and burden, $2,500 to systems, insurance, "
                    "and workspace, and $3,500 to ongoing sourcing and relationship "
                    "development. Each collected closing carries $1,500 field and marketing "
                    "expense, $750 transaction coordination, $650 file-development expense, "
                    "and $262.50 bookkeeping and closing administration. The resulting "
                    "$3,162.50 is a cohort allocation, not a claim that every failed "
                    "file costs nothing. The illustration assumes those allocations cover "
                    "the cohort's failed-file work and are paid in the collection month; "
                    "actual prepaid marketing and contractor deposits require a dated "
                    "working-capital schedule. Conservative revenue of $120,000 less "
                    "$96,000 expense yields $24,000 profit. Scaled revenue of $900,000 "
                    "less $585,000 expense yields $315,000 profit with three full-time "
                    "people and four contractors. Do not force those cases into the "
                    "Base model's identical price and throughput assumptions: they are "
                    "separate canonical annual scenarios. Preserve the scorecard totals "
                    "while testing each operating plan against local compensation, "
                    "contractor availability, collection delays, and the actual mix "
                    "of property values."
                ),
                (
                    "Implement property_tax_assessment_appeal_contingency as a segregated "
                    "TRACK_1 service rather than an unexplained commission uplift. At "
                    "annual notice release, ingest the assessor valuation roll, parcel "
                    "characteristics, taxable-value components, appeal deadline, and "
                    "notice reference. An automated valuation model compares recent "
                    "sales and neighboring equity ratios to flag potential overassessment; "
                    "it does not establish legal entitlement to relief. In California, "
                    "acquisition-value rules and exemptions can explain apparently "
                    "unequal assessments, so local specialists must filter those cases "
                    "before filing. Suppose supported taxable value falls $200,000 "
                    "and the applicable effective rate is 1.1%: verified first-year "
                    "tax reduction is $2,200, and a permitted 40% contingency earns "
                    "$880. Fifty successful parcels generate $44,000 gross service "
                    "fees before specialist shares and delivery costs, entirely "
                    "outside the $510,000 brokerage case. Price within the specified "
                    "30–50% range only where permitted and contractually authorized. "
                    "California Revenue and Taxation Code section 1603 controls "
                    "assessment-appeal application requirements and filing windows; "
                    "verify the county's applicable calendar rather than hard-coding "
                    "one statewide date. In regulated jurisdictions, partner with "
                    "licensed local consultants or attorneys of record. Prepare "
                    "pre-deadline batches, use supported electronic filing channels, "
                    "retain acknowledgments, and suspend collection until actual "
                    "first-year relief is verified."
                ),
            ],
            "table": {
                "caption": "Retained-Commission Ledger Bridge and Segregated Service Economics",
                "headers": [
                    "Economic control or modeled scenario",
                    "Exact arithmetic and recognized revenue boundary",
                    "Evidence required for operator reconciliation",
                    "Failure response that preserves clean reporting",
                ],
                "rows": [
                    [
                        "Base unit economics for one collected brokerage transaction",
                        "$500,000 × 2.5% × 68% equals $8,500 retained commission.",
                        "Match negotiated compensation, split schedule, final disbursement, and bank credit.",
                        "Investigate split discrepancies before changing expected retained fee records.",
                    ],
                    [
                        "Base monthly production at five collected completed transactions",
                        "$42,500 revenue minus $30,812.50 expense equals $11,687.50 profit.",
                        "Five distinct closed parcel files support five independent bank receipts.",
                        "A missed collection lowers cash rather than creating fictional completion.",
                    ],
                    [
                        "Base annual scorecard with two full-time people and three contractors",
                        "$510,000 revenue minus $369,750 expense equals $140,250 profit.",
                        "Twelve mature months reconcile to the exact 27.5% margin.",
                        "Separate prepaid costs and unpaid bills from the simplified cash illustration.",
                    ],
                    [
                        "Conservative annual scorecard using the canonical staffing configuration",
                        "$120,000 revenue minus $96,000 expense equals $24,000 profit.",
                        "Two full-time people and three contractors support the 20% margin.",
                        "Reduce committed spending when collection pace cannot sustain fixed costs.",
                    ],
                    [
                        "Scaled annual scorecard using the canonical seven-person configuration",
                        "$900,000 revenue minus $585,000 expense equals $315,000 profit.",
                        "Three full-time people and four contractors support the 35% margin.",
                        "Add production capacity only after reviewing actual bottleneck and margin evidence.",
                    ],
                    [
                        "Separate property-tax appeal service with verified first-year relief",
                        "$200,000 × 1.1% × 40% equals $880 gross service fees.",
                        "Final assessment relief and actual tax calculation establish the collectible basis.",
                        "Exclude all appeal fees from canonical retained brokerage revenue totals.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before spending, listing, closing, or recognizing cash",
                "body": (
                    "A failed check stops the affected action, preserves the evidence, "
                    "and assigns a specific person to resolve the exception."
                ),
                "items": [
                    "Verify current appointment, sale powers, required notices or court procedures, and the representative's authority for this specific parcel.",
                    "Verify occupancy, access permission, insurance, preliminary title, and the signed scope before committing field contractors or marketing expenditure.",
                    "Verify the executed compensation agreement, brokerage split, final settlement, and expected retained amount before accepting a commission posting.",
                    "Verify independent bank-line identity, exact cents, documentary completion, and a passing ledger reconciliation before reporting collected revenue.",
                ],
            },
        },
        {
            "heading": "4. Walk a mature 90-day cohort without disguising the startup cash gap",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk starts with an established pipeline, "
                    "not a newly launched brokerage. Opening inventory contains ten "
                    "executable files from two earlier cohorts: five are scheduled "
                    "to collect in Month 1 and five in Month 2. Their prior "
                    "authority work, marketing, and fallout have already occurred. "
                    "The operator also starts with $60,000 unrestricted working cash "
                    "after any setup spending; this is liquidity, not revenue. Each "
                    "new monthly cohort contains thirty leads. Six are scrubbed "
                    "for duplication, ownership mismatch, or absent actionable authority, "
                    "and six decline or select another provider. Eighteen remain "
                    "qualified: twelve enter documented nurture and six sign viable "
                    "listing engagements. One signed engagement per cohort falls "
                    "out before funding, leaving five expected collections. The "
                    "illustrated collection lag is two months after this signed, "
                    "authority-ready cohort entry. It is not two months after "
                    "a raw probate filing. The stated time to first deal remains "
                    "4–18 months for a new operator, because sourcing, appointment, "
                    "relationship development, and contested estate work can precede "
                    "this production window. Opening files therefore supply the "
                    "first two months of cash while the new Month 1 cohort "
                    "supplies Month 3."
                ),
                (
                    "At thirty days, the business has collected $42,500 from "
                    "five opening files, paid $30,812.50 modeled operating expense, "
                    "and generated $11,687.50 operating cash. Bank cash rises "
                    "from $60,000 to $71,687.50 without treating the opening "
                    "capital as income. At sixty days, the second opening "
                    "cohort produces the same receipt and expense pattern, "
                    "taking cumulative operating cash to $23,375 and bank "
                    "cash to $83,375. At ninety days, five Month 1 files "
                    "collect another $42,500; cumulative revenue is $127,500, "
                    "expense is $92,437.50, operating cash is $35,062.50, "
                    "and bank cash is $95,062.50. Across the three new "
                    "cohorts, ninety leads yield eighteen scrubs, eighteen "
                    "declines, fifty-four qualified prospects, eighteen signed "
                    "engagements, and thirty-six nurture records. Three signed "
                    "engagements fail. Of the remaining fifteen, five have "
                    "collected by day ninety and ten are scheduled for "
                    "Months 4 and 5. Together with the ten opening "
                    "collections, that produces exactly fifteen completed "
                    "collections during the quarter. This inventory bridge "
                    "prevents the common error of counting future signed "
                    "listings as current cash or counting the opening backlog "
                    "again as newly sourced business."
                ),
                (
                    "Annualize the mature quarter only after labeling its assumptions: "
                    "$127,500 times four equals $510,000 revenue, $92,437.50 "
                    "times four equals $369,750 expense, and $35,062.50 times "
                    "four equals $140,250 owner profit. Collections and operating "
                    "payments coincide in this illustration; accrual timing, "
                    "capital expenditures, borrowing, owner distributions, and "
                    "personal taxes are outside that cash bridge. A cold-start "
                    "comparison with no opening backlog and the same hypothetical "
                    "Month 3 collections pays $15,000 fixed expense in each "
                    "of Months 1 and 2, then $30,812.50 in Month 3. "
                    "It collects only $42,500, producing negative $18,312.50 "
                    "cumulative operating cash and ending with $41,687.50 "
                    "from the same $60,000 opening balance. Even that "
                    "comparison is faster than the stated startup deal "
                    "timeline and must not become a launch promise. "
                    "Stress-test a court continuance by moving the affected "
                    "receipt to its revised month while retaining already "
                    "committed payroll and vendor payments. Stress-test "
                    "family disputes by moving the file to HOLD rather "
                    "than merely reducing its probability percentage. "
                    "When liquidity tightens, defer discretionary promotion, "
                    "renegotiate authorized vendor timing, and protect "
                    "necessary safeguarding work; never borrow against "
                    "estate sale proceeds as though they were brokerage cash."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Month and distinct cohort movement",
                    "Lead disposition, scrubs, losses, and remaining inventory",
                    "Retained cash collections and timing assumptions",
                    "Operating expense paid during the illustrated month",
                    "Cumulative operating cash and unrestricted bank balance",
                ],
                "rows": [
                    [
                        "Month 1 intake: create the first new thirty-lead cohort",
                        "Six scrubbed; six declined; twelve nurture; six signed, with one subsequent fallout.",
                        "Five surviving new engagements target Month 3 collections, not immediate revenue.",
                        "New-cohort work is included in the stated pooled monthly cost allocation.",
                        "Intake alone changes neither collected revenue nor the opening $60,000 cash.",
                    ],
                    [
                        "Month 1 collections: complete five previously matured opening files",
                        "Five opening files close; five additional opening files remain for Month 2.",
                        "Five receipts at $8,500 produce $42,500 collected retained commissions.",
                        "$15,000 fixed plus $15,812.50 variable equals $30,812.50 paid operating expense.",
                        "Cumulative operating cash reaches $11,687.50; unrestricted bank cash reaches $71,687.50.",
                    ],
                    [
                        "Month 2 intake: create the second new thirty-lead cohort",
                        "Six scrubbed; six declined; twelve nurture; six signed, with one subsequent fallout.",
                        "Five surviving new engagements target Month 4, outside this quarter's collections.",
                        "Pooled cohort costs remain inside Month 2 fixed and variable allocations.",
                        "The intake row creates no additional cash movement beyond monthly collections.",
                    ],
                    [
                        "Month 2 collections: complete the remaining five opening files",
                        "Opening backlog reaches zero; Month 1 survivors remain scheduled for Month 3.",
                        "Another five $8,500 receipts lift cumulative retained collections to $85,000.",
                        "Another $30,812.50 paid expense lifts cumulative operating payments to $61,625.",
                        "Cumulative operating cash reaches $23,375; unrestricted bank cash reaches $83,375.",
                    ],
                    [
                        "Month 3 intake: create the third new thirty-lead cohort",
                        "Quarter totals reach eighteen scrubs, eighteen declines, thirty-six nurture records, and three signed fallouts.",
                        "Five Month 3 survivors target Month 5; ten future collections remain overall.",
                        "Month 3 pooled costs include modeled work across active and failed files.",
                        "Future engagements remain inventory rather than additions to current bank cash.",
                    ],
                    [
                        "Month 3 collections: complete five surviving Month 1 engagements",
                        "Quarter closes fifteen total files: ten opening files plus five newly sourced files.",
                        "Quarter collections reach $127,500, equivalent to the $510,000 annual Base run rate.",
                        "Quarter paid expense reaches $92,437.50, equivalent to $369,750 annual operating expense.",
                        "Cumulative operating cash reaches $35,062.50; unrestricted bank cash reaches $95,062.50.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A probate file becomes a business result only when valid authority, completed settlement, and retained cash tell the same story.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one county-docket-parcel identity per transaction and merge duplicate alerts before outreach or contractor assignment.",
        "Obtain current appointment evidence and a transaction-specific sale-path instruction covering notices, objections, confirmation, and authorized signatures.",
        "Paste the six reference modules into a local test program, then test duplicate events, conflicting payloads, stale versions, rollback, refunds, and concurrent writers.",
        "Rebuild the Base budget around five $8,500 retained monthly commissions, $15,000 fixed expense, and $3,162.50 allocated variable expense per collection.",
        "Maintain separate brokerage, acquisition-principal, estate-pass-through, and property-tax-service reporting so only retained commissions enter the canonical scorecard.",
        "Reconcile the 90-day cohort using opening backlog, dated bank receipts, failed-file costs, future inventory, and independent statement control totals before annualizing results.",
    ],
    "statutory_citations": [
        {
            "title": "California Probate Code section 10501 — Independent administration and court-supervised powers",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "relevance": (
                "Identify powers requiring court supervision and the limitations relevant "
                "to a representative operating under limited independent-administration authority."
            ),
        },
        {
            "title": "California Probate Code section 10580 — Notice of proposed action",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
            "relevance": (
                "Determine when a proposed transaction requires notice under the statutory "
                "notice framework before treating a sale as procedurally executable."
            ),
        },
        {
            "title": "California Probate Code section 10308 — Court confirmation and increased offers",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10308.",
            "relevance": (
                "Court-supervised sale planning must account for qualifying increased offers "
                "and confirmation procedures rather than treating an accepted contract as final."
            ),
        },
        {
            "title": "California Business and Professions Code section 10130 — Real estate license requirement",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "relevance": (
                "Assign activities requiring a real estate license to properly licensed "
                "people and distinguish brokerage services from unlicensed administrative support."
            ),
        },
        {
            "title": "12 U.S.C. section 2607 — Prohibition against kickbacks and unearned fees",
            "url": "https://www.law.cornell.edu/uscode/text/12/2607",
            "relevance": (
                "Review attorney and other referral arrangements for covered settlement "
                "transactions; distinguish prohibited referral compensation from permitted actual services."
            ),
        },
        {
            "title": "California Revenue and Taxation Code section 1603 — Assessment appeal applications",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=1603.",
            "relevance": (
                "Use the applicable assessment-appeal filing requirements and county calendar "
                "when preparing authorized property-tax protest batches."
            ),
        },
        {
            "title": "Texas Occupations Code chapter 1152 — Property tax consultants",
            "url": "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1152.htm",
            "relevance": (
                "Check registration, exemptions, and practice requirements before offering "
                "Texas property-tax consulting or assigning representation to a local partner."
            ),
        },
    ],
}
