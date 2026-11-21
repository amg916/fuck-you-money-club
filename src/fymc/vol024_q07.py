from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "tax-lien-investing-complete-operating-process-production-blueprint",
    "question_prompt": "How does an operator execute tax lien investing end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "County Auction Intake, Florida Bid-Down Certificates, Texas Redemption Rights, SQLite Cash Controls, and Post-Tyler Recovery",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #3, Tax Lien Investing, ranks #24 with a Money-to-Manpower Score of "
        "62/100: capital and specialist judgment, rather than staffing alone, constrain "
        "the business. This chapter maps four operator plays: certificate screening, "
        "bid-down acquisition, redemption servicing, and redeemable-deed disposition. "
        "A one-full-time-plus-two-contractor pod executes them through documented county "
        "rules, reserved cash, immutable receipts, and a balanced SQLite ledger. The "
        "worked cohort separates returned principal from realized revenue and reconciles "
        "a seasoned portfolio to the Base annual run rate. Annual owner profit remains "
        "$4,500 Conservative, $41,438 Base, and $99,000 Scaled. A six-module reference "
        "implementation controls duplicate imports, competing reservations, receipt "
        "replays, and cash classification without pretending a new auction purchase "
        "reliably redeems within ninety days."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$15,000",
            "context": "Annual realized interest, penalties, and disposition gains; excludes returned principal.",
            "note": "30% net margin; $4,500 annual owner net profit; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$97,500",
            "context": "Annual realized interest, penalties, and disposition gains; excludes returned principal.",
            "note": "42.5% net margin; $41,438 rounded annual owner net profit; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$180,000",
            "context": "Annual realized interest, penalties, and disposition gains; excludes returned principal.",
            "note": "55% net margin; $99,000 annual owner net profit; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Route Every Parcel Through Four Explicit Operator Plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build one acquisition record per jurisdiction, parcel, instrument, and "
                    "tax vintage before anyone opens the bidding screen. The chapter's four "
                    "mapped plays are certificate screening, bid-down acquisition, redemption "
                    "servicing, and redeemable-deed disposition; they are work queues, not "
                    "interchangeable investment products. The full-time operator owns cash, "
                    "auction decisions, and exception resolution. Contractor one handles "
                    "parcel research and title evidence; contractor two is retained local "
                    "counsel for jurisdiction-specific procedure and contested recovery. "
                    "Use the county tax collector's official sale file as the intake "
                    "authority, the property appraiser's GIS for parcel geometry, and the "
                    "clerk's index for recorded instruments. Bid4Assets or RealAuction may "
                    "supply the auction interface where the county appoints them, but the "
                    "vendor screen does not replace the published county terms. Preserve "
                    "each downloaded artifact with its retrieval timestamp, source URL, "
                    "and SHA-256 digest. Record whether the asset is a certificate, a "
                    "redeemable deed, or a conventional tax deed. This classification "
                    "determines what the buyer owns, how proceeds arise, and which "
                    "deadlines matter. Reject an ambiguous classification rather than "
                    "letting a low opening bid substitute for a verified statutory path."
                ),
                (
                    "Convert the legal mechanism into an executable maximum bid. Florida "
                    "Statutes section 197.432 governs certificate sales and the interest "
                    "bid-down mechanism; section 197.472 governs redemption calculations, "
                    "including treatment that differs for zero-percent certificates. Do "
                    "not import a platform's advertised maximum rate into every cash-flow "
                    "forecast. For an illustrative $10,000 certificate bid at eight percent, "
                    "six months of simple interest would be $400 before applicable "
                    "statutory adjustments, acquisition charges, and collection costs. "
                    "The $10,000 returned investment is principal, not $10,000 of sales. "
                    "Texas Tax Code section 34.21 uses a different redemption structure "
                    "with property classifications, redemption periods, and statutory "
                    "premiums; a premium is not an annual coupon. Store the rule version "
                    "beside the instrument, then have counsel confirm the calculation "
                    "before capital is committed. Screening must also identify severed "
                    "mineral interests, unusable access, municipal demolition exposure, "
                    "bankruptcy, and environmental flags. Use a score to order research, "
                    "not to override a disqualifying fact. Reserve a separate legal and "
                    "carrying-cost cushion outside the certificate bid. A purchase that "
                    "requires perfect title, immediate redemption, and free enforcement "
                    "has failed underwriting even when the auction platform accepts it."
                ),
                (
                    "Treat recovery as a new decision rather than an automatic extension "
                    "of acquisition. A certificate does not itself convey the parcel. "
                    "Florida's tax-deed application procedure under section 197.502 has "
                    "its own timing, payments, and administrative steps. Texas deed "
                    "redemption requires a different calendar and documented calculation. "
                    "Place bankruptcy indicators into counsel's queue before collection "
                    "activity because 11 U.S.C. section 362 can stay relevant acts. "
                    "After Tyler v. Hennepin County, do not underwrite an entitlement "
                    "to keep every dollar of value above the enforceable tax debt. "
                    "The Supreme Court's surplus-equity holding requires attention to "
                    "the actual jurisdiction's recovery and distribution mechanism; "
                    "it does not turn every certificate into immediate ownership. "
                    "Counsel should document notice recipients, service evidence, "
                    "redemption status, surplus treatment, and permitted disposition "
                    "before the operator selects a recovery route. The three-person "
                    "pod therefore caps active files by unresolved title and notice "
                    "exceptions, not by how many parcels an import script can load. "
                    "Close each week with three queues: capital eligible for auction, "
                    "owned instruments awaiting a documented event, and disputed files "
                    "requiring professional action. Never mix those queues merely "
                    "to make the acquisition dashboard look productive."
                ),
            ],
            "table": {
                "caption": "Four-Play Intake, Statutory Routing, and Three-Person Pod Responsibility Matrix",
                "headers": [
                    "Operating checkpoint",
                    "Required evidence and source",
                    "Assigned owner and execution rule",
                    "Failure response and retained record",
                ],
                "rows": [
                    [
                        "Certificate screening starts with jurisdiction and instrument classification.",
                        "County sale terms, tax vintage, parcel geometry, and recorded descriptions.",
                        "Research contractor builds the packet; operator confirms the instrument class.",
                        "Reject mismatched parcel identifiers and preserve both conflicting source artifacts.",
                    ],
                    [
                        "Certificate screening separates property quality from apparent tax delinquency discounts.",
                        "Clerk instruments, access evidence, demolition notices, and environmental screening results.",
                        "Research contractor escalates defects before the operator allocates bid capacity.",
                        "Scrub unusable collateral and record the specific reason against intake.",
                    ],
                    [
                        "Bid-down acquisition translates statutory mechanics into an enforceable bid ceiling.",
                        "Florida sections 197.432 and 197.472 plus current county auction instructions.",
                        "Operator locks maximum cash exposure after counsel resolves rule exceptions.",
                        "Reject unsupported rate assumptions and retain the approved calculation worksheet.",
                    ],
                    [
                        "Redemption servicing watches official events rather than projected interest accrual.",
                        "County redemption statement, official receipt reference, and matching bank settlement.",
                        "Operator books realized receipts; counsel handles disputed entitlement or timing.",
                        "Keep unreceived interest outside realized revenue and investigate unmatched deposits.",
                    ],
                    [
                        "Redeemable-deed disposition preserves classification-specific redemption and surplus rights.",
                        "Texas section 34.21, recorded deed, title work, and local procedure memorandum.",
                        "Counsel establishes the permitted route before operator authorizes disposition spending.",
                        "Stop unsupported recovery actions and retain notice and distribution evidence.",
                    ],
                    [
                        "Weekly capacity review protects the one-full-time-plus-two-contractor operating pod.",
                        "Aged exception list, available cash, hearing dates, and contractor commitments.",
                        "Operator limits new awards when unresolved files consume available specialist hours.",
                        "Release research capacity first; never manufacture liquidity through optimistic collections.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy Cleaner Evidence Before Buying More Certificates",
                "body": (
                    "Veteran operators win by eliminating expensive ambiguity before auction "
                    "day and by preserving the exact evidence needed at redemption."
                ),
                "items": [
                    "Download the county's final sale revision immediately before bidding; compare parcel removals and corrected balances against the earlier research packet.",
                    "Calculate the minimum acceptable return at the actual bid-down rate, including platform charges and a counsel reserve, rather than at the statutory headline rate.",
                    "Store county receipt numbers with jurisdiction and receipt year; an unscoped receipt number is not a dependable cross-county duplicate key.",
                    "Maintain a separate aging report for unrecovered principal and title exceptions; a high nominal coupon does not repair a blocked recovery path.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Normalize and classify intake",
                    "action": "Create the parcel-instrument-vintage key and archive the official source bundle.",
                    "detail": "The research contractor resolves legal descriptions, rule versions, and disqualifying property facts before scoring.",
                },
                {
                    "step": 2,
                    "title": "Verify and reserve bounded cash",
                    "action": "Confirm eligibility, title review, statutory calculations, and an evidence-backed maximum bid.",
                    "detail": "The operator reserves cash atomically; local counsel owns unresolved procedural interpretations.",
                },
                {
                    "step": 3,
                    "title": "Record official acquisition and servicing events",
                    "action": "Use authoritative award and redemption receipts as immutable, jurisdiction-scoped event keys.",
                    "detail": "Reconcile the platform action separately from the ledger posting; unresolved external outcomes remain exceptions.",
                },
                {
                    "step": 4,
                    "title": "Reconcile cash and archive closure evidence",
                    "action": "Separate returned basis, realized revenue, direct costs, and operating expenses.",
                    "detail": "Close an instrument only after the receipt, bank movement, ledger entries, and remaining ownership state agree.",
                },
            ],
        },
        {
            "heading": "2. Install the Six-Module Ledger and Idempotent Execution Boundary",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference below is a single SQLite program split into six "
                    "copy-pasteable modules. Concatenate the code cells in order into "
                    "one Python file; run the included self-test before adapting it. "
                    "It uses only the standard library and does not call an auction "
                    "service. All money is integer cents. Every posted event balances, "
                    "official receipt keys are unique, and journal entries become "
                    "immutable when their event posts. Intake identity includes the "
                    "jurisdiction, parcel, vintage, and instrument rail, preventing "
                    "a later certificate from overwriting an earlier one. Payload "
                    "fingerprints make a repeated identical request harmless while "
                    "rejecting the same event key with different economics. The "
                    "state sequence is intake, verified, reserved, owned, and closed. "
                    "Reserved cash is an internal restricted-cash subaccount, not a "
                    "claim that a county or third-party escrow account exists. A "
                    "real escrow arrangement needs its own bank account and documented "
                    "custody terms. Cash transferred between free and held accounts "
                    "does not become an expense. Acquisition transfers held cash "
                    "into investment basis; realization separates that basis from "
                    "interest, penalties, gains, losses, and collection charges. "
                    "These distinctions are the minimum useful ledger, not optional "
                    "presentation choices for a prettier scorecard."
                ),
                (
                    "The concurrency guarantee has a precise boundary: cooperating "
                    "processes using these functions against one local SQLite database. "
                    "BEGIN IMMEDIATE serializes writers before any balance or state "
                    "read, so two reservations cannot both spend the same free cash. "
                    "Unique keys and conditional state changes occur inside that "
                    "transaction, with rollback on every exception. The posting trigger "
                    "rejects an unbalanced event, while mutation triggers protect "
                    "posted history. Do not place this database on a shared network "
                    "filesystem or let spreadsheets write directly into its tables. "
                    "Use PostgreSQL with account-row locking and equivalent constraints "
                    "when multiple application hosts need concurrent access. Neither "
                    "SQLite nor an HTTP client can make an external auction bid and "
                    "a local commit one atomic act. The design therefore records "
                    "confirmed official outcomes instead of automatically retrying "
                    "purchases. An interrupted bid remains reserved while the operator "
                    "checks the platform and county record. Release a lost-auction "
                    "reservation only after documented confirmation. Ambiguous outcomes "
                    "stay held; they are not retried with a new business key. This "
                    "boundary eliminates local check-then-act races without inventing "
                    "an exactly-once promise for an external system that does not "
                    "provide one. Administrative database access remains a separately "
                    "controlled operational capability."
                ),
                (
                    "Deploy the ledger beside an evidence directory with read-only "
                    "closed packets, daily database backups, and a tested restore "
                    "procedure. SQLite's backup API is preferable to copying a live "
                    "database file without its write-ahead log. Keep auction credentials "
                    "outside source code and give each contractor only the records "
                    "needed for their assigned queue. The three evidence hashes in "
                    "verification identify eligibility, title review, and the rule "
                    "worksheet; they do not themselves prove that those documents "
                    "are correct. The operator must inspect and sign the underlying "
                    "packet. This compact implementation supports full instrument "
                    "exits and immediate settlement receipts. Partial redemptions, "
                    "unsettled escrow, subsequent-tax advances, and installment "
                    "recoveries require explicit additional event types before use. "
                    "Do not disguise them as ordinary expenses or overwrite purchase "
                    "basis. Test duplicate receipts, changed-payload replays, insufficient "
                    "cash, interrupted transactions, and competing reservations against "
                    "a disposable database. The self-test below covers the core "
                    "purchase-to-redemption path and a conflicting replay; it is a "
                    "reference test, not a report of execution in this manuscript. "
                    "For production, reconcile the official certificate inventory "
                    "and external bank statements independently of the program's "
                    "internal checks. Balanced entries can still encode the wrong "
                    "parcel, the wrong bank account, or a forged receipt."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and operating purpose",
                    "Copy-pasteable Python and SQL reference",
                    "Transaction boundary and operator responsibility",
                    "Expected evidence and verification outcome",
                ],
                "rows": [
                    [
                        "Module one creates constrained storage and balanced immutable posting primitives.",
                        """from __future__ import annotations
import hashlib
import json
import sqlite3
from contextlib import contextmanager

SCHEMA = '''
CREATE TABLE IF NOT EXISTS assets (
    id INTEGER PRIMARY KEY,
    jurisdiction TEXT NOT NULL,
    parcel TEXT NOT NULL,
    vintage TEXT NOT NULL,
    rail TEXT NOT NULL CHECK (rail IN ('certificate', 'redeemable_deed')),
    intake_hash TEXT NOT NULL,
    score INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100),
    maximum_cents INTEGER NOT NULL CHECK (maximum_cents > 0),
    book_cents INTEGER NOT NULL DEFAULT 0 CHECK (book_cents >= 0),
    state TEXT NOT NULL DEFAULT 'intake'
        CHECK (state IN ('intake','verified','reserved','owned','closed')),
    UNIQUE (jurisdiction, parcel, vintage, rail)
);
CREATE TABLE IF NOT EXISTS evidence (
    asset_id INTEGER NOT NULL REFERENCES assets(id),
    action TEXT NOT NULL,
    payload TEXT NOT NULL,
    UNIQUE (asset_id, action)
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    source_key TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL,
    asset_id INTEGER REFERENCES assets(id),
    payload_hash TEXT NOT NULL,
    payload TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'draft'
        CHECK (state IN ('draft','posted'))
);
CREATE TABLE IF NOT EXISTS entries (
    event_id INTEGER NOT NULL REFERENCES events(id),
    account TEXT NOT NULL CHECK
        (account IN ('CASH_FREE','CASH_HELD','ASSET','REVENUE','EXPENSE','EQUITY')),
    cents INTEGER NOT NULL CHECK (cents != 0),
    UNIQUE (event_id, account)
);
CREATE TRIGGER IF NOT EXISTS entries_insert_guard
BEFORE INSERT ON entries
WHEN (SELECT state FROM events WHERE id = NEW.event_id) != 'draft'
BEGIN SELECT RAISE(ABORT, 'Posted entries are immutable'); END;
CREATE TRIGGER IF NOT EXISTS entries_update_guard
BEFORE UPDATE ON entries
BEGIN SELECT RAISE(ABORT, 'Journal updates are prohibited'); END;
CREATE TRIGGER IF NOT EXISTS entries_delete_guard
BEFORE DELETE ON entries
BEGIN SELECT RAISE(ABORT, 'Journal deletion is prohibited'); END;
CREATE TRIGGER IF NOT EXISTS event_insert_guard
BEFORE INSERT ON events WHEN NEW.state != 'draft'
BEGIN SELECT RAISE(ABORT, 'Events must begin as drafts'); END;
CREATE TRIGGER IF NOT EXISTS event_post_guard
BEFORE UPDATE OF state ON events WHEN NEW.state = 'posted'
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT(*) FROM entries WHERE event_id = NEW.id) < 2
        OR (SELECT COALESCE(SUM(cents), 0) FROM entries
            WHERE event_id = NEW.id) != 0
    THEN RAISE(ABORT, 'Posting requires balanced entries') END;
END;
CREATE TRIGGER IF NOT EXISTS event_update_guard
BEFORE UPDATE ON events WHEN OLD.state = 'posted'
BEGIN SELECT RAISE(ABORT, 'Posted events are immutable'); END;
CREATE TRIGGER IF NOT EXISTS event_delete_guard
BEFORE DELETE ON events
BEGIN SELECT RAISE(ABORT, 'Event deletion is prohibited'); END;
CREATE TRIGGER IF NOT EXISTS evidence_update_guard
BEFORE UPDATE ON evidence
BEGIN SELECT RAISE(ABORT, 'Evidence history is immutable'); END;
CREATE TRIGGER IF NOT EXISTS evidence_delete_guard
BEFORE DELETE ON evidence
BEGIN SELECT RAISE(ABORT, 'Evidence deletion is prohibited'); END;
'''

def open_ledger(path):
    c = sqlite3.connect(path, timeout=30, isolation_level=None)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys = ON')
    c.execute('PRAGMA busy_timeout = 30000')
    c.execute('PRAGMA journal_mode = WAL')
    c.execute('PRAGMA synchronous = FULL')
    c.executescript(SCHEMA)
    return c

@contextmanager
def atomic(c):
    c.execute('BEGIN IMMEDIATE')
    try:
        yield
        c.execute('COMMIT')
    except BaseException:
        if c.in_transaction:
            c.execute('ROLLBACK')
        raise

def encode(payload):
    return json.dumps(payload, sort_keys=True, separators=(',', ':'))

def fingerprint(payload):
    return hashlib.sha256(encode(payload).encode('utf-8')).hexdigest()

def money(value, positive=False):
    if type(value) is not int or value < 0 or (positive and value == 0):
        raise ValueError('Money must be nonnegative integer cents')

def prior(c, key, payload):
    if not isinstance(key, str) or not key.strip():
        raise ValueError('A scoped source key is required')
    row = c.execute(
        'SELECT payload_hash FROM events WHERE source_key = ?', (key,)
    ).fetchone()
    if row is None:
        return False
    if row['payload_hash'] != fingerprint(payload):
        raise RuntimeError('Source key conflicts with its original payload')
    return True

def balance(c, account):
    return c.execute(
        '''SELECT COALESCE(SUM(j.cents), 0)
           FROM entries j JOIN events e ON e.id = j.event_id
           WHERE j.account = ? AND e.state = 'posted' ''',
        (account,)
    ).fetchone()[0]

def post(c, key, kind, asset_id, payload, lines):
    if not c.in_transaction:
        raise RuntimeError('Posting requires an active writer transaction')
    if prior(c, key, payload):
        return False
    totals = {}
    for account, cents in lines:
        if type(cents) is not int:
            raise ValueError('Journal values must be integer cents')
        totals[account] = totals.get(account, 0) + cents
    lines = [(account, cents) for account, cents in totals.items() if cents]
    if len(lines) < 2 or sum(cents for _, cents in lines) != 0:
        raise ValueError('Journal entries must balance')
    event_id = c.execute(
        '''INSERT INTO events
           (source_key, kind, asset_id, payload_hash, payload)
           VALUES (?, ?, ?, ?, ?)''',
        (key, kind, asset_id, fingerprint(payload), encode(payload))
    ).lastrowid
    c.executemany(
        'INSERT INTO entries(event_id, account, cents) VALUES (?, ?, ?)',
        [(event_id, account, cents) for account, cents in lines]
    )
    c.execute("UPDATE events SET state = 'posted' WHERE id = ?", (event_id,))
    return True

def require_state(c, asset_id, state):
    row = c.execute('SELECT * FROM assets WHERE id = ?', (asset_id,)).fetchone()
    if row is None or row['state'] != state:
        raise RuntimeError('Instrument state does not permit this action')
    return row

def move(c, asset_id, old, new, book_cents):
    changed = c.execute(
        '''UPDATE assets SET state = ?, book_cents = ?
           WHERE id = ? AND state = ?''',
        (new, book_cents, asset_id, old)
    ).rowcount
    if changed != 1:
        raise RuntimeError('Conditional instrument transition failed')
""",
                        "Every writer uses one immediate transaction before reading spendable cash.",
                        "Unique business identities, balanced posting triggers, and immutable journal history persist.",
                    ],
                    [
                        "Module two imports and scores immutable parcel-instrument-vintage acquisition candidates.",
                        """def intake(c, jurisdiction, parcel, vintage, rail, maximum_cents, risk_points):
    money(maximum_cents, positive=True)
    if type(risk_points) is not int or not 0 <= risk_points <= 100:
        raise ValueError('Risk points must be integers from zero through one hundred')
    if rail not in ('certificate', 'redeemable_deed'):
        raise ValueError('Instrument rail requires explicit classification')
    identity = [jurisdiction, parcel, vintage, rail]
    if any(not isinstance(value, str) or not value.strip() for value in identity):
        raise ValueError('Each instrument identity component is required')
    payload = {
        'identity': identity,
        'maximum_cents': maximum_cents,
        'risk_points': risk_points,
    }
    digest = fingerprint(payload)
    with atomic(c):
        row = c.execute(
            '''SELECT id, intake_hash FROM assets
               WHERE jurisdiction = ? AND parcel = ? AND vintage = ? AND rail = ?''',
            tuple(identity)
        ).fetchone()
        if row is not None:
            if row['intake_hash'] != digest:
                raise RuntimeError('Existing intake requires an explicit revision workflow')
            return row['id']
        return c.execute(
            '''INSERT INTO assets
               (jurisdiction, parcel, vintage, rail, intake_hash, score, maximum_cents)
               VALUES (?, ?, ?, ?, ?, ?, ?)''',
            tuple(identity) + (digest, 100 - risk_points, maximum_cents)
        ).lastrowid
""",
                        "Identity lookup and insertion share the same serialized writer transaction.",
                        "Repeated imports return the existing identifier; changed underwriting cannot overwrite history.",
                    ],
                    [
                        "Module three verifies evidence and controls reserved-cash state transitions.",
                        """def verify(c, asset_id, evidence_hashes):
    required = {'eligibility', 'title_review', 'rule_worksheet'}
    if set(evidence_hashes) != required:
        raise ValueError('Three named verification artifacts are required')
    for digest in evidence_hashes.values():
        if (not isinstance(digest, str) or len(digest) != 64
                or any(ch not in '0123456789abcdef' for ch in digest)):
            raise ValueError('Evidence requires lowercase SHA-256 digests')
    payload = encode(evidence_hashes)
    with atomic(c):
        old = c.execute(
            "SELECT payload FROM evidence WHERE asset_id = ? AND action = 'verify'",
            (asset_id,)
        ).fetchone()
        if old is not None:
            if old['payload'] != payload:
                raise RuntimeError('Verification replay changes retained evidence')
            return False
        row = require_state(c, asset_id, 'intake')
        if row['score'] < 75:
            raise RuntimeError('Research score requires exception review before verification')
        c.execute(
            "INSERT INTO evidence(asset_id, action, payload) VALUES (?, 'verify', ?)",
            (asset_id, payload)
        )
        move(c, asset_id, 'intake', 'verified', 0)
        return True

def reserve(c, asset_id):
    key = 'reserve:' + str(asset_id)
    payload = {'kind': 'reserve', 'asset_id': asset_id}
    with atomic(c):
        if prior(c, key, payload):
            return False
        row = require_state(c, asset_id, 'verified')
        amount = row['maximum_cents']
        if balance(c, 'CASH_FREE') < amount:
            raise RuntimeError('Available cash cannot cover the reservation')
        post(c, key, 'reserve', asset_id, payload,
             [('CASH_HELD', amount), ('CASH_FREE', -amount)])
        move(c, asset_id, 'verified', 'reserved', 0)
        return True

def release(c, asset_id, confirmation):
    if not isinstance(confirmation, str) or not confirmation.strip():
        raise ValueError('Official nonpurchase confirmation is required')
    key = 'release:' + str(asset_id)
    payload = {
        'kind': 'release', 'asset_id': asset_id, 'confirmation': confirmation
    }
    with atomic(c):
        if prior(c, key, payload):
            return False
        row = require_state(c, asset_id, 'reserved')
        amount = row['maximum_cents']
        post(c, key, 'release', asset_id, payload,
             [('CASH_FREE', amount), ('CASH_HELD', -amount)])
        move(c, asset_id, 'reserved', 'closed', 0)
        return True
""",
                        "Evidence recording, cash checks, and state movement occur without intervening writers.",
                        "Ambiguous auction outcomes remain reserved until documented purchase or nonpurchase confirmation.",
                    ],
                    [
                        "Module four posts funding, confirmed awards, full realizations, and cash expenses.",
                        """def fund(c, source, cents):
    money(cents, positive=True)
    payload = {'kind': 'funding', 'cents': cents}
    with atomic(c):
        return post(c, 'funding:' + source, 'funding', None, payload,
                    [('CASH_FREE', cents), ('EQUITY', -cents)])

def purchase(c, asset_id, receipt, cost_cents):
    money(cost_cents, positive=True)
    payload = {'kind': 'purchase', 'asset_id': asset_id, 'cost_cents': cost_cents}
    key = 'receipt:' + receipt
    with atomic(c):
        if prior(c, key, payload):
            return False
        row = require_state(c, asset_id, 'reserved')
        held = row['maximum_cents']
        if cost_cents > held:
            raise RuntimeError('Confirmed award exceeds reserved acquisition capacity')
        post(c, key, 'purchase', asset_id, payload, [
            ('ASSET', cost_cents), ('CASH_HELD', -held),
            ('CASH_FREE', held - cost_cents)
        ])
        move(c, asset_id, 'reserved', 'owned', cost_cents)
        return True

def realize(c, asset_id, receipt, basis, interest=0, penalty=0,
            gain=0, loss=0, fees=0):
    for amount in (basis, interest, penalty, gain, loss, fees):
        money(amount)
    money(basis, positive=True)
    if gain and loss:
        raise ValueError('One disposition cannot carry both a gain and a loss')
    gross = interest + penalty + gain
    cash = basis + gross - loss - fees
    if cash < 0:
        raise ValueError('Cash-negative recovery requires a separate event design')
    payload = {
        'kind': 'realization', 'asset_id': asset_id, 'basis': basis,
        'interest': interest, 'penalty': penalty, 'gain': gain,
        'loss': loss, 'fees': fees
    }
    key = 'receipt:' + receipt
    with atomic(c):
        if prior(c, key, payload):
            return False
        row = require_state(c, asset_id, 'owned')
        if basis != row['book_cents']:
            raise RuntimeError('This implementation supports full exits only')
        post(c, key, 'realization', asset_id, payload, [
            ('CASH_FREE', cash), ('ASSET', -basis),
            ('REVENUE', -gross), ('EXPENSE', loss + fees)
        ])
        move(c, asset_id, 'owned', 'closed', 0)
        return True

def expense(c, receipt, cents, category):
    money(cents, positive=True)
    if not isinstance(category, str) or not category.strip():
        raise ValueError('Expense category is required')
    payload = {'kind': 'expense', 'cents': cents, 'category': category}
    key = 'expense:' + receipt
    with atomic(c):
        if prior(c, key, payload):
            return False
        if balance(c, 'CASH_FREE') < cents:
            raise RuntimeError('Expense exceeds available cash')
        return post(c, key, 'expense', None, payload,
                    [('EXPENSE', cents), ('CASH_FREE', -cents)])
""",
                        "Receipt replay detection precedes ownership validation inside the same transaction.",
                        "Returned basis bypasses revenue; realized losses and collection fees remain expenses.",
                    ],
                    [
                        "Module five exposes event-level reconciliation without misclassifying returned investment principal.",
                        """VIEWS = '''
CREATE VIEW IF NOT EXISTS v_event_reconciliation AS
SELECT
    e.id AS event_id,
    e.source_key,
    e.kind,
    e.asset_id,
    SUM(CASE WHEN j.account IN ('CASH_FREE','CASH_HELD')
             THEN j.cents ELSE 0 END) AS cash_change_cents,
    -SUM(CASE WHEN j.account = 'REVENUE'
              THEN j.cents ELSE 0 END) AS realized_revenue_cents,
    SUM(CASE WHEN j.account = 'EXPENSE'
             THEN j.cents ELSE 0 END) AS expense_cents,
    CASE WHEN e.kind = 'realization'
         THEN -SUM(CASE WHEN j.account = 'ASSET'
                        THEN j.cents ELSE 0 END)
         ELSE 0 END AS exited_basis_cents,
    CASE WHEN e.kind = 'purchase'
         THEN SUM(CASE WHEN j.account = 'ASSET'
                       THEN j.cents ELSE 0 END)
         ELSE 0 END AS purchased_basis_cents,
    SUM(j.cents) AS balance_check_cents
FROM events e JOIN entries j ON j.event_id = e.id
WHERE e.state = 'posted'
GROUP BY e.id, e.source_key, e.kind, e.asset_id;

CREATE VIEW IF NOT EXISTS v_account_balances AS
SELECT j.account, SUM(j.cents) AS balance_cents
FROM entries j JOIN events e ON e.id = j.event_id
WHERE e.state = 'posted'
GROUP BY j.account;
'''

def install_views(c):
    c.executescript(VIEWS)

def reconciliation(c):
    return [dict(row) for row in c.execute(
        'SELECT * FROM v_event_reconciliation ORDER BY event_id'
    )]
""",
                        "Each reporting query reads committed postings from a consistent SQLite statement snapshot.",
                        "Match event cash changes to bank evidence and exited basis to instrument inventory.",
                    ],
                    [
                        "Module six validates ledger invariants and exercises a complete receipt-replay example.",
                        """def qa(c):
    with atomic(c):
        if c.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise RuntimeError('Database integrity check failed')
        if c.execute('PRAGMA foreign_key_check').fetchone() is not None:
            raise RuntimeError('Foreign key check failed')
        if c.execute("SELECT 1 FROM events WHERE state != 'posted'").fetchone():
            raise RuntimeError('Uncommitted workflow draft survived a transaction')
        bad = c.execute(
            '''SELECT e.id FROM events e JOIN entries j ON j.event_id = e.id
               GROUP BY e.id HAVING SUM(j.cents) != 0 OR COUNT(*) < 2'''
        ).fetchone()
        if bad:
            raise RuntimeError('Event-level balance invariant failed')
        expected_held = c.execute(
            "SELECT COALESCE(SUM(maximum_cents), 0) FROM assets WHERE state = 'reserved'"
        ).fetchone()[0]
        expected_basis = c.execute(
            "SELECT COALESCE(SUM(book_cents), 0) FROM assets WHERE state = 'owned'"
        ).fetchone()[0]
        if balance(c, 'CASH_HELD') != expected_held:
            raise RuntimeError('Reserved cash differs from reserved instruments')
        if balance(c, 'ASSET') != expected_basis:
            raise RuntimeError('Investment basis differs from owned instruments')
        if balance(c, 'CASH_FREE') < 0 or balance(c, 'CASH_HELD') < 0:
            raise RuntimeError('Cash account contains a negative balance')
        return {
            'cash_cents': balance(c, 'CASH_FREE') + balance(c, 'CASH_HELD'),
            'investment_cents': balance(c, 'ASSET'),
            'revenue_cents': -balance(c, 'REVENUE'),
            'expense_cents': balance(c, 'EXPENSE')
        }

def self_test():
    c = open_ledger(':memory:')
    try:
        install_views(c)
        fund(c, 'fixture:bank:opening', 100000)
        asset_id = intake(
            c, 'FL:fixture-county', 'parcel-001', '2025',
            'certificate', 50000, 10
        )
        digest = hashlib.sha256(b'fixture evidence only').hexdigest()
        verify(c, asset_id, {
            'eligibility': digest,
            'title_review': digest,
            'rule_worksheet': digest
        })
        reserve(c, asset_id)
        purchase(c, asset_id, 'FL:fixture:2026:award-001', 45000)
        realize(c, asset_id, 'FL:fixture:2026:redeem-001',
                45000, interest=1000, fees=100)
        repeated = realize(
            c, asset_id, 'FL:fixture:2026:redeem-001',
            45000, interest=1000, fees=100
        )
        if repeated:
            raise RuntimeError('Identical receipt replay created another event')
        conflict_seen = False
        try:
            realize(c, asset_id, 'FL:fixture:2026:redeem-001',
                    45000, interest=1100, fees=100)
        except RuntimeError:
            conflict_seen = True
        if not conflict_seen:
            raise RuntimeError('Changed receipt replay escaped conflict detection')
        result = qa(c)
        expected = {
            'cash_cents': 100900, 'investment_cents': 0,
            'revenue_cents': 1000, 'expense_cents': 100
        }
        if result != expected:
            raise RuntimeError('Reference lifecycle totals differ from expected cents')
        return result
    finally:
        c.close()

if __name__ == '__main__':
    print(self_test())
""",
                        "Run invariant checks inside one writer transaction to prevent inconsistent cross-query reads.",
                        "Fixture expects $1,009 cash, zero investment basis, and $9 realized net profit.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Verifications Before Any Live Award",
                "body": (
                    "The reference controls local ledger races. Production readiness also "
                    "requires source verification, external settlement discipline, and "
                    "tested recovery procedures."
                ),
                "items": [
                    "Verify bidder registration, eligible entity, current county terms, funding deadline, and the exact certificate or deed classification against official records.",
                    "Verify title review, bankruptcy screening, redemption calculation, and notice or surplus treatment with retained jurisdiction-specific evidence.",
                    "Run two independent database connections against one insufficient combined cash balance; exactly one competing reservation must succeed.",
                    "Restore a backup, replay a recorded receipt, and match cash plus owned basis to the external bank statement and county inventory before authorizing live use.",
                ],
            },
        },
        {
            "heading": "3. Walk the Ninety-Day Cohorts Without Inventing Ninety-Day Redemptions",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a seasoned-book operating model, "
                    "not a promise that fresh purchases produce cash within a quarter. "
                    "Open with $750,000 of funded capital: $625,000 of documented "
                    "investment basis and $125,000 of unrestricted cash. That capital "
                    "assumption sits within the volume's $100,000 to $1,500,000 startup "
                    "range but is illustrative rather than a scorecard requirement. "
                    "Existing instruments supply the quarter's realizations; newly "
                    "acquired Month 1, Month 2, and Month 3 cohorts remain invested "
                    "at the walk's end. Each month screens forty leads, scrubs twelve "
                    "for instrument or collateral defects, researches twenty-eight, "
                    "verifies ten, bids on eight, and wins five. Two verified candidates "
                    "are deliberately unbid, and three bids lose. Five purchases at "
                    "$5,000 each deploy $25,000 monthly. Separately, five older positions "
                    "exit with $25,000 aggregate basis. These counts describe distinct "
                    "acquisition and realization cohorts. Preserve the cross-reference "
                    "between each old instrument and its original purchase date; "
                    "otherwise the dashboard will falsely credit this month's intake "
                    "with historical collections. The volume's six-to-thirty-six-month "
                    "time-to-first-deal range remains the planning horizon for an "
                    "unseasoned launch, and early calendar milestones measure readiness "
                    "rather than forced cash realization."
                ),
                (
                    "Each month's old-book receipts contain $15,000 of redeemed "
                    "certificate principal, $6,250 of realized interest, and $625 "
                    "of statutory penalties actually supported by settlement statements. "
                    "A separate disposition returns $10,000 of basis and realizes "
                    "a $1,250 gain through $11,250 of sale proceeds. Therefore "
                    "gross bank receipts are $33,125, but recognized operator revenue "
                    "is only $8,125: interest plus penalties plus gain. These "
                    "amounts are a portfolio aggregate, not a fabricated universal "
                    "county redemption formula. Assign every penalty to its actual "
                    "statutory instrument and exclude unreceived accruals. Monthly "
                    "operating overhead is $1,500, within the stated operating "
                    "range. Direct title, counsel, auction, and disposition costs "
                    "are $3,171.88 in Month 1, $3,171.87 in Month 2, and "
                    "$3,171.88 in Month 3. Total costs are consequently $4,671.88, "
                    "$4,671.87, and $4,671.88. The monthly overhead range is not "
                    "the entire cost structure; deal-level costs remain economically "
                    "real. No capital write-off is assumed in this Base walk. "
                    "The twelve monthly intake scrubs are rejected opportunities, "
                    "not twelve realized investment losses. A later impairment "
                    "would reduce the scenario's actual result rather than being "
                    "hidden inside returned principal or silently offset by invented revenue."
                ),
                (
                    "Month-end cash increases by $3,453.12, $3,453.13, and $3,453.12 "
                    "after purchases and all modeled costs. Quarter receipts of "
                    "$99,375 less $75,000 of new investment and $14,015.63 of "
                    "costs leave $10,359.37 of incremental cash. Opening unrestricted "
                    "cash of $125,000 therefore becomes $135,359.37. Investment "
                    "basis stays $625,000 because $75,000 exits while $75,000 "
                    "is purchased, and combined cash plus basis becomes $760,359.37. "
                    "The revenue run rate is $24,375 per quarter and $97,500 "
                    "annually. At exactly 42.5 percent, annual owner profit is "
                    "$41,437.50, displayed as the canonical rounded $41,438. "
                    "The quarter's exact margin target is $10,359.375 before "
                    "cent allocation; alternating quarter allocations of $10,359.37 "
                    "and $10,359.38 reconcile the full year without inventing "
                    "fractional cash cents. Do not multiply the first rounded "
                    "quarter by four and treat the two-cent difference as "
                    "operating variance. Nor should the regularized table imply "
                    "smooth real-world redemptions. Actual monthly receipts are "
                    "lumpy, and the reserve must cover dry periods, contested "
                    "title, and counsel commitments. Keep the Conservative "
                    "$4,500 and Scaled $99,000 annual owner-profit cases visible "
                    "beside the Base case when deciding how much capital "
                    "the household or investing entity can leave unavailable."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and distinct cohort movement",
                    "Cash timing and recognized revenue",
                    "Scrubs, losses, and complete operating costs",
                    "Cash-flow reconciliation and remaining investment basis",
                ],
                "rows": [
                    [
                        "Month 1: forty leads, twelve scrubs, twenty-eight researched, ten verified, eight bids, five purchases.",
                        "Older cohorts return $25,000 principal plus $8,125 revenue; gross cash receipts equal $33,125.",
                        "Twelve pre-purchase scrubs; zero booked capital losses; $1,500 overhead plus $3,171.88 direct costs.",
                        "$33,125 receipts less $25,000 purchases less $4,671.88 costs; cumulative cash gain $3,453.12.",
                    ],
                    [
                        "Month 2: forty new leads, twelve scrubs, ten verified, eight bids, five additional purchases.",
                        "Different older instruments return $25,000 principal plus $8,125 revenue; gross receipts equal $33,125.",
                        "Twelve pre-purchase scrubs; zero booked capital losses; $1,500 overhead plus $3,171.87 direct costs.",
                        "$33,125 receipts less $25,000 purchases less $4,671.87 costs; cumulative cash gain $6,906.25.",
                    ],
                    [
                        "Month 3: forty new leads, twelve scrubs, ten verified, eight bids, five additional purchases.",
                        "Separate historical positions return $25,000 principal plus $8,125 revenue; gross receipts equal $33,125.",
                        "Twelve pre-purchase scrubs; zero booked capital losses; $1,500 overhead plus $3,171.88 direct costs.",
                        "$33,125 receipts less $25,000 purchases less $4,671.88 costs; cumulative cash gain $10,359.37.",
                    ],
                    [
                        "Quarter totals: 120 leads, thirty-six scrubs, thirty verified, twenty-four bids, fifteen purchases.",
                        "$75,000 returned principal plus $24,375 recognized revenue produces $99,375 gross bank receipts.",
                        "Thirty-six rejected opportunities; zero capital write-offs; $4,500 overhead plus $9,515.63 direct costs.",
                        "$99,375 receipts less $75,000 purchases less $14,015.63 costs equals $10,359.37 cash gain.",
                    ],
                    [
                        "Annual Base normalization uses four quarters with explicit alternating cent allocations.",
                        "$97,500 annual revenue excludes $300,000 illustrative annual returned principal and replacement purchases.",
                        "$18,000 overhead plus $38,062.50 direct costs equals $56,062.50 total annual expenses.",
                        "$41,437.50 exact owner profit rounds to $41,438 at the canonical 42.5 percent margin.",
                    ],
                    [
                        "Day 90 stock reconciliation preserves all three new acquisition cohorts as invested.",
                        "$125,000 opening cash plus $10,359.37 net movement equals $135,359.37 ending unrestricted cash.",
                        "$625,000 opening basis minus $75,000 exited basis plus $75,000 purchases leaves basis unchanged.",
                        "$135,359.37 cash plus $625,000 investment basis equals $760,359.37 combined book assets.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Close the Books, Resolve Exceptions, and Expand Only Verified Capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Close each operating day by matching four records: the county "
                    "or appointed auction vendor's official event, the instrument "
                    "inventory, the bank transaction, and the ledger event. A "
                    "deposit description alone does not establish principal or "
                    "interest classification. Split a combined county remittance "
                    "using its instrument-level settlement detail before posting "
                    "individual realizations. If the bank receives a pooled amount "
                    "before that detail arrives, hold it in a separately implemented "
                    "unapplied-receipts workflow rather than improvising revenue "
                    "entries in this compact ledger. Likewise, an auction deposit "
                    "held by a vendor needs a real external-custody account "
                    "extension; the sample's internal CASH_HELD account does not "
                    "prove remittance. The operator owns the reconciliation, while "
                    "the research contractor checks instrument identifiers and "
                    "counsel resolves disputed rights. Record every exception with "
                    "a responsible person, next action, and dated evidence. "
                    "Separate cash outstanding from documents outstanding: the "
                    "first changes liquidity planning, while the second can "
                    "prevent a lawful recovery even when the bank balance "
                    "looks healthy. Send unmatched settlement references into "
                    "the next morning's priority queue. Never solve a mismatch "
                    "by deleting a posted event, editing its payload, or "
                    "moving a receipt to a different parcel without a documented correction."
                ),
                (
                    "Run a weekly legal-calendar review independently of projected "
                    "yield. Counsel should confirm jurisdiction-specific redemption "
                    "periods, application windows, service requirements, and "
                    "bankruptcy status against the current file. Calendar entries "
                    "need the legal source, triggering event, computation method, "
                    "responsible person, and supporting artifact. A database date "
                    "alone is not proof of valid notice. Post-Tyler recovery "
                    "analysis must distinguish enforceable debt, recoverable "
                    "expenses, buyer economics, and owner surplus. Neither "
                    "the acquisition spreadsheet nor the disposition worksheet "
                    "should assume that all sale proceeds belong to the "
                    "investor. For capital planning, stress the Base book "
                    "with delayed collections and explicit loss amounts. A "
                    "$20,000 realized principal loss, with everything else "
                    "unchanged, reduces exact Base owner profit from $41,437.50 "
                    "to $21,437.50. Three months without the modeled receipts "
                    "would also require cash for commitments and costs; it "
                    "would not create recognized interest merely because "
                    "the calendar advanced. Distinguish that cash stress "
                    "from an impairment conclusion. The first concerns "
                    "when money arrives, and the second concerns how "
                    "much remains recoverable. Both matter, but combining "
                    "them into one generic risk score conceals the "
                    "specific operating decision that the pod must make."
                ),
                (
                    "Use the first ninety days to prove the production system "
                    "before widening geographic coverage. During days one through "
                    "thirty, select a jurisdiction, assemble official rule packets, "
                    "test the ledger, and rehearse one complete acquisition "
                    "without submitting a live bid. During days thirty-one "
                    "through sixty, complete registrations, verify contractor "
                    "capacity, set cash limits, and execute only documented "
                    "opportunities that meet the bid ceiling. During days "
                    "sixty-one through ninety, audit receipt handling, restore "
                    "a backup, review stale research, and examine whether "
                    "new acquisitions can be serviced within existing capacity. "
                    "These are launch milestones; the seasoned-book cohort "
                    "table is a separate economic illustration. Expansion "
                    "requires evidence that exception aging, reconciliation "
                    "quality, and cash coverage remain acceptable, not "
                    "simply that lead volume increased. The Base pod "
                    "remains one full-time operator and two contractors. "
                    "The Scaled case explicitly increases staffing to "
                    "two full-time people and three contractors, with "
                    "$180,000 revenue and $99,000 annual owner profit "
                    "at a 55 percent margin. Automation helps with "
                    "auction screening and redemption tracking; it does "
                    "not eliminate counsel, create missing title evidence, "
                    "or accelerate statutory clocks. Grow the number "
                    "of cleanly serviced instruments only after the "
                    "current book can be explained from source document "
                    "to reconciled cash without oral reconstruction."
                ),
            ],
            "table": {
                "caption": "Daily Close, Recovery Exceptions, and Production Acceptance Matrix",
                "headers": [
                    "Failure or acceptance test",
                    "Concrete reproduction or independent source",
                    "Required result and retained evidence",
                    "Owner and immediate operating response",
                ],
                "rows": [
                    [
                        "Duplicate receipt replay must never create a second economic event.",
                        "Submit the identical scoped county receipt twice using the same amounts.",
                        "Second request returns without posting; cash and revenue totals remain unchanged.",
                        "Operator preserves both request logs and investigates any changed receipt payload.",
                    ],
                    [
                        "Competing cash reservations must never overdraw available acquisition capacity.",
                        "Use two database connections reserving individually affordable but jointly unaffordable instruments.",
                        "One transaction succeeds; the other observes reduced cash and rejects reservation.",
                        "Operator blocks live deployment until the concurrency test passes reproducibly.",
                    ],
                    [
                        "Interrupted posting must leave neither partial journal entries nor ownership changes.",
                        "Inject an exception after entry insertion but before the enclosing transaction commits.",
                        "Rollback restores previous balances, instrument state, and receipt-key availability together.",
                        "Technical maintainer retains test evidence and verifies database restoration procedures.",
                    ],
                    [
                        "Official inventory must agree with owned basis and instrument identity.",
                        "Compare county certificate records and recorded deeds against every owned asset.",
                        "Each position has matching jurisdiction, parcel, vintage, instrument rail, and cost.",
                        "Research contractor resolves mismatches before the operator authorizes related recovery spending.",
                    ],
                    [
                        "Bank settlement must support every realized receipt and expense amount.",
                        "Compare statement lines with official remittance detail and event reconciliation exports.",
                        "Principal remains outside revenue; fees, losses, and gains retain explicit classifications.",
                        "Operator investigates unmatched cash instead of editing previously posted economic history.",
                    ],
                    [
                        "Recovery authority must survive notice, bankruptcy, redemption, and surplus review.",
                        "Counsel reviews current statutes, case docket, service evidence, and distribution worksheet.",
                        "Written route confirms permitted next action and identifies every unresolved procedural dependency.",
                        "Counsel controls disputed recovery work while operator preserves liquidity and deadlines.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A tax lien becomes an operating result only when the statutory right, instrument basis, and bank receipt reconcile.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Assign the four mapped plays to the one-full-time-plus-two-contractor pod and define a maximum unresolved-file workload before importing auction candidates.",
        "Build jurisdiction-parcel-vintage-instrument identities and archive official sale terms, title evidence, and rule worksheets with SHA-256 digests.",
        "Concatenate the six reference modules, run the self-test, and complete competing-reservation, interruption, receipt-replay, and backup-restoration tests before live use.",
        "Set maximum bids from verified statutory cash flows, reserve cash atomically, and retain ambiguous external auction outcomes as unresolved reservations.",
        "Reproduce the ninety-day Base walk with $24,375 realized revenue, $14,015.63 costs, $75,000 returned principal, and $10,359.37 incremental cash.",
        "Close each month against bank statements and official instrument inventory; have counsel separately review bankruptcy, notice, redemption, and surplus-equity exceptions.",
    ],
    "statutory_citations": [
        {
            "title": "Florida Statutes § 197.432 — Sale of tax certificates for unpaid taxes",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.432.html",
            "relevance": "Establishes the Florida certificate-sale framework and bid-down mechanics that must be reflected in acquisition underwriting and current county instructions.",
        },
        {
            "title": "Florida Statutes § 197.472 — Redemption of tax certificates",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.472.html",
            "relevance": "Controls Florida redemption amounts and relevant interest treatment; supports instrument-level settlement calculations rather than generic coupon assumptions.",
        },
        {
            "title": "Florida Statutes § 197.502 — Application for obtaining tax deed by holder of tax sale certificate",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.502.html",
            "relevance": "Provides the application framework, timing, and payment requirements that distinguish certificate ownership from later tax-deed procedures.",
        },
        {
            "title": "Texas Tax Code § 34.21 — Right of redemption",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm#34.21",
            "relevance": "Defines classification-dependent redemption rights and amounts for Texas tax-sale property; premiums must not be treated as universal annual interest rates.",
        },
        {
            "title": "11 U.S.C. § 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "Requires bankruptcy-specific review before acts that may enforce liens, collect claims, or affect property subject to the automatic stay.",
        },
        {
            "title": "Tyler v. Hennepin County, 598 U.S. 631 (2023)",
            "url": "https://www.supremecourt.gov/opinions/22pdf/22-166_8n59.pdf",
            "relevance": "Addresses retention of surplus equity beyond tax debt under the Takings Clause; recovery models must examine applicable ownership and distribution rules.",
        },
    ],
}
