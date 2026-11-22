from __future__ import annotations

VOLUME_020_SUBTITLE = (
    "The Complete Playbook for Government Contract Brokering: "
    "$120,000–$1,000,000 USD in Annual Service Revenue, "
    "Built from a 2 FT + 3 C Five-Person Bid Desk"
)

VOLUME_020_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Federal Bid Desk",
        "subtitle": (
            "Build a recurring-fee procurement service around SAM.gov opportunity "
            "screening, solicitation matrices, and submission calendars."
        ),
        "audience": (
            "Procurement specialists serving capable small-business suppliers "
            "that need disciplined capture support without a full internal bid team."
        ),
        "research_basis": (
            "SAM.gov provides federal opportunity discovery; FAR 4.1102 establishes "
            "registration requirements subject to stated exceptions. FAR Subpart 3.4 "
            "and FAR 52.203-5 constrain contingent-fee arrangements. Position the "
            "desk around documented services rather than selling influence or "
            "assuming every award-linked fee is permissible."
        ),
        "sources": [
            "https://sam.gov/opportunities",
            "https://www.acquisition.gov/far/4.1102",
            "https://www.acquisition.gov/far/subpart-3.4",
            "https://www.acquisition.gov/far/52.203-5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Prime/Sub Teaming Desk",
        "subtitle": (
            "Turn supplier capability evidence into documented workshare, "
            "responsible teaming, and executable delivery plans."
        ),
        "audience": (
            "Experienced capture operators supporting established primes and "
            "specialist subcontractors with demonstrable delivery capacity."
        ),
        "research_basis": (
            "FAR Subpart 9.6 recognizes contractor team arrangements without "
            "eliminating prime responsibility. FAR 52.215-23 addresses excessive "
            "pass-through charges when applicable. Under 13 CFR 125.6, covered "
            "set-aside contracts impose category-specific subcontracting limits; "
            "a paper intermediary cannot substitute for required performance."
        ),
        "sources": [
            "https://www.acquisition.gov/far/subpart-9.6",
            "https://www.acquisition.gov/far/52.215-23",
            "https://www.ecfr.gov/current/title-13/section-125.6",
            "https://www.acquisition.gov/far/52.219-14",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Municipal Solicitation Desk",
        "subtitle": (
            "Run repeatable local-government bid operations with jurisdiction-specific "
            "submission controls and fixed-scope service fees."
        ),
        "audience": (
            "Regional bid operators helping suppliers pursue municipal purchasing "
            "opportunities while maintaining separate rulebooks for each jurisdiction."
        ),
        "research_basis": (
            "New York General Municipal Law sections 103 and 104-b illustrate "
            "the distinction between competitive-bidding requirements and local "
            "procurement policies for other purchases. These provisions are a "
            "jurisdiction-specific example, not a nationwide municipal rule. "
            "Municipal work involving federal awards also requires analysis of "
            "applicable 2 CFR Part 200 procurement provisions."
        ),
        "sources": [
            "https://www.nysenate.gov/legislation/laws/GMU/103",
            "https://www.nysenate.gov/legislation/laws/GMU/104-B",
            "https://www.ecfr.gov/current/title-2/section-200.318",
            "https://www.ecfr.gov/current/title-2/section-200.319",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_020_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-bid-desk-delivery-workflow",
            "process_flow",
            "Operate a Bid Desk, Not an Influence Channel",
            "Five evidence-backed handoffs from supplier intake to service billing.",
            1,
            "operating_framework",
            (
                "The operator sells procurement support to supplier clients. "
                "Government contract face value and subcontract principal remain "
                "outside recognized operator service revenue. Federal and municipal "
                "solicitations require separate rule matrices."
            ),
            (
                "Automate solicitation alerts, bid calendars, and checklist reminders; "
                "retain named human ownership of eligibility, pricing, and submission."
            ),
            [
                (
                    "Qualify the supplier",
                    "Document delivery capacity before pursuit",
                    1.0,
                    (
                        "Record client authority, past performance, delivery resources, "
                        "cash requirements, and conflicts. Check SAM.gov registration "
                        "and exclusions where relevant; verify claimed set-aside status "
                        "rather than treating a profile entry as sufficient evidence."
                    ),
                ),
                (
                    "Screen the opportunity",
                    "Match requirements against documented capability",
                    2.0,
                    (
                        "Use SAM.gov saved searches and municipal purchasing portals. "
                        "Extract mandatory qualifications, place of performance, "
                        "response deadlines, amendments, and evaluation factors into "
                        "a solicitation matrix with a named pursuit owner."
                    ),
                ),
                (
                    "Design the service",
                    "Separate fees from contract principal",
                    3.0,
                    (
                        "Define fixed-scope or retainer deliverables, client "
                        "responsibilities, and acceptance evidence. Review contingent-fee "
                        "restrictions and proposed teaming structures before signing; "
                        "a fixed fee does not cure prohibited conduct."
                    ),
                ),
                (
                    "Prepare and submit",
                    "Control versions, amendments, and receipts",
                    4.0,
                    (
                        "Maintain a dated bid calendar, assign technical sections, "
                        "validate required representations, and obtain client signoff. "
                        "Have the authorized submitter retain the final package, "
                        "amendment acknowledgments, and portal receipt."
                    ),
                ),
                (
                    "Deliver and collect",
                    "Invoice accepted procurement support services",
                    5.0,
                    (
                        "Record completed service milestones and invoice under the "
                        "client agreement. Track receivables aging and supplier "
                        "performance separately; recognize earned service fees without "
                        "booking the client's government award as operator revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-02-qualified-client-cohort",
            "funnel",
            "One Annual Client Cohort, Five Nested Stages",
            "200 screened suppliers become 20 signed and served clients.",
            6,
            "illustrative_model",
            (
                "Illustrative mature-year acquisition cohort, not measured conversion "
                "data. Every stage is a subset of the preceding stage, counted by "
                "unique supplier organization. All 20 final clients receive a full "
                "year of services averaging $28,000 each; partial-year starts would "
                "require a separate revenue schedule."
            ),
            (
                "200 to 80 to 40 to 25 to 20 produces 10% end-to-end conversion "
                "and $560,000 Base-Case recognized service revenue. Signed service "
                "clients are not government contract awards."
            ),
            [
                (
                    "Screened suppliers",
                    "200 distinct prospective client organizations",
                    200.0,
                    (
                        "Select suppliers with a defined public-sector offering, "
                        "reachable decision-makers, and a plausible delivery footprint. "
                        "Count each organization once, even when it pursues multiple "
                        "solicitations through different purchasing portals."
                    ),
                ),
                (
                    "Capability-qualified suppliers",
                    "80 organizations; 40% of initial cohort",
                    80.0,
                    (
                        "Confirm relevant capability evidence, resource availability, "
                        "and procurement fit. Remove organizations seeking access "
                        "payments, unsupported certifications, or opportunities they "
                        "cannot perform with the proposed team."
                    ),
                ),
                (
                    "Completed discovery engagements",
                    "40 organizations; 50% of qualified cohort",
                    40.0,
                    (
                        "Complete a structured discovery meeting with an authorized "
                        "buyer. Establish bid volume, service boundaries, payment "
                        "capacity, and which activities remain with the client's "
                        "technical and pricing owners."
                    ),
                ),
                (
                    "Issued service proposals",
                    "25 organizations; 62.5% of discovery cohort",
                    25.0,
                    (
                        "Issue scoped service proposals only after reviewing fee "
                        "structure, conflicts, and delivery effort. Include milestone "
                        "acceptance, invoice timing, and workload limits rather than "
                        "promising a government award."
                    ),
                ),
                (
                    "Signed and served clients",
                    "20 organizations; 80% of proposal cohort",
                    20.0,
                    (
                        "Deliver the modeled annual service mix: four clients at "
                        "each of $40,000, $30,000, $28,000, $24,000, and $18,000. "
                        "Total recognized fees equal $560,000 across 20 clients."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-service-revenue-waterfall",
            "waterfall",
            "Base Case: $560,000 Revenue to $126,000 Owner Net",
            "Four expense deductions reconcile exactly to a 22.5% net margin.",
            3,
            "illustrative_model",
            (
                "USD per mature operating year. The first bar is recognized service "
                "revenue, the next four bars are signed expense movements, and the "
                "sixth bar is the closing total, not another movement. Expense "
                "allocation is illustrative; revenue, net margin, and owner net "
                "match the canonical Base Case."
            ),
            (
                "$560,000 - $210,000 - $140,000 - $60,000 - $24,000 = $126,000; "
                "$126,000 / $560,000 = 22.5%. Costs total $434,000. No client "
                "award principal enters this bridge."
            ),
            [
                (
                    "Recognized service revenue",
                    "Opening total: $560,000 annual service fees",
                    560000.0,
                    (
                        "Recognize earned bid-desk and teaming-support fees under "
                        "client service agreements. Exclude government award face "
                        "value, client purchasing volume, and funds that merely "
                        "pass through for another party."
                    ),
                ),
                (
                    "Direct contract delivery",
                    "Expense movement: subtract $210,000 annually",
                    -210000.0,
                    (
                        "Allocate aggregate project-based compensation to the three "
                        "contractor seats covering capture analysis, proposal "
                        "production, and delivery verification. Remaining contribution "
                        "after this deduction is $350,000."
                    ),
                ),
                (
                    "Full-time personnel",
                    "Expense movement: subtract $140,000 annually",
                    -140000.0,
                    (
                        "Budget total loaded compensation for two full-time seats "
                        "at an illustrative $70,000 each. Verify actual hiring costs "
                        "before adopting this allocation. Remaining contribution "
                        "after personnel expense is $210,000."
                    ),
                ),
                (
                    "Operating infrastructure",
                    "Expense movement: subtract $60,000 annually",
                    -60000.0,
                    (
                        "Allocate $24,000 to software and secure document operations, "
                        "$18,000 to external legal and accounting services, and "
                        "$18,000 to insurance, selling, and administration. These "
                        "outside services do not create dedicated pod seats."
                    ),
                ),
                (
                    "Rework and credit losses",
                    "Expense movement: subtract $24,000 annually",
                    -24000.0,
                    (
                        "Model $16,000 of unrecovered delivery rework and $8,000 "
                        "of recognized client credit-loss expense. These are modeled "
                        "expenses, not an additional cash reserve or an assumption "
                        "that every late invoice becomes a loss."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "Closing total: $126,000 at 22.5%",
                    126000.0,
                    (
                        "Treat this bar as the closing total. Non-direct operating "
                        "expenses equal $224,000 annually, or approximately $18,666.67 "
                        "monthly, inside the stated $5,000–$25,000 monthly operating "
                        "range; direct contract delivery remains separately identified."
                    ),
                ),
            ],
        ),
        (
            "diag-04-service-package-revenue-yields",
            "horizontal_bars",
            "Five Service Niches, One Recognized-Revenue Basis",
            "Annual service fees per client; four clients in each niche.",
            2,
            "illustrative_model",
            (
                "Bar lengths show illustrative annual operator service fees per "
                "client in USD, not observed market prices, contract award values, "
                "or profit margins. Each client belongs to one primary service "
                "package; no client is counted in two bars."
            ),
            (
                "Four clients per package yield $160,000 + $120,000 + $112,000 "
                "+ $96,000 + $72,000 = $560,000. Package pricing must support "
                "documented work rather than payments for influence."
            ),
            [
                (
                    "Federal technical-services capture",
                    "$40,000 annual service fees per client",
                    40000.0,
                    (
                        "Four clients contribute $160,000 through capability mapping, "
                        "solicitation analysis, and recurring capture coordination. "
                        "Invoice contracted monthly services; keep the client's "
                        "technical solution and bid pricing under client ownership."
                    ),
                ),
                (
                    "Municipal facilities bid operations",
                    "$30,000 annual service fees per client",
                    30000.0,
                    (
                        "Four clients contribute $120,000 through local portal "
                        "monitoring, site-visit scheduling, document assembly, and "
                        "amendment control. Maintain separate jurisdiction rules "
                        "instead of applying federal clauses indiscriminately."
                    ),
                ),
                (
                    "Prime/sub teaming administration",
                    "$28,000 annual service fees per client",
                    28000.0,
                    (
                        "Four clients contribute $112,000 through capability "
                        "verification, workshare documentation, and teaming records. "
                        "Charge for actual support work; review FAR 9.6, applicable "
                        "pass-through clauses, and set-aside performance limits."
                    ),
                ),
                (
                    "Public-supply solicitation desk",
                    "$24,000 annual service fees per client",
                    24000.0,
                    (
                        "Four clients contribute $96,000 through specification "
                        "crosswalks, supplier confirmations, lead-time tracking, and "
                        "bid assembly. Identify applicable domestic-source and "
                        "nonmanufacturer requirements before pursuing supply awards."
                    ),
                ),
                (
                    "Post-submission administration",
                    "$18,000 annual service fees per client",
                    18000.0,
                    (
                        "Four clients contribute $72,000 through status tracking, "
                        "client-directed clarification coordination, document retention, "
                        "and service reporting. Keep authorized government "
                        "communications distinct from unsolicited access selling."
                    ),
                ),
            ],
        ),
        (
            "diag-05-statutory-structure-decision-tree",
            "decision_tree",
            "Four Checks Before Accepting the Engagement",
            "Each branch either proceeds with evidence or stops for redesign.",
            5,
            "operating_framework",
            (
                "The numeric values indicate check sequence, not risk scores. "
                "Apply federal statutes and clauses according to their scope and "
                "the solicitation. For municipal work, identify local ethics and "
                "purchasing rules separately; federal funding can add requirements."
            ),
            (
                "Run all four checks before promising services. A favorable result "
                "on fee structure does not resolve procurement integrity, kickbacks, "
                "or unlawful performance arrangements."
            ),
            [
                (
                    "Contingent-fee structure",
                    "Proceed with documented lawful compensation",
                    1.0,
                    (
                        "Does compensation depend on securing a government contract? "
                        "If yes, stop for analysis under 41 U.S.C. 3901, FAR "
                        "Subpart 3.4, and applicable FAR 52.203-5 terms, including "
                        "the narrowly defined bona fide employee or agency exception. "
                        "If no, document service deliverables and continue."
                    ),
                ),
                (
                    "Procurement integrity",
                    "Proceed only with authorized information",
                    2.0,
                    (
                        "Does the work involve protected bid, proposal, or source "
                        "selection information, or restricted employment contacts? "
                        "If yes, stop the affected activity and obtain a documented "
                        "resolution under 41 U.S.C. 2102–2104 and FAR 3.104. "
                        "Otherwise record information provenance and continue."
                    ),
                ),
                (
                    "Kickbacks and influence",
                    "Reject improper payments or preferential treatment",
                    3.0,
                    (
                        "Is anything of value being offered for improper favorable "
                        "treatment in a prime contract or related subcontract? "
                        "If yes, reject the arrangement and address applicable "
                        "reporting duties. Apply 41 U.S.C. 8702 and FAR Subpart "
                        "3.5; separately assess public-official bribery under "
                        "18 U.S.C. 201 where applicable."
                    ),
                ),
                (
                    "Performance and eligibility",
                    "Proceed only with executable lawful workshare",
                    4.0,
                    (
                        "Can the eligible contractor perform the required workshare "
                        "and substantiate intermediary value? If no, redesign or "
                        "decline. Evaluate 13 CFR 125.6, applicable FAR 52.219-14 "
                        "and 52.215-23 terms, and ostensible-subcontractor exposure "
                        "under 13 CFR 121.103(h). If yes, retain the calculation "
                        "and responsibility matrix."
                    ),
                ),
            ],
        ),
        (
            "diag-06-five-to-seven-person-pod",
            "org_architecture",
            "Five Core Seats; Two Seats Added at Scale",
            "Conservative and Base: 2 FT + 3 C. Scaled: 3 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT means full-time employee; C means contractor seat with variable "
                "engagement hours. Each stage represents one seat, not one full-time "
                "equivalent. Seats six and seven exist only in the Scaled "
                "Small-Team scenario; headcount alone does not establish capacity."
            ),
            (
                "Canonical annual outcomes: Conservative $120,000 revenue at 15% "
                "equals $18,000 owner net; Base $560,000 at 22.5% equals $126,000; "
                "Scaled $1,000,000 at 30% equals $300,000. Recognized service fees "
                "remain the revenue basis in every scenario."
            ),
            [
                (
                    "Managing operator",
                    "Core seat one: full-time accountable lead",
                    1.0,
                    (
                        "Own client selection, service pricing, conflict review, "
                        "cash forecasting, and engagement scope. Approve pursuit "
                        "capacity using actual hours and receivables rather than "
                        "the nominal value of prospective client awards."
                    ),
                ),
                (
                    "Bid operations manager",
                    "Core seat two: full-time workflow owner",
                    1.0,
                    (
                        "Maintain solicitation alerts, bid calendars, version "
                        "control, amendment tracking, and submission receipts. "
                        "Escalate missed client inputs early enough to withdraw "
                        "or revise a pursuit without a defective submission."
                    ),
                ),
                (
                    "Capture analyst",
                    "Core seat three: contracted research specialist",
                    1.0,
                    (
                        "Screen SAM.gov notices and municipal opportunities, map "
                        "requirements to supplier capabilities, and maintain "
                        "pursuit evidence. Distinguish public opportunity intelligence "
                        "from protected procurement information."
                    ),
                ),
                (
                    "Proposal specialist",
                    "Core seat four: contracted production specialist",
                    1.0,
                    (
                        "Assemble response matrices, edit client-provided technical "
                        "content, and check required attachments. Record unresolved "
                        "claims for client correction instead of inventing past "
                        "performance or unsupported qualifications."
                    ),
                ),
                (
                    "Supplier performance verifier",
                    "Core seat five: contracted delivery specialist",
                    1.0,
                    (
                        "Validate supplier commitments, lead times, workshare "
                        "evidence, and delivery dependencies. Escalate supplier "
                        "failure and substitution risk before the client commits "
                        "to an unsupported performance schedule."
                    ),
                ),
                (
                    "Client delivery lead",
                    "Scaled seat six: additional full-time employee",
                    1.0,
                    (
                        "Add in the Scaled scenario to manage service acceptance, "
                        "renewals, and cross-client workload. The resulting employee "
                        "count is three; preserve separation between client award "
                        "administration and operator service billing."
                    ),
                ),
                (
                    "Surge proposal specialist",
                    "Scaled seat seven: additional contracted specialist",
                    1.0,
                    (
                        "Add in the Scaled scenario for concurrent submission "
                        "peaks and independent package checks. The resulting "
                        "contractor count is four; schedule actual availability "
                        "rather than assuming every contractor works full time."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-reference-budget",
            "stacked_comparison",
            "Allocate a $55,000 Reference Startup Budget",
            "Four buckets across $20,000 lean, $55,000 reference, and $90,000 expanded plans.",
            4,
            "illustrative_model",
            (
                "Numeric bar values represent the $55,000 central/reference startup "
                "plan in USD, inside the canonical $20,000–$90,000 startup capital "
                "range. Each stage also specifies its $20,000 lean-plan and "
                "$90,000 expanded-plan allocation. These are funding alternatives, "
                "not the Conservative, Base, or Scaled annual earnings scenarios."
            ),
            (
                "Lean: $8,000 + $4,000 + $5,000 + $3,000 = $20,000. Reference: "
                "$22,000 + $11,000 + $14,000 + $8,000 = $55,000. Expanded: "
                "$36,000 + $18,000 + $23,000 + $13,000 = $90,000."
            ),
            [
                (
                    "Working-capital runway",
                    "Reference $22,000; lean $8,000; expanded $36,000",
                    22000.0,
                    (
                        "Hold cash for staged operating commitments and collection "
                        "timing. At $5,000 monthly operating expense, the lean, "
                        "reference, and expanded allocations cover 1.6, 4.4, and "
                        "7.2 months before receipts, respectively; at $25,000 they "
                        "cover 0.32, 0.88, and 1.44 months. Direct delivery costs "
                        "can require additional cash."
                    ),
                ),
                (
                    "Contracting and risk setup",
                    "Reference $11,000; lean $4,000; expanded $18,000",
                    11000.0,
                    (
                        "Fund scoped agreement review, insurance placement, entity "
                        "administration, and jurisdiction-specific operating procedures. "
                        "SAM.gov registration itself is free; any paid assistance "
                        "must be separately described rather than represented as "
                        "a government registration charge."
                    ),
                ),
                (
                    "Bid-desk systems and launch delivery",
                    "Reference $14,000; lean $5,000; expanded $23,000",
                    14000.0,
                    (
                        "Fund secure document storage, access controls, CRM setup, "
                        "calendar automation, and limited launch contractor work. "
                        "Use SAM.gov alerts, Microsoft 365, and documented checklists "
                        "before purchasing overlapping research subscriptions."
                    ),
                ),
                (
                    "Pipeline development",
                    "Reference $8,000; lean $3,000; expanded $13,000",
                    8000.0,
                    (
                        "Fund targeted supplier outreach, capability interviews, "
                        "industry meetings, and scoped proposal development. Model "
                        "the stated 3–12 months to first deal; startup cash alone "
                        "does not support every combination of that delay and "
                        "the $5,000–$25,000 monthly operating range."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-roadmap",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Bid Desk",
            "Build operating readiness without assuming an award in the first month.",
            12,
            "operating_framework",
            (
                "Numeric values identify milestone end days. The sprint establishes "
                "service scope, systems, and pursuit discipline; the canonical "
                "time to first deal remains 3–12 months. Client awards, signed "
                "engagements, recognized fees, and collected cash are separate events."
            ),
            (
                "Advance on completed evidence: a service charter, an opportunity "
                "matrix, a tested submission workflow, and a dated pursuit plan."
            ),
            [
                (
                    "Days 1-7",
                    "Define one service niche and fee structure",
                    7.0,
                    (
                        "Select one supplier segment and initial jurisdiction. "
                        "Draft deliverables, exclusions, pricing, and client "
                        "responsibilities; complete the four statutory checks. "
                        "Produce a service charter, conflict register, and startup "
                        "cash plan with explicit spending limits."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build alerts, calendars, and opportunity evidence",
                    14.0,
                    (
                        "Configure SAM.gov saved searches and relevant municipal "
                        "portal monitoring. Review ten actual notices, record "
                        "mandatory requirements and amendments, and assign calendar "
                        "owners. Produce a dated opportunity matrix with documented "
                        "reasons for pursuing or rejecting each notice."
                    ),
                ),
                (
                    "Days 15-21",
                    "Test supplier qualification and submission controls",
                    21.0,
                    (
                        "Conduct five capability interviews and document delivery "
                        "constraints. Run a mock submission using a public notice, "
                        "without transmitting a bid. Test attachment naming, "
                        "deadline time zones, client signoff, access recovery, "
                        "and receipt retention."
                    ),
                ),
                (
                    "Days 22-30",
                    "Launch measured outreach and cash review",
                    30.0,
                    (
                        "Issue service proposals only to qualified prospects "
                        "with reviewed structures. Publish a ninety-day pursuit "
                        "calendar and weekly receivables review. Record observed "
                        "cohort conversion separately from the illustrative funnel; "
                        "do not count outreach, bids, or client awards as earned fees."
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
        for identifier, kind, title, subtitle, chapter, tag, note, caption, stages in specs
    ]
