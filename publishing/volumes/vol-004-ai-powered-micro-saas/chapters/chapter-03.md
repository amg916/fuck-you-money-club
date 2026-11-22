# Chapter 03: How the Business Makes Money: Hybrid Pricing, Token Metering & Churn Math

*Base Platform Fee + Metered Credits, Inference Gross-Margin Floors (>80%), Net Revenue Retention (NRR) & Conservative/Base/Scaled P&Ls*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Sell a bounded business outcome, not an unlimited invitation to spend your API balance. A $99 monthly seat with included workflow credits and prepaid overage packs makes demand measurable before it becomes a liability. Price against expensive customers, reconcile cached and uncached tokens, and distinguish inference margin from fully loaded owner profit. This chapter builds an illustrative credit ledger, customer contribution model, churn bridge, and three annual operating cases. Telecom examples monetize legitimate verification and routing work, never subsidy capture or manufactured traffic. Every number is an operating assumption to replace with invoices and cohort evidence.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Base seat | $99/month |  |  |
| Inference margin | >80% |  |  |
| Base annual profit | $112,500 |  |  |

## 1. Replace unlimited promises with bounded outcome credits  `🏷️ ILLUSTRATIVE_MODEL`

The $29 unlimited plan fails when its price is fixed but its upstream obligation is not. Suppose 100 accounts produce $2,900 monthly revenue. Ninety nine customers each consume $3 of inference, while one automated customer runs 400,000 workflows costing one cent each. Model charges reach $4,297 before hosting, payments, support, or salaries. The top one percent has converted apparent recurring revenue into a negative contribution business. This is an illustrative stress test, not a claim about typical customer behavior. A retry bug can create the same damage without hostile intent. Measure costs at tenant and workflow level, then replay the largest observed customer through the proposed price book. Average usage is useful for forecasting; tail usage determines whether the promise is financially survivable under sustained automated demand.

Charge $99 per seat each month with 1,000 standard workflow credits, then $20 for each additional 200 credits. A standard workflow has explicit input, output, tool, and retry limits. Expensive document batches consume several credits according to a published schedule rather than pretending every request is equivalent. Automatic packs require a customer selected monthly spending ceiling and clearly disclosed renewal and purchase terms. Reserve credits before dispatch, settle successful work once, and release unused reservations when processing fails. Customer retries reuse an idempotency key, preventing duplicate charges for the same delivered outcome. Stop new work when the funded balance or spending ceiling is exhausted. This is not artificial scarcity: it prevents either party from discovering an unbounded liability after the monthly invoice has already been issued.

Define the sold outcome precisely enough that support can settle a disputed charge without reading a model transcript. A completed extraction might mean a validated record delivered to the customer, not every internal model attempt. Failed internal retries remain your cost, so the credit price needs room for them. Show balance, consumed credits, purchased packs, and remaining spending capacity in the account ledger. Separate purchased credits from included allowances, with explicit expiration and refund treatment. Do not count a prepaid balance as delivered service merely because cash arrived. For consumer internet subscriptions, 15 U.S.C. section 8403 addresses negative option disclosures, express informed consent, and simple mechanisms to stop recurring charges. Match the actual customer and transaction scope rather than asserting that every business subscription falls under that provision.

**Find the tail before it finds the bank balance**

| Naive Trap | Detection Metric | Durable Operator Fallback |
| --- | --- | --- |
| $29 unlimited AI | Top 1% share of model cost | Bounded credits and funded packs |
| Silent retry loops | Attempts per delivered result | Retry ceiling and idempotency |
| Hidden overages | Disputes per paid invoice | Visible ledger and spending ceiling |

## 2. Meter tokens into customer contribution  `🏷️ ILLUSTRATIVE_MODEL`

Use hypothetical provider rates of $2 per million uncached input tokens, $0.20 per million cached input tokens, and $8 per million output tokens. One standard workflow consumes 2,000 uncached input tokens, 3,000 cache read tokens, and 500 output tokens. Its inference cost is $0.004 plus $0.0006 plus $0.004, or $0.0086. At 1,000 workflows, inference totals $8.60 against the $99 seat, leaving a 91.31 percent inference margin. These rates are modeling inputs, not a vendor quotation. Record cache writes separately when charged, and never apply a cache discount to tokens reported as uncached. Reconcile provider usage fields and invoice rounding against the internal ledger. Cache expiry, context growth, tool calls, and model changes can all break a price that looked attractive in a spreadsheet last month.

