from __future__ import annotations

VOLUME_022_SUBTITLE = (
    "The Complete Playbook for Medical Equipment Resale: "
    "$250,000–$1,800,000 USD in Annual Gross Resale Proceeds, "
    "Built Around a 2 FT + 4 C Six-Person Pod and Scaling to Eight People"
)

VOLUME_022_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Traceable Diagnostic Equipment Desk",
        "subtitle": (
            "Build a diagnostic resale operation around serial-level provenance, "
            "documented biomed testing, and buyer-specific acceptance criteria."
        ),
        "audience": (
            "Equipment traders and biomedical service operators selling refurbished "
            "diagnostic devices to independent practices and outpatient facilities."
        ),
        "research_basis": (
            "FDA servicing and remanufacturing guidance supports evaluating each "
            "intervention by its effect on safety, performance specifications, "
            "and intended use. Device registration, listing, and quality-system "
            "duties depend on the actual activities performed; ordinary resale "
            "must not be treated as automatically equivalent to manufacturing. "
            "The commercial thesis is that a complete evidence packet reduces "
            "buyer diligence friction; price premiums remain untested."
        ),
        "sources": [
            "https://www.fda.gov/medical-devices/quality-and-compliance-medical-devices/remanufacturing-medical-devices",
            "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807",
            "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Data-Clean Surgical Asset Exit",
        "subtitle": (
            "Turn facility equipment retirements into documented resale lots "
            "with clear title, decontamination evidence, and verified media sanitization."
        ),
        "audience": (
            "Asset-disposition operators serving surgical centers, hospitals, "
            "and buyers of reusable surgical equipment."
        ),
        "research_basis": (
            "45 CFR 164.310(d) establishes device and media controls for regulated "
            "entities handling electronic protected health information. Business "
            "associate status depends on the service and data relationship, not "
            "merely possession of a device. UCC 9-315 addresses continuation of "
            "security interests after disposition, supporting lien diligence "
            "rather than reliance on a seller invoice alone. Decontamination "
            "and media sanitization require separate evidence records."
        ),
        "sources": [
            "https://www.law.cornell.edu/cfr/text/45/164.310",
            "https://www.law.cornell.edu/cfr/text/45/164.502",
            "https://www.law.cornell.edu/ucc/9/9-315",
            "https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/index.html",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Specialty Equipment Liquidity Desk",
        "subtitle": (
            "Trade veterinary and aesthetic equipment against verified buyer demand, "
            "service access, and model-specific operating restrictions."
        ),
        "audience": (
            "Specialist equipment brokers and refurbishers with access to veterinary "
            "practices, aesthetic clinics, and qualified service contractors."
        ),
        "research_basis": (
            "FDA treats animal devices differently from human medical devices, "
            "including the absence of an animal-device premarket approval requirement; "
            "that distinction does not establish permission for a human-use claim. "
            "21 CFR 801.109 addresses prescription-device labeling conditions, while "
            "radiation-emitting equipment can create additional obligations. "
            "State professional-use and equipment requirements must be checked "
            "for the destination and device. The positioning emphasizes narrow "
            "model expertise rather than presumed regulatory interchangeability."
        ),
        "sources": [
            "https://www.fda.gov/animal-veterinary/animal-health-literacy/how-fda-regulates-animal-devices",
            "https://www.law.cornell.edu/cfr/text/21/801.109",
            "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-J",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_022_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-traceable-resale-workflow",
            "process_flow",
            "From Retired Device to Accepted Resale",
            "Five evidence-backed stages for diagnostic, surgical, veterinary, and aesthetic equipment.",
            1,
            "operating_framework",
            (
                "Stage values indicate sequence, not elapsed time or conversion. "
                "The canonical time to first deal is 3–9 months. Inventory tracking "
                "and service-history indexing automate records, not physical testing "
                "or device-specific regulatory classification."
            ),
            (
                "Keep one serial-level record from sourcing through buyer acceptance; "
                "never substitute a cosmetic refurbishment claim for functional evidence."
            ),
            [
                (
                    "Source against demand",
                    "1 | Buyer need and asset identity",
                    1.0,
                    (
                        "Record model, serial number, intended use, accessories, software "
                        "revision, asking price, and two dated buyer-demand observations. "
                        "Check recalls and service support before committing inventory cash."
                    ),
                ),
                (
                    "Establish transfer rights",
                    "2 | Ownership and disposition evidence",
                    2.0,
                    (
                        "Match seller authority to the serial list, inspect relevant "
                        "UCC filings, and obtain required secured-party release or "
                        "disposition authorization. UCC 9-315 means sale alone does "
                        "not necessarily remove a security interest."
                    ),
                ),
                (
                    "Quarantine and sanitize",
                    "3 | Separate biological and data controls",
                    3.0,
                    (
                        "Require device-compatible decontamination documentation and "
                        "inspect every data-bearing component. Record sanitization "
                        "method and verification separately; do not assume a factory "
                        "reset removes stored patient records or that surface cleaning "
                        "addresses internal contamination."
                    ),
                ),
                (
                    "Restore and verify",
                    "4 | Qualified biomed acceptance evidence",
                    4.0,
                    (
                        "Use model-specific test procedures, calibrated instruments, "
                        "parts traceability, and measured acceptance limits. Evaluate "
                        "servicing versus remanufacturing before changes to performance, "
                        "safety specifications, or intended use; investigate duties "
                        "under 21 CFR Parts 807 and 820 when triggered."
                    ),
                ),
                (
                    "Deliver and close",
                    "5 | Settled proceeds and buyer acceptance",
                    5.0,
                    (
                        "Confirm site readiness, insured freight, installation scope, "
                        "payment settlement, and signed acceptance. Archive test results, "
                        "transfer records, warranty terms, and service history against "
                        "the serial number; recognize equipment resale proceeds rather "
                        "than treating refundable deposits as completed revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-02-serial-lot-conversion-funnel",
            "funnel",
            "A Cohort Funnel That Rejects Weak Inventory Early",
            "One acquisition cohort; each later stage is a subset of the preceding stage.",
            6,
            "illustrative_model",
            (
                "Illustrative cohort of 100 distinct candidate lots followed over "
                "3–9 months, not a monthly sales forecast. One opportunity identifier "
                "persists through all stages; repeat inquiries do not create new lots. "
                "Counts do not establish prices, annual revenue, or realized margin."
            ),
            (
                "Four completed sales from 100 sourced opportunities represent "
                "4% cohort conversion, not four sales during the launch sprint."
            ),
            [
                (
                    "Identified resale lots",
                    "100 lots | Starting acquisition cohort",
                    100.0,
                    (
                        "Log 100 distinct serial-defined lots with a named seller, "
                        "device family, location, asking terms, and evidence of "
                        "ownership authority; remove duplicate listings before counting."
                    ),
                ),
                (
                    "Documented screening passes",
                    "60 lots | 60% of starting cohort",
                    60.0,
                    (
                        "Retain 60 of the original 100 after checking provenance, "
                        "recall status, manufacturer support, and availability of "
                        "decontamination and service records; exclude undocumented inventory."
                    ),
                ),
                (
                    "Technical and economic passes",
                    "30 lots | 50% of preceding stage",
                    30.0,
                    (
                        "Retain 30 of those 60 after qualified inspection, landed-cost "
                        "estimates, parts availability, and buyer-price comparisons; "
                        "reject lots whose credible repair exposure erases contribution."
                    ),
                ),
                (
                    "Acquired buyer-backed lots",
                    "12 lots | 40% of preceding stage",
                    12.0,
                    (
                        "Acquire 12 of those 30 within the working-capital limit after "
                        "documenting qualified buyer interest and enforceable purchase "
                        "terms; buyer interest alone is neither a sale nor cash."
                    ),
                ),
                (
                    "Accepted and settled sales",
                    "4 lots | 33.3% of preceding stage",
                    4.0,
                    (
                        "Close four of the 12 acquired lots after testing, delivery, "
                        "acceptance, and payment settlement. The other eight remain "
                        "open cohort inventory or documented dispositions; they are "
                        "not counted as completed sales."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-waterfall",
            "waterfall",
            "Base-Case Gross Proceeds to Owner Net",
            "$1,025,000 annual gross equipment resale proceeds → $164,000 annual owner net.",
            3,
            "illustrative_model",
            (
                "USD per year. First and last bars are absolute totals; the middle "
                "four bars are signed deductions. Acquisition, refurbishment, and "
                "delivery are modeled direct costs, separate from operating overhead. "
                "The cost allocation is illustrative; canonical revenue, net margin, "
                "and owner net are fixed. No unlisted residual deduction is assumed."
            ),
            (
                "$1,025,000 − $574,000 − $102,500 − $41,000 − $143,500 "
                "= $164,000, exactly 16.0% of gross resale proceeds. "
                "Gross proceeds are operator equipment sales, not a brokerage fee "
                "or the buyer's downstream clinical receipts."
            ),
            [
                (
                    "Gross resale proceeds",
                    "$1,025,000 | Opening total, 100.0%",
                    1025000.0,
                    (
                        "Canonical Base-Case annual equipment resale revenue. "
                        "Recognize sales under the operator's applicable accounting "
                        "policy; exclude pass-through sales taxes and refundable deposits "
                        "from this illustrative revenue total."
                    ),
                ),
                (
                    "Equipment acquisition",
                    "−$574,000 | 56.0% of gross proceeds",
                    -574000.0,
                    (
                        "Cost of equipment sold, including purchase premiums assigned "
                        "to those units; remaining bridge value is $451,000. "
                        "Unsold purchases stay in inventory rather than becoming "
                        "current-period cost of sold equipment."
                    ),
                ),
                (
                    "Refurbishment and biomed QA",
                    "−$102,500 | 10.0% of gross proceeds",
                    -102500.0,
                    (
                        "Parts, direct contractor bench labor, calibration, documented "
                        "decontamination, and unit-level testing assigned to sold units; "
                        "remaining bridge value is $348,500. Do not charge the same "
                        "contractor invoice again within overhead."
                    ),
                ),
                (
                    "Delivery and transaction costs",
                    "−$41,000 | 4.0% of gross proceeds",
                    -41000.0,
                    (
                        "Crating, insured freight, payment charges, and modeled "
                        "sale-related warranty expense; remaining bridge value is "
                        "$307,500. Assign warranty exposure consistently and avoid "
                        "counting both the provision and settlement as separate costs."
                    ),
                ),
                (
                    "Pod and operating overhead",
                    "−$143,500 | 14.0% of gross proceeds",
                    -143500.0,
                    (
                        "Loaded payroll, premises, insurance, software, selling expense, "
                        "and administration consume $143,500 annually, approximately "
                        "$11,958 monthly within the $5,000–$22,000 canonical operating "
                        "range. This is a budget envelope requiring local staffing validation."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$164,000 | Closing total, 16.0%",
                    164000.0,
                    (
                        "Canonical Base-Case modeled owner net, with no additional "
                        "deduction invented for an unspecified tax or funding structure. "
                        "Reference scenarios remain $250,000 × 10% = $25,000 and "
                        "$1,800,000 × 22% = $396,000; owner net is not gross margin."
                    ),
                ),
            ],
        ),
        (
            "diag-04-specialty-contribution-yields",
            "horizontal_bars",
            "Compare Contribution Yield Before Buying",
            "Five illustrative specialty and settlement combinations, measured on equal $10,000 sales.",
            2,
            "illustrative_model",
            (
                "Each numeric value is a percentage of a hypothetical $10,000 sale "
                "remaining after equipment acquisition, refurbishment, freight, "
                "transaction costs, and modeled warranty expense, before shared "
                "overhead. These are screening examples, not observed market yields "
                "or scenario net margins. Payment method alone does not determine yield."
            ),
            (
                "Use quoted unit costs to replace these assumptions. The Base-Case "
                "waterfall has 30% contribution before 14% overhead; these specialty "
                "bars are not a weighted revenue mix or a replacement scorecard."
            ),
            [
                (
                    "Diagnostic ultrasound with bank settlement",
                    "32% contribution | $3,200 per $10,000 sale",
                    32.0,
                    (
                        "$10,000 sale less $5,400 acquisition, $900 refurbishment, "
                        "and $500 delivery, payment, and warranty costs leaves $3,200. "
                        "Test probes for defects and verify software-license transfer "
                        "before accepting the apparent spread."
                    ),
                ),
                (
                    "Surgical instrument sets with bank settlement",
                    "35% contribution | $3,500 per $10,000 sale",
                    35.0,
                    (
                        "$10,000 sale less $4,700 acquisition, $1,300 refurbishment, "
                        "and $500 delivery, payment, and warranty costs leaves $3,500. "
                        "Confirm set completeness and reusable-device instructions; "
                        "exclude single-use reprocessing from this illustration."
                    ),
                ),
                (
                    "Veterinary monitors with bank settlement",
                    "28% contribution | $2,800 per $10,000 sale",
                    28.0,
                    (
                        "$10,000 sale less $5,600 acquisition, $1,000 refurbishment, "
                        "and $600 delivery, payment, and warranty costs leaves $2,800. "
                        "Verify intended animal use, compatible accessories, and "
                        "service access rather than assuming human-device equivalence."
                    ),
                ),
                (
                    "Aesthetic laser with card settlement",
                    "24% contribution | $2,400 per $10,000 sale",
                    24.0,
                    (
                        "$10,000 sale less $5,500 acquisition, $1,300 refurbishment, "
                        "and $800 delivery, card, and warranty costs leaves $2,400. "
                        "Validate handpiece life, energy output, destination requirements, "
                        "and dispute exposure before releasing equipment."
                    ),
                ),
                (
                    "Diagnostic cart with third-party lender settlement",
                    "30% contribution | $3,000 per $10,000 sale",
                    30.0,
                    (
                        "$10,000 sale less $5,300 acquisition, $1,100 refurbishment, "
                        "and $600 delivery, settlement, and warranty costs leaves $3,000. "
                        "Confirm lender acceptance conditions, payout timing, and "
                        "recourse terms; funding approval alone is not settled proceeds."
                    ),
                ),
            ],
        ),
        (
            "diag-05-device-release-decision-tree",
            "decision_tree",
            "Four Checks Before Purchase or Release",
            "A failed check moves the lot into documented hold or rejection, never an automatic exception.",
            5,
            "operating_framework",
            (
                "Numeric values indicate check order, not risk scores. Each affirmative "
                "branch advances to the next check; unresolved evidence holds the lot, "
                "and an unremediable defect rejects it. Complete purchase-stage checks "
                "before commitment and repeat release-stage checks before shipment. "
                "Requirements depend on device, activity, destination, and data role."
            ),
            (
                "Keep title, device regulation, patient-data handling, and biological "
                "safety as distinct evidence tracks. Passing one does not satisfy another."
            ),
            [
                (
                    "Clear title and transfer authority?",
                    "Yes: advance | Unresolved: hold purchase",
                    1.0,
                    (
                        "Match seller authority, asset serials, sale terms, and relevant "
                        "lien searches. Under UCC 9-315, a security interest can survive "
                        "a sale unless disposition is authorized or another rule applies. "
                        "Obtain applicable release evidence; reject assets the seller "
                        "cannot lawfully transfer."
                    ),
                ),
                (
                    "Correct device and activity classification?",
                    "Yes: advance | Duty unresolved: hold work",
                    2.0,
                    (
                        "Review intended use, prescription restrictions under 21 CFR "
                        "801.109, and whether proposed work constitutes remanufacturing. "
                        "Assess registration and listing under 21 CFR Part 807 and "
                        "manufacturer quality-system duties under Part 820 when applicable. "
                        "Check destination-state licensing and radiation requirements; "
                        "do not assume every reseller must register as a manufacturer."
                    ),
                ),
                (
                    "Patient-data exposure resolved?",
                    "Yes: advance | Verification fails: hold media",
                    3.0,
                    (
                        "Identify drives, removable media, network credentials, and "
                        "embedded storage. Determine covered-entity or business-associate "
                        "responsibilities under 45 CFR 164.502(e), with written terms "
                        "under 164.504(e) where required. For regulated handling, apply "
                        "164.310(d) device and media controls; verify sanitization while "
                        "preserving safe device operation and software entitlements."
                    ),
                ),
                (
                    "Decontamination and functional acceptance complete?",
                    "Yes: release | Evidence incomplete: quarantine",
                    4.0,
                    (
                        "Require manufacturer-compatible decontamination records, "
                        "calibrated biomed results, accessory completeness, recall "
                        "resolution, and agreed buyer acceptance limits. Where occupational "
                        "exposure is reasonably anticipated, apply 29 CFR 1910.1030 "
                        "bloodborne-pathogen controls. Reject equipment lacking a credible "
                        "route to safe, supported operation."
                    ),
                ),
            ],
        ),
        (
            "diag-06-core-and-scaled-pod-seats",
            "org_architecture",
            "Six Core Seats, Eight at Scaled Capacity",
            "Conservative and Base: 2 FT + 4 C; Scaled Small-Team: 3 FT + 5 C.",
            11,
            "operating_framework",
            (
                "Each numeric value represents one person in the eight-person scaled "
                "architecture. The first six seats form the core pod; the final two "
                "are scaled additions. FT means full-time and C means contractor, "
                "not a full-time-equivalent commitment. Contractor hours and local "
                "loaded payroll must fit the modeled cost envelopes."
            ),
            (
                "The same six-person core supports canonical $250,000 and $1,025,000 "
                "gross-revenue scenarios. The $1,800,000 scaled scenario uses eight "
                "people; automation does not remove technical accountability."
            ),
            [
                (
                    "Core FT 1: Commercial lead",
                    "One core full-time seat | Buying and sales",
                    1.0,
                    (
                        "Own demand qualification, acquisition ceilings, written sale "
                        "terms, contribution estimates, and aged-stock decisions. "
                        "Review title exceptions with the relevant specialist and "
                        "keep commercial urgency separate from technical release."
                    ),
                ),
                (
                    "Core FT 2: Operations lead",
                    "One core full-time seat | Inventory and records",
                    1.0,
                    (
                        "Own receiving quarantine, serial-level inventory tracking, "
                        "service-history indexing, cost allocation, documentation "
                        "completeness, and buyer acceptance scheduling. Reconcile physical "
                        "assets against the inventory ledger every week."
                    ),
                ),
                (
                    "Core C 1: Biomedical specialist",
                    "One core contractor seat | Testing and repair",
                    1.0,
                    (
                        "Perform model-qualified inspection, repair planning, calibration "
                        "checks, functional testing, and signed technical findings. "
                        "Escalate unavailable parts or unsupported software before "
                        "the commercial lead commits acquisition funds."
                    ),
                ),
                (
                    "Core C 2: Decontamination technician",
                    "One core contractor seat | Biological controls",
                    1.0,
                    (
                        "Apply device-compatible cleaning and decontamination procedures, "
                        "document process conditions, and flag inaccessible contamination. "
                        "Coordinate occupational exposure controls and never equate "
                        "clean appearance with completed decontamination."
                    ),
                ),
                (
                    "Core C 3: Specialist freight coordinator",
                    "One core contractor seat | Packing and delivery",
                    1.0,
                    (
                        "Arrange shock-sensitive packing, carrier selection, declared "
                        "value, transit evidence, receiving appointments, and damage "
                        "claims. Verify lift access, power requirements, and installation "
                        "responsibilities before dispatch."
                    ),
                ),
                (
                    "Core C 4: Data and documentation specialist",
                    "One core contractor seat | Media and traceability",
                    1.0,
                    (
                        "Map storage locations, perform authorized sanitization and "
                        "verification, preserve permitted service evidence, and assemble "
                        "release packets. Escalate device-specific regulatory questions "
                        "for qualified review rather than inventing certifications."
                    ),
                ),
                (
                    "Scaled FT 3: Account and inventory planner",
                    "One additional full-time seat | Scaled scenario only",
                    1.0,
                    (
                        "Own recurring buyer accounts, replenishment forecasts, site "
                        "readiness follow-up, and aging reviews at the $1,800,000 "
                        "gross-revenue scenario. Add capacity against measured workload "
                        "and funded payroll, not a revenue aspiration alone."
                    ),
                ),
                (
                    "Scaled C 5: Additional field biomed specialist",
                    "One additional contractor seat | Scaled scenario only",
                    1.0,
                    (
                        "Provide additional qualified bench or installation capacity "
                        "when test queues and geography exceed the core specialist's "
                        "coverage. Maintain the same instrument calibration, evidence "
                        "standards, and serial-level accountability."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Four Buckets Protect the Inventory Cycle",
            "Illustrative $200,000 startup stack, with $75,000 and $400,000 comparison allocations.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD in the central $200,000 startup allocation. "
                "Each bucket uses the same percentage at the $75,000 lower and "
                "$400,000 upper endpoints, allowing proportional stacked comparison. "
                "Capital allocations are funding uses, not annual expense or revenue. "
                "The central allocation is not an additional earnings scenario."
            ),
            (
                "All three capital stacks reconcile: $75,000, $200,000, and $400,000. "
                "Protect cash for slow sales and repair surprises; an initial "
                "inventory purchase is not immediate recognized profit."
            ),
            [
                (
                    "Equipment acquisition reserve",
                    "$100,000 central allocation | 50% of capital",
                    100000.0,
                    (
                        "Lower stack: $37,500; central stack: $100,000; upper stack: "
                        "$200,000. Fund serial-defined inventory within per-model "
                        "exposure limits and documented buyer demand. Keep unsold "
                        "equipment on the inventory ledger and review aging weekly."
                    ),
                ),
                (
                    "Refurbishment and testing capacity",
                    "$40,000 central allocation | 20% of capital",
                    40000.0,
                    (
                        "Lower stack: $15,000; central stack: $40,000; upper stack: "
                        "$80,000. Fund inspection, parts, bench work, calibrated test "
                        "equipment access, decontamination, and service documentation. "
                        "Separate durable tooling from unit-level inventory costs."
                    ),
                ),
                (
                    "Operating cash buffer",
                    "$50,000 central allocation | 25% of capital",
                    50000.0,
                    (
                        "Lower stack: $18,750; central stack: $50,000; upper stack: "
                        "$100,000. At the modeled $11,958 monthly Base-Case overhead, "
                        "the central buffer covers about 4.2 months before direct "
                        "inventory spending; a nine-month first-sale delay requires "
                        "lower burn or additional funded liquidity."
                    ),
                ),
                (
                    "Setup and transaction reserve",
                    "$10,000 central allocation | 5% of capital",
                    10000.0,
                    (
                        "Lower stack: $3,750; central stack: $10,000; upper stack: "
                        "$20,000. Fund insurance deposits, inventory-system setup, "
                        "initial packing materials, and specialist classification "
                        "review. Track refundable deposits separately from expenses "
                        "and avoid duplicating operating-buffer charges."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days-roadmap",
            "timeline_roadmap",
            "Thirty Days to an Evidence-Ready Trading Operation",
            "Build sourcing, testing, cash controls, and buyer evidence before expecting a closed deal.",
            12,
            "operating_framework",
            (
                "Numeric values indicate milestone order. The four periods cover "
                "Days 1–30 without gaps; the final period contains nine days. "
                "These are readiness milestones, not revenue commitments. Canonical "
                "time to first deal remains 3–9 months."
            ),
            (
                "End the sprint with a controlled acquisition pipeline and testable "
                "unit economics, not an invented first-month sale or compulsory purchase."
            ),
            [
                (
                    "Days 1-7",
                    "Define scope and establish the evidence register",
                    1.0,
                    (
                        "Select two supported device families and one destination "
                        "market. Record applicable FDA activity questions, state "
                        "requirements, intended use, title documents, and data exposure. "
                        "Build a serial-level SQLite or spreadsheet register with "
                        "links to a restricted-access evidence folder."
                    ),
                ),
                (
                    "Days 8-14",
                    "Qualify supply and verify buyer demand",
                    2.0,
                    (
                        "Interview five prospective buyers and screen ten distinct "
                        "seller lots. Record model preferences, budget authority, "
                        "installation constraints, and comparable asking prices. "
                        "Obtain written biomed and freight quotes for the two strongest "
                        "lots without treating interest as a purchase commitment."
                    ),
                ),
                (
                    "Days 15-21",
                    "Rehearse inspection and reconcile unit economics",
                    3.0,
                    (
                        "Inspect one authorized candidate with a qualified biomed "
                        "contractor. Review storage-media access, decontamination evidence, "
                        "test limits, service support, and title records. Reconcile "
                        "quoted acquisition, repair, delivery, and warranty exposure "
                        "against a defensible buyer price and the available cash buffer."
                    ),
                ),
                (
                    "Days 22-30",
                    "Prepare one complete acquisition decision packet",
                    4.0,
                    (
                        "Assemble price ceiling, serial list, seller authority, "
                        "classification review, service plan, sanitization method, "
                        "delivery quote, and draft acceptance terms. Proceed only "
                        "with resolved material issues and sufficient cash; otherwise "
                        "retain a documented rejection and continue sourcing."
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
