from __future__ import annotations

_SCHEMA = r'''
import hashlib
import json
import sqlite3
from contextlib import contextmanager

db = sqlite3.connect(
    "operator_ledger.sqlite3",
    timeout=30,
    isolation_level=None,
)
db.row_factory = sqlite3.Row
db.execute("PRAGMA foreign_keys = ON")
db.execute("PRAGMA journal_mode = WAL")
db.execute("PRAGMA synchronous = FULL")
db.execute("PRAGMA busy_timeout = 30000")
db.executescript("""
CREATE TABLE IF NOT EXISTS deals (
    deal_id TEXT PRIMARY KEY,
    client_ref TEXT NOT NULL UNIQUE,
    intake_hash TEXT NOT NULL,
    model TEXT NOT NULL CHECK (
        model IN ('wholesale', 'rebate', 'treasury', 'concierge')
    ),
    state TEXT NOT NULL DEFAULT 'draft' CHECK (
        state IN (
            'draft', 'verified', 'committed',
            'shipped', 'accepted', 'settled'
        )
    ),
    exposure_cents INTEGER NOT NULL CHECK (exposure_cents >= 0),
    due_day TEXT NOT NULL,
    evidence_ref TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    payload_hash TEXT NOT NULL,
    deal_id TEXT REFERENCES deals(deal_id),
    evidence_ref TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS entries (
    event_id INTEGER NOT NULL REFERENCES events(event_id),
    line_no INTEGER NOT NULL,
    account TEXT NOT NULL,
    debit_cents INTEGER NOT NULL CHECK (debit_cents >= 0),
    credit_cents INTEGER NOT NULL CHECK (credit_cents >= 0),
    PRIMARY KEY (event_id, line_no),
    CHECK (
        (debit_cents > 0 AND credit_cents = 0)
        OR (credit_cents > 0 AND debit_cents = 0)
    )
);
CREATE TABLE IF NOT EXISTS outbox (
    message_key TEXT PRIMARY KEY,
    event_id INTEGER NOT NULL UNIQUE REFERENCES events(event_id),
    payload TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'pending' CHECK (
        state IN ('pending', 'inflight', 'sent', 'review')
    ),
    receipt TEXT
);
CREATE TABLE IF NOT EXISTS controls (
    singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
    exposure_limit_cents INTEGER NOT NULL
        CHECK (exposure_limit_cents >= 0)
);
INSERT OR IGNORE INTO controls VALUES (1, 2000000);
CREATE TRIGGER IF NOT EXISTS immutable_event_update
BEFORE UPDATE ON events BEGIN
    SELECT RAISE(ABORT, 'Events are append only');
END;
CREATE TRIGGER IF NOT EXISTS immutable_event_delete
BEFORE DELETE ON events BEGIN
    SELECT RAISE(ABORT, 'Events are append only');
END;
CREATE TRIGGER IF NOT EXISTS immutable_entry_update
BEFORE UPDATE ON entries BEGIN
    SELECT RAISE(ABORT, 'Entries are append only');
END;
CREATE TRIGGER IF NOT EXISTS immutable_entry_delete
BEFORE DELETE ON entries BEGIN
    SELECT RAISE(ABORT, 'Entries are append only');
END;
""")

def digest(value):
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

@contextmanager
def transaction():
    db.execute("BEGIN IMMEDIATE")
    try:
        yield
        db.execute("COMMIT")
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise

def existing_event(event_key, payload_hash):
    row = db.execute(
        "SELECT event_id, payload_hash FROM events WHERE event_key = ?",
        (event_key,),
    ).fetchone()
    if row is None:
        return None
    if row["payload_hash"] != payload_hash:
        raise ValueError("Idempotency key reused with different content")
    return row["event_id"]

def insert_event(event_key, payload_hash, deal_id, evidence_ref, lines):
    if not db.in_transaction:
        raise RuntimeError("Event insertion requires an active transaction")
    debit = 0
    credit = 0
    for account, dr, cr in lines:
        if not account or type(dr) is not int or type(cr) is not int:
            raise ValueError("Use named accounts and integer cents")
        if not ((dr > 0 and cr == 0) or (cr > 0 and dr == 0)):
            raise ValueError("Each entry must have exactly one positive side")
        debit += dr
        credit += cr
    if debit != credit:
        raise ValueError("Journal does not balance")
    cursor = db.execute(
        """INSERT INTO events
           (event_key, payload_hash, deal_id, evidence_ref)
           VALUES (?, ?, ?, ?)""",
        (event_key, payload_hash, deal_id, evidence_ref),
    )
    event_id = cursor.lastrowid
    db.executemany(
        """INSERT INTO entries
           (event_id, line_no, account, debit_cents, credit_cents)
           VALUES (?, ?, ?, ?, ?)""",
        [
            (event_id, number, account, dr, cr)
            for number, (account, dr, cr) in enumerate(lines, 1)
        ],
    )
    return event_id

def journal(event_key, evidence_ref, lines, deal_id=None):
    if not evidence_ref or not lines:
        raise ValueError("Cash journals require evidence and balanced entries")
    payload_hash = digest([deal_id, evidence_ref, lines])
    with transaction():
        prior = existing_event(event_key, payload_hash)
        if prior is not None:
            return prior
        return insert_event(
            event_key, payload_hash, deal_id, evidence_ref, lines
        )
'''

_INTAKE = r'''
from datetime import date

def intake(
    deal_id, client_ref, model, exposure_cents, due_day,
    evidence_ref, collectible_cents, landed_cents, fee_cents,
    loss_reserve_cents, minimum_edge_cents
):
    amounts = (
        exposure_cents, collectible_cents, landed_cents,
        fee_cents, loss_reserve_cents, minimum_edge_cents,
    )
    if any(type(value) is not int or value < 0 for value in amounts):
        raise ValueError("All amounts must be nonnegative integer cents")
    date.fromisoformat(due_day)
    if not deal_id or not client_ref or not evidence_ref:
        raise ValueError("Deal identity and source evidence are mandatory")
    edge = (
        collectible_cents - landed_cents
        - fee_cents - loss_reserve_cents
    )
    if edge < minimum_edge_cents:
        raise ValueError("Conservative collectible edge fails intake")
    values = [
        deal_id, client_ref, model, exposure_cents, due_day,
        evidence_ref, collectible_cents, landed_cents,
        fee_cents, loss_reserve_cents, minimum_edge_cents,
    ]
    intake_hash = digest(values)
    with transaction():
        old = db.execute(
            "SELECT deal_id, intake_hash FROM deals WHERE client_ref = ?",
            (client_ref,),
        ).fetchone()
        if old is not None:
            if old["intake_hash"] != intake_hash:
                raise ValueError("Client reference conflicts with prior intake")
            return old["deal_id"], edge
        db.execute(
            """INSERT INTO deals
               (deal_id, client_ref, intake_hash, model,
                exposure_cents, due_day, evidence_ref)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                deal_id, client_ref, intake_hash, model,
                exposure_cents, due_day, evidence_ref,
            ),
        )
    return deal_id, edge
'''

