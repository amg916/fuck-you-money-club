from __future__ import annotations


def build_volume_041_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-041-buying-group-card-float-and-rebate-arbitrage",
        "volume_id": "vol-041-buying-group-card-float-and-rebate-arbitrage",
        "title": (
            "Buying Group, Commercial Card-Float & Rebate Arbitrage "
            "— Operator Companion Workbook"
        ),
        "subtitle": (
            "6 Printable Operator Worksheets for Wholesale Buying-Group "
            "Underwriting, Commercial Card and Portal Spread Testing, "
            "Repayment-Safe Treasury Sweeps, Auditable Execution, "
            "Automation Controls, and a Measured 30-Day Launch"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": (
                    "Arbitrage Deal / Counterparty Underwriting "
                    "& Spread Qualification"
                ),
                "purpose": (
                    "Qualify each opportunity before committing purchasing capacity. "
                    "Separate wholesale fulfillment, commercial card and portal "
                    "rebates, and treasury earnings into distinct economic models. "
                    "Document enforceable commitments, settlement behavior, reward "
                    "eligibility, and repayment resources so apparent spread never "
                    "conceals counterparty exposure or borrowed principal."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Assign every opportunity to one primary model before "
                        "calculating returns. Record merchandise reimbursement, "
                        "purchase-linked rewards, and treasury income in separate "
                        "columns, even when one operating cycle produces all three. "
                        "Never present card capacity or merchant transaction volume "
                        "as earned income."
                    ),
                    (
                        "Obtain the buying group's written quantity, SKU, destination, "
                        "acceptance criteria, and payout clock before ordering. Treat "
                        "BuyForMeRetail, Pointsmaker, and MaxOutDeals as candidates "
                        "requiring current verification, rather than assuming their "
                        "terms, warehouse capacity, or settlement reliability."
                    ),
                    (
                        "Verify sales-tax treatment using the actual seller, delivery "
                        "destination, resale documentation, and transaction facts. "
                        "A DE, NH, or OR warehouse address alone does not establish "
                        "that every charge disappears or that a particular retailer "
                        "will accept your documentation."
                    ),
                    (
                        "Price the opportunity without speculative rewards first. "
                        "Then add separately supported commercial card rewards and "
                        "one eligible shopping portal. Check resale exclusions, "
                        "category caps, offer activation, and payment-method restrictions "
                        "before describing any reward rate as available."
                    ),
                    (
                        "Approve only quantities that survive delayed reimbursement "
                        "without interest-bearing balances or emergency sales. Record "
                        "the person responsible for settlement escalation, the cash "
                        "reserve supporting repayment, and the precise conditions "
                        "that suspend additional purchases from the same counterparty."
                    ),
                ],
                "fields": [
                    field(
                        "Primary model and income boundaries",
                        "textarea",
                        (
                            "Identify the primary operating model, the paying party, "
                            "the purchased asset or service, and each separate income "
                            "stream. Explain which amounts are reimbursements, "
                            "purchase-price adjustments, earned fees, or interest."
                        ),
                        (
                            "Deal BG-001 is wholesale fulfillment, not a treasury "
                            "trade. Ten devices cost $8,000 and carry an $8,240 "
                            "written reimbursement commitment. A supported $160 card "
                            "reward is tracked separately. Potential portal rewards "
                            "and subsequent interest remain separate records; the "
                            "$8,000 card liability is never earnings."
                        ),
                    ),
                    field(
                        "Counterparty identity and verified settlement history",
                        "textarea",
                        (
                            "Record the contracting entity, independently confirmed "
                            "payment instructions, evidence sources, and observed "
                            "settlement distribution. Distinguish your own completed "
                            "transactions from marketing statements or another "
                            "operator's unverified experience."
                        ),
                        (
                            "The pilot file for a prospective Pointsmaker arrangement "
                            "must contain its current contracting entity and independently "
                            "confirmed payout details before release. Illustrative "
                            "internal results from five later pilot lots show settlement "
                            "in three, four, four, five, and eight business days, "
                            "supporting an eight-day stress input."
                        ),
                    ),
                    field(
                        "Written commitment and acceptance specification",
                        "textarea",
                        (
                            "Capture the commitment identifier, exact product "
                            "configuration, quantity ceiling, delivery window, "
                            "inspection rules, and payment trigger. State how "
                            "substitutions, late arrivals, rejected units, and "
                            "commitment cancellation affect reimbursement."
                        ),
                        (
                            "Commitment BG-001 covers ten sealed devices with matching "
                            "manufacturer SKU and serial-number records at $824 each. "
                            "The proposed addendum requires inspection within two "
                            "business days after carrier delivery and written defect "
                            "evidence for rejection. Substitutions require written "
                            "acceptance before purchase; silence does not authorize "
                            "different merchandise."
                        ),
                    ),
                    field(
                        "Warehouse destination and tax sourcing evidence",
                        "textarea",
                        (
                            "Identify the actual receiving warehouse, seller tax "
                            "treatment, resale-certificate status, and evidence retained. "
                            "Explain why the transaction receives its recorded "
                            "treatment rather than relying exclusively on a "
                            "destination abbreviation."
                        ),
                        (
                            "The selected shipment goes to a verified DE receiving "
                            "address listed in the commitment. The retailer invoice "
                            "shows zero sales tax and the shipping record matches "
                            "that destination. The file retains the resale certificate "
                            "where applicable, seller acceptance, and transaction-specific "
                            "sourcing support rather than a blanket exemption assumption."
                        ),
                    ),
                    field(
                        "Commercial card reward eligibility",
                        "textarea",
                        (
                            "Record the exact business card program, eligible "
                            "transaction category, reward rate, exclusions, limits, "
                            "posting delay, and issuer terms. Distinguish a documented "
                            "uncapped rate from a promotional headline or "
                            "conditional offer."
                        ),
                        (
                            "For this illustrative deal, the current business card "
                            "agreement supports 2% on the $8,000 eligible merchandise "
                            "purchase, producing $160. The evidence packet includes "
                            "the applicable terms and transaction category. A separate "
                            "4% offer is excluded until activation, category matching, "
                            "remaining capacity, and resale eligibility are documented."
                        ),
                    ),
                    field(
                        "Portal attribution and stacking decision",
                        "textarea",
                        (
                            "Choose one shopping portal per transaction and document "
                            "its attribution requirements, resale restrictions, coupon "
                            "rules, payout conditions, and reversal window. Explain "
                            "whether portal value enters the base calculation "
                            "or only conditional upside."
                        ),
                        (
                            "Rakuten and TopCashback are compared, but only one "
                            "tracking path is selected. A possible 1% reward would "
                            "add $80 on $8,000 of eligible merchandise. Because "
                            "wholesale eligibility remains unverified in this example, "
                            "the approved base spread includes zero portal income; "
                            "$80 appears only as conditional upside."
                        ),
                    ),
                    field(
                        "B2B invoice fee-versus-rebate screen",
                        "textarea",
                        (
                            "For a separate Plastiq or Melio opportunity, document "
                            "the real invoice, permitted payment route, current "
                            "quoted fee, reward treatment, and recipient settlement "
                            "timing. Calculate spread without borrowing assumptions "
                            "that the transaction cannot support."
                        ),
                        (
                            "A hypothetical $10,000 supplier invoice carries a quoted "
                            "2.9% processing fee, or $290. If the issuer awards "
                            "$200 on the invoice amount only, the transaction loses "
                            "$90 before other costs. It is rejected. The example "
                            "uses an input quote, not a claim about either platform's "
                            "current pricing."
                        ),
                    ),
                    field(
                        "Treasury opportunity and available cash source",
                        "textarea",
                        (
                            "Identify whether deployable cash is owner capital or "
                            "cleared operating proceeds. Record the repayment reserve, "
                            "eligible holding period, expected yield, bonus conditions, "
                            "and withdrawal timing before treating treasury earnings "
                            "as incremental value."
                        ),
                        (
                            "An independent $10,000 owner-funded cash allocation may "
                            "earn approximately $34.52 over 28 days at a 4.5% "
                            "simple annualized rate using 365 days. The card repayment "
                            "reserve is excluded. Any bank bonus remains separate "
                            "until its deposit, balance, duration, account-status, "
                            "and payout requirements are satisfied."
                        ),
                    ),
                    field(
                        "Concentration limit and delayed-payout stress",
                        "textarea",
                        (
                            "Set counterparty and issuer exposure limits using "
                            "unsettled purchase cost, not expected rewards. Describe "
                            "the longest modeled payout delay, available unrestricted "
                            "cash, and the stop-purchase trigger protecting "
                            "statement repayment."
                        ),
                        (
                            "The first counterparty receives an $8,000 unsettled-cost "
                            "limit against $20,000 of unrestricted cash. An eight-business-day "
                            "payout stress leaves the statement fully repayable. "
                            "Additional commitments stop when any accepted lot passes "
                            "its written payment date or total unsettled cost would "
                            "exceed the limit, even if attractive offers remain."
                        ),
                    ),
                    field(
                        "Approved spread and rejection rationale",
                        "textarea",
                        (
                            "Summarize contribution before overhead, distinguish "
                            "confirmed assumptions from conditional upside, and "
                            "document the acceptance decision. Include merchandise "
                            "cost, shipping, loss provision, rewards, and the "
                            "specific remaining verification steps."
                        ),
                        (
                            "BG-001 shows $240 merchandise spread plus $160 supported "
                            "card rewards, less $60 shipping and a $40 loss "
                            "provision, yielding $300 expected contribution. Verified "
                            "portal eligibility could add $80 later. Purchase remains "
                            "blocked until the commitment and shipping coverage are "
                            "confirmed; future card rewards cannot fund today's repayment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when the commitment, counterparty identity, "
                    "destination treatment, supported reward terms, $300 base "
                    "contribution, and full repayment resources are documented. "
                    "Leave the $80 conditional portal amount outside the approved "
                    "base case until eligibility evidence resolves it."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": (
                    "Unit Economics, Escrow/Reserve Float "
                    "& Working-Capital Calculator"
                ),
                "purpose": (
                    "Build a cash-first operating model that reconciles individual "
                    "deals with the supplied annual scorecard. Separate gross "
                    "activity, retained contribution, owner profit, restricted "
                    "balances, and card liabilities. Stress timing mismatches "
                    "before allocating cleared cash to bank bonuses or T-bill "
                    "holdings."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Create three economic schedules: wholesale merchandise, "
                        "commercial card and portal rebates, and treasury income. "
                        "Link them through transaction identifiers without combining "
                        "their denominators. An $8,000 merchandise purchase, a "
                        "$160 reward, and an $8,000 liability describe different "
                        "economic facts."
                    ),
                    (
                        "Enter the Conservative, Base, and Scaled figures exactly "
                        "as supplied. Apply the 35% retained-share assumption to "
                        "gross scorecard revenue, then reconcile remaining costs "
                        "to owner profit. Do not force individual electronics "
                        "transactions to exhibit that portfolio-level retained share."
                    ),
                    (
                        "Build the payment calendar from actual purchase, statement "
                        "closing, payment due, warehouse acceptance, and cleared "
                        "ACH dates. Treat 55 days as a possible cycle configuration, "
                        "not a universal entitlement. Preserve a conservative "
                        "repayment buffer before any treasury allocation."
                    ),
                    (
                        "Distinguish an internal repayment reserve from contractual "
                        "escrow. Record ownership, withdrawal rights, restrictions, "
                        "and release conditions for every account. Do not describe "
                        "ordinary business cash as protected escrow merely because "
                        "a spreadsheet assigns it a dedicated label."
                    ),
                    (
                        "Run delayed ACH, denied rewards, rejected merchandise, "
                        "carrier loss, and issuer shutdown cases separately and "
                        "together. Show the resulting cash gap and contribution "
                        "loss. Reduce purchase volume whenever survival depends "
                        "on selling assets before their scheduled liquidity date."
                    ),
                ],
                "fields": [
                    field(
                        "Wholesale landed-cost contribution bridge",
                        "textarea",
                        (
                            "Calculate wholesale contribution using committed "
                            "reimbursement less actual merchandise cost, shipping, "
                            "and expected loss. Keep purchase-linked rewards on "
                            "separate lines and distinguish cash expenses from "
                            "noncash planning provisions."
                        ),
                        (
                            "Ten devices cost $8,000; reimbursement is $8,240. "
                            "Shipping costs $60 and the planning loss provision "
                            "is $40, leaving $140 wholesale contribution. Supported "
                            "card rewards add $160, bringing expected combined "
                            "contribution to $300. Cleared reimbursement less merchandise "
                            "and shipping produces $180 cash spread before reward "
                            "posting or realized losses."
                        ),
                    ),
                    field(
                        "Conservative canonical annual reconciliation",
                        "textarea",
                        (
                            "Reconcile the Conservative scenario from gross "
                            "scorecard revenue through the retained-share bridge "
                            "to owner profit. State retained margin, staffing, "
                            "and the distinction between routine overhead and "
                            "other operating costs."
                        ),
                        (
                            "Conservative gross revenue is $250,000. The 65% "
                            "merchandise-cost bridge is $162,500, leaving $87,500 "
                            "retained revenue. Remaining costs total $67,500, leaving "
                            "$20,000 owner profit: 8% gross margin and 22.86% "
                            "retained margin. Staffing is one full-time operator "
                            "plus two contractors; illustrative overhead is $18,000 "
                            "annually within those remaining costs."
                        ),
                    ),
                    field(
                        "Base canonical annual reconciliation",
                        "textarea",
                        (
                            "Reconcile the Base scenario without changing the "
                            "canonical gross amount, owner profit, or retained "
                            "share. Separate monthly overhead from other residual "
                            "costs, and identify the team assumed by the "
                            "scorecard."
                        ),
                        (
                            "Base gross revenue is $1,025,000. Subtract the $666,250 "
                            "merchandise-cost bridge to obtain $358,750 retained "
                            "revenue. Residual costs of $215,250 leave $143,500 "
                            "owner profit, equal to 14% gross and 40% retained "
                            "margins. Illustrative residual costs comprise $54,000 "
                            "annual overhead and $161,250 other costs; staffing "
                            "is one full-time operator plus two contractors."
                        ),
                    ),
                    field(
                        "Scaled canonical annual reconciliation",
                        "textarea",
                        (
                            "Reconcile the Scaled scenario and show both gross "
                            "and retained profit margins. Explain how the "
                            "five-person team and upper monthly overhead input "
                            "fit inside the residual cost allowance."
                        ),
                        (
                            "Scaled gross revenue is $1,800,000. The $1,170,000 "
                            "merchandise-cost bridge leaves $630,000 retained revenue. "
                            "Residual costs of $270,000 leave $360,000 owner "
                            "profit, equal to 20% gross and 57.14% retained "
                            "margins. Staffing is two full-time operators plus "
                            "three contractors. Illustrative annual overhead of "
                            "$108,000 leaves $162,000 for other residual costs."
                        ),
                    ),
                    field(
                        "Scorecard basis versus accounting presentation",
                        "textarea",
                        (
                            "Document the supplied 35% retained-share convention "
                            "and distinguish it from transaction-specific accounting. "
                            "Identify who controls merchandise before transfer "
                            "and how purchase rebates, interest, and principal-agent "
                            "conclusions affect ledger presentation."
                        ),
                        (
                            "The planning bridge labels $358,750 as Base retained "
                            "revenue, but does not automatically establish ASC 606 "
                            "revenue presentation. The accountant evaluates control "
                            "under ASC 606-10-55-36 through 55-40. Purchase-linked "
                            "rebates may reduce inventory cost; interest is separately "
                            "classified. The workbook preserves the canonical bridge "
                            "while maintaining an accounting-policy reconciliation."
                        ),
                    ),
                    field(
                        "Statement dates and usable float days",
                        "textarea",
                        (
                            "Enter actual card dates and calculate the available "
                            "repayment interval for each purchase. Record whether "
                            "the grace period applies, and identify charges "
                            "whose timing differs materially from a headline "
                            "55-day assumption."
                        ),
                        (
                            "An illustrative January 2, 2027 purchase closes on "
                            "January 31 and is due February 25, providing 54 "
                            "calendar days from purchase. A January 30 purchase "
                            "has only 26 days. The operator verifies grace-period "
                            "eligibility and schedules repayment for February 22, "
                            "rather than assuming every charge receives 55 days."
                        ),
                    ),
                    field(
                        "Reserve ownership and escrow restrictions",
                        "textarea",
                        (
                            "List each cash account, balance, legal owner, "
                            "permitted use, and withdrawal restriction. Define "
                            "the amount dedicated to card repayment and "
                            "whether any actual escrow agreement changes access "
                            "or beneficiary rights."
                        ),
                        (
                            "A business deposit account holds $20,000 of owner "
                            "capital. An internal allocation reserves $8,000 for "
                            "the card statement and $2,000 for shipping, disputes, "
                            "and operating variability. This is a management reserve, "
                            "not escrow. No third-party beneficiary or contractual "
                            "release condition exists; $10,000 remains available "
                            "for a separately approved treasury allocation."
                        ),
                    ),
                    field(
                        "Treasury yield and bonus calculator",
                        "textarea",
                        (
                            "Calculate interest using deployable cash, the actual "
                            "holding period, and an explicit yield convention. "
                            "Record bonus qualification separately, and prevent "
                            "the same cash balance from earning overlapping "
                            "returns in the model."
                        ),
                        (
                            "For planning, $10,000 multiplied by 4.5% multiplied "
                            "by 28 divided by 365 equals $34.52 before tax "
                            "and fees. Actual T-bill earnings use purchase price "
                            "and maturity proceeds. A hypothetical $200 bank bonus "
                            "requiring 90 days is excluded from the 28-day result "
                            "and cannot use the same simultaneously allocated dollars."
                        ),
                    ),
                    field(
                        "Combined delayed-ACH and reward-denial stress",
                        "textarea",
                        (
                            "Model reimbursement arriving after the card due "
                            "date while a reward is denied. Show the "
                            "cash required to repay, revised contribution, "
                            "purchasing suspension, and whether an additional "
                            "loss could exhaust available reserves."
                        ),
                        (
                            "Assume the $8,240 reimbursement arrives March 5, "
                            "after the February 25 card due date, and the "
                            "$160 reward is denied. The reserved $8,000 repays "
                            "the card without relying on ACH. Expected contribution "
                            "falls from $300 to $140. New purchases stop; "
                            "any disputed reimbursement triggers a separate "
                            "full-principal loss test."
                        ),
                    ),
                    field(
                        "Working-capital ceiling and startup allocation",
                        "textarea",
                        (
                            "Allocate startup cash within the supplied range "
                            "and calculate the maximum unsettled purchasing "
                            "cost supported without future reimbursements. Include "
                            "monthly overhead, shipment exposure, and a "
                            "minimum cash floor before authorizing expansion."
                        ),
                        (
                            "A $25,000 startup allocation sits within the "
                            "$10,000–$55,000 range: $16,000 supports two $8,000 "
                            "unsettled lots, $4,500 covers one illustrative Base "
                            "overhead month, and $4,500 remains a contingency "
                            "floor. Maximum unsettled merchandise cost is $16,000; "
                            "available credit above that amount does not increase "
                            "the cash-supported purchasing limit."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three canonical profit bridges must reconcile exactly. "
                    "Every purchase must have dated, unrestricted repayment "
                    "resources; treasury allocations must exclude required reserves. "
                    "The delayed-ACH stress must show full statement repayment "
                    "without treating expected rewards or borrowed principal as cash profit."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": (
                    "End-to-End Execution, Idempotent Ledger "
                    "& QA Pre-Flight Sheet"
                ),
                "purpose": (
                    "Translate a qualified deal into a reproducible evidence "
                    "chain from commitment through cleared settlement. Define "
                    "stable identifiers, duplicate-resistant imports, parcel "
                    "custody records, and exception ownership. Make every ledger "
                    "balance traceable without relying on portal screenshots "
                    "or an operator's recollection."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create the deal record before any purchase. Attach "
                        "the commitment, approved economics, destination, payment "
                        "method, and quantity authorization. Generate separate "
                        "identifiers for orders, parcels, serial numbers, card "
                        "charges, rewards, and ACH settlements so partial outcomes "
                        "remain independently traceable."
                    ),
                    (
                        "Check product configuration, seller eligibility, shipping "
                        "coverage, and receiving deadlines immediately before "
                        "checkout. Save the applicable offer terms and order "
                        "confirmation. If the price or destination changes, "
                        "recalculate contribution rather than relying on the "
                        "earlier approval."
                    ),
                    (
                        "Import records through stable source identifiers and "
                        "transactional database writes. Replaying the same source "
                        "file must not create another purchase, reward, or "
                        "settlement. Corrections should reverse or supersede "
                        "earlier entries while preserving the original evidence "
                        "and operator identity."
                    ),
                    (
                        "Reconcile carrier delivery, warehouse acceptance, "
                        "reimbursement allocation, and bank clearance as "
                        "different states. A delivered parcel is not an "
                        "accepted lot, and an ACH notification is not "
                        "cleared cash available for repayment or treasury deployment."
                    ),
                    (
                        "Run a daily exception report covering missing serials, "
                        "partial acceptance, overdue reimbursement, reward reversals, "
                        "and statement exposure. Assign each exception an owner "
                        "and next action. Close the lot only after cash, "
                        "liabilities, and supporting records reconcile."
                    ),
                ],
                "fields": [
                    field(
                        "Deal identifier and evidence manifest",
                        "textarea",
                        (
                            "Define a stable deal identifier and list the "
                            "documents needed to reconstruct authorization. "
                            "Record document versions, capture dates, and "
                            "integrity checks so updated terms cannot silently "
                            "replace the originally approved basis."
                        ),
                        (
                            "Deal BG-2027-001 links commitment version 2, the "
                            "$8,000 purchase budget, a ten-unit SKU list, "
                            "shipping instructions, and the reward eligibility "
                            "capture. The manifest stores a SHA-256 digest "
                            "for each retained document. A later commitment "
                            "amendment receives version 3 and a new approval "
                            "record without replacing version 2."
                        ),
                    ),
                    field(
                        "Purchase release and price-change checks",
                        "textarea",
                        (
                            "Specify the checks performed immediately before "
                            "purchase, including price, quantity, destination, "
                            "available cash, issuer capacity, and delivery "
                            "window. Define the price or timing change "
                            "that requires a revised contribution calculation."
                        ),
                        (
                            "Checkout must show ten units at $800 each, "
                            "the verified warehouse destination, and delivery "
                            "inside the commitment window. A change to "
                            "$815 per unit raises merchandise cost by "
                            "$150 and reduces expected contribution to "
                            "$153 after the related 2% reward increase. "
                            "The operator recalculates and reauthorizes before ordering."
                        ),
                    ),
                    field(
                        "Idempotency key and duplicate handling",
                        "textarea",
                        (
                            "Define the unique key for each imported event "
                            "and explain how duplicate delivery, amended "
                            "records, and partial settlements are handled. "
                            "Avoid using amount and date alone because "
                            "legitimate transactions can share both."
                        ),
                        (
                            "The SQLite events table enforces uniqueness on "
                            "source_system, source_account, and source_event_id. "
                            "A repeated bank import with the same transaction "
                            "identifier inserts zero additional events. An "
                            "amended settlement creates a linked correction "
                            "event. Two separate $824 payments on one "
                            "date remain distinct because their bank identifiers differ."
                        ),
                    ),
                    field(
                        "Card liability and purchase ledger entries",
                        "textarea",
                        (
                            "Describe how merchandise purchases, statement "
                            "liabilities, repayments, and purchase-linked rewards "
                            "enter the ledger. Preserve the difference "
                            "between inventory acquisition and expense recognition "
                            "when merchandise has not yet transferred."
                        ),
                        (
                            "The $8,000 purchase debits inventory and credits "
                            "card payable. An $8,000 payment later debits "
                            "card payable and credits bank cash. Merchandise "
                            "cost moves from inventory when the accounting "
                            "policy requires recognition. A $160 purchase-linked "
                            "reward follows the documented cost-adjustment policy "
                            "rather than automatically becoming a second sales entry."
                        ),
                    ),
                    field(
                        "Parcel custody and insured value",
                        "textarea",
                        (
                            "Record package contents, serial numbers, parcel "
                            "weight, carrier service, coverage terms, and "
                            "handoff evidence. Distinguish declared value "
                            "from insurance coverage and identify the "
                            "party responsible for pursuing a loss claim."
                        ),
                        (
                            "Two parcels each contain five devices with "
                            "$4,000 documented merchandise cost. Packing "
                            "photos show serials, seals, and protective "
                            "materials; acceptance receipts record weight. "
                            "The operator verifies electronics coverage and "
                            "claim exclusions instead of equating a declared "
                            "value entry with insurance. The shipping contractor "
                            "opens any carrier claim within the policy deadline."
                        ),
                    ),
                    field(
                        "Warehouse acceptance and partial rejection",
                        "textarea",
                        (
                            "Define the transition from carrier delivery "
                            "to accepted merchandise and record partial "
                            "outcomes by serial number. Explain how "
                            "rejected items affect reimbursement, inventory "
                            "location, return authorization, and the original "
                            "commitment balance."
                        ),
                        (
                            "The warehouse accepts nine devices and disputes "
                            "one seal. Accepted reimbursement is 9 multiplied "
                            "by $824, or $7,416. The tenth device "
                            "remains separately tracked at $800 cost "
                            "pending photographs and disposition. The ledger "
                            "does not mark all ten accepted merely "
                            "because both parcels have carrier delivery confirmation."
                        ),
                    ),
                    field(
                        "ACH allocation and cleared-cash confirmation",
                        "textarea",
                        (
                            "Specify how incoming transfers are matched "
                            "to commitments and how clearance status "
                            "is established. Record partial payments, "
                            "unallocated cash, returned transfers, and "
                            "the difference between a payer notification "
                            "and bank evidence."
                        ),
                        (
                            "A buying group announces an $8,240 payout "
                            "on Monday, but the bank posts it "
                            "Wednesday. The reconciler retains the notice "
                            "as pending and uses bank evidence for "
                            "the cash entry. If the transfer includes "
                            "two lots, a remittance allocation must "
                            "sum to $8,240 before either receivable is closed."
                        ),
                    ),
                    field(
                        "Reward lifecycle and reversal treatment",
                        "textarea",
                        (
                            "Track eligible, pending, confirmed, paid, "
                            "and reversed rewards separately. Define "
                            "when each state affects planning contribution, "
                            "accounting entries, and cash availability, "
                            "including corrections caused by returns "
                            "or portal attribution disputes."
                        ),
                        (
                            "The $160 card reward remains expected "
                            "until the issuer confirms posting under "
                            "the program terms. The potential $80 "
                            "portal reward stays outside the base "
                            "case until eligibility is supported. If "
                            "one $800 unit is returned, the "
                            "expected 2% card reward falls by $16, "
                            "with the reversal linked to that unit."
                        ),
                    ),
                    field(
                        "QA invariants and reconciliation tolerances",
                        "textarea",
                        (
                            "List numerical and state-based assertions "
                            "that must hold before lot closure. "
                            "Set explicit rounding tolerances and "
                            "identify discrepancies that always require "
                            "investigation regardless of their apparent "
                            "dollar size or operational convenience."
                        ),
                        (
                            "The batch asserts ten unique serials, "
                            "$8,000 original merchandise cost, $8,240 "
                            "committed reimbursement, and settlement allocations "
                            "matching bank cash within $0.01. Duplicate "
                            "serials fail regardless of value. A "
                            "$0.50 unexplained difference is assigned "
                            "to an exception record rather than "
                            "silently written into shipping expense to balance the lot."
                        ),
                    ),
                    field(
                        "Exception queue and closeout evidence",
                        "textarea",
                        (
                            "Assign exception owners, deadlines, escalation "
                            "paths, and the evidence required for "
                            "closure. Separate operational completion "
                            "from unresolved claims so a successful "
                            "shipment cannot conceal an unpaid "
                            "receivable or unsupported reward."
                        ),
                        (
                            "Exception EX-017 records a missing $824 "
                            "reimbursement allocation, with the settlement "
                            "contractor responsible for obtaining remittance "
                            "detail within one business day. The "
                            "operator suspends new commitments if the "
                            "contractual due date passes. Closure requires "
                            "matched bank cash or an approved loss "
                            "entry, not an email promising eventual payment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Replay the import twice without changing balances. Confirm "
                    "all serials, charges, settlements, and reward adjustments "
                    "have stable identifiers and supporting evidence. No lot "
                    "may be marked settled while its bank allocation, card "
                    "liability, or material exception remains unresolved."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": (
                    "Statutory, Licensing, Contract Addendum "
                    "& Compliance Audit"
                ),
                "purpose": (
                    "Turn applicable statutes, commercial terms, and tax "
                    "recordkeeping duties into specific operating controls. "
                    "Verify the facts that determine resale treatment, "
                    "business-credit rules, inventory ownership, and reporting. "
                    "Preserve contract evidence and prevent purchasing volume "
                    "from exceeding authorized commercial activity."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Map requirements to the actual entity, transaction, "
                        "warehouse, and payment instrument. State the triggering "
                        "facts beside each citation. Do not treat a "
                        "warehouse state's tax structure as a substitute "
                        "for examining seller collection rules or your "
                        "own business obligations."
                    ),
                    (
                        "Maintain resale certificates, seller acceptance "
                        "records, invoices, and shipping evidence as "
                        "one transaction packet. Review changes in "
                        "business location or fulfillment routing before "
                        "reusing earlier tax assumptions. Investigate missing "
                        "tax documentation before increasing the purchasing "
                        "limit."
                    ),
                    (
                        "Read the current issuer, portal, and B2B "
                        "payment terms for the precise transaction "
                        "type. Document restricted categories and "
                        "recipient rules. Exclude fabricated purchases, "
                        "self-payments, prohibited consumer card cycling, "
                        "and any arrangement designed to conceal "
                        "the underlying commercial purpose."
                    ),
                    (
                        "Use a written addendum to allocate "
                        "inspection deadlines, title, transit risk, "
                        "return costs, and reimbursement timing. "
                        "Reference the governing state's enacted "
                        "UCC provisions where relevant. Keep "
                        "contractual remedies separate from assumptions "
                        "about how quickly disputes will resolve."
                    ),
                    (
                        "Reconcile information returns to transaction-level "
                        "records rather than treating reported "
                        "payment volume as taxable profit. "
                        "Preserve a documented policy for "
                        "purchase-price adjustments, inventory costs, "
                        "interest, and bonuses. Assign periodic "
                        "review responsibility and track corrections "
                        "to completion."
                    ),
                ],
                "fields": [
                    field(
                        "Entity registration and operating-location requirements",
                        "textarea",
                        (
                            "Identify the operating entity, actual "
                            "business locations, warehouse relationship, "
                            "and registrations triggered by those "
                            "facts. Cite applicable provisions precisely "
                            "and distinguish using a third-party "
                            "warehouse from operating your own "
                            "facility."
                        ),
                        (
                            "For a planned Delaware operating location, "
                            "the checklist evaluates business licensing "
                            "under 30 Del. C. § 2301 "
                            "and records the activity classification. "
                            "Merely shipping to an independent "
                            "DE warehouse is evaluated separately. "
                            "The operator documents where purchasing, "
                            "inventory control, and employees actually "
                            "operate before concluding which registrations are required."
                        ),
                    ),
                    field(
                        "Resale certificate and destination-specific tax file",
                        "textarea",
                        (
                            "List the certificate jurisdiction, validity "
                            "conditions, seller acceptance, and "
                            "transaction evidence. Explain how "
                            "the actual sale qualifies for "
                            "recorded treatment and how incorrect "
                            "collection or certificate rejection "
                            "will be corrected."
                        ),
                        (
                            "For a California transaction using "
                            "resale treatment, the file evaluates "
                            "Cal. Rev. & Tax. Code "
                            "§§ 6091–6092 and Cal. Code "
                            "Regs., tit. 18, § 1668. "
                            "The invoice, accepted certificate, "
                            "and purchase-for-resale facts remain "
                            "linked. A separate shipment to "
                            "NH or OR receives its own sourcing analysis."
                        ),
                    ),
                    field(
                        "Business credit agreement and permitted usage",
                        "textarea",
                        (
                            "Record the card's business purpose, "
                            "issuer restrictions, repayment terms, "
                            "and transaction classifications. Explain "
                            "which contractual protections apply "
                            "and why consumer-credit assumptions "
                            "cannot be imported automatically "
                            "into a commercial arrangement."
                        ),
                        (
                            "The card funds documented business "
                            "inventory only. The review records "
                            "the business-purpose exemption in "
                            "15 U.S.C. § 1603(1) and "
                            "12 CFR § 1026.3(a), while "
                            "checking applicable exceptions and "
                            "the issuer agreement itself. "
                            "Repayment planning uses the actual "
                            "commercial contract, not assumed consumer billing protections."
                        ),
                    ),
                    field(
                        "Payment platform and reward program restrictions",
                        "textarea",
                        (
                            "Document permitted invoice categories, "
                            "recipient relationships, card network "
                            "rules, reward exclusions, and "
                            "verification requirements. Explain "
                            "how the operator establishes "
                            "a genuine commercial obligation "
                            "before using a payment platform."
                        ),
                        (
                            "A proposed Melio or Plastiq "
                            "payment must match a genuine "
                            "$10,000 supplier invoice and "
                            "an allowed recipient category "
                            "under current terms. The "
                            "operator retains the quote "
                            "and checks issuer treatment. "
                            "Payments to controlled accounts "
                            "solely to generate rewards are excluded from this operating model."
                        ),
                    ),
                    field(
                        "Title and transit-risk addendum",
                        "textarea",
                        (
                            "Draft the commercial allocation "
                            "of title, transit risk, "
                            "insurance responsibility, and loss "
                            "claims. Identify the governing "
                            "state and distinguish contract "
                            "language from default rules "
                            "that apply only when "
                            "the agreement leaves a gap."
                        ),
                        (
                            "Proposed clause: Title transfers "
                            "upon documented warehouse acceptance; "
                            "seller bears transit loss "
                            "until that event and "
                            "maintains the specified shipment "
                            "coverage. The contract separately "
                            "allocates risk rather than "
                            "assuming title determines it. "
                            "Review references include the governing state's versions of UCC "
                            "§§ 2-401 and 2-509."
                        ),
                    ),
                    field(
                        "Inspection, rejection, and return-cost addendum",
                        "textarea",
                        (
                            "Specify inspection timing, acceptable "
                            "defect evidence, rejection notice, "
                            "return authorization, and shipping "
                            "cost allocation. Address partial "
                            "acceptance so one disputed "
                            "unit cannot automatically suspend "
                            "payment for every accepted "
                            "unit in the commitment."
                        ),
                        (
                            "Proposed clause: Buyer reports "
                            "SKU, quantity, or seal "
                            "exceptions with serial-specific "
                            "photographs within two business "
                            "days after delivery. Undisputed "
                            "accepted units remain payable "
                            "on schedule. Return costs "
                            "follow documented fault. The "
                            "review checks the governing state's UCC §§ 2-601, 2-602, and 2-606."
                        ),
                    ),
                    field(
                        "Settlement clock and overdue-payment remedies",
                        "textarea",
                        (
                            "Define the event starting "
                            "the payment clock, the "
                            "business-day convention, bank "
                            "holiday treatment, remittance "
                            "detail, and escalation steps. "
                            "Specify suspension rights "
                            "without assuming contractual "
                            "remedies create immediate liquidity."
                        ),
                        (
                            "Proposed Net-5 language starts "
                            "the five-business-day clock "
                            "at documented acceptance and "
                            "requires serial-level remittance "
                            "detail. If Monday acceptance "
                            "is followed by no "
                            "holidays, the fifth subsequent "
                            "business day is the "
                            "following Monday. Overdue payment suspends new commitments; "
                            "the card reserve remains necessary throughout any dispute."
                        ),
                    ),
                    field(
                        "Information-return and inventory-basis reconciliation",
                        "textarea",
                        (
                            "Describe how payment reporting, "
                            "gross receipts, refunds, inventory "
                            "cost, and purchase-price "
                            "adjustments reconcile. Cite "
                            "the governing federal "
                            "framework without assuming "
                            "a reporting form determines "
                            "the final taxable amount."
                        ),
                        (
                            "The annual file reconciles "
                            "any Form 1099-K amounts "
                            "under IRC § 6050W "
                            "to transaction records, "
                            "returns, and duplicate "
                            "reporting. Inventory and "
                            "basis policies reference "
                            "IRC §§ 471 and "
                            "1012 as applicable. A $160 purchase-linked rebate "
                            "is evaluated as a cost adjustment, not automatically as unrelated revenue."
                        ),
                    ),
                    field(
                        "Treasury income, bonuses, and bank identity records",
                        "textarea",
                        (
                            "Record account ownership, bank "
                            "identity documentation, interest "
                            "classification, bonus conditions, "
                            "and tax support. Distinguish "
                            "deposit yield from Treasury "
                            "interest and verify state "
                            "treatment using the "
                            "actual instrument held."
                        ),
                        (
                            "The bank file retains "
                            "entity identification requested "
                            "under the bank's customer "
                            "identification procedures, addressed "
                            "in 31 CFR § "
                            "1020.220. Interest and "
                            "bonus treatment are reviewed "
                            "under IRC § 61. "
                            "Direct Treasury obligations receive a separate state-tax review "
                            "under 31 U.S.C. § 3124; bank interest is not relabeled Treasury income."
                        ),
                    ),
                    field(
                        "Audit cadence and evidence remediation",
                        "textarea",
                        (
                            "Assign review owners, "
                            "document-expiry checks, "
                            "sample sizes, and "
                            "correction deadlines. "
                            "Specify which defects "
                            "stop purchasing and "
                            "which permit existing "
                            "lots to settle "
                            "while remediation proceeds."
                        ),
                        (
                            "Each month the operator "
                            "samples five lots and "
                            "checks certificates, commitments, "
                            "shipping coverage, reward "
                            "terms, and bank matches. "
                            "An expired required certificate "
                            "stops affected purchases "
                            "immediately. A missing "
                            "internal annotation receives a two-business-day correction deadline "
                            "while already authorized shipments continue under their verified terms."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Required registrations and transaction-specific tax evidence "
                    "must be current. Contract terms must address acceptance, "
                    "title, transit risk, payment timing, and returns. Every "
                    "payment route must represent permitted business activity, "
                    "with an assigned owner for accounting and tax reconciliation."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": (
                    "Automation Pipeline, Acquisition Flywheel "
                    "& Risk Fallback Tracker"
                ),
                "purpose": (
                    "Automate evidence collection, spread calculations, and "
                    "exception routing without automating unsupported assumptions. "
                    "Build a repeatable supply and counterparty development "
                    "process around measured settlement quality. Preserve "
                    "manual operation, cash access, and repayment discipline "
                    "when integrations, issuers, portals, or carriers fail."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Map each input to an authorized source "
                        "and an accountable owner. Prefer documented "
                        "exports and permitted interfaces over fragile "
                        "browser behavior. Store source timestamps "
                        "and evidence versions so automation can "
                        "explain exactly which terms produced "
                        "each decision."
                    ),
                    (
                        "Implement reward routing as a constrained "
                        "comparison, not an automatic highest-rate "
                        "selector. Filter by resale eligibility, "
                        "transaction category, caps, payment compatibility, "
                        "and portal attribution. Treat missing "
                        "evidence as zero eligible reward "
                        "until the relevant condition "
                        "is resolved."
                    ),
                    (
                        "Separate calculations from money movement. "
                        "The system may propose purchasing "
                        "limits, reserve allocations, or "
                        "treasury transfers, but execution "
                        "must use explicitly authorized "
                        "accounts and permissions. Retain "
                        "an audit trail of "
                        "the approving operator and "
                        "final bank confirmation."
                    ),
                    (
                        "Develop counterparties through small "
                        "paid pilots, measured acceptance "
                        "quality, and documented settlement "
                        "performance. Increase allocation only "
                        "after repeated reconciled outcomes. "
                        "Use operational reliability and "
                        "specific product availability as "
                        "the acquisition message rather "
                        "than unsupported return claims."
                    ),
                    (
                        "Test recovery from duplicate "
                        "imports, unavailable portals, "
                        "issuer suspension, and "
                        "delayed ACH before "
                        "increasing volume. Keep "
                        "a manual payment "
                        "calendar and readable "
                        "ledger export. A "
                        "failed integration must reduce activity rather than hide liabilities."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized source and ingestion register",
                        "textarea",
                        (
                            "List each data source, "
                            "authorized access method, "
                            "refresh interval, schema "
                            "owner, and fallback. "
                            "Identify sensitive fields "
                            "that should be "
                            "excluded from exports "
                            "or masked before "
                            "contractors receive access."
                        ),
                        (
                            "The pipeline ingests operator-authorized "
                            "card CSV exports daily, "
                            "bank transaction exports each "
                            "morning, and commitment files "
                            "when received. Full card "
                            "numbers are excluded; an "
                            "internal account alias links "
                            "records. The settlement contractor "
                            "sees amounts and references but cannot initiate "
                            "payments or change bank destination details."
                        ),
                    ),
                    field(
                        "Deal-commit and tracking reconciler",
                        "textarea",
                        (
                            "Define the state machine "
                            "connecting commitment, purchase, "
                            "shipment, acceptance, reimbursement, "
                            "and closure. Specify "
                            "permitted transitions, "
                            "required evidence, and "
                            "the rule preventing "
                            "partial events from "
                            "closing an entire deal."
                        ),
                        (
                            "BG-2027-001 moves through "
                            "committed, purchased, shipped, "
                            "partially accepted, accepted, "
                            "partially paid, and "
                            "settled states. Nine "
                            "accepted serials cannot "
                            "produce the ten-unit "
                            "accepted state. The "
                            "reconciler computes outstanding cost and receivables "
                            "from unit records, while the operator resolves contradictory source evidence."
                        ),
                    ),
                    field(
                        "Reward-stack router and exclusion logic",
                        "textarea",
                        (
                            "Describe how the router "
                            "evaluates card offers "
                            "and one portal "
                            "without double counting. "
                            "Record evidence freshness, "
                            "caps, exclusions, and "
                            "the treatment of "
                            "an attractive rate "
                            "whose eligibility cannot be established."
                        ),
                        (
                            "The router compares a "
                            "supported 2% business "
                            "card reward with "
                            "a conditional 4% "
                            "offer and evaluates "
                            "Rakuten versus TopCashback "
                            "as mutually exclusive "
                            "portal paths. On "
                            "$8,000, it approves $160 card value. "
                            "The unsupported $320 card alternative and conditional $80 "
                            "portal value remain outside the executable recommendation."
                        ),
                    ),
                    field(
                        "Treasury scheduler and maturity constraints",
                        "textarea",
                        (
                            "Define the cash calculation "
                            "used before a "
                            "sweep, the minimum "
                            "repayment reserve, maturity "
                            "buffer, transfer timing, "
                            "and failure response. "
                            "Prevent projected ACH "
                            "receipts from becoming "
                            "deployable cash before clearance."
                        ),
                        (
                            "The scheduler starts with "
                            "cleared bank cash, "
                            "subtracts $8,000 card "
                            "repayment, $2,000 operating "
                            "reserve, and every "
                            "scheduled transfer. A "
                            "Treasury purchase is "
                            "proposed only if "
                            "maturity and cash availability precede the repayment buffer. "
                            "A maturity after February 22 cannot support the "
                            "illustrative February 25 card payment."
                        ),
                    ),
                    field(
                        "Counterparty acquisition and pilot sequence",
                        "textarea",
                        (
                            "Define the target counterparty "
                            "profile, outreach evidence, "
                            "pilot size, settlement "
                            "measurement, and expansion "
                            "criteria. Explain how "
                            "the operator evaluates "
                            "BuyForMeRetail, Pointsmaker, "
                            "or MaxOutDeals without "
                            "assuming identical commercial terms."
                        ),
                        (
                            "The operator requests current "
                            "onboarding requirements from "
                            "three candidate groups, "
                            "then selects one "
                            "documented $1,600 pilot. "
                            "Expansion requires three "
                            "fully reconciled lots, "
                            "no unresolved acceptance "
                            "disputes, and settlement within the written clock. "
                            "A different group starts its own pilot record; "
                            "the first group's performance does not transfer automatically."
                        ),
                    ),
                    field(
                        "Acquisition flywheel and referral discipline",
                        "textarea",
                        (
                            "Describe how reliable "
                            "fulfillment creates repeat "
                            "commitments and qualified "
                            "introductions. Track the "
                            "source, cost, and "
                            "outcome of each "
                            "relationship, and disclose "
                            "material referral relationships "
                            "when making promotional recommendations."
                        ),
                        (
                            "After three clean lots, "
                            "the operator sends "
                            "a concise capacity "
                            "report showing available "
                            "SKUs, serial accuracy, "
                            "and on-time delivery. "
                            "A resulting introduction "
                            "is tagged to "
                            "that report. If a public recommendation carries "
                            "a referral payment, the operator uses a clear "
                            "material-connection disclosure consistent with 16 CFR Part 255."
                        ),
                    ),
                    field(
                        "Issuer review or shutdown fallback",
                        "textarea",
                        (
                            "Specify the response "
                            "to an issuer "
                            "information request, reduced "
                            "limit, suspended account, "
                            "or terminated reward "
                            "program. Preserve repayment "
                            "and truthful documentation "
                            "without disguising transactions "
                            "or circumventing account restrictions."
                        ),
                        (
                            "An issuer suspension freezes "
                            "new card purchases "
                            "immediately. The operator "
                            "provides requested business "
                            "invoices and inventory "
                            "records through the "
                            "issuer's verified channel. "
                            "Existing liabilities remain "
                            "scheduled for cash repayment. Another authorized business "
                            "card is considered only under its own terms "
                            "and cash-supported limit, never as a concealment tactic."
                        ),
                    ),
                    field(
                        "Carrier loss and disputed-acceptance fallback",
                        "textarea",
                        (
                            "Record the response "
                            "to a missing "
                            "parcel or warehouse "
                            "dispute, including claim "
                            "evidence, cash exposure, "
                            "replacement authority, and "
                            "purchasing restrictions. "
                            "Separate expected recovery "
                            "from money currently available."
                        ),
                        (
                            "If one five-device parcel "
                            "is lost, $4,000 "
                            "of merchandise cost "
                            "is exposed. The "
                            "shipping contractor gathers "
                            "receipts, serials, photographs, "
                            "and coverage documents. "
                            "The ledger records "
                            "the claim separately and reserves zero immediate "
                            "recovery cash. Replacement purchases require additional capacity; "
                            "the original card liability remains due in full."
                        ),
                    ),
                    field(
                        "Alert thresholds and operator response",
                        "textarea",
                        (
                            "Define actionable thresholds "
                            "for settlement aging, "
                            "reserve coverage, duplicate "
                            "records, reward reversals, "
                            "and missing documents. "
                            "Assign recipients and "
                            "response deadlines so "
                            "alerts produce specific "
                            "operating decisions rather than background noise."
                        ),
                        (
                            "The system raises an "
                            "urgent alert when "
                            "repayment reserve coverage "
                            "falls below 1.00, "
                            "a required commitment "
                            "is missing, or "
                            "a bank event "
                            "duplicates an existing "
                            "identifier with different data. The operator responds "
                            "the same business day. Overdue accepted receivables "
                            "automatically suspend further commitments to that group."
                        ),
                    ),
                    field(
                        "Recovery test and manual operating kit",
                        "textarea",
                        (
                            "Define the backup "
                            "frequency, restore test, "
                            "manual records, and "
                            "maximum acceptable outage. "
                            "Explain how the "
                            "team keeps repayment "
                            "dates visible when "
                            "the primary reconciler "
                            "or a source integration becomes unavailable."
                        ),
                        (
                            "A daily SQLite backup "
                            "and encrypted document "
                            "archive support recovery. "
                            "Every Friday, the "
                            "operator exports open "
                            "lots, card due "
                            "dates, reserves, and "
                            "overdue receivables into "
                            "a readable file. A monthly restore test "
                            "must reproduce balances. During an outage exceeding "
                            "one business day, purchasing pauses while manual settlement tracking continues."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The automation must explain every recommendation, reject "
                    "duplicate events, preserve source evidence, and leave "
                    "money movement under explicit authority. Demonstrate one "
                    "successful restore and one manual repayment-calendar drill "
                    "before increasing purchasing volume beyond the pilot limit."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": (
                    "30-Day Launch Sprint, Pod KPI Scorecard "
                    "& Exit-Readiness Ledger"
                ),
                "purpose": (
                    "Convert the operating design into a measured launch "
                    "with explicit cash limits, named responsibilities, and "
                    "repeatable reporting. Track the evidence required for "
                    "expansion or transfer of the business. Preserve the "
                    "canonical annual scenarios without presenting a "
                    "30-day pilot as established annual performance."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan the first 30 days around "
                        "verification, system preparation, and a "
                        "small authorized pilot if prerequisites "
                        "are ready. The supplied time "
                        "to first deal is one "
                        "to three months, so a "
                        "launch sprint may finish before "
                        "the first settled transaction."
                    ),
                    (
                        "Assign each operating responsibility "
                        "to the full-time operator "
                        "or a defined contractor "
                        "role. Keep purchasing authority, "
                        "bank access, evidence handling, "
                        "and reconciliation distinct. Measure "
                        "actual hours rather than "
                        "assuming automation eliminates exception "
                        "work or supervision."
                    ),
                    (
                        "Report gross scorecard activity, "
                        "retained contribution, owner profit, "
                        "cash reserves, and unsettled "
                        "liabilities separately. Compare actual "
                        "results with Conservative, Base, "
                        "and Scaled assumptions only "
                        "after matching their economic "
                        "definitions and avoiding duplicate "
                        "reward or reimbursement recognition."
                    ),
                    (
                        "Increase volume through demonstrated "
                        "settlement quality and cash "
                        "capacity, not available credit "
                        "alone. Require completed pilot "
                        "evidence, stable contribution, and "
                        "successful delayed-payment stress "
                        "before adding counterparties, "
                        "invoices, or treasury "
                        "allocations to the operating schedule."
                    ),
                    (
                        "Build transferability from the "
                        "start by documenting procedures, "
                        "account dependencies, contract rights, "
                        "and data ownership. Identify "
                        "relationships that require fresh "
                        "underwriting or consent after "
                        "a sale. Maintain a "
                        "clean evidence room without "
                        "assuming personal credit access transfers."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 foundation and capital allocation",
                        "textarea",
                        (
                            "List the first-week "
                            "deliverables, responsible person, "
                            "cash allocation, and "
                            "conditions that must "
                            "be satisfied before "
                            "ordering. Include entity "
                            "records, business banking, "
                            "repayment reserves, and "
                            "the initial ledger configuration."
                        ),
                        (
                            "By day 7, the "
                            "operator documents the "
                            "$25,000 startup allocation, "
                            "business bank ownership, "
                            "card terms, and "
                            "resale requirements. The "
                            "ledger contains test "
                            "events only. A "
                            "$1,600 pilot ceiling is proposed, but actual "
                            "purchasing remains conditional on a verified commitment "
                            "and shipping coverage rather than the calendar deadline."
                        ),
                    ),
                    field(
                        "Days 8–14 counterparties and dry-run evidence",
                        "textarea",
                        (
                            "Define the second-week "
                            "underwriting tasks, counterparties "
                            "contacted, documents requested, "
                            "and test results. "
                            "Include a complete "
                            "simulated lot that "
                            "demonstrates duplicate-resistant "
                            "imports and dated "
                            "repayment planning before cash is committed."
                        ),
                        (
                            "The operator requests current "
                            "terms from BuyForMeRetail, "
                            "Pointsmaker, and MaxOutDeals "
                            "through their verified "
                            "business channels. A "
                            "simulated two-unit lot "
                            "tests $1,600 cost, "
                            "$1,648 reimbursement, and "
                            "$32 supported card rewards. Import replay creates "
                            "no duplicate events, and the repayment reserve "
                            "remains sufficient even when simulated reimbursement is delayed."
                        ),
                    ),
                    field(
                        "Days 15–21 limited pilot and observation",
                        "textarea",
                        (
                            "Specify the permitted "
                            "pilot size, expected "
                            "unit economics, evidence "
                            "captured, and conditions "
                            "that postpone execution. "
                            "Avoid assuming small "
                            "shipments inherit the "
                            "same per-unit freight "
                            "cost as a larger production lot."
                        ),
                        (
                            "If prerequisites clear, two "
                            "devices cost $1,600 "
                            "and carry $1,648 "
                            "reimbursement. Supported card "
                            "rewards add $32; "
                            "actual pilot shipping "
                            "is budgeted at "
                            "$20 and expected "
                            "loss at $8. Expected contribution is $52, "
                            "excluding portal upside. If onboarding remains incomplete, "
                            "the week produces verified documentation instead of an unauthorized purchase."
                        ),
                    ),
                    field(
                        "Days 22–30 reconciliation and expansion decision",
                        "textarea",
                        (
                            "Define the final-week "
                            "review, remaining receivables, "
                            "reward status, cash "
                            "verification, and decision "
                            "criteria. Distinguish a "
                            "successful process rehearsal "
                            "from a fully "
                            "settled transaction and "
                            "from a repeatable operating record."
                        ),
                        (
                            "At day 30, the "
                            "operator reports whether "
                            "the pilot is "
                            "unstarted, in transit, "
                            "accepted, or settled, "
                            "with dated evidence "
                            "for its actual "
                            "state. A settled "
                            "pilot supports another small test, not immediate "
                            "Base-scale purchasing. Three clean lots and adequate "
                            "reserves are required before the counterparty limit increases."
                        ),
                    ),
                    field(
                        "Pod responsibilities and access separation",
                        "textarea",
                        (
                            "Assign purchasing, shipment "
                            "documentation, reconciliation, treasury "
                            "decisions, and exception "
                            "resolution to named "
                            "roles. Match the "
                            "canonical team configuration "
                            "and define which "
                            "permissions contractors do "
                            "not receive."
                        ),
                        (
                            "The Conservative and Base "
                            "pod uses one "
                            "full-time operator plus "
                            "two contractors. The "
                            "operator controls commitments "
                            "and banking; contractor "
                            "one manages shipment "
                            "evidence; contractor two "
                            "reconciles settlements with read-only access. Scaled operations "
                            "use two full-time operators plus three contractors, "
                            "with bank permissions assigned separately from data-processing duties."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and measured results",
                        "textarea",
                        (
                            "Define each KPI's "
                            "numerator, denominator, measurement "
                            "window, and source. "
                            "Include settlement timing, "
                            "contribution, reserve coverage, "
                            "exception aging, and "
                            "labor intensity without "
                            "substituting gross transaction "
                            "volume for operating quality."
                        ),
                        (
                            "A hypothetical ten-lot week "
                            "has $80,000 merchandise "
                            "cost and $82,400 "
                            "committed reimbursement. Supported "
                            "card rewards are "
                            "$1,600, shipping $600, "
                            "and expected losses "
                            "$400, yielding $3,000 "
                            "expected contribution before overhead. If eight lots "
                            "clear within their payment clock, on-time settlement "
                            "is 80%; unresolved lots remain in the denominator."
                        ),
                    ),
                    field(
                        "Canonical scorecard and scenario comparison",
                        "textarea",
                        (
                            "Record the canonical "
                            "ranking, score, scenario "
                            "profits, retained-revenue range, "
                            "and staffing assumptions. "
                            "Explain how actual "
                            "pilot results will "
                            "be compared without "
                            "altering the supplied "
                            "Formula v2.0 economic definitions."
                        ),
                        (
                            "Candidate #41 ranks #10 "
                            "of 43 with "
                            "93/100: revenue 23, "
                            "margin 24, team "
                            "20, accessibility 13, "
                            "automation 13. Canonical "
                            "owner profits are "
                            "$20,000, $143,500, and "
                            "$360,000. Retained revenue spans $87,500–$630,000, with "
                            "$358,750 Base retained revenue. The pilot is "
                            "compared through a separate bridge, not substituted for these annual scenarios."
                        ),
                    ),
                    field(
                        "Scale triggers and drawdown controls",
                        "textarea",
                        (
                            "Set measurable expansion "
                            "criteria and define "
                            "the operating response "
                            "to shrinking contribution, "
                            "payment delays, reserve "
                            "depletion, or concentration. "
                            "Show how reduced "
                            "purchase volume restores "
                            "cash safety before additional commitments are accepted."
                        ),
                        (
                            "A counterparty limit increases "
                            "from $1,600 to "
                            "$4,000 only after "
                            "three reconciled lots, "
                            "no overdue accepted "
                            "receivables, and full "
                            "repayment reserve coverage. "
                            "Two consecutive lots "
                            "below the approved contribution floor trigger repricing. "
                            "Any overdue payout freezes that group's new "
                            "commitments until cash clears and the delay is explained."
                        ),
                    ),
                    field(
                        "Exit-readiness evidence and transferable assets",
                        "textarea",
                        (
                            "Identify the records, "
                            "procedures, software, contracts, "
                            "and relationships a "
                            "successor could evaluate. "
                            "Document assignment restrictions, "
                            "account dependencies, and "
                            "fresh underwriting requirements "
                            "rather than assuming "
                            "all operating advantages transfer with ownership."
                        ),
                        (
                            "The evidence room contains "
                            "12 monthly reconciliations, "
                            "counterparty settlement histories, "
                            "source-controlled automation, shipment "
                            "claim records, and "
                            "signed commercial terms. "
                            "A transfer matrix "
                            "flags issuer accounts "
                            "and portal memberships for fresh review. Personal "
                            "guarantees and individual account access are not "
                            "priced as automatically transferable assets; assignment rights are documented contract by contract."
                        ),
                    ),
                    field(
                        "Owner decision log and next operating milestone",
                        "textarea",
                        (
                            "State the completed "
                            "evidence, remaining limitations, "
                            "next authorized action, "
                            "cash ceiling, and "
                            "review date. Record "
                            "why the decision "
                            "follows observed results "
                            "rather than desired "
                            "annual profit or unused credit capacity."
                        ),
                        (
                            "Day-30 decision: documentation and "
                            "duplicate-import testing are "
                            "complete; one $1,600 "
                            "pilot is accepted "
                            "but not yet "
                            "paid. The next "
                            "action is settlement "
                            "verification, not expansion. "
                            "The cash-supported ceiling remains unchanged. The operator "
                            "reviews again after cleared reimbursement and updates "
                            "contribution when actual shipping, rewards, and any losses are known."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Close the sprint with a dated evidence-backed status, "
                    "reconciled cash and liabilities, assigned pod responsibilities, "
                    "and an explicit next purchasing limit. Preserve the "
                    "one-to-three-month first-deal expectation when onboarding "
                    "takes longer; claim repeatability only after multiple "
                    "fully reconciled operating cycles."
                ),
            },
        ],
    }
