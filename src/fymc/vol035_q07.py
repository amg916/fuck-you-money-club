from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "complete-operating-process-production-blueprint-90-day-cohort-walk",
    "question_prompt": "How does an operator execute subject-to & wraparound note arbitrage end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "County-Roll Intake, RMLO Underwriting, Due-on-Sale Exposure, Licensed Servicing, and an Atomic SQLite Cash Ledger",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #35, Subject-To & Wraparound Note Arbitrage, ranks #09 of 36 "
        "with a 90/100 Money-to-Manpower Score. This chapter connects 11 mapped "
        "plays through one evidence-driven operating process: source low-rate debt, "
        "verify title and payment obligations, originate through an RMLO, close "
        "through escrow, and reconcile retained spreads through licensed servicing. "
        "Six copy-pasteable engineering modules establish atomic transitions, "
        "duplicate-resistant posting, and independent bank controls. A worked "
        "90-day cohort produces $44,750 operating cash contribution and bridges "
        "explicitly to the $190,000 Base annual owner profit. Conservative and "
        "Scaled annual owner profits remain $28,000 and $442,000. Property-tax "
        "appeals supply a separate, documented intervention rather than an "
        "invented addition to the canonical revenue model."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual retained upfront spreads and wrap interest contribution",
            "note": "28% margin; $28,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$475,000",
            "context": "Annual retained upfront spreads and wrap interest contribution",
            "note": "40.0% margin; $190,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$850,000",
            "context": "Annual retained upfront spreads and wrap interest contribution",
            "note": "52% margin; $442,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Convert eleven operating plays into a verified acquisition queue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat intake as evidence collection, not permission to acquire a property. "
                    "The eleven mapped operating plays used here are debt-trigger sourcing, "
                    "county-roll ingestion, comparable-equity screening, property-tax appeal "
                    "execution, seller authorization, title and lien verification, underlying-loan "
                    "verification, RMLO buyer underwriting, escrow closing, licensed-servicer "
                    "boarding, and cash reconciliation. These are chapter-local workflow labels; "
                    "the supplied catalog identifier is property_tax_assessment_appeal_contingency. "
                    "Keep its TRACK_1 work order separate from the note acquisition order. "
                    "Pull authorized county assessor exports when annual notices appear, then "
                    "attach parcel identifiers, notice dates, protest deadlines, assessed values, "
                    "homestead status, and comparable sales. Record the source URL and retrieval "
                    "timestamp before scoring anything. A low mortgage coupon is attractive only "
                    "after the unpaid balance, arrears, escrow shortage, maturity, and transfer "
                    "terms survive verification. Seller permission to obtain statements does "
                    "not transfer the loan or release the seller from liability. Assign every "
                    "lead a stable source key and every subsequent decision an immutable event "
                    "key. The owner handles exceptions; contractors collect documents, underwrite "
                    "buyers, and service loans within their actual authority. Reject unsupported "
                    "balances rather than converting estimates into acquisition economics or "
                    "marketing claims about immediate available equity."
                ),
                (
                    "Use the assessment appeal as a measured intervention, not a reason to "
                    "buy a defective title. An automated valuation model should compare "
                    "assessment-to-supported-market-value ratios within defensible property "
                    "classes, neighborhoods, size bands, and condition groups. A parcel assessed "
                    "at $300,000 against supported value of $250,000 has a 1.20 ratio; "
                    "neighbors near 1.00 justify investigation, not an automatic reduction. "
                    "If an accepted assessment change reduces the actual first-year tax bill "
                    "from $12,000 to $7,200, the verified saving is $4,800. A 40% "
                    "contingency produces $1,920, within the specified 30–50% range. Calculate "
                    "the saving from the issued bill or refund after applicable exemptions "
                    "and rates, not merely from the valuation difference. In Texas, calendar "
                    "Tax Code §41.44 deadlines and evaluate unequal-appraisal evidence under "
                    "§41.43 with the authorized representative. Partner with licensed local "
                    "property-tax consultants or attorneys of record wherever required; "
                    "automate pre-deadline batch electronic filing only through permitted "
                    "county channels. Capture submission receipts, parcel-level exceptions, "
                    "and engagement authority. If the AVM fails validation, route to manual "
                    "comparables or withdraw before incurring representation costs. The worked "
                    "cohort excludes appeal fees entirely, preventing speculative savings from "
                    "inflating the Base case."
                ),
                (
                    "Price the acquisition around verified obligations and a funded failure "
                    "path. Obtain the note, deed of trust or mortgage, current statement, "
                    "payment history, reinstatement quote where relevant, tax certificate, "
                    "insurance declarations, and title commitment through authorized channels. "
                    "A subject-to conveyance generally leaves the existing borrower obligated; "
                    "a wrap adds another obligation rather than substituting the buyer for "
                    "that borrower. Under 12 U.S.C. §1701j-3, lenders generally may enforce "
                    "contractual due-on-sale clauses, subject to enumerated exceptions. An "
                    "ordinary investor transfer does not become protected merely because "
                    "a trust or servicing arrangement appears in the documents. Record the "
                    "acceleration exposure and a priced refinance, payoff, consensual unwind, "
                    "or sale strategy before committing capital. For illustration, a $1,500 "
                    "monthly underlying payment plus $500 of taxes and insurance creates "
                    "$2,000 monthly carrying exposure; a three-month interruption needs "
                    "$6,000 before collection, repair, or foreclosure costs. Do not label "
                    "that liquidity reserve an expense when it is merely transferred between "
                    "operator accounts. A written investment policy should reject transactions "
                    "whose acceleration or buyer-default exposure exceeds available capital. "
                    "The stated $12,000–$65,000 startup range is a planning envelope, not "
                    "proof that every candidate property fits it."
                ),
            ],
            "table": {
                "caption": "Eleven-Play Intake and Acquisition Evidence Matrix",
                "headers": [
                    "Operating play and accountable workstream",
                    "Required evidence before advancing the file",
                    "Unit economics or measurable production rule",
                    "Failure response and preserved audit artifact",
                ],
                "rows": [
                    [
                        "Debt-trigger sourcing plus authorized county-roll ingestion",
                        "Dated assessor export, parcel key, and seller contact authority",
                        "Score arrears and coupon separately from verified acquisition profitability",
                        "Quarantine stale records and retain original retrieval evidence",
                    ],
                    [
                        "Comparable-equity screening using a versioned valuation model",
                        "Comparable sales, property classes, condition adjustments, and ratio outputs",
                        "Investigate 1.20 subject ratio against supported 1.00 neighborhood ratios",
                        "Replace unreliable automation with documented manual comparable analysis",
                    ],
                    [
                        "property_tax_assessment_appeal_contingency — TRACK_1 administrative appeal execution",
                        "Signed engagement, authorized representative, statutory deadline, and filing receipt",
                        "$4,800 verified first-year reduction multiplied by 40% produces $1,920",
                        "Use qualified local representatives and batch filing before deadlines",
                    ],
                    [
                        "Seller authorization plus title and lien verification",
                        "Executed permissions, title commitment, judgment search, and lien payoff statements",
                        "Reject purchase economics until all senior claims receive explicit treatment",
                        "Stop acquisition when title defects exceed documented cure capacity",
                    ],
                    [
                        "Underlying-loan verification plus RMLO buyer qualification workstreams",
                        "Current servicing history, loan terms, income records, and underwriting decision",
                        "$2,000 monthly property exposure requires $6,000 for three interruption months",
                        "Decline unaffordable buyers and acquisitions lacking funded acceleration responses",
                    ],
                    [
                        "Escrow closing plus licensed third-party servicer boarding",
                        "Recorded instruments, required notices, funded escrow, and accepted boarding package",
                        "Release instructions only after documentary conditions and funding independently match",
                        "Hold disbursement when account ownership or payment routing conflicts",
                    ],
                    [
                        "Cash reconciliation closes the complete operating evidence chain",
                        "Settled bank export, servicer statement, and underlying payment confirmation",
                        "Recognize retained operator contribution rather than property value or principal",
                        "Freeze further distributions until discrepancies receive documented resolution",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the spread before optimizing acquisition volume",
                "body": (
                    "Experienced operators reduce information asymmetry and cash-control failures "
                    "before spending more on leads."
                ),
                "items": [
                    "Request escrow analyses alongside mortgage statements; an apparent coupon advantage can disappear when a shortage increases required monthly payments.",
                    "Make the licensed servicer prove underlying-payment delivery with lender-side evidence, not merely a debit from its own collection account.",
                    "Preserve the assessor notice envelope or electronic delivery record because a notice date can control the practical protest calendar.",
                    "Use separate engagement and billing records for assessment appeals so contingent tax fees never become hidden additions to wrap yield.",
                ],
            },
        },
        {
            "heading": "2. Install six atomic production modules before moving money",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The reference implementation below is a deliberately bounded SQLite "
                    "operator-contribution ledger, not a substitute for a licensed servicer's "
                    "borrower, trust, escrow, or amortization system. Copy its six cells into "
                    "the named files in one project directory. Initialize with sqlite3 "
                    "ledger.sqlite < schema.sql, then install the reporting views with "
                    "sqlite3 ledger.sqlite < reports.sql. Feed each Python command one JSON "
                    "object on standard input. Use integer cents, stable business identifiers, "
                    "and source-issued settlement references. Intake scoring prioritizes "
                    "review; it never constitutes credit approval. The workflow records "
                    "independently verified evidence, while cash posting accepts only earned, "
                    "settled operator amounts. Gross borrower receipts, refundable deposits, "
                    "escrow balances, and principal belong in the servicing system and are "
                    "excluded here. A separate general ledger must handle accruals, deferred "
                    "amounts, depreciation, entity taxes, and other entries outside this "
                    "restricted cash-contribution model. Financial reporting should classify "
                    "interest under applicable lending guidance and assess principal-versus-agent "
                    "presentation for relevant service revenue under ASC 606; neither permits "
                    "calling house value revenue. Back up the database using SQLite's backup "
                    "API and retain immutable source exports in encrypted storage with "
                    "access limited to the assigned transaction team."
                ),
                (
                    "Concurrency is controlled inside the stated boundary: every application "
                    "write opens BEGIN IMMEDIATE on the same local database, validates "
                    "the current record, and commits one complete transaction. UNIQUE "
                    "constraints protect source keys, event keys, and settlement references. "
                    "Canonical payload comparison distinguishes a safe retry from a "
                    "conflicting reuse of an identifier. A repeated request either returns "
                    "its previous outcome or fails explicitly; it cannot silently post twice. "
                    "Workflow updates additionally compare the expected state and require "
                    "exactly one affected row. Journal rows express balanced double-entry "
                    "amounts in a single immutable record, eliminating an intermediate "
                    "half-posted journal. WAL mode supports readers while SQLite serializes "
                    "writers. Keep the database on a supported local filesystem, not a "
                    "shared network mount. Multiple application hosts require a properly "
                    "implemented transactional database service rather than copied database "
                    "files. These controls remove application-level check-then-write races "
                    "for cooperating local writers; they do not make external banking or "
                    "servicer APIs exactly-once. No module sends payments. Import independently "
                    "confirmed settlements after external execution, preserving the provider's "
                    "reference. A future payment integration needs provider idempotency, an "
                    "outbox, and explicit recovery after uncertain responses before it can "
                    "safely automate disbursement."
                ),
                (
                    "Operate the scripts behind an authenticated work queue rather than "
                    "exposing raw JSON submission to sellers or buyers. Boolean verification "
                    "fields represent an authorized reviewer's recorded conclusions, not "
                    "self-certifying customer claims. Attach the reviewed evidence bundle "
                    "identifier to every transition and retain its hash and reviewer identity "
                    "in the surrounding document system. The reserve transition records "
                    "settled escrow evidence; it does not create or verify a bank transfer "
                    "by itself. Before production, restrict database writes to this service "
                    "account and test replay, collision, illegal transition, missing bank "
                    "control, and interrupted-transaction cases. The independent bank control "
                    "must come from an accountant's normalized statement export, never from "
                    "the ledger totals it is supposed to test. Normalization removes transfers "
                    "and segregated servicing flows while preserving a bridge back to the "
                    "complete statement. Each month, also reconcile servicer collections, "
                    "underlying principal and interest, tax disbursements, insurance payments, "
                    "and suspense balances outside this narrow ledger. The supplied QA "
                    "command checks structural integrity and operator cash differences; "
                    "it cannot establish borrower affordability or prove that a lender "
                    "accepted a payment. Require those independent checks before labeling "
                    "the monthly package complete."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and executable project file",
                    "Copy-pasteable implementation for the bounded local ledger",
                    "Production invariant and operating responsibility",
                    "Failure behavior and verification evidence",
                ],
                "rows": [
                    [
                        "Module 1 — save the database definition as schema.sql",
                        """PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;
PRAGMA busy_timeout=10000;

CREATE TABLE IF NOT EXISTS case_file (
    id INTEGER PRIMARY KEY,
    case_key TEXT NOT NULL UNIQUE,
    source_key TEXT NOT NULL UNIQUE,
    intake_payload TEXT NOT NULL,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    reserve_required_cents INTEGER NOT NULL CHECK(reserve_required_cents > 0),
    state TEXT NOT NULL CHECK(
        state IN ('SCORED', 'VERIFIED', 'ESCROW', 'READY', 'CLOSED')
    )
);

CREATE TABLE IF NOT EXISTS workflow_event (
    id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    case_id INTEGER NOT NULL REFERENCES case_file(id),
    payload TEXT NOT NULL,
    resulting_state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    settlement_ref TEXT NOT NULL UNIQUE,
    case_id INTEGER REFERENCES case_file(id),
    period TEXT NOT NULL CHECK(
        length(period) = 7
        AND period GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]'
        AND substr(period, 6, 2) BETWEEN '01' AND '12'
    ),
    kind TEXT NOT NULL CHECK(kind IN ('upfront', 'interest', 'opex')),
    payload TEXT NOT NULL,
    cash_cents INTEGER NOT NULL,
    revenue_cents INTEGER NOT NULL,
    expense_cents INTEGER NOT NULL,
    CHECK(cash_cents = revenue_cents - expense_cents),
    CHECK(
        (kind IN ('upfront', 'interest')
         AND case_id IS NOT NULL
         AND revenue_cents > 0 AND expense_cents = 0)
        OR
        (kind = 'opex' AND case_id IS NULL
         AND revenue_cents = 0 AND expense_cents > 0)
    )
);

CREATE TABLE IF NOT EXISTS bank_control (
    period TEXT PRIMARY KEY CHECK(
        length(period) = 7
        AND period GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]'
        AND substr(period, 6, 2) BETWEEN '01' AND '12'
    ),
    net_cash_cents INTEGER NOT NULL,
    statement_ref TEXT NOT NULL UNIQUE,
    payload TEXT NOT NULL
);

CREATE TRIGGER IF NOT EXISTS journal_no_update
BEFORE UPDATE ON journal BEGIN
    SELECT RAISE(ABORT, 'Journal corrections require a separately designed adjustment process');
END;

CREATE TRIGGER IF NOT EXISTS journal_no_delete
BEFORE DELETE ON journal BEGIN
    SELECT RAISE(ABORT, 'Posted operator cash records are immutable');
END;

CREATE TRIGGER IF NOT EXISTS event_no_update
BEFORE UPDATE ON workflow_event BEGIN
    SELECT RAISE(ABORT, 'Workflow evidence records are immutable');
END;

CREATE TRIGGER IF NOT EXISTS event_no_delete
BEFORE DELETE ON workflow_event BEGIN
    SELECT RAISE(ABORT, 'Workflow evidence records must remain available');
END;

CREATE TRIGGER IF NOT EXISTS control_no_update
BEFORE UPDATE ON bank_control BEGIN
    SELECT RAISE(ABORT, 'Statement controls require a reviewed replacement procedure');
END;

CREATE TRIGGER IF NOT EXISTS control_no_delete
BEFORE DELETE ON bank_control BEGIN
    SELECT RAISE(ABORT, 'Independent statement controls must remain available');
END;
""",
                        "Unique business keys and balanced immutable rows constrain every accepted posting",
                        "Database constraints reject duplicate references and structurally inconsistent cash entries",
                    ],
                    [
                        "Module 2 — save the intake scorer as intake.py",
                        """from __future__ import annotations

import json
import sqlite3
import sys

data = json.load(sys.stdin)
required = (
    "case_key", "source_key", "coupon_bps",
    "arrears_cents", "reserve_required_cents"
)
if any(key not in data for key in required):
    raise ValueError("Provide every required intake field")
for key in ("case_key", "source_key"):
    if not isinstance(data[key], str) or not data[key].strip():
        raise ValueError("Business identifiers must contain text")
for key in ("coupon_bps", "arrears_cents", "reserve_required_cents"):
    if type(data[key]) is not int or data[key] < 0:
        raise ValueError("Rate and monetary inputs require nonnegative integers")
if data["reserve_required_cents"] <= 0:
    raise ValueError("Set a positive reviewed reserve requirement")

score = 30
score += 40 if data["coupon_bps"] <= 450 else 10
score += 20 if data["arrears_cents"] == 0 else 0
payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
db = sqlite3.connect("ledger.sqlite", timeout=10, isolation_level=None)
db.execute("PRAGMA foreign_keys=ON")
try:
    db.execute("BEGIN IMMEDIATE")
    prior = db.execute(
        "SELECT id, intake_payload FROM case_file WHERE case_key=?",
        (data["case_key"],)
    ).fetchone()
    if prior:
        if prior[1] != payload:
            raise ValueError("Case identifier reused with conflicting intake")
        result = prior[0]
    else:
        cursor = db.execute(
            "INSERT INTO case_file "
            "(case_key, source_key, intake_payload, score, "
            "reserve_required_cents, state) VALUES (?, ?, ?, ?, ?, 'SCORED')",
            (
                data["case_key"], data["source_key"], payload,
                score, data["reserve_required_cents"]
            )
        )
        result = cursor.lastrowid
    db.execute("COMMIT")
    print(json.dumps({"case_id": result, "review_priority_score": score}))
except Exception:
    if db.in_transaction:
        db.execute("ROLLBACK")
    raise
finally:
    db.close()
""",
                        "Stable source identifiers prevent repeated imports from creating duplicate acquisitions",
                        "Conflicting payloads fail explicitly instead of overwriting previously reviewed evidence",
                    ],
                    [
                        "Module 3 — save the verification state machine as workflow.py",
                        """from __future__ import annotations

import json
import sqlite3
import sys

data = json.load(sys.stdin)
for key in ("event_key", "case_key", "action", "evidence_ref"):
    if not isinstance(data.get(key), str) or not data[key].strip():
        raise ValueError("Supply event, case, action, and reviewed evidence references")
transitions = {
    "verify": ("SCORED", "VERIFIED"),
    "escrow": ("VERIFIED", "ESCROW"),
    "ready": ("ESCROW", "READY"),
    "close": ("READY", "CLOSED"),
}
if data["action"] not in transitions:
    raise ValueError("Select a supported forward workflow action")
payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
db = sqlite3.connect("ledger.sqlite", timeout=10, isolation_level=None)
db.execute("PRAGMA foreign_keys=ON")
try:
    db.execute("BEGIN IMMEDIATE")
    prior = db.execute(
        "SELECT payload, resulting_state FROM workflow_event WHERE event_key=?",
        (data["event_key"],)
    ).fetchone()
    if prior:
        if prior[0] != payload:
            raise ValueError("Workflow identifier reused with different evidence")
        result = prior[1]
    else:
        row = db.execute(
            "SELECT id, state, reserve_required_cents FROM case_file WHERE case_key=?",
            (data["case_key"],)
        ).fetchone()
        if row is None:
            raise ValueError("Create the intake record before transitioning")
        expected, result = transitions[data["action"]]
        if row[1] != expected:
            raise ValueError("Current state does not permit this transition")
        if data["action"] == "verify":
            checks = ("title_ok", "underlying_ok", "rmlo_ok", "exit_funded")
        elif data["action"] == "ready":
            checks = ("notices_ok", "insurance_ok", "taxes_ok", "servicer_ok")
        elif data["action"] == "close":
            checks = ("recording_ok", "funding_settled", "boarding_accepted")
        else:
            checks = ("escrow_settled",)
            amount = data.get("reserve_cents")
            if type(amount) is not int or amount < row[2]:
                raise ValueError("Verified settled reserve is below the required amount")
        if any(data.get(key) is not True for key in checks):
            raise ValueError("Independent evidence review remains incomplete")
        changed = db.execute(
            "UPDATE case_file SET state=? WHERE id=? AND state=?",
            (result, row[0], expected)
        ).rowcount
        if changed != 1:
            raise RuntimeError("Expected exactly one atomic state transition")
        db.execute(
            "INSERT INTO workflow_event "
            "(event_key, case_id, payload, resulting_state) VALUES (?, ?, ?, ?)",
            (data["event_key"], row[0], payload, result)
        )
    db.execute("COMMIT")
    print(json.dumps({"resulting_state": result}))
except Exception:
    if db.in_transaction:
        db.execute("ROLLBACK")
    raise
finally:
    db.close()
""",
                        "Serialized transitions bind each forward state change to independently reviewed evidence",
                        "Retries return recorded outcomes while conflicting or premature transitions fail",
                    ],
                    [
                        "Module 4 — save settled cash and statement import as cash.py",
                        """from __future__ import annotations

import json
import re
import sqlite3
import sys

data = json.load(sys.stdin)
period = data.get("period", "")
if not isinstance(period, str) or not re.fullmatch(
    r"[0-9]{4}-(0[1-9]|1[0-2])", period
):
    raise ValueError("Use a calendar period formatted as YYYY-MM")
payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
db = sqlite3.connect("ledger.sqlite", timeout=10, isolation_level=None)
db.execute("PRAGMA foreign_keys=ON")
try:
    db.execute("BEGIN IMMEDIATE")
    if data.get("operation") == "bank_control":
        if type(data.get("net_cash_cents")) is not int:
            raise ValueError("Provide independently normalized integer cash cents")
        ref = data.get("statement_ref")
        if not isinstance(ref, str) or not ref.strip():
            raise ValueError("Provide the independent statement export reference")
        prior = db.execute(
            "SELECT payload FROM bank_control WHERE period=?", (period,)
        ).fetchone()
        if prior:
            if prior[0] != payload:
                raise ValueError("Period control conflicts with its recorded statement")
        else:
            db.execute(
                "INSERT INTO bank_control VALUES (?, ?, ?, ?)",
                (period, data["net_cash_cents"], ref, payload)
            )
    elif data.get("operation") == "post":
        for key in ("event_key", "settlement_ref", "evidence_ref"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                raise ValueError("Supply durable posting and evidence references")
        if data.get("earned") is not True or data.get("settled") is not True:
            raise ValueError("This bounded ledger accepts earned and settled amounts only")
        amount = data.get("amount_cents")
        kind = data.get("kind")
        if type(amount) is not int or amount <= 0:
            raise ValueError("Provide a positive integer amount in cents")
        if kind not in ("upfront", "interest", "opex"):
            raise ValueError("Choose an operator contribution or operating cost category")
        prior = db.execute(
            "SELECT payload FROM journal WHERE event_key=?",
            (data["event_key"],)
        ).fetchone()
        if prior:
            if prior[0] != payload:
                raise ValueError("Posting identifier conflicts with its original payload")
        else:
            case_id = None
            if kind != "opex":
                row = db.execute(
                    "SELECT id, state FROM case_file WHERE case_key=?",
                    (data.get("case_key"),)
                ).fetchone()
                if row is None or row[1] != "CLOSED":
                    raise ValueError("Contribution requires a closed and boarded case")
                case_id = row[0]
            revenue = amount if kind != "opex" else 0
            expense = amount if kind == "opex" else 0
            db.execute(
                "INSERT INTO journal "
                "(event_key, settlement_ref, case_id, period, kind, payload, "
                "cash_cents, revenue_cents, expense_cents) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    data["event_key"], data["settlement_ref"], case_id,
                    period, kind, payload, revenue - expense, revenue, expense
                )
            )
    else:
        raise ValueError("Choose post or bank_control as the operation")
    db.execute("COMMIT")
    print("Accepted atomically or matched an identical recorded retry")
except Exception:
    if db.in_transaction:
        db.execute("ROLLBACK")
    raise
finally:
    db.close()
""",
                        "One immutable balanced record posts each normalized settled contribution exactly once",
                        "Settlement collisions and unclosed cases stop posting without partial ledger writes",
                    ],
                    [
                        "Module 5 — save reconciliation and account views as reports.sql",
                        """CREATE VIEW IF NOT EXISTS v_monthly AS
SELECT
    period,
    SUM(revenue_cents) AS revenue_cents,
    SUM(expense_cents) AS expense_cents,
    SUM(cash_cents) AS net_cash_cents
FROM journal
GROUP BY period;

CREATE VIEW IF NOT EXISTS v_reconciliation AS
WITH periods AS (
    SELECT period FROM journal
    UNION
    SELECT period FROM bank_control
)
SELECT
    p.period,
    COALESCE(m.revenue_cents, 0) AS revenue_cents,
    COALESCE(m.expense_cents, 0) AS expense_cents,
    COALESCE(m.net_cash_cents, 0) AS ledger_cash_cents,
    b.net_cash_cents AS bank_cash_cents,
    CASE WHEN b.period IS NULL THEN NULL
         ELSE COALESCE(m.net_cash_cents, 0) - b.net_cash_cents
    END AS difference_cents,
    CASE
        WHEN b.period IS NULL THEN 'Independent bank control required'
        WHEN COALESCE(m.net_cash_cents, 0) != b.net_cash_cents
            THEN 'Investigate operator cash reconciliation difference'
        ELSE 'Operator cash agrees with independent statement control'
    END AS reconciliation_status
FROM periods p
LEFT JOIN v_monthly m ON m.period = p.period
LEFT JOIN bank_control b ON b.period = p.period;

CREATE VIEW IF NOT EXISTS v_account_lines AS
SELECT id AS journal_id, period, 'Operator cash' AS account,
       cash_cents AS debit_cents
FROM journal
UNION ALL
SELECT id, period, 'Retained operator revenue', -revenue_cents
FROM journal WHERE revenue_cents != 0
UNION ALL
SELECT id, period, 'Operator operating expense', expense_cents
FROM journal WHERE expense_cents != 0;
""",
                        "Independent statement controls expose missing periods and unmatched operator cash movement",
                        "Signed account lines sum to zero for every accepted journal identifier",
                    ],
                    [
                        "Module 6 — save repeatable ledger checks as qa.py",
                        """from __future__ import annotations

import sqlite3

db = sqlite3.connect("ledger.sqlite", timeout=10, isolation_level=None)
try:
    db.execute("BEGIN")
    integrity = db.execute("PRAGMA integrity_check").fetchall()
    if integrity != [("ok",)]:
        raise RuntimeError("SQLite structural integrity check failed")
    if db.execute("PRAGMA foreign_key_check").fetchall():
        raise RuntimeError("Foreign key integrity check failed")
    if db.execute("SELECT COUNT(*) FROM journal").fetchone()[0] == 0:
        raise RuntimeError("Load a reviewed test cohort before accepting QA")
    differences = db.execute(
        "SELECT period, difference_cents FROM v_reconciliation "
        "WHERE bank_cash_cents IS NULL OR difference_cents != 0"
    ).fetchall()
    if differences:
        raise RuntimeError("Resolve monthly operator cash controls: " + repr(differences))
    unbalanced = db.execute(
        "SELECT journal_id FROM v_account_lines GROUP BY journal_id "
        "HAVING SUM(debit_cents) != 0"
    ).fetchall()
    if unbalanced:
        raise RuntimeError("Account line balance check failed")
    open_cases = db.execute(
        "SELECT j.id FROM journal j JOIN case_file c ON c.id=j.case_id "
        "WHERE j.kind != 'opex' AND c.state != 'CLOSED'"
    ).fetchall()
    if open_cases:
        raise RuntimeError("Contribution exists against an incomplete case")
    db.execute("COMMIT")
    print("Ledger integrity, account balance, and operator cash controls passed")
finally:
    if db.in_transaction:
        db.execute("ROLLBACK")
    db.close()
""",
                        "A consistent read snapshot checks balances without racing concurrent committed writes",
                        "Failures stop acceptance and report the affected reconciliation periods explicitly",
                    ],
                ],
            },
        },
        {
            "heading": "3. Close, board, collect, and investigate exceptions without obscuring obligations",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "For every owner-occupant wrap in this operating model, engage a licensed "
                    "RMLO before promising terms or collecting nonrefundable origination "
                    "money. Verify the originator through NMLS Consumer Access and confirm "
                    "the relevant state authority, entity coverage, and activity scope. "
                    "The SAFE Act framework includes 12 U.S.C. §5103; loan-originator "
                    "requirements and limited seller-financer exclusions also appear in "
                    "12 CFR §1026.36. Do not turn an exclusion into a blanket exemption "
                    "from other lending duties. Determine the applicable creditor, loan, "
                    "and transaction coverage, then document repayment capacity under "
                    "12 CFR §1026.43 where required. Keep verified income, assets, employment, "
                    "debts, credit obligations, payment calculations, and underwriting "
                    "conclusions in the protected loan file. Underwrite the buyer's full "
                    "scheduled housing burden, including taxes, insurance, association dues, "
                    "and any balloon exposure, rather than the operator's desired spread. "
                    "The underwriting decision must precede closing and survive independent "
                    "file review. If the buyer fails, stop that buyer's transaction; do not "
                    "replace missing income verification with a larger down payment or "
                    "relabel an owner-occupied purchase as business-purpose credit. A "
                    "different qualified buyer, a conventional sale, or withdrawal is the "
                    "operating fallback, with each alternative repriced against actual carrying costs."
                ),
                (
                    "Escrow instructions should connect seller disclosures, underlying "
                    "lien information, buyer documents, recorded security instruments, "
                    "insurance interests, and payment routing in one closing checklist. "
                    "For Texas property, evaluate Property Code §5.016, including required "
                    "notice contents, timing, delivery, and applicable exceptions; separately "
                    "evaluate Finance Code Chapter 159 for wrap mortgage lending requirements. "
                    "Do not assume one disclosure satisfies the other regime. Have the "
                    "closing professional confirm the applicable delivery calendar before "
                    "scheduling signatures. Insurance must reflect actual ownership, "
                    "occupancy, lender interests, and the transaction structure; an old "
                    "policy left untouched can create a serious coverage dispute. Confirm "
                    "tax escrow responsibility without collecting the same obligation "
                    "through two incompatible channels. Board the licensed third-party "
                    "servicer using executed documents, amortization schedules, underlying "
                    "loan information, payment permissions, tax and insurance instructions, "
                    "and a tested reporting destination. Require written boarding acceptance. "
                    "The operator must never substitute an internal spreadsheet for proof "
                    "that the underlying lender received payment. If recording, funding, "
                    "or boarding fails, preserve escrow restrictions and use the closing "
                    "professional's documented correction process. No script in this chapter "
                    "authorizes escrow release, alters borrower rights, or cures a missed "
                    "statutory notice."
                ),
                (
                    "Run collections through the servicer, but keep exception ownership "
                    "inside the operator team. Each month match borrower receipts to "
                    "contractual allocations, underlying lender credits, escrow movements, "
                    "fees, principal changes, and retained interest. A $2,000 borrower "
                    "receipt is not $2,000 of operator revenue when most funds satisfy "
                    "another obligation. Export the actual retained amount only after "
                    "the waterfall and settlement agree. Configure alerts for returned "
                    "payments, lender-side posting delays, insurance cancellation notices, "
                    "tax delinquency, maturity changes, and unexplained suspense balances. "
                    "A buyer default requires a dated contact and resolution log, applicable "
                    "notices, and state-specific enforcement work; it does not permit "
                    "self-help possession or improvised eviction. Where applicable, "
                    "12 CFR §1024.41 restricts foreclosure timing and establishes loss "
                    "mitigation procedures, including the general 120-day delinquency "
                    "threshold subject to its conditions and exceptions. Reserve enough "
                    "liquidity to keep underlying obligations current while the lawful "
                    "process runs. If the underlying lender accelerates, activate the "
                    "documented payoff or refinance response and recalculate cash needs "
                    "immediately. Report an interrupted spread as an interrupted spread. "
                    "Do not smooth missing collections into reported revenue merely because "
                    "the annual scorecard assumes a performing portfolio and a target level "
                    "of production."
                ),
            ],
            "table": {
                "caption": "Closing, Servicing, and Exception Ownership Control Matrix",
                "headers": [
                    "Control point and responsible operating specialist",
                    "Evidence required before the next action",
                    "Specific accounting or transaction treatment",
                    "Exception response with an accountable owner",
                ],
                "rows": [
                    [
                        "Licensed RMLO completes owner-occupant underwriting before closing",
                        "Verified repayment records, applicable disclosures, and documented underwriting conclusion",
                        "Buyer affordability uses full scheduled housing obligations rather than desired spread",
                        "Operator replaces failed buyer or withdraws instead of inventing qualifications",
                    ],
                    [
                        "Closing professional reviews Texas transfer and wrap requirements",
                        "Section 5.016 analysis and Chapter 159 applicability documentation",
                        "Required delivery periods enter the closing calendar before signatures",
                        "Closing professional postpones execution when applicable notice evidence is incomplete",
                    ],
                    [
                        "Escrow holder verifies settlement and recording instructions independently",
                        "Executed instruments, approved settlement statement, and verified disbursement destinations",
                        "Refundable amounts remain outside earned operator contribution until properly released",
                        "Escrow holder retains restrictions until documented correction conditions are satisfied",
                    ],
                    [
                        "Insurance specialist confirms actual ownership and occupancy interests",
                        "Current binder or policy with appropriate insured and lender interests",
                        "Premium funding follows the documented escrow responsibility without duplicate collection",
                        "Operator obtains replacement coverage before allowing an uninsured exposure",
                    ],
                    [
                        "Licensed servicer accepts the complete boarding package",
                        "Accepted schedules, underlying account routing, and borrower payment setup",
                        "Underlying debt service remains a pass-through rather than operator revenue",
                        "Servicer rejects inconsistent schedules and returns the file for correction",
                    ],
                    [
                        "Bookkeeper reconciles lender credits against servicer remittance evidence",
                        "Borrower allocations, lender statements, escrow activity, and settled bank exports",
                        "Principal changes and trust balances stay outside retained spread revenue",
                        "Operator suspends distributions while bookkeeper resolves each unmatched amount",
                    ],
                    [
                        "Operator and enforcement counsel manage default or acceleration",
                        "Dated delinquency evidence, applicable notices, and updated payoff calculations",
                        "Carrying costs enter actual expenses when incurred rather than being concealed",
                        "Use funded cure, refinance, negotiated resolution, or lawful enforcement procedures",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before a file can become CLOSED",
                "body": (
                    "Each check requires identifiable evidence and an accountable reviewer. "
                    "A checked box without the underlying record cannot advance the file."
                ),
                "items": [
                    "Verify title, senior debt, maturity, arrears, due-on-sale exposure, and a funded payoff or refinance response against current source documents.",
                    "Verify licensed RMLO involvement, transaction-specific lending coverage, documented buyer repayment capacity, and required disclosures before execution.",
                    "Verify settled escrow, required notice delivery, recording instructions, appropriate insurance interests, and explicit tax-payment responsibility.",
                    "Verify licensed-servicer acceptance, underlying-payment routing, lender-side confirmation access, and a complete reconciliation owner before releasing operator distributions.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture and score the authorized intake",
                    "action": "Import a stable parcel and source key through intake.py.",
                    "detail": "Attach original debt and assessor evidence; treat the computed score only as review priority, never as purchase or credit authority.",
                },
                {
                    "step": 2,
                    "title": "Verify obligations and document funded escrow",
                    "action": "Record verify and escrow events through workflow.py after independent review.",
                    "detail": "The reserve amount must meet the reviewed requirement, and the evidence reference must identify actual settled funds rather than a pending transfer.",
                },
                {
                    "step": 3,
                    "title": "Complete closing and obtain boarding acceptance",
                    "action": "Record ready and close only after the closing professional and servicer complete their respective checks.",
                    "detail": "Preserve notices, executed documents, recording evidence, settlement evidence, and accepted servicing schedules in the protected transaction package.",
                },
                {
                    "step": 4,
                    "title": "Post settled contribution and close the month",
                    "action": "Import eligible net entries and independent statement controls through cash.py, then run qa.py.",
                    "detail": "Resolve differences before distributions; separately reconcile the full servicing waterfall, escrow obligations, and underlying lender credits.",
                },
            ],
        },
        {
            "heading": "4. Walk a 90-day replacement cohort into the exact Base run rate",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The cohort is an established operator's replacement-production "
                    "exercise, not a claim that a startup creates a seasoned portfolio "
                    "in ninety days. Begin with forty performing wrap positions and "
                    "replenish scheduled exits so the average performing exposure remains "
                    "forty note-years annually. Each position contributes an illustrative "
                    "$5,000 annual retained interest margin after underlying interest "
                    "pass-through, producing $200,000 annually. Actual servicing schedules "
                    "must support that amount; principal amortization and property value "
                    "are excluded. Separately, twenty-five annual placements retain "
                    "$11,000 each, producing $275,000. One illustrative closing receives "
                    "$18,000 of buyer funds and applies $7,000 to seller and direct "
                    "settlement allocations, leaving $11,000 earned operator spread; "
                    "escrow verifies the contractual entitlement and excludes refundable "
                    "amounts. Together, $275,000 plus $200,000 equals exactly $475,000 "
                    "of canonical revenue. The quarter closes one, two, and three "
                    "replacement placements, with matching departures at month-end. "
                    "Departing positions supply their final scheduled month; replacements "
                    "begin the next monthly collection cycle, preventing double-counted "
                    "interest. This assumes uninterrupted replacement and collections. "
                    "A missed payment, delayed placement, or vacancy changes actual "
                    "results and must appear as a variance rather than an invisible "
                    "adjustment to the target."
                ),
                (
                    "Track lead cohorts separately from cash dates. Month 1 receives "
                    "sixty leads, scrubs forty-eight, completes twelve desk reviews, "
                    "advances three diligence files, and closes one. Month 2 receives "
                    "eighty leads, scrubs sixty-four, reviews sixteen, advances five, "
                    "and closes two. Month 3 receives one hundred leads, scrubs "
                    "eighty, reviews twenty, advances seven, and closes three. Each "
                    "cohort closes within its labeled month only because these are "
                    "prequalified replacement opportunities inside an established "
                    "pipeline; a new operator should instead expect the stated two-to-six "
                    "month first-deal interval. The table accounts for every unclosed "
                    "lead rather than treating review activity as inventory. Failed "
                    "diligence consumes $1,000, $1,500, and $2,000 respectively, "
                    "already included in monthly operating outlays. No borrower credit "
                    "loss occurs in this worked case, and no refundable deposits are "
                    "counted as receipts. Monthly retained interest is $16,666.67, "
                    "$16,666.67, and $16,666.66, exactly $50,000 for the quarter. "
                    "Round at the portfolio reporting level while preserving individual "
                    "servicer allocations in cents. Closing contribution arrives only "
                    "after settlement; monthly interest arrives only after the servicer "
                    "waterfall and bank evidence support the recognized retained amount."
                ),
                (
                    "Use $23,750 of monthly all-in operating outlays for this established "
                    "Base business: $8,000 fixed platform and administrative overhead, "
                    "$12,000 variable acquisition and production expense, and $3,750 "
                    "contracted servicing, bookkeeping, and specialist support. The "
                    "$8,000 fixed component fits the stated $2,000–$12,000 monthly "
                    "overhead planning range; that range cannot be treated as the "
                    "entire Base cost base because $475,000 revenue less $190,000 "
                    "profit requires $285,000 annual expenses. Do not deduct the "
                    "$7,000 settlement allocation again: it was already removed "
                    "when deriving each $11,000 retained upfront spread. Quarterly "
                    "revenue is $116,000, expenses are $71,250, and operating cash "
                    "contribution is $44,750. This illustration assumes recognized "
                    "amounts settle within the same month, with no owner distributions "
                    "or new capital expenditures. A normalized Base quarter has "
                    "6.25 placements, $118,750 revenue, and $47,500 profit. The "
                    "worked quarter is lower by one-quarter placement, or $2,750. "
                    "Complete nineteen additional placements over the remaining nine "
                    "months while maintaining forty performing note-years to reach "
                    "the exact annual Base result. Conservative and Scaled retain "
                    "their separate canonical margins; neither is inferred by multiplying "
                    "this short cohort's observed cash margin."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Cohort or reconciliation checkpoint",
                    "Lead movement, scrubs, and production evidence",
                    "Settled contribution and operating expense timing",
                    "Cumulative cash or canonical reconciliation result",
                ],
                "rows": [
                    [
                        "Opening position before the first cohort begins",
                        "Forty performing positions exist before replacement production starts",
                        "Existing acquisition capital and funded reserves are opening assets, not receipts",
                        "Cumulative incremental operating cash starts at exactly $0.00",
                    ],
                    [
                        "Month 1 cohort closes one replacement placement",
                        "60 leads: 48 scrubbed, 9 desk-rejected, 2 diligence-rejected, 1 closed",
                        "$11,000 upfront plus $16,666.67 interest less $23,750 outlays equals $3,916.67",
                        "$3,916.67 cumulative; $1,000 failed diligence included; zero borrower losses",
                    ],
                    [
                        "Month 2 cohort closes two replacement placements",
                        "80 leads: 64 scrubbed, 11 desk-rejected, 3 diligence-rejected, 2 closed",
                        "$22,000 upfront plus $16,666.67 interest less $23,750 outlays equals $14,916.67",
                        "$18,833.34 cumulative; $1,500 failed diligence included; zero borrower losses",
                    ],
                    [
                        "Month 3 cohort closes three replacement placements",
                        "100 leads: 80 scrubbed, 13 desk-rejected, 4 diligence-rejected, 3 closed",
                        "$33,000 upfront plus $16,666.66 interest less $23,750 outlays equals $25,916.66",
                        "$44,750.00 cumulative; $2,000 failed diligence included; zero borrower losses",
                    ],
                    [
                        "Ninety-day actual totals preserve every cohort disposition",
                        "240 leads resolve into 192 scrubs, 33 desk rejections, 9 diligence rejections, 6 placements",
                        "$66,000 upfront plus $50,000 interest less $71,250 expenses equals $44,750",
                        "Six matched departures preserve forty performing positions without overlapping interest",
                    ],
                    [
                        "Normalized Base quarter supplies the explicit annualization bridge",
                        "6.25 average placements replace the worked quarter's six completed placements",
                        "$68,750 upfront plus $50,000 interest less $71,250 expenses equals $47,500",
                        "Actual contribution trails normalized Base by exactly $2,750 quarterly",
                    ],
                    [
                        "Annual scorecard checks preserve all three canonical scenarios",
                        "Base requires 25 placements and forty performing note-years across the full year",
                        "Conservative: $100,000 less $72,000; Base: $475,000 less $285,000; Scaled: $850,000 less $408,000",
                        "Owner profit reconciles to $28,000 at 28%, $190,000 at 40.0%, and $442,000 at 52%",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A spread becomes an operating result only when the obligations, servicing waterfall, and settled cash reconcile to the same evidence.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create parcel-level intake records with stable source keys, current loan evidence, assessor notice dates, and independently calculated protest deadlines.",
        "Document the eleven operating workstreams and keep property_tax_assessment_appeal_contingency engagements, savings verification, and fees separate from wrap revenue.",
        "Have the RMLO and closing professional verify buyer qualification, applicable lending rules, transfer notices, title, insurance, and the funded acceleration response.",
        "Deploy the six reference files in an isolated project environment and test concurrent retries, conflicting identifiers, illegal transitions, and interrupted transactions before production use.",
        "Require licensed-servicer boarding acceptance and monthly lender-side payment proof, then reconcile underlying debt service, escrow movements, and retained operator contribution separately.",
        "Reproduce the $44,750 cohort cash result and $2,750 normalized-quarter bridge, then track nineteen remaining placements and forty performing note-years against the annual Base plan.",
    ],
    "statutory_citations": [
        {
            "title": "12 U.S.C. §1701j-3 — Preemption of due-on-sale prohibitions",
            "url": "https://www.law.cornell.edu/uscode/text/12/1701j-3",
            "relevance": "Establishes the federal due-on-sale framework and enumerated transfer exceptions; ordinary investor acquisitions require explicit acceleration analysis.",
        },
        {
            "title": "12 U.S.C. §5103 — License or registration required",
            "url": "https://www.law.cornell.edu/uscode/text/12/5103",
            "relevance": "Supports verification of the applicable mortgage loan originator licensing or registration requirement before owner-occupant origination work.",
        },
        {
            "title": "12 CFR §1026.36 — Prohibited acts or practices and certain requirements for credit secured by a dwelling",
            "url": "https://www.consumerfinance.gov/rules-policy/regulations/1026/36/",
            "relevance": "Provides loan-originator provisions and limited seller-financer exclusions whose conditions must be evaluated without assuming broader exemptions.",
        },
        {
            "title": "12 CFR §1026.43 — Minimum standards for transactions secured by a dwelling",
            "url": "https://www.consumerfinance.gov/rules-policy/regulations/1026/43/",
            "relevance": "Provides applicable ability-to-repay requirements, transaction coverage, verification standards, and underwriting factors for covered dwelling-secured credit.",
        },
        {
            "title": "Texas Property Code §5.016 — Conveyance of residential property encumbered by lien",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.016",
            "relevance": "Requires transaction-specific analysis of notice contents, timing, recipients, and exceptions when residential property remains encumbered.",
        },
        {
            "title": "Texas Finance Code Chapter 159 — Wrap mortgage loan financing",
            "url": "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
            "relevance": "Supplies Texas wrap mortgage provisions that require separate review of licensing, disclosures, exemptions, and duties.",
        },
        {
            "title": "Texas Tax Code §41.44 — Notice of protest",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.41.htm#41.44",
            "relevance": "Controls protest filing deadlines and relevant timing rules for the county assessment appeal workflow.",
        },
        {
            "title": "Texas Tax Code §41.43 — Protest of determination of value or inequality of appraisal",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.41.htm#41.43",
            "relevance": "Provides the statutory framework for value and unequal-appraisal protests supported by parcel-level comparable evidence.",
        },
        {
            "title": "12 CFR §1024.41 — Loss mitigation procedures",
            "url": "https://www.consumerfinance.gov/rules-policy/regulations/1024/41/",
            "relevance": "Establishes applicable loss mitigation and foreclosure-related servicing requirements, including the general 120-day threshold subject to coverage and exceptions.",
        },
    ],
}
