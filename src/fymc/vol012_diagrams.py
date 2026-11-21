from __future__ import annotations

VOLUME_012_SUBTITLE = (
    "The Complete Playbook for Equipment Brokerage: "
    "$100,000–$800,000 USD in Annual Broker Commissions, "
    "Built Around a 1 FT + 3 C Four-Person Pod"
)

VOLUME_012_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Lien-Clear Heavy Equipment Broker",
        "subtitle": (
            "Broker construction equipment and fleet assets through documented "
            "ownership, secured-party releases, independent inspection, and escrow."
        ),
        "audience": (
            "Construction equipment specialists and fleet operators building "
            "an asset-light commission business without purchasing inventory."
        ),
        "research_basis": (
            "UCC 9-315 addresses continuing security interests after disposition; "
            "UCC 9-513 addresses termination statements. A filing search alone "
            "does not establish clear ownership or release a creditor's interest. "
            "California Vehicle Code section 11700 supplies a concrete vehicle "
            "dealer licensing example; apply vehicle rules only after classifying "
            "the asset and activity under the relevant state's law."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/9/9-315",
            "https://www.law.cornell.edu/ucc/9/9-513",
            (
                "https://leginfo.legislature.ca.gov/faces/"
                "codes_displaySection.xhtml?lawCode=VEH&sectionNum=11700."
            ),
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-First CNC Matchmaker",
        "subtitle": (
            "Turn machine specifications, service records, and independent "
            "inspection into qualified industrial buyer matches."
        ),
        "audience": (
            "Machine-tool sales specialists serving manufacturers that need "
            "verified CNC capacity, relocation planning, and disciplined acceptance."
        ),
        "research_basis": (
            "UCC 2-313 connects express warranties to qualifying factual "
            "affirmations, descriptions, and samples. UCC 2-316 governs warranty "
            "exclusions and modifications. Build a seller-approved evidence "
            "packet, identify the contracting seller, and distinguish verified "
            "measurements from seller statements; broker status does not turn "
            "every listing statement into a harmless opinion."
        ),
        "sources": [
            "https://www.law.cornell.edu/ucc/2/2-313",
            "https://www.law.cornell.edu/ucc/2/2-316",
            "https://www.law.cornell.edu/ucc/2/2-312",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Export-Ready Industrial Equipment Desk",
        "subtitle": (
            "Build documented equipment matches around classification, "
            "destination, end-user review, and controlled settlement."
        ),
        "audience": (
            "Experienced industrial brokers adding selected cross-border "
            "transactions to an established domestic equipment practice."
        ),
        "research_basis": (
            "15 CFR Part 734 establishes EAR scope; Part 738 addresses the "
            "Commerce Control List and Country Chart. Parts 744 and 746 add "
            "end-user, end-use, and destination restrictions. Classify the "
            "specific machine and transaction rather than assuming that used "
            "equipment or an EAR99 classification permits every shipment."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734",
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-738",
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744",
            "https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-746",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_012_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-equipment-mandate-to-commission",
            "process_flow",
            "From Seller Mandate to Earned Commission",
            "Five documented handoffs keep equipment principal outside broker revenue.",
            1,
            "operating_framework",
            (
                "The operator acts as a broker, not an inventory owner. Contract "
                "terms define commission entitlement, settlement instructions, "
                "inspection scope, and each party's responsibilities. Stage "
                "numbers indicate sequence rather than money or conversion."
            ),
            (
                "Use one transaction identifier across the mandate, serial-number "
                "evidence, lien work, buyer acceptance, and escrow statement. "
                "Recognize only the earned broker commission; never classify "
                "equipment purchase funds as operating revenue."
            ),
            [
                (
                    "Authorize the mandate",
                    "Verify seller identity, authority, asset, and commission terms",
                    1.0,
                    (
                        "Obtain a signed seller mandate naming the legal owner, "
                        "machine serial number or VIN, asking price, commission "
                        "formula, term, and authority to advertise. Independently "
                        "verify the signer's authority before distributing inventory."
                    ),
                ),
                (
                    "Build the evidence packet",
                    "Inspect condition and separate measurements from seller claims",
                    2.0,
                    (
                        "Collect service history, hour-meter evidence, ownership "
                        "documents, and an independent inspection. For CNC assets, "
                        "record controller version, spindle condition, tooling "
                        "inclusions, power requirements, and loading constraints."
                    ),
                ),
                (
                    "Resolve ownership and liens",
                    "Document creditor payoff and asset-specific release mechanics",
                    3.0,
                    (
                        "Search under the correct debtor identity and jurisdiction; "
                        "check certificate-of-title records where applicable. Under "
                        "UCC 9-315, a security interest can survive sale. Obtain "
                        "secured-party authorization and the required release "
                        "documents rather than treating a search result as clearance."
                    ),
                ),
                (
                    "Match and contract the buyer",
                    "Confirm purchasing authority, acceptance terms, and funded capacity",
                    4.0,
                    (
                        "Use Airtable inventory fields and HubSpot buyer alerts "
                        "to match capacity, location, budget, and timing. Document "
                        "inspection acceptance, seller representations, rigging "
                        "responsibility, delivery terms, and the commission trigger."
                    ),
                ),
                (
                    "Settle and reconcile",
                    "Release funds against agreed evidence and book commissions only",
                    5.0,
                    (
                        "Use an independent escrow provider appropriate to the "
                        "transaction. Verify changed wire instructions through a "
                        "previously verified phone number. Reconcile buyer funds, "
                        "creditor payoff, seller proceeds, broker commission, and "
                        "delivery evidence to the signed settlement statement."
                    ),
                ),
            ],
        ),
        (
            "diag-02-annual-equipment-opportunity-funnel",
            "funnel",
            "A Nested Annual Funnel to $450,000",
            "Follow equipment opportunities through five increasingly qualified cohorts.",
            6,
            "illustrative_model",
            (
                "Illustrative annual Base-Case planning cohort, not observed "
                "conversion data. Every count represents equipment opportunities "
                "from the same original 500-record cohort, deduplicated by owner "
                "and asset identifier. Assume 30 settled transactions, each at "
                "$250,000 equipment value and a 6% broker commission."
            ),
            (
                "500 × 40% × 50% × 50% × 60% = 30 settlements. "
                "30 × $15,000 = $450,000 recognized broker revenue. "
                "The corresponding $7,500,000 equipment transaction value belongs "
                "outside revenue. The 6% overall conversion is a planning assumption."
            ),
            [
                (
                    "Screened seller opportunities",
                    "500 distinct equipment opportunities enter the annual cohort",
                    500.0,
                    (
                        "Record owner identity, asset identifier, equipment class, "
                        "location, and disposition timing. Remove duplicate "
                        "listings before calculating any conversion rate."
                    ),
                ),
                (
                    "Signed broker mandates",
                    "200 opportunities retain documented seller authority and pricing",
                    200.0,
                    (
                        "Convert 40% of the original cohort into signed mandates "
                        "with commission terms, evidence access, and a plausible "
                        "asking price; retain rejected reasons in the CRM."
                    ),
                ),
                (
                    "Qualified buyer matches",
                    "100 mandated opportunities secure credible buyer engagement",
                    100.0,
                    (
                        "Convert 50% of mandated opportunities into buyer-matched "
                        "assets. Require named purchasing authority, suitable "
                        "capacity requirements, and a credible funding path; "
                        "email opens do not qualify."
                    ),
                ),
                (
                    "Diligence-ready transactions",
                    "50 matched opportunities reach documented diligence readiness",
                    50.0,
                    (
                        "Convert 50% of buyer-matched opportunities after "
                        "inspection scheduling, ownership review, negotiated "
                        "commercial terms, and a documented settlement route."
                    ),
                ),
                (
                    "Settled commission events",
                    "30 transactions generate fifteen thousand dollars each",
                    30.0,
                    (
                        "Convert 60% of diligence-ready opportunities into "
                        "settlements satisfying the contractual commission "
                        "trigger. Retain failed inspection, lien, funding, and "
                        "timing outcomes rather than deleting lost opportunities."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-commission-waterfall",
            "waterfall",
            "$450,000 Commissions to $157,500 Owner Net",
            "Six bars reconcile the canonical Base-Case 35.0% net margin.",
            3,
            "illustrative_model",
            (
                "Annual USD. Opening revenue and closing owner net are total "
                "bars; the four intervening values are negative expense movements. "
                "Expense allocations illustrate a reconciliation, not supplied "
                "scorecard line items. Contractor fees and deal-variable costs "
                "are separate from the recurring operating-overhead budget."
            ),
            (
                "$450,000 − $120,000 − $72,000 − $48,000 − $52,500 "
                "= $157,500; $157,500 / $450,000 = 35.0%. Recurring "
                "overhead is $4,000 monthly, within the canonical $2,500–$14,000 "
                "monthly range; total annual expenses also include variable "
                "deal costs. Equipment principal never enters this bridge."
            ),
            [
                (
                    "Gross broker commissions",
                    "$450,000 annual revenue from earned broker commissions",
                    450000.0,
                    (
                        "Opening total: 30 illustrative settlements at $15,000 "
                        "commission each. Do not add the $7,500,000 underlying "
                        "equipment value, escrow deposits, or creditor payoffs "
                        "to this revenue figure."
                    ),
                ),
                (
                    "Contractor execution",
                    "Subtract $120,000 for contracted delivery and transaction support",
                    -120000.0,
                    (
                        "Budget contractor sourcing, coordination, and routine "
                        "inspection labor across the three-contractor Base pod. "
                        "Resulting balance: $330,000. Contractor status must follow "
                        "actual working arrangements rather than the seat label."
                    ),
                ),
                (
                    "External deal services",
                    "Subtract $72,000 for incremental specialist and closing services",
                    -72000.0,
                    (
                        "Budget outside diagnostics, equipment-specific specialist "
                        "reports, title work, and deal travel borne by the broker. "
                        "Exclude labor already counted in contractor execution "
                        "and transport paid directly by buyers. Balance: $258,000."
                    ),
                ),
                (
                    "Recurring operating overhead",
                    "Subtract $48,000 for twelve months of operating infrastructure",
                    -48000.0,
                    (
                        "Allocate $4,000 monthly to CRM, inventory matching, "
                        "buyer alerts, insurance, bookkeeping, and communications. "
                        "This is the recurring overhead component, not the total "
                        "monthly equivalent of every expense. Balance: $210,000."
                    ),
                ),
                (
                    "Acquisition and settlement friction",
                    "Subtract $52,500 for acquisition, settlement fees, and losses",
                    -52500.0,
                    (
                        "Illustratively allocate $30,000 to buyer and seller "
                        "acquisition, $12,000 to broker-borne settlement charges, "
                        "and $10,500 to realized claim or collection losses. "
                        "Count each expense once. Resulting balance: $157,500."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$157,500 owner net equals thirty-five percent of revenue",
                    157500.0,
                    (
                        "Closing total, not an additional upward movement. "
                        "Preserve the canonical owner-net definition: no extra "
                        "owner salary or personal tax adjustment is introduced. "
                        "Conservative remains $100,000 × 25% = $25,000; "
                        "Scaled remains $800,000 × 45% = $360,000."
                    ),
                ),
            ],
        ),
        (
            "diag-04-equipment-subniche-commission-yields",
            "horizontal_bars",
            "Compare Commission Yield, Not Equipment Value",
            "Five illustrative sub-niche yields use the same $100,000 sale denominator.",
            2,
            "illustrative_model",
            (
                "Numeric values are commission percentages, not dollars, net "
                "margins, or published market averages. Each bar assumes a "
                "$100,000 equipment sale solely to isolate yield. Actual "
                "commission schedules depend on mandate scope and negotiation; "
                "these bars do not replace canonical annual scenarios."
            ),
            (
                "At a common $100,000 sale value, an 8% commission earns $8,000 "
                "and a 3% commission earns $3,000. Compare inspection effort, "
                "sales-cycle length, claim exposure, and collection reliability "
                "before choosing a niche. Escrow protects settlement mechanics; "
                "it does not establish equipment condition."
            ),
            [
                (
                    "Specialized industrial equipment",
                    "8% illustrative yield earns eight thousand dollars",
                    8.0,
                    (
                        "Assume a scarce, specification-sensitive asset with a "
                        "narrow buyer pool. Verify utilities, controls, guarding, "
                        "and removal scope; higher assumed commission yield can "
                        "be consumed by specialist diligence and slow matching."
                    ),
                ),
                (
                    "CNC machine tools",
                    "6% illustrative yield earns six thousand dollars",
                    6.0,
                    (
                        "Require serial-specific configuration, controller and "
                        "spindle evidence, service records, and independent "
                        "condition review. This 6% assumption also supports the "
                        "separate Base funnel's $250,000 average equipment sale."
                    ),
                ),
                (
                    "Heavy construction equipment",
                    "5% illustrative yield earns five thousand dollars",
                    5.0,
                    (
                        "Check hour-meter consistency, hydraulic condition, "
                        "undercarriage wear, attachment ownership, and lien "
                        "exposure. Document inspection limits where equipment "
                        "cannot be tested under working load."
                    ),
                ),
                (
                    "Warehouse and material-handling assets",
                    "4% illustrative yield earns four thousand dollars",
                    4.0,
                    (
                        "Verify rated capacity, mast configuration, battery "
                        "condition, charger inclusion, and service evidence. "
                        "Separate broker compensation from freight and loading "
                        "charges paid directly to service providers."
                    ),
                ),
                (
                    "Commercial fleet vehicles",
                    "3% illustrative yield earns three thousand dollars",
                    3.0,
                    (
                        "Check VIN, certificate of title, recorded lienholder, "
                        "mileage evidence, and state dealer or broker licensing "
                        "requirements. Reject payment from an unrelated party "
                        "until identity and transaction purpose are resolved."
                    ),
                ),
            ],
        ),
        (
            "diag-05-equipment-statutory-risk-preflight",
            "decision_tree",
            "Four Checks Before Advertising or Releasing Funds",
            "Each unresolved branch has a specific stop condition and corrective action.",
            5,
            "operating_framework",
            (
                "Four ordered decision nodes; numeric values indicate check "
                "sequence. Apply the relevant state's enacted UCC and licensing "
                "rules. Cornell UCC text is a reference model, not a substitute "
                "for identifying the controlling state enactment."
            ),
            (
                "Pass each check with retained evidence. Missing license coverage "
                "halts regulated activity; unresolved ownership halts settlement; "
                "unsupported condition claims halt publication; unresolved export "
                "restrictions halt the affected transaction or shipment."
            ),
            [
                (
                    "Activity and licensing",
                    "Proceed only after classifying asset, jurisdiction, and brokerage activity",
                    1.0,
                    (
                        "Determine whether the activity requires a dealer, "
                        "vehicle broker, auction, or other state authorization. "
                        "California Vehicle Code section 11700 is a vehicle "
                        "dealer example, not a universal CNC licensing rule. "
                        "If required coverage is absent, stop that activity "
                        "until the required authorization is effective."
                    ),
                ),
                (
                    "Ownership and lien release",
                    "Proceed only with verified ownership and executable creditor releases",
                    2.0,
                    (
                        "Apply UCC 9-315 and the applicable title regime. Obtain "
                        "a payoff statement and asset-specific release or sale "
                        "authorization from the secured party. Use an authorized "
                        "UCC-3 amendment or termination under UCC 9-513 as "
                        "appropriate; do not terminate a broader facility merely "
                        "because one machine is being sold."
                    ),
                ),
                (
                    "Condition and warranties",
                    "Proceed only with supportable descriptions and explicit contract allocation",
                    3.0,
                    (
                        "Review seller descriptions, inspection findings, and "
                        "contract language against applicable UCC 2-312, 2-313, "
                        "and 2-316. Identify the seller and the broker's authority. "
                        "Pause unsupported claims; a general as-is statement "
                        "does not automatically erase an express warranty."
                    ),
                ),
                (
                    "Export and payment integrity",
                    "Proceed only after resolving classification, counterparties, and settlement risks",
                    4.0,
                    (
                        "For export transactions, determine EAR scope under "
                        "15 CFR Part 734, classification and destination controls "
                        "under Part 738, and restrictions under Parts 744 and "
                        "746; also assess applicable OFAC sanctions under "
                        "31 CFR Chapter V. Resolve required authorizations "
                        "before shipment and independently verify escrow and "
                        "wire instructions before releasing funds."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-seat-equipment-brokerage-pod",
            "org_architecture",
            "Four Base Seats; Six People at Scale",
            "One full-time owner and three contractors divide commercial and evidence work.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person in the four-person "
                "Conservative and Base pod: 1 FT + 3 C. Contractor seats represent "
                "assigned responsibilities, not necessarily full-time workloads. "
                "Scaled expands to 2 FT + 4 C by adding one full-time commercial "
                "operator and one contractor inspection specialist."
            ),
            (
                "Conservative: $100,000 revenue and $25,000 owner net with "
                "1 FT + 3 C. Base: $450,000 revenue and $157,500 owner net "
                "with the same four people. Scaled: $800,000 revenue and "
                "$360,000 owner net with 2 FT + 4 C. The upper revenue "
                "scenario uses six people, not the four-person Base pod."
            ),
            [
                (
                    "Owner and commercial lead",
                    "One full-time seat owns mandates, pricing, and broker revenue",
                    1.0,
                    (
                        "Own seller qualification, buyer negotiation, signed "
                        "mandates, and commission collection. Review exceptions "
                        "without personally controlling every evidence source. "
                        "At scale, add a second full-time commercial operator "
                        "to split seller development and buyer conversion."
                    ),
                ),
                (
                    "Technical inspection specialist",
                    "One contractor seat owns independent equipment condition evidence",
                    1.0,
                    (
                        "Produce serial-specific inspection reports, photograph "
                        "defects, document test limitations, and estimate repair "
                        "scope separately from sale pricing. Add a second "
                        "contractor inspection specialist at scale to expand "
                        "equipment coverage and reduce scheduling bottlenecks."
                    ),
                ),
                (
                    "Inventory and buyer research analyst",
                    "One contractor seat owns inventory matching and buyer alerts",
                    1.0,
                    (
                        "Normalize Airtable inventory records, deduplicate owner "
                        "and asset identities, maintain HubSpot buyer segments, "
                        "and route relevant alerts. Measure qualified matches "
                        "and buyer replies rather than counting raw messages."
                    ),
                ),
                (
                    "Transaction coordinator",
                    "One contractor seat owns documents and independent settlement reconciliation",
                    1.0,
                    (
                        "Track lien searches, creditor documents, signatures, "
                        "inspection acceptance, and escrow statements. Require "
                        "separate verification of changed payment instructions; "
                        "the person entering a new bank destination must not "
                        "be its sole verifier."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "A $60,000 Asset-Light Startup Allocation",
            "Four cash buckets fit inside the canonical $10,000–$75,000 startup range.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD allocations totaling $60,000. This is "
                "one illustrative capitalization plan, not a prescribed minimum. "
                "Cash reserves are not immediate expenses; spending enters the "
                "appropriate operating category when incurred. Do not add these "
                "allocations again to the annual expense waterfall."
            ),
            (
                "$36,000 + $8,000 + $10,000 + $6,000 = $60,000. "
                "The $36,000 recurring-overhead reserve covers nine months at "
                "$4,000 monthly before revenue, matching the upper end of the "
                "canonical two-to-nine-month first-deal window. Other spending "
                "uses the remaining buckets and must be paced separately."
            ),
            [
                (
                    "Recurring-overhead reserve",
                    "$36,000 reserved for nine months of recurring operations",
                    36000.0,
                    (
                        "Hold this cash against the Base overhead assumption "
                        "of $4,000 monthly. It excludes owner household spending "
                        "and variable closing costs. Track actual runway weekly "
                        "because late commissions can arrive after bills fall due."
                    ),
                ),
                (
                    "Field verification capacity",
                    "$8,000 allocated to early inspections and ownership evidence",
                    8000.0,
                    (
                        "Fund initial specialist inspections, title and filing "
                        "searches, equipment photography, and necessary site "
                        "visits. Require asset-specific scopes and stop spending "
                        "when a seller cannot establish authority or access."
                    ),
                ),
                (
                    "Seller and buyer acquisition",
                    "$10,000 allocated to targeted sourcing and qualified outreach",
                    10000.0,
                    (
                        "Support focused trade-directory research, targeted "
                        "seller outreach, buyer qualification, and selected "
                        "industry visits. Release spending in small batches "
                        "against mandate and buyer-match evidence rather than "
                        "committing the full budget to broad advertising."
                    ),
                ),
                (
                    "Systems and transaction setup",
                    "$6,000 allocated to equipment records and settlement readiness",
                    6000.0,
                    (
                        "Configure Airtable asset records, HubSpot workflows, "
                        "document templates, e-signature, and secure file access. "
                        "Establish escrow-provider verification and bookkeeping "
                        "categories. Purchase no equipment inventory and advance "
                        "no buyer purchase principal from this allocation."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-equipment-brokerage-sprint",
            "timeline_roadmap",
            "Thirty Days to a Documented Brokerage Pipeline",
            "Four weekly milestones build readiness; the first deal can take two to nine months.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days: 7, 14, 21, and 30. "
                "Activity counts are sprint targets, not observed outcomes. "
                "A first-month settlement is not assumed, and the annual "
                "Base funnel is not compressed into this 30-day schedule."
            ),
            (
                "Finish the sprint with a narrow equipment thesis, auditable "
                "asset records, qualified buyer conversations, and a rehearsed "
                "settlement process. Preserve cash for the canonical two-to-nine-"
                "month first-deal window instead of funding the business from "
                "an assumed first-month commission."
            ),
            [
                (
                    "Days 1-7",
                    "Select one niche and establish operating and evidence requirements",
                    7.0,
                    (
                        "Choose a specific equipment class and geography. "
                        "Complete a licensing activity matrix, seller mandate "
                        "template, inspection checklist, and $60,000 cash plan. "
                        "Assign the four Base seats and create Airtable fields "
                        "for serial number, owner, condition, liens, and price."
                    ),
                ),
                (
                    "Days 8-14",
                    "Build twenty screened records and pursue five documented mandates",
                    14.0,
                    (
                        "Target 20 distinct seller opportunities and five "
                        "signed mandates with verified authority and evidence "
                        "access. Establish independent inspection coverage and "
                        "a lien-search workflow. Keep unsigned opportunities "
                        "separate from inventory authorized for advertising."
                    ),
                ),
                (
                    "Days 15-21",
                    "Qualify ten buyer conversations and test three asset matches",
                    21.0,
                    (
                        "Target ten conversations with identified purchasing "
                        "decision-makers and three asset-specific matches. "
                        "Record capacity, budget, location, and purchase timing. "
                        "Test HubSpot buyer alerts against relevant inventory "
                        "and retain explicit reasons for rejected matches."
                    ),
                ),
                (
                    "Days 22-30",
                    "Rehearse settlement and publish a cash-aware pipeline review",
                    30.0,
                    (
                        "Walk one candidate transaction through inspection "
                        "acceptance, creditor payoff, release documents, escrow "
                        "instructions, and commission reconciliation. Use a "
                        "simulation if no transaction is ready. Review cohort "
                        "counts, blocked evidence, cash runway, and the next "
                        "month's seller and buyer follow-up commitments."
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
