from __future__ import annotations


def build_volume_010_workbook() -> dict:
    def field(name: str, input_type: str, prompt: str, example: str) -> dict:
        return {
            "name": name,
            "type": input_type,
            "prompt": prompt,
            "example": example,
        }

    return {
        "workbook_id": "wb-010-building-an-seo-empire",
        "volume_id": "vol-010-building-an-seo-empire",
        "title": "Building an SEO Empire — Operator Companion Workbook",
        "subtitle": (
            "6 Printable Operator Worksheets for Search-Portfolio Underwriting, "
            "Publisher Unit Economics, Technical QA, Rights and Disclosure Controls, "
            "GEO Citation Measurement, and Exit-Ready Operating Systems"
        ),
        "worksheets": [
            {
                "worksheet_id": "ws-01",
                "number": 1,
                "title": "Search Portfolio Opportunity and Counterparty Underwriting",
                "purpose": (
                    "Select a defensible publishing vertical before committing acquisition "
                    "capital or commissioning a content library. Separate observable search "
                    "demand from attractive screenshots, qualify monetization counterparties, "
                    "and document why original evidence, distribution access, and editorial "
                    "capability can survive competitive imitation and ranking losses."
                ),
                "chapter_ref": "Q1, Q2, Q6",
                "instructions": [
                    (
                        "Choose one primary vertical and one adjacent expansion vertical. "
                        "Collect dated Google Search Console exports, representative search "
                        "results, publisher revenue statements, and advertiser terms. Label "
                        "each observation by source and period rather than combining estimates "
                        "with verified operating history."
                    ),
                    (
                        "Build a query sample spanning discovery, comparison, purchase, and "
                        "troubleshooting intent. Inspect the actual result pages and answer "
                        "surfaces. Reject opportunities whose apparent volume depends on "
                        "duplicate pages, unavailable data rights, or unsupported claims about "
                        "future rankings."
                    ),
                    (
                        "Qualify each affiliate network, advertising provider, sponsor, and "
                        "potential seller independently. Record settlement schedules, reversal "
                        "rights, traffic restrictions, assignment provisions, and account "
                        "ownership. A profitable website does not automatically carry "
                        "transferable monetization contracts into an acquisition."
                    ),
                    (
                        "Score evidence quality before scoring upside. Reconcile analytics "
                        "with bank settlements and platform statements where access is "
                        "authorized. Treat screenshots, modeled traffic, and selected winning "
                        "keywords as leads for investigation rather than substitutes for "
                        "complete source records."
                    ),
                    (
                        "Write an explicit proceed, revise, or reject decision with a maximum "
                        "capital commitment and named decision owner. Include the downside "
                        "conditions that stop spending, the evidence still needed, and the "
                        "next experiment that can resolve uncertainty cheaply."
                    ),
                ],
                "fields": [
                    field(
                        "Portfolio thesis and operator mandate",
                        "textarea",
                        (
                            "Define the publishing opportunity, reader problem, geographic "
                            "market, and owner responsibilities. Connect the thesis to the "
                            "canonical candidate score without treating that score as evidence "
                            "of traffic, contractual access, or achievable returns."
                        ),
                        (
                            "Candidate #25 is Building an SEO Empire, pipeline rank #07 of "
                            "29, with an 89/100 Money-to-Manpower score. Components are revenue potential 24, margin potential 22, team efficiency 18, startup accessibility 12, and automation potential 13. The mandate is a United States home-water "
                            "maintenance portfolio supported by original testing and documented "
                            "product compatibility."
                        ),
                    ),
                    field(
                        "Demand sample and search-result evidence",
                        "textarea",
                        (
                            "Describe the query sampling method, measurement period, intent "
                            "distribution, and result-page features. Identify which demand "
                            "estimates remain directional and which observations come from "
                            "authorized first-party search data or directly inspected results."
                        ),
                        (
                            "Review 120 queries: 40 troubleshooting, 35 comparisons, 25 "
                            "replacement-part searches, and 20 installation questions. Save "
                            "dated result captures and device settings for all 120. An "
                            "authorized adjacent site's 90-day Search Console export shows "
                            "18,400 clicks; third-party volume estimates remain separate "
                            "planning inputs and are never added to those clicks."
                        ),
                    ),
                    field(
                        "Original evidence and topical authority",
                        "textarea",
                        (
                            "Specify the evidence assets that make the proposed coverage "
                            "useful beyond rewritten search results. List testing procedures, "
                            "expert review, primary documents, update responsibility, and the "
                            "cost of maintaining factual accuracy across the topic cluster."
                        ),
                        (
                            "The first cluster contains 24 filter-maintenance guides supported "
                            "by 12 owned test units, manufacturer manuals, and a licensed "
                            "plumber's review. Allocate $2,400 to equipment and $1,800 to "
                            "review. Record pressure readings, installation constraints, "
                            "photograph ownership, and review dates so every comparison can "
                            "be reproduced and refreshed."
                        ),
                    ),
                    field(
                        "Programmatic page eligibility",
                        "textarea",
                        (
                            "Define the minimum unique information required before a template "
                            "becomes an indexable page. Document source permissions, entity "
                            "identifiers, missing-data handling, and editorial checks that "
                            "prevent scaled thin content or misleading product combinations."
                        ),
                        (
                            "A compatibility template has 600 possible model combinations, "
                            "but only 180 have verified dimensions, source rights, and "
                            "documented fit evidence. Publish those 180 after review; keep "
                            "the remaining combinations unpublished. Each page must contain "
                            "model-specific measurements, two original observations, a source "
                            "date, and a correction contact rather than swapped product names."
                        ),
                    ),
                    field(
                        "Monetization counterparty qualification",
                        "textarea",
                        (
                            "Record each prospective payer's commercial terms, traffic "
                            "eligibility, settlement currency, dispute process, and termination "
                            "rights. Identify dependencies on minimum traffic, account history, "
                            "geography, or seller-specific arrangements before including any "
                            "revenue in the operating forecast."
                        ),
                        (
                            "Network A offers a $20 accepted-action commission, monthly "
                            "validation, and payment 45 days after the earned period. "
                            "Advertising Provider B requires documented traffic and retains "
                            "invalid-traffic adjustment rights. Sponsor C proposes $7,000 "
                            "for one labeled package. Obtain written eligibility decisions; "
                            "do not assume the seller's accepted account transfers."
                        ),
                    ),
                    field(
                        "Acquisition seller and asset verification",
                        "textarea",
                        (
                            "List the ownership, analytics, revenue, rights, and technical "
                            "records required from a potential seller. State the reconciliation "
                            "method and explain how undisclosed liabilities, disputed assets, "
                            "or missing transfer permissions affect the purchase decision."
                        ),
                        (
                            "For a proposed $60,000 site purchase, request 24 months of "
                            "read-only analytics, network statements, settlement records, "
                            "domain ownership evidence, and contributor agreements. Reconcile "
                            "the last 12 months by payer and month. An unexplained $4,200 "
                            "gap pauses price negotiation until timing differences or "
                            "unsupported earnings are resolved in writing."
                        ),
                    ),
                    field(
                        "Competitive and search-policy exposure",
                        "textarea",
                        (
                            "Assess why incumbent publishers rank, whether the proposed "
                            "advantage can persist, and how current search policies affect "
                            "the operating model. Distinguish ordinary competition from "
                            "dependence on manipulative links, borrowed reputation, or "
                            "mass-produced low-value pages."
                        ),
                        (
                            "Eight of the top ten comparison results contain original "
                            "photos; six include measured flow rates. The portfolio competes "
                            "with better compatibility evidence, not purchased ranking links. "
                            "Reject a broker's offer of 50 paid followed links for $2,500. "
                            "Paid commercial placements receive appropriate link qualification "
                            "and remain separate from editorial judgments."
                        ),
                    ),
                    field(
                        "GEO citation opportunity and measurement",
                        "textarea",
                        (
                            "Define a reproducible method for observing citations in "
                            "generative answer systems. Record prompt sets, model or product "
                            "versions where visible, dates, geography, and citation destinations "
                            "without assuming a citation produces visits, leads, or revenue."
                        ),
                        (
                            "Test 30 maintenance questions weekly across three answer "
                            "products using permitted access methods. Store the prompt, "
                            "date, visible product version, cited URL, and answer accuracy. "
                            "A baseline of 9 citations across 90 observations becomes a "
                            "citation-frequency measure only; attributed referral sessions "
                            "and earned commissions are reported independently."
                        ),
                    ),
                    field(
                        "Concentration and downside underwriting",
                        "textarea",
                        (
                            "Quantify dependency on domains, search engines, individual pages, "
                            "affiliate merchants, and ad providers. Describe a stress event "
                            "using explicit revenue assumptions, then identify which costs "
                            "can actually change during the response period."
                        ),
                        (
                            "At the Base case, annual publisher revenue is $490,000. A "
                            "planning shock reducing every revenue channel by 30% leaves "
                            "$343,000. Holding annual costs at $330,750 leaves $12,250 "
                            "profit. This sensitivity is not another canonical scenario; "
                            "it exposes the need to reduce concentration and preserve "
                            "liquid operating cash."
                        ),
                    ),
                    field(
                        "Investment decision and evidence backlog",
                        "textarea",
                        (
                            "Write the underwriting decision with a spending limit, named "
                            "owner, unresolved evidence items, and dated review. Explain "
                            "what result would justify expansion and what observation would "
                            "stop further capital deployment into the selected opportunity."
                        ),
                        (
                            "Proceed with a $12,000 research and publication pilot inside "
                            "the overall startup budget. The portfolio lead must obtain "
                            "two written monetization eligibility responses, verify rights "
                            "for 24 guides, and complete baseline instrumentation. Reassess "
                            "after 90 days; pause new production if evidence quality "
                            "fails or projected cash coverage falls below the agreed floor."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The portfolio lead signs a dated decision supported by the 120-query "
                    "sample, documented rights, counterparty eligibility evidence, a "
                    "reconciled downside model, and a bounded pilot budget. Unresolved "
                    "ownership or monetization-transfer issues block acquisition spending."
                ),
            },
            {
                "worksheet_id": "ws-02",
                "number": 2,
                "title": "Publisher Unit Economics, Defect Reserve, and Cash Float",
                "purpose": (
                    "Translate visits, accepted affiliate actions, and sponsor deliverables "
                    "into recognized publisher revenue and cash requirements. Reconcile "
                    "every scenario to the canonical scorecard, distinguish settlement "
                    "adjustments from operating expenses, and expose the liquidity gap "
                    "between paying contributors and collecting counterparties' balances."
                ),
                "chapter_ref": "Q3, Q4",
                "instructions": [
                    (
                        "Start with the three canonical annual scenarios and compute "
                        "implied total costs before building channel assumptions. Keep "
                        "merchant sales, customer order values, and modeled search demand "
                        "outside publisher revenue. Label every operating decomposition "
                        "as an illustrative allocation."
                    ),
                    (
                        "Build revenue from measurable units: monetized sessions, recognized "
                        "advertising yield, validated affiliate actions, and delivered "
                        "sponsorship packages. Specify denominator definitions and reporting "
                        "periods. Do not combine pageview-based advertising rates with "
                        "session-based traffic without an explicit conversion."
                    ),
                    (
                        "Separate pre-recognition commission reversals, bad-debt expense, "
                        "production rework, and cash retained for liquidity. Each item "
                        "needs one treatment and one ledger location. A cash buffer "
                        "is an asset allocation, not an additional reduction in profit."
                    ),
                    (
                        "Calculate cash needs using stated settlement delays and payment "
                        "timing. Compare peak funding requirements with available startup "
                        "capital rather than annual profit. Model the six-to-24-month "
                        "first-deal interval separately from the mature Base-case operation "
                        "to avoid premature hiring."
                    ),
                    (
                        "Reconcile the completed model with actual supplier quotes and "
                        "counterparty terms. Explain any mismatch between the stated "
                        "monthly operating range and fully loaded annual costs. Do "
                        "not conceal missing labor costs inside unpaid owner effort "
                        "or optimistic collection assumptions."
                    ),
                ],
                "fields": [
                    field(
                        "Canonical annual scenario bridge",
                        "textarea",
                        (
                            "Enter gross operator revenue, net margin, annual owner net "
                            "profit, implied total annual costs, and team configuration "
                            "for all three canonical scenarios. Show the arithmetic so "
                            "later channel models cannot silently change the scorecard."
                        ),
                        (
                            "Conservative: $80,000 revenue minus $64,000 costs equals "
                            "$16,000 owner net at 20%, with 1 FT + 3 C. "
                            "Base: $490,000 minus $330,750 equals $159,250 at 32.5%, "
                            "with 1 FT + 3 C. Scaled: $900,000 minus $495,000 "
                            "equals $405,000 at 45%, with 1 FT + 3 C."
                        ),
                    ),
                    field(
                        "Base advertising revenue construction",
                        "textarea",
                        (
                            "Define the traffic unit, annual eligible volume, recognized "
                            "yield, and invalid-traffic treatment for advertising. Identify "
                            "whether reported yield already reflects provider deductions "
                            "so fees and traffic adjustments are not deducted twice."
                        ),
                        (
                            "The illustrative Base advertising channel uses 10,000,000 "
                            "annual monetized sessions at $24.50 publisher revenue per "
                            "1,000 sessions: 10,000,000 / 1,000 × $24.50 = $245,000. "
                            "The yield is after provider deductions and traffic adjustments. "
                            "Pageviews and all-site sessions remain separate metrics; "
                            "neither replaces eligible sessions in this calculation."
                        ),
                    ),
                    field(
                        "Affiliate recognition and merchant-sales separation",
                        "textarea",
                        (
                            "Build affiliate revenue from accepted actions and earned "
                            "commissions, showing provisional actions and rejected actions "
                            "separately. Explain how underlying merchant order value is "
                            "used diagnostically without being counted as publisher sales "
                            "or cash receipts."
                        ),
                        (
                            "Track 10,000 provisional actions at $20 each, then remove "
                            "200 rejected actions before recognition. The remaining 9,800 "
                            "actions generate $196,000 publisher revenue. If each accepted "
                            "action corresponds to a $150 merchant order, associated "
                            "merchant sales equal $1,470,000; that amount never enters "
                            "the publisher's $490,000 Base revenue."
                        ),
                    ),
                    field(
                        "Sponsorship delivery and revenue reconciliation",
                        "textarea",
                        (
                            "Record sponsorship price, deliverables, recognition timing, "
                            "refund obligations, and cash schedule. Reconcile all channels "
                            "to annual operator revenue, then provide explicit channel "
                            "allocations for the other canonical scenarios without implying "
                            "those allocations are supplied scorecard facts."
                        ),
                        (
                            "Seven delivered packages at $7,000 produce $49,000; together "
                            "with $245,000 advertising and $196,000 affiliate revenue, Base "
                            "totals $490,000. Illustrative Conservative channels are "
                            "$40,000/$32,000/$8,000; Scaled channels are "
                            "$450,000/$360,000/$90,000, ordered advertising/affiliate/sponsorship. "
                            "Advance sponsor receipts remain unearned until the corresponding "
                            "contracted delivery occurs."
                        ),
                    ),
                    field(
                        "Fully loaded expense bridge",
                        "textarea",
                        (
                            "Allocate the Base cost envelope across labor, contractors, "
                            "production, technology, distribution, administration, and "
                            "collectibility expense. Compare fully loaded monthly costs "
                            "with the stated operating range and flag scope differences "
                            "rather than forcing an artificial reconciliation."
                        ),
                        (
                            "Illustrative Base costs are payroll $144,000, contractors "
                            "$72,000, production $48,000, technology $18,000, distribution "
                            "$18,000, administration $18,500, and bad-debt expense $12,250: "
                            "$330,750 total. Monthly all-in cost is $27,562.50, exceeding "
                            "the stated $2,500–$14,000 range. Require budget-scope clarification; "
                            "that range cannot represent every mature Base expense."
                        ),
                    ),
                    field(
                        "Scrub, defect, and collectibility treatment",
                        "textarea",
                        (
                            "Define distinct accounting treatments for rejected affiliate "
                            "actions, unusable editorial work, and recognized receivables "
                            "that may not collect. Identify where each amount already "
                            "appears in the model, including the review owner and "
                            "supporting adjustment evidence."
                        ),
                        (
                            "The $4,000 affiliate rejection is removed before the "
                            "$196,000 commission figure. A $12,250 collectibility provision "
                            "equals 2.5% of $490,000 recognized revenue and is already "
                            "inside Base costs. Editorial rework of $3,000 is contained "
                            "within the $48,000 production budget. No item receives a "
                            "second reserve deduction."
                        ),
                    ),
                    field(
                        "Receivables and operating cash floor",
                        "textarea",
                        (
                            "Calculate expected receivables and the operating cash floor "
                            "using an explicit day-count convention. Distinguish revenue "
                            "awaiting collection from cash required to pay expenses, and "
                            "explain whether a liquidity cushion is additional to or "
                            "already inside another reserve."
                        ),
                        (
                            "Use a 30-day planning month and uniform flows. Base monthly "
                            "revenue is $490,000 / 12; 45 days outstanding implies "
                            "$61,250 receivables. Forty-five days of $27,562.50 monthly "
                            "costs requires $41,343.75. Add a separately designated "
                            "$12,250 liquidity cushion for a $53,593.75 cash floor; "
                            "retaining cash creates no extra expense."
                        ),
                    ),
                    field(
                        "Startup funding and delayed monetization",
                        "textarea",
                        (
                            "Allocate startup capital between irreversible setup costs "
                            "and liquid runway. Test both early and late ends of "
                            "the first-deal interval, showing when the mature operating "
                            "cash floor becomes relevant and which spending changes "
                            "prevent a funding shortfall."
                        ),
                        (
                            "Select $100,000 within the $10,000–$60,000 startup range: "
                            "$20,000 setup and $80,000 liquid cash. At $3,000 monthly "
                            "pre-revenue burn, six months leaves $62,000; 24 months "
                            "leaves $8,000. The latter cannot fund the $53,593.75 "
                            "mature cash floor, so defer expansion or secure additional "
                            "capital before increasing obligations."
                        ),
                    ),
                    field(
                        "Content cohort contribution and payback",
                        "textarea",
                        (
                            "Measure a content cohort using direct production cost, "
                            "maintenance burden, and attributable earned revenue. State "
                            "how attribution works and distinguish contribution payback "
                            "from company-wide net profit after shared payroll, overhead, "
                            "and collection risk."
                        ),
                        (
                            "A 40-guide cohort costs $12,000 to produce and reaches "
                            "$2,000 monthly attributable publisher revenue with $400 "
                            "monthly direct maintenance costs. Steady-state contribution "
                            "is $1,600, giving 7.5 months of contribution payback after "
                            "that run rate begins. The initial search ramp and shared "
                            "operating expenses extend actual cash recovery."
                        ),
                    ),
                    field(
                        "Labor feasibility and sensitivity decision",
                        "textarea",
                        (
                            "Test whether each canonical team can be paid from its "
                            "implied expense envelope using documented wage, contractor, "
                            "and overhead assumptions. Preserve the canonical numbers "
                            "while clearly identifying execution constraints and scenarios "
                            "that cannot support the proposed staffing arrangement."
                        ),
                        (
                            "Conservative allows only $64,000 total annual expenses for "
                            "1 FT + 3 C and all other costs. Two $50,000 "
                            "loaded employee quotes alone exceed that envelope by "
                            "$36,000. Retain the canonical scenario for comparison, "
                            "but do not authorize those hires; document the unresolved "
                            "staffing feasibility before committing to operations."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The model owner verifies all three canonical profit equations, "
                    "excludes merchant sales, assigns each adjustment once, and documents "
                    "the $53,593.75 illustrative Base cash floor. Staffing feasibility "
                    "and the monthly-cost scope mismatch require explicit resolution "
                    "before commitments exceed available cash."
                ),
            },
            {
                "worksheet_id": "ws-03",
                "number": 3,
                "title": "Publishing Execution Ledger and Technical QA Pre-Flight",
                "purpose": (
                    "Convert editorial plans into traceable publication events with "
                    "evidence, ownership, and repeatable technical checks. Use one "
                    "operating ledger to connect briefs, rights, deployments, monetization, "
                    "and corrections so multi-site scale increases throughput without "
                    "multiplying duplicate pages, broken attribution, or unreviewed claims."
                ),
                "chapter_ref": "Q7, Q8",
                "instructions": [
                    (
                        "Assign permanent identifiers to domains, content items, source "
                        "assets, and revenue counterparties. Preserve those identifiers "
                        "through URL changes and contractor handoffs. A readable title "
                        "is useful for editors but cannot replace a stable join "
                        "key in the operating ledger."
                    ),
                    (
                        "Move each content item through explicit research, drafting, "
                        "review, technical validation, publication, and monitoring states. "
                        "Record who performed each transition and the evidence inspected. "
                        "Prevent automation from publishing a page whose required "
                        "rights or factual checks remain incomplete."
                    ),
                    (
                        "Run representative browser and crawl checks before releasing "
                        "a new template. Examine mobile rendering, canonical URLs, "
                        "structured data, advertising behavior, and conversion events. "
                        "A successful server response alone does not establish that "
                        "a page is useful or measurable."
                    ),
                    (
                        "Reconcile publication and revenue records at consistent intervals. "
                        "Track earned commissions separately from pending clicks and "
                        "settled cash. Investigate changes in event volume against "
                        "deployment timestamps before interpreting a sudden increase "
                        "as genuine audience growth or monetization improvement."
                    ),
                    (
                        "Prepare a reversible deployment and incident procedure before "
                        "expanding the site fleet. Store versioned templates and "
                        "restorable backups, test restoration, and name the person "
                        "who can stop a faulty release without waiting for "
                        "a weekly management meeting."
                    ),
                ],
                "fields": [
                    field(
                        "Portfolio entity and publication ledger",
                        "textarea",
                        (
                            "Define the identifiers and required columns linking domains, "
                            "content items, authors, sources, templates, and revenue "
                            "placements. Explain how version history survives URL changes "
                            "and how operators distinguish a draft, a published page, "
                            "and an archived asset."
                        ),
                        (
                            "Content ID WATER-0042 belongs to domain SITE-02 and "
                            "template COMPAT-03. Ledger columns include canonical URL, "
                            "source IDs, rights status, reviewer, publication timestamp, "
                            "last verification date, and deployment ID. A URL migration "
                            "changes the URL column and redirect record, while "
                            "WATER-0042 remains the stable identifier across analytics "
                            "and editorial systems."
                        ),
                    ),
                    field(
                        "Research brief and acceptance specification",
                        "textarea",
                        (
                            "Specify the audience question, required original evidence, "
                            "source hierarchy, exclusions, and editorial acceptance "
                            "criteria for one representative brief. Include concrete "
                            "checks that distinguish useful reporting from paraphrased "
                            "competitor pages or unsupported commercial comparisons."
                        ),
                        (
                            "Brief WATER-0042 answers whether Model A cartridges fit "
                            "Housing B. Require measured diameter, thread dimensions, "
                            "two owned photographs, manufacturer documentation, and "
                            "reviewer sign-off. Exclude unsupported health claims. "
                            "Acceptance requires a clear compatibility conclusion, "
                            "installation limitations, source dates, and a visible "
                            "correction route before affiliate links are inserted."
                        ),
                    ),
                    field(
                        "Source provenance and asset rights",
                        "textarea",
                        (
                            "Record where factual inputs and media originated, which "
                            "permissions apply, and whether licenses permit publication, "
                            "modification, and transfer. State how missing provenance "
                            "blocks an asset without unnecessarily stopping unrelated "
                            "pages whose evidence is complete."
                        ),
                        (
                            "Photograph IMG-117 was created by Contractor C under a "
                            "signed assignment covering publication and transfer. "
                            "Specification SRC-081 links to a dated manufacturer "
                            "manual; only necessary factual measurements are extracted. "
                            "A third-party illustration lacking permission stays out "
                            "of WATER-0042. The editor substitutes an original diagram "
                            "and records its source file."
                        ),
                    ),
                    field(
                        "Crawlability and canonical pre-flight",
                        "textarea",
                        (
                            "List the response, robots, sitemap, canonical, redirect, "
                            "and internal-link checks required before publication. "
                            "Distinguish crawling controls from indexing instructions "
                            "and define the evidence that confirms the intended "
                            "version of each page is accessible."
                        ),
                        (
                            "Screaming Frog checks 180 release URLs: each intended "
                            "page returns 200, carries a self-referencing canonical, "
                            "and appears in the sitemap. Staging requires authentication. "
                            "Retired URLs redirect directly to relevant replacements. "
                            "A page requiring noindex remains crawlable so crawlers "
                            "can read that directive; robots.txt is not treated "
                            "as an indexing-removal tool."
                        ),
                    ),
                    field(
                        "Structured data and rendered-page truth",
                        "textarea",
                        (
                            "Define which structured-data types accurately describe "
                            "visible content and which claims require supporting "
                            "evidence. Describe validation tools, representative samples, "
                            "and rejection conditions for markup that overstates "
                            "reviews, prices, availability, authorship, or product testing."
                        ),
                        (
                            "Apply Article and BreadcrumbList markup to 24 editorial "
                            "guides and validate representative pages with Google's "
                            "Rich Results Test and Schema.org Validator. Do not "
                            "invent aggregate ratings or offer availability. Author "
                            "names, dates, and article headlines match visible "
                            "content. Valid markup is a technical check, not a "
                            "promise of enhanced search presentation."
                        ),
                    ),
                    field(
                        "Performance and advertising quality",
                        "textarea",
                        (
                            "Set performance measurements, device conditions, ad "
                            "placement constraints, and escalation thresholds. Separate "
                            "laboratory diagnostics from field experience, and explain "
                            "how layout movement or heavy third-party scripts can "
                            "damage readers even when advertising yield improves."
                        ),
                        (
                            "Use Lighthouse for release diagnostics and field data "
                            "for the 75th-percentile targets: LCP at most 2.5 "
                            "seconds, INP at most 200 milliseconds, and CLS at "
                            "most 0.1. Reserve ad dimensions before loading. A "
                            "template showing CLS 0.18 returns to engineering "
                            "rather than shipping solely because its projected "
                            "ad yield is higher."
                        ),
                    ),
                    field(
                        "Attribution events and commission reconciliation",
                        "textarea",
                        (
                            "Define event names, content identifiers, affiliate "
                            "sub-identifiers, deduplication rules, and reconciliation "
                            "frequency. Explain why an outbound click is not "
                            "a completed transaction and how platform-confirmed "
                            "actions connect to earned revenue without exposing "
                            "unnecessary reader information."
                        ),
                        (
                            "Emit affiliate_click with content ID WATER-0042, "
                            "placement ID P03, and merchant code M02. Do not "
                            "send email addresses or full visitor URLs to "
                            "affiliate sub-identifiers. Weekly reconciliation compares "
                            "2,400 outbound clicks with 96 accepted actions "
                            "at $20, producing $1,920 earned commissions; "
                            "click volume remains an operational metric."
                        ),
                    ),
                    field(
                        "Financial ledger close and evidence retention",
                        "textarea",
                        (
                            "Specify the monthly close sequence connecting payer "
                            "statements, recognized revenue, receivables, cash, "
                            "adjustments, and sponsorship delivery records. Name "
                            "the reviewer and explain how unresolved differences "
                            "remain visible instead of being forced into "
                            "miscellaneous income."
                        ),
                        (
                            "For a sample month, statements support $20,000 "
                            "advertising, $15,000 accepted commissions, and $7,000 "
                            "delivered sponsorship: $42,000 recognized revenue. "
                            "Starting receivables of $50,000 plus $42,000 "
                            "earned minus $38,000 collected leave $54,000, "
                            "assuming no other adjustments. The bookkeeper "
                            "attaches statements and bank matches; the "
                            "portfolio lead reviews the bridge."
                        ),
                    ),
                    field(
                        "Deployment rollback and restoration drill",
                        "textarea",
                        (
                            "Describe the release artifact, backup scope, "
                            "restoration procedure, and measurable recovery targets. "
                            "Include both content and configuration, and identify "
                            "which failures require a template rollback versus "
                            "a data restoration or isolated monetization change."
                        ),
                        (
                            "Release SITE-02-R17 includes a versioned template, "
                            "database snapshot, media manifest, and redirect "
                            "map. A staging restoration recovers the site "
                            "within 45 minutes against a two-hour target. "
                            "Daily backups support a 24-hour recovery-point "
                            "target. If affiliate links break after deployment, "
                            "revert the link component first and preserve "
                            "new editorial records."
                        ),
                    ),
                    field(
                        "Publication acceptance and correction ownership",
                        "textarea",
                        (
                            "Record the final evidence bundle for a release, "
                            "including sample selection, unresolved defects, "
                            "publication authority, and post-release checks. "
                            "Set correction severity levels so factual "
                            "errors, broken pages, and cosmetic issues "
                            "receive proportionate responses and named owners."
                        ),
                        (
                            "Release 24 guides only after all 24 pass "
                            "rights, source, disclosure, and link checks; "
                            "manually inspect six across mobile and desktop "
                            "templates. Incorrect compatibility claims trigger "
                            "immediate correction or temporary withdrawal. "
                            "Broken monetization links receive same-day repair. "
                            "The editor records the correction, affected "
                            "URLs, reviewer, and verification timestamp."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The editor and technical owner sign the release ledger after "
                    "rights verification, canonical checks, event reconciliation, "
                    "and a successful restoration drill. Every published item has "
                    "an accountable reviewer and a documented correction path."
                ),
            },
            {
                "worksheet_id": "ws-04",
                "number": 4,
                "title": "Rights, Advertising, Privacy, Contracts, and Outreach Audit",
                "purpose": (
                    "Turn applicable statutory duties and commercial obligations into "
                    "specific publishing controls. Inventory copyright permissions, "
                    "endorsement disclosures, data processing, outreach practices, and "
                    "transfer rights while distinguishing legal requirements from "
                    "search-platform rules and individual monetization contracts across "
                    "every portfolio domain."
                ),
                "chapter_ref": "Q5, Q9",
                "instructions": [
                    (
                        "Map the publisher's entity, audience locations, subject matter, "
                        "data collection, and commercial relationships before selecting "
                        "requirements. Apply each rule to an actual activity and "
                        "responsible owner. Avoid copying a generic policy that "
                        "does not match the deployed services."
                    ),
                    (
                        "Inspect the live reader journey rather than reviewing "
                        "documents alone. Follow affiliate links, sponsorship placements, "
                        "email signup, tracking requests, and deletion requests. "
                        "Save dated evidence showing how disclosures and privacy "
                        "choices operate on representative desktop and mobile pages."
                    ),
                    (
                        "Review contracts for payment, editorial control, termination, "
                        "data use, assignment, and dispute handling. Match each "
                        "contract to the correct legal entity and domain. "
                        "Record provisions that could obstruct a media sale "
                        "or cause revenue to stop after ownership changes."
                    ),
                    (
                        "Separate copyright ownership, factual accuracy, publicity "
                        "permissions, and advertising substantiation. A permitted "
                        "photograph does not validate a product claim, and "
                        "a citation does not automatically authorize copying. "
                        "Route unresolved issues to the appropriate specialist "
                        "before publishing affected material."
                    ),
                    (
                        "Finish with an evidence-backed remediation list, ordered "
                        "by reader harm, statutory exposure, and operational "
                        "dependency. Assign dates and verification methods. "
                        "Close a finding only after the actual page, "
                        "contract, or processing configuration has been corrected "
                        "and independently checked."
                    ),
                ],
                "fields": [
                    field(
                        "Entity, jurisdiction, and operating permissions",
                        "textarea",
                        (
                            "Identify the publishing entity, operating locations, "
                            "audience markets, subject matter, and applicable "
                            "registration or licensing checks. Explain why "
                            "ordinary publishing permissions differ from regulated "
                            "professional services or selling products directly "
                            "to readers."
                        ),
                        (
                            "The operating company publishes home-maintenance "
                            "information and earns advertising, affiliate, and "
                            "sponsorship income; it does not sell filter "
                            "inventory or provide plumbing services. The "
                            "operations owner checks state entity registration "
                            "and local business-license requirements. Reviews "
                            "of professional-service expansion occur before "
                            "adding paid installation bookings or representing "
                            "the publisher as a licensed contractor."
                        ),
                    ),
                    field(
                        "Copyright ownership and permitted reuse",
                        "textarea",
                        (
                            "Document ownership or permission for text, "
                            "images, charts, source datasets, and commissioned "
                            "work. Address exclusive rights and any "
                            "reliance on fair use with fact-specific "
                            "analysis rather than assuming public availability "
                            "creates unrestricted reuse rights."
                        ),
                        (
                            "Under 17 U.S.C. § 106, copying and "
                            "adaptation require an applicable right or "
                            "exception. Contributor agreements include a "
                            "signed assignment meeting 17 U.S.C. § 204(a). "
                            "For a proposed comparison excerpt, document "
                            "the four 17 U.S.C. § 107 factors. "
                            "Credit alone does not authorize reproducing "
                            "a competitor's chart or product photographs."
                        ),
                    ),
                    field(
                        "Affiliate and sponsorship disclosure placement",
                        "textarea",
                        (
                            "Specify how material commercial connections "
                            "are disclosed near relevant recommendations "
                            "and links. Cite the applicable endorsement "
                            "framework, define mobile visibility checks, "
                            "and separate reader-facing disclosure from "
                            "technical link attributes used by search systems."
                        ),
                        (
                            "Apply 15 U.S.C. § 45 and 16 CFR "
                            "Part 255, including § 255.5 for material "
                            "connections. Before the first affiliate "
                            "recommendation, display: 'We earn commissions "
                            "from qualifying purchases through these links.' "
                            "Label paid articles as sponsored. Check "
                            "mobile visibility; rel=\"sponsored\" supports "
                            "link qualification but does not replace "
                            "the reader-facing explanation."
                        ),
                    ),
                    field(
                        "Review integrity and claim substantiation",
                        "textarea",
                        (
                            "Describe controls for product testing, review "
                            "authenticity, sponsor influence, and objective "
                            "performance claims. State which evidence "
                            "must exist before publication and how "
                            "the team handles paid relationships without "
                            "fabricating experience or suppressing legitimate criticism."
                        ),
                        (
                            "A filter comparison claiming a 20% flow "
                            "improvement requires dated measurements, defined "
                            "conditions, and reproducible calculations. Apply "
                            "15 U.S.C. § 45 and relevant provisions "
                            "of 16 CFR Part 465 to review "
                            "practices. Sponsors may correct factual "
                            "errors but cannot purchase invented testing, "
                            "fake testimonials, or a predetermined editorial "
                            "ranking."
                        ),
                    ),
                    field(
                        "Privacy applicability and data inventory",
                        "textarea",
                        (
                            "Inventory collected identifiers, purposes, vendors, "
                            "retention, disclosures, and applicable jurisdictional "
                            "tests. Distinguish legal applicability from "
                            "voluntary operating choices, and record who "
                            "verifies thresholds, geographic reach, and "
                            "processor arrangements as the portfolio grows."
                        ),
                        (
                            "Inventory IP addresses, analytics identifiers, "
                            "newsletter emails, affiliate click metadata, "
                            "and support requests. Evaluate California "
                            "applicability under Cal. Civ. Code "
                            "§ 1798.140(d), then applicable duties "
                            "under §§ 1798.100 and 1798.120. For "
                            "European reach, assess GDPR Article 3 "
                            "before documenting Article 6 lawful "
                            "bases, Article 13 notices, and Article "
                            "28 processor terms."
                        ),
                    ),
                    field(
                        "Tracking choices, rights requests, and retention",
                        "textarea",
                        (
                            "Define the actual controls for storage "
                            "access, opt-outs, deletion requests, vendor "
                            "propagation, and retention. Include operational "
                            "tests for applicable privacy signals and "
                            "explain how legal preservation requirements "
                            "affect deletion without retaining unrelated "
                            "reader data indefinitely."
                        ),
                        (
                            "For applicable California sale or sharing "
                            "activities, test opt-out preference signals "
                            "under 11 CCR § 7025. For relevant "
                            "European device storage, assess national "
                            "implementation of Directive 2002/58/EC "
                            "Article 5(3). Route requests to a "
                            "tracked queue, verify identity proportionately, "
                            "and apply documented retention periods "
                            "while preserving required accounting records."
                        ),
                    ),
                    field(
                        "Commercial email and partner outreach",
                        "textarea",
                        (
                            "Define the rules for sponsor prospecting "
                            "and newsletter promotion, including sender "
                            "identity, message accuracy, address sourcing, "
                            "suppression, and unsubscribe processing. Distinguish "
                            "United States requirements from stricter "
                            "rules that may apply to recipients "
                            "in other jurisdictions."
                        ),
                        (
                            "For United States commercial email, apply "
                            "15 U.S.C. § 7704: accurate headers, "
                            "nondeceptive subjects, required identification, "
                            "a valid postal address, and functioning "
                            "opt-out instructions. Honor opt-outs within "
                            "10 business days and keep the "
                            "mechanism available for at least 30 "
                            "days after sending. Review recipient-country "
                            "requirements before expanding the 40-contact "
                            "sponsor pilot."
                        ),
                    ),
                    field(
                        "Counterparty contracts and assignment clauses",
                        "textarea",
                        (
                            "Capture contractual rights governing delivered "
                            "work, payment disputes, account termination, "
                            "assignment, access to data, and post-sale "
                            "transition. Draft concrete commercial positions "
                            "and identify where a counterparty's standard "
                            "terms require written clarification before "
                            "revenue can support valuation."
                        ),
                        (
                            "Proposed sponsor language states: 'The "
                            "$7,000 fee covers one labeled article "
                            "and one newsletter placement; factual "
                            "review does not confer editorial ranking "
                            "control.' Separately record net-30 payment, "
                            "cancellation remedies, and assignment terms. "
                            "Network A requires written transfer "
                            "permission, so the exit model treats "
                            "continuity as conditional until that "
                            "permission is obtained."
                        ),
                    ),
                    field(
                        "Search-platform and licensed-data restrictions",
                        "textarea",
                        (
                            "List platform policies and data-license "
                            "restrictions independently of statutory duties. "
                            "Explain how link practices, scaled "
                            "publishing, automated queries, and source "
                            "reuse are monitored, including the "
                            "specific activity that stops when "
                            "permission or permitted access is absent."
                        ),
                        (
                            "Review Google's Search spam policies "
                            "for scaled content abuse, link spam, "
                            "and site reputation abuse. Use approved "
                            "APIs or manual research for measurement "
                            "where required; do not bypass access "
                            "restrictions. A licensed equipment dataset "
                            "permits derived compatibility summaries but "
                            "prohibits redistribution of raw records, "
                            "so the public template excludes "
                            "downloadable source tables."
                        ),
                    ),
                    field(
                        "Findings register and verification evidence",
                        "textarea",
                        (
                            "Record each finding with its affected "
                            "assets, requirement source, severity, owner, "
                            "deadline, and closure evidence. Make "
                            "the remediation concrete enough that "
                            "another operator can verify completion "
                            "without relying on an assurance "
                            "that the issue was discussed."
                        ),
                        (
                            "Finding RIGHTS-07 covers four unlicensed "
                            "installation images. The editor removes "
                            "them immediately, replaces them with "
                            "owned photographs within three working "
                            "days, and attaches signed assignments "
                            "and live-page captures. Finding DISC-03 "
                            "moves affiliate disclosures above the "
                            "first recommendation on 12 mobile "
                            "pages; a second reviewer verifies "
                            "all 12 placements."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Every applicable requirement has an owner and retrievable "
                    "evidence. Remove unlicensed assets, unsupported claims, and "
                    "undisclosed paid placements before publication; verify privacy "
                    "and outreach controls against the actual services and "
                    "audiences rather than a generic policy document."
                ),
            },
            {
                "worksheet_id": "ws-05",
                "number": 5,
                "title": "Automation, Audience Growth, and Risk Fallback Tracker",
                "purpose": (
                    "Automate repeatable detection and reporting while preserving "
                    "editorial judgment, data integrity, and reversible changes. "
                    "Connect technical audits, refresh queues, sponsor outreach, "
                    "owned-audience growth, and GEO observations to explicit "
                    "risk thresholds so the portfolio responds coherently "
                    "when rankings or counterparties deteriorate."
                ),
                "chapter_ref": "Q6, Q10",
                "instructions": [
                    (
                        "Map each proposed automation from authorized input "
                        "through transformation to operator action. Identify "
                        "credentials, rate limits, data retention, failure "
                        "signals, and ownership. Prefer systems that "
                        "produce reviewable evidence over systems that "
                        "silently change many published pages at once."
                    ),
                    (
                        "Establish a baseline before activating alerts "
                        "or refresh rules. Segment by domain, "
                        "template, geography, device, and content age "
                        "where sample sizes support interpretation. "
                        "A traffic decline needs context before "
                        "it becomes a publishing instruction or "
                        "a staffing decision."
                    ),
                    (
                        "Build the growth loop around useful "
                        "reader outcomes and measurable commercial "
                        "relationships. Combine original resources, newsletters, "
                        "partner introductions, and sponsor outreach. "
                        "Keep outreach personalized and permission-aware; "
                        "never substitute bulk message volume for "
                        "qualified counterparties or durable audience demand."
                    ),
                    (
                        "Test fallback actions under simulated "
                        "ranking loss, payer suspension, feed "
                        "failure, and inaccurate automated suggestions. "
                        "Measure detection time and recovery "
                        "effort. Ensure the technical owner "
                        "can disable a broken integration "
                        "without taking unrelated editorial operations "
                        "offline."
                    ),
                    (
                        "Review automation economics monthly using "
                        "verified time saved, error rates, "
                        "and total operating cost. Retire "
                        "workflows that add maintenance burden "
                        "without improving decisions. Expansion requires "
                        "stable inputs and demonstrated reliability, "
                        "not simply a successful demonstration "
                        "on one handpicked page."
                    ),
                ],
                "fields": [
                    field(
                        "Authorized automation inventory",
                        "textarea",
                        (
                            "List the technical-audit, content-refresh, "
                            "and revenue-reporting workflows with "
                            "input permissions, execution frequency, "
                            "output destination, service owner, "
                            "and failure behavior. Identify "
                            "which outputs are recommendations "
                            "and which limited actions may "
                            "execute automatically."
                        ),
                        (
                            "Run a weekly Screaming Frog "
                            "audit, a daily Search Console "
                            "refresh-priority job, and a monthly "
                            "payer-statement reconciliation. Store service "
                            "credentials in the project's secret "
                            "manager with least privilege. Jobs "
                            "write dated reports and alert "
                            "the assigned owner; none may "
                            "rewrite articles, change canonical "
                            "URLs, or issue invoices without "
                            "the defined review."
                        ),
                    ),
                    field(
                        "Refresh prioritization and editorial review",
                        "textarea",
                        (
                            "Define the signals used to "
                            "prioritize content refreshes, minimum "
                            "sample sizes, seasonal adjustments, "
                            "and required editorial evidence. "
                            "Explain why declining clicks "
                            "alone do not justify "
                            "rewriting accurate material or "
                            "changing stable URLs."
                        ),
                        (
                            "Queue pages with at least "
                            "1,000 impressions in each "
                            "28-day window and a "
                            "30% click decline, then "
                            "compare year-over-year seasonality and "
                            "query mix. WATER-0042 falls "
                            "from 400 to 260 clicks. "
                            "The editor checks product "
                            "changes and result-page shifts "
                            "before choosing a factual "
                            "update, improved presentation, or "
                            "no change."
                        ),
                    ),
                    field(
                        "Technical anomaly detection and routing",
                        "textarea",
                        (
                            "Set thresholds for crawl failures, "
                            "indexing directives, broken links, "
                            "and template regressions. Specify "
                            "the comparison population and "
                            "escalation owner so transient "
                            "noise does not trigger "
                            "site-wide changes or hide "
                            "a genuine production defect."
                        ),
                        (
                            "Alert when more than 2% "
                            "of the 1,200 monitored "
                            "URLs return unexpected errors "
                            "on two consecutive checks, "
                            "or when any production "
                            "template introduces noindex unintentionally. "
                            "A 36-URL error cluster "
                            "exceeds the 24-URL threshold. "
                            "The technical owner checks "
                            "deployment logs and upstream "
                            "availability before reverting the "
                            "affected component."
                        ),
                    ),
                    field(
                        "Revenue-reporting freshness and reconciliation",
                        "textarea",
                        (
                            "Specify statement arrival expectations, "
                            "freshness indicators, validation totals, "
                            "and handling of delayed "
                            "counterparty data. Explain how "
                            "the dashboard distinguishes estimated "
                            "performance from recognized revenue "
                            "and collected cash without "
                            "silently carrying stale figures "
                            "forward."
                        ),
                        (
                            "The dashboard shows separate "
                            "columns for provisional commissions, "
                            "accepted commissions, receivables, "
                            "and bank receipts. If "
                            "Network A's file misses "
                            "its expected date by "
                            "two business days, mark "
                            "the period as awaiting "
                            "validation and notify operations. "
                            "Do not copy last "
                            "month's $15,000 into current "
                            "recognized revenue or suppress "
                            "the freshness warning."
                        ),
                    ),
                    field(
                        "Owned-audience and editorial growth loop",
                        "textarea",
                        (
                            "Design a repeatable audience "
                            "loop connecting search visits "
                            "to useful subscriber benefits, "
                            "repeat engagement, and commercial "
                            "outcomes. State denominators and "
                            "measurement windows, and keep "
                            "subscriber acquisition metrics separate "
                            "from revenue recognition and "
                            "long-term retention."
                        ),
                        (
                            "Offer an original maintenance "
                            "calendar to relevant readers. "
                            "From 20,000 eligible monthly "
                            "sessions, 400 verified signups "
                            "represent a 2% signup "
                            "rate. Of those subscribers, "
                            "160 click a useful "
                            "follow-up guide within 30 "
                            "days. Record acquisition source "
                            "and unsubscribe activity; do "
                            "not assign a dollar "
                            "value until measurable earnings "
                            "support it."
                        ),
                    ),
                    field(
                        "Sponsor and partner outreach experiment",
                        "textarea",
                        (
                            "Define a narrow counterparty "
                            "segment, research method, outreach "
                            "message, follow-up limit, and "
                            "success metric. Track reasons "
                            "for rejection and suppression "
                            "so growth work improves "
                            "qualification rather than repeatedly "
                            "contacting unsuitable or uninterested "
                            "organizations."
                        ),
                        (
                            "Research 40 equipment manufacturers "
                            "whose products appear in "
                            "existing original tests. Send "
                            "individually reviewed proposals describing "
                            "audience evidence and the "
                            "$7,000 labeled package, with "
                            "one follow-up after seven "
                            "business days. Six replies, "
                            "three qualified calls, and "
                            "one signed agreement describe "
                            "the funnel; recognize revenue "
                            "only as contracted delivery "
                            "occurs."
                        ),
                    ),
                    field(
                        "GEO experiment integrity and referral evidence",
                        "textarea",
                        (
                            "Describe how citation observations "
                            "are sampled, compared, and "
                            "audited across answer products. "
                            "Set limits on automated "
                            "access and explain how "
                            "you avoid claiming causal "
                            "revenue growth from unstable "
                            "answer outputs or citation "
                            "counts alone."
                        ),
                        (
                            "Retain the same 30-question "
                            "panel across three products "
                            "for four weekly observations. "
                            "Citations rise from 9 "
                            "to 15 of 90 "
                            "observations, but referral traffic "
                            "shows only 18 sessions "
                            "and no accepted commissions. "
                            "Report the citation change "
                            "and small referral sample "
                            "separately. Preserve inaccurate "
                            "citations as defects rather "
                            "than counting them as "
                            "wins."
                        ),
                    ),
                    field(
                        "Ranking-loss response and spending fallback",
                        "textarea",
                        (
                            "Define a ranking-loss trigger, "
                            "diagnostic sequence, cash response, "
                            "and communication owner. Distinguish "
                            "measurement faults, seasonality, technical "
                            "breakage, and competitive changes "
                            "before committing to expensive "
                            "rewrites, migrations, or additional "
                            "paid traffic."
                        ),
                        (
                            "A sustained 30% search-click "
                            "decline across two 28-day "
                            "windows triggers instrument checks, "
                            "Search Console segmentation, manual-action "
                            "review, and template inspection. "
                            "Pause $4,000 monthly discretionary "
                            "new-content commissioning while preserving "
                            "essential updates. Use the "
                            "$343,000 revenue stress test "
                            "only as sensitivity analysis; "
                            "do not relabel it "
                            "as the canonical Conservative "
                            "case."
                        ),
                    ),
                    field(
                        "Counterparty and infrastructure fallback",
                        "textarea",
                        (
                            "Record contingency actions for "
                            "ad-provider suspension, merchant removal, "
                            "hosting disruption, and data-feed "
                            "failure. Include contractual limits, "
                            "recovery evidence, and reader "
                            "impact so backup arrangements "
                            "do not imply guaranteed "
                            "eligibility or equivalent monetization."
                        ),
                        (
                            "If Merchant M02 ends "
                            "its program, disable its "
                            "commercial links while preserving "
                            "accurate editorial comparisons. Evaluate "
                            "two qualified alternatives without "
                            "assuming acceptance or matching "
                            "$20 commissions. If hosting "
                            "fails, restore the tested "
                            "backup to the designated "
                            "replacement environment and verify "
                            "DNS, certificates, forms, and "
                            "content before resuming normal "
                            "promotion."
                        ),
                    ),
                    field(
                        "Automation return and control review",
                        "textarea",
                        (
                            "Calculate the economic value "
                            "of each workflow from "
                            "verified operator time saved, "
                            "maintenance time, tool costs, "
                            "and error correction. Define "
                            "a retirement threshold and "
                            "a review cadence that "
                            "keeps operational complexity proportional "
                            "to portfolio size."
                        ),
                        (
                            "An audit workflow saves "
                            "eight hours monthly at "
                            "a $45 internal hourly "
                            "cost, creating $360 of "
                            "capacity value. Tool expense "
                            "is $120 and maintenance "
                            "takes two hours worth "
                            "$90, leaving $150 monthly "
                            "net capacity value. This "
                            "is not additional recognized "
                            "revenue. Retire or redesign "
                            "the workflow if repeated "
                            "false alerts erase that "
                            "benefit."
                        ),
                    ),
                ],
                "completion_gate": (
                    "Each active workflow has authorized inputs, an accountable "
                    "owner, freshness checks, and a tested failure response. "
                    "The team demonstrates one ranking-loss drill and one "
                    "counterparty-loss drill without publishing unsupported claims "
                    "or changing canonical financial scenarios."
                ),
            },
            {
                "worksheet_id": "ws-06",
                "number": 6,
                "title": "30-Day Launch Sprint, Pod Scorecard, and Exit Ledger",
                "purpose": (
                    "Organize the first month around evidence, controlled production, "
                    "and reliable measurement rather than immediate revenue promises. "
                    "Give the small team a disciplined scorecard and build "
                    "transferable records from day one so future growth "
                    "or a media exit can withstand buyer diligence."
                ),
                "chapter_ref": "Q11, Q12",
                "instructions": [
                    (
                        "Treat the 30-day sprint as an "
                        "operating-system launch, not the full "
                        "search maturation period. The canonical "
                        "first-deal interval remains six to "
                        "24 months. Select deliverables that "
                        "the team controls and document "
                        "external dependencies such as indexing "
                        "and monetization acceptance."
                    ),
                    (
                        "Assign each deliverable to a "
                        "single accountable owner and identify "
                        "supporting contributors. Match staffing "
                        "commitments to actual cash availability. "
                        "The canonical team configurations are "
                        "planning references, not evidence that "
                        "the startup budget can immediately "
                        "support every proposed employee and "
                        "contractor."
                    ),
                    (
                        "Review a compact weekly scorecard "
                        "covering production quality, indexable "
                        "inventory, audience evidence, earned "
                        "revenue, collections, and cash coverage. "
                        "Keep leading indicators separate "
                        "from financial outcomes. Escalate "
                        "changes that affect solvency "
                        "or factual reliability before "
                        "optimizing publication volume."
                    ),
                    (
                        "Create the exit-readiness ledger "
                        "while records are easy to "
                        "collect. Preserve contributor rights, "
                        "domain ownership, contracts, analytics "
                        "definitions, and monthly reconciliations. "
                        "Do not wait for a "
                        "buyer to discover that "
                        "critical accounts belong personally "
                        "to a departing contributor."
                    ),
                    (
                        "Finish the sprint with a "
                        "written continue, revise, or "
                        "pause decision. Compare completed "
                        "evidence against the original "
                        "spending ceiling and risk "
                        "thresholds. Document unfinished work "
                        "honestly and authorize only "
                        "the next bounded operating "
                        "period supported by available "
                        "cash and reliable data."
                    ),
                ],
                "fields": [
                    field(
                        "Thirty-day mission and spending boundary",
                        "textarea",
                        (
                            "State the sprint's controlled "
                            "deliverables, maximum spending, evidence "
                            "requirements, and excluded promises. "
                            "Connect the launch scope "
                            "to the longer monetization "
                            "timeline so early technical "
                            "completion is not confused "
                            "with a validated profitable "
                            "publishing business."
                        ),
                        (
                            "Within 30 days, complete "
                            "the 120-query sample, publish "
                            "24 reviewed guides, instrument "
                            "all commercial links, and "
                            "test restoration. Cap the "
                            "pilot at $12,000, already "
                            "included within the $20,000 "
                            "setup allocation. Do not "
                            "forecast first-month revenue; the "
                            "canonical first-deal window remains "
                            "six to 24 months, "
                            "subject to actual audience "
                            "and counterparty development."
                        ),
                    ),
                    field(
                        "Days 1–7 underwriting and foundation",
                        "textarea",
                        (
                            "Schedule the first week's "
                            "research, rights verification, counterparty "
                            "qualification, entity setup checks, "
                            "and measurement design. Specify "
                            "owners and tangible outputs "
                            "that must exist before "
                            "bulk commissioning or technical "
                            "template expansion begins."
                        ),
                        (
                            "The portfolio lead completes "
                            "120 query observations and "
                            "contacts two monetization providers. "
                            "The editor finalizes 24 "
                            "briefs and rights requirements. "
                            "The technical owner creates "
                            "a staging environment and "
                            "event specification. Spend at "
                            "most $2,500 this week, "
                            "with source exports, supplier "
                            "quotes, and signed contributor "
                            "terms attached to the "
                            "launch ledger."
                        ),
                    ),
                    field(
                        "Days 8–14 production and template proof",
                        "textarea",
                        (
                            "Define the second week's "
                            "content production batch, template "
                            "validation, source collection, and "
                            "review sampling. Explain how "
                            "early defects change the "
                            "remaining work plan before "
                            "the team repeats the "
                            "same error across the "
                            "portfolio."
                        ),
                        (
                            "Produce eight guides and "
                            "one compatibility template with "
                            "owned images and verified "
                            "measurements. Inspect all eight "
                            "for rights, claims, disclosures, "
                            "canonical behavior, and affiliate "
                            "events. A missing model "
                            "dimension pauses only the "
                            "affected compatibility page. Spend "
                            "at most $3,000 this "
                            "week and update the "
                            "brief template before commissioning "
                            "the next batch."
                        ),
                    ),
                    field(
                        "Days 15–21 controlled publication and outreach",
                        "textarea",
                        (
                            "Plan the third week's "
                            "publication, sitemap submission, outreach "
                            "preparation, subscriber offer, and "
                            "monitoring activities. Identify which "
                            "results depend on external "
                            "systems and define the "
                            "evidence needed to confirm "
                            "successful delivery without claiming "
                            "immediate search visibility."
                        ),
                        (
                            "Publish the first eight "
                            "guides and finish drafts "
                            "for the remaining 16. "
                            "Submit the sitemap through "
                            "Search Console, launch the "
                            "maintenance-calendar signup, and research "
                            "40 sponsor prospects. Spend "
                            "at most $3,500 this "
                            "week. Record submitted, discovered, "
                            "indexed, and receiving-clicks states "
                            "separately; sitemap submission alone "
                            "does not establish indexing "
                            "or rankings."
                        ),
                    ),
                    field(
                        "Days 22–30 reconciliation and next-period decision",
                        "textarea",
                        (
                            "Describe final publication checks, "
                            "cash reconciliation, recovery testing, "
                            "baseline reporting, and the "
                            "decision meeting. Define how "
                            "unfinished deliverables are recorded "
                            "and what evidence supports "
                            "the next spending authorization "
                            "rather than automatic continuation "
                            "of the original plan."
                        ),
                        (
                            "Publish the remaining 16 "
                            "guides after individual review, "
                            "restore a staging backup, "
                            "and reconcile all pilot "
                            "invoices. Week-four spending is "
                            "capped at $3,000, completing "
                            "the $12,000 pilot ceiling. "
                            "The lead reviews cash, "
                            "defects, counterparty responses, and "
                            "early search observations, then "
                            "authorizes a bounded 60-day "
                            "maintenance period or documents "
                            "a pause."
                        ),
                    ),
                    field(
                        "Pod ownership and canonical staffing",
                        "textarea",
                        (
                            "Map editorial, technical, commercial, "
                            "and reporting responsibilities to "
                            "the canonical small-team structure. "
                            "Distinguish role coverage from "
                            "immediate hiring commitments, and "
                            "identify backup ownership so "
                            "critical operations remain functional "
                            "during contributor absence or "
                            "turnover."
                        ),
                        (
                            "Base role design uses "
                            "1 FT + 3 C: "
                            "a portfolio lead and "
                            "managing editor, supported by "
                            "technical SEO, subject review, "
                            "writing, and design contractors. "
                            "Scaled remains 3 FT "
                            "+ 5 C, eight "
                            "people total. Initial engagements "
                            "follow funded scopes; this "
                            "role map does not "
                            "override the Conservative labor "
                            "feasibility issue or authorize "
                            "unfunded hiring."
                        ),
                    ),
                    field(
                        "Weekly pod KPI scorecard",
                        "textarea",
                        (
                            "Select a small set "
                            "of leading and lagging "
                            "indicators with definitions, reporting "
                            "owners, and response thresholds. "
                            "Include quality and liquidity "
                            "alongside production volume so "
                            "the team cannot improve "
                            "its apparent performance by "
                            "publishing defective pages or "
                            "ignoring receivables."
                        ),
                        (
                            "Week four targets are "
                            "24 reviewed guides live, "
                            "zero unresolved critical factual "
                            "defects, 100% commercial-link instrumentation, "
                            "and one verified restoration. "
                            "Report actual indexed URLs, "
                            "search clicks, accepted commissions, "
                            "and cash without inventing "
                            "targets already achieved. At "
                            "mature Base scale, compare "
                            "available cash with the "
                            "$53,593.75 floor and investigate "
                            "overdue payer balances weekly."
                        ),
                    ),
                    field(
                        "Exit evidence room and asset ownership",
                        "textarea",
                        (
                            "List the records a "
                            "buyer would need to "
                            "verify ownership, earnings quality, "
                            "traffic durability, operational continuity, "
                            "and transfer feasibility. Assign "
                            "update frequency and access "
                            "controls so sensitive contracts "
                            "and reader information are "
                            "not unnecessarily exposed during "
                            "diligence."
                        ),
                        (
                            "Maintain domain-registration evidence, contributor "
                            "assignments, source licenses, 24 "
                            "months of monthly revenue "
                            "bridges when available, analytics "
                            "definitions, deployment records, and "
                            "counterparty assignment clauses. Begin "
                            "with the records actually "
                            "created rather than fabricating "
                            "history. Provide staged read-only "
                            "buyer access and aggregated "
                            "audience reports; exclude raw "
                            "subscriber addresses from preliminary "
                            "marketing materials."
                        ),
                    ),
                    field(
                        "Illustrative valuation and proceeds bridge",
                        "textarea",
                        (
                            "Build a clearly labeled "
                            "exit sensitivity from canonical "
                            "profit, an explicit multiple "
                            "assumption, transaction costs, debt, "
                            "and working-capital treatment. Explain "
                            "which earnings normalization and "
                            "contract-transfer issues must be "
                            "resolved before using the "
                            "sensitivity in negotiations."
                        ),
                        (
                            "Using Base owner net "
                            "of $159,250 only as "
                            "a preliminary proxy, an "
                            "assumed 3.0× multiple implies "
                            "$477,750 enterprise value. With "
                            "8% transaction costs of "
                            "$38,220 and no debt, "
                            "the illustration leaves $439,530 "
                            "before taxes, escrow, and "
                            "cash or working-capital adjustments. "
                            "Buyer-accepted transferable earnings require "
                            "separate normalization and may "
                            "differ from owner net."
                        ),
                    ),
                    field(
                        "Continue, revise, pause, and handoff record",
                        "textarea",
                        (
                            "Write the final sprint "
                            "decision, remaining risks, next-period "
                            "budget, accountable owners, and "
                            "handoff evidence. State exactly "
                            "what has been completed "
                            "and what remains unverified "
                            "so future operators do "
                            "not mistake launch activity "
                            "for proven commercial performance."
                        ),
                        (
                            "Continue maintenance for 60 "
                            "days at a $3,000 "
                            "monthly ceiling after verifying "
                            "24 published guides, source "
                            "rights, event accuracy, and "
                            "restoration. First-deal timing, durable "
                            "rankings, and mature revenue "
                            "remain unverified. The lead "
                            "owns cash reviews, the "
                            "editor owns corrections, and "
                            "the technical contractor owns "
                            "monitoring. Pause expansion if "
                            "projected cash falls below "
                            "the agreed phase-specific minimum."
                        ),
                    ),
                ],
                "completion_gate": (
                    "The sprint owner records actual completion, reconciled spending, "
                    "tested recovery, and the next-period decision. The exit "
                    "ledger contains authentic ownership and operating evidence; "
                    "canonical profits remain separate from valuation assumptions, "
                    "unearned revenue, and unverified future performance."
                ),
            },
        ],
    }
