from __future__ import annotations

VOLUME_017_SUBTITLE = (
    "The Complete Playbook for Domain Investing: "
    "$20,000–$300,000 USD in Annual Gross Sales, "
    "a 1 FT + 1 C Core Pod, and a Four-Person Scaling Plan"
)

VOLUME_017_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Disciplined Domain Inventory Desk",
        "subtitle": (
            "Price brandable and exact-match inventory around acquisition basis, "
            "renewal exposure, and collected sale proceeds."
        ),
        "audience": (
            "A full-time owner and contract researcher operating a "
            "$8,000–$60,000 startup portfolio with patient capital."
        ),
        "research_basis": (
            "15 U.S.C. 1125(d) makes bad-faith intent to profit from protected "
            "marks central to cybersquatting exposure. Build mark screening, "
            "documented acquisition rationale, and renewal discipline into "
            "inventory selection rather than treating every available name "
            "as a saleable asset."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1125",
            "https://www.law.cornell.edu/uscode/text/15/1114",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Expired-Domain Acquisition Lab",
        "subtitle": (
            "Separate transferable domain value from historical traffic claims "
            "before bidding in drop-catch auctions."
        ),
        "audience": (
            "Specialist buyers who can inspect archived use, ownership history, "
            "link quality, auction terms, and transfer restrictions."
        ),
        "research_basis": (
            "15 U.S.C. 1125 addresses false designations and cybersquatting; "
            "15 U.S.C. 45 prohibits unfair or deceptive acts or practices. "
            "These sources support documented rights review and substantiation "
            "of seller claims, not an assumption that expired links or rankings "
            "will survive a transfer."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/1125",
            "https://www.law.cornell.edu/uscode/text/15/45",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Buyer-Matched Domain Upgrade Desk",
        "subtitle": (
            "Sell clean domain upgrades through relevant outreach, verified "
            "escrow instructions, and documented registrar handoffs."
        ),
        "audience": (
            "Owner-led operators combining inbound inquiry routing with "
            "carefully researched business-to-business upgrade offers."
        ),
        "research_basis": (
            "15 U.S.C. 7704 supplies concrete commercial-email requirements, "
            "including accurate headers, nondeceptive subjects, a postal "
            "address, and opt-out handling. 15 U.S.C. 1125(d) supports "
            "screening acquisition intent before targeting a prospective buyer."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/15/7704",
            "https://www.law.cornell.edu/uscode/text/15/1125",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_017_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-domain-inventory-to-cash",
            "process_flow",
            "Operate the Domain Inventory-to-Cash Loop",
            "Five controlled handoffs from sourcing to renewal or exit.",
            1,
            "operating_framework",
            (
                "The core pod is one full-time owner plus one contractor. "
                "First-deal timing is 2–9 months; a completed sourcing cycle "
                "does not establish buyer demand or immediate liquidity."
            ),
            (
                "Recognized operator revenue is gross domain sale proceeds. "
                "Escrow balances awaiting release and unsold asking prices "
                "are not completed-sale revenue."
            ),
            [
                (
                    "Source",
                    "Build a comparable-backed candidate queue",
                    1.0,
                    (
                        "Monitor NameBio comparables, expired-name lists, and "
                        "drop-catch auctions; record extension, sale date, "
                        "venue, buyer use case, and maximum bid."
                    ),
                ),
                (
                    "Screen",
                    "Document rights and historical-use checks",
                    2.0,
                    (
                        "Use USPTO Trademark Search, ICANN Lookup, RDAP, and "
                        "Wayback Machine records; reject mark-targeting "
                        "theses and investigate conflicting historical use."
                    ),
                ),
                (
                    "Acquire",
                    "Cap bids against total carrying exposure",
                    3.0,
                    (
                        "Include auction fees, transfer charges, premium "
                        "renewals, and expected holding periods in the bid "
                        "ceiling; record registrar access and ownership evidence."
                    ),
                ),
                (
                    "Market",
                    "Route inquiries into a priced negotiation",
                    4.0,
                    (
                        "Publish consistent marketplace and landing-page "
                        "prices; route inquiries to one owner and record "
                        "buyer identity, offer history, and net settlement math."
                    ),
                ),
                (
                    "Settle and recycle",
                    "Verify payment, transfer, and renewal decisions",
                    5.0,
                    (
                        "Verify escrow instructions independently, follow "
                        "registrar transfer procedures, reconcile released "
                        "proceeds, and reassess unsold names before renewal."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-domain-cohort-funnel",
            "funnel",
            "Track Domains Through One Nested Annual Cohort",
            "Count unique domains, not messages, leads, or auction impressions.",
            6,
            "illustrative_model",
            (
                "Illustrative annual cohort: 400 researched domains, 100 "
                "screen-cleared domains, 40 owned and listed domains, 20 with "
                "qualified inquiries, and eight completed sales. Each stage "
                "is a subset of the preceding stage. Existing holdings may "
                "enter the researched cohort; listing is not necessarily "
                "a current-year acquisition."
            ),
            (
                "Eight sales at an assumed $20,000 average produce the "
                "$160,000 Base-Case gross revenue. The implied 20% annual "
                "sell-through of 40 listed domains is a demanding modeling "
                "assumption, not a market benchmark."
            ),
            [
                (
                    "Researched domains",
                    "400 unique domains; complete cohort",
                    400.0,
                    (
                        "Deduplicate by domain and retain a dated record "
                        "of comparable sales, intended use, carrying cost, "
                        "and seller or auction provenance."
                    ),
                ),
                (
                    "Screen-cleared domains",
                    "100 domains; 25% of researched cohort",
                    100.0,
                    (
                        "Retain only domains passing documented rights, "
                        "historical-use, pricing, and transferability checks; "
                        "screen clearance does not authorize an unlimited bid."
                    ),
                ),
                (
                    "Owned and listed domains",
                    "40 domains; 40% of cleared subset",
                    40.0,
                    (
                        "Confirm control of every listed name, synchronize "
                        "prices across venues, and remove stale listings "
                        "immediately after a sale or ownership change."
                    ),
                ),
                (
                    "Domains with qualified inquiries",
                    "20 domains; 50% of listed subset",
                    20.0,
                    (
                        "Count each domain once after a buyer demonstrates "
                        "a credible use case and willingness to discuss "
                        "price; exclude automated spam and duplicate contacts."
                    ),
                ),
                (
                    "Completed domain sales",
                    "8 domains; 40% of inquiry subset",
                    8.0,
                    (
                        "Count only completed transactions; eight multiplied "
                        "by $20,000 equals $160,000 gross proceeds, with "
                        "acquisition and operating costs deducted separately."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "Reconcile $160,000 Gross Sales to $44,000 Owner Net",
            "Six bars establish the Base-Case 27.5% annual net margin.",
            3,
            "illustrative_model",
            (
                "The canonical Base Case fixes gross revenue at $160,000 "
                "and annual owner net profit at $44,000. The four expense "
                "buckets below are an illustrative allocation of the "
                "required $116,000 total cost, not additional scorecard facts. "
                "Intermediate bars are signed deductions; the final bar "
                "is an absolute total."
            ),
            (
                "$160,000 - $60,000 - $12,000 - $24,000 - $20,000 = "
                "$44,000; $44,000 / $160,000 = 27.5%. Conservative: "
                "$20,000 at 15% yields $3,000 with 1 FT + 1 C. "
                "Scaled: $300,000 at 40% yields $120,000 with 2 FT + 2 C."
            ),
            [
                (
                    "Gross domain sale proceeds",
                    "$160,000 annual operator revenue",
                    160000.0,
                    (
                        "Start with completed domain sales before selling "
                        "fees; do not substitute portfolio asking prices, "
                        "third-party merchant volume, or escrow deposits."
                    ),
                ),
                (
                    "Sold-domain acquisition basis",
                    "-$60,000 allocated purchase costs",
                    -60000.0,
                    (
                        "Assign purchase prices and acquisition fees to "
                        "the domains sold; unsold inventory purchases "
                        "remain a separate cash-use and inventory schedule."
                    ),
                ),
                (
                    "Portfolio renewals",
                    "-$12,000 annual carrying expense",
                    -12000.0,
                    (
                        "Include current-period renewal charges across "
                        "retained and sold inventory; remove any amounts "
                        "already included in acquisition basis."
                    ),
                ),
                (
                    "Selling and settlement costs",
                    "-$24,000 combined transaction expense",
                    -24000.0,
                    (
                        "Assume a blended 15% of gross proceeds covering "
                        "marketplace commissions and settlement charges; "
                        "replace this model rate with actual venue invoices."
                    ),
                ),
                (
                    "Other operating expense",
                    "-$20,000 annual operating budget",
                    -20000.0,
                    (
                        "Budget contractor support, research tools, outreach, "
                        "and administration at approximately $1,667 monthly; "
                        "exclude renewals and transaction fees counted above."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$44,000 retained operating result",
                    44000.0,
                    (
                        "This absolute endpoint equals 27.5% of gross "
                        "revenue; do not add it as another movement or "
                        "describe gross sales as the owner's earnings."
                    ),
                ),
            ],
        ),
        (
            "diag-04-domain-route-contribution-yields",
            "horizontal_bars",
            "Compare Direct Contribution Across Domain Sale Routes",
            "Five independent $10,000 sale examples; bar values are percentages.",
            2,
            "illustrative_model",
            (
                "All examples are hypothetical completed sales, not observed "
                "market yields. Direct contribution equals sale proceeds "
                "less acquisition, renewal, selling, and stated deal-specific "
                "costs. Shared overhead, unsold inventory, and holding time "
                "are excluded, so these percentages are not annual net margins."
            ),
            (
                "Compare routes only after equalizing sale price and cost "
                "definitions. These independent examples do not replace "
                "the canonical 15%, 27.5%, and 40% annual net margins."
            ),
            [
                (
                    "Brandable via marketplace",
                    "54% direct contribution; $5,400 retained",
                    54.0,
                    (
                        "$10,000 proceeds less $3,000 acquisition, $1,500 "
                        "selling costs, and $100 renewals leaves $5,400; "
                        "invented-word appeal still requires mark screening."
                    ),
                ),
                (
                    "Exact-match via marketplace",
                    "44% direct contribution; $4,400 retained",
                    44.0,
                    (
                        "$10,000 proceeds less $4,000 acquisition, $1,500 "
                        "selling costs, and $100 renewals leaves $4,400; "
                        "descriptive wording does not eliminate rights conflicts."
                    ),
                ),
                (
                    "Expired-authority via marketplace",
                    "30% direct contribution; $3,000 retained",
                    30.0,
                    (
                        "$10,000 proceeds less $5,000 acquisition, $1,500 "
                        "selling costs, $100 renewals, and $400 historical-use "
                        "research leaves $3,000; rankings can disappear."
                    ),
                ),
                (
                    "Drop-catch resale via marketplace",
                    "37% direct contribution; $3,700 retained",
                    37.0,
                    (
                        "$10,000 proceeds less $4,500 acquisition including "
                        "auction fees, $1,500 selling costs, $100 renewals, "
                        "and $200 diligence leaves $3,700."
                    ),
                ),
                (
                    "Outbound upgrade via direct escrow",
                    "55% direct contribution; $5,500 retained",
                    55.0,
                    (
                        "$10,000 proceeds less $3,500 acquisition, $300 "
                        "assumed settlement costs, $100 renewals, and $600 "
                        "outreach leaves $5,500; verify actual escrow pricing."
                    ),
                ),
            ],
        ),
        (
            "diag-05-domain-preflight-risk-tree",
            "decision_tree",
            "Resolve Four Pre-Flight Rights and Execution Checks",
            "Each checkpoint defines a proceed path and a stop-or-rework path.",
            5,
            "operating_framework",
            (
                "Apply rights checks before bidding and repeat relevant "
                "checks before marketing and transfer. UDRP is a contractual "
                "domain dispute policy, distinct from statutory ACPA claims; "
                "registration availability does not establish lawful use."
            ),
            (
                "Preserve dated evidence for acquisition intent, prior use, "
                "ownership, and outreach. Automated screening flags cases "
                "for review; it cannot establish the absence of disputes."
            ),
            [
                (
                    "Trademark and ACPA exposure",
                    "Document clean rationale or reject acquisition",
                    1.0,
                    (
                        "Review 15 U.S.C. 1114 and 1125, including 1125(d). "
                        "Proceed with documented independent use rationale; "
                        "reject a thesis built on bad-faith profit from "
                        "another party's protected mark."
                    ),
                ),
                (
                    "Applicable domain dispute policy",
                    "Check legitimate interests and adverse evidence",
                    2.0,
                    (
                        "For UDRP-covered names, examine confusing similarity, "
                        "rights or legitimate interests, and bad-faith "
                        "registration and use under paragraph 4(a). "
                        "Proceed after review; hold unresolved adverse facts."
                    ),
                ),
                (
                    "Control, transfer, and historical claims",
                    "Verify deliverability or suspend the listing",
                    3.0,
                    (
                        "Check registrar control, applicable transfer locks, "
                        "expiration, and dispute status. Under 15 U.S.C. 45, "
                        "substantiate traffic and authority claims; proceed "
                        "with evidence or remove unsupported claims."
                    ),
                ),
                (
                    "Commercial-email execution",
                    "Send compliant outreach or repair the campaign",
                    4.0,
                    (
                        "Apply 15 U.S.C. 7704: accurate headers, nondeceptive "
                        "subjects, required advertising identification, valid "
                        "postal address, and working opt-out. Honor opt-outs "
                        "within ten business days; suppress recipients before "
                        "further campaigns."
                    ),
                ),
            ],
        ),
        (
            "diag-06-domain-investing-pod-seats",
            "org_architecture",
            "Keep the Core Pod Small and Add Two Seats Deliberately",
            "Two core people; four people only in the scaled scenario.",
            11,
            "operating_framework",
            (
                "Conservative and Base use one full-time owner plus one "
                "contractor. Scaled uses two full-time people plus two "
                "contractors. Each stage represents one person; the last "
                "two seats are additions, not hidden Base-Case staffing."
            ),
            (
                "The owner retains bid limits, pricing authority, registrar "
                "control, and payout verification. Contractors receive only "
                "the access required for their assigned work."
            ),
            [
                (
                    "Core owner",
                    "1 FT; acquisition and commercial authority",
                    1.0,
                    (
                        "Set portfolio budgets and bid ceilings, review "
                        "rights risks, negotiate sales, control registrar "
                        "credentials, and reconcile escrow releases."
                    ),
                ),
                (
                    "Core research contractor",
                    "1 C; evidence and inventory operations",
                    1.0,
                    (
                        "Maintain comparable-sale records and renewal "
                        "calendars; use spreadsheets or SQLite for inventory "
                        "tracking without authority to transfer domains."
                    ),
                ),
                (
                    "Scaled sales operator",
                    "Add 1 FT; buyer pipeline ownership",
                    1.0,
                    (
                        "Handle inbound inquiry routing, qualification, "
                        "documented offers, and lawful outbound upgrades "
                        "within the owner's written pricing limits."
                    ),
                ),
                (
                    "Scaled operations contractor",
                    "Add 1 C; monitoring and reconciliation support",
                    1.0,
                    (
                        "Automate renewal reminders and comparable-sale "
                        "monitoring; audit listing consistency and transaction "
                        "records without unilateral payout or transfer access."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-30000-reference-allocation",
            "stacked_comparison",
            "Allocate a $30,000 Reference Startup Budget Across Four Buckets",
            "Compare $8,000 lean, $30,000 reference, and $60,000 expanded plans.",
            4,
            "illustrative_model",
            (
                "This illustrative $30,000 reference opening cash allocation "
                "sits within the $8,000–$60,000 USD startup capital range; "
                "it is not a required portfolio size or an annual expense "
                "forecast. Numeric values are reference-plan dollars. "
                "Each plan allocates 50% to acquisition inventory, 10% to "
                "research and transaction setup, 10% to renewal and transfer "
                "reserves, and 30% to operating runway. Lean and expanded "
                "amounts are shown in each bucket. Do not add these buckets "
                "to the annual waterfall as though all cash deployed were "
                "current expense."
            ),
            (
                "Lean: $4,000 + $800 + $800 + $2,400 = $8,000. "
                "Reference: $15,000 + $3,000 + $3,000 + $9,000 = $30,000. "
                "Expanded: $30,000 + $6,000 + $6,000 + $18,000 = $60,000. "
                "At $500–$5,000 monthly operating expense, the reference "
                "$9,000 operating reserve covers 1.8–18 months, excluding "
                "inventory purchases and separately reserved renewals "
                "and transfers."
            ),
            [
                (
                    "Acquisition inventory",
                    "Lean $4,000; reference $15,000; expanded $30,000; 50%",
                    15000.0,
                    (
                        "Allocate $4,000 of the $8,000 lean plan, $15,000 "
                        "of the $30,000 reference plan, or $30,000 of the "
                        "$60,000 expanded plan. Deploy gradually into "
                        "researched names and capped auction bids; retain "
                        "a per-domain basis ledger rather than marking "
                        "unsold inventory to asking prices."
                    ),
                ),
                (
                    "Research and transaction setup",
                    "Lean $800; reference $3,000; expanded $6,000; 10%",
                    3000.0,
                    (
                        "Allocate $800 of the $8,000 lean plan, $3,000 "
                        "of the $30,000 reference plan, or $6,000 of the "
                        "$60,000 expanded plan. Reserve for comparable-sale "
                        "tools, historical-use research, targeted rights "
                        "review, and initial transaction setup; release "
                        "funds against scoped work."
                    ),
                ),
                (
                    "Renewal and transfer reserve",
                    "Lean $800; reference $3,000; expanded $6,000; 10%",
                    3000.0,
                    (
                        "Allocate $800 of the $8,000 lean plan, $3,000 "
                        "of the $30,000 reference plan, or $6,000 of the "
                        "$60,000 expanded plan. Ring-fence cash against "
                        "registrar renewal schedules, premium-name charges, "
                        "and transfer costs; revise the reserve as holdings "
                        "and renewal dates change."
                    ),
                ),
                (
                    "Operating runway reserve",
                    "Lean $2,400; reference $9,000; expanded $18,000; 30%",
                    9000.0,
                    (
                        "Allocate $2,400 of the $8,000 lean plan, $9,000 "
                        "of the $30,000 reference plan, or $18,000 of the "
                        "$60,000 expanded plan. Support contractor work, "
                        "inquiry handling, and routine administration while "
                        "sales remain uneven. First-deal timing is 2–9 "
                        "months; the reference reserve covers nine months "
                        "only at monthly operating expense of $1,000 or less. "
                        "At $5,000 monthly, even the expanded operating "
                        "reserve covers only 3.6 months."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-domain-launch",
            "timeline_roadmap",
            "Build an Auditable Domain Desk in Thirty Days",
            "Four weekly milestones establish operations, not a promised sale.",
            12,
            "operating_framework",
            (
                "The launch sprint creates evidence, controls, and listings. "
                "Canonical first-deal timing remains 2–9 months. Buying "
                "inventory during the sprint is conditional on completed "
                "diligence and available carrying reserves."
            ),
            (
                "Exit day 30 with documented buy rules, controlled inventory, "
                "working inquiry routing, and a renewal calendar; report "
                "actual offers and settlements separately from asking prices."
            ),
            [
                (
                    "Days 1-7",
                    "Define the thesis and capital limits",
                    7.0,
                    (
                        "Choose one primary niche, document buyer use cases, "
                        "build a comparable-sales worksheet, allocate startup "
                        "cash, and set per-name and portfolio bid ceilings."
                    ),
                ),
                (
                    "Days 8-14",
                    "Complete diligence and secure operating accounts",
                    14.0,
                    (
                        "Record trademark and historical-use checks, review "
                        "auction terms, enable registrar multifactor "
                        "authentication, and create dated acquisition "
                        "decisions before placing authorized bids."
                    ),
                ),
                (
                    "Days 15-21",
                    "Publish controlled inventory and route inquiries",
                    21.0,
                    (
                        "List only owned names, synchronize venue prices, "
                        "test contact routing, maintain opt-out suppression, "
                        "and verify escrow and transfer procedures without "
                        "initiating a test ownership transfer."
                    ),
                ),
                (
                    "Days 22-30",
                    "Audit unit economics and the renewal runway",
                    30.0,
                    (
                        "Reconcile actual spending, inspect qualified "
                        "inquiries, calculate transaction-level contribution, "
                        "schedule 90-, 60-, and 30-day renewal reminders, "
                        "and define next-month retain-or-drop decisions."
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
