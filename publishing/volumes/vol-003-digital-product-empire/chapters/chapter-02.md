# Chapter 02: Who Pays, Why They Pay & Where Checkout Capital Sits

*B2B Expense-Account Buyers vs. Prosumers, Merchant-of-Record (Paddle / Lemon Squeezy) vs. Direct Stripe Settlement & Reserve Mechanics*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Sell saved work before selling inspiration. An expense-account buyer needs a usable output, an invoice, and a defensible reason to buy; an impulse buyer often needs only a persuasive promise. Those differences shape refunds, support, and acquisition cost. Checkout then decides who owes tax, who controls refunds, and when cash reaches payroll. Compare rails on contribution and available cash, not headline fees. This chapter connects buyer qualification, merchant-of-record economics, external web subscriptions, and genuine cohort scarcity to a small-team operating model with explicit costs and reserve assumptions.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Conservative | $10,000 net |  |  |
| Base | $159,375 net |  |  |
| Scaled | $440,000 net |  |  |

## 1. Sell an expense the buyer can defend  `🏷️ OPERATING_FRAMEWORK`

Start with the person who owns a recurring task, not the broadest audience that clicks an advertisement. An operations lead buying a hiring SOP or reporting template can justify a purchase against hours saved this week. Ask which task repeats, who signs off on expenses, and what file must exist at the end. A $100 product that removes two hours of work valued at $75 per hour has a concrete buying story, although the customer must validate that saving. Provide a preview, supported file formats, license scope, and an invoice with the correct business details. Reimbursement is not automatic: distinguish someone buying on a company card from someone hoping their manager will repay a personal purchase after the work is complete.

Treat lower refunds among qualified business buyers as a hypothesis to test, not a property bestowed by a business email address. These buyers may tolerate a higher price when the asset fits their workflow, yet demand more support when deployment is unclear. Track refunds by acquisition source, buyer role, product version, and reason over a fixed thirty day window. Separate an invoice correction from dissatisfaction and a duplicate charge from product failure. Prosumers occupy the middle: they buy tools for serious personal work but often spend their own money. Offer a focused sample rather than a sprawling bundle. Impulse consumer traffic may convert quickly and reverse quickly; compare retained contribution per visitor after refunds mature, not checkout conversion on launch day.

Use discovery calls to turn vague interest into a measurable use case. Ask what the buyer did last time, how long it took, and which existing document they can safely describe without sharing confidential material. Then show the closest finished output and ask what would prevent adoption. Record objections about accuracy, editing effort, licensing, and internal review separately. A buyer who needs custom integration belongs in a service offer, not a download funnel whose margins assume self service. Price the template around a repeatable outcome and state what implementation remains with the customer. Build a refund reason ledger before scaling ads. Ten enthusiastic interviews are useful design evidence, but they are not a substitute for paid use and observed renewal behavior.

**Buyer and scarcity failure detection**

| Naive Trap | Detection Metric | Durable Operator Fallback |
| --- | --- | --- |
| Business email means low refunds | 30-day refunds by buyer cohort | Qualify task and preview output |
| Resetting countdown creates demand | Timer resets while capacity is unchanged | Publish actual seats and release dates |

## 2. Separate the seller, processor, and cash owner  `🏷️ OPERATING_FRAMEWORK`

A merchant of record is the contractual seller on covered transactions, not merely a nicer payment form. Paddle, Lemon Squeezy, and FastSpring can take responsibility for collecting and remitting applicable transaction taxes within their service scope. That does not move your corporate income tax, product promises, or every local obligation to the platform. Read the seller agreement for supported countries, restricted products, refund authority, dispute charges, and termination provisions. The customer pays the merchant of record, which later pays your business under its payout rules. With direct Stripe processing, your business generally remains the seller. Stripe Tax calculation does not by itself register your business everywhere or file every return. Assign each obligation to a named party before comparing the quoted percentages.

