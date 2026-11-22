from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in judgment recovery, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "PACER Stay Checks, Lien Waterfalls, Recovery-Fee Reversals, Lawful Data Access & Capital Circuit-Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #8, Judgment Recovery, ranks #28 with a 79/100 Money-to-Manpower "
        "Score across a portfolio of 15 mapped plays. Its attractive fee economics "
        "collapse when operators buy face value instead of collectible priority, "
        "mistake client receipts for revenue, or enforce through bankruptcy and "
        "exemption defects. Canonical annual owner profit is $12,000 Conservative, "
        "$84,000 Base, and $200,000 Scaled; these outcomes require disciplined "
        "cost containment, not aggressive promises. This chapter isolates fatal "
        "intake defects, cash reversals, vendor-access failures, and misleading "
        "adjacent opportunities. Use docket evidence, dated asset waterfalls, "
        "transaction-level reconciliation, and explicit stop thresholds to protect "
        "capital. The question's 80% framing is rhetorical; no measured newcomer "
        "failure rate is asserted."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$60,000",
            "context": "Annual recognized service fees; client principal excluded",
            "note": "20% net margin; $12,000 owner profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$280,000",
            "context": "Annual recognized service fees; client principal excluded",
            "note": "30.0% net margin; $84,000 owner profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$500,000",
            "context": "Annual recognized service fees; client principal excluded",
            "note": "40% net margin; $200,000 owner profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Underwrite Collectible Priority Before Buying a Judgment Story",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is pricing the judgment's face amount instead "
                    "of the debtor's reachable equity. A $500,000 judgment against an "
                    "empty operating company is not a $500,000 asset pipeline. Begin "
                    "with the certified judgment, service history, appellate posture, "
                    "renewal calendar, recorded assignments, and exact debtor identity. "
                    "Match the entity through Secretary of State records, including "
                    "mergers and dissolved predecessors; an officer's address does not "
                    "make that officer personally liable. Search the relevant county "
                    "recorder, UCC filing office, and court dockets, then build an "
                    "asset-specific distribution waterfall. Illustratively, a $300,000 "
                    "realization less $210,000 senior secured debt, $30,000 sale expense, "
                    "and $40,000 applicable protected value leaves $20,000 before junior "
                    "claims and collection expense. A hypothetical 30% recovery fee "
                    "produces $6,000 service revenue, not $300,000. Spending $8,000 to "
                    "reach that result destroys contribution even if enforcement "
                    "succeeds. Treat this as screening arithmetic, not a legal priority "
                    "opinion: attachment, perfection, statutory liens, homestead rules, "
                    "ownership interests, and sale procedures can change the waterfall. "
                    "Require local counsel to validate the enforceable route before "
                    "committing nonrecoverable expense. Record each valuation's date "
                    "and evidence source so a stale broker estimate cannot silently "
                    "become today's collectible-equity assumption."
                ),
                (
                    "The next traps are procedural rather than commercial: defective "
                    "service, broken assignment chains, expired enforcement periods, "
                    "unrecorded liens, stayed judgments, and an assumed right to act "
                    "as counsel. A purchase agreement does not automatically authorize "
                    "a recovery company to represent another party, appear through "
                    "a nonlawyer, or bypass collection-agency licensing. Route filings, "
                    "debtor examinations, garnishments, and contested priority issues "
                    "through appropriately admitted counsel wherever required. Have "
                    "that counsel identify whether the proposed assignment genuinely "
                    "transfers ownership and which activities remain regulated. "
                    "Contractor labels do not change the underlying activity. Keep "
                    "separate dates for judgment entry, lien creation, lien expiration, "
                    "renewal eligibility, service completion, and the next enforceable "
                    "step; a single generic deadline field hides fatal differences. "
                    "An Airtable or SQLite register can surface missing evidence, "
                    "but the official docket and recorded instruments control. For "
                    "every material date, store the jurisdiction, triggering event, "
                    "rule citation, source document, and reviewer. Set internal "
                    "reminders at 180, 90, and 30 days before verified deadlines, "
                    "without treating those reminders as statutory periods. Reject "
                    "intake when standing or service remains unresolved after the "
                    "fixed diligence budget. Cheap defective paper becomes expensive "
                    "only after someone starts spending against it."
                ),
                (
                    "Consumer-debt misclassification and identity shortcuts create "
                    "another asymmetry: a small possible fee can expose the entire "
                    "operation. Determine the underlying transaction's purpose rather "
                    "than assuming every judgment against a company owner is commercial. "
                    "The federal Fair Debt Collection Practices Act defines covered "
                    "debt by personal, family, or household purpose under 15 U.S.C. "
                    "1692a(5); state collection statutes can reach different activities "
                    "or broader categories. A personal guaranty of business borrowing "
                    "is not automatically consumer debt, but its label alone is "
                    "insufficient evidence. Separate transaction classification from "
                    "the operator's collector status and licensing footprint. Likewise, "
                    "a judgment does not authorize unrestricted credit-report access, "
                    "motor-vehicle searches, impersonation, or account sharing. Document "
                    "a transaction-specific permissible purpose before using a consumer "
                    "report, and validate separate restrictions for other datasets. "
                    "Use public-record sources first, then licensed vendor products "
                    "only within the contracted purpose. Never use stolen credentials, "
                    "invented employment relationships, or a relative's identity to "
                    "obtain debtor information. Suspend a matter immediately after "
                    "an identity mismatch or unsupported access purpose. Those events "
                    "are not ordinary research friction: they undermine evidence "
                    "quality, invite vendor termination, and can create statutory "
                    "exposure that dwarfs the expected recovery fee."
                ),
            ],
            "table": {
                "caption": "Twelve Fatal Intake Traps and Their Evidence-Based Circuit-Breakers",
                "headers": [
                    "Fatal operating assumption",
                    "Evidence that exposes the defect",
                    "Economic or procedural failure mechanism",
                    "Mandatory containment and next action",
                ],
                "rows": [
                    [
                        "Face amount equals the debtor's collectible equity",
                        "Asset waterfall includes senior claims and liquidation costs",
                        "Large judgment balances conceal negligible reachable recovery proceeds",
                        "Price expected fee contribution after counsel validates priority",
                    ],
                    [
                        "Corporate officers automatically owe the entity's judgment",
                        "Judgment caption and liability findings identify actual obligors",
                        "Wrong-party enforcement generates expense without an enforceable obligation",
                        "Require a supported liability theory before targeting individuals",
                    ],
                    [
                        "A purchased judgment always conveys enforceable standing",
                        "Executed assignment chain connects every transfer without gaps",
                        "Missing ownership evidence defeats motions and delays collections",
                        "Resolve chain defects before paying acquisition consideration irrevocably",
                    ],
                    [
                        "Default judgments prove that service was effective",
                        "Service returns and docket challenges reveal procedural weaknesses",
                        "Vacatur risk erases leverage after enforcement costs accrue",
                        "Obtain counsel review before funding contested default enforcement",
                    ],
                    [
                        "Judgment life and lien duration are identical",
                        "Separate statutory calendars track judgment and lien expiration",
                        "Expired lien rights destroy priority despite surviving indebtedness",
                        "Maintain distinct verified deadlines with accountable human reviewers",
                    ],
                    [
                        "Any visible asset is available for levy",
                        "Ownership records and exemption analysis identify protected interests",
                        "Exempt or third-party property produces objections and liability",
                        "Exclude unsupported targets until ownership and exemptions resolve",
                    ],
                    [
                        "A recorder search establishes every competing claim",
                        "County records, UCC searches, and statutory claims reconcile",
                        "Unseen senior claims consume proceeds expected for juniors",
                        "Refresh jurisdiction-specific priority searches before irreversible enforcement spending",
                    ],
                    [
                        "Commercial branding removes all collection licensing obligations",
                        "Activity and jurisdiction matrix identifies applicable licensing requirements",
                        "Unlicensed work can interrupt collections and invalidate economics",
                        "Restrict activities until required licensing arrangements are verified",
                    ],
                    [
                        "Assignments eliminate restrictions on practicing law locally",
                        "Local representation rules distinguish ownership from permitted advocacy",
                        "Unauthorized representation jeopardizes filings and exposes the operator",
                        "Use admitted counsel for work requiring legal representation",
                    ],
                    [
                        "Every judgment supports unrestricted consumer report access",
                        "Documented purpose connects the request to lawful authority",
                        "Unsupported access creates statutory exposure and vendor suspension",
                        "Block restricted searches until the applicable purpose clears",
                    ],
                    [
                        "Old asset screenshots support current collection spending",
                        "Dated source records show intervening transfers and encumbrances",
                        "Stale equity assumptions overstate the expected recovery fee",
                        "Refresh material evidence before increasing the matter budget",
                    ],
                    [
                        "A large debtor portfolio solves weak individual underwriting",
                        "Cohort contribution reports expose repeated negative case economics",
                        "Correlated defects multiply losses rather than diversify them",
                        "Stop acquisition when matched cohorts breach contribution thresholds",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Pre-Flight Checks Before Irrecoverable Spending",
                "body": (
                    "A failed check blocks spending on the affected matter; it does "
                    "not become a note buried beneath the recovery forecast."
                ),
                "items": [
                    "Verify the debtor, enforceable judgment, service record, assignment chain, and any required local representation using linked source documents.",
                    "Refresh bankruptcy, appellate-stay, renewal, and lien-priority checks immediately before the proposed enforcement action.",
                    "Approve an asset-specific recovery waterfall that includes exemptions, senior claims, sale friction, counsel expense, and the operator's actual fee share.",
                    "Confirm licensing coverage, lawful dataset access, signed fee terms, authorized expense limits, and the exact account routing for client proceeds.",
                ],
            },
        },
        {
            "heading": "2. Treat Bankruptcy, Reversals, and Client Money as Separate Ledgers",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Bankruptcy is not merely a slower collection channel. Under "
                    "11 U.S.C. 362, a petition generally triggers an automatic stay "
                    "covering specified collection and enforcement acts, subject to "
                    "statutory exceptions. Do not wait for a mailed notice if reliable "
                    "information indicates a filing. Check PACER and the relevant "
                    "bankruptcy docket at intake, before each enforcement instruction, "
                    "and whenever a debtor, attorney, or payment processor reports "
                    "insolvency activity. A same-day check is an internal freshness "
                    "standard, not protection against a petition filed moments later. "
                    "Any credible filing signal pauses new collection activity pending "
                    "counsel review. Counsel determines the debtor identity, case "
                    "status, stay scope, applicable exceptions, and whether relief "
                    "is needed. Section 362(k) provides damages for qualifying injured "
                    "individuals after willful violations; other remedies may also "
                    "matter. Separately, discharge under 11 U.S.C. 524 can bar "
                    "collection of discharged personal liability even after the "
                    "bankruptcy case closes. Surviving liens require their own "
                    "analysis. Do not treat a closed docket, an existing writ, "
                    "or a debtor's informal permission as blanket authority to "
                    "resume. Record who reviewed the issue and exactly which "
                    "action may proceed before restarting automated reminders or "
                    "sending further instructions to enforcement personnel."
                ),
                (
                    "A cleared payment can still carry avoidance or restitution "
                    "risk. Section 547 of the Bankruptcy Code permits avoidance "
                    "of qualifying preferential transfers, generally examining a "
                    "90-day prepetition period and, for certain insider transfers, "
                    "a longer period. That timing alone does not establish liability: "
                    "the elements, defenses, creditor status, and transaction facts "
                    "matter. Sections 548 and 550 address other avoidance and "
                    "recovery questions, while section 546 limits particular avoidance "
                    "actions. Never reduce these provisions to a universal refund "
                    "deadline. A garnishment, settlement, or lien-related receipt "
                    "needs counsel's transaction-specific analysis when bankruptcy "
                    "emerges. Judgment vacatur, mistaken identity, duplicate payment, "
                    "and settlement rescission can create additional return demands "
                    "outside bankruptcy. Track gross receipts, beneficiary ownership, "
                    "earned fee allocation, unresolved disputes, and potential reversal "
                    "exposure separately. A contractual indemnity against an insolvent "
                    "client is weak protection; insurance exclusions and coverage "
                    "conditions need actual policy review. Set a documented cash "
                    "buffer based on identified exposure and available liquidity, "
                    "rather than assuming every distributed dollar is permanently "
                    "earned. A buffer is a cash-management decision, not automatically "
                    "an expense or a reduction of recognized revenue. Have the "
                    "accountant distinguish restricted cash, client liabilities, fee "
                    "recognition, and any supported loss provision."
                ),
                (
                    "The canonical cases use recognized service fees, never client "
                    "principal: $60,000 revenue less $48,000 costs yields $12,000 "
                    "owner profit; $280,000 less $196,000 yields $84,000; and "
                    "$500,000 less $300,000 yields $200,000. Margins are respectively "
                    "20%, 30.0%, and 40%. Team counts remain 1 FT plus 3 "
                    "contractors, 1 FT plus 3 contractors, and 2 FT plus "
                    "4 contractors; contractor counts are not full-time equivalents. "
                    "Illustratively, $1,000,000 of collected client principal at a "
                    "28% earned fee generates the Base case's $280,000 revenue "
                    "and a $720,000 client allocation before separately authorized "
                    "adjustments. That collection volume is an explanatory bridge, "
                    "not an additional scorecard assumption. Match bank receipts "
                    "to matter, payer, settlement terms, earned fee, client payable, "
                    "and distribution record. Use the applicable attorney trust "
                    "account or other legally required segregated arrangement; "
                    "never fund payroll from client allocations. In a stress "
                    "test against Base, an additional $12,000 failed-enforcement "
                    "expense, an $8,400 recognized-fee reversal, and $15,000 additional "
                    "defense expense reduce profit to $48,600. This is sensitivity "
                    "analysis, not a replacement scenario. The control objective "
                    "is to catch those departures before distributions and spending "
                    "make an otherwise manageable reversal impossible to absorb."
                ),
            ],
            "table": {
                "caption": "Receipt, Reversal, and Bankruptcy Exposure Reconciliation Matrix",
                "headers": [
                    "Receipt or event requiring review",
                    "Evidence preserved with the matter",
                    "Ledger and liquidity treatment required",
                    "Circuit-breaker before the next action",
                ],
                "rows": [
                    [
                        "Credible bankruptcy filing signal arrives during active enforcement",
                        "Petition identity and docket timestamp establish review context",
                        "Identify related receipts without assuming automatic fee entitlement",
                        "Pause enforcement instructions until counsel resolves stay scope",
                    ],
                    [
                        "Prepetition payment falls within a potential preference window",
                        "Transfer date and transaction facts support counsel's analysis",
                        "Track disputed exposure separately from unrestricted operating liquidity",
                        "Escalate before distributing cash implicated by identified exposure",
                    ],
                    [
                        "Settlement receipt contains both fees and client principal",
                        "Signed terms specify ownership and authorized expense deductions",
                        "Separate client liabilities from earned operator fee revenue",
                        "Require matched allocation before releasing any beneficiary distribution",
                    ],
                    [
                        "Court later vacates the judgment supporting prior recovery",
                        "Order text and restitution demands establish the dispute",
                        "Assess fee reversal and repayment obligations with advisers",
                        "Freeze affected distributions while counsel determines return obligations",
                    ],
                    [
                        "Payer disputes a duplicate or misdirected incoming transfer",
                        "Bank reference and matter identifier expose allocation errors",
                        "Hold unmatched funds outside the earned fee balance",
                        "Resolve identity and entitlement before issuing further distributions",
                    ],
                    [
                        "An insolvency notice follows an earlier client distribution",
                        "Distribution trail records each recipient and transfer amount",
                        "Model return exposure without assuming indemnity is collectible",
                        "Coordinate counsel and insurer notices under actual deadlines",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Contain the affected matter",
                    "action": "Pause collection instructions and affected distributions immediately.",
                    "detail": (
                        "Preserve the triggering notice, docket references, payment "
                        "identifiers, and action history; do not delete evidence or "
                        "attempt an improvised transfer to another account."
                    ),
                },
                {
                    "step": 2,
                    "title": "Establish the controlling facts",
                    "action": "Have counsel verify the order, debtor, transfer, and applicable restrictions.",
                    "detail": (
                        "Distinguish stay issues, discharge issues, avoidance demands, "
                        "vacatur, and ordinary reconciliation errors because their "
                        "remedies and response deadlines differ."
                    ),
                },
                {
                    "step": 3,
                    "title": "Reconcile exposure and available cash",
                    "action": "Match every implicated receipt to fees, client liabilities, and distributions.",
                    "detail": (
                        "Prepare a recipient-level transfer schedule and a liquidity "
                        "forecast; ask the accountant to classify any required "
                        "adjustment without treating client money as operating capital."
                    ),
                },
                {
                    "step": 4,
                    "title": "Resume only the documented permitted work",
                    "action": "Record counsel's action-specific direction and assign the next review date.",
                    "detail": (
                        "Update the docket register, vendor work queues, payment "
                        "instructions, and responsible reviewer before restarting "
                        "any previously paused activity."
                    ),
                },
            ],
        },
        {
            "heading": "3. Install Telemetry That Stops Margin Leaks and Access Failures",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Measure the denominator that actually drives profit. A recovery "
                    "rate calculated against judgments purchased this month mixes "
                    "fresh inventory with old receipts and produces false confidence. "
                    "Build intake cohorts by month, jurisdiction, debtor type, "
                    "enforcement route, and counsel; track cumulative realized fees "
                    "against cumulative direct costs for the same matters. Keep "
                    "open-case forecasts separate from realized contribution. Define "
                    "direct contribution as recognized fees less attributable counsel, "
                    "research, filing, service, investigator, and enforcement expenses. "
                    "Do not call it owner profit because shared payroll and "
                    "overhead remain. Illustratively, twelve matters producing $36,000 "
                    "fees against $24,000 direct costs contribute $12,000 before "
                    "overhead; a thirteenth matter consuming $5,000 without recovery "
                    "cuts that contribution to $7,000. Use internal tripwires: review "
                    "a mature cohort below 40% direct contribution margin, and "
                    "stop new intake in that route after two consecutive mature "
                    "cohorts fall below 25%. These are management thresholds, not "
                    "industry benchmarks or scorecard promises. Define maturity "
                    "before launch using the expected collection cycle, and "
                    "retain censored open matters in the dashboard. Otherwise, "
                    "closing bad files early while leaving optimistic files open "
                    "manufactures an attractive success rate without improving "
                    "cash generation or the quality of acquisition decisions."
                ),
                (
                    "Translate weak signals into bounded spending decisions. At "
                    "intake, estimate reachable proceeds, contractual fee share, "
                    "remaining direct expense, collection probability, and elapsed "
                    "time; show the assumptions rather than only a blended score. "
                    "A $20,000 reachable recovery at a 30% fee and a "
                    "50% collection probability produces $3,000 expected gross fees. "
                    "If another $4,000 is required before receipt, reject the "
                    "proposed step unless new evidence changes the inputs. Sunk "
                    "cost is not a reason to continue. Trigger human review "
                    "when cumulative matter spending reaches 75% of its authorized "
                    "budget, and require renewed authorization before exceeding "
                    "100%. Flag asset evidence older than 30 days before a "
                    "material new commitment, while using shorter intervals for "
                    "volatile assets. Track verified-action latency, not merely "
                    "emails sent: thirty days without a documented asset, docket, "
                    "or settlement development should trigger a case review. "
                    "The volume's $10,000–$75,000 startup capital, $2,000–$12,000 "
                    "monthly operating expense, and 6–24 months to first deal "
                    "can conflict sharply. Six months at $12,000 consumes $72,000 "
                    "before exceptional enforcement spending. Maintain a rolling "
                    "thirteen-week cash forecast and a longer runway model; stop "
                    "discretionary intake below three months of committed operating "
                    "cash unless funding is already secured."
                ),
                (
                    "Platform bans usually start with purpose drift, credential "
                    "sharing, prohibited automation, or ignored warnings rather "
                    "than an exotic technical failure. PACER, court portals, "
                    "LexisNexis Risk Solutions, and TransUnion products have "
                    "different access terms and permitted uses; a subscription "
                    "does not authorize every workflow. Store the vendor product, "
                    "named user, approved purpose, matter identifier, and access "
                    "event in an auditable log without retaining unnecessary "
                    "sensitive payloads. Use official exports or permitted "
                    "interfaces, rate limits, individual accounts, and prompt "
                    "offboarding. Never respond to suspension by rotating accounts, "
                    "borrowing a lawyer's login, masking request origins, or "
                    "buying leaked records. Stop the affected connector after "
                    "one authorization warning, one unexplained identity mismatch, "
                    "or repeated access-denied responses; obtain vendor clarification "
                    "before resuming. Deadline tracking must also fail visibly. "
                    "If a docket import fails, mark the affected calendar "
                    "unverified and assign a manual source check rather than "
                    "showing yesterday's green status. Reconcile each business "
                    "day's receipts by the next business day, and investigate "
                    "any unexplained client-balance difference immediately. Automate "
                    "exception detection, not legal conclusions. The operator "
                    "should see who owns each exception, what evidence resolves "
                    "it, and whether spending, communication, or distribution "
                    "remains blocked while the issue is open."
                ),
            ],
            "table": {
                "caption": "Internal Early-Warning Thresholds for Costs, Evidence, Cash, and Access",
                "headers": [
                    "Metric and precise measurement basis",
                    "Internal warning or stop threshold",
                    "Failure mode the threshold exposes",
                    "Required operator response and evidence",
                ],
                "rows": [
                    [
                        "Mature cohort contribution equals fees less attributable costs",
                        "Review below forty percent; pause after repeated sub-quarter margins",
                        "Aggregate receipts conceal structurally expensive enforcement routes",
                        "Audit matched cohorts and suspend the defective route",
                    ],
                    [
                        "Matter spending divided by its currently authorized budget",
                        "Review at seventy-five percent; renew authority before exceeding budget",
                        "Incremental requests turn weak cases into sunk-cost commitments",
                        "Recalculate expected fees and document the next spending decision",
                    ],
                    [
                        "Elapsed days since the last material asset verification",
                        "Refresh evidence beyond thirty days before material commitments",
                        "Stale ownership or lien information overstates reachable proceeds",
                        "Obtain current source evidence and rebuild the asset waterfall",
                    ],
                    [
                        "Unexplained difference between receipts and beneficiary-level ledger allocations",
                        "Investigate any difference; reconcile by next business day",
                        "Client principal becomes accidentally available for operating expenditure",
                        "Block affected distributions until records and balances agree",
                    ],
                    [
                        "Vendor authorization warnings and unexplained identity mismatch events",
                        "One credible warning immediately pauses the affected connector",
                        "Purpose drift or credential misuse threatens continued access",
                        "Preserve logs and obtain documented vendor clarification first",
                    ],
                    [
                        "Unrestricted cash divided by committed monthly operating expenditure",
                        "Pause discretionary intake below three months without secured funding",
                        "Long collection cycles exhaust capital before earned fees arrive",
                        "Update cash forecast and reduce uncommitted spending immediately",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four Veteran Habits That Preserve Optionality",
                "body": (
                    "Experienced operators buy evidence in stages and keep every "
                    "stage cheap enough to abandon when priority or authority fails."
                ),
                "items": [
                    "Commission a narrow lien-and-ownership review before a broad investigator package; stop if the waterfall cannot support the next dollar of enforcement expense.",
                    "Require counsel invoices to identify matter, task, and result so failed service attempts and repeated motion drafting cannot disappear inside aggregate billing.",
                    "Keep bankruptcy notices and assignment documents beside the receipt ledger; reversal analysis becomes faster when ownership and transfer history are already linked.",
                    "Negotiate milestone-based research scopes with explicit stop instructions; a useful negative finding should end spending rather than trigger a larger automatic package.",
                ],
            },
        },
        {
            "heading": "4. Quarantine Adjacent Plays Before They Import New Liabilities",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The mapped play unclaimed_property_escheatment_arbitrage, "
                    "State Treasury Escheatment & Unclaimed Corporate Warrant "
                    "Recovery, uses TRACK_1 intake rather than ordinary judgment "
                    "enforcement. Ingest state controller or treasury ledgers and "
                    "municipal or corporate uncashed-warrant registries for items "
                    "above $25,000, using authorized downloads and source terms. "
                    "Cross-match corporate officers through Secretary of State "
                    "filings, but require documentary authority from the actual "
                    "owner or lawful successor before signing recovery agreements. "
                    "An officer match is a lead, not proof of entitlement. "
                    "The play's 10–25% contingent finder-fee range is subordinate "
                    "to each state's statutory limits and timing restrictions. "
                    "California Code of Civil Procedure section 1582, for "
                    "example, imposes a 10% compensation ceiling and restricts "
                    "agreement timing. For an eligible $40,000 claim at a "
                    "permitted 10% fee, service revenue is $4,000; $1,200 "
                    "document and processing expense leaves $2,800 direct "
                    "contribution before overhead. The $40,000 asset never becomes "
                    "operator revenue. State clearly that owners may claim "
                    "directly for free. If the permitted fee is insufficient "
                    "or the agreement falls within a restricted period, defer "
                    "or decline rather than disguise compensation as document "
                    "charges. Uncashed warrants may require separate issuer "
                    "reissuance procedures before any escheat claim exists."
                ),
                (
                    "The second mapped play, "
                    "state_film_historic_brownfield_tax_credit_brokerage, State Film, "
                    "Historic Rehabilitation (HTC) & Brownfield Transferable Tax "
                    "Credit Placement, also belongs to TRACK_1. Its danger is "
                    "mistaking a certificate for an immediately usable transferable "
                    "asset. Match only certified state credits whose program "
                    "permits the contemplated transfer, and verify the buyer's "
                    "tax position, permitted tax type, usage year, carryforward "
                    "rules, transfer limits, filing steps, and potential recapture. "
                    "State transferability does not establish that federal historic "
                    "rehabilitation credits under 26 U.S.C. 47 can be sold "
                    "outright. For an illustrative eligible state credit with "
                    "$100,000 face value, a $92,000 negotiated purchase price "
                    "and separately disclosed $3,000 placement fee yield $3,000 "
                    "operator revenue, not $95,000 or $100,000. At $1,000 "
                    "direct diligence expense, contribution is $2,000 before "
                    "overhead; the buyer's initial total outlay is $95,000, "
                    "subject to the agreed transaction structure. These figures "
                    "are transaction assumptions, not market quotes or promised "
                    "tax savings. If eligibility, certification, or transfer "
                    "evidence fails, suspend settlement under written diligence "
                    "contingencies. Rematch only verified eligible credits and "
                    "taxpayers. Do not forward disputed certificates to new "
                    "buyers, imply agency endorsement, or treat escrowed purchase "
                    "funds as earned placement revenue."
                ),
                (
                    "Keep both adjacent plays outside the judgment collection "
                    "ledger until their entitlement, statutory terms, and fee "
                    "recognition conditions are established. They are two of "
                    "the volume's 15 mapped plays, not evidence that every "
                    "recovery method shares one license, contract, or settlement "
                    "workflow. An unclaimed-property claimant may own an asset "
                    "without owing the operator anything; a tax-credit buyer "
                    "may pay a discount yet lack usable tax capacity. "
                    "The same screening discipline applies across all three "
                    "lanes: identify the actual rights holder, verify the "
                    "transferable or enforceable right, calculate recognized "
                    "fees, and cap the next irreversible expense. Illustratively, "
                    "ten completed $40,000 property claims at lawful 10% "
                    "fees produce $40,000 service revenue, while ten completed "
                    "credit placements at $3,000 produce $30,000. Neither "
                    "figure includes the underlying $400,000 property value "
                    "or $1,000,000 credit face amount. These examples do "
                    "not add revenue to the canonical scenarios without "
                    "replacing another modeled fee source and accounting for "
                    "incremental costs. Build separate contracts, evidence "
                    "checklists, and reversal registers before expanding. If "
                    "a new lane needs unfamiliar licensing, entitlement "
                    "proof, or tax analysis, use qualified specialists and "
                    "a small capped pilot rather than subsidizing uncertainty "
                    "with client money from the core recovery business."
                ),
            ],
            "table": {
                "caption": "Adjacent-Play Entitlement, Fee, and Settlement Failure Matrix",
                "headers": [
                    "Mapped lane and concrete failure",
                    "Required entitlement or usability evidence",
                    "Illustrative fee economics and exposure",
                    "Fallback that limits irreversible capital",
                ],
                "rows": [
                    [
                        "Unclaimed property lead names an obsolete corporate officer",
                        "Current filings and succession documents establish claimant authority",
                        "Officer matching alone creates no collectible operator fee",
                        "Contact the verified rights holder through authorized channels",
                    ],
                    [
                        "Finder agreement exceeds the governing state's compensation limit",
                        "Current statutory text and signed terms establish permitted compensation",
                        "Forty-thousand-dollar claim at ten percent earns four thousand",
                        "Apply lawful caps and disclose free direct claiming",
                    ],
                    [
                        "Finder agreement falls within a statutory restricted period",
                        "Property delivery history and agreement dates resolve timing",
                        "Premature contracting jeopardizes collection of the contingent fee",
                        "Defer execution until the applicable statutory timing permits",
                    ],
                    [
                        "Uncashed warrant requires issuer reissuance rather than escheatment",
                        "Issuer confirmation establishes status and claimant documentation requirements",
                        "Registry face value remains owner property throughout processing",
                        "Use the issuer's documented procedure before pursuing treasury recovery",
                    ],
                    [
                        "State tax credit lacks verified transferability or buyer usability",
                        "Program certification and buyer tax review support contemplated transfer",
                        "Three-thousand-dollar placement fee depends on agreed earned-fee conditions",
                        "Suspend settlement and rematch only verified eligible participants",
                    ],
                    [
                        "Placement model assumes federal historic credits transfer outright",
                        "Program-specific statutory review separates federal and state treatment",
                        "Unsupported transfer assumptions erase expected placement contribution entirely",
                        "Exclude unsupported structures and obtain specialist transaction review",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "Buy verified collection rights, spend against reachable equity, and never "
        "mistake someone else's money for your margin."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        "Build a matter register linking debtor identity, service evidence, assignment chain, judgment deadlines, lien deadlines, and the responsible local attorney.",
        "Complete an asset-specific priority waterfall before authorizing research, acquisition, service, or enforcement expense beyond the initial diligence budget.",
        "Install event-driven bankruptcy checks and a documented pause procedure covering collection instructions, communications, and affected distributions.",
        "Reconcile receipts to earned fees and client liabilities daily, preserving recipient-level transfer records and identifying potential reversal exposure.",
        "Publish cohort contribution, budget utilization, evidence freshness, vendor warnings, and unrestricted-cash runway with named exception owners.",
        "Separate unclaimed-property and tax-credit intake, verify statutory limits and entitlement, and exclude underlying asset values from recognized service revenue.",
    ],
    "statutory_citations": [
        {
            "title": "11 U.S.C. 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": (
                "Defines stayed acts, exceptions, relief procedures, and remedies "
                "relevant to pausing post-judgment enforcement after a bankruptcy filing."
            ),
        },
        {
            "title": "11 U.S.C. 524 — Effect of discharge",
            "url": "https://www.law.cornell.edu/uscode/text/11/524",
            "relevance": (
                "Requires separate analysis of discharged personal liability rather "
                "than treating closure of a bankruptcy case as permission to collect."
            ),
        },
        {
            "title": "11 U.S.C. 547 — Preferences",
            "url": "https://www.law.cornell.edu/uscode/text/11/547",
            "relevance": (
                "Supplies preference elements, lookback provisions, and defenses "
                "for reviewing qualifying prepetition collection receipts."
            ),
        },
        {
            "title": "11 U.S.C. 548 — Fraudulent transfers and obligations",
            "url": "https://www.law.cornell.edu/uscode/text/11/548",
            "relevance": (
                "Identifies additional avoidance grounds requiring transaction-specific "
                "review when collected or transferred funds become disputed."
            ),
        },
        {
            "title": "11 U.S.C. 550 — Liability of transferee of avoided transfer",
            "url": "https://www.law.cornell.edu/uscode/text/11/550",
            "relevance": (
                "Addresses recovery from specified transferees and related defenses, "
                "supporting recipient-level payment records rather than blanket "
                "assumptions about who must repay."
            ),
        },
        {
            "title": "11 U.S.C. 546 — Limitations on avoiding powers",
            "url": "https://www.law.cornell.edu/uscode/text/11/546",
            "relevance": (
                "Provides limitations relevant to avoidance litigation; it does "
                "not create a universal deadline for every possible payment reversal."
            ),
        },
        {
            "title": "15 U.S.C. 1692a — FDCPA definitions",
            "url": "https://www.law.cornell.edu/uscode/text/15/1692a",
            "relevance": (
                "Defines covered consumer debt and collector status, requiring "
                "classification of the underlying transaction and operator activity."
            ),
        },
        {
            "title": "15 U.S.C. 1681b — Permissible purposes of consumer reports",
            "url": "https://www.law.cornell.edu/uscode/text/15/1681b",
            "relevance": (
                "Requires an applicable permissible purpose for consumer-report "
                "access; possession of a judgment is not unrestricted search authority."
            ),
        },
        {
            "title": "18 U.S.C. 2721 — Motor vehicle record privacy",
            "url": "https://www.law.cornell.edu/uscode/text/18/2721",
            "relevance": (
                "Restricts disclosure and use of personal information from motor "
                "vehicle records subject to enumerated permitted uses."
            ),
        },
        {
            "title": "California Code of Civil Procedure section 1582 — Recovery agreements",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1582.&lawCode=CCP",
            "relevance": (
                "Sets compensation, timing, and agreement requirements for covered "
                "unclaimed-property recovery arrangements, including a 10% ceiling."
            ),
        },
        {
            "title": "26 U.S.C. 47 — Rehabilitation credit",
            "url": "https://www.law.cornell.edu/uscode/text/26/47",
            "relevance": (
                "Governs the federal rehabilitation credit, which must be analyzed "
                "separately from state programs permitting particular credit transfers."
            ),
        },
        {
            "title": "26 U.S.C. 50 — Other special rules",
            "url": "https://www.law.cornell.edu/uscode/text/26/50",
            "relevance": (
                "Provides investment-credit recapture and related rules relevant "
                "when reviewing federal rehabilitation-credit structures."
            ),
        },
    ],
}