Now assume an account uses 1,200 workflows monthly and buys exactly one $20 pack, producing $119 of earned monthly revenue. Inference costs $10.32. Allocate $4 for vector storage and database hosting, $2 for other serving infrastructure, and payment fees at an illustrative 2.9 percent plus $0.30 on each of two transactions. Fees total $4.05 after rounding, leaving $98.63 contribution and an 82.88 percent delivery margin before support and overhead. Inference margin alone is 91.33 percent, a different measure with a different denominator of cost. A monthly combined charge would reduce fixed payment fees but introduce receivables exposure. The operator chooses the collection policy deliberately instead of silently borrowing from the provider to finance customers who may not pay their usage bill at the end of the month.

Measure average revenue per account using earned subscription and usage revenue divided by average active paying accounts over the same period. In this homogeneous example, account ARPU is $119; multiple seats would require separate account and seat measures. Track account contribution beside ARPU so an expensive upgrade cannot masquerade as expansion. Set an inference margin floor above eighty percent at the account and workflow tier, not merely across the portfolio. A $0.10 marginal credit permits less than $0.02 of inference cost at that floor. Reserve some of that allowance for failures and cost volatility. If a workflow exceeds its budget, reduce context, use a cheaper validated route, or charge additional credits prospectively. Never preserve the headline margin by excluding provider charges that are inconvenient to the sales story.

## 3. Price acquisition against churn, not optimism  `🏷️ ILLUSTRATIVE_MODEL`

Separate voluntary churn from involuntary churn before spending another acquisition dollar. Begin a month with 100 accounts, each generating $119, and lose two accounts through deliberate cancellation plus one through unresolved payment failure. Logo churn is three percent: two percent voluntary and one percent involuntary, measured against the opening population with mutually exclusive final loss reasons. Payment retries can recover failed collections, but a recovered account is not a new sale. Record cancellation requests, collection failures, recovery dates, and actual service termination separately. A temporary payment failure does not automatically establish revenue churn. Offer payment updates and sensible retries while measuring the share actually recovered. Product investment addresses poor outcomes and weak adoption; collection operations address failed cards. Combining the two obscures which intervention earns its cost and exaggerates product dissatisfaction.

Opening recurring revenue is $11,900. Three lost accounts remove $357, surviving accounts expand by $600, and other survivors contract by $200. Closing revenue from that same cohort is $11,943, making net revenue retention 100.36 percent: opening revenue minus churn and contraction plus expansion, divided by opening revenue. New customers are excluded. Gross revenue retention is 95.32 percent because it excludes expansion. For usage pricing, report a consistent trailing usage convention alongside contracted recurring fees; a single seasonal spike should not become imaginary permanent MRR. The example assumes the $119 baseline and all changes represent comparable recurring monthly activity. A positive NRR headline can coexist with losing customers and rising service costs. Examine cohort contribution retention as well, particularly when expansion comes from workflows with materially worse token consumption.

Using $98.63 monthly delivery contribution and constant three percent monthly logo churn gives a simplified contribution lifetime value of $3,287.67. At $600 fully loaded customer acquisition cost, LTV:CAC is 5.48 and acquisition payback is 6.08 months. The formula assumes stable churn, stable contribution, no discounting, and no expansion; it is a planning shortcut rather than observed lifetime profit. If $12 of variable monthly customer support belongs to each account, contribution falls to $86.63, lifetime value to $2,887.67, the ratio to 4.81, and payback to 6.93 months. Include sales labor, advertising, commissions, and acquisition tools in CAC. Compare mature cohorts against these assumptions before raising spend. Early customer survival alone cannot establish long term retention, and annual prepayment improves cash timing without proving the underlying acquisition economics are sound.

**SOP — Standard Operating Procedure**

1. Freeze the cohort
   - Snapshot opening paying accounts.
   - Exclude new accounts from retention calculations.
2. Reconcile losses
   - Classify actual terminations.
   - Distinguish voluntary exits, payment failures, and recovered accounts.
3. Bridge revenue
   - Apply expansion and contraction.
   - Use consistent usage windows and earned revenue.
4. Price acquisition
   - Calculate contribution payback.
   - Include variable support and fully loaded acquisition costs.

## 4. Sell telecom workflow tolls, not traffic fantasies  `🏷️ OPERATING_FRAMEWORK`