Use 5% plus $0.50 as a standard merchant-of-record comparison assumption, not a universal contractual quote. Paddle and Lemon Squeezy advertise that starting structure, subject to product terms and possible additions; FastSpring pricing requires a commercial quote rather than an asserted identical public tariff. A direct domestic card model uses Stripe at 2.9% plus $0.30 and an assumed eligible Stripe Tax calculation charge of 0.5%. International cards, currency conversion, subscriptions, tax filing services, and negotiated rates can alter the bill. Gumroad direct sales use a 10% plus $0.50 platform fee with payment processing potentially additional; Discover uses 30% under its applicable terms. Apple and Google commonly fall within a 15% to 30% commission range, with program, territory, and transaction exceptions requiring review.

Payment success is not spendable cash. Settlement first creates a platform balance; payout eligibility, a payout schedule, bank transit, and any reserve determine availability. A first payout can take longer than later payouts. A rolling reserve holds a percentage of eligible receipts for a stated period, while a fixed reserve or account review can restrict a different amount. Refund spikes, disputes, sudden volume growth, unusual ticket sizes, and delayed delivery can prompt review; no single trigger guarantees a particular hold. Maintain separate ledger balances for tax, unsettled proceeds, reserved funds, and available cash. Obtain the actual schedule from the account agreement and dashboard rather than relying on a generic comparison article. Fund payroll only from available cash after expected refunds and near-term operating commitments.

## 3. Acquire on the web without hiding the subscription  `🏷️ OPERATING_FRAMEWORK`

The mapped play web2app_quiz_subscription_billing_bypass describes mobile acquisition through a web diagnostic quiz followed by external Stripe or merchant-of-record checkout. Its durable version is a web purchase journey, not a trick that conceals charges or defeats app review. Advertise a specific diagnostic outcome, ask only questions needed to produce it, and show a useful result before offering the paid implementation asset. Tie the paid offer to the diagnosed task rather than manufacturing a frightening score to force conversion. Measure quiz completion, qualified checkout starts, paid activation, and retained subscriptions as separate events. A cheap quiz lead has no economic value until the buyer uses the product and stays. Preserve a clear distinction between an educational assessment and a professional diagnosis that the product cannot substantiate.

A $100 order on the modeled 5% plus $0.50 merchant-of-record rail leaves $94.50 after that fee alone. That is the narrow meaning of retaining 94%+ net revenue in this play: payment-fee retention before refunds, advertising, support, tax effects, and additional charges. It is not a 94% contribution margin. Direct Stripe plus the modeled tax calculation leaves $96.30 before those other costs. Mobile app distribution remains a separate contract question. External links, alternative billing, entitlements, and applicable fees vary by storefront, territory, app category, and program. Check the rules for the actual distribution path rather than assuming a web purchase exempts every app transaction from store economics. If the permitted path is unclear, sell a complete browser product while evaluating a supported app implementation.

For recurring offers, put the price, billing interval, trial conversion terms, and cancellation method where the buyer makes the purchase decision. A quiz completion is not permission to charge a card. Section 8403 of title 15 requires clear material disclosures before obtaining billing information, express informed consent before charging, and a simple mechanism to stop recurring charges for covered internet negative-option sales. Implement cancellation in the account flow and test it on mobile as carefully as checkout. Record the offer version and purchase event without collecting unnecessary sensitive data. Distinguish cancellation of future renewals from a refund of an earlier charge. Track first renewal failures and immediate cancellations by creative; a misleading advertisement can look efficient until the first billing cycle exposes the mismatch.

**SOP — Standard Operating Procedure**

1. Define the result
   - Write one useful quiz outcome.
   - Connect each question to an actual product decision.
2. Map the purchase path
   - Document web and app entry points.
   - Check storefront and territory terms for each path.
3. Test the lifecycle
   - Exercise purchase, renewal, refund, and cancellation.
   - Confirm receipts and entitlement changes match payment events.
4. Reconcile a cohort
   - Compare mature receipts with acquisition and support costs.
   - Expand only when contribution and available cash both support spending.

## 4. Allocate real capacity instead of manufacturing urgency  `🏷️ OPERATING_FRAMEWORK`

The mapped play verified_fan_ticketing_and_drop_allocation_farming belongs here as a lesson in legitimate allocation mechanics, not automated hoarding or evasion of another platform's purchase limits. Apply it to your own product cohort: define how many customers the team can actually onboard, establish eligibility, and allocate seats through a documented waitlist. Do not create duplicate identities, misrepresent fan status, or promise third-party tickets you do not control. For a template workshop, capacity may be the number of files an expert can review, not the number of downloads a server can deliver. A download is usually abundant; individualized attention is scarce. State which component is capped so buyers understand what expires and what remains available after a cohort fills. That distinction protects both trust and staffing economics.

