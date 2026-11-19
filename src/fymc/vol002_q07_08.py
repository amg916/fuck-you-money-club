"""Volume 002 operating chapters: title underwriting and investigative tools."""

CHAPTER_7 = {
    "id": "Q7",
    "chapter_id": "Q7",
    "chapter_number": 7,
    "question_number": 7,
    "slug": "title-underwriting-and-deceased-claims",
    "question_prompt": "Q7: How do title, lien priority, and succession determine who receives surplus?",
    "kicker": "Q7 / THE BIG MONEY PLAYBOOKS",
    "title": "The Complete Operating Process: Chain-of-Title, Lien Waterfall & Deceased-Owner Claims",
    "subtitle": "Underwriting vesting deeds, O&E encumbrance reports, corporate reinstatements, and probate surplus packets.",
    "layout_template": "research_exhibit",
    "reading_time_minutes": 12,
    "executive_summary": "A surplus balance is not an owner entitlement until the file establishes vesting, surviving claims, and authority to receive payment. This chapter turns recorder documents into a defensible distribution packet: reconstruct the relevant ownership snapshot, reconcile encumbrances against releases, calculate a documented waterfall, and identify the proper claimant when an entity has dissolved or an owner has died. The worked example allocates a $142,000 fund without confusing gross proceeds with recoverable owner money. Probate sourcing becomes useful only when succession evidence connects the historical owner to an authorized recipient.",
    "key_metrics": [
        {"label": "Illustrative fund", "value": "$142,000", "context": "Surplus already deposited after sale charges", "note": "Not the winning bid or property value."},
        {"label": "Owner remainder", "value": "$98,000", "context": "After two assumed allowed claims", "note": "Before recovery fees or additional estate expenses."},
        {"label": "Each co-owner", "value": "$49,000", "context": "Two established equal interests", "note": "Subject to the actual distribution order."},
    ],
    "sections": [
        {
            "heading": "1. Establish the historical vesting snapshot",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Start with the actual surplus ledger, sale case number, parcel legal description, and the jurisdiction's rule identifying whose interests attach to the fund. Pull the Last Deed of Record and reconstruct vesting at the moment of lis pendens or tax-sale certification where that event is relevant; do not assume either date universally controls entitlement. Record the notice date, sale date, deed recording date, and any statutory ownership cutoff separately. A current assessor screen can identify today's taxpayer while concealing the former owner who matters to this distribution. Order the complete recorded deed image, including exhibits, rather than trusting a search-result caption. Compare lot, block, subdivision, and metes-and-bounds text against the sale instrument before researching the person named on the first page.",
                "Work backward through the grantor and grantee indexes until every transfer into the relevant owner is supported. Search spelling variants, former married names, entity suffixes, and trustee capacities, then search forward through the sale and distribution period for corrections, assignments, deaths, or competing conveyances. Capture instrument number, execution date, recording date, grantor capacity, grantee capacity, and ownership fraction in a chronology. Two names on a deed do not automatically establish equal beneficial shares, and joint tenancy can change the succession analysis after death. Preserve the exact vesting language. A quitclaim deed, corrective deed, or transfer into a trust needs its own explanation rather than an assumption that the newest name inherits every surplus right.",
                "An Ownership & Encumbrance report is an index-driven research product, not a substitute for reading instruments or a universal insurance commitment. Specify the parcel, effective search date, names searched, and required copies when ordering it. Reconcile its ownership finding against the deed chronology and its exceptions against judgments, mortgages, tax liens, association claims, municipal assessments, and recorded notices. Mark any coverage gap between the report's effective date and your filing date. A missing attachment, omitted alias, or incorrectly indexed instrument can materially change who gets paid. Maintain an exception log containing the suspected defect, evidence requested, responsible researcher, and resolution. Price the file only after the unresolved exceptions are visible, rather than letting an attractive surplus number silently become assumed inventory.",
            ],
            "table": {
                "caption": "Historical ownership evidence register",
                "headers": ["Record", "Extract", "Failure to resolve"],
                "rows": [
                    ["Vesting deed and exhibits", "Capacity, shares, legal description", "Wrong claimant or parcel"],
                    ["Lis pendens / sale certification", "Event date and case reference", "Wrong entitlement snapshot"],
                    ["O&E report", "Effective date and exceptions", "Unsearched period or alias"],
                    ["Court distribution docket", "Orders and pending claims", "Duplicate or superseded allocation"],
                ],
            },
            "sop_steps": [
                {"step": 1, "title": "Anchor the fund", "action": "Match ledger to case and parcel.", "detail": "Separate deposited surplus from sale price and verify remaining balance."},
                {"step": 2, "title": "Reconstruct vesting", "action": "Retrieve deed images and historical indexes.", "detail": "Document the jurisdiction-specific entitlement date and intervening transfers."},
                {"step": 3, "title": "Resolve exceptions", "action": "Read every material encumbrance and release.", "detail": "Refresh the search before filing; carry unresolved items into the valuation."},
            ],
        },
        {
            "heading": "2. Reconcile liens before calculating the waterfall",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "For each mortgage or judgment, distinguish the existence of a recorded instrument from the amount currently enforceable against this particular fund. Obtain recorded Releases or Satisfactions of Mortgage and match the original instrument reference, borrower, lender, and parcel. Trace assignments so a release comes from the proper holder or documented successor. A partial release may free one parcel without satisfying the entire obligation; a canceled note may not remove a recorded exception by itself. For an apparent unpaid mortgage followed by a refinance, request the closing settlement statement, payoff demand, disbursement proof, and lender confirmation through authorized channels. That refinance trace can reveal an unrecorded payoff, but it does not authorize simply deleting the lien from the claim schedule.",
                "Resolve an unrecorded payoff through the recording or judicial mechanism available locally, with counsel handling contested entitlement. Request a corrective satisfaction from the successor servicer where supported, retain delivery evidence, and distinguish a pending correction from an accepted release. Then determine whether each claimant has a legally recognized interest in surplus, its priority, and its allowed amount. Recording order alone is insufficient: tax-sale rules, foreclosure seniority, statutory municipal priority, assignments, bankruptcy, and the distribution order can change the result. A senior lien that survives a sale does not necessarily get paid from that sale's surplus. Obtain an amount through the expected disbursement date, explaining interest, fees, credits, and any disputed component rather than copying the face amount from a decades-old mortgage.",
                "Use the following $142,000 example only after establishing that the municipal code lien is entitled to first payment from this fund and the junior HELOC is next. Those are case assumptions, not a nationwide lien hierarchy. The ledger already excludes sale expenses and the foreclosing obligation, so subtracting those again would understate owner proceeds. Deduct the allowed $18,500 municipal claim to leave $123,500; deduct the $25,500 HELOC to leave $98,000. Established equal ownership allocates $49,000 to each of two co-owners. No recovery commission, probate cost, or disputed inter-owner reimbursement is embedded in that split. Keep separate columns for proposed, admitted, and ordered amounts so a contested lien cannot masquerade as a final judicial allocation in either client communications or revenue forecasts.",
            ],
            "table": {
                "caption": "Illustrative ordered waterfall: assumed priorities must be established",
                "headers": ["Entry", "Deduction / allocation", "Fund remaining"],
                "rows": [
                    ["Deposited gross surplus", "$142,000 opening balance", "$142,000"],
                    ["Allowed municipal code lien", "-$18,500", "$123,500"],
                    ["Allowed junior HELOC", "-$25,500", "$98,000"],
                    ["Co-owner A: 50%", "$49,000 allocation", "$49,000"],
                    ["Co-owner B: 50%", "$49,000 allocation", "$0"],
                ],
            },
            "callout": {"kind": "OPERATOR GATE", "title": "A payoff trace is evidence, not a release", "body": "Carry unresolved lien amounts as disputed until the applicable release or distribution procedure resolves them.", "items": ["Match original instrument references.", "Verify the holder's authority.", "Separate proposed allocation from the court's order."]},
        },
        {
            "heading": "3. Restore entity authority without rewriting ownership",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "A commercial parcel formerly vested in an administratively dissolved LLC requires an entity-authority file, not an immediate payout to the person who answers the telephone. Retrieve the Secretary of State formation record, administrative dissolution notice, annual reports, registered-agent history, and available officer or manager filings. Compare the entity's exact legal name and formation jurisdiction to the vesting deed; similarly named entities may have different members and liabilities. Ask for the operating agreement, current management authority, and any winding-up documents needed to establish who can act. Public officer listings are leads, not conclusive proof of membership or distribution rights. The surplus may belong to the entity even when its former manager expects to receive the money personally.",
                "Check the formation state's reinstatement procedure, eligibility period, missing filings, tax clearance requirements, fees, and treatment of acts during dissolution. Some entities may wind up and collect assets without reinstatement; others need restoration or a different judicial route. Do not promise that reinstatement automatically cures every defect or transfers surplus to members. If reinstatement is appropriate, the authorized representative submits the required reports and payments, obtains confirmation, and updates the authority package with a current status record. Preserve the historical dissolution evidence as well as the restoration evidence so the chronology remains intelligible. For an out-of-state LLC, distinguish restoring the domestic entity from renewing foreign qualification in the property state, and determine which matters to the pending claim.",
                "Before incurring reinstatement costs, compare realistic entity proceeds against those costs and competing liabilities. For example, a potential $12,000 entity remainder with $2,400 in reinstatement and record expenses leaves $9,600 before professional fees, creditor claims, and taxes; it is not a $12,000 member distribution. Identify bankruptcy cases, receiverships, dissolution litigation, and secured creditor claims before selecting the payee. Build the final packet with the vesting instrument, surplus proof, restored or winding-up authority, authorized signer identification, and the resolution or agreement required for the claim. Keep entity funds in the appropriate entity or authorized fiduciary channel. A manager's personal bank instructions should never substitute for evidence explaining why that person is legally entitled to receive an entity asset.",
            ],
        },
        {
            "heading": "4. Convert deceased-owner leads into authorized probate packets",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Integrate Track 01 Operator Play probate_docket_inheritance_arbitrage by matching deceased former owners to probate dockets, not by treating an obituary's family list as a payment instruction. Retrieve the death certificate through an authorized route, probate case index, will if filed, appointment orders, letters, inventories, creditor notices, and prior distribution orders. Compare death timing against vesting and the sale because survivorship ownership may bypass the estate while a tenancy-in-common share may not. Confirm whether an appointed representative remains authorized and whether the surplus was previously inventoried or distributed. A closed estate can require reopening or supplemental proceedings. Record each proposed recipient's legal capacity separately from their relationship to the deceased, preserving uncertainty where documentary links are incomplete or contradictory.",
                "Choose the succession procedure under the governing jurisdiction and the character of the asset. California Probate Code section 13100 provides a qualifying personal-property collection procedure after at least 40 days, subject to other statutory conditions and the applicable date-sensitive estate-value limit; verify the current threshold and required affidavit evidence rather than applying it to all real estate. Florida section 735.201 permits summary administration when its conditions are satisfied, including the qualifying estate-value test or death more than two years earlier, with the statutory will restriction also considered. An heirship affidavit can support a family-history proposition without granting universal authority to collect court-held proceeds. Ask the custodian and probate counsel which procedure establishes the actual recipient before purchasing a generic packet marketed across states.",
                "The Unauthorized-Heir-Payout Trap occurs when the researcher finds one plausible relative, obtains a signature, and ignores other successors, estate creditors, or a still-serving representative. Prevent that error with a relationship matrix, documented searches for competing proceedings, and an explanation of each missing link. The Probate-Counsel Escrow Fallback means counsel coordinates the proper probate procedure and, where authorized by the custodian or court, receives funds into the appropriate fiduciary account pending lawful distribution. Escrow alone does not manufacture standing or cure an unauthorized claim. Track the distribution order, required notices, resolved creditor issues, final payee instructions, and receipt confirmation as separate deliverables. The commercial value of the probate play is assembling evidence efficiently, while reserving contested representation and distribution decisions for the authorized legal process.",
            ],
            "table": {
                "caption": "Forensic deceased-owner comparison",
                "headers": ["Issue", "Unauthorized-Heir-Payout Trap", "Probate-Counsel Escrow Fallback"],
                "rows": [
                    ["Recipient", "First located relative signs", "Documented representative or qualifying successor"],
                    ["Procedure", "Heirship affidavit treated as collection power", "Applicable affidavit, summary process, or administration established"],
                    ["Competing interests", "Other heirs and creditors ignored", "Required notices and claims addressed"],
                    ["Custody", "Direct transfer before authority established", "Authorized fiduciary receipt and documented distribution"],
                ],
            },
        },
    ],
    "pull_quote": "Underwrite the right to receive the money, not merely the name beside the parcel.",
    "diagram_id": "diag-05-lien-priority-tree",
    "action_checklist": [
        "Match the deposited balance, case number, and legal description.",
        "Document historical vesting and the controlling entitlement date.",
        "Reconcile O&E exceptions, assignments, releases, and refinance payoff evidence.",
        "Separate assumed lien priority from admitted or ordered distributions.",
        "Establish entity or probate authority before naming the recipient.",
        "Refresh searches and retain the final order and payment receipt.",
    ],
    "statutory_citations": [
        {"title": "California Probate Code section 13100", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=13100.", "relevance": "Conditional collection of qualifying personal property by successors; check associated provisions and current limits."},
        {"title": "Florida Statutes section 735.201", "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0735/Sections/0735.201.html", "relevance": "Eligibility conditions for summary administration, not automatic authority for any identified heir."},
    ],
}

