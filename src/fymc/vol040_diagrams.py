from __future__ import annotations

VOLUME_040_SUBTITLE = (
    "The Complete Playbook for Self-Funded Health, PBM & Workers' Comp Arbitrage: "
    "$120,000–$950,000 USD in Annual Retained Revenue with a "
    "1 FT + 3 C Core Pod (4 People), Scaling to 6 People"
)

VOLUME_040_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Mid-Market Benefits Renewal Desk",
        "subtitle": (
            "Turn Form 5500 renewal intelligence into disclosed advisory fees "
            "and retained stop-loss and TPA commissions."
        ),
        "audience": (
            "Licensed benefits producers serving mid-market employers considering "
            "self-funded plans, captive participation, and transparent service contracts."
        ),
        "research_basis": (
            "DOL Form 5500 filings support account research, while available "
            "Schedules A and C reveal selected insurance and service-provider "
            "relationships. Self-funded plans do not necessarily report their "
            "stop-loss arrangements on Schedule A; confirm renewal dates directly. "
            "29 U.S.C. 1108(b)(2)(B), added by CAA 2021, establishes compensation "
            "disclosure requirements for covered group-health brokerage and consulting."
        ),
        "sources": [
            "https://www.dol.gov/agencies/ebsa/employers-and-advisers/"
            "plan-administration-and-compliance/reporting-and-filing/form-5500",
            "https://www.law.cornell.edu/uscode/text/29/1108",
            "https://www.law.cornell.edu/uscode/text/29/1104",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Transparent PBM Recovery Desk",
        "subtitle": (
            "Reconcile pharmacy pricing, rebate obligations, and retained advisory "
            "fees without treating employer savings as operator revenue."
        ),
        "audience": (
            "Benefits advisers and pharmacy analysts with authorized employer "
            "engagements, contract audit rights, and secure claims-processing arrangements."
        ),
        "research_basis": (
            "CMS NADAC provides a pharmacy acquisition-cost benchmark, not a "
            "complete measure of employer prescription cost or recoverable spread. "
            "Repricing requires NDC, quantity, dispensing fees, eligibility, rebate "
            "terms, and specialty exclusions. 29 U.S.C. 1185m addresses prohibited "
            "gag clauses; HIPAA business-associate requirements constrain claims handling."
        ),
        "sources": [
            "https://www.medicaid.gov/medicaid/prescription-drugs/"
            "pharmacy-pricing/index.html",
            "https://www.law.cornell.edu/uscode/text/29/1185m",
            "https://www.ecfr.gov/current/title-45/subtitle-A/"
            "subchapter-C/part-164/subpart-E/section-164.504",
            "https://www.ecfr.gov/current/title-45/subtitle-A/"
            "subchapter-C/part-164/subpart-C/section-164.308",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Workers' Comp E-Mod Correction Desk",
        "subtitle": (
            "Convert documented payroll-code and experience-rating errors into "
            "carrier-approved corrections and collected contingent fee splits."
        ),
        "audience": (
            "Licensed Property & Casualty producers working with payroll specialists "
            "and experience-rating analysts on employer-authorized premium audits."
        ),
        "research_basis": (
            "Experience-rating procedures depend on the applicable state and rating "
            "organization; NCCI methods are not universal. California Insurance "
            "Code 11734 addresses experience-rating plans, and section 1631 "
            "establishes insurance licensing requirements. Validate payroll classes, "
            "loss runs, valuation dates, and correction deadlines before asserting "
            "a recoverable overcharge."
        ),
        "sources": [
            "https://leginfo.legislature.ca.gov/faces/"
            "codes_displaySection.xhtml?lawCode=INS&sectionNum=11734.",
            "https://leginfo.legislature.ca.gov/faces/"
            "codes_displaySection.xhtml?lawCode=INS&sectionNum=1631.",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_040_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-authorized-renewal-to-retained-fees",
            "process_flow",
            "From Renewal Signal to Retained Operator Revenue",
            "Five operating stages separate employer claim dollars from earned fees.",
            1,
            "operating_framework",
            (
                "Employer authorization, appropriate producer licenses, service "
                "agreements, and claims-access controls precede account-level work. "
                "The expected first-deal window is 2–5 months."
            ),
            (
                "The desk sells documented analysis and execution. Employer claim "
                "funds, premiums, rebate principal, and premium refunds remain "
                "outside operator revenue except for the contractual earned fee."
            ),
            [
                (
                    "Research the renewal",
                    "Form 5500 account intelligence",
                    1.0,
                    (
                        "Search DOL EFAST2 filings and available Schedules A/C for "
                        "employer, broker, and service-provider signals. Confirm "
                        "renewal timing and self-funded status directly rather than "
                        "assuming every stop-loss policy appears in public filings."
                    ),
                ),
                (
                    "Authorize the engagement",
                    "Licenses, scope, and compensation",
                    2.0,
                    (
                        "Verify state Life & Health and Property & Casualty "
                        "authority for the actual activities. Deliver covered "
                        "ERISA section 408(b)(2) disclosures and execute employer "
                        "authorization, fee terms, and applicable HIPAA agreements."
                    ),
                ),
                (
                    "Reconcile the evidence",
                    "PBM, stop-loss, and E-Mod analysis",
                    3.0,
                    (
                        "Normalize claims and contracts; compare NADAC with matched "
                        "NDC quantities and dispensing fees. Reconcile rebate "
                        "eligibility, payroll classes, loss runs, and rating "
                        "worksheets before labeling a difference recoverable."
                    ),
                ),
                (
                    "Implement the correction",
                    "Written terms and accountable owners",
                    4.0,
                    (
                        "Document specific and aggregate stop-loss attachments, "
                        "lasers, run-out coverage, and reference-based-pricing "
                        "balance-bill defense. Submit supported rating corrections "
                        "through the carrier or applicable bureau process."
                    ),
                ),
                (
                    "Recognize retained fees",
                    "Earned service revenue only",
                    5.0,
                    (
                        "Invoice PEPM services, reconcile retained commissions, "
                        "and recognize contingent splits when contractual earning "
                        "conditions and applicable variable-consideration criteria "
                        "are satisfied. Track cash collection separately."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-renewal-account-funnel",
            "funnel",
            "A Nested Renewal-to-Client Cohort",
            "400 researched employers narrow to 20 signed service accounts.",
            6,
            "illustrative_model",
            (
                "Illustrative annual cohort, not observed conversion performance. "
                "Each stage is a subset of the preceding stage; count unique "
                "employers once even when an account buys several services."
            ),
            (
                "The 5% end-to-end conversion is a planning assumption. Twenty "
                "signed accounts can support the illustrative Base revenue mix "
                "only when its lives, contracts, earning conditions, and full-year "
                "service periods also hold."
            ),
            [
                (
                    "Researched employers",
                    "400 unique employer accounts",
                    400.0,
                    (
                        "Deduplicate public filing records by employer identity. "
                        "Record the evidence date, broker relationship, likely "
                        "renewal window, and a legitimate business contact channel."
                    ),
                ),
                (
                    "Qualified renewal fits",
                    "200 accounts; 50% of prior stage",
                    200.0,
                    (
                        "Confirm employer size, renewal timing, decision-maker "
                        "access, and an identifiable PBM, stop-loss, or workers' "
                        "comp problem; exclude accounts outside the desk's authority."
                    ),
                ),
                (
                    "Completed discovery",
                    "80 accounts; 40% of prior stage",
                    80.0,
                    (
                        "Hold documented discovery with the employer's authorized "
                        "contact. Establish incumbent contract restrictions, available "
                        "records, procurement timing, and the economic buyer."
                    ),
                ),
                (
                    "Authorized diagnostic audits",
                    "40 accounts; 50% of prior stage",
                    40.0,
                    (
                        "Obtain signed scope and secure access to necessary "
                        "records. Complete a diagnostic with reproducible calculations "
                        "before proposing contingent recovery or replacement coverage."
                    ),
                ),
                (
                    "Signed service accounts",
                    "20 accounts; 50% of prior stage",
                    20.0,
                    (
                        "Execute service terms and required compensation disclosures. "
                        "These accounts overlap across revenue rails; signed status "
                        "alone does not establish earned revenue or collected cash."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-retained-revenue-profit-waterfall",
            "waterfall",
            "Base Economics: $535,000 to $240,750",
            "Four expense deductions leave exactly 45.0% annual owner net profit.",
            3,
            "illustrative_model",
            (
                "Formula v2.0 Base anchors are $535,000 annual operator revenue, "
                "$294,250 total expense, and $240,750 owner net profit. Expense "
                "categories are an illustrative allocation, not additional scorecard "
                "inputs. First and last bars are absolute totals; intermediate "
                "bars are signed deductions."
            ),
            (
                "The scorecard's gross revenue is already the operator's net "
                "retained fee and commission basis. Do not apply a second retained "
                "share haircut or add employer premiums and claim funds. Evaluate "
                "ASC 606 principal-agent presentation by contract."
            ),
            [
                (
                    "Retained operator revenue",
                    "$535,000 annual starting total",
                    535000.0,
                    (
                        "Combine earned PEPM advisory fees, retained stop-loss "
                        "and TPA commissions, PBM advisory fees, and earned E-Mod "
                        "refund splits. Exclude all underlying employer fund flows."
                    ),
                ),
                (
                    "Delivery labor",
                    "Subtract $168,000; $367,000 remains",
                    -168000.0,
                    (
                        "Budget delivery payroll or contracted capacity, specialist "
                        "analysis, and account execution. Include each delivery "
                        "expense once; owner distributions come from the final "
                        "profit rather than creating another expense deduction."
                    ),
                ),
                (
                    "Secure systems and records",
                    "Subtract $36,000; $331,000 remains",
                    -36000.0,
                    (
                        "Cover encrypted storage, access logging, secure transfer, "
                        "CRM administration, claims normalization, and permitted "
                        "benchmark access. Do not place identifiable claims in "
                        "unapproved general-purpose collaboration systems."
                    ),
                ),
                (
                    "Acquisition and renewals",
                    "Subtract $48,000; $283,000 remains",
                    -48000.0,
                    (
                        "Fund employer research, referral development, renewal "
                        "outreach, travel, and proposal execution. Account for "
                        "the incumbent broker's defense and delayed procurement "
                        "rather than booking every proposal as won."
                    ),
                ),
                (
                    "Insurance and administration",
                    "Subtract $42,250; $240,750 remains",
                    -42250.0,
                    (
                        "Cover professional liability and cyber coverage, licensing, "
                        "contract review, bookkeeping, and ordinary administration. "
                        "This is an expense allocation, not an employer claims "
                        "reserve or an additional retained-share deduction."
                    ),
                ),
                (
                    "Owner net profit",
                    "$240,750 annual ending total",
                    240750.0,
                    (
                        "$535,000 minus $168,000, $36,000, $48,000, and $42,250 "
                        "equals $240,750. Dividing the ending profit by $535,000 "
                        "gives exactly 45.0%; this final total is not another increment."
                    ),
                ),
            ],
        ),
        (
            "diag-04-base-payment-rail-yields",
            "horizontal_bars",
            "Five Payment Rails Behind the Base Case",
            "Illustrative annual retained revenue contributions sum to $535,000.",
            2,
            "illustrative_model",
            (
                "Bars measure annual earned operator dollars, not yield percentages "
                "or employer savings. Contract volumes and prices are illustrative. "
                "Accounts may overlap across rails, but the same fee cannot be "
                "recognized twice."
            ),
            (
                "Revenue mix: $240,000 + $110,000 + $55,000 + $90,000 + "
                "$40,000 = $535,000. All commissions are shown after external "
                "splits; PBM advisory fees must be distinct from PEPM scope."
            ),
            [
                (
                    "Self-funded PEPM advisory",
                    "$240,000 from 1,000 covered employees",
                    240000.0,
                    (
                        "Charge an illustrative $20 per employee per month across "
                        "1,000 covered employees for 12 months. Validate the "
                        "billing denominator, eligibility roster, service commencement, "
                        "and termination adjustments in each contract."
                    ),
                ),
                (
                    "Stop-loss placement commissions",
                    "$110,000 from 10 retained commissions",
                    110000.0,
                    (
                        "Ten annual placements retain $11,000 each after external "
                        "splits. Disclose direct and indirect compensation, model "
                        "chargebacks, and exclude the employer's full stop-loss "
                        "premium from operator revenue."
                    ),
                ),
                (
                    "TPA placement commissions",
                    "$55,000 from 11 retained commissions",
                    55000.0,
                    (
                        "Eleven TPA arrangements retain $5,000 each under written "
                        "compensation schedules. Disclose the payer and compensation "
                        "method; check state administrator rules before performing "
                        "activities beyond licensed placement and advice."
                    ),
                ),
                (
                    "PBM contract advisory",
                    "$90,000 from six separate mandates",
                    90000.0,
                    (
                        "Six earned advisory mandates generate $15,000 each for "
                        "contract reconciliation and repricing work outside PEPM "
                        "scope. Employer rebates and projected drug savings remain "
                        "outside the desk's revenue."
                    ),
                ),
                (
                    "Workers' comp recovery splits",
                    "$40,000 from four collected fee shares",
                    40000.0,
                    (
                        "Four completed corrections each produce a $10,000 fee, "
                        "illustratively 25% of a $40,000 employer refund. Only "
                        "the $40,000 aggregate fee share enters operator revenue; "
                        "$160,000 aggregate refunds do not."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-and-risk-preflight",
            "decision_tree",
            "Four Pre-Flight Decisions Before Execution",
            "Proceed only on documented authority, disclosures, access, and risk terms.",
            5,
            "operating_framework",
            (
                "These are sequential pass-or-remediate decisions, not alternative "
                "routes around a failed check. State requirements depend on the "
                "jurisdiction, product, and activities actually performed."
            ),
            (
                "A failed check pauses the affected activity while the team "
                "corrects its scope or evidence. Public account research can "
                "continue without accessing employer claim records."
            ),
            [
                (
                    "Licensed for the activity?",
                    "Pass to disclosures; otherwise rescope",
                    1.0,
                    (
                        "Verify active Life & Health and Property & Casualty "
                        "producer authority, appointments where required, and "
                        "applicable TPA or adjuster requirements. California "
                        "Insurance Code 1631 is one state example; a producer "
                        "license alone does not authorize every administrative role."
                    ),
                ),
                (
                    "Compensation properly disclosed?",
                    "Pass to access; otherwise correct documents",
                    2.0,
                    (
                        "For covered arrangements under 29 U.S.C. 1108(b)(2)(B), "
                        "identify services, direct and indirect compensation, "
                        "payers, and payment methods; furnish required disclosures "
                        "reasonably before execution, extension, or renewal. "
                        "Reconcile PBM and carrier payments with employer-facing terms."
                    ),
                ),
                (
                    "Claims access properly controlled?",
                    "Pass to terms; otherwise restrict processing",
                    3.0,
                    (
                        "Apply 45 CFR 164.502(b) minimum-necessary requirements "
                        "where applicable, 164.504(e) business-associate arrangements, "
                        "and 164.308 security safeguards. Verify plan-sponsor access "
                        "conditions and role separation rather than treating employer "
                        "ownership as unrestricted permission to inspect health records."
                    ),
                ),
                (
                    "Coverage and corrections supportable?",
                    "Proceed with evidence; otherwise redesign scope",
                    4.0,
                    (
                        "For ERISA fiduciary decisions, document the prudent process "
                        "under 29 U.S.C. 1104. Test lasers, attachment points, "
                        "run-out, exclusions, and balance-bill defense. For E-Mod "
                        "work, use the applicable bureau rules, correction deadlines, "
                        "and supported payroll and loss evidence."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-person-core-six-person-scale",
            "org_architecture",
            "Four Core Seats, Two Expansion Seats",
            "Base uses 1 FT + 3 C; Scaled uses 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT means full-time and C means contractor. Numeric values show "
                "Base seat counts, so the last two seats are zero until expansion. "
                "Contractor headcount is not equivalent to full-time capacity."
            ),
            (
                "Canonical annual scenarios remain separate: Conservative "
                "$120,000 revenue at 32% produces $38,400 profit with four people; "
                "Base $535,000 at 45.0% produces $240,750 with four; Scaled "
                "$950,000 at 58% produces $551,000 with six."
            ),
            [
                (
                    "Principal and account owner",
                    "1 FT in Base and Scaled",
                    1.0,
                    (
                        "Own employer relationships, engagement scope, compensation "
                        "disclosures, collections, and final commercial decisions. "
                        "Maintain licenses required for personal activities and "
                        "assign specialist work without delegating accountability."
                    ),
                ),
                (
                    "Licensed benefits specialist",
                    "1 C in Base and Scaled",
                    1.0,
                    (
                        "Run stop-loss and TPA market work, compare policy wording, "
                        "document lasers and attachment points, and reconcile "
                        "commission schedules. Escalate coverage mismatches before "
                        "the employer commits to replacement terms."
                    ),
                ),
                (
                    "PBM and claims analyst",
                    "1 C in Base and Scaled",
                    1.0,
                    (
                        "Maintain authorized claims extracts, NADAC matching, rebate "
                        "reconciliation, and reproducible calculations using Python "
                        "and SQL. Minimize identifiers and preserve source-to-output "
                        "audit trails for each employer engagement."
                    ),
                ),
                (
                    "Licensed workers' comp specialist",
                    "1 C in Base and Scaled",
                    1.0,
                    (
                        "Reconcile payroll classes, experience-rating worksheets, "
                        "loss runs, and carrier responses. Verify state-specific "
                        "producer or adjuster authority and obtain written evidence "
                        "for every proposed correction and contingent fee."
                    ),
                ),
                (
                    "Expansion account manager",
                    "0 Base seats; add 1 FT at Scaled",
                    0.0,
                    (
                        "Add a full-time service owner for renewals, eligibility "
                        "coordination, employer reporting, and collection follow-up. "
                        "Licensed personnel retain regulated advice and placement "
                        "responsibilities unless this seat also holds required authority."
                    ),
                ),
                (
                    "Expansion clinical reviewer",
                    "0 Base seats; add 1 C at Scaled",
                    0.0,
                    (
                        "Add appropriately qualified clinical review capacity for "
                        "authorized complex-claim analysis and stop-loss submission "
                        "support. Limit access by role; carrier contracts and "
                        "authorized decision-makers determine coverage and payment."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $8,000–$45,000 Without Funding Claims",
            "Four buckets compare lean, working, and expanded launch budgets.",
            4,
            "illustrative_model",
            (
                "Numeric values represent a $25,000 working launch budget. "
                "Each stage also supplies lean and expanded allocations; their "
                "totals are $8,000 and $45,000 respectively. These are capital "
                "budgets, not annual revenue or recurring expense totals."
            ),
            (
                "Working allocation totals $6,000 + $6,500 + $4,500 + $8,000 "
                "= $25,000. Liquidity supports the 2–5 month first-deal window; "
                "none of these buckets capitalizes employer claim liabilities."
            ),
            [
                (
                    "Licensing, contracts, and coverage",
                    "Lean $2,000 / Working $6,000 / Expanded $9,000",
                    6000.0,
                    (
                        "Fund required licensing work, professional liability and "
                        "cyber coverage deposits, service agreements, and compensation "
                        "disclosure templates. The lean allocation assumes existing "
                        "relevant licenses and a tightly limited initial service scope."
                    ),
                ),
                (
                    "Secure analysis infrastructure",
                    "Lean $1,500 / Working $6,500 / Expanded $11,000",
                    6500.0,
                    (
                        "Provision encrypted storage, multifactor authentication, "
                        "role-based access, logging, secure transfer, and claims "
                        "normalization. Use public CMS benchmarks and DOL filings "
                        "without assuming all required contract records are public."
                    ),
                ),
                (
                    "Account acquisition and proposals",
                    "Lean $1,500 / Working $4,500 / Expanded $8,000",
                    4500.0,
                    (
                        "Build a verified renewal list, referral materials, "
                        "discovery scripts, and evidence-backed proposals. Track "
                        "cost per completed discovery rather than celebrating "
                        "unqualified contact counts or speculative recoveries."
                    ),
                ),
                (
                    "Operating liquidity reserve",
                    "Lean $3,000 / Working $8,000 / Expanded $17,000",
                    8000.0,
                    (
                        "Bridge recurring cash expenses and collection delays. "
                        "At $2,000 monthly opex, reserves cover 1.5, 4, and "
                        "8.5 months respectively; at $11,000, they cover about "
                        "0.27, 0.73, and 1.55 months. Reconcile spending to runway."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Operating Desk",
            "Four weekly milestones establish capability, not booked annual revenue.",
            12,
            "operating_framework",
            (
                "Milestones are operating targets. Required licenses and access "
                "permissions may take longer than this sprint; affected activities "
                "remain paused. The canonical time to first deal is 2–5 months."
            ),
            (
                "Day 30 should produce a working acquisition and diagnostic "
                "system, signed scope where available, and clear next actions. "
                "Do not convert a diagnostic estimate into collected fee revenue."
            ),
            [
                (
                    "Days 1-7",
                    "Define authority, scope, and unit economics",
                    7.0,
                    (
                        "Choose one employer segment and initial service rail. "
                        "Build a state-activity licensing matrix, draft engagement "
                        "and disclosure documents, obtain coverage quotes, and "
                        "reconcile the $535,000 Base revenue and $294,250 expense model."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build secure intake and renewal intelligence",
                    14.0,
                    (
                        "Configure access controls and secure transfer, test intake "
                        "with synthetic records, and research 50 deduplicated "
                        "employers from public filings. Confirm renewal dates "
                        "directly and avoid placing health records in the CRM."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run discovery and one bounded diagnostic",
                    21.0,
                    (
                        "Target five completed discovery calls and one signed "
                        "diagnostic scope. With required authority and access in "
                        "place, reconcile a limited PBM or E-Mod sample; "
                        "otherwise continue testing only with synthetic records."
                    ),
                ),
                (
                    "Days 22-30",
                    "Deliver evidence and schedule the commercial path",
                    30.0,
                    (
                        "Present a reproducible findings pack separating potential "
                        "employer savings from operator fees. Identify contract "
                        "restrictions, risk owners, implementation dates, and "
                        "collection conditions; schedule renewal follow-up inside "
                        "the realistic 2–5 month first-deal window."
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