The mapped play mvno_lifeline_acp_telecom_subsidy_aggregation becomes an eligibility verification and enrollment operations product sold to authorized providers. Charge a platform seat plus a toll per verified subscriber record, with a defined verification event and evidence receipt. Do not bill every failed lookup as another verified subscriber. Track incomplete applications, duplicate checks, authorized rechecks, and final determinations separately. The service helps an operator maintain records and route work; it does not create eligibility or replace required program determinations. Section 54.400 defines Lifeline terms, while adjacent rules govern eligibility and enrollment duties. ACP ended in 2024, so the historical play name does not justify forecasting current ACP subsidy receipts. Subscription revenue comes from software customers, not assumed ownership of their subsidies, and verification costs remain visible in the credit model and customer invoice.

The mapped play telecom_voice_traffic_pumping_8yy_sms_arbitrage becomes a legitimate usage metered routing and carrier lookup micro SaaS. Sell A2P 10DLC registration workflow support, voice route monitoring, OTP routing, and carrier intelligence to customers handling authorized communications. Revenue is the disclosed software toll, not a promise to manufacture calls or harvest intercarrier payments. A carrier lookup, message submission, delivery receipt, and successful authentication are different billable events; select one and document how duplicates and failures behave. Registration does not itself establish permission to message a recipient. Track carrier surcharges and destination pricing separately from model costs. Decline artificial traffic and fraudulent OTP bursts rather than treating them as valuable expansion. A routing product survives because it reduces legitimate delivery waste, not because an unexplained traffic spike temporarily inflates its monthly invoice.

Keep carrier pass through charges outside the $99 software allowance unless the allowance explicitly funds them. A $0.01 software toll with $0.001 serving cost has ninety percent contribution before overhead, but that says nothing about a separate carrier charge. Determine principal versus agent revenue presentation from the actual contracts; do not inflate software ARPU by automatically calling every collected carrier dollar earned software revenue. Maintain identifiers linking tenant, authorized request, route, carrier invoice, delivery state, and billed event. Reserve funds before initiating costly external work, enforce tenant concurrency limits, and reconcile late carrier receipts without charging the same event twice. For verification products, minimize retained identity data and bound access by operational need. Neither example inherits the generic workflow cost assumptions automatically; both require measured lookup, communications, storage, and support costs.

> **OPERATOR GATE — No funded unit, no dispatch**
> 
> Execute only within the customer's disclosed spending limit and funded balance. Internal retries never create duplicate customer outcomes.
> - Reserve before external cost accrues.
> - Settle one durable event identifier once.
> - Expose carrier charges separately from software tolls.
> - Pause work at the spending ceiling.

## 5. Reconcile annual billings to spendable owner economics  `🏷️ ILLUSTRATIVE_MODEL`

The annual scenarios below are explicit planning cases, not forecasts derived from the homogeneous $119 account example. Conservative gross subscription billings are $50,000, Base billings are $375,000, and Scaled billings are $700,000. They assume all billed service is delivered within the year, no refunds or bad debt, and no sales tax included in revenue. Customer mix and annual usage differ across cases. Inference, hosting, and payment fees are delivery COGS; staffing, acquisition, and overhead come afterward. Conservative delivers $7,500 at fifteen percent net margin, Base delivers $112,500 at thirty percent, and Scaled delivers $315,000 at forty five percent. Here net means pretax owner operating profit after the listed economic labor charge, before financing and owner taxes. Do not label this amount after tax cash or combine it with gross billings when describing income.

Staffing is 1 FT + 2 C in Conservative and Base, then 2 FT + 3 C in Scaled, where FT means full time capacity and C means a limited hours contractor, not another full time employee. Conservative assigns only $30,000 to labor: $24,000 of founder economic compensation and $6,000 across contractors. That is a deliberately constrained owner operated case, not a credible market salary budget in many locations. Replacing the founder allocation with $60,000 would turn its $7,500 profit into a $28,500 loss. Base allocates $155,000 to labor and Scaled $235,000, including support, contractor payments, and assumed employment burden where applicable. Validate local hiring costs before accepting either margin. Founder distributions are not a second deductible expense simply because the operating model includes a charge for founder time.

The cash bridge starts with collections, subtracts provider bills, payroll, contractors, acquisition, overhead, and tax payments, then adjusts for deferred service obligations and working capital. Annual prepayment can make cash look stronger than earned profit while future inference remains unfunded. Maintain a reserve tied to outstanding credits and expected delivery cost. Tax timing is another separate ledger. Under current federal rules, section 174 generally amortizes foreign research expenditures over fifteen years using a midpoint convention, including qualifying software development costs. Domestic research treatment changed for tax years beginning after 2024 under section 174A, with transition rules and elections that require year specific analysis. Do not repeat the obsolete blanket claim that all current domestic software costs require five year amortization. Classify development location and tax year before converting operating profit into a tax cash estimate.