_TRANSITIONS = r'''
def advance(
    event_key, deal_id, expected_version, target,
    evidence_ref, lines=(), dispatch_payload=None
):
    allowed = {
        "draft": {"verified"},
        "verified": {"committed"},
        "committed": {"shipped", "accepted"},
        "shipped": {"accepted"},
        "accepted": {"settled"},
        "settled": set(),
    }
    if not evidence_ref:
        raise ValueError("A transition needs independently retained evidence")
    if target == "settled" and not lines:
        raise ValueError("Settlement requires a balanced clearing journal")
    if dispatch_payload is not None and target != "committed":
        raise ValueError("Only commitment can enqueue a purchase instruction")
    payload = [
        deal_id, expected_version, target,
        evidence_ref, lines, dispatch_payload,
    ]
    payload_hash = digest(payload)
    with transaction():
        prior = existing_event(event_key, payload_hash)
        if prior is not None:
            return prior
        row = db.execute(
            "SELECT * FROM deals WHERE deal_id = ?", (deal_id,)
        ).fetchone()
        if row is None:
            raise ValueError("Deal must exist before transition")
        if row["version"] != expected_version:
            raise ValueError("Version conflict requires a fresh read")
        if target not in allowed[row["state"]]:
            raise ValueError("Transition is outside the permitted state path")
        if target == "committed":
            exposure = db.execute(
                """SELECT COALESCE(SUM(exposure_cents), 0)
                   FROM deals
                   WHERE state IN ('committed', 'shipped', 'accepted')"""
            ).fetchone()[0]
            limit_cents = db.execute(
                "SELECT exposure_limit_cents FROM controls WHERE singleton = 1"
            ).fetchone()[0]
            if exposure + row["exposure_cents"] > limit_cents:
                raise ValueError("Portfolio exposure limit would be exceeded")
        event_id = insert_event(
            event_key, payload_hash, deal_id, evidence_ref, lines
        )
        cursor = db.execute(
            """UPDATE deals SET state = ?, version = version + 1
               WHERE deal_id = ? AND version = ?""",
            (target, deal_id, expected_version),
        )
        if cursor.rowcount != 1:
            raise RuntimeError("Concurrent transition was not applied")
        if dispatch_payload is not None:
            db.execute(
                """INSERT INTO outbox (message_key, event_id, payload)
                   VALUES (?, ?, ?)""",
                (
                    event_key,
                    event_id,
                    json.dumps(dispatch_payload, sort_keys=True),
                ),
            )
    return event_id
'''

_DISPATCH = r'''
def dispatch_one(sender):
    with transaction():
        row = db.execute(
            """SELECT message_key, payload FROM outbox
               WHERE state = 'pending' ORDER BY event_id LIMIT 1"""
        ).fetchone()
        if row is None:
            return False
        key = row["message_key"]
        cursor = db.execute(
            """UPDATE outbox SET state = 'inflight'
               WHERE message_key = ? AND state = 'pending'""",
            (key,),
        )
        if cursor.rowcount != 1:
            raise RuntimeError("Message claim was not applied")
    try:
        receipt = sender(key, json.loads(row["payload"]))
        if not isinstance(receipt, str) or not receipt.strip():
            raise ValueError("Sender must return a durable receipt reference")
    except Exception as exc:
        with transaction():
            db.execute(
                """UPDATE outbox SET state = 'review', receipt = ?
                   WHERE message_key = ? AND state = 'inflight'""",
                (type(exc).__name__, key),
            )
        raise
    with transaction():
        cursor = db.execute(
            """UPDATE outbox SET state = 'sent', receipt = ?
               WHERE message_key = ? AND state = 'inflight'""",
            (receipt, key),
        )
        if cursor.rowcount != 1:
            raise RuntimeError("Delivery outcome requires manual reconciliation")
    return True

# The sender must use message_key as its downstream idempotency key.
# Never automatically reclaim inflight or review messages.
# A crash after delivery requires receipt lookup before further action.
'''

_RECONCILIATION = r'''
db.executescript("""
CREATE VIEW IF NOT EXISTS account_balances AS
SELECT account,
       SUM(debit_cents) AS debit_cents,
       SUM(credit_cents) AS credit_cents,
       SUM(debit_cents - credit_cents) AS net_debit_cents
FROM entries
GROUP BY account;

CREATE VIEW IF NOT EXISTS deal_reconciliation AS
SELECT d.deal_id, d.model, d.state, d.due_day,
       COALESCE(SUM(CASE WHEN e.account = 'cash'
           THEN e.debit_cents - e.credit_cents ELSE 0 END), 0)
           AS cash_net_cents,
       COALESCE(SUM(CASE WHEN e.account = 'receivable'
           THEN e.debit_cents - e.credit_cents ELSE 0 END), 0)
           AS receivable_cents,
       COALESCE(SUM(CASE WHEN e.account = 'card_payable'
           THEN e.credit_cents - e.debit_cents ELSE 0 END), 0)
           AS card_payable_cents
FROM deals AS d
LEFT JOIN events AS v ON v.deal_id = d.deal_id
LEFT JOIN entries AS e ON e.event_id = v.event_id
GROUP BY d.deal_id, d.model, d.state, d.due_day;
""")

def reconciliation_rows():
    return [
        dict(row)
        for row in db.execute(
            "SELECT * FROM deal_reconciliation ORDER BY due_day, deal_id"
        )
    ]

# Example postings, all values in cents:
# journal("capital:001", "bank:capital:001", [
#     ("cash", 5500000, 0), ("owner_equity", 0, 5500000)
# ])
# journal("purchase:001", "issuer:purchase:001", [
#     ("inventory", 92500, 0), ("card_payable", 0, 92500)
# ], deal_id="deal-001")
# journal("repayment:001", "bank:repayment:001", [
#     ("card_payable", 92500, 0), ("cash", 0, 92500)
# ], deal_id="deal-001")
'''