CHAPTER_8 = {
    "id": "Q8",
    "chapter_id": "Q8",
    "chapter_number": 8,
    "question_number": 8,
    "slug": "surplus-investigative-and-skip-tracing-stack",
    "question_prompt": "Q8: Which investigative tools turn county records into verified surplus opportunities?",
    "kicker": "Q8 / THE BIG MONEY PLAYBOOKS",
    "title": "Tools, Public Databases & Skip-Tracing Investigative Stack",
    "subtitle": "County recorder indexes, Regrid/DataTree parcel GIS, PACER bankruptcy checks, and waterfall skip tracing.",
    "layout_template": "resource_directory",
    "reading_time_minutes": 12,
    "executive_summary": "Build the investigative stack around record provenance rather than the number of subscriptions. County indexes establish recorded transactions, assessor rolls identify parcels and mailing addresses, commercial platforms accelerate matching, and court dockets expose authority problems before outreach. A controlled skip-tracing waterfall corroborates identity without treating purchased contact data as proof. The same dated tax-roll pipeline can support a separate property-tax appeal service, provided comparable evidence, assessment dates, and local appeal rules drive the work. This chapter explains which source answers each question and where a convenient lookup becomes a misleading shortcut.",
    "key_metrics": [
        {"label": "Contact corroboration", "value": "2+ independent sources", "context": "Identity and contact confidence", "note": "Two resellers of one feed are not independent."},
        {"label": "Illustrative assessment reduction", "value": "$75,000", "context": "$300,000 assessment less $225,000 supported target", "note": "A worked model, not an expected award."},
        {"label": "Illustrative appeal fee", "value": "$450", "context": "25% of $1,800 realized savings", "note": "Only where the fee arrangement is permitted."},
    ],
    "sections": [
        {
            "heading": "1. Build a parcel-first public-record spine",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Begin with a dated county tax-roll export and a separate surplus ledger, preserving each source's retrieval date, assessment year, field definitions, and update cadence. Normalize assessor parcel numbers without losing leading zeros, suffixes, or the county identifier; an APN is not globally unique. Keep situs address separate from owner mailing address, and preserve original owner text before creating normalized matching fields. Join sale cases to parcels using both identifiers and legal descriptions, flagging splits, combinations, and condominium units for review. A tax-roll owner can lag a recorded transfer, so a successful join is a research lead rather than proof of entitlement. Maintain one internal case identifier linking the raw row, sale record, recorder evidence, and later claimant research.",
                "County Recorder Grantor/Grantee indexes answer who recorded which instrument and when. Search the former owner's exact name, common variants, trust capacities, and entity names in both directions, then obtain the deed, mortgage, assignment, release, or notice image associated with each relevant index entry. Document book and page or instrument number so another researcher can reproduce the finding. The Tax Assessor APN roll contributes land use, assessed values, tax districts, exemptions, building attributes, and mailing data, but those fields do not establish clean title or current contactability. When the recorder and assessor disagree, retain both versions and explain the effective dates. Do not silently overwrite a deed-derived owner with a more recent commercial enrichment result that merely repeats the assessor feed.",
                "Regrid can accelerate parcel geometry, address matching, and geographic review; DataTree can help locate property records, vesting information, and document products where its coverage supports the county. Treat both as discovery and retrieval layers whose specific fields, permissions, and update dates must be checked. A boundary drawn on a map is not a survey, and a cached owner name is not a certified vesting finding. Use a source register to distinguish original county evidence from vendor transformations and manually corrected values. For bulk work, use available official exports, documented APIs, or licensed downloads within their terms, and retain the original record identifier beside the normalized one. This makes a parcel mismatch repairable without rebuilding the entire investigative file from memory.",
            ],
            "table": {
                "caption": "Source directory: assign each tool a bounded job",
                "headers": ["Source", "Primary use", "Required cross-check"],
                "rows": [
                    ["Recorder grantor/grantee index", "Find recorded instruments", "Read complete document images"],
                    ["Assessor APN roll", "Parcel attributes and mailing leads", "Check vintage and deed ownership"],
                    ["Regrid", "Parcel matching and geographic context", "Confirm county identifiers and geometry limits"],
                    ["DataTree", "Property and document discovery", "Verify coverage and original records"],
                    ["PACER", "Bankruptcy proceedings and orders", "Read docket and authority documents"],
                    ["Secretary of State", "Entity status and filed officials", "Verify current authority separately"],
                ],
            },
        },
        {
            "heading": "2. Search bankruptcy and entity authority before outreach",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Run a bankruptcy search before contacting a former owner about an available fund. Use the PACER Case Locator and appropriate bankruptcy court docket, searching name variants and corroborating matches with lawful identifiers such as addresses, filing jurisdiction, or entity details. A common name match is not enough to label someone a debtor. Capture the petition date, chapter, case status, trustee, debtor counsel, and docket entries relevant to the property or proceeds. For an open Chapter 7 case, identify the trustee and examine schedules, exemption claims, sale orders, abandonment notices, and any order addressing surplus. For Chapter 13, identify the trustee and read the plan and confirmation order, because property-of-estate and vesting treatment can depend on the plan, statute, and controlling decisions.",
                "Section 541 of title 11 broadly defines bankruptcy estate property, including many interests held at commencement and certain proceeds, but it does not tell a researcher that every post-sale dollar automatically belongs to the debtor or trustee. Analyze when the ownership interest and surplus right arose, whether exemptions apply, and whether property was properly abandoned or otherwise dealt with by order. A discharge is not proof that an unadministered asset has returned to the debtor; an unscheduled asset can remain estate property after closing. Record uncertainty and direct authority questions to the appropriate representative or counsel before solicitation or an agreement concerning the asset. Separate locating a person from advising them to transfer or collect property that may be controlled by the bankruptcy estate.",
                "For entity-owned parcels, search Secretary of State filings in the formation jurisdiction and any relevant foreign registration jurisdiction. Officer, manager, registered-agent, annual-report, merger, and dissolution records help identify a current point of contact, but a registered agent's service address is not necessarily an operational office or authority to sign a recovery agreement. Cross-check the entity number, exact name, historical names, and filing dates against the deed and bankruptcy results. Where public filings omit members or use outdated officials, request current authority documents rather than guessing. Save a short authority memorandum naming the apparent claimant, evidence supporting that conclusion, unresolved questions, and the next document required. This prevents the skip-tracing team from pursuing a former employee while the actual entity is in receivership or bankruptcy.",
            ],
            "callout": {"kind": "OPERATOR GATE", "title": "Find the authorized recipient before outreach", "body": "A matched phone number does not resolve bankruptcy ownership, entity authority, or probate succession.", "items": ["Corroborate debtor identity.", "Identify open Chapter 7 or 13 representatives.", "Read relevant orders rather than relying on case status alone."]},
        },
        {
            "heading": "3. Operate a corroborated skip-tracing waterfall",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Start the waterfall with low-cost public evidence: deed mailing addresses, assessor correspondence addresses, filed court contacts, entity filings, and public obituary information. An obituary may connect a deceased owner to relatives or reveal a changed surname, but it does not establish heirship or authorize contacting every person listed. Compare address histories by date and distinguish residence, business, mailing service, and care-facility addresses. Use forwarding information only through authorized postal services or lawfully obtained records; a return-mail annotation is a lead, not a license to obtain restricted postal data. Document the source and date of each candidate address, and keep a deceased indicator separate from a confirmed death record. This preserves useful leads without letting an inference overwrite verified identity evidence.",
                "Next use a licensed people-search or skip-tracing product under a documented permissible purpose, then corroborate the result against at least one genuinely independent source. Wireless numbers, landlines, household members, and relatives should each carry a source, observed date, and confidence reason. Two vendors selling the same underlying telephone feed are one evidentiary lineage, not two independent confirmations. A shared surname and nearby address are weak support for a recycled mobile number; a consistent historical address chain plus a separate current public filing is stronger. Rank contacts by recency and agreement, set aside contradictory records, and record wrong-party responses promptly. For relatives, use a limited locating inquiry without disclosing the surplus amount or sensitive financial circumstances, and do not imply that the relative has any claim to the money.",
                "Before outreach, review the intended contact channel against applicable calling, texting, do-not-call, and professional solicitation rules. A vendor's verified label does not supply consent or establish that an automated dialing campaign is permitted. Use a neutral first message identifying the business and inviting the intended recipient to verify the matter through the official custodian. Do not publish sensitive identifiers or attach probate and bankruptcy documents to an unverified contact. Confirm identity through proportionate evidence before discussing the claim in detail, then move documents into a restricted case file. Track returned mail, wrong numbers, refusals, and contact preferences in a suppression record shared across the team. This turns the waterfall into a controlled investigation rather than repeated outreach to every purchased contact associated with a surname.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Collect public leads", "action": "Create dated address and identity candidates.", "detail": "Use county records, entity filings, obituaries, and authorized forwarding evidence."},
                {"step": 2, "title": "Enrich selectively", "action": "Query a licensed source for the documented purpose.", "detail": "Purchase only fields needed for this case and retain source lineage."},
                {"step": 3, "title": "Corroborate independently", "action": "Compare two or more independent sources.", "detail": "Resolve conflicting addresses and recycled phone indications before ranking contacts."},
                {"step": 4, "title": "Contact and correct", "action": "Use an appropriate channel and verify the recipient.", "detail": "Suppress wrong parties and refusals; record evidence without exposing financial details."},
            ],
        },
        {
            "heading": "4. Respect data boundaries and reuse the roll for assessment appeals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The Driver's Privacy Protection Act, 18 U.S.C. section 2721, limits disclosure and use of personal information from motor vehicle records to specified exceptions. Ordinary surplus prospecting is not automatically one of them, and a business identity does not create blanket access. Gramm-Leach-Bliley Act restrictions and its prohibition on obtaining financial customer information through false pretenses likewise do not disappear because a vendor sells a search box. Require the actual source, applicable purpose, and contractual permission for restricted datasets; omit them where the purpose is unsupported. The Computer Fraud and Abuse Act, 18 U.S.C. section 1030, addresses unauthorized computer access and related conduct. Use authorized credentials and permitted interfaces without bypassing access controls. Public availability, contractual permission, and statutory permitted use are distinct questions that deserve separate records.",
                "Reuse the same versioned county tax-roll pipeline for Track 01 Operator Play property_tax_assessment_appeal_contingency, Automated Commercial/Residential Property-Tax Appeal Arbitrage. This is an adjacent service for authorized owners, not a reason to represent former owners after they have lost the property. Screen assessed values against independently supported market values or uniformity measures allowed locally, using the correct valuation date and assessment ratio. Segment residential properties by neighborhood, size, age, condition, and sale validity; segment commercial properties by use, occupancy, income evidence, and capitalization assumptions where relevant. Automation can rank anomalies and assemble comparable candidates, but someone must inspect comparability, exemptions, equalization factors, and filing deadlines. Maintain separate engagements and permissions for appeals and surplus recovery even when both originate from one parcel record.",
                "The Valuation-Rejection Trap is filing an appeal supported by attractive but irrelevant sales, such as renovated houses outside the assessment neighborhood or commercial transfers with unusual financing. The Comparable-Equity Ratio Fallback is a documented uniformity argument only where that appeal basis is recognized: use similar properties, explain exclusions, calculate consistent assessment-to-market ratios, and reconcile material differences. Suppose the subject's supported market value is $1,000,000, its assessment is $300,000, and a valid comparable analysis supports a 22.5% assessment ratio. The modeled target is $225,000, a $75,000 reduction. At an effective 2.4% tax rate on the assessment reduction, annual savings would be $1,800; a permitted 25% realized-savings fee would be $450. Check caps, exemptions, tax-rate mechanics, and actual bills before invoicing, and revalidate annually rather than assuming an automatic recurring award.",
            ],
            "table": {
                "caption": "Forensic appeal comparison: evidence determines the available argument",
                "headers": ["Issue", "Valuation-Rejection Trap", "Comparable-Equity Ratio Fallback"],
                "rows": [
                    ["Comparable set", "Cherry-picked cheap or dissimilar sales", "Matched cohort with documented exclusions"],
                    ["Measurement date", "Current listing prices replace statutory valuation", "Evidence aligned to the assessment date"],
                    ["Theory", "Low price asserted without a recognized appeal basis", "Uniformity analysis where locally available"],
                    ["Calculation", "Assessment reduction mistaken for tax savings", "$75,000 x 2.4% = $1,800 modeled savings"],
                    ["Fee", "Invoice projected multi-year benefits immediately", "Apply permitted terms to verified realized savings"],
                ],
            },
        },
    ],
    "pull_quote": "Buy speed from tools; take proof from records.",
    "diagram_id": "diag-01-end-to-end-workflow",
    "action_checklist": [
        "Preserve raw county exports and normalize APNs without losing identifiers.",
        "Verify vendor findings against recorder images and dated assessor records.",
        "Check bankruptcy identity, trustees, plans, and relevant orders before outreach.",
        "Confirm entity representatives through current authority evidence.",
        "Corroborate contacts across independent source lineages and suppress wrong parties.",
        "Document permissible use and avoid restricted data without a supported purpose.",
        "Separate assessment appeal engagements and invoice only under verified fee terms.",
    ],
    "statutory_citations": [
        {"title": "18 U.S.C. section 2721", "url": "https://www.law.cornell.edu/uscode/text/18/2721", "relevance": "Restrictions and enumerated permitted uses for motor vehicle record personal information."},
        {"title": "11 U.S.C. section 541", "url": "https://www.law.cornell.edu/uscode/text/11/541", "relevance": "Defines bankruptcy estate property relevant to surplus entitlement and proceeds."},
        {"title": "11 U.S.C. section 554", "url": "https://www.law.cornell.edu/uscode/text/11/554", "relevance": "Abandonment rules and treatment of property not administered or abandoned."},
        {"title": "15 U.S.C. section 6802", "url": "https://www.law.cornell.edu/uscode/text/15/6802", "relevance": "Financial institution disclosure restrictions and exceptions for nonpublic personal information."},
        {"title": "15 U.S.C. section 6821", "url": "https://www.law.cornell.edu/uscode/text/15/6821", "relevance": "Prohibits obtaining financial institution customer information through false pretenses."},
        {"title": "18 U.S.C. section 1030", "url": "https://www.law.cornell.edu/uscode/text/18/1030", "relevance": "Computer access offenses relevant to unauthorized database access and access-control circumvention."},
    ],
}

CHAPTERS_7_TO_8 = [CHAPTER_7, CHAPTER_8]

