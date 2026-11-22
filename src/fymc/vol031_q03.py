from __future__ import annotations

CHAPTER_3 = {
    "id": "Q3",
    "chapter_id": "Q3",
    "chapter_number": 3,
    "question_number": 3,
    "slug": "unit-economics-margin-waterfall-working-capital-float",
    "question_prompt": "What are the real unit economics, gross-to-net margin deductions, scrub/reversal reserves, and working-capital float requirements for uber & commercial fleet arbitrage?",
    "kicker": "Q3 / THE BIG MONEY PLAYBOOKS",
    "title": "Unit Economics, Margin Waterfall & Working-Capital Float",
    "subtitle": "Driver Lease Cohorts, Investor Splits, ASC 606 Agency Presentation, California PUC Coverage Requirements & Payout-Lock Liquidity",
    "layout_template": "financial_breakdown",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #31, Uber & Commercial Fleet Arbitrage, ranks #15 of 36 with an "
        "89/100 Money-to-Manpower Score. This chapter translates 10 mapped plays "
        "into collectible vehicle-week economics, investor waterfalls, reversal "
        "allowances, and funded settlement gaps. Formula v2.0 fixes annual gross "
        "billings at $180,000, $690,000, and $1,200,000; the 55% retained share "
        "produces $99,000, $379,500, and $660,000 before retained operating costs. "
        "Annual owner net profits reconcile exactly to $25,200, $144,900, and "
        "$336,000. The illustrative allocation below exposes contractor labor, "
        "placement CAC, commercial coverage, downtime, and settlement losses "
        "without relabeling passenger fares as operator revenue. A fourteen-day "
        "collection cycle requires approximately $21,121, $58,759, and $90,329 "
        "of operating liquidity under stated assumptions, before setup spending."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$180,000",
            "context": "Annual gross operator billings; $99,000 retained at 55%",
            "note": (
                "14% gross-basis net margin; $25,200 annual owner net profit; "
                "25.45% retained net margin; 1 FT + 3 C"
            ),
        },
        {
            "label": "Base",
            "value": "$690,000",
            "context": "Annual gross operator billings; $379,500 retained at 55%",
            "note": (
                "21.0% gross-basis net margin; $144,900 annual owner net profit; "
                "38.18% retained net margin; 1 FT + 3 C"
            ),
        },
        {
            "label": "Scaled",
            "value": "$1,200,000",
            "context": "Annual gross operator billings; $660,000 retained at 55%",
            "note": (
                "28% gross-basis net margin; $336,000 annual owner net profit; "
                "50.91% retained net margin; 2 FT + 4 C"
            ),
        },
    ],
    "sections": [
        {
            "heading": "1. Normalize ten operating plays into collectible vehicle cohorts",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Start with the billing object, not the vehicle purchase price or a screenshot "
                    "of passenger receipts. For this chapter, gross billings mean operator-billed "
                    "driver leases, commercial dispatch charges, and qualifying co-host arrangements "
                    "before owner allocations. Underlying passenger fares, merchant delivery value, "
                    "refundable deposits, and investor vehicle purchase money are separate ledgers. "
                    "Build three illustrative cohorts with ten, thirty, and forty active vehicle "
                    "equivalents; an equivalent represents twelve collected vehicle-months rather "
                    "than a promise that every registered vehicle stays productive. Annual billings "
                    "per equivalent are $18,000, $23,000, and $30,000, producing exactly $180,000, "
                    "$690,000, and $1,200,000. The Base monthly equivalent is $1,916.6667, so retain "
                    "precision internally and round only the completed invoice. Tag every charge "
                    "with vehicle identification number, driver agreement, service interval, "
                    "investor contract, and collection status. Stripe or ACH processor exports "
                    "should reconcile to the operating bank account and QuickBooks Online "
                    "subledger, while Uber fleet statements support only the settlements actually "
                    "available under that account's terms. A bill is earned through the relevant "
                    "service obligation; an unpaid invoice is not distributable cash. Compare "
                    "collected vehicle-weeks with available vehicle-weeks before interpreting "
                    "higher fleet counts as economic growth."
                ),
                (
                    "Use ten mapped play labels for the operating analysis: weekly hybrid driver "
                    "leasing, weekly SUV driver leasing, Black SUV shift dispatch, licensed airport "
                    "transfer dispatch, cargo-van commercial placements, approved replacement-vehicle "
                    "placements, investor SUV co-hosting, investor hybrid co-hosting, investor "
                    "cargo-van co-hosting, and GPS-supported consignment management. These are "
                    "analytical billing lanes, not ten additional canonical identifiers. The supplied "
                    "play zero_metal_vehicle_cohost_consignment spans the final four lanes and "
                    "requires a contractually defined 25%–35% gross management split. On $2,000 "
                    "of eligible monthly collections, management receives $500, $600, or $700 "
                    "at those respective rates before its own delivery costs. At 30%, subtracting "
                    "$90 contractor service, $40 acquisition amortization, $25 telematics, and "
                    "$45 expected reversals leaves $400 monthly contribution before central "
                    "overhead and any additional operator-borne insurance. State who absorbs "
                    "maintenance before quoting that amount. Do not apply the portfolio's 55% "
                    "retained share mechanically to this single contract. Investor ownership "
                    "removes vehicle acquisition from the operator balance sheet, but it does "
                    "not remove collection exposure, contractual indemnities, deductibles, or "
                    "placement labor. If commercial coverage fails, pause the placement and "
                    "stop accruing unsupported availability charges rather than preserve a "
                    "fictional utilization metric."
                ),
                (
                    "Make the ten lanes comparable using contribution per collected vehicle-week, "
                    "not their advertised daily prices. A hybrid leased for $350 across fifty "
                    "collected weeks bills $17,500; an SUV at $500 across forty-six weeks bills "
                    "$23,000. A Black SUV dispatch lane billing an operator fee of $125 across "
                    "240 completed shifts contributes $30,000 of gross operator billings, not "
                    "the passengers' entire fares. Airport dispatch at $40 across 300 completed "
                    "transfers bills $12,000; a cargo van at $600 across forty weeks bills "
                    "$24,000. Replacement placements at $80 across 150 authorized days bill "
                    "$12,000. Investor SUV, hybrid, and van lanes collecting $2,000, $1,500, "
                    "and $2,500 monthly yield $600, $450, and $750 management fees at 30%; "
                    "a consignment device charge of $25 less $15 connectivity yields $10 "
                    "before installation recovery. These lane examples explain mechanics and "
                    "are not additive forecasts. Suspend airport dispatch without required "
                    "access, reject replacement use outside coverage, and reprice cargo "
                    "placements when mileage overwhelms maintenance allowances. For every lane, "
                    "fall back to fewer funded service intervals rather than unsecured credit "
                    "to drivers. Record cancellations and collection failures against the "
                    "originating cohort so replacement bookings cannot conceal deteriorating "
                    "unit performance."
                ),
            ],
            "table": {
                "caption": "Cohort Denominators, Contract Economics & Revenue Recognition Boundaries",
                "headers": [
                    "Operating measurement and its defined boundary",
                    "Concrete unit calculation for the operator",
                    "Evidence required before booking the amount",
                    "Failure response preserving the economic denominator",
                ],
                "rows": [
                    [
                        "Conservative cohort measured in collected vehicle equivalents",
                        "Ten equivalents times $18,000 produces $180,000 annually",
                        "Match collected service intervals against signed driver agreements",
                        "Remove unpaid idle intervals from productive capacity reporting",
                    ],
                    [
                        "Base cohort measured without rounding monthly invoice assumptions",
                        "Thirty equivalents times $23,000 produces $690,000 annually",
                        "Preserve annual precision when allocating monthly cohort budgets",
                        "Reconcile rounding differences separately from operating price concessions",
                    ],
                    [
                        "Scaled cohort measured independently from registered fleet count",
                        "Forty equivalents times $30,000 produces $1,200,000 annually",
                        "Require completed dispatch or lease performance for charges",
                        "Reduce forecast capacity when unavailable vehicles accumulate downtime",
                    ],
                    [
                        "Investor consignment contract using the supplied mapped play",
                        "$2,000 collected times 30% produces $600 management fees",
                        "Document eligible collections and investor distribution rights explicitly",
                        "Pause placements when coverage or collection authority fails",
                    ],
                    [
                        "Mixed portfolio retention assumption under Formula v2.0",
                        "Each $100 billed retains $55 before operator expenses",
                        "Support the aggregate with contract-level principal-agent accounting analysis",
                        "Separate unmatched contracts instead of forcing false retention",
                    ],
                    [
                        "Passenger fare and vehicle purchase accounting boundaries",
                        "Exclude fare volume and investor capital from operator revenue",
                        "Reconcile bank receipts to their actual contractual beneficiaries",
                        "Move misclassified receipts into payable or capital ledgers",
                    ],
                    [
                        "Active equivalent denominator for investor reporting and collections",
                        "Twelve collected vehicle-months constitute one annual active equivalent",
                        "Retain vehicle-week availability and settlement evidence together consistently",
                        "Explain fleet growth separately from collected productive capacity",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect collection quality before adding another investor vehicle",
                "body": (
                    "The strongest fleet dashboard connects contracts, service intervals, "
                    "cash settlements, and exception ownership rather than merely showing GPS dots."
                ),
                "items": [
                    "Keep separate gross-service, investor-payable, and operator-fee columns; a 30% co-host contract must not inherit the portfolio's 55% retention assumption.",
                    "Quote investor returns after a mileage-specific maintenance schedule and funded deductible allocation, not after an arbitrary percentage haircut.",
                    "Export Uber settlement adjustments before each investor distribution and attach the affected vehicle-week to every correction.",
                    "Measure installer, cleaner, and recovery contractor cost per completed placement; inexpensive hourly quotes often conceal repeat visits and unpaid downtime.",
                ],
            },
        },
        {
            "heading": "2. Reconcile every deduction from gross billings to owner profit",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The scorecard fixes the endpoints; the expense allocation below is an "
                    "illustrative operating budget that reconciles them, not a claim about "
                    "observed fleet invoices. Deduct 45% of gross billings for investor allocations "
                    "and pass-through fleet costs: $81,000 Conservative, $310,500 Base, and "
                    "$540,000 Scaled. Retained revenue is therefore $99,000, $379,500, and "
                    "$660,000. Under ASC 606, actual principal-versus-agent presentation depends "
                    "on control of each promised service; a contractual split alone does not "
                    "establish agency. Preserve the supplied 55% scorecard convention for "
                    "comparison, then document the accountant's contract-level presentation "
                    "separately. Never deduct the same insurance invoice once in pass-through "
                    "costs and again in retained operating expenses. The waterfall assigns "
                    "only additional operator-borne coverage to its insurance line. Likewise, "
                    "investor-borne depreciation belongs in the investor's asset economics; "
                    "operator-owned metal would require a new depreciation and capital budget. "
                    "Residual annual operating deductions of $73,800, $234,600, and $324,000 "
                    "leave the required owner profits. Dividing those profits by gross billings "
                    "gives 14%, 21.0%, and 28%; dividing by retained revenue gives 25.45%, "
                    "38.18%, and 50.91%. Always print the denominator beside a margin."
                ),
                (
                    "Budget delivery labor at $30,000, $96,000, and $144,000 annually, covering "
                    "contractor handoffs, cleaning coordination, inspections, collections support, "
                    "and the Scaled additional employee. The single full-time owner in the "
                    "smaller cases receives residual owner profit rather than an additional "
                    "salary deduction in this illustration. At Scaled, the second full-time "
                    "person's loaded compensation must fit inside the stated labor budget; "
                    "the four contractor relationships are not four full-time equivalents. "
                    "Do not imply passive earnings by omitting the owner's working hours. "
                    "Acquisition budgets of $6,000, $24,000, and $36,000 assume 120, 300, "
                    "and 400 successfully started placements at $50, $80, and $90 CAC. "
                    "These counts include replacements and renewals requiring fresh acquisition "
                    "work, not unique vehicles. Track advertising, referral payments, screening, "
                    "and onboarding against the same denominator; Checkr or another screening "
                    "vendor's invoice is not the entire CAC. Record a cancellation before "
                    "handoff as acquisition loss, not a productive placement. At Base, "
                    "$80 CAC against $100 weekly contribution before acquisition and central "
                    "overhead implies 0.8 collected weeks of simple payback. That test becomes "
                    "misleading if the $100 contribution omits downtime, reversals, or "
                    "commercial-use coverage."
                ),
                (
                    "Reserve 2% of gross billings for expected scrubs and reversals: $3,600, "
                    "$13,800, and $24,000. For this illustration, allocate 1.0 percentage "
                    "point to uncollectible driver balances, 0.6 to service credits and "
                    "disputed availability, and 0.4 to payment disputes and settlement "
                    "corrections. Actual bookkeeping should distinguish revenue adjustments "
                    "from credit losses and processor fees rather than treat this management "
                    "allowance as one universal accounting entry. Maintain an opening reserve, "
                    "new provision, identified utilization, recoveries, and closing reserve "
                    "rollforward. Charge realized losses against the appropriate allowance "
                    "instead of expensing the provision and the same write-off twice. "
                    "Maintenance and downtime budgets are $9,000, $24,000, and $18,000; "
                    "the Scaled decline requires a documented shift toward investor-borne "
                    "repairs and lower operator exposure, not miraculous reliability. Full "
                    "retained deductions average $6,150, $19,550, and $27,000 monthly. "
                    "Consequently, the supplied $2,500–$15,000 monthly opex range cannot "
                    "represent every deduction in these reconciled cases; treat its scope "
                    "as requiring clarification, not permission to erase costs. Owner profit "
                    "here is the scorecard operating residual before owner-level taxes "
                    "and distributions, with no added vehicle debt service assumed."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Annual Waterfall: Exact Endpoints With Explicit Illustrative Expense Allocations",
                "headers": [
                    "Waterfall component and accounting treatment",
                    "Conservative annual allocation with operating explanation",
                    "Base annual allocation with operating explanation",
                    "Scaled annual allocation with operating explanation",
                ],
                "rows": [
                    [
                        "Gross operator billings before contractual owner allocations",
                        "$180,000 from ten collected annual vehicle equivalents",
                        "$690,000 from thirty collected annual vehicle equivalents",
                        "$1,200,000 from forty collected annual vehicle equivalents",
                    ],
                    [
                        "Subtract investor distributions and pass-through fleet costs",
                        "$81,000 equals 45% of annual gross billings",
                        "$310,500 equals 45% of annual gross billings",
                        "$540,000 equals 45% of annual gross billings",
                    ],
                    [
                        "Retained revenue available before operator expense deductions",
                        "$99,000 equals 55% of annual gross billings",
                        "$379,500 equals 55% of annual gross billings",
                        "$660,000 equals 55% of annual gross billings",
                    ],
                    [
                        "Subtract delivery labor with owner compensation boundary",
                        "$30,000 funds contractors while owner receives residual profit",
                        "$96,000 funds contractors while owner receives residual profit",
                        "$144,000 funds contractors and additional employee loaded compensation",
                    ],
                    [
                        "Subtract placement acquisition spending using successful starts",
                        "$6,000 funds 120 successful placements at $50 each",
                        "$24,000 funds 300 successful placements at $80 each",
                        "$36,000 funds 400 successful placements at $90 each",
                    ],
                    [
                        "Subtract additional operator-borne commercial coverage expense only",
                        "$12,000 excludes policies already charged through investor allocations",
                        "$42,000 excludes policies already charged through investor allocations",
                        "$48,000 excludes policies already charged through investor allocations",
                    ],
                    [
                        "Subtract telematics subscriptions administration and accounting support",
                        "$9,600 funds devices software bookkeeping and administrative services",
                        "$24,000 funds devices software bookkeeping and administrative services",
                        "$36,000 funds devices software bookkeeping and administrative services",
                    ],
                    [
                        "Subtract expected billing scrubs reversals and collection losses",
                        "$3,600 represents 2% of annual gross operator billings",
                        "$13,800 represents 2% of annual gross operator billings",
                        "$24,000 represents 2% of annual gross operator billings",
                    ],
                    [
                        "Subtract operator-borne maintenance downtime and service remediation",
                        "$9,000 covers retained repair exposure and downtime remediation",
                        "$24,000 covers retained repair exposure and downtime remediation",
                        "$18,000 requires contractual transfer of additional repair exposure",
                    ],
                    [
                        "Subtract payment processing banking and treasury service expenses",
                        "$3,600 covers settlement costs without assumed vehicle borrowing",
                        "$10,800 covers settlement costs without assumed vehicle borrowing",
                        "$18,000 covers settlement costs without assumed vehicle borrowing",
                    ],
                    [
                        "Owner net profit after every listed retained deduction",
                        "$25,200 remains after $73,800 total retained operating deductions",
                        "$144,900 remains after $234,600 total retained operating deductions",
                        "$336,000 remains after $324,000 total retained operating deductions",
                    ],
                ],
            },
        },
        {
            "heading": "3. Fund settlement gaps without spending investor or driver money",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Model cash timing independently from margin. The liquidity example assumes "
                    "the operator collects the full billed amount, pays the 45% investor "
                    "and pass-through allocation seven days after service, and realizes cash "
                    "collections fourteen days after service. Those are planning assumptions, "
                    "not representations of a universal Uber payout schedule. If investors "
                    "receive their allocation directly and the operator collects only its "
                    "fee, rebuild receivables and payables on that narrower cash perimeter. "
                    "Use gross billings divided by 365 to establish daily throughput, "
                    "then multiply by days sales outstanding, or DSO. Fourteen-day receivables "
                    "are $6,904, $26,466, and $46,027. Seven-day contractual payables offset "
                    "only $1,553, $5,955, and $10,356. This offset is legitimate only "
                    "when the agreement actually permits that payment timing; an already "
                    "overdue investor distribution is not free working capital. Track service "
                    "date, invoice date, processor settlement date, bank availability, and "
                    "investor due date separately. A payout displayed as pending cannot "
                    "fund a premium debit tonight. Reconcile daily using bank-available "
                    "balances, not the larger processor dashboard balance, and age disputed "
                    "amounts separately from routine receivables to expose true collection "
                    "delays before the next distribution run."
                ),
                (
                    "Add thirty days of operating cash buffer, excluding only the modeled "
                    "scrub provision because the fourteen-day receivable model assumes "
                    "ordinary collection timing and the provision is not an immediate "
                    "cash payment. Annual non-provision costs are $70,200, $220,800, and "
                    "$300,000; thirty days equals $5,770, $18,148, and $24,658. This "
                    "buffer deliberately treats other budgeted costs as cash exposure, "
                    "even when individual repair invoices arrive unevenly. Add immediately "
                    "accessible deductible liquidity of $10,000, $20,000, and $30,000, "
                    "representing illustrative $5,000 claims capacity across two, four, "
                    "and six concurrent events. These amounts are balance-sheet funding "
                    "requirements, not additional annual expense deductions. The resulting "
                    "operating liquidity requirement is approximately $21,121, $58,759, "
                    "and $90,329: receivables less permitted payables plus operating "
                    "buffer plus deductible liquidity. Restricted security deposits, "
                    "investor distributions awaiting remittance, and tax collections cannot "
                    "fill the gap. Do not subtract expected loss reserves from receivables "
                    "to manufacture cash availability; persistently unpaid balances require "
                    "a separate bad-debt and collection forecast. Recalculate the buffer "
                    "weekly from the next thirteen weeks of actual premium, payroll, "
                    "repair, and investor payment dates rather than treating the "
                    "thirty-day approximation as a permanent treasury policy."
                ),
                (
                    "Stress payout access by extending DSO from fourteen to forty-five "
                    "days while holding the seven-day payable contract unchanged. The "
                    "additional thirty-one days consume $15,288, $58,603, and $101,918 "
                    "of cash, lifting total operating liquidity to approximately $36,408, "
                    "$117,362, and $192,247. This is a collection-delay sensitivity, not "
                    "a simultaneous revenue loss; apply a separate loss assumption if "
                    "the held amounts are ultimately unrecoverable. Add processor rolling "
                    "reserves only when they are outside these modeled receivables, "
                    "otherwise the same unavailable dollars get counted twice. The "
                    "published $12,000–$65,000 startup range therefore supports only "
                    "selected launch configurations, not automatic funding of the "
                    "Scaled case. Setup deposits, installer charges, licensing, and "
                    "coverage down payments sit above the operating liquidity estimate "
                    "unless already included in its expense schedule. Negotiate "
                    "collection-linked investor distributions where commercially acceptable, "
                    "stage new placements, or secure a committed facility before "
                    "assuming rapid expansion. A proposed credit line contributes "
                    "nothing until its documents, borrowing conditions, and draw "
                    "availability are verified. Stop owner distributions when "
                    "unrestricted cash falls below the next premium, payroll, "
                    "and contractually due investor remittances plus funded claims "
                    "capacity; profitable cohorts can still fail through settlement "
                    "timing alone."
                ),
            ],
            "table": {
                "caption": "Working-Capital Bridge Using Calendar-Day Cash Timing and Unrestricted Funds",
                "headers": [
                    "Cash bridge component and explicit timing assumption",
                    "Conservative funding amount and calculation basis",
                    "Base funding amount and calculation basis",
                    "Scaled funding amount and calculation basis",
                ],
                "rows": [
                    [
                        "Fourteen-day receivables before any separate collection loss",
                        "$6,904 equals $180,000 multiplied by fourteen over 365",
                        "$26,466 equals $690,000 multiplied by fourteen over 365",
                        "$46,027 equals $1,200,000 multiplied by fourteen over 365",
                    ],
                    [
                        "Subtract seven-day permitted investor and pass-through payables",
                        "$1,553 equals $81,000 multiplied by seven over 365",
                        "$5,955 equals $310,500 multiplied by seven over 365",
                        "$10,356 equals $540,000 multiplied by seven over 365",
                    ],
                    [
                        "Add thirty-day buffer for non-provision operating cash costs",
                        "$5,770 supports thirty days of $70,200 annual costs",
                        "$18,148 supports thirty days of $220,800 annual costs",
                        "$24,658 supports thirty days of $300,000 annual costs",
                    ],
                    [
                        "Add immediately accessible deductible liquidity without expensing twice",
                        "$10,000 supports two illustrative simultaneous $5,000 deductible events",
                        "$20,000 supports four illustrative simultaneous $5,000 deductible events",
                        "$30,000 supports six illustrative simultaneous $5,000 deductible events",
                    ],
                    [
                        "Total operating liquidity using unrounded underlying bridge calculations",
                        "$21,121 funds modeled gaps before incremental launch spending",
                        "$58,759 funds modeled gaps before incremental launch spending",
                        "$90,329 funds modeled gaps before incremental launch spending",
                    ],
                    [
                        "Additional cash required when collection extends thirty-one days",
                        "$15,288 funds movement from fourteen to forty-five DSO",
                        "$58,603 funds movement from fourteen to forty-five DSO",
                        "$101,918 funds movement from fourteen to forty-five DSO",
                    ],
                    [
                        "Total stressed liquidity with forty-five-day collection timing",
                        "$36,408 funds delayed collections without assuming changed profitability",
                        "$117,362 funds delayed collections without assuming changed profitability",
                        "$192,247 funds delayed collections without assuming changed profitability",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Close the vehicle-week billing ledger",
                    "action": "Match service evidence, contractual rates, and collection ownership before issuing each invoice.",
                    "detail": (
                        "Assign vehicle, driver, investor, service interval, and billing-lane identifiers; "
                        "separate refundable deposits from earned charges and preserve source statements."
                    ),
                },
                {
                    "step": 2,
                    "title": "Post the retained contribution bridge",
                    "action": "Calculate investor allocations first, then deduct only operator-borne costs and expected losses.",
                    "detail": (
                        "Reconcile the aggregate to 55% retained revenue for the scorecard comparison "
                        "without forcing individual 25%–35% co-host contracts into that percentage."
                    ),
                },
                {
                    "step": 3,
                    "title": "Refresh thirteen-week bank-available cash",
                    "action": "Schedule collections, coverage debits, contractor payments, claims cash, and investor due dates.",
                    "detail": (
                        "Run fourteen-day and forty-five-day collection cases; exclude restricted "
                        "deposits and avoid counting processor holds twice."
                    ),
                },
                {
                    "step": 4,
                    "title": "Release only funded distributions",
                    "action": "Pay contractually due beneficiaries and retain the documented unrestricted operating floor.",
                    "detail": (
                        "Suspend discretionary owner draws and unfunded placements when the forecast "
                        "cannot cover premiums, payroll, investor remittances, and funded claims capacity."
                    ),
                },
            ],
        },
        {
            "heading": "4. Stress retained contribution and verify the operating fallback",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run sensitivities against the reconciled waterfall rather than applying "
                    "a vague haircut to owner profit. With investor allocations fixed "
                    "at 45% of billings and the scrub provision varying at 2%, "
                    "each lost dollar of gross billings removes $0.53 of contribution "
                    "when every other cost stays fixed. A 10% billing decline "
                    "therefore reduces annual profit by $9,540, $36,570, and $63,600, "
                    "leaving $15,660, $108,330, and $272,400. This assumes the retained "
                    "share survives the mix change; a shift toward lower-fee consignment "
                    "requires a separate weighted-retention model. Increasing only "
                    "operator-borne insurance by 25% removes another $3,000, $10,500, "
                    "and $12,000. The combined billing and insurance stress leaves "
                    "$12,660, $97,830, and $260,400. If investor contracts promise "
                    "minimum payments, the 45% allocation is no longer fully variable "
                    "and this stress understates losses. Obtain actual renewal quotations "
                    "before adding vehicles; use the insurer's stated vehicle, driver, "
                    "territory, and commercial-use classifications. Do not replace "
                    "an expensive commercial policy with a personal policy that "
                    "excludes the activity. A temporarily parked vehicle still needs "
                    "coverage appropriate to its storage, custody, and contractual "
                    "obligations while the placement is paused."
                ),
                (
                    "Test three additional failure channels separately: acquisition inflation, "
                    "claims leakage, and reserve deterioration. Doubling CAC at unchanged "
                    "placement counts costs another $6,000, $24,000, and $36,000, "
                    "leaving profits of $19,200, $120,900, and $300,000 before "
                    "other stresses. One incremental unrecovered $10,000 claim costs "
                    "$10,000 in every scenario; if a previously funded allowance "
                    "already recognizes that exact loss, consuming its cash does "
                    "not create a second expense. Raising scrub losses from 2% "
                    "to 4% removes $3,600, $13,800, and $24,000 of additional "
                    "profit. At Base, forty productive vehicle-weeks lost at the "
                    "annualized rate of $23,000 divided by 52 means approximately "
                    "$17,692 less billing and $9,377 less contribution under "
                    "the same variable-cost assumptions. That calculation is an "
                    "alternative downtime stress, not something to stack on a "
                    "billing decline already covering those weeks. With non-provision "
                    "costs fixed, break-even gross billings equal those costs "
                    "divided by 0.53: approximately $132,453, $416,604, and "
                    "$566,038. These are operating break-even points, not cash "
                    "funding targets. Add incremental hiring, coverage tiers, or "
                    "minimum investor guarantees whenever the tested volume crosses "
                    "a real contractual cost step."
                ),
                (
                    "The zero_metal_vehicle_cohost_consignment fallback must function before "
                    "a delinquency occurs. Use professionally installed GPS and OBD-II "
                    "equipment, documented driver notice, controlled access, and "
                    "stationary-only starter controls where lawful. A telematics "
                    "signal alone does not establish safe immobilization: require "
                    "verified stationary status, an unoccupied safe location, "
                    "and a process that prevents interruption of a running "
                    "vehicle or emergency use. Disable remote immobilization "
                    "when these conditions cannot be established; pause "
                    "affected placements and arrange insurer-approved service "
                    "or lawful professional recovery after safety review. "
                    "California Public Utilities Code section 5433 addresses "
                    "transportation-network insurance periods; section 5371 "
                    "addresses charter-party carrier authority. Neither "
                    "substitutes for applicable local airport permissions "
                    "or New York City TLC licensing. Confirm actual "
                    "Period 1, 2, and 3 coverage where relevant, "
                    "plus separate rental and off-platform use. Apply "
                    "state rental disclosures and documented toll pass-through "
                    "terms to the actual contract category. When obtaining "
                    "consumer-report MVR products, establish a permissible "
                    "purpose under 15 U.S.C. 1681b and follow the "
                    "applicable notice process. Preserve installation records "
                    "and avoid rendering federally required safety equipment "
                    "inoperative under 49 U.S.C. 30122. Price these "
                    "requirements into delivery costs before promising "
                    "an investor distribution."
                ),
            ],
            "table": {
                "caption": "Standalone Sensitivities and One Explicit Combined Stress Against Canonical Owner Profit",
                "headers": [
                    "Stress definition with its retained-cost assumption",
                    "Conservative annual owner profit after stated stress",
                    "Base annual owner profit after stated stress",
                    "Scaled annual owner profit after stated stress",
                ],
                "rows": [
                    [
                        "Ten percent billing decline with 53% incremental contribution",
                        "$15,660 remains after $9,540 of lost annual contribution",
                        "$108,330 remains after $36,570 of lost annual contribution",
                        "$272,400 remains after $63,600 of lost annual contribution",
                    ],
                    [
                        "Twenty-five percent increase in operator-borne insurance expense",
                        "$22,200 remains after $3,000 additional annual coverage expense",
                        "$134,400 remains after $10,500 additional annual coverage expense",
                        "$324,000 remains after $12,000 additional annual coverage expense",
                    ],
                    [
                        "Combined billing decline and operator insurance increase",
                        "$12,660 remains after both explicitly defined operating stresses",
                        "$97,830 remains after both explicitly defined operating stresses",
                        "$260,400 remains after both explicitly defined operating stresses",
                    ],
                    [
                        "Double acquisition cost while successful placement counts remain",
                        "$19,200 remains after $6,000 additional annual acquisition spending",
                        "$120,900 remains after $24,000 additional annual acquisition spending",
                        "$300,000 remains after $36,000 additional annual acquisition spending",
                    ],
                    [
                        "One additional unrecovered claim outside existing expense allowances",
                        "$15,200 remains after recognizing one incremental $10,000 loss",
                        "$134,900 remains after recognizing one incremental $10,000 loss",
                        "$326,000 remains after recognizing one incremental $10,000 loss",
                    ],
                    [
                        "Double scrub provision from two to four percent",
                        "$21,600 remains after $3,600 additional expected annual losses",
                        "$131,100 remains after $13,800 additional expected annual losses",
                        "$312,000 remains after $24,000 additional expected annual losses",
                    ],
                    [
                        "Break-even gross billings assuming unchanged non-provision expense budgets",
                        "$132,453 covers $70,200 fixed costs at 53% contribution",
                        "$416,604 covers $220,800 fixed costs at 53% contribution",
                        "$566,038 covers $300,000 fixed costs at 53% contribution",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify economics, cash, coverage, and safe recovery before placement",
                "body": (
                    "A vehicle becomes deployable only when the contract, cash forecast, "
                    "coverage evidence, and operational fallback agree on the same use."
                ),
                "items": [
                    "Verify the signed 25%–35% co-host split, eligible collection definition, repair responsibility, deductible allocation, and investor payment dates against the vehicle-level waterfall.",
                    "Verify unrestricted funds cover the applicable settlement-gap model; document forty-five-day payout-lock capacity before committing distributions that depend on earlier collections.",
                    "Verify coverage for actual commercial operations, applicable rideshare periods, rental exposure, off-platform dispatch, and required carrier or airport permissions before service begins.",
                    "Verify professional installation, explicit notice, lawful stationary-only starter controls, and the disable-and-recover fallback; never authorize immobilization from an uncertain location signal.",
                ],
            },
        },
    ],
    "pull_quote": "A fleet earns its margin on collected vehicle-weeks and survives on cash that nobody else already owns.",
    "diagram_id": "diag-03",
    "action_checklist": [
        "Build a vehicle-week ledger separating gross service billings, investor payables, operator fees, restricted deposits, and underlying passenger fares.",
        "Reconcile annual gross billings of $180,000, $690,000, and $1,200,000 through 55% retained revenue to owner profits of $25,200, $144,900, and $336,000.",
        "Measure successful-placement CAC and contractor delivery cost by billing lane, including replacement activity and failed onboarding spending.",
        "Maintain a scrub and reversal rollforward that distinguishes provisions, realized losses, recoveries, revenue credits, and processor adjustments without duplicate expense.",
        "Fund a thirteen-week cash forecast using fourteen-day and forty-five-day collection cases, actual investor due dates, premium debits, and dedicated deductible liquidity.",
        "Verify commercial-use coverage, relevant permits, investor repair obligations, and the stationary-only telematics fallback before accepting the next vehicle placement.",
    ],
    "statutory_citations": [
        {
            "title": "California Public Utilities Code § 5433 — Transportation network company insurance",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=5433.&lawCode=PUC",
            "relevance": (
                "Establishes California transportation-network insurance requirements tied "
                "to operating periods; map actual use and policy evidence before dispatch."
            ),
        },
        {
            "title": "California Public Utilities Code § 5371 — Charter-party carrier authority",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=5371.&lawCode=PUC",
            "relevance": (
                "Requires applicable authority for charter-party carrier operations; "
                "validate service classification separately from rideshare participation."
            ),
        },
        {
            "title": "15 U.S.C. § 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": (
                "Controls permissible access to consumer reports, including qualifying "
                "MVR screening products; employment-purpose reports carry additional conditions."
            ),
        },
        {
            "title": "15 U.S.C. § 1681m — Duties of users taking adverse action",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681m",
            "relevance": (
                "Provides adverse-action notice duties when covered decisions rely on "
                "consumer reports; connect screening decisions to the applicable workflow."
            ),
        },
        {
            "title": "49 U.S.C. § 30122 — Making safety devices and elements inoperative",
            "url": "https://www.law.cornell.edu/uscode/text/49/30122",
            "relevance": (
                "Restricts specified commercial actors from knowingly rendering required "
                "vehicle safety systems inoperative; relevant to installer selection and modifications."
            ),
        },
    ],
}