**Illustrative annual P&Ls in USD; labor includes founder economic compensation**

| Annual line | Conservative | Base | Scaled |
| --- | --- | --- | --- |
| Gross subscription billings / earned revenue | $50,000 | $375,000 | $700,000 |
| Inference COGS | $5,000 | $30,000 | $49,000 |
| Vector / DB / serving hosting COGS | $2,500 | $15,000 | $21,000 |
| Payment fees COGS | $2,000 | $12,000 | $22,000 |
| Delivery contribution | $40,500 | $318,000 | $608,000 |
| Labor including support | $30,000 | $155,000 | $235,000 |
| Customer acquisition | $2,000 | $35,000 | $45,000 |
| Other operating overhead | $1,000 | $15,500 | $13,000 |
| Total operating costs | $42,500 | $262,500 | $385,000 |
| Net owner operating profit, pretax | $7,500 | $112,500 | $315,000 |
| Net operating margin | 15% | 30% | 45% |
| Staffing capacity | 1 FT + 2 C | 1 FT + 2 C | 2 FT + 3 C |

---

> ### “An unlimited plan sells the customer an option on your API balance; metered outcomes turn that open liability into a priced operating commitment.”

## Action Checklist

- [ ] Replace unlimited usage with a $99 seat and bounded credits.
- [ ] Replay the largest tenant through the credit price book.
- [ ] Reconcile cached, uncached, and output tokens to invoices.
- [ ] Split voluntary cancellations from failed payment losses.
- [ ] Calculate contribution payback for each acquisition cohort.
- [ ] Budget annual profit with explicit labor allocations.

## Statutory & Primary Authorities

1. 47 CFR section 54.400: Lifeline definitions; not standalone enrollment authorization. — <https://www.ecfr.gov/current/title-47/section-54.400>
2. 15 U.S.C. section 8403: Internet negative option disclosures, consent, and cancellation. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim>
3. 26 U.S.C. section 174: Foreign research amortization and software treatment; distinguish domestic section 174A. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section174&num=0&edition=prelim>

## Sources