Calculate capacity from service minutes before writing a launch email. Suppose three contractors can each devote four hours per week to reviews, giving twelve hours in total. At thirty minutes per review, theoretical capacity is twenty-four reviews; reserve four for rework and sell twenty weekly review seats. Those are illustrative allocations, not a staffing benchmark. Keep the download available separately if its marginal delivery cost is low. Order the waitlist by a published timestamp rule or use a disclosed lottery when fairness matters more than speed. Give selected buyers a real acceptance deadline and release unused seats to the next eligible person. Maintain an allocation log showing offered, accepted, expired, and refunded seats so support can resolve disputes without inventing exceptions or quietly overselling capacity.

A countdown is truthful only when the stated consequence happens. If a cohort closes Friday because onboarding starts Monday, close it Friday and publish the next intake rather than resetting the clock for every visitor. If a seat is reserved for fifteen minutes during checkout, release it when the reservation expires and avoid counting abandoned carts as completed sales. Show availability from the same inventory record used to accept orders. A waitlist should not silently become a paid subscription, and an allocation email should distinguish an invitation from a confirmed purchase. Watch complaints about urgency alongside conversion metrics. The operational test is simple: could a support person explain the deadline and capacity number using staffing records and order history? If not, remove the claim and sell the actual benefit.

> **OPERATOR GATE — Capacity must survive reconciliation**
> 
> Open the next cohort only when delivery time and collected cash support the seats offered.
> - Name the scarce service component.
> - Publish the allocation and expiry rules.
> - Reconcile seat inventory with paid orders.
> - Keep an accurate next-intake date.

## 5. Price the rail, then fund the cash cycle  `🏷️ ILLUSTRATIVE_MODEL`

Read the rail table as a controlled $100 tax-exclusive order comparison, not a live quote. Assume a domestic card, no currency conversion, no refund, no dispute, and no separately priced subscription tooling. For direct Stripe, assume the entire $100 is eligible for the 0.5% tax calculation charge. For Gumroad direct, show both the platform fee and an illustrative 2.9% plus $0.30 processing layer rather than hiding processing inside the headline rate. Store commissions are simplified percentages; taxes and contractual commission bases can change the actual settlement. Taxes collected from the buyer are liabilities, not revenue. Wayfair removed the physical-presence requirement for state sales-tax nexus, but it did not establish one nationwide threshold. EU VAT analysis likewise depends on customer status, location, and the applicable supply rules.

Model reserves as restricted cash rather than an additional processing expense. On the direct Stripe illustration, $100 less $3.70 in modeled fees leaves $96.30 before other deductions. An illustrative 10% reserve applied to gross receipts restricts another $10, leaving $86.30 initially available before payout timing and other liabilities. The $10 remains an asset subject to release or application against obligations; it is not lost margin merely because access is delayed. If eligible monthly billings are $40,000 and that reserve retains three monthly cohorts, approximately $12,000 can remain tied up at steady volume. This is a stress case, not a stated Stripe policy. Build a weekly cash forecast that includes opening available cash, scheduled releases, refunds, contractor invoices, advertising, and taxes payable, with no borrowing from customer tax balances.

The annual scenarios use gross product billings excluding transaction taxes and modeled costs that include refund leakage. Conservative means $50,000 gross less $40,000 costs, yielding $10,000 net at 20%. Base means $425,000 less $265,625, yielding $159,375 at 37.5%. Scaled means $800,000 less $360,000, yielding $440,000 at 55%. These are planning cases, not observed results or inevitable scale economies. The operating shape is 1 FT + 3 C: one full-time founder and three contractors with variable hours. The cost bridge includes contractor spend but excludes founder compensation and income taxes, so net here means modeled operating contribution before those items, not personal take-home profit. At conservative revenue, a fully paid full-time role is not funded. Insert the founder's required salary before deciding whether this business supports their livelihood.

**$100 order: modeled take rate, fee retention, and payout exposure; verify account terms**

