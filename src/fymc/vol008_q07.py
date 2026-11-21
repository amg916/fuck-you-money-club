from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "commercial-lead-generation-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute commercial lead generation end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Permissioned Outbound, Qualified-Call Routing, SQLite Event Controls, CAN-SPAM Duties, and a Cash-Reconciled Five-Client Cohort",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #18, Commercial Lead Generation, ranks #08 with an 85/100 "
        "Money-to-Manpower Score across 54 mapped plays. The operating advantage "
        "comes from proving lead acceptance, controlling delivery costs, and collecting "
        "contracted fees without treating client advertising spend as revenue. This "
        "chapter connects intake, permission checks, multi-inbox delivery, call routing, "
        "verification, billing, and cash through a six-module SQLite reference. A "
        "five-client, 90-day cohort earns $106,250, incurs $74,375 of operating costs, "
        "and produces $31,875 of owner profit, exactly one quarter of the Base case. "
        "Annual owner profit remains $20,000 Conservative, $127,500 Base, and "
        "$300,000 Scaled. Specialist plays receive explicit boundaries separating "
        "ordinary marketing fees from licensed legal operations, property transactions, "
        "and platform participation."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retainers and accepted-lead fees; client advertising excluded",
            "note": "20% net margin; $20,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual retainers and accepted-lead fees; client advertising excluded",
            "note": "30.0% net margin; $127,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$750,000",
            "context": "Annual retainers and accepted-lead fees; client advertising excluded",
            "note": "40% net margin; $300,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Contract the acceptance unit before connecting acquisition channels",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a signed service schedule defining territory, buyer role, "
                    "commercial need, exclusions, duplicate window, evidence standard, "
                    "acceptance deadline, and dispute owner. A qualified appointment is "
                    "not interchangeable with an answered call: specify whether attendance, "
                    "decision authority, or a documented buying project creates the fee. "
                    "For this chapter, five clients each purchase a $5,000 monthly service "
                    "retainer plus $250 per finally accepted lead. The retainer covers "
                    "campaign operations, reporting, and routing maintenance; the variable "
                    "fee covers a separately evidenced delivery unit. Client-funded media "
                    "stays outside recognized operator revenue and preferably remains in "
                    "client-owned advertising accounts. Record authorization to use each "
                    "domain, inbox, telephone number, CRM workspace, and destination "
                    "calendar before production access. In HubSpot or Salesforce, require "
                    "a client identifier, source event identifier, service period, "
                    "qualification fields, and evidence pointer. Store sensitive source "
                    "material in a restricted evidence repository rather than free-text "
                    "CRM notes. Assign one full-time owner to acceptance disputes and "
                    "three contractors to research, delivery operations, and quality "
                    "review. This allocation matches the Base staffing envelope without "
                    "assuming that contractor availability equals three additional "
                    "full-time employees. Establish named backups before the first "
                    "campaign creates a customer response."
                ),
                (
                    "Build the acquisition lane around actual authorization, not around "
                    "mailbox quantity. Configure SPF, DKIM, and DMARC for clearly "
                    "identified sending domains using Google Workspace or Microsoft 365; "
                    "separate client credentials and publish working reply addresses. "
                    "Multiple inboxes provide operational segregation and capacity "
                    "management, never a method for bypassing provider limits or "
                    "recipient suppression. Under 15 U.S.C. § 7704, commercial email "
                    "requires accurate transmission information, nondeceptive subjects, "
                    "applicable advertising identification, a valid postal address, and "
                    "a functioning opt-out mechanism. Process opt-outs immediately in "
                    "operations even though the federal deadline generally permits "
                    "ten business days. Preserve suppression across every campaign "
                    "acting for the same sender. Telephone and text permissions require "
                    "a separate analysis under 47 U.S.C. § 227 and 47 CFR § 64.1200; "
                    "a business job title does not establish that a number is exempt "
                    "from restrictions affecting wireless or residential recipients. "
                    "Check state calling and recording requirements before enabling "
                    "dialing or call recording. Use CallRail or Twilio routing logs "
                    "to prove delivery without assuming a recording is always available. "
                    "When permission evidence is incomplete, stop that channel and "
                    "offer a verified inbound form or explicitly requested callback instead."
                ),
                (
                    "Run intake through a deterministic funnel: normalize the source, "
                    "deduplicate within the contracted window, score explicit facts, "
                    "route eligible work, and hold the proposed fee until verification "
                    "finishes. Normalize telephone numbers with country context and "
                    "preserve original values in the restricted evidence store. For "
                    "email identity, avoid aggressive transformations that could merge "
                    "distinct recipients. Create a client-scoped HMAC fingerprint so "
                    "the ledger can detect repeats without storing contact details. "
                    "A high score only prioritizes review; it does not establish "
                    "permission, truthfulness, legal eligibility, or client acceptance. "
                    "Route calls against staffed schedules, fail over to a named "
                    "backup, and return unattended calls to a follow-up queue rather "
                    "than marking them qualified. Require a reason code for wrong "
                    "territory, duplicate contact, absent buying need, unreachable "
                    "prospect, and client-side missed appointment. Weekly reviews should "
                    "separate acquisition defects from recipient staffing failures "
                    "because the remedies differ. Suspend a source when its accepted "
                    "cost exceeds the contracted contribution allowance, even if raw "
                    "lead volume looks attractive. Deliver the client a compact evidence "
                    "packet containing timestamps, qualification answers, routing outcome, "
                    "and the acceptance decision. Only then create the variable "
                    "receivable and its durable billing event."
                ),
            ],
            "table": {
                "caption": "Contract-to-Cash Operating Matrix for Permissioned Commercial Lead Delivery",
                "headers": [
                    "Operating stage and accountable owner",
                    "Required evidence and named operating tools",
                    "Release condition and measurable operating rule",
                    "Failure treatment and retained audit record",
                ],
                "rows": [
                    [
                        "Client onboarding owned by the full-time operator",
                        "Signed territory schedule, fee definitions, and authorized HubSpot workspace",
                        "Five qualification fields and duplicate period agreed before acquisition",
                        "Unresolved definitions block delivery rather than creating disputed receivables",
                    ],
                    [
                        "Research intake owned by the assigned sourcing contractor",
                        "Source URL, collection timestamp, permission basis, and restricted evidence pointer",
                        "Client-scoped contact fingerprint passes the contracted duplicate-window test",
                        "Repeated identities receive a scrub reason and no second fee",
                    ],
                    [
                        "Outbound delivery owned by the campaign operations contractor",
                        "Google Workspace authentication reports and sender-wide suppression records",
                        "Identified sender, working unsubscribe path, and permitted channel established",
                        "Provider warnings pause affected campaigns instead of triggering inbox rotation",
                    ],
                    [
                        "Appointment routing owned by the scheduled recipient coordinator",
                        "CallRail destination logs, staffed calendar, and documented overflow contact",
                        "Commercial need and territory match before the appointment is transferred",
                        "Unanswered routing returns to follow-up without automatic acceptance billing",
                    ],
                    [
                        "Quality verification owned by an independent review contractor",
                        "Timestamped qualification answers and client acknowledgement of the delivery unit",
                        "Acceptance decision references evidence and the applicable contract version",
                        "Wrong-fit or disputed leads remain unbilled until review resolves",
                    ],
                    [
                        "Cash reconciliation owned by the full-time operating principal",
                        "Immutable billing key, bank receipt reference, and monthly receivables view",
                        "Collected cash matches allocated invoices without duplicate receipt posting",
                        "Unmatched receipts remain outside allocation pending documented bank investigation",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before the first production delivery",
                "body": (
                    "Complete these checks for each client and channel; a successful "
                    "test for one client does not authorize another client's campaign."
                ),
                "items": [
                    "Replay one opt-out through every sender workspace and confirm the contact cannot re-enter a scheduled sequence.",
                    "Place a permitted test call during staffed and unstaffed hours; verify destination, overflow, timestamp, and recording configuration.",
                    "Have the client classify ten sample records against the signed acceptance definition before activating variable fees.",
                    "Submit the same intake and payment identifiers concurrently; confirm one delivery obligation and one allocated receipt survive.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Bind the commercial unit",
                    "action": "Sign the service schedule and register an immutable client fee configuration.",
                    "detail": "Document duplicate windows, evidence requirements, territory, channel permissions, dispute ownership, and separate client-funded advertising.",
                },
                {
                    "step": 2,
                    "title": "Qualify and route authorized demand",
                    "action": "Normalize identities, check suppression, score explicit facts, and route only within staffed capacity.",
                    "detail": "Use stable source identifiers and retain restricted evidence outside the ledger; a score alone never authorizes contact.",
                },
                {
                    "step": 3,
                    "title": "Resolve the verification hold",
                    "action": "Record acceptance or rejection through the transactional state transition.",
                    "detail": "Accepted leads receive one immutable obligation; rejected leads receive no fee and retain a scrub reason in the evidence packet.",
                },
                {
                    "step": 4,
                    "title": "Close invoices and reconcile receipts",
                    "action": "Dispatch durable billing events and allocate bank-confirmed receipts with unique identifiers.",
                    "detail": "Compare earned revenue, delivery costs, cash collections, and open receivables before approving the next month's capacity.",
                },
            ],
        },
        {
            "heading": "2. Implement six atomic ledger modules with explicit external-system boundaries",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference below uses integer cents, SQLite foreign keys, "
                    "business-key uniqueness, and BEGIN IMMEDIATE transactions. Save "
                    "the SQL blocks as schema.sql and views.sql, concatenate modules "
                    "two through four in order into ledger.py, and save module six "
                    "as qa.py in the same directory. Run python qa.py against a "
                    "local filesystem with SQLite supporting window functions, version "
                    "3.25 or later. These are reference artifacts supplied as text; "
                    "their tests have not been executed here. Deploy one authoritative "
                    "database per operating ledger and prohibit direct application "
                    "writes outside these functions. Transactions serialize the "
                    "read-check-write sequences that otherwise allow duplicate "
                    "acceptance, conflicting retries, or concurrent overcollection. "
                    "A busy timeout fails the request rather than weakening a "
                    "constraint; retry the identical operation identifier after "
                    "backoff. Do not place the database on a shared network drive "
                    "or create independently writable replicas. Use managed Postgres "
                    "with equivalent unique constraints and row locking when multiple "
                    "application hosts need write access. Back up the database through "
                    "SQLite's backup interface and test restoration alongside the "
                    "separately protected evidence repository. A ledger backup without "
                    "its evidence index cannot substantiate the billable delivery unit."
                ),
                (
                    "Module two records four explicit qualification facts and an "
                    "evidence digest; the caller must already have completed channel "
                    "authorization and suppression checks. Module three implements "
                    "held, accepted, and rejected states. Here, verification escrow "
                    "means a noncash operational hold on a proposed fee, not custody "
                    "of client money or a regulated escrow account. Only a perfect "
                    "qualification score can proceed to acceptance, and a human "
                    "reviewer must still authorize that transition. Acceptance writes "
                    "the lead state, receivable, and outbox event in one transaction. "
                    "A retry returns the same obligation, while an attempted terminal "
                    "state reversal raises an exception. Retainers are recognized "
                    "when the month's contracted service is completed, not merely "
                    "because an invoice was sent. The worked cohort has no deposits, "
                    "post-acceptance credits, refunds, tax collections, or foreign "
                    "currency transactions. Route those transaction classes to an "
                    "accounting system with explicit liability and adjustment entries "
                    "rather than changing historical obligations here. Keep pre-acceptance "
                    "scrubs separate from credit notes: the former never become "
                    "revenue. This distinction prevents rejected prospects from "
                    "inflating both reported sales and apparent collection losses "
                    "when the operator explains performance to the client."
                ),
                (
                    "Module four deliberately performs remote delivery outside the "
                    "database transaction. Its sender callback must target an API "
                    "that atomically deduplicates the supplied stable key and returns "
                    "the same durable receipt for every replay. The key must remain "
                    "valid throughout the retry horizon; a provider's short retention "
                    "window is insufficient for indefinite unattended retries. Two "
                    "workers may transmit the same outbox item, but that provider "
                    "contract produces one external invoice and the local acknowledgement "
                    "records one receipt. If the destination lacks this property, "
                    "stop automatic replay after an ambiguous timeout and retrieve "
                    "the external result before proceeding. No local SQL transaction "
                    "can independently promise exactly-once behavior at an unrelated "
                    "service. Receipt allocation uses a separate bank-origin identifier "
                    "and rejects conflicting reuse or amounts exceeding the remaining "
                    "receivable. The reconciliation view reports earned revenue, "
                    "recorded costs, collections, operating cash movement, and "
                    "receivables by service month. Module six builds the entire "
                    "cohort, exercises concurrent acceptance and receipt retries, "
                    "and checks the expected totals. Add integration tests for the "
                    "chosen provider, restricted evidence store, access controls, "
                    "and restore process before using these functions with live "
                    "client records."
                ),
            ],
            "table": {
                "caption": "Six-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and copy destination",
                    "Executable reference source",
                    "Transactional control and operator responsibility",
                ],
                "rows": [
                    [
                        "Module one: save this complete database definition as schema.sql",
                        r'''PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

CREATE TABLE contracts (
    id TEXT PRIMARY KEY NOT NULL,
    retainer_cents INTEGER NOT NULL CHECK (retainer_cents > 0),
    lead_fee_cents INTEGER NOT NULL CHECK (lead_fee_cents > 0)
);

CREATE TABLE leads (
    id INTEGER PRIMARY KEY,
    contract_id TEXT NOT NULL REFERENCES contracts(id),
    cycle TEXT NOT NULL,
    source_key TEXT NOT NULL,
    contact_key TEXT NOT NULL,
    evidence_digest TEXT NOT NULL CHECK (length(evidence_digest) = 64),
    score INTEGER NOT NULL CHECK (score IN (0, 25, 50, 75, 100)),
    state TEXT NOT NULL DEFAULT 'held'
        CHECK (state IN ('held', 'accepted', 'rejected')),
    UNIQUE (contract_id, source_key),
    UNIQUE (contract_id, cycle, contact_key)
);

CREATE TABLE obligations (
    id TEXT PRIMARY KEY NOT NULL,
    contract_id TEXT NOT NULL REFERENCES contracts(id),
    cycle TEXT NOT NULL,
    kind TEXT NOT NULL CHECK (kind IN ('retainer', 'lead')),
    lead_id INTEGER UNIQUE REFERENCES leads(id),
    amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
    CHECK (
        (kind = 'retainer' AND lead_id IS NULL) OR
        (kind = 'lead' AND lead_id IS NOT NULL)
    )
);

CREATE UNIQUE INDEX one_retainer_per_cycle
ON obligations(contract_id, cycle)
WHERE kind = 'retainer';

CREATE TABLE outbox (
    event_key TEXT PRIMARY KEY NOT NULL REFERENCES obligations(id),
    payload TEXT NOT NULL,
    remote_receipt TEXT UNIQUE
);

CREATE TABLE receipts (
    receipt_key TEXT PRIMARY KEY NOT NULL,
    obligation_id TEXT NOT NULL REFERENCES obligations(id),
    cash_cycle TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK (amount_cents > 0)
);

CREATE TABLE costs (
    cycle TEXT PRIMARY KEY NOT NULL,
    amount_cents INTEGER NOT NULL CHECK (amount_cents > 0)
);

CREATE INDEX receipts_by_obligation
ON receipts(obligation_id);
''',
                        (
                            "Unique business keys prevent duplicate delivery units and "
                            "monthly retainers; initialize once before concurrent writers start."
                        ),
                    ],
                    [
                        "Module two: begin ledger.py with intake and scoring functions",
                        r'''from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime


@contextmanager
def transaction(db):
    connection = sqlite3.connect(db, timeout=30, isolation_level=None)
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        connection.execute("BEGIN IMMEDIATE")
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()


def period(value):
    if not isinstance(value, str):
        raise ValueError("Service period must be text")
    parsed = datetime.strptime(value, "%Y-%m")
    if parsed.strftime("%Y-%m") != value:
        raise ValueError("Use a zero-padded service period")
    return value


def positive_cents(value):
    if type(value) is not int or value <= 0:
        raise ValueError("Amount must be positive integer cents")
    return value


def text_key(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Identifier must contain meaningful text")
    return value


def register_contract(db, contract_id, retainer_cents, lead_fee_cents):
    values = (
        text_key(contract_id),
        positive_cents(retainer_cents),
        positive_cents(lead_fee_cents),
    )
    with transaction(db) as connection:
        connection.execute(
            "INSERT INTO contracts VALUES (?, ?, ?) "
            "ON CONFLICT(id) DO NOTHING",
            values,
        )
        stored = connection.execute(
            "SELECT id, retainer_cents, lead_fee_cents "
            "FROM contracts WHERE id = ?",
            (contract_id,),
        ).fetchone()
        if stored != values:
            raise ValueError("Contract identifier reused with different terms")


def intake(db, contract_id, cycle, source_key, contact_key, facts, digest):
    text_key(contract_id)
    period(cycle)
    text_key(source_key)
    text_key(contact_key)
    if len(facts) != 4 or any(type(item) is not bool for item in facts):
        raise ValueError("Provide four explicit Boolean qualification facts")
    if (
        not isinstance(digest, str)
        or len(digest) != 64
        or any(char not in "0123456789abcdef" for char in digest)
    ):
        raise ValueError("Evidence digest must be lowercase SHA-256 hex")
    score = sum(facts) * 25
    expected = (cycle, source_key, contact_key, digest, score)
    with transaction(db) as connection:
        existing = connection.execute(
            "SELECT id, cycle, source_key, contact_key, evidence_digest, score "
            "FROM leads WHERE contract_id = ? "
            "AND (source_key = ? OR (cycle = ? AND contact_key = ?))",
            (contract_id, source_key, cycle, contact_key),
        ).fetchall()
        if existing:
            if len(existing) != 1 or existing[0][1:] != expected:
                raise ValueError("Duplicate identity or conflicting intake replay")
            return existing[0][0]
        cursor = connection.execute(
            "INSERT INTO leads "
            "(contract_id, cycle, source_key, contact_key, evidence_digest, score) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (contract_id, cycle, source_key, contact_key, digest, score),
        )
        return cursor.lastrowid
''',
                        (
                            "Derive contact keys using client-scoped HMAC outside this "
                            "module; verify authorization before intake and preserve evidence separately."
                        ),
                    ],
                    [
                        "Module three: append verification and obligation functions to ledger.py",
                        r'''def _obligation(connection, identifier, contract_id, cycle, kind, lead_id, amount):
    expected = (identifier, contract_id, cycle, kind, lead_id, amount)
    connection.execute(
        "INSERT INTO obligations "
        "(id, contract_id, cycle, kind, lead_id, amount_cents) "
        "VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO NOTHING",
        expected,
    )
    stored = connection.execute(
        "SELECT id, contract_id, cycle, kind, lead_id, amount_cents "
        "FROM obligations WHERE id = ?",
        (identifier,),
    ).fetchone()
    if stored != expected:
        raise ValueError("Obligation replay changed immutable terms")
    payload = json.dumps(
        {
            "obligation_id": identifier,
            "contract_id": contract_id,
            "cycle": cycle,
            "kind": kind,
            "amount_cents": amount,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    connection.execute(
        "INSERT INTO outbox(event_key, payload) VALUES (?, ?) "
        "ON CONFLICT(event_key) DO NOTHING",
        (identifier, payload),
    )
    stored_payload = connection.execute(
        "SELECT payload FROM outbox WHERE event_key = ?",
        (identifier,),
    ).fetchone()[0]
    if stored_payload != payload:
        raise ValueError("Outbox payload differs from immutable obligation")
    return identifier


def decide(db, lead_id, accept):
    if type(accept) is not bool:
        raise ValueError("Acceptance decision must be explicitly Boolean")
    desired = "accepted" if accept else "rejected"
    with transaction(db) as connection:
        row = connection.execute(
            "SELECT contract_id, cycle, score, state FROM leads WHERE id = ?",
            (lead_id,),
        ).fetchone()
        if row is None:
            raise ValueError("Lead identifier does not exist")
        contract_id, cycle, score, state = row
        identifier = "lead:" + str(lead_id)
        if state != "held":
            if state != desired:
                raise ValueError("Terminal decisions cannot be overwritten")
            return identifier if accept else None
        if accept and score != 100:
            raise ValueError("Incomplete qualification cannot be accepted")
        connection.execute(
            "UPDATE leads SET state = ? WHERE id = ?",
            (desired, lead_id),
        )
        if not accept:
            return None
        amount = connection.execute(
            "SELECT lead_fee_cents FROM contracts WHERE id = ?",
            (contract_id,),
        ).fetchone()[0]
        return _obligation(
            connection, identifier, contract_id, cycle, "lead", lead_id, amount
        )


def recognize_retainer(db, contract_id, cycle):
    period(cycle)
    with transaction(db) as connection:
        row = connection.execute(
            "SELECT retainer_cents FROM contracts WHERE id = ?",
            (contract_id,),
        ).fetchone()
        if row is None:
            raise ValueError("Contract identifier does not exist")
        identifier = "retainer:" + contract_id + ":" + cycle
        return _obligation(
            connection, identifier, contract_id, cycle, "retainer", None, row[0]
        )
''',
                        (
                            "A serialized transaction commits acceptance, receivable, and "
                            "billing event together; rejected prospects never create recognized fees."
                        ),
                    ],
                    [
                        "Module four: append billing dispatch and cash allocation to ledger.py",
                        r'''def send_pending(db, send):
    with transaction(db) as connection:
        pending = connection.execute(
            "SELECT event_key, payload FROM outbox "
            "WHERE remote_receipt IS NULL ORDER BY event_key"
        ).fetchall()
    for event_key, payload in pending:
        receipt = text_key(send(event_key, json.loads(payload)))
        with transaction(db) as connection:
            stored = connection.execute(
                "SELECT remote_receipt FROM outbox WHERE event_key = ?",
                (event_key,),
            ).fetchone()[0]
            if stored is not None and stored != receipt:
                raise ValueError("Provider returned conflicting replay receipts")
            connection.execute(
                "UPDATE outbox SET remote_receipt = ? WHERE event_key = ?",
                (receipt, event_key),
            )


def collect(db, receipt_key, obligation_id, cash_cycle, amount_cents):
    text_key(receipt_key)
    text_key(obligation_id)
    period(cash_cycle)
    positive_cents(amount_cents)
    expected = (obligation_id, cash_cycle, amount_cents)
    with transaction(db) as connection:
        stored = connection.execute(
            "SELECT obligation_id, cash_cycle, amount_cents "
            "FROM receipts WHERE receipt_key = ?",
            (receipt_key,),
        ).fetchone()
        if stored is not None:
            if stored != expected:
                raise ValueError("Receipt identifier reused with different allocation")
            return
        obligation = connection.execute(
            "SELECT cycle, amount_cents FROM obligations WHERE id = ?",
            (obligation_id,),
        ).fetchone()
        if obligation is None:
            raise ValueError("Receipt requires an existing obligation")
        if cash_cycle < obligation[0]:
            raise ValueError("Advance receipts require a separate liability ledger")
        paid = connection.execute(
            "SELECT COALESCE(SUM(amount_cents), 0) FROM receipts "
            "WHERE obligation_id = ?",
            (obligation_id,),
        ).fetchone()[0]
        if paid + amount_cents > obligation[1]:
            raise ValueError("Receipt exceeds the remaining receivable")
        connection.execute(
            "INSERT INTO receipts VALUES (?, ?, ?, ?)",
            (receipt_key, obligation_id, cash_cycle, amount_cents),
        )


def book_cost(db, cycle, amount_cents):
    period(cycle)
    positive_cents(amount_cents)
    with transaction(db) as connection:
        connection.execute(
            "INSERT INTO costs VALUES (?, ?) ON CONFLICT(cycle) DO NOTHING",
            (cycle, amount_cents),
        )
        stored = connection.execute(
            "SELECT amount_cents FROM costs WHERE cycle = ?", (cycle,)
        ).fetchone()[0]
        if stored != amount_cents:
            raise ValueError("Closed monthly cost cannot be silently overwritten")
''',
                        (
                            "External delivery requires durable provider-side idempotency; "
                            "receipt allocation remains serialized and rejects conflicting or excessive collections."
                        ),
                    ],
                    [
                        "Module five: save monthly reconciliation views as views.sql",
                        r'''CREATE VIEW v_monthly AS
WITH periods AS (
    SELECT cycle FROM obligations
    UNION SELECT cycle FROM costs
    UNION SELECT cash_cycle FROM receipts
),
monthly AS (
    SELECT
        p.cycle,
        COALESCE((
            SELECT SUM(o.amount_cents) FROM obligations o
            WHERE o.cycle = p.cycle
        ), 0) AS revenue_cents,
        COALESCE((
            SELECT c.amount_cents FROM costs c
            WHERE c.cycle = p.cycle
        ), 0) AS cost_cents,
        COALESCE((
            SELECT SUM(r.amount_cents) FROM receipts r
            WHERE r.cash_cycle = p.cycle
        ), 0) AS cash_cents
    FROM periods p
)
SELECT
    cycle,
    revenue_cents,
    cost_cents,
    revenue_cents - cost_cents AS profit_cents,
    cash_cents,
    cash_cents - cost_cents AS net_cash_cents,
    SUM(cash_cents - cost_cents) OVER (
        ORDER BY cycle ROWS UNBOUNDED PRECEDING
    ) AS cumulative_cash_cents,
    SUM(revenue_cents - cash_cents) OVER (
        ORDER BY cycle ROWS UNBOUNDED PRECEDING
    ) AS ending_receivables_cents
FROM monthly;

CREATE VIEW v_receivables AS
SELECT
    o.id,
    o.contract_id,
    o.cycle,
    o.amount_cents,
    o.amount_cents - COALESCE(SUM(r.amount_cents), 0) AS open_cents
FROM obligations o
LEFT JOIN receipts r ON r.obligation_id = o.id
GROUP BY o.id, o.contract_id, o.cycle, o.amount_cents;
''',
                        (
                            "Monthly cash and earned revenue remain separate; cumulative "
                            "receivables assume the stated cohort has no opening balance or credits."
                        ),
                    ],
                    [
                        "Module six: save this reproducible cohort and concurrency harness as qa.py",
                        r'''from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import sqlite3

from ledger import (
    book_cost,
    collect,
    decide,
    intake,
    recognize_retainer,
    register_contract,
    send_pending,
    transaction,
)


def expect_value_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError("Expected operation to reject conflicting input")


def main():
    root = Path(__file__).resolve().parent
    with TemporaryDirectory() as directory:
        db = str(Path(directory) / "cohort.sqlite3")
        connection = sqlite3.connect(db)
        try:
            connection.executescript(
                (root / "schema.sql").read_text(encoding="utf-8")
            )
            connection.executescript(
                (root / "views.sql").read_text(encoding="utf-8")
            )
        finally:
            connection.close()

        for index in range(5):
            register_contract(db, "client-" + str(index), 2500000, 25000)

        months = [
            ("2026-01", 50, 40, 2450000),
            ("2026-02", 54, 42, 2485000),
            ("2026-03", 56, 43, 2502500),
        ]
        previous_cycle = None
        first_lead = None

        for cycle, submitted, accepted, cost in months:
            for index in range(5):
                client = "client-" + str(index)
                obligation = recognize_retainer(db, client, cycle)
                arguments = (
                    db, "bank:" + obligation, obligation, cycle, 2500000
                )
                if cycle == "2026-01" and index == 0:
                    with ThreadPoolExecutor(max_workers=8) as pool:
                        list(pool.map(lambda _: collect(*arguments), range(8)))
                else:
                    collect(*arguments)

            for index in range(submitted):
                client = "client-" + str(index % 5)
                source = cycle + ":source:" + str(index)
                fingerprint = sha256(source.encode("utf-8")).hexdigest()
                evidence = sha256(
                    ("evidence:" + source).encode("utf-8")
                ).hexdigest()
                facts = (True, True, True, index < accepted)
                lead = intake(
                    db, client, cycle, source, fingerprint, facts, evidence
                )
                assert intake(
                    db, client, cycle, source, fingerprint, facts, evidence
                ) == lead
                if first_lead is None:
                    first_lead = lead
                    with ThreadPoolExecutor(max_workers=8) as pool:
                        results = list(
                            pool.map(lambda _: decide(db, lead, True), range(8))
                        )
                    assert len(set(results)) == 1
                else:
                    decide(db, lead, index < accepted)

            if previous_cycle is not None:
                with transaction(db) as connection:
                    due = connection.execute(
                        "SELECT id, amount_cents FROM obligations "
                        "WHERE kind = 'lead' AND cycle = ? ORDER BY id",
                        (previous_cycle,),
                    ).fetchall()
                for obligation, amount in due:
                    collect(
                        db, "bank:" + obligation, obligation, cycle, amount
                    )

            book_cost(db, cycle, cost)
            previous_cycle = cycle

        expect_value_error(lambda: decide(db, first_lead, False))
        first_retainer = "retainer:client-0:2026-01"
        expect_value_error(
            lambda: collect(
                db, "extra-bank-entry", first_retainer, "2026-03", 1
            )
        )
        expect_value_error(
            lambda: collect(
                db,
                "bank:" + first_retainer,
                first_retainer,
                "2026-01",
                1,
            )
        )

        remote = {}

        def idempotent_test_provider(key, payload):
            expected = ("remote:" + key, payload)
            stored = remote.setdefault(key, expected)
            assert stored == expected
            return stored[0]

        send_pending(db, idempotent_test_provider)
        with transaction(db) as connection:
            connection.execute("UPDATE outbox SET remote_receipt = NULL")
        send_pending(db, idempotent_test_provider)
        assert len(remote) == 140

        with transaction(db) as connection:
            rows = connection.execute(
                "SELECT * FROM v_monthly ORDER BY cycle"
            ).fetchall()
            assert rows == [
                ("2026-01", 3500000, 2450000, 1050000,
                 2500000, 50000, 50000, 1000000),
                ("2026-02", 3550000, 2485000, 1065000,
                 3500000, 1015000, 1065000, 1050000),
                ("2026-03", 3575000, 2502500, 1072500,
                 3550000, 1047500, 2112500, 1075000),
            ]
            assert connection.execute(
                "SELECT COUNT(*) FROM leads WHERE state = 'accepted'"
            ).fetchone()[0] == 125
            assert connection.execute(
                "SELECT COUNT(*) FROM leads WHERE state = 'rejected'"
            ).fetchone()[0] == 35
            assert connection.execute(
                "SELECT COUNT(*) FROM obligations"
            ).fetchone()[0] == 140
            assert connection.execute(
                "SELECT SUM(open_cents) FROM v_receivables"
            ).fetchone()[0] == 1075000
            assert connection.execute(
                "SELECT COUNT(*) FROM v_receivables WHERE open_cents < 0"
            ).fetchone()[0] == 0
            assert connection.execute(
                "SELECT COUNT(*) FROM obligations o "
                "LEFT JOIN outbox b ON b.event_key = o.id "
                "WHERE b.event_key IS NULL"
            ).fetchone()[0] == 0
            assert connection.execute(
                "SELECT COUNT(*) FROM leads l "
                "LEFT JOIN obligations o ON o.lead_id = l.id "
                "WHERE (l.state = 'accepted' AND o.id IS NULL) "
                "OR (l.state != 'accepted' AND o.id IS NOT NULL)"
            ).fetchone()[0] == 0
            assert connection.execute("PRAGMA foreign_key_check").fetchall() == []

        print("Cohort totals and local transactional replay checks passed")


if __name__ == "__main__":
    main()
''',
                        (
                            "The harness uses synthetic identities and a fake billing "
                            "provider; production provider behavior and infrastructure still require integration testing."
                        ),
                    ],
                ],
            },
        },
        {
            "heading": "3. Walk three delivery cohorts from accepted units to collected cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Begin the 90-day walk when five contracted clients enter a "
                    "full service month, not on the day the business is incorporated. "
                    "The scorecard's one-to-four-month first-deal interval precedes "
                    "this mature cohort assumption. Month 1 submits 50 distinct "
                    "candidates, rejects ten, and accepts 40. Five $5,000 retainers "
                    "produce $25,000 of earned service revenue; 40 accepted units "
                    "at $250 produce another $10,000. Month 2 submits 54, rejects "
                    "12, and accepts 42, producing $35,500. Month 3 submits 56, "
                    "rejects 13, and accepts 43, producing $35,750. The quarter "
                    "therefore contains 160 submissions, 35 prebilling scrubs, and "
                    "125 accepted leads. Its 78.125% acceptance rate is a planning "
                    "assumption, not a claim about any acquisition channel. Each "
                    "month's retainer is earned and paid by that month's close; "
                    "accepted-lead invoices are collected in the following month. "
                    "There is no opening receivable, cancellation, refund, or "
                    "uncollectible invoice in this worked example. Those exclusions "
                    "make the timing bridge inspectable while leaving rejection "
                    "losses visible in the production denominator. Never count "
                    "the client's downstream contract value, sales pipeline, or "
                    "advertising budget as additional operator revenue."
                ),
                (
                    "Recognize $35,000 in Month 1 but collect only $25,000 because "
                    "the first $10,000 of lead fees remains outstanding. Operating "
                    "costs of $24,500 leave $500 of operating cash movement and "
                    "$10,500 of earned owner profit. Month 2 collects its $25,000 "
                    "retainer plus Month 1's $10,000 lead balance, pays $24,850 "
                    "of costs, and adds $10,150 of cash. Month 3 collects "
                    "$25,000 plus Month 2's $10,500 lead balance, pays $25,025, "
                    "and adds $10,475. Cumulative operating cash reaches $21,125; "
                    "the remaining $10,750 receivable explains the difference from "
                    "$31,875 of quarterly profit. Allocate the $74,375 cost "
                    "envelope as $18,000 of platform and administrative overhead "
                    "plus $56,375 of labor, delivery, and operator-funded acquisition. "
                    "The resulting $6,000 monthly overhead sits inside the "
                    "scorecard's $2,000–$12,000 monthly operating-overhead range; "
                    "it is not a substitute for fully loaded delivery costs. "
                    "Assume all modeled costs are paid in their service month. "
                    "A $10,000 opening operating reserve yields $31,125 closing "
                    "cash before owner distributions, while remaining separate "
                    "from both earned revenue and profit."
                ),
                (
                    "Annualize the quarter, not the highest month. Four equivalent "
                    "quarters produce $425,000 revenue, $297,500 costs, and "
                    "$127,500 owner profit at exactly 30.0%. The average monthly "
                    "revenue is $35,416.67 when rounded for display; multiplying "
                    "Month 3 alone by twelve would incorrectly imply $429,000. "
                    "The same annual model contains 60 client-month retainers "
                    "worth $300,000 and 500 accepted leads worth $125,000. "
                    "Across the quarter, the $56,375 delivery envelope equals "
                    "$352.34 per submitted candidate or $451 per accepted lead, "
                    "including retainer service work. Consequently, the $250 "
                    "variable fee cannot carry the entire operation alone; "
                    "retainer renewal is economically essential. If one client "
                    "leaves for a full month, the immediate retainer exposure "
                    "is $5,000 before considering lost lead fees. If ten "
                    "otherwise accepted leads are scrubbed, revenue falls "
                    "$2,500 unless replacement delivery restores the units. "
                    "Use these sensitivities to set weekly quality reviews "
                    "and renewal outreach rather than hiding deterioration "
                    "inside aggregate volume. The Conservative and Scaled "
                    "cases remain separate scorecard outcomes: $20,000 profit "
                    "on $100,000 revenue and $300,000 profit on $750,000 "
                    "revenue, with their stated staffing."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort and accepted delivery unit calculation",
                    "Earned operator revenue excluding client advertising",
                    "Cash collections and outstanding invoice timing",
                    "Paid operating costs and owner profit",
                    "Operating cash movement and reconciliation checkpoint",
                ],
                "rows": [
                    [
                        "Month 1: 50 submitted, ten scrubbed, 40 finally accepted",
                        "Five retainers earn $25,000; accepted fees earn $10,000; total $35,000",
                        "Collect $25,000 retainers; carry $10,000 accepted fees into Month 2",
                        "Pay $24,500 total costs; recognize $10,500 monthly owner profit",
                        "Add $500 operating cash; cumulative cash movement equals $500",
                    ],
                    [
                        "Month 2: 54 submitted, twelve scrubbed, 42 finally accepted",
                        "Five retainers earn $25,000; accepted fees earn $10,500; total $35,500",
                        "Collect $35,000 including prior fees; carry $10,500 into Month 3",
                        "Pay $24,850 total costs; recognize $10,650 monthly owner profit",
                        "Add $10,150 operating cash; cumulative cash movement reaches $10,650",
                    ],
                    [
                        "Month 3: 56 submitted, thirteen scrubbed, 43 finally accepted",
                        "Five retainers earn $25,000; accepted fees earn $10,750; total $35,750",
                        "Collect $35,500 including prior fees; carry $10,750 into Month 4",
                        "Pay $25,025 total costs; recognize $10,725 monthly owner profit",
                        "Add $10,475 operating cash; cumulative cash movement reaches $21,125",
                    ],
                    [
                        "Quarter total: 160 submitted, 35 scrubbed, 125 accepted delivery units",
                        "Fifteen client-month retainers plus accepted fees produce exactly $106,250",
                        "Collect $95,500 total cash; ending accepted-fee receivables equal $10,750",
                        "Pay $74,375 total costs; earn $31,875 at exactly 30.0%",
                        "Operating cash $21,125 plus receivables $10,750 equals profit $31,875",
                    ],
                    [
                        "Base annual bridge: repeat four equivalent delivery quarters",
                        "Sixty client-month retainers and 500 accepted leads produce $425,000",
                        "Collection timing rolls forward; annual revenue does not equal quarterly cash multiplied",
                        "Annual costs total $297,500; annual owner profit equals $127,500",
                        "Use 1 FT plus 3 C; annual margin remains exactly 30.0%",
                    ],
                    [
                        "Working-capital bridge: begin with $10,000 unrestricted operating reserve",
                        "Opening reserve is contributed cash rather than earned operator revenue",
                        "Month 4 collects remaining $10,750 if every due invoice clears",
                        "Reserve supports payment timing; daily liquidity requires a separate cash calendar",
                        "Closing cash before distributions equals $10,000 plus $21,125, or $31,125",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four tactics that protect accepted-unit economics",
                "body": (
                    "Optimize the accepted cohort and its collection behavior rather "
                    "than celebrating raw form fills, inbox counts, or answered calls."
                ),
                "items": [
                    "Review the first ten deliveries with the client's actual closer; adjust qualification questions before increasing acquisition spend.",
                    "Keep separate scoreboards for wrong-fit leads and client-missed appointments so the responsible party receives the corrective action.",
                    "Price retainers against real service workload: this cohort's $451 fully loaded delivery cost per accepted lead cannot be funded by $250 fees alone.",
                    "Run a weekly invoice-aging call with the client using immutable lead identifiers; resolve evidence disputes before the next fee batch becomes due.",
                ],
            },
        },
        {
            "heading": "4. Attach specialist plays without importing their risk or gross proceeds into revenue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat arizona_abs_mass_tort_cocounsel as a separate licensed "
                    "business architecture, not an upgrade to an ordinary marketing "
                    "invoice. Arizona Supreme Court Rule 31.1(c), ACJA § 7-209, "
                    "and the jurisdiction's removal of its former ER 5.4 "
                    "restrictions enable approved Alternative Business Structures; "
                    "they do not abolish other jurisdictions' professional rules. "
                    "Nonlawyer ownership requires the actual licensed structure, "
                    "responsible attorneys, and applicable fee-sharing arrangements. "
                    "Survivor matters involving detention facilities, clergy, "
                    "boarding schools, medical providers, or rideshare proceedings "
                    "require trauma-informed attorney intake and primary-document "
                    "verification before filing. An illustrative $200,000 collected "
                    "legal fee with a valid 25% allocation yields $50,000 to "
                    "the entitled firm before its costs, not $200,000 of "
                    "marketing revenue. The mapped $50,000–$400,000-plus settled-case "
                    "economics are possibilities requiring case-specific support, "
                    "not production forecasts. Segregate these receipts from the "
                    "five-client cohort. In restrictive jurisdictions, an MSO "
                    "can supply genuine services under a reviewed structure, "
                    "but its label does not authorize prohibited fee sharing. "
                    "Licensed attorneys must perform substantive legal work; "
                    "use independently justified single-event injury work to "
                    "support capacity while institutional dockets develop, without "
                    "pressuring survivors or assuming a settlement schedule."
                ),
                (
                    "Combine ad_library_spend_velocity_arbitrage with "
                    "google_maps_gbp_lead_gen_network only after separating evidence "
                    "from inference. Meta Ad Library, Google Ads Transparency "
                    "Center, and TikTok Creative Center can reveal creative "
                    "persistence and variants, but ordinary commercial visibility "
                    "does not establish exact spend or profitability. Review "
                    "permitted public interfaces at their allowed cadence. A "
                    "creative active beyond 30 days is a research signal; "
                    "adapt its structural hook or qualification flow using "
                    "entirely original copy, imagery, and video. A $1,000 "
                    "operator-funded test producing eight accepted leads costs "
                    "$125 per acceptance and earns $2,000 at the cohort's "
                    "$250 fee, leaving $1,000 before labor and overhead. "
                    "Stop or revise when accepted-unit costs erase that "
                    "contribution. For Maps, each profile must represent an "
                    "eligible real business, with accurate signage, staffing, "
                    "address treatment, and category selection. A partner's "
                    "shop or yard is insufficient if the business fails "
                    "Google's eligibility requirements; hide addresses where "
                    "service-area rules require it. Twelve qualified calls "
                    "with eight accepted appointments yield $2,000 at the "
                    "same fee. Fall back to original organic city pages "
                    "and authorized partner referrals if a listing cannot "
                    "be verified, rather than fabricating locations or reviews."
                ),
                (
                    "Apply platform_privilege_tier_account_arbitrage as documented "
                    "platform stewardship, not account trading or influence "
                    "laundering. Local Guides levels, Wikipedia confirmation "
                    "thresholds, Product Hunt participation, and review badges "
                    "do not establish guaranteed ranking power. Sell a "
                    "$1,500 monthly research-and-correction service requiring "
                    "ten contractor hours at $60: $900 remains before "
                    "tools and overhead, but the deliverable is verified "
                    "work, not purchased endorsement. Keep local contributions "
                    "within genuine geographic knowledge, follow conflict "
                    "restrictions, disclose paid editing where required, and "
                    "use correction requests rather than prohibited self-serving "
                    "edits. Never sell favorable reviews, access credentials, "
                    "or fabricated independent testimony. For "
                    "gis_landlocked_parcel_easement_assemblage, use QGIS parcel "
                    "geometry to identify candidates, then obtain recorded "
                    "deeds, title exceptions, and survey evidence before "
                    "representing access. County map lines cannot establish "
                    "a legal easement. A $2,000 research engagement with "
                    "$800 of contractor diligence leaves $1,200 before "
                    "overhead; the land's purchase price is not operator "
                    "revenue. If an option strategy is pursued separately, "
                    "make exercise contingent on title, survey, access, "
                    "and permitted use. Fall back to voluntary, survey-backed "
                    "access services when defects remain. Reject coercive "
                    "interference with existing access and never sell an "
                    "unverified parcel lead as an assured development opportunity."
                ),
            ],
            "table": {
                "caption": "Mapped Specialist Plays: Acceptance Units, Revenue Boundaries, and Risk Fallbacks",
                "headers": [
                    "Mapped play and authorized operating application",
                    "Concrete unit economics and recognition boundary",
                    "Required evidence before accepting the delivery unit",
                    "Risk fallback protecting the operator and client",
                ],
                "rows": [
                    [
                        "arizona_abs_mass_tort_cocounsel: operate only through the appropriately licensed legal structure",
                        "$200,000 collected legal fee times lawful 25% allocation equals $50,000",
                        "ABS license, attorney engagement, substantive work, and primary case documents",
                        "Use reviewed service structures where permitted; exclude speculative settlements from marketing revenue",
                    ],
                    [
                        "ad_library_spend_velocity_arbitrage: research persistent creatives through permitted public advertising interfaces",
                        "$1,000 test divided by eight accepted leads equals $125 acquisition cost",
                        "Dated observations, original asset files, accepted-lead evidence, and actual test spend",
                        "Adapt structural ideas only; replace weak tests before increasing acquisition budgets",
                    ],
                    [
                        "google_maps_gbp_lead_gen_network: support eligible real partner businesses and accurate locations",
                        "Twelve qualified calls yielding eight accepted appointments produce $2,000 fees",
                        "Business eligibility, partner authorization, verification evidence, and genuine call-routing records",
                        "Use original city pages and referrals instead of fabricated business locations",
                    ],
                    [
                        "platform_privilege_tier_account_arbitrage: provide evidence-backed corrections rather than purchasable platform influence",
                        "$1,500 service retainer less ten $60 hours leaves $900 before overhead",
                        "Reliable sources, required paid-contribution disclosure, and each platform's conflict rules",
                        "Submit transparent correction requests; refuse account sales and favorable-review purchases",
                    ],
                    [
                        "gis_landlocked_parcel_easement_assemblage: research voluntary access arrangements using recorded property evidence",
                        "$2,000 research engagement less $800 diligence leaves $1,200 before overhead",
                        "Recorded instruments, title exceptions, survey evidence, and written diligence contingencies",
                        "Offer survey-backed voluntary services when legal access cannot be established",
                    ],
                    [
                        "Portfolio separation: preserve the canonical commercial lead-generation revenue boundary",
                        "Base remains $425,000 revenue and $127,500 profit without specialist proceeds",
                        "Separate contracts, entity records, bank allocations, and applicable professional authorization",
                        "Exclude client asset values, media budgets, and hypothetical settlements from scorecards",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A lead becomes revenue only when the contracted evidence survives review, and revenue becomes cash only when a unique receipt clears.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Sign a five-field acceptance schedule defining territory, buyer role, need, duplicate window, evidence standard, and dispute ownership.",
        "Verify sender authentication, sender-wide suppression, telephone permissions, staffed routing, and client authorization before activating acquisition.",
        "Save the six reference modules, run the synthetic cohort harness, and test provider idempotency plus database restoration before live deployment.",
        "Close each month with accepted-unit counts, prebilling scrub reasons, earned retainers, variable-fee obligations, and bank-origin receipt identifiers.",
        "Reconcile the quarter to $106,250 revenue, $74,375 costs, $31,875 profit, $21,125 operating cash movement, and $10,750 ending receivables.",
        "Separate licensed legal operations, property transactions, platform contributions, and client-funded advertising from ordinary lead-generation revenue.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Defines commercial-email requirements affecting sender identity, "
                "subject lines, advertising identification, postal addresses, and opt-out processing."
            ),
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Requires channel-specific review of telephone and text practices, "
                "including restrictions associated with recipient numbers and calling technology."
            ),
        },
        {
            "title": "47 CFR § 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Provides implementing calling, permission, identification, and "
                "do-not-call requirements relevant to routed calls and outbound campaigns."
            ),
        },
        {
            "title": "Arizona Supreme Court Rule 31.1(c) and ACJA § 7-209 — Alternative Business Structures",
            "url": "https://www.azcourts.gov/Alternative-Business-Structure",
            "relevance": (
                "The Arizona judiciary's official ABS resource links the governing "
                "licensing framework; ownership and legal-service operations require actual authorization."
            ),
        },
        {
            "title": "California Civil Code § 1798.100 — Consumer privacy rights and business obligations",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.100.",
            "relevance": (
                "For covered businesses, informs collection notices, purpose limits, "
                "retention practices, and contractual controls for processing personal information."
            ),
        },
        {
            "title": "16 CFR Part 465 — Rule on the Use of Consumer Reviews and Testimonials",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465",
            "relevance": (
                "Addresses prohibited review and testimonial practices; platform "
                "stewardship must not become fabricated reviews or sentiment-conditioned review purchasing."
            ),
        },
        {
            "title": "18 U.S.C. § 2511 — Interception and disclosure of communications",
            "url": "https://www.law.cornell.edu/uscode/text/18/2511",
            "relevance": (
                "Supplies the federal interception framework for call-recording "
                "design; operators must also evaluate applicable stricter state requirements."
            ),
        },
    ],
}
