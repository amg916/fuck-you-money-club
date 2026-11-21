from __future__ import annotations


def build_volume_024_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-024-tax-lien-investing",
        "volume_id": "vol-024-tax-lien-investing",
        "title": "Tax Lien Investing — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Certificate and Redeemable-Deed "
            "Underwriting, Auction Bid-Down Math, Capital Reserves, Statutory "
            "Execution, Redemption Tracking, and Small-Team Portfolio Control"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Opportunity Underwriting and Counterparty Qualification",
                "purpose": (
                    "Build an evidence-backed acquisition thesis before committing "
                    "capital. Distinguish tax certificates from redeemable deeds, "
                    "qualify the selling authority and payment destination, and "
                    "reject parcels whose title, access, environmental exposure, "
                    "or recovery economics cannot support a defensible downside case."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Select one certificate jurisdiction and one comparison "
                        "jurisdiction. Retrieve current statutes, county auction "
                        "terms, redemption instructions, and bidder registration "
                        "requirements directly from official sources; record the "
                        "retrieval date and responsible reviewer beside each document."
                    ),
                    (
                        "Separate the security being purchased from the underlying "
                        "real estate. Identify whether the auction transfers a "
                        "certificate, a redeemable deed, or another interest, then "
                        "write the actual enforcement path rather than assuming "
                        "immediate ownership or occupancy."
                    ),
                    (
                        "Underwrite each parcel using assessor records, recorded "
                        "instruments, mapping, tax history, and a documented title "
                        "search. Treat apparent discounts as questions requiring "
                        "evidence, especially where access, structures, liens, "
                        "ownership disputes, or contamination could impair recovery."
                    ),
                    (
                        "Independently authenticate the auction administrator and "
                        "settlement account before funding. Call a published county "
                        "number rather than a number supplied in a payment email, "
                        "and retain the verification record with the proposed bid."
                    ),
                    (
                        "Apply exposure limits to the complete economic interest, "
                        "including required subsequent taxes and enforcement "
                        "funding. Rank approved candidates by evidence quality, "
                        "capital duration, and downside recovery, then document "
                        "specific reasons for every rejected parcel."
                    ),
                ],
                "fields": [
                    field(
                        "Investment mandate and capacity boundary",
                        "textarea",
                        (
                            "Define the permitted instruments, geography, cash "
                            "commitment, staffing capacity, and expected waiting "
                            "period. Explain which opportunities remain outside "
                            "the mandate even when their advertised statutory "
                            "return appears attractive to a new bidder."
                        ),
                        (
                            "The pilot permits Florida tax certificates and "
                            "separately reviewed Texas redeemable deeds, with "
                            "$125,000 committed capital and no occupied-property "
                            "management. Volume 024 ranks #24 of 29 and scores "
                            "62/100. Budget one full-time operator plus two "
                            "contractors; retain the canonical 6–36 month "
                            "first-deal planning window."
                        ),
                    ),
                    field(
                        "Instrument classification and ownership rights",
                        "textarea",
                        (
                            "Describe the exact interest conveyed, the document "
                            "evidencing ownership, the redemption mechanism, and "
                            "the next lawful enforcement step. Identify rights "
                            "the investor does not receive merely by winning "
                            "the auction or paying the purchase amount."
                        ),
                        (
                            "A Florida certificate evidences a tax lien, not "
                            "a right to enter the residence or collect rent. "
                            "A Texas tax-sale deed conveys a different interest "
                            "subject to applicable redemption rights. The file "
                            "therefore uses separate certificate and deed "
                            "checklists, custody records, and possession "
                            "instructions rather than one generic foreclosure script."
                        ),
                    ),
                    field(
                        "Auction authority and settlement verification",
                        "textarea",
                        (
                            "Identify the public seller, auction platform, "
                            "registration requirements, deposit treatment, and "
                            "authorized payment destination. Specify how the "
                            "operator will independently confirm account changes "
                            "and preserve evidence before sending an irreversible "
                            "wire or other settlement payment."
                        ),
                        (
                            "The operator finds the auction link through the "
                            "county tax collector's official website and calls "
                            "the published office number to confirm settlement "
                            "instructions. A second reviewer checks the account "
                            "beneficiary and $5,000 deposit credit. Any emailed "
                            "account substitution suspends funding until the "
                            "county independently confirms the change."
                        ),
                    ),
                    field(
                        "Parcel identity and collateral triangulation",
                        "textarea",
                        (
                            "Reconcile the parcel identifier, legal description, "
                            "street reference, assessed improvements, and mapped "
                            "boundaries. Describe how conflicting records will "
                            "be resolved before bidding, including narrow "
                            "strips, common areas, landlocked parcels, and "
                            "separately assessed mineral interests."
                        ),
                        (
                            "Parcel FL-PILOT-017 shows an $82,000 assessed value, "
                            "but the auction description excludes the adjoining "
                            "house lot. QGIS mapping reveals a narrow drainage "
                            "tract with no recorded access. The analyst rejects "
                            "the $4,600 certificate because the apparent "
                            "collateral value belongs largely to a different "
                            "legal description."
                        ),
                    ),
                    field(
                        "Title stack and competing claims",
                        "textarea",
                        (
                            "List recorded owners, mortgages, federal claims, "
                            "judgments, easements, bankruptcy indicators, and "
                            "other interests requiring review. Distinguish "
                            "priority from extinguishment, and identify which "
                            "searches must be refreshed before enforcement "
                            "or any eventual property disposition."
                        ),
                        (
                            "A $12,000 certificate is secured by a parcel "
                            "with a $140,000 mortgage and a recorded federal "
                            "tax lien. Mortgage size alone does not decide "
                            "tax-lien priority, but federal notice and "
                            "redemption issues require review under 26 U.S.C. "
                            "7425. The investor withholds a bid until counsel "
                            "maps surviving interests and procedures."
                        ),
                    ),
                    field(
                        "Environmental and physical downside screen",
                        "textarea",
                        (
                            "Identify prior uses, physical deterioration, "
                            "demolition exposure, flood conditions, and "
                            "environmental indicators that could make ownership "
                            "uneconomic. State what evidence is needed before "
                            "moving from a passive certificate position "
                            "toward acquiring or controlling the property."
                        ),
                        (
                            "A former dry-cleaning parcel supports a $9,000 "
                            "tax claim but carries solvent-release indicators "
                            "in state records. Acquisition could create "
                            "exposure under 42 U.S.C. 9607. The operator "
                            "declines the pilot purchase rather than treating "
                            "the lien amount as the maximum possible loss; "
                            "future ownership review would address 40 CFR Part 312."
                        ),
                    ),
                    field(
                        "Redemption evidence and duration thesis",
                        "textarea",
                        (
                            "Build a redemption thesis from observable county "
                            "records rather than owner stereotypes or "
                            "unsupported payment predictions. Separate "
                            "historical cohort behavior from a promise about "
                            "one parcel, and show how slower recovery "
                            "changes available acquisition cash."
                        ),
                        (
                            "A reviewed county sample contains 120 comparable "
                            "certificates: 78 redeemed within twelve months, "
                            "24 during months thirteen through twenty-four, "
                            "and 18 remained open at the cutoff. Those "
                            "observations inform liquidity scenarios only. "
                            "The $100,000 pilot remains fundable if its "
                            "unredeemed balance persists for thirty months."
                        ),
                    ),
                    field(
                        "Concentration and correlated exposure limits",
                        "textarea",
                        (
                            "Set maximum exposure by parcel, owner group, "
                            "county, property type, and hazard cluster. Include "
                            "unsettled wins and required future advances "
                            "when testing limits so simultaneous auctions "
                            "cannot quietly exceed the approved capital "
                            "or geographic risk budget."
                        ),
                        (
                            "The $100,000 deployment budget permits at most "
                            "$10,000 per parcel, $15,000 per related owner "
                            "group, and $40,000 per county. A proposed "
                            "$8,000 certificate fails because existing and "
                            "unsettled exposure to the same owner already "
                            "equals $11,000. Separate parcels do not reset "
                            "the beneficial-owner concentration limit."
                        ),
                    ),
                    field(
                        "Bid ceiling and walk-away rationale",
                        "textarea",
                        (
                            "Translate the downside case into an auction "
                            "instruction appropriate to the bidding mechanism. "
                            "For interest bid-down auctions, state a minimum "
                            "acceptable rate; for price auctions, state "
                            "a maximum cash bid including reserves "
                            "and expected execution costs."
                        ),
                        (
                            "For a $10,000 Florida certificate, the desk "
                            "will not bid below 8% because the approved "
                            "nine-month illustration yields $600 gross "
                            "interest before $100 of direct costs. For "
                            "a Texas deed, a separate $24,000 maximum "
                            "purchase bid leaves cash for recording, "
                            "subsequent taxes, and the reviewed downside case."
                        ),
                    ),
                    field(
                        "Investment decision and evidence owner",
                        "textarea",
                        (
                            "Record the final acquire, watch, or reject "
                            "decision with dated evidence, unresolved "
                            "conditions, and a named role responsible "
                            "for clearing each condition. Preserve rejected "
                            "opportunities so repeated auctions do not "
                            "erase prior defect discoveries."
                        ),
                        (
                            "FL-PILOT-022 enters the approved list at an "
                            "8% minimum bid rate after parcel identity, "
                            "title exceptions, and settlement instructions "
                            "are checked. The title contractor owns a "
                            "final bankruptcy refresh before enforcement. "
                            "FL-PILOT-017 remains rejected for access and "
                            "description defects; a lower auction price "
                            "does not remove those defects."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when every approved parcel has a verified "
                    "instrument type, authenticated settlement route, documented "
                    "downside case, exposure-limit check, and signed bid instruction."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Defect Reserve, and Working-Capital Float",
                "purpose": (
                    "Convert auction terms into cash-flow arithmetic without "
                    "counting returned capital as revenue. Reconcile the three "
                    "canonical scenarios, distinguish reserve earmarks from "
                    "actual losses, and determine whether operating cash can "
                    "support delayed redemptions, required advances, and "
                    "property-disposition costs."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the canonical revenue, margin, profit, and team "
                        "figures before adding any deal assumptions. Maintain "
                        "a separate deployment schedule because an invested "
                        "dollar returning to the bank is recovered capital, "
                        "not newly earned operator revenue."
                    ),
                    (
                        "Calculate each certificate or deed using its own "
                        "statutory mechanism. Document interest periods, "
                        "redemption minimums, eligible penalty bases, and "
                        "auction increments; do not convert a flat statutory "
                        "penalty into annual interest or apply one state's "
                        "formula elsewhere."
                    ),
                    (
                        "Build a cash waterfall showing purchase capital, "
                        "fees, subsequent advances, redemption receipts, "
                        "basis recovery, and earned amounts. Keep county "
                        "collection charges separate from investor proceeds "
                        "unless the actual settlement statement establishes "
                        "that the investor receives them."
                    ),
                    (
                        "Create separate schedules for spendable operating "
                        "cash, earmarked defect reserves, realized losses, "
                        "and accounting adjustments. A reserve transfer "
                        "does not automatically create an expense, while "
                        "an actual impairment requires its own documented "
                        "measurement and recognition decision."
                    ),
                    (
                        "Stress the portfolio for slower collections, "
                        "unusable collateral, and higher enforcement costs. "
                        "Reduce new bids before assuming additional capital "
                        "will appear, then reconcile the revised cash "
                        "balance to the bank and all unsettled auction "
                        "commitments at least weekly."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical scenario reconciliation",
                        "textarea",
                        (
                            "Record all three canonical annual cases with "
                            "recognized revenue, net margin, owner net "
                            "profit, and team capacity. Explain the "
                            "base-case rounding convention and identify "
                            "returned capital as an excluded amount "
                            "rather than a fourth revenue component."
                        ),
                        (
                            "Conservative: $15,000 revenue, 30% margin, "
                            "$4,500 owner profit, 1 FT + 2 C. Base: "
                            "$97,500 revenue, 42.5% margin, $41,438 rounded "
                            "owner profit, 1 FT + 2 C. Scaled: $180,000 "
                            "revenue, 55% margin, $99,000 owner profit, "
                            "2 FT + 3 C. Base arithmetic produces "
                            "$41,437.50 before whole-dollar rounding."
                        ),
                    ),
                    field(
                        "Annual expense bridge and staffing interpretation",
                        "textarea",
                        (
                            "Reconcile annual operating and direct costs "
                            "to each scenario's required total expense. "
                            "Explain whether staffing counts describe "
                            "working capacity or fully salaried positions, "
                            "and avoid presenting owner profit as "
                            "both wages and residual earnings."
                        ),
                        (
                            "Conservative costs total $10,500: $6,000 recurring "
                            "opex plus $4,500 direct costs and losses. "
                            "Base costs total $56,062.50: $24,000 plus "
                            "$32,062.50. Scaled costs total $81,000: "
                            "$48,000 plus $33,000. These illustrative "
                            "allocations reconcile the canon; team counts "
                            "describe capacity, not a promise that these "
                            "budgets fund market-rate employee salaries."
                        ),
                    ),
                    field(
                        "Deployment cohorts and recognized revenue boundary",
                        "textarea",
                        (
                            "Show how a completed collection cohort "
                            "supports the annual revenue scenario. Separate "
                            "recovered certificate principal or disposition "
                            "basis from realized interest, penalties, and "
                            "gains, and distinguish this arithmetic "
                            "from a forecast of portfolio-wide yield."
                        ),
                        (
                            "Illustrative completed cohorts recover $100,000, "
                            "$650,000, and $1,200,000 of capital while "
                            "earning $15,000, $97,500, and $180,000 "
                            "respectively. Corresponding receipts are "
                            "$115,000, $747,500, and $1,380,000. The "
                            "15% ratios describe these selected cohorts, "
                            "not annualized returns on every outstanding "
                            "asset or a single state's certificate rate."
                        ),
                    ),
                    field(
                        "Certificate bid-down and redemption calculation",
                        "textarea",
                        (
                            "Calculate a certificate's gross earned amount "
                            "under the actual bid rate and statutory "
                            "period rules. Show the applicable redemption "
                            "minimum separately, test a zero-rate bid, "
                            "and subtract investor-paid costs before "
                            "describing deal-level contribution."
                        ),
                        (
                            "Using nine statutory months, a $10,000 Florida "
                            "certificate bid at 8% earns $600. The "
                            "5% minimum would be $500, so $600 controls "
                            "under this simplified fact pattern. At "
                            "6%, $450 becomes $500; a zero-rate "
                            "certificate does not receive that minimum. "
                            "Review Fla. Stat. 197.172 and 197.472(2)."
                        ),
                    ),
                    field(
                        "Redeemable-deed penalty base and timing",
                        "textarea",
                        (
                            "Identify the deed's property classification, "
                            "redemption period, eligible reimbursement "
                            "components, and statutory premium. Calculate "
                            "the amount from the qualified base rather "
                            "than applying a headline percentage to "
                            "unrelated legal expenses or an invented "
                            "annual interest balance."
                        ),
                        (
                            "For a qualifying Texas homestead redemption "
                            "during the first year, assume a $24,000 "
                            "purchase bid, $100 recording fee, and "
                            "$900 of qualifying taxes paid. The "
                            "$25,000 statutory aggregate produces a "
                            "$6,250 premium at 25%, for $31,250 "
                            "total redemption payment under Tex. Tax "
                            "Code 34.21; the premium is not an APR."
                        ),
                    ),
                    field(
                        "Deal cash waterfall and deployable balance",
                        "textarea",
                        (
                            "Prepare a complete before-and-after cash "
                            "reconciliation for one purchase. Include "
                            "direct costs and untouched reserve cash, "
                            "then show exactly which receipt amount "
                            "is principal recovery and which amount "
                            "is earned contribution after those costs."
                        ),
                        (
                            "Starting cash is $10,400. Pay $10,000 "
                            "for the certificate and $100 in direct "
                            "costs, leaving $300 reserved. Redemption "
                            "returns $10,600: $10,000 principal plus "
                            "$600 interest. Ending cash is $10,900; "
                            "the $500 increase is contribution after "
                            "costs. Keeping $300 reserved changes "
                            "spendable cash, not the $500 result."
                        ),
                    ),
                    field(
                        "Scrub losses and defect reserve policy",
                        "textarea",
                        (
                            "Set a cash reserve using exposure and "
                            "defect severity, then distinguish it from "
                            "screening expense and realized capital loss. "
                            "Explain when an adverse title finding "
                            "causes rejection, a valuation review, "
                            "or a documented charge to results."
                        ),
                        (
                            "The base portfolio earmarks 3% of $650,000, "
                            "or $19,500, within its existing $150,000 "
                            "liquidity allocation. The earmark is not "
                            "an added expense. Base direct costs "
                            "include $18,000 contractor work, $9,600 "
                            "title work, and $4,462.50 realized losses, "
                            "totaling $32,062.50; losses require "
                            "asset-specific recovery evidence."
                        ),
                    ),
                    field(
                        "Startup capital and operating runway",
                        "textarea",
                        (
                            "Allocate initial capital between investments "
                            "and liquid support without exceeding the "
                            "canonical startup range. Test monthly opex "
                            "against the stated range and identify "
                            "which legal, tax, or contractor commitments "
                            "will shorten the apparent cash runway."
                        ),
                        (
                            "Illustrative startup allocations are $125,000 "
                            "with $100,000 deployed, $800,000 with "
                            "$650,000 deployed, and $1,500,000 with "
                            "$1,200,000 deployed. Monthly recurring "
                            "opex is $500, $2,000, and $4,000. "
                            "All fit the canonical ranges. Liquid "
                            "balances also fund direct costs and "
                            "advances, so dividing cash only by "
                            "monthly opex overstates usable runway."
                        ),
                    ),
                    field(
                        "Delayed redemption and enforcement stress",
                        "textarea",
                        (
                            "Model a collection delay using cash "
                            "commitments rather than merely reducing "
                            "an expected yield. Identify the reserve "
                            "floor, extra carrying period, enforcement "
                            "budget, and resulting reduction in new "
                            "bids before assuming external funding "
                            "will cover the shortfall."
                        ),
                        (
                            "Base liquid cash is $150,000, including "
                            "$19,500 earmarked for defects. A twelve-month "
                            "delay consumes $24,000 recurring opex; "
                            "planned enforcement requires another "
                            "$30,000. After those commitments and "
                            "the reserve floor, only $76,500 remains "
                            "uncommitted before other direct costs. "
                            "The desk cancels a proposed $90,000 "
                            "auction allocation rather than borrowing implicitly."
                        ),
                    ),
                    field(
                        "Disposition gain and owner-profit bridge",
                        "textarea",
                        (
                            "Calculate recognized disposition gain from "
                            "net proceeds and documented carrying basis. "
                            "Prevent selling costs from being deducted "
                            "twice, and explain how deal-level results "
                            "feed annual owner profit without treating "
                            "the property's entire sale price "
                            "as operator revenue."
                        ),
                        (
                            "A property sells for $170,000 with $2,500 "
                            "selling costs and $150,000 documented "
                            "basis. Net proceeds of $167,500 recover "
                            "$150,000 capital and produce $17,500 "
                            "gain. Pairing that gain with $30,000 "
                            "realized interest and $50,000 penalties "
                            "reconciles base gross revenue to $97,500; "
                            "do not deduct the $2,500 again."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when all three canonical cases reconcile, "
                    "base rounding is explicit, principal is excluded from "
                    "revenue, and the stressed cash schedule funds every "
                    "committed payment without double-counting reserves."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Execution, Asset Ledger, and Technical QA Pre-Flight",
                "purpose": (
                    "Translate an approved bid into an auditable asset record "
                    "from registration through final recovery. Establish "
                    "transaction identifiers, document custody, deadline "
                    "controls, bank reconciliation, and technical checks "
                    "that prevent duplicate funding, missing certificates, "
                    "misclassified receipts, and premature enforcement."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Create a lifecycle record before registering a bid. "
                        "Use explicit states for screened, approved, bid, "
                        "won, funded, issued, redeemed, enforcement review, "
                        "and closed, with a documented reason and "
                        "responsible role for every transition."
                    ),
                    (
                        "Reconcile the auction award against the approved "
                        "instruction before paying. Check parcel identity, "
                        "certificate amount, rate, premium where relevant, "
                        "deposit credit, and settlement cutoff; stop any "
                        "payment whose economic terms differ from the "
                        "authorized bid record."
                    ),
                    (
                        "Store certificate evidence, deed records, title "
                        "searches, notices, and county statements under "
                        "stable asset identifiers. Preserve original files "
                        "and retrieval metadata so later corrections "
                        "cannot silently replace the evidence supporting "
                        "an earlier investment or statutory decision."
                    ),
                    (
                        "Separate asset accounting from operational alerts. "
                        "An approaching deadline should create a review "
                        "task, not an automatic filing or owner demand; "
                        "each consequential action needs confirmed facts, "
                        "current procedural requirements, and a documented "
                        "authorized reviewer."
                    ),
                    (
                        "Run calculation, reconciliation, access-control, "
                        "and recovery tests before live use. Use synthetic "
                        "records for technical QA, then compare sample "
                        "real assets against county evidence without "
                        "assuming that a successful import proves "
                        "the underlying records are correct."
                    ),
                ],
                "fields": [
                    field(
                        "Lifecycle states and transition evidence",
                        "textarea",
                        (
                            "Define allowed asset states and the "
                            "evidence required to move between them. "
                            "Specify which transitions can be performed "
                            "by an analyst and which require "
                            "settlement, legal, or accounting review "
                            "before the operational record changes."
                        ),
                        (
                            "Asset FL-2027-022 moves from approved to "
                            "won only after the county award matches "
                            "its 8% instruction. Funded requires bank "
                            "confirmation; issued requires certificate "
                            "evidence. A calendar reminder may move "
                            "the asset to enforcement review, but "
                            "only documented legal review authorizes "
                            "the next application or filing step."
                        ),
                    ),
                    field(
                        "Stable identifiers and duplicate protection",
                        "textarea",
                        (
                            "Design identifiers that distinguish the "
                            "same parcel across tax years, auctions, "
                            "certificates, and ownership interests. "
                            "Explain how repeated downloads and "
                            "payment retries will be recognized "
                            "without merging separate assets or "
                            "sending money twice to the seller."
                        ),
                        (
                            "The ledger key combines state, county, "
                            "instrument class, tax year, and county "
                            "certificate number. Parcel identity remains "
                            "a separate linked attribute. Two imported "
                            "rows for certificate 2027-004812 trigger "
                            "a duplicate exception; a 2028 certificate "
                            "on the same parcel remains distinct. "
                            "A settlement reference can attach to "
                            "only one funded transaction."
                        ),
                    ),
                    field(
                        "Award verification and settlement worksheet",
                        "textarea",
                        (
                            "Reconcile the approved bid, official "
                            "award, deposit, and remaining settlement "
                            "amount. Capture payment deadlines with "
                            "time zones and define the independent "
                            "checks required before releasing funds "
                            "or accepting a changed county instruction."
                        ),
                        (
                            "Three awarded certificates total $27,500 "
                            "and the county applies a $5,000 "
                            "deposit, leaving $22,500 due. The "
                            "reviewer confirms that each rate equals "
                            "or exceeds its approved floor and "
                            "that the deadline is 3:00 p.m. "
                            "Eastern on the stated date. The "
                            "bank instruction carries the county's "
                            "verified settlement reference."
                        ),
                    ),
                    field(
                        "Asset subledger and document custody",
                        "textarea",
                        (
                            "Specify the minimum fields needed to "
                            "reconstruct ownership, carrying basis, "
                            "statutory terms, and document history. "
                            "Keep original evidence accessible while "
                            "recording corrections as new versions "
                            "rather than silently overwriting "
                            "the record used to approve acquisition."
                        ),
                        (
                            "Each record stores purchase amount, "
                            "investor-paid fees, issued rate, "
                            "instrument date, county identifier, "
                            "recording reference, and source-document "
                            "checksum. A corrected owner spelling "
                            "creates version two while preserving "
                            "version one. The deed image and "
                            "certificate receipt are separate document "
                            "types; possession of an auction "
                            "screenshot alone does not establish issuance."
                        ),
                    ),
                    field(
                        "Redemption receipt allocation",
                        "textarea",
                        (
                            "Define how county receipts are matched "
                            "to assets and split between returned "
                            "capital, earned amounts, and other "
                            "adjustments. Include an exception route "
                            "for bundled remittances, partial payments, "
                            "or receipts that disagree with "
                            "the county's detailed settlement record."
                        ),
                        (
                            "A $31,800 remittance covers three assets: "
                            "$30,000 principal and $1,800 interest "
                            "according to the county statement. "
                            "The ledger closes those certificate "
                            "balances and records only $1,800 "
                            "as revenue. An unmatched $40 bank "
                            "difference stays in a reconciliation "
                            "exception account pending evidence; "
                            "it is not forced into interest income."
                        ),
                    ),
                    field(
                        "Statutory calendar and deadline ownership",
                        "textarea",
                        (
                            "List the triggering event, source "
                            "provision, calculated date, local "
                            "procedural conditions, and reviewer "
                            "for each deadline. Distinguish "
                            "eligibility to begin a process "
                            "from expiration, redemption cutoff, "
                            "notice service, and the date "
                            "a court may actually act."
                        ),
                        (
                            "For Florida certificates, the calendar "
                            "tracks the tax-deed application framework "
                            "in Fla. Stat. 197.502 and the "
                            "certificate-expiration rules in 197.482. "
                            "The reviewer verifies the relevant "
                            "April 1 reference and any exceptions. "
                            "Alerts occur 180, 90, and 30 "
                            "days before the reviewed deadline; "
                            "none automatically files a tax-deed application."
                        ),
                    ),
                    field(
                        "Interest engine and rounding tests",
                        "textarea",
                        (
                            "Describe test cases for statutory "
                            "period counting, minimum returns, "
                            "zero-rate purchases, money precision, "
                            "and rounding. Identify the official "
                            "record used to resolve disagreements "
                            "rather than treating an internal "
                            "spreadsheet as the final redemption "
                            "payoff authority."
                        ),
                        (
                            "Python decimal-based tests cover $10,000 "
                            "at 8% for nine statutory months "
                            "equaling $600, and 6% equaling "
                            "$450 before the Florida minimum "
                            "test. A zero-rate fixture expects "
                            "zero certificate interest. Whole-dollar "
                            "scenario presentation uses ROUND_HALF_UP "
                            "so $41,437.50 displays as $41,438. "
                            "Actual payoff differences require county "
                            "statement review."
                        ),
                    ),
                    field(
                        "Bank reconciliation and cash availability",
                        "textarea",
                        (
                            "Reconcile bank cash to funded assets, "
                            "unsettled commitments, operating payments, "
                            "and reserve earmarks. Show which "
                            "balance controls bidding and explain "
                            "how pending deposits or unconfirmed "
                            "redemption notices are excluded "
                            "from immediately spendable cash."
                        ),
                        (
                            "The bank holds $82,000. Subtract "
                            "$22,500 unsettled awards, $12,000 "
                            "scheduled operating and title payments, "
                            "and a $19,500 reserve floor "
                            "to obtain $28,000 available for "
                            "additional commitments. A county "
                            "email announcing a $15,000 "
                            "redemption does not increase that "
                            "amount until the funds settle "
                            "and the asset allocation is verified."
                        ),
                    ),
                    field(
                        "Exception escalation and payment suspension",
                        "textarea",
                        (
                            "Define severity levels for parcel "
                            "mismatches, missing issuance evidence, "
                            "rate discrepancies, suspected account "
                            "substitution, and deadline errors. "
                            "Assign a response time and "
                            "a specific action that remains "
                            "suspended until the responsible "
                            "reviewer resolves the exception."
                        ),
                        (
                            "A deed referencing a different "
                            "legal description is a critical "
                            "exception: suspend further advances "
                            "and obtain county and title "
                            "review immediately. A $12 "
                            "rounding discrepancy is investigated "
                            "within two business days. Both "
                            "remain visible in the ledger; "
                            "neither is cleared merely because "
                            "a dashboard's overall asset count "
                            "still matches."
                        ),
                    ),
                    field(
                        "Pre-flight acceptance and recovery drill",
                        "textarea",
                        (
                            "Define the evidence proving that "
                            "the operational system can "
                            "reconstruct balances and deadlines "
                            "after an error or outage. "
                            "Include restore testing, limited "
                            "access rights, sample document "
                            "retrieval, and end-to-end reconciliation "
                            "before the first live acquisition."
                        ),
                        (
                            "The reviewer restores yesterday's "
                            "encrypted SQLite backup into an "
                            "isolated workspace and reproduces "
                            "all 25 synthetic assets, their "
                            "document references, and $250,000 "
                            "aggregate principal. A read-only "
                            "analyst cannot alter settlement "
                            "instructions. Five sampled redemption "
                            "fixtures reconcile exactly, and "
                            "a missing source document blocks "
                            "the associated state transition."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only after award-to-bank reconciliation, "
                    "document retrieval, duplicate detection, statutory-date "
                    "review, calculation fixtures, and backup restoration "
                    "pass with recorded results and assigned exception owners."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract, and Outreach Audit",
                "purpose": (
                    "Turn jurisdiction-specific rules into explicit operating "
                    "requirements. Review bidder eligibility, rate limits, "
                    "redemption rights, notice procedures, bankruptcy, "
                    "servicemember protections, federal claims, and surplus "
                    "handling before any enforcement activity, while keeping "
                    "contracts and owner communications within the actual "
                    "rights acquired."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Build a jurisdiction matrix from current statutory "
                        "text and official county procedures. Record "
                        "effective dates and distinguish statewide rules "
                        "from auction-specific practices, especially where "
                        "registration, assignment, premiums, or redemption "
                        "calculations differ between neighboring counties."
                    ),
                    (
                        "Map each contemplated enforcement step to its "
                        "required notices, parties, waiting periods, "
                        "and evidence. Treat returned mail, bankruptcy "
                        "indicators, military-service questions, and "
                        "federal claims as substantive review events "
                        "rather than clerical obstacles to process "
                        "completion."
                    ),
                    (
                        "Review surplus treatment after Tyler using "
                        "the actual jurisdiction and procedure. "
                        "Separate lien recovery from owner equity, "
                        "and do not model all remaining property "
                        "value as investor profit merely because "
                        "an older tax-foreclosure practice "
                        "allowed retention."
                    ),
                    (
                        "Check the activities performed by each "
                        "participant rather than assuming an "
                        "investment label resolves licensing questions. "
                        "Direct purchases, third-party servicing, debt "
                        "collection, brokerage, pooled offerings, and "
                        "property management can create different "
                        "requirements and contractual responsibilities."
                    ),
                    (
                        "Approve communication templates against the "
                        "actual instrument rights and verified "
                        "balances. Remove threats of immediate "
                        "possession, misleading government affiliation, "
                        "and unsupported payoff demands; retain "
                        "delivery evidence and route disputed "
                        "amounts to the authorized county "
                        "or legal process."
                    ),
                ],
                "fields": [
                    field(
                        "Florida certificate rules and auction eligibility",
                        "textarea",
                        (
                            "Document bidder eligibility, interest "
                            "ceiling, bid-down mechanics, payment "
                            "rules, and redemption calculations "
                            "for the selected Florida county. "
                            "Identify which requirements arise "
                            "from statute and which come "
                            "from the county's current auction "
                            "registration materials."
                        ),
                        (
                            "The Florida checklist cites Fla. "
                            "Stat. 197.172, 197.432, and "
                            "197.472 for interest and certificate "
                            "sale or redemption rules. The "
                            "statutory ceiling is 18%, not "
                            "the investor's assured return. "
                            "County materials supply registration "
                            "and deposit instructions. The "
                            "reviewer separately documents the "
                            "5% redemption minimum and its "
                            "zero-rate exception."
                        ),
                    ),
                    field(
                        "Arizona rate and foreclosure eligibility comparison",
                        "textarea",
                        (
                            "Describe Arizona's certificate rate "
                            "framework and the distinction "
                            "between holding a certificate "
                            "and becoming eligible to seek "
                            "foreclosure. Record notice requirements "
                            "separately so passage of time "
                            "cannot be mistaken for automatic "
                            "ownership or immediate possession."
                        ),
                        (
                            "Arizona review cites A.R.S. "
                            "42-18053 and 42-18114 for "
                            "the interest framework and "
                            "bid-down sale, including the "
                            "16% ceiling. A.R.S. 42-18201 "
                            "generally permits a foreclosure "
                            "action after three years, "
                            "subject to applicable requirements. "
                            "The file separately checks "
                            "42-18202 notice obligations "
                            "and current surplus procedures "
                            "before authorizing litigation."
                        ),
                    ),
                    field(
                        "Texas deed classification and redemption rights",
                        "textarea",
                        (
                            "Classify the Texas property and "
                            "identify the redemption clock's "
                            "trigger, eligible reimbursement "
                            "items, and premium schedule. "
                            "Explain why the shorter period "
                            "for other property cannot "
                            "be substituted for the "
                            "homestead or agricultural rules."
                        ),
                        (
                            "Tex. Tax Code 34.21 generally "
                            "provides two years for qualifying "
                            "homestead, agricultural-use property, "
                            "and mineral interests, measured "
                            "from deed recording. Other "
                            "property generally has 180 "
                            "days. The applicable premium "
                            "is generally 25% during "
                            "the first year and 50% "
                            "during the second for "
                            "the two-year category, not "
                            "compounded annual interest."
                        ),
                    ),
                    field(
                        "Notice recipients and returned-mail response",
                        "textarea",
                        (
                            "Identify parties entitled to "
                            "notice, address sources, service "
                            "methods, and evidence retention. "
                            "Describe the escalation when "
                            "mail fails and explain "
                            "why a mailing receipt "
                            "alone may not establish "
                            "that the constitutional notice "
                            "obligation has been satisfied."
                        ),
                        (
                            "The notice file applies "
                            "Mennonite Board of Missions "
                            "v. Adams, 462 U.S. "
                            "791 (1983), and Jones "
                            "v. Flowers, 547 U.S. "
                            "220 (2006), alongside local "
                            "procedure. Returned certified "
                            "mail triggers review of "
                            "additional reasonable steps "
                            "when practicable. Staff retain "
                            "address searches, returned "
                            "envelopes, delivery records, "
                            "and counsel's documented "
                            "service analysis."
                        ),
                    ),
                    field(
                        "Post-Tyler equity and surplus treatment",
                        "textarea",
                        (
                            "Explain how the planned "
                            "procedure protects owner equity "
                            "beyond the tax obligation. "
                            "Identify the controlling local "
                            "sale, valuation, or surplus "
                            "process without assuming that "
                            "one Supreme Court decision "
                            "creates identical mechanics "
                            "for every private certificate "
                            "holder."
                        ),
                        (
                            "Tyler v. Hennepin County, "
                            "598 U.S. 631 (2023), "
                            "rejects governmental retention "
                            "of value exceeding the "
                            "tax debt under the "
                            "facts addressed. A $120,000 "
                            "sale against $20,000 "
                            "reviewed claims therefore "
                            "does not create $100,000 "
                            "automatic investor gain. "
                            "The file maps applicable "
                            "local surplus procedures, "
                            "including Tex. Tax Code "
                            "34.04 where relevant."
                        ),
                    ),
                    field(
                        "Bankruptcy and servicemember protections",
                        "textarea",
                        (
                            "Specify searches and escalation "
                            "steps for bankruptcy and "
                            "military-service indicators before "
                            "enforcement. Distinguish routine "
                            "portfolio monitoring from an "
                            "act against protected property "
                            "or a request for default "
                            "judgment, and require documented "
                            "review of applicable exceptions."
                        ),
                        (
                            "A PACER search reveals "
                            "a pending Chapter 13 "
                            "case associated with the "
                            "record owner. The operator "
                            "suspends contemplated enforcement "
                            "for review under 11 "
                            "U.S.C. 362 rather than "
                            "assuming tax status defeats "
                            "the stay. Counsel also "
                            "checks 50 U.S.C. 3931 "
                            "default-judgment protections "
                            "and 3991 tax-related "
                            "protections when relevant."
                        ),
                    ),
                    field(
                        "Federal claims and surviving redemption rights",
                        "textarea",
                        (
                            "Identify recorded federal claims "
                            "and determine whether the "
                            "planned process requires federal "
                            "notice, joinder, or additional "
                            "redemption tracking. Avoid "
                            "assuming that local tax "
                            "priority alone eliminates "
                            "every federal interest "
                            "or permits immediate "
                            "resale with clear title."
                        ),
                        (
                            "A recorded federal tax "
                            "lien triggers review of "
                            "26 U.S.C. 7425 before "
                            "a nonjudicial sale. The "
                            "file examines applicable "
                            "notice requirements, including "
                            "the statutory 25-day "
                            "notice timing where required. "
                            "If discharged through "
                            "the relevant sale process, "
                            "federal redemption can "
                            "extend 120 days or "
                            "the longer applicable "
                            "local period under "
                            "7425(d)."
                        ),
                    ),
                    field(
                        "Activity-specific licensing and capital sourcing",
                        "textarea",
                        (
                            "Describe who supplies capital "
                            "and which services each "
                            "entity performs. Review "
                            "licensing and offering "
                            "requirements separately for "
                            "own-account investing, outside "
                            "capital, collection services, "
                            "brokerage, and property "
                            "management instead of "
                            "using a single blanket "
                            "classification."
                        ),
                        (
                            "The pilot uses only "
                            "the owner's $125,000 "
                            "and does not solicit "
                            "passive investors. A "
                            "future pooled vehicle "
                            "requires a separate "
                            "Securities Act registration "
                            "or exemption analysis, "
                            "including 15 U.S.C. "
                            "77e. Outsourced collection "
                            "activity receives its "
                            "own state-law and "
                            "15 U.S.C. 1692a "
                            "coverage review rather "
                            "than inheriting the "
                            "investor's operating assumptions."
                        ),
                    ),
                    field(
                        "Assignments, servicing contracts, and custody terms",
                        "textarea",
                        (
                            "Specify how an assignment "
                            "becomes effective, who "
                            "holds original evidence, "
                            "who receives redemption "
                            "funds, and how errors "
                            "are resolved. Tie "
                            "contract language to "
                            "county recognition and "
                            "the actual instrument "
                            "rather than treating "
                            "a generic transfer "
                            "form as sufficient."
                        ),
                        (
                            "The servicing agreement "
                            "states: 'Servicer may "
                            "monitor county records "
                            "and reconcile receipts "
                            "but may not settle "
                            "claims or initiate "
                            "enforcement without written "
                            "authority.' A $10,000 "
                            "certificate assignment "
                            "closes only after "
                            "required county recognition "
                            "is documented. Redemption "
                            "routing, document return, "
                            "error correction, and "
                            "termination assistance "
                            "receive separate clauses."
                        ),
                    ),
                    field(
                        "Owner outreach and payoff accuracy",
                        "textarea",
                        (
                            "Draft an owner-contact "
                            "standard covering identity, "
                            "purpose, verified balances, "
                            "disputes, and communication "
                            "records. State which "
                            "claims and collection "
                            "methods are prohibited "
                            "because they exceed "
                            "the investor's rights "
                            "or misrepresent the "
                            "county's role."
                        ),
                        (
                            "The approved message "
                            "identifies the private "
                            "certificate holder and "
                            "directs the owner "
                            "to the county's "
                            "official redemption channel. "
                            "It does not demand "
                            "payment to an "
                            "unverified account or "
                            "threaten immediate eviction. "
                            "A disputed $600 "
                            "interest amount is "
                            "checked against the "
                            "county payoff statement "
                            "before any further "
                            "balance representation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when current jurisdiction rules, notice "
                    "requirements, protected-party checks, federal claims, "
                    "surplus treatment, activity-specific permissions, and "
                    "communication templates have documented reviewers "
                    "and no unresolved execution-blocking issue."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Opportunity Pipeline, and Risk Fallback",
                "purpose": (
                    "Automate repeatable screening and redemption monitoring "
                    "without automating unsupported legal conclusions or "
                    "irreversible payments. Build an evidence-preserving "
                    "opportunity pipeline, measure screening precision, "
                    "and establish manual fallbacks for changed county "
                    "formats, stale records, duplicate assets, and "
                    "interrupted data access."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Inventory official data sources and their permitted "
                        "access methods before writing import routines. "
                        "Prefer published downloads or authorized interfaces, "
                        "record refresh cadence, and avoid assuming that "
                        "public visibility permits unrestricted automated "
                        "collection or redistribution of every field."
                    ),
                    (
                        "Separate source capture, normalization, scoring, "
                        "human review, and execution into distinct "
                        "steps. Preserve original rows and transformation "
                        "versions so a changed parcel format cannot "
                        "silently alter the asset identity or "
                        "approved bidding instruction."
                    ),
                    (
                        "Automate deterministic checks first: duplicate "
                        "detection, missing identifiers, exposure limits, "
                        "deadline reminders, and receipt matching. "
                        "Route ownership ambiguities, title conclusions, "
                        "bankruptcy questions, and statutory interpretation "
                        "to qualified reviewers instead of giving "
                        "a screening score decision authority."
                    ),
                    (
                        "Develop growth through additional official "
                        "auction coverage and carefully qualified "
                        "professional relationships. Measure approved "
                        "opportunities per review hour rather "
                        "than owner-contact volume, and expand "
                        "only when reserve capacity and "
                        "documented reviewer throughput support "
                        "the larger pipeline."
                    ),
                    (
                        "Test failures deliberately using synthetic "
                        "input files and disconnected integrations. "
                        "Define when automation stops, who "
                        "switches to manual county verification, "
                        "and how restored processing avoids "
                        "duplicate alerts, duplicate ledger "
                        "entries, or conflicting versions "
                        "of the same record."
                    ),
                ],
                "fields": [
                    field(
                        "Source inventory and permitted collection",
                        "textarea",
                        (
                            "List each official auction, "
                            "assessor, recorder, and "
                            "redemption source with "
                            "access method, refresh "
                            "schedule, permitted use, "
                            "and responsible role. "
                            "Explain how unavailable "
                            "or restricted access "
                            "changes the workflow "
                            "without bypassing source "
                            "controls."
                        ),
                        (
                            "County A publishes "
                            "a weekly auction "
                            "CSV, County B "
                            "offers a manual "
                            "redemption search, and "
                            "the recorder charges "
                            "$1 per document "
                            "image. The analyst "
                            "downloads permitted files "
                            "and logs retrieval "
                            "dates. County B "
                            "remains a manual "
                            "task until an "
                            "authorized interface is "
                            "available; no login "
                            "or access restriction "
                            "is circumvented."
                        ),
                    ),
                    field(
                        "Normalization schema and source lineage",
                        "textarea",
                        (
                            "Define normalized columns, "
                            "currency precision, date "
                            "formats, and source "
                            "references. Preserve raw "
                            "values beside interpreted "
                            "values so reviewers "
                            "can trace every "
                            "screening result back "
                            "to the county "
                            "record that produced "
                            "it."
                        ),
                        (
                            "A Python csv "
                            "import writes county_id, "
                            "tax_year, parcel_id, "
                            "instrument_id, face_amount, "
                            "source_date, and source_hash "
                            "into SQLite. Currency "
                            "uses decimal arithmetic. "
                            "The raw parcel "
                            "value '001-024-009' "
                            "retains its leading "
                            "zeros even if "
                            "a separate search "
                            "key removes punctuation. "
                            "Every derived record "
                            "links to its "
                            "original input row."
                        ),
                    ),
                    field(
                        "Screening rules and rejection explanations",
                        "textarea",
                        (
                            "Specify deterministic exclusion "
                            "rules and explainable "
                            "ranking factors. Record "
                            "which findings require "
                            "human review rather "
                            "than automatic rejection, "
                            "and keep the "
                            "reason attached to "
                            "the asset so "
                            "future imports preserve "
                            "the decision history."
                        ),
                        (
                            "The first pass "
                            "rejects missing legal "
                            "descriptions and bids "
                            "above the parcel "
                            "limit, while flagging "
                            "industrial-use indicators "
                            "for specialist review. "
                            "Of 500 rows, "
                            "320 fail explicit "
                            "mandate rules, 140 "
                            "need additional evidence, "
                            "and 40 enter "
                            "detailed underwriting. "
                            "The score never "
                            "labels a parcel "
                            "clear-title merely "
                            "because no lien "
                            "appears in one "
                            "download."
                        ),
                    ),
                    field(
                        "Redemption monitoring and event verification",
                        "textarea",
                        (
                            "Describe how redemption "
                            "events are detected, "
                            "verified, matched to "
                            "cash, and closed. "
                            "Define the distinction "
                            "between a changed "
                            "county status, a "
                            "confirmed payoff statement, "
                            "and an actual "
                            "bank receipt before "
                            "automating any accounting "
                            "entry."
                        ),
                        (
                            "A daily comparison "
                            "flags FL-2027-022 "
                            "as redeemed and "
                            "opens a reconciliation "
                            "task. The operator "
                            "retrieves the county "
                            "detail showing $10,000 "
                            "principal and $600 "
                            "interest, then matches "
                            "the $10,600 settled "
                            "deposit. Only after "
                            "both checks does "
                            "the asset close; "
                            "the initial status "
                            "change alone creates "
                            "no cash balance "
                            "or realized revenue."
                        ),
                    ),
                    field(
                        "Professional outreach and auction coverage",
                        "textarea",
                        (
                            "Identify lawful growth "
                            "channels that improve "
                            "evidence quality or "
                            "auction access rather "
                            "than pressuring property "
                            "owners. Set measurable "
                            "relationship and coverage "
                            "targets while excluding "
                            "referral payments or "
                            "special access arrangements "
                            "that have not "
                            "been reviewed."
                        ),
                        (
                            "During the first "
                            "month, the operator "
                            "requests published auction "
                            "calendars from four "
                            "counties, interviews two "
                            "title contractors, and "
                            "obtains one fixed-scope "
                            "local counsel proposal. "
                            "The target is "
                            "twenty fully evidenced "
                            "candidates, not two "
                            "hundred owner solicitations. "
                            "Public staff receive "
                            "no payment for "
                            "preferential information "
                            "or queue placement."
                        ),
                    ),
                    field(
                        "Review productivity and screening precision",
                        "textarea",
                        (
                            "Measure throughput using "
                            "completed evidence checks "
                            "and approved opportunities "
                            "rather than raw "
                            "import volume. Define "
                            "false positives, reviewer "
                            "hours, and retained "
                            "decision quality so "
                            "automation gains cannot "
                            "hide increased defect "
                            "rates or skipped "
                            "title review."
                        ),
                        (
                            "Forty automated candidates "
                            "consume twenty reviewer "
                            "hours and produce "
                            "twelve approved bids, "
                            "or 0.6 approved "
                            "opportunities per hour. "
                            "Eight candidates contained "
                            "parcel-identity errors, "
                            "yielding a 20% "
                            "identity-defect rate "
                            "within the reviewed "
                            "set. The next "
                            "iteration improves identifier "
                            "checks before increasing "
                            "county coverage or "
                            "the acquisition budget."
                        ),
                    ),
                    field(
                        "Data minimization and access separation",
                        "textarea",
                        (
                            "Specify the information "
                            "necessary for underwriting "
                            "and statutory execution, "
                            "who can access "
                            "it, and which "
                            "fields should remain "
                            "outside marketing exports. "
                            "Separate payment authority "
                            "from research permissions "
                            "and document retention "
                            "according to operational "
                            "need."
                        ),
                        (
                            "Analysts can view "
                            "parcel records and "
                            "title evidence but "
                            "cannot edit bank "
                            "beneficiaries. The settlement "
                            "reviewer receives payment "
                            "access separately. Owner "
                            "mailing addresses stay "
                            "within the asset "
                            "file and authorized "
                            "notice workflow; they "
                            "are excluded from "
                            "relationship-marketing exports. "
                            "Access is reviewed "
                            "monthly and revoked "
                            "when a contractor's "
                            "engagement ends."
                        ),
                    ),
                    field(
                        "Fallback for stale or changed county data",
                        "textarea",
                        (
                            "Define freshness thresholds, "
                            "schema-change detection, "
                            "manual verification steps, "
                            "and bidding restrictions "
                            "during data failure. "
                            "Explain how the "
                            "team will distinguish "
                            "a genuinely empty "
                            "auction list from "
                            "an unsuccessful download "
                            "or broken import."
                        ),
                        (
                            "An auction file "
                            "older than seven "
                            "days receives a "
                            "stale-data flag. If "
                            "the certificate-number "
                            "column disappears, import "
                            "stops and preserves "
                            "the prior dataset. "
                            "The analyst checks "
                            "the official portal "
                            "manually before any "
                            "bid. A zero-row "
                            "response is treated "
                            "as a retrieval "
                            "exception until the "
                            "county confirms there "
                            "are no offerings."
                        ),
                    ),
                    field(
                        "Monitoring thresholds and response ownership",
                        "textarea",
                        (
                            "Set actionable thresholds "
                            "for unmatched receipts, "
                            "missed refreshes, upcoming "
                            "deadlines, and concentration "
                            "breaches. Assign each "
                            "alert to a "
                            "specific role with "
                            "a response period "
                            "and the exact "
                            "activity that stops "
                            "while the issue "
                            "remains open."
                        ),
                        (
                            "Any settlement-account change "
                            "requires immediate payment "
                            "suspension. Unmatched receipts "
                            "older than two "
                            "business days go "
                            "to the ledger "
                            "owner. A statutory "
                            "deadline inside ninety "
                            "days requires legal "
                            "review scheduling. County "
                            "exposure above $40,000 "
                            "blocks additional pilot "
                            "bids until commitments "
                            "are reduced or "
                            "the owner explicitly "
                            "revises the documented "
                            "limit."
                        ),
                    ),
                    field(
                        "Automation expansion decision and rollback",
                        "textarea",
                        (
                            "Define the evidence "
                            "required to expand "
                            "automation into another "
                            "county or workflow. "
                            "Include parallel manual "
                            "checks, error tolerance, "
                            "version control, and "
                            "a rollback plan "
                            "that preserves asset "
                            "history without repeating "
                            "payments or statutory "
                            "communications."
                        ),
                        (
                            "The new county "
                            "adapter runs beside "
                            "manual review for "
                            "four weekly cycles. "
                            "All asset identifiers "
                            "and money fields "
                            "must match source "
                            "documents exactly. One "
                            "misassigned certificate "
                            "blocks production use. "
                            "Rollback restores the "
                            "prior parser version "
                            "and reprocesses source "
                            "files idempotently; "
                            "payment and notice "
                            "systems remain outside "
                            "the adapter's authority."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Expand only after source permissions, lineage, "
                    "screening precision, redemption verification, alert "
                    "ownership, manual fallback, and rollback tests "
                    "are documented and no automation can independently "
                    "release funds or initiate enforcement."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch, Pod KPI Scorecard, and Exit Readiness",
                "purpose": (
                    "Use the first thirty days to establish investable "
                    "readiness rather than manufacture premature returns. "
                    "Assign pod responsibilities, reconcile canonical "
                    "economics, measure capital and evidence quality, "
                    "and preserve transferable records for a "
                    "controlled portfolio sale, assignment, or "
                    "orderly wind-down."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Plan four weekly milestones that produce "
                        "verifiable artifacts: jurisdiction rules, "
                        "qualified candidates, tested records, and "
                        "a funded operating plan. Preserve "
                        "the canonical 6–36 month first-deal "
                        "window; a thirty-day setup sprint "
                        "does not imply a realized "
                        "return within thirty days."
                    ),
                    (
                        "Assign a single accountable role "
                        "to each acquisition, settlement, "
                        "ledger, and statutory task. "
                        "Use contractors for scoped "
                        "specialist work, but keep "
                        "investment authority and bank "
                        "permissions explicit so a "
                        "small pod does not "
                        "rely on informal delegation."
                    ),
                    (
                        "Track leading indicators separately "
                        "from earned results. Evidence "
                        "completion, review throughput, "
                        "liquidity coverage, and deadline "
                        "health support readiness, while "
                        "realized interest, penalties, "
                        "disposition gains, and owner "
                        "profit determine actual "
                        "economic performance."
                    ),
                    (
                        "Review the scorecard weekly "
                        "against canonical scenario "
                        "definitions and current cash "
                        "commitments. Explain deviations "
                        "using cohort timing and "
                        "documented costs instead "
                        "of changing the revenue "
                        "definition or counting "
                        "unredeemed principal as "
                        "new earnings."
                    ),
                    (
                        "Prepare transfer and wind-down "
                        "records from the first "
                        "acquisition. Maintain instrument "
                        "evidence, assignment restrictions, "
                        "basis history, open notices, "
                        "and service responsibilities "
                        "so another operator can "
                        "underwrite the portfolio "
                        "without relying on "
                        "the founder's memory."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 jurisdiction and capital setup",
                        "textarea",
                        (
                            "Specify the first "
                            "week's concrete deliverables "
                            "for jurisdiction selection, "
                            "capital allocation, official "
                            "source collection, and "
                            "specialist engagement. State "
                            "what remains deliberately "
                            "unfunded until the "
                            "evidence and execution "
                            "systems are ready "
                            "for a live "
                            "purchase."
                        ),
                        (
                            "By day seven, "
                            "the operator has "
                            "a Florida rules "
                            "matrix, a Texas "
                            "comparison memo, two "
                            "contractor scopes, and "
                            "$125,000 allocated "
                            "as $100,000 potential "
                            "deployment plus $25,000 "
                            "liquid support. No "
                            "auction payment is "
                            "authorized yet. The "
                            "bank verification checklist "
                            "and written parcel "
                            "limits are completed "
                            "before bidder registration "
                            "is activated."
                        ),
                    ),
                    field(
                        "Days 8–14 candidate underwriting sprint",
                        "textarea",
                        (
                            "Define the second "
                            "week's screening volume, "
                            "evidence standards, reviewer "
                            "assignments, and rejection "
                            "record. Show how "
                            "the team will "
                            "produce a smaller "
                            "qualified list rather "
                            "than treating every "
                            "imported auction row "
                            "as an investable "
                            "opportunity."
                        ),
                        (
                            "The analyst screens "
                            "200 official auction "
                            "rows, advances twenty "
                            "to parcel review, "
                            "and commissions title "
                            "work on six. "
                            "Three pass the "
                            "mandate; two fail "
                            "access review and "
                            "one has unresolved "
                            "federal-claim issues. "
                            "The three approved "
                            "files include legal "
                            "descriptions, downside "
                            "cases, bid floors, "
                            "and identified evidence "
                            "owners before any "
                            "capital commitment."
                        ),
                    ),
                    field(
                        "Days 15–21 execution rehearsal",
                        "textarea",
                        (
                            "Describe the rehearsal "
                            "that tests acquisition, "
                            "settlement, custody, redemption, "
                            "and exception handling "
                            "without sending money. "
                            "Include a deliberately "
                            "incorrect input and "
                            "explain what the "
                            "system must prevent "
                            "before the rehearsal "
                            "can be considered "
                            "successful."
                        ),
                        (
                            "The pod rehearses "
                            "a $10,000 certificate "
                            "at 8%, nine "
                            "statutory months, and "
                            "$600 interest. A "
                            "duplicate award, a "
                            "changed beneficiary, and "
                            "a mismatched parcel "
                            "are inserted deliberately. "
                            "The system rejects "
                            "duplicate funding, suspends "
                            "the beneficiary change, "
                            "and blocks issuance "
                            "until parcel evidence "
                            "matches. The mock "
                            "redemption reconciles "
                            "without counting principal "
                            "as revenue."
                        ),
                    ),
                    field(
                        "Days 22–30 readiness and acquisition decision",
                        "textarea",
                        (
                            "Define the final "
                            "week's decision artifacts, "
                            "remaining blockers, and "
                            "authority to proceed "
                            "or wait. Separate "
                            "completion of operational "
                            "setup from actual "
                            "deal timing, auction "
                            "availability, redemption, "
                            "and recognition of "
                            "earned investment "
                            "revenue."
                        ),
                        (
                            "By day thirty, "
                            "three candidate files, "
                            "a tested ledger, "
                            "a verified settlement "
                            "route, and a "
                            "thirty-month liquidity "
                            "stress are ready. "
                            "The next suitable "
                            "auction is still "
                            "months away, so "
                            "capital remains liquid. "
                            "The launch milestone "
                            "is readiness; the "
                            "canonical first-deal "
                            "window remains 6–36 "
                            "months and no "
                            "revenue is booked."
                        ),
                    ),
                    field(
                        "Pod responsibilities and staffing economics",
                        "textarea",
                        (
                            "Assign operating roles "
                            "for the conservative, "
                            "base, and scaled "
                            "configurations. Explain "
                            "how contractor scopes "
                            "and working capacity "
                            "fit the expense "
                            "bridge, and identify "
                            "any hiring decision "
                            "that requires a "
                            "separate wage-budget "
                            "test before expansion."
                        ),
                        (
                            "Conservative and base "
                            "use 1 FT "
                            "+ 2 C: "
                            "an owner-operator, "
                            "a title specialist, "
                            "and local counsel. "
                            "Scaled uses 2 "
                            "FT + 3 "
                            "C, five people "
                            "total, adding operating "
                            "capacity and a "
                            "scoped field specialist. "
                            "These capacity labels "
                            "do not establish "
                            "salary funding; any "
                            "employee hire must "
                            "fit a separately "
                            "costed operating plan."
                        ),
                    ),
                    field(
                        "Weekly operating KPI scorecard",
                        "textarea",
                        (
                            "Set numerical targets "
                            "for evidence completion, "
                            "review productivity, cash "
                            "reconciliation, deadline "
                            "ownership, and concentration. "
                            "Distinguish leading metrics "
                            "from realized earnings "
                            "and identify which "
                            "missed targets suspend "
                            "new commitments rather "
                            "than merely creating "
                            "a dashboard warning."
                        ),
                        (
                            "Weekly targets are "
                            "100% verified parcel "
                            "identity, 100% assigned "
                            "statutory deadlines, zero "
                            "unreviewed settlement "
                            "changes, and no "
                            "unmatched receipt older "
                            "than two business "
                            "days. The pilot "
                            "retains its $10,000 "
                            "parcel and $40,000 "
                            "county limits. Any "
                            "breach suspends affected "
                            "bids; importing 1,000 "
                            "extra rows does "
                            "not offset a "
                            "failed cash-control "
                            "metric."
                        ),
                    ),
                    field(
                        "Canonical performance and score interpretation",
                        "textarea",
                        (
                            "Record the candidate's "
                            "score components and "
                            "annual owner-profit "
                            "targets without treating "
                            "a score as "
                            "a return forecast. "
                            "Explain how the "
                            "capital-intensive profile "
                            "changes launch priorities "
                            "relative to a "
                            "labor-light operating "
                            "business."
                        ),
                        (
                            "The 62/100 score "
                            "comprises revenue potential "
                            "17, margin potential "
                            "15, team efficiency "
                            "17, startup accessibility "
                            "5, and automation "
                            "8. Annual owner-profit "
                            "targets remain $4,500, "
                            "$41,438, and $99,000 "
                            "for conservative, base, "
                            "and scaled cases. "
                            "The capital and "
                            "labor intensive classification "
                            "prioritizes cash duration, "
                            "title quality, and "
                            "recovery discipline over "
                            "rapid acquisition "
                            "volume."
                        ),
                    ),
                    field(
                        "Pause, stop-loss, and redeployment criteria",
                        "textarea",
                        (
                            "Define conditions for "
                            "pausing purchases, escalating "
                            "an impaired asset, "
                            "or reallocating capital. "
                            "Recognize that illiquid "
                            "certificates may lack "
                            "an immediate exit "
                            "and distinguish a "
                            "decision threshold from "
                            "an executable market "
                            "sale at a "
                            "known price."
                        ),
                        (
                            "New bids pause "
                            "when spendable liquidity "
                            "falls below twelve "
                            "months of committed "
                            "opex plus reviewed "
                            "near-term advances. A "
                            "suspected title loss "
                            "above $5,000 triggers "
                            "asset-specific recovery "
                            "review. The operator "
                            "does not assume "
                            "a certificate can "
                            "be sold tomorrow "
                            "at face value; "
                            "redeployment waits for "
                            "verified redemption or "
                            "a documented "
                            "assignment offer."
                        ),
                    ),
                    field(
                        "Transfer package and buyer diligence ledger",
                        "textarea",
                        (
                            "List the records "
                            "a buyer or "
                            "successor operator needs "
                            "to validate ownership, "
                            "basis, statutory status, "
                            "and future obligations. "
                            "Identify assignment "
                            "restrictions and distinguish "
                            "sale preparation from "
                            "permission to transfer "
                            "private documents or "
                            "execute a portfolio "
                            "sale."
                        ),
                        (
                            "A proposed twenty-certificate "
                            "package includes county "
                            "issuance evidence, $200,000 "
                            "aggregate principal, "
                            "rate schedules, recorded "
                            "assignments, redemption "
                            "history, title exceptions, "
                            "and reviewed deadlines. "
                            "Buyer access uses "
                            "a controlled data "
                            "room with necessary "
                            "fields only. Transfer "
                            "requires county-specific "
                            "assignment steps and "
                            "owner authorization; "
                            "a prepared diligence "
                            "folder does not "
                            "itself authorize "
                            "the sale."
                        ),
                    ),
                    field(
                        "Exit valuation and orderly wind-down",
                        "textarea",
                        (
                            "Calculate a possible "
                            "portfolio exit using "
                            "documented basis, actual "
                            "offer terms, and "
                            "transfer costs. Preserve "
                            "cash for continuing "
                            "deadlines and services "
                            "until assignments are "
                            "effective, and explain "
                            "how exit gain "
                            "or loss enters "
                            "recognized operator "
                            "results."
                        ),
                        (
                            "A buyer offers "
                            "$196,000 for certificates "
                            "with $200,000 carrying "
                            "basis, and transfer "
                            "costs are $2,000. "
                            "Net proceeds of "
                            "$194,000 create a "
                            "$6,000 realized loss, "
                            "not $194,000 revenue. "
                            "The operator retains "
                            "$8,000 for documented "
                            "wind-down obligations "
                            "and continues deadline "
                            "monitoring until county "
                            "records and contracts "
                            "confirm the effective "
                            "transfer."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Finish the sprint only when all four weekly artifacts, "
                    "pod assignments, canonical reconciliations, liquidity "
                    "tests, KPI thresholds, and transfer records are complete; "
                    "report unresolved blockers and recognize earnings only "
                    "when supported by realized transactions."
                ),
            },
        ],
    }
