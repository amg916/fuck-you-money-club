from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-and-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in no surprises act (idr) medical arbitration & out-of-network recovery, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "ERISA Jurisdiction, QPA Baselines, IDR Fee Exposure, HIPAA Controls, and Cash-Verified Recovery Circuit Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #45, Rank #09 of 49, scores 94/100, but its small-team advantage disappears "
        "when eligibility defects, missed deadlines, and uncollected awards masquerade as production. "
        "This chapter organizes 12 mapped plays: eleven chapter-local recovery controls and the supplied "
        "level-funded benefits advisory adjacency. The canonical annual owner-profit cases are $33,000 "
        "Conservative, $217,150 Base, and $504,000 Scaled, supported by earned operator revenue of "
        "$110,000, $505,000, and $900,000. None includes baseline provider collections or unpaid awards. "
        "Use claim-level jurisdiction evidence, business-day clocks, fee-adjusted incremental cash, and "
        "documented reversal reserves to protect those economics. The question's 80% framing is not "
        "an observed failure statistic; the actionable subject is preventable capital loss."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$110,000",
            "context": "Annual earned contingency revenue on fee-adjusted incremental cash collections",
            "note": "30% net margin; $33,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$505,000",
            "context": "Annual earned contingency revenue on fee-adjusted incremental cash collections",
            "note": "43.0% net margin; $217,150 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual earned contingency revenue on fee-adjusted incremental cash collections",
            "note": "56% net margin; $504,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reject jurisdiction defects before they become paid filings",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is treating every out-of-network short payment as federal IDR inventory. "
                    "Coverage, service category, date, location, and the applicable payment-setting law determine the route; "
                    "a payer logo does not. The second is equating ERISA status with automatic federal eligibility. "
                    "Distinguish self-funded plans, fully insured coverage, applicable specified state law, and relevant "
                    "state opt-in arrangements before assigning a filing queue. Capture the plan sponsor, administrator, "
                    "funding evidence, service location, emergency status, facility network status, and any notice-and-consent "
                    "documentation. Ground-ambulance claims generally sit outside these federal surprise-billing protections; "
                    "air-ambulance disputes require their own analysis. A denial involving coverage or medical necessity "
                    "may require an appeal rather than a payment-amount arbitration. Chapter-local play P01, jurisdiction "
                    "proof, buys a second check before money leaves the account. If screening costs $20 per claim, "
                    "screening 100 claims costs $2,000; preventing four defective filings with $750 of otherwise stranded "
                    "fees and work avoids $3,000, leaving $1,000 of illustrative protection. The fallback is a documented "
                    "state-law, contractual, or benefit-appeal route, never relabeling the claim to fit federal eligibility. "
                    "Retain the source document behind every routing decision, including the effective date of the rule used."
                ),
                (
                    "The third trap is confusing the initial filing clock with the negotiation period. Ordinarily, open "
                    "negotiation must be initiated within 30 business days after receipt of the initial payment or denial; "
                    "the negotiation period itself lasts 30 business days, followed by a four-business-day federal IDR "
                    "initiation window. Extensions and special circumstances require evidence, not a salesperson's promise. "
                    "Chapter-local play P02, deadline provenance, stores the actual receipt event, negotiation delivery evidence, "
                    "applicable holiday calendar, and calculated last permissible action. Set an internal initiation target "
                    "two business days before the legal deadline and require a second reviewer whenever receipt dates "
                    "disagree. An 835 transaction date is not automatically proof of when the provider received the "
                    "payment or denial. Chapter-local play P03, authority validation, links each submission to the correct "
                    "provider entity, NPI, tax identifier, and written representative authority. A shared spreadsheet that "
                    "silently changes time zones can destroy an otherwise strong recovery. For 50 cases carrying $400 "
                    "of expected operator contribution each, one missed batch risks $20,000; a $300 monthly calendar "
                    "and review budget is inexpensive by comparison. When authority or timing remains unresolved, stop "
                    "new submissions for that cohort and preserve the available correction or extension evidence."
                ),
                (
                    "The fourth trap is batching for convenience instead of legal eligibility. Chapter-local play P04, "
                    "batch integrity, groups only disputes satisfying the applicable version of the batching requirements "
                    "and preserves a manifest of every included item. Do not assume that a shared payer brand, "
                    "specialty, or spreadsheet tab establishes the required party and service relationships. Validate the "
                    "service window, provider identity, plan or issuer identity, and permitted item or service grouping "
                    "against current controlling rules and CMS instructions. Chapter-local play P05, cooling-period separation, "
                    "tracks the 90-calendar-day restriction after a determination for the relevant parties and same or "
                    "similar items or services. Preserve affected claims for the applicable post-period initiation pathway; "
                    "the rule provides a subsequent 30-business-day window for qualifying suspended disputes, not permission "
                    "to ignore their records. Litigation and implementation changes make a versioned rule register essential. "
                    "At an illustrative $600 entity-fee exposure per defective filing, five bad submissions consume $3,000 "
                    "before staff time. The fallback is a smaller eligible batch or individual filing supported by "
                    "the effective rules, not a manipulated code. Keep the original coding intact and send genuine "
                    "coding errors back through the provider's authorized correction process."
                ),
            ],
            "table": {
                "caption": "Jurisdiction, Clock, and Batch Defects That Consume Filing Capital",
                "headers": [
                    "Failure mechanism and exposed operational assumption",
                    "Evidence required before assigning the claim route",
                    "Early warning threshold for internal intervention",
                    "Capital preserving response and accountable operating owner",
                ],
                "rows": [
                    [
                        "P01: Payer branding substitutes for actual plan funding evidence",
                        "Retain plan documents and claim-specific state-law routing analysis",
                        "Any unresolved funding classification blocks paid filing preparation",
                        "Jurisdiction reviewer redirects claims into the documented applicable process",
                    ],
                    [
                        "Emergency classification is inferred solely from physician specialty",
                        "Retain encounter facts establishing the relevant protected service category",
                        "Any conflicting encounter classification triggers immediate clinical documentation review",
                        "Clinical reviewer resolves evidence before the filing team proceeds",
                    ],
                    [
                        "Coverage denials enter payment arbitration without a routing assessment",
                        "Read benefit denial grounds and available appeal correspondence together",
                        "Any medical-necessity denial requires a separate appeal-route determination",
                        "Appeals lead preserves benefit remedies without manufacturing payment eligibility",
                    ],
                    [
                        "P02: Electronic remittance timestamp replaces documented payment receipt",
                        "Preserve receipt records and delivered negotiation notices with timestamps",
                        "Any conflicting receipt dates require same-day deadline-owner reconciliation",
                        "Deadline owner uses supported dates and documented escalation procedures",
                    ],
                    [
                        "P03: Representative submits under an incorrect provider legal identity",
                        "Match authorization, tax identifier, NPI, and contracting provider records",
                        "Any identity mismatch stops submission until records are corrected",
                        "Provider liaison obtains corrected authority and preserves amendment history",
                    ],
                    [
                        "P04: Similar spreadsheet descriptions are mistaken for batch eligibility",
                        "Attach the effective batching rule and item-level eligibility manifest",
                        "One unsupported batch member triggers full manifest revalidation",
                        "Filing lead separates eligible items without changing underlying coding",
                    ],
                    [
                        "P05: Same-party cooling restrictions disappear across separate work queues",
                        "Link determinations and affected items within one restriction register",
                        "Any overlap with an active restriction triggers queue separation",
                        "Calendar owner preserves qualifying subsequent-window claims and supporting evidence",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four pre-flight checks before committing nonrecoverable money",
                "body": (
                    "These are internal operating requirements. A passed checklist does not replace the "
                    "claim-specific statutory analysis or current filing instructions."
                ),
                "items": [
                    "Verify the protected service category, funding evidence, and federal-versus-state route with a named reviewer.",
                    "Recalculate negotiation and initiation dates from preserved receipt evidence using the applicable business-day calendar.",
                    "Validate representative authority, party identities, batch membership, and active cooling-period restrictions.",
                    "Confirm the current fee schedule, signed expense allocation, and cash reserve covering an adverse eligibility decision.",
                ],
            },
        },
        {
            "heading": "2. Reconcile earned fees to collected cash, not arbitration headlines",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The fifth trap is booking the selected offer as collected revenue. Chapter-local play P06, baseline "
                    "reconciliation, distinguishes the payer's disclosed QPA from its actual initial allowed amount and "
                    "payment. They are not interchangeable fields. Define the baseline using the signed engagement and "
                    "claim-level remittance record, then identify only additional payer cash actually received and matched "
                    "to that claim. Patient cost-sharing, the original provider collection, and outstanding awards do not "
                    "become operator revenue. Chapter-local play P07, fee-adjusted settlement, applies the contracted contingency "
                    "percentage only after unrecovered administrative fees, entity fees, and agreed casework costs. Consider "
                    "an illustrative $12,000 initial payer payment followed by $8,000 of additional deposited recovery. "
                    "Assume a $125 administrative charge, a $600 entity deposit subsequently refunded, and $600 of "
                    "casework costs. These are modeling inputs, not representations of current published charges. After "
                    "the refund clears, the distributable recovery base is $8,000 minus $125 minus $600, or $7,275. "
                    "A 30% contingency earns $2,182.50. Before that refund clears, retain the $600 reserve and "
                    "limit the provisional fee base to $6,675. The remaining $600 is neither earned fee revenue "
                    "nor spendable working capital merely because the operator expects to prevail."
                ),
                (
                    "The sixth trap is assuming all unsuccessful or dismissed cases have identical refund treatment. Budget "
                    "the CMS administrative fee as nonrefundable and reserve the certified entity fee through actual "
                    "reconciliation. The prevailing party's entity-fee refund follows the applicable process; losing cases expose "
                    "that fee to forfeiture. For ineligibility dismissals, conservatively reserve the full charge unless the "
                    "effective instructions and entity policy establish a return, and recognize recovery only when received. "
                    "Chapter-local play P08, reversal reserve, also covers payer recoupments, duplicate payments, corrected remittances, "
                    "and provider refunds. Never distribute against an unmatched EFT. In the example, a failed claim "
                    "with no incremental recovery can strand $125 plus $600 plus $600, or $1,325. The contract "
                    "must identify who bears that loss; concealing it inside the next provider's settlement creates "
                    "both trust and accounting problems. At cohort level, 100 initiated disputes with 75 favorable "
                    "determinations but only 60 paid recoveries of $2,000 generate $120,000 of incremental cash, not "
                    "$150,000. If unrecovered fees total $20,000 and casework costs total $10,000, the contingency "
                    "base is $90,000 and a 30% operator share is $27,000. The other fifteen favorable outcomes "
                    "remain collection work, not another $9,000 of earned fees."
                ),
                (
                    "The seventh trap is double counting revenue while hiding the expense burden. Formula v2.0 fixes "
                    "Conservative operator revenue at $110,000, expenses at $77,000, and owner net profit at $33,000, "
                    "a 30% margin with 1 FT + 2 C. Base uses $505,000, $287,850, and $217,150, respectively, "
                    "a 43.0% margin with 1 FT + 2 C. Scaled uses $900,000, $396,000, and $504,000, "
                    "a 56% margin with 2 FT + 3 C. These revenues are earned contingency shares, not "
                    "underlying provider collections or award face values. The model treats the operator's retained earned "
                    "share as revenue; document the ASC 606 principal-versus-agent assessment rather than automatically grossing "
                    "up money handled for providers. Expenses already deducted in the provider settlement must not "
                    "be deducted again as unreimbursed operator costs. Conversely, costs the operator actually absorbs remain "
                    "expenses. At an illustrative uniform 30% contingency, the three revenue targets require approximately "
                    "$366,667, $1,683,333, and $3,000,000 of fee-adjusted collected recovery bases. Those bases are operating "
                    "requirements, not additional revenue scenarios. A monthly close should bridge bank deposits, provider "
                    "liabilities, refunds, retained fees, overhead, and owner profit, with every unresolved difference assigned "
                    "to a person and a dated resolution task."
                ),
            ],
            "table": {
                "caption": "Cash Waterfall Controls and Canonical Formula v2.0 Reconciliation",
                "headers": [
                    "Ledger component and specific economic failure mode",
                    "Required calculation or canonical scenario control value",
                    "Evidence needed before recognizing the economic event",
                    "Corrective response when the reconciliation does not balance",
                ],
                "rows": [
                    [
                        "P06: Initial payer payment becomes inflated operator recovery",
                        "Subtract the supported initial baseline from matched additional collections",
                        "Match original remittance, subsequent remittance, and deposited payer funds",
                        "Accounting lead reverses unsupported fees before provider settlement release",
                    ],
                    [
                        "P07: Published award amount substitutes for deposited recovery",
                        "Count only incremental received cash within the contractual waterfall",
                        "Retain bank match and claim-level explanation of each deposit",
                        "Collections owner tracks the unpaid award outside earned revenue",
                    ],
                    [
                        "Entity deposit refund is spent before actual receipt",
                        "Reserve the entire deposit until the refund is reconciled",
                        "Match refund confirmation to the actual receiving account transaction",
                        "Treasury owner reduces provisional distributions by the outstanding reserve",
                    ],
                    [
                        "P08: Later payer recoupment leaves provider settlement overdistributed",
                        "Recompute net incremental recovery and associated retained contingency share",
                        "Preserve recoupment rationale and corrected claim-level remittance allocation",
                        "Settlement owner issues contractual adjustments and rebuilds required reserves",
                    ],
                    [
                        "Conservative scenario converts recovery volume into overstated business revenue",
                        "$110,000 earned revenue minus $77,000 expenses equals $33,000 profit",
                        "Reconcile 30% margin and the 1 FT plus 2 C team",
                        "Owner rejects forecasts that include baseline collections or awards",
                    ],
                    [
                        "Base scenario hides costs already allocated through provider settlements",
                        "$505,000 earned revenue minus $287,850 expenses equals $217,150 profit",
                        "Reconcile 43.0% margin and the 1 FT plus 2 C team",
                        "Controller removes duplicate expenses while retaining genuinely absorbed costs",
                    ],
                    [
                        "Scaled scenario treats five people as unlimited casework capacity",
                        "$900,000 earned revenue minus $396,000 expenses equals $504,000 profit",
                        "Reconcile 56% margin and the 2 FT plus 3 C team",
                        "Operations lead caps intake when documented service capacity deteriorates",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the cash waterfall before celebrating a determination",
                "body": (
                    "Veteran operators maintain separate determination, cash, fee, and reversal records. "
                    "A single status field cannot represent all four."
                ),
                "items": [
                    "Store the initial QPA disclosure and actual initial payer payment separately so a QPA correction cannot silently rewrite the recovery baseline.",
                    "Allocate batch charges using a signed, consistent method and retain the allocation version with every provider statement.",
                    "Hold expected entity-fee refunds in a receivable and reserve account until the bank transaction actually clears.",
                    "Require a second reviewer to match large payer EFTs across claims before any contingency invoice or provider distribution.",
                ],
            },
        },
        {
            "heading": "3. Detect operational decay before access restrictions or recoupments spread",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The eighth trap is replacing evidence with a persuasive template. Chapter-local play P09, offer integrity, "
                    "requires a sourced explanation of the proposed payment and a documented review of relevant permitted "
                    "factors. QPA is an input, not a license to invent clinical acuity or a universal multiplier "
                    "that wins every dispute. Licensed FAIR Health material can inform research where permitted, but "
                    "identify the statistic, source rights, population, and relevance; an impermissible charge benchmark does "
                    "not become usable because a vendor sold it. The federal framework excludes certain considerations, "
                    "including usual and customary charges, billed charges, and public-payer reimbursement rates. Respect the "
                    "effective rules and court decisions governing how permissible information is weighed. A clinician validates "
                    "acuity statements against the actual encounter; the operator never changes medical documentation to improve "
                    "the offer. For 40 briefs requiring 30 minutes of expert review at $120 per hour, "
                    "quality assurance costs $2,400. Avoiding four $750 defective filings already offsets that amount. "
                    "The fallback for weak evidence is a narrower supportable offer or negotiated settlement. Copying "
                    "another provider's outcome, fabricating a comparator, or deleting unfavorable records can turn an "
                    "ordinary collection dispute into contractual exposure, referral risk, and a loss of portal access."
                ),
                (
                    "The ninth trap is treating patient information as harmless sales material. Chapter-local play P10, access "
                    "containment, begins with a HIPAA business associate agreement when the relationship requires one, approved "
                    "subcontractor arrangements, role-based access, and audit retention. An 835 ERA parser should extract "
                    "CARC and RARC signals into a controlled queue, not send raw patient records to a "
                    "personal mailbox or an unapproved public AI service. Apply minimum-necessary practices where required "
                    "and follow the applicable Security Rule safeguards for electronic protected health information. Portal "
                    "accounts must identify authorized people; do not share credentials, rotate fictitious identities, or "
                    "evade rate limits after access is restricted. Use supported interfaces and permitted automation, "
                    "with retries bounded by documented service behavior. Suspend the affected integration on the first "
                    "unexplained access denial or material authorization mismatch; preserve the event and contact the "
                    "appropriate administrator. For a five-person operation, one shared login creates five indistinguishable "
                    "sources of error, while named accounts make investigation and revocation practical. The fallback "
                    "is a controlled manual workflow using authorized access, not an alternate account designed to "
                    "bypass enforcement. Report suspected incidents through the established response process, assess notification "
                    "duties, and prevent the same credentials from reaching unaffected provider workspaces."
                ),
                (
                    "The tenth trap is scaling intake while collection quality decays. Chapter-local play P11, cohort circuit "
                    "breakers, measures eligibility dismissals, deadline misses, unpaid determinations, refund aging, and reversals by "
                    "provider, payer, service category, and filing month. The thresholds here are internal triggers, not "
                    "statutory tolerances. A single missed statutory deadline freezes new work in the affected queue "
                    "until the clock defect is corrected. More than 2% eligibility dismissals across the latest "
                    "50 resolved filings triggers full re-screening; fewer than 50 observations require review of every "
                    "dismissal rather than a reassuring percentage. Payment is generally due within 30 calendar days "
                    "after determination under the federal framework; track the specific obligation and escalate overdue "
                    "balances through documented payer contacts and appropriate complaint channels. If more than 20% of "
                    "favorable determined dollars remain unpaid beyond 45 days, stop increasing that payer's exposure. "
                    "If reversals exceed 3% of trailing 90-day incremental cash, recalculate the reserve before "
                    "distributing more fees. These are conservative management choices, not evidence of industry averages. "
                    "A $10,000 reserve funding $1,000 weekly net cash burn lasts ten weeks; favorable outcome "
                    "statistics cannot extend that runway. The fallback is fewer paid filings, tighter evidence review, "
                    "and active collections, not pressure on patients to fund the shortfall."
                ),
            ],
            "table": {
                "caption": "Evidence Integrity, HIPAA Access, and Collection Telemetry Circuit Breakers",
                "headers": [
                    "Observed defect or hazardous shortcut requiring intervention",
                    "Metric definition and internal response trigger level",
                    "Specific operational action taken when triggered immediately",
                    "Evidence necessary before normal processing can resume",
                ],
                "rows": [
                    [
                        "P09: Clinical acuity narrative lacks encounter-specific documentary support",
                        "Any unsupported clinical assertion stops the affected brief",
                        "Clinical reviewer removes unsupported statements and verifies remaining evidence",
                        "Retain signed review notes linked to the actual encounter",
                    ],
                    [
                        "Benchmark packet relies on a prohibited payment consideration",
                        "Any excluded benchmark triggers review of the entire packet",
                        "Brief owner replaces unsupported valuation with permissible sourced evidence",
                        "Document source rights and the applicable evidentiary rule version",
                    ],
                    [
                        "P10: Shared credentials prevent reliable attribution of portal actions",
                        "Any shared account discovery triggers immediate access remediation",
                        "Access administrator provisions named authorization and revokes unsafe access",
                        "Verify individual accounts and retained audit events before resuming",
                    ],
                    [
                        "Patient records appear in an unapproved external processing service",
                        "Any confirmed unauthorized transfer starts the incident response process",
                        "Security owner contains exposure and assesses applicable notification duties",
                        "Retain containment evidence and approved processing arrangements before restarting",
                    ],
                    [
                        "P11: Eligibility dismissals reveal systematic claim routing deterioration",
                        "Above 2% across fifty resolved filings triggers re-screening",
                        "Jurisdiction lead reviews the cohort before additional paid submissions",
                        "Document root cause and corrected routing on affected claims",
                    ],
                    [
                        "Favorable determinations accumulate without corresponding incremental payer cash",
                        "Above 20% unpaid beyond forty-five days limits payer exposure",
                        "Collections lead escalates aged balances and slows new spending",
                        "Demonstrate actual cash recovery rather than revised collection promises",
                    ],
                    [
                        "Recoupments exceed the reserve supporting distributed contingency fees",
                        "Above 3% of trailing ninety-day recovery triggers reserve recalculation",
                        "Controller reduces distributions and recomputes claim-level settlement adjustments",
                        "Reconcile reversal exposure and funded reserves before releasing cash",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the affected cohort",
                    "action": "Stop additional paid submissions and discretionary distributions for the identified defect.",
                    "detail": (
                        "Keep unrelated validated work moving. Name the incident owner, impacted provider and payer "
                        "cohort, available cash, next deadlines, and the exact reason for intervention."
                    ),
                },
                {
                    "step": 2,
                    "title": "Preserve and reconstruct evidence",
                    "action": "Rebuild the claim history from source records rather than dashboard status labels.",
                    "detail": (
                        "Collect receipt evidence, delivered notices, authority documents, fee receipts, determination "
                        "records, remittances, bank matches, and access logs without altering original records."
                    ),
                },
                {
                    "step": 3,
                    "title": "Reprice exposure and select the remedy",
                    "action": "Calculate stranded charges, reversible operator fees, outstanding provider liabilities, and runway.",
                    "detail": (
                        "Use the documented correction, collection, appeal, complaint, or incident-response route. "
                        "Do not conceal the defect through duplicate filings or substituted identities."
                    ),
                },
                {
                    "step": 4,
                    "title": "Resume only the corrected workflow",
                    "action": "Test the repaired rule against the affected cohort and independently review results.",
                    "detail": (
                        "Require supported dates, valid authority, balanced cash records, and resolved access issues. "
                        "Keep enhanced monitoring until the next cohort confirms that the defect has stopped recurring."
                    ),
                },
            ],
        },
        {
            "heading": "4. Keep adjacent benefits revenue from contaminating the recovery engine",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The eleventh trap is selling a benefits restructuring project as a guaranteed cure for disputed "
                    "provider payments. The supplied mapped play, erisa_level_funded_transparent_pbm_bor_arbitrage, belongs to TRACK_1 and "
                    "is the twelfth play in this chapter's map, alongside local controls P01 through P11. "
                    "Use public Form 5500 Schedule A and Schedule C information, where filed and informative, "
                    "to identify renewal timing and compensation-review opportunities. These filings have reporting limits and "
                    "lags; they do not establish current claim jurisdiction, hidden misconduct, or permission to contact "
                    "individual patients. Obtain employer authorization for a CAA 2021 service-provider compensation-disclosure review "
                    "under ERISA section 408(b)(2)(B). A properly licensed advisory team may seek a broker-of-record "
                    "appointment and disclose direct and indirect compensation. At $40 PEPM for 250 covered employees, "
                    "the advisory fee is $10,000 monthly and $120,000 annually; at $65 PEPM it is "
                    "$16,250 monthly and $195,000 annually. Define the billing population explicitly so employee and "
                    "member counts cannot be interchanged. These are separate illustrative advisory receipts, not additions "
                    "to the canonical recovery scenarios. If licensing, scope, or compensation transparency is incomplete, "
                    "narrow the assignment to authorized disclosed work with qualified partners rather than collecting "
                    "brokerage compensation through an unrelated IDR invoice."
                ),
                (
                    "The twelfth trap is assuming unbundling necessarily lowers employer cost. Compare the existing bundled arrangement "
                    "with separately contracted TPA administration, stop-loss coverage, suitable captive participation, and a transparent "
                    "pass-through PBM only after defining equivalent benefits and risk assumptions. Specify attachment points, "
                    "lasers, exclusions, terminal liability, runout funding, collateral, and claim-payment timing. NADAC is a "
                    "published acquisition-cost reference, not a complete pharmacy contract. An explicitly defined NADAC-based "
                    "methodology needs the applicable publication date, dispensing fees, specialty-drug treatment, rebate ownership, "
                    "audit rights, and a negotiated fallback for drugs without a usable NADAC value. For "
                    "250 employees, a quoted $12 PEPM administrative reduction equals $36,000 annually. If incremental "
                    "stop-loss and collateral carrying costs total $45,000, the proposal is already $9,000 worse "
                    "before adding advisory fees or transition work. Do not bury those costs in a "
                    "different exhibit. The fallback is to retain or competitively rebid the existing structure, "
                    "obtain explicit pricing fallbacks, and postpone implementation until the employer accepts the risk-adjusted "
                    "economics. Keep employer advisory records separate from provider recovery records; neither relationship creates "
                    "automatic authority to reuse the other's protected information or negotiate on behalf of "
                    "an adverse party without a documented conflict assessment."
                ),
                (
                    "The thirteenth trap is financing an evidence-heavy recovery business with fee commitments that exceed its "
                    "cash buffer. The canonical startup range is $10,000 to $45,000, monthly operating expense "
                    "range is $1,800 to $10,500, and first-deal timing is one to four months. "
                    "Those ranges are planning inputs, not complete annual cost bridges: case charges, reimbursable "
                    "pass-throughs, staffing, and the owner's compensation treatment must still reconcile to the three "
                    "canonical scenarios. At $10,500 monthly overhead, four months consumes $42,000 before incremental "
                    "filing exposure, leaving only $3,000 from a $45,000 opening balance. Do not commit "
                    "that remainder to a large payer cohort whose determinations have not converted into cash. "
                    "Maintain a thirteen-week cash forecast separating provider money, earned operator fees, refundable deposits, "
                    "nonrecoverable charges, and reversal reserves. Require a positive stress-case balance after assuming "
                    "no new collections for the next eight weeks and funding already committed case costs. "
                    "If that test fails, reduce intake, renegotiate authorized expense funding, or return incomplete "
                    "files before incurring charges. The durable advantage is selective underwriting of collectible "
                    "claims with defensible evidence, not the maximum number of portal submissions a small "
                    "team can generate in a day."
                ),
            ],
            "table": {
                "caption": "TRACK_1 Benefits Adjacency and Recovery Business Capital Boundaries",
                "headers": [
                    "Adjacent operating decision and potential failure mechanism",
                    "Concrete unit economics or required documentary analysis",
                    "Evidence and commercial terms required before proceeding",
                    "Fallback that preserves capital and client relationships",
                ],
                "rows": [
                    [
                        "Public benefit filings are treated as current employer authorization",
                        "Review Schedule A and C only where actually informative",
                        "Obtain employer authorization before the compensation-disclosure review begins",
                        "Use filings for research while requesting current employer documents",
                    ],
                    [
                        "Broker-of-record opportunity bypasses applicable licensing and compensation transparency",
                        "Disclose direct compensation and reasonably expected indirect compensation",
                        "Verify qualified personnel and the written advisory service scope",
                        "Restrict work to authorized services supported by qualified partners",
                    ],
                    [
                        "PEPM quote silently switches between employees and covered members",
                        "250 employees at $40 PEPM produce $120,000 annual receipts",
                        "Define billable population and reconciliation frequency in the agreement",
                        "Reprice using agreed census evidence before issuing any invoice",
                    ],
                    [
                        "Higher advisory tier becomes an unsupported savings promise",
                        "250 employees at $65 PEPM produce $195,000 annual receipts",
                        "Document expanded service scope and separately disclose other compensation",
                        "Reduce scope or retain existing arrangements when economics deteriorate",
                    ],
                    [
                        "Unbundling ignores stop-loss exposure and collateral carrying costs",
                        "$36,000 administration savings minus $45,000 added costs loses $9,000",
                        "Compare equivalent benefits and documented retained-risk assumptions together",
                        "Retain or competitively rebid the existing risk-adjusted structure",
                    ],
                    [
                        "NADAC reference omits missing-price and specialty-drug contractual treatment",
                        "Define reference timing, dispensing charges, rebates, and pricing fallbacks",
                        "Obtain auditable PBM terms covering every material drug category",
                        "Negotiate explicit fallback pricing before transferring pharmacy administration",
                    ],
                    [
                        "Opening capital disappears before the first collection cycle closes",
                        "$45,000 opening cash minus four $10,500 months leaves $3,000",
                        "Maintain funded reserves and a thirteen-week cash forecast",
                        "Reduce new commitments before provider funds subsidize operator expenses",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A winning determination is evidence; only reconciled incremental cash can pay the operator.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build a claim-level jurisdiction register linking plan funding, protected service category, applicable state law, and reviewer evidence before any paid filing.",
        "Implement receipt-based negotiation and IDR clocks with business-day calendars, delivery receipts, cooling-period tracking, and independent deadline review.",
        "Execute provider authority, expense-allocation terms, required HIPAA agreements, and named-user access controls before importing patient claim records.",
        "Reconcile every contingency invoice to incremental deposited payer cash after unrecovered fees and agreed casework costs, with refund and reversal reserves.",
        "Activate cohort intervention rules for missed deadlines, eligibility dismissals, overdue determinations, recoupments, and unexplained portal access restrictions.",
        "Keep TRACK_1 benefits advisory revenue separate, document PEPM populations and compensation disclosures, and stress-test eight weeks without new recovery cash.",
    ],
    "statutory_citations": [
        {
            "title": "42 U.S.C. § 300gg-111 — Preventing surprise medical bills",
            "url": "https://www.law.cornell.edu/uscode/text/42/300gg-111",
            "relevance": (
                "Establishes protected-service requirements, federal payment-dispute mechanics, "
                "permitted and prohibited considerations, and payment timing."
            ),
        },
        {
            "title": "45 CFR § 149.510 — Independent dispute resolution process",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.510",
            "relevance": (
                "Provides the federal negotiation, initiation, batching, cooling-period, determination, "
                "and fee framework; apply the effective provisions with controlling judicial decisions."
            ),
        },
        {
            "title": "45 CFR § 149.520 — Air ambulance independent dispute resolution",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-149/subpart-F/section-149.520",
            "relevance": (
                "Supports separate analysis of air-ambulance disputes rather than assuming all "
                "transportation claims follow the same federal pathway."
            ),
        },
        {
            "title": "45 CFR § 164.504(e) — Business associate contracts",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.504",
            "relevance": (
                "Defines required business associate contractual safeguards and relevant "
                "subcontractor obligations when handling protected health information."
            ),
        },
        {
            "title": "45 CFR § 164.312 — Technical safeguards",
            "url": "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.312",
            "relevance": (
                "Addresses electronic protected health information access control, audit controls, "
                "integrity, authentication, and transmission security."
            ),
        },
        {
            "title": "29 U.S.C. § 1108(b)(2)(B) — Group health plan service-provider compensation disclosures",
            "url": "https://www.law.cornell.edu/uscode/text/29/1108",
            "relevance": (
                "Provides the ERISA compensation-disclosure framework relevant to covered group "
                "health plan brokerage and consulting service arrangements."
            ),
        },
        {
            "title": "29 U.S.C. § 1144 — ERISA preemption and exceptions",
            "url": "https://www.law.cornell.edu/uscode/text/29/1144",
            "relevance": (
                "Informs the distinction between employee benefit plan regulation and state "
                "insurance regulation without replacing claim-specific surprise-billing jurisdiction analysis."
            ),
        },
    ],
}
