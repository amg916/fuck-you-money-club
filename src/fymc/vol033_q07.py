from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "insurance-housing-end-to-end-production-and-90-day-cohort",
    "question_prompt": "How does an operator execute insurance housing & corporate rental arbitrage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Carrier ALE Authorizations, Landlord Sublease Addenda, SQLite Posting Controls, and a $197,500 Quarterly Billing Bridge",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #33, Insurance Housing & Corporate Rental Arbitrage, ranks #07 of 36 "
        "with a 90/100 Money-to-Manpower Score. This chapter converts 12 mapped plays "
        "into an executable operating sequence: permissioned demand, documented placement "
        "authority, protected inventory, controlled occupancy, and reconciled cash. The "
        "scorecard produces annual owner profit of $21,600 Conservative, $150,100 Base, "
        "and $364,000 Scaled. Its 45% retained share separates landlord and utility "
        "pass-throughs from operator contribution. Six copy-pasteable engineering modules "
        "demonstrate serialized reservations, balanced journals, durable outbound intent, "
        "and repeatable reconciliation. A worked 90-day cohort bills $197,500, earns "
        "$37,525, and generates $20,025 operating cash while carrying $17,500 receivables. "
        "The operating discipline is simple: an authorized placement, a collectible "
        "invoice, and a matched bank receipt are three different events."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$180,000",
            "context": "Annual gross billings; $81,000 retained revenue at 45%",
            "note": "12% gross-basis net margin; 26.67% retained margin; $21,600 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$790,000",
            "context": "Annual gross billings; $355,500 retained revenue at 45%",
            "note": "19.0% gross-basis net margin; 42.22% retained margin; $150,100 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,400,000",
            "context": "Annual gross billings; $630,000 retained revenue at 45%",
            "note": "26% gross-basis net margin; 57.78% retained margin; $364,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Convert permissioned demand into a documented placement order",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the payer, not the apartment. An insurance Additional Living Expense "
                    "placement begins with a displaced household, an adjuster or authorized housing "
                    "coordinator, and a documented coverage window. Capture the claim reference, "
                    "authorized billing entity, approved nightly ceiling, household requirements, "
                    "anticipated repair duration, and extension decision date. Record a coordinator's "
                    "instruction separately from a carrier payment undertaking; one does not establish "
                    "the other. Corporate relocation follows the same sequence with a purchase order, "
                    "employee authorization, and accounts-payable contact replacing claim documentation. "
                    "Use HubSpot or Airtable for relationship work, but make the ledger placement "
                    "identifier the durable reference on every quote, lease, invoice, and bank match. "
                    "The operating map contains twelve plays: permissioned demand, warm routing, payer "
                    "verification, coverage-window scoring, inventory sourcing, landlord authorization, "
                    "placement packaging, move-in execution, telemetry triage, extension billing, "
                    "turnover recovery, and cash reconciliation. These are this chapter's twelve "
                    "workflow mappings, not twelve additional catalog identifiers. Each has an owner, "
                    "an evidence artifact, and a measurable exit condition. A coordinator's enthusiastic "
                    "telephone request remains an intake record until rate, dates, authority, and "
                    "payment responsibility are documented. Keep household hardship details out of "
                    "marketing tools; store only the requirements necessary to deliver suitable housing."
                ),
                (
                    "The catalog play high_velocity_dm_outbound_systems belongs at the demand edge, "
                    "not inside carrier collections. Replace blind cold mass-DM blasts, PeerFloodError "
                    "failures, and silent Message Request graveyards with comment-to-DM triggers, "
                    "hand-raiser reactions, and warm-signal routing through authorized inboxes. A useful "
                    "offer is a location-specific availability digest for relocation coordinators; it "
                    "should not expose displaced households or claim details. Require a user-initiated "
                    "comment, reaction, or inbound message before automated DM dispatch, and send "
                    "external links only after the prospect replies. Where the platform does not "
                    "support that trigger through its permitted interface, use a human response or "
                    "an inbound form instead. Deduplicate the initiating platform event before assigning "
                    "an inbox. In Month 1, sixty hand-raisers yield thirty-six qualified conversations, "
                    "twenty quoted opportunities, fourteen verified opportunities, and ten signed "
                    "placements. Six quote-stage scrubs consume time but create neither revenue nor "
                    "inventory commitments. Four verified opportunities remain unsigned. At $150 per "
                    "occupied day, three hundred billed days produce $45,000 gross billings. The "
                    "45% retained contribution is $20,250 before operating expense. Optimize that "
                    "conversion and collection chain rather than raw message volume; adding inboxes "
                    "must never become a mechanism for bypassing platform restrictions."
                ),
                (
                    "Before making a property available, obtain the landlord's explicit written "
                    "corporate-housing sublease addendum naming the permitted use, occupant substitution "
                    "mechanism, term boundaries, insurance requirements, and utility responsibility. "
                    "Do not treat a general residential lease as permission to operate relocation "
                    "inventory. New York Real Property Law section 226-b illustrates why local lease "
                    "and subletting rules require property-specific review; its statutory scope and "
                    "exceptions matter. Inspect habitability, working smoke and carbon-monoxide devices, "
                    "egress, furnishings, and accessibility requirements before collecting move-in "
                    "money. Apply documented accommodation procedures consistent with 42 U.S.C. "
                    "3604(f) and 24 CFR 100.204 rather than scoring disability-related requests "
                    "as commercial risk. Evaluate occupancy taxes separately for each jurisdiction. "
                    "Texas Tax Code section 156.101 addresses permanent residents occupying qualifying "
                    "lodging for at least thirty consecutive days, but its state rule does not "
                    "automatically resolve every local levy or documentation question. Obtain the "
                    "applicable written occupancy evidence and preserve it with the invoice. Score "
                    "economics on authorized duration, expected collections, and available inventory, "
                    "not protected characteristics. Reject a placement when lawful use, documented "
                    "payment responsibility, or acceptable property condition cannot be established; "
                    "offer an authorized alternative rather than quietly weakening the placement file."
                ),
            ],
            "table": {
                "caption": "Twelve Mapped Plays: Intake Evidence, Unit Economics, and Failure Fallbacks",
                "headers": [
                    "Mapped workflow plays and accountable owner",
                    "Required evidence before committing operator resources",
                    "Concrete unit calculation and operating measure",
                    "Failure response protecting cash and occupancy",
                ],
                "rows": [
                    [
                        "Permissioned demand: high_velocity_dm_outbound_systems; relationship owner operates TRACK_2",
                        "Preserve initiating comment or reaction and subsequent prospect reply",
                        "Sixty hand-raisers produce thirty-six qualified Month 1 conversations",
                        "Use inbound forms when permitted trigger interfaces are unavailable",
                    ],
                    [
                        "Warm routing: relationship owner assigns one accountable inbox",
                        "Store platform event identifier and current conversation assignment",
                        "One initiating event creates one durable outbound intent record",
                        "Quarantine uncertain sends rather than dispatching duplicate external messages",
                    ],
                    [
                        "Payer verification and coverage-window scoring: operator owns both decisions",
                        "Obtain payer authority, authorized dates, rate ceiling, and billing address",
                        "Twenty quotes become fourteen verified opportunities and ten signed placements",
                        "Hold unsigned opportunities outside committed property inventory and revenue",
                    ],
                    [
                        "Inventory sourcing and landlord authorization: property coordinator owns both",
                        "Attach signed corporate-housing addendum and inspected property condition record",
                        "Three hundred occupied days at $150 generate $45,000 billings",
                        "Substitute authorized inventory when proposed lease terms prohibit occupancy",
                    ],
                    [
                        "Placement packaging: operator translates authorization into executable occupant documents",
                        "Match household requirements, approved quote, purchase order, and occupancy agreement",
                        "Forty-five percent of $45,000 leaves $20,250 retained contribution",
                        "Reprice or decline placements failing documented duration and cost thresholds",
                    ],
                    [
                        "Move-in execution and telemetry triage: field contractor owns delivery",
                        "Record inventory photographs, tested access code, and disclosed sensor settings",
                        "One property inspection precedes each new household access activation",
                        "Use attended key delivery when smart-lock provisioning cannot be verified",
                    ],
                    [
                        "Extension billing: operator owns authorization before continued paid occupancy",
                        "Obtain written dates and rate changes before adding reserved nights",
                        "Ten extra nights at $175 add $1,750 authorized gross billings",
                        "Escalate expiring authority without using self-help lockouts against occupants",
                    ],
                    [
                        "Turnover recovery and cash reconciliation: field contractor and operator",
                        "Match condition evidence, vendor invoices, payer remittance, and bank settlement",
                        "Quarterly $37,525 earnings bridge to $20,025 operating cash",
                        "Separate disputed damage recovery from collectible authorized housing invoices",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Preserve the spread before increasing placement volume",
                "body": "Experienced housing operators negotiate the edges of the stay before they celebrate the nightly rate.",
                "items": [
                    "Ask the coordinator for the next repair milestone and extension decision owner; diary both seven days before current authority expires.",
                    "Negotiate a landlord early-release schedule separately from the payer cancellation schedule, then price the uncovered gap explicitly.",
                    "Photograph utility meter readings at possession and departure; bill contractual caps against dated evidence rather than estimated excess usage.",
                    "Give the payer one stable placement reference across every portal and invoice, while retaining each portal's own submission receipt.",
                ],
            },
        },
        {
            "heading": "2. Build the six-module ledger and serialize every irreversible transition",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference below is deliberately small enough to inspect. Copy the six source "
                    "cells, in row order, into housing_reference.py and run Python 3.9 or later. "
                    "It creates a local SQLite database, exposes intake and transition functions, "
                    "posts balanced journals, and provides a repeatable demonstration. The chapter "
                    "does not report an executed test run. Use a single host with a local filesystem; "
                    "this design is not a distributed database or a shared network-drive recipe. "
                    "Every business mutation opens its own connection, obtains BEGIN IMMEDIATE, "
                    "and either commits completely or rolls back. SQLite therefore serializes "
                    "competing writers before they inspect inventory or journal identity. A busy "
                    "timeout fails closed instead of bypassing the lock. Unique event keys make "
                    "replayed requests harmless only when their payloads match; changed payloads "
                    "raise an exception. Interval triggers reject overlapping reserved, active, "
                    "or historical completed stays, including adjacent requests arriving concurrently. "
                    "Dates use half-open intervals, so one departure can share a date with the "
                    "next arrival. Production deployment still needs encrypted storage, access "
                    "controls, tested backups, migration management, and monitoring. Those controls "
                    "support this transactional core; they do not replace database-enforced identity "
                    "or inventory invariants."
                ),
                (
                    "The verification and funds workflow separates commercial facts from state labels. "
                    "A draft becomes VERIFIED only after payer evidence exists and the unit has "
                    "a recorded landlord addendum. RESERVED additionally requires any contractual "
                    "deposit to appear as posted cash against that placement's deposit liability. "
                    "A deposit is not retained revenue. If local rules require a trust account "
                    "or regulated escrow arrangement, use the required custodian and maintain "
                    "a separate bank-control implementation; the reference is a liability ledger, "
                    "not an escrow service. ACTIVE means actual possession, and CLOSED means "
                    "documented departure, not merely an adjuster's claim closure. A reserved "
                    "stay can be cancelled before possession; an active household needs a lawful "
                    "departure process. Optimistic version checks reject stale instructions even "
                    "though writes are serialized. The transition API accepts evidence references "
                    "rather than pretending software can independently authenticate a carrier letter. "
                    "Bind those references to access-controlled documents and human verification "
                    "in the application layer. After reservation, inventory dates cannot be edited "
                    "casually. An extension requires an explicit replacement workflow or a "
                    "separately reserved adjacent interval, with fresh payer authority and another "
                    "overlap check. Never overwrite the original commercial agreement to make "
                    "a late extension look timely."
                ),
                (
                    "Money posting and external delivery have different correctness boundaries. The "
                    "journal enforces at least two nonzero lines, a zero signed-cent balance, "
                    "immutable posted entries, and one payload per business event. Correct a "
                    "mistake with a reversing entry and a replacement event, not an UPDATE "
                    "to a posted line. The outbox records durable external intent in the "
                    "same transaction as a state change. A worker claims that intent with "
                    "a unique token before making any external request. Exactly-once delivery "
                    "cannot be manufactured across an arbitrary housing portal or messaging "
                    "service: pass the event key where the provider supports idempotency, "
                    "and quarantine an uncertain outcome otherwise. A crashed CLAIMED item "
                    "requires investigation; it is never automatically returned to READY. "
                    "This removes competing-worker dispatch races without promising impossible "
                    "network semantics. ALE Solutions and CRS interfaces should be used only "
                    "through authorized integrations or documented manual submissions, with "
                    "portal receipts retained. Smart-lock provisioning uses the same outbox "
                    "pattern but needs a separate access policy. Never tie an occupied "
                    "household's door access to a delinquent invoice. The six modules establish "
                    "transactional correctness for their stated scope; vendor authentication, "
                    "document review, and lawful occupancy decisions remain explicit operating responsibilities."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and execution order within one file",
                    "Enforced boundary and operator evidence requirement",
                    "Copy-pasteable Python source in shared module namespace",
                    "Failure behavior and production integration requirement",
                ],
                "rows": [
                    [
                        "Module 1: initialize schema, transaction context, and immutable journal controls",
                        "Local SQLite writer serialization protects reservations and balanced posted entries",
                        '''import hashlib
import json
import secrets
import sqlite3
from contextlib import contextmanager
from datetime import date

DB = "housing_reference.sqlite3"

def fingerprint(value):
    packed = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(packed.encode("utf-8")).hexdigest()

@contextmanager
def transaction():
    connection = sqlite3.connect(DB, timeout=30, isolation_level=None)
    connection.row_factory = sqlite3.Row
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA synchronous = FULL")
        connection.execute("BEGIN IMMEDIATE")
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()

SCHEMA = """
CREATE TABLE IF NOT EXISTS unit (
    id TEXT PRIMARY KEY,
    addendum_ref TEXT NOT NULL CHECK(length(addendum_ref) > 0)
);
CREATE TABLE IF NOT EXISTS stay (
    id TEXT PRIMARY KEY,
    source_event TEXT NOT NULL UNIQUE,
    payload_hash TEXT NOT NULL,
    unit_id TEXT NOT NULL REFERENCES unit(id),
    starts TEXT NOT NULL,
    ends TEXT NOT NULL CHECK(ends > starts),
    authorized_cents INTEGER NOT NULL CHECK(authorized_cents > 0),
    deposit_required INTEGER NOT NULL CHECK(deposit_required >= 0),
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    payer_ref TEXT NOT NULL DEFAULT '',
    state TEXT NOT NULL DEFAULT 'DRAFT'
        CHECK(state IN ('DRAFT','VERIFIED','RESERVED','ACTIVE','CLOSED','CANCELLED')),
    version INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    payload_hash TEXT NOT NULL,
    effective_date TEXT NOT NULL,
    stay_id TEXT REFERENCES stay(id),
    state TEXT NOT NULL DEFAULT 'DRAFT' CHECK(state IN ('DRAFT','POSTED'))
);
CREATE TABLE IF NOT EXISTS line (
    journal_id INTEGER NOT NULL REFERENCES journal(id),
    sequence INTEGER NOT NULL,
    account TEXT NOT NULL CHECK(account IN (
        'cash','receivable','vendor_payable','deposit_liability',
        'retained_revenue','opex_expense'
    )),
    cents INTEGER NOT NULL CHECK(typeof(cents) = 'integer' AND cents != 0),
    PRIMARY KEY(journal_id, sequence)
);
CREATE TABLE IF NOT EXISTS outbox (
    event_key TEXT PRIMARY KEY,
    payload TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'READY'
        CHECK(state IN ('READY','CLAIMED','SENT','UNCERTAIN')),
    token TEXT UNIQUE,
    receipt TEXT
);
CREATE TRIGGER IF NOT EXISTS stay_overlap_insert
BEFORE INSERT ON stay
WHEN NEW.state IN ('RESERVED','ACTIVE','CLOSED')
BEGIN
    SELECT RAISE(ABORT, 'inventory overlap')
    WHERE EXISTS (
        SELECT 1 FROM stay s
        WHERE s.unit_id = NEW.unit_id
          AND s.state IN ('RESERVED','ACTIVE','CLOSED')
          AND s.starts < NEW.ends AND NEW.starts < s.ends
    );
END;
CREATE TRIGGER IF NOT EXISTS stay_overlap_update
BEFORE UPDATE ON stay
WHEN NEW.state IN ('RESERVED','ACTIVE','CLOSED')
BEGIN
    SELECT RAISE(ABORT, 'inventory overlap')
    WHERE EXISTS (
        SELECT 1 FROM stay s
        WHERE s.id != NEW.id AND s.unit_id = NEW.unit_id
          AND s.state IN ('RESERVED','ACTIVE','CLOSED')
          AND s.starts < NEW.ends AND NEW.starts < s.ends
    );
END;
CREATE TRIGGER IF NOT EXISTS stay_dates_frozen
BEFORE UPDATE OF unit_id, starts, ends ON stay
WHEN OLD.state IN ('RESERVED','ACTIVE','CLOSED')
BEGIN
    SELECT RAISE(ABORT, 'reserved inventory requires replacement workflow');
END;
CREATE TRIGGER IF NOT EXISTS journal_insert_draft
BEFORE INSERT ON journal WHEN NEW.state != 'DRAFT'
BEGIN
    SELECT RAISE(ABORT, 'journal must begin as draft');
END;
CREATE TRIGGER IF NOT EXISTS journal_balance
BEFORE UPDATE OF state ON journal WHEN NEW.state = 'POSTED'
BEGIN
    SELECT RAISE(ABORT, 'journal is incomplete or unbalanced')
    WHERE (SELECT COUNT(*) FROM line WHERE journal_id = NEW.id) < 2
       OR (SELECT COALESCE(SUM(cents), 0) FROM line WHERE journal_id = NEW.id) != 0;
END;
CREATE TRIGGER IF NOT EXISTS journal_frozen_update
BEFORE UPDATE ON journal WHEN OLD.state = 'POSTED'
BEGIN
    SELECT RAISE(ABORT, 'posted journal is immutable');
END;
CREATE TRIGGER IF NOT EXISTS journal_frozen_delete
BEFORE DELETE ON journal WHEN OLD.state = 'POSTED'
BEGIN
    SELECT RAISE(ABORT, 'posted journal is immutable');
END;
CREATE TRIGGER IF NOT EXISTS line_insert_guard
BEFORE INSERT ON line
WHEN (SELECT state FROM journal WHERE id = NEW.journal_id) != 'DRAFT'
BEGIN
    SELECT RAISE(ABORT, 'cannot append to posted journal');
END;
CREATE TRIGGER IF NOT EXISTS line_frozen_update
BEFORE UPDATE ON line
BEGIN
    SELECT RAISE(ABORT, 'journal lines are append-only');
END;
CREATE TRIGGER IF NOT EXISTS line_frozen_delete
BEFORE DELETE ON line
BEGIN
    SELECT RAISE(ABORT, 'journal lines are append-only');
END;
"""

def initialize():
    connection = sqlite3.connect(DB, timeout=30, isolation_level=None)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")
        connection.execute("PRAGMA synchronous = FULL")
        connection.executescript("BEGIN IMMEDIATE;\\n" + SCHEMA + "\\nCOMMIT;")
    except BaseException:
        if connection.in_transaction:
            connection.rollback()
        raise
    finally:
        connection.close()
''',
                        "Reject overlapping inventory and unbalanced journals before committing any mutation",
                    ],
                    [
                        "Module 2: score permissioned intake and deduplicate source-event payloads",
                        "Require canonical dates, integer cents, and documented user-triggered demand",
                        '''def intake(event, stay_id, unit_id, starts, ends, authorized_cents,
           deposit_required, triggered, payer_known, duration_known):
    if not triggered:
        raise ValueError("user-initiated trigger required")
    if any(type(value) is not int for value in (authorized_cents, deposit_required)):
        raise ValueError("amounts must be integer cents")
    if authorized_cents <= 0 or deposit_required < 0:
        raise ValueError("invalid commercial amounts")
    if not all(isinstance(value, str) and value for value in (event, stay_id, unit_id)):
        raise ValueError("stable identifiers required")
    start_date = date.fromisoformat(starts)
    end_date = date.fromisoformat(ends)
    if start_date.isoformat() != starts or end_date.isoformat() != ends:
        raise ValueError("canonical ISO dates required")
    days = (end_date - start_date).days
    if not 30 <= days <= 270:
        raise ValueError("route outside target duration to manual review")
    score = 40 + 30 * bool(payer_known) + 30 * bool(duration_known)
    values = {
        "event": event, "stay_id": stay_id, "unit_id": unit_id,
        "starts": starts, "ends": ends, "authorized_cents": authorized_cents,
        "deposit_required": deposit_required, "triggered": bool(triggered),
        "payer_known": bool(payer_known), "duration_known": bool(duration_known)
    }
    digest = fingerprint(values)
    with transaction() as connection:
        old = connection.execute(
            "SELECT id, payload_hash FROM stay WHERE source_event = ?", (event,)
        ).fetchone()
        if old:
            if old["payload_hash"] != digest:
                raise ValueError("source event reused with changed payload")
            return old["id"]
        connection.execute(
            """INSERT INTO stay (
                id, source_event, payload_hash, unit_id, starts, ends,
                authorized_cents, deposit_required, score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (stay_id, event, digest, unit_id, starts, ends,
             authorized_cents, deposit_required, score)
        )
    return stay_id
''',
                        "Reject untriggered dispatch inputs and route duration exceptions for documented review",
                    ],
                    [
                        "Module 3: verify evidence and transition reservation or funds-control states",
                        "Require fresh version, payer evidence, and posted contractual deposit liability",
                        '''def transition(stay_id, expected_version, target, evidence_ref):
    allowed = {
        "DRAFT": {"VERIFIED"},
        "VERIFIED": {"RESERVED", "CANCELLED"},
        "RESERVED": {"ACTIVE", "CANCELLED"},
        "ACTIVE": {"CLOSED"},
        "CLOSED": set(),
        "CANCELLED": set()
    }
    if not isinstance(evidence_ref, str) or not evidence_ref.strip():
        raise ValueError("documented transition evidence required")
    with transaction() as connection:
        stay = connection.execute(
            "SELECT * FROM stay WHERE id = ?", (stay_id,)
        ).fetchone()
        if not stay or stay["version"] != expected_version:
            raise ValueError("missing stay or stale version")
        if target not in allowed[stay["state"]]:
            raise ValueError("invalid state transition")
        payer_ref = stay["payer_ref"]
        if target == "VERIFIED":
            unit = connection.execute(
                "SELECT addendum_ref FROM unit WHERE id = ?", (stay["unit_id"],)
            ).fetchone()
            if not unit or not unit["addendum_ref"]:
                raise ValueError("landlord addendum required")
            payer_ref = evidence_ref
        if target == "RESERVED":
            held = connection.execute(
                """SELECT COALESCE(-SUM(l.cents), 0)
                   FROM journal j JOIN line l ON l.journal_id = j.id
                   WHERE j.state = 'POSTED' AND j.stay_id = ?
                     AND l.account = 'deposit_liability'""", (stay_id,)
            ).fetchone()[0]
            if not payer_ref or held < stay["deposit_required"]:
                raise ValueError("payer authority or cleared deposit missing")
        connection.execute(
            """UPDATE stay SET state = ?, payer_ref = ?, version = version + 1
               WHERE id = ? AND version = ?""",
            (target, payer_ref, stay_id, expected_version)
        )
        key = "stay:" + stay_id + ":" + str(expected_version + 1)
        payload = json.dumps({
            "stay_id": stay_id, "state": target, "evidence_ref": evidence_ref
        }, sort_keys=True)
        connection.execute(
            "INSERT INTO outbox(event_key, payload) VALUES (?, ?)", (key, payload)
        )
    return expected_version + 1
''',
                        "Rollback the entire transition when inventory overlaps or evidence is incomplete",
                    ],
                    [
                        "Module 4: post immutable balanced journals and claim durable outbound intents",
                        "Separate cent-exact accounting identity from uncertain external network delivery",
                        '''def post(event_key, effective_date, entries, stay_id=None):
    date_value = date.fromisoformat(effective_date)
    if date_value.isoformat() != effective_date:
        raise ValueError("canonical posting date required")
    entries = list(entries)
    if len(entries) < 2 or any(type(cents) is not int or cents == 0
                               for account, cents in entries):
        raise ValueError("two or more nonzero integer-cent lines required")
    if sum(cents for account, cents in entries) != 0:
        raise ValueError("entry does not balance")
    deposits = [cents for account, cents in entries if account == "deposit_liability"]
    if deposits:
        accounts = {account for account, cents in entries}
        if not stay_id or len(entries) != 2 or accounts != {"cash", "deposit_liability"}:
            raise ValueError("deposit receipt or refund requires matched cash and stay")
    payload = {
        "effective_date": effective_date, "entries": entries, "stay_id": stay_id
    }
    digest = fingerprint(payload)
    with transaction() as connection:
        old = connection.execute(
            "SELECT id, payload_hash FROM journal WHERE event_key = ?", (event_key,)
        ).fetchone()
        if old:
            if old["payload_hash"] != digest:
                raise ValueError("journal event reused with changed payload")
            return old["id"]
        cursor = connection.execute(
            """INSERT INTO journal(event_key, payload_hash, effective_date, stay_id)
               VALUES (?, ?, ?, ?)""",
            (event_key, digest, effective_date, stay_id)
        )
        journal_id = cursor.lastrowid
        connection.executemany(
            "INSERT INTO line(journal_id, sequence, account, cents) VALUES (?, ?, ?, ?)",
            [(journal_id, index, account, cents)
             for index, (account, cents) in enumerate(entries)]
        )
        connection.execute(
            "UPDATE journal SET state = 'POSTED' WHERE id = ?", (journal_id,)
        )
    return journal_id

def claim_outbox():
    with transaction() as connection:
        row = connection.execute(
            "SELECT event_key, payload FROM outbox WHERE state = 'READY' ORDER BY event_key LIMIT 1"
        ).fetchone()
        if not row:
            return None
        token = secrets.token_hex(24)
        connection.execute(
            "UPDATE outbox SET state = 'CLAIMED', token = ? WHERE event_key = ?",
            (token, row["event_key"])
        )
        return {"event_key": row["event_key"], "payload": row["payload"], "token": token}

def finish_outbox(event_key, token, receipt=None):
    state = "SENT" if receipt else "UNCERTAIN"
    with transaction() as connection:
        cursor = connection.execute(
            """UPDATE outbox SET state = ?, receipt = ?
               WHERE event_key = ? AND token = ? AND state = 'CLAIMED'""",
            (state, receipt, event_key, token)
        )
        if cursor.rowcount != 1:
            raise ValueError("stale claim or previously completed delivery")
''',
                        "Preserve uncertain deliveries for investigation rather than blindly repeating external effects",
                    ],
                    [
                        "Module 5: expose monthly reconciliation view and aggregate balance controls",
                        "Distinguish invoice billings, retained contribution, receivables, and operating cash",
                        '''VIEW_SQL = """
CREATE VIEW IF NOT EXISTS monthly_reconciliation AS
SELECT
    substr(j.effective_date, 1, 7) AS month,
    SUM(CASE WHEN l.account = 'retained_revenue' THEN -l.cents ELSE 0 END)
        AS retained_cents,
    SUM(CASE WHEN l.account = 'opex_expense' THEN l.cents ELSE 0 END)
        AS opex_cents,
    SUM(CASE WHEN l.account = 'cash' THEN l.cents ELSE 0 END)
        AS cash_change_cents,
    SUM(CASE WHEN l.account = 'receivable' THEN l.cents ELSE 0 END)
        AS receivable_change_cents,
    SUM(CASE WHEN l.account = 'retained_revenue' THEN -l.cents
             WHEN l.account = 'opex_expense' THEN -l.cents ELSE 0 END)
        AS profit_cents
FROM journal j JOIN line l ON l.journal_id = j.id
WHERE j.state = 'POSTED'
GROUP BY substr(j.effective_date, 1, 7)
"""

def create_reconciliation_view():
    with transaction() as connection:
        connection.execute(VIEW_SQL)

def balances():
    with transaction() as connection:
        return {
            row["account"]: row["cents"]
            for row in connection.execute(
                """SELECT l.account, SUM(l.cents) AS cents
                   FROM journal j JOIN line l ON l.journal_id = j.id
                   WHERE j.state = 'POSTED' GROUP BY l.account"""
            )
        }

def monthly_report():
    with transaction() as connection:
        return [
            dict(row) for row in connection.execute(
                "SELECT * FROM monthly_reconciliation ORDER BY month"
            )
        ]
''',
                        "Match ledger movements against bank evidence and independently maintained invoice subledgers",
                    ],
                    [
                        "Module 6: run isolated cohort assertions and reservation rejection checks",
                        "Use temporary database without changing live placements or existing operating records",
                        '''def require(condition, message):
    if not condition:
        raise AssertionError(message)

def run_reference_checks():
    import os
    import tempfile

    global DB
    previous_db = DB
    try:
        with tempfile.TemporaryDirectory() as folder:
            DB = os.path.join(folder, "reference.sqlite3")
            initialize()
            create_reconciliation_view()
            months = [
                ("2026-01-31", 4500000, 2475000, 1710000, 3000000),
                ("2026-02-28", 6500000, 3575000, 1710000, 6000000),
                ("2026-03-31", 8750000, 4812500, 1715000, 9000000)
            ]
            for day, gross, vendor, expense, collected in months:
                prefix = "cohort:" + day
                invoice = [
                    ("receivable", gross),
                    ("vendor_payable", -vendor),
                    ("retained_revenue", -(gross - vendor))
                ]
                first = post(prefix + ":invoice", day, invoice)
                require(post(prefix + ":invoice", day, invoice) == first,
                        "replay created another journal")
                post(prefix + ":receipt", day,
                     [("cash", collected), ("receivable", -collected)])
                post(prefix + ":vendor", day,
                     [("vendor_payable", vendor), ("cash", -vendor)])
                post(prefix + ":opex", day,
                     [("opex_expense", expense), ("cash", -expense)])
            totals = balances()
            require(totals["cash"] == 2002500, "cash bridge failed")
            require(totals["receivable"] == 1750000, "receivable bridge failed")
            require(totals["vendor_payable"] == 0, "unsettled landlord costs")
            require(sum(totals.values()) == 0, "trial balance failed")
            require(-totals["retained_revenue"] - totals["opex_expense"] == 3752500,
                    "owner profit bridge failed")
            report = monthly_report()
            require([row["profit_cents"] for row in report] ==
                    [315000, 1215000, 2222500], "monthly profit failed")
            try:
                post("cohort:2026-01-31:invoice", "2026-01-31",
                     [("receivable", 1), ("retained_revenue", -1)])
            except ValueError:
                pass
            else:
                raise AssertionError("changed replay was accepted")
            with transaction() as connection:
                connection.execute(
                    "INSERT INTO unit(id, addendum_ref) VALUES (?, ?)",
                    ("unit-a", "documents/landlord-addendum-a")
                )
            for suffix in ("a", "b"):
                stay_id = "stay-" + suffix
                intake("trigger-" + suffix, stay_id, "unit-a",
                       "2026-04-01", "2026-05-01", 450000, 0, True, True, True)
                transition(stay_id, 0, "VERIFIED", "documents/payer-" + suffix)
            transition("stay-a", 1, "RESERVED", "documents/reservation-a")
            try:
                transition("stay-b", 1, "RESERVED", "documents/reservation-b")
            except sqlite3.IntegrityError:
                pass
            else:
                raise AssertionError("overlapping reservation was accepted")
            with transaction() as connection:
                drafts = connection.execute(
                    "SELECT COUNT(*) FROM journal WHERE state != 'POSTED'"
                ).fetchone()[0]
                require(drafts == 0, "abandoned draft journal found")
                require(connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
                        "database integrity check failed")
                require(not connection.execute("PRAGMA foreign_key_check").fetchall(),
                        "foreign key check failed")
            return report
    finally:
        DB = previous_db

if __name__ == "__main__":
    for result in run_reference_checks():
        print(result)
''',
                        "Run additional contention and crash tests before connecting real provider adapters",
                    ],
                ],
            },
        },
        {
            "heading": "3. Operate possession, extensions, exceptions, and daily cash controls",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Once inventory is reserved, build a possession packet rather than a loose "
                    "collection of messages. Include the executed occupancy agreement, landlord "
                    "authorization, payer instruction, arrival contact, appliance instructions, "
                    "emergency maintenance route, inspection photographs, and furnishing inventory. "
                    "Verify the smart lock locally before activating the household's access "
                    "window; a successful API response is insufficient evidence that the door "
                    "opens. Schlage or Yale hardware can support access operations, while "
                    "Minut-style noise monitoring and leak sensors can surface maintenance "
                    "exceptions. Configure monitoring for the disclosed operational purpose; "
                    "avoid recording conversations or collecting unnecessary household details. "
                    "A leak alert should create a maintenance ticket with acknowledgement "
                    "and escalation times, not automatically accuse an occupant of damage. "
                    "Route electrical, plumbing, and habitability emergencies to qualified "
                    "contractors and maintain a relocation alternative when a unit becomes "
                    "unusable. New York Real Property Law section 235-b provides a concrete "
                    "habitability reference where applicable; contracts cannot make unsafe "
                    "housing operationally acceptable. The Base team remains one full-time "
                    "operator and three contractors, with cleaning, field maintenance, and "
                    "bookkeeping assignments explicitly covered. Contractor availability must "
                    "be purchased and budgeted, not assumed to appear free whenever the "
                    "operator's phone receives an alert."
                ),
                (
                    "Run extension control against three calendars: payer authority, landlord "
                    "commitment, and actual household possession. Start the extension inquiry "
                    "seven days before current authority expires and request a written "
                    "decision with revised dates and rate. If authority expires first, "
                    "stop creating unsupported payer charges and resolve responsibility "
                    "with the contracting parties. If the landlord term expires first, "
                    "secure an authorized extension or arrange replacement housing. Never "
                    "solve a commercial discrepancy by disabling access for an occupied "
                    "household. Early claim closeout is a separate exposure: the insurer "
                    "may end authorization while the operator still owes fixed rent. "
                    "At a $175 daily billing rate and the illustrative 55% property-cost "
                    "allocation, a ten-day unrecovered tail represents $962.50 of property "
                    "cost before operating expense. Actual master-lease rent remains fixed "
                    "according to contract, so that allocation is a planning proxy rather "
                    "than a cancellation clause. Negotiate notice periods and release "
                    "fees, then maintain a replacement-demand queue that respects existing "
                    "occupancy rights. Utility-cap invoices require the contract threshold, "
                    "service period, meter or supplier evidence, and payer responsibility. "
                    "Disputed damage, utility excess, and authorized housing charges should "
                    "have separate invoice lines and collections tracks so one contested "
                    "charge does not obscure the entire placement balance."
                ),
                (
                    "Close each operating day with an exception queue, not a dashboard "
                    "screenshot. Match portal acknowledgements to submitted invoices, bank "
                    "receipts to remittance references, and landlord payments to approved "
                    "cost schedules. A portal's accepted status is not cash settlement. "
                    "Keep receipt dates, invoice dates, and service dates as separate "
                    "fields in the production application; the compact reference uses "
                    "effective posting dates and monthly control totals. Those totals "
                    "must be supported by invoice-level records before live use. Separate "
                    "refundable deposits, collected occupancy taxes, and restricted funds "
                    "from operating income. The worked cohort excludes occupancy taxes "
                    "and customer deposits, assumes eligible documented treatment where "
                    "necessary, and pays all modeled property costs and operating expenses "
                    "during the quarter. The scorecard's 45% retained-share presentation "
                    "is an analytical convention, not a universal ASC 606 conclusion. "
                    "Assess principal-versus-agent treatment from control of the promised "
                    "service and the actual contracts. If the operator is principal, "
                    "report gross revenue and property expense while preserving the "
                    "same contribution bridge; if agent, the reference's net presentation "
                    "may fit the approved accounting policy. In either case, underlying "
                    "housing billings, retained contribution, owner profit, and bank "
                    "cash remain four distinct measures with separate reconciliation evidence."
                ),
            ],
            "table": {
                "caption": "Daily Production Controls: Possession, Exceptions, and Cash Evidence",
                "headers": [
                    "Operating control and accountable execution owner",
                    "Required record before the control is complete",
                    "Measured threshold or exact accounting treatment",
                    "Escalation preserving service continuity and ledger integrity",
                ],
                "rows": [
                    [
                        "Arrival readiness: field contractor verifies the actual property",
                        "Tested entry method, dated inspection photographs, and delivered furnishing inventory",
                        "Complete one documented readiness inspection before each household takes possession",
                        "Arrange attended access or equivalent replacement housing when readiness fails",
                    ],
                    [
                        "Property telemetry: maintenance contractor acknowledges disclosed operational alerts",
                        "Retain sensor event, contractor acknowledgement, response action, and resolution photograph",
                        "Triage active leaks immediately using the documented emergency contact ladder",
                        "Dispatch qualified maintenance rather than treating sensor readings as occupant fault",
                    ],
                    [
                        "Extension control: operator reconciles three independent contractual calendars",
                        "Preserve revised payer dates and landlord extension evidence before additional reservation",
                        "Ten authorized extra nights at $175 generate $1,750 additional billings",
                        "Resolve uncovered dates without automatically charging an unauthorized payer account",
                    ],
                    [
                        "Early closeout exposure: operator compares remaining rent against collectible charges",
                        "Keep payer termination notice and landlord release calculation with placement record",
                        "Ten days at $96.25 allocated property cost expose $962.50",
                        "Negotiate release or replacement demand while honoring lawful possession requirements",
                    ],
                    [
                        "Invoice and bank matching: bookkeeper maintains separate settlement evidence",
                        "Match placement reference, invoice number, portal receipt, remittance, and bank entry",
                        "Month 3 closing receivables equal $17,500 after $90,000 collections",
                        "Investigate payer allocation differences before marking invoices fully paid",
                    ],
                    [
                        "Deposit and tax segregation: operator applies jurisdiction-specific accounting instructions",
                        "Document restricted balances, applicable tax treatment, and refundable deposit obligations",
                        "Exclude refundable liabilities and collected taxes from retained operating contribution",
                        "Use required custodial accounts and resolve classification exceptions before distribution",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before committing a household",
                "body": "The operator records these verification outcomes before inventory commitment; a software state label does not substitute for underlying evidence.",
                "items": [
                    "Verify the landlord's signed addendum covers corporate housing, occupant substitution, insurance obligations, and the proposed term.",
                    "Verify the payer's authorized dates, rate ceiling, invoicing instructions, cancellation exposure, and extension decision owner.",
                    "Verify property condition, functioning access, emergency contacts, required accommodation handling, and applicable occupancy-tax evidence.",
                    "Verify available working capital, deposit-liability treatment, inventory availability, and a tested reversal path for any posting error.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the verified placement file",
                    "action": "Deduplicate the initiating event and attach payer and property evidence.",
                    "detail": "Record authorized dates and rate, landlord addendum, household requirements, document references, and the accountable operator before moving from draft.",
                },
                {
                    "step": 2,
                    "title": "Reserve inventory and deliver possession",
                    "action": "Commit the serialized reservation and complete the inspected arrival handoff.",
                    "detail": "Check contractual deposit funding, reject date overlaps, verify actual lock operation, and retain the occupant handoff receipt.",
                },
                {
                    "step": 3,
                    "title": "Control service and extensions",
                    "action": "Review alerts and reconcile payer, landlord, and possession calendars daily.",
                    "detail": "Obtain fresh written extension authority, document utility-cap calculations, and escalate uncovered dates without disrupting lawful access.",
                },
                {
                    "step": 4,
                    "title": "Reconcile cash and close the placement",
                    "action": "Match service invoices, supplier costs, bank settlements, and departure evidence.",
                    "detail": "Post reversals for corrections, retain unresolved receivables separately, refund deposits under applicable rules, and archive the complete evidence chain.",
                },
            ],
        },
        {
            "heading": "4. Walk the 90-day cohort from hand-raisers to reconciled owner cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Treat the walkthrough as a modeled quarter, not an assertion that a "
                    "new operator instantly reaches the annual average. Month 1 signs "
                    "cohort A with ten placements and bills three hundred occupied days "
                    "at $150, producing $45,000. Month 2 signs cohort B with eight "
                    "placements; cohort A contributes two hundred forty billed days "
                    "and B contributes one hundred sixty, all at the illustrative "
                    "$162.50 monthly blended rate, producing $65,000. Month 3 signs "
                    "cohort C with ten placements; A contributes one hundred days, "
                    "B one hundred eighty, and C two hundred twenty, at a $175 "
                    "blended rate, producing $87,500. These blended rates describe "
                    "the monthly invoice mix, not unilateral repricing of existing "
                    "agreements. Contracted extensions or different underlying placements "
                    "must support every rate. Billed days can be partial-month "
                    "occupancy within a longer authorized stay; they do not establish "
                    "a separate short-stay product. Month 3 throughput exceeds the "
                    "annual average, so repeating Month 3 four times would overstate "
                    "the Base case. Annualize the entire quarter instead. The result "
                    "is $197,500 multiplied by four, exactly $790,000 gross billings, "
                    "with seasonality and subsequent vacancy absorbed only within "
                    "the stated full-quarter operating assumptions."
                ),
                (
                    "Apply the scorecard bridge before considering distributions. Property "
                    "rent and utility pass-throughs consume 55% of gross billings: "
                    "$24,750 in Month 1, $35,750 in Month 2, and $48,125 "
                    "in Month 3. Retained contribution is therefore $20,250, "
                    "$29,250, and $39,375. Operating expense is $17,100, "
                    "$17,100, and $17,150, leaving monthly owner profit of "
                    "$3,150, $12,150, and $22,225. Quarterly totals are "
                    "$108,625 pass-throughs, $88,875 retained contribution, "
                    "$51,350 operating expense, and $37,525 profit. Four "
                    "quarters produce $355,500 retained revenue, $205,400 "
                    "operating expense, and exactly $150,100 annual owner "
                    "profit. The annual gross-basis margin is 19.0%; the "
                    "retained-basis margin rounds to 42.22%. Monthly operating "
                    "expense stays within the supplied $3,000 to $18,000 "
                    "range. For specificity, each first-two-month expense "
                    "budget comprises $9,000 staffing and contractor work, "
                    "$2,100 turnover and supplies, $1,000 software and "
                    "connectivity, $1,000 insurance and accounting, $1,500 "
                    "demand generation, and $2,500 maintenance and operations. "
                    "Month 3 adds $50 to operations. This is an illustrative "
                    "expense allocation, not extra owner compensation layered "
                    "onto the canonical profit. Financing charges or entity-level "
                    "taxes added by a real business require an explicit "
                    "reforecast rather than silent removal from the ledger."
                ),
                (
                    "Collections arrive later than earnings. Month 1 collects "
                    "$30,000 against $45,000 billed; Month 2 collects the "
                    "remaining $15,000 plus $45,000 of current invoices; "
                    "Month 3 collects the prior $20,000 plus $70,000 "
                    "of current invoices. Quarter-end receivables are $17,500. "
                    "Paying modeled property costs and operating expenses "
                    "currently produces monthly operating cash changes of "
                    "negative $11,850, positive $7,150, and positive "
                    "$24,725. Cumulative operating cash is negative $11,850, "
                    "negative $4,700, then positive $20,025. Add the "
                    "$17,500 receivable increase to cash generation and "
                    "the bridge returns exactly $37,525 profit. An "
                    "illustrative $40,000 unrestricted opening cash balance "
                    "ends at $60,025 before distributions; already-purchased "
                    "furnishings, landlord deposits, and setup costs must "
                    "be budgeted separately within the actual startup plan. "
                    "The table's six, eight, and ten quote-stage scrubs "
                    "produce zero recognized losses because rejected "
                    "opportunities never became receivables. The cohort "
                    "assumes zero post-booking credit losses; that assumption "
                    "must remain visible. A $5,000 quarterly write-off "
                    "would reduce annualized owner profit by $20,000 "
                    "without reducing landlord commitments. Review aging "
                    "weekly and retain liquidity until disputed invoices "
                    "and upcoming rent are covered. Profitable paper "
                    "does not fund the next landlord payment."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort measure and explicit modeling treatment",
                    "Month 1: cohort A enters production",
                    "Month 2: cohort B joins continuing placements",
                    "Month 3: cohort C completes quarterly bridge",
                ],
                "rows": [
                    [
                        "Permissioned lead funnel before any property commitment",
                        "60 hand-raisers; 36 qualified conversations; 20 quoted opportunities",
                        "80 hand-raisers; 48 qualified conversations; 26 quoted opportunities",
                        "100 hand-raisers; 60 qualified conversations; 32 quoted opportunities",
                    ],
                    [
                        "Verification scrubs and signed placement conversion by originating cohort",
                        "14 verified; six scrubbed; ten signed; four verified remain unsigned",
                        "18 verified; eight scrubbed; eight signed; ten verified remain unsigned",
                        "22 verified; ten scrubbed; ten signed; twelve verified remain unsigned",
                    ],
                    [
                        "Occupied day attribution with supported blended invoice rates",
                        "Cohort A supplies 300 days at $150 blended daily billing",
                        "A supplies 240 days; B supplies 160; blended rate $162.50",
                        "A supplies 100 days; B 180; C 220; rate $175",
                    ],
                    [
                        "Gross billing and fifty-five percent property-cost allocation",
                        "$45,000 billed; $24,750 landlord and utility pass-through costs",
                        "$65,000 billed; $35,750 landlord and utility pass-through costs",
                        "$87,500 billed; $48,125 landlord and utility pass-through costs",
                    ],
                    [
                        "Retained contribution less operating expense equals owner profit",
                        "$20,250 retained less $17,100 operating expense equals $3,150 profit",
                        "$29,250 retained less $17,100 operating expense equals $12,150 profit",
                        "$39,375 retained less $17,150 operating expense equals $22,225 profit",
                    ],
                    [
                        "Collection allocation and resulting closing accounts receivable balance",
                        "Collect $30,000 current invoices; closing receivables total $15,000",
                        "Collect $15,000 prior plus $45,000 current; receivables total $20,000",
                        "Collect $20,000 prior plus $70,000 current; receivables total $17,500",
                    ],
                    [
                        "Current cash outlays and cumulative operating cash generation",
                        "Pay $41,850; monthly cash negative $11,850; cumulative negative $11,850",
                        "Pay $52,850; monthly cash positive $7,150; cumulative negative $4,700",
                        "Pay $65,275; monthly cash positive $24,725; cumulative positive $20,025",
                    ],
                    [
                        "Unrestricted liquidity from illustrative $40,000 opening operating cash",
                        "Closing cash $28,150 before distributions and separately funded setup costs",
                        "Closing cash $35,300 before distributions and separately funded setup costs",
                        "Closing cash $60,025; $17,500 receivables explain earnings above cash",
                    ],
                    [
                        "Post-booking credit losses and clean Base-case annualization boundary",
                        "Zero realized credit losses; rejected quotes never enter receivables",
                        "Zero realized credit losses; collections clear all prior-month invoices",
                        "Quarter profit $37,525 times four equals $150,100 annual owner profit",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Reserve only what you can lawfully deliver, bill only what is authorized, and distribute only what has survived reconciliation.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one placement identifier linking the initiating trigger, payer authority, landlord addendum, occupancy agreement, portal submission, invoice, and bank receipt.",
        "Copy the six engineering source cells into one reference file, run the isolated checks, and add simultaneous-writer and interrupted-worker tests before live integration.",
        "Document jurisdiction-specific subletting, habitability, occupancy-tax, deposit, and insurance requirements for every property before advertising availability.",
        "Configure permissioned comment-to-DM routing with event deduplication, prospect-reply link controls, and manual handling of uncertain external deliveries.",
        "Implement the seven-day extension review and daily three-calendar comparison covering payer authority, landlord commitment, and actual possession.",
        "Reproduce the $197,500 quarterly billing bridge, $37,525 owner profit, $20,025 operating cash, and $17,500 closing receivables before considering distributions.",
    ],
    "statutory_citations": [
        {
            "title": "New York Real Property Law section 226-b — Right to sublease or assign",
            "url": "https://www.nysenate.gov/legislation/laws/RPP/226-B",
            "relevance": "Evaluate the statute's applicable residential subletting framework and exceptions; obtain explicit written corporate-housing authorization for each property rather than assuming a standard lease permits the operating model.",
        },
        {
            "title": "New York Real Property Law section 235-b — Warranty of habitability",
            "url": "https://www.nysenate.gov/legislation/laws/RPP/235-B",
            "relevance": "Where applicable, use the statutory habitability obligation to inform property inspection, emergency maintenance, condition documentation, and replacement-housing procedures.",
        },
        {
            "title": "Texas Tax Code section 156.101 — Exception for permanent residents",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.156.htm#156.101",
            "relevance": "Assess the state hotel-occupancy-tax permanent-resident exception and its thirty-consecutive-day requirement; retain supporting occupancy records and evaluate local taxes separately.",
        },
        {
            "title": "42 U.S.C. 3604 — Discrimination in the sale or rental of housing",
            "url": "https://www.law.cornell.edu/uscode/text/42/3604",
            "relevance": "Design qualification, placement, and household-requirement procedures around lawful commercial criteria and applicable fair-housing protections rather than protected characteristics.",
        },
        {
            "title": "24 CFR 100.204 — Reasonable accommodations",
            "url": "https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/subchapter-A/part-100/subpart-D/section-100.204",
            "relevance": "Maintain an operational process for reasonable accommodation requests affecting housing rules, policies, practices, or services where the regulation applies.",
        },
    ],
}
