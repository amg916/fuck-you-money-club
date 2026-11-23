from __future__ import annotations

VOLUME_041_SUBTITLE = (
    "The Complete Playbook for Buying Group, Commercial Card-Float & Rebate "
    "Arbitrage — $250,000–$1,800,000 USD Annual Gross Activity, Built from a "
    "1 FT + 2 C (3 People) Pod"
)

VOLUME_041_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Pre-Committed Wholesale Buying Desk",
        "subtitle": (
            "Build a three-person buying-group operation around verified orders, "
            "documented warehouse delivery, and cleared ACH settlement."
        ),
        "audience": (
            "Electronics procurement operators with $10,000–$55,000 of startup "
            "capital and disciplined parcel-level reconciliation."
        ),
        "research_basis": (
            "Separate BuyForMeRetail, Pointsmaker, and MaxOutDeals commitments "
            "from speculative inventory. DE, NH, and OR lack a general state "
            "sales tax, but a warehouse address alone does not establish every "
            "purchase's tax treatment. Verify destination, seller collection "
            "rules, and resale documentation where applicable. UCC 2-509 "
            "provides default risk-of-loss rules subject to the parties' agreement; "
            "record the actual contract allocation before shipping."
        ),
        "sources": [
            "https://revenue.delaware.gov/",
            "https://www.revenue.nh.gov/",
            "https://www.oregon.gov/dor/",
            "https://www.law.cornell.edu/ucc/2/2-509",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Commercial Rewards Contribution Desk",
        "subtitle": (
            "Measure card and portal rewards after payment fees, exclusions, "
            "reversals, and the cost of settling every statement."
        ),
        "audience": (
            "B2B purchasing teams using commercial cards for genuine inventory "
            "purchases and eligible supplier invoices."
        ),
        "research_basis": (
            "Route eligible transactions through Rakuten, TopCashback, and "
            "documented card offers without assuming every layer stacks. Compare "
            "Plastiq and Melio fees with collectible rewards before paying. "
            "26 U.S.C. 1012 supplies the general cost-basis rule, while "
            "26 U.S.C. 6050W addresses payment-settlement reporting. Maintain "
            "purchase-price adjustment records separately from interest and "
            "other receipts; a reporting form does not establish profit."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/26/1012",
            "https://www.law.cornell.edu/uscode/text/26/6050W",
            "https://www.law.cornell.edu/uscode/text/26/61",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Settlement-First Treasury Desk",
        "subtitle": (
            "Earn bank bonuses and short-duration Treasury returns only after "
            "protecting card repayment and operating liquidity."
        ),
        "audience": (
            "Small treasury teams with settled surplus cash, a daily liability "
            "calendar, and documented bank-offer qualification records."
        ),
        "research_basis": (
            "31 CFR Part 356 governs marketable Treasury securities offerings. "
            "12 U.S.C. 1821 establishes the deposit-insurance framework; coverage "
            "depends on the depositor, institution, and ownership category rather "
            "than account count alone. Model interest under 26 U.S.C. 61 and "
            "classify each bank bonus from its terms and facts. An advertised "
            "55-day card interval is a scheduling assumption, not investment "
            "capital or an extension of the contractual payment deadline."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-31/subtitle-B/chapter-II/subchapter-A/part-356",
            "https://www.law.cornell.edu/uscode/text/12/1821",
            "https://www.law.cornell.edu/uscode/text/26/61",
            "https://www.treasurydirect.gov/marketable-securities/treasury-bills/",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_041_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-commitment-to-cleared-cash",
            "process_flow",
            "Commit First, Ship Second, Reconcile Every Dollar",
            "Three separate earnings ledgers share one repayment calendar.",
            1,
            "operating_framework",
            (
                "The wholesale lane records merchandise reimbursement and landed "
                "cost; the rewards lane records eligible card and portal receipts; "
                "the treasury lane records earned interest and qualified bonuses. "
                "Record each economic benefit once. Net-3 and Net-5 settlement "
                "terms are counterparty-specific commitments, not cleared cash."
            ),
            (
                "A card charge creates a repayment liability. Only settled "
                "contribution after merchandise, fees, losses, and operating "
                "costs can support owner profit."
            ),
            [
                (
                    "Validate the wholesale commitment",
                    "Step 1 — secure quantity, price, and acceptance terms",
                    1.0,
                    (
                        "Check BuyForMeRetail, Pointsmaker, or MaxOutDeals terms "
                        "for the exact SKU, receiving address, quantity limit, "
                        "commitment expiry, inspection period, and payout clock. "
                        "Reject purchases that rely on an uncommitted resale."
                    ),
                ),
                (
                    "Price the three earnings lanes",
                    "Step 2 — separate merchandise, rewards, and treasury",
                    2.0,
                    (
                        "Calculate wholesale contribution without rewards first. "
                        "Then evaluate Rakuten, TopCashback, and card offers "
                        "against reseller exclusions, eligible categories, caps, "
                        "and reversals. Keep treasury interest outside both "
                        "purchase and reward contribution calculations."
                    ),
                ),
                (
                    "Fund and document the shipment",
                    "Step 3 — reserve repayment before releasing inventory",
                    3.0,
                    (
                        "Verify DE, NH, or OR delivery treatment and applicable "
                        "resale certificates. Capture serial numbers, parcel "
                        "weight, insurance limits, and carrier acceptance. "
                        "Store card closing and due dates beside each purchase."
                    ),
                ),
                (
                    "Match receiving to cleared ACH",
                    "Step 4 — reconcile committed, accepted, and paid amounts",
                    4.0,
                    (
                        "Join order ID, tracking number, warehouse receipt, "
                        "inspection adjustments, and bank transaction. An ACH "
                        "initiation notice is not settlement. Escalate shortages "
                        "and stop new commitments when counterparty limits bind."
                    ),
                ),
                (
                    "Settle liabilities before sweeping",
                    "Step 5 — pay the card and invest only surplus cash",
                    5.0,
                    (
                        "Protect the full statement payment and operating buffer. "
                        "Sweep only settled surplus into eligible bank accounts "
                        "or maturity-matched T-bills. Record principal movements "
                        "as balance-sheet transfers and earned yield separately."
                    ),
                ),
            ],
        ),
        (
            "diag-02-wholesale-opportunity-cohort",
            "funnel",
            "From 200 Screened Offers to 30 Settled Orders",
            "One nested wholesale cohort; every later stage belongs to the prior stage.",
            6,
            "illustrative_model",
            (
                "Illustrative 90-day cohort of 200 distinct buying-group offers, "
                "each representing one potential order. Counts are not revenue "
                "forecasts or observed conversion rates. The funnel excludes "
                "standalone B2B payment transactions and treasury placements."
            ),
            (
                "Cumulative conversion is 100%, 75%, 45%, 25%, and 15%; "
                "do not multiply settled-order count by unrelated merchant GMV."
            ),
            [
                (
                    "Screened wholesale offers",
                    "200 offers — 100% of the starting cohort",
                    200.0,
                    (
                        "Capture SKU, seller, destination warehouse, commitment "
                        "price, order cap, and stated payout term. Deduplicate "
                        "repeated listings before assigning an opportunity ID."
                    ),
                ),
                (
                    "Verified commitments",
                    "150 offers — 75% of the starting cohort",
                    150.0,
                    (
                        "Remove 50 offers lacking current written acceptance, "
                        "verified receiving instructions, or dependable "
                        "counterparty identity. The remaining 150 belong to "
                        "the original 200-offer cohort."
                    ),
                ),
                (
                    "Positive stressed contribution",
                    "90 offers — 45% of the starting cohort",
                    90.0,
                    (
                        "Remove 60 commitments whose landed cost, insured "
                        "shipping, payout deductions, or return exposure erase "
                        "the wholesale spread. Do not rescue negative merchandise "
                        "economics with unconfirmed portal rewards."
                    ),
                ),
                (
                    "Funded and shipped orders",
                    "50 offers — 25% of the starting cohort",
                    50.0,
                    (
                        "Defer 40 otherwise profitable offers because cash "
                        "reserves, card availability, or counterparty exposure "
                        "limits are exhausted. Ship only against documented "
                        "repayment capacity and valid receiving instructions."
                    ),
                ),
                (
                    "Accepted and cash settled",
                    "30 orders — 15% of the starting cohort",
                    30.0,
                    (
                        "At the measurement cutoff, 30 shipped orders have "
                        "accepted quantities and cleared ACH. The other 20 "
                        "remain outstanding within the shipped cohort; keep "
                        "their inventory, receivables, and liabilities visible."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "Base Case — $1,025,000 Gross Activity to $143,500 Owner Profit",
            "Six bars reconcile the canonical 14.0% gross-basis net margin.",
            3,
            "illustrative_model",
            (
                "USD per year. First and final bars are absolute totals; four "
                "interior bars are signed deductions. Formula v2.0 fixes gross "
                "activity at $1,025,000, retained_share at 0.35, retained "
                "contribution at $358,750, and owner profit at $143,500. The "
                "three post-merchandise expense allocations are editorial "
                "reconciliation assumptions, not supplied engine line items. "
                "The scorecard's retained metric does not replace an ASC 606 "
                "principal-versus-agent assessment for reported revenue."
            ),
            (
                "$1,025,000 − $666,250 − $108,000 − $61,500 − $45,750 "
                "= $143,500. Owner profit is 14.0% of gross activity and "
                "40.0% of $358,750 retained contribution."
            ),
            [
                (
                    "Gross scorecard activity",
                    "$1,025,000 annual gross-basis starting total",
                    1025000.0,
                    (
                        "Aggregate the canonical wholesale reimbursement, "
                        "commercial reward, and treasury-yield activity basis. "
                        "Exclude card credit limits, borrowed principal, "
                        "supplier GMV outside this operation, and sweep transfers."
                    ),
                ),
                (
                    "Landed merchandise deduction",
                    "−$666,250 leaves $358,750 retained contribution",
                    -666250.0,
                    (
                        "Apply the canonical 65% blended merchandise-cost "
                        "deduction. The remaining 35% is the supplied retained "
                        "contribution metric, not an assertion that every "
                        "buying-group order earns a 35% merchandise spread."
                    ),
                ),
                (
                    "Pod and recurring operating cost",
                    "−$108,000 leaves $250,750 before variable deductions",
                    -108000.0,
                    (
                        "Illustratively allocate $72,000 to contractor support "
                        "and $36,000 to systems, bookkeeping, insurance, and "
                        "recurring administration. Total recurring opex equals "
                        "$9,000 monthly. Owner labor is compensated through "
                        "the resulting owner-profit measure."
                    ),
                ),
                (
                    "Payment and carrying cost",
                    "−$61,500 leaves $189,250 before fulfillment losses",
                    -61500.0,
                    (
                        "Deduct illustrative transaction fees and actual "
                        "financing or carrying charges. Do not count repayment "
                        "of card principal as an expense or treat an unused "
                        "credit line as earned income."
                    ),
                ),
                (
                    "Incremental fulfillment losses",
                    "−$45,750 leaves $143,500 annual owner profit",
                    -45750.0,
                    (
                        "Deduct incremental return freight, realized parcel "
                        "losses, and settlement shortfalls after recoveries. "
                        "Exclude amounts already included in landed merchandise "
                        "cost and avoid adding a second expense for the same loss."
                    ),
                ),
                (
                    "Owner profit total",
                    "$143,500 — 14.0% gross and 40.0% retained margin",
                    143500.0,
                    (
                        "Render this endpoint as a total anchored at zero, "
                        "not as another positive increment. Preserve the "
                        "canonical owner-profit definition without inserting "
                        "additional personal-tax or owner-draw assumptions."
                    ),
                ),
            ],
        ),
        (
            "diag-04-unit-contribution-by-lane",
            "horizontal_bars",
            "Five Routes, Explicit Denominators",
            "Illustrative contribution percentages, not interchangeable annual returns.",
            2,
            "illustrative_model",
            (
                "Each bar uses $10,000 of its stated purchase, invoice, or "
                "treasury principal as denominator. Wholesale and rewards bars "
                "cover one transaction cycle; treasury covers 55 days. These "
                "examples are not components of the annual scorecard bridge. "
                "All prices, reward rates, and payment fees below are modeling "
                "inputs rather than current provider quotations."
            ),
            (
                "Keep wholesale spread, reward contribution, and treasury "
                "yield separate. Negative fee-versus-rebate transactions "
                "cannot be improved merely by increasing payment volume."
            ),
            [
                (
                    "Insured electronics wholesale",
                    "2.40% — $240 contribution per $10,000 purchase",
                    2.4,
                    (
                        "A pre-committed $10,300 reimbursement less $10,000 "
                        "merchandise and $60 insured outbound shipping leaves "
                        "$240 before shared overhead. Exclude card and portal "
                        "rewards from this wholesale-only calculation."
                    ),
                ),
                (
                    "Commodity wholesale replenishment",
                    "0.80% — $80 contribution per $10,000 purchase",
                    0.8,
                    (
                        "A $10,200 reimbursement less $10,000 merchandise, "
                        "$80 shipping, and $40 expected deductions leaves "
                        "$80 before overhead. A further $100 receiving "
                        "shortfall turns the order contribution negative."
                    ),
                ),
                (
                    "Eligible card and portal stack",
                    "3.00% — $300 incremental rewards per $10,000 spend",
                    3.0,
                    (
                        "Assume $200 collectible card rewards plus $100 "
                        "collectible portal rewards and zero incremental "
                        "payment fee. Verify Rakuten or TopCashback attribution, "
                        "reseller eligibility, and card terms. Test claimed "
                        "uncapped 2%–4% offers rather than assuming availability."
                    ),
                ),
                (
                    "B2B invoice payment rail",
                    "−0.90% — $90 loss per $10,000 invoice",
                    -0.9,
                    (
                        "An illustrative Plastiq or Melio route earns $200 "
                        "at 2% of eligible invoice spend but costs $290 at "
                        "a 2.9% fee. The $90 deficit precedes interest and "
                        "overhead; verify rail and issuer eligibility separately."
                    ),
                ),
                (
                    "Settled cash treasury placement",
                    "0.603% — about $60.27 per $10,000 over 55 days",
                    4.0 * 55.0 / 365.0,
                    (
                        "Use $10,000 × 4% × 55/365 for a simple-interest "
                        "planning estimate before fees and taxes. Actual "
                        "T-bill return follows purchase price and maturity "
                        "proceeds. Exclude bank bonuses until qualification "
                        "and exclude borrowed card principal from profit."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-risk-decisions",
            "decision_tree",
            "Four Checks Before Capital Leaves the Account",
            "Proceed sequentially; any failed check stops that transaction.",
            5,
            "operating_framework",
            (
                "Four ordered decision nodes. A pass advances to the next "
                "node; a failure routes to the corrective action in its detail. "
                "Sources establish statutory context, while seller, issuer, "
                "carrier, and buying-group contracts supply transaction terms."
            ),
            (
                "Tax documentation, loss allocation, reward records, and "
                "repayment liquidity must each stand independently."
            ),
            [
                (
                    "Destination and resale treatment",
                    "Pass with documented sourcing and destination treatment",
                    1.0,
                    (
                        "Verify DE, NH, or OR delivery and applicable seller "
                        "collection rules; retain valid resale certificates "
                        "where required. Oregon's general sales-tax position "
                        "appears in ORS 305.620. If treatment is unresolved, "
                        "price tax into the order or defer the purchase."
                    ),
                ),
                (
                    "Commitment and shipment exposure",
                    "Pass with written acceptance and recoverable loss exposure",
                    2.0,
                    (
                        "Apply the contract's loss allocation against UCC "
                        "2-509 defaults. Verify carrier coverage exclusions, "
                        "declared-value limits, claim deadlines, and inspection "
                        "rights. If uninsured exposure exceeds the loss budget, "
                        "reduce shipment size or reject the commitment."
                    ),
                ),
                (
                    "Permitted payment and reward records",
                    "Pass with genuine spend and auditable reward treatment",
                    3.0,
                    (
                        "Confirm issuer and payment-provider permission for "
                        "the transaction; exclude prohibited consumer "
                        "card-cycling and circular manufactured payments. "
                        "Retain basis records under 26 U.S.C. 1012 and "
                        "reconcile applicable 1099-K reporting under "
                        "26 U.S.C. 6050W without equating receipts to profit."
                    ),
                ),
                (
                    "Due-date liquidity and concentration",
                    "Pass only when stressed repayment remains fully funded",
                    4.0,
                    (
                        "For a $10,000 charge due on day 55, delay expected "
                        "Net-5 ACH by another 60 days and assume a $500 "
                        "shipping or return loss. Require $10,500 unrestricted "
                        "cash plus other due obligations. Otherwise reduce "
                        "the purchase; do not rely on a new card charge "
                        "or an unsettled Treasury sale to make repayment."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-pod",
            "org_architecture",
            "A Three-Person Base Pod, Five People at Scale",
            "Conservative and Base use 1 FT + 2 C; Scaled uses 2 FT + 3 C.",
            11,
            "operating_framework",
            (
                "FT denotes a full-time seat and C denotes a contractor seat. "
                "The first three seats form the starting pod; the last two "
                "activate only in the scaled configuration. Seat count does "
                "not specify contractor hours or imply identical workloads."
            ),
            (
                "Separate purchasing authority, receipt evidence, and cash "
                "reconciliation. Use bank entitlements and documented dual "
                "authorization for new payees without sharing credentials."
            ),
            [
                (
                    "Owner and treasury lead",
                    "Base seat 1 — full-time capital and counterparty owner",
                    1.0,
                    (
                        "Set exposure limits, authorize commitments, manage "
                        "issuer relationships, and maintain the repayment "
                        "calendar. Review cleared ACH and reserve sufficiency "
                        "daily; suspend purchasing when liquidity headroom "
                        "or counterparty reliability deteriorates."
                    ),
                ),
                (
                    "Procurement and fulfillment specialist",
                    "Base seat 2 — contractor purchase and parcel operator",
                    1.0,
                    (
                        "Verify SKU eligibility, commitment expiry, warehouse "
                        "instructions, and shipping evidence. Maintain serial "
                        "number records and open carrier claims promptly. "
                        "Prepare purchase batches without unilateral authority "
                        "to create and pay new bank beneficiaries."
                    ),
                ),
                (
                    "Reconciliation and rewards specialist",
                    "Base seat 3 — contractor ledger and exception operator",
                    1.0,
                    (
                        "Match card charges, accepted inventory, ACH receipts, "
                        "portal attribution, and reward reversals. Reconcile "
                        "purchase-price adjustments and reporting forms; "
                        "send unmatched transactions to the owner with "
                        "amount, age, evidence, and next action."
                    ),
                ),
                (
                    "Operations and counterparty manager",
                    "Scaled seat 4 — additional full-time operating owner",
                    1.0,
                    (
                        "Absorb increased order volume, monitor warehouse "
                        "acceptance quality, and maintain vetted counterparty "
                        "capacity. Keep exposure diversified across reliable "
                        "Net-3 and Net-5 groups without weakening due-date "
                        "cash reserves or documentation standards."
                    ),
                ),
                (
                    "Automation and controls specialist",
                    "Scaled seat 5 — additional contractor systems operator",
                    1.0,
                    (
                        "Maintain the deal-commit reconciler, eligible reward "
                        "router, ACH ledger, and maturity alerts using "
                        "permitted exports and interfaces. Test duplicate "
                        "matching, stale balances, failed imports, and "
                        "issuer account restrictions before expanding volume."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Four Capital Buckets Across $10,000–$55,000",
            "An illustrative $30,000 plan keeps cash reserves distinct from card capacity.",
            4,
            "illustrative_model",
            (
                "numeric_value represents the $30,000 central plan in USD. "
                "Stage text also provides complete $10,000 and $55,000 plans. "
                "These capital plans do not determine annual scenario revenue. "
                "Canonical Conservative economics are $250,000 gross, $87,500 "
                "retained contribution, and $20,000 owner profit at 8% gross "
                "margin and 22.86% rounded retained margin. Base economics are "
                "$1,025,000 gross, $358,750 retained, and $143,500 owner profit "
                "at 14% gross and 40% retained margins. Scaled economics are "
                "$1,800,000 gross, $630,000 retained, and $360,000 owner profit "
                "at 20% gross and 57.14% rounded retained margins. Each "
                "scenario uses retained_share=0.35."
            ),
            (
                "Low plan totals $10,000; central plan totals $30,000; high "
                "plan totals $55,000. Card limits are liabilities available "
                "for use, not additional startup equity or owner income."
            ),
            [
                (
                    "Purchase working capital",
                    "$4,000 low / $12,000 central / $22,000 high",
                    12000.0,
                    (
                        "Fund small committed orders and settlement gaps. "
                        "Scale order size to actual cash recovery rather "
                        "than theoretical card capacity. A $12,000 inventory "
                        "allocation does not authorize $12,000 of additional "
                        "unreserved card obligations."
                    ),
                ),
                (
                    "Protected repayment liquidity",
                    "$3,500 low / $10,500 central / $19,250 high",
                    10500.0,
                    (
                        "Keep this cash unrestricted and separate from "
                        "treasury experiments. Cover statements under delayed "
                        "ACH and issuer account restrictions. Add all other "
                        "due obligations before measuring headroom; stop "
                        "buying when the reserve becomes insufficient."
                    ),
                ),
                (
                    "Shipping and loss liquidity",
                    "$1,500 low / $4,500 central / $8,250 high",
                    4500.0,
                    (
                        "Fund insured shipping, return freight, deductibles, "
                        "and claim-payment delays. This allocation is a "
                        "cash buffer, not an expense automatically recognized "
                        "on day one. Replenish it after realized losses "
                        "before increasing parcel values."
                    ),
                ),
                (
                    "Systems and launch operating cash",
                    "$1,000 low / $3,000 central / $5,500 high",
                    3000.0,
                    (
                        "Fund ledger setup, bookkeeping, shipping tools, "
                        "and initial contractor onboarding. Canonical monthly "
                        "opex spans $1,500–$9,000; launch cash alone does "
                        "not cover a full 1–3 month first-deal window. "
                        "Throttle activity or add funded runway before hiring."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to a Controlled Pilot",
            "Build evidence and repayment discipline before pursuing annual scale.",
            12,
            "operating_framework",
            (
                "Four consecutive weekly milestones cover days 1–30. "
                "The canonical first-deal window is 1–3 months, so this "
                "sprint targets operational readiness rather than requiring "
                "a completed deal by day 30. Provider availability, issuer "
                "terms, and warehouse acceptance must be verified directly."
            ),
            (
                "Expand only after an entire commitment-to-cleared-cash cycle "
                "reconciles. A successful import, pending reward, or initiated "
                "ACH does not establish realized profit."
            ),
            [
                (
                    "Map counterparties and obligations",
                    "Days 1-7 — establish the three-ledger operating foundation",
                    1.0,
                    (
                        "Verify buying-group identities and current terms, "
                        "collect receiving instructions, and document tax "
                        "treatment. Create separate wholesale, rewards, and "
                        "treasury accounts in the operating ledger. Record "
                        "issuer closing dates, due dates, limits, and restrictions."
                    ),
                ),
                (
                    "Build matching and stress tests",
                    "Days 8-14 — prove every transaction can be reconstructed",
                    2.0,
                    (
                        "Load permitted card and bank exports into a "
                        "reconciler keyed by order and settlement identifiers. "
                        "Test duplicate rows, split ACH, missing parcels, "
                        "reward reversals, and a 60-day payout delay. "
                        "Require reserved cash to survive the stressed schedule."
                    ),
                ),
                (
                    "Execute a bounded pilot",
                    "Days 15-21 — submit a small order only if ready",
                    3.0,
                    (
                        "Use one verified commitment, insured shipment, "
                        "documented purchase terms, and full repayment "
                        "coverage. Capture portal attribution only where "
                        "reseller use is permitted. If onboarding remains "
                        "incomplete, rehearse with synthetic ledger entries "
                        "rather than forcing a purchase."
                    ),
                ),
                (
                    "Reconcile and set expansion limits",
                    "Days 22-30 — close evidence gaps before increasing exposure",
                    4.0,
                    (
                        "Match any received inventory acceptance and cleared "
                        "ACH to the original commitment; retain open items "
                        "as receivables rather than assumed cash. Compare "
                        "actual contribution with the order model, pay "
                        "obligations on time, and sweep only genuine surplus. "
                        "Continue the pilot into months two or three if needed."
                    ),
                ),
            ],
        ),
    ]
    return [
        dict(
            diagram_id=identifier,
            chart_type=kind,
            title=title,
            subtitle=subtitle,
            chapter_number=chapter,
            epistemic_tag=tag,
            assumptions_note=note,
            caption=caption,
            stages=[
                dict(label=label, value=value, numeric_value=float(number), detail=detail)
                for label, value, number, detail in stages
            ],
        )
        for (
            identifier,
            kind,
            title,
            subtitle,
            chapter,
            tag,
            note,
            caption,
            stages,
        ) in specs
    ]
