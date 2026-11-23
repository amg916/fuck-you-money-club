from __future__ import annotations

_SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS claims (
    claim_id TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    invoice_key TEXT NOT NULL,
    play TEXT NOT NULL,
    cohort TEXT NOT NULL,
    source_sha256 TEXT NOT NULL CHECK(length(source_sha256) = 64),
    recoverable_cents INTEGER NOT NULL CHECK(recoverable_cents > 0),
    fee_bps INTEGER NOT NULL CHECK(fee_bps BETWEEN 1 AND 5000),
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    state TEXT NOT NULL DEFAULT 'held'
        CHECK(state IN ('held', 'verified', 'submitted', 'settled',
                        'invoiced', 'void')),
    external_ref TEXT UNIQUE,
    UNIQUE(client_id, invoice_key, play)
);

CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    claim_id TEXT NOT NULL REFERENCES claims(claim_id),
    kind TEXT NOT NULL,
    payload_sha256 TEXT NOT NULL CHECK(length(payload_sha256) = 64),
    evidence_json TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT
        (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE TABLE IF NOT EXISTS postings (
    event_id TEXT PRIMARY KEY REFERENCES events(event_id),
    claim_id TEXT NOT NULL REFERENCES claims(claim_id),
    debit_account TEXT NOT NULL,
    credit_account TEXT NOT NULL,
    amount_cents INTEGER NOT NULL CHECK(amount_cents > 0),
    CHECK(
        (debit_account = 'AR' AND credit_account = 'REVENUE')
        OR
        (debit_account = 'CASH' AND credit_account = 'AR')
    )
);

CREATE UNIQUE INDEX IF NOT EXISTS one_earning_per_claim
    ON postings(claim_id)
    WHERE credit_account = 'REVENUE';

CREATE INDEX IF NOT EXISTS events_by_claim
    ON events(claim_id, created_at);

CREATE INDEX IF NOT EXISTS postings_by_claim
    ON postings(claim_id);
"""

_INTAKE_PY = """
import hashlib
import json
from datetime import date


def intake(db, claim_id, client_id, invoice_key, play, cohort,
           source_sha256, recoverable_cents, fee_bps, facts):
    if not all(isinstance(value, str) and value.strip()
               for value in (claim_id, client_id, invoice_key, play)):
        raise ValueError('Nonempty claim identities are required')
    if date.fromisoformat(cohort + '-01').strftime('%Y-%m') != cohort:
        raise ValueError('Use an ISO year-month cohort')
    if (len(source_sha256) != 64 or
            any(c not in '0123456789abcdef' for c in source_sha256)):
        raise ValueError('Use the immutable source SHA-256 digest')
    if type(recoverable_cents) is not int or recoverable_cents <= 0:
        raise ValueError('Recovery must be positive integer cents')
    if type(fee_bps) is not int or not 1 <= fee_bps <= 5000:
        raise ValueError('Fee basis points must be between 1 and 5000')

    weights = {
        'authorization_signed': 25,
        'baseline_locked': 25,
        'deadline_open': 20,
        'contract_eligible': 20,
        'payer_identified': 10,
    }
    if set(facts) != set(weights):
        raise ValueError('Supply every named scoring fact exactly once')
    if any(type(value) is not bool for value in facts.values()):
        raise ValueError('Scoring facts must be actual booleans')
    score = sum(weight for name, weight in weights.items() if facts[name])
    payload = {
        'claim_id': claim_id,
        'client_id': client_id,
        'invoice_key': invoice_key,
        'play': play,
        'cohort': cohort,
        'source_sha256': source_sha256,
        'recoverable_cents': recoverable_cents,
        'fee_bps': fee_bps,
        'facts': facts,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    digest = hashlib.sha256(encoded.encode('utf-8')).hexdigest()
    event_id = 'intake:' + claim_id
    values = (
        claim_id, client_id, invoice_key, play, cohort, source_sha256,
        recoverable_cents, fee_bps, score,
    )

    db.execute('BEGIN IMMEDIATE')
    try:
        prior = db.execute(
            'SELECT payload_sha256 FROM events WHERE event_id = ?',
            (event_id,),
        ).fetchone()
        if prior:
            if prior[0] != digest:
                raise ValueError('An intake key cannot change its payload')
            db.commit()
            return claim_id

        db.execute(
            'INSERT INTO claims '
            '(claim_id, client_id, invoice_key, play, cohort, source_sha256, '
            'recoverable_cents, fee_bps, score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            values,
        )
        db.execute(
            'INSERT INTO events '
            '(event_id, claim_id, kind, payload_sha256, evidence_json) '
            'VALUES (?, ?, ?, ?, ?)',
            (event_id, claim_id, 'intake', digest, encoded),
        )
        db.commit()
        return claim_id
    except BaseException:
        db.rollback()
        raise
"""

_WORKFLOW_PY = """
import hashlib
import json


def _encoded(payload):
    text = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    return text, hashlib.sha256(text.encode('utf-8')).hexdigest()


def _evidence(evidence):
    if not isinstance(evidence, dict):
        raise ValueError('Evidence must be a structured object')
    digest = evidence.get('document_sha256', '')
    if (not isinstance(digest, str) or len(digest) != 64 or
            any(c not in '0123456789abcdef' for c in digest)):
        raise ValueError('Attach a verified document SHA-256 digest')
    if not isinstance(evidence.get('reviewer'), str):
        raise ValueError('Name the responsible evidence reviewer')
    if not evidence['reviewer'].strip():
        raise ValueError('Reviewer identity must be nonempty')


def _replay(db, event_id, digest):
    row = db.execute(
        'SELECT payload_sha256 FROM events WHERE event_id = ?',
        (event_id,),
    ).fetchone()
    if row and row[0] != digest:
        raise ValueError('An event key cannot change its payload')
    return bool(row)


def advance(db, event_id, claim_id, target, evidence, external_ref=None):
    if not isinstance(event_id, str) or not event_id.startswith('step:'):
        raise ValueError('Transition keys must use the step namespace')
    _evidence(evidence)
    allowed = {
        'held': {'verified', 'void'},
        'verified': {'submitted', 'void'},
        'submitted': {'settled', 'void'},
        'settled': {'invoiced'},
        'invoiced': set(),
        'void': set(),
    }
    payload = {
        'claim_id': claim_id,
        'target': target,
        'evidence': evidence,
        'external_ref': external_ref,
    }
    text, digest = _encoded(payload)
    db.execute('BEGIN IMMEDIATE')
    try:
        if _replay(db, event_id, digest):
            db.commit()
            return
        row = db.execute(
            'SELECT state, score, recoverable_cents, fee_bps, external_ref '
            'FROM claims WHERE claim_id = ?',
            (claim_id,),
        ).fetchone()
        if row is None:
            raise ValueError('Claim must exist before transition')
        state, score, recovery, fee_bps, existing_ref = row
        if target not in allowed[state]:
            raise ValueError('Transition is outside the state graph')
        if target == 'verified' and score != 100:
            raise ValueError('Every intake fact must pass before verification')
        if target == 'submitted':
            if not isinstance(external_ref, str) or not external_ref.strip():
                raise ValueError('Record the provider-qualified acknowledgement')
        elif external_ref is not None:
            raise ValueError('External references belong to submission events')
        if target == 'settled':
            actual = evidence.get('actual_recovery_cents')
            if type(actual) is not int or actual != recovery:
                raise ValueError('Settlement mismatch requires reviewed rework')
        if target == 'invoiced':
            if evidence.get('performance_complete') is not True:
                raise ValueError('Document completed contractual performance')
            if evidence.get('unconditional_fee_right') is not True:
                raise ValueError('Document the unconditional fee receivable')

        db.execute(
            'INSERT INTO events '
            '(event_id, claim_id, kind, payload_sha256, evidence_json) '
            'VALUES (?, ?, ?, ?, ?)',
            (event_id, claim_id, target, digest, text),
        )
        ref = external_ref if target == 'submitted' else existing_ref
        changed = db.execute(
            'UPDATE claims SET state = ?, external_ref = ? '
            'WHERE claim_id = ? AND state = ?',
            (target, ref, claim_id, state),
        ).rowcount
        if changed != 1:
            raise RuntimeError('State compare-and-swap failed')
        if target == 'invoiced':
            fee = (recovery * fee_bps + 5000) // 10000
            if fee <= 0:
                raise ValueError('Rounded fee must be positive')
            db.execute(
                'INSERT INTO postings '
                '(event_id, claim_id, debit_account, credit_account, amount_cents) '
                'VALUES (?, ?, ?, ?, ?)',
                (event_id, claim_id, 'AR', 'REVENUE', fee),
            )
        db.commit()
    except BaseException:
        db.rollback()
        raise


def receive(db, claim_id, bank_transaction_id, amount_cents, evidence):
    _evidence(evidence)
    if not isinstance(bank_transaction_id, str) or not bank_transaction_id.strip():
        raise ValueError('Use an account-qualified immutable bank transaction ID')
    if type(amount_cents) is not int or amount_cents <= 0:
        raise ValueError('Receipt must be positive integer cents')
    event_id = 'bank:' + bank_transaction_id
    payload = {
        'claim_id': claim_id,
        'bank_transaction_id': bank_transaction_id,
        'amount_cents': amount_cents,
        'evidence': evidence,
    }
    text, digest = _encoded(payload)
    db.execute('BEGIN IMMEDIATE')
    try:
        if _replay(db, event_id, digest):
            db.commit()
            return
        row = db.execute(
            'SELECT state FROM claims WHERE claim_id = ?', (claim_id,)
        ).fetchone()
        if row is None or row[0] != 'invoiced':
            raise ValueError('A fee receivable must precede allocation')
        balance = db.execute(
            'SELECT COALESCE(SUM(CASE WHEN debit_account = ? '
            'THEN amount_cents ELSE -amount_cents END), 0) '
            'FROM postings WHERE claim_id = ?',
            ('AR', claim_id),
        ).fetchone()[0]
        if amount_cents > balance:
            raise ValueError('Receipt exceeds the open fee receivable')
        db.execute(
            'INSERT INTO events '
            '(event_id, claim_id, kind, payload_sha256, evidence_json) '
            'VALUES (?, ?, ?, ?, ?)',
            (event_id, claim_id, 'receipt', digest, text),
        )
        db.execute(
            'INSERT INTO postings '
            '(event_id, claim_id, debit_account, credit_account, amount_cents) '
            'VALUES (?, ?, ?, ?, ?)',
            (event_id, claim_id, 'CASH', 'AR', amount_cents),
        )
        db.commit()
    except BaseException:
        db.rollback()
        raise
"""

_RECONCILIATION_SQL = """
CREATE VIEW IF NOT EXISTS claim_reconciliation AS
SELECT
    c.claim_id,
    c.client_id,
    c.cohort,
    c.state,
    COALESCE(SUM(
        CASE WHEN p.credit_account = 'REVENUE'
        THEN p.amount_cents ELSE 0 END
    ), 0) AS earned_fee_cents,
    COALESCE(SUM(
        CASE WHEN p.debit_account = 'CASH'
        THEN p.amount_cents ELSE 0 END
    ), 0) AS received_fee_cents,
    COALESCE(SUM(
        CASE WHEN p.debit_account = 'AR'
        THEN p.amount_cents
        WHEN p.credit_account = 'AR'
        THEN -p.amount_cents
        ELSE 0 END
    ), 0) AS receivable_cents
FROM claims AS c
LEFT JOIN postings AS p ON p.claim_id = c.claim_id
GROUP BY c.claim_id, c.client_id, c.cohort, c.state;
"""

_QA_PY = """
def check(db):
    db.execute('BEGIN')
    try:
        if db.execute('PRAGMA integrity_check').fetchall() != [('ok',)]:
            raise RuntimeError('SQLite structural integrity failed')
        if db.execute('PRAGMA foreign_key_check').fetchall():
            raise RuntimeError('Ledger foreign-key integrity failed')

        bad_balances = db.execute(
            'SELECT claim_id FROM claim_reconciliation '
            'WHERE receivable_cents < 0 '
            'OR earned_fee_cents != received_fee_cents + receivable_cents'
        ).fetchall()
        if bad_balances:
            raise RuntimeError('Fee roll-forward failed: ' + repr(bad_balances))

        bad_states = db.execute(
            'SELECT claim_id FROM claim_reconciliation '
            'WHERE (state = ? AND earned_fee_cents <= 0) '
            'OR (state != ? AND earned_fee_cents != 0)',
            ('invoiced', 'invoiced'),
        ).fetchall()
        if bad_states:
            raise RuntimeError('Earning state mismatch: ' + repr(bad_states))

        bad_events = db.execute(
            'SELECT p.event_id FROM postings AS p '
            'JOIN events AS e ON e.event_id = p.event_id '
            'WHERE p.claim_id != e.claim_id '
            'OR (p.credit_account = ? AND e.kind != ?) '
            'OR (p.debit_account = ? AND e.kind != ?)',
            ('REVENUE', 'invoiced', 'CASH', 'receipt'),
        ).fetchall()
        if bad_events:
            raise RuntimeError('Posting evidence mismatch: ' + repr(bad_events))
        db.commit()
        return {
            'integrity': 'passed',
            'fee_roll_forward': 'passed',
            'state_alignment': 'passed',
            'event_alignment': 'passed',
        }
    except BaseException:
        db.rollback()
        raise
"""

_RUNNER_PY = """
import argparse
import json
import sqlite3
from pathlib import Path

from intake import intake
from workflow import advance, receive
from qa import check


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('database')
    parser.add_argument(
        'action',
        choices=('init', 'intake', 'advance', 'receive', 'report', 'qa'),
    )
    parser.add_argument('--payload', default='{}')
    args = parser.parse_args()
    payload = json.loads(args.payload)
    root = Path(__file__).resolve().parent
    db = sqlite3.connect(args.database, timeout=30, isolation_level=None)
    try:
        db.execute('PRAGMA foreign_keys = ON')
        db.execute('PRAGMA busy_timeout = 30000')
        db.execute('PRAGMA journal_mode = WAL')
        db.execute('PRAGMA synchronous = FULL')
        if args.action == 'init':
            sql = (
                (root / 'schema.sql').read_text(encoding='utf-8')
                + '\\n'
                + (root / 'reconciliation.sql').read_text(encoding='utf-8')
            )
            try:
                db.executescript('BEGIN IMMEDIATE;\\n' + sql + '\\nCOMMIT;')
            except BaseException:
                if db.in_transaction:
                    db.rollback()
                raise
            print('Schema and reconciliation view initialized')
        elif args.action == 'intake':
            print(intake(db, **payload))
        elif args.action == 'advance':
            advance(db, **payload)
            print('Transition committed or matching replay accepted')
        elif args.action == 'receive':
            receive(db, **payload)
            print('Receipt committed or matching replay accepted')
        elif args.action == 'qa':
            print(json.dumps(check(db), sort_keys=True))
        else:
            rows = db.execute(
                'SELECT cohort, SUM(earned_fee_cents), '
                'SUM(received_fee_cents), SUM(receivable_cents) '
                'FROM claim_reconciliation GROUP BY cohort ORDER BY cohort'
            ).fetchall()
            print(json.dumps(rows))
    finally:
        db.close()


if __name__ == '__main__':
    main()
"""

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort-walk",
    "question_prompt": (
        "How does an operator execute contingent corporate bill-audit & tax-credit "
        "recovery end-to-end from intake to reconciled cash, backed by an auditable "
        "technical/ledger blueprint and a worked 90-day cohort walk?"
    ),
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": (
        "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk"
    ),
    "subtitle": (
        "FedEx/UPS Eligibility, Utility Baselines, Form 8850 Timing, IRC Section "
        "179D Allocation Evidence, and a Transactional SQLite Fee Subledger"
    ),
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #38, Contingent Corporate Bill-Audit & Tax-Credit Recovery, "
        "holds Rank #06 of 42 with a Money-to-Manpower Score of 94/100. This "
        "chapter turns 12 mapped plays into one controlled production line: "
        "authorize access, freeze evidence, verify eligibility, submit once, "
        "prove client benefit, earn the fee, and reconcile operator cash. Six "
        "copy-pasteable engineering modules define a transactional SQLite "
        "subledger without treating client recoveries as operator revenue. "
        "The worked cohort earns $126,250 over 90 days, exactly one quarter "
        "of the $505,000 Base revenue case, while exposing collection lag "
        "and $10,000 closing receivables. Annual owner profit remains "
        "$33,000 Conservative, $217,150 Base, and $504,000 Scaled; tax-service "
        "restrictions determine compensation structure before any engagement starts."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": (
                "Annual earned operator fees; excludes client bills, recovered "
                "principal, and deduction amounts"
            ),
            "note": (
                "30% net margin; $33,000 annual owner net profit; "
                "1 FT + 3 C"
            ),
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": (
                "Annual earned contingency shares, shared-savings fees, and "
                "processing revenue"
            ),
            "note": (
                "43.0% net margin; $217,150 annual owner net profit; "
                "1 FT + 3 C"
            ),
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": (
                "Annual earned operator revenue, never underlying customer "
                "spend or tax benefits"
            ),
            "note": (
                "56% net margin; $504,000 annual owner net profit; "
                "2 FT + 4 C, six people total"
            ),
        },
    ],
    "sections": [
        {
            "heading": (
                "1. Convert twelve recovery plays into authorized, "
                "evidence-complete work packets"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a signed engagement, a narrowly scoped Letter of "
                    "Authorization, and a baseline invoice snapshot before revealing "
                    "recoverable findings. Record the legal customer, billing account, "
                    "service location, covered period, permitted access method, "
                    "submission deadline, fee trigger, and refund destination. The "
                    "customer receives the supplier refund directly; the operator "
                    "separately invoices an earned service fee. Obtain FedEx or UPS "
                    "contract schedules before testing service guarantees because a "
                    "negotiated waiver can erase an apparently attractive late-delivery "
                    "claim. Use authorized EDI exports or documented carrier interfaces "
                    "where access exists, rather than assuming every developer account "
                    "includes refund submission. For utilities, preserve tariff sheets, "
                    "meter identifiers, interval histories, sewer factors, and municipal "
                    "credit policies. Freeze original files with SHA-256 digests; retain "
                    "OCR output as a derivative, never as the sole evidence. Intake "
                    "scores authorization and baseline integrity at 25 points each, "
                    "deadline and contract eligibility at 20 each, and an identified "
                    "payer at ten. A score below 100 can prioritize remediation but "
                    "cannot authorize submission. This deliberately separates sales "
                    "enthusiasm from production readiness and makes rejected work "
                    "visible before contractors spend scarce review hours."
                ),
                (
                    "Map the shelf into twelve operational lanes, not twelve different "
                    "businesses. Parcel service refunds, duplicate parcel charges, and "
                    "dimensional corrections share invoice ingestion but require "
                    "different evidence. Utility tariff changes, cooling-tower sewer "
                    "abatements, utility tax exemptions, waste true-ups, and telecom "
                    "disconnects share site ownership records but not eligibility rules. "
                    "Property assessment appeals need jurisdiction-specific authority "
                    "and qualified representation. WOTC processing, specialty-credit "
                    "documentation, and Section 179D allocation support belong in "
                    "separate tax-service workspaces with distinct fee terms. The "
                    "matrix supplies illustrative unit economics for all twelve; only "
                    "the refund lanes enter the worked cohort. A $20,000 verified "
                    "supplier recovery at 25% produces $5,000 of operator revenue, "
                    "not $20,000. A $1,000 monthly verified saving at a 30% split "
                    "produces $300 per qualifying month, not an immediate $10,800 "
                    "receivable merely because the contract runs 36 months. Specify "
                    "the counterfactual baseline, volume adjustments, termination "
                    "rights, and disputed-month treatment before starting. Keep "
                    "proposed benefits, earned fees, invoiced balances, and bank "
                    "receipts in separate fields so commercial forecasts cannot "
                    "quietly become accounting entries during a busy weekly close."
                ),
                (
                    "Treat section_179d_municipal_deduction_allocation_arbitrage as "
                    "TRACK_1 coordination of an eligible owner, qualifying designer, "
                    "and independent energy certifier. It is not the resale of a "
                    "freely transferable deduction. Establish building ownership, "
                    "designer responsibility, applicable construction and placed-in-service "
                    "dates, energy-model support, allocation documentation, and the "
                    "rules governing the particular project year. Section 179D "
                    "includes a termination rule for property whose construction "
                    "begins after June 30, 2026; a current calendar date alone "
                    "does not establish project eligibility. Illustratively, a "
                    "$100,000 allowable deduction at a 24% marginal rate represents "
                    "$24,000 of potential taxpayer benefit, while a separately "
                    "agreed $6,000 documentation engagement produces only $6,000 "
                    "of operator fees. Neither figure establishes the deduction "
                    "without project-specific substantiation. Apply Treasury Circular "
                    "230 Section 10.27 to the actual practitioner service and "
                    "proceeding, accounting for applicable judicial limits rather "
                    "than assuming all tax-related contingency arrangements are "
                    "permitted or prohibited. If eligibility, allocation authority, "
                    "or compensation treatment remains disputed, pause allocation, "
                    "obtain independent tax review, and offer fixed-fee documentation "
                    "support only for eligible projects. Do not substitute a "
                    "marketing success fee for that unresolved analysis."
                ),
            ],
            "table": {
                "caption": (
                    "Twelve Mapped Operator Plays — Illustrative Units, Evidence, "
                    "and Specific Risk Fallbacks"
                ),
                "headers": [
                    "Mapped play and operating scope",
                    "Illustrative operator fee calculation",
                    "Evidence required before production work",
                    "Failure condition and practical fallback",
                ],
                "rows": [
                    [
                        "Parcel service-guarantee refunds through authorized FedEx or UPS channels",
                        "$20,000 accepted service refunds multiplied by 25% earns $5,000",
                        "Executed carrier contract, guarantee eligibility, tracking events, and invoice identifiers",
                        "Guarantee waiver defeats eligibility; redirect review toward documented billing errors",
                    ],
                    [
                        "Duplicate parcel-charge recovery across customer-authorized billing account histories",
                        "$8,000 duplicate charges recovered multiplied by 30% earns $2,400",
                        "Matching shipment identifiers, duplicate invoice lines, and original payment records",
                        "Legitimate rebilling explains duplicates; close claim without charging recovery fees",
                    ],
                    [
                        "Dimensional-weight and accessorial correction using verified shipment measurement evidence",
                        "$12,000 accepted adjustments multiplied by 25% earns $3,000 operator fees",
                        "Package measurements, applicable dimensional divisor, carrier adjustments, and service contract",
                        "Missing contemporaneous measurements blocks recovery; implement prospective measurement capture instead",
                    ],
                    [
                        "Commercial utility tariff reclassification with normalized monthly savings measurement",
                        "$1,000 verified monthly savings multiplied by 30% earns $300 monthly",
                        "Applicable tariff, interval usage, demand peaks, and approved classification change",
                        "Usage shifts distort baseline; recalculate counterfactual before recognizing monthly fees",
                    ],
                    [
                        "Cooling-tower sewer abatement supported by separately measured evaporative water consumption",
                        "$24,000 approved sewer credits multiplied by 25% earns $6,000",
                        "Municipal abatement rule, approved submeter, inspection records, and consumption reconciliation",
                        "Unapproved meter prevents retrospective credits; pursue approved prospective measurement only",
                    ],
                    [
                        "Utility sales-tax exemption recovery for demonstrably eligible customer usage categories",
                        "$16,000 recoverable tax credits multiplied by 25% earns $4,000",
                        "State exemption authority, usage study, valid certificates, and covered invoice periods",
                        "Exemption classification remains contested; obtain specialist review before refund submission",
                    ],
                    [
                        "Waste-service contract true-ups for unsupported lifts, surcharges, or rate changes",
                        "$10,000 vendor credits multiplied by 30% earns $3,000 operator fees",
                        "Signed waste agreement, lift logs, service changes, and surcharge calculations",
                        "Contract authorizes charges; close historical claim and negotiate prospective pricing",
                    ],
                    [
                        "Telecom inventory disconnects with verified savings across the shared-savings term",
                        "$2,000 verified monthly savings multiplied by 25% earns $500 monthly",
                        "Circuit ownership, utilization evidence, termination terms, and customer disconnect authorization",
                        "Critical circuit or termination penalty defeats savings; retain service pending redesign",
                    ],
                    [
                        "Property-tax assessment appeals through properly authorized jurisdiction-qualified representation",
                        "$40,000 realized tax reduction multiplied by permitted 25% earns $10,000",
                        "Assessment notice, valuation support, appeal deadline, and required representative credentials",
                        "Licensing or deadline prevents representation; refer qualified counsel without unauthorized filing",
                    ],
                    [
                        "WOTC processing with Form 8850 and state workforce certification coordination",
                        "Twenty completed processing units at $150 each earns $3,000",
                        "Qualifying hire date, timely prescreening, certification packet, and employer wage records",
                        "Statutory hiring window or submission deadline fails; exclude affected worker processing",
                    ],
                    [
                        "Specialty tax-credit documentation under separately reviewed fixed-fee service engagements",
                        "Four accepted documentation packages at $1,500 each earns $6,000",
                        "Credit-specific eligibility analysis, underlying expenditures, responsible preparer, and substantiation file",
                        "Unsupported expenditure or service restriction blocks work; narrow scope before invoicing",
                    ],
                    [
                        (
                            "section_179d_municipal_deduction_allocation_arbitrage — "
                            "TRACK_1 eligible allocation coordination and documentation"
                        ),
                        (
                            "$100,000 deduction times 24% suggests $24,000 taxpayer "
                            "benefit; documentation fee equals $6,000"
                        ),
                        (
                            "Eligible owner, qualifying designer, independent certification, "
                            "construction timing, and allocation instrument"
                        ),
                        (
                            "Pause allocation, obtain independent tax review, and offer "
                            "fixed-fee documentation support only for eligible projects"
                        ),
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four verifications before a recoverable finding leaves the workspace",
                "body": (
                    "The founder owns the engagement decision; the evidence reviewer "
                    "records the result and supporting document digest."
                ),
                "items": [
                    (
                        "Verify signed authorization covers the exact account, entity, "
                        "period, interface, and representative action being proposed."
                    ),
                    (
                        "Verify the frozen contract and baseline establish claim "
                        "eligibility, including carrier guarantee waivers and tariff dates."
                    ),
                    (
                        "Verify deadlines, applicable tax-service compensation treatment, "
                        "and any required property-tax representative credentials."
                    ),
                    (
                        "Verify the customer refund destination and separate operator "
                        "fee trigger; prohibit recovery principal from entering revenue."
                    ),
                ],
            },
        },
        {
            "heading": (
                "2. Install six executable reference modules around a "
                "transactional fee subledger"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Extract the six reference cells into the filenames shown, place "
                    "them together, and initialize with python runner.py recovery.db "
                    "init. Python 3.9 and SQLite are sufficient; the chapter module "
                    "itself imports no application dependencies. The reference is a "
                    "refund-fee subledger, not a complete general ledger or a tax "
                    "return engine. It deliberately excludes custodial funds, supplier "
                    "principal, recurring savings accruals, credit notes, and foreign "
                    "currency. Those require additional reviewed posting types rather "
                    "than improvised negative receipts. Store integer cents and "
                    "integer basis points, with explicit half-up fee rounding. "
                    "The natural claim key combines client, invoice item, and play; "
                    "make invoice_key granular enough to distinguish recoverable "
                    "line items while preventing the same line from being counted "
                    "twice under renamed campaigns. SHA-256 connects the database "
                    "to immutable evidence retained outside it. A hash proves "
                    "identity of bytes, not commercial validity, so a named "
                    "reviewer still validates every document. The scoring script "
                    "records facts without granting credentials. Run intake with "
                    "a JSON payload containing the documented parameters; missing "
                    "facts, altered replay payloads, or duplicate natural keys "
                    "fail instead of silently changing an existing claim."
                ),
                (
                    "Every mutating function obtains BEGIN IMMEDIATE before reading "
                    "mutable state, holds the SQLite writer reservation through "
                    "validation and posting, and commits the event with its business "
                    "effect. Unique event identifiers reject changed retries; a "
                    "matching replay returns without another posting. A partial "
                    "unique index allows one earnings entry per claim, and a "
                    "provider-qualified external reference prevents two local claims "
                    "from sharing one acknowledgement. Concurrent receipts serialize "
                    "before checking the open balance, so two workers cannot each "
                    "consume the same receivable. These properties remove "
                    "check-then-write races within this controlled database path. "
                    "Use one local database on durable storage, not a network "
                    "filesystem or independent copied databases. Set foreign keys "
                    "on every connection, retain FULL synchronous durability, and "
                    "restrict write access to the service identity. The reference "
                    "makes no network submissions: it records an acknowledgement "
                    "only after a documented external action. Where a provider "
                    "supports idempotency keys, reuse a stable claim identifier. "
                    "Where it does not, an ambiguous timeout requires a status "
                    "inquiry and human resolution, never an automatic resend. "
                    "A database transaction cannot make an unrelated carrier "
                    "system participate in an atomic commit."
                ),
                (
                    "The verification and escrow state machine starts at held, "
                    "advances through verified, submitted, settled, and invoiced, "
                    "and allows documented voiding before settlement. Here escrow "
                    "means an internal evidence hold, not possession of client "
                    "money. Submission requires a provider-qualified acknowledgement; "
                    "settlement requires documentary proof that the actual customer "
                    "recovery equals the reviewed amount. A partial award stops "
                    "the transition for controlled rework rather than overstating "
                    "fees. Invoicing records completed contractual performance and "
                    "an unconditional fee right, then debits fee receivables and "
                    "credits operator revenue atomically. Bank receipts debit cash "
                    "and credit those receivables using an account-qualified bank "
                    "transaction identifier. The minimal implementation allocates "
                    "one bank transaction to one claim; multi-invoice deposits "
                    "need a dedicated allocation model before use. Reconciliation "
                    "shows earned fees minus allocated receipts equals remaining "
                    "receivables for every claim and cohort. QA runs inside one "
                    "read transaction, avoiding inconsistent snapshots during "
                    "concurrent writes. Structural checks supplement, rather than "
                    "replace, independent bank and source-document matching. "
                    "Export monthly operator expenses into the accounting system "
                    "separately; do not infer owner profit from this revenue-only "
                    "subledger. These supplied modules are reference source, "
                    "not reported execution results."
                ),
            ],
            "table": {
                "caption": (
                    "Production Engineering / SQLite-or-Postgres Ledger & "
                    "Idempotent Workflow Reference Table — Six SQLite Modules"
                ),
                "headers": [
                    "Module filename and narrowly bounded responsibility",
                    "Copy-pasteable executable reference source",
                    "Concurrency control and operating boundary",
                ],
                "rows": [
                    [
                        "schema.sql — create constrained claims, evidence events, and paired ledger postings",
                        _SCHEMA_SQL,
                        (
                            "Natural keys, event keys, provider references, and one "
                            "earning per claim have database uniqueness enforcement."
                        ),
                    ],
                    [
                        "intake.py — validate identifiers, freeze scoring inputs, and insert one work packet",
                        _INTAKE_PY,
                        (
                            "Writer reservation precedes replay checks; changed "
                            "payloads and duplicate natural claims fail without mutation."
                        ),
                    ],
                    [
                        "workflow.py — transition evidence holds, recognize earned fees, and allocate receipts",
                        _WORKFLOW_PY,
                        (
                            "State change, evidence event, and posting commit together; "
                            "external submission remains outside the database boundary."
                        ),
                    ],
                    [
                        "reconciliation.sql — expose earned fees, collected cash, and remaining claim receivables",
                        _RECONCILIATION_SQL,
                        (
                            "Each paired posting contributes once; customer recovery "
                            "principal never enters operator revenue or fee cash."
                        ),
                    ],
                    [
                        "qa.py — verify structure, fee roll-forwards, states, and posting evidence alignment",
                        _QA_PY,
                        (
                            "One read snapshot prevents mixed-version checks; "
                            "independent bank matching remains an additional operating control."
                        ),
                    ],
                    [
                        "runner.py — initialize storage and expose explicit JSON-driven operational commands",
                        _RUNNER_PY,
                        (
                            "Local durable storage, controlled writers, bounded lock "
                            "waiting, and explicit errors define the supported deployment."
                        ),
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Extract and initialize the six reference files",
                    "action": (
                        "Copy each executable cell to its named file and run "
                        "python runner.py recovery.db init on local durable storage."
                    ),
                    "detail": (
                        "Use a disposable database first. Preserve evidence separately, "
                        "restrict database access, and include the SQLite backup API "
                        "in the deployment backup procedure."
                    ),
                },
                {
                    "step": 2,
                    "title": "Exercise intake and transition replay behavior",
                    "action": (
                        "Create one fully scored claim, replay the identical intake, "
                        "then attempt the same identifier with a changed amount."
                    ),
                    "detail": (
                        "The matching retry must create no new event; the changed "
                        "retry must fail. Concurrent verification attempts must "
                        "produce only one committed transition."
                    ),
                },
                {
                    "step": 3,
                    "title": "Prove settlement and receipt invariants",
                    "action": (
                        "Record documented submission and settlement, invoice once, "
                        "then test duplicate and competing bank allocations."
                    ),
                    "detail": (
                        "A settlement mismatch must stop; a duplicate receipt must "
                        "be harmless; competing receipts must never exceed the "
                        "remaining receivable."
                    ),
                },
                {
                    "step": 4,
                    "title": "Close the subledger against independent records",
                    "action": (
                        "Run python runner.py recovery.db qa and report, then "
                        "match every receipt to the bank statement."
                    ),
                    "detail": (
                        "Export earned fees, cash, and receivables into the main "
                        "books. Reconcile operating expenses separately and "
                        "investigate every unmatched bank credit."
                    ),
                },
            ],
        },
        {
            "heading": (
                "3. Operate the evidence queue, specialist handoffs, and "
                "exception recovery without inventing cash"
            ),
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run a daily queue by deadline exposure, expected collectible "
                    "fee, and remaining evidence effort. The founder owns customer "
                    "communication, engagement scope, and collection; three contractors "
                    "cover invoice analysis, domain verification, and bookkeeping "
                    "with narrowly separated access. Begin each morning with expiring "
                    "carrier claims, unresolved acknowledgements, municipal inquiries, "
                    "and tax-processing deadlines. An OCR exception goes back to "
                    "the source invoice, not directly into a dispute letter. "
                    "Utility reviewers compare billed rate components to the "
                    "effective tariff and distinguish a retrospective credit from "
                    "a prospective classification change. Parcel reviewers establish "
                    "that service commitments applied to that shipment before "
                    "calculating lateness. The bookkeeper receives accepted amounts "
                    "and evidence references, not authority to revise eligibility. "
                    "Hold a weekly exception review with explicit owners and "
                    "next-contact dates. A municipal refund that takes another "
                    "60 days changes the collection forecast; it does not "
                    "justify recording a bank receipt. Similarly, a verbal "
                    "carrier concession stays out of settled status until the "
                    "credit memo or payment evidence arrives. This cadence "
                    "protects the small-team model by preventing contractors "
                    "from repeatedly rediscovering why the same unresolved "
                    "claim cannot yet move forward."
                ),
                (
                    "Separate tax-credit workflow from ordinary bill corrections at "
                    "the first intake screen. WOTC uses employer prescreening and "
                    "state workforce certification, including the statutory "
                    "28-day submission timing under Section 51(d)(13); confirm "
                    "the applicable eligible-hire window under Section 51(c)(4) "
                    "rather than assuming a later legislative extension. The "
                    "Form 8850 process must capture the applicant's timely "
                    "prescreening information, employer signatures, hiring dates, "
                    "and submission evidence. An ATS integration should create "
                    "a deadline task and secure document request, not fabricate "
                    "answers from demographic guesses. Where tax-return information "
                    "falls within Section 7216, apply its disclosure and use "
                    "restrictions and the applicable Treasury regulations before "
                    "sharing records with contractors or outside processors. "
                    "Property-tax matters receive a separate jurisdiction review; "
                    "Texas Occupations Code Chapter 1152, for example, governs "
                    "property-tax consultants within its scope and exemptions. "
                    "Independent qualified specialists own technical conclusions "
                    "outside the founder's competence. Compensation follows the "
                    "actual service and applicable rules, not the general "
                    "25%–50% commercial audit pitch. The fixed processing and "
                    "documentation examples in the matrix therefore remain "
                    "outside the refund-only reference ledger until their "
                    "performance obligations and posting rules are explicitly implemented."
                ),
                (
                    "Use exception handling to preserve economics instead of "
                    "concealing losses. A disputed baseline creates a measurement "
                    "task; an expired deadline creates a closed loss; an "
                    "unconfirmed provider response creates an inquiry, not another "
                    "submission. For partial settlements, retain the original "
                    "claim and evidence trail, approve a revised work packet "
                    "under a controlled amendment procedure, and prevent the "
                    "same provider acknowledgement from supporting duplicate "
                    "revenue. The compact reference intentionally refuses this "
                    "amendment path until an extended model is reviewed. "
                    "Likewise, reversals, customer refunds, chargebacks, and "
                    "split bank deposits belong in explicit extension tests "
                    "before live use. Archive raw evidence with restricted "
                    "access, encrypted storage, retention dates, and documented "
                    "deletion authority; the SQLite database stores digests "
                    "and review metadata rather than payroll documents. "
                    "Restore a backup into an isolated environment and "
                    "compare claim counts, event counts, fee totals, and "
                    "bank allocations before declaring recovery successful. "
                    "For shared savings, recalculate each month using "
                    "agreed production or occupancy normalizers and retain "
                    "the baseline version used. A 36-month contract is "
                    "a measurement commitment, not permission to recognize "
                    "three years of estimated fees on signing day."
                ),
            ],
            "table": {
                "caption": (
                    "Production Exception Matrix — Named Owner, Release Evidence, "
                    "and Recovery Action"
                ),
                "headers": [
                    "Exception detected in the operating queue",
                    "Accountable owner and evidence required",
                    "Concrete release or closure criterion",
                    "Specific fallback preserving money and auditability",
                ],
                "rows": [
                    [
                        "Carrier contract contains a service-guarantee waiver affecting proposed shipment claims",
                        "Parcel analyst retrieves signed contract schedule and effective service terms",
                        "Eligibility reviewer confirms a recoverable billing error independent of waived guarantee",
                        "Close waived service claims and inspect duplicate charges or supported measurement errors",
                    ],
                    [
                        "Utility credit amount differs from the originally verified recovery expectation",
                        "Utility reviewer obtains credit memorandum and line-level explanation from the supplier",
                        "Reviewed amendment reconciles approved recovery before any revised fee is recognized",
                        "Keep compact ledger transition blocked until controlled amendment support is implemented",
                    ],
                    [
                        "Provider submission times out without a reliable acknowledgement or accepted case identifier",
                        "Founder checks provider case history using the original customer and claim identifiers",
                        "Documented provider response establishes whether the original submission already exists",
                        "Do not resend automatically when provider idempotency support cannot resolve ambiguity",
                    ],
                    [
                        "WOTC packet lacks timely prescreening or state workforce submission evidence",
                        "Tax-processing specialist checks Form 8850 dates and retained delivery confirmation",
                        "Applicable statutory eligibility and timing requirements are supported by contemporaneous records",
                        "Exclude the affected worker rather than reconstructing signatures or backdating records",
                    ],
                    [
                        "Section 179D project lacks qualifying allocation authority or independent energy certification",
                        "Independent tax reviewer checks owner eligibility, designer role, dates, and certification",
                        "Eligible project documentation supports the allocation and permitted service compensation structure",
                        "Pause allocation and offer fixed-fee documentation support only for eligible projects",
                    ],
                    [
                        "Bank deposit combines multiple fee invoices beyond the reference allocation model",
                        "Bookkeeper obtains remittance detail identifying every invoice and paid amount",
                        "Reviewed deposit-allocation extension preserves one immutable bank transaction with multiple allocations",
                        "Hold deposit in the main-book suspense process without fabricating separate bank transactions",
                    ],
                    [
                        "Backup restoration produces different event counts or unmatched operator bank receipts",
                        "Bookkeeper and technical contractor compare snapshot totals with independent statement records",
                        "Restored ledger passes structural checks and source-to-bank reconciliation for the affected period",
                        "Keep production writes suspended while restoring the last verified consistent backup",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that prevent expensive rework",
                "body": (
                    "Experienced operators spend review minutes on claim eligibility "
                    "and collection evidence before spending hours on presentation."
                ),
                "items": [
                    (
                        "Ask for the carrier pricing addendum with the first invoice "
                        "export; guarantee waivers often hide outside the shipment data."
                    ),
                    (
                        "Photograph cooling-tower submeter identifiers and retain the "
                        "municipality's acceptance record before projecting sewer credits."
                    ),
                    (
                        "Save provider acknowledgement identifiers immediately and "
                        "qualify them with provider and account context before ledger entry."
                    ),
                    (
                        "Send fee invoices with the exact supplier credit memo and "
                        "contract calculation; this shortens customer approval disputes."
                    ),
                ],
            },
        },
        {
            "heading": (
                "4. Walk a ninety-day cohort from lead scrubs to "
                "Base-case earned profit and closing cash"
            ),
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a deliberately explicit steady-production quarter rather "
                    "than portraying a cold start as instant cash. The modeled "
                    "operator begins with authorized prospect relationships, ready "
                    "invoice access, $24,000 opening liquidity, and no opening "
                    "fee receivables. This fits within the $6,000–$35,000 startup "
                    "capital range but does not eliminate the stated one-to-four-month "
                    "first-deal interval for a new entrant. Each month supplies "
                    "40 qualified leads, ten signed work packets, two eligibility "
                    "scrubs, and eight retained cases. Across 90 days, 120 "
                    "leads produce 30 signed packets, six closed losses, and "
                    "24 collectible cases. Cohort A earns $60,000, cohort B "
                    "earns $41,250, and cohort C earns $25,000; these are "
                    "different verified recovery sizes, not equal-value deals. "
                    "All use a permitted 25% commercial refund fee, requiring "
                    "$240,000, $165,000, and $100,000 of actual customer "
                    "recoveries respectively. The resulting $505,000 customer "
                    "recovery total is coincidentally equal to annual Base "
                    "operator revenue, but the two measures have different "
                    "periods and meanings. Quarter operator revenue is only "
                    "$126,250. Scrubbed packets earn zero and their review "
                    "effort remains inside the modeled delivery expense."
                ),
                (
                    "Month 1 recognizes $30,000 from cohort A and collects "
                    "$20,000, leaving $10,000 receivable. Month 2 recognizes "
                    "another $20,000 from A and $22,500 from B, while "
                    "collecting $25,000 from A and $15,000 from B. "
                    "Month 3 recognizes A's remaining $10,000, B's "
                    "remaining $18,750, and C's $25,000; receipts are "
                    "$15,000, $21,250, and $20,000 respectively. Thus "
                    "quarter earnings total $126,250, cash receipts total "
                    "$116,250, and closing receivables total $10,000, "
                    "split evenly between B and C. Customer recovery "
                    "evidence supports each recognition event, and the "
                    "contract makes the fee unconditional at completed "
                    "performance; a signature alone never earns revenue. "
                    "The cash pattern assumes reasonably prompt commercial "
                    "refund processing, not municipal or tax-refund timing. "
                    "Slower utility credits move their affected cases "
                    "into later periods instead of borrowing cash from "
                    "another cohort in the presentation. The two scrubs "
                    "per cohort consist of one contract or eligibility "
                    "failure and one evidence or deadline failure. Their "
                    "losses reduce signed-to-retained conversion to 80%, "
                    "with no invented fee receivable to write off afterward."
                ),
                (
                    "Monthly operating expense is $23,987.50, comprising $6,500 "
                    "of recurring overhead and $17,487.50 of delivery, contractor, "
                    "and variable operating costs. Recurring overhead stays "
                    "within the supplied $1,500–$9,500 monthly opex range; "
                    "the additional direct costs reconcile the full scorecard "
                    "expense envelope rather than pretending the overhead "
                    "range covers every expense. Quarter costs are "
                    "$71,962.50 and earned owner profit is $54,287.50, "
                    "exactly 43% of revenue. Cash operating flow is "
                    "negative $3,987.50 in Month 1, positive $16,012.50 "
                    "in Month 2, and positive $32,262.50 in Month 3. "
                    "Cumulative flow therefore reaches $44,287.50, with "
                    "$68,287.50 closing cash after opening liquidity. "
                    "The $10,000 difference between earned profit and "
                    "cash flow is closing receivables. No owner distributions, "
                    "capital purchases, borrowing, or personal taxes enter "
                    "this operating illustration. Four equivalent quarters "
                    "produce $505,000 revenue, $287,850 expenses, and "
                    "$217,150 annual owner profit with one full-time "
                    "operator and three contractors. Annual cash requires "
                    "its own receivable roll-forward; do not multiply "
                    "the first quarter's collection lag mechanically. "
                    "Conservative and Scaled economics remain separate "
                    "canonical cases, not extrapolations from optimistic "
                    "recovery principal or unsigned savings estimates."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort, period, or reconciliation control",
                    "Lead conversion, scrubs, and earned operator fees",
                    "Fee collection timing and closing receivables",
                    "Operating expense, profit, and cumulative cash",
                ],
                "rows": [
                    [
                        "Cohort A originates during Month 1 and completes recognition during Month 3",
                        (
                            "Forty leads yield ten signed packets; two scrubbed, "
                            "eight retained; $60,000 earned on $240,000 customer recoveries"
                        ),
                        (
                            "Collect $20,000 in Month 1, $25,000 in Month 2, "
                            "$15,000 in Month 3; closing receivables equal zero"
                        ),
                        (
                            "Recognition is $30,000, $20,000, then $10,000; "
                            "delivery costs remain in the monthly expense pool"
                        ),
                    ],
                    [
                        "Cohort B originates during Month 2 and completes recognition during Month 3",
                        (
                            "Forty leads yield ten signed packets; two scrubbed, "
                            "eight retained; $41,250 earned on $165,000 customer recoveries"
                        ),
                        (
                            "Collect $15,000 in Month 2 and $21,250 in "
                            "Month 3; closing receivables equal $5,000"
                        ),
                        (
                            "Recognition is $22,500 then $18,750; no additional "
                            "revenue is created when remaining receivables collect"
                        ),
                    ],
                    [
                        "Cohort C originates during Month 3 and earns its modeled fees that month",
                        (
                            "Forty leads yield ten signed packets; two scrubbed, "
                            "eight retained; $25,000 earned on $100,000 customer recoveries"
                        ),
                        (
                            "Collect $20,000 during Month 3; remaining $5,000 "
                            "is a supported closing fee receivable"
                        ),
                        (
                            "All $25,000 is earned during Month 3; timing "
                            "assumes ready evidence and prompt commercial refunds"
                        ),
                    ],
                    [
                        "Month 1 consolidated close starts with $24,000 opening liquidity",
                        (
                            "Forty leads, ten signed packets, two scrubs, eight "
                            "retained cases; recognized operator revenue equals $30,000"
                        ),
                        (
                            "Operator receipts equal $20,000; cumulative earned fees "
                            "less receipts leave $10,000 closing receivables"
                        ),
                        (
                            "Expenses $23,987.50; profit $6,012.50; monthly and "
                            "cumulative flow negative $3,987.50; closing cash $20,012.50"
                        ),
                    ],
                    [
                        "Month 2 consolidated close combines new work with earlier cohort collections",
                        (
                            "Forty new leads, ten signed packets, two scrubs; "
                            "A and B recognition totals $42,500"
                        ),
                        (
                            "Operator receipts equal $40,000; cumulative earned fees "
                            "less receipts leave $12,500 closing receivables"
                        ),
                        (
                            "Expenses $23,987.50; profit $18,512.50; monthly flow "
                            "$16,012.50; cumulative flow $12,025; closing cash $36,025"
                        ),
                    ],
                    [
                        "Month 3 consolidated close finishes the illustrated ninety-day recognition cycle",
                        (
                            "Forty new leads, ten signed packets, two scrubs; "
                            "A, B, and C recognition totals $53,750"
                        ),
                        (
                            "Operator receipts equal $56,250; cumulative earned fees "
                            "less receipts leave $10,000 closing receivables"
                        ),
                        (
                            "Expenses $23,987.50; profit $29,762.50; monthly flow "
                            "$32,262.50; cumulative flow $44,287.50; closing cash $68,287.50"
                        ),
                    ],
                    [
                        "Quarter control and annual Base run-rate reconciliation preserve period distinctions",
                        (
                            "120 leads, 30 signed, six scrubbed, 24 retained; "
                            "$126,250 quarter fees times four equals $505,000 annually"
                        ),
                        (
                            "$116,250 quarter receipts plus $10,000 closing "
                            "receivables equals $126,250 earned operator revenue"
                        ),
                        (
                            "$71,962.50 quarter expenses and $54,287.50 profit "
                            "annualize to $287,850 expenses and $217,150 profit"
                        ),
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "A recovery is real when the evidence proves the customer benefit, "
        "the contract earns the fee, and the bank closes the loop."
    ),
    "diagram_id": "diag-01",
    "action_checklist": [
        (
            "Secure account-specific Letters of Authorization and immutable "
            "baseline snapshots before disclosing proposed recoveries."
        ),
        (
            "Map each work packet to one of the twelve operating lanes, "
            "document its fee trigger, and close ineligible packets explicitly."
        ),
        (
            "Extract the six reference modules, initialize a disposable SQLite "
            "database, and test replay, duplicate, concurrency, and overpayment cases."
        ),
        (
            "Require provider acknowledgements, verified customer settlement "
            "evidence, and completed performance before recognizing refund fees."
        ),
        (
            "Route WOTC timing, Section 179D allocations, practitioner fee "
            "restrictions, and property-tax credentials to qualified reviewers."
        ),
        (
            "Reconcile $126,250 quarter earnings to $116,250 receipts and "
            "$10,000 receivables, then match expenses and bank cash independently."
        ),
    ],
    "statutory_citations": [
        {
            "title": (
                "31 CFR Section 10.27 — Treasury Circular 230 fee provisions"
            ),
            "url": (
                "https://www.ecfr.gov/current/title-31/subtitle-A/part-10/"
                "subpart-B/section-10.27"
            ),
            "relevance": (
                "Evaluate contingent compensation against the actual practitioner "
                "service, proceeding, regulatory exceptions, and applicable judicial "
                "limits before agreeing to tax-related fee terms."
            ),
        },
        {
            "title": (
                "26 U.S.C. Section 179D — Energy efficient commercial buildings deduction"
            ),
            "url": "https://www.law.cornell.edu/uscode/text/26/179D",
            "relevance": (
                "Establish eligible building and owner facts, designer allocation "
                "authority, certification requirements, applicable benefit rules, "
                "and the construction-beginning termination provision."
            ),
        },
        {
            "title": (
                "26 U.S.C. Section 51 — Work opportunity credit"
            ),
            "url": "https://www.law.cornell.edu/uscode/text/26/51",
            "relevance": (
                "Apply Section 51(d)(13) certification and prescreening requirements, "
                "including the 28-day submission rule, and verify the eligible-hire "
                "window under Section 51(c)(4)."
            ),
        },
        {
            "title": (
                "26 U.S.C. Section 7216 — Disclosure or use of information by "
                "preparers of returns"
            ),
            "url": "https://www.law.cornell.edu/uscode/text/26/7216",
            "relevance": (
                "Identify restrictions and applicable exceptions before a covered "
                "preparer discloses or uses tax-return information in contractor "
                "handoffs or processing integrations."
            ),
        },
        {
            "title": (
                "26 CFR Section 301.7216-2 — Permissible disclosures or uses "
                "without taxpayer consent"
            ),
            "url": (
                "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-F/"
                "part-301/section-301.7216-2"
            ),
            "relevance": (
                "Evaluate the precise regulatory exception and its conditions "
                "rather than assuming every operational disclosure is permitted."
            ),
        },
        {
            "title": (
                "Texas Occupations Code Chapter 1152 — Property Tax Consultants"
            ),
            "url": "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1152.htm",
            "relevance": (
                "Check registration requirements, scope, and exemptions before "
                "undertaking covered Texas property-tax consulting services."
            ),
        },
    ],
}
