from __future__ import annotations


def build_volume_019_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {"name": name, "type": input_type, "prompt": prompt, "example": example}

    return {
        "workbook_id": "wb-019-enterprise-software-reselling",
        "volume_id": "vol-019-enterprise-software-reselling",
        "title": "Enterprise Software Reselling — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Enterprise VAR Underwriting, "
            "CPPO and CSP Deal Economics, License Delivery, Contract Controls, "
            "Renewal Automation, and Small-Team Launch Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity, Vertical Underwriting, and Counterparty Qualification",
                "purpose": (
                    "Select enterprise software opportunities that combine enforceable channel rights, "
                    "funded customer demand, manageable implementation work, and collectible invoices. "
                    "Use this worksheet before committing engineering capacity or accepting vendor "
                    "payment obligations, with separate evidence for the customer, publisher, "
                    "distributor, and marketplace route."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one vertical and one initial software problem rather than presenting "
                        "an unrestricted product catalog. Document the buyer's existing environment, "
                        "budget owner, renewal deadline, deployment constraints, and measurable reason "
                        "to buy through your company instead of directly."
                    ),
                    (
                        "Verify reseller status through the publisher or authorized distributor before "
                        "quoting. Record the legal entity, approved territory, eligible products, program "
                        "tier, expiration date, and separate permissions required for AWS Marketplace "
                        "CPPO or Microsoft CSP transactions."
                    ),
                    (
                        "Interview the economic buyer and implementation owner separately. Reconcile "
                        "their answers against procurement records, current entitlements, security "
                        "requirements, and contract dates; a favorable technical demonstration does "
                        "not establish purchasing authority, payment capacity, or migration readiness."
                    ),
                    (
                        "Build a short counterparty evidence packet containing registration documents, "
                        "credit terms, references, procurement contacts, and vendor escalation routes. "
                        "Identify concentration and related-party exposure before treating several "
                        "subsidiaries or distributor accounts as genuinely independent sources of demand."
                    ),
                    (
                        "Score the opportunity using documented evidence, then assign pursue, repair, "
                        "or decline. Require named owners and dated remedies for unresolved channel "
                        "rights, weak collection terms, or implementation dependencies before issuing "
                        "an offer that creates a binding obligation."
                    ),
                ],
                "fields": [
                    field(
                        "Vertical and urgent operating problem",
                        "textarea",
                        (
                            "Define the initial customer segment, operational pain, purchasing trigger, "
                            "and scope boundary. Explain why this segment needs a reseller's technical "
                            "or procurement capability rather than an additional purchasing intermediary."
                        ),
                        (
                            "Target regional manufacturers with 300 to 900 employees using fragmented "
                            "endpoint tools. The opening offer consolidates 600 managed endpoints before "
                            "an October renewal. Our advantage is entitlement cleanup and deployment "
                            "sequencing; we exclude plant-control systems because their validation work "
                            "would exceed the implementation team's capacity."
                        ),
                    ),
                    field(
                        "Buying committee and funded authority",
                        "textarea",
                        (
                            "Name the economic buyer, technical evaluator, procurement representative, "
                            "and payment owner by role. Record the evidence connecting their authority "
                            "to the exact product, budget period, purchase amount, and signing entity."
                        ),
                        (
                            "The IT director owns requirements, the CFO controls a $120,000 annual "
                            "software budget, and procurement issues the purchase order. Accounts payable "
                            "confirms the invoicing entity and portal. A budget extract dated June 3 "
                            "covers the proposed $100,000 package; the security architect evaluates "
                            "deployment but cannot authorize spending."
                        ),
                    ),
                    field(
                        "Publisher and distributor authorization",
                        "textarea",
                        (
                            "Capture documentary proof of channel authorization, including entity name, "
                            "territory, product family, agreement term, support obligations, and resale "
                            "restrictions. Distinguish publisher authorization from a distributor account "
                            "that merely permits product purchasing."
                        ),
                        (
                            "The publisher confirms our domestic entity may resell its endpoint "
                            "subscription in the United States through December 31. The distributor "
                            "provides a matching account schedule and escalation contact. We archive "
                            "both documents, verify renewal requirements quarterly, and exclude Canadian "
                            "affiliates until territorial permission is documented."
                        ),
                    ),
                    field(
                        "Marketplace route and transaction eligibility",
                        "textarea",
                        (
                            "Select direct VAR resale, AWS Marketplace CPPO, or the appropriate Microsoft "
                            "CSP arrangement. Identify which party creates the offer, accepts payment, "
                            "supplies entitlements, handles taxes, and carries settlement or cancellation exposure."
                        ),
                        (
                            "Use AWS Marketplace CPPO only after the publisher issues the required "
                            "selling authorization and the buyer confirms its eligible account. The "
                            "channel manager checks current settlement and fee terms. A separate "
                            "implementation statement of work bills $20,000 directly; marketplace "
                            "purchase eligibility does not automatically authorize access to customer systems."
                        ),
                    ),
                    field(
                        "Deal registration and competitive protection",
                        "textarea",
                        (
                            "Document registration status, protected products, expiration, pricing benefits, "
                            "and conflict procedures. Explain what remains competitive even after "
                            "registration and how the team will respond if the publisher rejects or "
                            "withdraws the registration."
                        ),
                        (
                            "Register 600 endpoint seats against the customer's legal entity with an "
                            "expected September signature. The publisher confirms a 90-day registration "
                            "period and deal-specific discount. Protection covers the named opportunity, "
                            "not every affiliate or later expansion. If disputed, suspend discount "
                            "claims and obtain a written channel-manager determination before repricing."
                        ),
                    ),
                    field(
                        "Customer credit and procurement evidence",
                        "textarea",
                        (
                            "Assess collection risk using payment history, credit references, purchasing "
                            "procedures, and invoice acceptance requirements. Record deposit terms and "
                            "exposure limits separately from the customer's willingness to sign a "
                            "large multiyear subscription."
                        ),
                        (
                            "The customer supplies two trade references showing payment within 45 "
                            "days and confirms a mandatory purchase-order field. We require $30,000 "
                            "before ordering and cap unpaid exposure at $70,000. Procurement validates "
                            "the supplier record first; an unsigned portal invitation does not justify "
                            "releasing a noncancelable vendor order."
                        ),
                    ),
                    field(
                        "Implementation fit and delivery dependencies",
                        "textarea",
                        (
                            "List systems, migration steps, customer responsibilities, required skills, "
                            "and acceptance evidence. Identify dependencies that can consume implementation "
                            "spread even when the software discount appears attractive, including access "
                            "delays and inconsistent source inventories."
                        ),
                        (
                            "The $20,000 implementation covers inventory validation, a 50-device pilot, "
                            "and deployment to 550 remaining endpoints. Planned delivery cost is "
                            "$12,000. The customer supplies administrative access and approved maintenance "
                            "windows. Unsupported operating systems and application remediation require "
                            "a signed scope change rather than unpaid expansion of the original work."
                        ),
                    ),
                    field(
                        "Concentration and counterparty linkage",
                        "textarea",
                        (
                            "Measure customer, publisher, distributor, and sector concentration using "
                            "annual billings and contribution. Identify shared ownership, common payment "
                            "systems, and correlated renewal dates that could make apparently separate "
                            "accounts fail or delay payment together."
                        ),
                        (
                            "Three subsidiaries represent $420,000 of the $1,400,000 base scenario, "
                            "or 30% of gross revenue, but share one treasury function. The same "
                            "publisher supplies 65% of license purchases. Treat the subsidiaries as "
                            "one credit exposure and develop a second authorized product line before "
                            "adding another related account."
                        ),
                    ),
                    field(
                        "Evidence-weighted opportunity score",
                        "textarea",
                        (
                            "Create a repeatable scoring rubric for demand, channel rights, collection "
                            "quality, implementation fit, and competitive differentiation. Assign "
                            "evidence-based points and state which failures require repair regardless "
                            "of the total numerical score."
                        ),
                        (
                            "Award 25 points for funded demand, 25 for verified channel rights, "
                            "20 for collection quality, 20 for delivery fit, and 10 for differentiation. "
                            "This opportunity scores 86 of 100. Missing resale permission still forces "
                            "repair, even if other categories score perfectly; numerical strength "
                            "cannot substitute for contractual authority."
                        ),
                    ),
                    field(
                        "Pursuit decision and bounded next commitment",
                        "textarea",
                        (
                            "State pursue, repair, or decline with an accountable owner, evidence "
                            "deadline, and maximum next commitment. Connect the decision to the "
                            "candidate's specialist profile instead of treating pipeline size as proof "
                            "of operating quality."
                        ),
                        (
                            "Pursue with a $2,000 discovery budget and no vendor purchase until "
                            "authorization and deposit evidence are complete. Enterprise Software "
                            "Reselling is candidate 23, ranked 19 of 29, with a 87/100 "
                            "Money-to-Manpower Score. That disciplined specialist profile favors "
                            "repeatable deployments over broad catalog selling or speculative inventory commitments."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The channel lead and delivery lead sign the evidence packet only after "
                    "resale rights, purchasing authority, credit exposure, deployment scope, and "
                    "the next spending limit are documented; unresolved mandatory conditions "
                    "remain assigned repair items rather than approved pursuits."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve, and Working-Capital Float",
                "purpose": (
                    "Translate license discounts and implementation spreads into owner-level "
                    "economics without confusing vendor pass-through costs, customer spending, "
                    "or marketplace transaction volume with profit. Reconcile every annual "
                    "scenario to the canonical scorecard, then size cash needs using actual "
                    "collection and supplier-payment dates."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Separate license billings, implementation billings, vendor purchases, delivery "
                        "labor, transaction fees, overhead, and expected credits. Use one currency "
                        "and one reporting period throughout; exclude collected sales taxes from "
                        "revenue and keep customer deposits distinct from earned revenue."
                    ),
                    (
                        "Determine the principal-versus-agent presentation for each actual arrangement "
                        "with the accountant using ASC 606 considerations. The canonical scenarios "
                        "use gross license resale and service billings; do not force a "
                        "commission-only agency arrangement into that gross presentation."
                    ),
                    (
                        "Calculate a representative deal from customer price through attributable "
                        "costs and a supported defect allowance. Identify whether each reserve "
                        "represents a revenue adjustment, cost estimate, or cash buffer so the "
                        "same exposure is not deducted twice."
                    ),
                    (
                        "Build a dated cash waterfall from deposit through final collection, "
                        "including vendor due dates, payroll, marketplace settlement delays, and "
                        "restricted cash. Size the funding requirement from the deepest cumulative "
                        "deficit rather than multiplying revenue by an arbitrary percentage."
                    ),
                    (
                        "Reconcile Conservative, Base, and Scaled results exactly, then stress "
                        "payment delay, discount erosion, and delivery rework separately. Preserve "
                        "the canonical benchmarks while labeling any actual forecast that "
                        "departs from their revenue, cost, staffing, or timing assumptions."
                    ),
                ],
                "fields": [
                    field(
                        "Revenue basis and presentation boundary",
                        "textarea",
                        (
                            "Describe what the company sells and controls before transfer, its pricing "
                            "discretion, and its fulfillment responsibility. Separate gross resale "
                            "arrangements from agency commissions, customer cloud consumption, taxes, "
                            "and marketplace-reported transaction volume."
                        ),
                        (
                            "The benchmark records $80,000 of license resale and $20,000 of "
                            "implementation billings, with $68,000 of vendor cost retained in expenses. "
                            "For a different arrangement that earns only a $5,000 referral commission, "
                            "record the commission under the appropriate policy rather than treating "
                            "the customer's $100,000 purchase as our revenue."
                        ),
                    ),
                    field(
                        "Representative deal contribution bridge",
                        "textarea",
                        (
                            "Enter customer billings and every direct cost before overhead. Show "
                            "license spread separately from implementation spread, and identify any "
                            "marketplace fees, distributor charges, or commissions that could otherwise "
                            "disappear inside an attractive discount percentage."
                        ),
                        (
                            "License billings of $80,000 less $68,000 vendor cost produce $12,000 "
                            "spread. Implementation billings of $20,000 less $12,000 delivery labor "
                            "produce $8,000 spread. Combined contribution is $20,000 before the "
                            "$2,000 defect allowance and $4,000 operating allocation, leaving "
                            "$14,000 modeled deal profit on $100,000 billings."
                        ),
                    ),
                    field(
                        "Scrub and defect reserve methodology",
                        "textarea",
                        (
                            "Estimate losses from seat-count corrections, provisioning errors, credits, "
                            "and rework using observable frequencies and severities. Distinguish the "
                            "management allowance from accounting entries, and define when evidence "
                            "requires increasing, using, or releasing the estimate."
                        ),
                        (
                            "Across 20 comparable $100,000 deals, four required $5,000 of incremental "
                            "rework and two required $10,000, producing $40,000 expected cost across "
                            "$2,000,000 billings, or 2%. Apply $2,000 to the example deal. "
                            "Credit exposure is tracked separately; the accountant maps actual events "
                            "to expense or revenue adjustment without duplicating this estimate."
                        ),
                    ),
                    field(
                        "Conservative canonical reconciliation",
                        "textarea",
                        (
                            "Reproduce the Conservative annual revenue, net margin, owner net profit, "
                            "and staffing exactly. Calculate the total allowable cost envelope and "
                            "explain why thin earnings require explicit scrutiny of labor affordability "
                            "and founder time."
                        ),
                        (
                            "Conservative gross revenue is $300,000 and net margin is 8%, yielding "
                            "$24,000 annual owner net profit. Total modeled costs are $276,000. "
                            "Staffing remains 2 full-time people plus 3 contractors. Verify that "
                            "actual compensation and contractor hours fit the cost envelope; unpaid "
                            "founder work must not silently improve an operating forecast."
                        ),
                    ),
                    field(
                        "Base canonical reconciliation",
                        "textarea",
                        (
                            "Reproduce the Base annual revenue, net margin, owner net profit, and "
                            "staffing exactly. Translate the benchmark into a repeatable deal model "
                            "without claiming that every customer has identical implementation scope "
                            "or collection timing."
                        ),
                        (
                            "Base gross revenue is $1,400,000 at a 14.0% net margin, producing "
                            "$196,000 annual owner net profit and $1,204,000 total modeled costs. "
                            "Staffing is 2 full-time people plus 3 contractors. Fourteen example "
                            "deals at $100,000 billings and $14,000 profit reconcile the arithmetic, "
                            "while actual delivery schedules require separate capacity validation."
                        ),
                    ),
                    field(
                        "Scaled canonical reconciliation",
                        "textarea",
                        (
                            "Reproduce the Scaled annual revenue, net margin, owner net profit, and "
                            "staffing exactly. Identify the operating improvements required to reach "
                            "that margin instead of mechanically extending the Base deal's economics "
                            "to higher volume."
                        ),
                        (
                            "Scaled gross revenue is $2,500,000 at 20% net margin, yielding "
                            "$500,000 annual owner net profit with $2,000,000 total modeled costs. "
                            "The team is 3 full-time people plus 4 contractors, seven people "
                            "altogether. Twenty-five unchanged Base example deals yield only $350,000 "
                            "profit; reaching the benchmark requires another $150,000 of improvement."
                        ),
                    ),
                    field(
                        "Dated working-capital float",
                        "textarea",
                        (
                            "List cash inflows and outflows by settlement date, then calculate the "
                            "largest cumulative deficit. Treat an unspent reserve as a liquidity "
                            "buffer rather than pretending it is already a supplier payment or "
                            "collected revenue."
                        ),
                        (
                            "Collect $30,000 on day 0, pay the vendor $68,000 on day 15, "
                            "and pay $12,000 delivery labor plus $4,000 operating costs by day "
                            "30. The deficit reaches $54,000 before the remaining $70,000 arrives "
                            "on day 60. Add a $2,000 liquidity buffer for a $56,000 funding target."
                        ),
                    ),
                    field(
                        "Startup capital and concurrent exposure",
                        "textarea",
                        (
                            "Compare startup funds with overlapping deal deficits, fixed operating "
                            "burn, and delayed first revenue. Use the supplied capital, expense, "
                            "and first-deal ranges while distinguishing a range boundary from a "
                            "funded operating plan."
                        ),
                        (
                            "The candidate range is $15,000 to $75,000 startup capital, $5,000 "
                            "to $25,000 monthly operating expense, and 3 to 9 months to "
                            "first deal. A $150,000 plan using $30,000 for six months of "
                            "pre-deal burn and $112,000 for two concurrent buffered deals leaves "
                            "only $8,000 before other setup costs."
                        ),
                    ),
                    field(
                        "Discount and collection stress cases",
                        "textarea",
                        (
                            "Calculate separate effects of vendor-cost increases, slower payment, and "
                            "delivery overruns. State which stress changes profit and which initially "
                            "changes cash duration, then combine them only after preserving their "
                            "individual effects."
                        ),
                        (
                            "A five-point increase in vendor cost measured against $80,000 license "
                            "billings adds $4,000 expense and reduces modeled profit from $14,000 "
                            "to $10,000. A collection delay from day 60 to day 90 extends "
                            "the $54,000 peak deal deficit for 30 days without changing its "
                            "amount, before financing charges or additional operating burn."
                        ),
                    ),
                    field(
                        "Pricing floor and funding decision",
                        "textarea",
                        (
                            "Set the minimum acceptable price and deposit using complete costs, target "
                            "margin, and available liquidity. Identify who can authorize a deviation "
                            "and require a revised cash schedule whenever the customer changes "
                            "payment terms."
                        ),
                        (
                            "With $84,000 fixed modeled cash costs, a 2% revenue-based defect "
                            "allowance, and a 14% profit target, the price floor is "
                            "$84,000 divided by 0.84, or $100,000. If price drops to "
                            "$95,000, profit becomes $9,100 after a $1,900 allowance; the "
                            "owner must accept the lower margin explicitly."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner and accountant reconcile all three canonical scenarios, verify "
                    "the deal's revenue presentation, and confirm committed liquidity covers "
                    "the dated peak deficit plus the selected buffer before vendor obligations "
                    "are incurred."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Turn a signed software order into correct entitlements, accepted deployment, "
                    "and an auditable receivable. Establish one transaction identifier across "
                    "quotes, vendor purchases, marketplace records, service tickets, and ledger "
                    "entries so fulfillment defects can be traced without relying on personal "
                    "email histories."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign a deal identifier before generating the final quote and propagate "
                        "it into CRM, purchasing, implementation, and accounting records. Keep "
                        "customer-facing documents readable while preserving internal references "
                        "that connect every revision, entitlement change, and payment event."
                    ),
                    (
                        "Perform a four-way comparison of the signed customer order, approved "
                        "vendor quote, marketplace offer where applicable, and planned entitlement "
                        "configuration. Resolve differences in quantities, subscription dates, "
                        "currency, support level, and legal entity before provisioning begins."
                    ),
                    (
                        "Sequence implementation through a small pilot with explicit rollback "
                        "criteria before broad deployment. Record customer responsibilities and "
                        "technical evidence at each stage; successful license activation alone "
                        "does not demonstrate application compatibility, policy correctness, or "
                        "operational acceptance."
                    ),
                    (
                        "Record invoices, deposits, vendor liabilities, service milestones, and "
                        "credits according to the established accounting policy. Reconcile "
                        "marketplace settlement statements separately from offer acceptance, "
                        "because acceptance, provisioning, billing, and cash receipt can occur "
                        "on different dates."
                    ),
                    (
                        "Close the deal only after entitlement counts, customer acceptance, support "
                        "handoff, renewal dates, and ledger balances agree. Keep unresolved "
                        "exceptions assigned to an owner and due date rather than hiding "
                        "them in a completed implementation ticket."
                    ),
                ],
                "fields": [
                    field(
                        "Transaction identity and document lineage",
                        "textarea",
                        (
                            "Define the identifiers connecting the opportunity, quote version, customer "
                            "purchase order, vendor order, marketplace offer, deployment ticket, and "
                            "invoice. Specify where authoritative documents live and how superseded "
                            "versions remain distinguishable."
                        ),
                        (
                            "Deal ESR-1042 links HubSpot opportunity 1042, quote Q1042 revision 3, "
                            "customer purchase order 8816, vendor order V5720, and Jira project "
                            "DEP-1042. The controlled document folder marks revision 2 superseded. "
                            "The invoice references the purchase order and deal ID, preventing "
                            "accounts payable from rejecting an otherwise accurate $100,000 bill."
                        ),
                    ),
                    field(
                        "Quote-to-order commercial comparison",
                        "textarea",
                        (
                            "Compare product identifiers, quantities, price, term, renewal treatment, "
                            "support tier, tax treatment, and billing frequency across all binding "
                            "records. Identify which document controls each term and assign correction "
                            "responsibility before submission."
                        ),
                        (
                            "The signed quote requests 600 annual endpoint seats with premium "
                            "support, while the distributor draft contains 650 standard-support seats. "
                            "Purchasing stops the order and obtains a corrected draft. The reviewer "
                            "checks the September 1 start date and $68,000 vendor price against "
                            "the approved economics before releasing the purchase."
                        ),
                    ),
                    field(
                        "Tenant identity and provisioning authority",
                        "textarea",
                        (
                            "Record the verified customer tenant or account, designated administrator, "
                            "entitlement destination, and permitted access method. Explain how the "
                            "team prevents provisioning into a test tenant, reseller-owned account, "
                            "or similarly named affiliated company."
                        ),
                        (
                            "The customer's administrator confirms the production tenant identifier "
                            "through an established service ticket and authenticated portal session. "
                            "A second operator compares it with the signed deployment worksheet. "
                            "CSP administration uses approved granular delegated privileges where "
                            "applicable; no technician accepts shared owner credentials or provisions "
                            "licenses based solely on a forwarded email."
                        ),
                    ),
                    field(
                        "Pilot design and rollback evidence",
                        "textarea",
                        (
                            "Define pilot population, compatibility tests, success thresholds, monitoring "
                            "duration, and rollback procedure. Include representative high-risk workloads "
                            "rather than selecting only easy devices that could conceal the main "
                            "deployment failure modes."
                        ),
                        (
                            "Pilot 50 endpoints across finance, engineering, and warehouse teams "
                            "for five business days. Require all critical applications to launch, "
                            "zero unresolved severity-one incidents, and at least 49 devices reporting "
                            "correct policy. The technician documents uninstall and policy restoration "
                            "steps, then demonstrates rollback on two designated test devices."
                        ),
                    ),
                    field(
                        "Entitlement reconciliation and technical QA",
                        "textarea",
                        (
                            "Reconcile purchased, assigned, active, and billable licenses using vendor "
                            "exports and the customer's inventory. Define treatment for duplicates, "
                            "departed users, dormant devices, service accounts, and temporary migration "
                            "overlap before certifying delivery."
                        ),
                        (
                            "The vendor portal shows 600 purchased seats, 592 assigned seats, "
                            "and 584 active endpoints. Inventory identifies eight reserved onboarding "
                            "seats and eight offline devices awaiting maintenance windows. No duplicate "
                            "serial numbers remain. The customer accepts the documented deployment "
                            "schedule for offline devices instead of treating purchased seats as "
                            "proof of complete activation."
                        ),
                    ),
                    field(
                        "Service acceptance and scope-change ledger",
                        "textarea",
                        (
                            "Specify objective acceptance artifacts, customer response deadlines, "
                            "authorized signers, and procedures for additional work. Separate contractual "
                            "acceptance from internal ticket closure and record disputed deliverables "
                            "without assuming that silence always establishes acceptance."
                        ),
                        (
                            "Acceptance requires the endpoint inventory export, pilot test report, "
                            "policy screenshots, and administrator handoff session. The IT director "
                            "signs within the contract's five-business-day review period or lists "
                            "specific defects. A request to remediate 40 unsupported laptops becomes "
                            "a $6,000 change order, not an invisible addition to the $20,000 implementation."
                        ),
                    ),
                    field(
                        "Accounting event and deposit treatment",
                        "textarea",
                        (
                            "Describe the event sequence for deposits, supplier obligations, license "
                            "transfer, service completion, receivables, and earned revenue. State the "
                            "accounting policy dependencies and avoid treating cash receipt or a "
                            "purchase order as automatic revenue recognition."
                        ),
                        (
                            "Day-zero receipt of $30,000 is initially tracked as a customer "
                            "deposit under the established policy. License and service amounts are "
                            "recognized when the applicable obligations are satisfied, using the "
                            "accountant's allocation. The $68,000 vendor liability and $70,000 "
                            "remaining customer balance receive separate records; the deposit is "
                            "applied once, not counted again as revenue."
                        ),
                    ),
                    field(
                        "Marketplace settlement and fee reconciliation",
                        "textarea",
                        (
                            "Match offer records, customer invoices, marketplace fees, tax movements, "
                            "settlement reports, and bank receipts. Specify how timing differences "
                            "and withheld amounts are investigated without silently reducing license "
                            "quantities or changing the customer's contracted price."
                        ),
                        (
                            "For an illustrative $80,000 license transaction, the settlement report "
                            "shows a contract-specific $1,000 marketplace charge and $79,000 remitted. "
                            "The customer separately pays $20,000 for services. Record $100,000 "
                            "gross billings under the applicable principal policy and classify the "
                            "$1,000 charge within the example's $4,000 operating allocation, not twice."
                        ),
                    ),
                    field(
                        "Support handoff and renewal master record",
                        "textarea",
                        (
                            "Capture support ownership, response commitments, publisher escalation "
                            "routes, renewal dates, notice periods, and license-adjustment restrictions. "
                            "Ensure the recurring account record survives personnel changes and does "
                            "not depend on one salesperson's private calendar."
                        ),
                        (
                            "The account record lists September 1 subscription commencement, August "
                            "31 expiration, and the contract's actual renewal-notice deadline. "
                            "Support triage belongs to the service coordinator, with publisher "
                            "escalation attached. Renewal tasks open 120 days before expiration, "
                            "but cancellation reminders use the earlier contractual notice deadline "
                            "when the agreement requires one."
                        ),
                    ),
                    field(
                        "Exception closure and evidence retention",
                        "textarea",
                        (
                            "List remaining delivery, commercial, and accounting exceptions with "
                            "severity, owner, due date, and proof required for closure. Establish "
                            "record retention using contract, tax, dispute, and privacy requirements "
                            "rather than indefinite accumulation."
                        ),
                        (
                            "Exception EX-17 concerns eight offline endpoints and remains assigned "
                            "to the customer administrator until September 12. EX-18 concerns a "
                            "$1,000 fee classification and belongs to bookkeeping. The delivery "
                            "lead can close implementation after accepted scope is complete, but "
                            "neither exception disappears from the shared ledger until supporting "
                            "evidence is attached."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A reviewer other than the provisioning operator verifies tenant identity, "
                    "commercial terms, entitlement reconciliation, acceptance evidence, and "
                    "accounting links. Any remaining exception has an explicit owner, deadline, "
                    "and documented effect on collection, support, or renewal."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract, and Outreach Audit",
                "purpose": (
                    "Convert channel rules and applicable statutes into transaction-level "
                    "operating checks. Establish who may resell, who may access customer "
                    "systems, which procurement clauses apply, and how outreach is conducted, "
                    "while preserving evidence that connects each requirement to the "
                    "actual customer and contract."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Map each transaction to its entities, jurisdictions, product category, "
                        "customer sector, and sales channel before selecting requirements. "
                        "Separate universally used company controls from statutes or procurement "
                        "clauses that apply only because a particular customer or contract "
                        "creates the obligation."
                    ),
                    (
                        "Read the reseller agreement together with the end-user license and "
                        "customer statement of work. Compare assignment, renewal, audit, "
                        "support, cancellation, and liability terms so the customer promise "
                        "does not exceed rights granted by the publisher."
                    ),
                    (
                        "Inspect data flows and administrative access before implementation. "
                        "Determine whether the reseller processes personal information or "
                        "regulated records, identify required contract terms, and constrain "
                        "access to the minimum permissions and retention periods needed "
                        "for the documented service."
                    ),
                    (
                        "Review public-sector opportunities against the actual solicitation and "
                        "incorporated clauses rather than assuming commercial purchasing "
                        "practices transfer unchanged. Assign responsibility for representations, "
                        "product eligibility, mandatory flowdowns, and any schedule or "
                        "vehicle-specific pricing requirements before submission."
                    ),
                    (
                        "Audit email, telephone, and partner-generated outreach with source "
                        "records and suppression evidence. Document deficiencies as concrete "
                        "corrective work, including responsible owner and verification date, "
                        "before repeating the affected campaign or accepting another order "
                        "with the same defect."
                    ),
                ],
                "fields": [
                    field(
                        "Resale rights and copyright boundary",
                        "textarea",
                        (
                            "Identify the contractual rights supporting resale, distribution, activation, "
                            "and implementation. Address license restrictions directly and explain "
                            "why possession of an activation key or downloaded installer does "
                            "not establish transferable software rights."
                        ),
                        (
                            "The reviewer maps distribution restrictions to the publisher agreement "
                            "and records 17 U.S.C. § 106 as the copyright-rights baseline. "
                            "They do not assume 17 U.S.C. § 109 resolves subscription transfer "
                            "rights. Only publisher-issued entitlements flow to the named customer; "
                            "unused keys from another customer are never repackaged as authorized inventory."
                        ),
                    ),
                    field(
                        "Contract hierarchy and negotiated risk",
                        "textarea",
                        (
                            "Document the order of precedence among the master agreement, order "
                            "form, publisher terms, and service statement. Compare refund exposure, "
                            "warranties, indemnities, liability limits, and termination rights against "
                            "the upstream obligations actually available."
                        ),
                        (
                            "The master agreement controls service liability, the signed order "
                            "controls quantities and price, and publisher terms control software "
                            "use. A customer requests unrestricted refunds, but the vendor purchase "
                            "is noncancelable. The team negotiates objective delivery remedies before "
                            "signature and records the jurisdiction-specific treatment of software "
                            "under applicable contract law, including UCC Article 2 where relevant."
                        ),
                    ),
                    field(
                        "Renewal, cancellation, and seat-change rules",
                        "textarea",
                        (
                            "Capture the actual renewal mechanism, notice method, minimum term, "
                            "cancellation window, and seat-reduction rules. Assess automatic-renewal "
                            "statutes only within their defined scope and distinguish consumer "
                            "requirements from enterprise purchasing arrangements."
                        ),
                        (
                            "The account's annual subscription permits cancellation only within "
                            "the current program's documented window after renewal. The manager "
                            "stores that rule and its source date. California Business and "
                            "Professions Code § 17602 is reviewed when consumer offers fall "
                            "within its scope, not automatically imposed on every negotiated "
                            "business-to-business software purchase."
                        ),
                    ),
                    field(
                        "Privacy role and processing agreement",
                        "textarea",
                        (
                            "Map personal information accessed during selling, migration, support, "
                            "and telemetry collection. Determine controller, business, processor, "
                            "service-provider, or contractor roles from actual activities and "
                            "document applicable use restrictions, deletion duties, and subprocessors."
                        ),
                        (
                            "Implementation exports employee names, work emails, and device "
                            "identifiers into an access-controlled migration workspace. For an "
                            "applicable California engagement, the contract addresses California "
                            "Civil Code § 1798.100(d) and relevant 11 CCR § 7051 terms. "
                            "The reseller prohibits unrelated use, lists the approved hosting "
                            "provider, and deletes staging files after verified handoff."
                        ),
                    ),
                    field(
                        "Regulated customer data and security obligations",
                        "textarea",
                        (
                            "Determine whether the service creates access to health, payment, "
                            "government, or other specially regulated information. Link each "
                            "required agreement and technical safeguard to the actual data "
                            "flow rather than the customer's industry label alone."
                        ),
                        (
                            "A healthcare deployment that exposes electronic protected health "
                            "information triggers review of business-associate obligations under "
                            "45 CFR §§ 164.502(e) and 164.504(e), plus applicable Security "
                            "Rule duties. A license-only sale with no such access is evaluated "
                            "separately. The delivery plan prohibits copying patient records into "
                            "ordinary support tickets or demonstration tenants."
                        ),
                    ),
                    field(
                        "Federal procurement and product eligibility",
                        "textarea",
                        (
                            "Identify the purchasing vehicle, solicitation clauses, required "
                            "registrations, product-origin conditions, and customer representations. "
                            "Separate commercial software licensing rules from security, supply "
                            "chain, and trade requirements that arise through incorporated terms."
                        ),
                        (
                            "For a federal commercial-software opportunity, the contracts lead "
                            "reviews FAR 12.212 and, for applicable defense purchases, DFARS "
                            "227.7202. They inspect incorporated FAR 52.204-25 restrictions "
                            "and FAR 52.225-5 trade requirements where included. No salesperson "
                            "asserts product eligibility from a distributor listing alone; publisher "
                            "evidence and the actual solicitation control the response."
                        ),
                    ),
                    field(
                        "Email and telephone outreach controls",
                        "textarea",
                        (
                            "Specify the outreach channel, recipient category, source of contact "
                            "details, sender identity, opt-out workflow, and suppression ownership. "
                            "Evaluate calling technology and recipient context before assuming "
                            "that every business campaign has identical statutory treatment."
                        ),
                        (
                            "Commercial email uses accurate headers, a valid postal address, "
                            "and a working opt-out under 15 U.S.C. § 7704; requests are "
                            "honored within 10 business days. Telephone campaigns receive a "
                            "separate review under 47 U.S.C. § 227 and 47 CFR § 64.1200, "
                            "including calling technology, number type, permission evidence, and "
                            "applicable state restrictions."
                        ),
                    ),
                    field(
                        "Tax sourcing and exemption evidence",
                        "textarea",
                        (
                            "Determine where licenses and services are sourced, which charges "
                            "are taxable, who collects tax, and whether exemption documents "
                            "apply. Distinguish marketplace collection from direct service "
                            "billing and keep tax liabilities outside operating revenue."
                        ),
                        (
                            "The tax reviewer checks New York Tax Law § 1105(a) and "
                            "applicable guidance for prewritten software, then verifies customer "
                            "use locations and any exemption certificate. Marketplace collection "
                            "on an $80,000 license order does not automatically resolve tax "
                            "on the separately billed $20,000 implementation; each invoice "
                            "receives its documented treatment."
                        ),
                    ),
                    field(
                        "Sanctions, exports, and payment redirection",
                        "textarea",
                        (
                            "Identify cross-border users, restricted destinations, beneficial "
                            "ownership concerns, and unusual payment instructions. Define when "
                            "export classification, sanctions screening, or independent bank-detail "
                            "verification is required before provisioning or transmitting funds."
                        ),
                        (
                            "A domestic buyer requests administrator access for an overseas "
                            "affiliate, triggering review of publisher territorial restrictions "
                            "and applicable Export Administration Regulations in 15 CFR Parts "
                            "730–774. Screening also checks relevant OFAC program restrictions. "
                            "A simultaneous bank-change email receives an independent callback "
                            "to the established distributor contact before any payment details change."
                        ),
                    ),
                    field(
                        "Requirement register and remediation evidence",
                        "textarea",
                        (
                            "Create a compact register connecting each applicable obligation "
                            "to its source, owner, evidence, review date, and transaction "
                            "effect. Distinguish missing documentation from an actual prohibited "
                            "activity and record the specific remedy for each."
                        ),
                        (
                            "Register item LEG-12 links reseller authorization to the publisher "
                            "agreement, names the channel manager, and expires December 31. "
                            "Item DATA-04 requires the signed processing addendum before tenant "
                            "access. Item TAX-03 requires a validated exemption certificate "
                            "before tax removal. Weekly review records completed evidence "
                            "rather than a blanket declaration that every requirement is satisfied."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The responsible contract, tax, and security reviewers confirm applicable "
                    "requirements with transaction-specific evidence. No sale proceeds on "
                    "unverified resale rights, unsupported procurement representations, missing "
                    "required data terms, or unresolved payment-redirection concerns."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Growth Flywheel, and Risk Fallback Tracker",
                "purpose": (
                    "Automate repeatable channel work without allowing stale prices, duplicate "
                    "events, or incorrect entitlement counts to create binding mistakes. "
                    "Connect renewal alerts, quote generation, and license reconciliation "
                    "to a measurable growth process, with human ownership and tested "
                    "fallbacks for vendor or platform failures."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Map the lifecycle from account qualification through renewal and select "
                        "only stable steps for automation. Define the authoritative system "
                        "for each datum so a convenient CRM copy cannot override current "
                        "vendor pricing, executed contract terms, or accepted entitlement evidence."
                    ),
                    (
                        "Implement renewal alerts, quote generation, and license reconciliation "
                        "as separate workflows with explicit inputs, outputs, owners, and "
                        "failure conditions. Start with draft outputs and comparison reports "
                        "before allowing any workflow to initiate an external commercial commitment."
                    ),
                    (
                        "Test duplicate delivery, missing identifiers, expired pricing, rate limits, "
                        "and partial failures before expanding workflow scope. Preserve "
                        "idempotency and traceability so retrying an event cannot create "
                        "a second order, duplicate invoice, or unauthorized increase "
                        "in customer entitlements."
                    ),
                    (
                        "Build growth around verified customer outcomes and timely renewal "
                        "conversations rather than undifferentiated contact volume. Measure "
                        "qualified meetings, protected opportunities, implementation attachment, "
                        "collection quality, and retained contribution by source to identify "
                        "channels that actually improve owner earnings."
                    ),
                    (
                        "Maintain a fallback for vendor-policy changes, marketplace outages, "
                        "slow collections, and channel competition. Assign activation thresholds "
                        "and test the manual procedure periodically so a failed automation "
                        "does not become a reason to bypass required authorization "
                        "or contractual checks."
                    ),
                ],
                "fields": [
                    field(
                        "System ownership and data contract",
                        "textarea",
                        (
                            "Assign authoritative sources for customer identity, product price, "
                            "contract term, entitlement quantity, invoice status, and renewal "
                            "date. Define required identifiers, validation rules, update frequency, "
                            "and ownership when two systems disagree."
                        ),
                        (
                            "HubSpot owns opportunity stage, the signed contract repository "
                            "owns renewal terms, the vendor portal owns provisioned quantities, "
                            "and QuickBooks Online owns posted receivables. Every integration "
                            "carries deal ID ESR-1042 and tenant ID. A CRM quantity change "
                            "creates a reconciliation task; it never directly rewrites the "
                            "vendor's entitlement record."
                        ),
                    ),
                    field(
                        "Renewal alert schedule and ownership",
                        "textarea",
                        (
                            "Define alert dates relative to both expiration and cancellation "
                            "deadlines, with escalation recipients and completion evidence. "
                            "Include customer usage review, publisher price validity, procurement "
                            "lead time, and the consequences of missed notice."
                        ),
                        (
                            "For an August 31 expiration and a July 2 cancellation deadline, "
                            "open discovery on May 3 and require a buyer decision by "
                            "June 15. Send owner reminders at 120, 90, and 60 days "
                            "before expiration, but escalate against July 2. Completing a "
                            "reminder requires recorded customer direction, not merely opening "
                            "the notification."
                        ),
                    ),
                    field(
                        "Quote generation and stale-price protection",
                        "textarea",
                        (
                            "Specify validated quote inputs, discount limits, offer expiration, "
                            "document versioning, and review conditions. Prevent automated "
                            "documents from promising unavailable program terms, unsupported "
                            "tax treatment, or discounts that expired after deal registration."
                        ),
                        (
                            "A draft generator combines the approved SKU list, 600-seat "
                            "quantity, current $68,000 vendor quote, and $20,000 service scope. "
                            "If vendor pricing expires Friday, the customer quote expires "
                            "no later than Friday. Changes exceeding a two-point margin "
                            "threshold route to the owner; automation produces a draft "
                            "rather than silently accepting the lower return."
                        ),
                    ),
                    field(
                        "License reconciliation automation",
                        "textarea",
                        (
                            "Describe how vendor exports, identity records, and endpoint "
                            "inventory are normalized and compared. Set thresholds for "
                            "exceptions and explain why automated discovery should not "
                            "delete accounts or purchase seats without authorized action."
                        ),
                        (
                            "A nightly Python job compares portal exports with Microsoft "
                            "Entra ID and the endpoint inventory using immutable identifiers. "
                            "It flags 12 duplicate device records and eight inactive assignments. "
                            "The service coordinator investigates before any change. The workflow "
                            "does not deactivate users, reduce contracted quantities, or buy "
                            "replacement seats merely because a report shows a mismatch."
                        ),
                    ),
                    field(
                        "Idempotency and failure recovery",
                        "textarea",
                        (
                            "Define the event key, processing status, retry policy, and "
                            "reconciliation procedure for external actions. Explain how "
                            "operators distinguish an unprocessed request from a completed "
                            "action whose acknowledgement was lost during transmission."
                        ),
                        (
                            "The integration uses deal ID, quote revision, and action type "
                            "as its idempotency key. After a vendor API timeout, it "
                            "checks the vendor order reference before resubmitting. Three "
                            "failed attempts move the event into a review queue. The "
                            "operator compares external records and records a resolution, "
                            "preventing two $68,000 purchase orders from one customer acceptance."
                        ),
                    ),
                    field(
                        "Outbound targeting and suppression loop",
                        "textarea",
                        (
                            "Define the target account list, evidence of relevance, outreach "
                            "sequence, suppression process, and success measures. Keep "
                            "contact sourcing distinct from purchasing authority and ensure "
                            "partner-supplied lists inherit the same exclusion and review rules."
                        ),
                        (
                            "Build a 120-account manufacturer list from documented fit signals "
                            "and existing professional relationships. Send two relevant emails "
                            "about renewal inventory cleanup, then stop unless engagement "
                            "supports follow-up. Suppression updates synchronize before each "
                            "send. Track replies and qualified meetings separately; a contact "
                            "opening a message does not establish permission for unrelated campaigns."
                        ),
                    ),
                    field(
                        "Growth funnel and source economics",
                        "textarea",
                        (
                            "Calculate stage conversion and acquisition cost from named "
                            "campaigns using actual qualified outcomes. Connect new deals "
                            "to contribution, collection performance, and delivery capacity "
                            "rather than evaluating growth solely through gross billings."
                        ),
                        (
                            "A $6,000 campaign reaches 120 selected accounts, produces 12 "
                            "qualified meetings, six validated opportunities, and two wins. "
                            "Acquisition cost is $3,000 per win. If each deal earns "
                            "$14,000 before incremental acquisition spending, the pair contributes "
                            "$22,000 afterward, unless that spending was already included "
                            "in the deal's operating allocation."
                        ),
                    ),
                    field(
                        "Customer outcome and referral flywheel",
                        "textarea",
                        (
                            "Identify the measurable customer result that supports expansion, "
                            "reference use, or referrals. Define permission for publishing "
                            "customer details and separate verified operational benefits from "
                            "unsubstantiated claims about savings or security outcomes."
                        ),
                        (
                            "The quarterly review documents 48 reclaimed assignments at an "
                            "illustrative $120 annual seat price, representing $5,760 potential "
                            "renewal savings if contract rules permit reduction. The account "
                            "manager requests permission for an anonymized case study and "
                            "one peer introduction. They do not describe unused seats "
                            "as realized savings before the renewal quantity actually changes."
                        ),
                    ),
                    field(
                        "Vendor policy and channel competition fallback",
                        "textarea",
                        (
                            "Set monitoring ownership and response triggers for discount "
                            "changes, program termination, registration disputes, and competing "
                            "offers. Identify alternatives that remain authorized and explain "
                            "how existing customer obligations will be honored during transition."
                        ),
                        (
                            "If the publisher reduces discount by five points on $80,000 "
                            "license billings, the manager reworks the $4,000 margin loss "
                            "before issuing new quotes. Existing signed commitments receive "
                            "separate review. Alternatives include a documented distributor "
                            "route or a properly authorized competing product; the team "
                            "never substitutes gray-market keys to preserve a promised discount."
                        ),
                    ),
                    field(
                        "Collection, outage, and manual operating fallback",
                        "textarea",
                        (
                            "Define triggers for collection escalation, marketplace outage "
                            "handling, and temporary manual processing. State who can "
                            "activate each fallback and which commercial, technical, and "
                            "recordkeeping controls remain mandatory while systems are unavailable."
                        ),
                        (
                            "At seven days overdue, the account manager contacts procurement; "
                            "at 15 days, the owner reviews further credit exposure. "
                            "A marketplace outage pauses new offer commitments while staff "
                            "maintain a dated manual register. They do not promise direct "
                            "billing as an interchangeable substitute until customer procurement "
                            "and publisher channel terms permit that route."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each automation has a named owner, authoritative inputs, tested duplicate "
                    "and failure handling, and a documented manual fallback. Growth reporting "
                    "separates qualified demand, retained contribution, and cash collection "
                    "from raw activity counts."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod Scorecard, and Exit Readiness",
                "purpose": (
                    "Organize the first month around channel access, validated demand, "
                    "repeatable delivery, and cash discipline rather than forcing an "
                    "unrealistic immediate close. Establish a small-team scorecard and "
                    "transferable operating records that support renewal continuity, "
                    "management review, and eventual ownership transition."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set a 30-day evidence target that respects the candidate's three "
                        "to twelve month first-deal range. Use the sprint to establish "
                        "authorization, account fit, pricing reliability, and implementation "
                        "readiness; distinguish completed setup work from signed revenue "
                        "or received customer cash."
                    ),
                    (
                        "Assign the operating pod before scheduling outreach and delivery. "
                        "Record full-time roles, contractor specialties, actual available "
                        "hours, and escalation responsibility so a five-person roster "
                        "does not imply five people working full-time on every "
                        "customer engagement simultaneously."
                    ),
                    (
                        "Review the scorecard weekly using documented definitions and "
                        "consistent denominators. Pair revenue and profit measures with "
                        "credit exposure, entitlement defects, renewal coverage, and "
                        "delivery utilization to prevent a seemingly productive sales "
                        "week from creating an unmanageable downstream workload."
                    ),
                    (
                        "Preserve canonical annual benchmarks separately from the rolling "
                        "forecast and actual results. Update the forecast when "
                        "compensation, vendor costs, payment terms, or conversion evidence "
                        "changes; do not silently rewrite the benchmark to make "
                        "a weak month appear aligned."
                    ),
                    (
                        "Build exit readiness through ordinary operating hygiene: assignable "
                        "contracts, documented customer relationships, accurate deferred "
                        "obligations, reproducible reconciliations, and accessible procedures. "
                        "Evaluate transfer restrictions before describing the company as "
                        "sale-ready, because channel rights and marketplace arrangements "
                        "may require counterparty permission."
                    ),
                ],
                "fields": [
                    field(
                        "Day-one baseline and sprint objective",
                        "textarea",
                        (
                            "Record starting capital, current permissions, available people, "
                            "existing relationships, and the evidence required by day "
                            "30. State which outcomes are prerequisites for revenue "
                            "and which are actual commercial results."
                        ),
                        (
                            "Start with $150,000 cash, two full-time operators, three "
                            "contractor relationships, and no completed resale authorization. "
                            "Day-30 targets are one authorized product line, 20 qualified "
                            "accounts, six discovery meetings, and two costed proposals. "
                            "Booked revenue remains zero until an executed transaction "
                            "supports recognition under the established policy; proposal value "
                            "is reported only as pipeline."
                        ),
                    ),
                    field(
                        "Week-one channel and operating foundation",
                        "textarea",
                        (
                            "Define the first week's deliverables, owners, dependencies, and "
                            "acceptance evidence. Prioritize channel eligibility, contractual "
                            "templates, banking controls, and the smallest coherent offer "
                            "before investing time in broad campaign assets."
                        ),
                        (
                            "During days 1 through 7, the channel lead submits the "
                            "publisher application and verifies distributor terms. The delivery "
                            "lead scopes the 600-endpoint offer and contractor rates. "
                            "Bookkeeping configures deposits, receivables, and vendor liabilities. "
                            "Completion requires saved application evidence, a costed service "
                            "scope, and tested invoice fields; an application submission "
                            "is not recorded as authorization."
                        ),
                    ),
                    field(
                        "Week-two demand and qualification sprint",
                        "textarea",
                        (
                            "Set account research, discovery, and qualification targets with "
                            "clear evidence standards. Identify how the team will "
                            "learn about buying authority, renewal dates, incumbent "
                            "licenses, procurement friction, and implementation constraints."
                        ),
                        (
                            "During days 8 through 14, research 20 manufacturers and "
                            "complete six discovery meetings. Four accounts must provide "
                            "renewal timing and a named budget owner before entering "
                            "qualified pipeline. The account manager records two disqualifications "
                            "for unsupported plant-system requirements, demonstrating that qualification "
                            "removes poor fits instead of merely increasing opportunity counts."
                        ),
                    ),
                    field(
                        "Week-three quoting and delivery rehearsal",
                        "textarea",
                        (
                            "Define proposal preparation, vendor-price validation, deployment "
                            "rehearsal, and cash-model testing for the third week. "
                            "Specify which activities can proceed before authorization "
                            "and which external commitments must wait for documented rights."
                        ),
                        (
                            "During days 15 through 21, prepare two internally reviewed "
                            "$100,000 proposals using confirmed vendor economics. Rehearse "
                            "tenant verification and license reconciliation in an authorized "
                            "test environment. If channel approval is still pending, "
                            "retain proposals as drafts and communicate the dependency; "
                            "do not accept a customer order that presumes rights "
                            "the company has not obtained."
                        ),
                    ),
                    field(
                        "Week-four review and next-month commitments",
                        "textarea",
                        (
                            "Describe the final sprint review, evidence required for "
                            "continued investment, and next-month spending limits. Separate "
                            "execution problems the team can repair from market "
                            "signals that justify changing the vertical or offer."
                        ),
                        (
                            "During days 22 through 30, review six discovery records, "
                            "two costed proposals, authorization status, and runway. Continue "
                            "with a $5,000 next-month operating ceiling if at least "
                            "two accounts show funded demand and a credible procurement "
                            "path. If neither does, revise targeting before increasing "
                            "outbound spending; the first-deal expectation remains three "
                            "to twelve months."
                        ),
                    ),
                    field(
                        "Pod roles and capacity allocation",
                        "textarea",
                        (
                            "Assign commercial, delivery, bookkeeping, security, and specialist "
                            "work across full-time employees and contractors. Quantify "
                            "productive capacity, concurrent-project limits, and coverage "
                            "during absences rather than equating headcount with available "
                            "implementation hours."
                        ),
                        (
                            "The Base pod uses two full-time people for channel "
                            "sales and delivery coordination, plus three contractors "
                            "covering implementation, security review, and bookkeeping. If "
                            "implementation capacity is 80 contractor hours monthly and "
                            "each deployment needs 40, cap planned starts at two. "
                            "The Scaled roster adds one full-time role and one "
                            "contractor, reaching seven people."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and operating thresholds",
                        "textarea",
                        (
                            "Define revenue, contribution, collection, renewal, defect, and "
                            "capacity measures with formulas and data sources. Include "
                            "thresholds that trigger concrete action, and distinguish "
                            "leading indicators from realized outcomes in the weekly "
                            "management discussion."
                        ),
                        (
                            "Track qualified opportunities, quote-to-win conversion, accepted "
                            "service hours, overdue receivables, and renewal decisions "
                            "completed before notice deadlines. Set a 100% evidence "
                            "target for reseller rights and tenant verification. If "
                            "more than 10% of receivables are over 30 days "
                            "past due, review new credit commitments before expanding "
                            "sales volume or vendor exposure."
                        ),
                    ),
                    field(
                        "Canonical scorecard and forecast variance",
                        "textarea",
                        (
                            "Preserve the candidate score breakdown and all annual "
                            "scenario outputs in the management record. Explain "
                            "variance using actual costs and timing rather than "
                            "substituting pipeline value, customer cloud spending, or "
                            "uncollected invoices for owner profit."
                        ),
                        (
                            "Scores are revenue potential 24, margin potential 23, team efficiency 17, startup accessibility 11, and automation potential 12. Annual benchmarks remain "
                            "$300,000/$24,000, $1,400,000/$196,000, and $2,500,000/$500,000 "
                            "for gross revenue/owner net profit. The weekly forecast "
                            "shows deviations separately and retains the corresponding "
                            "8%, 14%, and 20% canonical margins."
                        ),
                    ),
                    field(
                        "Exit-readiness records and transfer restrictions",
                        "textarea",
                        (
                            "Inventory customer contracts, channel agreements, renewal "
                            "cohorts, deferred service obligations, intellectual property, "
                            "and concentration exposures. Identify assignment, change-of-control, "
                            "and administrator-transfer requirements that a buyer would "
                            "need resolved before taking over operations."
                        ),
                        (
                            "The readiness folder contains executed customer agreements, "
                            "publisher authorizations, twelve-month renewal schedules, and "
                            "receivable aging. Five contracts require assignment permission, "
                            "so they remain explicit transfer tasks. The owner "
                            "also documents $40,000 of unperformed prepaid implementation "
                            "work; a potential buyer cannot treat the associated "
                            "cash as freely distributable earnings without considering "
                            "the remaining delivery obligation."
                        ),
                    ),
                    field(
                        "Continue, repair, or pause decision",
                        "textarea",
                        (
                            "State the day-30 operating decision, accountable owner, "
                            "next review date, and maximum cash commitment. Tie "
                            "the decision to authorization, validated demand, realistic "
                            "capacity, and available funding rather than enthusiasm "
                            "or sunk setup effort."
                        ),
                        (
                            "Continue for 30 additional days with a $5,000 operating "
                            "limit and no speculative license purchases. Authorization "
                            "is complete, two accounts have funded requirements, and "
                            "the example deal's $56,000 buffered funding need fits "
                            "available cash. Pause new commitments if vendor terms "
                            "change or customer deposits disappear; existing support "
                            "duties remain staffed during any pause."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The owner signs the day-30 review with evidence of authorization, "
                    "qualified demand, capacity, runway, and accountable next actions. "
                    "Actual results, rolling forecasts, and canonical benchmarks remain "
                    "separate, while transfer restrictions and unfinished customer "
                    "obligations stay visible in the readiness ledger."
                ),
            },
        ],
    }
