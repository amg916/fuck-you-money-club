from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-and-landing-your-first-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in subject-to & wraparound note arbitrage, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (2–6 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "Mine Recorder and Municipal Signals, Match Low-Rate Debt to RMLO-Qualified Demand, and Close Through Auditable Servicing",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #35, Subject-To & Wraparound Note Arbitrage, holds Rank #09 of 36 "
        "with a 90/100 Money-to-Manpower Score. Its sourcing advantage is finding "
        "transferable economics before competing buyers price them, not hiding ownership "
        "changes from lenders. This chapter translates 11 mapped plays into a disciplined "
        "pipeline: municipal distress signals, recorded debt, seller intent, buyer demand, "
        "and professional referrals. Separate property acquisition from mortgage origination, "
        "route owner-occupant buyers through a licensed RMLO, and verify every underlying "
        "payment through a licensed servicer. The canonical annual owner-profit cases are "
        "$28,000 Conservative, $190,000 Base, and $442,000 Scaled. Build toward the first "
        "three completed transactions before expanding toward ten; track seller permissions, "
        "documented debt economics, buyer repayment capacity, and cash reserves rather than "
        "celebrating unqualified lead counts."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$100,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wraparound interest margin",
            "note": "28% net margin; $28,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$475,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wraparound interest margin",
            "note": "40.0% net margin; $190,000 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$850,000",
            "context": "Annual operator revenue: net upfront spreads plus retained wraparound interest margin",
            "note": "52% net margin; $442,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Mine Debt and Property Events Before Buying Another Lead List",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with one county, two adjacent postal areas, and a property type your "
                    "title company, insurance broker, and servicer already understand. Build a "
                    "parcel-centered ledger in Airtable or PostgreSQL with parcel identifier, "
                    "recorded owner, mailing address, deed date, mortgage recording date, lien "
                    "events, permit status, and source timestamp. Pull county recorder indexes, "
                    "assessor ownership exports, municipal inspection results, and court foreclosure "
                    "dockets through permitted downloads. A recorded mortgage amount is historical "
                    "principal, not today's payoff; a recording year suggests a rate cohort but "
                    "does not establish the contract rate. Require a seller-authorized current "
                    "statement before scoring debt economics. Cross-reference expired listings "
                    "through an authorized broker relationship rather than scraping restricted MLS "
                    "screens. Deduplicate by parcel and owner before spending on enrichment. Exclude "
                    "active bankruptcy cases pending specialist review, properties beyond your repair "
                    "capacity, and situations where statutory foreclosure-rescue restrictions defeat "
                    "the proposed approach. The useful signal is a solvable mismatch: affordable "
                    "existing debt, a seller needing a timely exit, manageable property defects, "
                    "and buyers whose documented income supports the eventual payment. Cheap debt "
                    "without transferable operating economics is simply an attractive line in a "
                    "spreadsheet. Record source permissions alongside each import so a vendor "
                    "change does not erase provenance."
                ),
                (
                    "Implement municipal_code_violation_trigger_arbitrage as a narrow daily "
                    "exception queue, not a citywide scraping campaign. Poll municipal building "
                    "department portals and county recorder dockets for failed structural or fire "
                    "inspections, expired permits, new code citations, and newly filed mechanic's "
                    "liens. Join events to parcels, suppress duplicate notices, and distinguish an "
                    "open violation from a cured case. A lien filing is an allegation requiring "
                    "document review, not proof that every claimed dollar is collectible. An "
                    "illustrative weekly batch of 100 events might yield 25 unique properties, "
                    "eight reachable owners, three authorized assessments, and one viable acquisition "
                    "conversation. At $250 for permitted data and research, that is $10 per unique "
                    "property and $250 per acquisition conversation before labor. With owner "
                    "permission, route the remediation track exclusively to one qualified contractor "
                    "or construction attorney while separately documenting any acquisition interest. "
                    "Do not receive a percentage of legal fees or disguise settlement-service "
                    "referrals as data sales. Treat any separate remediation revenue as outside "
                    "this volume's scorecard. When portal access is restricted or rate-limited, "
                    "use low-frequency scheduled API or bulk exports. Identify every message as "
                    "private commercial contractor or remediation assistance; never imitate an "
                    "inspector, municipality, or court."
                ),
                (
                    "Use eleven mapped plays as operating queues, with the required municipal "
                    "play and ten chapter-specific sourcing workflows shown below. These workflow "
                    "labels describe execution rather than additional canonical identifiers. Rate "
                    "each queue by verified conversations per research hour, not the dramatic "
                    "appearance of its distress signal. Low-equity owners with current payments "
                    "can be better counterparties than owners facing tomorrow's auction because "
                    "there is time for title, disclosures, buyer underwriting, and lender review. "
                    "Mechanic's liens and failed inspections usually belong in a remediation-first "
                    "queue until release costs and repair scope are established. Interview three "
                    "local agents and two property managers about homes that attract payment-sensitive "
                    "buyers but stall under ordinary financing. Ask for property characteristics "
                    "and transaction bottlenecks, not protected-class profiles. Build a small inbound "
                    "page explaining existing-debt purchases, potential lender acceleration, seller "
                    "credit exposure, and the documents needed for evaluation. Give sellers a "
                    "choice between a conventional sale referral, a documented creative-finance "
                    "review, and no further contact. Public-record distress never establishes "
                    "permission for unrestricted calling or texting. Keep acquisition outreach "
                    "separate from mortgage advertising, and have the RMLO review any advertised "
                    "credit terms before publication. Review queue performance every Friday and "
                    "stop funding channels that produce inaccessible documents rather than usable "
                    "seller decisions."
                ),
            ],
            "table": {
                "caption": "Eleven Mapped Sourcing Plays: Test Units, Evidence Requirements, and Risk Fallbacks",
                "headers": [
                    "Mapped play and actionable operating signal",
                    "Illustrative sourcing unit math and budget",
                    "Evidence required before advancing the opportunity",
                    "Risk fallback when the signal fails",
                ],
                "rows": [
                    [
                        "municipal_code_violation_trigger_arbitrage: inspect failed inspections, expired permits, citations, and mechanic's liens",
                        "Research 100 events for $250; target one qualified acquisition conversation",
                        "Verify open case status, owner authority, repair scope, and lien documents",
                        "Use scheduled bulk exports; identify private assistance and route remediation exclusively",
                    ],
                    [
                        "Recorded low-rate debt cohort: investigate older purchase mortgages with recent seller intent",
                        "Review 80 parcels for $160; target four seller-authorized statement reviews",
                        "Obtain current rate, remaining balance, maturity, arrears, and transfer provisions",
                        "Discard inferred rates when actual statements eliminate the payment advantage",
                    ],
                    [
                        "Expired listing reset: approach owners whose conventional listing strategy recently stalled",
                        "Evaluate 30 authorized broker leads; seek six substantive seller conversations",
                        "Confirm listing status, brokerage obligations, realistic value, and seller timing",
                        "Offer a conventional relisting referral when creative terms add unnecessary risk",
                    ],
                    [
                        "Absentee landlord exit: identify owners describing management fatigue and deferred maintenance",
                        "Mail 60 researched owners for $90; model three voluntary responses",
                        "Review leases, deposits, tenant protections, repair estimates, and insurance availability",
                        "Retain existing tenancy economics or decline unsupported vacant-possession assumptions",
                    ],
                    [
                        "Pre-foreclosure document review: prioritize sufficient time for deliberate transaction execution",
                        "Research 20 filings for $100; seek two complete reinstatement packages",
                        "Verify sale date, reinstatement quote, representation, and applicable rescue restrictions",
                        "Refer urgent cases to housing counseling or counsel instead of rushing",
                    ],
                    [
                        "Estate representative outreach: address verified fiduciaries managing a documented property disposition",
                        "Review 15 authorized introductions; target three properly documented property evaluations",
                        "Confirm probate authority, beneficiary constraints, recorded title, and transaction powers",
                        "Pause until court authority and required signatures are fully established",
                    ],
                    [
                        "Relocation timing mismatch: serve sellers carrying two housing payments during transition",
                        "Request ten agent introductions; seek two sellers with documented timing needs",
                        "Compare sale alternatives, remaining debt, move date, and reserve requirements",
                        "Recommend an ordinary sale when net proceeds sufficiently solve timing",
                    ],
                    [
                        "Agent dead-file review: revisit failed transactions with financing-related cancellation evidence",
                        "Review 25 permitted files; target five current owner permission requests",
                        "Separate buyer financing failures from unresolved property defects or valuation disputes",
                        "Require a fresh valuation and authorized outreach before reopening negotiations",
                    ],
                    [
                        "RMLO buyer-demand map: aggregate documented payment capacity without exposing applicant identities",
                        "Review 20 voluntary inquiries; target five complete licensed underwriting intakes",
                        "Use consented intake, verified affordability ranges, and consistent housing criteria",
                        "Keep unqualified inquiries in education rather than promising future mortgage approval",
                    ],
                    [
                        "Servicer and professional introductions: invite unpaid problem-solving conversations with authorized counterparties",
                        "Hold eight professional meetings; target two owner-requested acquisition introductions monthly",
                        "Confirm owner permission and independent selection of settlement-service providers",
                        "Reject referral compensation structures tied to covered settlement-service business",
                    ],
                    [
                        "Educational inbound page: explain existing-debt purchases with a document-first intake",
                        "Spend $300 on local traffic; target three complete seller submissions",
                        "Collect property identifiers and contact permission before requesting sensitive documents",
                        "Revise targeting and disclosures when traffic produces misleading credit expectations",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Win the Document Race Rather Than the Distress Race",
                "body": "Prioritize verified debt and repair facts that competing cash-offer campaigns rarely obtain.",
                "items": [
                    "Save both the original municipal event and its latest disposition; a cured violation should not keep generating distress messages.",
                    "Ask for the mortgage statement before discussing a purchase premium; a recent refinance can erase the presumed low-rate advantage.",
                    "Have a contractor price the inspection failure separately from cosmetic improvements so a repair budget does not bury a life-safety issue.",
                    "Offer the seller a secure, revocable document-sharing invitation rather than requesting mortgage statements through ordinary text messages.",
                ],
            },
        },
        {
            "heading": "2. Qualify Both Sides Before Calling a Spread Profitable",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Apply a 100-point seller-and-property score only after basic ownership and "
                    "contact permissions are established. Allocate 25 points to verified debt "
                    "economics, 20 to title and transfer feasibility, 20 to buyer-supported "
                    "affordability, 15 to property condition, 10 to seller objectives, and 10 "
                    "to reserves and exit liquidity. Advance scores of 80 or more, request "
                    "specific missing evidence at 65 through 79, and archive lower scores unless "
                    "a documented fact changes. These thresholds are internal priorities, not "
                    "statistical predictions. A hard stop overrides every score: unresolved "
                    "authority, an unmanageable lien, unsafe occupancy, unsupported repayment "
                    "capacity, or inadequate acceleration reserves cannot be offset by a low "
                    "interest rate. Have title counsel inspect the mortgage, deed restrictions, "
                    "junior liens, tax balances, association claims, and any foreclosure timetable. "
                    "The Garn-St Germain framework generally permits enforcement of due-on-sale "
                    "clauses subject to enumerated exceptions; an ordinary investor acquisition "
                    "does not become protected merely because payments remain current. Do not "
                    "use a trust as a concealment device. Identify whether lender consent, a "
                    "permitted assumption, payoff, or another documented structure can solve the "
                    "transfer issue. If it cannot, price the exposure explicitly or decline. "
                    "Record who reviewed the proposed structure and which documents support "
                    "their conclusion."
                ),
                (
                    "Build buyer demand before locking scarce reserves into inventory, but do "
                    "not confuse a large down payment with repayment capacity. Route every "
                    "owner-occupant wrap buyer through a licensed RMLO under the applicable SAFE "
                    "Act, state licensing, and Dodd-Frank Ability-to-Repay framework. Counsel and "
                    "the RMLO should identify which creditor duties and seller-financing "
                    "provisions apply; the chapter's operating standard uses licensed underwriting "
                    "even when a narrow exclusion might otherwise be available. Collect application "
                    "data through the licensed workflow, obtain appropriate authorization for "
                    "consumer reports, and avoid storing Social Security numbers in the marketing "
                    "CRM. Evaluate verified income, employment where relevant, obligations, "
                    "credit history, mortgage-related expenses, and the applicable payment "
                    "calculation. Apply consistent criteria and handle adverse-action duties "
                    "through the responsible creditor. Build demand maps from payment ranges, "
                    "property needs, and timing, not ethnicity, disability, familial status, or "
                    "neighborhood proxies for protected characteristics. Ask the RMLO for "
                    "de-identified counts of completed, supportable files rather than raw applicant "
                    "records. A pipeline of five documented households at an affordable total "
                    "housing payment is more useful than fifty people clicking seller-finance "
                    "advertisements. Refresh capacity before contracting because debt, employment, "
                    "insurance costs, and property taxes can change between inquiry and closing."
                ),
                (
                    "Test the spread using amortization rather than subtracting two advertised "
                    "interest rates. Illustratively, an underlying $240,000 balance at 3% with "
                    "360 monthly payments has principal-and-interest payments of about $1,012. "
                    "A $270,000 wrap at 7.5% over the same term produces about $1,888. "
                    "The roughly $876 monthly payment difference is not retained interest "
                    "revenue: first-month interest is $1,687.50 on the wrap and $600 on "
                    "the underlying loan, a $1,087.50 interest difference, while principal "
                    "amortization explains the remaining distinction. Servicing, losses, carrying "
                    "costs, and operating expenses further affect cash and profit. Add taxes, "
                    "insurance, association charges, and lawful escrow treatment to the buyer's "
                    "affordability analysis. Obtain actual insurance quotes for the ownership and "
                    "occupancy structure; preserving an unsuitable old policy is not a savings "
                    "strategy. For a $30,000 buyer down payment, $12,000 seller equity, "
                    "$4,000 arrears, and $4,000 transaction costs leave a $10,000 provisional "
                    "upfront economic spread before accounting classification. Allocating another "
                    "$6,000 to reserves leaves $4,000 deployable cash, not a second expense "
                    "or additional revenue. Have the accountant distinguish sale economics, "
                    "financing principal, restricted cash, and recognized operator spreads. Replace "
                    "every illustrative input with closing documents before approving an offer. "
                    "Stress the exit against both buyer default and lender acceleration."
                ),
            ],
            "table": {
                "caption": "Documented Qualification Scorecard with Overrides That Protect Capital",
                "headers": [
                    "Scored category and maximum available points",
                    "Evidence supporting a strong qualification result",
                    "Downside test required before capital commitment",
                    "Disposition when evidence fails the test",
                ],
                "rows": [
                    [
                        "Verified debt economics receives twenty-five possible points",
                        "Current statement confirms balance, rate, arrears, maturity, and payment composition",
                        "Recalculate amortization and compare retained interest with servicing and loss costs",
                        "Request corrected debt records or reject the unsupported spread assumption",
                    ],
                    [
                        "Title and transfer feasibility receives twenty possible points",
                        "Title review resolves authority, liens, restrictions, disclosures, and transfer exposure",
                        "Model lender acceleration without assuming continued payment prevents enforcement",
                        "Pursue documented consent, assumption, conventional payoff, or a declined transaction",
                    ],
                    [
                        "Buyer-supported affordability receives twenty possible points after licensed review",
                        "RMLO documents supportable total housing payment under applicable underwriting requirements",
                        "Include insurance renewal, tax changes, association charges, and applicable payment resets",
                        "Reduce price or financing amount without weakening documented underwriting standards",
                    ],
                    [
                        "Property condition receives fifteen possible points after independent inspection",
                        "Qualified inspection and written estimates establish safety issues and repair sequencing",
                        "Test delayed permits, contractor overruns, and inability to occupy during repairs",
                        "Require completed remediation or decline properties beyond available repair capacity",
                    ],
                    [
                        "Seller objectives receive ten possible points after alternatives discussion",
                        "Seller understands continuing loan exposure, alternatives, timing, and proposed consideration",
                        "Confirm voluntary decisions without depending on an imminent foreclosure deadline",
                        "Refer to a conventional sale or independent adviser when objectives conflict",
                    ],
                    [
                        "Reserves and exit liquidity receive ten possible points",
                        "Committed cash covers modeled carrying costs and a credible acceleration response",
                        "Stress six months of missed receipts plus locally estimated enforcement expenses",
                        "Do not close when the exit requires uncommitted future buyer deposits",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four Verifications Before Making the Offer Binding",
                "body": "A strong sourcing score never substitutes for a complete closing and servicing structure.",
                "items": [
                    "Verify title, seller authority, recorded liens, underlying loan terms, due-on-sale exposure, and the documented response to acceleration.",
                    "Verify licensed RMLO review of every owner-occupant buyer, applicable creditor duties, consistent affordability criteria, and required disclosures.",
                    "Verify the third-party servicer's required licenses, underlying-payment reporting, escrow responsibilities, and late-payment escalation procedure.",
                    "Verify actual insurance placement, repair funding, reserve liquidity, and state-specific wrap requirements, including Texas provisions where applicable.",
                ],
            },
        },
        {
            "heading": "3. Run a Permission-Aware Cadence That Converts Documents into Offers",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use a six-touch, twenty-one-day cadence only where each channel is lawful "
                    "and the recipient has not opted out. Day one is a plain mailed "
                    "letter naming your company, property, private commercial purpose, and "
                    "document-review offer. Day three is a manually placed call after applicable "
                    "do-not-call screening and state-law review. Day seven is a short email "
                    "where an address was properly obtained, with accurate sender information "
                    "and an effective unsubscribe process. Day ten is a useful follow-up "
                    "explaining what a current mortgage statement reveals. Day fourteen offers "
                    "a fifteen-minute comparison of conventional sale, assumption if available, "
                    "and existing-debt acquisition. Day twenty-one closes the sequence and "
                    "offers a clear stop-contact choice. Do not treat a public telephone "
                    "number as permission for automated dialing, prerecorded messages, or "
                    "marketing texts. Use Twilio only after a documented channel-specific review "
                    "and required permissions; use the CRM to enforce suppression across "
                    "vendors. For inbound demand, publish one factual local case walkthrough "
                    "and a secure intake form rather than promising universal qualification. "
                    "Keep credit advertisements under RMLO review, including Regulation Z "
                    "triggering-term requirements. A channel that creates complaints faster "
                    "than qualified files is expensive even when its nominal response rate "
                    "looks impressive."
                ),
                (
                    "Model conversion with an explicit denominator. An illustrative cohort of "
                    "300 unique researched owners might produce 240 deliverable, eligible "
                    "contacts, 36 two-way conversations, 18 document-complete seller files, "
                    "nine fully screened opportunities, six written offers, four signed purchase "
                    "agreements, and three closings. That equals 80% contact eligibility, 15% "
                    "conversation conversion from eligible contacts, 50% document completion "
                    "from conversations, and 1% closing conversion from raw records. A signed "
                    "purchase agreement is an intermediate milestone, not booked revenue; "
                    "a referral mandate also does not transfer property. At $1,500 of data "
                    "and outreach spend, acquisition marketing cost is $500 per closing "
                    "before labor, legal work, inspections, and failed-file costs. Label these "
                    "figures as planning hypotheses until your own cohorts mature. Track "
                    "cohorts by first-contact month and source so a long closing cycle "
                    "does not make this week's channel look ineffective. Three closings from "
                    "300 records does not mean ten closings require exactly 1,000 records; "
                    "seller mix, title defects, buyer capacity, and reserves can change "
                    "conversion materially. Review document-completion and offer-acceptance "
                    "rates separately. If conversations are healthy but statements never "
                    "arrive, fix trust and secure intake before purchasing more records. "
                    "Never scale marketing faster than the underwriting team's document "
                    "review capacity."
                ),
                (
                    "Handle objections by clarifying the actual exposure, not by winning a "
                    "debate. When a seller asks whether the loan leaves their name, answer "
                    "that a subject-to transfer ordinarily leaves their existing borrower "
                    "obligation in place unless the lender releases it. Offer payment "
                    "visibility and independent review, not a promise of release. When "
                    "asked whether the lender can call the loan, explain the due-on-sale "
                    "clause, applicable law, and the transaction's documented response plan. "
                    "If a seller demands all retail equity immediately, compare conventional "
                    "sale proceeds rather than forcing an unsuitable structure. If a buyer "
                    "asks to qualify solely through a deposit, explain that licensed "
                    "repayment-capacity review still applies. If a contractor wants an "
                    "exclusive lead, establish owner permission, service scope, response "
                    "time, and any lawful fixed-price work separately from mortgage "
                    "settlement referrals. Record the objection category and the next "
                    "evidence-producing action in the CRM. A respectful decline with a "
                    "specific reason is a useful outcome because it preserves time and "
                    "prevents unsuitable commitments. Follow every substantive call with a "
                    "written summary of discussed alternatives, requested records, and "
                    "unresolved risks. Avoid scripts claiming government affiliation, "
                    "guaranteed credit repair, hidden lender protection, or inevitable "
                    "foreclosure savings. Those claims undermine the very trust required "
                    "to obtain reliable documents."
                ),
            ],
            "table": {
                "caption": "Twenty-One-Day Contact Cadence and Evidence-Based Objection Responses",
                "headers": [
                    "Touchpoint or objection requiring a response",
                    "Specific message or operator response approach",
                    "Required next action and recorded evidence",
                    "Stop condition or alternative transaction path",
                ],
                "rows": [
                    [
                        "Day one mailed introduction to researched property owners",
                        "Explain private commercial purpose and offer a documented sale-options comparison",
                        "Record mailing source, parcel match, delivery result, and any response permission",
                        "Suppress future outreach immediately when the owner requests no contact",
                    ],
                    [
                        "Day three screened manual telephone conversation with owner",
                        "Ask about timing and objectives before discussing any proposed financing structure",
                        "Record contact screening, stated authority, requested documents, and next appointment",
                        "End the sequence when representation or contact restrictions prevent direct engagement",
                    ],
                    [
                        "Day seven email and day ten document follow-up",
                        "Provide secure intake instructions without requesting sensitive mortgage documents by text",
                        "Measure completed statements and ownership evidence rather than opens or clicks",
                        "Honor unsubscribe requests across every connected outbound marketing vendor",
                    ],
                    [
                        "Day fourteen comparison and day twenty-one sequence closure",
                        "Compare conventional sale, available assumption, and documented existing-debt acquisition economics",
                        "Send written alternatives and invite an explicit future-contact preference",
                        "Archive inactive files without pretending silence establishes ongoing marketing permission",
                    ],
                    [
                        "Seller objects that the existing mortgage remains personal",
                        "Confirm continuing borrower exposure unless the lender provides an actual release",
                        "Offer independent review and describe monthly servicing visibility without overstating protection",
                        "Recommend a payoff sale when continued liability conflicts with seller objectives",
                    ],
                    [
                        "Buyer proposes a large deposit instead of underwriting",
                        "Explain that deposit strength does not replace documented repayment-capacity assessment",
                        "Refer the complete application to the licensed RMLO through secure intake",
                        "Decline unsupported financing rather than relabeling the arrangement to avoid duties",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Build and clean the weekly cohort",
                    "action": "Import permitted records, deduplicate parcels, and verify owner contact eligibility.",
                    "detail": "Assign a source timestamp, source cost, suppression status, and responsible operator to every record before the first message.",
                },
                {
                    "step": 2,
                    "title": "Convert conversation into an evidence packet",
                    "action": "Request authorized mortgage statements, ownership records, repair facts, and seller objectives.",
                    "detail": "Use a secure intake service and measure document completion within seven days of the first substantive conversation.",
                },
                {
                    "step": 3,
                    "title": "Match seller economics with licensed buyer review",
                    "action": "Complete title screening, affordability assessment, servicing design, and reserve stress tests.",
                    "detail": "Issue a written offer only when unresolved matters are identified, priced where appropriate, and assigned to a qualified reviewer.",
                },
                {
                    "step": 4,
                    "title": "Close and reconcile the cohort",
                    "action": "Track agreement, closing, boarding, and verified first-payment milestones separately.",
                    "detail": "Calculate cost per closing and document the reasons for every withdrawal before increasing the next cohort's marketing budget.",
                },
            ],
        },
        {
            "heading": "4. Land Three Controlled Closings, Then Earn the Right to Pursue Ten",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Sequence the first two to six months around evidence, not an arbitrary "
                    "closing quota. During weeks one and two, engage local real-estate "
                    "counsel, title or escrow, a licensed RMLO, an insurance broker, and "
                    "a third-party servicer licensed where required. Confirm who can "
                    "actually support wrap transactions; a familiar company name does not "
                    "establish jurisdictional capability. During weeks three through six, "
                    "work the first researched cohort and build parallel buyer intake. "
                    "During weeks seven through twelve, advance the strongest files "
                    "through inspections, underwriting, disclosures, and closing preparation. "
                    "Months four through six should concentrate on verified servicing "
                    "performance and a second cohort only when reserves remain adequate. "
                    "Three completed transactions are a practical initial target; reaching "
                    "ten within this window requires unusually strong conversion, capacity, "
                    "and capital, rather than a different definition of a win. Distinguish "
                    "signed agreements, completed acquisitions, completed wrap sales, and "
                    "performing boarded notes on the dashboard. Some transactions will "
                    "not close in the window. A file that exits to an ordinary sale "
                    "can validate your sourcing relationship without generating wrap "
                    "revenue. Do not count it in this volume's retained-interest "
                    "production. Assign each live file a next action, accountable "
                    "person, and dated dependency so outside professionals are not "
                    "mistaken for available full-time staff."
                ),
                (
                    "Keep the Formula v2.0 scenarios fixed while treating sourcing volumes "
                    "as illustrative support. Conservative annual operator revenue is "
                    "$100,000, expenses are $72,000, and owner net profit is $28,000 "
                    "at 28% with 1 FT + 3 C. Base revenue is $475,000, expenses "
                    "are $285,000, and owner profit is $190,000 at 40.0% with "
                    "1 FT + 3 C. Scaled revenue is $850,000, expenses are $408,000, "
                    "and owner profit is $442,000 at 52% with 2 FT + 4 C. "
                    "One arithmetic bridge is ten recognized upfront spreads averaging "
                    "$4,000 plus twenty performing note-year equivalents averaging "
                    "$3,000 of retained interest for Conservative; twenty-five times "
                    "$7,000 plus fifty times $6,000 for Base; and forty times "
                    "$10,000 plus seventy-five times $6,000 for Scaled. These are "
                    "illustrative revenue mixes, not additional scorecard inputs or "
                    "first-year promises. A note-year equivalent represents twelve "
                    "months of recognized contribution, so midyear closings contribute "
                    "fractionally. Despite the scorecard's gross-revenue label, its "
                    "basis already excludes property face value, loan principal, and "
                    "pass-through debt service. Preserve that retained-share basis "
                    "without taking the spread twice. Have the accountant apply "
                    "ASC 606 where applicable to fee or sale components and the "
                    "relevant lending guidance to interest; cash collection alone "
                    "does not determine recognized revenue."
                ),
                (
                    "Board each closed wrap with a documented payment waterfall and "
                    "monthly reconciliation of buyer receipts, underlying debt service, "
                    "taxes, insurance, servicing charges, reserves, and operator "
                    "distributions. Autopay is a collection mechanism, not evidence "
                    "that the underlying lender was paid. Obtain servicer reports "
                    "and independently verify the underlying account through authorized "
                    "access or statements; investigate differences before distributing "
                    "cash. Keep buyer defaults and underlying-payment failures in "
                    "separate exception queues because one can occur without the "
                    "other. Reconfirm escrow sufficiency after tax reassessments and "
                    "insurance renewals. For Texas transactions, review Property "
                    "Code Section 5.016 alongside Finance Code Chapter 159, including "
                    "applicable licensing, disclosures, borrower rights, and payment "
                    "obligations; one notice provision does not cover the entire "
                    "structure. Review federal servicing requirements and state "
                    "collection procedures with the servicer before drafting default "
                    "messages. Reserve planning should use actual local foreclosure "
                    "timelines, repair exposure, and an acceleration-response model, "
                    "not merely six scheduled installments. The $12,000–$65,000 "
                    "startup range and $2,000–$12,000 monthly operating range do "
                    "not authorize thin property reserves or replace the annual "
                    "scenario expense totals. Increase sourcing only after the first "
                    "three transactions demonstrate clean document retention, timely "
                    "underlying payments, and accurate revenue classification. A "
                    "performing note with transparent servicing is the repeatable "
                    "product; an impressive closing photograph is not."
                ),
            ],
            "table": {
                "caption": "First-Deal Milestones and Exact Formula v2.0 Revenue Reconciliation",
                "headers": [
                    "Milestone or canonical annual operating case",
                    "Measurable production or recognized revenue basis",
                    "Required economics and staffing or accountability",
                    "Verification before increasing transaction acquisition volume",
                ],
                "rows": [
                    [
                        "Initial preparation during the first two operating weeks",
                        "Complete provider engagement, permitted data setup, secure intake, and template review",
                        "Owner coordinates counsel, RMLO, title, insurance, and licensed servicing resources",
                        "Confirm jurisdictional capability and written responsibility for every material closing task",
                    ],
                    [
                        "First researched cohort during weeks three through twelve",
                        "Track 300 records through conversations, complete files, agreements, and actual closings",
                        "Illustrative $1,500 marketing spend targets three closings before professional transaction costs",
                        "Replace assumed conversion rates with observed source-cohort results before expanding spend",
                    ],
                    [
                        "First three performing transactions before pursuing ten completed wins",
                        "Require completed closings, boarded accounts, and verified first underlying payments",
                        "Maintain committed reserves independent of anticipated deposits from future buyers",
                        "Reconcile statements and clear payment exceptions before increasing simultaneous transaction commitments",
                    ],
                    [
                        "Conservative annual case using the canonical retained operator revenue basis",
                        "$100,000 revenue equals $40,000 upfront spreads plus $60,000 retained interest",
                        "$72,000 expenses leave $28,000 profit at 28%; team 1 FT + 3 C",
                        "Illustrative mix uses ten upfront spreads and twenty full note-year equivalents",
                    ],
                    [
                        "Base annual case using the canonical retained operator revenue basis",
                        "$475,000 revenue equals $175,000 upfront spreads plus $300,000 retained interest",
                        "$285,000 expenses leave $190,000 profit at 40.0%; team 1 FT + 3 C",
                        "Illustrative mix uses twenty-five upfront spreads and fifty full note-year equivalents",
                    ],
                    [
                        "Scaled annual case using the canonical retained operator revenue basis",
                        "$850,000 revenue equals $400,000 upfront spreads plus $450,000 retained interest",
                        "$408,000 expenses leave $442,000 profit at 52%; team 2 FT + 4 C",
                        "Illustrative mix uses forty upfront spreads and seventy-five full note-year equivalents",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Source the problem, verify the debt, qualify the buyer, and count the spread only after the ledger explains it.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Choose one county and build a parcel-centered ledger joining recorder, assessor, municipal inspection, permit, and lien events through permitted sources.",
        "Launch municipal_code_violation_trigger_arbitrage with daily exception review, owner-authorized exclusive remediation routing, and a scheduled-export fallback.",
        "Score each documented opportunity across debt, title, affordability, condition, seller objectives, and reserves; enforce hard stops regardless of total points.",
        "Run the twenty-one-day permission-aware cadence and measure raw records, eligible contacts, conversations, complete files, offers, agreements, and closings separately.",
        "Route every owner-occupant wrap buyer through a licensed RMLO and confirm title, insurance, state wrap requirements, servicing responsibilities, and acceleration exposure.",
        "Reconcile the first three boarded transactions to verified underlying payments and the canonical retained-revenue basis before committing capital toward ten completed wins.",
    ],
    "statutory_citations": [
        {
            "title": "12 U.S.C. § 1701j-3 — Preemption of due-on-sale prohibitions",
            "url": "https://www.law.cornell.edu/uscode/text/12/1701j-3",
            "relevance": "Establishes the federal due-on-sale framework and enumerated exceptions; ordinary investor transfers require transaction-specific analysis rather than assumptions based on continued payment.",
        },
        {
            "title": "12 U.S.C. § 5103 — Mortgage loan originator licensing and registration",
            "url": "https://www.law.cornell.edu/uscode/text/12/5103",
            "relevance": "Supports verification of applicable SAFE Act licensing or registration obligations for mortgage origination activity, alongside state requirements.",
        },
        {
            "title": "15 U.S.C. § 1639c — Minimum standards for residential mortgage loans",
            "url": "https://www.law.cornell.edu/uscode/text/15/1639c",
            "relevance": "Provides the statutory ability-to-repay framework for covered residential mortgage lending and supports documented borrower repayment-capacity review.",
        },
        {
            "title": "12 CFR § 1026.43 — Minimum standards for transactions secured by a dwelling",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.43",
            "relevance": "Defines covered transaction requirements and repayment-capacity considerations; counsel and the licensed RMLO determine applicability to each proposed wrap.",
        },
        {
            "title": "12 CFR § 1026.36 — Prohibited acts or practices and loan originator provisions",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.36",
            "relevance": "Contains loan-originator rules and conditions relevant to certain seller-financing exclusions; those provisions do not establish a blanket exemption from other duties.",
        },
        {
            "title": "Texas Property Code § 5.016 — Conveyance of residential property encumbered by lien",
            "url": "https://statutes.capitol.texas.gov/Docs/PR/htm/PR.5.htm#5.016",
            "relevance": "Requires review of applicable notice duties, timing, and exceptions when conveying residential property that remains subject to existing liens.",
        },
        {
            "title": "Texas Finance Code Chapter 159 — Wrap mortgage loan financing",
            "url": "https://statutes.capitol.texas.gov/Docs/FI/htm/FI.159.htm",
            "relevance": "Addresses Texas wrap-mortgage licensing, disclosures, borrower protections, and related obligations beyond the property-transfer notice analysis.",
        },
        {
            "title": "12 U.S.C. § 2607 — Prohibition against kickbacks and unearned fees",
            "url": "https://www.law.cornell.edu/uscode/text/12/2607",
            "relevance": "Requires scrutiny of payments tied to referrals of settlement-service business involving covered federally related mortgage loans.",
        },
        {
            "title": "47 CFR § 64.1200 — Restrictions on telemarketing and telephone solicitation",
            "url": "https://www.ecfr.gov/current/title-47/section-64.1200",
            "relevance": "Informs channel-specific review of calls, texts, consent requirements, do-not-call procedures, and suppression practices before outreach.",
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": "Supports accurate sender information, required commercial-message elements, effective opt-out mechanisms, and timely suppression.",
        },
        {
            "title": "12 CFR § 1026.24 — Advertising",
            "url": "https://www.ecfr.gov/current/title-12/section-1026.24",
            "relevance": "Requires review of advertised credit terms, triggering disclosures, and prohibited misleading practices in dwelling-secured credit advertising.",
        },
        {
            "title": "42 U.S.C. § 3604 — Discrimination in the sale or rental of housing",
            "url": "https://www.law.cornell.edu/uscode/text/42/3604",
            "relevance": "Supports consistent housing access, nondiscriminatory advertisements, and exclusion of protected-class targeting from buyer-demand maps.",
        },
        {
            "title": "12 CFR § 1002.9 — Notifications",
            "url": "https://www.ecfr.gov/current/title-12/section-1002.9",
            "relevance": "Governs applicable creditor notification and adverse-action duties; the responsible creditor must manage these obligations rather than leaving them to a marketing CRM.",
        },
    ],
}
