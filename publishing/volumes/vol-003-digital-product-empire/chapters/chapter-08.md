# Chapter 08: Tools, Attribution Stack, Micro-Extensions & AI Search (GEO)

*Server-Side Conversion APIs, First-Party Identity Pixels, Contextual Chrome Micro-Tools & Generative Engine Optimization*

> THE BIG MONEY PLAYBOOKS · THE FUCK YOU MONEY CLUB

## Executive Summary

Build the stack around paid orders, not dashboard claims. Choose who handles sales tax, make refunds visible, and send each sale through one clean event ledger. A free Chrome tool should earn its pitch by saving time. Identity matching belongs on a narrow, documented B2B path, not every page. Search citations require public evidence that a reader can check. This directory assigns tools, costs, and owners to those jobs. Spend only when a measured lift in retained contribution pays for the software, labor, and support load.

### Key Metrics

| Metric | Value | Confidence | Source |
| --- | --- | --- | --- |
| Conservative | $10,000 net |  |  |
| Base | $159,375 net |  |  |
| Scaled | $440,000 net |  |  |

## 1. Buy a ledger before buying a growth stack  `🏷️ ILLUSTRATIVE_MODEL`

Start with the order ledger and choose the seller of record before choosing a page builder. Lemon Squeezy and Paddle offer merchant of record services: check product eligibility, supported markets, payout timing, tax scope, and refund terms in the actual contract. Standard Stripe payment processing leaves your business as seller; adding tax software does not by itself transfer that role. Compare total fees at your real order value, including cross border charges, disputes, and foreign exchange. Keep order IDs, product versions, tax, discounts, refunds, and cash payouts in separate fields. Gross billings are not bank deposits. A monthly payout can contain old orders and reserves, so reconcile by order and settlement batch rather than assuming the bank statement describes this month's sales.

Use one full time owner and three contractors, written as 1 FT + 3 C, across each annual scenario. Contractor hours vary with volume; this is not four full time salaries hidden in a lean label. Conservative means $50,000 gross and $10,000 net contribution at 20%. Base means $425,000 gross and $159,375 net at 37.5%. Scaled means $800,000 gross and $440,000 net at 55%. Define gross here as product billings before refunds, excluding sales tax collected. Deduct refunds, payment fees, acquisition, software, delivery, and allocated team labor to reach these modeled contributions. They precede income tax and any unallocated overhead. Higher margins require evidence of lower support cost and cheaper repeat demand; volume alone does not create them or pay the owner's time.

The directory gives planning allowances, not live vendor quotes. Select one option per job and price its required tier against current usage before purchase. The owner holds cash and product decisions; contractors cover engineering, editorial work, and lifecycle operations. A contractor can own several rows, but every row needs one named maintainer. Start with a checkout, event store, email list, and public site. Add an extension or identity vendor only after the basic order path survives a refund test. Record seat limits, event caps, export rights, and cancellation dates beside each subscription. A cheap starter tier that cannot export raw orders is expensive when you switch tools. Review spend per retained buyer each month, not just software spend as a share of gross sales.

**Complete Stack Cost & Role Directory — illustrative monthly allowances in USD**

| Job / tool | Cost basis | Owner |
| --- | --- | --- |
| MoR: Lemon Squeezy / Paddle; or Stripe | Variable transaction fees; quote separately | Owner |
| Meta CAPI / Google Enhanced Conversions | $20–100 hosting; labor extra | Engineer |
| PostHog / Plausible | $0–100; choose by telemetry need | Engineer |
| Beehiiv / ConvertKit (Kit) | $0–150; list dependent | Lifecycle |
| Site, calculator directory, benchmarks | $20–100 hosting | Editor |
| Manifest V3 Chrome utility | $0–50 hosting; build labor extra | Engineer |
| US B2B identity resolution | $200–1,000 trial ceiling; optional | Lifecycle |
| Ledger, backups, secret storage | $20–100 | Engineer |
| Search citation sampling | $0–100; manual first | Editor |

## 2. Repair measurement without inventing attribution  `🏷️ OPERATING_FRAMEWORK`

Server side delivery repairs part of the measurement gap caused by browser limits; it does not restore permission or identify every lost visitor. Safari ITP limits tracking, while iOS app tracking restrictions are a related but distinct constraint. Use a signed checkout webhook as the paid order source. Send eligible purchase events to Meta CAPI with a stable event ID shared by the browser event for deduplication. Configure Google Enhanced Conversions through a supported integration with properly normalized, hashed first party customer fields where permitted. Keep the platform's order or transaction key and test its duplicate rules separately. Hashing is not anonymization. Never forward card data, private form text, or identifiers collected for a purpose that does not support advertising measurement under your stated practices.

