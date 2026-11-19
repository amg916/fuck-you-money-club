"""Volume 002: surplus funds recovery, chapters Q1 and Q2."""

_Q1 = {
    "id": "Q1",
    "chapter_id": "Q1",
    "chapter_number": 1,
    "question_number": 1,
    "slug": "what-is-surplus-funds-recovery",
    "question_prompt": "Q1: What Exactly Is Surplus Funds & Tax-Sale Overage Recovery?",
    "kicker": "Q1 / THE BIG MONEY PLAYBOOKS",
    "title": "What Exactly Is Surplus Funds & Tax-Sale Overage Recovery?",
    "subtitle": "Tax-deed overages, mortgage foreclosure excess proceeds, and the statutory rules separating them.",
    "layout_template": "opportunity_overview",
    "reading_time_minutes": 12,
    "executive_summary": "Surplus recovery connects documented claimants with cash remaining after a forced property sale pays the obligations specified by its governing statute. The opportunity is administrative and evidentiary, not ownership of abandoned money. Tax deeds, redeemable deeds, judicial foreclosures, and trustee sales produce different priority waterfalls, deadlines, and claim procedures. Tax lien certificates generally sell a lien rather than the property itself. A disciplined operator classifies the sale, reconciles actual deposited proceeds, establishes claimant standing, and builds the correct jurisdiction-specific packet before estimating a collectible fee.",
    "key_metrics": [
        {"label": "Tax deed example", "value": "$60,000", "context": "$92,000 paid bid less $32,000 statutory charges", "note": "Illustrative pool before claimant-priority allocation."},
        {"label": "Trustee sale example", "value": "$85,000", "context": "$310,000 proceeds less $225,000 expenses and secured debt", "note": "Junior liens can reduce the former owner's share."},
        {"label": "Required classification", "value": "4 sale families", "context": "Tax deed, redeemable deed, judicial sale, trustee sale", "note": "A lien certificate is not an immediate property-sale surplus."}
    ],
    "sections": [
        {
            "heading": "Start with the sale instrument, not the lead list",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Surplus funds recovery is the work of identifying excess sale proceeds, proving who may receive them, and completing the applicable distribution process. The recovery firm does not create the money or acquire it merely by finding a record. Its starting evidence is the sale instrument: a tax deed, redeemable tax deed, sheriff's return, or trustee's deed identifying the proceeding that generated the deposit. Record the parcel identifier, sale date, case number, selling officer, successful bidder, and actual funds received. An auction results spreadsheet is a prospecting source, not a bank reconciliation. A canceled sale, unpaid bid, postponed closing, or corrected judgment can erase an apparent surplus before a claimant has anything collectible.",
                "In a tax deed sale, the initial surplus calculation is the winning third-party bid actually paid minus the delinquent taxes, interest, penalties, and sale expenses payable under the applicable statute. Suppose the bidder pays $92,000 and the verified statutory charges total $32,000: the provisional surplus is $60,000. That pool is not automatically the owner's check. Governmental interests, other qualifying lienholders, and the entitled owner must be evaluated under the distribution rules. Florida section 197.582 supplies a tax deed distribution framework, including treatment of governmental liens and claims against remaining funds. Use the clerk's actual distribution ledger to identify what has already been paid instead of deducting the same lien twice from an advertised surplus figure.",
                "A tax lien certificate sale normally transfers a tax lien investment, not title to the underlying property. Bidding may determine interest or a premium; any premium follows its own statutory treatment and is not automatically excess equity payable to the owner. Redemption typically pays the certificate obligation without a property auction. A later deed proceeding can create surplus, but that requires a separate event and accounting. Redeemable deed auctions differ: they sell a deed subject to statutory redemption rights and can generate excess proceeds from the sale price. Track the redemption period, redemption event, and distribution restrictions separately. Do not classify a sale from an auction vendor's marketing label when the recorded instrument and statute describe a different transaction."
            ],
            "table": {
                "caption": "Identify the event that can create a distributable pool",
                "headers": ["Instrument", "Initial accounting", "Critical distinction"],
                "rows": [
                    ["Tax deed", "Paid bid less statutory tax and sale charges", "Remaining pool still has a priority waterfall"],
                    ["Redeemable deed", "Paid bid less authorized obligations", "Redemption can affect timing and entitlement"],
                    ["Tax lien certificate", "Lien purchase and possible bid premium", "No immediate property-sale equity distribution"],
                    ["Mortgage foreclosure sale", "Paid proceeds less sale expenses and foreclosed debt", "Junior interests precede residual owner equity"]
                ]
            }
        },
        {
            "heading": "Reconstruct the foreclosure waterfall dollar by dollar",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "For a judicial mortgage foreclosure, start with the winning third-party bid actually deposited and subtract the amounts the judgment and distribution order authorize: foreclosed mortgage debt, accrued interest, recoverable charges, and sheriff or court sale expenses. A $310,000 paid bid against a $218,000 updated judgment balance and $7,000 separately payable sale costs leaves an $85,000 provisional pool. Confirm that the judgment does not already include those costs. The case docket should supply the final judgment, sale confirmation where required, certificate or sheriff's return, registry deposit, and disbursement orders. A face-value bid by the lender using a credit against its debt is not equivalent to a third party depositing that amount as cash available for distribution.",
                "For a California nonjudicial trustee sale, Civil Code section 2924k orders proceeds through sale costs and expenses, the obligation secured by the deed of trust being foreclosed, subordinate liens in priority order, and the trustor or successor entitled to the remainder. Using the same $310,000 receipt, $7,000 sale expenses, and $218,000 secured obligation gives $85,000 before subordinate claims. If a validated junior lien receives $50,000, the residual owner pool is $35,000, not $85,000. A proposed 15 percent recovery fee on that residual would be $5,250 only if the governing rules permit that arrangement. This arithmetic illustrates allocation; it does not establish that any particular percentage or contract form is valid in that jurisdiction.",
                "These examples assume a senior mortgage foreclosure. If the foreclosing instrument is junior, senior interests may survive against the property instead of being paid from that sale's proceeds; blindly subtracting every recorded mortgage can therefore misstate the surplus. Conversely, ignoring subordinate claims overstates the owner's recovery. Obtain a title chronology rather than relying on the latest deed alone, and distinguish recorded balances from supported payoff claims. Bankruptcy stays, a vacated judgment, disputed heirship, or an interpleader proceeding can change the available route and timing. Keep separate fields for gross receipts, authorized sale deductions, remaining fund, contested claims, estimated owner allocation, and actual payout. Never describe the whole registry balance as recoverable owner money while competing interests remain unresolved."
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "A posted bid is not a collectible balance",
                "body": "Price the case only after the custodian confirms the deposit and the claimant's likely position in the waterfall.",
                "items": ["Reconcile sale receipts and prior disbursements.", "Separate cash bids from credit bids.", "Identify unresolved competing claims and redemption events."]
            }
        },
        {
            "heading": "Run Track 01: Distressed Asset Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The distressed_asset_recovery play, Distressed Asset Recovery, becomes a narrowly defined surplus operation when its inputs are public sale records, deposited-fund ledgers, title documents, claimant identity evidence, and current jurisdiction instructions. Start with one county and one sale family so that a small team learns the real document requirements instead of assembling incompatible packets. Store a source date and record locator for each input. A lead should advance from identified to fund-confirmed only after a named office verifies the balance or publishes a current ledger. Contact discovery is a separate workstream: a possible telephone match does not establish the person's identity, former ownership, entitlement, or authority to act for a deceased owner or dissolved company.",
                "Run the play as four steps: classify the sale and responsible office; reconcile the fund and priority chain; establish the claimant and assemble the applicable packet; track an authorized distribution and reconcile the fee. Each step should produce an artifact that another operator can inspect without repeating the investigation. Those artifacts are a jurisdiction record, a balance worksheet, a claimant evidence index, and a payout reconciliation. Where representation or a contested court filing requires counsel, route that component rather than presenting clerical assistance as advocacy. A useful handoff includes the docket, disputed issue, relevant deadline, and missing evidence. It should not merely say that the case looks complicated or ask counsel to reconstruct months of unindexed research.",
                "Measure verified-fund rate as confirmed positive balances divided by reviewed leads, packet acceptance as packets accepted without correction divided by submitted packets, and recovery conversion as paid claims divided by eligible submitted claims. Track median days from submission to payout separately from prospecting time. For example, 40 confirmed funds from 100 reviewed leads is a 40 percent verification rate; 12 accepted packets from 15 submissions is 80 percent first-pass acceptance. Neither statistic establishes profitability without case costs and claimant allocations. Track cash fee receipts, staff hours, record charges, and counsel costs by sale family. A large advertised balance with unresolved priority disputes may yield worse contribution per hour than a modest uncontested claim with a documented living owner."
            ],
            "sop_steps": [
                {"step": 1, "title": "Classify", "action": "Identify instrument and jurisdiction.", "detail": "Capture sale date, case number, statutory route, and custodian."},
                {"step": 2, "title": "Reconcile", "action": "Confirm receipts and priority deductions.", "detail": "Obtain the ledger and separate estimates from recorded payments."},
                {"step": 3, "title": "Substantiate", "action": "Document standing and prepare the correct claim.", "detail": "Index identity, title, authority, competing interests, and deadlines."},
                {"step": 4, "title": "Collect", "action": "Track the authorized payout.", "detail": "Reconcile claimant receipt and any separately authorized service fee."}
            ]
        },
        {
            "heading": "Replace the one-contract trap with segmented recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The naive approach buys a national list, quotes a fixed share of every posted balance, and sends one assignment agreement to every former owner. Its failure is observable before litigation: clerks reject the named payee, trustees demand a different claim procedure, and customers discover that the promised amount ignored junior liens. A signed document does not change a statutory priority, revive an expired claim, or authorize representation that the operator cannot provide. Segment the workflow by state, county, sale mechanism, fund age, and claimant type. Maintain dated versions of local instructions and record the reason for each contract variant. Do not treat a successful packet in one Florida county as evidence that a California trustee must accept it.",
                "Use the forensic comparison below as a diagnostic worksheet rather than a slogan. A rejected assignment belongs in the contract-route denominator, while a missing death certificate belongs in the evidence-defect denominator. Combining them into a generic rejection count prevents corrective action. When the owner is deceased, determine whether the procedure accepts heir evidence or requires an estate representative; when the owner is an entity, identify the person authorized to act and the entity's current status. An operator should be able to explain precisely why the next document is needed. Asking every claimant for every possible record wastes time, increases exposure of sensitive information, and produces large packets that still omit the one required fact.",
                "Economics follow the verified route. On a $35,000 residual allocation, a hypothetical permitted $5,250 fee less $900 in direct case expense leaves $4,350 before overhead and taxes. If the owner receives only $10,000 after a competing claim succeeds, the same hypothetical percentage produces $1,500 and just $600 before overhead. Keep that sensitivity visible when deciding how much research to fund. Never substitute an estimated surplus for a receivable in the firm's cash forecast. Close the case only when the custodian's distribution, the claimant's receipt, and the firm's earned fee reconcile. Preserve the evidence index and rejection history so the next case starts with improved local knowledge rather than another generic contract and another avoidable delay."
            ],
            "table": {
                "caption": "Forensic contract and procedure diagnostics",
                "headers": ["Naive One-Contract-Fits-All Trap", "Detection Metric", "Jurisdiction-Segmented Recovery Fallback"],
                "rows": [
                    ["Universal assignment and payee", "Rejected assignment count / assignment submissions", "Use the jurisdiction's accepted claimant and payment route"],
                    ["Fee on posted gross balance", "Quoted balance minus supported owner allocation", "Quote against documented residual and applicable fee rules"],
                    ["Same packet for every owner", "Evidence corrections / submitted packets", "Separate living owner, estate, trust, and entity evidence"],
                    ["One nationwide deadline", "Cases without a sourced deadline / active cases", "Calendar the statute, sale event, and actual notice separately"]
                ]
            }
        }
    ],
    "pull_quote": "The bid creates a pool; the priority chain determines whose money it is.",
    "diagram_id": "diag-01-end-to-end-workflow",
    "action_checklist": [
        "Identify the sale instrument before calculating surplus.",
        "Confirm deposited cash and subtract only supported statutory deductions.",
        "Reconstruct lien priority and distinguish the pool from the owner allocation.",
        "Run distressed_asset_recovery through all four documented steps.",
        "Use the jurisdiction-specific packet, contract route, and deadline.",
        "Reconcile actual disbursement before recording a collected fee."
    ],
    "statutory_citations": [
        {"title": "Fla. Stat. section 197.582", "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.582.html", "relevance": "Tax deed proceeds, distribution priorities, and claims against remaining funds; consult the current text for the applicable procedure."},
        {"title": "Cal. Civ. Code section 2924k", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=2924k.", "relevance": "Nonjudicial trustee sale proceeds waterfall: expenses, secured obligation, subordinate interests, and residual entitlement."}
    ]
}

