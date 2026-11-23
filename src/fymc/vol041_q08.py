from __future__ import annotations

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "public-records-apis-data-pipelines-and-operator-tooling",
    "question_prompt": "Which exact public registries, government databases, commercial APIs, enrichment waterfalls, and diagnostic tools give a small buying group, card-float & ticket allocation arbitrage desk an unfair information edge?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Public Records, APIs, Data Pipelines & Operator Tooling",
    "subtitle": "Secretary-of-State Records, UCC Searches, Ticketmaster Discovery, SkyBox, Card Settlement Ledgers, and BOTS Act-Safe Allocation Intelligence",
    "layout_template": "resource_directory",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #41, ranked #09 of 42 with a 93/100 Money-to-Manpower Score, turns "
        "verified commitments, settlement timing, and transferable inventory into a small-team "
        "information advantage. This chapter maps 11 operator plays to public records, contracted "
        "feeds, and auditable ledgers, including the supplied sportsbook promo-conversion play "
        "with its certainty claims corrected. Eighteen named resources support counterparty "
        "screening, card reconciliation, event identity, shipment evidence, and resale-rule checks. "
        "Formula v2.0 produces annual owner profits of $20,000 Conservative, $143,500 Base, "
        "and $360,000 Scaled. Those profits reconcile against a 35% retained spread, not "
        "merchant purchase volume or customer betting turnover. Build read-only ingestion first; "
        "release purchases and listings only when identifiers, cash dates, transfer rights, and "
        "exception ownership reconcile."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross scorecard basis; $87,500 retained revenue at 35%.",
            "note": "8% gross-basis net margin; 22.86% retained margin; $20,000 owner profit; 1 FT + 2 C.",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross scorecard basis; $358,750 retained revenue at 35%.",
            "note": "14.0% gross-basis net margin; 40.0% retained margin; $143,500 owner profit; 1 FT + 2 C.",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross scorecard basis; $630,000 retained revenue at 35%.",
            "note": "20% gross-basis net margin; 57.14% retained margin; $360,000 owner profit; 2 FT + 3 C.",
        },
    ],
    "sections": [
        {
            "heading": "1. Build an evidence waterfall before extending counterparty exposure",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with an evidence waterfall, not a purchased contact list. For each buying "
                    "group, capture the contracting entity, formation jurisdiction, filing number, "
                    "remittance instructions, authorized signer, and a purchase-order acceptance that "
                    "names the merchandise and rejection rules. Search the formation registry first; "
                    "then search applicable UCC records under the exact debtor name and appropriate "
                    "filing jurisdiction. A registered entity can still be insolvent, and a financing "
                    "statement describes a claimed security interest rather than a current payoff "
                    "balance. Review sanctions results using identifying attributes instead of "
                    "treating a similar name as a definitive match. Ask the counterparty for resale "
                    "documentation and verify it through the relevant state's available process. "
                    "Bank-account ownership and payout reliability require separate evidence; neither "
                    "a Secretary-of-State record nor a SAM registration establishes them. Obtain "
                    "payment changes through a callback to a previously verified contact, never "
                    "through the changed email thread alone. Store the source URL, retrieval time, "
                    "document hash, reviewer, and next review date. When a portal offers only "
                    "interactive search, use a documented manual lookup rather than inventing an "
                    "API or scraping around access restrictions. An unavailable registry becomes "
                    "an open exposure exception, not a fabricated clean result."
                ),
                (
                    "The chapter's eleven mapped plays are committed buying-group fulfillment, "
                    "counterparty routing, commercial-card rebates, statement-float scheduling, "
                    "insured shipment recovery, secondary-ticket resale, event-decay repricing, "
                    "stadium seat-license brokerage, corporate-suite allocation, resale-tax "
                    "reconciliation, and sportsbook promo conversion. These are operating mappings, "
                    "not additional catalog identifiers. Give each play a measurable unit and a "
                    "source that can contradict the trade thesis. A committed order for ten units "
                    "at $500 creates $5,000 of purchase exposure before shipping; an accepted order "
                    "is not settled cash. Routing two such orders to different buyers reduces "
                    "single-buyer exposure to $5,000 each but does not remove correlated ACH delays. "
                    "A valid exemption on a $10,000 taxable purchase at an illustrative 8% rate "
                    "avoids an $800 acquisition tax payment; it is not automatically $800 of revenue. "
                    "If documentation fails, price the actual tax treatment or decline the order. "
                    "For Net-3 and Net-5 buyers, define when the clock starts: carrier delivery, "
                    "inspection acceptance, or invoice approval can produce materially different "
                    "cash dates. Record settlement percentiles from the desk's own receipts and "
                    "cap new commitments against the slower observed outcome. Public records "
                    "support identity; historical settlements determine usable credit capacity."
                ),
                (
                    "Run enrichment in increasing order of expense and sensitivity. Normalize "
                    "the entity name and address, resolve the official filing identifier, retrieve "
                    "relevant filings, request the signed contract and resale certificate, then "
                    "validate payout changes and insurer eligibility. Stop when a material mismatch "
                    "appears; purchasing another commercial profile cannot repair conflicting "
                    "contracting names. Use domain and telephone checks only as corroboration, "
                    "because a polished website and working number are inexpensive to create. "
                    "For ticket activity, resolve the event's jurisdiction and resale channel before "
                    "checking licensing, transfer conditions, and mandatory price disclosures. "
                    "For sportsbook activity, check the state regulator's current authorized-operator "
                    "list and participant eligibility rather than assuming a familiar national "
                    "brand operates everywhere. The nine official resources below form the first "
                    "half of an eighteen-resource directory. Their freshness entries distinguish "
                    "the desk's polling schedule from the publisher's update timing. A daily "
                    "lookup does not make a filing real-time. Preserve the actual record date "
                    "and mark stale evidence explicitly. Maintain a source register recording "
                    "access rights, contractual restrictions, fee schedules, and the last successful "
                    "retrieval. Review that register monthly and before entering a new state "
                    "or adding an unfamiliar settlement rail."
                ),
            ],
            "table": {
                "caption": "Official evidence directory, resources 1–9: identity, liens, tax, resale, and gaming",
                "headers": [
                    "Named resource and specific operating purpose",
                    "Exact access method and cost tier",
                    "Refresh latency and desk review schedule",
                    "Rate-limit hygiene and usable fallback evidence",
                ],
                "rows": [
                    [
                        "Delaware Division of Corporations Entity Search verifies formation identity, not repayment capacity.",
                        "Open https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx; basic entity lookup is free, while document products carry fees.",
                        "Read the displayed record status before onboarding; request current certificates when contract exposure warrants them.",
                        "Use the interactive search manually; if unavailable, obtain certified documents and verify them when service resumes.",
                    ],
                    [
                        "New York Department of State Corporation and Business Entity Database resolves New York contracting entities.",
                        "Use https://apps.dos.ny.gov/publicInquiry/ for free public searches; order official document copies separately when required.",
                        "Recheck before first funding and material contract changes; registry publication timing controls underlying freshness.",
                        "Avoid automated form hammering; request filed documents directly and retain a dated manual search worksheet.",
                    ],
                    [
                        "New York Department of State UCC records reveal indexed financing statements for applicable debtor searches.",
                        "Start at https://dos.ny.gov/uniform-commercial-code; follow official search instructions and budget published search or copy fees.",
                        "Search before extending exposure and after material credit events; filing and indexing delays remain relevant.",
                        "Use exact debtor names and proper jurisdiction; obtain official searches when portal access or indexing creates ambiguity.",
                    ],
                    [
                        "OFAC Sanctions List Search supports sanctions screening with identity-based review of potential matches.",
                        "Use https://sanctionssearch.ofac.treas.gov/ or published list downloads; public search and list access are free.",
                        "Refresh against newly published lists and before material new relationships; record the actual list version used.",
                        "Cache downloaded lists instead of repeating searches; resolve matches using official identifiers and published program information.",
                    ],
                    [
                        "SAM.gov Entity Information and Exclusions provide federal-registration context and federal exclusion records.",
                        "Use https://sam.gov/ public search; API access requires its documented account and key arrangements.",
                        "Review at onboarding when relevant; capture source timestamps because federal status does not measure private-buyer solvency.",
                        "Follow the account's documented API quota; use manual public search and contracting documents when API retrieval fails.",
                    ],
                    [
                        "New York Tax Department Certificate of Authority lookup checks seller-registration evidence within its stated scope.",
                        "Begin at https://www.tax.ny.gov/bus/st/register.htm and follow official sales-tax vendor lookup links; public guidance is free.",
                        "Verify registration when onboarding and revisit certificate changes; retain the dated exemption document separately.",
                        "Respect interactive access controls; use department confirmation procedures and completed ST-120 documentation where applicable.",
                    ],
                    [
                        "Federal Trade Commission Fees Rule materials explain mandatory fee disclosure for live-event ticket offers.",
                        "Read https://www.ftc.gov/legal-library/browse/rules/rule-unfair-or-deceptive-fees and linked rule text; official materials are free.",
                        "Review current text before launching pricing changes and monitor amendments; the rule is not an inventory feed.",
                        "Cache dated rule copies without excessive requests; reconcile interpretation against current 16 CFR Part 464.",
                    ],
                    [
                        "New York Department of State Ticket Reseller materials identify licensing procedures and related operating requirements.",
                        "Open https://dos.ny.gov/ticket-reseller; public instructions are free, while licensing carries the published application charges.",
                        "Review before serving the jurisdiction and each renewal; confirm actual license status through the official process.",
                        "Use linked official services as documented; request department confirmation when online evidence does not establish current status.",
                    ],
                    [
                        "New York State Gaming Commission sports-wagering materials identify authorized activity and regulator-issued operating information.",
                        "Use https://gaming.ny.gov/ and navigate to sports wagering; public operator information requires no subscription.",
                        "Check before participant onboarding and new operator use; retain publication dates rather than assuming continuous updates.",
                        "Use normal page retrieval with caching; confirm ambiguity through regulator publications before allowing participant activity.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Buy better evidence before buying more inventory",
                "body": "The strongest small-desk advantages come from precise exceptions that competitors overlook.",
                "items": [
                    "Keep separate Net-3 clocks for delivery, inspection, and accepted invoice; negotiate the actual trigger into every buying-group commitment.",
                    "Match the purchase-order entity, insured consignee, invoice recipient, and remitting entity before allowing third-party payout instructions.",
                    "Track lien-search jurisdiction and debtor-name spelling alongside results; an inexpensive search under the wrong name can create false comfort.",
                    "Export event-transfer restrictions and seller payout schedules before purchasing; a profitable ticket can still create an unfinanceable settlement gap.",
                ],
            },
        },
        {
            "heading": "2. Connect contracted inventory feeds without mistaking access for trading rights",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use Ticketmaster Discovery to identify events, venues, attractions, and "
                    "published event status, not to obtain privileged inventory or bypass ticket "
                    "purchase controls. Its developer key and documented endpoints provide metadata "
                    "within the account's permitted limits; availability of a discovery record says "
                    "nothing about transferable ownership. Resolve the venue, local start time, "
                    "timezone, event identifier, seating description, and postponement status before "
                    "merging a seller's stock. Then connect SkyBox or Automatiq only through the "
                    "commercial access actually granted to the desk. Product names do not establish "
                    "API entitlement, exchange coverage, webhook availability, or a guaranteed "
                    "synchronization interval. Obtain written interface documentation and test "
                    "listing creation, cancellation, partial fills, and duplicate delivery in a "
                    "nonproduction workflow where offered. A $150 ticket sale against $100 face "
                    "basis, a $22.50 selling fee, and $5 fulfillment cost leaves $22.50 before "
                    "shared operating costs. If the same seat sells twice, replacement costs can "
                    "erase many such units. Assign each owned ticket a stable inventory key and "
                    "lock that key while a sale is being resolved. When feed freshness exceeds "
                    "the desk's threshold, suspend affected listings rather than treating cached "
                    "availability as permission to continue selling."
                ),
                (
                    "Card tooling must distinguish authorization, posting, statement close, payment "
                    "due, rebate accrual, and rebate receipt. A transaction feed can help reconcile "
                    "merchant spend, but it does not establish a universal sixty-day interest-free "
                    "period. Actual usable float depends on purchase timing, issuer terms, grace "
                    "eligibility, and payment execution. On $10,000 of qualifying spend, a contractual "
                    "3% rebate contributes $300 before fees, exclusions, returns, and issuer "
                    "adjustments. An illustrative 40-day funding alternative at 12% simple annual "
                    "cost is $131.51, calculated as $10,000 multiplied by 0.12 and 40/365. That "
                    "avoided cost is a comparison, not an additional cash rebate to book. Stress "
                    "the ledger for an ACH receipt arriving after the card due date, an issuer "
                    "review that freezes new spending, and a reward reversal after a return. "
                    "Use statement exports as the final payment-schedule reference and bank "
                    "settlement evidence for receipts. Plaid coverage and product support vary "
                    "by institution and account type; confirm commercial-card compatibility before "
                    "buying a connection. Never promise uncapped 2%–4% economics without checking "
                    "the actual agreement, qualifying categories, annual caps, and redemption "
                    "conditions for that specific account."
                ),
                (
                    "The second nine resources connect event truth, contractual inventory, money "
                    "movement, shipments, and local diagnostics. Refresh intervals in the directory "
                    "are operating targets, not vendor service commitments. Prefer an authorized "
                    "webhook where available, but keep a scheduled reconciliation because callbacks "
                    "can arrive late, repeat, or disappear. For polling, honor documented quotas "
                    "and Retry-After responses, apply bounded exponential backoff with jitter, "
                    "and stop retrying authentication failures until credentials are repaired. "
                    "Store secrets outside exported datasets and restrict connector accounts to "
                    "the minimum read or trading scope required. Shipment protection deserves "
                    "its own evidence chain: a $20,000 shipment with an illustrative 0.5% "
                    "insurance premium costs $100, but the policy's exclusions and declared-value "
                    "rules determine whether the merchandise is covered. Carrier tracking proves "
                    "a recorded scan, not contents, acceptance quality, or insurance recovery. "
                    "Preserve serials, packing photographs, weights, purchase invoices, and the "
                    "insurance certificate. If delivery stalls, pause replacement purchasing until "
                    "the original exposure is understood. Run SQLite integrity checks and HTTP "
                    "diagnostics against sanitized examples, not live credential dumps. The fallback "
                    "for a broken integration is a controlled export and reconciled exception "
                    "queue, not silent manual edits to production balances."
                ),
            ],
            "table": {
                "caption": "Commercial interfaces and diagnostic directory, resources 10–18: exact access and bounded fallbacks",
                "headers": [
                    "Named resource and specific operating purpose",
                    "Exact access method and cost tier",
                    "Refresh latency and desk review schedule",
                    "Rate-limit hygiene and usable fallback evidence",
                ],
                "rows": [
                    [
                        "Ticketmaster Discovery API resolves event identity, venue relationships, and published event metadata.",
                        "Register at https://developer.ticketmaster.com/; use documented Discovery v2 endpoints with a developer key and permitted access tier.",
                        "Poll active event metadata hourly as a desk target; source propagation can lag actual venue changes.",
                        "Read current key quotas and honor throttling; fall back to the official venue and event pages.",
                    ],
                    [
                        "SkyBox provides ticket inventory and point-of-sale workflows for approved seller operations.",
                        "Request an approved seller account through https://www.skybox.vividseats.com/; confirm current commercial terms and integration entitlement directly.",
                        "Use contracted synchronization features and reconcile active listings frequently; measure actual delay instead of assuming instantaneous updates.",
                        "Follow issued integration documentation; use authorized inventory exports and suspend stale listings during connection failures.",
                    ],
                    [
                        "Automatiq supports contracted ticket distribution and pricing workflows within granted account permissions.",
                        "Contact https://www.automatiq.com/ for product access, supported integrations, and quoted commercial pricing.",
                        "Measure update acknowledgments against listing changes; vendor and exchange propagation determine actual execution latency.",
                        "Observe contracted request limits and deduplicate updates; revert to controlled approved-channel exports when synchronization fails.",
                    ],
                    [
                        "Plaid Transactions can supply supported account activity for settlement and purchase reconciliation.",
                        "Use https://plaid.com/docs/transactions/ through an approved application; sandbox access and production commercial pricing differ.",
                        "Treat account updates as asynchronous and institution-dependent; reconcile final balances against bank and issuer statements.",
                        "Use documented cursor synchronization and relevant webhooks; fall back to authorized account CSV exports after coverage checks.",
                    ],
                    [
                        "American Express business account statements provide issuer-origin purchase, payment, and rebate evidence.",
                        "Sign into the authorized account at https://www.americanexpress.com/; statement access accompanies the account's own fee structure.",
                        "Check due dates daily during exposure and ingest each posted statement; pending activity can change before posting.",
                        "Prefer supported downloads rather than scripted login sessions; use issuer support and archived statements during portal interruptions.",
                    ],
                    [
                        "Chase business credit-card statements provide independent payment-calendar and posted-transaction reconciliation evidence.",
                        "Use the authorized account at https://www.chase.com/; export available activity and statements under account terms.",
                        "Review upcoming payments daily and reconcile statement-cycle totals; transaction posting and reward availability follow issuer timing.",
                        "Use supported exports and approved account connections; resolve missing records through issuer statements and account support.",
                    ],
                    [
                        "UPS Developer Portal tracking interfaces support shipment milestones for buying-group delivery reconciliation.",
                        "Register at https://developer.ups.com/; obtain the required OAuth access and confirm account-specific service terms and charges.",
                        "Poll open exceptions hourly as a target; carrier scans may appear later than physical handling events.",
                        "Honor documented API limits and cache unchanged scans; use authorized UPS tracking pages and shipment documents as fallback.",
                    ],
                    [
                        "USPS Developer Portal tracking services provide supported postal shipment-status access where the account qualifies.",
                        "Start at https://developers.usps.com/; verify current tracking-product enrollment, authentication requirements, and any applicable commercial conditions.",
                        "Refresh unresolved shipments on a bounded schedule; scan publication remains event-driven rather than continuously current.",
                        "Follow the current product's limits instead of legacy assumptions; use official USPS tracking and retained mailing receipts.",
                    ],
                    [
                        "Python sqlite3, urllib.request, ssl, and logging provide local storage, transport inspection, and connector diagnostics.",
                        "Use the installed Python standard library without subscription charges; run authorized requests and local database integrity checks.",
                        "Measure every job's timestamps and elapsed duration locally; diagnostic freshness follows the desk's configured execution schedule.",
                        "Cap retries, redact secrets, and preserve TLS verification; use sanitized fixtures and prior validated exports during outages.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Reconcile immutable events into exposure, inventory, and cash decisions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Design the pipeline around immutable source events and reversible derived "
                    "views. A compact SQLite deployment can hold counterparties, commitments, "
                    "purchase lines, shipments, tickets, card postings, cash receipts, and exception "
                    "records without requiring a data warehouse. Give every imported item a source "
                    "identifier, account identifier, retrieval timestamp, source event time, currency, "
                    "and provenance hash. Use integer cents or Decimal for money, never binary "
                    "floating-point totals that drift during reconciliation. Store event timestamps "
                    "in UTC while preserving the venue timezone and original local representation. "
                    "Distinguish an absent value from a verified zero; missing fee information "
                    "should prevent a profitability calculation instead of silently increasing "
                    "the spread. Idempotency keys should reflect the source's stable transaction "
                    "identifier and event version where available. Do not deduplicate two "
                    "legitimate purchases merely because their amounts and merchant names match. "
                    "Retain raw payloads only when licensing and privacy requirements permit, "
                    "with access controls and a defined retention schedule. For restricted "
                    "payloads, preserve permitted normalized fields and retrieval evidence. "
                    "A scheduled backup must include restoration testing; an intact database "
                    "file is insufficient if connector credentials, schema migrations, and "
                    "reconciliation checkpoints cannot be recovered on another authorized workstation."
                ),
                (
                    "Separate receipt of a feed message from permission to change economic "
                    "state. A purchase-order acknowledgment creates committed demand; a card "
                    "authorization creates provisional spend; a posted charge creates a payable; "
                    "an accepted delivery creates the contractual reimbursement claim; and a "
                    "settled ACH creates cash. Build explicit transitions and retain reversals "
                    "rather than overwriting the prior state. For tickets, distinguish owned, "
                    "listed, reserved, sold, transferred, accepted, and paid. A transfer email "
                    "without recipient acceptance may leave fulfillment risk outstanding. Use "
                    "a reconciliation queue that identifies the oldest unmatched dollar amount "
                    "and the person responsible for resolving it. Alert when buyer cash is "
                    "forecast after the issuer's actual payment deadline, not merely when an "
                    "invoice looks overdue. Maintain a daily exposure report by buyer, issuer, "
                    "event, carrier, and bank rail. Twenty tickets with a planned $25 markdown "
                    "loss each imply a $500 event risk budget; a cancellation can exceed that "
                    "budget, so the model also needs refund and unrecoverable-fee cases. Apply "
                    "pre-event markdown curves from executable market evidence, with explicit "
                    "minimum proceeds and inventory-review times. Asking prices alone do not "
                    "prove that the desk can liquidate its seats."
                ),
                (
                    "Build the operator screen around decisions, not decorative charts. Show "
                    "available settled cash, issuer payments due, accepted-but-unpaid buying-group "
                    "receivables, inventory that can actually transfer, and exceptions requiring "
                    "human action. Every figure should open its component transactions and "
                    "evidence trail. A stale event-status feed should disable automated repricing "
                    "for that event until an official source is checked; it should not disable "
                    "unrelated shipment reconciliation. Give write-enabled connectors separate "
                    "permissions and audit trails from read-only research connectors. Replay "
                    "sanitized fixtures for duplicate webhooks, partial refunds, a timezone "
                    "change, a postponed event, a returned ACH, and a card-reward reversal. "
                    "Validate both the expected balance and the expected operational restriction. "
                    "For a stadium seat-license brokerage engagement, an illustrative $1,000 "
                    "earned fee less $250 of direct diligence cost leaves $750 before shared "
                    "costs, but only the governing license agreement can establish assignment "
                    "rights and required transfer charges. If rights cannot be verified, stop "
                    "marketing that allocation and retain the documentary exception. Review "
                    "access logs weekly, remove departed contractors promptly, and keep participant "
                    "identity material outside broadly shared analytics. The best automation "
                    "reduces unresolved exposure rather than merely reducing keystrokes."
                ),
            ],
            "table": {
                "caption": "Four reconciliation controls connecting source evidence to permissible operating actions",
                "headers": [
                    "Control boundary and authoritative input evidence",
                    "Required stored fields and mathematical check",
                    "Specific failure signal requiring operator intervention",
                    "Fallback action preserving capital and traceability",
                ],
                "rows": [
                    [
                        "Buying-group acceptance connects signed purchase commitments with delivery and inspection evidence.",
                        "Store committed units, accepted units, unit reimbursement, rejection terms, and the contractual settlement-clock trigger.",
                        "Accepted invoice remains unpaid beyond its agreed clock or remitting entity differs from verified instructions.",
                        "Freeze incremental buyer exposure, confirm the discrepancy independently, and retain the existing receivable without inventing cash.",
                    ],
                    [
                        "Issuer payment planning connects posted statements with settled bank receipts and approved payment instructions.",
                        "Calculate daily cash after scheduled payments, conservative buyer receipts, reserve requirements, and any confirmed rebate credits.",
                        "Expected buyer settlement falls after the issuer deadline or an issuer restriction invalidates purchasing capacity.",
                        "Stop new card commitments, fund existing obligations from available reserves, and verify payment completion independently.",
                    ],
                    [
                        "Ticket inventory control connects ownership records with listing acknowledgments and final transfer acceptance.",
                        "Track unique seat identifiers, event timezone, sale amount, selling fees, transfer state, and payout eligibility.",
                        "Two active sales reference one owned seat or event updates invalidate previously assumed transfer conditions.",
                        "Suspend affected listings, reconcile each channel manually, and resolve buyer obligations using documented exchange procedures.",
                    ],
                    [
                        "Shipment recovery connects insured values with packing evidence, carrier scans, and buyer inspection records.",
                        "Match serial-level cost, declared value, premium, policy exclusions, delivery timestamp, and any documented damage amount.",
                        "Carrier delivery lacks buyer acceptance or the policy excludes the shipped merchandise and destination combination.",
                        "Preserve claim evidence immediately, follow notice deadlines, and avoid replacement purchases that double unresolved exposure.",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Register the source and its permission boundary",
                    "action": "Record access owner, supported interface, pricing basis, documented quota, and permitted data uses.",
                    "detail": "Test a read-only retrieval and archive a sanitized example before allowing production ingestion or any listing writes.",
                },
                {
                    "step": 2,
                    "title": "Normalize and quarantine conflicting evidence",
                    "action": "Resolve entity, event, shipment, and transaction identifiers before calculating exposure or margin.",
                    "detail": "Reject duplicate economic events while retaining legitimate equal-value transactions; route incomplete fee or currency fields to an exception queue.",
                },
                {
                    "step": 3,
                    "title": "Reconcile state transitions and settlement dates",
                    "action": "Match commitments to purchases, acceptance to receivables, and posted cash to the relevant obligation.",
                    "detail": "Recompute issuer coverage and event exposure after each material update; preserve reversals rather than replacing historical records.",
                },
                {
                    "step": 4,
                    "title": "Prove recovery before enabling automation",
                    "action": "Replay outage and duplicate-message fixtures, restore a backup, and reconcile the resulting balances.",
                    "detail": "Enable bounded automation only for verified paths; keep unrelated workflows operational when one source becomes stale or unavailable.",
                },
            ],
        },
        {
            "heading": "4. Bound promo claims and reconcile every play to retained owner economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The supplied play sportsbook_promo_ev_matched_betting_syndicates is the "
                    "Regulated Sportsbook & Sweepstakes Sign-Up Promo Conversion mapping under "
                    "TRACK_2. Its advertised certainty needs correction: bonuses, opposing wagers, "
                    "and sweepstakes credits do not produce guaranteed risk-free cash. Eligibility, "
                    "stake-return rules, odds movement, market suspension, payout restrictions, "
                    "tax treatment, and conflicting settlement rules can all change proceeds. "
                    "A theoretical fifteen offers averaging $300 at 70% conversion produces "
                    "$3,150 before costs; twenty-five offers averaging $400 at 80% produces "
                    "$8,000 before costs. Neither example establishes that those offers coexist "
                    "for a resident or remain available. Treat the supplied 70%–85% band as "
                    "a conditional modeling assumption, never as an observed constant. Maintain "
                    "an offer ledger containing the official terms, eligibility date, bonus "
                    "type, minimum odds, expiry, qualifying-wager cost, and withdrawal conditions. "
                    "Do not mix regulated sportsbook authorization with sweepstakes eligibility; "
                    "their state availability and governing rules require separate checks. If "
                    "terms prohibit coordinated play or the economics require someone else's "
                    "credentials, exclude that offer. An information platform should calculate "
                    "participant-specific expected outcomes and downside cases, not manufacture "
                    "certainty by hiding losing legs, taxes, or disqualified promotions."
                ),
                (
                    "Use the requested client-side fallback as an ownership control: each "
                    "participant acts only on their own personal device, account, and cellular "
                    "connection, without location spoofing, credential sharing, or delegated wager "
                    "placement. This does not override operator terms or state restrictions. "
                    "Prefer high-liquidity mainlines when permitted, but recognize that hedge "
                    "availability can disappear between executions. Do not place the first leg "
                    "when the second leg cannot be funded and executed within the approved "
                    "risk budget; stop when eligibility or settlement definitions conflict. "
                    "For an illustrative $100 bonus, assume $78 of realized conversion proceeds "
                    "after opposing-wager settlement and $6 of additional qualifying costs. "
                    "Distributable contribution is $72. A permitted contractual 25% service "
                    "share would be $18, leaving $54 for the participant before their applicable "
                    "taxes; participant deposits and wager turnover are not platform revenue. "
                    "Whether a split-profit arrangement, custody, referral activity, or wagering "
                    "assistance requires licensing must be resolved for the actual jurisdiction "
                    "before launch. Apply the same rights-first approach to suites: four "
                    "authorized allocations at $2,500 produce $10,000 proceeds; $8,500 basis "
                    "and $500 selling costs leave $1,000 before shared costs. Without documented "
                    "suballocation rights, the fallback is to decline the transaction."
                ),
                (
                    "Finally, reconcile the entire desk to Formula v2.0 without adding illustrative "
                    "play profits on top of the canonical cases. Conservative gross basis of "
                    "$250,000 retains 35%, or $87,500; subtracting $67,500 of modeled remaining "
                    "costs leaves $20,000. Base gross basis of $1,025,000 retains $358,750; "
                    "subtracting $215,250 leaves $143,500. Scaled gross basis of $1,800,000 "
                    "retains $630,000; subtracting $270,000 leaves $360,000. Those results "
                    "equal 8%, 14.0%, and 20% of gross basis, or 22.86%, 40.0%, "
                    "and 57.14% of retained revenue. The 65% basis layer is $162,500, "
                    "$666,250, and $1,170,000 respectively. Retained spread is the scorecard's "
                    "net contribution convention; ASC 606 principal-versus-agent presentation "
                    "still depends on control and the actual contract, not an automatic 35% "
                    "recognition election. Keep rebates, refunds, sales taxes collected, customer "
                    "funds, and pass-through purchase principal in their appropriate accounts. "
                    "The stated $1,500–$9,000 monthly operating-overhead range is not a substitute "
                    "for every modeled residual cost. Reconcile labor, selling costs, losses, "
                    "and other cost categories without double counting. Staff the cases at "
                    "1 FT plus 2 contractors, 1 FT plus 2 contractors, and 2 FT "
                    "plus 3 contractors, respectively."
                ),
            ],
            "table": {
                "caption": "Canonical profit reconciliation and the separate promo-conversion unit ledger",
                "headers": [
                    "Scenario or separately identified illustrative unit",
                    "Gross basis and retained contribution calculation",
                    "Remaining costs and exact owner outcome",
                    "Operating interpretation and required risk fallback",
                ],
                "rows": [
                    [
                        "Conservative canonical case uses one full-time operator and two contractors.",
                        "$250,000 gross basis less $162,500 basis layer equals $87,500 retained revenue at 35%.",
                        "$87,500 retained revenue less $67,500 remaining modeled costs equals $20,000 annual owner profit.",
                        "Preserve 8% gross-basis margin and 22.86% retained margin; suspend purchases when buyer delays consume reserves.",
                    ],
                    [
                        "Base canonical case retains one full-time operator and two contractors.",
                        "$1,025,000 gross basis less $666,250 basis layer equals $358,750 retained revenue at 35%.",
                        "$358,750 retained revenue less $215,250 remaining modeled costs equals $143,500 annual owner profit.",
                        "Preserve 14.0% gross-basis margin and 40.0% retained margin; reconcile channel costs before expanding purchasing limits.",
                    ],
                    [
                        "Scaled canonical case employs two full-time operators and three contractors.",
                        "$1,800,000 gross basis less $1,170,000 basis layer equals $630,000 retained revenue at 35%.",
                        "$630,000 retained revenue less $270,000 remaining modeled costs equals $360,000 annual owner profit.",
                        "Preserve 20% gross-basis margin and 57.14% retained margin; diversify buyers and enforce event-specific inventory limits.",
                    ],
                    [
                        "Illustrative promo unit remains separate from every canonical volume scenario.",
                        "$100 bonus produces assumed $78 realized conversion proceeds; subtract $6 qualifying costs for $72 contribution.",
                        "A permitted 25% service share yields $18 platform contribution and $54 participant contribution before applicable taxes.",
                        "Exclude participant turnover from operator revenue; abandon the offer when eligibility, legality, or hedge execution fails.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before capital or write-enabled connectors go live",
                "body": "Each check must resolve against dated evidence owned by a named operator.",
                "items": [
                    "Verify the buying-group legal entity, signed acceptance terms, independently confirmed payout instructions, and actual Net-3 or Net-5 clock trigger.",
                    "Verify the issuer's real due date, qualifying rebate terms, available settled reserves, and the downside cash position after a delayed ACH.",
                    "Verify ticket ownership, transfer and suballocation rights, applicable reseller licensing, all-in price treatment, and BOTS Act-safe acquisition methods.",
                    "Verify participant eligibility, current operator authorization, permitted service arrangements, personal account control, and offer-specific downside before any promo activity.",
                ],
            },
        },
    ],
    "pull_quote": "A spread becomes usable profit only when ownership, settlement, and source evidence agree.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Create the eighteen-source register with access owners, current terms, documented quotas, dated retrieval evidence, and a tested fallback for each resource.",
        "Onboard two independently vetted buying groups using signed commitments, exact entity identifiers, verified remittance instructions, and measured settlement clocks.",
        "Build separate card authorization, posting, statement, payment, rebate-accrual, and rebate-receipt states; stress every due date against delayed buyer cash.",
        "Resolve owned tickets to authoritative event identifiers, document transfer rights, and suspend stale listings before enabling automated pricing or distribution.",
        "Implement immutable ingestion, cent-accurate reconciliation, sanitized replay tests, restricted connector credentials, and a successfully restored backup.",
        "Reconcile the three canonical retained-revenue cases and isolate promo-service fees from participant deposits, wagers, and conditional conversion illustrations.",
    ],
    "statutory_citations": [
        {
            "title": "15 U.S.C. § 45c — Better Online Ticket Sales Act",
            "url": "https://www.law.cornell.edu/uscode/text/15/45c",
            "relevance": (
                "Prohibits circumventing covered ticket-issuer controls and specified resale of "
                "tickets acquired through prohibited circumvention. Use no queue or CAPTCHA bypass "
                "software; retain acquisition evidence and honor issuer purchase controls."
            ),
        },
        {
            "title": "16 CFR Part 464 — Rule on Unfair or Deceptive Fees",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464",
            "relevance": (
                "Requires covered live-event ticket offers to present total prices with mandatory "
                "charges as prescribed and prohibits misleading fee representations. Model any "
                "permitted exclusions and required final-payment disclosures explicitly."
            ),
        },
        {
            "title": "New York Arts and Cultural Affairs Law § 25.07 — Ticket reseller licensing",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/25.07",
            "relevance": (
                "Provides New York's ticket-reseller licensing framework. Determine whether the "
                "desk's actual resale activities require licensing and retain current evidence "
                "before operating within the statute's scope."
            ),
        },
        {
            "title": "New York Arts and Cultural Affairs Law § 25.07-A — Ticket pricing",
            "url": "https://www.nysenate.gov/legislation/laws/ACA/25.07-A",
            "relevance": (
                "Establishes ticket-price disclosure requirements relevant to New York offers. "
                "Map mandatory fees and total-cost presentation into listing and checkout tests."
            ),
        },
        {
            "title": "New York Tax Law § 1132 — Collection of sales tax and exemption documentation",
            "url": "https://www.nysenate.gov/legislation/laws/TAX/1132",
            "relevance": (
                "Addresses collection obligations and documentation affecting presumptively taxable "
                "receipts. Maintain properly completed resale evidence rather than treating an "
                "entity registration as a sales-tax exemption."
            ),
        },
        {
            "title": "New York UCC § 9-503 — Name of debtor and secured party",
            "url": "https://www.nysenate.gov/legislation/laws/UCC/9-503",
            "relevance": (
                "Explains debtor-name requirements for financing statements. Use the legally "
                "appropriate name when searching and evaluating UCC evidence."
            ),
        },
        {
            "title": "New York UCC § 9-307 — Location of debtor",
            "url": "https://www.nysenate.gov/legislation/laws/UCC/9-307",
            "relevance": (
                "Supplies debtor-location rules relevant to Article 9 analysis. Determine the "
                "appropriate filing jurisdiction and applicable exceptions before relying on "
                "a single state's search."
            ),
        },
        {
            "title": "New York Racing, Pari-Mutuel Wagering and Breeding Law § 1367-A — Mobile sports wagering",
            "url": "https://www.nysenate.gov/legislation/laws/PML/1367-A",
            "relevance": (
                "Establishes New York's mobile sports-wagering framework. Check authorized operators "
                "and jurisdiction-specific operating requirements; do not treat sportsbook "
                "authorization as permission for unrelated sweepstakes or third-party wagering services."
            ),
        },
    ],
}
