from __future__ import annotations

CHAPTER_2 = {
    "id": "Q2",
    "chapter_id": "Q2",
    "chapter_number": 2,
    "question_number": 2,
    "slug": "medical-equipment-resale-buyers-payment-rails-and-fee-protection",
    "question_prompt": "Who writes the check in medical equipment resale, what acute financial or statutory pain forces them to pay, and how do funds clear cleanly without circumvention or non-payment?",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & How the Payment Rail Works",
    "subtitle": "Hospital Treasury, Practice Owners, Serial-Level Escrow, UCC Title Controls & Chapter 11 Trade-Claim Distributions",
    "layout_template": "executive_summary",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #14, Medical Equipment Resale, ranks #20 with a Money-to-Manpower "
        "Score of 85/100. Buyers pay to restore clinical capacity, preserve capital, "
        "or replace equipment whose service economics have deteriorated. This chapter "
        "maps three plays: replacement-capacity resale, documented refurbishment with "
        "milestone settlement, and "
        "chapter11_trade_claim_convenience_class_rollup, an adjacent claim-investing "
        "strategy kept outside equipment revenue. The canonical annual owner profits "
        "are $25,000 Conservative, $164,000 Base, and $396,000 Scaled. Gross equipment "
        "proceeds, rather than financing principal or claim face value, drive those "
        "cases. Identify the actual budget holder, validate title and serviceability, "
        "bind acceptance to observable tests, and route funds through independently "
        "verified instructions. A clinician's enthusiasm cannot replace treasury "
        "authority, collectibility, or a serial-specific release condition."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$250,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "10% net margin; $25,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$1,025,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "16.0% net margin; $164,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$1,800,000",
            "context": "Annual gross equipment resale proceeds; acquisition and refurbishment included in margin",
            "note": "22% net margin; $396,000 annual owner net profit; 1 FT + 3 C, eight people total",
        },
    ],
    "sections": [
        {
            "heading": "1. Sell the Budget Holder a Recoverable Operating Outcome",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The person who wants the machine rarely controls every condition "
                    "needed to buy it. In a hospital, a department director establishes "
                    "clinical need, biomedical engineering evaluates supportability, "
                    "supply chain creates the purchase order, and treasury or accounts "
                    "payable releases funds. An ambulatory surgery center may compress "
                    "those roles into an administrator and physician owner, while a "
                    "veterinary practice often relies on an owner and equipment lender. "
                    "Build a buyer map before negotiating price: legal purchasing entity, "
                    "authorized signer, budget source, purchase-order threshold, delivery "
                    "site, acceptance signer, and payment-release owner. Ask what happens "
                    "if the current device remains unavailable for thirty days, then "
                    "separate lost appointments from genuinely recoverable contribution. "
                    "A scheduled procedure is not automatically collectible revenue. "
                    "Verify whether the purchase replaces an existing asset, adds a "
                    "service line, or consumes an already approved capital allocation. "
                    "Request the procurement checklist and vendor-onboarding timetable "
                    "before reserving stock. A signed quotation from a clinician without "
                    "purchasing authority creates inventory exposure, not an enforceable "
                    "treasury commitment. Record each decision maker's specific objection "
                    "and required evidence in HubSpot or Salesforce, attached to the "
                    "serial-number opportunity rather than a generic account note."
                ),
                (
                    "The first chapter-level operating play, replacement-capacity resale, "
                    "monetizes speed without pretending every outage creates unlimited "
                    "pricing power. Suppose an ultrasound outage displaces twelve "
                    "appointments weekly, each yielding $180 of contribution after "
                    "incremental clinical costs. Four weeks represent $8,640 of potential "
                    "contribution exposure, but only if staffing, referrals, collections, "
                    "and patient demand support those appointments. A refurbished unit "
                    "priced at $25,000 can therefore compete on delivery certainty and "
                    "service continuity rather than a dramatic discount against an "
                    "irrelevant new-system list price. Obtain the buyer's probe, software, "
                    "network, and room requirements before promising a replacement. "
                    "Confirm whether existing service coverage transfers and whether "
                    "the manufacturer will support the configuration. If compatibility "
                    "fails, the fallback is a separately contracted rental, another "
                    "documented configuration, or a canceled reservation under agreed "
                    "terms; it is never an improvised clinical substitution. Aesthetic "
                    "buyers may instead value predictable treatment capacity, while "
                    "veterinary buyers may prioritize parts availability and technician "
                    "access. Do not present human-device regulatory requirements as "
                    "identical for veterinary-only equipment. In every segment, sell "
                    "a supported operating outcome with measurable delivery conditions, "
                    "not a vague promise that the purchase pays for itself."
                ),
                (
                    "The second operating play, documented refurbishment with milestone "
                    "settlement, turns uncertain condition into evidence a budget holder "
                    "can defend. For an illustrative $40,000 surgical-equipment sale, "
                    "use a $4,000 reservation deposit, $32,000 released after specified "
                    "bench tests and shipment authorization, and $4,000 following "
                    "installation acceptance. These amounts total the equipment price; "
                    "they are not three separate revenue streams. Before accepting "
                    "the deposit, disclose included accessories, excluded consumables, "
                    "software-license transfer conditions, warranty scope, and the "
                    "identity of the servicing organization. The buyer pays for fewer "
                    "surprises, traceable testing, and a bounded remedy if performance "
                    "misses the agreed specification. Establish an acceptance period "
                    "long enough to perform the tests, but do not allow an unrelated "
                    "construction delay to suspend all payment indefinitely. For a "
                    "financed purchase, obtain the lender's actual funding conditions: "
                    "some lenders require delivery confirmation and a signed acceptance "
                    "certificate before paying the seller. If those conditions leave "
                    "the operator financing the entire shipment, require funded escrow "
                    "or revise the delivery sequence. The fallback for unresolved "
                    "performance is repair, replacement, or return under a priced "
                    "remedy schedule, with transport responsibility and refund timing "
                    "written before the device leaves the warehouse."
                ),
            ],
            "table": {
                "caption": "Six Buyer Archetypes: Economic Pain, Actual Authority, and Release Evidence",
                "headers": [
                    "Buyer and operating use",
                    "Acute reason to spend",
                    "Who controls the actual funds",
                    "Evidence that unlocks the payment",
                ],
                "rows": [
                    [
                        "Hospital imaging department replacing an unsupported diagnostic system",
                        "Canceled examinations consume contribution while existing service coverage expires",
                        "Capital committee authorizes expenditure and treasury executes approved disbursement",
                        "Purchase order, biomed acceptance, vendor onboarding, and matched invoice",
                    ],
                    [
                        "Ambulatory surgery center replacing a failed surgical equipment stack",
                        "Operating room cancellations disrupt schedules and contracted physician availability",
                        "Administrator commits budget within limits and ownership authorizes exceptions",
                        "Serial-specific configuration, electrical testing, installation record, and acceptance signature",
                    ],
                    [
                        "Independent veterinary practice adding an affordable diagnostic imaging capability",
                        "Outside referrals surrender contribution and delay treatment decisions locally",
                        "Practice owner signs purchase while lender controls financed disbursement",
                        "Veterinary suitability, service access, delivered accessories, and lender acceptance",
                    ],
                    [
                        "Aesthetic practice replacing an aging energy-based treatment platform",
                        "Unreliable sessions strand booked appointments and increase maintenance expense",
                        "Practice owner or controller releases documented equipment acquisition funds",
                        "Correct handpieces, support availability, license rights, and functional testing",
                    ],
                    [
                        "Regional equipment dealer purchasing stock for a named downstream buyer",
                        "Unavailable inventory threatens an existing sale with defined delivery",
                        "Dealer principal approves purchase and controller executes supplier payment",
                        "Verified buyer entity, resale documentation, serial list, and cleared funds",
                    ],
                    [
                        "Equipment lessor funding a practice's approved capital asset purchase",
                        "Incomplete acceptance documentation prevents commencement of the lease transaction",
                        "Lessor funding desk releases principal after contractual conditions resolve",
                        "Executed lease, delivery certificate, lien arrangements, and authentic acceptance",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Sell the Acceptance Packet Before Selling the Machine",
                "body": (
                    "Experienced buyers reward evidence that survives purchasing, "
                    "biomed, and treasury review without repeated clarification."
                ),
                "items": [
                    "Ask the buyer's biomed team for its incoming inspection checklist before commissioning refurbishment work.",
                    "Quote the exact probes, handpieces, software options, and accessory serials; a model name alone leaves expensive configuration disputes.",
                    "Confirm lender funding conditions directly with the independently verified funding desk before signing freight instructions.",
                    "Show the buyer a redacted sample acceptance packet containing measured results, technician identity, decontamination evidence, and service exclusions.",
                ],
            },
        },
        {
            "heading": "2. Choose the Settlement Mechanism Before Committing Inventory",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "A payment method and a release condition solve different problems. "
                    "Wire and ACH move money; escrow governs custody and release; "
                    "milestone holds allocate performance risk; factoring monetizes a "
                    "receivable. Compare all eight arrangements in the matrix rather "
                    "than treating them as interchangeable bank products. For a "
                    "$25,000 diagnostic sale, an illustrative $5,000 deposit plus "
                    "$20,000 before dispatch minimizes seller credit exposure but "
                    "requires sufficient buyer confidence. A buyer requesting payment "
                    "thirty days after installation is asking for unsecured credit "
                    "unless collateral or a separate structure changes that exposure. "
                    "Verify receipts through the receiving bank's authenticated channel, "
                    "not a screenshot, emailed remittance, or shipping agent's assurance. "
                    "Check the purchasing entity against the originating account and "
                    "document legitimate differences, including lender-funded purchases. "
                    "A wire is generally difficult to reverse once completed, but "
                    "fraud recovery processes and legal claims still exist. ACH "
                    "availability does not remove return or unauthorized-payment risk. "
                    "Set release rules with the bank for the actual transaction "
                    "type and risk profile. Do not copy consumer return periods "
                    "into commercial-credit procedures or assume one waiting period "
                    "eliminates every payment dispute. Treasury evidence must match "
                    "the sale, amount, currency, and authorized payer."
                ),
                (
                    "Escrow works only when the agreement specifies what evidence "
                    "causes money to move. Name the custody provider, verify its "
                    "identity and applicable authority, identify fees, and define "
                    "dispute handling before funding. For the $40,000 milestone "
                    "example, a buyer might fund the full price into escrow, "
                    "with releases of $4,000, $32,000, and $4,000 under the "
                    "written sequence. The buyer's funding confirmation is distinct "
                    "from the operator receiving released cash. Attach the serial "
                    "schedule and objective tests so the provider does not need "
                    "to judge whether a surgeon merely likes the device. Specify "
                    "what happens if the buyer refuses inspection, the carrier "
                    "damages the shipment, or a required software entitlement "
                    "cannot transfer. A marketplace checkout through a provider "
                    "such as Stripe or PayPal may offer convenient collection, "
                    "but payout timing, reserves, prohibited categories, and dispute "
                    "rights must fit the equipment transaction. Never bypass a "
                    "marketplace's contractual fee rules by moving its introduced "
                    "buyer off-platform. A reservation retainer also needs explicit "
                    "earned, refundable, and creditable portions. Calling a payment "
                    "nonrefundable does not itself resolve defective performance "
                    "or conflicting contract provisions. Reconcile escrow balances "
                    "separately from cash available to purchase the next unit."
                ),
                (
                    "Factoring becomes relevant only after examining whether a "
                    "collectible, assignable receivable actually exists. On an "
                    "illustrative accepted $100,000 invoice, an 80% advance "
                    "provides $80,000 initially; a hypothetical $3,000 total fee "
                    "leaves $17,000 released from the reserve after full customer "
                    "payment. Net proceeds are $97,000, before other transaction "
                    "costs, rather than $180,000 of revenue. Confirm recourse, "
                    "dilution adjustments, customer notification, anti-assignment "
                    "terms, and existing lender liens. Factor quotes can become "
                    "uneconomic when installation disputes delay payment. A "
                    "statutory disbursement is fundamentally different: a bankruptcy "
                    "distribution follows court and plan mechanics, not the seller's "
                    "preferred settlement schedule. Keep that rail confined to the "
                    "claim-investing play described later. Operationally, require "
                    "two-person verification for bank-detail changes, with a "
                    "callback to a previously authenticated number. A new email "
                    "signature or urgent closing deadline is insufficient evidence. "
                    "Maintain an invoice-to-bank reconciliation showing deposit, "
                    "remaining balance, taxes collected, freight charges, credits, "
                    "and retained amounts. When a buyer demands an unexplained "
                    "third-party refund, stop the refund workflow and investigate "
                    "through established contacts. Do not turn an equipment "
                    "transaction into a pass-through transfer for unrelated parties."
                ),
            ],
            "table": {
                "caption": "Eight Payment and Settlement Arrangements Compared at the Release Decision",
                "headers": [
                    "Arrangement and appropriate transaction",
                    "Who authorizes movement or release",
                    "Primary failure mode to price",
                    "Required operating control before release",
                ],
                "rows": [
                    [
                        "Bank wire for an identified purchaser's equipment balance",
                        "Authorized payer instructs its bank using independently verified details",
                        "Spoofed instructions redirect funds despite an authentic equipment transaction",
                        "Confirm receipt through bank access and authenticate every changed instruction",
                    ],
                    [
                        "Independent escrow for equipment requiring staged acceptance evidence",
                        "Escrow provider follows executed instructions and documented release conditions",
                        "Ambiguous tests trap funds while parties dispute subjective performance",
                        "Attach serials, test thresholds, inspection deadlines, and dispute procedures",
                    ],
                    [
                        "Commercial ACH for established buyers with approved credit exposure",
                        "Authorized account holder initiates credit or authorizes permitted debit",
                        "Returns or authorization disputes emerge after apparent funds availability",
                        "Set bank-specific release procedures and exposure limits by transaction type",
                    ],
                    [
                        "Reservation retainer for time-limited allocation of identified equipment",
                        "Buyer authorizes payment under explicit reservation and refund terms",
                        "Seller treats refundable money as unrestricted earned operating income",
                        "Define reservation expiry, credit application, refund triggers, and bookkeeping",
                    ],
                    [
                        "Statutory disbursement for an acquired allowed bankruptcy trade claim",
                        "Plan administrator distributes according to confirmed plan and court orders",
                        "Objection, reserve, transfer delay, or plan restriction reduces recovery",
                        "Verify claim status, transfer record, distribution address, and actual entitlement",
                    ],
                    [
                        "Platform checkout for equipment allowed by the marketplace contract",
                        "Platform processor releases payouts under account and transaction rules",
                        "Chargebacks, reserves, or category restrictions interrupt expected seller liquidity",
                        "Review equipment eligibility, payout terms, evidence requirements, and fee obligations",
                    ],
                    [
                        "Factoring an accepted invoice from a creditworthy equipment purchaser",
                        "Factor advances against eligibility and collects the assigned receivable",
                        "Recourse and performance disputes return collection exposure to the seller",
                        "Validate acceptance, assignment rights, liens, reserves, and effective financing cost",
                    ],
                    [
                        "Milestone holds for bench testing, delivery, and installation acceptance",
                        "Named buyer representative or custodian certifies contractual milestone evidence",
                        "Buyer delays inspection and withholds funds beyond the planned cycle",
                        "Use measurable tests, bounded holds, cure periods, and escalation deadlines",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Authenticate the payer and authority",
                    "action": "Match the contract entity, signer, purchase order, and funding source.",
                    "detail": "Verify lender involvement directly and record who can authorize escrow release or invoice payment.",
                },
                {
                    "step": 2,
                    "title": "Lock the acceptance and settlement schedule",
                    "action": "Attach the serial schedule, test criteria, payment amounts, and release evidence.",
                    "detail": "Specify tax treatment, freight responsibility, inspection deadlines, cure rights, and refund routing.",
                },
                {
                    "step": 3,
                    "title": "Verify money before relinquishing control",
                    "action": "Confirm bank receipt or authenticated escrow funding through independent channels.",
                    "detail": "Apply the agreed rail-specific release rule and obtain two-person review of changed banking details.",
                },
                {
                    "step": 4,
                    "title": "Close the evidence and cash loop",
                    "action": "Reconcile delivery, acceptance, funds, fees, taxes, credits, and remaining holds.",
                    "detail": "Keep the complete packet under the equipment serial and pursue exceptions before extending additional credit.",
                },
            ],
        },
        {
            "heading": "3. Protect the Spread with Credit, Title, and Device Evidence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Counterparty screening should answer whether this entity can "
                    "pay this invoice on these terms. Verify formation and "
                    "standing through the relevant secretary of state, corroborate "
                    "the operating address, obtain trade references independently, "
                    "and examine a commercial credit report where available. "
                    "For meaningful unsecured exposure, request recent statements, "
                    "accounts-payable aging, existing lender restrictions, and the "
                    "source of repayment. PACER litigation and bankruptcy searches "
                    "can reveal context, but a matching name alone proves "
                    "nothing; resolve entity identifiers. Establish a credit "
                    "limit against aggregate exposure, including devices already "
                    "shipped and unresolved acceptance holds. A buyer offering "
                    "a large order while refusing basic identity verification "
                    "deserves smaller exposure, not a larger discount. On the "
                    "supply side, check ownership, lease status, and security "
                    "interests before acquiring equipment. UCC search results "
                    "require interpretation by debtor name, jurisdiction, and "
                    "collateral description; possession is not proof of clean "
                    "title. UCC section 9-315 generally preserves a security "
                    "interest after disposition unless an applicable rule or "
                    "authorization changes that result. Obtain authenticated "
                    "payoff and release instructions when needed. A low "
                    "purchase price cannot compensate for inventory that "
                    "belongs to a lessor or remains encumbered."
                ),
                (
                    "Device evidence protects payment because condition disputes "
                    "often become collection disputes. Index service history, "
                    "serial photographs, recalls, maintenance intervals, accessories, "
                    "and measured acceptance results in the inventory record. "
                    "Distinguish servicing that restores intended performance "
                    "from changes that can constitute remanufacturing; significant "
                    "changes to safety, performance specifications, or intended "
                    "use require device-specific regulatory analysis before "
                    "marketing. Applicable manufacturer obligations can include "
                    "registration, listing, and the Quality Management System "
                    "Regulation in 21 CFR Part 820. Do not assume every "
                    "reseller is a manufacturer, or that describing work "
                    "as refurbishment settles the classification. For patient "
                    "data, identify whether HIPAA applies to the parties "
                    "and services, establish any required business-associate "
                    "arrangement, and use an approved sanitization process "
                    "that preserves lawful device operation. HHS requires "
                    "covered entities and relevant business associates to "
                    "address device and media controls under 45 CFR "
                    "164.310(d). A factory reset is not automatically "
                    "verified data removal. Record the method, affected "
                    "media, verification result, and technician. Obtain "
                    "decontamination evidence suitable for the device and "
                    "handling task; dirty equipment should not travel "
                    "through ordinary receiving workflows while staff "
                    "debate who was supposed to clean it."
                ),
                (
                    "Fee protection starts by deciding whether the operator "
                    "is principal, broker, or service provider. The canonical "
                    "model assumes equipment resale as principal: the "
                    "operator buys inventory and recognizes gross resale "
                    "proceeds, with acquisition and refurbishment embedded "
                    "in margin. A disclosed broker earning $2,000 on "
                    "another party's $40,000 sale has a different revenue "
                    "basis and must not report the entire sale as "
                    "its fee. For brokerage work, define protected "
                    "introductions, transaction scope, fee trigger, payment "
                    "timing, exclusions for existing relationships, and "
                    "a reasonable duration in the signed engagement. "
                    "Use dated introduction records and a closing "
                    "statement rather than hiding seller identity until "
                    "the last minute. For principal sales, protect "
                    "the spread through enforceable price, substitution, "
                    "acceptance, warranty, and default terms. Do not "
                    "confuse a security-interest clause with completed "
                    "perfection or priority. UCC section 2-401 generally "
                    "limits retained title in delivered goods to a "
                    "security interest, so credit sales need an "
                    "Article 9 strategy where appropriate. Keep "
                    "equipment sourcing compensation distinct from patient "
                    "referrals. The federal Anti-Kickback Statute can "
                    "reach remuneration tied to federally reimbursable "
                    "business; a sourcing-fee label does not determine "
                    "the substance of the arrangement."
                ),
            ],
            "table": {
                "caption": "Six Evidence Controls That Protect Collectibility and Equipment Ownership",
                "headers": [
                    "Control and accountable operating owner",
                    "Evidence required in the transaction record",
                    "Payment or inventory failure prevented",
                    "Fallback when evidence remains inadequate",
                ],
                "rows": [
                    [
                        "Sales operations verifies purchasing identity and signing authority",
                        "Entity record, verified address, purchase order, and authorized signatory",
                        "An enthusiastic employee commits funds the organization never authorized",
                        "Require authorized execution before reserving or purchasing dedicated inventory",
                    ],
                    [
                        "Credit owner reviews aggregate open customer exposure",
                        "Credit report, references, financial statements, and existing unpaid invoices",
                        "Multiple individually small shipments create an unmanageable unsecured balance",
                        "Reduce credit limit or require funded settlement before shipment",
                    ],
                    [
                        "Acquisition lead validates ownership and existing lender claims",
                        "Bill of sale, lease release, lien search, and payoff evidence",
                        "Secured creditor or lessor asserts superior rights after acquisition",
                        "Pay verified lienholder directly under documented release arrangements",
                    ],
                    [
                        "Biomed lead substantiates the quoted configuration and performance",
                        "Serial photographs, service history, measured tests, and accessory inventory",
                        "Missing options or failed performance justify a material payment dispute",
                        "Repair, substitute by agreement, or return under written remedies",
                    ],
                    [
                        "Data and receiving leads verify safe equipment transfer",
                        "Media sanitization record, decontamination evidence, and handling instructions",
                        "Residual patient data or contamination prevents safe incoming acceptance",
                        "Quarantine equipment and complete qualified remediation before further movement",
                    ],
                    [
                        "Deal owner documents compensation and protected commercial introductions",
                        "Executed engagement, dated introduction record, fee trigger, and closing statement",
                        "Counterparties close directly while disputing the intermediary's earned compensation",
                        "Use contractual collection remedies without obstructing legitimate device servicing",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Checks Before Releasing a Serial Number",
                "body": (
                    "Keep equipment under operational control until the evidence "
                    "supports the specific release decision."
                ),
                "items": [
                    "Verify ownership and resolve identified leases or liens with authenticated release documentation.",
                    "Complete configuration testing, serviceability review, decontamination evidence, and applicable patient-data sanitization.",
                    "Match the buyer's authorized commitment to funded escrow, verified receipt, or an explicitly approved credit limit.",
                    "Confirm signed acceptance criteria, freight responsibility, warranty remedies, and independently authenticated payment instructions.",
                ],
            },
        },
        {
            "heading": "4. Separate Chapter 11 Claim Economics from Equipment Revenue",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The required adjacent play is "
                    "chapter11_trade_claim_convenience_class_rollup: Chapter 11 "
                    "Bankruptcy Schedule E/F Trade-Claim & Convenience-Class "
                    "Rollups, TRACK_1. Equipment suppliers may hold unpaid "
                    "trade receivables against a restructuring hospital or "
                    "practice group and prefer immediate cash to uncertain "
                    "distributions. The operator purchases a documented claim "
                    "at a discount; the seller receives the purchase price, "
                    "while the plan administrator later pays the recognized "
                    "claim holder under applicable plan terms. Start with "
                    "Schedule E/F, invoices, delivery records, credits, "
                    "contracts, proofs of claim, and the claims register. "
                    "A scheduled amount is a diligence lead, not proof "
                    "of an allowed collectible asset. Under 11 U.S.C. "
                    "1111(a), certain scheduled claims are deemed filed, "
                    "but disputed, contingent, or unliquidated scheduled "
                    "claims fall outside that treatment. Evaluate bar "
                    "dates, objections, setoff, recoupment, asserted priority, "
                    "and possible claim-disallowance issues. Separate "
                    "equipment ownership disputes from unsecured invoice "
                    "claims. A retained security interest, lease, or "
                    "reclamation position can change both rights and "
                    "valuation. Never buy solely because a schedule "
                    "shows a familiar equipment vendor and an "
                    "apparently attractive face amount. Confirm who "
                    "actually owns the receivable and whether it "
                    "has already been assigned or factored."
                ),
                (
                    "Convenience-class economics depend on the actual plan, "
                    "not a generic small-claim threshold. Section 1122(b) "
                    "permits a separate class of small unsecured claims "
                    "when the court approves the amount as reasonable "
                    "and necessary for administrative convenience. Read "
                    "eligibility, election mechanics, aggregation provisions, "
                    "anti-splitting terms, distribution caps, and amendment "
                    "history before bidding. Suppose a supported $10,000 "
                    "claim has an illustrative 70% probability of "
                    "receiving a $6,000 distribution and a 30% "
                    "probability of zero recovery. Expected cash is "
                    "$4,200. Paying $2,800 plus $400 of transfer "
                    "and administration costs produces $1,000 of "
                    "undiscounted expected surplus before funding costs "
                    "and taxes; success produces $2,800, while zero "
                    "recovery loses $3,200. Apply a timing discount "
                    "and sensitivity analysis rather than presenting "
                    "expected value as a promised payout. If "
                    "supported general-unsecured recovery falls to 20% "
                    "of face, the $2,000 receipt would lose "
                    "$1,200 against that same cost basis. Do "
                    "not manufacture convenience eligibility by splitting "
                    "claims or assume buying several claims preserves "
                    "each seller's treatment. Stop affected purchases, "
                    "enforce documented seller recourse where available, "
                    "and price only supported general-unsecured recoveries. "
                    "Seller recourse is worth less when the "
                    "seller cannot perform."
                ),
                (
                    "Transfer procedure controls whether the expected payment "
                    "reaches the intended account. For qualifying transfers "
                    "after a proof of claim is filed, Bankruptcy "
                    "Rule 3001(e) provides filing and notice mechanics, "
                    "including a transferor objection period generally "
                    "measured at twenty-one days after mailed notice. "
                    "Different transfer situations have different procedures; "
                    "follow the rule, local requirements, and case "
                    "orders rather than one universal form. Confirm "
                    "the claims agent's register, distribution instructions, "
                    "tax documentation, and recognized holder before "
                    "projecting settlement timing. Keep claim purchases "
                    "in a separate ledger and capital allocation. "
                    "The volume scorecard remains exclusively equipment "
                    "resale: Conservative revenue of $250,000 less "
                    "$225,000 total costs yields $25,000; Base "
                    "revenue of $1,025,000 less $861,000 yields "
                    "$164,000; Scaled revenue of $1,800,000 less "
                    "$1,404,000 yields $396,000. Those costs "
                    "collectively include acquisition, refurbishment, and "
                    "other expenses needed to reach the specified "
                    "net margins. Claim face value, lender principal, "
                    "escrow deposits, and expected distributions cannot "
                    "inflate those equipment figures. With startup "
                    "capital of $20,000 to $95,000 and monthly "
                    "operating expense of $4,000 to $18,000, "
                    "cash trapped in speculative claims competes "
                    "directly with saleable inventory. Preserve capacity "
                    "for the stated three-to-nine-month first-deal window "
                    "before funding this adjacent strategy."
                ),
            ],
            "table": {
                "caption": "Chapter 11 Trade-Claim Purchase and Distribution Evidence Matrix",
                "headers": [
                    "Claim-investing decision and specific evidence",
                    "Economic or procedural test required",
                    "Failure mode that destroys expected spread",
                    "Required response before additional capital deployment",
                ],
                "rows": [
                    [
                        "Originate from Schedule E/F and corroborating vendor records",
                        "Match debtor entity, invoices, delivery evidence, credits, and ownership",
                        "Scheduled balance includes disputed amounts or previously assigned receivables",
                        "Reconcile the claim file and exclude unsupported purchased amounts",
                    ],
                    [
                        "Establish filing status using claims register and case orders",
                        "Check scheduled treatment, bar dates, amendments, and existing objections",
                        "Missed filing requirement prevents the expected claim from participating",
                        "Suspend purchase until a supported procedural path is documented",
                    ],
                    [
                        "Read convenience-class provisions in the operative bankruptcy plan",
                        "Test threshold, elections, aggregation rules, splitting restrictions, and caps",
                        "Purchased portfolio receives general-unsecured treatment instead of modeled convenience recovery",
                        "Reprice supported recovery or stop purchases affected by restrictions",
                    ],
                    [
                        "Underwrite the illustrative ten-thousand-dollar documented unsecured trade claim",
                        "Seventy percent times six thousand produces forty-two hundred expected receipts",
                        "A zero distribution loses thirty-two hundred including modeled transaction costs",
                        "Discount timing and stress recovery before setting maximum purchase price",
                    ],
                    [
                        "Complete applicable Rule 3001(e) transfer and notice procedures",
                        "Confirm filing, transferor notice, objection handling, and recognized holder",
                        "Administrator sends distribution to an unresolved or incorrect claimant",
                        "Resolve register discrepancies before relying on projected settlement cash",
                    ],
                    [
                        "Separate purchased claims from canonical equipment resale performance",
                        "Track purchase basis, distributions, expenses, timing, and seller recourse",
                        "Claim principal or face value inflates reported equipment revenue",
                        "Maintain separate ledgers and preserve inventory working capital first",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "The deal is not the buyer's promise; it is the serial-specific evidence that turns authorized money into collectible proceeds.",
    "diagram_id": "diag-04",
    "action_checklist": [
        "Map the requesting user, budget owner, authorized signer, acceptance signer, and payment-release owner for each qualified equipment buyer.",
        "Attach serials, accessories, service records, software rights, decontamination evidence, and measurable acceptance tests to every executable quotation.",
        "Select a settlement structure and document deposits, release triggers, credit exposure, refund conditions, and independently verified bank instructions.",
        "Screen buyer credit and supplier title, resolve identified liens or leases, and cap aggregate unsecured exposure before shipment.",
        "Document principal-versus-broker status and fee triggers while keeping equipment sourcing compensation separate from patient referral arrangements.",
        "Underwrite any Chapter 11 claim through plan-specific recovery, transfer, and objection evidence, using a separate ledger that cannot alter the canonical equipment scorecard.",
    ],
    "statutory_citations": [
        {
            "title": "UCC § 2-401 — Passing of Title; Reservation for Security",
            "url": "https://www.law.cornell.edu/ucc/2/2-401",
            "relevance": "Model UCC rule limiting retained title in delivered goods to a security interest; check the governing state's enacted text when structuring credit sales.",
        },
        {
            "title": "UCC § 9-315 — Secured Party's Rights on Disposition of Collateral and in Proceeds",
            "url": "https://www.law.cornell.edu/ucc/9/9-315",
            "relevance": "Supports lien diligence and authenticated releases because security interests can continue after disposition, subject to applicable exceptions and authorization.",
        },
        {
            "title": "45 CFR § 164.310(d) — Device and Media Controls",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310",
            "relevance": "Requires applicable HIPAA-regulated entities to address disposal, media reuse, and other device and media controls involving electronic protected health information.",
        },
        {
            "title": "21 CFR § 807.20 — Establishment Registration and Device Listing Applicability",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-B/section-807.20",
            "relevance": "Helps determine registration and listing obligations based on the actual device activities performed rather than the commercial refurbishment label.",
        },
        {
            "title": "21 CFR Part 820 — Quality Management System Regulation",
            "url": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820",
            "relevance": "Establishes applicable device-manufacturer quality system requirements; servicing and remanufacturing classification must precede assumptions about obligations.",
        },
        {
            "title": "42 U.S.C. § 1320a-7b(b) — Federal Anti-Kickback Statute",
            "url": "https://www.law.cornell.edu/uscode/text/42/1320a-7b",
            "relevance": "Addresses prohibited remuneration involving referrals or other federally reimbursable business; equipment sourcing fees require analysis of the actual arrangement.",
        },
        {
            "title": "11 U.S.C. § 1111(a) — Claims and Interests",
            "url": "https://www.law.cornell.edu/uscode/text/11/1111",
            "relevance": "Provides deemed-filed treatment for certain scheduled claims while excluding claims scheduled as disputed, contingent, or unliquidated.",
        },
        {
            "title": "11 U.S.C. § 1122(b) — Administrative Convenience Classification",
            "url": "https://www.law.cornell.edu/uscode/text/11/1122",
            "relevance": "Permits a separate small-unsecured-claim class using a court-approved amount reasonable and necessary for administrative convenience; the operative plan controls eligibility.",
        },
        {
            "title": "11 U.S.C. § 502 — Allowance of Claims or Interests",
            "url": "https://www.law.cornell.edu/uscode/text/11/502",
            "relevance": "Frames claim allowance, objections, and disallowance issues that affect the value of purchased trade receivables.",
        },
        {
            "title": "Federal Rule of Bankruptcy Procedure 3001(e) — Transferred Claims",
            "url": "https://www.law.cornell.edu/rules/frbp/rule_3001",
            "relevance": "Specifies transfer procedures, including applicable evidence, notice, and objection mechanics; the correct subsection depends on the transfer circumstances.",
        },
    ],
}
