from __future__ import annotations

VOLUME_044_SUBTITLE = (
    "The Complete Playbook for Customs Duty Drawback, Tariff Refund & "
    "Antitrust Claim Recovery: $110,000–$920,000 USD in Annual Earned Fees, "
    "Built Around a 1 FT + 3 C (4 People) Pod, Expanding to Six at Scale"
)

VOLUME_044_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Import-to-Export Recovery Desk",
        "subtitle": (
            "Turn documented import duties and qualifying export evidence into "
            "broker-filed drawback claims with earned contingency economics."
        ),
        "audience": (
            "Importers, exporters, and recovery operators serving repeat inventory "
            "movements with traceable entry, product, and export records."
        ),
        "research_basis": (
            "19 U.S.C. § 1313 and 19 CFR Part 190 support distinct drawback "
            "routes with route-specific eligibility, timing, and evidence requirements. "
            "The positioning emphasizes unused-merchandise claims, qualifying "
            "substitution, and licensed filing rather than treating every tariff "
            "payment as recoverable. The commercial hypothesis is a zero-upfront "
            "25%–35% contingency on realized eligible recoveries."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/19/1313",
            "https://www.ecfr.gov/current/title-19/chapter-I/part-190",
            "https://www.ecfr.gov/current/title-19/chapter-I/part-111",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Liquidation-Clock Refund Desk",
        "subtitle": (
            "Separate pre-liquidation corrections from statutory protests, then "
            "price evidence work against collectible duty refunds."
        ),
        "audience": (
            "Importer finance teams and specialist operators managing classification, "
            "valuation, origin, or other documented entry errors with trade professionals."
        ),
        "research_basis": (
            "19 U.S.C. § 1514 establishes protestable decisions and generally "
            "requires protest within 180 days of liquidation or the applicable "
            "protestable decision. ACE Post-Summary Correction is a separate "
            "pre-liquidation mechanism, not a substitute name for a protest. "
            "Licensed customs brokers or trade counsel assess the available "
            "route before the operator assigns expected fee value."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/19/1514",
            "https://www.ecfr.gov/current/title-19/chapter-I/part-174",
            "https://www.ecfr.gov/current/title-19/chapter-I/part-111",
            "https://www.cbp.gov/trade/programs-administration/entry-summary",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The B2B Settlement Evidence Desk",
        "subtitle": (
            "Package eligible purchase and interchange records for existing "
            "court-approved antitrust settlement distributions."
        ),
        "audience": (
            "Multi-location merchants, procurement-heavy businesses, and recovery "
            "operators able to reconcile historical accounts-payable and processing records."
        ),
        "research_basis": (
            "15 U.S.C. § 15 supplies a private antitrust damages framework, while "
            "Federal Rule of Civil Procedure 23 and each settlement's orders, "
            "class definition, plan of allocation, and administrator instructions "
            "control class participation and distribution. This positioning covers "
            "administrative evidence services for existing settlements, not litigation "
            "origination. Required third-party filer disclosures explain that eligible "
            "claimants may file directly at zero cost."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/15",
            "https://www.law.cornell.edu/rules/frcp/rule_23",
            "https://www.uscourts.gov/court-records/find-case-pacer",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_044_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-three-lane-recovery-workflow",
            "process_flow",
            "One Evidence Desk, Three Distinct Recovery Lanes",
            "Classify first; verify eligibility before assigning collectible value.",
            1,
            "operating_framework",
            (
                "Drawback, tariff refunds, and antitrust distributions are alternative "
                "routes through this workflow, not sequential recoveries on the same "
                "dollars. Importer duty principal, merchant purchase volume, and gross "
                "settlement pools never become operator revenue. Formal customs "
                "filings use a licensed 19 CFR Part 111 customs broker or trade "
                "counsel with valid Customs Powers of Attorney."
            ),
            (
                "The operator sells evidence assembly and recovery coordination; "
                "only earned contingency fees enter the revenue scorecard."
            ),
            [
                (
                    "Authorize the account",
                    "Written scope and record access",
                    1.0,
                    (
                        "Execute the recovery agreement, identify the claimant entity, "
                        "document record-access authority, and price a zero-upfront "
                        "25%–35% contingency on realized recoveries. Obtain the required "
                        "Customs Power of Attorney directly for the filing professional."
                    ),
                ),
                (
                    "Route the recovery",
                    "Three separate eligibility ledgers",
                    2.0,
                    (
                        "Create distinct ledgers for 19 U.S.C. § 1313 drawback, "
                        "19 U.S.C. § 1514 protests or ACE Post-Summary Correction, "
                        "and existing B2B antitrust settlements. Assign each ledger "
                        "its own deadline, collectible base, cost budget, and cash estimate."
                    ),
                ),
                (
                    "Reconcile primary evidence",
                    "Entry, export, or purchase proof",
                    3.0,
                    (
                        "Use ImportGenius or Panjiva for discovery, then reconcile "
                        "authorized ACE CBP Form 7501 records, duty payments, export "
                        "bills of lading, and inventory movements. For settlements, "
                        "reconcile accounts-payable or processor records to class periods. "
                        "Manifest matches and eight-digit HTS matches are candidate "
                        "links, not proof of statutory eligibility."
                    ),
                ),
                (
                    "Submit the correct packet",
                    "Professional filing or permitted submission",
                    4.0,
                    (
                        "The broker or trade counsel files the correct customs route "
                        "and retains Part 190 evidence for drawback. Settlement packets "
                        "follow the court-approved claim form, allocation plan, "
                        "third-party filer rules, and claimant authorization. Block "
                        "duplicate claims and unsupported substitutions before submission."
                    ),
                ),
                (
                    "Reconcile cash and fee",
                    "Realized recovery to earned revenue",
                    5.0,
                    (
                        "Match the agency refund or administrator distribution to "
                        "the claimant ledger, resolve offsets and reversals, and "
                        "calculate the contracted earned fee. Record client recovery "
                        "principal separately from operator consideration; retain an "
                        "auditable bridge from payment notice to fee invoice."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-nested-cohort-funnel",
            "funnel",
            "From 240 Screened Accounts to 20 Paid Accounts",
            "Illustrative mature annual cohort supporting $515,000 in earned fees.",
            6,
            "illustrative_model",
            (
                "Every stage is a subset of the preceding account cohort, with one "
                "primary lane assigned per account to avoid double counting. Counts "
                "are planning assumptions, not observed conversion rates. Twenty paid "
                "accounts comprise ten drawback accounts, six tariff-refund accounts, "
                "and four settlement accounts. At an illustrative 30% fee, recoveries "
                "of $1,000,000, $500,000, and $216,666.67 produce $300,000, $150,000, "
                "and $65,000 in fees after cent rounding. Remaining submitted accounts "
                "are still pending, deficient, or unpaid at the measurement date."
            ),
            (
                "The cohort converts 8.33% of screened accounts into paid accounts; "
                "average earned fees are $25,750 per paid account."
            ),
            [
                (
                    "Screened accounts",
                    "240 accounts; starting cohort",
                    240.0,
                    (
                        "Identify importer-exporter pairs, documented entry-error "
                        "candidates, and businesses potentially inside an existing "
                        "settlement class. Count businesses once, rather than counting "
                        "each entry, shipment, or purchase as a separate prospect."
                    ),
                ),
                (
                    "Authorized evidence access",
                    "120 accounts; 50% of starting cohort",
                    120.0,
                    (
                        "Obtain written authority and usable source records from "
                        "120 of the 240 screened accounts. Exclude businesses "
                        "whose records cannot be accessed through authorized channels "
                        "or whose contracting entity cannot establish ownership."
                    ),
                ),
                (
                    "Eligibility substantiated",
                    "60 accounts; 50% of prior cohort",
                    60.0,
                    (
                        "Validate deadlines, claimant identity, statutory route, "
                        "recoverable duty components, or settlement class membership. "
                        "Remove prohibited duties, expired remedies, unsupported exports, "
                        "and purchases outside the court-defined class period."
                    ),
                ),
                (
                    "Complete packets submitted",
                    "40 accounts; 66.67% of prior cohort",
                    40.0,
                    (
                        "Submit forty complete account packets through the required "
                        "filing channel. Record submission acknowledgments and track "
                        "all agency or administrator requests without treating "
                        "submitted claim amounts as earned fee revenue."
                    ),
                ),
                (
                    "Cash realized and fees earned",
                    "20 accounts; 50% of prior cohort",
                    20.0,
                    (
                        "Recognize $515,000 in earned operator fees from paid "
                        "recoveries, not from requested awards. Ten drawback accounts "
                        "average $30,000 in fees, six refund accounts average $25,000, "
                        "and four settlement accounts average $16,250."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-fee-profit-waterfall",
            "waterfall",
            "$515,000 Earned Fees to $231,750 Owner Profit",
            "Six bars reconcile the Formula v2.0 Base-Case 45.0% net margin.",
            3,
            "illustrative_model",
            (
                "The first bar is gross operator fee revenue, the next four are "
                "negative expense movements, and the final bar is an absolute ending "
                "total rather than an additional movement. All figures are annual USD. "
                "The operator earns its own contracted fees; client recovery principal "
                "is excluded rather than grossed up and reduced by a retained-share "
                "factor. ASC 606 principal-versus-agent assessment still applies to "
                "third-party consideration. Owner profit is after the modeled business "
                "expenses, before owner personal taxes, with no extra owner salary "
                "deducted. Contractor fees plus evidence costs are variable delivery "
                "costs; technology plus overhead are recurring operating costs."
            ),
            (
                "$515,000 − $174,000 − $36,000 − $28,500 − $44,750 = $231,750; "
                "$231,750 ÷ $515,000 = 45.0%."
            ),
            [
                (
                    "Earned operator fees",
                    "$515,000 annual fee revenue",
                    515000.0,
                    (
                        "The illustrative lane mix contributes $300,000 from drawback, "
                        "$150,000 from tariff refunds, and $65,000 from settlement "
                        "distributions. Approximately $1.717 million in client recoveries "
                        "supports these fees at 30%; that recovery principal is excluded."
                    ),
                ),
                (
                    "Contractor delivery expense",
                    "−$174,000 annual specialist expense",
                    -174000.0,
                    (
                        "Budget the three core contractors collectively: licensed "
                        "broker, evidence analyst, and trade or settlement counsel. "
                        "Their compensation is an operator expense, not a second "
                        "claim against the client's recovered principal."
                    ),
                ),
                (
                    "Evidence acquisition expense",
                    "−$36,000 annual case expense",
                    -36000.0,
                    (
                        "Budget purchased records, scanning, retrieval, and secure "
                        "document delivery separately from contractor labor. Paid "
                        "accounts consume $24,600 under lane budgets; another $11,400 "
                        "covers screened, unresolved, and unsuccessful account evidence."
                    ),
                ),
                (
                    "Technology and subscriptions",
                    "−$28,500 annual platform expense",
                    -28500.0,
                    (
                        "Cover manifest intelligence, authorized record reconciliation, "
                        "secure storage, accounting, and document workflow software. "
                        "Do not assume public manifests replace private entry evidence "
                        "or provide unrestricted ACE account access."
                    ),
                ),
                (
                    "Insurance and operating overhead",
                    "−$44,750 annual overhead expense",
                    -44750.0,
                    (
                        "Cover insurance, accounting, prospecting, routine administration, "
                        "and modest bond-related expense where contracted. Together "
                        "with technology, recurring costs total $73,250 annually, or "
                        "$6,104.17 monthly, inside the $1,500–$9,500 planning range."
                    ),
                ),
                (
                    "Owner operating profit",
                    "$231,750 ending total; 45.0% margin",
                    231750.0,
                    (
                        "Total annual expenses equal $283,250. Conservative economics "
                        "remain $110,000 revenue, $74,800 expenses, and $35,200 profit "
                        "at 32%; scaled economics remain $920,000 revenue, $386,400 "
                        "expenses, and $533,600 profit at 58%."
                    ),
                ),
            ],
        ),
        (
            "diag-04-collectible-base-fee-yield",
            "horizontal_bars",
            "Five Fee Yields on the Same $100,000 Recovery",
            "Compare earned operator fees, not import value or settlement pool size.",
            2,
            "illustrative_model",
            (
                "Each independent bar assumes $100,000 of realized eligible client "
                "recovery and a stated illustrative contingency within 25%–35%. "
                "Bars show revenue before delivery costs, not net profit, expected "
                "claim value, or additive annual forecasts. Drawback recovery is "
                "calculated after applicable statutory limits, often 99% of qualifying "
                "duties, taxes, and fees; $100,000 here is the actual recovery base. "
                "Fee terms require client acceptance and must fit the applicable "
                "filing arrangement and any settlement-specific restrictions."
            ),
            (
                "Higher headline percentages do not offset weak evidence, delayed "
                "cash, duplicate claims, or nonrecoverable duty components."
            ),
            [
                (
                    "Direct unused-merchandise drawback",
                    "$25,000 fee at 25%",
                    25000.0,
                    (
                        "Use a substantiated 19 U.S.C. § 1313(j)(1) claim with "
                        "qualifying unused merchandise and timely export or destruction. "
                        "Specific identification and clean inventory tracing support "
                        "the lower illustrative service rate."
                    ),
                ),
                (
                    "Substitution drawback",
                    "$35,000 fee at 35%",
                    35000.0,
                    (
                        "Use a qualifying 19 U.S.C. § 1313(j)(2) route with "
                        "the applicable eight-digit HTS classification test, possession "
                        "requirements, special classification restrictions, and valuation "
                        "limits. Identical tariff codes alone do not establish eligibility."
                    ),
                ),
                (
                    "ACE entry correction refund",
                    "$25,000 fee at 25%",
                    25000.0,
                    (
                        "Correct an eligible unliquidated entry through ACE Post-Summary "
                        "Correction using documented classification, valuation, or origin "
                        "facts. The filing professional verifies current CBP timing "
                        "rules and entry-type restrictions before preparing the correction."
                    ),
                ),
                (
                    "Timely liquidation protest",
                    "$35,000 fee at 35%",
                    35000.0,
                    (
                        "Use 19 U.S.C. § 1514 and 19 CFR Part 174 for "
                        "a protestable decision filed within the applicable deadline. "
                        "The collectible base is the supported refund actually paid, "
                        "not the full duties shown on every challenged entry."
                    ),
                ),
                (
                    "B2B settlement distribution",
                    "$30,000 fee at 30%",
                    30000.0,
                    (
                        "Package eligible purchase or interchange records for an "
                        "existing court-approved settlement. Apply the fee only to "
                        "the client's realized distribution under accepted terms, "
                        "with required filer disclosures and direct-filing information."
                    ),
                ),
            ],
        ),
        (
            "diag-05-lane-specific-preflight-decision-tree",
            "decision_tree",
            "Four Checks Before Valuing a Claim",
            "Test the selected lane, then apply the shared authority and cash check.",
            5,
            "operating_framework",
            (
                "The first three nodes are alternative lane branches; an eligible "
                "branch proceeds to the fourth shared check. A failed eligibility "
                "test stops that lane unless a documented correction remains possible. "
                "Documentation budgets are incremental purchased-evidence costs per "
                "paid account and exclude contractor labor. Cash windows are "
                "illustrative planning intervals from a complete filing to receipt, "
                "not agency or administrator service commitments."
            ),
            (
                "Separate eligibility, collectible base, evidence expense, surety "
                "exposure, and payment timing before assigning expected fee value."
            ),
            [
                (
                    "Drawback eligibility",
                    "If eligible, continue to shared check",
                    1.0,
                    (
                        "Apply 19 U.S.C. § 1313 and 19 CFR Part 190, including "
                        "the applicable export or destruction requirements and generally "
                        "the five-year claim-completion limit measured from importation. "
                        "Exclude duties barred from drawback, including antidumping and "
                        "countervailing duties. Base value on qualifying refundable duty "
                        "components after statutory limits. Budget $1,500 in evidence "
                        "cost per paid account. Accelerated payment requires applicable "
                        "CBP authorization and bond coverage; without it, plan standard "
                        "payment. Model 6–18 months for standard recovery, potentially longer."
                    ),
                ),
                (
                    "Tariff-refund route",
                    "Choose correction or timely protest",
                    2.0,
                    (
                        "Use PSC only for eligible unliquidated entries, ordinarily "
                        "within 300 days of entry and at least 15 days before "
                        "scheduled liquidation, whichever deadline arrives first. Use "
                        "19 U.S.C. § 1514 protests generally within 180 days of "
                        "liquidation or the applicable protestable decision. Base value "
                        "on substantiated overpaid duties. Budget $1,200 per paid account. "
                        "An ordinary refund request has no drawback accelerated-payment "
                        "bond, although existing entry bonds remain separate. Model "
                        "3–12 months after a complete filing, potentially longer."
                    ),
                ),
                (
                    "Settlement class eligibility",
                    "Validate the actual court-defined class",
                    3.0,
                    (
                        "Use the settlement order, claim deadline, class period, "
                        "allocation plan, and Federal Rule of Civil Procedure 23. "
                        "Check claimant identity, exclusions, releases, assignments, and "
                        "duplicate submissions. The collectible base is the eventual "
                        "allocated distribution, not purchase volume or the settlement "
                        "fund. Budget $600 per paid account. Ordinary administrative "
                        "claim filing generally requires no customs surety bond; inspect "
                        "the actual order for separate security terms. Model 6–24 months "
                        "or longer, especially when appeals delay distribution."
                    ),
                ),
                (
                    "Authority and cash capacity",
                    "Proceed only with supported execution",
                    4.0,
                    (
                        "Verify broker or trade-counsel authority and valid Customs "
                        "Powers of Attorney for formal CBP filings, Part 190 records "
                        "for drawback, and court-required third-party filer disclosures "
                        "for settlements explaining direct filing at zero cost. Confirm "
                        "surety capacity before requesting accelerated payment. If collateral "
                        "exceeds available capital, use the standard-payment route or "
                        "defer the account; never fund operations from client principal."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod-architecture",
            "org_architecture",
            "Four Core People; Six at Scaled Capacity",
            "Base pod: 1 FT + 3 C. Scaled pod: 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT means full-time operator; C means contracted specialist. The "
                "first four seats form the Conservative and Base pod. The final "
                "two seats are added only for the Scaled scenario. Counsel must "
                "possess the competence required by the accepted case mix; narrow "
                "the service scope if the retained professional cannot cover it. "
                "Software and licensed data subscriptions are tools, not additional seats."
            ),
            (
                "Conservative revenue and profit are $110,000 and $35,200; Base "
                "figures are $515,000 and $231,750; Scaled figures are $920,000 "
                "and $533,600 with six people."
            ),
            [
                (
                    "Owner and recovery lead",
                    "Core seat 1; full-time operator",
                    1.0,
                    (
                        "Own client acquisition, contract economics, lane assignment, "
                        "cash forecasting, fee reconciliation, and account-level exception "
                        "decisions. Maintain separation between operator consideration "
                        "and funds belonging to the claimant."
                    ),
                ),
                (
                    "Licensed customs broker",
                    "Core seat 2; contracted professional",
                    1.0,
                    (
                        "Execute authorized customs business under 19 CFR Part 111. "
                        "Validate drawback routes, PSC availability, protest submissions, "
                        "POA scope, and bond arrangements while preserving filing "
                        "acknowledgments and supporting records."
                    ),
                ),
                (
                    "Evidence reconciliation analyst",
                    "Core seat 3; contracted specialist",
                    1.0,
                    (
                        "Match ACE entry lines to source invoices, inventory events, "
                        "and export bills of lading. Assemble settlement purchase "
                        "evidence, track reconciliation exceptions, and maintain the "
                        "duplicate-claim ledger across all three lanes."
                    ),
                ),
                (
                    "Trade and settlement counsel",
                    "Core seat 4; contracted professional",
                    1.0,
                    (
                        "Resolve complex statutory eligibility, protest grounds, "
                        "settlement-class interpretation, and filer-disclosure requirements. "
                        "Escalate disputes beyond the contracted scope rather than "
                        "letting administrative staff make unsupported legal determinations."
                    ),
                ),
                (
                    "Operations and collections lead",
                    "Scaled seat 5; second full-time operator",
                    1.0,
                    (
                        "Take over deadline monitoring, evidence-request scheduling, "
                        "status reconciliation, invoice collections, and operating "
                        "capacity planning. Add this seat against demonstrated "
                        "workload and collected fee capacity."
                    ),
                ),
                (
                    "Settlement ledger specialist",
                    "Scaled seat 6; fourth contractor",
                    1.0,
                    (
                        "Reconcile high-volume accounts-payable and processor exports, "
                        "normalize class-period purchases, resolve entity mapping, "
                        "and package administrator responses without substituting "
                        "purchase totals for distributable recovery estimates."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate $8,000–$35,000 Without Buying Claim Principal",
            "Four buckets; illustrative Base launch allocation totals $20,000.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $20,000 Base launch plan. Each bucket "
                "also states a lean and expanded allocation; lean allocations sum "
                "to $8,000 and expanded allocations sum to $35,000. These are startup "
                "capital allocations, not annual revenue scenarios or additional "
                "waterfall expenses. Reconcile actual spending to the expense ledger "
                "to avoid counting the same cost twice. Substantial surety collateral "
                "is outside these budgets; choose standard payment if accelerated "
                "payment cannot fit verified capital capacity."
            ),
            (
                "Lean: $1,000 + $2,000 + $3,000 + $2,000 = $8,000. "
                "Base launch: $20,000. Expanded: $4,000 + $9,000 + $14,000 "
                "+ $8,000 = $35,000."
            ),
            [
                (
                    "Entity and risk setup",
                    "$2,500 Base; $1,000 lean; $4,000 expanded",
                    2500.0,
                    (
                        "Fund entity setup, contract preparation, insurance deposits, "
                        "and authority documentation. Keep client recovery agreements "
                        "separate from broker Powers of Attorney and settlement "
                        "administrator authorization forms."
                    ),
                ),
                (
                    "Secure evidence tooling",
                    "$5,000 Base; $2,000 lean; $9,000 expanded",
                    5000.0,
                    (
                        "Fund initial manifest intelligence, encrypted storage, "
                        "reconciliation scripts, access controls, and audit logging. "
                        "Purchase only the data coverage needed for the first "
                        "authorized cohort instead of broad speculative datasets."
                    ),
                ),
                (
                    "Specialist launch capacity",
                    "$8,000 Base; $3,000 lean; $14,000 expanded",
                    8000.0,
                    (
                        "Reserve broker, analyst, and counsel capacity for initial "
                        "eligibility work and sample packets. Obtain written scopes "
                        "and fee schedules before accepting labor-intensive cases "
                        "with uncertain records or fragile deadlines."
                    ),
                ),
                (
                    "Working-capital reserve",
                    "$4,500 Base; $2,000 lean; $8,000 expanded",
                    4500.0,
                    (
                        "Hold cash for evidence retrieval, recurring overhead, and "
                        "collection delays. At $1,500 monthly spend, the Base reserve "
                        "covers three months; at $9,500, less than one month. "
                        "Throttle intake when expected payment timing exceeds runway."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-roadmap",
            "timeline_roadmap",
            "Thirty Days to a Controlled Recovery Desk",
            "Build evidence and filing readiness before forecasting near-term cash.",
            12,
            "operating_framework",
            (
                "Four weekly milestones cover Days 1–7, 8–14, 15–21, and 22–30. "
                "The canonical first-deal planning range is 1–3 months; a signed "
                "engagement is distinct from a paid agency refund or settlement "
                "distribution. The first month targets authorized evidence, tested "
                "reconciliation, and complete packets, not collection of the annual "
                "Base revenue target."
            ),
            (
                "Launch with a small, traceable cohort and preserve the right to "
                "decline defective evidence before spending scarce specialist capacity."
            ),
            [
                (
                    "Days 1–7",
                    "Define lanes and appoint the core pod",
                    7.0,
                    (
                        "Contract the broker, analyst, and counsel; establish "
                        "25%–35% fee terms; configure separate recovery and revenue "
                        "ledgers. Build statutory deadline fields, claimant identity "
                        "checks, and court-specific disclosure templates. Allocate "
                        "startup capital without assuming accelerated-payment access."
                    ),
                ),
                (
                    "Days 8–14",
                    "Acquire authorized sample evidence",
                    14.0,
                    (
                        "Obtain source records from three pilot accounts, ideally "
                        "one per lane. Reconcile a sample entry-to-export chain, "
                        "a correction or protest candidate, and an existing settlement "
                        "purchase ledger. Record actual evidence gaps and retrieval costs."
                    ),
                ),
                (
                    "Days 15–21",
                    "Test eligibility and packet integrity",
                    21.0,
                    (
                        "Have the filing professional verify customs eligibility "
                        "and clocks; have counsel verify settlement class and "
                        "filer terms. Test duplicate detection, duty-component exclusions, "
                        "export trace completeness, and fee calculations against "
                        "source documents before valuing the pilot pipeline."
                    ),
                ),
                (
                    "Days 22–30",
                    "Submit complete pilots and set cadence",
                    30.0,
                    (
                        "Submit only complete, authorized packets through the "
                        "appropriate channel and capture acknowledgments. Set weekly "
                        "exception triage, monthly cash forecasts, and account-level "
                        "cost tracking. Carry pending claims as pipeline records, "
                        "not realized recovery or earned operator fees."
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