Choose PostHog when product events, cohorts, and controlled experiments justify its configuration work. Choose Plausible when aggregate acquisition and a small set of conversion goals answer the question. Neither tool replaces the accounting ledger. Define view, calculator completion, checkout start, paid order, activation, refund, and repeat purchase before adding events. Exclude staff and test orders. Join transactions through an opaque internal key rather than putting customer emails in URLs. Reconcile daily counts and value totals against the checkout source, then investigate missing events and duplicates. Track server acceptance and platform reporting separately: an accepted event can still be unmatched or attributed differently. Fix currency, timestamps, and refund handling before arguing about which channel deserves credit for a sale that both platforms claim as their own.

Set a common reporting window and keep click based, view based, and self reported attribution in separate columns. Compare cohorts on retained revenue after the refund window, not launch day receipts. Use Beehiiv or ConvertKit to separate leads by useful actions such as completing a calculator, buying a pack, or using an update. Keep unsubscribe and suppression state synchronized across imports. A purchase does not automatically create permission for every email use in every market. Test one segment against a holdout when list size permits, and include the cost of editorial labor. If a campaign raises attributed sales but leaves total retained orders unchanged, it may be claiming demand rather than creating it. Keep the simpler sequence until incremental contribution supports a more elaborate automation tree.

**Forensic attribution and distribution checks**

| Naive Trap | Detection Metric | Durable Operator Fallback |
| --- | --- | --- |
| Server delivery restores every lost identity | Unmatched events; ledger discrepancy | Report unresolved orders separately; honor collection limits |
| Both platforms earned the same sale | Attributed orders exceed ledger orders | Deduplicate orders; retain separate attribution views |
| Extension installs equal demand | Task completion and retained purchase rates | Improve the free task; measure voluntary offer clicks |
| Identity match equals qualified buyer | False matches, complaints, research cost | Verify company accounts and carry suppression forward |
| Search citations guarantee revenue | Citation frequency versus retained referrals | Publish reproducible evidence and measure downstream orders |

## 3. Turn one Chrome micro-step into qualified demand  `🏷️ OPERATING_FRAMEWORK`

The chrome_extension_contextual_arbitrage play starts with a task, not an advertising slot. Build a free Manifest V3 utility that fixes one repeated workflow step: clean a pasted CSV, format a project brief, or check a pricing formula. Run locally where possible, use narrowly scoped permissions, and request access only for the feature being used. Keep executable code in the reviewed package rather than downloading remote code to change behavior. A user who finishes the free task can see a relevant $49–$149 Pro template or pack that completes the next step. The free result must remain useful without purchase. Put the offer in the extension's own interface, not as an injected replacement for another site's checkout, search results, or affiliate links. Measure the usefulness of the tool before expanding its pitch.

Attribution belongs on a deliberate click from the utility to your landing page. Use a campaign code that describes the tool version, not the user's browsing history. Zero cookie-stuffing means no hidden affiliate requests, forced redirects, silent cart actions, or background clicks. Never read unrelated tabs to guess buying intent. Explain any data transfer in the store listing and interface, and keep telemetry proportional to the promised function. Count successful task completions, voluntary offer clicks, retained purchases, and support tickets by release. Installs are a weak denominator because many extensions sit unused. A smaller utility with two hundred weekly users solving the same problem can teach more than ten thousand installs gathered from a broad giveaway. Price maintenance, browser changes, and store review delays into the channel's acquisition cost.

Start with one supported input and a clear error message for unsupported data. Test empty input, malformed rows, large files, offline use, and revoked permissions before publishing. Keep API keys out of the extension package; use a backend only when a feature genuinely needs it. If a paid pack requires a license, verify access without collecting the user's complete browsing activity. Offer an export of the useful free result so the tool does not become a hostage mechanism. Record the exact release associated with each campaign code, then compare retained contribution across versions. Remove a pitch that raises clicks while increasing refunds. The best distribution asset becomes a trusted part of a workflow; the paid product earns its position by reducing the next block of work rather than making the free tool deliberately frustrating.

**SOP — Standard Operating Procedure**

1. Pick the micro-step
   - Observe five target users.
   - Choose one repeated task with an exportable result.
2. Build the utility
   - Ship a local Manifest V3 prototype.
   - Document each permission and test revoked access.
