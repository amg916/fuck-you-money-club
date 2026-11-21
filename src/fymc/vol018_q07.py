from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "land-flipping-complete-operating-process-production-blueprint-90-day-cohort",
    "question_prompt": "How does an operator execute land flipping end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "County GIS to Insured Closing: SQLite Event Accounting, Recorded Access, UCC-Aware Title Review, and a Cash-Reconciled Land Cohort",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #6, Land Flipping, ranks #18 with a 72/100 Money-to-Manpower Score. "
        "This chapter maps six operator plays: county screening, owner sourcing, access-cleared "
        "vacant resale, buildable infill, minor subdivision, and title-insured disposition. "
        "A one-full-time-owner, three-contractor pod runs evidence-backed acquisitions rather "
        "than speculative parcel accumulation. Six executable reference modules connect intake, "
        "screening, verification, escrow states, immutable accounting events, and bank reconciliation. "
        "The worked cohort separates $212,500 of quarterly gross sale proceeds from acquisition "
        "basis, operating expense, and unsold inventory. Annual owner profits remain exactly "
        "$24,000 Conservative, $157,250 Base, and $375,000 Scaled. The operating discipline is "
        "simple: document access, price verified uses, preserve closing evidence, and reconcile "
        "every dollar before recycling acquisition capital."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$200,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "12% net margin; $24,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$850,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "18.5% net margin; $157,250 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,500,000",
            "context": "Annual gross parcel sale proceeds; acquisition costs included in net margin",
            "note": "25% net margin; $375,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Route six plays through one evidence-controlled acquisition pod",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a county, a buyer profile, and an explicit exclusion map, not a national "
                    "list of inexpensive acreage. Candidate #6's six chapter-mapped plays are county "
                    "screening, owner sourcing, access-cleared vacant resale, buildable infill, minor "
                    "subdivision, and title-insured disposition. County screening identifies the operating "
                    "territory; owner sourcing creates permissioned conversations and offers; the next "
                    "three plays describe alternative parcel treatments; disposition converts inventory "
                    "into collected sale proceeds. They are not six simultaneous businesses or six "
                    "independent revenue streams. Use QGIS with county assessor polygons, recorded "
                    "plats, FEMA flood layers, and dated aerial imagery to establish the first-pass "
                    "universe. Preserve county identifiers and leading zeros in assessor parcel numbers; "
                    "an address is neither a stable parcel key nor proof of ownership. Track the "
                    "source date of every layer because assessment boundaries and recently recorded "
                    "splits can disagree. Reject parcels outside the chosen buyer's price, access, "
                    "utility, or topography envelope before purchasing expensive reports. A low "
                    "assessment does not establish a discount, and an advertised road does not "
                    "establish a recorded right of passage. Screening produces a research queue; "
                    "only verified instruments and settlement evidence advance a parcel toward cash."
                ),
                (
                    "Constrain the Base pod to one full-time owner and three scoped contractors: "
                    "a GIS and comparable-sales analyst, a title and escrow provider, and a survey "
                    "or land-use specialist. The owner controls offers, acquisition capital, exceptions, "
                    "and buyer negotiations. Contractor counts describe recurring delivery relationships, "
                    "not three full-time salaries hidden inside a small expense allowance. Obtain "
                    "written scopes and quotes; engage additional specialists only by replacing scope "
                    "or explicitly revising the operating plan. Reserve a thirty-six-hour owner week "
                    "across sourcing, underwriting, contractor review, disposition, and reconciliation. "
                    "Keep four hours available for access disputes, failed closings, and seller "
                    "documents rather than selling all forty hours to a spreadsheet. The cohort "
                    "budget uses $6,000 monthly operating expense, within the canonical $3,000 to "
                    "$15,000 range, and includes recurring contractor support and unsuccessful "
                    "diligence. Settlement-specific costs sit separately in deal expense. Owner profit "
                    "is the modeled residual before owner distributions; do not quietly add an "
                    "owner salary and still claim the same margin. Limit active acquisitions to "
                    "the capital and specialist capacity actually available. A speculative subdivision "
                    "can occupy the same survey resource needed to rescue an otherwise straightforward "
                    "infill closing."
                ),
                (
                    "Underwrite the exit before negotiating the purchase. Build a comparable-sale packet "
                    "from recorded transfers, verified brokerage information, and direct buyer feedback; "
                    "separate closed sales from listings and exclude transfers with materially different "
                    "access, utilities, entitlement, or acreage. Calculate the offer ceiling as expected "
                    "gross resale proceeds less acquisition basis additions, selling costs, holding "
                    "costs, allocated operating expense, and required owner profit. Do not multiply "
                    "county assessed value by an arbitrary discount and call the result underwriting. "
                    "For access-cleared vacant resale, obtain the recorded easement and confirm its "
                    "benefited parcel, permitted uses, maintenance obligations, and connection to a "
                    "public road. For infill, obtain the applicable zoning text, setbacks, minimum "
                    "lot dimensions, utility service conditions, and a defensible buildable envelope. "
                    "For minor subdivisions, establish the local plat procedure and realistic survey, "
                    "review, improvement, and recording costs before assuming additional saleable "
                    "lots. California Government Code sections 66424 and 66426 illustrate why "
                    "parcel creation is a statutory process rather than a GIS drawing exercise. "
                    "Keep the worked cohort on existing parcels without entitlement upside. That "
                    "choice isolates ordinary acquisition and disposition execution from development "
                    "risk and prevents an unapproved split from subsidizing the Base margin."
                ),
            ],
            "table": {
                "caption": "Six Mapped Land-Flipping Plays and Four-Person Pod Responsibilities",
                "headers": [
                    "Mapped operator play",
                    "Required evidence and named working tools",
                    "Accountable pod member and capacity boundary",
                    "Economic decision and principal failure mode",
                ],
                "rows": [
                    [
                        "Play one: county screening establishes a repeatable acquisition territory.",
                        "QGIS project preserves assessor polygons, source dates, flood overlays, and exclusions.",
                        "GIS contractor researches; owner approves one bounded county acquisition thesis.",
                        "Reject weak buyer demand before spending scarce title and survey dollars.",
                    ],
                    [
                        "Play two: owner sourcing turns selected parcels into priced offers.",
                        "Recorded ownership, mailing provenance, response history, and signed offer terms remain linked.",
                        "Owner handles negotiations; analyst prepares evidence without representing unrelated sellers.",
                        "Measure accepted offers against collected sale proceeds rather than lead counts.",
                    ],
                    [
                        "Play three: access-cleared vacant resale monetizes a verified usability discount.",
                        "Recorded easement, public-road connection, survey exceptions, and maintenance duties support pricing.",
                        "Title provider checks instruments; survey specialist resolves physical boundary conflicts.",
                        "A visible track without enforceable access can destroy the planned exit.",
                    ],
                    [
                        "Play four: buildable infill matches small parcels with identified builders.",
                        "Zoning text, setbacks, utility letters, and topographic envelope substantiate buyer utility.",
                        "Land-use specialist checks constraints; owner obtains direct builder price feedback.",
                        "Utility extension costs can exceed the apparent discount on purchase price.",
                    ],
                    [
                        "Play five: minor subdivision creates lots only through completed local procedures.",
                        "Survey proposal, subdivision ordinance, agency conditions, and recorded plat define deliverables.",
                        "Survey specialist owns technical scope; owner caps capital and calendar exposure.",
                        "Keep unrecorded additional lots outside booked revenue and cohort exit assumptions.",
                    ],
                    [
                        "Play six: title-insured disposition converts owned inventory into reconciled cash.",
                        "Executed contract, settlement statement, deed recording, and title coverage support closure.",
                        "Escrow provider closes; owner independently confirms bank receipt and accounting entries.",
                        "Report gross parcel proceeds while deducting acquisition basis and settlement costs.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four checks that protect the land spread",
                "body": "Experienced operators buy document-supported usability, not attractive satellite images.",
                "items": [
                    "Ask the title examiner to identify the exact recorded instrument supplying access; compare its legal description with the parcel being acquired.",
                    "Request both utility availability and the conditions of service; a nearby main can still require expensive extensions, capacity work, or easements.",
                    "Call two actual builders about a dimensioned infill sketch before using their neighborhood sales as comparable evidence.",
                    "Price the existing legal parcel first; treat a proposed split as a separate investment until survey, agency conditions, and recording costs are documented.",
                ],
            },
        },
        {
            "heading": "2. Assemble six executable modules with atomic state and accounting transitions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The six-module reference below is a small SQLite application, not a payment "
                    "robot or a replacement for professional title examination. Copy the code cells "
                    "in order into one Python file, call initialize with a database path, and keep "
                    "that file on a local filesystem controlled by the operator. SQLite WAL, "
                    "foreign keys, integer cents, unique identities, and BEGIN IMMEDIATE transactions "
                    "serialize database decisions across local processes. A busy writer fails after "
                    "the configured timeout; the caller retries the complete request with the same "
                    "event key. Never retry only the posting portion. Every state-changing request "
                    "contains a stable source identifier, external event identifier, and canonical "
                    "payload. Identical replays return the original event; a reused identifier with "
                    "different contents raises an error. State validation, evidence checks, balanced "
                    "journal insertion, and state advancement occur inside one transaction, eliminating "
                    "the database check-then-write race. The reference deliberately sends no external "
                    "wires, deeds, or messages. Escrow performs those actions through its established "
                    "controls; this application records confirmed results. Consequently, a timeout "
                    "cannot issue a second payment. Multi-host deployment requires a server database "
                    "and equivalent transaction semantics rather than a shared network-mounted SQLite file."
                ),
                (
                    "Treat evidence as attributed, immutable review records, not boolean truth supplied "
                    "by a public web form. Each record names a reviewer, document location, digest, "
                    "verdict, and expiration time. The latest review for each required category "
                    "controls advancement; a failed replacement blocks the next transition even if "
                    "an earlier review passed. The code expects its callers to be trusted internal "
                    "adapters behind operating-system access controls. Reviewer names are audit "
                    "metadata, not authentication credentials, and the program does not independently "
                    "fetch or interpret the referenced documents. The screening score merely orders "
                    "work: documented access, plausible zoning fit, closed comparable coverage, and "
                    "environmental screening contribute explicit points. A high score cannot substitute "
                    "for the later evidence requirements. Verify environmental assumptions against "
                    "site history and appropriate professional investigation. When CERCLA liability "
                    "protections are being pursued, 42 U.S.C. 9601(40) and 40 CFR Part 312 "
                    "make timing and scope material; a desktop wetland layer alone does not "
                    "satisfy all appropriate inquiries. Obtain jurisdiction-specific wetlands advice "
                    "before proposing fill under Clean Water Act section 404. Keep investigation "
                    "findings attached to the parcel so a subsequent buyer package cannot silently "
                    "drop an inconvenient constraint."
                ),
                (
                    "The journal recognizes acquisition as inventory against cash, not immediate loss. "
                    "A completed sale records gross proceeds as revenue, releases the parcel's "
                    "actual inventory basis into cost of goods sold, and expenses settlement "
                    "deductions. Because escrow commonly remits a net deposit, the sale has one "
                    "cash line for proceeds less deductions; that line reconciles to one immutable "
                    "bank reference. Monthly operating expense uses a separate event and reference. "
                    "The example assumes full-cash purchases, full-cash sales, and expenses paid "
                    "when recorded. Earnest-money advances, debt, seller notes, multiple settlement "
                    "disbursements, and partial-lot allocations require additional accounts and event "
                    "types before use; never force those transactions into the simplified handlers. "
                    "The reconciliation view compares imported bank amounts with posted cash, "
                    "including bank-only and ledger-only references. A balanced journal is necessary "
                    "but insufficient: an entirely omitted closing can still leave debits equal "
                    "to credits. Import complete statement coverage and investigate every unmatched "
                    "reference. Run the supplied checks after posting and again after the statement "
                    "period closes. They test journal balance, inventory state, bank matching, "
                    "duplicate handling, and rollback in an isolated database. These reference "
                    "checks are provided for execution; no test execution or production certification "
                    "is asserted here."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Executable reference module",
                    "Copy-pasteable Python and SQL implementation",
                    "Operator integration contract",
                    "Concurrency and audit invariant",
                ],
                "rows": [
                    [
                        "Module one establishes schema, connection policy, and serialized transaction boundaries.",
                        r'''import hashlib
import json
import sqlite3
import time
from contextlib import contextmanager

def connect(path):
    connection = sqlite3.connect(
        str(path), timeout=30, isolation_level=None
    )
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 30000")
    return connection

@contextmanager
def transaction(path):
    connection = connect(path)
    try:
        connection.execute("BEGIN IMMEDIATE")
        yield connection
        connection.commit()
    except BaseException:
        connection.rollback()
        raise
    finally:
        connection.close()

def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    )

def positive_cents(value):
    if type(value) is not int or value <= 0:
        raise ValueError("Expected a positive integer amount in cents")
    return value

def initialize(path):
    connection = connect(path)
    try:
        connection.execute("PRAGMA journal_mode = WAL")
        connection.executescript("""
CREATE TABLE IF NOT EXISTS parcel (
    id INTEGER PRIMARY KEY,
    county TEXT NOT NULL,
    apn TEXT NOT NULL,
    UNIQUE(county, apn)
);
CREATE TABLE IF NOT EXISTS lead (
    id INTEGER PRIMARY KEY,
    parcel_id INTEGER NOT NULL REFERENCES parcel(id),
    source TEXT NOT NULL,
    external_id TEXT NOT NULL,
    payload TEXT NOT NULL,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    UNIQUE(source, external_id)
);
CREATE TABLE IF NOT EXISTS deal (
    id INTEGER PRIMARY KEY,
    parcel_id INTEGER NOT NULL UNIQUE REFERENCES parcel(id),
    state TEXT NOT NULL DEFAULT 'intake'
        CHECK(state IN (
            'intake', 'verified', 'escrow',
            'acquired', 'listed', 'sold'
        ))
);
CREATE TABLE IF NOT EXISTS evidence (
    id INTEGER PRIMARY KEY,
    deal_id INTEGER NOT NULL REFERENCES deal(id),
    kind TEXT NOT NULL,
    uri TEXT NOT NULL,
    digest TEXT NOT NULL,
    reviewer TEXT NOT NULL,
    passed INTEGER NOT NULL CHECK(passed IN (0, 1)),
    expires INTEGER NOT NULL,
    recorded INTEGER NOT NULL,
    UNIQUE(deal_id, kind, digest, reviewer, passed, expires)
);
CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY,
    source TEXT NOT NULL,
    external_id TEXT NOT NULL,
    deal_id INTEGER REFERENCES deal(id),
    kind TEXT NOT NULL,
    payload TEXT NOT NULL,
    recorded INTEGER NOT NULL,
    UNIQUE(source, external_id)
);
CREATE TABLE IF NOT EXISTS journal (
    event_id INTEGER NOT NULL REFERENCES event(id),
    line INTEGER NOT NULL,
    account TEXT NOT NULL CHECK(account IN (
        'cash', 'inventory', 'cogs', 'revenue', 'expense'
    )),
    cents INTEGER NOT NULL CHECK(cents <> 0),
    bank_ref TEXT,
    UNIQUE(event_id, line),
    CHECK(
        (account = 'cash' AND bank_ref IS NOT NULL)
        OR (account <> 'cash' AND bank_ref IS NULL)
    )
);
CREATE UNIQUE INDEX IF NOT EXISTS one_cash_post_per_bank_reference
    ON journal(bank_ref) WHERE account = 'cash';
CREATE TABLE IF NOT EXISTS bank (
    bank_ref TEXT PRIMARY KEY,
    cents INTEGER NOT NULL CHECK(cents <> 0),
    booked_date TEXT NOT NULL,
    statement_uri TEXT NOT NULL
);
""")
        for table in ("evidence", "event", "journal", "bank"):
            for operation in ("UPDATE", "DELETE"):
                name = table + "_block_" + operation.lower()
                sql = (
                    "CREATE TRIGGER IF NOT EXISTS " + name
                    + " BEFORE " + operation + " ON " + table
                    + " BEGIN SELECT RAISE(ABORT, "
                    + "'Append-only audit records'); END;"
                )
                connection.execute(sql)
    finally:
        connection.close()
''',
                        "Initialize once before workers start; use integer cents and county-canonical parcel identifiers.",
                        "Unique constraints and immediate transactions serialize local writes; immutable audit rows reject mutation.",
                    ],
                    [
                        "Module two deduplicates source intake and calculates transparent screening priorities.",
                        r'''def intake(path, source, external_id, county, apn, facts):
    identity = [source, external_id, county, apn]
    if any(not isinstance(value, str) or not value.strip()
           for value in identity):
        raise ValueError("Every source and parcel identity must be populated")
    county, apn = county.strip(), apn.strip()
    for field in ("access_documented", "zoning_fit", "environmental_clear"):
        if type(facts[field]) is not bool:
            raise ValueError("Screening flags must be explicit booleans")
    comps = facts["sold_comps"]
    if type(comps) is not int or comps < 0:
        raise ValueError("Closed comparable count must be a nonnegative integer")
    payload = canonical({
        "county": county, "apn": apn, "facts": facts
    })
    score = (
        30 * int(facts["access_documented"])
        + 25 * int(facts["zoning_fit"])
        + 5 * min(comps, 5)
        + 20 * int(facts["environmental_clear"])
    )
    with transaction(path) as connection:
        previous = connection.execute(
            "SELECT parcel_id, payload FROM lead "
            "WHERE source = ? AND external_id = ?",
            (source, external_id),
        ).fetchone()
        if previous:
            if previous["payload"] != payload:
                raise ValueError("Intake identifier reused with different content")
            return connection.execute(
                "SELECT id FROM deal WHERE parcel_id = ?",
                (previous["parcel_id"],),
            ).fetchone()["id"]
        connection.execute(
            "INSERT INTO parcel(county, apn) VALUES (?, ?) "
            "ON CONFLICT(county, apn) DO NOTHING",
            (county, apn),
        )
        parcel_id = connection.execute(
            "SELECT id FROM parcel WHERE county = ? AND apn = ?",
            (county, apn),
        ).fetchone()["id"]
        connection.execute(
            "INSERT INTO lead(parcel_id, source, external_id, payload, score) "
            "VALUES (?, ?, ?, ?, ?)",
            (parcel_id, source, external_id, payload, score),
        )
        connection.execute(
            "INSERT INTO deal(parcel_id) VALUES (?) "
            "ON CONFLICT(parcel_id) DO NOTHING",
            (parcel_id,),
        )
        return connection.execute(
            "SELECT id FROM deal WHERE parcel_id = ?", (parcel_id,)
        ).fetchone()["id"]
''',
                        "Canonicalize parcel formatting in the county adapter; preserve leading zeros and source lineage.",
                        "Concurrent duplicate leads converge on one parcel and deal without overwriting prior source content.",
                    ],
                    [
                        "Module three records attributed evidence and validates the latest review snapshot.",
                        r'''BASE_EVIDENCE = ("title", "access", "zoning", "environment", "valuation")
REQUIREMENTS = {
    "verified": BASE_EVIDENCE,
    "escrow": BASE_EVIDENCE + ("escrow_instructions",),
    "acquired": BASE_EVIDENCE + (
        "escrow_instructions", "purchase_settlement"
    ),
    "listed": BASE_EVIDENCE + (
        "purchase_settlement", "disclosures"
    ),
    "sold": BASE_EVIDENCE + (
        "purchase_settlement", "disclosures",
        "sale_settlement", "title_coverage"
    ),
}
NEXT_STATE = {
    "intake": "verified",
    "verified": "escrow",
    "escrow": "acquired",
    "acquired": "listed",
    "listed": "sold",
}

def record_evidence(path, deal_id, kind, uri, digest,
                    reviewer, passed, expires):
    allowed = set()
    for required in REQUIREMENTS.values():
        allowed.update(required)
    if kind not in allowed:
        raise ValueError("Evidence category is outside the review contract")
    if not uri or not reviewer:
        raise ValueError("Document location and reviewer are required")
    if (len(digest) != 64
            or any(char not in "0123456789abcdef" for char in digest)):
        raise ValueError("Evidence requires a lowercase SHA-256 digest")
    if type(passed) is not bool:
        raise ValueError("Review verdict must be an explicit boolean")
    if type(expires) is not int or expires <= int(time.time()):
        raise ValueError("Evidence expiration must be a future epoch second")
    values = (
        deal_id, kind, uri, digest, reviewer, int(passed), expires
    )
    with transaction(path) as connection:
        connection.execute(
            "INSERT INTO evidence(deal_id, kind, uri, digest, reviewer, "
            "passed, expires, recorded) VALUES (?, ?, ?, ?, ?, ?, ?, ?) "
            "ON CONFLICT(deal_id, kind, digest, reviewer, passed, expires) "
            "DO NOTHING",
            values + (int(time.time()),),
        )
        row = connection.execute(
            "SELECT id, uri FROM evidence WHERE deal_id = ? AND kind = ? "
            "AND digest = ? AND reviewer = ? AND passed = ? AND expires = ?",
            (deal_id, kind, digest, reviewer, int(passed), expires),
        ).fetchone()
        if row["uri"] != uri:
            raise ValueError("Evidence identity reused with another location")
        return row["id"]

def evidence_snapshot(connection, deal_id, target):
    accepted = []
    now = int(time.time())
    for kind in REQUIREMENTS[target]:
        row = connection.execute(
            "SELECT id, passed, expires FROM evidence "
            "WHERE deal_id = ? AND kind = ? ORDER BY id DESC LIMIT 1",
            (deal_id, kind),
        ).fetchone()
        if not row or not row["passed"] or row["expires"] <= now:
            raise ValueError("Required evidence failed: " + kind)
        accepted.append(row["id"])
    return accepted
''',
                        "Authenticated internal reviewers inspect actual instruments; stored digests identify the exact reviewed versions.",
                        "Evidence selection occurs inside the advancing write transaction; later revisions cannot alter its historical snapshot.",
                    ],
                    [
                        "Module four advances escrow states and posts balanced, replay-safe accounting events.",
                        r'''def prior_event(connection, source, external_id, payload):
    row = connection.execute(
        "SELECT id, payload FROM event WHERE source = ? AND external_id = ?",
        (source, external_id),
    ).fetchone()
    if row and row["payload"] != payload:
        raise ValueError("Event identifier reused with different content")
    return row["id"] if row else None

def write_event(connection, source, external_id, deal_id,
                kind, payload, lines):
    if not source or not external_id:
        raise ValueError("Stable event source and identifier are required")
    if sum(line[1] for line in lines) != 0:
        raise ValueError("Journal event does not balance")
    cursor = connection.execute(
        "INSERT INTO event(source, external_id, deal_id, kind, payload, recorded) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (source, external_id, deal_id, kind, payload, int(time.time())),
    )
    event_id = cursor.lastrowid
    for number, (account, cents, bank_ref) in enumerate(lines, 1):
        connection.execute(
            "INSERT INTO journal(event_id, line, account, cents, bank_ref) "
            "VALUES (?, ?, ?, ?, ?)",
            (event_id, number, account, cents, bank_ref),
        )
    return event_id

def advance(path, source, external_id, deal_id, expected, target, data):
    request = canonical({
        "kind": "transition", "deal": deal_id,
        "expected": expected, "target": target, "data": data
    })
    with transaction(path) as connection:
        prior = prior_event(connection, source, external_id, request)
        if prior is not None:
            return prior
        row = connection.execute(
            "SELECT state FROM deal WHERE id = ?", (deal_id,)
        ).fetchone()
        if not row or row["state"] != expected:
            raise ValueError("Deal state differs from expected state")
        if NEXT_STATE.get(expected) != target:
            raise ValueError("Transition is outside the allowed sequence")
        evidence_ids = evidence_snapshot(connection, deal_id, target)
        if data.get("evidence_ids") != evidence_ids:
            raise ValueError("Caller must bind the current ordered evidence identifiers")
        lines = []
        if target == "acquired":
            amount = positive_cents(data["purchase_cents"])
            reference = data["bank_ref"]
            if not isinstance(reference, str) or not reference.strip():
                raise ValueError("Confirmed purchase requires a bank reference")
            lines = [
                ("inventory", amount, None),
                ("cash", -amount, reference),
            ]
        elif target == "sold":
            gross = positive_cents(data["gross_cents"])
            costs = data["selling_costs_cents"]
            if type(costs) is not int or not 0 <= costs < gross:
                raise ValueError("Selling costs must be nonnegative and below proceeds")
            reference = data["bank_ref"]
            if not isinstance(reference, str) or not reference.strip():
                raise ValueError("Confirmed sale requires a bank reference")
            basis = connection.execute(
                "SELECT COALESCE(SUM(j.cents), 0) AS basis "
                "FROM journal j JOIN event e ON e.id = j.event_id "
                "WHERE e.deal_id = ? AND j.account = 'inventory'",
                (deal_id,),
            ).fetchone()["basis"]
            positive_cents(basis)
            lines = [
                ("cash", gross - costs, reference),
                ("revenue", -gross, None),
                ("cogs", basis, None),
                ("inventory", -basis, None),
            ]
            if costs:
                lines.append(("expense", costs, None))
        event_id = write_event(
            connection, source, external_id, deal_id, target, request, lines
        )
        connection.execute(
            "UPDATE deal SET state = ? WHERE id = ? AND state = ?",
            (target, deal_id, expected),
        )
        return event_id

def post_opex(path, source, external_id, cents, bank_ref, description):
    positive_cents(cents)
    if not bank_ref or not description:
        raise ValueError("Expense requires a bank reference and description")
    payload = canonical({
        "kind": "opex", "cents": cents,
        "bank_ref": bank_ref, "description": description
    })
    with transaction(path) as connection:
        prior = prior_event(connection, source, external_id, payload)
        if prior is not None:
            return prior
        return write_event(
            connection, source, external_id, None, "opex", payload,
            [("expense", cents, None), ("cash", -cents, bank_ref)],
        )

def current_evidence_ids(path, deal_id, target):
    with transaction(path) as connection:
        return evidence_snapshot(connection, deal_id, target)
''',
                        "Record externally confirmed cash closings only; fetch evidence identifiers and retry stale requests after review.",
                        "Posting, evidence binding, and state advancement commit together; repeated payment references cannot create second cash entries.",
                    ],
                    [
                        "Module five imports statement evidence and exposes a complete cash reconciliation view.",
                        r'''def initialize_reconciliation(path):
    with transaction(path) as connection:
        connection.execute("""
CREATE VIEW IF NOT EXISTS cash_reconciliation AS
WITH ledger AS (
    SELECT bank_ref, SUM(cents) AS ledger_cents
    FROM journal WHERE account = 'cash'
    GROUP BY bank_ref
), references_all AS (
    SELECT bank_ref FROM ledger
    UNION
    SELECT bank_ref FROM bank
)
SELECT r.bank_ref,
       l.ledger_cents,
       b.cents AS bank_cents,
       COALESCE(l.ledger_cents, 0) - COALESCE(b.cents, 0)
           AS difference_cents,
       CASE
           WHEN l.bank_ref IS NULL THEN 'bank entry awaits ledger posting'
           WHEN b.bank_ref IS NULL THEN 'ledger entry awaits statement evidence'
           WHEN l.ledger_cents = b.cents THEN 'matched amount and immutable reference'
           ELSE 'amount difference requires settlement investigation'
       END AS status
FROM references_all r
LEFT JOIN ledger l ON l.bank_ref = r.bank_ref
LEFT JOIN bank b ON b.bank_ref = r.bank_ref
""")

def import_bank(path, bank_ref, cents, booked_date, statement_uri):
    if type(cents) is not int or cents == 0:
        raise ValueError("Bank amount must be a nonzero integer in cents")
    if not bank_ref or not booked_date or not statement_uri:
        raise ValueError("Statement identity, date, and source are required")
    with transaction(path) as connection:
        row = connection.execute(
            "SELECT cents, booked_date, statement_uri FROM bank WHERE bank_ref = ?",
            (bank_ref,),
        ).fetchone()
        values = (cents, booked_date, statement_uri)
        if row:
            if tuple(row) != values:
                raise ValueError("Bank identity reused with different statement content")
            return
        connection.execute(
            "INSERT INTO bank(bank_ref, cents, booked_date, statement_uri) "
            "VALUES (?, ?, ?, ?)",
            (bank_ref,) + values,
        )

def reconciliation(path):
    connection = connect(path)
    try:
        return [
            dict(row) for row in connection.execute(
                "SELECT * FROM cash_reconciliation ORDER BY bank_ref"
            )
        ]
    finally:
        connection.close()
''',
                        "Namespace bank references by institution, account, and transaction identifier; import complete operating statement coverage.",
                        "Repeated statement imports are harmless; mismatched amounts and absent counterpart entries remain visible.",
                    ],
                    [
                        "Module six checks integrity and exercises duplicate handling and transaction rollback.",
                        r'''def qa(path, require_statement_match=False):
    connection = connect(path)
    try:
        if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise AssertionError("SQLite integrity check failed")
        if connection.execute("PRAGMA foreign_key_check").fetchall():
            raise AssertionError("Foreign key check failed")
        unbalanced = connection.execute(
            "SELECT event_id FROM journal GROUP BY event_id "
            "HAVING SUM(cents) <> 0"
        ).fetchall()
        if unbalanced:
            raise AssertionError("Unbalanced journal events exist")
        missing = connection.execute(
            "SELECT e.id FROM event e LEFT JOIN journal j ON j.event_id = e.id "
            "WHERE e.kind IN ('acquired', 'sold', 'opex') "
            "GROUP BY e.id HAVING COUNT(j.line) = 0"
        ).fetchall()
        if missing:
            raise AssertionError("Cash events are missing journal lines")
        bad_inventory = connection.execute("""
SELECT d.id
FROM deal d
LEFT JOIN event e ON e.deal_id = d.id
LEFT JOIN journal j ON j.event_id = e.id
GROUP BY d.id, d.state
HAVING
    (d.state IN ('acquired', 'listed')
     AND COALESCE(SUM(CASE WHEN j.account = 'inventory'
                          THEN j.cents ELSE 0 END), 0) <= 0)
 OR (d.state NOT IN ('acquired', 'listed')
     AND COALESCE(SUM(CASE WHEN j.account = 'inventory'
                          THEN j.cents ELSE 0 END), 0) <> 0)
""").fetchall()
        if bad_inventory:
            raise AssertionError("Inventory does not match parcel custody state")
        rows = [
            dict(row) for row in connection.execute(
                "SELECT * FROM cash_reconciliation "
                "WHERE ledger_cents IS NULL OR bank_cents IS NULL "
                "OR difference_cents <> 0"
            )
        ]
        if require_statement_match and rows:
            raise AssertionError("Statement reconciliation remains incomplete")
        return rows
    finally:
        connection.close()

def self_test():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "reference-test.sqlite"
        initialize(path)
        initialize_reconciliation(path)
        facts = {
            "access_documented": True,
            "zoning_fit": True,
            "sold_comps": 4,
            "environmental_clear": True,
        }
        deal_id = intake(path, "county-export", "lead-1", "06037", "000123", facts)
        assert intake(
            path, "county-export", "lead-1", "06037", "000123", facts
        ) == deal_id
        try:
            advance(path, "escrow", "premature-1", deal_id,
                    "intake", "verified", {"evidence_ids": []})
        except ValueError:
            pass
        else:
            raise AssertionError("Missing evidence unexpectedly advanced a deal")
        try:
            with transaction(path) as connection:
                connection.execute(
                    "INSERT INTO event(source, external_id, kind, payload, recorded) "
                    "VALUES ('test', 'rollback-1', 'probe', '{}', 0)"
                )
                raise RuntimeError("Deliberate rollback probe")
        except RuntimeError:
            pass
        with transaction(path) as connection:
            assert connection.execute(
                "SELECT COUNT(*) FROM event"
            ).fetchone()[0] == 0
        first = post_opex(
            path, "bookkeeper", "expense-1", 600000,
            "bank:operating:001", "Monthly operating expense"
        )
        assert post_opex(
            path, "bookkeeper", "expense-1", 600000,
            "bank:operating:001", "Monthly operating expense"
        ) == first
        try:
            post_opex(
                path, "bookkeeper", "expense-1", 600001,
                "bank:operating:001", "Monthly operating expense"
            )
        except ValueError:
            pass
        else:
            raise AssertionError("Changed replay unexpectedly succeeded")
        import_bank(
            path, "bank:operating:001", -600000,
            "2026-01-31", "local:statements/january.pdf"
        )
        assert qa(path, require_statement_match=True) == []
    return "Isolated intake, evidence, rollback, replay, and bank checks passed"
''',
                        "Run self_test separately, then run qa against the operating database after each statement close.",
                        "Checks reject orphaned inventory and unbalanced postings; isolated tests never modify the operating database.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Initialize and test the isolated reference",
                    "action": "Assemble the six code cells in order and call self_test before loading operating records.",
                    "detail": "Use a local SQLite database, restrictive filesystem permissions, and a tested backup process; initialize schema before concurrent workers start.",
                },
                {
                    "step": 2,
                    "title": "Bind reviewed evidence to each transition",
                    "action": "Record attributed document reviews, fetch current_evidence_ids, and include that ordered list in the transition data.",
                    "detail": "A concurrent replacement review causes a stale evidence list to fail; inspect the replacement instead of automatically accepting it.",
                },
                {
                    "step": 3,
                    "title": "Record completed escrow results exactly once",
                    "action": "Advance acquired or sold only after the external closing is confirmed, using a stable event identifier and statement-matchable bank reference.",
                    "detail": "An acquired request supplies purchase_cents; a sold request supplies gross_cents and selling_costs_cents; both include bank_ref and evidence_ids.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and close the statement period",
                    "action": "Import complete operating cash movements, inspect reconciliation, and run qa with require_statement_match enabled.",
                    "detail": "The reference tracks operating cash deltas; maintain the independently evidenced opening cash balance and extend accounts before posting capital contributions or debt.",
                },
            ],
        },
        {
            "heading": "3. Worked 90-Day Cohort Walk: distinguish profit, inventory, and cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Read this walk as a prepared operating cohort, not a promise that a new "
                    "operator closes inside ninety days. The canonical time to first deal remains "
                    "three to twelve months. County selection, contractor onboarding, buyer discovery, "
                    "and seller conversations begin before day one; acquisition-ready opportunities "
                    "enter the illustrated quarter. Opening unrestricted cash is $150,000, within "
                    "the $50,000 to $400,000 startup range, and opening parcel inventory is zero. "
                    "Each monthly lead cohort contains 120 researched records: ninety fail desktop "
                    "screening, twenty of the thirty survivors fail contact-stage qualification, "
                    "seven of the remaining ten fail offer underwriting, and two of three offers "
                    "do not close. One parcel is acquired per month for $70,000. These nested "
                    "counts reconcile to 119 non-acquisitions and one acquisition, not 119 paid "
                    "diligence reports. Budget $600 of each month's $6,000 operating expense for "
                    "unsuccessful research and diligence; the other $5,400 supports sourcing, "
                    "contractor retainers, systems, and administration. No earnest money is "
                    "forfeited and no parcel is written down in this example. Those zero realized "
                    "losses are explicit scenario assumptions, while the screening losses and "
                    "research expense remain visible."
                ),
                (
                    "Month one acquires parcel A for $70,000 and pays $6,000 operating expense, "
                    "creating a $76,000 cash outflow and $74,000 ending cash. There is no sale, "
                    "so the month reports a $6,000 operating loss and $70,000 inventory. Month "
                    "two acquires parcel B for $70,000 and sells A for $106,250 gross. Escrow "
                    "deducts $7,593.75 of selling and holding charges, remitting $98,656.25 to "
                    "the operating bank account. Releasing A's $70,000 basis and charging "
                    "$6,000 operating expense produces $22,656.25 owner profit. Because the "
                    "replacement purchase equals the released basis, monthly cash also rises "
                    "$22,656.25. Month three repeats those amounts: parcel C is acquired, B "
                    "sells, and C remains inventory awaiting a later buyer. Ending cash is "
                    "$119,312.50, not $189,312.50; the difference is capital still invested in C. "
                    "The quarter's $39,312.50 profit reconciles to a $30,687.50 cash decline "
                    "after the $70,000 inventory increase. There are no receivables, payables, "
                    "borrowings, owner distributions, or other working-capital movements in this "
                    "walk. An operator adding any of them must extend the bridge rather than "
                    "reuse its final cash figure."
                ),
                (
                    "Annualize the quarter's two completed sales, not its three acquisition checks. "
                    "Four equivalent earnings quarters generate eight sales totaling $850,000, "
                    "$560,000 released acquisition basis, $60,750 selling and holding expense, "
                    "and $72,000 operating expense. The residual is exactly $157,250, or "
                    "18.5% of gross parcel sale proceeds. After the initial inventory build, "
                    "each later quarter purchases two replacement parcels and sells two parcels; "
                    "it does not keep buying three while presenting unchanged working capital. "
                    "Across the first year, nine purchases cost $630,000, eight parcels sell, "
                    "and one $70,000 parcel remains. Operating cash increases $87,250, taking "
                    "the initial $150,000 to $237,250 before distributions. The first quarter's "
                    "inventory build explains why cash generation trails owner profit. The "
                    "Conservative case remains $200,000 revenue at 12%, yielding $24,000; "
                    "the Scaled case remains $1,500,000 at 25%, yielding $375,000 with two "
                    "full-time staff and four contractors. Neither case is created by multiplying "
                    "the example's lead counts. Test slower exits separately: another quarter "
                    "holding C delays its cash release and adds actual carrying costs. A "
                    "stale parcel cannot be counted as a completed sale merely to preserve "
                    "the annual target."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and deal or lead cohort",
                    "Gross proceeds, basis, and recognized owner result",
                    "Cash timing, expense, and explicit scrubs",
                    "Cumulative cash and inventory reconciliation",
                ],
                "rows": [
                    [
                        "Month 1 researches 120 leads and acquires parcel A; 119 records do not become purchases.",
                        "Gross proceeds equal $0; released basis equals $0; operating loss equals $6,000.",
                        "Pay $70,000 acquisition and $6,000 opex, including $600 failed diligence; realized forfeitures equal $0.",
                        "Monthly cash flow is negative $76,000; cumulative flow is negative $76,000; cash equals $74,000; inventory equals $70,000.",
                    ],
                    [
                        "Month 2 researches 120 new leads, acquires parcel B, and completes parcel A's disposition.",
                        "Gross proceeds equal $106,250; basis equals $70,000; sale charges equal $7,593.75; owner profit equals $22,656.25.",
                        "Collect $98,656.25 net settlement; pay $70,000 acquisition and $6,000 opex; 119 leads produce no acquisition.",
                        "Monthly cash flow equals $22,656.25; cumulative flow is negative $53,343.75; cash equals $96,656.25; inventory equals $70,000.",
                    ],
                    [
                        "Month 3 researches 120 new leads, acquires parcel C, and completes parcel B's disposition.",
                        "Gross proceeds equal $106,250; basis equals $70,000; sale charges equal $7,593.75; owner profit equals $22,656.25.",
                        "Collect $98,656.25 net settlement; pay $70,000 acquisition and $6,000 opex; parcel C remains unsold.",
                        "Monthly cash flow equals $22,656.25; cumulative flow is negative $30,687.50; cash equals $119,312.50; inventory equals $70,000.",
                    ],
                    [
                        "Quarter total covers 360 researched leads, three acquisitions, two dispositions, and 357 non-acquisitions.",
                        "Revenue $212,500 minus basis $140,000 minus sale charges $15,187.50 minus opex $18,000 equals $39,312.50 profit.",
                        "Acquisition cash totals $210,000; opex includes $1,800 unsuccessful diligence; principal write-downs and forfeitures remain zero.",
                        "Profit $39,312.50 less inventory increase $70,000 equals negative $30,687.50 cash flow before distributions.",
                    ],
                    [
                        "Base annual bridge uses eight dispositions and nine acquisitions, retaining one parcel at year end.",
                        "Revenue $850,000 minus basis $560,000 minus sale charges $60,750 minus opex $72,000 equals $157,250 profit.",
                        "Cash purchases total $630,000; later quarters replace two sold parcels each rather than building additional inventory.",
                        "Annual cash increase equals $87,250; ending cash equals $237,250; ending inventory equals $70,000; margin equals 18.5%.",
                    ],
                    [
                        "Inventory custody bridge follows parcel A into Month 2, parcel B into Month 3, and parcel C beyond day ninety.",
                        "Only A and B contribute quarterly sale revenue; C contributes no recognized proceeds or released basis.",
                        "No debt, seller notes, receivables, payable balances, or owner distributions alter this illustrated cash bridge.",
                        "Opening cash $150,000 plus quarterly cash change negative $30,687.50 reconciles exactly to closing cash $119,312.50.",
                    ],
                ],
            },
        },
        {
            "heading": "4. Close the evidence loop before recycling acquisition capital",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Before entering escrow, compare the executed purchase agreement with the title "
                    "commitment's vesting, legal description, exceptions, and required instruments. "
                    "A clean-looking ownership record does not resolve tax liens, probate "
                    "authority, boundary encroachments, mineral reservations, or access exclusions. "
                    "Ask the title provider which exceptions remain after closing and whether "
                    "available endorsements address the actual insured risk. Title insurance "
                    "does not establish zoning compliance or physical buildability. Where fixtures "
                    "or recorded secured interests are implicated, obtain a targeted search and "
                    "review under the applicable state's enacted UCC provisions; UCC 9-501 "
                    "illustrates the recording-office distinction for fixture filings. Do not "
                    "treat every vacant parcel as requiring a generic personal-property filing "
                    "search. Confirm seller identity and signing authority through the escrow "
                    "provider's procedures, independently verify changed wire instructions using "
                    "an established telephone number, and preserve the signed settlement "
                    "statement. State-specific disclosure duties survive an attractive resale "
                    "spread. When representing another owner rather than selling owned inventory, "
                    "review the relevant broker licensing provisions; California Business and "
                    "Professions Code sections 10130 and 10131 provide a concrete example. "
                    "The operator's entity, contractor scopes, marketing claims, and actual "
                    "activities must agree."
                ),
                (
                    "Run a weekly exception meeting from the evidence queue rather than a slideshow "
                    "of acquisition targets. Review parcels whose latest access, title, zoning, "
                    "or environmental evidence failed; contracts nearing diligence deadlines; "
                    "aged inventory without current buyer feedback; and cash events lacking "
                    "statement support. Assign each exception one owner, a next action, and "
                    "an explicit deadline. The GIS contractor can refresh comparable sales "
                    "and flag changed parcel boundaries, but cannot resolve a disputed easement "
                    "by changing a score. The survey specialist can quantify an encroachment, "
                    "but the owner must decide whether the revised economics still support "
                    "the offer. The title provider can document a curative requirement, but "
                    "cash should not leave merely because a checklist contains a green "
                    "cell. Preserve adverse evidence alongside subsequent cures. If an access "
                    "instrument changes, record the new document and reopen the relevant "
                    "review before further advancement. Stop new acquisitions when cash "
                    "needed for committed closings, expected carrying costs, and the chosen "
                    "operating reserve exceeds unrestricted funds. The example's $74,000 "
                    "first-month cash trough is observable liquidity, not automatically "
                    "available buying power. Commitments outside the ledger still consume "
                    "real capacity and belong in the weekly capital schedule."
                ),
                (
                    "At period close, reconcile three independent views: parcel custody, settlement "
                    "documents, and bank cash. Every acquired parcel must have one identifiable "
                    "inventory balance and a recorded ownership package; every disposed parcel "
                    "must have gross proceeds, released basis, selling expense, and a matching "
                    "net receipt. Inspect the entire bank statement, not only transactions "
                    "already exported by the application. Compare opening bank balance plus "
                    "all statement movements with closing bank balance, then classify any "
                    "capital contribution, distribution, loan, refund, or transfer outside "
                    "the reference handlers. Back up SQLite using its backup API while "
                    "the database is live, retain document versions separately, and test "
                    "restoration into an isolated location. A copied database file without "
                    "its active WAL can omit committed work. Recompute the scorecard "
                    "bridge from posted amounts rather than copying last month's dashboard. "
                    "Track acquisition-to-sale days, cash tied up by parcel, realized "
                    "spread after expenses, and reasons for rejected offers. Increase "
                    "volume only when those controls remain current within the four-person "
                    "Base pod. Moving to the six-person Scaled team is an explicit "
                    "capacity change with different economics, not permission to book "
                    "unclosed transactions or ignore evidence that makes a parcel harder "
                    "to sell."
                ),
            ],
            "table": {
                "caption": "Closing, Exception, and Recovery Controls for a Title-Insured Land Pod",
                "headers": [
                    "Control and review cadence",
                    "Evidence inspected by the accountable operator",
                    "Failure response and preserved audit trail",
                    "Ledger or capital consequence before further commitments",
                ],
                "rows": [
                    [
                        "Recorded access review occurs before purchase and after any material instrument change.",
                        "Title provider compares easement description, benefited parcel, permitted use, and public-road connection.",
                        "Block advancement and commission targeted review when physical access exceeds recorded rights.",
                        "Exclude speculative access value from the offer and preserve funds for verified opportunities.",
                    ],
                    [
                        "Buildability and environmental review precedes any representation of a usable building envelope.",
                        "Land-use specialist checks zoning, setbacks, utility conditions, flood information, and site history.",
                        "Revise buyer materials and price assumptions when restrictions reduce the plausible use.",
                        "Record actual investigation expense and reassess carrying exposure before committing acquisition cash.",
                    ],
                    [
                        "Escrow instruction verification occurs before each outward payment through independent communication.",
                        "Owner confirms established contact details, beneficiary instructions, settlement terms, and signing authority.",
                        "Pause the external payment when instructions change without independent confirmation and retain communications.",
                        "Post acquisition cash only after the externally completed transaction has documented support.",
                    ],
                    [
                        "Weekly inventory aging review follows every acquired parcel until a completed sale.",
                        "Owner compares acquisition date, current buyer feedback, carrying bills, and realistic exit value.",
                        "Choose documented repricing, additional investigation, or a revised hold plan with assigned deadlines.",
                        "Reduce available acquisition capacity by committed closing funds and expected holding expenditure.",
                    ],
                    [
                        "Monthly bank reconciliation connects the complete statement with immutable cash event references.",
                        "Owner compares bank-only entries, ledger-only entries, net settlement receipts, and statement balance movement.",
                        "Investigate differences individually; never edit historical entries merely to force matching totals.",
                        "Use an explicitly designed correcting-event extension for errors before treating the period as closed.",
                    ],
                    [
                        "Periodic restoration testing verifies recoverable accounting records and linked document versions.",
                        "Operator restores a backup into isolation and checks journal integrity, evidence references, and balances.",
                        "Resolve missing files or inconsistent snapshots before relying on the backup for recovery.",
                        "Suspend new workflow writes during incident recovery until the restored baseline is reconciled.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before acquisition capital moves",
                "body": "The owner signs off on evidence and liquidity; a screening score cannot substitute for any check.",
                "items": [
                    "Verify seller authority, the insured legal description, recorded access, and the title exceptions that will remain after closing.",
                    "Verify the priced use against zoning, dimensions, utility conditions, environmental findings, and any required subdivision procedure.",
                    "Verify the settlement amount and wire instructions independently, then reserve cash for committed closings and the chosen operating runway.",
                    "Verify stable event identifiers, current evidence versions, integer-cent postings, and an available statement reference before recording the completed purchase.",
                ],
            },
        },
    ],
    "pull_quote": "A parcel becomes profit only when verified rights become a completed sale and the settlement becomes reconciled cash.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Select one county and buyer profile, then preserve dated QGIS layers, parcel identifiers, and explicit exclusion reasons.",
        "Assign the owner, GIS analyst, title and escrow provider, and survey or land-use specialist to written scopes within the Base expense budget.",
        "Assemble the six reference modules, run the isolated checks, and bind reviewed evidence identifiers to every state transition.",
        "Fund the illustrated cohort only after modeling the $74,000 first-month cash trough and all commitments outside the reference ledger.",
        "Reconcile quarterly revenue of $212,500 and owner profit of $39,312.50 to the $70,000 inventory increase and negative $30,687.50 cash change.",
        "Close each statement period with parcel custody, settlement documents, bank references, tested backups, and the exact annual Base profit bridge.",
    ],
    "statutory_citations": [
        {
            "title": "California Government Code section 66424 — Definition of subdivision",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=66424.&lawCode=GOV",
            "relevance": "Defines subdivision for California's map framework; use the applicable jurisdiction's rules before treating proposed parcel divisions as saleable lots.",
        },
        {
            "title": "California Government Code section 66426 — Tentative and final map requirements",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=66426.&lawCode=GOV",
            "relevance": "Establishes map requirements and exceptions relevant to California subdivision planning, review scope, and timing.",
        },
        {
            "title": "42 U.S.C. 9601(40) — Bona fide prospective purchaser",
            "url": "https://www.law.cornell.edu/uscode/text/42/9601",
            "relevance": "Sets conditions associated with purchaser status under CERCLA, including inquiry and continuing-obligation considerations that affect acquisition diligence.",
        },
        {
            "title": "40 CFR Part 312 — Innocent Landowners, Standards for Conducting All Appropriate Inquiries",
            "url": "https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
            "relevance": "Provides inquiry standards and timing requirements when the acquisition strategy relies on qualifying environmental investigation.",
        },
        {
            "title": "33 U.S.C. 1344 — Permits for dredged or fill material",
            "url": "https://www.law.cornell.edu/uscode/text/33/1344",
            "relevance": "Governs section 404 permitting for covered discharges; evaluate jurisdiction and required permits before assuming constrained land can be filled.",
        },
        {
            "title": "California Business and Professions Code section 10130 — Real estate license requirement",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=10130.&lawCode=BPC",
            "relevance": "Requires licensing for covered California brokerage activity; distinguish owned-inventory transactions from representing other owners.",
        },
        {
            "title": "California Business and Professions Code section 10131 — Real estate broker activities",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=10131.&lawCode=BPC",
            "relevance": "Defines covered activities performed for another for compensation, informing contractor scopes and representation boundaries.",
        },
        {
            "title": "UCC section 9-501 — Filing office",
            "url": "https://www.law.cornell.edu/ucc/9/9-501",
            "relevance": "Identifies model filing-office rules, including real-property recording for certain fixture filings; confirm the applicable state's enacted text for the parcel review.",
        },
    ],
}