_QA = r'''
def qa():
    issues = []
    if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        issues.append("SQLite integrity check failed")
    if db.execute("PRAGMA foreign_key_check").fetchone() is not None:
        issues.append("Foreign key integrity check failed")
    for row in db.execute(
        """SELECT event_id FROM entries GROUP BY event_id
           HAVING SUM(debit_cents) != SUM(credit_cents)"""
    ):
        issues.append("Unbalanced event " + str(row["event_id"]))
    for row in db.execute(
        """SELECT deal_id FROM deal_reconciliation
           WHERE state = 'settled'
             AND (receivable_cents != 0 OR card_payable_cents != 0)"""
    ):
        issues.append("Settlement residual on " + row["deal_id"])
    for row in db.execute(
        """SELECT message_key FROM outbox
           WHERE state IN ('inflight', 'review')"""
    ):
        issues.append("Delivery receipt investigation for " + row["message_key"])
    exposure = db.execute(
        """SELECT COALESCE(SUM(exposure_cents), 0) FROM deals
           WHERE state IN ('committed', 'shipped', 'accepted')"""
    ).fetchone()[0]
    limit_cents = db.execute(
        "SELECT exposure_limit_cents FROM controls WHERE singleton = 1"
    ).fetchone()[0]
    if exposure > limit_cents:
        issues.append("Active exposure exceeds the configured portfolio limit")
    for row in db.execute(
        """SELECT deal_id FROM deal_reconciliation
           WHERE card_payable_cents > 0 AND due_day <= date('now')"""
    ):
        issues.append("Card payment requires immediate confirmation for " + row["deal_id"])
    return issues

def require_clean_close():
    issues = qa()
    if issues:
        raise RuntimeError("; ".join(issues))
    return reconciliation_rows()

# Run independent processes against the same local database for contention tests.
# Replay an identical intake and event; counts and balances must remain unchanged.
# Reuse either key with changed content; the operation must raise ValueError.
# Attempt two commitments exceeding the shared limit; only eligible work may commit.
# Inject a crash after sender acceptance; the message must remain blocked from retry.
# Copy a live database using sqlite3.Connection.backup, then verify the restored copy.
'''

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort-walk",
    "question_prompt": (
        "How does an operator execute buying group, commercial card-float & rebate "
        "arbitrage end-to-end from intake to reconciled cash, backed by an auditable "
        "technical/ledger blueprint and a worked 90-day cohort walk?"
    ),
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": (
        "BuyForMeRetail Commitments, Commercial-Card Liability Calendars, SQLite "
        "Double-Entry Controls, IRC Basis Records & Cleared-ACH Cohort Economics"
    ),
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #41 ranks #10 of 43 with a 93/100 Money-to-Manpower Score. "
        "This operating blueprint connects 11 mapped plays without confusing wholesale "
        "receipts, card rewards, treasury income, or optional fintech referral fees. "
        "The canonical annual owner-profit cases are $20,000 Conservative, $143,500 "
        "Base, and $360,000 Scaled. Six copy-pasteable engineering modules establish "
        "integer-cent journals, unique event identities, serialized commitments, durable "
        "dispatch records, reconciliation views, and close checks. A worked 90-day "
        "cohort earns $35,875 after every modeled cost and releases the same cash "
        "after receivables clear. Operators work backward from issuer due dates, "
        "not advertised float. Warehouse acceptance, rebate eligibility, referral "
        "qualification, and bank evidence each have separate proof requirements; "
        "unresolved delivery outcomes stop retries rather than creating duplicate exposure."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": (
                "Annual gross scorecard basis; $87,500 retained contribution at 35%."
            ),
            "note": (
                "8% gross-basis margin; $20,000 annual owner net profit; "
                "22.86% retained margin; 1 FT + 2 C."
            ),
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": (
                "Annual gross scorecard basis; $358,750 retained contribution at 35%."
            ),
            "note": (
                "14.0% gross-basis margin; $143,500 annual owner net profit; "
                "40.0% retained margin; 1 FT + 2 C."
            ),
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": (
                "Annual gross scorecard basis; $630,000 retained contribution at 35%."
            ),
            "note": (
                "20% gross-basis margin; $360,000 annual owner net profit; "
                "57.14% retained margin; 2 FT + 3 C."
            ),
        },
    ],
    "sections": [
        {
            "heading": "1. Intake three separate economic models before authorizing exposure",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Begin every opportunity with a counterparty, economic model, collectible "
                    "amount, exposure ceiling, evidence packet, and last safe repayment date. "
                    "For wholesale fulfillment, obtain a written quantity and price commitment "
                    "from BuyForMeRetail, Pointsmaker, or MaxOutDeals before ordering; those names "
                    "identify diligence targets, not verified current offers. Record the receiving "
                    "warehouse, accepted product condition, serial-number requirements, ownership "
                    "transfer, inspection window, and the contractual trigger for Net-3 or Net-5 "
                    "payment. A carrier delivery scan is not warehouse acceptance. DE, NH, and "
                    "OR generally lack statewide general sales taxes, but destination alone "
                    "does not establish a resale exemption elsewhere. Retain the certificate "
                    "applicable to the seller and transaction, and resolve pickup, use-tax, "
                    "and nexus questions before purchase. Under UCC 2-509 and 2-513, risk "
                    "allocation and inspection rights depend on the transaction and agreement; "
                    "write both into the commitment packet. A $1,000 reimbursement against "
                    "$925 merchandise, $12 freight, $8 processing, and $10 expected loss "
                    "leaves $45 before fixed overhead. If the group will not document "
                    "acceptance and payout conditions, reject the order rather than replacing "
                    "missing evidence with an assumed reward or optimistic settlement date."
                ),
                (
                    "Keep the rebate model separate from that wholesale spread. An eligible "
                    "$10,000 commercial-card purchase at an assumed 2% earns $200; a "
                    "verified 1% portal award contributes another $100 only if the merchant, "
                    "category, account, and purchase path qualify. Rakuten and TopCashback "
                    "tracking is evidence of attribution, not final collectibility. Save offer "
                    "terms and timestamps, and remove pending awards from repayment capacity. "
                    "Likewise, a $10,000 B2B invoice routed through Plastiq or Melio at an "
                    "illustrative 2.9% processing fee costs $290. A 2% reward leaves a "
                    "$90 loss before financing effects. Even forty days of 4% simple "
                    "yield on $10,000 produces only $43.84, leaving a $46.16 deficit; "
                    "reject that combination. These percentages are modeling assumptions, not "
                    "current provider quotations. The treasury model instead measures interest "
                    "and qualifying bank bonuses against owned, available capital, minimum "
                    "balance commitments, fees, and withdrawal timing. A promotional fifty-five-day "
                    "statement interval is a maximum scheduling possibility, not an asset "
                    "or universal card term. Record purchase principal as a payable, forecast "
                    "actual due dates, and exclude borrowed principal from both revenue and "
                    "owner profit under every scenario."
                ),
                (
                    "The eleventh mapped play is free_llc_fintech_bounty_stacking, an optional "
                    "concierge sidecar with its own referral ledger. Offer a $0 service-fee "
                    "formation workflow while founders pay mandatory state charges directly. "
                    "After formation, present a sequential Required Business Infrastructure "
                    "Checklist covering banking, commercial cards, payroll, bookkeeping, and "
                    "merchant processing, while clearly distinguishing optional vendor choices "
                    "from actual operating necessities. Obtain informed permission before sending "
                    "founder information to any provider. Illustratively, eligible paid referral "
                    "amounts of $400, $300, $150, $150, and $150 total $1,150; "
                    "twenty fully qualified formations therefore earn $23,000. The broader "
                    "$600–$1,800+ range is an underwriting hypothesis requiring written partner "
                    "terms, not evidence that every founder qualifies. Disclose material referral "
                    "relationships under 16 CFR 255.5 and never fabricate business activity "
                    "to satisfy account conditions. Prequalify genuine thirty-day operating "
                    "revenue intent and release optional bookkeeping and operating-agreement "
                    "templates after verified bank funding, with that condition disclosed upfront. "
                    "Do not withhold filed documents or documents required for formation or "
                    "funding. If funding fails, stop referral accrual and retain a direct "
                    "provider path; no bounty is worth misleading the founder or financing "
                    "their qualification deposit."
                ),
            ],
            "table": {
                "caption": (
                    "Eleven Mapped Operator Plays: Ten Chapter Workflow Labels "
                    "Plus the Supplied Fintech Play Identifier"
                ),
                "headers": [
                    "Mapped play or paired operating plays",
                    "Concrete unit economics and operating mechanism",
                    "Evidence required before recognizing collectible value",
                    "Failure fallback that limits operator exposure",
                ],
                "rows": [
                    [
                        "Buying-group precommitment and destination-specific resale treatment form plays one and two.",
                        "$1,000 reimbursement less $925 merchandise leaves $75 before downstream costs.",
                        "Signed quantity commitment, receiving address, seller treatment, and applicable resale certificate.",
                        "Reject uncommitted inventory and resolve transaction-specific tax treatment before ordering.",
                    ],
                    [
                        "Commercial-card reward eligibility and shopping-portal attribution form plays three and four.",
                        "$10,000 eligible spend generates $200 card rewards plus $100 portal awards.",
                        "Issuer terms, merchant exclusions, activation timestamp, portal trace, and final award confirmation.",
                        "Remove disputed awards from collectible forecasts and preserve the underlying purchase rationale.",
                    ],
                    [
                        "B2B invoice routing and statement-cycle scheduling form plays five and six.",
                        "$200 reward minus $290 processing charge creates a $90 initial deficit.",
                        "Provider fee quotation, permitted card type, invoice legitimacy, and actual issuer dates.",
                        "Pay through cheaper rails when rewards and owned-capital timing cannot cover charges.",
                    ],
                    [
                        "Insured parcel handling and counterparty exposure limits form plays seven and eight.",
                        "$12 freight plus $10 expected loss consumes $22 of each illustrative spread.",
                        "Serial photographs, carrier acceptance, policy coverage, warehouse acceptance, and aging report.",
                        "Freeze new commitments after delayed remittance and pursue documented parcel recovery separately.",
                    ],
                    [
                        "Owned-capital Treasury-bill sweep execution constitutes the ninth mapped operating play.",
                        "$15,000 at 4% for thirty days earns approximately $49.32 interest.",
                        "Unencumbered balance, settlement calendar, maturity proceeds, and independently confirmed issuer obligations.",
                        "Keep repayment reserves outside the sweep and liquidate early only after pricing risk.",
                    ],
                    [
                        "Qualified bank-account bonus collection constitutes the tenth mapped operating play.",
                        "A $300 earned bonus less $25 fees contributes $275 before tax effects.",
                        "Written eligibility, qualifying funding evidence, required balance history, and actual award posting.",
                        "Skip bonuses requiring restricted cash that would breach the repayment reserve policy.",
                    ],
                    [
                        "free_llc_fintech_bounty_stacking supplies the eleventh play through a separately tracked concierge sidecar.",
                        "Twenty eligible formations multiplied by $1,150 paid referral value produce $23,000.",
                        "Founder permission, genuine operating intent, funded-account verification, partner terms, and award statements.",
                        "Stop accrual after failed qualification and offer optional templates only under disclosed conditions.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before the first irreversible commitment",
                "body": (
                    "The reviewer signs the evidence packet; a script cannot establish "
                    "merchant eligibility, customer permission, or cleared cash by itself."
                ),
                "items": [
                    (
                        "Match product, quantity, receiving address, acceptance trigger, "
                        "payment schedule, and insured risk allocation to the group commitment."
                    ),
                    (
                        "Verify issuer purchase eligibility and actual statement dates; "
                        "decline consumer card-cycling and spending outside the approved business purpose."
                    ),
                    (
                        "Reserve full near-term principal repayment in accessible funds, "
                        "then test a fourteen-day ACH delay without counting pending rewards."
                    ),
                    (
                        "Verify founder permission, partner referral eligibility, genuine "
                        "funding, and upfront template conditions before any concierge referral."
                    ),
                ],
            },
        },
        {
            "heading": "2. Build the integer-cent ledger and serialize every commitment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Copy the six reference modules in table order into one Python 3.9 "
                    "script; they share a connection and function namespace without third-party "
                    "dependencies. Module seven is a deployment instruction rather than another "
                    "software component. SQLite runs on one local host with a private database "
                    "file, WAL journaling, full synchronization, foreign keys, and a busy "
                    "timeout. Each worker process opens its own connection; do not share "
                    "a connection across threads or place this database on a network "
                    "filesystem. BEGIN IMMEDIATE serializes writers before they inspect exposure, "
                    "so two commitments cannot both consume the same remaining portfolio "
                    "limit. UNIQUE client references, immutable event keys, content hashes, "
                    "and version predicates prevent duplicate posting and stale transitions "
                    "through these functions. Integer cents eliminate binary floating-point "
                    "drift. The default $20,000 exposure ceiling is a policy input, not "
                    "an assertion that the bank has supplied that capacity. Recalculate "
                    "it from verified liquidity whenever obligations change. Evidence references "
                    "point to restricted documents; never store full card credentials, bank "
                    "login secrets, or founder identity scans inside free-form dispatch payloads. "
                    "Only the service account writes the file, and every adjustment uses "
                    "a reversing journal rather than editing prior entries."
                ),
                (
                    "The verification and escrow-control state machine progresses from draft "
                    "to verified, committed, shipped where relevant, accepted, and settled. "
                    "Here escrow-control means an internal reservation of the operator's own "
                    "funds, not custody of customer money or provision of an escrow "
                    "service. Verification requires an independently reviewed evidence reference; "
                    "a reference string alone proves nothing. Commitment atomically checks "
                    "active exposure, advances the version, records an event, and enqueues "
                    "an optional instruction. For rebate and treasury work, committed can "
                    "advance directly to accepted after eligibility evidence arrives. Settlement "
                    "requires balanced entries, and the close checks flag residual receivables "
                    "or card liabilities. Rejected, disputed, or canceled commitments remain "
                    "reserved until an operator documents a resolution; this deliberately "
                    "conservative reference does not automate release of disputed exposure. "
                    "Extend those paths only with equivalent transaction and journal tests. "
                    "The dispatcher claims each instruction once and sends its immutable "
                    "key downstream. A timeout moves the instruction to investigation; a "
                    "process crash leaves it inflight. Neither condition permits blind retry. "
                    "Downstream idempotency and receipt lookup are prerequisites for unattended "
                    "execution. Database serialization removes local read-check-write races; it "
                    "cannot manufacture exactly-once behavior inside an unrelated merchant or bank."
                ),
                (
                    "Use the posting API for every financial event and restrict direct "
                    "SQL writes to controlled migrations. Inventory acquisition debits inventory "
                    "and credits card payable; card repayment debits that payable and "
                    "credits cash. Wholesale acceptance records the receivable and the appropriate "
                    "revenue or clearing accounts under the documented accounting policy. "
                    "Customer reimbursement clears the receivable, while rewards enter separate "
                    "income or purchase-basis adjustment accounts according to their substance. "
                    "Treasury principal transfers between cash and investments without creating "
                    "income. The reconciliation view intentionally exposes account movements "
                    "rather than labeling every cash receipt profit. Settlement imports use "
                    "stable statement identifiers, account identity, and transaction identity, "
                    "not a date-and-amount guess. Test identical replays, conflicting payloads, "
                    "simultaneous commitments, partial failures, delayed receipts, and restore "
                    "procedures before enabling any external sender. The supplied checks "
                    "inspect journal balance, foreign keys, delivery ambiguity, exposure, and "
                    "settlement residuals; they do not replace comparison against independently "
                    "downloaded bank and issuer statements. Back up through SQLite's backup "
                    "API and test the restored copy. For multiple application hosts, move "
                    "the same invariants to Postgres with row locking or serializable "
                    "transactions and bounded whole-transaction retries, not shared-file SQLite."
                ),
            ],
            "table": {
                "caption": (
                    "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table"
                ),
                "headers": [
                    "Module and deployment responsibility",
                    "Invariant and operator evidence requirement",
                    "Copy-pasteable Python reference or deployment instruction",
                ],
                "rows": [
                    [
                        "Module one creates the schema, transaction wrapper, and balanced journal API.",
                        "Unique identities and append-only records protect committed journal history against duplicate requests.",
                        _SCHEMA,
                    ],
                    [
                        "Module two scores collectible edge and registers immutable intake identity.",
                        "Only conservative collectible amounts enter scoring; pending incentives receive no repayment credit.",
                        _INTAKE,
                    ],
                    [
                        "Module three implements verification, reserved exposure, and versioned state transitions.",
                        "Serialized exposure checks and event insertion share one indivisible local database transaction.",
                        _TRANSITIONS,
                    ],
                    [
                        "Module four dispatches durable instructions through a caller-supplied authorized sender.",
                        "Ambiguous external outcomes remain blocked until receipt investigation establishes the actual result.",
                        _DISPATCH,
                    ],
                    [
                        "Module five exposes account balances and deal-level cash reconciliation views.",
                        "Principal repayment and receivable collection remain distinct from recognized operating income.",
                        _RECONCILIATION,
                    ],
                    [
                        "Module six provides close checks and explicit failure-injection acceptance cases.",
                        "A clean local check must still reconcile against independent external financial statements.",
                        _QA,
                    ],
                    [
                        "Deployment instruction keeps the six modules inside one controlled service boundary.",
                        "Each process owns its connection; only authorized service identities may modify persistent storage.",
                        (
                            "Concatenate modules one through six in order into one script. "
                            "Run contention and crash tests against a disposable local database. "
                            "Supply a sender only after confirming downstream idempotency and receipt lookup. "
                            "Use filesystem permissions, encrypted backups, and separately retained source evidence."
                        ),
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register a conservatively scored intake",
                    "action": (
                        "Call intake with stable source identity, integer-cent costs, "
                        "collectible proceeds, exposure, and the actual repayment date."
                    ),
                    "detail": (
                        "Exclude unearned portal awards and conditional referral bonuses; "
                        "retain source documents outside the database under restricted access."
                    ),
                },
                {
                    "step": 2,
                    "title": "Verify and reserve before external execution",
                    "action": (
                        "Advance through verified and committed using current versions "
                        "and independently checked evidence references."
                    ),
                    "detail": (
                        "Refresh the exposure limit from verified accessible liquidity; "
                        "the commitment transaction reserves capacity before dispatch."
                    ),
                },
                {
                    "step": 3,
                    "title": "Dispatch once and resolve ambiguous receipts",
                    "action": (
                        "Pass a provider-supported idempotency key to the authorized "
                        "sender and retain the durable acceptance receipt."
                    ),
                    "detail": (
                        "Never reclaim an inflight instruction automatically; investigate "
                        "provider status before any corrective operation or reversal."
                    ),
                },
                {
                    "step": 4,
                    "title": "Post, reconcile, and close the cohort",
                    "action": (
                        "Import statement-linked balanced journals, compare independent "
                        "statements, and run require_clean_close after residuals clear."
                    ),
                    "detail": (
                        "Keep failed checks visible and unresolved commitments reserved; "
                        "release capacity only after verified settlement or reviewed resolution."
                    ),
                },
            ],
        },
        {
            "heading": "3. Walk three monthly cohorts from qualified demand to cleared cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The worked cohort is an illustrative composition of the supplied "
                    "Base scorecard, not a claim about current buying-group prices or "
                    "partner payouts. Each month processes sixty wholesale shipments and "
                    "thirty concierge leads. Six leads fail genuine operating-intent screening "
                    "and four fail funded-account qualification, leaving twenty earned referral "
                    "packages at $1,150. These ten scrubs generate neither revenue nor "
                    "referral receivables. Monthly wholesale reimbursements total $60,000; "
                    "merchandise costs are $55,520.84 in Month 1 and $55,520.83 "
                    "in Months 2 and 3. Earned card and portal rebates total "
                    "$2,000 monthly, approximately $1,110.42 at a modeled 2% card "
                    "rate plus $889.58 from separately eligible portal activity. Treasury "
                    "income contributes $416.67, $416.67, and $416.66. Each treasury "
                    "amount combines approximately $49.32 interest on $15,000 over "
                    "thirty days at an assumed 4% annual rate with a separately "
                    "earned illustrative bank bonus; quarterly rounding produces $147.95 "
                    "interest and $1,102.05 bonuses. Those bonus amounts are explicit "
                    "scenario inputs, not published account offers. The referral sidecar "
                    "contributes $23,000 monthly, so gross scorecard receipts reach "
                    "$256,250 across ninety days without counting purchase principal "
                    "or founder-paid state fees as additional revenue."
                ),
                (
                    "Start with $55,000 owner capital, within the stated $10,000–$55,000 "
                    "startup range. Hold $40,000 as accessible repayment and operating "
                    "reserves and place at most $15,000 of genuinely surplus owned "
                    "cash into the treasury sleeve. Sequential shipment batches keep "
                    "active merchandise exposure below the illustrated $20,000 ceiling; "
                    "the monthly purchase total is throughput, not simultaneous borrowing. "
                    "The cash model assumes every month's merchandise principal is "
                    "repaid during that month, leaving no ending card payable. Month "
                    "1 earns $85,416.67 but collects $75,416.67 because $10,000 "
                    "of wholesale reimbursement remains outstanding. Month 2 collects "
                    "that opening receivable while leaving its own $10,000 outstanding, "
                    "so collections equal $85,416.67. Month 3 clears the prior "
                    "$10,000 and collects its entire current cohort, producing "
                    "$95,416.66 cash receipts. All earned rebates, referrals, and "
                    "treasury income are assumed collected within their respective months. "
                    "If partner terms contradict that timing, move the receipt date "
                    "and increase required capital rather than changing earned profit. "
                    "The resulting month-end cash balances are $56,958.33, $68,916.67, "
                    "and $90,875.00, including the treasury sleeve at realizable "
                    "value and assuming no owner distributions."
                ),
                (
                    "Cost treatment is deliberately complete. Each monthly cohort incurs "
                    "$8,000 variable concierge fulfillment, equivalent to $400 for "
                    "each successful formation; $2,437.50 variable wholesale handling "
                    "and associated transaction costs; $1,500 realized shipment, return, "
                    "and rebate-reversal losses; and $6,000 fixed operating expense. "
                    "The variable categories exclude merchandise already deducted and "
                    "exclude costs already captured elsewhere. Quarterly post-merchandise "
                    "costs therefore equal $53,812.50: $24,000 concierge delivery, "
                    "$7,312.50 wholesale handling, $4,500 realized losses, and "
                    "$18,000 fixed overhead. Fixed overhead sits within the canonical "
                    "monthly operating range; variable fulfillment does not disappear "
                    "into that range. Gross receipts of $256,250 less $166,562.50 "
                    "merchandise leave $89,687.50 retained contribution, exactly 35%. "
                    "Subtracting $53,812.50 yields $35,875 owner profit, exactly "
                    "14% of gross and 40% of retained contribution. Four identical "
                    "quarters annualize to $1,025,000 gross, $358,750 retained, "
                    "and $143,500 owner profit. Actual recognition follows the "
                    "principal-versus-agent assessment: the supplied ASC 606 net-presentation "
                    "assumption is a scorecard convention, not proof that every "
                    "wholesale transaction qualifies for net reporting. Buying title "
                    "and bearing inventory risk can change financial-statement presentation "
                    "without changing this cash bridge."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort stage and measurable operating throughput",
                    "Earned gross basis and retained contribution",
                    "Cash timing, repayment, scrubs, and costs",
                    "Owner profit and cumulative operating cash bridge",
                ],
                "rows": [
                    [
                        "Month 1 originates sixty shipments and thirty founder leads; twenty founders qualify.",
                        "$85,416.67 gross less $55,520.84 merchandise produces $29,895.83 retained contribution.",
                        "$75,416.67 collected; $10,000 receivable; $55,520.84 principal paid; $17,937.50 other costs paid.",
                        "$11,958.33 profit; $1,958.33 cumulative cash generation; $56,958.33 ending cash including capital.",
                    ],
                    [
                        "Month 2 repeats sixty shipments and thirty leads with identical qualification discipline.",
                        "$85,416.67 gross less $55,520.83 merchandise produces $29,895.84 retained contribution.",
                        "$85,416.67 collected; opening $10,000 clears; replacement $10,000 receivable; $73,458.33 total costs paid.",
                        "$11,958.34 profit; $13,916.67 cumulative cash generation; $68,916.67 ending cash including capital.",
                    ],
                    [
                        "Month 3 repeats throughput and clears every outstanding wholesale cohort receivable.",
                        "$85,416.66 gross less $55,520.83 merchandise produces $29,895.83 retained contribution.",
                        "$95,416.66 collected; receivables close at zero; $55,520.83 principal and $17,937.50 other costs paid.",
                        "$11,958.33 profit; $35,875.00 cumulative cash generation; $90,875.00 ending cash including capital.",
                    ],
                    [
                        "Qualification scrub bridge rejects six intent failures and four funding failures monthly.",
                        "Twenty earned packages monthly at $1,150 produce $69,000 quarterly referral revenue.",
                        "Thirty rejected quarterly leads create no bounty accrual and require no qualification financing.",
                        "$24,000 quarterly concierge delivery cost supports sixty successful formations before allocated overhead.",
                    ],
                    [
                        "Loss and operating-cost bridge explicitly separates variable delivery from fixed overhead.",
                        "$89,687.50 quarterly retained contribution supports $53,812.50 of additional modeled costs.",
                        "$31,312.50 variable fulfillment; $4,500 realized losses; $18,000 fixed operating expense.",
                        "$35,875 quarterly owner profit survives every modeled merchandise, delivery, loss, and overhead deduction.",
                    ],
                    [
                        "Treasury and liability bridge separates owned surplus investments from commercial-card repayment reserves.",
                        "$147.95 interest plus $1,102.05 earned bank bonuses produces $1,250 quarterly treasury income.",
                        "$40,000 opening accessible reserve supports capped exposure; $15,000 owned surplus funds the sweep.",
                        "No borrowed principal enters revenue; ending card payables and cohort receivables both equal zero.",
                    ],
                    [
                        "Annualization bridge repeats the complete quarter four times without additional growth assumptions.",
                        "$1,025,000 annual gross and $358,750 retained contribution match the canonical Base scorecard.",
                        "$666,250 annual merchandise plus $215,250 additional costs reconcile the entire gross-to-profit bridge.",
                        "$143,500 annual owner profit equals 14.0% gross margin and 40.0% retained margin.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make timing visible before volume makes it expensive",
                "body": (
                    "The strongest spread can still fail when acceptance evidence, "
                    "issuer dates, or referral conditions arrive late."
                ),
                "items": [
                    (
                        "Partition warehouse shipments by receiving batch and photograph "
                        "serials before sealing; one disputed carton should not obscure an entire remittance."
                    ),
                    (
                        "Schedule card payments from cleared bank balances several business "
                        "days before the due date, rather than waiting for the advertised float maximum."
                    ),
                    (
                        "Preserve portal click evidence and offer exclusions at purchase "
                        "time; recognize a reversal against the originating cohort instead of burying it later."
                    ),
                    (
                        "Evaluate bank bonuses per restricted-capital day: a $300 award "
                        "requiring $20,000 for ninety days earns only $3.33 daily before fees and displaced yield."
                    ),
                ],
            },
        },
        {
            "heading": "4. Close the control loop and scale only reconciled cohorts",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run a morning liquidity review against actual statement dates and "
                    "a separate afternoon receiving review against warehouse acceptance. "
                    "Stress the largest group by fourteen additional calendar days "
                    "of ACH delay, shift settlement across a weekend, remove all "
                    "pending portal awards, and assume a high-value parcel recovery "
                    "takes sixty days. In the illustrated policy, $20,000 active "
                    "principal plus $6,000 near-term fixed overhead and $1,500 "
                    "loss coverage consumes $27,500 of the $40,000 accessible "
                    "reserve, leaving $12,500 before other scheduled obligations. "
                    "Include those other obligations before treating the remainder as "
                    "available capacity. A $5,000 delayed reimbursement can fit "
                    "this snapshot; additional variable-service payables can eliminate "
                    "that headroom. Stop new commitments if the forward balance "
                    "crosses the reserve floor. Card issuer financial review or "
                    "account closure means switch eligible business purchases to "
                    "preapproved alternatives or cash within existing capacity, not "
                    "manufactured payments or accelerated consumer card-cycling. Treasury "
                    "maturities should precede planned withdrawals; an early sale "
                    "can introduce price and settlement risk. Diversification across "
                    "vetted groups reduces concentration but does not make their "
                    "warehouse or banking dependencies independent."
                ),
                (
                    "The controller closes four separate reconciliations: purchase and "
                    "inventory movements, group acceptance and reimbursement, issuer "
                    "purchases and repayments, and incentive qualification and receipts. "
                    "IRC section 6001 and 26 CFR 1.6001-1 require adequate "
                    "records; preserve invoices, award terms, settlement statements, "
                    "adjustment explanations, and the accounting treatment selected "
                    "for each incentive type. Section 1012 supplies the general "
                    "cost-basis starting point, while purchase-linked rebates may "
                    "require basis or expense adjustments rather than duplicate "
                    "income. Referral compensation and bank awards need separate "
                    "classification instead of being automatically treated as merchandise "
                    "discounts. Where section 6050W reporting applies, reconcile "
                    "1099-K gross settlement amounts to underlying transactions, "
                    "refunds, fees, and books; an information return is not "
                    "a profit calculation. Maintain a written principal-versus-agent "
                    "analysis for wholesale arrangements and prevent one receipt "
                    "from appearing simultaneously as gross reimbursement and "
                    "incremental retained revenue. Keep the cohort report on "
                    "a consistent pretax owner-profit basis without silently "
                    "mixing personal taxes or owner distributions into operating "
                    "costs. Corrections use linked reversal entries and replacement "
                    "events, preserving the evidence chain. A mismatch remains "
                    "open until independently supported, even when the aggregate "
                    "bank balance appears comfortable."
                ),
                (
                    "Scale the reconciled control system rather than extrapolating a "
                    "single attractive offer. The canonical Conservative case is "
                    "$250,000 gross, $87,500 retained contribution, and $20,000 "
                    "owner profit; additional post-merchandise costs therefore equal "
                    "$67,500. Base is $1,025,000 gross, $358,750 retained, "
                    "and $143,500 profit, leaving $215,250 additional costs. "
                    "Scaled is $1,800,000 gross, $630,000 retained, and "
                    "$360,000 profit, leaving $270,000 additional costs. Those "
                    "bridges preserve the supplied 8%, 14%, and 20% "
                    "gross margins and approximately 22.86%, 40%, and "
                    "57.14% retained margins. They do not establish that "
                    "today's partner offers can produce those results. One "
                    "full-time operator and two contractors support Conservative "
                    "and Base; two full-time operators and three contractors "
                    "support Scaled. Assign one person commitment authority, "
                    "another independent statement reconciliation, and a designated "
                    "backup for due-date execution. Increase throughput only after "
                    "a complete acceptance, payout, reward-reversal, and statement "
                    "cycle closes without unexplained residuals. Reprice any "
                    "model whose realized losses or collection delays exceed "
                    "underwriting. If the concierge sidecar cannot earn the "
                    "modeled $23,000 monthly, replace that contribution with "
                    "documented eligible economics or publish a lower forecast; "
                    "never relabel card principal or merchant volume as revenue."
                ),
            ],
            "table": {
                "caption": (
                    "Daily Control Ownership, Statutory Records, and Canonical Scale Bridges"
                ),
                "headers": [
                    "Control owner and concrete operating checkpoint",
                    "Numeric threshold or financial reconciliation requirement",
                    "Evidence source and required decision record",
                    "Exception response before further exposure increases",
                ],
                "rows": [
                    [
                        "Commitment owner reviews counterparty aging before every additional warehouse purchase batch.",
                        "$20,000 active principal ceiling remains subordinate to the complete forward liquidity forecast.",
                        "Group acceptance timestamps, contractual payout triggers, cleared remittances, and concentration ledger.",
                        "Stop new orders when delayed reimbursement compromises repayment capacity or documented acceptance.",
                    ],
                    [
                        "Treasury owner tests delayed ACH against actual issuer payment execution dates.",
                        "$40,000 accessible reserve less $27,500 illustrated obligations leaves $12,500 provisional headroom.",
                        "Bank available balance, issuer statement, scheduled variable costs, and investment settlement calendar.",
                        "Reduce commitments before consuming headroom required by other known or reasonably expected payments.",
                    ],
                    [
                        "Receiving contractor assembles serial evidence and carrier recovery documentation for disputed parcels.",
                        "$1,500 monthly modeled realized losses must include reversals without duplicate merchandise deductions.",
                        "Packing photographs, carrier scan, declared coverage, receiving exception, and final recovery statement.",
                        "Reserve disputed value and exclude expected insurance proceeds until adequately supported as collectible.",
                    ],
                    [
                        "Controller reconciles incentive classification and information-return totals against underlying transaction records.",
                        "1099-K gross settlements reconcile through refunds and fees rather than becoming assumed profit.",
                        "IRC 6001 records, section 1012 basis schedules, and section 6050W settlement documentation.",
                        "Post linked corrections and preserve original evidence until every material difference is explained.",
                    ],
                    [
                        "Conservative staffing uses one full-time operator plus two contractors with separated review duties.",
                        "$250,000 gross minus $162,500 merchandise minus $67,500 additional costs equals $20,000 profit.",
                        "$87,500 retained contribution supports 8% gross margin and approximately 22.86% retained margin.",
                        "Keep commitments within verified capacity when lower volume cannot absorb the fixed operating base.",
                    ],
                    [
                        "Base staffing uses one full-time operator plus two contractors across reconciled monthly cohorts.",
                        "$1,025,000 gross minus $666,250 merchandise minus $215,250 additional costs equals $143,500 profit.",
                        "$358,750 retained contribution supports 14.0% gross margin and exactly 40.0% retained margin.",
                        "Revise the forecast when referral eligibility, actual collection timing, or realized losses deteriorate.",
                    ],
                    [
                        "Scaled staffing uses two full-time operators plus three contractors with independent close responsibility.",
                        "$1,800,000 gross minus $1,170,000 merchandise minus $270,000 additional costs equals $360,000 profit.",
                        "$630,000 retained contribution supports 20% gross margin and approximately 57.14% retained margin.",
                        "Add throughput only after tested recovery procedures and independently reconciled statements support expansion.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "A spread becomes spendable profit only after the goods, rewards, liabilities, "
        "and cleared cash agree."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        (
            "Create separate wholesale, rebate, treasury, and optional concierge "
            "ledgers; assign stable source identities before importing any transaction."
        ),
        (
            "Collect written group commitments, receiving rules, applicable resale "
            "evidence, carrier coverage, and issuer due dates before placing orders."
        ),
        (
            "Install the six reference modules in order and test duplicate events, "
            "conflicting payloads, concurrent commitments, dispatch crashes, and restored backups."
        ),
        (
            "Fund accessible repayment reserves and rerun the fourteen-day ACH-delay "
            "stress with every scheduled service payment and pending reward excluded from liquidity."
        ),
        (
            "Rebuild the three-month cash bridge from source statements, including "
            "referral scrubs, merchandise repayment, realized losses, and the $10,000 receivable roll."
        ),
        (
            "Close to $35,875 quarterly profit only when the illustrated assumptions "
            "are actually met; publish variances and preserve the canonical scenario labels."
        ),
    ],
    "statutory_citations": [
        {
            "title": "26 U.S.C. § 6001 — Notice or regulations requiring records",
            "url": "https://www.law.cornell.edu/uscode/text/26/6001",
            "relevance": (
                "Supports maintaining source records for merchandise costs, referral "
                "compensation, rewards, treasury receipts, and reported transaction amounts."
            ),
        },
        {
            "title": "26 CFR § 1.6001-1 — Records",
            "url": (
                "https://www.ecfr.gov/current/title-26/section-1.6001-1"
            ),
            "relevance": (
                "Connects the ledger's evidence references and retained statements "
                "to the requirement for sufficient books and records."
            ),
        },
        {
            "title": "26 U.S.C. § 1012 — Basis of property: cost",
            "url": "https://www.law.cornell.edu/uscode/text/26/1012",
            "relevance": (
                "Provides the general cost-basis framework used when evaluating "
                "purchase-linked adjustments; incentive classification requires transaction-specific analysis."
            ),
        },
        {
            "title": "26 U.S.C. § 6050W — Returns relating to payment settlements",
            "url": "https://www.law.cornell.edu/uscode/text/26/6050W",
            "relevance": (
                "Anchors reconciliation of applicable payment-settlement information "
                "reporting to gross transactions, adjustments, and the operator's books."
            ),
        },
        {
            "title": "16 CFR § 255.5 — Disclosure of material connections",
            "url": "https://www.ecfr.gov/current/title-16/section-255.5",
            "relevance": (
                "Addresses material referral relationships when recommending compensated "
                "fintech providers through the optional founder concierge workflow."
            ),
        },
        {
            "title": "6 Del. C. § 2-509 — Risk of loss in the absence of breach",
            "url": "https://delcode.delaware.gov/title6/c002/sc05/index.html#2-509",
            "relevance": (
                "Provides an enacted UCC risk-of-loss rule relevant when Delaware "
                "law governs; the shipment contract and governing law determine application."
            ),
        },
        {
            "title": "6 Del. C. § 2-513 — Buyer's right to inspection of goods",
            "url": "https://delcode.delaware.gov/title6/c002/sc05/index.html#2-513",
            "relevance": (
                "Supports distinguishing carrier delivery from inspection and acceptance "
                "when documenting warehouse reimbursement conditions under applicable Delaware law."
            ),
        },
    ],
}