_Q2 = {
    "id": "Q2",
    "chapter_id": "Q2",
    "chapter_number": 2,
    "question_number": 2,
    "slug": "who-pays-and-where-surplus-sits",
    "question_prompt": "Q2: Who Pays, Why They Pay & Where Excess Proceeds Sit",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & Where Excess Proceeds Sit",
    "subtitle": "County treasurers, clerks of court, foreclosure trustees, and escheatment clocks.",
    "layout_template": "executive_summary",
    "reading_time_minutes": 12,
    "executive_summary": "The claimant owns the entitlement; the custodian controls the payment process. Surplus may sit with a tax collector, county treasury, court registry, sheriff, or private foreclosure trustee, and each office has different records and release requirements. Successful recovery follows the money from sale receipt through deposit, distribution order, issued warrant, and possible state transfer. This chapter separates claim deadlines from unclaimed-property clocks, explains direct claimant payment, and applies the state treasury recovery play to aged warrants and transferred proceeds without mistaking a public list for proof of ownership.",
    "key_metrics": [
        {"label": "Custody map", "value": "5 office types", "context": "Tax collector, circuit clerk, superior court registry, trustee, sheriff", "note": "County treasury may hold cash while another office adjudicates claims."},
        {"label": "Aging screen", "value": "1-5 years", "context": "Common unclaimed-property screening range, depending on state and category", "note": "Not a universal surplus transfer deadline or extension of claim rights."},
        {"label": "Transfer reconciliation", "value": "100% matched", "context": "Target for cases advanced as state-held funds", "note": "Match county remittance evidence to the state property record."}
    ],
    "sections": [
        {
            "heading": "Map custody, decision authority, and payment authority separately",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Who pays has two answers: the successful bidder supplies the sale proceeds, while the office or trustee holding the remaining money issues the distribution. That custodian pays because a statute, accepted claim, court order, or trustee distribution process establishes entitlement, not because the recovery firm discovered the lead. Build three separate fields for cash custodian, claim decision maker, and payment issuer. A county treasurer may hold pooled cash while the tax collector receives claims and another county body authorizes distribution. Calling only the auction vendor can leave the operator with a sale price but no current balance. Request the deposit reference, remaining principal, prior distributions, hold status, and office responsible for the next action before contacting a claimant about a specific recoverable amount.",
                "The County Tax Collector commonly administers tax-sale accounting and excess-proceeds notices, although the county treasury may physically hold the funds. A Clerk of the Circuit Court can hold tax deed surplus or foreclosure registry deposits where local law assigns that function. A Superior Court Clerk Registry holds court-deposited funds and generally releases them through the applicable court procedure. These are jurisdiction-specific roles, not interchangeable national job descriptions. For each county, obtain the official excess-proceeds instructions and registry payment requirements. Record whether claims are administrative submissions, motions in an existing case, or another prescribed procedure. A downloadable claimant form does not establish that the office can resolve disputed priority without a judge, nor that the recovery firm may appear for the claimant.",
                "A Private Foreclosure Trustee may initially retain nonjudicial sale surplus, request evidence from claimants, distribute under the statutory waterfall, or deposit disputed money with a court through the applicable process. A Sheriff's Civil Division may collect judicial sale proceeds and then remit them to a clerk or distribute them as directed. The sheriff's return is therefore a trail marker, not proof that the sheriff still holds cash. Ask for the transfer date, receiving registry, case reference, and amount. Preserve both ends of the handoff. If the original office reports a zero balance, distinguish payment to the claimant, payment to lienholders, transfer to another custodian, and reversal of the sale. Each explanation leads to a different next step and a different economic outcome."
            ],
            "table": {
                "caption": "Custodian routing map",
                "headers": ["Office", "Record to request", "Release or handoff evidence"],
                "rows": [
                    ["County Tax Collector", "Tax sale excess-proceeds ledger", "Accepted claim and county payment authorization"],
                    ["Clerk of the Circuit Court", "Tax deed file or foreclosure registry ledger", "Applicable clerk procedure or distribution order"],
                    ["Superior Court Clerk Registry", "Case-linked deposit record", "Court-directed registry disbursement"],
                    ["Private Foreclosure Trustee", "Trustee sale accounting and claim notice", "Distribution statement or court deposit reference"],
                    ["Sheriff's Civil Division", "Sale return and remittance record", "Court-directed payment or transfer to clerk"]
                ]
            }
        },
        {
            "heading": "Structure direct payment and repair the address trail",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Properly structured recovery normally asks the court, county, or trustee to pay the entitled claimant directly rather than routing the entire recovery through the operator's ordinary business account. The approved distribution can be a check, county warrant, or electronic payment where the custodian offers that method. A court registry is not necessarily an escrow account in the contractual sense; use the office's terminology and instructions. Submit the claimant's verified payee name, mailing address, and required payment documents through the official channel. Do not promise a wire merely because the claimant prefers one. If separate payment of an operator fee is permitted, the agreement and distribution instructions must support it; otherwise invoice the claimant under the valid arrangement after receipt.",
                "For an illustrative $40,000 owner allocation and a permitted $4,000 fee, direct payment might mean a $40,000 county check to the claimant followed by the claimant's $4,000 payment to the firm. A different jurisdiction may accept a properly authorized split, but that is not the default assumption. Record the distribution date, payee, instrument number, gross amount, fee basis, and cleared fee receipt separately. The issued check date is not always the claimant's receipt date, and a canceled warrant is not a paid claim. Bank details require verification through an independently established contact channel; a last-minute email changing the destination should not override the authenticated claimant record. Preserve only the sensitive evidence needed for the claim and restrict access to payment information.",
                "Former owners frequently miss notices because the government's last recorded address is the very property they lost. Displacement, forwarding expiration, tenancy changes, estate administration, and returned mail can break that chain. Do not turn this practical failure mode into an unsupported claim that a measured majority never receive notice. Inspect the notice certificate, mailing address, returned envelope, and any subsequent address update to understand this particular file. Search authorized public records for a current contact route and explain the sale date, holding office, and independent verification method in outreach. Never impersonate the custodian or imply that payment requires hiring the firm. Show the claimant how to confirm the fund and the available self-claim procedure before discussing the optional service and its cost."
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Follow the payee, not just the check",
                "body": "A release is complete only when the correct claimant receives the authorized amount and the fee is reconciled separately.",
                "items": ["Verify identity and authority against the claim record.", "Confirm payment instructions using an independent channel.", "Distinguish issued, returned, canceled, reissued, and cleared payments."]
            }
        },
        {
            "heading": "Separate claim deadlines from county-to-state aging clocks",
            "epistemic_status": "statutory_fact",
            "paragraphs": [
                "There is no single national escheatment clock for excess proceeds. A one-to-five-year range is useful for screening certain unclaimed-property categories across states, but it is not a rule that every county surplus moves to a state treasury within that interval. Some statutes impose an earlier deadline to claim the underlying sale surplus; others govern uncashed warrants, court deposits, abandoned property reports, or local disposition of unclaimed balances. Those events can have different starting dates and consequences. Build separate dates for sale, deed recording, notice, claim cutoff, payment issuance, last relevant owner activity where applicable, holder reporting, and state receipt. Never assure an owner that a treasury search will restore a right already lost under the sale-specific statute.",
                "California Revenue and Taxation Code section 4675 provides an excess-proceeds claim framework tied to parties of interest and a one-year period following recordation of the tax deed to the purchaser. Recordation is not necessarily the auction date. Obtain the recorded deed and calculate from the statutory event rather than the date a lead vendor exported its list. Texas Tax Code section 34.04 provides a petition route for excess proceeds held by the court clerk, with a two-year period following the sale and statutory allocation requirements. The Texas process is not interchangeable with California's administrative tax-sale claim route. Read related provisions and current local instructions before deciding where an unclaimed balance goes after the claim period; expiry does not automatically mean a searchable state asset remains.",
                "An issued county warrant introduces another timeline. The county may void a stale instrument, allow reissue, retain an unpaid liability, or report qualifying property under the state's unclaimed-property regime. Determine which event actually happened by obtaining the warrant register and any cancellation or remittance record. A warrant's printed expiration date is not itself proof of forfeiture, and an old issue date is not proof of state transfer. If the county says the balance was remitted, request the holder report year, property category, amount, and available transfer reference. Then reconcile against the state record. A courthouse deadline, warrant validity period, and state holding period should occupy separate worksheet columns, with a source and responsible office for each unresolved question."
            ],
            "table": {
                "caption": "Four clocks that must not be conflated",
                "headers": ["Clock", "Starting evidence", "Operational consequence"],
                "rows": [
                    ["California tax sale claim", "Recorded tax deed; section 4675", "Calendar the applicable one-year claim period"],
                    ["Texas excess-proceeds petition", "Sale record; section 34.04", "Calendar the applicable two-year petition period"],
                    ["Uncashed county warrant", "Issue and cancellation register", "Determine reissue rights and unpaid liability status"],
                    ["State unclaimed-property reporting", "Applicable property category and holder report", "Verify actual remittance rather than assume transfer"]
                ]
            }
        },
        {
            "heading": "Run Track 01: State Treasury Escheatment & Unclaimed Corporate Warrant Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The unclaimed_property_escheatment_arbitrage play, State Treasury Escheatment & Unclaimed Corporate Warrant Recovery, extends the investigation when sale proceeds become an aged county payment or are demonstrably transferred to the state. Its inputs are county surplus ledgers, warrant registers, holder remittance records, state property listings, historical owner addresses, and evidence of current claimant authority. Intercepting an aged warrant means identifying and resolving it for its lawful claimant before another administrative handoff, not diverting payment. Corporate warrants require special care: a similarly named entity, a renamed company, and a dissolved business are not automatically the same claimant. Link the original payee to the present legal entity through official entity records, merger documents, or other required succession evidence.",
                "Work the play in four stages: locate the county item, trace its present custody, establish the claimant's continuity, and submit through the current holder's procedure. Suppose a county ledger shows a $24,000 owner payment issued three years ago. The register shows cancellation, and a remittance record later shows $24,000 reported to the state. Match the owner's name, address, holder, and available property reference before opening the state claim. If the county instead confirms an outstanding reissuable warrant, pursue reissue there and avoid filing a duplicate state claim. A state search with no match is inconclusive; reporting batches, masked amounts, naming differences, and processing delays may require a holder inquiry rather than an immediate conclusion that the money disappeared.",
                "Track custody-resolution rate, documented-transfer match rate, claimant-authority completeness, first-pass acceptance, and days from complete submission to cleared payment. Define the denominator for each metric: finding ten state listings among fifty searched names is not a recovery rate. If eight of ten alleged transfers match actual state records, the documented-transfer match rate is 80 percent, and the other two remain unresolved rather than collectible inventory. Price the work using the rules applicable to the current asset and claim route, including any restrictions on locator agreements, fees, timing, or assignments. Close duplicate county and state records under one internal case identifier. The durable advantage is an auditable chain from original sale to present custodian to entitled claimant, not a collection of aging spreadsheets advertising the same dollars twice."
            ],
            "sop_steps": [
                {"step": 1, "title": "Locate", "action": "Find the original surplus or aged warrant.", "detail": "Capture sale, claimant, amount, instrument, and source date."},
                {"step": 2, "title": "Trace", "action": "Confirm present custody.", "detail": "Match cancellation, reissue, registry transfer, or state remittance evidence."},
                {"step": 3, "title": "Establish", "action": "Prove claimant continuity and authority.", "detail": "Resolve name changes, estates, corporate succession, and address history."},
                {"step": 4, "title": "Recover", "action": "Submit to the verified current holder.", "detail": "Track deficiencies, direct payout, fee receipt, and duplicate closure."}
            ]
        }
    ],
    "pull_quote": "An old balance is a lead; a traced custody chain is a recoverable case.",
    "diagram_id": "diag-04-jurisdiction-fee-caps",
    "action_checklist": [
        "Identify the cash holder, decision maker, and payment issuer separately.",
        "Trace sheriff and trustee handoffs to the receiving registry.",
        "Confirm a current claimant address without misrepresenting the firm's role.",
        "Calendar claim, warrant, reporting, and transfer dates independently.",
        "Match alleged state transfers to holder evidence and treasury records.",
        "Apply unclaimed_property_escheatment_arbitrage without duplicate claims.",
        "Reconcile direct claimant receipt and the separately earned fee."
    ],
    "statutory_citations": [
        {"title": "Cal. Rev. & Tax. Code section 4675", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=4675.", "relevance": "California tax-sale excess-proceeds claims, parties of interest, and the claim period following tax deed recordation."},
        {"title": "Tex. Tax Code section 34.04", "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm", "relevance": "Texas petition procedure, timing, and allocation for excess proceeds held by the court clerk; read related disposition provisions separately."}
    ]
}

CHAPTERS_1_TO_2 = [_Q1, _Q2]

