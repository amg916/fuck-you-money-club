from __future__ import annotations


def build_volume_048_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-048-qui-tam-sec-and-irs-whistleblower-analytics",
        "volume_id": "vol-048-qui-tam-sec-and-irs-whistleblower-analytics",
        "title": "Data-Mined Qui Tam, SEC & IRS Whistleblower Analytics — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Counsel Underwriting, Retainer Economics, "
            "Evidence Provenance, Statutory Routing, Controlled Automation, and a Cash-Safe "
            "30-Day Launch in Forensic Whistleblower Analytics"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Arbitrage Deal / Counterparty Underwriting & Spread Qualification",
                "purpose": (
                    "Qualify a paying law-firm counterparty and a reproducible evidence thesis before "
                    "spending scarce analyst hours. Separate a useful public-data anomaly from an "
                    "actionable claim, document counsel's evidentiary requirements, and price support "
                    "work independently of speculative statutory recoveries."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Start with one named counsel account, one dataset family, and one alleged "
                        "payment mechanism. Record the purchasing decision-maker, retainer budget, "
                        "conflict-screening method, and source permissions before compiling a "
                        "subject-specific evidence package or circulating identifiable allegations."
                    ),
                    (
                        "Reproduce each anomaly against a defensible peer cohort and inspect ordinary "
                        "explanations such as specialty, geography, coding changes, referral mix, and "
                        "suppressed records. Treat statistical distance as a research lead rather "
                        "than a finding of knowing misconduct."
                    ),
                    (
                        "Ask counsel to identify the government payment nexus, knowledge theory, "
                        "materiality theory, and representative-claim requirements. Keep unavailable "
                        "claim-level proof explicitly listed as an evidence gap; never manufacture "
                        "patient records or imply aggregate utilization establishes false billing."
                    ),
                    (
                        "Create separate commercial and litigation decisions. A funded analytics "
                        "assignment may proceed even when a statutory filing is unsuitable, provided "
                        "the contract describes legitimate deliverables and prohibits contingent "
                        "collection assumptions from funding current operating commitments."
                    ),
                    (
                        "Have counsel evaluate public disclosure, original-source status, first-to-file "
                        "issues, and lawful evidence acquisition before selecting a filing route. "
                        "Record rejection reasons and preservation instructions so an attractive "
                        "anomaly does not bypass substantive eligibility screening."
                    ),
                ],
                "fields": [
                    field(
                        "Paying counterparty and purchase authority",
                        "textarea",
                        (
                            "Identify the law firm, authorized signer, billing contact, conflict-screening "
                            "channel, and independent ability to pay. Specify a retainer purchase "
                            "decision that does not depend on intervention, settlement, or award collection."
                        ),
                        (
                            "Harbor Trial Group, a fictional plaintiff firm, authorizes a $7,500 monthly "
                            "analytics retainer through its managing partner. Accounts payable accepts "
                            "net-15 invoices. The engagement funds 45 analyst hours and one evidence "
                            "memorandum monthly; payment remains due even if counsel declines every "
                            "proposed statutory filing."
                        ),
                    ),
                    field(
                        "Dataset thesis and government payment nexus",
                        "textarea",
                        (
                            "Describe the source release, unit of observation, government payment "
                            "relationship, and suspected mechanism. Distinguish provider-level aggregates "
                            "from individual claims and explain what additional evidence would connect "
                            "the anomaly to an actionable payment."
                        ),
                        (
                            "The pilot compares one CMS Part B provider-service release with the matching "
                            "Open Payments year. An orthopedic cohort contains 420 providers; 18 exceed "
                            "the selected utilization threshold. The lead concerns potentially unsupported "
                            "services, but aggregate payments establish neither an individual false claim "
                            "nor knowledge of falsity."
                        ),
                    ),
                    field(
                        "Peer cohort and innocent-explanation challenge",
                        "textarea",
                        (
                            "Specify cohort inclusion rules, minimum sample size, normalization method, "
                            "and alternative explanations. Record the analyst responsible for challenging "
                            "the thesis and the result required before a subject enters counsel review."
                        ),
                        (
                            "Compare providers within specialty and state, excluding cohorts below 30 "
                            "members. A provider at 3.8 times median utilization falls to 1.4 times after "
                            "site-of-service adjustment. The challenger removes that lead, retains the "
                            "calculation, and prevents the original ranking from appearing in the "
                            "counsel-facing priority queue."
                        ),
                    ),
                    field(
                        "Representative-claim evidence sufficiency",
                        "textarea",
                        (
                            "Ask counsel to map the applicable Rule 9(b) standard to available facts. "
                            "Identify claim identifiers, dates, statements, payment evidence, and firsthand "
                            "support while separating circuit-specific pleading requirements from internal "
                            "research preferences."
                        ),
                        (
                            "Counsel requests two lawfully obtained representative transactions showing "
                            "service date, billing code, asserted falsity, and payment connection. The "
                            "public dataset supplies none of those complete transactions. The evidence "
                            "matrix therefore records an unresolved pleading gap, assigns counsel to "
                            "assess permissible alternatives, and prevents an analyst from labeling "
                            "the matter filing-ready."
                        ),
                    ),
                    field(
                        "Public-disclosure and original-source screen",
                        "textarea",
                        (
                            "Inventory earlier reports, proceedings, media coverage, and government "
                            "disclosures relevant to substantially the same allegations. Have counsel "
                            "assess 31 U.S.C. § 3730(e)(4), including applicable disclosure categories "
                            "and original-source facts."
                        ),
                        (
                            "A trade article already describes the same billing pattern, and the analyst "
                            "used only published aggregates. Counsel records elevated public-disclosure "
                            "risk and requests evidence of qualifying independent knowledge that "
                            "materially adds to the disclosure. The team does not assume that downloading "
                            "government data automatically establishes or defeats original-source status."
                        ),
                    ),
                    field(
                        "First-to-file, conflicts, and relator identity",
                        "textarea",
                        (
                            "Record counsel's conflict result, proposed relator identity, overlapping "
                            "public litigation, and limits on discovering sealed cases. Separate "
                            "entity matching from legal conclusions about 31 U.S.C. § 3730(b)(5) "
                            "and relator eligibility."
                        ),
                        (
                            "The conflict screen clears the fictional purchasing firm for an initial "
                            "engagement. Counsel identifies one public related action but cannot exclude "
                            "an earlier sealed complaint. The proposed relator's knowledge chronology "
                            "remains separate from the analytics company's service contract; a data "
                            "vendor is not automatically the proper statutory claimant."
                        ),
                    ),
                    field(
                        "Retainer scope and contribution spread",
                        "textarea",
                        (
                            "Define deliverable limits, included hours, contractor rates, revision "
                            "allowances, and direct delivery costs. Calculate assignment contribution "
                            "before shared overhead and owner profit; exclude hypothetical government "
                            "recoveries from the commercial spread calculation."
                        ),
                        (
                            "A $7,500 monthly retainer includes 45 hours at $70 internal delivery cost, "
                            "$300 source processing, and $550 independent review. Direct cost totals "
                            "$4,000; assignment contribution is $3,500, or 46.67%. This assignment "
                            "spread excludes shared overhead and does not replace the canonical "
                            "45.0% Base annual net margin."
                        ),
                    ),
                    field(
                        "Authorized evidence boundary and access record",
                        "textarea",
                        (
                            "List permitted public sources, licensed datasets, client-provided materials, "
                            "and restricted categories. Require written authority for nonpublic records "
                            "and distinguish lawful preservation from unauthorized access, credential "
                            "sharing, or acquisition of privileged third-party communications."
                        ),
                        (
                            "The engagement permits CMS downloads, SAM.gov public notices, licensed "
                            "import-manifest records, and documents counsel lawfully supplies. It "
                            "excludes hospital credentials, patient portal access, and employer "
                            "mailbox exports without established authority. Sensitive source material "
                            "enters a restricted workspace only after counsel documents acquisition "
                            "rights and the assigned analyst's access."
                        ),
                    ),
                    field(
                        "Lead disposition and commercial decision",
                        "textarea",
                        (
                            "Set separate acceptance criteria for paid research and potential litigation. "
                            "Record evidence gaps, maximum research spend, decision owner, and "
                            "expiration date so an unresolved legal thesis cannot silently become "
                            "an unlimited unpaid investigation."
                        ),
                        (
                            "Counsel purchases a $3,000 fixed-scope corroboration memo despite unresolved "
                            "claim-level evidence. Work stops after 20 analyst hours or delivery, "
                            "whichever occurs first under the agreed scope. Filing consideration "
                            "remains deferred until counsel resolves eligibility and pleading issues; "
                            "the vendor's invoice is payable regardless of that decision."
                        ),
                    ),
                    field(
                        "Zero-recovery underwriting and concentration limit",
                        "textarea",
                        (
                            "Test the account assuming every proposed matter yields no award. Identify "
                            "retainer collection risk, client concentration, termination exposure, and "
                            "the cash-funded workload that remains supportable without settlement "
                            "proceeds or advances against contingent claims."
                        ),
                        (
                            "The first firm represents 100% of initial revenue, so contractors receive "
                            "only funded monthly assignments. The downside model sets all statutory "
                            "receipts to $0 for five years. A 30-day termination clause triggers "
                            "scope reduction rather than borrowing against a sealed matter or "
                            "promising contractors a future recovery."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Advance only when a named firm can fund the defined scope, counsel has "
                    "documented eligibility and evidence gaps, and the engagement remains viable "
                    "with every statutory award receipt set to $0."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Unit Economics, Escrow/Reserve Float & Working-Capital Calculator",
                "purpose": (
                    "Build a cash model that survives lengthy investigations and complete recovery "
                    "failure. Reconcile all three canonical annual scenarios, distinguish earned "
                    "service revenue from collected cash, and keep restricted funds, claim values, "
                    "government collections, and contingent award interests outside spendable runway."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Copy the canonical annual revenue, margin, profit, and staffing figures "
                        "without substituting a probability-weighted recovery forecast. Build a "
                        "service-revenue bridge capable of supporting each scenario, and label that "
                        "bridge as a planning composition rather than historical performance."
                    ),
                    (
                        "Separate signed contracts, earned revenue, invoices, collections, restricted "
                        "cash, and award contingencies into distinct accounts. Apply contract-specific "
                        "recognition treatment and have the accountant resolve ASC 606 principal-agent "
                        "questions before presenting gross amounts as operator revenue."
                    ),
                    (
                        "Calculate monthly cash commitments from actual staffing and payment terms. "
                        "Keep the stated overhead range separate from total delivery costs, and "
                        "recognize that a funded launch budget can still expire before the "
                        "four-to-twelve-month first-deal window closes."
                    ),
                    (
                        "Model non-intervention, dismissal, settlement delay, unsuccessful proceedings, "
                        "and collection delay explicitly. Use documented cohort denominators for "
                        "observed rates; label planning assumptions clearly instead of presenting "
                        "a selected dismissal percentage as a universal government statistic."
                    ),
                    (
                        "Reconcile every reserve movement to an unrestricted bank balance and a "
                        "written release condition. Do not treat client trust funds, refundable "
                        "advances, government recovery principal, or a projected relator share "
                        "as freely available operating float."
                    ),
                ],
                "fields": [
                    field(
                        "Conservative scenario reconciliation",
                        "textarea",
                        (
                            "Enter the exact Conservative revenue, net margin, owner profit, and team. "
                            "Provide a service-only revenue bridge and implied annual costs, preserving "
                            "the distinction between canonical outputs and an illustrative sales mix."
                        ),
                        (
                            "Conservative revenue is $95,000 with a 32% net margin and $30,400 annual "
                            "owner net profit; team capacity is 1 FT + 2 C. An illustrative bridge "
                            "is $6,000 monthly retainers for 12 months plus $23,000 project fees. "
                            "Implied total annual costs are $64,600; award receipts are $0."
                        ),
                    ),
                    field(
                        "Base scenario reconciliation",
                        "textarea",
                        (
                            "Enter the exact Base revenue, net margin, owner profit, and team. "
                            "Reconcile a complete annual delivery-cost envelope and a repeatable "
                            "retainer mix without adding contingent recoveries to recognized "
                            "service revenue."
                        ),
                        (
                            "Base revenue is $487,500, margin is 45.0%, and annual owner net profit "
                            "is $219,375 with 1 FT + 2 C. Five $7,500 monthly retainers generate "
                            "$450,000; projects add $37,500. Costs total $268,125, comprising "
                            "$72,000 overhead, $144,000 delivery labor, $36,000 project costs, "
                            "and $16,125 administration."
                        ),
                    ),
                    field(
                        "Scaled Small-Team scenario reconciliation",
                        "textarea",
                        (
                            "Enter the exact Scaled revenue, net margin, owner profit, and staffing. "
                            "Identify the capacity assumptions supporting higher contribution, and "
                            "calculate implied costs without extending the scenario beyond "
                            "the specified five-person team."
                        ),
                        (
                            "Scaled revenue is $880,000 at 58% net margin, producing $510,400 annual "
                            "owner net profit with 2 FT + 3 C, five people total. Eight $8,750 "
                            "monthly retainers generate $840,000; projects add $40,000. Implied costs "
                            "are $369,600, requiring reusable pipelines and measured delivery "
                            "efficiency rather than assumed award proceeds."
                        ),
                    ),
                    field(
                        "Recognized revenue and retained-share boundary",
                        "textarea",
                        (
                            "Distinguish gross service billings, pass-through amounts, government "
                            "collections, statutory awards, and the operator's legally attributable "
                            "interest. Document ASC 606 principal-agent treatment for service contracts "
                            "and the accountant's separate treatment of any award."
                        ),
                        (
                            "A fictional matter produces $10 million in government collections, but "
                            "the operator records none of that principal as revenue. A $40,000 "
                            "research assignment contains $10,000 of agent-arranged pass-through "
                            "services; under the assumed net presentation, service revenue is "
                            "$30,000 and retained_share equals 0.75. Statutory receipts remain "
                            "separately evaluated."
                        ),
                    ),
                    field(
                        "Monthly overhead and full operating commitment",
                        "textarea",
                        (
                            "Identify recurring overhead within the stated $1,500–$9,500 range, then "
                            "add labor, delivery, and administrative obligations separately. Explain "
                            "which commitments activate only after collections and which continue "
                            "during a client acquisition drought."
                        ),
                        (
                            "Base overhead is $6,000 monthly, within the stated range. Allocated labor "
                            "is $12,000, project costs average $3,000, and administration averages "
                            "$1,343.75, producing total monthly costs of $22,343.75. Average Base "
                            "revenue is $40,625 monthly. These annualized allocations describe "
                            "steady-state operations, not the initial pre-client burn."
                        ),
                    ),
                    field(
                        "Startup capital and first-deal runway",
                        "textarea",
                        (
                            "Select startup capital within $10,000–$45,000 and deduct one-time launch "
                            "spending. Calculate pre-client runway against the four-to-twelve-month "
                            "first-deal range, including a concrete cost reduction when the initial "
                            "funding cannot cover that interval."
                        ),
                        (
                            "Starting capital of $30,000 less $6,000 setup leaves $24,000. At $6,000 "
                            "monthly pre-client burn, runway is four months, leaving an eight-month "
                            "gap against a twelve-month first deal. Reducing committed burn to "
                            "$2,000 extends runway to twelve months; paid contractors begin only "
                            "after funded client work arrives."
                        ),
                    ),
                    field(
                        "Restricted advances and reserve release",
                        "textarea",
                        (
                            "Separate vendor advances, counsel-controlled trust funds, refundable "
                            "balances, and unrestricted reserves. Specify ownership, refund duties, "
                            "recognition timing, and release conditions rather than treating "
                            "all deposited funds as productive operating capital."
                        ),
                        (
                            "A firm pays a $15,000 advance covering two future service months. "
                            "The ledger initially records a contract liability, subject to the "
                            "actual cancellation terms. The operator excludes the refundable "
                            "balance from discretionary reserves. Counsel's client trust account "
                            "remains outside operator custody, and no interest benefit is assumed."
                        ),
                    ),
                    field(
                        "Collections lag and working-capital stress",
                        "textarea",
                        (
                            "Calculate the cash gap caused by delayed invoices using full operating "
                            "commitments rather than overhead alone. Identify minimum unrestricted "
                            "cash, contractor payment dates, receivable aging triggers, and a "
                            "specific stop-work response."
                        ),
                        (
                            "At Base monthly costs of $22,343.75, a conservative two-month "
                            "collection interruption requires $44,687.50 before any incremental "
                            "project spending. A $50,000 unrestricted reserve leaves $5,312.50 "
                            "above that stress requirement. Invoices exceeding 30 days trigger "
                            "partner outreach; new unfunded deliverables pause under the "
                            "engagement's agreed suspension clause."
                        ),
                    ),
                    field(
                        "Non-intervention, dismissal, and zero-recovery tree",
                        "textarea",
                        (
                            "Build a complete outcome tree with explicit denominators for "
                            "non-intervention and dismissal rates. Treat Granston-era dismissal "
                            "policy as context, not a universal rate, and distinguish screening "
                            "assumptions from observed case outcomes."
                        ),
                        (
                            "An illustrative 100-filed-matter stress cohort assumes 80 non-interventions. "
                            "Within those 80, eight dismissals imply 10%; 60 other matters yield "
                            "no recovery and 12 recover. Of 20 intervention matters, four yield "
                            "zero and 16 recover. Total zero-recovery outcomes are 72; these "
                            "are scenario assumptions, not published DOJ frequencies."
                        ),
                    ),
                    field(
                        "Award timing and cash exclusion schedule",
                        "textarea",
                        (
                            "Maintain a separate contingent-upside schedule showing route, statutory "
                            "range, counsel assessment, expected delay, and collection status. "
                            "Exclude uncollected awards from payroll coverage, operating reserves, "
                            "canonical revenue bridges, and debt service calculations."
                        ),
                        (
                            "The upside schedule assumes potential realization in years two through "
                            "five or later, with FCA investigations potentially remaining under "
                            "extended seal. All five annual operating budgets assign uncollected "
                            "awards $0 spendable cash. SEC and IRS matters follow their own "
                            "confidentiality regimes rather than being described as FCA sealed dockets."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Approve the model only when all three canonical profits reconcile exactly, "
                    "restricted balances are excluded from runway, and both the launch plan and "
                    "steady-state commitments survive the stated zero-award cash stress."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "End-to-End Execution, Idempotent Ledger & QA Pre-Flight Sheet",
                "purpose": (
                    "Turn an authorized research assignment into a reproducible, counsel-ready "
                    "evidence package without corrupting provenance or leaking restricted facts. "
                    "Define immutable acquisition records, reversible transformations, duplicate "
                    "controls, human verification, and invoice events that survive reruns and "
                    "independent reconstruction."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign a non-descriptive matter identifier before acquisition, then record "
                        "the source release, retrieval time, authority, checksum, and custodian. "
                        "Preserve source bytes separately from normalized working copies so later "
                        "transformations never overwrite the original evidence."
                    ),
                    (
                        "Run ingestion and entity resolution with stable keys and explicit versioning. "
                        "Treat repeat delivery as a replay, not a new business event. "
                        "Quarantine schema changes and unresolved identifiers before they affect "
                        "rankings, evidence exports, or invoices."
                    ),
                    (
                        "Make every allegation traceable to source records and every calculation "
                        "reproducible from a recorded configuration. Keep analyst interpretation "
                        "visibly separate from source text, and require a second person to "
                        "challenge material factual assertions."
                    ),
                    (
                        "Use restricted workspaces for counsel-controlled material and segregate "
                        "ordinary sales records from matter evidence. Before transmission, verify "
                        "recipients, authorization, export contents, and attachment metadata; avoid "
                        "external processing services unless the engagement specifically permits them."
                    ),
                    (
                        "Close delivery only after artifact counts, hashes, claim references, "
                        "permissions, and commercial milestones reconcile. Record failed checks "
                        "as open work rather than silently repairing the evidence history or "
                        "marking an incomplete package as accepted."
                    ),
                ],
                "fields": [
                    field(
                        "Matter identifier and authorization envelope",
                        "textarea",
                        (
                            "Assign a stable opaque matter identifier and capture who authorized "
                            "research, permitted sources, data classes, workspace members, and "
                            "delivery scope. Keep subject names and allegation language out "
                            "of broadly visible project identifiers."
                        ),
                        (
                            "Matter M048-001 covers a 20-hour public-source corroboration assignment "
                            "authorized by counsel's engagement email. Workspace access includes "
                            "one lead analyst, one reviewer, and two designated firm contacts. "
                            "The sales board contains only M048-001 and contract value; it "
                            "contains no subject identity, allegations, or sealed-case status."
                        ),
                    ),
                    field(
                        "Acquisition manifest and source integrity",
                        "textarea",
                        (
                            "Record retrieval timestamp, source URL or licensed delivery reference, "
                            "release identifier, byte count, checksum algorithm, and acquisition "
                            "authority. Explain how replacement releases are preserved without "
                            "erasing earlier source versions."
                        ),
                        (
                            "The manifest records a CMS release downloaded at 14:20 UTC, its "
                            "published release label, 184,320,000 bytes, and the full machine-generated "
                            "SHA-256 digest in a dedicated checksum field. A corrected release "
                            "receives a second immutable artifact identifier; the original remains "
                            "available with its superseded status and retrieval history."
                        ),
                    ),
                    field(
                        "Normalization specification and excluded records",
                        "textarea",
                        (
                            "Document column mappings, types, suppression handling, units, rounding, "
                            "and exclusion reasons. Identify source changes that stop processing "
                            "rather than allowing coercion to create misleading zeros or "
                            "silently shift monetary scales."
                        ),
                        (
                            "The parser stores payment amounts as integer cents and provider "
                            "identifiers as strings. Suppressed counts remain explicitly suppressed "
                            "rather than becoming zero. Of 120,000 rows, 350 missing stable "
                            "identifiers enter quarantine. A changed payment-column name stops "
                            "the run until the reviewer approves a versioned mapping update."
                        ),
                    ),
                    field(
                        "Entity resolution and collision handling",
                        "textarea",
                        (
                            "Specify authoritative identifiers, match precedence, temporal validity, "
                            "and collision handling across CMS, Open Payments, procurement, "
                            "and manifests. Prevent name similarity alone from combining "
                            "unrelated organizations or assigning conduct to the wrong person."
                        ),
                        (
                            "CMS records join through validated NPI values where appropriate; "
                            "procurement entities use UEI and documented historical crosswalks. "
                            "Two similarly named importers share no verified identifier, so "
                            "they remain separate. A reviewer resolves 12 candidate matches "
                            "and rejects five; rejected pairs persist in a versioned "
                            "do-not-merge register."
                        ),
                    ),
                    field(
                        "Idempotent event and artifact ledger",
                        "textarea",
                        (
                            "Define stable deduplication keys, transaction boundaries, retry behavior, "
                            "and immutable event references. Explain how repeated ingestion, "
                            "delivery acknowledgments, or invoice requests avoid duplicate "
                            "evidence records and duplicate commercial charges."
                        ),
                        (
                            "A SQLite ledger enforces a unique tuple of matter identifier, "
                            "source release, source-record key, and transformation version. "
                            "Replaying 5,000 previously processed records inserts zero duplicates. "
                            "Invoice events use a separate unique matter-period-milestone key; "
                            "a retried delivery acknowledgment references the original event "
                            "instead of generating a second bill."
                        ),
                    ),
                    field(
                        "Anomaly reproducibility and negative controls",
                        "textarea",
                        (
                            "Capture scoring parameters, cohort membership, software version, "
                            "random seed where used, and negative-control outcomes. Require "
                            "explanations for unstable rankings before an anomaly is represented "
                            "as a priority investigative lead."
                        ),
                        (
                            "Model version 1.3 ranks 420 providers using specialty-adjusted "
                            "service intensity. A shuffled-provider negative control produces "
                            "no stable priority cluster. Changing the minimum cohort from "
                            "30 to 40 removes three of 18 leads; the memo reports "
                            "that sensitivity and preserves both output manifests for review."
                        ),
                    ),
                    field(
                        "Evidence assertion and contradiction matrix",
                        "textarea",
                        (
                            "Link each material assertion to exact source locations, supporting "
                            "records, contradictory evidence, and reviewer disposition. Distinguish "
                            "verbatim source content, computed findings, witness statements, "
                            "and counsel's legal analysis in the delivered package."
                        ),
                        (
                            "Assertion A-07 reports unusually high service intensity and cites "
                            "source rows 1842–1859 plus calculation C-14. A public specialty "
                            "description supplies a plausible alternative explanation. The "
                            "reviewer changes the conclusion from suspected false billing "
                            "to unresolved utilization anomaly and assigns counsel a targeted "
                            "corroboration question."
                        ),
                    ),
                    field(
                        "Restricted export and recipient verification",
                        "textarea",
                        (
                            "List export recipients, counsel authorization, encryption method, "
                            "attachment inventory, redaction checks, and access expiration. "
                            "Specify the conditions that stop delivery when a package "
                            "contains seal-sensitive or improperly scoped material."
                        ),
                        (
                            "Package P-004 contains one memo and three evidence appendices. "
                            "Counsel confirms two named recipients through the existing "
                            "engagement channel. The reviewer removes internal subject "
                            "aliases from document properties, verifies redactions, and "
                            "sets seven-day access expiry. A mismatched recipient address "
                            "stops transmission until independently corrected."
                        ),
                    ),
                    field(
                        "Delivery acceptance and invoice reconciliation",
                        "textarea",
                        (
                            "Connect contract milestones to accepted artifacts, invoice amounts, "
                            "revenue treatment, and collection status. Separate evidence revisions "
                            "from new paid scope so a rerun or corrected file "
                            "cannot accidentally create additional billable events."
                        ),
                        (
                            "The monthly contract requires one memo and one counsel "
                            "review call for $7,500. Acceptance event D-011 references "
                            "the artifact manifest and meeting record. A corrected "
                            "appendix replaces the deliverable version without changing "
                            "the milestone key. Invoice I-011 remains $7,500, with "
                            "collection tracked separately from delivery acceptance."
                        ),
                    ),
                    field(
                        "Failed-check register and recovery rehearsal",
                        "textarea",
                        (
                            "Record blocking defects, severity, owner, correction evidence, "
                            "and rerun results. Include a restoration rehearsal demonstrating "
                            "that evidence, ledger uniqueness, and access restrictions survive "
                            "a failed job or workstation loss."
                        ),
                        (
                            "A checksum mismatch blocks one downloaded archive and every "
                            "dependent output. The operator retrieves a fresh authorized "
                            "copy, preserves the failed acquisition record, and reruns "
                            "processing. A separate restore test rebuilds 24 artifacts "
                            "from backup with matching hashes and confirms that replay "
                            "creates no duplicate invoices."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Release the package only after provenance, entity matching, assertions, "
                    "recipient authorization, duplicate prevention, and invoice totals pass "
                    "documented checks; every remaining evidentiary limitation must appear "
                    "in the counsel-facing delivery record."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Statutory, Licensing, Contract Addendum & Compliance Audit",
                "purpose": (
                    "Translate statutory routes and professional boundaries into concrete operating "
                    "controls. Reserve legal judgments and filings for licensed counsel, preserve "
                    "FCA seal procedures, distinguish award programs accurately, and prevent "
                    "service contracts from implying transferable awards, protected status, or "
                    "permission to acquire restricted evidence."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Assign licensed counsel to select the cause of action, claimant, forum, "
                        "filing sequence, and required disclosures. The analytics team supplies "
                        "verified factual work and source records; it does not independently "
                        "file complaints or represent a relator."
                    ),
                    (
                        "For an FCA route, document statutory eligibility, first-to-file exposure, "
                        "pleading sufficiency, service requirements, and seal instructions. "
                        "Treat the statutory initial seal period and every court extension "
                        "as active handling requirements rather than a marketing timeline."
                    ),
                    (
                        "For SEC, IRS, or CFTC routes, create separate eligibility and "
                        "submission checklists. Do not transfer FCA award percentages, seal "
                        "procedures, or originality standards across programs; have counsel "
                        "verify the governing provisions and current official forms."
                    ),
                    (
                        "Review engagement language for unauthorized legal practice, professional "
                        "fee-sharing restrictions, evidence ownership, confidentiality, access "
                        "rights, and refund duties. Specify fixed or hourly analytics "
                        "compensation without assuming a vendor may purchase a statutory "
                        "award interest."
                    ),
                    (
                        "Recheck current statutes, regulations, court orders, and local "
                        "professional rules before each filing or sensitive disclosure. "
                        "Record the authority consulted, reviewing lawyer, unresolved issue, "
                        "and required operational restriction instead of relying on "
                        "a generic certification."
                    ),
                ],
                "fields": [
                    field(
                        "Licensed counsel and reserved decisions",
                        "textarea",
                        (
                            "Identify counsel's licensed jurisdiction, engagement scope, filing "
                            "responsibility, and escalation contact. List the legal determinations "
                            "reserved to counsel and the factual services the analytics "
                            "operator may deliver under the signed engagement."
                        ),
                        (
                            "The engagement assigns counsel responsibility for claimant "
                            "eligibility, causes of action, pleading, filing, service, "
                            "and communications with agencies. The operator prepares "
                            "reproducible calculations and source indexes for $7,500 "
                            "monthly. Counsel verifies applicable admission requirements "
                            "before litigation; the vendor does not describe its "
                            "analysts as legal representatives."
                        ),
                    ),
                    field(
                        "FCA seal, filing, and government service",
                        "textarea",
                        (
                            "Translate 31 U.S.C. § 3730(b)(2) into a counsel-owned "
                            "filing checklist. Include in-camera filing, initial seal "
                            "duration, government service materials, defendant-service restrictions, "
                            "and controls for court-ordered extensions and disclosure permissions."
                        ),
                        (
                            "Counsel files the complaint in camera and under seal "
                            "for at least 60 days, serving the government with "
                            "the complaint and substantially all material evidence "
                            "and information as required. The defendant is not "
                            "served until the court orders. Analysts follow each "
                            "extension order and make no public case announcement."
                        ),
                    ),
                    field(
                        "Public disclosure, first-to-file, and particularity",
                        "textarea",
                        (
                            "Record counsel's analysis under 31 U.S.C. §§ 3730(e)(4) "
                            "and 3730(b)(5), plus Federal Rule of Civil Procedure "
                            "9(b). Identify unresolved factual gaps and jurisdiction-specific "
                            "pleading standards without reducing eligibility to a "
                            "dataset originality score."
                        ),
                        (
                            "Counsel finds that an earlier news report may disclose "
                            "substantially the same allegations, while the proposed "
                            "relator has no documented qualifying original-source "
                            "contribution. Representative transactions also remain "
                            "missing. The matter receives a hold on filing work, "
                            "a lawful corroboration plan, and a capped research "
                            "budget rather than an eligibility certificate."
                        ),
                    ),
                    field(
                        "FCA award range and dismissal exposure",
                        "textarea",
                        (
                            "Distinguish intervened and non-intervened FCA award ranges "
                            "and record exclusions, reductions, government dismissal "
                            "authority, and court-dependent seal consequences. Do not "
                            "promise an award percentage or describe every seal "
                            "violation as automatic forfeiture."
                        ),
                        (
                            "Under 31 U.S.C. § 3730(d), ordinary ranges are "
                            "15%–25% when the government proceeds and 25%–30% "
                            "when it does not, subject to statutory qualifications. "
                            "Counsel separately assesses dismissal under § 3730(c)(2)(A), "
                            "including applicable Polansky procedures. Seal breaches "
                            "can cause serious sanctions and case loss; consequences "
                            "depend on governing law and facts."
                        ),
                    ),
                    field(
                        "SEC Form TCR and award eligibility",
                        "textarea",
                        (
                            "Document counsel's SEC submission route, original-information "
                            "analysis, voluntary-submission timing, monetary threshold, "
                            "and award-application tracking. Distinguish independent "
                            "analysis eligibility from assumptions that any "
                            "public-data ranking earns a statutory award."
                        ),
                        (
                            "Counsel evaluates a proposed Form TCR under 15 U.S.C. "
                            "§ 78u-6 and 17 CFR §§ 240.21F-2 through 240.21F-4. "
                            "Covered actions generally require sanctions exceeding "
                            "$1 million; potential awards are 10%–30% of qualifying "
                            "collections. The file records originality, exclusions, "
                            "submission timing, and the later award-claim deadline "
                            "as separate issues."
                        ),
                    ),
                    field(
                        "IRS Form 211 threshold and evidence routing",
                        "textarea",
                        (
                            "Record the taxpayer nexus, evidence of underpayment, "
                            "amount-in-dispute analysis, individual income threshold "
                            "where relevant, and counsel's Form 211 preparation "
                            "plan. Distinguish mandatory-program eligibility from "
                            "discretionary awards and eventual proceeds collection."
                        ),
                        (
                            "Counsel evaluates 26 U.S.C. § 7623(b), whose "
                            "15%–30% framework generally requires proceeds in "
                            "dispute exceeding $2 million. For an individual "
                            "taxpayer, gross income must exceed $200,000 for "
                            "a relevant taxable year. The operator supplies "
                            "lawfully sourced transaction analysis; counsel "
                            "prepares Form 211 and evaluates reductions or "
                            "alternate treatment."
                        ),
                    ),
                    field(
                        "CFTC route and cross-program separation",
                        "textarea",
                        (
                            "Where derivatives conduct is relevant, record counsel's "
                            "CFTC route under its distinct statute and regulations. "
                            "Separate agency jurisdiction, submission records, "
                            "related-action treatment, confidentiality instructions, "
                            "and award calculations from FCA, SEC, and "
                            "IRS assumptions."
                        ),
                        (
                            "A derivatives-manipulation lead goes to counsel "
                            "for analysis under 7 U.S.C. § 26 and "
                            "17 CFR Part 165. The CFTC framework generally "
                            "uses a sanctions threshold exceeding $1 million "
                            "and a 10%–30% award range. A separate submission "
                            "register prevents treating one factual package "
                            "as automatically eligible across agencies."
                        ),
                    ),
                    field(
                        "Compensation addendum and award-interest restriction",
                        "textarea",
                        (
                            "Draft concrete compensation terms covering service "
                            "fees, pass-through expenses, contingent interests, "
                            "and professional-rule review. Require counsel "
                            "to assess applicable state fee-sharing and "
                            "unauthorized-practice rules before any proposed "
                            "recovery-linked arrangement."
                        ),
                        (
                            "The addendum states: 'Analytics fees are $7,500 "
                            "monthly for the defined services and are "
                            "payable independently of litigation outcomes. "
                            "This agreement assigns no statutory award "
                            "and no legal-fee interest.' Counsel reviews "
                            "applicable state rules corresponding to "
                            "professional-conduct Rule 5.4 before considering "
                            "any different compensation structure."
                        ),
                    ),
                    field(
                        "Evidence access, privacy, and reporting rights",
                        "textarea",
                        (
                            "Identify lawful collection authority, sensitive-data "
                            "restrictions, protective orders, privilege handling, "
                            "and reporting-rights language. Avoid treating "
                            "an engagement or confidentiality clause as "
                            "permission to access unrelated systems or "
                            "impede protected agency communications."
                        ),
                        (
                            "Counsel limits the pilot to public and licensed "
                            "data, with no patient-level protected information. "
                            "Any later health-data work requires a documented "
                            "HIPAA analysis under 45 CFR Parts 160 and "
                            "164. The confidentiality addendum preserves "
                            "applicable reporting rights and is reviewed "
                            "against SEC Rule 21F-17's anti-impeding requirements."
                        ),
                    ),
                    field(
                        "Seal incident and preservation response",
                        "textarea",
                        (
                            "Define immediate steps for suspected disclosure, "
                            "misdirected transmission, or unauthorized access. "
                            "Preserve evidence, restrict further dissemination, "
                            "notify counsel, and reserve court or agency "
                            "communications for the responsible lawyer "
                            "under applicable duties."
                        ),
                        (
                            "An analyst discovers that a restricted attachment "
                            "went to an unintended recipient. They disable "
                            "the access link, preserve the message and "
                            "access log, and immediately notify counsel. "
                            "Counsel determines required court action and "
                            "recipient instructions. The operator neither "
                            "deletes the audit trail nor publicly explains "
                            "the underlying sealed allegations."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Proceed only with counsel-owned filing instructions, documented program "
                    "eligibility analysis, enforceable service terms, and a tested restricted "
                    "disclosure response; unresolved legal questions remain assigned to "
                    "counsel with explicit work limits."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation Pipeline, Acquisition Flywheel & Risk Fallback Tracker",
                "purpose": (
                    "Automate repeatable acquisition, normalization, and evidence assembly while "
                    "keeping legal conclusions and sensitive disclosures under human control. "
                    "Build a counsel acquisition loop using sanitized capability demonstrations, "
                    "measure useful output rather than lead volume, and define practical "
                    "fallbacks for source failures."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Prioritize one reproducible pipeline before adding more datasets. "
                        "Use authorized APIs or published downloads, documented "
                        "rate limits, stable source versions, and bounded "
                        "retry behavior so automation improves evidence quality "
                        "instead of amplifying acquisition mistakes."
                    ),
                    (
                        "Separate deterministic calculations from interpretive drafting. "
                        "Require source citations and reviewer approval for "
                        "every material assertion, and prohibit automated "
                        "filing, subject contact, or public accusation based "
                        "solely on an anomaly score or generated summary."
                    ),
                    (
                        "Use public or synthetic examples to demonstrate "
                        "capability to prospective firms. Track permission "
                        "to contact, qualified meetings, paid pilots, "
                        "retainer conversion, and collection timing without "
                        "exposing sealed matters or promising recoveries "
                        "as a sales tactic."
                    ),
                    (
                        "Define fallback behavior for unavailable sources, "
                        "schema drift, excessive false positives, client "
                        "loss, and counsel rejection. Every fallback "
                        "must state an owner, spending ceiling, "
                        "maximum delay, and the condition for "
                        "resuming ordinary production."
                    ),
                    (
                        "Review automation performance alongside evidence "
                        "accuracy and security events. Retire a "
                        "pipeline when repeated errors consume "
                        "its claimed labor savings, and preserve "
                        "a manual route capable of delivering "
                        "the contracted memo without unsupported "
                        "technical shortcuts."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized source schedule and retry budget",
                        "textarea",
                        (
                            "List CMS, Open Payments, SAM.gov, and licensed "
                            "manifest acquisition schedules with access "
                            "authority and release cadence. Set "
                            "timeouts, rate limits, retry ceilings, "
                            "and ownership for failed or "
                            "changed source deliveries."
                        ),
                        (
                            "The operator checks CMS and Open Payments "
                            "release notices weekly, retrieves SAM.gov "
                            "records through authorized access, and "
                            "imports manifests under a commercial "
                            "license. Each job allows three bounded "
                            "retries before pausing. The lead analyst "
                            "reviews failures the next business day; "
                            "no job bypasses access restrictions "
                            "to maintain freshness."
                        ),
                    ),
                    field(
                        "Stdlib pipeline components and handoff contracts",
                        "textarea",
                        (
                            "Define small ingestion, validation, scoring, "
                            "ledger, and export components with "
                            "explicit inputs and outputs. Specify "
                            "the minimal Python standard-library "
                            "implementation and the checks required "
                            "before each component hands data "
                            "to the next."
                        ),
                        (
                            "The prototype uses urllib.request for "
                            "authorized retrieval, csv and json "
                            "for parsing, decimal for money, "
                            "hashlib for checksums, and sqlite3 "
                            "for event storage. Each component "
                            "emits a manifest containing version, "
                            "row counts, and rejection counts. "
                            "The export component accepts only "
                            "reviewed evidence assertions."
                        ),
                    ),
                    field(
                        "Outlier precision and research-hour yield",
                        "textarea",
                        (
                            "Measure counsel-useful leads against reviewed "
                            "candidates, including false positives "
                            "and hours spent. Define an "
                            "economic threshold for retaining "
                            "a scoring rule rather than "
                            "optimizing for the largest "
                            "possible anomaly queue."
                        ),
                        (
                            "A batch produces 40 candidates; human "
                            "review finds eight sufficiently "
                            "corroborated for counsel discussion, "
                            "a 20% useful-lead rate. Review "
                            "takes 24 hours, or three "
                            "hours per useful lead. A "
                            "revised cohort rule produces six "
                            "useful leads in 12 hours, "
                            "improving yield despite lower "
                            "headline candidate volume."
                        ),
                    ),
                    field(
                        "FOIA and primary-source corroboration queue",
                        "textarea",
                        (
                            "Track targeted public-record requests, "
                            "custodian, statutory route, expected "
                            "limitations, fees, and fallback "
                            "sources. Keep FOIA response "
                            "timing separate from contractual "
                            "delivery promises and protect "
                            "restricted matter details in "
                            "request language."
                        ),
                        (
                            "Counsel approves a narrowly scoped "
                            "request under 5 U.S.C. § 552 "
                            "for identified contract-payment "
                            "records, with a $250 fee "
                            "ceiling. The queue anticipates "
                            "redactions and delays, including "
                            "potential Exemptions 4, 6, "
                            "or 7. The current paid "
                            "memo proceeds using available "
                            "primary records and explicitly "
                            "lists missing corroboration."
                        ),
                    ),
                    field(
                        "Dossier assembly and assertion review",
                        "textarea",
                        (
                            "Specify which dossier sections can "
                            "be assembled automatically and "
                            "which require analyst or "
                            "counsel judgment. Require precise "
                            "citations, contradiction handling, "
                            "and reproducibility before "
                            "generated narrative reaches "
                            "an external recipient."
                        ),
                        (
                            "Automation assembles source inventories, "
                            "entity crosswalks, calculation "
                            "tables, and evidence references. "
                            "The analyst writes factual "
                            "interpretation and the reviewer "
                            "checks every material sentence "
                            "against cited artifacts. Counsel "
                            "alone supplies legal theories. "
                            "A missing citation blocks "
                            "that assertion from the "
                            "export, not merely from "
                            "a footnote list."
                        ),
                    ),
                    field(
                        "Counsel acquisition funnel and paid-pilot offer",
                        "textarea",
                        (
                            "Define the target firm profile, "
                            "permitted outreach channel, "
                            "sanitized demonstration, paid "
                            "pilot scope, and conversion "
                            "metric. Separate historical "
                            "conversion observations from "
                            "launch assumptions and "
                            "avoid subject-specific allegations "
                            "in prospecting."
                        ),
                        (
                            "The launch targets 30 firms "
                            "with relevant public practice "
                            "profiles through individualized "
                            "business outreach. Planning "
                            "assumptions are six meetings, "
                            "two $3,000 paid pilots, "
                            "and one retainer discussion. "
                            "The demonstration uses synthetic "
                            "entities and public methodology. "
                            "These funnel counts are "
                            "targets, not reported sales "
                            "or expected award outcomes."
                        ),
                    ),
                    field(
                        "Reuse, confidentiality, and referral flywheel",
                        "textarea",
                        (
                            "Identify reusable methods, "
                            "client-owned deliverables, "
                            "restricted evidence, and "
                            "permitted case-study content. "
                            "Define how satisfied "
                            "clients may introduce "
                            "other firms without "
                            "sharing protected matter "
                            "details or creating "
                            "unreviewed compensation obligations."
                        ),
                        (
                            "After an accepted pilot, "
                            "the firm may introduce "
                            "the operator to another "
                            "practice partner using a "
                            "generic capability statement. "
                            "No referral payment is "
                            "offered. Reusable parsing "
                            "code remains separate from "
                            "client evidence, and the "
                            "operator publishes neither "
                            "subject names nor matter "
                            "outcomes without documented "
                            "authority and counsel review."
                        ),
                    ),
                    field(
                        "Seal-sensitive tooling and third-party boundaries",
                        "textarea",
                        (
                            "Document where restricted data "
                            "may be processed, which "
                            "external services are "
                            "authorized, retention settings, "
                            "access logs, and "
                            "incident ownership. Treat "
                            "uploading client material "
                            "as a disclosure decision "
                            "rather than a routine "
                            "formatting operation."
                        ),
                        (
                            "Restricted documents remain "
                            "in the counsel-approved "
                            "workspace with named-user "
                            "access and logged exports. "
                            "Public demonstrations run "
                            "separately. Analysts do "
                            "not upload matter text "
                            "to external drafting "
                            "services. Any proposed "
                            "service requires documented "
                            "client authority, reviewed "
                            "retention terms, and a "
                            "tested deletion and "
                            "incident-response procedure."
                        ),
                    ),
                    field(
                        "Source outage and quality fallback",
                        "textarea",
                        (
                            "Define fallback sources, "
                            "maximum stale-data age, "
                            "manual review scope, "
                            "spending cap, and "
                            "client communication for "
                            "a failed source "
                            "or deteriorating model. "
                            "Prohibit silent substitution "
                            "of incomplete or "
                            "incompatible releases."
                        ),
                        (
                            "If the current CMS "
                            "download fails validation, "
                            "the analyst may use "
                            "the prior verified "
                            "release only with "
                            "its date prominently "
                            "stated and counsel's "
                            "scope agreement. Manual "
                            "triage is capped at "
                            "six hours and $420 "
                            "internal cost. New "
                            "comparisons spanning incompatible "
                            "release definitions remain "
                            "paused."
                        ),
                    ),
                    field(
                        "Automation return and retirement trigger",
                        "textarea",
                        (
                            "Compare build effort, "
                            "maintenance, verification, "
                            "and avoided labor "
                            "using the same "
                            "cost basis. Define "
                            "the error threshold "
                            "and payback horizon "
                            "that justify maintaining, "
                            "revising, or retiring "
                            "an automated component."
                        ),
                        (
                            "A dossier assembler costs "
                            "40 hours at $70, "
                            "or $2,800, to build. "
                            "It saves ten monthly "
                            "hours but requires "
                            "two maintenance hours, "
                            "yielding $560 monthly "
                            "net labor savings "
                            "and five-month payback. "
                            "Two material citation "
                            "errors in one month "
                            "trigger manual assembly "
                            "until the defect "
                            "is resolved."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Scale automation only after a reproducible pilot demonstrates useful "
                    "lead yield, controlled disclosures, positive measured labor economics, "
                    "and a funded manual fallback; outreach must use authorized, "
                    "nonrestricted demonstration material."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod KPI Scorecard & Exit-Readiness Ledger",
                "purpose": (
                    "Convert the operating model into a funded first-month sprint with accountable "
                    "owners and measurable evidence quality. Track retainer collections, capacity, "
                    "runway, and client concentration while preparing transferable business "
                    "records that exclude restricted case materials and speculative valuations "
                    "of uncollected awards."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the first 30 days as infrastructure, validation, "
                        "and commercial discovery rather than a promise "
                        "of a closed engagement. Preserve the "
                        "four-to-twelve-month first-deal assumption and fund "
                        "only work that fits the current "
                        "unrestricted launch reserve."
                    ),
                    (
                        "Assign one accountable owner to each deliverable, "
                        "review task, and cash decision. Translate "
                        "the canonical staffing labels into "
                        "funded capacity and actual contractor "
                        "commitments; do not assume a "
                        "contractor count represents unlimited "
                        "or full-time availability."
                    ),
                    (
                        "Publish a weekly scorecard separating activity, "
                        "quality, commercial conversion, earned revenue, "
                        "collections, and cash runway. Count "
                        "a metric only when its "
                        "supporting artifact exists, and "
                        "mark missed targets as missed "
                        "rather than redefining success."
                    ),
                    (
                        "Prepare an exit ledger that distinguishes "
                        "owned software, reusable methods, "
                        "assignable contracts, restricted client "
                        "materials, and contingent personal "
                        "rights. Require counsel review "
                        "before buyer disclosure or "
                        "transfer, and do not "
                        "assume statutory interests are "
                        "saleable business assets."
                    ),
                    (
                        "End the sprint with an evidence-based "
                        "continue, narrow, or pause "
                        "decision. Keep the canonical "
                        "annual scenarios as planning "
                        "benchmarks while using actual "
                        "collections, delivery capacity, "
                        "and source quality to "
                        "determine the next month's "
                        "authorized spending."
                    ),
                ],
                "fields": [
                    field(
                        "Days 1–7 foundation and spending ceiling",
                        "textarea",
                        (
                            "Set first-week deliverables for "
                            "engagement design, counsel "
                            "review, source selection, "
                            "workspace setup, and "
                            "budget controls. Identify "
                            "the owner and "
                            "acceptance artifact for "
                            "each item without "
                            "assuming an immediate "
                            "paying client."
                        ),
                        (
                            "The founder owns a "
                            "one-source pilot specification, "
                            "draft service agreement, "
                            "and $30,000 capital "
                            "ledger. Week-one spending "
                            "is capped at $2,500 "
                            "within the $6,000 "
                            "setup allowance. Acceptance "
                            "requires a counsel-reviewed "
                            "scope, authorized source "
                            "record, and restricted "
                            "workspace test, not "
                            "a completed filing "
                            "or signed retainer."
                        ),
                    ),
                    field(
                        "Days 8–14 reproducible demonstration",
                        "textarea",
                        (
                            "Define a narrow demonstration "
                            "dataset, reproducibility "
                            "test, independent "
                            "challenge, and "
                            "sanitized presentation. "
                            "Specify what counts "
                            "as a usable "
                            "capability demonstration "
                            "while preventing "
                            "unverified public "
                            "allegations or "
                            "unauthorized disclosures."
                        ),
                        (
                            "The analyst builds one "
                            "CMS cohort using "
                            "synthetic subject labels "
                            "in the external "
                            "presentation. A contractor "
                            "receives six funded "
                            "review hours to "
                            "challenge normalization "
                            "and alternative explanations. "
                            "Success means identical "
                            "rerun outputs, traceable "
                            "calculations, and a "
                            "sanitized methodology memo; "
                            "it does not mean "
                            "identifying fraud."
                        ),
                    ),
                    field(
                        "Days 15–21 counsel discovery and pilot scope",
                        "textarea",
                        (
                            "Set targeted outreach, "
                            "meeting, and "
                            "proposal goals "
                            "with a defined "
                            "paid deliverable. "
                            "Capture buyer "
                            "objections and "
                            "budget evidence "
                            "without converting "
                            "informal interest "
                            "into booked "
                            "revenue or "
                            "a forecast "
                            "award."
                        ),
                        (
                            "The founder contacts "
                            "15 selected firms "
                            "and seeks three "
                            "discovery meetings. "
                            "The proposed pilot "
                            "costs $3,000 for "
                            "a capped 20-hour "
                            "corroboration memo. "
                            "Meeting notes record "
                            "practice fit, purchasing "
                            "authority, and evidence "
                            "requirements. An interested "
                            "partner without a "
                            "signed scope remains "
                            "a prospect, with "
                            "$0 earned revenue."
                        ),
                    ),
                    field(
                        "Days 22–30 acceptance and next-month decision",
                        "textarea",
                        (
                            "List month-end "
                            "artifacts, "
                            "unresolved "
                            "defects, "
                            "commercial "
                            "results, "
                            "and cash "
                            "remaining. "
                            "Define the "
                            "conditions "
                            "for continuing "
                            "outreach, "
                            "narrowing the "
                            "offer, or "
                            "pausing spend "
                            "when the "
                            "launch has "
                            "not produced "
                            "a contract."
                        ),
                        (
                            "At day 30, "
                            "the operator "
                            "has one "
                            "validated demonstration, "
                            "four counsel "
                            "meetings, and "
                            "no signed "
                            "pilot. With "
                            "$22,000 remaining "
                            "after $6,000 "
                            "setup and "
                            "$2,000 operating "
                            "spend, they "
                            "continue targeted "
                            "outreach at "
                            "the $2,000 "
                            "monthly ceiling. "
                            "The result "
                            "is launch "
                            "readiness, not "
                            "a completed "
                            "first deal."
                        ),
                    ),
                    field(
                        "Pod roles and funded delivery capacity",
                        "textarea",
                        (
                            "Translate 1 FT + 2 C "
                            "and 2 FT + 3 C "
                            "into responsibilities, "
                            "available hours, "
                            "review coverage, "
                            "and funded "
                            "commitments. "
                            "Distinguish roster "
                            "membership from "
                            "actual billable "
                            "availability "
                            "before accepting "
                            "additional retainers."
                        ),
                        (
                            "The Base pod "
                            "assigns the "
                            "founder 100 "
                            "monthly delivery "
                            "hours and "
                            "two contractors "
                            "80 hours "
                            "each, totaling "
                            "260. Five "
                            "retainers at "
                            "45 hours "
                            "consume 225, "
                            "leaving 35 "
                            "for projects "
                            "and review. "
                            "Any proposal "
                            "exceeding that "
                            "capacity requires "
                            "reduced scope "
                            "or funded "
                            "capacity before "
                            "acceptance."
                        ),
                    ),
                    field(
                        "Weekly cash and acquisition KPI scorecard",
                        "textarea",
                        (
                            "Define exact "
                            "numerators, "
                            "denominators, "
                            "data sources, "
                            "and owners "
                            "for acquisition, "
                            "retention, "
                            "collections, "
                            "and runway "
                            "metrics. "
                            "Keep signed "
                            "contract value, "
                            "earned revenue, "
                            "and banked "
                            "cash separate "
                            "in every "
                            "weekly review."
                        ),
                        (
                            "Week four "
                            "records 30 "
                            "outreach attempts, "
                            "six meetings, "
                            "two proposals, "
                            "and zero "
                            "signed engagements. "
                            "Meeting conversion "
                            "is 20%; "
                            "proposal conversion "
                            "from meetings "
                            "is 33.33%. "
                            "Earned service "
                            "revenue and "
                            "collections both "
                            "remain $0. "
                            "The founder "
                            "reconciles runway "
                            "to the "
                            "bank ledger "
                            "rather than "
                            "pipeline value."
                        ),
                    ),
                    field(
                        "Evidence quality and adverse-outcome scorecard",
                        "textarea",
                        (
                            "Track reproducibility, "
                            "citation accuracy, "
                            "entity-match errors, "
                            "counsel rejection, "
                            "and confidentiality "
                            "incidents using "
                            "stable definitions. "
                            "Keep research "
                            "rejection separate "
                            "from filed-case "
                            "non-intervention "
                            "or dismissal "
                            "so small "
                            "samples cannot "
                            "imply government "
                            "outcome rates."
                        ),
                        (
                            "The pilot checks "
                            "100 material "
                            "citations and "
                            "finds two "
                            "errors, yielding "
                            "98% initial "
                            "accuracy and "
                            "100% after "
                            "documented correction. "
                            "Counsel rejects "
                            "three of "
                            "eight leads "
                            "for insufficient "
                            "corroboration. "
                            "No complaints "
                            "have been "
                            "filed, so "
                            "there is "
                            "no observed "
                            "DOJ outcome "
                            "cohort to "
                            "calculate."
                        ),
                    ),
                    field(
                        "Client concentration and renewal resilience",
                        "textarea",
                        (
                            "Measure client "
                            "concentration, "
                            "renewal dates, "
                            "termination "
                            "notice, "
                            "receivable "
                            "exposure, "
                            "and delivery "
                            "dependency. "
                            "Describe the "
                            "specific staffing "
                            "and cash "
                            "response if "
                            "the largest "
                            "retainer ends "
                            "before replacement "
                            "business "
                            "is collected."
                        ),
                        (
                            "At Base steady "
                            "state, each "
                            "of five "
                            "equal retainers "
                            "represents 20% "
                            "of recurring "
                            "fees. Losing "
                            "one removes "
                            "$7,500 monthly "
                            "revenue. The "
                            "operator reviews "
                            "notice terms, "
                            "reduces uncommitted "
                            "contractor hours, "
                            "and uses "
                            "the unrestricted "
                            "reserve while "
                            "replacing the "
                            "account. "
                            "They do "
                            "not bridge "
                            "the gap "
                            "with projected "
                            "awards."
                        ),
                    ),
                    field(
                        "Exit-readiness assets and transfer restrictions",
                        "textarea",
                        (
                            "Inventory owned "
                            "code, "
                            "documentation, "
                            "licensed "
                            "sources, "
                            "contracts, "
                            "client "
                            "permissions, "
                            "and "
                            "restricted "
                            "evidence. "
                            "Identify "
                            "assignment "
                            "conditions "
                            "and counsel "
                            "review before "
                            "any buyer "
                            "receives "
                            "materials "
                            "or an "
                            "award interest "
                            "appears in "
                            "a sale "
                            "schedule."
                        ),
                        (
                            "The asset register "
                            "lists parser "
                            "code, test "
                            "fixtures, and "
                            "generic operating "
                            "procedures as "
                            "operator-owned. "
                            "Two dataset "
                            "licenses require "
                            "vendor approval "
                            "for transfer; "
                            "five service "
                            "contracts require "
                            "assignment review. "
                            "Restricted client "
                            "evidence stays "
                            "outside the "
                            "initial buyer "
                            "room. "
                            "Contingent statutory "
                            "interests are "
                            "excluded pending "
                            "specific counsel "
                            "analysis."
                        ),
                    ),
                    field(
                        "Owner decision and canonical benchmark ledger",
                        "textarea",
                        (
                            "Record the "
                            "owner's "
                            "continue, "
                            "narrow, "
                            "or pause "
                            "decision "
                            "against "
                            "actual "
                            "cash, "
                            "quality, "
                            "capacity, "
                            "and buyer "
                            "evidence. "
                            "Retain the "
                            "canonical "
                            "score and "
                            "scenario "
                            "benchmarks "
                            "without "
                            "presenting "
                            "them as "
                            "achieved "
                            "results."
                        ),
                        (
                            "The decision ledger "
                            "retains pipeline "
                            "rank #16 "
                            "of 49 "
                            "and score "
                            "92/100, comprising "
                            "24 revenue, "
                            "24 margin, "
                            "20 team, "
                            "12 accessibility, "
                            "and 12 "
                            "automation points. "
                            "Annual profit "
                            "benchmarks remain "
                            "$30,400, "
                            "$219,375, "
                            "and $510,400. "
                            "The owner "
                            "continues a "
                            "cash-capped launch; "
                            "none of "
                            "those benchmarks "
                            "is reported "
                            "as earned."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Close the sprint when all six worksheets have accountable owners, "
                    "cash and quality metrics reconcile to evidence, the next month's "
                    "spend is funded without awards, and transfer restrictions are "
                    "recorded before any external diligence."
                ),
            },
        ],
    }
