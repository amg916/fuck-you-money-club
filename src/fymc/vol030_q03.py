from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for lending & flash-funding arbitrage?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Escrow-Locked Fee Cohorts, ASC 606 Presentation, UCC Account Control, Promotional Credit Costs & Chapter 11 Recovery Timing",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #30, Lending & Flash-Funding Arbitrage, holds Rank #04 of 36 "
        "with a 93/100 Money-to-Manpower Score across 14 mapped plays. The "
        "economic asset is an earned funding fee, documented EMD participation, "
        "or origination point, never principal passing through escrow. Formula "
        "v2.0 fixes annual owner profit at $36,000 Conservative, $227,375 Base, "
        "and $522,500 Scaled. This chapter reconstructs those outcomes through "
        "explicit fee cohorts, reversals, contractor labor, acquisition costs, "
        "capital charges, credit losses, and overhead. It separates fee DSO "
        "from principal release locks, sizes simultaneous funding commitments, "
        "and tests promotional-credit resets and bankruptcy-claim delays. "
        "The operating discipline is simple: price every locked dollar, "
        "verify repayment cash independently, and reject apparent yield "
        "created by omitted costs or unsupported recoveries."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual gross earned-fee basis; escrow principal excluded",
            "note": "30% margin; $36,000 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$535,000",
            "context": "Annual gross earned-fee basis; escrow principal excluded",
            "note": "42.5% margin; $227,375 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$950,000",
            "context": "Annual gross earned-fee basis; escrow principal excluded",
            "note": "55% margin; $522,500 owner profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Define the earned-fee cohort before measuring yield",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Build the ledger around a funded transaction identifier, not the wire "
                    "amount. For each transaction, record committed principal, principal "
                    "actually released, contractual fee, earned date, fee settlement date, "
                    "principal return date, capital provider, and beneficiary verification "
                    "evidence. A $100,000 escrow advance that returns $103,500 contains "
                    "$100,000 of recovered principal and $3,500 of potential fee income; "
                    "it does not create $103,500 of revenue. Separate refundable deposits "
                    "and unearned charges from earned fees. An origination point on a "
                    "$100,000 facility produces $1,000 only when the contract and applicable "
                    "accounting policy support recognition. Track principal as an asset "
                    "and recovered principal as an asset conversion. Do not recognize "
                    "uncollected interest merely because the bank statement shows a "
                    "larger payoff request. Use QuickBooks Online or a comparable ledger "
                    "with a transaction subledger exported from the settlement platform. "
                    "ALTA settlement statements, executed funding agreements, and bank "
                    "confirmations must reconcile to the same identifier. A proof-of-funds "
                    "letter documents stated capacity, not cash already available for "
                    "repayment. Revenue quality depends on enforceable entitlement, "
                    "completed performance, and collection evidence rather than the "
                    "apparent velocity of repeated wires. Report funded counts alongside "
                    "canceled applications so the denominator cannot conceal underwriting waste."
                ),
                (
                    "The illustrative cohorts reproduce the canonical fee totals without "
                    "inventing principal revenue. Conservative comprises 40 transactional "
                    "closings at $2,000, 20 EMD participations at $1,500, and ten "
                    "originations at $1,000: $120,000 across 70 fee events. Base comprises "
                    "100 closings at $3,500, 60 EMD participations at $2,500, and 35 "
                    "originations at $1,000: $535,000 across 195 events. Scaled comprises "
                    "150 closings at $4,500, 80 EMD participations at $3,000, and 35 "
                    "originations at $1,000: $950,000 across 265 events. These are "
                    "reconciliation assumptions, not observed production or quoted market "
                    "pricing. Count a fee event separately from a unique customer; a "
                    "repeat sponsor can generate several events, while one closing can "
                    "contain multiple separately documented services. Avoid billing the "
                    "same service twice under different labels. The EMD assumptions "
                    "require enforceable participation economics and eligible escrow "
                    "conditions. Ordinary early-stage earnest-money advances often lack "
                    "unconditional end-buyer cash, so they fail this platform's release "
                    "standard. Exclude those opportunities rather than weakening verification "
                    "to preserve the modeled count. If the eligible pipeline cannot "
                    "supply 60 Base participations, reduce revenue explicitly and rebuild "
                    "the cost waterfall; do not substitute unsigned JV expectations."
                ),
                (
                    "Resolve gross-versus-net presentation at the contract level. The "
                    "scorecard uses the operator's earned transactional fees, EMD JV "
                    "splits, and origination points before the modeled deductions. It "
                    "does not authorize recognizing a partner's entire settlement "
                    "entitlement. If a JV collects $5,000 but this operator owns a "
                    "50% participation, the modeled EMD fee is $2,500. Store retained_share "
                    "as 0.50 for that contract and reconcile the other $2,500 to its "
                    "owner. Where ASC 606 applies, evaluate principal-versus-agent "
                    "presentation; lending interest and certain origination fees instead "
                    "require analysis under the relevant lending guidance, including "
                    "ASC 310-20. Do not force every funding charge into service revenue. "
                    "Here, the fee cohorts already reflect the operator's entitlement, "
                    "so applying a second participation haircut would understate income. "
                    "The reversal allowance below reduces that earned-fee planning basis "
                    "for expected concessions and failed settlements. Accordingly, the "
                    "canonical margins use gross fee revenue as their denominator, "
                    "not financial-statement revenue after contra-revenue adjustments. "
                    "Preserve both views in the workbook with explicit labels. Review "
                    "state licensing and interest characterization before quoting a "
                    "$3,500 charge for three days: commercial purpose, a corporate "
                    "borrower, or a fee label alone does not establish an exemption."
                ),
            ],
            "table": {
                "caption": "Earned-Fee Cohorts and Recognition Boundaries by Operating Rail",
                "headers": [
                    "Operating rail and evidence",
                    "Conservative fee construction",
                    "Base fee construction",
                    "Scaled fee construction",
                ],
                "rows": [
                    [
                        "Transactional closings require separately executed funding fee agreements",
                        "Forty completed closings multiply by $2,000, producing $80,000",
                        "One hundred completed closings multiply by $3,500, producing $350,000",
                        "One hundred fifty completed closings multiply by $4,500, producing $675,000",
                    ],
                    [
                        "EMD participations include only the operator's enforceable entitlement",
                        "Twenty qualifying participations multiply by $1,500, producing $30,000",
                        "Sixty qualifying participations multiply by $2,500, producing $150,000",
                        "Eighty qualifying participations multiply by $3,000, producing $240,000",
                    ],
                    [
                        "Origination fees require completed performance and documented accounting treatment",
                        "Ten recognized origination events multiply by $1,000, producing $10,000",
                        "Thirty-five recognized origination events multiply by $1,000, producing $35,000",
                        "Thirty-five recognized origination events multiply by $1,000, producing $35,000",
                    ],
                    [
                        "Annual gross fee basis excludes all returned funding principal",
                        "Seventy earned fee events together produce exactly $120,000",
                        "One hundred ninety-five earned fee events produce exactly $535,000",
                        "Two hundred sixty-five earned fee events produce exactly $950,000",
                    ],
                    [
                        "JV retained_share applies before entering the operator revenue cohort",
                        "A $3,000 settlement with 50% entitlement contributes only $1,500",
                        "A $5,000 settlement with 50% entitlement contributes only $2,500",
                        "A $6,000 settlement with 50% entitlement contributes only $3,000",
                    ],
                    [
                        "Principal movement belongs in the funding asset subledger",
                        "A returned $100,000 advance adds zero earned fee revenue",
                        "A returned $100,000 advance adds zero earned fee revenue",
                        "A returned $100,000 advance adds zero earned fee revenue",
                    ],
                    [
                        "Release eligibility requires independently verified unconditional end-buyer cash",
                        "Reject unsupported deposits even when projected fee revenue falls",
                        "Remove ineligible EMD events before relying on cohort totals",
                        "Increase verified eligible production rather than relaxing release conditions",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Keep attractive settlement totals from contaminating earnings",
                "body": (
                    "Veteran operators reconcile entitlement, release authority, and collection "
                    "timing before discussing annualized fee yield."
                ),
                "items": [
                    "Assign separate principal, earned-fee, partner-payable, and reversal accounts to every escrow identifier; a returned advance must never credit fee revenue.",
                    "Obtain the settlement agent's wire callback number from an independently established source, then verify beneficiary instructions outside the originating email thread.",
                    "Track cancellation reasons by referring wholesaler and title office; repeated unfunded end-buyers should change acquisition spending before they become credit losses.",
                    "Require written fee allocation on each JV statement; calculate retained_share once, then prohibit a second partner deduction in the owner-profit workbook.",
                ],
            },
        },
        {
            "heading": "2. Reconcile every dollar from fee billings to owner profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Treat the canonical owner-profit figures as fixed reconciliation "
                    "targets and the expense allocation as an explicit illustrative "
                    "budget. Conservative deducts $6,000 of fee reversals, $24,000 of "
                    "delivery labor, $18,000 of acquisition spending, $12,000 of capital "
                    "charges, $6,000 of expected principal losses, and $18,000 of overhead. "
                    "The $84,000 deduction leaves $36,000. Base deducts $16,050, $72,000, "
                    "$55,000, $75,000, $21,400, and $68,175 respectively. Total deductions "
                    "of $307,625 leave $227,375. Scaled deducts $19,000, $110,000, "
                    "$75,000, $95,000, $28,500, and $100,000, leaving $522,500 after "
                    "$427,500 of deductions. Those profits divided by $120,000, "
                    "$535,000, and $950,000 equal 30%, 42.5%, and 55%. The "
                    "reversal rates decline from 5% to 3% to 2% because "
                    "the illustration assumes better screening, not because scale "
                    "automatically eliminates disputes. Expected principal-loss budgets "
                    "equal 5%, 4%, and 3% of the fee basis solely "
                    "as planning allocations; actual loss estimation must use funded "
                    "exposure, default probability, recoveries, and concentration. Replace "
                    "these allocations with observed cohort experience without silently "
                    "altering the published canonical scenario. Any revised production "
                    "forecast belongs in a separately labeled operating version."
                ),
                (
                    "Make contractor delivery labor measurable rather than hiding it "
                    "inside a target margin. The Base $72,000 budget can represent "
                    "1,200 settlement-review hours at $40 plus 600 underwriting-support "
                    "hours at $40, allocated between two contractors. At 195 fee "
                    "events, that is $369.23 of delivery labor per event before "
                    "acquisition work. Base acquisition spending of $55,000 across "
                    "50 newly activated sponsor relationships gives a $1,100 customer "
                    "CAC; dividing by 195 events gives $282.05 of acquisition expense "
                    "per event, a different metric. Record repeat business separately "
                    "so neither denominator is mistaken for the other. The owner "
                    "is the single full-time operator in Conservative and Base. "
                    "Scaled uses two full-time people and three contractors; its "
                    "$110,000 delivery budget includes $60,000 of contractor charges "
                    "and $50,000 of loaded nonowner employee cost. Owner profit "
                    "remains the residual available for owner compensation and distributions, "
                    "without deducting an additional hypothetical owner salary. Overhead "
                    "covers software, insurance, bookkeeping, professional review, and "
                    "administration. Its monthly equivalents are $1,500, $5,681.25, and "
                    "$8,333.33; adding paid delivery labor produces $3,500, $11,681.25, "
                    "and $17,500. Therefore, the advertised $2,000–$12,000 monthly opex "
                    "range cannot serve as an all-in ceiling at Scaled."
                ),
                (
                    "Maintain two loss mechanisms because a canceled fee and missing "
                    "principal have different economics. Fee scrubs, negotiated refunds, "
                    "and billing reversals reduce the fee basis; losses on funding "
                    "assets consume capital and require an exposure-based allowance. "
                    "A cash reserve is a liquidity designation, not an additional "
                    "expense when the same expected loss has already entered the "
                    "waterfall. When an anticipated loss becomes a write-off, charge "
                    "the established allowance and recognize only the necessary "
                    "incremental adjustment. Likewise, paying a previously accrued "
                    "refund settles a liability rather than creating a second "
                    "deduction. At Base, $535,000 less $16,050 of reversals yields "
                    "$518,950 of net fees before the remaining expenses. Dividing "
                    "$227,375 by that net figure produces approximately 43.81%, "
                    "which must not replace the scorecard's 42.5% gross-basis margin. "
                    "Allocate the $75,000 Base capital budget transparently: 100 "
                    "transactional events at $500 cost $50,000, 60 EMD events "
                    "at $400 cost $24,000, and facility administration costs $1,000. "
                    "These are negotiated-budget assumptions, not lending quotes. "
                    "Avoid counting a capital partner's share twice when the "
                    "contract already defines revenue net of that entitlement. "
                    "Reconcile contractual payment priority before assigning any amount "
                    "to revenue, financing cost, or partner payable."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Gross-Fee-to-Owner-Profit Waterfall in Annual Dollars",
                "headers": [
                    "Waterfall line and treatment",
                    "Conservative annual reconciliation",
                    "Base annual reconciliation",
                    "Scaled annual reconciliation",
                ],
                "rows": [
                    [
                        "Start with earned operator fees before modeled reversal deductions",
                        "$120,000 gross fees exclude every dollar of escrow principal",
                        "$535,000 gross fees exclude every dollar of escrow principal",
                        "$950,000 gross fees exclude every dollar of escrow principal",
                    ],
                    [
                        "Deduct fee scrubs and reversals as contra-revenue allowances",
                        "Subtract $6,000 for expected reversals, representing 5% of fees",
                        "Subtract $16,050 for expected reversals, representing 3% of fees",
                        "Subtract $19,000 for expected reversals, representing 2% of fees",
                    ],
                    [
                        "Show net fees as a subtotal without another deduction",
                        "$114,000 remains after subtracting the fee reversal allowance",
                        "$518,950 remains after subtracting the fee reversal allowance",
                        "$931,000 remains after subtracting the fee reversal allowance",
                    ],
                    [
                        "Deduct paid delivery labor including contractors and nonowner employees",
                        "Subtract $24,000 of paid contractor review and settlement labor",
                        "Subtract $72,000 of paid contractor review and settlement labor",
                        "Subtract $110,000 including $60,000 contractors and $50,000 loaded employment",
                    ],
                    [
                        "Deduct acquisition spending using distinct customer and transaction denominators",
                        "Subtract $18,000 of referral development and customer acquisition spending",
                        "Subtract $55,000 of referral development and customer acquisition spending",
                        "Subtract $75,000 of referral development and customer acquisition spending",
                    ],
                    [
                        "Deduct capital charges without treating principal repayments as expenses",
                        "Subtract $12,000 of documented financing and facility servicing charges",
                        "Subtract $75,000 of documented financing and facility servicing charges",
                        "Subtract $95,000 of documented financing and facility servicing charges",
                    ],
                    [
                        "Deduct expected principal losses separately from fee reversal allowances",
                        "Subtract $6,000 of estimated credit losses on funded exposures",
                        "Subtract $21,400 of estimated credit losses on funded exposures",
                        "Subtract $28,500 of estimated credit losses on funded exposures",
                    ],
                    [
                        "Deduct overhead separately from paid delivery and financing expenses",
                        "Subtract $18,000 for insurance, software, administration, and professional review",
                        "Subtract $68,175 for insurance, software, administration, and professional review",
                        "Subtract $100,000 for insurance, software, administration, and professional review",
                    ],
                    [
                        "Retain canonical owner profit using gross fees as denominator",
                        "$36,000 owner profit equals 30% of $120,000 gross fees",
                        "$227,375 owner profit equals 42.5% of $535,000 gross fees",
                        "$522,500 owner profit equals 55% of $950,000 gross fees",
                    ],
                ],
            },
        },
        {
            "heading": "3. Size principal locks separately from fee DSO and promotional credit",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A profitable cohort can fail because principal returns after "
                    "the next commitment becomes payable. Measure three clocks: "
                    "principal lock from funding release to reusable cleared cash, "
                    "fee DSO from earned date to collection, and facility repayment "
                    "from borrowing to its contractual due date. The Base illustration "
                    "assumes $100,000 average transactional principal for 100 events "
                    "and three calendar days of lock. Average occupied capital "
                    "is $100,000 times 100 times three divided by 365, or "
                    "$82,192. Add 60 EMD events at $25,000 with ten-day locks: "
                    "$41,096 average occupied capital. Their combined $123,288 average "
                    "does not establish adequate capacity. Two simultaneous transactional "
                    "closings require $200,000, and three simultaneous EMD positions "
                    "require another $75,000. These overlap assumptions are planning "
                    "limits, not measured percentiles. Weekend cutoffs, bank holidays, "
                    "recording delays, and returned wires can expand calendar-day "
                    "locks even when documents describe same-day funding. End-buyer "
                    "cash must be unconditional, independently verified on deposit, "
                    "and available under the settlement instructions before release "
                    "strictly to a bonded title or settlement agent. Bonding does "
                    "not replace verification or prove that a loss is covered. "
                    "Confirm coverage limits, exclusions, and the identity of the "
                    "protected party rather than treating a certificate as repayment."
                ),
                (
                    "Build the liquidity envelope from cash obligations rather than "
                    "adding every balance-sheet metric together. Base cash operating "
                    "deductions, excluding reversal and credit-loss allowances, total "
                    "$270,175 annually. A 21-day expense runway therefore requires "
                    "$15,544 rounded to whole dollars. Add the $275,000 simultaneous "
                    "principal commitment and a separately designated $37,450 cash "
                    "buffer matching the modeled reversal and credit-loss allowances. "
                    "The resulting planning envelope is $327,994. This buffer is "
                    "cash earmarked against already modeled expenses, not another "
                    "profit deduction. With $100,000 of genuinely available equity, "
                    "the remaining capacity requirement is $227,994; with $25,000, "
                    "it is $302,994. Neither figure establishes that a lender "
                    "will provide the facility. At five-day fee DSO, Base fee "
                    "receivables average approximately $7,329 using $535,000 divided "
                    "by 365 times five. Report that receivable as a collection "
                    "indicator rather than automatically adding it to the expense "
                    "runway, which already bridges operating payments. A daily cash "
                    "schedule must capture exact overlaps, collateral restrictions, "
                    "facility availability, and minimum balances. Never count money "
                    "in a client's escrow account as unrestricted corporate cash. "
                    "UCC account control concerns collateral rights; it does not "
                    "itself authorize withdrawals or displace settlement instructions."
                ),
                (
                    "The aged_shelf_corp_tradeline_credit_stacking play must compare a "
                    "reinstated entity with genuine, disclosed business borrowing, "
                    "not treat entity age as operating history. Verify beneficial "
                    "ownership, tax filings, actual revenue, existing liens, and "
                    "the lender's permitted use of proceeds. A promotional $50,000 "
                    "facility with a 3% transfer charge costs $1,500 even at "
                    "zero stated APR. Repaying it over ten months requires "
                    "$5,000 of monthly principal reduction plus the charge and "
                    "any other contractual costs. If $20,000 remains when a "
                    "24% APR begins, one month costs approximately $400 of "
                    "interest before daily-balance effects. Cash advances may carry "
                    "immediate interest and a separate fee; a purchase promotion "
                    "does not establish a usable wire facility. Do not simulate "
                    "purchases, cycle merchant transactions, or overstate business "
                    "history to create escrow liquidity. Compare the fully loaded "
                    "cost with a transparent term facility: $50,000 held for "
                    "90 days at 18% simple annual interest costs approximately "
                    "$2,219 before origination charges. Include only the selected "
                    "funding route in the capital-cost ledger. If underwriting "
                    "disclosures are inaccurate or repayment depends on fresh "
                    "applications, halt applications, correct disclosures, and use "
                    "a transparent term facility or reduce financed spending. "
                    "Unused promotional limits are not committed settlement cash."
                ),
            ],
            "table": {
                "caption": "Base Liquidity Envelope, DSO Diagnostics, and Funding-Rail Controls",
                "headers": [
                    "Cash requirement or funding rail",
                    "Concrete calculation and operating assumption",
                    "Evidence required before relying on capacity",
                    "Fallback when timing or eligibility changes",
                ],
                "rows": [
                    [
                        "Transactional principal occupancy measures average cash tied in escrow",
                        "$100,000 times 100 events times three days divided by 365 equals $82,192",
                        "Match funding timestamps to cleared reusable principal return timestamps",
                        "Extend lock assumptions when weekends or recording delays recur",
                    ],
                    [
                        "EMD principal occupancy assumes only release-eligible funded participation events",
                        "$25,000 times 60 events times ten days divided by 365 equals $41,096",
                        "Document refundable terms, cash verification, and participation payment priority",
                        "Exclude early-stage deposits lacking the required unconditional end-buyer cash",
                    ],
                    [
                        "Peak principal capacity follows explicit simultaneous funding commitment limits",
                        "Two $100,000 closings plus three $25,000 deposits require $275,000",
                        "Maintain a dated commitment calendar and confirmed facility availability",
                        "Decline additional commitments before exhausting verified available funding capacity",
                    ],
                    [
                        "Operating runway bridges actual cash expenses during collection interruptions",
                        "$270,175 annual cash deductions times 21 divided by 365 equals $15,544",
                        "Reconcile payable dates against fee collection and bank settlement dates",
                        "Shorten discretionary spending commitments while preserving verification and servicing",
                    ],
                    [
                        "Designated loss cash protects already budgeted reversals and credit losses",
                        "$16,050 plus $21,400 establishes a separate $37,450 cash buffer",
                        "Keep reserve designations separate from new income statement expenses",
                        "Replenish depleted cash after updating realized loss and exposure estimates",
                    ],
                    [
                        "Fee DSO diagnoses collection lag without duplicating expense runway",
                        "$535,000 annual fees times five divided by 365 equals $7,329",
                        "Measure earned dates against actual fee deposits rather than invoices",
                        "Replace average DSO with deal-level receipts during settlement interruptions",
                    ],
                    [
                        "Promotional corporate credit requires truthful underwriting and permitted disbursement",
                        "$50,000 at a 3% transfer charge creates $1,500 immediate cost",
                        "Read promotion exclusions, cash advance terms, and contractual repayment dates",
                        "Halt applications, correct disclosures, then refinance transparently or reduce spending",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight conditions before committing the wire",
                "body": (
                    "A positive spreadsheet contribution does not authorize release. "
                    "Each transaction must satisfy these observable operating conditions."
                ),
                "items": [
                    "Independently verify unconditional end-buyer cash on deposit, authorized disbursement instructions, and release exclusively to the identified bonded title or settlement agent.",
                    "Confirm fee enforceability, applicable commercial-lending licensing or exemption, and usury treatment for the actual borrower, collateral, jurisdiction, and charge structure.",
                    "Demonstrate that the daily cash schedule survives the funded principal lock, contracted facility repayment date, and an additional four-day settlement delay.",
                    "Verify borrower and entity disclosures against source records, confirm permitted credit proceeds, and reject any repayment plan dependent on undisclosed new applications.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create the dated funding packet",
                    "action": "Join the signed agreement, settlement statement, and beneficiary verification to one transaction identifier.",
                    "detail": "Record earned fees separately from principal, partner entitlements, refundable deposits, and contingent charges.",
                },
                {
                    "step": 2,
                    "title": "Reserve daily funding capacity",
                    "action": "Enter principal release, expected reuse, fee collection, and facility repayment on the same daily cash schedule.",
                    "detail": "Deduct existing commitments and restricted balances before calculating available capacity; apply the four-day delay stress.",
                },
                {
                    "step": 3,
                    "title": "Verify the settlement cash independently",
                    "action": "Confirm unconditional buyer funds and authenticated wire instructions with the authorized settlement agent.",
                    "detail": "Use an independently sourced callback channel and retain the confirmation record; changed instructions restart verification.",
                },
                {
                    "step": 4,
                    "title": "Close the principal and fee ledgers",
                    "action": "Match returned principal, collected fees, capital charges, contractor invoices, and any reversals after settlement.",
                    "detail": "Release unused capacity only when cash is reusable; update cohort DSO, lock duration, CAC, and allowance experience.",
                },
            ],
        },
        {
            "heading": "4. Stress the margin and quarantine slow bankruptcy recoveries",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Stress costs against the fixed fee cohorts before allowing "
                    "growth assumptions to rescue the answer. Apply three simultaneous "
                    "changes: fee reversals rise by two percentage points of "
                    "gross fees, acquisition spending rises 20%, and capital "
                    "charges rise 25%. Conservative incurs $2,400, $3,600, and "
                    "$3,000 of additional deductions, reducing profit from $36,000 "
                    "to $27,000 and margin to 22.5%. Base incurs $10,700, "
                    "$11,000, and $18,750, reducing profit by $40,450 to "
                    "$186,925, or approximately 34.94%. Scaled incurs $19,000, "
                    "$15,000, and $23,750, reducing profit by $57,750 to "
                    "$464,750, or approximately 48.92%. These stressed outcomes "
                    "are overlays, not replacements for the canonical scenarios. "
                    "A separate uninsured $100,000 incremental principal loss beyond "
                    "existing allowances would reduce unstressed Base profit to "
                    "$127,375. It would exceed Conservative annual profit by "
                    "$64,000. That concentration matters more than a small "
                    "improvement in fee conversion. Separately, expanding Base transactional "
                    "locks from three to seven days increases average transactional "
                    "capital from $82,192 to $191,781, approximately $109,589 more. "
                    "This is an average funding increase, not a sufficient "
                    "peak facility limit. Recalculate simultaneous commitments and "
                    "repricing before accepting delayed transactions; the capital "
                    "charge stress does not automatically fund the extra principal."
                ),
                (
                    "The chapter11_trade_claim_convenience_class_rollup play belongs in "
                    "a separate duration bucket because bankruptcy distributions "
                    "do not replenish a 72-hour escrow facility. Consider a "
                    "documented $10,000 trade claim purchased for $2,500. Assume "
                    "an 80% probability of allowance and an applicable plan "
                    "distribution of 60% of allowed face value. Expected "
                    "receipts are $4,800, before timing adjustments. Subtract "
                    "$2,500 purchase price, $400 verification and servicing, "
                    "and $450 carrying cost, representing two years at "
                    "9% simple interest on the purchase price. Expected "
                    "contribution is $1,450 over two years, not annual "
                    "flash-funding income. The simplified allowance assumption treats "
                    "disallowance as zero recovery; replace it with supported "
                    "claim-specific outcomes when available. If the applicable "
                    "recovery becomes 30%, expected receipts fall to $2,400 "
                    "and contribution becomes negative $950. Obtain invoices, "
                    "delivery evidence, debtor payment history, transfer documentation, "
                    "and the operative plan rather than buying from Schedule "
                    "E/F alone. A scheduled liability does not establish "
                    "final allowance or a distribution entitlement. Under 11 "
                    "U.S.C. 502, objections can change the allowed amount. "
                    "Use PACER and the court-authorized claims agent to "
                    "reconcile claim numbers, amendments, objections, voting treatment, "
                    "and distribution status before committing acquisition cash."
                ),
                (
                    "Convenience-class treatment arises from the actual plan and "
                    "11 U.S.C. 1122(b), not from mechanically dividing a "
                    "large claim into smaller invoices. Read thresholds, election "
                    "deadlines, aggregation provisions, transferee treatment, and restrictions "
                    "on claim splitting before modeling any enhanced recovery. "
                    "Federal Rule of Bankruptcy Procedure 3001(e) distinguishes "
                    "transfer procedures; for a qualifying transfer after proof "
                    "of claim has been filed, file evidence of transfer "
                    "and account for the transferor's 21-day objection period "
                    "after the clerk's notice. Other transfer circumstances require "
                    "their own procedure. Do not equate completion of that "
                    "process with allowance or payment. If an objection "
                    "or plan provision defeats the thesis, stop affected "
                    "purchases, enforce documented seller recourse where available, "
                    "and price only supported general-unsecured recoveries. Seller "
                    "recourse is worth the seller's actual ability and "
                    "obligation to pay. Keep these claims outside the "
                    "three canonical fee cohorts; their inclusion would otherwise "
                    "fabricate current revenue and conceal long-duration capital "
                    "consumption. Monthly management review should reconcile published "
                    "scenario profit, current cash availability, and downside exposure "
                    "as separate outputs. Grow only after realized collection "
                    "timing and delivery capacity support the next commitment. "
                    "The durable edge is verified repayment plus disciplined "
                    "capital allocation, not a spectacular annualized yield on "
                    "money that cannot yet be reused."
                ),
            ],
            "table": {
                "caption": "Scenario Sensitivities and Bankruptcy-Claim Duration Boundaries",
                "headers": [
                    "Stress or adjacent operating play",
                    "Concrete unit math and result",
                    "Failure mechanism that changes the decision",
                    "Required fallback or operating response",
                ],
                "rows": [
                    [
                        "Conservative combined reversal, acquisition, and capital cost stress",
                        "$36,000 less $2,400, $3,600, and $3,000 leaves $27,000 profit",
                        "A small fee cohort cannot absorb repeated settlement cancellations",
                        "Reduce acquisition commitments and decline transactions with thin net contribution",
                    ],
                    [
                        "Base combined reversal, acquisition, and capital cost stress",
                        "$227,375 less $10,700, $11,000, and $18,750 leaves $186,925 profit",
                        "Higher financing charges and weaker referral quality compress cash earnings",
                        "Reprice new commitments and rebuild customer-level acquisition payback calculations",
                    ],
                    [
                        "Scaled combined reversal, acquisition, and capital cost stress",
                        "$522,500 less $19,000, $15,000, and $23,750 leaves $464,750 profit",
                        "Additional volume does not remove concentrated principal loss exposure",
                        "Cap simultaneous sponsor exposure and preserve independent settlement verification",
                    ],
                    [
                        "Base transactional principal locks expand from three to seven days",
                        "Average transactional capital rises approximately $109,589 to reach $191,781",
                        "Delayed recording or payout releases consume otherwise reusable funding capacity",
                        "Secure additional committed capacity or reduce concurrent funded transaction counts",
                    ],
                    [
                        "Incremental uninsured principal loss exceeds the established allowance",
                        "A further $100,000 loss reduces unstressed Base profit to $127,375",
                        "One failed repayment can overwhelm many successfully collected transaction fees",
                        "Stop related releases and pursue documented recovery rights immediately",
                    ],
                    [
                        "Chapter 11 documented trade claim with supported recovery assumptions",
                        "$4,800 expected receipts less $2,500, $400, and $450 yields $1,450",
                        "Allowance objections and long distribution timelines impair expected contribution",
                        "Fund from separately allocated patient capital rather than settlement liquidity",
                    ],
                    [
                        "Convenience-class thesis fails and supported recovery falls to 30%",
                        "$2,400 expected receipts less $3,350 total costs creates $950 loss",
                        "Plan aggregation provisions or objections eliminate the assumed recovery advantage",
                        "Stop purchases, enforce available seller recourse, and price general-unsecured recoveries",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A funding fee becomes an edge only when the principal returns on time and every deduction has already been counted.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Reconcile 70, 195, and 265 illustrative fee events to the exact $120,000, $535,000, and $950,000 canonical gross-fee totals, excluding escrow principal and partner entitlements.",
        "Build separate contra-revenue, paid delivery, CAC, capital-charge, credit-loss, and overhead accounts that reconcile to $36,000, $227,375, and $522,500 owner profit.",
        "Create a daily principal-release and fee-collection calendar; test the Base $327,994 liquidity envelope against actual overlap, restricted balances, and facility availability.",
        "Verify unconditional end-buyer cash, bonded settlement-agent identity, authenticated wire instructions, and applicable state fee and lending requirements before each release.",
        "Document promotional-credit charges, permitted uses, truthful entity history, reset dates, and principal repayment capacity; halt inaccurate applications and replace unsupported borrowing.",
        "Maintain bankruptcy claims in a separate duration portfolio with source claim evidence, Rule 3001(e) transfer tracking, plan-specific class analysis, and supported recovery pricing.",
    ],
    "statutory_citations": [
        {
            "title": "California Financial Code Section 22100 — Finance Lender and Broker Licensing",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22100.",
            "relevance": (
                "Requires licensing for covered finance-lender or broker activity; "
                "evaluate the actual transaction and applicable exemptions before "
                "pricing or funding California lending operations."
            ),
        },
        {
            "title": "California Financial Code Section 22050 — Specified Exemptions",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=FIN&sectionNum=22050.",
            "relevance": (
                "Provides specified exemptions whose factual conditions must be "
                "checked rather than inferred from commercial purpose or entity age."
            ),
        },
        {
            "title": "New York General Obligations Law Section 5-501 — Interest Rates",
            "url": "https://www.nysenate.gov/legislation/laws/GOB/5-501",
            "relevance": (
                "Provides a primary interest-rate framework; analyze applicable "
                "rates, charge characterization, borrower rules, and statutory "
                "exceptions before relying on short-duration funding fees."
            ),
        },
        {
            "title": "UCC Section 9-104 — Control of Deposit Account",
            "url": "https://www.law.cornell.edu/ucc/9/9-104",
            "relevance": (
                "Explains deposit-account control for secured transactions. Check "
                "the governing state's enacted text and distinguish collateral "
                "control from contractual authority to disburse escrow funds."
            ),
        },
        {
            "title": "11 U.S.C. Section 502 — Allowance of Claims or Interests",
            "url": "https://www.law.cornell.edu/uscode/text/11/502",
            "relevance": (
                "Supports claim-allowance and objection analysis before assigning "
                "recovery probabilities or recording expected bankruptcy distributions."
            ),
        },
        {
            "title": "11 U.S.C. Section 1122(b) — Administrative Convenience Class",
            "url": "https://www.law.cornell.edu/uscode/text/11/1122",
            "relevance": (
                "Permits a separate class of qualifying small unsecured claims "
                "subject to court-approved parameters; the operative plan determines "
                "whether purchased claims receive the assumed treatment."
            ),
        },
        {
            "title": "Federal Rule of Bankruptcy Procedure 3001(e) — Transferred Claims",
            "url": "https://www.law.cornell.edu/rules/frbp/rule_3001",
            "relevance": (
                "Establishes procedures for transferred claims, including evidence "
                "of certain transfers after filing and the transferor's 21-day "
                "objection period following the clerk's notice."
            ),
        },
    ],
}
