from __future__ import annotations

VOLUME_033_SUBTITLE = (
    "The Complete Playbook for Insurance Housing & Corporate Rental Arbitrage: "
    "$180,000–$1,400,000 USD in Annual Gross Billings with a "
    "1 FT + 3 C (4 People) Core Pod; Six Seats at Scale"
)

VOLUME_033_POSITIONING_ALTERNATIVES = [
    {
        "title": "The ALE Placement Desk",
        "subtitle": (
            "Turn authorized displaced-household requests into documented "
            "30-to-270-day housing placements with controlled lease exposure."
        ),
        "audience": (
            "Furnished-housing operators building referral relationships with "
            "insurance housing coordinators and claim representatives."
        ),
        "research_basis": (
            "Additional Living Expense coverage can support temporary housing "
            "after a covered loss, but policy limits, claim authorization, "
            "approved dates, and the actual contracting payer determine collection. "
            "Build a placement file around written spending authority rather "
            "than assuming every household expense is carrier-payable."
        ),
        "sources": [
            "https://content.naic.org/consumer/insurance-search.htm",
            "https://www.tdi.texas.gov/pubs/consumer/cb025.html",
            "https://www.law.cornell.edu/uscode/text/42/3604",
        ][1:],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Corporate Housing Spread",
        "subtitle": (
            "Control landlord permission, occupancy duration, and payer terms "
            "before committing to furnished master leases."
        ),
        "audience": (
            "Relocation coordinators and furnished-rental operators serving "
            "employers, project teams, and temporary assignments."
        ),
        "research_basis": (
            "Written landlord authority must match the proposed subletting "
            "and occupant structure. New York Real Property Law section 226-b "
            "illustrates jurisdiction-specific restrictions and procedures; "
            "Texas Tax Code section 156.101 illustrates why a permanent-resident "
            "tax exemption requires a specific occupancy analysis."
        ),
        "sources": [
            "https://www.nysenate.gov/legislation/laws/RPP/226-B",
            "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.156.htm#156.101",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Four-Person Relocation Pod",
        "subtitle": (
            "Run placement intake, property readiness, extensions, and "
            "collections through four accountable seats before scaling to six."
        ),
        "audience": (
            "Owner-operators replacing informal hosting routines with "
            "documented furnished-housing service delivery."
        ),
        "research_basis": (
            "Fair Housing Act requirements under 42 U.S.C. 3604 and "
            "24 CFR 100.202 inform consistent screening and disability-related "
            "housing practices where applicable. California Civil Code "
            "section 1941.1 supplies concrete dwelling-condition requirements "
            "for California properties, making readiness evidence an "
            "operating responsibility rather than a marketing claim."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/42/3604",
            "https://www.ecfr.gov/current/title-24/subtitle-B/chapter-I/"
            "subchapter-A/part-100/subpart-D/section-100.202",
            "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml"
            "?sectionNum=1941.1.&lawCode=CIV",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_033_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-placement-to-collection",
            "process_flow",
            "Control the Placement Before Buying the Lease",
            "Five linked records connect payer authority to collected housing cash.",
            1,
            "operating_framework",
            (
                "Operating framework for authorized ALE and corporate placements "
                "lasting approximately 30–270 days. A referral is neither "
                "payment authorization nor a signed occupancy agreement."
            ),
            (
                "The control point is a documented match among landlord "
                "permission, payer commitment, occupant terms, and lease exposure."
            ),
            [
                (
                    "Qualify the placement",
                    "Capture payer, dates, household, and authorized budget",
                    1.0,
                    (
                        "Record the contracting payer, claim or purchase-order "
                        "reference, household requirements, covered dates, and "
                        "spending limit in Airtable. Obtain written authority "
                        "before representing a carrier as the debtor."
                    ),
                ),
                (
                    "Secure lawful inventory",
                    "Obtain explicit landlord corporate-housing sublease permission",
                    2.0,
                    (
                        "Execute a property-specific written addendum covering "
                        "corporate occupants, subletting, furnished use, access, "
                        "maximum occupancy, and lease-break terms; reject verbal "
                        "permission and conflicting building restrictions."
                    ),
                ),
                (
                    "Price the exposure",
                    "Match approved stay economics against committed lease costs",
                    3.0,
                    (
                        "Quote rent, included utilities, utility caps, taxes, "
                        "deposits, and extension pricing separately. Stress-test "
                        "an early claim closeout against remaining landlord rent "
                        "and the next realistically obtainable placement."
                    ),
                ),
                (
                    "Deliver and extend",
                    "Document readiness, access, and written extension authority",
                    4.0,
                    (
                        "Capture condition photographs and a readiness checklist; "
                        "issue time-limited smart-lock access. Use authorized ALE "
                        "or CRS portal exports to reconcile dates, and request "
                        "extensions before current funding expires."
                    ),
                ),
                (
                    "Collect and reconcile",
                    "Match invoices, receipts, deposits, and landlord settlements",
                    5.0,
                    (
                        "Reconcile approved nights and documented utility-cap "
                        "charges in QuickBooks Online. Keep refundable deposits "
                        "separate from earnings; close access credentials and "
                        "record vacancy exposure when occupants depart."
                    ),
                ),
            ],
        ),
        (
            "diag-02-authorized-placement-funnel",
            "funnel",
            "A Placement Funnel with Traceable Denominators",
            "One 100-request cohort narrows to twelve executed, funded starts.",
            6,
            "illustrative_model",
            (
                "Illustrative acquisition cohort, not observed conversion data "
                "or an annual revenue forecast. Each stage is a subset of "
                "the preceding stage; use one request identifier throughout."
            ),
            (
                "Track loss reasons separately: missing authority, inventory "
                "mismatch, rejected terms, or an unfunded start."
            ),
            [
                (
                    "Received housing requests",
                    "100 requests captured within one intake cohort",
                    100.0,
                    (
                        "Deduplicate requests across adjusters, relocation desks, "
                        "and authorized housing portals. Count one household or "
                        "corporate assignment once, even when multiple properties "
                        "are proposed."
                    ),
                ),
                (
                    "Payer-qualified requests",
                    "60 requests retain documented authority and budget",
                    60.0,
                    (
                        "Sixty percent of intake passes payer identity, approved "
                        "dates, and budget checks. Reject unsupported promises "
                        "that a later claim decision will reimburse the stay."
                    ),
                ),
                (
                    "Inventory-matched requests",
                    "36 qualified requests match permitted ready inventory",
                    36.0,
                    (
                        "Sixty percent of qualified requests fit landlord "
                        "permission, location, household needs, readiness date, "
                        "and occupancy limits; apply consistent screening and "
                        "reasonable-accommodation procedures where required."
                    ),
                ),
                (
                    "Accepted commercial terms",
                    "18 matched requests accept documented pricing and terms",
                    18.0,
                    (
                        "Half of matched requests accept the complete quote, "
                        "including taxes, utility caps, cancellation exposure, "
                        "extension mechanics, and the responsible contracting payer."
                    ),
                ),
                (
                    "Executed funded starts",
                    "12 accepted requests become executed funded placements",
                    12.0,
                    (
                        "Two-thirds of accepted requests produce signed agreements "
                        "and the required deposit or documented credit terms. "
                        "Overall cohort conversion is twelve percent; placement "
                        "count alone does not establish annual billings."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-billings-to-owner-profit",
            "waterfall",
            "From $790,000 Gross Billings to $150,100 Owner Profit",
            "Six bars reconcile the 45% retained spread and 19.0% gross-basis margin.",
            3,
            "illustrative_model",
            (
                "Formula v2.0 canonical Base totals: $790,000 gross billings, "
                "$355,500 retained revenue, and $150,100 annual owner profit. "
                "The three operating-expense categories are illustrative "
                "allocations totaling $205,400, not supplied line-item forecasts. "
                "First and last bars are totals; intervening negative values "
                "are deductions. The 45% retained presentation follows the "
                "supplied ASC 606 scorecard convention; actual reporting requires "
                "the contract-specific principal-versus-agent assessment."
            ),
            (
                "$790,000 − $434,500 − $96,000 − $72,000 − $37,400 = "
                "$150,100. Owner profit is 19.0% of gross billings and "
                "42.22% of retained revenue."
            ),
            [
                (
                    "Gross housing billings",
                    "$790,000 annual customer housing billings before deductions",
                    790000.0,
                    (
                        "Opening total represents billed housing activity, "
                        "not underlying property value or retained operator "
                        "revenue. Refundable deposits and taxes collected solely "
                        "for remittance are outside this modeled total."
                    ),
                ),
                (
                    "Landlord rent and utilities",
                    "Subtract $434,500 for the 55% pass-through share",
                    -434500.0,
                    (
                        "Landlord master-lease rent and utility pass-throughs "
                        "consume fifty-five percent of billings, leaving "
                        "$355,500 retained revenue at the canonical forty-five "
                        "percent retained share."
                    ),
                ),
                (
                    "Delivery labor expense",
                    "Subtract $96,000 for modeled non-owner delivery labor",
                    -96000.0,
                    (
                        "Illustrative contractor and support-labor expense covers "
                        "placement coordination, field execution, and billing. "
                        "The owner's full-time seat receives the remaining "
                        "modeled owner profit rather than a second salary deduction."
                    ),
                ),
                (
                    "Property services and systems",
                    "Subtract $72,000 for services, insurance, and operating systems",
                    -72000.0,
                    (
                        "Illustrative expense covers turnover services, maintenance, "
                        "commercial insurance, access hardware support, and "
                        "software subscriptions. Exclude landlord rent and utility "
                        "amounts already deducted in the pass-through bar."
                    ),
                ),
                (
                    "Acquisition and administration",
                    "Subtract $37,400 for acquisition and administrative expenses",
                    -37400.0,
                    (
                        "Illustrative expense includes referral acquisition, "
                        "payment processing, bookkeeping, and general administration. "
                        "Total post-spread operating expense is $205,400 annually, "
                        "or $17,116.67 monthly before rounding."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$150,100 remains after all modeled operating deductions",
                    150100.0,
                    (
                        "Closing total is the canonical Base owner profit, "
                        "not another positive increment. Divide by $790,000 "
                        "for 19.0% gross-basis margin or by $355,500 "
                        "for 42.22% retained-basis margin."
                    ),
                ),
            ],
        ),
        (
            "diag-04-placement-rail-retained-yields",
            "horizontal_bars",
            "Compare Retained Spread Before Overhead",
            "Illustrative retained dollars per $100 of housing billings.",
            2,
            "illustrative_model",
            (
                "Independent underwriting examples, not measured market yields "
                "or a weighted portfolio forecast. Each bar subtracts only "
                "landlord rent and utility pass-throughs. The canonical "
                "portfolio retained share remains 45%; these bars are not "
                "owner net margins."
            ),
            (
                "A higher apparent spread can disappear through vacancy, "
                "slow collection, chargebacks, or an unpriced lease extension."
            ),
            [
                (
                    "Authorized ALE housing invoice",
                    "$48 retained per $100 under this illustration",
                    48.0,
                    (
                        "Illustrative $52 landlord-and-utility cost leaves $48 "
                        "before overhead. Require a named contracting payer and "
                        "written coverage dates; an adjuster referral alone "
                        "does not establish carrier payment liability."
                    ),
                ),
                (
                    "Employer purchase-order ACH",
                    "$45 retained per $100 under this illustration",
                    45.0,
                    (
                        "Illustrative $55 landlord-and-utility cost leaves $45 "
                        "before overhead. Match employer purchase-order limits, "
                        "invoice routing, and ACH settlement terms; fund the "
                        "gap between landlord due dates and customer receipts."
                    ),
                ),
                (
                    "Relocation intermediary invoice",
                    "$42 retained per $100 under this illustration",
                    42.0,
                    (
                        "Illustrative $58 landlord-and-utility cost leaves $42 "
                        "before overhead. Identify the intermediary's actual "
                        "payment obligation and separately expense any platform "
                        "or placement fee rather than hiding it in rent."
                    ),
                ),
                (
                    "Healthcare staffing housing",
                    "$46 retained per $100 under this illustration",
                    46.0,
                    (
                        "Illustrative $54 landlord-and-utility cost leaves $46 "
                        "before overhead. Align assignment cancellation terms "
                        "with landlord exposure and document who pays when "
                        "a worker changes facilities or leaves early."
                    ),
                ),
                (
                    "Direct corporate card booking",
                    "$44 retained per $100 under this illustration",
                    44.0,
                    (
                        "Illustrative $56 landlord-and-utility cost leaves $44 "
                        "before overhead. Deduct card-processing costs later "
                        "as operating expense and preserve signed occupancy "
                        "records for billing disputes and chargeback responses."
                    ),
                ),
            ],
        ),
        (
            "diag-05-property-and-placement-preflight",
            "decision_tree",
            "Four Checks Before a Binding Housing Commitment",
            "Every check must pass; a failed branch returns to remediation.",
            5,
            "operating_framework",
            (
                "Sequential decision framework, not a numerical risk score. "
                "Cited state provisions apply only in their jurisdictions. "
                "Assess the actual property, occupancy classification, "
                "contracting structure, and local rules."
            ),
            (
                "Written permission, tax treatment, dwelling readiness, and "
                "funded risk allocation must agree before committing rent."
            ),
            [
                (
                    "Landlord authority",
                    "Pass with explicit permission; otherwise stop lease commitment",
                    1.0,
                    (
                        "Obtain an executed corporate-housing sublease addendum "
                        "for every property. Check lease, building, and local "
                        "restrictions; New York Real Property Law section 226-b "
                        "has scope and procedure limits and is not blanket "
                        "permission for corporate subletting."
                    ),
                ),
                (
                    "Occupancy and tax treatment",
                    "Pass with documented classification; otherwise reprice or decline",
                    2.0,
                    (
                        "Review lodging classification and state plus local "
                        "occupancy taxes. Texas Tax Code section 156.101 "
                        "addresses the state permanent-resident exemption for "
                        "at least thirty consecutive days with uninterrupted "
                        "payment; do not export that rule nationwide."
                    ),
                ),
                (
                    "Habitability and fair housing",
                    "Pass with readiness evidence; otherwise repair before occupancy",
                    3.0,
                    (
                        "Inspect required heating, plumbing, electrical safety, "
                        "and dwelling conditions; California Civil Code "
                        "section 1941.1 supplies California requirements. Apply "
                        "42 U.S.C. 3604 and 24 CFR 100.202 where applicable "
                        "to screening and disability-related housing practices."
                    ),
                ),
                (
                    "Insurance and closeout exposure",
                    "Pass with funded exposure; otherwise renegotiate before signing",
                    4.0,
                    (
                        "Have the broker confirm furnished corporate-sublet "
                        "coverage, exclusions, and required liability limits. "
                        "Compare early claim closeout with landlord lease-break "
                        "costs, verify commercial insurance requirements, and "
                        "assign utility overruns and uninsured losses explicitly."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-seat-pod",
            "org_architecture",
            "Four Core Seats, Six at Scale",
            "The placement seat converts to full-time before two contractor additions.",
            11,
            "operating_framework",
            (
                "FT means full-time; C means contractor. Core pod: owner "
                "1 FT plus placement, property, and billing 3 C. Scaled pod: "
                "owner and placement 2 FT plus property, billing, inventory, "
                "and coverage 4 C. Each node represents one person when active; "
                "the last two nodes activate only in the scaled scenario. "
                "Worker classification follows actual working arrangements."
            ),
            (
                "Conservative: $180,000 gross, $81,000 retained, $21,600 profit "
                "at 12% gross margin and 26.67% retained margin. Base: "
                "$790,000 gross, $355,500 retained, $150,100 profit at 19.0% "
                "and 42.22%. Scaled: $1,400,000 gross, $630,000 retained, "
                "$364,000 profit at 26% and 57.78%."
            ),
            [
                (
                    "Owner and commercial lead",
                    "Core and scaled: one full-time accountable operator",
                    1.0,
                    (
                        "Own landlord commitments, payer credit terms, pricing "
                        "floors, cash exposure, and placement exceptions. Review "
                        "a weekly forward vacancy schedule and aged receivables "
                        "before accepting additional fixed lease obligations."
                    ),
                ),
                (
                    "Placement and extension lead",
                    "Core: one contractor; scaled: one full-time lead",
                    1.0,
                    (
                        "Own intake, approved budgets, inventory matching, and "
                        "extension reminders. Reconcile authorized ALE or CRS "
                        "portal records with Airtable; use supported integrations "
                        "or permitted exports rather than assuming API access."
                    ),
                ),
                (
                    "Property readiness lead",
                    "Core and scaled: one contracted property-readiness specialist",
                    1.0,
                    (
                        "Own inspections, turnover scheduling, access provisioning, "
                        "and vendor dispatch. Use smart locks plus disclosed "
                        "leak and noise-level telemetry; avoid recording private "
                        "conversations or using cameras inside occupied homes."
                    ),
                ),
                (
                    "Billing and collections lead",
                    "Core and scaled: one contracted billing specialist",
                    1.0,
                    (
                        "Own QuickBooks Online invoices, approved utility-cap "
                        "charges, payment matching, deposit liabilities, and "
                        "extension billing. Escalate overdue balances before "
                        "additional unfunded nights accumulate."
                    ),
                ),
                (
                    "Inventory onboarding specialist",
                    "Scaled addition: one contractor for incremental property onboarding",
                    1.0,
                    (
                        "Activate only in the six-person configuration. Assemble "
                        "landlord addenda, property specifications, tax treatment "
                        "records, readiness photographs, and insurance evidence "
                        "without shifting final lease authority from the owner."
                    ),
                ),
                (
                    "Service coverage specialist",
                    "Scaled addition: one contractor for extended service coverage",
                    1.0,
                    (
                        "Activate only in the six-person configuration. Provide "
                        "documented incident triage and extension follow-up "
                        "coverage; route emergencies to appropriate responders "
                        "and log handoffs to the property lead."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Cash Before Adding Fixed Rent",
            "Four buckets reconcile $12,000 lean, $30,000 planning, and $60,000 upper budgets.",
            4,
            "illustrative_model",
            (
                "Illustrative allocations within the canonical $12,000–$60,000 "
                "startup range. Numeric values encode the $30,000 planning "
                "stack; each stage also supplies lean and upper allocations. "
                "Weights remain 30%, 35%, 20%, and 15%. These are cash uses, "
                "not four immediate profit-and-loss expenses."
            ),
            (
                "Lean totals $12,000; planning totals $30,000; upper totals "
                "$60,000. Validate deposits and furnishing quotes before "
                "choosing a property count."
            ),
            [
                (
                    "Lease-entry cash",
                    "$3,600 lean; $9,000 planning; $18,000 upper allocation",
                    9000.0,
                    (
                        "Thirty percent funds landlord security deposits and "
                        "contractually required prepaid rent. Track refundable "
                        "deposits as assets and prepaid rent by service period; "
                        "neither is automatically an immediate operating expense."
                    ),
                ),
                (
                    "Furniture and property setup",
                    "$4,200 lean; $10,500 planning; $21,000 upper allocation",
                    10500.0,
                    (
                        "Thirty-five percent funds furniture, linens, kitchen "
                        "equipment, installation, and initial readiness work. "
                        "Obtain property-specific quotes; distinguish durable "
                        "assets from consumables and avoid assuming one budget "
                        "equips an arbitrary number of units."
                    ),
                ),
                (
                    "Vacancy and collection liquidity",
                    "$2,400 lean; $6,000 planning; $12,000 upper allocation",
                    6000.0,
                    (
                        "Twenty percent remains available for vacancy gaps, "
                        "payer delays, and early-closeout rent exposure. This "
                        "cash reserve is not a deductible expense merely "
                        "because it has been assigned to a budget bucket."
                    ),
                ),
                (
                    "Launch systems and risk setup",
                    "$1,800 lean; $4,500 planning; $9,000 upper allocation",
                    4500.0,
                    (
                        "Fifteen percent funds insurance inception payments, "
                        "contract preparation, access equipment, bookkeeping "
                        "setup, and workflow configuration. Separate recurring "
                        "charges from prepayments and installed assets."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Build a Placement-Ready Desk in Thirty Days",
            "Four weekly milestones establish evidence before expanding lease exposure.",
            12,
            "operating_framework",
            (
                "The sprint prepares operations; canonical time to first deal "
                "remains one to three months. Numeric values are milestone "
                "end days, not expected placements. Initial commitments must "
                "fit available capital and documented payer demand."
            ),
            (
                "End the month with permissioned inventory, tested billing, "
                "clear responsibility, and a controlled live-placement pipeline."
            ),
            [
                (
                    "Days 1–7",
                    "Choose one service area and document operating constraints",
                    7.0,
                    (
                        "Map landlord permission requirements, occupancy taxes, "
                        "habitability rules, and insurance needs. Build a "
                        "thirteen-week cash forecast using the $3,000–$18,000 "
                        "monthly operating-expense envelope and separately "
                        "model landlord rent and utility pass-through timing."
                    ),
                ),
                (
                    "Days 8–14",
                    "Qualify inventory and complete the property permission file",
                    14.0,
                    (
                        "Inspect candidate units, obtain furnishing quotes, "
                        "and negotiate explicit corporate-housing sublease "
                        "addenda. Obtain broker coverage confirmation and "
                        "calculate the cash loss from an early departure "
                        "followed by an unfilled lease period."
                    ),
                ),
                (
                    "Days 15–21",
                    "Test intake, extension tracking, access, and invoice reconciliation",
                    21.0,
                    (
                        "Configure Airtable records, authorized portal exports, "
                        "QuickBooks Online invoice mapping, and smart-lock "
                        "expiry. Run a synthetic placement through extension, "
                        "utility overage, partial payment, and early-closeout "
                        "cases without transmitting invented customer records."
                    ),
                ),
                (
                    "Days 22–30",
                    "Open qualified referrals and review every proposed commitment",
                    30.0,
                    (
                        "Contact relevant insurance housing coordinators and "
                        "corporate relocation desks with verified inventory "
                        "facts. Track the nested request cohort, evaluate "
                        "signed payer terms, and commit only exposure the "
                        "cash forecast can support if first collection slips."
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