3. Add the next step
   - Link a relevant $49–$149 pack.
   - Use a visible voluntary click and a release campaign code.
4. Reconcile the cohort
   - Review retained sales after refunds.
   - Subtract support, build amortization, and channel costs.

## 4. Resolve B2B identity narrowly, then earn the outreach  `🏷️ OPERATING_FRAMEWORK`

The identity_graph_pixel_arbitrage play belongs on selected high ticket B2B product pages, not a general audience site. Begin with company level signals and information visitors knowingly supply. A first party endpoint can route data into an identity service, but the endpoint's domain does not make the service first party or make its output accurate. US geofencing narrows the operating scope; it does not establish a visitor's residence or remove state privacy duties. Exclude sensitive pages, minors, and consumer profiles. Record the source of each match, its confidence, the purpose of collection, and the recipient. If the vendor cannot explain where contact data came from or support deletion, do not route that data into outreach. A guessed person is not a lead simply because a dashboard assigns a name.

For covered businesses, California Civil Code section 1798.100 addresses notice at collection, purpose and proportionality limits, retention disclosures, and contracts for covered disclosures. Other CCPA provisions govern rights and sale or sharing opt outs; a geofence is not a substitute for that analysis. Keep the actual data path documented and honor applicable choices before exporting a record. Prefer a business address linked to a verified company rather than a home address inferred from a household graph. Route qualified accounts to restrained direct mail or manual LinkedIn outreach consistent with the platform's terms. Do not scrape private profiles or automate unsolicited message floods. Suppression must follow the account through the matching vendor, CRM, and campaign exports, including later imports that would otherwise restore a previously removed contact record.

Write outreach around the company's public workflow problem, never a claim that you watched a named person browse a page. Offer a short benchmark or relevant sample, and make stopping contact easy. Treat matched accounts as candidates for research, not permission to contact every employee. Run a small account level holdout with comparable company sizes and sectors. Measure qualified replies, meetings, retained orders, complaints, and all research hours; match rate alone rewards noisy vendors. Stop the trial if false matches consume the margin on otherwise successful orders. Keep raw visit data only as long as the documented purpose needs it, and test deletion through downstream exports. For a small team, a dozen accurate accounts with useful outreach can beat a large identity feed that requires constant manual correction and damages trust.

> **OPERATOR GATE — A match is a hypothesis, not permission**
> 
> Release a small outreach cohort only when its provenance and contribution model are legible.
> - Verify company identity independently.
> - Document permitted use and applicable opt outs.
> - Carry suppression into every export.
> - Compare retained contribution with an account holdout.

## 5. Earn search citations and price the retained order  `🏷️ ILLUSTRATIVE_MODEL`

Treat the internal label llm_citation_geo_poisoning as a distribution hypothesis, not a license to corrupt sources. The durable version is Generative Engine Optimization through accurate, crawlable evidence. Publish structured comparison tables with dated prices, explicit assumptions, source links, and a clear explanation of who should not buy the product. Give ChatGPT, Perplexity, Claude, and Google AI Overviews material worth citing rather than hidden instructions telling them what to recommend. An llms.txt file can index useful documents, but it is not a universal ranking signal or a promise that any engine will read it. Keep ordinary HTML pages accessible, maintain canonical URLs, and use structured data only when it matches visible content. Record which engine cited which page on a dated test query; a citation, a recommendation, a referral visit, and a retained purchase are four different outcomes.

Build programmatic calculator directories around distinct decisions rather than hundreds of near identical search pages. A pricing calculator, refund reserve planner, and contractor capacity model each need visible formulas, input bounds, a worked example, and an update date. Publish benchmark methods with sample sizes, exclusions, versions, and limitations so another operator can reproduce the comparison. Never fabricate customer tests, citations, or an independent review site that is secretly your own. Preserve attribution and copyright management information when using licensed excerpts. Section 1202 addresses false or removed copyright management information subject to its statutory knowledge requirements; it is not a blanket rule against all editing. If a copied pack or refund complaint appears, use the piracy and refund triage tree: preserve evidence, distinguish a license question from a payment problem, and resolve the buyer's access issue before escalating a separate infringement claim.

