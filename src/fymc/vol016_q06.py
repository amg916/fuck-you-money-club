from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-first-probate-real-estate-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in probate real estate, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (4–18 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "County Dockets, Executor Authority, Municipal Distress Signals, Attorney Referrals, and Retained-Commission Pipeline Economics",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #9, Probate Real Estate, ranks #16 with a 76/100 Money-to-Manpower "
        "Score. This chapter turns 11 mapped plays into an authority-first sourcing "
        "system: docket intelligence, property distress signals, professional referrals, "
        "and executor service demand become verified conversations rather than indiscriminate "
        "mailing lists. Start with one county, establish lawful contact routes, and measure "
        "each transition from matched estate to collected commission. The first 3-to-10 "
        "closed wins belong inside a 4–18 month planning window, with court delays and "
        "family disputes explicitly tracked. Canonical annual owner profits are $24,000 "
        "Conservative, $140,250 Base, and $315,000 Scaled. Revenue means retained brokerage "
        "commissions after brokerage splits, never property sale proceeds, acquisition "
        "principal, or contractor invoices."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$120,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "20% net margin; $24,000 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$510,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "27.5% net margin; $140,250 annual owner net profit; 2 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$900,000",
            "context": "Annual retained brokerage commissions after brokerage splits",
            "note": "35% net margin; $315,000 annual owner net profit; 3 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Mine estate-property intersections instead of buying bereavement lists",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start in one county where your supervising broker can support probate "
                    "listings and local title counsel can explain the sale path. Build a "
                    "daily work queue from the superior court probate index, assessor parcel "
                    "records, recorder instruments, and municipal enforcement portals. A "
                    "petition identifies a possible estate, not an authorized seller; an "
                    "assessor mailing address identifies a tax destination, not necessarily "
                    "the owner or personal representative. Join records through parcel "
                    "number, vesting name, property address, and case number, retaining each "
                    "source URL and retrieval date. Require a human check before merging "
                    "common names or contacting anybody. Exclude sealed records and avoid "
                    "republishing family allegations or sensitive docket attachments. Use "
                    "Airtable or a protected SQLite database for normalized records, with "
                    "separate tables for estates, parcels, authority documents, contacts, and "
                    "activities. One estate can own several parcels, while one parcel can "
                    "involve multiple proceedings; forcing everything into a single lead "
                    "row produces duplicate outreach and mistaken authority assumptions. "
                    "Prefer permitted docket alerts and bulk downloads over fragile "
                    "scraping. Record access limits, source refresh intervals, and suppression "
                    "decisions so another operator can reproduce the shortlist without "
                    "reconstructing a researcher's memory."
                ),
                (
                    "The highest-value signal is usually a solvable coordination problem "
                    "attached to a marketable asset: an appointed representative living "
                    "elsewhere, an unsecured vacant home, an unresolved permit, or carrying "
                    "costs consuming estate liquidity. None proves distress pricing or "
                    "permission to sell. Implement municipal_code_violation_trigger_arbitrage "
                    "by checking permitted municipal building portals and county recorder "
                    "dockets daily for failed structural or fire inspections, expired "
                    "permits, code citations, and newly filed mechanic's liens. Cross-match "
                    "those events against verified estate parcels, then determine whether "
                    "the estate wants contractor or construction-attorney assistance. A "
                    "filed lien is a claim requiring investigation, not an adjudicated "
                    "debt. Route an authorized introduction exclusively to one suitable "
                    "provider for a documented response window; share only necessary "
                    "details and never imply municipal endorsement. Illustratively, 40 "
                    "alerts at eight review minutes consume 320 minutes; at $30 per "
                    "research hour, screening costs $160 before software and supervision. "
                    "If six events match estates and two produce requested introductions, "
                    "research cost is $80 per introduction. Book no contractor invoice "
                    "as brokerage revenue. When daily access is unavailable, use "
                    "low-frequency scheduled API or bulk exports and identify every "
                    "outreach as private commercial contractor or remediation assistance."
                ),
                (
                    "Operate the 11 mapped plays below as complementary entry points into "
                    "one estate pipeline, not eleven independent businesses or eleven "
                    "revenue forecasts. New appointments establish authority candidates; "
                    "attorney relationships reduce documentation friction; executor "
                    "education captures voluntary demand; condition signals identify "
                    "specific work somebody must coordinate. Every record receives one "
                    "primary acquisition source and optional supporting signals, preventing "
                    "a permit notice, lawyer introduction, and webinar registration from "
                    "becoming three credited opportunities. Distinguish a brokerage "
                    "prospect from an acquisition prospect before discussing price. If "
                    "your business might purchase the property, disclose that role and "
                    "associated conflicts, obtain independent valuation support, and "
                    "follow the jurisdiction's fiduciary and brokerage requirements. "
                    "Do not present your own offer as independent market advice. "
                    "Underwriting must separately identify purchase principal, repair "
                    "capital, financing expense, and resale exposure; none belongs in "
                    "this volume's retained-commission scorecard. For the initial launch, "
                    "favor brokerage and executor coordination over speculative inventory. "
                    "Review source quality weekly using documented authority, reachable "
                    "decision-makers, and achievable sale timing rather than raw lead "
                    "counts. Suspend a source that repeatedly creates mistaken identities "
                    "or unwanted contact, even when its apparent cost per record looks low."
                ),
            ],
            "table": {
                "caption": "Eleven Mapped Probate Sourcing Plays: Signals, Test Economics, and Failure Fallbacks",
                "headers": [
                    "Mapped play and operating entry point",
                    "Evidence that earns further investigation",
                    "Illustrative unit math for a bounded test",
                    "Failure mode and specific operating fallback",
                ],
                "rows": [
                    [
                        "New-appointment docket mining for verified estate-property matches",
                        "Compare appointment orders and issued letters against recorder vesting",
                        "Review 100 cases at six minutes each: ten research hours",
                        "Petitions lack authority; wait for appointment evidence before qualification",
                    ],
                    [
                        "Probate-attorney referral flywheel through documented property-status briefs",
                        "Counsel requests help with valuation, access, or sale execution",
                        "Twelve tailored meetings yielding three introductions means four meetings each",
                        "Avoid paid legal referrals; offer useful documentation without reciprocal obligations",
                    ],
                    [
                        "Out-of-area executor concierge through secure property coordination",
                        "Representative confirms travel constraints and requests local operating support",
                        "Eight consultations yielding two mandates means four consultations per mandate",
                        "Distance proves no urgency; offer scheduled reporting instead of pressure",
                    ],
                    [
                        "Vacancy and carrying-cost triage for authorized estate representatives",
                        "Verified vacancy combines with insurance questions and recurring estate expenses",
                        "Three months at $2,200 carrying costs exposes $6,600 estate expense",
                        "Occupancy remains uncertain; obtain authorized inspection before proposing access",
                    ],
                    [
                        "municipal_code_violation_trigger_arbitrage: verified estate remediation and construction-attorney introductions",
                        "Failed structural or fire inspections, expired permits, citations, new mechanic's liens",
                        "Forty eight-minute reviews cost $160 at $30 per research hour",
                        "Use scheduled API or bulk exports; identify private commercial assistance",
                    ],
                    [
                        "Title-curative triage for recorder discrepancies and blocked transfers",
                        "Title professional identifies vesting, release, or ownership defects requiring resolution",
                        "Six screened parcels producing two viable files means three screens each",
                        "Do not interpret ownership conclusively; route defects to qualified counsel",
                    ],
                    [
                        "Expired probate-listing recovery through broker-approved representation checks",
                        "Listing expired and authorized representative confirms no conflicting exclusive engagement",
                        "Twenty researched expirations yielding four conversations means five records each",
                        "Honor active representation; defer solicitation until broker verifies availability",
                    ],
                    [
                        "Executor education inbound through county-specific sale-process resources",
                        "Visitor requests a consultation about authority documents and sale preparation",
                        "Two hundred relevant visits yielding eight requests implies four percent conversion",
                        "Low-intent traffic wastes time; narrow pages to local procedural questions",
                    ],
                    [
                        "Estate cleanout and remediation partner introductions after executor permission",
                        "Provider encounters requested sale coordination beyond their contracted service scope",
                        "Ten partner conversations yielding two introductions means five conversations each",
                        "No undisclosed referral payments; use documented, permission-based introductions",
                    ],
                    [
                        "Court-sale calendar monitoring for properly funded probate buyers",
                        "Published hearing or sale notice identifies terms requiring independent verification",
                        "Six buyer briefings yielding two qualified attendees means three briefings each",
                        "Overbid and deposit rules vary; verify court-specific requirements before attendance",
                    ],
                    [
                        "Stalled-estate reactivation through requested milestone-based follow-up",
                        "Representative previously deferred sale pending appointment, dispute resolution, or title work",
                        "Thirty permitted follow-ups yielding three consultations implies ten percent conversion",
                        "Respect opt-outs and unresolved disputes; pause until an agreed milestone",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Four habits that separate useful intelligence from noisy lists",
                "body": (
                    "Prioritize verified estate work and preserve the source trail; "
                    "the competitive advantage is accurate coordination, not intrusive volume."
                ),
                "items": [
                    "Save the appointment document reference separately from the petition; the filing date does not establish the representative's powers.",
                    "Ask title staff which recorder defects repeatedly delay local probate closings, then add those document checks before pricing appointments.",
                    "Offer attorneys a one-page property-status brief covering authority evidence, access, title questions, carrying costs, and next responsibility.",
                    "Give a remediation provider one authorized response window, then return control to the executor instead of broadcasting the estate's details.",
                ],
            },
        },
        {
            "heading": "2. Qualify authority, economics, and readiness before spending acquisition money",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a 100-point qualification scorecard, but separate ranking from "
                    "permission. Award up to 25 points for documented authority, 20 for "
                    "a verified estate-property ownership connection, 15 for a stated "
                    "service need, 15 for feasible net proceeds, 15 for a realistic "
                    "decision timeline, and 10 for an appropriate contact route. A high "
                    "total never cures missing authority or a prohibited contact method. "
                    "Records scoring 75 or more can receive an appointment request only "
                    "after those prerequisites are satisfied; scores from 50 through 74 "
                    "receive missing-evidence tasks; lower scores remain research records "
                    "or are closed with a reason. These thresholds are internal workflow "
                    "choices, not externally validated predictors. Request current letters, "
                    "the appointment order, relevant restrictions, and the representative's "
                    "preferred counsel contact. In California, distinguish full from "
                    "limited authority under the Independent Administration of Estates "
                    "Act; Probate Code section 10501 addresses transactions requiring "
                    "court supervision, including real-property sales under limited "
                    "authority. Proposed-action notice procedures may apply under sections "
                    "10580 and following. Have counsel establish the applicable procedure "
                    "before promising a signing or closing date. A beneficiary's "
                    "enthusiasm is useful context, but it does not substitute for "
                    "the representative's verified powers."
                ),
                (
                    "Build a property economics sheet before recommending repairs or "
                    "promising an attractive net. Obtain a broker price opinion or "
                    "comparative market analysis, request title review through the proper "
                    "channel, and identify mortgage payoff requirements, recorded liens, "
                    "taxes, occupancy, insurance, utilities, and probable sale expenses. "
                    "Separate recorded amounts from current payoff figures and preliminary "
                    "estimates from written quotes. For illustration, a $750,000 sale "
                    "less $310,000 mortgage payoff, $18,000 other verified obligations, "
                    "$45,000 selling expenses, and $12,000 approved property work leaves "
                    "$365,000 before other estate liabilities and distributions. That "
                    "figure is a property-level planning estimate, not the brokerage's "
                    "revenue or the beneficiaries' assured distribution. Compare as-is "
                    "and repair paths using incremental net proceeds and time, not "
                    "photographic appeal. If $20,000 of work supports only $25,000 of "
                    "additional proceeds before another $6,000 of carrying expense, "
                    "the repair path loses $1,000 before execution risk. Ask the "
                    "representative and counsel who can authorize spending, sign vendor "
                    "contracts, and approve access. Do not advance substantial repair "
                    "money casually; reimbursement, security, conflicts, and estate "
                    "liquidity need explicit treatment. Preserve vendor estimates and "
                    "version every revised net sheet."
                ),
                (
                    "Translate qualification into a service proposition with clear "
                    "boundaries: establish the sale route, document condition, present "
                    "pricing options, coordinate authorized vendors, and report progress. "
                    "Avoid selling speed where the bottleneck is a hearing, objection, "
                    "or contested appointment. During discovery, ask what must happen "
                    "before a sale decision, who advises the representative, whether "
                    "anybody occupies the property, and which expenses are already "
                    "uncomfortable. Do not ask a newly contacted family to recount "
                    "personal circumstances merely to improve a sales script. A useful "
                    "first deliverable is a two-page readiness brief with an evidence "
                    "list, unresolved questions, estimated work sequence, and three "
                    "pricing alternatives supported by comparable sales. If the family "
                    "disagrees, stop framing consensus as a marketing objection and "
                    "return decision authority and dispute management to counsel. If "
                    "the property is occupied, require a lawful access plan rather "
                    "than assuming probate permits immediate possession. If title is "
                    "unclear, do not solicit a binding price commitment before the "
                    "appropriate professionals resolve the issue. Assign every blocking "
                    "question a responsible person and next review date. This makes "
                    "your pipeline operationally useful even when the correct immediate "
                    "answer is to wait."
                ),
            ],
            "table": {
                "caption": "Authority-First Qualification Scorecard and Evidence Requirements",
                "headers": [
                    "Qualification dimension and maximum available points",
                    "Evidence required for the strongest rating",
                    "Partial-credit condition requiring further operator work",
                    "Stop condition and assigned resolution route",
                ],
                "rows": [
                    [
                        "Documented representative authority contributes up to twenty-five points",
                        "Current letters and appointment order support the contemplated transaction",
                        "Appointment established but sale restrictions still require counsel review",
                        "Unappointed petitioner cannot authorize listing; await verified representative authority",
                    ],
                    [
                        "Verified estate-property connection contributes up to twenty points",
                        "Recorder vesting and estate documentation reconcile with parcel identifiers",
                        "Name matches but ownership chain requires title professional investigation",
                        "Conflicting ownership evidence pauses outreach claims about estate control",
                    ],
                    [
                        "Expressed service need contributes up to fifteen points",
                        "Representative requests valuation, preparation, access coordination, or sale execution",
                        "Public signal suggests work but representative has expressed no need",
                        "Explicit refusal triggers suppression rather than escalating sales pressure",
                    ],
                    [
                        "Feasible property net proceeds contribute up to fifteen points",
                        "Supported pricing and documented obligations indicate a workable sale path",
                        "Preliminary equity appears positive but payoff information remains incomplete",
                        "Likely shortfall requires lender and counsel strategy before promises",
                    ],
                    [
                        "Realistic transaction timing contributes up to fifteen points",
                        "Decision milestones and court procedure support an actionable work sequence",
                        "Sale is contemplated after a specific unresolved estate milestone",
                        "Active dispute pauses forecasts until counsel provides updated direction",
                    ],
                    [
                        "Appropriate reachable contact route contributes up to ten points",
                        "Verified representative provides contact preferences and necessary channel permissions",
                        "Only a permitted postal route has been independently verified",
                        "Suppression or channel restrictions prevent the proposed contact method",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four prerequisites before soliciting a signed mandate",
                "body": (
                    "Qualification scores prioritize work; these checks determine "
                    "whether the next proposed action is appropriate."
                ),
                "items": [
                    "Match parcel vesting to estate evidence and verify current letters, appointment restrictions, and the actual signing representative.",
                    "Confirm broker supervision, licensing coverage, existing representation, and any principal-buyer conflict before presenting your role.",
                    "Document the applicable court-supervised or independent-administration sale procedure with counsel, including notice and objection handling.",
                    "Check source access permissions, contact suppression, channel-specific requirements, and the representative's preferred communication route.",
                ],
            },
        },
        {
            "heading": "3. Run a restrained multichannel cadence that earns the first appointment",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Design a 45-day initial cadence around usefulness and contact "
                    "permissions, not escalating pressure. On day one, send a plain "
                    "postal letter when that route is appropriate: identify your "
                    "licensed brokerage, explain the property coordination service, "
                    "and offer a short readiness checklist. Do not print probate "
                    "details on the envelope or imply court affiliation. On day "
                    "ten, make a manual call only after applicable federal and "
                    "state solicitation rules, suppression lists, and calling hours "
                    "have been checked. Publication of a telephone number does not "
                    "itself authorize marketing calls or texts. On day twenty-one, "
                    "send one substantive follow-up by a permitted route, such as "
                    "an explanation of valuation versus an investor offer. On day "
                    "forty-five, ask whether they want milestone-based follow-up; "
                    "without a response, stop the initial sequence rather than "
                    "silently enrolling them in indefinite pursuit. Use requested "
                    "email for the checklist and appointment logistics, while "
                    "applying CAN-SPAM requirements to commercial email. Do not "
                    "launch automated calls, prerecorded messages, or marketing "
                    "texts merely because a CRM supports them. Configure channel "
                    "eligibility and suppression before importing records into "
                    "HubSpot, Pipedrive, or another CRM."
                ),
                (
                    "Make professional outreach more specific than asking lawyers "
                    "to send deals. Identify twelve local probate practices and "
                    "offer a sample property-status brief, a description of broker "
                    "coverage, and a reliable response standard for requested "
                    "valuation work. Ask which property problems consume their "
                    "staff's time and show how your deliverable reduces that "
                    "work without trespassing into legal representation. Track "
                    "meetings, requested follow-ups, introductions, and completed "
                    "assignments separately. Do not exchange settlement-service "
                    "referrals for things of value where RESPA section 8 applies; "
                    "also assess state brokerage and professional-conduct rules. "
                    "A cleanout contractor's invoice and an attorney's fee remain "
                    "their revenue, not yours. For inbound demand, publish a "
                    "county-specific executor property checklist, a page explaining "
                    "your brokerage service, and an accessible consultation form "
                    "that requests only necessary information. Google Business "
                    "Profile and Search Console can identify whether local "
                    "searchers find the pages and request appointments. Avoid "
                    "publishing identifiable case studies without permission. "
                    "Offer educational events through libraries or professional "
                    "groups when invited, and distinguish general process "
                    "education from a proposed engagement. Measure qualified "
                    "consultations per staff hour rather than page views alone; "
                    "a small audience with actual authority can outperform a "
                    "large audience of curious researchers."
                ),
                (
                    "Handle objections by resolving the underlying uncertainty, "
                    "not by defeating the speaker. When a representative says "
                    "their attorney handles everything, ask whether counsel "
                    "would find a concise property-status brief useful; accept "
                    "a refusal immediately. When they prefer an investor, "
                    "compare a documented cash offer with a supported brokerage "
                    "net sheet using identical carrying-cost assumptions and "
                    "clearly disclosed roles. When they fear repair costs, "
                    "present an as-is route alongside a bounded vendor scope; "
                    "never manufacture safety assurances about an uninspected "
                    "property. When relatives disagree, explain that you can "
                    "document pricing alternatives while counsel addresses "
                    "authority and disputes. After a useful conversation, "
                    "request one modest next action: a document review, an "
                    "authorized walkthrough, or a scheduled pricing meeting. "
                    "Send a written recap stating who supplies each document "
                    "and what you will deliver next. The appointment should "
                    "end with an explicit decision: signed brokerage engagement, "
                    "a defined follow-up milestone, or a respectful close. "
                    "Do not classify a conversation, free valuation, or "
                    "unsigned proposal as a win. Record objections as "
                    "structured reasons so the next month's messaging answers "
                    "actual questions rather than repeating a script that "
                    "failed the previous cohort."
                ),
            ],
            "table": {
                "caption": "Probate Outreach Cadence and Objection-to-Action Conversion Matrix",
                "headers": [
                    "Contact moment or stated prospect objection",
                    "Specific message or diagnostic response to use",
                    "Small next commitment worth requesting explicitly",
                    "Boundary that prevents avoidable relationship damage",
                ],
                "rows": [
                    [
                        "Day-one postal introduction to an appropriately verified representative",
                        "Identify the brokerage and offer a practical property-readiness checklist",
                        "Request their preferred route for receiving the optional checklist",
                        "Keep sensitive estate details off the exterior mailing envelope",
                    ],
                    [
                        "Day-ten manual call after applicable solicitation checks",
                        "Ask whether local property coordination would resolve an existing task",
                        "Offer a fifteen-minute discussion focused on one property problem",
                        "Honor refusal and suppression immediately across every connected campaign",
                    ],
                    [
                        "Day-twenty-one follow-up addressing valuation versus a principal offer",
                        "Explain that comparable-sales analysis differs from your own purchase bid",
                        "Request permission to prepare clearly labeled sale-route comparisons",
                        "Disclose principal interests and avoid claiming independent buyer-side neutrality",
                    ],
                    [
                        "Representative says their attorney already handles estate decisions",
                        "Offer a concise property brief for counsel if they want one",
                        "Request permission before making a coordinated introduction to counsel",
                        "Do not suggest replacing counsel or bypassing existing representation",
                    ],
                    [
                        "Representative fears repairs or prefers an immediate investor sale",
                        "Compare as-is brokerage and documented cash-offer nets consistently",
                        "Schedule authorized access to resolve only material pricing uncertainties",
                        "Never promise repair returns or omit additional holding expenses",
                    ],
                    [
                        "Day-forty-five closeout or unresolved family disagreement",
                        "Offer milestone-based follow-up and acknowledge counsel's dispute-management role",
                        "Record a requested review date or close the prospect respectfully",
                        "Stop repeated solicitation and avoid mediating contested legal authority",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build and verify the county queue",
                    "action": "Deduplicate estate-property matches and preserve source evidence.",
                    "detail": "Check appointment status, parcel ownership, existing representation, and source-use restrictions before any outreach task is released.",
                },
                {
                    "step": 2,
                    "title": "Assign qualification and contact eligibility",
                    "action": "Score six dimensions and separately verify channel prerequisites.",
                    "detail": "Place missing documents with a named owner; keep suppressed contacts out of every active campaign regardless of their score.",
                },
                {
                    "step": 3,
                    "title": "Deliver the readiness consultation",
                    "action": "Offer one practical next step through the permitted cadence.",
                    "detail": "Produce an evidence-backed brief, discuss sale routes and costs, and confirm what the representative wants done next.",
                },
                {
                    "step": 4,
                    "title": "Convert and instrument the mandate",
                    "action": "Obtain the broker-approved engagement and open the transaction checklist.",
                    "detail": "Record signing authority, negotiated compensation, notice or court requirements, source attribution, and the expected collection milestone.",
                },
            ],
        },
        {
            "heading": "4. Measure closed wins, collected commissions, and the economics of patience",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a bounded cohort model to plan the first "
                    "3-to-10 closed wins over 4–18 months; the following "
                    "conversion rates are test assumptions, not published market "
                    "benchmarks. Suppose 600 deduplicated estate-property matches "
                    "produce 240 verified authority candidates, of which 120 "
                    "receive an appropriate, deliverable outreach attempt. Thirty-six "
                    "hold substantive conversations, eighteen attend consultations, "
                    "ten sign mandates, and six eventually close. The "
                    "conditional stage rates are 40%, 50%, 30%, 50%, "
                    "55.6%, and 60%, respectively; raw-record-to-close yield is "
                    "1%. At unchanged performance, three closings require "
                    "about 300 initial matches and ten require about "
                    "1,000, but county supply and court capacity can "
                    "invalidate that linear scaling. Track elapsed days "
                    "between stages and retain open files in their "
                    "actual stages rather than counting them as losses "
                    "or successes prematurely. Separate no-contact outcomes "
                    "from disqualification, rejected proposals, and delayed "
                    "closings. Six closings at an illustrative $15,000 "
                    "retained commission each produce $90,000 for that "
                    "cohort when earned under the engagement; this "
                    "is neither an annual forecast nor a replacement "
                    "for the canonical scenarios. Track collection separately "
                    "from recognition so cash planning reflects actual receipts."
                ),
                (
                    "Reconcile every annual plan to retained brokerage commissions "
                    "after brokerage splits. One illustrative unit is a "
                    "$750,000 completed sale with a separately negotiated 2.5% "
                    "side commission and 80% brokerage retention: $750,000 "
                    "multiplied by 2.5% multiplied by 80% equals $15,000. "
                    "These inputs are modeling choices, not a customary "
                    "or prescribed commission rate. Eight such closings "
                    "produce the Conservative $120,000 revenue; subtract "
                    "$96,000 of total modeled operating costs to "
                    "leave $24,000 owner profit at 20%. Thirty-four "
                    "produce Base revenue of $510,000; $369,750 of "
                    "costs leaves $140,250 at 27.5%. Sixty produce "
                    "Scaled revenue of $900,000; $585,000 of costs "
                    "leaves $315,000 at 35%. The corresponding teams "
                    "remain 2 FT plus 3 C, 2 FT "
                    "plus 3 C, and 3 FT plus 4 C. "
                    "The underlying sale values are $6,000,000, "
                    "$25,500,000, and $45,000,000, respectively, and "
                    "never become operator revenue. Treat the stated "
                    "$3,000–$18,000 monthly opex range as a planning "
                    "input whose covered categories must be identified, "
                    "not automatically the complete annual cost envelope. "
                    "Payroll, contractors, marketing, and transaction costs "
                    "must reconcile to the canonical total without "
                    "double-counting amounts already removed in brokerage splits."
                ),
                (
                    "Instrument the first cohort before increasing spend. "
                    "If its acquisition work costs $12,000 across "
                    "research, mail, content, and attributable labor, "
                    "six collected closings imply $2,000 acquisition "
                    "cost per closed client. If only three "
                    "close, that rises to $4,000; spending "
                    "the same money does not preserve the "
                    "original efficiency. Include acquisition costs inside, "
                    "not in addition to, the annual scenario's "
                    "expense total. Review the funnel monthly "
                    "and the legal or title blockers weekly. "
                    "Poor authority yield suggests a record-matching "
                    "problem; strong conversations but weak mandates "
                    "suggest an unclear service proposition; signed "
                    "mandates stalled before closing suggest transaction "
                    "execution or court timing rather than insufficient "
                    "marketing. Allocate the $15,000–$100,000 startup "
                    "capital range through a dated cash schedule "
                    "that includes licensing, insurance, systems, research, "
                    "marketing, and runway. A $15,000 balance "
                    "against $3,000 monthly outflow lasts five "
                    "months before setup costs, making an "
                    "eighteen-month first closing untenable without "
                    "additional funding or lower burn. Use "
                    "docket alerts and transaction checklists to "
                    "reduce missed work, not to remove "
                    "professional judgment. Expand only after a "
                    "mature cohort demonstrates repeatable sourcing, "
                    "service delivery, and collected commission economics."
                ),
            ],
            "table": {
                "caption": "Illustrative Cohort Benchmarks with Explicit Denominators and Repair Actions",
                "headers": [
                    "Measured transition within the pilot cohort",
                    "Numerator, denominator, and conditional conversion assumption",
                    "Evidence required before advancing the CRM stage",
                    "Diagnostic response when the transition underperforms",
                ],
                "rows": [
                    [
                        "Deduplicated estate-property match becomes verified authority candidate",
                        "240 candidates from 600 initial matches equals forty percent",
                        "Appointment evidence and parcel connection survive a human review",
                        "Inspect joins, stale dockets, and misleading petitioner-only records",
                    ],
                    [
                        "Verified authority candidate receives appropriate deliverable outreach",
                        "120 delivered attempts from 240 candidates equals fifty percent",
                        "Permitted contact route and delivery record support the outreach entry",
                        "Improve address verification without bypassing suppression or channel restrictions",
                    ],
                    [
                        "Delivered outreach produces a substantive two-way service conversation",
                        "36 conversations from 120 delivered attempts equals thirty percent",
                        "Representative discusses a genuine property task and preferred next action",
                        "Test clearer service relevance rather than increasing contact pressure",
                    ],
                    [
                        "Substantive conversation becomes an attended property-readiness consultation",
                        "18 attended consultations from 36 conversations equals fifty percent",
                        "Meeting occurs and produces documented questions, evidence, and responsibilities",
                        "Reduce scheduling friction and clarify the consultation's practical deliverable",
                    ],
                    [
                        "Attended consultation converts into an authorized signed brokerage mandate",
                        "10 signed mandates from 18 consultations equals approximately 55.6 percent",
                        "Broker-approved agreement identifies authorized parties and negotiated compensation",
                        "Examine role confusion, weak pricing evidence, and competing representation",
                    ],
                    [
                        "Signed brokerage mandate closes with commission collection tracked separately",
                        "6 closings from 10 mandates equals sixty percent eventually",
                        "Closing evidence supports earned commission and accounting tracks actual receipt",
                        "Separate court delay, title blockage, cancellation, and collection lag",
                    ],
                ],
            },
        },
    ],
    "pull_quote": (
        "The best probate lead is a verified decision-maker with a solvable property "
        "problem, not a name attached to a death."
    ),
    "diagram_id": "diag-02",
    "action_checklist": [
        "Select one county and document permitted court, assessor, recorder, and municipal data access before building the estate-property queue.",
        "Implement the six-dimension qualification scorecard while keeping authority, representation, and contact eligibility as separate prerequisites.",
        "Launch the 11 mapped plays with primary-source attribution, bounded test budgets, and explicit fallbacks for inaccessible or misleading records.",
        "Configure the 45-day permitted-contact cadence, suppression controls, attorney briefing template, and executor readiness deliverable.",
        "Track a deduplicated cohort from raw matches through signed mandates, closed sales, and collected retained commissions without annualizing immature results.",
        "Reconcile annual revenue, full operating costs, team counts, and owner profit to the three canonical scenarios before expanding spend or geography.",
    ],
    "statutory_citations": [
        {
            "title": "California Business and Professions Code section 10130",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=10130.",
            "relevance": "Establishes the licensing requirement for acting as a real estate broker or salesperson in California, subject to statutory exceptions.",
        },
        {
            "title": "California Probate Code section 10501",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10501.",
            "relevance": "Identifies actions requiring court supervision under independent administration, including real-property sales when the representative has limited authority.",
        },
        {
            "title": "California Probate Code section 10580",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10580.",
            "relevance": "Addresses proposed-action notice requirements for specified independent-administration actions, subject to applicable statutory exceptions.",
        },
        {
            "title": "California Probate Code section 10308",
            "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=10308.",
            "relevance": "Governs qualifying increased offers at hearings for confirmation of real-property sales; court-sale buyer preparation must reflect the applicable procedure.",
        },
        {
            "title": "12 U.S.C. section 2607 — RESPA section 8",
            "url": "https://www.law.cornell.edu/uscode/text/12/2607",
            "relevance": "Restricts referral fees, kickbacks, and unearned fee arrangements involving settlement services for federally related mortgage loans.",
        },
        {
            "title": "47 CFR section 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": "Sets federal requirements affecting telephone solicitation, automated and prerecorded communications, consent, and do-not-call practices.",
        },
        {
            "title": "15 U.S.C. section 7704 — Commercial electronic mail requirements",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Establishes requirements for commercial email, including accurate transmission information, nondeceptive subject lines, postal identification, and opt-out handling.",
        },
    ],
}
