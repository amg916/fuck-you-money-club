"""Volume 001 opening chapters: legal lanes, evidence, payers, and capital."""

_Q1 = {
    "id": "Q1",
    "chapter_id": "Q1",
    "chapter_number": 1,
    "question_number": 1,
    "slug": "what-is-heir-hunting",
    "question_prompt": "Q1: What Exactly Is Heir Hunting?",
    "kicker": "Q1 / THE BIG MONEY PLAYBOOKS",
    "title": "What Exactly Is Heir Hunting?",
    "subtitle": "Three adjacent businesses with different claimants, rules and evidence.",
    "layout_template": "opportunity_overview",
    "reading_time_minutes": 12,
    "executive_summary": "Heir hunting is evidence work that connects a legally entitled person to an asset or estate, not a universal license to collect abandoned money. Three adjacent lanes share public records but differ in authority: intestate probate research, state custodial unclaimed property, and foreclosure or tax-sale surplus recovery. Choose the lane before calculating a fee or contacting a claimant. This chapter turns public records into a documented research queue, distinguishes kinship from entitlement, and replaces brittle portal scraping with permissioned data access, source provenance, and measurable case qualification.",
    "key_metrics": [
        {"label": "Legal lanes", "value": "3", "context": "Classify before contracting", "note": "Probate, custodial property, and surplus are distinct."},
        {"label": "Qualified yield", "value": "8 / 200 = 4%", "context": "Illustrative weekly intake", "note": "A research funnel, not an expected recovery rate."},
    ],
    "sections": [
        {
            "heading": "Separate the three businesses before accepting a file",
            "epistemic_status": "statutory_fact",
            "paragraphs": [
                "Intestate probate heir research asks which people inherit property that passes without an effective testamentary disposition. California Probate Code section 6402 supplies an order of succession for the part of an intestate estate not passing to a surviving spouse under section 6401, or the entire intestate estate when there is no surviving spouse. Start with the death certificate, probate petition, docket, and any will or trust references; a surname match does not establish intestacy. A personal representative may commission genealogy, but the probate court resolves disputed rights and supervises distribution through applicable proceedings. Your deliverable is a sourced family reconstruction and evidentiary packet, not a private declaration that someone owns a percentage of the decedent's assets.",
                "State custodial unclaimed property concerns a holder's transfer of dormant property to a state administrator for the owner's benefit. The claimant may be a living individual, corporation, estate, or successor, so this lane often needs identity and authority documents rather than an extended family tree. California's State Controller administers the state claim process; it does not become the probate court merely because an account owner died. Locate the property identifier, reported owner, former address, reporting holder, and available property description. Then establish the claimant's right to that particular item. An heir who proves kinship may still need estate authority or another permitted succession procedure before the Controller can release funds to the appropriate recipient.",
                "Foreclosure and tax-sale surplus recovery concerns proceeds left after legally prioritized payments, not a dormant bank account waiting in a state database. California Civil Code section 2924k orders distribution of trustee-sale proceeds, including sale expenses, secured obligations, junior interests, and the remaining balance to the trustor or successor as specified. Tax-sale excess proceeds follow a different statutory process; do not transplant the trustee-sale sequence into a tax file. Identify whether the custodian is a trustee, court, county tax collector, or clerk acting in a particular role. Obtain the sale record, proceeds accounting, lien history, and governing claim instructions. The former owner is a lead, not proof that no competing interest has priority.",
            ],
            "table": {
                "caption": "Same research skills, different legal destinations",
                "headers": ["Lane", "Decision-maker or administrator", "Core evidence", "Critical distinction"],
                "rows": [
                    ["Intestate probate", "Probate court; personal representative", "Vital records, family tree, docket", "Kinship plus applicable succession law"],
                    ["Custodial property", "State Controller or equivalent", "Property ID, owner identity, authority", "Claim to a specific reported asset"],
                    ["Sale surplus", "Trustee, county official, or court", "Sale accounting, title and liens", "Priority and timely claim procedure"],
                ],
            },
        },
        {
            "heading": "Contracts follow authority, not the investigator's label",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "A fee agreement must identify the actual service, authorized client, payment source, and event that earns compensation. An individual heir can engage research concerning their own interest without thereby authorizing expenses against an entire estate. A personal representative's engagement raises a separate question: whether that representative can retain the service on the proposed terms and whether payment requires court review. A state claim assistance contract faces its own timing, disclosure, and compensation rules. Calling all three services heir hunting does not harmonize those rules. Misclassification can produce an unenforceable agreement, an invalid assignment, or a demand against someone who never owed the fee. Classify the asset and authority before choosing contractual language or projecting collections.",
                "Use a lane memorandum as the first work product. Record the asset identifier, decedent or reported owner, current custodian, jurisdiction, procedural posture, prospective claimant, and evidence of signing authority. Keep entitlement and contactability in separate fields: a located relative may have no inheritable share, while a well-supported heir may remain difficult to reach. For a probate matter, distinguish letters appointing the representative from a petition merely requesting appointment. For a corporate property claim, distinguish an officer's current position from authority to act for a dissolved predecessor. For surplus, distinguish the auction price from the custodian's confirmed balance. Each distinction prevents a plausible public record from silently becoming an unsupported contractual assumption.",
                "Consider an illustrative file showing a deceased homeowner, a completed trustee sale, and a state listing for an old utility refund. There are at least two assets, potentially two procedures, and possibly an estate proceeding needed to establish who may act. The same death certificate can support both files, but neither an engagement nor an award automatically transfers between them. Build separate asset records linked to one research subject, assign separate deadlines, and document which custodian receives each packet. If the surplus was already distributed, close that opportunity rather than attaching its stale amount to the utility claim. This asset-level discipline makes case economics intelligible and prevents double-counting recoveries in the sales pipeline.",
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Name the asset, claimant, and authority",
                "body": "Do not quote a recovery percentage from a name match alone.",
                "items": ["Confirm the legal lane and jurisdiction.", "Identify the custodian and current balance evidence.", "Document who can engage the firm and who can receive payment."],
            },
        },
        {
            "heading": "Track 01: Public-Record & API Intelligence",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The public_record_api_intelligence play converts permitted public data into a prioritized evidence queue. Inputs include probate docket indexes, appointment entries, recorder instruments, published surplus lists, state property listings, and official business registry records. Supplement with authorized vital records and source-specific exports where access permits; public visibility does not mean unrestricted bulk access or access to sealed attachments. Preserve the source URL, retrieval date, query parameters, record identifier, and a copy or permitted reference to the underlying document. A docket index describes events but may omit the operative order. Treat index-only findings as leads until the document supports them, and separate verified fields from inferred relationships in the case database.",
                "The four-step workflow is acquire, normalize, corroborate, and route. Acquire from documented APIs, downloads, or records requests at the source's allowed pace. Normalize dates, entity suffixes, addresses, and instrument numbers without deleting raw values. Corroborate each promising match against an independent identifier and the document establishing the asset or authority. Route the result to the correct legal lane with an assigned researcher, next evidence request, and explicit rejection reason when unsuitable. A shared surname and city are weak signals; a matching predecessor corporation number and historical address are stronger, but still require successor evidence. Maintain one canonical asset key so repeated downloads do not inflate the inventory or trigger duplicate claimant outreach.",
                "Measure the queue rather than boasting about scraped rows. Record source coverage against the stated jurisdiction list, document retrieval success, duplicate rate, verified claimant yield, median record age, and labor minutes per qualified file. In an illustrative batch of 200 leads, 40 duplicates and 80 obsolete records leave 80 for review; eight supported cases represent a four percent yield on gross intake, not ten percent on all available opportunities. If acquisition and review cost $640, qualified acquisition cost is $80 before deeper genealogy, outreach, and claim preparation. Track those later costs separately. A rising yield can conceal shrinking source coverage, so report both denominators alongside the case count and avoid treating incomplete downloads as empty jurisdictions.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Acquire", "action": "Use permitted feeds or records requests.", "detail": "Save source identifiers, retrieval dates, and access conditions."},
                {"step": 2, "title": "Normalize", "action": "Create stable asset and subject keys.", "detail": "Retain raw names and dates beside standardized values."},
                {"step": 3, "title": "Corroborate", "action": "Inspect underlying records and independent identifiers.", "detail": "Keep inferred kinship separate from demonstrated entitlement."},
                {"step": 4, "title": "Route", "action": "Assign a lane, owner, and next evidence task.", "detail": "Reject stale, duplicated, or unsupported opportunities explicitly."},
            ],
        },
        {
            "heading": "Replace portal fragility with a durable evidence queue",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The naive portal-scraping trap begins when an operator equates faster requests with better inventory. HTTP 429 responses and CAPTCHA blocks indicate that the acquisition method has reached an access boundary; retries without a budget can turn one missed update into an entire night's corrupted intake. Do not route around controls with identity rotation or CAPTCHA defeat. Honor documented retry instructions, stop automated access when required, and preserve the last successful snapshot as historical data. Mark freshness explicitly rather than presenting cached records as current balances. Distinguish a transport failure from a genuine zero-result response, and retain response metadata sufficient to explain why a jurisdiction's apparent opportunity count suddenly fell.",
                "The durable fallback is a records-request and cached-queue operating model. Ask the custodian whether a bulk extract, scheduled export, or documented API is available, describing the record fields and date range needed. Use the applicable state public-records process for state or county records; federal FOIA does not govern a county probate office merely because the request concerns public information. Calendar acknowledgment and production milestones under the applicable rules, log fees, and ingest deliveries through the same deduplication path as online records. While waiting, researchers work already acquired cases in priority order, with a fresh custodian check before reliance. Pending requests remain pending inventory, never invented new assets or assumed recoveries.",
                "Close each research cycle with an evidence audit of a small, defined sample. Select both accepted and rejected records, reproduce the match from stored identifiers, and inspect whether the underlying document supports the chosen lane. Count erroneous merges, stale balances, and missing appointment documents separately because each calls for a different repair. An erroneous merge needs entity resolution changes; stale balances need refresh scheduling; missing authority needs a new documentary task. Compare the cost of an official extract with researcher hours lost to unreliable acquisition. The winning operation is not the one collecting the most names. It is the one producing defensible, correctly routed files without letting access failures or speculative family links masquerade as money.",
            ],
            "table": {
                "caption": "Forensic acquisition failures and durable alternatives",
                "headers": ["Naive Portal-Scraping Trap", "Detection Metric", "Durable FOIA/Cached Queue Operator Fallback"],
                "rows": [
                    ["HTTP 429/CAPTCHA blocks", "429 share; blocked sessions; last successful fetch", "Respect access limits; request authorized export; work dated cache"],
                    ["Zero results treated as zero assets", "Response validity; expected pagination; source coverage", "Record failed acquisition separately; reconcile official delivery"],
                    ["Names merged without asset keys", "Duplicate rate; sampled false merges", "Retain raw fields and stable IDs; manually resolve ambiguity"],
                    ["Old balances sold as current", "Record age; custodian-confirmed balance rate", "Refresh before reliance; flag historical snapshots"],
                ],
            },
        },
    ],
    "pull_quote": "A name is a lead. An asset, an entitlement chain, and an authorized payer make a case.",
    "diagram_id": "diag-01-end-to-end-workflow",
    "action_checklist": [
        "Classify each asset as probate, custodial property, or sale surplus.",
        "Record the decision-maker, custodian, claimant, and signing authority.",
        "Retrieve the operative document behind each promising index entry.",
        "Run acquire, normalize, corroborate, and route with stable asset keys.",
        "Measure qualified yield and cost using explicit denominators.",
        "Replace blocked acquisition with permitted exports and dated queues.",
    ],
    "statutory_citations": [
        {"title": "California Probate Code section 6402", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6402.&lawCode=PROB", "relevance": "Intestate succession for the share not passing to a surviving spouse under section 6401."},
        {"title": "California Civil Code section 2924k", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2924k.&lawCode=CIV", "relevance": "Priority of distribution of trustee-sale proceeds; not the tax-sale excess proceeds procedure."},
        {"title": "California Revenue and Taxation Code section 4675", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=4675.&lawCode=RTC", "relevance": "Separate claim framework for tax-sale excess proceeds."},
    ],
}

_Q2 = {
    "id": "Q2",
    "chapter_id": "Q2",
    "chapter_number": 2,
    "question_number": 2,
    "slug": "who-pays-and-where-capital-sits",
    "question_prompt": "Q2: Who Pays, Why They Pay & Where Estate Capital Sits",
    "kicker": "Q2 / THE BIG MONEY PLAYBOOKS",
    "title": "Who Pays, Why They Pay & Where Estate Capital Sits",
    "subtitle": "Find the payer, the asset holder and the authority to act before discussing price.",
    "layout_template": "executive_summary",
    "reading_time_minutes": 12,
    "executive_summary": "An attractive balance is not revenue until an entitled claimant can obtain it and an authorized client owes the agreed fee. Separate individual heir engagements, estate genealogy retainers, and state property assistance contracts. Then distinguish gross inventory from distributable residue, and a public listing from an approved claim. Corporate warrant research can produce substantial files, but officer matches, statutory timing, and successor authority determine whether those files are usable. Build economics from verified recovery and collectible compensation, while showing claimants the official route for filing directly without a paid intermediary.",
    "key_metrics": [
        {"label": "Corporate warrant screen", "value": ">$25,000", "context": "Research prioritization only", "note": "Not a statutory eligibility threshold or promised balance."},
        {"label": "Illustrative residue", "value": "$350,000", "context": "$600,000 gross less $250,000 deductions", "note": "Actual distributions require verified liabilities and authority."},
        {"label": "California locator ceiling", "value": "10%", "context": "CCP section 1582 covered agreements", "note": "Timing, written agreement, and disclosure requirements also apply."},
    ],
    "sections": [
        {
            "heading": "Separate the client, the asset holder, and the person writing the check",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "An individual heir may hire a researcher under a permitted contingency agreement or assignment concerning that heir's interest. The heir is the client; the estate is not automatically the client, and another heir owes nothing merely because the research benefited the family. Define whether compensation attaches to funds actually received, a permitted assigned interest, or another specified event, and verify that the proposed arrangement is valid in the relevant jurisdiction. An assignment can change rights and collection mechanics, so it is not simply an invoice with a different heading. Identify the signer's capacity and avoid presenting a projected inheritance as cash already available to satisfy a fee. A signed agreement without a collectible recovery remains a contingent business asset.",
                "An estate administrator or other personal representative may instead retain genealogy services to identify beneficiaries or resolve missing branches. Here the engagement concerns work for the estate, usually defined by a research scope, rate or fixed budget, and deliverable. Obtain evidence of appointment and confirm the representative's powers, any restrictions, and the applicable process for payment or court review. A petitioner's promise before appointment is different from an authorized representative's engagement. Separate professional research charges from reimbursable document purchases and identify who approves expanded scope. A well-documented report may be payable under the engagement even if it excludes a suspected heir; the service is evidentiary work, not necessarily a successful percentage recovery for one individual.",
                "For state custodial property, the Controller holds the asset and adjudicates the claim through its procedures, but that does not make the Controller the investigator's customer. The claimant generally establishes identity and entitlement, receives the approved disbursement through the authorized process, and owes any valid assistance fee under the separate agreement. Do not assume the agency will split a payment or honor an assignment without confirming its rules. Give the claimant the official California State Controller unclaimed property search and claim route at claimit.ca.gov, explain that they can file directly without paying a locator, and describe the actual work your fee buys. Keep disclosure distinct from sales pressure: convenience, document assembly, and difficult succession evidence are services, not exclusive access to government money.",
            ],
            "table": {
                "caption": "Authority and payment map",
                "headers": ["Engagement", "Who authorizes", "Where capital sits", "Payment basis"],
                "rows": [
                    ["Individual heir contingency or assignment", "Entitled individual acting with capacity", "Estate or relevant custodian", "Valid agreement tied to the individual's defined interest"],
                    ["Estate genealogy retainer", "Duly authorized personal representative", "Estate accounts and assets", "Authorized research charges; review where required"],
                    ["State property assistance", "Owner or documented authorized successor", "State Controller", "Valid locator agreement; agency payment rules remain separate"],
                ],
            },
        },
        {
            "heading": "Gross inventory is not distributable residue",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "California Probate Code section 8800 generally requires the personal representative to file an inventory and appraisal within four months after letters are first issued, subject to the court's permitted extension. The inventory is a structured account of estate property and value, not an assurance that heirs receive the headline total. Review the filed Inventory and Appraisal, attachments, supplemental inventories, creditor filings, secured loan statements, tax obligations, and available accountings. Check valuation dates and whether a listed interest is fractional, encumbered, or difficult to sell. A residence valued at $500,000 with a $300,000 mortgage is not $500,000 of heir spending power. Equally, assets passing outside probate should not be added to the probate fee base just because they belonged to the same decedent.",
                "Use an explicit illustrative waterfall: $600,000 of gross probate assets, less $120,000 of secured debt, $40,000 of administration and funeral costs, $60,000 of taxes and other allowed creditor obligations, and a $30,000 reserve leaves $350,000 provisionally available for distribution. These buckets must be mutually exclusive; do not deduct a mortgage twice if a sale schedule already reports net proceeds. The reserve is a planning holdback, not necessarily a final expense. Reconcile each amount to a dated document and label estimates, disputed claims, and settled balances separately. If two heirs share that provisional residue equally, each modeled interest is $175,000, not $300,000. A later tax adjustment or contested claim changes both the residue and the fee opportunity.",
                "A purely illustrative ten percent fee on one heir's $175,000 actual receipt would be $17,500, assuming that arrangement is valid and the contract uses that base. This example does not import the California state-property locator ceiling into probate engagements or establish a permitted probate rate. If the firm spends $4,000 on research and records, its contribution before overhead is $13,500 only after collection; unrecovered files and financing costs still affect portfolio profit. Track expected receipt date separately from amount, because a $17,500 fee collected eighteen months later cannot fund today's payroll. Rebuild the waterfall when property is sold, claims are resolved, or the representative proposes distribution, and do not treat an unsigned draft accounting as a final award.",
            ],
            "table": {
                "caption": "Illustrative estate waterfall, not an appraisal or award",
                "headers": ["Component", "Amount", "Evidence to reconcile"],
                "rows": [
                    ["Gross probate assets", "$600,000", "Inventory, appraisal, and subsequent changes"],
                    ["Secured debt", "($120,000)", "Payoff statements; no duplicate netting"],
                    ["Administration and funeral", "($40,000)", "Invoices and applicable authorization"],
                    ["Taxes and other creditor obligations", "($60,000)", "Returns, allowed claims, settlements"],
                    ["Planning reserve", "($30,000)", "Identified unresolved exposure"],
                    ["Provisional distributable residue", "$350,000", "Updated accounting and distribution process"],
                ],
            },
        },
        {
            "heading": "Track 01: State Treasury Escheatment & Unclaimed Corporate Warrant Recovery",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The unclaimed_property_escheatment_arbitrage play targets overlooked corporate property, including uncashed warrants above $25,000 as an internal prioritization screen. In this context a warrant is a government payment instrument, not an equity purchase right or an arrest record. First determine whether the unpaid item remains with the issuing agency, has expired under the issuer's rules, or has actually been remitted into a state custodial property program. Those states lead to different reissue or claim procedures. A stale warrant list is not automatically the Controller's payable inventory. Record issuer, warrant number, payee, issue date, available amount, and current custodian. Where the public record does not reveal the amount, retain it as unknown rather than fabricating a threshold-qualified lead.",
                "Cross-match the payee against Secretary of State records using entity number, jurisdiction, former names, historical addresses, merger records, and filed officer information. A current officer match creates a route for verifying authority; it does not prove personal ownership of corporate funds or authorize payment to that officer. Search beyond active corporations when the payee is dissolved, suspended, merged, or acquired, but document the chain from original payee to current claimant. Request the documents the relevant custodian requires, which may include officer authority, merger evidence, corporate identification, and proof connecting the entity to the reported address. A similarly named active company is not a substitute for a dissolved predecessor unless the succession documents actually connect them.",
                "Build the commercial case only after checking timing and collectibility. For California property covered by CCP section 1582, agreements entered during the interval from the statutory holder report through twelve months after delivery to the Controller are invalid under that section. Outside the prohibited interval, covered agreements still face the ten percent compensation limit and written, signed disclosure requirements. Do not substitute the warrant issue date, database publication date, or first outreach date for the required statutory events. Obtain support for report and delivery dates; hold the contract task when those dates are unknown. Distinguish this agreement restriction from the underlying owner's ability to file a claim, and check other jurisdictions independently rather than exporting California's interval nationwide.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Locate the instrument", "action": "Capture warrant and custodian identifiers.", "detail": "Distinguish issuer-held stale payments from property delivered to the state."},
                {"step": 2, "title": "Resolve the entity", "action": "Cross-match SOS officers, entity numbers, and historical names.", "detail": "Require successor evidence for mergers or dissolved payees."},
                {"step": 3, "title": "Check timing and terms", "action": "Document statutory event dates and applicable fee rules.", "detail": "Separate owner claim eligibility from locator agreement eligibility."},
                {"step": 4, "title": "Assemble and reconcile", "action": "Submit through the authorized claimant and track actual payment.", "detail": "Reconcile approved amount, claimant receipt, and separately collectible fee."},
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Officer identity is not ownership",
                "body": "Corporate money belongs to the entitled entity or documented successor, not the person whose name appears in an officer search.",
                "items": ["Confirm the exact payee and entity number.", "Establish signing authority and succession documents.", "Verify agreement timing and disclose the official direct claim route."],
            },
        },
        {
            "heading": "Turn a promising balance into a collectible, documented fee",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The naive trap is to treat every large balance as a ready-made ten percent invoice. A $40,000 corporate listing might produce at most $4,000 under an applicable ten percent ceiling, but that arithmetic says nothing about whether the agreement is timely, the entity is entitled, or the Controller approves the full amount. If records and research cost $1,200 and later servicing costs $600, modeled contribution is $2,200 before overhead only on a full, paid recovery. At a fifty percent collection probability across comparable files, expected gross fees are $2,000; subtract the full $1,800 if those costs are incurred on every file, leaving just $200. Label that probability as an assumption unless your own completed cohort supports it.",
                "Use a case ledger that keeps listed amount, verified custodian balance, claimed amount, approved amount, claimant receipt, and firm fee collection as separate fields. Attach the source and date for each transition. A status marked submitted does not justify recognizing an approved balance, and a Controller payment confirmation does not prove that your invoice has been paid. Record why cases fail: wrong entity, missing successor documents, prohibited agreement timing, duplicate recovery, or insufficient remaining balance. Those categories improve screening more than an undifferentiated lost-case count. Measure cycle time from qualified engagement to receipt and track pending cases by age, so a growing queue of unresolved claims is not mistaken for an expanding cash-generating book.",
                "Finish each offer with a concrete scope and the official alternative. Explain which records you obtain, which identity documents the claimant supplies, what triggers compensation, and how unrecovered expenses are handled under the valid agreement. For California covered locator agreements, capture the required written disclosures, including the nature and value of the property and the name and address of the person or entity possessing it, alongside the claimant's signature. Check the current statutory text and custodian instructions before using a template. Never imply a public balance is secret or that an heir or company must hire your firm to approach the agency. The durable service sells documented execution on a difficult file, not ownership of the claimant's access to their own money.",
            ],
            "table": {
                "caption": "Forensic corporate recovery: naive trap versus durable fallback",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Officer match treated as entitlement", "Files missing entity number or authority proof", "Verify original payee, signer authority, and successor chain"],
                    ["Every stale warrant treated as state cash", "Custodian confirmations versus raw listings", "Route to issuer reissue or state claim procedure as appropriate"],
                    ["Immediate contract despite unknown timing", "Files lacking report and delivery dates", "Document statutory dates; defer prohibited agreements"],
                    ["Listed amount booked as revenue", "Receipt-to-listing ratio; unpaid invoice aging", "Separate balance, award, claimant receipt, and collected fee"],
                ],
            },
        },
    ],
    "pull_quote": "Find the authorized payer before pricing the work, and find the residue before pricing the inheritance.",
    "diagram_id": "diag-04-jurisdiction-fee-caps",
    "action_checklist": [
        "Identify the client, custodian, authorized signer, and payment mechanism separately.",
        "Reconcile gross inventory to provisional residue without double-counting deductions.",
        "Show the claimant the official direct claim route and explain the service offered.",
        "Screen corporate warrants above $25,000 without inventing undisclosed balances.",
        "Cross-match SOS records and document corporate succession and signing authority.",
        "Verify statutory report and delivery dates before entering a locator agreement.",
        "Track claimant receipt separately from the firm's collected fee.",
    ],
    "statutory_citations": [
        {"title": "California Code of Civil Procedure section 1582", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1582.&lawCode=CCP", "relevance": "Covered property-locator agreement timing, compensation ceiling, and written disclosure requirements."},
        {"title": "California Probate Code section 8800", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=8800.&lawCode=PROB", "relevance": "Personal representative's inventory and appraisal filing obligation and general four-month timetable."},
    ],
}

CHAPTERS_1_TO_2 = [_Q1, _Q2]

