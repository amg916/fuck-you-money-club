from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "unclaimed-property-recovery-production-blueprint-and-90-day-cohort",
    "question_prompt": "How does an operator execute unclaimed property recovery end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Treasury Claim Packets, Statutory Finder Agreements, SQLite Fee Ledgers, Idempotent Posting & Seasoned-Cohort Cash Conversion",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #07 with an 85/100 "
        "Money-to-Manpower Score. This production blueprint connects 12 mapped plays "
        "to evidence collection, statutory finder agreements, treasury submissions, "
        "owner-directed distributions, and reconciled service fees. Annual owner net "
        "profit remains $15,000 Conservative, $95,625 Base, and $225,000 Scaled; client "
        "property never becomes operator revenue. Six executable reference modules "
        "serialize SQLite writes, bind retries to request fingerprints, and connect "
        "each invoice and receipt to balanced journal postings. A worked 90-day walk "
        "separates new intake from seasoned opening claims, explaining how seventeen "
        "$1,250 monthly fees support the Base run rate without pretending a new "
        "business collects immediately. Property-tax appeals remain a separately "
        "contracted adjacent service with licensed-local execution where required."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; client assets excluded",
            "note": "25% net margin; $15,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees; client assets excluded",
            "note": "37.5% net margin; $95,625 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees; client assets excluded",
            "note": "50% net margin; $225,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Convert twelve recovery routes into evidence-backed production lanes",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with the administering treasury, not a purchased list promising instant "
                    "recoveries. Download permitted state search results or holder records, preserve "
                    "the retrieval date and source locator, and assign one internal case to each "
                    "jurisdiction/property identifier. A name match is a lead, never proof of ownership. "
                    "The twelve routes below are this chapter's operational mapping, not twelve "
                    "independent revenue forecasts: eleven address recovery evidence patterns and one "
                    "addresses an adjacent tax-appeal service. California Code of Civil Procedure "
                    "sections 1540 and 1582 illustrate why claim authority and finder compensation "
                    "must be checked separately. Record the applicable agreement restrictions, fee "
                    "ceiling, waiting interval, registration requirements, and version date before "
                    "outreach progresses into engagement. Explain that the owner can claim directly "
                    "through the administering agency without hiring the service. Offer a plain "
                    "description of the work purchased: locating records, resolving discrepancies, "
                    "assembling evidence, and tracking requests. Never imply treasury affiliation. "
                    "For the Base illustration, a successful case releases $12,500 to its owner "
                    "and earns a separately collectible $1,250 service fee where that ten-percent "
                    "arrangement is permitted. That distinction follows the case through every screen."
                ),
                (
                    "Build evidence requirements around the ownership chain rather than one universal "
                    "upload form. An individual may need a former-address connection; a renamed "
                    "company may need amendments and merger documents; an estate may require current "
                    "appointment papers and the agency's specific claimant process. Corporate uncashed "
                    "warrants require an additional question: is the item still payable by the issuing "
                    "agency, already transferred to a treasury, or subject to a separate reissue "
                    "procedure? A stale payment image alone does not settle that question. Use the "
                    "official corporate registry, county recorder, issuing controller, and treasury "
                    "claim portal as distinct sources. Store sensitive documents in an encrypted "
                    "document repository with individual access grants; the ledger stores opaque "
                    "evidence references rather than identity-document contents. Ask only for "
                    "documents needed for the particular claim, and remove rejected prospect "
                    "documents under a documented retention schedule. Escalate competing heirs, "
                    "conflicting corporate successors, and uncertain signatures instead of converting "
                    "a matching score into authorization. The economic stop is equally concrete: "
                    "a $300 property at ten percent yields $30 before labor, so direct the owner "
                    "to self-service unless lawful aggregation makes the work economical."
                ),
                (
                    "The mapped adjacent play property_tax_assessment_appeal_contingency begins when "
                    "the county releases annual assessment notices and valuation rolls. Ingest parcel "
                    "identifiers, assessed values, building characteristics, exemptions, and comparable "
                    "sales or neighborhood equity ratios. An automated valuation model flags apparent "
                    "overassessment; a qualified reviewer checks comparability, valuation date, "
                    "jurisdictional appeal grounds, and filing authority before any protest. A "
                    "$500,000 assessment reduction at an illustrative two-percent effective tax rate "
                    "produces $10,000 of first-year tax reduction. A lawful contract charging thirty "
                    "to fifty percent of the verified reduction produces $3,000 to $5,000 in fees; "
                    "a $1,000 local representation cost leaves $2,000 to $4,000 before other expenses. "
                    "Keep those fees outside the unclaimed-property scorecard and outside the cohort "
                    "below. Texas Occupations Code Chapter 1152 supplies a concrete registration "
                    "screen, while Texas Tax Code section 41.44 supplies protest deadlines that must "
                    "be calculated from the actual notice and applicable exception. The fallback "
                    "is a licensed local consultant or attorney of record where required, using "
                    "reviewed pre-deadline batch electronic filings only where the county supports "
                    "them. A missed deadline or weak comparable set cancels that parcel's production slot."
                ),
            ],
            "table": {
                "caption": "Twelve Mapped Production Routes: Evidence, Unit Economics & Failure Fallbacks",
                "headers": [
                    "Mapped operating route",
                    "Evidence and production mechanics",
                    "Unit economics and accounting boundary",
                    "Failure trigger and concrete fallback",
                ],
                "rows": [
                    [
                        "Individual owner recovery using former residential addresses",
                        "Connect treasury property identifiers to dated address evidence and verified claimant identity.",
                        "$12,500 released property supports a permitted $1,250 fee, never $12,500 operator revenue.",
                        "Conflicting identity evidence stops engagement; send the owner the official direct-claim route.",
                    ],
                    [
                        "Name-change recovery supported by documented identity continuity",
                        "Join former and current names through accepted marriage, court, or agency records.",
                        "Keep the same $1,250 fee assumption only when extra documentation preserves case margin.",
                        "An unsupported surname connection requires additional evidence, not a higher matching score.",
                    ],
                    [
                        "Estate recovery through an authorized personal representative",
                        "Verify appointment scope, estate identifiers, agency instructions, and each necessary ownership link.",
                        "Budget specialist document costs before accepting a fee dependent on eventual distribution.",
                        "Contested authority moves to estate counsel; suspend collection activity until authority resolves.",
                    ],
                    [
                        "Active corporate recovery with current signing authority",
                        "Match company identifiers, historical addresses, treasury records, and authorized officer documentation.",
                        "Aggregate eligible company properties while separately preserving each property's recovery and fee trail.",
                        "An employee's email alone cannot establish signing authority; obtain the required corporate evidence.",
                    ],
                    [
                        "Corporate successor recovery after merger or dissolution",
                        "Trace original owner through merger filings, assignments, dissolution records, and authorized successors.",
                        "Price lengthy successor reconstruction against expected lawful fees before commissioning paid record retrieval.",
                        "An incomplete succession chain requires specialist review rather than speculative ownership assertions.",
                    ],
                    [
                        "Corporate uncashed warrant recovery from issuing agencies",
                        "Determine whether the issuing controller retains liability or transferred the warrant to treasury.",
                        "Recognize only the contracted service fee after the qualifying recovery event actually occurs.",
                        "If the issuer still controls payment, follow its reissue process instead of duplicate treasury filing.",
                    ],
                    [
                        "Vendor overpayment recovery from holder and treasury records",
                        "Reconcile vendor account credits, remittance histories, original payee names, and transferred property identifiers.",
                        "Compare expected fee yield against statement-reconstruction hours and paid archival document charges.",
                        "Disputed commercial credits remain outside uncontested recovery production until the underlying balance resolves.",
                    ],
                    [
                        "Payroll property recovery for verified former employees",
                        "Connect employer payroll records, owner identity, reporting periods, and the official property entry.",
                        "Small balances ordinarily favor direct claiming unless permitted aggregation covers actual service costs.",
                        "Never request payroll portal passwords; use owner-provided records and agency-accepted evidence instead.",
                    ],
                    [
                        "Securities cash-proceeds recovery with distribution-history review",
                        "Determine whether treasury holds cash proceeds, securities, or another property form before valuation.",
                        "Use actual recoverable proceeds for fee calculations, not an assumed current share quotation.",
                        "Disputed liquidation values require agency clarification before presenting any recovery estimate to owners.",
                    ],
                    [
                        "Utility and tenancy deposit recovery with occupancy evidence",
                        "Match historical service addresses, account names, occupancy dates, and the property reporting entity.",
                        "A $300 deposit yields only $30 at ten percent, usually favoring self-service.",
                        "Unclear tenant allocation or joint ownership requires allocation evidence before preparing a claim.",
                    ],
                    [
                        "Multi-state corporate recovery with duplicate-property suppression",
                        "Normalize legal entities while preserving distinct state property identifiers and independent claim authority.",
                        "Batch document reuse reduces effort without combining client principal with recognized service revenue.",
                        "Potential duplicate reporting requires holder clarification before counting multiple anticipated fee opportunities.",
                    ],
                    [
                        "property_tax_assessment_appeal_contingency — annual notice and valuation-roll production",
                        "Ingest county rolls, flag AVM equity outliers, review comparables, and batch authorized protests.",
                        "$10,000 verified first-year savings yields $3,000–$5,000 fees before licensed-local representation costs.",
                        "Use licensed local consultants or attorneys where required; exclude unsupported parcels before deadlines.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four ways experienced recovery operators protect throughput",
                "body": "The largest gains come from better evidence routing and fewer false starts, not more indiscriminate outreach.",
                "items": [
                    "Ask the issuing controller whether a corporate warrant was transferred before investing in a treasury packet; record the answer and contact date.",
                    "Maintain an accepted-document checklist for each treasury and claimant type; reuse the checklist, never another owner's documents.",
                    "Offer direct-claim instructions with the first substantive proposal; measure signed engagements after that disclosure rather than counting pressured signatures.",
                    "Refresh corporate registry evidence near submission because a changed officer or dissolved entity can invalidate an otherwise complete packet.",
                ],
            },
        },
        {
            "heading": "2. Install the six-module ledger and make every local write replay-safe",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The six modules form one copy-pasteable Python reference program: concatenate "
                    "their code cells in order and run them with Python 3.9 or later. They use "
                    "only SQLite and the standard library, create a local recovery.sqlite3 file, "
                    "and expose functions rather than initiating treasury requests. Execute them "
                    "first against a disposable database; this chapter supplies reference source, "
                    "not a report of executed tests. The design assumes one trusted application "
                    "service owns database writes, local storage implements SQLite locking "
                    "correctly, and each worker opens its own connection. Do not place the live "
                    "database on an ordinary network filesystem. BEGIN IMMEDIATE serializes "
                    "writers before they inspect state; unique property keys, unique receipt "
                    "references, and immutable accounting rows provide additional barriers. A "
                    "busy timeout produces an explicit failure rather than permission to skip "
                    "locking. Each operation stores a canonical request fingerprint and response "
                    "inside the same transaction as its changes. Repeating the same operation "
                    "returns its recorded result; reusing its key with different input fails. "
                    "These mechanisms remove check-then-write races within this local ledger "
                    "under the stated deployment boundaries."
                ),
                (
                    "Keep the state machine narrower than the marketing funnel. INTAKE becomes "
                    "VERIFIED only after identity, authority, current jurisdiction rules, and a "
                    "permitted agreement have been checked outside the scoring function. FILED "
                    "requires an official submission reference, APPROVED requires agency evidence, "
                    "and OWNER_PAID requires evidence that the owner actually received the property. "
                    "The reference stores that evidence's opaque identifier and writes a permanent "
                    "transition record. ESCROW_REVIEW is an exception state, not an escrow account: "
                    "the business does not receive, pool, or redistribute client principal. Its "
                    "only exit returns to VERIFIED after documented resolution, requiring later "
                    "filing stages to be established again. If a matter genuinely requires custody "
                    "or escrow, route it to a separately authorized provider and keep it out of "
                    "this payment workflow. The scoring script ranks expected effort using "
                    "nonnegative integer cents and evidence indicators; it cannot establish "
                    "ownership or waive a statutory restriction. Reject oversized integers, "
                    "empty identifiers, and contradictory duplicate property records before "
                    "they enter the working queue. A low score influences priority, not the "
                    "legal validity of someone's claim."
                ),
                (
                    "Invoice creation is permitted only after OWNER_PAID, using the fee frozen "
                    "at intake and confirmed during verification. That recognition rule assumes "
                    "a contract whose recovery service is earned at this documented event; "
                    "contracts with materially different performance terms need a separately "
                    "reviewed accounting rule. Database triggers create the receivable/revenue "
                    "posting and move the case to INVOICED atomically. A full bank receipt "
                    "creates the bank/receivable posting and moves it to SETTLED. Each journal "
                    "row contains one equal debit-credit pair, so the reference cannot create "
                    "an internally unbalanced posting. Invoice and receipt tables are immutable, "
                    "and their unique constraints prevent a second invoice or settlement for "
                    "the same case. The intentionally narrow model accepts one full fee "
                    "payment, not partial payments, refunds, credit notes, write-offs, or "
                    "multi-invoice remittances. Route those exceptions to a separately designed "
                    "accounting workflow rather than editing history. Use posted bank references, "
                    "not emailed payment screenshots. Processor fees are separate expenses, "
                    "never an unexplained reduction of recognized fees or an excuse to mark "
                    "a short receipt as full settlement."
                ),
                (
                    "Reconciliation is a three-way comparison: the signed fee schedule and owner "
                    "distribution evidence support the invoice; the invoice supports the journal; "
                    "the posted bank transaction supports the receipt. The view reports fee "
                    "revenue, bank collections, and outstanding receivables by claim, while the "
                    "QA module checks referential integrity, amount consistency, and accounting "
                    "state. Those checks cannot authenticate a forged document or prove that "
                    "a bank reference was independently reviewed. Keep reviewer identity and "
                    "source evidence in the protected case system, and resolve every exception "
                    "before reporting collectible cash. Treasury portals also sit outside the "
                    "database transaction. Without a documented agency idempotency mechanism, "
                    "exactly-once external submission cannot be promised: use one designated "
                    "submitter per case, preserve submission receipts, and investigate an "
                    "uncertain response before retrying. Never automatically repeat a filing "
                    "because a browser timed out. Test parallel duplicate intake, repeated "
                    "receipt delivery, conflicting operation payloads, and interrupted commits "
                    "in an isolated environment before deployment. The reference ledger covers "
                    "service-fee receivables and receipts; payroll, contractor costs, taxes, "
                    "and financing remain in the operator's complete accounting system."
                ),
            ],
            "table": {
                "caption": "Six-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and invariant",
                    "Copy-pasteable Python and SQL source",
                    "Deployment boundary and operator acceptance check",
                ],
                "rows": [
                    [
                        "Module 1 — constrained schema and serialized transactional operation wrapper",
                        """import hashlib
import json
import sqlite3
import uuid

MAX_CENTS = 10 ** 12

SCHEMA = '''
CREATE TABLE IF NOT EXISTS claims (
    claim_id TEXT PRIMARY KEY,
    jurisdiction TEXT NOT NULL,
    property_key TEXT NOT NULL,
    owner_key TEXT NOT NULL,
    face_cents INTEGER NOT NULL CHECK (
        typeof(face_cents) = 'integer' AND face_cents > 0
        AND face_cents <= 1000000000000
    ),
    fee_cents INTEGER NOT NULL CHECK (
        typeof(fee_cents) = 'integer' AND fee_cents > 0
        AND fee_cents <= face_cents
    ),
    score INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    state TEXT NOT NULL CHECK (state IN (
        'INTAKE', 'VERIFIED', 'FILED', 'APPROVED', 'OWNER_PAID',
        'INVOICED', 'SETTLED', 'SCRUBBED', 'ESCROW_REVIEW'
    )),
    UNIQUE (jurisdiction, property_key)
);
CREATE TABLE IF NOT EXISTS operations (
    operation_key TEXT PRIMARY KEY,
    fingerprint TEXT NOT NULL,
    result_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS transitions (
    transition_id INTEGER PRIMARY KEY,
    operation_key TEXT NOT NULL UNIQUE,
    claim_id TEXT NOT NULL REFERENCES claims(claim_id),
    previous_state TEXT NOT NULL,
    next_state TEXT NOT NULL,
    evidence_key TEXT NOT NULL,
    UNIQUE (claim_id, operation_key)
);
CREATE TABLE IF NOT EXISTS invoices (
    invoice_id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL UNIQUE REFERENCES claims(claim_id),
    amount_cents INTEGER NOT NULL CHECK (
        typeof(amount_cents) = 'integer' AND amount_cents > 0
    )
);
CREATE TABLE IF NOT EXISTS receipts (
    receipt_id TEXT PRIMARY KEY,
    invoice_id TEXT NOT NULL UNIQUE REFERENCES invoices(invoice_id),
    bank_account_key TEXT NOT NULL,
    bank_reference TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK (
        typeof(amount_cents) = 'integer' AND amount_cents > 0
    ),
    UNIQUE (bank_account_key, bank_reference)
);
CREATE TABLE IF NOT EXISTS journal (
    posting_key TEXT PRIMARY KEY,
    invoice_id TEXT NOT NULL REFERENCES invoices(invoice_id),
    debit_account TEXT NOT NULL,
    credit_account TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK (
        typeof(amount_cents) = 'integer' AND amount_cents > 0
    ),
    CHECK (
        (debit_account = 'receivable' AND credit_account = 'fee_revenue')
        OR (debit_account = 'bank' AND credit_account = 'receivable')
    ),
    UNIQUE (invoice_id, debit_account, credit_account)
);
CREATE TRIGGER IF NOT EXISTS claim_identity_frozen
BEFORE UPDATE OF jurisdiction, property_key, owner_key, face_cents, fee_cents
ON claims
BEGIN
    SELECT RAISE(ABORT, 'Create a reviewed correction workflow');
END;
CREATE TRIGGER IF NOT EXISTS invoice_guard
BEFORE INSERT ON invoices
BEGIN
    SELECT CASE WHEN NOT EXISTS (
        SELECT 1 FROM claims
        WHERE claim_id = NEW.claim_id
          AND state = 'OWNER_PAID'
          AND fee_cents = NEW.amount_cents
    ) THEN RAISE(ABORT, 'Invoice requires paid owner and exact fee') END;
END;
CREATE TRIGGER IF NOT EXISTS invoice_post
AFTER INSERT ON invoices
BEGIN
    INSERT INTO journal VALUES (
        'invoice:' || NEW.invoice_id, NEW.invoice_id,
        'receivable', 'fee_revenue', NEW.amount_cents
    );
    UPDATE claims SET state = 'INVOICED' WHERE claim_id = NEW.claim_id;
END;
CREATE TRIGGER IF NOT EXISTS receipt_guard
BEFORE INSERT ON receipts
BEGIN
    SELECT CASE WHEN NOT EXISTS (
        SELECT 1 FROM invoices i JOIN claims c ON c.claim_id = i.claim_id
        WHERE i.invoice_id = NEW.invoice_id
          AND i.amount_cents = NEW.amount_cents
          AND c.state = 'INVOICED'
    ) THEN RAISE(ABORT, 'Receipt requires open invoice and full fee') END;
END;
CREATE TRIGGER IF NOT EXISTS receipt_post
AFTER INSERT ON receipts
BEGIN
    INSERT INTO journal VALUES (
        'receipt:' || NEW.receipt_id, NEW.invoice_id,
        'bank', 'receivable', NEW.amount_cents
    );
    UPDATE claims SET state = 'SETTLED'
    WHERE claim_id = (
        SELECT claim_id FROM invoices WHERE invoice_id = NEW.invoice_id
    );
END;
'''

def open_database(path):
    connection = sqlite3.connect(path, timeout=30, isolation_level=None)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA journal_mode = WAL")
    connection.execute("PRAGMA synchronous = FULL")
    connection.executescript(SCHEMA)
    for table in ("operations", "transitions", "invoices", "receipts", "journal"):
        for action in ("UPDATE", "DELETE"):
            trigger = table + "_block_" + action.lower()
            sql = (
                "CREATE TRIGGER IF NOT EXISTS " + trigger
                + " BEFORE " + action + " ON " + table
                + " BEGIN SELECT RAISE(ABORT, 'Append-only record'); END;"
            )
            connection.execute(sql)
    return connection

db = open_database("recovery.sqlite3")

def required_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("A nonempty string is required")
    return value.strip()

def cents(value):
    if type(value) is not int or not 0 < value <= MAX_CENTS:
        raise ValueError("Use positive bounded integer cents")
    return value

def atomic(operation_key, payload, work):
    operation_key = required_text(operation_key)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    fingerprint = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    db.execute("BEGIN IMMEDIATE")
    try:
        prior = db.execute(
            "SELECT fingerprint, result_json FROM operations WHERE operation_key = ?",
            (operation_key,),
        ).fetchone()
        if prior is not None:
            if prior["fingerprint"] != fingerprint:
                raise ValueError("Operation key was reused with different input")
            result = json.loads(prior["result_json"])
        else:
            result = work()
            db.execute(
                "INSERT INTO operations VALUES (?, ?, ?)",
                (operation_key, fingerprint, json.dumps(result, sort_keys=True)),
            )
        db.execute("COMMIT")
        return result
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
""",
                        "Use local durable storage, one connection per worker, and a single trusted application writer boundary.",
                    ],
                    [
                        "Module 2 — deterministic intake scoring with duplicate-property conflict detection",
                        """def intake(operation_key, jurisdiction, property_key, owner_key,
           face_cents, fee_cents, address_match, entity_match):
    jurisdiction = required_text(jurisdiction).upper()
    property_key = required_text(property_key)
    owner_key = required_text(owner_key)
    face_cents = cents(face_cents)
    fee_cents = cents(fee_cents)
    if fee_cents > face_cents:
        raise ValueError("Fee exceeds property value")
    if type(address_match) is not bool or type(entity_match) is not bool:
        raise ValueError("Evidence indicators must be boolean")
    score = (
        40 * int(address_match)
        + 40 * int(entity_match)
        + 20 * int(fee_cents >= 100000)
    )
    payload = {
        "kind": "intake", "jurisdiction": jurisdiction,
        "property_key": property_key, "owner_key": owner_key,
        "face_cents": face_cents, "fee_cents": fee_cents,
        "address_match": address_match, "entity_match": entity_match,
    }

    def work():
        existing = db.execute(
            "SELECT * FROM claims WHERE jurisdiction = ? AND property_key = ?",
            (jurisdiction, property_key),
        ).fetchone()
        if existing is not None:
            expected = (owner_key, face_cents, fee_cents)
            actual = (
                existing["owner_key"], existing["face_cents"],
                existing["fee_cents"],
            )
            if actual != expected:
                raise ValueError("Duplicate property has conflicting ownership or amounts")
            return {"claim_id": existing["claim_id"], "created": False}
        claim_id = uuid.uuid4().hex
        db.execute(
            "INSERT INTO claims VALUES (?, ?, ?, ?, ?, ?, ?, 'INTAKE')",
            (claim_id, jurisdiction, property_key, owner_key,
             face_cents, fee_cents, score),
        )
        return {"claim_id": claim_id, "created": True}

    return atomic(operation_key, payload, work)
""",
                        "Normalize source identifiers before calling intake; matching scores rank review effort without authorizing claims.",
                    ],
                    [
                        "Module 3 — verification and escrow-exception state machine with permanent evidence references",
                        """ALLOWED_TRANSITIONS = {
    "INTAKE": {"VERIFIED", "SCRUBBED", "ESCROW_REVIEW"},
    "VERIFIED": {"FILED", "SCRUBBED", "ESCROW_REVIEW"},
    "FILED": {"APPROVED", "SCRUBBED", "ESCROW_REVIEW"},
    "APPROVED": {"OWNER_PAID", "SCRUBBED", "ESCROW_REVIEW"},
    "ESCROW_REVIEW": {"VERIFIED", "SCRUBBED"},
}

def transition(operation_key, claim_id, next_state, evidence_key):
    operation_key = required_text(operation_key)
    claim_id = required_text(claim_id)
    next_state = required_text(next_state)
    evidence_key = required_text(evidence_key)
    payload = {
        "kind": "transition", "claim_id": claim_id,
        "next_state": next_state, "evidence_key": evidence_key,
    }

    def work():
        row = db.execute(
            "SELECT state FROM claims WHERE claim_id = ?", (claim_id,)
        ).fetchone()
        if row is None:
            raise ValueError("Claim does not exist")
        previous = row["state"]
        if next_state not in ALLOWED_TRANSITIONS.get(previous, set()):
            raise ValueError("State transition is not permitted")
        db.execute(
            "INSERT INTO transitions "
            "(operation_key, claim_id, previous_state, next_state, evidence_key) "
            "VALUES (?, ?, ?, ?, ?)",
            (operation_key, claim_id, previous, next_state, evidence_key),
        )
        db.execute(
            "UPDATE claims SET state = ? WHERE claim_id = ?",
            (next_state, claim_id),
        )
        return {"claim_id": claim_id, "state": next_state}

    return atomic(operation_key, payload, work)
""",
                        "Evidence references must resolve to reviewed records; ESCROW_REVIEW holds the workflow, never client funds.",
                    ],
                    [
                        "Module 4 — atomic fee invoicing and full-receipt posting with independent bank uniqueness",
                        """def invoice(operation_key, claim_id):
    claim_id = required_text(claim_id)
    payload = {"kind": "invoice", "claim_id": claim_id}

    def work():
        prior = db.execute(
            "SELECT invoice_id FROM invoices WHERE claim_id = ?", (claim_id,)
        ).fetchone()
        if prior is not None:
            return {"invoice_id": prior["invoice_id"]}
        claim = db.execute(
            "SELECT fee_cents FROM claims WHERE claim_id = ?", (claim_id,)
        ).fetchone()
        if claim is None:
            raise ValueError("Claim does not exist")
        invoice_id = uuid.uuid4().hex
        db.execute(
            "INSERT INTO invoices VALUES (?, ?, ?)",
            (invoice_id, claim_id, claim["fee_cents"]),
        )
        return {"invoice_id": invoice_id}

    return atomic(operation_key, payload, work)

def receive(operation_key, invoice_id, bank_account_key,
            bank_reference, amount_cents):
    invoice_id = required_text(invoice_id)
    bank_account_key = required_text(bank_account_key)
    bank_reference = required_text(bank_reference)
    amount_cents = cents(amount_cents)
    payload = {
        "kind": "receive", "invoice_id": invoice_id,
        "bank_account_key": bank_account_key,
        "bank_reference": bank_reference, "amount_cents": amount_cents,
    }

    def work():
        prior = db.execute(
            "SELECT * FROM receipts "
            "WHERE bank_account_key = ? AND bank_reference = ?",
            (bank_account_key, bank_reference),
        ).fetchone()
        if prior is not None:
            if (prior["invoice_id"], prior["amount_cents"]) != (
                invoice_id, amount_cents
            ):
                raise ValueError("Bank reference conflicts with an existing receipt")
            return {"receipt_id": prior["receipt_id"]}
        receipt_id = uuid.uuid4().hex
        db.execute(
            "INSERT INTO receipts VALUES (?, ?, ?, ?, ?)",
            (receipt_id, invoice_id, bank_account_key,
             bank_reference, amount_cents),
        )
        return {"receipt_id": receipt_id}

    return atomic(operation_key, payload, work)
""",
                        "Accept independently reviewed posted bank credits only; route partial payments and reversals outside this narrow workflow.",
                    ],
                    [
                        "Module 5 — claim-level revenue, bank, and receivable reconciliation view",
                        """db.executescript('''
CREATE VIEW IF NOT EXISTS fee_reconciliation AS
SELECT
    c.claim_id,
    c.jurisdiction,
    c.property_key,
    c.state,
    i.invoice_id,
    COALESCE(i.amount_cents, 0) AS invoice_cents,
    COALESCE(r.amount_cents, 0) AS receipt_cents,
    COALESCE(j.revenue_cents, 0) AS revenue_cents,
    COALESCE(j.bank_cents, 0) AS bank_cents,
    COALESCE(j.receivable_cents, 0) AS receivable_cents
FROM claims c
LEFT JOIN invoices i ON i.claim_id = c.claim_id
LEFT JOIN receipts r ON r.invoice_id = i.invoice_id
LEFT JOIN (
    SELECT
        invoice_id,
        SUM(CASE WHEN credit_account = 'fee_revenue'
                 THEN amount_cents ELSE 0 END) AS revenue_cents,
        SUM(CASE WHEN debit_account = 'bank'
                 THEN amount_cents ELSE 0 END) AS bank_cents,
        SUM(CASE
            WHEN debit_account = 'receivable' THEN amount_cents
            WHEN credit_account = 'receivable' THEN -amount_cents
            ELSE 0 END) AS receivable_cents
    FROM journal
    GROUP BY invoice_id
) j ON j.invoice_id = i.invoice_id;
''')

def reconciliation_rows():
    return [
        dict(row) for row in db.execute(
            "SELECT * FROM fee_reconciliation ORDER BY claim_id"
        )
    ]
""",
                        "Compare this service-fee subledger with bank statements and the complete operating ledger before closing each month.",
                    ],
                    [
                        "Module 6 — snapshot-consistent structural and accounting QA checks",
                        """def quality_checks():
    db.execute("BEGIN")
    try:
        integrity = db.execute("PRAGMA integrity_check").fetchall()
        if [row[0] for row in integrity] != ["ok"]:
            raise RuntimeError("SQLite integrity check failed")
        if db.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("Foreign-key check failed")
        failures = db.execute('''
            SELECT claim_id FROM fee_reconciliation
            WHERE revenue_cents != invoice_cents
               OR bank_cents != receipt_cents
               OR receivable_cents != invoice_cents - receipt_cents
               OR receivable_cents < 0
               OR (state = 'SETTLED' AND (
                   invoice_cents = 0 OR receipt_cents != invoice_cents
               ))
               OR (state = 'INVOICED' AND (
                   invoice_cents = 0 OR receipt_cents != 0
               ))
               OR (invoice_cents > 0 AND state NOT IN ('INVOICED', 'SETTLED'))
        ''').fetchall()
        if failures:
            raise RuntimeError("Claim accounting reconciliation failed")
        missing_operations = db.execute('''
            SELECT t.transition_id
            FROM transitions t
            LEFT JOIN operations o ON o.operation_key = t.operation_key
            WHERE o.operation_key IS NULL
        ''').fetchall()
        if missing_operations:
            raise RuntimeError("Transition operation evidence is incomplete")
        totals = dict(db.execute('''
            SELECT
                COALESCE(SUM(revenue_cents), 0) AS revenue_cents,
                COALESCE(SUM(bank_cents), 0) AS bank_cents,
                COALESCE(SUM(receivable_cents), 0) AS receivable_cents
            FROM fee_reconciliation
        ''').fetchone())
        db.execute("COMMIT")
        return totals
    except BaseException:
        if db.in_transaction:
            db.execute("ROLLBACK")
        raise
""",
                        "Run read-only checks against a consistent snapshot, then separately verify evidence authenticity and duplicate-delivery behavior.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before a case leaves verification",
                "body": "An automated match can propose work; only documented authority, permissible terms, and a reviewed packet can justify submission.",
                "items": [
                    "Verify claimant identity and the complete authority chain against the agency's accepted evidence requirements; resolve joint-owner and successor conflicts.",
                    "Attach a dated jurisdiction rules sheet covering registration, finder compensation, waiting restrictions, required contract language, and direct-claim disclosure.",
                    "Confirm that the treasury will distribute property directly to the owner and that the signed fee schedule matches the ledger's integer-cent amount.",
                    "Check the official property identifier, prior filing history, packet version, assigned submitter, and portal receipt procedure before sending any documents.",
                ],
            },
        },
        {
            "heading": "3. Run intake, submission, collection, and close as four accountable handoffs",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Assign the Base team as one full-time operator plus two contractors, not "
                    "three interchangeable generalists. The operator owns client relationships, "
                    "jurisdiction decisions, exception disposition, and monthly close. One contractor "
                    "normalizes public records and assembles evidence requests; the other reviews "
                    "packet completeness and monitors agency correspondence under limited access. "
                    "Neither contractor needs unrestricted identity-document exports or authority "
                    "to change payout instructions. In a sixty-lead monthly cohort, remove twelve "
                    "duplicate or previously resolved records, eighteen identity or authority "
                    "mismatches, and ten cases whose lawful fee cannot support production cost. "
                    "That leaves twenty qualified files. Reserve three further losses for "
                    "withdrawals, agency denials, or unresolved evidence, producing seventeen "
                    "eventual paid fees in the illustration. These are mutually exclusive "
                    "outcome buckets, not overlapping rejection percentages. Record the actual "
                    "reason and date for each exit so acquisition quality can be measured by "
                    "source and claimant type. Avoid replacing a missing document with an "
                    "optimistic probability. A queue should contain a next action, named "
                    "responsible role, and evidence deadline; otherwise its aging report merely "
                    "counts neglected cases rather than controllable work."
                ),
                (
                    "After engagement, assemble one versioned packet manifest showing each requested "
                    "document, repository reference, reviewer, and official submission identifier. "
                    "Check the current treasury instructions immediately before filing because "
                    "forms and acceptable evidence can change between prospecting and submission. "
                    "Use the agency's secure upload method where offered; keep passwords, "
                    "authentication codes, and complete identity numbers out of shared task "
                    "notes. Status tracking can poll a permitted API or generate reminders "
                    "for manual portal review, but it should not bypass access controls or "
                    "treat a missing response as a denial. Set internal follow-up intervals "
                    "from the agency's published process and the case's last substantive "
                    "event, not from an invented universal payment deadline. Record each "
                    "request for additional evidence as a separate task tied to the original "
                    "claim. Before responding, verify that the requesting message actually "
                    "comes from the agency. A changed beneficiary, substituted bank account, "
                    "or request to route principal through the recovery business triggers "
                    "an exception review. Filing volume is a throughput metric; it is not "
                    "recognized revenue and cannot fund payroll before collections arrive."
                ),
                (
                    "Close the loop only after independently supporting both the owner's recovery "
                    "and the operator's receipt. The owner distribution record establishes the "
                    "contractual fee event in this model; the bank credit establishes cash. "
                    "If the owner has recovered property but has not paid the fee, show a "
                    "receivable and a collection task rather than deleting the invoice or "
                    "reporting settlement. Reconcile contract amount, invoice, bank reference, "
                    "and journal totals at least monthly, with a second reviewer checking "
                    "exceptions and changes to payment instructions. Distinguish fixed operating "
                    "overhead from variable delivery costs when comparing economics with the "
                    "scorecard. The Base walk uses $6,000 monthly fixed overhead, within the "
                    "stated $1,500–$8,000 monthly operating range, plus $7,281.25 of variable "
                    "case-delivery and collection costs. Total modeled monthly expense is "
                    "$13,281.25. The fixed bucket includes modeled operator compensation and "
                    "platform overhead; contractor effort and other delivery charges belong "
                    "in the variable bucket without double counting. Owner net profit is "
                    "the residual after those modeled expenses. Maintain invoice-level support "
                    "for the cost categories rather than presenting this illustrative allocation "
                    "as a quoted vendor budget."
                ),
            ],
            "table": {
                "caption": "Six Handoff Controls Connecting Source Evidence to Reconciled Service Cash",
                "headers": [
                    "Production handoff and responsible role",
                    "Required evidence before accepting the handoff",
                    "Specific failure signal requiring intervention",
                    "Recorded disposition and accounting treatment",
                ],
                "rows": [
                    [
                        "Research contractor hands normalized records to the operator",
                        "Preserve official source locator, extraction date, property identifier, and preliminary ownership connection.",
                        "The same state property appears under multiple imported records or incompatible claimant identities.",
                        "Merge duplicate leads into one case; retain conflicting evidence without creating duplicate fee forecasts.",
                    ],
                    [
                        "Operator hands authorized engagement to the packet contractor",
                        "Attach reviewed authority evidence, permissible agreement, direct-claim disclosure, and dated jurisdiction rules.",
                        "A registration requirement, waiting restriction, or disputed signature remains unresolved during preparation.",
                        "Hold submission work and document resolution; unsigned opportunities remain outside recognized service revenue.",
                    ],
                    [
                        "Packet contractor hands reviewed submission materials to the submitter",
                        "Provide the packet manifest, accepted-document checklist, agency form version, and owner authorization.",
                        "A required exhibit is missing or an agency identifier differs from the source property.",
                        "Return the packet with a specific correction task before any external document transmission.",
                    ],
                    [
                        "Designated submitter hands official filing evidence to status tracking",
                        "Save agency receipt, claim reference, submission timestamp, and the exact transmitted packet version.",
                        "The portal times out after submission without supplying a reliable acceptance or rejection result.",
                        "Investigate filing status before retrying; never manufacture a second filing to clear the queue.",
                    ],
                    [
                        "Operator hands confirmed owner distribution to the fee ledger",
                        "Retain distribution evidence and the contract calculation supporting the fixed collectible service amount.",
                        "The owner recovered a different amount or disputes whether the service fee was earned.",
                        "Resolve the discrepancy before invoicing through this fixed-fee reference; preserve every prior evidence version.",
                    ],
                    [
                        "Bookkeeping reviewer hands reconciled collections to monthly reporting",
                        "Match posted bank credit, unique receipt reference, invoice amount, and balanced journal entries.",
                        "The payment is partial, reversed, duplicated, or reduced by unexplained intermediary deductions.",
                        "Use a separately reviewed exception workflow; do not overwrite receipts or conceal open receivables.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Normalize and economically scrub the lead cohort",
                    "action": "Create one property case, verify source provenance, and assign an exclusive lead disposition.",
                    "detail": "For the worked cohort, reconcile sixty leads to twelve duplicates, eighteen mismatches, ten low-yield exits, and twenty qualified files.",
                },
                {
                    "step": 2,
                    "title": "Verify authority and submit the accepted packet",
                    "action": "Review the jurisdiction rules sheet, signed agreement, claimant authority, and agency-specific evidence manifest.",
                    "detail": "Store the official filing reference before moving to FILED; an uncertain portal response requires investigation rather than automatic resubmission.",
                },
                {
                    "step": 3,
                    "title": "Document distribution and create the earned fee",
                    "action": "Confirm owner-directed recovery, apply the contracted fee calculation, and create the invoice through the transactional function.",
                    "detail": "The illustrative $12,500 owner recovery supports a $1,250 service fee only where the agreement and jurisdiction permit that amount.",
                },
                {
                    "step": 4,
                    "title": "Match bank cash and close the reporting period",
                    "action": "Post the reviewed full fee receipt, run ledger QA, and reconcile the service-fee subledger to the complete accounts.",
                    "detail": "Keep open receivables separate from cash and include fixed overhead plus variable delivery costs before reporting owner net profit.",
                },
            ],
        },
        {
            "heading": "4. Walk a seasoned 90-day cohort without borrowing revenue from the future",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a steady-state illustration, not a "
                    "day-one startup forecast. Assume January through March constitute the "
                    "measurement window and that October, November, and December intake "
                    "cohorts already exist at opening. Each older cohort contains sixty "
                    "original leads with the same eventual disposition: twelve duplicates, "
                    "eighteen mismatches, ten uneconomic cases, three later losses, and "
                    "seventeen successful fee cases. The older cohorts mature one per "
                    "month during the window. January, February, and March intake repeats "
                    "the sixty-lead process, but their seventeen eventual successes are "
                    "planning estimates, not booked receivables. For illustration they "
                    "mature in April, May, and June respectively; actual treasury timing "
                    "can be longer. This respects the volume's three-to-twelve-month time "
                    "to first deal rather than promising collections during the first "
                    "ninety days of a new business. Opening operating cash is $35,000 "
                    "after any earlier setup spending, funded before the illustrated "
                    "window. That reserve is not revenue, and it should not be confused "
                    "with a claim that all prior startup costs and three months of "
                    "operations fit inside the same amount."
                ),
                (
                    "Each maturing cohort produces seventeen owner distributions of $12,500, "
                    "or $212,500 of client property, and seventeen $1,250 fees, or $21,250 "
                    "of recognized operator revenue. Assume owners receive their property "
                    "and pay their full fees within the same measurement month; ending "
                    "fee receivables are therefore zero in this particular walk. Monthly "
                    "fixed overhead of $6,000 plus variable costs of $7,281.25 produces "
                    "$13,281.25 of total expense and $7,968.75 of owner net profit. "
                    "Cumulative operating cash contribution is $7,968.75 after January, "
                    "$15,937.50 after February, and $23,906.25 after March. Adding the "
                    "opening reserve gives closing cash of $42,968.75, $50,937.50, and "
                    "$58,906.25. These balances assume no owner distributions, debt "
                    "service, new capital spending, or additional financing during the "
                    "window, and modeled expenses are paid in their respective months. "
                    "The table records new intake and old-cohort settlement separately "
                    "so the same seventeen successes cannot be counted twice. The "
                    "three later losses per cohort earn no fee, and their pursuit "
                    "cost is already inside the modeled operating expense rather than "
                    "silently omitted from margin."
                ),
                (
                    "Across ninety days, recognized fees total $63,750, operating expense "
                    "totals $39,843.75, and owner net profit totals $23,906.25. Multiplying "
                    "those steady-state quarterly figures by four produces exactly "
                    "$255,000 revenue, $159,375 expense, and $95,625 owner net profit: "
                    "the canonical 37.5-percent Base margin. Underlying client recoveries "
                    "total $637,500 during the quarter and $2,550,000 at the illustrated "
                    "annual cadence, but neither figure belongs in operator revenue. "
                    "The other scorecard cases remain separate: Conservative revenue "
                    "of $60,000 less $45,000 expense yields $15,000 profit at twenty-five "
                    "percent; Scaled revenue of $450,000 less $225,000 expense yields "
                    "$225,000 profit at fifty percent. Do not transplant Base lead "
                    "conversion into those cases without a new capacity model. Stress "
                    "the cash walk by delaying one month's fee receipts: $21,250 "
                    "moves from bank cash into receivables if recovery and earning "
                    "conditions are already satisfied. If the owner distribution "
                    "itself is delayed, fee recognition also moves. Continue paying "
                    "actual delivery costs, reforecast runway weekly, and reduce "
                    "discretionary acquisition before relying on uncertain treasury "
                    "payments to cover committed expenses."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Measurement month and separately identified cohort",
                    "Lead scrubs, downstream losses, and deal count",
                    "Client recovery and recognized service-fee timing",
                    "Operating expense and incremental cash treatment",
                    "Cumulative operating cash and closing reserve",
                ],
                "rows": [
                    [
                        "Month 1, January: newly acquired January intake cohort",
                        "Sixty leads less twelve duplicates, eighteen mismatches, and ten low-yield exits leaves twenty qualified files.",
                        "Three later losses and seventeen April successes are forecasts; January recognized revenue remains zero for this cohort.",
                        "Preparation effort is included in January's combined $13,281.25 operating expense, not charged twice.",
                        "No separate cash contribution is added for this intake cohort; use January's combined close below.",
                    ],
                    [
                        "Month 1, January: seasoned October opening cohort settles",
                        "The original sixty leads resolve into forty initial scrubs, three later losses, and seventeen paid fees.",
                        "$212,500 reaches owners; seventeen $1,250 fees produce $21,250 January revenue and collected cash.",
                        "$6,000 fixed overhead plus $7,281.25 variable cost leaves $7,968.75 January operating cash contribution.",
                        "Cumulative operating contribution reaches $7,968.75; the $35,000 opening reserve becomes $42,968.75 closing cash.",
                    ],
                    [
                        "Month 2, February: newly acquired February intake cohort",
                        "Sixty leads again leave twenty qualified files after twelve duplicates, eighteen mismatches, and ten low-yield exits.",
                        "Seventeen May successes remain forecast after three expected later losses; February revenue is zero here.",
                        "Preparation effort is included in February's combined $13,281.25 operating expense, without a second allocation.",
                        "No forecast fee enters bank cash; February's combined closing balance appears in the settlement row.",
                    ],
                    [
                        "Month 2, February: seasoned November opening cohort settles",
                        "Forty initial scrubs plus three later losses leave seventeen successful cases from sixty original leads.",
                        "Owners receive $212,500; seventeen collected $1,250 fees produce $21,250 of February recognized revenue.",
                        "February pays $13,281.25 total operating expense and adds $7,968.75 to cumulative operating cash.",
                        "Cumulative operating contribution reaches $15,937.50; cash including the opening reserve closes at $50,937.50.",
                    ],
                    [
                        "Month 3, March: newly acquired March intake cohort",
                        "Sixty leads produce twenty qualified files after forty initial scrubs; three later losses remain forecast.",
                        "Seventeen June successes are future planning cases; no March invoice or receipt is created for them.",
                        "Preparation effort belongs within March's combined $13,281.25 operating expense and is not added again.",
                        "Future service fees remain outside March cash; the settlement row supplies the combined quarter-end balance.",
                    ],
                    [
                        "Month 3, March: seasoned December opening cohort settles",
                        "Sixty original leads reconcile to forty initial scrubs, three later losses, and seventeen collected service fees.",
                        "$212,500 reaches owners; $21,250 March service revenue brings quarterly recognized fees to exactly $63,750.",
                        "March expense is $13,281.25; quarterly expense is $39,843.75 and quarterly owner profit is $23,906.25.",
                        "Cumulative operating contribution reaches $23,906.25; quarter-end cash including the reserve equals $58,906.25.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A recoverable asset becomes a business result only when ownership is proved, the fee is earned, and the bank receipt reconciles.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Publish a dated jurisdiction rules sheet covering finder registration, compensation restrictions, waiting intervals, accepted authority evidence, and direct-claim disclosure.",
        "Configure the twelve production routes while keeping property-tax appeals separately contracted, locally represented where required, and outside recovery scorecard revenue.",
        "Concatenate the six reference modules into an isolated test program and exercise duplicate intake, conflicting retries, concurrent receipts, and interrupted transactions before deployment.",
        "Assign one full-time operator and two contractors explicit evidence, submission, status-tracking, and reconciliation responsibilities with restricted document access.",
        "Build a sixty-lead cohort report with mutually exclusive dispositions and distinguish new intake forecasts from seasoned claims eligible for invoicing.",
        "Close monthly by reconciling owner recovery evidence, $1,250 illustrative fees, bank receipts, and total expenses against the $21,250 Base revenue cadence.",
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure § 1540 — Claims to property held by the Controller",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1540.&lawCode=CCP",
            "relevance": "Establishes the statutory claim route; use current Controller procedures to determine claimant evidence, authority, and claim handling.",
        },
        {
            "title": "California Code of Civil Procedure § 1582 — Agreements to locate or recover reported property",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1582.&lawCode=CCP",
            "relevance": "Review agreement timing restrictions, the ten-percent compensation ceiling, and required agreement content before accepting a California recovery engagement.",
        },
        {
            "title": "Florida Statutes § 717.135 — Recovery or purchase of unclaimed property",
            "url": "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0717/Sections/0717.135.html",
            "relevance": "Supplies jurisdiction-specific requirements for recovery agreements and compensation analysis; do not substitute another state's contract template.",
        },
        {
            "title": "Florida Statutes § 717.1400 — Registration",
            "url": "https://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0717/Sections/0717.1400.html",
            "relevance": "Check the registration framework applicable to representatives before preparing or submitting Florida recovery claims for clients.",
        },
        {
            "title": "Texas Occupations Code Chapter 1152 — Property Tax Consultants",
            "url": "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1152.htm",
            "relevance": "Determine registration requirements, exemptions, and permitted representation for the separately operated property-tax assessment appeal play.",
        },
        {
            "title": "Texas Tax Code § 41.44 — Notice of Protest",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.41.htm#41.44",
            "relevance": "Calculate protest filing deadlines from the applicable notice and statutory provisions before scheduling reviewed batch submissions.",
        },
    ],
}
