from __future__ import annotations

CHAPTER_6 = {
    "id": "Q6",
    "chapter_id": "Q6",
    "chapter_number": 6,
    "question_number": 6,
    "slug": "sourcing-demand-mining-and-landing-your-first-deals",
    "question_prompt": "Where do high-margin deals, clients, or undervalued assets hide in intellectual property licensing, and what repeatable outbound/inbound sourcing system lands the first 3-to-10 wins (6–24 months)?",
    "kicker": "Q6 / THE BIG MONEY PLAYBOOKS",
    "title": "Sourcing, Demand Mining & Landing Your First Deals",
    "subtitle": "Mine Patent Assignments, Brand Category Gaps, Catalog Rights and Dataset Procurement Signals into Auditable Minimum Guarantees and Royalties",
    "layout_template": "step_by_step_sop",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #19, Intellectual Property Licensing, ranks #13 with a 79/100 "
        "Money-to-Manpower Score. Its four mapped operator plays are patent "
        "commercialization, brand category licensing, catalog reuse, and dataset "
        "licensing. Source demand before accumulating rights: pair public records "
        "with product launches, procurement requirements, and buyer interviews. "
        "A one-founder, three-contractor pod can qualify ownership, scope permitted "
        "uses, negotiate minimum guarantees, and install royalty reporting without "
        "carrying a product company. Annual owner net profit is $12,500 Conservative, "
        "$180,625 Base, and $480,000 Scaled; the scaled team expands to two full-time "
        "people and four contractors. This chapter turns a 6–24 month development "
        "window into a measured sourcing pipeline, separating signed mandates from "
        "paying licenses and licensee sales from operator revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$50,000",
            "context": "Annual gross revenue from license fees and royalties only",
            "note": "25% net margin; $12,500 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Base",
            "value": "$425,000",
            "context": "Annual gross revenue from license fees and royalties only",
            "note": "42.5% net margin; $180,625 annual owner net profit; 1 FT + 3 C",
        },
        {
            "label": "Scaled",
            "value": "$800,000",
            "context": "Annual gross revenue from license fees and royalties only",
            "note": "60% net margin; $480,000 annual owner net profit; 2 FT + 4 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Pair Every Rights-Supply Signal with a Buyer-Side Trigger",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Start with four mapped plays, not a miscellaneous collection of assets: "
                    "patent commercialization, brand category licensing, catalog reuse, and "
                    "dataset licensing. Each play needs a rights source, a buyer trigger, and "
                    "a measurable economic advantage. For patents, inspect university technology "
                    "transfer listings, USPTO Patent Center prosecution records, and Assignment "
                    "Center transfers; pair a relevant asset with an announced product platform "
                    "or engineering bottleneck. For brands, compare trademark registrations and "
                    "owner catalogs with retailers' assortment gaps. For catalogs, match archive "
                    "inventories against publishers' release calendars and producers' reuse "
                    "requirements. For datasets, connect documented collection rights with "
                    "procurement requests describing coverage, freshness, or evaluation needs. "
                    "Create one Airtable record per asset and intended use, rather than one "
                    "record per owner. Capture the source URL, observation date, rights contact, "
                    "territory, likely buyer, trigger date, and unresolved ownership question. "
                    "A patent assignment is a research lead, not proof that every necessary "
                    "right transferred; a downloadable file is not permission to sublicense. "
                    "Reject leads whose only thesis is that intellectual property looks cheap. "
                    "The relevant discount is the gap between an obtainable license and a "
                    "specific buyer's documented cost of delay, substitution, or internal creation."
                ),
                (
                    "Mine intent on the buyer side before seeking broad exclusivity from an "
                    "owner. Read SEC EDGAR product descriptions, company engineering vacancies, "
                    "trade show exhibitor announcements, retailer category plans, and SAM.gov "
                    "solicitations for concrete application language. A robotics launch can "
                    "justify investigating sensing patents; it does not establish infringement. "
                    "A publisher expanding localized editions can justify asking about "
                    "translation and territorial rights; it does not establish budget. For "
                    "datasets, identify required fields, update intervals, provenance evidence, "
                    "and whether buyers need internal analytics, redistribution, or model "
                    "training. Those uses are separate negotiation variables. Record an exact "
                    "quotation from a public source and formulate one falsifiable hypothesis: "
                    "the buyer will pay to obtain a stated capability before a stated "
                    "milestone. Test it in an interview without disclosing restricted asset "
                    "materials. Favor triggers younger than ninety days unless a longer "
                    "procurement cycle is visible. Maintain a suppression field for stale "
                    "triggers, explicit refusals, and already licensed categories. The founder "
                    "reviews twenty new asset-use hypotheses weekly while the diligence "
                    "contractor prepares source packets. Stop adding records when review "
                    "backlogs exceed two weeks; additional names cannot repair weak demand evidence."
                ),
                (
                    "Seek undervalued rights where coordination costs obscure an otherwise "
                    "credible application. University portfolios may have neglected industry "
                    "segments; established brands may lack a manufacturer in one category; "
                    "regional archives may hold well-indexed material without an active licensing "
                    "desk; specialist data owners may serve users manually without a reusable "
                    "license package. Interview the owner about existing grants, reserved "
                    "channels, obligations to funders, restrictions on exclusivity, and willingness "
                    "to support diligence. For federally funded inventions, investigate applicable "
                    "government rights and obligations under 35 U.S.C. §§ 202–204 rather than "
                    "assuming unrestricted exclusivity. Define a narrow first offer covering "
                    "one field, one territory, one buyer class, and a clear expiration. "
                    "Do not purchase a portfolio merely to make outreach sound authoritative. "
                    "Use a documented representation mandate or a conditional rights arrangement "
                    "that specifies who can negotiate and who must sign. Keep owner authorization "
                    "separate from buyer qualification in the CRM. With startup capital of "
                    "$25,000–$250,000 and a 6–24 month first-deal window, avoid tying the entire "
                    "budget to speculative rights acquisition. Reserve capacity for document "
                    "review, buyer evaluation, and reporting setup, because those activities "
                    "convert a promising introduction into a collectible contract."
                ),
            ],
            "table": {
                "caption": "Public-Record and Intent Signals for the Four Mapped Licensing Plays",
                "headers": [
                    "Mapped play and sourcing location",
                    "Buyer trigger worth investigating",
                    "Evidence to capture before outreach",
                    "Failure mode and immediate response",
                ],
                "rows": [
                    [
                        "Patent commercialization through university technology transfer portfolio listings",
                        "Manufacturer announces a product requiring the disclosed technical capability",
                        "Capture patent family identifiers, remaining term, and licensing contact",
                        "Broad abstract misleads buyers; request application-specific technical review first",
                    ],
                    [
                        "Patent commercialization through USPTO Assignment Center transfer records",
                        "Acquirer divests a business while retaining adjacent patent assets",
                        "Collect recorded instruments and investigate omitted co-owners or encumbrances",
                        "Recorded ownership alone is incomplete; reconcile operative transfer documents",
                    ],
                    [
                        "Brand category licensing through USPTO Trademark Search and TSDR",
                        "Retailer expands an assortment where the brand lacks licensees",
                        "Document relevant goods, registration status, owner contacts, and category restrictions",
                        "Recognition lacks purchase intent; test retailer interest before exclusivity",
                    ],
                    [
                        "Catalog reuse through archive inventories and publisher rights desks",
                        "Producer needs dated footage or localized editions before release",
                        "List individual works, contributor releases, territories, and existing grants",
                        "Archive possession masks missing rights; clear each required layer",
                    ],
                    [
                        "Dataset licensing through specialist associations and commercial data owners",
                        "Procurement brief requests missing coverage, refresh frequency, or evaluation access",
                        "Document collection sources, contractual permissions, permitted purposes, and refresh costs",
                        "Access terms prohibit resale; exclude affected records before packaging",
                    ],
                    [
                        "Cross-play demand discovery through EDGAR, SAM.gov, and exhibitor announcements",
                        "Published launch or solicitation exposes a specific capability deadline",
                        "Save dated source excerpts and identify accountable operational buyers",
                        "Public interest lacks budget; verify procurement authority during discovery",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Trade Narrow Rights Packages for Faster Buyer Decisions",
                "body": (
                    "Experienced operators reduce uncertainty before expanding the asset package. "
                    "These tactics improve evidence quality without adding another full-time role."
                ),
                "items": [
                    "Ask university licensing staff which applications have received repeat inquiries but no completed license; investigate why each buyer stalled.",
                    "For brand opportunities, obtain the owner's existing category exclusions before approaching manufacturers, preventing conflicts with incumbent licensees.",
                    "For catalogs, request a rights ledger for ten representative works before evaluating thousands of files; missing contributor documentation often repeats.",
                    "For datasets, offer an authorized, purpose-limited evaluation sample with field definitions and provenance notes rather than circulating the complete asset.",
                ],
            },
        },
        {
            "heading": "2. Score Rights, Demand, and Collection Risk Before Spending",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Use a hundred-point qualification score with six weighted dimensions: "
                    "ownership and licensing authority, twenty-five; buyer urgency, twenty; "
                    "permitted-use fit, twenty; contribution economics, fifteen; implementation "
                    "readiness, ten; and reporting observability, ten. Score evidence, not founder "
                    "enthusiasm. A named buyer with an approved project merits more urgency "
                    "credit than a market-size report. A complete assignment chain earns more "
                    "ownership credit than an owner's verbal assertion. Advance records scoring "
                    "at least seventy-five only when critical defects are resolved; a high "
                    "total cannot compensate for absent licensing authority or prohibited use. "
                    "Keep fifty-five through seventy-four in a targeted research queue, and "
                    "archive lower scores unless a specific missing document could change "
                    "the result. These thresholds are internal operating choices, not measured "
                    "industry averages. The founder owns buyer evidence, the IP counsel "
                    "contractor reviews title and scope, the diligence contractor checks asset "
                    "fitness, and the royalty operations contractor models reporting and "
                    "collection. That is Candidate #19's one-full-time, three-contractor pod. "
                    "Contractor capacity is purchased by deliverable, with work-in-progress "
                    "limits that protect the founder from supervising four different speculative "
                    "negotiations at once. Log every score change with its supporting evidence."
                ),
                (
                    "Build a diligence packet appropriate to each play instead of applying "
                    "a single ownership checklist. Patent packets require family coverage, "
                    "maintenance status, assignment instruments, existing licenses, and a "
                    "technical mapping to the intended application. Under 35 U.S.C. § 261, "
                    "patent assignments require a written instrument; recorded documents "
                    "remain inputs to review rather than a complete title conclusion. Brand "
                    "packets require territory and goods coverage plus workable quality "
                    "standards, sample approvals, and inspection rights supporting controlled "
                    "use under 15 U.S.C. § 1127. Catalog packets separate copyright ownership "
                    "from music, performer, privacy, publicity, and embedded-material rights; "
                    "17 U.S.C. § 204 addresses signed writings for transfers of copyright "
                    "ownership. Dataset packets distinguish copyrightable selection or "
                    "arrangement from underlying facts and separately assess contracts, trade "
                    "secrets, personal information, and source restrictions. Never label raw "
                    "facts exclusively owned simply because someone assembled a spreadsheet. "
                    "If a proposed dataset contains sensitive personal information, pause "
                    "distribution until purpose, access, retention, and applicable requirements "
                    "are resolved. Require the seller to identify precisely what they can "
                    "grant, and require counsel to flag gaps before a buyer receives a "
                    "definitive rights representation."
                ),
                (
                    "Qualify commercial fit through a thirty-minute discovery meeting that "
                    "ends with a named decision and next date. Ask what the buyer would "
                    "build or buy without the license, which use is indispensable, which "
                    "territory generates value, who approves expenditure, and what could "
                    "block deployment after signature. Request a bounded volume estimate "
                    "rather than a flattering total market forecast. For a hypothetical "
                    "royalty, $2 million of eligible licensee product sales at three percent "
                    "produces $60,000 of operator royalty revenue, not $2 million. If a "
                    "$30,000 advance is fully recoupable against that same obligation, total "
                    "royalties remain $60,000 rather than $90,000. Cash timing and revenue "
                    "recognition still depend on contractual performance and the applicable "
                    "accounting treatment. Have the royalty contractor test definitions for "
                    "returns, discounts, bundled products, affiliates, currency conversion, "
                    "and reporting periods. Calculate expected contribution after owner "
                    "participations, specialist review, support, and collection effort. A "
                    "large headline minimum with extensive customization can be inferior "
                    "to a smaller repeatable license. Route unusual engineering or clearance "
                    "burdens back into pricing before presenting terms, and document whether "
                    "the operator acts as licensor or agent so revenue is counted on the "
                    "correct basis."
                ),
            ],
            "table": {
                "caption": "Evidence-Weighted Qualification Scorecard with Non-Negotiable Stop Conditions",
                "headers": [
                    "Dimension and available score weight",
                    "Evidence supporting a strong qualification",
                    "Reason to stop or reduce score",
                    "Accountable pod member and next action",
                ],
                "rows": [
                    [
                        "Ownership and licensing authority receive twenty-five available qualification points",
                        "Executed instruments connect the granting party to requested rights",
                        "Unresolved co-owner interests or prior exclusivity prevent the proposed grant",
                        "IP counsel contractor reconciles documents before definitive rights representations",
                    ],
                    [
                        "Buyer urgency receives twenty available evidence-weighted qualification score points",
                        "Named sponsor confirms funded project timing and decision participants",
                        "General curiosity lacks an application deadline or purchasing authority",
                        "Founder secures dated discovery notes and a specific next decision",
                    ],
                    [
                        "Permitted-use fit receives twenty available evidence-weighted qualification score points",
                        "Requested territory, field, channels, and sublicensing fit documented authority",
                        "Existing agreements exclude required territories or essential downstream uses",
                        "IP counsel contractor narrows scope or records a blocking restriction",
                    ],
                    [
                        "Contribution economics receive fifteen available evidence-weighted qualification score points",
                        "Expected license income covers participations, delivery, support, and collection",
                        "Customization costs consume margin despite an attractive headline payment",
                        "Royalty operations contractor models costs before founder quotes terms",
                    ],
                    [
                        "Implementation readiness receives ten available evidence-weighted qualification score points",
                        "Buyer confirms integration resources and successfully evaluates authorized materials",
                        "Technical dependencies exceed available buyer capability or delivery capacity",
                        "Diligence contractor documents acceptance tests and unresolved implementation dependencies",
                    ],
                    [
                        "Reporting observability receives ten available evidence-weighted qualification score points",
                        "Buyer can export contract-defined sales or usage with traceable identifiers",
                        "Bundled revenue or affiliate transfers cannot be reconciled reliably",
                        "Royalty operations contractor tests sample reports before contract execution",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Verify Four Conditions Before Sending Definitive Terms",
                "body": (
                    "The founder records each decision in the asset-use record. A score "
                    "does not override a failed authority, use, economics, or reporting check."
                ),
                "items": [
                    "Verify the granting party, signed authority, existing grants, co-owner interests, and any security interests affecting the proposed rights.",
                    "Verify exact field, territory, duration, sublicensing permissions, and exclusions against the buyer's actual deployment plan.",
                    "Verify a named budget owner, measurable buyer benefit, delivery costs, and a minimum payment structure the pod can support.",
                    "Verify sample reporting, royalty definitions, audit access, payment mechanics, and practical remedies for missing or inaccurate reports.",
                ],
            },
        },
        {
            "heading": "3. Run a Permissioned Outreach Cadence and Measure Real Conversion",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Operate two coordinated queues: owners who can authorize a package, "
                    "and buyers whose projects can absorb it. Do not imply that an owner "
                    "has retained the operator before the mandate is signed. Start buyer "
                    "research with a neutral problem interview, then use authorized materials "
                    "once representation is documented. A practical fifteen-business-day "
                    "cadence begins with a short email on day one citing the public trigger, "
                    "a narrowly relevant capability, and one question. On day four, send "
                    "a professional-network connection request without attaching restricted "
                    "materials. On day eight, offer a one-page rights brief through the "
                    "established channel. On day twelve, call a published business number "
                    "when appropriate; on day fifteen, send a concise close-the-loop message "
                    "and stop unless the recipient engages. Honor refusals across channels. "
                    "Commercial email must follow applicable requirements under 15 U.S.C. "
                    "§ 7704, including accurate headers, nondeceptive subjects, required "
                    "identification, a valid postal address, and a working opt-out mechanism. "
                    "Use HubSpot suppression lists and dated CRM tasks rather than purchased "
                    "bulk sequences. The founder personally handles replies because early "
                    "objections reveal whether the asset, use case, or buyer selection is "
                    "wrong. Delegate preparation, not judgment."
                ),
                (
                    "Use a cohort model to plan capacity, then replace assumptions with "
                    "observed results. An illustrative 6–24 month cohort starts with two "
                    "hundred raw asset-use leads, of which eighty have credible rights and "
                    "demand evidence, forty produce two-way conversations, twenty reach "
                    "qualified discovery, twelve request a scoped evaluation or terms, "
                    "eight enter substantive negotiation, and five sign paying licenses. "
                    "The corresponding stage conversions are forty percent, fifty percent, "
                    "fifty percent, sixty percent, roughly sixty-seven percent, and roughly "
                    "sixty-three percent; overall conversion is two and one-half percent. "
                    "These are planning benchmarks, not historical results or expected "
                    "market performance. Count each lead once, tie multiple contacts to "
                    "one opportunity, and distinguish an owner mandate from a paying buyer "
                    "license. A signed mandate establishes authority but does not establish "
                    "license revenue. Track days in stage, reasons lost, and overdue next "
                    "actions alongside conversion. Below-target replies suggest poor "
                    "targeting or weak relevance; strong discovery with weak evaluation "
                    "suggests unclear rights or poor asset fit; stalled negotiations suggest "
                    "economic, reporting, or scope friction. Do not solve every shortfall "
                    "by increasing message volume. Review the oldest five opportunities "
                    "weekly and either schedule a buyer decision or return them to nurture."
                ),
                (
                    "Build inbound around evidence buyers can inspect without receiving "
                    "the underlying restricted asset. Publish one authorized application "
                    "brief per active play, describing permitted uses, excluded uses, "
                    "territory, delivery format, evaluation process, and reporting requirements. "
                    "A patent brief should describe the problem and application without "
                    "asserting that prospects infringe. A brand brief should show approved "
                    "category concepts rather than imply unrestricted endorsement. Catalog "
                    "previews require appropriate display permission; dataset previews "
                    "should use authorized samples or clearly labeled synthetic examples. "
                    "Place these briefs where demand already gathers: university licensing "
                    "directories, relevant trade associations, industry newsletters, and "
                    "owner-approved website pages. Offer a scheduled technical clinic "
                    "instead of a vague contact form. Ask inbound prospects for their "
                    "intended use, territory, launch date, budget range, and reporting "
                    "capability before allocating specialist time. Handle objections by "
                    "isolating the disputed variable. For price, compare scoped alternatives "
                    "and reduce breadth rather than automatically discounting. For rights "
                    "concerns, provide the relevant diligence evidence under suitable "
                    "confidentiality terms. For evaluation requests, define access limits, "
                    "success criteria, and an expiration. For exclusivity, trade a narrow "
                    "field and measurable performance commitments rather than surrendering "
                    "every future market for one uncertain buyer."
                ),
            ],
            "table": {
                "caption": "First-Deal Conversion Benchmarks and Objection-Handling Responses",
                "headers": [
                    "Stage or objection requiring intervention",
                    "Evidence or illustrative conversion benchmark",
                    "Specific response within the four-person pod",
                    "Exit condition recorded in the CRM",
                ],
                "rows": [
                    [
                        "Raw sourcing advances into evidence-qualified asset and use records",
                        "Two hundred raw records yield eighty qualified records in this model",
                        "Diligence contractor links source evidence and founder validates buyer relevance",
                        "Rights and demand evidence support a specific outreach hypothesis",
                    ],
                    [
                        "Qualified records advance into conversations and documented discovery meetings",
                        "Eighty qualified records yield forty conversations and twenty discoveries",
                        "Founder tests urgency, purchasing authority, and the buyer's practical alternative",
                        "Named sponsor accepts a dated next decision with clear scope",
                    ],
                    [
                        "Discovery advances through evaluation, negotiation, and signed paying licenses",
                        "Twenty discoveries yield twelve evaluations, eight negotiations, five licenses",
                        "Pod resolves the highest-impact rights, delivery, or reporting obstacle",
                        "Executed buyer license and payment setup satisfy documented completion criteria",
                    ],
                    [
                        "Buyer objects that pricing exceeds their available project budget",
                        "Buyer identifies budget owner, alternative cost, and essential deployment scope",
                        "Founder narrows territory, field, duration, or support before discounting",
                        "Revised scope preserves contribution and receives a dated buyer response",
                    ],
                    [
                        "Buyer questions ownership or requests unrestricted access before evaluation",
                        "Buyer specifies missing rights evidence or necessary technical acceptance tests",
                        "Counsel supplies targeted evidence while diligence contractor controls sample access",
                        "Evaluation agreement defines permitted access, success criteria, and expiration",
                    ],
                    [
                        "Buyer demands broad exclusivity without committing meaningful minimum payments",
                        "Buyer explains competitive need and provides supportable deployment assumptions",
                        "Founder offers field-limited exclusivity tied to negotiated performance obligations",
                        "Contract defines scope, minimums, reporting, and consequences of underperformance",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Create an evidence-linked sourcing cohort",
                    "action": "Enter twenty asset-use hypotheses weekly across the four mapped plays.",
                    "detail": (
                        "Record the public trigger, source date, rights contact, buyer role, "
                        "specific use, and next research question; stop intake when review "
                        "work exceeds the pod's two-week capacity."
                    ),
                },
                {
                    "step": 2,
                    "title": "Qualify authority and buyer urgency",
                    "action": "Apply the hundred-point score and resolve all critical defects.",
                    "detail": (
                        "Founder checks demand; counsel checks authority and scope; diligence "
                        "contractor checks fitness; royalty operations contractor checks unit "
                        "economics and reportability."
                    ),
                },
                {
                    "step": 3,
                    "title": "Run the five-touch sourcing sequence",
                    "action": "Use days one, four, eight, twelve, and fifteen for relevant outreach.",
                    "detail": (
                        "Personalize around a documented trigger, use authorized materials, "
                        "honor channel restrictions and opt-outs, and end the sequence "
                        "without escalating pressure when the prospect does not engage."
                    ),
                },
                {
                    "step": 4,
                    "title": "Convert evaluation into a scoped license",
                    "action": "Attach acceptance criteria, commercial terms, and a sample royalty report.",
                    "detail": (
                        "Schedule a buyer decision, obtain the correct signatures, verify "
                        "payment setup, and assign obligation tracking before counting "
                        "the opportunity as a signed paying license."
                    ),
                },
            ],
        },
        {
            "heading": "4. Land Three-to-Ten Wins Without Losing Revenue Discipline",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use the first three licenses to establish repeatability rather than "
                    "maximize the number of different asset types under management. The "
                    "four mapped plays define the sourcing universe, but the founder "
                    "should concentrate delivery on whichever one or two produce the "
                    "strongest qualified demand. During months one through three, assemble "
                    "rights evidence and conduct buyer discovery; during months four "
                    "through six, seek mandates and bounded evaluations; during months "
                    "six through twenty-four, convert qualified opportunities into paying "
                    "licenses as diligence and procurement permit. These phases overlap "
                    "and do not establish a promised closing date. Make evaluation access "
                    "purpose-limited, time-limited, and distinct from production rights. "
                    "The definitive agreement should state licensed rights, exclusions, "
                    "territory, duration, deliverables, payment obligations, reporting, audit "
                    "procedures, renewal, termination, and treatment of retained materials. "
                    "Brand agreements additionally need operational quality controls. "
                    "Have counsel assess exclusivity, territorial restrictions, tying, and "
                    "other competitive restraints under applicable competition law, "
                    "including 15 U.S.C. § 1; intellectual property does not create "
                    "automatic immunity for restrictive arrangements. Do not let a buyer's "
                    "requested launch date erase unresolved authority or reporting questions. "
                    "A delayed clean grant is more useful than a rapid signature the "
                    "operator cannot properly administer."
                ),
                (
                    "Reconcile the scorecard with earned license economics, not licensee "
                    "turnover or the face value of multiyear contracts. Conservative annual "
                    "gross revenue is $50,000; at a twenty-five percent net margin, costs "
                    "are $37,500 and owner net profit is $12,500. An illustrative three-win "
                    "allocation is $15,000, $15,000, and $20,000 of annual recognized revenue. "
                    "Base annual gross revenue is $425,000; at a forty-two and one-half "
                    "percent net margin, costs are $244,375 and owner net profit is "
                    "$180,625. Five licenses contributing $85,000 each illustrate that "
                    "revenue total. Scaled annual gross revenue is $800,000; at a sixty "
                    "percent net margin, costs are $320,000 and owner net profit is "
                    "$480,000. Ten licenses contributing $80,000 each illustrate the "
                    "scaled total. These allocations are scenario decompositions, not "
                    "recommended prices or predicted first-year receipts. Count advances "
                    "and minimum guarantees consistently with their recoupment and "
                    "recognition treatment, never twice. If the operator merely represents "
                    "an owner as agent, count the operator's earned fee rather than "
                    "passing the owner's entire receipt through the scorecard. Keep the "
                    "Conservative and Base teams at one full-time person plus three "
                    "contractors; Scaled uses two full-time people plus four contractors."
                ),
                (
                    "Install collection and renewal mechanics before the first reporting "
                    "period closes. The royalty operations contractor maps contract "
                    "definitions to a CSV template with license identifier, reporting "
                    "period, product or dataset identifier, territory, eligible sales "
                    "or usage, permitted deductions, rate, currency, and amount due. "
                    "Test one sample report against source records and record the "
                    "reconciliation method. Use Airtable or HubSpot for obligation "
                    "dates, QuickBooks Online for invoices and cash matching, and "
                    "calendar alerts for renewals and audit windows. Automation should "
                    "surface exceptions rather than silently accept every submitted "
                    "number. Flag missing periods, unexplained deduction increases, "
                    "territory mismatches, and usage growth without corresponding "
                    "royalties. Store contract versions and supporting reports with "
                    "access restricted to the pod members who need them. After each "
                    "close, obtain permission before publishing a case study or naming "
                    "the licensee; confidential terms remain private. Ask satisfied "
                    "buyers and owners for one adjacent introduction tied to the "
                    "same use case. Expand toward ten wins only when existing "
                    "reporting arrives reliably, renewals have accountable owners, "
                    "and exception work fits available contractor hours. A sourcing "
                    "system becomes high-margin when every new contract reuses "
                    "proven evidence, negotiation boundaries, and collection routines."
                ),
            ],
            "table": {
                "caption": "Canonical Annual Economics and First-License Operating Controls",
                "headers": [
                    "Scenario or operating control",
                    "Recognized operator revenue and economic boundary",
                    "Cost, profit, or verification requirement",
                    "Team ownership and execution constraint",
                ],
                "rows": [
                    [
                        "Conservative annual case supports three illustrative paying license relationships",
                        "$50,000 annual gross revenue excludes underlying licensee product sales",
                        "$37,500 total costs leave $12,500 profit at 25% margin",
                        "One full-time founder and three contractors administer narrowly scoped rights",
                    ],
                    [
                        "Base annual case supports five illustrative paying license relationships",
                        "$425,000 annual gross revenue equals five illustrative $85,000 contributions",
                        "$244,375 total costs leave $180,625 profit at 42.5% margin",
                        "One full-time founder and three contractors reuse established delivery processes",
                    ],
                    [
                        "Scaled annual case supports ten illustrative paying license relationships",
                        "$800,000 annual gross revenue equals ten illustrative $80,000 contributions",
                        "$320,000 total costs leave $480,000 profit at 60% margin",
                        "Two full-time people and four contractors support six-person operating capacity",
                    ],
                    [
                        "Recoupable advances must reconcile against the same royalty obligation",
                        "$2 million eligible licensee sales at 3% produce $60,000 royalties",
                        "$30,000 recoupable advance does not increase total royalties to $90,000",
                        "Royalty operations contractor separates collections, earned amounts, and remaining balances",
                    ],
                    [
                        "Monthly operating range must remain distinct from total annual costs",
                        "$2,000–$15,000 monthly operating range is a separate planning input",
                        "Reconcile owner participations, variable delivery costs, and other scenario expenses",
                        "Founder maintains runway against the $25,000–$250,000 startup capital range",
                    ],
                    [
                        "Renewal and royalty exceptions require evidence-backed follow-up before expansion",
                        "Contract-defined reports support invoices rather than unverified buyer projections",
                        "Reconcile deductions, territories, usage, currency, and missing reporting periods",
                        "Royalty operations contractor escalates exceptions while founder manages commercial resolution",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "Source the buyer's deadline before the asset, and sell only the rights you can prove and administer.",
    "diagram_id": "diag-02",
    "action_checklist": [
        "Create four sourcing views for patent commercialization, brand category licensing, catalog reuse, and dataset licensing, with one record per asset and intended use.",
        "Pair twenty weekly sourcing hypotheses with dated public triggers, named buyer roles, source links, rights contacts, and explicit next research questions.",
        "Apply the hundred-point qualification score and document authority, permitted use, contribution economics, and reporting readiness before issuing definitive terms.",
        "Run the fifteen-business-day outreach cadence with authorized briefs, suppression controls, dated next actions, and separate tracking for mandates and paying licenses.",
        "Negotiate bounded evaluations and scoped licenses with precise minimums, recoupment rules, quality controls where relevant, reporting definitions, and audit procedures.",
        "Reconcile the first three-to-ten wins to canonical annual revenue and profit cases, then automate renewal alerts and royalty exceptions before expanding workload.",
    ],
    "statutory_citations": [
        {
            "title": "35 U.S.C. § 261 — Ownership; assignment",
            "url": "https://www.law.cornell.edu/uscode/text/35/261",
            "relevance": (
                "Requires written instruments for patent assignments and addresses "
                "recording and priority issues; supports document-based title review "
                "rather than reliance on a portfolio listing."
            ),
        },
        {
            "title": "35 U.S.C. § 202 — Disposition of rights",
            "url": "https://www.law.cornell.edu/uscode/text/35/202",
            "relevance": (
                "Establishes rights and conditions concerning federally funded subject "
                "inventions, including retained government rights that can affect "
                "university patent licensing diligence."
            ),
        },
        {
            "title": "35 U.S.C. § 204 — Preference for United States industry",
            "url": "https://www.law.cornell.edu/uscode/text/35/204",
            "relevance": (
                "Addresses domestic manufacturing commitments for certain exclusive "
                "licenses to use or sell subject inventions in the United States, "
                "with an agency waiver mechanism."
            ),
        },
        {
            "title": "17 U.S.C. § 106 — Exclusive rights in copyrighted works",
            "url": "https://www.law.cornell.edu/uscode/text/17/106",
            "relevance": (
                "Identifies distinct exclusive rights that catalog packages must "
                "map to the buyer's reproduction, adaptation, distribution, "
                "performance, or display requirements."
            ),
        },
        {
            "title": "17 U.S.C. § 204 — Execution of transfers of copyright ownership",
            "url": "https://www.law.cornell.edu/uscode/text/17/204",
            "relevance": (
                "Requires a signed writing for transfers of copyright ownership "
                "other than transfers by operation of law; supports review of "
                "catalog assignments and exclusive grants."
            ),
        },
        {
            "title": "15 U.S.C. § 1127 — Trademark definitions and related-company use",
            "url": "https://www.law.cornell.edu/uscode/text/15/1127",
            "relevance": (
                "Defines related-company use by reference to owner control over "
                "the nature and quality of goods or services, informing practical "
                "brand quality-control provisions."
            ),
        },
        {
            "title": "15 U.S.C. § 1 — Restraints of trade",
            "url": "https://www.law.cornell.edu/uscode/text/15/1",
            "relevance": (
                "Provides the statutory basis for evaluating contractual restraints "
                "that may arise in exclusivity, territorial allocation, tying, "
                "and other licensing arrangements."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Governs commercial email practices including header accuracy, "
                "subject lines, identification, postal addresses, and opt-out "
                "handling in the sourcing cadence."
            ),
        },
    ],
}
