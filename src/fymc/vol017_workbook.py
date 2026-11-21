from __future__ import annotations


def build_volume_017_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {"name": name, "type": input_type, "prompt": prompt, "example": example}

    return {
        "workbook_id": "wb-017-domain-investing",
        "volume_id": "vol-017-domain-investing",
        "title": "Domain Investing — Operator Companion Workbook",
        "subtitle": "6 Printable Operator Worksheets for Domain Underwriting, Auction Discipline, Renewal Float, Trademark Screening, Secure Transfers, Outbound Upgrades, and Portfolio Exit Readiness",
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity Underwriting and Counterparty Qualification",
                "purpose": (
                    "Separate investable domain inventory from attractive stories by documenting buyer demand, "
                    "clean title, comparable transactions, carrying costs, and dispute exposure. Establish a "
                    "defensible acquisition ceiling before bidding, then qualify the seller and prospective "
                    "buyer without treating historic traffic or asking prices as verified value."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one acquisition lane: brandable, exact-match, or expired-authority inventory. "
                        "Describe the commercial problem the name solves, the probable end-user buyer, and "
                        "the evidence required to support resale pricing. Use separate assumptions for "
                        "wholesale liquidation and retail disposition."
                    ),
                    (
                        "Build a dated evidence packet using ICANN Lookup, registrar RDAP, USPTO Trademark "
                        "Search, WIPO decisions, and archived pages. Record what each source establishes "
                        "and what remains unresolved; registration availability alone establishes neither "
                        "clean ownership nor freedom from trademark conflict."
                    ),
                    (
                        "Collect closed-sale comparables with transaction dates, extensions, word counts, "
                        "and venue context. Label asking prices separately. Adjust explicitly for inferior "
                        "extensions, awkward spelling, longer holding periods, and concentrated buyer "
                        "demand rather than applying an unexplained portfolio-wide valuation multiplier."
                    ),
                    (
                        "Verify seller control and delivery mechanics before sending funds. Reconcile the "
                        "registrant account, invoicing entity, escrow beneficiary, transfer restrictions, "
                        "and auction terms. Where privacy services obscure public records, seek private "
                        "evidence through the transaction provider instead of guessing ownership."
                    ),
                    (
                        "Set the maximum all-in bid and rejection conditions before the auction starts. "
                        "Assign a second reviewer to trademark concerns or unusual ownership chains. "
                        "Preserve rejected opportunities so recurring defects become acquisition filters "
                        "rather than repeated research expenses."
                    ),
                ],
                "fields": [
                    field(
                        "Acquisition lane and buyer problem",
                        "textarea",
                        "Describe the domain category, buyer workflow, extension preference, and concrete upgrade benefit. Identify which assumptions are supported by evidence and which need validation before capital is committed to an illiquid asset.",
                        "Illustrative asset HarborLedger.example represents a brandable bookkeeping name, not a live listing. Target buyers are established bookkeeping firms using long hyphenated addresses. The thesis is easier verbal recall and cleaner email presentation; it does not assume search rankings, existing traffic, or rights to another business's identity.",
                    ),
                    field(
                        "Buyer universe and concentration",
                        "textarea",
                        "List distinct buyer segments, realistic purchasing authority, and evidence of spending capacity. Explain whether demand survives removal of the most obvious buyer, especially when a name resembles one company's distinctive brand.",
                        "The research sheet identifies 40 independent bookkeeping firms, 12 practice-management vendors, and 8 accounting education businesses. Removing the largest prospect leaves 59 potential users. No valuation depends on selling to a single trademark owner, and five exploratory conversations will test whether the naming benefit matters.",
                    ),
                    field(
                        "Closed-sale comparable set",
                        "textarea",
                        "Record three relevant completed sales, dates, source references, and adjustment logic. Distinguish verified public records from synthetic planning examples, and explain why an advertised asking price cannot substitute for transaction evidence in underwriting.",
                        "Training-only comparables are two-word commercial names closing at $6,000, $8,500, and $10,000. Their median is $8,500. A $500 deduction for weaker pronunciation produces an $8,000 retail hypothesis. Before purchasing, replace all three synthetic records with dated NameBio or marketplace transaction evidence.",
                    ),
                    field(
                        "Auction and drop-catch bid ceiling",
                        "textarea",
                        "Calculate the maximum hammer bid after platform charges, renewal exposure, research cost, and the chosen capital-at-risk limit. Record auction extension rules and whether a deposit, backorder charge, or premium renewal changes the calculation.",
                        "The approved all-in acquisition cap is $3,000. With a buyer charge equal to 10% of hammer price and $200 of fixed acquisition expenses, maximum hammer price is ($3,000 minus $200) divided by 1.10, or $2,545.45. The bidder stops at $2,545.",
                    ),
                    field(
                        "Trademark and dispute screen",
                        "textarea",
                        "Document exact, phonetic, plural, and commercial-context searches across trademark records and actual market use. Record the search date, relevant goods or services, ownership history, and any evidence that changes the legitimate-use thesis.",
                        "For the fictional bookkeeping candidate, the reviewer searches the proposed words, sound-alikes, and accounting services in USPTO records and ordinary web results. A similar active bookkeeping brand triggers rejection. A clean search packet reduces uncertainty but does not establish that unregistered rights or foreign conflicts are absent.",
                    ),
                    field(
                        "Expired-authority evidence scrub",
                        "textarea",
                        "Separate backlink quantity from transferable commercial usefulness. Review archived content, referring-domain quality, anchor concentration, redirects, malware history, and evidence of ownership changes; state precisely which historical signals receive zero value until independently corroborated.",
                        "A candidate shows 300 referring domains in an exported report, but 210 appear to be directory spam and 40 links target removed pages. The remaining 50 receive manual sampling. Acquisition value remains name-based until evidence supports utility; historical authority receives no automatic dollar premium.",
                    ),
                    field(
                        "Seller authority and title packet",
                        "textarea",
                        "Identify the contracting seller, payment beneficiary, domain-control evidence, and any broker authority. Explain how conflicting identities, business dissolutions, disputed prior transfers, or unverifiable account screenshots will be resolved before an irreversible payment instruction.",
                        "The seller supplies a signed authorization from the registered business, a registrar-generated ownership record, and a temporary DNS TXT challenge. The escrow beneficiary matches that business. A broker receives commission only under a separate written instruction; a screenshot alone is insufficient proof of authority.",
                    ),
                    field(
                        "Registrar restrictions and holding exposure",
                        "textarea",
                        "Record registration date, last transfer, registrant changes, expiration, registry premiums, and registrar-specific restrictions. Estimate the cash and time consequences of delivery delays without assuming that changing an account setting removes a mandatory transfer restriction.",
                        "The registrar confirms an inter-registrar transfer restriction remains for 35 days after a recent transfer. Retail delivery is scheduled after that date, with 90 days remaining before expiration. The purchase agreement permits the documented delay; the operator does not promise immediate transfer to another registrar.",
                    ),
                    field(
                        "Offer thesis and abandonment criteria",
                        "textarea",
                        "Write the specific investment thesis, purchase ceiling, expected holding window, and evidence that would invalidate the opportunity. Include a wholesale exit assumption that is independent of retail aspirations and explain when walking away preserves capital.",
                        "Acquire only below $3,000 all-in, target an $8,000 retail sale, and budget a 24-month hold. A $750 wholesale exit is a stress assumption, not a promised bid. Abandon the purchase if ownership cannot be verified, premium renewal exceeds $200 annually, or a relevant trademark conflict emerges.",
                    ),
                    field(
                        "Underwriting decision record",
                        "textarea",
                        "Summarize the decision, reviewer, evidence location, unresolved conditions, and capital authorization. Separate an attractive name from an executable transaction, and make clear which conditions must be satisfied before the bid or purchase becomes binding.",
                        "Decision DI-017-001 permits bidding up to $2,545 hammer only after seller authority and the registrar restriction are documented. The owner signs the commercial thesis; the research contractor signs the evidence checklist. The packet includes dated exports, source URLs, and the rejected alternatives supporting pricing discipline.",
                    ),
                ],
                "completion_gate": (
                    "Advance only when the buyer thesis, comparable evidence, seller authority, trademark "
                    "screen, transfer timing, and all-in purchase ceiling are documented; unresolved title "
                    "or relevant trademark concerns stop the acquisition."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve, and Working-Capital Float",
                "purpose": (
                    "Reconcile the three canonical scenarios to gross domain sale proceeds and annual owner "
                    "net profit while exposing acquisition costs, renewals, selling charges, and cash timing. "
                    "Separate inventory purchases from realized costs, reserve liquidity for defective assets, "
                    "and test whether the stated team can operate inside the modeled budget."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the canonical Conservative, Base, and Scaled revenue, margin, owner profit, "
                        "and staffing figures before adding assumptions. Treat sale proceeds as operator "
                        "revenue for owned inventory; distinguish broker commissions and buyer business "
                        "sales from that revenue basis."
                    ),
                    (
                        "Build a cost bridge for each scenario that totals revenue minus owner profit. "
                        "Allocate sold-domain basis, renewals, selling charges, direct diligence, and operating "
                        "overhead without double counting. Label the allocation as a planning decomposition, "
                        "not an additional canonical source."
                    ),
                    (
                        "Construct a monthly cash schedule independently of the profit calculation. Show "
                        "opening cash, inventory purchases, renewal dates, escrow settlement delays, and "
                        "operating payments. An unsold domain can consume cash without creating a completed "
                        "sale or an immediately realized acquisition expense."
                    ),
                    (
                        "Create a specific reserve for title defects, disputed transfers, chargebacks, "
                        "failed auctions, and emergency renewals. Distinguish cash earmarking from a booked "
                        "expense, and update realized losses in the ledger rather than silently changing "
                        "the published scenario totals."
                    ),
                    (
                        "Stress-test slower sales, lower prices, and labor costs that exceed the allowance. "
                        "Identify the minimum cash balance and actions available before exhaustion. "
                        "Preserve the canonical figures as reference cases while clearly marking any "
                        "new forecast as an alternative sensitivity."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        "Enter gross annual domain sale proceeds, net margin, owner net profit, total modeled costs, and team composition for all three cases. Verify multiplication and subtraction before using the scenarios in purchase decisions.",
                        "Conservative: $20,000 times 15% equals $3,000 profit, with $17,000 costs and 1 FT plus 1 C. Base: $160,000 times 27.5% equals $44,000, with $116,000 costs and the same team. Scaled: $300,000 times 40% equals $120,000, with $180,000 costs and 2 FT plus 2 C.",
                    ),
                    field(
                        "Sales count and average realized price",
                        "textarea",
                        "Translate annual revenue into completed sale counts and average prices using explicit illustrative assumptions. Distinguish names listed, qualified inquiries, signed agreements, funded escrow transactions, and completed sales so pipeline activity never masquerades as recognized proceeds.",
                        "One illustrative bridge is 4 completed sales at $5,000 for Conservative, 20 at $8,000 for Base, and 30 at $10,000 for Scaled. These yield exactly $20,000, $160,000, and $300,000. Counts and prices are planning assumptions; unsigned offers and unsold listings contribute zero completed-sale revenue.",
                    ),
                    field(
                        "Cost allocation bridge",
                        "textarea",
                        "Allocate each canonical cost total across sold inventory basis, portfolio renewals, selling charges, direct diligence, and operating overhead. Explain allocation assumptions and show every subtotal so no balancing amount is hidden inside an unexplained miscellaneous category.",
                        "Conservative allocates $8,000, $2,000, $3,000, $1,000, and $3,000 respectively, totaling $17,000. Base allocates $60,000, $12,000, $20,000, $4,000, and $20,000, totaling $116,000. Scaled allocates $90,000, $18,000, $30,000, $6,000, and $36,000, totaling $180,000. These are illustrative allocations preserving the canonical results.",
                    ),
                    field(
                        "Operating burn and labor feasibility",
                        "textarea",
                        "Separate recurring operating burn from sold inventory basis and transaction selling costs. Test contractor commitments, software, owner draws, and employee compensation against available cash; staffing labels describe capacity and must not silently imply fully funded market salaries.",
                        "Renewals plus diligence plus overhead equal $6,000, $36,000, and $60,000 annually, or $500, $3,000, and $5,000 monthly. The range matches the stated operating envelope. Before hiring, itemize compensation within these amounts; if required payroll exceeds them, the canonical case is operationally infeasible without a separately labeled revision.",
                    ),
                    field(
                        "Single-domain contribution calculation",
                        "textarea",
                        "Calculate sale proceeds less realized acquisition basis, allocated renewal cost, selling charges, and direct diligence for one completed transaction. Identify which overhead remains outside contribution so a strong individual sale is not confused with annual owner profit.",
                        "A Base illustration sells for $8,000, carries $3,000 acquisition basis, $600 renewal allocation, $1,000 selling charges, and $200 diligence allocation. Contribution is $3,200. Subtracting $1,000 allocated overhead leaves $2,200 owner profit per sale; 20 identical allocations produce the canonical $44,000 annual result.",
                    ),
                    field(
                        "Opening capital and cash trough",
                        "textarea",
                        "Specify startup cash within the stated range and schedule inventory purchases, recurring burn, and settlement receipts by month. Identify the lowest projected cash balance, keeping purchase capital separate from expenses recognized on completed sales.",
                        "A $50,000 opening balance funds $24,000 of initial inventory, leaving $26,000. Six months of Base recurring burn at $3,000 consumes $18,000, leaving $8,000 before sales. Acquisition purchases reduce cash immediately; their accounting treatment follows the adopted inventory policy rather than the timing of an auction receipt.",
                    ),
                    field(
                        "Renewal ladder and premium exposure",
                        "textarea",
                        "List domain counts, renewal prices, expiration months, and premium exceptions. Reconcile the annual schedule to the selected scenario while distinguishing standard registry charges from registrar services, restoration charges, and optional products that require separate authorization.",
                        "The Base renewal allowance is $12,000: 400 standard names at $20 cost $8,000, while 20 premium names at $200 cost $4,000. The ladder spreads expected payments across months but retains actual expiration dates. A registry price change triggers a new forecast and a domain-by-domain retention review.",
                    ),
                    field(
                        "Scrub and defect cash reserve",
                        "textarea",
                        "Size an earmarked cash buffer using explicit loss events and severities. Explain whether each item is a cash restriction, potential expense, or realized loss, and identify the evidence required before returning unused reserve capacity to acquisitions.",
                        "Earmark $5,000 from the $8,000 six-month cash trough: $2,000 for a disputed delivery, $1,500 for unexpected renewal exposure, and $1,500 for settlement interruption. Unrestricted cash is then $3,000. Earmarking does not itself reduce the canonical $44,000 profit; realized costs enter a separately updated operating forecast.",
                    ),
                    field(
                        "Escrow settlement and capital recycling",
                        "textarea",
                        "Calculate the period between buyer funding, verified delivery, provider release, and bank availability. Record transaction-specific hold assumptions and prohibit reinvestment of pending balances, especially where inspection terms, payment reversals, or ownership disputes can delay receipt.",
                        "An $8,000 sale carries an assumed $1,000 total selling charge, producing $7,000 net cash settlement. The forecast assumes five business days after verified delivery before bank availability, subject to provider terms. Acquisition spending uses cleared bank cash only; the ledger still records $8,000 gross sale proceeds.",
                    ),
                    field(
                        "Downside sensitivity and stop-spend rule",
                        "textarea",
                        "Stress the selected case using explicit changes to sale volume, price, and holding time. Preserve the canonical case alongside the sensitivity, and state the cash threshold that suspends bidding before renewal obligations or contracted expenses become unfunded.",
                        "If Base completes only 10 sales at $8,000, revenue becomes $80,000. Holding $36,000 recurring costs constant and assuming $30,000 sold basis plus $10,000 selling charges leaves $4,000. This sensitivity is not the canonical Base case. Suspend new acquisitions whenever unrestricted cash falls below three months of recurring burn.",
                    ),
                ],
                "completion_gate": (
                    "Advance only when all three canonical cases reconcile exactly, the selected cost "
                    "allocation is transparent, labor feasibility is tested, and monthly cash covers "
                    "scheduled renewals plus the explicitly earmarked defect reserve."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution Ledger and Technical Transfer Pre-Flight",
                "purpose": (
                    "Turn each acquisition and sale into an auditable sequence of verified ownership, "
                    "contracted delivery, funded settlement, secure transfer, and reconciled bookkeeping. "
                    "Prevent credential exposure, duplicate listings, lost renewals, and premature revenue "
                    "entries while preserving enough evidence to resolve delivery disputes without reconstructing events."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign one immutable asset identifier to each domain and one transaction identifier "
                        "to each purchase or sale. Link contracts, invoices, registrar events, renewal "
                        "payments, and settlement records through those identifiers rather than relying "
                        "on email subject lines."
                    ),
                    (
                        "Document the actual delivery route before promising a closing date. Confirm "
                        "whether the buyer needs an account push or an inter-registrar transfer, then "
                        "check locks, expiration, DNS dependencies, buyer account requirements, and "
                        "provider evidence standards."
                    ),
                    (
                        "Keep registrar credentials, recovery material, and transfer authorization codes "
                        "outside the printable workbook. Use a password manager with individual access "
                        "and multifactor authentication. The workbook records secret references and "
                        "responsible people, never the secret values themselves."
                    ),
                    (
                        "Treat buyer funding, asset delivery, and released proceeds as distinct states. "
                        "Verify each state through the provider's authenticated interface, not an email "
                        "claim. Preserve timestamps and event identifiers so settlement cannot be triggered "
                        "by a forged notification."
                    ),
                    (
                        "Close the transaction by reconciling gross proceeds, fees, bank receipts, asset "
                        "basis, and remaining obligations. Remove stale sales listings and verify the "
                        "buyer's control. Review exceptions weekly until every disputed or delayed "
                        "transaction has an accountable owner."
                    ),
                ],
                "fields": [
                    field(
                        "Asset register and evidence identifiers",
                        "textarea",
                        "Define the inventory record linking domain spelling, extension, registrar, ownership entity, acquisition date, basis, expiration, and evidence. Include internationalized-name handling where relevant so visually similar strings cannot be substituted during transfer or bookkeeping.",
                        "Asset DI-A0042 records HarborLedger.example, its exact lowercase ASCII representation, seller entity, purchase invoice PI-0042, and a $3,000 acquisition basis. Transaction DI-S0020 links the later sale. For an internationalized candidate, store both displayed Unicode and validated ASCII forms, with a manual comparison before contracting.",
                    ),
                    field(
                        "Purchase closing checklist",
                        "textarea",
                        "Record contract execution, escrow funding, seller verification, promised delivery method, and acceptance evidence. Identify which events authorize payment release and how discrepancies in the domain string, seller identity, or transfer timing will halt completion.",
                        "Purchase PI-0042 requires the exact asset identifier, a signed ownership warranty, funded escrow, and confirmed delivery into the operator's registrar account. The reviewer compares the final domain string against the contract before accepting. A mismatch in one character stops release and creates a dated exception record.",
                    ),
                    field(
                        "Registrar security and recovery ownership",
                        "textarea",
                        "Name the account owner, individual operator access, multifactor method, recovery custodian, and change-notification destination. Explain how access is removed after contractor departure without sharing a master login or relying on a former operator's personal mailbox.",
                        "The owner holds the registrar account with a hardware security key and a separately stored backup key. The contractor receives delegated access where supported, without payment or recovery privileges. Workbook reference VAULT-REG-02 points to the password manager; departure requires immediate access removal and recovery-contact verification.",
                    ),
                    field(
                        "Transfer restriction verification",
                        "textarea",
                        "Capture current transfer status, restriction dates, required authorization steps, and registrar confirmation. Distinguish an optional security lock from policy or registry restrictions, and document any permitted registrant-change lock opt-out before the relevant change occurs.",
                        "The selling registrar confirms that a recent transfer prevents another inter-registrar transfer until the stated 60-day period expires. Removing clientTransferProhibited would not remove that restriction. The agreement schedules delivery after expiry; any account push alternative requires confirmation that the registrar permits it and the buyer accepts it.",
                    ),
                    field(
                        "DNS and service continuity plan",
                        "textarea",
                        "Identify nameservers, DNSSEC status, active mail records, redirects, and any services included in the sale. Separate domain ownership from hosting or customer data, and plan changes so accidental service interruption cannot become an avoidable delivery dispute.",
                        "The sale transfers the domain only, excluding website files and mailboxes. Existing MX records are removed at the agreed cutover after seller confirmation. If DNS providers change, the operator coordinates DS record handling with the buyer and verifies resolution; stale DNSSEC delegation must not break the transferred name.",
                    ),
                    field(
                        "Buyer funding and impersonation check",
                        "textarea",
                        "Document the authenticated funding confirmation, buyer identity matching, and trusted communication channel. Specify how changed payment details, urgent release demands, spoofed escrow messages, or requests to move outside the agreed provider will be independently verified.",
                        "The buyer claims an $8,000 payment has cleared. The operator signs into the escrow provider through a saved address and checks transaction ES-0020 rather than following the email link. A later request to change the beneficiary is verified through the established channel and held until the provider confirms.",
                    ),
                    field(
                        "Delivery evidence and acceptance",
                        "textarea",
                        "Define the evidence that proves buyer control without exposing credentials. Record transfer completion, registrar confirmation, buyer acknowledgment, and the agreement's inspection period, including the process for resolving a timely objection before proceeds are released.",
                        "Delivery evidence includes the registrar's completed-transfer event, timestamped buyer acknowledgment, and a buyer-created DNS TXT challenge. The agreement provides a two-business-day inspection period for control and exact-name verification. Website performance is excluded because the asset sale contains no traffic promise or operating website deliverable.",
                    ),
                    field(
                        "Gross proceeds and settlement ledger",
                        "textarea",
                        "Record sale price, each selling charge, net provider release, bank receipt, and realized acquisition basis. Explain how the ledger preserves gross domain revenue even when a provider deposits only the fee-reduced amount into the operating account.",
                        "Sale DI-S0020 records $8,000 gross proceeds, $900 marketplace commission, $100 escrow cost, and a $7,000 bank receipt. The asset register releases $3,000 sold-domain basis. Renewal, diligence, and overhead allocations remain separately visible; the $7,000 deposit is not mislabeled as gross annual revenue.",
                    ),
                    field(
                        "Listing synchronization and duplicate-sale prevention",
                        "textarea",
                        "List every marketplace, landing page, broker mandate, and direct-sale channel carrying the asset. Define the event that pauses other listings and the evidence that confirms removal, especially where fixed-price or fast-transfer settings create binding sale exposure.",
                        "HarborLedger.example appears on two marketplaces and an owned landing page. Once the selected sale becomes binding under its contract, the operator pauses every competing listing immediately. Completed delivery triggers permanent removal. A daily reconciliation flags any sold asset still marked available and assigns same-day manual remediation.",
                    ),
                    field(
                        "Exception log and closeout verification",
                        "textarea",
                        "Record failed transfers, unexplained fees, disputed acceptance, late settlement, and unresolved access changes. Assign an owner and next review date, then define the evidence required to close each exception without erasing the original event history.",
                        "Exception EX-009 tracks a $100 difference between the expected and actual payout. The owner obtains the provider statement, identifies an additional service charge, and updates the ledger. Closeout requires matched bank cash, documented buyer control, removed listings, and zero remaining seller-access dependencies for the transferred asset.",
                    ),
                ],
                "completion_gate": (
                    "Close a sale only after exact-name delivery, authenticated buyer control, contract "
                    "acceptance, bank settlement reconciliation, basis release, and listing removal are "
                    "evidenced; retain open exceptions with named owners and dated next actions."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Contract, and Outreach Audit",
                "purpose": (
                    "Apply trademark, domain-dispute, contracting, outreach, and jurisdiction-specific operating "
                    "requirements to actual assets and communications. Convert legal exposure into documented "
                    "acquisition exclusions, factual sales claims, enforceable delivery terms, and targeted "
                    "specialist review rather than relying on availability checks or broad ownership assertions."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Screen the domain's words, use context, acquisition history, and intended buyers "
                        "against trademark rights. Preserve dated search evidence and commercial rationale. "
                        "Reject targeting strategies whose value depends on another party's distinctive "
                        "mark or an implied relationship with that party."
                    ),
                    (
                        "Evaluate UDRP and ACPA exposure separately because their procedures and remedies "
                        "differ. Record the relevant elements, available evidence, and response deadlines "
                        "if a complaint arrives. Do not assume a favorable trademark search eliminates "
                        "bad-faith evidence."
                    ),
                    (
                        "Read the registrar, registry, marketplace, and escrow terms governing the actual "
                        "transaction. Reconcile ownership warranties, delivery method, inspection, fees, "
                        "refund mechanics, and dispute venue. Obtain targeted contract review when the "
                        "transaction creates unfamiliar or material obligations."
                    ),
                    (
                        "Audit outbound messages for accurate identity, truthful subject lines, postal "
                        "address, advertising disclosures where required, and working suppression procedures. "
                        "Separate United States commercial-email requirements from other jurisdictions; "
                        "a business recipient is not an automatic exemption."
                    ),
                    (
                        "Map the operator's entity location, customer markets, business registrations, "
                        "tax treatment, and personal-data handling. Record the source and responsible "
                        "reviewer for each conclusion. Resolve transaction-specific uncertainty before "
                        "making representations that the evidence cannot support."
                    ),
                ],
                "fields": [
                    field(
                        "Trademark search scope and findings",
                        "textarea",
                        "Record exact and similar-mark searches, relevant goods or services, common-law use checks, and geographic scope. Explain how the domain's intended use changes the assessment and identify any facts requiring specialist review before purchase or outreach.",
                        "The operator searches USPTO Trademark Search, reviews relevant TSDR records, and checks ordinary commercial use of the candidate phrase in bookkeeping. A similar registered mark in directly overlapping services stops acquisition pending review. Search results are dated and retained; absence from one database does not establish unrestricted use.",
                    ),
                    field(
                        "UDRP element analysis",
                        "textarea",
                        "Apply UDRP paragraph 4(a) to confusing similarity, rights or legitimate interests, and registration and use in bad faith. Preserve facts about acquisition timing, prior use, advertising content, and the commercial reason for selecting the domain.",
                        "The worksheet records each of the three UDRP elements separately. A generic descriptive phrase acquired for a documented industry naming thesis differs from a typo acquired to approach one brand owner. Reviewer notes address paragraph 4(b) bad-faith examples and paragraph 4(c) legitimate-interest circumstances without treating either list as exhaustive.",
                    ),
                    field(
                        "ACPA exposure and remedy record",
                        "textarea",
                        "Assess bad-faith intent to profit and protected-mark similarity under 15 U.S.C. § 1125(d). Record conduct that increases exposure, including misleading contact details, repeated mark-targeted registrations, or offers whose rationale depends on exploiting another party's reputation.",
                        "The risk register cites 15 U.S.C. § 1125(d) and the statutory-damages election in 15 U.S.C. § 1117(d), which provides $1,000 to $100,000 per domain as the court considers just. These are litigation remedies, not automatic invoices; a plausible dispute stops promotional outreach while facts are reviewed.",
                    ),
                    field(
                        "Complaint response and preservation plan",
                        "textarea",
                        "Define who receives registrar notices, records service dates, preserves acquisition evidence, and instructs dispute counsel. Distinguish administrative proceedings from court litigation, and explain why domain transfers, deletions, or evidence alteration must stop once a dispute is identified.",
                        "A WIPO complaint notification is routed to the owner and designated counsel the same day. The log captures the commencement date and provider instructions, including the response deadline under UDRP Rules paragraph 5, ordinarily 20 days. Transfer attempts stop, records are preserved, and current rules are checked for any extension procedure.",
                    ),
                    field(
                        "Sale agreement and asset boundaries",
                        "textarea",
                        "Specify the exact domain, price, payment provider, delivery route, ownership representations, acceptance evidence, and excluded assets. Address renewal responsibility and transaction failure explicitly rather than relying on a marketplace listing to define every obligation between the parties.",
                        "The agreement sells HarborLedger.example for $8,000, domain only. It excludes trademarks, website content, mailboxes, customer lists, and traffic commitments. Seller represents authority to transfer; buyer assumes renewals after delivery. Failed delivery by the agreed date permits cancellation and return of funds under the escrow provider's documented process.",
                    ),
                    field(
                        "Commercial-email content requirements",
                        "textarea",
                        "Review outbound email under 15 U.S.C. § 7704 for accurate headers, nondeceptive subjects, required identification, a valid postal address, and a clear opt-out. Explain how the same requirements apply when a contractor sends messages for the operator.",
                        "A sample message uses the sender's real business identity and subject 'Domain name available for purchase.' It identifies the commercial offer, includes the operator's valid postal address, and offers a simple unsubscribe reply. It never claims a prior relationship, trademark ownership, traffic performance, or an approaching auction deadline without evidence.",
                    ),
                    field(
                        "Suppression and international outreach routing",
                        "textarea",
                        "Define how opt-outs are captured, shared with contractors, and applied before subsequent sends. Identify recipient jurisdictions requiring separate analysis, including consent-based regimes, and prohibit unsupported assumptions that United States email practices are universally sufficient for cross-border prospecting.",
                        "An opt-out enters the suppression register immediately, with processing completed within the CAN-SPAM limit of 10 business days. The mechanism remains available for at least 30 days after sending. Canadian prospects are held for CASL analysis under S.C. 2010, c. 23, section 6 before any campaign is authorized.",
                    ),
                    field(
                        "Entity, licensing, and tax fact pattern",
                        "textarea",
                        "Record the operator's entity, business location, inventory ownership, employee locations, and customer footprint. Identify applicable registration and tax questions without asserting that every domain investor needs a special trading license or that every sale has identical tax treatment.",
                        "The operator owns its inventory through one registered entity and works from one city. The checklist assigns review of local business registration, state tax classification of domain transfers, and income-tax treatment of inventory and renewals. IRC § 471 and applicable accounting rules are reviewed against the actual business facts.",
                    ),
                    field(
                        "Personal-data handling and evidence access",
                        "textarea",
                        "Describe what seller, buyer, and prospect information is collected, why it is necessary, who can access it, and when it is removed. Separate public domain research from private identity documents and payment records entrusted to transaction providers.",
                        "The portfolio register stores business contact details, contract identifiers, and transaction status, not passport scans or card numbers. Identity documents stay with the escrow provider where feasible. Contractors access only assigned prospects; retention is reviewed against contractual and statutory requirements, with GDPR Articles 5 and 6 assessed where applicable.",
                    ),
                    field(
                        "Claims audit and reviewer sign-off",
                        "textarea",
                        "Compare listings, landing pages, outbound copy, and contracts against the evidence packet. Flag statements about search visibility, trademark safety, past revenue, or likely appreciation that exceed documented facts, and assign correction ownership before the material is published.",
                        "The reviewer removes 'guaranteed first-page ranking' and replaces it with a factual description of the domain's wording and extension. Historical traffic is omitted because account-level evidence is unavailable. The signed checklist cites the retained support for every remaining performance claim and records the version approved for use.",
                    ),
                ],
                "completion_gate": (
                    "Publish or transact only after asset-specific trademark review, applicable dispute "
                    "analysis, documented contract terms, outreach suppression testing, and jurisdictional "
                    "operating checks are complete; unresolved material issues receive targeted specialist review."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Outbound Growth, and Risk Fallback Tracker",
                "purpose": (
                    "Automate repetitive portfolio administration without delegating uncontrolled bids, sensitive "
                    "registrar changes, or unsupported claims. Connect renewal monitoring, comparable-sale research, "
                    "inbound routing, and targeted upgrade outreach to accountable operators, measurable conversion, "
                    "auditable data quality, and manual fallbacks that preserve assets when integrations fail."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Choose one authoritative inventory register and assign stable identifiers before "
                        "connecting external services. Define field ownership, source timestamps, and "
                        "refresh schedules. A marketplace listing must not overwrite verified registrar "
                        "expiration data or a completed-sale status."
                    ),
                    (
                        "Automate renewal reminders using multiple lead times and a manual verification "
                        "queue. Test missed payments, stale API credentials, premium price changes, and "
                        "missing assets. An enabled auto-renew switch is useful evidence, but it is "
                        "not proof of payment."
                    ),
                    (
                        "Route inquiries by asset, buyer intent, price range, and dispute indicators. "
                        "Separate ordinary negotiation from impersonation or trademark complaints. "
                        "Require a person to approve binding prices and sensitive account actions "
                        "unless a narrowly defined mandate already authorizes them."
                    ),
                    (
                        "Build outbound lists around genuine naming upgrades and documented buyer fit. "
                        "Use small batches, truthful messages, and shared suppression controls. Measure "
                        "qualified replies and completed sales rather than rewarding message volume "
                        "or unverified email-open estimates."
                    ),
                    (
                        "For every integration, document the trigger, authorized action, failure "
                        "signal, responsible operator, and manual fallback. Run a tabletop outage "
                        "exercise before relying on automation for renewals, sale availability, "
                        "or delivery commitments that affect third parties."
                    ),
                ],
                "fields": [
                    field(
                        "Inventory system of record",
                        "textarea",
                        "Name the authoritative register, key fields, update permissions, and reconciliation process. Explain how registrar observations, marketplace listings, and operator decisions are merged without losing original evidence or allowing stale external records to reactivate sold inventory.",
                        "A SQLite register keys every asset by immutable asset ID and exact domain string. Registrar exports update observed expiration and status fields; only the owner changes disposition status. A sold flag cannot be cleared by marketplace import. Daily backups and a weekly restore test protect the register.",
                    ),
                    field(
                        "Renewal reminder ladder",
                        "textarea",
                        "Define reminder intervals, accountable recipients, escalation timing, and proof of successful renewal. Include premium renewal review and payment-method expiry checks so the automation detects both missing reminders and failed underlying payments before an asset enters an expensive recovery period.",
                        "Alerts fire at 90, 60, 30, 14, and 7 days before expiration. Premium renewals over $200 require an owner retention decision at 60 days. A paid invoice and refreshed registrar expiration close the task; an auto-renew setting alone leaves the renewal task open.",
                    ),
                    field(
                        "Comparable-sale monitoring pipeline",
                        "textarea",
                        "Describe permitted data sources, refresh frequency, normalization, and human validation. Keep asking prices separate from completed transactions, retain source references, and prevent one unusual sale or an unverified scraped record from automatically raising acquisition limits.",
                        "A weekly review imports permitted NameBio exports and manually verified marketplace records. The script normalizes extension, length, word count, and sale date while preserving the original row. Three comparable closed sales prompt a pricing review; the software never changes the acquisition ceiling or submits an auction bid.",
                    ),
                    field(
                        "Inbound inquiry classification",
                        "textarea",
                        "Define routing categories, response targets, minimum buyer information, and escalation conditions. Identify messages requiring a human before any reply, including disputes, suspicious payment instructions, purported ownership claims, and requests to disclose private seller or buyer information.",
                        "Ordinary purchase inquiries receive an acknowledgment within four business hours and route to the owner. A stated budget above $5,000 receives priority review. Trademark complaints, account-recovery requests, and changed payment instructions bypass automatic negotiation. The contractor sees the inquiry text but cannot release transfer codes or alter beneficiary details.",
                    ),
                    field(
                        "Outbound upgrade qualification",
                        "textarea",
                        "Specify observable reasons a prospect benefits from the name, the lawful source of contact information, and exclusion criteria. Separate genuine brand improvement from outreach that pressures a party by referencing its protected mark or implying exclusive rights.",
                        "A 30-prospect pilot targets independent firms with long generic descriptive domains and a clear public business contact route. Each record explains the pronunciation or brevity improvement in one sentence. Companies whose distinctive marks drive the candidate's value are excluded, and the list is checked against suppression records before sending.",
                    ),
                    field(
                        "Message experiment and offer discipline",
                        "textarea",
                        "Record the tested message, audience, offer price, follow-up interval, and stop conditions. Use factual product descriptions and realistic response expectations, avoiding invented scarcity, exaggerated search benefits, or automated sequences that continue after rejection or an opt-out.",
                        "The pilot offers the fictional name at $8,000 and explains its shorter spelling without claiming traffic. Fifteen prospects receive a concise naming-upgrade message and fifteen receive a pronunciation-focused version. One follow-up occurs after seven days; rejection or opt-out stops further contact immediately and updates the shared register.",
                    ),
                    field(
                        "Funnel metrics and attribution",
                        "textarea",
                        "Define denominators and event timestamps for delivered messages, positive replies, qualified negotiations, accepted offers, funded transactions, and completed sales. Attribute revenue only after the required closing event, and keep small-sample results distinct from reliable annual conversion assumptions.",
                        "A pilot sends 30 messages, records 28 deliveries, 4 positive replies, and 2 qualified negotiations. Positive replies equal 14.3% of deliveries; qualified negotiations equal 7.1%. With zero completed sales, revenue remains $0. An $8,000 verbal offer stays in pipeline and does not increase recognized proceeds.",
                    ),
                    field(
                        "Access scopes and action boundaries",
                        "textarea",
                        "List each integration's permissions, secret storage, rotation owner, and permitted actions. Separate research and notification automation from purchase commitments, registry changes, domain transfers, and outbound publication so a compromised component cannot exercise every operator privilege.",
                        "The renewal monitor receives read-only registrar access where supported and writes alerts to the task queue. The research script cannot access escrow or registrar secrets. Binding offers, purchases, and transfer releases remain manual. Tokens live in a password manager or deployment secret store, never in workbook examples or exported logs.",
                    ),
                    field(
                        "Integration outage and manual fallback",
                        "textarea",
                        "Define observable failure signals, alert destinations, recovery targets, and the manual procedure for each critical automation. Include stale data and partial success, not just total outages, because a silent missing asset can be more dangerous than a visible error.",
                        "If the registrar import is over 24 hours old or returns fewer than 420 expected assets, the owner receives an alert. The fallback is a direct registrar export and manual comparison of the next 60 days of expirations. New automated reminders are marked stale until reconciliation confirms complete coverage.",
                    ),
                    field(
                        "Experiment budget and scale decision",
                        "textarea",
                        "Set a bounded growth experiment budget, labor allowance, success threshold, and review date. Link any expansion to verified qualified demand and adequate renewal liquidity, rather than increasing acquisitions or outreach solely because the automation can process more records.",
                        "The 30-prospect pilot has a $300 diligence allocation and six owner hours, tracked inside the Base annual allowances rather than added invisibly. Expansion requires five qualified conversations across two batches and no unresolved suppression defects. New inventory purchases remain paused if cash falls below the renewal and operating reserve threshold.",
                    ),
                ],
                "completion_gate": (
                    "Activate the pipeline only after renewal alerts, inquiry routing, suppression, access "
                    "limits, data reconciliation, and manual outage procedures pass documented tests; scale "
                    "outreach only from qualified demand and funded operating capacity."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Pod Scorecard, and Exit-Readiness Ledger",
                "purpose": (
                    "Launch a disciplined domain operation in 30 days without pretending the first sale "
                    "must arrive within that window. Translate the canonical scorecard into accountable work, "
                    "cash controls, portfolio health measures, and transferable records that support a small "
                    "team or an eventual portfolio disposition."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Set the launch objective around operational readiness, screened inventory, "
                        "funded renewals, and tested transaction procedures. The stated first-deal "
                        "window is 3 to 24 months; a 30-day sprint must not rely on immediate "
                        "sales to meet unavoidable payments."
                    ),
                    (
                        "Assign every recurring task to an accountable person and define backup "
                        "coverage. Use the canonical staffing patterns as capacity references, then "
                        "test actual labor commitments against the operating budget before hiring "
                        "or promising availability the team cannot provide."
                    ),
                    (
                        "Review leading and lagging metrics separately each week. Track clean "
                        "underwriting packets, qualified inquiries, funded transactions, completed "
                        "sales, renewal coverage, and unrestricted cash. Do not treat portfolio "
                        "asking prices as realized revenue or proof of liquidity."
                    ),
                    (
                        "Prepare transfer-ready records as the portfolio grows rather than reconstructing "
                        "them during an exit. Maintain ownership evidence, cost basis, registrar "
                        "restrictions, disputes, renewal liabilities, and listing status. Restrict "
                        "buyer diligence access to information necessary for the proposed transaction."
                    ),
                    (
                        "At day 30, compare completed work with the written launch criteria and "
                        "record exceptions openly. Continue, narrow the acquisition lane, or stop "
                        "new purchases based on evidence and cash. Preserve the canonical scenarios "
                        "separately from the actual operating forecast."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical position and launch objective",
                        "textarea",
                        "Record the candidate identity, pipeline rank, score breakdown, capital range, operating range, and first-deal window. Translate the positioning into a practical launch objective without treating the score as evidence of market liquidity or a predicted investment return.",
                        "Candidate #16, Domain Investing, ranks #17 of 29 and scores 74/100: revenue 17, margin 18, team efficiency 19, accessibility 9, automation 11. Positioning is Disciplined Specialist Play. Launch assumptions retain $10,000–$150,000 startup capital, $500–$5,000 monthly operating costs, and 3–24 months to the first deal.",
                    ),
                    field(
                        "Days 1 through 7: foundation deliverables",
                        "textarea",
                        "List first-week deliverables, responsible people, evidence locations, and explicit completion tests. Prioritize inventory governance, registrar security, scenario reconciliation, and legal screening procedures before spending the available acquisition budget on attractive names that lack a documented thesis.",
                        "By day 7, the owner configures secured registrar access, an asset register, and a $50,000 cash plan. The contractor completes ten research packets with no purchases. Completion requires tested backup recovery, exact canonical scenario reconciliation, a trademark-screen template, and a funded renewal-reserve rule recorded in the operating log.",
                    ),
                    field(
                        "Days 8 through 14: underwriting and purchase discipline",
                        "textarea",
                        "Define second-week research volume, rejection criteria, acquisition limits, and seller-verification requirements. Keep the milestone focused on decision quality rather than forcing a purchase, and specify how auction enthusiasm will be constrained by the approved cash and bid ceilings.",
                        "By day 14, review 25 candidates, complete five full packets, and authorize at most two purchases below $3,000 each all-in. Any unresolved ownership issue or relevant trademark conflict rejects the candidate. A week with zero qualifying purchases still passes if evidence quality and rejection records meet the standard.",
                    ),
                    field(
                        "Days 15 through 21: transaction and outreach rehearsal",
                        "textarea",
                        "Plan the third-week dry runs for listing synchronization, inquiry routing, escrow verification, transfer evidence, and targeted outreach. Identify which tests can use synthetic records and which actions require a real counterparty's explicit agreement before they occur.",
                        "By day 21, run a synthetic $8,000 sale through the ledger without moving money or changing a real domain. Test suppression with internal addresses, rehearse a registrar outage, and prepare the 30-prospect pilot. Publishing listings or contacting prospects begins only under the owner's explicit operating authorization.",
                    ),
                    field(
                        "Days 22 through 30: readiness review",
                        "textarea",
                        "Define final-week deliverables, acceptance criteria, unresolved-issue reporting, and the next operating cycle. Measure launch readiness using completed controls and funded obligations while keeping real inquiries and completed sales visible as separate, nonmandatory outcomes of the sprint.",
                        "By day 30, every acquired asset has title evidence, renewal coverage, a price thesis, and a tested transfer route. The owner reviews pilot replies and all cash commitments. A launch with zero sales remains viable only if the documented holding runway is funded and no critical ownership or security exceptions remain.",
                    ),
                    field(
                        "Pod roles and labor cost ownership",
                        "textarea",
                        "Assign acquisition, research, renewal, negotiation, transfer, and bookkeeping responsibilities across the stated team. Define FT and C consistently, identify backup coverage, and reconcile paid labor commitments to the selected cost allocation rather than treating headcount as free operating capacity.",
                        "Conservative and Base use 1 full-time operator plus 1 contractor; Scaled uses 2 full-time operators plus 2 contractors, four people total. The owner handles pricing and transfers, while the contractor researches and reconciles. Scaled adds coverage, but actual compensation must fit a documented forecast; the labels alone do not fund salaries.",
                    ),
                    field(
                        "Weekly KPI scorecard",
                        "textarea",
                        "Define each metric, source, owner, review cadence, and intervention threshold. Include inventory aging, qualified inquiries, completed sales, realized prices, renewal coverage, and unrestricted runway, with clear denominators that prevent misleading percentages from small or changing samples.",
                        "Friday review shows 420 owned domains, 38 expiring within 90 days, 6 qualified inquiries, 2 active negotiations, and zero completed sales that week. Renewal funding coverage must remain 100% for retained assets. Runway equals unrestricted cash divided by current monthly recurring burn; below three months suspends new purchases.",
                    ),
                    field(
                        "Actual-versus-canonical profit ledger",
                        "textarea",
                        "Compare actual gross proceeds, realized costs, owner profit, and cash movements with the selected reference case. Explain timing differences, separate owner distributions from operating costs, and preserve the original scenario values even when actual performance requires a different forecast.",
                        "The Base reference remains $160,000 revenue, $116,000 costs, and $44,000 annual owner net profit. At quarter end, actual completed sales total $24,000 with $19,000 recorded costs, producing $5,000 operating profit on the adopted basis. Inventory purchases and owner distributions appear separately in the cash bridge; no annualization is presented as achieved results.",
                    ),
                    field(
                        "Exit data room and portfolio valuation",
                        "textarea",
                        "List buyer-diligence records, access restrictions, valuation methods, renewal liabilities, and transfer constraints. Distinguish retail asking value from executable wholesale offers, and quantify net sale cash only after fees and retained obligations are deducted from a documented offer.",
                        "A restricted data room contains ownership evidence, basis schedules, expiration dates, disputes, and registrar restrictions, but no passwords or transfer codes. An illustrative $60,000 portfolio offer less $6,000 selling costs and $4,000 seller-retained obligations yields $50,000 cash. A $400,000 sum of retail asking prices is not substituted for that executable offer.",
                    ),
                    field(
                        "Continue, narrow, or exit decision",
                        "textarea",
                        "Write the day-30 decision using evidence quality, available cash, buyer response, operational reliability, and unresolved exposure. Identify the next review date and measurable conditions for expansion, acquisition suspension, selective liquidation, or a complete portfolio sale.",
                        "Decision: continue research but suspend acquisitions until unrestricted cash exceeds three months of recurring burn after reserve funding. Retain only names with documented buyer demand and renewal support. Revisit in 30 days; expansion requires clean transfer tests, no unresolved material disputes, and qualified conversations rather than a higher portfolio asking-price total.",
                    ),
                ],
                "completion_gate": (
                    "Complete the sprint when all six worksheets are signed, every owned asset has "
                    "traceable title and funded retention, actual results reconcile to the ledger, "
                    "team costs are supportable, and the next 30-day decision has explicit cash "
                    "thresholds, accountable owners, and a dated review."
                ),
            },
        ],
    }
