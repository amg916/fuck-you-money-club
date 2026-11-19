"""Volume 002 operating chapters and independently built field workbook."""

Q11 = {
    "id": "Q11",
    "chapter_id": "Q11",
    "chapter_number": 11,
    "question_number": 11,
    "slug": "scaling-a-surplus-recovery-firm",
    "question_prompt": "Q11: How do you scale a small surplus recovery firm?",
    "kicker": "Q11 / THE BIG MONEY PLAYBOOKS",
    "title": "Small-Team Scaling: Running a High-Margin 2-to-4 Person Recovery Firm",
    "subtitle": "Separating county list ingestion, title underwriting, claimant outreach, and outside motion counsel.",
    "layout_template": "action_checklist",
    "reading_time_minutes": 12,
    "executive_summary": "Scale surplus recovery by separating evidence collection, underwriting, claimant communication, and filing responsibility before adding counties. The Base model uses two full-time operators and two part-time contractors, with outside attorneys engaged per file rather than counted as permanent seats. Revenue follows collected fees, not listed balances or signed agreements. Weekly aging reconciliation exposes stalled disbursements; script audits protect communication accuracy; encrypted, restricted records reduce claimant-data exposure. Expand to three full-time operators and three contractors only when measured capacity, contribution margins, and a funded collection runway support the additional desk.",
    "key_metrics": [
        {"label": "Base", "value": "$425,000 gross fees", "context": "2 FT + 2 C", "note": "35% modeled margin; $148,750 owner net."},
        {"label": "Multi-State", "value": "$750,000 gross fees", "context": "3 FT + 3 C", "note": "45% modeled margin; $337,500 owner net."},
        {"label": "Score", "value": "86/100", "context": "22/22/18/12/12", "note": "+/-3 points; High confidence editorial rating."},
    ],
    "sections": [
        {
            "heading": "Four seats, explicit handoffs, and outside legal capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "The four-person Base firm consists of a Principal/Underwriting Lead, a Full-Time Outreach & Claimant Specialist, a Part-Time County List & Title Abstractor, and a Part-Time Notary/Packet Coordinator. The first two positions are full-time; the latter two are modeled contractor seats, subject to actual worker classification. A network of per-file state surplus attorneys supplies outside motion counsel and is an expense, not a hidden fifth permanent employee. The principal decides whether the evidence supports spending more on a claim. The abstractor assembles records without deciding disputed legal priority. The specialist handles claimant communication, while the coordinator checks packet completeness and arranges execution. Nobody promises a payout merely because a county list contains a name.",
                "Each file moves through named handoffs with an accountable sender and receiver. Ingestion delivers the official list date, county account identifier, sale type, stated balance, and source document. Abstracting delivers recorded vesting instruments, grantor and grantee searches, an ownership and encumbrance report, and a chronology of potentially surviving interests. Underwriting returns a written claimant hypothesis, estimated net distributable amount, unresolved priority questions, and a spending ceiling. Outreach receives only the contact data and approved factual explanation needed for that assignment. Packet coordination receives counsel's current document checklist. Counsel receives the evidence bundle and unresolved questions rather than an unsupported instruction to file immediately. A rejected handoff records the missing instrument and next responsible person.",
                "Do not assume that calling the abstractor or coordinator a contractor settles employment status. Section 203 of Title 29 defines employee, employer, and employ broadly for federal wage-and-hour purposes; classification depends on the applicable legal framework and actual relationship, not a budget label. Review control, independence, scheduling, tools, and economic circumstances with appropriate advisers, including separate state requirements. Budget payroll treatment if the facts require it. A coordinator who is also a notary must follow the commissioning state's rules, avoid prohibited conflicts, and keep notarization distinct from explaining legal rights. Outside attorneys determine representation, filings, and legal strategy under their engagement terms. These boundaries preserve a lean operating model without substituting inexpensive administrative labor for licensed judgment.",
            ],
            "table": {
                "caption": "Base responsibility map",
                "headers": ["Seat", "Allocation", "Deliverable"],
                "rows": [
                    ["Principal/Underwriting Lead", "1 FT", "Evidence decision and spending ceiling"],
                    ["Outreach & Claimant Specialist", "1 FT", "Verified contact and accurate explanation"],
                    ["County List & Title Abstractor", "1 C, part-time", "Indexed vesting and lien record bundle"],
                    ["Notary/Packet Coordinator", "1 C, part-time", "Execution and packet completeness"],
                    ["State surplus attorney network", "Per-file external expense", "Legal priority analysis and filing"],
                ],
            },
        },
        {
            "heading": "Capacity economics before a six-person multi-state desk",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "The Base illustration collects $425,000 in annual gross fees and retains $148,750 at a 35 percent owner-net margin, leaving $276,250 for modeled operating costs. Gross fees are the firm's earned collections, not the claimant's surplus balance and not the face value of signed contracts. Specify whether principal compensation is included in costs before comparing actual results with this illustration; owner distributions cannot also appear as an additional operating expense. Record payroll, contractor invoices, counsel charges borne by the firm, title reports, tracing, software, insurance, and unrecovered acquisition spending consistently. An apparently excellent month can simply reflect old files paying together. Track originating cohorts beside cash receipts so that a collection spike does not masquerade as durable production.",
                "The Multi-State illustration grows to three full-time staff and three contractor seats, collecting $750,000 in gross fees with $337,500 owner net at a 45 percent margin. Its cost ceiling is therefore $412,500 annually. Add a Full-Time Operations & Reconciliation Lead to the principal and outreach specialist, and add a second Part-Time County List & Title Abstractor to the existing abstractor and packet coordinator. The new operations lead owns queue control, aging, and quality sampling; the principal retains exception underwriting. Counsel remains an external per-file network with state-specific competence. The margin improvement is an assumption to test through throughput and purchased-service costs, not an automatic reward for entering another jurisdiction or hiring another operator.",
                "Translate the revenue goal into observable capacity before increasing commitments. At an illustrative $8,500 average collected fee, the Base goal requires fifty paid files annually; at $10,000 per collected fee, the Multi-State goal requires seventy-five. Neither average is a proposed fee rate: lawful contract terms and actual claimant recoveries determine earned fees. If only half of counsel-ready files ultimately collect within the planning year, seventy-five collections require roughly one hundred fifty counsel-ready files, with opening backlog and timing modeled separately. Measure abstracting hours, outreach attempts, execution failures, and counsel turnaround on the current cohort. Purchase additional capacity at the measured bottleneck, not at the loudest complaint. Maintain a six-month operating reserve separately from expected but unpaid fees.",
            ],
            "table": {
                "caption": "Illustrative annual operating envelope",
                "headers": ["Model", "Staff", "Gross fees", "Costs", "Owner net"],
                "rows": [
                    ["Conservative", "2 FT + 2 C", "$100,000", "$75,000", "$25,000 / 25%"],
                    ["Base", "2 FT + 2 C", "$425,000", "$276,250", "$148,750 / 35%"],
                    ["Multi-State", "3 FT + 3 C", "$750,000", "$412,500", "$337,500 / 45%"],
                ],
            },
        },
        {
            "heading": "Weekly reconciliation turns aging claims into assigned work",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Every Monday, reconcile the claim register against the clerk's docket, counsel's filing receipts, county disbursement communications, and the firm's bank receipts. Use calendar days since the clerk accepted a complete claim as the primary aging clock, while preserving sale date, contract date, statutory deadline, and last activity separately. Label buckets 0-30, 31-60, 61-90, 91-180, and over 180 days so that every file belongs to exactly one bucket. Those are internal management intervals, not statutory payment promises. A pending objection may be normal in one county and urgent in another. Record the actual reason, next event, responsible party, and evidence date instead of changing the clock to make the report look younger.",
                "For the first thirty days, confirm receipt, assigned claim number, and whether the clerk identified missing documents. At sixty days, seek a dated status update through counsel or the clerk's permitted channel and compare the case with its county's observed processing history. At ninety days, review unresolved service, competing claims, hearings, and proposed distribution calculations with counsel. At one hundred eighty days, reassess expected collection timing and reserve coverage without abandoning an otherwise viable claim. A deadline due tomorrow takes precedence over a young aging bucket. Separate funds ordered, funds issued, claimant funds received, and firm fees collected; these are different events. Never count the full county payment as firm revenue when most belongs to the claimant.",
                "Make reconciliation a short exception meeting with documentary outputs. The operations owner identifies stale evidence, unexplained amount changes, duplicate county entries, and bank receipts that do not match the case ledger. The principal resolves spending changes; counsel owns legal responses; the specialist delivers claimant updates using verified facts. Reconcile opening receivables plus newly earned fees minus collections and supported adjustments to closing receivables, applying the firm's accounting policy consistently. Keep speculative pipeline outside that arithmetic. If a claimant receives funds directly, use authorized payment evidence and the contract to establish the fee due rather than treating silence as payment. A weekly signed reconciliation note should list exceptions, owners, due dates, and the specific records needed to close each item.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Freeze the register", "action": "Export dated case balances.", "detail": "Preserve prior balances and source timestamps."},
                {"step": 2, "title": "Match evidence", "action": "Compare docket, counsel, county, and bank records.", "detail": "Separate claimant proceeds from collected firm fees."},
                {"step": 3, "title": "Assign exceptions", "action": "Name an owner and next date.", "detail": "Prioritize statutory deadlines independently of aging."},
                {"step": 4, "title": "Close the loop", "action": "Save reconciliation and claimant updates.", "detail": "Carry unresolved differences into the next meeting."},
            ],
        },
        {
            "heading": "Audit communication and protect claimant records",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Audit five outreach interactions per specialist each week, or every interaction when the week's volume is lower. Include at least one nonresponse sequence, one fee explanation, and one disputed-identity exchange when available. Score whether the specialist accurately named the firm, identified the official source, explained the claimant's direct filing option, described contractual fees without exaggeration, and avoided claiming government affiliation. Use recordings only where the required consent and recording rules have been satisfied; otherwise audit contemporaneous notes and the script version. A scripted conversation can remain humane and flexible while keeping factual claims stable. Correct a misleading statement promptly, document the correction, and revise the specific sentence that caused the problem before the next similar contact.",
                "Keep claimant identification, addresses, signatures, banking details, and probate records in an encrypted case repository with role-based access and individual accounts. Use encryption in transit and at rest, multifactor authentication, device encryption, expiring document links, and encrypted backups with tested restoration. The abstractor normally needs property records rather than banking instructions; the outreach specialist does not need every probate attachment. Exchange sensitive packets through the protected repository instead of open email attachments or shared personal drives. Log access and downloads, revoke access immediately when assignments end, and document a retention schedule tied to contracts and applicable duties. Do not place identification numbers in task titles, public calendar invitations, or spreadsheets distributed to unrelated vendors.",
                "Section 6801 of Title 15 states the privacy and safeguarding policy for customers of financial institutions and describes objectives for administrative, technical, and physical safeguards. Determine whether the particular recovery business and activities fall within applicable financial-institution definitions and implementing rules; do not claim that every recovery firm automatically has identical obligations under that section. The controls described here remain practical operating choices regardless of that determination. Test one lost-device scenario and one mistaken-recipient scenario before expanding the desk. Identify who disables access, preserves logs, contacts counsel, and evaluates notification requirements. Combine communication findings, access exceptions, filing errors, and aging trends in the weekly operating review so growth reflects reliable execution rather than merely more records in the queue.",
            ],
            "callout": {"kind": "OPERATOR GATE", "title": "Expand a proven queue, not an unmeasured backlog", "body": "Add a county only after assigning its records, counsel, and collection runway.", "items": ["Document state-specific filing responsibility.", "Fund six months of modeled operating costs.", "Resolve critical script and data-access exceptions."]},
        },
    ],
    "pull_quote": "Scale the handoff before you scale the county list.",
    "diagram_id": "diag-06-small-team-org",
    "action_checklist": [
        "Assign the four Base seats and per-file attorney responsibilities.",
        "Document worker classification using actual working arrangements.",
        "Reconcile the 30/60/90/180-day claim buckets weekly.",
        "Audit outreach samples and correct inaccurate scripts.",
        "Test encryption, access revocation, and backup restoration.",
        "Compare measured capacity with the six-person cost envelope.",
    ],
    "statutory_citations": [
        {"title": "29 U.S.C. § 203", "url": "https://www.law.cornell.edu/uscode/text/29/203", "relevance": "Federal wage-and-hour definitions relevant to staffing and classification analysis."},
        {"title": "15 U.S.C. § 6801", "url": "https://www.law.cornell.edu/uscode/text/15/6801", "relevance": "Financial-institution customer privacy and safeguarding policy; applicability requires separate analysis."},
    ],
}

