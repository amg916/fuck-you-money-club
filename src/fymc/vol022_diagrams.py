from __future__ import annotations

VOLUME_022_SUBTITLE = (
    "The Complete Playbook for Medical Equipment Resale: "
    "$250,000–$1,800,000 USD in Annual Gross Resale Proceeds, "
    "Built Around a 1 FT + 3 C Four-Person Pod and Scaling to Six People"
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
                "The canonical time to first deal is 2–7 months. Inventory tracking "
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
                "2–7 months, not a monthly sales forecast. One opportunity identifier "
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
                        "$11,958 monthly within the $4,000–$18,000 canonical operating "
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
            "diag-06-four-core-and-two-expansion-seats",
            "org_architecture",
            "Four Core Seats, Six at Scaled Capacity",
            "Conservative and Base: 1 FT + 3 C; Scaled Small-Team: 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "The first four entries are core seats with numeric values of 1, "
                "representing 1 FT + 3 C. The final two entries have numeric values "
                "of 0 because they are expansion seats excluded from core headcount; "
                "adding 1 FT + 1 C produces the six-person scaled pod of 2 FT + 4 C. "
                "FT means full-time and C means contractor, not a full-time-equivalent "
                "commitment. External vendor and trade sub-crews are charged to direct "
                "subcontractor/COGS pass-through, not internal pod headcount. Allocate "
                "each labor charge once; contractor hours and local loaded payroll "
                "must fit the modeled cost envelopes."
            ),
            (
                "The four-person core supports canonical $250,000 and $1,025,000 "
                "gross-revenue scenarios; the $1,800,000 scaled scenario uses six people. "
                "FYMC 2.0 score: 85/100; rank #20 of 29; tier: Elite Small-Team Cash "
                "Machine. Automation does not remove technical accountability."
            ),
            [
                (
                    "Core FT 1: Commercial and operations lead",
                    "One core full-time seat | Buying, sales, and inventory",
                    1.0,
                    (
                        "Own demand qualification, acquisition ceilings, written sale "
                        "terms, contribution estimates, and aged-stock decisions. "
                        "Oversee receiving quarantine, cost allocation, and buyer "
                        "acceptance scheduling; reconcile physical assets against "
                        "the inventory ledger weekly. Keep commercial urgency "
                        "separate from technical release."
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
                        "the commercial lead commits acquisition funds. Specify "
                        "qualified external bench work when needed and allocate "
                        "unit-level labor to direct costs without duplicate overhead."
                    ),
                ),
                (
                    "Core C 2: Logistics and decontamination coordinator",
                    "One core contractor seat | Biological controls and delivery",
                    1.0,
                    (
                        "Coordinate qualified external decontamination providers, "
                        "device-compatible procedures, process records, and occupational "
                        "exposure controls. Arrange packing, insured freight, receiving "
                        "appointments, site readiness, and damage claims. External "
                        "cleaning, packing, and installation crews are direct "
                        "subcontractor/COGS pass-through, not additional pod seats."
                    ),
                ),
                (
                    "Core C 3: Data and documentation specialist",
                    "One core contractor seat | Media and traceability",
                    1.0,
                    (
                        "Map storage locations, perform authorized sanitization and "
                        "verification, preserve permitted service evidence, and assemble "
                        "release packets. Maintain serial-level inventory records and "
                        "service-history indexing. Escalate device-specific regulatory "
                        "questions for qualified review rather than inventing certifications."
                    ),
                ),
                (
                    "Scaled FT 2: Account and inventory planner",
                    "Expansion only | One additional FT seat; zero core count",
                    0.0,
                    (
                        "Join only at scaled capacity to own recurring buyer accounts, "
                        "replenishment forecasts, site readiness follow-up, and aging "
                        "reviews at the $1,800,000 gross-revenue scenario. Add capacity "
                        "against measured workload and funded payroll, not a revenue "
                        "aspiration alone; this seat raises full-time headcount to two."
                    ),
                ),
                (
                    "Scaled C 4: Additional field biomed specialist",
                    "Expansion only | One additional C seat; zero core count",
                    0.0,
                    (
                        "Join only at scaled capacity to provide additional qualified "
                        "bench or installation coverage when test queues and geography "
                        "exceed the core specialist's capacity. Maintain the same "
                        "instrument calibration, evidence standards, and serial-level "
                        "accountability; this seat raises contractor headcount to four."
                    ),
                ),
            ],
        ),
        (
            "diag-07-lean-reference-expanded-startup-allocation",
            "stacked_comparison",
            "Four Buckets Allocate the $55,000 Reference Budget",
            "Startup capital: $20,000–$95,000 USD; compare $20,000 lean, $55,000 reference, and $95,000 expanded.",
            4,
            "illustrative_model",
            (
                "Numeric values are USD in the central $55,000 reference startup "
                "plan, within the canonical $20,000–$95,000 range. Each bucket uses "
                "the same percentage at the $20,000 lean and $95,000 expanded "
                "endpoints, allowing proportional stacked comparison. Capital "
                "allocations are funding uses, not annual expense or revenue. "
                "The reference allocation is not an additional earnings scenario "
                "or a guarantee of sufficient runway."
            ),
            (
                "All four buckets reconcile at each funding level: $20,000 lean, "
                "$55,000 reference, and $95,000 expanded. Monthly opex remains "
                "$4,000–$18,000 and time to first deal remains 2–7 months; match "
                "commitments to funded liquidity rather than assuming the cash "
                "buffer covers the entire launch. Inventory purchases are not profit."
            ),
            [
                (
                    "Equipment acquisition reserve",
                    "$27,500 reference allocation | 50% of capital",
                    27500.0,
                    (
                        "Lean stack: $10,000; reference stack: $27,500; expanded stack: "
                        "$47,500. Fund serial-defined inventory within per-model "
                        "exposure limits and documented buyer demand. Keep unsold "
                        "equipment on the inventory ledger and review aging weekly."
                    ),
                ),
                (
                    "Refurbishment and testing capacity",
                    "$11,000 reference allocation | 20% of capital",
                    11000.0,
                    (
                        "Lean stack: $4,000; reference stack: $11,000; expanded stack: "
                        "$19,000. Fund inspection, parts, bench work, calibrated test "
                        "equipment access, decontamination, and service documentation. "
                        "Separate durable tooling from unit-level inventory costs."
                    ),
                ),
                (
                    "Operating cash buffer",
                    "$13,750 reference allocation | 25% of capital",
                    13750.0,
                    (
                        "Lean stack: $5,000; reference stack: $13,750; expanded stack: "
                        "$23,750. At the modeled $11,958 monthly Base-Case overhead, "
                        "the reference buffer covers about 1.15 months before direct "
                        "inventory spending, shorter than the 2–7 month first-deal "
                        "window. Phase commitments, reduce launch burn, or secure "
                        "additional liquidity before taking on unfunded obligations."
                    ),
                ),
                (
                    "Setup and transaction reserve",
                    "$2,750 reference allocation | 5% of capital",
                    2750.0,
                    (
                        "Lean stack: $1,000; reference stack: $2,750; expanded stack: "
                        "$4,750. Fund insurance deposits, inventory-system setup, "
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
                "time to first deal remains 2–7 months."
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
