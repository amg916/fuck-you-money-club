"""Volume 003: Digital Product Empire, chapter Q12."""

CHAPTER_12 = {
    "id": "Q12",
    "chapter_id": "Q12",
    "chapter_number": 12,
    "question_number": 12,
    "slug": "first-30-days-digital-product-launch-plan",
    "question_prompt": "Q12: How Do You Launch and Verify a Cash-Flowing Digital Product in 30 Days?",
    "kicker": "Q12 / THE BIG MONEY PLAYBOOKS",
    "title": "The First 30 Days: From Zero to Verified Cash-Flowing SKU",
    "subtitle": "Day-by-Day Validation, MoR Checkout Wiring, Pre-Sale Proof, SLO Funnel Launch & Kill/Scale Decision Gates",
    "layout_template": "thirty_day_plan",
    "reading_time_minutes": 14,
    "executive_summary": "Thirty days should produce a paid, delivered, reconciled SKU, not a polished folder of speculative assets. Start with repeated buyer pain, sell a tightly scoped outcome, and use an approved merchant of record before collecting money. Build only what the first buyers purchased. Wire delivery evidence, refunds, and acquisition attribution before increasing traffic. This sprint assigns every day an artifact and every week a numeric stop condition. A profitable advertisement is not a profitable company: distinguish gross billings, retained revenue, contribution, labor, and withdrawable cash. Scale only the cohort that survives that reconciliation.",
    "key_metrics": [
        {"label": "Pre-sale proof", "value": "5 / 100", "context": "Five independent buyers from 100 qualified offer-page visitors during a 72-hour test.", "note": "Illustrative decision threshold, not a conversion benchmark; lower traffic means insufficient evidence."},
        {"label": "Paid learning budget", "value": "$350 maximum", "context": "$50/day combined across two creatives on days 15-21.", "note": "A capped experiment; pause earlier when the predefined loss threshold is reached."},
        {"label": "Small-team economic range", "value": "$10,000-$440,000", "context": "Illustrative annual modeled net contribution after budgeted operating labor.", "note": "Conservative through Scaled scenarios; 1 FT + 3 C, not projected first-month earnings."},
    ],
    "sections": [
        {
            "heading": "Days 1-7: Sell one bounded outcome before building the library",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 1: choose one buyer, one expensive recurring task, and one observable finished result. Record twenty relevant ads from public ad libraries, including promise, price, format, and destination; longevity is a research clue, not proof of profitable spend. Day 2: collect twenty distinct Reddit or search discussions in which buyers describe the same task, failed alternatives, and purchase constraints. Preserve links and dates, remove personal identifiers from working notes, and separate firsthand complaints from promotional replies. Day 3: conduct five short buyer conversations and rank pains by frequency, urgency, existing expenditure, and whether a downloadable asset can actually resolve them. Select one problem supported by three independent evidence types. Reject ideas requiring custom implementation for every customer unless that work is explicitly priced. The artifact is a one-page evidence brief, not a spreadsheet claiming that search volume equals demand.",
                "Day 4: define three tiers around the same result: a $39 starter workflow, a $99 implementation bundle, and a $249 team license with bounded asynchronous support. Specify deliverables, permitted users, exclusions, delivery date, and support response window for each. Submit the merchant-of-record account application immediately with accurate business, product, banking, and ownership details; underwriting timing is outside the sprint's control. Confirm that the provider accepts this product category and pre-sales, and identify settlement delays, reserves, refund charges, tax handling, and supported upsell flows. Start the paid test only after the account is usable. If acceptance slips, use a clearly labeled unpaid reservation page and move the paid clock rather than describing reservations as revenue. Name the person accountable for customer delivery even when the merchant of record is the seller on the receipt.",
                "Days 5-7: run a full 72-hour pre-sale test against one unchanged offer and log unique qualified visits, independent buyers, gross collected funds, objections, and requested refunds. A provisional pass requires five unrelated paying buyers from at least 100 qualified visitors, without founder-friend purchases or discounts that erase contribution. Fewer visitors produces an incomplete test, not a failed market. Zero purchases after 100 qualified visits stops the build; one to four purchases earns one tightly scoped positioning revision, not a month of speculative production. Publish an honest delivery date and keep pre-sale funds available for refunds. The merchandise shipping framework in 16 CFR Part 435 matters where covered merchandise is sold, but its application to a pure digital download must not be assumed. Regardless, record the actual delivery promise and promptly resolve any missed date.",
            ],
            "table": {
                "caption": "30-Day Milestone & Kill-Criteria Table",
                "headers": ["Window", "Required milestone", "Kill or hold criterion", "Next funded action"],
                "rows": [
                    ["Days 1-7", "Pain brief, three tiers, usable MoR, 72-hour paid test", "0/100 qualified visitors buy: stop build; fewer than 100: evidence incomplete", "5+ independent buyers: fund only the promised v1.0"],
                    ["Days 8-14", "Delivered modules, IP ledger, tested checkout and refund events", "Any missing entitlement, duplicate charge, or unlicensed asset: hold launch", "Repair defect and replay affected event sequence"],
                    ["Days 15-21", "Organic distribution and capped $350 SLO experiment", "Creative spends $80 with zero attributed orders: pause it", "Keep buyer-level source records; do not infer profit from clicks"],
                    ["Days 22-30", "Reconciled cohort, onboarding revision, two partner pilots", "Negative contribution after one controlled repair: stop paid acquisition", "Scale only with 20+ delivered paid orders and the stated margin tests"],
                ],
            },
        },
        {
            "heading": "Days 8-14: Deliver modular v1.0 and make every payment reconstructible",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 8: turn the purchased promise into three modules: the core asset, a worked example, and a short implementation checklist. Define completion as the buyer producing the promised output, not consuming hours of video. Day 9: build the core asset and have someone outside production follow it without coaching. Day 10: finish the example and checklist, then record every third-party component in an IP ledger containing creator, source, license version, commercial-use permission, redistribution limits, and proof of purchase. Obtain written contractor assignments or sufficient licenses before accepting deliverables; a paid invoice alone does not settle ownership. Check fonts, screenshots, stock media, source files, and sample datasets separately. Ship original examples rather than repackaged competitor materials. Freeze v1.0 scope when the promised task works; optional lessons belong in a later backlog, not the launch dependency chain.",
                "Day 11: wire a two-step checkout that collects necessary buyer details first and then displays the complete price and payment action. Add an optional $19 order bump and a $79 post-purchase one-click upsell only where the merchant supports a properly authorized additional charge. Keep both unselected until the buyer acts, and ensure declining either preserves the original purchase. Day 12: test successful payment, failed payment, duplicate webhook, delayed webhook, partial refund, full refund, and an abandoned upsell. Grant access from verified server-side payment state, not the browser success page. Use provider event identifiers for idempotency and reconcile entitlements to order lines. For any recurring tier, 15 U.S.C. section 8403 requires clear material terms, express informed consent, and simple mechanisms to stop recurring charges. Keep launch tiers one-time unless recurring value and cancellation operations are actually implemented.",
                "Day 13: create an evidence chain connecting checkout authorization, payment reference, product version, delivery timestamp, account access, and support history. Verify webhook signatures, restrict evidence access, and define retention around actual processor requirements; never store raw card details. Visa CE 3.0 webhook logging is supporting infrastructure, not automatic dispute protection. Eligible disputes require qualifying historical transactions and matching data under the network's rules, which a new store may not possess. Confirm current eligibility and required fields with the merchant or processor instead of manufacturing history or promising chargeback immunity. Day 14: deliver to pre-sale customers, reconcile each order to access and receipt, and complete a real refund test using the provider's permitted process. A missing entitlement or duplicate charge stops wider traffic until repaired. Keep reserve balances distinct from funds available to pay contractors this week.",
            ],
            "sop_steps": [
                {"step": 1, "title": "Define the event contract", "action": "Map order, payment, refund, and entitlement states.", "detail": "Store provider references and product versions; document who owns each transition."},
                {"step": 2, "title": "Authenticate and deduplicate", "action": "Verify signatures and process each event idempotently.", "detail": "Replay duplicate and out-of-order events without granting duplicate benefits or recreating refunded access."},
                {"step": 3, "title": "Deliver and evidence", "action": "Connect verified payment to the purchased files and receipt.", "detail": "Retain timestamps and appropriate access evidence without collecting unnecessary sensitive data."},
                {"step": 4, "title": "Refund and reconcile", "action": "Test full and partial refunds against order-line entitlements.", "detail": "Match the merchant ledger, customer communication, access state, and settlement adjustment."},
            ],
        },
        {
            "heading": "Days 15-21: Launch a capped SLO experiment, not a traffic bonfire",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 15: publish one useful Reddit walkthrough where community rules allow commercial participation, disclose your connection, and answer the actual question before mentioning the product. Publish a YouTube demonstration showing the completed workflow, its constraints, and a sample output rather than an earnings montage. Start the self-liquidating offer, or SLO, experiment at $50 daily total, split $25 between two creative angles pointing to the same page. Treat self-liquidating as the test hypothesis: front-end contribution must cover acquisition, not merely generate receipts. Day 16: review comment quality, checkout errors, and delivery failures before touching budgets. Tag each channel and creative, preserve order-level source data, and deduplicate cross-device or repeated purchases where supportable. Organic production time still has a cost, even when platform clicks have no invoice. Keep that labor visible instead of presenting organic acquisition as economically free.",
                "Day 17: introduce a comment-to-DM trigger on a platform that supports the workflow, with a clear invitation to request the asset and only the promised follow-up. Do not scrape commenters into an unsolicited sequence. Day 18: test SparkLoop newsletter co-registration through the account's available partner functionality, with an explicit subscriber choice and a record of source and permission. Verify current availability, commercial terms, eligible placements, and suppression behavior before funding it. Measure confirmed subscriptions, seven-day engagement, qualified product visits, purchases, and refunds separately; a cheap subscriber who never sees the offer is not validated demand. Keep newsletter acquisition costs outside the $350 ad cap unless you deliberately revise the written budget. Use a small separately recorded allocation, or defer the paid placement if cash is constrained. Never purchase a subscriber count and relabel it a customer cohort.",
                "Day 19: inspect the two creative cohorts without declaring a winner from click-through rate. If a creative spends $80 with zero attributed purchases after allowing the chosen attribution delay, pause it and examine audience fit, page promise, and payment failures. This is a loss-control rule, not statistical proof that the market is dead. Day 20: change only one weak element, such as the first demonstration frame or the stated use case, and record the revision time so cohorts remain separable. Day 21: close the seven-day experiment at no more than $350 in ad spend, export orders and costs, and retain screenshots of the actual offers served. Do not restart the budget because an unprofitable ad has impressive engagement. Five orders can justify another bounded learning test; they cannot establish stable acquisition economics or support a large contractor commitment.",
            ],
            "table": {
                "caption": "Forensic launch diagnostics",
                "headers": ["Naive Trap", "Detection Metric", "Durable Operator Fallback"],
                "rows": [
                    ["Treat ad longevity as proof of profit", "No observed spend, margin, or refund data", "Use ads to discover positioning; validate with independent paid orders"],
                    ["Call every email address demand", "Confirmed subscribers without qualified visits or purchases", "Audit permission and engagement, then calculate buyer conversion by source"],
                    ["Declare SLO success from gross ROAS", "Gross receipts exceed ads while contribution stays negative", "Deduct refunds, fees, fulfillment, support, and acquisition before expanding"],
                    ["Treat CE 3.0 logging as immunity", "Missing eligible transaction history or required matching fields", "Retain genuine delivery evidence and confirm eligibility with the processor"],
                    ["Scale a noisy creative winner", "Fewer than 20 delivered paid orders in the decision cohort", "Hold spend and extend the bounded observation window"],
                ],
            },
        },
        {
            "heading": "Days 22-30: Audit the cohort, repair onboarding, then decide",
            "epistemic_status": "operating_framework",
            "paragraphs": [
                "Day 22: export order-level billings, taxes, refunds, merchant fees, affiliate charges, ad spend, support time, and settlement status into one cohort ledger. Group by acquisition source and purchase date rather than mixing pre-sale enthusiasts with cold traffic. Day 23: observe five customers attempting their first useful output and classify failures as unclear instructions, broken assets, unrealistic promise, or wrong audience. Day 24: repair the largest repeated onboarding failure with a shorter start page, a completed example, or a corrected file; do not bury refund instructions to manufacture retention. Day 25: send a focused activation message to customers who have not started, inviting a reply about the specific obstacle. Compare activation and support contacts before and after the change, while noting different cohort ages. Refund reduction is valuable only when customers receive the promised result, not when requesting help becomes harder.",
                "Day 26: invite two relevant affiliate partners to a bounded pilot with the finished product, approved factual claims, clear commission terms, and a disclosure requirement. Pay commissions on retained eligible sales after the defined refund window, and explain reversal treatment before anyone promotes. Day 27: inspect partner links, attribution precedence, duplicate orders, and coupon leakage; do not credit the same acquisition to two channels without recording the actual double cost. Day 28: calculate contribution by cohort and isolate unpaid labor from cash expenses. Day 29: compare the results to the written Kill, Fix, and Scale rules, including the size and age of the sample. Day 30: publish a one-page internal decision with orders, delivered customers, refunds, support hours, contribution, reserve balances, and the next spending limit. A signed-off spreadsheet without matched settlement records is still an estimate of cash, not verified cash flow.",
                "Kill paid acquisition when the cohort remains contribution-negative after one documented offer or onboarding repair and the capped retest budget is exhausted. Fix when retained demand exists but activation falls below 70% within seven days, delivery fails, or support exceeds twenty minutes per buyer. Scale only after at least twenty delivered paid orders, positive contribution after acquisition, observed refunds no higher than 5% among orders aged fourteen days, and acquisition cost no greater than 70% of pre-acquisition contribution per order. These are internal thresholds, not industry averages or statistical confidence claims. Fourteen days does not mature every refund or dispute; maintain a forward reserve and extend observation where terms require it. If evidence qualifies, raise the daily budget by 20%, observe three full days, and reverse the increase if economics deteriorate. Otherwise finish day 30 with an explicit hold, not a fabricated success.",
            ],
            "callout": {
                "kind": "OPERATOR GATE",
                "title": "Day 30 buys a decision, not a success story",
                "body": "A launch is cash-flowing only when delivered sales reconcile to receipts and current cash obligations. Positive cohort contribution alone does not establish business profitability.",
                "items": [
                    "Kill: negative contribution persists after one bounded repair and retest.",
                    "Fix: buyers exist, but activation, delivery, support, or checkout fails the stated threshold.",
                    "Scale: at least 20 delivered paid orders meet margin, acquisition, and aged-refund tests.",
                    "Hold: traffic, settlement, or refund-window evidence is incomplete; preserve remaining cash.",
                ],
            },
        },
        {
            "heading": "Price the experiment against annual economics, not launch-day screenshots",
            "epistemic_status": "illustrative_model",
            "paragraphs": [
                "Use a worked order model before approving another dollar of spend. Assume a $39 entry product, a $19 bump accepted by 25% of buyers, and a $79 upsell accepted by 10%. Expected gross billings per initial buyer are $51.65, excluding separately collected sales tax. Deduct a modeled 5% refund allowance of $2.58, merchant fees of 6% plus $0.50 totaling $3.60, and $5.00 of delivery and variable support cost. Pre-acquisition contribution is $40.47; at $28 customer acquisition cost, contribution after acquisition is $12.47. The proposed scale ceiling is 70% of $40.47, or $28.33, so $28 only narrowly qualifies. Actual fee bases, additional transaction charges, refund patterns, and support usage replace these assumptions. Repeat the calculation for each channel, adding affiliate commissions where incurred, rather than using this blended illustration to conceal an unprofitable paid cohort.",
                "The annual planning cases are Conservative at $50,000 gross billings and 20% modeled net contribution, producing $10,000; Base at $425,000 and 37.5%, producing $159,375; and Scaled at $800,000 and 55%, producing $440,000. These are scenario assumptions, not first-month targets or evidence of achievable margins. Each uses a nominal team of 1 FT + 3 C: one full-time owner-operator and three fractional contractors covering production, distribution, and support. Cost envelopes must include refunds, merchant fees, acquisition, tools, and budgeted operating labor. The Conservative envelope is only $40,000, which generally cannot fund a market-rate full-time salary plus three substantial retainers. It therefore requires very small contractor allocations and constrained owner compensation; disclose imputed owner labor separately. Higher margins require demonstrated operating leverage, not simply multiplying volume while freezing workload, acquisition cost, and refund exposure.",
                "Separate the economic ledger from the treasury ledger on the final review. Gross billings are customer charges before refunds and exclude tax collected for government; modeled net contribution here is the residual after the stated operating cost envelope, before income tax, financing, and exceptional costs. Cash available additionally depends on settlement timing, merchant reserves, contractor payables, and customer refund obligations. South Dakota v. Wayfair removed the physical-presence barrier to state sales-tax collection duties; it did not create one nationwide threshold or make every digital product taxable. Confirm the merchant-of-record contract's seller role and covered jurisdictions, then assess direct sales or excluded transactions separately. Do not count tax collections as product margin. A verified SKU has a reproducible customer outcome and a reconciled transaction trail; a sustainable business also pays for the operator's time and survives a less favorable cohort next month.",
            ],
            "table": {
                "caption": "Worked SLO unit economics and annual small-team scenarios",
                "headers": ["Model line", "Calculation", "Result", "Boundary"],
                "rows": [
                    ["Expected gross per buyer", "$39 + (25% x $19) + (10% x $79)", "$51.65", "Illustrative attach rates; sales tax excluded"],
                    ["Pre-acquisition contribution", "$51.65 - $2.58 refunds - $3.60 fees - $5.00 service", "$40.47", "Rounded model; replace with merchant ledger"],
                    ["After-acquisition contribution", "$40.47 - $28.00 CAC", "$12.47", "Before fixed operating labor and overhead"],
                    ["Conservative annual", "$50,000 gross - $40,000 cost envelope", "$10,000 net / 20%", "1 FT + 3 C; constrained owner compensation"],
                    ["Base annual", "$425,000 gross - $265,625 cost envelope", "$159,375 net / 37.5%", "1 FT + 3 C; budget labor within the envelope"],
                    ["Scaled annual", "$800,000 gross - $360,000 cost envelope", "$440,000 net / 55%", "1 FT + 3 C; operating leverage must be demonstrated"],
                ],
            },
        },
    ],
    "pull_quote": "The first thirty days should buy evidence, not confidence: deliver one promised outcome, reconcile every dollar, and fund only the next measurable improvement.",
    "diagram_id": "diag-08-thirty-day-launch-roadmap",
    "action_checklist": [
        "Create the day-one pain brief with twenty ad records, twenty dated discussions, and five scheduled buyer conversations.",
        "Write the $39, $99, and $249 tier promises, delivery dates, license scope, and merchant-of-record application requirements.",
        "Prepare the 72-hour pre-sale ledger with qualified-visitor, independent-buyer, refund, and insufficient-evidence fields.",
        "Assign the v1.0 modules and IP ledger, then schedule checkout, duplicate-event, delivery, and refund tests before day 14.",
        "Set the combined $50/day creative budget, $350 ceiling, source tags, and $80 zero-order pause rule before launch.",
        "Book the day-30 cohort review and enter Kill, Fix, Scale, and Hold thresholds before seeing campaign results.",
    ],
    "statutory_citations": [
        {"title": "16 CFR Part 435 — Mail, Internet, or Telephone Order Merchandise Rule", "url": "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-435", "relevance": "Primary delivery-promise, delay, and refund framework for covered merchandise orders; assess scope rather than assuming pure digital downloads are covered."},
        {"title": "15 U.S.C. section 8403 — Negative option marketing on the Internet", "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim", "relevance": "Requires clear disclosure of material terms, express informed consent, and simple mechanisms to stop recurring charges in covered online negative-option transactions."},
        {"title": "South Dakota v. Wayfair, Inc., 585 U.S. 162 (2018)", "url": "https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf", "relevance": "Supreme Court opinion overturning the physical-presence rule for state sales-tax collection; distinguish state nexus and product-taxability rules from the merchant-of-record contract's allocated responsibilities."},
    ],
}