Q12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-thirty-days-surplus-plan",
    "question_prompt": "Q12: What should a surplus recovery operator do in the first thirty days?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30 Days: Step-by-Step Surplus Implementation Plan",
    "subtitle": "From county statute selection and O&E title scrubs to your first verified claim packets.",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 12,
    "executive_summary": "The first month should produce a documented county strategy, thirty evidence-backed title screens, twelve carefully selected claimant investigations, and a reproducible packet workflow. Begin with official statutes and clerk procedures, then engage state-qualified counsel before contacting prospects. Separate posted balances from recoverable equity and distinguish a negative database search from proven entitlement. Spend the final week executing supported claims or rehearsing packet quality control when signatures are unavailable. Judge the pilot by evidence completeness, acquisition economics, and a funded 180-day runway, not by an assumed first-month payout or a target number of signed agreements.",
    "key_metrics": [
        {"label": "Market", "value": "2 counties", "context": "1-2 states", "note": "Choose documented volume and accessible official records."},
        {"label": "Underwriting", "value": "30 files", "context": "$15,000 minimum posted gross balance", "note": "Screening threshold, not evidence of claimant equity."},
        {"label": "Outreach", "value": "Top 12 claimants", "context": "Title and bankruptcy review first", "note": "Contact only supported candidates; do not fill a quota with weak files."},
        {"label": "Liquidity", "value": "180 days", "context": "Operating reserve horizon", "note": "Unpaid contingent fees are excluded from available cash."},
    ],
    "sections": [
        {
            "heading": "Days 1-7: Select the counties and document the rules",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 1 defines the pilot's cash ceiling, accountable operator, and available weekly hours. Day 2 compares official excess-proceeds inventories and sale calendars to choose two high-volume tax-deed or foreclosure counties in one or two states. Volume means a dated count of plausible balances and recent sales, not a marketing claim about a state. Prefer counties with accessible docket records, recorded instruments, and a clear clerk contact channel. Keep tax-sale and mortgage-foreclosure routes in separate columns because the same county can administer them under different statutes. Record the selection rationale and a backup county, but do not launch a third queue before the first two have usable forms and a documented review process.",
                "Day 3 opens a jurisdiction matrix for each selected sale type. Capture claimant eligibility, priority, claim deadline, fee caps if applicable, contract restrictions, assignment requirements, waiting periods if applicable, and the official authority for each entry. Mark uncertain entries unresolved rather than copying assumptions from a neighboring state. Florida section 197.582 addresses tax-deed surplus distribution; California Revenue and Taxation Code section 4675 addresses claims to excess proceeds from tax-defaulted property sales. Neither citation should be casually substituted for a mortgage-foreclosure rule. Separate the statute's text from counsel's interpretation and the clerk's administrative instructions. Preserve retrieval dates and section references so a later rule change can be traced to the affected files and outreach language.",
                "Day 4 downloads current clerk claim forms, instructions, proof-of-identity requirements, and sample filing receipts where available. Day 5 checks the forms against the matrix and sends specific unresolved questions to a licensed foreclosure or probate attorney qualified for the chosen matters. Day 6 agrees co-origination terms with that attorney, spelling out claimant representation, conflicts, referral arrangements, fee allocation where permitted, costs, custody of documents, and responsibility for filing. Do not assume a nonlawyer may share legal fees; structure compensation around applicable professional rules. Day 7 signs the supported arrangement and freezes the pilot checklist. If a second state requires additional counsel, secure that coverage before its files advance to legal work rather than treating one attorney's license as nationwide authority.",
            ],
            "table": {
                "caption": "First-week daily evidence",
                "headers": ["Day", "Action", "Saved output"],
                "rows": [
                    ["1", "Set budget and ownership", "Cash ceiling and hours"],
                    ["2", "Choose two counties", "Dated inventory comparison"],
                    ["3", "Map statutes", "Fee, deadline, waiting-period matrix"],
                    ["4", "Collect clerk forms", "Versioned official forms"],
                    ["5", "Resolve route questions", "Counsel question log"],
                    ["6", "Draft co-origination terms", "Responsibility and cost schedule"],
                    ["7", "Sign supported terms", "Engagement and pilot checklist"],
                ],
            },
        },
        {
            "heading": "Days 8-14: Underwrite thirty balances, not thirty names",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 8 retrieves the official county excess-proceeds lists and preserves the original documents, publication dates, and source URLs. Day 9 normalizes parcel identifiers, case numbers, sale dates, apparent owners, and gross balances, then removes duplicates and filters balances below $15,000. A posted balance is only an intake signal: disbursements, superior claims, stale postings, and administrative adjustments may already have changed it. Confirm the current amount through an official record or permitted clerk inquiry before spending heavily. Create thirty numbered pilot files with immutable source references. If fewer than thirty meet the criteria, record the shortfall and continue the supported sample; lowering the threshold merely to fill the worksheet corrupts the pilot's economics.",
                "Days 10 through 12 run grantor and grantee vesting searches and ownership-and-encumbrance, or O&E, scrubs on ten files per day, adjusting the pace if records require more work. Link the sale account to the correct legal description and trace conveyances through the relevant entitlement date. Search former names, trusts, estates, entity variations, and recorded interests against the appropriate county index. Identify mortgages, judgments, tax liens, assignments, releases, probate documents, and potentially competing interests. A deed alone does not establish who receives every dollar. Keep an instrument-by-instrument timeline, with recording number and unresolved effect, and send legal priority questions to counsel rather than deleting a lien because it is old or absent from a commercial summary.",
                "Day 13 reconciles the thirty O&E bundles with the current surplus evidence and creates a provisional waterfall for each file. Subtract only documented allowances and claims in a counsel-supported priority order, keeping uncertain deductions visible as ranges. A $40,000 posted balance with $18,000 of potential superior claims and $2,000 of authorized costs suggests $20,000 of provisional claimant equity, not a $40,000 fee base. Day 14 ranks candidates by supported net equity, record completeness, deadline proximity, and contact feasibility. Select up to twelve lien-clean candidates, meaning the surviving-interest review supports outreach rather than that every search can prove an absolute absence of liens. Preserve rejected files and reasons so the principal can distinguish poor county inventory from weak search execution.",
            ],
            "table": {
                "caption": "Daily production and exception register",
                "headers": ["Day", "Action", "Completion evidence"],
                "rows": [
                    ["8", "Pull official lists", "Original files and dates"],
                    ["9", "Filter and deduplicate", "Thirty eligible file IDs or shortfall"],
                    ["10", "Scrub files 1-10", "Vesting and O&E bundles"],
                    ["11", "Scrub files 11-20", "Instrument chronology"],
                    ["12", "Scrub files 21-30", "Lien and release evidence"],
                    ["13", "Calculate waterfalls", "Documented equity ranges"],
                    ["14", "Rank candidates", "Top twelve and rejection reasons"],
                ],
            },
        },
        {
            "heading": "Days 15-21: Verify people and explain the offer accurately",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 15 skip-traces the top twelve supported claimants using permitted sources and stores provenance for each address and telephone number. Match multiple identifiers without spreading sensitive personal data into the general task queue. Day 16 checks probate authority, trust capacity, entity status, and name collisions before assuming the located person can sign. A surviving family member is not automatically the authorized estate representative, and a former officer may not bind a dissolved entity. Suppress wrong-party contacts and record the reason. If a claimant declines further contact, update all active contact channels rather than relying on one employee's notes. Never discuss the apparent surplus with unrelated neighbors or employers simply because they answered a tracing call.",
                "Day 17 searches PACER for relevant bankruptcy cases using verified names and appropriate identifiers, then has counsel evaluate matches, discharge records, trustee authority, abandoned property, and pending proceedings where material. A negative PACER search is evidence of the search performed, not universal proof of bankruptcy clearance. Record query date, identifiers, result, reviewer, and remaining limitations; use current docket records to resolve matches. Refresh this review before filing if time or new information warrants it. The operational aim is bankruptcy-clear routing supported by counsel, not a checkbox that silently ignores unresolved cases. Hold affected outreach or contracting steps when authority is uncertain, while continuing supported files that do not depend on that unresolved question.",
                "Day 18 prepares transparent verification packets naming the official source, the firm's private role, the claimant's option to approach the clerk directly, the proposed fee basis, anticipated costs, and uncertainties in amount and timing. Day 19 sends packets through approved contact channels and logs delivery without treating delivery as agreement. Day 20 conducts scripted conversations and records them only where applicable recording and consent requirements are satisfied; otherwise use structured contemporaneous notes. Explain that posted surplus can be reduced by competing claims. Day 21 audits the first interactions against the actual documents, corrects misunderstandings, and schedules only supported signings. Measure verified contacts and informed decisions separately from signed contracts so the team does not improve its apparent conversion rate by pressuring confused recipients.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Verify", "action": "Match claimant identity and authority.", "detail": "Retain source references and unresolved discrepancies."},
                {"step": 2, "title": "Review bankruptcy", "action": "Search PACER and route material results to counsel.", "detail": "Date the review; a negative query alone is not clearance."},
                {"step": 3, "title": "Explain", "action": "Send the source-backed verification packet.", "detail": "State private role, direct filing option, fees, costs, and uncertainty."},
                {"step": 4, "title": "Audit", "action": "Compare the conversation with the packet.", "detail": "Correct discrepancies before execution or filing."},
            ],
        },
        {
            "heading": "Days 22-30: Execute packets and decide from measured economics",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Day 22 confirms willing claimants, signing authority, document versions, and any required witnesses. Day 23 coordinates the mobile notary and accessible appointment logistics without instructing the notary to bypass identification or presence requirements. Day 24 checks signed pages, certificates, dates, exhibits, legal descriptions, and consistency of claimant names. Day 25 sends complete packets to counsel for final legal review and filing where the route requires counsel; obtain the actual submission receipt and note any clerk deficiencies. If no claimant has signed, run the same sequence on a clearly labeled synthetic or redacted training packet and stop before submission. A rehearsal tests workflow but must never appear in the register as a real filed claim or earned fee.",
                "Day 26 reconciles actual filing acknowledgments, missing exhibits, and claimant updates. Day 27 totals pilot acquisition spending, separating list preparation, title searches, tracing, outreach labor, notary costs, and case-specific counsel charges so nothing is counted twice. Calculate cost per screened file, verified contact, signed engagement, and filed claim using actual denominators; when the denominator is zero, label the ratio unavailable. An illustrative $6,000 spent across thirty screens costs $200 per screen; if three engagements result, acquisition cost is $2,000 per engagement before later servicing costs. Those ratios do not establish profitability. Estimate collection probability and expected net fee contribution separately, document assumptions, and do not present a signed contingent agreement as collected revenue.",
                "Day 28 tests the 180-day reserve runway using available unrestricted cash and forecast operating outflows. At $12,000 monthly cash burn, six months requires approximately $72,000 before a separate allowance for committed case costs and adverse timing; subtract those commitments first when computing runway. Use a dated cash schedule when exact 180-day coverage matters. Day 29 compares findings with the initial spending ceiling and identifies the single largest bottleneck, whether inventory quality, title ambiguity, contact accuracy, or execution. Day 30 records Continue, Revise, or Stop with evidence and a named next action. Continue only when supported economics and cash coverage justify the next cohort; revise a fixable bottleneck with a bounded experiment; stop new acquisition when the model cannot fund its own unresolved exposure. Preserve servicing obligations on existing claims under every decision.",
            ],
            "table": {
                "caption": "Final-week execution record",
                "headers": ["Day", "Action", "Output"],
                "rows": [
                    ["22", "Confirm signers", "Authority and appointment list"],
                    ["23", "Coordinate notary", "Execution record or rehearsal"],
                    ["24", "Inspect packet", "QC exceptions and corrections"],
                    ["25", "Counsel review and filing", "Receipt or labeled rehearsal result"],
                    ["26", "Reconcile acknowledgments", "Deficiency and update log"],
                    ["27", "Calculate acquisition costs", "Actual spend and denominators"],
                    ["28", "Stress reserve runway", "180-day cash schedule"],
                    ["29", "Diagnose bottleneck", "Evidence-backed experiment"],
                    ["30", "Continue / Revise / Stop", "Decision, owner, and next date"],
                ],
            },
            "callout": {"kind": "OPERATOR GATE", "title": "Day-30 Continue / Revise / Stop", "body": "Decide on evidence, contribution economics, and funded runway rather than promised first-month collections.", "items": ["Continue: supported pipeline and adequate cash coverage.", "Revise: one bounded, measurable correction.", "Stop: cease new acquisition while servicing existing obligations."]},
        },
    ],
    "pull_quote": "Your first thirty days should produce proof, not promises.",
    "diagram_id": "diag-08-30-day-roadmap",
    "action_checklist": [
        "Select two counties and document each sale route separately.",
        "Record fee rules, waiting periods, deadlines, and current clerk forms.",
        "Sign supported co-origination terms with licensed counsel.",
        "Scrub thirty files and rank up to twelve supported claimants.",
        "Complete identity, authority, and bankruptcy review before advancing claims.",
        "File supported packets or document an end-to-end rehearsal.",
        "Calculate actual acquisition costs and a 180-day reserve schedule.",
        "Record the Day-30 decision and continuing claimant obligations.",
    ],
    "statutory_citations": [
        {"title": "Fla. Stat. § 197.582", "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.582.html", "relevance": "Florida tax-deed surplus distribution framework; distinguish mortgage-foreclosure procedures."},
        {"title": "Cal. Rev. & Tax. Code § 4675", "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=4675.&lawCode=RTC", "relevance": "California tax-defaulted sale excess-proceeds claims, eligible interests, and claim timing."},
    ],
}