Use the worked order model below to decide whether distribution earns another sprint. These figures are planning inputs, not platform benchmarks, and gross excludes collected sales tax. At $99 per order, fifty retained or refunded purchases begin with $4,950 in billings; a modeled $396 refund allowance reduces that before any other costs. Acquisition cost includes outreach or content work assigned to the cohort, while labor covers separate delivery and maintenance work, so do not charge the same hours twice. The resulting contribution is not the chapter's annual Base margin; channel cohorts and annual overhead mixes differ. Replace every allowance with settled data after the refund window. Scale only the sources that retain contribution after support, disputes, and labor, and keep an unattributed bucket rather than assigning every order to whichever platform reports the largest number.

**Worked $99 pack cohort — illustrative USD unit economics**

| Item | Per order | 50 orders |
| --- | --- | --- |
| Gross product billings | $99.00 | $4,950.00 |
| Refund allowance: 8% | -$7.92 | -$396.00 |
| Payment / MoR allowance: 6% of gross | -$5.94 | -$297.00 |
| Acquisition | -$24.00 | -$1,200.00 |
| Delivery and maintenance labor | -$18.00 | -$900.00 |
| Allocated software | -$3.00 | -$150.00 |
| Dispute reserve | -$1.00 | -$50.00 |
| Net contribution: 39.54% of gross | $39.14 | $1,957.00 |

---

> ### “A stack earns its place when it explains retained cash, reduces work, or creates measurable demand; a prettier attribution story does none of those things.”

## Action Checklist

- [ ] Compare MoR and processor costs on twenty actual orders.
- [ ] Reconcile one paid order, duplicate webhook, and refund.
- [ ] Assign a maintainer and spending cap to every tool.
- [ ] Prototype one local Chrome workflow with a $99 Pro link.
- [ ] Document B2B identity provenance and outreach suppression.
- [ ] Publish one reproducible benchmark and schedule citation sampling.

## Statutory & Primary Authorities

1. Cal. Civ. Code section 1798.100: Covered businesses: collection notice, purpose limits, retention, and recipient contracts. — <https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV>
2. Chrome Web Store Developer Program Policies: Extension permissions, user data use, disclosures, and deceptive behavior. — <https://developer.chrome.com/docs/webstore/program-policies/policies>
3. 17 U.S.C. section 1202: Copyright management information protections, subject to statutory knowledge requirements. — <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title17-section1202&num=0&edition=prelim>

## Sources

