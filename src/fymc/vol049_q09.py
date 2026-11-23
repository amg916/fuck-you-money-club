from __future__ import annotations

CHAPTER_9 = {
    "id": "Q9",
    "chapter_id": "Q9",
    "chapter_number": 9,
    "question_number": 9,
    "slug": "contracts-statutory-guardrails-licensing-outreach-scripts",
    "question_prompt": "Which federal/state statutes, licensing boundaries, contract clauses, and compliant outreach scripts govern regulated prediction-market terminals & licensed igaming affiliates?",
    "kicker": "Q9 / THE BIG MONEY PLAYBOOKS",
    "title": "Contracts, Statutory Guardrails, Licensing & Outreach Scripts",
    "subtitle": "CFTC Publisher Boundaries, NJ/PA/MI Affiliate Permissions, Auditable CPA/NGR Contracts, and Permission-Based Partner Scripts",
    "layout_template": "legal_compliance_notes",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #49, Regulated Prediction-Market Terminals & Licensed iGaming Affiliates, "
        "holds Rank #18 of 49 with a 91/100 Money-to-Manpower Score. Its 12 mapped plays "
        "combine non-custodial analytics, permitted referral software, licensed affiliate distribution, "
        "and evidence-backed settlement. The operating boundary matters more than the interface: "
        "publishing probabilities does not automatically exempt solicitation, personalized advice, or "
        "order activity from registration. Separate SaaS revenue from state-authorized CPA and NGR "
        "commissions, contract every deduction, and suppress prohibited destinations. Canonical annual "
        "owner profit is $19,500 Conservative, $137,750 Base, and $325,000 Scaled. This chapter "
        "turns federal definitions, jurisdiction-specific permissions, commercial clauses, hosted-publication "
        "placements, and verbatim outreach into a reproducible system that preserves attribution evidence "
        "without taking custody or confusing player activity with operator revenue."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$75,000",
            "context": "Annual operator revenue; excludes player stakes and trading volume",
            "note": "26% net margin; $19,500 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$362,500",
            "context": "Annual operator revenue; affiliate commissions measured after contractual deductions",
            "note": "38.0% net margin; $137,750 owner profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$650,000",
            "context": "Annual operator revenue; SaaS, permitted rebates, and earned affiliate fees",
            "note": "50% net margin; $325,000 owner profit; 2 FT + 3 C",
        },
    ],
    "sections": [
        {
            "heading": "1. Classify every feature before selling access or referrals",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Build two product lanes with separate contracts, ledgers, destination policies, and "
                    "release records. Lane A sells non-custodial event-contract analytics and only those "
                    "builder referrals expressly permitted by the relevant venue and applicable law. "
                    "Lane B earns commissions from appropriately licensed sportsbook and casino operators "
                    "where the affiliate has the required permissions. For this chapter, the 12 mapped "
                    "implementation plays are subscription terminals, cross-venue probability comparisons, "
                    "positive-EV alerts, historical research exports, permitted builder referrals, licensed "
                    "CPA comparisons, NGR revenue sharing, geofenced attribution, owned-email education, "
                    "permission-based SMS alerts, partner API distribution, and parasitic_seo. These are "
                    "operating mappings, not assertions that every feature is authorized everywhere. Label "
                    "each feature with its payer, user action, compensation basis, destination, and license "
                    "dependency. A monthly research subscription differs materially from compensation tied "
                    "to customer trading, even when both appear behind the same button. Never accept "
                    "deposits, pool capital, take withdrawal credentials, or direct US users to unlicensed "
                    "offshore or crypto venues or unlawful sweepstakes casinos. Maintain a feature inventory "
                    "that distinguishes publishing, promotion, introductions, recommendations, and transaction "
                    "handling. Assign an accountable owner to each classification and attach the evidence "
                    "supporting its permitted scope before charging customers."
                ),
                (
                    "Apply the Commodity Exchange Act to conduct rather than marketing labels. Under "
                    "7 U.S.C. § 1a(12), compensated advice and analysis about covered commodity interests "
                    "can implicate commodity trading adviser status; publisher exclusions and the regular-business "
                    "conditions require a fact-specific examination. Registration obligations and exemptions "
                    "also require analysis under 7 U.S.C. § 6m and 17 CFR § 4.14. Do not treat "
                    "a general research label as permission to deliver individualized trade instructions. "
                    "The introducing broker definition in 7 U.S.C. § 1a(31) matters because an IB "
                    "can solicit or accept orders without accepting customer funds. Non-custody therefore "
                    "does not resolve the registration question. The futures commission merchant definition "
                    "in § 1a(28) addresses additional conduct involving customer money or property. Before "
                    "adding account-linked alerts, referral compensation, prefilled tickets, or order connectivity, "
                    "obtain a written classification covering the actual workflow and compensation. Verify "
                    "Kalshi and ForecastEx permissions through current official venue documentation and agreements; "
                    "a venue's regulated status does not authorize every intermediary activity. If classification "
                    "remains unresolved, retain general research and remove the affected referral or transaction "
                    "feature. Record the removed capability in the release manifest so engineering cannot "
                    "silently restore it through a configuration change."
                ),
                (
                    "Translate market-data permissions into enforceable system behavior. A WebSocket connection "
                    "does not itself grant rights to redistribute quotes, retain historical snapshots, train "
                    "models, or sell derived feeds. Negotiate those uses separately for each source, including "
                    "termination access and archival evidence needed for customer disputes. A sub-second engine "
                    "should record exchange timestamps, local receipt timestamps, market status, and processing "
                    "lag; it should not advertise executable cross-venue arbitrage when settlement definitions, "
                    "fees, position limits, or available depth differ. Positive-EV labels need an explicit "
                    "model version, price timestamp, fee assumption, and explanation that estimated probability "
                    "can be wrong. Keep API secrets server-side and request the least privileged scope "
                    "available; exclude trading and withdrawal authority from analytics integrations. Test a "
                    "stale-feed fallback that disables actionable price comparisons while preserving historical "
                    "research. For example, 120 subscriptions at $100 monthly produce $144,000 annual subscription "
                    "revenue regardless of whether subscribers collectively trade $1 million or $100 million. "
                    "If a builder arrangement separately pays $18,500 annually, recognize only the earned "
                    "contractual software or referral amount after assessing its conditions. Neither user "
                    "turnover nor hypothetical trading gains enter the publisher's revenue ledger. This separation "
                    "also makes cancellation, access suspension, and revenue reconciliation independently testable."
                ),
            ],
            "table": {
                "caption": "Federal Feature Classification and Venue-Permission Evidence Matrix",
                "headers": [
                    "Feature and commercial purpose",
                    "Authority or governing boundary",
                    "Evidence retained before activation",
                    "Fallback when permission is absent",
                ],
                "rows": [
                    [
                        "Sell general probability research through recurring subscriptions",
                        "Assess CTA definitions under 7 U.S.C. § 1a(12)",
                        "Retain feature descriptions and written classification reasoning",
                        "Remove individualized recommendations while preserving general research",
                    ],
                    [
                        "Receive compensation for permitted venue referral software",
                        "Assess IB conduct under 7 U.S.C. § 1a(31)",
                        "Retain compensation terms and solicitation workflow analysis",
                        "Disable compensated referrals until classification is resolved",
                    ],
                    [
                        "Exclude deposits and withdrawals from every integration",
                        "Assess FCM conduct under 7 U.S.C. § 1a(28)",
                        "Retain permission scopes and customer credential exclusions",
                        "Offer public research without linked customer accounts",
                    ],
                    [
                        "Distribute live quotes inside paid customer terminals",
                        "Enforce source contracts governing commercial market-data redistribution",
                        "Retain executed licenses specifying display and derived uses",
                        "Use expressly licensed delayed or historical datasets",
                    ],
                    [
                        "Publish model-based probability and positive-EV research alerts",
                        "Evaluate adviser status and exemption conditions separately",
                        "Retain model assumptions and dated registration analysis",
                        "Suspend affected alerts and retain descriptive market summaries",
                    ],
                    [
                        "Link customers toward currently permitted regulated destinations",
                        "Check venue status and current jurisdictional restrictions",
                        "Retain dated destination records and permitted audience definitions",
                        "Suppress destination links when eligibility cannot be established",
                    ],
                    [
                        "Export historical research for independent customer analysis",
                        "Apply contractual retention and downstream distribution limitations",
                        "Retain dataset provenance and customer export entitlements",
                        "Supply aggregate research that respects licensed usage rights",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four release checks before monetized traffic",
                "body": (
                    "A feature is ready only when its legal classification, commercial permission, "
                    "technical behavior, and accounting treatment describe the same activity."
                ),
                "items": [
                    "Attach written CTA/IB/FCM classification to the actual interface, compensation schedule, and credential scopes; recheck after material changes.",
                    "Verify each destination's current authorization and each required affiliate credential for the specific product and jurisdiction.",
                    "Exercise stale-price, location-failure, age-screen, and prohibited-destination suppression paths using recorded test cases.",
                    "Reconcile one subscription, one qualifying CPA event, and one NGR statement without counting customer stakes as operator revenue.",
                ],
            },
        },
        {
            "heading": "2. Turn jurisdiction differences into executable distribution rules",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Create a jurisdiction register at the product level, not merely the brand level. "
                    "New Jersey internet gaming and sports wagering operate under distinct statutory provisions "
                    "and Division of Gaming Enforcement rules; vendor classification depends on services and "
                    "compensation, not the affiliate's preferred title. Review N.J.S.A. 5:12-92 and N.J.A.C. "
                    "13:69J for vendor obligations, together with the applicable internet gaming and sports "
                    "wagering provisions. Pennsylvania combines the Pennsylvania Race Horse Development and Gaming "
                    "Act with specific interactive gaming and sports wagering requirements; obtain the Pennsylvania "
                    "Gaming Control Board's applicable supplier or vendor determination. Michigan separately regulates "
                    "internet gaming under MCL 432.301 et seq. and internet sports betting under MCL "
                    "432.401 et seq.; record the Michigan Gaming Control Board classification for the "
                    "services actually supplied. West Virginia requires its own product and supplier analysis "
                    "rather than inheriting neighboring permissions. Ontario is a separate country and regulatory "
                    "system involving AGCO standards and the operator's iGaming Ontario arrangements. Do not "
                    "describe an Ontario registration as US authorization. For every destination, record the "
                    "operator entity, product, credential requirement, permitted traffic source, approval evidence, "
                    "renewal date, and responsible contact. Missing evidence suppresses monetized distribution "
                    "rather than creating an assumed permission."
                ),
                (
                    "Use a 21-plus access policy across this volume's acquisition funnel, while accurately "
                    "distinguishing that commercial choice from each jurisdiction's statutory age. Ontario generally "
                    "uses 19 for regulated internet casino and sports betting participation; a stricter "
                    "publisher policy does not change that rule. A birth-year screen and IP lookup "
                    "are preliminary filters, not operator-grade identity verification or wagering geolocation. The "
                    "licensed operator remains responsible for its required identity, exclusion, and location "
                    "checks, while the affiliate must satisfy its own advertising and distribution duties. "
                    "Configure server-side destination rules by jurisdiction, product, device signal quality, and "
                    "campaign permission; fail closed when a monetized destination cannot be validated. "
                    "Do not use VPN troubleshooting to help people bypass location restrictions. Present "
                    "appropriate responsible-gaming resources and current local helpline disclosures next to "
                    "commercial calls to action, not solely in a remote footer. Keep state-specific "
                    "templates because required wording and resources can change. Block youth-oriented placements "
                    "and audiences, prohibit claims of income replacement, and avoid messaging that encourages "
                    "recovering losses. Preserve template versions and campaign screenshots so a later reviewer "
                    "can reconstruct what the audience actually saw, including the destination and disclosure "
                    "visible on mobile devices."
                ),
                (
                    "Separate federal truth-in-advertising requirements from channel-specific permission rules. Section "
                    "5 of the FTC Act, 15 U.S.C. § 45, prohibits deceptive commercial practices; "
                    "16 CFR Part 255 explains endorsement principles, including clear disclosure of material "
                    "connections. Put an affiliate-compensation statement beside rankings and outbound links, and "
                    "explain whether payment affects ordering. Quantified win-rate, return, speed, and ranking "
                    "claims need evidence matching the stated population and period. Commercial email must "
                    "satisfy CAN-SPAM, including accurate headers, a valid postal address, and an effective "
                    "opt-out honored within ten business days. Do not assume that receiving a business "
                    "card authorizes promotional texts. Automated calls and texts require a separate analysis "
                    "under 47 U.S.C. § 227 and 47 CFR § 64.1200, including applicable permission, "
                    "revocation, and do-not-call requirements. Ontario campaigns also require Canadian anti-spam "
                    "and local marketing analysis; a US email process is not automatically portable. "
                    "Collect only attribution fields needed to establish eligibility and payment, with defined "
                    "retention and deletion rules. Send pseudonymous event identifiers rather than raw player "
                    "identity documents. When rules conflict with a partner's growth request, narrow the "
                    "audience or remove the channel instead of weakening evidence collection."
                ),
            ],
            "table": {
                "caption": "Jurisdiction, Advertising, and Channel Deployment Matrix",
                "headers": [
                    "Jurisdiction or distribution channel",
                    "Concrete authority and operating issue",
                    "Required operating record and control",
                    "Practical restriction or recovery action",
                ],
                "rows": [
                    [
                        "New Jersey casino and sportsbook affiliate distribution",
                        "Apply N.J.S.A. 5:12-92 and relevant DGE vendor rules",
                        "Document service classification and required credentials before activation",
                        "Suspend affected destinations when credential evidence expires",
                    ],
                    [
                        "Pennsylvania interactive gaming and sports wagering acquisition",
                        "Apply 4 Pa.C.S. gaming provisions and PGCB requirements",
                        "Document product-specific supplier or vendor classification decisions",
                        "Keep casino and sportsbook permissions independently configurable",
                    ],
                    [
                        "Michigan internet gaming and internet sports betting",
                        "Apply MCL 432.301 and 432.401 statutory frameworks",
                        "Document MGCB classification and permitted operator relationships",
                        "Disable campaigns exceeding approved services or compensation",
                    ],
                    [
                        "West Virginia casino and sports wagering promotion",
                        "Apply W. Va. Code chapters 29-22D and 29-22E",
                        "Document product-specific operator authority and supplier requirements",
                        "Avoid treating another state's permission as transferable",
                    ],
                    [
                        "Ontario regulated internet gaming and sportsbook promotion",
                        "Apply Ontario gaming law and applicable AGCO standards",
                        "Record operator status and restrictions on inducement advertising",
                        "Use separate Canadian campaigns and jurisdiction-specific templates",
                    ],
                    [
                        "Commercial email promoting subscriptions or affiliate comparisons",
                        "Apply 15 U.S.C. § 7704 message requirements",
                        "Retain sender identity and dated suppression processing evidence",
                        "Stop messages to opted-out recipients across vendors",
                    ],
                    [
                        "Promotional text messages and automated telephone outreach",
                        "Apply 47 U.S.C. § 227 and implementing rules",
                        "Retain permission provenance and synchronized revocation records",
                        "Do not launch purchased-list texting without sufficient authorization",
                    ],
                ],
            },
        },
        {
            "heading": "3. Contract the fee waterfall and reconcile every profit case",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "Use separate schedules for software services and gaming acquisition. Define scope, "
                    "territory, approved domains, eligible products, prohibited conduct, and change-control responsibilities. "
                    "For CPA, define a first-time depositor with measurable requirements: new eligible account, "
                    "verified identity, qualifying deposit, any lawful qualifying activity, attribution window, duplicate "
                    "policy, and fraud exclusions. State whether payment depends on acceptance, settlement, "
                    "or another specified event, and place a deadline on rejection with reason codes. "
                    "For NGR, enumerate the starting measure and every permitted deduction rather than "
                    "accepting an expandable administration category. Specify bonus treatment, gaming taxes, payment "
                    "costs, chargebacks, negative carryover, cross-product netting, and termination-tail commissions. A "
                    "bounded anti-circumvention clause should protect identified introductions for a stated period "
                    "without claiming ownership of all operator customers. Require itemized statements, reasonable "
                    "audit access, payment dates, currency, and a dispute window long enough to inspect "
                    "cohort evidence. Define ownership of publisher code, original editorial work, event schemas, "
                    "and licensed source material. Allocate liability by responsibility, negotiate a meaningful "
                    "cap with express exceptions, and specify governing law, forum, escalation, and emergency "
                    "relief. Do not accept unilateral fee changes that retroactively rewrite already qualified "
                    "events or completed service periods."
                ),
                (
                    "Reconcile the canonical Formula v2.0 outcomes before inventing a growth narrative. "
                    "Conservative revenue of $75,000 less $55,500 costs produces $19,500 owner profit "
                    "and a 26% margin. Base revenue of $362,500 less $224,750 costs produces "
                    "$137,750 and 38.0%. Scaled revenue of $650,000 less $325,000 costs produces "
                    "$325,000 and 50%. Staffing remains 1 FT + 2 C, 1 FT + 2 C, "
                    "and 2 FT + 3 C respectively. An illustrative allocation, not an additional "
                    "scorecard assumption, assigns Conservative revenue to $45,000 subscriptions, $6,000 permitted "
                    "builder fees, and $24,000 earned affiliate commissions. Base assigns $144,000, $18,500, "
                    "and $200,000; Scaled assigns $240,000, $30,000, and $380,000. Each allocation "
                    "sums exactly to its canonical total. Assess ASC 606 principal-versus-agent treatment "
                    "for each contractual promise; the scorecard's gross-revenue label does not mean gross "
                    "player deposits, sportsbook handle, or casino stakes. Affiliate revenue is the operator's "
                    "earned commission after contractual revenue-share deductions, with applicable reversals and "
                    "variable-consideration constraints. No numerical retained_share factor is supplied here, so "
                    "do not fabricate one or multiply an already net commission by another retention "
                    "percentage. Keep pass-through amounts outside recognized operator revenue when the accounting "
                    "assessment requires net presentation."
                ),
                (
                    "A reproducible Base affiliate bridge uses 500 accepted FTDS at $300 each "
                    "for $150,000 CPA revenue, with FTD defined in the contract as first-time "
                    "depositor. A separate illustrative revenue-share cohort generates $300,000 contractual gross "
                    "gaming revenue, less $50,000 bonuses, $30,000 administration charges, and $20,000 "
                    "specified gaming taxes, leaving $200,000 NGR. A 30% share yields $60,000; "
                    "a contractually defined $10,000 commission-account carryover reduces payable earned commissions "
                    "to $50,000. Do not subtract that carryover from NGR instead unless the "
                    "contract defines that different method. Total affiliate revenue is $200,000. Deduct "
                    "$60,000 attributable CAC and $40,000 affiliate operating expense to produce $100,000 "
                    "contribution, a 50% affiliate margin. The separate $162,500 software and builder "
                    "lane bears $124,750 expense, producing $37,750; combined profit is the canonical "
                    "$137,750. Expense allocations must reconcile once, without duplicating shared payroll. "
                    "Stress the same model for post-NFL budget cuts: losing 100 accepted CPA "
                    "events removes $30,000 revenue. With unchanged costs, profit falls to $107,750; "
                    "that is a sensitivity, not a replacement Base case. If NGR deductions "
                    "expand or carryover persists, suspend paid acquisition, negotiate cohort isolation, and "
                    "favor subscriptions with measurable retention instead of buying more low-quality deposits."
                ),
            ],
            "table": {
                "caption": "Commercial Clause Checklist and Settlement Evidence Matrix",
                "headers": [
                    "Clause and negotiated commercial purpose",
                    "Specific language requirement to capture",
                    "Evidence used during monthly settlement",
                    "Failure response and economic consequence",
                ],
                "rows": [
                    [
                        "Scope separates analytics subscriptions from gaming acquisition",
                        "List permitted products, territories, domains, and compensation methods",
                        "Compare deployed features against signed service schedule versions",
                        "Remove out-of-scope features before their next paid activation",
                    ],
                    [
                        "CPA trigger defines an accepted first-time depositor",
                        "Specify qualifying events, attribution windows, and rejection deadlines",
                        "Match event identifiers to dated acceptance and rejection records",
                        "Challenge unsupported reversals before the contractual dispute deadline",
                    ],
                    [
                        "NGR schedule fixes deductions and carryover treatment",
                        "Enumerate bonus, tax, administration, and account-netting mechanics",
                        "Rebuild cohort waterfalls from itemized monthly partner statements",
                        "Pause acquisition when effective commission falls below thresholds",
                    ],
                    [
                        "Anti-circumvention protects specific documented commercial introductions only",
                        "Limit protected parties, covered transactions, duration, and remedies",
                        "Retain introduction records and partner acknowledgments with timestamps",
                        "Use agreed dispute procedures instead of withholding unrelated services",
                    ],
                    [
                        "Liability allocation follows controllable acts and omissions",
                        "Specify cap basis, exclusions, indemnities, and defense procedures",
                        "Retain security tests and incident response responsibility records",
                        "Reject unlimited exposure unsupported by price or insurance",
                    ],
                    [
                        "Dispute resolution preserves timely payment and evidence",
                        "Define escalation, governing law, forum, and undisputed payment duties",
                        "Retain notices, reconciliations, correspondence, and statement version history",
                        "Escalate disputed deductions without surrendering unrelated earned fees",
                    ],
                    [
                        "IP and data provisions preserve licensed operating rights",
                        "Separate original code ownership from restricted source-data permissions",
                        "Retain source licenses and executed downstream usage schedules",
                        "Disable restricted exports while preserving lawful customer access",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Protect the commission before scaling the click",
                "body": (
                    "The best acquisition contract can be recalculated from its evidence. Negotiate "
                    "the statement structure and test events before negotiating larger traffic commitments."
                ),
                "items": [
                    "Demand an example NGR statement with every deduction populated; rebuild its result before accepting the commercial schedule.",
                    "Negotiate negative carryover by cohort and product, with explicit expiration or reset treatment rather than silent cross-account netting.",
                    "Cap CPA rejection timing and require reason-coded evidence so an operator cannot indefinitely reclassify accepted events.",
                    "Secure hosted-content migration rights and archive live disclosures before paying publication setup fees or committing paid traffic.",
                ],
            },
        },
        {
            "heading": "4. Use permission-based scripts and evidence-led publication partnerships",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "Treat parasitic_seo, the Parasitic SEO & High-DR Subfolder Leasing play, as "
                    "a contracted distribution experiment rather than a search-ranking entitlement. The play's "
                    "DR 80-plus placement and rank-one-to-three within 48 hours targets are acquisition "
                    "hypotheses, not delivery claims. DR is a third-party metric, not a Google "
                    "authorization. Paid third-party pages placed mainly to exploit host reputation may "
                    "violate search policies even when commercially documented. Partner with topically aligned "
                    "trade publications that retain meaningful editorial review, publish original comparisons and "
                    "calculators, and distinguish sponsored relationships. Require approved domains, publication standards, "
                    "appropriate sponsored-link attributes, correction rights, takedown timing, attribution fields, and "
                    "migration rights. An illustrative $1,200 monthly placement generating 2,000 visits at "
                    "a 3% click-through rate produces 60 outbound visits; a 5% accepted-FTD rate "
                    "produces three CPA events. At $300 each, revenue is $900, leaving a "
                    "$300 loss before editorial and operating expense. Do not hide the loss "
                    "behind ranking screenshots. If discovery underperforms or platform policy risk increases, "
                    "end the lease and use aligned editorial partnerships as top-of-funnel feeders into "
                    "owned email lists and separately authorized SMS lists. Preserve audience permission "
                    "records; publication traffic does not itself create permission to message individual readers."
                ),
                (
                    "Use this operator outreach script verbatim after replacing only the factual "
                    "identity and territory fields with verified details: 'Hello, I run a non-custodial "
                    "research and comparison publisher. We are evaluating your licensed offering for audiences "
                    "in our documented permitted territories. We do not accept player funds or "
                    "place bets. Please send your affiliate service classification requirements, approved traffic "
                    "sources, CPA acceptance definition, and itemized NGR schedule. We will activate "
                    "links only after the required permissions and destination controls are documented. "
                    "Who owns partner onboarding and monthly settlement?' Follow with this discovery "
                    "script: 'Which legal entity signs, which products and territories are covered, "
                    "and what credential must our entity hold? What makes an FTD payable? "
                    "Which deductions apply before our share, how does negative carryover work, "
                    "and can casino losses offset sportsbook commissions? Please show a sample statement "
                    "and rejected-event report. Who can authorize changes, and how much notice "
                    "applies?' These questions expose incompatible settlement terms before integration work. "
                    "Record answers against the draft contract rather than relying on meeting memory. "
                    "If the partner will not document deductions or classification responsibilities, stop "
                    "commercial onboarding and continue only general, unlinked research until the missing "
                    "terms are resolved in writing."
                ),
                (
                    "Use this publication script verbatim: 'We propose an original, clearly disclosed "
                    "comparison guide for your existing gaming or market-structure audience. Your editors "
                    "retain review and correction rights. We will identify compensated links, exclude "
                    "prohibited destinations, and maintain jurisdiction-specific calls to action. We are buying "
                    "defined editorial distribution, not promised search positions. Please confirm placement duration, "
                    "permitted link treatment, access to aggregate performance reports, and removal or migration "
                    "rights.' For customer discovery, use: 'Which probability comparisons do you currently "
                    "rebuild manually, how frequently do stale quotes interrupt that work, and what "
                    "would make a research subscription useful? Our service publishes analytics; it "
                    "does not accept funds or execute transactions. Would you like one product "
                    "summary by email?' Record that answer without treating it as SMS authorization. "
                    "The first commercial email must identify the sender, include the required postal "
                    "address, explain why the recipient is receiving it, and provide a functional "
                    "opt-out. Use separate, clearly described authorization for promotional texts when required "
                    "and synchronize revocations across vendors. Run the four-step launch procedure below "
                    "before sending production traffic. Keep outreach truthful: do not claim registration "
                    "is pending unless an application actually exists, and do not describe an "
                    "operator relationship as active before the agreement takes effect."
                ),
            ],
            "table": {
                "caption": "Verbatim Script Deployment and Partner Evidence Matrix",
                "headers": [
                    "Conversation and intended commercial outcome",
                    "Required evidence before making claims",
                    "Question or term requiring written confirmation",
                    "Fallback when the counterpart declines",
                ],
                "rows": [
                    [
                        "Operator introduction seeks the correct onboarding contact",
                        "Verify sender identity and actual target jurisdiction eligibility",
                        "Request responsible onboarding owner and service classification process",
                        "Keep discussion exploratory and disable monetized destination links",
                    ],
                    [
                        "CPA discovery establishes payable customer acquisition events",
                        "Prepare event schema without transmitting player identity documents",
                        "Request acceptance criteria and reason-coded rejection reporting deadlines",
                        "Decline paid acquisition until payment triggers are auditable",
                    ],
                    [
                        "NGR discovery exposes deductions and negative carryover",
                        "Prepare a sample waterfall using expressly illustrative values",
                        "Request itemized deductions and cross-product offset treatment",
                        "Prefer transparent CPA terms or recurring research subscriptions",
                    ],
                    [
                        "Publication outreach secures aligned editorial distribution inventory",
                        "Verify publication audience and real editorial oversight practices",
                        "Confirm disclosure placement and sponsored-link treatment in writing",
                        "Choose another aligned publication rather than disguised placements",
                    ],
                    [
                        "Hosted guide negotiation protects content portability rights",
                        "Document ownership of original text and licensed datasets",
                        "Confirm removal timing and rights to republish original material",
                        "Publish owned-domain research without restrictive hosting commitments",
                    ],
                    [
                        "Customer discovery validates recurring analytics subscription demand",
                        "Prepare accurate demonstrations using permitted market-data sources",
                        "Ask which manual research task warrants recurring payment",
                        "Offer descriptive education without individualized trading instructions",
                    ],
                    [
                        "Permission-based follow-up preserves channel-specific messaging evidence",
                        "Retain request wording and timestamp with recipient details",
                        "Confirm authorized channel and process every withdrawal promptly",
                        "Send no further promotion after permission is withdrawn",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Classify the exact service and compensation",
                    "action": (
                        "Inventory publishing, referrals, personalization, account access, and any "
                        "transaction-related features before partner integration."
                    ),
                    "detail": (
                        "Attach the CFTC classification analysis, venue permissions, and jurisdiction-specific "
                        "affiliate requirements to the release record; remove unresolved capabilities."
                    ),
                },
                {
                    "step": 2,
                    "title": "Execute auditable commercial schedules",
                    "action": (
                        "Sign separate software and gaming acquisition schedules with explicit fee triggers, "
                        "deductions, ownership, liability, and dispute procedures."
                    ),
                    "detail": (
                        "Recalculate a sample CPA statement and NGR waterfall, then verify that "
                        "termination, carryover, and retrospective rejection terms match the operating model."
                    ),
                },
                {
                    "step": 3,
                    "title": "Test destination controls and attribution",
                    "action": (
                        "Run synthetic subscription and referral events through age screens, jurisdiction "
                        "filters, source permissions, and settlement exports."
                    ),
                    "detail": (
                        "Confirm prohibited destinations remain suppressed, stale quotes disable affected "
                        "comparisons, event identifiers are deduplicated, and no player funds reach the publisher."
                    ),
                },
                {
                    "step": 4,
                    "title": "Launch narrowly and reconcile the first settlement",
                    "action": (
                        "Send a bounded amount of permitted traffic and compare accepted events, "
                        "earned fees, CAC, and itemized deductions against the signed schedules."
                    ),
                    "detail": (
                        "Retain campaign screenshots and permission records; expand only after the "
                        "first settlement reconciles and off-season sensitivity remains affordable."
                    ),
                },
            ],
        },
    ],
    "pull_quote": (
        "Own the research, document the permission, and reconcile the commission before buying the next click."
    ),
    "diagram_id": "diag-05",
    "action_checklist": [
        "Create separate software and gaming acquisition ledgers with payer, service, recognition basis, deductions, and supporting contract references.",
        "Obtain written CTA/IB/FCM feature classification and remove custody, pooling, unauthorized solicitation, and prohibited destination functionality.",
        "Build a product-specific NJ/PA/MI/WV/ON permission register with operator evidence, affiliate requirements, renewal dates, and fail-closed link controls.",
        "Negotiate CPA acceptance evidence, itemized NGR deductions, bounded carryover, audit access, ownership rights, liability allocation, and dispute deadlines.",
        "Test 21-plus funnel policy, jurisdiction suppression, responsible-gaming disclosures, material-connection notices, attribution deduplication, and messaging withdrawals.",
        "Reconcile canonical profits of $19,500, $137,750, and $325,000, then separately stress placement losses and post-NFL CPA contraction.",
    ],
    "statutory_citations": [
        {
            "title": "7 U.S.C. § 1a — Commodity Exchange Act definitions",
            "url": "https://www.law.cornell.edu/uscode/text/7/1a",
            "relevance": (
                "Defines commodity trading advisers, futures commission merchants, and introducing brokers; "
                "non-custody alone does not settle intermediary registration."
            ),
        },
        {
            "title": "7 U.S.C. § 6m — Registration of commodity trading advisers and commodity pool operators",
            "url": "https://www.law.cornell.edu/uscode/text/7/6m",
            "relevance": (
                "Supports feature-specific analysis of compensated advice and applicable registration obligations "
                "rather than relying on a publisher label."
            ),
        },
        {
            "title": "17 CFR § 4.14 — Exemption from registration as a commodity trading adviser",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-4/section-4.14",
            "relevance": (
                "Provides conditional exemptions whose applicability must be assessed against the actual "
                "research, personalization, and customer-interaction workflow."
            ),
        },
        {
            "title": "15 U.S.C. § 45 — Unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": (
                "Governs deceptive commercial claims, including unsupported performance claims and misleading "
                "presentations of compensated comparisons."
            ),
        },
        {
            "title": "16 CFR Part 255 — Guides concerning endorsements and testimonials in advertising",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255",
            "relevance": (
                "Supplies FTC interpretive guidance on endorsements and disclosure of material connections "
                "between publishers and compensated destinations."
            ),
        },
        {
            "title": "15 U.S.C. § 7704 — Requirements for transmission of commercial electronic mail",
            "url": "https://www.law.cornell.edu/uscode/text/15/7704",
            "relevance": (
                "Establishes commercial email requirements covering headers, sender information, postal address, "
                "opt-out functionality, and suppression timing."
            ),
        },
        {
            "title": "47 U.S.C. § 227 — Restrictions on use of telephone equipment",
            "url": "https://www.law.cornell.edu/uscode/text/47/227",
            "relevance": (
                "Requires separate examination of promotional calling and texting practices rather than "
                "treating email permission as interchangeable authorization."
            ),
        },
        {
            "title": "47 CFR § 64.1200 — Delivery restrictions",
            "url": "https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200",
            "relevance": (
                "Contains implementing requirements relevant to covered calls, texts, permission records, "
                "revocation handling, and do-not-call procedures."
            ),
        },
    ],
}
