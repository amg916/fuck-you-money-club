from __future__ import annotations

VOLUME_043_SUBTITLE = (
    "The Complete Playbook for Live-Event, Super Bowl & VIP Ticket Brokering: "
    "$220,000–$1,800,000 USD in Annual Gross Billings, "
    "a Core 1 FT + 2 C Pod (3 People), and Settlement-Disciplined Arbitrage"
)

VOLUME_043_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Synchronized Ticket Inventory Desk",
        "subtitle": (
            "Run authorized multi-exchange resale through SkyBox, Automatiq, or "
            "Logitix while controlling replacement exposure and delayed settlement."
        ),
        "audience": (
            "One full-time inventory operator and two contractors managing "
            "documented ticket rights across multiple secondary exchanges."
        ),
        "research_basis": (
            "15 U.S.C. §45c prohibits covered ticket-purchase security circumvention "
            "and specified resale of tickets obtained through prohibited conduct. "
            "16 CFR Part 464 supplies federal total-price requirements for "
            "live-event tickets. These requirements support an inventory-control "
            "positioning, rather than automated primary-market queue bypass."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45c",
            "https://www.ecfr.gov/current/title-16/part-464",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Stadium Suite Seat-Splitting Desk",
        "subtitle": (
            "Turn expressly transferable suite capacity into individually priced "
            "corporate seats without losing control of minimum commitments."
        ),
        "audience": (
            "Small hospitality operators with venue relationships, written "
            "seat-splitting permission, and enough liquidity to absorb empty seats."
        ),
        "research_basis": (
            "New York Arts and Cultural Affairs Law Article 25 establishes "
            "ticket-resale requirements, including licensing and pricing provisions. "
            "16 CFR Part 464 informs live-event total-price presentation. Neither "
            "source grants suite subdivision rights; the venue agreement must "
            "expressly permit the proposed resale and access structure."
        ),
        "sources": [
            "https://www.nysenate.gov/legislation/laws/ACA/A25",
            "https://www.ecfr.gov/current/title-16/part-464",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Tentpole Corporate Hospitality Desk",
        "subtitle": (
            "Build Super Bowl, World Cup, F1, Masters, and Final Four packages "
            "around verified entitlements, milestone collections, and refund liquidity."
        ),
        "audience": (
            "Corporate hospitality brokers sourcing authorized ticket allotments "
            "and separately documented lounge, transport, and hosting services."
        ),
        "research_basis": (
            "15 U.S.C. §45c constrains covered acquisition methods; 16 CFR Part 464 "
            "addresses live-event ticket total-price presentation and fee "
            "misrepresentations. Sponsor inventory requires contractual resale "
            "permission, and an event name alone establishes no affiliation, "
            "hospitality entitlement, or transfer authority."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/45c",
            "https://www.ecfr.gov/current/title-16/part-464",
            "https://www.nysenate.gov/legislation/laws/ACA/A25",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_043_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-controlled-ticket-workflow",
            "process_flow",
            "Acquire Rights, Lock Inventory, Collect Settled Cash",
            "Three brokerage models share controls, not capital or payout profiles.",
            1,
            "operating_framework",
            (
                "The core pod is one full-time operator plus two contractors. "
                "Multi-exchange resale, suite seat-splitting, and tentpole hospitality "
                "must have separate inventory, obligation, and settlement ledgers. "
                "This is event-rights brokerage, not wholesale electronics buying."
            ),
            (
                "A confirmed sale does not release working capital. Track transfer "
                "acceptance, event completion, refund exposure, and actual payout "
                "before replenishing inventory."
            ),
            [
                (
                    "Verify acquisition rights",
                    "Document source and permitted resale",
                    1.0,
                    (
                        "Record seller identity, acquisition evidence, event, seat "
                        "identifiers, transfer restrictions, and written authority. "
                        "Apply 15 U.S.C. §45c; never bypass queues, purchase limits "
                        "enforced by covered controls, or ticketing security measures."
                    ),
                ),
                (
                    "Separate deal structures",
                    "Assign one of three ledgers",
                    2.0,
                    (
                        "Exchange resale funds individual tickets before payout; "
                        "suite splitting commits a suite minimum before seats sell; "
                        "tentpole packages combine ticket allotments with distinct "
                        "service deposits. Require venue subdivision permission and "
                        "supplier-specific cancellation terms."
                    ),
                ),
                (
                    "Publish locked inventory",
                    "One authoritative inventory record",
                    3.0,
                    (
                        "Configure SkyBox, Automatiq, or Logitix for supported "
                        "StubHub, Vivid Seats, SeatGeek, and TickPick connections. "
                        "Test reservation propagation and automatic holds; suspend "
                        "affected listings when acknowledgments lag. Never assume "
                        "cross-exchange synchronization is inherently atomic."
                    ),
                ),
                (
                    "Transfer verified entitlements",
                    "Reconcile ticket and service delivery",
                    4.0,
                    (
                        "Capture accepted barcode transfers, named hospitality "
                        "entitlements, suite access credentials, and B2B invoice "
                        "matches. Price with mandatory charges included where "
                        "required; preserve the buyer-facing offer and delivery trail."
                    ),
                ),
                (
                    "Release settled proceeds",
                    "Reconcile event-level cash and profit",
                    5.0,
                    (
                        "Match exchange statements and corporate receipts to each "
                        "sale. Deduct acquisition, sell fees, markdown losses, "
                        "clawback provisions, operating costs, and funding expense. "
                        "Keep cash reserved until the applicable refund and "
                        "post-event settlement obligations are covered."
                    ),
                ),
            ],
        ),
        (
            "diag-02-corporate-buyer-cohort",
            "funnel",
            "One Corporate Buyer Cohort, Five Nested Stages",
            "Measure collected and settled business rather than proposal volume.",
            6,
            "illustrative_model",
            (
                "Illustrative cohort of 200 distinct corporate prospects followed "
                "through their events and final settlement, not necessarily within "
                "30 days. Every later stage is a subset of the preceding stage. "
                "Counts are neither ticket quantities nor canonical revenue inputs."
            ),
            (
                "Conditional conversion is 50%, 50%, 40%, then 60%; "
                "12 settled accounts represent 6% of the original cohort."
            ),
            [
                (
                    "Screened corporate prospects",
                    "200 distinct prospect accounts",
                    200.0,
                    (
                        "Identify a named buyer, relevant event, plausible group "
                        "size, and legitimate business contact route. Deduplicate "
                        "accounts before counting outreach across multiple employees."
                    ),
                ),
                (
                    "Qualified event buyers",
                    "100 accounts; 50% of prospects",
                    100.0,
                    (
                        "Confirm spending authority, event dates, seat requirements, "
                        "payment method, and procurement timing. Exclude accounts "
                        "whose collection timetable cannot fund supplier commitments."
                    ),
                ),
                (
                    "Executable package offers",
                    "50 accounts; 50% of qualified buyers",
                    50.0,
                    (
                        "Issue inventory-backed offers with expiration times, "
                        "mandatory charges, precise inclusions, transfer conditions, "
                        "and cancellation terms. A speculative supplier inquiry "
                        "does not qualify as an executable offer."
                    ),
                ),
                (
                    "Collected buyer deposits",
                    "20 accounts; 40% of offers",
                    20.0,
                    (
                        "Count cleared deposits tied to accepted contracts, not "
                        "unsigned purchase orders. Record deposits as liabilities "
                        "until performance supports revenue recognition; retain "
                        "liquidity against refundable amounts."
                    ),
                ),
                (
                    "Fulfilled settled accounts",
                    "12 accounts; 60% of depositors",
                    12.0,
                    (
                        "Require completed delivery, reconciled supplier costs, "
                        "cleared final payment, and documented residual exposure. "
                        "The other eight depositors remain pending or are canceled; "
                        "their deposits are not automatically earned profit."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "Base Case: $1,010,000 Gross to $191,900 Owner Profit",
            "Six signed bars end at 19.0% gross margin and 47.5% retained margin.",
            3,
            "illustrative_model",
            (
                "Formula v2.0 fixes gross billings, retained_share=0.4, and owner "
                "profit; the expense split below is an illustrative allocation "
                "that reconciles exactly. Gross billings are not net-presented "
                "operator revenue. Normalize fee-net exchange remittances back to "
                "gross once, then deduct the sell fee once. Apply ASC 606 "
                "principal-versus-agent analysis to actual contracts before choosing "
                "financial-statement presentation; the scorecard uses 40% retained "
                "revenue. Owner profit is after modeled operating costs and funding "
                "expense, before owner-specific income taxes."
            ),
            (
                "$1,010,000 - $606,000 - $80,800 - $40,400 - $20,200 - $70,700 "
                "= $191,900. Retained revenue is $404,000; $191,900 / $404,000 "
                "= 47.5%. Conservative: $220,000 gross, $88,000 retained, "
                "$26,400 profit, 12% gross margin, 30% retained margin, "
                "1 FT + 2 C. Base: $1,010,000 gross, $404,000 retained, "
                "$191,900 profit, 19.0% gross margin, 47.5% retained margin, "
                "1 FT + 2 C. Scaled: $1,800,000 gross, $720,000 retained, "
                "$468,000 profit, 26% gross margin, 65% retained margin, "
                "2 FT + 3 C. The sixth bar ends at profit; do not append "
                "profit as another additive bar."
            ),
            [
                (
                    "Gross customer billings",
                    "+$1,010,000 annual gross",
                    1010000.0,
                    (
                        "Aggregate secondary ticket sales, suite-seat sales, and "
                        "VIP package billings before the modeled acquisition and "
                        "selling deductions. Exclude taxes collected for authorities "
                        "and refundable customer deposits awaiting performance."
                    ),
                ),
                (
                    "Ticket and suite acquisition",
                    "-$606,000; $404,000 retained",
                    -606000.0,
                    (
                        "Deduct 60% of gross for face-value inventory and contracted "
                        "ticket, suite, and package acquisition. The resulting 40% "
                        "retained spread is $404,000, not the owner's profit."
                    ),
                ),
                (
                    "Exchange and collection fees",
                    "-$80,800; $323,200 remaining",
                    -80800.0,
                    (
                        "Model blended exchange sell fees and direct collection "
                        "charges at 8% of gross. Match fee schedules to each rail; "
                        "do not apply an exchange fee again to an already "
                        "fee-net remittance."
                    ),
                ),
                (
                    "Unsold inventory and markdown loss",
                    "-$40,400; $282,800 remaining",
                    -40400.0,
                    (
                        "Charge 4% of gross for incremental unsold inventory "
                        "write-offs and markdown variance against the acquisition "
                        "baseline. Do not deduct a realized markdown twice when "
                        "actual gross billings already include its price effect."
                    ),
                ),
                (
                    "Event disruption loss provision",
                    "-$20,200; $262,600 remaining",
                    -20200.0,
                    (
                        "Charge 2% of gross for expected postponement, cancellation, "
                        "refund, and clawback losses net of supportable supplier "
                        "recoveries. Maintain a separate cash liquidity reserve; "
                        "moving cash into that reserve is not another expense."
                    ),
                ),
                (
                    "Operating and funding expense",
                    "-$70,700; $191,900 owner profit",
                    -70700.0,
                    (
                        "Allocate $64,700 to contractor compensation, POS services, "
                        "administration, and other operating costs, plus $6,000 "
                        "to inventory and delayed-payout funding expense. Combined "
                        "monthly cost averages $5,891.67. Payout delay itself "
                        "changes cash timing; its funding cost reduces profit."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-net-yield",
            "horizontal_bars",
            "Compare Fully Loaded Deal Yield by Sub-Niche",
            "Five illustrative unit models use net profit divided by gross receipts.",
            2,
            "illustrative_model",
            (
                "These independent underwriting examples are not measured market "
                "averages and do not determine the canonical scenario mix. Each "
                "deducts acquisition, selling or collection fees, incremental "
                "slippage, expected disruption loss, allocated operations, and "
                "funding cost. Settlement intervals are planning assumptions, "
                "not stated exchange policies."
            ),
            (
                "A higher percentage spread can still consume more cash for longer. "
                "Underwrite settlement dates, refund duties, and supplier deposits "
                "alongside each net yield."
            ),
            [
                (
                    "Multi-exchange ticket resale",
                    "17% net; $170 on $1,000",
                    17.0,
                    (
                        "$1,000 gross less $600 acquisition, $100 exchange fees, "
                        "$40 slippage, $20 disruption provision, $60 operations, "
                        "and $10 funding leaves $170. Fund inventory upfront; "
                        "stress-test payout seven days after event completion."
                    ),
                ),
                (
                    "Suite splitting with ACH",
                    "19% net; $950 on $5,000",
                    19.0,
                    (
                        "$5,000 gross less $3,000 suite allocation, $50 collection "
                        "fees, $300 empty-seat slippage, $150 disruption provision, "
                        "$500 operations, and $50 funding leaves $950. Suite "
                        "minimums remain payable even when individual seats fail "
                        "to sell; ACH collection does not remove refund duties."
                    ),
                ),
                (
                    "Tentpole hospitality with wire",
                    "20% net; $2,000 on $10,000",
                    20.0,
                    (
                        "$10,000 gross less $6,000 package acquisition, $100 "
                        "collection fees, $500 slippage, $300 disruption provision, "
                        "$900 operations, and $200 funding leaves $2,000. Apply "
                        "to Super Bowl, World Cup, F1, or Final Four bundles "
                        "only with documented rights; model a 90-day deposit cycle."
                    ),
                ),
                (
                    "NFL and NBA playoff strips",
                    "7% net; $140 on $2,000",
                    7.0,
                    (
                        "$2,000 gross less $1,200 acquisition, $200 exchange fees, "
                        "$140 slippage, $60 disruption provision, $140 operations, "
                        "and $20 funding leaves $140. Verify SSL and playoff-option "
                        "transfer terms; elimination changes both inventory and "
                        "refund obligations before post-event settlement."
                    ),
                ),
                (
                    "Masters hospitality with card",
                    "16% net; $1,600 on $10,000",
                    16.0,
                    (
                        "$10,000 gross less $6,000 acquisition, $200 collection "
                        "fees, $700 slippage, $400 disruption provision, $900 "
                        "operations, and $200 funding leaves $1,600. Verify each "
                        "badge entitlement and hospitality component; model "
                        "120-day supplier exposure and continuing card disputes."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-risk-decisions",
            "decision_tree",
            "Four Decisions Before Publishing an Offer",
            "Any failed check stops the affected transaction until corrected.",
            5,
            "operating_framework",
            (
                "Apply requirements by event location, customer location, seller "
                "activity, and contract. Federal rules do not replace state "
                "licensing, venue restrictions, or exchange-specific obligations."
            ),
            (
                "Document the answer and evidence for each branch. Strong demand "
                "cannot cure defective acquisition rights, unlawful pricing, "
                "unfunded refunds, or duplicate inventory."
            ),
            [
                (
                    "Acquisition and resale authority",
                    "Pass with evidence; otherwise reject",
                    1.0,
                    (
                        "Check 15 U.S.C. §45c acquisition restrictions and retain "
                        "purchase provenance. Verify sponsor resale permission, "
                        "suite subdivision rights, and event transfer conditions. "
                        "Reject covered circumvention and inventory without "
                        "supportable authority."
                    ),
                ),
                (
                    "Licensing and total price",
                    "Pass after jurisdiction-specific checks",
                    2.0,
                    (
                        "Apply relevant reseller licensing, including New York "
                        "Arts and Cultural Affairs Law Article 25 when applicable. "
                        "Under 16 CFR §§464.2–464.3, display required total pricing "
                        "and avoid fee misrepresentations; account separately for "
                        "permitted exclusions and required prepayment disclosures."
                    ),
                ),
                (
                    "Liquidity and disruption capacity",
                    "Pass only with funded stress coverage",
                    3.0,
                    (
                        "Model rainout, postponement, injury-driven markdown, and "
                        "cancellation. Stress a 30-day payout extension and supplier "
                        "refund arriving after customer reimbursement. If available "
                        "cash cannot fund obligations, reduce position size or "
                        "decline the purchase."
                    ),
                ),
                (
                    "Inventory lock and delivery",
                    "Pass tested synchronization; otherwise pause",
                    4.0,
                    (
                        "Test POS hold propagation, stale-feed alerts, transfer "
                        "eligibility, and emergency delisting across active channels. "
                        "Stress a replacement charge equal to 200% of sale value "
                        "where contract terms support it; this is not a universal "
                        "exchange penalty."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod",
            "org_architecture",
            "Three Core Seats, Two Capacity-Triggered Additions",
            "Base economics use 1 FT + 2 C; scaled economics use 2 FT + 3 C.",
            11,
            "operating_framework",
            (
                "FT means full-time seat; C means contractor seat. The first three "
                "roles form the core pod. Add the fourth and fifth only for the "
                "five-person scaled configuration; do not attribute scaled output "
                "to the unchanged three-person team."
            ),
            (
                "Automation supports pricing, listing synchronization, barcode "
                "transfer, and invoice matching. Named operators still own "
                "exception handling and cash reconciliation."
            ),
            [
                (
                    "Owner and inventory principal",
                    "Core full-time seat; cumulative one",
                    1.0,
                    (
                        "Own acquisition limits, supplier rights, event exposure, "
                        "dynamic drop-curve pricing, and playoff-probability inputs. "
                        "Set position size from available settlement liquidity "
                        "rather than headline inventory markups."
                    ),
                ),
                (
                    "POS and transfer operator",
                    "Core contractor seat; cumulative two",
                    2.0,
                    (
                        "Manage SkyBox, Automatiq, or Logitix exceptions, hold "
                        "acknowledgments, barcode transfers, and emergency channel "
                        "suspension. Reconcile sold inventory against delivery "
                        "evidence before marking orders complete."
                    ),
                ),
                (
                    "Corporate sales coordinator",
                    "Core contractor seat; cumulative three",
                    3.0,
                    (
                        "Qualify corporate buyers, assemble documented package "
                        "offers, collect authorized deposits, and reconcile B2B "
                        "suite invoices. Keep promised access and hospitality "
                        "services aligned with supplier entitlements."
                    ),
                ),
                (
                    "Settlement and event controller",
                    "Scaled full-time seat; cumulative four",
                    4.0,
                    (
                        "Own daily cash forecasting, exchange-statement matching, "
                        "refund exposure, reserve sizing, and event-level profit "
                        "close. Separate bank reconciliation from the operator "
                        "initiating inventory purchases."
                    ),
                ),
                (
                    "Event fulfillment coordinator",
                    "Scaled contractor seat; cumulative five",
                    5.0,
                    (
                        "Handle event-day access exceptions, supplier confirmations, "
                        "group manifests, and service-delivery evidence. Escalate "
                        "missing entitlements before entry time instead of "
                        "substituting undocumented benefits."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $40,000 Without Spending the Refund Buffer",
            "Four buckets fit the canonical $10,000–$50,000 startup envelope.",
            4,
            "illustrative_model",
            (
                "Numeric values are dollar allocations for one $40,000 launch "
                "stack, totaling exactly $40,000. The 40%, 20%, 15%, and 25% "
                "allocation also maps to $10,000 and $50,000 examples. Acquisition "
                "cash and refundable deposits are not automatically expenses; "
                "a cash reserve is not a second profit deduction."
            ),
            (
                "A $10,000 launch should emphasize small, transferable positions. "
                "Do not interpret the capital range as sufficient to warehouse "
                "an entire premium suite or speculative tentpole allotment."
            ),
            [
                (
                    "Liquid resale inventory",
                    "$16,000; 40% of startup capital",
                    16000.0,
                    (
                        "Allocate $4,000 at a $10,000 launch or $20,000 at $50,000. "
                        "Buy small positions with documented transferability and "
                        "multiple demand outlets; cap correlated exposure to "
                        "one team, venue, or event date."
                    ),
                ),
                (
                    "Suite and hospitality deposits",
                    "$8,000; 20% of startup capital",
                    8000.0,
                    (
                        "Allocate $2,000 at a $10,000 launch or $10,000 at $50,000. "
                        "Fund only contract-sized deposits with understood balance "
                        "dates and cancellation terms. Customer prepayment cannot "
                        "justify an uncovered refundable obligation."
                    ),
                ),
                (
                    "Operating setup and runway",
                    "$6,000; 15% of startup capital",
                    6000.0,
                    (
                        "Allocate $1,500 at a $10,000 launch or $7,500 at $50,000. "
                        "Budget applicable licensing, POS onboarding, bookkeeping, "
                        "payment setup, and initial contractor coverage. Recurring "
                        "spending must fit the $1,800–$11,000 monthly operating range."
                    ),
                ),
                (
                    "Settlement and refund liquidity",
                    "$10,000; 25% of startup capital",
                    10000.0,
                    (
                        "Allocate $2,500 at a $10,000 launch or $12,500 at $50,000. "
                        "Hold liquid cash for delayed exchange payout, replacement "
                        "tickets, and customer refunds ahead of supplier recoveries. "
                        "Increase the buffer when correlated event exposure rises."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to an Instrumented Brokerage Desk",
            "Build execution readiness first; the first deal may take 1–3 months.",
            12,
            "operating_framework",
            (
                "Milestones describe implementation work rather than promised "
                "sales. Use operator-owned accounts and authorized supplier "
                "inventory. Do not fund positions that fail rights, liquidity, "
                "pricing, or delivery checks."
            ),
            (
                "By day 30, produce a rights file, tested inventory controls, "
                "a priced offer set, and a cash-exposure report. Revenue and "
                "owner profit follow completed, reconciled transactions."
            ),
            [
                (
                    "Days 1-7",
                    "Map rights and settlement obligations",
                    7.0,
                    (
                        "Choose one initial model, identify applicable reseller "
                        "requirements, inspect supplier contracts, and document "
                        "exchange payout terms. Build separate gross, retained "
                        "revenue, expense, customer-deposit, and cash-reserve accounts."
                    ),
                ),
                (
                    "Days 8-14",
                    "Test inventory and payment controls",
                    14.0,
                    (
                        "Configure the selected POS and supported channels. Test "
                        "holds, stale-feed alerts, authorized transfers, duplicate "
                        "order handling, and invoice matching using permitted test "
                        "procedures. Record observed latency and a manual delisting "
                        "procedure for failed synchronization."
                    ),
                ),
                (
                    "Days 15-21",
                    "Underwrite offers and qualify buyers",
                    21.0,
                    (
                        "Price five small inventory-backed offers with acquisition, "
                        "fees, markdown exposure, disruption provision, operations, "
                        "and funding costs. Begin the corporate cohort ledger; "
                        "collect deposits only against clear contracts and "
                        "supportable delivery rights."
                    ),
                ),
                (
                    "Days 22-30",
                    "Reconcile pilot or rehearse settlement",
                    30.0,
                    (
                        "If a legitimate pilot sale occurs, reconcile payment, "
                        "transfer, and expected payout without declaring premature "
                        "profit. Otherwise rehearse a cancellation and 30-day "
                        "settlement delay. Schedule the next 60 days around the "
                        "canonical 1–3 month first-deal window."
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
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages
        in specs
    ]
