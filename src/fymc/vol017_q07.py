from __future__ import annotations

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "domain-investing-complete-operating-process-production-blueprint",
    "question_prompt": "How does an operator execute domain investing end-to-end from intake to reconciled cash, backed by an auditable technical/ledger blueprint and a worked 90-day cohort walk?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process, Production Blueprint & 90-Day Cohort Walk",
    "subtitle": "Acquisition Screens, Registrar Transfers, Escrow Evidence, SQLite Journals, UDRP Controls & a Cash-Reconciled Domain Cohort",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #16, Domain Investing, ranks #22 with a 83/100 Money-to-Manpower Score. "
        "This chapter converts eight mapped plays into a controlled acquisition, verification, "
        "sale, transfer, and reconciliation process. Seven domain operating plays cover brandables, "
        "exact-match names, expired assets, drop-catching, upgrades, inbound conversion, and renewal "
        "recycling; the supplied search-feed arbitrage play receives a separate economic boundary. "
        "A six-module SQLite reference makes duplicate events harmless, serializes competing writes, "
        "and separates sale proceeds from escrow balances and inventory purchases. The worked "
        "90-day cohort produces $40,000 gross sales, $11,000 operating profit, and $8,000 cash growth "
        "before opening capital. Annual owner profit remains exactly $3,000 Conservative, $44,000 Base, "
        "and $120,000 Scaled; cohort timing is illustrative, not evidence of immediate liquidity."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$20,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "15% net margin; $3,000 annual owner net profit; 1 FT + 1 C",
        },
        {
            "label": "Base",
            "value": "$160,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "27.5% net margin; $44,000 annual owner net profit; 1 FT + 1 C",
        },
        {
            "label": "Scaled",
            "value": "$300,000",
            "context": "Annual gross domain sale proceeds; acquisition and renewal costs included in margin",
            "note": "40% net margin; $120,000 annual owner net profit; 2 FT + 2 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Route Eight Plays Through One Acquisition and Rights Screen",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with a candidate record, not an auction bid. Record the normalized domain, "
                    "discovery source, seller representation, asking price, acquisition ceiling, renewal "
                    "price, expiration date, registrar, and evidence links before discussing upside. "
                    "Use ICANN Lookup for registration context, USPTO Trademark Search for federal "
                    "marks, WIPO decisions for dispute patterns, and the Internet Archive for historical "
                    "use. A clean federal search does not eliminate common-law rights or confusing "
                    "similarity. Under 15 U.S.C. § 1125(d), bad-faith intent to profit from another "
                    "party's mark can create liability; registering a misspelling to sell it to the "
                    "mark owner is a rejection signal, not an outbound strategy. For expired assets, "
                    "inspect prior redirects, anchor concentration, malware history, and whether "
                    "valuable backlinks remain live. Neither an Ahrefs metric nor a historical "
                    "traffic screenshot establishes transferable traffic. Require a plausible buyer "
                    "unrelated to protected-brand confusion and a use case that survives the loss "
                    "of every historical link. Preserve dated evidence because the screening decision "
                    "must remain explainable after ownership, content, or search results change. "
                    "Treat seller assertions as leads for verification rather than facts that "
                    "automatically enter the valuation model."
                ),
                (
                    "Map seven local operating plays around the supplied eighth play: brandable "
                    "inventory, exact-match commercial names, expired-asset diligence, drop-catch "
                    "bidding, outbound upgrades, inbound conversion, and renewal recycling. These "
                    "seven labels organize this chapter; they are not additional supplied catalog "
                    "identifiers. Each opportunity receives a maximum cash exposure rather than a "
                    "vague quality score. For example, a $2,000 completed sale less a $500 acquisition, "
                    "$200 selling charge, and $20 renewal leaves $1,280 before shared operating costs. "
                    "That realized spread says nothing about the probability of selling another name. "
                    "A portfolio of 100 names renewing at $15 creates $1,500 of annual carrying "
                    "cost even when inquiries stop. Write acquisition ceilings against a stressed "
                    "holding period, and distinguish a retail asking price from observable completed "
                    "sales on NameBio. For outbound upgrades, select businesses with a genuine "
                    "descriptive fit, identify the sender accurately, and honor opt-outs under "
                    "15 U.S.C. § 7704 where applicable. Do not send trademark owners threatening "
                    "offers or imply that purchasing the name resolves a manufactured problem. "
                    "When evidence is weak, reduce the bid or leave the auction; additional "
                    "automation cannot repair a defective acquisition thesis."
                ),
                (
                    "Keep tier1_search_feed_afd_rsoc_arbitrage in a separate experimental ledger. "
                    "The supplied mapping describes wholesale search-feed arrangements, two-click "
                    "related-search journeys, $0.08–$0.35 purchased visits, $8–$45 advertiser auction "
                    "CPCs, and $25 million–$400 million-plus gross-scale ambitions. Those are "
                    "descriptions of that mapped strategy, not this domain portfolio's revenue "
                    "forecast or evidence that any named program currently accepts the proposed "
                    "traffic. Advertiser CPC is not the publisher's realized revenue per purchased "
                    "visitor. At 10,000 visits costing $0.20 each, spend is $2,000; a measured $0.16 "
                    "publisher yield produces $1,600 and a $400 loss before overhead. Require a "
                    "current written contract covering the exact domain, traffic source, geography, "
                    "and landing experience before buying traffic on Meta, TikTok, Taboola, or "
                    "Outbrain. Verify present product availability directly with each provider. "
                    "The proposed three-provider fallback involving System1, Tonic, Sedo, or "
                    "Media.net works only when three independently authorized arrangements exist. "
                    "Edge bot challenges and datacenter or VPN screening reduce invalid traffic "
                    "but never authorize prohibited sources. If editorial requirements, permissions, "
                    "or settlement quality fail, pause paid acquisition and return the asset to "
                    "ordinary sale inventory without moving rejected traffic elsewhere."
                ),
            ],
            "table": {
                "caption": "Eight Mapped Plays: Acquisition Math, Evidence, and Loss Containment",
                "headers": [
                    "Mapped operating play",
                    "Concrete unit economics",
                    "Evidence required before deployment",
                    "Risk fallback and stop condition",
                ],
                "rows": [
                    [
                        "Brandable inventory selected for independent commercial naming demand",
                        "Sell for $2,000 against $500 acquisition, $200 selling charge, and $20 renewal",
                        "Retain comparable completed sales and a dated trademark-screening evidence packet",
                        "Reject protected-brand dependence and cap exposure before entering any auction",
                    ],
                    [
                        "Exact-match commercial names serving descriptive buyer search intent",
                        "A $3,000 sale less $900 acquisition and $300 fee leaves $1,800 before carrying costs",
                        "Document descriptive use, plausible buyers, and comparable extension-specific completed transactions",
                        "Reduce bids when demand depends on one trademark owner or unsupported traffic",
                    ],
                    [
                        "Expired-asset diligence separating domain ownership from inherited traffic assumptions",
                        "A $600 purchase plus $20 renewal requires $620 recovery before selling costs",
                        "Inspect archived pages, live referring links, redirects, and historical abuse reports",
                        "Value the name without backlinks when authority evidence cannot be reproduced",
                    ],
                    [
                        "Drop-catch bidding with a fixed all-in acquisition ceiling",
                        "A $750 auction ceiling plus $50 charges creates $800 maximum acquisition exposure",
                        "Confirm auction terms, seller authority, registrar destination, and expected transfer restrictions",
                        "Stop bidding at the recorded ceiling rather than financing auction momentum",
                    ],
                    [
                        "Outbound upgrades offered to independently suitable descriptive-name buyers",
                        "Forty researched contacts costing $10 each consume $400 before any completed sale",
                        "Record buyer fit, accurate sender identity, suppression checks, and response disposition",
                        "Stop outreach after opt-out and abandon campaigns driven by trademark leverage",
                    ],
                    [
                        "Inbound conversion using documented ownership and controlled escrow instructions",
                        "A $4,000 sale with $400 commission yields $3,600 before inventory and operating costs",
                        "Verify marketplace fee terms, buyer correspondence, ownership evidence, and settlement references",
                        "Use independently verified escrow instructions when payment messages conflict or change",
                    ],
                    [
                        "Renewal recycling driven by forward carrying costs and buyer evidence",
                        "One hundred names at $15 renewals require $1,500 yearly carrying cash",
                        "Review inquiries, remaining holding budget, renewal price changes, and deletion deadlines",
                        "Export the renewal decision log before intentionally allowing weak inventory to expire",
                    ],
                    [
                        "tier1_search_feed_afd_rsoc_arbitrage operated outside the domain-sale scorecard",
                        "Ten thousand visits at $0.20 cost $2,000; $0.16 realized yield loses $400",
                        "Obtain current source-specific contracts and measured publisher settlement data before spending",
                        "Maintain three authorized providers only when available; otherwise stop unsupported traffic acquisition",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy Evidence Before Buying Inventory",
                "body": "Experienced operators protect their renewal budget and transaction evidence before optimizing asking prices.",
                "items": [
                    "Record the registrar's actual renewal price, including premium renewal treatment, instead of copying the first-year promotional registration price.",
                    "Compare completed sales within the same extension and buyer use case; exclude unsold marketplace asking prices from the valuation sample.",
                    "Save the registrar's transfer eligibility result before quoting a delivery date, including any applicable 60-day restrictions.",
                    "Use an independently opened escrow account session to verify payment instructions; never trust changed bank details carried only in an email thread.",
                ],
            },
        },
        {
            "heading": "2. Install a Six-Module Ledger With Atomic Events and Explicit External Boundaries",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use the six reference modules below as a small, auditable implementation, "
                    "not a marketplace crawler. Save their named files together in a project "
                    "directory, initialize ledger.db from the schema, and import the Python helpers "
                    "from a trusted local operator session. All monetary inputs are integer USD "
                    "cents. The schema separates assets, deals, immutable events, durable transfer "
                    "commands, and paired debit-credit journal entries. Domain normalization uses "
                    "lowercase IDNA form; ownership evidence still needs human verification. "
                    "Every write opens BEGIN IMMEDIATE, so competing SQLite writers serialize "
                    "before reading mutable state. Unique domain keys, event keys, command keys, "
                    "and journal source-line pairs prevent duplicate local effects. A partial "
                    "unique index prevents two active deals against the same asset. Exact event "
                    "replays return without posting; a reused key with a different payload raises "
                    "an error. WAL improves reader coexistence, while synchronous FULL requests "
                    "durable commits. Store the database on supported local storage rather than "
                    "a shared network filesystem. Make encrypted backups and test restoration "
                    "before live use. SQLite protects transaction consistency, not a host whose "
                    "administrator can replace database files or alter the application."
                ),
                (
                    "The local reference closes its read-modify-write races through transactions "
                    "and constraints, but no ledger can promise exactly-once effects across an "
                    "uncooperative registrar or escrow endpoint. Therefore the reference never "
                    "automatically transmits external transfer commands. Funding creates one durable "
                    "instruction with a stable key; an operator checks the provider's current "
                    "state, executes through an authorized interface, and records independently "
                    "verified evidence. If a request times out after possible execution, query "
                    "status rather than resubmitting blindly. Automating that boundary requires "
                    "documented provider idempotency and authenticated response verification. "
                    "The state machine is DRAFT, VERIFIED, FUNDED, TRANSFERRED, then SETTLED. "
                    "Cancellation is allowed before funding; later exceptions require separately "
                    "reviewed refund or reversal entries instead of erasing history. A screenshot "
                    "of a payment promise is not funding evidence. A registrar push is not "
                    "necessarily complete contractual delivery. The trusted caller attests that "
                    "the applicable buyer acceptance and seller obligations are satisfied before "
                    "recording TRANSFERRED. Public webhooks must not call these helpers directly; "
                    "an adapter must authenticate the provider, validate payloads, and independently "
                    "resolve account and transaction references before creating an internal event."
                ),
                (
                    "Recognize the gross sale when the documented delivery conditions are "
                    "satisfied, then record payout separately. The transfer event debits escrow "
                    "receivable and credits sale revenue for the gross amount, while moving "
                    "the acquired asset's cost from inventory into cost of goods sold. Settlement "
                    "debits cash for net proceeds, debits the selling-fee expense, and clears "
                    "escrow receivable. This prevents payout timing from silently redefining "
                    "revenue. A $12,000 sale with $1,200 fees creates $10,800 cash, not $10,800 "
                    "gross revenue. Acquisition payments increase inventory and reduce cash; "
                    "they become operating expense only when sold or written down under the "
                    "chosen accounting policy. The example uses acquisition cost as carrying "
                    "value and expenses renewals. Review the entity's actual treatment with its "
                    "accountant before adopting production reporting. The monthly view exposes "
                    "both operating profit and cash movement excluding capital contributions. "
                    "The QA module checks inventory agreement, receivable clearance, unmatched "
                    "delivery evidence, and minimum event coverage. Add authenticated provider "
                    "statement imports and bank matching before treating a live period as "
                    "closed; a balanced internal journal cannot prove that external money arrived."
                ),
            ],
            "table": {
                "caption": "Production Engineering / SQLite-or-Postgres Ledger & Idempotent Workflow Reference Table",
                "headers": [
                    "Module and file",
                    "Copy-pasteable reference implementation",
                    "Concurrency and evidence contract",
                ],
                "rows": [
                    [
                        "Module 1: save the database definition as schema.sql",
                        """PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = FULL;

CREATE TABLE IF NOT EXISTS asset (
    id INTEGER PRIMARY KEY,
    domain TEXT NOT NULL UNIQUE,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    cost INTEGER NOT NULL DEFAULT 0 CHECK(cost >= 0),
    state TEXT NOT NULL DEFAULT 'SCREENED'
        CHECK(state IN ('SCREENED','HELD','RESERVED','SOLD'))
);
CREATE TABLE IF NOT EXISTS deal (
    id TEXT PRIMARY KEY,
    asset_id INTEGER NOT NULL REFERENCES asset(id),
    gross INTEGER NOT NULL CHECK(gross > 0),
    fee INTEGER NOT NULL CHECK(fee >= 0 AND fee < gross),
    state TEXT NOT NULL
        CHECK(state IN ('DRAFT','VERIFIED','FUNDED','TRANSFERRED','SETTLED','CANCELLED'))
);
CREATE UNIQUE INDEX IF NOT EXISTS one_live_deal
    ON deal(asset_id) WHERE state <> 'CANCELLED';

CREATE TABLE IF NOT EXISTS event (
    event_key TEXT PRIMARY KEY,
    payload TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS command (
    command_key TEXT PRIMARY KEY,
    deal_id TEXT NOT NULL REFERENCES deal(id),
    action TEXT NOT NULL CHECK(action = 'TRANSFER'),
    evidence TEXT,
    UNIQUE(deal_id, action)
);
CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY,
    source_key TEXT NOT NULL REFERENCES event(event_key),
    line_no INTEGER NOT NULL,
    booked_on TEXT NOT NULL,
    debit TEXT NOT NULL,
    credit TEXT NOT NULL,
    amount INTEGER NOT NULL CHECK(amount > 0),
    currency TEXT NOT NULL DEFAULT 'USD' CHECK(currency = 'USD'),
    UNIQUE(source_key, line_no),
    CHECK(debit <> credit)
);
CREATE TRIGGER IF NOT EXISTS journal_no_update
BEFORE UPDATE ON journal BEGIN
    SELECT RAISE(ABORT, 'journal is append only');
END;
CREATE TRIGGER IF NOT EXISTS journal_no_delete
BEFORE DELETE ON journal BEGIN
    SELECT RAISE(ABORT, 'journal is append only');
END;
CREATE TRIGGER IF NOT EXISTS event_no_update
BEFORE UPDATE ON event BEGIN
    SELECT RAISE(ABORT, 'event is append only');
END;
CREATE TRIGGER IF NOT EXISTS event_no_delete
BEFORE DELETE ON event BEGIN
    SELECT RAISE(ABORT, 'event is append only');
END;""",
                        "Run once through sqlite3.executescript; immutable journal rows and uniqueness protect committed local records.",
                    ],
                    [
                        "Module 2: save normalization, scoring, and transaction helpers as ledger_core.py",
                        """from contextlib import contextmanager
from datetime import date
import json
import re
import sqlite3

@contextmanager
def tx():
    db = sqlite3.connect('ledger.db', timeout=30, isolation_level=None)
    try:
        db.execute('PRAGMA foreign_keys = ON')
        db.execute('PRAGMA synchronous = FULL')
        db.execute('BEGIN IMMEDIATE')
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()

def event(db, key, payload):
    if not isinstance(key, str) or not key.strip():
        raise ValueError('event key required')
    encoded = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    old = db.execute(
        'SELECT payload FROM event WHERE event_key=?', (key,)
    ).fetchone()
    if old:
        if old[0] != encoded:
            raise ValueError('event key payload conflict')
        return False
    db.execute('INSERT INTO event(event_key,payload) VALUES (?,?)',
               (key, encoded))
    return True

def cents(value, positive=False):
    if type(value) is not int or value < int(positive):
        raise ValueError('integer USD cents required')
    return value

def evidence_ref(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('verified evidence reference required')
    return value

def post(db, key, line, day, debit, credit, amount):
    cents(amount, positive=True)
    day = date.fromisoformat(day).isoformat()
    db.execute(
        'INSERT INTO journal(source_key,line_no,booked_on,debit,credit,amount) '
        'VALUES (?,?,?,?,?,?)', (key, line, day, debit, credit, amount)
    )

def intake(name, rights_clear, buyer_count, comparable_count):
    domain = name.strip().rstrip('.').encode('idna').decode('ascii').lower()
    labels = domain.split('.')
    if len(domain) > 253 or len(labels) < 2:
        raise ValueError('public domain format required')
    if any(not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?', x)
           for x in labels):
        raise ValueError('invalid domain label')
    if rights_clear is not True:
        raise ValueError('rights screen must pass')
    if any(type(x) is not int or x < 0
           for x in (buyer_count, comparable_count)):
        raise ValueError('nonnegative evidence counts required')
    score = 40 + min(buyer_count, 5) * 8 + min(comparable_count, 4) * 5
    with tx() as db:
        db.execute(
            'INSERT INTO asset(domain,score) VALUES (?,?) '
            'ON CONFLICT(domain) DO NOTHING', (domain, score)
        )
        return db.execute(
            'SELECT id,score FROM asset WHERE domain=?', (domain,)
        ).fetchone()

def acquire(asset_id, cost, day, key, proof):
    cents(cost, positive=True)
    evidence_ref(proof)
    payload = ['acquire', asset_id, cost, day, proof]
    with tx() as db:
        if not event(db, key, payload):
            return
        row = db.execute(
            'SELECT state FROM asset WHERE id=?', (asset_id,)
        ).fetchone()
        if row != ('SCREENED',):
            raise ValueError('asset must be screened and unacquired')
        post(db, key, 1, day, 'inventory', 'cash', cost)
        db.execute('UPDATE asset SET cost=?,state=? WHERE id=?',
                   (cost, 'HELD', asset_id))

def cash_entry(kind, amount, day, key, proof):
    cents(amount, positive=True)
    evidence_ref(proof)
    pairs = {
        'capital': ('cash', 'equity'),
        'renewal': ('renewals', 'cash'),
        'opex': ('opex', 'cash'),
    }
    debit, credit = pairs[kind]
    with tx() as db:
        if event(db, key, [kind, amount, day, proof]):
            post(db, key, 1, day, debit, credit, amount)
""",
                        "Screening scores route review rather than predict sales; acquisition requires independent ownership and payment evidence.",
                    ],
                    [
                        "Module 3: save the verified escrow state machine as workflow.py",
                        """from ledger_core import tx, event, post, cents, evidence_ref

def open_deal(deal_id, asset_id, gross, fee, key):
    if not isinstance(deal_id, str) or not deal_id.strip():
        raise ValueError('deal identifier required')
    cents(gross, positive=True)
    cents(fee)
    if fee >= gross:
        raise ValueError('fee must be smaller than gross sale')
    with tx() as db:
        if not event(db, key, ['open', deal_id, asset_id, gross, fee]):
            return
        row = db.execute(
            'SELECT state FROM asset WHERE id=?', (asset_id,)
        ).fetchone()
        if row != ('HELD',):
            raise ValueError('asset is not available')
        db.execute(
            'INSERT INTO deal(id,asset_id,gross,fee,state) VALUES (?,?,?,?,?)',
            (deal_id, asset_id, gross, fee, 'DRAFT')
        )
        db.execute('UPDATE asset SET state=? WHERE id=?',
                   ('RESERVED', asset_id))

def advance(deal_id, target, day, key, proof):
    evidence_ref(proof)
    allowed = {
        'DRAFT': {'VERIFIED', 'CANCELLED'},
        'VERIFIED': {'FUNDED', 'CANCELLED'},
        'FUNDED': {'TRANSFERRED'},
    }
    with tx() as db:
        if not event(db, key, ['advance', deal_id, target, day, proof]):
            return
        row = db.execute(
            'SELECT d.state,d.asset_id,d.gross,a.cost '
            'FROM deal d JOIN asset a ON a.id=d.asset_id WHERE d.id=?',
            (deal_id,)
        ).fetchone()
        if not row or target not in allowed.get(row[0], set()):
            raise ValueError('invalid transition')
        _, asset_id, gross, cost = row
        if target == 'FUNDED':
            db.execute(
                'INSERT INTO command(command_key,deal_id,action) VALUES (?,?,?)',
                ('transfer:' + deal_id, deal_id, 'TRANSFER')
            )
        if target == 'TRANSFERRED':
            changed = db.execute(
                'UPDATE command SET evidence=? '
                'WHERE deal_id=? AND action=? AND evidence IS NULL',
                (proof, deal_id, 'TRANSFER')
            ).rowcount
            if changed != 1:
                raise ValueError('one pending transfer instruction required')
            post(db, key, 1, day, 'escrow_receivable', 'revenue', gross)
            post(db, key, 2, day, 'cogs', 'inventory', cost)
            db.execute('UPDATE asset SET state=? WHERE id=?',
                       ('SOLD', asset_id))
        if target == 'CANCELLED':
            db.execute('UPDATE asset SET state=? WHERE id=?',
                       ('HELD', asset_id))
        db.execute('UPDATE deal SET state=? WHERE id=?', (target, deal_id))
""",
                        "The trusted caller verifies evidence; external transfer execution remains manual unless provider idempotency is documented.",
                    ],
                    [
                        "Module 4: save atomic payout reconciliation as settlement.py",
                        """from ledger_core import tx, event, post, cents, evidence_ref

def settle(deal_id, net_received, day, receipt_key, proof):
    cents(net_received, positive=True)
    evidence_ref(proof)
    with tx() as db:
        payload = ['settle', deal_id, net_received, day, proof]
        if not event(db, receipt_key, payload):
            return
        row = db.execute(
            'SELECT state,gross,fee FROM deal WHERE id=?', (deal_id,)
        ).fetchone()
        if not row or row[0] != 'TRANSFERRED':
            raise ValueError('completed delivery required before settlement')
        _, gross, fee = row
        if net_received != gross - fee:
            raise ValueError('payout differs from recorded gross less fee')
        post(db, receipt_key, 1, day,
             'cash', 'escrow_receivable', net_received)
        if fee:
            post(db, receipt_key, 2, day,
                 'selling_fees', 'escrow_receivable', fee)
        db.execute('UPDATE deal SET state=? WHERE id=?',
                   ('SETTLED', deal_id))
""",
                        "Use provider-account-qualified receipt keys and verified bank evidence; mismatched payouts remain unreconciled for investigation.",
                    ],
                    [
                        "Module 5: save monthly cash and profit views as reconciliation.sql",
                        """CREATE VIEW IF NOT EXISTS account_balance AS
SELECT account, SUM(delta) AS balance
FROM (
    SELECT debit AS account, amount AS delta FROM journal
    UNION ALL
    SELECT credit AS account, -amount AS delta FROM journal
)
GROUP BY account;

CREATE VIEW IF NOT EXISTS monthly_reconciliation AS
WITH monthly AS (
    SELECT substr(booked_on,1,7) AS month,
        SUM(CASE WHEN credit='revenue' THEN amount ELSE 0 END
          - CASE WHEN debit='revenue' THEN amount ELSE 0 END) AS gross,
        SUM(CASE WHEN debit='cogs' THEN amount ELSE 0 END
          - CASE WHEN credit='cogs' THEN amount ELSE 0 END) AS cogs,
        SUM(CASE WHEN debit='selling_fees' THEN amount ELSE 0 END
          - CASE WHEN credit='selling_fees' THEN amount ELSE 0 END) AS fees,
        SUM(CASE WHEN debit='renewals' THEN amount ELSE 0 END
          - CASE WHEN credit='renewals' THEN amount ELSE 0 END) AS renewals,
        SUM(CASE WHEN debit='opex' THEN amount ELSE 0 END
          - CASE WHEN credit='opex' THEN amount ELSE 0 END) AS opex,
        SUM(CASE WHEN debit='cash' AND credit<>'equity' THEN amount ELSE 0 END
          - CASE WHEN credit='cash' AND debit<>'equity' THEN amount ELSE 0 END) AS cash_change
    FROM journal GROUP BY substr(booked_on,1,7)
)
SELECT month,gross,cogs,fees,renewals,opex,
       gross-cogs-fees-renewals-opex AS owner_profit,
       cash_change
FROM monthly;""",
                        "Amounts remain integer cents; capital contributions are excluded from operating cash movement and owner profit.",
                    ],
                    [
                        "Module 6: save structural and accounting checks as qa.py",
                        """from ledger_core import tx

def check():
    with tx() as db:
        if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('database integrity check failed')
        if db.execute('PRAGMA foreign_key_check').fetchall():
            raise ValueError('foreign key check failed')
        balances = dict(db.execute(
            'SELECT account,balance FROM account_balance'
        ))
        permitted = {
            'cash', 'equity', 'inventory', 'escrow_receivable',
            'revenue', 'cogs', 'selling_fees', 'renewals', 'opex'
        }
        if set(balances) - permitted:
            raise ValueError('unrecognized ledger account')
        if sum(balances.values()) != 0:
            raise ValueError('trial balance mismatch')
        inventory = db.execute(
            "SELECT COALESCE(SUM(cost),0) FROM asset WHERE state<>'SOLD'"
        ).fetchone()[0]
        if balances.get('inventory', 0) != inventory:
            raise ValueError('inventory subledger mismatch')
        receivable = db.execute(
            "SELECT COALESCE(SUM(gross),0) FROM deal WHERE state='TRANSFERRED'"
        ).fetchone()[0]
        if balances.get('escrow_receivable', 0) != receivable:
            raise ValueError('escrow receivable mismatch')
        if balances.get('cash', 0) < 0:
            raise ValueError('cash requires funding or investigation')
        missing = db.execute(
            "SELECT COUNT(*) FROM deal d LEFT JOIN command c ON c.deal_id=d.id "
            "WHERE d.state IN ('TRANSFERRED','SETTLED') "
            "AND (c.command_key IS NULL OR c.evidence IS NULL)"
        ).fetchone()[0]
        if missing:
            raise ValueError('delivery evidence missing')
        return list(db.execute(
            'SELECT * FROM monthly_reconciliation ORDER BY month'
        ))
""",
                        "Run after each import and before closing; separately compare bank, registrar, escrow, and inventory evidence.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Initialize the isolated project ledger",
                    "action": "Save the six named reference files and create ledger.db using schema.sql followed by reconciliation.sql.",
                    "detail": "Use sqlite3.connect and executescript from Python's standard library; retain the same working directory for all helper calls.",
                },
                {
                    "step": 2,
                    "title": "Record opening cash and verified acquisitions",
                    "action": "Call cash_entry for actual capital, then intake and acquire for each independently verified purchased asset.",
                    "detail": "For the cohort example, opening capital is 2,500,000 cents; source keys must identify real, nonreused provider or bank references.",
                },
                {
                    "step": 3,
                    "title": "Advance only evidence-backed transactions",
                    "action": "Open the deal, verify ownership and terms, confirm escrow funding, and record completed contractual delivery.",
                    "detail": "The funded event creates a durable transfer instruction, not an external API call; reconcile ambiguous provider outcomes before acting again.",
                },
                {
                    "step": 4,
                    "title": "Close receipts and test duplicate events",
                    "action": "Settle verified payouts, enter renewal and operating payments, run check, and reconcile external statements.",
                    "detail": "Replay identical events and confirm unchanged balances; changed payloads, competing active deals, and incorrect net receipts must fail without partial writes.",
                },
            ],
        },
        {
            "heading": "3. Execute a Worked 90-Day Cohort Walk Without Confusing Profit and Cash",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The Worked 90-Day Cohort Walk is a deliberately successful illustrative "
                    "quarter calibrated to the Base case, not a measured sell-through forecast. "
                    "Opening owner capital is $25,000, within the stated $8,000–$60,000 startup "
                    "range. There is no opening inventory, debt, payable, or escrow balance. "
                    "Month 1 screens 30 acquisition candidates, rejects 20, and purchases ten "
                    "names for $8,000. Month 2 screens 22, rejects 16, and purchases six for "
                    "$6,000. Month 3 screens 16, rejects 12, and purchases four for $4,000. "
                    "These rejected candidates never become assets and therefore create no "
                    "inventory write-off. Buyer inquiries arrive separately: eight, fourteen, "
                    "and twenty by month. Scrub three, four, and six for spam, impersonation, "
                    "or lack of a credible purchasing path, leaving five, ten, and fourteen "
                    "qualified inquiries. Qualification does not mean a sale, and repeated "
                    "contacts from one buyer must not inflate the lead count. The remaining "
                    "qualified conversations either mature into the seven completed sales or "
                    "remain open at quarter end. Keep inquiry cohorts separate from asset "
                    "cohorts so a sale is attributed to its actual acquired name rather than "
                    "the latest marketing activity."
                ),
                (
                    "Month 1 produces no completed sales and consumes $11,300 cash: $8,000 "
                    "acquisitions, $300 renewals, and $3,000 operating expense. Month 2 closes "
                    "two Month 1 names for $12,000 gross, with $5,000 combined acquisition "
                    "basis and $1,200 selling fees. Both transfer and payout occur before "
                    "month end, yielding $10,800 cash receipts. After $6,000 acquisitions, "
                    "$300 renewals, and $3,000 operating expense, monthly cash increases "
                    "$1,500. Month 3 closes five names for $28,000 gross: two additional "
                    "Month 1 names for $8,000 with $2,500 basis, two Month 2 names for "
                    "$16,000 with $5,500 basis, and one Month 3 name for $4,000 with "
                    "$2,000 basis. Selling fees are $2,800, producing $25,200 net receipts. "
                    "Subtract $4,000 acquisitions, $300 renewals, and $3,100 operating expense "
                    "to obtain $17,800 monthly cash growth. There are no unpaid completed "
                    "sales, refunds, acquisition losses, or write-downs in this particular "
                    "walk. That explicit zero is a scenario assumption requiring verification, "
                    "not permission to omit adverse events from a live ledger. An escrow "
                    "delay would leave receivables outstanding and reduce cash without "
                    "changing an already earned gross sale."
                ),
                (
                    "Quarter-end inventory contains thirteen names at $3,000 carrying cost: "
                    "six Month 1 names totaling $500, four Month 2 names totaling $500, "
                    "and three Month 3 names totaling $2,000. Gross sales of $40,000 less "
                    "$15,000 sold inventory, $4,000 selling fees, $900 renewals, and $9,100 "
                    "operating expense produce $11,000 owner operating profit. Cash growth "
                    "is only $8,000 because inventory purchases exceed cost of goods sold "
                    "by $3,000. Closing cash is therefore $33,000, and cash plus inventory "
                    "equals $36,000, reconciling opening capital plus profit. Four equivalent "
                    "quarters yield $160,000 revenue, $116,000 total costs, and $44,000 "
                    "profit at 27.5%, exactly the canonical Base case. Repeating the cash "
                    "pattern would also accumulate $12,000 inventory and generate $32,000 "
                    "annual cash growth; do not present $44,000 as distributable cash while "
                    "retaining that inventory expansion. The $9,100 quarterly operating "
                    "envelope averages approximately $3,033 monthly and includes contractor "
                    "support and operating systems. Owner profit is the residual available "
                    "for owner compensation and entity-specific obligations, not a second "
                    "salary added above the model. Maintain the Base staffing configuration "
                    "of one full-time operator and one contractor."
                ),
            ],
            "table": {
                "caption": "Worked 90-Day Cohort Walk",
                "headers": [
                    "Period and acquisition cohort",
                    "Lead scrubs and completed sales",
                    "Recognized costs and operating result",
                    "Cash timing and cumulative reconciliation",
                ],
                "rows": [
                    [
                        "Month 1 purchases ten names for $8,000 after rejecting twenty candidates",
                        "Eight inquiries minus three scrubs leave five qualified; no sales close",
                        "No sold basis; $300 renewals plus $3,000 opex produce $3,300 loss",
                        "No receipts; $11,300 outflow leaves $13,700 cash and negative $11,300 cumulative change",
                    ],
                    [
                        "Month 2 purchases six names for $6,000 after rejecting sixteen candidates",
                        "Fourteen inquiries minus four scrubs; two Month 1 names sell for $12,000",
                        "$5,000 sold basis plus $1,200 fees, $300 renewals, and $3,000 opex leave $2,500 profit",
                        "$10,800 payout less $9,300 other payments adds $1,500; cumulative change is negative $9,800",
                    ],
                    [
                        "Month 3 purchases four names for $4,000 after rejecting twelve candidates",
                        "Twenty inquiries minus six scrubs; five names across three acquisition cohorts sell for $28,000",
                        "$10,000 sold basis plus $2,800 fees, $300 renewals, and $3,100 opex leave $11,800 profit",
                        "$25,200 payout less $7,400 other payments adds $17,800; cumulative change reaches positive $8,000",
                    ],
                    [
                        "Quarterly accrual total covers twenty purchased names and seven completed sales",
                        "Forty-two inquiries minus thirteen scrubs leave twenty-nine qualified; completed gross sales total $40,000",
                        "$15,000 sold basis plus $4,000 fees, $900 renewals, and $9,100 opex leave $11,000 profit",
                        "All seven payouts clear within the quarter; no closing receivable or modeled inventory loss",
                    ],
                    [
                        "Quarterly cash bridge retains thirteen names with $3,000 aggregate acquisition basis",
                        "Remaining inventory comprises six first-cohort, four second-cohort, and three third-cohort names",
                        "$11,000 profit less $3,000 inventory growth equals $8,000 operating cash growth",
                        "$25,000 opening capital plus $8,000 growth leaves $33,000 cash and $36,000 total assets",
                    ],
                    [
                        "Annualized Base run rate repeats the quarter's economics four times",
                        "Twenty-eight illustrative completed sales generate exactly $160,000 annual gross domain proceeds",
                        "$60,000 sold basis plus $16,000 fees, $3,600 renewals, and $36,400 opex leave $44,000 profit",
                        "Unchanged inventory growth produces $32,000 annual cash growth and $12,000 additional retained inventory",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Committing the Next Cohort",
                "body": "Expansion follows reconciled evidence, not optimistic asking prices or an unusually strong closing week.",
                "items": [
                    "Confirm ownership, rights-screen evidence, actual renewal prices, and transfer eligibility for every proposed acquisition before committing funds.",
                    "Confirm funded escrow independently and verify the receiving account before releasing a domain or its transfer authorization code.",
                    "Reconcile gross proceeds, selling fees, sold acquisition basis, and bank deposits; investigate every difference before declaring the period closed.",
                    "Recompute available cash after reserved renewals and open transfer obligations; delay purchases when the next cohort depends on an unclosed sale.",
                ],
            },
        },
        {
            "heading": "4. Close the Evidence Chain, Stress Liquidity, and Expand Only the Working System",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Close the month by matching four independent records: the purchase invoice, "
                    "registrar ownership history, escrow transaction history, and bank statement. "
                    "Use provider-account-qualified identifiers because two services can issue "
                    "the same short transaction number. The registrar proves a technical "
                    "ownership event, the contract defines delivery, escrow documents conditional "
                    "funds, and the bank proves settlement cash. None substitutes for all the "
                    "others. Reconcile the domain inventory by normalized name and acquisition "
                    "basis, not merely by count; thirteen names worth $3,000 cannot be replaced "
                    "in the ledger by thirteen names carrying an arbitrary retail valuation. "
                    "Preserve rejected acquisition evidence and lost inquiry reasons separately "
                    "from purchased inventory. If a name expires, is transferred incorrectly, "
                    "or becomes impaired, record the approved accounting consequence through "
                    "an append-only adjustment workflow. The reference intentionally stops short "
                    "of general refunds, chargebacks, taxes, multicurrency, and impairment automation; "
                    "extend the account model and tests before using those features. Never "
                    "force an exception through a successful-sale function just to clear a "
                    "dashboard warning. The monthly report should state unresolved exceptions, "
                    "responsible operators, and expected next actions alongside its revenue "
                    "and profit totals."
                ),
                (
                    "Stress cash before expanding inventory. In the worked quarter, delaying "
                    "all Month 3 payouts beyond day ninety removes $25,200 from closing "
                    "cash, reducing it from $33,000 to $7,800 while completed-sale profit "
                    "can remain unchanged. That balance must still fund renewals and next "
                    "month's operating commitments. A separate demand stress removes the "
                    "Month 3 sales entirely: gross revenue falls to $12,000, sold basis "
                    "to $5,000, and selling fees to $1,200; with $900 renewals and $9,100 "
                    "opex, the quarter loses $4,200 before impairment. Purchases still "
                    "consume $18,000 cash, leaving $7,800 cash and $13,000 inventory. "
                    "The identical cash balance hides very different risk: one business "
                    "holds collectible receivables, the other holds unsold names. Maintain "
                    "separate dashboards for overdue payouts, renewal exposure, inquiry "
                    "conversion, and aging inventory. The canonical Conservative case is "
                    "$20,000 revenue minus $17,000 costs for $3,000 profit, not a slight "
                    "variation of the successful quarter. Since first-deal timing can "
                    "span three to twenty-four months, size the initial portfolio so "
                    "extended inactivity does not force distressed liquidation or missed "
                    "renewals on the strongest assets."
                ),
                (
                    "Scale only the activities whose evidence and economics survive review. "
                    "Renewal tracking can create calendar tasks and reserved-cash reports; "
                    "comparable-sale monitoring can collect candidate observations; inbound "
                    "routing can deduplicate leads and assign a response owner. Keep rights "
                    "judgments, acquisition commitments, changed payment instructions, and "
                    "ambiguous transfer outcomes under explicit human review. The Scaled "
                    "case remains $300,000 gross proceeds, $180,000 total costs, and "
                    "$120,000 owner net profit at 40%, staffed by two full-time people "
                    "and two contractors. It does not inherit the search-feed strategy's "
                    "advertiser spend, traffic receipts, or ambitious wholesale scale. "
                    "If that separate experiment becomes viable, maintain its own profit "
                    "center and invalid-traffic reserve rather than improving domain "
                    "margins with unrelated gross flows. Apply 15 U.S.C. § 1125(d) "
                    "and the relevant contractual domain dispute policy throughout the "
                    "holding period, not only during acquisition. Under 15 U.S.C. "
                    "§ 1117(d), statutory damages for an established cybersquatting "
                    "violation can range from $1,000 to $100,000 per domain. That "
                    "exposure overwhelms many small-name spreads. The operating advantage "
                    "is a defensible selection process and clean execution, not a "
                    "larger speculative list of names."
                ),
            ],
            "table": {
                "caption": "Month-End Forensic Controls and Exception Recovery",
                "headers": [
                    "Control and failure condition",
                    "Evidence and deterministic check",
                    "Recovery action preserving the audit trail",
                    "Named operating owner and frequency",
                ],
                "rows": [
                    [
                        "Duplicate provider notification attempts to repeat an existing sale posting",
                        "Compare the stable event key and canonical payload before modifying any balance",
                        "Return unchanged for an exact replay; reject changed payloads under reused identifiers",
                        "Full-time operator reviews rejected-event counts during each daily transaction check",
                    ],
                    [
                        "Two buyers attempt to reserve the same acquired domain concurrently",
                        "Use serialized writes and the partial unique active-deal index on asset identity",
                        "Allow one reservation and reject the competing transaction without partial journal writes",
                        "Sales operator confirms availability immediately before issuing a binding transaction instruction",
                    ],
                    [
                        "Escrow payment differs from gross proceeds less the agreed selling fee",
                        "Match the provider statement, recorded fee, account identity, and actual bank receipt",
                        "Leave the deal unsettled and investigate deductions before recording any adjustment",
                        "Contractor prepares reconciliation and the full-time operator resolves all monetary differences",
                    ],
                    [
                        "Registrar transfer reports completion while contractual buyer acceptance remains outstanding",
                        "Compare registrar history with signed delivery terms and independently verified buyer acceptance",
                        "Keep the funded transaction open until delivery conditions support revenue recognition",
                        "Transaction operator reviews funded transfers daily until acceptance evidence is complete",
                    ],
                    [
                        "Renewal exposure exceeds cash reserved for the next holding interval",
                        "Total actual renewal charges by deadline and compare with uncommitted bank cash",
                        "Freeze discretionary acquisitions and document selective renewal or intentional expiry decisions",
                        "Portfolio operator reviews ninety-day renewal exposure weekly and before every auction",
                    ],
                    [
                        "Search-feed settlement contains invalid-traffic deductions or unsupported source allegations",
                        "Reconcile provider-approved sources, edge filtering records, and actual publisher settlement statements",
                        "Pause affected traffic and investigate; never reroute rejected traffic to conceal its source",
                        "Separate experiment owner reviews source permissions before spending and settlements before expansion",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A domain is inventory until a verified buyer, completed delivery, and reconciled ledger turn it into earned cash.",
    "diagram_id": "diag-01",
    "action_checklist": [
        "Create one normalized asset record per domain and attach acquisition, ownership, rights-screen, renewal, and transfer-eligibility evidence before bidding.",
        "Save and initialize the six reference modules, then test exact event replay, conflicting payload rejection, concurrent reservations, and rollback after invalid settlement.",
        "Document the registrar and escrow state transitions, including independent funding checks and the manual treatment of ambiguous external outcomes.",
        "Reproduce the quarter's $40,000 revenue, $29,000 costs, $11,000 profit, $3,000 retained inventory, and $8,000 cash growth from underlying transactions.",
        "Run the delayed-payout and absent-sale stresses before funding another acquisition cohort, reserving cash for renewals and existing obligations.",
        "Keep search-feed traffic economics outside domain-sale reporting and require current source-specific provider authorization before any paid-traffic experiment.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 1125(d) — Cyberpiracy prevention",
            "url": "https://www.law.cornell.edu/uscode/text/15/1125",
            "relevance": "Screen acquisitions and sales conduct for protected-mark conflicts and bad-faith intent to profit; document independent descriptive or brandable use cases.",
        },
        {
            "title": "15 U.S.C. § 1117(d) — Statutory damages for cybersquatting",
            "url": "https://www.law.cornell.edu/uscode/text/15/1117",
            "relevance": "The statutory damages election can range from $1,000 to $100,000 per domain for an established violation, making rights screening economically material.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Structure commercial outbound campaigns around accurate transmission information, nondeceptive subjects, required sender information, and honored opt-out requests.",
        },
        {
            "title": "15 U.S.C. § 45 — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": "Avoid deceptive traffic claims, fabricated ownership assertions, and misleading buyer-facing representations in domain listings and related monetization experiments.",
        },
    ],
}
