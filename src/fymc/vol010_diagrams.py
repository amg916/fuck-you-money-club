from __future__ import annotations

VOLUME_010_SUBTITLE = (
    "The Complete Playbook for Building an SEO Empire: "
    "$80,000–$900,000 USD Annually, Starting with a "
    "1 FT + 3 C (4 People) Publishing Pod"
)

VOLUME_010_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Search Portfolio Operating System",
        "subtitle": (
            "Build a multi-site publishing portfolio with repeatable technical "
            "audits, content refresh queues, and earned-revenue reporting."
        ),
        "audience": (
            "Publisher-operators starting with one full-time employee and three "
            "contractors who need site-level economics rather than traffic vanity metrics."
        ),
        "research_basis": (
            "Copyright ownership and endorsement disclosures create concrete "
            "requirements for repeatable publishing operations. Track image licenses, "
            "contributor rights, affiliate relationships, and disclosure placement "
            "alongside each content record. These sources support operating "
            "requirements, not the modeled revenue or audience demand."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/17/106",
            "https://www.law.cornell.edu/uscode/text/17/204",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-Led Authority Publisher",
        "subtitle": (
            "Pair topical authority and selective programmatic SEO with original "
            "evidence, attributable GEO citations, and transparent monetization."
        ),
        "audience": (
            "Editors and technical founders building useful reference libraries "
            "instead of interchangeable pages assembled around keyword permutations."
        ),
        "research_basis": (
            "17 U.S.C. 107 makes fair-use analysis fact-specific; it does not "
            "provide blanket permission to reproduce competing publications. "
            "15 U.S.C. 45 and 16 CFR 255.1 support truthful commercial claims "
            "and endorsements. Apply these requirements to comparison pages, "
            "sponsor copy, quotations, and expert contributions. GEO citation "
            "capture remains a measured distribution experiment."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/17/107",
            "https://www.law.cornell.edu/uscode/text/15/45",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.1",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Transfer-Ready Search Media Portfolio",
        "subtitle": (
            "Build auditable content rights, diversified publisher receipts, "
            "and transferable operating records before pursuing a media exit."
        ),
        "audience": (
            "Small-team portfolio owners preparing acquisition diligence while "
            "continuing to operate advertising, affiliate, and sponsorship programs."
        ),
        "research_basis": (
            "17 U.S.C. 204 establishes writing requirements for copyright "
            "ownership transfers, while 17 U.S.C. 201 addresses initial ownership "
            "and works made for hire. Maintain executed contributor agreements "
            "and distinguish owned material from licensed material. Advertising "
            "relationship disclosures remain necessary during ordinary operations; "
            "asset ownership alone does not establish transferability of platform "
            "accounts or commercial contracts."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/17/204",
            "https://www.law.cornell.edu/uscode/text/17/201",
            "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_010_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-search-portfolio-production-loop",
            "process_flow",
            "Turn Search Demand into Owned Publishing Assets",
            "Five operating stages connect useful pages to publisher revenue.",
            1,
            "operating_framework",
            (
                "The operating sequence covers multi-site search publishing, "
                "selective programmatic production, and GEO citation tracking. "
                "Stage numbers express sequence, not revenue forecasts. The "
                "canonical time to first deal is 3–12 months."
            ),
            (
                "Automate technical audits, refresh queues, and revenue reporting; "
                "retain human responsibility for evidence, rights, and editorial quality."
            ),
            [
                (
                    "Map demand",
                    "Stage 1: select defensible topic clusters",
                    1.0,
                    (
                        "Combine Google Search Console, Ahrefs, and direct SERP "
                        "inspection to map intent, competing formats, audience "
                        "needs, and plausible advertising or affiliate demand."
                    ),
                ),
                (
                    "Design assets",
                    "Stage 2: establish evidence and page architecture",
                    2.0,
                    (
                        "Specify original research, licensed media, internal links, "
                        "and differentiated page templates. Reject programmatic "
                        "variants that add no substantive user value."
                    ),
                ),
                (
                    "Publish and verify",
                    "Stage 3: release tested editorial units",
                    3.0,
                    (
                        "Use Screaming Frog and Search Console to inspect status "
                        "codes, canonicals, rendering, and indexability. Editors "
                        "verify claims, contributor rights, and commercial disclosures."
                    ),
                ),
                (
                    "Monetize earned attention",
                    "Stage 4: connect approved commercial relationships",
                    4.0,
                    (
                        "Record advertising earnings, approved affiliate commissions, "
                        "and delivered sponsorship revenue. Exclude referred merchant "
                        "sales, pending commissions, and undelivered sponsor commitments."
                    ),
                ),
                (
                    "Refresh and package",
                    "Stage 5: reinvest using auditable asset records",
                    5.0,
                    (
                        "Queue decaying pages in Airtable; reconcile revenue in "
                        "BigQuery and Looker Studio. Log sampled GEO citations "
                        "separately from referrals and maintain transfer-ready rights records."
                    ),
                ),
            ],
        ),
        (
            "diag-02-organic-to-payable-affiliate-cohort",
            "funnel",
            "Measure One Cohort through Payable Affiliate Outcomes",
            "100,000 eligible organic sessions narrow to 530 payable sessions.",
            6,
            "illustrative_model",
            (
                "Illustrative cohort, not observed performance or an annual "
                "projection. Every downstream count is a subset of the original "
                "100,000 sessions, counted once per stage. Use permitted attribution "
                "records and a stated 60-day reconciliation window. Assume exactly "
                "one $20 approved commission per payable session."
            ),
            (
                "The cohort earns $10,600 in affiliate revenue: 530 multiplied "
                "by $20. Merchant order value is excluded. Advertising and "
                "sponsorship earnings are outside this conversion funnel."
            ),
            [
                (
                    "Organic entry sessions",
                    "100,000 sessions establish the original cohort",
                    100000.0,
                    (
                        "Freeze eligible organic landing sessions for the cohort "
                        "period. Exclude internal traffic and bot traffic; document "
                        "measurement exclusions instead of treating them as conversions."
                    ),
                ),
                (
                    "Commercial-content readers",
                    "40,000 sessions; 40% of entry cohort",
                    40000.0,
                    (
                        "Count sessions reaching at least one relevant comparison "
                        "or product-selection page. Multiple page views within "
                        "the same session do not enlarge this stage."
                    ),
                ),
                (
                    "Affiliate outbound sessions",
                    "12,000 sessions; 30% of commercial readers",
                    12000.0,
                    (
                        "Count sessions with at least one disclosed affiliate "
                        "outbound event. Preserve campaign and content identifiers "
                        "without transmitting unnecessary personal information."
                    ),
                ),
                (
                    "Attributed purchase sessions",
                    "600 sessions; 5% of outbound sessions",
                    600.0,
                    (
                        "Match merchant-reported purchase events back to eligible "
                        "outbound sessions. Deduplicate purchases within each session "
                        "and retain pending status during returns review."
                    ),
                ),
                (
                    "Payable purchase sessions",
                    "530 sessions; 88.33% of purchase sessions",
                    530.0,
                    (
                        "Remove 70 sessions whose purchases were reversed or "
                        "disallowed. Final conversion is 0.53% of the original "
                        "cohort; reconcile $10,600 to approved commission statements."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-revenue-to-owner-net",
            "waterfall",
            "Reconcile $490,000 Gross to $159,250 Owner Net",
            "Four illustrative cost deductions produce the canonical 32.5% margin.",
            3,
            "illustrative_model",
            (
                "First and last bars are totals; the four intervening bars are "
                "negative deductions. Revenue and owner net are canonical; cost "
                "category allocations are illustrative. Annual costs total $330,750, "
                "or $27,562.50 monthly. The supplied $2,500–$14,000 monthly opex "
                "range cannot be an all-in ceiling for this Base case: implied "
                "annual costs exceed its $240,000 upper annual equivalent by "
                "$90,750. Resolve that scope difference before budgeting."
            ),
            (
                "$490,000 minus $156,000 minus $84,000 minus $42,000 minus "
                "$48,750 equals $159,250; $159,250 divided by $490,000 equals "
                "32.5%. Referred merchant sales never enter publisher gross revenue."
            ),
            [
                (
                    "Publisher gross revenue",
                    "$490,000 annual recognized operator revenue",
                    490000.0,
                    (
                        "Illustrative rail allocation is $218,000 advertising, "
                        "$212,000 approved affiliate commissions, and $60,000 "
                        "delivered sponsorship revenue; the three components reconcile."
                    ),
                ),
                (
                    "Full-time labor",
                    "Subtract $156,000 in modeled annual labor",
                    -156000.0,
                    (
                        "Allocate $156,000 to the single full-time seat in the "
                        "1 FT + 3 C core pod. Treat this as a modeled loaded "
                        "labor budget, not a salary survey finding or a separate "
                        "owner distribution."
                    ),
                ),
                (
                    "Contracted production",
                    "Subtract $84,000 in modeled contractor fees",
                    -84000.0,
                    (
                        "The core pod includes three fractional contractor seats, "
                        "not four. The unchanged $84,000 production envelope covers "
                        "their purchased capacity and any external vendor/trade "
                        "sub-crews charged to direct subcontractor/COGS pass-through. "
                        "External crews are not internal pod headcount; do not "
                        "add their costs again outside this deduction."
                    ),
                ),
                (
                    "Publishing infrastructure",
                    "Subtract $42,000 in modeled infrastructure costs",
                    -42000.0,
                    (
                        "Budget hosting, security maintenance, audit tools, analytics, "
                        "licensed datasets, and production software. Separate one-time "
                        "setup purchases from recurring costs to prevent duplication."
                    ),
                ),
                (
                    "Commercial and administrative costs",
                    "Subtract $48,750 in modeled remaining expenses",
                    -48750.0,
                    (
                        "Allocate $24,000 to commercial development, $12,000 to "
                        "bookkeeping and contract administration, and $12,750 to "
                        "insurance, banking, and other incurred operating expenses."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$159,250 retained after modeled operating costs",
                    159250.0,
                    (
                        "Preserve the canonical Base result. Conservative revenue "
                        "of $80,000 at 20% yields $16,000; Scaled revenue of "
                        "$900,000 at 45% yields $405,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-publisher-revenue-yields",
            "horizontal_bars",
            "Compare Sub-Niches on Publisher Revenue per 1,000 Sessions",
            "Equal traffic allocations produce a $49 blended publisher yield.",
            2,
            "illustrative_model",
            (
                "Illustrative yields, not market benchmarks. Allocate 2,000,000 "
                "annual sessions to each of five sub-niches: 10,000,000 sessions "
                "total. All yield components are USD of operator revenue per "
                "1,000 sessions, after affiliate reversals. Equal traffic weighting "
                "produces $49 blended yield and $490,000 annual Base revenue."
            ),
            (
                "Across the five equal-traffic segments, advertising contributes "
                "$218,000, affiliate commissions $212,000, and sponsorships $60,000. "
                "Yield comparisons require consistent session definitions and periods."
            ),
            [
                (
                    "Home workshop references",
                    "$30 earned per 1,000 eligible sessions",
                    30.0,
                    (
                        "$18 advertising plus $10 affiliate commissions plus $2 "
                        "sponsorship equals $30. At 2,000,000 annual sessions, "
                        "publisher revenue is $60,000; original photos reduce rights risk."
                    ),
                ),
                (
                    "Outdoor equipment guides",
                    "$40 earned per 1,000 eligible sessions",
                    40.0,
                    (
                        "$20 advertising plus $15 affiliate commissions plus $5 "
                        "sponsorship equals $40. At 2,000,000 annual sessions, "
                        "publisher revenue is $80,000; monitor seasonal traffic concentration."
                    ),
                ),
                (
                    "Creative software tutorials",
                    "$50 earned per 1,000 eligible sessions",
                    50.0,
                    (
                        "$22 advertising plus $23 affiliate commissions plus $5 "
                        "sponsorship equals $50. At 2,000,000 annual sessions, "
                        "publisher revenue is $100,000; refresh screenshots after interface changes."
                    ),
                ),
                (
                    "Small-business workflow guides",
                    "$60 earned per 1,000 eligible sessions",
                    60.0,
                    (
                        "$24 advertising plus $28 affiliate commissions plus $8 "
                        "sponsorship equals $60. At 2,000,000 annual sessions, "
                        "publisher revenue is $120,000; verify affiliate attribution windows."
                    ),
                ),
                (
                    "Specialist software comparisons",
                    "$65 earned per 1,000 eligible sessions",
                    65.0,
                    (
                        "$25 advertising plus $30 affiliate commissions plus $10 "
                        "sponsorship equals $65. At 2,000,000 annual sessions, "
                        "publisher revenue is $130,000; monitor partner concentration and reversals."
                    ),
                ),
            ],
        ),
        (
            "diag-05-publication-statutory-risk-checks",
            "decision_tree",
            "Resolve Rights, Claims, Privacy, and Distribution before Release",
            "Each affirmative answer advances; each negative answer triggers repair.",
            5,
            "operating_framework",
            (
                "Four sequential yes-or-no checks. A failed check sends the "
                "affected page, tracking feature, or outreach campaign to the "
                "named corrective action before reassessment. Statutory duties "
                "depend on the activity and applicable jurisdiction; search "
                "platform policies are separate contractual and distribution risks."
            ),
            (
                "Record evidence, the responsible owner, and the corrective "
                "action. Do not treat an automated SEO score as proof of "
                "copyright permission, truthful advertising, or lawful data handling."
            ),
            [
                (
                    "Rights established?",
                    "Yes: advance; no: replace or document permission",
                    1.0,
                    (
                        "Editor checks text, images, datasets, and contributor "
                        "agreements against 17 U.S.C. 106, 107, and 204. "
                        "Fair use requires specific analysis; attribution alone "
                        "does not grant reproduction rights."
                    ),
                ),
                (
                    "Commercial claims supportable?",
                    "Yes: advance; no: correct claims and disclosures",
                    2.0,
                    (
                        "Commercial lead checks evidence under 15 U.S.C. 45 "
                        "and material connections under 16 CFR 255.5. Place "
                        "clear disclosures with endorsements; do not bury paid "
                        "relationships in a distant policy page."
                    ),
                ),
                (
                    "Data handling scoped?",
                    "Yes: advance; no: disable affected collection",
                    3.0,
                    (
                        "Technical lead maps identifiers, recipients, retention, "
                        "and applicable rights. Assess Cal. Civ. Code "
                        "1798.100, 1798.120, and 1798.140 applicability; assess "
                        "COPPA under 15 U.S.C. 6502 and 16 CFR 312 "
                        "for child-directed services or relevant actual knowledge."
                    ),
                ),
                (
                    "Distribution method acceptable?",
                    "Yes: release; no: revise outreach or templates",
                    4.0,
                    (
                        "Operator checks commercial email against 15 U.S.C. "
                        "7704, including accurate headers and functioning opt-out. "
                        "Separately inspect Google spam policies for scaled "
                        "content abuse, link spam, and site reputation abuse."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-core-six-scaled-publishing-seats",
            "org_architecture",
            "Operate Four Core Seats; Add Two Only in the Scaled Model",
            "Conservative and Base: 1 FT + 3 C. Scaled: 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "Six entries depict four core seats and two Scaled-only expansion "
                "seats. A numeric value of 1 marks a person included in the core "
                "pod; 0 marks an expansion seat excluded from core headcount, "
                "not an unstaffed role once scaled. The core is 1 FT + 3 C "
                "(4 people); adding 1 FT + 1 C produces 2 FT + 4 C "
                "(6 people). Contractor seats are fractional service relationships, "
                "not full-time equivalents. External vendor/trade sub-crews are "
                "direct subcontractor/COGS pass-through, not internal pod seats. "
                "FYMC 2.0 score: 89/100; rank #07 of 29; "
                "tier: Elite Small-Team Cash Machine."
            ),
            (
                "The four-person core supports the canonical $80,000 Conservative "
                "and $490,000 Base scenarios; the six-person configuration belongs "
                "to the $900,000 Scaled scenario. Add the full-time partnerships "
                "lead and contracted production specialist only when funded workload "
                "justifies expansion. Resize paid capacity for Conservative revenue; "
                "scenario revenue alone does not establish workload capacity."
            ),
            [
                (
                    "Portfolio operator",
                    "Core seat 1: full-time portfolio and commercial ownership",
                    1.0,
                    (
                        "Own topic allocation, site-level profit reporting, partner "
                        "concentration, and capital deployment. Reconcile advertising, "
                        "payable affiliate commissions, and delivered sponsorships. "
                        "Maintain the rights register and transaction-ready records; "
                        "retain commercial responsibility until the expansion lead joins."
                    ),
                ),
                (
                    "Managing editor",
                    "Core seat 2: contracted editorial ownership",
                    1.0,
                    (
                        "Own evidence standards, contributor briefs, publishing "
                        "cadence, and refresh priorities within contracted capacity. "
                        "Review commercial claims, contributor rights, and disclosure "
                        "placement; prevent duplicative programmatic page expansion."
                    ),
                ),
                (
                    "Technical SEO engineer",
                    "Core seat 3: contracted technical delivery",
                    1.0,
                    (
                        "Maintain crawl monitoring, template tests, structured data, "
                        "analytics connectors, and deployment checks. Route indexing "
                        "regressions to a tracked repair queue instead of mass "
                        "resubmission; support the operator's revenue reporting."
                    ),
                ),
                (
                    "Subject and production specialist",
                    "Core seat 4: contracted research, writing, and CMS production",
                    1.0,
                    (
                        "Produce original explanations, testing records, and attributable "
                        "expert contributions. Supply source packets and documented "
                        "media rights, format accessible pages, and verify internal "
                        "links. Scope combined research and production work to "
                        "purchased capacity rather than assuming multiple full-time roles."
                    ),
                ),
                (
                    "Growth partnerships lead",
                    "Scaled-only seat 5: additional full-time commercial owner",
                    0.0,
                    (
                        "Add one FT seat in the Scaled configuration to diversify "
                        "sponsorships and manage partner renewals. Protect editorial "
                        "independence and document placement obligations before "
                        "recognizing sponsor revenue; this seat is outside the core pod."
                    ),
                ),
                (
                    "Production specialist",
                    "Scaled-only seat 6: additional contracted production capacity",
                    0.0,
                    (
                        "Add one C seat in the Scaled configuration for licensed "
                        "visuals, accessible CMS formatting, and publication checks. "
                        "Relieve the core subject specialist's production workload "
                        "only after measuring editorial review capacity and the "
                        "refresh backlog; this seat is outside the core pod."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-35000-reference-allocation",
            "stacked_comparison",
            "Allocate a $35,000 Reference Startup Plan across Four Buckets",
            "Lean $10,000, reference $35,000, and expanded $60,000 USD launch plans.",
            4,
            "illustrative_model",
            (
                "Numeric values depict the $35,000 central/reference startup "
                "budget within the canonical $10,000–$60,000 USD range. Each "
                "bucket also specifies lean and expanded allocations; all three "
                "plans use 40%, 30%, 20%, and 10% shares and sum exactly to "
                "$10,000, $35,000, and $60,000 respectively. These are illustrative "
                "cash allocations, not accounting capitalization instructions or "
                "additional annual costs. Expanded startup funding does not "
                "automatically activate the Scaled pod."
            ),
            (
                "Lean: $4,000 + $3,000 + $2,000 + $1,000 = $10,000. "
                "Reference: $14,000 + $10,500 + $7,000 + $3,500 = $35,000. "
                "Expanded: $24,000 + $18,000 + $12,000 + $6,000 = $60,000. "
                "Budget continuing funding separately for the canonical 3–12 months "
                "to first deal and $2,500–$14,000 USD monthly opex range; "
                "startup capital alone does not guarantee sufficient runway."
            ),
            [
                (
                    "Original content and evidence",
                    "$14,000 reference; $4,000 lean; $24,000 expanded; 40%",
                    14000.0,
                    (
                        "Allocate $4,000 of the $10,000 lean plan, $14,000 of "
                        "the $35,000 reference plan, or $24,000 of the $60,000 "
                        "expanded plan. Fund original testing, commissioned writing, "
                        "editing, and documented media licenses."
                    ),
                ),
                (
                    "Technical publishing foundation",
                    "$10,500 reference; $3,000 lean; $18,000 expanded; 30%",
                    10500.0,
                    (
                        "Allocate $3,000 of the $10,000 lean plan, $10,500 of "
                        "the $35,000 reference plan, or $18,000 of the $60,000 "
                        "expanded plan. Fund templates, hosting setup, backups, "
                        "access controls, and initial crawl remediation."
                    ),
                ),
                (
                    "Measurement and commercial setup",
                    "$7,000 reference; $2,000 lean; $12,000 expanded; 20%",
                    7000.0,
                    (
                        "Allocate $2,000 of the $10,000 lean plan, $7,000 of "
                        "the $35,000 reference plan, or $12,000 of the $60,000 "
                        "expanded plan. Fund attribution setup, reporting connectors, "
                        "partner materials, and contributor agreement preparation."
                    ),
                ),
                (
                    "Unspent working reserve",
                    "$3,500 reference; $1,000 lean; $6,000 expanded; 10%",
                    3500.0,
                    (
                        "Allocate $1,000 of the $10,000 lean plan, $3,500 of "
                        "the $35,000 reference plan, or $6,000 of the $60,000 "
                        "expanded plan. The reference reserve covers 1.4 months "
                        "at $2,500 monthly opex or 0.25 months at $14,000. "
                        "Reserve cash is not an incurred expense; avoid counting "
                        "the same funded activity again as an additional cash need."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-search-portfolio-sprint",
            "timeline_roadmap",
            "Use the First 30 Days to Establish a Measurable Publishing System",
            "Ship an evidence-backed pilot, not a promised first-month revenue result.",
            12,
            "operating_framework",
            (
                "Four weekly milestones span Days 1–7, 8–14, 15–21, and "
                "22–30. Numeric values are milestone end days. Deliverable "
                "counts are sprint planning assumptions for the four-person "
                "core pod (1 FT + 3 C), not traffic forecasts. First-deal timing remains "
                "the canonical 3–12 months."
            ),
            (
                "Finish with a tested pilot, documented rights, functioning "
                "revenue definitions, and a funded next sprint. Ranking losses, "
                "slow audience growth, and revenue concentration remain explicit risks."
            ),
            [
                (
                    "Days 1–7",
                    "Select one site and one evidence-backed cluster",
                    7.0,
                    (
                        "Operator and editor map 30 queries, review ten competing "
                        "pages, and select one initial site. Record expected "
                        "revenue rails, rights requirements, and a twelve-month cash plan."
                    ),
                ),
                (
                    "Days 8–14",
                    "Test two templates and commission ten briefs",
                    14.0,
                    (
                        "Technical contractor validates canonicals, indexing controls, "
                        "mobile rendering, and analytics events. Editor commissions "
                        "ten distinct briefs and completes the four publication checks."
                    ),
                ),
                (
                    "Days 15–21",
                    "Publish ten reviewed pages with traceable evidence",
                    21.0,
                    (
                        "Release the pilot after editorial and technical review. "
                        "Connect internal links, submit the sitemap, and sample "
                        "GEO citations across twenty fixed prompts while recording "
                        "engine, date, wording, and cited destination."
                    ),
                ),
                (
                    "Days 22–30",
                    "Audit the pilot and fund the next sprint",
                    30.0,
                    (
                        "Review crawl results, measured impressions, referral events, "
                        "and production hours. Test revenue reconciliation with "
                        "clearly labeled synthetic records; rank refresh work and "
                        "record cash needs without counting pending deals as revenue."
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
