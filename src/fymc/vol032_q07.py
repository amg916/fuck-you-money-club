from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute iso payment processing & atm arbitrage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "IRIS CRM Boarding, Sponsor-Verified MIDs, Reg E ATM Receipts, SQLite Journals & a Cash-Reconciled Merchant Cohort",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #32, ISO Payment Processing & ATM Arbitrage, ranks #02 of 36 "
        "with a 94/100 Money-to-Manpower Score. This chapter organizes 12 mapped "
        "plays into an executable operating sequence: authorized outbound, qualification, "
        "Schedule A pricing, underwriting, MID configuration, gateway attachment, dispute "
        "deflection, venue contracting, ATM deployment, telemetry, residual auditing, and "
        "retention. The production reference uses transactional SQLite, immutable monetary "
        "entries, explicit workflow evidence, and replay-safe event keys. A worked "
        "90-day cohort reaches the $445,000 Base annual revenue run rate while exposing "
        "the cash required before residual collections mature. Annual owner profits remain "
        "exactly $27,000 Conservative, $189,125 Base, and $440,000 Scaled. Merchant "
        "settlements and ATM vault cash never become operator revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$90,000",
            "context": "Annual operator revenue from net retained residuals, gateway markups, and ATM surcharges",
            "note": "30% net margin; $27,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$445,000",
            "context": "Annual operator revenue from net retained residuals, gateway markups, and ATM surcharges",
            "note": "42.5% net margin; $189,125 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual operator revenue from net retained residuals, gateway markups, and ATM surcharges",
            "note": "55% net margin; $440,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Convert qualified demand into sponsor-approved, economically valid accounts",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Begin with one economic record per merchant legal entity and one location record per ATM venue. "
                    "IRIS CRM holds the relationship, application checklist, Schedule A version, referral source, and "
                    "sponsor decision reference; the ledger holds money and immutable event identifiers. The twelve "
                    "operating workstreams named here describe this chapter's implementation map, rather than inventing "
                    "eleven additional catalog identifiers. Qualification starts with processing statements, ownership "
                    "documents, fulfillment timing, refund practices, and the actual merchant category. A merchant "
                    "processing $100,000 monthly at a retained twenty basis points contributes $200 monthly before "
                    "operator overhead; the $100,000 settlement volume is neither revenue nor working capital available "
                    "to the ISO. Price the retained spread after interchange, assessments, processor charges, referral "
                    "shares, and contractual deductions. If the residual report already supplies that retained amount, "
                    "do not multiply another retained_share into it. Document the ASC 606 principal-versus-agent "
                    "assessment for each fee stream instead of treating every customer charge as gross revenue. "
                    "A gateway attachment contributes only its contractual retained markup. Underwriting failure ends "
                    "the application or returns it for legitimate correction; it never triggers disguised reboarding "
                    "under a different business description. Keep rejected applications outside activation forecasts "
                    "until new evidence actually changes the sponsor decision."
                ),
                (
                    "The catalog play multi_inbox_free_workspace_outbound_clusters requires a materially narrower "
                    "production interpretation than its headline capacity claim. Three hundred authorized inboxes "
                    "sending twenty-five messages on twenty working days produce 150,000 attempted messages; at "
                    "fifteen daily, the same estate produces 90,000. Those figures establish arithmetic, not permission, "
                    "deliverability, or primary-inbox placement. Use Microsoft 365 developer or partner benefits only "
                    "when their actual terms authorize this production use; otherwise budget licensed mailboxes or "
                    "an approved outbound provider. Cloudflare Email Routing handles inbound forwarding rather than "
                    "supplying a bulk outbound SMTP service. Maintain a maximum of two or three secondary domains "
                    "per tenant as an administrative ceiling, remove tracking pixels, and centralize suppression across "
                    "every domain. CAN-SPAM, 15 U.S.C. 7704, requires accurate routing information, truthful subjects, "
                    "a postal address, and timely opt-out handling. Verify all addresses through authorized validation "
                    "methods, but classify catch-all results as uncertain because SMTP responses cannot prove delivery "
                    "to a particular person. Exclude uncertain addresses from the first pilot. Warm standby domains "
                    "serve documented continuity needs, never circumvention of complaints, provider restrictions, or "
                    "recipient blocks. At a purely illustrative 0.2% application yield, 150,000 attempts produce "
                    "300 applications before underwriting scrubs and onboarding losses."
                ),
                (
                    "Execute the first four workstreams through a single evidence packet: qualified intake, approved "
                    "outbound provenance, signed commercial pricing, and sponsor underwriting. Then configure the MID "
                    "and gateway only for the approved legal entity, business model, descriptor, and permitted channels. "
                    "High-risk MID orchestration means sponsor-authorized routing among disclosed accounts; it does "
                    "not mean transaction laundering or hiding chargebacks. A rejected vertical falls back to a "
                    "different expressly willing sponsor or leaves the pipeline. Pricing review separates credit "
                    "surcharges, bona fide cash discounts, and dual-price displays. Debit and prepaid transactions "
                    "must not receive a credit-card surcharge merely because a terminal can technically add one. "
                    "Apply current Visa and Mastercard rules, sponsor requirements, and relevant state law together; "
                    "New York General Business Law section 518 is a concrete display requirement to evaluate for "
                    "New York merchants. Record the tested terminal profile and photographed customer-facing prices. "
                    "For ATM venues, negotiate exclusivity, access hours, replenishment responsibility, surcharge "
                    "allocation, outage handling, and termination rights before installation. Twenty venues retaining "
                    "$200 monthly each contribute $4,000 monthly; a quoted $3 consumer fee is not automatically "
                    "$3 retained by the operator. Reject a venue whose access restrictions prevent reliable service, "
                    "even when its footfall forecast looks attractive."
                ),
            ],
            "table": {
                "caption": "Intake-to-Activation Evidence and Unit-Economics Matrix",
                "headers": [
                    "Operating workstream and accountable record",
                    "Required evidence before progressing the record",
                    "Concrete unit economics or operating capacity",
                    "Failure condition and practical operating fallback",
                ],
                "rows": [
                    [
                        "Authorized outbound ownership remains with the acquisition contractor",
                        "Document mailbox entitlement, source provenance, and global suppression synchronization",
                        "Three hundred inboxes produce 90,000 to 150,000 monthly attempts",
                        "Stop restricted sending and move only to an authorized production service",
                    ],
                    [
                        "Merchant qualification remains attached to one legal entity",
                        "Collect statements, ownership evidence, fulfillment timing, and refund procedures",
                        "A $100,000 monthly merchant at twenty retained basis points contributes $200",
                        "Reject unsupported volume claims and rebuild pricing from actual statements",
                    ],
                    [
                        "Schedule A pricing remains versioned beside signed commercial terms",
                        "Identify interchange treatment, assessments, processor charges, and referral deductions",
                        "Retained contribution equals contractual earnings after every applicable upstream deduction",
                        "Reprice or decline accounts whose support burden consumes the retained spread",
                    ],
                    [
                        "Sponsor underwriting owns acceptance of each merchant business model",
                        "Retain sponsor decision reference and current merchant-category approval evidence",
                        "Fifty applications less ten sponsor scrubs leave forty potential launches",
                        "Resolve evidence gaps without disguising business activity or changing identity",
                    ],
                    [
                        "MID configuration and gateway attachment share one approved identity",
                        "Verify descriptors, payment channels, refund permissions, and gateway fee schedules",
                        "Gateway contribution includes retained markup rather than underlying transaction settlement",
                        "Suspend inconsistent routing and restore the sponsor-approved configuration",
                    ],
                    [
                        "Venue contracting establishes exclusive access and surcharge allocation",
                        "Execute access rights, replenishment duties, termination provisions, and service expectations",
                        "Twenty venues retaining $200 monthly generate $4,000 monthly operator revenue",
                        "Replace inaccessible venues rather than assuming uninterrupted machine availability",
                    ],
                    [
                        "Terminal pricing and ATM disclosures require recorded acceptance tests",
                        "Capture credit pricing, debit treatment, ATM fee screens, and cancellation behavior",
                        "Customer-disclosed fees must reconcile to actual contractual retained fee amounts",
                        "Disable the affected pricing feature until corrected test evidence exists",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy durable residual quality rather than impressive application counts",
                "body": "Experienced operators underwrite the support burden and collection terms before celebrating booked volume.",
                "items": [
                    "Replay three actual merchant statements through the signed Schedule A before presenting savings; confirm the processor's residual export uses the same assessment treatment.",
                    "Tie every residual variance to MID, statement month, fee code, and contract version so a processor analyst can resolve it without another discovery call.",
                    "Ask ATM venues for access restrictions and event calendars before estimating withdrawals; attractive weekend traffic is useless when replenishment access closes early.",
                    "Keep a unified suppression registry across outbound tenants and vendors; continuity domains inherit every opt-out and complaint restriction immediately.",
                ],
            },
        },
        {
            "heading": "2. Implement the six-module production ledger and replay-safe workflow",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the six reference modules below as consecutive blocks in one local Python file. The reference "
                    "runs on Python 3.9 with SQLite and stores integer cents, explicit account pairs, source event "
                    "identifiers, and sponsor evidence. Every mutating function opens its own connection and executes "
                    "BEGIN IMMEDIATE before reading state or writing changes. SQLite therefore serializes writers "
                    "before the check-and-write sequence, eliminating local duplicate-insert and stale-state races "
                    "within this reference. Unique constraints remain the final defense against conflicting event "
                    "keys, merchant references, and bank matches. A busy writer causes a bounded database error "
                    "rather than silent partial execution; the caller may retry the identical request key. Use a "
                    "local filesystem with supported locking, not a shared network drive. PostgreSQL deployments "
                    "need equivalent transactions, row locking, uniqueness, and retry handling rather than a literal "
                    "copy of SQLite connection settings. Store documents in access-controlled storage and put only "
                    "opaque evidence references here. Never place PANs, security codes, raw identity documents, or "
                    "mailbox credentials into JSON payloads. The example is deliberately small enough to review, "
                    "but operational deployment still needs authenticated adapters, backups, restoration tests, "
                    "secret management, monitoring, and an access policy for every person who can alter records."
                ),
                (
                    "Separate verification from custody. The verification and escrow state machine records whether "
                    "a sponsor reports an external hold or release; it does not establish an operator escrow "
                    "account, accept merchant settlement funds, or authorize movement of vault cash. Received "
                    "applications become verified only with an external evidence reference. Verified records become "
                    "active only after a released or unnecessary hold is documented. A later suspension creates "
                    "another transition rather than editing past receipts. In the same transaction, each transition "
                    "writes an outbox instruction with a unique operation key. That makes database state and the "
                    "intent to notify IRIS CRM atomic, but it cannot make an arbitrary external API exactly-once. "
                    "A dispatcher must use provider-supported idempotency keys or query a durable remote operation "
                    "reference before retrying. After an ambiguous timeout without either capability, mark the "
                    "instruction for review and reconcile externally; do not blindly send it again. Verification "
                    "evidence must come from the authenticated sponsor adapter or an accountable reviewer, because "
                    "a nonempty text field alone proves nothing about underwriting. At the infrastructure boundary, "
                    "the honest promise is race-free local transitions plus controlled external replay, not an "
                    "impossible universal guarantee about systems outside the operator's control."
                ),
                (
                    "The monetary journal represents each posting as one balanced debit-credit pair. Recognized "
                    "residual earnings debit receivables and credit revenue; collections debit cash and credit "
                    "receivables; immediately settled ATM fees debit cash and credit revenue. Expenses debit "
                    "expense and credit cash, while contributed startup capital credits equity rather than revenue. "
                    "Each cash entry requires a matching imported bank movement with identical signed cents, and "
                    "a unique bank reference prevents matching the same movement twice. Residual recognition and "
                    "collection use different entry identifiers so a delayed payment cannot create duplicate "
                    "earnings. This compact reference accepts already normalized one-to-one bank movements; "
                    "production batch deposits require a separate allocation table with sum-to-bank validation "
                    "inside the same transaction. Refunds, reversals, receivable write-offs, and multi-line allocations "
                    "also require explicit extensions and tests before deployment. Never force those cases through "
                    "an unrelated expense category merely to make a screen balance. The reconciliation view exposes "
                    "cash, receivables, recognized revenue, expense, and equity by deal. QA checks database integrity, "
                    "foreign keys, negative receivables, unmatched bank movements, and ambiguous outbox work. Close "
                    "only after source statements, allocation detail, bank evidence, and journal totals agree; "
                    "a mathematically balanced journal can still contain an economically incorrect classification."
                ),
            ],
            "table": {
                "caption": "Six-Module Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and implementation boundary",
                    "Copy-pasteable Python and SQL reference",
                    "Operator input and execution contract",
                    "Race control and failure interpretation",
                ],
                "rows": [
                    [
                        "Module one creates constrained records and the serialized transaction primitive",
                        """import json
import sqlite3
from contextlib import contextmanager

DB = 'operator_ledger.sqlite3'

def connect():
    conn = sqlite3.connect(DB, timeout=5.0, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('PRAGMA busy_timeout = 5000')
    return conn

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))

@contextmanager
def transaction():
    conn = connect()
    try:
        conn.execute('BEGIN IMMEDIATE')
        yield conn
        conn.commit()
    except BaseException:
        if conn.in_transaction:
            conn.rollback()
        raise
    finally:
        conn.close()

conn = connect()
try:
    conn.execute('PRAGMA journal_mode = WAL')
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS deals (
        deal_id INTEGER PRIMARY KEY,
        external_ref TEXT NOT NULL UNIQUE,
        identity_json TEXT NOT NULL,
        score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
        state TEXT NOT NULL DEFAULT 'received'
            CHECK(state IN ('received','verified','active','suspended','rejected')),
        escrow_status TEXT NOT NULL DEFAULT 'unnecessary'
            CHECK(escrow_status IN ('unnecessary','held','released')),
        evidence_ref TEXT NOT NULL DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS events (
        event_id TEXT PRIMARY KEY NOT NULL,
        request_json TEXT NOT NULL,
        result_json TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS outbox (
        operation_key TEXT PRIMARY KEY NOT NULL,
        deal_id INTEGER NOT NULL REFERENCES deals(deal_id),
        payload_json TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'ready'
            CHECK(status IN ('ready','sent','review'))
    );
    CREATE TABLE IF NOT EXISTS bank (
        bank_ref TEXT PRIMARY KEY NOT NULL,
        signed_cents INTEGER NOT NULL CHECK(signed_cents <> 0)
    );
    CREATE TABLE IF NOT EXISTS journal (
        entry_id TEXT PRIMARY KEY NOT NULL,
        deal_id INTEGER NOT NULL REFERENCES deals(deal_id),
        kind TEXT NOT NULL,
        debit TEXT NOT NULL,
        credit TEXT NOT NULL,
        cents INTEGER NOT NULL CHECK(cents > 0),
        bank_ref TEXT UNIQUE REFERENCES bank(bank_ref),
        CHECK (
            (kind='recognize' AND debit='ar' AND credit='revenue'
                AND bank_ref IS NULL)
            OR (kind='collect' AND debit='cash' AND credit='ar'
                AND bank_ref IS NOT NULL)
            OR (kind='direct' AND debit='cash' AND credit='revenue'
                AND bank_ref IS NOT NULL)
            OR (kind='expense' AND debit='expense' AND credit='cash'
                AND bank_ref IS NOT NULL)
            OR (kind='fund' AND debit='cash' AND credit='equity'
                AND bank_ref IS NOT NULL)
        )
    );
    ''')
finally:
    conn.close()
""",
                        "Execute this block first on a local filesystem with reliable SQLite locking",
                        "Writer serialization precedes every state check; uniqueness rejects conflicting identities",
                    ],
                    [
                        "Module two scores evidence completeness and deduplicates immutable application intake",
                        """def intake(event_id, external_ref, identity):
    required = {'statements_checked', 'ownership_checked', 'sponsor_fit_checked'}
    if set(identity) != required or any(type(v) is not bool for v in identity.values()):
        raise ValueError('Provide the three boolean evidence checks')
    if not event_id or not external_ref:
        raise ValueError('Stable event and external references are required')
    score = (
        40 * identity['statements_checked']
        + 30 * identity['ownership_checked']
        + 30 * identity['sponsor_fit_checked']
    )
    identity_json = canonical(identity)
    request = canonical(['intake', external_ref, identity])
    with transaction() as conn:
        old = conn.execute(
            'SELECT request_json, result_json FROM events WHERE event_id=?',
            (event_id,)
        ).fetchone()
        if old:
            if old['request_json'] != request:
                raise ValueError('Event key reused with different intake data')
            return json.loads(old['result_json'])
        row = conn.execute(
            'SELECT deal_id, identity_json FROM deals WHERE external_ref=?',
            (external_ref,)
        ).fetchone()
        if row:
            if row['identity_json'] != identity_json:
                raise ValueError('Existing identity requires an explicit amendment workflow')
            deal_id = row['deal_id']
        else:
            cursor = conn.execute(
                'INSERT INTO deals(external_ref,identity_json,score) VALUES(?,?,?)',
                (external_ref, identity_json, score)
            )
            deal_id = cursor.lastrowid
        result = {'deal_id': deal_id, 'score': score}
        conn.execute(
            'INSERT INTO events(event_id,request_json,result_json) VALUES(?,?,?)',
            (event_id, request, canonical(result))
        )
        return result
""",
                        "Pass opaque merchant references and reviewer-confirmed checks, never sensitive documents",
                        "The score prioritizes work only and cannot replace sponsor underwriting acceptance",
                    ],
                    [
                        "Module three records verification and external escrow status with an atomic outbox",
                        """def transition(event_id, deal_id, target, escrow_status, evidence_ref):
    allowed = {
        'received': {'verified', 'rejected'},
        'verified': {'active', 'rejected'},
        'active': {'suspended'},
        'suspended': {'active', 'rejected'},
        'rejected': set(),
    }
    if not event_id or not evidence_ref:
        raise ValueError('Stable event key and verified external evidence are required')
    if escrow_status not in {'unnecessary', 'held', 'released'}:
        raise ValueError('Invalid external hold status')
    request = canonical(
        ['transition', deal_id, target, escrow_status, evidence_ref]
    )
    with transaction() as conn:
        old = conn.execute(
            'SELECT request_json,result_json FROM events WHERE event_id=?',
            (event_id,)
        ).fetchone()
        if old:
            if old['request_json'] != request:
                raise ValueError('Event key reused with different transition data')
            return json.loads(old['result_json'])
        row = conn.execute(
            'SELECT state FROM deals WHERE deal_id=?', (deal_id,)
        ).fetchone()
        if row is None or target not in allowed[row['state']]:
            raise ValueError('Invalid workflow transition')
        if target == 'active' and escrow_status == 'held':
            raise ValueError('Sponsor hold must be resolved before activation')
        conn.execute(
            'UPDATE deals SET state=?,escrow_status=?,evidence_ref=? WHERE deal_id=?',
            (target, escrow_status, evidence_ref, deal_id)
        )
        result = {'deal_id': deal_id, 'state': target, 'escrow_status': escrow_status}
        conn.execute(
            'INSERT INTO outbox(operation_key,deal_id,payload_json) VALUES(?,?,?)',
            (event_id, deal_id, canonical(result))
        )
        conn.execute(
            'INSERT INTO events(event_id,request_json,result_json) VALUES(?,?,?)',
            (event_id, request, canonical(result))
        )
        return result
""",
                        "An authenticated sponsor adapter supplies evidence and external hold determinations",
                        "Database state and outbox intent commit together; remote delivery needs independent idempotency",
                    ],
                    [
                        "Module four imports bank movements and posts balanced immutable monetary entries",
                        """PAIRS = {
    'recognize': ('ar', 'revenue'),
    'collect': ('cash', 'ar'),
    'direct': ('cash', 'revenue'),
    'expense': ('expense', 'cash'),
    'fund': ('cash', 'equity'),
}

def import_bank(bank_ref, signed_cents):
    if not bank_ref or type(signed_cents) is not int or signed_cents == 0:
        raise ValueError('Bank reference and nonzero integer cents are required')
    with transaction() as conn:
        old = conn.execute(
            'SELECT signed_cents FROM bank WHERE bank_ref=?', (bank_ref,)
        ).fetchone()
        if old:
            if old['signed_cents'] != signed_cents:
                raise ValueError('Bank reference changed its monetary amount')
            return
        conn.execute('INSERT INTO bank VALUES(?,?)', (bank_ref, signed_cents))

def post(entry_id, deal_id, kind, cents, bank_ref=None):
    if not entry_id or kind not in PAIRS or type(cents) is not int or cents <= 0:
        raise ValueError('Stable entry key, supported kind, and positive cents required')
    debit, credit = PAIRS[kind]
    expected = (deal_id, kind, debit, credit, cents, bank_ref)
    with transaction() as conn:
        old = conn.execute(
            'SELECT deal_id,kind,debit,credit,cents,bank_ref FROM journal WHERE entry_id=?',
            (entry_id,)
        ).fetchone()
        if old:
            if tuple(old) != expected:
                raise ValueError('Entry key reused with different monetary data')
            return
        if kind == 'recognize':
            if bank_ref is not None:
                raise ValueError('Accrual recognition cannot consume a bank movement')
        else:
            movement = conn.execute(
                'SELECT signed_cents FROM bank WHERE bank_ref=?', (bank_ref,)
            ).fetchone()
            signed = -cents if kind == 'expense' else cents
            if movement is None or movement['signed_cents'] != signed:
                raise ValueError('Cash posting requires an exact signed bank match')
        if kind == 'collect':
            outstanding = conn.execute(
                '''SELECT COALESCE(SUM(
                    CASE WHEN debit='ar' THEN cents
                         WHEN credit='ar' THEN -cents ELSE 0 END
                ),0) FROM journal WHERE deal_id=?''',
                (deal_id,)
            ).fetchone()[0]
            if cents > outstanding:
                raise ValueError('Collection exceeds this deal receivable')
        conn.execute(
            '''INSERT INTO journal
               (entry_id,deal_id,kind,debit,credit,cents,bank_ref)
               VALUES(?,?,?,?,?,?,?)''',
            (entry_id,) + expected
        )
""",
                        "Import normalized authenticated bank movements before matching corresponding cash entries",
                        "Duplicate keys replay safely; unique bank references prevent concurrent double matching",
                    ],
                    [
                        "Module five exposes reconciled economic balances without counting settlement principal",
                        """conn = connect()
try:
    conn.executescript('''
    CREATE VIEW IF NOT EXISTS reconciliation AS
    SELECT d.deal_id, d.external_ref,
        COALESCE(SUM(CASE WHEN j.debit='cash' THEN j.cents
                          WHEN j.credit='cash' THEN -j.cents ELSE 0 END),0) AS cash_cents,
        COALESCE(SUM(CASE WHEN j.debit='ar' THEN j.cents
                          WHEN j.credit='ar' THEN -j.cents ELSE 0 END),0) AS ar_cents,
        COALESCE(SUM(CASE WHEN j.credit='revenue' THEN j.cents ELSE 0 END),0) AS revenue_cents,
        COALESCE(SUM(CASE WHEN j.debit='expense' THEN j.cents ELSE 0 END),0) AS expense_cents,
        COALESCE(SUM(CASE WHEN j.credit='equity' THEN j.cents ELSE 0 END),0) AS equity_cents
    FROM deals d
    LEFT JOIN journal j ON j.deal_id=d.deal_id
    GROUP BY d.deal_id, d.external_ref;

    CREATE VIEW IF NOT EXISTS unmatched_bank AS
    SELECT b.bank_ref, b.signed_cents
    FROM bank b
    LEFT JOIN journal j ON j.bank_ref=b.bank_ref
    WHERE j.entry_id IS NULL;
    ''')
finally:
    conn.close()

def reconciliation_snapshot():
    conn = connect()
    try:
        return [dict(row) for row in conn.execute(
            'SELECT * FROM reconciliation ORDER BY deal_id'
        )]
    finally:
        conn.close()
""",
                        "Read retained residual receivables separately from settled cash and contributed equity",
                        "Views derive balances from immutable entries rather than editable cached totals",
                    ],
                    [
                        "Module six runs snapshot-consistent close checks and surfaces external delivery exceptions",
                        """def qa_close():
    with transaction() as conn:
        integrity = [row[0] for row in conn.execute('PRAGMA integrity_check')]
        if integrity != ['ok']:
            raise RuntimeError('SQLite integrity check failed')
        if conn.execute('PRAGMA foreign_key_check').fetchone():
            raise RuntimeError('Foreign key check failed')
        if conn.execute(
            'SELECT 1 FROM reconciliation WHERE ar_cents < 0 LIMIT 1'
        ).fetchone():
            raise RuntimeError('Negative receivable requires investigation')
        if conn.execute(
            '''SELECT 1 FROM reconciliation
               WHERE cash_cents + ar_cents
                   <> equity_cents + revenue_cents - expense_cents
               LIMIT 1'''
        ).fetchone():
            raise RuntimeError('Accounting equation failed')
        unmatched = conn.execute('SELECT COUNT(*) FROM unmatched_bank').fetchone()[0]
        review = conn.execute(
            "SELECT COUNT(*) FROM outbox WHERE status='review'"
        ).fetchone()[0]
        pending = conn.execute(
            "SELECT COUNT(*) FROM outbox WHERE status='ready'"
        ).fetchone()[0]
        if unmatched or review:
            raise RuntimeError(
                'Resolve unmatched bank movements and ambiguous external deliveries'
            )
        return {
            'database_checks': 'passed',
            'pending_outbox_operations': pending,
            'source_document_review': 'Required separately before financial close',
        }
""",
                        "Run after importing the complete period and separately reviewing source-document classifications",
                        "One serialized snapshot prevents changing totals during checks; pending deliveries remain visible",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four boundaries before activating live money workflows",
                "body": "These checks determine whether an account, integration, or period can advance safely.",
                "items": [
                    "Confirm the sponsor-approved entity, MCC, descriptor, channels, and underwriting evidence match the proposed MID configuration.",
                    "Verify signed Schedule A deductions, retained revenue treatment, gateway allocation, and venue surcharge sharing against actual sample statements.",
                    "Run simultaneous duplicate requests and conflicting-payload tests; require one local economic effect and explicit rejection of conflicting reuse.",
                    "Demonstrate bank matching, backup restoration, outbox timeout recovery, debit surcharge exclusion, and ATM fee cancellation before live activation.",
                ],
            },
        },
        {
            "heading": "3. Operate daily exceptions, dispute controls, and the monthly cash close",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start each day with three queues rather than a generic sales dashboard: applications missing "
                    "decision evidence, live accounts with changed risk signals, and money events without a matching "
                    "source. The owner handles sponsor relationships, pricing exceptions, and the final close. Three "
                    "contractors cover acquisition operations, onboarding and support, and ATM field service with "
                    "bookkeeping responsibilities allocated explicitly; their hours and scope belong in the cost "
                    "model. IRIS CRM can automate reminders and residual comparisons, but the processor statement "
                    "remains the economic source for earned residuals. Verifi RDR and Ethoca can reduce dispute "
                    "handling when supported by the processor and merchant setup. Their refunds, service fees, "
                    "and any overlap must be reconciled to the merchant and sponsor reports rather than presented "
                    "as free recovered revenue. Define a merchant-specific intervention threshold below the "
                    "applicable current program limit and assign a named reviewer. Suspicious transaction patterns "
                    "or a sponsor restriction stop affected processing through authorized controls. Do not move "
                    "transactions to another MID to hide the signal. The fallback is evidence collection, corrected "
                    "fulfillment, refund remediation, or an orderly sponsor-directed exit. MATCH exposure and "
                    "termination consequences make accurate onboarding more valuable than aggressively maximizing "
                    "the number of live accounts."
                ),
                (
                    "ATM operations need their own physical and monetary proof. Telemetry should distinguish low "
                    "cash, communications failure, dispenser faults, and an apparently online machine with rejected "
                    "withdrawals. Set replenishment triggers from expected withdrawals before the next authorized "
                    "visit, then add a documented demand buffer. A machine dispensing eighty $60 withdrawals "
                    "before service needs $4,800 of principal availability; a twenty-five percent buffer raises "
                    "that operating estimate to $6,000. That amount belongs in the vault-cash arrangement, not "
                    "the revenue forecast. Use insured cash logistics or another contractually approved replenishment "
                    "model, and assign responsibility for shortages and reconciliation. Under Regulation E, "
                    "12 CFR 1005.16, disclose the ATM fee on screen or paper before commitment and allow the "
                    "consumer to elect to continue; retain the tested flow and device configuration. Do not "
                    "invent a blanket exterior placard requirement from an obsolete rule. FinCEN classification "
                    "depends on the actual activities and custody structure, so evaluate expanded transfer or "
                    "exchange services separately under 31 CFR 1010.100. A conventional withdrawal-only installation "
                    "does not justify copying the regulatory treatment of a different money-services business. "
                    "After an outage, reconcile successful dispenses, reversals, surcharge events, and settlement "
                    "reports before booking the day's retained earnings."
                ),
                (
                    "Close processing residuals by statement month, not by the day the bank deposit happens "
                    "to arrive. Load the signed Schedule A, expected merchant population, current gateway pricing, "
                    "and venue revenue-share schedules into the comparison process. Calculate expected retained "
                    "earnings, explain every material difference, and recognize only supportable earned amounts. "
                    "A processor reserve or disputed adjustment stays visible as a separate receivable issue; "
                    "merchant funds held by the sponsor do not become an ISO expense or cash asset merely "
                    "because a dashboard displays them. Match deposits against remittance identifiers and investigate "
                    "short payments before marking invoices collected. For the Base model, annual recognized "
                    "operator revenue is $445,000 and total operating costs are $255,875, leaving $189,125. "
                    "The monthly equivalent is $37,083.333 recurring revenue and $21,322.917 total costs. The "
                    "quoted $1,500–$10,000 monthly opex range therefore cannot be treated as the entire Base "
                    "expense envelope; this walkthrough interprets it as recurring nonlabor overhead and separately "
                    "budgets labor and delivery costs. That interpretation is an explicit modeling assumption, "
                    "not an additional scorecard fact. Retention work then targets merchants whose net contribution "
                    "survives service cost, repricing pressure, and expected attrition, rather than preserving "
                    "unprofitable volume for a presentation."
                ),
            ],
            "table": {
                "caption": "Daily Production Exceptions, Evidence Owners, and Monthly Close Controls",
                "headers": [
                    "Production control and accountable operating role",
                    "Evidence source and required reconciliation detail",
                    "Unit calculation or measurable decision rule",
                    "Exception response and documented completion evidence",
                ],
                "rows": [
                    [
                        "Application contractor clears missing documents before sponsor submission",
                        "IRIS CRM checklist links directly to restricted evidence references",
                        "Application completeness score measures evidence availability rather than credit approval",
                        "Return incomplete applications without representing them as sponsor-approved accounts",
                    ],
                    [
                        "Owner reviews sponsor restrictions and merchant chargeback trend changes",
                        "Sponsor reports identify merchant category, program status, and investigation requests",
                        "Set internal intervention thresholds below current applicable sponsor program limits",
                        "Suspend affected activity through authorized controls and preserve investigation evidence",
                    ],
                    [
                        "Support contractor reconciles Verifi RDR and Ethoca events",
                        "Match alert identifiers, refund records, service charges, and processor reports",
                        "Count retained benefit after refunds and provider charges rather than gross alerts",
                        "Investigate overlapping alerts before enabling additional automatic refund pathways",
                    ],
                    [
                        "Field-service contractor monitors remote ATM health and replenishment requirements",
                        "Telemetry combines dispenser status, withdrawal events, cash levels, and access windows",
                        "Eighty $60 withdrawals plus twenty-five percent buffer require $6,000 availability",
                        "Dispatch approved service and reconcile reversals before recognizing retained fees",
                    ],
                    [
                        "Bookkeeping contractor audits monthly residuals against signed Schedule A",
                        "Compare MID-level fee codes, assessments, referral shares, and contractual adjustments",
                        "A twenty-basis-point retained spread on $100,000 yields $200 monthly contribution",
                        "Open itemized processor disputes instead of overwriting original earnings records",
                    ],
                    [
                        "Owner closes bank cash separately from earned residual receivables",
                        "Tie remittance references and normalized bank movements to unique journal entries",
                        "Every matched cash event consumes one bank movement exactly once",
                        "Hold unexplained deposits in the exception workflow until classification is evidenced",
                    ],
                    [
                        "Owner renews accounts using contribution and service-burden evidence",
                        "Combine contract renewal dates, support time, rate requests, and residual trends",
                        "Repricing must preserve positive retained contribution after incremental support costs",
                        "Offer justified pricing changes or execute a documented orderly account exit",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Intake and price the actual activity",
                    "action": "Create the merchant or venue record and attach source-document references.",
                    "detail": "Calculate retained unit economics from signed terms; separate settlement principal, gateway markup, surcharge sharing, and operating costs.",
                },
                {
                    "step": 2,
                    "title": "Verify and activate the approved configuration",
                    "action": "Record sponsor evidence, resolve external holds, and test the payment or ATM flow.",
                    "detail": "Confirm descriptors, debit treatment, surcharge displays, ATM cancellation behavior, and authorized venue access before activation.",
                },
                {
                    "step": 3,
                    "title": "Monitor exceptions and recognize earned contribution",
                    "action": "Review daily dispute, telemetry, outbox, and statement-matching queues.",
                    "detail": "Use stable source identifiers and immutable postings; escalate ambiguous external calls rather than repeating unsupported side effects.",
                },
                {
                    "step": 4,
                    "title": "Collect, reconcile, and renew",
                    "action": "Match deposits to receivables, run close checks, and review account profitability.",
                    "detail": "Resolve every material variance, retain source evidence, and allocate retention effort to economically durable merchants and venues.",
                },
            ],
        },
        {
            "heading": "4. Walk a 90-day cohort from signed applications to the Base run rate",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The worked cohort is a transparent illustration, not a claim that an unseasoned pipeline "
                    "normally reaches the Base case in ninety days. It assumes existing referral access, sponsor "
                    "capacity, and progressively weighted activation within each month. The merchant counts below "
                    "are full-month-equivalent earning accounts; actual calendar activations must be prorated before "
                    "using the model. Month 1 processes 400 qualified leads into fifty applications, removes ten "
                    "underwriting scrubs and four failed launches, and produces thirty-six earning merchant "
                    "equivalents. Month 2 adds sixty-five applications from 600 leads, scrubs fifteen, and loses "
                    "one existing account, reaching eighty-five equivalents. Month 3 adds eighty-five applications "
                    "from 800 leads, scrubs seventeen, and loses three existing accounts, reaching 150. At "
                    "$200 retained monthly per earning merchant, processing contributes $7,200, $17,000, and "
                    "$30,000. Retained gateway contributions add $800, $2,000, and $3,083.33. Thus processing "
                    "and gateway earnings total $8,000, $19,000, and $33,083.33. The scenario assumes those "
                    "earnings settle in the following month and that ATM retained fees settle within the "
                    "earning month. Different sponsor remittance calendars require a different cash bridge, "
                    "even when recognized revenue is unchanged."
                ),
                (
                    "ATM retained fees contribute $1,000 in Month 1, $2,500 in Month 2, and $4,000 "
                    "in Month 3. One supporting venue mix is five venues at $200, ten venues at "
                    "$250 during a stronger event month, and twenty venues at a normalized $200. The "
                    "model does not assume the Month 2 event uplift persists. Revenue after documented "
                    "pre-recognition adjustments is therefore $9,000, $21,500, and $37,083.33. Provisional "
                    "processing and gateway estimates of $8,600, $20,200, and $35,083.33 are reduced by "
                    "$600, $1,200, and $2,000 respectively for evidenced contractual deductions and corrections; "
                    "these amounts are already excluded from recognized revenue and must not be deducted "
                    "again as cash losses. Application scrubs and merchant attrition are likewise already "
                    "embedded in earning-account counts. This illustration assumes no additional receivable "
                    "default; an actual default would reduce profit and require a write-off extension to "
                    "the reference ledger. Cash receipts are only $1,000, $10,500, and $23,000 because "
                    "processing collections lag. Against cash operating costs of $9,000, $15,000, and "
                    "$21,322.92, monthly operating cash flow is negative $8,000, negative $4,500, and "
                    "positive $1,677.08. The difference between earnings and cash is the surviving receivable, "
                    "not hidden profitability."
                ),
                (
                    "Fund the illustration with $35,000 of owner capital and spend $12,000 at inception "
                    "on startup assets and deposits, assumed capitalized for this cash bridge and excluded "
                    "from recurring operating expense. The $23,000 opening cash balance falls to $15,000 "
                    "after Month 1, $10,500 after Month 2, and recovers to $12,177.08 after Month "
                    "3. Cumulative operating cash flow is negative $10,822.92; including startup uses, "
                    "cumulative project cash flow is negative $22,822.92. Three-month recognized revenue "
                    "of $67,583.33 less $45,322.92 operating costs produces $22,260.41 operating profit. "
                    "Subtract the $33,083.33 closing receivable and the same negative operating cash "
                    "flow appears. In steady Month 4, prior-month residual collections plus current ATM "
                    "receipts reach $37,083.33, supporting approximately $15,760.42 monthly owner profit "
                    "at a 42.5% margin. Use exact annual values and year-end penny adjustments rather "
                    "than annualizing rounded monthly cents. The Base annual composition is $360,000 "
                    "processing, $37,000 gateway, and $48,000 ATM contribution. Conservative remains "
                    "$90,000 revenue with $63,000 costs; Scaled remains $800,000 revenue with "
                    "$360,000 costs. Scaling requires another full-time role and a fourth contractor, "
                    "not merely multiplying the outbound estate while ignoring service capacity."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period, cohort construction, and scrub treatment",
                    "Recognized retained revenue and cash collection timing",
                    "Operating costs and incremental operating cash flow",
                    "Cumulative cash position and reconciliation evidence",
                ],
                "rows": [
                    [
                        "Startup: contribute $35,000 owner equity before funding the initial deployment",
                        "Owner capital is financing cash rather than recognized operator revenue",
                        "Spend $12,000 on assumed capitalized startup assets and deposits",
                        "Opening operating cash equals $23,000; cumulative project cash flow equals negative $12,000",
                    ],
                    [
                        "Month 1: 400 leads; 50 applications less 10 scrubs and 4 failed launches yield 36 earning merchants",
                        "$7,200 processing plus $800 gateway plus $1,000 ATM equals $9,000 revenue; collect $1,000",
                        "$9,000 cash operating costs produce negative $8,000 monthly operating cash flow",
                        "Ending cash is $15,000; receivables are $8,000; cumulative project cash flow is negative $20,000",
                    ],
                    [
                        "Month 2: 600 leads; 65 applications less 15 scrubs plus 36 opening merchants less 1 attrition yield 85",
                        "$17,000 processing plus $2,000 gateway plus $2,500 ATM equals $21,500 revenue; collect $10,500",
                        "$15,000 cash operating costs produce negative $4,500 monthly operating cash flow",
                        "Ending cash is $10,500; receivables are $19,000; cumulative project cash flow is negative $24,500",
                    ],
                    [
                        "Month 3: 800 leads; 85 applications less 17 scrubs plus 85 opening merchants less 3 attrition yield 150",
                        "$30,000 processing plus $3,083.33 gateway plus $4,000 ATM equals $37,083.33 revenue; collect $23,000",
                        "$21,322.92 cash operating costs produce positive $1,677.08 monthly operating cash flow",
                        "Ending cash is $12,177.08; receivables are $33,083.33; cumulative project cash flow is negative $22,822.92",
                    ],
                    [
                        "Ninety-day total: 1,800 leads and 200 applications include 42 underwriting scrubs",
                        "$67,583.33 recognized revenue and $34,500 collected cash differ by $33,083.33 closing receivables",
                        "$45,322.92 total operating costs produce $22,260.41 profit and negative $10,822.92 operating cash flow",
                        "$35,000 capital less $12,000 startup uses less $10,822.92 operating cash consumption equals $12,177.08",
                    ],
                    [
                        "Month 4 steady state: replace attrition while retaining 150 merchant equivalents and twenty normalized venues",
                        "Collect $33,083.33 prior residuals plus $4,000 current ATM fees, totaling $37,083.33 cash",
                        "Rounded $21,322.92 costs produce $15,760.41 cash contribution before annual penny adjustments",
                        "Illustrative ending cash rises to $27,937.49 while recurring receivables remain $33,083.33",
                    ],
                    [
                        "Base annual bridge: $360,000 processing plus $37,000 gateway plus $48,000 ATM retained contribution",
                        "Annual recognized operator revenue equals exactly $445,000, excluding settlement volume and vault principal",
                        "Annual operating costs equal $255,875; annual owner profit equals $189,125 at 42.5%",
                        "One full-time operator and three contractors support the canonical Base staffing envelope",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "An account becomes valuable when its approved economics survive the journey from source statement to reconciled cash.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one merchant identity record and one venue record with signed pricing, sponsor evidence, source references, and accountable owners.",
        "Validate outbound production entitlements and global suppression before testing the multi_inbox_free_workspace_outbound_clusters capacity arithmetic.",
        "Assemble the six reference blocks in a sandbox and test duplicate events, conflicting payloads, concurrent transitions, duplicate bank matches, and restoration.",
        "Verify credit surcharge displays, debit exclusions, sponsor-approved routing, ATM fee acceptance, and venue replenishment access using recorded test evidence.",
        "Build the Month 1 through Month 3 cohort using earning-account equivalents, explicit scrubs, contractual deductions, cash lags, and funded startup uses.",
        "Close residuals against source statements and bank receipts, then reconcile the annual Base totals to $445,000 revenue and $189,125 owner profit.",
    ],
    "statutory_citations": [
        {
            "title": "12 CFR 1005.16 — Disclosures at automated teller machines",
            "url": "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.16",
            "relevance": "Requires applicable ATM fee disclosure before commitment and the consumer's election to continue; informs screen-flow testing and retained configuration evidence.",
        },
        {
            "title": "15 U.S.C. 1693o-2 — Reasonable fees and rules for payment card transactions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1693o-2",
            "relevance": "Establishes the statutory debit interchange and routing framework; evaluate it alongside network surcharge rules rather than treating it as permission to surcharge debit cards.",
        },
        {
            "title": "12 CFR 235.7 — Limitations on payment card restrictions",
            "url": "https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-235/section-235.7",
            "relevance": "Provides debit network exclusivity and routing requirements relevant to processor configurations and merchant routing controls.",
        },
        {
            "title": "15 U.S.C. 7704 — Other protections for users of commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs commercial email routing information, subject lines, required disclosures, and opt-out handling across every outbound tenant and vendor.",
        },
        {
            "title": "New York General Business Law section 518 — Credit card surcharge disclosure",
            "url": "https://www.nysenate.gov/legislation/laws/GBS/518",
            "relevance": "Requires evaluation of New York credit-card surcharge amounts and customer-facing total-price displays before enabling merchant pricing configurations.",
        },
        {
            "title": "31 CFR 1010.100 — General definitions",
            "url": "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/section-1010.100",
            "relevance": "Defines money-services business categories and related terms; classify actual ATM, transfer, exchange, and custody activities rather than assuming all equipment deployments receive identical treatment.",
        },
    ],
}
