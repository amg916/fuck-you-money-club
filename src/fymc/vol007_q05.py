from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in unclaimed property recovery, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Treasury Identity Defects, Finder-Fee Restrictions, Claim Reversals, Portal Suspensions & Cohort-Level Cash Controls",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #5, Unclaimed Property Recovery, holds Rank #04 with an 89/100 "
        "Money-to-Manpower Score, but strong economics require disciplined rejection of "
        "defective claims. Within the volume's 12 mapped plays, this chapter separates "
        "treasury recovery from adjacent freight-audit contingencies and identifies where "
        "identity errors, invalid agreements, duplicate submissions, portal abuse, and "
        "premature fee recognition destroy cash. The canonical annual owner profit cases "
        "are $15,000 Conservative, $95,625 Base, and $225,000 Scaled; client property is "
        "never operator revenue. Use claim-level evidence chains, state-specific contract "
        "checks, cohort contribution tests, and explicit stop conditions to protect those "
        "outcomes. The question's 80% figure is a framing device, not an established "
        "industry failure statistic."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; excludes client asset value",
            "note": "25% net margin; $15,000 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$255,000",
            "context": "Annual recognized service fees; excludes client asset value",
            "note": "37.5% net margin; $95,625 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$450,000",
            "context": "Annual recognized service fees; excludes client asset value",
            "note": "50% net margin; $225,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Reject defective ownership before purchasing another lead",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is treating a treasury search result as a receivable. "
                    "A matching surname, historical address, or employer proves only that further "
                    "research may be worthwhile; it does not establish entitlement. Separate "
                    "discovery, identity corroboration, authority, submission, adjudication, payment, "
                    "and fee collection into distinct claim states. Record the state property "
                    "identifier, holder name, reported owner, property category, source timestamp, "
                    "and evidence supporting each transition. Never merge two records solely "
                    "because a matching algorithm assigns a high similarity score. For an "
                    "individual, compare historical addresses and name changes against documents "
                    "the treasury actually accepts. For a corporation, reconcile the reported "
                    "entity with Secretary of State records, merger documents, and the authorized "
                    "signer's capacity. A dissolved subsidiary and its parent are not interchangeable "
                    "claimants. For an estate, identify the lawful representative rather than "
                    "assuming the nearest relative can sign. Use a protected evidence repository "
                    "with restricted access, not attachments scattered across contractor inboxes. "
                    "Airtable can hold operational identifiers while the sensitive documents remain "
                    "in a separately controlled workspace. Stop intake when identity conflicts remain "
                    "unresolved; paying for more outreach only compounds the cost of an unusable "
                    "claim and exposes another person's records."
                ),
                (
                    "The second cluster of traps is economic: buying stale lists, chasing tiny "
                    "balances, counting duplicate properties twice, and paying contractors for "
                    "submissions rather than accepted evidence. A listing with an undisclosed balance "
                    "cannot support a precise fee forecast; price the research exposure separately "
                    "until the amount is established. Consider an illustrative $600 property with "
                    "a permissible 10% fee: maximum gross service revenue is $60. Thirty minutes "
                    "of research at a $30 hourly loaded rate costs $15, and another hour of "
                    "document handling costs $30, leaving $15 before acquisition, software, rejection "
                    "risk, and collection work. That claim becomes destructive after one avoidable "
                    "rework cycle. By contrast, several verified properties belonging to one owner "
                    "may share an evidence package, but only where the receiving agencies accept "
                    "the same documents. Deduplicate using jurisdiction plus property identifier, "
                    "then link related claims without deleting their separate status histories. "
                    "Compensate researchers for verified ownership packages with documented quality "
                    "checks rather than raw lead counts. Establish a maximum research spend per "
                    "unqualified lead and require an explicit reason before exceeding it. A large "
                    "public balance attached to the wrong entity is less valuable than a modest "
                    "balance with clean authority and an economical evidence path."
                ),
                (
                    "Customer distrust is a unit-economics problem, not merely a branding problem. "
                    "The third cluster of traps includes treasury impersonation, artificial urgency, "
                    "concealing the free direct-claim route, and collecting identity documents before "
                    "explaining who operates the service. Use your actual business identity, describe "
                    "the source of the property lead, disclose that the owner can claim directly "
                    "without hiring you, and provide the official treasury address independently "
                    "of your engagement link. Never imply a government affiliation or invent an "
                    "expiration deadline. These shortcuts increase complaints, payment disputes, and "
                    "the chance that legitimate outreach infrastructure becomes unusable. Separate "
                    "permission to communicate from authority to submit a claim; a reply to an "
                    "email is not a signed engagement or an agency authorization. If commercial "
                    "email is used, implement the sender identification and opt-out requirements "
                    "of 15 U.S.C. § 7704 where applicable. Evaluate telephone and text outreach "
                    "under the applicable calling rules before enabling automated campaigns. Track "
                    "complaints by lead supplier, message version, and channel rather than averaging "
                    "them across the business. One substantiated impersonation complaint triggers "
                    "an immediate pause of the implicated template while evidence is preserved. "
                    "The remedy is a corrected process, not another sending domain."
                ),
            ],
            "table": {
                "caption": "Twelve Claim Defects That Convert Apparent Property Value Into Operator Loss",
                "headers": [
                    "Fatal beginner trap and its apparent attraction",
                    "Evidence revealing the actual failure mechanism",
                    "Economic or operational damage to the business",
                    "Circuit-breaker before additional money is committed",
                ],
                "rows": [
                    [
                        "Treating identical names as proof of ownership",
                        "Historical addresses and accepted identity records contradict",
                        "Research spending accumulates against an ineligible claimant",
                        "Require corroborated identity before requesting claim authority",
                    ],
                    [
                        "Assuming parent companies own every subsidiary balance",
                        "Merger instruments fail to transfer the relevant entitlement",
                        "Corporate claims stall while authority must be reconstructed",
                        "Trace the ownership chain through executed corporate documents",
                    ],
                    [
                        "Accepting a relative's signature without estate authority",
                        "Treasury requirements demand representative documents not yet obtained",
                        "Document costs exceed the remaining recoverable service fee",
                        "Verify the applicable estate pathway before engagement spending",
                    ],
                    [
                        "Buying recycled leads already worked by competing finders",
                        "Property identifiers duplicate existing active or closed records",
                        "Repeated outreach consumes budget and generates owner complaints",
                        "Deduplicate jurisdiction and property identifiers before list purchase",
                    ],
                    [
                        "Chasing small balances because intake appears nearly free",
                        "Loaded handling cost consumes most permitted fee proceeds",
                        "Minor evidence requests erase the entire claim contribution",
                        "Apply a documented research budget and minimum contribution",
                    ],
                    [
                        "Forecasting exact fees from listings without disclosed balances",
                        "Public search results provide no verified property amount",
                        "Revenue forecasts subsidize acquisition with unsupported expected receipts",
                        "Keep speculative balances outside the collectible fee forecast",
                    ],
                    [
                        "Paying contractors exclusively for raw submission volume",
                        "High submission counts accompany repeated missing-document rejection notices",
                        "Rework absorbs staff capacity without increasing accepted claims",
                        "Pay for verified packages and sample evidence quality",
                    ],
                    [
                        "Signing finder agreements during a restricted statutory interval",
                        "Jurisdiction dates place execution inside an invalidity period",
                        "Recovery occurs but the expected fee becomes unenforceable",
                        "Verify applicable dates and contract rules before signing",
                    ],
                    [
                        "Charging an adjacent industry's contingency on treasury claims",
                        "The applicable finder statute restricts compensation or terms",
                        "Excess fees create disputes and potential repayment exposure",
                        "Classify the recovery lane before selecting contract economics",
                    ],
                    [
                        "Using treasury branding to manufacture immediate customer trust",
                        "Messages imply public authority that the operator lacks",
                        "Complaints threaten channel access and create deception exposure",
                        "Identify the private service and direct treasury alternative",
                    ],
                    [
                        "Submitting duplicate claims to accelerate agency attention",
                        "Multiple confirmation numbers reference the same underlying property",
                        "Conflicting submissions create delays and increase administrative scrutiny",
                        "Maintain one controlled submission history per property identifier",
                    ],
                    [
                        "Recognizing disputed fees before the contractual earning event",
                        "Claim approval exists but payment conditions remain unmet",
                        "Reported margins conceal collection risk and refund obligations",
                        "Reconcile fee recognition with earned rights and reversals",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Use evidence reuse without recycling identity mistakes",
                "body": "Experienced operators reduce repeated work while preserving a separate entitlement trail for every property.",
                "items": [
                    "Build an owner-level evidence index, but record which document and version each treasury accepted for each individual claim.",
                    "Maintain historical corporate names and merger dates as search aliases; never let an alias automatically substitute the legal claimant.",
                    "Ask for the agency's exact deficiency reason before ordering another certificate, notarization, or archival search.",
                    "Compare suppliers on verified contribution per purchased lead after rework, not on advertised property balances or match counts.",
                ],
            },
        },
        {
            "heading": "2. Engineer around invalid agreements, reversals, and restricted access",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Finder economics are jurisdiction-specific, and a contract template is not a "
                    "portable operating license. California Code of Civil Procedure § 1582 addresses "
                    "agreement timing, compensation restrictions, and required agreement content; its "
                    "10% limit must be read with the section's timing and applicability rules. "
                    "Texas Property Code § 74.507 governs agreements to recover reported property, "
                    "including a 10% compensation ceiling and enforceability requirements. New York "
                    "Abandoned Property Law § 1416 provides a separate framework for recovery "
                    "agreements. Do not infer identical clocks, covered parties, exemptions, or "
                    "signature requirements from similar percentages. Before solicitation or signing, "
                    "record the governing program, property status, reporting or delivery dates "
                    "needed by that statute, finder registration requirements, permitted compensation, "
                    "required disclosures, and allowed representative activity. Where a date determines "
                    "whether an agreement is valid, obtain that date from an authoritative record "
                    "rather than substituting the day your researcher found the listing. A claim "
                    "can be genuine while the fee agreement is invalid. When requirements cannot "
                    "be satisfied, pause the paid engagement and give the owner the direct-claim "
                    "route; do not relabel the same recovery fee as research, processing, or "
                    "consulting to evade a restriction. Version every state-specific agreement "
                    "against its effective legal requirements."
                ),
                (
                    "A clawback is not one event. Distinguish an agency's recovery of an erroneous "
                    "property payment, a customer's demand to reverse an unearned fee, a card "
                    "chargeback, and an accounting credit issued after a service dispute. Each "
                    "requires different evidence and a different ledger entry. Approval notices "
                    "may precede disbursement, and a deposited payment may later become disputed "
                    "when ownership evidence proves defective. Define the fee-earning event, payer, "
                    "payment route, dispute procedure, and refund treatment in the valid agreement. "
                    "Prefer treasury payment directly to the rightful owner with a separately "
                    "documented service invoice where the program permits that arrangement. Do not "
                    "route client property through the operating account merely to make collection "
                    "easier. Custody changes the operational and legal analysis and must be evaluated "
                    "before implementation. An illustrative $10,000 owner recovery at a permissible "
                    "10% fee creates $1,000 of service consideration, not $10,000 of operator "
                    "revenue. If a $300 portion is later refunded, the ledger must reflect that "
                    "reversal rather than burying it as miscellaneous spending. Preserve the "
                    "agreement version, entitlement evidence, agency correspondence, payment confirmation, "
                    "and invoice together. A refund reserve based on observed dispute cohorts "
                    "supports liquidity planning but does not automatically replace the applicable "
                    "revenue-recognition policy."
                ),
                (
                    "Access failures often begin as productivity experiments: scripted logins against "
                    "portal restrictions, bulk harvesting beyond published permissions, shared claimant "
                    "credentials, forged authorization, and repeated submissions under alternate identities. "
                    "These shortcuts can trigger suspension, termination, or a permanent ban under "
                    "the applicable service terms, while deception and unauthorized access create "
                    "additional exposure. Treat a CAPTCHA, authentication challenge, or explicit rate "
                    "limit as a boundary, not an engineering puzzle to bypass. Use published "
                    "downloads, permitted interfaces, and agency-approved representative workflows. "
                    "Read-only access reduces mutation risk but does not authorize collecting every "
                    "record visible to an account. Keep a source register with permitted uses, "
                    "rate limits, credential owner, and revocation procedure. Use individual accounts "
                    "where supported and store secrets in a controlled password manager such as "
                    "1Password Business rather than a spreadsheet. Restrict contractors to assigned "
                    "cases, redact irrelevant identifiers, and remove access when assignments end. "
                    "One exposed identity document triggers containment, access review, and assessment "
                    "of applicable notification duties; it is not merely another service ticket. "
                    "Measure authentication errors and access-denial responses separately from ordinary "
                    "empty search results. When an interface rejects automation, stop the affected "
                    "job and switch only to an expressly permitted workflow, preserving legitimate "
                    "manual work elsewhere."
                ),
            ],
            "table": {
                "caption": "State Agreement Rules, Payment Defects, and Access Boundaries",
                "headers": [
                    "Authority or control requiring a specific review",
                    "Concrete evidence retained in the claim record",
                    "Failure mode that invalidates the expected economics",
                    "Required operator response before work can resume",
                ],
                "rows": [
                    [
                        "California Code of Civil Procedure section 1582",
                        "Applicable report dates and signed agreement version retained",
                        "Restricted execution timing or excess compensation undermines collection",
                        "Resolve statutory applicability before executing the recovery agreement",
                    ],
                    [
                        "Texas Property Code section 74.507 recovery agreements",
                        "Property details and compensation terms match statutory requirements",
                        "Improper terms make the expected service fee unenforceable",
                        "Use a current Texas-specific agreement for covered property",
                    ],
                    [
                        "New York Abandoned Property Law section 1416",
                        "Current recovery agreement requirements are documented by program",
                        "Imported contract language misses jurisdiction-specific restrictions or requirements",
                        "Review applicable terms before committing paid acquisition spend",
                    ],
                    [
                        "Agency correction of an erroneous owner payment",
                        "Payment reference and corrected entitlement determination remain linked",
                        "Collected fees become disputed after underlying ownership changes",
                        "Suspend collection and assess refund treatment against evidence",
                    ],
                    [
                        "Customer fee dispute following a completed recovery",
                        "Executed agreement and earned-fee calculation support the invoice",
                        "Unclear earning conditions convert successful claims into refunds",
                        "Reconcile the dispute before recording additional collectible fees",
                    ],
                    [
                        "Portal terms and authenticated representative access permissions",
                        "Permitted interface documentation and named account ownership retained",
                        "Unauthorized automation removes access to an entire workflow",
                        "Stop the affected integration and obtain permitted access",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before a paid claim enters production",
                "body": "Any failed check stops the affected claim; unrelated verified claims can continue through their established workflows.",
                "items": [
                    "Confirm the claimant's identity, legal entitlement, and signer's authority using the receiving program's accepted evidence.",
                    "Verify the governing finder rules, relevant dates, registration requirements, fee calculation, and direct-claim disclosure before agreement execution.",
                    "Confirm the submission channel permits the intended representative activity and that all access is explicitly authorized.",
                    "Calculate expected contribution after acquisition, evidence work, rework, collection, and reversal exposure; reject claims below the documented floor.",
                ],
            },
        },
        {
            "heading": "3. Detect margin leaks with cohort contribution and liquidity telemetry",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Anchor every dashboard to the canonical fee basis. Conservative produces "
                    "$60,000 in annual recognized service fees, $45,000 in implied total costs, "
                    "and $15,000 in owner net profit at 25%, with 1 FT + 2 C. "
                    "Base produces $255,000 in fees, $159,375 in costs, and $95,625 in "
                    "owner net profit at 37.5%, also with 1 FT + 2 C. Scaled "
                    "produces $450,000 in fees, $225,000 in costs, and $225,000 in owner "
                    "net profit at 50%, with 2 FT + 3 C. These costs are the "
                    "arithmetic residuals of the supplied scorecard, not a newly estimated staffing "
                    "budget. If every engagement hypothetically earned a lawful 10% fee, those "
                    "revenues would correspond to $600,000, $2,550,000, and $4,500,000 of underlying "
                    "recoveries respectively. Real fee mixes can differ, so never make that "
                    "illustration a property-volume commitment. Client recoveries remain outside "
                    "operator revenue. The $1,500–$8,000 monthly opex range describes an operating "
                    "planning range, not a cap on all annual scenario costs. Reconcile labor, "
                    "acquisition, variable fulfillment, and refunds explicitly. The 3–12 month "
                    "time to first deal means that a promising pipeline can coexist with "
                    "insufficient cash, particularly near the $5,000 startup-capital minimum."
                ),
                (
                    "Track contribution by acquisition cohort and jurisdiction rather than celebrating "
                    "gross approvals. Define claim contribution as earned service fees net of "
                    "reversals, less attributable acquisition, research, document procurement, submission, "
                    "and collection costs. Keep shared overhead separate so the cohort measure "
                    "does not masquerade as owner net profit. In an illustrative cohort of "
                    "100 purchased leads, $2,000 acquisition spending plus $3,000 research and "
                    "fulfillment spending creates $5,000 of direct cost. Ten completed claims "
                    "at $800 each produce $8,000 before reversals and $3,000 contribution "
                    "before overhead. Two full $800 fee reversals reduce that contribution "
                    "to $1,400; another $1,500 rework cycle makes it negative $100. "
                    "This sensitivity explains why approval rate alone is a weak operating "
                    "signal. Measure lead-to-qualified-owner conversion, qualified-to-authorized conversion, "
                    "first-pass document acceptance, earned-to-collected fee conversion, and reversal "
                    "dollars divided by the relevant earned-fee cohort. Preserve both counts "
                    "and dollars so one large claim cannot conceal widespread defects. Use "
                    "mature cohorts for conversion comparisons and label younger cohorts by age. "
                    "Otherwise, an improvement in sourcing may merely reflect older claims "
                    "finally paying while recent low-quality purchases have not reached adjudication. "
                    "Investigate every material variance at the source-record level before changing "
                    "staff targets."
                ),
                (
                    "Set circuit-breakers as internal management thresholds, not invented treasury "
                    "standards. For a rolling sample of at least 30 reviewed packages, a "
                    "first-pass deficiency rate above 15% pauses the responsible template or "
                    "research source for review. Any confirmed wrong-owner submission stops the "
                    "affected matching rule immediately, regardless of sample size. A reversal "
                    "rate above 5% of earned fees in a mature cohort triggers a reserve "
                    "review and freezes expansion of that cohort's acquisition channel. Treat "
                    "these starting thresholds as hypotheses to recalibrate with observed loss "
                    "severity and agency behavior. Monitor days from complete submission to "
                    "payment separately from days waiting for owner documents; otherwise, staff "
                    "can improve apparent speed by postponing the submission timestamp. Escalate "
                    "claims aging beyond twice the comparable jurisdiction's trailing median, "
                    "but check published processing updates before assuming a defect. Maintain "
                    "a thirteen-week cash forecast excluding owner property, unearned fees, and "
                    "speculative balances. A $12,000 unrestricted cash balance against $6,000 "
                    "of monthly net cash burn provides roughly two months of runway. "
                    "That is shorter than the stated first-deal window's lower end, so "
                    "additional lead purchases should stop unless committed receipts or new "
                    "capital close the gap. Pipeline value cannot pay current payroll."
                ),
            ],
            "table": {
                "caption": "Illustrative Early-Warning Thresholds With Explicit Denominators and Responses",
                "headers": [
                    "Metric and denominator used for operational review",
                    "Initial internal threshold requiring investigation or intervention",
                    "Evidence needed to distinguish delay from deterioration",
                    "Circuit-breaker protecting cash and legitimate claim throughput",
                ],
                "rows": [
                    [
                        "First-pass deficiencies divided by reviewed submission packages",
                        "More than fifteen percent across thirty reviewed packages",
                        "Agency deficiency codes grouped by document and preparer",
                        "Pause the defective template while unaffected submissions continue",
                    ],
                    [
                        "Confirmed wrong-owner submissions within each matching rule",
                        "Any confirmed occurrence triggers an immediate rule suspension",
                        "Original source records compared with claimant identity evidence",
                        "Review every open claim touched by that rule",
                    ],
                    [
                        "Reversed fee dollars divided by mature earned fees",
                        "More than five percent triggers channel expansion suspension",
                        "Refund causes separated from ordinary payment collection delays",
                        "Update liquidity reserves and repair the affected contract",
                    ],
                    [
                        "Submission age relative to comparable jurisdiction processing history",
                        "More than twice the trailing median requires investigation",
                        "Complete-submission timestamp checked against published agency processing updates",
                        "Resolve deficiencies before committing additional paid escalation work",
                    ],
                    [
                        "Unrestricted cash divided by expected monthly net burn",
                        "Less than three months prompts acquisition spending review",
                        "Thirteen-week receipts forecast excludes owner assets and speculation",
                        "Stop discretionary lead buying when committed cash is insufficient",
                    ],
                    [
                        "Interface access-denial events grouped by authorized integration",
                        "Any explicit prohibition or suspension stops affected automation",
                        "Response logs distinguish permission failures from empty searches",
                        "Use only documented permitted workflows while seeking clarification",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Reconcile the claim event ledger",
                    "action": "Join property identifiers, agreement versions, agency events, invoices, receipts, and credits.",
                    "detail": "Keep owner property movements separate from service-fee entries and investigate unmatched references before publishing the weekly dashboard.",
                },
                {
                    "step": 2,
                    "title": "Measure mature cohort contribution",
                    "action": "Calculate earned fees net of reversals and subtract attributable delivery and acquisition costs.",
                    "detail": "Group by source, jurisdiction, claimant type, and acquisition month; show shared overhead separately from contribution.",
                },
                {
                    "step": 3,
                    "title": "Apply targeted circuit-breakers",
                    "action": "Stop the defective matching rule, agreement, supplier, or integration when its threshold is breached.",
                    "detail": "Assign an accountable reviewer and preserve the underlying evidence rather than disabling unrelated verified claim work.",
                },
                {
                    "step": 4,
                    "title": "Release only after documented repair",
                    "action": "Review affected cases and validate the corrected workflow on a small authorized sample.",
                    "detail": "Record the defect, remediation, sample results, and restart decision; continue monitoring the next mature cohort for recurrence.",
                },
            ],
        },
        {
            "heading": "4. Keep freight contingencies separate and make automation fail safely",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The mapped play freight_detention_audit_contingency, Automated Parcel, LTL Freight "
                    "& Tariff Overcharge Contingency Auditing, belongs to TRACK_1 and is an "
                    "adjacent recovery workflow, not permission to import freight fees into "
                    "treasury claims. Ingest mid-market shippers' UPS, FedEx, and LTL EDI "
                    "billing feeds through authorized read-only interfaces, and obtain CBP Form "
                    "7501 entry summaries through an authorized importer or broker data channel. "
                    "There is no assumption that every carrier or customs document has a "
                    "public API. Match invoices to contracted rates, shipment characteristics, "
                    "service commitments, adjustment notices, and payment records before flagging "
                    "late-delivery SLA refunds, dimensional-weight errors, duplicate charges, freight "
                    "classification issues, or potential duty drawback. Carrier service guarantees "
                    "may be suspended, excluded, waived, or subject to short claim deadlines. "
                    "An algorithmic exception is therefore a research candidate, not a "
                    "collectible receivable. At a contractual 40% contingency within the mapped "
                    "35–50% range, $20,000 in verified, collected carrier credits produces "
                    "$8,000 of service fees and leaves $12,000 with the shipper. "
                    "If direct audit and collection work costs $3,000, contribution is "
                    "$5,000 before shared overhead and reversals. Keep this illustration "
                    "outside the canonical treasury scenarios unless actual booked service fees "
                    "are deliberately included and reconciled."
                ),
                (
                    "Duty drawback adds a distinct statutory evidence burden. Under 19 U.S.C. "
                    "§ 1313 and the applicable rules in 19 CFR Part 190, some "
                    "qualifying drawback provisions can return up to 99% of eligible duties, "
                    "taxes, and fees, but an entry summary alone does not establish "
                    "eligibility. The specific provision determines the required import, export "
                    "or destruction, merchandise, possession, and record evidence. Separate discovery "
                    "and data preparation from activities requiring a licensed customs broker "
                    "or another authorized filer under 19 U.S.C. § 1641. Never promise "
                    "a customs recovery simply because duties appear on Form 7501. "
                    "For illustration, $50,000 of duties fully eligible for a 99% "
                    "return yields $49,500 before service compensation; a separately valid "
                    "40% contingent service agreement would yield $19,800 only on that "
                    "realized recovery. Eligibility defects reduce the recovery base before "
                    "the fee is calculated. If service-guarantee refunds are unavailable, "
                    "apply the mapped fallback: pivot toward non-waivable dimensional-weight "
                    "and duplicate-charge recoveries where governing terms support that treatment, "
                    "plus LTL freight-class corrections and contract-rate benchmarking. Do "
                    "not assume every billing error survives every contractual deadline. "
                    "Benchmarking future rates creates prospective savings, not recovered cash, "
                    "and requires a separately defined compensation basis rather than a "
                    "fictional refund invoice."
                ),
                (
                    "The final asymmetric failure is allowing automation to convert one bad "
                    "assumption into hundreds of external acts. Record matching and claim "
                    "status tracking are the primary automation levers; signing, identity "
                    "attestation, and submission authority require controls appropriate to the "
                    "receiving program. Run matching changes against a retained set of "
                    "previously adjudicated examples, including common names, deceased owners, "
                    "renamed entities, and duplicate property records. Compare false-positive "
                    "rates before enabling broader use. A status worker should use an "
                    "idempotent event key so replaying an agency notification cannot create "
                    "another invoice or submission. A portal outage should create a "
                    "retry task within permitted limits, not mark every pending claim "
                    "rejected. Require two-person review for changes to payment instructions "
                    "and independently verify the request through an established contact "
                    "channel. Keep a dated change log and a reversible deployment "
                    "path for matching rules, document templates, and fee calculations. "
                    "Every week, sample accepted cases as well as rejected ones; "
                    "successful payment does not prove that the underlying process was "
                    "sound. Expand only when mature cohort contribution, available cash, "
                    "document quality, and permitted access remain intact. The small-team "
                    "advantage comes from eliminating repeatable defects, not from making "
                    "unverified submissions faster."
                ),
            ],
            "table": {
                "caption": "Freight-Audit Boundaries and Automation Controls That Preserve Recovery Economics",
                "headers": [
                    "Recovery lane or automated operation being evaluated",
                    "Evidence required before an exception becomes collectible",
                    "Concrete economic treatment or asymmetric failure exposure",
                    "Fallback when the original assumption does not hold",
                ],
                "rows": [
                    [
                        "Authorized UPS and FedEx service-guarantee refund auditing",
                        "Shipment commitments and applicable guarantee terms support eligibility",
                        "Suspended guarantees can eliminate the entire projected recovery",
                        "Shift toward supported billing corrections with valid deadlines",
                    ],
                    [
                        "Dimensional-weight and duplicate-charge exceptions within carrier invoices",
                        "Measured dimensions and invoice references substantiate each adjustment",
                        "Forty percent of twenty thousand produces eight thousand",
                        "Contest only documented errors supported by governing terms",
                    ],
                    [
                        "LTL freight-class corrections and negotiated contract-rate comparisons",
                        "Shipment characteristics and executed rate schedules support calculations",
                        "Prospective savings differ from realized collectible refund proceeds",
                        "Price benchmarking separately when no retrospective credit exists",
                    ],
                    [
                        "Potential duty drawback identified through customs entry records",
                        "Applicable import and export evidence supports statutory eligibility",
                        "Entry duties alone cannot establish a collectible drawback",
                        "Route eligible work through the appropriate authorized filer",
                    ],
                    [
                        "Automated claim-status polling and event ingestion workflows",
                        "Permitted interface use and unique event keys documented",
                        "Repeated events otherwise create duplicate invoices or submissions",
                        "Queue controlled retries without inventing a rejection status",
                    ],
                    [
                        "Changes to claimant payment instructions or representative details",
                        "Independent callback and second reviewer confirm authorized changes",
                        "One diverted payment can exceed many months of profit",
                        "Freeze the change while preserving the original instructions",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "A recovery business earns its margin by proving entitlement before spending cash, not by counting property it does not own.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Create a jurisdiction-by-program register covering finder registration, compensation limits, restricted timing, required terms, direct-claim disclosure, and authorized submission routes.",
        "Deduplicate every purchased lead by jurisdiction and property identifier, then verify identity and signatory authority before paying for deeper evidence work.",
        "Reconcile the $60,000, $255,000, and $450,000 annual fee scenarios to their exact costs and owner profits without including client asset value.",
        "Publish weekly mature-cohort contribution, first-pass deficiencies, fee reversals, claim aging, access-denial events, and thirteen-week unrestricted cash forecasts.",
        "Install targeted stop controls for wrong-owner submissions, prohibited interface activity, disputed payment instructions, and acquisition channels with deteriorating contribution.",
        "Keep freight_detention_audit_contingency contracts, customs authority, evidence requirements, and 35–50% contingency economics separate from state-treasury finder engagements.",
    ],
    "statutory_citations": [
        {
            "title": "California Code of Civil Procedure § 1582 — Agreements to locate or recover property",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1582.&lawCode=CCP",
            "relevance": "Establishes restrictions on recovery agreement timing, compensation, and required agreement content for covered California property.",
        },
        {
            "title": "Texas Property Code § 74.507 — Fee for recovery",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.74.htm#74.507",
            "relevance": "Sets compensation and enforceability requirements for agreements assisting recovery of covered unclaimed property.",
        },
        {
            "title": "New York Abandoned Property Law § 1416 — Agreements to locate abandoned property",
            "url": "https://www.nysenate.gov/legislation/laws/ABP/1416",
            "relevance": "Provides New York-specific restrictions and requirements that must be checked before using a recovery agreement.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Governs applicable commercial email practices, including misleading transmission information, identification, and opt-out handling.",
        },
        {
            "title": "19 U.S.C. § 1313 — Drawback and refunds",
            "url": "https://www.law.cornell.edu/uscode/text/19/1313",
            "relevance": "Defines drawback pathways and substantive eligibility conditions; duties listed on an entry summary alone do not establish entitlement.",
        },
        {
            "title": "19 CFR Part 190 — Modernized drawback",
            "url": "https://www.ecfr.gov/current/title-19/chapter-I/part-190",
            "relevance": "Supplies operational rules for applicable drawback claims, evidence, procedures, and recordkeeping.",
        },
        {
            "title": "19 U.S.C. § 1641 — Customs brokers",
            "url": "https://www.law.cornell.edu/uscode/text/19/1641",
            "relevance": "Defines customs business and broker licensing boundaries relevant when adjacent recovery services extend beyond data analysis.",
        },
    ],
}
