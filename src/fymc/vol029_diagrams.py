from __future__ import annotations

VOLUME_029_SUBTITLE = (
    "The Complete Playbook for Insurance Restoration: "
    "$500,000–$2,500,000 USD in Annual Gross Restoration Billings "
    "with a 2 FT + 2 C (4 People) Core Pod, Expanding to 3 FT + 3 C (6 People) at Scale"
)

VOLUME_029_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Evidence-First Restoration Operator",
        "subtitle": (
            "Build water, fire, and mold restoration files that connect "
            "authorized scope, field measurements, job costs, and collections."
        ),
        "audience": (
            "Restoration owners assembling a 2 FT + 2 C (four-person) "
            "core pod around documented mitigation and reconstruction."
        ),
        "research_basis": (
            "29 CFR 1910.134 establishes respiratory-protection requirements "
            "when respirators are required. 40 CFR 745.85 establishes work "
            "practices for covered renovation work. These requirements support "
            "an evidence-first operating model; they do not establish demand "
            "or validate the proposed positioning. Use applicable IICRC "
            "practices for psychrometric and moisture documentation without "
            "representing a private standard as a contractor license."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-29/section-1910.134",
            "https://www.ecfr.gov/current/title-40/section-745.85",
            "https://www.epa.gov/lead/renovation-repair-and-painting-program",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Contractor-Scope Collections Playbook",
        "subtitle": (
            "Turn measured restoration work into supported invoices without "
            "crossing into unauthorized public adjusting."
        ),
        "audience": (
            "Contractor-led restoration firms using Xactimate estimates and "
            "supplements while retaining control of receivables and scope."
        ),
        "research_basis": (
            "Texas Insurance Code sections 4102.051 and 4102.163 distinguish "
            "licensed public adjusting from contractor activity and restrict "
            "dual-role conduct. Texas Business and Commerce Code section "
            "27.02 addresses property-insurance deductible practices. These "
            "Texas examples support role separation and documented collection "
            "procedures; each operating state requires its own rule mapping."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.4102.htm#4102.051",
            "https://statutes.capitol.texas.gov/Docs/IN/htm/IN.4102.htm#4102.163",
            "https://statutes.capitol.texas.gov/Docs/BC/htm/BC.27.htm#27.02",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Cash-Controlled Restoration Pod",
        "subtitle": (
            "Match dispatch capacity, remediation credentials, and working "
            "capital before accepting the next storm-loss job."
        ),
        "audience": (
            "Owner-operators managing $18,000–$75,000 USD of startup capital "
            "across a 2 FT + 2 C (four-person) core and "
            "3 FT + 3 C (six-person) scaled pod."
        ),
        "research_basis": (
            "Texas Occupations Code Chapter 1958 provides a concrete example "
            "of state mold-assessment and remediation regulation. OSHA "
            "construction standards establish jobsite safety responsibilities. "
            "These operating constraints justify explicit credential and "
            "capacity checks, but do not substantiate revenue forecasts."
        ),
        "sources": [
            "https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1958.htm",
            "https://www.ecfr.gov/current/title-29/section-1926.20",
            "https://www.ecfr.gov/current/title-29/section-1926.1101",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_029_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-evidence-to-collection",
            "process_flow",
            "From Loss Intake to Collected Restoration Invoice",
            "Five accountable handoffs connect field evidence with job economics.",
            1,
            "operating_framework",
            (
                "Stage numbers indicate sequence, not conversion rates. "
                "Restoration contract billings are operator revenue; total "
                "insured property value and insurer claim reserves are not."
            ),
            (
                "Dispatch, photo documentation, and job-cost tracking automate "
                "handoffs without deciding coverage or negotiating policy rights."
            ),
            [
                (
                    "Qualify the loss",
                    "Intake and jurisdiction review",
                    1,
                    (
                        "Record property address, water source or fire damage, "
                        "occupancy, access authority, emergency hazards, and "
                        "required contractor or remediation credentials."
                    ),
                ),
                (
                    "Authorize the work",
                    "Signed scope and payment terms",
                    2,
                    (
                        "Obtain the customer's work authorization, explain "
                        "deductible responsibilities, and document payment "
                        "terms without promising insurer coverage."
                    ),
                ),
                (
                    "Mitigate and measure",
                    "Time-stamped field evidence",
                    3,
                    (
                        "Assign drying equipment and responsible technicians; "
                        "record temperature, relative humidity, humidity ratio, "
                        "material moisture, equipment days, and dated photographs "
                        "using applicable IICRC documentation practices."
                    ),
                ),
                (
                    "Estimate and reconcile",
                    "Supported Xactimate scope",
                    4,
                    (
                        "Tie quantities, labor, equipment, and supplements to "
                        "actual work and supporting evidence. Route policy "
                        "interpretation or claim negotiation outside contractor scope."
                    ),
                ),
                (
                    "Invoice and collect",
                    "Receivable and margin closeout",
                    5,
                    (
                        "Submit an itemized invoice, track customer and insurer "
                        "remittance paths, resolve contractual scope discrepancies, "
                        "and reconcile receipts against job costs without "
                        "unauthorized public adjusting."
                    ),
                ),
            ],
        ),
        (
            "diag-02-loss-inquiry-cohort",
            "funnel",
            "A Single Restoration Inquiry Cohort",
            "120 inquiries narrow to 30 fully collected jobs at day 120.",
            6,
            "illustrative_model",
            (
                "Hypothetical cohort followed for 120 days after intake closes. "
                "Every later group is a subset of the preceding group. Counts "
                "are neither annual sales forecasts nor recognized revenue."
            ),
            (
                "Separate lead qualification, completed work, and cash receipt; "
                "a paid-job count cannot substitute for earned contract revenue."
            ),
            [
                (
                    "Recorded inquiries",
                    "120 inquiries; 100% of intake",
                    120,
                    (
                        "Log every unique loss inquiry with source, address, "
                        "contact permission, and incident date; remove duplicate "
                        "calls concerning the same property and event."
                    ),
                ),
                (
                    "Qualified opportunities",
                    "84 qualified; 70% of intake",
                    84,
                    (
                        "Retain jobs inside the service radius with appropriate "
                        "credentials, accessible premises, available capacity, "
                        "and a customer able to authorize work."
                    ),
                ),
                (
                    "Authorized jobs",
                    "48 signed; 57.1% of qualified",
                    48,
                    (
                        "Count only executed work authorizations with a defined "
                        "scope and payment terms; insurer acknowledgment alone "
                        "does not create customer authorization."
                    ),
                ),
                (
                    "Completed and invoiced",
                    "36 completed; 75% of authorized",
                    36,
                    (
                        "Require completed contracted scope, supporting job "
                        "records, and an issued invoice; twelve authorized "
                        "jobs remain outside this completed subset."
                    ),
                ),
                (
                    "Fully collected jobs",
                    "30 collected; 83.3% of completed",
                    30,
                    (
                        "Require cleared payment against the full outstanding "
                        "invoice balance; six completed jobs remain unpaid "
                        "or partially paid at the observation cutoff."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-profit-bridge",
            "waterfall",
            "Base-Case Gross Billings to Owner Net Profit",
            "$1,500,000 revenue less $1,305,000 costs leaves $195,000.",
            3,
            "illustrative_model",
            (
                "Annual USD. First bar is opening revenue; four negative bars "
                "are cost deductions; the sixth bar is the closing total, "
                "not an additional cash inflow. Cost allocations are illustrative; "
                "canonical scenario revenue and net profit remain fixed."
            ),
            (
                "Conservative: $500,000 × 8% = $40,000 with 2 FT + 2 C. "
                "Base: $1,500,000 × 13.0% = $195,000 with 2 FT + 2 C. "
                "Scaled: $2,500,000 × 18% = $450,000 with 3 FT + 3 C."
            ),
            [
                (
                    "Gross restoration billings",
                    "$1,500,000 opening revenue; 100%",
                    1500000,
                    (
                        "Recognized restoration contract revenue includes "
                        "subcontracted work and materials. Do not substitute "
                        "total claim value, property value, or cash advances."
                    ),
                ),
                (
                    "Subcontractors and materials",
                    "−$795,000 direct costs; 53%",
                    -795000,
                    (
                        "Charge actual contractor invoices and consumed "
                        "materials to jobs. The 2 FT + 2 C core pod includes "
                        "two individual contractor seats, not employee salaries. "
                        "External vendor and trade sub-crews are charged to "
                        "direct subcontractor/COGS pass-through and are not "
                        "included in internal pod headcount."
                    ),
                ),
                (
                    "Employee payroll and burden",
                    "−$270,000 employee costs; 18%",
                    -270000,
                    (
                        "Illustrative loaded annual payroll for the two "
                        "full-time seats in the 2 FT + 2 C core pod averages "
                        "$135,000 per FT seat, including the working "
                        "owner-manager seat where applicable."
                    ),
                ),
                (
                    "Field operating costs",
                    "−$105,000 field operations; 7%",
                    -105000,
                    (
                        "Allocate vehicle operation, equipment depreciation "
                        "or rental, maintenance, consumables, and field safety "
                        "costs without repeating direct material charges."
                    ),
                ),
                (
                    "Administrative operating costs",
                    "−$135,000 administrative costs; 9%",
                    -135000,
                    (
                        "Allocate facilities, insurance, dispatch software, "
                        "estimating subscriptions, bookkeeping, marketing, and "
                        "collection losses. Payroll, field, and administrative "
                        "costs total $42,500 monthly, excluding variable direct costs."
                    ),
                ),
                (
                    "Annual owner net profit",
                    "$195,000 closing total; 13.0%",
                    195000,
                    (
                        "Subtract all four cost groups from gross revenue: "
                        "$1,500,000 − $795,000 − $270,000 − $105,000 − "
                        "$135,000 = $195,000. This is profit, not available "
                        "cash before receivable collection."
                    ),
                ),
            ],
        ),
        (
            "diag-04-subniche-contribution-yields",
            "horizontal_bars",
            "Compare Job Contribution Before Fixed Operating Costs",
            "Five illustrative service and payment-path combinations.",
            2,
            "illustrative_model",
            (
                "Numeric values are hypothetical contribution percentages: "
                "billings less job-variable costs, divided by billings. They "
                "are not observed market averages, net margins, or an annual "
                "service mix; do not add the percentages."
            ),
            (
                "Use actual job-cost records to replace these planning inputs. "
                "The canonical Base-Case net margin remains 13.0% after all costs."
            ),
            [
                (
                    "Clean-water mitigation",
                    "45% illustrative job contribution",
                    45,
                    (
                        "Customer-authorized extraction and drying with itemized "
                        "equipment days; customer payment or insurer remittance "
                        "must be reconciled to the same contract balance."
                    ),
                ),
                (
                    "Fire and smoke cleaning",
                    "40% illustrative job contribution",
                    40,
                    (
                        "Document affected surfaces, cleaning methods, and "
                        "contents handling; disputed cleaning scope can delay "
                        "collection despite completed field labor."
                    ),
                ),
                (
                    "Mold remediation",
                    "38% illustrative job contribution",
                    38,
                    (
                        "Use required remediation credentials and project "
                        "protocols; customer-funded work remains collectible "
                        "under its contract even when coverage is excluded."
                    ),
                ),
                (
                    "Storm stabilization",
                    "35% illustrative job contribution",
                    35,
                    (
                        "Separate emergency protection from permanent repair; "
                        "weather exposure, access equipment, and crew travel "
                        "can erode initially attractive invoice yields."
                    ),
                ),
                (
                    "Reconstruction",
                    "28% illustrative job contribution",
                    28,
                    (
                        "Align progress invoices with completed milestones; "
                        "mortgage-servicer endorsements, retainage, and trade "
                        "rework can extend the cash conversion cycle."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-checks",
            "decision_tree",
            "Four Checks Before Dispatch or Scope Expansion",
            "Proceed only through applicable, documented operating requirements.",
            5,
            "operating_framework",
            (
                "Numbers identify sequential decisions rather than risk scores. "
                "A failed check routes to the corrective action in its detail. "
                "Texas citations are jurisdiction-specific examples, not "
                "nationwide contractor rules."
            ),
            (
                "Coverage uncertainty does not authorize contractor claim "
                "negotiation, deductible concessions, or unsafe mobilization."
            ),
            [
                (
                    "Credentials match the work?",
                    "Yes: continue; no: reassign scope",
                    1,
                    (
                        "Verify local contractor requirements and applicable "
                        "remediation licensing, including Texas Occupations "
                        "Code Chapter 1958 where relevant. If credentials are "
                        "missing, exclude the work or use a properly qualified "
                        "provider under a permitted contracting arrangement."
                    ),
                ),
                (
                    "Activity stays within contractor scope?",
                    "Yes: continue; no: redirect request",
                    2,
                    (
                        "Under Texas Insurance Code sections 4102.051 and "
                        "4102.163, assess licensing and contractor restrictions "
                        "before any adjusting activity. Explain construction "
                        "quantities and prices; redirect coverage advocacy "
                        "or settlement negotiation to an authorized professional."
                    ),
                ),
                (
                    "Payment terms preserve required deductibles?",
                    "Yes: continue; no: correct terms",
                    3,
                    (
                        "Review Texas Business and Commerce Code section 27.02 "
                        "where applicable. Reject prohibited deductible waivers, "
                        "disguised rebates, and inflated invoices; document the "
                        "customer's actual payment obligations and collection path."
                    ),
                ),
                (
                    "Hazards and cash exposure controlled?",
                    "Yes: dispatch; no: resolve deficiencies",
                    4,
                    (
                        "Apply 29 CFR 1910.134 when respiratory protection is "
                        "required, 29 CFR 1926.1101 for covered asbestos work, "
                        "and 40 CFR 745.85 for covered renovations. Assign "
                        "qualified crews, protective measures, and funded "
                        "job commitments before releasing affected work."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-core-six-scaled-pod",
            "org_architecture",
            "Four Core Seats, Six at Scale",
            "2 FT + 2 C core pod; add 1 FT + 1 C for a 3 FT + 3 C scaled pod.",
            11,
            "operating_framework",
            (
                "Numeric values show core-seat occupancy: four values of "
                "one and two expansion values of zero. The core comprises "
                "2 FT + 2 C; activating both expansion seats produces "
                "3 FT + 3 C, six people total. Contractor seats represent "
                "individual capacity commitments, not guaranteed full-time "
                "employee equivalents. External vendor and trade sub-crews "
                "are direct subcontractor/COGS pass-through, not internal "
                "pod headcount."
            ),
            (
                "Conservative and Base scenarios use the four-person core; "
                "the Scaled scenario uses all six seats. Consolidate operating "
                "responsibilities within the core before expansion, and verify "
                "worker classification from actual working arrangements."
            ),
            [
                (
                    "FT 1: Owner-manager and estimator",
                    "Core employee seat; commercial and scope accountability",
                    1,
                    (
                        "Own pricing, cash forecasting, jurisdiction selection, "
                        "Xactimate estimates, measured quantities, and supplement "
                        "support. Escalate contractual disputes appropriately "
                        "without negotiating policy coverage or claim settlement."
                    ),
                ),
                (
                    "FT 2: Project and mitigation lead",
                    "Core employee seat; field delivery, safety, and quality",
                    1,
                    (
                        "Coordinate dispatch and trades, direct extraction and "
                        "drying, verify psychrometric records and hazard controls, "
                        "review job costs, and confirm completion before billing. "
                        "Maintain required qualifications for assigned work."
                    ),
                ),
                (
                    "C 1: Mitigation technician",
                    "Core contractor seat; extraction and monitoring capacity",
                    1,
                    (
                        "Perform agreed extraction, equipment handling, moisture "
                        "monitoring, and containment tasks within documented "
                        "qualifications and the project's hazard-control plan. "
                        "Record equipment checks and removal evidence."
                    ),
                ),
                (
                    "C 2: Dispatch and receivables coordinator",
                    "Core contractor seat; scheduling and billing support",
                    1,
                    (
                        "Coordinate arrivals, maintain authorization records, "
                        "prepare invoices, track aging, and reconcile cleared "
                        "payments under the agreed service scope. The owner-manager "
                        "retains commercial accountability and approval authority."
                    ),
                ),
                (
                    "FT 3: Safety and quality lead",
                    "Expansion employee seat; core occupancy zero",
                    0,
                    (
                        "Activate at scale to audit hazard controls, training, "
                        "field records, and rework. The project and mitigation "
                        "lead retains these responsibilities before this hire."
                    ),
                ),
                (
                    "C 3: Reconstruction coordinator",
                    "Expansion contractor seat; core occupancy zero",
                    0,
                    (
                        "Activate at scale to coordinate qualified trade vendors, "
                        "approved repair scopes, moisture acceptance criteria, "
                        "and completion records. External trade sub-crews remain "
                        "direct subcontractor/COGS pass-through, not pod seats."
                    ),
                ),
            ],
        ),
        (
            "diag-07-45000-reference-startup-capital",
            "stacked_comparison",
            "Startup Capital: A $45,000 Reference Plan",
            "Four buckets total $45,000 within the $18,000–$75,000 USD range.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $45,000 central/reference startup "
                "allocation in USD. Details also provide complete $18,000 lean "
                "and $75,000 expanded allocations across the same four buckets. "
                "Startup capital is funding capacity, not revenue or an "
                "immediate operating expense. Choose equipment access and "
                "job commitments to fit available funding."
            ),
            (
                "Lean: $7,000 + $5,000 + $2,000 + $4,000 = $18,000. "
                "Reference: $18,000 + $12,000 + $6,000 + $9,000 = $45,000. "
                "Expanded: $30,000 + $20,000 + $10,000 + $15,000 = $75,000."
            ),
            [
                (
                    "Working-capital reserve",
                    "$18,000 reference allocation; 40.0%",
                    18000,
                    (
                        "Lean $7,000; reference $18,000; expanded $30,000. "
                        "Fund receivable delays and job commitments. Model "
                        "cash needs against the $4,000–$20,000 monthly operating "
                        "expense planning range and separately fund variable "
                        "direct job costs; a reserve does not guarantee runway "
                        "through the 1–5 month time-to-first-deal window."
                    ),
                ),
                (
                    "Mitigation equipment",
                    "$12,000 reference allocation; 26.7%",
                    12000,
                    (
                        "Lean $5,000; reference $12,000; expanded $20,000. "
                        "Prioritize extraction, air movement, dehumidification, "
                        "moisture meters, protective equipment, and calibrated "
                        "measurement tools. Use rental access or suitable used "
                        "equipment where needed and rent overflow capacity."
                    ),
                ),
                (
                    "Vehicle and mobilization setup",
                    "$6,000 reference allocation; 13.3%",
                    6000,
                    (
                        "Lean $2,000; reference $6,000; expanded $10,000. "
                        "Fund vehicle rental or lease deposits, secure storage, "
                        "load restraint, and initial mobilization equipment. "
                        "Lean deployment assumes access to a suitable existing "
                        "or rented vehicle; ongoing costs remain operating expenses."
                    ),
                ),
                (
                    "Business and technical setup",
                    "$9,000 reference allocation; 20.0%",
                    9000,
                    (
                        "Lean $4,000; reference $9,000; expanded $15,000. "
                        "Fund licensing, training, insurance deposits, estimating "
                        "setup, dispatch configuration, bookkeeping systems, "
                        "and initial referral development. Limit launch scope "
                        "to work supported by funded credentials and safeguards."
                    ),
                ),
            ],
        ),
        (
            "diag-08-first-thirty-days",
            "timeline_roadmap",
            "Thirty Days to an Operationally Ready Restoration Pod",
            "Four weekly milestones establish evidence, capacity, and cash controls.",
            12,
            "operating_framework",
            (
                "Numeric values are milestone end days. The canonical time "
                "to first deal is 1–5 months; this sprint establishes readiness "
                "and does not assume a paid job within thirty days. Monthly "
                "operating costs span $4,000–$20,000 depending on deployment."
            ),
            (
                "Use simulated job files until authorized customer work is "
                "available; never fabricate loss evidence, invoices, or insurer responses."
            ),
            [
                (
                    "Days 1-7",
                    "Jurisdiction, scope, and cash plan",
                    7,
                    (
                        "Map contractor and remediation credentials, define "
                        "public-adjusting boundaries, select the startup budget, "
                        "and build a thirteen-week cash forecast separating "
                        "operating costs from direct job commitments."
                    ),
                ),
                (
                    "Days 8-14",
                    "Pod, equipment, and safety readiness",
                    14,
                    (
                        "Assign two employee and two contractor core roles, "
                        "verify qualifications and worker classification, secure "
                        "equipment access, and document hazard assessment, "
                        "respiratory protection, and emergency escalation procedures."
                    ),
                ),
                (
                    "Days 15-21",
                    "Evidence and billing rehearsal",
                    21,
                    (
                        "Run a simulated water-loss file through dispatch, "
                        "photo capture, psychrometric readings, Xactimate scope, "
                        "customer authorization, job-cost coding, and invoice "
                        "reconciliation; resolve missing evidence before live use."
                    ),
                ),
                (
                    "Days 22-30",
                    "Referral activation and measured deployment",
                    30,
                    (
                        "Contact targeted property managers and referral "
                        "partners, track the inquiry cohort, and accept only "
                        "authorized work within capacity. Review weekly cash "
                        "exposure, receivable aging, safety events, and job contribution."
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