| Rail | Fee assumptions | Fee / retained | Reserve and payout mechanics |
| --- | --- | --- | --- |
| Paddle MoR | 5% + $0.50 baseline | $5.50 / $94.50 | Contractual payout schedule; risk holds possible; additions excluded |
| Lemon Squeezy MoR | 5% + $0.50 baseline | $5.50 / $94.50 | Holding period and payout cycle; additions and payout fees excluded |
| FastSpring MoR | 5% + $0.50 comparison assumption only | $5.50 / $94.50 modeled | Obtain actual quote, payout cycle, and reserve terms |
| Stripe direct + Stripe Tax | 2.9% + $0.30 + 0.5% | $3.70 / $96.30 | Account-specific settlement; rolling or fixed reserves possible, not universal |
| Gumroad direct | 10% + $0.50; assumed processing $3.20 extra | $13.70 / $86.30 | Eligibility, holding period, review, and payout method govern availability |
| Gumroad Discover | 30% inclusive platform comparison | $30.00 / $70.00 | Marketplace payout eligibility and account review still apply |
| Apple in-app | 15% to 30% scenario range | $15-$30 / $85-$70 | Program-specific fiscal payout cycle and adjustments; exceptions apply |
| Google in-app | 15% to 30% scenario range | $15-$30 / $85-$70 | Program-specific payment cycle and adjustments; exceptions apply |

---

> ### “A cheaper checkout is not a better business when the savings disappear into refunds, tax administration, or cash you cannot yet withdraw.”

## Action Checklist

- [ ] Interview five buyers about their last recurring task.
- [ ] Tag orders by buyer role and acquisition source.
- [ ] Obtain written rail pricing and payout terms.
- [ ] Reconcile available, pending, and reserved balances.
- [ ] Test cancellation and renewal disclosures end to end.
- [ ] Publish cohort capacity and build the annual cost bridge.

## Statutory & Primary Authorities

1. South Dakota v. Wayfair, 585 U.S. 162 (2018): Physical presence is not required for state sales-tax nexus; state rules still govern. — <https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf>
2. EU Council Directive 2006/112/EC: EU VAT framework; customer status and place-of-supply rules matter for digital sales. — <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006L0112>
3. 15 U.S.C. section 8403: Online negative-option sales require material disclosures, express informed consent, and simple stopping mechanisms. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section8403&num=0&edition=prelim>

## Sources

1. Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? (Tutorly) — Tutorly @ [00:00:20]: This choice splits our three contenders into two completely different categories. Stripe Checkout is a standard payment processor, while Paddle and Lemon Squeezy act as a merchant of record. A merchant of record means the platform becomes the legal seller of your product. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=IfaCBBIoVK0&t=20s>
2. Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub) — TechWealth Hub @ [00:01:36]: Fourth, customer support for payment issues. And the crazy part, you enable all of this with one line of code. In your Stripe checkout session, you add managed payments enabled. You now have paddle level tax compliance with Stripe level infrastructure. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=KRdWGDk-GkY&t=96s>
3. Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain Vova (Vova Feldman)) — Captain Vova (Vova Feldman) @ [00:01:44]: Records that already set kind of the standards for the prices for Merchant of Record in the market. Whether you've been following the events or not, last year Stripe acquired payment solution called Lemon Squeezy, a Merchant of Record actually. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=5zGuxRrg_O0&t=104s>
4. Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild) — SoloBuild @ [00:02:00]: Stripe Tax can calculate and collect tax for you, but registering and filing are only included in its Tax Complete plan, which starts at ninety dollars a month. Lemon Squeezy and Paddle each say they are your merchant of record. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=i05UCC3UvNY&t=120s>
5. Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech) — houdztech @ [00:03:05]: They handle a sepa, so dozens of local methods. Lemon Squeezy supports 135 plus countries for payments and 20 plus payment methods including cards, PayPal, Apple Pay, Google Pay, Alipay, and WeChat Pay. Paddle's reach is technically broader. This is mixed on both sides. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=185s>
6. Lemon Squeezy for Merchant of Record Honest Review - Watch Before Using (HelperMan) — HelperMan @ [00:01:20]: But there there are definitely some downsides you should know before using it. First, fees can feel higher compared to using a standard payment processor directly because you're paying for the extra tax and compliance handling. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=IA4eosnOzIE&t=80s>
7. NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products (How2Genius) — How2Genius @ [00:02:20]: You can create fully branded storefronts and checkout experiences, including upsells, bundles, and localized pricing. It also supports a wide range of payment methods, credit cards, PayPal, Apple Pay, and more, so customers can pay however they prefer. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=140s>
8. How to Sell Notion Templates on Gumroad (Step By Step 2026) (BrightGuide) — BrightGuide @ [00:01:02]: From there, select your currency. Make sure you choose the currency you want to sell in, especially if your if your audience is based in a particular region. Once the currency is set, enter your product price. This is the amount customers will pay for your template. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=oMxSmqY3mzM&t=62s>
9. How to start selling your Framer templates through Lemon Squeezy (Framer) — Framer @ [00:03:38]: So it is important that you use this link and send it to us or share it on Twitter or share it anywhere you want so you can copy this share it wherever you want and then that is how you start selling your templates through lemon squeezy thanks for watching. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=RN0VWAvL-qc&t=218s>
10. How to Sell Notion Templates on Gumroad (2026 Revenue Snapshot) (Tutorials At Desk) — Tutorials At Desk @ [00:03:45]: After that, follow the on-screen instructions to connect a supported payout method such as Stripe or PayPal, depending on what Gumroad offers in your region. You'll be asked to complete identity verification and payment setup. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=VEFf-FR0dxw&t=225s>
11. Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an Existing App  #mcp (Stephen S.) — Stephen S. @ [00:03:38]: So I had to go in and specify the correct tax classification. So in this case, software as a service personal use for these products. But once you do that, then the uh checkout API will work and it will open up these pages. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=218s>
12. Paddle for Merchant of Record Honest Review - Watch Before Using (HelperMan) — HelperMan @ [00:02:00]: Overall, after 6 months of using Paddle, I think it's one of the best payment solutions for SaaS businesses and digital product creators who want simplicity and global compliance support. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=o3KRrFnoAgM&t=120s>
13. How to Build 1 Click Upsells in GoHighLevel (Marketing Mark) — Marketing Mark @ [00:00:45]: So, what we want to do to add a one-click upsell, and by one-click upsell I mean that since we've captured their payment information on our checkout page, the system has that stored. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=0u4Tmd6BlWA&t=45s>
14. How to sell Notion templates on Gumroad[2026 Full Guide] (Extreme How To's) — Extreme How To's @ [00:01:46]: " This instruction will guide users through the process of obtaining the template. For pricing options, you can choose to toggle on allow customers to pay what they want. This feature can attract more buyers as it offers flexibility in pricing. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=SK_-uXSKE88&t=106s>
15. How to Start Selling Digital Products in 2026 (Step-by-Step Tutorial) (Rochelle Be) — Rochelle Be @ [00:07:06]: 't even know that you're good at problem solving in that area. Okay, so that's the second circle. We're now on to circle three, which is what people pay for. Because we want things that people are actually going to pay you money for. You might be good at rock collecting. — Attributed practitioner commentary on buyer psychology, Merchant-of-Record platforms (Paddle/Lemon Squeezy), and direct Stripe checkout settlement. — <https://www.youtube.com/watch?v=4e4pRrWsJvU&t=426s>
16. ✅ 💰 CALIFORNIA Unclaimed Property Investigations - Tips from a Licensed Private Investigator! — Security and Investigations Leadership Channel @ [00:06:11]: You to get their money at the unclaimed property division because there's so many other John Smith's I had to happen before this person the unclaimed property division wanted my client to prove that this person is John Smith and Metra Sonny mom's coming up with so that person was able to prove who they are but the problem is they were not able to prove that they worked at a certain place because there are owed money. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=371s>
17. ✅ 💰 CALIFORNIA Unclaimed Property Investigations - Tips from a Licensed Private Investigator! — Security and Investigations Leadership Channel @ [00:00:00]: Unclaimed property versus surplus — candidate asset — Classify state-held intangible property separately from county tax-sale and mortgage-sale proceeds. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=0s>
18. Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR PITCH | #10 — Probate Mastery @ [00:00:00]: Curative lead sourcing — geographic buy box — Collect dead wholesaler leads, code violations, tax-delinquent deceased owners and aged probates. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=0s>
