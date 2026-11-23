from __future__ import annotations

VOLUME_041_SUBTITLE = (
    "The Complete Playbook for Buying-Group Spreads, Card Float and Ticket "
    "Allocations: $250,000–$1,800,000 USD in Annual Gross Receipts, "
    "a 1 FT + 2 C (3 People) Core Pod, and a Five-Person Scale Plan"
)

VOLUME_041_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Purchase-Order-to-Rebate Desk",
        "subtitle": (
            "Turn pre-committed wholesale orders into settled spreads and "
            "contractual card rebates without outrunning available cash."
        ),
        "audience": (
            "One full-time operator and two contractors managing documented "
            "buying-group commitments, insured shipments and daily settlement reconciliation."
        ),
        "research_basis": (
            "UCC sections 2-201 and 2-509 inform written order evidence and "
            "shipment risk allocation; California resale-certificate rules inform "
            "purchase documentation. These sources support operating controls, "
            "not the commercial availability of a particular rebate rate."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/2/2-201",
            "https://www.law.cornell.edu/ucc/2/2-509",
            "https://www.law.cornell.edu/regulations/california/18-CCR-1668",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Authorized Ticket Allocation Desk",
        "subtitle": (
            "Broker transferable event inventory through documented allocations, "
            "all-in prices and disciplined pre-event markdown curves."
        ),
        "audience": (
            "Small ticket operators using SkyBox or Automatiq to reconcile "
            "authorized inventory, exchange listings and completed transfers."
        ),
        "research_basis": (
            "15 U.S.C. section 45c establishes restrictions on ticket-control "
            "circumvention and specified resale of tickets acquired through "
            "violations. 16 CFR Part 464 supplies concrete total-price disclosure "
            "requirements for covered live-event ticket offers."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45c",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-464",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Settlement-First Arbitrage Pod",
        "subtitle": (
            "Coordinate buying-group orders, issuer-funded timing and event "
            "allocations around one reconciled exposure ledger."
        ),
        "audience": (
            "Owner-led desks expanding from three people to five while keeping "
            "card obligations, counterparty receipts and inventory exposure visible."
        ),
        "research_basis": (
            "UCC section 2-609 informs adequate-assurance remedies when reasonable "
            "grounds for insecurity arise. Ticket acquisition restrictions and "
            "resale-certificate requirements remain separate controls within the "
            "shared ledger; operational consolidation does not merge their rules."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/2/2-609",
            "https://www.law.cornell.edu/uscode/text/15/45c",
            "https://www.law.cornell.edu/regulations/california/18-CCR-1668",
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
            "Commit First, Purchase Second, Reconcile Through Settlement",
            "Five operating steps connect authorized inventory to cleared cash.",
            1,
            "operating_framework",
            (
                "Buying-group orders and ticket allocations use separate evidence "
                "records. Net-3 and Net-5 are negotiated counterparty terms, not "
                "assured clearing dates. A 60-day ledger horizon does not create "
                "a contractual 60-day interest-free card period."
            ),
            (
                "The purchase-order reconciler links commitment, purchase, delivery, "
                "receivable and card obligation before an operator increases exposure."
            ),
            [
                (
                    "Document the commitment",
                    "Signed terms before any purchasing commitment",
                    1.0,
                    (
                        "Record the vetted buying group's accepted SKU, quantity, "
                        "reimbursement, acceptance criteria and Net-3 or Net-5 "
                        "trigger. For tickets, verify allocation ownership and transfer rights."
                    ),
                ),
                (
                    "Reserve cash and limits",
                    "Cash coverage before card authorization occurs",
                    2.0,
                    (
                        "Reserve full card repayment independently of expected ACH "
                        "receipts. Verify issuer category eligibility, rebate exclusions, "
                        "available limits and the actual statement due date."
                    ),
                ),
                (
                    "Acquire through authorized channels",
                    "Permitted purchases with retained acquisition evidence",
                    3.0,
                    (
                        "Use ordinary merchant checkout or authorized allocation "
                        "contracts. Preserve receipts and purchase limits; prohibit "
                        "queue or CAPTCHA bypass and credential sharing."
                    ),
                ),
                (
                    "Deliver and evidence acceptance",
                    "Tracked delivery tied to each receivable",
                    4.0,
                    (
                        "Insure high-value merchandise and retain serial numbers, "
                        "carrier acceptance and signed delivery evidence. Record "
                        "ticket transfers and synchronize SkyBox or Automatiq listings."
                    ),
                ),
                (
                    "Clear and reconcile",
                    "Cleared receipts matched against card liabilities",
                    5.0,
                    (
                        "Match bank-cleared ACH, exchange payouts, fees and issuer "
                        "rebates to each order. Pay the card on time even when "
                        "a buying group delays reimbursement."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-opportunity-cohort",
            "funnel",
            "One Cohort From Sourced Opportunity to Cleared Settlement",
            "Nested counts preserve the same opportunity unit throughout.",
            6,
            "illustrative_model",
            (
                "Illustrative 90-day observation of 200 opportunities sourced in "
                "one intake window; an opportunity is one proposed order or "
                "allocation lot, not a ticket, person or dollar. Later stages "
                "are subsets of earlier stages. First-deal planning remains "
                "one to three months."
            ),
            (
                "Twenty-four settled opportunities represent 12% of the original "
                "cohort; unsettled purchases remain exposure rather than realized wins."
            ),
            [
                (
                    "Sourced opportunities",
                    "200 proposed order or allocation lots",
                    200.0,
                    (
                        "Log 200 distinct opportunities with seller identity, "
                        "inventory description, expected settlement terms and source "
                        "evidence; remove duplicates before measuring conversion."
                    ),
                ),
                (
                    "Verified counterparties and rights",
                    "120 verified lots from the original cohort",
                    120.0,
                    (
                        "Retain 120 opportunities after counterparty, transfer-right, "
                        "issuer-eligibility and purchase-limit checks; this is 60% "
                        "of sourced opportunities."
                    ),
                ),
                (
                    "Accepted commercial terms",
                    "60 documented commitments from verified opportunities",
                    60.0,
                    (
                        "Obtain accepted order terms or allocation agreements for "
                        "60 opportunities, representing 50% of verified opportunities "
                        "and 30% of the original cohort."
                    ),
                ),
                (
                    "Purchased and delivered",
                    "30 funded commitments with delivery evidence",
                    30.0,
                    (
                        "Fund and deliver 30 committed opportunities after cash "
                        "coverage checks; this is 50% of documented commitments "
                        "and 15% of sourced opportunities."
                    ),
                ),
                (
                    "Cleared and reconciled",
                    "24 completed settlements with matched ledger entries",
                    24.0,
                    (
                        "Reconcile cleared settlement for 24 delivered opportunities, "
                        "or 80% of delivered lots. Keep the remaining six in "
                        "receivable aging without assuming they are losses."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-owner-profit-bridge",
            "waterfall",
            "Base-Case Gross Receipts to $143,500 Owner Profit",
            "$1,025,000 gross receipts; 35% retained spread; 14.0% gross-basis margin.",
            3,
            "illustrative_model",
            (
                "Formula v2.0 endpoints are canonical; the three expense buckets "
                "are an illustrative allocation. Opening and closing bars are "
                "totals; intermediate bars are signed deductions. Conservative "
                "gross $250,000 less 65% basis leaves $87,500 retained contribution "
                "and $20,000 owner profit: 8% gross-basis margin and 22.86% retained "
                "margin. Base retained contribution is $358,750 with 40.0% retained "
                "margin. Scaled gross $1,800,000 leaves $630,000 retained contribution "
                "and $360,000 profit: 20% gross-basis margin and 57.14% retained "
                "margin. The retained_share=0.35 convention is the scorecard's "
                "net presentation; actual ASC 606 principal-versus-agent analysis "
                "determines recognized revenue for each contract."
            ),
            (
                "$1,025,000 - $666,250 - $61,500 - $96,000 - $57,750 "
                "= $143,500. Gross reimbursements and resale proceeds are not "
                "interchangeable with retained operator revenue."
            ),
            [
                (
                    "Gross receipts",
                    "$1,025,000 annual scorecard gross receipts",
                    1025000.0,
                    (
                        "Aggregate buying-group reimbursements, card-rebate yields "
                        "and ticket resale proceeds once each. Exclude unrelated "
                        "merchant sales and card borrowing from this gross total."
                    ),
                ),
                (
                    "Merchandise and ticket basis",
                    "Subtract $666,250 of direct acquisition basis",
                    -666250.0,
                    (
                        "Deduct landed merchandise and face-value ticket basis at "
                        "65% of aggregate gross receipts. Remaining modeled retained "
                        "contribution equals $358,750, or 35%."
                    ),
                ),
                (
                    "Transaction and distribution costs",
                    "Subtract $61,500 of variable execution costs",
                    -61500.0,
                    (
                        "Allocate 6.0% of gross receipts to exchange commissions, "
                        "payment charges and selling-side fulfillment costs. Exclude "
                        "costs already capitalized within landed acquisition basis."
                    ),
                ),
                (
                    "Recurring pod operating costs",
                    "Subtract $96,000 of annual operating costs",
                    -96000.0,
                    (
                        "Allocate $8,000 monthly to contractors, software, bookkeeping, "
                        "business insurance and administration. This fits the "
                        "$1,500–$9,000 monthly range; owner draws are distributions."
                    ),
                ),
                (
                    "Loss and carrying costs",
                    "Subtract $57,750 of modeled residual costs",
                    -57750.0,
                    (
                        "Allocate realized markdowns, credit losses, rebate reversals "
                        "and borrowing costs without duplicating acquisition basis "
                        "or exchange fees; residual costs equal this scenario balance."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$143,500 remaining after all modeled costs",
                    143500.0,
                    (
                        "Closing total equals 14.0% of $1,025,000 gross receipts "
                        "and 40.0% of $358,750 retained contribution. It is the "
                        "owner-profit endpoint, not an additional cash receipt."
                    ),
                ),
            ],
        ),
        (
            "diag-04-eligible-card-rebate-yields",
            "horizontal_bars",
            "Compare Rebate Yields on Eligible Settled Purchase Dollars",
            "Five illustrative payment-rail cases use one denominator.",
            2,
            "illustrative_model",
            (
                "Bars are hypothetical contractual rebate rates inside the supplied "
                "2%–4% range, not named issuer offers or observed market averages. "
                "Each rate uses eligible settled purchase spend before interest, "
                "fees and clawbacks. Uncapped treatment requires express issuer "
                "terms; these rates do not derive the 35% portfolio retained share."
            ),
            (
                "At $10,000 eligible spend, these cases produce $200–$400 of "
                "rebates before costs. Float is payment timing, not another yield."
            ),
            [
                (
                    "Buying-group general merchandise",
                    "2.0% rebate on eligible settled purchases",
                    2.0,
                    (
                        "A modeled $10,000 purchase produces $200 of rebates only "
                        "when resale activity and merchant classification qualify "
                        "under the actual commercial card agreement."
                    ),
                ),
                (
                    "Buying-group electronics orders",
                    "2.5% rebate on eligible settled purchases",
                    2.5,
                    (
                        "A modeled $10,000 purchase produces $250 before card costs. "
                        "Check electronics exclusions, rebate caps and returns; "
                        "shipment value does not change the contracted rate."
                    ),
                ),
                (
                    "Authorized event ticket inventory",
                    "3.0% rebate on eligible settled purchases",
                    3.0,
                    (
                        "A modeled $10,000 purchase produces $300 only if ticket "
                        "transactions qualify. Exchange sale proceeds and inventory "
                        "appreciation are separate from this rebate calculation."
                    ),
                ),
                (
                    "Transferable corporate-suite allocations",
                    "3.5% rebate on eligible settled purchases",
                    3.5,
                    (
                        "A modeled $10,000 card purchase produces $350 before "
                        "surcharges. Reject the card rail when its incremental "
                        "cost exceeds the collectible contractual rebate."
                    ),
                ),
                (
                    "Issuer-qualified promotional purchases",
                    "4.0% rebate on eligible settled purchases",
                    4.0,
                    (
                        "A modeled $10,000 purchase produces $400 within verified "
                        "offer terms. Replace the rate when promotional periods "
                        "expire; never extend temporary pricing across the annual model."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutes-and-exposure",
            "decision_tree",
            "Four Pre-Flight Checks Before Committing Capital",
            "Every check must pass; unresolved evidence means no purchase.",
            5,
            "operating_framework",
            (
                "These are sequential checks, not a jurisdiction-complete rulebook. "
                "Select applicable state ticket licensing, transfer and tax rules "
                "for each transaction. A blocked branch returns to evidence "
                "collection or rejects the opportunity."
            ),
            (
                "A lawful acquisition channel, accurate price, documented resale "
                "treatment and funded downside must exist before execution."
            ),
            [
                (
                    "Acquisition rights and BOTS Act",
                    "Proceed only with documented authorized acquisition",
                    1.0,
                    (
                        "Apply 15 U.S.C. section 45c: no queue, CAPTCHA or "
                        "ticket-limit circumvention. Reject resale covered by the "
                        "statute's knowledge or participation conditions. Verify "
                        "suite and stadium seat license transfer restrictions."
                    ),
                ),
                (
                    "Displayed prices and local permissions",
                    "Proceed only with correct covered total prices",
                    2.0,
                    (
                        "Apply 16 CFR Part 464 to covered ticket offers, including "
                        "required total-price prominence and permitted exclusions. "
                        "Verify applicable state all-in pricing, reseller licensing "
                        "and venue-specific transfer requirements before listing."
                    ),
                ),
                (
                    "Resale and shipment documentation",
                    "Proceed only with applicable tax and delivery evidence",
                    3.0,
                    (
                        "Validate resale-certificate eligibility under applicable state "
                        "rules; California purchases may invoke 18 CCR section 1668. "
                        "Document shipment risk under adopted UCC section 2-509 "
                        "and verify insurance exclusions."
                    ),
                ),
                (
                    "Cash coverage and loss capacity",
                    "Proceed only with funded settlement-delay downside",
                    4.0,
                    (
                        "Require cash coverage for card obligations despite delayed "
                        "ACH, issuer shutdown or frozen exchange payouts. Set "
                        "counterparty concentration limits and pre-event stop-loss "
                        "markdown curves before acquiring inventory."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-pod",
            "org_architecture",
            "Three Core Seats, Two Explicit Scale Additions",
            "Base uses 1 FT + 2 C; Scaled uses 2 FT + 3 C.",
            11,
            "operating_framework",
            (
                "FT means full-time; C means contractor. Each numeric value "
                "represents one person in the five-person scaled design. Only "
                "the first three seats operate in Conservative and Base cases. "
                "Contractor hours are not assumed equivalent to full-time hours."
            ),
            (
                "The owner controls exposure; operators maintain evidence and "
                "reconciliation. Adding people does not automatically produce "
                "the Scaled scenario's $360,000 owner profit."
            ),
            [
                (
                    "Owner and capital lead",
                    "Core full-time seat across all scenarios",
                    1.0,
                    (
                        "Own counterparty selection, issuer relationships, cash "
                        "coverage and concentration limits. Authorize purchases "
                        "against documented commitments rather than available card limits alone."
                    ),
                ),
                (
                    "Settlement and ledger specialist",
                    "Core contractor seat for daily reconciliations",
                    1.0,
                    (
                        "Maintain the 60-day statement horizon, reconcile buying-group "
                        "ACH and exchange payouts, track rebates and flag "
                        "receivables that pass contractual due dates."
                    ),
                ),
                (
                    "Inventory and fulfillment coordinator",
                    "Core contractor seat for delivery and listings",
                    1.0,
                    (
                        "Track insured shipments, serial numbers and ticket transfers. "
                        "Use SkyBox or Automatiq to reconcile exchange inventory "
                        "and apply owner-defined markdown curves."
                    ),
                ),
                (
                    "Allocation and operations manager",
                    "Additional full-time seat in the Scaled case",
                    1.0,
                    (
                        "Manage a larger authorized allocation pipeline and buying-group "
                        "order book. Separate commercial sourcing from settlement "
                        "reconciliation while preserving one exposure ledger."
                    ),
                ),
                (
                    "Exception and peak-event specialist",
                    "Additional contractor seat in the Scaled case",
                    1.0,
                    (
                        "Resolve transfer failures, carrier claims, disputed reimbursements "
                        "and event-week listing exceptions. Maintain evidence trails "
                        "without overriding purchasing or issuer restrictions."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-buckets",
            "stacked_comparison",
            "Allocate $30,000 Before Expanding Purchase Volume",
            "Four cash buckets also reconcile the $10,000 and $55,000 endpoints.",
            4,
            "illustrative_model",
            (
                "Numeric values show one $30,000 deployment, not three stacked "
                "scenarios. Bucket details define matching $10,000 minimum and "
                "$55,000 upper plans. Card limits are borrowing capacity, not "
                "startup equity; uncollected rebates and expected ACH are not cash."
            ),
            (
                "Minimum $4,000 + $1,000 + $4,000 + $1,000 = $10,000; "
                "working $15,000 + $3,000 + $9,000 + $3,000 = $30,000; "
                "upper $28,000 + $6,000 + $17,000 + $4,000 = $55,000."
            ),
            [
                (
                    "Committed merchandise purchases",
                    "$15,000 reserved for documented buying-group orders",
                    15000.0,
                    (
                        "Allocate $4,000 minimum, $15,000 working or $28,000 upper "
                        "to acquisition principal. Recycle funds only after cleared "
                        "receipts; never count inventory and its funding twice."
                    ),
                ),
                (
                    "Ticket allocation inventory",
                    "$3,000 reserved for transferable event allocations",
                    3000.0,
                    (
                        "Allocate $1,000 minimum, $3,000 working or $6,000 upper "
                        "to bounded ticket exposure. Avoid illiquid seat-license "
                        "commitments that exceed the selected plan's loss capacity."
                    ),
                ),
                (
                    "Settlement and repayment liquidity",
                    "$9,000 held outside normal purchasing activity",
                    9000.0,
                    (
                        "Allocate $4,000 minimum, $9,000 working or $17,000 upper "
                        "to delays and payment obligations. Size purchasing below "
                        "cash-covered obligations; this reserve alone may be insufficient."
                    ),
                ),
                (
                    "Setup and initial operating runway",
                    "$3,000 reserved for systems and launch operations",
                    3000.0,
                    (
                        "Allocate $1,000 minimum, $3,000 working or $4,000 upper "
                        "to setup, insurance deposits and initial tools. Budget "
                        "later $1,500–$9,000 monthly operating costs separately."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-controlled-launch",
            "timeline_roadmap",
            "Build the Desk in Thirty Days Without Forcing a Trade",
            "Four weekly milestones establish evidence, liquidity and execution readiness.",
            12,
            "operating_framework",
            (
                "The sprint builds operating capability, not an assumed first "
                "settlement. Canonical time to first deal remains one to three "
                "months. Paid tools and live purchases require funded commitments "
                "within the selected startup capital plan."
            ),
            (
                "Finish with a reconciled pilot or a documented reason to keep "
                "capital idle; neither projected rebates nor pending ACH fund repayment."
            ),
            [
                (
                    "Days 1-7",
                    "Establish counterparties, rules and capital boundaries",
                    7.0,
                    (
                        "Vet at least two buying groups, record Net-3 or Net-5 "
                        "terms, map ticket jurisdictions and confirm issuer resale "
                        "eligibility. Select the startup budget and concentration limits."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build linked order, inventory and statement ledgers",
                    14.0,
                    (
                        "Implement the deal-commit reconciler and 60-day obligation "
                        "view. Test partial ACH, duplicate payouts, rebate reversals "
                        "and transfer failures; evaluate SkyBox or Automatiq inventory synchronization."
                    ),
                ),
                (
                    "Days 15-21",
                    "Rehearse full settlement before a bounded pilot",
                    21.0,
                    (
                        "Run a documented purchase-to-settlement simulation. Execute "
                        "one small purchase only when commitments, transfer rights, "
                        "insurance and repayment cash are verified; otherwise continue sourcing."
                    ),
                ),
                (
                    "Days 22-30",
                    "Reconcile evidence and set the next exposure limit",
                    30.0,
                    (
                        "Match cleared receipts and due card obligations where "
                        "a pilot exists. Review aging, realized spread and markdown "
                        "behavior; expand only within funded limits and documented capacity."
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
                dict(
                    label=label,
                    value=value,
                    numeric_value=float(number),
                    detail=detail,
                )
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