1. The Economics of Owning a SaaS Company (Business Mechanics) — Business Mechanics @ [00:14:02]: In the optimistic scenario, you've built a product with strong retention, a healthy net revenue retention above 110%, a CAC payback period under 12 months, and monthly churn under 2%. Revenue compounds because you're not just adding new customers. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=Ju9H1oq7CM8&t=842s>
2. How to update Stripe Billing to add usage-based pricing - Full Guide (GuideFrame) — GuideFrame @ [00:00:43]: Set the price per unit in the specified currency. Determine if there is a minimum price or a maximum price to charge. If necessary, configure pricing tiers by clicking add tier to establish varying rates based on usage. Save the pricing plan after reviewing all the details. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=xssyCPxzFWA&t=43s>
3. The Economics of Owning a SaaS Company (Costoday) — Costoday @ [00:10:19]: A SAS company with two ZUA's customers paying $100 a month, $2. 4 $4 million in annual recurring revenue, a taxi payback period of 9 months, monthly churn held at 2% and net revenue retention at 115% through consistent upselling. Annual revenue approximately $2. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=aOKH0EoSCCc&t=619s>
4. Core Unit Economics: The Financial Formulas Behind SaaS, E-Commerce, and Marketplaces (One Minute Finance) — One Minute Finance @ [00:04:31]: 18,000 pounds left in real contribution to help cover your operating expenses and eventually generate a profit. You absolutely have to calculate LTV on gross profit, not revenue, or your entire financial model just collapses. Okay, section three, the LTV to CAC ratio. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=Xpw9vNbYna0&t=271s>
5. 11 essential SaaS metrics explained in 11 minutes (ChartMogul) — ChartMogul @ [00:06:00]: There are two types of revenue retention or revenue churn rate that we look at in SAS normally. The first is gross revenue retention rate and the second is net revenue retention rate. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=zo3QHrXiprs&t=360s>
6. Why agents recompute the same prompt, and how prompt caching fixes it (Efficient NLP) — Efficient NLP @ [00:02:07]: You can kind of see this in the token economics. Uh here is the Anthropic pricing page right now and they price um $5 per million tokens for the Opus model. The price for a cache read is 10 times cheaper at 50 cents per million tokens. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=Q_U4pRggC5I&t=127s>
7. Make Your AI Chatbot Pay For Itself — Stripe Usage Metering, Paywalls & Caps (Chat Data) (Medical Chat) — Medical Chat @ [00:01:18]: Instead of a flat fee, you charge only for what people actually use. Bill per message or by credits, so your heavier, smarter models simply cost a little more. Add volume tiers and the price drops as usage grows. Your biggest customers get your best rate. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=yo4GOxbqovo&t=78s>
8. Monetizing your APIs with usage-based billing (Stripe Developers) — Stripe Developers @ [00:00:50]: The second price represents a tiered pricing model. And if we scroll down to the bottom, you can notice that it's associated with two tiers. The first tier represents a quantity from 1 to 40 and the second tier captures all the rest. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=o_6aujJ5WbM&t=50s>
9. SaaS Metrics Explained: MRR, ARR, Churn, LTV & CAC | Product Management for Beginners (CodeLucky) — CodeLucky @ [00:03:41]: Your customer acquisition cost feeds into your monthly recurring revenue which grows into your annual recurring revenue. Your churn rate directly impacts your lifetime value. Lower churn increases LTV and lower CAC improves your overall LTV to CAC ratio. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=hyC9WOKzUMc&t=221s>
10. Google Cloud Credits for Startups 2026: $350K or $2K? (XRaise) — XRaise @ [00:01:53]: So plan for your bill to come back in year two. And they don't cover everything. Credits work on Google's own cloud products billed by usage. They can't be used on third-party services, including what you buy through Google Cloud Marketplace. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=vLchERSjKS8&t=113s>
11. Free Cloud Credits for Startups: Tech Stack on a Budget (Trapture Explains) — Trapture Explains @ [00:02:47]: 150,000 over time as you build with sustained Azure usage. Once those credits are used, Microsoft says your workload simply move to standard pay as you go pricing. If you don't qualify for a program yet, there are free tiers. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=VmuCPx8GGTU&t=167s>
12. How KV Cache Speeds Up LLMs for Faster AI Models on GPUs (IBM Technology) — IBM Technology @ [00:01:21]: You'll submit a long prompt and then wait for a bit. Then suddenly tokens will stream back fast. That lag before your first token is the model processing your prompt. This is the pre-fill phase. It's one of the two phases in LLM inferencing, and it's highly compute bound. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=o0gkdZBtwEg&t=81s>
13. Real-Time Token Usage Metering, Credit Ledgers & Stripe Billing Webhooks (E Learning by AL SADDAT) — E Learning by AL SADDAT @ [00:00:52]: Once the stream completes, settle the exact prompt plus completion tokens cost and immediately release any unused reserve back to the tenants available balance. Second, immutable double entry credit ledger. Never overwrite a single credits integer without an audit trail. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=0K7i4CFP_qc&t=52s>
14. Someone open-sourced Stripe Billing (Mistral uses it) (Indie Hacker News) — Indie Hacker News @ [00:02:15]: So if your app retries a request, nobody gets built twice. Pricing sits on top of that. Graduated tiers and packages can live in the same plan as minimum commitments or plane seats. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=_lbbl0hdJIg&t=135s>
15. How Prompt Caching makes LLM calls 10x Cheaper (cruxbits8) — cruxbits8 @ [00:02:53]: After the first turn, almost every input token on every later turn is a cache read. The whole conversation runs at a tenth of the price. Every response tells you how many tokens it wrote to the cache, and how many it read back. — Attributed practitioner commentary on token/inference metering, seat-plus-usage hybrid pricing, net revenue retention, and SaaS gross vs. net margins. — <https://www.youtube.com/watch?v=xncObRtKRsw&t=173s>
16. How to start selling your Framer templates through Lemon Squeezy — Framer @ [00:03:14]: Framer it is very important that you use the the share URL this URL won't change even if you make changes to your product listing so for example sometimes the URL can change on the store Page when you change the name of your template or make some tweaks like the price the share link will always remain the same so it is important that you use this link and send it to us or share. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=RN0VWAvL-qc&t=194s>
17. Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? — SoloBuild @ [00:03:13]: Stripe Tax's no-code option is half a percent per transaction, where you're registered to collect. Stripe Billing, for subscriptions, is point seven percent of billing volume. Stack those, and a US subscription business lands near four point one percent plus thirty cents. That's rough math, but it shows the headline rate isn't the full bill. How's that price looking now, Nova? NOVA: That's more than the sticker said. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=i05UCC3UvNY&t=193s>
18. Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an Existing App #mcp — Stephen S. @ [00:03:17]: These plans. So I'm going to click on the pro plan and you can see that it opens up the checkout here. What's pretty cool is it actually created descriptions for the price variant and then obviously the price that was grabbed from our marketing site and then Stripe Power created the price artifact in Stripe using MCP. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=197s>
