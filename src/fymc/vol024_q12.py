from __future__ import annotations

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-day-tax-lien-launch-kill-fix-scale",
    "question_prompt": "What is the exact Day-1-to-Day-30 execution schedule for launching tax lien investing, and what quantitative thresholds govern Kill, Fix, or Scale decisions at Day 30/60/90?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30-Day Launch Sprint & Kill / Fix / Scale Gates",
    "subtitle": "County Auction Eligibility, Certificate Bid-Down Economics, Redemption Ledgers, and Post-Tyler Recovery Controls",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #3, Tax Lien Investing, holds Rank #24 with a Money-to-Manpower "
        "Score of 62/100: capital discipline matters more than auction activity. "
        "This sprint maps four operator plays: auction screening, certificate "
        "bid-down acquisition, redemption tracking, and redeemable-deed or "
        "foreclosure disposition. One full-time owner and two contractors build "
        "a county-specific operating file, test economics, and establish recovery "
        "controls before risking principal. Annual owner profit remains $4,500 "
        "Conservative, $41,438 Base, and $99,000 Scaled; returned principal never "
        "becomes revenue. Day 30 validates readiness, Day 60 tests repeatability, "
        "and Day 90 determines controlled expansion. A $3,000 monthly operating "
        "ceiling, explicit exposure limits, and measurable Kill, Fix, or Scale "
        "thresholds prevent a thirty-day launch from becoming an uncontrolled "
        "property-recovery experiment."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$15,000",
            "context": "Annual realized interest, penalties, and disposition gains; returned principal excluded",
            "note": "30% net margin; $4,500 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$97,500",
            "context": "Annual realized interest, penalties, and disposition gains; returned principal excluded",
            "note": "42.5% net margin; $41,438 annual owner net profit, rounded; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$180,000",
            "context": "Annual realized interest, penalties, and disposition gains; returned principal excluded",
            "note": "55% net margin; $99,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Days 1–7: Charter the Pod, Ring-Fence Capital, and Select One County",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start Day 1 by separating a launch decision from an investment "
                    "return promise. Candidate #3 carries a $100,000–$1,500,000 startup "
                    "capital range and a six-to-thirty-six-month time to first deal; "
                    "this thirty-day sprint establishes capability rather than assuming "
                    "an auction award or redemption. Map the work into four plays: "
                    "auction screening, certificate bid-down acquisition, redemption "
                    "tracking, and redeemable-deed or foreclosure disposition. These are "
                    "distinct workflows, not interchangeable statutory products. Assign "
                    "the full-time owner capital allocation, county communication, bidding, "
                    "and ledger signoff. Contractor one performs parcel, title, and "
                    "physical-access research; contractor two is locally qualified "
                    "counsel responsible for procedure review and recovery estimates. "
                    "Use contractors for bounded work orders, not fictional full-time "
                    "coverage. Reserve forty owner hours and eight hours per contractor "
                    "each week, with any additional hours requiring a revised budget. "
                    "Day 2 produces a signed capital charter, task ownership sheet, and "
                    "separate account structure. Day 3 produces a county selection memo "
                    "comparing auction format, redemption mechanics, notice duties, and "
                    "available records. Begin with one certificate jurisdiction; keep "
                    "redeemable deeds in a separate research lane until their distinct "
                    "vesting and redemption rules are documented. No parcel advances "
                    "because its advertised rate looks attractive."
                ),
                (
                    "For a concrete pilot, assume $100,000 of dedicated capital, not "
                    "borrowed household liquidity. Ring-fence $25,000 as reserve and "
                    "limit the first authorized batch to $20,000 of all-in committed "
                    "exposure. All-in exposure includes certificate principal, nonrefundable "
                    "fees, committed subsequent taxes, and asset-specific recovery costs. "
                    "Cap each parcel at $5,000 and each county at $20,000 throughout "
                    "the pilot. Preserve the remaining capital for later reviewed "
                    "batches; auction deposits count as restricted cash, not expenses "
                    "unless forfeited. Set cumulative operating-cash ceilings of $3,000 "
                    "at Day 30, $6,000 at Day 60, and $9,000 at Day 90. "
                    "Allocate the first month's ceiling to $1,200 counsel, $800 parcel "
                    "and title research, $300 records and software, $200 travel, and "
                    "$500 contingency. Obtain fixed-scope quotes on Day 4; if local "
                    "pricing exceeds these allowances, reduce the parcel batch rather "
                    "than remove legal review. The ceiling excludes invested principal "
                    "but includes external services and overhead. Owner labor still "
                    "consumes capacity even when no salary leaves the account. Keep "
                    "the $25,000 reserve floor after subtracting all commitments and "
                    "the next ninety days of planned operating spending. That prevents "
                    "an apparently affordable bid from consuming the recovery runway."
                ),
                (
                    "Days 5–7 convert public records into a reproducible underwriting "
                    "dataset. Record the parcel identifier, legal description, auction "
                    "identifier, owner of record, tax years, assessed classification, "
                    "mapped access, delinquent balance, and source retrieval date. "
                    "Download the county's bidder packet and results history, then "
                    "retain immutable copies with SHA-256 hashes generated by Python "
                    "hashlib. Use county GIS for boundaries, the recorder for recorded "
                    "instruments, and FEMA's Map Service Center for flood exposure; "
                    "none substitutes for a title examination or site-specific access "
                    "assessment. Assemble thirty unique parcels and advance at least "
                    "twelve to complete review. Mark apparent duplicates by legal "
                    "description as well as parcel number because reassessments and "
                    "splits can change identifiers. Contractor one checks whether a "
                    "tiny strip, drainage tract, contaminated use, or inaccessible lot "
                    "explains the delinquency. Counsel distinguishes certificate "
                    "ownership from possession and documents which later proceeding "
                    "could create marketable title. A suspected bankruptcy, unresolved "
                    "ownership mismatch, or missing redemption rule blocks bidding "
                    "immediately. Day 7 ends with an evidence-backed shortlist, not "
                    "a purchase target. If fewer than twelve parcels survive, keep "
                    "screening within the same spending ceiling instead of lowering "
                    "the evidence standard."
                ),
            ],
            "table": {
                "caption": "Week One Daily Deliverables and Named Accountability",
                "headers": [
                    "Daily execution assignment and accountable operator",
                    "Required artifact before the next assignment",
                    "Evidence source and practical verification method",
                    "Stop condition requiring a documented correction",
                ],
                "rows": [
                    [
                        "Day 1: Owner assigns four separate operator plays",
                        "Signed responsibility map with weekly capacity allocations",
                        "Owner and both contractors acknowledge scoped deliverables",
                        "Unassigned bidding or recovery responsibility blocks progression",
                    ],
                    [
                        "Day 2: Owner segregates reserve and pilot funds",
                        "Capital charter limits initial committed exposure explicitly",
                        "Bank balances reconcile against deposits and commitments",
                        "Reserve below twenty-five thousand dollars stops deployment",
                    ],
                    [
                        "Day 3: Counsel compares county auction mechanics",
                        "One county memo identifies certificate-specific operating requirements",
                        "Official statutes and current bidder packet agree",
                        "Conflicting redemption instructions require written county clarification",
                    ],
                    [
                        "Day 4: Owner obtains bounded contractor quotations",
                        "Signed work orders fit the operating ceiling",
                        "Quoted hours and deliverables match pod capacity",
                        "Unpriced recovery work blocks approval of affected parcels",
                    ],
                    [
                        "Day 5: Research contractor imports thirty unique parcels",
                        "Deduplicated register preserves parcel and legal-description identifiers",
                        "County list reconciles against assessor parcel records",
                        "Identifier mismatches remain excluded until records reconcile",
                    ],
                    [
                        "Day 6: Research contractor screens access and land use",
                        "Twelve review candidates carry documented physical-risk findings",
                        "County GIS and recorder evidence support findings",
                        "Unresolved access or contamination concerns remove candidates",
                    ],
                    [
                        "Day 7: Owner freezes the initial evidence packet",
                        "Versioned shortlist includes sources and retrieval dates",
                        "File hashes preserve the reviewed source versions",
                        "Incomplete evidence returns parcels to research status",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Conditions Before Any Auction Deposit",
                "body": (
                    "A deposit can create restricted cash and binding obligations. "
                    "Complete all four checks before funding registration."
                ),
                "items": [
                    "Confirm bidder identity, entity eligibility, deposit deadline, settlement deadline, and default consequences directly against the current county packet.",
                    "Have local counsel document the specific instrument, redemption calculation, expiration rules, notice responsibilities, and permitted recovery route.",
                    "Reconcile unrestricted cash after deposits, committed taxes, recovery allowances, and ninety-day spending against the $25,000 reserve floor.",
                    "Require matched parcel identifiers, completed title review, verified bid ceilings, and zero unresolved bankruptcy or ownership issues for every proposed bid.",
                ],
            },
        },
        {
            "heading": "2. Days 8–14: Price the Instrument, Stress Redemption, and Rehearse Bidding",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Day 8 builds the auction calculator from the selected county's "
                    "actual mechanism: interest-rate bid-down, premium bidding, or "
                    "another specified allocation method. Never assume an advertised "
                    "maximum is the rate earned. Day 9 translates redemption rules "
                    "into dated cash flows, including rounding, minimum charges, "
                    "noninterest-bearing premiums, reimbursable expenses, and payment "
                    "timing where applicable. Florida Statutes sections 197.432 and "
                    "197.472 illustrate why sale mechanics and redemption computation "
                    "must be read together; a generic annual-rate spreadsheet cannot "
                    "replace those rules. For a deliberately simplified certificate "
                    "example, invest $4,000 principal and incur $400 of upfront, "
                    "nonrecoverable costs. Redemption after twenty-four months at twelve "
                    "percent simple annual interest yields $960 of interest and $560 "
                    "after those costs. Dividing $560 by $4,400 and two years gives "
                    "a 6.36% simple annualized planning yield. At fourteen percent, "
                    "interest becomes $1,120 and the same calculation gives 8.18%. "
                    "These are screening calculations, not internal rates of return "
                    "or promises about a particular jurisdiction. Under this pilot's "
                    "eight-percent stressed hurdle, the first bid fails and the second "
                    "barely passes. Any additional unbudgeted cost can reverse that "
                    "decision, so contractor quotations belong inside the calculator "
                    "before the auction starts."
                ),
                (
                    "Day 10 tests early redemption, twenty-four-month redemption, and "
                    "a thirty-six-month unresolved position with no assumed interest "
                    "receipt. The last case is a liquidity test, not an invented "
                    "right to collect forever. Model statutory accrual limits and "
                    "expiration dates separately. Day 11 runs a recovery waterfall "
                    "using conservative property proceeds, sale costs, taxes, title "
                    "work, notice expenses, and amounts legally payable to other "
                    "parties. For coverage screening, require independently supported "
                    "net property proceeds before satisfying this position to exceed "
                    "three times projected all-in exposure. Coverage between two and "
                    "three times requires correction or a smaller bid; below two "
                    "times kills the parcel. Coverage is a loss-severity proxy, not "
                    "a right to retain the entire property surplus. Tyler v. "
                    "Hennepin County, 598 U.S. 631 (2023), makes excess-value assumptions "
                    "especially dangerous in tax foreclosure analysis. Counsel must "
                    "map the governing distribution procedure rather than credit "
                    "the investor with every dollar of equity. Bankruptcy protection "
                    "under 11 U.S.C. section 362 can interrupt collection and "
                    "enforcement; a search hit triggers case-specific review rather "
                    "than an automated notice or filing. Record the worst-case "
                    "additional cash demand and whether the reserve can actually "
                    "fund it without selling another position."
                ),
                (
                    "Days 12–14 convert the model into an executable bidding discipline. "
                    "Run twenty dry-run bids spanning early redemption, reduced rates, "
                    "premium erosion, parcel withdrawal, competing bids, settlement "
                    "failure, and duplicate records. Require all twenty expected "
                    "outputs to reconcile, with currency differences no greater than "
                    "one cent against independently calculated fixtures. Keep an "
                    "approved maximum principal and a minimum acceptable rate on "
                    "each bid ticket; premium auctions need an explicit maximum "
                    "premium instead. The owner enters bids while the research "
                    "contractor checks the ticket and resulting exposure. Counsel "
                    "does not become an auction clerk; their limited hours belong "
                    "to exceptions and procedure. Use the county-designated portal, "
                    "whether Realauction, Grant Street Group, or another provider, "
                    "only under the county's published bidder rules. Do not scrape "
                    "authenticated areas or automate submission without permission. "
                    "A spreadsheet with protected formulas and a second-person "
                    "readback can outperform fragile browser automation at this "
                    "scale. Day 14 ends with twelve fully reviewed parcels, at "
                    "least three economically qualified candidates, and a locked "
                    "bid file. If market bidding pushes every candidate below "
                    "the hurdle, record a valid no-bid result. Winning nothing "
                    "is preferable to purchasing a rate that cannot cover "
                    "the actual work."
                ),
            ],
            "table": {
                "caption": "Week Two Bid-Down Economics and Recovery Stress Tests",
                "headers": [
                    "Daily modeling task and responsible pod member",
                    "Required calculation or documented operational output",
                    "Quantitative acceptance test before bid file release",
                    "Failure response preserving capital and evidence quality",
                ],
                "rows": [
                    [
                        "Day 8: Owner encodes the actual auction mechanism",
                        "Separate rate ceilings from premium bid limits",
                        "Every candidate uses its county-specific calculation method",
                        "Reject generic yield estimates lacking instrument-specific mechanics",
                    ],
                    [
                        "Day 9: Counsel reviews redemption computation assumptions",
                        "Dated cash flows identify interest and recoverable expenses",
                        "All statutory inputs link to primary authority",
                        "Pause affected instruments until interpretations are resolved",
                    ],
                    [
                        "Day 10: Owner stresses three redemption timing cases",
                        "Early, delayed, and unresolved cases show cash demands",
                        "Twenty-four-month planning yield reaches eight percent minimum",
                        "Reduce bids or remove economically weak candidates",
                    ],
                    [
                        "Day 11: Research contractor estimates conservative recovery coverage",
                        "Net property proceeds exclude unsupported surplus capture",
                        "Coverage reaches three times projected all-in exposure",
                        "Two-to-three-times coverage requires correction before any bidding",
                    ],
                    [
                        "Day 12: Owner runs twenty calculator test fixtures",
                        "Independent calculations cover rate and premium failure modes",
                        "Twenty outputs reconcile within one cent each",
                        "Repair formulas and repeat the complete test suite",
                    ],
                    [
                        "Day 13: Owner rehearses bidding with contractor readback",
                        "Bid tickets preserve rate floors and exposure ceilings",
                        "Zero simulated bids exceed authorized parcel limits",
                        "Disable submission until ticket checks operate reliably",
                    ],
                    [
                        "Day 14: Owner locks the reviewed auction file",
                        "Twelve complete files include three qualified candidates",
                        "Each proposed bid passes every hard-stop condition",
                        "Keep capital idle when qualifying inventory disappears",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Practitioner Tactics That Protect the Bid Before the Bid",
                "body": (
                    "Protect the economics at the parcel level. County averages "
                    "and advertised rates conceal the work that consumes returns."
                ),
                "items": [
                    "Compare the auction legal description against the recorder, not just the assessor address; vacant strips and split parcels can share misleading location labels.",
                    "Keep the latest withdrawal list beside the bid ticket and recheck immediately before submission; a redeemed or withdrawn item should never survive on a stale shortlist.",
                    "Ask the county which redemption amounts are remitted to certificate holders and which fees remain with the county; model the actual holder receipt.",
                    "Record the losing rate or premium on qualified no-bids; repeated market-clearing failures reveal a county-selection problem before capital is trapped.",
                ],
            },
        },
        {
            "heading": "3. Days 15–21: Operate the Ledger and Rehearse the Recovery Handoff",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Day 15 registers the approved bidder and verifies funding "
                    "instructions through an independently obtained county contact. "
                    "An emailed account change never authorizes a transfer by itself. "
                    "If the auction calendar falls outside the sprint, complete "
                    "registration research and a sandbox rehearsal without manufacturing "
                    "a purchase deadline. Day 16 reconciles deposits, restricted cash, "
                    "available cash, and commitments. Day 17 conducts the permitted "
                    "auction session or repeats the dry run against published "
                    "historical results. The owner alone releases bids, and every "
                    "award must match a previously reviewed ticket. Day 18 verifies "
                    "the certificate or deed record, payment receipt, ownership "
                    "registration, parcel identity, and applicable start dates. A "
                    "bid acknowledgment is not sufficient evidence of the acquired "
                    "interest. Keep original county receipts alongside a normalized "
                    "CSV register maintained with Python csv and decimal; SQLite "
                    "can hold the transaction history without introducing a paid "
                    "platform. Record who entered and who reviewed each change. "
                    "For the three-person pod, the research contractor performs "
                    "the second check while counsel handles legal exceptions. "
                    "If settlement instructions cannot be authenticated or an "
                    "award differs from the approved parcel, freeze additional "
                    "activity and contact the county promptly. Do not quietly "
                    "substitute a nearby parcel to preserve the appearance "
                    "of sprint completion."
                ),
                (
                    "Day 19 builds the redemption tracker around events rather "
                    "than optimistic accruals. Store acquisition date, statutory "
                    "redemption dates, certificate expiration, subsequent-tax choices, "
                    "notice prerequisites, and recovery eligibility separately. Use "
                    "thirty-day and seven-day internal reminders where the actual "
                    "procedure permits, but calendar statutory service and filing "
                    "deadlines exactly; internal reminders never extend them. Test "
                    "five events: full redemption, partial county remittance, incorrect "
                    "parcel allocation, upcoming expiration, and a bankruptcy flag. "
                    "Every event must route to an owner and preserve source "
                    "evidence. Day 20 reconciles a mock $4,600 receipt composed "
                    "of $4,000 returned principal and $600 realized interest. "
                    "The operating dashboard reports $600 revenue, not $4,600, "
                    "while the principal ledger reduces the asset balance by "
                    "$4,000. Penalties count only when legally payable to this "
                    "holder and realized under the dashboard's stated basis. "
                    "Disposition revenue is the realized gain after the relevant "
                    "asset basis, not gross property sale proceeds; separately "
                    "tracked expenses must not be deducted twice. Maintain "
                    "unrealized accruals in a distinct forecast column. A "
                    "county redemption notice without cleared funds updates "
                    "status but does not create spendable cash or prove "
                    "the annual scorecard economics."
                ),
                (
                    "Day 21 completes the fourth play's recovery handoff without "
                    "initiating premature enforcement. A certificate position and "
                    "a Texas redeemable deed require different instructions: "
                    "Texas Tax Code section 34.21 describes redemption rights "
                    "and redemption amounts, not a universal certificate coupon. "
                    "Counsel produces separate decision trees identifying the "
                    "eligible initiating party, necessary searches, parties requiring "
                    "notice, waiting periods, service evidence, and distribution "
                    "rules. Jones v. Flowers, 547 U.S. 220 (2006), illustrates "
                    "why returned notice can require additional reasonable "
                    "steps when practicable; a mailing log alone may not "
                    "finish the task. Federal interests can add requirements "
                    "under 26 U.S.C. section 7425, so flag federal liens "
                    "for specific review rather than assuming every tax sale "
                    "eliminates them. Obtain a capped estimate for the next "
                    "procedural stage and a separate estimate for contested "
                    "work. Do not initiate owner contact, possession activity, "
                    "or foreclosure through an unreviewed automated sequence. "
                    "For every held position, name the next lawful action, "
                    "its earliest permissible date, its cost, and its evidence "
                    "requirement. The sprint succeeds when the pod can maintain "
                    "a dormant position accurately for months, not when it "
                    "can generate aggressive letters in minutes. A clean "
                    "handoff preserves both capital and procedural options."
                ),
            ],
            "table": {
                "caption": "Week Three Settlement, Redemption Tracking, and Recovery Handoff",
                "headers": [
                    "Daily operational assignment and accountable pod member",
                    "Artifact retained in the position evidence folder",
                    "Verification requirement before marking the assignment complete",
                    "Exception handling that prevents premature next actions",
                ],
                "rows": [
                    [
                        "Day 15: Owner verifies registration and payment instructions",
                        "Current bidder registration and authenticated funding details",
                        "Independent county contact confirms destination and deadlines",
                        "Changed transfer details require fresh independent verification",
                    ],
                    [
                        "Day 16: Owner reconciles restricted and available cash",
                        "Deposit ledger distinguishes restricted cash from expenses",
                        "Bank balance equals categorized cash and commitments",
                        "Unexplained differences suspend deposits and new bidding",
                    ],
                    [
                        "Day 17: Owner conducts auction or documented rehearsal",
                        "Bid log records authorized limits and actual outcomes",
                        "Every submitted bid matches a reviewed ticket",
                        "Out-of-range market pricing produces a documented no-bid",
                    ],
                    [
                        "Day 18: Contractor verifies acquired instrument records",
                        "County receipt and registered interest match identifiers",
                        "Every award reconciles to payment and ownership records",
                        "Disputed awards remain blocked from subsequent investment",
                    ],
                    [
                        "Day 19: Owner tests five redemption tracking events",
                        "Event register includes deadlines and accountable owners",
                        "Five tested events route correctly without omissions",
                        "Missed reminders trigger calendar repair and retesting",
                    ],
                    [
                        "Day 20: Owner reconciles principal and realized receipts",
                        "Mock remittance separates returned principal from interest",
                        "Four-thousand-dollar principal never enters recognized operating revenue",
                        "Classification errors require ledger correction before reporting",
                    ],
                    [
                        "Day 21: Counsel delivers instrument-specific recovery instructions",
                        "Written handoff specifies lawful dates and notice duties",
                        "Every held position has a costed next action",
                        "Missing procedure or service evidence blocks enforcement",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Capture the originating county event",
                    "action": "Save the official notice, remittance detail, or position update.",
                    "detail": "Attach parcel and instrument identifiers, retrieval date, original file, and the responsible owner before changing the register.",
                },
                {
                    "step": 2,
                    "title": "Classify cash and procedural consequences",
                    "action": "Separate principal, realized holder income, reimbursed costs, and unresolved differences.",
                    "detail": "Update deadlines independently from cash recognition; a status notice does not establish cleared funds or authority to enforce.",
                },
                {
                    "step": 3,
                    "title": "Obtain the appropriate second review",
                    "action": "Route arithmetic to the research contractor and legal exceptions to counsel.",
                    "detail": "Require one-cent cash reconciliation and documented resolution of bankruptcy, notice, ownership, and distribution questions.",
                },
                {
                    "step": 4,
                    "title": "Close the event with an auditable next action",
                    "action": "Record the reviewer, supporting evidence, next deadline, and remaining commitment.",
                    "detail": "Release capital only after cleared receipts reconcile; preserve the prior register state and retain unresolved exceptions in the owner queue.",
                },
            ],
        },
        {
            "heading": "4. Days 22–30 and Reviews at 60/90: Kill Defects, Fix Friction, Scale Evidence",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Day 22 audits every reviewed parcel against its original "
                    "sources and closes duplicate identifiers. Day 23 reruns "
                    "the twenty calculator fixtures after any changes. Day 24 "
                    "rechecks county withdrawals, remittance status, and bankruptcy "
                    "exceptions. Day 25 obtains counsel's written confirmation "
                    "that every live deadline and contemplated next action "
                    "matches the selected instrument. Day 26 reconciles bank "
                    "cash, restricted deposits, principal, realized receipts, and "
                    "unpaid commitments. Day 27 measures throughput using completed "
                    "files rather than downloaded records: target no more than "
                    "ninety owner minutes and $150 of repeatable external "
                    "screening cost per fully reviewed parcel. Allocate recurring "
                    "research costs across all completed files, including rejected "
                    "ones; identify initial procedure-design costs separately. "
                    "Day 28 tests the thirty-six-month no-receipt case and "
                    "revalidates the reserve floor. Day 29 assembles a decision "
                    "packet containing the shortlist, no-bid log, cash bridge, "
                    "exception register, and next sixty-day calendar. Day 30 "
                    "holds a forty-five-minute review with both contractors. "
                    "Record Kill, Fix, or Scale for the operating lane "
                    "and separately for each parcel. No completed auction "
                    "is required when the calendar prevents one. A complete "
                    "rehearsal can justify maintaining readiness, but cannot "
                    "establish actual recovery speed or realized investment yield."
                ),
                (
                    "Apply decisions in order: any Kill condition overrides "
                    "all positive indicators; Scale requires every listed "
                    "prerequisite; everything else becomes Fix with an owner "
                    "and a fourteen-day correction deadline. Kill means stop "
                    "new commitments in the affected lane, preserve records, "
                    "and maintain existing positions lawfully. It does not "
                    "mean abandon notices, surrender value, or force an "
                    "immediate sale. Hard stops include an unresolvable legal "
                    "right, coverage below two times, an unauthorized bid, "
                    "or unrestricted reserves below $25,000 after commitments "
                    "and planned spending. Operating-cash ceilings are $3,000, "
                    "$6,000, and $9,000 at the three reviews; unauthorized "
                    "overspending pauses new deployment until a corrected "
                    "charter is expressly adopted. Day 30 Scale authorizes "
                    "only the initial $20,000 aggregate exposure ceiling. "
                    "Day 60 can raise it to $35,000, and Day 90 "
                    "to $50,000, provided evidence and capacity tests pass. "
                    "The $20,000 county concentration cap remains, so higher "
                    "aggregate deployment requires a separately reviewed second "
                    "or third county rather than silent concentration. All "
                    "limits include existing holdings and commitments, not "
                    "just the next auction's bids. If suitable auctions "
                    "or qualified inventory are absent, retain the current "
                    "cap and use Fix to continue bounded research without "
                    "forcing a purchase."
                ),
                (
                    "Keep the scorecard separate from this pilot's milestone "
                    "dashboard. Conservative annual revenue is $15,000 with "
                    "$10,500 implied costs and $4,500 owner profit. Base "
                    "revenue is $97,500 with $56,062.50 implied costs and "
                    "$41,437.50 profit, displayed as $41,438 at a 42.5% "
                    "margin. Scaled revenue is $180,000 with $81,000 implied "
                    "costs and $99,000 profit at 55%. These are annual "
                    "realized-interest, penalty, and disposition-gain cases; neither "
                    "principal recovery nor auction spending increases revenue. "
                    "The $3,000 monthly sprint ceiling is a spending "
                    "authorization, not a forecast of perpetual costs. "
                    "Spending that amount every month would exceed the "
                    "Conservative case's entire annual cost allowance, so "
                    "Day 90 must approve a reconciled twelve-month cost "
                    "plan before continuation. Keep the launch pod at "
                    "one full-time owner plus two contractors. The Scaled "
                    "scorecard assumes two full-time people plus three "
                    "contractors and cannot be claimed merely because "
                    "the pilot passes Day 90. Add capacity only after "
                    "a funded workload plan supports it. Treat no-redemption "
                    "positions as unresolved evidence, not failures by "
                    "default: the stated six-to-thirty-six-month deal horizon "
                    "makes ninety-day profit extrapolation unreliable. Scale "
                    "reviewed deployment capacity first; claim economic "
                    "validation only when realized cohort results actually "
                    "support the proposed expansion."
                ),
            ],
            "table": {
                "caption": "Quantitative Day 30, Day 60, and Day 90 Decision Matrix",
                "headers": [
                    "Review date and decision for the operating lane",
                    "Quantitative trigger or minimum evidence requirement",
                    "Capital action and concentration control after review",
                    "Required corrective artifact or evidence of readiness",
                ],
                "rows": [
                    [
                        "Day 30 Kill: Stop new commitments immediately",
                        "Reserve below $25,000 or spending above $3,000",
                        "Freeze acquisitions while preserving existing servicing duties",
                        "Owner documents cash restoration and corrected commitments",
                    ],
                    [
                        "Day 30 Fix: Repair incomplete readiness before bidding",
                        "Fewer than twelve reviewed files or three qualifiers",
                        "Keep exposure unchanged and spend within existing ceiling",
                        "Close gaps within fourteen days without weakening criteria",
                    ],
                    [
                        "Day 30 Scale: Authorize the bounded initial pilot",
                        "Twelve files, three qualifiers, twenty passing calculator tests",
                        "Limit aggregate exposure to $20,000 across approved tickets",
                        "All preflight checks pass with zero unresolved exceptions",
                    ],
                    [
                        "Day 60 Kill: Stop an unsafe or overrun lane",
                        "Reserve breach, unauthorized bid, or spending above $6,000",
                        "Suspend additional commitments without abandoning current positions",
                        "Document incident causes and preserve every live deadline",
                    ],
                    [
                        "Day 60 Fix: Reduce friction before enlarging exposure",
                        "Fewer than twenty-four files or four new qualifiers",
                        "Retain prior cap and complete fourteen-day remediation",
                        "Repeatable costs above $150 per file require redesign",
                    ],
                    [
                        "Day 60 Scale: Expand only independently reviewed capacity",
                        "Twenty-four files, four new qualifiers, zero cash breaks",
                        "Raise aggregate cap to $35,000 across approved counties",
                        "Last twelve files average at most ninety owner minutes",
                    ],
                    [
                        "Day 90 Kill: Halt expansion with unresolved capital threats",
                        "Reserve breach, unresolvable rights, or spending above $9,000",
                        "Stop new capital commitments and protect existing claims",
                        "Counsel and owner document funded position-maintenance actions",
                    ],
                    [
                        "Day 90 Fix: Hold exposure until economics are supportable",
                        "Fewer than thirty-six files or five new qualifiers",
                        "Maintain prior exposure cap without automatic budget increases",
                        "Missing twelve-month cost bridge blocks further deployment growth",
                    ],
                    [
                        "Day 90 Scale: Increase deployment without claiming realized validation",
                        "Thirty-six files, five new qualifiers, zero unresolved exceptions",
                        "Raise aggregate cap to $50,000 with county limits intact",
                        "Five event tests pass and annual costs reconcile",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Scale the evidence before the exposure, and never count returned principal as proof of profit.",
    "diagram_id": "diag-08",
    "action_checklist": [
        "By Day 2, sign the $100,000 pilot charter with a $25,000 reserve floor, $5,000 parcel limit, and $20,000 initial aggregate exposure ceiling.",
        "By Day 7, select one certificate county, retain current primary sources, and screen thirty unique parcels for twelve complete reviews.",
        "By Day 14, reconcile twenty bid-calculator fixtures and approve at least three candidates meeting the eight-percent stressed planning hurdle and three-times coverage requirement.",
        "By Day 21, test five redemption events, reconcile principal separately from realized income, and obtain counsel's costed recovery instructions for each held instrument.",
        "By Day 30, complete the daily audit sequence and document the lane-level decision, parcel-level exceptions, cash position, and fourteen-day correction assignments.",
        "At Days 60 and 90, apply every hard stop first, retain parcel and county limits, and reconcile the twelve-month cost plan before authorizing expanded deployment.",
    ],
    "statutory_citations": [
        {
            "title": "Florida Statutes § 197.432 — Sale of tax certificates",
            "url": "https://www.flsenate.gov/Laws/Statutes/2025/197.432",
            "relevance": "Establishes Florida certificate sale mechanics that must be reflected in the auction model rather than replaced with advertised maximum-rate assumptions.",
        },
        {
            "title": "Florida Statutes § 197.472 — Redemption of tax certificates",
            "url": "https://www.flsenate.gov/Laws/Statutes/2025/197.472",
            "relevance": "Provides Florida redemption computation and payment rules used to distinguish holder receipts, principal recovery, and applicable charges.",
        },
        {
            "title": "Texas Tax Code § 34.21 — Right of redemption",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm#34.21",
            "relevance": "Defines Texas tax-sale redemption rights and amounts, demonstrating why redeemable deeds need a separate model from tax-lien certificates.",
        },
        {
            "title": "11 U.S.C. § 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "Requires case-specific review of bankruptcy stays and applicable exceptions before collection, enforcement, or recovery actions proceed.",
        },
        {
            "title": "26 U.S.C. § 7425 — Discharge of liens",
            "url": "https://www.law.cornell.edu/uscode/text/26/7425",
            "relevance": "Addresses federal lien treatment, notice, and federal redemption issues that can affect a tax-sale recovery analysis.",
        },
        {
            "title": "Tyler v. Hennepin County, 598 U.S. 631 (2023)",
            "url": "https://www.supremecourt.gov/opinions/22pdf/22-166_8n59.pdf",
            "relevance": "Rejects government retention of surplus value under the challenged tax-foreclosure arrangement and supports explicit review of excess-value distribution assumptions.",
        },
        {
            "title": "Jones v. Flowers, 547 U.S. 220 (2006)",
            "url": "https://www.law.cornell.edu/supct/html/04-1477.ZO.html",
            "relevance": "Explains the need for additional reasonable notice steps when mailed tax-sale notice is returned unclaimed and further practicable steps are available.",
        },
    ],
}
