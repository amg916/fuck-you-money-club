from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-and-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in subject-to & wraparound note arbitrage, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Due-on-Sale Acceleration, RMLO File Defects, Servicer Reconciliation, Texas Wrap Disclosures, and Trigger-Mail Loss Controls",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #35, Subject-To & Wraparound Note Arbitrage, holds Rank #09 of 36 "
        "with a 90/100 Money-to-Manpower Score. Its 11 mapped plays require a common "
        "discipline: protect the underlying loan before distributing the wrap spread. "
        "The canonical annual owner profits are $28,000 Conservative, $190,000 Base, "
        "and $442,000 Scaled; none includes home value or pass-through mortgage payments "
        "as operator revenue. This chapter dismantles acceleration exposure, defective "
        "origination, escrow leakage, premature down-payment recognition, servicing "
        "blind spots, and deceptive acquisition tactics. It also unpacks "
        "public_filing_trigger_mail_arbitrage through explicit acquisition math and "
        "private-brand alternatives. Treat the question's 80% as a rhetorical prompt, "
        "not a measured failure rate: intervention follows documented defects, cash "
        "coverage, and payment evidence rather than an invented industry statistic."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wrap interest margin",
            "note": "28% net margin; $28,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$475,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wrap interest margin",
            "note": "40.0% net margin; $190,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$850,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wrap interest margin",
            "note": "52% net margin; $442,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Kill the Deal Before a Senior Lien Kills the Spread",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is treating a subject-to deed as a lender-approved "
                    "assumption. Title can transfer while the seller remains personally liable "
                    "on the existing note; neither a servicing agreement nor punctual payments "
                    "automatically removes the lender's contractual acceleration rights. Read "
                    "the note, security instrument, riders, modification history, and any "
                    "assumption provisions before quoting a spread. Under 12 U.S.C. § 1701j-3, "
                    "certain transfers receive statutory protection, but an ordinary investor "
                    "purchase does not become protected merely because someone inserts a trust. "
                    "The inter vivos trust exception has specific borrower-beneficiary and "
                    "occupancy-right conditions. Never manufacture occupancy statements or hide "
                    "a transfer through misleading correspondence. Obtain written lender "
                    "consent or model acceleration as a live exposure. For an illustrative "
                    "$180,000 senior balance, $15,000 of cash cannot fund payoff; even a "
                    "refinance requires executable credit, valuation, timing, and closing "
                    "proceeds. Maintain an independent sale alternative and a current payoff "
                    "estimate. Stop acquisition when neither consent nor a credible payoff "
                    "path exists within the proposed risk budget. A low coupon is valuable "
                    "only while the capital structure survives the lender exercising its "
                    "rights. Document who receives lender notices and how the seller forwards "
                    "them immediately, without surrendering access to their own account."
                ),
                (
                    "The second trap is buying an attractive payment instead of a verified "
                    "lien stack. Obtain a title commitment, recorded instruments, current "
                    "senior statement, authorized payoff information, tax status, association "
                    "balances, and pending foreclosure docket entries. A reinstatement quote "
                    "does not establish a full payoff, and an online balance may omit "
                    "recoverable advances, default interest, trustee charges, or a deferred "
                    "modification balance. Ask the title agent to identify junior liens, "
                    "judgments, vesting defects, marital interests, and exceptions that remain "
                    "after closing. For a $220,000 property with $180,000 senior debt, an "
                    "undiscovered $18,000 junior lien consumes nearly half the apparent "
                    "$40,000 equity before selling expenses. An $8,000 tax lien and $12,000 "
                    "disposition budget eliminate the rest. Do not describe that exposure "
                    "as a documentation inconvenience. Require an updated search through "
                    "recording, documented releases where needed, and explicit allocation "
                    "of cure costs. Fraudulent notarization, forged seller authority, or "
                    "an unsupported power of attorney requires stopping the transaction, "
                    "not adding a price discount. The fallback is a properly cured closing "
                    "or withdrawal. Maintain evidence of seller identity and voluntary "
                    "execution through the closing professional, with access restricted "
                    "to people actually performing the transaction."
                ),
                (
                    "The third and fourth traps are buying a foreclosure clock and leaving "
                    "insurance written for yesterday's ownership. Public notices can identify "
                    "distress, but they do not establish sufficient time to cure, transfer "
                    "title, underwrite a buyer, or record documents. Have local foreclosure "
                    "counsel map the actual sale date, postponement evidence, reinstatement "
                    "deadline, and any bankruptcy stay under 11 U.S.C. § 362. Do not assume "
                    "a seller's verbal account of postponement changes the docket. Separately, "
                    "have the insurance producer confirm the correct insured interests, "
                    "occupancy, vacancy conditions, mortgagee provisions, deductibles, and "
                    "effective dates. A seller's old homeowner policy is not an operating "
                    "plan for an investor-owned property occupied by a wrap buyer. Bind "
                    "appropriate coverage without misrepresenting ownership. Budget taxes "
                    "and insurance from current assessments and replacement-cost quotations, "
                    "not last year's escrow installment. If monthly escrow rises from "
                    "$350 to $525, the additional $175 consumes 35% of a $500 monthly "
                    "spread before servicing. Require a reserve replenishment plan before "
                    "releasing distributions. The circuit-breaker is immediate review of "
                    "any cancellation, force-placed coverage notice, tax delinquency, or "
                    "unverified sale postponement; those events outrank a new acquisition "
                    "and receive a named owner on the same business day."
                ),
            ],
            "table": {
                "caption": "Senior-Lien and Property Defects That Defeat Apparently Cheap Debt",
                "headers": [
                    "Failure mechanism",
                    "Evidence required before committing acquisition capital",
                    "Internal escalation threshold",
                    "Operator fallback and responsible specialist",
                ],
                "rows": [
                    [
                        "Unapproved ownership transfer exposes the senior loan to acceleration.",
                        "Executed loan documents and written lender responses establish actual rights.",
                        "Any unresolved acceleration notice suspends discretionary owner distributions immediately.",
                        "Transaction counsel evaluates consent, funded refinance, or orderly property sale.",
                    ],
                    [
                        "Trust paperwork is incorrectly treated as universal transfer protection.",
                        "Counsel documents statutory conditions against actual beneficiary and occupancy facts.",
                        "Any mismatch between claimed exception and facts stops reliance.",
                        "Use an ordinary disclosed transfer with separately underwritten acceleration exposure.",
                    ],
                    [
                        "Junior liens consume equity assumed available for a workout.",
                        "Title commitment and updated search identify liens through recording.",
                        "Any unreleased monetary lien requires documented treatment before closing.",
                        "Title agent obtains releases or revises closing proceeds and economics.",
                    ],
                    [
                        "Deferred principal makes an online mortgage balance materially incomplete.",
                        "Authorized payoff statement includes advances, fees, and deferred amounts.",
                        "Any payoff variance exceeding documented reserves triggers complete repricing.",
                        "Obtain a corrected payoff and rebuild the acquisition waterfall.",
                    ],
                    [
                        "A scheduled trustee sale outruns the proposed closing timeline.",
                        "Foreclosure counsel verifies deadlines directly against docket and trustee evidence.",
                        "Any unverified postponement prevents reliance on additional closing time.",
                        "Secure documented resolution or abandon the acquisition before funding.",
                    ],
                    [
                        "Incorrect insured interests create coverage disputes after a casualty.",
                        "Insurance producer confirms ownership, occupancy, insured interests, and effective dates.",
                        "Any lapse or material application mismatch receives immediate escalation.",
                        "Bind suitable replacement coverage and recalculate carrying costs before proceeding.",
                    ],
                    [
                        "Tax reassessment erases spread hidden by historical escrow estimates.",
                        "Current assessor records and jurisdiction-specific reassessment rules support projections.",
                        "A projected reserve shortfall blocks release of discretionary distributions.",
                        "Increase reserves or reject economics that require stale tax assumptions.",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Verifications Before Acquisition Funds Leave Escrow",
                "body": (
                    "These are transaction-specific release conditions, not substitutes for "
                    "lender consent or jurisdiction-specific underwriting."
                ),
                "items": [
                    "Have transaction counsel document the due-on-sale analysis and an executable payoff alternative for the actual senior balance.",
                    "Require the title agent to reconcile every lien, deferred balance, release, and recording exception to the settlement statement.",
                    "Obtain an effective insurance binder and a tax-and-insurance reserve projection reflecting the new ownership and occupancy.",
                    "Confirm seller identity, signing authority, foreclosure timing, and notice-delivery responsibilities before authorizing disbursement.",
                ],
            },
        },
        {
            "heading": "2. Originate a Collectible Note Instead of a Refund Obligation",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The fifth trap is assuming seller financing sits outside mortgage "
                    "origination rules. For every owner-occupant wrap buyer, this operating "
                    "model uses a properly licensed residential mortgage loan originator "
                    "and a documented ability-to-repay assessment. Verify the individual "
                    "and sponsoring entity through NMLS Consumer Access, then verify "
                    "authority for the property state and proposed activity. The SAFE "
                    "Act framework in 12 U.S.C. §§ 5101–5116 and state implementation "
                    "govern licensing; Regulation Z separately addresses loan-originator "
                    "rules, covered-creditor duties, and repayment analysis. Seller-financer "
                    "exclusions under 12 CFR § 1026.36(a)(4) and (5) have distinct "
                    "conditions and do not erase every other obligation. Require counsel "
                    "and the RMLO to classify creditor status, transaction coverage, "
                    "disclosures, high-cost features, and applicable state restrictions "
                    "before choosing terms. Underwrite income, assets relied upon, existing "
                    "obligations, housing costs, and payment changes using reliable records "
                    "where required. A buyer earning $5,000 monthly with $2,200 housing "
                    "expense and $900 other debt has a 62% illustrative debt-to-income "
                    "ratio; a large deposit does not cure unaffordable payments. Reject "
                    "fabricated income, coached omissions, and undocumented exceptions. "
                    "The fallback is a supportable structure or no loan, never a "
                    "stronger collection script."
                ),
                (
                    "The sixth trap is confusing signed disclosure pages with an enforceable "
                    "closing process. In Texas, examine both Tex. Prop. Code § 5.016 "
                    "and the wrap mortgage framework in Tex. Fin. Code Chapter 159; "
                    "their applicability, exceptions, notices, timing, licensing, and "
                    "remedies require separate analysis. Section 5.016 addresses covered "
                    "conveyances subject to recorded liens and includes advance notice "
                    "requirements; do not reduce the analysis to a buyer initialing "
                    "a form at the signing table. Chapter 159 adds wrap-specific "
                    "requirements that a generic deed package can miss. Maintain dated "
                    "delivery evidence and have Texas counsel confirm the closing "
                    "professional and document package satisfy the applicable provisions. "
                    "A purchase-money residential mortgage generally falls outside the "
                    "federal rescission right under 12 CFR § 1026.23(f)(1), but that "
                    "does not eliminate state remedies or cure other federal disclosure "
                    "defects. Avoid promising one universal cancellation period. For an "
                    "illustrative $20,000 buyer deposit, retain sufficient transaction "
                    "liquidity until delivery, funding, and applicable cancellation "
                    "conditions are resolved. If a valid refund obligation arises after "
                    "the operator spent $15,000 on unrelated acquisitions, accounting "
                    "profit offers no defense against a cash shortfall. Track the "
                    "refund exposure separately from recognized spread."
                ),
                (
                    "The seventh and eighth traps are counting all collected cash as "
                    "revenue and believing the property substitutes for defensible "
                    "servicing records. Split each buyer payment into principal, interest, "
                    "tax and insurance escrow, authorized fees, and any suspense amount. "
                    "The retained interest spread is distinct from principal recovery "
                    "and fiduciary or custodial balances. Likewise, a down payment may "
                    "contain amounts needed to cure arrears, pay settlement expenses, "
                    "fund reserves, or satisfy refund conditions; cash receipt alone "
                    "does not establish earned upfront spread. Have the accountant "
                    "document recognition under the applicable accounting framework, "
                    "including principal-versus-agent analysis where relevant. Do not "
                    "apply a second retained-share haircut to the canonical figures, "
                    "which already exclude underlying home value and pass-through "
                    "debt service. Preserve the executed note, security instrument, "
                    "endorsements, assignments, payment history, and custody trail. "
                    "UCC § 3-301 concerns entitlement to enforce qualifying negotiable "
                    "instruments; state enactments, instrument language, and mortgage "
                    "law determine the actual enforcement route. A scanned PDF does "
                    "not universally replace custody of the original paper note. "
                    "Stop secondary sales when chain-of-title or payment representations "
                    "cannot be substantiated. Contractual repurchase demands can reverse "
                    "months of spread through principal reimbursement, accrued amounts, "
                    "and negotiated expense recovery."
                ),
            ],
            "table": {
                "caption": "Origination, Refund, and Note-Sale Defects with Concrete File Controls",
                "headers": [
                    "Beginner shortcut and resulting exposure",
                    "Required file evidence and responsible reviewer",
                    "Internal stop condition or forensic metric",
                    "Correction before additional capital is committed",
                ],
                "rows": [
                    [
                        "An unlicensed intermediary arranges covered consumer mortgage credit.",
                        "NMLS records and state requirements support the assigned RMLO's authority.",
                        "Any unresolved licensing mismatch prevents further origination work or closing.",
                        "Replace the intermediary and review all previously affected transactions.",
                    ],
                    [
                        "Buyer deposits replace verified evidence of repayment capacity.",
                        "RMLO assessment documents income, obligations, housing costs, and repayment assumptions.",
                        "Any unsupported material underwriting input stops the proposed credit decision.",
                        "Rebuild underwriting from reliable evidence or decline the transaction.",
                    ],
                    [
                        "Generic seller-financer exclusions are applied beyond their actual conditions.",
                        "Counsel records transaction classification and each claimed exclusion's supporting facts.",
                        "Any unmet exclusion condition requires analysis under the applicable full rules.",
                        "Use a properly licensed structure and required disclosures before closing.",
                    ],
                    [
                        "Texas wrap notices are delivered only at document signing.",
                        "Counsel verifies applicable timing, delivery evidence, forms, and closing requirements.",
                        "Any missed applicable notice requirement suspends the planned closing schedule.",
                        "Reset the closing timetable and resolve statutory remedies with counsel.",
                    ],
                    [
                        "Refundable buyer funds finance unrelated acquisition expenses prematurely.",
                        "Accountant reconciles deposit restrictions and current refund exposure by transaction.",
                        "Any unfunded enforceable refund exposure stops discretionary cash withdrawals.",
                        "Restore required liquidity and resolve the buyer obligation promptly.",
                    ],
                    [
                        "Principal collections and escrow balances inflate reported operating revenue.",
                        "Monthly ledger separates principal, retained interest, custodial balances, and fees.",
                        "Any unexplained ledger classification variance requires reconciliation before reporting.",
                        "Correct revenue entries and rebuild the transaction cash waterfall.",
                    ],
                    [
                        "Unsupported note-sale representations create expensive contractual repurchase demands.",
                        "Custodian and counsel verify originals, endorsements, assignments, and payment evidence.",
                        "Any material custody or representation defect suspends the proposed sale.",
                        "Cure documentation or retain the asset without unsupported warranties.",
                    ],
                ],
            },
        },
        {
            "heading": "3. Audit Cash at Both Loans and Stress the Owner-Profit Cases",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The ninth trap is monitoring the wrap receipt while ignoring the "
                    "underlying mortgage. Use a licensed third-party servicer authorized "
                    "for the jurisdiction and product, with a contract that allocates "
                    "senior payments, escrow administration, statements, complaints, "
                    "and exception handling. Obtain seller-authorized access or delivery "
                    "of senior statements without impersonating the borrower or sharing "
                    "credentials improperly. Reconcile three independent records: "
                    "cleared buyer receipts, the servicer's allocation ledger, and "
                    "the senior lender's posted payment. A servicer disbursement "
                    "confirmation alone does not prove correct lender application. "
                    "Set internal alerts when a scheduled senior payment lacks posting "
                    "evidence two business days after its expected posting date, when "
                    "any escrow balance becomes negative, or when a notice reports "
                    "delinquency despite a successful disbursement. These are chosen "
                    "operating thresholds, not statutory grace periods. ACH returns, "
                    "partial payments, reversals, and suspense allocations require "
                    "separate exception queues. A $1,650 buyer payment less $1,150 "
                    "senior principal and interest, $350 tax and insurance provision, "
                    "and $35 servicing cost leaves $115 in cash before other costs. "
                    "That cash residual is not automatically retained interest revenue: "
                    "both loans' principal components must still be separated. Never "
                    "market the $500 headline difference as spendable monthly profit."
                ),
                (
                    "The tenth trap is treating foreclosure carrying cost as a remote "
                    "legal bill rather than a liquidity schedule. Model missed receipts, "
                    "senior debt service, insurance, taxes, preservation, counsel, sale "
                    "expenses, and recovery timing separately. Six months at $1,500 "
                    "of unavoidable property carrying cost consumes $9,000; add "
                    "$7,000 of legal and preservation expense and the illustrative "
                    "workout requires $16,000 before any recovery. A $10,000 reserve "
                    "covers only 62.5% of that stress budget. If the senior payment "
                    "continues while the buyer defaults, that reserve cannot be "
                    "replaced by a spreadsheet receivable. Track delinquency buckets, "
                    "broken payment promises, returned debits, legal milestones, and "
                    "liquid unrestricted cash against each property's next obligations. "
                    "Choose a minimum six-month carrying reserve plus a separately "
                    "priced workout allowance as an internal starting policy, then "
                    "increase it for slower jurisdictions and concentrated portfolios. "
                    "Apply applicable servicing, notice, loss-mitigation, and foreclosure "
                    "requirements before enforcement; Regulation X obligations depend "
                    "on coverage and any relevant exemptions. Do not improvise lockouts "
                    "or utility shutoffs. A workout may preserve more value than "
                    "immediate enforcement, but modifications require a documented "
                    "affordability analysis, senior-loan protection, and an updated "
                    "net recovery comparison."
                ),
                (
                    "The eleventh trap is using scale to hide negative exception economics. "
                    "The canonical Conservative case is $100,000 annual operator revenue "
                    "at 28% margin, producing $28,000 owner profit and $72,000 implied "
                    "costs with 1 FT plus 3 C. Base is $475,000 at 40.0%, producing "
                    "$190,000 and $285,000 implied costs with the same team. Scaled "
                    "is $850,000 at 52%, producing $442,000 and $408,000 implied costs "
                    "with 2 FT plus 4 C. These revenue figures comprise net upfront "
                    "spreads and retained wrap interest margin, not property value, "
                    "loan principal, or total borrower remittances. Reconcile monthly "
                    "reports to those definitions before comparing margins. As a "
                    "separate sensitivity, one unrecovered $16,000 workout expense "
                    "reduces Base profit to $174,000 and margin to approximately "
                    "36.63% if revenue and all other costs remain unchanged. It "
                    "does not replace the canonical Base case. Track exception "
                    "cost per active note, reserve coverage, refund liabilities, "
                    "and concentration by senior lender, servicer, jurisdiction, "
                    "and maturity month. Pause acquisitions when required reserves "
                    "are unfunded or existing exceptions lack accountable owners. "
                    "Automation should expose discrepancies faster; it must not "
                    "permit one employee to change payment instructions, approve "
                    "disbursement, and certify the same reconciliation."
                ),
            ],
            "table": {
                "caption": "Internal Telemetry Thresholds and Formula v2.0 Profit Reconciliation",
                "headers": [
                    "Metric and explicit calculation",
                    "Evidence source and review frequency",
                    "Chosen internal escalation threshold",
                    "Immediate intervention and economic interpretation",
                ],
                "rows": [
                    [
                        "Senior posting lag measures elapsed business days after expected posting.",
                        "Compare lender statements against servicer disbursements every business day.",
                        "Escalate after two business days without independently verified posting.",
                        "Trace the payment before assuming the senior loan remains current.",
                    ],
                    [
                        "Escrow coverage compares available balances with scheduled property obligations.",
                        "Review escrow ledger, tax bills, and insurance notices every month.",
                        "Any projected shortage before an obligation falls due requires action.",
                        "Fund the shortage and suspend discretionary distributions until coverage returns.",
                    ],
                    [
                        "ACH return rate divides returned collection attempts by total attempts.",
                        "Review servicer return codes and cohort denominators each collection cycle.",
                        "Investigate every return; two repeated returns trigger individual account review.",
                        "Resolve authorization or affordability problems without repeated unauthorized debit attempts.",
                    ],
                    [
                        "Workout coverage divides unrestricted allocated reserves by modeled workout cash.",
                        "Update carrying-cost budgets and legal estimates monthly for distressed accounts.",
                        "Coverage below one hundred percent blocks acquisition-funded reserve depletion.",
                        "Replenish cash or reduce exposure through an executable recovery plan.",
                    ],
                    [
                        "Conservative reconciles $100,000 revenue less $72,000 implied annual costs.",
                        "Monthly ledger supports $28,000 owner profit at twenty-eight percent margin.",
                        "Any inclusion of principal or custodial balances invalidates the comparison.",
                        "Maintain the canonical staffing assumption of one employee plus three contractors.",
                    ],
                    [
                        "Base reconciles $475,000 revenue less $285,000 implied annual costs.",
                        "Monthly ledger supports $190,000 owner profit at forty percent margin.",
                        "Additional $16,000 unrecovered expense reduces sensitivity profit to $174,000.",
                        "Keep the sensitivity separate from the unchanged canonical Base case.",
                    ],
                    [
                        "Scaled reconciles $850,000 revenue less $408,000 implied annual costs.",
                        "Monthly ledger supports $442,000 owner profit at fifty-two percent margin.",
                        "Unfunded reserves or unmanaged exceptions suspend further portfolio expansion.",
                        "Retain the staffing assumption of two employees plus four contractors.",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the Servicer Prove the Entire Cash Chain",
                "body": (
                    "Veteran operators measure the state of both loans and the property, "
                    "not merely whether a buyer's debit succeeded."
                ),
                "items": [
                    "Reconcile by property identifier and payment period so a correctly sized payment applied to the wrong loan cannot pass the audit.",
                    "Calendar tax bills and insurance renewals independently of servicer reminders; investigate any unexplained escrow withdrawal before distributions.",
                    "Maintain a reserve schedule by property and stress event, preventing one cash balance from being counted against several simultaneous defaults.",
                    "Require independent callback verification for changed payment instructions and dual authorization before releasing funds to a new destination.",
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the affected cash waterfall",
                    "action": "Suspend discretionary distributions for the affected property when a payment, reserve, or notice exception appears.",
                    "detail": "Continue required protective payments through verified channels; record the alert time, property identifier, and accountable operator.",
                },
                {
                    "step": 2,
                    "title": "Reconstruct the payment chain",
                    "action": "Match bank settlement, servicer allocation, and lender posting using independently obtained records.",
                    "detail": "Separate principal, interest, escrow, suspense, reversals, and fees; document discrepancies without assuming that a successful transfer cured them.",
                },
                {
                    "step": 3,
                    "title": "Choose the funded corrective path",
                    "action": "Coordinate with the servicer, RMLO, accountant, or local counsel according to the defect.",
                    "detail": "Approve a cash-backed cure, lawful workout, refinance, or disposition plan with deadlines and identified funding sources.",
                },
                {
                    "step": 4,
                    "title": "Close only on independent evidence",
                    "action": "Restore normal distributions only after another reviewer verifies posting, coverage, and corrected records.",
                    "detail": "Retain the evidence package and revise the control that allowed the defect, including vendor performance tracking where relevant.",
                },
            ],
        },
        {
            "heading": "4. Replace Deceptive Acquisition Shortcuts with Measurable Private Offers",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The twelfth trap is turning public-record access into an official-looking "
                    "collection scheme. The mapped play public_filing_trigger_mail_arbitrage "
                    "uses daily Secretary of State new-LLC filings and County Recorder "
                    "deed or mortgage recordings to identify timely private offers. "
                    "Its legitimate products include recurring workplace compliance "
                    "updates, property-tax appeal contingency services, and exclusive "
                    "new-mover or B2B introductions. It does not authorize fake "
                    "government poster invoices, deed-copy bills, invented citations, "
                    "or implied mandatory purchases. Under 39 U.S.C. § 3001(d), "
                    "solicitations styled as bills or invoices face specific "
                    "nonmailability rules unless statutory conditions are met; "
                    "other provisions address misleading governmental connections. "
                    "California Business and Professions Code § 17537.9 separately "
                    "regulates covered recorded-document copy solicitations. Use "
                    "unambiguous private commercial branding and describe the "
                    "actual optional service before its price. A new deed can "
                    "represent an ordinary purchase, estate transfer, or internal "
                    "reorganization, not distress or permission to infer personal "
                    "hardship. Validate event types and recipient relevance before "
                    "sending. For subject-to sourcing, keep acquisition offers "
                    "separate from subscription invoices and tax-appeal proposals. "
                    "Never claim the recorder, lender, or state agency selected "
                    "the recipient for your offer. The fallback is a clearly "
                    "private letter that accurately states why the service may "
                    "be useful."
                ),
                (
                    "Operate the trigger pipeline with permitted feeds, documented "
                    "data rights, and limited retention. Deduplicate by jurisdiction, "
                    "recording identifier, property, and mailing address; suppress "
                    "prior opt-outs and returned addresses before a Lob or "
                    "PostGrid API submission. Public availability does not "
                    "override source terms, privacy requirements, or a provider's "
                    "acceptable-use rules. Do not evade blocked access, rotate "
                    "accounts after suspension, or submit a deceptive creative "
                    "through a different print vendor. Archive the exact letter "
                    "version, source event, suppression decision, batch identifier, "
                    "and delivery outcome. Consider an illustrative 1,000-piece "
                    "batch costing $1.20 per delivered attempt, or $1,200. At "
                    "a 2% qualified response rate, 20 responses and a 25% "
                    "response-to-customer conversion produce five customers and "
                    "$240 postage-only acquisition cost each. A genuine $300 "
                    "annual update subscription with $120 direct fulfillment "
                    "cost contributes $180 before acquisition overhead, leaving "
                    "a $60 first-year deficit per customer before data, staff, "
                    "refunds, and payment fees. Recurrence helps only if renewal "
                    "is earned and measured. Pause that cohort rather than "
                    "claiming positive lifetime value from unsupported retention. "
                    "For property-tax appeals, recognize contingent fees only "
                    "when earned under the contract and applicable rules, not "
                    "when a homeowner submits an inquiry."
                ),
                (
                    "The thirteenth trap is mistaking deliverability for permission "
                    "and response for durable contribution. Instrument complaint "
                    "rate, opt-out completion, address failure, refund demand, "
                    "chargeback exposure, and cohort contribution separately. "
                    "Any substantiated government-impersonation complaint warrants "
                    "an immediate batch pause and creative review; any unsuppressed "
                    "opt-out requires correcting the pipeline before the next "
                    "submission. Use an internal returned-mail investigation "
                    "threshold above 5% of a mature batch, while acknowledging "
                    "that provider enforcement uses its own rules and evidence. "
                    "A vendor can suspend or terminate service for deceptive "
                    "content or account abuse even when postage was paid. "
                    "Preserve records and appeal through the vendor's established "
                    "process, not replacement identities. For exclusive lead "
                    "monetization, document authorized sharing, the permitted "
                    "recipient, and exclusivity; never resell the same exclusive "
                    "lead and conceal the duplication. Keep subscription and "
                    "lead economics outside the wrap scorecard unless the "
                    "reporting perimeter explicitly includes them. This chapter's "
                    "mapped-play analysis supplies a controlled sourcing "
                    "alternative, not extra revenue silently added to $475,000 "
                    "Base operator revenue. The final circuit-breaker is "
                    "simple: stop the activity causing the defect, preserve "
                    "evidence, fund existing obligations, and resume only "
                    "after a responsible reviewer verifies the correction "
                    "against the actual file."
                ),
            ],
            "table": {
                "caption": "Trigger-Mail Acquisition Economics, Vendor Risk, and Private-Brand Fallbacks",
                "headers": [
                    "Failure mechanism or unit-economic assumption",
                    "Forensic evidence and practical measurement",
                    "Internal threshold for pausing the activity",
                    "Legitimate fallback preserving the commercial objective",
                ],
                "rows": [
                    [
                        "Government-lookalike invoices imply mandatory payment for optional private services.",
                        "Review archived creative against actual service terms and statutory requirements.",
                        "Any substantiated impersonation complaint immediately pauses the affected creative.",
                        "Replace it with clearly private branding and a genuine optional offer.",
                    ],
                    [
                        "Unclassified deed events falsely identify ordinary owners as distressed sellers.",
                        "Compare recording codes and document context before assigning acquisition intent.",
                        "Any systematic event misclassification stops the affected source segment.",
                        "Use neutral property-service messaging without unsupported claims about hardship.",
                    ],
                    [
                        "Duplicate events generate repeated mail and contradictory service offers.",
                        "Deduplicate jurisdiction, recording identifier, property, recipient, and campaign history.",
                        "Any repeat mailing after recorded opt-out requires immediate pipeline correction.",
                        "Suppress the recipient across connected campaigns before additional API submissions.",
                    ],
                    [
                        "Five customers from $1,200 postage imply $240 acquisition cost.",
                        "Track twenty qualified responses and five purchases from one thousand attempts.",
                        "Measured acquisition cost exceeding earned contribution pauses that customer cohort.",
                        "Improve targeting or offer economics without assuming unobserved future renewals.",
                    ],
                    [
                        "A $300 subscription less $120 fulfillment yields $180 contribution.",
                        "Subtract refunds, payment fees, data costs, and acquisition overhead separately.",
                        "The illustrative $60 first-year deficit precedes all additional overhead.",
                        "Retest pricing and delivery costs before increasing the mailing budget.",
                    ],
                    [
                        "Restricted source access or deceptive content causes vendor account termination.",
                        "Retain source permissions, provider notices, creative versions, and submission logs.",
                        "Any access revocation or vendor suspension stops the affected integration.",
                        "Resolve the documented issue through authorized review rather than identity changes.",
                    ],
                    [
                        "Duplicate exclusive leads create refunds and undermine downstream buyer trust.",
                        "Maintain recipient permissions, sale records, and enforceable exclusivity commitments.",
                        "Any duplicate exclusive sale stops further distribution of that lead.",
                        "Refund according to obligations and repair exclusivity checks before resuming.",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A wrap spread is only worth distributing after the senior payment, property reserves, and enforceable borrower obligations reconcile.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build a property-level evidence file linking the senior note, title commitment, payoff estimate, insurance binder, and acceleration response plan.",
        "Have the licensed RMLO and local counsel document buyer underwriting, transaction classification, state wrap requirements, and dated disclosure delivery.",
        "Separate principal, escrow, refundable deposits, retained interest, and earned upfront spreads before comparing results with the canonical scorecard.",
        "Reconcile cleared buyer funds, servicer allocation, and senior lender posting; assign every exception an owner and a funded correction deadline.",
        "Stress each property for six months of carrying costs plus a separately priced workout, and block distributions when required reserves are unfunded.",
        "Audit trigger-mail branding, source permissions, suppression logic, exclusivity, and cohort contribution before submitting another acquisition batch.",
    ],
    "statutory_citations": [
        {
            "title": "12 U.S.C. § 1701j-3 — Preemption of due-on-sale prohibitions",
            "url": "https://www.law.cornell.edu/uscode/text/12/1701j-3",
            "relevance": "Establishes the federal due-on-sale framework and enumerated protected transfers; a subject-to acquisition requires analysis of actual facts and loan documents.",
        },
        {
            "title": "12 U.S.C. § 5103 — Mortgage loan originator licensing and registration",
            "url": "https://www.law.cornell.edu/uscode/text/12/5103",
            "relevance": "Supports verification of the mortgage originator's licensing or registration status alongside applicable state implementation requirements.",
        },
        {
            "title": "12 CFR § 1026.36 — Prohibited acts or practices and loan-originator requirements",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.36",
            "relevance": "Includes seller-financer exclusions with specific conditions and rules affecting loan-originator conduct; exclusions must not be treated as universal exemptions.",
        },
        {
            "title": "12 CFR § 1026.43 — Minimum standards for transactions secured by a dwelling",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.43",
            "relevance": "Defines ability-to-repay requirements for covered transactions, including evaluation and verification of relevant repayment factors.",
        },
        {
            "title": "12 CFR § 1026.23 — Right of rescission",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.23",
            "relevance": "Distinguishes covered rescindable transactions from exceptions, including residential mortgage transactions, without displacing separate state remedies.",
        },
        {
            "title": "Tex. Prop. Code § 5.016 — Conveyance of residential property encumbered by lien",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.016",
            "relevance": "Addresses notices, timing, exceptions, and remedies for covered conveyances subject to recorded liens; delivery must be evaluated before closing.",
        },
        {
            "title": "Tex. Fin. Code Chapter 159 — Wrap Mortgage Loan Financing",
            "url": "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
            "relevance": "Provides Texas wrap-specific licensing and transaction requirements, including disclosure and closing provisions requiring dedicated review.",
        },
        {
            "title": "11 U.S.C. § 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "Requires bankruptcy-related stay analysis before pursuing affected collection, foreclosure, or transfer activity.",
        },
        {
            "title": "12 CFR § 1024.41 — Loss mitigation procedures",
            "url": "https://www.ecfr.gov/current/title-12/section-1024.41",
            "relevance": "Supplies servicing and foreclosure-related procedures for covered mortgage loans, subject to scope and applicable exemptions.",
        },
        {
            "title": "39 U.S.C. § 3001 — Nonmailable matter",
            "url": "https://www.law.cornell.edu/uscode/text/39/3001",
            "relevance": "Addresses invoice-styled solicitations and misleading governmental connections; trigger-mail creative must accurately identify the private commercial offer.",
        },
        {
            "title": "Cal. Bus. & Prof. Code § 17537.9 — Recorded-document solicitation requirements",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17537.9.",
            "relevance": "Imposes requirements on covered solicitations offering copies of recorded documents, reinforcing the need for state-specific creative review.",
        },
    ],
}
