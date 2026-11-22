from __future__ import annotations

VOLUME_030_SUBTITLE = (
    "The Complete Playbook for Lending & Flash-Funding Arbitrage: "
    "$120,000–$950,000 USD in Annual Earned Revenue; "
    "a 1 FT + 2 C Three-Person Pod, Expanding to Five People at Scale"
)

VOLUME_030_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Escrow-Locked Liquidity Desk",
        "subtitle": (
            "Operate 24-to-72-hour transactional double-close funding through "
            "verified settlement agents, deposited buyer cash, and reconciled payoffs."
        ),
        "audience": (
            "Experienced real-estate operators with title relationships, "
            "$25,000–$100,000 in startup capital, and documented capital-provider terms."
        ),
        "research_basis": (
            "Business-purpose credit can be exempt from federal consumer-credit "
            "disclosure requirements under 15 U.S.C. 1603(1) and "
            "12 CFR 1026.3(a). That exemption does not resolve state lender "
            "licensing, permissible charges, or settlement-agent authority. "
            "California Financial Code section 22100 supplies a concrete "
            "licensing inquiry; New York General Obligations Law section "
            "5-501 supplies a separate rate-and-charge inquiry."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1603",
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/section-1026.3",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=22100.&lawCode=FIN",
            "https://www.nysenate.gov/legislation/laws/GOB/5-501",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Earned-Fee Funding Pod",
        "subtitle": (
            "Build a three-person funding operation around earned fees and "
            "contractual EMD JV splits, never escrow principal or property sale prices."
        ),
        "audience": (
            "Small private-capital teams that need transaction-level underwriting, "
            "a principal-versus-fee ledger, and a repeatable owner-profit model."
        ),
        "research_basis": (
            "An earnest-money deposit, abbreviated EMD, does not become outside "
            "lending law merely because documents call its return a JV split. "
            "California Financial Code section 22100 and New York General "
            "Obligations Law section 5-501 support substance-first review of "
            "licensing and charges. UCC 9-109(d)(11) generally excludes creation "
            "or transfer of real-property interests from Article 9, subject to "
            "listed exceptions; a UCC filing alone is not a real-estate lien."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=22100.&lawCode=FIN",
            "https://www.nysenate.gov/legislation/laws/GOB/5-501",
            "https://www.law.cornell.edu/ucc/9/9-109",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Verified Liquidity-Velocity Playbook",
        "subtitle": (
            "Separate lawful corporate-credit liquidity from purchase-only "
            "promotions, then control every escrow release and repayment deadline."
        ),
        "audience": (
            "Operators evaluating corporate-credit facilities alongside committed "
            "cash, with issuer-permitted transfers and independently verified escrow accounts."
        ),
        "research_basis": (
            "Business-purpose treatment under 12 CFR 1026.3(a) does not make "
            "purchase-rate promotions applicable to cash advances or transfers. "
            "The controlling issuer agreement must establish permitted use, "
            "transaction classification, fees, and repricing dates. "
            "18 U.S.C. 1014 addresses covered false statements made to influence "
            "specified institutions; applications and proof-of-funds records "
            "must accurately describe resources and borrowing arrangements."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-12/chapter-X/part-1026/section-1026.3",
            "https://www.law.cornell.edu/uscode/text/18/1014",
            "https://www.law.cornell.edu/uscode/text/15/1603",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_030_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-escrow-locked-funding-workflow",
            "process_flow",
            "Five Controls Between Intake and Repaid Capital",
            (
                "A 24-to-72-hour funding interval begins at confirmed outbound "
                "settlement, not at the first borrower inquiry."
            ),
            1,
            "operating_framework",
            (
                "This workflow authorizes releases only to bonded title or "
                "settlement agents after independently verifying unconditional "
                "end-buyer cash on deposit. Traditional early EMD requests "
                "without that cash fail this release standard. The workflow "
                "does not equate a wire receipt with settled, available funds."
            ),
            (
                "Keep principal movements, earned funding fees, and capital-provider "
                "repayments in separate ledger accounts; close each exposure only "
                "after the return wire and fee allocation reconcile."
            ),
            [
                (
                    "Document the transaction",
                    "Collect contracts, entity records, and funding requests.",
                    1.0,
                    (
                        "Use a structured intake form and permission-restricted "
                        "document room. Capture both purchase contracts, borrower "
                        "authority, property jurisdiction, requested principal, "
                        "expected payoff, and the proposed 24-to-72-hour interval. "
                        "Issue proof of funds only against verified available "
                        "cash or a documented, drawable capital commitment."
                    ),
                ),
                (
                    "Underwrite repayment",
                    "Match buyer cash against every required disbursement.",
                    2.0,
                    (
                        "Obtain the settlement statement and agent-confirmed "
                        "available buyer cash. Test whether unconditional proceeds "
                        "cover funded principal, earned charges, liens, taxes, "
                        "and closing costs without another sale or unfunded loan. "
                        "Reject dry-closing assumptions and conditional buyer deposits."
                    ),
                ),
                (
                    "Authenticate the settlement agent",
                    "Verify authority, bond coverage, and bank coordinates.",
                    3.0,
                    (
                        "Check the applicable regulator's license record, bond "
                        "or coverage evidence, and title-underwriter relationship "
                        "where relevant. Call a previously verified number, not "
                        "one supplied in a changed wire email. Independently "
                        "match beneficiary ownership and account details."
                    ),
                ),
                (
                    "Release under written instructions",
                    "Require independent verification before owner-authorized wiring.",
                    4.0,
                    (
                        "The underwriting contractor records verification; the "
                        "owner separately authorizes the wire. Written escrow "
                        "instructions specify permitted disbursements, closing "
                        "conditions, payoff order, and return handling. A changed "
                        "beneficiary or missing cash confirmation stops release."
                    ),
                ),
                (
                    "Reconcile payoff and earnings",
                    "Close principal exposure before distributing earned returns.",
                    5.0,
                    (
                        "Match bank settlement identifiers to the Qualia or "
                        "SoftPro closing file and the QuickBooks payoff ledger. "
                        "Record principal as recovery of funding, not revenue. "
                        "Recognize only earned contractual fees, operator EMD "
                        "JV allocations, and origination points under the "
                        "applicable revenue-recognition assessment."
                    ),
                ),
            ],
        ),
        (
            "diag-02-base-case-nested-funding-cohorts",
            "funnel",
            "From 250 Inquiries to 50 Earned-Fee Closings",
            (
                "An illustrative annual nested cohort reconciles exactly "
                "to $535,000 in Base-Case recognized operator revenue."
            ),
            6,
            "illustrative_model",
            (
                "Every downstream count is a subset of the preceding count; "
                "each funded closing represents one distinct inquiry. "
                "The assumed earned-fee mix is 30 transactional closings at "
                "$12,500, 15 operator EMD JV allocations at $8,000, and "
                "five separate origination engagements at $8,000. "
                "These assumptions are illustrative, not observed conversion rates. "
                "EMD allocations require transactions satisfying this desk's "
                "cash-on-deposit release standard and appropriate legal characterization."
            ),
            (
                "30 × $12,500 + 15 × $8,000 + 5 × $8,000 = $535,000. "
                "Average earned revenue is $10,700 per completed engagement; "
                "neither property value nor escrow principal enters that total."
            ),
            [
                (
                    "Received funding inquiries",
                    "250 unique annual requests enter the intake ledger.",
                    250.0,
                    (
                        "Deduplicate by borrower entity, property, and closing "
                        "event. Capture referral source and requested timing "
                        "without counting repeat emails or revised applications "
                        "as additional opportunities."
                    ),
                ),
                (
                    "Complete commercial-purpose files",
                    "150 complete files retain sixty percent of inquiries.",
                    150.0,
                    (
                        "Require executed transaction documents, entity authority, "
                        "stated business purpose, and a named settlement agent. "
                        "Remove 100 incomplete or out-of-scope inquiries before "
                        "spending contractor time on detailed payoff analysis."
                    ),
                ),
                (
                    "Underwritten eligible transactions",
                    "100 eligible files retain two-thirds of complete submissions.",
                    100.0,
                    (
                        "Resolve state licensing and charge treatment, available "
                        "capital, collateral characterization, and repayment "
                        "economics. Remove 50 files with unresolved legal scope, "
                        "weak documents, or insufficient risk-adjusted fee contribution."
                    ),
                ),
                (
                    "Verified escrow-ready transactions",
                    "75 release-ready files retain seventy-five percent of eligibility.",
                    75.0,
                    (
                        "Require authenticated beneficiary details, verified "
                        "settlement-agent authority and coverage, unconditional "
                        "buyer cash, and signed disbursement instructions. "
                        "Twenty-five eligible files do not satisfy every release condition."
                    ),
                ),
                (
                    "Completed earned-fee engagements",
                    "50 completed engagements retain two-thirds of release-ready files.",
                    50.0,
                    (
                        "Twenty-five release-ready opportunities lapse or withdraw "
                        "before funding and generate no assumed revenue. "
                        "The remaining 50 produce the specified $535,000 fee mix "
                        "after completion; conditional fee quotes are excluded."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-earned-revenue-waterfall",
            "waterfall",
            "Base Case: $535,000 Earned Revenue to $227,375 Owner Profit",
            (
                "Six bars reconcile recognized gross operator revenue, "
                "four expense deductions, and the exact 42.5% net margin."
            ),
            3,
            "illustrative_model",
            (
                "The opening and closing bars are totals; the four intervening "
                "bars are signed deductions, not cumulative balances. "
                "Expense categories are an illustrative allocation of the "
                "canonical $307,625 total costs. Recognized gross revenue "
                "excludes escrow principal and amounts collected for other "
                "principals. Operator EMD JV allocations are already limited "
                "to the earned contractual operator share; no additional "
                "retained-share multiplier is supplied or applied."
            ),
            (
                "$535,000 − $107,000 − $80,250 − $64,200 − $56,175 "
                "= $227,375; $227,375 ÷ $535,000 = 42.5%. "
                "Conservative: $120,000 × 30% = $36,000 with 1 FT + 2 C. "
                "Scaled: $950,000 × 55% = $522,500 with 2 FT + 3 C. "
                "Principal-versus-agent presentation follows the applicable "
                "ASC 606 assessment, not the size of the escrow wire."
            ),
            [
                (
                    "Recognized gross operator revenue",
                    "$535,000 earned fees and operator JV allocations.",
                    535000.0,
                    (
                        "Opening total: $375,000 transactional funding fees, "
                        "$120,000 earned operator EMD JV allocations, and "
                        "$40,000 separate origination fees. Do not add property "
                        "sale prices, escrow principal, unearned points, or "
                        "another participant's beneficial share."
                    ),
                ),
                (
                    "Capital access and carrying costs",
                    "Subtract $107,000 for documented funding-capital expenses.",
                    -107000.0,
                    (
                        "Illustrative deduction of 20% of revenue leaves "
                        "$428,000. Includes contracted facility interest, "
                        "commitment charges, and deployment carry; excludes "
                        "repayment of borrowed principal and distributions "
                        "already excluded from recognized operator revenue."
                    ),
                ),
                (
                    "Contractor delivery and specialist costs",
                    "Subtract $80,250 for the three-person operating pod.",
                    -80250.0,
                    (
                        "Illustrative deduction of 15% of revenue leaves "
                        "$347,750. Covers the two contractors and directly "
                        "attributable outside specialist work. The owner's "
                        "residual profit is not deducted again as a distribution."
                    ),
                ),
                (
                    "Recurring operating overhead",
                    "Subtract $64,200, equivalent to $5,350 monthly overhead.",
                    -64200.0,
                    (
                        "Illustrative deduction of 12% of revenue leaves "
                        "$283,550. Covers software, insurance, bookkeeping, "
                        "secure communications, and recurring operating services. "
                        "$5,350 falls within the canonical $2,000–$12,000 "
                        "monthly operating-expense range."
                    ),
                ),
                (
                    "Loss allowance and transaction friction",
                    "Subtract $56,175 for modeled losses and closing friction.",
                    -56175.0,
                    (
                        "Illustrative deduction of 10.5% of revenue leaves "
                        "$227,375. Models credit-loss expense, failed-file "
                        "costs, wire charges, and unrecovered closing expenses. "
                        "Moving cash into a reserve account alone is not "
                        "an additional expense."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$227,375 residual profit at exactly 42.5% margin.",
                    227375.0,
                    (
                        "Closing total, not an additional positive movement: "
                        "the Base-Case 1 FT + 2 C pod retains 42.5 cents "
                        "per earned revenue dollar after the modeled costs. "
                        "The figure is owner profit, not gross billings "
                        "or deployed funding capacity."
                    ),
                ),
            ],
        ),
        (
            "diag-04-funding-lane-earned-fee-yields",
            "horizontal_bars",
            "Compare Earned Fee Yield, Not Escrow Throughput",
            (
                "Five hypothetical lane quotes express operator fees "
                "as a percentage of $100,000 deployed principal."
            ),
            2,
            "illustrative_model",
            (
                "Numeric values are fee-yield percentage points per deployment, "
                "not annual returns or net margins. Each example assumes "
                "$100,000 principal and a 72-hour exposure solely to standardize "
                "comparison. Prices are editorial assumptions, not market "
                "benchmarks or recommended charges. Payment rails do not "
                "themselves create yield. These unit examples are separate "
                "from the annual Base-Case cohort and must not be summed "
                "into its $535,000 revenue."
            ),
            (
                "Fee yield = earned operator fee ÷ deployed principal × 100. "
                "A 1.25% fee produces $1,250 revenue, not $101,250. "
                "Applicable charge limits, minimum bank charges, capital carry, "
                "and failed-closing losses determine whether any quote is usable."
            ),
            [
                (
                    "Complex double-close through Fedwire",
                    "$1,250 earned fee per $100,000 deployed principal.",
                    1.25,
                    (
                        "Assume a hypothetical 1.25% fee for a document-intensive "
                        "72-hour double close. Both closing legs must be "
                        "executable, buyer cash unconditional, and the beneficiary "
                        "verified. Complexity does not excuse an impermissible charge."
                    ),
                ),
                (
                    "Repeat-borrower double-close through Fedwire",
                    "$1,000 earned fee per $100,000 deployed principal.",
                    1.0,
                    (
                        "Assume a hypothetical 1.00% fee where reusable entity "
                        "records reduce intake work. Reconfirm bank coordinates "
                        "and available buyer cash for every transaction; "
                        "a repeat relationship never substitutes for wire authentication."
                    ),
                ),
                (
                    "Escrow-controlled EMD JV allocation",
                    "$800 operator allocation per $100,000 deployed principal.",
                    0.8,
                    (
                        "Assume a hypothetical 0.80% earned operator allocation "
                        "on a 72-hour escrow-controlled transaction. Reject early "
                        "EMD requests lacking unconditional end-buyer cash under "
                        "this desk's mandate. A JV label does not settle "
                        "whether lending rules apply."
                    ),
                ),
                (
                    "Same-bank commercial escrow transfer",
                    "$600 earned fee per $100,000 deployed principal.",
                    0.6,
                    (
                        "Assume a hypothetical 0.60% fee and confirmed "
                        "settlement-agent acceptance of an internal bank transfer. "
                        "Verify funds availability and the legal beneficiary; "
                        "a same-bank route does not eliminate mistaken-recipient "
                        "or fraudulent-instruction risk."
                    ),
                ),
                (
                    "Issuer-permitted credit-funded escrow wire",
                    "$400 earned fee per $100,000 deployed principal.",
                    0.4,
                    (
                        "Assume a hypothetical 0.40% fee only where the issuer "
                        "expressly permits the actual credit-to-cash transaction "
                        "and the settlement agent accepts its documented source. "
                        "Do not treat a 0%-APR purchase promotion as cash-advance "
                        "pricing or use fabricated merchant purchases. Deduct "
                        "transfer fees and actual borrowing charges separately."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-release-decision-tree",
            "decision_tree",
            "Four Pre-Flight Decisions Before Capital Leaves",
            (
                "All four checks must pass; unresolved evidence "
                "means no release, not a higher-priced exception."
            ),
            5,
            "operating_framework",
            (
                "Render four sequential decision nodes with pass and fail "
                "branches described in each detail. Numeric values indicate "
                "decision order, not risk scores. State examples illustrate "
                "jurisdiction-specific analysis and are not nationwide exemptions."
            ),
            (
                "Federal business-purpose treatment, state lending authority, "
                "escrow safety, and usable liquidity are separate questions. "
                "Passing one never substitutes for passing the remaining three."
            ),
            [
                (
                    "Commercial purpose and transaction substance",
                    "Pass documented business-purpose facts; stop unsupported classifications.",
                    1.0,
                    (
                        "Apply 15 U.S.C. 1603(1) and 12 CFR 1026.3(a) "
                        "to the actual credit purpose where relevant. "
                        "An LLC borrower alone does not establish business "
                        "purpose. If consumer-purpose facts emerge, stop this "
                        "commercial workflow and assess the applicable consumer regime."
                    ),
                ),
                (
                    "State authority, charges, and security",
                    "Pass verified licensing and charge analysis; stop unresolved scope.",
                    2.0,
                    (
                        "Identify relevant state connections and document the "
                        "applicable license or exemption. Examine California "
                        "Financial Code section 22100 when applicable; examine "
                        "New York General Obligations Law section 5-501 and "
                        "Penal Law section 190.40 when applicable. Include "
                        "origination and fixed fees in the legally required "
                        "charge analysis. UCC 9-109(d)(11) prevents treating an "
                        "ordinary Article 9 filing as a substitute for real-property security."
                    ),
                ),
                (
                    "Escrow authority and unconditional buyer cash",
                    "Pass verified agent and cash evidence; stop dry closings.",
                    3.0,
                    (
                        "Verify settlement-agent licensing where required, "
                        "current bond or coverage evidence, beneficiary ownership, "
                        "and independently confirmed buyer cash. Check coverage "
                        "limits and exclusions rather than assuming every fraud "
                        "loss is covered. Conditional deposits, changed bank "
                        "details, or missing payoff authority stop disbursement."
                    ),
                ),
                (
                    "Permitted liquidity and repayment control",
                    "Pass actual facility terms; stop promotional-rate assumptions.",
                    4.0,
                    (
                        "Verify issuer-permitted use, cash-transfer eligibility, "
                        "transaction fees, available limits, and repayment dates. "
                        "Keep applications and proof-of-funds statements accurate; "
                        "18 U.S.C. 1014 applies to covered false statements. "
                        "If promotional pricing expires before a credible payoff "
                        "buffer, or repayment depends on new borrowing, reject "
                        "that source and use an independently acceptable facility."
                    ),
                ),
            ],
        ),
        (
            "diag-06-three-to-five-person-funding-pod",
            "org_architecture",
            "A Three-Person Core with Two Explicit Scale Additions",
            (
                "Conservative and Base Case use 1 FT + 2 C; "
                "Scaled Small-Team uses 2 FT + 3 C."
            ),
            11,
            "operating_framework",
            (
                "FT means full-time operator; C means contractor. Each node "
                "represents one person, not one full-time equivalent. "
                "The first three seats form the core pod; the last two "
                "are added only for the Scaled Small-Team scenario. "
                "Settlement agents and capital providers remain external "
                "counterparties rather than hidden pod headcount."
            ),
            (
                "Owner authorization and independent wire verification remain "
                "separate at both sizes. Automation assembles evidence and "
                "flags exceptions; it never independently changes beneficiary "
                "instructions or releases capital."
            ),
            [
                (
                    "Core seat: owner and capital lead",
                    "One full-time owner controls pricing and capital authorization.",
                    1.0,
                    (
                        "Own counterparty selection, capacity limits, charge "
                        "economics, and final wire authorization. Maintain "
                        "capital-provider agreements and decide whether a file "
                        "meets the desk's mandate. Receive verification evidence "
                        "from another person before authorizing funds."
                    ),
                ),
                (
                    "Core seat: underwriting contractor",
                    "One contractor verifies transaction evidence and wire instructions.",
                    1.0,
                    (
                        "Review contracts, business-purpose facts, jurisdiction "
                        "findings, payoff coverage, and settlement-agent records. "
                        "Perform independent callbacks and preserve the evidence "
                        "trail. In the core pod, this person verifies the "
                        "beneficiary while the owner authorizes release."
                    ),
                ),
                (
                    "Core seat: escrow-ledger contractor",
                    "One contractor reconciles principal, earned fees, and repayments.",
                    1.0,
                    (
                        "Maintain the QuickBooks subledger and reconcile it "
                        "against Qualia or SoftPro statements and bank records. "
                        "Separate principal assets and obligations from revenue, "
                        "track aged payoffs, and report unresolved variances "
                        "without editing bank beneficiaries."
                    ),
                ),
                (
                    "Scale addition: full-time operations lead",
                    "Add one full-time operator only in the scaled scenario.",
                    1.0,
                    (
                        "Own queue discipline, funding calendars, exposure "
                        "aggregation, contractor scheduling, and escalation timing. "
                        "Add this seat when measured file concurrency exceeds "
                        "documented core-pod capacity, rather than treating "
                        "the $950,000 revenue case as a three-person result."
                    ),
                ),
                (
                    "Scale addition: wire-control contractor",
                    "Add one contractor for independent settlement verification capacity.",
                    1.0,
                    (
                        "Take primary responsibility for authenticated callbacks, "
                        "beneficiary-change review, and archived verification "
                        "records. The owner retains release authority; the "
                        "underwriter retains transaction review. This addition "
                        "brings the scaled pod to two full-time people "
                        "and three contractors."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-four-bucket-allocation",
            "stacked_comparison",
            "Allocate a $75,000 Startup Budget Before Quoting Capacity",
            (
                "Four non-overlapping buckets sit inside the canonical "
                "$25,000–$100,000 USD startup range."
            ),
            4,
            "illustrative_model",
            (
                "Render one stacked $75,000 startup allocation with four "
                "segments. Numeric values are dollars, not annual expenses "
                "or scenario revenue. This selected budget does not imply "
                "that every operation needs the same proportions. "
                "Additional deployment capacity requires documented capital "
                "commitments; undrawn commitments and credit limits are "
                "not startup cash."
            ),
            (
                "$40,000 + $15,000 + $10,000 + $10,000 = $75,000. "
                "Only $40,000 is initially designated for deployment. "
                "Committed external capital and actual repayment timing "
                "must support any larger transaction volume."
            ),
            [
                (
                    "Deployable risk capital",
                    "$40,000 remains available for approved escrow funding.",
                    40000.0,
                    (
                        "Represent 53.33% of startup cash as deployable capital. "
                        "Set per-file and aggregate exposure limits below "
                        "available liquidity after outstanding wires. Returning "
                        "principal replenishes capacity; it does not create "
                        "recognized operator revenue."
                    ),
                ),
                (
                    "Operating runway",
                    "$15,000 supports recurring operations before reliable fee collections.",
                    15000.0,
                    (
                        "Represent 20.00% of startup cash as operating runway. "
                        "At the illustrative $5,350 monthly Base-Case overhead "
                        "allocation, this covers about 2.8 months of overhead "
                        "only, not capital carry or every contractor charge. "
                        "A four-month first-deal interval requires additional "
                        "runway or lower initial burn."
                    ),
                ),
                (
                    "Documentation and control setup",
                    "$10,000 funds jurisdiction work and secure operating setup.",
                    10000.0,
                    (
                        "Represent 13.33% of startup cash as a setup budget "
                        "for applicable licensing work, transaction documents, "
                        "insurance placement, secure intake, hardware security "
                        "keys, and restricted bank permissions. Obtain actual "
                        "quotes before committing deployment capacity."
                    ),
                ),
                (
                    "Contingency and liquidity reserve",
                    "$10,000 stays uncommitted for delays and operating shocks.",
                    10000.0,
                    (
                        "Represent 13.33% of startup cash as a segregated "
                        "liquidity reserve. Do not count it simultaneously "
                        "as committed loan funding. Reserve cash does not "
                        "replace the annual loss-expense assumption or make "
                        "a disputed escrow release acceptable."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-controlled-launch-roadmap",
            "timeline_roadmap",
            "Thirty Days to a Documented Funding Desk",
            (
                "Four weekly milestones establish operating readiness; "
                "the canonical first-deal window remains one to four months."
            ),
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days: 7, 14, 21, and 30. "
                "The final interval intentionally spans nine days. "
                "A day-30 pilot may remain an unfunded rehearsal if transaction, "
                "legal, capital, or escrow evidence is incomplete."
            ),
            (
                "Measure readiness through completed evidence, segregated "
                "permissions, and reconciled test files. Never compress "
                "underwriting or release conditions to satisfy a calendar target."
            ),
            [
                (
                    "Days 1-7: define the operating mandate",
                    "Finish jurisdiction scope, fee logic, and capital-source terms.",
                    7.0,
                    (
                        "Choose the initial state and transaction type, document "
                        "commercial-purpose facts, and establish applicable lender "
                        "and settlement requirements. Build the $75,000 startup "
                        "allocation and the exact three-scenario scorecard. "
                        "Record every facility's usable amount, charges, permitted "
                        "uses, and repayment timing."
                    ),
                ),
                (
                    "Days 8-14: implement evidence and permissions",
                    "Configure intake, independent callbacks, and a principal-separated ledger.",
                    14.0,
                    (
                        "Create restricted intake storage, a transaction checklist, "
                        "and QuickBooks accounts separating principal, fees, "
                        "capital costs, and losses. Assign owner authorization "
                        "and contractor verification permissions. Test a changed "
                        "beneficiary alert and document why the simulated "
                        "wire remains unreleased."
                    ),
                ),
                (
                    "Days 15-21: rehearse complete closing files",
                    "Complete two unfunded rehearsals and one failure exercise.",
                    21.0,
                    (
                        "Walk two sample files from contract intake through "
                        "Qualia or SoftPro statement review and payoff "
                        "reconciliation. Simulate missing buyer cash, a callback "
                        "mismatch, and a delayed return wire. Verify that "
                        "exception ownership and escalation timestamps remain visible."
                    ),
                ),
                (
                    "Days 22-30: pilot only a qualified transaction",
                    "Run one bounded pilot or preserve an unfunded readiness file.",
                    30.0,
                    (
                        "If all four pre-flight checks pass, use a documented "
                        "exposure cap, independently verified settlement instructions, "
                        "and daily payoff tracking. Otherwise continue sourcing "
                        "without disbursement. Compare actual earned fees and "
                        "costs with the Base-Case model; do not extrapolate "
                        "one closing into proven annual performance."
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