1. Stripe vs Lemon Squeezy vs Paddle (2026): Which Should You Use? (SoloBuild) — SoloBuild @ [00:07:58]: Last, decide whether you need the extras. Lemon Squeezy bundles a store and affiliate tools, and Paddle bundles billing support. And if you sell one digital product, our earlier video on Gumroad, Stan Store, and Payhip covers the all-in-one stores. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=i05UCC3UvNY&t=478s>
2. NEW* Paddle vs FastSpring — Best Checkout & Tax for Digital Products (How2Genius) — How2Genius @ [00:03:01]: Fastspring also integrates with popular CRM and marketing tools, helping you automate workflows from purchase to onboarding. If your main goal is quick setup, automatic US and Canadian tax handling, and easy subscription management, Paddle is the better choice. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=Y5VXhUB7aNM&t=181s>
3. Stripe Just KILLED Paddle and Gumroad (Managed Payments) (TechWealth Hub) — TechWealth Hub @ [00:00:34]: Europe, handling GST in Australia, managing chargebacks and disputes, and dealing with fraud. It's a nightmare, especially if you're a solo developer or small team. That's why services like Paddle, Gumroad, and Lemon Squeezy existed. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=KRdWGDk-GkY&t=34s>
4. Lemon Squeezy Vs Stripe Checkout Vs Paddle (2026) Which One Is Better? (Tutorly) — Tutorly @ [00:02:40]: If your customers include larger companies with specific billing requirements, Paddle provides tools that support more complex payment situations. Lemon Squeezy charges the same base fee of 5% plus 50 cents. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=IfaCBBIoVK0&t=160s>
5. Skool vs Circle (2026): The Best Online Communities & Courses? (Click Guide) — Click Guide @ [00:01:23]: The business at $199 per month, provides workflows and automations and API access. Enterprise plan comes at $419 per month, and it has advanced analytics, lower transaction fees of 1%. The plus plan comes at a custom pricing. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=F5Le0mxyMhg&t=83s>
6. How to Sell Notion Templates on Gumroad (2026 Revenue Snapshot) (Tutorials At Desk) — Tutorials At Desk @ [00:03:39]: Then choose your account type, usually either individual or business, depending on how you're operating. After that, follow the on-screen instructions to connect a supported payout method such as Stripe or PayPal, depending on what Gumroad offers in your region. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=VEFf-FR0dxw&t=219s>
7. Stripe's Merchant of Record (MoR) Solution: Adding Managed Payments to an Existing App  #mcp (Stephen S.) — Stephen S. @ [00:00:55]: Now if I come down here to the MCP servers, I can see that the Stripe MCP is there. And for this, I'm going to authorize, jump back into Curo, and now I can see that I have access to all of these tools. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=F-WZgXuQIuQ&t=55s>
8. Are Free Skool Communities Dying? Why I Turned Mine Paid (Doug Boughton) — Doug Boughton @ [00:12:29]: Um and I've built a tool around this. It's called Event Stack AI. Uh I sell this tool for up to $299 a month for the highest plan. My clients get it for free. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=8lz_gy-Osw8&t=749s>
9. Stripe Managed Payments: The Threat to Paddle and the Future of MoR (Captain Vova (Vova Feldman)) — Captain Vova (Vova Feldman) @ [00:01:49]: Whether you've been following the events or not, last year Stripe acquired payment solution called Lemon Squeezy, a Merchant of Record actually. And the question that is kind of inevitable is are they going to sunset that solution? — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=5zGuxRrg_O0&t=109s>
10. Paddle vs LemonSqueezy (2026) | Which One is Better? (houdztech) — houdztech @ [00:02:42]: Lemon Squeezy is designed for simplicity. The UI is clean, modern, and genuinely easy to navigate. Setup takes 15 to 30 minutes. They have built-in email marketing, affiliate management, and a no code storefront builder. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=Qq-EyvVj7IM&t=162s>
11. How To Make & Sell Notion Templates (Make $1000+ MONTH!) (Bree and Steve) — Bree and Steve @ [00:05:32]: So I'm going to hit new database and I'm going to go ahead and resize this so we're gonna go in and do is add the different habits that you would like to track so this can be really anything I'm just gonna go ahead and list a couple of random ones. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=zmw7OXf39rQ&t=332s>
12. How to launch your SELF-LIQUIDATING OFFER Funnel (with real-world examples!) (Pete McPherson DYEB) — Pete McPherson DYEB @ [00:18:59]: This is a tool that you can use ASAP. Next to go through a bump offer and then an upsell. It could be the systems and strategies that are related to the tools. And actually, this is an important point that I didn't mention earlier. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=wYKYVjEiqLY&t=1139s>
13. How to Do Surplus Funds in Georgia (Step-by-Step Guide) (Money Making Juggernaut) — Money Making Juggernaut @ [00:02:45]: You guys can see here, just a very basic Google search can give us access to many counties across the entire state of Georgia. We can also use Excess Elite. Excess Elite is the number one leading database provider. They also have a CRM that allows you to market. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=FJj3hN2KbIg&t=165s>
14. How to start selling your Framer templates through Lemon Squeezy (Framer) — Framer @ [00:03:43]: Twitter or share it anywhere you want so you can copy this share it wherever you want and then that is how you start selling your templates through lemon squeezy thanks for watching. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=RN0VWAvL-qc&t=223s>
15. Getting Started with Digital Preservation: Fixity Pro (ScottishArchivesTV) — ScottishArchivesTV @ [00:05:07]: You to run a manual scan make sure that manual only is selected under schedule the scan if you set up an email address to send your reports to you can enter it now by clicking add report recipient email entering your email address and clicking add. — Attributed practitioner commentary on analytics, first-party attribution pixels, email/co-reg engines, Chrome micro-tools, and GEO citation visibility. — <https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=307s>
16. Getting Started with Digital Preservation: Fixity Pro — ScottishArchivesTV @ [00:04:48]: To run then click the save project button and when you're if your PC is on and fix it to open at the specified day and time the scan will run for you to run a manual scan make sure that manual only is selected under schedule the scan if you set up an email address to send your reports to you can enter it now by clicking add report recipient email entering your email address. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=288s>
17. Getting Started with Digital Preservation: Fixity Pro — ScottishArchivesTV @ [00:00:00]: Regrid acquisition and import — spatial scope and licensed dataset — Choose state/county coverage and inspect County Coverage Report plus Parcel Schema/Data Dictionary. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=0s>
18. Getting Started with Digital Preservation: Fixity Pro — ScottishArchivesTV @ [00:00:00]: Spatial filtering and API integration — parcel dataset and selection criteria — Combine attribute predicates with explicit spatial predicates such as intersects or within. — Matched source commentary; not independent verification or legal authority. — <https://www.youtube.com/watch?v=1pRY7lpZ7nA&t=0s>
