from __future__ import annotations

VOLUME_046_SUBTITLE = (
    "The Complete Playbook for Mass-Tort Intake, HITECH Record Triage "
    "& Law-Firm MSOs: $160,000-$1,250,000 USD in Annual Contracted Revenue; "
    "Launch with a 1 FT + 3 C Pod (4 People), Scale to 6"
)

VOLUME_046_POSITIONING_ALTERNATIVES = [
    {
        "title": "The Fixed-Fee Mass-Tort MSO",
        "subtitle": (
            "Build a four-person intake and administration pod around "
            "documented service costs, independent counsel, and collected invoices."
        ),
        "audience": (
            "Experienced legal-operations managers serving plaintiff firms through "
            "fair-market fixed or cost-plus administrative service agreements."
        ),
        "research_basis": (
            "47 U.S.C. 227 and 47 CFR 64.1200 establish relevant telephone "
            "marketing requirements. State-adopted professional-conduct rules, "
            "including restrictions corresponding to ABA Model Rule 5.4, determine "
            "permitted MSO structures. The ABA model text is not itself a "
            "nationwide statute. Price administrative services independently of "
            "retainer signatures, legal fees, settlement awards, or litigation outcomes."
        ),
        "sources": [
            "https://www.law.cornell.edu/uscode/text/47/227",
            "https://www.ecfr.gov/current/title-47/section-64.1200",
            "https://www.azcourts.gov/abs",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Evidence-Ready Record Desk",
        "subtitle": (
            "Turn authorized EMR and pharmacy requests into source-linked "
            "exposure chronologies, with clinical exceptions routed to qualified staff."
        ),
        "audience": (
            "Medical-record operations specialists supporting mass-tort counsel "
            "with auditable retrieval, chronology preparation, and deficiency repair."
        ),
        "research_basis": (
            "45 CFR 164.524 governs individual access to protected health "
            "information, while 45 CFR 164.508 supplies authorization requirements "
            "for disclosures requiring authorization. The HHS Ciox notice limits "
            "how third-party directions and patient-rate fees may be characterized. "
            "45 CFR 164.504(e) governs business-associate contracts where that "
            "relationship actually exists; a law-firm vendor is not automatically "
            "a business associate merely because it handles medical records."
        ),
        "sources": [
            "https://www.ecfr.gov/current/title-45/section-164.524",
            "https://www.ecfr.gov/current/title-45/section-164.508",
            "https://www.ecfr.gov/current/title-45/section-164.504",
            "https://www.hhs.gov/hipaa/court-order-right-of-access/index.html",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
    {
        "title": "The Causation-Aware Intake Platform",
        "subtitle": (
            "Separate claimant identity, usable proof, counsel acceptance, "
            "and vendor collections before expanding campaign exposure."
        ),
        "audience": (
            "Plaintiff-firm operations leaders and separately licensed Arizona "
            "ABS operators building disciplined claimant acquisition infrastructure."
        ),
        "research_basis": (
            "Federal Rule of Evidence 702 makes expert reliability central to "
            "litigation risk; intake acceptance does not resolve general causation. "
            "Arizona's court-administered ABS licensing framework is a distinct "
            "ownership pathway, not a blanket exception available to an ordinary "
            "MSO or to operations in every jurisdiction."
        ),
        "sources": [
            "https://www.law.cornell.edu/rules/fre/rule_702",
            "https://www.law.cornell.edu/uscode/text/28/1407",
            "https://www.azcourts.gov/abs",
        ],
        "validation_status": (
            "Source-informed editorial positioning; not market-tested."
        ),
    },
]


def build_volume_046_diagrams_data() -> list[dict]:
    specs = [
        (
            "diag-01-intake-to-collected-service-fee",
            "process_flow",
            "Five Handoffs from Inquiry to Collected MSO Fee",
            "Evidence quality controls delivery; service contracts control compensation.",
            1,
            "operating_framework",
            (
                "Counsel owns representation decisions and legal advice. The MSO "
                "performs contracted administrative work at fair-market fixed or "
                "cost-plus rates. Case milestones measure operations, not a "
                "percentage interest in legal fees or settlement proceeds."
            ),
            (
                "Maintain separate claimant, evidence, service-delivery, and "
                "invoice ledgers. A signed retainer is neither usable medical "
                "proof nor recognized MSO revenue."
            ),
            [
                (
                    "Raw inquiry",
                    "Capture provenance and contact permission before routing",
                    1.0,
                    (
                        "Capture source URL, campaign identifier, timestamp, "
                        "seller-specific contact language, and TrustedForm certificate "
                        "when available. Use authorized LexisNexis identity checks "
                        "and restricted identity tokens; a certificate alone proves "
                        "neither claimant identity nor complete contact eligibility."
                    ),
                ),
                (
                    "Signed law-firm retainer",
                    "Counsel accepts representation after duplicate-retainer screening",
                    2.0,
                    (
                        "Route conflict questions, existing representation, and "
                        "retainer execution to the law firm. Scrub duplicates "
                        "against authorized firm records and claimant attestations; "
                        "do not imply access to a universal retainer registry."
                    ),
                ),
                (
                    "Usable EMR and pharmacy proof",
                    "Retrieve records through the applicable documented access route",
                    3.0,
                    (
                        "Validate patient identity, recipient, scope, and authority "
                        "under 45 CFR 164.524 or 164.508 as applicable. Preserve "
                        "source pages, pharmacy identifiers, service dates, and "
                        "request receipts; log missing exposure or diagnosis evidence."
                    ),
                ),
                (
                    "Deficiency-free accepted case",
                    "Counsel confirms completeness against the current evidence matrix",
                    4.0,
                    (
                        "An LLM may draft ICD-10 and exposure chronologies, but "
                        "trained reviewers verify every material assertion against "
                        "the record. Counsel determines legal sufficiency; a "
                        "qualified clinician resolves clinical interpretation questions."
                    ),
                ),
                (
                    "Collected MSO vendor fee",
                    "Match contracted service delivery to invoice and cleared payment",
                    5.0,
                    (
                        "Bill the law firm's operating account for administrative "
                        "services, not client trust funds. Track ACH settlement, "
                        "service credits, and replacement-window obligations "
                        "separately from legal recoveries and claimant cohort counts."
                    ),
                ),
            ],
        ),
        (
            "diag-02-nested-claimant-quality-cohorts",
            "funnel",
            "The Conversion Waterfall That Exposes Acquisition Leakage",
            "A single illustrative annual cohort, with no entrants added between stages.",
            6,
            "illustrative_model",
            (
                "Illustrative mature-cohort counts are 1,200, 480, 336, 252, and "
                "210. Each stage is a strict subset of its predecessor. The final "
                "count identifies files associated with paid service invoices; "
                "it is not a count of per-case commissions or settlements."
            ),
            (
                "Conversions are 40.0%, 70.0%, 75.0%, and 83.33% sequentially; "
                "17.5% of raw inquiries reach the final cohort. Annual Base "
                "revenue remains $705,000 from contracted services, not 210 "
                "multiplied by a claimant bounty."
            ),
            [
                (
                    "Raw inquiry cohort",
                    "1,200 inquiries enter the same annual measurement cohort",
                    1200.0,
                    (
                        "Illustratively remove 180 duplicate or synthetic inquiries "
                        "and 540 additional inquiries lacking eligibility, contact, "
                        "or counsel acceptance before retainer completion. Retain "
                        "mutually exclusive disposition codes so losses reconcile."
                    ),
                ),
                (
                    "Signed retainer cohort",
                    "480 retained claimants represent 40.0% of raw inquiries",
                    480.0,
                    (
                        "Counsel signs only after representation checks. At a "
                        "fixed 540 other exclusions, increasing duplicate or "
                        "synthetic losses from 180 to 240 reduces retained "
                        "claimants to 420 before downstream attrition."
                    ),
                ),
                (
                    "Usable proof cohort",
                    "336 usable record packets represent 70.0% of retainers",
                    336.0,
                    (
                        "Reject 144 packets for absent exposure, incompatible "
                        "dates, missing diagnosis support, or unusable records. "
                        "The Base retrieval and triage pool is $66,000, equal "
                        "to $137.50 per retained claimant or $196.43 per usable "
                        "packet. At 60.0% usability, 288 packets cost $229.17 each."
                    ),
                ),
                (
                    "Accepted case cohort",
                    "252 accepted files represent 75.0% of usable packets",
                    252.0,
                    (
                        "Remove 84 files with unresolved firm-defined deficiencies. "
                        "Define a 30-day contractual service-defect replacement "
                        "window and charge actual rework to its responsible cost "
                        "pool. If acceptance falls to 60.0%, expect about 202 files; "
                        "do not represent rounding as an additional claimant."
                    ),
                ),
                (
                    "Collected service cohort",
                    "210 files associate with cleared vendor service invoices",
                    210.0,
                    (
                        "The remaining 42 accepted files associate with invoices "
                        "still unpaid at the cohort cutoff. Cash status does not "
                        "reverse properly recognized revenue automatically. Model "
                        "a 60-day delay on one $58,750 monthly service invoice as "
                        "a $58,750 working-capital exposure, not lost settlement value."
                    ),
                ),
            ],
        ),
        (
            "diag-03-base-case-owner-profit-bridge",
            "waterfall",
            "Base Case: $705,000 Revenue to $267,900 Owner Profit",
            "Six bars reconcile annual service revenue, four cost pools, and the ending total.",
            3,
            "illustrative_model",
            (
                "Canonical Formula v2.0 totals are fixed; the four expense pools "
                "are an illustrative allocation of $437,100. The first and last "
                "bars are totals; the four interior values are signed changes. "
                "Revenue excludes client trust balances, settlements, and "
                "pass-through amounts for which the MSO is an agent."
            ),
            (
                "$705,000 - $180,000 - $144,000 - $66,000 - $47,100 = $267,900; "
                "$267,900 / $705,000 = 38.0%. Conservative: $160,000 revenue, "
                "$118,400 costs, $41,600 profit at 26%. Scaled: $1,250,000 "
                "revenue, $625,000 costs, $625,000 profit at 50%."
            ),
            [
                (
                    "Recognized service revenue",
                    "$705,000 annual contracted administrative service revenue",
                    705000.0,
                    (
                        "Equivalent to twelve $58,750 monthly service invoices "
                        "earned through contracted delivery. Apply ASC 606 "
                        "principal-versus-agent analysis to reimbursed media and "
                        "retrieval charges; no separate retained-share factor is "
                        "supplied or invented for this canonical revenue total."
                    ),
                ),
                (
                    "Acquisition delivery expense",
                    "Subtract $180,000 for owned campaign delivery costs",
                    -180000.0,
                    (
                        "Allocate $15,000 monthly to media and attributable "
                        "campaign production where the MSO bears those costs. "
                        "Audit source quality and vendor credits. Direct "
                        "law-firm media spend is outside this MSO expense pool."
                    ),
                ),
                (
                    "Pod delivery labor",
                    "Subtract $144,000 for contracted and employed delivery capacity",
                    -144000.0,
                    (
                        "Illustrative annual pool: $60,000 employed operations "
                        "seat, $30,000 intake contractor, $30,000 record contractor, "
                        "and $24,000 chronology contractor. Treat amounts as loaded "
                        "planning allowances; contractor seats represent scheduled "
                        "capacity, not three additional full-time employees."
                    ),
                ),
                (
                    "Record and triage outlays",
                    "Subtract $66,000 for retrieval and evidence-processing expenses",
                    -66000.0,
                    (
                        "Illustratively allocate $36,000 to provider and pharmacy "
                        "retrieval, $18,000 to secure parsing and processing, "
                        "and $12,000 to external exception work. Keep pod labor "
                        "outside this pool to prevent double counting."
                    ),
                ),
                (
                    "Core overhead expense",
                    "Subtract $47,100 for recurring non-delivery operating support",
                    -47100.0,
                    (
                        "Budget $3,925 monthly for secure systems, insurance, "
                        "bookkeeping, contract maintenance, and general administration. "
                        "The supplied $2,500-$14,000 monthly opex range is treated "
                        "here as core recurring overhead, not total modeled costs "
                        "of $36,425 monthly."
                    ),
                ),
                (
                    "Annual owner profit",
                    "$267,900 ending profit equals a 38.0% net margin",
                    267900.0,
                    (
                        "This is the canonical modeled owner-profit measure "
                        "after the four expense pools, not a settlement share. "
                        "Tax treatment, owner distributions, and cash timing "
                        "remain separate schedules; do not count collections "
                        "again after recognizing earned service revenue."
                    ),
                ),
            ],
        ),
        (
            "diag-04-service-rail-contribution-yield",
            "horizontal_bars",
            "Compare Service Yield Without Pricing Claimant Outcomes",
            "Illustrative contribution dollars per delivered hour, before shared overhead.",
            2,
            "illustrative_model",
            (
                "Hourly equivalents normalize fixed or cost-plus service packages; "
                "they are neither market quotations nor payments for retaining "
                "a claimant. Each numeric value equals allocated service revenue "
                "less direct delivery cost per hour. These unit examples do "
                "not independently rebuild the canonical annual scorecard."
            ),
            (
                "Choose rails by administrative scope, documented cost, and "
                "collection reliability. Larger contribution per hour does not "
                "establish better evidence quality or permit legal fee-sharing."
            ),
            [
                (
                    "Exposure chronology package",
                    "$60 contribution per hour through fixed-scope ACH invoices",
                    60.0,
                    (
                        "Allocate $150 service revenue and $90 direct cost per "
                        "delivered hour for source-linked exposure chronologies. "
                        "Version the counsel-supplied evidence matrix and reserve "
                        "clinical interpretation for qualified personnel."
                    ),
                ),
                (
                    "Pharmacy proof coordination",
                    "$55 contribution per hour through cost-plus ACH invoices",
                    55.0,
                    (
                        "Allocate $130 service revenue and $75 direct cost per "
                        "hour coordinating dispensing records and product identifiers. "
                        "Disclose retrieval charges and price service effort "
                        "without asserting a universal third-party patient-rate cap."
                    ),
                ),
                (
                    "Medical device record desk",
                    "$50 contribution per hour through fixed-scope operating-account payments",
                    50.0,
                    (
                        "Allocate $125 service revenue and $75 direct cost per "
                        "hour locating implant records, operative reports, and "
                        "device identifiers. Missing lot numbers trigger a "
                        "documented deficiency task rather than an invented match."
                    ),
                ),
                (
                    "Retainer deficiency support",
                    "$45 contribution per hour through monthly administrative retainers",
                    45.0,
                    (
                        "Allocate $110 service revenue and $65 direct cost per "
                        "hour resolving incomplete signatures and missing intake "
                        "fields. Counsel handles conflicts and representation; "
                        "administrative compensation does not depend on signing."
                    ),
                ),
                (
                    "Paid-media administration",
                    "$40 contribution per hour through fixed management invoices",
                    40.0,
                    (
                        "Allocate $100 service revenue and $60 direct cost per "
                        "hour to campaign administration and source auditing. "
                        "Exclude direct client advertising spend from these unit "
                        "figures and do not buy a share of recoveries."
                    ),
                ),
            ],
        ),
        (
            "diag-05-preflight-statutory-risk-routing",
            "decision_tree",
            "Four Pre-Flight Checks Before Contact or Record Processing",
            "Each failed check routes to a named correction, not automatic case rejection.",
            5,
            "operating_framework",
            (
                "This is an ordered pass-or-repair decision chain. Apply the "
                "rules of the operating jurisdiction, communication method, "
                "record holder, and actual entity structure. A vendor certificate "
                "or an Arizona affiliation does not replace that analysis."
            ),
            (
                "Proceed only through the permitted service path: independent "
                "counsel, documented contact authority, valid record access, "
                "and verified identity and evidence provenance."
            ),
            [
                (
                    "Entity and compensation",
                    "Pass fixed or cost-plus scope; otherwise repair the agreement",
                    1.0,
                    (
                        "Check state-adopted Rule 5.4 restrictions, unauthorized "
                        "practice rules, and attorney-advertising or runner statutes, "
                        "including California Business and Professions Code "
                        "sections 6151-6152 where applicable. An Arizona ABS "
                        "requires actual court licensing and scope verification; "
                        "do not extend its permissions across unrelated jurisdictions."
                    ),
                ),
                (
                    "Contact authority",
                    "Pass documented channel authority; otherwise suppress the contact",
                    2.0,
                    (
                        "Apply 47 U.S.C. 227, 47 CFR 64.1200, applicable state "
                        "calling rules, revocations, and do-not-call requirements. "
                        "Use one-to-one seller-specific consent as an operating "
                        "standard where consent is required; the FCC's 2023 "
                        "one-to-one amendment was vacated in 2025 and is not "
                        "a universal federal mandate."
                    ),
                ),
                (
                    "Record access and security",
                    "Pass route-specific authority; otherwise correct scope and recipient",
                    3.0,
                    (
                        "Distinguish individual access under 45 CFR 164.524 "
                        "from authorization under 164.508 and applicable "
                        "42 CFR Part 2 restrictions. Account for the Ciox "
                        "limits on third-party directions and fees. Track the "
                        "access rule's 30-day response period and permitted "
                        "written extension; assess business-associate duties "
                        "under 164.504(e) from the actual relationship."
                    ),
                ),
                (
                    "Identity and causation exposure",
                    "Pass verified provenance; otherwise quarantine the affected work",
                    4.0,
                    (
                        "Check duplicate identity tokens, existing representation, "
                        "source-page integrity, and inconsistent exposure dates. "
                        "Counsel tracks MDL orders under 28 U.S.C. 1407 and "
                        "expert-admissibility exposure under Federal Rule of "
                        "Evidence 702. A general-causation dismissal can strand "
                        "campaign spending even when intake files are complete."
                    ),
                ),
            ],
        ),
        (
            "diag-06-four-to-six-person-pod",
            "org_architecture",
            "Four Core Seats, Two Deliberate Scale Additions",
            "Base and Conservative use 1 FT + 3 C; Scaled uses 2 FT + 4 C.",
            11,
            "operating_framework",
            (
                "FT means full-time employee; C means contractor seat with "
                "explicit scheduled capacity. Numeric values show headcount "
                "presence: one for each core seat and zero for each scale-only "
                "seat at Base. The last two stages each add one person at "
                "Scaled. Client counsel and external advisers are outside this pod."
            ),
            (
                "Base staffing is four people, not four full-time equivalents. "
                "Add one employee and one contractor only when sustained "
                "queues, service budgets, and signed contracts support them."
            ),
            [
                (
                    "Operations lead",
                    "Core full-time seat owns service scope and invoice reconciliation",
                    1.0,
                    (
                        "Own the service ledger, vendor economics, access "
                        "permissions, and daily exception queue. Escalate legal "
                        "decisions to client counsel. Use the Base $60,000 "
                        "loaded labor allowance without counting owner profit "
                        "as a second operating expense."
                    ),
                ),
                (
                    "Intake specialist",
                    "Core contractor seat verifies provenance and administrative completeness",
                    1.0,
                    (
                        "Maintain contact evidence, identity discrepancies, and "
                        "duplicate-retainer flags within the $30,000 Base allowance. "
                        "Do not provide legal advice or independently decide "
                        "whether the law firm should represent a claimant."
                    ),
                ),
                (
                    "Record retrieval coordinator",
                    "Core contractor seat manages authorizations and provider follow-up",
                    1.0,
                    (
                        "Use the $30,000 Base allowance to manage request "
                        "receipts, scope defects, delivery channels, and provider "
                        "invoices. Maintain route-specific timers; never assume "
                        "every provider request shares the individual-access deadline."
                    ),
                ),
                (
                    "Chronology quality specialist",
                    "Core contractor seat validates extracted facts against source pages",
                    1.0,
                    (
                        "Use the $24,000 Base allowance for chronology verification "
                        "and structured deficiency tickets. Restrict LLM access "
                        "to approved environments; if clinical interpretation is "
                        "required, assign appropriately qualified personnel."
                    ),
                ),
                (
                    "Delivery manager",
                    "Scaled addition creates the second full-time employee seat",
                    0.0,
                    (
                        "Add when sustained record and invoice queues exceed "
                        "the measured capacity of the four-person pod. Separate "
                        "daily workload assignment from the lead's contract "
                        "ownership, and budget within the Scaled $625,000 total "
                        "expense envelope."
                    ),
                ),
                (
                    "Evidence exception specialist",
                    "Scaled addition creates the fourth contractor seat",
                    0.0,
                    (
                        "Add targeted capacity for complex pharmacy histories, "
                        "missing implant records, and replacement-window rework. "
                        "The resulting six-person pod is 2 FT + 4 C; "
                        "do not carry Base labor allocations forward unchanged."
                    ),
                ),
            ],
        ),
        (
            "diag-07-startup-capital-allocation",
            "stacked_comparison",
            "Allocate Startup Capital Before Expanding Acquisition",
            "Four buckets total $12,000 lean, $30,000 planning, or $50,000 expanded.",
            4,
            "illustrative_model",
            (
                "Numeric values encode the $30,000 planning stack. Each stage "
                "also supplies its lean and expanded allocations. The endpoints "
                "are startup funding envelopes, not annual operating expenses, "
                "revenue forecasts, or a substitute for receivables funding."
            ),
            (
                "Lean: $3,000 + $2,500 + $2,500 + $4,000 = $12,000. "
                "Planning: $9,000 + $7,500 + $6,000 + $7,500 = $30,000. "
                "Expanded: $15,000 + $12,000 + $10,000 + $13,000 = $50,000."
            ),
            [
                (
                    "Contract and operating design",
                    "$9,000 planning allocation; $3,000 lean and $15,000 expanded",
                    9000.0,
                    (
                        "Fund jurisdiction-specific service agreements, compensation "
                        "structure assessment, record-access forms, insurance "
                        "setup, and initial vendor diligence. Arizona ABS "
                        "licensing is a separate scoped undertaking, not an "
                        "assumed deliverable inside this allocation."
                    ),
                ),
                (
                    "Secure intake and record stack",
                    "$7,500 planning allocation; $2,500 lean and $12,000 expanded",
                    7500.0,
                    (
                        "Configure restricted CRM roles, MFA, encrypted storage, "
                        "audit exports, TrustedForm capture, and approved "
                        "identity-verification integrations. Confirm contractual "
                        "data handling before connecting an LLM to live records."
                    ),
                ),
                (
                    "Controlled acquisition pilot",
                    "$6,000 planning allocation; $2,500 lean and $10,000 expanded",
                    6000.0,
                    (
                        "Purchase a bounded campaign sample with daily spend "
                        "limits and source-level loss reporting. Require documented "
                        "contact authority, vendor credit terms, and counsel's "
                        "current case criteria before increasing campaign exposure."
                    ),
                ),
                (
                    "Retrieval and cash reserve",
                    "$7,500 planning allocation; $4,000 lean and $13,000 expanded",
                    7500.0,
                    (
                        "Reserve cash for initial provider charges, contractor "
                        "timing, and disputed service credits. Even the expanded "
                        "$13,000 bucket cannot absorb a delayed $58,750 Base "
                        "monthly invoice; arrange staged billing or additional "
                        "working capital before committing that delivery volume."
                    ),
                ),
            ],
        ),
        (
            "diag-08-thirty-day-launch-sprint",
            "timeline_roadmap",
            "Thirty Days to a Measured, Contract-Ready Delivery System",
            "Build the operating evidence before treating acquisition volume as progress.",
            12,
            "operating_framework",
            (
                "The canonical time to first deal is 1-4 months. This sprint "
                "establishes readiness and pilot evidence; it does not assume "
                "a signed customer, completed provider response, or collected "
                "revenue within thirty days."
            ),
            (
                "Exit with traceable permissions, a reconciled sample cohort, "
                "a costed service scope, and explicit working-capital needs. "
                "Expand only against measured capacity and authorized live work."
            ),
            [
                (
                    "Days 1-7",
                    "Select one service niche and document the permitted contract structure",
                    7.0,
                    (
                        "Choose one counsel-defined exposure and evidence matrix. "
                        "Draft fixed or cost-plus scope, jurisdictional rules "
                        "mapping, defect definitions, and a 30-day contractual "
                        "replacement window. Record the $705,000 Base revenue "
                        "and $437,100 expense targets as annual planning figures."
                    ),
                ),
                (
                    "Days 8-14",
                    "Configure provenance capture and test record-handling boundaries",
                    14.0,
                    (
                        "Test synthetic intake records through CRM permissions, "
                        "contact suppression, duplicate checks, and invoice mapping. "
                        "Verify authorization templates and approved storage. "
                        "Demonstrate source-page citations and a manual exception "
                        "route before allowing live record parsing."
                    ),
                ),
                (
                    "Days 15-21",
                    "Run a bounded authorized pilot and measure retrieval loss",
                    21.0,
                    (
                        "After customer authorization, launch only the budgeted "
                        "sample and log every cohort transition. Record provider "
                        "outlays even when proof fails. If no customer has "
                        "signed, continue synthetic workflow testing and prospect "
                        "discussions rather than processing live claimant records."
                    ),
                ),
                (
                    "Days 22-30",
                    "Reconcile service economics and publish the next operating decision",
                    30.0,
                    (
                        "Calculate duplicate loss, usable-proof yield, deficiency "
                        "repair cost, and invoice aging. Keep pending provider "
                        "requests out of completed-proof counts. Reconcile the "
                        "six-bar Base bridge, stress one delayed monthly invoice, "
                        "and set the next month's spend from signed scope and cash."
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
