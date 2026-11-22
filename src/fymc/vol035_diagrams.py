from __future__ import annotations

VOLUME_035_SUBTITLE = (
    "The Complete Playbook for Subject-To & Wraparound Note Arbitrage: "
    "$100,000–$850,000 USD in Annual Operator Revenue, "
    "a 1 FT + 3 C (4 People) Core Pod, and a Six-Person Scale Plan"
)

VOLUME_035_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Low-Rate Debt Spread Desk",
        "subtitle": (
            "Acquire subject to existing debt, price acceleration exposure, "
            "and retain documented wraparound payment spreads."
        ),
        "audience": (
            "Experienced residential operators with title counsel, licensed RMLO "
            "relationships, and liquidity beyond the initial setup budget."
        ),
        "research_basis": (
            "12 U.S.C. §1701j-3 generally permits enforcement of contractual "
            "due-on-sale provisions, subject to enumerated limitations. A routine "
            "investor acquisition is not automatically an exempt transfer. The "
            "operating edge therefore depends on verified debt terms, transparent "
            "transfer documentation, and a credible payoff or refinance response."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/12/1701j-3",
            "https://www.ecfr.gov/current/title-12/chapter-I/part-191",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The RMLO-Underwritten Wraparound Desk",
        "subtitle": (
            "Build owner-occupant wrap transactions around documented repayment "
            "capacity, state licensing, and transaction-specific disclosures."
        ),
        "audience": (
            "Small real estate teams prepared to use licensed origination "
            "professionals rather than treating seller exemptions as a shortcut."
        ),
        "research_basis": (
            "12 U.S.C. §§5102–5103 establish SAFE Act definitions and licensing "
            "or registration requirements. Regulation Z, 12 CFR §§1026.36 and "
            "1026.43, governs relevant origination conduct and repayment-capacity "
            "requirements within its scope. The operating policy sends every "
            "owner-occupant wrap buyer through a licensed RMLO; counsel documents "
            "transaction coverage and any applicable exemption. Texas Property "
            "Code §5.016 and Finance Code Chapter 159 require separate analysis."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/12/5102",
            "https://www.law.cornell.edu/uscode/text/12/5103",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/section-1026.36",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/section-1026.43",
            "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.016",
            "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Servicer-Verified Note Spread Pod",
        "subtitle": (
            "Run a four-person core operation around verified collections, "
            "underlying mortgage payments, and tax-and-insurance reconciliation."
        ),
        "audience": (
            "Portfolio operators who value payment evidence, exception handling, "
            "and retained contribution more than property-face-value headlines."
        ),
        "research_basis": (
            "Regulation X servicing provisions, including 12 CFR §§1024.17, "
            "1024.35, and 1024.41 where applicable, identify concrete escrow, "
            "error-resolution, and loss-mitigation responsibilities. A licensed "
            "third-party servicer provides the operating rail; the operator "
            "still reconciles receipts and underlying payments. Texas Finance "
            "Code Chapter 159 adds wrap-specific requirements for covered loans."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1024/section-1024.17",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1024/section-1024.35",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1024/section-1024.41",
            "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_035_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-subject-to-wrap-operating-loop",
            "process_flow",
            "From Existing Debt to Verified Retained Spread",
            "Five linked controls separate a performing wrap from an opaque payment promise.",
            1,
            "operating_framework",
            (
                "Workflow order is operational, not a forecast of five completed "
                "transactions. First-deal timing remains 2–6 months. Property "
                "value, loan principal, escrow deposits, and pass-through debt "
                "service are excluded from canonical operator revenue."
            ),
            (
                "The operator acquires subject to existing debt without assuming "
                "that the original borrower has been released. A wrap adds a "
                "separate buyer obligation; it does not remove the senior lien."
            ),
            [
                (
                    "Source low-equity debt situations",
                    "Match seller needs with verified existing debt",
                    1.0,
                    (
                        "Use county recorder filings, foreclosure notices, and "
                        "authorized seller records to identify low-equity "
                        "situations. Confirm seller objectives, arrears, occupancy, "
                        "and equity before pricing the existing rate advantage."
                    ),
                ),
                (
                    "Underwrite title and acceleration",
                    "Price senior-lien exposure before making commitments",
                    2.0,
                    (
                        "Obtain title work, mortgage statements, reinstatement "
                        "figures, insurance terms, and the actual security "
                        "instrument. Model lender acceleration under 12 U.S.C. "
                        "§1701j-3 and reject transactions without a funded response."
                    ),
                ),
                (
                    "Qualify the wrap buyer",
                    "Route every owner-occupant buyer through licensed origination",
                    3.0,
                    (
                        "Have the licensed RMLO document income, assets, debts, "
                        "credit obligations, and repayment capacity. Apply "
                        "12 CFR §1026.43 where covered and document the treatment "
                        "of taxes, insurance, balloon terms, and payment changes."
                    ),
                ),
                (
                    "Close with transparent payment routing",
                    "Execute recorded instruments and configure licensed servicing",
                    4.0,
                    (
                        "Counsel and title professionals coordinate deed, wrap "
                        "note, security instrument, notices, and lien priority. "
                        "The licensed servicer establishes borrower autopay, "
                        "underlying-payment routing, escrow handling, and reporting."
                    ),
                ),
                (
                    "Reconcile and manage exceptions",
                    "Verify underlying payments before releasing retained cash",
                    5.0,
                    (
                        "Reconcile the wrap ledger, underlying lender statement, "
                        "bank settlement, tax account, and insurance evidence "
                        "monthly. Escalate missing payments immediately; borrower "
                        "autopay success alone does not prove senior-debt payment."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-seller-to-serviced-wrap-funnel",
            "funnel",
            "One Cohort, Five Measurable Conversion Steps",
            "A 500-record sourcing cohort narrows to six funded and boarded wraps.",
            6,
            "illustrative_model",
            (
                "Illustrative six-month cohort, not observed conversion data. "
                "Every stage is a subset of the preceding stage. Counts do not "
                "derive the $475,000 annual Base-Case revenue: annual retained "
                "interest also depends on the seasoned performing portfolio."
            ),
            (
                "Track losses by reason: seller mismatch, title defects, "
                "acceleration liquidity, buyer repayment capacity, and closing "
                "attrition. Do not count an application as a funded wrap."
            ),
            [
                (
                    "Screened seller records",
                    "500 unique records establish the cohort denominator",
                    500.0,
                    (
                        "Deduplicate property and owner records, verify the "
                        "trigger date, and document contact eligibility. This "
                        "starting population represents 100% of the defined cohort."
                    ),
                ),
                (
                    "Documented seller conversations",
                    "150 conversations equal 30% of screened records",
                    150.0,
                    (
                        "Count only sellers who discuss debt terms and transaction "
                        "objectives. The remaining 350 records never advance into "
                        "documented underwriting during this cohort window."
                    ),
                ),
                (
                    "Debt-and-title qualified opportunities",
                    "45 opportunities equal 30% of seller conversations",
                    45.0,
                    (
                        "Require usable debt evidence, preliminary title findings, "
                        "a priceable arrears position, and a credible acceleration "
                        "response. These opportunities equal 9% of starting records."
                    ),
                ),
                (
                    "Matched and underwritten wrap files",
                    "12 files equal 26.7% of qualified opportunities",
                    12.0,
                    (
                        "Each file has a specific qualified buyer, licensed RMLO "
                        "review, documented repayment analysis, and counsel-reviewed "
                        "structure. These files equal 2.4% of starting records."
                    ),
                ),
                (
                    "Funded and servicer-boarded wraps",
                    "Six closings equal 50% of underwritten files",
                    6.0,
                    (
                        "Count only executed closings with confirmed funding, "
                        "recording submission, servicing setup, and an underlying "
                        "payment schedule. Final conversion equals 1.2% of records."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-retained-revenue-waterfall",
            "waterfall",
            "$475,000 Operator Revenue to $190,000 Owner Profit",
            "Four expense deductions reconcile exactly to the Base-Case 40.0% net margin.",
            3,
            "illustrative_model",
            (
                "Annual USD. First and final bars are totals; intervening bars "
                "are signed deductions. Canonical revenue already excludes home "
                "face value and pass-through debt service. The four expense "
                "allocations are editorial assumptions totaling $285,000, not "
                "additional canonical inputs. Do not deduct senior debt twice."
            ),
            (
                "Conservative: $100,000 revenue less $72,000 expenses equals "
                "$28,000 profit at 28%. Base: $475,000 less $285,000 equals "
                "$190,000 at 40.0%. Scaled: $850,000 less $408,000 equals "
                "$442,000 at 52%. Core staffing is four people; scaled staffing "
                "is six. These are annual scenarios, not month-one run rates."
            ),
            [
                (
                    "Gross operator revenue",
                    "$475,000 annual retained-spread revenue before operating expenses",
                    475000.0,
                    (
                        "Illustratively, $210,000 earned net upfront spreads plus "
                        "$265,000 retained annual wrap interest equals $475,000. "
                        "Do not book every cash down payment as earned revenue. "
                        "Apply transaction-specific accounting: interest follows "
                        "applicable interest guidance, while any ASC 606 service "
                        "component requires its own principal-versus-agent analysis."
                    ),
                ),
                (
                    "Acquisition and closing expenses",
                    "Subtract $100,000 of annual direct transaction expenses",
                    -100000.0,
                    (
                        "Allocate sourcing, title, recording, counsel, and "
                        "transaction-specific origination expenses not already "
                        "netted from upfront spreads. Running contribution becomes "
                        "$375,000; property purchase principal is excluded."
                    ),
                ),
                (
                    "Realized losses and carrying expenses",
                    "Subtract $80,000 of annual loss and workout expenses",
                    -80000.0,
                    (
                        "Model recognized credit losses, property protection, "
                        "workout counsel, and nonrecoverable carrying expenses. "
                        "Running contribution becomes $295,000. Moving cash into "
                        "a reserve account is not itself an expense."
                    ),
                ),
                (
                    "Contractor and servicing expenses",
                    "Subtract $60,000 of annual recurring delivery expenses",
                    -60000.0,
                    (
                        "Cover recurring contractor retainers, licensed servicing "
                        "charges, reconciliation support, and borrower-service "
                        "administration. Running contribution becomes $235,000; "
                        "exclude origination charges already assigned above."
                    ),
                ),
                (
                    "Systems and administrative overhead",
                    "Subtract $45,000 of annual recurring overhead expenses",
                    -45000.0,
                    (
                        "Cover CRM, document controls, bookkeeping, business "
                        "insurance, and administrative support. Combined with "
                        "the prior $60,000, recurring overhead equals $105,000 "
                        "annually, or $8,750 monthly, within the stated opex range."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$190,000 remaining profit equals exactly 40.0% margin",
                    190000.0,
                    (
                        "Calculate $475,000 minus $100,000 minus $80,000 minus "
                        "$60,000 minus $45,000. Owner distributions and personal "
                        "taxes are outside this illustrative operating bridge; "
                        "profit does not equal immediately distributable cash."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-contractual-rate-spreads",
            "horizontal_bars",
            "Five Sub-Niches, One Consistent Spread Measure",
            "Compare contractual rate-spread proxies, not borrower APR or investor return.",
            2,
            "illustrative_model",
            (
                "Numeric values are annual percentage-point differences between "
                "illustrative wrap and underlying note rates. Rates are examples, "
                "not market quotes. Unequal balances, amortization, defaults, "
                "fees, escrow, and prepayments change actual retained yield."
            ),
            (
                "At equal $100,000 interest-only balances, one percentage point "
                "equals $1,000 annual gross interest spread. Actual underwriting "
                "must model both amortization schedules and monthly cash timing."
            ),
            [
                (
                    "Clean-payment low-equity resale",
                    "3.0 percentage points from 6.5% less 3.5%",
                    3.0,
                    (
                        "Illustrative equal-balance gross spread is $3,000 "
                        "annually per $100,000. Use licensed-servicer ACH "
                        "collections and verify senior-lender settlement rather "
                        "than relying on a buyer payment screenshot."
                    ),
                ),
                (
                    "Relocation seller with seasoned debt",
                    "3.5 percentage points from 7.0% less 3.5%",
                    3.5,
                    (
                        "Illustrative equal-balance gross spread is $3,500 "
                        "annually per $100,000. Confirm occupancy and insurance "
                        "changes, obtain a complete payment history, and model "
                        "seller release separately from the property transfer."
                    ),
                ),
                (
                    "Documented reinstatement opportunity",
                    "4.0 percentage points from 7.5% less 3.5%",
                    4.0,
                    (
                        "Illustrative equal-balance gross spread is $4,000 "
                        "annually per $100,000. A higher spread can disappear "
                        "after arrears, reinstatement fees, foreclosure deadlines, "
                        "and a delayed first wrap payment."
                    ),
                ),
                (
                    "Self-employed owner-occupant buyer",
                    "4.5 percentage points from 8.0% less 3.5%",
                    4.5,
                    (
                        "Illustrative equal-balance gross spread is $4,500 "
                        "annually per $100,000. Require RMLO-reviewed income "
                        "evidence and repayment capacity; a larger down payment "
                        "does not replace the required underwriting analysis."
                    ),
                ),
                (
                    "Texas covered wrap transaction",
                    "5.0 percentage points from 8.5% less 3.5%",
                    5.0,
                    (
                        "Illustrative equal-balance gross spread is $5,000 "
                        "annually per $100,000. Price only after reviewing Texas "
                        "Finance Code Chapter 159, Property Code §5.016, "
                        "applicable rate limits, licensing, and required disclosures."
                    ),
                ),
            ],
        ),
        (
            "diag-05-wrap-preflight-decision-tree",
            "decision_tree",
            "Four Decisions Before Committing Capital",
            "Each affirmative branch advances; each unresolved branch stops commitment.",
            5,
            "operating_framework",
            (
                "The four nodes are sequential decision checks. Stage numbers "
                "represent order, not probabilities. Transaction scope, state "
                "requirements, lien terms, and borrower use determine the "
                "applicable rules; a servicer does not cure defective origination."
            ),
            (
                "Do not conceal a transfer, substitute a trust label for "
                "statutory analysis, or infer lender permission from continued "
                "payment acceptance. Keep written evidence for every decision."
            ),
            [
                (
                    "Can acceleration be absorbed?",
                    "Yes advances; absent funding means decline the acquisition",
                    1.0,
                    (
                        "Review 12 U.S.C. §1701j-3 and the actual due-on-sale "
                        "clause. Document lender permission where obtained or "
                        "specific statutory protection where applicable. Otherwise "
                        "quantify payoff exposure and verify available liquidity "
                        "or a credible refinance plan."
                    ),
                ),
                (
                    "Is origination properly structured?",
                    "Yes advances; deficient underwriting returns to licensed RMLO",
                    2.0,
                    (
                        "Route every owner-occupant wrap buyer through a licensed "
                        "RMLO. Map SAFE Act requirements under 12 U.S.C. "
                        "§§5102–5103 and Regulation Z §§1026.36 and 1026.43. "
                        "Document coverage, repayment capacity, compensation "
                        "treatment, and any specifically applicable exemption."
                    ),
                ),
                (
                    "Are state wrap requirements satisfied?",
                    "Yes advances; missing notices stop closing preparation",
                    3.0,
                    (
                        "For Texas, counsel checks Property Code §5.016 for "
                        "covered encumbered-property conveyances, including "
                        "applicable advance notices, and Finance Code Chapter "
                        "159 for wrap licensing and transaction duties. Document "
                        "recipient, delivery timing, closing conditions, and "
                        "applicable exceptions rather than copying generic forms."
                    ),
                ),
                (
                    "Can title and payments remain controlled?",
                    "Yes permits closing; unresolved control defects require remediation",
                    4.0,
                    (
                        "Confirm lien priority, current taxes, insurance interests, "
                        "and foreclosure remedies. Contract a licensed third-party "
                        "servicer, document applicable Regulation X duties, test "
                        "underlying-payment reporting, and fund transaction-specific "
                        "reserves before accepting buyer funds."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-person-core-six-person-scale-pod",
            "org_architecture",
            "Four Core Seats, Six at Scaled Volume",
            "One full-time owner and three contractors form the canonical starting pod.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person. Core seats total "
                "1 FT + 3 C; adding both expansion seats produces 2 FT + 4 C. "
                "Title companies, lenders, and the servicer are external vendors, "
                "not extra dedicated pod seats. Contractor credentials must fit "
                "the actual duties assigned."
            ),
            (
                "The owner controls capital and exceptions; the RMLO owns buyer "
                "underwriting; counsel owns transaction documents; servicing "
                "operations verifies the licensed servicer's payment evidence."
            ),
            [
                (
                    "Core owner and acquisition lead",
                    "One full-time seat owns pricing and capital decisions",
                    1.0,
                    (
                        "Maintain seller relationships, approve documented "
                        "underwriting assumptions, manage acceleration liquidity, "
                        "and review weekly pipeline aging. Personally resolve "
                        "material exceptions rather than delegating risk acceptance "
                        "to an automated CRM status."
                    ),
                ),
                (
                    "Core licensed RMLO",
                    "One contractor seat owns buyer origination and underwriting",
                    1.0,
                    (
                        "Collect repayment evidence, document applicable ability-"
                        "to-repay analysis, manage required borrower disclosures, "
                        "and coordinate permissible origination compensation. "
                        "Reject incomplete files before the closing calendar "
                        "creates pressure to bypass review."
                    ),
                ),
                (
                    "Core real estate counsel",
                    "One contractor seat owns statutory analysis and documents",
                    1.0,
                    (
                        "Review transfer restrictions, state wrap requirements, "
                        "security instruments, remedies, and title exceptions. "
                        "Coordinate external title and settlement vendors and "
                        "maintain a transaction-specific notice evidence checklist."
                    ),
                ),
                (
                    "Core servicing operations specialist",
                    "One contractor seat owns independent monthly payment reconciliation",
                    1.0,
                    (
                        "Reconcile licensed-servicer reports against underlying "
                        "lender statements and bank records. Track taxes, "
                        "insurance, borrower inquiries, and delinquency aging; "
                        "this seat does not substitute for required servicing "
                        "licenses or external servicer functions."
                    ),
                ),
                (
                    "Scaled portfolio operations lead",
                    "Second full-time seat adds capacity for portfolio exceptions",
                    1.0,
                    (
                        "Add at scaled workload to manage reconciliations, "
                        "collection escalation, servicer service levels, and "
                        "cash forecasting. The owner retains capital decisions "
                        "while this seat prevents exception queues from aging."
                    ),
                ),
                (
                    "Scaled diligence and coordination specialist",
                    "Fourth contractor seat expands document and closing capacity",
                    1.0,
                    (
                        "Collect authorized records, maintain title and insurance "
                        "checklists, coordinate document delivery, and track "
                        "closing dependencies. Leave regulated origination, "
                        "legal interpretation, and licensed servicing activity "
                        "with the appropriately credentialed providers."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-four-bucket-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Buying Payment Spread",
            "Four buckets reconcile to lean $12,000, planning $35,000, and expanded $65,000.",
            4,
            "illustrative_model",
            (
                "Numeric values show the $35,000 planning stack in USD. Every "
                "detail supplies corresponding lean and expanded allocations. "
                "These are setup-and-liquidity budgets, not property purchase "
                "prices, annual expenses, or a promise that acceleration can "
                "be funded from startup cash."
            ),
            (
                "Lean total: $3,000 + $4,000 + $2,000 + $3,000 = $12,000. "
                "Planning total: $8,000 + $10,000 + $7,000 + $10,000 = $35,000. "
                "Expanded total: $15,000 + $20,000 + $10,000 + $20,000 = $65,000."
            ),
            [
                (
                    "Professional structure and document setup",
                    "$8,000 planning allocation establishes transaction-specific operating documents",
                    8000.0,
                    (
                        "Lean $3,000; planning $8,000; expanded $15,000. Fund "
                        "counsel review, RMLO engagement setup, entity records, "
                        "state requirement mapping, and initial title diligence. "
                        "Per-closing costs still require separate transaction budgets."
                    ),
                ),
                (
                    "Transaction and reinstatement liquidity",
                    "$10,000 planning allocation supports documented closing cash requirements",
                    10000.0,
                    (
                        "Lean $4,000; planning $10,000; expanded $20,000. Hold "
                        "cash for verified arrears, title cures, and closing "
                        "timing differences. Decline deals whose cure requirements "
                        "exceed committed funds; these amounts cannot fund an "
                        "arbitrary senior-mortgage payoff."
                    ),
                ),
                (
                    "Sourcing and servicing infrastructure",
                    "$7,000 planning allocation builds auditable records and payment rails",
                    7000.0,
                    (
                        "Lean $2,000; planning $7,000; expanded $10,000. Configure "
                        "a CRM such as HubSpot, access-controlled document storage, "
                        "licensed-servicer boarding, bookkeeping, and payment "
                        "reconciliation exports. Use dual review for payment "
                        "destination changes."
                    ),
                ),
                (
                    "Runway and exception cash reserve",
                    "$10,000 planning allocation protects early operating continuity",
                    10000.0,
                    (
                        "Lean $3,000; planning $10,000; expanded $20,000. Preserve "
                        "cash for operating delays and payment exceptions. At "
                        "$2,000–$12,000 monthly opex, $10,000 covers roughly "
                        "0.83–5 months before transaction shocks; arrange more "
                        "runway when the 2–6 month first-deal window requires it."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-operating-sprint",
            "timeline_roadmap",
            "Thirty Days to a Documented Operating System",
            "Build sourcing, underwriting, closing controls, and payment evidence before scaling.",
            12,
            "operating_framework",
            (
                "Four milestone values are ending calendar days: 7, 14, 21, "
                "and 30. This sprint prepares the operation; the canonical "
                "first-deal expectation remains 2–6 months. Do not force a "
                "closing into thirty days to satisfy the diagram."
            ),
            (
                "Day 30 success means an auditable acquisition and servicing "
                "process with named owners, funded operating runway, and a "
                "qualified pipeline—not an assumed funded transaction."
            ),
            [
                (
                    "Days 1-7",
                    "Select the market and document statutory operating requirements",
                    7.0,
                    (
                        "Owner and counsel choose one jurisdiction, review "
                        "12 U.S.C. §1701j-3 and applicable state wrap rules, "
                        "engage the RMLO, and map title, disclosure, and servicing "
                        "responsibilities. Deliver a written transaction checklist "
                        "and startup cash allocation."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure sourcing records and rehearse the underwriting workflow",
                    14.0,
                    (
                        "Build the deduplicated seller cohort, configure CRM "
                        "stage definitions, and assemble an authorized sample "
                        "file. Test senior-debt amortization, wrap amortization, "
                        "escrow changes, default carrying cost, and acceleration "
                        "liquidity in a spreadsheet."
                    ),
                ),
                (
                    "Days 15-21",
                    "Validate buyer qualification and licensed-servicer payment controls",
                    21.0,
                    (
                        "Have the RMLO review a qualified buyer file when "
                        "available; otherwise rehearse with clearly synthetic "
                        "records. Confirm servicer licensing and contractual "
                        "scope, test reconciliation exports without live funds, "
                        "and rehearse a failed underlying payment escalation."
                    ),
                ),
                (
                    "Days 22-30",
                    "Review qualified files and prove end-to-end exception handling",
                    30.0,
                    (
                        "Counsel reviews candidate documents and notice timing; "
                        "operations completes a mock monthly reconciliation. "
                        "The owner verifies runway and deal-specific liquidity, "
                        "records unresolved defects, and schedules only files "
                        "that satisfy the documented requirements."
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
