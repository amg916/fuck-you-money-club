from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in data-mined qui tam, sec & irs whistleblower analytics, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "CMS Evidence Defects, Rule 9(b), FCA Public-Disclosure Exposure, Award Recoupment, and Retainer Cash Circuit-Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #48, ranked #16 of 49 with a 92/100 Money-to-Manpower Score, "
        "turns forensic analytics into collected law-firm retainers before treating "
        "whistleblower awards as upside. Across its 11 mapped plays, the central "
        "failure is confusing a statistical anomaly, an actionable claim, and "
        "spendable cash. This chapter dismantles evidence contamination, public-disclosure "
        "exposure, seal mistakes, contingent-fee assumptions, contractor overruns, and "
        "procurement pass-through defects. Formula v2.0 annual owner profits remain "
        "$30,400 Conservative, $219,375 Base, and $510,400 Scaled. Operating budgets "
        "exclude uncollected awards, including matters taking 2–5+ years. Concrete "
        "thresholds stop defective dossiers and unprofitable engagements early. "
        "The question's 80% figure is a framing device, not an observed newcomer "
        "failure rate; every numerical circuit-breaker below is an explicit operating assumption."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$95,000",
            "context": "Annual gross operator revenue; collected forensic retainers and project fees",
            "note": "32% net margin; $30,400 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$487,500",
            "context": "Annual gross operator revenue; collected forensic retainers and project fees",
            "note": "45.0% net margin; $219,375 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$880,000",
            "context": "Annual gross operator revenue; collected forensic retainers and project fees",
            "note": "58% net margin; $510,400 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Kill defective evidence before it becomes a defective complaint",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first trap is treating an outlier as a false claim. CMS Part B "
                    "utilization, Part D prescribing, Open Payments transfers, and SAM.gov "
                    "awards describe different units, reporting periods, and legal relationships. "
                    "A high reimbursement total may reflect specialty mix, a referral center, "
                    "or reassigned billing rather than fabricated services. Build cohorts by "
                    "specialty, geography, service code, and reporting year before ranking "
                    "providers. Preserve downloaded bytes, release notes, retrieval timestamps, "
                    "and SHA-256 digests with Python hashlib; never overwrite an earlier "
                    "release with a corrected file. Require a second analyst to reproduce "
                    "every material total from the frozen source. An illustrative investigation "
                    "trigger is a peer-adjusted result above the ninety-ninth percentile "
                    "with at least thirty comparable observations, but that trigger supports "
                    "research, not an allegation. Stop dossier delivery when a material "
                    "identifier join lacks documented corroboration or a suppressed cell "
                    "has been treated as zero. Track reproducibility as accepted calculations "
                    "divided by tested calculations, targeting 100% for cited exhibits. "
                    "The operator sells a defensible analytical process; counsel decides "
                    "whether the facts support falsity, knowledge, materiality, and a "
                    "federal payment nexus. A clean chart without those elements is "
                    "an expensive visualization, not litigation inventory."
                ),
                (
                    "The second trap is assuming public-data synthesis automatically creates "
                    "an eligible relator. Under 31 U.S.C. § 3730(e)(4), substantially the "
                    "same allegations or transactions disclosed through specified public "
                    "channels can expose an FCA action to dismissal unless an exception "
                    "applies or the Government opposes dismissal. The original-source "
                    "analysis is substantive: timestamped downloading alone does not "
                    "establish independent knowledge that materially adds to disclosed "
                    "allegations. FOIA production is not a magic originality certificate. "
                    "Maintain a disclosure chronology separating public records, independently "
                    "obtained observations, voluntary government disclosures, and the proposed "
                    "complaint date. Counsel should also evaluate first-to-file exposure "
                    "under § 3730(b)(5), recognizing that sealed competing cases may "
                    "prevent definitive clearance. The third trap is pleading aggregate "
                    "suspicion without the circumstances required by Federal Rule of "
                    "Civil Procedure 9(b). Build a representative-claim matrix with claimant, "
                    "date, payment program, alleged false statement, supporting record, "
                    "and missing factual links. Circuit standards differ; representative "
                    "claim examples are not a universal mechanical prerequisite. Measure "
                    "claim-link completeness against counsel's jurisdiction-specific checklist "
                    "rather than inventing missing invoices. If public records cannot "
                    "support the required inference, stop the complaint workstream and "
                    "offer a bounded research engagement instead of manufacturing certainty."
                ),
                (
                    "The fourth trap is treating a seal as an ordinary confidentiality "
                    "label. FCA complaints must be filed through licensed relator counsel "
                    "under the statutory seal, served with the required disclosure on "
                    "the Government, and withheld from the defendant until the court "
                    "orders otherwise. The initial statutory period is sixty days; "
                    "extensions can produce investigations lasting years. Keep matter names "
                    "out of shared sales systems, invoices visible to unrelated customers, "
                    "public repositories, and external AI prompts. Use counsel-controlled "
                    "storage, role-based access, encrypted transfer, and a named recipient "
                    "list for every export. One unauthorized external disclosure triggers "
                    "an immediate distribution stop, evidence preservation, and counsel-led "
                    "response. A seal breach can cause sanctions and imperil participation, "
                    "but State Farm v. Rigsby rejects automatic dismissal for every "
                    "violation; do not promise either inevitable forfeiture or automatic "
                    "forgiveness. The fifth trap is acquisition misconduct: borrowed "
                    "credentials, unauthorized portal access, restricted patient exports, "
                    "and fabricated corroboration can overwhelm an otherwise useful "
                    "analysis. Record acquisition authority separately from factual "
                    "relevance. A record's usefulness does not authorize obtaining it. "
                    "Quarantine questionable material without further circulation, preserve "
                    "access logs, and let counsel determine lawful handling and any "
                    "required remedial steps before analysis resumes."
                ),
            ],
            "table": {
                "caption": "Evidence Defect Matrix: CMS, Public Disclosures, Pleading Particularity, and Sealed Material",
                "headers": [
                    "Failure mechanism",
                    "Early-warning measurement",
                    "Immediate circuit-breaker",
                    "Evidence required before resumption",
                ],
                "rows": [
                    [
                        "CMS cohort combines incompatible specialties and billing years",
                        "Any material comparison lacks matching cohort definitions",
                        "Suspend rankings and rebuild the relevant peer groups",
                        "Documented specialty filters, year alignment, and sensitivity calculations",
                    ],
                    [
                        "Provider identifiers merge distinct people or corporate entities",
                        "Any cited identity match lacks independent source corroboration",
                        "Remove affected exhibits from the counsel delivery package",
                        "Verified identifier crosswalk with dates and source references",
                    ],
                    [
                        "Public-source aggregation is mistaken for original-source eligibility",
                        "Disclosure chronology contains no independently supported additive facts",
                        "Stop complaint drafting pending counsel's statutory eligibility analysis",
                        "Written chronology distinguishing public disclosures and independent knowledge",
                    ],
                    [
                        "Aggregate reimbursement patterns replace particularized allegations of falsity",
                        "Counsel's claim matrix contains unresolved material factual links",
                        "Limit engagement to research until deficiencies are addressed",
                        "Jurisdiction-specific pleading assessment supported by authentic underlying records",
                    ],
                    [
                        "Sealed matter identifiers enter broadly accessible collaboration systems",
                        "One unauthorized recipient or public synchronization event appears",
                        "Freeze outbound distribution and preserve relevant access evidence",
                        "Counsel-directed response record and corrected recipient access inventory",
                    ],
                    [
                        "Researcher obtains records through credentials they cannot authorize",
                        "Acquisition log lacks documented permission for restricted access",
                        "Stop collection and quarantine material without further circulation",
                        "Counsel-reviewed acquisition basis and documented permitted handling instructions",
                    ],
                    [
                        "Suppressed CMS observations are silently converted into zeros",
                        "One cited calculation treats suppression as measured absence",
                        "Invalidate affected results and rerun documented sensitivity analysis",
                        "Corrected treatment of suppression with reproducible calculation outputs",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Make the evidence packet survive an adversarial reread",
                "body": (
                    "Experienced teams optimize for reproducible contradictions, not the "
                    "largest anomaly count. These practices reduce paid rework before "
                    "counsel commits to a filing."
                ),
                "items": [
                    "Attach a source-release identifier and SHA-256 digest to each exhibit so later CMS revisions cannot silently change the alleged pattern.",
                    "Keep a disconfirming-evidence worksheet alongside the accusation theory; require analysts to test specialty mix, ownership changes, and billing reassignment.",
                    "Ask counsel for the jurisdiction-specific Rule 9(b) checklist before purchasing additional datasets, then price only the research needed to close identified gaps.",
                    "Use neutral matter codes on contractor invoices and maintain the identity mapping only in counsel-authorized storage with restricted access.",
                ],
            },
        },
        {
            "heading": "2. Reconcile cash without borrowing against a sealed hypothesis",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The sixth trap is booking alleged damages, Government recoveries, "
                    "or projected awards as operator revenue. Formula v2.0 fixes annual "
                    "gross operator revenue at $95,000, $487,500, and $880,000; corresponding "
                    "cost ceilings are $64,600, $268,125, and $369,600. Subtraction produces "
                    "$30,400, $219,375, and $510,400 of annual owner net profit at "
                    "32%, 45.0%, and 58% margins. A transparent illustrative allocation "
                    "uses no award receipts: Conservative has five $1,500 monthly "
                    "retainers plus $5,000 of completed projects; Base has eight $5,000 "
                    "monthly retainers plus $7,500 of completed projects; Scaled has "
                    "ten $7,000 monthly retainers plus $40,000 of completed projects. "
                    "These allocations explain the supplied totals without claiming "
                    "the scorecard prescribed customer counts. Each assumes twelve "
                    "paid months and earned service delivery. An advance retainer "
                    "can create a contract liability until performance occurs. Under "
                    "ASC 606, principal-versus-agent analysis determines gross or net "
                    "presentation for pass-through services. Never include client claim "
                    "value, merchant turnover, or federal contract value in this "
                    "revenue line. Maintain separate ledgers for earned retainers, "
                    "collected cash, refundable advances, reimbursable costs, and realized "
                    "award proceeds; reconcile them monthly before describing the "
                    "business as profitable. Revenue visibility and available cash "
                    "are related measurements, not interchangeable balances."
                ),
                (
                    "The seventh trap is financing payroll with contingent percentages. "
                    "FCA shares generally run 15%–25% when the Government proceeds "
                    "and 25%–30% when it does not, subject to statutory adjustments "
                    "and exclusions. SEC and CFTC programs generally use 10%–30% "
                    "ranges for qualifying awards; IRS § 7623(b) generally uses "
                    "15%–30%, with eligibility thresholds and reduction rules. These "
                    "are distinct programs, not one universal 15%–30% entitlement. "
                    "An analytics vendor has no automatic right to a relator's "
                    "award or counsel's legal fee. State professional-conduct rules, "
                    "including restrictions on sharing legal fees with nonlawyers, "
                    "must shape engagement design. Price ordinary research as documented "
                    "services rather than assuming a percentage arrangement is permissible. "
                    "For sensitivity analysis only, a $1,000,000 recovery multiplied "
                    "by a 20% eligible share equals a $200,000 award before "
                    "applicable deductions. If counsel's valid fee agreement absorbs "
                    "40% and reimbursable case costs equal $20,000, the illustrative "
                    "retained amount is $100,000 before taxes. That amount belongs "
                    "only to the legally entitled recipient. It contributes zero "
                    "to this operator's budget unless entitlement, measurement, and "
                    "receipt are established. An unfavorable judgment, dismissal, "
                    "ineligibility determination, or failed collection instead produces "
                    "zero award revenue after years of work."
                ),
                (
                    "The eighth trap is hiding delivery leakage inside attractive "
                    "headline margins. In the illustrative Base allocation, eight "
                    "clients consuming thirty analyst hours monthly require 240 "
                    "hours before selling, management, and quality control. At a "
                    "$75 blended delivery cost, that is $18,000 monthly, leaving "
                    "$4,343.75 from the Base monthly cost ceiling of $22,343.75 "
                    "for all other expenses. The canonical 1 FT + 2 C "
                    "team therefore needs explicitly contracted capacity; headcount "
                    "alone does not prove deliverability. An extra eight hours "
                    "per client each month adds $57,600 annually, cutting owner "
                    "profit from $219,375 to $161,775 if prices remain unchanged. "
                    "Trigger scope revision when delivery hours exceed 110% of "
                    "the signed allowance for two consecutive months. Suspend "
                    "discretionary enrichment when an undisputed invoice exceeds "
                    "forty-five days, subject to the engagement's notice terms. "
                    "Require a thirteen-week cash forecast excluding all prospective "
                    "awards. Three months of the Base total cost ceiling is "
                    "$67,031.25, above the $10,000–$45,000 startup range; deposits, "
                    "staged hiring, or a smaller initial footprint must bridge "
                    "that gap. The stated $1,500–$9,500 monthly operating-expense "
                    "range does not replace fully loaded scenario costs. "
                    "Refund obligations and committed contractor payments remain "
                    "cash exposures even when revenue collection stops."
                ),
            ],
            "table": {
                "caption": "Formula v2.0 Reconciliation and Cash Leakage Tripwires",
                "headers": [
                    "Economic exposure",
                    "Specific unit calculation",
                    "Operating warning threshold",
                    "Required response and cash treatment",
                ],
                "rows": [
                    [
                        "Conservative service allocation excludes every prospective statutory award",
                        "Five retainers × $1,500 × twelve months, plus $5,000 projects",
                        "Annual total costs must remain within the $64,600 ceiling",
                        "Preserve $30,400 owner profit by matching scope to collections",
                    ],
                    [
                        "Base service allocation assumes twelve fully paid delivery months",
                        "Eight retainers × $5,000 × twelve months, plus $7,500 projects",
                        "Annual total costs must remain within the $268,125 ceiling",
                        "Reconcile $219,375 owner profit against earned services and expenses",
                    ],
                    [
                        "Scaled service allocation requires expanded contracted delivery capacity",
                        "Ten retainers × $7,000 × twelve months, plus $40,000 projects",
                        "Annual total costs must remain within the $369,600 ceiling",
                        "Maintain $510,400 owner profit without counting pending award proceeds",
                    ],
                    [
                        "Base analyst overruns quietly consume the owner's residual margin",
                        "Eight clients × eight extra hours × $75 × twelve months",
                        "Delivery exceeds 110% of allowance for two consecutive months",
                        "Reprice or narrow scope before the $57,600 leakage recurs",
                    ],
                    [
                        "Illustrative award deductions reduce the recipient's retained contribution",
                        "$200,000 award less $80,000 fee and $20,000 case costs",
                        "Any budget includes contingent proceeds before established operator entitlement",
                        "Exclude the prospective $100,000 entirely from operating cash forecasts",
                    ],
                    [
                        "Delayed law-firm payments create payroll exposure despite reported revenue",
                        "Three Base cost months require $67,031.25 of available funding",
                        "Undisputed invoice exceeds forty-five days without agreed resolution",
                        "Apply contractual notice and pause discretionary new research spending",
                    ],
                    [
                        "Refundable advances falsely inflate cash available for owner distributions",
                        "$5,000 advance less $3,000 earned leaves $2,000 delivery obligation",
                        "Available cash falls below refundable balances plus committed costs",
                        "Retain required cash and reconcile performance before recognizing revenue",
                    ],
                ],
            },
        },
        {
            "heading": "3. Price dismissal, award denial, and platform exclusion explicitly",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The ninth trap is interpreting DOJ non-intervention as either "
                    "vindication or automatic defeat. Non-intervention leaves a relator "
                    "to proceed under § 3730(c)(3), usually with heavier financing "
                    "and litigation burdens; it is not itself a merits judgment. "
                    "Government dismissal under § 3730(c)(2)(A) is a separate event. "
                    "The Granston memorandum describes dismissal considerations, not a "
                    "statutory recovery entitlement or a portable probability table. "
                    "United States ex rel. Polansky v. Executive Health Resources "
                    "addresses Government dismissal after intervention, including later "
                    "intervention, and the applicable procedural framework. Build an "
                    "illustrative cohort of twenty counsel-screened matters: six stop "
                    "for public-disclosure or pleading defects; fourteen proceed; "
                    "three receive intervention and eleven do not. Assume two "
                    "of those eleven later face Government dismissal, leaving "
                    "nine privately pursued matters. The model's non-intervention "
                    "rate is 11/14, or 78.6%; its assumed Government-dismissal "
                    "rate among non-intervened matters is 2/11, or 18.2%. These "
                    "are planning inputs, not reported DOJ or Granston rates. "
                    "If one intervened and one privately pursued matter ultimately "
                    "collect, eighteen of twenty produce zero recovery. Replace "
                    "every assumption with counsel's documented cohort experience "
                    "when available, preserving the denominator and observation "
                    "window so incompatible rates cannot be multiplied together."
                ),
                (
                    "The tenth trap is treating submission as award eligibility. "
                    "SEC Form TCR and IRS Form 211 serve different statutory "
                    "programs and require distinct evidence, identity, timing, and "
                    "award procedures. Route both through counsel under this operating "
                    "model. An anonymous SEC submission requires attorney representation "
                    "and additional identification procedures before payment; a generic "
                    "anonymous email does not substitute for the prescribed process. "
                    "Monitor SEC Notices of Covered Action because an award "
                    "application generally must arrive within ninety calendar days "
                    "of the notice. IRS mandatory-award eligibility generally requires "
                    "proceeds in dispute exceeding $2,000,000 and, for an individual "
                    "taxpayer, gross income exceeding $200,000 for at least one "
                    "taxable year at issue. Tax return information remains subject "
                    "to statutory confidentiality restrictions. Track each program's "
                    "filing receipt, declaration, supplemental submission, notice date, "
                    "and application deadline independently. Distinguish denial before "
                    "payment from recoupment after payment. False statements, "
                    "disqualifying conduct, revised proceeds, invalid entitlement, or "
                    "contractual disputes can create reductions or repayment exposure "
                    "depending on the governing rule or agreement. Never assert "
                    "a universal clawback period. Preserve award determinations, "
                    "fee calculations, cost invoices, and correspondence so counsel "
                    "can reconcile actual retained proceeds rather than reverse-engineering "
                    "them from an optimistic press release."
                ),
                (
                    "The eleventh trap is converting data access into an adversarial "
                    "contest with the source platform. Repeated rate-limit violations, "
                    "shared API credentials, scraping behind revoked access, and "
                    "concealed account replacement can cause permanent account exclusion "
                    "or contractual liability. Use documented CMS downloads, approved "
                    "API access, permitted Open Payments exports, licensed import-manifest "
                    "datasets, and authorized SAM.gov interfaces. Cache immutable public "
                    "releases instead of repeatedly retrieving identical records. Set "
                    "a local operational pause after three consecutive HTTP 429 "
                    "responses, honor Retry-After, and resume only within published "
                    "access conditions. A revoked credential or explicit access "
                    "denial triggers an immediate stop, not credential rotation "
                    "to defeat the restriction. Separately, monitor false-positive "
                    "burden: if more than 20% of a twenty-item reviewed "
                    "sample fails basic entity or arithmetic validation, disable "
                    "that scoring rule until corrected. Keep safety thresholds "
                    "distinct from legal conclusions. A 19% defect rate still "
                    "does not justify forwarding a known error. External enrichment "
                    "also creates disclosure risk when query strings contain "
                    "sealed defendant names or protected identifiers. Strip "
                    "sensitive fields before authorized enrichment and use a "
                    "counsel-approved offline workflow where stripping would destroy "
                    "context. The fallback is slower legitimate research, not "
                    "a disguised replacement account or a purchased credential."
                ),
            ],
            "table": {
                "caption": "Zero-Recovery Funnel, Award Defects, and Data-Access Circuit-Breakers",
                "headers": [
                    "Risk or decision point",
                    "Illustrative measurement or actual rule",
                    "Capital exposure being contained",
                    "Operator action before additional spending",
                ],
                "rows": [
                    [
                        "Public-disclosure and pleading defects eliminate apparently attractive matters",
                        "Six of twenty illustrative matters stop before filing",
                        "Further drafting expenses would fund already identified factual defects",
                        "Return a bounded research conclusion and stop complaint expansion",
                    ],
                    [
                        "Government non-intervention shifts costs without resolving underlying merits",
                        "Eleven of fourteen illustrative filed matters receive non-intervention",
                        "Private litigation financing can exceed the analytics engagement budget",
                        "Obtain a separately funded scope before supporting continued litigation",
                    ],
                    [
                        "Government dismissal requires separate treatment from non-intervention decisions",
                        "Two of eleven illustrative non-intervened matters later face dismissal",
                        "Expected award proceeds disappear while previously incurred costs remain",
                        "Set award forecasts to zero pending counsel's procedural assessment",
                    ],
                    [
                        "SEC notice monitoring fails after a valid initial submission",
                        "Award applications generally require filing within ninety calendar days",
                        "Missed application timing can eliminate otherwise qualifying award participation",
                        "Maintain counsel-owned deadlines with independently checked backup reminders",
                    ],
                    [
                        "IRS mandatory-award thresholds are confused with universal submission requirements",
                        "Assess disputed proceeds and individual income thresholds separately",
                        "Paid research may target matters outside mandatory-award eligibility",
                        "Counsel evaluates the applicable award pathway before expanding scope",
                    ],
                    [
                        "Source platform rejects requests after repeated quota exhaustion",
                        "Three consecutive HTTP 429 responses trigger a local pause",
                        "Account exclusion can interrupt every customer using that source",
                        "Honor access conditions and replace collection with permitted exports",
                    ],
                    [
                        "Scoring rule generates excessive elementary validation failures",
                        "More than four failures in twenty reviewed items stops deployment",
                        "Analyst rework and unreliable exhibits destroy retained engagement margin",
                        "Disable the rule and rebuild its validation test set",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight verifications before a dossier leaves the workspace",
                "body": (
                    "A failed verification stops external delivery. Preserve the work "
                    "already performed, identify the defect, and resume only after the "
                    "responsible person documents its resolution."
                ),
                "items": [
                    "Verify acquisition authority, immutable source copies, and reproducible exhibit totals; quarantine every restricted record lacking a documented access basis.",
                    "Obtain counsel's public-disclosure, original-source, first-to-file, and jurisdiction-specific pleading assessment without claiming inaccessible sealed dockets have been cleared.",
                    "Verify recipient permissions, seal-sensitive fields, and the exact filing or award-application deadline before transferring any matter package.",
                    "Confirm the engagement remains solvent with zero award receipts, documented contractor capacity, and cash reserved for refunds and committed delivery.",
                ],
            },
        },
        {
            "heading": "4. Remove procurement pass-through defects and rehearse the shutdown",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The required mapped play, gsa_municipal_set_aside_facility_ghost_brokering, "
                    "is workable only as disclosed coordination between an eligible "
                    "facility-service prime and qualified subcontractors. The name must "
                    "not become an operating instruction to conceal who performs "
                    "the work. Consider an illustrative $100,000 eligible service "
                    "contract: a documented $5,000 coordination fee less $3,200 "
                    "of delivery costs leaves $1,800 contribution before overhead. "
                    "The operator records only the earned $5,000 service fee, "
                    "not the prime's $100,000 contract revenue. A cost-of-personnel "
                    "or similarly situated entity analysis under applicable federal "
                    "limitations on subcontracting must follow the actual solicitation "
                    "and 13 CFR § 125.6; the label coordinator does not "
                    "excuse prohibited pass-through performance. Federal service set-asides "
                    "generally restrict payments to nonsimilarly situated subcontractors "
                    "to 50% of the amount paid by the Government for "
                    "contract performance, subject to applicable rules and exclusions. "
                    "Municipal programs can impose different certification, performance, "
                    "and disclosure requirements. Verify the specific local ordinance "
                    "and solicitation rather than transplanting federal percentages. "
                    "Match capability, licenses, staffing, and required status before "
                    "quoting. The forensic business must also screen conflicts "
                    "before accepting investigative work involving its own coordination "
                    "customers, subcontractors, or counterparties with overlapping records."
                ),
                (
                    "The twelfth trap is disguising a success commission as routine "
                    "coordination while ignoring procurement restrictions. For covered "
                    "federal contracts, FAR Subpart 3.4 and applicable clauses "
                    "address contingent fees for obtaining Government contracts, "
                    "with defined exceptions that counsel must evaluate. A "
                    "fee is not permissible merely because an invoice says "
                    "consulting. False eligibility certifications, fabricated subcontractor "
                    "capacity, sham invoices, and undisclosed kickbacks can expose "
                    "participants to payment recovery, termination, exclusion, and "
                    "other liability. Track eligibility evidence by bid date, "
                    "subcontractor status by performance period, and performance "
                    "payments against the applicable limitation. An unverified "
                    "certification or projected prohibited payment allocation stops "
                    "the bid. If the $5,000 coordination fee is refundable "
                    "upon a valid contract defect and $3,200 has already "
                    "been spent, returning the fee changes the engagement "
                    "from $1,800 contribution to a $3,200 loss. That "
                    "$5,000 adverse swing must fit the refund reserve. "
                    "The required fallback is to withdraw noncompliant bids "
                    "and operate as a disclosed subcontractor on unrestricted "
                    "work. Do not repackage the same ineligible arrangement "
                    "under another entity. Keep this play's fee ledger "
                    "separate from forensic retainers and award proceeds; its "
                    "illustrative economics are not additional revenue silently "
                    "added to the canonical volume scenarios."
                ),
                (
                    "The thirteenth trap is continuing because sunk research costs "
                    "feel recoverable. Implement a weekly exception meeting using "
                    "one ledger for evidence defects, another for delivery "
                    "economics, and a third for deadlines and access incidents. "
                    "Assign an accountable person and a next review date "
                    "to every exception. Red conditions include unauthorized "
                    "disclosure, missing acquisition authority, fabricated support, "
                    "a prohibited procurement arrangement, and insufficient cash "
                    "for committed obligations. Amber conditions include disputed "
                    "scope, declining paid utilization, and evidence needing "
                    "corroboration. Counsel owns legal determinations; the operator "
                    "owns collection pauses, cost freezes, and accurate reporting. "
                    "Rehearse a zero-recovery quarter in which the largest "
                    "retainer pauses and no contingent proceeds arrive. In "
                    "the Base allocation, losing one $5,000 monthly client "
                    "for three months removes $15,000 revenue before any "
                    "cost adjustment. If costs remain fixed, annual owner "
                    "profit falls to $204,375. Reforecast immediately instead "
                    "of waiting for an annual margin report. Close "
                    "an engagement with a source inventory, delivered-work "
                    "acceptance record, outstanding invoice schedule, refund "
                    "calculation, and counsel-directed retention instructions. Never "
                    "delete records to make an incident disappear. The "
                    "durable advantage is surviving enough ordinary paid "
                    "engagements to pursue exceptional matters without pressuring "
                    "analysts to turn uncertainty into allegations."
                ),
            ],
            "table": {
                "caption": "Disclosed Facility Coordination, Refund Exposure, and Orderly Exit Controls",
                "headers": [
                    "Operator failure mode",
                    "Concrete test or unit economics",
                    "Required operating response",
                    "Fallback preserving legitimate service revenue",
                ],
                "rows": [
                    [
                        "Coordinator records the prime's contract value as operator revenue",
                        "$100,000 contract supports only the separate $5,000 earned fee",
                        "Recognize documented coordination services rather than underlying procurement volume",
                        "Invoice disclosed services with delivery evidence and contractual acceptance",
                    ],
                    [
                        "Service set-aside performance becomes an opaque prohibited pass-through",
                        "Assess nonsimilarly situated payments under the applicable 50% limitation",
                        "Stop bidding until the actual performance allocation satisfies requirements",
                        "Withdraw defective bids and pursue disclosed unrestricted subcontract work",
                    ],
                    [
                        "Municipal certification is assumed equivalent to federal program eligibility",
                        "Compare each bidder representation against the actual local solicitation",
                        "Obtain valid program evidence before submitting any eligibility certification",
                        "Select unrestricted municipal work matching verified licenses and capacity",
                    ],
                    [
                        "Contingent procurement commission is mislabeled as ordinary analytical support",
                        "Review covered contract clauses and applicable contingent-fee exceptions",
                        "Have counsel resolve compensation structure before accepting the engagement",
                        "Offer permissible documented services without concealed award-procurement commissions",
                    ],
                    [
                        "Refundable coordination fee is distributed before defect exposure clears",
                        "$5,000 refund after $3,200 costs produces a $3,200 loss",
                        "Reserve cash against the specific contractual repayment exposure",
                        "Use staged earned payments tied to verified service delivery",
                    ],
                    [
                        "Forensic investigation overlaps the operator's own procurement customer relationships",
                        "Any shared counterparty triggers a documented conflict assessment",
                        "Restrict access and obtain counsel's decision before substantive work",
                        "Decline conflicting matters while retaining unrelated authorized service engagements",
                    ],
                    [
                        "Lost retainer is concealed by optimistic pending award estimates",
                        "Three unpaid Base retainer months remove $15,000 annual revenue",
                        "Reforecast owner profit to $204,375 before any cost adjustments",
                        "Resize spending and replace revenue through ordinary paid services",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the defective workstream",
                    "action": "Pause affected collection, external delivery, or bidding immediately.",
                    "detail": (
                        "Preserve source files, permission records, correspondence, and "
                        "access logs. Do not broaden the pause to unrelated authorized "
                        "engagements unless the incident affects their evidence or systems."
                    ),
                },
                {
                    "step": 2,
                    "title": "Assign authority and quantify exposure",
                    "action": "Send the factual incident record to the responsible counsel and operator.",
                    "detail": (
                        "List affected recipients, deadlines, earned fees, refundable "
                        "balances, committed contractor costs, and potential award "
                        "dependencies. Separate established facts from unresolved hypotheses."
                    ),
                },
                {
                    "step": 3,
                    "title": "Rebuild the zero-award cash forecast",
                    "action": "Update thirteen weeks of collections, refunds, payroll, and contracted spending.",
                    "detail": (
                        "Remove every prospective statutory award. Apply the actual "
                        "engagement terms to service pauses and refunds, and identify "
                        "the funding needed before any new commitment."
                    ),
                },
                {
                    "step": 4,
                    "title": "Resume with evidence or execute the fallback",
                    "action": "Document corrected authority, calculations, recipients, and engagement scope.",
                    "detail": (
                        "Resume only the corrected activity. If a procurement bid remains "
                        "noncompliant, withdraw it and pursue disclosed unrestricted work; "
                        "if evidence remains insufficient, close the allegation workstream."
                    ),
                },
            ],
        },
    ],
    "pull_quote": (
        "A sealed theory cannot pay payroll, and an unexplained anomaly cannot carry a complaint."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        "Reproduce every cited CMS, Open Payments, SAM.gov, or manifest calculation from a frozen source release with a recorded SHA-256 digest.",
        "Give counsel a disclosure chronology, acquisition-authority ledger, and jurisdiction-specific claim matrix before expanding any allegation.",
        "Separate earned retainers, refundable advances, reimbursable costs, collected cash, and realized award receipts in the monthly reconciliation.",
        "Run a thirteen-week cash forecast with zero award proceeds and test the loss of the largest retainer for three months.",
        "Implement source-access pauses, recipient checks, SEC notice monitoring, and counsel-owned filing deadlines with documented backup responsibility.",
        "Verify the disclosed facility-coordination play's eligibility, compensation, and subcontracting allocation; withdraw defective bids and use the unrestricted-work fallback.",
    ],
    "statutory_citations": [
        {
            "title": "31 U.S.C. § 3729 — False Claims Act liability",
            "url": "https://www.law.cornell.edu/uscode/text/31/3729",
            "relevance": (
                "Defines actionable false claims and related conduct; statistical "
                "outliers alone do not establish the required liability elements."
            ),
        },
        {
            "title": "31 U.S.C. § 3730 — Qui tam procedure, participation, and awards",
            "url": "https://www.law.cornell.edu/uscode/text/31/3730",
            "relevance": (
                "Supplies the seal, first-to-file, public-disclosure, original-source, "
                "Government-dismissal, and relator-share framework."
            ),
        },
        {
            "title": "Federal Rule of Civil Procedure 9(b) — Pleading fraud or mistake",
            "url": "https://www.law.cornell.edu/rules/frcp/rule_9",
            "relevance": (
                "Requires particularity in pleading fraud; counsel must apply "
                "controlling circuit standards to the proposed FCA allegations."
            ),
        },
        {
            "title": "State Farm Fire & Casualty Co. v. United States ex rel. Rigsby, 580 U.S. 26 (2016)",
            "url": "https://www.supremecourt.gov/opinions/16pdf/15-513_43j7.pdf",
            "relevance": (
                "Explains why an FCA seal violation does not mandate automatic "
                "dismissal while leaving meaningful remedial consequences available."
            ),
        },
        {
            "title": "United States ex rel. Polansky v. Executive Health Resources, Inc., 599 U.S. 419 (2023)",
            "url": "https://www.supremecourt.gov/opinions/22pdf/21-1052_fd9g.pdf",
            "relevance": (
                "Addresses Government dismissal of qui tam litigation after "
                "intervention and distinguishes that process from non-intervention."
            ),
        },
        {
            "title": "15 U.S.C. § 78u-6 — SEC whistleblower incentives and protection",
            "url": "https://www.law.cornell.edu/uscode/text/15/78u-6",
            "relevance": (
                "Establishes SEC award percentages, eligibility conditions, "
                "disqualifications, and confidentiality provisions."
            ),
        },
        {
            "title": "17 CFR § 240.21F-9 — Procedures for submitting original information",
            "url": "https://www.ecfr.gov/current/title-17/section-240.21F-9",
            "relevance": (
                "Governs SEC information submission procedures, including "
                "requirements associated with anonymous submissions through counsel."
            ),
        },
        {
            "title": "17 CFR § 240.21F-10 — Procedures for making an award claim",
            "url": "https://www.ecfr.gov/current/title-17/section-240.21F-10",
            "relevance": (
                "Provides the SEC covered-action notice and award-application "
                "process, including the general ninety-calendar-day filing deadline."
            ),
        },
        {
            "title": "7 U.S.C. § 26 — CFTC whistleblower incentives and protection",
            "url": "https://www.law.cornell.edu/uscode/text/7/26",
            "relevance": (
                "Separately establishes CFTC whistleblower award eligibility "
                "and the program's 10%–30% statutory award range."
            ),
        },
        {
            "title": "26 U.S.C. § 7623 — IRS whistleblower awards",
            "url": "https://www.law.cornell.edu/uscode/text/26/7623",
            "relevance": (
                "Sets IRS award pathways, mandatory-award thresholds, "
                "percentage ranges, reductions, and exclusions."
            ),
        },
        {
            "title": "26 U.S.C. § 6103 — Confidentiality of returns and return information",
            "url": "https://www.law.cornell.edu/uscode/text/26/6103",
            "relevance": (
                "Constrains disclosure of tax return information and explains "
                "why an IRS submission does not create unrestricted access to taxpayer records."
            ),
        },
        {
            "title": "13 CFR § 125.6 — Limitations on subcontracting",
            "url": "https://www.ecfr.gov/current/title-13/section-125.6",
            "relevance": (
                "Controls covered set-aside performance allocations, including "
                "service-contract limitations and treatment of similarly situated entities."
            ),
        },
        {
            "title": "48 CFR § 52.203-5 — Covenant Against Contingent Fees",
            "url": "https://www.ecfr.gov/current/title-48/section-52.203-5",
            "relevance": (
                "Defines the covered contractual restriction, exceptions, and "
                "remedies relevant to compensation for obtaining Government contracts."
            ),
        },
        {
            "title": "41 U.S.C. § 8702 — Prohibition on kickbacks",
            "url": "https://www.law.cornell.edu/uscode/text/41/8702",
            "relevance": (
                "Prohibits covered kickback conduct in federal contracting; "
                "disclosed coordination cannot conceal improper procurement payments."
            ),
        },
    ],
}
