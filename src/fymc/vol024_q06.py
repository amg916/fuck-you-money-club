from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-first-tax-lien-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in tax lien investing, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (3–10 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "County Auction Signals, Certificate Assignments, Texas Redemption Premiums, and Post-Tyler Surplus Controls",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #3, Tax Lien Investing, ranks #24 with a Money-to-Manpower Score of "
        "81/100. Source executable claims rather than impressive advertised rates. This "
        "chapter maps four operator plays: primary certificate auctions, county-held "
        "certificate purchases, documented secondary assignments, and redeemable-deed "
        "auctions. A one-full-time, two-contractor pod turns county records, auction "
        "results, title exceptions, and seller liquidity signals into priced decisions "
        "and the first three to ten documented acquisitions over a 6–36-month operating "
        "horizon. Conservative, Base, and Scaled annual owner profits are $4,500, "
        "$41,438, and $99,000 respectively; returned principal never becomes revenue. "
        "Use jurisdiction-specific eligibility checks, redemption timing, bid ceilings, "
        "and surplus-preservation procedures to protect those economics. Acquisition "
        "wins and realized cash wins remain separate scoreboards."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$15,000",
            "context": "Annual realized interest, penalties and disposition gains; returned principal excluded",
            "note": "30% margin; $4,500 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$97,500",
            "context": "Annual realized interest, penalties and disposition gains; returned principal excluded",
            "note": "42.5% margin; $41,438 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$180,000",
            "context": "Annual realized interest, penalties and disposition gains; returned principal excluded",
            "note": "55% margin; $99,000 annual owner net profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Map four acquisition plays onto authoritative county signals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with two jurisdictions, not a national delinquency spreadsheet. "
                    "For this chapter, the four mapped operator plays are primary certificate "
                    "auctions, county-held certificate purchases, secondary certificate assignments, "
                    "and redeemable-deed auctions. These are acquisition lanes, not interchangeable "
                    "claims on property. A Florida certificate generally represents a tax lien; "
                    "a Texas tax-sale deed carries a different ownership and redemption structure. "
                    "Build a jurisdiction card from the tax collector or treasurer, recorder, "
                    "assessor, court clerk, and current sale instructions. Capture registration "
                    "deadlines, deposit mechanics, eligible bidder restrictions, bidding method, "
                    "assignment procedure, redemption calculation, and the next enforceable action "
                    "date. Florida Statutes section 197.432 governs certificate sales; section "
                    "197.502 addresses applications for tax deeds. Do not describe buying the "
                    "certificate as buying the house. The one full-time operator owns jurisdiction "
                    "selection and bid authority. Contractor one maintains records and parcel "
                    "joins; contractor two supplies scoped title and local-procedure expertise, "
                    "using appropriately licensed counsel where necessary. The pod should reject "
                    "a county when its records cannot support repeatable identity matching or "
                    "its required follow-through exceeds available cash and contractor capacity. "
                    "That rejection is productive sourcing: it prevents cheap inventory from "
                    "becoming an expensive servicing obligation."
                ),
                (
                    "Mine signals that change executability rather than signals that merely "
                    "advertise distress. Download current sale lists and prior auction results "
                    "from the official county source; retain retrieval dates and the original "
                    "files. Where a county directs bidders to RealAuction or another platform, "
                    "verify that connection through the county website before registering or "
                    "funding anything. Join certificate numbers to parcel identifiers, then "
                    "reconcile assessor descriptions against recorded legal descriptions. Repeated "
                    "sale appearances, county-held inventory, assignment availability, falling bid "
                    "rates, and clustered redemptions each answer different questions. Repeated "
                    "appearances may indicate title trouble rather than overlooked value. Falling "
                    "rates indicate competitive capital, while a documented seller winding down "
                    "a certificate portfolio may create a negotiable assignment price. Use QGIS "
                    "to flag landlocked strips, drainage parcels, and access discontinuities; "
                    "use FEMA maps and local zoning records to identify investigation needs, "
                    "not to certify buildability. Search PACER or the relevant court record "
                    "for bankruptcy issues before advancing enforcement assumptions. Store source "
                    "links, document dates, and unresolved exceptions in SQLite or a controlled "
                    "spreadsheet. Auction screening should surface records for judgment, not "
                    "silently transform a weak parcel match into a purchase recommendation."
                ),
                (
                    "Demand mining means measuring who competes for claims, who needs liquidity, "
                    "and who could eventually buy an asset if lawful enforcement produces "
                    "marketable ownership. Examine published auction results for bid-rate compression "
                    "and recurring purchasers, but do not assume purchaser names reveal available "
                    "capital or willingness to sell. Build an opt-in list of certificate holders "
                    "who actually offer assignments, local title professionals familiar with tax "
                    "sales, and property brokers serving the relevant parcel type. Ask brokers "
                    "for closed comparable sales and realistic marketing periods, not optimistic "
                    "listing prices. For county-held inventory, investigate why a claim remained "
                    "available and which statutory purchase terms apply; unsold does not mean "
                    "discounted. For redeemable deeds, record occupancy, possession restrictions, "
                    "redemption classes, and the cash needed while ownership remains defeasible. "
                    "Texas Tax Code section 34.21 distinguishes redemption periods and premiums "
                    "by property category and timing. A premium is not a universal annual "
                    "yield. Set the first three-to-ten acquisition objective within the stated "
                    "6–36-month horizon, while maintaining a separate calendar for redemptions "
                    "and dispositions. Winning a bid can occur earlier than that horizon; "
                    "recovering deployable cash may take substantially longer than the auction "
                    "screen makes apparent."
                ),
            ],
            "table": {
                "caption": "Four-Play Source Map and Official-Record Signal Tests",
                "headers": [
                    "Source or acquisition lane",
                    "Signal worth investigating",
                    "Required corroborating evidence",
                    "Pod action and rejection condition",
                ],
                "rows": [
                    [
                        "Primary certificate auctions listed by the county collector",
                        "Acceptable bid rates persist across comparable prior sales",
                        "Current sale rules and parcel-specific certificate records agree",
                        "Operator sets maximum capital exposure before registering bids",
                    ],
                    [
                        "County-held certificates offered through official purchase procedures",
                        "Available inventory fits researched parcel and servicing criteria",
                        "County confirms availability, purchase terms, and assignment mechanics",
                        "Records contractor rejects stale lists without current confirmation",
                    ],
                    [
                        "Secondary assignments offered by documented existing certificate holders",
                        "Seller requests liquidity and provides a verifiable inventory",
                        "Recorded holder identity matches transferable certificate ownership rights",
                        "Operator negotiates only after independently confirming transfer requirements",
                    ],
                    [
                        "Redeemable-deed auctions administered under applicable state procedures",
                        "Purchase basis survives redemption and delayed disposition scenarios",
                        "Recorded documents establish property category and redemption timing",
                        "Specialist rejects cases requiring unsupported possession or title assumptions",
                    ],
                    [
                        "Official auction results and historical certificate redemption records",
                        "Competitive rates and cash recovery patterns differ materially",
                        "Cohorts separate redeemed claims from still-outstanding certificate balances",
                        "Records contractor reports timing bias before estimating recovery patterns",
                    ],
                    [
                        "Recorder, court, assessor, zoning, and mapped parcel records",
                        "Identity conflicts or access defects explain neglected inventory",
                        "Legal description and court findings resolve each material exception",
                        "Specialist stops purchases when essential exceptions remain unresolved",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Look for information advantages, not advertised maximum rates",
                "body": "The best sourcing edge is a faster, documented explanation of why a claim is available and how cash can return.",
                "items": [
                    "Compare successive official sale-list versions; withdrawals can reveal payment activity, but verify the actual reason before changing redemption assumptions.",
                    "Retain unsuccessful auction bids alongside winning bids so rate compression becomes visible before the next deposit deadline.",
                    "Ask assignment sellers for a certificate-level exception schedule, then reconcile it independently against county ownership and balance records.",
                    "Sample old county-held inventory before buying a batch; repeated access, contamination, or legal-description defects often explain apparent abundance.",
                ],
            },
        },
        {
            "heading": "2. Qualify claims with bid-down math and cash-loss constraints",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a one-hundred-point qualification score only after binary rejection "
                    "tests. Allocate twenty-five points to claim identity and priority evidence, "
                    "twenty-five to parcel utility and conservative recovery support, twenty to "
                    "redemption economics, fifteen to procedural executability, and fifteen to "
                    "capital duration and concentration. An illustrative passing threshold is "
                    "eighty points, but no aggregate score cures a mismatched legal description, "
                    "unresolved transfer restriction, unsupported title assumption, or unfunded "
                    "required action. Contractor one assembles the evidence packet; contractor "
                    "two reviews exceptions; the operator signs the purchase decision and "
                    "documents any departure from the rubric. Separate assessed value from "
                    "market evidence and separate property value from the amount the claim "
                    "can lawfully recover. Check senior or surviving interests under the "
                    "actual jurisdiction's rules rather than assuming all tax claims erase "
                    "everything else. Bankruptcy requires special attention because 11 U.S.C. "
                    "section 362 can constrain collection and enforcement activity. Record "
                    "whether a proceeding exists and obtain case-specific direction before "
                    "taking affected action. Keep inspection, title, transfer, servicing, and "
                    "potential enforcement costs explicit. A small certificate can fail "
                    "qualification solely because fixed diligence costs consume its plausible "
                    "interest receipts."
                ),
                (
                    "Price a certificate from cash movements, not its statutory headline. "
                    "For an illustrative jurisdiction allowing simple interest at the winning "
                    "rate, a $10,000 certificate at eight percent redeemed after nine months "
                    "produces $600 interest before applicable adjustments and costs. The "
                    "$10,000 returned principal is capital recovery, not revenue. If direct "
                    "diligence and servicing total $180, contribution before shared overhead "
                    "is $420. At a two-percent winning rate, otherwise identical interest "
                    "is $150 and contribution becomes negative $30. This illustration is "
                    "not a substitute for Florida's actual minimum-charge provisions: section "
                    "197.472 includes a five-percent minimum in specified circumstances and "
                    "an exception for certificates bid at zero percent. Encode the local "
                    "rule rather than applying one spreadsheet formula everywhere. Arizona "
                    "section 42-18114 uses interest-rate bidding with a statutory ceiling; "
                    "the ceiling does not describe the rate an auction winner necessarily "
                    "receives. For premium-bid jurisdictions, separately model whether the "
                    "premium earns interest, is refundable, or remains exposed. Stress "
                    "redemption at three, twelve, and twenty-four months, then model "
                    "nonredemption with explicit procedural costs. The lowest acceptable "
                    "rate must survive the expensive timing case, not merely the "
                    "most convenient expected date."
                ),
                (
                    "For a Texas redeemable deed, maintain a distinct worksheet reflecting "
                    "section 34.21's eligible redemption amounts, applicable property class, "
                    "and timing. The twenty-five-percent and fifty-percent premiums described "
                    "for qualifying two-year redemptions are statutory redemption mechanics, "
                    "not recurring annual coupons. Do not assume every improvement, fee, "
                    "or financing charge enters the redeemable base. Likewise, a possible "
                    "eventual property sale is not current disposition revenue. For all "
                    "four plays, build a downside case that assumes no prompt redemption, "
                    "additional carrying costs, and a contested next step. Tyler v. Hennepin "
                    "County, 598 U.S. 631 (2023), rejects the government's retention of "
                    "surplus value beyond the tax debt in the circumstances addressed "
                    "there; it does not make every private certificate foreclosure identical. "
                    "Have the specialist identify current state procedures and any surplus "
                    "distribution duties applicable to the selected route. Do not underwrite "
                    "an automatic windfall from eliminating an owner's equity. Cap both "
                    "individual parcel exposure and aggregate cash tied to one county "
                    "or enforcement deadline. The operator should prefer six serviceable "
                    "claims to ten claims that force simultaneous litigation spending. "
                    "Keep reserves outside the bid budget, because winning more auctions "
                    "does not replenish cash."
                ),
            ],
            "table": {
                "caption": "Qualification Weights, Evidence Requirements, and Hard Rejection Tests",
                "headers": [
                    "Decision dimension",
                    "Specific evidence to collect",
                    "Illustrative scoring or pricing treatment",
                    "Failure requiring rejection or specialist resolution",
                ],
                "rows": [
                    [
                        "Claim identity and priority receive twenty-five possible points",
                        "Match certificate, parcel, holder, legal description, and balances",
                        "Award full points only after documented independent reconciliation",
                        "Conflicting legal descriptions remain unresolved before bidding closes",
                    ],
                    [
                        "Parcel utility and recovery support receive twenty-five points",
                        "Obtain access evidence, zoning records, and closed comparables",
                        "Discount recovery assumptions for documented liquidity and condition weaknesses",
                        "Expected recovery relies entirely on unsupported assessor valuations",
                    ],
                    [
                        "Redemption economics receive twenty of the available points",
                        "Document winning rate, minimum charges, premiums, and recoverable costs",
                        "Run three timing cases and one nonredemption case",
                        "Direct costs exceed plausible receipts at permitted bid terms",
                    ],
                    [
                        "Procedural executability receives fifteen of the available points",
                        "Verify bidder eligibility, transfer procedure, notices, and action dates",
                        "Budget specialist work before any deadline becomes binding",
                        "Necessary enforcement action exceeds documented authority or available capacity",
                    ],
                    [
                        "Capital duration and concentration receive fifteen possible points",
                        "Measure county exposure, maturity clustering, and available cash reserves",
                        "Preserve servicing reserves outside all planned auction deposits",
                        "Simultaneous adverse outcomes exhaust the remaining operating cash",
                    ],
                    [
                        "Binary exception checks operate independently from aggregate scores",
                        "Review bankruptcy records, material title defects, and surplus procedures",
                        "Require eighty points plus resolution of material exceptions",
                        "High scores cannot compensate for unresolved purchase-blocking defects",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify four conditions before capital leaves the account",
                "body": "A purchase proceeds only when the evidence packet supports the claim, the procedure, the cash model, and the funded next action.",
                "items": [
                    "Confirm the official payee, bidder identity, deposit deadline, refund conditions, and independently verified payment instructions.",
                    "Reconcile certificate number, parcel identifier, legal description, current holder, redemption status, and assignability with authoritative records.",
                    "Recalculate receipts under the jurisdiction's actual interest, premium, minimum-charge, and cost-recovery rules; exclude returned principal.",
                    "Document bankruptcy review, unresolved title issues, applicable surplus procedures, and enough reserved cash for the adverse servicing case.",
                ],
            },
        },
        {
            "heading": "3. Convert public records into three to ten documented acquisitions",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Run different contact sequences for public administrators and willing "
                    "certificate sellers. Agencies provide records and procedures; they are "
                    "not prospects to pressure into preferential treatment. On day one, "
                    "send the published records contact a concise request identifying the "
                    "sale year, certificate fields, existing electronic format, and relevant "
                    "date range. On day five, call during posted hours to clarify "
                    "availability and any copying charges; follow the agency's response "
                    "schedule rather than repeatedly escalating. For an identified assignment "
                    "seller, day one is a personalized email naming the verified portfolio "
                    "or publicly offered certificates and requesting permission to review "
                    "an inventory. Day four is a manual call to a published business "
                    "number where lawful; day nine is a short written explanation of "
                    "required documents and settlement mechanics. Day fifteen closes the "
                    "loop, then pauses unless the seller responds. Respect opt-outs and "
                    "applicable channel restrictions; automated calling and texting introduce "
                    "additional requirements under 47 U.S.C. section 227. Commercial email "
                    "must satisfy applicable requirements of 15 U.S.C. section 7704. "
                    "No deceptive county affiliation, false deadline, bulk owner-pressure "
                    "campaign, or implication that a certificate holder already owns "
                    "the underlying home belongs in this acquisition system."
                ),
                (
                    "Create one inbound page describing actual purchasing criteria: selected "
                    "jurisdictions, certificate vintages, minimum document package, permissible "
                    "assignment structure, and the process for receiving a conditional price. "
                    "State that funds move only through independently verified settlement "
                    "instructions and the required county transfer procedure. Publish one "
                    "useful jurisdiction-specific worksheet showing how bid rate, redemption "
                    "date, and direct costs interact. Invite sellers to submit certificate "
                    "identifiers and business contact details; do not request occupants' "
                    "sensitive personal records. Ask local title professionals and brokers "
                    "for introductions to willing holders, not confidential client lists. "
                    "The operator handles every substantive seller conversation initially; "
                    "contractor one prepares verified records and contractor two resolves "
                    "transfer and title exceptions. Use a shared pipeline with stages "
                    "for sourced, matched, screened, specialist-reviewed, quoted or bid, "
                    "accepted, settled, and cash-realized. Each stage needs an evidence "
                    "link, owner, next date, and reason for rejection. Limit weekly "
                    "specialist reviews to the pod's purchased capacity; an illustrative "
                    "limit of six complete packets prevents half-reviewed opportunities "
                    "from accumulating before auction day. Track inbound and outbound "
                    "sources separately so referrals do not conceal poor cold-contact "
                    "economics or excessive administrative work."
                ),
                (
                    "Set conversion benchmarks as testable planning assumptions, not published "
                    "industry averages. An illustrative campaign starts with four hundred "
                    "raw certificate or deed records, resolves one hundred sixty into "
                    "current identifiable opportunities, screens sixty for basic economics, "
                    "and sends twenty-four complete packets to specialist review. Twelve "
                    "survive for priced decisions; six receive an eligible bid or "
                    "written offer; three settle with ownership or certificate transfer "
                    "confirmed. Those transitions are forty, 37.5, forty, fifty, fifty, "
                    "and fifty percent respectively, with a 0.75-percent overall acquisition "
                    "conversion. Auctions and assignments need separate subfunnels because "
                    "an auction award is not a signed seller mandate. If six "
                    "priced submissions produce no purchases, first inspect bid ceilings "
                    "and competition rather than indiscriminately expanding the mailing list. "
                    "Handle objections with evidence: a seller demanding face value plus "
                    "all accrued interest receives a dated payoff comparison and an "
                    "explanation of assignment friction; a seller refusing records receives "
                    "a precise document request and no binding offer. When someone "
                    "claims the house guarantees the return, explain the actual claim, "
                    "redemption rights, title conditions, and next lawful action. Preserve "
                    "rejected opportunities for scheduled factual updates, but do not "
                    "recontact people who declined further contact."
                ),
            ],
            "table": {
                "caption": "Contact Cadence and Evidence-Based Objection Responses",
                "headers": [
                    "Channel and timing",
                    "Specific message or useful asset",
                    "Response or objection to diagnose",
                    "Concrete next action and conversion evidence",
                ],
                "rows": [
                    [
                        "Official records email sent at campaign opening",
                        "Request existing certificate fields for named sale years",
                        "Agency requires narrower scope or applicable copying charges",
                        "Narrow fields and retain the agency's documented response",
                    ],
                    [
                        "Administrator clarification call after the published response interval",
                        "Confirm current inventory source and bidder procedure references",
                        "Staff cannot interpret individual investment or title questions",
                        "Move interpretation to the contracted local procedure specialist",
                    ],
                    [
                        "Personalized seller email on the first contact day",
                        "Identify offered certificates and request permission for review",
                        "Seller expects full accrued value without supporting documents",
                        "Send dated pricing inputs and request verifiable ownership evidence",
                    ],
                    [
                        "Manual business call on the fourth contact day",
                        "Explain transfer sequence and independently verified settlement instructions",
                        "Seller worries about payment risk during certificate transfer",
                        "Agree a lawful settlement sequence before issuing binding terms",
                    ],
                    [
                        "Written seller follow-up on the ninth contact day",
                        "Provide document checklist and an evidence-backed conditional range",
                        "Seller insists property value makes further diligence unnecessary",
                        "Explain claim limitations and preserve the unresolved exception",
                    ],
                    [
                        "Inbound worksheet and referral page maintained throughout sourcing",
                        "Publish actual jurisdiction criteria and a redemption-cost example",
                        "Submission lacks certificate identifiers needed for independent matching",
                        "Request identifiers before counting the submission as qualified",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build the official-source universe",
                    "action": "Collect dated county records and map each opportunity to one of the four plays.",
                    "detail": "Contractor one deduplicates parcel and certificate identifiers, preserving source files and rejected identity matches.",
                },
                {
                    "step": 2,
                    "title": "Qualify and reserve capital",
                    "action": "Apply binary exceptions, weighted scoring, local redemption math, and concentration limits.",
                    "detail": "The operator funds a separate servicing reserve; contractor two reviews material title and procedural exceptions.",
                },
                {
                    "step": 3,
                    "title": "Contact, price, and submit",
                    "action": "Use the appropriate agency or seller cadence and submit only fully supported bids or offers.",
                    "detail": "Record eligibility, price ceiling, document conditions, verified payment instructions, and a dated next action.",
                },
                {
                    "step": 4,
                    "title": "Settle and activate servicing",
                    "action": "Confirm recorded or administrative transfer, reconcile cash, and calendar every required next step.",
                    "detail": "Count an acquisition only after the transfer is confirmed; count realized receipts only after the cash event occurs.",
                },
            ],
        },
        {
            "heading": "4. Reconcile sourcing throughput to realized profit and servicing capacity",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Keep the canonical scorecard separate from the illustrative acquisition "
                    "funnel. Conservative annual gross revenue is $15,000 at a thirty-percent "
                    "net margin, producing $4,500 owner net profit and $10,500 implied "
                    "annual operating costs. Base gross revenue is $97,500 at 42.5 "
                    "percent, producing $41,437.50 before whole-dollar presentation, reported "
                    "as $41,438; implied costs are $56,062.50. Scaled gross revenue "
                    "is $180,000 at fifty-five percent, producing $99,000 owner profit "
                    "and $81,000 implied costs. These revenues comprise realized interest, "
                    "penalties, and disposition gains, excluding returned principal. Do not "
                    "replace them with certificate purchase volume, property sale proceeds, "
                    "or the face amount of the tax claims. The stated monthly "
                    "opex range of $500–$4,000 is a planning input, not an "
                    "identity that overrides scenario-level total costs. Reconcile contractor "
                    "charges, direct deal costs, and other modeled expenses without "
                    "counting them twice. Conservative and Base use one full-time role "
                    "plus two contractors; Scaled uses two full-time roles plus three "
                    "contractors. Role counts describe capacity, not proof that the "
                    "Conservative revenue supports three market-rate salaries. Specify owner "
                    "labor treatment and contractor hours before treating the model "
                    "as a hiring budget."
                ),
                (
                    "Use the $15,000–$85,000 startup capital range to design a "
                    "deployment schedule, not to infer a promised portfolio yield. "
                    "A hypothetical $100,000 deployment earning eight percent for a "
                    "full year would generate $8,000 simple interest before costs, "
                    "so it cannot by itself explain the Conservative $15,000 "
                    "revenue case. Different capital deployment, timing, penalties, or "
                    "realized gains would be needed; document those assumptions instead "
                    "of quietly upgrading the rate. Redemption tracking should reconcile "
                    "county notices, bank deposits, certificate balances, and ledger "
                    "entries. Separate principal recovery, realized receipts, recoverable "
                    "cost reimbursements, and unresolved differences. Use Python's standard "
                    "library or a spreadsheet to produce deadline reminders and "
                    "exception reports, but require human review before enforcement "
                    "or payment instructions. A certificate showing a changed status "
                    "on a portal is not proof that the correct amount "
                    "reached the bank. The operator reviews cash weekly; contractor "
                    "one checks records and calendar exceptions; contractor two handles "
                    "specialist issues within the agreed scope. Reinvest only reconciled "
                    "cash after retaining the next servicing reserve. Capital velocity "
                    "is useful only when the returned amount and its legal "
                    "allocation are both correct."
                ),
                (
                    "Run the first campaign as a sequence of dated learning "
                    "cycles across the 6–36-month horizon. During initial setup, "
                    "complete jurisdiction cards, score historical examples, and test "
                    "record joins before placing capital. During the first eligible "
                    "sale or assignment window, aim for a small number of "
                    "fully serviceable acquisitions rather than spending the entire "
                    "available budget. Review each settled purchase against its "
                    "original packet: actual bid terms, transfer friction, contractor "
                    "hours, and newly discovered exceptions. Every quarter, compare "
                    "the four plays on cost per reviewed packet, cost per "
                    "settled claim, realized receipts, outstanding principal, and approaching "
                    "procedural deadlines. Avoid declaring a sourcing channel superior "
                    "because it redeemed quickly while another channel's cases remain "
                    "open; show open cohorts separately. Expand toward ten wins "
                    "only when the existing inventory can absorb an adverse "
                    "redemption cycle without missing required work. Add the Scaled "
                    "team's second full-time role and third contractor when observed "
                    "servicing demand supports that capacity, not because a spreadsheet "
                    "lists the larger profit case. The durable first-deal system "
                    "is an auditable path from official source to priced "
                    "claim to confirmed cash, with every unresolved obligation "
                    "visible to its assigned owner."
                ),
            ],
            "table": {
                "caption": "Cash Recognition, Canonical Economics, and Capacity Controls",
                "headers": [
                    "Measurement or scenario",
                    "Required ledger or operating treatment",
                    "Review evidence and accountable role",
                    "Decision that the measurement should trigger",
                ],
                "rows": [
                    [
                        "Conservative case records $15,000 annual recognized gross revenue",
                        "Apply thirty-percent margin for $4,500 annual owner profit",
                        "Operator reconciles $10,500 implied costs against actual expense categories",
                        "Maintain one full-time role with two scoped contractors",
                    ],
                    [
                        "Base case records $97,500 annual recognized gross revenue",
                        "Apply 42.5-percent margin; report rounded owner profit of $41,438",
                        "Operator retains $41,437.50 profit and $56,062.50 costs internally",
                        "Increase throughput only while existing servicing capacity remains adequate",
                    ],
                    [
                        "Scaled case records $180,000 annual recognized gross revenue",
                        "Apply fifty-five-percent margin for $99,000 annual owner profit",
                        "Operator reconciles $81,000 implied costs with expanded team responsibilities",
                        "Use two full-time roles and three scoped contractors",
                    ],
                    [
                        "Returned certificate principal remains separate from recognized revenue",
                        "Credit investment principal recovery without inflating operating receipts",
                        "Records contractor matches county statements with cleared bank deposits",
                        "Release reinvestment cash only after reconciliation and reserve review",
                    ],
                    [
                        "Disposition gains require a completed and reconciled transaction",
                        "Separate sale proceeds, investment basis, and directly attributable costs",
                        "Operator reviews settlement records and the selected accounting treatment",
                        "Exclude projected property equity from realized revenue reporting",
                    ],
                    [
                        "Outstanding cohorts retain visible deadlines and unresolved cash exposure",
                        "Report open principal separately from already redeemed claim results",
                        "Specialist and records contractor maintain assigned next-action calendars",
                        "Pause new purchases when required servicing exceeds funded capacity",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Buy the claim you can verify, fund the process you must finish, and count only the cash you actually earn.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Select two jurisdictions and complete dated rule cards covering eligibility, bidding, assignment, redemption, enforcement, and surplus treatment.",
        "Build a source-linked inventory across primary auctions, county-held certificates, secondary assignments, and redeemable-deed sales without mixing their legal mechanics.",
        "Apply the weighted qualification rubric, resolve binary exceptions, and calculate local-rule bid ceilings with separate servicing reserves.",
        "Launch the agency and willing-seller contact sequences, publish the inbound criteria worksheet, and record opt-outs and channel-specific conversion results.",
        "Settle the first three fully reviewed acquisitions, confirm transfers independently, and activate redemption and procedural deadline tracking immediately.",
        "Reconcile principal separately from realized receipts, compare costs with the canonical cases, and expand toward ten wins only within funded servicing capacity.",
    ],
    "statutory_citations": [
        {
            "title": "Florida Statutes § 197.432 — Sale of tax certificates for unpaid taxes",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.432.html",
            "relevance": "Establishes Florida certificate-sale mechanics that must inform auction screening and bid preparation.",
        },
        {
            "title": "Florida Statutes § 197.472 — Redemption of tax certificates",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.472.html",
            "relevance": "Controls redemption calculations, including the specified minimum charge and treatment of zero-percent bids.",
        },
        {
            "title": "Florida Statutes § 197.502 — Application for obtaining tax deed by holder of tax sale certificate",
            "url": "https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/Sections/0197.502.html",
            "relevance": "Defines the certificate holder's tax-deed application route and supports action-date and cash-reserve planning.",
        },
        {
            "title": "Arizona Revised Statutes § 42-18114 — Sale of tax lien; interest rate",
            "url": "https://www.azleg.gov/ars/42/18114.htm",
            "relevance": "Provides the statutory interest-rate bidding framework; maximum permitted rates must not be mistaken for achieved yields.",
        },
        {
            "title": "Texas Tax Code § 34.21 — Right of redemption",
            "url": "https://statutes.capitol.texas.gov/Docs/TX/htm/TX.34.htm#34.21",
            "relevance": "Distinguishes redemption periods, eligible amounts, and premiums for Texas tax-sale property categories.",
        },
        {
            "title": "11 U.S.C. § 362 — Automatic stay",
            "url": "https://www.law.cornell.edu/uscode/text/11/362",
            "relevance": "Requires bankruptcy-aware review before collection or enforcement actions affected by the stay.",
        },
        {
            "title": "Tyler v. Hennepin County, 598 U.S. 631 (2023)",
            "url": "https://www.supremecourt.gov/opinions/22pdf/22-166_8n59.pdf",
            "relevance": "Primary judicial authority addressing retention of surplus property value beyond tax debt; informs jurisdiction-specific surplus review.",
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": "Relevant to telephone and text outreach design, particularly automated methods and applicable restrictions.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of messages",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Supplies commercial-email requirements relevant to sender identification, message content, and opt-out handling.",
        },
    ],
}
