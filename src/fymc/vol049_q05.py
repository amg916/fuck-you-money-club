from __future__ import annotations

CHAPTER_5 = {
    "id": "Q5",
    "chapter_id": "Q5",
    "chapter_number": 5,
    "question_number": 5,
    "slug": "beginner-traps-clawbacks-and-asymmetric-failure-modes",
    "question_prompt": "What kills 80% of newcomers in regulated prediction-market terminals & licensed igaming affiliates, and what forensic metrics detect margin leaks, regulatory landmines, or platform bans before they wipe out capital?",
    "kicker": "Q5 / THE BIG MONEY PLAYBOOKS",
    "title": "Beginner Traps, Clawbacks & Asymmetric Failure Modes",
    "subtitle": "Forensic CPA and NGR Ledgers, CFTC Registration Boundaries, Feed Integrity, and State-Specific Affiliate Circuit Breakers",
    "layout_template": "expert_insights",
    "reading_time_minutes": 14,
    "executive_summary": (
        "Candidate #49, Rank #18 of 49, scores 91/100, but its attractive small-team "
        "economics depend on separating subscription revenue from contingent gambling "
        "commissions. This chapter organizes 12 mapped plays into operating controls "
        "for registration boundaries, feed integrity, attribution, clawbacks, seasonality, "
        "and platform dependency. The question's 80% figure is a framing device, not "
        "an established failure statistic. Formula v2.0 annual owner profits remain "
        "$19,500 Conservative, $137,750 Base, and $325,000 Scaled. Protect those cases "
        "by reconciling qualified deposits to cash, measuring NGR after contractual "
        "deductions, suppressing stale probability comparisons, and stopping campaigns "
        "before acquisition costs exceed collectible commissions. The objective is "
        "a non-custodial analytics and properly registered affiliate operation, never "
        "a disguised brokerage, wagering pool, or workaround for restricted venues."
    ),
    "key_metrics": [
        {
            "label": "Conservative",
            "value": "$75,000",
            "context": "Annual operator revenue; excludes customer deposits and trading volume",
            "note": "26% net margin; $19,500 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Base",
            "value": "$362,500",
            "context": "Annual operator revenue; affiliate commissions measured after deductions",
            "note": "38.0% net margin; $137,750 annual owner net profit; 1 FT + 2 C",
        },
        {
            "label": "Scaled",
            "value": "$650,000",
            "context": "Annual operator revenue; separate SaaS, permitted rebates, and affiliate ledgers",
            "note": "50% net margin; $325,000 annual owner net profit; 2 FT + 3 C (5 people)",
        },
    ],
    "sections": [
        {
            "heading": "1. Stop registration drift before a productive feature becomes a different business",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The first fatal trap is treating non-custodial as a universal exemption. "
                    "A dashboard can avoid possessing customer money yet still cross a "
                    "registration boundary through solicitation, order handling, individualized "
                    "advice, or compensation arrangements. Under 7 U.S.C. § 1a and "
                    "17 CFR § 1.3, activity matters more than the label analytics. "
                    "An introducing broker can solicit or accept covered orders without "
                    "accepting the money supporting them; custody is therefore an incomplete "
                    "test. Evaluate commodity trading adviser status and any applicable "
                    "publisher exclusion or exemption separately, including 17 CFR § 4.14 "
                    "where relevant. Keep the initial product read-only: authorized market "
                    "observations, documented probability calculations, and links whose "
                    "destination and commercial terms have been checked. Do not accept "
                    "trading credentials, transmit customer orders, aggregate stakes, or "
                    "operate pooled accounts. A permitted builder rebate requires a written "
                    "program and an activity-specific registration assessment, not a "
                    "marketing representative's reassurance. Record every proposed feature "
                    "against account access, order influence, compensation, and user "
                    "interaction. Stop release when any answer changes. This catches the "
                    "apparently harmless trade button before it converts a subscription "
                    "product into a materially different operating model."
                ),
                (
                    "The second trap is copying one state's affiliate workflow into every "
                    "territory. NJ DGE, PA PGCB, and MI MGCB administer distinct supplier "
                    "and affiliate requirements; classification can depend on services, "
                    "compensation, and operator relationships. WV and Ontario require "
                    "their own analysis, and Ontario is a Canadian jurisdiction rather "
                    "than another American state. The chapter's 21+ access policy is "
                    "an intentionally restrictive product choice, not a statement that "
                    "every listed jurisdiction uses the same statutory age. Confirm "
                    "the audience, operator license, affiliate status, approved advertising "
                    "terms, responsible-gaming disclosures, and permitted tracking fields "
                    "for each destination. A visitor's self-declared location is not "
                    "sufficient evidence for a state-specific acquisition offer. Use "
                    "lawfully obtained location signals to restrict the portal, while "
                    "the licensed operator performs its own account, identity, location, "
                    "and eligibility checks. Suppress offers when signals conflict; "
                    "never suggest VPN workarounds. Under 16 CFR § 255.5, disclose "
                    "material affiliate relationships clearly beside recommendations. "
                    "The third trap is burying that disclosure while calling paid "
                    "placement an objective ranking. Preserve ranking inputs and "
                    "creative versions so a complaint can be reconstructed without "
                    "collecting unnecessary sensitive identity documents."
                ),
                (
                    "Use twelve mapped operating plays as this chapter's control index, "
                    "not as twelve independently forecast revenue businesses. They are "
                    "publisher-boundary isolation, jurisdiction-specific offer eligibility, "
                    "settlement-equivalent probability comparison, stale-feed suppression, "
                    "free_tier_api_waterfall_multiplexing, signed deposit attribution, "
                    "cohort-qualified CPA purchasing, deduction-level NGR reconciliation, "
                    "negative-carryover containment, seasonal acquisition throttling, "
                    "dependency concentration limits, and evidence-led incident recovery. "
                    "These descriptive labels organize the chapter; only the waterfall "
                    "identifier is supplied as an external mapped identifier. The "
                    "waterfall is the TRACK_1 Multi-Provider Free-Tier API Router & "
                    "B2B Data-Enrichment Reselling play, applied to authorized business "
                    "research rather than bettor profiling. Assign an owner and a "
                    "fallback to every play. For example, if a $300 CPA is conditional "
                    "on a qualified first deposit, a click and even an account opening "
                    "are worth zero earned CPA until the contract's conditions hold. "
                    "If a builder agreement is suspended, disable the compensated "
                    "link and retain independently licensed subscription analytics. "
                    "If a jurisdiction becomes uncertain, remove its acquisition "
                    "offers while preserving permitted read-only material. None of "
                    "these fallbacks includes offshore crypto routing, unlawful "
                    "sweepstakes destinations, borrowed accounts, or relabeling "
                    "compensation to conceal what the operator actually does."
                ),
            ],
            "table": {
                "caption": "Registration, Advertising, and Destination Controls Before Commercial Exposure",
                "headers": [
                    "Failure mechanism",
                    "Evidence required",
                    "Early warning threshold",
                    "Operator circuit breaker",
                ],
                "rows": [
                    [
                        "Adding order transmission to a read-only terminal",
                        "Written activity assessment covering solicitation and account access",
                        "Any feature receives credentials or transmits customer instructions",
                        "Disable execution features and retain authorized observation tools",
                    ],
                    [
                        "Assuming absence of custody resolves every registration question",
                        "Separate IB, FCM, and adviser boundary assessments",
                        "Compensation or personalization changes without an updated assessment",
                        "Freeze the changed function pending activity-specific classification",
                    ],
                    [
                        "Extending one state registration across unrelated territories",
                        "Jurisdiction matrix naming operator license and affiliate status",
                        "Any destination lacks a verified current operating basis",
                        "Remove that destination from every acquisition offer surface",
                    ],
                    [
                        "Routing restricted visitors through alternative unlicensed gambling destinations",
                        "Destination allowlist linked to current authorized operator records",
                        "Any redirect resolves outside the documented destination allowlist",
                        "Block the redirect and investigate the complete link chain",
                    ],
                    [
                        "Presenting purchased ranking placement as independent editorial selection",
                        "Visible relationship disclosure and reproducible ranking input history",
                        "Any compensated recommendation omits its nearby material disclosure",
                        "Withdraw the recommendation until disclosure and ranking align",
                    ],
                    [
                        "Confusing portal age policy with operator eligibility verification",
                        "Documented audience policy plus operator-side eligibility responsibility allocation",
                        "Any acquisition route bypasses the required audience restrictions",
                        "Suppress offers and repair the affected visitor journey",
                    ],
                    [
                        "Letting informal rebate promises authorize new commercial activity",
                        "Executed program terms and documented permitted service scope",
                        "Any payout relies on undocumented eligibility or service assumptions",
                        "Exclude the rebate forecast and suspend compensated placement",
                    ],
                ],
            },
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Four checks before the first compensated visitor",
                "body": (
                    "A small team can make these checks reproducible without collecting "
                    "customer funds or imitating the licensed operator's account systems."
                ),
                "items": [
                    "Verify read-only product behavior and document IB, FCM, and adviser boundary analysis against the actual features and compensation.",
                    "Confirm each operator destination, jurisdiction-specific affiliate classification, required registration, and current contractual permission before publishing its offer.",
                    "Exercise the 21+ audience restriction, jurisdiction suppression, nearby compensation disclosure, and jurisdiction-appropriate responsible-gaming information.",
                    "Obtain the precise CPA qualification, reversal, NGR deduction, negative-carryover, reporting, dispute, and payment clauses before assigning acquisition budget.",
                ],
            },
        },
        {
            "heading": "2. Make market comparisons and upstream economics survive contact with reality",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The fourth trap is selling apparent cross-venue arbitrage between "
                    "contracts that do not settle identically. A Kalshi event contract, "
                    "a ForecastEx contract available through an authorized channel, "
                    "and a sportsbook proposition can disagree on settlement source, "
                    "deadline, cancellation, overtime, or exceptional events. An apparent "
                    "four-cent probability gap is meaningless when one contract counts "
                    "overtime and another excludes it. Normalize event identifiers, "
                    "outcome wording, settlement authority, fees, depth, and executable "
                    "size before presenting a comparison. An illustrative $1 contract "
                    "bought for $0.48 against an independently estimated 0.51 probability "
                    "has three cents of modeled gross edge; two cents of transaction "
                    "cost and one cent of slippage remove it completely. Estimation "
                    "error can make the result worse. Sportsbook decimal odds of "
                    "2.10 imply about 47.62% before adjusting for the full market's "
                    "overround; that is not automatically comparable to a contract's "
                    "displayed midpoint. Label the observation time and calculation "
                    "method. Suppress positive-EV labels when matching is incomplete "
                    "or available depth cannot support the displayed size. The safe "
                    "fallback is an informational comparison with explicit differences, "
                    "not an asserted executable hedge or a promised return."
                ),
                (
                    "The fifth trap is mistaking a fast WebSocket connection for a "
                    "reliable market feed. Transport latency, upstream publication age, "
                    "sequence gaps, and local processing delay are different measurements. "
                    "For an illustrative liquid-market service target, flag quote age "
                    "above one second and suppress actionable comparisons above two "
                    "seconds; tune both limits to documented venue cadence rather "
                    "than presenting them as universal rules. A quiet market requires "
                    "heartbeat evidence, not fabricated price updates. Record monotonic "
                    "receive time, source timestamps where supplied, sequence identifiers, "
                    "and snapshot version. On reconnect, rebuild state from the "
                    "provider's supported snapshot and replay procedure; do not stitch "
                    "an old order book to new deltas blindly. Separate a genuine "
                    "empty book from a missing update. The sixth trap is treating "
                    "accessible feeds as commercially redistributable. Obtain rights "
                    "for storage, derived displays, attribution, and downstream use "
                    "from each provider; a public endpoint alone supplies none of "
                    "those permissions. Use token buckets, bounded retries, and "
                    "provider-specific budgets. A rate-limit response must reduce "
                    "traffic rather than trigger account rotation. If authorized "
                    "live access fails, show clearly timestamped historical analytics "
                    "or disable the affected instrument instead of silently "
                    "substituting scraped sportsbook prices."
                ),
                (
                    "The seventh trap sits inside free_tier_api_waterfall_multiplexing: "
                    "free requests are not free resale rights. Its specified design "
                    "aggregates 30–60+ B2B data, email-verification, firmographic, DNS, "
                    "and SERP providers offering roughly 50–1,000 monthly developer "
                    "lookups each. Forty providers averaging 250 permitted lookups "
                    "yield 10,000 raw monthly calls, not 10,000 complete enriched "
                    "records. At two calls per cache miss and an 80% fresh-cache "
                    "hit rate, 20,000 requested records consume 8,000 calls, leaving "
                    "2,000 for retries and exceptional fields. Ten customers at "
                    "$199 monthly produce $1,990 subscription billings; $150 hosting "
                    "and $400 support leave $1,440 before acquisition, other labor, "
                    "and overhead. This is a standalone sensitivity example, not "
                    "additional scorecard revenue. Maintain 40+ interchangeable "
                    "adapters, Postgres field provenance, expiry rules, and contractual "
                    "resale flags. Prioritize the local graph cache when quotas "
                    "tighten, then use permitted direct public-web, DNS, and MX "
                    "extraction for business records only. MX existence does not "
                    "prove mailbox deliverability. Exclude providers prohibiting "
                    "aggregation or resale, honor shared account quotas, and degrade "
                    "record completeness visibly. Never multiply free accounts, "
                    "evade blocks, or enrich individual bettors with unrelated "
                    "personal attributes to rescue unit economics."
                ),
            ],
            "table": {
                "caption": "Feed Integrity and Free-Tier Waterfall Defects That Manufacture False Margin",
                "headers": [
                    "Technical trap",
                    "Measurement and unit basis",
                    "Initial operating threshold",
                    "Fallback preserving product integrity",
                ],
                "rows": [
                    [
                        "Comparing outcomes with different settlement or cancellation terms",
                        "Matched settlement fields for every displayed contract pair",
                        "Any unresolved outcome definition blocks an executable comparison",
                        "Publish the differences without presenting a synthetic hedge",
                    ],
                    [
                        "Showing an apparent edge before costs and depth",
                        "Expected payoff less price, fees, and executable slippage",
                        "Zero or negative modeled net edge suppresses alerts",
                        "Retain neutral observations with complete calculation input history",
                    ],
                    [
                        "Serving a stale quote through a healthy socket",
                        "Source age, receive delay, heartbeat age, and sequence continuity",
                        "Illustrative two-second quote age suspends actionable liquid-market comparisons",
                        "Display observation time and switch to historical analytics",
                    ],
                    [
                        "Merging old snapshots with unrelated post-reconnect order updates",
                        "Snapshot version and sequence continuity for each instrument",
                        "Any unreconciled sequence gap invalidates the reconstructed book",
                        "Rebuild through the provider's supported recovery and replay",
                    ],
                    [
                        "Redistributing accessible prices without commercially sufficient usage rights",
                        "Provider terms covering retention, display, attribution, and resale",
                        "Any missing required permission excludes that commercial feed",
                        "Remove the affected feed while retaining independently licensed inputs",
                    ],
                    [
                        "Counting free API calls as complete enriched records",
                        "Calls per miss multiplied by uncached requested records",
                        "Projected authorized usage above eighty percent triggers capacity planning",
                        "Prioritize current cache entries and reduce optional enrichment fields",
                    ],
                    [
                        "Treating DNS or MX presence as verified deliverability",
                        "Field-level provenance and distinct verification confidence classifications",
                        "Any unsupported deliverability claim blocks the enriched record",
                        "Return only the narrower technically supported domain finding",
                    ],
                ],
            },
            "callout": {
                "kind": "INSIDER PRO-TIPS",
                "title": "Veteran tactics for preserving evidence and negotiating leverage",
                "body": (
                    "The best protection is a reproducible record that survives a "
                    "provider change, operator dispute, or apparently profitable anomaly."
                ),
                "items": [
                    "Keep a settlement-difference registry for recurring event pairs; one cancellation-rule mismatch should suppress every affected comparison automatically.",
                    "Replay recorded authorized feed sequences through the exact production normalization version before enabling a revised probability alert.",
                    "Negotiate deduction definitions, invoice-level reason codes, dispute deadlines, and negative-carryover scope before negotiating a higher headline RevShare.",
                    "Store provider permission versions beside waterfall adapter versions so quota savings never conceal a changed resale or retention restriction.",
                ],
            },
        },
        {
            "heading": "3. Reconcile qualified deposits to collectible commissions, not dashboard celebrations",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                (
                    "The eighth trap is optimizing to raw first-time-depositor events "
                    "instead of contract-qualified, collectible CPA. An illustrative "
                    "campaign buys 120 candidate depositors at $180 acquisition "
                    "cost each, or $21,600. At $300 headline CPA, gross expected "
                    "commission is $36,000. A 15% invalidation rate removes $5,400, "
                    "leaving $30,600 before $3,000 servicing costs and $21,600 "
                    "acquisition costs: only $6,000 contribution. The effective "
                    "commission per candidate is $255, not $300. Duplicate "
                    "accounts, existing customers, excluded locations, chargebacks, "
                    "minimum-deposit failures, and prohibited traffic sources can "
                    "all defeat qualification, but only the actual contract "
                    "determines the applicable reasons and timing. Record click, "
                    "registration, deposit, qualification, reversal, invoice, and "
                    "cash dates as separate states. Use operator-supported signed "
                    "S2S callbacks, idempotent event keys, and server-held secrets; "
                    "never let browser parameters declare an earned commission. "
                    "Compare mature cohorts rather than yesterday's incomplete "
                    "traffic. Investigate a five-percentage-point increase in "
                    "reversals against the mature baseline, and pause a placement "
                    "if expected contribution per candidate becomes nonpositive. "
                    "These are initial business triggers, not regulatory limits. "
                    "Keep reversal reason codes and appeal evidence without "
                    "retaining raw payment credentials or excess identity records."
                ),
                (
                    "The ninth trap is reading NGR as a universal accounting "
                    "definition. It is a negotiated commission base whose "
                    "deductions can include bonuses, taxes, payment charges, "
                    "administration, jackpot contributions, and adjustments. "
                    "Start with an illustrative $50,000 gaming gross revenue "
                    "figure, already distinct from stakes and deposits. Subtract "
                    "$10,000 bonuses, $5,000 administration, and $5,000 taxes "
                    "where the agreement permits those deductions: eligible "
                    "NGR becomes $30,000. A 25% share produces $7,500 before "
                    "carryover. If the contract carries an $8,000 negative "
                    "balance at the commission-share level, current cash "
                    "commission is zero and $500 remains negative. A balance "
                    "carried at the underlying NGR level would produce a "
                    "different result; store its level explicitly. This is "
                    "the tenth trap: assuming each month resets or that losses "
                    "cannot cross brands, countries, or players. Negotiate "
                    "ring-fenced balances and a clear expiry or reset where "
                    "commercially available. Never subtract the same bonus "
                    "once inside NGR and again from the affiliate invoice. "
                    "Alert when total deductions rise more than five percentage "
                    "points against the mature contractual baseline, then "
                    "reconcile each line before buying further traffic into "
                    "that cohort."
                ),
                (
                    "Keep the Formula v2.0 scorecard intact while exposing its "
                    "economic plumbing. Conservative revenue of $75,000 less "
                    "$55,500 expenses equals $19,500 owner profit, or 26%. "
                    "Base revenue of $362,500 less $224,750 expenses equals "
                    "$137,750, or 38.0%. Scaled revenue of $650,000 less "
                    "$325,000 expenses equals $325,000, or 50%. An illustrative "
                    "Base allocation is $180,000 subscriptions, $12,500 permitted "
                    "builder rebates, and $170,000 affiliate commissions after "
                    "deductions. The affiliate bridge starts at $240,000 "
                    "provisional commissions and subtracts $40,000 contractual "
                    "bonus and administration deductions, $18,000 invalidations, "
                    "and $12,000 share-level carryover absorption. Its $170,000 "
                    "revenue less $72,000 CAC and $28,000 other affiliate "
                    "costs contributes $70,000. Subscription and rebate revenue "
                    "of $192,500 less $124,750 remaining expenses contributes "
                    "$67,750, reconciling exactly to Base owner profit. These "
                    "allocations illustrate the supplied totals rather than "
                    "replace them. Assess principal-versus-agent presentation "
                    "and variable consideration under ASC 606; neither deposits "
                    "nor user trading volume become operator revenue. No "
                    "separate retained_share factor was supplied, so do not "
                    "invent one or apply another haircut to already net "
                    "commissions. A cash reserve changes liquidity, not profit "
                    "again unless a separate expense is actually warranted."
                ),
            ],
            "table": {
                "caption": "CPA, NGR, and Scorecard Bridges With Explicit Denominators",
                "headers": [
                    "Ledger or scenario",
                    "Revenue bridge and recognition basis",
                    "Cost or deduction bridge",
                    "Decision and reconciliation result",
                ],
                "rows": [
                    [
                        "Illustrative CPA campaign with one hundred twenty candidates",
                        "One hundred twenty times $300 yields $36,000 provisional commission",
                        "$5,400 invalidations, $21,600 acquisition, and $3,000 servicing apply",
                        "$6,000 contribution remains after the complete campaign bridge",
                    ],
                    [
                        "Illustrative NGR agreement before commission-level negative balance",
                        "$50,000 gaming gross revenue becomes $30,000 eligible NGR",
                        "$10,000 bonuses plus $5,000 administration plus $5,000 taxes",
                        "Twenty-five percent share produces $7,500 before carryover absorption",
                    ],
                    [
                        "Illustrative negative balance carried at commission-share level",
                        "$7,500 current share offsets an $8,000 opening deficit",
                        "Carryover consumes current commission without creating new deposits",
                        "Current cash commission is zero with $500 deficit remaining",
                    ],
                    [
                        "Canonical Conservative annual operator scorecard reconciliation basis",
                        "$75,000 operator revenue excludes deposits and customer trading volume",
                        "$55,500 total expenses include modeled operating acquisition costs",
                        "$19,500 owner profit equals a twenty-six percent margin",
                    ],
                    [
                        "Canonical Base annual operator scorecard reconciliation basis",
                        "$362,500 operator revenue combines separately controlled commercial ledgers",
                        "$224,750 total expenses reconcile acquisition and remaining operating costs",
                        "$137,750 owner profit equals a thirty-eight percent margin",
                    ],
                    [
                        "Canonical Scaled annual operator scorecard reconciliation basis",
                        "$650,000 operator revenue supports the specified five-person operating team",
                        "$325,000 total expenses remain distinct from customer wagering stakes",
                        "$325,000 owner profit equals a fifty percent margin",
                    ],
                    [
                        "Illustrative Base affiliate allocation within canonical annual totals",
                        "$240,000 provisional commissions become $170,000 after specified deductions",
                        "$72,000 CAC plus $28,000 other affiliate operating costs",
                        "$70,000 affiliate contribution joins $67,750 subscription and rebate contribution",
                    ],
                ],
            },
            "sop_steps": [
                {
                    "step": 1,
                    "title": "Freeze the cohort evidence",
                    "action": "Export authorized event states, contract version, creative identifier, jurisdiction, and operator statement for the same mature cohort.",
                    "detail": "Preserve event timestamps and stable pseudonymous identifiers; separate reporting delay from actual qualification failure.",
                },
                {
                    "step": 2,
                    "title": "Rebuild qualification and deduction bridges",
                    "action": "Match every provisional CPA and NGR line to qualification, reversal, permitted deduction, and carryover records.",
                    "detail": "Deduplicate callbacks and identify whether each negative balance exists at underlying NGR or commission-share level.",
                },
                {
                    "step": 3,
                    "title": "Tie accruals to invoices and cash",
                    "action": "Reconcile earned commission, estimated reversals, invoiced amount, payment timing, and actual bank receipt independently.",
                    "detail": "Record unresolved differences with owners and contractual dispute deadlines; do not convert delayed cash automatically into a second expense.",
                },
                {
                    "step": 4,
                    "title": "Reset spend using collectible contribution",
                    "action": "Calculate cohort contribution after CAC, servicing, contractual deductions, and expected valid reversals before restoring acquisition.",
                    "detail": "Resume only the supported placement and jurisdiction; preserve the unaffected subscription service throughout the investigation.",
                },
            ],
        },
        {
            "heading": "4. Cut spend before seasonality, concentration, and bans turn a leak into insolvency",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                (
                    "The eleventh trap is annualizing NFL-season CPA rates into "
                    "a twelve-month forecast. Repeat the earlier campaign after "
                    "budgets tighten: 80 candidate depositors at $220 headline "
                    "CPA yield $17,600 provisional commission. The same 15% "
                    "invalidation rate leaves $14,960. Acquisition at $180 per "
                    "candidate costs $14,400, and $3,000 servicing produces "
                    "a $2,440 contribution loss. More volume accelerates that "
                    "loss unless acquisition economics or fixed servicing "
                    "change. Maintain sport-calendar cohorts, operator budget "
                    "confirmations, and campaign-level stop dates. Track "
                    "collectible commission per candidate against fully "
                    "allocated acquisition and servicing cost, not a blended "
                    "dashboard return inflated by older profitable cohorts. "
                    "As an initial policy, stop a placement when its mature "
                    "expected contribution is nonpositive; investigate sooner "
                    "when commission per candidate falls 15% against its "
                    "matched seasonal baseline. Never describe this stress "
                    "case as a revised canonical forecast. It is a "
                    "sensitivity test around the supplied Base case. The "
                    "fallback is to reduce paid affiliate acquisition, "
                    "retain useful subscription analytics, and renegotiate "
                    "placement terms. Email reactivation also needs audience "
                    "permission and suppression handling; repeated messaging "
                    "to excluded or vulnerable users is not a substitute "
                    "for a broken CPA spread."
                ),
                (
                    "The twelfth trap is using shortcuts that destroy the "
                    "underlying distribution account. Fake depositors, self-referral "
                    "rings, purchased identities, prohibited brand bidding, "
                    "cloaked landing pages, fabricated testimonials, and "
                    "unapproved incentivized traffic can trigger commission "
                    "reversal, termination, and wider liability. Do not "
                    "experiment with them to discover an operator's tolerance. "
                    "Store approved traffic sources and creative versions, "
                    "then reject campaign launches that do not match. "
                    "Monitor unusual repeated device or payment-linked "
                    "signals only through operator-authorized, privacy-conscious "
                    "reporting; shared household patterns alone do not prove "
                    "fraud. A suspected attribution defect calls for "
                    "reconciliation, not accusations or concealment. Platform "
                    "dependency is another asymmetric exposure: a single "
                    "search account, payment processor, feed license, or "
                    "affiliate operator can interrupt collections while "
                    "payroll continues. Treat more than 35% of trailing "
                    "ninety-day collectible revenue from one commercial "
                    "counterparty as a concentration alert, not an automatic "
                    "legal threshold. Maintain exportable customer entitlements, "
                    "documented recovery procedures, and alternative authorized "
                    "providers. An alternate account must never be used "
                    "to evade a suspension. Preserve subscription access "
                    "where permitted, remove the disputed dependency, and "
                    "use the provider's documented appeal channel with "
                    "a complete evidence package."
                ),
                (
                    "Build a daily exception sheet that connects product "
                    "health to cash survival. Include quote suppression "
                    "minutes, callback signature failures, unmatched qualified "
                    "events, mature reversal percentage, deduction ratio, "
                    "negative balances, receivable aging, and available "
                    "cash after committed obligations. For an illustrative "
                    "policy, investigate unmatched events above 1% after "
                    "the contracted reporting window, quarantine every "
                    "invalidly signed callback, and escalate invoices "
                    "fifteen days beyond their contractual due date. "
                    "Compare unrestricted cash with the next ninety "
                    "days of payroll, hosting, acquisition commitments, "
                    "and plausible contractual repayment exposure. The "
                    "published $1,500–$10,000 monthly opex range is "
                    "a planning input, not permission to omit CAC "
                    "or contractor costs from the canonical expense "
                    "bridge. Stress the largest counterparty's delayed "
                    "payment and one season of reduced CPA together. "
                    "If that combined stress consumes the operating "
                    "buffer, stop discretionary acquisition before "
                    "cutting monitoring or reconciliation. During an "
                    "incident, preserve signed event evidence, revoke "
                    "compromised credentials, disable only the affected "
                    "surface, and notify contractual counterparts as "
                    "required. Restore service after replay tests "
                    "and cash-ledger reconciliation demonstrate that "
                    "the original defect is closed. A profitable "
                    "screen is insufficient evidence; collectibility "
                    "and recoverability are the operating standard."
                ),
            ],
            "table": {
                "caption": "Seasonality, Platform Dependency, and Cash-Survival Circuit Breakers",
                "headers": [
                    "Asymmetric exposure",
                    "Forensic measurement",
                    "Initial response threshold",
                    "Containment and recovery action",
                ],
                "rows": [
                    [
                        "Post-NFL acquisition spending retains peak-season commission assumptions",
                        "Mature collectible commission per candidate versus complete acquisition cost",
                        "Nonpositive expected contribution immediately stops the affected placement",
                        "Reduce paid acquisition and preserve independently useful subscription analytics",
                    ],
                    [
                        "Campaign quality deterioration hides inside blended historical returns",
                        "Reversal percentage measured against matched mature seasonal cohorts",
                        "Five-percentage-point deterioration starts a documented cohort investigation",
                        "Hold incremental spend while qualification reasons are reconciled",
                    ],
                    [
                        "Unapproved traffic tactics expose every related affiliate payout",
                        "Traffic-source allowlist matched to creative and destination versions",
                        "Any prohibited source prevents that campaign from launching",
                        "Remove the source and preserve evidence for contractual resolution",
                    ],
                    [
                        "Single commercial counterparty controls too much collectible revenue",
                        "Trailing ninety-day collectible revenue concentration by commercial counterparty",
                        "Above thirty-five percent prompts diversification and liquidity stress testing",
                        "Add authorized alternatives without evading account restrictions or suspensions",
                    ],
                    [
                        "Callback defects inflate deposit attribution and expected receivables",
                        "Signature validity, event uniqueness, and mature unmatched event percentage",
                        "Invalid signatures quarantine immediately; unmatched events above one percent investigate",
                        "Replay authenticated records and rebuild the affected qualification cohort",
                    ],
                    [
                        "Delayed invoices consume cash reserved for committed operating obligations",
                        "Contractual due dates compared with actual unrestricted cash receipts",
                        "Fifteen days past contractual due date triggers payment escalation",
                        "Pause discretionary spending and pursue documented collection procedures",
                    ],
                    [
                        "Largest counterparty delay coincides with an off-season commission decline",
                        "Combined ninety-day cash stress including plausible contractual repayment exposure",
                        "Projected operating-buffer exhaustion suspends discretionary acquisition before further commitments",
                        "Protect monitoring, reconciliation, essential service delivery, and recovery capacity",
                    ],
                ],
            },
        },
    ],
    "pull_quote": "An affiliate dashboard reports possibilities; a reconciled cohort ledger proves what the business can keep.",
    "diagram_id": "diag-05",
    "action_checklist": [
        "Create separate subscription, permitted builder-rebate, CPA, and NGR ledgers, then reconcile the three canonical revenue, expense, and owner-profit cases.",
        "Document activity-specific IB, FCM, and adviser boundary assessments, and verify affiliate eligibility for every jurisdiction and licensed destination.",
        "Implement settlement matching, source-age measurement, sequence-gap recovery, and automatic suppression of unsupported positive-EV comparisons.",
        "Version provider permissions and maintain 40+ authorized waterfall adapters with Postgres provenance, shared-quota accounting, and visibly degraded fallback results.",
        "Reconcile mature S2S deposit cohorts through qualification, reversals, contractual NGR deductions, carryover balances, invoices, and actual cash receipts.",
        "Run the off-season CPA and largest-counterparty delay stress together, assigning explicit spend stops, incident owners, and evidence-backed restoration criteria.",
    ],
    "statutory_citations": [
        {
            "title": "7 U.S.C. § 1a — Commodity Exchange Act definitions",
            "url": "https://www.law.cornell.edu/uscode/text/7/1a",
            "relevance": (
                "Defines relevant regulated roles, including introducing broker, "
                "futures commission merchant, and commodity trading adviser; "
                "supports activity-based analysis rather than reliance on product labels."
            ),
        },
        {
            "title": "7 U.S.C. § 6d — Futures commission merchants and introducing brokers",
            "url": "https://www.law.cornell.edu/uscode/text/7/6d",
            "relevance": (
                "Provides registration and related requirements for covered "
                "intermediary activity; absence of customer custody does not "
                "alone resolve introducing-broker status."
            ),
        },
        {
            "title": "7 U.S.C. § 6m — Registration of commodity trading advisers and commodity pool operators",
            "url": "https://www.law.cornell.edu/uscode/text/7/6m",
            "relevance": (
                "Supports separate evaluation of adviser registration requirements "
                "and statutory exceptions when analytics become advice concerning "
                "covered commodity interests."
            ),
        },
        {
            "title": "17 CFR § 1.3 — Definitions",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-1/section-1.3",
            "relevance": (
                "Supplies regulatory definitions used to assess solicitation, "
                "order handling, advisory activity, and intermediary classifications "
                "against the actual product workflow."
            ),
        },
        {
            "title": "17 CFR § 4.14 — Exemption from registration as a commodity trading adviser",
            "url": "https://www.ecfr.gov/current/title-17/chapter-I/part-4/section-4.14",
            "relevance": (
                "Identifies conditional adviser-registration exemptions that must "
                "be evaluated on their precise facts; the word publisher is "
                "not a universal exemption."
            ),
        },
        {
            "title": "16 CFR § 255.5 — Disclosure of material connections",
            "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-B/part-255/section-255.5",
            "relevance": (
                "Explains material-connection disclosure principles for endorsements, "
                "including compensated recommendations and affiliate relationships "
                "that audiences would not reasonably expect."
            ),
        },
        {
            "title": "15 U.S.C. § 45 — Unfair methods of competition and unfair or deceptive acts or practices",
            "url": "https://www.law.cornell.edu/uscode/text/15/45",
            "relevance": (
                "Provides the statutory basis for addressing deceptive commercial "
                "representations, including unsupported performance claims, misleading "
                "rankings, and concealed material commercial relationships."
            ),
        },
    ],
}