CHAPTERS_11_TO_12 = [Q11, Q12]

def build_volume_002_workbook() -> dict:
    """Return a fresh workbook, including independent nested worksheet records."""
    def field(label: str, input_type: str, guidance: str) -> dict:
        return {"field_label": label, "input_type": input_type, "guidance": guidance}

    return {
        "workbook_id": "wb-002-surplus-funds-recovery",
        "title": "Surplus Funds Recovery Operator Companion Workbook",
        "subtitle": "6 Field Worksheets, Lien-Priority Calculators & 30-Day Execution Logs",
        "worksheets": [
            {
                "worksheet_number": 1,
                "slug": "county-list-and-statute-screen",
                "title": "County List and Statute Screen",
                "purpose": "Select two evidence-backed pilot counties and distinguish their tax-sale and foreclosure claim routes before acquisition spending.",
                "instructions": [
                    "Complete one record per county and sale route; never transfer tax-deed assumptions into a mortgage-foreclosure file.",
                    "Attach the official inventory and current forms, then extract each rule with its source, retrieval date, and unresolved questions.",
                    "Compare eligible inventory, record accessibility, counsel coverage, and deadlines; explain why the chosen pair outranks alternatives.",
                ],
                "fields": [
                    field("County, state, and sale route", "text", "Name the administering office and distinguish tax deed, tax-defaulted sale, and mortgage foreclosure."),
                    field("Official inventory source and snapshot", "textarea", "Record URL, retrieval date, list date, file reference, and count of unique balances at least $15,000."),
                    field("Governing statutes and effective text", "textarea", "Record section, official URL, retrieval date, and the precise rule supported; identify unresolved interpretation."),
                    field("Fee and contract restrictions", "textarea", "Record applicable fee cap and base, assignment restrictions, and counsel's source-backed interpretation; unknown is not unrestricted."),
                    field("Waiting periods and claim deadlines", "textarea", "Record triggering event, calculation method, actual deadline, authority, and reminder dates separately."),
                    field("Clerk forms and filing channel", "textarea", "List current form versions, identity evidence, required exhibits, filing location, and receipt method."),
                    field("Counsel coverage and co-origination terms", "textarea", "Record licensed attorney, relevant state coverage, engagement scope, permissible compensation arrangement, and signed date."),
                    field("County selection decision", "textarea", "Compare volume and record quality; name the reviewer, spending ceiling, remaining questions, and next review date."),
                ],
                "completion_checklist": [
                    "Two counties have dated official inventory evidence.",
                    "Sale routes, fee rules, waiting periods, and deadlines are separately documented.",
                    "Current clerk forms and applicable counsel coverage are attached.",
                    "Unresolved rules have owners rather than guessed answers.",
                ],
            },
            {
                "worksheet_number": 2,
                "slug": "chain-of-title-and-lien-waterfall",
                "title": "Chain of Title and Lien Waterfall",
                "purpose": "Connect a surplus account to a supported claimant and calculate provisional equity without confusing recorded interests with resolved priority.",
                "instructions": [
                    "Create one sheet per file and attach the source instruments, not just a commercial title summary.",
                    "Build a chronological vesting chain, then a separate counsel-reviewed priority waterfall; chronology alone does not decide legal priority.",
                    "Mark disputed interests and missing releases explicitly. Recalculate low and high equity estimates when unresolved claims change.",
                ],
                "fields": [
                    field("File, parcel, case, and sale identifiers", "text", "Match the legal description and sale account; document any identifier mismatch."),
                    field("Current verified surplus balance", "number", "Enter dollars and attach the official balance evidence and as-of date."),
                    field("Grantor and grantee search log", "textarea", "Record index, search period, name variations, query dates, and instrument references for each link."),
                    field("Vesting and representative authority", "textarea", "Identify entitlement date, owner, conveyances, probate appointment, trust capacity, or entity authority evidence."),
                    field("O&E surviving-interest register", "textarea", "For each mortgage, judgment, tax lien, or other interest, record amount, holder, recording number, release, and unresolved effect."),
                    field("Counsel-reviewed priority order", "textarea", "List allowed claims in distribution order with legal basis and reviewer; distinguish disputed from established amounts."),
                    field("Provisional equity waterfall", "textarea", "Start with verified surplus; subtract supported superior distributions and authorized costs once. Show claimant allocations and uncertain ranges separately."),
                    field("Bankruptcy search and disposition", "textarea", "Record PACER identifiers, query date, case matches, counsel review, trustee issues, and refresh date; no-match is not conclusive clearance."),
                    field("Underwriting disposition", "textarea", "Advance, investigate, or decline; name the unresolved evidence, owner, deadline, and spending ceiling."),
                ],
                "completion_checklist": [
                    "Vesting instruments and legal description match the surplus account.",
                    "Each potential surviving interest has evidence and a disposition.",
                    "Priority assumptions and bankruptcy questions are reviewed by counsel.",
                    "Equity ranges exclude unsupported or duplicate deductions.",
                ],
            },
            {
                "worksheet_number": 3,
                "slug": "net-surplus-and-fee-calculator",
                "title": "Net Surplus and Fee Calculator",
                "purpose": "Separate claimant recovery, lawful firm fees, file contribution, and reserve coverage using auditable manual calculations.",
                "instructions": [
                    "Copy only dated, supported amounts from the title waterfall. These are calculation fields, not an automated legal-priority engine.",
                    "Calculate claimant allocation after superior distributions, then apply the supported contractual fee basis and applicable restrictions.",
                    "Keep claimant-borne expenses separate from firm-borne costs and reconcile every deduction to avoid double counting.",
                ],
                "fields": [
                    field("Verified county surplus", "number", "Enter S in dollars with evidence date; a posted list balance may require refresh."),
                    field("Superior distributions and pool costs", "textarea", "Itemize L and K with sources; provisional available equity is max(0, S - L - K). Flag any unresolved priority."),
                    field("Claimant allocation", "textarea", "Enter A after supported competing-owner shares; explain allocation evidence and low/high scenarios."),
                    field("Permitted fee basis and contractual terms", "textarea", "Specify dollar or percentage terms, fee base B, and source-backed cap if applicable. Do not assume every jurisdiction permits the same base."),
                    field("Firm fee calculation", "textarea", "For a permitted percentage contract compute F = B x rate, limited by applicable rules and contract. Distinguish estimated, earned, and collected F."),
                    field("Claimant net distribution", "textarea", "Compute A minus claimant-paid F and any separately authorized claimant expenses not already deducted; explain any negative result rather than concealing it."),
                    field("Firm contribution and acquisition cost", "textarea", "Compute collected F minus firm-borne acquisition and servicing costs. Track expected contribution separately using explicit collection assumptions."),
                    field("Pilot unit acquisition ratios", "textarea", "Divide actual acquisition spend by screened files, verified contacts, engagements, and filed claims separately; use unavailable for zero denominators."),
                    field("180-day cash reserve", "textarea", "List unrestricted cash, committed case costs, and dated operating outflows. Exclude unpaid fees; compute remaining cash and coverage under delayed collections."),
                ],
                "completion_checklist": [
                    "Fees are not calculated on an unsupported posted balance.",
                    "Every cost is assigned once to the proper payer.",
                    "Claimant net, firm fee, and firm contribution remain distinct.",
                    "Cash coverage survives the documented collection-delay scenario.",
                ],
            },
            {
                "worksheet_number": 4,
                "slug": "skip-trace-and-outreach-log",
                "title": "Skip-Trace and Outreach Log",
                "purpose": "Document supported identity matching, transparent contact, and communication quality for the top twelve candidates.",
                "instructions": [
                    "Open one log per claimant; keep sensitive identifiers in the restricted repository and reference them by file ID here.",
                    "Record each contact attempt with channel, time, script version, outcome, and next action. Suppress wrong parties and declined contact across channels.",
                    "Audit actual statements against the verification packet; preserve recordings only when recording requirements are satisfied.",
                ],
                "fields": [
                    field("Candidate and underwriting reference", "text", "Record file ID, rank, supported equity range, and underwriting review date."),
                    field("Trace sources and identity match", "textarea", "Record permitted source, retrieval date, matching identifiers, confidence limitations, and wrong-party exclusions."),
                    field("Authority and bankruptcy review", "textarea", "Reference representative authority evidence and counsel's dated disposition of relevant PACER results."),
                    field("Verification packet version", "text", "Reference official source, private-firm identity, direct filing option, fee basis, costs, and uncertainties."),
                    field("Contact attempt history", "textarea", "Record timestamp, channel, verified recipient, script version, outcome, and permitted next contact."),
                    field("Recording basis or structured notes", "textarea", "Record applicable recording requirements and obtained consent where needed; otherwise use contemporaneous notes."),
                    field("Claimant decision and suppression", "textarea", "Distinguish questions, interest, agreement, refusal, wrong party, and no response; record suppression actions."),
                    field("QA findings and corrections", "textarea", "Identify exact inaccurate statement, corrected wording, reviewer, claimant follow-up, and completion date."),
                ],
                "completion_checklist": [
                    "Identity and signing authority are supported before execution.",
                    "No government affiliation or assured payout was implied.",
                    "Fee explanation and direct filing option were provided accurately.",
                    "Wrong-party and declined-contact records are suppressed.",
                ],
            },
            {
                "worksheet_number": 5,
                "slug": "claim-packet-notary-and-counsel-qc",
                "title": "Claim Packet, Notary and Counsel QC",
                "purpose": "Produce a complete, traceable execution and filing package while separating real submissions from training rehearsals.",
                "instructions": [
                    "Use the current county-route checklist and counsel's file-specific requirements; document deviations rather than silently omitting exhibits.",
                    "Review execution before submission and retain the actual receipt. If unsigned, rehearse with labeled synthetic or redacted documents and do not submit.",
                    "After filing, preserve deficiencies and aging events without resetting the original acceptance date.",
                ],
                "fields": [
                    field("File and packet mode", "text", "Specify real claim or rehearsal, county route, case ID, claimant, and checklist version."),
                    field("Required forms and exhibits", "textarea", "Index claim form, identity evidence, vesting documents, authority papers, and counsel-required attachments."),
                    field("Execution and notary record", "textarea", "Record signer capacity, appointment, required witnesses, certificate completeness, and notary details without duplicating sensitive ID numbers."),
                    field("Document consistency review", "textarea", "Check names, dates, legal description, signatures, pagination, exhibit references, and unfilled fields."),
                    field("Counsel review and corrections", "textarea", "Name responsible attorney, review date, legal questions resolved, remaining deficiencies, and final packet version."),
                    field("Submission and acknowledgment", "textarea", "Record filing channel, actual submission date, receipt ID, and accepted-complete date; rehearsal has no real receipt."),
                    field("Aging and next event", "textarea", "Assign 0-30, 31-60, 61-90, 91-180, or over-180-day bucket from acceptance; record statutory deadlines independently."),
                    field("Disbursement and fee reconciliation", "textarea", "Track ordered, issued, claimant-received, and firm-collected amounts with evidence; do not recognize the entire claimant payment as fees."),
                ],
                "completion_checklist": [
                    "Current forms, authority, and required exhibits are complete.",
                    "Execution defects are corrected before submission.",
                    "Real filings have receipts; rehearsals are labeled and unsubmitted.",
                    "Aging owner, next event, and claimant update are assigned.",
                ],
            },
            {
                "worksheet_number": 6,
                "slug": "thirty-day-surplus-execution-log",
                "title": "Thirty-Day Surplus Execution Log",
                "purpose": "Connect every pilot day to a saved deliverable and make the Day-30 decision from actual evidence and cash exposure.",
                "instructions": [
                    "Create one daily row for days 1-30 using Q12's roadmap; record planned output, actual output, evidence reference, spending, and unresolved owner.",
                    "Reconcile weekly totals without counting the same file twice. Report shortfalls rather than weakening underwriting thresholds.",
                    "At day thirty, record Continue, Revise, or Stop and preserve existing claimant-service obligations regardless of acquisition decisions.",
                ],
                "fields": [
                    field("Daily execution rows", "textarea", "For each day record date, owner, planned action, actual result, evidence link, cost, and next step."),
                    field("Days 1-7 county foundation", "textarea", "Reference two county choices, statutory matrix, fee and waiting-period findings, current forms, and signed counsel arrangement."),
                    field("Days 8-14 title production", "textarea", "Track official lists, balances at least $15,000, thirty O&E screens, missing records, waterfalls, and ranked candidates."),
                    field("Days 15-21 claimant verification", "textarea", "Track up to twelve trace investigations, authority checks, PACER review, packet delivery, outreach, and script corrections."),
                    field("Days 22-26 execution evidence", "textarea", "Track signers, notary appointments, packet QC, counsel submissions, receipts, or explicitly labeled rehearsal outcomes."),
                    field("Days 27-28 economics and reserve", "textarea", "Record acquisition spend, actual conversion denominators, expected contribution assumptions, and the 180-day cash schedule."),
                    field("Day 29 bottleneck diagnosis", "textarea", "Name the dominant constraint, supporting counts, proposed correction, experiment budget, and success measure."),
                    field("Day 30 Continue / Revise / Stop", "textarea", "Record decision, evidence, cash coverage, responsible owner, next review date, and ongoing servicing commitments."),
                ],
                "completion_checklist": [
                    "All thirty days have actual outputs or explained exceptions.",
                    "Cohort counts reconcile without duplicate files or rehearsal filings.",
                    "Unit costs use actual denominators and cash excludes unpaid fees.",
                    "The final decision has evidence, an owner, and a dated next action.",
                ],
            },
        ],
    }


