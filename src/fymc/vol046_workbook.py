from __future__ import annotations


def build_volume_046_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-046-mass-tort-intake-hitech-triage-and-law-firm-msos",
        "volume_id": "vol-046-mass-tort-intake-hitech-triage-and-law-firm-msos",
        "title": "Mass-Tort Case Acquisition, HITECH Record Triage & Law-Firm MSOs — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Fixed-Fee MSO Underwriting, "
            "Claimant-to-Collection Economics, HITECH Record Evidence, Law-Firm "
            "Contract Controls, Human-Supervised Automation, and Small-Team Launch Execution"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Underwrite the law-firm customer, acquisition supplier, and administrative "
                    "service spread before committing media or retrieval cash. Separate the "
                    "firm's legal judgment from MSO production duties, establish evidence "
                    "quality thresholds, and reject arrangements that monetize settlements "
                    "or disguise paid claimant recommendations."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Identify the contracting firm, supervising attorney, payment entity, "
                        "and every acquisition subcontractor. Verify licenses and ownership "
                        "against primary registries, then record who controls advertising, "
                        "client acceptance, legal strategy, record access, and payment authorization "
                        "before evaluating the projected spread."
                    ),
                    (
                        "Describe deliverables as administrative work with fair-market fixed "
                        "or documented cost-plus pricing. Test whether compensation changes "
                        "with retained clients, accepted cases, legal fees, or recoveries; "
                        "remove those dependencies from the ordinary nonlawyer MSO agreement "
                        "before purchasing traffic."
                    ),
                    (
                        "Build one dated inquiry cohort through signed retainers, usable "
                        "record proof, attorney acceptance, and collection of administrative "
                        "invoices. Keep duplicate exclusions and missing evidence visible "
                        "rather than improving conversion rates by silently deleting rejected "
                        "or incomplete records."
                    ),
                    (
                        "Price an adverse cohort using increased duplicates, unusable "
                        "records, slower provider responses, and customer rework demands. "
                        "Require the firm to own medical and legal eligibility criteria, "
                        "while the MSO measures production capacity, evidence provenance, "
                        "and contractual payment exposure."
                    ),
                    (
                        "Approve the opportunity only after confirming a funded customer, "
                        "a credible cash runway, and a signed scope with bounded rework. "
                        "Document reasons for rejection as carefully as acceptance so "
                        "future acquisition teams cannot revive a structurally defective arrangement."
                    ),
                ],
                "fields": [
                    field(
                        "Counterparty identity and attorney authority",
                        "textarea",
                        (
                            "Identify the firm entity, bar jurisdictions, supervising attorney, "
                            "accounts-payable contact, and administrative decision maker. Explain "
                            "how primary-source verification and delegated authority will be "
                            "documented before onboarding any acquisition supplier."
                        ),
                        (
                            "Illustrative customer Harbor Trial Group PLLC supplies its formation "
                            "record, W-9, operating address, and two attorney bar records. The "
                            "engagement partner signs the scope; accounts payable confirms a "
                            "$58,750 monthly service budget. The MSO retains dated verification "
                            "evidence and repeats license checks quarterly."
                        ),
                    ),
                    field(
                        "Purchased service and fair-market pricing thesis",
                        "textarea",
                        (
                            "Define the actual administrative service being purchased, its "
                            "capacity limits, and its pricing evidence. Distinguish procurement "
                            "of advertising and support labor from selling recommendations, "
                            "representation decisions, or ownership interests in recoveries."
                        ),
                        (
                            "The firm purchases campaign administration, intake staffing, "
                            "authorized record coordination, and chronology production for "
                            "$58,750 monthly. Three comparable service proposals support the "
                            "rate. The contract promises staffing and documented tasks, not "
                            "108 accepted claims, and never changes compensation with settlement "
                            "value or attorney fee receipts."
                        ),
                    ),
                    field(
                        "Canonical opportunity classification",
                        "textarea",
                        (
                            "Record the candidate's canonical score, staffing, startup range, "
                            "and time horizon. Explain which assumptions require validation "
                            "locally rather than treating the published ranking as evidence "
                            "of counterparty quality or immediate demand."
                        ),
                        (
                            "Candidate 46 ranks 13 of 49 and scores 93/100, comprising "
                            "25 revenue, 23 margin, 19 team efficiency, 13 startup accessibility, "
                            "and 13 automation points. Budget $12,000–$50,000 startup capital "
                            "and 1–4 months to first deal; the base pod has one full-time "
                            "operator and three contractors."
                        ),
                    ),
                    field(
                        "Inquiry ownership and provenance",
                        "textarea",
                        (
                            "Specify the evidence required for every incoming inquiry, including "
                            "publisher identity, source page, notice version, collection time, "
                            "authorized recipient, and contact permission. State how rejected "
                            "provenance affects vendor payment and downstream handling."
                        ),
                        (
                            "A 1,000-inquiry monthly cohort includes publisher IDs, landing-page "
                            "versions, source timestamps, and TrustedForm certificate references. "
                            "The firm receives only records supported by its approved contact "
                            "language. Twenty inquiries lacking retrievable permission evidence "
                            "enter quarantine, remain in raw-volume reporting, and receive no "
                            "automated outbound contact."
                        ),
                    ),
                    field(
                        "Duplicate and identity-risk screen",
                        "textarea",
                        (
                            "Define exact-match and fuzzy-match signals, authorized identity "
                            "checks, escalation ownership, and evidence retention. Avoid "
                            "assuming that a certificate, identity score, or database match "
                            "proves claim validity or permits sharing another firm's confidential information."
                        ),
                        (
                            "Of 1,000 inquiries, 100 are suppressed as duplicate or unresolved "
                            "identity-risk records, leaving 900 unique candidates. Phone, date "
                            "of birth, and normalized address support internal matching. "
                            "Authorized LexisNexis checks supplement manual review; a full SSN "
                            "is neither routinely collected nor exposed in the intake dashboard."
                        ),
                    ),
                    field(
                        "Retainer and evidence conversion waterfall",
                        "textarea",
                        (
                            "Enter raw inquiries, unique candidates, signed firm retainers, "
                            "usable EMR or pharmacy proof, and deficiency-free attorney "
                            "acceptances. Show stage denominators and distinguish operational "
                            "outcomes from the contractual event that earns administrative revenue."
                        ),
                        (
                            "The planning cohort moves from 1,000 raw inquiries to 900 unique "
                            "candidates, 180 signed retainers, 126 usable evidence files, and "
                            "108 accepted cases. Stage rates are 90%, 20%, 70%, and 85.71%. "
                            "Collection means payment of the separate $58,750 service invoice, "
                            "not monetization of individual accepted claims."
                        ),
                    ),
                    field(
                        "Exposure and injury evidence definition",
                        "textarea",
                        (
                            "Ask the supervising attorney to define the dated eligibility "
                            "matrix, acceptable exposure sources, injury documentation, and "
                            "contradiction handling. Record evidence requirements without "
                            "allowing intake staff or language models to diagnose injury or promise eligibility."
                        ),
                        (
                            "The firm's matrix requires a dated dispensing history, identified "
                            "product, documented diagnosis, and counsel's timing assessment. "
                            "Of 180 retained clients, 54 lack usable proof at the cutoff. "
                            "Staff identify missing pages and contradictions; only the attorney "
                            "decides whether further investigation, another theory, or closure is appropriate."
                        ),
                    ),
                    field(
                        "Replacement window and supplier remedies",
                        "textarea",
                        (
                            "Define the difference between correcting defective administrative "
                            "work and replacing a claimant. Specify notice periods, included "
                            "labor, evidence needed for supplier credits, and limits preventing "
                            "open-ended service costs or promises about representation outcomes."
                        ),
                        (
                            "The firm has 30 days after packet delivery to report missing "
                            "index pages or transcription defects. Up to 20 corrective labor "
                            "hours are included monthly. The MSO does not replace rejected "
                            "clients or refund fees because a case fails; publisher credits "
                            "address documented duplicate or fabricated submissions only."
                        ),
                    ),
                    field(
                        "Customer credit and concentration exposure",
                        "textarea",
                        (
                            "Assess payment authority, receivable aging, customer concentration, "
                            "and the source of operating funds. Describe protections against "
                            "funding services from client trust balances or waiting for "
                            "settlements before the firm pays ordinary administrative invoices."
                        ),
                        (
                            "The first customer represents 100% of projected revenue, so the "
                            "operator obtains trade references and a $15,000 service advance "
                            "from the firm's operating account. Invoices mature in 30 days, "
                            "independent of litigation results. Client trust money is excluded; "
                            "overdue balances trigger a prospective spending pause."
                        ),
                    ),
                    field(
                        "Underwriting decision and adverse-case spread",
                        "textarea",
                        (
                            "State the proceed, renegotiate, or decline decision using measured "
                            "conversion, contractual protections, and stressed cost exposure. "
                            "Name the person who can stop spending when evidence quality, "
                            "customer liquidity, or lawful operating structure deteriorates."
                        ),
                        (
                            "Proceed with the $58,750 fixed scope only after counsel approves "
                            "advertising and payment terms. Base monthly costs are $36,425, "
                            "leaving $22,325. A $6,000 rework shock reduces contribution to "
                            "$16,325. The operator stops new media commitments if unpaid "
                            "invoices exceed $58,750 or provenance defects exceed 5%."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The operator and supervising attorney sign a dated underwriting record "
                    "with verified entities, fair-market pricing support, the complete cohort "
                    "waterfall, a funded payment plan, and explicit rejection of recovery-linked "
                    "compensation under the ordinary MSO structure."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Reconcile the three canonical annual scenarios and translate the base "
                    "case into cohort costs, invoice timing, and cash requirements. Keep "
                    "law-firm trust balances outside the model, distinguish revenue from "
                    "cash collection, and stress duplicate attrition, record rejection, "
                    "retrieval spending, and bounded rework."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Enter annual revenue, total operating cost, margin, owner net profit, "
                        "and staffing for all three canonical scenarios. Preserve exact "
                        "annual values, label monthly rounding, and do not substitute "
                        "settlement awards or client medical expenses for recognized MSO revenue."
                    ),
                    (
                        "Separate standing overhead from campaign media, record charges, "
                        "delivery labor, and allocated costs. Reconcile every base-case "
                        "dollar to the annual model so the published monthly overhead "
                        "range is not misrepresented as the complete expense burden."
                    ),
                    (
                        "Calculate stage conversion and cost per operational outcome from "
                        "one cohort. Keep those ratios as diagnostic measures rather "
                        "than contractual prices per retained client or accepted case, "
                        "and retain raw inquiries as the top-of-funnel denominator."
                    ),
                    (
                        "Model invoice recognition, payment timing, service advances, "
                        "supplier terms, and unrestricted reserves separately. Use a "
                        "daily cash calendar after the initial run-rate estimate, and "
                        "never count customer trust balances or future settlement receipts "
                        "as available working capital."
                    ),
                    (
                        "Stress each major driver independently before combining shocks. "
                        "Document which costs are already committed, which can be "
                        "reduced prospectively, and which require a signed scope amendment "
                        "so collection delays do not produce hidden reductions in service quality."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Record conservative annual revenue, operating costs, net margin, "
                            "owner net profit, and team composition. Explain the monthly "
                            "equivalent and identify whether any cash reserve movement "
                            "has incorrectly been recorded as an operating expense."
                        ),
                        (
                            "Conservative recognized service revenue is $160,000; total annual "
                            "costs are $118,400; owner net profit is $41,600 at 26%. Staffing "
                            "is one full-time operator plus three contractors. Monthly "
                            "equivalents are approximately $13,333.33 revenue, $9,866.67 costs, "
                            "and $3,466.67 profit; annual amounts control rounding."
                        ),
                    ),
                    field(
                        "Base scenario reconciliation",
                        "textarea",
                        (
                            "Enter the base annual and monthly income statement using only "
                            "contracted administrative service revenue. Identify the exact "
                            "cost ceiling needed to preserve the canonical margin and "
                            "distinguish owner net profit from additional owner withdrawals."
                        ),
                        (
                            "Base revenue is $705,000 annually, or $58,750 monthly. Annual "
                            "costs of $437,100 equal $36,425 monthly, leaving $267,900 annual "
                            "owner net profit and $22,325 monthly at 38.0%. The team remains "
                            "one full-time operator plus three contractors; owner distributions "
                            "do not become a second operating expense."
                        ),
                    ),
                    field(
                        "Scaled small-team reconciliation",
                        "textarea",
                        (
                            "Record the scaled revenue, margin, total costs, owner net "
                            "profit, and six-person staffing constraint. Explain how process "
                            "capacity and customer diversification must support the scenario "
                            "without assuming settlement participation or a larger hidden team."
                        ),
                        (
                            "Scaled service revenue is $1,250,000, annual costs are $625,000, "
                            "and annual owner net profit is $625,000 at 50%. Staffing is "
                            "two full-time people plus four contractors. Approximate monthly "
                            "revenue is $104,166.67; monthly cost and profit are each "
                            "$52,083.33, with annual totals authoritative."
                        ),
                    ),
                    field(
                        "Revenue recognition and retained-share boundary",
                        "textarea",
                        (
                            "Describe the promised service, performance period, principal "
                            "versus agent assessment, and treatment of customer advances. "
                            "Identify amounts excluded from operator revenue and explain "
                            "how gross billings would be adjusted if pass-through agency facts apply."
                        ),
                        (
                            "The illustrative base assumes the MSO controls and delivers "
                            "the contracted service, recognizing $58,750 over each service "
                            "month under ASC 606. A $15,000 advance is initially a contract "
                            "liability. Settlement awards and trust funds contribute zero; "
                            "an agency arrangement would require net presentation and explicit reconciliation."
                        ),
                    ),
                    field(
                        "Base monthly cost bridge",
                        "textarea",
                        (
                            "Allocate the complete monthly expense budget to media, record "
                            "outlays, delivery labor, systems, and remaining overhead. Explain "
                            "which costs sit inside the published standing-overhead range "
                            "and which variable costs must be added separately."
                        ),
                        (
                            "Budget $18,000 media, $4,500 record outlays, $8,000 delivery "
                            "contractors, $2,500 systems, and $3,425 allocated overhead, totaling "
                            "$36,425. Standing overhead is $5,925, within the $2,500–$14,000 "
                            "reference range. Campaign spending, retrieval, and delivery labor "
                            "explain why complete base expenses exceed that standing range."
                        ),
                    ),
                    field(
                        "Waterfall cost per operational outcome",
                        "textarea",
                        (
                            "Calculate media cost per raw inquiry and total cost per "
                            "signed retainer, usable evidence file, and accepted case. "
                            "State the relevant denominators and explain why these "
                            "management ratios do not establish lawful compensation terms."
                        ),
                        (
                            "With $18,000 media and $36,425 total cost, 1,000 inquiries "
                            "cost $18 each in media. Total cost is $202.36 per 180 "
                            "retainers, $289.09 per 126 usable files, and $337.27 per "
                            "108 acceptances. These are cohort diagnostics; the fixed monthly "
                            "service invoice remains $58,750."
                        ),
                    ),
                    field(
                        "Duplicate and nonqualifying-proof sensitivity",
                        "textarea",
                        (
                            "Stress duplicate prevalence and unusable-record rates while "
                            "holding the raw cohort and media budget constant. Recalculate "
                            "downstream counts, state whether fractions represent expectations, "
                            "and identify costs that do not fall automatically with conversion."
                        ),
                        (
                            "At 20% duplicate suppression, 1,000 inquiries produce 800 unique "
                            "candidates and 160 retainers at 20%. If only 60% yield usable "
                            "proof, 96 files remain; using the baseline 108/126 acceptance "
                            "ratio, expected acceptances are approximately 82.29. Media stays "
                            "$18,000, and lower throughput does not automatically reduce fixed staffing commitments."
                        ),
                    ),
                    field(
                        "Retrieval outlay and corrective-service stress",
                        "textarea",
                        (
                            "Model provider charges, request frequency, and labor needed "
                            "for incomplete packets. Separate lawful provider fees from "
                            "MSO handling costs, and state whether the customer contract "
                            "absorbs overruns or permits prospective documented scope changes."
                        ),
                        (
                            "The $4,500 retrieval budget assumes 180 files averaging $25 "
                            "in permitted external outlays, not a statutory fee schedule. "
                            "An $8 increase per file adds $1,440; 40 extra labor hours "
                            "at $35 add $1,400. Monthly cost becomes $39,265, leaving "
                            "$19,485 profit and approximately 33.17% margin."
                        ),
                    ),
                    field(
                        "Working-capital runway and reserve float",
                        "textarea",
                        (
                            "Estimate cash needed for the collection cycle, add an "
                            "unrestricted operating reserve, and compare available funding. "
                            "Keep service advances, credit facilities, restricted money, "
                            "and founder capital separate so the model cannot double-count liquidity."
                        ),
                        (
                            "At $36,425 monthly cost, a simplified 45-day cycle consumes "
                            "$54,637.50; adding a $15,000 reserve requires $69,637.50. "
                            "Founder capital of $35,000 plus a $35,000 committed line "
                            "provides $70,000. This excludes any service advance; actual "
                            "daily disbursements and line charges require separate cash-calendar validation."
                        ),
                    ),
                    field(
                        "Collection shock and cash-stop threshold",
                        "textarea",
                        (
                            "Extend the collection cycle and calculate the resulting "
                            "funding shortfall without altering earned revenue. Specify "
                            "which spending pauses first, how customer continuity is "
                            "protected, and who authorizes any additional committed borrowing."
                        ),
                        (
                            "A 60-day cycle requires $72,850 operating cash plus the "
                            "$15,000 reserve, totaling $87,850. Against $70,000 committed "
                            "funding, the shortfall is $17,850. The operator pauses new "
                            "media purchases before exhausting reserves, preserves existing "
                            "record follow-up, and seeks revised payment terms rather than settlement-linked compensation."
                        ),
                    ),
                ],
                "completion_gate": (
                    "All three annual scenarios reconcile exactly; base monthly costs total "
                    "$36,425; the five-stage waterfall is visible; and a dated cash calendar "
                    "demonstrates funding without client trust money, settlement proceeds, "
                    "or duplicated service advances."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn each authorized inquiry into a traceable administrative workflow "
                    "without duplicate contacts, duplicate record charges, or unsupported "
                    "clinical summaries. Establish stable identifiers, evidence lineage, "
                    "human legal decisions, reconciled invoice events, and controlled "
                    "exception handling from intake receipt through collected service fees."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign separate identifiers to people, matters, source inquiries, "
                        "record requests, document versions, and invoices. Preserve "
                        "their relationships without treating a phone number as a "
                        "permanent identity or assuming one person can have only one matter."
                    ),
                    (
                        "Define each state transition with its authorized actor, "
                        "required evidence, timestamp, and retry behavior. Capture "
                        "rejection and correction events rather than overwriting "
                        "history, and keep production state distinct from the firm's "
                        "legal representation and case-acceptance decisions."
                    ),
                    (
                        "Verify the applicable record-access route before generating "
                        "requests. Check signatures, recipient instructions, identity "
                        "evidence, provider destinations, and deadlines; then reconcile "
                        "received pages against requested date ranges before sending "
                        "anything to a chronology parser or attorney reviewer."
                    ),
                    (
                        "Test automation with duplicate deliveries, timeouts, partial "
                        "documents, incorrect identity matches, and withdrawn permissions. "
                        "Require deterministic event keys and human exception handling "
                        "so retries cannot create additional invoices, unauthorized "
                        "contacts, or requests to an obsolete recipient."
                    ),
                    (
                        "Reconcile the operational ledger to provider outlays, supplier "
                        "credits, the monthly administrative invoice, and actual bank "
                        "receipts. Review a sample of completed packets against source "
                        "pages, and record the supervising attorney's acceptance independently "
                        "from the accounting close."
                    ),
                ],
                "fields": [
                    field(
                        "Identifier map and minimum-data design",
                        "textarea",
                        (
                            "Define the identifiers linking inquiry, person, matter, request, "
                            "document, and invoice records. Specify where sensitive identity "
                            "attributes reside and how authorized staff resolve collisions "
                            "without exposing medical content in general operational logs."
                        ),
                        (
                            "Inquiry INQ-24001 links to person PER-810, matter MAT-430, "
                            "request REQ-990, and document DOC-771 version 2. The service "
                            "invoice is INV-046-07. Restricted identity storage holds birth "
                            "date and address; ordinary logs show tokens only. A second "
                            "matter receives its own identifier after attorney confirmation."
                        ),
                    ),
                    field(
                        "Idempotency key and delivery semantics",
                        "textarea",
                        (
                            "Specify stable event keys, uniqueness enforcement, transaction "
                            "boundaries, and safe retry behavior. Explain how the workflow "
                            "handles an external provider that cannot support idempotency "
                            "rather than assuming every successful network call is observable."
                        ),
                        (
                            "The request key combines matter ID, provider ID, request "
                            "scope, and authorization version. A PostgreSQL unique constraint "
                            "blocks duplicate creation; an outbox records pending delivery. "
                            "If a portal submission times out after possible receipt, staff "
                            "check provider status before resubmission, preventing a second "
                            "charge for the same request."
                        ),
                    ),
                    field(
                        "State machine and decision authority",
                        "textarea",
                        (
                            "List operational states and required evidence for advancing "
                            "between them. Identify the attorney-owned transitions and "
                            "describe how a failed identity match, missing permission, "
                            "or incomplete source record suspends the affected activity."
                        ),
                        (
                            "States are received, provenance checked, duplicate screened, "
                            "firm retainer signed, access request authorized, records received, "
                            "proof indexed, attorney accepted, and service period reconciled. "
                            "Only firm counsel marks representation and acceptance. Missing "
                            "contact permission blocks outbound calls; missing record authority "
                            "blocks retrieval without deleting the inquiry's audit trail."
                        ),
                    ),
                    field(
                        "Access request pre-flight",
                        "textarea",
                        (
                            "Record the chosen HIPAA access or authorization route, "
                            "requester identity, signature requirements, exact recipient, "
                            "provider destination, and requested scope. Explain how an "
                            "incorrect route or superseded authorization is detected before transmission."
                        ),
                        (
                            "For a patient-directed electronic copy, staff verify the "
                            "written signed instruction, designated recipient, and relevant "
                            "electronic-record scope under 45 CFR 164.524. A broader "
                            "third-party release uses a valid 164.508 authorization when "
                            "appropriate. The checklist records route selection; it does "
                            "not treat all signed documents as interchangeable."
                        ),
                    ),
                    field(
                        "Provider clock and follow-up schedule",
                        "textarea",
                        (
                            "Track the provider's receipt date, applicable response period, "
                            "documented extension, and escalation owner. Distinguish an "
                            "internal follow-up target from a statutory deadline and "
                            "record when another applicable rule requires faster handling."
                        ),
                        (
                            "A covered provider receives an individual access request "
                            "on day 0. Staff check status on day 10 and escalate "
                            "on day 25. Under 45 CFR 164.524(b)(2), the baseline "
                            "is 30 days, with one qualifying 30-day extension supported "
                            "by timely written reasons and a completion date."
                        ),
                    ),
                    field(
                        "Document receipt and provenance manifest",
                        "textarea",
                        (
                            "Specify checks for patient identity, requested dates, page "
                            "counts, file integrity, and source attribution. Explain how "
                            "partial production, corrupted files, and unrelated patients' "
                            "pages are isolated before routine staff or models can process them."
                        ),
                        (
                            "A 142-page production contains 137 matching pages, three "
                            "blank pages, and two pages for another patient. The "
                            "reviewer restricts the mixed file, records the incident, "
                            "requests corrected production, and creates a controlled "
                            "working copy. SHA-256 digests and receipt timestamps "
                            "identify every source and derivative version."
                        ),
                    ),
                    field(
                        "Chronology extraction and clinical QA",
                        "textarea",
                        (
                            "Define the structured chronology fields, source-page citations, "
                            "uncertainty handling, and human review sample. Require the "
                            "parser to distinguish recorded diagnosis from inferred "
                            "causation and to preserve conflicting dates rather than silently resolving them."
                        ),
                        (
                            "Each row records encounter date, provider, quoted diagnosis, "
                            "recorded ICD-10 code, medication, exposure reference, and page "
                            "citation. A model extracts 24 events; a reviewer corrects "
                            "two date errors and rejects one unsupported causal statement. "
                            "Counsel receives the corrected chronology, original excerpts, "
                            "and a contradiction list."
                        ),
                    ),
                    field(
                        "Deficiency queue and rework aging",
                        "textarea",
                        (
                            "Categorize missing evidence, vendor defects, client follow-up, "
                            "and attorney questions separately. Assign owners and "
                            "deadlines, preserve the replacement-window clock, and "
                            "explain which corrections are included in the fixed administrative scope."
                        ),
                        (
                            "Of 126 usable files, 18 await attorney-identified deficiencies "
                            "and 108 are accepted. Ten need missing date ranges, five "
                            "need medication reconciliation, and three need signed corrections. "
                            "The coordinator assigns two-business-day triage targets; the "
                            "30-day contractual notice window applies to administrative defects, "
                            "not promised case outcomes."
                        ),
                    ),
                    field(
                        "Service ledger and collection reconciliation",
                        "textarea",
                        (
                            "Describe how completed services support the monthly invoice "
                            "without multiplying fees by accepted claims. Match invoice "
                            "identifiers, credits, deposits, and bank receipts, preserving "
                            "the distinction between earned revenue and the date cash arrives."
                        ),
                        (
                            "July services support one $58,750 invoice. The ledger applies "
                            "a previously recorded $15,000 service advance and matches "
                            "a $43,750 bank receipt, leaving zero receivable. The "
                            "108 accepted cases appear in the service report only; "
                            "no ledger line allocates a percentage of attorney fees."
                        ),
                    ),
                    field(
                        "Pre-flight test evidence and release record",
                        "textarea",
                        (
                            "List the test cases required before production changes, "
                            "expected results, reviewer identity, and retained artifacts. "
                            "Include permissions withdrawal, duplicate transmission, "
                            "incorrect patient matching, and invoice replay rather than testing "
                            "only successful intake and extraction paths."
                        ),
                        (
                            "The test pack contains 12 synthetic matters: two duplicate "
                            "webhooks, two missing permissions, two patient mismatches, "
                            "two partial packets, two invoice replays, and two valid "
                            "paths. Expected results include one request per stable key "
                            "and zero duplicate invoices. The release record stores "
                            "actual outcomes before deployment."
                        ),
                    ),
                ],
                "completion_gate": (
                    "A synthetic end-to-end cohort demonstrates reproducible identifiers, "
                    "safe retries, correct access routing, source-linked chronology output, "
                    "attorney-controlled acceptance, and an invoice-to-receipt reconciliation "
                    "with no duplicate request charges or unsupported case-linked fees."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Translate professional-conduct rules, health-record access requirements, "
                    "contact restrictions, and confidentiality duties into inspectable "
                    "contract terms and operational evidence. Distinguish ordinary nonlawyer "
                    "MSO work from a specifically licensed Arizona structure, and assign "
                    "qualified legal owners to jurisdiction-specific interpretation and remediation."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Create a jurisdiction matrix covering the firm, prospective "
                        "client, advertising audience, caller, provider, and service "
                        "entity. Have firm counsel identify applicable adopted rules "
                        "and state statutes rather than assuming ABA model language "
                        "itself supplies nationwide operating permission."
                    ),
                    (
                        "Attach the service scope, pricing support, independence terms, "
                        "security duties, and rework limits to the agreement. "
                        "Test actual conduct against those clauses, because a fixed "
                        "invoice label cannot cure prohibited referrals, unauthorized "
                        "legal practice, or interference with professional judgment."
                    ),
                    (
                        "Classify every record request by legal route and every "
                        "data recipient by actual function. Verify applicable "
                        "authorizations, business-associate duties, security controls, "
                        "and transfer restrictions before granting access to health "
                        "records or connecting an external processing service."
                    ),
                    (
                        "Audit advertisements, permission language, calling practices, "
                        "recordings, and vendor sourcing against current federal "
                        "and state requirements. Preserve the version examined and "
                        "counsel's determination, including any deliberately stricter "
                        "contractual operating standard that exceeds a statutory minimum."
                    ),
                    (
                        "Assign each finding an owner, remediation deadline, and "
                        "evidence requirement. Suspend the affected activity when "
                        "authority or lawful structure is absent, while preserving "
                        "existing client files and routing representation questions "
                        "to the responsible attorney rather than intake personnel."
                    ),
                ],
                "fields": [
                    field(
                        "Jurisdiction and professional-rule matrix",
                        "textarea",
                        (
                            "Identify each relevant jurisdiction and the adopted rules "
                            "governing the proposed service. Record counsel's primary "
                            "sources and review date, distinguishing model provisions "
                            "from binding local requirements and identifying specific unresolved operating restrictions."
                        ),
                        (
                            "The firm serves New York clients while its MSO operates "
                            "remotely. Counsel checks New York Rules 5.4, 5.5, and "
                            "7.2 plus Judiciary Law 478 for unauthorized-practice exposure. "
                            "The matrix separately records advertising destinations and "
                            "caller locations; expansion into Florida requires a new "
                            "state-specific review before traffic begins."
                        ),
                    ),
                    field(
                        "Rule 5.4 pricing and independence addendum",
                        "textarea",
                        (
                            "Draft the operative compensation and independence clauses "
                            "for an ordinary nonlawyer MSO. Address settlement sensitivity, "
                            "client selection, strategy control, payment source, and "
                            "fair-market documentation without relying solely on the phrase fixed fee."
                        ),
                        (
                            "Clause: The monthly administrative fee is $58,750 for "
                            "defined services and does not vary with referrals, "
                            "retainers, recoveries, or legal fees. The firm exclusively "
                            "controls representation and professional judgment. Payment "
                            "comes from its operating account. Quarterly scope changes "
                            "require documented service costs and prospective written agreement."
                        ),
                    ),
                    field(
                        "Arizona ABS structure verification",
                        "textarea",
                        (
                            "If an Arizona alternative business structure is proposed, "
                            "identify the licensed entity, approved ownership, compliance "
                            "responsibility, authorized activities, and license conditions. "
                            "Explain why an Arizona connection alone does not authorize "
                            "fee sharing elsewhere."
                        ),
                        (
                            "The ordinary launch uses no ABS exception and receives "
                            "zero legal-fee participation. A later co-venture requires "
                            "verification under Arizona Supreme Court Rule 33.1 and "
                            "ACJA 7-209, including license scope and responsible personnel. "
                            "An Arizona mailing address or lawyer shareholder does not "
                            "convert the current MSO into that licensed entity."
                        ),
                    ),
                    field(
                        "Advertising, referrals, and intake boundaries",
                        "textarea",
                        (
                            "Specify who approves advertisements and intake scripts, "
                            "what staff may explain, and what they must escalate. "
                            "Address paid recommendations, misleading claim values, "
                            "solicitation restrictions, and jurisdiction-specific recordkeeping requirements "
                            "using the firm's adopted professional rules."
                        ),
                        (
                            "Under applicable counterparts to ABA Rules 7.1, 7.2, "
                            "7.3, and 5.5, counsel approves every campaign and "
                            "script version. Staff collect facts and schedule attorney "
                            "calls; they do not estimate settlements or determine "
                            "eligibility. Vendor invoices identify advertising services, "
                            "not payments for personal recommendations or retained clients."
                        ),
                    ),
                    field(
                        "TCPA contact permission and suppression",
                        "textarea",
                        (
                            "Record the approved contact channels, consent evidence, "
                            "seller identity, revocation handling, and suppression checks. "
                            "Distinguish contractual one-to-one permission standards from "
                            "current federal requirements, and account for technology-specific "
                            "and state-specific calling restrictions."
                        ),
                        (
                            "The contract requires firm-specific one-to-one written "
                            "permission for covered marketing outreach under 47 U.S.C. "
                            "227 and 47 CFR 64.1200. Counsel notes the FCC's "
                            "2023 one-to-one amendment was vacated in 2025; the "
                            "stricter contract remains. Revocations enter immediate "
                            "suppression, with applicable calling-hour and state rules checked."
                        ),
                    ),
                    field(
                        "HITECH access, authorization, and fee routing",
                        "textarea",
                        (
                            "Specify when individual access, electronic third-party "
                            "direction, or a separate authorization applies. Record "
                            "the fee rule for the selected route and avoid "
                            "representing HITECH as a universal cheap-records mechanism "
                            "for litigation vendors."
                        ),
                        (
                            "The route sheet cites 42 U.S.C. 17935(e), 45 CFR "
                            "164.524, and 164.508. Counsel applies the Ciox decision's "
                            "limits when evaluating third-party directions. Individual "
                            "access fees follow permitted cost categories; the team "
                            "does not assume those limits cover every third-party "
                            "request or that search charges belong in individual-access fees."
                        ),
                    ),
                    field(
                        "HIPAA role and processing agreement inventory",
                        "textarea",
                        (
                            "Determine whether each participant is a covered entity, "
                            "business associate, subcontractor, or other authorized "
                            "recipient. Tie required agreements and safeguards to "
                            "actual functions rather than assuming possession of medical "
                            "records automatically establishes HIPAA business-associate status."
                        ),
                        (
                            "A patient's law firm is not automatically a business "
                            "associate merely because it receives authorized records. "
                            "If the MSO performs covered functions for a covered "
                            "entity or business associate, counsel evaluates 45 CFR "
                            "160.103, 164.502(e), and 164.504(e). Appropriate agreements "
                            "precede vendor access, alongside contractual confidentiality and security duties."
                        ),
                    ),
                    field(
                        "Sensitive records and recording restrictions",
                        "textarea",
                        (
                            "Identify record categories and communication practices "
                            "requiring additional review, including substance-use "
                            "treatment, psychotherapy notes, minors' information, and "
                            "call recordings. Specify how staff detect these categories "
                            "and stop inappropriate routing before external processing."
                        ),
                        (
                            "A packet marked as a substance-use treatment program "
                            "record is restricted pending counsel's 42 CFR Part 2 "
                            "assessment, including litigation-use limits. Psychotherapy "
                            "notes receive separate authorization review. Call recording "
                            "is disabled until counsel checks 18 U.S.C. 2511 and "
                            "applicable state all-party rules for the participants' locations."
                        ),
                    ),
                    field(
                        "Security incident and notification ownership",
                        "textarea",
                        (
                            "Define incident reporting, containment, evidence preservation, "
                            "legal classification, and notification responsibility. Distinguish "
                            "contractual escalation times from statutory outside limits, "
                            "and require review of state obligations alongside applicable "
                            "HIPAA breach provisions."
                        ),
                        (
                            "The MSO alerts the firm's incident lead within four "
                            "hours of discovering misdirected records, suspends the "
                            "link, and preserves access evidence. Counsel evaluates "
                            "45 CFR 164.400–414 when applicable, including business-associate "
                            "notice without unreasonable delay and within 60 days. "
                            "The four-hour contract deadline controls internal escalation."
                        ),
                    ),
                    field(
                        "Contract audit findings and remediation evidence",
                        "textarea",
                        (
                            "Record each finding, affected workflow, owner, deadline, "
                            "and objective closure evidence. Include confidentiality, "
                            "subcontractor access, legal independence, source permissions, "
                            "payment terms, and retention so the audit examines "
                            "operations as well as signed documents."
                        ),
                        (
                            "Finding A removes a supplier clause promising payment "
                            "per signed retainer. Finding B disables an unapproved "
                            "document processor. Finding C adds a 30-day defect "
                            "notice period. Counsel signs the revised scope, security "
                            "verifies processor removal, and the operator stores "
                            "executed versions before restarting the affected acquisition channel."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Firm counsel confirms the applicable operating structure, advertising "
                    "and contact rules, record-request routes, and executed agreements. "
                    "Every critical finding has objective closure evidence or the affected "
                    "activity remains suspended with a named remediation owner."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Design automation that lowers administrative effort without transferring "
                    "legal judgment to software or multiplying questionable inquiries. "
                    "Connect permission evidence, duplicate screening, provider retrieval, "
                    "source-linked chronology extraction, and operational feedback while "
                    "maintaining human fallback capacity for fraud, outages, evidence defects, "
                    "and litigation shocks."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Map each automation to a specific bottleneck, measurable "
                        "time saving, authorized dataset, and accountable human. "
                        "Keep identity screening, record access, clinical extraction, "
                        "and legal acceptance separate so a convenient integration "
                        "cannot silently acquire authority beyond its assigned function."
                    ),
                    (
                        "Set baseline acquisition and evidence-quality metrics before "
                        "testing new publishers. Compare complete cohorts using "
                        "duplicate rates, permission defects, usable records, and "
                        "customer collection, rather than optimizing solely for "
                        "cheap inquiries or a model-generated prediction of case value."
                    ),
                    (
                        "Apply restricted access and data minimization to every "
                        "integration. Keep medical narratives away from advertising "
                        "platforms, verify processor terms before sending records, "
                        "and ensure operational analytics can function with "
                        "aggregated measures rather than identifiable client information."
                    ),
                    (
                        "Define measurable stop conditions for model errors, vendor "
                        "fraud, retrieval backlog, system failures, and changes "
                        "in litigation viability. Pair every stop condition "
                        "with a manual queue, responsible owner, and communication "
                        "plan so production can degrade safely."
                    ),
                    (
                        "Close the acquisition feedback loop with documented vendor "
                        "remedies and prospective budget changes. Preserve cohort "
                        "history after changes, separate supplier defects from "
                        "medical nonqualification, and prevent customer pressure "
                        "from turning administrative metrics into prohibited outcome-based compensation."
                    ),
                ],
                "fields": [
                    field(
                        "Automation inventory and human ownership",
                        "textarea",
                        (
                            "List each automated step, trigger, source system, "
                            "permitted output, accountable reviewer, and fallback. "
                            "Explain which decisions remain with the firm and "
                            "how the inventory prevents tools from expanding "
                            "their role through undocumented integrations."
                        ),
                        (
                            "The inventory assigns TrustedForm retrieval to acquisition "
                            "operations, authorized identity checks to the intake "
                            "lead, request scheduling to the records coordinator, "
                            "and chronology extraction to a supervised processor. "
                            "Firm counsel alone decides representation and acceptance. "
                            "Each connector has an owner, access scope, retry limit, "
                            "and manual work instruction."
                        ),
                    ),
                    field(
                        "Permission evidence and fraud firewall",
                        "textarea",
                        (
                            "Define the combined checks for provenance, duplicate "
                            "submission, suspicious identity patterns, and conflicting "
                            "retainer claims. Explain the limits of commercial "
                            "tools and how manual escalation protects legitimate "
                            "people from automatic rejection based on imperfect matching."
                        ),
                        (
                            "A 1,000-inquiry cohort triggers 70 exact duplicates, "
                            "20 probable duplicates, and 10 unresolved identity "
                            "alerts. Staff resolve ambiguous matches before "
                            "progression. TrustedForm supports source evidence; "
                            "LexisNexis supports authorized identity research. Neither "
                            "proves exclusive representation, and no cross-firm "
                            "client list is exchanged without a lawful basis."
                        ),
                    ),
                    field(
                        "Provider retrieval scheduler and retry budget",
                        "textarea",
                        (
                            "Specify request scheduling, rate limits, status polling, "
                            "retry counts, and escalation for providers without "
                            "reliable electronic interfaces. Separate internal automation "
                            "targets from provider legal obligations and prevent "
                            "retries from creating repeated charges or duplicate disclosures."
                        ),
                        (
                            "The scheduler creates at most one active request "
                            "per stable request key and permits three technical "
                            "retries for transport failures. A confirmed receipt "
                            "switches the job to status tracking. Portal ambiguity "
                            "goes to manual checking; day-10 follow-up and "
                            "day-25 escalation remain visible on the provider calendar."
                        ),
                    ),
                    field(
                        "Chronology model contract and evaluation",
                        "textarea",
                        (
                            "Specify permitted model processing, retention terms, "
                            "required source citations, evaluation cases, and error "
                            "thresholds. Require abstention on unsupported facts "
                            "and explain how prompt-like instructions embedded "
                            "inside source documents are treated as record content."
                        ),
                        (
                            "The selected processor must support the required "
                            "contractual safeguards and appropriate BAA where "
                            "applicable; identifiable records never enter a "
                            "public consumer chat. A 50-document test set "
                            "requires every chronology statement to cite a "
                            "page. Embedded instructions are ignored, and "
                            "unsupported causal conclusions always route to rejection."
                        ),
                    ),
                    field(
                        "Acquisition experiment and cohort scorecard",
                        "textarea",
                        (
                            "Define one controlled acquisition experiment with "
                            "budget, audience, approved message, evaluation period, "
                            "and quality metrics. Keep downstream acceptance "
                            "as a quality measure rather than a supplier "
                            "payment trigger or a proxy for settlement value."
                        ),
                        (
                            "Two approved publishers each receive a $3,000 "
                            "two-week media allocation. Publisher A delivers "
                            "150 inquiries with 8% duplicates; Publisher B "
                            "delivers 200 with 25% duplicates. The operator "
                            "waits for matured permission and evidence metrics "
                            "before reallocating spend, while paying for contracted "
                            "advertising rather than accepted cases."
                        ),
                    ),
                    field(
                        "Privacy-preserving acquisition feedback",
                        "textarea",
                        (
                            "Describe what conversion information may leave the "
                            "case-management environment and what must remain "
                            "restricted. Address pixels, audience uploads, hashed "
                            "identifiers, medical categories, and reporting thresholds "
                            "so campaign optimization does not disclose client health or representation details."
                        ),
                        (
                            "The media dashboard receives weekly channel totals "
                            "for valid permissions and administrative completion, "
                            "subject to counsel's review. It receives no "
                            "diagnoses, medical pages, claimant lists, or "
                            "retainer identities. Hashed email addresses remain "
                            "restricted identifiers, not anonymous statistics; "
                            "tracking pixels are excluded from authenticated intake "
                            "and medical-document pages."
                        ),
                    ),
                    field(
                        "Queue capacity and manual fallback staffing",
                        "textarea",
                        (
                            "Calculate available processing hours, average handling "
                            "time, maximum queue age, and fallback capacity. "
                            "Explain how automation failure changes throughput "
                            "without hiding unpaid overtime, extra workers, "
                            "or reduced review standards inside the small-team scenario."
                        ),
                        (
                            "Three contractors provide 80 delivery hours monthly "
                            "at a blended $100 hourly allocation, matching "
                            "$8,000 labor. At 20 minutes per packet, "
                            "180 packets use 60 hours and leave 20 "
                            "for corrections. A 40-hour outage exceeds that "
                            "buffer; new intake is throttled or additional "
                            "paid capacity is explicitly budgeted."
                        ),
                    ),
                    field(
                        "Vendor fraud trigger and containment",
                        "textarea",
                        (
                            "Set measurable thresholds for suspicious clusters, "
                            "permission failures, duplicate spikes, and supplier "
                            "noncooperation. Describe payment disputes, preservation "
                            "of evidence, and protection of potentially legitimate "
                            "clients without accusing every flagged individual of fabrication."
                        ),
                        (
                            "A publisher's duplicate rate rises from 10% "
                            "to 28% across 200 inquiries, with 16 "
                            "unretrievable permission records. The operator pauses "
                            "that source, preserves original submissions, and "
                            "requests contractual credits for proven defects. "
                            "Existing signed clients remain with firm counsel "
                            "for individual assessment rather than automatic batch rejection."
                        ),
                    ),
                    field(
                        "Rule 702 litigation shock response",
                        "textarea",
                        (
                            "Describe how the operation detects a material "
                            "causation ruling or litigation-development risk and "
                            "changes prospective spending. Identify counsel's role "
                            "under Federal Rule of Evidence 702 and "
                            "separate docket monitoring from automated predictions about legal outcomes."
                        ),
                        (
                            "Counsel monitors the relevant MDL docket through "
                            "PACER and evaluates any Rule 702 general-causation "
                            "decision. A material adverse ruling prompts a "
                            "same-day review of new media commitments. The "
                            "MSO preserves existing files, continues authorized "
                            "administrative duties, and follows counsel's instructions "
                            "rather than terminating representation or promising another recovery."
                        ),
                    ),
                    field(
                        "Recovery drill and automation restart",
                        "textarea",
                        (
                            "Define a repeatable drill covering service outage, "
                            "incorrect extraction, unauthorized recipient, and delayed "
                            "provider response. Require evidence of restored "
                            "integrity, reconciled event counts, and authorized "
                            "restart rather than assuming system availability proves correct operation."
                        ),
                        (
                            "The monthly drill disables the request connector "
                            "for two hours and injects five replayed "
                            "events into a synthetic queue. Staff use "
                            "the manual register, then reconcile request "
                            "keys and provider receipts before restart. "
                            "Success requires zero duplicate submissions, no "
                            "unreconciled outlays, and documented review of every exception."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each automation has an authorized data scope, measured performance "
                    "target, named human owner, and tested manual fallback. Acquisition "
                    "feedback excludes identifiable health information, and fraud, model "
                    "error, cash stress, and Rule 702 shocks have explicit spending-stop rules."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Convert the operating design into a sequenced 30-day readiness sprint "
                    "with accountable owners, affordable pilot limits, and auditable metrics. "
                    "Build a transferable service business through clean contracts, repeatable "
                    "production, reliable collections, controlled data access, and records "
                    "that support diligence without exposing client confidences."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first 30 days as a readiness "
                        "and controlled-pilot sprint, not a promise of "
                        "immediate contracted revenue. Keep the canonical "
                        "1–4 month first-deal horizon visible and avoid "
                        "committing a full base-case media budget before "
                        "customer authority and funding exist."
                    ),
                    (
                        "Assign one accountable owner to each sprint "
                        "deliverable and define observable completion evidence. "
                        "Sequence contracts, permissions, security, synthetic "
                        "testing, and funded production so the team "
                        "does not collect sensitive records merely to "
                        "demonstrate technical progress."
                    ),
                    (
                        "Publish a weekly pod scorecard with raw "
                        "cohort counts, conversion denominators, queue aging, "
                        "source defects, service effort, receivable aging, "
                        "and cash runway. Label immature cohorts and "
                        "separate customer acceptance decisions from administrative "
                        "service billing and collection."
                    ),
                    (
                        "Create an exit-readiness ledger from the "
                        "first signed engagement rather than reconstructing "
                        "it during a transaction. Preserve pricing "
                        "support, contract versions, assignment conditions, "
                        "processor inventories, and reconciliations while "
                        "limiting prospective buyers to appropriately aggregated "
                        "or authorized diligence materials."
                    ),
                    (
                        "At day 30, compare completed evidence "
                        "against the launch criteria and document "
                        "unresolved dependencies. Continue only the funded "
                        "and authorized scope, maintain explicit recovery "
                        "plans for delays, and update the next "
                        "30-day plan without rewriting historical targets."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 counterparty and scope sprint",
                        "textarea",
                        (
                            "List first-week deliverables for customer verification, "
                            "jurisdiction mapping, service design, and pricing "
                            "support. Assign owners and evidence artifacts, "
                            "and specify which production activities remain "
                            "disabled until the customer relationship is authorized and funded."
                        ),
                        (
                            "By day 3, the operator assembles entity "
                            "and bar verification; by day 5, counsel "
                            "reviews the jurisdiction matrix; by day 7, "
                            "the firm receives the $58,750 monthly scope "
                            "and pricing support. Paid traffic and "
                            "medical-record collection remain disabled while "
                            "contract execution and funding are pending."
                        ),
                    ),
                    field(
                        "Days 8–14 contracts and security sprint",
                        "textarea",
                        (
                            "Define second-week outputs for service terms, "
                            "contact scripts, data processing, account permissions, "
                            "and incident ownership. Require specific evidence "
                            "of execution and configuration rather than "
                            "treating an unsigned template or planned setting as completed work."
                        ),
                        (
                            "The week-two checklist requires executed service "
                            "terms, counsel-approved advertisements, role-based access, "
                            "multifactor authentication, processor review, and "
                            "a named incident lead. The operator "
                            "captures configuration evidence using synthetic "
                            "records. Any outstanding BAA required by "
                            "the actual relationship blocks that processor "
                            "from receiving identifiable health records."
                        ),
                    ),
                    field(
                        "Days 15–21 synthetic test and pilot sprint",
                        "textarea",
                        (
                            "Specify the synthetic test pack, permitted "
                            "live-pilot scope, spending limit, customer authorization, "
                            "and stopping conditions. Explain how pilot "
                            "results will be reported when retainers, "
                            "provider responses, or collection events have not yet matured."
                        ),
                        (
                            "Days 15–18 run the 12-matter synthetic "
                            "pack and invoice replay tests. If "
                            "contracts and funding are complete, days "
                            "19–21 permit a $1,500 media pilot "
                            "with at most 100 inquiries. The "
                            "report marks record and collection stages "
                            "as pending events with named follow-up "
                            "dates, never as completed conversions."
                        ),
                    ),
                    field(
                        "Days 22–30 launch decision and next cycle",
                        "textarea",
                        (
                            "Define the day-30 decision evidence, unresolved "
                            "dependencies, authorized spending ceiling, and "
                            "next-cycle priorities. Explain what happens "
                            "if no firm has signed by "
                            "the deadline while preserving the canonical first-deal timeline and startup budget."
                        ),
                        (
                            "Day 30 requires a verified contract, "
                            "funding evidence, passing synthetic tests, "
                            "and counsel-approved workflows before routine "
                            "production. If no firm has signed, "
                            "the team continues targeted outreach within "
                            "the 1–4 month first-deal horizon and "
                            "spends no base-case media budget. The "
                            "next sprint prioritizes contracting rather than artificial volume."
                        ),
                    ),
                    field(
                        "Pod roles, capacity, and escalation map",
                        "textarea",
                        (
                            "Assign the full-time operator and three "
                            "contractors to defined responsibilities, hours, "
                            "handoffs, and escalation duties. Identify "
                            "customer-side attorney responsibilities separately so "
                            "the staffing model does not quietly include unbudgeted legal personnel or unlimited contractor availability."
                        ),
                        (
                            "The full-time operator owns commercial terms, "
                            "cash, and QA. Contractor A handles "
                            "intake, B coordinates records, and C "
                            "prepares chronologies within the $8,000 "
                            "delivery allocation. Firm counsel remains "
                            "customer-side and owns representation decisions. "
                            "The scaled plan adds one full-time "
                            "operator and one contractor, reaching six people total."
                        ),
                    ),
                    field(
                        "Weekly KPI definitions and cohort maturity",
                        "textarea",
                        (
                            "Define the weekly metrics, denominators, "
                            "cutoff date, accountable owner, and "
                            "maturity labels. Include each waterfall "
                            "stage, operational errors, and collection "
                            "performance so an attractive inquiry count cannot conceal rejected proof or unpaid administrative invoices."
                        ),
                        (
                            "The mature monthly reference reports "
                            "1,000 inquiries, 900 unique candidates, "
                            "180 retainers, 126 usable files, "
                            "108 acceptances, and $58,750 collected "
                            "against service invoices. Weekly cohorts "
                            "show days since intake and open "
                            "provider requests. The scorecard separately "
                            "tracks duplicate rate, correction hours, "
                            "receivable aging, and unrestricted cash days."
                        ),
                    ),
                    field(
                        "Startup allocation and purchase discipline",
                        "textarea",
                        (
                            "Allocate founder startup capital among "
                            "setup, testing, systems, and working "
                            "cash while remaining inside the "
                            "canonical range. Distinguish spending authority "
                            "from cash already disbursed and reconcile remaining liquidity before starting the full operating cycle."
                        ),
                        (
                            "A $35,000 startup allocation reserves "
                            "$7,000 for contracts and setup, "
                            "$3,000 for systems, $1,500 for "
                            "pilot media, and $23,500 for "
                            "working cash. If all setup "
                            "allocations are spent, founder cash "
                            "plus the $35,000 line totals "
                            "$58,500, leaving $11,137.50 below "
                            "the $69,637.50 full-cycle requirement."
                        ),
                    ),
                    field(
                        "Contract and operating-asset transfer ledger",
                        "textarea",
                        (
                            "Record transferable contracts, assignment "
                            "conditions, operating procedures, software "
                            "licenses, and intellectual-property ownership. "
                            "Separate business assets from client "
                            "relationships and medical records, and identify permissions needed before a buyer can access restricted materials or assume service duties."
                        ),
                        (
                            "The ledger lists the executed "
                            "MSO agreement, assignment-consent clause, "
                            "workflow documentation, contractor IP "
                            "assignments, and processor licenses. "
                            "A buyer initially receives aggregate "
                            "revenue and defect metrics only. "
                            "Client files and medical records "
                            "remain restricted; counsel evaluates "
                            "confidentiality, contract, and transfer "
                            "requirements before any expanded diligence access."
                        ),
                    ),
                    field(
                        "Quality of earnings and concentration evidence",
                        "textarea",
                        (
                            "Specify the monthly records supporting "
                            "recognized revenue, collected cash, "
                            "complete costs, owner net profit, "
                            "and customer concentration. Explain "
                            "how extraordinary setup costs, unpaid labor, restricted advances, and pass-through amounts will be identified rather than hidden in a valuation narrative."
                        ),
                        (
                            "The diligence folder reconciles $705,000 "
                            "base annual revenue, $437,100 costs, "
                            "and $267,900 owner net profit "
                            "to contracts, service records, and "
                            "bank activity. It separately reports "
                            "customer concentration, receivable aging, "
                            "advance liabilities, and setup costs. "
                            "No valuation multiple is applied "
                            "to settlement awards or uncollected "
                            "hypothetical legal fees."
                        ),
                    ),
                    field(
                        "Day-30 sign-off and measurable next commitments",
                        "textarea",
                        (
                            "Record the final readiness decision, "
                            "remaining risks, named owners, "
                            "due dates, and funded next "
                            "commitments. Keep evidence of "
                            "what actually happened separate from targets and require explicit customer authorization before expanding traffic, jurisdictions, services, or data recipients."
                        ),
                        (
                            "Illustrative decision: technical readiness "
                            "passes, but full production waits "
                            "for the $11,137.50 liquidity "
                            "gap to close or the "
                            "scope to shrink prospectively. "
                            "The operator owns funding by "
                            "day 37; counsel owns final "
                            "campaign review by day 34. "
                            "Only the funded pilot continues, "
                            "with results recorded as actuals."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The day-30 ledger distinguishes completed work from targets, identifies "
                    "every unfunded commitment, and records customer authorization for the "
                    "next scope. Staffing, cash, canonical scenario totals, contract "
                    "transferability, and restricted-data handling reconcile before expansion."
                ),
            },
        ],
    }
