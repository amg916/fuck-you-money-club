from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "medical-equipment-resale-operating-process-production-blueprint",
    "question_prompt": "How does an operator execute medical equipment resale end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Serial-Level Biomed Evidence, FDA Role Classification, HIPAA Media Controls, SQLite Journals & Escrow-to-Cash Reconciliation",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, ranks #22 with a 64/100 "
        "Money-to-Manpower Score. This chapter maps three operator plays: diagnostic "
        "replacement lots, surgical/veterinary procedure bundles, and pre-sold aesthetic "
        "refurbishment. A two-full-time, four-contractor pod moves each serialized asset "
        "through title verification, decontamination, biomed testing, buyer acceptance, "
        "and reconciled cash. The production reference joins immutable evidence, "
        "transactional state changes, balanced journals, and retry-safe notifications "
        "without treating escrow funding as sales. A worked operating quarter produces "
        "$256,250 revenue and $41,000 owner profit, reconciling to the Base annual "
        "$1,025,000 revenue and $164,000 profit. Conservative annual profit is $25,000; "
        "Scaled annual profit is $396,000. Capital, service access, and inventory "
        "aging determine whether the apparent spread becomes spendable cash."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "10% net margin; $25,000 annual owner net profit; 2 FT + 4 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "16.0% net margin; $164,000 annual owner net profit; 2 FT + 4 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin.",
            "note": "22% net margin; $396,000 annual owner net profit; 3 FT + 5 C, eight people.",
        },
    ],
    "sections": [
        {
            "heading": "1. Assign one accountable pod and purchase only evidence-backed inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run Candidate #14 through three explicitly mapped plays: diagnostic replacement "
                    "lots, surgical/veterinary procedure bundles, and pre-sold aesthetic refurbishment. "
                    "These are merchandising lanes, not three independent businesses. Diagnostic "
                    "lots require probe condition, software entitlement, and exportable test results; "
                    "procedure bundles require a verified accessory manifest and compatible power "
                    "and gas connections; aesthetic units require treatment-counter evidence, "
                    "handpiece condition, and lawful software access. Keep human-use and veterinary "
                    "claims separate because intended use changes the applicable requirements. In "
                    "every lane, the modeled operator takes title and acts as principal; an agency "
                    "commission arrangement would require a different revenue model. Assign the "
                    "first full-time operator to sourcing, pricing, buyer qualification, and collections. "
                    "Assign the second to inventory custody, evidence completeness, dispatch, and "
                    "ledger review. Four fractional contractors cover biomed testing, specialist "
                    "repair, decontamination/media handling, and crating/freight. Purchase these "
                    "services against defined tickets rather than assuming four continuously available "
                    "technicians. The same pod serves all three lanes through a shared serial "
                    "register. A unit without a named buyer profile, accessible service procedure, "
                    "and bounded refurbishment budget stays outside purchased inventory even when "
                    "the auction spread looks attractive."
                ),
                (
                    "At intake, create a device identity from manufacturer, model, and physical "
                    "serial number, then photograph the nameplate and every included accessory. "
                    "Record the seller's authority to transfer the unit, acquisition document, "
                    "known liens, service history, software restrictions, recall findings, and "
                    "pickup conditions. A hospital surplus list is a sourcing lead, not proof "
                    "that every accessory or embedded license transfers. Obtain a lien release "
                    "when the seller's equipment is encumbered; possession alone does not resolve "
                    "a secured creditor's interest. Keep source documents in restricted object "
                    "storage and place their hashes and references in the inventory record. "
                    "Patient records, screenshots containing patient identifiers, and drive images "
                    "do not belong in the sales database. Route the device into dirty quarantine "
                    "before powering it or connecting it to any network. Require the seller's "
                    "decontamination evidence, then apply the receiving procedure appropriate to "
                    "the device and contamination risk. Price inbound freight, test labor, "
                    "replacement parts, cleaning, and expected outbound support before bidding. "
                    "A low purchase price cannot compensate for unavailable passwords, unsupported "
                    "firmware, damaged probes, or consumables that the buyer cannot obtain "
                    "through an authorized supply channel."
                ),
                (
                    "Use a purchasing score to prioritize investigation, never to certify clinical "
                    "safety. The reference score weights title evidence, documented demand, "
                    "serviceability, and price headroom, but release still requires device-specific "
                    "technical evidence. Separate servicing that restores original performance "
                    "from work that significantly changes performance, safety specifications, or "
                    "intended use. Remanufacturing can change the operator's FDA role and associated "
                    "registration, quality-system, labeling, and reporting duties; classify the "
                    "actual activity before accepting the work. Ordinary resale does not automatically "
                    "make every reseller a manufacturer or covered HIPAA entity. Conversely, "
                    "contractual responsibility for protected data cannot be dismissed because "
                    "the chassis is secondhand. Determine whether a business associate relationship "
                    "exists and document the required handling arrangements before receiving "
                    "accessible patient data. The release packet should contain the applicable "
                    "service procedure revision, calibrated test-equipment identity, measured "
                    "results, repair history, accessory reconciliation, and an independent "
                    "reviewer decision. Preset failure thresholds and rework limits before "
                    "testing begins. Otherwise, a technician under shipment pressure can turn "
                    "an unresolved fault into a cosmetic description, leaving the sales "
                    "operator to discover the defect during buyer acceptance."
                ),
            ],
            "table": {
                "caption": "Three-Play Intake, Custody, and Release Responsibility Matrix",
                "headers": [
                    "Operating lane or handoff",
                    "Required technical and commercial evidence",
                    "Named pod accountability and capacity rule",
                    "Failure response and retained audit record",
                ],
                "rows": [
                    [
                        "Diagnostic replacement lots enter through serial-specific replacement demand.",
                        "Capture probe images, operating hours, licensed options, and comparable completed sales.",
                        "Sourcing operator buys only after biomed contractor confirms test access.",
                        "Reject locked systems; preserve seller correspondence and the failed-access evidence.",
                    ],
                    [
                        "Surgical/veterinary procedure bundles follow a complete accessory manifest.",
                        "Match connectors, rated power, intended use, and reusable accessory condition.",
                        "Inventory operator assigns one bundle ticket across testing and packing contractors.",
                        "Separate incomplete bundles; revise buyer scope before making shipment commitments.",
                    ],
                    [
                        "Pre-sold aesthetic refurbishment begins with buyer-specific acceptance criteria.",
                        "Verify handpiece counts, cooling performance, software transfer, and service availability.",
                        "Sourcing operator reserves specialist hours before promising a delivery date.",
                        "Stop unsupported modifications; retain proposed work and role-classification findings.",
                    ],
                    [
                        "Dirty receiving quarantine precedes bench testing and sales photography.",
                        "Obtain contamination history and document device-appropriate cleaning and media handling.",
                        "Decontamination contractor signs completion; inventory operator controls physical release.",
                        "Isolate failed units; record location, containment measures, and reprocessing instructions.",
                    ],
                    [
                        "Biomed release requires measured results against the applicable service procedure.",
                        "Attach analyzer calibration status, raw readings, firmware identity, and reviewer signoff.",
                        "Biomed contractor tests; a separately assigned qualified reviewer resolves exceptions.",
                        "Return failed equipment to repair status without deleting earlier test results.",
                    ],
                    [
                        "Buyer acceptance and collections close the serialized ownership cycle.",
                        "Match signed acceptance, delivered accessories, invoice amount, and settled bank receipt.",
                        "Collections operator reconciles cash while inventory operator closes custody records.",
                        "Keep disputed receivables open; record claims separately from sales adjustments.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy service access and evidence before buying apparent margin",
                "body": (
                    "Experienced equipment traders price the missing dependency, not just the visible chassis. "
                    "Use these tactics before committing scarce pod hours."
                ),
                "items": [
                    "Ask for probe or handpiece serials before bidding; a chassis photograph can conceal the component that carries most replacement cost.",
                    "Have the specialist confirm password, calibration fixture, and parts access before scheduling pickup; discovering a locked service mode at receiving consumes storage and capital.",
                    "Photograph accessory layouts twice, at receiving and sealed packing, so a missing pedal or cable can be assigned to the correct custody interval.",
                    "Negotiate evidence-backed acceptance criteria before cosmetic refurbishment; otherwise the buyer can introduce new clinical performance expectations after freight has been paid.",
                ],
            },
        },
        {
            "heading": "2. Implement six transactional modules with evidence-linked journals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The six reference modules below concatenate into one Python 3.9 script using "
                    "SQLite and the standard library. They are an accounting and workflow kernel, "
                    "not a replacement for device-specific service procedures or a payment provider. "
                    "Run one connection per worker against a local disk database, enable foreign "
                    "keys on every connection, and keep the database off shared network filesystems. "
                    "BEGIN IMMEDIATE serializes competing writers before either can read mutable "
                    "state. Every operation records a canonical payload under a stable event key; "
                    "an identical retry returns without side effects, while changed content under "
                    "the same key fails. Device transitions also compare an expected version, so "
                    "two operators cannot both advance the same version. A busy timeout produces "
                    "a retryable failure rather than a partial transaction. Store integer cents "
                    "and explicit account names, never floating currency. The journal accepts "
                    "only balanced batches and makes posted rows immutable. This reference "
                    "intentionally excludes payables, deposits, taxes, and foreign currencies; "
                    "extend its account model and reconciliation equation before introducing "
                    "those transactions. Restrict writes to these functions because arbitrary "
                    "SQL access bypasses application-level authorization and batch validation."
                ),
                (
                    "Verification is an evidence decision, not a Boolean supplied by a marketplace "
                    "webhook. The authenticated application must check reviewer identity, document "
                    "hashes, signer authority, and provider receipts before calling advance. "
                    "The compact kernel requires nonempty evidence references and preserves them "
                    "inside the event payload; it does not validate a laboratory certificate or "
                    "authenticate an escrow message itself. Its state path moves from intake "
                    "through verified, funded, released, accepted, and settled. Funded means "
                    "the agreed escrow provider has confirmed the required funds, not that "
                    "operator cash or revenue has been recognized. Released requires a packing "
                    "record and shipment authority; accepted requires the contractual acceptance "
                    "record. Post revenue when the governing sale terms establish the recognition "
                    "event, using an accountant-reviewed policy rather than the state label "
                    "alone. Settled requires a matched bank reference and the relevant receipt "
                    "journal. Keep returns and disputes in a separate controlled exception "
                    "process with reversing entries; never overwrite the original sale. The "
                    "deliberately linear reference rejects unsupported transitions instead of "
                    "pretending that every equipment dispute can be resolved through one "
                    "universal automated state diagram."
                ),
                (
                    "Posting creates its notification in the same database transaction as the "
                    "journal, eliminating the lost-message interval between committing money "
                    "and queuing work. Dispatch is at least once: a crash after remote receipt "
                    "but before the local acknowledgement causes a retry with the identical "
                    "key and payload. The receiver must atomically deduplicate that key and "
                    "reject payload changes; without that contract, duplicate external effects "
                    "remain possible. Notifications contain no payment or shipment command, "
                    "and consumers must not derive ordered physical actions from their delivery "
                    "order. This confines race-free mutation to the documented transaction "
                    "boundary rather than making an impossible promise about arbitrary external "
                    "systems. Use the provider's immutable transaction identifier as the posting "
                    "reference and reject identifiers invented for retries. Reconcile the trial "
                    "balance, inventory account, receivables, and bank statement daily. The "
                    "reference identity assumes zero opening balances and separately posted "
                    "capital, which suits the worked cohort. Production operation also requires "
                    "encrypted backups, restricted evidence access, tested restores, and "
                    "independent review of source totals. A balanced journal proves arithmetic "
                    "consistency; it does not prove that the equipment exists or that a "
                    "customer actually accepted it."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and execution order",
                    "Transaction boundary and operating responsibility",
                    "Copy-pasteable Python reference, concatenate modules in order",
                    "Evidence and deployment acceptance requirement",
                ],
                "rows": [
                    [
                        "Module one establishes database identities, immutable journals, and transactional helpers.",
                        "Inventory operator provisions local storage; every worker opens its own connection.",
                        '''import hashlib
import json
import sqlite3
from contextlib import contextmanager

db = sqlite3.connect("equipment.sqlite3", timeout=30, isolation_level=None)
db.execute("PRAGMA foreign_keys = ON")
db.execute("PRAGMA journal_mode = WAL")
db.execute("PRAGMA busy_timeout = 30000")

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)

def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

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

db.executescript("""
CREATE TABLE IF NOT EXISTS devices (
    device_id TEXT PRIMARY KEY,
    maker TEXT NOT NULL,
    model TEXT NOT NULL,
    serial TEXT NOT NULL,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    status TEXT NOT NULL CHECK(status IN
      ('intake','verified','funded','released','accepted','settled','rejected')),
    version INTEGER NOT NULL DEFAULT 0 CHECK(version >= 0),
    UNIQUE(maker, model, serial)
);
CREATE TABLE IF NOT EXISTS events (
    event_key TEXT PRIMARY KEY,
    payload_hash TEXT NOT NULL,
    payload TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS batches (
    event_key TEXT PRIMARY KEY REFERENCES events(event_key),
    source TEXT NOT NULL,
    reference TEXT NOT NULL,
    UNIQUE(source, reference)
);
CREATE TABLE IF NOT EXISTS lines (
    event_key TEXT NOT NULL REFERENCES batches(event_key),
    line_number INTEGER NOT NULL,
    account TEXT NOT NULL CHECK(account IN
      ('cash','inventory','receivable','capital','sales',
       'cost_of_sales','operating_expense','scrubs_expense')),
    cents INTEGER NOT NULL CHECK(
      typeof(cents) = 'integer' AND
      cents BETWEEN -1000000000000 AND 1000000000000 AND cents != 0),
    PRIMARY KEY(event_key, line_number)
);
CREATE TABLE IF NOT EXISTS outbox (
    event_key TEXT PRIMARY KEY REFERENCES batches(event_key),
    payload TEXT NOT NULL,
    delivered INTEGER NOT NULL DEFAULT 0 CHECK(delivered IN (0,1))
);
""")
for table in ("events", "batches", "lines"):
    for operation in ("UPDATE", "DELETE"):
        db.execute(
            "CREATE TRIGGER IF NOT EXISTS lock_" + table + "_" + operation +
            " BEFORE " + operation + " ON " + table +
            " BEGIN SELECT RAISE(ABORT, 'immutable journal evidence'); END"
        )

def seen(event_key, payload):
    text = canonical(payload)
    fingerprint = digest(payload)
    prior = db.execute(
        "SELECT payload_hash, payload FROM events WHERE event_key = ?",
        (event_key,)
    ).fetchone()
    if prior:
        if prior != (fingerprint, text):
            raise ValueError("event key reused with changed content")
        return True
    db.execute("INSERT INTO events VALUES (?, ?, ?)",
               (event_key, fingerprint, text))
    return False

def require_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("a substantive reference is required")
    return value.strip()
''',
                        "Preserve schema version and restore evidence; restrict direct database modification.",
                    ],
                    [
                        "Module two performs serialized intake and transparent purchasing-priority scoring.",
                        "Acquisition operator supplies normalized identifiers and four documented investigation scores.",
                        '''def intake(device_id, maker, model, serial, ratings):
    identity = [require_text(x) for x in (device_id, maker, model, serial)]
    names = ("title", "demand", "service", "headroom")
    if set(ratings) != set(names):
        raise ValueError("four named ratings are required")
    if any(type(ratings[n]) is not int or not 0 <= ratings[n] <= 5
           for n in names):
        raise ValueError("ratings must be integers from zero through five")
    score = sum(ratings[n] * weight for n, weight in
                zip(names, (6, 6, 5, 3)))
    payload = {"kind": "intake", "identity": identity,
               "ratings": ratings, "score": score}
    key = "intake:" + digest(identity[0])
    with transaction():
        if seen(key, payload):
            return key
        db.execute(
            "INSERT INTO devices "
            "(device_id,maker,model,serial,score,status) "
            "VALUES (?,?,?,?,?,'intake')",
            tuple(identity) + (score,)
        )
    return key
''',
                        "Duplicate physical serials fail atomically; scoring never substitutes for technical release.",
                    ],
                    [
                        "Module three advances verification, escrow evidence, acceptance, and settlement states.",
                        "Authenticated application validates evidence before invoking this version-checked state transition.",
                        '''NEXT = {
    "intake": {"verified", "rejected"},
    "verified": {"funded", "rejected"},
    "funded": {"released"},
    "released": {"accepted"},
    "accepted": {"settled"},
}
REQUIRED = {
    "verified": ("title_record", "decontamination", "media_record",
                 "biomed_report", "reviewer"),
    "funded": ("provider_receipt", "funding_match"),
    "released": ("packing_record", "shipment_authority"),
    "accepted": ("acceptance_record",),
    "settled": ("bank_match", "receipt_posting"),
    "rejected": ("rejection_record",),
}

def advance(device_id, expected_version, target, evidence):
    device_id = require_text(device_id)
    if type(expected_version) is not int or expected_version < 0:
        raise ValueError("expected version must be a nonnegative integer")
    if target not in REQUIRED:
        raise ValueError("unsupported target state")
    for name in REQUIRED[target]:
        require_text(evidence.get(name))
    payload = {"kind": "transition", "device": device_id,
               "version": expected_version, "target": target,
               "evidence": evidence}
    key = "state:" + digest([device_id, expected_version, target])
    with transaction():
        if seen(key, payload):
            return key
        row = db.execute(
            "SELECT status,version FROM devices WHERE device_id = ?",
            (device_id,)
        ).fetchone()
        if not row or row[1] != expected_version:
            raise ValueError("device version conflict")
        if target not in NEXT.get(row[0], set()):
            raise ValueError("transition is not permitted")
        if target == "settled":
            posted = db.execute(
                "SELECT 1 FROM batches WHERE event_key = ?",
                (evidence["receipt_posting"],)
            ).fetchone()
            if not posted:
                raise ValueError("receipt journal is required")
        changed = db.execute(
            "UPDATE devices SET status = ?, version = version + 1 "
            "WHERE device_id = ? AND version = ?",
            (target, device_id, expected_version)
        ).rowcount
        if changed != 1:
            raise RuntimeError("atomic transition failed")
    return key
''',
                        "Evidence references remain in immutable events; settlement linkage still requires source review.",
                    ],
                    [
                        "Module four posts balanced journals and delivers retry-safe accounting notifications.",
                        "Collections operator uses stable source references; receiver enforces atomic idempotency.",
                        '''ACCOUNTS = {
    "cash", "inventory", "receivable", "capital", "sales",
    "cost_of_sales", "operating_expense", "scrubs_expense"
}

def post(source, reference, entries):
    source, reference = require_text(source), require_text(reference)
    entries = list(entries)
    if not 2 <= len(entries) <= 200:
        raise ValueError("journal requires two through two hundred lines")
    for account, cents in entries:
        if account not in ACCOUNTS:
            raise ValueError("unsupported account")
        if type(cents) is not int or not 0 < abs(cents) <= 1000000000000:
            raise ValueError("journal amounts must be bounded integer cents")
    if sum(cents for account, cents in entries) != 0:
        raise ValueError("journal is not balanced")
    payload = {"kind": "posting", "source": source,
               "reference": reference, "entries": entries}
    key = "post:" + digest([source, reference])
    with transaction():
        if seen(key, payload):
            return key
        db.execute("INSERT INTO batches VALUES (?, ?, ?)",
                   (key, source, reference))
        db.executemany("INSERT INTO lines VALUES (?, ?, ?, ?)",
                       [(key, i, account, cents)
                        for i, (account, cents) in enumerate(entries)])
        notice = {"kind": "ledger.posted", "key": key,
                  "posting_hash": digest(payload)}
        db.execute("INSERT INTO outbox(event_key,payload) VALUES (?, ?)",
                   (key, canonical(notice)))
    return key

def dispatch_one(send):
    row = db.execute(
        "SELECT event_key,payload FROM outbox "
        "WHERE delivered = 0 ORDER BY event_key LIMIT 1"
    ).fetchone()
    if not row:
        return False
    key, text = row
    payload = json.loads(text)
    acknowledgement = send(key, payload)
    if acknowledgement != {"key": key, "payload_hash": digest(payload)}:
        raise ValueError("receiver acknowledgement does not match")
    with transaction():
        db.execute(
            "UPDATE outbox SET delivered = 1 "
            "WHERE event_key = ? AND payload = ? AND delivered = 0",
            (key, text)
        )
    return True
''',
                        "Concurrent dispatch may repeat delivery; receiver deduplication prevents repeated downstream effects.",
                    ],
                    [
                        "Module five exposes trial balance and the cohort cash reconciliation equation.",
                        "Ledger reviewer separates equipment revenue, inventory investment, receivables, and capital.",
                        '''db.executescript("""
CREATE VIEW IF NOT EXISTS trial_balance AS
SELECT account, SUM(cents) AS balance_cents
FROM lines GROUP BY account;

CREATE VIEW IF NOT EXISTS ledger_totals AS
SELECT
 COALESCE(SUM(CASE WHEN account='cash' THEN cents ELSE 0 END),0) AS cash,
 COALESCE(SUM(CASE WHEN account='inventory' THEN cents ELSE 0 END),0) AS inventory,
 COALESCE(SUM(CASE WHEN account='receivable' THEN cents ELSE 0 END),0) AS receivable,
 -COALESCE(SUM(CASE WHEN account='capital' THEN cents ELSE 0 END),0) AS capital,
 -COALESCE(SUM(CASE WHEN account='sales' THEN cents ELSE 0 END),0) AS revenue,
 COALESCE(SUM(CASE WHEN account IN
 ('cost_of_sales','operating_expense','scrubs_expense')
 THEN cents ELSE 0 END),0) AS expenses
FROM lines;

CREATE VIEW IF NOT EXISTS cash_reconciliation AS
SELECT cash, inventory, receivable, capital, revenue, expenses,
 revenue-expenses AS profit,
 cash-(capital+revenue-expenses-inventory-receivable) AS residual
FROM ledger_totals;
""")
''',
                        "Zero residual confirms the restricted model identity, not bank or serial existence.",
                    ],
                    [
                        "Module six checks database integrity and reproducibly posts the worked cohort.",
                        "Run the cohort only in an empty test database; production QA remains read-only.",
                        '''def qa():
    with transaction():
        if db.execute("PRAGMA integrity_check").fetchall() != [("ok",)]:
            raise RuntimeError("database integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("foreign key check failed")
        bad = db.execute(
            "SELECT b.event_key FROM batches b "
            "LEFT JOIN lines l ON l.event_key=b.event_key "
            "GROUP BY b.event_key "
            "HAVING COUNT(l.line_number)<2 OR COALESCE(SUM(l.cents),0)!=0"
        ).fetchall()
        if bad:
            raise RuntimeError("unbalanced or incomplete journal")
        if db.execute(
            "SELECT residual FROM cash_reconciliation"
        ).fetchone()[0] != 0:
            raise RuntimeError("cash identity failed")
        return dict(db.execute(
            "SELECT account,balance_cents FROM trial_balance"
        ).fetchall())

def worked_cohort():
    def dollars(reference, entries):
        return post("cohort-90", reference,
                    [(account, amount * 100) for account, amount in entries])

    dollars("opening-capital", [("cash", 150000), ("capital", -150000)])
    months = (
        ("month-1", 90000, 70000, 45000, 60000),
        ("month-2", 60000, 85000, 56000, 85000),
        ("month-3", 63000, 101250, 67000, 96250),
    )
    for label, purchases, sales, cost, receipts in months:
        dollars(label + "-purchases",
                [("inventory", purchases), ("cash", -purchases)])
        dollars(label + "-sales",
                [("receivable", sales), ("sales", -sales)])
        dollars(label + "-cost",
                [("cost_of_sales", cost), ("inventory", -cost)])
        dollars(label + "-receipts",
                [("cash", receipts), ("receivable", -receipts)])
        dollars(label + "-opex",
                [("operating_expense", 15000), ("cash", -15000)])
        dollars(label + "-scrubs",
                [("scrubs_expense", 750), ("cash", -750)])
    balances = qa()
    expected = {
        "cash": 13100000, "inventory": 4500000, "receivable": 1500000,
        "capital": -15000000, "sales": -25625000,
        "cost_of_sales": 16800000, "operating_expense": 4500000,
        "scrubs_expense": 225000,
    }
    if balances != expected:
        raise RuntimeError("cohort totals differ from the isolated fixture")
    return balances

# Invoke worked_cohort() in an isolated test database, then invoke it again.
# Identical retries must preserve every account balance and journal count.
''',
                        "Verify replay, conflicting payload rejection, and competing versions before operating deployment.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Establish identities and evidence ownership",
                    "action": "Create the device record and retain serial photographs, seller authority, and source-document hashes.",
                    "detail": "Normalize maker and model using controlled vocabulary; preserve the original serial transcription and prohibit speculative identity merges.",
                },
                {
                    "step": 2,
                    "title": "Verify before recording funded status",
                    "action": "Complete decontamination, media handling, biomed review, and buyer-specific acceptance terms.",
                    "detail": "The authenticated application validates evidence and escrow receipts; the workflow kernel only preserves references and enforces transitions.",
                },
                {
                    "step": 3,
                    "title": "Post recognition and cash as distinct events",
                    "action": "Record the approved sale recognition, release inventory cost, and post collections against the matching receivable.",
                    "detail": "Use immutable source references for every posting; buyer escrow funding alone creates neither recognized sales nor settled operator cash.",
                },
                {
                    "step": 4,
                    "title": "Close custody and reconcile independent sources",
                    "action": "Match bank receipts, signed acceptance, serialized inventory, and journal balances before closing the deal.",
                    "detail": "Resolve discrepancies through documented reversing entries and exception tickets; retain original evidence and never rewrite posted history.",
                },
            ],
        },
        {
            "heading": "3. Walk the 90-day cohort from purchased inventory to collected proceeds",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Treat this as a mature operating quarter with a warmed seller and buyer "
                    "pipeline, not a promise that a new entrant collects immediately. Candidate "
                    "#14 still carries a three-to-nine-month time to first deal and a "
                    "$75,000–$400,000 startup capital range. The illustration begins with "
                    "$150,000 cash, no inventory, no receivables, and no debt. Month 1 screens "
                    "24 leads, rejects 18 before purchase, acquires six units, and sells four. "
                    "Month 2 screens 20 leads, rejects 15, acquires five units, and sells "
                    "the two carried units plus three new units. Month 3 screens 24 leads, "
                    "rejects 18, acquires six units, and sells two carried units plus four "
                    "new units. Two units remain at quarter end. Each acquisition amount "
                    "includes the modeled capitalizable purchase and refurbishment outlay; "
                    "sold-unit costs are released separately into cost of sales. Rejected "
                    "leads never become inventory and create no equipment writeoff. The "
                    "separate $750 monthly scrub expense covers failed inspections and "
                    "disposal of noncapitalized consumables, paid within the month. This "
                    "distinction prevents counting the same refurbishment dollar both in "
                    "inventory cost and again as an operating loss."
                ),
                (
                    "Recognized gross resale proceeds are $70,000, $85,000, and $101,250 "
                    "across the three months, totaling $256,250. These are the operator's "
                    "principal sales, not the buyer's subsequent procedure revenue or the "
                    "equipment's original list price. Collections are $60,000, $85,000, "
                    "and $96,250. Month 2 collects Month 1's remaining $10,000 plus "
                    "$75,000 of current sales; Month 3 collects Month 2's remaining "
                    "$10,000 plus $86,250 of current sales. Ending receivables therefore "
                    "equal $15,000, all from Month 3. Cash purchases total $213,000, "
                    "while cost of sales totals $168,000, leaving $45,000 of inventory. "
                    "Monthly operating expense is $15,000: an illustrative $8,500 combined "
                    "loaded budget for two full-time roles, $2,500 for four fractional "
                    "contractors, and $4,000 for occupancy, insurance, software, and other "
                    "overhead. These are explicit capacity assumptions, not market wage "
                    "claims. Obtain actual local quotes and reduce deal throughput if "
                    "the contractor allocation cannot buy the required qualified hours. "
                    "Contract labor included in this overhead budget is not also included "
                    "in the acquisition and refurbishment amounts."
                ),
                (
                    "Quarter profit is $256,250 less $168,000 cost of sales, $45,000 "
                    "operating expense, and $2,250 scrub expense: exactly $41,000. Monthly "
                    "profits of $9,250, $13,250, and $18,500 have different margins; "
                    "only the quarter must reconcile to the 16.0% Base margin. Cash "
                    "tells a different story. Operating cash movement is negative $45,750 "
                    "in Month 1, positive $9,250 in Month 2, and positive $17,500 "
                    "in Month 3. The cumulative negative $19,000 movement takes opening "
                    "cash from $150,000 to $131,000. Reconcile that movement as "
                    "$41,000 profit minus $45,000 inventory growth minus $15,000 "
                    "receivable growth. There are no owner distributions, financing inflows "
                    "after opening, or sales-tax flows in this illustration. Multiplying "
                    "quarter revenue and profit by four yields the canonical Base "
                    "$1,025,000 and $164,000 annual figures, respectively. Do not "
                    "multiply the startup inventory build by four: a continuing business "
                    "replenishes working capital rather than resetting to empty each "
                    "quarter. The Conservative and Scaled cases retain their own "
                    "canonical margins and staffing; this cohort does not manufacture "
                    "either case through a simple throughput multiplier."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and sourced deal cohort",
                    "Recognized sales, costs, and scrub treatment",
                    "Cash receipts and cash purchase timing",
                    "Operating expense, profit, and cumulative cash flow",
                    "Closing inventory, receivables, and pod implications",
                ],
                "rows": [
                    [
                        "Opening day: warmed pipeline, zero owned units, and $150,000 contributed capital.",
                        "Opening revenue and expenses are zero; capital contribution is never equipment sales.",
                        "Bank receives $150,000 once; no additional borrowing or owner contributions follow.",
                        "Operating cash flow starts at zero before any inventory purchasing activity.",
                        "Two full-time operators reserve four fractional contractor schedules before committing purchases.",
                    ],
                    [
                        "Month 1: 24 leads, 18 rejected, six acquired, and four sold.",
                        "$70,000 sales less $45,000 sold-unit cost and $750 paid scrub expense.",
                        "$60,000 collected; $90,000 paid for acquisitions and included refurbishment work.",
                        "$15,000 opex; $9,250 profit; cumulative operating cash movement negative $45,750.",
                        "$104,250 cash, $45,000 inventory across two units, and $10,000 receivables remain.",
                    ],
                    [
                        "Month 2: 20 leads, 15 rejected, five acquired, and five sold.",
                        "$85,000 sales less $56,000 sold-unit cost and $750 paid scrub expense.",
                        "$85,000 collected, including $10,000 prior receivables; $60,000 paid for inventory.",
                        "$15,000 opex; $13,250 profit; cumulative operating cash movement negative $36,500.",
                        "$113,500 cash, $49,000 inventory across two units, and $10,000 receivables remain.",
                    ],
                    [
                        "Month 3: 24 leads, 18 rejected, six acquired, and six sold.",
                        "$101,250 sales less $67,000 sold-unit cost and $750 paid scrub expense.",
                        "$96,250 collected, including $10,000 prior receivables; $63,000 paid for inventory.",
                        "$15,000 opex; $18,500 profit; cumulative operating cash movement negative $19,000.",
                        "$131,000 cash, $45,000 inventory across two units, and $15,000 receivables remain.",
                    ],
                    [
                        "Quarter close: 68 leads, 51 rejected, 17 acquired, and 15 sold.",
                        "$256,250 revenue minus $168,000 cost, $45,000 opex, and $2,250 scrubs.",
                        "$241,250 receipts minus $213,000 purchases, $45,000 opex, and $2,250 scrubs.",
                        "$41,000 owner profit reconciles to negative $19,000 operating cash movement.",
                        "Profit less $45,000 inventory growth and $15,000 receivable growth explains cash.",
                    ],
                    [
                        "Base annual run rate multiplies quarter sales and profit by four.",
                        "$1,025,000 annual gross resale revenue supports exactly $164,000 annual owner profit.",
                        "Maintain working-capital balances; do not repeat the opening capital contribution.",
                        "16.0% net margin remains the Base target with $180,000 annualized opex.",
                        "Two full-time roles plus four contractors remain six people, not six full-time equivalents.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Stress the handoffs, preserve exceptions, and close the operating quarter",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first thirty days of implementation should establish evidence quality "
                    "before expanding inventory exposure. Configure the serial register, assign "
                    "restricted evidence folders, verify each contractor's scope, and rehearse "
                    "receiving with one representative unit from the chosen lane. Obtain "
                    "device-specific cleaning and test procedures and confirm that necessary "
                    "fixtures are available. Build buyer acceptance language around measurable "
                    "configuration and performance, not vague promises of excellent condition. "
                    "During days 31 through 60, exercise the complete ledger fixture in "
                    "an isolated database and then process a limited live batch only after "
                    "technical and commercial readiness. Deliberately submit identical intake "
                    "events, altered retries, and competing state transitions. The identical "
                    "retry must preserve counts; altered content must fail; only one "
                    "competing version may advance. Interrupt notification delivery after the "
                    "receiver commits but before acknowledgement, then confirm that the "
                    "receiver suppresses the repeated key. During days 61 through 90, "
                    "increase throughput only where contractor hours, warehouse segregation, "
                    "and buyer acceptance capacity support it. A startup that has not "
                    "yet acquired a qualified buyer should finish the process rehearsal "
                    "rather than copy the mature cohort's revenue schedule into its "
                    "cash forecast."
                ),
                (
                    "Inventory aging needs a technical clock as well as a calendar clock. "
                    "Review unsold units weekly for manufacturer support changes, expiring "
                    "consumables, battery deterioration, software access, and declining buyer "
                    "demand. Record a priced recovery route for every unit: qualified "
                    "resale, documented parts recovery, return to supplier, or controlled "
                    "disposal. Do not describe equipment as clinically ready when it "
                    "has only passed a power-on check. Match outbound photographs and "
                    "packing records to the serial manifest, use appropriate freight "
                    "coverage, and document any shock indicators or temperature controls "
                    "required by the device. When transit damage appears, preserve "
                    "packaging and carrier evidence before repair destroys the claim "
                    "record. Media sanitization must follow the device's storage architecture; "
                    "a factory reset may leave patient records in service partitions "
                    "or removable media. Verify the result and retain a certificate "
                    "that identifies the media and method without copying patient content. "
                    "If sanitization would disable clinical functionality, escalate to "
                    "the manufacturer-supported procedure rather than improvising. A blocked "
                    "unit remains physically segregated and commercially unavailable until "
                    "the responsible reviewer resolves both the technical condition and "
                    "the data-handling evidence."
                ),
                (
                    "At quarter close, reconcile three independent populations: physical serials, "
                    "commercial documents, and cash transactions. Count the two remaining "
                    "cohort units, substantiate their combined $45,000 carrying amount, "
                    "and investigate any impairment indicator rather than forcing the "
                    "inventory account to match a target. Confirm the $15,000 "
                    "receivable balance against buyer acceptance and subsequent receipts. "
                    "Trace every bank deposit to a source reference and distinguish "
                    "escrow balances from settled bank cash. Review warranty, return, "
                    "and damage claims for additional expense requirements; if real "
                    "experience exceeds the illustration, report the lower actual profit "
                    "instead of protecting the 16.0% narrative. The six-person Base "
                    "pod should automate inventory tracking and service-history indexing, "
                    "but keep purchase authority, technical release, and cash review "
                    "explicitly assigned. The Scaled scorecard allows three full-time "
                    "roles and five contractors, $1,800,000 revenue, and $396,000 "
                    "profit at 22%; that outcome requires a genuinely different "
                    "operating mix and cost performance. Conservative operation remains "
                    "$250,000 revenue and $25,000 profit at 10%. Use observed "
                    "repair variance, collection days, and inventory aging to decide "
                    "which case the business resembles, then size purchasing commitments "
                    "to that evidence rather than to the most attractive headline."
                ),
            ],
            "table": {
                "caption": "Failure Injection, Physical Exceptions, and Quarter-Close Evidence",
                "headers": [
                    "Failure or exception being challenged",
                    "Concrete control and expected system behavior",
                    "Independent evidence retained by the pod",
                    "Recovery action before further exposure",
                ],
                "rows": [
                    [
                        "Two workers attempt to release the same device version concurrently.",
                        "Immediate transactions serialize writes; only the first valid version update succeeds.",
                        "Retain both request identifiers and the rejected version-conflict response.",
                        "Refresh current state and investigate intent before issuing another transition.",
                    ],
                    [
                        "A payment-source retry arrives with a changed amount or account allocation.",
                        "Canonical payload comparison rejects changed content under the existing source reference.",
                        "Preserve provider source data and the rejected payload comparison record.",
                        "Resolve source correction with an explicit reversal and new documented reference.",
                    ],
                    [
                        "Notification receiver commits successfully while the sender loses its acknowledgement.",
                        "Resend the same immutable key; receiver returns its previously committed result.",
                        "Compare receiver deduplication records with the local pending outbox entry.",
                        "Mark delivery only after matching acknowledgement; never invent a replacement key.",
                    ],
                    [
                        "Stored patient records remain accessible after a cosmetic factory reset.",
                        "Quarantine the unit and block technical release pending verified media treatment.",
                        "Retain storage inventory and sanitization verification without preserving patient content.",
                        "Apply the supported method and repeat functional testing before release.",
                    ],
                    [
                        "Delivered equipment fails the buyer's agreed acceptance test after freight damage.",
                        "Open a custody-linked claim and prevent premature closure of disputed receivables.",
                        "Preserve packing photographs, carrier records, acceptance readings, and repair estimates.",
                        "Record approved credits or reversals separately and reassess inventory recovery value.",
                    ],
                    [
                        "Quarter profit appears correct but bank and physical inventory disagree.",
                        "Compare cash receipts, serial counts, cost layers, and receivable aging independently.",
                        "Retain signed count sheets, bank matches, and source-level reconciliation exceptions.",
                        "Correct supported differences through new entries and report actual revised results.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before releasing purchased equipment",
                "body": (
                    "The accountable operators verify these conditions on every serialized sale. "
                    "A missing condition stops physical release rather than creating an undocumented exception."
                ),
                "items": [
                    "Ownership and scope verified: seller authority, lien resolution where required, accessory manifest, transferable software rights, and intended-use classification are documented.",
                    "Technical and media evidence verified: decontamination, storage treatment, calibrated test results, applicable procedure revision, and qualified review are complete.",
                    "Commercial movement verified: buyer acceptance criteria, authentic escrow evidence, packing requirements, freight responsibility, and shipment authority match the same serial.",
                    "Ledger and retry behavior verified: source references are stable, journal entries balance, competing versions reject correctly, and the notification receiver demonstrates atomic deduplication.",
                ],
            },
        },
    ],
    "pull_quote": "A profitable equipment sale ends with an accepted serial, defensible evidence, and cash that survives reconciliation.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Assign the diagnostic, surgical/veterinary, and aesthetic plays to one two-full-time, four-contractor pod with explicit ticket-hour limits.",
        "Create serial-level intake records linking seller authority, service history, contamination handling, media treatment, and buyer demand.",
        "Concatenate the six reference modules in an isolated test environment and verify cohort replay, payload conflicts, competing versions, and notification deduplication.",
        "Define device-specific technical release and contractual acceptance requirements before bidding or promising shipment.",
        "Reconcile the worked quarter to $256,250 revenue, $41,000 profit, $131,000 closing cash, $45,000 inventory, and $15,000 receivables.",
        "Close each month against physical counts, bank receipts, source documents, actual contractor capacity, and unresolved warranty or damage claims.",
    ],
    "statutory_citations": [
        {
            "title": "21 CFR 807.20 — Establishment registration and device listing applicability",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-B/section-807.20",
            "relevance": (
                "Determine whether actual manufacturing, processing, importing, or other covered "
                "activities trigger registration and listing; do not assign one regulatory role "
                "to every equipment reseller."
            ),
        },
        {
            "title": "21 CFR 820.10 — Requirements for a quality management system",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/subpart-A/section-820.10",
            "relevance": (
                "Assess quality-system obligations when the operator's activities place it within "
                "the covered manufacturer scope, including relevant remanufacturing activities."
            ),
        },
        {
            "title": "21 CFR 801.109 — Prescription devices",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-801/subpart-D/section-801.109",
            "relevance": (
                "Check applicable prescription-device labeling and sale conditions for the "
                "specific human-use device rather than treating every used unit as unrestricted merchandise."
            ),
        },
        {
            "title": "45 CFR 164.310(d) — Device and media controls",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": (
                "For regulated entities and applicable business associate operations, implement "
                "device and media controls addressing disposal, media reuse, movement, and accountability."
            ),
        },
        {
            "title": "45 CFR 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Where the equipment-handling relationship constitutes business associate activity, "
                "establish the required contractual safeguards and protected-information responsibilities."
            ),
        },
        {
            "title": "21 CFR 803.50 — Manufacturer reporting requirements",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-803/subpart-E/section-803.50",
            "relevance": (
                "When the operator falls within manufacturer reporting obligations, route qualifying "
                "death, serious-injury, and malfunction information through the applicable reporting process."
            ),
        },
        {
            "title": "California Commercial Code § 9315 — Secured party rights in collateral and proceeds",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=COM&sectionNum=9315.",
            "relevance": (
                "For transactions governed by this provision, evaluate continuing security interests "
                "and applicable exceptions; obtain appropriate release evidence rather than assuming "
                "physical possession establishes unencumbered title."
            ),
        },
    ],
}
