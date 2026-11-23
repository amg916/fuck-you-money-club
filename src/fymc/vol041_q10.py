from __future__ import annotations

CHAPTER_10 = {
    "id": "Q10",
    "chapter_id": "Q10",
    "chapter_number": 10,
    "question_number": 10,
    "slug": "automation-ai-leverage-scalable-distribution-flywheels",
    "question_prompt": "How does a 1 FT + 2 C (3 people) buying group, commercial card-float & rebate arbitrage team automate 70%+ of repetitive research, qualification, fulfillment, and traffic/deal acquisition while keeping human-in-the-loop QA?",
    "kicker": "Q10 / THE BIG MONEY PLAYBOOKS",
    "title": "Automation, AI Leverage & Scalable Distribution Flywheels",
    "subtitle": "Python Deal Reconciliation, Telegram Signal Intake, Rebate Eligibility Routing, and T-Bill Settlement Controls Under IRC 6050W",
    "layout_template": "case_study_walkthrough",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #41, ranked #10 of 43 with a 93/100 Money-to-Manpower Score, earns its "
        "automation edge through reconciled evidence rather than unattended purchasing. This "
        "chapter translates 11 mapped plays into a three-person operating system spanning "
        "wholesale commitments, commercial rebates, and treasury income. Python workers normalize "
        "deal messages; constrained language models extract terms; humans authorize commitments "
        "and cash movements. The canonical annual owner-profit cases remain $20,000 Conservative, "
        "$143,500 Base, and $360,000 Scaled, with the Scaled team expanding to five people. "
        "Every workflow separates borrowed statement float from earned contribution, validates "
        "portal eligibility before spending, and measures exception-adjusted labor savings. "
        "Distribution compounds only when useful inbound tools generate qualified demand without "
        "exposing private deal inventory or harvesting community members."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross scorecard basis; $87,500 retained contribution at 35%.",
            "note": "8% gross-basis net margin; $20,000 annual owner net profit; 22.86% retained net margin; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross scorecard basis; $358,750 retained contribution at 35%.",
            "note": "14.0% gross-basis net margin; $143,500 annual owner net profit; 40.0% retained net margin; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross scorecard basis; $630,000 retained contribution at 35%.",
            "note": "20% gross-basis net margin; $360,000 annual owner net profit; 57.14% retained net margin; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence-first intake system around eleven operating plays",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build three separate ledgers before connecting any feed: wholesale fulfillment, "
                    "commercial card and portal rewards, and bank or Treasury earnings. A shared "
                    "deal identifier connects evidence without merging their economics. For "
                    "BuyForMeRetail, Pointsmaker, and MaxOutDeals, store the commitment identifier, "
                    "accepted SKU, quantity ceiling, destination, expiration, reimbursement amount, "
                    "and settlement terms from the actual accepted offer. An advertised opportunity "
                    "is not a purchase commitment. Python workers using urllib.request, json, "
                    "sqlite3, decimal, and zoneinfo can normalize authorized exports and documented "
                    "webhooks; do not assume these vendors expose public integration endpoints. "
                    "Preserve source timestamps and document hashes alongside parsed fields. An "
                    "LLM may extract a proposed record into a fixed schema, but supplier text is "
                    "untrusted data, never executable instructions. Require exact evidence spans "
                    "for amounts and dates, reject absent terms, and route conflicting quantities "
                    "to a person. The full-time operator owns capital and commitments; one contractor "
                    "handles procurement evidence and parcel exceptions, while the second handles "
                    "reconciliation and inbound acquisition. Access follows those duties: contractors "
                    "can prepare records without possessing payment-release credentials. Keep "
                    "separate production and test data, and redact account identifiers before any "
                    "external model request. This structure makes automation replace repetitive "
                    "handling rather than silently transferring spending authority."
                ),
                (
                    "Implement telegram_channel_signal_scraping as permission-aware signal intake, "
                    "not audience extraction. Monitor public Telegram broadcasts through a permitted "
                    "read-only client where access and platform terms allow; the official Bot API "
                    "does not provide unrestricted historical access to arbitrary public channels. "
                    "For OTC deal rooms, wholesale distress feeds, and niche community streams, "
                    "require explicit access rights before ingesting their messages. Capture product "
                    "identifiers, requested volumes, delivery windows, and public contact routes, "
                    "then deduplicate using source ID plus message ID. Never enumerate members "
                    "or turn participant identities into an outbound list. If access becomes "
                    "uncertain, stop that connector and retain only permitted passive public "
                    "listeners; shift prospect capture to an official Bot API utility bot that "
                    "people initiate themselves. Give the bot a shipment-readiness calculator or "
                    "buying-group eligibility checklist, then ask users to submit their own "
                    "requirements. An illustrative 1,000-message batch costing $2 to process "
                    "and yielding 20 qualified signals costs $0.10 per signal before human "
                    "review. If only four become accepted commitments, processing cost becomes "
                    "$0.50 per commitment. Record both denominators so an impressive extraction "
                    "rate cannot disguise weak purchasing relevance or excessive reviewer effort. "
                    "Expire stale offers rather than repeatedly promoting yesterday's apparent spread."
                ),
                (
                    "The eleven mapped plays below are chapter-level operating applications; only "
                    "telegram_channel_signal_scraping carries a supplied catalog identifier. Their "
                    "purpose is to form one auditable chain, not eleven disconnected subscriptions. "
                    "Start with a two-week baseline of repetitive handling minutes, including "
                    "rework, exception chasing, and duplicate entry. Suppose 1,000 monthly records "
                    "previously required six minutes each, totaling 100 hours. If automation leaves "
                    "250 records requiring four minutes of review, plus ten hours of exception "
                    "handling and maintenance, remaining work is 26.67 hours: a 73.33% reduction. "
                    "That meets the 70% objective without pretending human authorization disappeared. "
                    "Also measure qualification precision, settlements reconciled before due dates, "
                    "and dollars exposed to unresolved exceptions. A pipeline that saves time but "
                    "increases overdue balances has failed. Use idempotency keys for every state "
                    "transition, distinguish ingestion time from commercial effective time, and "
                    "retain an append-only event history. A daily dashboard should show stale "
                    "commitments, parcels without acceptance scans, unmatched ACH credits, and "
                    "rewards awaiting eligibility confirmation. When a connector breaks, a "
                    "documented CSV import must preserve the same identifiers and validation rules. "
                    "Manual recovery should change the transport, not weaken the evidence needed "
                    "to commit capital or recognize earnings."
                ),
            ],
            "table": {
                "caption": "Eleven mapped operating applications, with unit math and recovery boundaries",
                "headers": [
                    "Mapped operating play",
                    "Automation and evidence boundary",
                    "Illustrative unit economics",
                    "Human check and fallback",
                ],
                "rows": [
                    [
                        "telegram_channel_signal_scraping converts permitted broadcasts into qualified deal signals",
                        "Read permitted public messages without harvesting participant identities",
                        "Two dollars processing divided by twenty qualified signals equals ten cents",
                        "Stop uncertain access and capture inbound through utility bots",
                    ],
                    [
                        "Commitment normalization converts accepted wholesale offers into structured records",
                        "Extract accepted quantities and expiration with exact evidence spans",
                        "Thirty dollars processing across three hundred commitments equals ten cents",
                        "Operator verifies binding terms before any purchase is released",
                    ],
                    [
                        "Wholesale qualification matches product identifiers against accepted buying instructions",
                        "Compare SKU condition quantity destination and acceptance deadline",
                        "One prevented fifty-dollar mismatch covers five hundred ten-cent checks",
                        "Conflicting identifiers require supplier clarification instead of inferred matches",
                    ],
                    [
                        "Shipment reconciliation joins carrier scans with warehouse receiving evidence",
                        "Match tracking identifiers carton counts serials and receiving timestamps",
                        "Twenty dollars processing across two hundred parcels equals ten cents",
                        "Missing acceptance scans trigger carrier investigation and purchase suspension",
                    ],
                    [
                        "Portal routing compares eligible alternatives without assuming simultaneous stacking",
                        "Store exclusions click evidence caps and eligible purchase category",
                        "One thousand eligible dollars at one percent yields ten dollars",
                        "Use one qualifying portal path and exclude disputed rewards",
                    ],
                    [
                        "Card offer routing selects eligible commercial payment instruments",
                        "Validate issuer terms merchant category limits and statement dates",
                        "One thousand eligible dollars at two percent yields twenty dollars",
                        "Skip rewards assumptions when issuer eligibility remains unresolved",
                    ],
                    [
                        "Invoice fee screening rejects negative payment-service reward spreads",
                        "Compare current Plastiq or Melio fees against permitted rewards",
                        "Ten thousand dollars earns two hundred against hypothetical fees of two hundred ninety",
                        "Use ordinary ACH when the card route loses ninety dollars",
                    ],
                    [
                        "Statement liability scheduling forecasts repayment from cleared available cash",
                        "Join actual statement due dates with dated cash obligations",
                        "Twenty thousand dollars due remains twenty thousand dollars payable",
                        "Pause commitments when reserves cannot cover stressed settlement delays",
                    ],
                    [
                        "Treasury sweep scheduling invests only verified surplus repayment capacity",
                        "Match bill maturity and bank availability against liability calendar",
                        "Ten thousand at four-point-five percent for forty-five days yields fifty-five dollars forty-eight cents",
                        "Keep repayment reserves liquid rather than relying on early sales",
                    ],
                    [
                        "Inbound utility distribution converts useful calculators into submitted requirements",
                        "Attribute public resource visits to voluntarily completed qualification forms",
                        "Three hundred dollars divided by ten commitments equals thirty dollars",
                        "Remove misleading calculators and route incomplete submissions to review",
                    ],
                    [
                        "Settlement attribution reconciliation connects growth spend with earned contribution",
                        "Join cleared reimbursements vested rewards and completed treasury earnings",
                        "Thirty-five dollars contribution less thirty dollars acquisition leaves five dollars",
                        "Stop scaling when unresolved disputes erase measured acquisition payback",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make evidence cheaper than exception chasing",
                "body": "Preserve the small artifacts that determine whether an apparent spread survives receiving, settlement, and reward review.",
                "items": [
                    "Archive the accepted commitment and destination instructions together; a later edited deal message must not rewrite the original purchasing limit.",
                    "Capture portal exclusions and the qualifying click before checkout; a missing tracked transaction is an exception, not earned cash.",
                    "Match parcel serials and carton weights before dispatch, then retain delivery and warehouse acceptance as separate events.",
                    "Publish rounded, synthetic calculator examples; keep current counterparties, committed quantities, and account-specific offers outside public growth assets.",
                ],
            },
        },
        {
            "heading": "2. Route purchases through three separate unit-economic engines",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Wholesale fulfillment starts with a pre-committed buyer, not a speculative cart. "
                    "Consider a deliberately simplified accepted order: merchandise costs $1,000, "
                    "the buying group reimburses $1,020, insured shipping costs $12, and the "
                    "expected return or damage provision is $3. Wholesale contribution is $5 "
                    "before overhead. An independently eligible 2% commercial card reward adds "
                    "$20, and a qualifying 1% portal reward adds $10, producing $35 combined "
                    "contribution only when those rewards become earned under their terms. Keep "
                    "the $1,020 reimbursement, $1,000 merchandise cost, and separate $30 reward "
                    "components visible; do not call reimbursement or borrowed purchasing capacity "
                    "profit. This transaction illustration is not the canonical portfolio's 35% "
                    "retained-share assumption. A DE, NH, or OR warehouse address does not itself "
                    "establish every exemption for every seller or transaction. Validate destination "
                    "treatment, resale documentation where relevant, title transfer, and actual "
                    "warehouse acceptance requirements. Washington RCW 82.04.470 illustrates the "
                    "importance of substantiated wholesale treatment rather than an unsupported "
                    "resale assertion. Reject any order whose shipping, tax, or receiving conditions "
                    "consume the spread. Route uncertain tax treatment to a documented decision "
                    "before purchase, rather than allowing a scraper to treat a promotional "
                    "headline as the governing commercial terms."
                ),
                (
                    "The rebate router compares Rakuten and TopCashback as alternative qualifying "
                    "portal paths, then tests whether a commercial card reward or card-linked "
                    "offer can coexist with the selected path. Do not add two portal rates for "
                    "one purchase or presume every gift card, business purchase, coupon, or bulk "
                    "order qualifies. Store merchant exclusions, category restrictions, caps, "
                    "activation requirements, return windows, and the terms snapshot used in the "
                    "decision. Treat uncapped 2% to 4% rewards as a candidate eligibility range, "
                    "not a universal issuer promise. For a B2B invoice routed through Plastiq "
                    "or Melio, illustrative $10,000 principal at a 2% reward earns $200; an "
                    "assumed 2.9% processing charge costs $290, leaving a $90 loss before any "
                    "other cost. These are hypothetical inputs, not current vendor quotations. "
                    "With equal eligible principal, the reward rate must exceed the fee rate "
                    "plus incremental costs merely to break even. Model financed fees separately "
                    "if they increase the statement balance. Require an authentic invoice, an "
                    "eligible recipient, and permitted card usage. Default to ordinary bank "
                    "payment when economics fail. Do not rescue a negative payment spread by "
                    "counting unconfirmed bonuses, repeatedly recycling limits, or assuming "
                    "issuer review will never interrupt availability."
                ),
                (
                    "Treasury income is the third engine: interest, bill discount accretion, and "
                    "earned bank bonuses belong here, while swept principal remains an asset "
                    "matched against repayment liabilities. An illustrative $10,000 genuinely "
                    "available for 45 days at a simple annualized 4.5% produces $55.48 using "
                    "principal times rate times days divided by 365. Actual Treasury pricing "
                    "and yield conventions determine realized earnings; this calculation is a "
                    "planning approximation, not a quoted bill return. Subtract transfer charges, "
                    "funding costs, and any sale loss. Record bonus eligibility periods separately "
                    "so the same cash is not simultaneously assumed available for a locked "
                    "deposit and a card payment. At portfolio level, retain the canonical Formula "
                    "v2.0 cases exactly: $250,000, $1,025,000, and $1,800,000 gross bases yield "
                    "$87,500, $358,750, and $630,000 at retained_share=0.35. Owner profits are "
                    "$20,000, $143,500, and $360,000. Residual costs after retained contribution "
                    "are therefore $67,500, $215,250, and $270,000; do not equate that entire "
                    "residual with monthly operating overhead. Retained margins are 22.86%, "
                    "40.0%, and 57.14%. The retained view distinguishes contribution from gross "
                    "flows; actual ASC 606 gross-versus-net presentation depends on principal-agent "
                    "facts and contract obligations, not merely applying the scorecard percentage."
                ),
            ],
            "table": {
                "caption": "Separate economic ledgers and canonical Formula v2.0 reconciliation",
                "headers": [
                    "Economic component or scenario",
                    "Gross movement and classification",
                    "Retained contribution or profit bridge",
                    "Automation decision and evidence requirement",
                ],
                "rows": [
                    [
                        "Wholesale example preserves reimbursement and merchandise cost separately",
                        "Buyer reimburses one thousand twenty against one thousand merchandise dollars",
                        "Twelve shipping dollars and three reserve dollars leave five",
                        "Release purchase only against accepted commitment and verified destination",
                    ],
                    [
                        "Commercial rewards example requires two independently qualifying reward sources",
                        "One thousand eligible purchase dollars supports twenty plus ten rewards",
                        "Thirty earned reward dollars supplement five wholesale contribution dollars",
                        "Exclude pending rewards from cash available for statement repayment",
                    ],
                    [
                        "Treasury example uses surplus cash without erasing repayment obligations",
                        "Ten thousand principal remains an asset rather than earned revenue",
                        "Forty-five days at four-point-five percent approximates fifty-five dollars forty-eight cents",
                        "Verify maturity settlement and transfer timing before allocating funds",
                    ],
                    [
                        "Conservative canonical case maintains one employee plus two contractors",
                        "Annual gross basis equals exactly two hundred fifty thousand dollars",
                        "Retained $87,500 less $67,500 residual costs yields $20,000 profit",
                        "Report eight percent gross margin and 22.86 percent retained margin",
                    ],
                    [
                        "Base canonical case maintains one employee plus two contractors",
                        "Annual gross basis equals exactly one million twenty-five thousand dollars",
                        "Retained $358,750 less $215,250 residual costs yields $143,500 profit",
                        "Report fourteen percent gross margin and forty percent retained margin",
                    ],
                    [
                        "Scaled canonical case requires two employees plus three contractors",
                        "Annual gross basis equals exactly one million eight hundred thousand dollars",
                        "Retained $630,000 less $270,000 residual costs yields $360,000 profit",
                        "Report twenty percent gross margin and 57.14 percent retained margin",
                    ],
                ],
            },
        },
        {
            "heading": "3. Stress repayment timing and recover failed automations without duplicate spending",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat 55-day statement float as an upper-bound scenario available only when "
                    "purchase timing and the issuer's actual terms support it. Store the posted "
                    "transaction date, statement closing date, due date, grace conditions, and "
                    "scheduled payment date for each account. A purchase near closing may have "
                    "substantially less runway. Net-3 or Net-5 buying-group language also needs "
                    "an explicit starting event: carrier delivery, warehouse acceptance, or "
                    "approved reconciliation can produce different settlement dates. Forecast "
                    "cash from cleared ACH, not a dashboard marked paid. Suppose $20,000 is due "
                    "on day 55 and reimbursement is expected on day 10. Stress warehouse "
                    "acceptance slipping seven days, payout slipping fifteen more, and bank "
                    "availability slipping three, moving usable reimbursement to day 35. Then "
                    "stress a dispute extending beyond day 55. The reserve must still cover "
                    "the full $20,000 plus payment charges; an expected reimbursement is not "
                    "a substitute for that reserve. Schedule repayment several business days "
                    "early using the account's verified processing rules. Treasury bills should "
                    "mature with transfer slack before payment, and emergency coverage must "
                    "not depend on selling a bill at a favorable price. Suspend new "
                    "commitments immediately when stressed coverage falls below scheduled obligations."
                ),
                (
                    "Use a durable state machine: observed, qualified, committed, ordered, shipped, "
                    "accepted, reimbursed, and closed. Reward and treasury events follow separate "
                    "linked states because their completion dates differ. Verify documented webhook "
                    "signatures where available, enforce replay windows, and acknowledge receipt "
                    "only after persisting the event. For integrations without signed delivery, "
                    "retrieve corroborating evidence through authenticated exports before advancing "
                    "money-sensitive states. A sqlite3 prototype can use unique event keys and "
                    "transactions; higher write concurrency may require a managed database rather "
                    "than forcing the prototype beyond its operating envelope. Keep payment "
                    "instructions out of LLM outputs. The model can recommend an exception "
                    "classification but cannot alter beneficiary details or release money. Retry "
                    "read operations with bounded exponential backoff; never blindly repeat an "
                    "order or transfer after a timeout. First query its external reference, "
                    "then require a person to resolve ambiguous completion. Dead-letter records "
                    "need an owner, next action, and due time. If issuer review freezes an "
                    "account, stop that account's new purchases and preserve its repayment "
                    "schedule; do not redirect transactions to bypass the restriction. If a "
                    "parcel disappears, freeze expected reimbursement, preserve serial and insurance "
                    "evidence, and open the carrier claim within the applicable deadline."
                ),
                (
                    "Budget automated runs using explicit assumptions rather than calling model "
                    "usage negligible. At assumed prices of $0.50 per million input tokens "
                    "and $2 per million output tokens, a 2,000-input, 300-output extraction "
                    "costs $0.0016. Adding $0.0034 for hosting, storage, and monitoring produces "
                    "$0.005 per normal run, or $50 for 10,000 runs. These are budgeting "
                    "inputs, not a vendor price claim. If 8% require two minutes of "
                    "review at $30 per hour, review adds $800; fully loaded processing is "
                    "$850, or $0.085 per run before development and maintenance. Track retries "
                    "and multi-message documents because they increase token consumption. Route "
                    "deterministic fields through regular parsing first, and reserve model calls "
                    "for ambiguous language. Maintain a labeled evaluation set covering changed "
                    "quantities, expired commitments, portal exclusions, and suspicious payment "
                    "instructions. A model or prompt update must match critical-field accuracy "
                    "before production replacement. Log extracted values and evidence references "
                    "without storing unnecessary personal data. Retain raw artifacts according "
                    "to a documented access and retention schedule. The operator samples successful "
                    "runs as well as exceptions: silent systematic errors often look clean "
                    "until a warehouse rejects an entire batch or a reward program reverses "
                    "multiple transactions together."
                ),
            ],
            "table": {
                "caption": "Failure recovery matrix for commitments, parcels, rewards, and statement liabilities",
                "headers": [
                    "Failure signal requiring intervention",
                    "Automated containment and evidence capture",
                    "Human recovery action and ownership",
                    "Restart condition tied to observable evidence",
                ],
                "rows": [
                    [
                        "Commitment expiration arrives before purchase confirmation becomes available",
                        "Block order creation and preserve original accepted offer evidence",
                        "Procurement contractor requests renewed quantity and price confirmation",
                        "Operator verifies refreshed acceptance before releasing another purchase instruction",
                    ],
                    [
                        "Carrier delivery appears without matching warehouse acceptance records",
                        "Freeze expected settlement date and collect parcel tracking history",
                        "Fulfillment contractor submits serial carton and receiving evidence",
                        "Warehouse acceptance resolves quantity differences and establishes settlement timing",
                    ],
                    [
                        "Buying group marks payment sent without cleared ACH credit",
                        "Exclude pending funds from available repayment and treasury balances",
                        "Reconciliation contractor investigates reference identifiers with the counterparty",
                        "Bank evidence confirms usable funds and matching settlement amount",
                    ],
                    [
                        "Issuer review restricts account purchasing or available credit",
                        "Disable new purchase routing while preserving existing liability forecasts",
                        "Full-time operator answers issuer requests through authenticated account channels",
                        "Issuer confirms permitted account use and repayment coverage remains intact",
                    ],
                    [
                        "Transfer request times out after submission to external service",
                        "Mark completion ambiguous and suppress automatic duplicate transfer attempts",
                        "Operator checks external reference and reconciles actual account movements",
                        "Confirmed transfer status supports one documented subsequent action only",
                    ],
                    [
                        "Portal tracking disappears or rewards reverse after return review",
                        "Remove provisional reward contribution and recalculate actual purchase economics",
                        "Reconciliation contractor submits permitted evidence through official support routes",
                        "Posted reward or documented rejection closes the outstanding exception",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before consequential execution",
                "body": "Automation prepares evidence; a named person authorizes commitments, changed payment details, and transfers.",
                "items": [
                    "Verify accepted SKU, quantity, price, warehouse address, and expiration against the original buying-group commitment before ordering.",
                    "Verify current card and portal eligibility, fee assumptions, and a positive standalone contribution calculation before selecting a payment route.",
                    "Verify stressed cleared-cash coverage for every statement due date, including disputed reimbursements and transfer delays, before any treasury sweep.",
                    "Verify beneficiary details through an established authenticated channel and inspect external transaction status before releasing or retrying a transfer.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture and validate evidence",
                    "action": "Persist source records, normalize identifiers, and reject unsupported commercial fields.",
                    "detail": "Use unique source keys, timestamped terms snapshots, and decimal amounts; route conflicting records into an owned exception queue.",
                },
                {
                    "step": 2,
                    "title": "Calculate independent economic and liquidity tests",
                    "action": "Compute wholesale contribution, eligible rewards, treasury earnings, and stressed statement coverage separately.",
                    "detail": "Exclude pending rewards and uncleared reimbursements from repayment cash; reject negative invoice fee spreads.",
                },
                {
                    "step": 3,
                    "title": "Authorize and execute once",
                    "action": "Present the evidence bundle to the authorized operator before consequential execution.",
                    "detail": "Bind authorization to the exact quantities, amounts, recipient, and terms; changed inputs require renewed authorization.",
                },
                {
                    "step": 4,
                    "title": "Reconcile and learn from exceptions",
                    "action": "Match receiving, cleared ACH, posted rewards, and repayment evidence before closing records.",
                    "detail": "Feed resolved exception labels into evaluations and operating rules without allowing model-generated changes to deploy themselves.",
                },
            ],
        },
        {
            "heading": "4. Scale distribution from verified contribution rather than vanity traffic",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build distribution around useful operating artifacts, not claims of effortless "
                    "card-funded income. A public shipping-loss calculator, statement-date planner, "
                    "or portal fee comparison can attract suppliers and authorized wholesale "
                    "participants without revealing private commitments. Programmatic pages should "
                    "answer distinct questions with maintained inputs, methodology, and worked "
                    "examples; do not publish thousands of near-identical pages generated from "
                    "unverified rates. A Telegram utility bot can return a user-requested "
                    "eligibility worksheet and offer a shareable result stripped of identifying "
                    "details. Sharing must be user-initiated, with no automatic messages to contacts. "
                    "Outbound targets should come from legitimate business directories or direct "
                    "relationships, not harvested community membership. For commercial email, "
                    "15 U.S.C. 7704 requires truthful routing information, nondeceptive subjects, "
                    "required identification and address disclosures, and a working opt-out "
                    "mechanism with timely honoring of requests. Store suppression records across "
                    "all campaigns. Keep buying-group procurement, rebate education, and treasury "
                    "tools visibly distinct so a supplier inquiry does not become an implied "
                    "invitation to finance unrelated activity. The flywheel is specific: useful "
                    "tool, voluntarily submitted requirement, qualified opportunity, settled outcome, "
                    "and an anonymized improvement to the tool. Growth earns another iteration "
                    "only when settlement data confirms that the acquired opportunity contributed "
                    "more than its acquisition and servicing cost."
                ),
                (
                    "Instrument the funnel through settled commitments rather than stopping at "
                    "clicks. Suppose a monthly utility campaign costs $300 and produces 100 "
                    "voluntary submissions, 20 qualified opportunities, and ten accepted, settled "
                    "orders. Acquisition cost is $3 per submission, $15 per qualified opportunity, "
                    "and $30 per settled order. If each order earns the earlier illustrative "
                    "$35 combined contribution, the cohort produces $350 before acquisition "
                    "and $50 afterward, before handling labor and overhead. At ten minutes "
                    "of servicing per order and $30 per hour, labor consumes the remaining "
                    "$50. The campaign therefore has no residual contribution in this example; "
                    "higher traffic alone cannot fix it. Improve qualification or repeat-order "
                    "retention before increasing spend. Attribute repeat orders conservatively "
                    "and cap projected customer value until repeated settlements exist. Referral "
                    "benefits should be explicit operating costs and payable only after the "
                    "defined qualifying outcome. Never condition them on exposing another "
                    "person's account information. Compare channels using contribution after "
                    "returns, denied rewards, shipping disputes, and review labor. Publish "
                    "weekly cohort tables with acquisition month and settlement maturity, "
                    "because a young cohort with pending reversals will otherwise appear "
                    "stronger than an older cohort whose losses have already arrived."
                ),
                (
                    "Scale only after operational capacity and economic evidence agree. The "
                    "canonical Base case remains one full-time operator plus two contractors; "
                    "the Scaled case explicitly expands to two full-time people plus three "
                    "contractors. Do not present $360,000 owner profit as a proven three-person "
                    "outcome. Startup capital of $10,000 to $55,000 and monthly operating "
                    "overhead of $1,500 to $9,000 are planning ranges, not substitutes for "
                    "a dated repayment reserve calculation. First-deal timing remains one "
                    "to three months. Before increasing throughput, inspect counterparty "
                    "concentration, outstanding uninsured exposure, stale receiving records, "
                    "and the age distribution of unpaid reimbursements. Diversifying across "
                    "vetted Net-3 and Net-5 counterparties reduces dependence but does not "
                    "turn their receivables into cash. Preserve the record chain needed "
                    "to reconcile payment reporting under 26 U.S.C. 6050W and property "
                    "basis under 26 U.S.C. 1012. Classify purchase-linked adjustments "
                    "separately from service compensation and bank interest; do not assume "
                    "every reward has identical tax treatment. Reconcile applicable payment "
                    "reports against returns, fees, and ledger categories rather than "
                    "treating reported payment volume as owner income. The durable advantage "
                    "is an evidence-rich operating history that improves routing, qualification, "
                    "and recovery while keeping principal, revenue, contribution, and profit "
                    "distinct at every stage."
                ),
            ],
            "table": {
                "caption": "Distribution flywheel scorecard tied to settlement and contribution",
                "headers": [
                    "Distribution loop and intended audience",
                    "Useful asset and permitted acquisition route",
                    "Measurement linked to actual unit economics",
                    "Failure boundary and corrective operating action",
                ],
                "rows": [
                    [
                        "Public calculator attracts operators researching shipment and payment economics",
                        "Publish synthetic examples with dated inputs and transparent calculations",
                        "Track qualified submissions rather than treating page impressions as demand",
                        "Withdraw stale rate examples until verified inputs replace them",
                    ],
                    [
                        "Telegram utility bot captures voluntarily initiated wholesale qualification requests",
                        "Return requested worksheets without collecting unrelated community member identities",
                        "Measure processing cost per submitted and accepted buying requirement",
                        "Disable unsolicited messaging and retain user-controlled sharing mechanics",
                    ],
                    [
                        "Targeted business outreach connects legitimate suppliers with documented requirements",
                        "Use relevant business contacts and maintain centralized email suppression",
                        "Compare outreach labor and tooling against settled cohort contribution",
                        "Stop campaigns generating irrelevant responses or repeated recipient objections",
                    ],
                    [
                        "Referral loop rewards genuinely completed and documented commercial introductions",
                        "Explain reward conditions and request introductions without private account data",
                        "Deduct referral expense before calculating acquired order contribution",
                        "Withhold unearned referral payments when qualifying settlement remains incomplete",
                    ],
                    [
                        "Repeat-order loop reduces acquisition cost through reliable fulfillment history",
                        "Offer verified counterparties updated capacity and accepted product requirements",
                        "Count repeat contribution only after receiving and settlement evidence",
                        "Reduce allocations when counterparty payment aging exceeds operating limits",
                    ],
                    [
                        "Programmatic resource loop improves tools using anonymized resolved exceptions",
                        "Publish distinct maintained explanations instead of repetitive generated landing pages",
                        "Measure useful engagement together with mature cohort contribution",
                        "Remove private identifiers and review every consequential public calculation",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Automate the evidence trail, not the assumption that tomorrow's reimbursement can pay today's liability.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create separate wholesale, reward, and treasury ledgers with shared deal identifiers and explicit principal-versus-income classifications.",
        "Implement permitted Telegram signal intake and an inbound utility bot without collecting channel member lists or sending unsolicited messages.",
        "Build the commitment-to-settlement state machine with unique event keys, evidence snapshots, human authorization, and a validated CSV recovery path.",
        "Stress every statement due date against delayed acceptance, delayed ACH, disputed parcels, issuer restrictions, and Treasury transfer timing.",
        "Measure automated-run cost, review minutes, retry volume, and exception-adjusted labor reduction against a documented two-week baseline.",
        "Scale acquisition only after mature cohorts show positive contribution after shipping losses, reward reversals, review labor, and channel costs.",
    ],
    "statutory_citations": [
        {
            "title": "26 U.S.C. 6050W — Returns relating to payments made in settlement of payment card and third party network transactions",
            "url": "https://www.law.cornell.edu/uscode/text/26/6050W",
            "relevance": "Reconcile applicable payment reporting with transaction ledgers; reported settlement volume is not equivalent to owner profit.",
        },
        {
            "title": "26 U.S.C. 1012 — Basis of property: cost",
            "url": "https://www.law.cornell.edu/uscode/text/26/1012",
            "relevance": "Preserve acquisition-cost and adjustment records supporting merchandise basis rather than collapsing reimbursements and rewards into one cash total.",
        },
        {
            "title": "Washington RCW 82.04.470 — Wholesale sale, reseller permit, and taxability presumption",
            "url": "https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.470",
            "relevance": "Apply the jurisdiction's actual wholesale substantiation requirements; a warehouse destination alone does not replace required resale evidence.",
        },
        {
            "title": "15 U.S.C. 7704 — Other protections for users of commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Configure commercial outreach with truthful headers, nondeceptive subjects, required disclosures, a valid postal address, and timely opt-out handling.",
        },
        {
            "title": "12 CFR 330.3 — General principles of deposit insurance",
            "url": "https://www.ecfr.gov/current/title-12/chapter-III/subchapter-B/part-330/section-330.3",
            "relevance": "Evaluate bank sweep balances using applicable depositor, ownership-category, and insured-bank aggregation rules rather than assuming every account receives separate coverage.",
        },
    ],
}
